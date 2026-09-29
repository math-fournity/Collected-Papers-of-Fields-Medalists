## A NEW PROOF OF SZEMEREDI’S THEOREM <sup>´</sup>

## W.T. Gowers

## Contents

1 Introduction 466  
2 Uniform Sets and Roth's Theorem 470  
3 Higher-degree Uniformity 477  
4 Two Motivating Examples 485  
5 Consequences of Weyl's Inequality 489  
6 Somewhat Additive Functions 498  
7 Variations on a Theorem of Freiman 501  
8 Progressions of Length Four 510  
9 Obtaining Approximate Homomorphisms 514  
10 Properties of Approximate Homomorphisms 518  
11 The Problem of Longer Progressions 533  
12 Strengthening a Bihomomorphism 535  
13 Finding a Bilinear Piece 542  
14 Obtaining Many Respected Arrangements 553  
15 Increasing the Density of Respected Arrangements 560  
16 Finding a Multilinear Piece 566  
17 The Main Inductive Step 576  
18 Putting Everything Together 583  
Concluding Remarks and Acknowledgements 586  
References 587

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">The research for this article was carried out in part for the Clay Mathematics Institute.</span></small>

## 1 Introduction

In 1927 van der Waerden published a celebrated theorem, which states that if the positive integers are partitioned into finitely many classes, then at least one of these classes contains arbitrarily long arithmetic progressions. This is one of the fundamental results of Ramsey theory, and it has been strengthened in many diferent directions. A more precise statement of the theorem is as follows.

Theorem 1.1. Let k and r be positive integers. Then there exists a positive integer$M = M ( k , r )$such that, however the set$\{ 1 , 2 , \ldots , M \}$is partitioned into r subsets, at least one ofthe subsets contains an arithmetic progression of length k.

It is natural to wonder how quickly the least such M grows as a function of$k$and$r ,$but this has turned out to be a surprisingly dificult question. The original proof of van der Waerden bounds M above by an Ackermanntype function in$k ,$even when$r = 2$, and it was a major advance when Shelah, in 1987, gave the first primitive recursive upper bound (with a beautifully transparent proof). His bound can be described as follows. Define a tower function$T$inductively by letting$T ( 1 ) = 2$and$T ( k ) = 2 ^ { T ( k - 1 ) }$ for$k > 1$. Then define a function W by$W ( 1 ) = 2$and$W ( k ) = T ( W ( k - 1 ) )$ for$k > 1$. Shelah obtained a bound of the form$M ( k , 2 ) \leqslant W ( C k )$(with C an absolute constant). Although this was a huge improvement on the pre-vious bound, it still left an enormous gap, as the best known lower bound was, and still is, exponential in k.

A strengthening of a completely diferent kind was conjectured by Erd˝os and Tur´an in 1936. They realised that it ought to be possible to find arithmetic progressions of length k in any suficiently dense set of integers, which would show that the colouring in van der Waerden’s theorem was, in a sense, a distraction. The translation-invariance of the notion of an arithmetic progression rules out simple counterexamples to this stronger statement. (One can contrast this situation with a theorem of Schur which states that in any finite colouring of N there are solutions of the equation $x + y = z$with$x , y$and z all of the same colour. However, the set of all odd integers has density$1 / 2$and contains no solutions.) The conjecture was proved by Szemer´edi in 1974. Szemer´edi’s theorem, which we now state precisely, is one of the milestones of combinatorics.

Theorem 1.2. Let k be a positive integer and let$\delta > 0$. There exists a positive integer$N = N ( k , \delta )$such that every subset of the set$\{ 1 , 2 , \ldots , N \}$ of size at least δN contains an arithmetic progression of length k.

It is very simple to see that this result strengthens van der Waerden’s theorem, and that$M ( k , r )$can be chosen to be$N ( k , r ^ { - 1 } )$.

A second proof of Szemer´edi’s theorem was given by Furstenberg in 1977, using ergodic theory, which provides an extremely useful conceptual framework for discussing the result. This proof was also a major breakthrough, partly because of the dificulty of Szemer´edi’s original proof, and partly because Furstenberg’s techniques have since been extended to prove many natural generalizations of the theorem which do not seem to follow from Szemer´edi’s approach. These include a density version of the Hales-Jewett theorem [FK] and a “polynomial Szemer´edi theorem” [BL].

Why then, if there are already two proofs of Szemer´edi’s theorem, should one wish to find a third? There are several related reasons.

First of all, it is likely that Erd˝os and Tur´an, when they made their original conjecture, hoped that it would turn out to be the “real” theorem underlying van der Waerden’s theorem, and perhaps for that reason have an easier proof. If they did, then their hope has not been fulfilled, as all known proofs are long and complicated. Szemer´edi’s original paper runs to 47 pages, full of intricate combinatorial arguments, and it takes a few seconds even to check that the diagram near the beginning of the dependences between the various lemmas really does indicate a valid proof. Furstenberg’s proof is considerably simpler (especially as presented in [FKO]), but requires a certain initial investment in learning the necessary definitions from ergodic theory, and is still significantly harder than the proof of van der Waerden’s theorem. (On the positive side, some of the ideas of Szemer´edi’s proof, most notably the so-called regularity lemma, have turned out to be extremely useful in many other contexts, and, as mentioned above, Furstenberg’s proof has been the starting point of a great deal of further research.)

Second, Erd˝os and Tur´an gave as the main motivation for their conjecture the likelihood that in order to prove it one would be forced not to use the sorts of arguments that led to such weak bounds for van der Waerden’s theorem, and would therefore obtain far better estimates. However, this hope was not fulfilled by Szemer´edi’s proof because he used van der Waerden’s theorem in his argument. He also used the regularity lemma just mentioned, which makes a tower-type contribution to the size of the bound from any argument that uses it. (See [G1] for a proof that this is necessary.) Furstenberg’s proof gives no bound, even in principle, as it uses the axiom of choice. Moreover, although van der Waerden’s theorem is not directly applied, it is likely that any attempt to make the argument quantitative would lead to rapidly growing functions for similar reasons.

Third, there is a possibility left open by the first result in the direction of Szemer´edi’s theorem, the assertion for progressions of length three, which was proved by Roth [R1]. Roth gave a beautiful argument using exponential-sum estimates, but his approach seemed not to generalize. Indeed, progress was made on the problem only when Szemer´edi found a different, more combinatorial argument for progressions of length three which was more susceptible to generalization. However, it is highly desirable to find an exponential-sums argument for the general case, because all the best bounds for similar problems have come from these techniques rather than purely combinatorial ones [Sz3], [H-B], [Bou]. (Although Roth used ideas from Szemer´edi’s proof for progressions of length four [S1] and combined them with analytic techniques to give a second proof for that case [R2], the argument is not really a direct generalization of his earlier proof, and relies on van der Waerden’s theorem.)

Fourth, there are certain important conjectures related to Szemer´edi’s theorem, and the existing arguments get nowhere near to them. The most famous is Erd˝os’s conjecture that every set X of positive integers such that $\textstyle \sum _ { x \in X } x ^ { - 1 }$diverges contains arbitrarily long arithmetic progressions. Since the set of primes has this property, a positive solution to the conjecture would answer an old question in number theory using no more about the primes than the fact that they are reasonably dense. Even if the conjecture turns out to be too optimistic, there is a resemblance between Roth’s proof and the result of van der Corput (adapting the proof of Vinogradov’s three-primes theorem) that the primes contain infinitely many arithmetic progressions of length three, which suggests that generalizing Roth’s proof to longer progressions could at least lead to a number-theoretic proof that the primes contain arbitrarily long arithmetic progressions.

In this paper, we show that Roth’s argument can be generalized, and that this does indeed result in a significant improvement to the bounds, even for van der Waerden’s theorem. Our main result (restated in equivalent form later as Theorem 18.2) is the following.

Theorem 1.3. For every positive integer k there is a constant$c = c ( k ) >$ 0 such that every subset of$\{ 1 , 2 , \ldots , N \}$of size at least$N ( \log \log N ) ^ { - c }$ contains an arithmetic progression of length k. Moreover, c can be taken to be$2 ^ { - 2 ^ { k + 9 } }$

This immediately implies an estimate for$N ( k , \delta )$which is doubly exponential in$\delta ^ { - 1 }$and quintuply exponential in k.

There are, however, some serious dificulties in carrying out the generalization, as we shall demonstrate with examples later in the paper. This perhaps explains why the generalization has not been discovered already. Very roughly, our strategy is to reduce the problem to what is known as an inverse problem in additive number theory (deducing facts about the structure of a set of numbers from properties of its set of sums or diferences). We then apply a variant of a famous inverse result due to Freiman [F1,2]. Freiman’s proof of his theorem is very complicated, though it has recently been considerably tidied up by Bilu [Bi]. A very much simpler proof of Freiman’s theorem was recently given by Ruzsa [Ru1,2], and to him we owe a huge mathematical debt. His methods have inspired many parts of this paper, including several arguments where his results are not quoted directly.

It has to be admitted that this paper is actually longer than those of Szemer´edi and Furstenberg, and less self-contained. This is partly because my overriding priority when writing it has been to make the basic ideas as clear as possible, even if this adds several pages. Many results are proved first in a special case and later in full generality. This is intended to make it as easy as possible to read about progressions of length four and five, which involve most of the interesting ideas but by no means all of the technicalities. (The special case of progressions of length four was covered in an earlier paper [G2] but it is treated here as well, and a better bound, claimed in the earlier paper, is here proved in full.) Sections 4 and 11 are devoted to examples showing that certain simpler arguments do not work. They are therefore not logically necessary. However, the whole of the rest of the paper is, in a sense, a response to those examples. Another priority has been to make the sections as independent as possible. Where it is essential that one section depends on another, we have tried to make it depend on a single clearly stated result, in the hope that readers will if they wish be able to understand the broad outline of the proof without following the details.

Despite these eforts, the quickest way to understand a proof of Szemer´edi’s theorem is probably still to read the paper of Furstenberg, Katznelson and Ornstein [FKO] mentioned earlier. However, the proof in this paper gives quantitative information, and I hope that at least some mathematicians, particularly those with a background in additive number theory, will find the approach a congenial one.

## 2 Uniform Sets and Roth’s Theorem

It is not hard to prove that a random subset of the set$\{ 1 , 2 , \ldots , N \}$of cardinality$\delta N$contains, with high probability, roughly the expected number of arithmetic progressions of length$k ,$that is,$\delta ^ { k }$times the number of such progressions in the whole of$\{ 1 , 2 , \ldots , N \}$. A natural idea is therefore to try to show that random sets contain the fewest progressions of length$k ,$which would then imply Szemer´edi’s theorem. In view of many other examples in combinatorics where random sets are extremal, this is a plausible statement, but unfortunately it is false. Indeed, if random sets were the worst, then the value of$\delta$needed to ensure an arithmetic progression of length three would be of order of magnitude$N ^ { - 2 / 3 }$, whereas in fact it is known to be at least$\exp ( - c ( \log N ) ^ { 1 / 2 } )$for some absolute constant$c > 0 ~ [ \mathrm { B e } ]$ (The random argument suggested above is to choose$\delta$so that the expected number of arithmetic progressions is less than one. Using a standard trick in probabilistic combinatorics, we can instead ask for the expected number to be at most$\delta N / 2$and then delete one point from each one. This slightly better argument lifts the density significantly, but still only to$c N ^ { - 1 / 2 } . )$.)

Despite this, it is tempting to try to exploit the fact that random sets contain long arithmetic progressions. Such a proof could be organized as follows.

(1) Define an appropriate notion of pseudorandomness.

(2) Prove that every pseudorandom subset of$\{ 1 , 2 , \ldots , N \}$contains roughly the number of arithmetic progressions of length k that you would expect.

(3) Prove that if$A \subset \{ 1 , 2 , \ldots , N \}$has size δN and is not pseudorandom, then there exists an arithmetic progression$P \subset \{ 1 , 2 , \dotsc , N \}$with length tending to infinity with$N .$, such that$| A \cap P | \geqslant ( \delta + \epsilon ) | P |$, for some$\epsilon > 0$that depends on δ (and k) only.

If these three steps can be carried out, then a simple iteration proves$\mathrm { S z e - }$ mer´edi’s theorem. As we shall see, this is exactly the scheme of Roth’s proof for progressions of length three.

First, we must introduce some notation. Throughout the paper we shall be considering subsets of$\mathbb { Z } _ { N }$rather than subsets of$\{ 1 , 2 , \ldots , N \}$. It will be convenient (although not essential) to take$N$to be a prime number. We shall write$\omega$for the number$\exp ( 2 \pi i / N )$. Given a function$f : \mathbb { Z } _ { N } \to \mathbb { C }$ and$r \in \mathbb { Z } _ { N }$we set

$$
\hat {f} (r) = \sum_ {s \in \mathbb {Z} _ {N}} f (s) \omega^ {- r s}.
$$

The function$\hat { f }$is the discrete Fourier transform of$f .$. (In most papers in analytic number theory, the above exponential sum is written$\textstyle \sum _ { s = 1 } ^ { N } \bar { e } ( - r s / N )$, or possibly$\begin{array} { r } { \sum _ { s = 1 } ^ { N } e _ { N } ( - r s ) . ) } \end{array}$Let us write$f$∗$g$for the function

$$
f * g (s) = \sum_ {t \in \mathbb {Z} _ {N}} f (t) \overline {{g (t - s)}}.
$$

(This is not standard notation, but we shall have no use for the convolution $\sum f ( t ) g ( s - t )$in this paper, so it is very convenient.) From now on, all sums will be over$\mathbb { Z } _ { N }$unless it is specified otherwise. We shall use the following basic identities over and over again in the paper.

$$
(f * g) ^ {\wedge} (r) = \hat {f} (r) \overline {{\hat {g} (r)}},\tag{1}
$$

$$
\sum_ {r} \hat {f} (r) \overline {{\hat {g} (r)}} = N \sum_ {s} f (s) \overline {{g (s)}},\tag{2}
$$

$$
\sum_ {r} | \hat {f} (r) | ^ {2} = N \sum_ {s} | f (s) | ^ {2},\tag{3}
$$

$$
f (s) = N ^ {- 1} \sum_ {r} \hat {f} (r) \omega^ {r s}.\tag{4}
$$

Of these, the first tells us that convolutions transform to pointwise products, the second and third are Parseval’s identities and the last is the inversion formula. To check them directly, note that

$$
\begin{array}{l} (f * g) (r) = \sum_ {s} (f * g) (s) \omega^ {- r s} \\ \qquad = \sum_ {s, t} f (t) \overline {{g (t - s)}} \omega^ {- r t} \omega^ {r (t - s)} \\ \qquad = \sum_ {t, u} f (t) \omega^ {- r t} \overline {{g (u) \omega^ {- r u}}} \\ \qquad = \hat {f} (r) \overline {{\hat {g} (r)}}, \end{array}
$$

which proves (1). We may deduce (2), since

$$
\sum_ {r} \hat {f} (r) \overline {{\hat {g} (r)}} = \sum_ {r} \sum_ {s} f * g (s) \omega^ {- r s} = N f * g (0) = N \sum_ {s} f (s) \overline {{g (s)}},
$$

where for the second equality we used the fact that$\sum _ { \mathbf { \boldsymbol { s } } } \omega ^ { - r s }$is N if$r = 0$ and zero otherwise. Identity (3) is a special case of (2). Noting that the function$r \mapsto \omega ^ { - r s }$is the Fourier transform of the characteristic function of the singleton$\{ s \}$, we can deduce (4) from (2) as well (though it is perhaps more natural just to expand the right-hand side and give a direct proof).

There is one further identity, suficiently important to be worth stating as a lemma.

Lemma 2.1. Let f and g be functions from$\mathbb { Z } _ { N }$to$\mathbb { C } .$. Then

$$
\sum_ {r} | \hat {f} (r) | ^ {2} | \overline {{\hat {g} (r)}} | ^ {2} = N \sum_ {t} \Big | \sum_ {s} f (s) \overline {{g (s - t)}} \Big | ^ {2}.\tag{5}
$$

Proof. By identities (1) and (2),

$$
\begin{array}{r l} \sum_ {r} | \hat {f} (r) | ^ {2} | \overline {{\hat {g} (r)}} | ^ {2} & = \sum_ {r} \bigl | (f * g) ^ {\wedge} (r) \bigr | ^ {2} \\ & = N \sum_ {t} \bigl | f * g (t) \bigr | ^ {2} \\ & = N \sum_ {t, s, u} f (s) \overline {{g (s - t) f (u)}} g (u - t) \\ & = N \sum_ {t} \Bigl | \sum_ {s} f (s) \overline {{g (s - t)}} \Bigr | ^ {2} \end{array}
$$

as required.

Setting$f = g$and expanding the right-hand side of (5), one obtains another identity which shows that sums of fourth powers of Fourier coeficients have an interesting interpretation.

$$
\sum_ {r} | \hat {f} (r) | ^ {4} = N \sum_ {a - b = c - d} f (a) \overline {{f (b) f (c)}} f (d).\tag{6}
$$

It is of course easy to check this identity directly.

Nearly all the functions in this paper will take values with modulus at most one. In such a case, one can think of Lemma 2.1 as saying that if $f$has a large inner product with a large number of rotations of g, then$f$ and$g$must have large Fourier coeficients in common, where large means of size proportional to N. We shall be particularly interested in the Fourier coeficients of characteristic functions of sets$A \subset \mathbb { Z } _ { N }$of cardinality δN, which we shall denote by the same letter as the set itself. Notice that identity (6), when applied to (the characteristic function of) a set A, tells us that the sum$\textstyle \sum _ { r } | { \hat { A } } ( r ) | ^ { 4 }$is N times the number of quadruples$( a , b , c , d ) \in$ $A ^ { 4 }$such that$a - b = c - d .$

For technical reasons it is also useful to consider functions of mean zero. Given a set A of cardinality δN, let us define the balanced function of A to be$f _ { A } : \mathbb { Z } ^ { N } \longrightarrow [ - 1 , 1 ]$where

$$
f _ {A} (s) = \left\{ \begin{array}{l l} 1 - \delta & s \in A \\ - \delta & s \notin A. \end{array} \right.
$$

This is the characteristic function of A minus the constant function δ1. Note that$\textstyle \sum _ { s \in \mathbb { Z } _ { N } } f _ { A } ( s ) = { \hat { f } } _ { A } ( 0 ) = 0$and that$\hat { f } _ { A } ( r ) = \hat { A } ( r )$for$r \neq 0$

We are now in a position to define a useful notion of pseudorandomness. The next lemma (which is not new) gives several equivalent definitions involving constants$c _ { i }$. When we say that one property involving$c _ { i }$implies another involving$c _ { j }$, we mean that if the first holds, then so does the second for a constant$c _ { j }$that tends to zero as$c _ { i }$tends to zero. (Thus, if one moves from one property to another and then back again, one does not necessarily recover the original constant.) From the point of view of the eventual bounds obtained, it is important that the dependence is no worse than a fixed power. This is always true below.

In this paper we shall use the letter D to denote the closed unit disc in C (unless it obviously means something else).

Lemma 2.2. Let f be a function from$\mathbb { Z } _ { N }$to D. The following are equivalent.

(i)$\begin{array} { r } { \sum _ { k } \mathopen { } \mathclose \bgroup \left| \sum _ { s } f ( s ) \overline { { f ( s - k ) } } \aftergroup \egroup \right| ^ { 2 } \leqslant c _ { 1 } N ^ { 3 } . } \end{array}$

(ii)$\begin{array} { r } { \sum _ { a - b = c - d } f ( a ) \overline { { f ( b ) f ( c ) } } f ( d ) \leqslant c _ { 1 } N ^ { 3 } . } \end{array}$

(iii)$\begin{array} { r } { \sum _ { r } | \hat { f } ( r ) | ^ { 4 } \leqslant c _ { 1 } N ^ { 4 } } \end{array}$

(iv) max<sub>r</sub>$| \hat { f } ( r ) | \leqslant c _ { 2 } N$

(v)$\begin{array} { r } { \sum _ { k } \mathopen { } \mathclose \bgroup \left| \sum _ { s } f ( s ) \overline { { g ( s - k ) } } \aftergroup \egroup \right| ^ { 2 } \leqslant c _ { 3 } N ^ { 2 } \mathopen { } \mathclose \bgroup \left\| g \aftergroup \egroup \right\| _ { 2 } ^ { 2 } } \end{array}$for every function$g : \mathbb { Z } _ { N } \to \mathbb { C }$

 Proof. The equivalence of (i) and (ii) comes from expanding the left-hand side of (i), and the equivalence of (i) and (iii) follows from identity (6) above. It is obvious that (iii) implies (iv) if$c _ { 2 } \geqslant c _ { 1 } ^ { 1 / 4 }$. Since

$$
\sum_ {r} | \hat {f} (r) | ^ {4} \leqslant \max _ {r} | \hat {f} (r) | ^ {2} \sum_ {r} | \hat {f} (r) | ^ {2} \leqslant N ^ {2} \max _ {r} | \hat {f} (r) | ^ {2},
$$

we find that (iv) implies (iii) if$c _ { 1 } \geqslant c _ { 2 } ^ { 2 }$. It is obvious that (v) implies (i) if $c _ { 1 } \geqslant c _ { 3 }$. By Lemma 2.1, the left-hand side of (v) is

$$
N ^ {- 1} \sum_ {r} | \hat {f} (r) | ^ {2} | \hat {g} (r) | ^ {2} \leqslant N ^ {- 1} \left(\sum_ {r} | \hat {f} (r) | ^ {4}\right) ^ {1 / 2} \left(\sum_ {r} | \hat {g} (r) | ^ {4}\right) ^ {1 / 2}
$$

by the Cauchy-Schwarz inequality. Using the additional inequality

$$
\left(\sum_ {r} | \hat {g} (r) | ^ {4}\right) ^ {1 / 2} \leqslant \sum_ {r} | \hat {g} (r) | ^ {2},
$$

we see that (iii) implies (v) if$c _ { 3 } \geqslant c _ { 1 } ^ { 1 / 2 }$

A function$f : \mathbb { Z } _ { N } \to D$satisfying condition (i) above, with$c _ { 1 } = \alpha .$, will be called α-uniform. If f is the balanced function$f _ { A }$of some set$A \subset \mathbb { Z } _ { N }$, then we shall also say that A is α-uniform. If$A \subset \mathbb { Z } _ { N }$is an α-uniform set of cardinality δN, and f is its balanced function, then

$$
\sum_ {r} | \hat {A} (r) | ^ {4} = | A | ^ {4} + \sum_ {r} | \hat {f} (r) | ^ {4} \leqslant | A | ^ {4} + \alpha N ^ {4}.
$$

We noted earlier that$\textstyle \sum _ { r } | { \hat { A } } ( r ) | ^ { 4 }$is N times the number of quadruples $( a , b , c , d ) \in A ^ { 4 }$such that$a - b = c - d .$. If A were a random set of size $\delta N$, then we would expect about$\delta ^ { 4 } N ^ { 3 } = N ^ { - 1 } | A | ^ { 4 }$such quadruples (which from the above is clearly a lower bound). Therefore, the number α is measuring how close A is to being random in this particular sense. Notice that quadruples$( a , b , c , d )$with$a - b = c - d$are the same as quadruples of the form$( x , x + s , x + t , x + s + t )$

We remark that our definition of an α-uniform set coincides with the definition of quasirandom subsets of$\mathbb { Z } _ { N }$, due to Chung and Graham. They prove that several formulations of the definition (including those of this paper) are equivalent. They do not mention the connection with Roth’s theorem, which we shall now explain. We need a very standard lemma, which we prove in slightly greater generality than is immediately necessary, so that it can be used again later. Let us define the diameter of a subset $X \subset \mathbb { Z } _ { N }$to be the smallest integer s such that$X \subset \{ n , n + 1 , \ldots , n + s \}$ for some$n \in \mathbb { Z } _ { N }$

Lemma 2.3. Let$r , s$and N be positive integers with$r , s \leqslant N$and$r s \geqslant N$2 and let$\phi : \{ 0 , 1 , \ldots , r - 1 \} \to \mathbb { Z } _ { N }$be linear$( { \mathrm { i . e . } }$, of the form$\phi ( x ) = a x + b )$. Then the set$\{ 0 , 1 , \ldots , r - 1 \}$can be partitioned into arithmetic progressions $P _ { 1 } , \ldots , P _ { M }$such that for each j the diameter of$\phi ( P _ { j } )$is at most s and the length of$P _ { j }$lies between$( r s / 4 N ) ^ { 1 / 2 }$and$( r s / N ) ^ { 1 / 2 }$

Proof. Let$t = \lceil ( r N / 4 s ) ^ { 1 / 2 } \rceil$. Of the numbers$\phi ( 0 ) , \phi ( 1 ) , \ldots , \phi ( t )$, at least two must be within$N / t$. Therefore, by the linearity of φ, we can find a non-zero$u \leqslant t$such that$| \phi ( u ) - \phi ( 0 ) | \leqslant N / t$. Split$\{ 0 , 1 , \ldots , r - 1 \}$ into congruence classes mod$u .$Each congruence class is an arithmetic progression of cardinality either$\lfloor r / u \rfloor$or$\lceil r / u \rceil$. If P is any set of at most $s t / N$consecutive elements of a congruence class, then diam$\phi ( P ) \leqslant s$. It is easy to check first that$s t / N \leqslant r / 3 t \leqslant ( 1 / 2 ) \lfloor r / u \rfloor$, next that this implies that the congruence classes can be partitioned into sets$P _ { j }$of consecutive elements with every$P _ { j }$of cardinality between$\lceil s t / 2 N \rceil$and$\lfloor s t / N \rfloor$, and finally that this proves the lemma.✷

Corollary 2.4. Let$f$be a function from the set$\{ 0 , 1 , \ldots , r - 1 \}$to the closed unit disc in$\mathbb { C } ,$let$\phi : \mathbb { Z } _ { N } \to \mathbb { Z } _ { N }$be linear and let$\alpha > 0$. If

$$
\left| \sum_ {x = 0} ^ {r - 1} f (x) \omega^ {- \phi (s)} \right| \geqslant \alpha r,
$$

then there is a partition of$\{ 0 , 1 , \ldots , r - 1 \}$into$m \leqslant ( 8 \pi r / \alpha ) ^ { 1 / 2 }$arithmetic

progressions$P _ { 1 } , \ldots , P _ { m }$such that

$$
\sum_ {j = 1} ^ {m} \left| \sum_ {x \in P _ {j}} f (x) \right| \geqslant (\alpha / 2) r
$$

and such that the lengths ofthe$P _ { j }$all lie between$( \alpha r / \pi ) ^ { \frac { 1 } { 2 } } / 4$and$( \alpha r / \pi ) ^ { \frac { 1 } { 2 } } / 2$

Proof. Let$s \leqslant \alpha N / 4 \pi$and let$m = ( 1 6 \pi r / \alpha ) ^ { 1 / 2 }$. By Lemma 2.3 we can find a partition of$\{ 0 , 1 , \ldots , r - 1 \}$into arithmetic progressions$P _ { 1 } , \ldots , P _ { m }$ such that the diameter of$\phi ( P _ { j } )$is at most s for every$j$and the length of each$P _ { j }$lies between$r / m$and$2 r / m$. By the triangle inequality,

$$
\sum_ {j = 1} ^ {m} \left| \sum_ {x \in P _ {j}} f (x) \omega^ {- \phi (x)} \right| \geqslant \alpha r.
$$

Let$x _ { j } ~ \in ~ P _ { j } .$The estimate on the diameter of$\phi ( P _ { j } )$implies that $| \omega ^ { - \phi ( \check { x } ) } - \omega ^ { - \check { \phi } ( x _ { j } ) } |$is at most$\alpha / 2$for every$x \in P _ { j }$. Therefore

$$
\begin{array}{l} \sum_ {j = 1} ^ {m} \Big | \sum_ {x \in P _ {j}} f (x) \Big | = \sum_ {j = 1} ^ {m} \Big | \sum_ {x \in P _ {j}} f (x) \omega^ {- \phi (x _ {j})} \Big | \\ \geqslant \sum_ {j = 1} ^ {m} \Big | \sum_ {x \in P _ {j}} f (x) \omega^ {- \phi (x)} \Big | - \sum_ {j = 1} ^ {m} (\alpha / 2) | P _ {j} | \\ \geqslant \alpha r / 2 \end{array}
$$

as claimed.

Corollary 2.5. Let$A \subset \mathbb { Z } _ { N }$and suppose that$| \hat { A } ( r ) | \geqslant \alpha N$for some $r \neq 0$. Then there exists an arithmetic progression$P \subset \{ 0 , 1 , \dotsc , N - 1 \}$ of length at least$( \alpha ^ { 3 } N / 1 2 8 \pi ) ^ { 1 / 2 }$such that$| A \cap P | \geqslant ( \delta + \alpha / 8 ) | P |$

Proof. Define$\phi ( x ) = r x$and let$f$be the balanced function of A (regarded as a function on$\{ 0 , 1 , \ldots , N { - } 1 \} )$. By Corollary 2.4 we can partition the set $\{ 0 , 1 , \ldots , N - 1 \}$into m$\leqslant ( 1 6 \pi N / \alpha ) ^ { 1 / 2 }$arithmetic progressions$P _ { 1 } , \ldots , P _ { m }$ of lengths between$N / m$and$2 N / m$such that

$$
\sum_ {j = 1} ^ {m} \left| \sum_ {x \in P _ {j}} f (x) \right| \geqslant \alpha N / 2.
$$

Since$\textstyle \sum _ { x \in P _ { i } } f ( x )$is real for all$j ,$, and since$\textstyle \sum _ { j = 1 } ^ { m } \sum _ { x \in P _ { j } } f ( x ) = 0$, if we define J to be the set of$j$with$\textstyle \sum _ { x \in P _ { i } } f ( x ) \geqslant 0$, we have

$$
\sum_ {j \in J} \sum_ {x \in P _ {j}} f (x) \geqslant \alpha N / 4.
$$

Therefore, we can find j such that$\textstyle \sum _ { x \in P _ { i } } f ( x ) \geq \alpha N /$4m. But$| P _ { j } | { \leqslant } 2 N / m$，so$\textstyle \sum _ { x \in P _ { i } } f ( x ) \geqslant \alpha | P _ { j } | / 8$, which implies that$| A \cap P _ { j } | \geqslant ( \delta + \alpha / 8 ) | P _ { j } |$✷

We can now give Roth’s proof of his theorem on arithmetic progressions of length three.

Theorem 2.6. Let$\delta > 0$, let$N \geqslant \exp \exp ( C \delta ^ { - 1 } )$(where C is an absolute constant) and let$A \subset \{ 1 , 2 , \ldots , N \}$be a set of size at least$\delta N$. Then A contains an arithmetic progression of length three.

Proof. Since we are passing to smaller progressions and iterating, we cannot simply assume that N is prime, so we shall begin by dealing with this small technicality. Let$N _ { 0 }$be a positive integer and let$A _ { 0 }$be a subset of $\{ 1 , 2 , \ldots , N _ { 0 } \}$of size at least$\delta _ { 0 } N _ { 0 }$

By Bertrand’s postulate (which is elementary – it would be a pity to use the full strength of the prime number theorem in a proof of Roth’s theorem) there is a prime p between$N _ { 0 } / 3$and$2 N _ { 0 } / 3$. Write q for$N _ { 0 } - p$ If$| A _ { 0 } \cap \{ 1 , 2 , \dotsc , p \} | \leqslant \delta _ { 0 } ( 1 - \delta _ { 0 } / 1 6 0 ) p$, then we know that

$$
\begin{array}{c} \big | A _ {0} \cap \{p + 1, \ldots , N _ {0} \} \big | \geqslant \delta_ {0} \big (N _ {0} - (1 - \delta_ {0} / 1 6 0) p \big) = \delta_ {0} (q + \delta_ {0} p / 1 6 0) \\ \geqslant \delta_ {0} (1 + \delta_ {0} / 3 2 0) q. \end{array}
$$

Let us call this situation case 0.

If case 0 does not hold, then let N be the prime p obtained above, let $A = A _ { 0 } \cap \left\{ 1 , \ldots , N \right\}$and let$\delta = \delta _ { 0 } ( 1 - \delta _ { 0 } / 1 6 0 )$. Let$B = A \cap \left[ N / 3 , 2 N / 3 \right)$ If$| B | \leqslant \delta N / 5$, then either$A \cap [ 0 , N / 3 )$or$A \cap [ 2 { N } / 3 , { N } )$has cardinality at least$2 \delta N / 5 = ( 6 \delta / 5 ) ( N / 3 )$. This situation we shall call case 1.

Next, let$\alpha = \delta ^ { 2 } / 1 0$and suppose that$| \hat { A } ( r ) | > \alpha N$for some non-zero r. In this case, by Corollary 2.5 there is an arithmetic progression P of cardinality at least$( \alpha ^ { 3 } N / 1 2 8 \pi ) ^ { 1 / 2 }$such that$| A \cap P | \geqslant ( \delta + \delta ^ { 2 } / 8 0 ) | P |$. This situation will be case 2.

If case 2 does not hold, then$| \hat { A } ( r ) | \leqslant \alpha N$for every non-zero r, which says that A satisfies condition (iv) of Lemma 2.2. The number of triples $( x , y , z ) \in A \times B ^ { 2 }$such that$x + z = 2 y$is then

$$
\begin{array}{l} N ^ {- 1} \sum_ {x \in A} \sum_ {y \in B} \sum_ {z \in B} \sum_ {r} \omega^ {r (2 y - x - z)} = N ^ {- 1} \sum_ {r} \hat {A} (r) \hat {B} (- 2 r) \hat {B} (r) \\ \quad \geqslant N ^ {- 1} | A | | B | ^ {2} - N ^ {- 1} \max _ {r \neq 0} | \hat {A} (r) | \Big (\sum_ {r \neq 0} | \hat {B} (- 2 r) | ^ {2} \Big) ^ {1 / 2} \Big (\sum_ {r \neq 0} | \hat {B} (r) | ^ {2} \Big) ^ {1 / 2} \\ \quad \geqslant \delta | B | ^ {2} - \alpha | B | N. \end{array}
$$

If in addition case 1 does not hold, then this quantity is minimized when $| B | = \delta N / 5$, and the minimum value is$\delta ^ { 3 } N ^ { 2 } / 5 0$, implying the existence of at least this number of triples$( x , y , z ) \in A \times B ^ { 2 }$in arithmetic progression mod N. Since B lives in the middle third, these are genuine progressions in $\{ 1 , 2 , \ldots , N \}$, and since there are only N degenerate progressions (i.e., with diference zero) we can conclude that A contains an arithmetic progression of length three as long as$N \geqslant 5 0 \delta ^ { - 3 }$. This we shall call case 3.

To summarize, if case 3 holds and$N \geqslant 5 0 \delta ^ { - 3 }$, then A contains an arithmetic progression of length three. In case 2, we can find a subprogression P of$\{ 1 , \ldots , N \}$of cardinality at least$( \alpha ^ { 3 } N / 1 2 8 \pi ) ^ { 1 / 2 }$such that$| A \cap P | \geqslant \delta ( 1 + \delta / 8 0 ) | P |$. Since$\{ 1 , \ldots , N \}$is a subprogression of $\{ 1 , \dots , N _ { 0 } \} , A = A _ { 0 } \cap \{ 1 , \dots , N \}$and one can easily check that$\delta ( 1 + \delta / 8 0 ) \geq$ $\delta _ { 0 } ( 1 + \delta _ { 0 } / 3 2 0 )$, we may conclude that in case 2 there is a subprogression P of$\{ 1 , \ldots , N _ { 0 } \}$of cardinality at least$( \alpha ^ { 3 } N _ { 0 } / 3 8 4 \pi ) ^ { 1 / 2 }$such that $| A _ { 0 } \cap P | \geqslant \delta _ { 0 } ( 1 + \delta _ { 0 } / 3 2 0 ) | P |$. As for cases 0 and 1, it is easy to see that the same conclusion also holds, and indeed a much stronger one as$P$ has a length which is linear in$N _ { 0 }$

This gives us the basis for an iteration argument. If$A _ { 0 }$does not contain an arithmetic progression of length three, then we drop down to a progression P where the density of A is larger, and repeat. If the density at step m of the iteration is$\delta _ { m } ,$then at each subsequent iteration the density increases by at least$\delta _ { m } ^ { 2 } / 3 2 0$. It follows that the density reaches$2 \delta _ { m }$after at most$3 2 0 \delta _ { m } ^ { - 1 }$further steps. It follows that the total number of steps cannot be more than$3 2 0 ( \delta ^ { - 1 } + ( 2 \delta ) ^ { - 1 } + ( 4 \delta ) ^ { - 1 } + \ldots ) = 6 4 0 \delta ^ { - 1 }$. At each step, the size of the progression in which A lives is around the square root of what it was at the previous step. The result now follows from a simple calculation (left to the reader).✷

## 3 Higher-degree Uniformity

There seems to be no obvious way of using α-uniformity to obtain progressions of length greater than three. (Of course, the truth of Szemer´edi’s theorem makes it hard to formalize this statement, but in the next section we show that α-uniformity does not give strong information about the number of arithmetic progressions of length k if$k > 3 . )$) The aim of this section is to define a notion of pseudo-randomness which is more suitable for the purpose. The next definition is once again presented as a series of approximately equivalent statements. In order to simplify the presentation for the case of progressions of length four, we shall prove two lemmas, even though the second implies the first. Given a function$f : \mathbb { Z } _ { N } \to \mathbb { Z } _ { N }$, we shall define, for any$k ,$, the diference function$\Delta ( f ; k )$by$\Delta ( f ; k ) ( s ) = f ( s ) { \overline { { f ( s - k ) } } }$. The reason for the terminology is that if, as will often be the case,$f ( s ) = \omega ^ { \phi ( s ) }$ for some function$\phi : \mathbb { Z } _ { N } \to \mathbb { Z } _ { N }$, then$\Delta ( f ; k ) ( s ) = \omega ^ { \phi ( k ) - \phi ( s - k ) }$

Now let us define iterated diference functions in two diferent ways as follows. The first is inductive, setting$\Delta ( f ; a _ { 1 } , \ldots , a _ { d } ) ( s )$to be $\Delta ( \Delta ( f ; a _ { 1 } , \ldots , a _ { d - 1 } ) ; a _ { d } ) ( s )$. The second makes explicit the result of the inductive process. Let C stand for the map from$\mathbb { C } ^ { N }$to$\mathbb { C } ^ { N }$which takes a function to its pointwise complex conjugate. Given a function$f : \mathbb { Z } _ { N } \to \mathbb { C } .$ we define

$$
\Delta (f; a _ {1}, \dots , a _ {d}) (s) = \prod_ {\epsilon_ {1}, \dots , \epsilon_ {d}} \left(C ^ {\epsilon_ {1} + \dots + \epsilon_ {d}} f\right) \left(s - \sum_ {i = 1} ^ {d} a _ {i} \epsilon_ {i}\right)
$$

where the product is over all sequences$\epsilon _ { 1 } , \ldots , \epsilon _ { d }$with$\epsilon _ { i } \in \{ 0 , 1 \}$. When $d = 3 .$, for example, this definition becomes

$$
\begin{array}{c} \Delta (f; a, b, c) (s) = f (s) \overline {{f (s - a) f (s - b) f (s - c)}} \\ \times f (s - a - b) f (s - a - c) f (s - b - c) \overline {{f (s - a - b - c)}}. \end{array}
$$

We now define a function$f$from$\mathbb { Z } _ { N }$to the closed unit disc$D \subset \mathbb { C }$to be α-uniform of degree d if

$$
\sum_ {a _ {1}, \dots , a _ {d}} \left| \sum_ {s} \Delta (f; a _ {1}, \dots , a _ {d}) (s) \right| ^ {2} \leqslant \alpha N ^ {d + 2}.
$$

When d equals two or three, we say that f is quadratically or cubically α-uniform respectively. As with the definition of α-uniformity (which is the same as α-uniformity of degree one) this definition has several useful reformulations.

Lemma 3.1. Let f be a function from$\mathbb { Z } _ { N }$to D. The following are equivalent.

(i) f is c<sub>1</sub>-uniform of degree d.

$$
(i i) \sum_ {s} \sum_ {a _ {1}, \dots , a _ {d + 1}} \Delta (f; a _ {1}, \dots , a _ {d + 1}) (s) \leqslant c _ {1} N ^ {d + 2}.
$$

(iii) There is a function$\alpha : \mathbb { Z } _ { N } ^ { d - 1 } { \longrightarrow } [ 0 , 1 ]$such that$\begin{array} { r } { \sum _ { a _ { 1 } , \dots , a _ { d - 1 } } \alpha ( a _ { 1 } , \dots , a _ { d - 1 } ) } \end{array}$ $\leqslant c _ { 1 } N ^ { d - 1 }$and$\Delta ( f ; a _ { 1 } , \ldots , a _ { d - 1 } )$is$\alpha ( a _ { 1 } , \ldots , a _ { d - 1 } )$)-uniform for every $( a _ { 1 } , \dotsc , a _ { d - 1 } )$

(iv) There is a function α :$\colon \mathbb { Z } _ { N }  [ 0 , 1 ]$such that$\begin{array} { r } { \sum _ { r } \alpha ( r ) = c _ { 1 } N } \end{array}$and $\Delta ( f ; r )$is$\alpha ( r )$-uniform of degree$d - 1$for every r.

(v)$\begin{array} { r } { \sum _ { a _ { 1 } , \dots , a _ { d - 1 } } \sum _ { r } \bigl | \Delta ( f ; a _ { 1 } , \dots , a _ { d - 1 } ) ^ { \wedge } ( r ) \bigr | ^ { 4 } \leqslant c _ { 1 } N ^ { d + 3 } . } \end{array}$

(vi) For all but$c _ { 2 } N ^ { d - 1 }$choices of$( a _ { 1 } , . . . , a _ { d - 1 } )$the function$\Delta ( f ; a _ { 1 } , . . . , a _ { d - 1 } )$ is$c _ { 2 } – u n i f o r m$

(vii) There are at most$c _ { 3 } N ^ { d - 1 }$values of$( a _ { 1 } , \dotsc , a _ { d - 1 } )$for which there exists some$r \in \mathbb { Z } _ { N }$with$\left| \Delta ( f ; a _ { 1 } , \ldots , a _ { d - 1 } ) ^ { \wedge } ( r ) \right| \geqslant c _ { 3 } N$

Proof. The equivalence of (i) and (ii) is easy, as the left-hand sides of the relevant expressions are equal. It is also obvious that (ii) and (iii) are equivalent. A very simple inductive argument shows that (ii) is equivalent to (iv). The equivalence of (i) and (v) follows, as in the proof of the equivalence of (i) and (iii) in Lemma 2.1, by expanding the left-hand side of (v). Alternatively, it can be deduced from Lemma 2.1 by applying that equivalence to each function$\Delta ( f ; a _ { 1 } , \ldots , a _ { d - 1 } )$and adding.

Averaging arguments show that (iii) implies (vi) as long as$c _ { 1 } \leqslant c _ { 2 } ^ { 2 }$, and that (vi) implies (iii) as long as$c _ { 1 } \geqslant 2 c _ { 2 }$. Finally, the equivalence of (i) and (ii) in Lemma 2.1 shows that in this lemma (vi) implies (vii) if$c _ { 3 } \geqslant c _ { 2 } ^ { 1 / 4 }$ and (vii) implies (vi) if$c _ { 2 } \geqslant c _ { 3 }$✷

Notice that properties (i) and (ii) above make sense even when$d = 0$ Therefore, we shall define a function$f : \mathbb { Z } _ { N } \to D$to be α-uniform of degree zero if$\begin{array} { r } { \left| \sum _ { s } f ( s ) \right| ^ { 2 } \leqslant \alpha N ^ { 2 } } \end{array}$. Property (iv) now makes sense when$d = 1$  This definition will allow us to begin an inductive argument at an earlier and thus easier place.

The next result is the main one of this section. Although it will not be applied directly, it easily implies the results that are needed for later.

Theorem 3.2. Let$k \geqslant 2$and let$f _ { 1 } , \ldots , f _ { k }$be functions from$\mathbb { Z } _ { N }$to D such that$f _ { k }$is α-uniform of degree$k - 2$. Then

$$
\left| \sum_ {r} \sum_ {s} f _ {1} (s) f _ {2} (s - r) \dots f _ {k} (s - (k - 1) r) \right| \leqslant \alpha^ {1 / 2 ^ {k - 1}} N ^ {2}.
$$

Proof. When$k = 2$, we know that

$$
\left| \sum_ {r} \sum_ {s} f _ {1} (s) f _ {2} (s - r) \right| = \left| \left(\sum_ {s} f _ {1} (s)\right) \left(\sum_ {t} f _ {2} (t)\right) \right| \leqslant \alpha^ {1 / 2} N ^ {2},
$$

since$\begin{array} { r } { \left| \sum _ { s } f _ { 1 } ( s ) \right| \leqslant N } \end{array}$and$\begin{array} { r } { \left| \sum _ { t } f _ { 2 } ( t ) \right| \leqslant \alpha ^ { 1 / 2 } N } \end{array}$

When$k > 2$ , assume the result for$k - 1$, let$f _ { k }$be α-uniform of degree $k - 2$and let$\alpha : \mathbb { Z } _ { N } \longrightarrow [ 0 , 1 ]$be a function with the property that$\Delta ( f _ { k } ; r )$ is$\alpha ( r )$-uniform of degree$k - 3$for every$r \in \mathbb { Z } _ { N }$. Then

$$
\begin{array}{l} \left| \sum_ {r} \sum_ {s} f _ {1} (s) \ldots f _ {k} (s - (k - 1) r) \right| ^ {2} \\ \leqslant N \sum_ {s} \left| \sum_ {r} f _ {1} (s) f _ {2} (s - r) \ldots f _ {k} (s - (k - 1) r) \right| ^ {2} \\ \leqslant N \sum_ {s} \left| \sum_ {r} f _ {2} (s - r) f _ {3} (s - 2 r) \ldots f _ {k} (s - (k - 1) r) \right| ^ {2} \\ = N \sum_ {s} \sum_ {r} \sum_ {t} f _ {2} (s - r) \overline {{f _ {2} (s - t)}} \ldots f _ {k} (s - (k - 1) r) \overline {{f _ {k} (s - (k - 1) t)}} \\ = N \sum_ {s} \sum_ {r} \sum_ {u} f _ {2} (s) \overline {{f _ {2} (s - u)}} \ldots f _ {k} (s - (k - 2) r) \overline {{f _ {k} (s - (k - 2) r - (k - 1) u)}} \\ = N \sum_ {s} \sum_ {r} \sum_ {u} \Delta (f _ {2}; u) (s) \Delta (f _ {3}; 2 u) (s - r) \ldots \Delta (f _ {k}; (k - 1) u) (s - (k - 2) r) \end{array}
$$

Since$\Delta ( f _ { k } ; ( k - 1 ) u )$is$\alpha ( ( k - 1 ) u )$-uniform of degree$k - 3 .$, our inductive hypothesis implies that this is at most$N \textstyle \sum _ { u } \alpha ( ( k - 1 ) u ) ^ { 1 / 2 ^ { k - 2 } } N ^ { 2 }$, and since $\begin{array} { r } { \sum _ { u } \alpha ( ( k - 1 ) u ) \leqslant \alpha N } \end{array}$, this is at most$\alpha ^ { 1 / 2 ^ { k - 2 } } N ^ { 4 }$, which proves the result for$k .$.✷

The interest in Theorem 3.2 is of course that the expression on the lefthand side can be used to count arithmetic progressions. Let us now define a set$A \subset \mathbb { Z } _ { N }$to be α-uniform of degree d if its balanced function is. (This definition makes sense when$d = 0$, but only because it applies to all sets.) The next result implies that a set$A$which is α-uniform of degree$d - 2$ for some small$\alpha$contains about the number of arithmetic progressions of length d that a random set of the same cardinality would have, where this means arithmetic progressions mod N. We shall then show how to obtain genuine progressions, which turns out to be a minor technicality, similar to the corresponding technicality in the proof of Roth’s theorem.

Corollary 3.3. Let$A _ { 1 } , \ldots , A _ { k }$be subsets of$\mathbb { Z } _ { N }$, such that$A _ { i }$has cardinality$\delta _ { i } N$for every$i ,$and is$\alpha ^ { 2 ^ { i - 1 } }$<sup>1</sup>-uniform of degree$i - 2$for every$i \geqslant 3$ Then

$$
\left| \sum_ {r} \left| (A _ {1} + r) \cap \dots \cap (A _ {k} + k r) \right| - \delta_ {1} \dots \delta_ {k} N ^ {2} \right| \leqslant 2 ^ {k} \alpha N ^ {2}.
$$

Proof. For each$i ,$let$f _ { i }$be the balanced function of$A _ { i }$. Then

$$
\left| \left(A _ {1} + r\right) \cap \dots \cap \left(A _ {k} + k r\right) \right| = \sum_ {s} \left(\delta_ {1} + f _ {1} (s - r)\right) \dots \left(\delta_ {k} + f _ {k} (s - k r)\right),
$$

so we can rewrite$| ( A _ { 1 } + r ) \cap \cdots \cap ( A _ { k } + k r ) | - \delta _ { 1 } \ldots \delta _ { k } N$as

$$
\sum_ {B \subset [ k ], B \neq \emptyset} \prod_ {i \notin B} \delta_ {i} \sum_ {s} \prod_ {i \in B} f _ {i} (s - i r)  .
$$

Now if j = max B, then$\begin{array} { r } { \sum _ { r } \sum _ { s } \prod _ { i \in B } f _ { i } ( s - i r ) } \end{array}$is at most$\alpha ^ { 2 ^ { j - 1 } / 2 ^ { j - 1 } } N ^ { 2 }$, by Theorem 3.2. It follows that

$$
\begin{array}{c} \Big | \sum_ {r} \big | (A _ {1} + r) \cap \dots \cap (A _ {k} + k r) \big | - \delta_ {1} \ldots \delta_ {k} N ^ {2} \Big | \leqslant \sum_ {B \subset [ k ], B \neq \emptyset} \prod_ {i \notin B} \delta_ {i}. \alpha N ^ {2} \\ = \alpha N ^ {2} \Big (\prod_ {i = 1} ^ {k} (1 + \delta_ {i}) - 1 \Big), \end{array}
$$

which is at most$2 ^ { k } \alpha N ^ { 2 }$, as required.

We now prove two simple technical lemmas.

Lemma 3.4. Let$d \geqslant 1$and let$f : \mathbb { Z } _ { N } \to D$be α-uniform of degree$d .$ Then$f$is$\alpha ^ { 1 / 2 }$-uniform of degree$d - 1$

Proof. Our assumption is that

$$
\sum_ {a _ {1}, \ldots , a _ {d}} \left| \sum_ {s} \Delta (f; a _ {1}, \ldots , a _ {d}) (s) \right| ^ {2} \leqslant \alpha N ^ {d + 2}.
$$

By the Cauchy-Schwarz inequality, this implies that

$$
\Big | \sum_ {a _ {1}, \ldots , a _ {d}} \sum_ {s} \Delta (f; a _ {1}, \ldots , a _ {d}) (s) \Big | \leqslant \alpha^ {1 / 2} N ^ {d + 1},
$$

which, by the equivalence of properties (i) and (ii) in Lemma 3.1, proves the lemma.✷

Lemma 3.5. Let A be an α-uniform subset of$\mathbb { Z } _ { N }$of cardinality δN, and let P be an interval of the form$\{ a + 1 , \ldots , a + M \}$, where$M = \beta N$. Then $\left| \left| A \cap P \right| - \beta \delta N \right| \leqslant \alpha ^ { 1 / 4 } N$

Proof. First, we can easily estimate the Fourier coeficients of the set P. Indeed,

$$
\begin{array}{c} | \hat {P} (r) | = \bigg | \sum_ {s = 1} ^ {M} \omega^ {- r (a + s)} \bigg | \\ = \big | (1 - \omega^ {r M}) / (1 - \omega^ {r}) \big | \leqslant N / 2 r. \end{array}
$$

(We also know that it is at most$M$, but will not need to use this fact.)

This estimate implies that$\begin{array} { r } { \sum _ { r \neq 0 } | \hat { P } ( r ) | ^ { 4 / 3 } \leqslant N ^ { 4 / 3 } } \end{array}$. Therefore,

$$
\begin{array}{l} \big | | A \cap P | - \beta \delta N \big | = N ^ {- 1} \Big | \sum_ {r \neq 0} \hat {A} (r) \hat {P} (r) \Big | \\ \leqslant N ^ {- 1} \Big (\sum_ {r \neq 0} | \hat {A} (r) | ^ {4} \Big) ^ {1 / 4} \Big (\sum_ {r \neq 0} | \hat {P} (r) | ^ {4 / 3} \Big) ^ {3 / 4} \\ \leqslant \Big (\sum_ {r \neq 0} | \hat {A} (r) | ^ {4} \Big) ^ {1 / 4} \leqslant \alpha^ {1 / 4} N, \end{array}
$$

using property (iv) of Lemma 3.1.

Corollary 3.6. Let$A \subset \mathbb { Z } _ { N }$be α-uniform of degree$k - 2$and have cardinality δN. If$\alpha \leqslant ( \delta / 2 ) ^ { k 2 ^ { k } }$and$N \geqslant 3 2 k ^ { 2 } \delta ^ { - k }$, then A contains an arithmetic progression of length k.

Proof. Let$A _ { 1 } = A _ { 2 } = A \cap [ ( k - 2 ) N / ( 2 k - 3 ) , ( k - 1 ) N / ( 2 k - 3 ) ]$, and let $A _ { 3 } = \cdots = A _ { k } = A$. By Lemma 3.4 A is$\alpha ^ { 1 / 2 ^ { k - 3 } }$-uniform (of degree one), so by Lemma 3.5 the sets$A _ { 1 }$and$A _ { 2 }$both have cardinality at least$\delta N / 4 k$ since, by the first inequality we have assumed, we know that$\alpha ^ { 1 / 2 ^ { k - 1 } } \leqslant \delta / 4 k$

Therefore, by Corollary 3.3, A contains at least$\big ( \big ( \frac { \delta ^ { k } } { 1 6 k ^ { 2 } } \big ) - 2 ^ { k } \alpha ^ { 1 / 2 ^ { k - 1 } } \big ) N ^ { 2 }$   arithmetic progressions modulo N with the first two terms belonging to the interval$[ ( k - 2 ) N / ( 2 k - 3 ) , ( k - 1 ) N / ( 2 k - 3 ) ]$. The only way such a progression can fail to be genuine is if the common diference is zero, and there are at most$\delta N$such degenerate progressions. Thus the corollary is proved, since the two inequalities we have assumed imply that $( \delta ^ { \bar { k } } / 1 6 k ^ { \bar { 2 } } ) - 2 ^ { k } \alpha ^ { 1 / 2 ^ { k - 1 } } \geqslant \delta ^ { k } / 3 2 k ^ { 2 }$and$\delta ^ { k } N ^ { 2 } / 3 2 k ^ { 2 } > \delta N$✷

Remark. Notice that the proof of Corollary 3.6 did not use Fourier coeficients. This shows that in the proof of Theorem 2.6, the Fourier analysis was not really needed for the analysis of case 3. However, it was used in a more essential way for case 2.

In order to prove Szemer´edi’s theorem, it is now enough to prove that if$A \subset \mathbb { Z } _ { N }$is a set of size δN which is not$( \delta / 2 ) ^ { k 2 ^ { k } }$-uniform of degree$d - 2$ then there is an arithmetic progression$P \subset \mathbb { Z } _ { N }$of length tending to infinity with N, such that$| A \cap P | \geqslant ( \delta + \epsilon ) | P |$, where$\epsilon > 0$depends on δ and d only. Thus, we wish to deduce a structural property of A from information about its diferences. We do not quite have an inverse problem, as usually defined, of additive number theory, but it is certainly in the same spirit, and we shall relate it to a well-known inverse problem, Freiman’s theorem, later in the paper. For the rest of this section we shall give a combinatorial characterization of α-uniform sets of degree d. The result will not be needed for Szemer´edi’s theorem but gives a little more insight into what is being proved. Also, Lemma 3.7 below will be used near the end of the paper.

Let A be a subset of$\mathbb { Z } _ { N }$and let$d \geqslant 0$. By a d-dimensional cube in A we shall mean a function$\phi : \{ 0 , 1 \} ^ { d } \to A$of the form

$$
\phi : (\epsilon_ {1}, \dots , \epsilon_ {d}) \mapsto a _ {0} + \epsilon_ {1} a _ {1} + \dots + \epsilon_ {d} a _ {d},
$$

where$a _ { 0 } , a _ { 1 } , \ldots , a _ { d }$all belong to$\mathbb { Z } _ { N }$. We shall say that such a cube is contained in A, even though it is strictly speaking contained in$A ^ { \{ 0 , 1 \} ^ { d } }$

Let$A \subset \mathbb { Z } _ { N }$have cardinality δN. Then A obviously contains exactly $\delta N$cubes of dimension zero and$\delta ^ { 2 } N ^ { 2 }$cubes of dimension one. As remarked after Lemma 2.2, the number of two-dimensional cubes in A can be written as$\begin{array} { r } { N ^ { - 1 } \sum _ { r } | \hat { A } ( r ) | ^ { 4 } } \end{array}$, so A is α-uniform if and only if there are at most $( \delta ^ { 4 } + \alpha ) N ^ { 3 }$of them. We shall now show that A contains at least$\delta ^ { 2 ^ { d } } N ^ { d + 1 }$ cubes of dimension d, and that equality is nearly attained if A is α-uniform of degree$d - 1$for some small α. The remarks we have just made prove this result for$d = 1$. Notice that equality is also nearly attained (with high probability) if A is a random set of cardinality$\delta N$. This is why we regard higher-degree uniformity as a form of pseudorandomness.

Lemma 3.7. Let A be a subset of$\mathbb { Z } _ { N }$of cardinality δN and let d - 0. Then A contains at least$\delta ^ { 2 ^ { d } } N ^ { d + 1 }$cubes of dimension d.

Proof. We know the result for$d = 0$or 1 so let$d > 1$and assume that the result is known for$d - 1$. The number of d-dimensional cubes in A is the sum over all r of the number of$( d - 1 )$)-dimensional cubes in$A \cap ( A + r )$ Write$\delta ( r ) N$for the cardinality of$A \cap ( A + r )$Then by induction the number of d-dimensional cubes in A is at least$\textstyle \sum _ { r } \delta ( r ) ^ { 2 ^ { d - 1 } } N ^ { d }$. Since the average value of$\delta ( r )$is exactly$\delta ^ { 2 }$, this is at least$\delta ^ { 2 ^ { d } } N ^ { d + 1 }$as required. ✷

The next lemma is little more than the Cauchy-Schwarz inequality and some notation. It will be convenient to use abbreviations such as x for $( x _ { 1 } , \ldots , x _ { k } )$and$x . y$for$\textstyle \sum _ { i = 1 } ^ { k } x _ { i } y _ { i }$. If$\epsilon \in \{ 0 , 1 \} ^ { k }$then we shall write$| \epsilon |$for $\textstyle \sum _ { i = 1 } ^ { k } \epsilon _ { i }$. Once again, C is the operation of complex conjugation.

Lemma 3.8. For every$\epsilon \in \{ 0 , 1 \} ^ { k }$let$f _ { \epsilon }$be a function from$\mathbb { Z } _ { N }$to D. Then

$$
\Big | \sum_ {x \in \mathbb {Z} _ {N} ^ {d}} \sum_ {s} \prod_ {\epsilon \in \{0, 1 \} ^ {d}} C ^ {| \epsilon |} f _ {\epsilon} (s - \epsilon . x) \Big | \leqslant \prod_ {\epsilon \in \{0, 1 \} ^ {d}} \Big | \sum_ {x \in \mathbb {Z} _ {N} ^ {d}} \sum_ {s} \prod_ {\eta \in \{0, 1 \} ^ {d}} C ^ {| \eta |} f _ {\epsilon} (s - \eta . x) \Big | ^ {\frac {1}{2 ^ {d}}}.
$$

$$
\begin{array}{l} \text {Proof.} \\ \left| \sum_ {x \in \mathbb {Z} _ {N} ^ {d}} \sum_ {s} \prod_ {\epsilon \in \{0, 1 \} ^ {d}} C ^ {| \epsilon |} f _ {\epsilon} (s - \epsilon . x) \right| \\ = \Big | \sum_ {x \in \mathbb {Z} _ {N} ^ {d - 1}} \Big (\sum_ {s} \prod_ {\epsilon \in \{0, 1 \} ^ {d - 1}} C ^ {| \epsilon |} f _ {\epsilon , 0} (s - \epsilon . x) \Big) \Big (\sum_ {t} \prod_ {\epsilon \in \{0, 1 \} ^ {d - 1}} C ^ {| \epsilon |} f _ {\epsilon , 1} (t - \epsilon . x) \Big) \Big | \\ \leqslant \Big (\sum_ {x \in \mathbb {Z} _ {N} ^ {d - 1}} \Big | \sum_ {s} \prod_ {\epsilon \in \{0, 1 \} ^ {d - 1}} C ^ {| \epsilon |} f _ {\epsilon , 0} (s - \epsilon . x) \Big | ^ {2} \Big) ^ {\frac {1}{2}} \\ \cdot \Big (\sum_ {x \in \mathbb {Z} _ {N} ^ {d}} \Big | \sum_ {s} \prod_ {\epsilon \in \{0, 1 \} ^ {d - 1}} C ^ {| \epsilon |} f _ {\epsilon , 1} (s - \epsilon . x) \Big | ^ {2} \Big) ^ {\frac {1}{2}}. \end{array}
$$

Let us write$P _ { d } ( \epsilon )$and$Q _ { d } ( \epsilon )$for the sequences$( \epsilon _ { 1 } , \ldots , \epsilon _ { d - 1 } , 0 )$and $( \epsilon _ { 1 } , \epsilon \cdot \cdot , \epsilon _ { d - 1 } , 1 )$. Then

$$
\sum_ {x \in \mathbb {Z} _ {N} ^ {d - 1}} \left| \sum_ {s} \prod_ {\epsilon \in \{0, 1 \} ^ {d - 1}} C ^ {| \epsilon |} f _ {\epsilon , 0} (s - \epsilon . x) \right| ^ {2} = \sum_ {x \in \mathbb {Z} _ {N} ^ {d}} \sum_ {s} \prod_ {\epsilon \in \{0, 1 \} ^ {d}} C ^ {| \epsilon |} f _ {P _ {d} (\epsilon)} (s - \epsilon . x)
$$

and similarly for the second bracket with$\mathrm { \Delta } Q \mathrm { \Delta } d ,$so the two parts are square roots of expressions of the form we started with, except that the function$f _ { \epsilon }$ no longer depends on$\epsilon _ { d }$. Repeating this argument for the other coordinates, we obtain the result.✷

If we regard Lemma$3 . 8$as a modification of the Cauchy-Schwarz inequality, then the next lemma is the corresponding modification of Minkowski’s inequality.

Lemma 3.9. Given any function$f : \mathbb { Z } _ { N } \to \mathbb { C }$and any$d \geqslant 2$, define$\| f \| _ { d }$ by the formula

$$
\| f \| _ {d} = \Big | \sum_ {x \in \mathbb {Z} _ {N} ^ {d}} \sum_ {s} \prod_ {\epsilon \in \{0, 1 \} ^ {d}} C ^ {| \epsilon |} f (s - \epsilon . x) \Big | ^ {1 / 2 ^ {d}}.
$$

Then$\| f + g \| _ { d } \leqslant \| f \| _ { d } + \| g \| _ { d }$for any pair of functions$f , g : \mathbb { Z } _ { N } \longrightarrow \mathbb { C }$. In other words,$\| . \| _ { d }$is a norm.

Proof. If we expand$\| f + g \| ^ { 2 ^ { d } }$, we obtain the sum

$$
\sum_ {x \in \mathbb {Z} _ {N} ^ {d}} \sum_ {s} \prod_ {\epsilon \in \{0, 1 \} ^ {d}} C ^ {| \epsilon |} (f + g) (s - \epsilon . x).
$$

If we expand the product we obtain$2 ^ { 2 ^ { d } }$terms of the form $\begin{array} { r } { \prod _ { \epsilon \in \{ 0 , 1 \} ^ { d } } C ^ { | \epsilon | } f _ { \epsilon } ( s - \epsilon . x ) } \end{array}$, where each function$f _ { \epsilon }$is either f or$g .$. For each one of these terms, if we take the sum over$x _ { 1 } , \ldots , x _ { d }$and s and apply

Lemma 3.8, we have an upper estimate of$\| f \| _ { d } ^ { k } \| g \| _ { d } ^ { l }$, where k and l are the number of times that$f _ { \epsilon }$equals$f$and g respectively. From this it follows that

$$
\| f + g \| ^ {2 ^ {d}} \leqslant \sum_ {k = 0} ^ {2 ^ {d}} \binom {2 ^ {d}} {k} \| f \| _ {d} ^ {k} \| g \| _ {d} ^ {2 ^ {d} - k} = (\| f \| _ {d} + \| g \| _ {d}) ^ {2 ^ {d}},
$$

which proves the lemma.

It is now very easy to show that equality is almost attained in Lemma 3.7 for sets that are suficiently uniform.

Lemma 3.10. Let A be α-uniform of degree$d - 1$. Then A contains at most$( \delta + \alpha ^ { 1 / 2 ^ { d } } ) ^ { 2 ^ { d } } N ^ { d + 1 }$cubes of dimension d.

Proof. Write$A = \delta + f$where$| A | = \delta N$and f is the balanced function of A. Then$\left\| A \right\| _ { d } \leqslant \left\| \delta \right\| _ { d } + \left\| f \right\| _ { d } .$. It is easy to see that$\| A \| _ { d } ^ { 2 ^ { d } }$is the number of d-dimensional cubes in A and that$\| \delta \| _ { d } ^ { 2 ^ { d } } = \delta ^ { 2 ^ { d } } N ^ { d + 1 }$. Moreover, the statement that A is α-uniform of degree$d - 1$is equivalent to the statement that$\| f \| _ { d } ^ { 2 ^ { d } } \leqslant \alpha N ^ { d + 1 }$. Therefore, Lemma 3.9 tells us that A contains at most$( \delta + \alpha ^ { 1 / 2 ^ { d } } ) ^ { 2 ^ { d } } N ^ { d + 1 }$cubes of dimension d.✷

Remark. In a sense, the normed spaces just defined encapsulate all the information we need about the arithmetical properties of the functions we consider. In their definitions they bear some resemblance to Sobolev spaces. Although I cannot think of any potential applications, I still feel that it would be interesting to investigate them further.

## 4 Two Motivating Examples

We now know that Szemer´edi’s theorem would follow from an adequate understanding of higher-degree uniformity. A natural question to ask is whether degree-one uniformity implies higher-degree uniformity (for which it would be enough to show that it implied quadratic uniformity). To make the question precise, if A has density δ and is α-uniform, does it follow that A is quadratically β-uniform, for some$\beta$which, for fixed δ, tends to zero as α tends to zero? If so, then the same result for higher-degree uniformity can be deduced, and Szemer´edi’s theorem follows easily, by the method of §2.

The first result of this section is a simple counterexample showing that uniformity does not imply quadratic uniformity. Let A be the set$\{ s \in \mathbb { Z } _ { N }$: $| s ^ { 2 } | \leqslant N / 1 0 \}$. If$s \in A \cap ( A + k )$, then$| s ^ { 2 } | \leqslant N / 1 0$and$| ( s - k ) ^ { 2 } | \leqslant N / 1 0$ as well, which implies that$| 2 s k - k ^ { 2 } | \leqslant N / 5 .$, or equivalently that s lies inside the set$( 2 k ) ^ { - 1 } \{ s : | s - k / 2 | \leqslant N / 5 \}$. It follows that$A \cap ( A + k )$is not uniform for any$k \neq 0$

It is possible, but not completely straightforward, to show that A itself is uniform. Rather than$_ \mathrm { g o }$into the details, we prove a closely related fact which is in some ways more natural. Let$f ( s ) = \omega ^ { s ^ { 2 } }$. We shall show that$f$ is a very uniform function, while$\Delta ( f ; k )$fails badly to be uniform for any $k \neq 0$. For the uniformity of$f _ { i }$, notice that

$$
| \hat {f} (r) | = \left| \sum_ {s} \omega^ {s ^ {2} - r s} \right| = \left| \sum_ {s} \omega^ {(s - r / 2) ^ {2}} \right| = \left| \sum_ {s} \omega^ {s ^ {2}} \right|
$$

for every r. Therefore,$| \hat { f } ( \boldsymbol r ) | = N ^ { 1 / 2 }$for every$r \in \mathbb { Z } _ { N }$, so$f$is as uniform as a function into the unit circle can possibly be. On the other hand, $\Delta ( f ; k ) ( s ) = \omega ^ { 2 k s - k ^ { 2 } }$, so that

$$
\Delta (f; k) ^ {\wedge} (r) = \left\{ \begin{array}{l l} N & \mathrm{r=2k} \\ 0 & \mathrm{otherwise,} \end{array} \right.
$$

which shows that$\Delta ( f ; k )$is, for$k \neq 0$, as non-uniform as possible.

More generally, if$\phi : \mathbb { Z } _ { N } { \longrightarrow } \mathbb { Z } _ { N }$is a quadratic polynomial and$f ( s ) { = } \omega ^ { \phi ( s ) }$ then f is highly uniform, but there is some$\lambda \in \mathbb { Z } _ { N }$such that, for every$k ,$

$$
\Delta (f; k) ^ {\wedge} (r) = \left\{ \begin{array}{l l} N & r = \lambda k \\ 0 & \text { otherwise }. \end{array} \right.
$$

This suggests an attractive conjecture, which could perhaps replace the false idea that if A is uniform then so are almost all$A \cap ( A + k )$. Perhaps if there are many values of k for which$A \cap ( A + k )$fails to be uniform, then there must be a quadratic function$\phi : \mathbb { Z } _ { N } \to \mathbb { Z } _ { N }$such that$\left| \sum _ { s \in A } \omega ^ { - \phi ( s ) } \right|$ <sup></sup> is large. We shall see in the next section that such “quadratic bias” would actually imply the existence of a long arithmetic progression$P _ { j }$such that $| A \cap P _ { j } | / | P _ { j } |$was significantly larger than$| A | / N$. This would give a proof of Szemer´edi’s theorem for progressions of length four, and one can see how the above ideas might be generalized to higher-degree polynomials and longer arithmetic progressions.

The second example of this section shows that such conjectures are still too optimistic. As with the first example, we shall consider functions that are more general than characteristic functions of subsets of$\mathbb { Z } _ { N }$. However, this should be enough to convince the reader not to try to prove the conjectures.

Let r be about$\sqrt { N }$and for$0 \leqslant a , b < r / 2$define$\phi ( a r + b )$to be$a ^ { 2 } + b ^ { 2 }$

Now define

$$
f (s) = \left\{ \begin{array}{l l} \omega^ {\phi (s)} & s = a r + b \text {   for   some   } 0 \leqslant a, b <   r / 2 \\ 0 & \text { otherwise. } \end{array} \right.
$$

The function f is not quadratic, but it resembles a quadratic form in two variables (with the numbers 1 and r behaving like a basis of a twodimensional space).

Suppose$s = a r + b$and$k = c r +$d are two numbers in$\mathbb { Z } _ { N }$, where all of $a , b , a - c$and$b - d$lie in the interval$[ 0 , r / 2 )$. Then

$$
f (s) \overline {{f (s - k)}} = \omega^ {2 a c - c ^ {2} + 2 b d - d ^ {2}} = \omega^ {\phi_ {k} (a r + b)},
$$

where$\phi _ { k }$depends linearly on the pair$( a , b )$. The property that will interest us about$\phi _ { k }$is that, at least when c and d are not too close to$r / 2$, there are several pairs$( a , b )$such that the condition on$( a , b , c , d )$applies, and therefore several quadruples$\left( \left( a _ { i } , b _ { i } \right) \right) _ { i = 1 } ^ { 4 }$such that

$$
(a _ {1}, b _ {1}) + (a _ {2}, b _ {2}) = (a _ {3}, b _ {3}) + (a _ {4}, b _ {4})
$$

and

$$
\phi_ {k} (a _ {1} r + b _ {1}) + \phi_ {k} (a _ {2} r + b _ {2}) = \phi_ {k} (a _ {3} r + b _ {3}) + \phi_ {k} (a _ {4} r + b _ {4}).
$$

Here, “several” means a number proportional to$N ^ { 3 }$, which is the maximum it could be.

Let B be the set of all$s = a r + b$for which$a , b , c$and d satisfy the conditions above. (Of course, B depends on$k . )$Then

$$
\begin{array}{l} \sum_ {q} \Big | \sum_ {s \in B} \omega^ {\phi_ {k} (s) - q s} \Big | ^ {4} \\ = N \sum \{\omega^ {\phi_ {k} (s) + \phi_ {k} (t) - \phi_ {k} (u) - \phi_ {k} (v)}: s, t, u, v \in B, s + t = u + v \}. \end{array}
$$

Now the set B has been chosen so that if$s , t , u , v \in B$and$s + t = u + v ,$ then$\phi _ { k } ( s ) + \phi _ { k } ( t ) = \phi _ { k } ( u ) + \phi _ { k } ( v )$. Therefore, the right-hand side above is N times the number of quadruples$( s , t , u , v ) \in B ^ { 4 }$such that$s + t = u + v$ It is not hard to check that if c and d are smaller than$r / 4$, say, then B has cardinality proportional to$N ^ { 3 }$, and therefore that the right-hand side above is proportional to$N ^ { 4 }$. Lemma 2.1 now tells us that$\phi _ { k }$has a large Fourier coeficient. Thus, at the very least, we have shown that, for many values of k,$\Delta ( f ; k )$fails to be uniform.

If we could find a genuinely quadratic function$\phi ( s ) = a s ^ { 2 } + b s + c$such that$\begin{array} { r } { \left| \sum _ { s } f ( s ) \omega ^ { - \phi ( s ) } \right| ^ { 2 } } \end{array}$was proportional to$N ^ { 2 }$, then, expanding, we would have

$$
\sum_ {s, k} f (s) \overline {{f (s - k)}} \omega^ {- \phi (s) + \phi (s - k)} = \sum_ {s, k} f (s) \overline {{f (s - k)}} \omega^ {- 2 a s k - b k}
$$

proportional to$N ^ { 2 }$, which would imply that the number of k for which $\Delta ( f ; k ) \sim ( 2 a k )$was proportional to$N$was proportional to N. A direct calculation (left to the interested reader) shows that such a phenomenon does not occur. That is, there is no value of λ such that$\Delta ( f ; k ) ^ { \wedge } ( \lambda k )$is large for many values of k.

There are of course many examples like the second one above. One can define functions that resemble d-dimensional quadratic forms, and provided that d is small the same sort of behaviour occurs. Thus, we must accept that the ideas of this paper so far do not lead directly to a proof of Szemer´edi’s theorem, and begin to come to terms with these “multi-dimensional” examples. It is for this purpose that our major tool, an adaptation of Freiman’s theorem, is used, as will be explained later in the paper.

Returning to the first example of this section, it should be noted that the set$A = \lbrace s \in \mathbb { Z } _ { N } : \lvert s ^ { 2 } \rvert \leqslant N / 1 0 \rbrace$also serves to show that a uniform set need not have roughly the same number of arithmetic progressions of length four as a random set. Indeed, it is not hard to show that if$x , x + d$ and$x + 2 d$all lie in$A _ { i }$, then it is a little ‘too likely’ that$x + 3 d$will also lie in$A ,$, which shows that A contains ‘too many’ progressions of length four.

Until recently, I was confident that a modificiation of this example could be constructed with too few progressions of length four. However, I have recently changed my mind, after a conversation with Gil Kalai in which he challenged me actually to produce such a modification. In fact, there are convincing heuristic arguments in support of the following conjecture, even though at first it seems very implausible.

Conjecture 4.1. Let$A \subset \mathbb { Z } _ { N }$be a set of size δN. Then, if A is$\alpha \mathrm { - }$ uniform, the number of quadruples$( x , x + d , x + 2 d , x + 3 d )$in$A ^ { 4 }$is at least $( \delta ^ { 4 } - \beta ) N ^ { 2 }$, where$\beta$tends to zero as α tends to zero.

In other words, uniform sets always contain at least the expected number of progressions of length four.

It can be shown that quadratically uniform sets sometimes contain significantly fewer progressions of length five than random sets of the same cardinality. However, the example depends in an essential way on 5 being odd, and the following extension of Conjecture 4.1 appears to be true as well.

Conjecture 4.2. Let$A \subset \mathbb { Z } _ { N }$be a set of size$\delta N$and let k be an even number. Then, if A is α-uniform of degree$k - 1$, the number of sequences $( x , x + d , . . . , x + ( k + 1 ) d )$belonging to$\cdot A ^ { k + 2 }$is at least$( \delta ^ { k + 2 } - \beta ) N ^ { 2 }$, where $\beta$tends to zero as α tends to zero.

## 5 Consequences of Weyl’s Inequality

In this section we shall generalize Lemma 2.2 and Corollary 2.3 from linear functions to general polynomials. Most of the results of the section are well known. Since the proofs are short, we shall give many of them in full, to keep the paper as self-contained as possible. The main exception is Weyl’s inequality itself: there seems little point in reproducing the proof when it is well explained in many places. Once we have generalized these two results, we will have shown that for the proof of Szemer´edi’s theorem it is enough to prove that a set which fails to be uniform of degree d exhibits “polynomial bias”, rather than “linear$\mathrm { b i a s } ^ { \mathrm { * } }$as we showed in the case$d = 1$. We shall not try to define the notion of bias precisely. If a set A has balanced function$f$and there is a polynomial$\phi : \mathbb { Z } _ { N } \to \mathbb { Z } _ { N }$of degree d such that$\begin{array} { r } { \left| \sum _ { s } f ( s ) \omega ^ { - \phi ( s ) } \right| } \end{array}$is large, then A exhibits polynomial bias in <sub></sub> <sub></sub>the required sense. However, the second example in the previous section showed that this is too much to ask for, so a precise definition would have to be somewhat weaker.

First, we give some simple estimates for certain Fourier coeficients. We shall write$[ - M , M )$for the set$\{ - M , - ( M - 1 ) , \dots , M - 1 \}$

Lemma 5.1. Let$I ~ \subset ~ \mathbb { Z } _ { N }$be the interval$[ - M , M )$. Then$| \hat { I } ( r ) | \ \leqslant$ min$\{ 2 M , N / 2 | r | \}$

Proof. This is a simple direct calculation. The upper bound of 2M is trivial. To obtain the bound of$N / 2 | r |$, note that for θ in the range$[ - \pi , \pi ]$one has

$$
\left| 1 - e ^ {i \theta} \right| \geqslant 2 | \theta | / \pi .
$$

Applying this estimate with$\theta = 2 \pi r / N$gives

$$
| \hat {I} (r) | = \left| \sum_ {s = - M} ^ {M - 1} \omega^ {r s} \right| = \left| \frac {\omega^ {- r M} - \omega^ {r M}}{1 - \omega^ {r}} \right| \leqslant \frac {2}{| 1 - \omega^ {r} |} \leqslant \frac {N}{2 | r |},
$$

as was wanted.

Given an integer$r \in \mathbb { Z } _ { N }$, we shall use the notation$| r |$to stand for the modulus of the unique representative of r that lies in the interval $[ - N / 2 , N / 2 )$(i.e., the distance from r to zero).

Lemma 5.2. Let A be a subset of$\mathbb { Z } _ { N }$of cardinality t, let M be an even integer and suppose that$A \cap [ - M , M ) = \emptyset$. Then there exists r with $0 < | r | \leqslant N ^ { 2 } M ^ { - 2 }$such that$| \hat { A } ( r ) | \geqslant t M / 2 N$

Proof. Let$I = [ - M / 2 , M / 2 )$. Then$A \cap ( I - I ) = \emptyset$. It follows that $\langle A , I * I \rangle = 0$, which is the same as saying that$\begin{array} { r } { \sum _ { s } A ( s ) I * I ( s ) = 0 } \end{array}$

By identities (1) and (2) of$\ S 2$(transforms of convolutions and Parseval’s identity) it follows that$\begin{array} { r } { \sum _ { r } \hat { A } ( r ) | \hat { I } ( r ) | ^ { 2 } = 0 } \end{array}$. Since${ \hat { I } } ( 0 ) = M$and$\hat { A } ( 0 ) = t$, it follows that

$$
\sum_ {r \neq 0} | \hat {A} (r) | | \hat {I} (r) | ^ {2} \geqslant t M ^ {2}.
$$

By Lemma 5.1, we know, for each$r ,$that$| \hat { I } ( r ) | \leqslant$min$\{ M , N / 2 | r | \}$. It follows that

$$
\begin{array}{l} \sum_ {r \neq 0} | \hat {A} (r) | | \hat {I} (r) | ^ {2} \leqslant \max _ {0 <   | r | \leqslant N ^ {2} M ^ {- 2}} | \hat {A} (r) | \sum_ {r} | \hat {I} (r) | ^ {2} + t \sum_ {| r | \geqslant N ^ {2} M ^ {- 2}} N ^ {2} / 4 | r | ^ {2} \\ \qquad \leqslant M N \max _ {0 <   | r | \leqslant N ^ {2} M ^ {- 2}} | \hat {A} (r) | + (3 / 4) t N ^ {2} (N ^ {2} M ^ {- 2}) ^ {- 1} \\ \qquad = M N \max _ {0 <   | r | \leqslant N ^ {2} M ^ {- 2}} | \hat {A} (r) | + (3 / 4) t M ^ {2}. \end{array}
$$

Therefore, there exists r with$| r | \leqslant N ^ { 2 } M ^ { - 2 }$and$| \hat { A } ( r ) | \geqslant M ^ { 2 } t / 4 M N =$ $t M / 4 N$, which proves the lemma.✷

Remark. A more obvious approach to proving the above result would be to use I instead of$I * I$. That is, one would consider the sum$\textstyle \sum _ { r } { \hat { A } } ( r ) { \hat { I } } ( r )$ It turns out, however, that the estimates that one obtains are not strong enough. The trick of using$I * I$instead is basically the familiar device of replacing the Dirichlet kernel by the F´ejer kernel.

The next lemma is a special case of Weyl’s inequality. (To obtain the inequality in its full generality, replace$s ^ { k }$below by an arbitrary monic polynomial of degree$k .$The proof is unafected.) We shall make a fairly standard deduction from it, so it seems appropriate to use standard notation as well. Thus, e(x) means exp(2πix).

Lemma 5.3. Let a and q be integers with$( a , q ) = 1$. Let α be a real number such that$\left| \alpha - a / q \right| \leqslant q ^ { - 2 }$. Then, for all$\epsilon > 0$

$$
\left| \sum_ {s = 1} ^ {t} e (\alpha s ^ {k}) \right| \leqslant C _ {\epsilon} t ^ {1 + \epsilon} (q ^ {- 1} + t ^ {- 1} + q t ^ {- k}) ^ {1 / 2 ^ {k - 1}}.
$$

Moreover,$i f t \geqslant 2 ^ { 2 ^ { 3 2 k ^ { 2 } } }$, then the above inequality is valid with$\epsilon = 1 / k 2 ^ { k + 1 }$ and$C _ { \epsilon } = 1 0 0 0$✷

The above estimate for$C _ { \epsilon }$is important because we wish to use the inequality to obtain explicit bounds. Unfortunately, I have not managed to find in the literature any presentation of Weyl’s inequality that bothers to estimate$C _ { \epsilon }$. If one follows the proof given by Vaughan [V] and keeps track of everything that is swallowed up by the$t ^ { \epsilon } { . }$, one can replace the$C _ { \epsilon } t ^ { \epsilon }$ in the right-hand side of the inequality by

$$
5 0 0 (2 t) ^ {8 k / 2 ^ {k - 1} \log \log t} (\log t) ^ {1 / 2 ^ {k - 1}}.
$$

It is from this that we deduced the final part of the lemma. Note that, although$C _ { \epsilon }$became an absolute constant, we paid for it with the assumption that t was suficiently large. Since we are stating this estimate rather than giving a detailed proof, the reader may be reassured to know that for what follows it would not matter if t was required to be far larger – quadruply exponential in$k ,$say. Moreover, Weyl’s inequality does not give the best known estimate for the exponential sum in question. It is used here because its proof is reasonably simple, which makes checking the estimate above relatively straightforward.

The next lemma is very standard, and is due to Dirichlet.

Lemma 5.4. Let α be a real number. For every integer$u \geqslant 1$there exist integers a and q with$( a , q ) = 1 , 1 \leqslant q \leqslant$u and$\vert \alpha - a / q \vert \leqslant 1 / q u$✷

 The next lemma is also due to Weyl. Since it is again hard to find in the literature in the quantitative form we need, we give a complete proof.

Lemma 5.5. Let$k \geqslant 2$, let$t \geqslant 2 ^ { 2 ^ { 3 2 k ^ { 2 } } }$, let$N \geqslant t$and and let$a \in \mathbb { Z } _ { N }$. Then there exists$p \leqslant t$such that$| p ^ { k } a | \leqslant t ^ { - 1 / k 2 ^ { k + 1 } } N$

Proof. Let$A = \{ a , 2 ^ { k } a , 3 ^ { k } a , \ldots , t ^ { k } a \}$. By Lemma 5.2, if the result is false then there exists r such that$0 < | { \boldsymbol { r } } | \leqslant t ^ { 1 / k 2 ^ { k } }$and$| \hat { A } ( r ) | \geqslant \frac { 1 } { 2 } t ^ { 1 - 1 / k 2 ^ { k + 1 } }$ Setting$\alpha = - a r / N$, we have

$$
\hat {A} (r) = \sum_ {u \in A} \omega^ {- r u} = \sum_ {s = 1} ^ {t} \omega^ {- r s ^ {k} a} = \sum_ {s = 1} ^ {t} e (\alpha s ^ {k}).
$$

Lemma 5.4 gives us integers b and q with$( b , q ) \ = \ 1 , \ 1 \leqslant q \leqslant t$and $\left| \alpha - b / q \right| \leqslant 1 / q t$. By Lemma 5.3 we know that

$$
| \hat {A} (r) | \leqslant 1 0 0 0 t ^ {1 + 1 / k 2 ^ {k + 1}} \left(q ^ {- 1} + t ^ {- 1} + t ^ {1 - k}\right) ^ {1 / 2 ^ {k - 1}}.
$$

By the lower bound for$| \hat { A } ( \boldsymbol r ) |$, we may deduce that

$$
2 0 0 0 t ^ {1 / k 2 ^ {k}} (q ^ {- 1} + t ^ {- 1} + q ^ {1 - k}) ^ {1 / 2 ^ {k - 1}} \geqslant 1
$$

which implies, after a small calculation (using the assumption that$t \geqslant$ $2 ^ { 2 ^ { 3 2 k ^ { 2 } } } )$, that$q \leqslant 2 t ^ { 1 / 2 k }$

We may now argue directly. We know that$\left| \alpha - b / q \right| \leqslant 1 / q t$. Multiplying both sides by$( r q ) ^ { k } N / r$we find that

$$
\left| - a (r q) ^ {k} - b (r q) ^ {k - 1} N \right| \leqslant \left(| r | q\right) ^ {k - 1} N / t \leqslant t ^ {- 1 / 2} N,
$$

so we can set$p = r q$(contradicting the initial assumption that the result was false).✷

Corollary 5.6. Let$\phi : \mathbb { Z } _ { N } \to \mathbb { Z } _ { N }$be any polynomial of degree$k ,$let $K = ( k ! ) ^ { 2 } 2 ^ { ( k + 1 ) ^ { 2 } }$and let r be an integer exceeding$2 ^ { 2 ^ { 4 0 k ^ { 2 } } }$. Then for every $m \geqslant \dot { r } ^ { 1 - 1 / K }$the set$\{ 0 , 1 , 2 , \ldots , r - 1 \}$can be partitioned into arithmetic progressions$P _ { 1 } , \ldots , P _ { m }$such that the diameter of$\cdot _ { \phi } ( P _ { j } )$is at most$r ^ { - 1 / K } N$ for every$j$and the lengths of any two$P _ { j }$difer by at most 1.

Proof. The case$k = 1$follows immediately from Lemma 2.2. Given$k > 1$ let us write$\phi ( x ) = a x ^ { k } + \psi _ { 1 } ( x )$, in such a way that$\psi _ { 1 }$is a polynomial of degree$k - 1$. By Lemma 5.5 we can find$p \leqslant r ^ { 1 / 2 }$such that$| a p ^ { k } | \leqslant$ $r ^ { - 1 / k 2 ^ { k + 2 } } N$. Then for any s we have

$$
\begin{array}{c} \phi (x + s p) = a (x + s p) ^ {k} + \psi_ {1} (x + s p) \\ = s ^ {k} (a p ^ {k}) + \psi_ {2} (x, p), \end{array}
$$

where$\psi _ { 2 }$is, for any fixed$x , \mathrm { a }$polynomial of degree at most$k - 1$in$p$.

For any$u ,$the diameter of the set$\{ s ^ { k } ( a p ^ { k } ) : 0 \leqslant s < u \}$is at most $u ^ { k } | a p ^ { k } | \leqslant u ^ { k } r ^ { - 1 / k 2 ^ { k + 2 } } N$. Therefore, for any$u \leqslant r ^ { 1 / 4 }$, we can partition the set$\{ 0 , 1 , \ldots , r - 1 \}$into arithmetic progressions of the form

$$
Q _ {j} = \left\{x _ {j}, x _ {j} + p, \ldots , x _ {j} + (u _ {j} - 1) p \right\},
$$

such that, for every$j , u - 1 \leqslant u _ { j } \leqslant \iota$u and there exists a polynomial$\phi _ { j }$of degree at most$k - 1$such that, for any subset$P \subset Q _ { j }$

$$
\operatorname{diam} (\phi (P)) \leqslant u ^ {k} r ^ {- 1 / k 2 ^ {k + 1}} N + \operatorname{diam} (\phi_ {j} (P)).
$$

Let us choose$u = r ^ { 1 / k ^ { 2 } 2 ^ { k + 2 } }$, with the result that$u ^ { k } r ^ { - 1 / k 2 ^ { k + 1 } } = r ^ { - 1 / k 2 ^ { k + 2 } }$ It is easy to check that$u \geqslant 2 ^ { 2 ^ { 4 0 ( k - 1 ) ^ { 2 } } }$. Therefore, by induction, if$v \leqslant u ^ { 1 / L }$ where$\dot { L } = ( ( k - 1 ) ! ) ^ { 2 } 2 ^ { k ^ { 2 } }$, then every$Q _ { j }$can be partitioned into arithmetic progressions$P _ { j t }$of length$v - 1$or v in such a way that diam$( \phi _ { j } ( P _ { j t } ) ) \leqslant$ $u ^ { - 1 / L } N$for every t. It is not hard to check that this, with our choice of u above, gives us the inductive hypothesis for$k .$✷

Corollary 5.7. Let$\phi : \mathbb { Z } _ { N } \to \mathbb { Z } _ { N }$be a polynomial of degree$k _ { : }$, let$K =$ $( k ! ) ^ { 2 } 2 ^ { ( k + 1 ) ^ { 2 } }$, let$\alpha { > } 0$and let$r$be an integer exceeding max$\lbrace 2 ^ { 2 ^ { 4 0 k ^ { 2 } } } , ( 4 \pi / \alpha ) ^ { K } \rbrace$ Then, for any m$\geqslant r ^ { 1 - 1 / K }$, there is a partition of the set$\{ 0 , 1 , \ldots , r - 1 \}$ into arithmetic progressions$P _ { 1 } , \ldots , P _ { m }$such that the sizes of the$P _ { j }$difer by at most one, and if$f : \mathbb { Z } _ { N } \to D$is any function such that

$$
\left| \sum_ {s = 0} ^ {r - 1} f (s) \omega^ {- \phi (s)} \right| \geqslant \alpha r,
$$

then

$$
\sum_ {j = 1} ^ {m} \left| \sum_ {s \in P _ {j}} f (s) \right| \geqslant (\alpha / 2) r.
$$

Proof. By Corollary 5.6 we can choose$P _ { 1 } , \ldots , P _ { m }$such that diam$\left( \phi ( P _ { j } ) \right) =$ $N r ^ { - 1 / K }$for every$j .$By the second lower bound for r, this is at most $\alpha N / 4 \pi$. Exactly as in the proof of Corollary 2.3, this implies the result. ✷

Corollary 5.8. Let$A \subset \mathbb { Z } _ { N }$be a set of cardinality δN with balanced function$f .$Suppose that we can find disjoint arithmetic progressions $P _ { 1 } , \dots , P _ { M }$such that$A \subset \cup _ { i } P _ { i }$, and polynomials$\phi _ { 1 } , \ldots , \phi _ { M }$of degree at most k such that

$$
\sum_ {i = 1} ^ {M} \Big | \sum_ {s \in P _ {i}} f (s) \omega^ {- \phi_ {i} (s)} \Big | \geqslant \alpha N.
$$

Suppose also that$| P _ { i } | \leqslant 2 | P _ { j } |$for all$i , j$. Then there is an arithmetic progression$Q$of cardinality at least$( N / M ) ^ { 1 / K } / 8$such that$| A \cap Q | \ \geqslant$ $( \delta + \alpha / 8 ) | Q |$

Proof. We know that no$P _ { i }$has cardinality more than 2N/M. By Corollary 5.7, if m$\leqslant C ( 2 N / M ) ^ { 1 - 1 / K }$, each$P _ { i }$can be partitioned into arithmetic progressions$P _ { i 1 } , \ldots , P _ { i m }$such that

$$
\sum_ {j = 1} ^ {m} \Big | \sum_ {s \in P _ {i j}} f (s) \Big | \geqslant \frac {1}{2} \Big | \sum_ {s \in P _ {i}} f (s) \omega^ {- \phi_ {i} (s)} \Big |.
$$

Summing over i, we find that

$$
\sum_ {i = 1} ^ {M} \sum_ {j = 1} ^ {m} \left| \sum_ {s \in P _ {i j}} f (s) \right| \geqslant \alpha N.
$$

Since A is contained in the union of the$P _ { i j }$we also know that

$$
\sum_ {i = 1} ^ {M} \sum_ {j = 1} ^ {m} \sum_ {s \in P _ {i j}} f (s) = 0.
$$

Let$\begin{array} { r } { F _ { i j } = \sum _ { s \in P _ { i j } } f ( s ) } \end{array}$and let J be the set of$( i , j )$such that$F _ { i j } \geqslant 0$. Then the inequalities above imply that$\sum _ { ( i , j ) \in J } F _ { i j } \geqslant \alpha N / 4$, so we can find$P _ { i j }$ with$\sum _ { s \in P _ { i j } } f ( s ) \ \geqslant \ \alpha N / 4 M m$. Since$| P _ { i j } | \leqslant 4 N / M m$, this shows that $| A \cap P _ { i j } | \geqslant ( \delta + \alpha / 1 6 ) | P _ { i j } |$✷

We have now finished one of the key stages in the proof. As promised in the introduction to this section, if we want to generalize Roth’s argument, we may now look for “polynomial bias”, rather than the “linear bias” which arises there, since polynomial bias implies linear bias on small subprogressions.

We continue the section with three results that generalize Lemma 5.5 and Corollary 5.6 to statements dealing with several polynomials at once. These generalizations will not be needed for progressions of length four, but they are very important for progressions of length six or more, and the next lemma is needed for progressions of length five (in the case$k = 2 )$ Our methods of proof are extremely crude, and it is quite likely that much better bounds are known. However, we have not been able to find them and the poor bounds here do not greatly afect the estimate we shall eventually obtain for Szemer´edi’s theorem.

Lemma 5.9. Let$\phi _ { 1 } , \ldots , \phi _ { q }$be polynomials from$\mathbb { Z } _ { N }$to$\mathbb { Z } _ { N }$of degree at most k, let$K = ( k ! ) ^ { 2 } 2 ^ { ( k + 1 ) ^ { 2 } }$and let r be an integer exceeding$2 ^ { 2 ^ { 4 0 k ^ { 2 } } K ^ { q - 1 } }$ Then for every m$\geqslant r ^ { 1 - 1 / 2 K ^ { q } }$the set$\{ 0 , 1 , 2 , \ldots , r - 1 \}$can be partitioned into arithmetic progressions$P _ { 1 } , \ldots , P _ { m }$such that the diameter of$\phi _ { i } ( P _ { j } )$is at most$r ^ { - 1 / K ^ { q } } N$for every i and every$j ,$, and the lengths of any two$P _ { j }$ difer by at most 1.

Proof. First we prove by induction that for every$p \leqslant q$we can partition the set$\{ 0 , 1 , \ldots , r - 1 \}$into arithmetic progressions$P _ { 1 } , \ldots , P _ { m }$of size at least$r ^ { 1 / \dot { K } ^ { p } }$such that diam$\phi _ { i } ( P _ { j } )$is at most$r ^ { - 1 / K ^ { p } } N$for every$i \leqslant p$and $j \leqslant m$. When$p = 1$this follows immediately from Corollary 5.6. If we know it for$p - 1$, let$Q _ { 1 } , \ldots , Q _ { l }$be the arithmetic progressions obtained. The size of each$Q _ { i }$is at least$r ^ { 1 / K ^ { p - 1 } } \geqslant 2 ^ { 2 ^ { 4 0 k ^ { 2 } } }$, so by Corollary 5.6 each$Q _ { i }$ can be partitioned into further arithmetic progressions$P _ { j }$of cardinality at least$( r ^ { 1 / K ^ { p - 1 } } ) ^ { 1 / K } = r ^ { 1 / K ^ { p } }$, such that, for every$j ,$, the diameter of$\phi _ { q } ( P _ { j } )$ is at most$( r ^ { - 1 / K ^ { p - 1 } } ) ^ { 1 / K } N = r ^ { - 1 / K ^ { p } } N$. This is clearly enough to give us the statement for$p .$

In particular, we have the statement when$p = q$. To obtain the lemma, notice that if$k ^ { 2 } \leqslant m$, then an arithmetic progression of length m can be partitioned into subprogressions each of which has length k or$k + 1$✷

We are now going to prove a similar result for multilinear functions, which in this context means functions of the form

$$
\mu (x _ {1}, \dots , x _ {k}) = \sum_ {A \subset [ k ]} c _ {A} \prod_ {j \in A} x _ {j}.
$$

Define a box in$\mathbb { Z } _ { N } ^ { k }$of common diference d to be a product$\scriptstyle P = Q _ { 1 } \times \dots \times Q _ { k } ,$ where each$Q _ { i }$is an arithmetic progression in$\mathbb { Z } _ { N }$(even when$\mathbb { Z } _ { N }$is embedded into$\mathbb { Z } )$of common diference$d .$The width of$P$is defined to be min$| Q _ { i } |$

Lemma 5.10. Let$k \geqslant 2$, let$K = k ^ { 2 } 2 ^ { k + 3 }$, let$m \geq 2 ^ { K ^ { 2 ^ { k } } 2 ^ { 3 2 k ^ { 2 } + 1 } }$, let$P$be $\mathrm { a }$box in$\mathbb { Z } _ { N } ^ { k }$of width at least m and let$\mu$be a k-linear function from$P$ to$\mathbb { Z } _ { N }$. Then$P$can be partitioned into boxes$P _ { 1 } , \ldots , P _ { M }$, such that each$P _ { j }$ has width at least$m ^ { K ^ { - 2 ^ { k } } }$and the diameter of$\mu ( P _ { j } )$is at most 2m<sup>−</sup>$\cdot K ^ { - 2 ^ { k } } N$ for every$j$.

Proof. As noted above,$\mu$can be written as a sum of terms of the form $c _ { A } \prod _ { j \in A } x _ { j }$. Take any total ordering on the subsets of$[ k ]$which extends the partial ordering by inclusion, and define the height of$\mu$to be the largest position in this ordering of a set$A$such that the coeficient$c _ { A }$is non-zero. We shall prove the result by induction on the height. The precise inductive hypothesis is that if$\mu$has height at most$p ,$then any box Q of width $t \geq 2 ^ { K ^ { p } 2 ^ { 3 2 k ^ { 2 } + 1 } }$can be partitioned into boxes$Q _ { j }$of width at least$t ^ { K ^ { - p } }$such that for every$j$the diameter of$\mu ( Q _ { j } )$is at most$( 1 + 2 ^ { - k } p ) t ^ { - K ^ { - p } } N$

First, if the height is zero or one, then$\mu$is constant and the result is trivial. Now let$Q$be a box of width t and common diference$d _ { 0 }$, let $\mu : Q \to \mathbb { Z } _ { N }$be a k-linear function of height$p$and suppose that the result is true for all multilinear functions of height less than$p .$Let$A$be the$p ^ { \mathrm { t h } }$ set in the ordering on the subsets of [k], and let$c _ { A }$be the corresponding coeficient of$\mu .$.

By Lemma 5.5, we can find$r \leqslant t ^ { 1 / 2 }$, such that, setting$d = r d _ { 0 }$, we have the inequality$| c _ { A } d ^ { | A | } | \leqslant t ^ { - 1 / k 2 ^ { k + 2 } } N$. Now, for any$( x _ { 1 } , \dots , x _ { k } ) \in Q$ we can define a function$\nu$by

$$
\nu (b _ {1}, \dots , b _ {k}) = \mu (x _ {1} + d b _ {1}, \dots , x _ {k} + d b _ {k})
$$

and write it in the form

$$
\nu (b _ {1}, \dots , b _ {k}) = \sum_ {B \subset [ k ]} c _ {B} ^ {\prime} d ^ {| B |} \prod_ {j \in B} b _ {j}.
$$

It is not hard to see that, because$\mu$has height$p ,$so does$\nu ,$and also that $c _ { A } ^ { \prime } = c _ { A }$, whatever the choice of$( x _ { 1 } , \ldots , x _ { k } )$. Therefore, we can write

$$
\nu (b _ {1}, \dots , b _ {k}) = c _ {A} d ^ {| A |} \prod_ {j \in A} b _ {j} + \nu^ {\prime} (b _ {1}, \dots , b _ {k}),
$$

where$\nu ^ { \prime }$has height at most$p - 1$. If max$\{ b _ { 1 } , \ldots , b _ { k } \} \leqslant m ^ { 1 / k ^ { 2 } 2 ^ { k + 3 } }$, then our estimate for$c _ { A } d ^ { \vert A \vert }$implies that$\begin{array} { r } { \left| c _ { A } d ^ { | A | } \prod _ { i \in A } b _ { j } \right| \leqslant t ^ { - 1 / k 2 ^ { k + 3 } } N } \end{array}$

Now we are almost finished. Since$r \leqslant t ^ { 1 / 2 }$, there is no problem in partitioning$Q$into boxes of common diference d and width$t ^ { 1 / \dot { k } ^ { 2 } 2 ^ { k + 3 } } = t ^ { 1 / \dot { K } }$. In each such box, we have shown that$\mu$can be written as a sum$\nu _ { 1 } + \nu _ { 2 }$of multilinear functions such that$\nu _ { 1 }$is bounded above in size by$t ^ { - 1 / k 2 ^ { k + 3 } } { \cal N }$and$\nu _ { 2 }$ has height at most$p { - } 1$(with the functions$\nu _ { 1 }$and$\nu _ { 2 }$depending on the box). By induction, each such box can be further partitioned into boxes of width at least$t ^ { 1 / K ^ { p } }$such that$\nu _ { 2 }$has diameter at most$( 1 + ( p - 1 ) 2 ^ { - k } ) t ^ { - K ^ { - p } } N$ Since

$$
t ^ {- 1 / k} 2 ^ {k + 2} N + \big (1 + 2 ^ {- k} (p - 1) \big) t ^ {- K ^ {- p}} N \leqslant (1 + 2 ^ {- k} p) t ^ {- K ^ {- p}} N,
$$

we have proved the inductive hypothesis for p and hence the whole lemma. ✷

It is now not hard to deduce a multiple version of the above lemma.

Corollary 5.11. Let k$\geqslant 2$, let$K = k ^ { 2 } 2 ^ { k + 3 }$, let P be a box in$\mathbb { Z } _ { N } ^ { k }$of width at least$m \geqslant 2 ^ { K ^ { 2 ^ { k } q } 2 ^ { 3 2 k ^ { 2 } + 1 } }$and let$\mu _ { 1 } , \ldots , \mu _ { q }$be k-linear functions from$P$to$\mathbb { Z } _ { N }$. Then$P$can be partitioned into boxes$P _ { 1 } , \dots , P _ { M }$, such that each$P _ { j }$has width at least$m ^ { K ^ { - 2 ^ { k } q } }$and the diameter of$\mu _ { i } ( P _ { j } )$is at most 2m$\cdot K ^ { - 2 ^ { k } q } N$for every i and$j$.

Proof. We can apply Lemma 5.10 q times, obtaining a sequence of finer and finer partitions into boxes, such that for each refinement another of the$\mu _ { i }$satisfies the conclusion of that lemma. The width of the boxes at the final stage of this process is at least the number obtained by raising m to the power$K ^ { - 2 ^ { k } }$q times, which is$m ^ { K ^ { - 2 ^ { k } q } }$. The worst estimate for the diameter comes at the last refinement, and gives$2 m ^ { - K ^ { - 2 ^ { k } q } } N$✷

To end this section, we now give four simple lemmas, all of which are closely related to results that have already appeared in this paper (such as Lemma 2.3, Lemma 2.4 and Corollary 2.5). It will be convenient to have them stated explicitly.

Lemma 5.12. Let$Q \subset \mathbb { Z } _ { N }$be a mod-N arithmetic progression of size$m$ Then$Q$can be partitioned into$4 m ^ { 1 / 2 }$proper arithmetic progressions.

Proof. Let$Q = \{ a , a + d , \ldots , a + ( m - 1 ) d \}$. By the pigeonhole principle we can find distinct integers$l _ { 1 }$and$l _ { 2 }$lying in the interval$[ 0 , m ^ { 1 / 2 } ]$such that $| l _ { 1 } d - l _ { 2 } d | \leqslant m ^ { - 1 / 2 } N$and hence l lying in the interval$( 0 , m ^ { 1 / 2 } )$such that $| l d | \leqslant m ^ { - 1 / 2 } N$. We can partition$Q$into l mod-N arithmetic progressions $R _ { 1 } , \ldots , R _ { l }$each of which has common diference$l d$and length at least$m ^ { 1 / 2 }$ Each$R _ { i }$can be partitioned into mod-N arithmetic progressions$S _ { j }$of common diference ld and length between$m ^ { 1 / 2 }$and$m$. Of these there can be at most$2 m ^ { 1 / 2 }$. Finally, each$S _ { j }$can be split into at most two parts, each of which is a proper arithmetic progression.✷

Lemma 5.13. Let$Q _ { 1 } , \ldots , Q _ { M }$be mod-N arithmetic progressions that form a partition of$\mathbb { Z } _ { N }$. There is a refinement of this partition consisting of at most 4 NM proper arithmetic progressions.

Proof. Let$Q _ { i }$have cardinality$m _ { i }$. By Lemma 18.1, one can partition$Q _ { i }$ into at most$4 m _ { i } ^ { 1 / 2 }$proper arithmetic progressions. Since$m _ { 1 } + \ldots + m _ { M } = N$ the Cauchy-Schwarz inequality tells us that$4 ( m _ { 1 } ^ { 1 / 2 } + \dots + m _ { M } ^ { 1 / 2 } ) { \leqslant } 4 { \sqrt { M N } }$. ✷ Lemma 5.14. Let$\phi : \mathbb { Z } _ { N } \to \mathbb { Z } _ { N }$be a polynomial of degree k and let $K = ( k ! ) ^ { 2 } 2 ^ { k ^ { 2 } }$. Let$f : \mathbb { Z } _ { N } \to [ - 1 , 1 ]$and let$Q _ { 1 } , \ldots , Q _ { M }$be arithmetic progressions such that

$$
\sum_ {i = 1} ^ {M} \left| \sum_ {s \in Q _ {i}} f (s) \omega^ {- \phi (s)} \right| \geqslant \alpha N.
$$

There is a refinement of$Q _ { 1 } , \ldots , Q _ { M }$consisting of arithmetic progressions $R _ { 1 } , \dots , R _ { L }$such that$L \leqslant C M ^ { 1 / K } N ^ { 1 - 1 / K }$and

$$
\sum_ {j = 1} ^ {L} \left| \sum_ {s \in R _ {j}} f (s) \right| \geqslant (\alpha / 2) N.
$$

Proof. Let$m _ { i }$be the cardinality of$Q _ { i }$and let$\alpha _ { i }$be defined by the equation

$$
\left| \sum_ {s \in Q _ {i}} f (s) \omega^ {- \phi (s)} \right| = \alpha_ {i} | Q _ {i} |.
$$

Our assumption is that$\begin{array} { r } { \sum _ { i = 1 } ^ { M } \alpha _ { i } | Q _ { i } | \geqslant \alpha N } \end{array}$. By Corollary 5.7, each$Q _ { i }$can be partitioned into at most$C m _ { i } ^ { 1 - 1 / K }$subprogressions$Q _ { i 1 } , \ldots , Q _ { i M _ { i } }$such thatM

$$
\sum_ {j = 1} ^ {M _ {i}} \left| \sum_ {s \in Q _ {i j}} f (s) \right| \geqslant (\alpha_ {i} / 2) | Q _ {i} |,
$$

so, summing over$i ,$we have the inequality

$$
\sum_ {i = 1} ^ {M} \sum_ {j = 1} ^ {M _ {i}} \left| \sum_ {s \in Q _ {i j}} f (s) \right| \geqslant (\alpha / 2) N.
$$

The number of sets we have used is at most$C \sum _ { i = 1 } ^ { M } m _ { i } ^ { 1 - 1 / K }$. Since$\textstyle \sum _ { i = 1 } ^ { M } m _ { i }$ $= N$, this is at most$C M ^ { 1 / K } N ^ { 1 - 1 / K }$, by H¨older’s inequality.✷

Lemma 5.15. Let$f : \mathbb { Z } _ { N } \to [ - 1 , 1 ]$, suppose that$\textstyle \sum _ { s } f ( s ) = 0$and let $P _ { 1 } , \ldots , P _ { M }$be sets partitioning$\mathbb { Z } _ { N }$such that

$$
\sum_ {j = 1} ^ {M} \Big | \sum_ {s \in P _ {j}} f (s) \Big | \geqslant \alpha N.
$$

Then there exists$j$such that$\textstyle \sum _ { s \in P _ { i } } f ( s ) \geqslant \alpha | P _ { j } | / 4$and$\left| P _ { j } \right| \geqslant \alpha N / 4 M .$

Proof. For each$j$let$a _ { j } = \operatorname* { m a x } \Bigl \{ 0 , \sum _ { s \in P _ { j } } f ( s ) \Bigr \}$. The hypotheses about the function$f$imply that$\textstyle \sum _ { j = 1 } ^ { M } a _ { j } \stackrel { \textstyle \sum } { \geqslant } \alpha N / 2$. However,

$$
\sum \left\{a _ {j}: a _ {j} <   \alpha | Q _ {j} | / 4 \right\} <   \alpha N / 4
$$

and

$$
\sum \left\{a _ {j}: | Q _ {j} | <   \alpha N / 4 m \right\} <   \alpha N / 4
$$

(as$a _ { j } \leqslant | Q _ { j } | )$so there must be other values of$j$contributing to$\textstyle \sum _ { j = 1 } ^ { M } a _ { j }$ This proves the lemma.✷

## 6 Somewhat Additive Functions

We saw in §4 that it is possible for a set A to have small Fourier coeficients, but for$A \cap ( A + k )$to have at least one non-trivial large Fourier coeficient for every k. Moreover, the obvious conjecture concerning such sets, that they correlate with some function of the kind$\omega ^ { q ( s ) }$where$q$is a quadratic polynomial, is false. The aim of the next three sections is to show that such a set A must nevertheless exhibit quadratic bias of some sort. We will then be able to use the results of the last section to find linear bias, which will complete the proof for progressions of length four. The generalization to longer progressions will use similar ideas, but involves one extra important dificulty.

Notice that what we are trying to prove is very natural. If we replace A by a function on$\mathbb { Z } _ { N }$of the form$f ( s ) = \omega ^ { \phi ( s ) }$, where$\phi : \mathbb { Z } _ { N } \to \mathbb { Z } _ { N }$ then we are trying to prove that${ \mathrm { i f } } ,$for many k, the function$\phi _ { k } ( s ) =$ $\phi ( s ) - \phi ( s - k )$has some sort of linearity property, resulting in a large Fourier coeficient for the diference function$\Delta ( f ; k ) = \omega ^ { \phi ( s ) - \phi ( s - k ) }$, then$\phi$ itself must in some way be quadratic. Many arguments in additive number theory (in particular Weyl’s inequality) use the fact that taking diference functions reduces the degree of, and hence simplifies, a polynomial. We are trying to do something like the reverse process, “integrating” rather than “diferentiating” and showing that the degree goes up by one. This is another sense in which we are engaged in an inverse problem.

This section contains a simple but crucial observation, which greatly restricts the possibilities for the Fourier coeficients of$A \cap ( A + k )$that are large. Let A be a set which is not quadratically α-uniform and let$f$be the balanced function of A. Then there are at least$\alpha N$values of k such that

we can find r for which

$$
\left| \sum_ {s} f (s) f (s - k) \omega^ {- r s} \right| \geqslant \alpha N.
$$

Letting B be the set of k for which such an r exists, we can find a function $\phi : B \to \mathbb { Z } _ { N }$such that

$$
\sum_ {k \in B} \left| \sum_ {s} f (s) f (s - k) \omega^ {- \phi (k) s} \right| ^ {2} \geqslant \alpha^ {3} N ^ {3}.
$$

We shall show that the function$\phi$has a weak-seeming property which we shall call γ-additivity, for a certain constant$\gamma > 0$to be defined later. Using a variant of Freiman’s theorem proved in the next section, we shall show that this property gives surprisingly precise information about$\phi .$

Proposition 6.1. Let$\alpha > 0$, let$f : \mathbb { Z } _ { N } \to D$, let$B \subset \mathbb { Z } _ { N }$and let $\phi : B \to \mathbb { Z } _ { N }$be a function such that

$$
\sum_ {k \in B} \left| \Delta (f; k) ^ {\wedge} (\phi (k)) \right| ^ {2} \geqslant \alpha N ^ {3}.
$$

Then there are at least$\alpha ^ { 4 } N ^ { 3 }$quadruples$( a , b , c , d ) \in B ^ { 4 }$such that$a + b =$ c + d and$\phi ( a ) + \phi ( b ) = \phi ( c ) + \phi ( d )$

Proof. Expanding the left-hand side of the inequality we are assuming gives us the inequality

$$
\sum_ {k \in B} \sum_ {s, t} f (s) \overline {{f (s - k) f (t)}} f (t - k) \omega^ {- \phi (k) (s - t)} \geqslant \alpha N ^ {3}.
$$

If we now introduce the variable$u = s - t$we can rewrite this as

$$
\sum_ {k \in B} \sum_ {s, u} f (s) \overline {{f (s - k) f (s - u)}} f (s - k - u) \omega^ {- \phi (k) u} \geqslant \alpha N ^ {3}.
$$

Since$| f ( x ) | \leqslant 1$for every x, it follows that

$$
\sum_ {u} \sum_ {s} \left| \sum_ {k \in B} \overline {{f (s - k)}} f (s - k - u) \omega^ {- \phi (k) u} \right| \geqslant \alpha N ^ {3},
$$

which implies that

$$
\sum_ {u} \sum_ {s} \left| \sum_ {k \in B} \overline {{f (s - k)}} f (s - k - u) \omega^ {- \phi (k) u} \right| ^ {2} \geqslant \alpha^ {2} N ^ {4}.
$$

For each u and x let$f _ { u } ( x ) = \overline { { f ( - x ) } } f ( - x - u )$and let$g _ { u } ( x ) = B ( x ) \omega ^ { \phi ( x ) u }$ The above inequality can be rewritten

$$
\sum_ {u} \sum_ {s} \left| \sum_ {k} f _ {u} (k - s) \overline {{g _ {u} (k)}} \right| ^ {2} \geqslant \alpha^ {2} N ^ {4}.
$$

By Lemma 2.1, we can rewrite it again as

$$
\sum_ {u} \sum_ {r} | \hat {f} _ {u} (r) | ^ {2} | \hat {g} _ {u} (r) | ^ {2} \geqslant \alpha^ {2} N ^ {5}.
$$

Since$\begin{array} { r } { \sum _ { r } | \hat { f } ( r ) | ^ { 4 } \leqslant N ^ { 4 } } \end{array}$, the Cauchy-Schwarz inequality now implies that

$$
\sum_ {u} \left(\sum_ {r} | \hat {g} _ {u} (r) | ^ {4}\right) ^ {1 / 2} \geqslant \alpha^ {2} N ^ {3}.
$$

Applying the Cauchy-Schwarz inequality again, we can deduce that

$$
\sum_ {u, r} | \hat {g} _ {u} (r) | ^ {4} = \sum_ {u, r} \Bigl | \sum_ {k \in B} \omega^ {\phi (s) u - r s} \Bigr | ^ {4} \geqslant \alpha^ {4} N ^ {5}.
$$

Expanding the left-hand side of this inequality we find that

$$
\sum_ {u, r} \sum_ {a, b, c, d \in B} \omega^ {u (\phi (a) + \phi (b) - \phi (c) - \phi (d))} \omega^ {- r (a + b - c - d)} \geqslant \alpha^ {4} N ^ {5}.
$$

But now the left-hand side is exactly$N ^ { 2 }$times the number of quadruples $( a , b , c , d ) \in B ^ { 4 }$for which$a + b = c + d$and$\phi ( a ) + \phi ( b ) = \phi ( c ) + \phi ( d )$. This proves the proposition.✷

If G is an Abelian group and$a , b , c ,$d are elements of G such that $a + b = c + d ,$we shall say that$( a , b , c , d )$is an additive quadruple. Given a subset$B \subset \mathbb { Z } _ { N }$and a function$\phi : B \to \mathbb { Z } _ { N }$, let us say that a quadruple $( a , b , c , d ) \in B ^ { 4 }$is φ-additive if it is additive and in addition$\phi ( a ) + \phi ( b ) =$ $\phi ( c ) + \phi ( d )$. Let us say also that$\phi$is γ-additive if there are at least$\gamma N ^ { 3 } \ \phi -$ additive quadruples. It is an easy exercise to show that if$\gamma = 1$then$B$must be the whole of$\mathbb { Z } _ { N }$and$\phi : \mathbb { Z } _ { N } \to \mathbb { Z } _ { N }$must be of the form$\phi ( x ) = \lambda x + \mu _ { \ O }$ i.e., linear. Notice that the property of γ-additivity appeared, undefined, in$\ S 4$during the discussion of the function$\phi _ { k }$. Let us now give a simple but useful reformulation of the concept of γ-additivity.

Lemma 6.2. Let$\gamma > 0$, let$B \subset \mathbb { Z } _ { N }$, let$\phi : B \to \mathbb { Z } _ { N }$be a$\gamma \mathrm { - } \mathrm { a } d d i t i$ve function and let$\Gamma \subset \mathbb { Z } _ { N } ^ { 2 }$be the graph of$\phi$. Then Γ contains at least$\gamma N ^ { 3 }$ additive quadruples (in the group$\mathbb { Z } _ { N } ^ { 2 } )$✷

As we have just remarked, a 1-additive function must be a linear. We finish this section with an important (and, in the light of the second example of$\ S 4 .$, natural) example of a γ-additive function which cannot be approximated by a linear function even though$\gamma$is reasonably large. Let $x _ { 1 } , \ldots , x _ { d } \in Z _ { N }$and$r _ { 1 } , \hdots , r _ { d } \in \mathbb { N }$be such that all the numbers$\textstyle \sum _ { i = 1 } ^ { d } a _ { i } x _ { i }$ with$0 \leqslant a _ { i } < r _ { i }$are distinct. Let$y _ { 1 } , \dots , y _ { d } \in \mathbb { Z } _ { N }$be arbitrary, and define

$$
\phi \bigg (\sum_ {i = 1} ^ {d} a _ {i} x _ {i} \bigg) = \sum_ {i = 1} ^ {d} a _ {i} y _ {i}.
$$

Let$\phi ( s )$be arbitrary for the other values of s. Then a simple calculation shows that the number of additive quadruples is at least$( 2 / 3 ) ^ { d } r _ { 1 } ^ { 3 } \ldots r _ { d } ^ { 3 } .$. If $r _ { 1 } \ldots r _ { d } = \beta N$, then$\phi$is$( 2 / 3 ) ^ { d } \beta ^ { 3 } .$-additive.

The function φ resembles a linear map between vector spaces, and the number d can be thought of as the dimension of the domain of the φ. In the next two sections we shall show that all γ-additive functions have, at least in part, something like the above form, with d not too large and$r _ { 1 } \ldots r _ { d }$ an appreciable fraction of N (both depending, of course, on γ).

## 7 Variations on a Theorem of Freiman

Let A be a subset of Z of cardinality m. It is easy to see that$A { + } A = \{ x { + } y :$ $x , y \in A \}$has cardinality between 2m − 1 and$m ( m + 1 ) / 2$. Suppose that $| A + A | \leqslant C m$for some constant C. What information does this give about the set$A ?$This problem is called an inverse problem of additive number theory, since it involves deducing the structure of A from the behaviour of$A + A \ -$in contrast to a direct problem where properties of A give information about$A + A$

It is clear that$A + A$will be small when A is a subset of an arithmetic progression of length not much greater than m. After a moment’s thought, one realises that there are other examples. For instance, one can take a “progression of progressions” such as$\{ a M + b : 0 \leqslant a < h , 0 \leqslant b < k \}$ where$M \gg k$and$h k = m$. This example can then be generalized to a large subset of a “d-dimensional” arithmetic progression, provided that d is reasonably small. A beautiful and famous result of Freiman asserts that these simple examples exhaust all possibilities. A precise statement of the theorem is as follows.

Theorem 7.1.. Let C be a constant. There exist constants$d _ { 0 }$and K depending only on C such that whenever A is a subset of$\mathbb { Z }$with$| A | = m$ and$| A + A | \leqslant C m$, there exist$d \leqslant d _ { 0 }$, an integer x<sub>0</sub> and positive integers $x _ { 1 } , \ldots , x _ { d }$and$k _ { 1 } , \ldots , k _ { d }$such that$k _ { 1 } k _ { 2 } \ldots k _ { d } \leqslant K \ i$m and

$$
A \subset \left\{x _ {0} + \sum_ {i = 1} ^ {d} a _ {i} x _ {i}: 0 \leqslant a _ {i} <   k _ {i} (i = 1, 2, \dots , d) \right\}.
$$

The same is true$i f \left| A - A \right| \leqslant C m$

It is an easy exercise to deduce from Theorem 7.1 the same result for subsets of$\mathbb { Z } ^ { n }$, where$x _ { 0 } , x _ { 1 } , \ldots , x _ { d }$are now points in$\mathbb { Z } ^ { n }$. We shall in fact be interested in the case$n = 2$, since we shall be applying Freiman’s theorem to a graph coming from Proposition 6.1 and Lemma 6.2.

The number$k _ { 1 } k _ { 2 } \ldots k _ { d }$is called the size of the d-dimensional arithmetic progression. Note that this is not necessarily the same as the cardinality of the set since there may be numbers (or more generally points of$\mathbb { Z } ^ { D } )$ which can be written in more than one way as$\textstyle x _ { 0 } + \sum _ { i = 1 } ^ { d } a _ { i } x _ { i }$. When every such representation is unique, we shall call the set a proper d-dimensional arithmetic progression. (This terminology is all standard.)

Freiman’s original proof of Theorem 7.1 was long and very dificult to understand. Although a simplified version of his argument now exists [Bi], an extremely important breakthrough came a few years ago with a new and much easier proof by Ruzsa, which also provided a reasonable bound. This improved bound is very important for the purposes of our bound for Szemer´edi’s theorem. Full details of Ruzsa’s proof can be found in [Ru1,2,3] or in a book by Nathanson [N], which also contains all necessary background material.

We shall in fact need a modification of Freiman’s theorem, in which the hypothesis and the conclusion are weakened. In its qualitative form, the modification is a result of Balog and Szemer´edi. However, they use Szemer´edi’s uniformity lemma, which for us is too expensive. Our argument will avoid the use of the uniformity lemma and thereby produce a much better bound than the bound of Balog and Szemer´edi. It will be convenient (though not essential) to consider the version of Freiman’s theorem where $A - A$, rather than$A + A$is assumed to be small. Our weaker hypothesis concerns another parameter associated with a set$A .$, which has several descriptions, and which appeared at the end of the previous section in connection with the graph of the function$\phi .$. It is

$$
\left\| A * A \right\| _ {2} ^ {2} = \sum_ {k \in \mathbb {Z}} \left| A \cap (A + k) \right| ^ {2} = \left| \{(a, b, c, d) \in A ^ {4}: a - b = c - d \} \right|.
$$

(Freiman calls this invariant$M ^ { \prime }$in his book$[ \mathrm { F } 2 \ \mathrm { p } . 4 1 ] . \$It is a straightforward exercise to show that

$$
\left\| A * A \right\| _ {2} ^ {2} \leqslant m ^ {2} + 2 \left(1 ^ {2} + \dots + (m - 1) ^ {2}\right)
$$

with equality if and only if$A$is an arithmetic progression of length$m$. The Balog-Szemer´edi theorem is the following result.

Theorem 7.2. Let A be a subset of$\cdot _ { \mathbb { Z } } D$of cardinality m and suppose that $\| A * A \| _ { 2 } ^ { 2 } \geqslant c _ { 0 } m ^ { 3 }$. Then there are constants$^ { c , }$K and$d _ { 0 }$depending only on $c _ { 0 }$and an arithmetic progression$P$of dimension d$\prime \leqslant d _ { 0 }$and size at most Km such that$| A \cap P | \geqslant$cm.

This result states that if$\| A * A \| _ { 2 } ^ { 2 }$is, to within a constant, as big as possible, then A has a proportional subset satisfying the conclusion of Freiman’s theorem. Notice that, qualitatively at least, the conclusion of Theorem 7.2 cannot be strengthened, since if A has a proportional subset B with$\| B * B \| _ { 2 } ^ { 2 }$large, then$\| A * A \| _ { 2 } ^ { 2 }$is large whatever$A \ \backslash \ B$is. To see that the new hypothesis is weaker, notice that if$| A - A | \leqslant C m$，then$A \cap ( A + k )$is empty except for at most Cm values of$k ,$while $\textstyle \sum _ { k \in \mathbb { Z } } | A \cap ( A + k ) | = m ^ { 2 }$. It follows from the Cauchy-Schwarz inequal-ity that$\begin{array} { r } { \sum _ { k \in \mathbb { Z } } | A \cap ( A + k ) | ^ { 2 } \geqslant m ^ { 3 } / C } \end{array}$

The most obvious approach to deducing Theorem 7.2 from Theorem 7.1 is to show that a set satisfying the hypothesis of Theorem 7.2 has a large subset satisfying the hypothesis of Theorem 7.1. This is exactly what Balog and Szemer´edi did and we shall do as well.

Proposition 7.3. Let A be a subset of$\mathbb { Z } ^ { n }$of cardinality m such that $\| A * A \| _ { 2 } ^ { 2 } \geqslant c _ { 0 } m ^ { 3 }$. Then there are constants c and C depending only on c<sub>0</sub> and a subset$A ^ { \prime \prime } \subset A$of cardinality at least cm such that$| A ^ { \prime \prime } - A ^ { \prime \prime } | \leqslant C m$ Moreover, c and C can be taken as$2 ^ { - 2 0 } c _ { 0 } ^ { 1 2 }$and$2 ^ { 3 8 } c _ { 0 } ^ { - 2 4 }$respectively.

We shall need the following lemma for the proof.

Lemma 7.4. Let V be a set of size$m ,$let$\delta > 0$and let$A _ { 1 } , \ldots , A _ { n }$be subsets of V such that$\begin{array} { r } { \sum _ { x = 1 } ^ { n } \sum _ { y = 1 } ^ { n } | A _ { x } \cap A _ { y } | \geqslant \delta ^ { 2 } m n ^ { 2 } } \end{array}$. Then there is a subset$K \subset [ n ]$ <sub>of cardinality at least</sub>$2 ^ { - 1 / 2 } \delta ^ { 5 } n$such that for at least 90% of the pairs$( x , y ) \in K ^ { 2 }$the intersection$A _ { x } \cap A _ { y }$has cardinality at least $\delta ^ { 2 } m / 2$. In particular, the result holds$i f \left| A _ { x } \right| \geqslant$δm for every x.

Proof. For every$j \leqslant$m let$B _ { j } = \{ i : j \in A _ { i } \}$and let$E _ { j } = B _ { j } ^ { 2 }$. Choose five numbers$j _ { 1 } , \dotsc , j _ { 5 } \leqslant$m at random (uniformly and independently), and let $X = E _ { j _ { 1 } } \cap \cdots \cap E _ { j _ { 5 } }$. The probability$p _ { x y }$that a given pair$( x , y ) \in [ n ] ^ { 2 }$ belongs to$E _ { j _ { r } }$is m${ } ^ { \cdot 1 } | A _ { x } \cap A _ { y } |$, so the probability that it belongs to$X$ is$p _ { x y } ^ { 5 }$. By our assumption we have that$\bar { \sum _ { x , y = 1 } ^ { n } { p _ { x y } \geqslant \delta ^ { 2 } n ^ { 2 } } }$, which implies (by H¨older’s inequality) that$\textstyle \sum _ { x , y = 1 } ^ { n } p _ { x y } ^ { 5 } \geqslant \delta ^ { 1 0 } n ^ { 2 }$. In other words, the expected size of X is at least$\delta ^ { 1 0 } n ^ { 2 }$

Let Y be the set of pairs$( x , y ) \in X$such that$\vert A _ { x } \cap A _ { y } \vert < \delta ^ { 2 } m / 2$, or equivalently$p _ { x y } < \delta ^ { 2 } / 2$. Because of the bound on$p _ { x y } ,$the probability that $( x , y ) \in Y$is at most$( \delta ^ { 2 } / 2 ) ^ { 5 }$, so the expected size of$Y$is at most$\delta ^ { 1 0 } n ^ { 2 } / 3 2$

It follows that the expectation of$| X | - 1 6 | Y |$is at least$\delta ^ { 1 0 } n ^ { 2 } / 2$. Hence, there exist$j _ { 1 } , \dots , j _ { 5 }$such that$| X | \geqslant 1 6 | Y |$and$| X | \geqslant \delta ^ { 1 0 } n ^ { 2 } / 2$. It follows that the set$K = B _ { j _ { 1 } } \cap \cdot \cdot \cdot \cap B _ { j _ { 5 } }$satisfies the conclusion of the lemma.✷

Proof of Proposition 7.3. The function$f ( x ) = A * A ( x )$(from$\mathbb { Z } ^ { n }$to Z) is non-negative and satisfies$\| f \| _ { \infty } \leqslant m , \| f \| _ { 2 } ^ { 2 } \geqslant c _ { 0 } m ^ { 3 }$and$\| f \| _ { 1 } = m ^ { 2 }$. This implies that$f ( x ) \geqslant c _ { 0 } m / 2$for at least$c _ { 0 } m / 2$values of$x .$, since otherwise we could write$f = g + h$with$g$and h disjointly supported, g supported on fewer than$c _ { 0 } m / 2$points and$\| h \| _ { \infty } \leqslant c _ { 0 } m / 2$, which would tell us that

$$
\| f \| _ {2} ^ {2} \leqslant \| g \| _ {2} ^ {2} + \| h \| _ {\infty} \| h \| _ {1} <   (c _ {0} m / 2) m ^ {2} + (c _ {0} m / 2). m ^ {2} = c _ {0} m ^ {3}.
$$

Let us call a value of x for which$f ( x ) \geqslant c _ { 0 } m / 2$a popular diference and let us define a graph$G$with vertex set A by joining a to b if$b - a$(and hence $a - b )$is a popular diference. The average degree in G is at least$c _ { 0 } ^ { 2 } m / 4$2 so there must be at least$c _ { 0 } ^ { 2 } m / 8$vertices of degree at least$c _ { 0 } ^ { 2 } m / 8$. Let $\delta = c _ { 0 } ^ { 2 } / 8$, let$a _ { 1 } , \ldots , a _ { n }$be vertices of degree at least$c _ { 0 } ^ { 2 } m / 8 .$, with$\begin{array} { r } { n \geqslant \delta m , } \end{array}$ and let$A _ { 1 } , \ldots , A _ { n }$be the neighbourhoods of the vertices$a _ { 1 } , \ldots , a _ { n }$. By Lemma 7.4 we can find a subset$A ^ { \prime } \subset \{ a _ { 1 } , \ldots , a _ { n } \}$of cardinality at least $\delta ^ { 5 } n / \sqrt { 2 }$such that at least 90% of the intersections$A _ { i } \cap A _ { j }$with$a _ { i } , a _ { j } \in A ^ { \prime }$ are of size at least$\delta ^ { 2 } m / 2$. Set$\alpha = \delta ^ { 6 } / \sqrt { 2 }$so that$| A ^ { \prime } | \geqslant \alpha m$

Now define a graph H with vertex set$A ^ { \prime } .$, joining$a _ { i }$to$a _ { j }$if and only if$| A _ { i } \cap A _ { j } | \geqslant \delta ^ { 2 } m / 2$. The average degree of the vertices in H is at least $( 9 / 1 0 ) | A ^ { \prime } |$, so at least$| A ^ { \prime } | / 2$vertices have degree at least$4 | A ^ { \prime } | / 5$. Define $A ^ { \prime \prime }$to be the set of all such vertices.

We claim now that$A ^ { \prime \prime }$has a small diference set. To see this, consider any two elements$a _ { i } , a _ { j } \in A ^ { \prime \prime }$. Since the degrees of$a _ { i }$and$a _ { j }$are at least $( 4 / 5 ) | A ^ { \prime } |$in H, there are at least$( 3 / 5 ) | A ^ { \prime } |$points$a _ { k } \in A ^ { \prime }$joined to both $a _ { i }$and$a _ { j }$. For every such k we have$| A _ { i } \cap A _ { k } |$and$| A _ { j } \cap A _ { k } |$both of size at least$\dot { \delta } ^ { 2 } m / 2$. If$b \in A _ { i } \cap A _ { k }$, then both$a _ { i } - b$and$a _ { k } - b$are popular diferences. It follows that there are at least$c _ { 0 } ^ { 2 } m ^ { 2 } / 4$ways of writing$a _ { i } - a _ { k }$ as$( p - q ) - ( r - s )$, where$p , q , r , s \in A , p - q = a _ { i } - b$and$r - s = a _ { k } - b$ Summing over all$b \in A _ { i } \cap A _ { k }$, we find that there are at least$\delta ^ { 2 } c _ { 0 } ^ { 2 } m ^ { 3 } / 8$ways of writing$a _ { i } - a _ { k }$as$( p - q ) - ( r - s )$with$p , q , r , s \in A$. The same is true of $a _ { j } - a _ { k }$. Finally, summing over all k such that$a _ { k }$is joined in H to both$a _ { i }$ and$a _ { j }$, we find that there are at least$( 3 / 5 ) | A ^ { \prime } | \delta ^ { 4 } c _ { 0 } ^ { 4 } m ^ { 6 } / 6 4 \geqslant \alpha \delta ^ { 4 } c _ { 0 } ^ { 4 } m ^ { 7 } / 1 2 0$ ways of writing$a _ { i } - a _ { j }$in the form$\left( p - q \right) - \left( r - s \right) - \left( \left( t - u \right) - \left( v - w \right) \right)$ with$p , q , \dots , w \in A$

Since there are at most$m ^ { 8 }$elements in$A ^ { 8 }$, the number of diferences of elements of$A ^ { \prime \prime }$is at most$1 2 0 m / \alpha \delta ^ { 4 } c _ { 0 } ^ { 4 } \ \leqslant \ 2 ^ { 3 8 } m / c _ { 0 } ^ { 2 4 }$. Note also that the cardinality of$A ^ { \prime \prime }$is at least$( 1 / 2 ) \alpha m \geqslant c _ { 0 } ^ { 1 2 } m / 2 ^ { 2 0 }$. The proposition is proved.✷

It is possible to apply Theorem 7.2 as it stands in order to prove$\mathrm { S z e - }$ mer´edi’s theorem for progressions of length four (and quite possibly in general). Instead, we shall combine Proposition 7.3 with a weaker version of Freiman’s theorem that gives less information about the structure of a set A with small diference set. There are three advantages in doing this. The first is that with our weaker version we can get a much better bound. The second is that using the weaker version is cleaner, particularly when we come to the general case. The third is that the weaker version is easier to prove than Freiman’s theorem itself, as it avoids certain arguments from the geometry of numbers.

We shall not be concerned in this paper with arbitrary sets A such that$| A - A | \leqslant C | A |$, but rather with graphs of functions from subsets of$\mathbb { Z } _ { N }$to$\mathbb { Z } _ { N }$. We now prove a result for such functions. An important concept introduced by Freiman is that of a Freiman homomorphism (as it is now called). Let A and B be two subsets of Abelian groups. A function$\phi : A  B$is a Freiman homomorphism of order k if, whenever $a _ { 1 } , \dots , a _ { 2 k } \in A$and

$$
a _ {1} + \dots + a _ {k} = a _ {k + 1} + \dots + a _ {2 k},
$$

we have also

$$
\phi (a _ {1}) + \dots + \phi (a _ {k}) = \phi (a _ {k + 1}) + \dots + \phi (a _ {2 k}).
$$

Equivalently,$\phi$induces a well-defined function from kA to$k B ,$, where kA denotes the sum of k copies of the set A. When$k = 2$one speaks simply of a Freiman homomorphism. Note that a Freiman homomorphism of order 2k also induces a well-defined function from$k A - k A$to$k B - k B$. If$\phi$ has an inverse which is also a Freiman homomorphism of order k, then φ is said to be a Freiman isomorphism of order k. The next lemma shows that a function$\phi : B \subset \mathbb { Z } _ { N } \to \mathbb { Z } _ { N }$for which the graph has a small diference set can be restricted to a large subset of$B$on which it is a Freiman homomorphism of order$k .$This lemma plays the role in our proof that Theorem 2 of [Ru1] did in Ruzsa’s proof, and the proof is in a very similar spirit. Indeed, the whole scheme of our proof in the rest of this section is based on his ideas.

Lemma 7.5. Let$B \subset \mathbb { Z } _ { N }$and let$\phi : B \to \mathbb { Z } _ { N }$be a function with graph Γ. Suppose that$| \Gamma - \Gamma | \leqslant C | \Gamma |$. Then there is a subset$B ^ { \prime } \subset B$of size at least $| B | / 8 k C ^ { 4 k }$such that the restriction of$\phi$to$C$is a Freiman homomorphism of order k.

Proof. First, a theorem of Ruzsa [Ru2] (deduced from a result of Pl¨unnecke [P] for which Ruzsa discovered a simpler proof) implies that$| 4 k \Gamma - 4 k \Gamma | \leqslant$ $\bar { C } ^ { \bar { 4 } k } | \Gamma |$. If for some x we could find more than$C ^ { 4 k }$distinct values of$y$such that$( x , y ) \in 2 k \Gamma - 2 k \Gamma$, then for every$( z , w ) \in 2 k \Gamma - 2 k \Gamma$there would be more than$C ^ { 4 k }$distinct values of u such that$( z - x , u ) \in 4 k \Gamma - 4 k \Gamma$. But the number of z such that$( z , w ) \in 2 k \Gamma - 2 k \Gamma$for some w is certainly at least |Γ|, so this would contradict the upper bound for$| 4 k \Gamma - 4 k \Gamma |$

Therefore, there are in particular at most$C ^ { 4 k }$distinct values of y such that$( 0 , y ) { \in } 2 k \Gamma - 2 k \Gamma$. I$\dot { \mathbf { \eta } } ( x , y ) , ( x , y ^ { \prime } ) \in k \Gamma - k \Gamma$then$( 0 , y - y ^ { \prime } ) \in 2 k \Gamma - 2 k \Gamma$ Hence, there is a set K of size at most$C ^ { 4 k }$such that, writing$K _ { x }$for the set$\{ y : ( x , y ) \in k \Gamma - k \Gamma \}$, we have$K _ { x } - K _ { x } \subset K$for every x.

Now let$0 \leqslant M < N / 2$be even. For every$w \in \mathbb { Z } _ { N }$, there are exactly 2M non-zero values of d such that

$$
w \in \left\{- M d, - (M - 1) d, \dots , - 2 d, - d \right\} \cup \left\{d, 2 d, \dots , M d \right\},
$$

since the equation$a d = w$has a unique solution whenever$a \neq 0 .$. Therefore, the number of values of d for which$K \cap \{ d y : - M \leqslant y \leqslant M \} \neq \{ 0 \}$is at most$2 M C ^ { 4 k }$

Let d be such that if we define P to be$\{ d y : - M \leqslant y \leqslant M \}$then $K \cap P = \{ 0 \}$. Let$P ^ { \prime } = \{ d y : - M / 2 \leqslant y \leqslant M / 2 \}$, let$L \leqslant M / 2 k$and let $Q = \{ d y : 0 \leqslant y \leqslant L \}$. Define$\Gamma _ { a }$to be the set$\{ ( x , y ) \in \Gamma : y \in a + Q \}$

We claim that$\Gamma _ { a }$is the graph of a homomorphism of order k. If not, then we can find$( x _ { 1 } , y _ { 1 } ) , \dotsc , ( x _ { 2 k } , y _ { 2 k } )$and$( x _ { 1 } ^ { \prime } , y _ { 1 } ^ { \prime } ) , \ldots , ( x _ { 2 k } ^ { \prime } , y _ { 2 k } ^ { \prime } ) \in \Gamma _ { a }$such that

$$
x _ {1} + \dots + x _ {k} - x _ {k + 1} - \dots - x _ {2 k} = x _ {1} ^ {\prime} + \dots + x _ {k} ^ {\prime} - x _ {k + 1} ^ {\prime} - \dots - x _ {2 k} ^ {\prime},
$$

but

$$
y _ {1} + \dots + y _ {k} - y _ {k + 1} - \dots - y _ {2 k} \neq y _ {1} ^ {\prime} + \dots + y _ {k} ^ {\prime} - y _ {k + 1} ^ {\prime} - \dots - y _ {2 k} ^ {\prime},
$$

and hence$x , y , y ^ { \prime }$such that$y \neq y ^ { \prime }$and$( x , y ) , ( x , y ^ { \prime } ) \in k \Gamma _ { a } - k \Gamma _ { a }$. However, $k \Gamma _ { a } - k \Gamma _ { a }$is the set of all points of the form

$$
\left(x _ {1} + \dots + x _ {k} - x _ {k + 1} - \dots - x _ {2 k}, y _ {1} + \dots + y _ {k} - y _ {k + 1} - \dots - y _ {2 k}\right)
$$

such that$( x _ { i } , y _ { i } ) \in \Gamma$and$y _ { i } \in a + Q$for every i. This is a subset of $\{ ( x , y ) \in k \Gamma - k \Gamma : y \in P ^ { \prime } \} = \{ ( x , y ) : y \in K _ { x } \cap P ^ { \prime } \}$. It follows that $( K _ { x } - K _ { x } ) \cap ( P ^ { \prime } - P ^ { \prime } )$is non-empty and hence that$K \cap P$is non-empty, which is a contradiction.

Therefore, as long as$2 M C ^ { 4 k } < N - 1$, we can find a value of d such that$\Gamma _ { a }$is the graph of a homomorphism for every a. The average size of $\Gamma _ { a }$is$( L + 1 ) | \Gamma | / N$, so if we choose M to be at least$N / 4 C ^ { 4 k }$and L to be at least$( M / 2 k ) - 1$, as we may, then we can find a such that the size of$\Gamma _ { a }$ is at least$| \Gamma | / 8 k C ^ { 4 k }$✷

Let us now collect what we have done so far into a single result, specialized to the case$k = 8$

Corollary 7.6. Let$B _ { 0 } \subset \mathbb { Z } _ { N }$have cardinality αN, and let$\phi : B _ { 0 } \to \mathbb { Z } _ { N }$ have$\gamma ( \alpha N ) ^ { 3 }$additive quadruples. Then there is a subset$B \subset B _ { 0 }$of cardinality at least$2 ^ { - 1 8 8 2 } \gamma ^ { 1 1 6 4 } \alpha N$such that the restriction of$\phi$to B is a homomorphism of order 8.

Proof. By Proposition 7.3 we can find a subset$B _ { 1 } \subset B _ { 0 }$of cardinality at least$2 ^ { - 2 0 } \gamma ^ { 1 2 } \alpha N$such that, letting Γ be the graph of φ restricted to$B _ { 1 }$, we have$| \Gamma - \Gamma | \leqslant 2 ^ { 5 8 } \gamma ^ { - 3 6 } | \Gamma |$. Let$C = 2 ^ { 5 8 } \gamma ^ { - 3 6 }$. By Lemma 7.5 we can restrict $\phi$to a subset$B \subset B _ { 1 }$of cardinality at least$| \bar { B } _ { 1 } | / 6 4 C ^ { 3 2 } \geqslant 2 ^ { - 1 8 8 2 } \gamma ^ { 1 1 6 4 } \alpha N$ such that it becomes a homomorphism of order 8.✷

The next lemma is a variant of an argument of Bogolyubov [B]. The original argument was used by Ruzsa in his proof of Freiman’s theorem. Given a subset$K \subset \mathbb { Z } _ { N }$and$\delta > 0$, let us define the Bohr neighbourhood $B ( K , \delta )$to be the set of all$d \in \mathbb { Z } _ { N }$such that$| s d | \leqslant \delta N$for every$s \in K$. An elementary fact about Bohr neighbourhoods is contained in the next lemma, which is another well-known application of Dirichlet’s “box” principle.

Lemma 7.7. Let K be a subset of$\mathbb { Z } _ { N }$and let$\delta > 0$. Then the cardinality of the Bohr neighbourhood$B ( K , \delta )$is at least$( \delta / 2 ) ^ { | K | } N$. In particular, if $\delta > ( N / 2 ) ^ { - 1 / | K | }$then$B ( K , \delta )$contains a non-zero element.

Proof. Let the elements of K be$r _ { 1 } , \ldots , r _ { k }$, and let φ be the mapping from $\mathbb { Z } _ { N }$to$\mathbb { Z } _ { N } ^ { k }$defined by$\phi : x \mapsto \left( r _ { 1 } x , \ldots , r _ { k } x \right)$. Let$m = \lceil \delta ^ { - 1 } \rceil$and for $1 \leqslant j \leqslant \varkappa$m let$I _ { j } = \{ x \in \mathbb { Z } _ { N } : ( j - 1 ) N / m \leqslant x < j N / m \}$. There are exactly$m ^ { k }$possible products of k of the intervals$I _ { j } ,$so one of them,$Q$ say, must contain$\phi ( x )$for at least$m ^ { - k } N$values of$x \in \mathbb { Z } _ { N }$. Let C be the set of x such that$\phi ( x ) \in Q$. Then it is easy to see that$C - C \subset B$ Clearly also$| C - C | \geqslant | C |$. The lemma now follows from the observation that m$^ { - 1 } \geqslant \delta / 2$✷

Another useful remark about Bohr neighbourhoods is that $B ( K , \delta _ { 1 } ) + B ( K , \delta _ { 2 } ) \subset B ( K , \delta _ { 1 } + \delta _ { 2 } )$. Further facts about them will be proved in §10.

Lemma 7.8. Let$A \subset \mathbb { Z } _ { N }$be a set of size αN and let$\phi : A  \mathbb { Z } _ { N }$be a Freiman homomorphism of order 8. Let$K = \{ r \in \mathbb { Z } _ { N } : | \hat { A } ( r ) | \geqslant \alpha ^ { 3 / 2 } N / 4 \}$ Then K has cardinality at most 16α<sup>−2</sup>, and there is a homomorphism $\psi : B ( K , \alpha / 3 2 \pi ) \to \mathbb { Z } _ { N }$such that$\phi ( x ) - \phi ( y ) = \psi ( x - y )$whenever$x , y \in A$ and$x - y \in B ( K , \alpha / 3 2 \pi )$

Proof. Let g be the function$A * A * A * A$. Then$\hat { g } ( \boldsymbol r ) = | \hat { A } ( \boldsymbol r ) | ^ { 4 }$and $\begin{array} { r } { g ( r ) = N ^ { - 1 } \sum _ { r } | \hat { A } ( r ) | ^ { 4 } \omega ^ { r x } } \end{array}$for every$r \in \mathbb { Z } _ { N }$. Let$\lambda = \alpha ^ { 3 / 2 } / 4$so that

$K = \{ r : | \hat { A } ( r ) | \geqslant \lambda N \}$. Since$\| \hat { A } \| ^ { 2 } = \alpha N ^ { 2 }$, we have$\lambda ^ { 2 } N ^ { 2 } | K | \leqslant \alpha N ^ { 2 }$and hence$| K | \leqslant \alpha \lambda ^ { - 2 } = 1 \overset { \cdot } { 6 } \alpha ^ { - 2 }$as stated. We also know that

$$
\sum_ {r \notin K} | \hat {A} (r) | ^ {4} <   \lambda^ {2} N ^ {2} \sum_ {r \notin K} | \hat {A} (r) | ^ {2} \leqslant \alpha \lambda^ {2} N ^ {4}.
$$

Therefore, if we define$h ( x )$to be$\begin{array} { r } { N ^ { - 1 } \sum _ { r \in K } | \hat { A } ( r ) | ^ { 4 } \omega ^ { r x } } \end{array}$, we find that $| g ( x ) - h ( x ) | \leqslant \alpha \lambda ^ { 2 } N ^ { 3 }$for every x.

Now choose d such that$| r d | \leqslant \alpha N / 3 2 \pi$for every$r \in K$. Then, for every$x ,$

$$
\begin{array}{r l} & {| h (x + d) - h (x) | = N ^ {- 1} \Big | \sum_ {r \in K} | \hat {A} (r) | ^ {4} (\omega^ {r (x + d)} - \omega^ {r x}) \Big |} \\ & {\qquad \leqslant N ^ {- 1} \sum_ {r \in K} | \hat {A} (r) | ^ {4} | \omega^ {r d} - 1 |} \\ & {\qquad \leqslant 2 \pi (\alpha / 3 2 \pi) \alpha^ {3} N ^ {3} = \alpha \lambda^ {2} N ^ {3},} \end{array}
$$

where for the last inequality we used the fact that$\begin{array} { r l } { \sum _ { r } | \hat { A } ( r ) | ^ { 4 } } & { { } \leqslant } \end{array}$ $\begin{array} { r } { ( \alpha N ) ^ { 2 } \sum _ { r } | \hat { A } ( r ) | ^ { 2 } = \alpha ^ { 3 } N ^ { 4 } } \end{array}$. It follows that, under the same condition on$d ,$ we have

$$
\left| g (x + d) - g (x) \right| \leqslant 3 \alpha \lambda^ {2} N ^ {3}
$$

for every x.

Since$g ( 0 ) \geqslant N ^ { - 1 } | \hat { A } ( 0 ) | ^ { 4 } = \alpha ^ { 4 } N ^ { 3 } = 4 \alpha \lambda ^ { 2 } N ^ { 3 }$, it follows that$g ( d ) > 0$ for every d$\epsilon \ B = B ( K , \alpha / 3 2 \pi )$, so$B \subset 2 A - 2 A$. Now$\phi$induces a homomorphism$\psi _ { 0 }$(of order 2) on$2 A - 2 A$, which therefore restricts to a homomorphism$\psi$on B. If$x , y \in A$with$x - y = d \in B$, then$\psi ( d ) =$ $\phi ( x ) + \phi ( x ) - \phi ( x ) - \phi ( y ) = \phi ( x ) - \phi ( y )$✷

Remark. Notice that the same result holds, with an almost identical proof, if$\phi$maps A into a general Abelian group G rather than$\mathbb { Z } _ { N }$

Given that$\phi$was already a homomorphism of order 8 in the statement of Lemma 7.8, the reader may be excused for wondering what has been gained in the conclusion. The answer is that$B = B ( K , \alpha / 3 2 \pi )$has so much structure, in particular containing many long arithmetic progressions, that much more can be said about homomorphisms defined on B than about homomorphisms on arbitrary sets. The next corollary illustrates this.

Corollary 7.9. Let A and K be as in Lemma 7.8 and let m be a positive integer. For every$d \in B ( K , \alpha / 3 2 \pi m )$there exists c such that$\phi ( x ) - \phi ( y ) =$ $c ( x - y )$whenever$x - y$belongs to the set$\{ j d : - m \leqslant j \leqslant m \}$

Proof. This follows from Lemma 7.8 together with the observations that $\{ j d : - m \leqslant j \leqslant m \} \subset B ( K , \alpha / 3 2 \pi )$, that the restriction of any homomorphism to$\{ j d : - m \leqslant j \leqslant m \}$is linear and that$\psi ( 0 ) = 0$✷

We now give a useful definition which arises naturally out of the statement of Lemma 7.8. Let$A , B \subset \mathbb { Z } _ { N }$and let$\phi : A  \mathbb { Z } _ { N }$. We shall say that $\phi$is a B-homomorphism if there is a homomorphism$\psi : B \to \mathbb { Z } _ { N }$such that, whenever$x , y \in A$and$x - y = z$with$z \in B$, we have$\phi ( x ) - \phi ( y ) = \psi ( z )$ In other words,$\phi$induces a homomorphism on$( A - A ) \cap B$

The last two results of this section are once again simply a putting together of earlier results.

Corollary 7.10.. Let N be suficiently large, let$B _ { 0 } \subset \mathbb { Z } _ { N }$have cardinality αN and let$\phi : B _ { 0 } \to \mathbb { Z } _ { N }$have$\gamma ( \alpha N ) ^ { 3 }$additive quadruples. Then there exist a mod-N arithmetic progression$P$of length at least$N ^ { 2 ^ { - 3 7 7 0 } \gamma ^ { 2 3 2 8 } \alpha ^ { 2 } }$, a subset$H \subset P$of cardinality at least$2 ^ { - 1 8 \bar { 4 } 9 } \gamma ^ { 1 1 6 4 } \alpha | P |$and constants $\lambda , \mu \in \mathbb { Z } _ { N }$such that$\phi ( s ) = \lambda s + \mu$for every$s \in H$

Proof. Corollary 7.6 says that there is a subset$B \subset B _ { 0 }$of cardinality at least$\beta N$, where$\beta = 2 ^ { - 1 8 8 2 } \gamma ^ { 1 1 6 4 } \alpha$, such that the restriction of$\phi$to $B$is a Freiman homomorphism of order 8. To this pair$( B , \phi )$we apply Corollary 7.9. Let K be the set of size at most$1 6 \beta ^ { - 2 }$coming from Corollary 7.8. By Lemma 7.7, the Bohr neighbourhood$B ( K , \beta / 3 2 \pi m )$ has a non-zero element if$\beta / 3 2 \pi m > ( N / 2 ) ^ { - \beta ^ { 2 } / 1 6 }$Assume that m is chosen so that this inequality is satisfied and let d be a non-zero element of$B ( K , \beta / 3 2 \pi m )$Let$P _ { 0 }$be the mod-N arithmetic progression $( d , 2 d , \ldots , m d )$. By an easy averaging argument, there exists$k \in \mathbb { Z } _ { N }$such that$| ( P _ { 0 } + k ) \cap B | \geqslant \beta m$Choose such a k and let$P = P _ { 0 } + k$and $H = P \cap B$. Since$x - y \in \{ j d : - m \leqslant j \leqslant m \}$whenever$x , y \in P .$Corollary 7.9 gives us a constant$c \in \mathbb { Z } _ { N }$such that$\phi ( x ) - \phi ( y ) = c ( x - y )$for every$x , y \in H$. It remains only to check that if N is suficiently large then there exists an integer m$\geqslant N ^ { \tilde { 2 } ^ { - 3 7 7 0 } \gamma ^ { 2 3 2 8 } \alpha ^ { 2 } }$such that$\beta / 3 2 m > ( \stackrel { \cdot } { N } / 2 ) ^ { - \beta ^ { 2 } / 1 6 }$ This is a calculation left to the reader, but we state here for later reference that N can be taken to be$( 2 \gamma ^ { - 1 } \alpha ^ { - 1 } ) ^ { 2 ^ { 4 0 0 0 } \gamma ^ { - 2 3 2 8 } \alpha ^ { - 2 } }$✷

The final result will be used when$q = 1$in the proofs of Lemmas 13.7 and 13.9 and for general$q$in the proof of Lemma 16.3. Unlike our previous results, it applies to subsets of arithmetic progressions rather than subsets of$\mathbb { Z } _ { N }$

Corollary 7.11. Let R be an arithmetic progression in$\mathbb { Z } ,$for$1 \leqslant i \leqslant q$let $A _ { i } \subset R$be a set of cardinality at least$\alpha | R |$and for each i let$\phi _ { i } : A _ { i } \to \mathbb { Z } _ { N }$ be a homomorphism oforder 8. As long as$m \leqslant | R | ^ { 2 ^ { - 1 4 } \alpha ^ { 2 } q ^ { - 1 } }$it is possible to partition R into arithmetic progressions$S _ { 1 } , \ldots , S _ { M }$, all of size m or$m + 1$ and all with the same common diference, such that the restriction of any $\phi _ { i }$to any$A _ { i } \cap S _ { j }$is linear.

Proof. Let$R = \{ a , a { + } h , \ldots , a { + } ( l { - } 1 ) h \}$. We can embed R 8-isomorphically into$\mathbb { Z } _ { p }$for a prime$p < 1 6 l$using the map$\iota : a + j h \mapsto j$. Let$A _ { i } ^ { \prime } = \iota A _ { i }$and let$\phi _ { i } ^ { \prime } = \phi _ { i } \iota ^ { - 1 }$. (In other words, let us regard each$A _ { i }$as a subset of$\mathbb { Z } _ { p \cdot } )$ We know that$| A _ { i } ^ { \prime } | \geqslant \alpha p / 1 6$for every i. We shall now apply Lemma 7.8, with α replaced by$\alpha / 1 6$, to$A _ { i } ^ { \prime } \subset \mathbb { Z } _ { p }$and$\phi _ { i } ^ { \prime }$which maps$A _ { i } ^ { \prime }$to$\mathbb { Z } _ { N }$(see the remark following Lemma 7.8).

Let$L = \{ 1 \} \cup \{ r \in \mathbb { Z } _ { p } : | \hat { A } _ { i } ^ { \prime } ( r ) | \geqslant \alpha ^ { 3 / 2 } p / 2 5 6$for some i}. By Lemma 7.8 we know that$| L | \leqslant 2 ^ { 1 2 } \alpha ^ { \dot { - } 2 } q { + } \dot { 1 }$and that for each i there is a homomorphism $\psi _ { i } : B ( L , \alpha / 5 1 2 \pi ) \to \mathbb { Z } _ { N }$such that$\phi _ { i } ^ { \prime } ( x ) - \phi _ { i } ^ { \prime } ( y ) = \psi ( x - y )$whenever $x - y \in B ( L , \alpha / 5 1 2 \pi )$. By Lemma 7.7,$B ( L , \alpha / 5 1 2 \pi m ^ { 2 } )$contains a non-zero element d. Because$1 \in L$, we know that$\vert d \vert \leqslant \alpha p / 5 1 2 \pi m ^ { 2 }$, which implies that$\mathbb { Z } _ { p }$can be partitioned into (genuine) arithmetic progressions each of which has common diference$d$and length at least$m ^ { 2 }$. We can then partition these progressions into further subprogressions of length m or $m + 1$. As in the proof of Corollary 7.9, for each i there exists$c _ { i }$such that if $S$is one of these subprogressions and$x , y \in S$, then$\phi _ { i } ^ { \prime } ( x ) - \phi _ { i } ^ { \prime } ( y ) = c _ { i } ( x - y )$ The corollary follows on using$\iota ^ { - 1 }$to transfer us back to$R , A _ { i }$and φ<sub>i</sub>. ✷

## 8 Progressions of Length Four

We have now shown that if$A \cap ( A + k ) \sim ( \phi ( k ) )$is large for many values of k then$\phi$resembles a linear function. If φ is linear, then the rest of the argument is simple. Indeed, suppose that$\phi ( k ) = 2 c k$for every$k ,$for some constant$c \in \mathbb { Z } _ { N }$. Then inequality (6.1) becomes

$$
\sum_ {k} \sum_ {s, u} A (s) A (s - k) A (s - u) A (s - k - u) \omega^ {- 2 c k u} \geqslant \alpha^ {3} N ^ {3}.
$$

Using the identity

$$
2 k u = s ^ {2} - (s - k) ^ {2} - (s - u) ^ {2} + (s - k - u) ^ {2},
$$

we can deduce that

$$
\sum_ {r} \sum_ {a, b, c, d} A (a) A (b) A (c) A (d) \omega^ {- r (a - b - c + d)} \omega^ {- c (a ^ {2} - b ^ {2} - c ^ {2} + d ^ {2})} \geqslant \alpha^ {3} N ^ {4},
$$

or in other words that

$$
\sum_ {r} \Big | \sum_ {s} A (s) \omega^ {- c s ^ {2}} \omega^ {- r s} \Big | ^ {4} \geqslant \alpha^ {3} N ^ {4}.
$$

By the implication of (iii) from (iv) in Lemma 2.2, this tells us that for some value of r we have the lower bound

$$
\left| \sum_ {s} A (s) \omega^ {- c s ^ {2}} \omega^ {- r s} \right| \geqslant \alpha^ {3 / 2} N,
$$

or in other words that A exhibits quadratic bias of a particularly strong kind. The aim of this section is to give a similar argument that shows the existence of quadratic bias under the weaker assumption that$\phi$has a reasonably large linear part, such as is guaranteed by Corollary 7.10.

Let us remind ourselves why this is needed. We are examining sets $A \subset \mathbb { Z } _ { N }$that fail to be quadratically α-uniform. Let A be such a set and let$f$be the balanced function of$A$. Then there is a subset$B \subset \mathbb { Z } _ { N }$of cardinality at least αN, and a function$\phi : B \to \mathbb { Z } _ { N }$such that$| \Delta ( f ; k ) ^ { \wedge } ( \phi ( k ) ) | \geqslant$ $\alpha N$for every$k \in B$. By Proposition 6.1 we know that B contains at least $\alpha ^ { 1 2 } N ^ { 3 }$additive quadruples for the function$\phi .$. Corollary 7.10 then implies that$\phi$can be restricted to a large arithmetic progression P where it often agrees with a linear function$s \mapsto a s + b$. This provides the motivation for the next proposition.

Proposition 8.1. Let$A \subset \mathbb { Z } _ { N }$have balanced function$f .$. Let$P$be an arithmetic progression (in$\mathbb { Z } _ { N } )$of cardinality T. Suppose that there exist λ and$\mu$such that$\begin{array} { r } { \sum _ { k \in P } | \Delta ( f ; k ) ^ { \wedge } ( \lambda k + \mu ) | ^ { 2 } \geqslant \beta N ^ { 2 } T } \end{array}$. Then there exist quadratic polynomials$\psi _ { 0 } , \psi _ { 1 } , \dots , \psi _ { N - 1 }$such that

$$
\sum_ {s} \left| \sum_ {z \in P + s} f (z) \omega^ {- \psi_ {s} (z)} \right| \geqslant \beta N T / \sqrt {2}.
$$

Proof. Expanding the assumption we are given, we obtain the inequality

$$
\sum_ {k \in P} \sum_ {s, t} f (s) f (s - k) f (t) f (t - k) \omega^ {- (\lambda k + \mu) (s - t)} \geqslant \beta N ^ {2} T.
$$

Substituting$u = s - t .$, we deduce that

$$
\sum_ {k \in P} \sum_ {s, u} f (s) f (s - k) f (s - u) f (s - k - u) \omega^ {- (\lambda k + \mu) u} \geqslant \beta N ^ {2} T.
$$

Let$P = \{ x + d , x + 2 d , \ldots , x + T d \}$. Then we can rewrite the above inequality as

$$
\sum_ {i = 1} ^ {T} \sum_ {s, u} f (s) f (s - x - i d) f (s - u) f (s - x - i d - u) \omega^ {- (\lambda x + \lambda i d + \mu) u} \geqslant \beta N ^ {2} T.\tag{\((*)\}
$$

Since there are exactly T ways of writing$u = y + j d$with$y \in \mathbb { Z } _ { N }$and $1 \leqslant j \leqslant T$, we can rewrite the left-hand side above as

$$
\begin{array}{c} \frac {1}{T} \sum_ {s} \sum_ {i = 1} ^ {T} \sum_ {y} \sum_ {j = 1} ^ {T} f (s) f (s - x - i d) f (s - y - j d) \\ \cdot f (s - x - i d - y - j d) \omega^ {- (\lambda x + \lambda i d + \mu) (y + j d)}. \end{array}
$$

Let us define$\gamma ( s , y )$by the equation

$$
\begin{array}{c} \left| \sum_ {i = 1} ^ {T} \sum_ {j = 1} ^ {T} f (s - x - i d) f (s - y - j d) f (s - x - i d - y - j d) \omega^ {- (\lambda x + \mu + \lambda i d) (y + j d)} \right| \\ = \gamma (s, y) T ^ {2}. \end{array}
$$

Since$| f ( s ) | \leqslant 1 , ( * )$tells us that the average value of$\gamma ( s , y )$is at least$\beta .$ In general, suppose we have real functions$f _ { 1 } , f _ { 2 }$and$f _ { 3 }$such that

$$
\left| \sum_ {i = 1} ^ {T} \sum_ {j = 1} ^ {T} f _ {1} (i) f _ {2} (j) f _ {3} (i + j) \omega^ {- (a i + b j - 2 c i j)} \right| \geqslant c T ^ {2}.
$$

Since$2 c i j = c ( ( i + j ) ^ { 2 } - i ^ { 2 } - j ^ { 2 } )$, we can rewrite this as

$$
\left| \sum_ {i = 1} ^ {T} \sum_ {j = 1} ^ {T} f _ {1} (i) \omega^ {- (a i + c i ^ {2})} f _ {2} (i) \omega^ {- (b j + c j ^ {2})} f _ {3} (i + j) \omega^ {c (i + j) ^ {2}} \right| \geqslant c T ^ {2}
$$

and then replace the left-hand side by

$$
\frac {1}{N} \left| \sum_ {r} \sum_ {i = 1} ^ {T} \sum_ {j = 1} ^ {T} \sum_ {k = 1} ^ {2 T} f _ {1} (i) \omega^ {- (a i + c i ^ {2})} f _ {2} (j) \omega^ {- (b j + c j ^ {2})} f _ {3} (k) \omega^ {c k ^ {2}} \omega^ {- r (i + j - k)} \right|.
$$

If we now set$g _ { 1 } ( r ) = \sum _ { i = 1 } ^ { T } f _ { 1 } ( i ) \omega ^ { - ( a i + c i ^ { 2 } ) } \omega ^ { - r i } , g _ { 2 } ( r ) = \sum _ { j = 1 } ^ { T } f _ { 2 } ( j ) \omega ^ { - ( b j + c j ^ { 2 } ) } \omega ^ { - r j }$

and$\begin{array} { r } { g _ { 3 } ( r ) = \sum _ { k = 1 } ^ { 2 T } f _ { 3 } ( k ) \omega ^ { - c k ^ { 2 } } \omega ^ { - r k } } \end{array}$, then we have

$$
\left| \sum_ {r} g _ {1} (r) g _ {2} (r) g _ {3} (r) \right| \geqslant c T ^ {2} N,
$$

which implies, by the Cauchy-Schwarz inequality, that$\left\| g _ { 1 } \right\| _ { \infty } \left\| g _ { 2 } \right\| _ { 2 } \left\| g _ { 3 } \right\| _ { 2 } \geqslant$ $c T ^ { 2 } N$. Since$\| g _ { 2 } \| _ { 2 } ^ { 2 } \leqslant N T$and$\lVert g _ { 3 } \rVert _ { 2 } ^ { 2 } \leqslant 2 N T$(by identity (3) of$\ S 2 )$, this tells us that$| g _ { 1 } ( r ) | \geqslant c T / \sqrt { 2 }$for some r. In particular, there exists a quadratic polynomial$\psi$such that$\begin{array} { r } { \left| \sum _ { i = 1 } ^ { T } f _ { 1 } ( i ) \omega ^ { - \bar { \psi } ( i ) } \right| \geqslant c T / \sqrt { 2 } } \end{array}$

<sub></sub>Let us apply this general fact to the functions$f _ { 1 } ( i ) = f ( x - s - i d )$ $f _ { 2 } ( j ) = f ( s - y - j d )$and$f _ { 3 } ( k ) = f ( s - x - y - k d )$. It gives us a quadratic polynomial$\psi _ { s , y }$such that

$$
\left| \sum_ {i = 1} ^ {T} f (s - x - i d) \omega^ {- \psi_ {s, y} (i)} \right| \geqslant \gamma (s, y) T / \sqrt {2}.
$$

Let$\gamma ( s )$be the average of$\gamma ( s , y )$, and choose$\psi _ { s }$to be one of the$\psi _ { s , y }$in such a way that

$$
\left| \sum_ {i = 1} ^ {T} f (s - x - i d) \omega^ {- \psi_ {s} (i)} \right| \geqslant \gamma (s) T / \sqrt {2}.
$$

 If we now sum over s, we have the required statement (after a small change to the definition of the$\psi _ { s } )$✷

Theorem 8.2. There is an absolute constant C with the following property. Let A be a subset of${ \mathrm { ~ } } \operatorname { \mathbb { Z } } _ { N }$with cardinality δN.$I f N \geqslant \exp \exp \bigl ( ( 1 / \delta ) ^ { C } \bigr )$, then $A$contains an arithmetic progression of length four.

Proof. Our assumption certainly implies that$N \geqslant 3 2 k ^ { 2 } \delta ^ { - k }$. Suppose now that the result is false. Then Corollary 3.6 implies that A is not$\alpha \mathrm { - }$ quadratically uniform, where$\alpha = ( \delta / 2 ) ^ { 6 4 }$. By Lemma 3.1 (in particular the implication of (i) from$\big ( \mathrm { v } \big ) \big )$there is a set$B \subset \mathbb { Z } _ { N }$of cardinality at least α${ } ; N / 2$together with a function$\phi : B \to \mathbb { Z } _ { N }$, such that$| \Delta ( f ; k ) ^ { \wedge } ( \phi ( k ) ) | \geqslant$ $\alpha N / 2$for every$k \in B$. In particular,

$$
\sum_ {k \in B} \left| \Delta (f; k) ^ {\wedge} (\phi (k)) \right| ^ {2} \geqslant (\alpha / 2) ^ {3} N ^ {3}.
$$

Hence, by Proposition 6.1, B contains at least$( \alpha / 2 ) ^ { 1 2 } N ^ { 3 }$φ-additive quadruples.

By Corollary 7.10, we can find a mod-N arithmetic progression$P$of size at least$N ^ { 2 ^ { - 3 2 0 0 0 } \alpha ^ { 3 0 0 0 0 } }$and constants$\lambda , \mu \in \mathbb { Z } _ { N }$such that

$$
\sum_ {k \in P} \left| \Delta (f; k) ^ {\wedge} (\lambda k + \mu) \right| ^ {2} \geqslant 2 ^ {- 1 6 0 0 0} \alpha^ {1 5 0 0 0} | P | N ^ {2}.
$$

Therefore, by Proposition 8.1, we have quadratic polynomials$\psi _ { 0 } , \psi _ { 1 } , . . . , \psi _ { N }$−1 such that 1

$$
\sum_ {s} \Big | \sum_ {z \in P + s} f (z) \omega^ {- \psi_ {s} (z)} \Big | \geqslant \beta N | P | / \sqrt {2}
$$

where$\beta = 2 ^ { - 1 6 0 0 0 } \alpha ^ { 1 5 0 0 0 }$

By a simple averaging argument we can find a partition of$\mathbb { Z } _ { N }$into mod-$N$arithmetic progressions$P _ { 1 } , \dots , P _ { M }$of length$| P | \ \mathrm { o r } \ | P | + 1$and also a sequence$\psi _ { 1 } , \dots , \psi _ { M }$(after renaming) of quadratic polynomials such that

$$
\sum_ {j = 1} ^ {M} \left| \sum_ {z \in P _ {j}} f (z) \omega^ {- \psi_ {j} (z)} \right| \geqslant \beta N / 2.
$$

(Each$P _ { j }$is either a translate of$P$or a translate of P extended by one point. Because of the small extensions we have changed$\sqrt { 2 }$to 2.) By Lemma 5.13 we can refine this partition and produce a partition into genuine arithmetic progressions$Q _ { 1 } , \ldots , Q _ { L }$, which automatically satisfy an inequality of the form

$$
\sum_ {j = 1} ^ {M} \left| \sum_ {z \in Q _ {j}} f (z) \omega^ {- \psi_ {j} (z)} \right| \geqslant \beta N / 2.
$$

Once again, we have renamed the functions$\psi _ { j }$. Lemma 5.13 allows us to take$L \leqslant N ^ { 1 - 2 ^ { - 3 2 0 0 2 } \alpha ^ { 3 0 0 0 0 } }$. Next, Lemma 5.14 gives us a further refinement of$Q _ { 1 } , \ldots , Q _ { L }$into arithmetic progressions$R _ { 1 } , \ldots , R _ { H }$such that

$$
\sum_ {i = 1} ^ {H} \left| \sum_ {s \in R _ {i}} f (s) \right| \geqslant \beta N / 4
$$

and H is at most$N ^ { 1 - 2 ^ { - 3 2 0 1 0 } \alpha ^ { 3 0 0 0 0 } }$Finally, Lemma 5.15 gives us an arithmetic progression R of cardinality at least$\beta N ^ { 2 ^ { - 3 2 0 1 } 0 } \alpha ^ { 3 0 0 0 0 }$such that $\textstyle \sum _ { s \in R } f ( s ) \geq \beta | R | / 1 6$. This implies that the cardinality of$A \cap R$is at least$| R | ( \delta + 2 ^ { - 1 6 0 0 4 } \alpha ^ { 1 5 0 0 0 } )$. Recalling that$\alpha = ( \delta / 2 ) ^ { 6 4 }$, we find that the density of A has gone up from δ in$\mathbb { Z } _ { N }$to at least$\delta ( 1 + ( \delta / 2 ) ^ { 9 8 0 0 0 0 } )$inside the arithmetic progression R.

We now iterate this argument. The iteration can be performed at most $( \delta / 2 ) ^ { - 1 0 0 0 0 0 0 }$times, and at each step the value of N is raised to a power which exceeds$( \delta / 2 ) ^ { 2 0 0 0 0 0 0 }$. It is not hard to check that N will always remain suficiently large for the argument to work, as long as the initial value of N is at least exp$\exp ( \delta ^ { - C } )$, where C can be taken to be 2000000. ✷

An alternative formulation of the condition on N and δ is that δ should be at least$( \log \log N ) ^ { - c }$for some absolute constant$c > 0$. We have the following immediate corollary.

Corollary 8.3. There is an absolute constant$c > 0$with the following property. If the set$\{ 1 , 2 , \ldots , N \}$is coloured with at most$( \log \log N ) ^ { c }$ colours, then there is a monochromatic arithmetic progression of length four.✷

## 9 Obtaining Approximate Homomorphisms

The results of this section and the next can be combined to give an alternative proof of Corollary 7.9. The approach is longer, and the bound worse, but it does not make use of Pl¨unnecke’s inequality, so the comparison is less unfavourable than it seems. Our reason for giving it is that later in the paper we shall come across functions that are almost Freiman homomorphisms, but not quite, and we have not found a quick way of turning them into genuine homomorphisms without losing important information about their Fourier coeficients. Instead, therefore, we have been forced to examine these approximate homomorphisms and produce a version of Corollary 7.9 for them directly. It is quite possible that there is an argument for obtaining genuine homomorphisms in the later contexts. This would result in a significant simplification of the paper.

The later applications all need results that are more complicated than those proved in this section (see §12 and §15). Therefore, this section is another one which is not strictly necessary. However, the reader may find it useful to see the method of proof at work in a simpler case. Recall that we showed in Corollary 7.6 that if$B \subset \mathbb { Z } _ { N }$and$\phi : B \to \mathbb { Z } _ { N }$is a somewhat additive function, then$\phi$has a restriction to a large subset of B which is an isomorphism of order eight. In this section we shall give an alternative approach which yields what we shall call an approximate isomorphism. Because the isomorphism is approximate rather than exact, it is harder to apply Bogolyubov-type techniques to it, and that will be the task of the next section.

Let$B \subset \mathbb { Z } _ { N }$. We shall call a function$\phi : B \to \mathbb { Z } _ { N }$a γ-homomorphism of order k if, of the sequences$( x _ { 1 } , \dots , x _ { 2 k } ) \in B ^ { 2 k }$such that

$$
x _ {1} + \dots + x _ {k} = x _ {k + 1} + \dots + x _ {2 k},
$$

the proportion that also satisfy

$$
\phi (x _ {1}) + \dots + \phi (x _ {k}) = \phi (x _ {k + 1}) + \dots + \phi (x _ {2 k})
$$

is at least$\gamma , ~ \mathrm { H } ~ \gamma$is close to 1, then we shall say that$\phi$is an approximate homomorphism of order k.

Lemma 9.1. Let$a _ { 1 } , \ldots , a _ { n }$be non-negative real numbers. Then

$$
\sum_ {i = 1} ^ {n} a _ {i} ^ {4} \leqslant \left(\sum_ {i = 1} ^ {n} a _ {i} ^ {2}\right) ^ {6 / 7} \left(\sum_ {i = 1} ^ {n} a _ {i} ^ {1 6}\right) ^ {1 / 7}.
$$

Proof. The result follows from H¨older’s inequality if one writes$a _ { i } ^ { 4 } ~ =$ $a _ { i } ^ { 1 2 / 7 } a _ { i } ^ { 1 6 / 7 }$and takes$p = 7 / 6 , q = 7$✷

Lemma 9.2. Let$B \subset \mathbb { Z } _ { N }$and let$\phi : B \to \mathbb { Z } _ { N }$be γ-additive. Then there are at least$\gamma ^ { 7 } N ^ { 1 5 }$sequences$a _ { 1 } , \ldots , a _ { 1 6 }$such that

$$
a _ {1} + \dots + a _ {8} = a _ {9} + \dots + a _ {1 6}
$$

and

$$
\phi (a _ {1}) + \dots + \phi (a _ {8}) = \phi (a _ {9}) + \dots + \phi (a _ {1 6}).
$$

Proof. Given u$\in \mathbb { Z } _ { N }$, define$f _ { u } ( a )$to be$\omega ^ { u \phi ( a ) }$if$a \in B$, and zero otherwise. Then$\begin{array} { r } { \sum _ { a } | f _ { u } ( a ) | ^ { 2 } = | B | \leqslant N , \ : \mathrm { s o } \ : \sum _ { u , r } | \hat { f } _ { u } ( r ) | ^ { 2 } \leqslant N ^ { 3 } } \end{array}$

 Next, we look at fourth powers. We have

$$
\sum_ {u, r} | \hat {f} _ {u} (r) | ^ {4} = \sum_ {u, r} \Bigl | \sum_ {a} \omega^ {u \phi (a) - r a} \Bigr | ^ {4},
$$

which is exactly$N ^ { 2 }$times the number of additive quadruples$( a _ { 1 } , a _ { 2 } , a _ { 3 } , a _ { 4 } )$ and thus, by hypothesis, at least$\gamma N ^ { 5 }$

Finally, we look at sixteenth powers. A similar argument shows that $\textstyle \sum _ { u , r } | { \hat { f } } _ { u } ( r ) | ^ { 1 6 }$counts$N ^ { 2 }$times the number of sequences$( a _ { 1 } , \ldots , a _ { 1 6 } )$such that

$$
a _ {1} + \dots + a _ {8} = a _ {9} + \dots + a _ {1 6}
$$

and

$$
\phi (a _ {1}) + \dots + \phi (a _ {8}) = \phi (a _ {9}) + \dots + \phi (a _ {1 6}).
$$

Lemma 9.1 implies that

$$
\sum_ {u, r} | \hat {f} _ {u} (r) | ^ {1 6} \geqslant (\gamma N ^ {5}. N ^ {- 1 8 / 7}) ^ {7} = \gamma^ {7} N ^ {1 7}.
$$

Hence, the number of sequences with the desired properties is, as stated, at least$\gamma ^ { 7 } N ^ { 1 5 }$✷

Lemma 9.3. Let$\eta > 0$, let$B \subset \mathbb { Z } _ { N }$be a set of size$\beta N$and let$\phi : B \to \mathbb { Z } _ { N }$ be a function with at least$\alpha \beta ^ { 1 5 } N ^ { 1 5 }$sequences$a _ { 1 } , \ldots , a _ { 1 6 }$such that

$$
a _ {1} + \dots + a _ {8} = a _ {9} + \dots + a _ {1 6}\tag{1}
$$

and

$$
\phi (a _ {1}) + \dots + \phi (a _ {8}) = \phi (a _ {9}) + \dots + \phi (a _ {1 6}).\tag{2}
$$

Then, as long as N is suficiently large (in terms of$\alpha , \beta$and$\eta )$, there is a subset$B ^ { \prime } \subset B$with at least$( \alpha \eta / 4 ) ^ { 2 ^ { 1 9 } } \beta ^ { 1 5 } N ^ { 1 5 }$sequences$( a _ { 1 } , \dotsc , a _ { 1 6 } )$satisfying condition (1), such that the proportion of them that satisfy condition (2) as well is at least$1 - \eta$. In other words,$B ^ { \prime }$is reasonably large and the restriction of$\phi$to$B ^ { \prime }$is a$( 1 - \eta )$-homomorphism of order eight.

Proof. The basic idea is that if we let M be a suitable fraction of N and P be the interval$[ - M , M ] \subset \mathbb { Z } _ { N }$, and if we choose r and s randomly, then the set of all$x \in A$such that$r x + s \phi ( x )$belongs to P tends to have a larger proportion of sequences satisfying condition (2) than A itself. This is because the events that we choose$a _ { i }$for$i = 1 , 2 , \ldots , 1 6$are better correlated if$( a _ { 1 } , \dotsc , a _ { 1 6 } )$satisfies condition (2) than if it does not. Repeating the process, one can make the proportion as close as one likes to 1. Note that this is a natural approach to try, given the proof of Lemma 7.5.

The calculations are, however, enormously simplified if one uses Riesz products (that is, products of the form$2 ^ { - k } \textstyle \prod _ { i = 1 } ^ { k } ( 1 + \cos \theta _ { i } ) )$and a small modification of the above idea. Choose$r _ { 1 } , \ldots , r _ { k } , s _ { 1 } , \ldots , s _ { k }$uniformly and independently at random from$\mathbb { Z } _ { N }$. Once the choice is fixed, let a point $x \in B \ \mathrm { g o }$into$B ^ { \prime }$with probability

$$
2 ^ {- k} \prod_ {i = 1} ^ {k} \left(1 + \cos \frac {2 \pi}{N} \big (r _ {i} x + s _ {i} \phi (x) \big)\right),
$$

and let these probabilities be independent.

It must be stressed that this independence occurs only$a f t e r$we have conditioned on the choice of$r _ { 1 } , \ldots , r _ { k } , s _ { 1 } , \ldots , s _ { k }$. The whole point of the proof is that in total there is a dependence which favours sequences satisfying condition (2). To see that this is true, let$a _ { 1 } , \ldots , a _ { 1 6 }$be sixteen points in$\mathbb { Z } _ { N }$. The probability that they are all chosen is

$$
N ^ {- 2 k} \sum_ {r _ {1}, \dots , r _ {k}} \sum_ {s _ {1}, \dots , s _ {k}} 2 ^ {- 1 6 k} \prod_ {i = 1} ^ {k} \prod_ {j = 1} ^ {1 6} \left(1 + \cos \frac {2 \pi}{N} \left(r _ {i} a _ {j} + s _ {i} \phi (a _ {j})\right)\right)
$$

which equals

$$
N ^ {- 2 k} 2 ^ {- 1 6 k} \left(\sum_ {r, s} \prod_ {j = 1} ^ {1 6} \left(1 + \cos \frac {2 \pi}{N} \left(r a _ {j} + s \phi (a _ {j})\right)\right)\right) ^ {k},
$$

which we shall rewrite as

$$
N ^ {- 2 k} 2 ^ {- 1 6 k} \left(2 ^ {- 1 6} \sum_ {r, s} \prod_ {j = 1} ^ {1 6} \left(1 + 1 + \omega^ {r a _ {j} + s \phi (a _ {j})} + \omega^ {- (r a _ {j} + s \phi (a _ {j}))}\right)\right) ^ {k}.
$$

The product over j is a sum of$4 ^ { 1 6 }$terms, each of which is of the form

$$
\prod_ {j = 1} ^ {1 6} \omega^ {\epsilon_ {j} (r a _ {j} + s \phi (a _ {j}))} = \omega^ {r \sum_ {j} \epsilon_ {j} a _ {j} + s \sum_ {j} \epsilon_ {j} \phi (a _ {j})},
$$

where$\epsilon _ { 1 } , \ldots , \epsilon _ { 1 6 }$all belong to the set$\{ - 1 , 0 , 1 \}$. Such a term contributes zero to the sum over r and$s ,$unless$\begin{array} { r } { \sum _ { j = 1 } ^ { 1 6 } \epsilon _ { j } \dot { a } _ { j } = \sum _ { j = 1 } ^ { 1 6 } \epsilon _ { j } \phi ( a _ { j } ) = 0 } \end{array}$, in which case it contributes$N ^ { 2 }$

Let us now consider sequences$( a _ { 1 } , \dotsc , a _ { 1 6 } ) \in \mathbb { Z } _ { N } ^ { 1 6 }$satisfying condition (1). The set of such sequences is a fifteen-dimensional subspace of the vector space$\mathbb { Z } _ { N } ^ { 1 6 }$. Given$( \epsilon _ { 1 } , \epsilon \cdot \cdot , \epsilon _ { 1 6 } ) \in \{ - 1 , 0 , 1 \} ^ { 1 6 }$, the set of sequences $( a _ { 1 } , \dotsc , a _ { 1 6 } )$in this subspace satisfying the additional condition that$\epsilon _ { 1 } a _ { 1 } +$ $\dots + \epsilon _ { 1 6 } a _ { 1 6 } = 0$is a fourteen-dimensional subspace of$\mathbb { Z } _ { N } ^ { 1 6 }$and hence has cardinality$N ^ { 1 4 }$, except if$( \epsilon _ { 1 } , \dots , \epsilon _ { 1 6 } )$is a multiple of$( 1 , \ldots , 1 , - 1 , \ldots , - 1 )$

(eight 1s followed by eight −1s). Let us call a sequence$( a _ { 1 } , \dotsc , a _ { 1 6 } )$satisfying condition (1) degenerate if it also satisfies a genuinely distinct linear condition with coeficients in$\{ - 1 , 0 , 1 \}$, and otherwise non-degenerate. The number of degenerate sequences is clearly at most$3 ^ { 1 6 } N ^ { 1 4 }$. Let us call a non-degenerate sequence good if it satisfies condition (2) and bad otherwise. (It is part of the definition of non-degeneracy that both good and bad sequences satisfy condition (1).)

Our arguments above show that a bad sequence is chosen with probability$2 ^ { - 1 6 k }$, since the only terms that contribute are the$2 ^ { 1 6 }$terms with $\epsilon _ { j } = 0$for every j. A good sequence, on the other hand, is chosen with probability 2$- 1 6 k \left( 2 ^ { - 1 6 } ( 2 ^ { 1 6 } + 2 ) \right) ^ { k } = 2 ^ { - 1 6 k } ( 1 + 2 ^ { - 1 5 } ) ^ { k }$, because there are two  further terms making a contribution, namely those with$\epsilon _ { 1 } = \cdot \cdot \cdot = \epsilon _ { 8 } =$ $- \epsilon _ { 9 } = \cdot \cdot \cdot = - \epsilon _ { 1 6 } = \pm 1$. Let X and Y be the numbers of good and bad sequences chosen. Then the expected value of X is, from our hypothesis, at least$( 1 + 2 ^ { - 1 5 } ) ^ { k } 2 ^ { - 1 6 k } \alpha \beta ^ { 1 5 } \bar { N ^ { 1 5 } }$, and the expected value of Y is at most $2 ^ { - 1 6 k } \beta ^ { 1 5 } \dot { N } ^ { 1 5 }$. Using the fact that$2 ^ { 2 ^ { - 1 5 } } \leqslant 1 + 2 ^ { - 1 5 }$, we can deduce that if $2 ^ { 2 ^ { - 1 5 } \dot { k } } \geqslant 2 / \alpha \eta$, then

$$
\eta \mathbb {E} X - \mathbb {E} Y \geqslant \eta (2 / \alpha \eta) 2 ^ {- 1 6 k} \alpha \beta^ {1 5} N ^ {1 5} - 2 ^ {- 1 6 k} \beta^ {1 5} N ^ {1 5} = 2 ^ {- 1 6 k} \beta^ {1 5} N ^ {1 5}
$$

Now$2 ^ { 2 ^ { - 1 5 } k } \geqslant ( 2 / \alpha \eta )$if and only if$2 ^ { - 1 6 k } \leqslant ( \alpha \eta / 2 ) ^ { 2 ^ { 1 9 } }$. Let k be an integer such that o19919

$$
2 (\alpha \eta / 4) ^ {2 ^ {1 9}} \leqslant 2 ^ {- 1 6 k} \leqslant (\alpha \eta / 2) ^ {2 ^ {1 9}}.
$$

If N is large enough that$( \alpha \eta / 4 ) ^ { 2 ^ { 1 9 } } \beta ^ { 1 5 } N \geqslant 3 ^ { 1 6 }$, then the values for the above expectations and the upper estimate for the number of degenerate configurations imply that there exists a set$B ^ { \prime }$such that$\eta X ~ \geqslant ~ Y$and $X \geqslant ( \alpha \eta / 4 ) ^ { 2 ^ { 1 9 } } \beta ^ { 1 5 } \bar { N } ^ { 1 5 }$, as was claimed.✷

Lemmas 9.2 and 9.3 combined show that a somewhat additive function can be restricted to an approximate homomorphism of order eight.

Corollary 9.4. Let$B \subset \mathbb { Z } _ { N }$have size βN, let$\phi : B \to \mathbb { Z } _ { N }$be$\gamma \beta ^ { 3 } .$ additive and let$\eta > 0$. There is a subset$B ^ { \prime } \subset B$containing at least $( \gamma ^ { 7 } \beta ^ { 6 } \eta / 4 ) ^ { 2 ^ { 1 9 } } \beta ^ { 1 5 } N ^ { \dot { 1 } 5 }$sequences$( a _ { 1 } , \dotsc , a _ { 1 6 } )$with$a _ { 1 } + \cdot \cdot \cdot + a _ { 8 } = a _ { 9 } + \cdot \cdot \cdot + a _ { 1 6 }$ such that the restriction of φ to$B ^ { \prime }$is a (1−η)-homomorphism of order eight. Proof. Lemma 9.2 allows us to take$\alpha { = } ( \gamma \beta ^ { 3 } ) ^ { 7 } \beta ^ { - 1 5 } { = } \gamma ^ { 7 } \beta ^ { 6 }$in Lemma 9.3. ✷

## 10 Properties of Approximate Homomorphisms

Let$A \subset \mathbb { Z } _ { N }$be a set of size αN and let$\phi : A \ :  \ : \mathbb { Z } _ { N }$be a$( 1 - \epsilon ) \cdot$ homomorphism. Since A contains at least$\alpha ^ { 4 } N ^ { 3 }$additive quadruples, it also contains at least$( 1 - \epsilon ) \alpha ^ { 4 } N ^ { 3 }$φ-additive quadruples. Corollary 7.6 allows us to pass to a large subset$A ^ { \prime }$of A such that the restriction of$\phi$ to$A ^ { \prime }$is a Freiman homomorphism of order 8. Lemma 7.8 then provides a large Bohr neighbourhood B such that the restriction of$\phi$to$A ^ { \prime }$is a B-homomorphism.

Later in the paper approximate homomorphisms will arise in a context where we wish to restrict them to exact B-homomorphisms, but are unable to use the above argument. This may seem surprising, as the argument is perfectly valid: the reason it is inadequate is that the Bohr neighbourhood$B$that it gives is defined in terms of the set$A ^ { \prime } { \mathrm { . } }$, so by using it we lose information about the large Fourier coeficients of A. This will matter later, because then we shall have a collection of sets$A _ { h }$and approximate homomorphisms$\phi _ { h }$indexed by a set$H \subset \mathbb { Z } _ { N } ^ { k }$. The large Fourier coeficients associated with each set$A _ { h }$will be related, and we shall exploit this. Therefore, in this section our aim is to obtain a theorem similar to Lemma 7.8, but the Bohr neighbourhood will be defined in terms of the Fourier coeficients of the original set A rather than those of the subset$A ^ { \prime }$

This seems to make the proof harder, although it is based on similar ideas, and in particular uses Bogolyubov’s method. Most of the proofs in this section are simple averaging arguments. However, there are so many of them that when put together they are not particularly simple. It is likely that there is a shorter proof of the main result, but we have been unable to find one.

To complicate matters further, it is necessary to consider objects that are slightly more general than functions from$\mathbb { Z } _ { N }$to$\mathbb { Z } _ { N }$, to allow for multisets that occur naturally in later sections. By a multifunction from$\mathbb { Z } _ { N }$to $\mathbb { Z } _ { N }$, we shall mean a function from a set$X$to$\mathbb { Z } _ { N }$, together with a partition $\textstyle X = \bigcup _ { r \in \mathbb { Z } _ { N } } X _ { r }$. Equivalently, it is simply a pair of functions from X to $\mathbb { Z } _ { N }$, and indeed it will be useful to write$r ( x )$for the function that takes $x \in X$to the unique r such that$x \in X _ { r }$. We shall call a set X together with such a partition (or function) a domain, and if$\phi : X \to \mathbb { Z } _ { N }$, we shall call X the domain$o f \phi$

Given a domain$X = \left( X , r \right)$, we shall define$X - X$to be the set$X \times X$ together with the function$( x , y ) \mapsto r ( y ) - r ( x )$, or equivalently the partition $\textstyle X \times X = \bigcup _ { d } Y _ { d }$, where$Y _ { d }$is the set of pairs$( x , y )$such that$x \in X _ { r }$and $y \in X _ { r + d }$for some$r .$. More generally, by$k X - l X$we mean the set$X ^ { k + l }$ with the function

$$
(x _ {1}, \dots , x _ {k + l}) \mapsto r (x _ {1}) + \dots + r (x _ {k}) - r (x _ {k + 1}) - \dots - r (x _ {k + l}).
$$

A function$\phi : X \to \mathbb { Z } _ { N }$will be called a$( 1 - \eta )$-homomorphism of order k ${ \mathrm { i f } } ,$out of the 2k-tuples$( x _ { 1 } , \dots , x _ { 2 k } ) \in X ^ { 2 k }$such that

$$
r (x _ {1}) + \dots + r (x _ {k}) = r (x _ {k + 1}) + \dots + r (x _ {2 k}),
$$

the proportion such that

$$
\phi (x _ {1}) + \dots + \phi (x _ {k}) = \phi (x _ {k + 1}) + \dots + \phi (x _ {2 k})
$$

is at least$1 - \eta .$Note that this definition is not vacuous when$k = 1$

We shall define an additive quadruple to be a quadruple$( a , b , c , d ) \in X ^ { 4 }$ such that$r ( a ) - r ( b ) = r ( c ) - r ( d )$and we shall say that it is φ-additive if in addition$\phi ( a ) - \phi ( b ) = \phi ( c ) - \phi ( d )$. Then$\mathrm { ~ a ~ } ( 1 - \eta )$-homomorphism of order two is a function$\phi$such that the proportion of additive quadruples that are φ-additive is at least$1 - \eta$, just as when$X = \mathbb { Z } _ { N }$

We shall now investigate the extent to which these more general approximate homomorphisms resemble exact ones. The arguments are more complicated than one might expect, and the reason for the complication is the existence of examples of the following kind. Let$A$and B be subsets of $\mathbb { Z } _ { N }$, with$A = \{ a , a + r , \ldots , a + ( M { - } 1 ) r \}$and$B = \{ b , b + s , \ldots , b + ( M - 1 ) s \}$ where$M = \alpha N$for some small$\alpha > 0$. If there are no small linear relations between r and s$( \mathrm { i . e . }$, pairs$u , v$of small elements of$\mathbb { Z } _ { N }$such that ru + sv = 0) then the intersection of A and$B$will have cardinality roughly $\alpha ^ { 2 } N$. Moreover, almost all the additive quadruples in$A \cup B$will lie entirely in A or entirely in$B .$. (These facts are easy to check.) Hence, if we define a function$\phi$to be linear on A and also linear, but with a diferent gradient, on$B \backslash A$, then$\phi$will be a$( 1 - \eta )$-homomorphism for some small η (depending on α). In fact,$\phi$will even be a$( 1 - \eta )$-homomorphism of high order (for a larger$\eta ,$but still small). Most of the efort of this section is devoted to showing how to “pick out” A or B in an example such as the above, in order to obtain a well-defined and well-behaved diference function for the restriction of$\phi .$

Let$\textstyle X = \bigcup _ { r } X _ { r }$be a domain, let B be a set and let$L$be a non-negative real number. We shall say that X is$( B , L )$-invariant if, given any$r \in \mathbb { Z } _ { N }$ and any$d \in B$, the sizes of$X _ { r + d }$and$X _ { r }$difer by at most$L$. If L is small (compared, for example, with the average size of the$X _ { r } )$we shall say that X is almost B-invariant.

We shall now prove several lemmas under the same set of hypotheses. To save repetition later, we state the hypotheses once and for all here. Let$X = \left( X , r \right)$be a domain such that X has cardinality αMN and$X _ { r }$ has cardinality at most M for every r. Let$\sigma > 0$be a parameter to be chosen later and let$B \subset \mathbb { Z } _ { N }$be some set such that$B = - B$and X is $( B , \sigma M )$-invariant. Let$\phi : X \to \mathbb { Z } _ { N }$be a$( 1 - \eta )$-homomorphism.

For every$( x , y ) \in X ^ { 2 }$let us define$q ( x , y )$to be the number of pairs $( z , w ) \in X ^ { 2 }$such that$r ( w ) - r ( z ) = r ( y ) - r ( x )$. Let$b ( x , y )$be the number of pairs$( u , v ) \in X ^ { 2 }$such that$r ( u ) - r ( x ) = r ( v ) - r ( y ) \in B$. One can also write these as

$$
q (x, y) = \sum_ {d} | X _ {r (x) + d} | | X _ {r (y) + d} |
$$

and

$$
b (x, y) = \sum_ {d \in B} | X _ {r (x) + d} | | X _ {r (y) + d} |.
$$

We shall also let$e ( x , y )$be the number of pairs$( u , v )$such that$r ( u ) - r ( x ) =$ $r ( v ) - r ( y ) \in B$and$\phi ( u ) - \phi ( x ) \neq \phi ( v ) - \phi ( y )$

In words,$q ( x , y )$is the number of additive quadruples starting with $( x , y ) , b ( x , y )$is the number of such quadruples$( x , y , z , w )$such that $( r ( z ) , r ( w ) )$is$( r ( x ) , r ( y ) )$translated by some$d \in B$and$e ( x , y )$(the error) is the number of those special additive quadruples that fail to be φ-additive. Finally, let$\epsilon ( x , y )$be the proportionate error, i.e.,$e ( x , y ) / b ( x , y )$

Our first lemma collects together some simple facts about the function q. Lemma 10.1.$q ( x , y ) \leqslant \alpha M ^ { 2 } N$for every x, y,$\begin{array} { r } { \sum _ { y \in X } q ( x , y ) \leqslant \alpha ^ { 2 } M ^ { 3 } N ^ { 2 } } \end{array}$for every x and$\begin{array} { r } { \sum _ { x , y \in X } q ( x , y ) \geqslant \alpha ^ { 4 } M ^ { 4 } N ^ { 3 } } \end{array}$

Proof. For the first estimate we wish to count the number of pairs$( z , w )$ such that$( x , y , z , w )$is an additive quadruple. There are at most$| X | =$ $\alpha M N$ways of choosing z. Once z is chosen,$r ( w )$is determined so there are at most M choices for w. The second estimate follows immediately.

As for the third, notice that the left-hand side is equal to $\begin{array} { r } { \sum _ { r - s = t - u } | X _ { r } | | X _ { s } | | X _ { t } | | X _ { u } | } \end{array}$. By §2 identity (6) applied to the function $f ( s ) = | X _ { s } | .$, this is at least$N ^ { - 1 } | X | ^ { 4 }$, which is the estimate claimed.✷

One can think of the numbers$q ( x , y )$as defining a weighted graph, where the weight of the edge$( x , y )$measures the popularity of the diference $r ( y ) - r ( x )$in$X$. Roughly speaking, our aim will be to show that$\phi$is well behaved on “components” of this weighted graph – that is, highly connected subsets which are not highly connected to the rest of the graph. In the example discussed earlier of two “unrelated” arithmetic progressions A and$B ,$the components can be taken as A and$B \setminus A$, since$q ( x , y )$tends to be large if x and y both belong to A or both belong to$B ,$, and small otherwise. The pairs$( x , y )$that contribute a significant error$e ( x , y )$tend to be those for which x and y belong to diferent sets, and therefore for which the weight$q ( x , y )$is small. Our next lemma shows that this is true in general. That is, most of the error occurs, if at all, on edges with small weight.

Lemma 10.2. If$\sigma \leqslant \eta \alpha ^ { 2 }$, then$\begin{array} { r } { \sum _ { x , y \in X } \epsilon ( x , y ) q ( x , y ) \leqslant 1 5 \eta \sum _ { x , y \in X } q ( x , y ) } \end{array}$

Proof. Let$X ^ { \prime } \subset X$be the union of all$X _ { r }$of size at least$5 \eta \alpha ^ { 2 } M$. We begin by estimating$\textstyle \sum _ { x , y \in X ^ { \prime } } \epsilon ( x , y ) q ( x , y )$. Let$x \in X _ { r }$and$y \in X _ { s }$and let $X _ { r } \cup X _ { s } \subset X ^ { \prime }$. Then$\begin{array} { r } { b ( x , y ) = \sum _ { d \in B } | X _ { r + d } | | X _ { s + d } | } \end{array}$. Let$L = \eta \alpha ^ { 2 } M$. Since X is$( B , L )$-invariant, we can deduce from this expression for$b ( x , y )$that

$$
| B | \left(| X _ {r} | - L\right) \left(| X _ {s} | - L\right) \leqslant b (x, y) \leqslant | B | \left(| X _ {r} | + L\right) \left(| X _ {s} | + L\right).
$$

Furthermore, if u and v are such that$r ( u ) - r = r ( v ) - s \in B$, the$( B , L ) \cdot$ invariance also implies that

$$
\left| B \right| \left(\left| X _ {r} \right| - 2 L\right) \left(\left| X _ {s} \right| - 2 L\right) \leqslant b (u, v) \leqslant \left| B \right| \left(\left| X _ {r} \right| + 2 L\right) \left(\left| X _ {s} \right| + 2 L\right).
$$

Since both$\vert X _ { r } \vert$and$| X _ { s } |$are at least$5 \eta \alpha ^ { 2 } M = 5 L$, the above estimates imply that$b ( u , v ) / b ( x , y ) < 4$

Now let S be the set of all sextuples$( x , y , z , w , u , v ) \in X ^ { 6 }$with$x , y \in X ^ { \prime }$ satisfying the following conditions:

$$
r (w) - r (z) = r (y) - r (x)\tag{1}
$$

$$
r (u) - r (x) = r (v) - r (y) \in B\tag{2}
$$

$$
r (w) - r (z) = r (v) - r (u)\tag{3}
$$

$$
\phi (u) - \phi (x) \neq \phi (v) - \phi (y).\tag{4}
$$

Of course, (1) and (2) imply (3), and (2) and (3) imply (1).) Then

$$
\sum_ {(x, y, z, w, u, v) \in S} b (x, y) ^ {- 1} = \sum_ {x, y \in X ^ {\prime}} b (x, y) ^ {- 1} q (x, y) e (x, y) = \sum_ {x, y \in X ^ {\prime}} \epsilon (x, y) q (x, y).
$$

Condition (4) implies that either$\phi ( x ) - \phi ( y ) \neq \phi ( z ) - \phi ( w )$or$\phi ( u ) - \phi ( v ) \neq$ $\phi ( z ) - \phi ( w )$. Therefore, we can write$S = E \cup F$, where

$$
E = \left\{(x, y, z, w, u, v) \in S: \phi (x) - \phi (y) \neq \phi (z) - \phi (w) \right\}
$$

and

$$
F = \left\{(x, y, z, w, u, v) \in S: \phi (u) - \phi (v) \neq \phi (z) - \phi (w) \right\}.
$$

We now estimate the sum over S by splitting it into E and F.

For any fixed quadruple$( x , y , z , w )$satisfying condition (1), the number of pairs$( u , v )$such that$( x , y , z , w , u , v )$satisfies condition (2) is exactly $b ( x , y )$. It follows that${ \textstyle \sum } \{ b ( x , y ) ^ { - 1 } : ( x , y , z , w , u , v ) \in E \}$is at most the number of additive quadruples$( x , y , z , w )$with$x , y \in X ^ { \prime }$that fail to be φ-additive, which is by hypothesis at most$\eta$times the total number of additive quadruples. That is,

$$
\sum \left\{b (x, y) ^ {- 1}: (x, y, z, w, u, v) \in E \right\} \leqslant \eta \sum_ {x, y \in X} q (x, y).
$$

Since$B = - B$, for every quadruple$( z , w , u , v )$satisfying condition (3) the number of pairs$( x , y )$satisfying condition (2) is$b ( u , v )$. For each such pair, we have shown that$b ( u , v ) < 4 b ( x , y )$, so the sum of$b ( x , y ) ^ { - 1 }$over all of them is less than 4. Therefore,${ \textstyle \sum } \{ b ( x , y ) ^ { - 1 } : ( x , y , z , w , u , v ) \in { \cal F } \}$is less than 4 times the number of additive quadruples$( z , w , u , v )$that fail to be φ-additive. So this time we have

$$
\sum \left\{b (x, y) ^ {- 1}: (x, y, z, w, u, v) \in F \right\} <   4 \eta \sum_ {x, y \in X} q (x, y).
$$

Putting the two estimates together, we find that

$$
\sum_ {x, y \in X ^ {\prime}} \epsilon (x, y) q (x, y) \leqslant 5 \eta \sum_ {x, y \in X} q (x, y).
$$

We must also count the additive quadruples$( x , y , z , w )$such that either $x \notin X ^ { \prime }$or$y \notin X ^ { \prime }$, which means that either$| X _ { r ( x ) } | \mathrm { ~ o r ~ } | X _ { r ( y ) } |$is less than $5 \eta \alpha ^ { 2 } M$. There are easily seen to be at most$2 ( 5 \eta \dot { \alpha } ^ { 2 } M N ) ( \alpha \ddot { M } N ) ( \alpha M N ) M$ $= 1 0 \eta \alpha ^ { 4 } M ^ { 4 } N ^ { 4 }$of them. Since there are at least$\alpha ^ { 4 } M ^ { 4 } { \dot { N } } ^ { 3 }$additive quadruples, this number is at most$\begin{array} { r } { 1 0 \eta \sum _ { x , y \in X } q ( x , y ) } \end{array}$. This estimate, together with the earlier one, proves the lemma.✷

We are aiming to find a large subset of X where the error$\epsilon ( x , y )$is almost always small. The above lemma suggests that we can achieve this by choosing a subset of a “component” of the weighted graph given by$q .$ Roughly speaking, we do this by picking a random point$x \in X$and taking the set of all$y$in a neighbourhood of$x$(in an appropriate weighted sense). Such a set will be a union of sets$\left| X _ { r } \right|$. For technical reasons it will be very convenient to have all the$X _ { r }$that we choose of approximately the same size, and to have other properties of a similar kind. These properties will be obtained by somewhat messy averaging arguments.

To make these ideas more precise, let us define some more functions and prove another lemma. For every$x \in X$, let$R ( x ) = | X _ { r ( x ) } |$, let$Q ( x ) =$ $\textstyle \sum _ { y \in X } q ( x , y )$and let$\begin{array} { r } { E ( x ) = \sum _ { y \in X } \epsilon ( x , y ) q ( x , y ) } \end{array}$

Lemma 10.3. There exists$x \in X$such that$R ( x ) \geqslant \alpha ^ { 2 } M / 2 , Q ( x ) \geqslant$ $\alpha ^ { 3 } M ^ { 3 } N ^ { 2 } / 4$and$E ( x ) \leqslant 6 0 \eta Q ( x )$

Proof. Lemma 10.1 tells us that$\begin{array} { r } { \sum _ { x \in { \cal { X } } } Q ( x ) \geqslant \alpha ^ { 4 } M ^ { 4 } N ^ { 3 } } \end{array}$and that$Q ( x ) \leqslant$ $\alpha ^ { 2 } M ^ { 3 } N ^ { 2 }$for every x. Let$X ^ { \prime }$be the set of$x \in X$such that$R ( x ) \geqslant \alpha ^ { 2 } M / 2$ Clearly,$| X \setminus X ^ { \prime } | \leqslant \alpha ^ { 2 } M N / 2$, so

$$
\sum_ {x \in X ^ {\prime}} Q (x) \geqslant \alpha^ {4} M ^ {4} N ^ {3} - (\alpha^ {2} M N / 2) (\alpha^ {2} M ^ {3} N ^ {2}) = \alpha^ {4} M ^ {4} N ^ {3} / 2 \geqslant \frac {1}{2} \sum_ {x \in X} Q (x).
$$

Let us now choose$x \ \in \ X ^ { \prime }$uniformly at random. The expected value of$Q ( x )$is at least$| X | ^ { - 1 } \alpha ^ { 4 } M ^ { 4 } N ^ { 3 } / 2 = \alpha ^ { 3 } M ^ { 3 } N ^ { 2 } / 2$. By Lemma 10.2 the expectation of$E ( x )$is at most 15η times the expectation of$Q ( x )$over$X$ which is at most 30η times the expectation of$Q ( x )$over$X ^ { \prime }$. It follows that the expectation of$Q ( x ) - ( 1 / 6 0 \eta ) E ( x )$over$X ^ { \prime }$is at least$\alpha ^ { 3 } M ^ { 3 } N ^ { 2 } / 4$, so we can find$x \in X ^ { \prime }$such that$Q ( x ) \geq \alpha ^ { 3 } M ^ { 3 } N ^ { 2 } / 4$and$E ( x ) \leqslant 6 0 \eta Q ( x )$ This proves the lemma.✷

Let us now fix an x satisfying the conclusion of Lemma 10.3 and write $q ( y )$for$q ( x , y ) , \epsilon ( y )$for$\epsilon ( x , y )$and S for$Q ( x )$

Lemma 10.4.$H r ( z ) - r ( y ) \in B$, then$| q ( z ) - q ( y ) | \leqslant \sigma \alpha M ^ { 2 } N$

Proof. Let$r ( z ) - r ( y ) = d \in B$. Then

$$
q (y) = \sum_ {t - s = r (y) - r (x)} | X _ {s} | | X _ {t} |
$$

and

$$
q (z) = \sum_ {t - s = r (y) - r (x)} | X _ {s} | | X _ {t + d} |.
$$

From the$( B , \sigma M )$-invariance of$X$we deduce that

$$
\begin{array}{c} {| q (z) - q (y) | \leqslant \sum_ {t - s = r (y) - r (x)} | X _ {s} | \big | | X _ {t + d} | - | X _ {t} | \big |} \\ {\leqslant \sigma M \sum_ {s} | X _ {s} | = \sigma \alpha M ^ {2} N,} \end{array}
$$

as stated.

For the next lemma, we use the notation$W { + d }$to stand for all elements $x \in X$such that there exists$w \in W$with$r ( x ) = r ( w ) + d .$

Lemma 10.5. There exists a subset$W \subset X$with the following properties.

(i) W is a union of sets of the form$X _ { r }$

(ii) The function q varies by a factor of at most two on$W .$

(iii) For at least$( 1 - 5 \eta ^ { 1 / 2 } ) | W |$of the points$y \in W$we have$\epsilon ( y ) \leqslant 3 0 0 \eta ^ { 1 / 2 }$

(iv) W has cardinality at least$\rho ^ { 2 } \alpha ^ { 2 } M N / 1 6$

(v) The function R varies by a factor of at most two on$W$, and is always at least$\alpha ^ { 2 } M / 1 6$

(vi)$| W \cap ( W + d ) | \geqslant ( 1 - \eta ) | W |$for every$d \in B$

Proof. By Lemmas 10.1 and 10.3 we know that$q ( y ) \leqslant \alpha M ^ { 2 } N$for every y, that$\begin{array} { r } { S = \sum _ { u \in { \cal { X } } } q ( y ) \ \geqslant \ \alpha ^ { 3 } M ^ { 3 } N ^ { 2 } / 4 } \end{array}$and that$\begin{array} { r } { \sum _ { y \in X } \epsilon ( y ) q ( y ) \ \leqslant } \end{array}$ $6 0 \eta \sum _ { y \in X } q ( y ) = 6 0 \mathring { \eta } . \mathrm { ~ I ~ }$Let$X ^ { \prime }$be the set of all$y \in X$such that$R ( y ) \geqslant$ $\alpha ^ { 2 } M / 8$and let$\begin{array} { r } { S ^ { \prime } = \sum _ { y \in X ^ { \prime } } q ( y ) } \end{array}$. Then

$$
\sum_ {y \in X \backslash X ^ {\prime}} q (y) \leqslant (\alpha^ {2} M N / 8) (\alpha M ^ {2} N) = \alpha^ {3} M ^ {3} N ^ {2} / 8,
$$

from which it follows that$S ^ { \prime } \geqslant S / 2$

We now choose λ and$\mu$independently and uniformly from the interval $[ - \rho , 1 + \rho ]$and make the following definitions.

$$
\begin{array}{r l} & W _ {\lambda , \mu} = \left\{y: (\lambda - \rho) \alpha M ^ {2} N \leqslant q (y) \leqslant (\lambda + \rho) \alpha M ^ {2} N \right\} \\ & \qquad \cap \left\{y: (\mu - \rho) M \leqslant R (y) \leqslant (\mu + \rho) M \right\}; \\ & V _ {\lambda , \mu} = \left\{y: (\lambda - \rho) \alpha M ^ {2} N \leqslant q (y) \leqslant (\lambda - \rho + \sigma) \alpha M ^ {2} N \right\} \\ & \qquad \cap \left\{y: (\lambda + \rho - \sigma) \alpha M ^ {2} N \leqslant q (y) \leqslant (\lambda + \rho) \alpha M ^ {2} N \right\} \\ & \qquad \cap \left\{y: (\mu - \rho) M \leqslant R (y) \leqslant (\mu - \rho + \sigma) M \right\} \\ & \qquad \cap \left\{y: (\mu + \rho - \sigma) M \leqslant R (y) \leqslant (\mu + \rho) M \right\}. \end{array}
$$

We also set$\begin{array} { r } { S _ { \lambda , \mu } = \sum _ { y \in X ^ { \prime } \cap W _ { \lambda , \mu } } q ( y ) } \end{array}$and$\begin{array} { r } { E _ { \lambda , \mu } = \sum _ { y \in W _ { \lambda , \mu } } \epsilon ( y ) q ( y ) } \end{array}$. We  shall now use an averaging argument to find λ and$\mu$such that$S _ { \lambda , \mu }$is large, while$E _ { \lambda , \mu }$, and also the sizes of$W _ { \lambda , \mu }$and$V _ { \lambda , \mu } .$, are small.

To do this, we simply calculate or estimate the expectations of all the quantities concerned. Since any fixed$y \in X$has a probability of$\textstyle \left( { \frac { 2 \rho } { 1 + 2 \rho } } \right) ^ { 2 }$of belonging to$W _ { \lambda , \mu }$we find that the expectation of$S _ { \lambda , \mu }$is$\textstyle \left( { \frac { 2 \rho } { 1 + 2 \rho } } \right) ^ { 2 } S ^ { \prime }$, which we know is at least$\frac { 2 \rho ^ { 2 } } { ( 1 + 2 \rho ) ^ { 2 } } S .$. We also find that the expectation of$E _ { \lambda , \mu }$is at most$\Big ( \frac { 2 \rho } { 1 + 2 \rho } \Big ) ^ { 2 } 6 0 \eta \dot { S }$and the expected size of$\begin{array} { r } { W _ { \lambda , \mu } \mathrm { ~ i s ~ } \big ( \frac { 2 \rho } { 1 + 2 \rho } \big ) ^ { 2 } \alpha M N } \end{array}$. The probability of any given$y \in X$belonging to$V _ { \lambda , \mu }$is at most$\scriptstyle \left( { \frac { 4 \sigma } { 1 + 2 \rho } } \right)$, which implies that the expected size of$V _ { \lambda , \mu }$is at most$\scriptstyle { \left( { \frac { 4 \sigma } { 1 + 2 \rho } } \right) } \alpha M N$

By linearity of expectation, we may deduce that

$$
\mathbb {E} \left(S _ {\lambda , \mu} - \frac {E _ {\lambda , \mu}}{7 2 0 \eta} - \frac {S | W _ {\lambda , \mu} |}{1 2 \alpha M N} - \frac {\rho^ {2} S | V _ {\lambda , \mu} |}{1 2 \sigma (1 + 2 \rho) \alpha M N}\right) \geqslant \frac {\rho^ {2}}{(1 + 2 \rho) ^ {2}} S \geqslant \frac {\rho^ {2} S}{4}.
$$

Therefore there exist λ and$\mu$such that$S _ { \lambda , \mu } \geqslant \rho ^ { 2 } S / 4 , E _ { \lambda , \mu } \leqslant 7 2 0 \eta S _ { \lambda , \mu } ,$ $| W _ { \lambda , \mu } | \leqslant 1 2 \alpha M N S _ { \lambda , \mu } / S$and$| V _ { \lambda , \mu } | \leqslant$12σ$\rho ^ { - 2 } ( 1 + 2 \rho ) \alpha M N S _ { \lambda , \mu } / S .$. Our aim is now to prove that$W = W _ { \lambda , \mu }$has the desired properties.

Property (i) follows immediately from the definition of$W _ { \lambda , \mu }$. To prove (ii), notice that the average value of$q ( y )$over$W _ { \lambda , \mu }$is at$S _ { \lambda , \mu } / | W _ { \lambda , \mu } |$, which is at least$S / 1 2 \alpha M N \geqslant \alpha ^ { 2 } M ^ { 2 } N / 6 4$. It follows that$\lambda + \rho \geqslant \alpha / 4 8$, and hence that$\lambda - \rho \geqslant ( \lambda + \rho ) / 2 \ ( { \mathrm { a s } } \ \rho \leqslant \alpha / 1 9 2 )$

The upper estimate for$E _ { \lambda , \mu }$tells us that$\begin{array} { r l } { \sum _ { y \in W } \epsilon ( y ) q ( y ) } & { { } \leqslant } \end{array}$ $7 2 0 \eta \sum _ { y \in W } q ( y )$. Since the function q varies over W by a factor of at most two, we obtain (iii), since otherwise we would have$\sum _ { y \in W } \epsilon ( y ) q ( y ) >$ ${ \mathrm { 1 5 0 0 } } \eta { \mathrm { | } } W { \mathrm { | } } \operatorname* { m i n } _ { y \in W } q ( w )$, a contradiction.

Since$S _ { \lambda , \mu } ~ \geqslant ~ \rho ^ { 2 } S / 4 ~ \geqslant ~ \rho ^ { 2 } \alpha ^ { 3 } M ^ { 3 } N ^ { 2 } / 1 6$and$q ( y ) \leqslant \alpha M ^ { 2 } N$for every $y \in X$, the cardinality of W must be at least$\rho ^ { 2 } \alpha ^ { 2 } M N / 1 6$, which is property (iv).

Because$S _ { \lambda , \mu }$is non-zero, there exists$y \in W$such that$R ( y ) \geqslant \alpha ^ { 2 } M / 8$ from which it follows that$\mu + \rho \geqslant \alpha ^ { 2 } / 8$and therefore, as$\rho \leqslant \alpha ^ { 2 } / 3 2$, that $\mu - \rho \geqslant ( \mu + \rho ) / 2$and$\mu - \rho \geqslant \alpha ^ { 2 } / 1 6$. This gives us (v).

Let us now set$V = V _ { \lambda , \mu }$and choose$y \in W \setminus V . { \mathrm { ~ I f ~ } } d \in B$then by the $( B , \sigma M )$-invariance of X and our lower bound for$\mu ,$we have$| X _ { r ( y ) - d } | \geqslant$ $| X _ { r ( y ) } | - \sigma M \geqslant ( \mu - \rho ) M > 0$. Choosing any$z \in X _ { r ( y ) - d } .$, we then know that$\vert q ( z ) - q ( y ) \vert \leqslant \sigma \alpha M ^ { 2 } N .$, by Lemma 10.4, from which it follows that $( \lambda - \rho ) \alpha M ^ { 2 } N \leqslant q ( z ) \leqslant ( \lambda + \rho ) \alpha M ^ { 2 } N$. The$( B , \sigma M )$-invariance of X also gives us that$| R ( z ) - R ( y ) | \leqslant \sigma M$, and from this it follows that$( \mu - \rho ) M \leqslant$ $R ( z ) \leqslant ( \mu + \rho ) M$. We have therefore shown that if$y \in W \setminus V , d \in B$and $z \in X _ { r ( y ) - d } ,$, then$z \in W$. Moreover, such a z exists, so$y \in W + d$

All this shows that$W \setminus V \subset W \cap ( W + d )$. We have shown that the cardinality of W is at least$\rho ^ { 2 } \alpha ^ { 2 } M N / 1 6$, while the cardinality of V is at most $1 2 \sigma \rho ^ { - 2 } ( 1 + 2 \rho ) \alpha M N S _ { \lambda , \mu } / S$, which is certainly at most$2 4 \sigma \rho ^ { - 2 } \alpha M N$. Since $\sigma \leqslant \eta \rho ^ { 4 } \alpha / 3 8 4$, we find that$| V | \leqslant \eta | W |$and therefore obtain property (vi). ✷

Before we state the next lemma, it will be very useful to introduce the following shorthand notation. Given any finite set U and any proposition $P ( u )$involving the elements u of U, we shall say that$f o r \left( 1 - \epsilon \right)$-almost every $u \in U , P ( u )$if the set$\{ u \in U : P ( u ) \}$has cardinality at least$( 1 - \epsilon ) | U |$ We shall further abbreviate this by writing$( ( 1 - \epsilon ) \mathrm { a . e . } \ u \in U ) \ P ( u )$

Lemma 10.6. If$\sigma \leqslant \eta \rho \alpha ^ { 2 } / 1 6$then there exist a subset B of B of cardinality at least$( 1 - 1 0 \eta ^ { 1 / 5 } ) | B |$and a function$\psi : B ^ { \prime } \to \mathbb { Z } _ { N }$such that, for every$d \in B ^ { \prime }$2

$$
\left((1 - 1 0 \eta^ {1 / 5}) \text {a.e.} w \in W\right) \left((1 - 1 0 \eta^ {1 / 5}) \text {a.e.} z \in X _ {r (w) + d}\right) \quad \phi (z) - \phi (w) = \psi (d).
$$

Proof. Let us define$W ^ { \prime }$to be the set of all$w \in W \cap ( W - d )$such that $\epsilon ( w ) \leqslant 3 0 0 \eta ^ { 4 / 5 }$We know from Lemma$1 0 . 5 \ ( \mathrm { i i i } )$and (vi) (and the fact that $B = - B )$that$W ^ { \prime }$has cardinality at least$( 1 - 6 \eta ^ { 1 / 5 } ) | W |$

Given$d \in B$and$w ~ \in ~ W ^ { \prime }$, let us say that d is good for w if for $( 1 - 3 5 \eta ^ { 2 / 5 } )$-almost every pair$( y , z ) \in X _ { r ( x ) + d } { \times } X _ { r ( w ) + d }$we have$\phi ( { \boldsymbol { y } } ) { - } \phi ( { \boldsymbol { x } } )$

$\mathbf { \Phi } = ~ \phi ( z ) - \phi ( w )$. Notice that$| X _ { r ( x ) + d } | \ \geqslant \ | X _ { r ( x ) } | / 2$by Lemma 10.3 and $( B , \sigma M )$-invariance, and$| X _ { r ( w ) + d } | \geqslant | X _ { r ( w ) } | / 2$by Lemma 10.5 (iv). Therefore, the number of$d \in B$that fail to be good for$( x , w )$is at most$3 5 \eta ^ { 2 / 5 } | B |$ because otherwise we would have

$$
\begin{array}{c} e (x, w) \geqslant 1 2 2 5 \eta^ {4 / 5} | B | \min _ {d \in B} | X _ {r (x) + d} | | X _ {r (w) + d} | \\ \geqslant 3 0 6 \eta^ {4 / 5} \sum_ {d \in B} | X _ {r (x) + d} | | X _ {r (w) + d} | \\ = 3 0 6 \eta^ {4 / 5} b (x, w), \end{array}
$$

which would imply that$\epsilon ( w ) \geqslant 3 0 6 \eta ^ { 4 / 5 }$, contradicting the assumption that $w \in W ^ { \prime }$

So far we have shown that

$$
(\forall w \in W ^ {\prime}) \big ((1 - 3 5 \eta^ {2 / 5}) \text {   a.e.   } d \in B \big) \quad d \text {   is   good   for   } w  .\tag{\((*)\}
$$

It follows that

$$
\left(\left(1 - 9 \eta^ {1 / 5}\right) \text {a.e.} d \in B\right) \left(\left(1 - 4 \eta^ {1 / 5}\right) \text {a.e.} w \in W ^ {\prime}\right) d \text {is good for} w,
$$

since otherwise there would be at least$3 6 \eta ^ { 2 / 5 }$pairs$( d , w ) \in B \times W ^ { \prime }$such that d is not good for$w ,$, which contradicts$( * )$

Let$B ^ { \prime }$be the set of all$d \in B$such that d is good for$( 1 - 6 \eta ^ { 1 / 5 } ) .$ almost every$w \in W ^ { \prime }$. We have shown that$B ^ { \prime }$has cardinality at least $( 1 - 9 \eta ^ { 1 / 5 } ) | B |$, as is required in the statement of the lemma. We turn now to the definition of the function$\psi$.

If d is good for$w ,$, then another simple averaging argument shows that

$$
\begin{array}{c} \big ((1 - 6 \eta^ {1 / 5}) \text {a.e.} y \in X _ {r (x) + d} \big) \big ((1 - 6 \eta^ {1 / 5}) \text {a.e.} z \in X _ {r (w) + d} \big) \\ \phi (y) - \phi (x) = \phi (z) - \phi (w). \end{array}
$$

Let$Y _ { r ( x ) + d }$be the set of such y, and for each$y \in Y _ { r ( x ) + d } .$, let$Z _ { y }$be the set of$z \in X _ { r ( w ) + d }$such that$\phi ( y ) - \phi ( x ) = \phi ( z ) - \phi ( w )$. Since$1 - 6 \eta ^ { 1 / 5 } > 1 / 2$ any two of the sets$Z _ { y }$overlap. It is also clear that$\phi$is constant on any set$Z _ { y }$. Therefore, it is constant on$Y _ { r ( x ) + d }$as well, taking a value a, say. This argument also implies that we can find a set$Y _ { r ( w ) + d } \subset X _ { r ( w ) + d }$of size at least$( 1 - 6 \eta ^ { 1 / 5 } ) | X _ { r ( w ) + d } |$on which$\phi$is constant, since we may choose $Y _ { r ( w ) + d } = Z _ { y }$for some$y \in Y _ { r ( x ) + d } .$. Let this constant value be b. Then $a \dot { - } \dot { \phi } ( x ) = b - \phi ( w )$, and this common value we shall call$\psi ( d )$. Because$\phi$ is constant on$Y _ { r ( x ) + d }$which has size at least half that of$X _ { r ( x ) + d } .$, the value of$\psi ( d )$is well-defined$( { \mathrm { i . e . } }$., does not depend on w).

We have shown that, if d is good for w, then$\phi ( z ) - \phi ( w ) = b - \phi ( w ) =$ $\psi ( d )$whenever z belongs to a set$Y _ { r ( w ) + d }$of cardinality at least $( 1 - 6 \eta ^ { 1 / 5 } ) | X _ { r ( w ) + d } |$. Therefore, for every d$\in { \boldsymbol { B ^ { \prime } } }$

$$
\left((1 - 4 \eta^ {1 / 5}) \text {a.e.} w \in W ^ {\prime}\right) \left((1 - 6 \eta^ {1 / 5}) \text {a.e.} w ^ {\prime} \in X _ {r (w) + d}\right) \quad \phi (w ^ {\prime}) - \phi (w) = \psi (d).
$$

This, together with the fact that$| W ^ { \prime } | \geqslant ( 1 - 6 \eta ^ { 1 / 5 } ) | W |$, proves the lemma. (Of course, we have proved a slightly better result, but it is convenient to set all the errors equal to the worst one of$1 0 \eta ^ { 1 / 5 } . )$✷

Later, the following small modification of Lemma 10.6 will be useful.

Lemma 10.7. Let$\psi : B ^ { \prime } \to \mathbb { Z } _ { N }$be the function constructed in Lemma 10.6 and let$\theta = 1 0 \eta ^ { 1 / 5 }$. Then for$( 1 - \theta ^ { 1 / 2 } )$-almost every$w \in W$2

$$
\left((1 - \theta^ {1 / 2}) \text {a.e.} d \in B ^ {\prime}\right) \left((1 - \theta) \text {a.e.} w ^ {\prime} \in X _ {r (w) + d}\right) \quad \phi (w ^ {\prime}) - \phi (w) = \psi (d).
$$

Proof. This is another simple averaging argument. Let us write$P ( w , d )$for the statement

$$
\big ((1 - \theta) \text {   a.e.   } w ^ {\prime} \in X _ {r (w) + d} \big) \quad \phi (w ^ {\prime}) - \phi (w) = \psi (d)  .
$$

Lemma 10.6 states that

$$
(\forall d \in B) ((1 - \theta) \text {   a.e.   } w \in W) \quad P (w, d).\tag{\((*)\}
$$

If what we wish to prove is false, then there are at least$\theta | W | | B ^ { \prime } |$pairs $( w , d ) \in W \times B ^ { \prime }$such that not$P ( w , d )$. This contradicts (∗).✷

Our next main task will be to prove that$\psi$is a homomorphism on$B ^ { \prime }$ Before we do this, we prove a technical lemma which will allow us to condense what would otherwise be a very tedious argument. Roughly speaking, it tells us that we can “shift” statements by some$d \in B$, introducing only a small error.

Lemma 10.8. Let$d \in B ,$let$\theta > 0$and let$P$be a property of elements of W such that$P ( w )$for$( 1 - \theta ) { \mathrm { a . e . ~ } } w \in W$. Then

$$
\left((1 - \theta^ {1 / 2} - \eta) \text {a.e.} w \in W\right) \left((1 - 2 \theta^ {1 / 2}) \text {a.e.} w ^ {\prime} \in X _ {r (w) + d}\right) P (w ^ {\prime}).
$$

Proof. Let$\Delta$be the set of pairs$( w , w ^ { \prime } ) \in W ^ { 2 }$such that$r ( w ^ { \prime } ) - r ( w ) = d$ and not$P ( w ^ { \prime } )$. Because$P ( w ^ { \prime } )$for (1 − θ) a.e.$w \in W$, the cardinality of$\Delta$ is at most$\theta | W | \operatorname* { m a x } _ { w \in W } R ( w )$

Now Lemma 10.5 (vi) and the symmetry of B imply that at most$\eta | W |$ elements of W fail to belong to$W \cap ( W - d )$. Therefore, if the lemma is false, then there are more than$\theta ^ { 1 / 2 } | W |$elements$w \in W \cap ( W - d )$such that not$P ( w ^ { \prime } )$for at least$2 { \theta } ^ { 1 / 2 } | X _ { r ( w ) + d } |$elements of$X _ { r ( w ) + d } .$. Therefore, the cardinality of$\Delta$is greater than$2 \theta | W | \operatorname* { m i n } _ { w \in W } R ( w )$. By Lemma 10.5 (v), this is a contradiction, so the lemma is proved.✷

Lemma 10.9. Let$\theta = 1 0 \eta ^ { 1 / 5 }$and assume that$6 \theta ^ { 1 / 2 } < 1$. Then the function $\psi : B ^ { \prime } \to \mathbb { Z } _ { N }$constructed in Lemma 10.6 is a Freiman homomorphism.

Proof. Suppose that$d _ { 1 } , d _ { 2 } , d _ { 3 } , d _ { 4 } \in B ^ { \prime }$are such that$d _ { 1 } + d _ { 2 } = d _ { 3 } + d _ { 4 }$ Lemma 10.6 tells us that

$$
\left((1 - \theta) \text {   a.e.   } w \in W\right) \left((1 - \theta) \text {   a.e.   } w ^ {\prime} \in X _ {r (w) + d _ {1}}\right) \quad \phi (w ^ {\prime}) - \phi (w) = \psi (d _ {1})\tag{1}
$$

and

$$
\big ((1 - \theta) \text {   a.e.   } w \in W \big) \big ((1 - \theta) \text {   a.e.   } w ^ {\prime \prime} \in X _ {r (w) + d _ {1}} \big) \quad \phi (w ^ {\prime}) - \phi (w) = \psi (d _ {2}).\tag{2}
$$

Applying Lemma 10.8 to (2), with$d = d _ { 1 }$, we deduce that for

$$
\begin{array}{c} \big ((1 - 2 \theta^ {1 / 2}) \text {a.e.} w \in W \big) \big ((1 - 2 \theta^ {1 / 2}) \text {a.e.} w ^ {\prime} \in X _ {r (w) + d _ {1}} \big) \\ \big ((1 - \theta) \text {a.e.} w ^ {\prime \prime} \in X _ {r (w ^ {\prime}) + d _ {2}} \big) \end{array}
$$

we have

$$
\phi (w ^ {\prime \prime}) - \phi (w ^ {\prime}) = \psi (d _ {2}).\tag{3}
$$

Noting that$r ( w ^ { \prime } ) + d _ { 2 }$is the same as$r ( w ) + d _ { 1 } + d _ { 2 }$when$w ^ { \prime } \in X _ { r ( w ) + d _ { 1 } }$ we can deduce from (1) and (3) that for

$$
\begin{array}{c} \big ((1 - 3 \theta^ {1 / 2}) \text {a.e.} w \in W \big) \big ((1 - 3 \theta^ {1 / 2}) \text {a.e.} w ^ {\prime} \in X _ {r (w) + d _ {1}} \big) \\ \big ((1 - \theta) \text {a.e.} w ^ {\prime \prime} \in X _ {r (w) + d _ {1} + d _ {2}} \big) \end{array}
$$

we have

$$
\phi (w ^ {\prime}) - \phi (w) = \psi (d _ {1}) \quad \text { and } \quad \phi (w ^ {\prime \prime}) - \phi (w ^ {\prime}) = \psi (d _ {2}).\tag{4}
$$

Because$1 - 3 \theta ^ { 1 / 2 } > 0$, it follows from (4) that in particular

$$
\begin{array}{c} \big ((1 - 3 \theta^ {1 / 2}) \text {a.e.} w \in W \big) \big ((1 - \theta) \text {a.e.} w ^ {\prime \prime} \in X _ {r (w) + d _ {1} + d _ {2}} \big) \\ \phi (w ^ {\prime \prime}) - \phi (w) = \psi (d _ {1}) + \psi (d _ {2}). \end{array}\tag{5}
$$

An identical argument shows that

$$
\begin{array}{c} \big ((1 - 3 \theta^ {1 / 2}) \text {a.e.} w \in W \big) \big ((1 - \theta) \text {a.e.} w ^ {\prime \prime} \in X _ {r (w) + d _ {3} + d _ {4}} \big) \\ \phi (w ^ {\prime \prime}) - \phi (w) = \psi (d _ {3}) + \psi (d _ {4}). \end{array}\tag{6}
$$

Since$1 - 6 \theta ^ { 1 / 2 } > 0$and$d _ { 1 } + d _ { 2 } = d _ { 3 } + d _ { 4 }$, (5) and (6) imply that $\psi ( d _ { 1 } ) + \psi ( d _ { 2 } ) = \psi ( d _ { 3 } ) + \psi ( d _ { 4 } )$, as required.✷

We shall now specialize to the case where B is a Bohr neighbourhood. (For the definition and elementary facts, see §7.) First, we need some more easy results about such sets.

Lemma 10.10. Let K be a set of size k, let$\scriptstyle { B = B ( K , \delta ) }$and let d∈$B ( K , \zeta )$ Then$| B \cap ( B + d ) | \geqslant ( 1 - 2 ^ { k + 1 } \delta ^ { - k } k \zeta ) | B |$

Proof. If$x \in B \setminus \left( B + d \right)$, then for some$r \in K$we must have

$$
(\delta - \zeta) N \leqslant | r d | \leqslant \delta N,
$$

as otherwise x would belong to$B ( K , \delta \mathrm { ~ - ~ } \zeta )$, which would imply that $x - d \in B$. It follows that the cardinality of$B \setminus ( B + d )$is at most$2 k \zeta N$ Since B has cardinality at least$( \delta / 2 ) ^ { k } N$, the result follows.✷

Corollary 10.11. Let K be a set of size$k ,$let$B = B ( K , \delta )$, let$B ^ { \prime } \subset B$ be a set of size at least$( 7 / 8 ) | B |$, let$\zeta = 2 ^ { - ( k + 4 ) } \delta ^ { k } k$and let$C = B ( K , \zeta )$ Then$C \subset B ^ { \prime } - B ^ { \prime }$and any homomorphism$\psi$from$B ^ { \prime }$to$\mathbb { Z } _ { N }$induces a homomorphism$\psi _ { 1 }$from$C$to$\mathbb { Z } _ { N }$

Proof. If$d \in C$, then$| B \cap ( B + d ) | \geqslant ( 7 / 8 ) | B |$, by Lemma 10.10 and our choice of$\zeta .$. This implies that$| B ^ { \prime } \cap ( B ^ { \prime } + d ) | \geqslant ( 5 / 8 ) | B |$and in particular that$d \in B ^ { \prime } - B ^ { \prime }$

It follows that$\psi$induces a function$\psi _ { 1 }$on$C .$. The content of the corollary is that ψ<sub>1</sub> is itself a homomorphism. To prove this, let$d _ { 1 } , d _ { 2 } , d _ { 3 } , d _ { 4 } \in C$ with$d _ { 1 } + d _ { 2 } = d _ { 3 } + d _ { 4 }$. By what we have just proved, we know that $B \cap \left( B + d _ { 1 } \right)$and$\left( B + d _ { 1 } \right) \cap \left( B + d _ { 1 } + d _ { 2 } \right)$both have cardinality at least $( 7 / 8 ) | B |$. Therefore,$B \cap ( B + d _ { 1 } ) \cap ( B + d _ { 1 } + d _ { 2 } )$has cardinality at least $( 3 / 4 ) | B |$. We also know that$B \cap \left( B + d _ { 3 } \right)$has cardinality at least$( 7 / 8 ) | B |$ so$B \cap ( B + d _ { 1 } ) \cap ( B + d _ { 1 } + d _ { 2 } ) \cap ( B + d _ { 3 } )$has cardinality at least$( 5 / 8 ) | B |$ This implies that$B ^ { \prime } \cap ( B ^ { \prime } + d _ { 1 } ) \cap ( B ^ { \prime } + d _ { 1 } + d _ { 2 } ) \cap ( B ^ { \prime } + d _ { 3 } )$has cardinality at least$( 1 / 8 ) | B |$. It follows that we can find$x \ \in \ B ^ { \prime }$such that $x - d _ { 1 } , x - d _ { 3 }$and$x - d _ { 1 } - d _ { 2 } = x - d _ { 3 } - d _ { 4 }$all belong to$B ^ { \prime }$. Hence, $\psi _ { 1 } ( d _ { 1 } ) + \psi _ { 1 } ( d _ { 2 } ) = \psi _ { 1 } ( d _ { 3 } ) + \psi _ { 1 } ( d _ { 4 } )$as was needed.✷

Armed with these facts about Bohr neighbourhoods, let us return to the set$W ,$now with the assumption that$B = B ( K , \delta )$is a Bohr neighbourhood. Let$W _ { 1 }$be the set of all$w \in W$such that

$$
\left((1 - \theta^ {1 / 2}) \text {a.e.} d \in B ^ {\prime}\right) \left((1 - \theta) \text {a.e.} z \in X _ {r (w) + d}\right) \quad \phi (z) - \phi (w) = \psi (d).
$$

If$\theta ^ { 1 / 2 } \leqslant 1 / 8$(as we shall assume), then Lemma 10.7 implies that$W _ { 1 }$has cardinality at least$7 | W | / 8$

Lemma 10.12. Assume that$\theta ^ { 1 / 2 } \leqslant 1 / 8$. Let$B = B ( K , \delta )$and let$B ^ { \prime }$and $\psi$be given by Lemma 10.6. Let$C$and$\psi _ { 1 }$be as in Corollary 10.11 and let $w _ { 1 } , w _ { 2 } \in W _ { 1 }$with$r ( w _ { 1 } ) - r ( w _ { 2 } ) = c \in C$. Then$\phi ( w _ { 1 } ) - \phi ( w _ { 2 } ) = \psi _ { 1 } ( c )$

Proof. By the definition of$W _ { 1 }$and the assumption that$\theta ^ { 1 / 2 } \leqslant 1 / 8$, we have the statements

$$
(7 / 8 \text {   a.e.   } d \in B ^ {\prime}) ((1 - \theta) \text {   a.e.   } z \in X _ {r (w _ {1}) + d}) \quad \phi (z) - \phi (w _ {1}) = \psi (d)\tag{1}
$$

and

$$
(7 / 8 \text { a.e. } d \in B ^ {\prime}) \big ((1 - \theta) \text { a.e. } z \in X _ {r (w _ {2}) + d} \big) \quad \phi (z) - \phi (w _ {2}) = \psi (d)\tag{2}
$$

Because$r ( w _ { 1 } ) - r ( w _ { 2 } ) \in C .$, we know from the proof of Corollary 10.11 that

$$
\left| B ^ {\prime} \cap (B ^ {\prime} - r (w _ {1}) + r (w _ {2})) \right| \geqslant (5 / 8) | B ^ {\prime} |.\tag{3}
$$

(2) and (3) imply that

$$
\begin{array}{c} (1 / 2 \text {a.e.} d \in B ^ {\prime}) \big ((1 - \theta) \text {a.e.} z \in X _ {d + r (w _ {1})} \big) \\ \phi (z) - \phi (w _ {2}) = \psi \big (d + r (w _ {1}) - r (w _ {2}) \big). \end{array}\tag{4}
$$

From (1) and (4) it follows that for 3/8-almost every$d \in B ^ { \prime }$, for$( 1 - \theta )$ almost every$z \in X _ { r ( w _ { 1 } ) + d }$we have both

$$
\phi (z) - \phi (w _ {1}) = \psi (d) \text {   and   } \phi (z) - \phi (w _ {2}) = \psi \bigl (d + r (w _ {1}) - r (w _ {2}) \bigr).
$$

In particular, there exist d and z such that both equations hold, which implies that

$$
\phi (w _ {2}) - \phi (w _ {1}) = \psi (d + r (w _ {1}) - r (w _ {2})) - \psi (d) = \psi (d + c) - \psi (c) = \psi (c).
$$

We are now in a position to prove a new version of Lemma 7.7 in which the hypotheses are weaker. Before stating it, let us consider the constraints on the various parameters that have been introduced in this section. First of all, the strongest condition that we have placed on η is that$\theta ^ { 1 / 2 } < 1 / 6$ where$\theta = 1 0 \eta ^ { 1 / 5 }$(see Lemma 10.9). It can be checked that this condition is satisfied when$\eta = 2 ^ { - 4 3 }$. We set$\rho =$min$\lbrace \alpha / 1 9 2 , \alpha ^ { 2 } / 3 2 \rbrace$and$\sigma = \eta \rho ^ { 4 } \alpha / 3 8 4$ If$\alpha \leqslant 1 / 6$, then$\rho = \alpha ^ { 2 } / 3 2$and all the results of the section are satisfied (for our chosen value of η) if$\sigma = 2 ^ { - 7 2 } \alpha ^ { 9 }$

Theorem 10.13. Let$\eta = 2 ^ { - 4 3 }$and let$X = X _ { 0 } \cup \dots \cup X _ { N - 1 }$be the domain of a$( 1 - \eta )$-homomorphism$\phi$of order eight. Suppose that$| X _ { i } | \leqslant M$for each i and that$| X | = \alpha M N$. Let$g ( s )$be the size of$X _ { s }$for every s, let$\lambda =$ $2 ^ { - 3 7 } \alpha ^ { 1 1 / 2 }$and define K to be$\{ r \in \mathbb { Z } _ { N } : | \hat { g } ( r ) | \geqslant \lambda M \}$. Then$| K | \leqslant 2 ^ { 7 4 } \alpha ^ { - 1 0 }$ Let$k = 2 ^ { 7 4 } \alpha ^ { - 1 0 }$, let$\epsilon = \alpha ^ { - 4 } \lambda ^ { 4 } / \pi$and let$\zeta = 2 ^ { - 1 5 5 k } \alpha ^ { 1 8 k } k \leqslant 2 ^ { - ( k + 4 ) } \epsilon ^ { k } k$ $I f C = B ( K , \zeta )$, then there is a homomorphism$\psi _ { 1 } : C \to \mathbb { Z } _ { N }$together with a subset$Y \subset X$of size at least$\alpha ^ { 3 } | X | / 1 0 0 0$such that, whenever$y , z \in Y$ and$r ( y ) - r ( z ) \in C$, we have$\phi ( y ) - \phi ( z ) = \psi _ { 1 } ( r ( y ) - r ( z ) )$.

Proof. Let$B = B ( K , \epsilon )$and let$L = \alpha ^ { 3 } M ^ { 4 } N ^ { 3 }$. We know that$\left| 2 X - 2 X \right| =$ $( \alpha M N ) ^ { 4 }$and that$| ( 2 X - 2 X ) _ { s } | \leqslant \alpha ^ { 3 } M ^ { 4 } N ^ { 3 } = L$for every s. Now we shall show that$2 X - 2 X$is (B, σL)-invariant.

If we write$h ( s ) = | ( 2 X - 2 X ) _ { s } |$, then$\hat { h } ( r ) = | \hat { g } ( r ) | ^ { 4 }$. We know also that$| \hat { g } ( r ) | \leqslant \alpha M N$for every r. Since$\| \hat { g } \| ^ { 2 } = N \| g \| ^ { 2 } \leqslant \alpha M ^ { 2 } N ^ { 2 }$, we find that$| K | \leqslant \lambda ^ { - 2 } \alpha = 2 ^ { 7 4 } \alpha ^ { - 1 0 }$, as in the proof of Lemma 7.7. We also have the obvious inequality

$$
\sum_ {r \notin K} | \hat {g} (r) | ^ {4} \leqslant \lambda^ {2} M ^ {2} N ^ {2} \| \hat {g} \| ^ {2} \leqslant \alpha \lambda^ {2} M ^ {4} N ^ {4}.
$$

Now$\begin{array} { r } { \boldsymbol { h } ( s ) = N ^ { - 1 } \sum _ { r } \hat { \boldsymbol { h } } ( r ) \omega ^ { r s } } \end{array}$, so

$$
\begin{array}{l} h (s) - h (t) = N ^ {- 1} \sum_ {r} | \hat {g} (r) | ^ {4} (\omega^ {r s} - \omega^ {r t}) \\ \qquad = N ^ {- 1} \sum_ {r \in K} | \hat {g} (r) | ^ {4} \omega^ {r t} (\omega^ {r (s - t)} - 1) + N ^ {- 1} \sum_ {r \notin K} | \hat {g} (r) | ^ {4} \omega^ {r t} (\omega^ {r (s - t)} - 1). \end{array}
$$

From the inequality above, the sum over$r \not \in K$is at most$2 \alpha \lambda ^ { 2 } M ^ { 4 } N ^ { 3 }$(after the multiplication by$N ^ { - 1 } )$. As for the other part, if we make the additional assumption that$s - t \in B$, then$| \omega ^ { r ( s - t ) } - 1 | \leqslant$2π for each$r \in K$, so the sum is at most$N ^ { - 1 } 2 \pi \epsilon | K _ { \lambda } | ( \alpha \dot { M } N ) ^ { 4 } \leqslant 2 \pi \epsilon \lambda ^ { - 2 } \alpha ^ { 5 } M ^ { 4 } N ^ { 3 } = 2 \alpha \lambda ^ { 2 } M ^ { 4 } N ^ { 3 }$ The$( B , \sigma L )$-invariance of$2 X - 2 X$follows.

We know that$\phi$induces a$( 1 - \eta )$-homomorphism$\phi ^ { \prime \prime }$(of order two) on$2 X - 2 X$Therefore, we can find a set$W$of cardinality at least $\rho \alpha ^ { 2 } L N / 1 6 = \alpha ^ { 7 } M ^ { 4 } N ^ { 4 } / 5 1 2$with the properties claimed in Lemma 10.5. Corollary 10.11, Lemma 10.12 and the definition in between then give us a set$W _ { 1 }$of cardinality at least$\alpha ^ { 7 } M ^ { 4 } N ^ { 4 } / 1 0 0 0 = \alpha ^ { 3 } | 2 X - 2 X | / 1 0 0 0$and a homomorphism$\psi _ { 1 } : W _ { 1 } \to \mathbb { Z } _ { N }$such that, whenever$w _ { 1 } , w _ { 2 } \in W _ { 1 }$and $r ( w _ { 1 } ) - r ( w _ { 2 } ) \in C$, we have$\phi ^ { \prime \prime } ( w _ { 1 } ) - \phi ^ { \prime \prime } ( w _ { 2 } ) = \psi _ { 1 } ( w _ { 1 } - w _ { 2 } )$

Now choose$( x _ { 2 } , x _ { 3 } , x _ { 4 } ) \in X ^ { 3 }$uniformly at random. The expected number of$y \in X$such that$( y , x _ { 2 } , x _ { 3 } , x _ { 4 } ) \in W$is at least$\alpha ^ { 3 } | X | / 1 0 0 0$, so let us fix$( x _ { 2 } , x _ { 3 } , x _ { 4 } )$such that the set Y of all y such that$( y , x _ { 2 } , x _ { 3 } , x _ { 4 } ) \in W$has cardinality at least$\alpha ^ { 3 } | X | / 1 0 0 0$. If$y , z \in Y$and$r ( y ) - r ( z ) = c \in C$, then $r ( y , x _ { 2 } , x _ { 3 } , x _ { 4 } ) - r ( z , x _ { 2 } , x _ { 3 } , x _ { 4 } ) = c ,$so

$$
\phi (y) - \phi (z) = \phi^ {\prime \prime} (y, x _ {2}, x _ {3}, x _ {4}) - \phi^ {\prime \prime} (z, x _ {2}, x _ {3}, x _ {4}) = \psi (y - z).
$$

This proves the theorem.

Corollary 10.14. Let K be as in Theorem 10.13, let$Y$be the set obtained there and let m be a positive integer. For every$d \in B ( K , \zeta / m )$ there exists c such that$\phi ( x ) - \phi ( y ) = c ( r ( x ) - r ( y ) )$) whenever$x , y \in Y$and $r ( x ) - r ( y )$belongs to the set$\{ j d : - m \leqslant j \leqslant m \}$

Proof. As with Corollary 7.8 this follows from the observations that$\{ j d :$ $- m \leqslant j \leqslant m \} \subset B ( K , \zeta )$, that the restriction of any homomorphism to $\{ j d : - m \leqslant j \leqslant m \}$is linear and that$\psi _ { 1 } ( 0 ) = 0$✷

## 11 The Problem of Longer Progressions

This section is a brief introduction to the rest of the paper and the difficulties that must be overcome before the proof can be extended from progressions of length four to progressions of arbitrary length. As with the other known proofs of Szemer´edi’s theorem, the new dificulties that arise with progressions of length greater than four are considerable. In our case, it is because we must extend Freiman’s theorem (or, to be more accurate, our weaker version of Freiman’s theorem) from “linear” functions to “multilinear” ones.

To see this, consider the case of progressions of length five. The main result of$\ S 3$suggests that we should$_ \mathrm { g o }$up a degree, and look at sets that fail to be uniform of degree three, or, as we shall say, cubically uniform. (Sets such as$\{ x \in \mathbb { Z } _ { N } : | x ^ { 3 } | \leqslant N / 1 0 0 0 0 \}$} show that this is necessary as well as suficient.) If$A$is such a set and$f$is the balanced function of$A ,$then $\Delta ( f ; k , l )$has a large Fourier coeficient for many values of$k , l .$. In other words, we can find a large subset$B \subset \mathbb { Z } _ { N } ^ { 2 }$and a function$\phi : B \to \mathbb { Z } _ { N }$such that$\Delta ( f ; k , l )$has a large Fourier coeficient at$\phi ( k , l )$. By the main result of$\ S 6$, for some reasonably large$\gamma > 0$the function$\phi$is γ-additive in both variables, and this is true for the restriction of$\phi$to any large subset of$B$ That is, for many x we can fix$x$and$\phi ( x , y )$will be somewhat additive in$y _ { \mathrm { { i } } }$, and vice versa.

The object of the next few sections will be to look at such “somewhat bi-additive” functions, and show that there is a large subset$C \subset B$such that the restriction of$\phi$to$C$resembles a multidimensional bilinear function, rather as a somewhat additive function has a restriction resembling a multidimensional linear one. This involves showing that the multidimensional linearity of$\phi$in x somehow “interacts” with the multidimensional linearity in$y ,$which turns out to be harder than one might think, as we shall now explain.

First, it is important that the additivity property should hold for restrictions of$\phi .$For example, let$\lambda$be an arbitrary function from$\mathbb { Z } _ { N }$to$\mathbb { Z } _ { N }$ and define

$$
\phi (x, y) = \left\{ \begin{array}{l l} \lambda (x) y & 0 \leqslant x \leqslant y <   N \\ x \lambda (y) & 0 \leqslant y <   x <   N. \end{array} \right.
$$

There are certainly many additive quadruples in each variable, but if λ does not have special additivity properties, then the quadruples with x fixed do not mix with those with$y$fixed and there is nothing more to say about$\phi ,$ and in particular no restriction of$\phi$that looks bilinear.

Let us informally call a function quasilinear if it resembles a low-dimensional linear function (see, for example, the function defined at the end of$\ S 6 )$. A more serious complication arises even if we know for every x that $\phi ( x , y )$is quasilinear in$y$for every x and vice versa. It is tempting to suppose that one might be able to find a large subset$B ^ { \prime } \subset B .$, and numbers $x _ { 0 } , x _ { 1 } , \dotsc , x _ { d } , \ r _ { 1 } , \dotsc , r _ { d } , \ y _ { 0 } , y _ { 1 } , \dotsc , y _ { d } , \ s _ { 1 } , \dotsc , s _ { d }$and$( c _ { i j } ) _ { i , j = 0 } ^ { d }$such that the restriction of$\phi$to$B ^ { \prime }$was of the form

$$
\phi \bigg (x _ {0} + \sum_ {i = 1} ^ {d} a _ {i} x _ {i}, y _ {0} + \sum_ {i = 1} ^ {d} b _ {j} y _ {j} \bigg) = \sum_ {i, j = 0} ^ {d} c _ {i j} a _ {i} b _ {j}
$$

for$0 \leqslant x _ { i } < r _ { i }$and$0 \leqslant y _ { j } < s _ { j }$

However, this would imply that one could find a small “common basis” for all the functions$y \mapsto \phi ( x , y )$(and similarly the other way round) and a simple example shows that such a statement is too strong. Indeed, let$\psi$ be a non-trivial (i.e., non-linear) quasilinear function from$\mathbb { Z } _ { N }$to$\mathbb { Z } _ { N }$. (For definiteness one could let$\psi ( z ) = z { \big ( } { \mathrm { m o d } } m { \big ) }$for some m near${ \sqrt { N } } . )$Define $\phi ( x , y )$to be$\psi ( x y )$. The natural bases for the functions$y \mapsto \psi ( x y )$are all completely diferent, and there is no small basis that can be used for all (or even a large proportion) of them. We shall not prove this here.

However, just as what we really used when proving Szemer´edi’s theorem for progressions of length four was Corollary 7.10, which told us that the function φ had a small (but not too small) linear restriction, the statement we actually need for progressions of length five is that one can find reasonably long arithmetic progressions (we obtain a power of N) P and$Q$with the same common diference and a bilinear function$\psi : { P } \times { Q }  \mathbb { Z } _ { N }$such that$\psi$agrees with$\phi$for a significant proportion of the points$( x , y ) \in P { \times } Q$ If we wish to prove Szemer´edi’s theorem for progressions of length$k ,$we need the obvious generalization of this to$\left( k - 3 \right)$)-linear functions. In proving these statements, we shall obtain some insight into the form of a typical “quasimultilinear” function, but we avoid having to describe them precisely. It would be interesting to obtain a precise description, so this is an area where there is still work to be done.

It seems, then, that there is something objective about the problem which makes the dificulty increase sharply as the size of the desired progression goes from two to three to four to five, and then remain roughly constant from that point onwards. Three is the first non-trivial case, four involves quadratic functions rather than just linear ones and five involves bilinearity in the large Fourier coeficients rather than just linearity, but that is the last time that some parameter, which one has hardly noticed because it equals one, suddenly and annoyingly changes to two.

## 12 Strengthening a Bihomomorphism

Although the proof of Szemer´edi’s theorem for progressions of length five is not significantly easier than it is for the result in general, the notation is cleaner and one or two complications can be avoided. Therefore, we shall treat this case separately. Let us take a non-cubically uniform function $f : \mathbb { Z } _ { N } \to D$and begin the longish process of finding bilinear behaviour in any function$\phi$for which$\Delta ( f ; k , l ) ^ { \wedge } ( \phi ( k , l ) )$is often large.

In order to motivate some of the lemmas that follow, let us consider what the natural two-variable analogue of a Freiman homomorphism ought to be. That is, given a subset$A \subset \mathbb { Z } _ { N } ^ { 2 }$, we ask what property of a function$\phi : A  \mathbb { Z } _ { N }$relates to that of being a homomorphism in the way that bilinearity relates to linearity. In the last section, we discussed an analogous problem for quasilinear functions rather than homomorphisms, and saw that it was not easy to give a satisfactory definition. Giving a good definition of a “bihomomorphism” is not all that easy either.

The most obvious definition is that$\phi ( x , y )$should be a homomorphism in y for any fixed$x ,$and vice versa. This property can indeed be shown to hold for the functions$\phi$that will concern us. However, to see that it is natural to ask for more, consider the set$A = A _ { 1 } \cup A _ { 2 }$, where$A _ { 1 }$is the set of all$( x , y )$such that$0 < x < N / 2$and$0 < y < N / 2$, while$A _ { 2 }$is the set of all$( x , y )$such that$N / 2 < x < N$and$N / 2 < y < N$. Define a function$\phi$ by letting$\phi ( x , y )$be xy if$( x , y ) \in A _ { 1 }$and 2xy if$( x , y ) \in A _ { 2 }$. This function has the following undesirable property. Suppose we define a new function $\psi$by setting

$$
\psi (x, d) = \phi (x, y + d) - \phi (x, y)
$$

whenever$y$can be found such that both$( x , y )$and$( x , y + d )$belong to $A$. This is a well-defined function and for fixed x it is an isomorphism in d. However, it can be checked very easily that for fixed d it is not an isomorphism in x. This suggests that a stronger property will probably be useful, and the suggestion turns out to be correct.

To simplify the discussion, let us introduce some terminology. A vertical parallelogram is a quadruple of points in$\mathbb { Z } _ { N } ^ { 2 }$of the form$( ( x , y ) , ( x , y + h )$，$( x + w , y ^ { \prime } ) , ( x + w , y ^ { \prime } + h ) \}$. We shall call w and$h$respectively the width and height of the parallelogram. If P is the above parallelogram, then we shall denote these by$w ( P )$and$h ( P )$. If$\phi$is a function from$A \subset \mathbb { Z } _ { N } ^ { 2 }$to $\mathbb { Z } _ { N }$and all the points of P lie in A, then we set

$$
\phi (P) = \phi (x, y) - \phi (x, y + h) - \phi (x + w, y ^ {\prime}) + \phi (x + w, y ^ {\prime} + h).
$$

Ideally, we would like to find, given suitable conditions on φ, a large set such that, for any vertical parallelogram P lying in the set,$\phi ( P )$depends only on the width and height of$P .$This may be possible, and has the potential to simplify this paper considerably, but we have not managed to find an argument for or against it. Instead, we shall obtain a set where $\phi ( P )$is nearly independent of everything except for the width and height.

Our first main task will be to find many pairs$P _ { 1 } , P _ { 2 }$of vertical parallelograms of the same width and height, such that$\phi ( P _ { 1 } ) = \phi ( P _ { 2 } )$. For this, we shall need a slight generalization of Proposition 6.1, proved in exactly the same way.

Proposition 12.1. For each$k \in \mathbb { Z } _ { N }$, let$\lambda _ { k } \geqslant 0 .$. Let$f _ { 1 } , \ldots , f _ { p }$be functions from$\mathbb { Z } _ { N }$to$D$and let$\phi _ { 1 } , . . . , \phi _ { p }$be functions from$\mathbb { Z } _ { N }$to$\mathbb { Z } _ { N }$ such that p

$$
\sum_ {k} \lambda_ {k} \prod_ {i = 1} ^ {p} | \Delta (f _ {i}; k) ^ {\wedge} (\phi_ {i} (k)) | ^ {2} \geqslant \alpha N ^ {2 p + 1}.
$$

Call a quadruple$( a , b , c , d ) \in \mathbb { Z } _ { N } ^ { 4 }$simultaneously additive if$a - b = c - d$ and$\phi _ { i } ( a ) - \phi _ { i } ( b ) = \phi _ { i } ( c ) - \phi _ { i } ( d )$for every$i \leqslant p$. Then the sum of$\lambda _ { a } \lambda _ { b } \lambda _ { c } \lambda _ { d }$ over all simultaneously additive quadruples$( a , b , c , d )$is at least$\alpha ^ { 4 } N ^ { 3 }$

Proof. Expanding the given inequality yields that

$$
\sum_ {k} \lambda_ {k} \sum_ {s _ {1}, \dots , s _ {p}} \sum_ {t _ {1}, \dots , t _ {p}} \prod_ {i = 1} ^ {p} f _ {i} (s _ {i}) \overline {{f _ {i} (s _ {i} - k) f _ {i} (t _ {i})}} f _ {i} (t _ {i} - k) \omega^ {- \phi_ {i} (k) (s _ {i} - t _ {i})} \geqslant \alpha N ^ {2 p + 1}.
$$

Substituting$u _ { i } = s _ { i } - t _ { i }$then gives

$$
\sum_ {k} \lambda_ {k} \sum_ {s _ {1}, \dots , s _ {p}} \sum_ {u _ {1}, \dots , u _ {p}} \prod_ {i = 1} ^ {p} f _ {i} (s _ {i}) \overline {{f _ {i} (s _ {i} - k) f _ {i} (s _ {i} - u _ {i})}} f _ {i} (s _ {i} - k - u _ {i}) \omega^ {- \phi_ {i} (k) u _ {i}}
$$

$$
\geqslant \alpha N ^ {2 p + 1}.
$$

Since$| f _ { i } ( x ) | \leqslant 1$for every x and$i ,$this implies that

$$
\sum_ {s _ {1}, \dots , s _ {p}} \sum_ {u _ {1}, \dots , u _ {p}} \left| \sum_ {k} \lambda_ {k} \prod_ {i = 1} ^ {p} \overline {{f _ {i} (s _ {i} - k)}} f (s _ {i} - k - u _ {i}) \omega^ {- \phi_ {i} (k) u _ {i}} \right| \geqslant \alpha N ^ {2 p + 1}
$$

and hence, by the Cauchy-Schwarz inequality, that

$$
\sum_ {s _ {1}, \ldots , s _ {p}} \sum_ {u _ {1}, \ldots , u _ {p}} \left| \sum_ {k} \lambda_ {k} \prod_ {i = 1} ^ {p} \overline {{f _ {i} (s _ {i} - k)}} f (s _ {i} - k - u _ {i}) \omega^ {- \phi_ {i} (k) u _ {i}} \right| ^ {2} \geqslant \alpha^ {2} N ^ {2 p + 2}.
$$

Let us introduce a new variable s and write$v _ { i } = s - s _ { i }$. Then, multiplying both sides by N (in diferent ways) we obtain

$$
\sum_ {s} \sum_ {u _ {1}, \dots , u _ {p}} \sum_ {v _ {1}, \dots , v _ {p}} \left| \sum_ {k} \lambda_ {k} \prod_ {i = 1} ^ {p} \overline {{f _ {i} (s - v _ {i} - k)}} f _ {i} (s - v _ {i} - k - u _ {i}) \omega^ {- \phi_ {i} (k) u _ {i}} \right| ^ {2} \geqslant \alpha^ {2} N ^ {2 p + 3}.
$$

We now apply Lemma 2.1 to the functions

$$
a _ {u, v} (k) = \prod_ {i = 1} ^ {p} \overline {{f _ {i} (- v _ {i} - k)}} f _ {i} (- v _ {i} - k - u _ {i})
$$

and

$$
b _ {u, v} (k) = \lambda_ {k} \prod_ {i = 1} ^ {p} \omega^ {\phi_ {i} (k) u _ {i}},
$$

which tells us that

$$
\sum_ {u, v} \sum_ {r} | \hat {a} _ {u, v} (r) | ^ {2} | \hat {b} _ {u, v} (r) | ^ {2} \geqslant \alpha^ {2} N ^ {2 p + 4}.
$$

By the Cauchy-Schwarz inequality it follows that

$$
\left(\sum_ {u, v} \sum_ {r} | \hat {a} _ {u, v} (r) | ^ {4}\right) \left(\sum_ {u, v} \sum_ {r} | \hat {b} _ {u, v} (r) | ^ {4}\right) \geqslant \alpha^ {4} N ^ {4 p + 8}.
$$

Now$\begin{array} { r } { \sum _ { r } | \hat { a } _ { u , v } ( r ) | ^ { 4 } ~ \mathrm { i s } , } \end{array}$for every$u , v ,$at most$N ^ { 4 } \mathrm { ( e . g . }$by$\mathrm { ~ \ S 2 ~ } \left( \mathrm { 6 } \right) )$so $\begin{array} { r } { \sum _ { u , v } \sum _ { r } | \hat { a } _ { u , v } ( r ) | ^ { 4 } \leqslant N ^ { 2 p + 4 } } \end{array}$. Since$\begin{array} { r } { \hat { b } _ { u , v } ( r ) = \sum _ { k } \lambda _ { k } \prod _ { i = 1 } ^ { p } \omega ^ { \phi _ { i } ( k ) u _ { i } - r k } } \end{array}$, which  does not depend on$v = ( v _ { 1 } , \ldots , v _ { k } )$, it follows that

$$
\sum_ {u _ {1}, \ldots , u _ {p}} \sum_ {r} \Big | \sum_ {k} \lambda_ {k} \prod_ {i = 1} ^ {p} \omega^ {\phi_ {i} (k) u _ {i} - r k} \Big | ^ {4} \geqslant \alpha^ {4} N ^ {p + 4}.
$$

But the left-hand side above is easily seen to be$N ^ { p + 1 }$times the sum of $\lambda _ { a } \lambda _ { b } \lambda _ { c } \lambda _ { d }$over all simultaneously additive quadruples$( a , b , c , d )$. The result is proved.✷

We shall now apply the above result to find many good pairs of parallelograms. Note that the number of pairs$( P _ { 1 } , P _ { 2 } )$of vertical parallelograms with the same width and height is$N ^ { 8 }$

Lemma 12.2. Let$\gamma , \eta > 0 ;$, let$f : \mathbb { Z } _ { N } \to D$and let$B \subset \mathbb { Z } _ { N }$be a set of cardinality$\beta N ^ { 2 }$such that$| \Delta ( f ; k , l ) ^ { \wedge } ( \phi ( k , l ) ) | \geqslant \gamma N$for every$( k , l ) \in B$ Then there are at least$\beta ^ { 1 6 } \gamma ^ { 4 8 } N ^ { 8 }$pairs$( P _ { 1 } , P _ { 2 } )$of vertical parallelograms such that$P _ { 1 }$and$P _ { 2 }$have the same width and height and such that$\phi ( P _ { 1 } ) =$ $\phi ( P _ { 2 } )$

Proof. The average size of a vertical cross-section of$B$(that${ \mathrm { i s } } ,$a set of the form$B _ { x } = \{ y \in \mathbb { Z } _ { N } : ( x , y ) \in B \} )$) is$\beta N$. Hence, by Lemma 6.1 and H¨older’s inequality, the average number of additive quadruples in a vertical cross-section of B is at least$( \beta \gamma ^ { 2 } ) ^ { 4 } N ^ { 3 }$. We shall call a pair of points$\big ( ( x , y ) , ( x , y + h ) \big )$a vertical edge of height h. Given such a pair, define$q \big ( ( x , y ) , ( x , y + h ) \big )$to be the number of$y ^ { \prime } \in \mathbb { Z } _ { N }$such that

$$
\phi (x, y + h) - \phi (x, y) = \phi (x, y ^ {\prime} + h) - \phi (x, y ^ {\prime}),
$$

where equality is deemed not to hold unless$\phi$is defined at all four points. Letting$\zeta = ( \beta \gamma ^ { 2 } ) ^ { 4 }$, we have that the average value of$q ( e )$over all vertical edges e is at least$\zeta N$

For each$h ,$let$\zeta ( h )$be the average of$q ( e )$over vertical edges e of height h. We can find y such that, setting$\lambda _ { x } = N ^ { - 1 } q \big ( ( x , y ) , ( x , y + h ) \big )$ we have$\begin{array} { r } { \sum _ { x } \lambda _ { x } \geqslant \zeta ( h ) N } \end{array}$. Since$\lambda _ { x }$is zero unless both$( x , y )$and$( x , y + h )$ lie in B, this tells us that

$$
\sum_ {x} \lambda_ {x} \left| \Delta (f; x, y + h) ^ {\wedge} (\phi (x, y + h)) \right| ^ {2} \left| \Delta (f; x, y) ^ {\wedge} (\phi (x, y)) \right| ^ {2} \geqslant \zeta (h) \gamma^ {4} N ^ {5}.
$$

Hence, by Proposition 12.1, the sum of$\lambda _ { a } \lambda _ { b } \lambda _ { c } \lambda _ { d }$over all quadruples $( a , b , c , d )$such that$a - b = c - d , \phi ( a , y ) - \phi ( b , y ) - \phi ( c , y ) + \phi ( d , y )$and $\phi ( a , y + h ) - \phi ( b , y + h ) - \phi ( c , y + h ) + \phi ( d , y + h ) |$is at least$( \zeta ( h ) \gamma ^ { 4 } ) ^ { 4 } N ^ { 3 }$ Each such quadruple gives rise to a set of$N ^ { 4 } \lambda _ { a } \lambda _ { b } \lambda _ { c } \lambda _ { d }$pairs of parallelograms with the desired properties, and all these sets are disjoint. Summing over all h and using the fact that the average value of$\zeta ( h )$is$\zeta ,$we obtain from H¨older’s inequality that the total number of pairs of parallelograms with the given properties is at least$\zeta ^ { 4 } \gamma ^ { 1 6 } N ^ { 8 }$, which proves the result. ✷

We shall in fact need many arrangements of eight parallelograms $( P _ { 1 } , \ldots , P _ { 8 } )$, all of the same height, such that

$$
w (P _ {1}) - w (P _ {2}) - w (P _ {3}) + w (P _ {4}) = w (P _ {5}) - w (P _ {6}) - w (P _ {7}) + w (P _ {8})
$$

and

$$
\phi (P _ {1}) - \phi (P _ {2}) - \phi (P _ {3}) - \phi (P _ {4}) = \phi (P _ {5}) - \phi (P _ {6}) - \phi (P _ {7}) + \phi (P _ {8}).
$$

(It is not particularly natural to divide the resulting 32 points into parallelograms – we do this merely to provide a link to the discussion so far.) It turns out that this follows automatically from Lemma 12.2. First we need a result similar to Lemma 9.2.

Lemma 12.3. Let$B \subset \mathbb { Z } _ { N } ^ { 2 }$and let$\phi : B \to \mathbb { Z } _ { N }$. Suppose that there are$\theta N ^ { 8 }$pairs of parallelograms$( P _ { 1 } , P _ { 2 } )$in B such that$h ( P _ { 1 } ) = h ( P _ { 2 } )$ $w ( P _ { 1 } ) = w ( P _ { 2 } )$and$\phi ( P _ { 1 } ) = \phi ( P _ { 2 } )$. Then there are at least$\theta ^ { 7 } N ^ { 3 2 }$sequences $( x _ { 1 } , \dots , x _ { 1 6 } , y _ { 1 } , \dots , y _ { 1 6 } , h )$such that

$$
x _ {1} + \dots + x _ {8} = x _ {9} + \dots + x _ {1 6}
$$

and

$$
\phi_ {h} (x _ {1}, y _ {1}) + \dots + \phi_ {h} (x _ {8}, y _ {8}) = \phi_ {h} (x _ {9}, y _ {9}) + \dots + \phi_ {h} (x _ {1 6}, y _ {1 6}),
$$

where$\phi _ { h } ( x , y )$stands for$\phi ( x , y + h ) - \phi ( x , y )$

Proof. Given$u \in \mathbb { Z } _ { N }$, define$g _ { u } ( x , y )$to be$\omega ^ { u \phi ( x , y ) } \mathrm { ~ i f ~ } ( x , y ) \in { \cal B }$, and zero otherwise. Let$\begin{array} { r } { f _ { u , h } ( x ) = \sum _ { u } g _ { u } ( x , y + h ) \overline { { g _ { u } ( x , y ) } } } \end{array}$. Adopting the convention that$\omega$raised to an undefined power is zero, we can write

$$
f _ {u, h} (x) = \sum_ {y} \omega^ {u (\phi (x, y + h) - \phi (x, y))}.
$$

Clearly,$| f _ { u , h } ( x ) | { \leqslant } N$for every$u , h , x .$, from which it follows that$\textstyle \sum _ { x } | f _ { u , h } ( x ) | ^ { 2 }$ $\leqslant N ^ { 3 }$for every$u , h$and therefore that$\begin{array} { r } { \sum _ { u , r } | \hat { f } _ { u , h } ( r ) | ^ { 2 } \leqslant N ^ { 5 } } \end{array}$for every h.

Next, we look at fourth powers. We have

$$
\sum_ {u, r} | \hat {f} _ {u, h} (r) | ^ {4} = \sum_ {u, r} \left| \sum_ {x, y} \omega^ {u (\phi (x, y + h) - \phi (x, y)) - r x} \right| ^ {4}
$$

which works out as$N ^ { 2 }$times the number of octuples$( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } , y _ { 1 } , y _ { 2 } , y _ { 3 } , y _ { 4 } )$ such that$x _ { 1 } - x _ { 2 } = x _ { 3 } - x _ { 4 }$(so that the sum over r is N rather than zero) and

$$
\phi_ {h} (x _ {1}, y _ {1}) - \phi_ {h} (x _ {2}, y _ {2}) = \phi_ {h} (x _ {3}, y _ {3}) - \phi_ {h} (x _ {4}, y _ {4}),
$$

where we take the equality to be false unless both sides are defined. In other words,$\textstyle \sum _ { u , r } | \hat { f } _ { u , h } ( r ) | ^ { 4 }$is$N ^ { 2 }$times the number of parallelogram pairs of height h with the same width and same value of$\phi$.

Finally, we look at sixteenth powers. It is not hard to check that $\begin{array} { r } { \sum _ { u , r } | \hat { f } _ { u , h } ( r ) | ^ { 1 6 } } \end{array}$counts$N ^ { 2 }$times the number of sequences$( x _ { 1 } , \ldots , x _ { 1 6 } .$ $y _ { 1 } , \ldots , y _ { 1 6 } )$such that

$$
x _ {1} + \dots + x _ {8} = x _ {9} + \dots + x _ {1 6}
$$

and

$$
\phi_ {h} \left(x _ {1}, y _ {1}\right) + \dots + \phi_ {h} \left(x _ {8}, y _ {8}\right) = \phi_ {h} \left(x _ {9}, y _ {9}\right) + \dots + \phi_ {h} \left(x _ {1 6}, y _ {1 6}\right).
$$

From our assumption and the above arguments, we know that $\begin{array} { r } { \sum _ { u , r , h } | \hat { f } _ { u , h } ( r ) | ^ { 2 } \leqslant N ^ { \bar { 6 } } } \end{array}$and$\begin{array} { r } { \sum _ { u , r , h } | \hat { f } _ { u , h } ( r ) | ^ { 4 } \geqslant \theta \bar { N } ^ { 1 0 } } \end{array}$. It follows from Lemma 9.1 that$\begin{array} { r } { \sum _ { u , r , h } | \hat { f } _ { u , h } ( r ) | ^ { 1 6 } \geqslant ( \theta N ^ { 1 0 } / N ^ { 3 6 / 7 } ) ^ { 7 } = \theta ^ { 7 } N ^ { 3 4 } } \end{array}$. Hence, the num-ber of sequences with the desired properties is at least$\theta ^ { 7 } N ^ { 3 2 }$, as stated. ✷

Next, we combine Lemmas 12.2 and 12.3 in the obvious way.

Lemma 12.4. Let$\beta , \gamma > 0$, let$f : \mathbb { Z } _ { N } \to D$, let$B \subset \mathbb { Z } _ { N } ^ { 2 }$be a set of cardinality$\beta N ^ { 2 }$and let$\phi : B \to \mathbb { Z } _ { N }$. Suppose that$| \Delta ( f ; k , \bar { l } ) \land ( \phi ( k , l ) ) | \geqslant$ $\gamma N$for every$( k , l ) \in B$. Then there are at least$\beta ^ { 1 1 2 } \gamma ^ { 3 3 6 } N ^ { 3 2 }$sequences $( x _ { 1 } , \dots , x _ { 1 6 } , y _ { 1 } , \dots , y _ { 1 6 } , h )$such that

$$
x _ {1} + \dots + x _ {8} = x _ {9} + \dots + x _ {1 6}
$$

and

$$
\phi_ {h} (x _ {1}, y _ {1}) + \dots + \phi_ {h} (x _ {8}, y _ {8}) = \phi_ {h} (x _ {9}, y _ {9}) + \dots + \phi_ {h} (x _ {1 6}, y _ {1 6}).
$$

Proof. Lemma 12.2 allows us to take$\theta = \beta ^ { 1 6 } \gamma ^ { 4 8 }$in Lemma 12.3.

Let us define a d-arrangement of height h to be a sequence of points $\left( ( x _ { 1 } , y _ { 1 } ) , ( x _ { 1 } , y _ { 1 } + h ) , ( x _ { 2 } , y _ { 2 } ) , ( x _ { 2 } , y _ { 2 } + h ) , \ldots , ( x _ { 2 d } , y _ { 2 d } ) , ( x _ { 2 d } , y _ { 2 d } + h ) \right)$such that$x _ { 1 } + \cdot \cdot \cdot + x _ { d } = x _ { d + 1 } + \cdot \cdot \cdot + x _ { 2 d }$. Given a set$B \subset \mathbb { Z } _ { N } ^ { 2 }$and a function $\phi : B \to \mathbb { Z } _ { N }$we shall say that$\phi$respects such a d-arrangement if

$$
\phi_ {h} \left(x _ {1}, y _ {1}\right) + \dots + \phi_ {h} \left(x _ {d}, y _ {d}\right) = \phi_ {h} \left(x _ {d + 1}, y _ {d + 1}\right) + \dots + \phi_ {h} \left(x _ {2 d}, y _ {2 d}\right).
$$

Of course, for this to happen, all the points of the d-arrangement must lie in the set$B .$, so that$\phi _ { h }$is defined where it needs to be. Our interest will be principally in 8-arrangements.

Lemma 12.4 gives us, under certain hypotheses on B and$\phi _ { ; }$, a large collection of 8-arrangements in the set$B$that are respected by$\phi .$. Indeed, since the total number of 8-arrangements cannot possibly exceed$\beta ^ { 1 5 } N ^ { 3 2 }$ if$| B | = \beta N ^ { 2 }$, it shows that the proportion of 8-arrangements respected by$\phi$is greater than zero (and independent of N). In the rest of this section, we shall show how to choose a large subset$B ^ { \prime } \subset B$such that $\phi$respects almost all of the 8-arrangements in$B ^ { \prime }$. As in$\ S 9$, when we restricted to an approximate homomorphism of order eight, this is done by a random selection with suitable dependences, with Riesz products to define the probabilities.

Lemma 12.5. Let$\eta > 0$, let$B \subset \mathbb { Z } _ { N } ^ { 2 }$be a set of size$\beta N ^ { 2 }$and let$\phi : \pentagon$ $B  \mathbb { Z } _ { N }$be a function that respects at least$\alpha \beta ^ { 1 5 } N ^ { 3 2 }$8-arrangements. If N is suficiently large (depending on$\beta$and$\eta )$then there is a subset $B ^ { \prime } \subset B$containing at least$( \bar { \alpha \eta } / 4 ) ^ { 2 ^ { 3 6 } } \beta ^ { 1 5 } \bar { N } ^ { 3 2 }$8-arrangements, such that the proportion of 8-arrangements respected by$\phi$is at least$1 - \eta$

Proof. Choose$r _ { 1 } , \dots , r _ { k } , \ s _ { 1 } , \dots , s _ { k } , \ t _ { 1 } , \dots , t _ { k } \in \mathbb { Z } _ { N }$uniformly and independently at random from$\mathbb { Z } _ { N }$. Having made the choice, let each point $( x , y ) \in B$be in$B ^ { \prime }$with probability

$$
p (x, y) = 2 ^ {- k} \prod_ {i = 1} ^ {k} \left(1 + \cos \frac {2 \pi}{N} \left(r _ {i} y + s _ {i} x y + t _ {i} \phi (x, y)\right)\right),
$$

and let these choices be independent. Note once again that this independence exists only after we condition on the choice of$r _ { 1 } , \ldots , r _ { k } , s _ { 1 } , \ldots , s _ { k }$2 $t _ { 1 } , \ldots , t _ { k }$: it is very important that in total there is a dependence. Now consider a sequence of points$( a _ { 1 } , b _ { 1 } ) , \dotsc , ( a _ { 3 2 } , b _ { 3 2 } )$. The probability that

they are all chosen is

$$
N ^ {- 3 k} \sum_ {r _ {1}, \ldots , r _ {k}} \sum_ {s _ {1}, \ldots , s _ {k}} \sum_ {t _ {1}, \ldots , t _ {k}} 2 ^ {- 3 2 k} \prod_ {i = 1} ^ {k} \prod_ {j = 1} ^ {3 2} \bigl (1 + \cos {\frac {2 \pi}{N}} (r _ {i} b _ {j} + s _ {i} a _ {j} b _ {j} + t _ {i} \phi (a _ {j}, b _ {j})) \bigr)
$$

which equals

$$
N ^ {- 3 k} 2 ^ {- 3 2 k} \left(\sum_ {r, s, t} 2 ^ {- 3 2} \prod_ {j = 1} ^ {3 2} \left(1 + 1 + \omega^ {r b _ {j} + s a _ {j} b _ {j} + t \phi (a _ {j}, b _ {j})} + \omega^ {- (r b _ {j} + s a _ {j} b _ {j} + t \phi (a _ {j}, b _ {j}))}\right)\right) ^ {k}.
$$

When the product over j is expanded, each term is of the form

$$
\omega^ {r} \sum \epsilon_ {j} b _ {j} + s \sum \epsilon_ {j} a _ {j} b _ {j} + t \sum \epsilon_ {j} \phi (a _ {j}, b _ {j}),
$$

where$\epsilon _ { 1 } , \ldots , \epsilon _ { 3 2 }$belong to the set$\{ - 1 , 0 , 1 \}$. Each such term, when summed over$r , s$and t, gives zero, unless

$$
\sum_ {j = 1} ^ {3 2} \epsilon_ {j} b _ {j} = \sum_ {j = 1} ^ {3 2} \epsilon_ {j} a _ {j} b _ {j} = \sum_ {j = 1} ^ {3 2} \epsilon_ {j} \phi (a _ {j}, b _ {j}) = 0,
$$

in which case it gives$N ^ { 3 }$

Now let us suppose that our sequence of points$( a _ { i } , b _ { i } )$forms an$8 -$ arrangement. Then we can write$a _ { 2 i - 1 } = a _ { 2 i } = x _ { i }$and$b _ { 2 i - 1 } = b _ { 2 i } - h = y _ { i }$ for some$( x _ { 1 } , \dots , x _ { 1 6 } , y _ { 1 } , \dots , y _ { 1 6 } , h )$such that$x _ { 1 } + \cdot \cdot \cdot + x _ { 8 } = x _ { 9 } + \cdot \cdot \cdot + x _ { 1 6 } .$ If$\epsilon _ { 1 } = 1$and$\epsilon _ { 2 } \neq - 1$and the corresponding term does not make a zero contribution, then$\epsilon _ { 1 } b _ { 1 } + \epsilon _ { 2 } b _ { 2 }$is either$y _ { 1 }$or$2 y _ { 1 } + h$and this must be zero. The number of choices of$( x _ { 1 } , \dots , x _ { 1 6 } , y _ { 1 } , \dots , y _ { 1 6 } , h )$for which this is true and$x _ { 1 } + \cdot \cdot \cdot + x _ { 8 } = x _ { 9 } + \cdot \cdot \cdot + x _ { 1 6 }$is at most$N ^ { 3 1 }$in each case. Repeating this argument for each$\epsilon _ { 2 i - 1 }$shows that the number of 8-arrangements making a non-zero contribution to a term where we do not have$\epsilon _ { 2 j - 1 } + \epsilon _ { 2 j } = 0$for every i is at most$3 2 N ^ { 3 1 }$

If$\epsilon _ { 2 j - 1 } + \epsilon _ { 2 j } = 0$for every$j ,$, then

$$
\sum_ {j = 1} ^ {3 2} \epsilon_ {j} a _ {j} b _ {j} = h (\epsilon_ {2} x _ {1} + \epsilon_ {4} x _ {2} + \dots + \epsilon_ {3 2} x _ {1 6}) .
$$

The number of 8-arrangements of height 0 is obviously at most$N ^ { 3 1 }$. Let $( \epsilon _ { 2 } , \epsilon _ { 4 } , \ldots , \epsilon _ { 3 2 } )$be a sequence which is not a multiple of the sequence $( 1 , \ldots , 1 , - 1 , \ldots , - 1 )$(where 1 and −1 each occur eight times). The number of 8-arrangements such that$\epsilon _ { 2 } x _ { 1 } + \epsilon _ { 4 } x _ { 2 } + \cdot \cdot \cdot + \epsilon _ { 3 2 } x _ { 1 6 } = 0$is at most $N ^ { 3 1 }$because we are imposing two independent linear conditions on the sequence$( x _ { 1 } , \dots , x _ { 1 6 } , y _ { 1 } , \dots , y _ { 1 6 } , h )$(in the vector space$\mathbb { Z } _ { N } ^ { 3 3 } )$. Hence, with the exception of at most$( 3 3 + 3 ^ { 1 6 } ) N ^ { 3 1 }$of them, an 8-arrangement makes a non-zero contribution to the sum only for sequences$\epsilon _ { 1 } , \ldots , \epsilon _ { 3 2 }$such that $\epsilon _ { 2 j - 1 } + \epsilon _ { 2 j } = 0$for every$j$, and$\epsilon _ { 2 } = \epsilon _ { 4 } = \cdot \cdot \cdot = \epsilon _ { 1 6 } = - \epsilon _ { 1 8 } = \cdot \cdot \cdot = - \epsilon _ { 3 2 }$ Moreover, the contribution will be zero unless$\begin{array} { r } { \sum _ { j = 1 } ^ { 3 2 } \epsilon _ { j } \phi ( a _ { j } , b _ { j } ) = 0 } \end{array}$. (This last statement follows from considering the sum over t.)

Our argument has shown that, ignoring at most$( 6 5 + 3 ^ { 1 6 } ) N ^ { 3 1 }$degenerate cases, given an 8-arrangement in$B ,$the probability that it lies in$B ^ { \prime }$ is$2 ^ { - 3 2 k } { \left( 2 ^ { - 3 2 } ( 2 ^ { 3 2 } + 2 ) \right) } ^ { k }$if$\phi$respects the 8-arrangement, but only$2 ^ { - 3 2 k }$if  it does not. Hence, our hypotheses imply that the expected number$X$of 8-arrangements respected by$\phi$is at least$2 ^ { - 3 2 k } ( 1 + 2 ^ { - 3 \overline { { 1 } } } ) ^ { k } \alpha \beta ^ { 1 5 } N ^ { 3 2 }$, and the expected number$Y$of bad but non-degenerate 8-arrangements is at most $2 ^ { - 3 2 k } \beta ^ { 1 5 } N ^ { 3 2 }$. Using the fact that$2 ^ { 2 ^ { - 3 1 } } \leqslant 1 + 2 ^ { - 3 1 }$, we can deduce that if $2 ^ { 2 ^ { - 3 1 } \dot { k } } \geqslant 2 / \alpha \eta$, then

$$
\eta \mathbb {E} X - \mathbb {E} Y \geqslant \alpha \eta (2 / \alpha \eta) 2 ^ {- 3 2 k} \beta^ {1 5} N ^ {3 2} - 2 ^ {- 3 2 k} \beta^ {1 5} N ^ {3 2} = 2 ^ {- 3 2 k} \beta^ {1 5} N ^ {3 2}
$$

Now$2 ^ { 2 ^ { - 3 1 } k } \geqslant ( 2 / \alpha \eta )$if and only if$2 ^ { - 3 2 k } \leqslant ( \alpha \eta / 2 ) ^ { 2 ^ { 3 6 } }$. Let k be an integer such that

$$
2 (\alpha \eta / 4) ^ {2 ^ {3 6}} \leqslant 2 ^ {- 6 4 k} \leqslant (\alpha \eta / 2) ^ {2 ^ {3 6}}.
$$

If N is large enough that$( \alpha \eta / 4 ) ^ { 2 ^ { 3 6 } } \beta ^ { 1 5 } N \geqslant 6 5 + 3 ^ { 1 6 }$, then the values for the above expectations and the upper estimate for the number of degenerate 8-arrangements imply that there exists a set$B ^ { \prime }$such that$\eta X \geqslant Y$and $X \geqslant ( \alpha \eta / 4 ) ^ { 2 ^ { 3 6 } } \beta ^ { 1 5 } \bar { N } ^ { 3 2 }$, as was claimed.✷

If we combine Lemmas 12.4 and 12.5 we obtain the main result of this section.

Lemma 12.6. Let$\beta , \gamma , \eta \ > \ 0$Let$f ~ : ~ \mathbb { Z } _ { N } \ \to \ D$, let$B \subset \mathbb { Z } _ { N } ^ { 2 }$be a set of cardinality at least$\beta N ^ { 2 }$and let$\phi ~ : ~ B ~ \to ~ \mathbb { Z } _ { N }$be such that $| \Delta ( f ; k , l ) ^ { \wedge } ( \phi ( k , l ) ) | \geqslant \gamma N$for every$( k , l ) \in B$. Then there is a subset $B ^ { \prime } \subset B$containing at least$2 ^ { - 2 ^ { 3 7 } } \beta ^ { 2 ^ { 4 3 } } \gamma ^ { 2 ^ { 4 5 } } \eta ^ { 2 ^ { 3 6 } } N ^ { 3 2 }$8-arrangements, such that the proportion of them respected by$\phi$is at least$1 - \eta$

Proof. By Lemma 12.4 there are at least$\beta ^ { 1 1 2 } \gamma ^ { 3 3 6 } N ^ { 3 2 }$8-arrangements respected by$\phi .$. This allows us to take$\alpha = \beta ^ { 9 7 } \gamma ^ { 3 3 6 }$in Lemma 12.5. It is not hard to check that$( \beta ^ { 9 7 } \gamma ^ { 3 3 6 } \eta / 4 ) ^ { 2 ^ { 3 6 } } \beta ^ { 1 5 } \geqslant 2 ^ { - 2 ^ { 3 7 } } \beta ^ { 2 ^ { 4 3 } } \gamma ^ { 2 ^ { 4 5 } } \eta ^ { 2 ^ { 3 6 } } N ^ { 3 2 }$, so the lemma is proved.✷

## 13 Finding a Bilinear Piece

We shall now use the results of the previous two sections to prove that if $A \subset \mathbb { Z } _ { N }$is a set with balanced function$f , B$is a large subset of$A$and $\phi : B \to \mathbb { Z } _ { N }$has the property that$\Delta ( f ; x , y ) ^ { \wedge } ( \phi ( x , y ) )$is large for every $( x , y ) \in B$, then$\phi$exhibits a small (but not too small) amount of bilinearity, in the following sense: there are arithmetic progressions$P , Q \subset \mathbb { Z } _ { N }$of size a power of N and with the same common diference, and a large subset C of$B \cap ( P \times Q )$such that the restriction of$\phi$to$C$is bilinear. This is the key to extending our proof from progressions of length four to progressions of length five.

What we prove in this section is suficient for finding progressions of length five, but not as strong as the corresponding case of the inductive hypothesis we shall need when generalizing the argument. Then it becomes necessary to show that almost all of the graph of$\phi$is contained in a small number of bilinear pieces, which is not a huge extra dificulty but it makes the argument look more complicated. Another way in which the argument of this section is slightly simpler than the argument for the general case (in §16) is that we can use Lemma 7.10 to allow us to assume that$\phi ( x , y )$is a homomorphism of order 8 in y for every fixed x and vice versa (see the proof of Theorem 13.10 for this).

The next lemma is another generalization of Proposition 6.1 with an almost identical proof. To recover the earlier proposition for the function $f : \mathbb { Z } _ { N } \to D$, apply this coming lemma to the function$g ( x , y ) = f ( x + y )$

Lemma 13.1. Let$f : \mathbb { Z } _ { N } ^ { 2 } \to D$be a function into the closed unit disc. For any h, define

$$
f _ {h} (x) = \sum_ {y} f (x, y + h) \overline {{f (x , y)}}.
$$

Let$B \subset \mathbb { Z } _ { N }$and let$\sigma : B  Z _ { N }$be a function such that

$$
\sum_ {h \in B} \left| \hat {f} _ {h} (\sigma (h)) \right| ^ {2} \geqslant \alpha N ^ {5}.
$$

Then there are at least$\alpha ^ { 4 } N ^ { 3 }$quadruples$( a , b , c , d ) \in B ^ { 4 }$such that$a + b =$ c + d and$\sigma ( a ) + \sigma ( b ) = \sigma ( c ) + \sigma ( d )$

Proof. Expanding what the hypothesis says, we find that

$$
\begin{array}{c} \sum_ {h \in B} | \hat {f} _ {h} (\sigma (h)) | ^ {2} = \sum_ {h \in B} \sum_ {x, x ^ {\prime}} f _ {h} (x) \overline {{f _ {h} (x ^ {\prime})}} \omega^ {- (x - x ^ {\prime}) \sigma (h)} \\ = \sum_ {h \in B} \sum_ {x, u} f _ {h} (x + u) \overline {{f _ {h} (x)}} \omega^ {- u \sigma (h)} \\ = \sum_ {h \in B} \sum_ {x, u} \sum_ {y, y ^ {\prime}} f (x + u, y ^ {\prime} + h) \overline {{f (x + u , y ^ {\prime}) f (x , y + h)}} f (x, y) \omega^ {- u \sigma (h)} \end{array}
$$

is at least$\alpha N ^ { 5 }$. It follows that

$$
\sum_ {x, u} \sum_ {y, y ^ {\prime}} \left| \sum_ {h \in B} f (x + u, y ^ {\prime} + h) \overline {{f (x , y + h)}} \omega^ {- u \sigma (h)} \right| \geqslant \alpha N ^ {5}
$$

which implies that

$$
\sum_ {x, u} \sum_ {y, y ^ {\prime}} \Big | \sum_ {h \in B} f (x + u, y ^ {\prime} + h) \overline {{f (x , y + h)}} \omega^ {- u \sigma (h)} \Big | ^ {2} \geqslant \alpha^ {2} N ^ {6}.
$$

For each triple${ t } = ( u , x , w )$, let$a _ { t } ( h ) = f ( x + u , w + h ) \overline { { f ( x , h ) } }$and$b _ { t } ( h ) =$ $B ( h ) \omega ^ { u \sigma ( h ) }$. Then we may rewrite the above inequality as

$$
\sum_ {t} \sum_ {y} \Big | \sum_ {h} a _ {t} (h + y) \overline {{b _ {t} (h)}} \Big | ^ {2} \geqslant \alpha^ {2} N ^ {6}.
$$

As in the proof of Proposition 12.1, we may apply Lemma 2.1 and the Cauchy-Schwarz inequality to deduce that

$$
\left(\sum_ {t} \sum_ {r} | \hat {a} _ {t} (r) | ^ {4}\right) \left(\sum_ {t} \sum_ {r} | \hat {b} _ {t} (r) |\right) ^ {4} \geqslant \alpha^ {4} N ^ {1 4}.
$$

Since$\begin{array} { r } { \sum _ { r } | \hat { a } _ { t } ( r ) | ^ { 4 } \leqslant N ^ { 4 } } \end{array}$for every t and$\begin{array} { r } { \hat { b } _ { t } ( r ) = \sum _ { h \in B } \omega ^ { u \sigma ( h ) - r h } } \end{array}$for every t and r, we then find that

$$
N ^ {2} \sum_ {u} \sum_ {r} \left| \sum_ {h \in B} \omega^ {u \sigma (h) - r h} \right| ^ {4} \geqslant \alpha^ {4} N ^ {7}.
$$

But the left-hand side is exactly$N ^ { 4 }$times the number of quadruples $( a , b , c , d )$that we wish to find.✷

In fact, we shall need the above lemma only in the special case of 01- valued functions. The next corollary is a restatement of the lemma in the language of §10.

Corollary 13.2. Let$A \ \subset \ \mathbb { Z } _ { N } ^ { 2 }$. For any$h \ \in \ \mathbb { Z } _ { N }$, define a domain $X _ { h } = X _ { h , 0 } \cup X _ { h , 1 } \cup \cdot \cdot \cdot \cup X _ { h , N - 1 }$by letting$X _ { h , x }$be the set of all pairs $( ( x , y ) , ( x , y + h ) )$, for which both$( x , y )$and$( x , y + h )$belong to A. Let$f _ { h } ( x )$ be the cardinality of$X _ { h , x } .$. Let$B \subset \mathbb { Z } _ { N }$and let$\sigma : B  \mathbb { Z } _ { N }$be any function such that$\begin{array} { r } { \sum _ { h \in B } | \hat { f } _ { h } ( \sigma ( h ) ) | ^ { 2 } \geqslant \alpha N ^ { 5 } } \end{array}$. Then there are at least$\alpha ^ { 4 } N ^ { 3 }$quadruples$( a , b , c , d ) \mathsf { \bar { \Psi } } \in B ^ { 4 }$such that$a + b = c + d$and$\sigma ( a ) + \sigma ( b ) = \sigma ( c ) + \sigma ( d )$

Proof. This follows immediately from Lemma 13.1 applied to the characteristic function of A.✷

Corollary 13.3. Let$A \subset \mathbb { Z } _ { N } ^ { 2 }$, and for$h \in \mathbb { Z } _ { N }$let$X _ { h }$and$f _ { h }$be as in Corollary 13.2. Let$\theta > 0$. Then there exist Freiman homomorphisms $\sigma _ { 1 } , \ldots , \sigma _ { q }$of order eight, defined on subsets$B _ { 1 } , \ldots , B _ { q }$of$\mathbb { Z } _ { N }$, and a set $G \subset \mathbb { Z } _ { N }$of cardinality at least$( 1 - \theta ) N$, such that whenever$h \in G$and $| \hat { f } _ { h } ( r ) | \geqslant \theta N ^ { 2 }$there exists$i \leqslant q$such that$r = \sigma _ { i } ( h )$The sets$B _ { i }$have cardinality at least$2 ^ { - 1 8 8 2 } \theta ^ { 1 0 4 7 7 } N$and$q \leqslant 2 ^ { 1 8 8 2 } \theta ^ { - 1 0 \dot { 4 } 7 9 }$

Proof. Suppose that$B \subset \mathbb { Z } _ { N }$is a set of size$\theta N$and that$\sigma : B  \mathbb { Z } _ { N }$is a function with the property that$| \hat { f } _ { h } ( \sigma ( h ) ) | \geqslant \theta N ^ { 2 }$for every$h \in B$. Then $\begin{array} { r } { \sum _ { h \in B } | \hat { f } _ { h } ( \sigma ( h ) ) | ^ { 2 } \geqslant \theta ^ { 3 } N ^ { 5 } } \end{array}$. Hence, by Corollary 13.2, B contains at least $\theta ^ { 1 2 } N ^ { 3 }$σ-additive quadruples. It follows from Corollary 7.6 (with$\alpha = \theta$and $\gamma = \theta ^ { 9 } )$that there is a subset C of B of cardinality at least$2 ^ { - 1 8 8 2 } \theta ^ { 1 0 4 7 7 } N$ such that the restriction of$\sigma$to C is a Freiman homomorphism of order eight.

Now let$\Gamma _ { 0 }$be the set of all pairs$( h , r )$such that$| \hat { f } _ { h } ( r ) | \geqslant \theta N ^ { 2 }$. If the projection of Γ to the h-axis has size less than$\theta N$, then we are done. Otherwise, we can choose B and σ satisfying the hypotheses of the previous paragraph and hence can find$B _ { 1 } \subset B$of cardinality at least$2 ^ { - 1 8 8 2 } \theta ^ { 1 0 4 7 7 } N$ such that the restriction of σ to$B _ { 1 }$is a homomorphism of order eight. Let $\sigma _ { 1 }$be this restriction and let$\Gamma _ { 1 } = \Gamma \setminus \{ ( h , \sigma _ { 1 } ( h ) ) : h \in B _ { 1 } \}$

If the projection of$\Gamma _ { 1 }$to the h-axis has cardinality less than$\theta N$, we are done. Otherwise, the above argument can be repeated. Continue the repetitions until it is no longer possible and we are then done. Now $\begin{array} { r } { \sum _ { h , r } | \bar { \hat { f } } _ { h } ( r ) | ^ { 2 } = N \sum _ { h , s } f _ { h } ( s ) ^ { 2 } } \end{array}$which is clearly at most$N ^ { 5 }$, so$\Gamma _ { 0 }$has car-dinality at most$\theta ^ { - 2 } N$. It follows that$q \leqslant 2 ^ { 1 8 8 2 } \theta ^ { - 1 0 4 7 9 }$as stated.✷

We shall now prove several lemmas under the same set of hypotheses, so it is convenient to state the hypotheses first and not keep repeating them. Let A be a subset of$\mathbb { Z } _ { N } ^ { 2 }$of cardinality$\alpha N ^ { 2 }$and let$\phi : A  \mathbb { Z } _ { N }$be a function with the following two properties. First,$\phi ( x , y )$is, for every fixed$x ,$, a homomorphism of order 8 in y and for every fixed y a homomorphism of order 8 in x. Second, the proportion of all 8-arrangements in A respected by$\phi$is at least$1 - \eta _ { \mathrm { : } }$where$\eta = 2 ^ { - 4 4 }$. (This second property states that $A$satisfies the conclusion of Lemma 12.6.) For each$h \in \mathbb { Z } _ { N }$, let us write $C ( h )$for the number of 8-arrangements in A of height h and$G ( h )$for the number of these 8-arrangements respected by$\phi .$. The domains$X _ { h }$and the functions$f _ { h }$are as defined in Corollary 13.2.

Lemma 13.4. Let$\theta > 0 , \theta _ { 1 } = 2 ^ { - 1 8 8 2 } \theta ^ { 1 0 4 7 7 } , q = 2 ^ { 1 8 8 2 } \theta ^ { - 1 0 4 7 9 }$and$m =$ $\lfloor ( \theta _ { 1 } / 6 4 \pi ) N ^ { \theta _ { 1 } ^ { 2 } / 1 6 q } \rfloor$. Then there exist an arithmetic progression$P$of length $m _ { 0 } \in \{ m - 1 , m \}$and a subset$H \subset P$such that

$$
\sum \left\{C (h): h \in H, G (h) \geqslant (1 - 2 \eta) C (h) \right\} \geqslant \alpha^ {3 2} N ^ {3 1} m _ {0} / 8,
$$

and there exist constants$a _ { 1 } , \ldots , a _ { q }$and$b _ { 1 } , \ldots , b _ { q }$such that, whenever$h \in$ H and$r \in \mathbb { Z } _ { N }$have the property that$| \hat { f } _ { h } ( r ) | \geqslant \theta N$, we have$r = a _ { i } h + b _ { i }$ for some$i \leqslant q$

Proof. Let G be the set and$\sigma _ { 1 } , \ldots , \sigma _ { q }$the Freiman homomorphisms of order 8 given by Corollary 13.3. For each$i \leqslant q$the homomorphism$\sigma _ { i }$is defined on a set$B _ { i }$of size at least$\theta _ { 1 } N$, so by Corollary 7.9 there exist a set$K _ { i }$of size at most$1 6 \theta _ { 1 } ^ { - 2 }$and some$c _ { i } \in \mathbb { Z } _ { N }$such that if m is a positive integer, d belongs to the Bohr neighbourhood$B ( K _ { i } , \theta _ { 1 } / 3 2 \pi m )$and$x , y \in B _ { i }$with $x - y = j d$for some$j$with$| j | \leqslant m$, then$\sigma _ { i } ( x ) - \sigma _ { i } ( y ) = c _ { i } ( x - y )$

By Lemma 7.7 and the definition of m we can find a non-zero d belonging to the Bohr neighbourhood

$$
\bigcap_ {i = 1} ^ {q} B \left(K _ {i}, \theta_ {1} / 3 2 \pi m\right) = B \left(\bigcup K _ {i}, \theta_ {1} / 3 2 \pi m\right).
$$

Let$d _ { 0 }$be such a value of$d ,$and partition$\mathbb { Z } _ { N }$into arithmetic progressions $P _ { 1 } , \dots , P _ { M }$such that each$P _ { j }$has common diference$d _ { 0 }$and the lengths of the$P _ { j }$are all equal to$m - 1$or m. By the way$d _ { 0 }$was chosen, the restriction of any$\sigma _ { i }$to any$P _ { j }$(or more correctly to$B _ { i } \cap P _ { j } )$is linear.

Our arithmetic progression$P$will be one of the progressions$P _ { j } ,$, chosen by an averaging argument. By our second assumption on$\phi ,$we know that

$$
\sum_ {h} G (h) \geqslant (1 - \eta) \sum_ {h} C (h),
$$

which implies that

$$
\sum \left\{C (h): G (h) \geqslant (1 - 2 \eta) C (h) \right\} \geqslant \frac {1}{2} \sum_ {h} C (h).
$$

This estimate says that at least half of the 8-arrangements in A have a height h for which the function$\phi _ { h }$is$\mathfrak { a } \ ( 1 - 2 \eta )$-homomorphism of order 8. We also know that$\begin{array} { r } { \sum _ { h \notin G } C ( h ) \ \leqslant \ \theta N ^ { 3 2 } } \end{array}$. Since the total number of 8-arrangements in A is$\begin{array} { r } { \sum _ { h } \overset { \vartriangle } { \boldsymbol { C } } ( h ) \geqslant \alpha ^ { 3 2 } N ^ { 3 2 } } \end{array}$, we can deduce that

$$
\sum \left\{C (h): h \in G, G (h) \geqslant (1 - 2 \eta) C (h) \right\} \geqslant \frac {1}{4} \sum_ {h} C (h).
$$

By averaging and the above estimate, we can choose some$j$such that

$$
\begin{array}{c} \sum \left\{C (h): G (h) \geqslant (1 - 2 \eta) C (h), h \in P _ {j} \cap G \right\} \geqslant \alpha^ {3 2} N ^ {3 1} (m - 1) / 4 \\ \geqslant \alpha^ {3 2} N ^ {3 1} m _ {0} / 8. \end{array}
$$

Let us set$P = P _ { j }$and$H = P _ { j } \cap G$. We know that each$\sigma _ { i }$, when restricted to$P ,$is linear. Therefore, we can find the constants$a _ { 1 } , \ldots , a _ { q }$and$b _ { 1 } , \ldots , b _ { q }$ required by the lemma.✷

This fact, that the set of large Fourier coeficients for each$\hat { f } _ { h }$“varies linearly” in$h ,$is the key to the whole argument. Our version of Bogolyubov’s argument in §10 tells us that$2 X _ { h } - 2 X _ { h }$is approximately d-invariant if $( a _ { i } h + b _ { i } ) d$is small for$1 \leqslant i \leqslant q$. Our next aim is to find a further partition of$P$into arithmetic progressions in each of which we can choose the same value of d with this property. The linearity of$a _ { i } h + b _ { i }$allows us to do so. It is to show this that we shall need the multiple recurrence result, Lemma 5.9.

Lemma 13.5. There exists an arithmetic progression$Q \subset P$of size$m _ { 1 } \geqslant$ $m _ { 0 } ^ { 1 / 2 ^ { 1 2 q } } / 2$and common diference$d ,$such that$| ( a _ { i } h + b _ { i } ) d | \leqslant m _ { 0 } ^ { - 1 / 2 ^ { 1 1 q } } .$N for every$i \leqslant q$. Moreover,$Q$can be chosen so that there are at least$\alpha ^ { 3 2 } m _ { 1 } / 2 0$ values of$h \in Q \cap H$for which$C ( h ) \geqslant \alpha ^ { 3 2 } N ^ { 3 1 } / 1 6$and$G ( h ) \geqslant ( 1 - 2 \eta ) C ( h )$

Proof. For each$i ,$let$\tau _ { i }$be the quadratic polynomial$a _ { i } h ^ { 2 } / 4 + b _ { i } h / 2$. The result is very simple if$m _ { 0 } < 2 ^ { 2 ^ { 1 2 q } }$, as then the only restriction on$m _ { 1 }$is that it should be at least 1. Otherwise, m satisfies the lower bound on r required in Lemma 5.9 when$k = 2$(and therefore$K = 2 ^ { 1 1 } )$. That lemma therefore tells us that$P$can be partitioned into arithmetic progressions$Q _ { 1 } , \ldots , Q _ { L }$ of sizes difering by one and at least$m _ { 0 } ^ { 1 / 2 ^ { 1 2 q } }$such that, for every i and$j ,$, the diameter of$\tau _ { i } ( Q _ { j } )$is at most$m _ { 0 } ^ { - 1 / 2 ^ { 1 1 q } } N$. By averaging, we can find one of these progressions, which we shall call$Q ^ { \prime }$, such that$| Q ^ { \prime } | = m _ { 1 } \geqslant c m _ { 0 } ^ { 1 / 2 ^ { 1 2 q } }$ and

$$
\sum \left\{C (h): h \in Q ^ {\prime} \cap H, G (h) \geqslant (1 - 2 \eta) C (h) \right\} \geqslant \alpha^ {3 2} N ^ {3 1} m _ {1} / 8.
$$

Let the common diference of$Q ^ { \prime }$be d. Choose any$h \in Q ^ { \prime }$which is not an end point. Then$\tau _ { i } ( h + d ) - \tau _ { i } ( h - d ) = ( a _ { i } h + b _ { i } ) d ,$, so the estimate on the diameter of$\tau _ { i } ( Q ^ { \prime } )$implies that$| ( a _ { i } h + b _ { i } ) d | \leqslant m _ { 0 } ^ { - 1 / 2 ^ { 1 1 q } } N$for every i. Now let$Q$be$Q ^ { \prime }$without the two end points.

By another averaging argument, there are at least$\alpha ^ { 3 2 } m _ { 1 } / 1 6$values of $h \in Q ^ { \prime } \cap$H such that$C ( h ) \geqslant \alpha ^ { 3 2 } N ^ { 3 1 } / 1 6$and$G ( h ) \geqslant ( 1 - 2 \eta ) C ( h )$. This certainly implies the slightly worse estimate for$Q$✷

It is vital for our later purposes that the common diference d of$Q$ should be the same as the d for which the numbers$( a _ { i } h + b _ { i } ) d$are all small. It was to achieve this that we needed to use quadratic recurrence and not just linear recurrence.

Let us define I to be the set of all$h \in Q \cap H$such that$C ( h ) \geqslant \alpha ^ { 3 2 } N ^ { 1 5 } / 1 6$ and$G ( h ) \geqslant ( 1 - 2 \eta ) C ( h )$. Notice that if$h \in I$then$\phi _ { h }$is a$( 1 - 2 \eta )$ homomorphism of order$8$on the domain$X _ { h }$. Lemma 13.5 asserts that I has cardinality at least$\alpha ^ { 3 2 } m _ { 1 } / 2 0$. For the next lemma, recall that a typical element of the domain$X _ { h }$, which was defined in the statement of Corollary 13.2, is a pair$v = ( ( x , y ) , ( x , y + h ) )$and that$r ( v )$is defined to be x.

Lemma 13.6. Let$k = 2 ^ { 1 1 4 } \alpha ^ { - 3 2 0 } , \zeta = 2 ^ { - 2 2 8 k } \alpha ^ { 5 7 6 k }$and$q = 2 ^ { 2 ^ { 2 0 } } \alpha ^ { - 2 ^ { 2 1 } }$. Then there is an arithmetic progression$R \subset \mathbb { Z } _ { N }$of size$m _ { 2 } \overset { \_ } { \geqslant } ( \zeta / 2 ) N ^ { 1 / 2 ^ { 1 3 q } }$and common diference d such that for every$h \in I$there is a subset$Y _ { h } \subset X _ { h }$of size at least$2 ^ { - 2 6 } \alpha ^ { 1 2 8 } N ^ { 2 }$such that the restriction of$\phi _ { h }$$\{ v \in Y _ { h } : r ( v ) \in$ $R \}$is linear. Moreover, R can be chosen such that

$$
\sum_ {h \in I} \left| \{v \in Y _ {h}: r (v) \in R \} \right| \geqslant 2 ^ {- 2 6} \alpha^ {1 2 8} m _ {2} N | I | \geqslant 2 ^ {- 3 1} \alpha^ {1 6 0} m _ {1} m _ {2} N.
$$

Proof. We know that$| X _ { h , r } | \leqslant N$for every$r .$. The lower bound on$C ( h )$ for each$h \in I$implies that$\begin{array} { r } { \left. X _ { h } \right. = \sum _ { r } \left. X _ { h , r } \right. \geqslant \alpha ^ { 3 2 } N ^ { 2 } / 1 6 } \end{array}$. We are about to apply Corollary 10.14, which uses the hypotheses of Theorem 10.13, to the domain$X _ { h }$. We may do so if we replace α in the statements of Theorem 10.13 and Corollary 10.14 by$\alpha ^ { 3 2 } / 1 6$. (Note that η was defined in this section to be$2 ^ { - 4 4 }$, so for$h \in I$the$( 1 - 2 \eta )$-homomorphism$\phi _ { h }$is a$( 1 - \eta )$-homomorphism in the sense of Theorem 10.13.) This allows us to take$\overset { \cdot } { \lambda } = 2 ^ { - 5 9 } \alpha ^ { 1 7 6 } , k = 2 ^ { 1 1 4 } \alpha$<sup>−320</sup> and$\zeta = 2 ^ { - 2 2 8 k } \alpha ^ { 5 7 6 k }$. Corollary 10.14 then states that if$K _ { h } = \{ r \in \mathbb { Z } _ { N } : | { \hat { f } } _ { h } ( r ) | \geqslant \lambda N \}$, then there exists a set $Y _ { h } \subset X _ { h }$of cardinality at least$( \alpha ^ { 3 2 } / 1 6 ) ^ { 3 } | \dot { X } _ { h } | / 1 0 0 0 \geqslant 2 ^ { - 2 6 } \alpha ^ { 1 2 8 } N ^ { 2 }$with the following property: for every positive integer m and every d in the Bohr neighbourhood$B ( K _ { h } , \zeta / m )$, there exists$c _ { h } \in \mathbb { Z } _ { N }$such that$\phi _ { h } ( v ) - \phi _ { h } ( w ) =$ $c _ { h } ( r ( v ) - r ( w ) )$whenever$v , w \in Y _ { h }$and$r ( v ) - r ( w ) \in \{ j d : - m \leqslant j \leqslant m \}$

Now, Lemmas 13.4 and 13.5 combined, with θ set equal to$\lambda .$tell us that the common diference d of the arithmetic progression Q satisfies the property that$| r d | \leqslant m _ { 0 } ^ { - 1 / 2 ^ { 1 1 q } } N$whenever$| \hat { f } _ { h } ( r ) | \geqslant \theta N$, where$q$may be taken to be the number in the statement of this lemma. In other words, we are told that this d belongs to all the Bohr neighbourhoods$B ( K _ { h } , \zeta / m )$2 provided that the inequality$m _ { 0 } ^ { - 1 / 2 ^ { 1 1 q } } \leqslant \zeta / m$holds, where$m _ { 0 }$is as given in the statement of Lemma 13.4. It is not hard to check that$m = ( \zeta / 2 ) N ^ { 1 / 2 ^ { 1 3 q } }$ satisfies the inequality. (In fact, we could replace 13 by 12, but it is convenient later for m<sub>2</sub> to be significantly less than$m _ { 1 } . )$

Since$m \ < \ N ^ { 1 / 2 }$, we can partition$\mathbb { Z } _ { N }$into arithmetic progressions $R _ { 1 } , \dots , R _ { L }$of common diference d and lengths m or m + 1. For every $R _ { i }$and for every$h \in I$the restriction of$\phi _ { h }$to$\{ v \in Y _ { h } : r ( v ) \in R _ { i } \}$is linear. Since$| Y _ { h } | \geqslant 2 ^ { - 2 6 } \alpha ^ { 1 2 8 } N ^ { 2 }$for every$h \in I$, we know that$\textstyle \sum _ { h \in I } | Y _ { h } | \geqslant$ $2 ^ { - 2 6 } \alpha ^ { 1 2 8 } N ^ { 2 } | \dot { I } |$. An averaging argument therefore gives us one of the$R _ { i }$ which we shall call$R ,$such that

$$
\sum_ {h \in I} \left| \{v \in Y _ {h}: r (v) \in R \} \right| \geqslant 2 ^ {- 2 6} \alpha^ {1 2 8} | I | m _ {2} N \geqslant 2 ^ {- 3 1} \alpha^ {1 6 0} m _ {1} m _ {2} N
$$

where$m _ { 2 }$equals either m or$m + 1$. This proves the lemma.

Lemma 13.7. There exist$y \in \mathbb { Z } _ { N }$, an arithmetic progression$S \subset R$of size $m _ { 3 } \geqslant m _ { 2 } ^ { 2 ^ { - 6 6 } \alpha ^ { 2 5 6 } }$and a set$B \subset S \times ( I + y )$of size at least$2 ^ { - 2 6 } \alpha ^ { 1 2 8 } m _ { 3 } | I | \geqslant$ $2 ^ { - 3 1 } \alpha ^ { 1 6 0 } m _ { 1 } m _ { 3 }$such that, for every$h \in I$, the restriction of$\phi ( x , y + h )$to B is linear in x.

Proof. Choose$y \in \mathbb { Z } _ { N }$uniformly at random. The expected number of pairs$x , h$such that$x \in R , \ h \ \in \ I$and$( ( x , y ) , ( x , y + h ) ) \ \in \ Y _ { h }$is at least$2 ^ { - 2 6 } \alpha ^ { 1 2 8 } m _ { 2 } | I |$, so let us fix a value of y such that there are at least this many. The number of$x \in R$such that$( x , y ) \in A$is then at least $2 ^ { - 2 6 } \alpha ^ { 1 2 8 } m _ { 2 }$. One of our main assumptions is that$\phi$is a homomorphism of order 8 for each fixed$y$. Hence, by Corollary 7.11, applied to the single set $\{ x \in R : ( x , y ) \in A \}$we can find a partition of R into arithmetic progressions$S _ { 1 } , \ldots , S _ { M }$all of length at least$m _ { 2 } ^ { 2 ^ { - 6 6 } \alpha ^ { 2 5 6 } }$such that the restriction of$x \mapsto \phi ( y , x )$to any$S _ { j }$is linear (where defined). By averaging, we can choose some$S _ { j }$, which we shall call$S ,$such that the number of pairs x, h with$x \in S , h \in I$and$( ( x , y ) , ( x , y + h ) ) \in Y _ { h }$is at least$2 ^ { - 2 6 } \alpha ^ { 1 2 8 } m _ { 3 } | I |$ where$m _ { 3 }$is the size of S.

Let$B \subset S \times ( I + y )$be the set of all points$( x , y + h )$such that$h \in I$ and$( ( x , y ) , ( x , y + h ) ) \in Y _ { h }$. We have shown that B has cardinality at least $2 ^ { - 2 6 } \alpha ^ { 1 2 8 } m _ { 3 } | I | \geqslant 2 ^ { - 3 1 } \alpha ^ { 1 6 0 } m _ { 1 } m _ { 3 }$and found constants c and$c _ { h } \ ( h \in I )$, such that, for any$x _ { 1 } , x _ { 2 } \in S$and any$h \in I$

$$
\phi (x _ {1}, y) - \phi (x _ {2}, y) = c (x _ {1} - x _ {2})
$$

and

$$
\phi (x _ {1}, y + h) - \phi (x _ {1}, y) - \phi (x _ {2}, y + h) + \phi (x _ {2}, y) = c _ {h} (x _ {1} - x _ {2}).
$$

It follows that, for every$h \in I$

$$
\phi (x _ {1}, y + h) - \phi (x _ {2}, y + h) = (c _ {h} - c) (x _ {1} - x _ {2}),
$$

which tells us that the restrictions of$\phi$to the rows of B are all linear. ✷

We have now efectively reduced the dimension of our problem by one, as the next two lemmas will demonstrate. For each$h \in H$, let$a ( h )$and $c ( h )$be the unique constants such that$\phi ( x , y + h ) = a ( h ) + c ( h ) x$for every x with$( x , y + h ) \in B$

Lemma 13.8. Assume that m$\geqslant 2 ^ { 8 4 } \alpha ^ { - 4 1 6 }$. Then there is a subset$J \subset I$ such that the map$h \mapsto ( a ( h ) , c ( h ) )$is a homomorphism of order 8 on J and the set C of$( x , y + h ) \in B$such that$h \in J$has cardinality at least $2 ^ { - 8 4 } \alpha ^ { 4 1 6 } m _ { 1 } m _ { 3 }$

Proof. We know that B has size at least$\begin{array} { r l } { 2 ^ { - 3 1 } \alpha ^ { 1 6 0 } m _ { 1 } m _ { 3 } } & { { } = } \end{array}$ $2 ^ { - 3 1 } \alpha ^ { 1 6 0 } m _ { 1 } m _ { 3 } | S | | Q + y |$. We also know (from our main assumption) that $\phi ( x , y + h )$is a homomorphism of order 8 in$h$for every fixed x. Suppose that$x _ { 1 } , \ x _ { 2 }$and$h ( 1 ) , \ldots , h ( 1 6 )$are such that$( x _ { i } , y + h ( j ) ) \in B$for every $i , j$. Because$\phi ( x , y + h )$is a homomorphism of order 8 in$h ,$, easy linear algebra shows that

$$
a _ {h (1)} + \dots + a _ {h (8)} = a _ {h (9)} + \dots + a _ {h (1 6)}
$$

and

$$
c _ {h (1)} + \dots + c _ {h (8)} = c _ {h (9)} + \dots + c _ {h (1 6)}.
$$

For any pair$( x _ { 1 } , x _ { 2 } ) \in S ^ { 2 }$let$J ( x _ { 1 } , x _ { 2 } )$be the set of all$h \in I$such that$( x _ { 1 } , y + h )$and$( x _ { 2 } , y + h )$are in$B ,$, and let$C ( x _ { 1 } , x _ { 2 } )$be the set of all $( x , y + h ) \in B$such that$h \in J ( x _ { 1 } , x _ { 2 } )$. We shall choose J to be one of the $J ( x _ { 1 } , x _ { 2 } )$and for that we need the corresponding set$C ( x _ { 1 } , x _ { 2 } )$to be large, which (needless to say) we do by averaging.

Notice first that$\begin{array} { r } { \sum _ { x _ { 1 } , x _ { 2 } } | C ( x _ { 1 } , x _ { 2 } ) | } \end{array}$counts all quadruples$( x _ { 1 } , x _ { 2 } , x _ { 3 } , h ) \in$ $S ^ { 3 } \times I$such that$( x _ { i } , y + h ) \in B$for$i = { 1 , 2 , 3 }$. Therefore, letting$D _ { h } =$ $\{ x \in S : ( x , y + h ) \in B \}$, we can write this sum as$\textstyle \sum _ { h \in I } | D _ { h } | ^ { 3 }$. Since $\begin{array} { r } { \sum _ { h \in I } \left| D _ { h } \right| = \left| B \right| } \end{array}$, this is at least$| I | ^ { - 2 } | B | ^ { 3 }$, which our earlier estimates tell us is at least$2 ^ { - 8 3 } \alpha ^ { 4 1 6 } m _ { 1 } m _ { 3 } ^ { 3 }$The contribution to the sum from sets $C ( x _ { 1 } , x _ { 2 } )$such that$x _ { 1 } = x _ { 2 }$is certainly no more than$m _ { 1 } m _ { 3 } ^ { 2 }$, which, by our assumed lower bound for$m _ { 3 } ,$is at most half the total. Therefore, there exist$x _ { 1 } \neq x _ { 2 }$such that$C ( x _ { 1 } , x _ { 2 } )$has cardinality at least$2 ^ { - 8 4 } \alpha ^ { 4 1 6 } m _ { 1 } m _ { 3 }$

We have shown that the map$h \mapsto \left( a _ { h } , c _ { h } \right)$is a homomorphism of order 8 from$J = J ( x _ { 1 } , x _ { 2 } )$to$\mathbb { Z } _ { N } ^ { 2 }$, so we may set$J = J ( x _ { 1 } , x _ { 2 } )$and the lemma is proved.✷

At this point let us recall that the arithmetic progression$S$is a subset of$R ,$which has the same common diference d as$Q .$. Moreover, we fixed our numbers so that R would be considerably smaller than$Q .$It follows that $S$is a subset of a translate of$Q$and, writing$d _ { 1 }$for the common diference of$S _ { i }$, that$d _ { 1 }$is a multiple of d. Recall also that the cardinalities of$S$and $Q$are$m _ { 3 }$and$m _ { 1 }$respectively and that J is a subset of$Q$

Lemma 13.9. There exists an arithmetic progression$U \subset Q$of common diference$d _ { 2 }$, which is a multiple of$\mathbf { \Phi } _ { d _ { 1 } }$, and size$m _ { 4 } \geqslant m _ { 3 } ^ { 2 ^ { - 1 8 2 } \bar { \alpha } ^ { 8 3 2 } }$such that the set D of all$( x , y + h ) \in C$such that$h \in U \cap J$has cardinality at least$2 ^ { - 8 4 } \alpha ^ { 4 1 6 } m _ { 3 } m _ { 4 } = 2 ^ { - \dot { 8 } 4 } \alpha ^ { 4 1 6 } | S | | U + y |$and the restriction of$\phi$to D is bilinear.

Proof. Let us partition$Q$into maximal subprogressions$T _ { 1 } , \dots , T _ { M }$of common diference$d _ { 1 }$. By the remarks immediately preceding the statement of this lemma, each$T _ { i }$has cardinality at least$m _ { 3 }$. By averaging, we can choose$T = T _ { j }$such that the set of all$( x , y + h ) \in C$with$h \in J \cap T$has cardinality at least$2 ^ { - 8 4 } \alpha ^ { 4 1 6 } m _ { 3 } | T |$. Applying Corollary 7.11 to the homomorphism$h \mapsto ( a ( h ) , c ( h ) )$restricted to$J { \cap T }$, with α replaced by$2 ^ { - 8 4 } \alpha ^ { 4 1 6 }$，we obtain a partition of$T$into arithmetic progressions$U _ { 1 } , \dots , U _ { L }$of size at least$| T | ^ { 2 ^ { - \mathbf { \hat { 1 } 8 2 } } \alpha ^ { 8 3 2 } }$such that the restriction of the map$h \mapsto ( a ( h ) , c ( h ) )$to any$U _ { i }$is linear. By averaging again we may choose$U = U _ { i }$of cardinality $m _ { 4 }$such that the set D defined in the statement has the required size. Then because the coeficients$a ( h )$and$c ( h )$vary linearly in h when$h \in U \cap J ,$ the restriction of$\phi$to D is bilinear.✷

Corollary 13.10. There exist arithmetic progressions V and W with the same common diference and same cardinality$m _ { 5 } \geqslant m _ { 4 } ^ { 1 / 2 } - 1$, and a subset $E \subset V \times W$of size at least$2 ^ { - 8 6 } \alpha ^ { 4 1 6 } | V | | W |$, such that the restriction of$\phi$ to$E$is bilinear.

Proof. We already have a comparable statement for$S \times ( U + y )$. The common diference of$S$is$d _ { 1 }$and the common diference of$U + y$is$d _ { 2 }$ which is a multiple of$d _ { 1 }$. All we do now is apply one further averaging argument to pass to subprogressions of the same size and same common diference.

Since U is a subset of a translate of$S ,$, a maximal subprogression of$S$ with common diference$d _ { 2 }$has cardinality at least$m _ { 4 } - 1$. It is therefore not hard to show that$S \times ( U + y )$can be partitioned into sets of the form$V \times W$，where$V$and$W$are arithmetic progressions with common diference$d _ { 2 }$and size m or$m + 1$, where$m \geqslant m _ { 4 } ^ { 1 / 2 } - 1$. By an averaging argument we can choose one of these sets$V \times W$such that$D \cap ( V \times W ) \geqslant 2 ^ { - 8 4 } \alpha ^ { 4 1 6 } | V | | W |$ The slightly worse bound in the lemma comes from the fact that we may wish to remove end-points from$V$and W to make them the same size. ✷

Let us now show that we can achieve the hypotheses that we have been assuming in the last few lemmas.

Lemma 13.11. Let$f : \mathbb { Z } _ { N } \to D$be a function which fails to be cubically α-uniform. Then there exists a set$A \subset \mathbb { Z } _ { N } ^ { 2 }$of size at least$( \alpha / 2 ) ^ { 2 ^ { 6 6 } } N ^ { 2 }$and a function$\phi : A  \mathbb { Z } _ { N }$such that, for every fixed$x , \phi ( x , y )$is a Freiman homomorphism of order 8 in y, for every fixed y it is a homomorphism of order 8 in x, the proportion of all 8-arrangements in A respected by$\phi$is at least$1 - 2 ^ { - 7 3 }$and$| \Delta ( f ; k , l ) \rangle \langle \phi ( k , l ) ) | \geqslant \alpha N / 2$for every$( k , l ) \in A$

Proof. By Lemma 3.1 (the easy implication of (ii) from$\left( \mathrm { v i } \right) )$there is a set$A _ { 0 } \subset \mathbb { Z } _ { N } ^ { 2 }$of size at least$\alpha N ^ { 2 } / 2$and a function$\phi : A _ { 0 } \to \mathbb { Z } _ { N }$such that$| \Delta ( f ; k , l ) \land ( \phi ( k , l ) ) | \ \geqslant \ \alpha N / 2$for every$( k , l ) \in A _ { 0 }$. For each$k ,$let $A _ { 0 , k }$be the cross-section$\{ l : ( k , l ) \in A _ { 0 } \}$, let$| A _ { 0 , k } | = \alpha _ { k } N$and define $\phi _ { k } : A _ { 0 , k } \to \mathbb { Z } _ { N }$by$\phi _ { k } ( l ) = \phi ( k , l )$

Fixing k and applying Proposition 6.1 to the functions$\Delta ( f ; k ) : \mathbb { Z } _ { N } \longrightarrow$ $D$and$\phi _ { k } : A _ { 0 , k } \to \mathbb { Z } _ { N }$, we find that there are at least$\alpha _ { k } ^ { 4 } N ^ { 3 } \ \phi _ { k }$-additive quadruples in$A _ { 0 , k }$. Applying Corollary 7.6 with$B _ { 0 } = A _ { 0 , k } , \phi = \phi _ { k }$and $\alpha = \gamma = \alpha _ { k }$, we obtain a subset$A _ { 1 , k } \subset A _ { 0 , k }$of size at least$2 ^ { - 1 8 8 2 } \alpha _ { k } ^ { 1 1 6 5 } N$ such that the restriction of$\phi _ { k }$to$A _ { 1 , k }$is a Freiman homomorphism of order 8. Since the average of$\alpha _ { k }$is at least$\alpha / 2$, the union of the sets$A _ { 1 , k }$is a set$A _ { 1 }$of cardinality$\zeta N ^ { 2 }$, where$\zeta \geqslant 2 ^ { ' 1 8 8 2 } ( \alpha / 2 ) ^ { 1 1 6 5 } = 2 ^ { - 3 0 4 7 } \alpha ^ { 1 1 6 5 }$. The restriction of$\phi ( k , l )$to$A _ { 1 }$is a homomorphism of order 8 in l for any fixed k.

Repeating this argument for the second variable, we can pass to a further subset$A _ { 2 } \subset A _ { 1 }$of cardinality at least$2 ^ { - 3 0 4 7 } \zeta ^ { 1 1 6 5 } N ^ { 2 } \geqslant ( \mathsf { \bar { \alpha } } / 2 ) ^ { 2 2 2 } N ^ { 2 }$such that the restriction of$\phi$to$A _ { 2 }$is a homomorphism of order 8 in each variable separately. Let$\beta = ( \alpha / 2 ) ^ { 2 ^ { 2 2 } }$

We now apply Lemma 12.6 with$B = A _ { 2 } , \gamma = \alpha / 2$and$\eta = 2 ^ { - 4 4 }$. This yields a set A with at least

$$
2 ^ {- 2 ^ {3 7}} \beta^ {2 ^ {4 3}} \gamma^ {2 ^ {4 5}} \eta^ {2 ^ {3 6}} N ^ {3 2} \geqslant (\alpha / 2) ^ {2 ^ {6 6}} N ^ {3 2}
$$

8-arrangements, such that the proportion respected by φ is at least$1 - 2 ^ { - 4 4 }$ Since the cardinality of such a set must be at least$( \dot { \alpha } / 2 ) ^ { 2 ^ { 6 6 } } N ^ { 2 }$, the lemma is proved.✷

We are now ready for the main result of this section.

Theorem 13.12. Let f be a function from$\mathbb { Z } _ { N }$to the closed unit disc. If f is not cubically α-uniform then there exist arithmetic progressions$P$ and$Q$of size at least$N ^ { ( 1 / 2 ) ^ { ( 1 / \alpha ) ^ { 2 ^ { 7 0 } } } }$and with the same common diference, a subset$B \subset P \times Q$of size at least$( \alpha / 2 ) ^ { 2 ^ { 7 6 } } | P | | Q |$and a bilinear function $\phi : P \times Q \to \mathbb { Z } _ { N }$, such that$\Delta ( f ; k , l ) ^ { \wedge } ( \phi ( k , l ) ) \geqslant$α${ } _ { N / 2 }$for every$( k , l ) \in B$ Proof. By Lemma 13.11 we can find a set$A \subset \mathbb { Z } _ { N } ^ { 2 }$of size at least$( \alpha / 2 ) ^ { 2 ^ { 6 6 } } N ^ { 2 }$ and a function$\phi : A  \mathbb { Z } _ { N }$such that, for every fixed$x , \phi ( x , y )$is a Freiman homomorphism of order 8 in$y .$for every fixed$y$it is a homomorphism of order 8 in$x ,$the proportion of all 8-arrangements in$A$respected by φ is at least$1 - 2 ^ { - 4 4 }$and$| \Delta ( f ; k , l ) \rangle ( \phi ( k , l ) ) | \geqslant \alpha N / 2$for every$( k , l ) \in A$. Apart from the last condition, these are the hypotheses stated just before Lemma 13.4, except that α has been replaced by$( \alpha / 2 ) ^ { 2 ^ { 6 6 } }$. The results numbered 13.4 to 13.10 all hold under this set of hypotheses, so the theorem follows from Corollary 13.10 and a back-of-envelope estimate for$m _ { 5 }$when$\alpha$is replaced by$( \dot { \alpha } / 2 ) ^ { 2 ^ { 6 6 } }$✷

Notice the relationship between the above theorem and Freiman’s theorem. The hypotheses are somewhat diferent, but all we have used is that there are many 8-arrangements respected by φ, which is a fairly natural generalization of the hypotheses of the Balog-Szemer´edi theorem to graphs of functions in two variables. The conclusion of the theorem is in some ways much weaker, since we find only a very small set with good structure. On the other hand, the structure obtained is stronger, as we have gone up from linearity to bilinearity. It is very likely that a development of the argument above could be used to give a complete description of functions $\phi : \mathbb { Z } _ { N } ^ { 2 } \to \mathbb { Z } _ { N }$that respect many 8-arrangements. This would deserve to be called a bilinear Freiman (or Balog-Szemer´edi) theorem. Theorem 13.12 one could perhaps call a weak bilinear Freiman theorem.

The next three sections will generalize the above theorem from non-cubically uniform functions to functions that fail to be uniform of degree k, producing an appropriate (k − 1)-linear piece. The generalization is long, but does not involve any significant new ideas. The reader who wishes to follow a proof of Szemer´edi’s theorem for progressions of length five can go straight to §17.

## 14 Obtaining Many Respected Arrangements

This section and the next consist of relatively routine generalizations of the results of §12 to functions of k variables. The reason we are presenting them separately is that the argument for two variables is notationally simpler and therefore easier to understand, while containing all the essential ideas.

We begin with a result which, in both its statement and its proof, is very similar to Proposition 12.1, but which seems to be hard to unify with that result. Recall that if$f : \mathbb { Z } _ { N } ^ { 2 } \to \mathbb { C }$, then$f _ { h } ( y )$is defined as$\textstyle \sum _ { x } f ( x +$ $h , y ) { \overline { { f ( x , y ) } } }$

Proposition 14.1. For each$h \in \mathbb { Z } _ { N }$let$\lambda _ { h } \geqslant 0$. Let$f ^ { ( 1 ) } , \ldots , f ^ { ( p ) }$be functions from$\mathbb { Z } _ { N } ^ { 2 }$to the closed unit disc D and let$\sigma _ { 1 } , \ldots , \sigma _ { p }$be functions from$\mathbb { Z } _ { N }$to$\mathbb { Z } _ { N }$such that

$$
\sum_ {h} \lambda_ {h} \prod_ {i = 1} ^ {p} \left| \hat {f} _ {h} ^ {(i)} (\sigma_ {i} (h)) \right| ^ {2} \geqslant \alpha N ^ {4 p + 1}.
$$

Then the sum of$\lambda _ { a } \lambda _ { b } \lambda _ { c } \lambda _ { d }$over all quadruples$( a , b , c , d )$such that$a + b =$ $c + d$and$\sigma _ { i } ( a ) + \sigma _ { i } ( b ) = \sigma _ { i } ( c ) + \sigma _ { i } ( d )$for every i is at least$\alpha ^ { 4 } N ^ { 3 }$

Proof. In the argument to follow, we shall often abbreviate$( x _ { 1 } , \ldots , x _ { p } )$by x, and similarly for other sequences of length$p .$. The left-hand side of the inequality we are assuming is, when written out in full,

$$
\begin{array}{r l} \sum_ {h} \lambda_ {h} \sum_ {x, w, y, z} \prod_ {i = 1} ^ {p} f ^ {(i)} (x _ {i} + h, y _ {i}) \overline {{f ^ {(i)} (x _ {i} , y _ {i}) f ^ {(i)} (w _ {i} + h , z _ {i})}} \\ & \cdot f ^ {(i)} (w _ {i}, z _ {i}) \omega^ {- \sigma_ {i} (h) (y _ {i} - z _ {i})}. \end{array}
$$

Substituting$u _ { i } = y _ { i } - z _ { i }$, this becomes

$$
\sum_ {h} \lambda_ {h} \sum_ {x, w, u, z} \prod_ {i = 1} ^ {p} f ^ {(i)} (x _ {i} + h, z _ {i} + u _ {i}) \overline {{f ^ {(i)} (x _ {i} , z _ {i} + u _ {i}) f ^ {(i)} (w _ {i} + h , z _ {i})}}
$$

Since this exceeds$\alpha N ^ { 4 p + 1 }$and$| f ^ { ( i ) } ( x , y ) | \ \leqslant \ 1$for every$i , x , y$we may deduce that

$$
\sum_ {x, w, u, z} \left| \sum_ {h} \lambda_ {h} \prod_ {i = 1} ^ {p} f ^ {(i)} (x _ {i} + h, z _ {i} + u _ {i}) \overline {{f ^ {(i)} (w _ {i} + h , z _ {i})}} \omega^ {- u _ {i} \sigma_ {i} (h)} \right| \geqslant \alpha N ^ {4 p + 1}
$$

and hence, by the Cauchy-Schwarz inequality, that

$$
\sum_ {x, w, u, z} \left| \sum_ {h} \lambda_ {h} \prod_ {i = 1} ^ {p} f ^ {(i)} (x _ {i} + h, z _ {i} + u _ {i}) \overline {{f ^ {(i)} (w _ {i} + h , z _ {i})}} \omega^ {- u _ {i} \sigma_ {i} (h)} \right| ^ {2} \geqslant \alpha^ {2} N ^ {4 p + 2}.
$$

We now introduce a variable s and write$x _ { i } = s + x _ { i } ^ { \prime }$and$w _ { i } = s + w _ { i } ^ { \prime } .$. From the above, we can deduce that

$$
\sum_ {s} \sum_ {x ^ {\prime}, w ^ {\prime}, u, z} \Big | \sum_ {h} \lambda_ {h} \prod_ {i = 1} ^ {p} f ^ {(i)} (s + x _ {i} ^ {\prime} + h, z _ {i} + u _ {i}) \overline {{f ^ {(i)} (s + w _ {i} ^ {\prime} + h , z _ {i})}} \omega^ {- u _ {i} \sigma_ {i} (h)} \Big | ^ {2}
$$

$$
\geqslant \alpha^ {2} N ^ {4 p + 3}.
$$

Applying Lemma 2.1 and the Cauchy-Schwarz inequality in the usual way (see for example the proof of Proposition 12.1) we deduce that

$$
\sum_ {r} \sum_ {x ^ {\prime}, w ^ {\prime}, u, z} \left| \sum_ {h} \lambda_ {h} \prod_ {i = 1} ^ {p} \omega^ {\sigma_ {i} (h) u _ {i} - r h} \right| ^ {4} \geqslant \alpha^ {4} N ^ {4 p + 4}.
$$

Since the left-hand side above is$N ^ { 4 p + 1 }$times the sum of$\lambda _ { a } \lambda _ { b } \lambda _ { c } \lambda _ { d }$over all quadruples$( a , b , c , d )$such that$a + b = c + d$and$\sigma _ { i } ( a ) + \sigma _ { i } ( b ) = \sigma _ { i } ( c ) + \sigma _ { i } ( d )$ for every$i ,$the result is proved.✷

In the next section, we shall need to deal with functions defined on sets$B \subset \mathbb { Z } _ { N } ^ { k }$which will be k-dimensional generalizations of the somewhat additive functions that appeared in$\ S 6$. They arise in two diferent ways, but in both cases they have a property which we shall call the product property. To define this, suppose that B is a subset of$\mathbb { Z } _ { N } ^ { k }$and that$\phi : B \to \mathbb { Z } _ { N }$ Given any$j \leqslant k$and any$y \in \mathbb { Z } _ { N } ^ { k }$, define$B ( y , j )$to be the set of all$x \in B$ such that$x _ { i } = y _ { i }$whenever$i \neq j$. This is the one-dimensional cross-section of B that goes through$y$in the j-direction. Now define$C ( y , j )$to be the set of all$x \in \mathbb { Z } _ { N }$such that$( y _ { 1 } , \dots , y _ { j - 1 } , x , y _ { j + 1 } , \dots , y _ { k } ) \in B ( y , j )$, and define a function$\phi _ { y , j } : C ( y , j ) \longrightarrow \mathbb { Z } _ { N }$by

$$
\phi_ {y, j} (x) = \phi \left(y _ {1}, \dots , y _ {j - 1}, x, y _ {j + 1}, \dots , y _ {k}\right).
$$

This is the restriction of$\phi$to$B ( y , j )$, but for convenience regarded as a function defined on a subset of$\mathbb { Z } _ { N }$. Let us define a j-restriction of$\phi$to be any function of the form$\phi _ { y , j }$for some$y \in \mathbb { Z } _ { N } ^ { k }$. We shall say that$\phi$ has the product property with parameter$\gamma \ { \mathrm { i f } } ,$whenever$j \leqslant k , \psi _ { 1 } , \ldots , \psi _ { p }$ are j-restrictions of$\phi , E$is a subset of$\mathbb { Z } _ { N }$on which all the$\psi _ { i }$are defined and$\theta : E \to \mathbb { R } _ { + }$, the sum of$\theta ( a ) \theta ( b ) \theta ( c ) \theta ( d )$over all additive quadruples $( a , b , c , d )$that are$\psi _ { i } .$-additive for every i is at least$\gamma ^ { 8 p } N ^ { - 1 } \bigl ( \sum _ { x } \theta ( x ) \bigr ) ^ { 4 }$

Lemma 14.2. Let$f : \mathbb { Z } _ { N } \to D$, let$B \subset \mathbb { Z } _ { N } ^ { k }$and let$\phi : B \to \mathbb { Z } _ { N }$be such that$| \Delta ( f ; r _ { 1 } , \ldots , r _ { k } ) ^ { \sim } ( \phi ( r _ { 1 } , \ldots , r _ { k } ) ) | \geqslant \gamma N$for every$( r _ { 1 } , \dots , r _ { k } ) \in B$ Then$\phi$has the product property with parameter$\gamma$.

Proof. Let$y _ { 1 } , \ldots , y _ { p }$be elements of$\mathbb { Z } _ { N } ^ { k - 1 }$and let E be the set of all$r \in$ $\mathbb { Z } _ { N }$such that$( y _ { i } , r ) \in B$for every i. Then if we are given a function $\theta : E \to \mathbb { R } _ { + }$, we can set$\theta ( k ) = 0$for k /∈ E and apply Proposition 12.1 to the functions$f _ { i } = \Delta ( f ; y _ { i } )$. Since$\Delta ( f _ { i } ; r ) = \Delta ( f ; ( y _ { i } , r ) )$these functions satisfy the hypothesis of Lemma 12.1 with$\begin{array} { r } { \alpha = \gamma ^ { 2 p } \sum _ { k } \theta ( k ) N ^ { - 1 } } \end{array}$and$\sigma _ { i } ( r ) =$ $\phi ( y _ { i } , r )$. The conclusion of the lemma then gives us exactly what we want, at least for k-restrictions. By symmetry, the result is true for the other j-restrictions as well, and$\phi$has the product property with parameter γ. ✷

The second case in which we wish to deduce the product property is similar to the first, but we shall use Proposition 14.1 instead of Proposition 12.1. Given a function$f : \mathbb { Z } _ { N } ^ { k + 1 } \to \mathbb { C }$and$h = ( h _ { 1 } , \ldots , h _ { k } ) \in \mathbb { Z } _ { N } ^ { k }$, define a function$f _ { h } : \mathbb { Z } _ { N } \to \mathbb { C }$by

$$
f _ {h} (y) = \sum_ {x \in \mathbb {Z} _ {N} ^ {k}} \prod_ {\epsilon \in \{0, 1 \} ^ {k}} C ^ {| \epsilon | + k} f (x _ {1} + \epsilon_ {1} h _ {1}, \dots , x _ {k} + \epsilon_ {k} h _ {k}, y),
$$

where once again$C$stands for complex conjugation and$| \epsilon | = \sum \epsilon _ { i }$. For example when$k = 1$we have$\begin{array} { r } { f _ { h } ( y ) = \sum _ { x } f ( x + h , y ) \overline { { f ( x , y ) } } } \end{array}$, as before. (We have taken$C ^ { \left| \epsilon \right| + k }$rather than the simpler$\dot { C } ^ { | \epsilon | }$in the definition merely to make it consistent with the earlier one.)

Lemma 14.3. Let$f : \mathbb { Z } _ { N } ^ { k + 1 } \to D$, let$B \subset \mathbb { Z } _ { N } ^ { k }$and let$\phi : B \to \mathbb { Z } _ { N }$be such that$| \hat { f } _ { z } ( \phi ( z ) ) | \geqslant \gamma N ^ { k + 1 }$for every$z \in B$. Then$\phi$has the product property with parameter γ.

Proof. For any$y = ( y _ { 1 } , \dots , y _ { k - 1 } ) \in \mathbb { Z } _ { N } ^ { k - 1 }$we can define a function$g _ { y } :$ $\mathbb { Z } _ { N } ^ { 2 } \to D$by the formula

$$
g _ {y} (a, b) = \sum_ {u \in \mathbb {Z} _ {N} ^ {k - 1}} \prod_ {\epsilon \in \{0, 1 \} ^ {k - 1}} C ^ {| \epsilon | + k - 1} f (u _ {1} + \epsilon_ {1} y _ {1}, \dots , u _ {k - 1} + \epsilon_ {k - 1} y _ {k - 1}, a, b).
$$

It is then easy to check that for any$h \in \mathbb { Z } _ { N }$we have$( g _ { y } ) _ { h } = f _ { ( y , h ) }$

The proof is now more or less the same as that of Lemma 14.2. Let $y _ { 1 } , \ldots , y _ { p }$be elements of$\mathbb { Z } _ { N } ^ { k - 1 }$(note that$y _ { i }$is now a vector rather than a coeficient of$y )$and let$E$be the set of all$h \in \mathbb { Z } _ { N }$such that$( y _ { i } , h ) \in B$ for every i. Given a function$\theta : E \to \mathbb { R } _ { + }$, set$\theta ( k ) = 0$for$k \notin E$and this time apply Proposition 14.1 to the functions$\dot { g } ^ { ( i ) } = N ^ { - ( k - 1 ) } g _ { y _ { i } }$. We certainly have$g ^ { ( i ) } : \mathbb { Z } _ { N } ^ { 2 } \to D$. Since$g _ { h } ^ { ( i ) } = N ^ { - ( k - 1 ) } f _ { y _ { i } , h }$, we find that $\hat { g } _ { h } ^ { ( i ) } ( r ) = N ^ { - ( k - 1 ) } \hat { f } _ { y _ { i } , h } ( r )$, which is at least$\gamma N ^ { 2 }$if$h \in E$and$r = \phi ( y _ { i } , h )$ Therefore, the functions$g ^ { ( i ) }$satisfy the hypothesis of Proposition 14.1 with $\begin{array} { r } { \alpha = \gamma ^ { 2 p } \sum _ { k } \theta ( k ) N ^ { - 1 } } \end{array}$and$\sigma _ { i } ( h ) = \phi ( y _ { i } , h )$. The conclusion of the lemma then gives us exactly what we want for k-restrictions. Once again the result for j-restrictions follows by symmetry.✷

Now we shall define, in two stages, an appropriate generalization of a parallelogram. Let B be a subset of$\mathbb { Z } _ { N } ^ { k }$. By a cube in B with sidelengths $( h _ { 1 } , \ldots , h _ { k } )$we shall mean a function κ from$\{ 0 , 1 \} ^ { k }$to B of the form

$$
\kappa : \left(\epsilon_ {1}, \dots , \epsilon_ {k}\right) \mapsto \left(r _ {1} + \epsilon_ {1} h _ {1}, \dots , r _ {k} + \epsilon_ {k} h _ {k}\right).
$$

We shall sometimes denote this cube$\left[ r _ { 1 } , \ldots , r _ { k } ; h _ { 1 } , \ldots , h _ { k } \right]$. For$k \geqslant 2$it will later be convenient to think of$\mathbb { Z } _ { N } ^ { \bar { k } + 1 }$as a product$\mathbb { Z } _ { N } ^ { k } \times \mathbb { Z } _ { N }$. Given a subset$B \subset \mathbb { Z } _ { N } ^ { k + 1 }$, we shall mean by a cross-section of B a set of the form$B _ { r } = \{ \left( r _ { 1 } , \ldots , r _ { k } , r _ { k + 1 } \right) \in B : r _ { k + 1 } = r \}$. A cube in$B _ { r }$will simply mean a function from$\{ 0 , 1 \} ^ { k }$to$B _ { r }$of the form$\epsilon \mapsto ( \kappa ( \epsilon ) , r )$, where κ is a cube in$\mathbb { Z } _ { N } ^ { k }$. We shall sometimes denote this cube by$( \kappa , r )$. Two cubes (not necessarily in the same cross-section) will be called congruent if they have the same sidelengths$( h _ { 1 } , \ldots , h _ { k } )$. By a parallelepiped in B we shall mean an ordered pair of congruent cubes, both lying in cross-sections of B. A parallelepiped pair will mean an ordered quadruple $\big ( ( \kappa _ { 1 } , r _ { 1 } ) , ( \kappa _ { 2 } , r _ { 2 } ) , ( \kappa _ { 3 } , r _ { 3 } ) , ( \kappa _ { 4 } , r _ { 4 } ) \big )$, where$\kappa _ { 1 } , \kappa _ { 2 } , \kappa _ { 3 } , \kappa _ { 4 }$are congruent and $( r _ { 1 } , r _ { 2 } , r _ { 3 } , r _ { 4 } )$is an additive quadruple.

In order to prove facts about parallelepiped pairs, it will be convenient to make two further definitions. If$B \subset \mathbb { Z } _ { N } ^ { k }$, then by a configuration in

$B$we shall mean, roughly speaking, a product$Q _ { 1 } \times \cdots \times Q _ { k }$of additive quadruples. This is not quite an accurate description as additive quadruples are defined as ordered sets. The order matters here as well, and a precise definition is that a configuration in$B$is a function$\lambda : \{ 0 , 1 \} ^ { k } \times \{ 0 , 1 \} ^ { k }  B$ of the form

$$
\lambda : (\epsilon , \eta) \mapsto (r _ {1} + \epsilon_ {1} g _ {1} + \eta_ {1} h _ {1}, r _ {2} + \epsilon_ {2} g _ {2} + \eta_ {2} h _ {2}, \dots , r _ {k} + \epsilon_ {k} g _ {k} + \eta_ {k} h _ {k}).
$$

We shall sometimes denote this configuration by$[ r _ { 1 } , \ldots , r _ { k } ; g _ { 1 } , \ldots , g _ { k } ;$ $h _ { 1 } , \ldots , h _ { k } ]$

If we choose$j$and fix every$\epsilon _ { i }$and$\eta _ { i }$for$i \neq j$, then we define a restriction of λ which gives an additive quadruple in the j-direction. If $\phi$is a function from$B$to$\mathbb { Z } _ { N }$such that all the$4 ^ { k - 1 }$additive quadruples that arise in this way are φ-additive, then we shall say that$\phi$respects the configuration$\lambda .$

Given$B \subset \mathbb { Z } _ { N } ^ { k }$, a function$\phi : B \to \mathbb { Z } _ { N }$and a cube κ in$B .$, we define

$$
\phi (\kappa) = \sum_ {\epsilon \in \{0, 1 \} ^ {k}} (- 1) ^ {| \epsilon |} \phi (\kappa (\epsilon)).
$$

(Here, as elsewhere, || denotes$\textstyle \sum _ { i = 1 } ^ { k } \epsilon _ { i } . )$Just to illustrate this definition, we note that

$$
\phi [ x, y; a, b ] = \phi (x + a, y + b) - \phi (x + a, y) - \phi (x, y + b) + \phi (x, y).
$$

Define a cube pair in B to be an ordered pair$( \kappa _ { 1 } , \kappa _ { 2 } )$of congruent cubes. (The diference between this and a parallelepiped is that the cubes are full-dimensional.) We shall say that$\phi$respects this pair if$\phi ( \kappa _ { 1 } ) = \phi ( \kappa _ { 2 } )$

Lemma 14.4. Let$B \subset \mathbb { Z } _ { N } ^ { k }$be a set of size$\beta N ^ { k }$, let$\phi : B \to \mathbb { Z } _ { N }$and suppose that φ has the product property with parameter γ. Then φ respects at least$\beta ^ { 4 ^ { k } } \gamma ^ { 2 k . 4 ^ { k } } N ^ { 3 k }$configurations in$B .$

Proof. When$k = 1$, a configuration is an additive quadruple and$\phi$respects it if and only if it is φ-additive. Therefore, Proposition 6.1 gives us the result.

Now suppose that$k > 1$and that the result is true for$k - 1$. Let $B \subset \mathbb { Z } _ { N } ^ { k }$be a set of cardinality$\beta N ^ { k }$and for each$r$let$B _ { r }$be the cross-section$\{ ( x _ { 1 } , \ldots , x _ { k } ) \in B : x _ { k } = r \}$. Write$\beta ( r ) N ^ { k - 1 }$for the cardinality $B _ { r }$

By our inductive hypothesis,$B _ { r }$contains at least$\beta ( r ) ^ { 4 ^ { k - 1 } } \gamma ^ { 2 ( k - 1 ) . 4 ^ { k - 1 } } N ^ { 3 ( k - 1 ) }$ configurations respected by$\phi .$. By Jensen’s inequality, the average of this quantity over$r$is at least$\ddot { \beta } ^ { 4 ^ { \dot { k } - 1 } } \gamma ^ { \dot { 2 } ( k - 1 ) . 4 ^ { k - 1 } } N ^ { 3 ( k - 1 ) }$. Therefore, if a random configuration λ is chosen in$\mathbb { Z } _ { N } ^ { k - 1 }$, then the average number of values of r for which$\phi$respects the configuration$( \lambda , r )$(by which we mean the function from$\{ 0 , 1 \} ^ { k - 1 }$to$B _ { r }$defined by$\epsilon \mapsto ( \lambda ( \epsilon ) , r ) )$is at least$\beta ^ { 4 ^ { k - 1 } } \gamma ^ { 2 ( k - 1 ) . 4 ^ { k - 1 } } N$ Let$E ( \lambda )$be the set of such r and let$\eta ( \lambda ) N$be the size of$E ( \lambda )$

We now fix λ and apply the product property to the$4 ^ { k - 1 }$functions $x \mapsto \phi ( \lambda ( \epsilon _ { 1 } , \epsilon _ { 2 } ) , x )$, which are all defined on the set$E = E ( \lambda )$. Taking θ to be identically 1, we obtain from the product property that there are at least$\gamma ^ { 8 . 4 ^ { k - 1 } } \eta ( \lambda ) ^ { 4 } \dot { N } ^ { 3 }$quadruples$a + b = c + d$such that for every$( \epsilon _ { 1 } , \epsilon _ { 2 } ) \in$ $\{ 0 , 1 \} ^ { \dot { k } - 1 } \times \{ \dot { 0 } , \dot { 1 } \} ^ { k - 1 }$we have

$$
\phi (\lambda (\epsilon_ {1}, \epsilon_ {2}), a) + \phi (\lambda (\epsilon_ {1}, \epsilon_ {2}), b) = \phi (\lambda (\epsilon_ {1}, \epsilon_ {2}), c) + \phi (\lambda (\epsilon_ {1}, \epsilon_ {2}), d).
$$

But, by the definition of$E _ { \mathrm { { i } } }$each such quadruple gives us a configuration in B which is respected by$\phi .$. Since the average of$\eta ( \lambda )$is at least $\beta ^ { 4 ^ { k - 1 } } \gamma ^ { 2 ( k - 1 ) . 4 ^ { k - 1 } }$, Jensen’s inequality implies that the number of configurations in B that are respected by$\phi$is at least$\gamma ^ { 8 . 4 ^ { k - 1 } } \beta ^ { 4 ^ { k } } \gamma ^ { 2 ( k - 1 ) . 4 ^ { k } } N ^ { 3 k } =$ $\beta ^ { 4 ^ { k } } \gamma ^ { 2 k . 4 ^ { k } } N ^ { 3 k }$, which proves the result.✷

Corollary 14.5. Let$B \subset \mathbb { Z } _ { N } ^ { k }$be a set of size$\beta N ^ { k }$, let$\phi : B \to \mathbb { Z } _ { N }$ and suppose that φ has the product property with parameter$\gamma$. Then$\phi$ respects at least$\beta ^ { \dot { 4 } ^ { k } } \gamma ^ { 2 k . 4 ^ { k } } N ^ { 3 \hat { k } }$cube pairs in$B .$

Proof. Let$\lambda = [ r _ { 1 } , \ldots , r _ { k } ; g _ { 1 } , \ldots , g _ { k } ; h _ { 1 } , \ldots , h _ { k } ]$be a configuration in B which is respected by$\phi$. We shall show that the cube pair

$$
\left(\left[ r _ {1}, \dots , r _ {k}; h _ {1}, \dots , h _ {k} \right], \left[ r _ {1} + g _ {1}, \dots , r _ {k} + g _ {k}; h _ {1}, \dots , h _ {k} \right]\right)
$$

is also respected by$\phi .$. Since distinct configurations give distinct cube pairs in this way, we will have proved the corollary. For every$j$between 0 and k let us define$\kappa _ { j }$to be the cube

$$
\left[ r _ {1} + g _ {1}, \dots , r _ {j} + g _ {j}, r _ {j + 1}, \dots , r _ {k}; h _ {1}, \dots , h _ {k} \right].
$$

Because$\phi$respects the configuration$\lambda ,$we know that for all choices of$\eta _ { j }$ for$j \neq i ,$, the additive quadruple

$$
\begin{array}{c} (r _ {1} + g _ {1} + \eta_ {1} h _ {1}, \ldots , r _ {j - 1} + g _ {j - 1} + \eta_ {j - 1}, r _ {j} + \epsilon_ {j} g _ {j} + \eta_ {j} h _ {j}, r _ {j + 1} + \eta_ {j + 1} h _ {j + 1}, \\ \ldots , r _ {k} + \eta_ {k} h _ {k})  , \end{array}
$$

where$\epsilon _ { i }$and$\eta _ { i }$take the values 0 or 1, is$\phi \cdot$-additive. This implies that $\phi ( \kappa _ { j - 1 } ) = \phi ( \kappa _ { j } )$, and the argument works for every$j$between 1 and$k$. Therefore,$\phi ( \kappa _ { 0 } ) = \phi ( \kappa _ { k } )$, which is the required result.✷

Corollary 14.6. Let$B \subset \mathbb { Z } _ { N } ^ { k + 1 }$be a set of size$\beta N ^ { k + 1 }$, let$\phi : B \to \mathbb { Z } _ { N }$ and suppose that$\phi$has the product property with parameter$\gamma$. Then$\phi$ respects at least$\beta ^ { 4 ^ { k + 1 } } \gamma ^ { k . 4 ^ { k + 1 } } N ^ { 5 k + 3 }$parallelepiped pairs in$B$

Proof. The proof of this result is similar to that of Lemma 14.4. For each $r \in \mathbb { Z } _ { N }$let$\beta ( r ) N ^ { k }$be the size of the cross-section$B _ { r }$of B. By Corollary $1 4 . 5 , \phi$respects at least$\beta ( r ) ^ { 4 ^ { k } } \gamma ^ { 2 k . 4 ^ { k } } N ^ { 3 k }$cube pairs in$B _ { r }$. The average of this number over$r$is at least$\beta ^ { 4 ^ { k } } \gamma ^ { 2 k . 4 ^ { k } } N ^ { 3 k }$. Therefore, if we choose r at random and choose a cube κ in$\mathbb { Z } _ { N } ^ { k }$at random, the expected number of cubes$\kappa ^ { \prime }$in$\mathbb { Z } _ { N } ^ { k }$for which$\bigl ( ( \kappa , r ) , ( \bar { \kappa ^ { \prime } } , r ) \bigr )$is a cube pair in$B _ { r }$respected by $\phi$is at least$\beta ^ { 4 ^ { k } } \gamma ^ { 2 k . 4 ^ { k } } N ^ { k }$

Now let κ be some fixed cube in$\mathbb { Z } _ { N } ^ { k }$and for each r let$\theta ( r )$be the number of cubes$\kappa ^ { \prime }$in$\mathbb { Z } _ { N } ^ { k }$for which$\bigl ( ( \bar { \kappa } , r ) , ( \kappa ^ { \prime } , r ) \bigr )$is a cube pair in$B _ { r }$ respected by$\phi .$ Let θ be the average of the$\theta ( r )$. By the product property, the sum of$\theta ( a ) \theta ( b ) \theta ( c ) \theta ( d )$over all additive quadruples$( a , b , c , d )$such that

$$
\phi (\kappa (\epsilon), a) + \phi (\kappa (\epsilon), b) = \phi (\kappa (\epsilon), c) + \phi (\kappa (\epsilon), d)
$$

for every$\epsilon \in \{ 0 , 1 \} ^ { k }$is at least$\theta ^ { 4 } \gamma ^ { 8 . 2 ^ { k } } N ^ { 4 k + 3 }$. But this sum counts the number of parallelepiped pairs$\left( \left( \kappa _ { i } ^ { \prime } , r _ { i } \right) \right) _ { i = 1 } ^ { 4 }$in B such that, for each i,$( \kappa _ { i } , r _ { i } )$ lies in$B _ { r _ { i } }$and$( \kappa _ { i } ^ { \prime } , r _ { i } )$  is congruent to it. It is certainly a lower bound for the number of parallelepiped pairs such that each of the four cubes is congruent to κ.

If we now choose randomly, for every$\boldsymbol { h } \ = \ \left( h _ { 1 } , \ldots , h _ { k } \right)$, some cube $\kappa ( h )$with sidelengths$( h _ { 1 } , \ldots , h _ { k } )$and apply the above argument, we shall obtain, on average, at least$( { \beta ^ { 4 } } ^ { k } \gamma ^ { 2 k . 4 ^ { k } } ) ^ { 4 } \gamma ^ { 8 . 2 ^ { k } } N ^ { 5 k + 3 }$distinct parallelepiped pairs, since the average of θ (which still depends on$\kappa )$is at least$\beta ^ { 4 ^ { k } } \gamma ^ { 2 k . 4 ^ { k } }$ This proves the corollary (where, just for the sake of neatness, we have stated a weaker bound).✷

Let$B \subset \mathbb { Z } _ { N } ^ { k + 1 }$. By a d-arrangement in B we shall mean a sequence $C _ { 1 } , \ldots , C _ { 2 d }$of congruent cubes, where$C _ { j }$lies in the cross-section$B _ { r _ { j } }$, and

$$
r _ {1} + \dots + r _ {d} = r _ {d + 1} + \dots + r _ {2 d}.
$$

Thus, a parallelepiped pair is simply a 2-arrangement, and when$k = 1$we recover the definition of d-arrangement given in §12. It is also convenient to think of a d-arrangement as a function$\rho : \{ 0 , 1 \} ^ { k } \times \{ 1 , 2 , \ldots , 2 d \} \to \mathbb { Z } _ { N } ^ { k + 1 }$ of the form

$$
\rho : (\epsilon_ {1}, \dots , \epsilon_ {k}, j) \mapsto (y _ {1} ^ {j} + \epsilon_ {1} h _ {1}, \dots , y _ {k} ^ {j} + \epsilon_ {k} h _ {k}, r _ {j}).
$$

Here,$r _ { 1 } , \ldots , r _ { 2 d }$are as above and each of the constituent cubes of the$d -$ arrangement has sidelengths$( h _ { 1 } , \ldots , h _ { k } )$but is otherwise arbitrary. It is easy to see that the number of d-arrangements in$\mathbb { Z } _ { N } ^ { k + 1 }$is$N ^ { ( 2 d + 1 ) { \ddot { k } } + 2 d - 1 }$ The next lemma is a generalization of Lemma 12.4 and has a very similar proof.

Lemma 14.7. Let$B \subset \mathbb { Z } _ { N } ^ { k + 1 }$and let$\phi : B \to \mathbb { Z } _ { N }$. Suppose that φ respects $\theta N ^ { 5 k + 3 }$parallelepiped pairs in B. Then$\phi$respects at least$\theta ^ { 7 } \dot { N } ^ { 1 7 k + 1 5 }$8- arrangements in B.

Proof. Given$u , x \ \in \ \mathbb { Z } _ { N }$and$h \ = \ ( h _ { 1 } , \ldots , h _ { k } ) \ \in \ \mathbb { Z } _ { N } ^ { k }$, let$f _ { u , h } ( x )$be $\textstyle \sum _ { \kappa } \bar { \omega } ^ { u \phi ( \kappa , x ) }$, where the sum is over all configurations κ in$\mathbb { Z } _ { N } ^ { k }$with side-lengths$( h _ { 1 } , \ldots , h _ { k } )$, and we interpret$\omega ^ { u \phi ( \kappa , x ) }$as zero when$\phi ( \kappa , x )$is not defined (which happens when$( \kappa , x )$does not live in$B _ { x } )$. Clearly$\vert f _ { u , h } ( x ) \vert$ is at most$N ^ { k }$for every$u , x , h$, which implies that$\begin{array} { r } { \sum _ { x } \vert f _ { u , h } ( x ) \vert ^ { 2 } \leqslant N ^ { 2 k + 1 } } \end{array}$ for every$u , h .$, and therefore that$\begin{array} { r } { \sum _ { u , r , h } | \hat { f } _ { u , h } ( r ) | ^ { 2 } \leqslant N ^ { \bar { 3 } k + 3 } } \end{array}$

We also have

$$
\sum_ {u, r} | \hat {f} _ {u, h} (r) | ^ {4} = \sum_ {u, r} \Bigl | \sum_ {\kappa , x} \omega^ {u \phi (\kappa , x) - r x} \Bigr | ^ {4}
$$

for every$h ,$where once again κ ranges over all cubes in$\mathbb { Z } _ { N } ^ { k }$with sidelengths $( h _ { 1 } , \ldots , h _ { k } )$. This is$N ^ { 2 }$times the number of parallelepiped pairs respected by φ for which the sidelengths of the cubes are$( h _ { 1 } , \ldots , h _ { k } )$. It follows from our assumptions that

$$
\sum_ {u, r, h} | \hat {f} _ {u, h} (r) | ^ {4} \geqslant \theta N ^ {5 k + 5}.
$$

Similarly,$\begin{array} { r } { \sum _ { u , r , h } | \hat { f } _ { u , h } ( r ) | ^ { 1 6 } } \end{array}$is$N ^ { 2 }$times the number of 8-arrangements respected by φ. Therefore, by Lemma 9.1, the number of 8-arrangements is at least$\bar { N } ^ { - 2 } ( \theta N ^ { 5 k + 5 } / N ^ { 6 ( 3 \bar { k } + 3 ) / 7 } ) ^ { 7 } = \theta ^ { 7 } N ^ { 1 7 k + 1 5 }$as claimed.✷

Combining Corollary 14.6 and Lemma 14.7 we obtain the main result of this section (which will be applied in conjunction with Lemmas 14.2 and 14.3).

Lemma 14.8. Let$B \subset \mathbb { Z } _ { N } ^ { k + 1 }$be a set of size$\beta N ^ { k + 1 }$, let$\phi : B \to \mathbb { Z } _ { N }$ and suppose that φ has the product property with parameter γ. Then φ respects at least$\beta ^ { \dot { 7 } . 4 ^ { k + 1 } } \gamma ^ { 7 k . 4 ^ { k ^ { 2 } + 1 } } N ^ { 1 7 k + \dot { 1 } 5 }$8-arrangements in B.✷

## 15 Increasing the Density of Respected Arrangements

We shall now use an argument similar to those of §9 and §12 to pass to a subset of B where$\phi$respects almost all 8-arrangements. (We shall actually prove our results for general d-arrangements and then take d to be 8 later.) In order to do this, we shall need a brief discussion of a small number of degenerate cases where a later argument does not work. Just for the next lemma it will be convenient to consider sequences in$\{ - 1 , 1 \} ^ { k }$rather than$\{ 0 , 1 \} ^ { k }$

Lemma 15.1. Let$h _ { 1 } , \ldots , h _ { k }$be non-zero elements of$\mathbb { Z } _ { N }$, and let$\eta \textit { \textbf { \xi } }$ $\{ - 1 , 1 \} ^ { k } \to \{ - 1 , 0 , 1 \}$be a function such that the sum

$$
\sum_ {\epsilon \in \{- 1, 1 \} ^ {k}} \eta (\epsilon) \prod_ {i \in A} (y _ {i} + \epsilon_ {i} h _ {i})
$$

is independent of$y _ { 1 } , \ldots , y _ { k }$for every subset$A \subset \{ 1 , 2 , \ldots , k \}$. Then η is a multiple of the function$\epsilon \mapsto \prod \epsilon _ { i }$

Proof. Throughout this lemma, any sum over  will denote the sum over all  in the set$\{ - 1 , 1 \} ^ { k }$. The functions$\epsilon \mapsto \prod _ { i \in A } \epsilon _ { i }$are orthogonal with respect to the symmetric bilinear form$\begin{array} { r } { \langle \eta _ { 1 } , \eta _ { 2 } \rangle = \sum _ { \epsilon } \eta _ { 1 } ( \epsilon ) \eta _ { 2 } ( \epsilon ) } \end{array}$. (Recall that N is prime. This bilinear form is defined on the vector space$\mathbb { Z } _ { N } ^ { \{ - 1 , 1 \} ^ { k } }$and the functions are the Walsh basis for this space.) Therefore, it is enough to prove that$\begin{array} { r } { \sum _ { \epsilon } \eta ( \epsilon ) \prod _ { i \in A } \epsilon _ { i } = 0 } \end{array}$for every proper subset$A \subset \{ 1 , 2 , \ldots , k \}$ This we do by induction on A (with respect to containment).

First, let A be a proper subset of$\{ 1 , 2 , \ldots , k \}$and let$j \not \in A$. From the assumption of the lemma, applied to the set$A \cup \{ j \}$, we know that

$$
y _ {j} \sum_ {\epsilon} \eta (\epsilon) \prod_ {i \in A} (y _ {i} + \epsilon_ {i} h _ {i}) + h _ {j} \sum_ {\epsilon} \eta (\epsilon) \epsilon_ {j} \prod_ {i \in A} (y _ {i} + \epsilon_ {i} h _ {i})
$$

is independent of$y _ { j }$. Since the second part of the sum does not involve$y _ { j }$, this implies that

$$
\sum_ {\epsilon} \eta (\epsilon) \prod_ {i \in A} (y _ {i} + \epsilon_ {i} h _ {i}) = 0.
$$

Now we give the inductive argument. When$A = \emptyset$, we have

$$
\sum_ {\epsilon} \eta (\epsilon) \prod_ {i \in A} \epsilon_ {i} = \sum_ {\epsilon} \eta (\epsilon) = \sum_ {\epsilon} \eta (\epsilon) \prod_ {i \in A} (y _ {i} + \epsilon_ {i} h _ {i}),
$$

which is zero by the above inequality. For general A, we have

$$
\begin{array}{l} 0 = \sum_ {\epsilon} \eta (\epsilon) \prod_ {i \in A} (y _ {i} + \epsilon_ {i} h _ {i}) \\ \quad = \sum_ {\epsilon} \eta (\epsilon) \sum_ {B \subset A} \prod_ {i \in A \setminus B} y _ {i} \prod_ {i \in B} \epsilon_ {i} h _ {i} \\ \quad = \sum_ {B \subset A} \prod_ {i \in A \setminus B} y _ {i} \prod_ {i \in B} h _ {i} \sum_ {\epsilon} \eta (\epsilon) \prod_ {i \in B} \epsilon_ {i} \\ \quad = \prod_ {i \in A} h _ {i} \sum_ {\epsilon} \eta (\epsilon) \prod_ {i \in A} \epsilon_ {i} \end{array}
$$

where the last equality follows from the inductive hypothesis. Since the$h _ { i }$ are non-zero, the result is proved for A.✷

If we now make the substitution$y _ { i } ^ { \prime } = y _ { i } - h _ { i }$and$h _ { i } ^ { \prime } = 2 h _ { i }$, and then remove the dashes, we obtain the result for functions on$\{ 0 , 1 \} ^ { k }$, which is what we actually want.

Corollary 15.2. Let$h _ { 1 } , \ldots , h _ { k }$be non-zero elements of$\mathbb { Z } _ { N }$, and let $\eta : \{ 0 , 1 \} ^ { k }  \{ - 1 , 0 , 1 \}$be a function such that the sum

$$
\sum_ {\epsilon \in \{0, 1 \} ^ {k}} \eta (\epsilon) \prod_ {i \in A} (y _ {i} + \epsilon_ {i} h _ {i})
$$

is independent of$y _ { 1 } , \ldots , y _ { k }$for every subset$A \subset \{ 1 , 2 , \ldots , k \}$. Then$\eta$is a multiple of the parity function$\pi : \epsilon \mapsto ( - 1 ) ^ { \sum \epsilon _ { i } }$✷

Define a function η<sub>0</sub>$: \{ 0 , 1 \} ^ { k } \times \{ 1 , 2 , \ldots , 2 d \} \to \{ - 1 , 1 \}$by letting $\eta _ { 0 } ( \epsilon , j )$be$\pi ( \epsilon )$if$1 \leqslant j \leqslant$d and$- \pi ( \epsilon )$if$d + 1 \leqslant j \leqslant 2 d$. We shall say that a d-arrangement$\rho$is degenerate if there is a function$\eta \ : \cdot \ : \because \ :$ $\{ 0 , 1 \} ^ { k } \times \{ 1 , 2 , \ldots , 2 d \}  \{ - 1 , 0 , 1 \}$which is not a multiple of$\eta _ { 0 }$but which nevertheless has the property that

$$
\sum_ {\epsilon , j} \eta (\epsilon , j) \prod_ {i \in A} \rho (\epsilon , j) _ {i} = 0
$$

for every subset$A \subset \{ 1 , 2 , \dotsc , k + 1 \}$. (Here,$\rho ( \epsilon , j ) .$<sub>i</sub> denotes the$i ^ { \mathrm { t h } }$co-ordinate of$\rho ( \epsilon , j ) . )$We wish to show that there are very few degenerate d-arrangements. Let us give a simple lemma first.

Lemma 15.3. Let$\mu : \mathbb { Z } _ { N } ^ { k } \to \mathbb { Z } _ { N }$be a multilinear function which is not constant. Then for any a the number of solutions of$\mu ( y _ { 1 } , \ldots , y _ { k } ) = a$is at most$N ^ { k } - ( N - 1 ) ^ { k } \leqslant k N ^ { k - 1 }$

Proof. The result is trivial when$k = 1$, so let$k > 1$and assume the result for$k - 1$. There are unique multilinear functions$\mu _ { 1 }$and$\mu _ { 2 }$such that

$$
\mu (y _ {1}, \dots , y _ {k}) \equiv y _ {k} \mu_ {1} (y _ {1}, \dots , y _ {k - 1}) + \mu_ {2} (y _ {1}, \dots , y _ {k - 1}).
$$

If we can find two diferent elements$r , s$of$\mathbb { Z } _ { N }$such that the$( k - 1 )$-linear restrictions$\mu ( y _ { 1 } , \ldots , y _ { k - 1 } , r )$and$\mu ( y _ { 1 } , \dots , y _ { k - 1 } , s )$of$\mu$are both constant, then we can solve for$\mu _ { 1 }$and$\mu _ { 2 }$and show that they are both constant as well. Since$\mu$is non-constant,$\mu _ { 1 }$is not identically zero and there are exactly$N ^ { k - 1 }$solutions of the equation.

Otherwise, with the exception of at most one$r ,$the function $\mu ( y _ { 1 } , \ldots , y _ { k - 1 } , r )$is not constant. This allows us to apply our inductive hypothesis to conclude that the number of solutions of$\mu ( y _ { 1 } , \ldots , y _ { k } ) = a$is at most$N ^ { k - 1 } + ( N - 1 ) ( N ^ { k - 1 } - ( N - 1 ) ^ { k - 1 } ) = N ^ { k } - ( N - 1 ) ^ { k }$✷

The estimate above is sharp, since it gives the exact number of solutions of the equation$y _ { 1 } \ldots y _ { k } = 0$

Lemma 15.4. The number ofdegenerate d-arrangements in$\mathbb { Z } _ { N } ^ { k + 1 }$is at most $3 ^ { 2 d . 2 ^ { k } } k N ^ { ( 2 d + 1 ) k + 2 d - 2 }$

Proof. Let us fix non-zero sidelengths$h _ { 1 } , . . . , h _ { k }$and cross-sections$r _ { 1 } , . . . , r _ { 2 d }$ and take a general d-arrangement

$$
\rho : (\epsilon_ {1}, \ldots , \epsilon_ {k}, j) \mapsto (y _ {1} ^ {j} + \epsilon_ {1} h _ {1}, \ldots , y _ {k} ^ {j} + \epsilon_ {k} h _ {k}, r _ {j})
$$

with those sidelengths.

Suppose first that$\eta ( \epsilon , j )$fails, for some$j ,$, to be a multiple of the parity function$\pi .$. Then Corollary 15.2 tells us that there exists a set $A \subset \{ 1 , \ldots , k \}$such that${ \textstyle \sum _ { \epsilon } } \eta ( \epsilon , j ) \prod _ { i \in { \cal A } } ( y _ { i } + \epsilon _ { i } h _ { i } )$, when considered as a function of$y _ { 1 } , \ldots , y _ { k }$, is non-constant. By Lemma$1 5 . 3$, whatever the choice of$\rho ( \epsilon , t )$for$t \neq j$there are at most$k N ^ { k - 1 }$choices of$( y _ { 1 } ^ { j } , \ldots , y _ { k } ^ { j } )$for which $\begin{array} { r } { \sum _ { \epsilon , t } \eta ( \epsilon , t ) \prod _ { i \in A } \rho ( \epsilon , t ) _ { i } = 0 } \end{array}$. Therefore, the number of d-arrangements with sidelengths$( h _ { 1 } , \ldots , h _ { k } )$and cross-sections$r _ { 1 } , \ldots , r _ { 2 d }$such that $\begin{array} { r c l } { \sum _ { \epsilon , t } \eta ( \epsilon ) \prod _ { i \in A } \rho ( \epsilon , t ) _ { i } } & { = } & { 0 } \end{array}$for every$A \subset \{ 1 , 2 , \ldots , k \}$is at most $k N ^ { k - 1 } N ^ { ( 2 d - 1 ) k } = k N ^ { 2 d k - 1 }$

If on the other hand$\eta ( \epsilon , j )$is a multiple of the parity function for every$j ,$ then let us write$\eta ( \epsilon , j ) = \eta _ { j } \pi ( \epsilon )$and consider the set$A = \{ 1 , 2 , \dots , k + 1 \}$ We have

$$
\sum_ {\epsilon , t} \eta (\epsilon , t) \prod_ {i \in A} \rho (\epsilon , t) _ {i} = \sum_ {\epsilon , t} \eta (\epsilon , t) \prod_ {i = 1} ^ {k + 1} \rho (\epsilon , t) _ {i} = (- 1) ^ {k} h _ {1} \dots h _ {k} \sum_ {j} \eta_ {j} r _ {j}.
$$

If$\eta$is not a multiple of$\eta _ { 0 }$, then$( \eta _ { 1 } , \dots , \eta _ { 2 d } )$is not a multiple of the sequence$( 1 , \ldots , 1 , - 1 , \ldots , - 1 )$(d ones followed by d minus ones). Therefore the equation$\textstyle \sum _ { j } \eta _ { j } r _ { j }$places a further linear restriction on the sequence $( r _ { 1 } , \ldots , r _ { 2 d } )$, meaning that the number of choices for this sequence is at most$N ^ { 2 d - 2 }$

There are (strictly) fewer than$3 ^ { 2 d . 2 ^ { k } }$functions$\eta : \{ 0 , 1 \} ^ { k } \times \{ 1 , \dots , 2 d \} \to$ $\{ - 1 , 0 , 1 \}$that are not multiples of$\eta _ { 0 }$. For each such function, the arguments we have just given show that the proportion of d-arrangements such that$\begin{array} { r } { \sum _ { \epsilon , t } \eta ( \epsilon ) \prod _ { i \in A } \rho ( \epsilon , t ) _ { i } = 0 } \end{array}$for every$A \subset \{ 1 , 2 , \dotsc , k + 1 \}$is at most $k / N$. Finally, the proportion of d-arrangements for which at least one of the sidelengths$h _ { i }$is zero is also at most$k / N$. The lemma is proved.✷

Notice that, in the above proof, the only set A containing the element $k + 1$that we needed to consider was the set$\{ 1 , 2 , \ldots , k + 1 \}$itself. Thus, it would be possible to get away with a weaker definition of degeneracy. We are now ready for another random selection with dependences defined using Riesz products.

Lemma 15.5. Let$\beta , \eta > 0$, let$B \subset \mathbb { Z } _ { N } ^ { k + 1 }$be a set of size$\beta N ^ { k + 1 }$and let$\phi : B \to \mathbb { Z } _ { N }$be a function respecting at least$\alpha \beta ^ { 1 5 } N ^ { 1 7 k + 1 5 }$8-arrangements in B. Then there is a subset$B ^ { \prime } \subset B$containing at least $( \alpha { \eta } / 4 ) ^ { 2 ^ { 2 ^ { k + 4 } + k + 3 } } \beta ^ { 1 5 } N ^ { 1 7 k + 1 5 }$8-arrangements, such that the proportion of them that are respected by$\phi$is at least$1 - \eta$

Proof. Let r be a positive integer to be determined later. For every set $A \subset \{ 1 , \ldots , k + 1 \}$and every$1 \leqslant j \leqslant r$choose elements$t _ { j }$and$s _ { A , j }$ uniformly and independently at random from$\mathbb { Z } _ { N }$. Having made the choices of the$t _ { j }$and the$s _ { A , j }$, let each element$y \in B$belong to$B ^ { \prime }$with probability $p ( y )$given by the formula

$$
2 ^ {- r} \prod_ {j = 1} ^ {r} \left(1 + \cos \frac {2 \pi}{N} \left(t _ {j} \phi (y) + \sum_ {A} s _ {A, j} \prod_ {i \in A} y _ {i}\right)\right)
$$

and let these probabilities be independent (conditional on the choices for the$t _ { j }$and$s _ { A , j } )$

Here, and for the rest of the proof, any sum over A ranges over all subsets of$\{ 1 , 2 , \ldots , k + 1 \}$. Let us adopt the following similar conventions. Any sum over  will range over$\{ 0 , 1 \} ^ { k }$, any sum over h will be over$\{ 1 , 2 , \ldots , 1 6 \}$ and any sum over$S$or$S _ { j }$will be over functions from the power set of $\{ 1 , 2 , \ldots , k + 1 \}$to$\mathbb { Z } _ { N }$. The idea of the last convention is that a sum over $S$or$S _ { j }$is shorthand for a string of$2 ^ { k + 1 }$sums of the form$\sum { _ { s _ { A } } }$or$\textstyle \sum _ { s _ { A , j } }$

The probability that an 8-arrangement$\lambda : \{ 0 , 1 \} ^ { k } \times \{ 1 , \dots , 1 6 \} \stackrel { } {  } B$ belongs to$B ^ { \prime }$is

$$
N ^ {- (2 ^ {k + 1} + 1) r} \sum_ {t _ {1}, \dots , t _ {r}} \sum_ {S _ {1}, \dots , S _ {r}} \prod_ {\epsilon , h} 2 ^ {- r} \prod_ {j = 1} ^ {r} \left(1 + \cos \frac {2 \pi}{N} \left(t _ {j} \phi (\lambda (\epsilon , h)) + \sum_ {A} s _ {A, j} \lambda (\epsilon , h) _ {i}\right)\right)
$$

which equals

$$
N ^ {- (2 ^ {k + 1} + 1) r} \left(\sum_ {t} \sum_ {S} \prod_ {\epsilon , h} 2 ^ {- r} \left(1 + \cos \frac {2 \pi}{N} (t \phi (\lambda (\epsilon , h)) + \sum_ {A} s _ {A} \lambda (\epsilon , h) _ {i})\right) ^ {r}. \right.
$$

By rewriting$\begin{array} { r } { 1 + \cos { \frac { 2 \pi } { N } } \big ( t \phi ( \lambda ( \epsilon , h ) ) + \sum _ { A } s _ { A } \lambda ( \epsilon , h ) _ { i } \big ) } \end{array}$as

$$
\frac {1}{2} (1 + 1 + \omega^ {t \phi (\lambda (\epsilon , h)) + \sum_ {A} s _ {A} \lambda (\epsilon , h) _ {i}} + \omega^ {- t \phi (\lambda (\epsilon , h)) - \sum_ {A} s _ {A} \lambda (\epsilon , h) _ {i}})
$$

we see that the product over$( \epsilon , h )$is a sum of$4 ^ { 2 ^ { k + 4 } }$terms of the form

$$
2 ^ {- 2 ^ {k + 4} (r + 1)} \prod_ {\epsilon , h} \omega^ {\eta (\epsilon , h) \left(t \phi (\lambda (\epsilon , h)) + \sum_ {A} s _ {A} \lambda (\epsilon , h) _ {i}\right)}
$$

which equals

$$
2 ^ {- 2 ^ {k + 4} (r + 1)} \omega^ {t} \sum_ {\epsilon , h} \eta (\epsilon , h) \phi (\lambda (\epsilon , h)) + \sum_ {A} s _ {A} \sum_ {\epsilon , h} \eta (\epsilon , h) \prod_ {i \in A} \lambda (\epsilon , h) _ {i}.
$$

$\mathrm { A }$term contributes to the sum over all the$s _ { A }$if and only if all the sums $\begin{array} { r } { \sum _ { \epsilon , h } \eta ( \epsilon , h ) \prod _ { i \in A } \lambda ( \epsilon , h ) _ { i } } \end{array}$<sub>i</sub> are zero, and if λ is non-degenerate, then this can happen only when η is a multiple of$\eta _ { 0 }$. If λ is non-degenerate,$\eta \neq 0$ and the term contributes to the sum over t, then we must have in addition that$\begin{array} { r } { \sum _ { \epsilon , h } \eta _ { 0 } ( \epsilon , h ) \phi ( \lambda ( \epsilon , h ) ) = 0 } \end{array}$. It is not hard to see that this is precisely the definition of$\phi$respecting the 8-arrangement$\lambda .$. The contribution of a non-zero term to the sum over t and the$s _ { A }$is$2 ^ { - 2 ^ { k + 4 } ( r + 1 ) } N ^ { 2 ^ { k } + 1 }$and the number of multiples of$\eta _ { 0 } .$, counted with multiplicity, is$2 ^ { 2 ^ { k + 4 } } + 2$, since 0 can be produced in$2 ^ { 2 ^ { k + 4 } }$ways, and$\pm \eta _ { 0 }$in one way each.

Therefore, if$\lambda$is non-degenerate, the sum over t and the$s _ { A }$is $2 ^ { - 2 ^ { k + 4 } r } N ^ { 2 ^ { k } + 1 }$if$\phi$does not respect λ and$2 ^ { - 2 ^ { k + 4 } r } N ^ { 2 ^ { k } + 1 } ( 1 + 2 . 2 ^ { - 2 ^ { k + 4 } } )$if it does. It follows that the probability that λ belongs to$B ^ { \prime }$is$2 ^ { - 2 ^ { k + 4 } r }$if $\phi$does not respect λ and$2 ^ { - \overset { \cdot } { 2 } ^ { k + 4 } r } ( 1 + \overset { \cdot } { 2 } . 2 ^ { - 2 ^ { k + 4 } } ) ^ { r }$if it does. Therefore, our hypotheses imply that the expected number X of 8-arrangements respected by φ is at least$\overset { \smile } { 2 ^ { - 2 ^ { k + 4 } r } } ( 1 + 2 . 2 ^ { - 2 ^ { k + 4 } } ) ^ { r } \alpha \beta ^ { 1 5 } N ^ { 1 7 k + 1 5 }$, and the expected number$Y$of non-degenerate 8-arrangements not respected by$\phi$is at most $2 ^ { - 2 ^ { k + 4 } r } \alpha \beta ^ { 1 5 } N ^ { 1 7 k + 1 5 }$. Using the fact that

$$
1 + 2. 2 ^ {- 2 ^ {k + 4}} \geqslant 2 ^ {2 ^ {- 2 ^ {k + 4} + 1}},
$$

we can deduce that if$2 ^ { 2 ^ { - 2 ^ { k + 4 } + 1 } r } \geqslant 2 / \alpha \eta .$, then

$$
\begin{array}{c} \eta \mathbb {E} X - \mathbb {E} Y \geqslant \alpha \eta (2 / \alpha \eta) 2 ^ {- 2 ^ {k + 4 r}} \beta^ {1 5} N ^ {1 7 k + 1 5} - 2 ^ {- 2 ^ {k + 4 r}} \beta^ {1 5} N ^ {1 7 k + 1 5} \\ \geqslant 2 ^ {- 2 ^ {k + 4 r}} \beta^ {1 5} N ^ {1 7 k + 1 5}. \end{array}
$$

But$2 ^ { 2 ^ { - 2 ^ { k + 4 } + 1 } r } \geqslant 2 / \alpha \eta$if and only if$2 ^ { r } \geqslant ( 2 / \alpha \eta ) ^ { 2 ^ { 2 ^ { k + 4 } - 1 } }$if and only if $2 ^ { - r } \leqslant ( \alpha \eta / 2 ) ^ { 2 ^ { 2 ^ { k + 4 } - 1 } }$if and only if

$$
2 ^ {- 2 ^ {k + 4} r} \leqslant (\alpha \eta / 2) ^ {2 ^ {2 ^ {k + 4} - 1} 2 ^ {k + 4}} = (\alpha \eta / 2) ^ {2 ^ {2 ^ {k + 4} + k + 3}}.
$$

Let r be an integer such that

$$
2 (\alpha \eta / 4) ^ {2 ^ {2 ^ {k + 4} + k + 3}} \leqslant 2 ^ {- 2 ^ {k + 4} r} \leqslant (\alpha \eta / 2) ^ {2 ^ {2 ^ {k + 4} + k + 3}}.
$$

If N is large enough that$( \alpha \eta / 4 ) ^ { 2 ^ { 2 ^ { k + 4 } + k + 3 } } \beta ^ { 1 5 } N \geqslant 3 ^ { 2 ^ { k + 4 } } k$, then Lemma 15.4 and the values of the above expectations imply that a set$B ^ { \prime }$exists such that$X \geqslant ( \alpha \eta / 4 ) ^ { 2 ^ { 2 ^ { k + 4 } + k + 3 } } \beta ^ { 1 5 } N ^ { 1 7 k + 1 5 }$，$\eta X \geqslant 2 Y$and$Y \geqslant Z$, where$Z$is the number of degenerate 8-arrangements. This proves the lemma.✷

The final lemma of this section is a combination of the previous one with Lemma 14.8 in the case$\eta = 2 ^ { - 4 4 }$, which is the value that will be used in applications.

Lemma 15.6. Let$\beta , \gamma > 0$. Let$B \subset \mathbb { Z } _ { N } ^ { k + 1 }$be a set ofsize$\beta N ^ { k + 1 }$and let$\phi :$ $B \to \mathbb { Z } _ { N }$be a function satisfying the product property with parameter γ. Then B has a subset$B ^ { \prime }$containing at least$( \beta \gamma / 2 ) ^ { 2 ^ { 2 ^ { k + 5 } } } N ^ { 1 7 k + 1 5 }$8-arrangements such that the proportion of them that are respected by$\phi$is at least $1 - 2 ^ { - 4 4 }$

Proof. By Lemma 14.8, φ respects at least$\beta ^ { 7 . 4 ^ { k } } \gamma ^ { 7 k . 4 ^ { k + 1 } } N ^ { 1 7 k + 1 5 }$8-arrangements, and therefore, by Lemma 15.5, B has a subset$B ^ { \prime }$containing at least $\left( 2 ^ { - 4 6 } \beta ^ { 7 . 4 ^ { k } } \gamma ^ { 7 k . 4 ^ { k + 1 } } \right) ^ { 2 ^ { 2 ^ { k + 4 } + k + 3 } } N ^ { 1 7 k + 1 5 } \mathrm { ~ 8 ~ }$-arrangements, such that the propor-tion respected by$\phi$is at least$1 - 2 ^ { - 4 4 }$. The lemma follows from a simple numerical check.✷

## 16 Finding a Multilinear Piece

This section is, as its title suggests, a generalization of §13. As with the last two sections, there will be no major new ideas over and above those needed for bilinearity (and hence progressions of length five) but it is not quite true that there is an obvious one-to-one correspondence between the lemmas that are needed. We begin with a simple consequence of Corollary 5.11. It is the appropriate generalization of Lemma 13.5.

Lemma 16.1. Let k be an integer, let$K = ( k + 1 ) ^ { 2 } 2 ^ { k + 4 }$and let$m \geqslant$ $2 ^ { K ^ { 2 ^ { k + 1 } q } 2 ^ { 3 2 ( k + 1 ) ^ { 2 } + 1 } }$. Let P be a box in$\mathbb { Z } _ { N } ^ { k }$of width at least$m ,$, and let $\mu _ { 1 } , \ldots , \mu _ { q }$be k-linear functions defined on$P .$. Then$P$can be partitioned into boxes$P _ { 1 } , \dots , P _ { M }$of width at least$m ^ { K ^ { - 2 ^ { k + 1 } } q }$with the following property. For every i and j and every$x \in P _ { j }$we have the inequality$| \mu _ { i } ( x ) d _ { j } | \leqslant$ $2 m ^ { - K ^ { - 2 ^ { k + 1 } q } } N$, where$d _ { j }$is the common diference of the box$P _ { j }$

Proof. Let d be the common diference of P and let$I \subset \mathbb { Z } _ { N }$be an arithmetic progression (in Z) of common diference d and size at least m. Then$Q =$ $P \times I$is a box in$\mathbb { Z } _ { N } ^ { k + 1 }$of gap d and width at least m. Define$( k + 1 )$-linear functions$\nu _ { i } : Q \to \mathbb { Z } _ { N }$by$\nu _ { i } ( x , y ) = \mu _ { i } ( x ) y$. By Corollary 5.11, we can partition$Q$into boxes$Q _ { j }$of width at least$m ^ { K ^ { - 2 ^ { k + 1 } } q }$in such a way that the diameter of every set$\nu _ { i } ( Q _ { j } )$is at most$2 C _ { k + 1 } m ^ { - K ^ { - 2 ^ { k + 1 } q } } N$. Let y be the minimal element of I and define an equivalence relation on$P$by setting $x _ { 1 } \sim x _ { 2 } { \mathrm { i f } } \left( x _ { 1 } , y \right)$and$( x _ { 2 } , y )$lie in the same box$Q _ { j }$. The equivalence classes are clearly boxes of width at least$m ^ { K ^ { - 2 ^ { k + 1 } } q }$, and the common diference$d _ { j }$ of one of these boxes$P _ { j }$is the common diference of the box$Q _ { j ^ { \prime } }$containing

$P _ { j } \times \{ y \}$. The result now follows from the observation that, given$x \in P _ { j }$

$$
\left| \mu_ {i} (x) d _ {j} \right| = \left| \nu_ {i} (x, y + d _ {j}) - \nu_ {i} (x, y) \right|,
$$

  which is at most the diameter of$\nu _ { i } ( Q _ { j ^ { \prime } } )$

We are about to state a somewhat complicated inductive hypothesis (Theorem 16.2 below) which will be used to prove the main result of this section. First, let us extend slightly the definition of the product property from §14. Let Γ be any subset of$\mathbb { Z } _ { N } ^ { k } \times \mathbb { Z } _ { N }$and let$\gamma > 0$. We shall say that Γ has the product property with parameter$\gamma \ { \mathrm { i f } } ,$for every subset $B \subset \mathbb { Z } _ { N } ^ { k }$and every function$\phi : B \to \mathbb { Z } _ { N }$with graph contained in Γ (in other words,$( x , \phi ( x ) ) \in \Gamma$for every$x \in B )$,$\phi$has the product property with parameter$\gamma .$. We shall sometimes abbreviate this as the γ-product property.

Before making the next definition, let us define three similar functions. We let$c ( \theta , \gamma , k ) = ( \gamma \theta ) ^ { 2 ^ { 2 ^ { k + \mathrm { s } } } } , q ( \theta , \gamma , k ) = 1 / c ( \theta , \gamma , k )$and$s ( \theta , \gamma , k ) =$ $( 2 / \theta \gamma ) ^ { 2 ^ { 2 ^ { k + 6 } } }$. We shall now define Γ to be$( \gamma , r ) – m u l t i p l y$k-linear if, for every$\theta > 0$and every box$P$of width$m .$, there exists a subset$H \subset P$ of cardinality at least$( 1 - \theta ) | P |$together with a partition of P into boxes $P _ { 1 } , \dots , P _ { M }$of width at least$\boldsymbol { m } ^ { c ( r ^ { - 1 } \theta , \gamma , k ) ^ { r } }$such that for each$j$there are k-linear functions$\mu _ { 1 } , \ldots , \mu _ { q }$defined on$P _ { j }$, where$q \leqslant q ( r ^ { - 1 } \theta , \gamma , k ) ^ { r }$, such that, for every$x \in P _ { j } \cap H$and every y with$( x , y ) \in \Gamma , y = \mu _ { i } ( x )$for some i. Loosely speaking, this says that every box$P$can be partitioned into further boxes$P _ { j }$such that, after a small bit of Γ has been thrown away, for every$j , \Gamma \cap ( P _ { j } \times \mathbb { Z } _ { N } )$is contained in the union of the graphs of not too many k-linear functions. If$r = 1$, we shall say simply that$\Gamma$is γ-multiply k-linear. If we do not wish to specify$k ,$, then we shall say that $\Gamma$is$( \gamma , r )$-multiply multilinear.

It is an immediate consequence of the definition that if Γ is a$( \gamma , r ) .$ multiply multilinear set and$\Gamma ^ { \prime } \subset \Gamma$, then$\Gamma ^ { \prime }$is also$( \gamma , r )$-multiply multi-linear.

The next theorem is the main inductive statement we shall need in order to prove an appropriate generalization of Theorem 13.12 to functions that fail to be uniform of degree$k + 1$. (See Corollary 16.11 below.)

Theorem 16.2. Let$\Gamma \subset \mathbb { Z } _ { N } ^ { k } \times \mathbb { Z } _ { N }$have cardinality at most$\gamma ^ { - 2 } N ^ { k }$and satisfy the product property with parameter$\gamma$. Then for every$\theta > 0$there is a subset J of$\mathbb { Z } _ { N } ^ { k }$of size at least$( 1 - \theta ) N ^ { k }$, such that$\Gamma \cap ( J \times \mathbb { Z } _ { N } )$is $( \gamma , \gamma ^ { - 2 } s ( \theta , \gamma , k ) )$)-multiply k-linear.

We shall split the proof of Theorem 16.2 into a number of lemmas, most of them easy. First, we check that the induction starts.

Lemma 16.3. Theorem 16.2 is true in the case$k = 1$

Proof. Let$\theta > 0$. Either there is a set H of size at most θN such that $\Gamma \subset H \times \mathbb { Z } _ { N }$or we can find a set A of size at least θN and a function $\phi : A  \mathbb { Z } _ { N }$such that$( x , \phi ( x ) ) \in \Gamma$for every$x \in A$. In the first case we can simply set$J = \mathbb { Z } _ { N } \ \backslash \ H$and the result is trivial. Otherwise, we know that$\phi$has the product property with parameter$\gamma .$, which implies that the number of φ-additive quadruples is at least$\gamma ^ { 8 } \theta ^ { 4 } N ^ { 3 } = \gamma ^ { 8 } \theta ( \theta N ) ^ { 3 }$. Corollary 7.6 now gives us a subset$B \subset A$of cardinality at least$2 ^ { - 1 8 8 2 } \gamma ^ { 9 3 1 2 } \theta ^ { 1 1 6 5 } \bar { N }$ such that the restriction of$\phi$to$B$is a homomorphism of order 8.

If we now remove from Γ all points$( x , \phi ( x ) )$with$x \in B$, we obtain a new set$\Gamma _ { 1 }$to which the above argument may be applied again. Continuing, we construct sets$B _ { 1 } , \ldots , B _ { q }$of cardinality at least$2 ^ { - 1 8 8 \bar { 2 } } \gamma ^ { 9 3 1 2 } \theta ^ { 1 1 6 5 } N$and homomorphisms$\phi _ { i } : B _ { i } \to \mathbb { Z } _ { N }$of order 8, such that the graph of each $\phi _ { i }$is contained in$\Gamma ,$, these graphs are disjoint and there is a set$J \subset \mathbb { Z } _ { N }$ of size at least$( 1 - \theta ) N$such that$x \in J$and$( x , y ) \in \Gamma$implies that $y = \phi _ { i } ( x )$for some i. Moreover, the upper bound on the size of Γ implies that$q \leqslant 2 ^ { 1 8 8 2 } \gamma ^ { - 9 3 1 4 } \theta ^ { - 1 1 6 5 }$

Now let$P$be an arithmetic progression (or a one-dimensional box). By Corollary 7.11, with$\alpha = 2 ^ { - 1 8 8 2 } \gamma ^ { 9 3 \bar { 1 2 } } \theta ^ { 1 1 6 5 }$and$q$as above, we can partition $P$into subprogressions$Q _ { 1 } , \ldots , Q _ { M }$, each of size at least$| P | ^ { 2 ^ { - 1 4 } \alpha ^ { 2 } q ^ { - 1 } } \geqslant$ $| P | ^ { 2 ^ { - 6 0 0 0 } \gamma ^ { 3 0 0 0 0 } \theta ^ { \mathrm { { 1 5 0 0 0 } } } }$such that the restriction of each$\phi _ { i }$to each$B _ { i } \cap Q _ { j }$is linear. It is not hard to check that these numbers do indeed demonstrate that$\Gamma \cap ( J \times \mathbb { Z } _ { N } )$is$( \gamma , \gamma ^ { - 2 } s ( \theta , \gamma , 1 ) ) ,$)-multiply linear.✷

We are now ready to begin the inductive argument in earnest.

Lemma 16.4. Suppose that Theorem 16.2 is true for k. Let$\theta > 0$and let$\Gamma \subset \mathbb { Z } _ { N } ^ { k + 1 } \times \mathbb { Z } _ { N }$be a set of cardinality at most$\gamma ^ { - 2 } N ^ { k + 1 }$satisfying the product property with parameter$\gamma$. Then either there is a set$H \subset \mathbb { Z } _ { N } ^ { k + 1 }$ of cardinality less than$\theta N ^ { k + 1 }$such that$\Gamma \subset H \times \mathbb { Z } _ { N }$, or one can find a set $B \subset \mathbb { Z } _ { N } ^ { k + 1 }$and a function$\phi : B \to \mathbb { Z } _ { N }$with the following properties:

(i) the restriction of$\phi$to any proper cross-section of$B$is $( \gamma , \gamma ^ { - 2 } s ( 2 ^ { - ( k + 2 ) } \theta , \gamma , k ) )$-multiply multilinear;

(ii) B contains at least$( \theta \gamma ) ^ { 2 ^ { 2 ^ { k + 5 } } } N ^ { 1 7 k + 1 5 }$8-arrangements;

(iii) of the 8-arrangements in$B _ { i }$, the proportion respected by$\phi$is at least $1 - 2 ^ { - 4 4 }$

Proof. If the first alternative does not hold, then we can find a set$A \subset$ $\mathbb { Z } _ { N } ^ { k + 1 }$of cardinality at least$\theta N ^ { k + 1 }$and a function$\phi : A  \mathbb { Z } _ { N }$such that $( x , \phi ( x ) ) \in \Gamma$for every$x \in A$. Then$\phi$has the γ-product property. In fact, so does the restriction of$\phi$to any cross-section of A of the form $A _ { X , z } = \{ x \in A : x _ { i } = z _ { i }$for every$i \in X \}$. (This follows directly from the definition.) Let$\zeta = 2 ^ { - ( k + 2 ) } \theta$, let$l \leqslant k$and let$A _ { X , z }$be an l-dimensional cross-section of A of cardinality$\beta N ^ { l }$. By the inductive hypothesis, there is a subset$A _ { X , z } ^ { \prime } \subset A _ { X , z }$of cardinality at least$( \beta - \zeta ) N ^ { l }$such that the restriction of$\phi$to$A _ { X , z } ^ { \prime }$is$( \gamma , \gamma ^ { - 2 } s ( \zeta , \gamma , l ) ) ,$)-multiply l-linear.

For any given set$X \subset [ k + 1 ]$of size$k + 1 - l$, there are$N ^ { k + 1 - l }$diferent cross-sections$A _ { X , z }$, which partition A. Therefore, we can find a subset $A ^ { \prime } \subset A$of cardinality at least$( \theta - \zeta ) N ^ { k + 1 }$, such that the restriction of$\phi$to any cross-section of$A ^ { \prime }$in direction X is$( \gamma , \gamma ^ { - 2 } s ( \zeta , \gamma , k ) ) ,$)-multiply l-linear. Repeating this argument for all the$2 ^ { k + 1 } - 1$non-empty sets$X \subset [ k + 1 ]$小，we can find a subset$A ^ { \prime \prime } \subset A$of cardinality at least$\theta N ^ { k + 1 } / 2$such that the restriction of$\phi$to any proper cross-section of$A ^ { \prime \prime }$is$( \gamma , \gamma ^ { - 2 } s ( \zeta , \gamma , k ) )$ multiply multilinear of the appropriate dimension.

As remarked just before the statement of the lemma, this property is preserved if we pass to a subset of$A ^ { \prime \prime }$. We now do precisely that, using Lemma 15.6 to find a subset$B$of$A ^ { \prime \prime }$containing at least$( \theta \gamma / 2 ) ^ { 2 ^ { 2 ^ { k + 5 } } } N ^ { 1 7 k + 1 5 }$ 8-arrangements, such that the proportion of them respected by$\phi$is at least $1 - 2 ^ { - 4 4 }$. The lemma is now proved.✷

For any$h _ { 1 } , \ldots , h _ { k } , x .$, let$X _ { h _ { 1 } , \ldots , h _ { k } } ( x )$be the set of all cubes with sidelengths$( h _ { 1 } , \ldots , h _ { k } )$in the cross-section$B _ { x }$of$B .$. Let$X _ { h _ { 1 } , \ldots , h _ { k } }$be the union of these sets. Then$X _ { h _ { 1 } , \ldots , h _ { k } }$is a domain (in the sense of$\ S 1 0$, under the splitting into the sets$X _ { h _ { 1 } , \ldots , h _ { k } } ( x ) )$). For the rest of this section, we shall frequently abbreviate$( h _ { 1 } , \ldots , h _ { k } )$by$h ,$, as we did in$\ S 1 4 .$. If we let$f$be the characteristic function of$B ,$, then it is easy to see from the definition of the function$f _ { h }$(given just before Lemma 14.3) that$f _ { h } ( y )$is the number of cubes with sidelengths$( h _ { 1 } , \ldots , h _ { k } ) = h$in the cross-section$B _ { y }$, or in other words the cardinality of$X _ { h } ( y )$. For each$\boldsymbol { h } = \left( h _ { 1 } , \ldots , h _ { k } \right)$, let$C ( h )$ be the number of 8-arrangements in B made out of cubes with sidelengths $( h _ { 1 } , \ldots , h _ { k } )$. Let$G ( h )$be the number of these that are respected by$\phi .$. Recall from just before Lemma 14.4 that any function$\phi : \mathbb { Z } _ { N } ^ { k \bar { + } 1 } \to \mathbb { Z } _ { N }$induces a function (which we also call$\phi )$on$X _ { h }$

We shall write$\theta _ { 1 }$for the number$( \theta \gamma / 2 ) ^ { 2 ^ { 2 ^ { k + 5 } } }$that appeared in the last lemma. Recall that the Bohr neighbourhood$B ( K , \zeta )$is defined to be the set of all$s \in \mathbb { Z } _ { N }$such that$| r s | \leqslant \zeta N$for every$r \in K$. Given a function$\phi$ defined on a domain$( Z , r )$and a subset$B \subset \mathbb { Z } _ { N }$with$B = - B$, we shall say that$\phi$is a B-homomorphism if there is a Freiman homomorphism$\psi : B \to$ $\mathbb { Z } _ { N }$such that$\phi ( x ) - \phi ( y ) = \psi ( r ( x ) - r ( y ) )$whenever$r ( x ) - r ( y ) \in B$. (This generalizes to multifunctions the definition given just after Corollary 7.9.) Thus, the conclusion of Theorem 10.13 is that$\phi$restricted to Y is a Chomomorphism.

Lemma 16.5. Let$( B , \phi )$be a pair satisfying conditions$( \mathrm { i } ) , \ ( \mathrm { i } \mathrm { i } )$and (iii) of Lemma 16.4 and let$f$be the characteristic function of B. Then there exists a set$H \subset \mathbb { Z } _ { N } ^ { k }$such that$\begin{array} { r } { \sum _ { h \in H } C ( h ) \ \geqslant \ ( \theta _ { 1 } / 4 ) N ^ { 1 7 k + 1 5 } } \end{array}$with the following property. For every$h \in H$there is a set$Y _ { h } \subset X _ { h }$of cardinality at least$2 ^ { - 2 2 } \theta _ { 1 } ^ { 6 } | X _ { h } |$such that the restriction of$\phi$to$Y _ { h }$is a$B ( K _ { h } , \zeta ) \cdot$ homomorphism, where

$$
K _ {h} = \left\{r \in \mathbb {Z} _ {N}: | \hat {f} _ {h} (r) | \geqslant 2 ^ {- 3 7} (\theta_ {1} / 4) ^ {1 1 / 2} N ^ {k + 1} \right\}
$$

and$\zeta = 2 ^ { - s ( \theta , \gamma , k ) }$

Proof. We continue to write$\eta$for the number$2 ^ { - 4 4 }$. Since$\phi$respects a proportion of at least$1 - \eta$of the 8-arrangements of$B .$, of which there are at least$\theta _ { 1 } N ^ { 1 7 k + 1 5 }$, we may deduce that

$$
\sum \{C (h): G (h) \geqslant (1 - 2 \eta) C (h) \} \geqslant \frac {1}{2} \sum C (h) \geqslant (\theta_ {1} / 2) N ^ {1 7 k + 1 5}.
$$

Another simple averaging argument shows that

$$
\sum \left\{C (h): G (h) \geqslant (1 - 2 \eta) C (h), C (h) \geqslant (\theta_ {1} / 4) N ^ {1 6 k + 1 5} \right\} \geqslant (\theta_ {1} / 4) N ^ {1 7 k + 1 5}
$$

Let H be the set of all$h \in \mathbb { Z } _ { N } ^ { k }$such that$G ( h ) \geqslant ( 1 - 2 \eta ) C ( h )$and$C ( h ) \geqslant$ $( \theta _ { 1 } / 4 ) N ^ { 1 6 k + 1 5 }$, and note that our estimate for$\textstyle \sum _ { h \in H } C ( h )$implies that$H$ has cardinality at least$\theta _ { 1 } N ^ { k } / 4$

The statement that$G ( h ) \geqslant ( 1 - 2 \eta ) C ( h )$is equivalent to the statement that the function induced by$\phi$on$X _ { h }$is a$( 1 - 2 \eta )$-homomorphism of order eight. We know that$X _ { h } ( y )$has cardinality at most$N ^ { k }$for each$y ,$and it is not hard to show that if$C ( h ) \geqslant ( \theta _ { 1 } / 4 ) N ^ { 1 6 k + 1 5 }$then the cardinality of$X _ { h }$ is at least$\theta _ { 1 } N ^ { k + 1 } / 4$. Therefore, for every$h \in H$we may apply Theorem 10.13 (with$\alpha = \theta _ { 1 } / 4$and$g = f _ { h } )$and find a subset$Y _ { h } \subset X _ { h }$of cardinality at least$2 ^ { - 1 6 } \theta _ { 1 } ^ { 3 } | X _ { h } |$such that the restriction of$\phi$to$Y _ { h }$is a$B ( K _ { h } , \zeta ) .$ homomorphism, where$\zeta$is determined (as a function of$\theta )$by the equations $\theta _ { 1 } = ( \theta \gamma / 2 ) ^ { 2 ^ { 2 ^ { k + 5 } } } , \alpha = \theta _ { 1 } / 4 , k _ { 0 } = 2 ^ { 7 4 } \alpha ^ { - 1 0 }$and$\zeta = 2 ^ { - 1 5 5 k _ { 0 } } \alpha ^ { 1 8 k _ { 0 } } k _ { 0 }$. It can be checked that the resulting number$\zeta$exceeds$2 ^ { - s ( \theta , \gamma , k ) }$✷

From the definition of a$B ( K _ { h } , \zeta )$-homomorphism, we know in particular that, for any$x \in \mathbb { Z } _ { N }$and any$h \in H$, the restriction of$\phi$to$Y _ { h } ( x )$is constant. Let us write$\phi ^ { \prime } ( h , x )$for this value, when it is defined. Corollary 10.14 tells us that if$d \in B ( K _ { h } , \zeta / l )$then the restriction of$\phi ^ { \prime } ( h , . )$to any arithmetic progression with common diference d and length at most l is linear. This fact will be used in the next lemma. We shall also adopt the convention that if a box in$\mathbb { Z } _ { N } ^ { k + 1 }$is written as a Cartesian product$A \times B$ then A and B are boxes in$\mathbb { Z } _ { N } ^ { \bar { k } }$and$\mathbb { Z } _ { N }$respectively.

Let$\delta = 2 ^ { - 3 7 } ( \theta _ { 1 } / 4 ) ^ { 1 1 / 2 }$and define$\Delta \subset \mathbb { Z } _ { N } ^ { k } \times \mathbb { Z } _ { N }$to be the set of all$( h , r )$ such that$| \hat { f } _ { h } ( r ) | \geqslant \delta N ^ { k + 1 }$, that is, such that$r \in K _ { h }$. Lemma 14.3 tells us that$\Delta$has the product property with parameter δ. Therefore, if Theorem $1 6 . 2$is true for k, then there is a subset$J \subset \mathbb { Z } _ { N } ^ { k }$of size at least$( 1 - \theta _ { 1 } / 8 ) N ^ { k }$ such that$\Delta _ { 1 } = \Delta \cap ( J \times \mathbb { Z } _ { N } )$is$( \delta , \delta ^ { - 2 } s ( \theta _ { 1 } / \bar { 8 } , \delta , k ) )$-multiply k-linear. Let ${ \cal H } _ { 1 } = { \cal H } \cap { \cal J } .$, where H is the set defined in the proof of Lemma 16.5. Since $\begin{array} { r } { \sum _ { h \not \in J } C ( h ) \leqslant ( \theta _ { 1 } / 8 ) N ^ { 1 7 k + 1 5 } } \end{array}$, we find that$\begin{array} { r } { \sum _ { h \in H _ { 1 } } C ( h ) \geqslant ( \theta _ { 1 } / 8 ) N ^ { 1 7 k + 1 5 } } \end{array}$

Before we state and prove the next lemma, let us remark that the definition of the set$\Delta$above is in a sense the moment where the induction takes place. For any given$h ,$there are at most$\delta ^ { - 2 }$values of$r$such that $( h , r ) \in \Delta$, so$\Delta$is the union of the graphs of at most$\delta ^ { - 2 }$functions. We have therefore managed once again to reduce the number of variables by one by considering a new function which tells us where some Fourier coefficients related to the domain of the old function are large. The results of the previous two sections together with the inductive hypothesis have told us that the new function has a lot of structure; this will now be used to tell us about the old function, which will complete the inductive step.

Lemma 16.6. Let$P = Q \times I$be a box in$\mathbb { Z } _ { N } ^ { k + 1 }$of width at least$m ,$, let $t = \delta ^ { - 2 } s ( \theta _ { 1 } / 8 , \delta , k )$, let$\sigma > 0$and let$l = ( \zeta / 2 ) m ^ { c ( t ^ { - 1 } \sigma , \delta , k ) ^ { t } / 2 K ^ { 2 ^ { k + 1 } q } }$. Then there is a subset$G \subset Q$of size at least$( 1 - \sigma ) | Q |$and a partition of$P$into boxes$S _ { u } = T _ { u } \times J _ { u }$of width at least l, such that, for every u and every $h \in G \cap H _ { 1 } \cap T _ { u }$, the function from$J _ { u }$to$\mathbb { Z } _ { N }$defined by$x \mapsto \phi ^ { \prime } ( h , x )$is linear.

Proof. Because$\Delta _ { 1 }$is$( \delta , t )$-multiply k-linear, we can find a subset$G \subset Q$of size at least$( 1 - \sigma ) | Q |$and a partition of$Q$into subboxes$Q _ { j }$of width at least $m _ { 1 } = m ^ { c ( \sigma / t , \delta , k ) ^ { t } }$such that for each$j$there are k-linear functions$\mu _ { 1 } , \ldots , \mu _ { q }$ from$Q _ { j }$to$\mathbb { Z } _ { N }$, with$q \leqslant q ( \sigma / t , \delta , k ) ^ { t }$such that$\Delta _ { 1 } \cap \left( \left( G \cap Q _ { j } \right) \times \mathbb { Z } _ { N } \right)$is contained in the union of the graphs of the$\mu _ { i }$ . This says that, for any $h \in G \cap Q _ { j }$, the set$K _ { h } = \{ r \in \mathbb { Z } _ { N } : | { \widehat f } _ { h } ( r ) | \geqslant \delta N ^ { k + 1 } \}$is a subset of $\{ \mu _ { 1 } , \ldots , \mu _ { q } \}$

By Lemma 16.1, each$Q _ { j }$may be partitioned into subboxes$R _ { t }$of width at least$m _ { 2 } = m _ { 1 } ^ { 1 / K ^ { 2 ^ { k + 1 } q } } \geqslant l ^ { 2 }$and common diference$d _ { t }$such that, given any $h \in R _ { t }$and any$i , | \mu _ { i } ( h ) d _ { t } | \leqslant 2 m _ { 1 } ^ { - 1 / K ^ { 2 ^ { k + 1 } q } } \leqslant \zeta N / ( l + 1 )$. By the conclusion of the last paragraph, this implies that, whenever$h \in G \cap R _ { t } , d _ { t }$belongs to the Bohr neighbourhood$B ( K _ { h } , \zeta / ( l + 1 ) )$. For each t,$R _ { t } \times I$can be partitioned into boxes$S _ { u } = T _ { u } \times J _ { u }$of width l or$l + 1$. As remarked after the statement of Lemma 16.5, the restriction of$\phi ^ { \prime } ( h , . )$to an arithmetic progression with common diference$d \in B ( K _ { h } , \zeta / ( l + 1 ) )$and length at most$l + 1$is linear. In other words, the function from$J _ { u }$to$\mathbb { Z } _ { N }$defined by $x \mapsto \phi ^ { \prime } ( h , x )$is linear, as stated.✷

Notice that it was vital in the above lemma that$\Delta _ { 1 }$should have good structure and that this should give us information, via Fourier coeficients, about the restriction of$\phi$to the sets$Y _ { h }$, even though the definition of$\Delta _ { 1 }$ was in terms of the$X _ { h }$. It was to achieve this that we worked so hard in §10.

Lemma 16.7. Let$\theta _ { 2 } = 2 ^ { - 2 1 } \theta _ { 1 } ^ { 5 }$Then there exist elements$x _ { 1 } , \ldots , x _ { k }$of $\mathbb { Z } _ { N }$such that, for at least$\theta _ { 2 } N ^ { k + 1 }$choices of$( h _ { 1 } , \ldots , h _ { k } , x )$with$h \in H _ { 1 }$，$\phi ^ { \prime } ( h , x )$is defined and equals

$$
\sum_ {\epsilon \in \{0, 1 \} ^ {k}} (- 1) ^ {| \epsilon |} \phi (x _ {1} + \epsilon_ {1} h _ {1}, x _ {2} + \epsilon_ {2} h _ {2}, \dots , x _ {k} + \epsilon_ {k} h _ {k}, x).
$$

Proof. The expression given for$\phi ^ { \prime } ( h , x )$is valid whenever$Y _ { h } ( x )$contains the cube$[ x _ { 1 } , \dots , x _ { k } ; h _ { 1 } , \dots , h _ { k } ]$. Since$| H _ { 1 } | \geqslant ( \theta _ { 1 } / 8 ) N ^ { k }$and$| X _ { h } | \geqslant$ $( \theta _ { 1 } / 4 ) N ^ { k + 1 }$for every$h \in H _ { 1 }$, we find that$\begin{array} { r l r } { \mathrm { ~ } } & { { } } & { \sum _ { h \in { \cal H } } | Y _ { h } | \geqslant 2 ^ { - 2 1 } \theta _ { 1 } ^ { 5 } N ^ { 2 k + 1 } = } \end{array}$ $\dot { \theta } _ { 2 } \dot { N } ^ { 2 k + 1 }$(by the estimate for the sizes of the sets$Y _ { h }$in Lemma 16.5). Therefore, if we choose the$x _ { j }$randomly, the expected number of choices of $( h _ { 1 } , \ldots , h _ { k } , x )$with$h \in H _ { 1 }$for which the equality holds is at least$\theta _ { 2 } N ^ { k + 1 }$ The lemma follows.✷

Lemma 16.8. Suppose that$\Gamma _ { 1 } , \ldots , \Gamma _ { r }$are$( \gamma , s )$-multiply$( k + 1 )$-linear subsets of$\mathbb { Z } _ { N } ^ { k + 1 } \times \mathbb { Z } _ { N }$. Then$\Gamma _ { 1 } \cup \dots \cup \Gamma _ { r }$is (γ, rs)-multiply (k + 1)-linear. $I f \phi _ { 1 } , \ldots , \phi _ { r }$are$( \gamma , s )$-multiply$( k + 1 )$-linear functions defined on a subset $B \subset \mathbb { Z } _ { N } ^ { k + 1 }$, then$\phi _ { 1 } + \cdot \cdot \cdot + \phi _ { r }$is$( \gamma , r s )$-multiply (k + 1)-linear.

Proof. Let P be a box. We can find a subset$H _ { 1 } ~ \subset ~ P$of size at least $( 1 - \theta / r s ) | P |$and a partition of P into boxes$Q$of width at least $\dot { m } ^ { c ( ( r s ) ^ { - 1 } \theta , \gamma , k ) ^ { s } }$such that$\Gamma _ { 1 }$restricted to any$Q \cap H _ { 1 }$is contained in the union of the graphs of$q ( ( r s ) ^ { - 1 } \theta , \gamma , k , ) ^ { s }$multilinear functions. Now repeat this argument inside each$Q$for the set$\Gamma _ { 2 }$and so on. At each of the r stages of this process, the width of the boxes is raised to the power $c ( ( r s ) ^ { - 1 } \theta , \gamma , k ) ^ { s }$, the number of new multilinear functions introduced inside each box is at most$q ( ( r s ) ^ { - 1 } \theta , \gamma , k ) ^ { s }$and$\theta | P | / r s$points are thrown away. Therefore, at the end of the process we have a width of at least $m ^ { c ( \check { ( } r s ) ^ { - 1 } \theta , \gamma , k ) ^ { r s } }$and$r q ( ( r s ) ^ { - 1 } \theta , \gamma , k ) ^ { s }$multilinear functions for each set$\Gamma _ { i }$ The result about unions follows (and in fact we have overestimated the number of multilinear functions needed). The result for sums of functions also follows, once we notice that there are$q ( ( r s ) ^ { - 1 } \theta , \gamma , k ) ^ { r s }$functions of the form$\mu _ { 1 } + \cdots + \mu _ { r }$, with each$\mu _ { i }$one of the multilinear functions chosen at the$i ^ { \mathrm { t h } }$stage.✷

Let us now fix a choice of$x _ { 1 } , \ldots , x _ { k }$satisfying the conclusion of Lemma 16.7 and write$\phi _ { \epsilon } ( h , x )$for$\phi ( x _ { 1 } + \epsilon _ { 1 } h _ { 1 } , \dots , x _ { k } + \epsilon _ { k } h _ { k } , x )$. Write also$\phi _ { 1 } ( h , x )$for the function$\phi _ { \epsilon } ( h , x )$when$\epsilon = ( 1 , 1 , \dots , 1 )$Regard all these functions as being defined on the set$B _ { 1 }$of$( h , x )$that satisfy the conclusion of Lemma 16.7, which can be rephrased as$\phi _ { 1 } ( h , x ) \ =$ $\begin{array} { r } { \phi ^ { \prime } ( h , x ) - \sum _ { \epsilon \neq 1 } ( - 1 ) ^ { | \epsilon | } \phi _ { \epsilon } ( h , x ) } \end{array}$and$h \in H _ { 1 }$. We now show that something like Lemma 16.6, but weaker, holds for the function$\phi _ { 1 }$as well.

Lemma 16.9. Let$t = \delta ^ { - 2 } s ( \theta _ { 1 } / 8 , \delta , k ) , r = ( 2 ^ { k } - 1 ) \gamma ^ { - 2 } s ( 2 ^ { - ( k + 2 ) } \theta , \gamma , k )$and $q = q ( \gamma , \sigma / 2 r , k ) ^ { r }$. Let$P = Q \times I$be any box in$\mathbb { Z } _ { N } ^ { k + 1 }$of width at least m and let$\sigma > 0$. Then there is a subset$E \subset P$of size at least$( 1 - \sigma ) | P |$and a partition of$P$into boxes$S _ { u } = T _ { u } \times J _ { u }$with the following property. Given u and$h \in T _ { u }$let$\psi _ { u , h }$be the function$x \mapsto \phi _ { 1 } ( h , x )$, where the domain is the set of all x such that$( h , x ) \in B _ { 1 } \cap E \cap S _ { u }$. Then for every u and$h \in T _ { u }$ the graph of$\psi _ { u , h }$is contained in the union of the graphs of at most$q$linear functions. The width of each box$S _ { u }$is at least

$$
l = (\zeta / 2 C _ {k + 1}) m ^ {c (\sigma / 2 r, \gamma , k) ^ {r} c (\sigma / 2 t, \delta , k) ^ {t} / 2 K ^ {2 ^ {k + 1} q}}.
$$

Proof. Given any sequence$\epsilon \in \{ 0 , 1 \} ^ { k }$apart from$( 1 , 1 , \ldots , 1 )$, let$X = \{ j :$ $\epsilon _ { j } = 0 \}$and let$B _ { \epsilon }$be the cross-section of B defined as the set of all$y \in B$ such that$y _ { j } = x _ { j }$for every$j \in X$. By property (i) of Lemma 16.4, the restriction of$\phi$to the cross-section$B _ { \epsilon }$is$( \gamma , \gamma ^ { - 2 } s ( 2 ^ { - ( k + 2 ) } \theta , \gamma , k ) )$)-multiply multilinear. It follows easily that$\phi _ { \epsilon }$itself is$( \gamma , \gamma ^ { - 2 } s ( 2 ^ { - ( k + 2 ) } \theta , \gamma , k ) )$ multiply$( k + 1 )$)-linear, since$\phi _ { \epsilon }$is obtained from the restriction of φ by introducing variables that make no diference, namely the$h _ { i }$with$i \in X$

Hence, by Lemma 16.8 and the expression for$\phi _ { 1 }$just before the statement of this lemma, we can write

$$
\phi_ {1} (h, x) = \phi^ {\prime} (h, x) + \phi^ {\prime \prime} (h, x),
$$

where$\phi ^ { \prime \prime }$is$( \gamma , r )$-multiply (k+1)-linear. By the definition of$( \gamma , r )$-multiple multilinearity, we can find a subset$F \subset P$of cardinality at least$( 1 - \sigma / 2 ) | P |$ and a partition of$P$into boxes$P _ { j }$of width at least$m _ { 1 } = m ^ { c ( ( 2 r ) ^ { - 1 } \sigma , \gamma , k ) ^ { r } }$ such that for every$j$there are$( k + 1 )$-linear functions$\mu _ { 1 } , \ldots , \mu _ { q }$from$P _ { j }$ to$\mathbb { Z } _ { N }$with the property that$\phi ^ { \prime \prime } ( h , x ) \ : = \ : \mu _ { i } ( h , x )$for some i, whenever $( h , x ) \in B _ { 1 } \cap F \cap P _ { j }$

By Lemma 16.6, each of the boxes$P _ { j } = Q _ { j } \times I _ { j }$gives a subset$G _ { j } \subset Q _ { j }$of size at least$( 1 - \sigma / 2 ) | Q _ { j } |$and a further partition into boxes$S _ { j u } = T _ { j u } \times J _ { j u }$ of width at least$m _ { 2 } = ( \zeta / 2 C _ { k + 1 } ) m _ { 1 } ^ { c ( ( 2 t ) ^ { - 1 } \sigma , \delta , k ) ^ { t } / 2 { K ^ { 2 } } ^ { k + 1 } q }$such that for every $h \in H _ { 1 } \cap G _ { j } \cap T _ { j u }$(recall that$( h , x ) \in B _ { 1 }$implies that$h \in H _ { 1 }$, which was defined just before the statement of Lemma 16.6), the restriction of$\phi ^ { \prime } ( h , x )$ to$B _ { 1 } \cap S _ { j u }$is linear in x. The lemma now follows on adding$\phi ^ { \prime }$and$\phi ^ { \prime \prime }$and taking E to be$F \cap \bigcup _ { j } ( G _ { j } \times I _ { j } )$✷

We have just shown that$\phi _ { 1 }$has a property similar to multiple multi-linearity but much weaker because it gives us linearity only in one of the variables. However, we also have information about the restriction of$\phi _ { 1 }$to proper cross-sections, and this enables us to show that the linear functions in the final variable are related to each other in a multilinear way. The details are in the next lemma.

Lemma 16.10. The function$\phi _ { 1 }$is itself$( \gamma , 1 )$-multiply (k + 1)-linear.

Proof. We begin by remarking that, since$\phi _ { 1 }$is a translation of a restriction of$\phi ,$property (i) of Lemma 16.4 implies that the restriction of$\phi _ { 1 }$to any cross-section of$B _ { 1 }$formed by fixing the final variable x is $( \gamma , \gamma ^ { - 2 } s ( 2 ^ { - ( k + 2 ) } \theta , \gamma , k ) )$-multiply multilinear of the appropriate dimension.

Now let$\rho > 0$, let$\sigma = \rho / 4$and let$P = Q \times I$be a box of width at least m. Applying Lemma 16.9, we can find a subset$E \subset P$of size at least $( 1 - \sigma ) | P |$and a partition of$P$into boxes$S _ { u } = T _ { u } \times J _ { u }$of width at least l satisfying the conclusion of that lemma. Let$S = T \times J$be one of these boxes, and write$B _ { 1 } ( h )$for the set$\{ ( h ^ { \prime } , x ) \in B _ { 1 } \cap E \cap S : h ^ { \prime } = h \}$. Each set$B _ { 1 } ( h )$can be partitioned into subsets$C _ { 1 } ( h ) , \ldots , C _ { q } ( h )$such that the restriction of$\phi _ { 1 }$to any$C _ { t } ( h )$is linear. An easy averaging argument shows thatq

$$
\sum_ {j = 1} ^ {q} \sum_ {h \in S} \left\{\left| C _ {t} (h) \right|: \left| C _ {t} (h) \right| \geqslant \sigma | J | / q \right\} \geqslant (1 - \sigma) | S |.
$$

Hence, there is a subset$D \subset S$of size at least$( 1 - \sigma ) | S |$such that, for every t,$C _ { t } ( h ) \cap D$is either empty or of size at least$\sigma | J | / q$

Now let$r = q \sigma ^ { - 2 }$and choose$x _ { 1 } , \ldots , x _ { r }$randomly from$J . \mathrm { ~ I f ~ } | C _ { t } ( h ) | \geqslant$ $\sigma | J | / q$, then the probability that$C _ { t } ( h )$does not contain two distinct points $( h , x _ { i } )$and$( h , x _ { j } )$is at most$( 1 - \sigma / q ) ^ { r } + r ( \sigma / q ) ( 1 - \sigma / q ) ^ { r - 1 }$, which is much smaller than$\sigma .$If we discard every set$C _ { t } ( h )$which does not contain such a distinct pair, then the expected number of points discarded is at most σ times the total number of points in the$C _ { t } ( h )$, which is certainly at most $\sigma | S |$. Hence, we can choose$x _ { 1 } , \ldots , x _ { r }$and find a set$F \subset S$of size at least $( 1 - \sigma ) | S |$such that for every$h , t$and every$( h , x ) \in C _ { t } ( h ) \cap D \cap F$there are$x _ { i }$and$x _ { j }$not the same with$( h , x _ { i } )$and$( h , x _ { j } )$both in$C _ { t } ( h ) \cap D \cap F$ as well.

For any fixed$h , t ,$, there are constants$\lambda _ { t } ( h )$and$\mu _ { t } ( h )$such that$\phi _ { 1 } ( h , x )$ $= \lambda _ { t } ( h ) x + \mu _ { t } ( h )$for every$( h , x ) \in C _ { t } ( h )$. If in addition$x _ { i } \neq x _ { j }$and$( h , x _ { i } )$ and$( h , x _ { j } )$both belong to$C _ { t } ( h )$, then$\lambda _ { t } ( h ) x _ { i } + \mu _ { t } ( h ) \ : = \ : \phi _ { 1 } ( h , x _ { i } )$and $\lambda _ { t } ( h ) x _ { j } + \mu _ { t } ( h ) = \phi _ { 1 } ( h , x _ { j } )$. These equations imply that

$$
\lambda_ {t} (h) = \left(x _ {i} - x _ {j}\right) ^ {- 1} \left(\phi_ {1} \left(h, x _ {i}\right) - \phi_ {2} \left(h, x _ {j}\right)\right),
$$

which we shall denote by$\lambda _ { i j } ( h )$, and that

$$
\mu_ {t} (h) = \phi_ {1} (h, x _ {i}) - \lambda_ {i j} (h) x _ {i},
$$

which we shall denote by$\mu _ { i j } ( h )$. By Lemma 16.8 and the remark with which we opened the proof, the functions$\lambda _ { i j }$and$\mu _ { i j }$are all$( \gamma , 2 \gamma ^ { - 2 } s ( 2 ^ { - ( k + 2 ) } \theta , \gamma , k ) )$ multiply multilinear, and for every$( h , x ) \in B _ { 1 } \cap E \cap D \cap F$we can find$i , j$ such that$\phi _ { 1 } ( h , x ) = \lambda _ { i j } ( h ) x + \mu _ { i j } ( h )$

It is not hard to see (using Lemma 16.8 again) that$\lambda _ { i j } ( h ) x + \mu _ { i j }$is a$( \gamma , 4 \gamma ^ { - 2 } s ( 2 ^ { - ( k + 2 ) } \theta , \gamma , k ) )$)-multiply multilinear function of$( h , x )$, and, by one further application of Lemma 16.8, the union of the graphs of all these functions, which contains the graph of$\phi _ { 1 }$restricted to$B _ { 1 } \cap E \cap D \cap F$, is $( \gamma , 4 r ^ { 2 } \gamma ^ { - 2 } s ( 2 ^ { - ( k + 2 ) } \theta , \gamma , k ) )$-multiply multilinear.

Let$p = 4 r ^ { 2 } \gamma ^ { - 2 } s ( 2 ^ { - ( k + 2 ) } \theta , \gamma , k )$. By what we have just shown, there is a subset$G \subset S$of size at least$( 1 - \sigma ) | S |$and a partition of S into boxes$V$of width at least$l ^ { c ( \gamma , \sigma / p , k ) ^ { p } }$such that for each one the graph of$\phi _ { 1 }$restricted to$V \cap E \cap D \cap F \cap G$is contained in the union of the graphs of$q ( \sigma / p , \gamma , k ) ^ { p }$ multilinear functions.

To complete the proof of the lemma, it is necessary only to check that $q ( \sigma / p , \gamma , k ) ^ { p } \leqslant q ( \rho , \gamma , k + 1 )$and that$l ^ { c ( \sigma / p , \gamma , k ) ^ { p } } \geqslant \dot { m ^ { c ( \rho , \gamma , k + 1 ) } }$. This is a back-of-envelope calculation left to the reader.✷

Proof of Theorem 16.2. Lemma 16.10 shows that if the result is true for k and$\Gamma \subset \mathbb { Z } _ { N } ^ { k + 1 } \times \mathbb { Z } _ { N }$has the product property with parameter$\gamma _ { : }$ then Γ has a$( \gamma , 1 )$-multiply$( k + 1 )$-linear subset of cardinality at least ${ \theta _ { 2 } N ^ { k + 1 } \geqslant N ^ { k + 1 } / s ( \theta , \gamma , k ) }$, if its projection has size at least$\theta N ^ { k + 1 }$. Now apply this result repeatedly, removing such sets from Γ until it no longer has a projection of size at least$\theta N ^ { k + 1 }$. Since$| \Gamma | \leqslant \gamma ^ { - 2 } N ^ { k + 1 }$, the number of sets removed is at most$\gamma ^ { - 2 } s ( \theta , \gamma , k )$. The result now follows from Lemma 16.8.✷

Corollary 16.11. If$f : \mathbb { Z } _ { N } \to D$fails to be α-uniform of degree$k + 1$ then there is a box$P \subset \mathbb { Z } _ { N } ^ { k }$of width at least$N ^ { ( \alpha / 2 ) ^ { 2 ^ { 2 ^ { k + 9 } } } }$and a multilinear function$\mu : P \to \mathbb { Z } _ { N }$such that, for at least$( \alpha / 2 ) ^ { 2 ^ { 2 ^ { k + 9 } } } | P |$values of $( y _ { 1 } , \ldots , y _ { k } )$, we have$| \Delta ( f ; y _ { 1 } , \ldots , y _ { k } ) ^ { \wedge } ( \mu ( y _ { 1 } , \ldots , y _ { k } ) ) | \geqslant ( \alpha / 2 ) N$

Proof. Since f is not α-uniform of degree$k + 1$, we find, using the implication of (ii) from (vi) in Lemma 3.1, that there is a set$B \subset \mathbb { Z } _ { N } ^ { k }$ of size at least$( \alpha / 2 ) N ^ { k }$and a function$\phi ~ : ~ B ~  ~ \mathbb { Z } _ { N }$such that $| \Delta ( f ; a _ { 1 } , \ldots , a _ { k } ) ^ { \Lambda } ( \phi ( a _ { 1 } , \ldots , a _ { k } ) ) | \geqslant ( \alpha / 2 ) N$for every$( a _ { 1 } , \dotsc , a _ { k } ) \ \in \ B$ Lemma 14.2 then implies that φ has the product property with parameter$\alpha / 2$. Next, Theorem 16.2 implies that B has a subset$C$of size at least $( \alpha / 4 ) N ^ { k }$such that the restriction of$\phi$to$C$is$( \alpha / 2 , r )$-multiply k-linear, where$r = 4 \alpha ^ { - 2 } s ( \alpha / 4 , \alpha / 2 , k )$. Applying the definition of multiple multi-linearity in the case where the box$P$is the whole of$\mathbb { Z } _ { N } ^ { k }$and$\theta = \alpha / 8$ we find a set$H \subset \mathbb { Z } _ { N } ^ { k }$of size at least$( 1 - \alpha / 8 ) N ^ { k }$and partition of$\mathbb { Z } _ { N } ^ { k }$ into boxes$P _ { 1 } , \dots , P _ { M }$of width at least$N ^ { c ( \alpha / \dot { 8 } r , \dot { \alpha } / 2 , k ) ^ { r } }$such that for every $j$the restriction of φ to$C \cap P _ { j } \cap H$is contained in the graph of at most $q ( \alpha / 8 r , \alpha / 2 , k ) ^ { r }$multilinear functions. By averaging, we can find a box$P _ { j }$ such that$| C \cap P _ { j } \cap H | \geqslant ( \alpha / 8 ) | P _ { j } |$. By further averaging, we can find a subset$D \subset P _ { j }$of size at least$( q ( \bar { \alpha } / 8 r , \alpha / 2 , k ) ^ { r } ) ^ { - 1 } ( \alpha / 8 ) | P _ { j } |$such that the restriction of$\phi$to$D$is multilinear. A straightforward calculation shows that this implies the corollary.✷

## 17 The Main Inductive Step

We are finally ready to generalize the argument of$\ S 8 .$, to complete a proof of Szemer´edi’s theorem for progressions of arbitrary length. It turns out that there is a second reason for this being harder than for progressions of length four, but fortunately it is much less serious than the dificulties we have dealt with in the last two sections.

To see the problem, let A be a set with balanced function f which fails to be cubically uniform. We know then that there are many pairs$( k , l )$ such that$\Delta ( f ; k , l )$has a large Fourier coeficient. The results of §9 show that the large Fourier coeficient has regions where it depends bilinearly on $( k , l )$. As at the beginning of §8, let us imagine that we actually have the best possible situation: that is, that we can find c such that

$$
\sum_ {k, l} | \Delta (f; k, l) ^ {\wedge} (6 c k l) | ^ {2} \geqslant \alpha N ^ {4},
$$

so that the dependence on (k, l) of where the large Fourier coeficient appears is genuinely bilinear.

Writing out the above inequality in full and making the usual substitution, we find that

$$
\sum_ {s} \sum_ {k, l, m} \Delta (f; k, l, m) (s) \omega^ {- 6 c k l m} \geqslant \alpha N ^ {4}.
$$

If we now use the identity

$$
6 k l m = \sum_ {\epsilon_ {1}, \epsilon_ {2}, \epsilon_ {3}} \left(s - \epsilon_ {1} k - \epsilon_ {2} l - \epsilon_ {3} m\right) ^ {3},
$$

where the sum is over the eight triples$( \epsilon _ { 1 } , \epsilon _ { 2 } , \epsilon _ { 3 } )$with$\epsilon _ { i } = 0$or 1, then, writing C once again for the operation of complex conjugation, we can deduce that

$$
\sum_ {s} \sum_ {k, l, m} \prod_ {\epsilon_ {1}, \epsilon_ {2}, \epsilon_ {3}} C ^ {\epsilon_ {1} + \epsilon_ {2} + \epsilon_ {3}} \left(f (s - \epsilon_ {1} k - \epsilon_ {2} l - \epsilon_ {3} m) \omega^ {- c (s - \epsilon_ {1} k - \epsilon_ {2} l - \epsilon_ {3} m) ^ {3}}\right) \geqslant \alpha N ^ {4}.
$$

Unfortunately, the standard trick that we applied in$\ S 8$(and of course many other places in the paper) of inserting a term$\omega ^ { - r ( a - \bar { b } - c + d ) }$simply does not have an equivalent here. (Indeed, if it did, then the whole paper would be far simpler.) So have we gained anything at all with the above manipulations? The answer is that we have, because the above inequality tells us precisely that the function$g ( s ) = f ( s ) \omega ^ { - c s ^ { 3 } }$is not quadratically α-uniform. Therefore, by the results of$\ S 8 , g$has plenty of quadratic bias, which tells us that there are many progressions$P$for which$\textstyle | \sum _ { s \in P } f ( s ) \omega ^ { \phi ( s ) } |$is large for some cubic polynomial$\phi$(depending on the progression). Finally, the results of §5 can be used to find a small progression where A is denser than it should be.

Of course, if we have only a small piece of bilinearity to work with, the argument above has to be modified a little, but the rough form of our inductive hypothesis, and indeed the rest of the proof, ought by now to be clear. Our first lemma is by no means new, but we state and briefly prove it, for the convenience of the reader.

Lemma 17.1. Let σ be any k-linear function$\left( o v e r \mathbb { Z } _ { N } \right)$in variables$x _ { 1 } , . . . , x _ { k }$ Then there are polynomials$\phi _ { \epsilon } ~ ( \epsilon \in \{ 0 , 1 \} ^ { k } )$of degree at most k giving the identity

$$
\phi (x _ {1}, \dots , x _ {k}) = \sum_ {\epsilon \in \{0, 1 \} ^ {k}} (- 1) ^ {| \epsilon |} \phi_ {\epsilon} (s - \epsilon . x).
$$

Proof. It is enough to prove the result in the case$\sigma ( x _ { 1 } , \dots , x _ { k } ) = x _ { 1 } \dots x _ { k }$ Now$s ^ { k } - ( s - x _ { 1 } ) ^ { k }$is a polynomial in s of degree$k - 1$with leading term $k x _ { 1 } s ^ { k - 1 }$. It follows that$s ^ { k } - ( s - x _ { 1 } ) ^ { k } - ( s - x _ { 2 } ) ^ { k } + ( s - x _ { 1 } - x _ { 2 } ) ^ { k }$is a polynomial in s of degree$k - 2$with leading term$k ( k - 1 ) x _ { 1 } x _ { 2 } s ^ { k - 2 }$ Continuing, we find that

$$
k! x _ {1} \dots x _ {k} = \sum_ {\epsilon \in \{0, 1 \} ^ {k}} (- 1) ^ {| \epsilon |} (s - \epsilon . x) ^ {k}
$$

as we wanted.

We now prove a proposition which is not exactly what we need later. Rather, it is a special case, which we give in the hope that the more general result, which is a bit complicated, will be easier to understand.

Proposition 17.2. Let$f : \mathbb { Z } _ { N } \to D$. Suppose that there is a k-linear function$\sigma : \mathbb { Z } _ { N } ^ { k }  \mathbb { Z } _ { N }$such that

$$
\sum_ {x \in \mathbb {Z} _ {N} ^ {k}} \left| \Delta (f; x) ^ {\wedge} (\sigma (x)) \right| ^ {2} \geqslant \alpha N ^ {k + 2}.
$$

Then there is a polynomial$\phi$of degree at most k such that, setting$g ( s ) =$ $f ( s ) \omega ^ { - \phi ( s ) }$, we have

$$
\sum_ {x \in \mathbb {Z} _ {N} ^ {k}} \left| \sum_ {s} \Delta (g; x) (s) \right| ^ {2} \geqslant \alpha N ^ {k + 2}.
$$

Proof. By Lemma 17.2 we may write

$$
x _ {k + 1} \sigma (x) = \sum_ {\epsilon \in \{0, 1 \} ^ {k + 1}} \phi_ {\epsilon} (s - \epsilon . x).
$$

We also have, for any$x \in \mathbb { Z } _ { N } ^ { k } .$

$$
\left| \Delta (f; x) ^ {\wedge} (\sigma (x)) \right| ^ {2} = \sum_ {s} \sum_ {y} \Delta (f; x, y) (s) \omega^ {- y \sigma (x)}.
$$

Therefore,

$$
\sum_ {x \in \mathbb {Z} _ {N} ^ {k}} \left| \Delta (f; x) ^ {\wedge} (\sigma (x)) \right| ^ {2} = \sum_ {x \in \mathbb {Z} _ {N} ^ {k + 1}} \sum_ {s} \sum_ {\epsilon \in \{0, 1 \} ^ {k + 1}} C ^ {| \epsilon |} \big (f (s - \epsilon . x) \omega^ {- \phi_ {\epsilon} (s - \epsilon . x)} \big).
$$

By Lemma 17.1, we can find some  such that the function$g ( s ) = f ( s ) \omega ^ { - \phi _ { \epsilon } ( s ) }$ satisfies the inequality

$$
\sum_ {x \in \mathbb {Z} _ {N} ^ {k + 1}} \sum_ {s} \Delta (g; x) (s) \geqslant \alpha N ^ {k + 2},
$$

which is equivalent to the inequality we want.

We must now deal with the fact that the results of the last two sections did not give us a k-linear function on the whole of$\mathbb { Z } _ { N } ^ { k }$, so the above proposition cannot be applied directly. We shall use another very standard and well known lemma. It is a reflection of the fact that the set of half-spaces in$\mathbb { R } ^ { k }$has VC-dimension at most$k ,$but the proof is elementary and we very briefly sketch it. The next three lemmas are not essential to our main argument, as their purpose is to improve the bound coming from a trivial argument, when using the trivial bound would have a negligible efect on our eventual estimates.

Lemma 17.4. The number of distinct regions defined by a set of m hyperplanes in$\mathbb { R } ^ { k }$is at most$\textstyle \sum _ { j = 0 } ^ { k } { \binom { m } { j } }$, with equality when the hyperplanes are in general position.

Proof. Apply induction on m, by considering how many new regions are created when each new hyperplane is added to the arrangement. To calculate this, use induction on k. The result is trivial when$k = 1$✷

Corollary 17.5. Given real numbers$\alpha _ { 1 } , \ldots , \alpha _ { k }$, set$\alpha = ( \alpha _ { 1 } , \ldots , \alpha _ { k } )$ and define a function$f : \{ 0 , 1 \} ^ { k } \to \mathbb { Z }$by$f ( \epsilon ) = \lfloor \epsilon . \alpha \rfloor$. If r is an integer and the$\alpha _ { i }$are allowed to vary in the interval$( - r , r ) _ { ; }$then the number of distinct such functions that can result is at most$2 ^ { 2 r k ^ { 3 } }$

Proof. The possible values taken by f are the integers between$\lfloor - r k \rfloor$and $\lfloor r k \rfloor$, and the set of  such that$f ( \epsilon ) \leqslant j$is the set of  such that$\epsilon . \alpha < j + 1$ Let us estimate how many distinct such sets can be obtained as α varies. Two real numbers α and$\alpha ^ { \prime }$give distinct sets if and only if there exists some  such that$\epsilon . \alpha < j + 1$and$\epsilon . \alpha ^ { \prime } \geqslant j + 1$, that is, if and only if the hyperplane$\{ \beta : \epsilon . \beta = j + 1 \}$separates α from$\alpha ^ { \prime } .$. There are$2 ^ { k }$diferent such hyperplanes, so the previous lemma tells us that the number of distinct sets of the given form is at most$k { \binom { 2 ^ { k } } { k } } \leqslant 2 ^ { k ^ { 2 } }$. The function$f$is determined by the$2 r k$sets$\{ \epsilon : f ( \epsilon ) \leqslant j \}$with$[ - k ^ { 2 } / 2 ] < j \leqslant \lfloor k ^ { 2 } / 2 \rfloor$, so the result follows.✷

Corollary 17.6. Let$\alpha _ { 0 } , \alpha _ { 1 } , \ldots , \alpha _ { k }$be real numbers, let$\alpha = ( \alpha _ { 1 } , \ldots , \alpha _ { k } )$ and define a function$f : \{ 0 , 1 \} ^ { k } \to \mathbb { Z } _ { M } b y f ( \epsilon ) = \lfloor \alpha _ { 0 } + \alpha . \epsilon \rfloor$(mod M). Ifα<sub>0</sub> can be arbitrary and the$\alpha _ { i }$are allowed to vary in the interval$\left( - r , r \right)$, then the number ofdistinct such functions that can result is at most$\dot { M } . 2 ^ { 2 r ( k + 1 ) ^ { 3 } }$

Proof. By Corollary 17.5, the number of functions that can result if the integer part of$\alpha _ { 0 }$is$j$(mod M) is at most$2 ^ { 2 r ( k + 1 ) ^ { 3 } }$, since each such function can be thought of as$j$added to the restriction of a function on$\{ 0 , 1 \} ^ { k + 1 }$ of the given form (and reduced mod$M )$. The result follows.✷

The trivial bound in Corollary 17.5 is$k ^ { 2 ^ { k + 1 } }$, which gives a bound of $M . ( k + 1 ) ^ { 2 ^ { k + 2 } }$in Corollary 17.6. As we commented above, this bound would be enough for our main result.

Before stating the next proposition, we define a concept which is similar to α-uniformity but designed for situations where we are given a multilinear function on a small domain. Let$f : \mathbb { Z } _ { N } \to D$. Suppose that we can partition$\mathbb { Z } _ { N }$into mod-N arithmetic progressions$Q _ { 1 } , \ldots , Q _ { M }$, each of length at most$m ,$, such that, defining$Q _ { i } f ( s )$to be$f ( s )$when$s \in Q _ { i }$and 0 otherwise, we haveM

$$
\sum_ {i = 1} ^ {M} \sum_ {x \in \mathbb {Z} _ {N} ^ {k + 1}} \sum_ {s} \Delta (Q _ {i} f; x) (s) \leqslant \alpha m ^ {k + 2} M.
$$

We shall then say that$f$is α-uniform ofdegree k with respect to the partition $Q _ { 1 } , \ldots , Q _ { M }$

Notice that i$\dot { \cdot } p \geqslant$km, then we can find an isomorphism$\gamma$from$Q _ { i }$to an arithmetic progression of length$| Q _ { i } |$inside$\mathbb { Z } _ { p }$such that, defining a$^ { 6 } \mathrm { c o p y } ^ { \mathrm { v } }$ $g$of$Q _ { i } f$inside$\mathbb { Z } _ { p }$by setting$g ( \gamma ( s ) ) = f ( s )$for$s \in Q _ { i }$and$g ( t ) = 0$for t not in the image of$\gamma ,$we have

$$
\sum_ {x \in \mathbb {Z} _ {N} ^ {k + 1}} \sum_ {s} \Delta (Q _ {i} f; x) (s) = \sum_ {y \in \mathbb {Z} _ {p} ^ {k + 1}} \sum_ {t} \Delta (g; y) (t).
$$

Hence, if

$$
\sum_ {x \in \mathbb {Z} _ {N} ^ {k + 1}} \sum_ {s} \Delta (Q _ {i} f; x) (s) \geqslant \beta m ^ {k + 2},
$$

we find that g is not$\beta ( m / p ) ^ { k + 2 }$-uniform$( \mathrm { i n ~ } \mathbb { Z } _ { p } )$of degree$k .$

Proposition 17.7. Let$f : \mathbb { Z } _ { N } \to D$. Suppose that there is a product $P = P _ { 1 } \times \cdots \times P _ { k }$of arithmetic progressions$P _ { i }$of common diference d and odd length m$\leqslant N ^ { 1 / 2 }$, and a k-linear function$\sigma : P  \mathbb { Z } _ { N }$such that

$$
\sum_ {x \in P} \left| \Delta (f; x) ^ {\wedge} (\sigma (x)) \right| ^ {2} \geqslant \alpha N ^ {2} m ^ {k}.
$$

Then there exist a polynomial φ ofdegree at most$k { + 1 }$and a partition of$\mathbb { Z } _ { N }$ into mod-N arithmetic progressions$Q _ { 1 } , \ldots , Q _ { M }$of size at least$m / 3 k$such that the function$g ( x ) = f ( x ) \omega ^ { - \phi ( x ) }$is not$2 ^ { - 2 ( k + 1 ) ^ { 3 } }$α-uniform of degree k with respect to the partition$Q _ { 1 } , \ldots , Q _ { M }$

Proof. Without loss of generality$d = 1$. Let$2 l + 1 = m$and let w be a real number such that$\lfloor l / k \rfloor - 1 < w \leqslant \lfloor l / k \rfloor$and$M = N / w$is an integer. For

$0 \leqslant j \leqslant M - 1$define$Q _ { j }$to be the interval$\{ x \in \mathbb { Z } _ { N } : j w \leqslant x < ( j + 1 ) w \}$ Notice that the cardinality of$Q _ { j }$is always$\lfloor l / k \rfloor - 1 \mathrm { o r } \lfloor l / k \rfloor$. Let a sequence $r = ( r _ { 1 } , \ldots , r _ { k } )$be defined by$P _ { i } = \{ r _ { i } - l , r _ { i } - l + 1 , \ldots , r _ { i } + l \}$and let I be the interval$\{ - l , - l + 1 , \ldots , l \}$. Then any$x \in P$can be written uniquely as $a + r$for some$a \in I ^ { k }$. Given$\epsilon \in \{ 0 , 1 \} ^ { k }$, we shall write$f _ { \epsilon }$for the function that takes s to$f ( s - \epsilon . r )$. Let us also write$\tau ( a )$for$\sigma ( a + r )$

Then

$$
\begin{array}{c} \sum_ {x \in P} | \Delta (f; x) ^ {\wedge} (\sigma (x)) | ^ {2} = \sum_ {a \in I ^ {k}} \Big | \sum_ {s} \omega^ {- s \sigma (a + r)} \prod_ {\epsilon} C ^ {| \epsilon |} f (s - \epsilon . a - \epsilon . r) \Big | ^ {2} \\ = \sum_ {a \in I ^ {k}} \Big | \sum_ {s} \omega^ {- s \tau (a)} \prod_ {\epsilon} C ^ {| \epsilon |} f _ {\epsilon} (s - \epsilon . a) \Big | ^ {2} \end{array}
$$

where the products are over all  in the set$\{ 0 , 1 \} ^ { k }$

If we now split each function$f _ { \epsilon }$up as$\textstyle \sum _ { j \in \mathbb { Z } _ { M } } Q _ { j } f _ { \epsilon }$, this expression becomes

$$
\sum_ {a \in I ^ {k}} \left| \sum_ {s} \omega^ {- s \tau (a)} \prod_ {\epsilon \in \{0, 1 \} ^ {k}} \sum_ {j = 1} ^ {M} (Q _ {j} C ^ {| \epsilon |} f _ {\epsilon}) (s - \epsilon . a) \right| ^ {2}.
$$

Interchanging the product over  with the sum over$j ,$we obtain

$$
\sum_ {a \in I ^ {k}} \left| \sum_ {s} \sum_ {j} \omega^ {- s \tau (a)} \prod_ {\epsilon \in \{0, 1 \} ^ {k}} (Q _ {j (\epsilon)} C ^ {| \epsilon |} f _ {\epsilon}) (s - \epsilon . a) \right| ^ {2},
$$

where now the sum over$j$stands for the sum over all functions$\begin{array} { l l } { { \mathit { j } } } & { { : } } \end{array}$ $\{ 0 , 1 \} ^ { k } \to \mathbb { Z } _ { M }$. Let us estimate how many such functions can give rise to a non-zero contribution to the entire expression.

This we can do using Corollary 17.5. If$Q _ { j ( \epsilon ) } f _ { \epsilon } ( s - \epsilon . a )$is non-zero, then$s - \epsilon . a \in Q _ { j ( \epsilon ) }$which implies that$j ( \epsilon ) w \ \leqslant \ s - \epsilon . a \ < \ j ( \epsilon ) w$and therefore that$j ( \epsilon )$is exactly the integer part of w$^ { - 1 } s - \epsilon . ( w ^ { - 1 } a )$. Since $- k - 1 < w ^ { - 1 } a _ { i } < k + 1$for every i, Corollary 17.5 implies that the number of functions$j$for which the product over  can ever be non-zero is at most $M . 2 ^ { 2 ( k + 1 ) ^ { 4 } }$

Let us define functions$j _ { 1 }$and$j _ { 2 }$(from$\{ 0 , 1 \} ^ { k }$to$\mathbb { Z } _ { M } )$to be equivalent if they are translations of each other. Corollary 17.5 with$M = 1$implies that the number of equivalence classes is at most$2 ^ { k ( k + 1 ) ^ { 2 } }$. Let us call them $J _ { 1 } , \ldots , J _ { L }$. By the Cauchy-Schwarz inequality, we can deduce from our calculations above that

$$
\alpha N ^ {2} m ^ {k} \leqslant L \sum_ {r = 1} ^ {L} \sum_ {a \in I ^ {k}} \left| \sum_ {s} \sum_ {j \in J _ {r}} \omega^ {- s \tau (a)} \prod_ {\epsilon} (Q _ {j (\epsilon)} C ^ {| \epsilon |} f _ {\epsilon}) (s - \epsilon . a) \right| ^ {2}.
$$

We can therefore find r such that, choosing some representative j of$J _ { r }$, we have

$$
L ^ {- 2} \alpha N ^ {2} m ^ {k} \leqslant \sum_ {a \in I ^ {k}} \left| \sum_ {s} \sum_ {i = 1} ^ {M} \omega^ {- s \tau (a)} \prod_ {\epsilon} (Q _ {j (\epsilon) + i} C ^ {| \epsilon |} f _ {\epsilon}) (s - \epsilon . a) \right| ^ {2}.
$$

Applying the Cauchy-Schwarz inequality again, this is at most

$$
M \sum_ {i = 1} ^ {M} \sum_ {a \in I ^ {k}} \left| \sum_ {s} \omega^ {- s \tau (a)} \prod_ {\epsilon} (Q _ {j (\epsilon) + i} C ^ {| \epsilon |} f _ {\epsilon}) (s - \epsilon . a) \right| ^ {2}.
$$

Obviously this still exceeds$L ^ { - 2 } \alpha N ^ { 2 } m ^ { k }$if we replace the sum over$a \in I _ { k }$ above by a sum over all of$\mathbb { Z } _ { N } ^ { k }$. Expanding the modulus squared and substituting in the usual way, the resulting inequality can be rewritten

$$
M \sum_ {i = 1} ^ {M} \sum_ {a \in \mathbb {Z} _ {N} ^ {k + 1}} \sum_ {s} \omega^ {- \rho (a)} \prod_ {\epsilon \in \{0, 1 \} ^ {k + 1}} (Q _ {j (\epsilon) + i} C ^ {| \epsilon |} f _ {\epsilon}) (s - \epsilon . a) \geqslant L ^ {- 2} \alpha N ^ {2} m ^ {k},
$$

where$j ( \epsilon )$and$f _ { \epsilon }$now mean$j ( \epsilon _ { 1 } , \dots , \epsilon _ { k } )$and$f _ { \epsilon _ { 1 } , \dots , \epsilon _ { k } }$respectively, and$\rho ( a )$ is defined to be$a _ { k + 1 } \tau ( a _ { 1 } , \ldots , a _ { k } )$. Applying Lemma 17.1, we obtain for each$\epsilon \in \{ 0 , 1 \} ^ { k + 1 }$a polynomial$\phi _ { \epsilon }$of degree at most$k + 1$in such a way that

$$
\rho (a) = \sum_ {\epsilon \in \{0, 1 \} ^ {k + 1}} (- 1) ^ {| \epsilon |} \phi_ {\epsilon} (s - \epsilon . a)
$$

for every$a \in \mathbb { Z } _ { N } ^ { k + 1 }$. Using these, we can rewrite the inequality yet again, this time as

$$
M \sum_ {i = 1} ^ {M} \sum_ {a \in \mathbb {Z} _ {N} ^ {k + 1}} \sum_ {s} \prod_ {\epsilon \in \{0, 1 \} ^ {k + 1}} (Q _ {j (\epsilon) + i} C ^ {| \epsilon |} f _ {\epsilon}) (s - \epsilon . a) \omega^ {- \phi_ {\epsilon} (s - \epsilon . a)} \geqslant L ^ {- 2} \alpha N ^ {2} m ^ {k}.
$$

We shall now apply Lemma 3.8 to the functions$Q _ { j ( \epsilon ) + i } C ^ { | \epsilon | } f _ { \epsilon }$. By the AM-GM inequality, the lemma implies that, for every i, the sum

$$
\sum_ {a \in \mathbb {Z} _ {N} ^ {k + 1}} \sum_ {s} \prod_ {\epsilon \in \{0, 1 \} ^ {k + 1}} (Q _ {j (\epsilon) + i} C ^ {| \epsilon |} f _ {\epsilon}) (s - \epsilon . a) \omega^ {- \phi_ {\epsilon} (s - \epsilon . a)}
$$

is bounded above by the average over$\eta \in \{ 0 , 1 \} ^ { k + 1 }$of

$$
\sum_ {a \in \mathbb {Z} _ {N} ^ {k + 1}} \sum_ {s} \prod_ {\epsilon \in \{0, 1 \} ^ {k + 1}} (Q _ {j (\eta) + i} C ^ {| \epsilon |} f _ {\eta}) (s - \epsilon . a) \omega^ {- \phi_ {\eta} (s - \epsilon . a)}.
$$

It follows by an averaging argument that we may choose$\eta \in \{ 0 , 1 \} ^ { k + 1 }$such that, setting$g ( s ) = f _ { \eta } ( s ) \omega ^ { - \phi _ { \eta } ( s ) }$, we have

$$
M \sum_ {i = 1} ^ {M} \sum_ {a \in \mathbb {Z} _ {N} ^ {k + 1}} \sum_ {s} \prod_ {\epsilon \in \{0, 1 \} ^ {k + 1}} (Q _ {j (\epsilon) + i} C ^ {| \epsilon |} g) (s - \epsilon . a) \geqslant L ^ {- 2} \alpha N ^ {2} m ^ {k},
$$

and this may be rewritten

or

$$
\begin{array}{c} \sum_ {i = 1} ^ {M} \sum_ {a \in \mathbb {Z} _ {N} ^ {k + 1}} \sum_ {s} \prod_ {\epsilon \in \{0, 1 \} ^ {k + 1}} (C ^ {| \epsilon |} Q _ {i} g) (s - \epsilon . a) \geqslant L ^ {- 2} \alpha M ^ {- 2} N ^ {2} m ^ {k} M  , \\ \sum_ {i = 1} ^ {M} \sum_ {a \in \mathbb {Z} _ {N} ^ {k + 1}} \sum_ {s} \Delta (Q _ {i} g; a) (s) \geqslant L ^ {- 2} \alpha M ^ {- 2} N ^ {2} m ^ {k} M \\ \geqslant 2 ^ {- 2 (k + 1) ^ {3}} \alpha m ^ {k + 2} M  . \end{array}
$$

This implies that the function$g$is not$2 ^ { - 2 ( k + 1 ) ^ { 3 } } \alpha \mathrm { - u n i f o r m }$with respect to the partition$Q _ { 1 } , \ldots , Q _ { M }$

This is not quite the statement of the proposition. To obtain${ \mathrm { i t } } ,$recall that$f _ { \eta } ( s ) = f ( s - \eta . r )$. Therefore, the statement about$g$implies that the function$f ( s ) \omega ^ { - \phi _ { \eta } ( s + \eta . r ) }$is not$2 ^ { - 2 ( k + 1 ) ^ { 3 } } c$α-uniform with respect to the partition$( Q _ { i } + \eta . r ) _ { i = 1 } ^ { m }$. Since$\phi _ { \eta } ( s + \eta . r )$is still a polynomial in s of degree at most$k + 1$, the proposition is proved.✷

## 18 Putting Everything Together

We are now ready for the proof of the main theorem. Indeed all we need to do is combine our earlier results in an obvious way. We shall divide the argument into two parts.

Theorem 18.1. Let$\alpha \leqslant 1 / 2$and let$A \subset \mathbb { Z } _ { N }$be a set which fails to be α-uniform of degree k. There exists a partition$o f \mathbb { Z } _ { N }$into arithmetic progressions$P _ { 1 } , \dots , P _ { M }$of average size at least$N ^ { \alpha ^ { 2 ^ { k + 1 0 } } }$such that

$$
\sum_ {j = 1} ^ {M} \left| \sum_ {s \in P _ {j}} f (s) \right| \geqslant \alpha^ {2 ^ {2 ^ {k + 1 0}}} N.
$$

Proof. The result will be proved by induction on k. First, Corollary 16.11 gives us a box$P ~ \subset ~ \mathbb { Z } _ { N } ^ { k }$of width at least$N ^ { ( \alpha / 2 ) ^ { 2 ^ { k + 8 } } }$and a multilinear function$\mu : P \to \mathbb { Z } _ { N }$such that, for at least$( \alpha / 2 ) ^ { 2 ^ { 2 ^ { k + 8 } } } | P |$values of $( y _ { 1 } , \dots , y _ { k } ) \in P$, we have

$$
\left| \Delta (f; y _ {1}, \dots , y _ {k}) ^ {\wedge} (\mu (y _ {1}, \dots , y _ {k})) \right| \geqslant (\alpha / 2) N.
$$

Let$\beta = ( \alpha ^ { 2 } / 8 ) ( \alpha / 2 ) ^ { 2 ^ { 2 ^ { k + 8 } } }$and let m be the largest odd number less than or equal to$N ^ { ( \alpha / 2 ) ^ { 2 ^ { k + 8 } } }$. Then the hypotheses for Proposition 17.7 are satisfied (with α replaced by$\beta )$. We can therefore find a polynomial$\phi$of degree at most$k$and a partition of$\mathbb { Z } _ { N }$into mod-N arithmetic progressions$Q _ { 1 } , \ldots , Q _ { M }$of size$l \ \mathrm { o r } \ l + 1$, where$l \geqslant m / 3 k$, such that the function $g ( x ) = f ( x ) \omega$<sup>−φ(x)</sup> is not$2 ^ { - 2 ( k + 3 ) ^ { 3 } } \beta .$-uniform of degree$k - 1$with respect to the partition$Q _ { 1 } , \ldots , Q _ { M }$

For each$i ,$define a (non-negative real) number$\beta _ { i }$by the equation

$$
\sum_ {x \in \mathbb {Z} _ {N} ^ {k}} \sum_ {s} \Delta (Q _ {i} g; x) (s) = \beta_ {i} l ^ {k + 1}.
$$

Since the sets$Q _ { i }$all have approximately the same size, the average value of$\beta _ { i }$is at least$2 ^ { - 2 ( k + 3 ) ^ { 3 } - 1 } { \overset { . } { \beta } }$. It follows that there is a set I of cardinality at least$2 ^ { - 2 ( k + 4 ) ^ { 3 } } \beta M$such that, for every$i \in I , \beta _ { i } \geqslant 2 ^ { - 2 ( k + 4 ) ^ { 3 } } \beta$. Let us now fix some$i \in I$

As described in the remarks before Proposition 17.7, we may associate with$Q _ { i } g$an “isomorphic” function$h _ { i } : \mathbb { Z } _ { p } \to \mathbb { C }$which fails to be$( \beta _ { i } / 2 k )$ uniform of degree$k - 1$. When this is done, the mod-N arithmetic progression$Q _ { i }$corresponds to an interval of integers in$\mathbb { Z } _ { p }$. By our inductive hypothesis, we can partition$\mathbb { Z } _ { p }$into proper arithmetic progressions $R _ { i 1 } , \ldots , R _ { i M _ { i } }$of average size at least$p ^ { ( \beta _ { i } / 2 k ) ^ { 2 ^ { 2 ^ { k + 9 } } } }$in such a way that

$$
\sum_ {j = 1} ^ {M _ {i}} \left| \sum_ {s \in R _ {i j}} h _ {i} (s) \right| \geqslant \left(\beta_ {i} / 2 k\right) ^ {2 ^ {2 ^ {k + 9}}} p.
$$

It follows that$Q _ { i }$can be partitioned into mod-N arithmetic progressions $S _ { i 1 } , \ldots , S _ { i M _ { i } }$of average size at least$r _ { i } = ( 2 k ) ^ { - 1 } p ^ { ( \beta _ { i } / 2 k ) ^ { 2 } } ^ { 2 ^ { k + 9 } }$such that

$$
\sum_ {j = 1} ^ {M _ {i}} \left| \sum_ {s \in S _ {i j}} g (s) \right| \geqslant \left(\beta_ {i} / 2 k\right) ^ {2 ^ {2 ^ {k + 9}}} | Q _ {i} |.
$$

The mod-N progressions$S _ { i j }$with$i \in I ,$, together with those$Q _ { i }$for which $i \not \in I ,$partition$\mathbb { Z } _ { N }$. From the way we chose$I ,$the average size of a cell in this partition is at least$r = ( 2 k ) ^ { - 1 } p ^ { ( 2 ^ { - ( k + 4 ) ^ { 3 } } \beta / 2 k ) ^ { 2 ^ { 2 ^ { k + 9 } } } }$. By Lemma 5.13 we can find a refinement of this partition into proper arithmetic progressions of average size at least$r ^ { 1 / 2 } / 4$. Let us call these progressions$T _ { 1 } , \dots , T _ { L }$ Since$\begin{array} { r } { \sum _ { i \in I } \left| Q _ { i } \right| \geqslant 2 ^ { - 2 ( k + 4 ) ^ { 3 } } \dot { \beta } N } \end{array}$we have the inequality

$$
\sum_ {j = 1} ^ {L} \left| \sum_ {s \in T _ {j}} g (s) \right| \geqslant (2 ^ {- 2 (k + 4) ^ {3}} \beta / 2 k) ^ {2 ^ {2 ^ {k + 9}}} 2 ^ {- 2 (k + 4) ^ {3}} \beta N.
$$

Let$\gamma = ( 2 ^ { - 2 ( k + 4 ) ^ { 3 } } \beta / 2 k ) ^ { 2 ^ { 2 ^ { k + 9 } } } 2 ^ { - 2 ( k + 4 ) ^ { 3 } } \beta$. We may now apply Lemma 5.14 to find a refinement of$T _ { 1 } , \dots , T _ { L }$into arithmetic progressions$U _ { 1 } , \dots , U _ { H }$

such that$H \leqslant C L ^ { 1 / K } N ^ { 1 - 1 / K }$and

$$
\sum_ {h = 1} ^ {H} \left| \sum_ {s \in U _ {h}} f (s) \right| \geqslant \gamma N / 2.
$$

All that remains is to check that$H ^ { - 1 } N \geqslant N ^ { \alpha ^ { 2 ^ { 2 ^ { k + 1 0 } } } }$and that$\gamma / 2 \geqslant$ $\alpha ^ { 2 ^ { 2 ^ { k + 1 0 } } }$. These are easy exercises for the reader (easy because$2 ^ { 2 ^ { k + 1 0 } }$is so much bigger than$2 ^ { 2 ^ { k + 9 } }$that estimates can be incredibly crude).✷

For the statement of our main theorem we shall use the notation$a \uparrow b$ for$a ^ { b } .$, with the obvious convention for bracketing, so that for example a ↑ b ↑ c stands for$a \uparrow ( b \uparrow c )$

Theorem 18.2. Let$0 < \delta \leqslant 1 / 2$, let k be a positive integer, let$N \geqslant$ $2 \uparrow 2 \uparrow \delta ^ { - 1 } \uparrow 2 \uparrow 2 \uparrow ( k + 9 )$and let A be a subset of the set$\{ 1 , 2 , \ldots , N \}$ of size at least δN. Then A contains an arithmetic progression of length k.

Proof. It is not hard to check that$N \geqslant 3 2 k ^ { 2 } \delta ^ { - k }$. Therefore, Corollary 3.6 implies the result when A is$( \delta / 2 ) ^ { k 2 ^ { k } }$-uniform of degree$k - 2$

Let$\alpha = ( \delta / 2 ) ^ { k 2 ^ { k } }$. If A is not α-uniform of degree$k - 2$then by Theorem 18.1 and Lemma 5.15 there is an arithmetic progression P of size at least$N ^ { \alpha ^ { 2 ^ { 2 ^ { k + 8 } } } }$such that$| A \cap P | \geqslant ( \delta + \alpha ^ { 2 ^ { 2 ^ { k + 8 } } } ) | P |$. We may then repeat the argument with the new density. After at most α<sup>−22</sup> repetitions, we find${ } _ { - 2 ^ { 2 ^ { k + 8 } } }$ an arithmetic progression of length$k ,$as long as N is large enough. Since at each repetition we are raising N to a power at least as big as$\alpha ^ { 2 ^ { 2 ^ { k + 8 } } }$and the argument works as long as$N \geqslant 3 2 k ^ { 2 } \delta ^ { - k }$, a suficient condition on the original N is that

$$
N \uparrow (\alpha \uparrow 2 \uparrow 2 \uparrow (k + 8)) \uparrow (\alpha^ {- 1} \uparrow 2 \uparrow 2 \uparrow (k + 8)) \geqslant 3 2 k ^ {2} \delta^ {- k}.
$$

It is not hard to check that this condition is satisfied when$N \geqslant$ $2 \uparrow 2 \uparrow \delta ^ { - 1 } \uparrow 2 \uparrow 2 \uparrow ( k + 9 )$, and the theorem is proved.✷

Notice that what matters for the bounds in the above proof is the number of times the iteration is performed. The fact that at each iteration we raise N to a very small power makes hardly any further diference.

Corollary 18.7. Let k be a positive integer and let${ \boldsymbol { N } } \_ { \mathbf { \lambda } } >$ $2 \uparrow 2 \uparrow 2 \uparrow 2 \uparrow 2 \uparrow ( k + 9 )$. Then however the set$\{ 1 , 2 , \ldots , N \}$is coloured with two colours, there will be a monochromatic arithmetic progression of length k.✷

Ron Graham has conjectured in several places (see e.g. [GRS]) that the function$M ( k , 2 )$is bounded above by a tower of twos of height k. Corollary 18.7 proves this conjecture for$k \geqslant 9$, and indeed gives a much stronger bound. It looks as though more would be needed to prove it for $k = 7$(for example) than merely tidying up our proof. For$k \leqslant 5 .$, the exact values of$M ( k , 2 )$are known and satisfy the conjecture.

## Concluding Remarks and Acknowledgements

The arguments of this paper leave open many interesting questions. The most obvious one is whether the multidimensional version of Szemer´edi’s theorem follows from similar arguments. There is not even a good bound in the case of three points in a triangle. (The precise statement is that, for suficiently large N, every subset of$[ N ] ^ { 2 }$of size at least$\delta N ^ { 2 }$contains a triple of the form$\{ ( a , b ) , ( a + d , b ) , ( a , b + d ) \}$. Very recently, Jozsef Solymosi sent me an argument that proves this using a lemma of Ruzsa and Szemer´edi, which itself uses Szemer´edi’s regularity lemma. Thus, at least a towertype bound can be proved for this problem.) It would of course also be extremely interesting to have quantitative versions of the results of [BL] and [FK] mentioned in the introduction.

Some of the ideas in this proof turn out not to be new. In particular, the content of$\ S 4 .$, that is, the relevance of exponentials in polynomials as well as the fact that they are not suficient, was discovered in an ergodic-theoretic context, independently and earlier by Kazhdan in recent unpublished work. In general, there seem to be very interesting connections between the methods of this paper and a new ergodic-theoretic approach that is not yet complete.

A more obvious connection with the ergodic methods is that the arguments of$\ S 3$closely resemble the arguments used by Furstenberg for the case of weak-mixing measure-preserving dynamical systems. His argument is based on the fact that a system that is weak-mixing is suficiently random to work, while one that is not can be decomposed in a useful way. This appears to be analogous in some way to the idea here of passing from a non-uniform set to a denser subset.

I am very grateful to B´ela Bollob´as for encouraging me to continue working on Szemer´edi’s theorem when an earlier attempt at proving it collapsed, and to Vitali Milman for making sure that I eventually finished this paper.

## References

[BS] A. Balog, E. Szemer<sup>´</sup>edi, A statistical theorem of set addition, Combinatorica 14 (1994), 263–268.

[Be] F.A. Behrend, On sets of integers which contain no three in arithmetic progression, Proc. Nat. Acad. Sci. 23 (1946), 331–332.

[BerL] V. Bergelson, A. Leibman, Polynomial extensions of van der Waerden’s and Szemer´edi’s theorems, J. Amer. Math. Soc. 9 (1996), 725–753.

[Bi] Y. Bilu, Structure of sets with small sumset, in “Structure Theory of Set Addition”, Ast´erisque 258 (1999), 77–108.

[Bo] N.N. Bogolyubov, Sur quelques propri´et´es arithm´etiques des presquep´eriodes, Ann. Chaire Math. Phys. Kiev 4 (1939), 185–194.

[Bou] J. Bourgain, On triples in arithmetic progression, Geom. Funct. Anal. 9 (1999), 968–984.

[CGW] F.R.K. Chung, R.L. Graham, R.M. Wilson, Quasi-random graphs, Combinatorica 9 (1989), 345–362.

[ET] P. Erdos, P. Tur <sup>˝</sup> an<sup>´</sup> , On some sequences of integers, J. London Math. Soc. 11 (1936), 261–264.

[F1] G.R. Freiman, Foundations of a Structural Theory of Set Addition, Kazan Gos. Ped. Inst., Kazan, 1966 (in Russian).

[F2] G.R. Freiman, Foundations of a Structural Theory of Set Addition, Translations of Mathematical Monographs 37, Amer. Math. Soc., Providence, RI, USA, 1973.

[Fu] H. Furstenberg, Ergodic behaviour of diagonal measures and a theorem of Szemer´edi on arithmetic progressions, J. Analyse Math. 31 (1977), 204–256.

[FuK] H. Furstenberg, Y. Katznelson, A density version of the Hales-Jewett theorem, J. d’Analyse Math. 57 (1991), 64–119.

[FuKO] H. Furstenberg, Y. Katznelson, D. Ornstein, The ergodic theoretical proof of Szemer´edi’s theorem, Bull. Amer. Math. Soc. 7 (1982), 527–552.

[G1] W.T. Gowers, Lower bounds of tower type for Szemer´edi’s uniformity lemma, Geometric And Functional Analysis 7 (1997), 322–337.

[G2] W.T. Gowers, A new proof of Szemer´edi’s theorem for arithmetic progressions of length four, Geometric And Functional Analysis 8 (1998), 529–551.

[GRS] R.L. Graham, B.L. Rothschild, J.H. Spencer, Ramsey Theory (2nd ed.), Wiley Interscience 1990.

[H] D.R. Heath-Brown, Integer sets containing no arithmetic progressions, J. London Math. Soc. (2) 35 (1987), 385–394.

[N] M.B. Nathanson, Additive Number Theory: Inverse Problems and the Geometry of Sumsets, Graduate Texts in Mathematics 165, Springer-Verlag, 1996.

[P] H. Plunnecke <sup>¨</sup> , Eigenschaften und Absch¨atzungen von Wirkingsfunktionen, Vol. 22, Berichte der Gesellschaft f¨ur Mathematik und Datenverarbeitung, Bonn, 1969.

[R1] K.F. Roth, On certain sets of integers, J. London Math. Soc. 28 (1953), 245–252.

[R2] K.F. Roth, Irregularities of sequences relative to arithmetic progressions, IV, Period. Math. Hungar. 2 (1972), 301–326.

[Ru1] I.Z. Ruzsa, Arithmetic progressions and the number of sums, Period. Math. Hungar. 25 (1992), 105–111.

[Ru2] I.Z. Ruzsa, An application of graph theory to additive number theory, Scientia, Ser. A 3 (1989), 97–109.

[Ru3] I. Ruzsa, Generalized arithmetic progressions and sumsets, Acta Math. Hungar. 65 (1994), 379–388.

[S] S. Shelah, Primitive recursive bounds for van der Waerden numbers, J. Amer. Math. Soc. 1 (1988), 683–697.

[Sz1] E. Szemer<sup>´</sup>edi, On sets of integers containing no four elements in arithmetic progression, Acta Math. Acad. Sci. Hungar. 20 (1969), 89–104.

[Sz2] E. Szemer<sup>´</sup>edi, On sets of integers containing no k elements in arithmetic progression, Acta Arith. 27 (1975), 299–345.

[Sz3] E. Szemer<sup>´</sup>edi, Integer sets containing no arithmetic progressions, Acta Math. Hungar. 56 (1990), 155–158.

[V] R.C. Vaughan, The Hardy-Littlewood Method (2nd ed.), Cambridge Tracts in Mathematics 125, CUP 1997.

[W] H. Weyl, Uber die Gleichverteilung von Zahlen mod Eins, Math. Annalen <sup>¨</sup> 77 (1913), 313–352.

W.T. Gowers, Centre for Mathematical Sciences, Wilberforce Road, Cambridge CB3 0WA, UK