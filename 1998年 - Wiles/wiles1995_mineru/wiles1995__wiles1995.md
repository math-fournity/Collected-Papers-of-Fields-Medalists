![](images/page_0_image_0.jpg)

Pierre de Fermat

# Modular elliptic curves and Fermat’s Last Theorem

By Andrew John Wiles\* For Nada, Claire, Kate and Olivia

![](images/page_0_image_4.jpg)

Andrew John Wiles

Cubum autem in duos cubos, aut quadratoquadratum in duos quadratoquadratos, et generaliter nullam in infinitum ultra quadratum potestatum in duos ejusdem nominis fas est dividere: cujes rei demonstrationem mirabilem sane detexi. Hanc marginis exiguitas non caperet.

\- Pierre de Fermat ∼ 1637

Abstract. When Andrew John Wiles was 10 years old, he read Eric Temple Bell’s The Last Problem and was so impressed by it that he decided that he would be the first person to prove Fermat’s Last Theorem. This theorem states that there are no nonzero integers $a , b , c , n$with$n > 2$such that$a ^ { n } + b ^ { n } = c ^ { n }$. The object of this paper is to prove that all semistable elliptic curves over the set of rational numbers are modular. Fermat’s Last Theorem follows as a corollary by virtue of previous work by Frey, Serre and Ribet.

## Introduction

An elliptic curve over Q is said to be modular if it has a finite covering by a modular curve of the form$X _ { 0 } ( N )$. Any such elliptic curve has the property that its Hasse-Weil zeta function has an analytic continuation and satisfies a functional equation of the standard type. If an elliptic curve over Q with a given j-invariant is modular then it is easy to see that all elliptic curves with the same j-invariant are modular (in which case we say that the j-invariant is modular). A well-known conjecture which grew out of the work of Shimura and Taniyama in the 1950’s and 1960’s asserts that every elliptic curve over Q is modular. However, it only became widely known through its publication in a paper of Weil in 1967 [We] (as an exercise for the interested reader!), in which, moreover, Weil gave conceptual evidence for the conjecture. Although it had been numerically verified in many cases, prior to the results described in this paper it had only been known that finitely many j-invariants were modular.

In 1985 Frey made the remarkable observation that this conjecture should imply Fermat’s Last Theorem. The precise mechanism relating the two was formulated by Serre as the ε-conjecture and this was then proved by Ribet in the summer of 1986. Ribet’s result only requires one to prove the conjecture for semistable elliptic curves in order to deduce Fermat’s Last Theorem.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\*The work on this paper was supported by an NSF grant.</span></small>

Our approach to the study of elliptic curves is via their associated Galois representations. Suppose that$\rho _ { p }$is the representation of$\operatorname { G a l } ( { \bar { \mathbf { Q } } } / \mathbf { Q } )$on the p-division points of an elliptic curve over Q, and suppose for the moment that $\rho _ { 3 }$is irreducible. The choice of 3 is critical because a crucial theorem of Langlands and Tunnell shows that if$\rho _ { 3 }$is irreducible then it is also modular. We then proceed by showing that under the hypothesis that$\rho _ { 3 }$is semistable at 3, together with some milder restrictions on the ramification of$\rho _ { 3 }$at the other primes, every suitable lifting of$\rho _ { 3 }$is modular. To do this we link the problem, via some novel arguments from commutative algebra, to a class number problem of a well-known type. This we then solve with the help of the paper [TW]. This sufices to prove the modularity of E as it is known that E is modular if and only if the associated 3-adic representation is modular.

The key development in the proof is a new and surprising link between two strong but distinct traditions in number theory, the relationship between Galois representations and modular forms on the one hand and the interpretation of special values of L-functions on the other. The former tradition is of course more recent. Following the original results of Eichler and Shimura in the 1950’s and 1960’s the other main theorems were proved by Deligne, Serre and Langlands in the period up to 1980. This included the construction of Galois representations associated to modular forms, the refinements of Langlands and Deligne (later completed by Carayol), and the crucial application by Langlands of base change methods to give converse results in weight one. However with the exception of the rather special weight one case, including the extension by Tunnell of Langlands’ original theorem, there was no progress in the direction of associating modular forms to Galois representations. From the mid 1980’s the main impetus to the field was given by the conjectures of Serre which elaborated on the ε-conjecture alluded to before. Besides the work of Ribet and others on this problem we draw on some of the more specialized developments of the 1980’s, notably those of Hida and Mazur.

The second tradition goes back to the famous analytic class number formula of Dirichlet, but owes its modern revival to the conjecture of Birch and Swinnerton-Dyer. In practice however, it is the ideas of Iwasawa in this field on which we attempt to draw, and which to a large extent we have to replace. The principles of Galois cohomology, and in particular the fundamental theorems of Poitou and Tate, also play an important role here.

The restriction that$\rho _ { 3 }$be irreducible at 3 is bypassed by means of an intriguing argument with families of elliptic curves which share a common $\rho _ { 5 }$. Using this, we complete the proof that all semistable elliptic curves are modular. In particular, this finally yields a proof of Fermat’s Last Theorem. In addition, this method seems well suited to establishing that all elliptic curves over Q are modular and to generalization to other totally real number fields.

Now we present our methods and results in more detail.

Let f be an eigenform associated to the congruence subgroup$\Gamma _ { 1 } ( N )$of $\operatorname { S L _ { 2 } } ( \mathbf { Z } )$of weight$k \geq 2$and character$\chi .$. Thus if$T _ { n }$is the Hecke operator associated to an integer n there is an algebraic integer$c ( n , f )$such that$T _ { n } f =$ $c ( n , f ) f$for each n. We let$K _ { f }$be the number field generated over Q by the $\{ c ( n , f ) \}$together with the values of$\chi$and let$\mathcal { O } _ { f }$be its ring of integers. For any prime$\lambda$of$\mathcal { O } _ { f }$let$\mathcal { O } _ { f , \lambda }$be the completion of$\mathcal { O } _ { f }$at$\lambda .$The following theorem is due to Eichler and Shimura (for$k = 2 )$and Deligne (for$k > 2 )$ The analogous result when$k = 1$is a celebrated theorem of Serre and Deligne but is more naturally stated in terms of complex representations. The image in that case is finite and a converse is known in many cases.

Theorem 0.1. For each prime$p \in \mathbf { Z }$and each prime$\lambda | p$of${ \mathcal { O } } _ { f }$there is a continuous representation

$$
\rho_ {f, \lambda}: \mathrm{Gal} (\bar {\mathbf {Q}} / \mathbf {Q}) \longrightarrow \mathrm{GL} _ {2} (\mathcal {O} _ {f, \lambda})
$$

which is unramified outside the primes dividing$N p$and such that for all primes $q \nmid N p$

$$
\operatorname{trace} \rho_ {f, \lambda} (\text { Frob } q) = c (q, f), \quad \det \rho_ {f, \lambda} (\text { Frob } q) = \chi (q) q ^ {k - 1}.
$$

We will be concerned with trying to prove results in the opposite direction, that is to say, with establishing criteria under which a λ-adic representation arises in this way from a modular form. We have not found any advantage in assuming that the representation is part of a compatible system of λ-adic representations except that the proof may be easier for some λ than for others.

Assume

$$
\rho_ {0}: \operatorname{Gal} (\bar {\mathbf {Q}} / \mathbf {Q}) \longrightarrow \operatorname{GL} _ {2} (\bar {\mathbf {F}} _ {p})
$$

is a continuous representation with values in the algebraic closure of a finite field of characteristic$p$and that det$\rho _ { 0 }$is odd. We say that$\rho _ { 0 }$is modular if$\rho _ { 0 }$and$\rho _ { f , \lambda }$mod λ are isomorphic over$\bar { \mathbf { F } } _ { p }$for some$f$and$\lambda$and some embedding of${ \mathcal { O } } _ { f } / \lambda$in$\bar { \mathbf { F } } _ { p }$. Serre has conjectured that every irreducible$\rho _ { 0 }$of odd determinant is modular. Very little is known about this conjecture except when the image of$\rho _ { 0 }$in$\mathrm { P G L _ { 2 } } ( \bar { \mathbf { F } } _ { p } )$is dihedral,$A _ { 4 }$or$S _ { 4 }$. In the dihedral case it is true and due (essentially) to Hecke, and in the$A _ { 4 }$and$S _ { 4 }$cases it is again true and due primarily to Langlands, with one important case due to Tunnell (see Theorem 5.1 for a statement). More precisely these theorems actually associate a form of weight one to the corresponding complex representation but the versions we need are straightforward deductions from the complex case. Even in the reducible case not much is known about the problem in the form we have described it, and in that case it should be observed that one must also choose the lattice carefully as only the semisimplification of $\overline { { \rho _ { f , \lambda } } } = \rho _ { f , \lambda }$mod λ is independent of the choice of lattice in$K _ { f , \lambda } ^ { 2 }$

If O is the ring of integers of a local field (containing$\mathbf { Q } _ { p } )$we will say that $\rho : { \mathrm { G a l } } ( { \bar { \mathbf { Q } } } / { \mathbf { Q } } ) \longrightarrow { \mathrm { G L } } _ { 2 } ( { \mathcal { O } } )$is a lifting of$\rho _ { 0 } \ \mathrm { i f } ,$for a specified embedding of the residue field of$\mathcal { O }$in$\bar { \mathbf { F } } _ { p } , \bar { \rho }$and$\rho _ { 0 }$are isomorphic over$\bar { \mathbf { F } } _ { p }$. Our point of view will be to assume that$\rho _ { 0 }$is modular and then to attempt to give conditions under which a representation$\rho$lifting$\rho _ { 0 }$comes from a modular form in the sense that$\rho \simeq \rho _ { f , \lambda }$over$\overline { { K _ { f , \lambda } } }$for some$f , \lambda$. We will restrict our attention to two cases:

(I)$\rho _ { 0 }$is ordinary (at$p )$by which we mean that there is a one-dimensional subspace of$\bar { \bar { \mathbf { F } } } _ { p } ^ { 2 } .$, stable under a decomposition group at$p$and such that the action on the quotient space is unramified and distinct from the action on the subspace.

(II)$\rho _ { 0 }$is flat (at$p )$, meaning that as a representation of a decomposition group at$p , \rho _ { 0 }$is equivalent to one that arises from a finite flat group scheme over$\mathbf { Z } _ { p }$, and det$\rho _ { 0 }$restricted to an inertia group at$p$is the cyclotomic character.

We say similarly that$\rho$is ordinary$( \mathrm { a t } ~ p )$, if viewed as a representation to$\bar { \mathbf { Q } } _ { p } ^ { 2 }$ there is a one-dimensional subspace of$\bar { \mathbf { Q } } _ { p } ^ { 2 }$stable under a decomposition group at$p$and such that the action on the quotient space is unramified.

Let$\varepsilon : \mathrm { G a l } ( \bar { \mathbf { Q } } / \mathbf { Q } ) \longrightarrow \mathbf { Z } _ { p } ^ { \times }$denote the cyclotomic character. Conjectural converses to Theorem 0.1 have been part of the folklore for many years but have hitherto lacked any evidence. The critical idea that one might dispense with compatible systems was already observed by Drinfield in the function field case [Dr]. The idea that one only needs to make a geometric condition on the restriction to the decomposition group at$p$was first suggested by Fontaine and Mazur. The following version is a natural extension of Serre’s conjecture which is convenient for stating our results and is, in a slightly modified form, the one proposed by Fontaine and Mazur. (In the form stated this incorporates Serre’s conjecture. We could instead have made the hypothesis that$\rho _ { 0 }$is modular.)

Conjecture. Suppose that$\rho : { \mathrm { G a l } } ( { \bar { \mathbf { Q } } } / { \mathbf { Q } } ) \longrightarrow { \mathrm { G L } } _ { 2 } ( { \mathcal { O } } )$is an irreducible lifting of$\rho _ { 0 }$and that$\rho$is unramified outside of a finite set of primes. There are two cases:

(i) Assume that$\rho _ { 0 }$is ordinary. Then$i f \rho$is ordinary and det$\rho = \varepsilon ^ { k - 1 } \chi$for some integer$k \geq 2$and some$\chi$of finite order,$\rho$comes from a modular form.

(ii) Assume that$\rho _ { 0 }$is flat and that p is odd. Then if ρ restricted to a decomposition group at$p$is equivalent to a representation on a p-divisible group, again$\rho$comes from a modular form.

In case (ii) it is not hard to see that if the form exists it has to be of weight$2 ;$in (i) of course it would have weight k. One can of course enlarge this conjecture in several ways, by weakening the conditions in (i) and (ii), by considering other number fields of Q and by considering groups other than$\mathrm { G L _ { 2 } }$

We prove two results concerning this conjecture. The first includes the hypothesis that$\rho _ { 0 }$is modular. Here and for the rest of this paper we will assume that$p$is an odd prime.

Theorem 0.2. Suppose that$\rho _ { 0 }$is irreducible and satisfies either (I) or (II) above. Suppose also that$\rho _ { 0 }$is modular and that

(i)$\rho _ { 0 }$is absolutely irreducible when restricted to$\mathbf { Q } { \biggl ( } { \sqrt { ( - 1 ) ^ { \frac { p - 1 } { 2 } } p } } { \biggr ) }$

(ii) If$q \equiv - 1$mod$p$is ramified in$\rho _ { 0 }$then either$\rho _ { 0 } | _ { D _ { q } }$is reducible over the algebraic closure where$D _ { q }$is a decomposition group at q or$\rho _ { 0 } | _ { I _ { q } }$is absolutely irreducible where$I _ { q }$is an inertia group at$q$.

Then any representation$\rho$as in the conjecture does indeed come from a modular form.

The only condition which really seems essential to our method is the requirement that$\rho _ { 0 }$be modular.

The most interesting case at the moment is when$p = 3$and$\rho _ { 0 }$can be defined over$\mathbf { F } _ { 3 }$. Then since$\mathrm { P G L _ { 2 } } ( \mathbf { F } _ { 3 } ) \simeq S _ { 4 }$every such representation is modular by the theorem of Langlands and Tunnell mentioned above. In particular, every representation into$\mathrm { G L _ { 2 } ( Z _ { 3 } ) }$whose reduction satisfies the given conditions is modular. We deduce:

Theorem 0.3. Suppose that E is an elliptic curve defined over Q and that$\rho _ { 0 }$is the Galois action on the 3-division points. Suppose that E has the following properties:

(i) E has good or multiplicative reduction at$3 .$.

(ii)$\rho _ { 0 }$is absolutely irreducible when restricted to$\mathbf { Q } \left( { \sqrt { - 3 } } \right)$

(iii) For any$q \equiv - 1$mod 3 either$\rho _ { 0 } | _ { D _ { q } }$is reducible over the algebraic closure or$\rho _ { 0 } | I _ { q }$is absolutely irreducible.

Then E should be modular.

We should point out that while the properties of the zeta function follow directly from Theorem 0.2 the stronger version that$E$is covered by$X _ { 0 } ( N )$

requires also the isogeny theorem proved by Faltings (and earlier by Serre when E has nonintegral j-invariant, a case which includes the semistable curves). We note that if E is modular then so is any twist of E, so we could relax condition (i) somewhat.

The important class of semistable curves, i.e., those with square-free conductor, satisfies (i) and (iii) but not necessarily (ii). If (ii) fails then in fact$\rho _ { 0 }$ is reducible. Rather surprisingly, Theorem 0.2 can often be applied in this case also by showing that the representation on the 5-division points also occurs for another elliptic curve which Theorem 0.3 has already proved modular. Thus Theorem 0.2 is applied this time with$p = 5$. This argument, which is explained in Chapter 5, is the only part of the paper which really uses deformations of the elliptic curve rather than deformations of the Galois representation. The argument works more generally than the semistable case but in this setting we obtain the following theorem:

Theorem 0.4. Suppose that E is a semistable elliptic curve defined over Q. Then E is modular.

More general families of elliptic curves which are modular are given in Chapter 5.

In 1986, stimulated by an ingenious idea of Frey [Fr], Serre conjectured and Ribet proved (in [Ri1]) a property of the Galois representation associated to modular forms which enabled Ribet to show that Theorem 0.4 implies ‘Fermat’s Last Theorem’. Frey’s suggestion, in the notation of the following theorem, was to show that the (hypothetical) elliptic curve$y ^ { 2 } = x ( x + u ^ { p } ) ( x - v ^ { p } )$ could not be modular. Such elliptic curves had already been studied in [He] but without the connection with modular forms. Serre made precise the idea of Frey by proposing a conjecture on modular forms which meant that the representation on the p-division points of this particular elliptic curve, if modular, would be associated to a form of conductor 2. This, by a simple inspection, could not exist. Serre’s conjecture was then proved by Ribet in the summer of 1986. However, one still needed to know that the curve in question would have to be modular, and this is accomplished by Theorem 0.4. We have then (finally!):

Theorem 0.5. Suppose that$u ^ { p } + v ^ { p } + w ^ { p } = 0$with$u , v , w \in \mathbf { Q }$and$p \geq 3 .$ then uvw = 0. (Equivalently - there are no nonzero integers$a , b , c , n$with$n > 2$ such that$a ^ { n } + b ^ { n } = c ^ { n } .$)

The second result we prove about the conjecture does not require the assumption that$\rho _ { 0 }$be modular (since it is already known in this case).

Theorem 0.6. Suppose that$\rho _ { 0 }$is irreducible and satisfies the hypothesis of the conjecture, including (I) above. Suppose further that

(i)$\rho _ { 0 } = \mathrm { I n d } _ { L } ^ { \mathbf { Q } } \kappa _ { 0 }$for a character κ of an imaginary quadratic extension L of Q which is unramified at p.

(ii) det$\rho _ { 0 } | _ { I _ { p } } = \omega$

Then a representation ρ as in the conjecture does indeed come from a modular form.

This theorem can also be used to prove that certain families of elliptic curves are modular. In this summary we have only described the principal theorems associated to Galois representations and elliptic curves. Our results concerning generalized class groups are described in Theorem 3.3.

The following is an account of the origins of this work and of the more specialized developments of the 1980’s that afected it. I began working on these problems in the late summer of 1986 immediately on learning of Ribet’s result. For several years I had been working on the Iwasawa conjecture for totally real fields and some applications of it. In the process, I had been using and developing results on #-adic representations associated to Hilbert modular forms. It was therefore natural for me to consider the problem of modularity from the point of view of #-adic representations. I began with the assumption that the reduction of a given ordinary #-adic representation was reducible and tried to prove under this hypothesis that the representation itself would have to be modular. I hoped rather naively that in this situation I could apply the techniques of Iwasawa theory. Even more optimistically I hoped that the case # = 2 would be tractable as this would sufice for the study of the curves used by Frey. From now on and in the main text, we write p for # because of the connections with Iwasawa theory.

After several months studying the 2-adic representation, I made the first real breakthrough in realizing that I could use the 3-adic representation instead: the Langlands-Tunnell theorem meant that$\rho _ { 3 }$, the mod 3 representation of any given elliptic curve over$\mathbf { Q } ,$would necessarily be modular. This enabled me to try inductively to prove that the$\operatorname { G L _ { 2 } } ( \mathbf { Z } / 3 ^ { n } \mathbf { Z } )$representation would be modular for each n. At this time I considered only the ordinary case. This led quickly to the study of$H ^ { i } ( \operatorname { G a l } ( F _ { \infty } / \mathbf { Q } ) , W _ { f } )$for$i = 1$and 2, where$F _ { \infty }$is the splitting field of the m-adic torsion on the Jacobian of a suitable modular curve, m being the maximal ideal of a Hecke ring associated to$\rho _ { 3 }$and$W _ { f }$the module associated to a modular form f described in Chapter 1. More specifically, I needed to compare this cohomology with the cohomology of$\operatorname { G a l } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } )$acting on the same module.

I tried to apply some ideas from Iwasawa theory to this problem. In my solution to the Iwasawa conjecture for totally real fields [Wi4], I had introduced a new technique in order to deal with the trivial zeroes. It involved replacing the standard Iwasawa theory method of considering the fields in the cyclotomic $\mathbf { Z } _ { p } .$-extension by a similar analysis based on a choice of infinitely many distinct primes$q _ { i } \equiv 1$mod$p ^ { n _ { i } }$with$n _ { i } \to \infty$as$i \to \infty$. Some aspects of this method suggested that an alternative to the standard technique of Iwasawa theory, which seemed problematic in the study of$W _ { f }$, might be to make a comparison between the cohomology groups as$\Sigma$varies but with the field Q fixed. The new principle said roughly that the unramified cohomology classes are trapped by the tamely ramified ones. After reading the paper [Gre1]. I realized that the duality theorems in Galois cohomology of Poitou and Tate would be useful for this. The crucial extract from this latter theory is in Section 2 of Chapter 1.

In order to put ideas into practice I developed in a naive form the techniques of the first two sections of Chapter 2. This drew in particular on a detailed study of all the congruences between f and other modular forms of difering levels, a theory that had been initiated by Hida and Ribet. The outcome was that I could estimate the first cohomology group well under two assumptions, first that a certain subgroup of the second cohomology group vanished and second that the form$f$was chosen at the minimal level for m. These assumptions were much too restrictive to be really efective but at least they pointed in the right direction. Some of these arguments are to be found in the second section of Chapter 1 and some form the first weak approximation to the argument in Chapter 3. At that time, however, I used auxiliary primes $q \equiv - 1$mod$p$when varying Σ as the geometric techniques I worked with did not apply in general for primes$q \equiv 1$mod$p .$(This was for much the same reason that the reduction of level argument in [Ri1] is much more dificult when$q \equiv 1$mod$p . )$In all this work I used the more general assumption that $\rho _ { p }$was modular rather than the assumption that$p = - 3$

In the late 1980’s, I translated these ideas into ring-theoretic language. A few years previously Hida had constructed some explicit one-parameter families of Galois representations. In an attempt to understand this, Mazur had been developing the language of deformations of Galois representations. Moreover, Mazur realized that the universal deformation rings he found should be given by Hecke ings, at least in certain special cases. This critical conjecture refined the expectation that all ordinary liftings of modular representations should be modular. In making the translation to this ring-theoretic language I realized that the vanishing assumption on the subgroup of$H ^ { 2 }$which I had needed should be replaced by the stronger condition that the Hecke rings were complete intersections. This fitted well with their being deformation rings where one could estimate the number of generators and relations and so made the original assumption more plausible.

To be of use, the deformation theory required some development. Apart from some special examples examined by Boston and Mazur there had been little work on it. I checked that one could make the appropriate adjustments to the theory in order to describe deformation theories at the minimal level. In the fall of 1989, I set Ramakrishna, then a student of mine at Princeton, the task of proving the existence of a deformation theory associated to representations arising from finite flat group schemes over$\mathbf { Z } _ { p }$. This was needed in order to remove the restriction to the ordinary case. These developments are described in the first section of Chapter 1 although the work of Ramakrishna was not completed until the fall of 1991. For a long time the ring-theoretic version of the problem, although more natural, did not look any simpler. The usual methods of Iwasawa theory when translated into the ring-theoretic language seemed to require unknown principles of base change. One needed to know the exact relations between the Hecke rings for diferent fields in the cyclotomic $\mathbf { Z } _ { p }$-extension of Q, and not just the relations up to torsion.

The turning point in this and indeed in the whole proof came in the spring of 1991. In searching for a clue from commutative algebra I had been particularly struck some years earlier by a paper of Kunz [Ku2]. I had already needed to verify that the Hecke rings were Gorenstein in order to compute the congruences developed in Chapter 2. This property had first been proved by Mazur in the case of prime level and his argument had already been extended by other authors as the need arose. Kunz’s paper suggested the use of an invariant (the η-invariant of the appendix) which I saw could be used to test for isomorphisms between Gorenstein rings. A diferent invariant (the${ \mathfrak { p } } / { \mathfrak { p } } ^ { 2 } -$ invariant of the appendix) I had already observed could be used to test for isomorphisms between complete intersections. It was only on reading Section 6 of [Ti2] that I learned that it followed from Tate’s account of Grothendieck duality theory for complete intersections that these two invariants were equal for such rings. Not long afterwards I realized that, unlike though it seemed at first, the equality of these invariants was actually a criterion for a Gorenstein ring to be a complete intersection. These arguments are given in the appendix.

The impact of this result on the main problem was enormous. Firstly, the relationship between the Hecke rings and the deformation rings could be tested just using these two invariants. In particular I could provide the inductive argument of section 3 of Chapter 2 to show that if all liftings with restricted ramification are modular then all liftings are modular. This I had been trying to do for a long time but without success until the breakthrough in commutative algebra. Secondly, by means of a calculation of Hida summarized in [Hi2] the main problem could be transformed into a problem about class numbers of a type well-known in Iwasawa theory. In particular, I could check this in the ordinary CM case using the recent theorems of Rubin and Kolyvagin. This is the content of Chapter 4. Thirdly, it meant that for the first time it could be verified that infinitely many j-invariants were modular. Finally, it meant that I could focus on the minimal level where the estimates given by me earlier

Galois cohomology calculations looked more promising. Here I was also using the work of Ribet and others on Serre’s conjecture (the same work of Ribet that had linked Fermat’s Last Theorem to modular forms in the first place) to know that there was a minimal level.

The class number problem was of a type well-known in Iwasawa theory and in the ordinary case had already been conjectured by Coates and Schmidt. However, the traditional methods of Iwasawa theory did not seem quite sufficient in this case and, as explained earlier, when translated into the ringtheoretic language seemed to require unknown principles of base change. So instead I developed further the idea of using auxiliary primes to replace the change of field that is used in Iwasawa theory. The Galois cohomology estimates described in Chapter 3 were now much stronger, although at that time I was still using primes$q \equiv - 1$mod$p$for the argument. The main dificulty was that although I knew how the η-invariant changed as one passed to an auxiliary level from the results of Chapter 2, I did not know how to estimate the change in the$\mathfrak { p / p ^ { 2 } \mathrm { - i n v a r i a n t } }$precisely. However, the method did give the right bound for the generalised class group, or Selmer group as it often called in this context, under the additional assumption that the minimal Hecke ring was a complete intersection.

I had earlier realized that ideally what I needed in this method of auxiliary primes was a replacement for the power series ring construction one obtains in the more natural approach based on Iwasawa theory. In this more usual setting, the projective limit of the Hecke rings for the varying fields in a cyclotomic tower would be expected to be a power series ring, at least if one assumed the vanishing of the$\mu \cdot$-invariant. However, in the setting with auxiliary primes where one would change the level but not the field, the natural limiting process did not appear to be helpful, with the exception of the closely related and very important construction of Hida [Hi1]. This method of Hida often gave one step towards a power series ring in the ordinary case. There were also tenuous hints of a patching argument in Iwasawa theory ([Scho], [Wi4, §10]), but I searched without success for the key.

Then, in August, 1991, I learned of a new construction of Flach [Fl] and quickly became convinced that an extension of his method was more plausible. Flach’s approach seemed to be the first step towards the construction of an Euler system, an approach which would give the precise upper bound for the size of the Selmer group if it could be completed. By the fall of 1992, I believed I had achieved this and begun then to consider the remaining case where the mod 3 representation was assumed reducible. For several months I tried simply to repeat the methods using deformation rings and Hecke rings. Then unexpectedly in May 1993, on reading of a construction of twisted forms of modular curves in a paper of Mazur [Ma3], I made a crucial and surprising breakthrough: I found the argument using families of elliptic curves with a common$\rho _ { 5 }$which is given in Chapter 5. Believing now that the proof was complete, I sketched the whole theory in three lectures in Cambridge, England on June 21-23. However, it became clear to me in the fall of 1993 that the construction of the Euler system used to extend Flach’s method was incomplete and possibly flawed.

Chapter 3 follows the original approach I had taken to the problem of bounding the Selmer group but had abandoned on learning of Flach’s paper. Darmon encouraged me in February, 1994, to explain the reduction to the complete intersection property, as it gave a quick way to exhibit infinite families of modular j-invariants. In presenting it in a lecture at Princeton, I made, almost unconsciously, critical switch to the special primes used in Chapter 3 as auxiliary primes. I had only observed the existence and importance of these primes in the fall of 1992 while trying to extend Flach’s work. Previously, I had only used primes$q \equiv - 1$mod$p$as auxiliary primes. In hindsight this change was crucial because of a development due to de Shalit. As explained before, I had realized earlier that Hida’s theory often provided one step towards a power series ring at least in the ordinary case. At the Cambridge conference de Shalit had explained to me that for primes$q \equiv 1$mod$p$he had obtained a version of Hida’s results. But excerpt for explaining the complete intersection argument in the lecture at Princeton, I still did not give any thought to my initial approach, which I had put aside since the summer of 1991, since I continued to believe that the Euler system approach was the correct one.

Meanwhile in January, 1994, R. Taylor had joined me in the attempt to repair the Euler system argument. Then in the spring of 1994, frustrated in the eforts to repair the Euler system argument, I begun to work with Taylor on an attempt to devise a new argument using$p = 2$. The attempt to use$p = 2$ reached an impasse at the end of August. As Taylor was still not convinced that the Euler system argument was irreparable, I decided in September to take one last look at my attempt to generalise Flach, if only to formulate more precisely the obstruction. In doing this I came suddenly to a marvelous revelation: I saw in a flash on September 19th, 1994, that de Shalit’s theory, if generalised, could be used together with duality to glue the Hecke rings at suitable auxiliary levels into a power series ring. I had unexpectedly found the missing key to my old abandoned approach. It was the old idea of picking$q _ { i } \mathrm { \dot { s } }$with$q _ { i } \equiv 1 { \bmod { p } } ^ { n _ { i } }$ and$n _ { i } \to \infty$as$i \to \infty$that I used to achieve the limiting process. The switch to the special primes of Chapter 3 had made all this possible.

After I communicated the argument to Taylor, we spent the next few days making sure of the details. the full argument, together with the deduction of the complete intersection property, is given in [TW].

In conclusion the key breakthrough in the proof had been the realization in the spring of 1991 that the two invariants introduced in the appendix could be used to relate the deformation rings and the Hecke rings. In efect the$\eta -$ invariant could be used to count Galois representations. The last step after the June, 1993, announcement, though elusive, was but the conclusion of a long process whose purpose was to replace, in the ring-theoretic setting, the methods based on Iwasawa theory by methods based on the use of auxiliary primes.

One improvement that I have not included but which might be used to simplify some of Chapter 2 is the observation of Lenstra that the criterion for Gorenstein rings to be complete intersections can be extended to more general rings which are finite and free as$\mathbf { Z } _ { p } { \mathrm { - m o d u l e s } }$Faltings has pointed out an improvement, also not included, which simplifies the argument in Chapter 3 and [TW]. This is however explained in the appendix to [TW].

It is a pleasure to thank those who read carefully a first draft of some of this paper after the Cambridge conference and particularly N. Katz who patiently answered many questions in the course of my work on Euler systems, and together with Illusie read critically the Euler system argument. Their questions led to my discovery of the problem with it. Katz also listened critically to my first attempts to correct it in the fall of 1993. I am grateful also to Taylor for his assistance in analyzing in depth the Euler system argument. I am indebted to F. Diamond for his generous assistance in the preparation of the final version of this paper. In addition to his many valuable suggestions, several others also made helpful comments and suggestions especially Conrad, de Shalit, Faltings, Ribet, Rubin, Skinner and Taylor.I am most grateful to H. Darmon for his encouragement to reconsider my old argument. Although I paid no heed to his advice at the time, it surely left its mark.

## Table of Contents

Chapter 1 1. Deformations of Galois representations

2. Some computations of cohomology groups

3. Some results on subgroups of$\operatorname { G L _ { 2 } } ( k )$

Chapter 2 1. The Gorenstein property

2. Congruences between Hecke rings

3. The main conjectures

Chapter 3 Estimates for the Selmer group

Chapter 4 1. The ordinary CM case

2. Calculation of η

Chapter 5 Application to elliptic curves

Appendix

References

## Chapter 1

This chapter is devoted to the study of certain Galois representations. In the first section we introduce and study Mazur’s deformation theory and discuss various refinements of it. These refinements will be needed later to make precise the correspondence between the universal deformation rings and the Hecke rings in Chapter 2. The main results needed are Proposition 1.2 which is used to interpret various generalized cotangent spaces as Selmer groups and (1.7) which later will be used to study them. At the end of the section we relate these Selmer groups to ones used in the Bloch-Kato conjecture, but this connection is not needed for the proofs of our main results.

In the second section we extract from the results of Poitou and Tate on Galois cohomology certain general relations between Selmer groups as Σ varies, as well as between Selmer groups and their duals. The most important observation of the third section is Lemma 1.10(i) which guarantees the existence of the special primes used in Chapter 3 and [TW].

## 1. Deformations of Galois representations

Let$p$be an odd prime. Let Σ be a finite set of primes including p and let$\mathbf { Q } _ { \Sigma }$be the maximal extension of Q unramified outside this set and$\infty$ Throughout we fix an embedding of Q, and so also of$\mathbf { Q } _ { \Sigma }$, in C. We will also fix a choice of decomposition group$D _ { q }$for all primes$q$in Z. Suppose that k is a finite field characteristic$p$and that

$$
\rho_ {0}: \operatorname{Gal} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}) \to \operatorname{GL} _ {2} (k)\tag{1.1}
$$

is an irreducible representation. In contrast to the introduction we will assume in the rest of the paper that$\rho _ { 0 }$comes with its field of definition k. Suppose further that det$\rho _ { 0 }$is odd. In particular this implies that the smallest field of definition for$\rho _ { 0 }$is given by the field$k _ { 0 }$generated by the traces but we will not assume that$k = k _ { 0 }$. It also implies that$\rho _ { 0 }$is absolutely irreducible. We consider the deformation$[ \rho ]$to$\operatorname { G L _ { 2 } } ( A )$of$\rho _ { 0 }$in the sense of Mazur [Ma1]. Thus if W(k) is the ring of Witt vectors of$k , A$is to be a complete Noeterian local W(k)-algebra with residue field k and maximal ideal$m .$, and a deformation$[ \rho ]$ is just a strict equivalence class of homomorphisms$\rho : \operatorname { G a l } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } ) \to \operatorname { G L } _ { 2 } ( A )$ such that$\rho$mod$m = \rho _ { 0 }$, two such homomorphisms being called strictly equivalent if one can be brought to the other by conjugation by an element of ker :$\mathrm { { G L } } _ { 2 } ( A ) \ \longrightarrow \ \mathrm { { G L } } _ { 2 } ( k )$. We often simply write$\rho$instead of$[ \rho ]$for the equivalent class.

We will restrict our choice of$\rho _ { 0 }$further by assuming that either:

(i)$\rho _ { 0 }$is ordinary; viz., the restriction of$\rho _ { 0 }$to the decomposition group$D _ { p }$ has (for a suitable choice of basis) the form

$$
\rho_ {0} | _ {D _ {p}} \approx \left( \begin{array}{c c} \chi_ {1} & * \\ 0 & \chi_ {2} \end{array} \right)\tag{1.2}
$$

where$\chi _ { 1 }$and$\chi _ { 2 }$are homomorphisms from$D _ { p }$to$k ^ { * }$with$\chi _ { 2 }$unramified. Moreover we require that$\chi _ { 1 } ~ \neq ~ \chi _ { 2 }$. We do allow here that$\rho _ { 0 } | _ { D _ { p } }$be semisimple. (If$\chi _ { 1 }$and$\chi _ { 2 }$are both unramified and$\rho _ { 0 } | _ { D _ { p } }$is semisimple then we fix our choices of$\chi _ { 1 }$and$\chi _ { 2 }$once and for all.)

(ii)$\rho _ { 0 }$is flat at$p$but not ordinary (cf. [Se1] where the terminology finite is used); viz.,$\rho _ { 0 } | _ { D _ { p } }$is the representation associated to a finite flat group scheme over$\mathbf { Z } _ { p }$but is not ordinary in the sense of (i). (In general when we refer to the flat case we will mean that$\rho _ { 0 }$is assumed not to be ordinary unless we specify otherwise.) We will assume also that det$\rho _ { 0 } | _ { I _ { p } } ~ = ~ \omega$ where$I _ { p }$is an inertia group at$p$and$\omega$is the Teichm¨uller character giving the action on$p ^ { \mathrm { t h } }$roots of unity.

In case (ii) it follows from results of Raynaud that$\rho _ { 0 } | _ { D _ { p } }$is absolutely irreducible and one can describe$\rho _ { 0 } | _ { I _ { p } }$explicitly. For extending a Jordan-H¨older series for the representation space (as an$I _ { p } { \mathrm { - m o d u l e } } )$to one for finite flat group schemes (cf. [Ray 1]) we observe first that the trivial character does not occur on a subquotient, as otherwise (using the classification of Oort-Tate or Raynaud) the group scheme would be ordinary. So we find by Raynaud’s results, that $\rho _ { 0 } \big | _ { I _ { p } } \otimes _ { k } \tilde { k } \simeq \psi _ { 1 } \oplus \psi _ { 2 }$where$\psi _ { 1 }$and$\psi _ { 2 }$are the two fundamental characters of degree 2 (cf. Corollary 3.4.4 of [Ray1]). Since$\psi _ { 1 }$and$\psi _ { 2 }$do not extend to characters of$\mathrm { G a l } ( \bar { \mathbf { Q } } _ { p } / \mathbf { Q } _ { p } ) , \rho _ { 0 } | _ { D _ { p } }$must be absolutely irreducible.

We sometimes wish to make one of the following restrictions on the deformations we allow:

(i) (a) Selmer deformations. In this case we assume that$\rho _ { 0 }$is ordinary, with notion as above, and that the deformation has a representative $\rho : { \mathrm { G a l } } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } ) \to { \mathrm { G L } } _ { 2 } ( A )$with the property that (for a suitable choice of basis)

$$
\rho | _ {D _ {p}} \approx \left( \begin{array}{c c} \tilde {\chi} _ {1} & * \\ 0 & \tilde {\chi} _ {2} \end{array} \right)
$$

with$\tilde { \chi } _ { 2 }$unramified,$\tilde { \chi } \equiv \chi _ { 2 }$mod$m .$, and det$\rho | _ { I _ { p } } = \varepsilon \omega ^ { - 1 } \chi _ { 1 } \chi _ { 2 }$where $\varepsilon$is the cyclotomic character,$\varepsilon : \operatorname { G a l } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } ) \to \mathbf { \dot { Z } } _ { p } ^ { * } .$, giving the action on all p-power roots of unity, ω is of order prime to$p$satisfying$\omega \equiv \varepsilon$ mod$p ,$and$\chi _ { 1 }$and$\chi _ { 2 }$are the characters of (i) viewed as taking values in $k ^ { * } \hookrightarrow A ^ { * }$

(i) (b) Ordinary deformations. The same as in (i)(a) but with no condition on the determinant.

(i) (c) Strict deformations. This is a variant on (i) (a) which we only use when $\rho _ { 0 } | _ { D _ { p } }$is not semisimple and not flat (i.e. not associated to a finite flat group scheme). We also assume that$\chi _ { 1 } \chi _ { 2 } ^ { - 1 } = \omega$in this case. Then a strict deformation is as in$( \mathrm { i } ) ( \mathrm { a } )$except that we assume in addition that $( \tilde { \chi } _ { 1 } / \tilde { \chi } _ { 2 } ) | _ { D _ { p } } = \varepsilon$

(ii) Flat (at p) deformations. We assume that each deformation$\rho$to$\operatorname { G L _ { 2 } } ( A )$ has the property that for any quotient$A / { \mathfrak { a } }$of finite order$\rho | _ { D _ { p } }$mod a is the Galois representation associated to the$\bar { \mathbf { Q } } _ { p } { \mathrm { - } } \mathrm { p o i n t s }$of a finite flat group scheme over$\mathbf { Z } _ { p }$

In each of these four cases, as well as in the unrestricted case (in which we impose no local restriction at$p )$one can verify that Mazur’s use of Schlessinger’s criteria [Sch] proves the existence of a universal deformation

$$
\rho : \operatorname{Gal} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}) \to \operatorname{GL} _ {2} (R).
$$

In the ordinary and restricted case this was proved by Mazur and in the flat case by Ramakrishna [Ram]. The other cases require minor modifications of Mazur’s argument. We denote the universal ring$R _ { \Sigma }$in the unrestricted case and$R _ { \Sigma } ^ { \mathrm { s e } } , \bar { R } _ { \Sigma } ^ { \mathrm { o r d } } , R _ { \Sigma } ^ { \mathrm { s t r } } , R _ { \Sigma } ^ { \mathrm { f } }$in the other four cases. We often omit the Σ if the context makes it clear.

There are certain generalizations to all of the above which we will also need. The first is that instead of considering$W ( k )$-algebras A we may consider O-algebras for O the ring of integers of any local field with residue field k. If we need to record which O we are using we will write$R _ { \Sigma , \mathcal { O } }$etc. It is easy to see that the natural local map of local O-algebras

$$
R _ {\Sigma , \mathcal {O}} \to R _ {\Sigma} \underset {W (k)} {\otimes} \mathcal {O}
$$

is an isomorphism because for functorial reasons the map has a natural section which induces an isomorphism on Zariski tangent spaces at closed points, and one can then use Nakayama’s lemma. Note, however, hat if we change the residue field via$i : \hookrightarrow k ^ { \prime }$then we have a new deformation problem associated to the representation$\rho _ { 0 } ^ { \prime } = i \circ \rho _ { 0 }$. There is again a natural map of$W ( k ^ { \prime } )$ algebras

$$
R (\rho_ {0} ^ {\prime}) \to R \underset {W (k)} {\otimes} W (k ^ {\prime})
$$

which is an isomorphism on Zariski tangent spaces. One can check that this is again an isomorphism by considering the subring$R _ { 1 }$of$R ( \rho _ { 0 } ^ { \prime } )$defined as the subring of all elements whose reduction modulo the maximal ideal lies in$k .$ Since$R ( \rho _ { 0 } ^ { \prime } )$is a finite$R _ { \mathrm { 1 - m o d u l e } , \ R _ { \mathrm { 1 } } }$is also a complete local Noetherian ring with residue field k. The universal representation associated to$\rho _ { 0 } ^ { \prime }$is defined over$R _ { 1 }$and the universal property of R then defines a map$R \to R _ { 1 }$. So we obtain a section to the map$R ( \rho _ { 0 } ^ { \prime } )  R _ { \otimes _ { W ( k ) } } W ( k ^ { \prime } )$and the map is therefore an isomorphism. (I am grateful to Faltings for this observation.) We will also need to extend the consideration of O-algebras tp the restricted cases. In each case we can require A to be an O-algebra and again it is easy to see that $R _ { \Sigma , \mathcal { O } } \simeq R _ { \Sigma } \otimes _ { W ( k ) } \mathcal { O }$in each case.

The second generalization concerns primes$q \neq p$which are ramified in$\rho _ { 0 }$ We distinguish three special cases$\mathrm { ( t y p e s ~ ( A ) }$and (C) need not be disjoint):

(A)$\rho _ { 0 } | _ { D _ { q } } = \left( \begin{array} { c c } { { \chi _ { 1 } } } & { { * } } \\ { { } } & { { \chi _ { 2 } } } \end{array} \right)$for a suitable choice of basis, with$\chi _ { 1 }$and$\chi _ { 2 }$unramified, $\chi _ { 1 } \chi _ { 2 } ^ { - 1 } = \omega$and the fixed space of$I _ { q }$of dimension 1,

(B)$\rho _ { 0 } | _ { I _ { q } } = ( { \bf \Phi } _ { 0 } ^ { \chi _ { q } } { \bf \Phi } _ { 1 } ^ { 0 } ) , \chi _ { q } \ne 1$, for a suitable choice of basis,

(C)$H ^ { 1 } ( \mathbf { Q } _ { q } , W _ { \lambda } ) = 0$where$W _ { \lambda }$is as defined in (1.6).

Then in each case we can define a suitable deformation theory by imposing additional restrictions on those we have already considered, namely:

(A)$\rho | _ { D _ { q } } = { \left( \begin{array} { l l } { \psi _ { 1 } } & { * } \\ & { \psi _ { 2 } } \end{array} \right) }$for a suitable choice of basis of$A ^ { 2 }$with$\psi _ { 1 }$and$\psi _ { 2 }$unramified and$\psi _ { 1 } \psi _ { 2 } ^ { - 1 } = \varepsilon ;$

(B)$\rho | _ { I _ { q } } = ( { \ O } _ { 0 } ^ { \chi _ { q } } { } _ { 1 } ^ { 0 } )$for a suitable choice of basis$( \chi _ { q }$of order prime to$p ,$so the same character as above);

(C) det$\rho | _ { I _ { q } } = \operatorname* { d e t } \rho _ { 0 } | _ { I _ { q } }$, i.e., of order prime to$p .$

Thus if M is a set of primes in$\Sigma$distinct from p and each satisfying one of $( \mathrm { A } ) , ( \mathrm { B } ) \mathrm { o r ( C ) }$for$\rho _ { 0 }$, we will impose the corresponding restriction at each prime in$\mathcal { M }$

Thus to each set of data$\mathcal { D } = \{ \cdot , \Sigma , \mathcal { O } , \mathcal { M } \}$where · is$\mathrm { S e }$, str, ord, flat or unrestricted, we can associate a deformation theory to$\rho _ { 0 }$provided

$$
\rho_ {0}: \operatorname{Gal} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}) \to \operatorname{GL} _ {2} (k)\tag{1.3}
$$

is itself of type D and O is the ring of integers of a totally ramified extension of$W ( k ) ; \rho _ { 0 }$is ordinary if · is Se or ord, strict if · is strict and flat if · is fl (meaning flat);$\rho _ { 0 }$is of type M, i.e., of type (A), (B) or (C) at each ramified primes$q \neq p , q \in \mathcal { M }$. We allow diferent types at diferent$q \mathrm { ^ { \circ } s }$. We will refer to these as the standard deformation theories and write$R _ { \mathcal { D } }$for the universal ring associated to$\mathcal { D }$and$\rho _ { \mathcal { D } }$for the universal deformation (or even$\rho$if$\mathcal { D }$is clear from the context).

We note here that if$\mathcal { D } = ( \mathrm { o r d } , \Sigma , \mathcal { O } , \mathcal { M } )$and$\mathcal { D } ^ { \prime } = ( \mathrm { S e } , \Sigma , \mathcal { O } , \mathcal { M } )$then there is a simple relation between$R _ { \mathcal { D } }$and$R _ { { D ^ { \prime } } }$. Indeed there is a natural map

$R _ { D }  R _ { D ^ { \prime } }$by the universal property of$R _ { \mathcal { D } }$, and its kernel is a principal ideal generated by$T = \varepsilon ^ { - 1 } ( \gamma )$det$\rho _ { \mathcal { D } } ( \gamma ) - 1$where$\gamma \in \operatorname { G a l } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } )$is any element whose restriction to$\operatorname { G a l } ( \mathbf { Q } _ { \infty } / \mathbf { Q } )$is a generator (where$\mathbf { Q } _ { \infty }$is the$\mathbf { Z } _ { p } .$-extension of$\mathbf { Q } )$and whose restriction to$\operatorname { G a l } ( \mathbf { Q } ( \zeta _ { N _ { p } } ) / \mathbf { Q } )$is trivial for any N prime to p with$\zeta _ { N } \in \mathbf { Q } _ { \Sigma } , \zeta _ { N }$being a primitive$N ^ { \mathrm { t h } }$root of 1:

$$
R _ {\mathcal {D}} / T \simeq R _ {\mathcal {D}} ^ {\prime}.\tag{1.4}
$$

It turns out that under the hypothesis that$\rho _ { 0 }$is strict, i.e. that$\rho _ { 0 } | _ { D _ { \boldsymbol { \tau } } }$ is not associated to a finite flat group scheme, the deformation problems in $( \mathrm { i } ) ( \mathrm { a } )$and$( \mathrm { i } ) ( \mathrm { c } )$are the same; i.e., every Selmer deformation is already a strict deformation. This was observed by Diamond. the argument is local, so the decomposition group$D _ { p }$could be replaced by$\operatorname { G a l } ( { \bar { \mathbf { Q } } } _ { p } / \mathbf { Q } )$

Proposition 1.1 (Diamond). Suppose that$\pi : D _ { p } \to { \mathrm { G L } } _ { 2 } ( A )$is a continuous representation where A is an Artinian local ring with residue field k, a finite field of characteristic p. Suppose$\pi \approx ( { \stackrel { \chi _ { 1 } \varepsilon } { \ 0 } } ^ { \ast } )$with$\chi _ { 1 }$and$\chi _ { 2 }$unramified and$\chi _ { 1 } \neq \chi _ { 2 }$. Then the residual representation π¯ is associated to a finite flat group scheme over$\mathbf { Z } _ { p }$

Proof (taken from [Dia, Prop. 6.1]). We may replace π by$\pi \otimes \chi _ { 2 } ^ { - 1 }$and we let$\varphi = \chi _ { 1 } \chi _ { 2 } ^ { - 1 }$. Then$\pi \cong ( { \varphi } \varepsilon _ { 1 } )$determines a cocycle$t : D _ { p } \longrightarrow M ( 1 )$where M is a free A-module of rank one on which$D _ { p }$acts via$\varphi .$. Let u denote the cohomology class in$H ^ { 1 } ( D _ { p } , M ( 1 ) )$defined by t, and let$u _ { 0 }$denote its image in$H ^ { 1 } ( D _ { p } , M _ { 0 } ( 1 ) )$where$M _ { 0 } = M / { \mathfrak { m } } M$. Let$G =$ker$\varphi$and let$F$be the fixed field of G (so F is a finite unramified extension of$\mathbf { Q } _ { p } )$. Choose n so that$p ^ { n } A$ $= ~ 0$. Since$H ^ { 2 } ( G , \mu _ { p ^ { r } } \to H ^ { 2 } ( G , \mu _ { p ^ { s } } )$is injective for$r \ \leq \ s .$, we see that the natural map of$A [ D _ { p } / G ]$-modules$H ^ { 1 } ( G , \mu _ { p ^ { n } } \otimes _ { \mathbf { Z } _ { p } } M ) \to H ^ { 1 } ( G , M ( 1 ) )$is an isomorphism. By Kummer theory, we have$H ^ { 1 } ( G , M ( 1 ) ) \cong F ^ { \times } / ( F ^ { \times } ) ^ { p ^ { n } } \otimes _ { \mathbf { Z } _ { p } } M$ as$D _ { p }$-modules. Now consider the commutative diagram

$$
\begin{array}{c} H ^ {1} (G, M (1)) ^ {D _ {p}} \xrightarrow {\sim} ((F ^ {\times} / (F ^ {\times}) ^ {p ^ {n}} \otimes_ {\mathbf {Z} _ {p}} M) ^ {D _ {p}} \xrightarrow {} M ^ {D _ {p}} \\ \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow \qquad \qquad \qquad \Biggl \downarrow , \\ H ^ {1} (G, M _ {0} (1)) \xrightarrow {\sim} (F ^ {\times} / (F ^ {\times}) ^ {p}) \otimes_ {\mathbf {F} _ {p}} M _ {0} \xrightarrow {} M _ {0} \end{array}
$$

where the right-hand horizontal maps are induced by$v _ { p } : F ^ { \times } \to \mathbf { Z }$. If$\varphi \neq 1$ then$M ^ { D _ { p } } \subset { \mathfrak { m } } M .$, so that the element res$u _ { 0 }$of$H ^ { 1 } ( G , \dot { M } _ { 0 } ( 1 ) )$is in the image of$( \mathcal { O } _ { F } ^ { \times } / ( \mathcal { O } _ { F } ^ { \times } ) ^ { p } ) \otimes _ { \mathbf { F } _ { p } } M _ { 0 }$. But this means that ¯π is “peu ramifi´e” in the sense of [Se] and therefore ¯π comes from a finite flat group scheme. (See [E1, (8.20].)

Remark. Diamond also observes that essentially the same proof shows that if$\pi : \operatorname { G a l } ( { \bar { \mathbf { Q } } } _ { q } / \mathbf { Q } _ { q } ) \to \operatorname { G L } _ { 2 } ( A )$, where A is a complete local Noetherian ring with residue field k, has the form$\pi | _ { I _ { q } } \cong ( _ { 0 1 } ^ { 1 * } )$with ¯π ramified then π is of type (A).

Globally, Proposition 1.1 says that if$\rho _ { 0 }$is strict and if$\mathcal { D } = ( \mathrm { S e } , \Sigma , \mathcal { O } , \mathcal { M } )$ and$\mathcal { D } ^ { \prime } = ( \mathrm { s t r } , \Sigma , \mathcal { O } , \mathcal { M } )$then the natural map$R _ { D }  R _ { D ^ { \prime } }$is an isomorphism.

In each case the tangent space of$R _ { \mathcal { D } }$may be computed as in [Ma1]. Let λ be a uniformizer for O and let$U _ { \lambda } \simeq k ^ { 2 }$be the representation space for$\rho _ { 0 }$ (The motivation for the subscript λ will become apparent later.) Let$V _ { \lambda }$be the representation space of$\operatorname { G a l } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } )$on$\mathrm { A d } \rho _ { 0 } = \mathrm { H o m } _ { k } ( U _ { \lambda } , U _ { \lambda } ) \simeq M _ { 2 } ( k )$. Then there is an isomorphism of k-vector spaces (cf. the proof of Prop. 1.2 below)

$$
\mathrm{Hom} _ {k} (m _ {\mathcal {D}} / (m _ {\mathcal {D}} ^ {2}, \lambda), k) \simeq H _ {\mathcal {D}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V _ {\lambda})\tag{1.5}
$$

where$H _ { \mathcal { D } } ^ { 1 } ( \mathrm { Q } _ { \Sigma } / \mathrm { Q } , V _ { \lambda } )$is a subspace of$H ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V _ { \lambda } )$which we now describe and$m _ { D }$is the maximal ideal of$R _ { C } a l D$. It consists of the cohomology classes which satisfy certain local restrictions at p and at the primes in M. We call $m _ { \mathscr D } / ( m _ { \mathscr D } ^ { 2 } , \lambda )$the reduced cotangent space of$R _ { \mathcal { D } }$

We begin with$p .$. First we may write (since$p \neq 2 )$, as$k [ \mathrm { G a l } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } ) ] \mathrm { . }$ modules,

$$
\begin{array}{c} V _ {\lambda} = W _ {\lambda} \oplus k, \text {where} W _ {\lambda} = \{f \in \operatorname{Hom} _ {k} (U _ {\lambda}, U _ {\lambda}): \operatorname{trace} f = 0 \} \\ \simeq (\operatorname{Sym} ^ {2} \otimes \det ^ {- 1}) \rho_ {0} \end{array}\tag{1.6}
$$

and k is the one-dimensional subspace of scalar multiplications. Then if$\rho _ { 0 }$ is ordinary the action of$D _ { p }$on$U _ { \lambda }$induces a filtration of$U _ { \lambda }$and also on$W _ { \lambda }$ and$V _ { \lambda }$. Suppose we write these$0 \subset U _ { \lambda } ^ { 0 } \subset U _ { \lambda } , \ 0 \subset W _ { \lambda } ^ { 0 } \subset W _ { \lambda } ^ { 1 } \subset W _ { \lambda }$and $0 \subset V _ { \lambda } ^ { 0 } \subset V _ { \lambda } ^ { 1 } \subset V _ { \lambda }$. Thus$U _ { \lambda } ^ { 0 }$is defined by the requirement that$D _ { p }$act on it via the character χ<sub>1</sub> (cf. (1.2)) and on$U _ { \lambda } / U _ { \lambda } ^ { 0 }$via$\chi _ { 2 }$. For$W _ { \lambda }$the filtrations are defined by

$$
\begin{array}{r c l} W _ {\lambda} ^ {1} & = & \{f \in W _ {\lambda}: f (U _ {\lambda} ^ {0}) \subset U _ {\lambda} ^ {0} \}, \\ W _ {\lambda} ^ {0} & = & \{f \in W _ {\lambda} ^ {1}: f = 0 \text {on} U _ {\lambda} ^ {0} \}, \end{array}
$$

and the filtrations for$V _ { \lambda }$are obtained by replacing W by V. We note that these filtrations are often characterized by the action of$D _ { p }$. Thus the action of$D _ { p }$on$W _ { \lambda } ^ { 0 }$is via$\chi _ { 1 } / \chi _ { 2 } ;$on$W _ { \lambda } ^ { 1 } / W _ { \lambda } ^ { 0 }$it is trivial and on$Q _ { \lambda } / W _ { \lambda } ^ { 1 }$it is via $\chi _ { 2 } / \chi _ { 1 }$. These determine the filtration if either$\chi _ { 1 } / \chi _ { 2 }$is not quadratic or$\rho _ { 0 } | _ { D _ { p } }$ is not semisimple. We define the k-vector spaces

$$
V _ {\lambda} ^ {\mathrm{ord}} = \{f \in V _ {\lambda} ^ {1}: f = 0 \text {in} \operatorname{Hom} (U _ {\lambda} / U _ {\lambda} ^ {0}, U _ {\lambda} / U _ {\lambda} ^ {0}) \},
$$

$$
H _ {\mathrm{Se}} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda}) = \ker \{H ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda}) \to H ^ {1} (\mathbf {Q} _ {p} ^ {\mathrm{unr}}, V _ {\lambda} / W _ {\lambda} ^ {0}) \},
$$

$$
H _ {\mathrm{ord}} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda}) = \ker \{H ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda}) \to H ^ {1} (\mathbf {Q} _ {p} ^ {\mathrm{unr}}, V _ {\lambda} / V _ {\lambda} ^ {\mathrm{ord}}) \},
$$

$$
H _ {\mathrm{str}} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda}) = \ker \left\{H ^ {1} \left(\mathbf {Q} _ {p}, V _ {\lambda}\right)\rightarrow H ^ {1} \left(\mathbf {Q} _ {p}, W _ {\lambda} / W _ {\lambda} ^ {0}\right) \oplus H ^ {1} \left(\mathbf {Q} _ {p} ^ {\mathrm{unr}}, k\right)\right\}.
$$

In the Selmer case we make an analogous definition for$H _ { \mathrm { S e } } ^ { 1 } ( \mathbf { Q } _ { p } , W _ { \lambda } )$by replacing$V _ { \lambda }$by$W _ { \lambda } ,$and similarly in the strict case. In the flat case we use the fact that there is a natural isomorphism of k-vector spaces

$$
H ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda}) \to \mathrm{Ext} _ {k [ D _ {p} ]} ^ {1} (U _ {\lambda}, U _ {\lambda})
$$

where the extensions are computed in the category of k-vector spaces with local Galois action. Then$H _ { \mathrm { f } } ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda } )$is defined as the k-subspace of$H ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda } )$ which is the inverse image of$\operatorname { E x t } _ { \mathrm { f l } } ^ { 1 } ( G , G )$, the group of extensions in the category of finite flat commutative group schemes over$\mathbf { Z } _ { p }$killed by$p , G$being the (unique) finite flat group scheme over$\mathbf { Z } _ { p }$associated to$U _ { \lambda }$. By [Ray1] all such extensions in the inverse image even correspond to k-vector space schemes. For more details and calculations see [Ram].

For q diferent from p and$q \in \mathcal { M }$we have three cases (A), (B), (C). In case$( \mathrm { A } )$there is a filtration by$D _ { q }$entirely analogous to the one for$p .$We write this$0 \subset W _ { \lambda } ^ { 0 , q } \subset W _ { \lambda } ^ { 1 , q } \subset W _ { \lambda }$and we set

$$
H _ {D _ {q}} ^ {1} (\mathbf {Q} _ {q}, V _ {\lambda}) = \left\{ \begin{array}{l l} \ker : H ^ {1} (\mathbf {Q} _ {q}, V _ {\lambda} \\ \qquad \to H ^ {1} (\mathbf {Q} _ {q}, W _ {\lambda} / W _ {\lambda} ^ {0, q}) \oplus H ^ {1} (\mathbf {Q} _ {q} ^ {\mathrm{unr}}, k) \text {in case (A)} \\ \ker : H ^ {1} (\mathbf {Q} _ {q}, V _ {\lambda}) \\ \qquad \to H ^ {1} (\mathbf {Q} _ {q} ^ {\mathrm{unr}}, V _ {\lambda}) & \text {in case (B) or (C)}. \end{array} \right.
$$

Again we make an analogous definition for$H _ { D _ { a } } ^ { 1 } ( \mathbf { Q } _ { q } , W _ { \lambda } )$by replacing$V _ { \lambda }$ by$W _ { \lambda }$and deleting the last term in case$( \mathrm { A } )$. We now define the k-vector space$H _ { \mathcal { D } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V _ { \lambda } )$as

$$
\begin{array}{c} H _ {\mathcal {D}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V _ {\lambda}) = \{\alpha \in H ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V _ {\lambda}): \alpha_ {q} \in H _ {D _ {q}} ^ {1} (\mathbf {Q} _ {q}, V _ {\lambda}) \text {for all} q \in \mathcal {M}, \\ \alpha_ {q} \in H _ {*} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda}) \} \end{array}
$$

where ∗ is$\mathrm { S e } ,$str, ord, fl or unrestricted according to the type of D. A similar definition applies to$H _ { \mathcal { D } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , W _ { \lambda } )$if · is Selmer or strict.

Now and for the rest of the section we are going to assume that$\rho _ { 0 }$arises from the reduction of the λ-adic representation associated to an eigenform. More precisely we assume that there is a normalized eigenform$f$of weight 2 and level$N$, divisible only by the primes in$\Sigma ,$and that there ia a prime$\lambda$ of$\mathcal { O } _ { f }$such that$\rho _ { 0 } = \rho _ { f , \lambda }$mod λ. Here${ \mathcal { O } } _ { f }$is the ring of integers of the field generated by the Fourier coeficients of f so the fields of definition of the two representations need not be the same. However we assume that$k \supseteq \mathcal { O } _ { f , \lambda } / \lambda$ and we fix such an embedding so the comparison can be made over k. It will be convenient moreover to assume that if we are considering$\rho _ { 0 }$as being of type$\mathcal { D }$then$\mathcal { D }$is defined using O-algebras where${ \mathcal { O } } \supseteq { \mathcal { O } } _ { f , \lambda }$is an unramified extension whose residue field is k. (Although this condition is unnecessary, it is convenient to use λ as the uniformizer for O.) Finally we assume that$\rho _ { f , \lambda }$ itself is of type D. Again this is a slight abuse of terminology as we are really considering the extension of scalars$\rho _ { f , \lambda } \bigotimes _ { \mathscr { O } _ { f , \lambda } } \mathcal { O }$and not$\rho _ { f , \lambda }$itself, but we will

do this without further mention if the context makes it clear. (The analysis of this section actually applies to any characteristic zero lifting of$\rho _ { 0 }$but in all our applications we will be in the more restrictive context we have described here.)

With these hypotheses there is a unique local homomorphism$R _ { \mathcal { D } }  \mathcal { O }$ of O-algebras which takes the universal deformation to (the class of)$\rho _ { f , \lambda }$. Let ${ \mathfrak { p } } _ { \mathcal { D } } = \ker : R _ { \mathcal { D } }  \mathcal { O }$. Let K be the field of fractions of O and let$U _ { f } = \dot { ( K / \mathcal { O } ) } ^ { 2 }$ with the Galois action taken from$\rho _ { f , \lambda }$. Similarly, let$V _ { f } = \mathrm { A d } \rho _ { f , \lambda } \otimes _ { \mathcal { O } } K / \mathcal { O } \simeq$ $( K / \mathcal { O } ) ^ { 4 }$with the adjoint representation so that

$$
V _ {f} \simeq W _ {f} \oplus K / \mathcal {O}
$$

where$W _ { f }$has Galois action via$\mathrm { S y m } ^ { 2 } \rho _ { f , \lambda } \otimes$det$\rho _ { f , \lambda } ^ { - 1 }$and the action on the second factor is trivial. Then if$\rho _ { 0 }$is ordinary the filtration of$U _ { f }$under the $\operatorname { A d } \rho$action of$D _ { p }$induces one on$W _ { f }$which we write$0 \subset W _ { f } ^ { 0 } \subset \joinrel \subset W _ { f } ^ { 1 } \subset W _ { f }$ Often to simplify the notation we will drop the index$f$from$\dot { W _ { f } ^ { 1 } } , V _ { f }$etc. There is also a filtration on$W _ { \lambda ^ { n } } = \{ \mathrm { k e r } \lambda ^ { n } : W _ { f }  W _ { f } \}$given by$\psi _ { \lambda ^ { n } } ^ { \dot { i } } = W ^ { \lambda ^ { n } } \cap W ^ { i }$ (compatible with our previous description for$n = 1 )$. Likewise we write$V _ { \lambda ^ { n } }$ for {ker$\lambda ^ { n } : V _ { f }  V _ { f } \}$

We now explain how to extend the definition of$H _ { \mathcal { D } } ^ { 1 }$to give meaning to $H _ { \mathcal { D } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V _ { \lambda ^ { n } } )$and$H _ { \mathcal { D } } ^ { 1 } ( \mathcal { Q } _ { \Sigma } / \mathbf { Q } , V )$and these are$\mathcal { O } / \lambda ^ { n }$and O-modules, respectively. In the case where$\rho _ { 0 }$is ordinary the definitions are the same with $V _ { \lambda ^ { n } }$or$V$replacing$V _ { \lambda }$and$\mathcal { O } / \lambda ^ { n }$or$K / \mathcal { O }$replacing k. One checks easily that as O-modules

$$
H _ {\mathcal {D}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V _ {\lambda^ {n}}) \simeq H _ {\mathcal {D}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V) _ {\lambda^ {n}},\tag{1.7}
$$

where as usual the subscript$\lambda ^ { n }$denotes the kernel of multiplication by$\lambda ^ { n }$ This just uses the divisibility of$H ^ { 0 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V )$and$H ^ { 0 } ( \mathbf { Q } _ { p } , W / W ^ { 0 } )$in the strict case. In the Selmer case one checks that for$m > n$the kernel of

$$
H ^ {1} (\mathbf {Q} _ {p} ^ {\mathrm{unr}}, V _ {\lambda^ {n}} / W _ {\lambda^ {n}} ^ {0}) \rightarrow H ^ {1} (\mathbf {Q} _ {p} ^ {\mathrm{unr}}, V _ {\lambda^ {m}} / W _ {\lambda^ {m}} ^ {0})
$$

has only the zero element fixed under$\operatorname { G a l } ( \mathbf { Q } _ { p } ^ { \mathrm { u n r } } / \mathbf { Q } _ { p } )$and the ord case is similar. Checking conditions at$q \in \mathcal { M }$is dome with similar arguments. In the Selmer and strict cases we make analogous definitions with$W _ { \lambda ^ { n } }$in place of$V _ { \lambda ^ { n } }$and W in place of V and the analogue of (1.7) still holds.

We now consider the case where$\rho _ { 0 }$is flat (but not ordinary). We claim first that there is a natural map of O-modules

$$
H ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda_ {n}}) \to \mathrm{Ext} _ {\mathcal {O} [ D _ {p} ]} ^ {1} (U _ {\lambda^ {m}}, U _ {\lambda^ {n}})\tag{1.8}
$$

for each$m \ \geq \ n$where the extensions are of O-modules with local Galois action. To describe this suppose that$\alpha \in H ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } )$. Then we can associate to α a representation$\rho _ { \alpha } : \mathrm { G a l } ( \bar { \mathbf { Q } } _ { p } / \mathbf { Q } _ { p } ) \to \bar { \mathrm { G L } } _ { 2 } ( { \mathcal { O } } _ { n } [ \varepsilon ] )$(where$\mathcal { O } _ { n } [ \varepsilon ] =$ $\mathcal { O } [ \varepsilon ] / ( \lambda ^ { n } \varepsilon , \varepsilon ^ { 2 } ) )$which is an O-algebra deformation of$\rho _ { 0 }$(see the proof of Proposition 1.1 below). Let$E = \mathcal { O } _ { n } [ \varepsilon ] ^ { 2 }$where the Galois action is via$\rho _ { \alpha }$. Then there is an exact sequence

$$
\begin{array}{c c c c c c c c} 0 & \longrightarrow & \varepsilon E / \lambda^ {m} & \longrightarrow & E / \lambda^ {m} & \longrightarrow & (E / \varepsilon) / \lambda^ {m} & \longrightarrow & 0 \\ & & | \wr & & & & | \wr & & \\ & & U _ {\lambda^ {n}} & & & & U _ {\lambda^ {m}} & \end{array}
$$

and hence an extension class in$\mathrm { E x t } ^ { 1 } ( U _ { \lambda ^ { m } } , U _ { \lambda ^ { n } } )$. One checks now that (1.8) is a map of O-modules. We define$H _ { f } ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } )$to be the inverse image of $\mathrm { E x t } _ { \mathrm { f l } } ^ { 1 } ( U _ { \lambda ^ { n } } , U _ { \lambda _ { n } } )$under (1.8), i.e., those extensions which are already extensions in the category of finite flat group schemes$\mathbf { Z } _ { p }$. Observe that$\mathrm { E x t } _ { \mathrm { f l } } ^ { 1 } ( U _ { \lambda ^ { n } } , U _ { \lambda ^ { n } } ) \cap$ $\mathrm { E x t } _ { \mathcal { O } [ D _ { v } ] } ^ { 1 } ( U _ { \lambda ^ { n } } , U _ { \lambda ^ { n } } )$is an O-module, so$H _ { \mathrm { f } } ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } )$is seen to be an O-submodule of$H ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda _ { n } } )$. We observe that our definition is equivalent to requiring that the classes in$H _ { \mathrm { f } } ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } )$map under (1.8) to$\mathrm { E x t } _ { \mathrm { f l } } ^ { 1 } ( U _ { \lambda ^ { m } } , U _ { \lambda ^ { n } } )$for all $m \geq n$. For if$e _ { m }$is the extension class in$\mathrm { E x t } ^ { 1 } ( U _ { \lambda ^ { m } } , U _ { \lambda ^ { n } } )$then$e _ { m } \hookrightarrow e _ { n } \oplus U _ { \lambda ^ { m } }$ as Galois-modules and we can apply results of [Ray1] to see that$e _ { m }$comes from a finite flat group scheme over$\mathbf { Z } _ { p }$if$e _ { n }$does.

In the flat (non-ordinary) case$\rho _ { 0 } | _ { I _ { p } }$is determined by Raynaud’s results as mentioned at the beginning of the chapter. It follows in particular that, since $\rho _ { 0 } | _ { D _ { p } }$is absolutely irreducible,$V ( \mathbf { Q } _ { p } \ : = \ : H ^ { 0 } ( \mathbf { Q } _ { p } , V )$is divisible in this case (in fact$V ( \mathbf { Q } _ { p } ) \simeq K T / \mathcal { O } )$). This$H ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } ) \simeq H ^ { 1 } ( \mathbf { Q } _ { p } , V ) _ { \lambda ^ { n } }$and hence we can define

$$
H _ {\mathrm{f}} ^ {1} (\mathbf {Q} _ {p}, V) = \bigcup_ {n = 1} ^ {\infty} H _ {\mathrm{f}} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}),
$$

and we claim that$H _ { \mathrm { f } } ^ { 1 } ( \mathbf { Q } _ { p } , V ) _ { \lambda ^ { n } } \simeq H _ { \mathrm { f } } ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } )$. To see this we have to compare representations for$m \geq n$

$$
\begin{array}{c c c} \rho_ {n, m}: \operatorname{Gal} (\bar {\mathbf {Q}} _ {p} / \mathbf {Q} _ {p}) & \longrightarrow & \operatorname{GL} _ {2} (\mathcal {O} _ {n} [ \varepsilon ] / \lambda^ {m}) \\ \Big \| & & \Big \downarrow_ {\varphi_ {m, n}} \\ \rho_ {m, m}: \operatorname{Gal} (\bar {\mathbf {Q}} _ {p} / \mathbf {Q} _ {p}) & \longrightarrow & \operatorname{GL} _ {2} (\mathcal {O} _ {m} [ \varepsilon ] / \lambda^ {m}) \end{array}
$$

where$\rho _ { n , m }$and$\rho _ { m , m }$are obtained from$\alpha _ { n } \in H ^ { 1 } ( \mathbf { Q } _ { p } , V X _ { \lambda ^ { n } } )$and$\mathrm { i m } ( \alpha _ { n } ) \in$ $H ^ { 1 } ( \mathbf { Q } _ { p } , \dot { V } _ { \lambda ^ { m } } )$and$\varphi _ { m , n } : a + b \varepsilon  a + \lambda ^ { m - n } b \varepsilon$. By [Ram, Prop 1.1 and Lemma 2.1] if$\rho _ { n , m }$comes from a finite flat group scheme then so does$\rho _ { m , m }$. Conversely $\varphi _ { m , n }$is injective and so$\rho _ { n , m }$comes from a finite flat group scheme if$\rho _ { m , m }$does; cf. [Ray1]. The definitions of$H _ { \mathcal { D } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V _ { \lambda ^ { n } } )$and$H _ { \mathcal { D } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V )$now extend to the flat case and we note that (1.7) is also valid in the flat case.

Still in the flat (non-ordinary) case we can again use the determination of$\rho _ { 0 } | _ { I _ { p } }$to see that$\dot { H } ^ { 1 } ( \mathbf { Q } _ { p } , V )$is divisible. For it is enough to check that $H ^ { 2 } ( \mathbf { Q } _ { p } , V _ { \lambda } ) = 0$and this follows by duality from the fact that$H ^ { 0 } ( \mathbf { Q } _ { p } , V _ { \lambda } ^ { * } ) = 0$ where$V _ { \lambda } ^ { * } = \operatorname { H o m } ( V _ { \lambda } , \pmb { \mu } _ { p } )$and$\mu _ { p }$is the group of$p ^ { \mathrm { t h } }$roots of unity. (Again this follows from the explicit form of$\rho _ { 0 } | _ { D _ { p } } . )$Much subtler is the fact that $H _ { \mathrm { f } } ^ { 1 } ( \mathbf { Q } _ { p } , V )$is divisible. This result is essentially due to Ramakrishna. For, using a local version of Proposition 1.1 below we have that

$$
\mathrm{Hom} _ {\mathcal {O}} (\mathfrak {p} _ {R} / \mathfrak {p} _ {R} ^ {2}, K / \mathcal {O}) \simeq H _ {\mathrm{f}} ^ {1} (\mathbf {Q} _ {p}, V)
$$

where R is the universal local flat deformation ring for$\rho _ { 0 } | _ { D _ { p } }$and O-algebras. (This exists by Theorem 1.1 of [Ram] because$\rho _ { 0 } | _ { D _ { p } }$is absolutely irreducible.) Since$R \simeq { R ^ { \mathrm { H } } \otimes _ { W ( k ) } \mathcal { O } }$where$R ^ { \mathrm { { f } } }$is the corresponding ring for W(k)-algebras the main theorem of [Ram, Th. 4.2] shows that R is a power series ring and the divisibility of$H _ { \mathrm { f } } ^ { 1 } ( \mathbf { Q } _ { p } , V )$then follows. We refer to [Ram] for more details about$R ^ { \mathrm { { f } } }$

Next we need an analogue of (1.5) for V. Again this is a variant of standard results in deformation theory and is given (at least for$\mathcal { D } = ( \mathrm { o r d } , \Sigma , W ( k ) , \phi )$ with some restriction on χ<sub>1</sub>, χ<sub>2</sub> in i(a)) in [MT, Prop 25].

Proposition 1.2. Suppose that$\rho _ { f , \lambda }$is a deformation of$\rho _ { 0 }$of type $\mathcal { D } = ( \cdot , \Sigma , \mathcal { O } , \mathcal { M } )$with O an unramified extension of$\mathcal { O } _ { f , \lambda }$. Then as O-modules

$$
\mathrm{Hom} _ {\mathcal {O}} (\mathfrak {p} _ {\mathcal {D}} / \mathfrak {p} _ {\mathcal {D}} ^ {2}, K / \mathcal {O}) \simeq H _ {\mathcal {D}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V).
$$

Remark. The isomorphism is functorial in an obvious way if one changes D to a larger$\mathcal { D } ^ { \prime }$

Proof. We will just describe the Selmer case with$\mathcal { M } = \phi$as the other cases use similar arguments. Suppose that α is a cocycle which represents a cohomology class in$H _ { \mathrm { S e } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V _ { \lambda ^ { n } } )$. Let$\mathcal { O } _ { n } [ \varepsilon ]$denote the ring$\mathcal { O } [ \varepsilon ] / ( \lambda ^ { n } \varepsilon , \varepsilon ^ { 2 } )$ We can associate to α a representation

$$
\rho_ {\alpha}: \operatorname{Gal} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}) \to \operatorname{GL} _ {2} (\mathcal {O} _ {n} [ \varepsilon ])
$$

as follows: set$\rho _ { \alpha } ( g ) = \alpha ( g ) \rho _ { f , \lambda } ( g )$where$\rho _ { f , \lambda } ( g )$, a priori in$\mathrm { G L _ { 2 } } ( { \mathcal { O } } )$, is viewed in$\mathrm { G L _ { 2 } } ( \mathcal { O } _ { n } [ \varepsilon ] )$via the natural mapping$\mathcal { O }  \mathcal { O } _ { n } [ \varepsilon ]$. Here a basis for$\mathcal { O } ^ { 2 }$ is chosen so that the representation$\rho _ { f , \lambda }$on the decomposition group$D _ { p } \subset$ $\operatorname { G a l } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } )$has the upper triangular form of$\mathrm { ( i ) ( a ) }$, and then$\alpha ( g ) \in V _ { \lambda ^ { n } }$is viewed in$\mathrm { G L _ { 2 } } ( \mathcal { O } _ { n } [ \varepsilon ] )$by identifying

$$
V _ {\lambda_ {n}} \simeq \bigg \{\left( \begin{array}{c c} 1 + y \varepsilon & x \varepsilon \\ z \varepsilon & 1 - t \varepsilon \end{array} \right) \bigg \} = \{\ker : \operatorname{GL} _ {2} (\mathcal {O} _ {n} [ \varepsilon ]) \to \operatorname{GL} _ {2} (\mathcal {O}) \}.
$$

Then

$$
W _ {\lambda^ {n}} ^ {0} = \bigg \{\left( \begin{array}{c c} 1 & x \varepsilon \\ & 1 \end{array} \right) \bigg \},
$$

$$
\begin{array}{l} W _ {\lambda^ {n}} ^ {1} = \Bigg \{\left( \begin{array}{c c} 1 + y \varepsilon & x \varepsilon \\ & 1 - y \varepsilon \end{array} \right) \Bigg \}, \\ W _ {\lambda^ {n}} = \Bigg \{\left( \begin{array}{c c} 1 + y \varepsilon & x \varepsilon \\ z \varepsilon & 1 - y \varepsilon \end{array} \right) \Bigg \}, \end{array}
$$

and

$$
V _ {\lambda^ {n}} ^ {1} = \bigg \{\left( \begin{array}{c c} 1 + y \varepsilon & x \varepsilon \\ & 1 - t \varepsilon \end{array} \right) \bigg \}.
$$

One checks readily that$\rho _ { \alpha }$is a continuous homomorphism and that the deformation$[ \rho _ { \alpha } ]$is unchanged if we add a coboundary to α.

We need to check that$[ \rho _ { \alpha } ]$is a Selmer deformation. Let$\mathcal { H } =$ $\mathrm { G a l } ( \bar { \mathbf { Q } } _ { p } / \mathbf { Q } _ { p } ^ { \mathrm { u n r } } )$and$\mathcal { G } = \operatorname { G a l } ( \mathbf { Q } _ { p } ^ { \operatorname { u n r } } / \mathbf { Q } _ { p } )$. Consider the exact sequence of${ \mathcal { O } } [ { \mathcal { G } } ] .$ modules

$$
0 \to (V _ {\lambda^ {n}} ^ {1} / W _ {\lambda^ {n}} ^ {0}) ^ {\mathcal {H}} \to (V _ {\lambda^ {n}} / W _ {\lambda^ {n}} ^ {0}) ^ {\mathcal {H}} \to X \to 0
$$

where X is a submodule of$( V _ { \lambda ^ { n } } / V _ { \lambda ^ { n } } ^ { 1 } ) ^ { \mathcal { H } }$. Since the action of on$p$$V _ { \lambda ^ { n } } / V _ { \lambda ^ { n } } ^ { 1 }$is via a character which is nontrivial mod λ (it equals$\chi _ { 2 } \chi _ { 1 } ^ { - 1 }$mod λ and$\chi _ { 1 } \not \equiv \chi _ { 2 } )$, we see that$X ^ { \mathcal { G } } = 0$and$H ^ { 1 } ( { \mathcal { G } } , X ) = 0$. Then we have an exact diagram of O-modules

$$
\begin{array}{c} \Bigg \downarrow \\ H ^ {1} (\mathcal {G}, (V _ {\lambda^ {n}} ^ {1} / W _ {\lambda^ {n}} ^ {0}) ^ {\mathcal {H}}) \simeq H ^ {1} (\mathcal {G}, (V _ {\lambda^ {n}} / W _ {\lambda^ {n}} ^ {0}) ^ {\mathcal {H}}) \\ \Bigg \downarrow \\ H ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}} / W _ {\lambda^ {n}} ^ {0}) \\ \Bigg \downarrow \\ H ^ {1} (\mathbf {Q} _ {p} ^ {\mathrm{unr}}, V _ {\lambda^ {n}} / W _ {\lambda^ {n}} ^ {0}) ^ {\mathcal {G}}. \end{array}
$$

By hypothesis the image of$\alpha$is zero in$H ^ { 1 } ( \mathbf { Q } _ { p } ^ { \mathrm { u n r } } , V _ { \lambda ^ { n } } / W _ { \lambda ^ { n } } ^ { 0 } ) ^ { \mathcal { G } }$. Hence it is in the image of$H ^ { 1 } ( \mathcal { G } , ( V _ { \lambda ^ { n } } ^ { 1 } / W _ { \lambda ^ { n } } ^ { 0 } ) ^ { \mathcal { H } } )$. Thus we can assume that it is represented in$H ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } / W _ { \lambda ^ { n } } ^ { \dot { 0 } } )$by a cocycle, which maps$\mathcal { G }$to$V _ { \lambda ^ { n } } ^ { 1 } / W _ { \lambda ^ { n } } ^ { 0 } ; \mathrm { i . e . }$ $f ( D _ { p } ) \subset V _ { \lambda ^ { n } } ^ { 1 } / W _ { \lambda ^ { n } } ^ { 0 ^ { \cdot } } , f ( I _ { p } ) = 0$. The diference between$f$and the image of α is a coboundary$\{ \sigma \mapsto \sigma \bar { \mu } - \bar { \mu } \}$for some$u \in V _ { \lambda ^ { n } }$. By subtracting the coboundary $\{ \sigma \mapsto \sigma u - u \}$from α globally we get a new α such that$\alpha = f$as cocycles mapping$\mathcal { G }$to$V _ { \lambda ^ { n } } ^ { 1 } / W _ { \lambda ^ { n } } ^ { 0 }$. Thus$\alpha ( D _ { p } ) \subset V _ { \lambda ^ { n } } ^ { 1 } , \alpha ( I _ { p } ) \subset W _ { \lambda ^ { \prime } } ^ { 0 }$and it is now easy to check that$[ \rho _ { \alpha } ]$is a Selmer deformation of$\rho _ { 0 }$.

Since$[ \rho _ { \alpha } ]$is a Selmer deformation there is a unique map of local$\mathcal { O } _ { - }$ algebras$\varphi _ { \alpha } : R _ { \mathcal { D } } \ \to \ \mathcal { O } _ { n } [ \varepsilon ]$inducing it. (If$\mathcal { M } \neq \phi$we must check the other conditions also.) Since$\rho _ { \alpha } \equiv \rho _ { f , \lambda }$mod ε we see that restricting$\varphi _ { \alpha }$to p<sub>D</sub> gives a homomorphism of O-modules,

$$
\varphi_ {\alpha}: \mathfrak {p} _ {\mathcal {D}} \to \varepsilon . \mathcal {O} / \lambda^ {n}
$$

such that$\varphi _ { \alpha } ( { \mathfrak { p } } _ { \mathcal { D } } ^ { 2 } ) = 0$. Thus we have defined a map$\varphi : \alpha  \varphi _ { \alpha }$2

$$
\varphi : H _ {\mathrm{Se}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V _ {\lambda^ {n}}) \to \operatorname{Hom} _ {\mathcal {O}} \left(\mathfrak {p} _ {\mathcal {D}} / \mathfrak {p} _ {\mathcal {D}} ^ {2}, \mathcal {O} / \lambda^ {n}\right).
$$

It is straightforward to check that this is a map of O-modules. To check the injectivity of$\varphi$suppose that$\varphi _ { \alpha } ( { \mathfrak { p } } _ { \mathcal { D } } ) = 0$. Then$\varphi _ { \alpha }$factors through$R _ { \mathcal { D } } / { \mathfrak { p } } _ { \mathcal { D } } \simeq \mathcal { O }$ and being an O-algebra homomorphism this determines$\varphi _ { \alpha }$. Thus$\left[ \rho _ { f , \lambda } \right] = \left[ \rho _ { \alpha } \right]$ If$A ^ { - 1 } \rho _ { \alpha } A = \rho _ { f , \lambda }$then A mod$\varepsilon$is seen to be central by Schur’s lemma and so may be taken to be I. A simple calculation now shows that α is a coboundary.

To see that$\varphi$is surjective choose

$$
\Psi \in \mathrm{Hom} _ {\mathcal {O}} (\mathfrak {p} _ {\mathcal {D}} / \mathfrak {p} _ {\mathcal {D}} ^ {2}, \mathcal {O} / \lambda^ {n}).
$$

Then$\rho _ { \Psi } : { \mathrm { G a l } } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } ) \to { \mathrm { G L } } _ { 2 } ( R _ { \mathcal { D } } / ( \mathfrak { p } _ { \mathcal { D } } ^ { 2 } , \ker \Psi ) )$is induced by a representative of the universal deformation (chosen to equal$\rho _ { f , \lambda }$when reduced mod$\rho _ { \mathcal { D } } )$and we define a map α<sub>Ψ</sub>$: \mathrm { G a l } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } ) \longrightarrow V _ { \lambda ^ { \prime } }$n by

$$
\alpha_ {\Psi} (g) = \rho_ {\Psi} (g) \rho_ {f, \lambda} (g) ^ {- 1} \in \left\{ \begin{array}{c c} 1 + \mathfrak {p} _ {\mathcal {D}} / (\mathfrak {p} _ {\mathcal {D}} ^ {2}, \ker \Psi) & \mathfrak {p} _ {\mathcal {D}} / (\mathfrak {p} _ {\mathcal {D}} ^ {2}, \ker \Psi) \\ \mathfrak {p} _ {\mathcal {D}} / (\mathfrak {p} _ {\mathcal {D}} ^ {2}, \ker \Psi) & 1 + \mathfrak {p} _ {\mathcal {D}} / (\mathfrak {p} _ {\mathcal {D}} ^ {2}, \ker \Psi) \end{array} \right\} \subseteq V _ {\lambda^ {n}}
$$

where$\rho _ { f , \lambda } ( g )$is viewed in$\mathrm { G L } _ { 2 } ( R _ { \mathcal { D } } / ( \mathfrak { p } _ { \mathcal { D } } ^ { 2 } , \ker \Psi ) )$via the structural map$\mathcal { O }$ $R _ { \mathcal { D } } ~ \left( R _ { \mathcal { D } } \right.$being an O-algebra and the structural map being local because of the existence of a section). The right-hand inclusion comes from

$$
\mathfrak {p} _ {D} / (\mathfrak {p} _ {D} ^ {2}, \ker \Psi) \stackrel {{\Psi}} {{\hookrightarrow}} \begin{array}{c c c} \mathcal {O} / \lambda^ {n} & \stackrel {{\sim}} {{\to}} & (\mathcal {O} / \lambda^ {n}) \cdot \varepsilon \\ 1 & \mapsto & \varepsilon . \end{array}
$$

Then$\alpha _ { \Psi }$is really seen to be a continuous cocycle whose cohomology class lies in$H _ { \mathrm { S e } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V _ { \lambda ^ { n } } )$. Finally$\varphi ( \alpha _ { \Psi } ) = \Psi$. Moreover, the constructions are compatible with change of n, i.e., for$V _ { \lambda ^ { n } } \hookrightarrow V _ { \lambda ^ { n + 1 } }$and$\lambda { : } \mathcal { O } / \lambda ^ { n } \hookrightarrow \mathcal { O } / \lambda ^ { n + 1 }$. 

We now relate the local cohomology groups we have defined to the theory of Fontaine and in particular to the groups of Bloch-Kato [BK]. We will distinguish these by writing$H _ { F } ^ { 1 }$for the cohomology groups of Bloch-Kato. None of the results described in the rest of this section are used in the rest of the paper. They serve only to relate the Selmer groups we have defined (and later compute) to the more standard versions. Using the lattice associated to$\rho _ { f , \lambda }$we obtain also a lattice$T \simeq \mathcal { O } ^ { 4 }$with Galois action via Ad$\rho _ { f , \lambda }$. Let$\gamma = T \otimes _ { \mathbf { Z } _ { p } } \mathbf { Q } _ { p }$ be associated vector space and identify V with$\nu / T$. Let$\operatorname { p r } : \mathcal { V } \to \dot { V }$be the natural projection and define cohomology modules by

$$
\begin{array}{c} H _ {F} ^ {1} (\mathbf {Q} _ {p}, \mathcal {V}) = \ker : H ^ {1} (\mathbf {Q} _ {p}, \mathcal {V}) \to H ^ {1} (\mathbf {Q} _ {p}, \mathcal {V} \underset {\mathbf {Q} _ {p}} {\otimes} B _ {\text {crys}}), \\ H _ {F} ^ {1} (\mathbf {Q} _ {p}, V) = \operatorname * {p r} \Big (H _ {F} ^ {1} (\mathbf {Q} _ {p}, \mathcal {V}) \Big) \subset H ^ {1} (\mathbf {Q} _ {p}, V), \\ H _ {F} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}) = (j _ {n}) ^ {- 1} \Big (H _ {F} ^ {1} (\mathbf {Q} _ {p}, V) \Big) \subset H ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}), \end{array}
$$

where$j _ { n } : V _ { \lambda ^ { n } } \to V$is the natural map and the two groups in the definition of$H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , \mathcal { V } )$are defined using continuous cochains. Similar definitions apply to$\begin{array} { r } { \mathcal { V } ^ { \bar { * } } \stackrel { } { = } \mathrm { H o m } _ { \mathbf { Q } _ { p } } ( \mathcal { V } , \mathbf { Q } _ { p } ( 1 ) ) } \end{array}$and indeed to any finite-dimensional continuous p-adic representation space. The reader is cautioned that the definition of $H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } )$is dependent on the lattice$T$(or equivalently on$V )$. Under certainly conditions Bloch and Kato show, using the theory of Fontaine and Lafaille, that this is independent of the lattice (see [BK, Lemmas 4.4 and 4.5]). In any case we will consider in what follows a fixed lattice associated to $\rho = \rho _ { f , \lambda } , \mathrm { A d } \rho ,$etc. Henceforth we will only use the notation$H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , - )$when the underlying vector space is crystalline.

Proposition 1.3. (i) If$\rho _ { 0 }$is flat but ordinary and$\rho _ { f , \lambda }$is associated to a p-divisible group then for all n

$$
H _ {\mathrm{f}} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}) = H _ {F} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}).
$$

(ii)${ \cal I } f \rho _ { f , \lambda }$is ordinary, det$\rho _ { f , \lambda } \Big \vert _ { I _ { p } } = \varepsilon \ a n d \rho _ { f , \lambda }$is associated to a p-divisible group, then for all$n _ { \colon }$,

$$
H _ {F} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}) \subseteq H _ {\mathrm{Se}} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}.
$$

Proof. Beginning with (i), we define$H _ { \mathrm { f } } ^ { 1 } ( \mathbf { Q } _ { p } , { \mathcal V } ) \ : = \ : \{ \alpha \in H ^ { 1 } ( \mathbf { Q } _ { p } , { \mathcal V } )$ $\kappa ( \alpha / \lambda ^ { n } ) \in H _ { \mathrm { f } } ^ { 1 } ( \mathbf { Q } _ { p } , V )$for all n} where κ :$H ^ { 1 } ( \mathbf { Q } _ { p } , \mathcal { V } ) \to H ^ { 1 } ( \mathbf { Q } _ { p } , { \cal V } )$. Then we see that in case (i),$H _ { \mathrm { f } } ^ { 1 } ( \mathbf { Q } _ { p } , V )$is divisible. So it is enough to how that

$$
H _ {F} ^ {1} (\mathbf {Q} _ {p}, \mathcal {V}) = H _ {\mathrm{f}} ^ {1} (\mathbf {Q} _ {p}, \mathcal {V}).
$$

We have to compare two constructions associated to a nonzero element α of $H ^ { 1 } ( \mathbf { Q } _ { p } , \mathcal { V } )$. The first is to associate an extension

$$
0 \to \mathcal {V} \to E \xrightarrow {\delta} K \to 0\tag{1.9}
$$

of K-vector spaces with commuting continuous Galois action. If we fix an e with$\delta ( e ) = 1$the action on e is defined by$\sigma e \mathrm { ~ = ~ } e + \hat { \alpha } ( \sigma )$with ˆα a cocycle representing α. The second construction begins with the image of the subspace $\langle \alpha \rangle$in$H ^ { 1 } ( \mathbf { Q } _ { p } , V )$. By the analogue of Proposition 1.2 in the local case, there is an O-module isomorphism

$$
H ^ {1} (\mathbf {Q} _ {p}, V) \simeq \operatorname{Hom} _ {\mathcal {O}} \left(\mathfrak {p} _ {R} / \mathfrak {p} _ {R} ^ {2}, K / \mathcal {O}\right)
$$

where R is the universal deformation ring of$\rho _ { 0 }$viewed as a representation of$\operatorname { G a l } ( { \bar { \mathbf { Q } } } _ { p } / \mathbf { Q } )$on O-algebras and${ \mathfrak { p } } _ { R }$is the ideal of$R$corresponding to${ \mathfrak { p } } _ { \mathcal { D } }$ $( \mathrm { i . e . }$, its inverse image in$R )$. Since$\alpha \neq 0$, associated to$\langle \alpha \rangle$is a quotient ${ \mathfrak { p } } _ { R } / ( { \mathfrak { p } } _ { R } ^ { 2 } , { \mathfrak { a } } )$of${ \mathfrak { p } } _ { R } / { \mathfrak { p } } _ { R } ^ { 2 }$which is a free O-module of rank one. We then obtain a homomorphism

$$
\rho_ {\alpha}: \operatorname{Gal} (\bar {\mathbf {Q}} _ {p} / \mathbf {Q} _ {p}) \to \operatorname{GL} _ {2} \left(R / \left(\mathfrak {p} _ {R} ^ {2}, \mathfrak {a}\right)\right)
$$

induced from the universal deformation (we pick a representation in the universal class). This is associated to an O-module of rank 4 which tensored with K gives a K-vector space$E ^ { \prime } \simeq ( K ) ^ { 4 }$which is an extension

$$
0 \to \mathcal {U} \to E ^ {\prime} \to \mathcal {U} \to 0\tag{1.10}
$$

where$\mathcal { U } \simeq K ^ { 2 }$has the Galis representation$\rho _ { f , \lambda }$(viewed locally).

In the first construction$\alpha \in H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , \mathcal { V } )$if and only if the extension (1.9) is crystalline, as the extension given in (1.9) is a sum of copies of the more usual extension where$\mathbf { Q } _ { p }$replaces K in (1.9). On the other hand$\langle \alpha \rangle \subseteq H _ { \mathrm { f } } ^ { 1 } ( \mathbf { Q } _ { p } , \mathcal { V } )$if and only if the second construction can be made through$R ^ { \mathrm { { f } } }$, or equivalently if and only if$E ^ { \prime }$is the representation associated to a p-divisible group. A priori, the representation associated to$\rho _ { \alpha }$only has the property that on all finite quotients it comes from a finite flat group scheme. However a theorem of Raynaud$[ \mathrm { R a y 1 } ]$says that then$\rho _ { \alpha }$comes from a p-divisible group. For more details on$R ^ { \mathrm { { f } } }$, the universal flat deformation ring of the local representation $\rho _ { 0 }$, see [Ram].) Now the extension$E ^ { \prime }$comes from a p-divisible group if and only if it is crystalline; cf. [Fo, §6]. So we have to show that (1.9) is crystalline if and only if (1.10) is crystalline.

One obtains (1.10) from (1.9) as follows. We view V as$\mathrm { H o m } _ { K } ( \mathcal { U } , \mathcal { U } )$and let

$$
X = \ker : \left\{\operatorname{Hom} _ {K} (\mathcal {U}, \mathcal {U}) \otimes \mathcal {U} \rightarrow \mathcal {U} \right\}
$$

where the map is the natural one$f \otimes w \mapsto f ( w )$. (All tensor products in this proof will be as K-vector spaces.) Then as$K [ D _ { p } ]$]-modules

$$
E ^ {\prime} \simeq (E \otimes \mathcal {U}) / X.
$$

To check this, one calculates explicitly with the definition of the action on$E$ (given above on$e )$and on$E ^ { \prime }$(given in the proof of Proposition 1.1). It follows from standard properties of crystalline representations that if E is crystalline, so is$E \otimes { \mathcal { U } }$and also$E ^ { \prime }$. Conversely, we can recover$E$from$E ^ { \prime }$as follows. Consider$E ^ { \prime } \otimes \mathcal { U } \simeq ( E \otimes \mathcal { U } \otimes \mathcal { U } ) / ( X \otimes \mathcal { U } )$. Then there is a natural map $\varphi : E \otimes ( \mathrm { d e t } )  E ^ { \prime } \otimes \mathcal { U }$induced by the direct sum decomposition$\mathcal { U } \otimes \mathcal { U } \simeq$ $\mathrm { ( d e t ) } \oplus \mathrm { S y m ^ { 2 } } \mathcal { U } .$. Here det denotes a 1-dimensional vector space over K with Galois action via det$\rho _ { f , \lambda }$. Now we claim that$\varphi$is injective on$\nu \otimes ( \mathrm { d e t } )$. For if$f \in \mathcal V$then$\varphi ( f ) = f \otimes ( w _ { 1 } \otimes w _ { 2 } - w _ { 2 } \otimes w _ { 1 } )$where$w _ { 1 } , w _ { 2 }$are a basis for$\mathcal { U }$ for which$w _ { 1 } \wedge w _ { 2 } = 1$in det$\simeq K$. So if$\varphi ( f ) \in X \otimes \mathcal { U }$then

$$
f (w _ {1}) \otimes w _ {2} - f (w _ {2}) \otimes w _ {1} = 0 \text {   in   } \mathcal {U} \otimes \mathcal {U}.
$$

But this is false unless$f ( w _ { 1 } ) = f ( w _ { 2 } ) = 0$whence$f = 0$. So$\varphi$is injective on$\nu \otimes$det and if$\varphi$itself were not injective then E would split contradicting $\alpha \neq 0$. So$\varphi$is injective and we have exhibited$E \otimes ( \mathrm { d e t } )$as a subrepresentation of$E ^ { \prime } \otimes \mathcal { U }$which is crystalline. We deduce that E is crystalline if$E ^ { \prime }$is. This completes the proof of (i).

To prove (ii) we check first that$H _ { \mathrm { S e } } ^ { 1 } ( { \bf Q } _ { p } , V _ { \lambda ^ { n } } ) = j _ { n } ^ { - 1 } \Big ( H _ { \mathrm { S e } } ^ { 1 } ( { \bf Q } _ { p } , V ) \Big )$(this was already used in (1.7)). We next have to show that$H _ { F } ^ { 1 } ( \dot { \mathbf { Q } } _ { p } , \mathcal { V } ) \subseteq H _ { \mathrm { S e } } ^ { 1 } ( \mathbf { Q } _ { p } , \mathcal { V } )$ where the latter is defined by

$$
H _ {\mathrm{Se}} ^ {1} (\mathbf {Q} _ {p}, \mathcal {V}) = \ker : H ^ {1} (\mathbf {Q} _ {p}, \mathcal {V}) \to H ^ {1} (\mathbf {Q} _ {p} ^ {\mathrm{unr}}, \mathcal {V} / \mathcal {V} ^ {0})
$$

with$\mathcal { V } ^ { 0 }$the subspace of$\nu$on which$I _ { p }$acts via$\varepsilon .$. But this follows from the computations in Corollary 3.8.4 of [BK]. Finally we observe that

$$
\operatorname{pr} \left(H _ {\mathrm{Se}} ^ {1} (\mathbf {Q} _ {p}, \mathcal {V})\right) \subseteq H _ {\mathrm{Se}} ^ {1} (\mathbf {Q} _ {p}, V)
$$

although the inclusion may be strict, and

$$
\operatorname{pr} \Big (H _ {F} ^ {1} (\mathbf {Q} _ {p}, \mathcal {V}) \Big) = H _ {F} ^ {1} (\mathbf {Q} _ {p}, V)
$$

by definition. This completes the proof.

These groups have the property that for$s \geq r _ { \ast }$

$$
H ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda} ^ {r}) \cap j _ {r, s} ^ {- 1} \Big (H _ {F} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {s}}) \Big) = H _ {F} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {r}})\tag{1.11}
$$

where$j _ { r , s } : V _ { \lambda ^ { r } } \to V _ { \lambda ^ { s } }$is the natural injection. The same holds for$V _ { \lambda ^ { r } } ^ { * }$and $V _ { \lambda ^ { s } } ^ { * }$in place of$V _ { \lambda ^ { r } }$and$V _ { \lambda } .$s where$V _ { \lambda ^ { r } } ^ { * }$is defined by

$$
V _ {\lambda^ {r}} ^ {*} = \mathrm{Hom} (V _ {\lambda^ {r}}, \pmb {\mu} _ {p ^ {r}})
$$

and similarly for$V _ { \lambda ^ { s } } ^ { * }$. Both results are immediate from the definition (and indeed were part of the motivation for the definition).

We also give a finite level version of a result of Bloch-Kato which is easily deduced from the vector space version. As before let$T \subset \mathcal { V }$be a Galois stable lattice so that$T \simeq \mathcal { O } ^ { 4 }$. Define

$$
H _ {F} ^ {1} (\mathbf {Q} _ {p}, T) = i ^ {- 1} \left(H _ {F} ^ {1} (\mathbf {Q} _ {p}, \mathcal {V})\right)
$$

under the natural inclusion$i : T \hookrightarrow \mathcal { V } .$and likewise for the dual lattice$T ^ { * } =$ Hom$\mathsf { \iota } _ { \mathbf { Z } _ { p } } ( V , ( \mathbf { Q } _ { p } / \mathbf { Z } _ { p } ) ( 1 ) )$in$\nu ^ { * }$. (Here$\mathcal { V } ^ { * } = \mathrm { H o m } ( \mathcal { V } , \mathbf { Q } _ { p } ( 1 ) )$; throughout this paper we use$M ^ { * }$to denote a dual of M with a Cartier twist.) Also write $\mathrm { p r } _ { n } \ : \ T \ \to \ T / \lambda ^ { n }$for the natural projection map, and for the mapping it induces on cohomology.

Proposition 1.4. If$\rho _ { f , \lambda }$is associated to a p-divisible group (the ordinary case is allowed) then

$$
\text {(i)} \operatorname * {p r} _ {n} \left(H _ {F} ^ {1} (\mathbf {Q} _ {p}, T)\right) = H _ {F} ^ {1} (\mathbf {Q} _ {p}, T / \lambda^ {n}) \text {   and   similarly   for   } T ^ {*}, T ^ {*} / \lambda^ {n}.
$$

(ii)$H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } )$is the orthogonal complement of$H _ { F } ^ { 1 } ( { \bf Q } _ { p } , V _ { \lambda ^ { n } } ^ { * } )$under Tate local duality between$H ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } )$and$H ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } ^ { * } \bar { ) }$and similarly for$W _ { \lambda ^ { n } }$ and$W _ { \lambda ^ { n } } ^ { * }$replacing$V _ { \lambda ^ { \prime } }$n and$V _ { \lambda ^ { n } } ^ { * }$

More generally these results hold for any crystalline representation$\mathcal { V } ^ { \prime }$in place of V and$\lambda ^ { \prime }$a uniformizer in$K ^ { \prime }$where$K ^ { \prime }$is any finite extension of$\mathbf { Q } _ { p }$ with$K ^ { \prime } \subset \operatorname { E n d } _ { \operatorname { G a l } ( { \overline { { \mathbf { Q } } } } _ { p } / \mathbf { Q } _ { p } ) } \mathcal { V } ^ { \prime }$

Proof. We first observe that$\mathrm { p r } _ { n } ( H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , T ) ) \subset H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , T / \lambda ^ { n } )$. Now from the construction we may identify$T / \lambda ^ { n }$with$V _ { \lambda ^ { n } \cdot \mathrm { ~ A ~ } }$result of Bloch-Kato ([BK, Prop. 3.8]) says that$H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , \mathcal { V } )$and$H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , \mathcal { V } ^ { * } )$are orthogonal complements under Tate local duality. It follows formally that$H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } ^ { * } )$ and$\mathrm { p r } _ { n } \big ( H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , T ) \big )$are orthogonal complements, so to prove the proposition it is enough to show that

$$
\# H _ {F} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}} ^ {*}) \# H _ {F} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}) = \# H ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}).\tag{1.12}
$$

Now if$r = \dim _ { K } H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , \boldsymbol { \nu } )$and$s = \dim _ { K } H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , \mathcal { V } ^ { * } )$then

$$
r + s = \dim_ {K} H ^ {0} (\mathbf {Q} _ {p}, \mathcal {V}) + \dim_ {K} H ^ {0} (\mathbf {Q} _ {p}, \mathcal {V} ^ {*}) + \dim_ {K} \mathcal {V}.\tag{1.13}
$$

From the definition,

$$
\# H _ {F} ^ {1} \left(\mathbf {Q} _ {p}, V _ {\lambda^ {n}}\right) = \# \left(\mathcal {O} / \lambda^ {n}\right) ^ {r} \cdot \# \ker \left\{H ^ {1} \left(\mathbf {Q} _ {p}, V _ {\lambda^ {n}}\right)\rightarrow H ^ {1} \left(\mathbf {Q} _ {p}, V\right)\right\}.\tag{1.14}
$$

The second factor is equal to$\# \{ V ( \mathbf { Q } _ { p } ) / \lambda ^ { n } V ( \mathbf { Q } _ { p } ) \}$. When we write$V ( \mathbf { Q } _ { p } ) ^ { \mathrm { d i v } }$ for the maximal divisible subgroup of$V ( \mathbf { Q } _ { p } )$this is the same as

$$
\begin{array}{c} \# (V (\mathbf {Q} _ {p}) / V (\mathbf {Q} _ {p}) ^ {\mathrm{div}}) / \lambda^ {n} = \# (V (\mathbf {Q} _ {p}) / V (\mathbf {Q} _ {p}) ^ {\mathrm{div}}) _ {\lambda^ {n}} \\ = \# V (\mathbf {Q} _ {p}) _ {\lambda^ {n}} / \# (V (\mathbf {Q} _ {p}) ^ {\mathrm{div}}) _ {\lambda^ {n}}. \end{array}
$$

Combining this with (1.14) gives

$$
\begin{array}{c} \# H _ {F} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}) = \# (\mathcal {O} / \lambda^ {n}) ^ {r} \\ \cdot \# H ^ {0} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}) / \# (\mathcal {O} / \lambda^ {n}) ^ {\dim_ {K} H ^ {0} (\mathbf {Q} _ {p}, \mathcal {V})}. \end{array}\tag{1.15}
$$

This, together with an analogous formula for #$H _ { F } ^ { 1 } ( { \bf Q } _ { p } , V _ { \lambda ^ { n } } ^ { * } )$and (1.13), gives $\# H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , V ^ { \lambda ^ { n } } ) \# H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } ^ { * } ) \ = \ \# ( \mathcal { O } / \lambda ^ { n } ) ^ { 4 } \cdot \# H ^ { 0 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } ) \# H ^ { 0 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } ^ { * } ) .$

As$\# H ^ { 0 } ( \mathbf { Q } _ { p } , V ^ { * } \lambda ^ { n } ) = \# H ^ { 2 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } )$the assertion of (1.12) now follows from the formula for the Euler characteristic of$V _ { \lambda ^ { n } }$

The proof for$W _ { \lambda ^ { n } }$, or indeed more generally for any crystalline representation, is the same.

We also give a characterization of the orthogonal complements of $H _ { \mathrm { S e } } ^ { 1 } ( \mathbf { Q } _ { p } , W _ { \lambda ^ { n } } )$and$H _ { \mathrm { S e } } ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } )$, under Tate’s local duality. We write these duals as$H _ { \mathrm { S e ^ { * } } } ^ { 1 } ( \mathbf { Q } _ { p } , W _ { \lambda ^ { n } } ^ { * } )$and$H _ { \mathrm { S e ^ { * } } } ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } ^ { * } )$respectively. Let

$$
\varphi_ {w}: H ^ {1} \left(\mathbf {Q} _ {p}, W _ {\lambda^ {n}} ^ {*}\right)\rightarrow \left(\mathbf {Q} _ {p}, W _ {\lambda^ {n}} ^ {*} / \left(W _ {\lambda^ {n}} ^ {*}\right) ^ {0}\right)
$$

be the natural map where$( W _ { \lambda ^ { n } } ^ { * } ) ^ { i }$is the orthogonal complement of$W _ { \lambda ^ { n } } ^ { 1 - i }$in $W _ { \lambda ^ { n } } ^ { * }$, and let$X _ { n , i }$be defined as the image under the composite map

$$
\begin{array}{r l} X _ {n, i} = \mathrm{im}: \mathbf {Z} _ {p} ^ {\times} / (\mathbf {Z} _ {p} ^ {\times}) ^ {p ^ {n}} \otimes \mathcal {O} / \lambda^ {n} & \to H ^ {1} (\mathbf {Q} _ {p}, \boldsymbol {\mu} _ {p ^ {n}} \otimes \mathcal {O} / \lambda^ {n}) \\ & \to H ^ {1} (\mathbf {Q} _ {p}, W _ {\lambda^ {n}} ^ {*} / (W _ {\lambda^ {n}} ^ {*}) ^ {0}) \end{array}
$$

where in the middle term$\mu _ { p ^ { n } } \otimes \mathcal { O } / \lambda ^ { n }$is to be identified with$( W _ { \lambda ^ { n } } ^ { * } ) ^ { 1 } / ( W _ { \lambda ^ { n } } ^ { * } ) ^ { 0 }$ Similarly if we replace$W _ { \lambda ^ { n } } ^ { * }$by$V _ { \lambda ^ { r } } ^ { * }$we let$Y _ { n , i }$be the image of$\mathbf { Z } _ { p } ^ { \times } / ( \mathbf { Z } _ { p } ^ { \times } ) ^ { p ^ { n } } \otimes$ $( \mathcal { O } / \lambda ^ { n } ) ^ { 2 }$in$H ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } ^ { * } / ( W _ { \lambda ^ { n } } ^ { * } ) ^ { 0 } )$, and we replace$\varphi _ { w }$by the analogous map$\varphi _ { v } .$

Proposition 1.5.

$$
\begin{array}{r} H _ {\mathrm{Se} ^ {*}} ^ {1} (\mathbf {Q} _ {p}, W _ {\lambda^ {n}} ^ {*}) = \varphi_ {w} ^ {- 1} (X _ {n, i}), \\ H _ {\mathrm{Se} ^ {*}} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}} ^ {*}) = \varphi_ {v} ^ {- 1} (Y _ {n, i}). \end{array}
$$

Proof. This can be checked by dualizing the sequence

$$
\begin{array}{r l} & 0 \to H _ {\mathrm{Str}} ^ {1} (\mathbf {Q} _ {p}, W _ {\lambda^ {n}}) \to H _ {\mathrm{Se}} ^ {1} (\mathbf {Q} _ {p}, W _ {\lambda^ {n}}) \\ & \qquad \to \ker : \{H ^ {1} (\mathbf {Q} _ {p}, W _ {\lambda^ {n}} / (W _ {\lambda^ {n}}) ^ {0}) \to H ^ {1} (\mathbf {Q} _ {p} ^ {\mathrm{unr}}, W _ {\lambda^ {n}} / (W _ {\lambda^ {n}}) ^ {0} \}, \end{array}
$$

where$H _ { \mathrm { s t r } } ^ { 1 } ( \mathbf { Q } _ { p } , W _ { \lambda ^ { n } } ) = \ker : H ^ { 1 } ( \mathbf { Q } _ { p } , W _ { \lambda ^ { n } } ) \longrightarrow H ^ { 1 } ( \mathbf { Q } _ { p } , W _ { \lambda ^ { n } } / ( W _ { \lambda ^ { n } } ) ^ { 0 } )$. The first term is orthogonal to ker :$H ^ { 1 } ( { \bf Q } _ { p } , W _ { \lambda ^ { n } } ^ { * } )  H ^ { 1 } ( { \bf Q } _ { p } , W _ { \lambda ^ { n } } ^ { * } / ( W _ { \lambda ^ { n } } ^ { * } ) ^ { 1 } )$. By the naturality of the cup product pairing with respect to quotients and subgroups the claim then reduces to the well known fact that under the cup product pairing

$$
H ^ {1} (\mathbf {Q} _ {p}, \pmb {\mu} _ {p ^ {n}}) \times H ^ {1} (\mathbf {Q} _ {p}, \mathbf {Z} / p ^ {n}) \to \mathbf {Z} / p ^ {n}
$$

the orthogonal complement of the unramified homomorphisms is the image of the units${ \bf Z } _ { p } ^ { \times } / ( { \bf Z } _ { p } ^ { \times } ) ^ { p ^ { n } }  H ^ { 1 } ( { \bf Q } _ { p } , \mu _ { p ^ { n } } )$. The proof for$V _ { \lambda ^ { \prime } }$n is essentially the same.

## 2. Some computations of cohomology groups

We now make some comparisons of orders of cohomology groups using the theorems of Poitou and Tate. We retain the notation and conventions of Section 1 though it will be convenient to state the first two propositions in a more general context. Suppose that

$$
L = \prod L _ {q} \subseteq \prod_ {p \in \Sigma} H ^ {1} (\mathbf {Q} _ {q}, X)
$$

is a subgroup, where$X$is a finite module for$\operatorname { G a l } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } )$of p-power order. We define$L ^ { * }$to be the orthogonal complement of$L$under the perfect pairing (local Tate duality)

$$
\prod_ {q \in \Sigma} H ^ {1} (\mathbf {Q} _ {q}, X) \times \prod_ {q \in \Sigma} H ^ {1} (\mathbf {Q} _ {q}, X ^ {*}) \to \mathbf {Q} _ {p} / \mathbf {Z} _ {p}
$$

where$X ^ { \ast } = \operatorname { H o m } ( X , \mu _ { p ^ { \infty } } )$. Let

$$
\lambda_ {X}: H ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, X) \to \prod_ {q \in \Sigma} H ^ {1} (\mathbf {Q} _ {q}, X)
$$

be the localization map and similarly$\lambda _ { X } \cdot$∗ for$X ^ { * }$. Then we set

$$
H _ {L} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, X) = \lambda_ {X} ^ {- 1} (L), H _ {L ^ {*}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, X ^ {*}) = \lambda_ {X ^ {*}} ^ {- 1} (L ^ {*}).
$$

The following result was suggested by a result of Greenberg (cf. [Gre1]) and is$\mathrm { a }$simple consequence of the theorems of Poitou and Tate. Recall that$p$is always assumed odd and that$p \in \Sigma$

Proposition 1.6.

$$
\# H _ {L} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, X) / \# H _ {L ^ {*}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, X ^ {*}) = h _ {\infty} \prod_ {q \in \Sigma} h _ {q}
$$

where

$$
\left\{ \begin{array}{l l} h _ {q} & = \# H ^ {0} (\mathbf {Q} _ {q}, X ^ {*}) / [ H ^ {1} (\mathbf {Q} _ {q}, X): L _ {q} ] \\ h _ {\infty} & = \# H ^ {0} (\mathbf {R}, X ^ {*}) \# H ^ {0} (\mathbf {Q}, X) / \# H ^ {0} (\mathbf {Q}, X ^ {*}). \end{array} \right.
$$

Proof.AdaptingtheexactsequenceproofofPoitouandTate(cf.[Mi2,Th.4.20]) we get a seven term exact sequence

$$
\begin{array}{c c c c c c} 0 & \longrightarrow & H _ {L} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, X) & \longrightarrow & H ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, X) & \longrightarrow & \prod_ {q \in \Sigma} H ^ {1} (\mathbf {Q} _ {q}, X) / L _ {q} \\ & & & & & \Big \downarrow \\ & & \prod_ {q \in \Sigma} H ^ {2} (\mathbf {Q} _ {q}, X) & \longleftarrow & H ^ {2} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, X) & \longleftarrow & H _ {L ^ {*}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, X ^ {*}) ^ {\wedge} \\ & & \Big \downarrow H ^ {0} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, X ^ {*}) ^ {\wedge} \longrightarrow 0, \end{array}
$$

where$M ^ { \wedge } = \operatorname { H o m } ( M , \mathbf { Q } _ { p } / \mathbf { Z } _ { p } )$. Now using local duality and global Euler characteristics (cf. [Mi2, Cor. 2.3 and Th. 5.1]) we easily obtain the formula in the proposition. We repeat that in the above proposition X can be arbitrary of p-power order.

We wish to apply the proposition to investigate$H _ { \mathcal { D } } ^ { 1 }$. Let$\mathcal { D } = ( \cdot , \Sigma , \mathcal { O } , \mathcal { M } )$ be a standard deformation theory as in Section 1 and define a corresponding group$L _ { n } = L _ { \mathcal { D } , n }$by setting

$$
L _ {n, q} = \left\{ \begin{array}{l l} H ^ {1} (\mathbf {Q} _ {q}, V _ {\lambda^ {n}}) & \text { for } q \neq p \text { and } q \not \in \mathcal {M} \\ H _ {D _ {q}} ^ {1} (\mathbf {Q} _ {q}, V _ {\lambda^ {n}}) & \text { for } q \neq p \text { and } q \in \mathcal {M} \\ H. ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}) & \text { for } q = p. \end{array} \right.
$$

Then$H _ { \mathcal { D } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V _ { \lambda ^ { n } } ) = H _ { L ^ { n } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V _ { \lambda ^ { n } } )$and we also define

$$
H _ {\mathcal {D} ^ {*}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V _ {\lambda^ {n}} ^ {*}) = H _ {L _ {n} ^ {*}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V _ {\lambda^ {n}} ^ {*}).
$$

We will adopt the convention implicit in the above that if we consider$\Sigma ^ { \prime } \supset \Sigma$ then$H _ { \mathcal { D } } ^ { 1 } ( \mathbf { Q } _ { \Sigma ^ { \prime } } / \mathbf { Q } , V _ { \lambda ^ { n } } )$places no local restriction on the cohomology classes at primes$q \in \Sigma ^ { \prime } - \Sigma$. Thus in$H _ { \mathcal { D } ^ { \ast } } ^ { 1 } ( \mathbf { Q } _ { \Sigma ^ { \prime } } / \mathbf { Q } , V _ { \lambda ^ { n } } ^ { \ast } )$we will require (by duality) that the cohomology class be locally trivial at$q \in \Sigma ^ { \prime } - \Sigma$

We need now some estimates for the local cohomology groups. First we consider an arbitrary finite$\operatorname { G a l } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } )$-module X:

Proposition 1.7. If$q \not \in \Sigma$, and X is an arbitrary finite$\operatorname { G a l } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } )$ module of p-power order,

$$
\# H _ {L ^ {\prime}} ^ {1} \left(\mathbf {Q} _ {\Sigma \cup q} / \mathbf {Q}, X\right) / \# H _ {L} ^ {1} \left(\mathbf {Q} _ {\Sigma} / \mathbf {Q}, X\right) \leq \# H ^ {0} \left(\mathbf {Q} _ {q}, X ^ {*}\right)
$$

where$L _ { \ell } ^ { \prime } = L _ { \ell } \ f o r \ \ell \in \Sigma$and$L _ { q } ^ { \prime } = H ^ { \prime } ( \mathbf { Q } _ { q } , X )$

Proof. Consider the short exact sequence of inflation-restriction:

$$
\begin{array}{c} 0 \to H _ {L} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, X) \to H _ {L ^ {\prime}} ^ {1} (\mathbf {Q} _ {\Sigma \cup q} / \mathbf {Q}, X) \to \mathrm{Hom} (\mathrm{Gal} (\mathbf {Q} _ {\Sigma \cup q} / \mathbf {Q} _ {\Sigma}), X) ^ {\mathrm{Gal} (\mathbf {Q} _ {\Sigma} / \mathbf {Q})} \\ \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Bigg \downarrow \\ H ^ {1} (\mathbf {Q} _ {q} ^ {\mathrm{unr}}, X) ^ {\mathrm{Gal} (\mathbf {Q} _ {q} ^ {\mathrm{unr}} / \mathbf {Q} _ {q})} \xrightarrow {\sim} H ^ {1} (\mathbf {Q} _ {q} ^ {\mathrm{unr}}, X) ^ {\mathrm{Gal} (\mathbf {Q} _ {q} ^ {\mathrm{unr}} / \mathbf {Q} _ {q})} \end{array}
$$

The proposition follows when we note that

$$
\# H ^ {0} (\mathbf {Q} _ {q}, X ^ {*}) = \# H ^ {1} (\mathbf {Q} _ {q} ^ {\mathrm{unr}}, X) ^ {\operatorname{Gal} (\mathbf {Q} _ {q} ^ {\mathrm{unr}} / \mathbf {Q} _ {q})}.
$$

Now we return to the study of$V _ { \lambda ^ { n } }$and$W _ { \lambda ^ { n } }$

Proposition 1.8.$I f q \in \mathcal { M } \left( q \neq p \right)$and$X = V _ { \lambda ^ { n } }$then$h _ { q } = 1$

Proof. This is a straightforward calculation. For example if q is of type (A) then we have

$$
L _ {n, q} = \ker \left\{H ^ {1} \left(\mathbf {Q} _ {q}, V _ {\lambda^ {n}}\right)\rightarrow H ^ {1} \left(\mathbf {Q} _ {q}, W _ {\lambda^ {n}} / W _ {\lambda^ {n}} ^ {0}\right) \oplus H ^ {1} \left(\mathbf {Q} _ {q} ^ {\text { unr }}, \mathcal {O} / \lambda^ {n}\right)\right\}.
$$

Using the long exact sequence of cohomology associated to

$$
0 \to W _ {\lambda^ {n}} ^ {0} \to W _ {\lambda^ {n}} \to W _ {\lambda^ {n}} / W _ {\lambda^ {n}} ^ {0} \to 0
$$

one obtains a formula for the order of$L _ { n , q }$in terms of$\# H ^ { 1 } ( \mathbf { Q } _ { q } , W _ { \lambda ^ { n } } )$ #$H ^ { i } ( { \bf Q } _ { q } , W _ { \lambda ^ { n } } / W _ { \lambda ^ { n } } ^ { 0 } )$etc. Using local Euler characteristics these are easily reduced to ones involving$H ^ { 0 } ( \mathbf { Q } _ { q } , W _ { \lambda ^ { n } } ^ { * } )$etc. and the result follows easily.

The calculation of$h _ { p }$is more delicate. We content ourselves with an inequality in some cases.

Proposition 1.9. (i)$I f X = V _ { \lambda ^ { n } }$then

$$
h _ {p} h _ {\infty} = \# (\mathcal {O} / \lambda) ^ {3 n} \# H ^ {0} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}} ^ {*}) / \# H ^ {0} (\mathbf {Q}, V _ {\lambda^ {n}} ^ {*})
$$

in the unrestricted case.

(ii)$I f X = V _ { \lambda ^ { r } }$then

$$
h _ {p} h _ {\infty} \leq \# (\mathcal {O} / \lambda) ^ {n} \# H ^ {0} (\mathbf {Q} _ {p}, (V _ {\lambda^ {n}} ^ {\mathrm{ord}}) ^ {*}) / \# H ^ {0} (\mathbf {Q}, W _ {\lambda^ {n}} ^ {*})
$$

in the ordinary case.

(iii) If$X = { V _ { \lambda ^ { n } } } o r W _ { \lambda ^ { n } }$then$h _ { p } h _ { \infty } \leq \# H ^ { 0 } ( \mathbf { Q } _ { p } , ( W _ { \lambda ^ { n } } ^ { 0 } ) ^ { * } ) / \# H ^ { 0 } ( \mathbf { Q } , W _ { \lambda ^ { n } } ^ { * } )$ in the Selmer case.

(iv)$I f X = V _ { \lambda ^ { n } }$or$W _ { \lambda ^ { n } }$then$h _ { p } h _ { \infty } = 1$in the strict case.

(v) If$X = V _ { \lambda ^ { n } }$then$h _ { p } h _ { \infty } = 1$in the flat case.

(vi) If X = V<sub>λ</sub>n or$W _ { \lambda ^ { n } }$then$h _ { p } h _ { \infty } ~ = ~ 1 / \# H ^ { 0 } ( \mathbf { Q } , V _ { \lambda ^ { n } } ^ { * } ) ~ i f ~ L _ { n , p } ~ =$ $H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , X )$and$\rho _ { f , \lambda }$arises from an ordinary p-divisible group.

Proof. Case (i) is trivial. Consider then case (ii) with$X = V _ { \lambda ^ { n } }$We have a long exact sequence of cohomology associated to the exact sequence:

$$
0 \to W _ {\lambda^ {n}} ^ {0} \to V _ {\lambda^ {n}} \to V _ {\lambda^ {n}} / W _ {\lambda^ {n}} ^ {0} \to 0.\tag{1.16}
$$

In particular this gives the map u in the diagram

$$
\begin{array}{c} H ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}) \\ \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \delta \\ 1 \to Z = H ^ {1} (\mathbf {Q} _ {p} ^ {\mathrm{unr}} / \mathbf {Q} _ {p}, (V _ {\lambda^ {n}} / W _ {\lambda^ {n}} ^ {0}) ^ {\mathcal {H}}) \to H ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}} / W _ {\lambda^ {n}} ^ {0}) \to H ^ {1} (\mathbf {Q} _ {p} ^ {\mathrm{unr}}, V _ {\lambda^ {n}} / W _ {\lambda^ {n}} ^ {0}) ^ {\mathcal {G}} \to 1 \end{array}
$$

where$\mathcal { G } = \mathrm { G a l } ( \mathbf { Q } _ { p } ^ { \mathrm { u n r } } / \mathbf { Q } _ { p } ) , \mathcal { H } = \mathrm { G a l } ( \bar { \mathbf { Q } } _ { p } / \mathbf { Q } _ { p } ^ { \mathrm { u n r } } )$and δ is defined to make the triangle commute. Then writing$h _ { i } ( M )$for$\dot { \# } H ^ { 1 } ( \mathbf { Q } _ { p } , M )$we have that$\# Z =$ $h _ { 0 } ( V _ { \lambda ^ { n } } / W _ { \lambda ^ { n } } ^ { 0 } )$and$\#$im$\delta \ge ( \# \mathrm { i m } u ) / ( \# Z )$. A simple calculation using the long exact sequence associated to (1.16) gives

$$
\# \mathrm{im} u = \frac {h _ {1} (V _ {\lambda^ {n}} / W _ {\lambda^ {n}} ^ {0}) h _ {2} (V _ {\lambda^ {n}})}{h _ {2} (W _ {\lambda^ {n}} ^ {0}) h _ {2} (V _ {\lambda^ {n}} / W _ {\lambda^ {n}} ^ {0})}.\tag{1.17}
$$

Hence

$$
[ H ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}): L _ {n, p} ] = \# \mathrm{im} \delta \geq \# (\mathcal {O} / \lambda) ^ {3 n} h _ {0} (V _ {\lambda^ {n}} ^ {*}) / h _ {0} (W _ {\lambda^ {n}} ^ {0}) ^ {*}.
$$

The inequality in (iii) follows for$X = V _ { \lambda ^ { \prime } }$n and the case$X = W _ { \lambda ^ { \prime } }$is similar. Case (ii) is similar. In case (iv) we just need #im u which is given by (1.17) with$W _ { \lambda ^ { n } }$replacing$V _ { \lambda ^ { n } }$. In case$\mathrm { ( v ) }$we have already observed in Section 1 that Raynaud’s results imply that$\# H ^ { 0 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } ^ { * } ) = 1$in the flat case. Moreover #$H _ { \mathrm { f } } ^ { 1 } ( \mathbf { Q } _ { p } , V _ { \lambda ^ { n } } )$can be computed to be$\# ( \mathcal { O } / \lambda ) ^ { 2 n }$from

$$
H _ {\mathrm{f}} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}) \simeq H _ {\mathrm{f}} ^ {1} (\mathbf {Q} _ {p}, V) _ {\lambda^ {n}} \simeq \mathrm{Hom} _ {\mathcal {O}} (\mathfrak {p} _ {R} / \mathfrak {p} _ {R} ^ {2}, K / \mathcal {O}) _ {\lambda^ {n}}
$$

where R is the universal local flat deformation ring of$\rho _ { 0 }$for O-algebras. Using the relation$R \simeq R ^ { \mathrm { { f } \mathrm { { f } } } } \otimes \mathcal { O }$where$R ^ { \mathrm { { f } } }$is the corresponding ring for$W ( k ) .$ W(k) algebras, and the main theorem of [Ram] (Theorem 4.2) which computes$R ^ { \mathrm { { f } } }$ we can deduce the result.

We now prove (vi). From the definitions

$$
\# H _ {F} ^ {1} (\mathbf {Q} _ {p}, V _ {\lambda^ {n}}) = \left\{ \begin{array}{l l} (\# \mathcal {O} / \lambda^ {n}) ^ {r} \# H ^ {0} (\mathbf {Q} _ {p}, W _ {\lambda^ {n}}) & \text {if \rho_{f,\lambda}|_{D_{p}} does not split} \\ (\# \mathcal {O} / \lambda^ {n}) ^ {r} & \text {if \rho_{f,\lambda}|_{D_{p}} splits} \end{array} \right.
$$

where$r = \dim _ { K } H _ { F } ^ { 1 } ( \mathbf { Q } _ { p } , \mathcal { V } )$. This we can compute using the calculations in [BK, Cor. 3.8.4]. We find that$r = 2$in the non-split case and$r = 3$in the split case and (vi) follows easily.

## 3. Some results on subgroups of$\operatorname { G L _ { 2 } } ( k )$

We now give two group-theoretic results which will not be used until Chapter 3. Although these could be phrased in purely group-theoretic terms it will be more convenient to continue to work in the setting of Section 1, i.e., with$\rho _ { 0 }$as in (1.1) so that im$\rho _ { 0 }$is a subgroup of$\operatorname { G L _ { 2 } } ( k )$and det$\rho _ { 0 }$is assumed odd.

## Lemma 1.10. If im$\rho _ { 0 }$has order divisible by p then:

(i) It contains an element$\gamma _ { 0 }$of order$m \geq 3$with$( m , p ) = 1$and$\gamma _ { 0 }$trivial on any abelian quotient of im$\rho _ { 0 }$

(ii) It contains an element$\rho _ { 0 } ( \sigma )$with any prescribed image in the Sylow 2-subgroup of (im$\rho _ { 0 } ) / ( \mathrm { i m } \ \rho _ { 0 } ) ^ { \prime }$and with the ratio of the eigenvalues not equal to$\omega ( \sigma )$. (Here$( \mathrm { i m } ~ \rho _ { 0 } ) ^ { \prime }$denotes the derived subgroup of$( \mathrm { i m } \ \rho _ { 0 } ) . )$

The same results hold if the image of the projective representation$\tilde { \rho } _ { 0 }$associated to$\rho _ { 0 }$is isomorphic to$A _ { 4 } , S _ { 4 } \ o r \ A _ { 5 }$

Proof. (i) Let$G = { \mathrm { i m } } \ \rho _ { 0 }$and let$Z$denote the center of$G .$Then we have a surjection$G ^ { \prime } \to ( G / Z ) ^ { \prime }$where the <sup></sup> denotes the derived group. By Dickson’s classification of the subgroups of$\operatorname { G L _ { 2 } } ( k )$containing an element of order$p , ( G / Z )$is isomorphic to$\mathrm { P G L _ { 2 } } ( k ^ { \prime } )$or$\mathrm { P S L _ { 2 } } ( k ^ { \prime } )$for some finite field$k ^ { \prime }$of characteristic p or possibly to$A _ { 5 }$when$p = 3$, cf. [Di, §260]. In each case we can find, and then lift to$G ^ { \prime } { \mathrm { . } }$an element of order m with$( m , p ) = 1$and$m \geq 3 .$ except possibly in the case$p = 3$and$\mathrm { P S L _ { 2 } } ( \mathbf { F } _ { 3 } ) \simeq A _ { 4 }$or$\mathrm { P G L _ { 2 } } ( \mathbf { F } _ { 3 } ) \simeq S _ { 4 }$ However in these cases$( G / Z ) ^ { \prime }$has order divisible by 4 so the 2-Sylow subgroup of$G ^ { \prime }$has order greater than 2. Since it has at most one element of exact order $2$(the eigenvalues would both be$^ { - 1 }$since it is in the kernel of the determinant and hence the element would be$- I )$it must also have an element of order 4.

The argument in the$A _ { 4 } , S _ { 4 }$and$A _ { 5 }$cases is similar.

(ii) Since$\rho _ { 0 }$is assumed absolutely irreducible,$G =$im$\rho _ { 0 }$has no fixed line. We claim that the same then holds for the derived group$G ^ { \prime }$For otherwise since$G ^ { \prime } \triangleleft G$we could obtain a second fixed line by taking$\langle g v \rangle$where$\langle v \rangle$is the original fixed line and$g$is a suitable element of$G .$. Thus$G ^ { \prime }$would be contained in the group of diagonal matrices for a suitable basis and it would be central in which case$G$would be abelian or its normalizer in$\operatorname { G L _ { 2 } } ( k )$, and hence also$G ,$would have order prime to$p .$Since neither of these possibilities is allowed,$G ^ { \prime }$has no fixed line.

By Dickson’s classification of the subgroups of$\operatorname { G L _ { 2 } } ( k )$containing an element of order$p$the image of im$\rho _ { 0 }$in$\mathrm { P G L _ { 2 } } ( k )$is isomorphic to$\mathrm { P G L _ { 2 } } ( k ^ { \prime } )$ or$\mathrm { P S L _ { 2 } } ( k ^ { \prime } )$for some finite field$k ^ { \prime }$of characteristic$p$or possibly to$A _ { 5 }$when $p = 3$. The only one of these with a quotient group of order$p$is$\mathrm { P S L _ { 2 } ( F _ { 3 } ) }$ when$p = 3$. It follows that$p \dag [ G : G ^ { \prime } ]$except in this one case which we treat separately. So assuming now that$p \dag \left[ G : G ^ { \prime } \right]$we see that$G ^ { \prime }$contains a non-trivial unipotent element$u .$Since$G ^ { \prime }$has no fixed line there must be another noncommuting unipotent element v in$G ^ { \prime }$. Pick a basis for$\rho _ { 0 } | _ { G ^ { \prime } }$consisting of their fixed vectors. Then let$\tau$be an element of$\operatorname { G a l } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } )$for which the image of$\rho _ { 0 } ( \tau )$in$G / G ^ { \prime }$is prescribed and let$\textstyle \rho _ { 0 } ( \tau ) = ( _ { c } ^ { a \ b } )$. Then

$$
\delta = \left( \begin{array}{c c} a & b \\ c & d \end{array} \right) \left( \begin{array}{c c} 1 & s \alpha \\ & 1 \end{array} \right) \left( \begin{array}{c c} 1 & \\ r \beta & 1 \end{array} \right)
$$

has det$( \delta ) = \operatorname* { d e t } \rho _ { 0 } ( \tau )$and trace$\delta = s \alpha ( r a \beta + c ) + b r \beta + a + d .$Since$p \geq 3$ we can choose this trace to avoid any two given values (by varying s) unless $r a \beta + c = 0$for all$r .$But$r a \beta + c$cannot be zero for all$r$as otherwise $a = c = 0$. So we can find a$\delta$for which the ratio of the eigenvalues is not $\omega ( \tau ) , \operatorname* { d e t } ( \delta )$being, of course, fixed.

Now suppose that im$\rho _ { 0 }$does not have order divisible by$p$but that the associated projective representation$\widetilde { \rho _ { 0 } }$has image isomorphic to$S _ { 4 }$or$A _ { 5 }$, so necessarily$p \neq 3$. Pick an element$\tau$such that the image of$\rho _ { 0 } ( \tau )$in$G / G ^ { \prime }$is any prescribed class. Since this fixes both det$\rho _ { 0 } ( \tau )$and$\omega ( \tau )$we have to show that we can avoid at most two particular values of the trace for$\tau$. To achieve this we can adapt our first choice of$\tau$by multiplying by any element og$G ^ { \prime }$. So pick$\sigma \in G ^ { \prime }$as in (i) which we can assume in these two cases has order$3 .$. Pick a basis for$\rho _ { 0 }$, by expending scalars if necessary, so that$\sigma \mapsto \left( \begin{array} { c } { { \alpha } } \\ { { \alpha ^ { - 1 } } } \end{array} \right)$. Then one checks easily that if$\textstyle \rho _ { 0 } ( \tau ) = ( _ { c } ^ { a \ b } )$we cannot have the traces of all of$\tau , \sigma \tau$and $\sigma ^ { 2 } \tau$lying in a set of the form$\{ \mp t \}$unless$a = d = 0$. However we can ensure that$\rho _ { 0 } ( \tau )$does not satisfy this by first multiplying$\tau$by a suitable element of $G ^ { \prime }$since$G ^ { \prime }$is not contained in the diagonal matrices (it is not abelian).

In the$A _ { 4 }$case, and in the$\mathrm { P S L _ { 2 } } ( \mathbf { F } _ { 3 } ) \simeq A _ { 4 }$case when$p = 3$, we use a diferent argument. In both cases we find that the 2-Sylow subgroup of$G / G ^ { \prime }$ is generated by an element z in the centre of$G$. Either a power of$z$is a suitable candidate for$\rho _ { 0 } ( \sigma )$or else we must multiply the power of z by an element of $G ^ { \prime }$, the ratio of whose eigenvalues is not equal to 1. Such an element exists because in$G ^ { \prime }$the only possible elements without this property are$\{ \mp I \}$(such elements necessary have determinant 1 and order prime to$p )$and we know that$\# G ^ { \prime } > 2$as was noted in the proof of part (i).

Remark. By a well-known result on the finite subgroups of$\mathrm { P G L _ { 2 } } ( \overline { { \mathbf { F } } } _ { p } )$this lemma covers all$\rho _ { 0 }$whose images are absolutely irreducible and for which$\widetilde { \rho _ { 0 } }$ is not dihedral.

Let$K _ { 1 }$be the splitting field of$\rho _ { 0 }$. Then we can view$W _ { \lambda }$and$W _ { \lambda } ^ { * }$as Gal$( K _ { 1 } ( \zeta _ { p } ) / \mathbf { Q } )$-modules. We need to analyze their cohomology. Recall that we are assuming that$\rho _ { 0 }$is absolutely irreducible. Let$\widetilde { \rho _ { 0 } }$be the associated projective representation to$\mathrm { P G L _ { 2 } } ( k )$

The following proposition is based on the computations in [CPS].

Proposition 1.11. Suppose that$\rho _ { 0 }$is absolutely irreducible. Then

$$
H ^ {1} (K _ {1} (\zeta_ {p}) / \mathbf {Q}, W _ {\lambda} ^ {*}) = 0.
$$

Proof. If the image of$\rho _ { 0 }$has order prime to$p$the lemma is trivial. The subgroups of$\operatorname { G L _ { 2 } } ( k )$containing an element of order$p$which are not contained in a Borel subgroup have been classified by Dickson [Di, §260] or [Hu, II.8.27]. Their images inside$\mathrm { P G L _ { 2 } } ( k ^ { \prime } )$where$k ^ { \prime }$is the quadratic extension of k are conjugate to$\mathrm { P G L _ { 2 } } ( F )$or$\mathrm { P S L _ { 2 } } ( F )$for some subfield$F$of$k ^ { \prime }$, or they are isomorphic to one of the exceptional groups$A _ { 4 } , S _ { 4 } , A _ { 5 }$

Assume then that the cohomology group$H ^ { 1 } ( K _ { 1 } ( \zeta _ { p } ) / { \bf Q } , W _ { \lambda } ^ { * } ) \ne 0$. Then by considering the inflation-restriction sequence with respect to the normal subgroup$\mathrm { G a l } ( K _ { 1 } ( \zeta _ { p } ) / K _ { 1 } )$we see that$\zeta _ { p } \in K _ { 1 }$. Next, since the representation is (absolutely) irreducible, the center Z of$\operatorname { G a l } ( K _ { 1 } / \mathbf { Q } )$is contained in the diagonal matrices and so acts trivially on$W _ { \lambda }$. So by considering the inflationrestriction sequence with respect to$Z$we see that$Z$acts trivially on$\zeta _ { p }$(and on$W _ { \lambda } ^ { * } )$. So$\operatorname { G a l } ( \mathbf { Q } ( \zeta _ { p } ) / \mathbf { Q } )$is a quotient of$\operatorname { G a l } ( K _ { 1 } / \mathbf { Q } ) / Z$. This rules out all cases when$p \neq 3$, and when$p = 3$we only have to consider the case where the image of the projective representation is isomporphic as a group to$\mathrm { P G L _ { 2 } } ( F )$ for some finite field of characteristic 3. (Note that$S _ { 4 } \simeq \mathrm { P G L _ { 2 } ( F _ { 3 } ) . } )$

Extending scalars commutes with formation of duals and$H ^ { 1 }$, so we may assume without loss of generality$F \subseteq k$. If$p \ = \ 3$and #$F ~ > ~ 3$then $H ^ { 1 } ( \mathrm { P S L } _ { 2 } ( F ) , W _ { \lambda } ) \ = \ 0$by results of [CPS]. Then if$\widetilde { \rho _ { 0 } }$is the projective representation associated to$\rho _ { 0 }$suppose that$g ^ { - 1 } \mathrm { i m } \ \widetilde { \rho _ { 0 } } g = \mathrm { P G L } _ { 2 } ( F )$and let $H = g \mathrm { P S L } _ { 2 } ( F ) g ^ { - 1 }$. Then$W _ { \lambda } \simeq W _ { \lambda } ^ { * }$over H and

$$
H ^ {1} (H, W _ {\lambda}) \underset {F} {\otimes} \bar {F} \simeq H ^ {1} (g ^ {- 1} H g, g ^ {- 1} (W _ {\lambda} \underset {F} {\otimes} \bar {F})) = 0.\tag{1.18}
$$

We deduce also that$H ^ { 1 } ( \mathrm { i m } \rho _ { 0 } , W _ { \lambda } ^ { * } ) = 0$

Finally we consider the case where$F = \mathbf { F } _ { 3 }$. I am grateful to Taylor for the following argument. First we consider the action of$\mathrm { P S L _ { 2 } ( F _ { 3 } ) }$on$W _ { \lambda }$explicitly by considering the conjugation action on matrices$\{ A \in M _ { 2 } ( \mathbf { F } _ { 3 } )$: trace$A = 0 \}$ One sees that no such matrix is fixed by all the elements of order 2, whence

$$
H ^ {1} (\mathrm{PSL} _ {2} (\mathbf {F} _ {3}), W _ {\lambda}) \simeq H ^ {1} (\mathbf {Z} / 3, (W _ {\lambda}) ^ {C _ {2} \times C _ {2}}) = 0
$$

where$C _ { 2 } \times C _ { 2 }$denotes the normal subgroup of order 4 in$\mathrm { P S L _ { 2 } } ( \mathbf { F } _ { 3 } ) \simeq A _ { 4 }$. Next we verify that there is a unique copy of$A _ { 4 }$in$\mathrm { P G L _ { 2 } ( \bar { \bf F } _ { 3 } ) }$up to conjugation. For suppose that A,$B \in \mathrm { G L _ { 2 } } ( \bar { \bf F } _ { 3 } )$are such that$A ^ { 2 } = B ^ { 2 } = I$with the images of$A , B$representing distinct nontrivial commuting elements of$\mathrm { P G L _ { 2 } ( \bar { \bf F } _ { 3 } ) }$. We can choose${ \boldsymbol { A } } = \bigl ( \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { - 1 } \end{array} \bigr )$by a suitable choice of basis, i.e., by a suitable conjugation. Then B is diagonal or antidiagonal as it commutes with A up to a scalar, and as B, A are distinct in$\mathrm { P G L _ { 2 } ( \overline { { F } } _ { 3 } ) }$we have$\boldsymbol { B } = \bigl ( \begin{array} { l l } { 0 - \boldsymbol { a } ^ { - 1 } } \\ { \boldsymbol { a } } & { 0 } \end{array} \bigr )$for some a. By conjugating by a diagonal matrix (which does not change A) we can assume that$a = 1$. The group generated by$\{ A , B \}$in$\mathrm { P G L _ { 2 } ( F _ { 3 } ) }$is its own centralizer so it has index at most 6 in its normalizer N. Since$N / \langle A , B \rangle \simeq S _ { 3 }$ there is a unique subgroup of N in which$\langle A , B \rangle$has index 3 whence the image of the embedding of$A _ { 4 }$in$\mathrm { P G L _ { 2 } ( \bar { \bf F } _ { 3 } ) }$is indeed unique (up to conjugation). So arguing as in (1.18) by extending scalars we see that$H ^ { 1 } ( \mathrm { i m } \rho _ { 0 } , W _ { \lambda } ^ { * } ) = 0$when $F = \mathbf { F } _ { 3 }$also.

The following lemma was pointed out to me by Taylor. It permits most dihedral cases to be covered by the methods of Chapter 3 and [TW].

## Lemma 1.12. Suppose that$\rho _ { 0 }$is absolutely irreducible and that

(a)$\tilde { \rho } _ { 0 }$is dihedral (the case where the image is$\mathbf { Z } / 2 \times \mathbf { Z } / 2$is allowed),

(b) ρ | is absolutely irreducible where$L = \mathbf { Q } { \Big ( } { \sqrt { ( - 1 ) ^ { ( p - 1 ) / 2 } p } } { \Big ) }$

Then for any positive integer n and any irreducible Galois stable subspace X of$W _ { \lambda } \otimes \bar { k }$there exists an element$\sigma \in \operatorname { G a l } ( { \bar { \mathbf { Q } } } / \mathbf { Q } )$such that

(i)$\tilde { \rho } _ { 0 } ( \sigma ) \neq 1 .$

(ii) σ fixes$\mathbf { Q } ( \zeta _ { p ^ { n } } )$

(iii) σ has an eigenvalue 1 on$X$.

Proof. If$\tilde { \rho } _ { 0 }$is dihedral then$\rho _ { 0 } \otimes \bar { k } = \mathrm { I n d } _ { H } ^ { G } \chi$for some H of index 2 in$G ,$ where$G = \operatorname { G a l } ( K _ { 1 } / \mathbf { Q } )$. (As before,$K _ { 1 }$is the splitting field of$\rho _ { 0 } . )$Here H can be taken as the full inverse image of any of the normal subgroups of index 2 defining the dihedral group. Then$W _ { \lambda } \otimes \bar { k } \simeq \delta \oplus \mathrm { I n d } _ { H } ^ { G } ( \chi / \chi ^ { \prime } )$where δ is the quadratic character$G  G / H$and$\chi ^ { \prime }$is the conjugate of$\chi$by any element of $G - H$. Note that$\chi \neq \chi ^ { \prime }$since H has nontrivial image in$\mathrm { P G L _ { 2 } } ( \bar { k } )$

To find a$\sigma$such that$\delta ( \sigma ) = 1$and conditions (i) and (ii) hold, observe that$M ( \zeta _ { p ^ { n } } )$is abelian where M is the quadratic field associated to δ. So conditions (i) and (ii) can be satisfied if$\tilde { \rho } _ { 0 }$is non-abelian. If$\tilde { \rho } _ { 0 }$is abelian$( \mathrm { i . e . }$ the image has the form$\mathbf { Z } / 2 \times \mathbf { Z } / 2 )$, then we use hypothesis (b). If Ind$\ l _ { H } ^ { G } ( \chi / \chi ^ { \prime } )$ is irreducible over$\bar { k }$then$W _ { \lambda } \otimes \bar { k }$is a sum of three distinct quadratic characters, none of which is the quadratic character associated to$L ,$and we can repeat the argument by changing the choice of H for the other two characters. If $X = \bar { \mathrm { I n d } _ { H } ^ { G } } ( \chi / \chi ^ { \prime } ) \otimes \bar { k }$is absolutely irreducible then pick any$\sigma \in G - H$This satisfies (i) and can be made to satisfy (ii) if (b) holds. Finally, since$\sigma \in G - H$ we see that$\sigma$has trace zero and$\sigma ^ { 2 } = \mathrm { \ i }$in its action on$X$. Thus it has an eigenvalue equal to 1.

## Chapter 2

In this chapter we study the Hecke rings. In the first section we recall some of the well-known properties of these rings and especially the Gorenstein property whose proof is rather technical, depending on a characteristic p version of the q-expansion principle. In the second section we compute the relations between the Hecke rings as the level is augmented. The purpose is to find the change in the η-invariant as the level increases.

In the third section we state the conjecture relating the deformation rings of Chapter 1 and the Hecke rings. Finally we end with the critical step of showing that if the conjecture is true at a minimal level then it is true at all levels. By the results of the appendix the conjecture is equivalent to the equality of the η-invariant for the Hecke rings and the${ \mathfrak { p } } / { \mathfrak { p } } ^ { 2 }$-invariant for the deformation rings. In Chapter 2, Section 2, we compute the change in the η-invariant and in Chapter 1, Section 1, we estimated the change in the${ \mathfrak { p } } / { \mathfrak { p } } ^ { 2 } .$ invariant.

## 1. The Gorenstein property

For any positive integer N let$X _ { 1 } ( N ) = X _ { 1 } ( N ) _ { / { \bf Q } }$be the modular curve over Q corresponding to the group$\Gamma _ { 1 } ( N )$and let$\dot { J _ { 1 } } ( N )$be its Jacobian. Let ${ \bf T } _ { 1 } ( N )$be the ring of endomorphisms of$J _ { 1 } ( N )$which is generated over Z by the standard Hecke operators$\{ T _ { l } = T _ { l * }$for$l \dag N , U _ { q } = U _ { q * }$for$q | N , \langle a \rangle = \langle a \rangle ,$∗ for$( a , N ) \ : = \ : 1 \}$. For precise definitions of these see$\mathrm { [ M W 1 , ~ C h . ~ \nabla 2 , \ S 5 ] }$In particular if one identifies the cotangent space of$J _ { 1 } ( N ) ( { \bf C } )$with the space of cusp forms of weight 2 on$\Gamma _ { 1 } ( N )$then the action induced by${ \bf T } _ { 1 } ( N )$is the usual one on cusp forms. We let$\Delta = \{ \langle a \rangle : ( a , N ) = 1 \}$

The group$( { \mathbf { Z } } / N { \mathbf { Z } } ) ^ { * }$acts naturally on$X _ { 1 } ( N )$via$\Delta$and for any subgroup$H \subseteq ( \mathbf { Z } / N \mathbf { Z } ) ^ { * }$we let$X _ { H } ( N ) = X _ { H } ( N ) _ { / \mathbf { Q } }$be the quotient$X _ { 1 } ( N ) / H$ Thus for$H = ( \mathbf { Z } / N \mathbf { Z } ) ^ { * }$we have$X _ { H } ( N ) = X _ { 0 } ( N )$corresponding to the group $\Gamma _ { 0 } ( N )$. In Section 2 it will sometimes be convenient to assume that H decomposes as a product$H = \prod H _ { q }$in$( \mathbf { Z } / N \mathbf { Z } ) ^ { * } \simeq \Pi ( \mathbf { Z } / q ^ { r } \mathbf { Z } ) ^ { * }$where the product is over the distinct prime powers dividing N. We let$J _ { H } ( N )$denote the Jacobian of$X _ { H } ( N )$and note that the above Hecke operators act naturally on $J _ { H } ( N )$also. The ring generated by these Hecke operators is denoted${ \bf T } _ { H } ( N )$ and sometimes, if H and N are clear from the context, we addreviate this to T.

Let$p$be a prime$\geq 3$. Let m be a maximal ideal of$\mathbf { T } = \mathbf { T } _ { H } ( N )$with $p \in \mathfrak { m }$. Then associated to m there is a continuous odd semisimple Galois representation$\rho _ { \mathfrak { m } }$

$$
\rho_ {\mathfrak {m}}: \operatorname{Gal} (\overline {{\mathbf {Q}}} / \mathbf {Q}) \to \operatorname{GL} _ {2} (\mathbf {T} / \mathfrak {m})\tag{2.1}
$$

unramified outside$N p$which satisfies

$$
\operatorname{trace} \rho_ {\mathfrak {m}} (\text { Frob } q) = T _ {q}, \det \rho_ {\mathfrak {m}} (\text { Frob } q) = \langle q \rangle q
$$

for each prime$q \nmid N p$. Here Frob$q$denotes a Frobenius at$q$in${ \mathrm { G a l } } ( { \overline { { \mathbf { Q } } } } / \mathbf { Q } )$ The representation$\rho _ { \mathfrak { m } }$is unique up to isomorphism. If$p \nmid N$(resp.$p | N )$we say that m is ordinary if$T _ { p } \notin$m (resp.$U _ { p } \notin \mathfrak { m } )$. This implies (cf., for example, theorem 2 of [Wi1]) that for our fixed decomposition group$D _ { p }$at$p _ { : }$

$$
\rho_ {\mathfrak {m}} \Big | _ {D _ {p}} \approx \left( \begin{array}{c c} \chi_ {1} & * \\ 0 & \chi_ {2} \end{array} \right)
$$

for a suitable choic of basis, with$\chi _ { 2 }$unramified and$\chi _ { 2 } ( \mathrm { F r o b } ~ p ) = T _ { p }$mod m (resp. equal to$U _ { p } )$. In particular$\rho _ { \mathfrak { m } }$is ordinary in the sense of Chapter 1 provided$\chi _ { 1 } \neq \chi _ { 2 }$. We will say that m is$D _ { p }$-distinguished if m is ordinary and $\chi _ { 1 } \neq \chi _ { 2 }$. (In practice$\chi _ { 1 }$is usually ramified so this imposes no extra condition.) We caution the reader that if$\rho _ { \mathfrak { m } }$is ordinary in the sense of Chapter 1 then we can only conclude that m is$D _ { p }$-distinguished if$p \nmid N$

Let$\mathbf { T } _ { \mathfrak { m } }$denote the completion of T at m so that$\mathbf { T } _ { \mathfrak { m } }$is a direct factor of the complete semi-local ring$\mathbf { T } _ { \boldsymbol { p } } = \mathbf { T } \otimes \mathbf { Z } _ { \boldsymbol { p } }$. Let D be the points of the associated m-divisible group

$$
\mathcal {D} = J _ {H} (N) (\overline {{\mathbf {Q}}}) _ {\mathfrak {m}} \simeq J _ {H} (N) (\overline {{\mathbf {Q}}}) _ {p ^ {\infty}} \underset {\mathbf {T} _ {p}} {\otimes} \mathbf {T} _ {\mathfrak {m}}.
$$

It is known that$\hat { \mathcal { D } } = \operatorname { H o m } _ { \mathbf { Z } _ { p } } ( \mathcal { D } , \mathbf { Q } _ { p } / \mathbf { Z } _ { p } )$is a rank 2$\mathbf { T } _ { \mathfrak { m } }$-module, i.e., that $\hat { \mathcal { D } } \bigotimes _ { \mathbf { Z } _ { p } } \mathbf { Q } _ { p } \simeq \big ( \mathbf { T } _ { \mathfrak { m } } \bigotimes _ { \mathbf { Z } _ { p } } \mathbf { Q } _ { p } \big ) ^ { 2 }$. Briefly it is enough to show that$H ^ { 1 } ( X _ { H } ( N ) , { \bf C } )$is free of rank 2 over$\mathbf { T } \otimes \mathbf { C }$and this reduces to showing that$S _ { 2 } ( \Gamma _ { H } ( N ) , { \bf C } )$，the space of cusp forms of weight 2 on$\Gamma _ { H } ( N )$, is free of rank 1 over$\mathbf { T } \otimes \mathbf { C }$ One shows then that if$\{ f _ { 1 } , \ldots , f _ { r } \}$is a complete set of normalized newforms in$S _ { 2 } ( \Gamma _ { H } ( N ) , { \bf C } )$of levels$m _ { 1 } , \ldots , m _ { \tau }$then if we set$d _ { i } ~ = ~ N / m _ { i }$, the form $\textstyle f = \Sigma f _ { i } ( d _ { i } z )$is a basis vector of$S _ { 2 } ( \Gamma _ { H } ( N ) , { \bf C } )$as a$\mathbf { T } \otimes \mathbf { C }$-module.

If m is ordinary then Theorem 2 of [Wi1], itself a straightforward generalization of Proposition 2 and (11) of [MW2], shows that (for our fixed decomposition group$D _ { p } )$there is a filtration of D by Pontrjagin duals of rank 1 $\mathbf { T } _ { \mathfrak { m } }$-modules (in the sense explained above)

$$
0 \to \mathcal {D} ^ {0} \to \mathcal {D} \to \mathcal {D} ^ {E} \to 0\tag{2.2}
$$

where$\mathcal { D } ^ { 0 }$is stable under$D _ { p }$and the induced action on$\mathcal { D } ^ { E }$is unramified with Frob$p = U _ { p }$on it if$p | N$and Frob$p$equal to the unit root of$x ^ { 2 } - T _ { p } x + p \langle p \rangle$ $= ~ 0$in$\mathbf { T } _ { \mathfrak { m } }$if$p \nmid N$We can describe$\mathcal { D } ^ { 0 }$and$\mathcal { D } ^ { E }$as follows. Pick$_ { \mathrm { ~ a ~ } \sigma \mathrm { ~ } } \in$ $I _ { p }$which induces a generator of Gal$( \mathbf { Q } _ { p } ( \zeta _ { N p ^ { \infty } } ) / \mathbf { Q } _ { p } ( \zeta _ { N p } ) )$. Let$\varepsilon : D _ { p } \to \mathbf { Z } _ { p } ^ { \times }$ be the cyclotomic character. Then${ \mathcal D } ^ { 0 } = \mathrm { k e r } ( \sigma - \varepsilon ( \sigma ) ) ^ { \mathrm { d i v } }$, the kernel being taken inside$\mathcal { D }$and ‘div’ meaning the maximal divisible subgroup. Although in [Wi1] this filtration is given only for a factor$A _ { f }$of$J _ { 1 } ( N )$it is easy to deduce the result for$J _ { H } ( N )$itself. We note that this filtration is defined without reference to characteristic p and also that if m is$D _ { p }$-distinguished,$\mathcal { D } ^ { 0 }$ (resp.$\mathcal { D } ^ { E } )$can be described as the maximal submodule on which$\sigma - \tilde { \chi } _ { 1 } ( \sigma )$ is topologically nilpotent for all$\sigma \in \operatorname { G a l } ( { \overline { { \mathbf { Q } } } } _ { p } / \mathbf { Q } _ { p } )$(resp. quotient on which $\sigma - \tilde { \chi } _ { 2 } ( \sigma )$is topologically nilpotent for all$\sigma \in \operatorname { G a l } ( { \overline { { \mathbf { Q } } } } _ { p } / \mathbf { Q } _ { p } ) )$, where$\tilde { \chi } _ { i } ( \sigma )$is any lifting of$\chi _ { i } ( \sigma )$to$\mathbf { T } _ { \mathfrak { m } }$

The Weil pairing$\langle ~ , ~ \rangle$on$J _ { H } ( { \cal N } ) ( \overline { { { \bf Q } } } ) _ { p ^ { M } }$satisfies the relation$\langle t _ { * } x , y \rangle =$ $\langle x , t ^ { * } y \rangle$for any Hecke operator t. It is more convenient to use an adapted pairing defined as follows. Let$w _ { \zeta }$, for$\zeta \ a$primitive$N ^ { \mathrm { t h } }$root of 1, be the involution of$X _ { 1 } ( N ) _ { / \mathbf { Q } ( \zeta ) }$defined in [MW1, p. 235]. This induces an involution of$X _ { H } ( N ) _ { / \mathbf { Q } ( \zeta ) }$also. Then we can define a new pairing [ , ] by setting (for a

fixed choice of$\zeta )$

$$
[ x, y ] = \langle x, w _ {\zeta} y \rangle .\tag{2.3}
$$

Then$[ t _ { * } x , y ] = [ x , t _ { * } y ]$for all Hecke operators t. In particular we obtain an induced pairing on$\mathcal { D } _ { p ^ { M } }$

The following theorem is the crucial result of this section. It was first proved by Mazur in the case of prime level [Ma2]. It has since been generalized in [Ti1], [Ri1] [M Ri], [Gro] and [E1], but the fundamental argument remains that of [Ma2]. For a summary see [E1, §9]. However some of the cases we need are not covered in these accounts and we will present these here.

Theorem 2.1. (i) If p  N and$\rho _ { \mathfrak { m } }$is irreducible then

$$
J _ {H} (N) (\overline {{\mathbf {Q}}}) [ \mathfrak {m} ] \simeq (\mathbf {T} / \mathfrak {m}) ^ {2}.
$$

(ii)$I f p \nmid N$and$\rho _ { \mathfrak { m } }$is irreducible and m is$D _ { p }$-distinguished then

$$
J _ {H} (N p) (\overline {{\mathbf {Q}}}) [ \mathfrak {m} ] \simeq (\mathbf {T} / \mathfrak {m}) ^ {2}.
$$

(In case (ii) m is a maximal ideal of$\mathbf { T } = \mathbf { T } _ { H } ( N p ) . )$

Corollary 1. In case (i),$J _ { H } ( \widehat { N ) ( \mathbf { Q } } ) _ { \mathfrak { m } } \simeq \mathbf { T } _ { \mathfrak { m } } ^ { 2 }$and$\mathrm { T a } _ { \mathfrak { m } } \Big ( J _ { H } \big ( N \big ) ( \overline { { \mathbf { Q } } } ) \Big ) \simeq$ $\mathbf { T } _ { \mathfrak { m } } ^ { 2 }$

In case (ii),$J _ { H } ( \widetilde { N p } ) ( \overline { { { \bf Q } } } ) _ { \mathfrak { m } } \simeq { \bf T } _ { \mathfrak { m } } ^ { 2 }$and$\mathrm { T a } _ { \mathfrak { m } } \Big ( J _ { H } \big ( N p \big ) ( \overline { { \mathbf { Q } } } ) \Big ) \ \simeq \ \mathbf { T } _ { \mathfrak { m } } ^ { 2 }$(where $\mathbf { T } _ { \mathfrak { m } } = \mathbf { T } _ { H } ( N p ) _ { \mathfrak { m } } )$

Corollary 2. In either of cases (i) or$( \mathrm { i i } ) \ \mathbf { T } _ { \mathfrak { m } }$is a Gorenstein ring.

In each case the first isomorphisms of Corollary 1 follow from the theorem together with the rank 2 result alluded to previously. Corrollary 2 and the second isomorphisms of corollory 1 then follow on applying duality (2.4). (In the proof and in all applications we will only use the notion of a Gorenstein $\mathbf { Z } _ { p } { \mathrm { - a l g e b r a } }$as defined in the appendix. For finite flat local$\mathbf { Z } _ { p } { \mathrm { - a l g e b r a s } }$the notions of Gorenstein ring and Gorenstein$\mathbf { Z } _ { p } { \mathrm { - a l g e b r a } }$are the same.) Here $\mathrm { T a } _ { \mathrm { m } } \Big ( J _ { H } ( N ) ( { \bf \overline { { Q } } } ) \Big ) \ = \ \mathrm { T a } _ { p } \Big ( J _ { H } ( N ) ( { \bf \overline { { Q } } } ) \Big ) \otimes \mathrm { { \bf T } _ { m } }$is the m-adic Tate module of $J _ { H } ( N )$

We should also point out that although Corollary 1 gives a representation from the m-adic Tate module

$$
\rho = \rho_ {\mathbf {T} _ {\mathfrak {m}}}: \operatorname{Gal} (\overline {{\mathbf {Q}}} / \mathbf {Q}) \to \operatorname{GL} _ {2} (\mathbf {T} _ {\mathfrak {m}})
$$

this can be constructed in a much more elementary way. (See [Ca3] for another argument.) For, the representation exists with$\mathbf { T } _ { \mathfrak { m } } \otimes \mathbf { Q }$replacing$\mathbf { T } _ { \mathfrak { m } }$when we use the fact that Hom$( \mathbf { Q } _ { p } / \mathbf { Z } _ { p } , \mathcal { D } ) \otimes \mathbf { Q }$was free of rank 2. A standard argument using the Eichler-Shimura relations implies that this representation$\rho ^ { \prime }$with values in$\mathrm { G L _ { 2 } } ( \mathbf { T } _ { \mathfrak { m } } \otimes \mathbf { Q } )$has the property that

$$
\text { trace } \rho^ {\prime} (\text { Frob } \ell) = T _ {\ell}, \det \rho^ {\prime} (\text { Frob } \ell) = \ell \langle \ell \rangle
$$

for all$\ell \dag \ N p$. We can normalize this representation by picking a complex conjugation c and choosing a basis such that$\rho ^ { \prime } ( c ) = \binom { 1 } { 0 } \ - 1$, and then by picking $\mathrm { ~ a ~ } \tau$for which$\rho ^ { \prime } ( \tau ) = \left( \begin{array} { c c } { { a _ { \tau } } } & { { b _ { \tau } } } \\ { { c _ { \tau } } } & { { d _ { \tau } } } \end{array} \right)$with$b _ { \tau } c _ { \tau } \not \equiv 0 ( { \mathfrak { m } } )$and by rescaling the basis so that$b _ { \tau } = 1$. (Note that the explicit description of the traces shows that if$\rho _ { \mathfrak { m } }$ is also normalized so that$\rho _ { \mathfrak { m } } ( { \boldsymbol { \hat { c } } } ) = { \binom { 1 } { 0 } } \ \ - { 0 } )$then$b _ { \rho } c _ { \tau }$mod$\mathfrak { m } =  { b _ { \tau , \mathfrak { m } } } c _ { \tau , \mathfrak { m } }$where $\begin{array} { r } { \rho _ { \mathfrak { m } } ( \tau ) = \binom { a _ { \tau , \mathfrak { m } } } { c _ { \tau , \mathfrak { m } } } \mathfrak { - } d _ { \tau , \mathfrak { m } } \ \big ) } \end{array}$. The existence of$\mathrm { ~ a ~ } \tau$such that$b _ { \tau } c _ { \tau } \not \equiv 0 ( { \mathfrak { m } } )$comes from the irreducibility of$\rho _ { \mathfrak { m } \cdot } )$With this normalization one checks that$\rho ^ { \prime }$actually takes values in the (closed) subring of$\mathbf { T } _ { \mathfrak { m } }$generated over$\mathbf { Z } _ { p }$by the traces. One can even construct the representation directly from the representations in Theorem 0.1 using this ring which is reduced. This is the method of Carayol which requires also the characterization of$\rho$by the traces and determinants (Theorem 1 of [Ca3]). One can also often interpret the$U _ { q }$operators in terms of$\rho$for$q | N$using the$\pi _ { q } \simeq \pi ( \sigma _ { q } )$theorem of Langlands (cf. [Ca1]) and the $U _ { q }$operator in case (ii) using Theorem 2.1.4 of [Wi1].

Proof (of theorem). The important technique for proving such multiplicityone results is due to Mazur and is based on the q-expansion principle in characteristic p. Since the kernel of$J _ { H } ( N ) ( { \overline { { \mathbf { Q } } } } ) \to J _ { 1 } ( N ) ( { \overline { { \mathbf { Q } } } } )$is an abelian group on which${ \mathrm { G a l } } ( { \overline { { \mathbf { Q } } } } / \mathbf { Q } )$acts through an abelian extension of Q, the intersection with ker m is trivial when$\rho _ { \mathfrak { m } }$is irreducible. So it is enough to verify the theorem for$J _ { 1 } ( N )$in part (i) (resp.$J _ { 1 } ( N p )$in part (ii)). The method for part (i) was developed by Mazur in [Ma2, Ch. II, Prop. 14.2]. It was extended to the case of$\Gamma _ { 0 } ( N )$in [Ri1, Th. 5.2] which summarizes Mazur’s argument. The case of $\Gamma _ { 1 } ( N )$is similar (cf. [E1, Th. 9.2]).

Now consider case (ii). Let$\Delta _ { ( p ) } = \{ \langle a \rangle : a \equiv 1 ( N ) \} \subseteq \Delta$. Let us first assume that$\Delta _ { ( p ) }$is nontrivial mod m, i.e., that$\delta - 1 \notin$m for some$\delta \in \Delta _ { ( p ) }$. This case is essentially covered in [Ti1] (and also in$\left[ \mathrm { G r o } \right] )$. We briefly review the argument for use later. Let$K = \mathbf Q _ { p } ( \zeta _ { p } ) , \zeta _ { p }$being a primitive$p ^ { \mathrm { t h } }$root of unity, and let$\mathcal { O }$be the ring of integers of the completion of the maximal unramified extension of$K$. Using the fact that$\Delta _ { ( p ) }$is nontrivial mod m together with Proposition 4, p. 269 of [MW1] we find that

$$
J _ {1} (N p) _ {\mathfrak {m} / \mathcal {O}} ^ {\acute {\mathrm{et}}} (\overline {{\mathbf {F}}} _ {p}) \simeq (\mathrm{Pic} ^ {0} \Sigma_ {1} ^ {\acute {\mathrm{et}}} \times \mathrm{Pic} ^ {0} \Sigma_ {1} ^ {\mu}) _ {\mathfrak {m}} (\overline {{\mathbf {F}}} _ {p})
$$

where the notation is taken from [MW1] loc. cit. Here$\Sigma _ { 1 } ^ { \mathrm { e t } }$and$\Sigma _ { 1 } ^ { \mu }$are the two smooth irreducible components of the special fibre of the canonical model of$X _ { 1 } ( N p ) _ { / \mathcal { O } }$described in [MW1, Ch. 2]. (The smoothness in this case was proved in [DR].) Also$J _ { 1 } ( N p ) _ { \mathrm { m } / \mathcal { O } } ^ { \mathrm { e t } }$denotes the canonical ´etale quotient of the m-divisible group over O. This makes sense because$J _ { 1 } ( N p ) _ { \mathfrak { m } }$does extend to a p-divisible group over O (again by a theorem of Deligne and Rapoport [DR] and because$\Delta _ { ( p ) }$is nontrivial mod m). It is ordinary as follows from (2.2) when we use the main theorem of Tate$\mathrm { ( [ T a ] ) }$since$\mathcal { D } ^ { 0 }$and$\mathcal { D } ^ { E }$clearly correspond to ordinary p-divisible groups.

Now the q-expansion principle implies that dim$_ { \overline { { \mathbf { F } } } _ { p } } X [ \mathfrak { m ^ { \prime } } ] \leq 1$where

$$
X = \{H ^ {0} (\Sigma_ {1} ^ {\mu}, \Omega^ {1}) \oplus H ^ {0} (\Sigma_ {1} ^ {\acute {\mathrm{et}}}, \Omega^ {1}) \}
$$

and${ \mathfrak { m } } ^ { \prime }$is defined by embedding$\mathbf { T } / \mathfrak { m } \hookrightarrow \overline { { \mathbf { F } } } _ { p }$and setting${ \mathfrak { m } } ^ { \prime } = \ker : \mathbf { T } \otimes { \overline { { \mathbf { F } } } } _ { p }  { \overline { { \mathbf { F } } } } _ { p }$ under the map$t \otimes a \mapsto a t$mod m. Also T acts on$\mathrm { P i c } ^ { 0 } \Sigma _ { 1 } ^ { \mu } \times \mathrm { P i c } ^ { 0 } \bar { \Sigma } _ { 1 } ^ { \acute { \mathrm { e t } } }$, the abelian variety part of the closed fibre of the Neron model of$J _ { 1 } ( N p ) _ { / \mathcal { O } }$, and hence also on its cotangent space$X$. (For a proof that$X [ \mathfrak { m } ^ { \prime } ]$is at most onedimensional, which is readily adapted to this case, see Lemma 2.2 below. For similar versions in slightly simpler contexts see [Wi3, §6] or [Gro, §12]. Then the Cartier map induces an injection 9cf. Prop. 6.5 of [Wi3])

$$
\delta : \{\mathrm{Pic} ^ {0} \Sigma_ {1} ^ {\mu} \times \mathrm{Pic} ^ {0} \Sigma_ {1} ^ {\acute {\mathrm{et}}} \} [ p ] (\overline {{\mathbf {F}}} _ {p}) \underset {\mathbf {F} _ {p}} {\otimes} \overline {{\mathbf {F}}} _ {p} \hookrightarrow X.
$$

The composite$\delta \circ w _ { \zeta }$can be checked to be Hecke invariant (cf. Prop. 6.5 of [Wi3]. In checking the compatibility for$U _ { p }$use the formulas of Theorem 5.3 of [Wi3] but note the correction in [MW1, p. 188].) It follows that

$$
J _ {1} (N p) _ {\mathfrak {m} / \mathcal {O}} (\overline {{\mathbf {F}}} _ {p}) [ \mathfrak {m} ] \simeq \mathbf {T} / \mathfrak {m}
$$

as a T-module.This shows that if$\hat { H }$is the Pontrjagin dual of $H = J _ { 1 } ( N p ) _ { \mathfrak { m } / \mathcal { O } } ( \overline { { \mathbf { F } } } _ { p } )$then$\hat { H } \simeq  { \mathbf { T } } _ { \mathfrak { m } }$since$\hat { H } / { \mathfrak { m } } \simeq \mathbf { T } / { \mathfrak { m } }$. Thus

$$
J _ {1} (N p) _ {\mathfrak {m} / \mathcal {O}} (\overline {{\mathbf {F}}} _ {p}) [ p ] \xrightarrow {\sim} \mathrm{Hom} (\mathbf {T} _ {\mathfrak {m}} / p, \mathbf {Z} / p \mathbf {Z}).
$$

Now our assumption that m is$D _ { p }$-distinguished enables us to identify

$$
\mathcal {D} ^ {0} = J _ {1} (N p) _ {\mathfrak {m} / \mathcal {O}} ^ {0} (\overline {{\mathbf {Q}}} _ {p}), \mathcal {D} ^ {E} = J _ {1} (N p) _ {\mathfrak {m} / \mathcal {O}} ^ {\acute {\mathrm{et}}} (\overline {{\mathbf {Q}}} _ {p}).
$$

For the groups on the right are unramified and those on the left are dual to groups where inertia acts via a character of finite order (duality with respect to Hom$( { \bf \Delta } , { \bf Q } _ { p } / { \bf Z } _ { p } ( 1 ) ) )$. So

$$
\mathcal {D} ^ {0} [ p ] \stackrel {\sim} {\to} \mathbf {T} _ {\mathfrak {m}} / p, \mathcal {D} ^ {E} [ p ] \stackrel {\sim} {\to} \mathrm{Hom} (\mathbf {T} _ {\mathfrak {m}} / p, \mathbf {Z} / p \mathbf {Z})
$$

as$\mathbf { T } _ { \mathrm { m } } { \mathrm { - m o d u l e s } } .$, the former following from the latter when we use duality under the pairing [ , ]. In particular as m is$D _ { p }$-distinguished,

$$
\mathcal {D} [ p ] \simeq \mathbf {T} _ {\mathfrak {m}} / p \oplus \operatorname{Hom} (\mathbf {T} _ {\mathfrak {m}} / p, \mathbf {Z} / p \mathbf {Z}).\tag{2.4}
$$

We now use an argument of Tilouine [Ti1]. We pick a complex conjugation $\tau$. This has distinct eigenvalues ±1 on$\ ] \rho _ { \mathfrak { m } }$so we may decompose$\mathcal { D } [ \boldsymbol { p } ]$into eigenspaces for τ :

$$
\mathcal {D} [ p ] = \mathcal {D} [ p ] ^ {+} \oplus \mathcal {D} [ p ] ^ {-}.
$$

Since$\mathbf { T } _ { \mathfrak { m } } / p$and Hom$( \mathbf { T } _ { \mathfrak { m } } / p , \mathbf { Z } / p \mathbf { Z } )$are both indecomposable Hecke-modules, by the Krull-Schmidt theorem this decomposition has factors which are isomorphic to those in (2.4) up to order. So in the decomposition

$$
\mathcal {D} [ \mathfrak {m} ] = \mathcal {D} [ \mathfrak {m} ] ^ {+} \oplus \mathcal {D} [ \mathfrak {m} ] ^ {-}
$$

one of the eigenspaces is isomorphic to$\mathbf { T } _ { \mathfrak { m } }$and the other to$( \mathbf { T } _ { \mathfrak { m } } / p ) [ \mathfrak { m } ]$. But since$\rho _ { \mathfrak { m } }$is irreducible it is easy to see by considering$\mathcal { D } [ \mathfrak { m } ] \oplus \mathrm { H o m } ( \mathcal { D } [ \mathfrak { m } ] , \operatorname* { d e t } \rho _ { \mathfrak { m } } )$ that τ has the same number of eigenvalues equal to +1 as equal to −1 in${ \mathcal { D } } [ { \mathfrak { m } } ]$2 whence #$( \mathbf { T } _ { \mathfrak { m } } / p ) [ \mathfrak { m } ] = \# ( \mathbf { T } / \mathfrak { m } )$. This shows that${ \mathcal { D } } [ { \mathfrak { m } } ] ^ { + } { \overset { \sim } { \to } } { \mathcal { D } } [ { \mathfrak { m } } ] ^ { - } \simeq \mathbf { T } / { \mathfrak { m } }$as required.

Now we consider the case where$\Delta _ { ( p ) }$is trivial mod m. This case was treated (but only for the group$\Gamma _ { 0 } ( N p )$and$\rho _ { \mathfrak { m } } \ \mathrm { \sim } \mathfrak { n } \mathrm { e w } ^ { \mathrm { ? } }$at$p -$the crucial restriction being the last one) in [M Ri]. Let$X _ { 1 } ( \boldsymbol { N } , \boldsymbol { p } ) _ { / \mathbf { Q } }$be the modular curve corresponding to$\Gamma _ { 1 } ( N ) \cap \Gamma _ { 0 } ( p )$and let$J _ { 1 } ( N , p )$be its Jacobian. Then since the composite of natural maps$J _ { 1 } ( N , p )  J _ { 1 } ( N p )  J _ { 1 } ( N , p )$is multiplication by an integer prime to$p$and since$\Delta _ { ( p ) }$is trivial mod m we see that

$$
J _ {1} (N, p) _ {\mathfrak {m}} (\overline {{\mathbf {Q}}}) \simeq J _ {1} (N p) _ {\mathfrak {m}} (\overline {{\mathbf {Q}}}).
$$

It will be enough then to use$J _ { 1 } ( N , p )$, and the corresponding ring T and ideal m.

The curve$X _ { 1 } ( N , p )$has a canonical model$X _ { 1 } ( N , p ) _ { / \mathbf { Z } _ { \boldsymbol { \varepsilon } } }$which over$\overline { { \mathbf { F } } } _ { p }$ consists of two smooth curves$\Sigma ^ { \mathrm { { e t } } }$and$\Sigma ^ { \mu }$intersecting transversally at the supersingular points (again this is a theorem of Deligne and Rapoport; cf. [DR, Ch. 6, Th. 6.9], [KM] or [MW1] for more details). We will use the models described in [MW1, Ch. II] and in particular the cusp ∞ will lie on$\Sigma ^ { \mu }$. Let Ω denote the sheaf of regular diferentials on$X _ { 1 } ( \boldsymbol { N } , \boldsymbol { p } ) _ { / \mathbf { F } _ { p } }$(cf. [DR, Ch. 1 §2], [M Ri, §7]). Over${ \overline { { \mathbf { F } } } } _ { p } .$, since$X _ { 1 } ( { \cal N } , p ) _ { / \overline { { \mathbf { F } } } _ { p } }$has ordinary double point singularities, the diferentials may be identified with the meromorphic diferentials on the normalization${ \cal X } _ { 1 } \bar { ( } N , p ) _ { / \overline { { { \bf F } } } _ { p } } = \Sigma ^ { \acute { \mathrm { e t } } } \cup \Sigma ^ { \mu }$which have at most simple poles at the supersingular points (the intersection points of the two components) and satisfy $\mathrm { r e s } _ { x _ { 1 } } + \mathrm { r e s } _ { x _ { 2 } } = 0 { \mathrm { ~ i f ~ } } x _ { 1 }$and$x _ { 2 }$are the two points above such a supersingular point. We need the following lemma:

$$
\text { LEMMA   2.2. } \dim_ {\mathbf {T} / \mathfrak {m}} H ^ {0} (X _ {1} (N, p) _ {/ \mathbf {F} _ {p}}, \Omega) [ \mathfrak {m} ] = 1.
$$

Proof. First we remark that the action of the Hecke operator$U _ { p }$here is most conveniently defined using an extension from characteristic zero. This is explained below. We will first show that$\dim _ { \mathbf { T } / \mathfrak { m } } H ^ { 0 } ( X _ { 1 } ( N , p ) _ { / \mathbf { F } _ { p } } , \Omega ) [ \mathfrak { m } ] \leq 1$ this being the essential step. If we embed${ \bf T } / \mathfrak { m } \ \hookrightarrow \ \overline { { \mathbf { F } } } _ { p }$and then set ${ \mathfrak { m } } ^ { \prime } = \ker : \mathbf { T } \otimes { \overline { { \mathbf { F } } } } _ { p } \to { \overline { { \mathbf { F } } } } _ { p }$(the map given by$t \otimes a \mapsto$at mod m) then it is $H ^ { 0 } ( X _ { 1 } ( N , p ) _ { / \overline { { \mathbf { F } } } _ { p } } , \Omega ) [ \mathfrak { m } ^ { \prime } ] \leq 1$. First we will suppose that there is no nonzero holomorphic diferential in$H ^ { 0 } ( X _ { 1 } ( N , p ) _ { / \overline { { { \bf F } } } _ { n } } , \Omega ) [ { \mathfrak { m } } ^ { \prime } ]$• $\mathrm { i . e . } .$, no diferential form which pulls back to holomorphic diferentials on$\Sigma ^ { \mathrm { e t } }$ and$\Sigma ^ { \mu }$. Then if$\omega _ { 1 }$and$\omega _ { 2 }$are two diferentials in$\mathsf { \bar { H } } ^ { 0 } ( X _ { 1 } ( N , p ) _ { / \overline { { \mathbf { F } } } _ { p } } , \Omega ) [ \mathfrak { m } ^ { \prime } ]$• the q-expansion principle shows that$\mu \omega _ { 1 } - \lambda \omega _ { 2 }$has zero q-expansion at ∞ for some pair$( \mu , \lambda ) \neq ( 0 , 0 )$in$\overline { { \mathbf { F } } } _ { p } ^ { 2 }$and thus is zero on$\Sigma ^ { \mu }$. As$\mu \omega _ { 1 } - \lambda \omega _ { 2 } = 0$on $\Sigma ^ { \mu }$it is holomorphic on$\Sigma ^ { \mathrm { { e t } } }$. By our hypothesis it would then be zero which shows that$\omega _ { 1 }$and$\omega _ { 2 }$are linearly dependent.

This use of the q-expansion principle in characteristic$p$is crucial and due to Mazur [Ma2]. The point is simply that all the coeficients in the q-expansion are determined by elementary formulae from the coeficient of$q$provided that $\omega$is an eigenform for all the Hecke operators. The formulae for the action of these operators in characteristic$p$follow from the formulae in characteristic zero. To see this formally (especially for the$U _ { p }$operator) one checks first that$H ^ { 0 } ( X _ { 1 } ( N , p ) _ { / \mathbf { Z } _ { p } } , \Omega )$, where Ω denotes the sheaf of regular diferentials on $X _ { 1 } ( N , p ) _ { / \mathbf { Z } _ { p } }$, behaves well under the base changes$\mathbf { Z } _ { p } \to { \overline { { \mathbf { Z } } } } _ { p }$and$\mathbf { Z } _ { p }  \mathbf { \overline { { Q } } } _ { p } ;$ cf. [Ma2, §II.3] or [Wi3, Prop. 6.1]. The action of the Hecke operators on $J _ { 1 } ( N , p )$induces an action on the connected component of the Neron model of $J _ { 1 } ( N , p ) _ { / \mathbf { Q } _ { p } } \mathrm { ~ ; ~ }$, so also on its tangent space and cotangent space. By Grothendieck duality the cotangent space is isomorphic to$H ^ { 0 } ( X _ { 1 } ( N , p ) _ { / \mathbf { Z } _ { p } } , \Omega )$; see (2.5) below. (For a summary of the duality statements used in this context, see [Ma2, §II.3]. For explicit duality over fields see [AK, Ch. VIII].) This then defines an action of the Hecke operators on this group. To check that over$\overline { { \mathbf { Q } } } _ { p }$ this gives the standard action one uses the commutativity of the diagram after Proposition 2.2 in [Mi1].

Now assume that there is a nonzero holomorphic diferential in

$$
H ^ {0} (X _ {1} (N, p) _ {/ \overline {{\mathbf {F}}} _ {p}}, \Omega) [ \mathfrak {m} ^ {\prime} ].
$$

We claim that the space of holomorphic diferentials then has dimension 1 and that any such diferential$\omega \neq 0$is actually nonzero on$\Sigma ^ { \mu }$. The dimension claim follows from the second assertion by using the q-expansion principle. To prove that$\omega \neq 0$on$\Sigma ^ { \mu }$we use the formula

$$
U _ {p *} (x, y) = (F x, y ^ {\prime})
$$

for$( x , y ) \in ( \mathrm { P i c } ^ { 0 } \Sigma ^ { \ ' \in } \times \mathrm { P i c } ^ { 0 } \Sigma ^ { \mu } ) ( \overline { { \mathbf { F } } } _ { p } )$, where$F$denotes the Frobenius endomorphism. The value of$y ^ { \prime }$will not be needed. This formula is a variant on the second part of Theorem 5.3 of [Wi3] where the corresponding result is proved for$X _ { 1 } ( N p )$. (A correction to the first part of Theorem 5.3 was noted in [MW1, p. 188].) One check then that the action of$U _ { p }$on ${ \cal X } _ { 0 } = H ^ { 0 } ( \Sigma ^ { \mu } , \bar { \Omega } ^ { 1 } ) \oplus H ^ { 0 } ( \Sigma ^ { \dot { \mathrm { e t } } } , \Sigma ^ { 1 } )$viewed as a subspace of$H ^ { 0 } ( X _ { 1 } ( N , p ) _ { / \overline { { \mathbf { F } } } _ { p } } , \Omega )$ is the same as the action on$X _ { 0 }$viewed as the cotangent space of$\mathrm { P i c } ^ { 0 } \Sigma ^ { \mu } \times$ $\mathrm { P i c } ^ { 0 } \Sigma ^ { \ ' \mathrm { e t } }$. From this we see that if$\omega = 0$on$\Sigma ^ { \mu }$then$U _ { p ^ { \omega } } = 0 ~ \mathrm { o n } ~ \Sigma ^ { \ ' \mathrm { e t } }$. But$U _ { p }$ acts as a nonzero scalar which gives a contradiction if$\omega \neq 0$. We can thus assume that the space of m<sup></sup>-torsion holomorphic diferentials has dimension 1 and is generated by ω. So if$\omega _ { 2 }$is now any diferential in$H ^ { 0 } ( X _ { 1 } ( N , p ) _ { / \overline { { \mathbf { F } } } _ { p } } , \Omega ) [ \mathfrak { m } ^ { \prime } ]$ then$\omega _ { 2 } - \lambda \omega$has zero q-expansion at ∞ for some choice of λ. Then$\omega _ { 2 } - \lambda \omega = 0$ on$\Sigma ^ { \mu }$whence$\omega _ { 2 } -$λω is holomorphic and so$\omega _ { 2 } = \lambda \omega$. We have now shown in general that dim$\big ( H ^ { 0 } ( X _ { 1 } ( N , p ) _ { / \overline { { \mathbf { F } } } _ { n } } , \Omega ) [ \mathfrak { m } ^ { \prime } ] \big ) \leq 1$

The singularities of$X _ { 1 } ( N , p ) _ { / \mathbf { Z } _ { p } }$at the supersingular points are formally isomorphic over$\widehat { \mathbf { Z } _ { p } ^ { \mathrm { u n r } } }$to$\widehat { \mathbf { Z } _ { p } ^ { \mathrm { u n r } } } [ [ X , Y ] ] / ( X Y - p ^ { k } )$with k = 1, 2 or 3 [cf. [DR, Ch. 6, Th. 6.9]). If we consider a minimal regular resolution$M _ { 1 } ( N , p ) _ { / { \bf Z } _ { p } }$ then$H ^ { 0 } ( M _ { 1 } ( N , p ) _ { / { \bf F } _ { p } } , \Omega ) \simeq H ^ { 0 } ( X _ { 1 } ( N , p ) _ { / { \bf F } _ { p } } , \Omega )$(see the argument in [Ma2, Prop. 3.4]), and a similar isomorphism holds for$H ^ { 0 } ( M _ { 1 } ( N , p ) _ { / { \bf Z } _ { v } } , \Omega )$

As$M _ { 1 } ( N , p ) _ { / { \bf Z } _ { p } }$is regular, a theorem of Raynaud [Ray2] says that the connected component of the Neron model of$J _ { 1 } ( N , p ) _ { / \mathbf { Q } _ { p } }$is$J _ { 1 } ( N , p ) _ { / { \bf Z } _ { p } } ^ { 0 } \ \simeq$ $\mathrm { P i c } ^ { 0 } ( M _ { 1 } ( N , p ) _ { / { \bf Z } _ { p } } )$. Taking tangent spaces at the origin, we obtain

$$
\mathrm{Tan} (J _ {1} (N, p) _ {/ \mathbf {Z} _ {p}} ^ {0}) \simeq H ^ {1} (M _ {1} (N, p) _ {/ \mathbf {Z} _ {p}}, \mathcal {O} _ {M _ {1} (N, p)}).\tag{2.5}
$$

Reducing both sides mod p and applying Grothendieck duality we get an isomorphism

$$
\mathrm{Tan} (J _ {1} (N, p) _ {/ \mathbf {F} _ {p}} ^ {0}) \xrightarrow {\sim} \mathrm{Hom} (H ^ {0} (X _ {1} (N, p) _ {/ \mathbf {F} _ {p}}, \Omega), \mathbf {F} _ {p}).\tag{2.6}
$$

(To justify the reduction in detail see the arguments in [Ma2, §II. 3]). Since Tan$( J _ { 1 } ( N , p ) _ { / { \bf Z } _ { p } } ^ { 0 } )$is a faithful$\mathbf { T } \otimes \mathbf { Z } _ { p }$-module it follows that

$$
H ^ {0} (X _ {1} (N, p) _ {/ \mathbf {F} _ {p}}, \Omega) [ \mathfrak {m} ]
$$

is nonzero. This completes the proof of the lemma.

To complete the proof of the theorem we choose an abelian subvariety $A$of$J _ { 1 } ( N , p )$with multiplicative reduction at p. Specifically let A be the connected part of the kernel of$J _ { 1 } ( N , p )  J _ { 1 } ( N ) \times J _ { 1 } ( N )$under the natural map$\hat { \varphi }$described in Section 2 (see (2.10)). Then we have an exact sequence

$$
0 \to A \to J _ {1} (N, p) \to B \to 0
$$

and$J _ { 1 } ( N , p )$has semistable reduction over$\mathbf { Q } _ { p }$and B has good reduction. By Proposition 1.3 of [Ma3] the corresponding sequence of connected group schemes

$$
0 \to A [ p ] _ {/ \mathbf {Z} _ {p}} ^ {0} \to J _ {1} (N, p) [ p ] _ {/ \mathbf {Z} _ {p}} ^ {0} \to B [ p ] _ {/ \mathbf {Z} _ {p}} ^ {0} \to 0
$$

is also exact, and by Corollary 1.1 of the same proposition the corresponding sequence of tangent spaces of Neron models is exact. Using this we may check that the natural map

$$
\mathrm{Tan} (J _ {1} (N, p) [ p ] _ {/ \overline {{\mathbf {F}}} _ {p}} ^ {t}) \underset {\mathbf {T} _ {p}} {\otimes} \mathbf {T} _ {\mathfrak {m}} \to \mathrm{Tan} (J _ {1} (N, p) _ {/ \overline {{\mathbf {F}}} _ {p}}) \underset {\mathbf {T} _ {p}} {\otimes} \mathbf {T} _ {\mathfrak {m}}\tag{2.7}
$$

is an isomorphism, where t denotes the maximal multiplicative-type subgroup scheme (cf. [Ma3, §1]). For it is enough to check such a relation on A and B separately and on B it is true because the m-divisible group is ordinary. This follows from (2.2) by the theorem of Tate [Ta] as before.

Now (2.6) together with the lemma shows that

$$
\operatorname{Tan} (J _ {1} (N, p)) / \mathbf {z} _ {p} \underset {\mathbf {T} _ {p}} {\otimes} \mathbf {T} _ {\mathfrak {m}} \simeq \mathbf {T} _ {\mathfrak {m}}.
$$

We claim that (2.7) together with this implies that as$\mathbf { T } _ { \mathfrak { m } } .$-modules

$$
V := J _ {1} (N, p) [ p ] ^ {t} (\overline {{\mathbf {Q}}} _ {p}) _ {\mathfrak {m}} \simeq (\mathbf {T} _ {\mathfrak {m}} / p).
$$

To see this it is suficient to exhibit an isomorphism of${ \overline { { \mathbf { F } } } } _ { p } .$-vector spaces

$$
\mathrm{Tan} (G _ {/ \overline {{\mathbf {F}}} _ {p}}) \simeq G (\overline {{\mathbf {Q}}} _ {p}) \underset {\mathbf {F} _ {p}} {\otimes} \overline {{\mathbf {F}}} _ {p}\tag{2.8}
$$

for any multiplicative-type group scheme (finite and flat)$G _ { / \mathbf { Z } _ { \tau } }$which is killed by p and moreover to give such an isomorphism that respects the action of endomorphism of$G _ { / \mathbf { Z } _ { p } }$. To obtain such an isomorphism observe that we have isomorphisms

$$
\begin{array}{c} \operatorname{Hom} _ {\overline {{\mathbf {Q}}} _ {p}} (\boldsymbol {\mu} _ {p}, G) \underset {\mathbf {F} _ {p}} {\otimes} \overline {{\mathbf {F}}} _ {p} \simeq \operatorname{Hom} _ {\overline {{\mathbf {F}}} _ {p}} (\boldsymbol {\mu} _ {p}, G) \underset {\mathbf {F} _ {p}} {\otimes} \overline {{\mathbf {F}}} _ {p} \\ \simeq \operatorname{Hom} \Bigl (\operatorname{Tan} (\boldsymbol {\mu} _ {p / \overline {{\mathbf {F}}} _ {p}}), \operatorname{Tan} (G / \overline {{\mathbf {F}}} _ {p}) \Bigr) \end{array}\tag{2.9}
$$

where Hom denotes homomorphisms of the group schemes viewed over$\overline { { \mathbf { Q } } } _ { p }$ and similarly for$\operatorname { H o m } _ { \overline { { \mathbf { F } } } _ { p } }$. The second isomorphism can be checked by reducing to the case$G = \mu _ { p }$. Now picking a primitive$p ^ { \mathrm { t h } }$root of unity we can identify the left-hand term in (2.9) with$G ( \overline { { \mathbf { Q } } } _ { p } ) \otimes _ { \mathbf { F } _ { p } } \overline { { \mathbf { F } } } _ { p } .$. Picking an isomorphism of Tan$( \mu _ { p / \overline { { \mathbf { F } } } _ { p } } )$with${ \overline { { \mathbf { F } } } } _ { p }$we can identify the last term in (2.9) with Tan$\left( G _ { / \overline { { \mathbf { F } } } _ { p } } \right)$ Thus after these choices are made we have an isomorphism in (2.8) which respects the action of endomorphisms of G.

On the other hand the action of$\operatorname { G a l } ( { \overline { { \mathbf { Q } } } } _ { p } / \mathbf { Q } _ { p } )$on V is ramified on every subquotient, so$V \subseteq { \mathcal { D } } ^ { 0 } [ p ]$. (Note that our assumption that$\Delta _ { ( p ) }$is trivial mod m implies that the action on$\mathcal { D } ^ { 0 } [ p ]$is ramified on every subquotient and on$\mathcal { D } ^ { E } [ { p } ]$is unramified on every subquotient.) By again examining A and B separately we see that in fact${ \cal V } = { \cal D } ^ { 0 } [ p ]$. For A we note that$A [ p ] / A [ p ] ^ { t }$is unramified because it is dual to${ \hat { A } } [ p ] ^ { t }$where A<sup>ˆ</sup> is the dual abelian variety. We can now proceed as we did in the case where$\Delta _ { ( p ) }$was nontrivial mod m. 

## 2. Congruences between Hecke rings

Suppose that q is a prime not dividing N. Let$\Gamma _ { 1 } ( N , q ) = \Gamma _ { 1 } ( N ) \cap \Gamma _ { 0 } ( q )$ and let$X _ { 1 } ( N , q ) = X _ { 1 } ( N , q ) _ { / { \bf q } }$be the corresponding curve. The two natural maps$X _ { 1 } ( N , q )  X _ { 1 } ( N )$induced by the maps$z \ \longrightarrow \ z$and$z  q z$on the upper half plane permit us to define a map$J _ { 1 } ( N ) \times J _ { 1 } ( N ) \to J _ { 1 } ( N , q )$. Using a theorem of Ihara, Ribet shows that this map is injective (cf. [Ri2, Cor. 4.2]). Thus we can define$\varphi$by

$$
0 \to J _ {1} (N) \times J _ {1} (N) \stackrel {\varphi} {\longrightarrow} J _ {1} (N, q).\tag{2.10}
$$

Dualizing, we define B by

$$
0 \to B \stackrel {\psi} {\longrightarrow} J _ {1} (N, q) \stackrel {\hat {\varphi}} {\longrightarrow} J _ {1} (N) \times J _ {1} (N) \to 0.
$$

Let${ \bf T } _ { 1 } ( N , q )$be the ring of endomorphisms of$J _ { 1 } ( N , q )$generated by the standard Hecke operators$\{ T _ { l * }$for$l ~ \dag ~ N q , U _ { l * }$for$l | N q , \langle a \rangle ~ = ~ \langle a \rangle$∗for $( a , N q ) = 1 \}$. One can check that$U _ { p }$preserves B either by an explicit calculation or by noting that B is the maximal abelian subvariety of$J _ { 1 } ( N , q )$with multiplicative reduction at$q .$We set$J _ { 2 } = J _ { 1 } ( N ) \times J _ { 1 } ( N )$

More generally, one can consider$J _ { H } ( N )$and$J _ { H } ( N , q )$in place of$J _ { 1 } ( N )$ and$J _ { 1 } ( N , q )$(where$J _ { H } ( N , q )$corresponds to$X _ { 1 } ( N , q ) / H )$and we write${ \bf T } _ { H } ( N )$ and${ \bf T } _ { H } ( N , q )$for the associated Hecke rings. In this case the corresponding map$\varphi$may have a kernel. However since the kernel of$J _ { H } ( N ) \to J _ { 1 } ( N )$does not meet ker m for any maximal ideal m whose associated$\rho _ { \mathfrak { m } }$is irreducible, the above sequence remain exact if we restrict to$\mathfrak { m } ^ { ( q ) }$-divisible groups,$\mathfrak { m } ^ { ( q ) }$ being the maximal ideal associated to m of the ring$\mathbf { T } _ { H } ^ { ( q ) } ( N , q )$generated by the standard Hecke operators but ommitting$U _ { q }$. With this minor modification the proofs of the results below for$H \neq 1$follow from the cases of full level. We will use the same notation in the general case. Thus$\varphi$is the map $J _ { 2 } = J _ { H } ( N ) ^ { 2 }  J _ { H } ( N , q )$induced by$z  z { \mathrm { ~ a n d ~ } } z  q z$on the two factors, and$B = \ker \hat { \varphi }$. (B will not be an abelian variety in general.)

The following lemma is a straightforward generalization of a lemma of Ribet ([Ri2]). Let$n _ { q }$be an integer satisfying$\begin{array} { r } { n _ { q } \equiv q ( N ) } \end{array}$and$n _ { q } \equiv 1 ( q )$, and write$\langle q \rangle = \langle n _ { q } \rangle \in \dot { \mathbf { T } } _ { H } ( N q )$

Lemma 2.3 (Ribet).$\psi ( B ) \cap \varphi ( J _ { 2 } ) _ { \mathfrak { m } ^ { ( q ) } } = \varphi ( J _ { 2 } ) [ U _ { q } ^ { 2 } - \langle q \rangle ] _ { \mathfrak { m } ^ { ( q ) } }$for irreducible$\rho _ { \mathfrak { m } }$

Proof. The left-hand side is$( \mathrm { i m } \varphi \cap$ker$\hat { \varphi } )$, so we compute$\varphi ^ { - 1 } ( \mathrm { i m } \varphi \cap$ ker$\hat { \varphi } ) = \ker ( \hat { \varphi } \circ \varphi )$

An explicit calculation shows that

$$
\hat {\varphi} \circ \varphi = \left[ \begin{array}{c c} q + 1 & T _ {q} \\ T _ {q} ^ {*} & q + 1 \end{array} \right] \text {on} J _ {2}
$$

where$T _ { q } ^ { * } = T _ { q } \cdot \langle q \rangle ^ { - 1 }$. The matrix action here is on the left. We also find that on$J _ { 2 }$

$$
U _ {q} \circ \varphi = \varphi \circ \left[ \begin{array}{c c} 0 & - \langle q \rangle \\ q & T _ {q} \end{array} \right],\tag{2.11}
$$

whence

$$
(U _ {q} ^ {2} - \langle q \rangle) \circ \varphi = \varphi \circ \left[ \begin{array}{c c} - \langle q \rangle & 0 \\ T _ {q} & - \langle q \rangle \end{array} \right] \circ (\hat {\varphi} \circ \varphi).
$$

Now suppose that m is a maximal ideal of$\mathbf { T } _ { H } ( N ) , p \in \mathfrak { m }$and$\rho _ { \mathfrak { m } }$is irreducible. We will now give a slightly stronger result than that given in the lemma in the special case$q = p .$. (The case$q \neq p$we will also strengthen but we will do this separately.) Assume the that$p \nmid N$and$T _ { p } \notin \mathfrak { m }$. Let$a _ { p }$be the unit root of$x ^ { 2 } - T _ { p } x + p \langle p \rangle = 0$in$\mathbf { T } _ { H } ( N ) _ { \mathfrak { m } }$. We first define a maximal ideal${ \mathfrak { m } } _ { p }$of${ \bf T } _ { H } ( N , p )$with the same associated representation as m. To do this consider the ring

$$
S _ {1} = \mathbf {T} _ {H} (N) [ U _ {1} ] / (U _ {1} ^ {2} - T _ {p} U _ {1} + p \langle p \rangle) \subseteq \operatorname{End} (J _ {H} (N) ^ {2})
$$

where$U _ { 1 }$is the endomorphism of$J _ { H } ( N ) ^ { 2 }$given by the matrix

$$
\left[ \begin{array}{c c} T _ {p} & - \langle p \rangle \\ p & 0 \end{array} \right].
$$

It is thus compatible with the action of$U _ { p }$on$J _ { H } ( N , p )$when compared using $\hat { \varphi } .$. Now$\mathfrak { m } _ { 1 } = ( \mathfrak { m } , U _ { 1 } - \widetilde { a _ { p } } )$is a maximal ideal of$S _ { 1 }$where$\widetilde { a _ { p } }$is any element of${ \bf T } _ { H } ( N )$representing the class$\bar { a } _ { p } \in \mathbf { T } _ { H } ( N ) _ { \mathfrak { m } } / { \mathfrak { m } } \simeq \mathbf { T } _ { H } ( \dot { N } ) / { \mathfrak { m } }$. Moreover $S _ { 1 , \mathfrak { m } _ { 1 } } \simeq \mathbf { T } _ { H } ( N ) _ { \mathfrak { m } }$and we let${ \mathfrak { m } } _ { p }$be the inverse image of m<sub>1</sub> in${ \bf T } _ { H } ( N , p )$under the natural map${ \bf T } _ { H } ( N , p )  { \bar { S } } _ { 1 }$. One checks that${ \mathfrak { m } } _ { p }$id D<sub>p</sub>-distinguished. For any standard Hecke operator t except$U _ { p } \ ( { \mathrm { i . e . , } } \ t = T _ { l } , U _ { q ^ { \prime } }$for$q ^ { \prime } \ne p \ \mathrm { o r } \ \langle a \rangle )$the image of t is t. The image of$U _ { p }$is$U _ { 1 }$

We need to check that the induced map

$$
\alpha : \mathbf {T} _ {H} (N, p) _ {\mathfrak {m} _ {p}} \longrightarrow S _ {1, \mathfrak {m} _ {1}} \simeq \mathbf {T} _ {H} (N) _ {\mathfrak {m}}
$$

is surjective. The only problem is to show that$T _ { p }$is in the image. In the present context one can prove this using the surjectivity of$\hat { \varphi }$in (2.12) and using the fact that the Tate-modules in the range and domain of$\hat { \varphi }$are free of rank 2 by Corollary 1 to Theorem 2.1. The result then follows from Nakayama’s lemma as one deduces easily that$\mathbf { T } _ { H } ( N ) _ { \mathfrak { m } }$is a cyclic$\mathbf { T } _ { H } ( N , p ) _ { \mathfrak { m } _ { \xi } }$-module. This argument was suggested by Diamond. A second argument using representations can be found at the end of Proposition 2.15. We will now give a third and more direct proof due to Ribet (cf. [Ri4, Prop. 2]) but found independently and shown to us by Diamond.

For the following lemma we let$\mathbf { T } ^ { M }$, for an integer M, denote the subring of End$\Big ( S _ { 2 } ( \Gamma _ { 1 } ( N ) ) \Big )$generated by the Hecke operators$T _ { n }$for positive integers n relatively prime to M. Here$S _ { 2 } \Big ( \Gamma _ { 1 } ( N ) \Big )$denotes the vector space of weight 2 cusp forms on$\Gamma _ { 1 } ( N )$. Write T for$\mathbf { T } ^ { 1 }$. It will be enough to show that$T _ { p }$is a redundant operator in$\mathbf { T } ^ { 1 }$, i.e., that$\mathbf { T } ^ { p } = \mathbf { T }$. The result for$\mathbf { T } _ { H } ( N ) _ { \mathfrak { m } }$then follows.

Lemma (Ribet). Suppose that$( M , N ) = 1$. If M is odd then$\mathbf { T } ^ { M } = \mathbf { T }$ If M is even then$\dot { \mathbf { T } } ^ { M }$has finite index in T equal to a power of 2.

As the rings are finitely generated free Z-modules, it sufices to prove that $\mathbf { T } ^ { M } \otimes \mathbf { F } _ { l }  \mathbf { T } \otimes \mathbf { F } _ { l }$is surjective unless l and M are both even. The claim follows from

1.$\mathbf { T } ^ { M } \otimes \mathbf { F } _ { l }  \mathbf { T } ^ { M / p } \otimes \mathbf { F } _ { l }$is surjective if$p | M$and$p \nmid l N$

2.$\mathbf { T } ^ { l } \otimes \mathbf { F } _ { l }  \mathbf { T } \otimes \mathbf { F } _ { l }$is surjective if$l \dag 2 N$

Proof of 1. Let A denote the Tate module$\mathrm { T a } _ { l } ( J _ { 1 } ( N ) )$. Then$R = \mathbf { T } ^ { M / p } \otimes$ $\mathbf { Z } _ { l }$acts faithfully on A. Let$R ^ { \prime } = ( R _ { \mathbf { Z } _ { l } } \mathbf { Q } _ { l } ) \cap \mathrm { E n d } _ { \mathbf { Z } _ { l } } A$and choose d so that $l ^ { d } R ^ { \prime } \subset l R$. Consider the$\operatorname { G a l } ( { \bar { \mathbf { Q } } } / \mathbf { Q } )$)-module$B ~ = ~ J _ { 1 } ( N ) [ l ^ { d } ] ~ \times ~ \mu _ { N l ^ { d } }$. By Cebotarev density, there is a prime <sup>ˇ</sup> q not dividing MNl so that Frobp = Frobq on B. Using the fact that$T _ { r } =$Frob$r + \langle r \rangle r ( { \mathrm { F r o b } } r ) ^ { - 1 }$on A for$r = p$and $r = q$, we see that$T _ { p } = T _ { q }$on$J _ { 1 } ( N ) [ l ^ { d } ]$. It follows that$T _ { p } - T _ { q }$is in$l ^ { d } \mathrm { E n d } _ { \mathbf { Z } _ { l } } A$ and therefore in$l ^ { d } R ^ { \prime } \subset l R$

Proof of2. Let S be the set of cusp forms in$S _ { 2 } ( \Gamma _ { 1 } ( N ) )$whose q-expansions at ∞ have coeficients in Z. Recall that$S _ { 2 } ( \Gamma _ { 1 } ( N ) ) = S { \otimes } \mathbf { C }$and that S is stable under the action of T (cf. [Sh1, Ch. 3] and [Hi4, §4]). The pairing$\mathbf { T } \otimes S  \mathbf { Z }$ defined by$T \otimes f \mapsto a _ { 1 } ( T f )$is easily checked to induce an isomorphism of T-modules

$$
S \cong \operatorname{Hom} _ {\mathbf {Z}} (\mathbf {T}, \mathbf {Z}).
$$

The surjectivity of$\mathbf { T } ^ { l } / l \mathbf { T } ^ { l } \to \mathbf { T } / l \mathbf { T }$is equivalent to the injectivity of the dual map

$$
\operatorname{Hom} (\mathbf {T}, \mathbf {F} _ {l}) \to \operatorname{Hom} (\mathbf {T} ^ {l}, \mathbf {F} _ {l}).
$$

Now use the isomorphism$S / l S \cong \operatorname { H o m } ( \mathbf { T } , \mathbf { F } _ { l } )$and note that if f is in the kernel of$S \to \mathrm { H o m } ( \mathbf{ T } ^ { l } , \mathbf { F } _ { l } )$, then$a _ { n } ( f ) = a _ { 1 } ( T _ { n } f )$is divisible by l for all n prime to l. But then the mod l form defined by f is in the kernel of the operator $\begin{array} { r } { q \frac { d } { d q } } \end{array}$, and is therefore trivial if l is odd. (See Corollary 5 of the main theorem of$\mathrm { \dot { [ K a ] } . ) }$Therefore f is in lS.

Remark. The argument does not prove that$\mathbf { T } ^ { M d } = \mathbf { T } ^ { d } \mathrm { i f } ( d , N ) \neq 1$

We now return to the assumptions that$\rho _ { \mathfrak { m } }$is irreducible,$p \nmid N$and $T _ { p } \notin$m. Next we define a principal ideal$( \Delta _ { p } )$$\mathbf { T } _ { H } ( N ) _ { \mathfrak { m } }$as follows. Since $\mathbf { T } _ { H } ( N , p ) _ { \mathfrak { m } _ { p } }$and$\mathbf { T } _ { H } ( N ) _ { \mathfrak { m } }$are both Gorenstein rings (by Corollary 2 of Theorem 2.1) we can define an adjoint$\hat { \alpha }$to

$$
\alpha : \mathbf {T} _ {H} (N, p) _ {\mathfrak {m} _ {p}} \longrightarrow S _ {1, \mathfrak {m} _ {1}} \simeq \mathbf {T} _ {H} (N) _ {\mathfrak {m}}
$$

in the manner described in the appendix and we set$\Delta _ { p } = ( \alpha \circ { \hat { \alpha } } ) ( 1 )$. Then $( \Delta _ { p } )$is independent of the choice of (Hecke-module) pairings on$\mathbf { T } _ { H } ( N , p ) _ { \mathfrak { m } _ { p } }$ and$\mathbf { T } _ { H } ( N ) _ { \mathfrak { m } }$. It is equal to the ideal generated by any composite map

$$
\mathbf {T} _ {H} (N) _ {\mathfrak {m}} \xrightarrow {\beta} \mathbf {T} _ {H} (N, p) _ {\mathfrak {m} _ {p}} \xrightarrow {\alpha} \mathbf {T} _ {H} (N) _ {\mathfrak {m}}
$$

provided that$\beta$is an injective map of$\mathbf { T } _ { H } ( N , p ) _ { \mathfrak { m } _ { p } }$-modules with$\mathbf { Z } _ { p }$torsion-free cokernel. (The module structure on$\mathbf { T } _ { H } ( N ) _ { \mathfrak { m } }$is defined via α.)

Proposition 2.4. Assume that m is$D _ { p }$-distinguished and that$\rho _ { \mathfrak { m } }$is irreducible of level N with$p \nmid N$. Then

$$
(\Delta_ {p}) = \left(T _ {p} ^ {2} - \langle p \rangle (1 + p) ^ {2}\right) = (a _ {p} ^ {2} - \langle p \rangle).
$$

Proof. Consider the maps on p-adic Tate-modules induced by$\varphi$and$\hat { \varphi } \colon$

$$
\operatorname{Ta} _ {p} \left(J _ {H} (N) ^ {2}\right) \xrightarrow {\varphi} \operatorname{Ta} _ {p} \left(J _ {H} (N, p)\right) \xrightarrow {\widehat {\varphi}} \operatorname{Ta} _ {p} \left(J _ {H} (N) ^ {2}\right).
$$

These maps commute with the standard Hecke operators with the exception of$T _ { p }$or$U _ { p }$(which are not even defined on all the terms). We define

$$
S _ {2} = \mathbf {T} _ {H} (N) [ U _ {2} ] / (U _ {2} ^ {2} - T _ {p} U _ {2} + p \langle p \rangle) \subseteq \operatorname{End} \left(J _ {H} (N) ^ {2}\right)
$$

where$U _ { 2 }$is the endomorphism of$J _ { H } ( N ) ^ { 2 }$defined by$\bigl ( { \begin{array} { l } { 0 \ { - } \langle p \rangle } \\ { p \quad T _ { p } } \end{array} } \bigr )$. It satisfies $\varphi U _ { 2 } = U _ { p } \varphi$. Again${ \mathfrak { m } } _ { 2 } = ( { \mathfrak { m } } , U _ { 2 } - { \widetilde { a _ { p } } } )$is a maximal ideal of$S _ { 2 }$and we have, on restricting to the${ \mathfrak { m } } _ { 1 } , { \mathfrak { m } } _ { p }$and m -adic Tate-modules:

$$
\operatorname{Ta} _ {\mathfrak {m} _ {2}} \left(J _ {H} (N) ^ {2}\right) \quad \xrightarrow {\varphi} \quad \operatorname{Ta} _ {\mathfrak {m} _ {p}} \left(J _ {H} (N, p)\right) \quad \xrightarrow {\widehat {\varphi}} \quad \operatorname{Ta} _ {\mathfrak {m} _ {1}} \left(J _ {H} (N) ^ {2}\right)\tag{2.12}
$$

$$
\uparrow \wr v _ {2}
$$

$$
\uparrow \wr v _ {1}
$$

$$
\mathrm{Ta} _ {\mathfrak {m}} \Big (J _ {H} (N) \Big)
$$

$$
\operatorname{Ta} _ {\mathfrak {m}} \left(J _ {H} (N)\right).
$$

The vertical isomorphisms are defined by$v _ { 2 } : x  ( - \langle p \rangle x , a _ { p } x )$and$v _ { 1 } : x$ $( a _ { p } x , p x )$. (Here$a _ { p } \in \mathbf { T } _ { H } ( N ) _ { \mathfrak { m } }$can be viewed as an element of${ \bf T } _ { H } ( N ) _ { p } \simeq$ $\Pi \mathbf { T } _ { H } ( N ) _ { \mathfrak { n } }$where the product is taken over the maximal ideals containing $p .$So$v _ { 1 }$and$v _ { 2 }$can be viewed as maps to$\mathrm { T a } _ { p } \Big ( J _ { H } ( N ) ^ { 2 } \Big )$whose images are respectively$\mathrm { T a } _ { \mathfrak { m } _ { 1 } } \left( J _ { H } ( N ) ^ { 2 } \right)$and$\mathrm { T a } _ { \mathfrak { m } _ { 2 } } \Big ( J _ { H } ( N ) ^ { 2 } \Big ) . \Big )$

Now$\widehat { \varphi }$is surjective and$\varphi$is injective with torsion-free cokernel by the result of Ribet mentioned before. Also$\begin{array} { l r } { \mathrm { T a } _ { \mathfrak { m } } \Big ( J _ { H } ( N ) \Big ) } & { \simeq } & { { \bf T } _ { H } ( N ) _ { \mathfrak { m } } ^ { 2 } } \end{array}$and $\mathrm { T a } _ { \mathfrak { m } _ { p } } \Big ( J _ { H } ( N , p ) \Big ) \simeq \mathbf { T } _ { H } ( N , p ) _ { \mathfrak { m } _ { p } } ^ { 2 }$by Corollary 1 to Theorem 2.1. So as$\varphi , \widehat { \varphi }$ are maps of$\mathbf { T } _ { H } ( N , p ) _ { \mathfrak { m } _ { \eta } }$-modules we can use this diagram to compute$\Delta _ { p }$as remarked just prior to the statement of the proposition. (The compatibility of the$U _ { p }$actions requires that, on identifying the completions$S _ { 1 , \mathfrak { m } _ { 1 } }$and$S _ { 2 , \mathfrak { m } _ { 2 } }$ with$\bar { \mathbf { T } } _ { H } ( N ) _ { \mathfrak { m } }$, we get$U _ { 1 } = U _ { 2 }$which is indeed the case.) We find that

$$
v _ {1} ^ {- 1} \circ \widehat {\varphi} \circ \varphi \otimes v _ {2} (z) = a _ {p} ^ {- 1} (a _ {p} ^ {2} - \langle p \rangle) (z).
$$

We now apply to$J _ { 1 } ( N , q ^ { 2 } )$(but$q \neq p )$the same analysis that we have just applied to$J _ { 1 } ( N , q ^ { 2 } )$. Here$X _ { 1 } ( A , B )$is the curve corresponding to$\Gamma _ { 1 } ( A ) \cap \Gamma _ { 0 } ( B )$ and$J _ { 1 } ( A , B )$its Jacobian. First we need the analogue of Ihara’s result. It is convenient to work in a slightly more general setting. Let us denote the maps $X _ { 1 } ( N q ^ { r - 1 } , q ^ { r } ) \to X _ { 1 } ( N q ^ { r - 1 } )$induced by$z \longrightarrow z$and$z  q z$by$\pi _ { 1 , r }$and$\pi _ { 2 , r }$ respectively. Similarly we denote the maps$X _ { 1 } ( N q ^ { r } , q ^ { r + 1 } )  X _ { 1 } ( N q ^ { r } )$induced by$z  z$and$z  q z \mathrm { \ b y \ } \pi _ { 3 , r }$and$\pi _ { 4 , r }$respectively. Also let$\pi : X _ { 1 } ( N q ^ { r } ) \to$ $X _ { 1 } ( N q ^ { r - 1 } , q ^ { r } )$denote the natural map induced by$z \longrightarrow z$

In the following lemma if m is a maximal ideal of$\mathbf { T } _ { 1 } ( N q ^ { r - 1 } )$or${ \bf T } _ { 1 } ( N q ^ { r } )$ we use$\mathfrak { m } ^ { ( q ) }$to denote the maximal ideal of$\mathbf { T } _ { 1 } ^ { ( q ) } ( N q ^ { r } , q ^ { r + 1 } )$compatible with m, the ring$\mathbf { T } _ { 1 } ^ { ( q ) } ( N q ^ { r } , q ^ { r + 1 } ) \subset \mathbf { T } _ { 1 } ( N q ^ { r } , q ^ { r + 1 } )$being the subring obtained by omitting$U _ { q }$from the list of generators.

Lemma 2.5. If$q \neq p$is a prime and$r \geq 1$then the sequence of abelian varieties

$$
0 \to J _ {1} (N q ^ {r - 1}) \xrightarrow {\xi_ {1}} J _ {1} (N q ^ {r}) \times J _ {1} (N q ^ {r}) \xrightarrow {\xi_ {2}} J _ {1} (N q ^ {r}, q ^ {r + 1})
$$

where$\xi _ { 1 } = \Bigl ( ( \pi _ { 1 , r } \circ \pi ) ^ { * } , - ( \pi _ { 2 , r } \circ \pi ) ^ { * } \Bigr )$and$\xi _ { 2 } = ( \pi _ { 4 , r } ^ { * } , \pi _ { 3 , r } ^ { * } )$induces a corresponding sequence$o f p$-divisible groups which becomes exact when localized at any$\mathfrak { m } ^ { ( q ) }$for which$\rho _ { \mathfrak { m } }$is irreducible.

Proof. Let$\Gamma ^ { 1 } ( N q ^ { r } )$denote the group$\left\{ \left( { \binom { a \ b } { c \ d } } \right) \in \Gamma _ { 1 } ( N ) : a \equiv d \equiv 1 ( q ^ { r } ) \right.$ $c \equiv 0 ( q ^ { r - 1 } ) , b \equiv 0 ( q ) \Big \}$. Let$B _ { 1 }$and$B ^ { 1 }$be given by

$$
B _ {1} = \Gamma_ {1} (N q ^ {r}) / \Gamma_ {1} (N q ^ {r}) \cap \Gamma (q), \quad B ^ {1} = \Gamma^ {1} (N q ^ {r}) / \Gamma_ {1} (N q ^ {r}) \cap \Gamma (q)
$$

and let$\Delta _ { q } = \Gamma _ { 1 } ( N q ^ { r - 1 } ) / \Gamma _ { 1 } ( N q ^ { r } ) \cap \Gamma ( q )$. Thus$\Delta _ { q } \simeq \mathrm { S L } _ { 2 } ( \mathbf { Z } / q ) { \mathrm { ~ i f ~ } } r = 1$and is of order a power of q if$r > 1$

The exact sequences of inflation-restriction give:

$$
H _ {1} (\Gamma_ {1} (N q ^ {r}), \mathbf {Q} _ {p} / \mathbf {Z} _ {p}) \stackrel {{\lambda_ {1}}} {{\longrightarrow}} H ^ {1} (\Gamma_ {1} (N q ^ {r}) \cap \Gamma (q), \mathbf {Q} _ {p} / \mathbf {Z} _ {p}) ^ {B _ {1}},
$$

together with a similar isomorphism with$\lambda ^ { 1 }$replacing$\lambda _ { 1 }$and$B ^ { 1 }$replacing$B _ { 1 }$. We also obtain

$$
H ^ {1} (\Gamma_ {1} (N q ^ {r - 1}), \mathbf {Q} _ {p} / \mathbf {Z} _ {p}) \stackrel {{\sim}} {{\longrightarrow}} H ^ {1} (\Gamma_ {1} (N q ^ {r}) \cap \Gamma (q), \mathbf {Q} _ {p} / \mathbf {Z} _ {p}) ^ {\Delta_ {q}}.
$$

The vanishing of$H ^ { 2 } ( \mathrm { S L } _ { 2 } ( \mathbf { Z } / q ) , \mathbf { Q } _ { p } / \mathbf { Z } _ { p } )$can be checked by restricting to the Sylow p-subgroup which is cyclic. Note that im$\lambda _ { 1 }$∩im$\lambda ^ { 1 } \subseteq H ^ { 1 } ( \Gamma _ { 1 } ( N q ^ { r } ) \cap \Gamma ( q )$ $\mathbf { Q } _ { p } / \mathbf { Z } _ { p } ) ^ { \Delta _ { q } }$since$B _ { 1 }$and$B ^ { 1 }$together generate$\Delta _ { q }$. Now consider the sequence

$$
\begin{array}{l} 0 \xrightarrow {} H ^ {1} (\Gamma_ {1} (N q ^ {r - 1}), \mathbf {Q} _ {p} / \mathbf {Z} _ {p}) \\ \xrightarrow {\operatorname{res} _ {1} \oplus - \operatorname{res} ^ {1}} H ^ {1} (\Gamma_ {1} (N q ^ {r}), \mathbf {Q} _ {p} / \mathbf {Z} _ {p}) \oplus H ^ {1} (\Gamma^ {1} (N q ^ {r}), \mathbf {Q} _ {p} / \mathbf {Z} _ {p}) \\ \xrightarrow {\lambda_ {1} \oplus \lambda^ {1}} H ^ {1} (\Gamma_ {1} (N q ^ {r}) \cap \Gamma (q), \mathbf {Q} _ {p} / \mathbf {Z} _ {p}). \end{array}\tag{2.13}
$$

We claim it is exact. To check this, suppose that$\lambda _ { 1 } ( x ) = - \lambda ^ { 1 } ( y )$. Then $\lambda _ { 1 } ( x ) ~ \in ~ H ^ { 1 } ( \Gamma _ { 1 } ( N q ^ { r } ) \cap \Gamma ( q ) , \mathbf { Q } _ { p } / \mathbf { Z } _ { p } ) ^ { \Delta _ { q } }$. So$\lambda _ { 1 } ( x )$is the restriction of an $x ^ { \prime } \in \Big . H ^ { 1 } \Big ( \Gamma _ { 1 } \big ( N q ^ { r - 1 } \big ) , \mathbf { Q } _ { p } \big / \mathbf { Z } _ { p } \Big )$whence$x - \mathrm { r e s } _ { 1 } ( x ^ { \prime } ) \in \ker \lambda _ { 1 } = 0$. It follows also that$y = - \mathrm { r e s } ^ { 1 } ( x ^ { \prime } )$

Now conjugation by the matrix$\textstyle { \binom { q 0 } { 0 1 } }$induces isomorphisms

$$
\Gamma^ {1} (N q ^ {r}) \simeq \Gamma_ {1} (N q ^ {r}), \quad \Gamma_ {1} (N q ^ {r}) \cap \Gamma (q) \simeq \Gamma_ {1} (N q ^ {r}, q ^ {r + 1}).
$$

So our sequence (2.13) yields the exact sequence of the lemma, except that we have to change from group cohomology to the cohomology of the associated complete curves. If the groups are torsion-free then the diference between these cohomologies is Eisenstein (more precisely$T _ { l } - 1 - l$for$l \equiv 1 { \bmod { N } } q ^ { r + 1 }$ is nilpotent) so will vanish when we localize at the preimage of$\mathfrak { m } ^ { ( q ) }$in the abstract Hecke ring generated as a polynomial ring by all the standard Hecke operators excluding$T _ { q }$. If$M \ \leq \ 3$then the group$\Gamma _ { 1 } ( M )$has torsion. For $M \ = \ 1 , 2 , 3$we can restrict to$\Gamma ( 3 ) , \Gamma ( 4 ) , \Gamma ( 3 )$, respectively, where the co-homology is Eisenstein as the corresponding curves have genus zero and the groups are torsion-free. Thus one only needs to check the action of the Hecke operators on the kernels of the restriction maps in these three exceptional cases. This can be done explicitly and again they are Eisenstein. This completes the proof of the lemma.

Let us denote the maps$X _ { 1 } ( N , q )  X _ { 1 } ( N )$induced by$z \longrightarrow z$and$z \longrightarrow q z$ by$\pi _ { 1 }$and$\pi _ { 2 }$respectively. Similarly we denote the maps$X _ { 1 } ( N , q ^ { 2 } )  X _ { 1 } ( N , q )$ induced by$z \longrightarrow z$and$z \longrightarrow q z$by$\pi _ { 3 }$and$\pi _ { 4 }$respectively.

From the lemma (with$r = 1 )$and Ihara’s result (2.10) we deduce that there is a sequence

$$
0 \to J _ {1} (N) \times J _ {1} (N) \times J _ {1} (N) \stackrel {\xi} {\longrightarrow} J _ {1} (N, q ^ {2})\tag{2.14}
$$

where$\xi = ( \pi _ { 1 } \circ \pi _ { 3 } ) ^ { * } \times ( \pi _ { 2 } \circ \pi _ { 3 } ) ^ { * } \times ( \pi _ { 2 } \circ \pi _ { 4 } ) ^ { * }$and that the induced map of$p \mathrm { - }$ divisible groups becomes injective after localization at${ \mathfrak { m } } ^ { ( q ) } \mathrm { { s } }$which correspond to irreducible$\rho _ { \mathfrak { m } } \mathrm { ^ { \prime } s }$. By duality we obtain a sequence

$$
J _ {1} (N, q ^ {2}) \stackrel {\hat {\xi}} {\longrightarrow} J _ {1} (N) ^ {3} \to 0
$$

which is ‘surjective’ on Tate modules in the same sense. More generally we can prove analogous results for$J _ { H } ( N )$and$J _ { H } ( N , q ^ { 2 } )$although there may be a kernel of order divisible by$p$in$J _ { H } ( N ) \to J _ { 1 } ( N )$. However this kernel will not meet the$\mathfrak { m } ^ { ( q ) }$-divisible group for any maximal ideal$\mathfrak { m } ^ { ( q ) }$whose associated $\rho _ { \mathfrak { m } }$is irreducible and hence, as in the earlier cases, will not afect the results if after passing to p-divisible groups we localize at such an$\mathfrak { m } ^ { ( q ) }$. We use the same notation in the general case when$H \neq 1 \mathrm { s o } \xi$is the map$J _ { H } ( N ) ^ { 3 }  J _ { H } ( N , q ^ { 2 } )$

We suppose now that m is a maximal ideal of${ \bf T } _ { H } ( N )$(as always with$p \in$ m) associated to an irreducible representation and that q is a prime,$p \nmid N p$ We now define a maximal ideal${ \mathfrak { m } } _ { q }$of${ \bf T } _ { H } ( N , q ^ { 2 } )$with the same associated representation as m. To do this consider the ring

$$
S _ {1} = \mathbf {T} _ {H} (N) [ U _ {1} ] / U _ {1} (U _ {1} ^ {2} - T _ {q} U _ {1} + q \langle q \rangle) \subseteq \operatorname{End} \left(J _ {H} (N) ^ {3}\right)
$$

where the action of$U _ { 1 }$on$J _ { H } ( N ) ^ { 3 }$is given by the matrix

$$
\left[ \begin{array}{c c c} T _ {q} & - \langle q \rangle & 0 \\ q & 0 & 0 \\ 0 & q & 0 \end{array} \right].
$$

Then$U _ { 1 }$satisfies the compatibility

$$
\widehat {\xi} \circ U _ {q} = U _ {1} \circ \widehat {\xi}.
$$

One checks this using the actions on cotangent spaces. For we may identify the cotangent spaces with spaces of cusp forms and with this identification any Hecke operator$t _ { * }$induces the usual action on cusp forms. There is a maximal ideal${ \mathfrak { m } } _ { 1 } = ( U _ { 1 } , { \mathfrak { m } } )$in$S _ { 1 }$and$S _ { 1 , \mathfrak { m } _ { 1 } } \simeq \mathbf { T } _ { H } ( N ) _ { \mathfrak { m } }$. We let${ \mathfrak { m } } _ { q }$denote the reciprocal image of m<sub>1</sub> in${ \bf T } _ { H } ( N , q ^ { 2 } )$under the natural map${ \bf T } _ { H } ( \hat { N } , q ^ { 2 } )  S _ { 1 }$

Next we define a principal ideal$( \Delta _ { q } ^ { \prime } )$of$\mathbf { T } _ { H } ( N ) _ { \mathfrak { m } }$using the fact that $\mathbf { T } _ { H } ( N , q ^ { 2 } ) _ { \mathfrak { m } _ { q } }$and$\mathbf { T } _ { H } ( N ) _ { \mathfrak { m } }$are both Gorenstein rings (cf. Corollary 2 to Theorem 2.1). Thus we set$\left( \Delta _ { q } ^ { \prime } \right) = \left( \widehat { \alpha } \circ \alpha ^ { \prime } \right)$where

$$
\alpha^ {\prime}: \mathbf {T} _ {H} (N, q ^ {2}) _ {\mathfrak {m} _ {q}} \to S _ {1, \mathfrak {m} _ {1}} \simeq \mathbf {T} _ {H} (N) _ {\mathfrak {m}}
$$

is the natural map and$\widehat { \alpha } ^ { \prime }$is the adjoint with respect to selected Hecke-module pairings on$\mathbf { T } _ { H } ( N , q ^ { 2 } ) _ { \mathfrak { m } _ { q } }$and$\mathbf { T } _ { H } ( N ) _ { \mathfrak { m } }$. Note that$\alpha ^ { \prime }$is surjective. To show that the$T _ { q }$operator is in the image one can use the existence of the associated 2-dimensional representation (cf. §1) in which$T _ { q } = \mathrm { t r a c e } ( \mathrm { F r o b } q )$and apply the Cebotarev density theorem. <sup>ˇ</sup>

Proposition 2.6. Suppose that frakm is a maximal ideal of${ \bf T } _ { H } ( N )$ associated to an irreducible$\rho _ { \mathfrak { m } }$. Suppose also that$q \nmid N p$. Then

$$
(\Delta_ {p} ^ {\prime}) = (q - 1) (T _ {q} ^ {2} - \langle q \rangle (1 + q) ^ {2}).
$$

Proof. We prove this in the same manner as we proved Proposition 2.4. Consider the maps on p-adic Tate-modules induced by$\xi$and$\widehat { \xi } \colon$

$$
\mathrm{Ta} _ {p} \Big (J _ {H} (N) ^ {3} \Big) \xrightarrow {\xi} \mathrm{Ta} _ {p} \Big (J _ {H} (N, q ^ {2}) \Big) \xrightarrow {\widehat {\xi}} \mathrm{Ta} _ {p} \Big (J _ {H} (N) ^ {3} \Big).\tag{2.15}
$$

These maps commute with the standard Hecke operators with the exception of$T _ { q }$and$U _ { q }$(which are not even defined on all the terms). We define

$$
S _ {2} = \mathbf {T} _ {H} (N) [ U _ {2} ] / U _ {2} (U _ {2} ^ {2} - T _ {q} U _ {2} + q \langle q \rangle) \subseteq \operatorname{End} \left(J _ {H} (N) ^ {3}\right)
$$

where$U _ { 2 }$is the endomorphism of$J _ { H } ( N ) ^ { 3 }$given by the matrix

$$
\left[ \begin{array}{c c c} 0 & 0 & 0 \\ q & 0 & - \langle q \rangle \\ 0 & q & T _ {q} \end{array} \right].
$$

Then$U _ { q } \xi = \xi U _ { 2 }$as one can verify by checking the equality$( \widehat { \xi } \circ \xi ) U ^ { 2 } = U _ { 1 } ( \widehat { \xi } \circ \xi )$ because$\hat { \xi } \circ \xi$is an isogeny. The formula for${ \widehat { \xi } } \circ \xi$is given below. Again ${ \mathfrak { m } } _ { 2 } = ( { \mathfrak { m } } , U _ { 2 } )$is a maximal ideal of$S _ { 2 }$and$S _ { 2 , \mathfrak { m } _ { 2 } } \simeq \mathbf { T } _ { H } ( N ) _ { \mathfrak { m } }$. On restricting (2.15) to the${ \mathfrak { m } } _ { 2 } , { \mathfrak { m } } _ { q }$and$\mathfrak { m } _ { 1 } \mathrm { - a d i c }$Tate modules we get

$$
\begin{array}{c c c c c} \mathrm{Ta} _ {\mathfrak {m} _ {2}} (J _ {H} (N) ^ {3}) & \stackrel {{\xi}} {{\longrightarrow}} & \mathrm{Ta} _ {\mathfrak {m} _ {q}} (J _ {H} (N, q ^ {2})) & \stackrel {{\widehat {\xi}}} {{\longrightarrow}} & \mathrm{Ta} _ {\mathfrak {m} _ {1}} (J _ {H} (N) ^ {3}) \\ \Bigg \uparrow \wr u _ {2} & & & & \Bigg \uparrow \wr u _ {1} \\ \mathrm{Ta} _ {\mathfrak {m}} (J _ {H} (N)) & & & & \mathrm{Ta} _ {\mathfrak {m}} (J _ {H} (N)). \end{array}\tag{2.16}
$$

The vertical isomorphisms are induced by$u _ { 2 } : z  ( \langle q \rangle z , - T _ { q } z , q z )$and$u _ { 1 }$: $z  ( 0 , 0 , z )$. Now a calculation shows that on$J _ { H } ( N ) ^ { 3 }$

$$
\hat {\xi} \circ \xi = \left[ \begin{array}{c c c} q (q + 1) & T _ {q} \cdot q & T _ {q} ^ {2} - \langle q \rangle (1 + q) \\ T _ {q} ^ {*} \cdot q & q (q + 1) & T _ {q} \cdot q \\ T _ {q} ^ {* 2} - \langle q \rangle^ {- 1} (1 + q) & T _ {q} ^ {*} \cdot q & q (q + 1) \end{array} \right]
$$

where$T _ { q } ^ { * } = \langle q \rangle ^ { - 1 } T _ { q }$

We compute then that

$$
(u _ {1} ^ {- 1} \circ \widehat {\xi} \circ \xi \circ u _ {2}) = - \langle q ^ {- 1} \rangle (q - 1) \left(T _ {q} ^ {2} - \langle q \rangle (1 + q) ^ {2}\right).
$$

Now using the surjectivity of$\widehat { \xi }$and that$\xi$has torsion-free cokernel in (2.16) (by Lemma 2.5) and that$\mathrm { T a } _ { \mathfrak { m } } \Big ( J _ { H } \big ( N \big ) \Big )$and$\mathrm { T a } _ { \mathfrak { m } _ { q } } \Big ( J _ { H } \big ( N , q ^ { 2 } \big ) \Big )$are each free of rank$2$over the respective Hecke rings (Corollary 1 of Theorem 2.1), we deduce the result as in Proposition 2.4.

There is one further (and completely elementary) generalization of this result. We let$\pi : X _ { H } ( N q , q ^ { 2 } )  X _ { H } ( N , q ^ { 2 } )$be the map given by$z \ \longrightarrow \ z$ Then$\pi ^ { * } : J _ { H } ( N , q ^ { 2 } )  J _ { H } ( N q , q ^ { 2 } )$has kernel a cyclic group and as before this will vanish when we localize at$\mathfrak { m } ^ { ( q ) }$if m is associated to an irreducible representation. (As before the superscript$q$denotes the omission of$U _ { q }$from the list of generators of${ \bf T } _ { H } ( N q , q ^ { 2 } )$and$\mathfrak { m } ^ { ( q ) }$denotes the maximal ideal of $\mathbf { T } _ { H } ^ { ( q ) } ( N q , q ^ { 2 } )$compatible with m.)

We thus have a sequence (not necessarily exact)

$$
0 \to J _ {H} (N) ^ {3} \stackrel {\kappa} {\longrightarrow} J _ {H} (N q, q ^ {2}) \to Z \to 0
$$

where$\kappa = \pi ^ { * } \circ \xi$which induces a corresponding sequence of p-divisible groups which becomes exact when localized at an$\mathfrak { m } ^ { ( q ) }$corresponding to an irreducible $\rho _ { \mathfrak { m } }$. Here$Z$is the quotient abelian variety$J _ { H } ( N q , q ^ { 2 } ) / \mathrm { i m } \kappa$. As before there is a natural surjective homomorphism

$$
\alpha : \mathbf {T} _ {H} (N q, q ^ {2}) _ {\mathfrak {m} _ {q}} \to S _ {1, \mathfrak {m} _ {1}} \simeq \mathbf {T} _ {H} (N) _ {\mathfrak {m}}
$$

where${ \mathfrak { m } } _ { q }$is the inverse image of$\mathfrak { m } _ { 1 }$in${ \bf T } _ { H } ( N q , q ^ { 2 } )$. (We note that one can replace$\hat { \mathbf { T } } _ { H } ( N q , q ^ { 2 } )$by${ \bf T } _ { H } ( N q ^ { 2 } )$in the definition of α and Proposition 2.7 below would still hold unchanged.) Since both rings are again Gorenstein we can define an adjoint$\widehat { \alpha }$and a principal ideal

$$
(\Delta_ {q}) = (\alpha \circ \widehat {\alpha}).
$$

Proposition 2.7. Suppose that m is a maximal ideal of$\mathbf { T } = \mathbf { T } _ { H } ( N )$ associated to an irreducible representation. Suppose that$q \nmid N p$. Then

$$
\left(\Delta_ {q}\right) = (q - 1) ^ {2} \left(T _ {q} ^ {2} - \langle q \rangle (1 + q) ^ {2}\right)).
$$

The proof is a trivial generalization of that of Proposition 2.6.

Remark 2.8. We have included the operator$U _ { q }$in the definition of$\mathbf { T } _ { \mathfrak { m } _ { q } } =$ $\mathbf { T } _ { H } ( N q , q ^ { 2 } ) _ { \mathfrak { m } _ { q } }$as in the application of the q-expansion principle it is important to have all the Hecke operators. However$U _ { q } = 0$in$\mathbf { T } _ { \mathfrak { m } _ { q } }$. To see this we recall that the absolute values of the eigenvalues$c ( q , f )$of$U _ { q }$on newforms of level $N q$with$q \nmid N$are known (cf. [Li]). They satisfy$c ( \widehat { q , f } ) ^ { 2 } = \langle q \rangle$in$\mathcal { O } _ { f }$(the ring of integers generated by the Fourier coeficients of f) if f is on$\Gamma _ { 1 } ( N , q )$, and$| c ( q , f ) | = q ^ { 1 / 2 }$if$f$is on$\Gamma _ { 1 } ( N q )$but not on$\Gamma _ { 1 } ( N , q )$. Also when$f$is a newform of level dividing N the roots of$x ^ { 2 } - c ( q , f ) x + q \chi _ { f } ( q ) = 0$have absolute value$q ^ { 1 / 2 }$where$c ( q , f )$is the eigenvalue of$T _ { q }$and$\chi _ { f } ( q )$of$\langle q \rangle$. Since for$f$on$\Gamma _ { 1 } ( N q , q ^ { 2 } ) , U _ { q } f$is a form on$\Gamma _ { 1 } ( N q )$we see that

$$
U _ {q} (U _ {q} ^ {2} - \langle q \rangle) \prod_ {f \in \mathcal {S} _ {1}} (U _ {q} - c (q, f)) \prod_ {f \in \mathcal {S} _ {2}} \left(U _ {q} ^ {2} - c (q, f) U _ {q} + q \langle q \rangle\right) = 0
$$

in${ \bf T } _ { H } ( N q , q ^ { 2 } ) \otimes { \bf C }$where$S _ { 1 }$is the set of newforms on$\Gamma _ { 1 } ( N q )$which are not on$\Gamma _ { 1 } ( n , q )$and$S _ { 2 }$is the set of newforms of level dividing N. In particular as $U _ { q }$is in${ \mathfrak { m } } _ { q }$it must be zero in$\mathbf { T } _ { \mathfrak { m } _ { q } }$

A slightly diferent situation arises if m is a maximal ideal of${ \bf T } = { \bf T } _ { \cal H } ( N , q )$ $( q \neq p )$which is not associated to any maximal ideal of level N (in the sense of having the same associated$\rho _ { \mathfrak { m } } )$. In this case we may use the map$\xi _ { 3 } = ( \pi _ { 4 } ^ { * } , \pi _ { 3 } ^ { * } )$ to give

$$
J _ {H} (N, q) \times J _ {H} (N, q) \xrightarrow {\xi_ {3}} J _ {H} (N, q ^ {2}) \xrightarrow {\hat {\xi} _ {3}} J _ {H} (N, q) \times J _ {H} (N, q).\tag{2.17}
$$

Then$\hat { \xi } _ { 3 } \circ \xi _ { 3 }$is given by the matrix

$$
\hat {\xi} _ {3} \circ \xi_ {3} = \left[ \begin{array}{c c} q & U _ {q} ^ {*} \\ U _ {q} & q \end{array} \right]
$$

on$J _ { H } ( N , q ) ^ { 2 }$, where$U _ { q } ^ { * } = U _ { q } \langle q \rangle ^ { - 1 }$and$U _ { q } ^ { 2 } = \langle q \rangle$on the m-divisible group. The second of these formulae is standard as mentioned above; cf. for example$[ \mathrm { L i } ,$ Th. 3], since$\rho _ { m }$is not associated to any maximal ideal of level N. For the first consider any newform f of level divisible by q and observe that the Petersson inner product$\Big \langle ( U _ { q } ^ { * } U _ { q } - 1 ) f ( r z ) , f ( m z ) \Big \rangle$is zero for any$r , m | ( N q / \mathrm { l e v e l } f )$ by [Li, Th. 3]. This shows that$U _ { q } ^ { * } U _ { q } f ( r z )$, a priori a linear combination of $f ( m _ { i } z )$, is equal to$f ( r z )$. So$U _ { q } ^ { * } \dot { U _ { q } } = 1$on the space of forms on$\Gamma _ { H } ( N , q )$ which are new at q, i.e. the space spanned by forms$\{ f ( s z ) \}$where f runs through newforms with q|level f. In particular$U _ { q } ^ { * }$preserves the m-divisible group and satisfies the same relation on it, again because$\rho _ { \mathfrak { m } }$is not associated to any maximal ideal of level N.

Remark 2.9. Assume that$\rho _ { \mathfrak { m } }$is of type (A) at$q$in the terminology of Chapter 1, §1 (which ensures that$\rho _ { \mathfrak { m } }$does not occur at level N). In this case${ \bf T } _ { \mathfrak { m } } = { \bf T } _ { H } ( N , q ) _ { \mathfrak { m } }$is already generated by the standard Hecke operators with the omission of$U _ { q }$. To see this, consider the$\mathrm { G L _ { 2 } } ( \mathbf { T } _ { \mathfrak { m } } )$representation of ${ \mathrm { G a l } } ( { \overline { { \mathbf { Q } } } } / \mathbf { Q } )$associated to the m-adic Tate module of$J _ { H } ( N , q )$(cf. the discussion following Corollary 2 of Theorem 2.1). Then this representation is already defined over the$\mathbf { Z } _ { p } .$-subalgebra$\mathbf { T } _ { \mathfrak { m } } ^ { \mathrm { t r } }$of$\mathbf { T } _ { \mathfrak { m } }$generated by the traces of Frobenius elements, i.e. by the$T _ { \ell }$for$\ell \nmid N q p$. In particular$\langle q \rangle \in \mathbf { T } _ { \mathfrak { m } } ^ { \mathrm { t r } }$. Furthermore, as $\mathbf { T } _ { m } ^ { \mathrm { t r } }$is local and complete, and as$U _ { q } ^ { 2 } = \langle q \rangle$, it is enough to solve$X ^ { 2 } = \langle q \rangle$ in the residue field of$\mathbf { T } _ { \mathfrak { m } } ^ { \mathrm { t r } }$. But we can even do this in$k _ { 0 }$(the minimal field of definition of$\rho _ { \mathfrak { m } } )$by letting X be the eigenvalue of Frob q on the unique unramified rank-one free quotient of$k _ { 0 } ^ { 2 }$and invoking the$\pi _ { q } \simeq \pi ( \sigma _ { q } )$theorem of Langlands (cf. [Ca1]). (It is to ensure that the unramified quotient is free of rank one that we assume$\rho _ { \mathfrak { m } }$to be of type (A).)

We assume now that$\rho _ { \mathfrak { m } }$is of type (A) at q. Define$S _ { 1 }$this time by setting

$$
S _ {1} = \mathbf {T} _ {H} (N, q) [ U _ {1} ] / U _ {1} (U _ {1} - U _ {q}) \subseteq \operatorname{End} \left(J _ {H} (N, q) ^ {2}\right)
$$

where$U _ { 1 }$is given by the matrix

$$
U _ {1} = \left[ \begin{array}{c c} 0 & q \\ 0 & U _ {q} \end{array} \right]\tag{2.18}
$$

on$J _ { H } ( N , q ) ^ { 2 }$. The map$\widehat { \xi } _ { 3 }$is not necessarily surjective and to remedy this we introduce$\mathfrak { m } ^ { ( q ) } = \mathfrak { m } \cap \mathbf { T } _ { H } ^ { ( q ) } ( N , q )$where$\mathbf { T } _ { H } ^ { ( q ) } ( N , q )$is the subring of${ \bf T } _ { H } ( N , q )$ generated by the standard Hecke operators but omitting$U _ { q }$. We also write$\mathfrak { m } ^ { ( q ) }$ for the corresponding maximal ideal of$\mathbf { T } _ { H } ^ { ( q ) } ( N q , q ^ { 2 } )$. Then on$\mathfrak { m } ^ { ( q ) }$-divisible groups,$\widehat { \xi } _ { 3 }$and$\widehat { \xi _ { 3 } } \circ \pi _ { * }$are surjective and we get a natural restriction map of localization${ \bf T } _ { H } \big ( N q , q ^ { 2 } \big ) _ { ( \mathfrak { m } ^ { ( q ) } ) } \longrightarrow S _ { 1 ( \mathfrak { m } ^ { ( q ) } ) }$. (Note that the image of$U _ { q }$under this map is$U _ { 1 }$and not$U _ { q } . )$The ideal${ \mathfrak { m } } _ { 1 } = ( { \mathfrak { m } } , U _ { 1 } )$is maximal in$S _ { 1 }$and so also in$S _ { 1 , ( \mathfrak { m } ^ { ( q ) } ) }$and we let${ \mathfrak { m } } _ { q }$denote the inverse image of${ \mathfrak { m } } _ { 1 }$under this restriction map. The inverse image of${ \mathfrak { m } } _ { q }$in${ \bf T } _ { H } ( N q , q ^ { 2 } )$is also a maximal ideal which we agin write${ \mathfrak { m } } _ { q }$. Since the completions$\mathbf { T } _ { H } ( N q , q ^ { 2 } ) _ { \mathfrak { m } _ { q } }$and$S _ { 1 , \mathfrak { m } _ { 1 } } \simeq \mathbf { T } _ { H } ( N , q ) _ { \mathfrak { m } }$ are both Gorenstein rings (by Corollary 2 of Theorem 2.1) we can define a principal ideal$( \Delta _ { q } )$of$\mathbf { T } _ { H } ( N , q ) _ { \mathfrak { m } }$by

$$
(\Delta_ {q}) = (\alpha \circ \widehat {\alpha})
$$

where$\alpha : { \bf T } _ { H } ( N q , q ^ { 2 } ) _ { \mathfrak { m } _ { q } } \to S _ { 1 , \mathfrak { m } _ { 1 } } \simeq { \bf T } ( N , q ) _ { \mathfrak { m } }$is the restriction map induced by the restriction map on m<sup>(q)</sup>-localizations described above.

Proposition 2.10. Suppose that m is a maximal ideal of${ \bf T } _ { H } ( N , q )$ associated to an irreducible m of type$( \mathrm { A } )$. Then

$$
(\Delta_ {q}) = (q - 1) ^ {2} (q + 1).
$$

Proof. The method is a straightforward adaptation of that used for Propositions 2.4 and 2.6. We let$S _ { 2 } = { \bf T } _ { H } ( N , q ) [ U _ { 2 } ] / U _ { 2 } ( U _ { 2 } - U _ { q } )$be the ring of endomorphisms of$J _ { H } ( N , q ) ^ { 2 }$where$U _ { 2 }$is given by the matrix

$$
\left[ \begin{array}{c c} U _ {q} & q \\ 0 & 0 \end{array} \right].
$$

This satisfies the compatability$\xi _ { 3 } U _ { 2 } = U _ { q } \xi _ { 3 }$. We define${ \mathfrak { m } } _ { 2 } = ( { \mathfrak { m } } , U _ { 2 } )$in$S _ { 2 }$ and observe that$S _ { 2 } , \mathfrak { m } _ { 2 } \simeq \mathbf { T } _ { H } ( N , q ) _ { \mathfrak { m } }$

Then we have maps

$$
\begin{array}{c c c c c} \mathrm{Ta} _ {\mathfrak {m} _ {2}} \Big (J _ {H} (N, q) ^ {2} \Big) & \stackrel {{\pi^ {*} \circ \xi_ {3}}} {{\hookrightarrow}} & \mathrm{Ta} _ {\mathfrak {m} _ {q}} \Big (J _ {H} (N q, q ^ {2}) \Big) & \stackrel {{\hat {\xi} _ {3} \circ \pi_ {*}}} {{\twoheadrightarrow}} & \mathrm{Ta} _ {\mathfrak {m} _ {1}} \Big (J _ {H} (N, q) ^ {2} \Big) \\ \uparrow \wr v _ {2} & & & & \uparrow \wr v _ {1} \\ \mathrm{Ta} _ {\mathfrak {m}} \Big (J _ {H} (N, q) \Big) & & & & \mathrm{Ta} _ {\mathfrak {m}} \Big (J _ {H} (N, q) \Big). \end{array}
$$

The maps$v _ { 1 }$and$v _ { 2 }$are given by$v _ { 2 } : z \to \left( - q z , a _ { q } z \right)$and$v _ { 1 } : z \to ( z , 0 )$ where$U _ { q } = a _ { q }$in$\mathbf { T } _ { H } ( N , q ) _ { \mathfrak { m } }$. One checks then that$v _ { 1 } ^ { - 1 } \circ ( \hat { \xi } _ { 3 } \circ \pi _ { * } ) \circ \left( \pi ^ { * } \circ \xi _ { 3 } \right) \circ v _ { 2 }$ is equal to$- ( q - 1 ) ( q ^ { 2 } - 1 )$or$- { \textstyle \frac { 1 } { 2 } } ( q - 1 ) ( q ^ { 2 } - 1 )$

The surjectivity of$\hat { \xi _ { 3 } } \circ \pi _ { * }$on the completions is equivalent to the statement that

$$
J _ {H} (N q, q ^ {2}) [ p ] _ {\mathfrak {m} _ {q}} \to J _ {H} (N, q) ^ {2} [ p ] _ {\mathfrak {m} _ {1}}
$$

is surjective. We can replace this condition by a similar one with$\mathfrak { m } ^ { ( q ) }$substituted for${ \mathfrak { m } } _ { q }$and for${ \mathfrak { m } } _ { 1 }$, i.e., the surjectivity of

$$
J _ {H} (N q, q ^ {2}) [ p ] _ {\mathfrak {m} ^ {(q)}} \rightarrow J _ {H} (N, q) ^ {2} [ p ] _ {\mathfrak {m} ^ {(q)}}.
$$

By our hypothesis that$\rho _ { \mathfrak { m } }$be of type (A) at$q$it is even suficient to show that the cokernel of$J _ { H } ( N q , q ^ { 2 } ) [ p ] \otimes \overline { { { \bf F } } } _ { p }  J _ { H } ( N , q ) ^ { 2 } [ p ] \otimes \overline { { { \bf F } } } _ { p }$has no subquotient as a Galois-module which is irreducible, two-dimensional and ramified at$q .$. This statement, or rather its dual, follows from Lemma 2.5. The injectivity of$\pi ^ { * } \circ \xi _ { 3 }$ on the completions and the fact that it has torsion-free cokernel also follows from Lemma 2.5 and our hypothesis that$\rho _ { \mathfrak { m } }$be of type (A) at$q .$

The case that corresponds to type (B) is similar. We assume in the analysis of type (B) (and also of type (C) below) that H decomposes as$\Pi H _ { q }$as described at the beginning of Section 1. We assume that m is a maximal ideal of${ \mathbf { T } } _ { H } ( N q ^ { r } )$where H contains the Sylow p-subgroup$S _ { p }$of$( \mathbf { Z } / q ^ { r } \mathbf { Z } ) ^ { * }$and that

$$
\rho_ {\mathfrak {m}} \Big | _ {I _ {q}} \approx \left( \begin{array}{c c} \chi_ {q} & \\ & 1 \end{array} \right)\tag{2.19}
$$

for a suitable choice of basis with$\chi _ { q } \neq 1$and cond$\chi _ { q } = q ^ { r }$. Here$q \nmid N p$and we assume also that$\rho _ { \mathfrak { m } }$is irreducible. We use the sequence

$$
J _ {H} (N q ^ {r}) \times J _ {H} (N q ^ {r}) \xrightarrow {(\pi^ {\prime}) ^ {*} \circ \xi_ {2}} J _ {H ^ {\prime}} (N q ^ {r}, q ^ {r + 1}) \xrightarrow {\hat {\xi} _ {2} \circ \pi_ {*} ^ {\prime}} J _ {H} (N q ^ {r}) \times J _ {H} (N q ^ {r})
$$

defined analogously to (2.17) where$\xi _ { 2 }$was as defined in Lemma 2.5 and where $H ^ { \prime }$is defined as follows. Using the notation$H = \Pi H _ { l }$as at the beginning of Section 1 set$H _ { l } ^ { \prime } = H _ { l }$for$l \neq q$and$H _ { q } ^ { \prime } \times S _ { p } = H _ { q }$. Then define$H ^ { \prime } = \Pi H _ { l } ^ { \prime }$and let$\pi ^ { \prime } : X _ { H ^ { \prime } } ( N q ^ { r } , q ^ { r + 1 } )  X _ { H } ( N q ^ { r } , \acute { q } ^ { r + 1 } )$be the natural map$z  z$. Using Lemma 2.5 we check that$\xi _ { 2 }$is injective on the$\mathfrak { m } ^ { ( q ) }$-divisible group. Again we set$S _ { 1 } = \mathbf { T } _ { H } ( N q ^ { r } ) [ U _ { 1 } ] / U _ { 1 } ( U _ { 1 } - U _ { q } ) \subseteq \mathrm { E n d } ( J _ { H } \Big ( N q ^ { r } ) ^ { 2 } \Big )$where$U _ { 1 }$is given by the matrix in (2.18). We define${ \mathfrak { m } } _ { 1 } = ( { \mathfrak { m } } , U _ { 1 } )$and let${ \mathfrak { m } } _ { q }$be the inverse image of${ \mathfrak { m } } _ { 1 }$in$\mathbf { T } _ { H ^ { \prime } } ( N q ^ { r } , q ^ { r + 1 } )$. The natural map (in which${ \bar { U _ { q } } } \to U _ { 1 } )$

$$
\alpha : \mathbf {T} _ {H ^ {\prime}} (N q ^ {r}, q ^ {r + 1}) _ {\mathfrak {m} _ {q}} \to S _ {1, \mathfrak {m} _ {1}} \simeq \mathbf {T} _ {H} (N q ^ {r}) _ {\mathfrak {m}}
$$

is surjective by the following remark.

Remark 2.11. When we assume that$\rho _ { \mathfrak { m } }$is of type (B) then the$U _ { q }$operator is redundant in${ \bf T } _ { \mathfrak { m } } = { \bf T } _ { H } ( N q ^ { r } ) _ { \mathfrak { m } }$. To see this, first assume that$\mathbf { T } _ { \mathfrak { m } }$is reduced and consider the$\mathrm { G L _ { 2 } } ( \mathbf { T } _ { \mathfrak { m } } )$representation of${ \mathrm { G a l } } ( { \overline { { \mathbf { Q } } } } / \mathbf { Q } )$associated to the madic Tate module. Pick a$\sigma _ { q } \in I _ { q }$, the inertia group in$D _ { q }$in${ \mathrm { G a l } } ( { \overline { { \mathbf { Q } } } } / \mathbf { Q } )$, such that$\chi _ { q } ( \sigma _ { q } ) \neq 1$. Then because the eigenvalues of$\sigma _ { q }$are distinct mod m we can diagonalize the representation with respect to$\sigma _ { q }$. If Frobq is a Frobenius in$D _ { q } ,$ then in the$\mathrm { G L _ { 2 } } ( \mathbf { T } _ { \mathfrak { m } } )$representation the image of Frob$q$normalizes$I _ { q }$and we can recover$U _ { q }$as the entry of the matrix giving the value of Frob$q$on the unit eigenvector for$\sigma _ { q }$. This is by the$\pi _ { q } \simeq \pi ( \sigma _ { q } )$theorem of Langlands as before (cf. [Ca1]) applied to each of the representations obtained from maps${ \bf T } _ { \mathfrak { m } }$ $\mathcal { O } _ { f , \lambda }$. Since the representation is defined over the Z -algebra$\mathbf { T } _ { \mathfrak { m } } ^ { \mathrm { t } r }$generated by the traces, the same reasoning applied to$\mathbf { T } _ { \mathfrak { m } } ^ { \mathrm { t r } }$shows that$U _ { q } \in \mathbf { T } _ { \mathfrak { m } } ^ { \mathrm { t r } }$

If$\mathbf { T } _ { \mathfrak { m } }$is not reduced the above argument shows only that there is an operator$v _ { q } \in \mathbf { T } _ { \mathfrak { m } } ^ { \mathrm { t r } }$such that$( U _ { q } - v _ { q } )$is nilpotent. Now${ \mathbf { T } } _ { H } ( N q ^ { r } )$can be viewed as a ring of endomorphisms of$S _ { 2 } ( \Gamma _ { H } ( N q ^ { r } ) )$, the space of cusp forms of weight 2 on$\Gamma _ { H } ( N q ^ { r } )$. There is a restriction map${ \bf T } _ { H } ( N q ^ { r } ) \to { \bf T } _ { H } ( N q ^ { r } )$new where${ \mathbf { T } } _ { H } ( N q ^ { r } ) ^ { \mathrm { n e w } }$is the image of${ \mathbf { T } } _ { H } ( N q ^ { r } )$in the ring of endomorphisms of $S _ { 2 } ( \Gamma _ { H } ( N q ^ { r } ) ) / \dot { S } _ { 2 } ( \Gamma _ { H } ( N q ^ { r } ) ) ^ { \mathrm { o d d } }$, the old part being defined as the sum of two copies of$S _ { 2 } ( \Gamma _ { H } ( N q ^ { r - 1 } ) )$mapped via$z \ \longrightarrow \ z$and$z  q z$. One sees that on m-completions$\mathbf { T } _ { \mathfrak { m } } \simeq ( \mathbf { T } _ { H } ( N q ^ { r } ) ^ { \mathrm { n e w } } ) _ { \mathfrak { m } }$since the conductor of$\rho _ { \mathfrak { m } }$is divisible by $q ^ { r }$. It follows that$U _ { q } \in \mathbf { T } _ { \mathfrak { m } }$satisfies an equation of the form$P ( U _ { q } ) = 0$where $P ( x )$is a polynomial with coeficients in$W ( k _ { \mathfrak { m } } )$and with distinct roots. By extending scalars to O (the integers of a local field containing$W ( k _ { \mathfrak { m } } ) )$we can assume that the roots lie in$\boldsymbol { T } \simeq \mathbf { T } _ { \mathfrak { m } } \otimes _ { W ( k _ { \mathfrak { m } } ) } \mathcal { O }$

Since$( U _ { q } - v _ { q } )$is nilpotent it follows that$P ( v _ { q } ) ^ { r } = 0$for some r. Then since$v _ { q } \in \mathbf { T } _ { \mathfrak { m } } ^ { \mathrm { t r } }$which is reduced,$P ( v _ { q } ) = 0$. Now consider the map$T \to \Pi T _ { ( \mathfrak { p } ) }$ where the product is taken over the localizations of T at the minimal primes p of$T$. The map is injective since the associated primes of the kernel are all maximal, whence the kernel is of finite cardinality and hence zero. Now in each$T _ { ( \mathfrak { p } ) } , U _ { q } = \alpha _ { i }$and$v _ { q } = \alpha _ { j }$for roots$\alpha _ { i } , \alpha _ { j }$of$P ( x ) = 0$because the roots are distinct. Since$U _ { q } \mathrm { ~ - ~ } v _ { q } \in { \mathfrak { p } }$for each p it follows that$\alpha _ { i } = \alpha _ { j }$for each p whence$U _ { q } = v _ { q }$in each$T _ { ( \mathfrak { p } ) }$. Hence$U _ { q } = v _ { q }$in$T$also and this finally shows that$U _ { q } \in \mathbf { T } _ { \mathfrak { m } } ^ { \mathrm { t r } }$in general.

We can therefore define a principal ideal

$$
(\Delta_ {q}) = (\alpha \circ \widehat {\alpha})
$$

using,as previously, that the rings$\mathbf T _ { H ^ { \prime } } ( N q ^ { r } , q ^ { r + 1 } ) _ { \mathfrak m _ { q } }$and$\mathbf { T } _ { H } ( N q ^ { r } ) _ { \mathfrak { m } }$are Gorenstein. We compute$( \Delta _ { q } )$in a similar manner to the type (A) case, but using this time that$U _ { q } ^ { * } U _ { q } = \stackrel { \textstyle } { q }$on the space of forms on$\Gamma _ { H } ( N q ^ { r } )$which are new at q, i.e., the space spanned by forms$\{ f ( s z ) \}$where$f$runs through newforms with$q ^ { r }$|level f. To see this let f be any newform of level divisible by$q ^ { r }$and observe that the Petersson inner product$\left. ( U _ { q } ^ { * } U _ { q } - q ) f ( r z ) , f ( m z ) \right. = 0$for any$m | ( N q ^ { r } / \mathrm { l e v e l } f )$by [Li, Th. 3(ii)]. This shows that$( U _ { q } ^ { * } U _ { q } \stackrel { , } { - } q ) f ( r z )$ a priori a linear combination of$\{ f ( m _ { i } z ) \}$, is zero. We obtain the following result.

Proposition 2.12. Suppose that m is a maximal ideal of${ \mathbf { T } } _ { H } ( N q ^ { r } )$ associated to an irreducible$\rho _ { \mathfrak { m } }$of type (B) at q, i.e., satisfying (2.19) including the hypothesis that H cantains$S _ { p }$. (Again$q \nmid N p . )$Then

$$
(\Delta_ {q}) = \Big ((q - 1) ^ {2} \Big).
$$

Finally we have the case where$\rho _ { \mathfrak { m } }$is of type (C) at$q .$. We assume then that m is a maximal ideal of${ \mathbf { T } } _ { H } ( N q ^ { r } )$where H contains the Sylow p-subgroup

$S _ { p }$of$( \mathbf { Z } / q ^ { r } \mathbf { Z } ) ^ { * }$and that

$$
H ^ {1} (\mathbf {Q} _ {q}, W _ {\lambda}) = 0\tag{2.20}
$$

where$W _ { \lambda }$is defined as in (1.6) but with$\rho _ { \mathfrak { m } }$replacing$\rho _ { 0 }$, i.e.,$W _ { \lambda } = \mathrm { a d } ^ { 0 } \rho _ { \mathrm { m } }$

This time we let${ \mathfrak { m } } _ { q }$be the inverse image of m in$\mathbf { T } _ { H ^ { \prime } } ( N q ^ { r } )$under the natural restriction map${ \bf \dot { T } } _ { H ^ { \prime } } ( N q ^ { r } ) \longrightarrow { \bf T } _ { H } ( N q ^ { r } )$with$H ^ { \prime }$defined as in the case of type B. We set

$$
(\Delta_ {q}) = (\alpha \circ \hat {\alpha})
$$

where$\alpha : { \bf T } _ { H ^ { \prime } } ( N q ^ { r } ) _ { \mathfrak { m } _ { q } }  { \bf T } _ { H } ( N q ^ { r } ) _ { \mathfrak { m } }$is the induced map on the completions, which as before are Gorenstein rings. The proof of the following proposition is analogous (but simpler) to the proof of Proposition 2.10. (Notice that the proposition does not require the condition that$\rho _ { \mathfrak { m } }$satisfy (2.20) but this is the case in which we will use it.)

Proposition 2.13. Suppose that m is a maximal of${ \mathbf { T } } _ { H } ( N q ^ { r } )$associated to an irreducible$\rho _ { \mathfrak { m } }$with H containing the Sylow p-subgroup of$( \mathbf { Z } / q ^ { r } \mathbf { Z } ) ^ { * }$ Then

$$
(\Delta_ {q}) = (q - 1).
$$

Finally, in this section we state Proposition 2.4 in the case$q \neq p$as this will be used in Chapter 3. Let$q$be a prime,$q \nmid N p$and let$S _ { 1 }$denote the ring

$$
T _ {H} (N) [ U _ {1} ] / \{U _ {1} ^ {2} - T _ {q} U _ {1} + \langle q \rangle q \} \subseteq \mathrm{End} (J _ {H} (N) ^ {2})\tag{2.21}
$$

where$\hat { \varphi } : J _ { H } ( N , q )  J _ { H } ( N ) ^ { 2 }$is the map defined after (2.10) and$U _ { 1 }$is the matrix

$$
\left[ \begin{array}{c c} T _ {q} & - \langle q \rangle \\ q & 0 \end{array} \right].
$$

Thus,$\hat { \varphi } U _ { q } = U _ { 1 } \hat { \varphi }$. Also$\langle q \rangle$is defined as$\langle n _ { q } \rangle$where$n _ { q } \equiv q ( N ) , n _ { q } \equiv 1 ( q )$ Let${ \mathfrak { m } } _ { 1 }$be a maximal ideal of$S _ { 1 }$containing the image of m, where m is a maximal ideal of${ \bf T } _ { H } ( N )$with associated irreducible$\rho _ { \mathfrak { m } }$. We will also assume that$\rho _ { \mathfrak { m } } ( \operatorname { F r o b } q )$has distinct eigenvalues. (We will only need this case and it simplifies the exposition.) Let${ \mathfrak { m } } _ { q }$denote the corresponding maximal ideals of${ \bf T } _ { H } ( N , q )$and${ \bf T } _ { H } ( N q )$under the natural restriction maps${ \bf T } _ { H } ( N q )$ ${ \bf T } _ { H } ( N , q )  S _ { 1 }$. The corresponding maps on completions are

$$
\begin{array}{c} \mathbf {T} _ {H} (N q) _ {\mathfrak {m} _ {q}} \xrightarrow {\beta} \mathbf {T} _ {H} (N, q) _ {\mathfrak {m} _ {q}} \\ \xrightarrow {\alpha} S _ {1, \mathfrak {m} _ {1}} \simeq \mathbf {T} _ {H} (N) _ {\mathfrak {m}} \underset {W (k _ {\mathfrak {m}})} {\otimes} W (k ^ {+}) \end{array}\tag{2.22}
$$

where$k ^ { + }$is the extension of$k _ { \mathfrak { m } }$generated by the eigenvalues of$\{ \rho _ { \mathfrak { m } } ( \mathrm { F r o b } q ) \}$ That$k ^ { + }$is either equal to$k _ { \mathfrak { m } }$or its quadratic extension. The maps$\beta ,$α are surjective, the latter because$T _ { q }$is a trace in the 2-dimensional representation to$\mathrm { G L _ { 2 } } ( \mathbf { T } _ { H } ( N ) _ { \mathfrak { m } } )$given after Theorem 2.1 and hence is ‘redundant’ by the Cebotarev density theorem. The completions are Gorenstein by Corollary 2 to <sup>ˇ</sup> Theorem 2.1 and so we define invariant ideals of$S _ { 1 , \mathfrak { m } _ { 1 } }$

$$
(\Delta) = (\alpha \circ \hat {\alpha}), \quad (\Delta^ {\prime}) = (\alpha \circ \beta) \circ (\widehat {\alpha \circ \beta}).\tag{2.23}
$$

Let$\alpha _ { q }$be the image of$U _ { 1 }$in$\mathbf { T } _ { H } ( N ) _ { \mathfrak { m } } \bigotimes _ { W ( k _ { \mathfrak { m } } ) } W ( k ^ { + } )$under the last isomorphism in (2.22). The proof of Proposition 2.4 yields

Proposition 2.4<sup></sup>. Suppose that$\rho _ { m }$is irreducible where m is a maximal ideal of${ \bf T } _ { H } ( N )$and that$\rho _ { \mathrm { m } } ( \mathrm { F r o b } q )$has distinct eigenvalues. Then

$$
\begin{array}{r l} & {(\Delta) = (\alpha_ {q} ^ {2} - \langle q \rangle),} \\ & {(\Delta^ {\prime}) = (\alpha_ {q} ^ {2} - \langle q \rangle) (q - 1).} \end{array}
$$

Remark. Note that if we suppose also that$q \equiv 1 ( p )$then$( \Delta )$is the unit ideal and$\alpha$is an isomorphism in (2.22).

## 3. The main conjectures

As we suggested in Chapter 1, in order to study the deformation theory of$\rho _ { 0 }$in detail we need to assume that it is modular. That this should always be so for det$\rho _ { 0 }$odd was conjectured by Serre. Serre also made a conjecture (the ‘ε’-conjecture) making precise where one could find a lifting of$\rho _ { 0 }$once one assumed it to be modular (cf. [Se]). This has now been proved by the combined eforts of a number of authors including Ribet, Mazur, Carayol, Edixhoven and others. The most dificult step was to show that if$\rho _ { 0 }$was unramified at a prime l then one could find a lifting in which l did not divide the level. This was proved (in slightly less generality) by Ribet. For a precise statement and complete references we refer to Diamond’s paper [Dia] which removed the last restrictions referred to in Ribet’s survey article [Ri3]. The following is a minor adaptation of the epsilon conjecture to our situation which can be found in [Dia, Th. 6.4]. (We wish to use weight 2 only.) Let$N ( \rho _ { 0 } )$be the prime to$p$part of the conductor of$\rho _ { 0 }$as defined for example in [Se].

Theorem 2.14. Suppose that$\rho _ { 0 }$is modular and satisfies (1.1) (so in particular is irreducible) and is of type$\mathcal { D } = ( \cdot , \Sigma , \mathcal { O } , \mathcal { M } )$with · = Se, str or fl. Suppose that at least one of the following conditions holds$\mathrm { ( i ) } \ p > 3 \ o r \ \mathrm { ( i i ) } \ \rho _ { 0 }$ is not induced from a character of$\mathbf { Q } ( { \sqrt { - 3 } } )$. Then there exists a newform f of weight 2 and a prime$\lambda$of${ \mathcal { O } } _ { f }$such that$\rho _ { f , \lambda }$is of type$\mathcal { D } ^ { \prime } = ( \cdot , \Sigma , \mathcal { O } ^ { \prime } , \mathcal { M } )$ for some$\mathcal { O } ^ { \prime }$, and such that$\left( \rho _ { f , \lambda } { \bmod { \lambda } } \right) \simeq \rho _ { 0 }$over${ \overline { { \mathbf { F } } } } _ { p } .$. Moreover we can assume that f has character$\chi _ { f }$of order prime to p and has level$N ( \rho _ { 0 } ) p ^ { \delta ( \rho _ { 0 } ) }$ where$\delta ( \rho _ { 0 } ) = 0 ~ i f ~ \rho _ { 0 } | _ { D _ { p } }$is associated to a finite flat group scheme over$\mathbf { Z } _ { p }$ and det$\rho _ { 0 } \Big \vert _ { I _ { p } } = \omega$, and$\delta ( \rho _ { 0 } ) = 1$otherwise. Furthermore in the Selmer case we can assume that$a _ { p } ( f ) \equiv \chi _ { 2 } ( \operatorname { F r o b } p )$mod λ in the notation of (1.2) where $a _ { p } ( f )$is the eigenvalue of$U _ { p }$.

For the rest of this chapter we will assume that$\rho _ { 0 }$is modular and that if$p = 3$then$\rho _ { 0 }$is not induced from a character of$\mathbf { Q } ( { \sqrt { - 3 } } )$. Here and in the rest of the paper we use the term ‘induced’ to signify that the representation is induced after an extension of scalars to the algebraic closure.

For each$\mathcal { D } = \{ \cdot , \Sigma , \mathcal { O } , \mathcal { M } \}$we will now define a Hecke ring$\mathbf { T } _ { \mathcal { D } }$except where · is unrestricted. Suppose first that we are in the flat, Slemer or strict cases. Recall that when referring to the flat case we assume that$\rho _ { 0 }$is not ordinary and that det$\rho _ { 0 } | _ { I _ { p } } = \omega$. Suppose that$\Sigma = \{ q _ { i } \}$and that$N ( \rho _ { 0 } ) =$ $\Pi q _ { i } ^ { s _ { i } }$with$s _ { i } \geq 0$. If$U _ { \lambda } \simeq k ^ { 2 }$is the representation space of$\rho _ { 0 }$we set${ n _ { q } } ~ =$ dim$\mathfrak { u } _ { k } ( U _ { \lambda } ) ^ { I _ { q } }$where$I _ { q }$in the inertia group at$q .$Define$M _ { 0 }$and M by

$$
M_{0} = N(\rho_{0})\prod_{\substack{n_{q_{i}} = 1\\ q_{i}\not\in\mathcal{M}\cup \{p\}}}q_{i}\cdot \prod_{n_{q_{i}} = 2}q_{i}^{2},\quad M = M_{0}p^{\tau (\rho_{0})}\tag{2.24}
$$

where$\tau ( \rho _ { 0 } ) = 1$if$\rho _ { 0 }$is ordinary and$\tau ( \rho _ { 0 } ) = 0$otherwise. Let H be the subgroup of$( \mathbf { Z } / M \mathbf { Z } ) ^ { * }$generated by the Sylow p-subgroup of$( \mathbf { Z } / q _ { i } \mathbf { Z } ) ^ { * }$for each $q _ { i } \in \mathcal { M }$as well as by all of$( \mathbf { Z } / q _ { i } \mathbf { Z } ) ^ { * }$for each$q _ { i } \in \mathcal { M }$of type (A). Let$\mathbf { T } _ { H } ^ { \prime } ( M )$ denote the ring generated by the standard Hecke operators$\{ T _ { l }$for$l \dag { M p , \langle a \rangle }$ for$( a , M p ) = 1 \}$. Let${ \mathfrak { m } } ^ { \prime }$denote the maximal ideal of$\mathbf { T } _ { H } ^ { \prime } ( M )$associated to the $f$and λ given in the theorem and let$k _ { \mathfrak { m ^ { \prime } } }$be the residue field$\mathbf { T } _ { H } ^ { \prime } ( M ) / \mathfrak { m }$. Note that m<sup></sup> does not depend on the particular choice of pair$( f , \lambda )$in theorem 2.14. Then$k _ { \mathfrak { m ^ { \prime } } } \simeq k _ { 0 }$where$k _ { 0 }$is the smallest possible field of definition for$\rho _ { 0 }$because $k _ { \mathfrak { m ^ { \prime } } }$is generated by the traces. Henceforth we will identify$k _ { 0 }$with$k _ { \mathfrak { m ^ { \prime } } }$. There is one exceptional case where$\rho _ { 0 }$is ordinary and$\rho _ { 0 } | _ { D _ { p } }$is isomorphic to a sum of two distinct unramified characters$( \chi _ { 1 }$and$\chi _ { 2 }$in the notation of Chapter 1, §1). If$\rho _ { 0 }$is not exceptional we define

$$
\mathbf {T} _ {\mathcal {D}} = \mathbf {T} _ {H} ^ {\prime} (M) _ {\mathfrak {m} ^ {\prime}} \underset {W (k _ {0})} {\otimes} \mathcal {O}.\tag{2.25(a)}
$$

If$\rho _ { 0 }$is exceptional we let$\mathbf { T } _ { H } ^ { \prime \prime } ( M )$denote the ring generated by the operators $\{ T _ { l }$for$l \ \dag \ M p , \langle a \rangle$for$( a , \bar { M } p ) \ : = \ : 1 , U _ { p } \}$. We choose$\mathfrak { m } ^ { \prime \prime }$to be a maximal ideal of$\mathbf { T } _ { H } ^ { \prime \prime } ( M )$lying above m<sup></sup> for which there is an embedding$k _ { \mathfrak { m ^ { \prime \prime } } } \hookrightarrow k$(over $k _ { 0 } = k _ { \mathfrak { m ^ { \prime } } } )$satisfying$U _ { p } \to \chi _ { 2 } ( \mathrm { F r o b } p )$. (Note that$\chi _ { 2 }$is specified by D.) Then in the exceptional case$k _ { \mathfrak { m ^ { \prime \prime } } }$is either$k _ { 0 }$or its quadratic extension and we define

$$
\mathbf {T} _ {\mathcal {D}} = \mathbf {T} _ {H} ^ {\prime \prime} (M) _ {\mathfrak {m} ^ {\prime \prime}} \underset {W (k _ {\mathfrak {m} ^ {\prime \prime}})} {\otimes} \mathcal {O}.\tag{2.25(b)}
$$

The omission of the Hecke operators$U _ { q }$for$q | M _ { 0 }$ensures that$\mathbf { T } _ { \mathcal { D } }$is reduced.

We need to relate$\mathbf { T } _ { \mathcal { D } }$to a Hecke ring with no missing operators in order to apply the results of Section 1.

Proposition 2.15. In the nonexceptional case there is a maximal ideal m for${ \bf T } _ { H } ( M )$with m$\cap _ { H } ^ { \prime } \left( M \right) = \mathfrak { m } ^ { \prime }$and$k _ { 0 } = k _ { \mathfrak { m } }$, and such that the natural map$\mathbf { T } _ { H } ^ { \prime } ( M ) _ { \mathfrak { m ^ { \prime } } } \to \mathbf { T } _ { H } ( M ) _ { \mathfrak { m } }$is an isomorphism, thus given

$$
\mathbf {T} _ {\mathcal {D}} \simeq \mathbf {T} _ {H} (M) _ {\mathfrak {m}} \underset {W (k _ {0})} {\otimes} \mathcal {O}.
$$

In the exceptional case the same statements hold with$\mathfrak { m } ^ { \prime \prime }$replacing m<sup></sup>,$\mathbf { T } _ { H } ^ { \prime \prime } ( M )$ replacing$\mathbf { T } _ { H } ^ { \prime } ( M )$and$k _ { \mathfrak { m ^ { \prime \prime } } }$replacing$k _ { 0 }$

Proof. For simplicity we describe the nonexceptional case indicating where appropriate the slight modifications needed in the exceptional case. To construct m we take the eigenform$f _ { 0 }$obtain from the newform$f$of Theorem 2.14 by removing the Euler factors at all primes$q \in \Sigma - \{ \mathcal { M } \cup p \}$. If$\rho _ { 0 }$is ordinary and$f$has level prime to$p$we also remove the Euler factor$\left( 1 - \beta _ { p } \cdot p ^ { - s } \right)$where $\beta _ { p }$is the non-unit eigenvalue in$\mathcal { O } _ { f \lambda }$. (By ‘removing Euler factors’ we mean take the eigenform whose L-series is that of$f$with these Euler factors removed.) Then$f _ { 0 }$is an eigenform of weight 2 on$\Gamma _ { H } ( M )$(this is ensured by the choice of$f )$with$\mathcal { O } _ { f , \lambda }$coeficients. We have a corresponding homomorphism $\pi _ { f _ { 0 } } : { \bf T } _ { \cal H } ( { \cal M } )  { \cal O } _ { f , \lambda }$and we let$\mathfrak { m } = \pi _ { f _ { 0 } } ^ { - 1 } ( \lambda )$

Since the Hecke operators we have used to generate$\mathbf { T } _ { H } ^ { \prime } ( M )$are prime to the level these is an inclusion with finite index

$$
\mathbf {T} _ {H} ^ {\prime} (M) \hookrightarrow \prod \mathcal {O} _ {g}
$$

where$g$runs over representatives of the Galois conjugacy classes of newforms associated to$\Gamma _ { H } ( M )$and where we note that by multiplicity one${ \mathcal { O } } _ { g }$can also be described as the ring of integers generated by the eigenvalues of the operators in$\mathbf { T } _ { H } ^ { \prime } ( M )$acting on$g .$. If we consider${ \bf T } _ { H } ( M )$in place of$\mathbf { T } _ { H } ^ { \prime } ( M )$we get a similar map but we have to replace the ring${ \mathcal { O } } _ { g }$by the ring

$$
S _ {g} = \mathcal {O} _ {g} [ X _ {q _ {1}}, \ldots , X _ {q _ {r}}, X _ {p} ] / \{Y _ {i}, Z _ {p} \} _ {i = 1} ^ {r}
$$

where$\{ p , p _ { 1 } , \ldots , q _ { r } \}$are the distinct primes dividing$M p$. Here

$$
Y _ {i} = \left\{ \begin{array}{l l} X _ {q _ {i}} ^ {r _ {i} - 1} \Big (X _ {q _ {i}} - \alpha_ {q _ {i}} (g) \Big) \Big (X _ {q _ {i}} - \beta_ {q _ {i}} (g) \Big) & \text { if } q _ {i} \nmid \text { level } (g) \\ X _ {q _ {i}} ^ {r _ {i}} \Big (X _ {q _ {i}} - a _ {q _ {i}} (g) \Big) & \text { if } q _ {i} | \text { level } (g), \end{array} \right.\tag{2.26}
$$

where the Euler factor of$g$at$q _ { i } \quad ( \mathrm { i . e . , }$of its associated L-series) is $( 1 - \alpha _ { q _ { i } } ( g ) q _ { i } ^ { - s } ) ( 1 - \beta _ { q _ { i } } ( g ) q _ { i } ^ { - s } )$in the first cases and$( 1 - a _ { q _ { i } } ( g ) q _ { i } ^ { - s } )$in the second case, and$q _ { i } ^ { r _ { i } } | | \Big ( M / \mathrm { l e v e l } ( g ) \Big )$. (We allow$a _ { q _ { i } } ( g )$to be zero here.) Similarly$Z _ { p }$is

defined by

$$
Z _ {p} = \left\{ \begin{array}{l l} X _ {p} ^ {2} - a _ {p} (g) X _ {p} + p \chi_ {g} (p) & \text {if} p | M, p \nmid \text {level} (g) \\ X _ {p} - a _ {p} (g) & \text {if} p \nmid M \\ X _ {p} - a _ {p} (g) & \text {if} p | \text {level} (g), \end{array} \right.
$$

where the Euler factor of$g$at$p$is$( 1 - a _ { p } ( g ) p ^ { - s } + \chi _ { g } ( p ) p ^ { 1 - 2 s } )$in the first two cases and$( 1 - a _ { p } ( g ) p ^ { - s } )$in the third case. We then have a commutative diagram

$$
\begin{array}{c c c} \mathbf {T} _ {H} ^ {\prime} (M) & \hookrightarrow & \prod_ {g} \mathcal {O} _ {g} \\ \bigcap & & \bigcap \\ \mathbf {T} _ {H} (M) & \hookrightarrow & \prod_ {g} S _ {g} = \prod_ {g} \mathcal {O} _ {g} [ X _ {q _ {1}}, \ldots , X _ {q _ {r}}, X _ {p} ] / \{Y _ {i}, Z _ {p} \} _ {i = 1} ^ {r} \end{array}\tag{2.27}
$$

where the lower map is given on$\{ U _ { q } , U _ { p }$or$T _ { p } \}$by$U _ { q _ { i } } \longrightarrow X _ { q _ { i } } , U _ { p }$or $T _ { p } \longrightarrow X _ { p }$(according as$p | M$or$p \nmid M )$. To verify the existence of such a homomorphism one considers the action of${ \bf T } _ { H } ( M )$on the space of forms of weight 2 invariant under$\Gamma _ { H } ( M )$and uses that$\textstyle \sum _ { j = 1 } ^ { r } g _ { j } ( m _ { j } z )$is a free generator as a$\mathbf { T } _ { H } ( M ) \otimes \mathbf { C } .$-module where$\{ g _ { j } \}$runs over the set of newforms and $m _ { j } = M / \mathrm { l e v e l } ( g _ { j } )$

Now we tensor all the rings in (2.27) with$\mathbf { Z } _ { p }$. Then completing the top row of (2.27) with respect to${ \mathfrak { m } } ^ { \prime }$and the bottom row with respect to m we get a commutative diagram

$$
\begin{array}{c c c c c} \mathbf {T} _ {H} ^ {\prime} (M) _ {\mathfrak {m} ^ {\prime}} & \subset \longrightarrow & \Bigl (\prod_ {g} \mathcal {O} _ {g} \Bigr) _ {\mathfrak {m} ^ {\prime}} & \simeq & \prod_ {\substack {g \\ \mathfrak {m} ^ {\prime} \to \mu}} \mathcal {O} _ {g, \mu} \\ \Biggl \downarrow & & \Biggl \downarrow & & \Biggl \downarrow \\ \mathbf {T} _ {H} (M) _ {\mathfrak {m}} & \subset \longrightarrow & \Bigl (\prod_ {g} S _ {g} \Bigr) _ {\mathfrak {m}} & \simeq & \prod (S _ {g}) _ {\mathfrak {m}}. \end{array}\tag{2.28}
$$

Here$\mu$runs through the primes above$p$in each${ \mathcal { O } } _ { g }$for which${ \mathfrak { m } } ^ { \prime } \to \mu$under ${ \bf T } _ { H ^ { \prime } } ( M ) \to { \mathcal O } _ { g }$. Now$( S _ { g } ) _ { \mathfrak { m } }$is given by

$$
\begin{array}{l} (S _ {g} \otimes \mathbf {Z} _ {p}) _ {\mathfrak {m}} \simeq \Big ((\mathcal {O} _ {g} \otimes \mathbf {Z} _ {p}) [ X _ {q _ {1}}, \ldots , X _ {q _ {r}}, X _ {p} ] / \{Y _ {i}, Z _ {p} \} _ {i = 1} ^ {r} \Big) _ {\mathfrak {m}} \\ \qquad \simeq \left(\prod_ {\mu | p} \mathcal {O} _ {g, \mu} [ X _ {q _ {1}}, \ldots , X _ {q _ {r}}, X _ {p} ] / \{Y _ {i}, Z _ {p} \} _ {i = 1} ^ {r}\right) _ {\mathfrak {m}} \\ \qquad \simeq \left(\prod_ {\mu | p} A _ {g, \mu}\right) _ {m} \end{array}\tag{2.29}
$$

where$A _ { g , \mu }$denotes the product of the factors of the complete semi-local ring $\mathcal { O } _ { g , \mu } [ X _ { q _ { 1 } } , \dots , X _ { q _ { r } } , X _ { p } ] / \{ Y _ { i } , Z _ { p } \} _ { i = 1 } ^ { r }$in which$X _ { q _ { i } }$is topologically nilpotent for $q _ { i } \notin \mathcal { M }$and in which$X _ { p }$is a unit if we are in the ordinary case$( { \mathrm { i . e . } }$, when $p | M )$. This is because$\bar { U _ { q _ { i } } } \in \mathfrak { m i f } q _ { i } \notin \mathcal { M }$and$U _ { p }$is a unit at m in the ordinary case.

Now if${ \mathfrak { m } } ^ { \prime } \to \mu$then in$( A _ { g , \mu } ) _ { \mu }$we claim that$Y _ { i }$is given up to a unit by $X _ { q _ { i } } - b _ { i }$for some$b _ { i } \in { \mathcal { O } } _ { g , \mu }$with$b _ { i } = 0 \mathrm { i f } q _ { i } \notin \mathcal { M }$. Similarly$Z _ { p }$is given up to a unit by$X _ { p } - \alpha _ { p } ( g )$where$\alpha _ { p } ( g )$is the unit root of$x ^ { 2 } - a _ { p } ( g ) \dot { x } + p \chi _ { g } ( p ) = 0$in ${ \mathcal { O } } _ { g , \mu }$if$p \nmid$level g and$p | M$and by$X _ { p } \mathrm { ~ - ~ } a _ { p } ( g )$if p|level g or$p \nmid M$This will show that$( A _ { g , \mu } ) _ { \mathfrak { m } } \simeq \mathcal { O } _ { g , \mu }$when${ \mathfrak { m } } ^ { \prime } \to \mu$and$( A _ { g , \mu } ) _ { \mathfrak { m } } = 0$otherwise.

For$q _ { i } \in \mathcal { M }$and for p, the claim is straightforward. For$q _ { i } \notin \mathcal { M }$, it amounts to the following. Let$U _ { g , \mu }$denote the 2-dimensional$K _ { g , \mu ^ { - } \mathrm { v e c t o r } }$space with Galois action via$\rho _ { g , \mu }$and let$n _ { q _ { i } } ( g , \mu ) = \dim ( U _ { g , \mu } ) ^ { I _ { q _ { i } } }$. We wish to check that $Y _ { i } = \mathrm { u n i t . } X _ { q _ { i } }$in$( A _ { g , \mu } ) _ { \mathfrak { m } }$and from the definition of$Y _ { i }$in (2.26) this reduces to checking that$r _ { i } = n _ { q _ { i } } ( g , \mu )$by the$\pi _ { q } \simeq \pi ( \sigma _ { q } )$of theorem (cf. [Ca1]). We use here that$\alpha _ { q _ { i } } ( g ) , \beta _ { q _ { i } } ( g )$and$a _ { q _ { i } } ( g )$are p-adic units when they are nonzero since they are eigenvalues of Frob$( q _ { i } )$. Now by definition the power of$q _ { i }$dividing M is the same as that dividing$\dot { N ( \rho _ { 0 } ) } q _ { i } ^ { n _ { q _ { i } } }$(cf. (2.21)). By an observation of Livn´e (cf. [Liv], [Ca2,§1]),

$$
\operatorname{ord} _ {q _ {i}} (\text { level } g) = \operatorname{ord} _ {q _ {i}} \left(N (\rho_ {0}) q _ {i} ^ {n _ {q _ {i}} - n _ {q _ {i}} (g, \mu)}\right).\tag{2.30}
$$

As by definition$q _ { i } ^ { r _ { i } } | | ( M / \mathrm { l e v e l } g )$we deduce that$r _ { i } = n _ { q _ { i } } ( g , \mu )$as reqired.

We have now shown that each$A _ { g , \mu } \simeq \mathcal { O } _ { g , \mu }$(when${ \mathfrak { m } } ^ { \prime } \to \mu )$and it follows from (2.28) and (2.29) that we have homomorphisms

$$
\mathbf{T}^{\prime}_{H}(M)_{\mathfrak{m}^{\prime}}\hookrightarrow \mathbf{T}_{H}(M)_{\mathfrak{m}}\hookrightarrow \prod_{\substack{g\\ \mathfrak{m}^{\prime}\to \mu}}\mathcal{O}_{g,\mu}
$$

where the inclusions are of finite index. Moreover we have seen that$U _ { q _ { i } } = 0$ in$\mathbf { T } _ { H } ( M ) _ { \mathfrak { m } }$for$q _ { i } ~ \notin ~ { \mathcal { M } }$. We now consider the primes$q _ { i } ~ \in ~ { \mathcal { M } }$. We have to show that the operators$U _ { q }$for$q \in { \mathcal { M } }$are redundant in the sense that they lie in$\mathrm { \bf T } _ { H } ^ { \prime } ( M ) _ { \mathrm { m ^ { \prime } } } , \mathrm { i . e . }$, in the$\mathbf { Z } _ { p }$-subalgebra of$\mathbf { T } _ { H } ( M ) _ { \mathfrak { m } }$generated by the $\{ T _ { l } : l \mathbin { \stackrel {  } { \cdot } } M p , \langle a \rangle : a \in ( \mathbf { Z } / M \mathbf { Z } ) ^ { * } \}$. For$q \in \mathcal { M }$of type (A),$U _ { q } \in \mathbf { T } _ { H } ^ { \prime } ( M ) _ { \mathfrak { m } ^ { \prime } }$ as explained in Remark 2.9 are for$q \in { \mathcal { M } }$of type (B),$U _ { q } \in \mathbf { T } _ { H } ^ { \prime } ( M ) _ { \mathfrak { m } ^ { \prime } }$as explained in Remark 2.11. For$q \in \mathcal { M }$of type (C) but not of type$( \mathrm { A } ) , U _ { q } = 0$ by the$\pi _ { q } \simeq \pi ( \sigma _ { q } )$theorem (cf. [Ca1]). For in this case$n _ { q } = 0$whence also $n _ { q } ( g , \mu ) = 0$for each pair$( g , \mu )$with${ \mathfrak { m } } ^ { \prime } \to \mu . { \mathrm { ~ H ~ } } \rho _ { 0 }$is strict or Selmer at$p$then $U _ { p }$can be recovered from the two-dimensional representation$\rho$(described after the corollaries to Theorem 2.1) as the eigenvalue of Frobp on the (free, of rank one) unramified quotient (cf. Theorem 2.1.4 of [Wi4]). As this representation is defined over the$\mathbf { Z } _ { p }$-subalgebra generated by the traces, it follows that$U _ { p }$ is contained in this subring. In the exceptional case$U _ { p }$is in$\mathbf { T } _ { H } ^ { \prime \prime } ( M ) _ { \mathfrak { m } ^ { \prime \prime } }$by definition.

Finally we have to show that$T _ { p }$is also redundant in the sense explained above when$p \nmid M$. A proof of this has already been given in Section 2 (Ribet’s lemma). Here we give an alternative argument using the Galois representations. We know that$T _ { p } \in \mathfrak { m }$and it will be enough to show that$T _ { p } \in ( \mathfrak { m } ^ { 2 } , p )$ Writing$k _ { \mathfrak { m } }$for the residue field${ \bf T } _ { H } ( M ) _ { \mathfrak { m } } / \mathfrak { m }$we reduce to the following situation. If$T _ { p } \notin ( \mathfrak { m } ^ { 2 } , p )$then there is a quotient

$$
\mathbf {T} _ {H} (M) _ {\mathfrak {m}} / (\mathfrak {m} ^ {2}, p) \twoheadrightarrow k _ {\mathfrak {m}} [ \varepsilon ] = \mathbf {T} _ {H} (M) _ {\mathfrak {m}} / \mathfrak {a}
$$

where$k _ { \mathfrak { m } } [ \varepsilon ]$is the ring of dual numbers$( \operatorname { s o } \ \varepsilon ^ { 2 } = 0 )$with the property that $T _ { p } \mapsto \lambda \varepsilon$with$\lambda \neq 0$and such that the image of$\mathbf { T } _ { H } ^ { \prime } ( M ) _ { \mathfrak { m } ^ { \prime } }$- lies in$k _ { \mathfrak { m } }$. Let$G _ { / \mathbf { Q } }$ denote the four-dimensional$k _ { \mathfrak { m } }$-vector space associated to the representation

$$
\rho_ {\varepsilon}: \operatorname{Gal} (\overline {{\mathbf {Q}}} / \mathbf {Q}) \longrightarrow \operatorname{GL} _ {2} (k _ {\mathfrak {m}} [ \varepsilon ])
$$

induced from the representation in Theorem 2.1. It has the form

$$
G _ {/ \mathbf {Q}} \simeq G _ {0 / \mathbf {Q}} \oplus G _ {0 / \mathbf {Q}}
$$

where$G _ { 0 }$is the corresponding space associated to$\rho _ { 0 }$by our hypothesis that the traces lie in$k _ { \mathfrak { m } }$. The semisimplicity of$G _ { / \mathbf { Q } }$here is obtained from the main theorem of [BLR]. Now$G _ { / \mathbf { Q } _ { p } }$extends to a finite flat group scheme$G _ { / \mathbf { Z } _ { p } }$ Explicitly it is a quotient of the group scheme$J _ { H } ( M ) _ { \mathfrak { m } } [ p ] _ { / \mathbf { Z } _ { p } }$. Since extensions to$\mathbf { Z } _ { p }$are unique (cf. [Ray1]) we know

$$
G _ {/ \mathbf {Z} _ {p}} \simeq G _ {0 / \mathbf {Z} _ {p}} \oplus G _ {0 / \mathbf {Z} _ {p}}.
$$

Now by the Eichler-Shimura relation we know that in$J _ { H } ( M ) _ { / \mathbf { F } _ { p } }$

$$
T _ {p} = F + \langle p \rangle F ^ {T}.
$$

Since$T _ { p } \in$m it follows that$F + \langle p \rangle F ^ { T } = 0$on$G _ { 0 / \mathbf { F } _ { \tau } }$and hence the same holds on$G _ { / \mathbf { F } _ { p } }$. But$T _ { p }$is an endomorphism of$G _ { / \mathbf { Z } _ { p } }$which is zero on the special fibre, so by [Ray1, Cor. 3.3.6],$T _ { p } = 0$on$G _ { / \mathbf { Z } _ { p } }$. It follows that$T _ { p } = 0$in$k _ { \mathfrak { m } } [ \varepsilon ]$ which contradicts our earlier hypothesis. So$T _ { p } \in ( \mathfrak { m } ^ { 2 } , p )$as required. This completes the proof of the proposition.

From the proof of the proposition it is also clear that m is the unique maximal ideal of${ \bf T } _ { H } ( M )$extending${ \mathfrak { m } } ^ { \prime }$and satisfying the conditions that$U _ { q } \in \mathfrak { m }$ for$q \in \Sigma - \{ \mathcal { M } \cup p \}$and$U _ { p } \notin \mathfrak { m i f } \rho _ { 0 }$is ordinary. For the rest of this chapter we will always make this choice of m (given$\rho _ { 0 } )$

Next we define$\mathbf { T } _ { \mathcal { D } }$in the case when$\mathcal { D } = ( \mathrm { o r d } , \Sigma , \mathcal { O } , \mathcal { M } )$. If n is any ordinary maximal ideal (i.e.$U _ { p } \notin \mathfrak { n } )$of${ \bf T } _ { H } ( N p )$with N prime to$p$then Hida has constructed a 2-dimensional Noetherian local Hecke ring

$$
\mathbf {T} _ {\infty} = e \mathbf {T} _ {H} (N p ^ {\infty}) _ {\mathfrak {n}} := \varprojlim e \mathbf {T} _ {H} (N p ^ {r}) _ {\mathfrak {n} _ {r}}
$$

which is a$\Lambda = \mathbf { Z } _ { p } [ [ T ] ]$-algebra satisfying${ \bf T } _ { \infty } / T \simeq { \bf T } _ { H } ( N p ) _ { \mathfrak { n } }$. Here${ \mathfrak { n } } _ { r }$is the inverse image of n under the natural restriction map. Also$T = \operatorname* { l i m } \langle 1 + N p \rangle - 1$ and$e \ = \ \varinjlim _ { r } U _ { p } ^ { r ! }$. For an irreducible$\rho _ { 0 }$of type$\mathcal { D }$we have defined$\mathbf { T } _ { \mathcal { D } ^ { \prime } }$in (2.25(a)), where$\mathcal { D } ^ { \prime } = ( \mathrm { S e } , \Sigma , \mathcal { O } , \mathcal { M } )$by

$$
\mathbf {T} _ {\mathcal {D} ^ {\prime}} \simeq \mathbf {T} _ {H} (M _ {0} p) _ {\mathfrak {m}} \underset {W (k _ {\mathfrak {m}})} {\otimes} \mathcal {O},
$$

the isomorphism coming from Proposition 2.15. We will define$\mathbf { T } _ { \mathcal { D } }$by

$$
\mathbf {T} _ {\mathcal {D}} = e \mathbf {T} _ {H} (M _ {0} p ^ {\infty}) _ {\mathfrak {m}} \underset {W (k _ {\mathfrak {m}})} {\otimes} \mathcal {O}.\tag{2.31}
$$

In particular we see that

$$
\mathbf {T} _ {\mathcal {D}} / T \simeq \mathbf {T} _ {\mathcal {D} ^ {\prime}},\tag{2.32}
$$

i.e., where$\mathcal { D } ^ { \prime }$is the same as D but with ‘Selmer’ replacing ‘ord’. Moreover if q is a height one prime ideal of$\mathbf { T } _ { \mathcal { D } }$containing$\Big ( ( 1 + T ) ^ { p ^ { n } } - ( 1 + N p ) ^ { p ^ { n } ( k - 2 ) } \Big )$ for any integers$n \geq 0 , k \geq 2$, then$\mathbf { T } _ { \mathcal { D } } / \mathfrak { q }$is associated to an eigenform in a natural way (generalizing the case$n = 0 , k = 2 )$. For more details about these rings as well as about Λ-adic modular forms see for example [Wi1] or [Hi1].

For each$n \geq 1$let$\mathbf { T } _ { n } = \mathbf { T } _ { H } ( M _ { 0 } p ^ { n } ) _ { \mathfrak { m } _ { n } }$Then by the argument given after the statement ofTheorem 2.1 we can construct a Galois representation$\rho _ { n }$ unramified outside$M p$with values in${ \mathrm { G L } } _ { 2 } ( \mathbf { T } _ { n } )$satisfying trace$\rho _ { n } ( \mathrm { F r o b } l ) = T _ { l } .$ det$\rho _ { n } ( \mathrm { F r o b } l ) = l \langle l \rangle$for$( l , M p ) = 1$. These representations can be patched together to give a continuous representation

$$
\rho = \varprojlim \rho_ {n}: \operatorname{Gal} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}) \longrightarrow \operatorname{GL} _ {2} (\mathbf {T} _ {\mathcal {D}})\tag{2.33}
$$

where$\Sigma$is the set of primes dividing$M p$. To see this we need to check the commutativity of the maps

$$
\begin{array}{c} R _ {\Sigma} \longrightarrow \mathbf {T} _ {n} \\ \searrow \quad \downarrow \\ \mathbf {T} _ {n - 1} \end{array}
$$

where the horizontal maps are induced by$\rho _ { n }$and$\rho _ { n - 1 }$and the vertical map is the natural one. Now the commutativity is valid on elements of$R _ { \Sigma }$, which are traces or determinants in the universal representation, since trace$( \mathrm { F r o b } l ) \mapsto T _ { l }$ under both horizontal maps and similarly for determinants. Here$R _ { \Sigma }$is the universal deformation ring described in Chapter 1 with respect to$\rho _ { 0 }$viewed with residue field$k = k _ { \mathfrak { m } }$. It sufices then to show that$R _ { \Sigma }$is generated (topologically) by traces and this reduces to checking that there are no nonconstant deformations of$\rho _ { 0 }$to$k [ \varepsilon ]$with traces lying in k (cf. [Ma1, §1.8]). For then if$R _ { \Sigma } ^ { \mathrm { t r } }$ denotes the closed$W ( k )$-subalgebra of$R _ { \Sigma }$generated by the traces we see that $R _ { \Sigma } ^ { \mathrm { t r } }  ( R _ { \Sigma } / m ^ { 2 } )$is surjective, m being the maximal ideal of$R _ { \Sigma }$, from which we easily conclude that$R _ { \Sigma } ^ { \mathrm { t r } } = R _ { \Sigma }$. To see that the condition holds, assume that a basis is chosen so that$\rho _ { 0 } ( c ) = ( \ O _ { 0 } ^ { 1 } - 1 )$for a chosen complex cunjugation c and$\rho _ { 0 } ( \sigma ) = ( \begin{array} { l } { a _ { \sigma } \ b _ { \sigma } } \\ { c _ { \sigma } \ d _ { \sigma } } \end{array} )$with$b _ { \sigma } = 1$and$c _ { \sigma } \neq 0$for some$\sigma$. (This is possible because$\rho _ { 0 }$is irreducible.) Then any deformation$[ p ]$to$k [ \varepsilon ]$can be represented by a representation$\rho$such that$\rho ( c )$and$\rho ( \sigma )$have the same properties. It follows easily that if the traces of$\rho$lie in k then$\rho$takes values in k whence it is equal to$\rho _ { 0 }$. (Alternatively one sees that the universal representation can be defined over$R _ { \Sigma } ^ { \mathrm { t r } }$by diagonalizing complex conjugation as before. Since the two maps$R _ { \Sigma } ^ { \mathrm { t r } }  \mathbf { T } _ { n - 1 }$induced by the triangle are the same, so the associated representations are equivalent, and the universal property then implies the commutativity of the triangle.)

The representations (2.33) were first exhibited by Hida and were the original inspiration for Mazur’s deformation theory.

For each$\mathcal { D } = \{ \cdot , \Sigma , \mathcal { O } , \mathcal { M } \}$where · is not unrestricted there is then a canonical surjective map

$$
\varphi_ {\mathcal {D}}: R _ {\mathcal {D}} \to \mathbf {T} _ {\mathcal {D}}
$$

which induces the representations described after the corollaries to Theorem 2.1 and in (2.33). It is enough to check this when$\mathcal { O } = W ( k _ { 0 } )$(or$W ( k _ { \mathfrak { m } ^ { \prime \prime } } )$in the exceptional case). Then one just has to check that for every pair$( g , \mu )$which appears in (2.28) the resulting representation is of type D. For then we claim that the image of the canonical map$R _ { \mathcal { D } }  \widetilde { { \bf T } _ { \mathcal { D } } } = \Pi \mathcal { O } _ { g , \mu }$is$\mathbf { T } _ { \mathcal { D } }$where here$\sim$ denotes the normalization. (In the case where · is ord this needs to be checked instead for$\mathbf { T } _ { n } \bigotimes _ { W ( k _ { 0 } ) } \mathcal { O }$for each$n . )$For this we just need to see that$R _ { \mathcal { D } }$is generated by traces. (In the exceptional case we have to show also that$U _ { p }$is in the image. This holds because it can be identified, using Theorem 2.1.4 of [Wi1], with the image of$u \in R _ { D }$where u is the eigenvalue of Frob p on the unique rank one unramified quotient of$R _ { \mathcal { D } } ^ { 2 }$with eigenvalue$\equiv \chi _ { 2 } ( \mathrm { F r o b } p )$which is specified in the definition of$\mathcal { D } . )$But we saw above that this was true for $R _ { \Sigma }$. The same then holds for$R _ { \mathcal { D } }$as$R _ { \Sigma }  R _ { \cal D }$is surjective because the map on reduced cotangent spaces is surjective (cf. (1.5)). To check the condition on the pairs$( g , \mu )$observe first that for$q \in \mathcal { M }$we have imposed the following conditions on the level and character of such$g \mathrm { ^ s }$by our choice of M and H:

$q$of type (A): q|| level g, det$\rho _ { g , \mu } \Big | _ { I _ { q } } = 1$

q of type (B): cond$\chi _ { q } | |$level g, det$\rho _ { g , \mu } \Big | _ { I _ { q } } = \chi _ { q } ,$

q of type (C): det$\rho _ { g , \mu } \Big | _ { I _ { q } }$is the Teichm¨uller lifting of det$\rho _ { 0 } \bigg \vert _ { I _ { q } }$

In the first two cases the desired form of$\rho _ { q , \mu } \Big | _ { D _ { q } }$then follows from the $\pi _ { q } \simeq \pi ( \sigma _ { q } )$theorem of Langlands (cf. [Ca1]). The third case is already of type (C). For$q = p$one can use Theorem 2.1.4 of [Wi1] in the ordinary case, the flat case being well-known.

The following conjecture generalized a fundamantal conjecture of Mazur and Tilouine for$\mathcal { D } = ( \mathrm { o r d } , \Sigma , W ( k _ { 0 } ) , \phi )$; cf. [MT].

Conjecture 2.16.$\varphi _ { \mathcal { D } }$is an isomorphism.

Equivalently this conjecture says that the representation described after the corollaries to Theorem 2.1 (or in (2.33) in the ordinary case) is the universal one for a suitable choice of$H , N$and m. We remind the reader that throughout this section we are assuming that if$p = 3$then$\rho _ { 0 }$is not induced from a character of$\mathbf { Q } ( { \sqrt { - 3 } } )$.

Remark. The case of most interest to us is when$p \ : = \ : 3$and$\rho _ { 0 }$is a representation with values in$\mathrm { G L _ { 2 } ( F _ { 3 } ) }$. In this case it is a theorem of Tunnell, extending results of Langlands, that$\rho _ { 0 }$is always modular. For$\mathrm { G L _ { 2 } ( F _ { 3 } ) }$is a double cover of$S _ { 4 }$and can be embedded in$\mathrm { G L _ { 2 } } ( \mathbf { Z } [ { \sqrt { - 2 } } ] )$whence in$\mathrm { G L _ { 2 } } ( \mathbf { C } )$; cf. [Se] and [Tu]. The conjecture will be proved with a mild restriction on$\rho _ { 0 }$ at the end of Chapter 3.

Remark. Our original restriction to the types (A), (B), (C) for$\rho _ { 0 }$was motivated by the wish that the deformation type (a) be of minimal conductor among its twists, (b) retain property (a) under unramified base changes. Without this kind of stability it can happen that after a base change of Q to an extension unramified at$\Sigma , \rho _ { 0 } \otimes \psi$has smaller ‘conductor’ for some character $\psi .$. The typical example of this is where$\rho _ { 0 } \Big \vert _ { D _ { a } } = \mathrm { I n d } _ { K } ^ { \mathbf { Q } _ { q } } ( \chi )$with$q \equiv - 1 ( p )$and $\chi$is a ramified character over$K .$, the unramified quadratic extension of$\mathbf { Q } _ { q } .$ What makes this dificult for us is that there are then nontrivial ramified local deformations$( { \mathrm { I n d } } _ { K } ^ { \mathbf { Q } _ { p } } \chi \xi$for$\xi \mathrm { ~ a ~ }$ramified character of order p of K) which we cannot detect by a change of level.

For the purposes of Chapter 3 it is convenient to digress now in order to introduce a slight varient of the deformation rings we have been considering so far. Suppose that$\mathcal { D } = ( \cdot , \Sigma , \mathcal { O } , \mathcal { M } )$is a standard deformation problem (associated to$\rho _ { 0 } )$w$\operatorname { r i t h } \cdot = \operatorname { S e }$, str or fl and suppose that$H , M _ { 0 } , M$and m are defined as in (2.24) and Proposition 2.15. We choose a finite set of primes $Q = \{ q _ { 1 } , . . . , q _ { r } \}$with$q _ { i } \nmid M p$. Furthermore we assume that each$q _ { i } \equiv 1 ( p )$ and that the eigenvalues$\{ \alpha _ { i } , \beta _ { i } \}$of$\rho _ { 0 } ( \mathrm { F r o b } q _ { i } )$are distinct for each$q _ { i } \in Q$ This last condition ensures that$\rho _ { 0 }$does not occur as the residual representation of the λ-adic representation associated to any newform on$\Gamma _ { H } ( M , q _ { 1 } \dots q _ { r } )$ where any$q _ { i }$divides the level of the form. This can be seen directly by looking at$\left( \mathrm { F r o b } q _ { i } \right)$in such a representation or by using Proposition$2 . 4 ^ { \dagger }$at the end of Section 2. It will be convenient to assume that the residue field of O contains $\alpha _ { i } , \beta _ { i }$for each$q _ { i }$

Pick$\alpha _ { i }$for each i. We let$\mathcal { D } _ { Q }$be the deformation problem associated to representations$\rho$of$\operatorname { G a l } ( \mathbf { Q } _ { \Sigma \cup Q } / \mathbf { Q } )$which are of type$\mathcal { D }$and which in addition satisfy the property that at each$q _ { i } \in Q$

$$
\rho \Big | _ {D _ {q _ {i}}} \sim \left( \begin{array}{c c} \chi_ {1, q _ {i}} & \\ & \chi_ {2, q _ {i}} \end{array} \right)\tag{2.34}
$$

with$\chi _ { 2 , q _ { i } }$unramified and$\chi _ { 2 , q _ { i } } ( \operatorname { F r o b } q _ { i } ) \equiv \alpha _ { i }$mod m for a suitable choice of basis. One checks as in Chapter 1 that associated to$\mathcal { D } _ { Q }$there is a universal deformation ring$R _ { Q }$. (These new contions are really variants on type (B).)

We will only need a corresponding Hecke ring in a very special case and it is convenient in this case to define it using all the Hecke operators. Let us now set$N = N ( \rho _ { 0 } ) p ^ { \delta ( \rho _ { 0 } ) }$where$\delta ( \rho _ { 0 } )$in as defined in Theorem 2.14. Let${ \mathfrak { m } } _ { 0 }$denote a maximal ideal of${ \bf T } _ { H } ( N )$given by Theorem 2.14 with the property that $\rho _ { \mathfrak { m } _ { 0 } } \simeq \rho _ { 0 }$over${ \overline { { \mathbf { F } } } } _ { p }$relative to a suitable embedding of$k _ { \mathfrak { m } _ { 0 } } \to k$over$k _ { 0 }$. (In the exceptional case we also impose the same condition on m about the reduction of$U _ { p }$as in the definition of$\mathbf { T } _ { \mathcal { D } }$in the exceptional case before (2.25)(b).) Thus $\rho _ { \mathfrak { m } _ { 0 } } \simeq \rho _ { f , \lambda }$mod λ over the residue field of$\mathcal { O } _ { f , \lambda }$for some choice of$f$and$\lambda$ with$f$of level N. By dropping one of the Euler factors at each$q _ { i }$as in the proof of Proposition 2.15, we obtain a form and hence a maximal ideal${ \mathfrak { m } } _ { Q }$of $\mathbf { T } _ { H } ( N q _ { 1 } \dots q _ { r } )$with the property that$\rho _ { \mathfrak { m } _ { Q } } \simeq \rho _ { 0 }$over$\overline { { \mathbf { F } } } _ { p }$relative to a suitable embedding$k _ { \mathfrak { m } _ { Q } } \to k$over$k _ { \mathfrak { m } _ { 0 } }$. The field$k _ { \mathfrak { m } _ { Q } }$is the extension of$k _ { 0 }$(or$k _ { \mathfrak { m ^ { \prime \prime } } }$in the exceptional case) generated by the$\alpha _ { i } , \beta _ { i }$. We set

$$
\mathbf {T} _ {Q} = \mathbf {T} _ {H} (N q _ {1} \dots q _ {r}) _ {\mathfrak {m} _ {Q}} \underset {W (k _ {\mathfrak {m} _ {Q}})} {\otimes} \mathcal {O}.\tag{2.35}
$$

It is easy to see directly (or by the arguments of Proposition 2.15) that $\mathbf { T } _ { Q }$is reduced and that there is an inclusion with finite index

$$
\mathbf {Q} _ {Q} \hookrightarrow \tilde {\mathbf {T}} _ {Q} = \prod \mathcal {O} _ {g, \mu}\tag{2.36}
$$

where the product is taken over representatives of the Galois conjugacy classes of eigenforms$g$of level$N q _ { 1 } \ldots q _ { r }$with${ \mathfrak { m } } _ { Q } \ \to \ \mu$. Now define$\mathcal { D } _ { Q }$using the choices$\alpha _ { i }$for which$U _ { q _ { i } } \ \to \ \alpha _ { i }$under the chosen embedding$k _ { \mathfrak { m } _ { Q } } \ \to \ k$. Then each of the 2-dimensional representations associated to each factor${ \mathcal { O } } _ { g , \mu }$is of type$\mathcal { D } _ { Q }$. We can check this for each$q \in Q$using either the$\pi _ { q } ~ \simeq ~ \pi ( \sigma _ { q } )$ theorem (cf. [Ca1]) as in the case of type (B) or using the Eichler-Shimura relation if$q$does not divide the level of the newform associated to$g .$. So we get a homomorphism of O-algebras$R _ { Q }  \tilde { \mathbf { T } } _ { Q }$and hence also an O-algebra map

$$
\varphi_ {Q}: R _ {Q} \to \mathbf {T} _ {Q}\tag{2.37}
$$

as$R _ { Q }$is generated by traces. This is not an isomorphism in general as we have used N in place of$M$. However it is surjective by the arguments of Proposition 2.15. Indeed, for$q | N ( \rho _ { 0 } ) p .$, we check that$U _ { q }$is in the image of ϕ using the arguments in the second half of the proof of Proposition 2.15. For$q \in Q$we use the fact that$U _ { q }$is the image of the value of$\chi _ { 2 , q } ( \mathrm { F r o b q } )$ in the universal representation;cf. (2.34). For$q | M$, but not of the previous types,$T _ { q }$is a trace in$\rho _ { \mathbf { T } _ { Q } }$and we can apply the Cebotarev density theorem <sup>ˇ</sup> to show that it is in the image of$\varphi _ { Q }$

Finally, if there is a section π$: \mathbf { T } _ { Q }  \mathcal { O }$, then set${ \mathfrak { p } } _ { Q } = \ker \pi$and let$\rho _ { \mathfrak { p } }$denote the 2-dimensional representation to$\mathrm { G L _ { 2 } } ( { \mathcal { O } } )$obtained from$\rho _ { \mathbf { T } _ { Q } }$mod${ \mathfrak { p } } _ { Q }$ Let$V = \mathrm { A d } \rho _ { \mathfrak { p } } \otimes _ { \mathcal { O } } K / \mathcal { O }$where K is the field of fractions of O. We pick a basis for$\rho _ { \mathfrak { p } }$satisfying (2.34) and then let

$$
\begin{array}{c} V ^ {(q _ {i})} = \left\{\left( \begin{array}{c c} a & 0 \\ 0 & 0 \end{array} \right) \right\} \\ \subseteq \operatorname{Ad} \rho_ {\mathfrak {m}} \underset {\mathcal {O}} {\otimes} K / \mathcal {O} = \left\{\left( \begin{array}{c c} a & b \\ c & d \end{array} \right): a, b, c, d \in \mathcal {O} \right\} \underset {\mathcal {O}} {\otimes} K / \mathcal {O} \end{array}\tag{2.38}
$$

and let$V _ { \left( q _ { i } \right) } = V / V ^ { \left( q _ { i } \right) }$. Then as in Proposition 1.2 we have an isomorphism

$$
\mathrm{Hom} _ {\mathcal {O}} (\mathfrak {p} _ {R _ {Q}} / \mathfrak {p} _ {R _ {Q}} ^ {2}, K / \mathcal {O}) \simeq H _ {\mathcal {D} _ {Q}} ^ {1} (\mathbf {Q} _ {\Sigma \cup Q} / \mathbf {Q}, V)\tag{2.39}
$$

where${ \mathfrak { p } } _ { R _ { Q } } = \ker ( \pi \circ \varphi _ { Q } )$and the second term is defined by

$$
H _ {\mathcal {D} _ {Q}} ^ {1} (\mathbf {Q} _ {\Sigma \cup Q} / \mathbf {Q}, V) = \ker : H _ {\mathcal {D}} ^ {1} (\mathbf {Q} _ {\Sigma \cup Q} / \mathbf {Q}, V) \to \prod_ {i = 1} ^ {r} H ^ {1} (\mathbf {Q} _ {q _ {i}} ^ {\mathrm{unr}}, V _ {(q _ {i})}).\tag{2.40}
$$

We return now to our discussion of Conjecture 2.16. We will call a deformation theory D minimal if$\Sigma = { \mathcal { M } } \cup \{ p \}$and · is Selmer, strict or flat. This notion will be critical in Chapter 3. (A slightly stronger notion of minimality is described in Chapter 3 where the Selmer condition is replaced, when possible, by the condition that the representations arise from finite flat group schemes - see the remark after the proof of Theorem 3.1.) Unfortunately even up to twist, not every$\rho _ { 0 }$has an associated minimal D even when$\rho _ { 0 }$is flat or ordinary at p as explained in the remarks after Conjecture 2.16. However this could be achieved if one replaced Q by a suitable finite extension depending on$\rho _ { 0 }$

Suppose now that f is a (normalized) newform, λ is a prime of$\mathcal { O } _ { f }$above p and$\rho f , \lambda$a deformation of$\rho _ { 0 }$of type D where$\mathcal { D } = ( \cdot , \Sigma , \mathcal { O } _ { f , \lambda } , \mathcal { M } )$with$\cdot = \mathrm { S e }$ str or fl. (Strictly speaking we may be changing$\rho _ { 0 }$as we wish to choose its field of definition to be$k = \mathcal { O } _ { f , \lambda } / \lambda . )$Suppose further that level$( f ) | M$where M is defined by (2.24).

Now let us set$\mathcal { O } = \mathcal { O } _ { f , \lambda }$for the rest of this section. There is a homomorphism

$$
\pi = \pi_ {\mathcal {D}, f}: \mathbf {T} _ {\mathcal {D}} \to \mathcal {O}\tag{2.41}
$$

whose kernel is the prime ideal$\mathfrak { p } _ { \mathbf { T } , f }$associated to f and λ. Similary there is a homomorphism

$$
R _ {\mathcal {D}} \to \mathcal {O}
$$

whose kernel is the prime ideal${ \mathfrak { p } } _ { R , f }$associated to f and λ and which factors through$\pi _ { f }$. Pick perfect pairings of O-modules, the second one$\mathbf { T } _ { \mathcal { D } }$-bilinear,

$$
\mathcal {O} \times \mathcal {O} \rightarrow \mathcal {O}, \quad \langle , \rangle : \mathbf {T} _ {\mathcal {D}} \times \mathbf {T} _ {\mathcal {D}} \rightarrow \mathcal {O}.\tag{2.42}
$$

In each case we use the term perfect pairing to signify that the pairs of induced maps$\mathcal { O }  \mathrm { H o m } _ { \mathcal { O } } ( \mathcal { O } , \mathcal { O } )$and$\mathbf { T } _ { \mathcal { D } }  \mathrm { H o m } _ { \mathcal { O } } ( \mathbf { T } _ { \mathcal { D } } , \mathcal { O } )$are isomorphisms. In addition the second one is required to be$\mathbf { T } _ { \mathcal { D } ^ { - } }$-linear. The existence of the second pairing is equivalent to the Gorenstein property, Corollary 2 of Theorem 2.1, as we explain below. Explicitly if h is a generator of the free$\mathbf { T } _ { \mathcal { D } ^ { - } } \mathrm { m o d u l e }$ $\mathrm { H o m } _ { \mathcal { O } } ( \mathbf { T } _ { \mathcal { D } } , \mathcal { O } )$we set$\langle t _ { 1 } , t _ { 2 } \rangle = h ( t _ { 1 } t _ { 2 } )$

A priori$\mathbf { T } _ { H } ( M ) _ { \mathfrak { m } }$(occurring in the description of$\mathbf { T } _ { \mathcal { D } }$in Proposition 2.15) is only Gorenstein as a$\mathbf { Z } _ { p }$-algebra but it follows immediately that it is also a Gorenstein$W ( k _ { \mathfrak { m } } )$-algebra. (The notion of Gorenstein O-algebra is explained in the appendix.) Indeed the map

$$
\mathrm{Hom} _ {W (k _ {\mathfrak {m}})} \Big (\mathbf {T} _ {H} (M) _ {\mathfrak {m}}, W (k _ {\mathfrak {m}}) \Big) \to \mathrm{Hom} _ {\mathbf {Z} _ {p}} \Big (\mathbf {T} _ {H} (M), \mathbf {Z} _ {p} \Big)
$$

given by$\varphi \mapsto$trace$\circ \varphi$is easily seen to be an isomorphism, as the reduction mod$p$is injective and the ranks are equal. Thus$\mathbf { T } _ { \mathcal { D } }$is a Gorenstein O-algebra.

Now let${ \hat { \pi } } : { \mathcal { O } }  \mathbf { T } _ { \mathcal { D } }$be the adjoint of$\pi$with respect to these pairings. Then define a principal ideal$( \eta )$of$\mathbf { T } _ { \mathcal { D } }$by

$$
(\eta) = (\eta_ {\mathcal {D}, f}) = (\hat {\pi} (1)).
$$

This is well-defined independently of the pairings and moreover one sees that ${ \bf T } _ { \mathcal { D } } / \eta$is torsion-free (see the appendix). From its description$( \eta )$is invariant under extensions of$\mathcal { O }$to$\mathcal { O } ^ { \prime }$in an obvious way. Since$\mathbf { T } _ { \mathcal { D } }$is reduced$\pi ( \eta ) \neq 0$

One can also verify that

$$
\pi (\eta) = \langle \eta , \eta \rangle\tag{2.43}
$$

up to a unit in$\mathcal { O } .$

We will say that$\mathcal { D } _ { 1 } ~ \supset ~ \mathcal { D }$if we obtain$\mathcal { D } _ { 1 }$by relaxing certain of the hypotheses on$\mathcal { D } , \mathrm { i . e . }$., if$\mathcal { D } = ( \cdot , \Sigma , \mathcal { O } , \mathcal { M } )$and$\mathcal { D } _ { 1 } = ( \cdot , \Sigma _ { 1 } , \mathcal { O } _ { 1 } , \mathcal { M } _ { 1 } )$we allow that$\Sigma _ { 1 } \supset \Sigma$, any$\mathcal { O } _ { 1 } , \mathcal { M } \supset \mathcal { M } _ { 1 }$(but of the same type) and if · is Se or str in D it can be${ \mathrm { S e } } ,$str, ord or unrestricted in$\mathcal { D } _ { 1 }$, if · is fl in$\mathcal { D } _ { 1 }$it can be fl or unrestricted in$\mathcal { D } _ { 1 }$. We use the term restricted to signify that · is$\mathrm { S e }$, str, fl or ord. The following theorem reduces conjecture 2.16 to a ‘class number’ criterion. For an interpretation of the right-hand side of the inequality in the theorem as the order of a cohomology group, see Propostion 1.2. For an interpretation of the left-hand side in terms of the value of an inner product, see Proposition 4.4.

Theorem 2.17. Assume, as above, that$\rho _ { f , \lambda }$is a deformation of ρ<sub>0</sub> of type$\mathcal { D } = ( \cdot , \Sigma , \mathcal { O } = \mathcal { O } _ { f , \lambda } , \mathcal { M } )$with$\cdot = \mathrm { S e }$, str or fl. Suppose that

$$
\# \mathcal {O} / \pi (\eta_ {\mathcal {D}, f}) \geq \# \mathfrak {p} _ {R, f} / \mathfrak {p} _ {R, f} ^ {2}.
$$

Then

(i)$\varphi _ { \mathcal { D } _ { 1 } } : R _ { \mathcal { D } _ { 1 } } \simeq \mathbf { T } _ { \mathcal { D } _ { 1 } }$is an isomorphism for all (restricted)$\mathcal { D } _ { 1 } \supset \mathcal { D }$

(ii)$\mathbf { T } _ { \mathcal { D } _ { 1 } }$is a complete intersection (over$\mathcal { O } _ { 1 } \textit { i f }$· is$\mathrm { S e }$, str$o r \mathbb { H } )$for all restricted$\mathcal { D } _ { 1 } \supset \mathcal { D }$

Proof. Let us write T for$\mathbf { T } _ { \mathcal { D } } , \ \mathfrak { p } _ { \mathbf { T } }$for$\mathfrak { p } _ { \mathbf { T } , f } , \ \mathfrak { p } _ { R }$for${ \mathfrak { p } } _ { R , f }$and η for$\eta _ { \eta , f }$ Then we always have

$$
\# \mathcal {O} / \eta \leq \# \mathfrak {p} _ {\mathbf {T}} / \mathfrak {p} _ {\mathbf {T}} ^ {2}.\tag{2.44}
$$

(Here and in what follows we sometimes write η for$\pi ( \eta )$if the context makes this reasonable.) This is proved as follows.$\mathbf { T } / \eta$acts faithfully on p<sub>T</sub>. Hence the Fitting ideal of$\mathfrak { p } _ { \mathbf { T } }$as a$\mathbf { T } / \eta \mathbf { \Sigma }$-module is zero. The same is then true of ${ \mathfrak { p } } _ { \mathbf { T } } / { \mathfrak { p } } _ { \mathbf { T } } ^ { 2 }$as an$\mathcal { O } / \eta = ( \mathbf { T } / \eta ) / \mathfrak { p } _ { \mathbf { T } }$-module. So the Fitting ideal of${ \mathfrak { p } } _ { \mathbf { T } } / { \mathfrak { p } } _ { \mathbf { T } } ^ { 2 }$as an O-module is contained in$( \eta )$and the conclusion is then easy. So together with the hypothesis of the theorem we get inequality (and hence equalities)

$$
\# \mathcal {O} / \pi (\eta) \geq \# \mathfrak {p} _ {R} / \mathfrak {p} _ {R} ^ {2} \geq \# \mathfrak {p} _ {\mathbf {T}} / \mathfrak {p} _ {\mathbf {T}} ^ {2} \geq \# \mathcal {O} / \pi (\eta).
$$

By Proposition 2 of the appendix T is a complete intersection over O. Part (ii) of the theorem then follows for D. Part (i) follows for D from Proposition 1 of the appendox.

We now prove inductively that we can deduce the same inequality

$$
\# \mathcal {O} _ {1} / \eta_ {\mathcal {D} _ {1}, f} \geq \# \mathfrak {p} _ {R _ {1}, f} / \mathfrak {p} _ {R _ {1}, f} ^ {2}\tag{2.45}
$$

for$\mathcal { D } _ { 1 } \supset \mathcal { D }$and$R _ { 1 } = R _ { D _ { 1 } }$. The above argument will then prove the theorem for$\mathcal { D } _ { 1 }$. We explain this first in the case$\mathcal { D } _ { 1 } = \mathcal { D } _ { q }$where$\mathcal { D } _ { q }$difers from D only in replacing Σ by$\Sigma \cup \{ q \}$. Let us write$\mathbf { T } _ { q }$for$\mathbf { T } _ { \mathcal { D } _ { q } } , \mathfrak { p } _ { R , q }$for${ \mathfrak { p } } _ { R , f }$with$R = R _ {  }$ and$\eta _ { q }$for$\eta _ { \mathcal { D } _ { q } , f }$. We recall that$U _ { q } = 0$in$\mathbf { T } _ { q }$

We choose isomorphisms

$$
\mathbf {T} \simeq \mathrm{Hom} _ {\mathcal {O}} (\mathbf {T}, \mathcal {O}), \quad \mathbf {T} _ {q} \simeq \mathrm{Hom} _ {\mathcal {O}} (\mathbf {T} _ {q}, \mathcal {O})\tag{2.46}
$$

coming from the fact that each of the rings is a Gorenstein O-algebra. If $\alpha _ { q } : \mathbf { T } _ { q }  \mathbf { T }$is the natural map we may consider the element$\Delta _ { q } = \alpha _ { q } \circ \hat { \alpha } _ { q } \in \mathbf { T }$ where the adjoint is with respect to the above isomorphisms. Then it is clear that

$$
\left(\alpha_ {q} (\eta_ {q})\right) = (\eta \Delta_ {q})\tag{2.47}
$$

as principal ideals of T. In particular$\pi ( \eta _ { q } ) = \pi ( \eta \Delta _ { q } )$in O.

Now it follows from Proposition 2.7 that the principal ideal$( \Delta _ { q } )$is given by

$$
(\Delta_ {q}) = \Big ((q - 1) ^ {2} (T _ {q} ^ {2} - \langle q \rangle (1 + q) ^ {2}) \Big).\tag{2.48}
$$

In the statement of Proposition 2.7 we used$\mathbf { Z } _ { p }$-pairings

$$
\mathbf {T} \simeq \mathrm{Hom} _ {\mathbf {Z} _ {p}} (\mathbf {T}, \mathbf {Z} _ {p}), \quad \mathbf {T} _ {q} \simeq \mathrm{Hom} _ {\mathbf {Z} _ {p}} (\mathbf {T} _ {q}, \mathbf {Z} _ {p})
$$

to define$( \Delta _ { q } ) \ : = \ : ( \alpha _ { q } \circ \hat { \alpha } _ { q } )$. However, using the description of the pairings as$W ( k _ { \mathfrak { m } } )$-algebras derived from these$\mathbf { Z } _ { p ^ { - } } \mathrm { p a i r i n g s }$in the paragraph following (2.42) we see that the ideal$( \Delta _ { q } )$is unchanged when we use$W ( k _ { \mathfrak { m } } )$-algebra pairings, and hence also when we extend scalars to$\mathcal { O }$as in (2.42).

On the other hand

$$
\# \mathfrak {p} _ {R, q} / \mathfrak {p} _ {R, q} ^ {2} \leq \# \mathfrak {p} _ {R} / \mathfrak {p} _ {R} ^ {2} \cdot \# \left\{\mathcal {O} / (q - 1) ^ {2} \left(T _ {q} ^ {2} - \langle q \rangle (1 + q) ^ {2}\right) \right\}
$$

by Propositions 1.2 and 1.7. Combining this with (2.47) and (2.48) gives (2.45). If$\mathcal M \neq \phi$we use a similar argument to pass from D to$\mathcal { D } _ { q }$where this time $\mathcal { D } _ { q }$signifies that D is unchanged except for dropping q from M. In each of types (A), (B), and (C) one checks from Propositions 1.2 and 1.8 that

$$
\# \mathfrak {p} _ {R, q} / \mathfrak {p} _ {R, q} ^ {2} \leq \# \mathfrak {p} _ {R} / \mathfrak {p} _ {R} ^ {2} \cdot \# H ^ {0} (\mathbf {Q} _ {q}, V ^ {*}).
$$

This is in agreement with Propositions 2.10, 2.12 and 2.13 which give the corresponding change in η by the method described above.

To change from an O-algebra to an$\mathcal { O } _ { \mathrm { 1 ^ { - a l g e b r a } } }$is straightforward (the complete intersection property can be checked using [Ku1, Cor. 2.8 on p. 209]), and to change from Se to ord we use (1.4) and (2.32). The change from str to ord reduces to this since by Proposition 1.1 strict deformations and Selmer deformations are the same. Note that for the ord case if R is a local Noetherian ring and$f \in R$is not a unit and not a zero divisor, then R is a complete intersection if and only if$R / f$is (cf. [BH, Th. 2.3.4]). This completes the proof of the theorem.

Remark 2.18. If we suppose in the Selmer case that f has level N with $p \nmid N$we can also consider the ring$\mathbf { T } _ { H } ( M _ { 0 } ) _ { \mathfrak { m } _ { 0 } }$(with$M _ { 0 }$as in (2.24) and m defined in the same way as for$\mathbf { T } _ { H } ( M ) )$. This time set

$$
T _ {0} = \mathbf {T} _ {H} (M _ {0}) _ {\mathfrak {m} _ {0}} \underset {W (k _ {\mathfrak {m} _ {0}})} {\otimes} \mathcal {O}, \quad T = \mathbf {T} _ {H} (M) _ {\mathfrak {m}} \underset {W (k _ {\mathfrak {m}})} {\otimes} \mathcal {O}.
$$

Define$\eta _ { 0 } , \eta , \mathfrak { p } _ { 0 }$and p with respect to these rings, and let$( \Delta _ { p } ) = \alpha _ { p } \circ { \hat { \alpha } } _ { p }$where $\alpha _ { p } : T  T _ { 0 }$and the adjoint is taken with respect to O-pairings on$T$and$T _ { 0 }$ We then have by Proposition 2.4

$$
\left(\eta_ {p}\right) = \left(\eta \cdot \Delta_ {p}\right) = \left(\eta \cdot \left(T _ {p} ^ {2} - \langle p \rangle (1 + p) ^ {2}\right)\right) = \left(\eta \cdot \left(a _ {p} ^ {2} - \langle p \rangle\right)\right)\tag{2.49}
$$

as principal ideals of$T .$, where$a _ { p }$is the unit root of$x ^ { 2 } - T _ { p } x + p \langle p \rangle = 0$

Remark. For some earlier work on how deformation rings change with Σ see [Bo].

## Chapter 3

In this chapter we prove the main results about Conjecture 2.16. We begin by showing that bound for the Selmer group to which it was reduced in Theorem 2.17 can be checked if one knows that the minimal Hecke ring is a complete intersection. Combining this with the main result of [TW] we complete the proof of Conjecture 2.16 under a hypothesis that ensures that a minimal Hecke ring exists.

## Estimates for the Selmer group

Let$\rho _ { 0 } : \mathrm { G a l } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } ) \to \mathrm { G L } _ { 2 } ( k )$be an odd irreducible representation which we will assume is modular. Let D be a deformation theory of type$( \cdot , \Sigma , { \mathcal { O } } , { \mathcal { M } } )$ such that$\rho _ { 0 }$is type D, where · is Selmer, strict or flat. We remind the reader that k is assumed to be the residue field of O. Then as explained in Theorem 2.14, we can pick a modular lifting$\rho _ { f , \lambda }$of$\rho _ { 0 }$of type D (altering k if necessary and replacing O by a ring containing$\mathcal { O } _ { f , \lambda } )$provided that$\rho _ { 0 }$is not induced from a character of$\mathbf { Q } ( { \sqrt { - 3 } } )$if$p = 3$. For the rest of this chapter, we will make the assumption that$\rho _ { 0 }$is not of this exceptional type. Theorem 2.14 also specifies a certain minimum level and character for f and in particular ensures that we can pick f to have level prime to p when$\rho _ { 0 } | _ { D _ { p } }$is associated to a finite flat group scheme over$\mathbf { Z } _ { p }$and det$\rho _ { 0 } | _ { I _ { p } } = \omega$

In Chapter 2, Section 3, we defined a ring$\mathbf { T } _ { \mathcal { D } }$associated to$\mathcal { D }$. Here we make a slight modification of this ring. In the case where · is Selmer and$\rho _ { 0 } | _ { D _ { \boldsymbol { p } } }$ is associated to a finite flat group scheme and det$\rho _ { 0 } | _ { I _ { p } } = \omega$we set

$$
\mathbf {T} _ {\mathcal {D} _ {0}} = \mathbf {T} _ {H} ^ {\prime} (M _ {0}) _ {\mathfrak {m} _ {0} ^ {\prime}} \underset {W (k _ {0})} {\otimes} \mathcal {O}\tag{3.1}
$$

with$M _ { 0 }$as in (2.24), H defined following (2.24) (it is actually a subgroup of$( \mathbf { Z } / M _ { 0 } \mathbf { Z } ) ^ { * } )$and${ \mathfrak { m } } _ { 0 } ^ { \prime }$the maximal ideal of$\mathbf { T } _ { H } ^ { \prime } ( M _ { 0 } )$associated to$\rho _ { 0 }$. The same proof as in Proposition 2.15 ensures that there is a maximal ideal${ \mathfrak { m } } _ { 0 }$of ${ \bf T } _ { H } ( M _ { 0 } )$with m<sub>0</sub>$\cap { \mathbf { T } } _ { H } ^ { \prime } ( M _ { 0 } ) = { \mathfrak { m } } _ { 0 } ^ { \prime }$and such that the natural map

$$
\mathbf {T} _ {\mathcal {D} _ {0}} = \mathbf {T} _ {H} ^ {\prime} (M _ {0}) _ {\mathfrak {m} _ {0} ^ {\prime}} \underset {W (k _ {0})} {\otimes} \mathcal {O} \to \mathbf {T} _ {H} (M _ {0}) _ {\mathfrak {m} _ {0}} \underset {W (k _ {0})} {\otimes} \mathcal {O}\tag{3.2}
$$

is an isomorphism. The maximal ideal m which we choose is characterized by the properties that$\rho _ { \mathfrak { m } _ { 0 } } = \rho _ { 0 }$and$U _ { q } \in \mathfrak { m } _ { 0 }$for$q \in \Sigma - \mathcal { M } \cup \{ p \}$. (The value of $T _ { p }$or of$U _ { q }$for$q \in \mathcal { M }$is determined by the other operators; see the proof of Proposition 2.15.) We now define$\mathbf { T } _ { \mathcal { D } _ { 0 } }$in general by the following:

$\mathbf { T } _ { \mathcal { D } _ { 0 } }$is given by (3.1) if · is Se and$\rho _ { 0 } | _ { D _ { p } }$is associated to a finite flat group scheme over$\mathbf { Z } _ { p }$and det$\rho _ { 0 } | _ { I _ { p } } = \omega ;$

$$
\begin{array}{l} \mathbf {T} _ {\mathcal {D} _ {0}} = \mathbf {T} _ {\mathcal {D}} \text {if} \cdot \text {is str or fl, or} \rho_ {0} | D _ {p} \text {is not associated} \\ \text {to a finite flat group scheme over} \mathbf {Z} _ {p}, \text {or} \\ \det \rho_ {0} | _ {I _ {p}} \neq \omega . \end{array}\tag{3.3}
$$

We choose a pair$( f , \lambda )$of minimum level and character as given by Theorem 2.14 and this gives a homomorphism of O-algebras

$$
\pi_ {f}: \mathbf {T} _ {C a l D _ {0}} \to \mathcal {O} \supseteq \mathcal {O} _ {f, \lambda}.
$$

We set${ \mathfrak { p } } _ { \mathbf { T } , f } = \ker \pi _ { f }$and similarly we let${ \mathfrak { p } } _ { R , f }$denote the inverse image of$\mathfrak { p } _ { \mathbf { T } , f }$ in$R _ { \mathcal { D } }$. We define a principal ideal$\left( \eta _ { \mathbf { T } , f } \right)$of$\mathbf { T } _ { \mathcal { D } _ { 0 } }$by taking an adjoint ˆπ<sub>f</sub> of π<sub>f</sub> with respect to parings as in (2.42) and write

$$
\eta_ {\mathbf {T}, f} = (\hat {\pi} _ {f} (1)).
$$

Note that${ \mathfrak { p } } _ { \mathbf { T } , f } / { \mathfrak { p } } _ { \mathbf { T } , f } ^ { 2 }$is finite and$\pi _ { f } ( \eta _ { \mathbf { T } , f } ) \neq 0$because$\mathbf { T } _ { \mathcal { D } _ { 0 } }$is reduced. We also write$\eta _ { \mathrm { T } , f }$for$\ddot { \pi } _ { f } ( \eta _ { \mathfrak { T } , f } )$if the context makes this usage reasonable. We let $V _ { f } = \operatorname { A d } \rho _ { \mathfrak { p } } \bigotimes _ { \mathcal { O } } ^ { \cdot } K / \mathcal { O }$where$\rho _ { \mathfrak { p } }$is the extension of scalars of$\rho _ { f , \lambda }$to$\mathcal { O } .$

Theorem 3.1. Assume that D is minimal, i.$e . , \sum = \mathcal { M } \cup \{ p \}$, and that $\rho _ { 0 }$is absolutely irreducible when restricted to$\mathbf { Q } { \biggl ( } { \sqrt { ( - 1 ) ^ { \frac { p - 1 } { 2 } } p } } { \biggr ) }$. Then

$$
\mathrm{(i)} \# H _ {\mathcal {D}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V _ {f}) \leq \# (\mathfrak {p} _ {\mathbf {T}, f} / \mathfrak {p} _ {\mathbf {T}, f} ^ {2}) ^ {2} \cdot c _ {p} / \# (\mathcal {O} / \eta_ {\mathbf {T}, f})
$$

where$c _ { p } = \# ( \mathcal { O } / U _ { p } ^ { 2 } - \langle p \rangle ) < \infty$when ρ is Selmer and$\rho _ { 0 } | _ { D _ { p } }$is associated to a finite flat group scheme over$\mathbf { Z } _ { p }$and det$\rho _ { 0 } | _ { I _ { p } } = \omega$, and$c _ { p } = 1$otherwise;

(ii)$i f \mathbf { T } _ { \mathcal { D } _ { 0 } }$is a complete intersection over O then (i) is an equality,$R _ { \mathcal { D } } \simeq$ $\mathbf { T } _ { \mathcal { D } }$and$\mathbf { T } _ { \mathcal { D } }$is a complete intersection.

In general, for any (not necessarily minimal) D of Selmer, strict or flat type, and any$\rho _ { f , \lambda }$of type$\mathcal { D } , \# H _ { \mathcal { D } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V _ { f } ) < \infty \ i f \rho _ { 0 }$is as above.

Remarks. The finiteness was proved by Flach in [Fl] under some restrictions on$f , p$and D by a diferent method. In particular, he did not consider the strict case. The bound we obtain in (i) is in fact the actual order of $H _ { \mathcal { D } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V _ { f } )$as follows from the main result of [TW] which proves the hypothesis of part (ii). Then applying Theorem 2.17 we obtain the order of this group for more general$\mathcal { D } \mathrm { { s } }$associated to$\rho _ { 0 }$under the condition that a minimal D exists associated to$\rho _ { 0 }$. This is stated in Theorem 3.3.

The case where the projective representation associated to$\rho _ { 0 }$is dihedral does not always have the property that a twist of it has an associated minimal D. In the case where the associated quadratic field is imaginary we will give a diferent argument in Chapter 4.

Proof. We will assume throughout the proof that D is minimal, indicating only at the end the slight changes needed fot the final assertion of the theorem. Let Q be a finite set of primes disjoint from Σ satisfying$q \equiv 1 ( p )$and$\rho _ { 0 } ( { \mathrm { F r o b } } q )$ having distinct eigenvalues for each$q \in Q$For the minimal deformation problem$\mathcal { D } = ( \cdot , \Sigma , \mathcal { O } , \mathcal { M } )$, let$\mathcal { D } _ { Q }$be the deformation problem described before (2.34); i.e., it is the refinement of$( \cdot , \Sigma \cup Q , \mathcal { O } , \mathcal { M } )$obtained by imposing the additional restriction (2.34) at each$q \in Q$. (We will assume for the proof that O is chosen so${ \mathcal { O } } / \lambda = k$contains the eigenvalues of$\rho _ { 0 } ( \mathrm { F r o b } q )$for each$q \in Q . )$ We set

$$
\mathbf {T} = \mathbf {T} _ {\mathcal {D} _ {0}}, R = R _ {\mathcal {D}}
$$

and recall the definition of$\mathbf { T } _ { Q }$and$R _ { Q }$from Chapter 2, §3 (cf. (2.35)). We write V for$V _ { f }$and recall the definition of$V _ { ( q ) }$following (2.38). Also remember that m<sub>Q</sub> is a maximal ideal of${ \mathbf { T } } _ { H } ( N q _ { 1 } \dots q _ { r } )$as in (2.35) for which$\rho _ { \mathfrak { m } _ { Q } } \simeq \rho _ { 0 }$ over$\bar { \mathbf { F } } _ { p }$(recall that this uses the same choice of embedding$k _ { \mathfrak { m } _ { Q } } \longrightarrow k$as in the definition of$\mathbf { T } _ { Q } )$. We use${ \mathfrak { m } } _ { Q }$also to denote the maximal ideal of$\mathbf { T } _ { Q }$if the context makes this reasonable.

Consider the exact and commutative diagram

$$
\begin{array}{c c c c c c c}0&\rightarrow&H _ {\mathcal {D}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V)&\rightarrow&H _ {\mathcal {D} _ {Q}} ^ {1} (\mathbf {Q} _ {\Sigma \cup Q} / \mathbf {Q}, V)&\stackrel {{\delta_ {Q}}} {{\rightarrow}}&\prod_ {q \in Q} H ^ {1} (\mathbf {Q} _ {q} ^ {\mathrm{unr}}, V ^ {(q)}) ^ {\mathrm{Gal} (\mathbf {Q} _ {q} ^ {\mathrm{unr}} / \mathbf {Q} _ {q})}\\&&| \wr&&| \wr&&\\0&\rightarrow&(\mathfrak {p} _ {R} / \mathfrak {p} _ {R} ^ {2}) ^ {*}&\rightarrow&(\mathfrak {p} _ {R _ {Q}} / \mathfrak {p} _ {R _ {Q}} ^ {2}) ^ {*}&&\Bigg | \wr_ {Q}\\&&\uparrow&&\uparrow&&\\0&\rightarrow&(\mathfrak {p} _ {\mathbf {T}} / \mathfrak {p} _ {\mathbf {T}} ^ {2}) ^ {*}&\rightarrow&(\mathfrak {p} _ {\mathbf {T} _ {Q}} / \mathfrak {p} _ {\mathbf {T} _ {Q}} ^ {2}) ^ {*}&\stackrel {{u _ {Q}}} {{\rightarrow}}&K _ {Q} \to 0\end{array}
$$

where$K _ { Q }$is by definition the cokernel in the horizontal sequence and ∗ denotes $\mathrm { H o m } _ { \mathscr { O } } ( \mathbf { \Sigma } , \mathbf { \tilde { { K } } } / \mathscr { O } )$for K the field of fractions of O. The key result is:

Lemma 3.2. The map$\iota _ { Q }$is injective for any finite set of primes Q satisfying

$$
q \equiv 1 (p), T _ {q} ^ {2} \not \equiv \langle q \rangle (1 + q) ^ {2} \bmod {\mathfrak {m}} f o r a l l q \in Q.
$$

Proof. Note that the hypotheses of the lemma ensure that$\rho _ { 0 } ( \mathrm { F r o b } q )$has distinct eigenvaluesw for each$q \in Q$. First, consider the ideal${ \mathfrak { a } } _ { Q }$of$R _ { Q }$defined

by

$$
\mathfrak {a} _ {Q} = \bigg \{a _ {i} - 1, b _ {i}, c _ {i}, d _ {i} - 1: \left( \begin{array}{c c} a _ {i} & b _ {i} \\ c _ {i} & d _ {i} \end{array} \right) = \rho_ {\mathcal {D} _ {Q}} (\sigma_ {i}) \text {with} \sigma_ {i} \in I _ {q _ {i}}, q _ {i} \in Q \bigg \}.\tag{3.4}
$$

Then the universal property of$R _ { Q }$shows that$R _ { Q } / { \mathfrak { a } } _ { Q } \simeq R$. This permits us to identify$( { \mathfrak { p } } _ { R } / { \mathfrak { p } } _ { R } ^ { 2 } ) ^ { * }$as

$$
(\mathfrak {p} _ {R} / \mathfrak {p} _ {R} ^ {2}) ^ {*} = \{f \in (\mathfrak {p} _ {R _ {Q}} / \mathfrak {p} _ {R _ {Q}} ^ {2}) ^ {*}: f (\mathfrak {a} _ {Q}) = 0 \}.
$$

If we prove the same relation for the Hecke rings, i.e., with T and$\mathbf { T } _ { Q }$replacing $R$and$R _ { Q }$then we will have the injectivity of$\iota _ { Q }$. We will write$\bar { \mathfrak { a } } _ { Q }$for the image of${ \mathfrak { a } } _ { Q }$in$\mathbf { T } _ { Q }$under the map$\varphi _ { Q }$of (2.37).

It will be enough to check that for any$q \in Q ^ { \prime } , Q ^ { \prime }$a subset of$Q , \mathbf { T } _ { Q ^ { \prime } } / \bar { \mathfrak { a } } _ { q } \simeq$ ${ \bf { T } } _ { Q ^ { \prime } - \{ q \} }$where${ \mathfrak { a } } _ { q }$is defined as in (3.4) but with$Q$replaced by$q .$. Let $\begin{array} { r } { N ^ { \prime } = N ( \rho _ { 0 } ) p ^ { \delta ( \rho _ { 0 } ) } \cdot \prod _ { q _ { i } \in Q ^ { \prime } - \{ q \} } q _ { i } } \end{array}$where$\delta ( \rho _ { 0 } )$is as defined in Theorem 2.14. Then take an element$\sigma \in \bar { I _ { q } } \subseteq \mathrm { G a l } ( \bar { \mathbf { Q } } _ { q } / \mathbf { Q } _ { q } )$which restricts to a generator of$\operatorname { G a l } ( \mathbf { Q } ( \zeta _ { N ^ { \prime } q } / \mathbf { Q } ( \zeta _ { N ^ { \prime } } ) )$. Then det$( \sigma ) = \langle t _ { q } \rangle \in \mathbf { T } _ { Q ^ { \prime } }$in the representation to $\mathrm { G L } _ { 2 } ( \mathbf { T } _ { Q ^ { \prime } } )$defined after Theorem 2.1. (Thus$t _ { q } \equiv 1 ( N ^ { \prime } )$and$t _ { q }$is a primitive root mod$q . )$It is easily checked that

$$
J _ {H} (N ^ {\prime}. q) _ {\mathfrak {m} _ {Q ^ {\prime}}} (\bar {\mathbf {Q}}) \simeq J _ {H} (N ^ {\prime} q) _ {\mathfrak {m} _ {Q ^ {\prime}}} (\bar {\mathbf {Q}}) [ \langle t _ {q} \rangle - 1 ].\tag{3.5}
$$

Here H is still a subgroup of$( \mathbf { Z } / M _ { 0 } \mathbf { Z } ) ^ { * }$. (We use here that$\rho _ { 0 }$is not reducible for the injectivity and also that$\rho _ { 0 }$is not induced from a character of$\mathbf { Q } ( { \sqrt { - 3 } } )$ for the surjectivity when$p = 3$. The latter is to avoid the ramification points of the covering$X _ { H } ( N ^ { \prime } q )  X _ { H } ( N ^ { \prime } , q )$of order 3 which can give rise to invariant divisors of$X _ { H } ( N ^ { \prime } q )$which are not the images of divisors on$X _ { H } ( N ^ { \prime } , q ) . )$

Now by Corollary 1 to Theorem 2.1 the Pontrjagin duals of the modules in (3.5) are free of rank two. It follows that

$$
(\mathbf {T} _ {H} (N ^ {\prime} q) _ {\mathfrak {m} _ {Q ^ {\prime}}}) ^ {2} / (\langle t _ {q} \rangle - 1) \simeq (\mathbf {T} _ {H} (N ^ {\prime}, q) _ {\mathfrak {m} _ {Q ^ {\prime}}}) ^ {2}.\tag{3.6}
$$

The hypotheses of the lemma imply the condition that$\rho _ { 0 } ( \mathrm { F r o b } q )$has distinct eigenvalues. So applying Proposition$2 . 4 ^ { \dagger }$(at the end of §2) and the remark following it (or using the fact remarked in Chapter 2, §3 that this condition implies that$\rho _ { 0 }$does not occur as the residual representation associated to any form which has the special representation at$q )$we see that after tensoring over $W ( k _ { \mathfrak { m } _ { Q ^ { \prime } } } )$with O, the right-hand side of (3.6) can be replaced by$\mathbf { T } _ { Q ^ { \prime } - \{ q \} } ^ { 2 }$thus giving

$$
\mathbf {T} _ {Q ^ {\prime} / \bar {\mathfrak {a}} _ {q}} ^ {2} \simeq \mathbf {T} _ {Q ^ {\prime} - \{q \}} ^ {2},
$$

since$\left. t _ { q } \right. \mathrm { ~ - ~ } 1 \in \mathrm { ~ } \bar { \mathfrak { a } } _ { q }$. Repeated inductively this gives the desired relation $\mathbf { T } _ { Q } / \bar { \mathbf { a } } _ { Q } \simeq \mathbf { T }$, and completes the proof of the lemma.

Suppose now that$Q$is a finite set of primes chosen as in the lemma. Recall that from the theory of congruences (Prop. 2.4’ at the end of §2)

$$
\eta_ {\mathbf {T} _ {Q, f}} / \eta_ {\mathbf {T}, f} = \prod_ {q \in Q} (q - 1),
$$

the factors$( \alpha _ { q } ^ { 2 } - \langle q \rangle )$being units by our hypotheses on$q \in Q$. (We only need that the right-hand side divides the left which is somewhat easier.) Also, from the theory of Fitting ideals (see the proof of (2.44))

$$
\begin{array}{r} \# (\mathfrak {p} _ {\mathbf {T}} / \mathfrak {p} _ {\mathbf {T}} ^ {2}) \geq \# (\mathcal {O} / \eta_ {\mathbf {T} _ {f}}) \\ \# (\mathfrak {p} _ {\mathbf {T} _ {Q}} / \mathfrak {p} _ {\mathbf {T} _ {Q}} ^ {2}) \geq \# (\mathcal {O} / \eta_ {\mathbf {T} _ {Q, f}}). \end{array}
$$

We dedeuce that

$$
\# K _ {Q} \geq \# \left(\mathcal {O} \Big / \prod_ {q \in Q} (q - 1)\right) \cdot t ^ {- 1}
$$

where$t = \# ( \mathfrak { p } _ { \mathbf { T } } / \mathfrak { p } _ { \mathbf { T } } ^ { 2 } ) / \# ( \mathcal { O } / \eta _ { \mathbf { T } , f } )$. Since the range of$\iota _ { Q }$has order given by

$$
\# \left\{\mathcal {O} \Big / \prod_ {q \in Q} (q - 1) \right\},
$$

we compute that the index of the image of$\iota _ { Q }$is$\leq t$as$\iota _ { Q }$is injective.

Keeping our assumption on$Q$from Lemma$3 . 2$, consider the kernel of$\lambda ^ { M }$ applied to the diagram at the beginning of the proof of the theorem. Then with M chosen large enough so that$\lambda ^ { \overset { \smile } { M } }$annihilates${ \mathfrak { p } } _ { \mathbf { T } } / { \mathfrak { p } } _ { \mathbf { T } } ^ { 2 }$(which is finite because T is reduced) we get:

$$
\begin{array}{c c c} 0 \to H _ {\mathcal {D}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V [ \lambda^ {M} ]) \to H _ {\mathcal {D} _ {Q}} ^ {1} (\mathbf {Q} _ {\Sigma \cup Q} / \mathbf {Q}, V [ \lambda^ {M} ]) \xrightarrow {\delta_ {Q}} \prod_ {q \in Q} H ^ {1} (\mathbf {Q} _ {q} ^ {\mathrm{unr}}, V ^ {(q)} [ \lambda^ {M} ]) ^ {\mathrm{Gal} (\mathbf {Q} _ {q} ^ {\mathrm{unr}} / \mathbf {Q} _ {q})} \\ \uparrow & \uparrow   \psi_ {Q} & \uparrow   \iota_ {Q} \\ 0 \to (\mathfrak {p _ {T}} / \mathfrak {p _ {T} ^ {2}}) ^ {*} & \to (\mathfrak {p _ {T}} _ {Q} / \mathfrak {p _ {T Q} ^ {2}}) ^ {*} [ \lambda^ {M} ] & \to K _ {Q} [ \lambda^ {M} ] \to (\mathfrak {p _ {T}} / \mathfrak {p _ {T} ^ {2}}) ^ {*}. \end{array}
$$

See (1.7) for the justification that$\lambda ^ { M }$can be taken inside the parentheses in the first two terms. Let$X _ { Q } = \psi _ { Q } ( ( \mathfrak { p } _ { \mathbf { T } _ { Q } } / \mathfrak { p } _ { \mathbf { T } _ { O } } ^ { 2 } ) ^ { * } [ \lambda ^ { M } ] )$. Then we can estimate the order of$\delta _ { Q } ( X _ { Q } )$using the fact that the image if$\iota _ { Q }$has index at most$t .$ We get

$$
\# \delta_ {Q} (X _ {Q}) \geq \left(\prod_ {q \in Q} \# \mathcal {O} / (\lambda^ {M}, q - 1)\right) \cdot (1 / t) \cdot (1 / \# (\mathfrak {p} _ {\mathbf {T}} / \mathfrak {p} _ {\mathbf {T}} ^ {2})).\tag{3.7}
$$

Now we choose$Q$to be a set of primes with the property that

$$
\varepsilon_ {Q}: H _ {\mathcal {D} ^ {*}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V _ {\lambda^ {M}} ^ {*}) \to \prod_ {q \in Q} H ^ {1} (\mathbf {Q} _ {q}, V _ {\lambda^ {M}} ^ {*})\tag{3.8}
$$

is injective. We also keep the condition that$\iota _ { Q }$is injective by only allowing $Q$to contain primes of the form given in the lemma. In addition, we require these$q \mathrm { ^ { \circ } s }$to satisfy$q \equiv 1 ( p ^ { M } )$

To see that this can be done, suppose that$x \in$ker$\varepsilon _ { Q }$and$\lambda x = 0$but $x \neq 0$. We have a commutative diagram

$$
\begin{array}{c c c} H ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V _ {\lambda^ {M}} ^ {*} [ \lambda ] & \stackrel {{\varepsilon_ {Q}}} {{\to}} & \prod_ {q \in Q} H ^ {1} (\mathbf {Q} _ {q}, V _ {\lambda^ {M}} ^ {*}) [ \lambda ] \\ | \wr & & | \wr \end{array}
$$

$$
H ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V _ {\lambda} ^ {*}) \stackrel {{\bar {\varepsilon} _ {Q}}} {{\longrightarrow}} \prod_ {q \in Q} H ^ {1} (\mathbf {Q} _ {q}, V _ {\lambda} ^ {*})
$$

the left-hand isomorphisms coming from our particular choices of$q \mathrm { ^ { \circ } s }$and the left-hand isomorphism from our hypothesis on$\rho _ { 0 }$. The same diagram will hold if we replace$Q$by$Q _ { 0 } = Q \cup \{ q _ { 0 } \}$and we now need to show that we can choose $q _ { 0 }$so that$\bar { \varepsilon } _ { Q _ { 0 } } ( x ) \neq 0$

The restriction map

$$
H ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V _ {\lambda} ^ {*}) \to \operatorname{Hom} (\operatorname{Gal} (\bar {\mathbf {Q}} / K _ {0} (\zeta_ {p})), V _ {\lambda} ^ {*}) ^ {\operatorname{Gal} (K _ {0} (\zeta_ {p}) / \mathbf {Q})}
$$

has kernel$H ^ { 1 } ( K _ { 0 } ( \zeta _ { p } ) / \mathbf { Q } , k ( 1 ) )$by Proposition 1.11 where here$K _ { 0 }$is the splitting field of$\rho _ { 0 }$. Now if$x \in H ^ { 1 } ( K _ { 0 } ( \zeta _ { p } ) / \mathbf { Q } , k ( 1 ) )$and$x \neq 0$then$p = 3$and x factors through an abelian extension L of$\mathbf { Q } ( \zeta _ { 3 } )$of exponent 3 which is non-abelian over$\mathbf { Q }$. In this exeptional case, L must ramify at some prime q of $\mathbf { Q } ( \zeta _ { 3 } )$, and if q lies over the rational prime$q \neq 3$then the composite map

$$
H ^ {1} (K _ {0} (\zeta_ {3}) / \mathbf {Q}, k (1)) \to H ^ {1} (\mathbf {Q} _ {q} ^ {\mathrm{unr}}, k (1)) \to H ^ {1} (\mathbf {Q} _ {q} ^ {\mathrm{unr}}, (\mathcal {O} / \lambda^ {M}) (1))
$$

is nonzero on$x .$. But then x is not of type$\mathcal { D } ^ { * }$which gives a contradiction. This only leaves the possibility that$L = \mathbf { Q } ( \zeta _ { 3 } , \sqrt [ 3 ] { 3 } )$but again this means that$x$is not of type$\mathcal { D } ^ { * }$as locally at the prime above 3, L is not generated by the cube root of a unit over$\mathbf { Q } _ { 3 } ( \zeta _ { 3 } )$. This argument holds whether or not D is minimal.

So$x _ { i }$, which we view in ker$\bar { \varepsilon } _ { Q }$, gives a nontrivial Galois-equivalent homomorphism$f _ { x } \in \mathrm { H o m } ( \mathrm { G a l } ( \bar { \mathbf { Q } } / K _ { 0 } ( \zeta _ { p } ) ) , V _ { \lambda } ^ { * } )$which factors through an abelian extension$M _ { x }$of$K _ { 0 } ( \zeta _ { p } )$of exponent$p .$Specifically we choose$M _ { x }$to be the minimal such extension. Assume first that the projective representation$\tilde { \rho } _ { 0 }$ associated to$\rho _ { 0 }$is not dihedral so that$\mathrm { S y m } ^ { 2 } \rho _ { 0 }$is absolutely irreducible. Pick a$\sigma \in \operatorname { G a l } ( M _ { x } ( \zeta _ { p ^ { M } } ) / \mathbf { Q } )$satisfying

(3.9)

(i)$\rho _ { 0 } ( \sigma )$has order$m \geq 3$with$( m , p ) = 1$2

(ii)$\sigma$fixes$\mathbf { Q } ( \operatorname* { d e t } \rho _ { 0 } ) ( \zeta _ { p ^ { M } } )$2

(iii)$f _ { x } ( \sigma ^ { m } ) \neq 0 .$

To show that this is possible, observe first that the first two conditions can be achieved by Lemma 1.10(i) and the subsequent remark. Let$\sigma _ { 1 }$be an element satisfying (i) and (ii) and let$\bar { \sigma } _ { 1 }$denote its image in$\mathrm { G a l } ( K _ { 0 } ( \zeta _ { p } ) / \mathbf { Q } )$ Then$\left. { \bar { \sigma } _ { 1 } } \right.$acts on$G \ = \ \operatorname { G a l } ( M _ { x } / K _ { 0 } ( \zeta _ { p } ) )$and under this action G decomposes as$G \simeq G _ { 1 } \oplus G _ { 1 } ^ { \prime }$where$\sigma _ { 1 }$acts trivially on$G _ { 1 }$and without fixed points on$G _ { 1 } ^ { \prime }$. If X is any irreducible Galois stable <sup>¯</sup>k-subspace of$f _ { x } ( G ) \otimes _ { \mathbf { F } _ { p } } { \bar { k } }$then ker$( \sigma _ { 1 } - 1 ) | _ { X } \neq 0$since$\mathrm { S y m } ^ { 2 } \rho _ { 0 }$is assumed absolutely irreducible. So also ker$( \sigma _ { 1 } - 1 ) | _ { f _ { x } ( G ) } \neq 0$and thus we can find$\tau \in G _ { 1 }$such that$f _ { x } ( \tau ) \neq 0$ Viewing$\tau$as an element of$G$we then take

$$
\tau_ {1} = \tau \times 1 \in \operatorname{Gal} (M _ {x} (\zeta_ {p ^ {M}}) / K _ {0} (\zeta_ {p})) \simeq G \times \operatorname{Gal} (K _ {0} (\zeta_ {p ^ {M}}) / K _ {0} (\zeta_ {p}))
$$

(This decomposition holds because$M _ { x }$is minimal and because$\mathrm { S y m } ^ { 2 } \rho _ { 0 }$and $\mu _ { p }$are distinct from the trivial representation.) Now$\tau _ { 1 }$commutes with$\sigma _ { 1 }$and either$f _ { x } ( ( \tau _ { 1 } \sigma _ { 1 } ) ^ { m } ) \neq 0$or$f _ { x } ( \sigma _ { 1 } ^ { m } ) \neq 0$. Since$\rho _ { 0 } ( \tau _ { 1 } \sigma _ { 1 } ) = \rho _ { 0 } ( \sigma _ { 1 } )$this gives (3.9) with at least one of$\sigma = \tau _ { 1 } \sigma _ { 1 } \ \mathrm { o r } \ \sigma = \sigma _ { 1 }$. We may then choose q<sub>0</sub> so that $\mathrm { F r o b } q _ { 0 } = \sigma$and we will then have$\bar { \varepsilon } _ { Q _ { 0 } } ( x ) \neq 0$. Note that conditions (i) and (ii) imply that$q _ { 0 } \equiv 1 ( p )$and also that$\rho _ { 0 } ( \sigma )$has distinct eigenvalues, thus giving both the hypothses of Lemma 3.2.

If on the other hand$\tilde { \rho } _ { 0 }$is dihedral then we pick$\sigma _ { \mathrm { } } ^ { \prime } \mathrm { s }$satisfying

(i)$\tilde { \rho } _ { 0 } ( \sigma ) \ne 1$2

(ii) σ fixes$\mathbf { Q } ( \zeta _ { p ^ { M } } )$

(iii)$f _ { x } ( \sigma ^ { m } ) \neq 0 ,$

with m the order of$\rho _ { 0 } ( \sigma )$(and$p \nmid m$since$\tilde { \rho } _ { 0 }$is dihedral). The first two conditions can be achieved using Lemma 1.12 and, in addition, we can assume that σ takes the eigenvalue 1 on any given irreducible Galois stable subspace X of$W _ { \lambda } \otimes \bar { k }$. Arguing as above, we find$\mathrm { ~ a ~ } \tau \in G _ { 1 }$such that$f _ { x } ( \tau ) \neq 0$and we proceed as before. Again, conditions (i) and (ii) imply the hypotheses of Lemma 3.2. So by successively adjoining$q \mathrm { ^ { \circ } s }$we can assume that$Q$is chosen so that$\varepsilon _ { Q }$is injective.

We have thus shown that we can choose$Q = \{ q _ { 1 } , \ldots , q _ { r } \}$to be a finite set of primes$q _ { i } \equiv 1 ( p ^ { M } )$satisfying the hypotheses of Lemma 3.2 as well as the injectivity of$\varepsilon _ { Q }$in (3.8). By Proposition 1.6, the injectivity of$\varepsilon _ { Q }$implies that

$$
\# H _ {\mathcal {D}} ^ {1} (\mathbf {Q} _ {\Sigma \cup Q} / \mathbf {Q}, V _ {g} [ \lambda^ {M} ]) = h _ {\infty} \cdot \prod_ {q \in \Sigma \cup Q} h _ {q}.\tag{3.10}
$$

Here we are using the convention explained after Proposition 1.6 to define$H _ { \mathcal { D } } ^ { 1 }$ Now, as$\mathcal { D }$was chosen to be minimal,$h _ { q } = 1$for$q \in \sum - \{ p \}$by Proposition 1.8. Also,$h _ { q } = \# ( \mathcal { O } / \lambda ^ { M } ) ^ { 2 }$for$q \in Q$. If · is str or fl then$h _ { \infty } h _ { p } = 1$ by Proposition 1.9 (iv) and (v). If · is Se,$h _ { \infty } h _ { p } \leq c _ { p }$by Proposition 1.9 (iii). (To compute this we can assume that$I _ { p }$acts on$W _ { \lambda } ^ { 0 }$via$\omega ,$as otherwise we get$h _ { \infty } h _ { p } \leq 1$. Then with this hypothesis,$( W _ { \lambda ^ { n } } ^ { 0 } ) ^ { * }$is easily verified to be unramified with Frob$p$acting as$U _ { p } ^ { \mathrm { 2 } } \bar { \langle p \rangle } ^ { - 1 }$by the description of$\rho _ { f , \lambda } | _ { D _ { \boldsymbol { \tau } } }$in [Wi1, Th. 2.1.4].) On the other hand, we have constructed classes which are ramified at primes in$Q$in (3.7). These are of type$\mathcal { D } _ { Q }$. We also have classes in

$$
\mathrm{Hom} (\mathrm{Gal} (\mathbf {Q} _ {\Sigma \cup Q} / \mathbf {Q}), \mathcal {O} / \lambda^ {M}) = H ^ {1} (\mathbf {Q} _ {\Sigma \cup Q} / \mathbf {Q}, \mathcal {O} / \lambda^ {M}) \hookrightarrow H ^ {1} (\mathbf {Q} _ {\Sigma \cup Q} / \mathbf {Q}, V _ {\lambda^ {M}})
$$

coming from the cyclotomic extension$\mathbf { Q } ( \zeta _ { q _ { 1 } } \ldots \zeta _ { q _ { r } } )$. These are of type D and disjoint from the classes obtained from (3.7). Combining these with (3.10) gives

$$
\# H _ {\mathcal {D}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V _ {f} [ \lambda^ {M} ]) \leq t \cdot \# (\mathfrak {p} _ {\mathbf {T}} / \mathfrak {p} _ {\mathbf {T}} ^ {2}) \cdot c _ {p}
$$

as required. This proves part (i) of Theorem 3.1.

Now if we assume that T is a complete intersection we have that$t = 1$ by Proposition 2 of the appendix. In the strict or flat cases (and indeed in all cases where$c _ { p } = 1 )$this implies that$R _ { \mathcal { D } } \simeq \mathbf { T } _ { \mathcal { D } }$by Proposition 1 of the appendix together with Proposition 1.2. In the Selmer case we get

$$
\# (\mathfrak {p} _ {\mathbf {T}} / \mathfrak {p} _ {\mathbf {T}} ^ {2}) \cdot c _ {p} = \# (\mathcal {O} / \eta_ {\mathbf {T}, f}) c _ {p} = \# (\mathcal {O} / \eta_ {\mathbf {T} _ {\mathcal {D}, f}}) \leq \# (\mathfrak {p} _ {\mathbf {T} _ {\mathcal {D}}} / \mathfrak {p} _ {\mathbf {T} _ {\mathcal {D}}} ^ {2})\tag{3.11}
$$

where the central equality is by Remark 2.18 and the right-hand inequality is from the theory of Fitting ideals. Now applying part (i) we see that the inequality in (3.11) is an equality. By Proposition 2 of the appendix,$\mathbf { T } _ { \mathcal { D } }$is also a complete intersection.

The final assertion of the theorem is proved in exactly the same way on noting that we only used the minimality to ensure that the$h _ { q } \mathrm { ' s }$were 1. In general, they are bounded independently of M and easily computed. (The only point to note is that if$\rho _ { f , \lambda }$is multiplicative type at$q$then$\rho _ { f , \lambda | _ { D _ { q } } }$does not split.)

Remark. The ring$\mathbf { T } _ { \mathcal { D } _ { 0 } }$defined in (3.1) and used in this chapter should be the deformation ring associated to the following deformation prblem$\mathcal { D } _ { 0 }$ One alters D only by replacing the Selmer condition by the condition that the deformations be flat in the sense of Chapter 1, i.e., that each deformation$\rho$ of$\rho _ { 0 }$to$\operatorname { G L _ { 2 } } ( A )$has the property that for any quotient$A / { \mathfrak { a } }$of finite order, $\rho | _ { D _ { p } }$mod a is the Galois representation associated to the${ \bar { \mathbf { Q } } } _ { p } .$-points of a finite flat group scheme over$\mathbf { Z } _ { p }$. (Of course,$\rho _ { 0 }$is ordinary here in contrast to our usual assumption for flat deformations.)

From Theorem 3.1 we deduce our main results about representations by using the main result of [TW], which proves the hypothesis of Theorem 3.1 (ii), and then applying Theorem 2.17. More precisely, the main result of [TW] shows that T is a complete intersection and hence that$t = 1$as explained above. The hypothesis of Theorem 2.17 is then given by Theorem 3.1 (i), together with the equality t = 1 (and the central equality of (3.11) in the

Selmer case) and Proposition 1.2. Strictly speaking, Theorem 1 of [TW] refers to a slightly smaller class of$\mathcal { D } \mathrm { { s } }$than those covered by Theorem 3.1 but up to a twist every such D is covered. It is straightforward to see that it is enough to check Theorem 3.3 for$\rho _ { 0 }$up to a suitable twist.

Theorem 3.3. Assume that ρ is modular and absolutely irreducible when restricted to$\mathbf { Q } { \Big ( } { \sqrt { ( - 1 ) ^ { \frac { p - 1 } { 2 } } p } } { \Big ) }$. Assume also that$\rho _ { 0 }$is of type (A), (B) or (C) at each$q \neq p$in$\Sigma$. Then the map$\varphi _ { \mathcal { D } } : R _ { \mathcal { D } }  \mathbf { T } _ { \mathcal { D } }$of Conjecture 2.16 is an isomorphism for all D associated to$\rho _ { 0 }$, i.e., where$\mathcal { D } = ( \cdot , \Sigma , \mathcal { O } , \mathcal { M } )$with $\cdot = \mathrm { S e , s t r , \mathrm { { H } } }$or ord. In particular if$\mathrm { \Omega } \cdot \mathrm { \Omega } = \mathrm { S e } .$, str or fl and f is any newform for which$\rho _ { f , \lambda }$is a deformation of ρ<sub>0</sub> of type D then

$$
\# H _ {\mathcal {D}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V _ {f}) = \# (\mathcal {O} / \eta_ {\mathcal {D}, f}) <   \infty
$$

where$\eta _ { \mathscr { D } , f }$is the invariant defined in Chapter 2 prior to (2.43).

The condition at$q \neq p$in Σ ensures that there is a minimal D associated to$\rho _ { 0 }$. The computation of the Selmer group follows from Theorem 2.17 and Proposition 1.2. Theorem 0.2 of the introduction follows from Theorem 3.3, after it is checked that a twist of a$\rho _ { 0 }$as in Theorem 0.2 satisfies the hypotheses of Theorem 3.3.

## Chapter 4

In this chapter we give a diferent (and slightly more general) derivation of the bound for the Selmer group in the CM case. In the first section we estimate the Selmer group using the main theorem of [Ru 4] which is based on Kolyvagin’s method. In the second section we use a calculation of Hida to relate the η-invariant to special values of an L-function. Some of these computations are valid in the non-CM case also. They are needed if one wishes to give the order of the Selmer group in terms of the special value of an L-function.

## 1. The ordinary CM case

In this section we estimate the order of the Selmer group in the ordinary CM case. In Section 1 we use the proof of the main conjecture by Rubin to bound the Selmer group in terms of an L-function. The methods are standard (cf. [de Sh]) and some special cases have been described elsewhere (cf. [Guo]). In Section 2 we use a calculation of Hida to relate this to the η-invariant.

We assume that

$$
\rho = \mathrm{Ind} _ {L} ^ {\mathbf {Q}} \kappa : \mathrm{Gal} (\bar {\mathbf {Q}} / \mathbf {Q}) \to \mathrm{GL} _ {2} (\mathcal {O})\tag{4.1}
$$

is the p-adic representation associated to a character$\kappa : \operatorname { G a l } ( \overline { { L } } / L ) \to \mathcal { O } ^ { \times }$of an imaginary quadratic field$L$. We assume that$p$is unramified in$L$and that$\kappa$ factors through an extension of L whose Galois group has the form$A \simeq \mathbf { Z } _ { p }$⊕T where$T$is a finite group of order prime to$p .$The ring$\mathcal { O }$is assumed to be the ring of integers of a local field with maximal ideal λ and we also assume that $\rho$is a Selmer deformation of$\rho _ { 0 } = \rho$mod λ which is supposed irreducible with det$\rho _ { 0 } | _ { I _ { p } } = \omega$. In particular it follows that$p$splits in$L , p = { \mathfrak { p } } { \bar { \mathfrak { p } } }$say, and that precisely one of$\kappa , \kappa ^ { * }$is ramified at p$\left( \kappa ^ { * } \right.$being the character$\tau \to \kappa ( \sigma \tau \sigma ^ { - 1 } )$ for any$\sigma$representing the nontrivial coset in$\operatorname { G a l } ( { \bar { \mathbf { Q } } } / \mathbf { Q } ) / \operatorname { G a l } ( { \bar { \mathbf { Q } } } / L ) )$. We can suppose without loss of generality that$\kappa$is ramified at p.

We consider the representation module$V \simeq ( K / \mathcal { O } ) ^ { 4 }$(where K is the field of fractions of O) and the representation is Ad$\rho .$. In this case V splits as

$$
V \simeq Y \oplus (K / \mathcal {O}) (\psi) \oplus K / \mathcal {O}
$$

where$\psi$is the quadratic character of$\operatorname { G a l } ( { \bar { \mathbf { Q } } } / \mathbf { Q } )$associated to$L$. We let Σ denote a finite set of primes including all those which ramify in$\rho$(and in particular$p )$. Our aim is to compute$H _ { \mathrm { S e } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V )$. The decomposition of $V$gives a corresponding decomposition of$H ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V )$and we can use it to define$H _ { \mathrm { S e } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , Y )$. Since$W ^ { \bar { 0 } } \subset Y$(see Chapter 1 for the definition of$W ^ { 0 } )$ we can define$H _ { \mathrm { S e } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , Y )$by

$$
H _ {\mathrm{Se}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y) = \ker \{H ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y) \to H ^ {1} (\mathbf {Q} _ {p} ^ {\mathrm{unr}}, Y / W ^ {0}) \}.
$$

Let$Y ^ { * }$be the arithmetic dual of$Y .$, i.e., Hom$( Y , \pmb { \mu } _ { p ^ { \infty } } ) \otimes \mathbf { Q } _ { p } / \mathbf { Z } _ { p }$. Where $\nu$for$\kappa \varepsilon / \kappa ^ { * }$and let$L ( \nu )$be the splitting field of$\nu .$Then we claim that Gal$\left( L ( \nu ) / L \right) \simeq \mathbf { Z } _ { p } \oplus T ^ { \prime }$with$T ^ { \prime }$a finite group of order prime to$p$. For this it is enough to show that$\chi = \kappa \kappa ^ { * } / \varepsilon$factors through a group of order prime to$p$since$\nu = \kappa ^ { 2 } \chi ^ { - 1 }$. Suppose that$\chi$has order$m = m _ { 0 } p ^ { r }$with$( m _ { 0 } , p ) = 1$ Then$\chi ^ { m _ { 0 } }$extends to a character of$\mathbf { Q }$which is then unramified at$p$since the same is true of$\chi$. Also it factors through an abelian extension of$L$with Galois group isomorphic to$\mathbf { Z } _ { { n } } ^ { 2 }$since$\chi$factors through such an extension with Galois group isomorphic to$\mathbf { Z } _ { p } ^ { 2 } \oplus T _ { 1 }$with$T _ { 1 }$of order prime to$p$(the composite of the splitting fields of$\kappa$and$\kappa ^ { * } )$. It follows that$\chi ^ { m _ { 0 } }$is also unramified outside$p ,$ whence it is trivial. This proves the claim.

Over$L$there is an isomorphism of Galois modules

$$
Y ^ {*} \simeq (K / \mathcal {O}) (\nu) \oplus (K / \mathcal {O}) (\nu^ {- 1} \varepsilon^ {2}).
$$

In analogy to the above we define$H _ { \mathrm { S e } } ^ { 1 } ( { \bf Q } _ { \Sigma } / { \bf Q } , Y ^ { * } )$by

$$
H _ {\mathrm{Se}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y ^ {*}) = \ker \{H ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y ^ {*}) \to H ^ {1} (\mathbf {Q} _ {p} ^ {\mathrm{unr}}, (W ^ {0}) ^ {*}) \}.
$$

Analogous definitions apply if$Y ^ { * }$is replaced by$Y _ { \lambda ^ { n } } ^ { * }$. Also we say informally that a cohomology class is Selmer at$p$if it vanishes in$H ^ { 1 } ( \mathbf { Q } _ { p } ^ { \mathrm { u n r } } , ( W ^ { 0 } ) ^ { * } )$(resp.

$H ^ { 1 } ( \mathbf { Q } _ { p } ^ { \mathrm { u n r } } , ( W _ { \lambda ^ { n } } ^ { 0 } ) ^ { * } ) \big )$. Let$M _ { \infty }$be the maximal abelian p-extension of$L ( \nu )$unramified outside p. The following proposition generalizes [CS, Prop. 5.9].

Proposition 4.1. There is an isomorphism

$$
H _ {\mathrm{unr}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y ^ {*}) \xrightarrow {\sim} \mathrm{Hom} (\mathrm{Gal} (M _ {\infty} / L (\nu)), (K / \mathcal {O}) (\nu)) ^ {\mathrm{Gal} (L (\nu) / L)}
$$

where$H _ { \mathrm { u n r } } ^ { 1 }$denotes the subgroup of classes which are Selmer at p and unramified everywhere else.

Proof. The sequence is obtained from the inflation-restriction sequence as follows. First we can replace$H ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , Y ^ { * } )$by

$$
\left. \right.\left\{H ^ {1} \left(\mathbf {Q} _ {\Sigma} / L, (K / \mathcal {O}) (\nu)\right) \oplus H ^ {1} \left(\mathbf {Q} _ {\Sigma} / L, (K / \mathcal {O}) \left(\nu^ {- 1} \varepsilon^ {2}\right)\right)\right\} ^ {\Delta}
$$

where$\Delta \ = \ \operatorname { G a l } ( L / \mathbf { Q } )$. The unramified condition then translates into the requirement that the cohomology class should lie in

$$
\left. \left\{H _ {\text {unr in} \Sigma - \mathfrak {p}} ^ {1} (\mathbf {Q} _ {\Sigma} / L, (K / \mathcal {O}) (\nu)) \oplus H _ {\text {unr in} \Sigma - \mathfrak {p} ^ {*}} ^ {1} \left(\mathbf {Q} _ {\Sigma} / L, (K / \mathcal {O}) \left(\nu^ {- 1} \varepsilon^ {2}\right)\right) \right\} ^ {\Delta}. \right.
$$

Since$\Delta$interchanges the two groups inside the parentheses it is enough to compute the first of them, i.e.,

$$
H _ {\mathrm{unr} \mathrm{in} \Sigma - \mathfrak {p}} ^ {1} (\mathbf {Q} _ {\Sigma} / L, K / \mathcal {O} (\nu)).\tag{4.2}
$$

The inflation-restriction sequence applied to this gives an exact sequence

$$
\begin{array}{r l} & 0 \to H _ {\mathrm{unrin} \Sigma - \mathfrak {p}} ^ {1} (L (\nu) / L, (K / \mathcal {O}) (\nu)) \\ & \to H _ {\mathrm{unrin} \Sigma - \mathfrak {p}} ^ {1} (\mathbf {Q} _ {\Sigma} / L, (K / \mathcal {O}) (\nu)) \\ & \to \mathrm{Hom} (\mathrm{Gal} (M _ {\infty} / L (\nu)), (K / \mathcal {O}) (\nu)) ^ {\mathrm{Gal} (L (\nu) / L)}. \end{array}\tag{4.3}
$$

The first term is zero as one easily check using the divisibility of$( K / \mathcal { O } ) ( \nu )$ Next note that$H ^ { 2 } ( L ( \nu ) / L , ( K / \mathcal { O } ) ( \nu ) )$is trivial. If$\nu \not \equiv 1 ( \lambda )$this is straightforward (cf. Lemma 2.2 of$\mathrm { [ R u l ] } )$. If$\nu \equiv 1 ( \lambda )$then$\mathrm { G a l } ( L ( \nu ) / L ) \simeq \mathbf { Z } _ { p }$and so it is trivial in this case also. It follows that any class in the final term of (4.3) lifts to a class c in$H ^ { 1 } ( \mathbf { Q } _ { \Sigma } / L , ( K / \mathcal { O } ) ( \nu ) )$. Let$L _ { 0 }$be the splitting field of$Y _ { \lambda } ^ { * }$ Then$M _ { \infty } L _ { 0 } / L _ { 0 }$is unramified outside p and$L _ { 0 } / L$has degree prime to$p .$. It follows that$c$is unramified outside p.

Now write$H _ { \mathrm { s t r } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , Y _ { n } ^ { * } )$(where$Y _ { n } ^ { * } = Y _ { \lambda ^ { n } } ^ { * }$and similarly for$Y _ { n } )$for the supgroup of$H _ { \mathrm { u n r } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , Y _ { n } ^ { * } )$given by

$$
H _ {\mathrm{str}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y _ {n} ^ {*}) = \left\{\alpha \in H _ {\mathrm{unr}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y _ {n} ^ {*}): \alpha_ {p} = 0 \text {in} H ^ {1} (\mathbf {Q} _ {p}, Y _ {n} ^ {*} / (Y _ {n} ^ {*}) ^ {0}) \right\}
$$

where$( Y _ { n } ^ { * } ) ^ { 0 }$is the first step in the filtration under$D _ { p } ,$thus equal to$( Y _ { n } / Y _ { n } ^ { 0 } ) ^ { * }$ or equivalently to$( Y ^ { * } ) _ { \lambda ^ { r } } ^ { 0 }$<sub>n</sub> where$( Y ^ { * } ) ^ { 0 }$is the divisible submodule of$Y ^ { * }$on which the action of$I _ { p }$is via$\varepsilon ^ { 2 }$. (If$p \neq 3$one can characterize$( Y _ { n } ^ { * } ) ^ { 0 }$as the maximal submodule on which$I _ { p }$acts via$\varepsilon ^ { 2 } . )$A similar definition applies with $Y _ { n }$replacing$Y _ { n } ^ { * }$. It follows from an examination of the action of$I _ { p }$on$Y _ { \lambda }$that

$$
H _ {\mathrm{str}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y _ {n}) = H _ {\mathrm{unr}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y _ {n}).\tag{4.4}
$$

In the case of$Y ^ { * }$we will use the inequality

$$
\# H _ {\mathrm{str}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y ^ {*}) \leq \# H _ {\mathrm{unr}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y ^ {*}).\tag{4.5}
$$

We also need the fact that for n suficiently large the map

$$
H _ {\mathrm{str}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y _ {n} ^ {*}) \rightarrow H _ {\mathrm{str}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y ^ {*})\tag{4.6}
$$

is injective. One can check this by replacing these groups by the subgroups of$H ^ { 1 } ( L , ( K / \mathcal { O } ) ( \nu ) _ { \lambda ^ { n } } )$and$H ^ { 1 } ( L , ( K / \mathcal { O } ) ( \nu ) )$which are unramified outside p and trivial at$\mathfrak { p } ^ { * }$, in a manner similar to the beginning of the proof of Proposition 4.1. the above map is then injective whenever the connecting homomorphism

$$
H ^ {0} (L _ {\mathfrak {p} ^ {*}}, (K / \mathcal {O}) (\nu)) \rightarrow H ^ {1} (L _ {\mathfrak {p} ^ {*}}, (K / \mathcal {O}) (\nu) _ {\lambda^ {n}})
$$

is injective, which holds for suficiently large n.

Now, by Propsition 1.6,

$$
\frac {\# H _ {\mathrm{str}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q} , Y _ {n})}{\# H _ {\mathrm{str}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q} , Y _ {n} ^ {*})} = \# H ^ {0} (\mathbf {Q} _ {p}, (Y _ {n} ^ {0}) ^ {*}) \frac {\# H ^ {0} (\mathbf {Q} , Y _ {n})}{\# H ^ {0} (\mathbf {Q} , Y _ {n} ^ {*})}.\tag{4.7}
$$

Also,$H ^ { 0 } ( \mathbf { Q } , Y _ { n } ) = 0$and a simple calculation shows that

$$
\# H ^ {0} (\mathbf {Q}, Y _ {n} ^ {*}) = \left\{ \begin{array}{l l} \inf _ {\mathfrak {q}} \# (\mathcal {O} / 1 - \nu (\mathfrak {q})) & \text { if } \nu = 1 \mod \lambda \\ 1 & \text { otherwise } \end{array} \right.
$$

where q runs through a set of primes of$\mathcal { O } _ { L }$prime to$p \mathrm { c o n d } ( \nu )$of density one. This can be checked since$Y ^ { * } = \mathrm { I n d } _ { L } ^ { \mathbf { Q } } ( \nu ) \otimes _ { \mathcal { O } } K / \mathcal { O }$. So, setting

$$
t = \left\{ \begin{array}{l l} \inf _ {\mathfrak {q}} \# (\mathcal {O} / (1 - \nu (\mathfrak {q}))) & \text {if} \nu \mod \lambda = 1 \\ 1 & \text {if} \nu \mod \lambda \neq 1 \end{array} \right.\tag{4.8}
$$

we get

$$
\# H _ {\mathrm{Se}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y) \leq \frac {1}{t} \cdot \prod \ell_ {q} \cdot \# \mathrm{Hom} (\mathrm{Gal} (M _ {\infty} / L (\nu)), (K / \mathcal {O}) (\nu)) ^ {\mathrm{Gal} (L (\nu) / L)}\tag{4.9}
$$

where$\ell _ { q } = \# H ^ { 0 } ( \mathbf { Q } _ { q } , Y ^ { * } )$for$q \neq p , \ell _ { p } = \operatorname* { l i m } _ { n  \infty } \# H ^ { 0 } ( \mathbf { Q } _ { p } , ( Y _ { n } ^ { 0 } ) ^ { * } )$. This follows from Proposition 4.1, (4.4)-(4.7) and the elementary estimate

$$
\# (H _ {\mathrm{Se}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y) / H _ {\mathrm{unr}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y)) \leq \prod_ {q \in \Sigma - \{p \}} \ell_ {q},\tag{4.10}
$$

which follows from the fact that #$H ^ { 1 } ( \mathbf { Q } _ { q } ^ { \mathrm { u n r } } , Y ) ^ { \mathrm { G a l } ( \mathbf { Q } _ { q } ^ { \mathrm { u n r } } / \mathbf { Q } _ { q } ) } = \ell _ { q } .$

Our objective is to compute$H _ { \mathrm { S e } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V )$and the main problem is to estimate$H _ { \mathrm { S e } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , Y )$. By (4.5) this in turn reduces to the problem of estimating

#Hom$( \mathrm { G a l } ( M _ { \infty } / L ( \nu ) ) , ( K / \mathcal { O } ) ( \nu ) ) ^ { \mathrm { G a l } ( L ( \nu ) / L ) } )$. This order can be computed using the ‘main conjecture’ established by Rubin using ideas of Kolyvagin. (cf. [Ru2] and especially [Ru4]. In the former reference Rubin assumes that the class number of L is prime to$p . )$We could now derive the result directly from this by referring to [de Sh, Ch.3], but we will recall some of the steps here.

Let$w _ { \mathsf { f } }$denote the number of roots of unity$\zeta$of L such that$\zeta \equiv 1$mod f (f an integral ideal of$\mathcal { O } _ { L } )$.We choose an f prime to$p$such that$w _ { \mathsf { f } } ~ = ~ 1$ Then there is a grossencharacter$\varphi$of$L$satisfying$\varphi ( ( \alpha ) ) = \alpha$for$\alpha \equiv 1$mod f (cf. [de Sh, II.1.4]). According to Weil, after fixing an embedding$\bar { \mathbf { Q } } \hookrightarrow \bar { \mathbf { Q } } _ { p }$we can asssociate a p-adic character$\varphi _ { p }$to$\varphi$(cf. [de Sh, II.1.1 (5)]). We choose an embedding corresponding to a prime above p and then we find$\varphi _ { p } = \kappa \cdot \chi$ for some$\chi$of finite order and conductor prime to$p .$Indeed$\varphi _ { p }$and$\kappa$are both unramified at$\mathfrak { p } ^ { * }$and satisfy$\varphi _ { p } | _ { I _ { \mathfrak { p } } } = \kappa | _ { I _ { \mathfrak { p } } } = \varepsilon$where$\varepsilon$is the cyclotomic character and$I _ { \mathfrak { p } }$is an inertia group at p. Without altering f we can even choose $\varphi$so that the order of$\chi$is prime to$p .$This is by our hyppothesis that κ factored through an extension of the form$\mathbf { Z } _ { p } \oplus T$with$T$of order prime to$p .$. To see this pick an abelian splitting field of$\varphi _ { p }$and κ whose Galois group has the form $G \oplus G ^ { \prime }$with$G$a pro-p-group and$G ^ { \prime }$of order prime to$p .$. Then we see that $\varphi | _ { G }$has conductor dividing$\mathfrak { f p } ^ { \infty }$. Also the only primes which ramify in a$\mathbf { Z } _ { p ^ { - } }$ extension lie above$p$so our hypothesis on$\kappa$ensures that$\kappa | _ { G }$has conductor dividing${ \mathfrak { f p } } ^ { \infty }$. The same is then true of the p-part of$\chi$which therefore has conductor dividing f. We can therefore adjust$\varphi$so that$\chi$has order prime to$p$as claimed. We will not however choose$\varphi$so that$\chi$is 1 as this would require${ \mathfrak { f p } } ^ { \infty }$to be divisible by cond$\chi$However we will make the assumption, by altering f if necessary, but still keeping f prime to$p ,$that both$\nu$and$\varphi _ { p }$ have conductor dividing$\mathbf { \boldsymbol { f } } \mathbf { \boldsymbol { p } } ^ { \infty }$. Thus we replace$\mathfrak { f p } ^ { \infty }$by l.c.m.{f, cond$\nu \}$

The grossencharacter$\varphi$(or more precisely$\varphi \circ N _ { F / L } )$is associated to a (unique) elliptic curve E defined over$F = L ( \mathfrak { f } )$, the ray class field of conductor f, with complex multiplication by$\mathcal { O } _ { L }$and isomorphic over C to$\mathbf { C } / { \mathcal { O } } _ { L }$(cf. [de Sh, II. Lemma 1.4]). We may even fix a Weierstrass model of E over${ \mathcal { O } } _ { F }$ which has good reduction at all primes above p. For each prime$\mathfrak { P }$of$F$above p we have a formal group$\hat { E } _ { \mathfrak { P } }$, and this is a relative Lubin-Tate group with respect to$F _ { \mathfrak { P } }$over$L _ { \mathfrak { p } }$(cf. [de Sh, Ch. II, §1.10]). We let$\lambda = \lambda _ { \hat { E } _ { \mathfrak { P } } }$be the logarithm of this formal group.

Let$U _ { \infty }$be the product of the principal local units at the primes above p of$L ( { \mathfrak { f p } } ^ { \infty } )$; i.e.,

$$
U _ {\infty} = \prod_ {\mathfrak {P} | \mathfrak {p}} U _ {\infty , \mathfrak {P}} \quad \text { where } \quad U _ {\infty , \mathfrak {P}} = \varprojlim U _ {n}, \mathfrak {P},
$$

each$U _ { n , \mathfrak { P } }$being the principal local units in$L ( { \mathfrak { f } } { \mathfrak { p } } ^ { n } ) _ { \mathfrak { P } }$. (Note that the primes of$L ( \mathfrak { f } )$above p are totally ramified in$L ( { \mathfrak { f p } } ^ { \infty } )$so we still call them$\{ \mathfrak { P } \} . )$We wish to define certain homomorphisms$\delta _ { k }$on$U _ { \infty }$. These were first introduced in [CW] in the case where the local field$F _ { \mathfrak { P } }$is$\mathbf { Q } _ { p }$

Assume for the moment that$F _ { \mathfrak { P } }$is$\mathbf { Q } _ { p }$. In this case$\hat { E } _ { \mathfrak { P } }$is isomorphic to the Lubin-Tate group associated to$\pi x + x ^ { p }$where$\pi = \varphi ( { \mathfrak { p } } )$. Then letting$\omega _ { n }$ be nontrivial roots of$[ \pi ^ { n } ] ( x ) = 0$chosen so that$[ \pi ] ( \omega _ { n } ) = \omega _ { n - 1 }$, it was shown in [CW] that to each element$u = \operatorname* { l i m } u _ { n } \in U _ { \infty , \mathfrak { P } }$there corresponded a unique power series$f _ { u } ( T ) \in \mathbf { Z } _ { p } [ [ T ] ] ^ { \times }$such that$f _ { u } ( \omega _ { n } ) = u _ { n }$for$n \geq 1$. The definition of$\delta _ { k , \mathfrak { P } } ( k \geq 1 )$in this case was then

$$
\delta_ {k, \mathfrak {P}} (u) = \left(\frac {1}{\lambda^ {\prime} (T)} \frac {d}{d T}\right) ^ {k} \log f _ {n} (T) \Bigg | _ {T = 0}.
$$

It is easy to see that$\delta _ { k , \mathfrak { P } }$gives a homomorphism:$U _ { \infty } \to U _ { \infty , \mathfrak { P } } \to \mathcal { O } _ { \mathfrak { p } }$satisfying $\delta _ { k , \mathfrak { P } } ( \varepsilon ^ { \sigma } ) = \theta ( \sigma ) ^ { k } \delta _ { k , \mathfrak { P } } ( \varepsilon )$where$\theta : \mathrm { G a l } \Big ( \overline { { F } } / F \Big )  \mathcal { O } _ { \mathfrak { p } } ^ { \times }$is the character giving the action on$E [ { \mathfrak { p } } ^ { \infty } ]$

The construction of the power series in [CW] does not extend to the case where the formal group has height$> 1$or to the case where it is defined over an extension of$\mathbf { Q } _ { p }$. A more natural approach was developed bt Coleman [Co] which works in general. (See also [Iw1].) The corresponding generalizations of $\delta _ { k }$were given in somewhat greater generality in [Ru3] and then in full generality by de Shalit [de Sh]. We now summarize these results, thus returning to the general case where$F _ { \mathfrak { P } }$is not assumed to be$\mathbf { Q } _ { p }$

To an element u = lim$u _ { n } \in U _ { \infty }$we can associate a power series$f _ { u , \mathfrak { P } } ( T ) \in$ $\mathcal { O } _ { \mathfrak { P } } [  { \mathbb { T } } ] ^ { \times }$where${ \mathcal { O } } _ { \mathfrak { P } }$is the ring of integers of$F _ { \mathfrak { P } } { \mathrm { ; } }$; see [de Sh, Ch. II §4.5]. (More precisely$f _ { u , \mathfrak { P } } ( T )$is the P-component of the power series described there.) For P we will choose the prime above p corresponding to our chosen embedding $\overline { { \mathbf { Q } } } \hookrightarrow \overline { { \mathbf { Q } } } _ { p }$. This power series satisfies$u _ { n , \mathfrak { P } } = ( f _ { u , \mathfrak { P } } ) ( \omega _ { n } )$for all$n > 0 , n \equiv 0 ( d )$ where$\dot { d } = [ F _ { \mathfrak { P } } : L _ { \mathfrak { p } } ]$and$\left\{ \omega _ { n } \right\}$is chosen as before as an inverse system of$\pi ^ { n }$ division points of$\hat { E } _ { \mathfrak { P } }$. We define a homomorphism$\delta _ { k } : U _ { \infty } \to \mathcal { O } _ { \mathfrak { P } }$by

$$
\delta_ {k} (u) := \delta_ {k, \mathfrak {P}} (u) = \left(\frac {1}{\lambda_ {\hat {E} _ {\mathfrak {P}}} ^ {\prime} (T)} \frac {d}{d T}\right) ^ {k} \log f _ {u, \mathfrak {P}} (T) \bigg | _ {T = 0}.\tag{4.11}
$$

Then

$$
\delta_ {k} (u ^ {\tau}) = \theta (\tau) ^ {k} \delta_ {k} (u) \quad \text { for } \tau \in \operatorname{Gal} (\bar {F} / F)\tag{4.12}
$$

where$\theta$again denotes the action on$E [ \mathfrak { p } ^ { \infty } ]$. Now$\theta = \varphi _ { p }$on$\operatorname { G a l } ( { \bar { F } } / F )$. We actually want a homomorphism on$u _ { \infty }$with a transformation property corresponding to$\nu$on all of$\operatorname { G a l } ( { \bar { L } } / L )$. Observe that$\nu = \varphi _ { p } ^ { 2 }$on$\operatorname { G a l } ( { \bar { F } } / F )$. Let$S$ be a set of coset representatives for$\operatorname { G a l } ( { \bar { L } } / L ) / \operatorname { G a l } ( { \bar { L } } / F )$and define

$$
\Phi_ {2} (u) = \sum_ {\sigma \in S} \nu^ {- 1} (\sigma) \delta_ {2} (u ^ {\sigma}) \in \mathcal {O} _ {\mathfrak {P}} [ \nu ].\tag{4.13}
$$

Each term is independent of the choice of coset representative by (4.8) and it is easily checked that

$$
\Phi_ {2} (u ^ {\sigma}) = \nu (\sigma) \Phi_ {2} (u).
$$

It takes integral values in$\mathcal { O } _ { \mathfrak { P } } [ \nu ]$. Let$U _ { \infty } ( \nu )$denote the product of the groups of local principal units at the primes above p of the field$L ( \nu )$(by which we mean projective limis of local principal units as before). Then$\Phi _ { 2 }$factors through$U _ { \infty } ( \nu )$and thus defines a continuous homomorphism

$$
\Phi_ {2}: U _ {\infty} (\nu) \to \mathbf {C} _ {p}.
$$

Let$\mathcal { C } _ { \infty }$be the group of projective limits of elliptic units in$L ( \nu )$as defined in [Ru4]. Then we have a crucial theorem of Rubin (cf. [Ru4], [Ru2]), proved using the ideas of Kolyvagin:

Theorem 4.2. There is an equality of characteristic ideals as$\Lambda \ =$ ${ \bf Z } _ { p } [ [ \mathrm { G a l } ( L ( \nu ) / L ) ] ]$-modules:

$$
\operatorname{char} _ {\wedge} (\operatorname{Gal} (M _ {\infty} / L (\nu))) = \operatorname{char} _ {\wedge} (U _ {\infty} (\nu) / \overline {{\mathcal {C}}} _ {\infty}).
$$

Let$\nu _ { 0 } = \nu$mod λ. For any$\mathbf { Z } _ { p } [ \mathrm { G a l } ( L ( \nu _ { 0 } ) / L ) ]$]-module X we write$X ^ { ( \nu _ { 0 } ) }$ for the maximal quotient of X$_ { \mathbf { z } _ { p } } ^ { \otimes \mathcal { O } }$on which the action of$\operatorname { G a l } ( L ( \nu _ { 0 } ) / L )$is via the Teichm¨uller lift of$\nu _ { 0 }$. Since$\operatorname { G a l } ( L ( \nu ) / L )$decomposes into a direct product of a pro-p group and a group of order prime to$p ,$

$$
\operatorname{Gal} (L (\nu) / L) \simeq \operatorname{Gal} (L (\nu) / L (\nu_ {0})) \times \operatorname{Gal} (L (\nu_ {0}) / L),
$$

we can also consider any$\mathbf { Z } _ { p } [ [ \operatorname { G a l } ( L ( \nu ) / L ) ] ]$-module also as a$\begin{array} { r } { \mathbf { Z } _ { p } [ \mathrm { G a l } ( L ( \nu _ { 0 } ) / L ) ] . } \end{array}$ module. In particular$X ^ { ( \nu _ { 0 } ) }$is a module over$\mathbf { Z } _ { p } [ \operatorname { G a l } ( L ( \nu _ { 0 } ) / L ) ] ^ { ( \nu _ { 0 } ) } \simeq \mathcal { O }$. Also $\Lambda ^ { \nu _ { 0 } ) } \simeq \mathcal { O } [ [ T ] ]$

Now according to results of Iwasawa ([Iw2, §12], [Ru2, Theorem 5.1]), $U _ { \infty } ( \nu ) ^ { ( \nu _ { 0 } ) }$is a free$\Lambda ^ { ( \nu _ { 0 } ) }$-module of rank one. We extend$\Phi _ { 2 }$O-linearly to $U _ { \infty } ( \nu ) \otimes \mathbf { z } _ { p } \mathcal { O }$and it then factors through$U _ { \infty } ( \nu ) ^ { ( \nu _ { 0 } ) }$. Suppose that u is a generator of$U _ { \infty } ( \nu ) ^ { ( \nu _ { 0 } ) }$and$\beta$an element of$\bar { \mathcal { C } } _ { \infty } ^ { ( \nu _ { 0 } ) }$. Then$f ( \gamma - 1 ) u = \beta$for some $f ( T ) \in { \mathcal { O } } [ [ T ] ]$and γ a topological generator of$\operatorname { G a l } ( L ( \nu ) / L ( \nu _ { 0 } ) )$. Computing $\Phi _ { 2 }$on both u and$\beta$gives

$$
f (\nu (\gamma) - 1) = \phi_ {2} (\beta) / \Phi_ {2} (u).\tag{4.14}
$$

Next we let$e ( { \mathfrak { a } } )$be the projective limit of elliptic units in lim$L _ { \mathfrak { f p } ^ { n } } ^ { \times }$for a some ideal prime to 6fp described in [de Sh, Ch. II,§4.9]. Then by the proposition of Chapter II, §2.7 of [de Sh] this is a$1 2 ^ { \mathrm { t h } }$power in lim$L _ { \mathfrak { f p } ^ { n } } ^ { \times }$. We let$\beta _ { 1 } = \beta ( { \mathfrak { a } } ) ^ { 1 / 1 2 }$be the projection of$e ( \mathfrak { a } ) ^ { 1 / 1 2 }$to$U _ { \infty }$and take$\beta = \mathrm { N o r m } \beta _ { 1 }$ where the norm is from$L _ { \mathfrak { f p } ^ { \infty } }$to$L ( \nu )$. A generalization of the calculation in [CW] which may be found in [de Sh, Ch. II, §4.10] shows that

$$
\Phi_ {2} (\beta) = (\text { root   of   unity }) \Omega^ {- 2} (N \mathfrak {a} - \nu (\mathfrak {a})) L _ {\mathfrak {f}} (2, \bar {\nu}) \in \mathcal {O} _ {\mathfrak {P}} [ \nu ]\tag{4.15}
$$

where Ω is a basis for the$\mathcal { O } _ { L }$-module of periods of our chosen Weierstrass model of$E _ { / F }$. (Recall that this was chosen to have good reduction at primes above p. The periods are those of the standard Neron diferential.) Also ν here should be interpreted as the grossencharacter whose associated p-adic character, via the chosen embedding$\overline { { \mathbf { Q } } } \hookrightarrow \overline { { \mathbf { Q } } } _ { p } ,$$\nu ,$and ν is the complex conjugate of$\nu .$

The only restrictions we have placed on f are that (i) f is prime to p; (ii)$w _ { \mathfrak { f } } = 1$; and (iii) cond$\nu | \mathfrak { f p } ^ { \infty }$. Now let$\boldsymbol { \mathfrak { f } } _ { 0 } \boldsymbol { \mathfrak { p } } ^ { \infty }$be the conductor of ν with f<sub>0</sub> prime to$p .$We show now that we can choose f such that$L _ { \mathfrak { f } } ( 2 , \overline { { \nu } } ) / L _ { \mathfrak { f } _ { 0 } } ( 2 , \overline { { \nu } } )$is a p-adic unit unless$\nu _ { 0 } = 1$in which case we can choose it to be t as defined in (4.4). We can clearly choose$L _ { \mathfrak { f } } ( 2 , \overline { { \nu } } ) / L _ { \mathfrak { f } _ { 0 } } ( 2 , \overline { { \nu } } )$to be a unit if$\nu _ { 0 } \neq 1$, as $\overline { { \nu } } ( \mathfrak { q } ) \nu ( \mathfrak { q } ) = \mathrm { N o r m } \mathfrak { q } ^ { 2 }$for any ideal q prime to f<sub>0</sub>p. Note that if$\nu _ { 0 } = 1$then also $p = 3$. Also if$\nu _ { 0 } = 1$then we see that

$$
\inf _ {\mathfrak {q}} \# \left\{\mathcal {O} / \left\{L _ {\mathfrak {f} _ {0} \mathfrak {q}} (2, \overline {{\nu}}) / L _ {\mathfrak {f} _ {0}} (2, \overline {{\nu}}) \right\} \right\} = t
$$

since$\overline { { \nu } } \varepsilon ^ { - 2 } = \nu ^ { - 1 }$

We can compute$\Phi _ { 2 } ( u )$by choosing a special local unit and showing that $\Phi _ { 2 } ( u )$is a p-adic unit, but it is suficient for us to know that it is integral. Then since$\mathrm { G a l } ( M _ { \infty } / L ( \nu ) )$has no finite Λ-submodule (by a result of Greenberg; see [Gre2, end of §4]) we deduce from Theorem 4.2, (4.14) and (4.15) that

$$
\begin{array}{l} \# \text {Hom} (\text {Gal} (M _ {\infty} / L (\nu)), (K / \mathcal {O}) (\nu)) ^ {\text {Gal} (L (\nu) / L)} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \leq \left\{ \begin{array}{l l} \# \mathcal {O} / \Omega^ {- 2} L _ {\mathfrak {f} _ {0}} (2, \bar {\nu}) & \text {if} \nu_ {0} \neq 1 \\ (\# \mathcal {O} / \Omega^ {- 2} L _ {\mathfrak {f} _ {0}} (2, \bar {\nu})) \cdot t & \text {if} \nu_ {0} = 1. \end{array} \right. \end{array}
$$

Combining this with (4.9) gives:

$$
\# H _ {\mathrm{Se}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, Y) \leq \# \Big (\mathcal {O} / \Omega^ {- 2} L _ {\mathfrak {f} _ {0}} (2, \bar {\nu}) \Big) \cdot \prod_ {q \in \Sigma} \ell_ {q}
$$

where$\ell _ { q } = \# H ^ { 0 } ( \mathbf { Q } _ { q } , Y ^ { * } ) \ ( \mathrm { f o r } \ q \neq p ) , \ell _ { p } = \# H ^ { 0 } ( \mathbf { Q } _ { p } , ( Y ^ { 0 } ) ^ { * } )$

Since$V \simeq Y \oplus ( K / \mathcal { O } ) ( \psi ) \oplus K / \mathcal { O }$we need also a formula for

$$
\# \ker \left\{H ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, (K / \mathcal {O}) (\psi) \oplus K / \mathcal {O}) \rightarrow H ^ {1} (\mathbf {Q} _ {p} ^ {\mathrm{unr}}, (K / \mathcal {O}) (\psi) \oplus K / \mathcal {O}) \right\}.
$$

This is easily computed to be

$$
\# (\mathcal {O} / h _ {L}) \cdot \prod_ {q \in \Sigma - \{p \}} \ell_ {q}\tag{4.16}
$$

where$\ell _ { q } = \# H ^ { 0 } ( \mathbf { Q } _ { q } , ( ( K / \mathcal { O } ) ( \psi ) \oplus K / \mathcal { O } ) ^ { * } )$and$h _ { L }$is the class number of$\mathcal { O } _ { L }$ Combining these gives:

Proposition 4.3.

$$
\# H _ {\mathrm{Se}} ^ {1} (\mathbf {Q} _ {\Sigma} / \mathbf {Q}, V) \leq \# (\mathcal {O} / \Omega^ {- 2} L _ {\mathfrak {f} _ {0}} (2, \overline {{\nu}})) \cdot \# (\mathcal {O} / h _ {L}) \cdot \prod_ {q \in \Sigma} \ell_ {q}
$$

$$
w h e r e \ell_ {q} = \# H ^ {0} (\mathbf {Q} _ {q}, V ^ {*}) (f o r q \neq p), \ell_ {p} = \# H ^ {0} (\mathbf {Q} _ {p}, (Y ^ {0}) ^ {*}).
$$

## 2. Calculation of η

We need to calculate explicitly the invariants$\eta _ { \mathscr { D } , f }$introduced in Chapter 2, $\ S 3$in a special case. Let$\rho _ { 0 }$be an irreducible representation as in (1.1). Suppose that f is a newform of weight 2 and level$N , \lambda$a prime of$\mathcal { O } _ { f }$above p and$\rho _ { f , \lambda }$a deformation of$\rho _ { 0 }$. Let m be the kernel of the homomorphism${ \bf T } _ { 1 } ( N )  \dot { \mathcal { O } } _ { f } / \lambda$ arising from$f .$. We write$T$for$\mathbf { T } _ { 1 } ( N ) _ { \mathfrak { m } } \bigotimes _ { W ( k _ { \mathfrak { m } } ) } \mathcal { O }$, where$\mathcal { O } = \mathcal { O } _ { f , \lambda }$and$k _ { \mathfrak { m } }$is the residue field of m. Assume that$p \nmid N$. We assume here that k is the residue field of O and that it is chosen to contain$k _ { \mathfrak { m } }$. Then by Corollary 1 of Theorem 2.1,$\mathbf { T } _ { 1 } ( N ) _ { \mathfrak { m } }$is Gorenstein andit follows that$T$is also a Gorenstein O-algebra (see the discussion following (2.42)). So we can use perfect pairings (the second one T-bilinear)

$$
\mathcal {O} \times \mathcal {O} \to \mathcal {O}, \quad \langle , \rangle : T \times T \to \mathcal {O}
$$

to define an invariant η of$T . \quad \mathrm { I f } \ \pi : \ T  \ { \mathcal { O } }$is the natural map, we set $( \eta ) = ( \hat { \pi } ( 1 ) )$where ˆπ is the adjoint of π with respect to the pairings. It is well-defined as an ideal of$T .$, depending only on$\pi$. Furthermore, as we noted in Chapter 2,$\ S 3 , \pi ( \eta ) = \langle \eta , \eta \rangle$up to a unit in O and as noted in the appendix $\eta = \mathrm { A n n } { \mathfrak { p } } = T [ { \mathfrak { p } } ]$where${ \mathfrak { p } } = \ker \pi$. We now give an explicit formula for η developed by Hida (cf. [Hi2] for a survey of his earlier results) by interpreting $\langle ~ , ~ \rangle$in terms of the cup product pairing on the cohomology of$X _ { 1 } ( N )$, and then in terms of the Petersson inner product of$f$with itself. The following account (which does not require the CM hypothesis) is adapted from [Hi2] and we refer there for more details.

Let

$$
(,): H ^ {1} (X _ {1} (N), \mathcal {O} _ {f}) \times H ^ {1} (X _ {1} (N), \mathcal {O} _ {f}) \to \mathcal {O} _ {f}\tag{4.17}
$$

be the cup product pairing with$\mathcal { O } _ { f }$as coeficients. (We sometimes drop the C from$X _ { 1 } ( N ) _ { / \mathbf { C } }$or$J _ { 1 } ( N ) _ { / \mathbf { C } }$if the context makes it clear that we are referring to the complex manifolds.) In particular$( t _ { * } x , y ) \ = \ ( x , t ^ { * } y )$for all $x , y$and for each standard Hecke correspondence t. We use the action of t on $H ^ { 1 } ( X _ { 1 } ( N ) , { \mathcal { O } } _ { f } )$given by$x \mapsto t ^ { * } x$and simply write tx for$t ^ { * } x$. This is the same as the action induced by$t _ { * } \in \mathbf { T } _ { 1 } ( N )$on$H ^ { 1 } ( J _ { 1 } ( N ) , { \mathcal { O } } _ { f } ) \simeq H ^ { 1 } ( X _ { 1 } ( N ) , { \mathcal { O } } _ { f } )$ Let${ \mathfrak { p } } _ { f }$be the minimal prime of${ \bf T } _ { 1 } ( N ) \otimes { \mathcal O } _ { f }$associated to$f \ ( \mathrm { i . e . } ,$, the kernel of ${ \bf T } _ { 1 } ( \dot { N } ) \otimes \mathcal { O } _ { f }  \mathcal { O } _ { f }$given by$t _ { l } \otimes \beta \mapsto \beta c _ { t } ( f )$where$t f = c _ { t } ( f ) f )$, and let

$$
L _ {f} = H ^ {1} (X _ {1} (N), \mathcal {O} _ {f}) [ \mathfrak {p} _ {f} ].
$$

If$f = \Sigma a _ { n } q ^ { n }$let$f ^ { \rho } = \Sigma \bar { a } _ { n } q ^ { n }$. Then$f ^ { \rho }$is again a newform and we define $L _ { f ^ { \rho } }$by replacing f by$f ^ { \rho }$in the definition of$L _ { f }$. (Note here that$\mathcal { O } _ { f } = \mathcal { O } _ { f \rho }$ as these rings are the integers of fields which are either totally real or CM by a result of Shimura. Actually this is not essential as we could replace$\mathcal { O } _ { f }$by any ring of integers containing it.) Then the pairing$( ~ , ~ )$induces another by restriction

$$
(,): L _ {f} \times L _ {f ^ {\rho}} \to \mathcal {O} _ {f}.\tag{4.18}
$$

Replacing$\mathcal { O }$(and the O<sub>f</sub>-modules) by the localization of$\mathcal { O } _ { f }$at$p$(if necessary) we can assume that$L _ { f }$and$L _ { f ^ { \rho } }$are free of rank 2 and direct summands as $\mathcal { O } _ { f } .$-modules of the respective cohomology groups. Let$\delta _ { 1 } , \delta _ { 2 }$be a basis of$L _ { f }$ Then also$\bar { \delta } _ { 1 } , \bar { \delta } _ { 2 }$is a basis of$L _ { f ^ { \rho } } = \overline { { L _ { f } } }$. Here complex conjugation acts on $H ^ { 1 } ( X _ { 1 } ( N ) , { \mathcal { O } } _ { f } )$via its action on$\mathcal { O } _ { f }$. We can then verify that

$$
(\boldsymbol {\delta}, \bar {\boldsymbol {\delta}}) := \det (\delta_ {i}, \bar {\delta} _ {j})
$$

is an element of$\mathcal { O } _ { f }$(or its localization at$p )$whose image in$\mathcal { O } _ { f , \lambda }$is given by $\pi ( \eta ^ { 2 } )$(unit). To see this, consider a modified pairing$\langle ~ , ~ \rangle$defined by

$$
\langle x, y \rangle = (x, w _ {\zeta} y)\tag{4.19}
$$

where$w _ { \zeta }$is defined as in (2.4). Then$\langle t x , y \rangle = \langle x , t y \rangle$for all$x , y$and Hecke operators t. Furthermore

$$
\det \langle \delta_ {i}, \delta_ {j} \rangle = \det (\delta_ {i}, w _ {\zeta} \delta_ {j}) = c \det (\delta_ {i} \overline {{\delta}} _ {j})
$$

for some p-adic unit$c \ : ( \mathrm { i n } \ : \mathcal { O } _ { f } )$. This is because$w _ { \zeta } ( L _ { f ^ { \rho } } ) = L _ { f }$and$w _ { \zeta } ( L _ { f } ) =$ $L _ { f ^ { \rho } }$. (One can check this, foe example, using the explicit bases described below.) Moreover, by Theorem 2.1,

$$
\begin{array}{c} H ^ {1} (X _ {1} (N), \mathbf {Z}) \otimes_ {\mathbf {T} _ {1} (N)} \mathbf {T} _ {1} (N) _ {\mathfrak {m}} \simeq \mathbf {T} _ {1} (N) _ {\mathfrak {m}} ^ {2}, \\ H ^ {1} (X _ {1} (N), \mathcal {O} _ {f}) \otimes_ {\mathbf {T} _ {1} (N) \otimes \mathcal {O} _ {f}} T \simeq T ^ {2}. \end{array}
$$

Thus (4.18) can be viewed (after tensoring with$\mathcal { O } _ { f , \lambda }$and modifying it as in (4.19)) as a perfect pairing of T-modules and so this serves to compute$\pi ( \eta ^ { 2 } )$ as explained earlier (the square coming from the fact that we have a rank 2 module).

To give a more useful expression for$( \delta , { \bar { \delta } } )$we observe that f and$\overline { { f ^ { \rho } } }$can be viewed as elements of$H ^ { 1 } ( X _ { 1 } ( N ) , \mathbf { C } ) \simeq H _ { \mathrm { D R } } ^ { 1 } ( X _ { 1 } ( N ) , \mathbf { C } )$via$f \mapsto f ( z ) d z , { \overline { { f ^ { \rho } } } } \mapsto$ ${ \overline { { f ^ { \rho } } } } d { \overline { { z } } }$. Then$\{ f , { \overline { { f ^ { \rho } } } } \}$form a basis for$L _ { f } \otimes _ { \mathcal { O } _ { f } } \mathbf { C }$. Similarly$\{ \bar { f } , f ^ { \rho } \}$form a basis for$L _ { f ^ { \rho } } \otimes _ { \mathcal { O } _ { f } } \mathbf { C }$. Define the vectors$\omega _ { 1 } ~ = ~ ( f , \overline { { { f ^ { \rho } } } } ) , \omega _ { 2 } ~ = ~ ( \bar { f } , f ^ { \rho } )$and write $\omega _ { 1 } = C \delta$and$\omega _ { 2 } = \bar { C } \bar { \delta }$with$C \in M _ { 2 } ( \mathbf { C } )$. Then writing$f _ { 1 } = f , f _ { 2 } = \overline { { f ^ { \rho } } }$we set

$$
(\boldsymbol {\omega}, \bar {\boldsymbol {\omega}}) := \det ((f _ {i}, \overline {{f _ {j}}})) = (\boldsymbol {\delta}, \bar {\boldsymbol {\delta}}) \det (C \bar {C}).
$$

Now$( \omega , \bar { \omega } )$is given explicitly in terms of the (non-normalized) Petersson inner product # , \$:

$$
(\omega , \bar {\omega}) = - 4 \langle f, f \rangle^ {2}
$$

where$\begin{array} { r } { \langle f , f \rangle = \int _ { \mathfrak { H } / \Gamma _ { 1 } ( N ) } f \bar { f } } \end{array}$dx dy.

To compute det(C) we consider integrals over classes in$H _ { 1 } ( X _ { 1 } ( N ) , { \mathcal { O } } _ { f } )$ By Poincar’e duality there exist classes$c _ { 1 } , c _ { 2 }$in$H _ { 1 } ( X _ { 1 } ( N ) , { \mathcal { O } } _ { f } )$such that det$\big ( \int _ { c _ { j } } \delta _ { i } \big )$is a unit in$\mathcal { O } _ { f }$. Hence det$C$generates the same$\mathcal { O } _ { f }$-module as is generated by$\textstyle \left\{ \operatorname* { d e t } \left( \int _ { c _ { j } } f _ { i } \right) \right\}$for all such choices of classes$( c _ { 1 } , c _ { 2 } )$and with $\{ f _ { 1 } , f _ { 2 } \} = \{ f , { \overline { { f ^ { \rho } } } } \}$. Letting$u _ { f }$be a generator of the${ \mathcal { O } } _ { f }$-module$\textstyle \left\{ \operatorname* { d e t } \left( \int _ { c _ { j } } f _ { i } \right) \right\}$ we have the following formula of Hida:

Proposition 4.4.$\pi ( \eta ^ { 2 } ) = \langle f , f \rangle ^ { 2 } / u _ { f } \bar { u } _ { f } \times ( \ u n i t \ i n \ O _ { f , \lambda } )$

Now we restrict to the case where$\rho _ { 0 } ~ = ~ \mathrm { I n d } _ { L } ^ { \mathbf { Q } } \kappa _ { 0 }$for some imaginary quadratic field L which is unramified at$p$and some$k ^ { \times }$-valued character κ of$\operatorname { G a l } ( { \bar { L } } / L )$. We assume that$\rho _ { 0 }$is irreducible,$\mathrm { i . e . , }$that$\kappa _ { 0 } ~ \neq ~ \kappa _ { 0 , \sigma }$where $\begin{array} { r l r } { \kappa _ { 0 , \sigma } ( \delta ) } & { { } = } & { \kappa _ { 0 } ( \sigma ^ { - 1 } \delta \sigma ) } \end{array}$for any$\sigma$representing the nontrivial coset of $\operatorname { G a l } ( { \bar { L } } / \mathbf { Q } ) / \operatorname { G a l } ( { \bar { L } } / L )$. In addition we wish to assume that$\rho _ { 0 }$is ordinary and det$\rho _ { 0 } | _ { I _ { p } } = \omega$. In particular$p$splits in$L$. These conditions imply that, if p is a prime of L above$p \kappa _ { 0 } ( \alpha ) \equiv \alpha ^ { - 1 }$mod p on$U _ { \mathfrak { p } }$after possible replacement of$\kappa _ { 0 }$ by$\kappa _ { 0 , \sigma }$. Here the$U _ { \mathfrak { p } }$are the units of$L _ { \mathfrak { p } }$and since$\kappa _ { 0 }$is a character, the restriction of$\kappa _ { 0 }$to an inertia group$I _ { \mathfrak { p } }$induces a homomorphism on$U _ { \mathfrak { p } }$. We assume now that p is fixed and$\kappa _ { 0 }$chosen to satisfy this congruence. Our choice of $\kappa _ { 0 }$will imply that the grossencharacter introduced below has conductor prime to$p .$.

We choose a (primitive) grossencharacter$\varphi$on$L$together with an embedding$\overline { { \mathbf { Q } } } \hookrightarrow \overline { { \mathbf { Q } } } _ { p }$corresponding to the prime p above$p$such that the induced p-adic character$\varphi _ { p }$has the properties:

(i)$\varphi _ { p }$mod p = κ<sub>0</sub> (p = maximal ideal of$\overline { { \mathbf { Q } } } _ { p } )$.

(ii)$\varphi _ { p }$factors through an abelian extension isomorphic to$\mathbf { Z } _ { p } \oplus T$with$T$of finite order prime to$p$.

(iii)$\varphi ( ( \alpha ) ) = \alpha$for$\alpha \equiv 1 ( \mathfrak { f } )$for some integral ideal f prime to$p .$

To obtain$\varphi \ { \mathrm { i t } }$is necessary first to define$\varphi _ { p }$. Let$M _ { \infty }$denote the maximal abelian extension of$L$which is unramified outside p. Let$\theta : \mathrm { G a l } ( M _ { \infty } / L ) \to$ $\overline { { \mathbf { Q } _ { p } } } ^ { \times }$be any character which factors through a$\mathbf { Z } _ { p } \mathrm { - e x t e n s i o n }$and induces the homomorphism$\alpha \mapsto \alpha ^ { - 1 }$on$U _ { \mathfrak { p } , 1 } \mapsto \mathrm { G a l } ( M _ { \infty } / L )$where$U _ { \mathfrak { p } , 1 } = \{ u \in U _ { \mathfrak { p } } : u \equiv$ $1 ( { \mathfrak { p } } ) \}$. Then set$\varphi _ { p } = \kappa _ { 0 } \theta$, and pick a grossencharacter$\varphi$such that$( \varphi ) _ { p } = \varphi _ { p } .$ Note that our choice of$\varphi$here is not necessarily intended to be the same as the choice of grossencharacter in Section 1.

Now let$\mathfrak { f } _ { \varphi }$be the conductor of$\varphi$and let$F$be the ray class field of conductor$\boldsymbol { \mathfrak { f } } _ { \varphi } \boldsymbol { \bar { \mathfrak { f } } } _ { \varphi }$. Then over$F$there is an elliptic curve, unique up to isomorphism, with complex multiplication by$\mathcal { O } _ { L }$and period lattice free, of rank one over$\mathcal { O } _ { L }$ and with associated grossencharacter$\varphi \circ N _ { F / L }$. The curve$E _ { / F }$is the extension of scalars of a unique elliptic curve$E _ { / F ^ { + } }$where$F ^ { + }$is the subfield of$F$of index 2. (See [Sh1,$( 5 . 4 . 3 ) ] . )$Over$F ^ { + }$this elliptic curve has only the p-power isogenies of the form$\pm p ^ { m }$for$m \in \mathbf { Z }$. To see this observe that$F$is unramified at$p$and$\rho _ { 0 }$is ordinary so that the only isogenies of degree$p$over$F$are the ones that correspond to division by ker p and ker$\mathfrak { p ^ { \prime } }$where${ \mathfrak { p } } { \mathfrak { p } } ^ { \prime } = ( p )$in$L .$. Over $F ^ { + }$these two subgroups are interchanged by complex conjugation, which gives the assertion. We let$E / o _ { F ^ { + } , ( p ) }$denote a Weierstrass model over${ \mathcal O } _ { F ^ { + } , ( p ) }$, the localization of${ \mathcal { O } } _ { F ^ { + } }$at$p ,$, with good reduction at the primes above$p .$. Let ω be a Neron diferential of$E _ { / \mathcal { O } _ { F ^ { + } , ( p ) } }$. Let Ω be a basis for the$\mathcal { O } _ { L }$-module of periods of$\omega _ { E }$. Then$\overline { { \Omega } } = u \cdot \Omega$for some p-adic unit in$F ^ { \times }$

According to a theorem of Hecke,$\varphi$is associated to a cusp form$f _ { \varphi }$in such a way that the L-series$L ( s , \varphi )$and$L ( s , f _ { \varphi } )$are equal (cf. [Sh4, Lemma$3 ] )$. Moreover since$\varphi$was assumed primitive,$f = f _ { \varphi }$is a newform. Thus the integer N = cond$f = | \Delta _ { L / \mathbf { Q } } | \mathrm { N o r m } _ { L / \mathbf { Q } } ( \mathrm { c o n d } \varphi )$is prime to$p$and there is a homomorphism

$$
\psi_ {f}: \mathbf {T} _ {1} (N) \twoheadrightarrow R _ {f} \subset \mathcal {O} _ {f} \subset \mathcal {O} _ {\varphi}
$$

satisfying$\psi _ { f } ( T _ { l } ) = \varphi ( { \mathfrak { c } } ) + \varphi ( { \hat { \mathfrak { c } } } ) { \mathrm { ~ i f ~ } } l = { \mathfrak { c } } { \hat { \mathfrak { c } } }$in$L , ~ ( l ~ \nmid N )$and$\psi _ { f } ( T _ { l } ) = 0$if l is inert in$L ~ ( l ~ \nmid ~ N )$. Also$\psi _ { f } ( l \langle l \rangle ) = \varphi ( ( l ) ) \psi ( l )$where ψ is the quadratic character associated to$L .$Using the embedding of$\bar { \mathbf { Q } }$in$\bar { \mathbf { Q } } _ { p }$chosen above we get a prime λ of$\mathcal { O } _ { f }$above$p ,$a maximal ideal m of${ \bf T } _ { 1 } ( N )$and a homomorphism ${ \bf T } _ { 1 } ( { \cal N } ) _ { \mathfrak { m } } \  \ \stackrel { \cdot } { \mathcal { O } } _ { f , \lambda }$such that the associated representation$\rho _ { f , \lambda }$reduces to $\rho _ { 0 }$mod$\lambda .$

Let$\mathfrak { p } _ { 0 } = \ker \psi _ { f } : \mathbf { T } _ { 1 } ( N ) \to \mathcal { O } _ { f }$and let

$$
A _ {f} = J _ {1} (N) / \mathfrak {p} _ {0} J _ {1} (N)
$$

be the abelian variety associated to f by Shimura. Over$F ^ { + }$there is an isogeny

$$
A _ {f / F ^ {+}} \sim (E _ {/ F ^ {+}}) ^ {d}
$$

where$d = [ O _ { f } : \mathbf { Z } ]$(see [Sh4, Th. 1]). To see this one checks that the p-adic$\mathrm { G a } \mathrm { - }$ lois representation associated to the Tate modules on each side are equivalent to$( \mathrm { I n d } _ { F } ^ { F ^ { + } } \varphi _ { o } ) \otimes \mathbf { z } _ { p } K _ { f , p }$where$K _ { f , p } = \mathcal { O } _ { f } \otimes \mathbf { Q } _ { p }$and where$\varphi _ { p } : { \mathrm { G a l } } ( { \overline { { F } } } / F ) \to \mathbf { Z } _ { p } ^ { \times }$ is the p-adic character associated to$\varphi$and restricted to$F$. (one compares trace(Frob #) in the two representations for$\ell \dag \ N p$and # split completely in $F ^ { + } ;$; cf. the discussion after Theorem 2.1 for the representation on$A _ { f } . )$

Now pick a nonconstant map

$$
\pi : X _ {1} (N) _ {/ F ^ {+}} \to E _ {/ F ^ {+}}
$$

which factors through$A _ { f / F ^ { + } }$. Let M be the composite of$F ^ { + }$and the normal closure of$K _ { f }$viewed in C. Let$\omega _ { E }$be a Neron diferential of$E _ { / \mathcal { O } _ { F ^ { + } , ( p ) } } .$ Extending scalars to M we can write

$$
\pi^ {*} \omega_ {E} = \sum_ {\sigma \in \mathrm{Hom} (K _ {f}, \mathbf {C})} a _ {\sigma} \omega_ {f ^ {\sigma}}, \quad a _ {\sigma} \in M
$$

where$\omega _ { f ^ { \sigma } } = \sum _ { n = 1 } ^ { \infty } a _ { n } ( f ^ { \sigma } ) q ^ { n } { \frac { d q } { q } }$for each$\sigma$. By suitably choosing π we can assume that$a _ { \mathrm { i d } } \neq 0$. Then there exist$\lambda _ { i } \in { \mathcal { O } } _ { M }$and$t _ { i } \in \mathbf { T } _ { 1 } ( N )$such that

$$
\sum \lambda_ {i} t _ {i} \pi^ {*} \omega_ {E} = c _ {1} \omega_ {f} \quad \mathrm{forsome} c _ {1} \in M.
$$

We consider the map

$$
\pi^ {\prime}: H _ {1} (X _ {1} (N) _ {/ \mathbf {C}}, \mathbf {Z}) \otimes \mathcal {O} _ {M, (p)} \to H _ {1} (E _ {/ \mathbf {C}}, \mathbf {Z}) \otimes \mathcal {O} _ {M, (p)}\tag{4.20}
$$

given by$\begin{array} { r } { \pi ^ { \prime } = \sum \lambda _ { i } ( \pi \circ t _ { i } ) } \end{array}$. Even if$\pi ^ { \prime }$is not surjective we claim that the image of$\pi ^ { \prime }$always has the form$H _ { 1 } ( E _ { / \mathbf { C } } , \mathbf { Z } ) \otimes a \mathcal { O } _ { M , ( p ) }$for some$a \in \mathcal { O } _ { M }$. This is because tensored with$\mathbf { Z } _ { p } \mathbf { \Delta } \pi ^ { \prime }$can be viewed as a$\operatorname { G a l } ( { \overline { { \mathbf { Q } } } } / F ^ { + } )$-equivariant map of p-adic Tate-modules, and the omly p-power isogenies on$E _ { / F ^ { + } }$have the form $\pm p ^ { m }$for some$m \in \mathbf { Z }$. It follows that we can factor$\pi ^ { \prime }$as$( 1 \otimes a ) \circ \alpha$for some other surjective α

$$
\alpha : H _ {1} (X _ {1} (N) _ {/ \mathbf {C}}, \mathbf {Z}) \otimes \mathcal {O} _ {M} \to H ^ {1} (E _ {/ \mathbf {C}}, \mathbf {Z}) \otimes \mathcal {O} _ {M},
$$

now allowing a to be in${ \mathcal { O } } _ { M , ( p ) }$. Now define$\alpha ^ { * }$on$\Omega _ { E / \mathbf { C } } ^ { 1 }$by$\textstyle \alpha ^ { * } = \sum a ^ { - 1 } \lambda _ { i } t _ { i } \circ \pi ^ { * }$ where$\pi ^ { * } : \Omega _ { E / \mathbf { C } } ^ { 1 } \to \Omega _ { J _ { 1 } ( N ) / \mathbf { C } } ^ { 1 }$is the map induced by$\pi$and$t _ { i }$has the usual action on$\Omega _ { J _ { 1 } ( N ) / \mathbf { C } } ^ { 1 }$. Then$\alpha ^ { * } ( \omega _ { E } ) = c \omega _ { f }$for some$c \in M$and

$$
\int_ {\gamma} \alpha^ {*} (\omega_ {E}) = \int_ {\alpha (\gamma)} \omega_ {E}\tag{4.21}
$$

for any class$\gamma \in H _ { 1 } ( X _ { 1 } ( N ) _ { / \mathbf { C } } , \mathcal { O } _ { M } )$. We note that α (on homology as in (4.20)) also comes from a map of abelian varieties$\alpha : J _ { 1 } ( N ) _ { / F ^ { + } } \otimes _ { \mathbf { Z } } \mathcal { O } _ { M } \to$ $E _ { / F ^ { + } } \otimes _ { \mathbf { Z } } \mathcal { O } _ { M }$although we have not used this to define$\alpha ^ { * }$

We claim now that$c \in \mathcal { O } _ { M , ( p ) }$. We can compute$\alpha ^ { * } ( \omega _ { E } )$by considering $\begin{array} { r } { \alpha ^ { * } ( \omega _ { E } \otimes 1 ) = \sum t _ { i } \pi ^ { * } \otimes a ^ { - 1 } \lambda _ { i } } \end{array}$on$\Omega _ { E / F ^ { + } } ^ { 1 } \otimes \mathcal { O } _ { M }$and then mapping the image in $\Omega _ { J _ { 1 } ( N ) / F ^ { + } } ^ { 1 } \otimes \mathcal { O } _ { M }$to$\Omega _ { J _ { 1 } ( N ) / F ^ { + } } ^ { 1 } \otimes _ { { \cal { O } } _ { F ^ { + } } } { \cal { O } } _ { M } = \Omega _ { J _ { 1 } ( N ) / M } ^ { 1 }$. Now let us write$\mathcal { O } _ { 1 }$for $\mathcal { O } _ { F ^ { + } , ( p ) }$. Then there are isomorphisms

$$
\Omega_ {J _ {1} (N) / \mathcal {O} _ {1} \otimes \mathcal {O} _ {2}} ^ {1} \xrightarrow {\stackrel {{s _ {1}}} {{\sim}}} \mathrm{Hom} (\mathcal {O} _ {M}, \Omega_ {J _ {1} (N) / \mathcal {O} _ {1}} ^ {1}) \xrightarrow {\stackrel {{s _ {2}}} {{\sim}}} \Omega_ {J _ {1} (N) / \mathcal {O} _ {1}} ^ {1} \otimes \delta^ {- 1}
$$

where$\delta$is the diferent of$M / \mathbf { Q }$. The first isomorphism can be described as follows. Let$e ( \gamma ) : J _ { 1 } ( N ) \to J _ { 1 } ( N ) \otimes \mathcal { O } _ { M }$for$\gamma \in { \mathcal { O } } _ { M }$be the map$x \mapsto x \otimes \gamma$ Then$t _ { 1 } ( \omega ) ( \delta ) = e ( \gamma ) ^ { * } \omega$. Similar identifications occur for$E$in place of$J _ { 1 } ( N )$ So to check that$\alpha ^ { * } ( \omega _ { E } \otimes 1 ) \in \Omega _ { J _ { 1 } ( N ) _ { / \mathcal { O } _ { 1 } } } ^ { 1 } \otimes \mathcal { O } _ { M }$it is enough to observe that by its construction α comes from a homomorphism$J _ { 1 } ( N ) _ { / \mathcal { O } _ { 1 } } \otimes \mathcal { O } _ { M } \to E _ { / \mathcal { O } _ { 1 } } \otimes \mathcal { O } _ { M }$ It follows that we can compare the periods of f and of$\omega _ { E }$

For$f ^ { \rho }$we use the fact that$\textstyle { \overline { { \int _ { \gamma } f ^ { \rho } d z } } } = \int _ { \gamma ^ { c } } f$dz where c is the${ \mathcal { O } } _ { M }$-linear map on homology coming from complex conjugation on the curve. We deduce:

Proposition 4.5.$\begin{array} { r } { u _ { f } = \frac { 1 } { 4 \pi ^ { 2 } } \Omega ^ { 2 } . ( 1 / p - a d i c \ i n t e g e r ) ) } \end{array}$

We now give an expression for$\langle f _ { \varphi } , f _ { \varphi } \rangle$in terms of the L-function of$\varphi$. This was first observed by Shimura$[ \mathrm { S h 2 } ]$although the precise form we want was given by Hida.

Proposition 4.6.

$$
\langle f_{\varphi},f_{\varphi}\rangle = \frac{1}{16\pi^{3}} N^{2}\Bigg\{\prod_{\substack{q|N\\ q\not\in S_{\varphi}}}\left(1 - \frac{1}{q}\right)\Bigg\} L_{N}(2,\varphi^{2}\bar{\chi})L_{N}(1,\psi)
$$

where$\chi$is the character of$f _ { \varphi }$and$\hat { \chi }$its restriction to$L ;$

ψ is the quadratic character associated to$L ;$

$L _ { N } ( \mathrm { ~  ~ { ~ \mathbf ~ { ~ \phi ~ } ~ } ~ } )$denotes that the Euler factors for primes dividing N have been removed;

$S _ { \varphi }$is the set of primes$q | N$such that$q = { \mathfrak { q } } { \mathfrak { q } } ^ { \prime }$with${ \mathfrak { q } } \ { \mathfrak { f } }$cond$\varphi$and${ \mathfrak { q } } , { \mathfrak { q } } ^ { \prime }$ primes of$L ,$not necessarily distinct.

Proof. One begins with a formula of Petterson that for an eigenform of weight 2 on$\Gamma _ { 1 } ( N )$says

$$
\langle f, f \rangle = (4 \pi) ^ {- 2} \Gamma (2) \Bigl (\frac {1}{3} \Bigr) \pi [ \mathrm{SL} _ {2} (\mathbf {Z}): \Gamma_ {1} (N) \cdot (\pm 1) ] \cdot \mathrm{Res} _ {s = 2} D (s, f, f ^ {\rho})
$$

where$D ( s , f , f ^ { \rho } ) = \sum _ { n = 1 } ^ { \infty } | a _ { n } | ^ { 2 } n ^ { - s } \operatorname { i f } f = \sum _ { n = 1 } ^ { \infty } a _ { n } q ^ { n }$(cf. [Hi3, (5.13)]). One checks that, removing the Euler factors at primes dividing N,

$$
D _ {N} (s, f, f ^ {\rho}) = L _ {N} (s, \varphi^ {2} \bar {\chi}) L _ {N} (s - 1, \psi) \zeta_ {\mathbf {Q}, N} (s - 1) / \zeta_ {\mathbf {Q}, N} (2 s - 2)
$$

by using Lemma 1 of [Sh3]. For each Euler factor of$f$at a$q | N$of the form $\left( 1 - \alpha _ { q } q ^ { - s } \right)$we get also an Euler factor in$D ( s , f , f ^ { \rho } )$of the form$\left( 1 - \alpha _ { q } \bar { \alpha } _ { q } q ^ { - s } \right)$ When$f = f _ { \varphi }$this can only happen for a split prime q where${ \mathfrak { q } } ^ { \prime }$divides the conductor of$\varphi$but q does not, or for a ramified prime q which does not divide the conductor of$\varphi .$. In this case we get a term$\left( 1 - q ^ { 1 - s } \right)$since$| \varphi ( { \mathfrak { q } } ) | ^ { 2 } = q$

Putting together the propositions of this section we now have a formula for $\pi ( \eta )$as defined at the beginning of this section. Actually it is more convenient to give a formula for$\pi ( \eta _ { M } )$, an invariant defined in the same way but with $\mathbf { T } _ { 1 } ( M ) _ { \mathfrak { m } _ { 1 } } \otimes _ { W ( k _ { \mathfrak { m } _ { 1 } } ) } \mathcal { O }$replacing$\mathbf { T } _ { 1 } ( N ) _ { \mathfrak { m } } \otimes _ { W ( k _ { \mathfrak { m } } ) } \mathcal { O }$where$M = p M _ { 0 }$with$p \nmid M _ { 0 }$ and$M / N$is of the form

$$
\prod_{q\in S_{\varphi}}q\cdot \prod_{\substack{q\nmid N\\ q\mid M_{0}}}q^{2}.
$$

Here${ \mathfrak { m } } _ { 1 }$is defined by the requirements that$\rho _ { \mathfrak { m } _ { 1 } } = \rho _ { 0 } , U _ { q } \in \mathfrak { m }$if$q | M ( q \neq p )$ and there is an embedding (which we fix)$k _ { \mathfrak { m } _ { 1 } } \hookrightarrow k$over$k _ { 0 }$taking$U _ { p } \to \alpha _ { p }$ where$\alpha _ { p }$is the unit eigenvalue of Frob p in$\rho _ { f , \lambda }$. So if$f ^ { \prime }$is the eigenform obtained from$f$by ‘removing the Euler factors’ at$q | ( M / N ) ( q \ \ne \ p )$and removing the non-unit Euler factor at$p$we have$\eta _ { M } = \hat { \pi } ( 1 )$where$\pi : T _ { 1 } =$ $\mathbf { T } _ { 1 } ( M ) _ { \mathfrak { m } _ { 1 } } \bigotimes _ { W ( k _ { \mathfrak { m } _ { 1 } ) } } \mathcal { O } \to \mathcal { O }$corresponds to$f ^ { \prime }$and the adjoint is taken with respect to perfect pairings of$T _ { 1 }$and$\mathcal { O }$with themselves as O-modules, the first one assumed T -bilinear.

Property (ii) of$\varphi _ { p }$ensures that M is as in (2.24) with$\mathcal { D } = ( \mathrm { S e } , \Sigma , \mathcal { O } , \phi )$ where Σ is the set of primes dividing M. (Note that$S _ { \varphi }$is precisely the set of primes$q$for which$n _ { q } = 1$in the notation of Chapter 2, §3.) As in Chapter 2, §3 there is a canonical map

$$
R _ {\mathcal {D}} \to \mathbf {T} _ {\mathcal {D}} \simeq \mathbf {T} _ {1} (M) _ {\mathfrak {m} _ {1}} \underset {W (k _ {\mathfrak {m} _ {1}})} {\otimes} \mathcal {O}
$$

which is surjective by the arguments in the proof of Proposition 2.15. Here we are considering a slightly more general situation than that in Chapter$2 ,$ $\ S 3$as we are allowing$\rho _ { 0 }$to be induced from a character of$\mathbf { Q } ( { \sqrt { - 3 } } )$. In this special case we define$\mathbf { T } _ { \mathcal { D } }$to be$\mathbf { T } _ { 1 } ( M ) _ { \mathfrak { m } _ { 1 } } \bigotimes _ { W ( k _ { \mathfrak { m } _ { 1 } ) } } \mathcal { O }$. The existence of the map in (4.22) is proved as in Chapter 2, §3. For the surjectivity, note that for each $q | M$(with$q \ne p ) \ { U _ { q } }$is zero in$\mathbf { T } _ { \mathcal { D } }$as$U _ { q } \in \mathfrak { m } _ { 1 }$for each such$q$so that we can apply Remark 2.8. To see that$U _ { p }$is in the image of$R _ { \mathcal { D } }$we use that it is the eigenvalue of Frob p on the unique unramified quotient which is free of rank one in the representation$\rho$described after the corollaries to Theorem 2.1 (cf. Theorem 2.1.4 of [Wi1]). To verify this one checks that$\mathbf { T } _ { \mathcal { D } }$is reduced or alternatively one can apply the method of Remark 2.11. We deduce that $U _ { p } \in \mathbf { T } _ { \mathcal { D } } ^ { \mathrm { t } r }$, the$W ( k _ { \mathfrak { m } _ { 1 } } )$-subalgebra of$\mathbf { T } _ { 1 } ( M ) _ { \mathfrak { m } _ { 1 } }$generated by the traces, and it follows then that it is in the image of$R _ { \mathcal { D } }$. We also need to give a definition of $\mathbf { T } _ { \mathcal { D } }$where$\mathcal { D } = ( \mathrm { o r d } , \Sigma , \mathcal { O } , \phi )$and$\rho _ { 0 }$is induced from a character of$\mathbf { Q } ( { \sqrt { - 3 } } )$. For this we use (2.31).

Now we take

$$
M = N p \prod_ {q \in S _ {\varphi}} q.
$$

The arguments in the proof of Theorem 2.17 show that

$$
\pi (\eta_ {M}) \mathrm{isdivisibleby} \pi (\eta) (\alpha_ {p} ^ {2} - \langle p \rangle) \cdot \prod_ {q \in S _ {\varphi}} (q - 1)
$$

where$\alpha _ { p }$is the unit eigenvalue of Frob$p$in$\rho _ { f , \lambda }$. The factor at$p$is given by remark 2.18 and at$q$it comes from the argument of Proposition 2.12 but with $H = H ^ { \prime } = 1$. Combining this with Propositions 4.4, 4.5, and 4.6, we have that

$$
\pi (\eta_ {M})
$$

$$
\Omega^ {- 2} L _ {N} \left(2, \varphi^ {2} \bar {\hat {\chi}}\right) \frac {L _ {N} (1 , \phi)}{\pi} \left(\alpha_ {p} ^ {2} - \langle p \rangle\right) \prod_ {q | N} (q - 1).
$$

We deduce:

Theorem 4.7.$\# ( \mathcal { O } / \pi ( \eta _ { M } ) ) = \# H _ { \mathrm { S e } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V ) .$

Proof. As explained in Chapter 2, §3 it is suficient to prove the inequality $\# ( { \mathcal { O } } / \pi ( \eta _ { M } ) ) \geq \# H _ { \mathrm { S e } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V )$as the opposite one is immediate. For this it sufices to compare (4.23) with Proposition 4.3. Since

$$
L _ {N} (2, \bar {\nu}) = L _ {N} (2, \nu) = L _ {N} (2, \varphi^ {2} \bar {\chi})
$$

(note that the right-hand term is real by Proposition 4.6) it sufices to air up the Euler factors at$q$for$q | N$in (4.23) and in the expression for the upper bound of #$H _ { \mathrm { S e } } ^ { 1 } ( \mathbf { Q } _ { \Sigma } / \mathbf { Q } , V )$

We now deduce the main theorem in the CM case using the method of Theorem 2.17.

Theorem 4.8. Suppose that$\rho _ { 0 }$as in (1.1) is an irreducible representation of odd determinant such that$\rho _ { 0 } = \mathrm { I n d } _ { L } ^ { \mathbf { Q } } \kappa _ { 0 }$for a character$\kappa _ { 0 }$of an imaginary quadratic extension L of Q which is unramified at$p .$Assume also that:

(i) det$\rho _ { 0 } \Big \vert _ { I _ { p } } = \omega ;$

(ii)$\rho _ { 0 }$is ordinary.

Then for every$\mathcal { D } = ( \cdot , \Sigma , \mathcal { O } , \phi )$uch that$\rho _ { 0 }$os of type D with$\cdot = \mathrm { S e }$or ord,

$$
R _ {\mathcal {D}} \simeq \mathbf {T} _ {\mathcal {D}}
$$

and$\mathbf { T } _ { \mathcal { D } }$is a complete intersection.

Corollary. For any ρ<sub>0</sub> as in the theorem suppose that

$$
\rho : \operatorname{Gal} (\bar {\mathbf {Q}} / \mathbf {Q}) \to \operatorname{GL} _ {2} (\mathcal {O})
$$

is a continuous representation with values in the ring of integers of a local field, unramified outside a finite set of primes, satisfying$\bar { \rho } \simeq \rho _ { 0 }$when viewed as representations to${ \mathrm { G L } } _ { 2 } ( { \bar { \mathbf { F } } } _ { p } )$. Suppose further that:

(i)$\rho \bigg \vert _ { D _ { p } }$is ordinary;

(ii) det$\rho \Big | _ { I _ { p } } = \chi \varepsilon ^ { k - 1 }$with$\chi$of finite order,$k \geq 2$

Then$\rho$is associated to a modular form of weight k.

## Chapter 5

In this chapter we prove the main results about elliptic curves and especially show how to remove the hypothesis that the representation associated to the 3-division points should be irreducible.

## Application to elliptic curves

The key result used is the following theorem of Langlands and Tunnell, extending earlier results of Hecke in the case where the projective image is dihedral.

Theorem 5.1 (Langlands-Tunnell). Suppose that$\rho : \mathrm { { \bf ~ G a l } } ( { \bar { \bf Q } } / { \bf Q } ) \ \to$ $\mathrm { G L _ { 2 } } ( \mathbf { C } )$is a continuous irreducible representation whose image is finite and solvable. Suppose further that det$\rho$is odd. Then there exists a weight one newform f such that$L ( s , f ) = L ( s , \rho )$up to finitely many Euler factors.

Langlands actually proved in [La] a much more general result without restriction on the determinant or the number field (which in our case is$\mathbf { Q } )$ However in the crucial case where the image in$\mathrm { P G L _ { 2 } ( C ) }$is$S _ { 4 }$, the result was only obtained with an additional hypothesis. This was subsequently removed by Tunnell in [Tu].

Suppose then that

$$
\rho_ {0}: \mathrm{Gal} (\bar {\mathbf {Q}} / \mathbf {Q}) \to \mathrm{GL} _ {2} (\mathbf {F} _ {3})
$$

is an irreducible representation of odd determinant. We now show, using the theorem, that this representation is modular in the sense that over${ \bar { \mathbf { F } } } _ { 3 }$ $\rho _ { 0 } \approx \rho _ { g , \mu }$mod$\mu$for some pair$( g , \mu )$with g some newform of weight 2 (cf. [Se, §5.3]). There exists a representation

$$
i: \mathrm{GL} _ {2} (\mathbf {F} _ {3}) \hookrightarrow \mathrm{GL} _ {2} \left(\mathbf {Z} [ \sqrt {- 2} ]\right) \subset \mathrm{GL} _ {2} (\mathbf {C}).
$$

By composing i with an automorphism of$\mathrm { G L _ { 2 } ( F _ { 3 } ) }$if necessary we can assume that i induces the identity on reduction mod$\left( 1 + { \sqrt { - 2 } } \right)$. So if we consider $i \circ \rho _ { 0 } : { \mathrm { G a l } } ( { \bar { \mathbf { Q } } } / \mathbf { Q } ) \to { \mathrm { G L } } _ { 2 } ( \mathbf { C } )$we obtain an irreducible representation which is easily seen to be odd and whose image is solvable. Applying the theorem we find a newform$f$of weight one associated to this representation. Its eigenvalues lie in$\mathbf { Z } \left[ { \sqrt { - 2 } } \right]$. Now pick a modular form$E$of weight one such that$E \equiv 1 ( 3 )$ For example, we can take$E = 6 E _ { 1 , x }$where$E _ { 1 , \chi }$is the Eisenstein series with Mellin transform given by$\zeta ( s ) \zeta ( s , \chi )$for$\chi$the quadratic character associated to$\mathbf { Q } ( { \sqrt { - 3 } } )$. Then$f E \equiv f$mod 3 and using the Deligne-Serre lemma ([DS, Lemma 6.11]) we can find an eigenform$g ^ { \prime }$of weight 2 with the same eigenvalues as$f$modulo a prime$\mu ^ { \prime }$above$( 1 + { \sqrt { - 2 } } )$. There is a newform$g$of weight 2 which has the same eigenvalues as$g ^ { \prime }$for almost all$T _ { l } \mathrm { \ ' s . }$and we replace$( g ^ { \prime } , \mu ^ { \prime } )$ by$( g , \mu )$for some prime$\mu$above$( 1 + { \sqrt { - 2 } } )$. Then the pair$( g , \mu )$satisfies our requirements for a suitable choice of$\mu$(compatible with$\mu ^ { \prime } )$

We can apply this to an elliptic curve E defined over Q by considering $E [ 3 ]$. We now show how in studying elliptic curves our restriction to irreducible representations in the deformation theory can be circumvented.

## Theorem 5.2. All semistable elliptic curves over Q are modular.

Proof. Suppose that E is a semistable elliptic curve over Q. Assume first that the representation$\bar { \rho } _ { E , 3 }$on$E [ 3 ]$is irreducible. Then if$\rho _ { 0 } ~ = ~ \bar { \rho } _ { E , 3 }$ restricted to$\operatorname { G a l } ( { \bar { \mathbf { Q } } } / \mathbf { Q } ( { \sqrt { - 3 } } ) )$were not absolutely irreducible, the image of the restriction would be abelian of order prime to 3. As the semistable hypothesis implies that all the inertia groups outside 3 in the splitting field of$\rho _ { 0 }$have order dividing 3 this means that the splitting field of$\rho _ { 0 }$is unramified outside 3. However,$\mathbf { Q } ( { \sqrt { - 3 } } )$has no nontrivial abelian extensions unramified outside 3 and of order prime to 3. So$\rho _ { 0 }$itself would factor through an abelian extension of$\mathbf { Q }$and this is a contradiction as$\rho _ { 0 }$is assumed odd and irreducible. So $\rho _ { 0 }$restricted to$\mathrm { G a l } ( { \bar { \mathbf { Q } } } / { \mathbf { Q } } ( { \sqrt { - 3 } } ) )$is absolutely irreducible and${ \rho } _ { E , 3 }$is then modular by Theorem 0.2 (proved at the end of Chapter 3). By Serre’s isogeny theorem, E is also modular (in the sense of being a factor of the Jacobian of a modular curve).

So assume now that$\bar { \rho } _ { E , 3 }$is reducible. Then we claim that the representation$\bar { \rho } _ { E , 5 }$on the 5-division points is irreducible. This is because$X _ { 0 } ( 1 5 ) ( \mathbf { Q } )$ has only four rational points besides the cusps and these correspond to non-semistable curves which in any case are modular; cf. [BiKu, pp. 79-80]. If we knew that$\bar { \rho } _ { E , 5 }$was modular we could now prove the theorem in the same way we did knowing that$\bar { \rho } _ { E , 3 }$was modular once we observe that$\bar { \rho } _ { E , 5 }$restricted to $\operatorname { G a l } ( { \bar { \mathbf { Q } } } / \mathbf { Q } ( { \sqrt { 5 } } ) )$is absolutely irreducible. This irreducibility follows a similar argument to the one for$\bar { \rho } _ { E , 3 }$since the only nontrivial abelian extension of $\mathbf { Q } ( { \sqrt { 5 } } )$unramified outside$5$and of order prime to 5 is$\mathbf { Q } ( \zeta _ { 5 } )$which is abelian over$\mathbf { Q } .$. Alternatively, it is enough to check that there are no elliptic curves $E$for which$\bar { \rho } _ { E , 5 }$is an induced representation over$\mathbf { Q } ( { \sqrt { 5 } } )$and$E$is semistable at 5. This can be checked in the supersingular case using the description of $\bar { \rho } _ { E , 5 } | _ { D _ { 5 } }$(in particular it is induced from a character of the unramified quadratic extension of$\mathbf { Q } _ { 5 }$whose restriction to inertia is the fundamental character of level 2) and in the ordinary case it is straightforward.

Consider the twisted form$X ( \rho ) _ { / \mathbf { Q } }$of$X ( 5 ) _ { / \mathbf { Q } }$defined as follows. Let $X ( 5 ) _ { / \mathbf { Q } }$be the (geometrically disconnected) curve whose non-cuspidal points classify elliptic curves with full level 5 structure and let the twisted curve be defined by the cohomology class (even homomorphism) in

$$
H ^ {1} (\mathrm{Gal} (L / \mathbf {Q}), \quad \mathrm{Aut}! X (5) _ {/ L})
$$

given by$\bar { \rho } _ { E , 5 } : \mathrm { G a l } ( L / \mathbf { Q } ) \longrightarrow \mathrm { G L } _ { 2 } ( \mathbf { Z } / 5 \mathbf { Z } ) \subseteq \mathrm { A u t } X ( 5 ) _ { / L }$where L denotes the splitting field of$\bar { \rho } _ { E , 5 }$. Then$E$defines a rational point on$X ( \rho ) _ { / \mathbf { Q } }$and hence also of an irreducible component of it which we denote$C .$. This curve$C$is smooth as$X ( \rho ) _ { / \bar { \mathbf { Q } } } = X ( 5 ) _ { / \bar { \mathbf { Q } } }$is smooth. It has genus zero since the same is true of the irreducible components of$X ( 5 ) _ { / \bar { \mathbf { Q } } }$

A rational point on C (necessarily non-cuspidal) corresponds to an elliptic curve$E ^ { \prime }$over Q with an isomorphism$E ^ { \prime } [ 5 ] \simeq E [ 5 ]$as Galois modules (cf. [DR, VI, Prop. 3.2]). We claim that we can choose such a point with the two properties that (i) the Galois representation$\bar { \rho } _ { E ^ { \prime } , 3 }$is irreducible and (ii)$E ^ { \prime }$(or a quadtratic twist)has semistable reduction at 5. The curve$E ^ { \prime }$(or a quadratic twist) will then satisfy all the properties needed to apply Theorem 0.2. (For the primes$q \neq 5$we just use the fact that$E ^ { \prime }$is semistable at$q \Longleftrightarrow \# \bar { \rho } _ { E ^ { \prime } , 5 } ( I _ { q } ) | 5 . )$ So$E ^ { \prime }$will be modular and hence so too will$\bar { \rho } _ { E ^ { \prime } , 5 }$

To pick a rational point on$C$satisfying (i) and (ii) we use the Hilbert irreducibility theorem. For, to ensure condition (i) holds, we only have to eliminate the possibility that the image of$\bar { \rho } _ { E ^ { \prime } , 3 }$is reducible. But this corresponds to$E ^ { \prime }$ being the image of a rational point on an irreducible covering of$C$of degree $4 .$Let$\mathbf Q ( t )$be the function field of C. We have therefore an irreducible polynomial$f ( x , t ) \in \mathbf { Q } ( t ) [ x ]$of degree$> 1$and we need to ensure that for many values$t _ { 0 }$in$\mathbf { Q } , \ f ( x , t _ { 0 } )$has no rational solution. Hilbert’s theorem ensures that there exists$\mathrm { ~ a ~ } t _ { 1 }$such that$f ( x , t _ { 1 } )$is irreducible. Then we pick a prime $p _ { 1 } \neq 5$such that$f ( x , t _ { 1 } )$has no root mod$p _ { 1 }$. (This is easily achieved using the Cebotarev density theorem; cf. [CF, ex. 6.2, p. 362].) So finally we pick any <sup>ˇ</sup> $t _ { 0 } \in \mathbf { Q }$which is$p _ { 1 }$-adically close to$t _ { 1 }$and also 5-adically close to the original value of t giving E. This last condition ensures that$E ^ { \prime }$(corresponding to$t _ { 0 } )$ or a quadratic twist has semistable reduction at 5. To see this, observe that since$j _ { E } \neq 0$, 1728, we can find a family$E ( j ) : y ^ { 2 } = x ^ { 3 } - g _ { 2 } ( j ) x - g _ { 3 } ( j )$with rational functions$g _ { 2 } ( j ) , g _ { 3 } ( j )$which are finite at$j _ { E }$and with the j-invariant of $E ( j _ { 0 } )$equal to$j _ { 0 }$whenever the$g _ { i } ( j _ { 0 } )$are finite. Then E is given by a quadratic twist of$E ( j _ { E } )$and so after a change of functions of the form$g _ { 2 } ( j ) \mapsto u ^ { 2 } g _ { 2 } ( j )$ $g _ { 3 } ( j ) \mapsto u ^ { 3 } g _ { 3 } ( j )$with$u \in \mathbf { Q } ^ { \times }$we can assume that$E ( j _ { E } ) = E$and that the equation$E ( j _ { E } )$is minimal at 5. Then for$j ^ { \prime } \in \mathbf { Q }$close enough 5-adically to$j _ { E }$ the equation$E ( j ^ { \prime } )$is still minimal and semistable at 5, since a criterion for this, for an integral model, is that either$\mathrm { o r d } _ { 5 } ( \triangle ( E ( j ^ { \prime } ) ) ) = 0$or$\mathrm { o r d } _ { 5 } ( c _ { 4 } ( E ( j ^ { \prime } ) ) ) = 0$ So up to a quadratic twist$E ^ { \prime }$is also semistable.

This kind of argument can be applied more generally.

Theorem 5.3. Suppose that$E$is an elliptic curve defined over$\mathbf { Q }$with the following properties:

(i) E has good or multiplicative reduction at 3, 5,

(ii) For$p = 3 , 5$and for any prime$q \equiv - 1$mod$p$either$\bar { \rho } _ { E , p } | _ { D _ { q } }$is reducible over$\bar { \mathbf { F } } _ { p }$or$\bar { \rho } _ { E , p } | I _ { q }$is irreducible over$\bar { \mathbf { F } } _ { p }$

Then E is modular.

Proof. the main point to be checked is that one can carry over condition (ii) to the new curve$E ^ { \prime }$. For this we use that for any odd prime$p \neq q$

$\bar { \rho } _ { E , p } | _ { D _ { q } }$is absolutely irreducible and$\bar { \rho } _ { E , p } | _ { I _ { q } }$is absolutely reducible

$$
\begin{array}{c} \text {and} 3 \nmid \# \bar {\rho} _ {E, p} (I _ {q}) \\ \Updownarrow \end{array}
$$

$E$acquires good reduction over an abelian 2-power extension of $\mathbf { Q } _ { q } ^ { \mathrm { u n r } }$but not over an abelian extension of$\mathbf { Q } _ { q }$

Suppose then that$q \equiv - 1 ( 3 )$and that$E ^ { \prime }$does not satisfy condition (ii) at $q \ ( \mathrm { f o r } \ p = 3 )$. Then we claim that also$3 \nmid \# \bar { \rho } _ { E ^ { \prime } , 3 } ( I _ { q } )$. For otherwise$\bar { \rho } _ { E ^ { \prime } , 3 } ( I _ { q } )$ has its normalizer in$\mathrm { G L _ { 2 } ( F _ { 3 } ) }$contained in a Borel, whence$\bar { \rho } _ { E ^ { \prime } , 3 } ( D _ { q } )$would be reducible which contradicts our hypothesis. So using the above equivalence we deduce, by passing via$\bar { \rho } _ { E ^ { \prime } , 5 } \simeq \bar { \rho } _ { E , 5 }$, that E also does not satisfy hypothesis (ii) at$p = 3$

We also need to ensure that$\bar { \rho } _ { E ^ { \prime } , 3 }$is absolutely irreducible over$\mathbf { Q } ( { \sqrt { - 3 } } )$ This we can do by observing that the property that the image of$\bar { \rho } _ { E ^ { \prime } , 3 }$lies in the Sylow 2-subgroup of$\mathrm { G L _ { 2 } } ( \mathbf { F } _ { 3 } )$implies that$E ^ { \prime }$is the image of a rational point on a certain irreducible covering of$C$of nontrivial degree. We can then argue in the same way we did in the previous theorem to eliminate the possibility that$\bar { \rho } _ { E ^ { \prime } , 3 }$was reducible, this time using two separate coverings to ensure that the image of$\bar { \rho } _ { E ^ { \prime } , 3 }$is neither reducible nor contained in a Sylow 2-subgroup.

Finally one also has to show that if both$\bar { \rho } _ { E , 5 }$is irreducible and$\bar { \rho } _ { E , 3 }$is induced from a character of$\mathbf { Q } ( { \sqrt { - 3 } } \ )$then$E$is modular. (The case where both were reducible has already been considered.) Taylor has pointed out that curves satisfying both these conditions are classified by the non-cuspidal rational points on a modular curve isomorphic to$X _ { 0 } ( 4 5 ) / W _ { 9 }$, and this is an elliptic curve isogenous to$X _ { 0 } ( 1 5 )$with rank zero over$\mathbf { Q } .$. The non-cuspidal rational points correspond to modular elliptic curves of conductor 338.

## Appendix

## Gorenstein rings and local complete intersections

Proposition 1. Suppose that O is a complete discrete valuation ring and that$\varphi : S  T$is a surjective local O-algebra homomorphism between complete local Noetherian O-algebras. Suppose further that${ \mathfrak { p } } _ { T }$is a prime ideal of $T$such that$T / { \mathfrak { p } } _ { T } \xrightarrow { \sim } { \mathcal { O } }$and let${ \mathfrak { p } } _ { S } = \varphi ^ { - 1 } ( { \mathfrak { p } } _ { T } )$. Assume that

(i)$T \simeq \mathcal { O } [ [ x _ { 1 } , \dots , x _ { r } ] ] / ( f _ { 1 } , \dots , f _ { r - u } )$where r is the size of a minimal set of O-generators of${ \mathfrak { p } } _ { T } / { \mathfrak { p } } _ { T } ^ { 2 }$

(ii)$\varphi$induces an isomorphism${ \mathfrak { p } } _ { S } / { \mathfrak { p } } _ { S } ^ { 2 } \xrightarrow { \sim } { \mathfrak { p } } _ { T } / { \mathfrak { p } } _ { T } ^ { 2 }$and that these are finitely generated O-modules whose free part has rank u.

Then$\varphi$is an isomorphism.

Proof. First we consider the case where$u = 0$. We may assume that the generators$x _ { 1 } , \ldots , x _ { r }$lie in${ \mathfrak { p } } _ { T }$by subtracting their residues in$T / { \mathfrak { p } } _ { T } \xrightarrow { \sim } { \mathcal { O } }$. By (ii) we may also write

$$
S \simeq \mathcal {O} [   [ x _ {1}, \dots , x _ {r} ]   ] / (g _ {1}, \dots , g _ {s})
$$

with$s \geq r$(by allowing repetitions if necessary) and p<sub>S</sub> generated by the images of$\{ x _ { 1 } \ldots , x _ { r } \}$. Let$\mathfrak { p } ~ = ~ ( x _ { 1 } , \ldots , x _ { r } )$in$[ [ x _ { 1 } , \ldots , x _ { r } ] ]$. Writing$f _ { i } \equiv$ $\Sigma a _ { i j } x _ { j }$mod${ \mathfrak { p } } ^ { 2 }$with$a _ { i j } \in \mathcal { O }$, we see that the Fitting ideal as an O-module of ${ \mathfrak { p } } _ { T } / { \mathfrak { p } } _ { T } ^ { 2 }$is given by

$$
F _ {\mathcal {O}} (\mathfrak {p} _ {T} / \mathfrak {p} _ {T} ^ {2}) = \det (a _ {i j}) \in \mathcal {O}
$$

and that this is nonzero by the hypothesis that$u \ : = \ : 0$. Similarly, if each $g _ { i } \equiv \Sigma b _ { i j } x _ { j }$mod${ \mathfrak { p } } ^ { 2 }$, then

$$
F _ {\mathcal {O}} \left(\mathfrak {p} _ {S} / \mathfrak {p} _ {S} ^ {2}\right) = \left\{\det \left(b _ {i j}\right): i \in I, \# I = r, I \subseteq \{1, \dots , s \} \right\}.
$$

By (ii) again we see that det$( a _ { i j } ) = \operatorname* { d e t } ( b _ { i j } )$as ideals of O for some choice$I _ { 0 }$ of I. After renumbering we may assume that$I _ { 0 } = \{ 1 , \ldots , r \}$. Then each$g _ { i }$ $( i = 1 , \ldots , r )$can be written$\begin{array} { r } { g _ { i } = \Sigma r _ { i j } f _ { i } } \end{array}$for some$r _ { i j } \in [ [ x _ { 1 } , \ldots , x _ { r } ] ]$and we have

$$
\det (b _ {i j}) \equiv \det (r _ {i j}) \cdot \det (a _ {i j}) \mod \mathfrak {p}.
$$

Hence det$( r _ { i j } )$is a unit, whence$( r _ { i j } )$is an invertible matrix. Thus the$f _ { i } { } ^ { \mathrm { ' } } \mathrm { s }$can be expressed in terms of the$g _ { i } \mathrm { ^ { * } s }$and so$S \simeq T$

We can extend this to the case$u \ne 0$by picking$x _ { 1 } , \ldots , x _ { r - u }$so that they generate$\left( \mathfrak { p } _ { T } / \mathfrak { p } _ { T } ^ { 2 } \right) ^ { \mathrm { t o r s } }$. Then we can write each$\begin{array} { r } { f _ { i } \equiv \sum _ { i = 1 } ^ { r - u } a _ { i j } x _ { j } } \end{array}$mod${ \mathfrak { p } } ^ { 2 }$and likewise for the$g _ { i } \mathrm { ^ { * } s }$. The argument is now just as before but applied to the Fitting ideals of$\left( \mathfrak { p } _ { T } / \mathfrak { p } _ { T } ^ { 2 } \right) ^ { \mathrm { t o r s } }$

For the next proposition we continue to assume that$\mathcal { O }$is a complete discrete valuation ring. Let$T$be a local O-algebra which as a module is finite and free over O. In addition, we assume the existence of an isomorphism of T-modules$T \xrightarrow { \sim } \mathrm { H o m } _ { \mathcal { O } } ( T , \mathcal { O } )$. We call a local O-algebra which is finite and free and satisfies this extra condition a Gorenstein O-algebra (cf. §5 of [Ti1]). Now suppose that p is a prime ideal of T such that$T / { \mathfrak { p } } \simeq { \mathcal { O } }$

Let$\beta : T  T / { \mathfrak { p } } \simeq \mathcal { O }$be the natural map and define a principal ideal of T by

$$
(\eta_ {T}) = (\hat {\beta} (1))
$$

where${ \hat { \beta } } : { \mathcal { O } }  T$is the adjoint of$\beta$with respect to perfect O-pairings on O and$T _ { \mathrm { : } }$, and where the pairing of T with itself is T-bilinear. (By a perfect pairing on a free O-module M of finite rank we mean a pairing$M \times M \to \mathcal { O }$ such that both the induced maps$M {  } \mathrm { H o m } _ { \mathscr { O } } ( M , { \mathscr { O } } )$are isomorphisms. When $M = T$we are thus requiring that this be an isomorphism of T-modules also.) The ideal$( \eta _ { T } )$is independent of the pairing. Also$T / \eta _ { T }$is torsion-free as an O-module, as can be seen by applying Hom( , O) to the sequence

$$
0 \to \mathfrak {p} \to T \to \mathcal {O} \to 0,
$$

to obtain a homomorphism$T / \eta _ { T } \hookrightarrow \mathrm { H o m } ( \mathfrak { p } , \mathcal { O } )$. This also shows that$( \eta _ { T } ) =$ Annp.

If we let l(M) denote the length of an O-module M, then

$$
l (\mathfrak {p} / \mathfrak {p} ^ {2}) \geq l (\mathcal {O} / \overline {{\eta_ {T}}})
$$

(where we write$\overline { { \eta _ { T } } }$for$\beta ( \eta _ { T } ) )$because p is a faithful$T / \eta _ { T } \mathrm { - m o d u l e }$. (For a brief account of the relevant properties of Fitting ideals see the appendix to [MW1].) Indeed, writing$F _ { R } ( M )$for the Fitting ideal of M as an R-module, we have

$$
F _ {T / \eta_ {T}} (\mathfrak {p}) = 0 \Rightarrow F _ {T} (\mathfrak {p}) \subset (\eta_ {T}) \Rightarrow F _ {T / \mathfrak {p}} (\mathfrak {p} / \mathfrak {p} ^ {2}) \subset (\overline {{\eta_ {T}}})
$$

and we then use the fact that the length of an O-module M is equal to the length of$\mathcal { O } / F _ { \mathcal { O } } ( M )$as$\mathcal { O }$is a discrete valuation ring. In particular when${ \mathfrak { p } } / { \mathfrak { p } } ^ { 2 }$ is a torsion O-module then$\overline { { \eta } } _ { T } \neq 0$

We need a criterion for a Gorenstein O-algebra to be a complete intersection. We will say that a local O-algebra S which is finite and free over O is a complete intersection over O if there is an O-algebra isomorphism $S \simeq { \mathcal { O } } [ [ x _ { 1 } , \dots , x _ { r } ] ] / ( f _ { 1 } , \dots , f _ { r } )$for some r. Such a ring is necessarily a Gorenstein O-algebra and$\{ f _ { 1 } , \ldots , f _ { r } \}$is necessarily a regular sequence. That$( \mathrm { i } ) \Rightarrow$ (ii) in the following proposition is due to Tate (see A.3, conclusion 4, in the appendix in [M Ro].)

Proposition 2. Assume that O is a complete discrete valuation ring and that$T$is a local Gorenstein O-algebra which is finite and free over O and that p is a prime ideal of T such that$T / { \mathfrak { p } } _ { T } \cong \mathcal { O }$and${ \mathfrak { p } } _ { T } / { \mathfrak { p } } _ { T } ^ { 2 }$is a torsion O-module. Then the following two conditions are equivalent:

(i)$T$is a complete intersection over O.

(ii)$l ( { \mathfrak { p } } _ { T } / { \mathfrak { p } } _ { T } ^ { 2 } ) = l ( { \mathcal { O } } / { \overline { { \eta _ { T } } } } )$as O-modules.

Proof. To prove that$\mathrm { ( i i ) } \Rightarrow \mathrm { ( i ) }$, pick a complete intersection$S$over$\mathcal { O }$(so assumed finite and flat over O) such that$\alpha { : } S {  } T$and such that${ \mathfrak { p } } _ { S } / { \mathfrak { p } } _ { S } ^ { 2 } \simeq { \mathfrak { p } } _ { T } / { \mathfrak { p } } _ { T } ^ { 2 }$ where${ \mathfrak { p } } _ { S } = \alpha ^ { - 1 } ( { \mathfrak { p } } _ { T } )$. The existence of such an$S$seems to be well known (cf. [Ti2, §6]) but here is an argument suggested by N. Katz and H. Lenstra (independently).

Write$T = \mathcal { O } [ x _ { 1 } , \dots , x _ { r } ] / ( f _ { 1 } , \dots , f _ { s } )$with${ \mathfrak { p } } _ { T }$the image in$T$of${ \mathfrak { p } } =$ $( x _ { 1 } , \ldots , x _ { r } )$. Since$T$is local and finite and free over$\mathcal { O } .$, it follows that also $T \simeq { \mathcal { O } } [ [ x _ { 1 } , \dots , x _ { r } ] ] / ( f _ { 1 } , \dots , f _ { s } )$. We can pick$g _ { 1 } , \ldots , g _ { r }$such that$\begin{array} { r } { g _ { i } = \Sigma a _ { i j } f _ { j } } \end{array}$ with$a _ { i j } \in \mathcal { O }$and such that

$$
(f _ {1}, \dots , f _ {s}, \mathfrak {p} ^ {2}) = (g _ {1}, \dots , g _ {r}, \mathfrak {p} ^ {2}).
$$

We then modify$g _ { 1 } , \ldots , g _ { r }$by the addition of elements$\left\{ \alpha _ { i } \right\}$of$( f _ { 1 } , \ldots , f _ { s } ) ^ { 2 }$and set$( g _ { 1 } ^ { \prime } = g _ { 1 } + \alpha _ { 1 } , \ldots , g _ { r } ^ { \prime } = g _ { r } + \alpha _ { r } )$. Since$T$is finite over${ \mathcal { O } } _ { : }$there exists an$N$ such that for each$i , x _ { i } ^ { N }$can be written in$T$as a polynomial$h _ { i } ( x _ { 1 } , \ldots , x _ { r } )$of total degree less than$N$. We can assume also that N is chosen greater than the total degree of$g _ { i }$for each i. Set$\alpha _ { i } = ( x _ { i } ^ { N } - h _ { i } ( x _ { 1 } , \ldots , x _ { r } ) ) ^ { 2 }$. Then set $S = \mathcal { O } [ [ x _ { 1 } , \dots , x _ { r } ] ] / ( g _ { 1 } ^ { \prime } , \dots , g _ { r } ^ { \prime } )$. Then S is finite over O by construction and also dim$( S ) \leq 1$since dim$( S / \lambda ) = 0$where (λ) is the maximal ideal of O. It follows that$\{ g _ { 1 } ^ { \prime } , \ldots , g _ { r } ^ { \prime } \}$is a regular sequence and hence that$\operatorname { d e p t h } ( S ) = \dim ( S ) = 1$ In particular the maximal O-torsion submodule of S is zero since it is also a finite length S-submodule of S.

Now$\mathcal { O } / ( \bar { \eta } _ { S } ) \simeq \mathcal { O } / ( \bar { \eta } _ { T } )$, since$l ( \mathcal { O } / ( \bar { \eta } _ { S } ) ) = l ( { \mathfrak { p } } _ { S } / { \mathfrak { p } } _ { S } ^ { 2 } )$) by$( \mathrm { i } ) \Rightarrow \ ( \mathrm { i i } )$and $l ( \mathcal { O } / ( \hat { \eta } _ { T } ) ) = l ( \mathfrak { p } _ { T } / \mathfrak { p } _ { T } ^ { 2 } )$by hypothesis. Pick isomorphisms

$$
T \simeq \mathrm{Hom} _ {\mathcal {O}} (T, \mathcal {O}), S \simeq \mathrm{Hom} _ {\mathcal {O}} (S, \mathcal {O})
$$

as T-modules and S-modules, respectively. The existence of the latter for complete intersections over$\mathcal { O }$is well known; cf. conclusion 1 of Theorem A.3 of [M Ro]. Then we have a sequence of maps, in which$\hat { \alpha }$and$\hat { \beta }$denote the adjoints with respect to these isomorphisms:

$$
\mathcal {O} \xrightarrow {\hat {\beta}} T \xrightarrow {\hat {\alpha}} S \xrightarrow {\alpha} T \xrightarrow {\beta} \mathcal {O}.
$$

One checks that$\hat { \alpha }$is a map of S-modules (T being given an S-action via α) and in particular that$\alpha \circ { \hat { \alpha } }$is multiplication by an element t of$T .$. Now $( \beta \circ \hat { \beta } ) = ( \bar { \eta } _ { T } )$in O and$( \beta \circ \alpha ) \circ ( \widehat { \beta \circ \alpha } ) = ( \bar { \eta } _ { S } )$in O. As$( \bar { \eta } _ { S } ) = ( \bar { \eta } _ { T } )$in O, we have that t is a unit mod${ \mathfrak { p } } _ { T }$and hence that α◦αˆ is an isomorphism. It follows that$S \simeq T$, as otherwise$S \simeq$ker α ⊕ imˆα is a nontrivial decomposition as S-modules, which contradicts S being local.

Remark. Lenstra has made an important improvement to this proposition by showing that replacing$\bar { \eta } _ { T }$by β(ann p) gives a criterion valid for all local O-algebra which are finite and free over${ \mathcal { O } } _ { : }$, thus without the Gorenstein hypothesis.

## Princeton University<sub>,</sub> Princeton<sub>,</sub> NJ

## References

[AK]A.Altman and S.Kleiman,An Introduction to Grothendieck Duality Theory, vol. 146, Springer Lecture Notes in Mathematics, 1970.

[BiKu] B. Birch and W. Kuyk (eds.), Modular Functions of One Variable IV, vol. 476, Springer Lecture Notes in Mathematics, 1975.

[Bo]N. Boston, Families of Galois representations  Increasing the ramification, Duke Math. J. 66, 357-367.

[BH]W. Bruns and J. Herzog, Cohen-Macauley Rings, Cambridge University Press, 1993.

[BK]S. Bloch and K. Kato, L-Functions and Tamagawa Numbers of Motives, The Grothendieck Festschrift, Vol. 1 (P. Cartier et al. eds.), Birkh¨auser, 1990.

[BLR] N.Boston, H.Lenstra, and K.Ribet, Quotients of group rings arising from twodimensional representations, C. R. Acad. Sci. Paris t312, Ser. 1 (1991), 323-328.

[CF]J.W.S.Cassels and A.Frolich <sup>¨</sup> (eds.),Algebraic Number Theory,Academic Press, 1967.

[Ca1]H. Carayol, Sur les repr´esentations p-adiques associ´ees aux formes modulares de Hilbert, Ann. Sci. Ec. Norm. Sup. IV, Ser. 19 (1986), 409-468.

[Ca2], Sur les repr´esentationes galoisiennes modulo  attach´ees aux formes modulaires, Duke Math. J. 59 (1989), 785-901.

[Ca3], Formes modulaires et repr´esentations Galoisiennes \`a valeurs dans un anneau local complet, in p-Adic Monodromy and the Birch-Swinnerton-Dyer Conjecture (eds. B. Mazur and G. Stevens), Contemp. Math., vol. 165, 1994.

[CPS] E. Cline, B. Parshall, and L. Scott, Cohomology of finite groups of Lie type I, Publ. Math. IHES 45 (1975), 169-191.

[CS]J.Coates and C.G.Schmidt,Iwasawa theory for the symmetric square of an elliptic curve, J. reine und angew. Math. 375/376 (1987), 104-156.

[CW]J.Coates and A.Wiles, On p-adic L-functions and elliptic units, Ser.A26,J.Aust. Math. Soc. (1978), 1-25.

[Co]R. Coleman, Division values in local fields, Invent. Math. 53 (1979), 91-116.

[DR]P.DeligneandM.Rapoport,Sch´emasdemodularesdecourbeselliptiques,inSpringer Lecture Notes in Mathematics, Vol. 349, 1973.

[DS]P. Deligne and J-P. Serre, Formes modulaires de poids 1, Ann. Sci. Ec. Norm. Sup. IV, Ser. 7 (1974), 507-530.

[Dia]F. Diamond, The refined conjecture of Serre, in Proc. 1993 Hong Kong Conf. on Elliptic Curves, Modular Forms and Fermat’s Last Theorem, J. Coates, S. T. Yau, eds., International Press, Boston, 22-37 (1995).

[Di]L.E.Dickson,Linear Groups with an Exposition of the Galois Field Theory,Teubner, Leipzig, 1901.

[Dr]V. Drinfeld, Two-dimensional -adic representations of the fundamental group of a curve over a finite field and automorphic forms on GL(2), Am. J. Math. 105 (1983), 85-114.

[E1]B. Edixhoven, Two weight in Serre’s conjecture on modular forms, Invent. Math. 109 (1992), 563-594.

[E2], L’action de l’alg\`ebre de Hecke sur les groupes de composantes des jacobiennes des courbes modulaires set “Eisenstein”, in Courbes Modulaires et Courbes de Shimura, Ast´erisque 196-197 (1991), 159-170.

[Fl]M.Flach,A finiteness theorem for the symmetric square of an elliptic curve,Invent. Math. 109 (1992), 307-327.

[Fo]J.-M.Fontaine,Sur certains types de repr´esentations p-adiques du groupe de Galois d’un corp local; construction d’un anneau de Barsotti-Tate, Ann. of Math. 115 (1982), 529-577.

[Fr]G. Frey, Links between stable elliptic curves and certain diophantine equations, Annales Universitatis Saraviensis 1 (1986), 1-40.

[Gre1] R.Greenberg,Iwasawa theory for p-adic representations, Adv.St.Pure Math. 17 (1989), 97-137.

[Gre2],On the structure of certain Galois groups,Invent.Math. 47 (1978), 85-99.

[Gro]B.H.Gross,A tameness criterion for Galois representations associated to modular forms mod p, Duke Math. J. 61 (1990), 445-517.

[Guo] L. Gou, General Selmer groups and critical values of Hecke L-functions, Math. Ann. 297 (1993), 221-233.

[He]Y.Hellegouarch,Points d’ordre$2 { p } ^ { h }$sur les courbes elliptiques,Acta Arith.XXVI (1975), 253-263.

[Hi1]H. Hida, Iwasawa modules attached to congruences of cusp forms, Ann. Sci. Ecole Norm. Sup. (4) 19 (1986), 231-273.

[Hi2], Theory of p-adic Hecke algebras and Galois representations, Sugaku Expositions 2-3 (1989), 75-102.

[Hi3], Congruences of Cusp forms and special values of their zeta functions, Invent. Math. 63 (1981), 225-261.

[Hi4], On p-adic Hecke algebras for GL<sub>2</sub> over totally real fields, Ann. of Math. 128 (1988), 295-384.

[Hu] B. Huppert, Endliche Gruppen I, Springer-Verlag, 1967.

[Ih]Y. Ihara, On modular curves over finite fields, in Proc. Intern. Coll. on discrete subgroups of Lie groups and application to moduli, Bombay, 1973, pp. 161-202.

[Iw1] K. Iwasawa, Local Class Field Theory, Oxford University Press, Oxford, 1986.

[Iw2], On Z -extension of algebraic number fields, Ann. of Math. 98 (1973), 246-326.

[Ka]N. Katz, A result on modular forms in characteristic p, in Modular Functions of One Variable V, Springer L. N. M. 601 (1976), 53-61.

[Ku1]E.Kunz,Introduction to Commutative Algebra and Algebraic Geometry,Birkha¨user, 1985.

[Ku2], Almost complete intersection are not Gorenstein, J. Alg. 28 (1974), 111-115.

[KM]N.Katz and B.Mazur, Arithmetic Moduli of Elliptic Curves,Ann.of Math.Studies 108, Princeton University Press, 1985.

[La]R. Langlands, Base Change for GL , Ann. of Math. Studies, Princeton University Press 96, 1980.

[Li]W. Li, Newforms and functional equations, Math. Ann. 212 (1975), 285-315.

[Liv]R.Livn<sup>´</sup>e,On the conductors of mod  Galois representations coming from modular forms, J. of No. Th. 31 (1989), 133-141.

[Ma1] B. Mazur, Deforming Galois representations, in Galois Groups over Q, vol. 16, MSRI Publications, Springer, New York, 1989.

[Ma2], Modular curves and the Eisenstein ideal, Publ. Math. IHES 47 (1977), 33-186.

[Ma3], Rational isogenies of prime degree, Invent. Math. 44 (1978), 129-162.

[M Ri] B. Mazur and K. Ribet, Two-dimensional representations in the arithmetic of modular curves, Courbes Modulaires et Courbes de Shimura, Ast´erisque 196-197 (1991), 215-255.

[M Ro] B. Mazur and L. Roberts, Local Euler characteristics, Invent. Math. 9 (1970), 201-234.

[MT]B. Mazur and J. Tilouine, Repr´esentations galoisiennes, diferentielles de K¨ahler et conjectures principales, Publ. Math. IHES 71 (1990), 65-103.

[MW1] B. Mazur and A. Wiles, Class fields of abelian extensions of Q, Invent.Math. 76 (1984), 179-330.

[MW2], On p-adic analytic families of Galois representations, Comp. Math. 59 (1986), 231-264.

[Mi1]J. S. Milne, Jacobian varieties, in Arithmetic Geometry (Cornell and Silverman, eds.), Springer-Verlag, 1986.

[Mi2], Arithmetic Duality Theorems, Academic Press, 1986.

[Ram] R.Ramakrishna,On a variation of Mazur’s deformation functor, Comp.Math. 87 (1993), 269-286.

[Ray1] M. Raynaud, Sch´emas en groupes de type$( p , p , \ldots , p )$, Bull. Soc. Math. France 102 (1974), 241-280.

[Ray2],Sp´ecialisation du foncteur de Picard, Publ.Math.IHES 38 (1970), 27-76.

[Ri1]K.A.Ribet,On modular representations of Gal(Q<sup>¯</sup> /Q) arising from modular forms, Invent. Math. 100 (1990), 431-476.

[Ri2], Congruence relations between modular forms, Proc. Int. Cong. of Math. 17 (1983), 503-514.

[Ri3], Report on mod l representations of Gal(Q<sup>¯</sup> /Q), Proc. of Symp. in Pure Math. 55 (1994), 639-676.

[Ri4], Multiplicities of p-finite mod p Galois representations in J<sub>0</sub>(Np), Boletim da Sociedade Brasileira de Matematica, Nova Serie 21 (1991), 177-188.

[Ru1] K. Rubin, Tate-Shafarevich groups and L-functions of elliptic curves with complex multiplication, Invent. Math. 89 (1987), 527-559.

[Ru2], The ‘main conjectures’ of Iwasawa theory for imaginary quadratic fields, Invent. Math. 103 (1991), 25-68.

[Ru3], Elliptic curves with complex multiplication and the conjecture of Birch and Swinnerton-Dyer, Invent. Math. 64 (1981), 455-470.

[Ru4], More ‘main conjectures’ for imaginary quadratic fields, CRM Proceedings and Lecture Notes, 4, 1994.

[Sch] M. Schlessinger, Functors on Artin Rings, Trans. A. M. S. 130 (1968), 208-222.

[Scho] R. Schoof, The structure of the minus class groups of abelian number fields, in Seminaire de Th´eorie des Nombres, Paris (1988-1989), Progress in Math. 91, Birkhauser (1990), 185-204.

[Se]J.-P. Serre, Sur les repr´esentationes modulaires de degr´e 2 de Gal(Q<sup>¯</sup> /Q), Duke Math. J. 54 (1987), 179-230.

[de Sh] E. de Shalit, Iwasawa Theory of Elliptic Curves with Complex Multiplication, Persp. in Math., Vol. 3, Academic Press, 1987.

[Sh1]G. Shimura, Introduction to the Arithmetic Theory of Automorphic Functions, Iwanami Shoten and Princeton University Press, 1971.

[Sh2], On the holomorphy of certain Dirichlet series, Proc. London Math. Soc. (3) 31 (1975), 79-98.

[Sh3], The special values of the zeta function associated with cusp forms, Comm. Pure and Appl. Math. 29 (1976), 783-803.