# SPARSE EQUIDISTRIBUTION PROBLEMS, PERIOD BOUNDS, AND SUBCONVEXITY

## AKSHAY VENKATESH

Abstract. We introduce a “geometric” method to bound periods of automorphic forms. The key features of this method are the use of equidistribution results in place of mean value theorems, and the systematic use of mixing and the spectral gap. Applications are given to equidistribution of sparse subsets of horocycles and to equidistribution of CM points; to subconvexity of the triple product period in the level aspect over number fields, which implies subconvexity for certain standard and Rankin-Selberg L-functions; and to bounding Fourier coeficients of automorphic forms.

## Contents

1. Introduction. 1  
2. Notation. 13  
3. Unipotent periods. 23  
4. Semisimple periods: triple products in the level aspect. 29  
5. Application to $L$-functions. 35  
6. Torus periods (I): subconvex bounds for character twists over a number field. 40  
7. Torus periods (II): equidistribution of compact torus orbits. 46  
8. Background on Sobolev norms and reduction theory. 49  
9. Background on quantitative equidistribution results. 56  
10. Background on Eisenstein series. 67  
11. Background on integral representations of $L$-functions. 75  
References 90

## 1. Introduction.

1.1. General introduction. Let$\Gamma \subset G$be a lattice in an$S \mathrm { . }$-arithmetic group. Let $Y \subset \Gamma \backslash G$be a subset endowed with a probability measure$\nu ,$and f a function on $\Gamma \backslash G .$. Fixing a basis$\{ \psi _ { i } ^ { ( Y ) } \}$for$L ^ { 2 } ( Y , \nu )$, we shall refer to the numbers$\textstyle \int f \psi _ { j } ^ { ( Y ) } d \nu ,$ as the periods of$f$along$Y .$Evidently, the periods depend heavily on the choice of basis for$L ^ { 2 } ( Y , \nu )$. They play a major role in the theory of automorphic forms, in significant part because they often express information about L-functions.

The present paper is centered around a geometric method yielding upper bounds for these periods. It is applicable, roughly speaking, when considering the periods of a fixed function$f$along a sequence of subsets$( Y _ { i } , \nu _ { i } )$, with the property that the$Y _ { i }$ are becoming equidistributed; that is to say, the$\nu _ { i }$approach weakly the G-invariant measure on$\Gamma \backslash G$. The key inputs of this method are, firstly, the equidistribution of the$\nu _ { i }$, and secondly, the mixing properties of certain auxiliary flows. More precisely, we shall need these properties in a quantitative form; in the cases we consider, this will follow eventually from an appropriate spectral gap.

This situation might seem rather restrictive. However, it arises often in many natural equidistribution questions (“sparse equidistribution problems,” as we discuss below) as well as in the analytic theory of automorphic forms (especially, subconvexity results for L-functions). There are applications besides those discussed in the present paper; our aim has not been to give an exhaustive discussion, but rather just to present a representative sample of interesting cases. We shall explain the method abstractly in Sec. 1.3 and will carry out, in the body of the paper, one example of each of the following cases:$Y _ { i }$is the orbit of a unipotent, a semisimple, and a toral subgroup of G.

In the present paper, we have focused mostly on the case of$\mathrm { P G L _ { 2 } }$and$\mathrm { G L _ { 2 } }$over number fields. All our results pertain to this setting, except for Thm. 3.2, which applies to a general semisimple group. The geometric methods of this paper are general and we hope to analyze further higher rank examples in a future paper.

Throughout the present methods we have tried to use “soft” techniques as a substitute for explicit spectral expansions. However, there still seem to be instances where the explicit spectral expansions are important. In a future paper [23], joint with P. Michel, we shall combine ideas drawn from this paper with ideas from Michel’s paper [22]; in that paper, we shall make much more explicit use of spectral decomposition.

We shall use the term “sparse equidistribution problems” to describe questions of the following flavor: Suppose$Z _ { i } \subset Y _ { i }$is a subset endowed with a measure$\nu _ { i } ^ { Z }$, and we would like to prove that the$\nu _ { i } ^ { Z }$are becoming equidistributed. In other words, we wish to deduce the equidistribution of the “sparse” subset$Z _ { i }$from the known equidistribution of$Y _ { i }$. Examples of this type of question are Shah’s conjecture [32] (where the$Z _ { i }$are discrete subsets of$Y _ { i }$, a full horocycle orbit) as well as Michel’s results on subsets of Heegner points [22] (where the$Z _ { i }$are subsets of the $Y _ { i } ,$, the set of all Heegner points.) The connection to period integrals is as follows: one can spectrally expand the measure$\nu _ { i } ^ { Z }$in terms of the basis for$L ^ { 2 } ( Y _ { i } , \nu _ { i } )$ Using our results for periods along$Y _ { i } ,$it will sometimes be possible to deduce the equidistribution of$\nu _ { i } ^ { Z }$

We now briefly summarize our results.

(1) Sec. 3 considers where the$Y _ { i } \mathrm { s }$are orbits, or pieces of orbits, of unipotent groups. The mixing flow is the horocycle flow along$Y _ { i }$

In Thm. 3.1 (p. 24) we show that certain sparse subsets of horocycles on compact quotients of$\operatorname { S L _ { 2 } } ( \mathbb { R } )$become equidistributed. This is progress towards a conjecture of N. Shah. In Thm. 3.2 (p. 27) we give a fairly general bound (in the context of an arbitrary semisimple group) on the Fourier coeficients of automorphic forms. In the case of$G = \mathrm { { S L } _ { 2 } ( \mathbb { R } ) }$it recovers results of Good [13] and Sarnak [30], which resolved a problem of Selberg. The present proof is more direct, avoiding in particular the triple product bounds for eigenfunctions.

(2) Sec. 4 considers the case when$G = { \mathrm { P G L } } _ { 2 } ( F \otimes \mathbb { R } )$, where$F$is a number field, and Γ is a congruence subgroup thereof. The$Y _ { i }$are a sequence of closed diagonal G-orbits on$\Gamma \backslash G \times \Gamma \backslash G$. The mixing flow (after lifting to the adeles) is the diagonal action of$\mathrm { P G L _ { 2 } } ( \mathbb { A } _ { F , f } )$, where$\mathbb { A } _ { F , f }$is the ring of finite adeles of$F$

Prop. 4.1 and Prop. 4.2 give period bounds in this context. We refer to Prop. 4.1 as a subconvex bound for the triple product period, for the reason that it should be in fact be equivalent to subconvexity for the triple product L-function, in the level aspect as one factor varies, but the necessary computation of p-adic integrals (Hypothesis 11.1) has apparently not yet been done in suficient generality. In Thm. 5.1 (p. 35) it is shown that these results yield subconvex bounds, in the level aspect, for standard and Rankin-Selberg L-functions attached to PGL .

The results on standard and Rankin-Selberg L-functions generalize results of Duke-Friedlander-Iwaniec and Kowalski-Michel-Vanderkam from the case$F = \mathbb { Q } . ^ { 1 }$The third result, concerning subconvexity of the triple product period in the level aspect, was not known even over$\mathbb { Q } ;$however, Bernstein and Reznikov [3] have shown subconvexity for the triple product period in the eigenvalue aspect.

(3) Sec. 6 considers the case when$Y _ { i }$is a certain family of noncompact torus orbits on$\Gamma \backslash G ,$, where$( \Gamma , G )$is as in Sec. 4. (In fact, the$Y _ { i }$are obtained by taking a fixed noncompact torus orbit, and translating by a p-adic unipotent, where p varies.) The mixing flow is the action of the adelic points of the torus.

We establish in Thm. 6.1 (p. 40) subconvexity for character twists of${ \mathrm { G L } } ( 2 )$in the level aspect. This was established for$F = \mathbb { Q }$by Duke-Friedlander-Iwaniec, and the special case where$F$is totally real and the form holomorphic at all infinite places was treated by Cogdell, Piatetski-Shapiro and Sarnak. In particular, (6.2) gives a subconvex bound for Gr¨ossencharacter L-functions over$F ,$in the level aspect; this was known over Q by work of Burgess, and some special cases were known in the general case.

(4) In Sec. 7 we consider the case where$Y _ { i }$is a (union of) compact torus orbits on Γ G, where (Γ, G) are as in Sec. 4. The equidistribution of such$Y _ { i }$will amount to the equidistribution of Heegner points, and we deduce it from Thm. 6.1 in Thm. 7.1 (p. 47). This result generalizes work of Duke over Q and was proven, conditionally on GRH, by Zhang, Cohen, and Ullmo-Clozel (independently). The present work makes this result unconditional.

Applying mixing properties of the adelic torus flow, we obtain in Thm. 7.2 (p. 48) we obtain, under a condition of splitting of enough small primes, the equidistribution of certain sparse subsets of Heegner points. In the case $F = \mathbb { Q } .$an unconditional result of this nature is due to Michel.<sup>2</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">PGL<sub>2</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>We have not attempted to address the issue of varying the central character. This, in a sense, is the most subtle point, as is shown by Michel’s recent work on Rankin-Selberg convolutions. Our aim in the present paper has been to show that one can derive a coherent theory for from the triple product bound of Prop. 4.1. The case of varying central character will be discussed in a future paper with Michel.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>Our method is diferent to Michel’s: we do not deduce our result from results on Rankin-Selberg convolutions, and indeed it is possible to deduce a subconvexity result from ours. However, there seem to be some curious parallels between the methods. In fact, the method of Thm. 7.2 is even more closely related – as Michel has pointed out to me – to the work [10] of Duke, Friedlander and Iwaniec. In that paper they amplify class group L-functions but obtain only a conditional result for precisely the same reason that Thm. 7.2 fails to be unconditional, namely, one cannot guarantee unconditionally the existence of enough small split primes.</span></small>

In that context of L-functions, one pleasing feature of the present method is that it is geometric: it proceeds not via Fourier coeficients but via the integral representation. In practice, this means that there is no diference between Maass or holomorphic forms, nor between$\mathbb { Q }$and an arbitrary base field. Moreover, we do not make use of either the trace formula or the Kuznetsov formula; indeed, we make no explicit use of families.

The recent work of Bernstein-Reznikov [3] is of a similar flavor. They establish a “subconvex” bound for the triple product when the eigenvalue of one factor varies, whereas we have treated the case where the level of one factor varies. Their method is also geometric in nature, and moreover their result applies to a nonarithmetic group. By contrast, the level aspect question is not well-posed if one leaves the arithmetic setting.

Throughout the paper we have not attempted to optimize the results. The input to our method is an equidistribution result. As far as possible we have tried to establish these results by relatively “geometric” methods, deriving in the end from the mixing properties of a certain flow. Of course, it is in many contexts better to use spectral methods, but this would involve departing from the geometric method that is intended to be the central theme of this paper. As remarked, we will pursue such “spectral” approaches in a forthcoming paper with P. Michel [23]; some of the results of this have been discussed in [24].

Finally, implicit in various parts of the paper is “adelic analysis”, i.e. the analytic theory of functions on adelic quotients, in the quantitative sense needed for analytic number theory. There seems to be considerable scope to develop this theory fully.

1.2. Other applications. The method of this paper has other applications not elaborated here. We discuss some of them here.

There are other subconvexity results that are naturally approached by the same method: for instance, a subconvex estimate for$L ( \pi , { \frac { 1 } { 2 } } + i t )$where t varies and π is a fixed cuspidal representation of GL(2) over a number field F. In such a context it is natural to use the fact that the horocycle flow is (quantifiably) weakly k-mixing, for certain$k > 1 ;$; the use of this higher order mixing is closely related to Weyl’s “successive squaring” approach to$\zeta ( 1 / 2 + i t )$. Of course, this particular instance of subconvexity is approachable by standard methods also; an intriguing question in the subconvexity context is how to combine the present methods with those such as Bernstein-Reznikov.

There are certain applications to efective equidistribution theorems: for instance, it is also possible to establish some new efective cases of Ratner’s theorem by the same ideas, see Rem. 3.1. The question of giving such “nontrivial” cases was raised by Margulis in his talk at the American Institute of Mathematics, June 2004. Unfortunately, these new cases are rather artificial.

One can give certain analytic applications: let Γ be a cocompact subgroup of $\mathrm { S L } ( 2 , \mathbb { R } )$, and let$\pi \subset L ^ { 2 } ( \Gamma \backslash \mathrm { S L } ( 2 , \mathbb { R } ) )$be an irreducible$\operatorname { S L } ( 2 , \mathbb { R } )$)-subrepresentation. For$m \in \mathbb { Z } .$let$e _ { m }$be the mth weight vector in$\pi ,$if defined; i.e. a vector which transforms under the character${ \left( \begin{array} { l l } { \ \cos ( \theta ) } & { \sin ( \theta ) } \\ { - \sin ( \theta ) } & { \cos ( \theta ) } \end{array} \right) } \ \mapsto \ e ^ { 2 \pi i m \theta }$. We normalize it (up to a complex scalar of absolute value 1) by requiring that$\| e _ { m } \| _ { L ^ { 2 } } = 1$ Bernstein and Reznikov proved the bound$\| e _ { m } \| _ { L ^ { \infty } } \ll ( 1 + | m | ) ^ { 1 / 2 }$, and asked$[ 2 ,$ Remark 2.5(4)] if any improvement of the exponent$1 / 2$is possible. It is quite easy to deduce from Lem. 3.1 such a bound; indeed, the analytic properties of the$e _ { m } .$

as$| m | \to \infty ,$is connected with the long time behavior of the horocycle flow in the same fashion that the analytic behavior of Laplacian eigenfunctions are connected to the long time behavior of the geodesic flow. In the time during which this paper was being revised for submission, Reznikov has proven independently a result of this type [28]. Since the result he obtains is most likely sharper than that obtained by the technique indicated above, we will not pursue this further, noting only that an advantage of the method we have indicated above is that it is likely to generalize to higher rank.

Moving slightly away from the main subject of the present paper, the idea of using equidistribution theorems to produce mean value results for L-functions seems capable of application in a variety of settings. In particular, equidistribution results are readily available on$\operatorname { G L } ( n )$, owing to Ratner’s work, whereas trace formulae are extremely unwieldy for$n > 2$. It would be interesting to see what mean-value statements can be deduced from Ratner-type equidistribution results.

Historically, one application of such results has been to nonvanishing results; here the most spectacular results (e.g. [34]) have been achieved through the socalled mollifier technique. It would be quite interesting to understand if there is a geometric interpretation of the mollifier technique.

1.3. Discussion of method: equidistribution, mixing, and periods. We now turn to a discussion of the specifics of the method used in this paper. This method itself is quite easy to describe. It consists in essence of two simple steps (see (1.2) and (1.3) below).

We also remark that the discussion that follows is a relatively faithful rendition of the method of the paper. The body of this paper does not really utilize any new ideas beyond the ones indicated below. Most of the bulk consists of the technical details necessary to connect periods with other objects of interest (e.g. equidistribution questions or L-functions), as well as setting up the machinery to quantify some standard equidistribution results. As much as possible, we have tried to give a self-contained treatment of all these technical details in Sections 8 – 11.

We hope the ensuing discussion serves as a unifying thread for the rest of the paper. We explain the method first in an abstract setting (Sec. 1.3.1). We then explain (Sec. 1.3.2 and 1.3.3) these ideas in a a more down-to-earth fashion, emphasizing the parallel with the analytic techniques for studying L-functions. Finally, Sec. 1.3.4 illustrates these ideas in a simple example – that of Fourier coeficients of modular forms.

1.3.1. Abstract setting. Let$G _ { 2 } \subset G _ { 1 }$be locally compact groups,$\Gamma \subset G _ { 1 }$a lattice, $X = \Gamma \backslash G _ { 1 }$. Let$x _ { i } \in X$and put$Y _ { i } = x _ { i } G _ { 2 }$. We shall suppose that there exists a $G _ { 2 }$-invariant probability measure$\nu _ { i }$on$Y _ { i } .$(This does not precisely cover all the contexts we consider – at some points we will consider$Y _ { i }$which are “long pieces” of a$G _ { 2 }$-orbit rather than a single$G _ { 2 }$-orbit, but the ideas in that case will be identical to those discussed here).

Let$f$be a function on$X$and ψ<sub>i</sub> a function on$Y _ { i }$such that$\textstyle \int _ { Y _ { i } } | \psi _ { i } | ^ { 2 } d \nu _ { i } = 1$. We will give a bound for the period$\int _ { Y _ { i } } f \psi _ { i } d \nu _ { i }$

In words, the idea will be to find certain correlations between the values of$\psi$ at diferent points; and then show that the values of$f$at these same points are “uncorrelated,” in some quantifiable sense. Putting these together will show that the period must be small. The “hard” ingredient here is some version of the spectral gap, i.e. quantitative mixing, which is what will show that the “uncorrelated-ness” property of$f$.

We will suppose that there exists$\sigma ,$, a measure on$G _ { 2 }$, such that

$$
\psi_ {i} \star \sigma = \lambda_ {i} \psi_ {i},\tag{1.1}
$$

for some$\lambda _ { i } \in \mathbb { C }$. Here ⋆σ denotes the action of$\sigma$by right convolution. Let$\check { \sigma }$be the image of$\sigma$by the involution$g \mapsto g ^ { - 1 }$of$G _ { 2 }$.

Then

$$
\begin{array}{r l r} & & {\left| \int f \cdot \psi_ {i} d \nu_ {i} \right| ^ {2} = \left| \lambda_ {i} ^ {- 1} \int_ {Y _ {i}} f \cdot (\psi_ {i} \star \sigma) d \nu_ {i} \right| ^ {2} = \left| \lambda_ {i} ^ {- 1} \int_ {Y _ {i}} (f \star \check {\sigma}) \cdot \psi_ {i} d \nu_ {i} \right| ^ {2}} \\ & & {\leq | \lambda_ {i} | ^ {- 2} \int_ {Y _ {i}} | f \star \check {\sigma} | ^ {2} d \nu_ {i},} \end{array}\tag{1.2}
$$

where we have applied Cauchy-Schwarz at the final step. Now, we are assuming that the$Y _ { i }$are becoming equidistributed, and so$\nu _ { i } \longrightarrow \nu .$, the$G _ { 1 }$invariant measure on$\Gamma \backslash G _ { 1 }$. Thus

$$
\begin{array}{c} \int_ {Y _ {i}} | f \star \check {\sigma} | ^ {2} d \nu_ {i} \approx \int_ {X} | f \star \check {\sigma} | ^ {2} d \nu \\ = \int_ {g, g ^ {\prime} \in G _ {2}} \langle g g ^ {\prime - 1} \cdot f, f \rangle_ {L ^ {2} (X)} d \sigma (g) d \sigma (g ^ {\prime}), \end{array}\tag{1.3}
$$

where$g g ^ { \prime - 1 } \cdot f$denotes the right translate of$f$by$g g ^ { \prime - 1 }$

If the G<sub>2</sub>-action on X is mixing in a quantifiable way – i.e., one has strong bounds on the decay of matrix coeficients – one obtains good upper bounds on the right-hand side of (1.3); in combination with (1.2) this gives an upper bound for the period$\textstyle { \big | } \int _ { Y _ { i } } f \psi _ { i } d \nu _ { i } { \big | }$

The strength of the information required about the mixing varies. In the cases we study where$G _ { 2 }$is amenable, any nontrivial information will sufice. In the one case where$G _ { 2 }$is semisimple, a strong bound towards Ramanujan is needed. For instance, in the case of triple products, we need any improvement of the bound that the pth Hecke eigenvalue of a cusp form on${ \mathrm { G L } } ( 2 )$is bounded in absolute value by $p ^ { 1 / 4 } + p ^ { - 1 / 4 }$. (In this normalization, the trivial bound is$p ^ { 1 / 2 } + p ^ { - 1 / 2 } )$.

In the rest of this paper, we shall merely apply this argument many times, with various diferent choices for$\Gamma , G _ { 1 } , G _ { 2 }$. The part of the argument which will vary is quantifying the equidistribution of the$\nu _ { i }$, i.e. keeping track of the error in the first approximation of (1.3). Thus we make heavy use of Sobolev norms (Sec. 8), which are an eficient method of bounding this error.

In each instance, the proof of the equidistribution result$\nu _ { i } \to \nu$will always be rather straightforward, except for the result of Sec. 7. The equidistribution result needed for the proof of Thm. 7.2 is essentially equivalent to the subconvexity result proved in Sec. 6. A rather striking point is that a similar logical dependence (although manifested very diferently) is present in the work of Michel. The meaning of this is unclear to the author.

In certain specific cases, the above technique is quite familiar. When$G _ { 2 }$is a one-parameter real group, the above argument is quite closely related to standard techniques of analytic number theory.$\overset \sim { 3 }$On the other hand, when$G _ { 2 }$is an adelic group, and σ a measure on$G _ { 2 }$that corresponds to the action of Hecke operators (this is carried out in Sec. 4, for instance), the above argument will be essentially “amplification” in the sense of Friedlander-Iwaniec [12].

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">G2</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">| fψ<sub>i</sub>dν<sub>i</sub>|<sup>4</sup>, | fψ<sub>i</sub>dν<sub>i</sub>|<sup>8</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>For example, in certain contexts when G<sub>2</sub> is abelian, one can push this method further by squaring multiple times, that is to say, considering  and so forth. In this</span></small>

In the following two sections, we shall attempt to explain more colloquially the main idea that is at work here, and also discuss how the method described above fits into the framework of analytic number theory. Modern proofs of subconvexity, following the path-breaking work of Friedlander-Iwaniec [12], have roughly speaking consisted of a mean-value theorem and an amplification step. We shall discuss how the proof indicated above may be viewed as geometrizing this strategy, where the mean-value step is replaced by an equidistribution theorem, and the amplification step is controlled using mixing.

Note, in particular, that in the work of Friedlander-Iwaniec, families of$L _ { - }$ functions play a central role, whereas the method above has in a certain sense eliminated the family. Although in the discussion below we rephrase matters so as to make clear the connection with the work of Friedlander-Iwaniec, it seems that from the perspective of the present paper the phrasing in terms of families is rather artificial.

1.3.2. Connection with analytic number theory: Equidistribution, and mean-value theorem for periods. Follow the notations of the previous section. We choose an orthonormal basis$\{ \psi _ { i , j } \} _ { j = 1 } ^ { \infty }$for$L ^ { 2 } ( Y _ { i } , \nu _ { i } )$so that$\psi _ { i , 1 } : = \psi _ { i }$

By Plancherel’s formula,$\begin{array} { r } { \sum _ { j = 1 } ^ { \infty } \left| \int f \psi _ { i , j } d \nu _ { i } \right| ^ { 2 } = \int | f | ^ { 2 } d \nu _ { i } } \end{array}$. Since$\nu _ { i } \to \nu$weakly, and we are holding f fixed, it follows that:

$$
\sum_ {j = 1} ^ {\infty} \left| \int f \psi_ {i, j} d \nu_ {i} \right| ^ {2} \rightarrow \int_ {\Gamma \backslash G} | f | ^ {2} d \nu ,\tag{1.4}
$$

as$i \to \infty$. Thus the equidistribution property of$\nu _ { i }$underlies a mean-value theorem for the$Y _ { i } .$-periods.

In many cases involving automorphic forms, the periods will essentially be special values of L-functions and (1.4) amounts to a mean-value theorem for L-functions. This is fairly well-known; for example, the mean-value theorem$\begin{array} { r } { \int _ { - T } ^ { T } | \zeta ( 1 / 2 + i t ) | ^ { 4 } d t \sim } \end{array}$ $T \log ( T ) ^ { 4 }$is rather closely connected with the equidistribution properties of the cycle$\{ ( 1 + i / T ) x , x \in \mathbb { R } \}$, when projected to$\mathrm { S L _ { 2 } ( Z ) \backslash \mathbb { H } }$. A more striking example is Vatsal’s use of equidistribution to prove nonvanishing results [38]. In general, it seems that there are many interesting mean value theorems for L-functions that are connected to equidistribution results.

In any case, (1.4) is not unrelated to the standard methods of obtaining such results; however, its primary advantage is that it is often technically much simpler, for example when working over a number field.

1.3.3. Connection with analytic number theory (II): Mixing, and bounds for a single period. We now wish to pass from (1.4) to nontrivial upper bounds for a single period. It is clear that (1.4) implies at once – by omitting all terms but one – that$\begin{array} { r } { | \int f \psi _ { i , j } d \nu _ { i } | \stackrel { < } { \sim } \| f \| _ { L ^ { 2 } ( X ) } ; } \end{array}$we shall refer to an improvement of this bound as nontrivial. It is evident that one must have some further information about$\{ \psi _ { i , j } \}$ in order to do this; otherwise one could simply take$\psi _ { i , 1 }$to be a multiple of$f | _ { Y _ { i } }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">G<sub>2</sub>-</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">G<sub>2</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">ζ(1/2 + it).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">context, one replaces the mixing property of the action with results about higher order mixing of the flow. Although we will not carry this out in the present paper, this seems rather closely connected to Weyl’s proof of subconvexity for</span></small>

In the context of analytic number theory, this is often carried out by “shortening the family,” that is to say: proving a sharp mean-value theorem of the form of$( 1 . 4 )$ but over some subfamily of$\{ \psi _ { i , j } \} _ { j = 1 } ^ { \infty } ;$then omitting all terms but$\psi _ { i , 1 } = \psi _ { i }$will often give a nontrivial upper bound. In the work of Friedlander-Iwaniec, a weighted mean-value theorem is derived, which has the same efect as shortening the family.

Such a weighted mean-value theorem is also implicit in our context. Following the notation of Sec. 1.3.1, suppose that there is a fixed measure σ on$G _ { 2 }$such that for all$i , j$, we have$\psi _ { i , j } \star \sigma = \lambda _ { i , j } \psi _ { i , j }$(some$\lambda _ { i , j } \in \mathbb { C } )$. Then, by Plancherel’s formula, and using the fact$\nu _ { i } \to \nu .$we conclude:

$$
\sum_ {j = 1} ^ {\infty} \left| \lambda_ {i, j} \right| ^ {2} \left| \int f \cdot \psi_ {i, j} d \nu_ {i} \right| ^ {2} \rightarrow \langle f \star \check {\sigma}, f \star \check {\sigma} \rangle_ {L ^ {2} (X)}.\tag{1.5}
$$

This gives a weighted mean value theorem, which for appropriate choices of$\sigma$ amounts to shortening the efective range of summation in (1.4). Moreover, the mixing of the$G _ { 2 } .$-flow bounds the right hand side of$( 1 . 5 )$. In this phrasing, it becomes clear that the measure$\sigma$has played the role of an “amplifier” and the orthonormal basis for$L ^ { 2 } ( Y _ { i } , \nu _ { i } )$has played the role of the family.

Having now explained the method in an abstract context and indicated its equivalence with other methods, we now indicate more informally the source of cancellation in periods that is at the center of our results.

In many natural situations, one obtains a basis for$L ^ { 2 } ( Y _ { i } , \nu _ { i } )$by diagonalizing a geometrically defined algebra of operators on$Y _ { i } .$. The result of this process is that the functions$\{ \psi _ { j } \}$exhibit correlations between their values at diferent points of$Y$. For instance (for example when$G _ { 2 }$is semisimple), it often will occur that there is a correspondence${ \mathcal { C } } : Y \mapsto Y$such the value of each$\psi _ { j }$at$P \in Y$and at the collection of points$\mathcal { C } ( P )$are correlated in some way. On the other hand (and we shall now speak quite imprecisely) if the correspondence$\mathcal { C } \mathrm { \ t e x t e n d s } ^ { \prime \prime }$to a correspondence${ \tilde { \mathcal { C } } } : X \mapsto X$one can often show, using mixing properties of${ \tilde { \mathcal { C } } } ,$, that the values of$f$at$P$and$\tilde { \mathcal { C } } ( P )$will be uncorrelated, at least if$P$is chosen at random w.r.t the the uniform measure on$X$

However, since the$Y _ { i }$are becoming equidistributed, it amounts to almost the same thing to choose$P$at random w.r.t.$\nu _ { i }$and w.r.t. the uniform measure on$X$ Thus, for ν -typical$P \in Y _ { i }$, the values of$f$at$P$and$\mathcal { C } ( P )$are uncorrelated, whereas the values of$\psi _ { j }$at$P$and$\mathcal { C } ( P )$are correlated. One can then play these phenomena against each other to obtain cancellation in the period integral$\int f \psi _ { j } d \nu _ { i }$

1.3.4. A concrete example. We shall now discuss how to bound Fourier coeficients of a modular form by the methods just described. Although the material below is essentially redone - with$\mathrm { S L } ( 2 , \mathbb { R } )$replaced by a general group – in Sec. 3, the example below was very important in motivating the author’s intuition, and it seems worthwhile to include it in the introduction.

Let$\Gamma \subset \mathrm { S L } ( 2 , \mathbb { R } )$be a lattice containing the element$\left( \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right)$. Let$f ( z )$be a holomorphic form of weight$2 \ \mathrm { w . r . t }$. Γ, which we write in a Fourier expansion $\begin{array} { r } { f ( z ) = \sum _ { n = 1 } ^ { \infty } a _ { n } e ^ { 2 \pi i n z } } \end{array}$. Hecke proved the bound$| a _ { n } | \leq C n .$a bound which was only improved (for a general – possibly nonarithmetic –$\Gamma )$much later, to$\left. a _ { n } \right. \le C n ^ { 5 / 6 }$ 2 by$\mathrm { A }$. Good. We shall sketch a simple proof of a nontrivial bound$| a _ { n } | \leq C n ^ { 1 - \delta }$ along the lines just indicated; for further details, we refer the reader to Sec. 3.2, where the procedure outlined is implemented for a general semisimple group.

We note that the ideas that will enter here are exactly those that will enter into the proof of equidistribution of sparse subsets of horocycles (see Sec. 3.1), or for the nontrivial bound for$L ^ { \infty }$norms in the weight aspect that is discussed in Sec. 1.2. The proof below also works for Maass forms (in that case the result is due to Sarnak).

The Fourier expansion implies that

$$
a _ {n} = e ^ {2 \pi} \int_ {x \in \mathbb {R} / \mathbb {Z}} f (x + \frac {i}{n}) e ^ {- 2 \pi i n x}.\tag{1.6}
$$

In words, the idea is as follows: the function$e ^ { - 2 \pi i n x }$takes the same values at $\textstyle x , x + { \frac { 1 } { n } } , x + { \frac { 2 } { n } } , \dotsc .$On the other hand, the values of the function$f$at these points are (in a quantifiable sense) uncorrelated, as we shall deduce from the mixing properties of the horocycle flow. Playing these two properties against each other will yield an improvement of the Hecke bound for$\left| a _ { n } \right|$4

Let$\tilde { f }$be the lift of f to$\Gamma \backslash \mathrm { S L } ( 2 , \mathbb { R } )$; that is to say,

$$
\tilde {f}: \Gamma \left( \begin{array}{c c} a & b \\ c & d \end{array} \right) \mapsto f (\frac {a i + b}{c i + d}) (c i + d) ^ {- 2}.
$$

Let$x _ { n } = \Gamma \left( \begin{array} { c c } { { n ^ { - 1 / 2 } } } & { { 0 } } \\ { { 0 } } & { { n ^ { 1 / 2 } } } \end{array} \right)$, and put$n ( t ) = { \left( \begin{array} { l l } { 1 } & { t } \\ { 0 } & { 1 } \end{array} \right) }$. Then the definitions show that$\begin{array} { r } { \tilde { f } ( x _ { n } n ( t ) ) = n ^ { - 1 } f ( \frac { i + t } { n } ) } \end{array}$; consequently, we see that

$$
a _ {n} = e ^ {2 \pi} \int_ {t = 0} ^ {n} \tilde {f} (x _ {n} n (t)) e ^ {- 2 \pi i t} d t\tag{1.7}
$$

(1.7) expresses the nth Fourier coeficient of$f$as the integral of$\tilde { f }$over a closed horocycle of length n. Moreover, (1.7) falls into the pattern of Sec. 1.3.1, with$G _ { 1 } =$ $\operatorname { S L _ { 2 } } ( \mathbb { R } )$,$G _ { 2 } = \{ n ( t ) : t \in \mathbb { R } \} , Y _ { n } = \{ x _ { n } n ( t ) : t \in \mathbb { R } \}$, and$\psi _ { n } : Y _ { n } \to \mathbb { C }$the function given by$x _ { n } n ( t ) \mapsto e ^ { - 2 \pi i t }$. The fact that the$Y _ { n }$are becoming equidistributed amounts to the “equidistribution of low horocycles,” cf. [31]. In the language of Sec. 1.3.1, we will take$\sigma$to be the measure on$G _ { 2 } \cong \mathbb { R }$that is a sum of point masses$\delta _ { i } ,$for integers$i = 1 , \ldots , K$. We now carry out the procedure of Sec. 1.3.1 in an explicit fashion in the paragraphs that follow.

Let$T$be the operation of right translation by n(1) on$C ^ { \infty } ( \Gamma \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } ) )$: that is to say, for$F \in C ^ { \infty } ( \Gamma \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } ) )$, we put$T F ( g ) = F ( g n ( 1 ) )$

The value of the right-hand side of (1.7) remains unchanged if we replace$\tilde { f }$by $T \tilde { f } ;$consequently, for any integer$K \geq 1$, we have

$$
a _ {n} = \frac {e ^ {2 \pi}}{K} \int_ {t = 0} ^ {n} (\sum_ {i = 0} ^ {K - 1} T ^ {i} \tilde {f} (x _ {n} n (t)) e ^ {- 2 \pi i t} d t.
$$

Applying the Cauchy-Schwarz inequality we deduce that

$$
\left| a _ {n} \right| ^ {2} \leq \frac {n}{e ^ {- 4 \pi} K ^ {2}} \int_ {t = 0} ^ {n} \left| \sum_ {i = 0} ^ {K - 1} T ^ {i} \tilde {f} (x _ {n} n (t)) \right| ^ {2} d t.\tag{1.8}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">P<sup>K</sup>k=1 <sup>c</sup>k</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">c<sub>k</sub> = f( <sup>k+i</sup> ), K = n.)n</span></small>

We now use come to the equidistribution part of the argument. The equidistribution of long closed horocycles asserts that the closed horocycle$\{ x + i y : 0 \leq x \leq 1 \}$ becomes equidistributed in$\Gamma \backslash \mathbb { H }$as$y  \infty$. Quantitatively, for any$F \in C ^ { \infty } ( \Gamma \backslash \mathbb { H } )$ we have

$$
\left| \int_ {0} ^ {1} F (x + i y) d x - \int_ {\Gamma \backslash \mathbb {H}} F \right| \leq C _ {F} y ^ {\delta},\tag{1.9}
$$

for some$C _ { F }$depending on$F _ { ; }$, and some$\delta$depending only on$\Gamma .$This assertion, originally proved by Sarnak [31] by spectral methods, can be deduced quite easily from the mixing properties of the geodesic flow; this is done, in a somewhat more general context, in Lem. 9.6.

We note that – a special case of the discussion in Sec. 1.3.2 – the equidistribution statement$( 1 . 9 )$above reflects a mean-value theorem for periods. Indeed, if one applies it to$F = y ^ { 2 } | f | ^ { 2 }$, one deduces the asymptotic for$\textstyle \sum _ { n < X } | a _ { n } | ^ { 2 }$

In any case, what will be more useful is the version of$( 1 . 9 )$that is lifted to $\Gamma \backslash \mathrm { S L _ { 2 } } ( \mathbb { R } )$. This asserts that for any$F \in C ^ { \infty } ( \Gamma \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } ) )$, we have

$$
\left| \frac {1}{n} \int_ {t = 0} ^ {n} F (x _ {n} n (t)) d t - \int_ {\Gamma \backslash \mathrm{SL} _ {2} (\mathbb {R})} F (g) d g \right| \leq C _ {F} n ^ {- \delta},\tag{1.10}
$$

where$\delta$is an explicit constant depending only on$\Gamma _ { \mathrm { {  } } }$, and$C _ { F }$is a constant depending on$F$

From (1.8) and (1.10) we conclude that

$$
\left| a _ {n} \right| ^ {2} \ll \frac {e ^ {4 \pi} n ^ {2}}{K ^ {2}} \left(\| \sum_ {i = 0} ^ {K - 1} T ^ {i} \tilde {f} \| _ {L ^ {2} (\Gamma \backslash \mathrm{SL} _ {2} (\mathbb {R}))} ^ {2} + C _ {f, K} n ^ {- \delta}\right).\tag{1.11}
$$

On the other hand, the explicit derivation of (1.10) shows that$C _ { F }$may be bounded by a Sobolev norm of$F$, and consequently the constant$C _ { f , K }$that appears in (1.11) is bounded by$O _ { f } ( K ^ { A } )$for some$A > 0$. Thus

$$
\left| a _ {n} \right| ^ {2} \ll_ {f} n ^ {2} K ^ {- 2} \left(\left\| \sum_ {i = 0} ^ {K - 1} T ^ {i} \tilde {f} \right\| _ {L ^ {2} \left(\Gamma \backslash \mathrm{SL} _ {2} (\mathbb {R})\right)} ^ {2} + K ^ {A} n ^ {- \delta}\right).
$$

We now use the fact that the horocycle flow is mixing, in a quantifiable way. This amounts to the assertion that there is an explicit$\delta ^ { \prime } > 0$and constant$C _ { f } ^ { \prime }$such that, for$i \in \mathbb { Z } , | \langle T ^ { i } \tilde { f } , \tilde { f } \rangle | \ll C _ { f } ^ { \prime } ( 1 + | i | ) ^ { - \delta ^ { \prime } }$. It follows easily that

$$
\| \sum_ {i = 0} ^ {K - 1} T ^ {i} \tilde {f} \| _ {L ^ {2}} ^ {2} \ll_ {f} K ^ {2 - \delta^ {\prime}}.
$$

We conclude that$| a _ { n } | \ll n ( K ^ { - \delta ^ { \prime } / 2 } { + } K ^ { A / 2 - 1 } n ^ { - \delta / 2 } )$. Taking K to be a suficiently small power of$n ,$we conclude that$a _ { n }$is bounded by$n ^ { 1 - \delta ^ { \prime \prime } }$for some$\delta ^ { \prime \prime } > 0$ depending only on Γ.

Clearly$\delta ^ { \prime \prime }$depends only on the spectral gap of$\Gamma \backslash \mathrm { S L _ { 2 } } ( \mathbb { R } )$. Of course, this dependence does not arise in the “spectral” methods. It can be removed in the above method, but this seems to require some extra input, e.g. the finite-dimensionality of the space of functionals on an irreducible$\mathrm { S L _ { 2 } ( \mathbb { R } ) }$-representation that are invariant under the subgroup$\{ n ( t ) : t \in \mathbb { R } \}$

1.3.5. Two other viewpoints on the method of$\it 1 . 3 . 4$. There are two other viewpoints which might be helpful in thinking about Section 1.3.4. Both of these viewpoints do not literally generalize to the other situations we consider (e.g. triple products) but may be helpful for intuition.

(1) The first is based on the following simple principle: suppose that$T$is a measure-preserving transformation of the probability space$( Y , \nu )$, and that$T$is ergodic. If$\mu _ { 1 } , \mu _ { 2 }$are two T-invariant probability measures with average$\begin{array} { r } { \frac { \mu _ { 1 } + \mu _ { 2 } } { 2 } = \nu , } \end{array}$then$\mu _ { 1 } = \mu _ { 2 } = \nu ;$this follows because$\nu$is an extreme point of the convex set of T-invariant probability measures. More generally, given any family of probability measures averaging to$\nu ,$they must almost all equal$\nu .$.

We will apply this to$Y = \mathrm { S L _ { 2 } ( \mathbb { Z } ) \backslash S L _ { 2 } ( \mathbb { R } ) }$and$T$the operation of translation by$n ( 1 )$

Let n be large; for$t \in \mathbb { R } / \mathbb { Z }$, let$\mu _ { t }$be the probability measure that corresponds to normalized counting measure on$\{ x _ { n } n ( t + k ) : k \in \mathbb { Z } , 0 \leq$ $k < n \}$. Here notation is as prior to (1.7).

Then$\textstyle \int _ { 0 } ^ { 1 } \mu _ { t }$is the measure on the closed horocycle$\{ x _ { n } n ( t ) : 0 \leq t \leq$ $n \}$. Thus the family of measures$\mu _ { t }$averages to the measure on a long closed horocycle which, as we remarked earlier (see (1.10)) approximates the$\operatorname { S L _ { 2 } } ( \mathbb { R } )$-invariant measure$d g$on$\Gamma \backslash \mathrm { S L _ { 2 } } ( \mathbb { R } )$. But this latter measure$d g$ is ergodic w.r.t.$T .$. So applying a more quantitative form of the principle discussed above shows that, for almost all$t \in [ 0 , 1 ]$$\mu _ { t }$must be close to$d g$ 2 It is simple to see that one can use this to deduce bounds for the Fourier coeficients, via (1.7).

(2) We will phrase the second rather imprecisely. Consider (1.7). Our strategy of proof can be rephrased as:

The function$t \mapsto { \\bar { f } } ( x _ { n } n ( t ) )$is weak-mixing, whereas the function$t \mapsto$ $e ^ { 2 \pi i t }$is periodic, and a weak-mixing function cannot correlate with a periodic function.

To explain this statement, we need to explain what it means for a function on the real line to be weak-mixing. Consider instead the case of a function$h : \mathbb { Z } \to \mathbb { R }$. Furstenberg’s correspondence principle asserts that one can (loosely speaking) associate to this a dynamical system$( Y , \nu , T )$in such a way that (again loosely speaking) h arises by sampling a function on Y along a generic trajectory$y _ { 0 } , T ( y _ { 0 } ) , T ^ { 2 } ( y _ { 0 } ) , . . .$We then say that h is weak-mixing if the system$( Y , \nu , T )$is so. The fact that our function $t \mapsto \tilde { f } ( x _ { n } n ( t ) )$(say, when restricted to integer times) is weak-mixing follows from the equidistribution of long closed horocycles together with the fact that the horocycle flow is, itself, mixing.

For more on this point of view, see e.g. [36, Section 4] and [36, Lemma 5.2] for a version of the statement that weak-mixing functions cannot correlate with periodic ones.

1.4. Connection to existing methods. The following comments pertain to the results of the present paper that concern subconvex bounds for L-functions. As we have emphasized above, the methods presented here are, upon examination, seen to be closely related to existing methods: in particular, “Sarnak’s spectral method,”

which gave the only hitherto known instance of subconvexity over a base other than Q.

Indeed, as we have already indicated, the equidistribution step of our method can be seen as the geometric version of a mean value theorem, and the rest of the method can be seen as an amplification step (or “shortening the family.”) Nevertheless, the key features of the present method are that it is essentially geometric (in that it avoids Fourier coeficients) and adelic (which allows us to import much from the modern theory of automorphic forms); it also does not use families in any explicit way. Once the notation is established – admittedly a nontrivial overhead – the method allows for very considerable technical simplification.

It is perhaps also noteworthy that the method given here does not require any exponential decay information for triple products. Although such exponential decay information is central only to subconvexity in the eigenvalue aspect, it has thus far entered as a technical device even in treatments of the level aspect.

In a sense, the present method bears the same relation to existing methods as adelic methods do to classical methods in the theory of automorphic forms. The classical situation has the advantage of concreteness, and whatever can be carried out in the adelic setting can be (in principle) carried out in the classical setting. However there is often a considerable technical and conceptual advantage in working adelically.

As we have discussed, the connection between equidistribution results and meanvalue theorems for periods – implicitly exploited throughout this paper – appears in the work of V. Vatsal.

D. Hejhal considered ideas similar to that of Sec. 3.2 in the context of proving bounds towards Fourier coeficients; see [14]. In the language of this paper, his method used a measure σ (notation of Sec. 1.3) with much larger support, and consequently he was unable to get unconditional results.

Finally, as was remarked in Sec. 1.1, the main result of Sec. 4.1 is the analogue in the level aspect of a recent result of Bernstein-Reznikov [3]: they establish a “subconvex bound” on triple products as the eigenvalue of one factor varies. Their methods also are geometric, avoiding the use of Fourier coeficients.

1.5. Acknowledgements. This paper grew out of my proof of Thm. 3.1. The original proof was significantly more complicated, and I am indebted to Elon Lindenstrauss for his insistence that Thm. 3.1 should amount to nothing more than equidistribution and mixing. It was thus his intuition that led to a simplification of the proof and an important step in my understanding. The idea that the methods for Thm. 3.1 might be applicable in a more general setting arose during conversations with Andreas Str¨ombergsson, who also made many valuable suggestions about an early version of this paper. I thank them both for their significant contributions.

I am very grateful to Gergely Harcos and Philippe Michel for their encouragement of this project. Philippe read carefully an early draft of this paper and pointed out many points where the argument and results could be significantly improved. I am also grateful to Peter Sarnak, from whom I learned much of what I know about this subject.

I have also benefited from several conversations with Joseph Bernstein and Andr´e Reznikov. I thank for their generosity in sharing and discussing their elegant ideas.

I have learned many of the methods that appear here from the work of others. I mention in particular Peter Sarnak’s paper [29], which uses the idea of changing the test vector; the Friedlander-Iwaniec idea of amplification and the geometric version of it that appears in Bourgain-Lindenstrauss$[ 5 ] ;$and the recent work of Bernstein-Reznikov [1], in particular their elegant use of Sobolev norms.

This paper sufered a considerable delay before submission. I would like to thank Philippe Michel for his encouragement and insistence that it be revised and submitted, without which the delay would have likely been considerably longer. I also thank Nicolas Bergeron and Marina Ratner for comments that improved the exposition and correctness.

The ideas of this paper were worked out during the workshop “Emerging applications of measure rigidity,” AIM, San Francisco and at the Isaac Newton Institute.

I was supported by the Clay Mathematics Institute during much of the writing of the paper, and I thank them for their generous support. I also thank the Institute for Advanced Study for providing excellent working conditions during the academic year 2005-2006. I was also partially supported by NSF grants DMS-0111298 and DMS-0245606.

1.6. Structure of paper. The logical structure of this paper is as follows: Sec. 2 introduces all necessary notation. The heart of the paper are Sec. 3 (unipotent periods), Sec. 4 (the triple product period), Sections 6 and 7 (torus periods). The remaining Sections 8 – 11 are of a technical nature, proving various technical results required in the main text; at a first reading (or even later) they should perhaps be referred to only as necessary.

The two examples that best convey the flavor of the paper are Theorem 3.1 and Prop. 4.1. The proofs of these results are relatively self-contained, and we advise that the reader start with them.

## 2. Notation.

2.1. General notation. We use the symbol$\ll$as is standard in analytic number theory: namely,$A \ll B$means that there exists a constant c such that$A \leq c B$ The notation$A \ll _ { f , g , h } B$means that the constant c may depend on the quantities $f , g , h ;$the notation$A \ll _ { \epsilon } B$or$A \ll _ { \varepsilon } B$will mean, unless otherwise indicated, that the stated bound holds for all$\epsilon { \mathrm { ~ o r ~ } } \varepsilon > 0$. In general, we will never explicate the dependence of implicit constants on the number field over which we work; and, by an abuse of terminology, we will sometimes use the phrase “absolute constant” to mean a constant that depends only on this number field.

If Z is a space we denote by$\delta _ { z }$the point measure at$z \in Z$, i.e.$\delta _ { z } ( f ) = f ( z )$for $f$a continuous function on$Z$

Now let$Z$be a right G-space. For f a function on$Z$and$g \in G$, we write$g \cdot f$ for the right translate of$f$by$^ { g , }$i.e.$g \cdot f ( z ) = f ( z g )$. If$\mu$is a measure on$Z ,$, we define the translate$g \cdot \mu$by the rule$g \cdot \mu ( g \cdot f ) = \mu ( f )$. In particular, if$\mu = \delta _ { z }$is the point mass at$z \in Z$, then$g \cdot \mu = \delta _ { z g ^ { - 1 } }$is the point mass$\mathrm { a t } ~ z g ^ { - 1 }$

If σ is a compactly supported measure on$G ,$we set$f \star \sigma \ { \stackrel { \mathrm { d e f } } { = } } \ \int _ { g } ( g \cdot f ) d \sigma ( g )$ i.e.$\begin{array} { r } { f \star \sigma ( z ) = \int _ { a \in G } f ( z g ) d \sigma ( g ) } \end{array}$. In particular, if$\delta _ { g _ { 0 } }$is the point-mass at$g _ { 0 }$, then $f \star \delta _ { g _ { 0 } } = g _ { 0 } \cdot f$is the right translate of$f$by$g _ { 0 }$.

If$\sigma _ { 1 } , \sigma _ { 2 }$are two compactly supported measures on$G _ { \ l }$, we define the convolution $\sigma _ { 1 } { \star } \sigma _ { 2 }$to be the pushforward to G of$\sigma _ { 1 } \times \sigma _ { 2 }$on$G \times G$, under the multiplication map $( g _ { 1 } , g _ { 2 } ) \in G \times G \mapsto g _ { 1 } g _ { 2 }$. Notations as above, one has the (somewhat unfortunate) compatibility relation$\left( f \star \sigma _ { 2 } \right) \star \sigma _ { 1 } = f \star \left( \sigma _ { 1 } \star \sigma _ { 2 } \right)$

For σ a measure on a group G, we denote by ˇσ the image of σ by the involution $g \mapsto g ^ { - 1 }$, and by$\| \sigma \|$the total variation of$\sigma$

If G is a Lie group, we denote by$\operatorname { A d } ( g )$the endomorphism${ } ^ { 4 \cdot } X  g X g ^ { - 1 \cdots }$of its Lie algebra.

If$B \subset A$is a finite index subgroup of the group A, then we denote by$[ A : B ]$ the index of$B$in A.

If h is an entire function, the notation$\textstyle \int _ { \mathfrak { R } ( s ) = \sigma } h ( s ) d s$denotes the line integral along the line$\Re ( s ) = \sigma$from$\sigma - i \infty$to$\sigma + i \infty$. The notation$\int _ { \Re ( s ) \gg 1 } h ( s ) d s$denotes $\textstyle \int _ { \mathfrak { R } ( s ) = \sigma } h ( s ) d s$for suficiently large$\sigma ;$in the contexts where we use this notation, the answer will be constant when σ is suficiently large.

2.2. Classical modular forms. As usual H denotes the upper half plane, i.e. $\{ z \in \mathbb { C } : \operatorname { I m } ( z ) > 0 \}$. It admits the usual action of$\mathrm { S L } ( 2 , \mathbb { R } )$by fractional linear transformations.

2.3. Number fields and associated notations. Let F be a number field. Throughout the paper we shall regard F as fixed: that is to say, we allow implicit constants in$\ll , \gg$may depend on$F$without explicit statement.

We set$F _ { \infty } = F \otimes \mathbb { R } , \mathbb { A } _ { F }$the ring of adeles of$F , \mathbb { A } _ { F , f }$the ring of finite adeles. Thus$\mathbb { A } _ { F } = F _ { \infty } \times \mathbb { A } _ { F , f }$. We will fix once and for all an additive character$\mathit { e } _ { F } :$ $\mathbb { A } _ { F } / F \longrightarrow \mathbb { C }$, and denote by$e _ { F _ { v } }$the induced additive character of$F _ { v }$

For each place v we have a canonical “absolute value”${ \bf \Phi } _ { x \mapsto | x | _ { v } }$on$F _ { v } ^ { \times }$, namely, $| x | _ { v } = \mathrm { m e a s } ( x S ) / \mathrm { m e a s } ( S )$for any Haar measure, meas, on$F _ { v } ^ { \times }$, and any subset S of positive measure.

The same definition defines a character$\mathbb { A } _ { F } ^ { \times } / F ^ { \times } \to \mathbb { R } _ { > 0 }$, which we denote by $a \mapsto | a | _ { \mathbb { A } }$, or simply by$a \mapsto | a |$if it is clear from context. We denote by$\mathbb { A } _ { F } ^ { 1 }$ the subgroup of$\mathbb { A } _ { F } ^ { \times }$consisting of adeles of norm$1 ;$then the quotient$\mathbb { A } _ { F } ^ { 1 } / F ^ { \times }$is compact. For a finite place v of$F _ { ; }$, we denote by$\mathfrak { o } _ { F _ { v } }$the maximal compact subring of the completion$F _ { v }$, by$\mathfrak { q } _ { v }$the maximal ideal of$\mathfrak { o } _ { F _ { v } }$, and by$q _ { v }$the cardinality of the residue field.

We shall generally denote ideals of${ \mathfrak { o } } _ { F }$by gothic letters l, q, n, etc. If f is an integral ideal of${ \mathfrak { o } } _ { F }$, we set$\mathrm { N } ( \mathfrak { f } ) : = | \pmb { \mathfrak { o } } _ { F } / \mathfrak { f } |$to be its norm. Moreover, we shall denote $\begin{array} { r } { \mathfrak { o } _ { \mathfrak { f } } : = \prod _ { \mathfrak { q } | \mathfrak { f } } \mathfrak { o } _ { \mathfrak { q } } } \end{array}$. Here$\mathfrak { o } _ { \mathfrak { q } }$denotes the completed ring, not the localized${ \mathrm { r i n g } } ,$i.e.${ \mathfrak { o } } _ { \mathfrak { f } }$is the inverse limit of the rings${ \mathfrak { o } } _ { F } / { \mathfrak { f } } ^ { N }$

We denote by d the diferent of the character$e _ { F } .$, i.e. d is a fractional ideal so that$\mathfrak { d } _ { v } ^ { - 1 }$is, for every finite place v, the largest$\mathfrak { o } _ { F _ { \tau } }$-submodule of$F _ { v }$upon which $e _ { F }$is trivial.

2.4. Adele groups and their function spaces. Let G be a connected reductive algebraic group over a number field$F ,$and let Z be its center. Denote by$\mathbb { A } _ { F , f }$ the ring of finite adeles, and fix for each finite place v a maximal open compact subgroup$K _ { v , \mathbf { G } } \subset \mathbf { G } ( F _ { v } )$with the property that$\begin{array} { r } { K _ { \mathrm { m a x , G } } ~ { \large : } = ~ \prod _ { v \mathrm { f i n i t e } } K _ { v , \mathbf G } } \end{array}$is a maximal open compact subgroup of$\mathbf { G } ( \mathbb { A } _ { F , f } )$. Put$\mathbf { X _ { G } } = \mathbf { G } ( F ) \backslash \mathbf { G } ( \mathbb { A } _ { F } )$$\mathbf { X _ { G , a d } } =$ $\mathbf { Z } ( \mathbb { A } _ { F } ) \mathbf { G } ( F ) \backslash \mathbf { G } ( \mathbb { A } _ { F } )$. Then$\mathbf { X _ { G , \mathrm { a d } } }$has finite volume with respect to any$\mathbf { G } ( \mathbb { A } _ { F } )$ invariant measure.

Let$\omega : \mathbf { Z } ( \mathbb { A } _ { F } )  \mathbb { C } ^ { \times }$be a unitary character. We define the space$C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$to be the space of functions on$\mathbf { X _ { G } }$whose stabilizer in$K _ { \operatorname* { m a x } , \mathbf { G } }$has finite index, which transform under$\mathbf { Z } ( \mathbb { A } _ { F } )$by$\omega ,$and so that the function$g \mapsto f ( x g )$is a$C ^ { \infty }$function of$g \in { \bf G } ( F _ { \infty } )$, for each$x \in \mathbf { X _ { G } }$. Similarly one defines an L<sup>2</sup>-space$L _ { \omega } ^ { 2 } ( \mathbf { X } _ { \mathbf { G } } )$, or simply$L ^ { 2 }$if the central character ω is clear from context, by completing the space of compactly supported functions in$C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$with respect to the Hilbert norm $\begin{array} { r } { \| f \| _ { 2 } : = \left( \int _ { \mathbf { X _ { G , \mathrm { a d } } } } | f ( g ) | ^ { 2 } d g \right) ^ { 1 / 2 } } \end{array}$

For$\psi \in C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$, we denote by$K _ { v , \psi }$the stabilizer of$\psi$in$K _ { v , \mathbf { G } }$, and put

$$
K _ {\psi} = \prod_ {v \text {   finite }} K _ {v, \psi}.\tag{2.1}
$$

We note that$K _ { \psi }$is, in general, a proper subgroup of the stabilizer of ψ in$K _ { \operatorname* { m a x } , \mathbf { G } }$ For$\psi \in C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$, we define the finite set of places$\operatorname { S u p p } ( \psi )$to be those finite v for which$K _ { v , \mathbf { G } }$does not fix$\psi .$, i.e.

$$
\operatorname{Supp} (\psi) \stackrel {{\text { def }}} {{=}} \left\{v: K _ {v, \mathbf {G}} \neq K _ {v, \psi} \right\}.\tag{2.2}
$$

It is convenient to introduce some notions of$^ { 6 6 } \mathrm { s i z e } ^ { 9 }$on$\mathbf { G } ( \mathbb { A } _ { F } )$. Let g be the Lie algebra of$\mathbf { G } ( F _ { \infty } )$. It is a finite dimensional real vector space; fix an arbitrary norm on it. For$g _ { \infty } \in \mathbf { G } ( F _ { \infty } )$, we denote by$\| g _ { \infty } \|$the operator norm of the adjoint endomorphism$\operatorname { A d } ( g _ { \infty } ^ { - 1 } ) : { \mathfrak { g } } \to { \mathfrak { g } }$. If v is a finite place of$F$and$g _ { v } \ \in \mathbf { G } ( F _ { v } )$ we set$\| g _ { v } \| = [ K _ { v , \mathbf G } g _ { v } K _ { v , \mathbf G } : K _ { v , \mathbf G } ]$, i.e. the number of right-$K _ { v , \mathbf { G } }$cosets in $K _ { v , \mathbf G } g _ { v } K _ { v , \mathbf G }$. For$g _ { f } = ( g _ { v } )$v finite$\mathbf { \{ } \in G ( A  _ { F , f } )$we put$\begin{array} { r } { \| g _ { f } \| = \prod _ { v } \| g _ { v } \| } \end{array}$. Finally for $g _ { \mathbb { A } } = ( g _ { \infty } , g _ { f } ) \in { \bf G } ( F _ { \infty } ) \times { \bf G } ( \mathbb { A } _ { F , f } )$, set$\| g _ { \mathbb { A } } \| = \| g _ { \infty } \| \cdot \| g _ { f } \|$

We remark that$\| g _ { \infty } \| , \| g _ { f } \| , \| g _ { \mathbb { A } } \|$are all invariant by the center of G.

2.5. The groups$\mathbf { G } = \mathrm { G L } ( 2 )$and$\mathbf { G } = \mathrm { { P G L } } ( 2 )$and some of their subgroups. We will deal most often with the cases of$\mathbf { G } = \mathrm { G L } ( 2 )$(resp.${ \mathbf { G } } = \mathrm { P G L } ( 2 ) )$. In that setting we shall write$\mathbf { X } _ { \mathrm { G L ( 2 ) } } \ ( \mathrm { r e s p . ~ } \mathbf { X } )$for$\mathbf { X _ { G } }$

We will make use of the following algebraic subgroups of$\mathrm { G L _ { 2 } }$, which we will often also regard as algebraic subgroups of$\mathrm { P G L _ { 2 } }$in the obvious way:

$$
N = \left( \begin{array}{c c} 1 & * \\ 0 & 1 \end{array} \right), B = \left( \begin{array}{c c} * & * \\ 0 & * \end{array} \right), A = \left( \begin{array}{c c} * & 0 \\ 0 & * \end{array} \right), Z = \left( \begin{array}{c c} x & 0 \\ 0 & x \end{array} \right).
$$

If R is any ring and$x \in R , y \in R ^ { \times }$, we denote<sup>5</sup>

$$
\begin{array}{c} n (x) = \left( \begin{array}{c c} 1 & x \\ 0 & 1 \end{array} \right), \quad \overline {{n}} (x) = \left( \begin{array}{c c} 1 & 0 \\ x & 1 \end{array} \right), \quad a (y) = \left( \begin{array}{c c} y & 0 \\ 0 & 1 \end{array} \right), \\ a ^ {\prime} (y) = \left( \begin{array}{c c} 1 & 0 \\ 0 & y \end{array} \right), \quad z (y) = \left( \begin{array}{c c} y & 0 \\ 0 & y \end{array} \right), w = \left( \begin{array}{c c} 0 & 1 \\ - 1 & 0 \end{array} \right). \end{array}\tag{2.3}
$$

all elements of$\operatorname { G L _ { 2 } } ( R )$

If v is a place of F and$x \in F _ { v } , y \in F _ { v } ^ { \times }$, we denote by$n _ { v } ( x )$(resp.$a _ { v } ( x ) )$the element n(x) (resp. a(y)) considered as an element of${ \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$via the natural inclusion$\mathrm { G L } _ { 2 } ( F _ { v } ) \hookrightarrow \mathrm { G L } _ { 2 } ( \mathbb { A } _ { F } )$

For each place v, we let$K _ { \tau }$be the standard maximal compact subgroup of $\mathrm { G L _ { 2 } } ( F _ { v } )$, i.e.$K _ { v }$is the stabilizer of the norm on$F _ { v } ^ { 2 }$given by$\sqrt { | x | _ { v } ^ { 2 / \deg ( v ) } + | y | _ { v } ^ { 2 / \deg ( v ) } }$ if v is archimedean, where deg(v) is the degree<sup>6</sup> of$F _ { v }$over R; and max$( | x _ { v } | , | y _ { v } | )$if v is nonarchimedean. Thus, in particular,$K _ { v } = \mathrm { G L } _ { 2 } ( \mathfrak { o } _ { F , v } )$if v is nonarchimedean.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">a(y)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">GL<sub>2</sub>.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">|x|v,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>(In Section 3.1 alone, we will use slightly diferent notation for a(y) to accomodate the fact that we deal with SL rather than We make the relevant notation clear in that section.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">x ∈ Fv</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>6</sup>Recall that |x|<sub>v</sub>, for a complex place v and x ∈ F<sub>v</sub>, is the square of the usual absolute value on C!</span></small>

We put$\begin{array} { r } { K _ { \mathrm { m a x } } = \prod _ { v \mathrm { f i n i t e } } K _ { v } . \ K _ { v } } \end{array}$(respectively$K _ { \operatorname* { m a x } } )$is a maximal compact subgroup of$\mathrm { G L _ { 2 } } ( F _ { v } )$(respectively$\mathrm { G L _ { 2 } } \big ( \mathbb { A } _ { F , f } \big ) \big )$, and (by projection) can also be regarded as a maximal compact subgroup of$\mathrm { P G L } _ { 2 } ( F _ { v } )$(respectively$\mathrm { P G L _ { 2 } } ( \mathbb { A } _ { F , f } ) )$ Similarly$K _ { \operatorname* { m a x } } \times K _ { \infty }$is a maximal compact subgroup of${ \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$, and may also be regarded as a maximal compact subgroup of$\mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$

For q a finite prime of$F$, we denote by$\varpi _ { \mathfrak { q } } \in F _ { \mathfrak { q } }$a uniformizer, and by$\left[ \varpi _ { \mathfrak { q } } \right]$the element of$\mathbb { A } _ { F } ^ { \times }$that is the image of$\varpi _ { \mathfrak { q } }$under the natural inclusion$F _ { \mathfrak { q } } ^ { \times } \hookrightarrow \mathbb { A } _ { F } ^ { \times }$

Let q be a finite prime of F. It will be convenient to define certain open compact subgroups of$K _ { \mathfrak { q } }$. For each$e _ { \mathfrak { q } } > 0$, we define$K [ { \mathfrak { q } } ^ { e _ { q } } ] \subset K _ { \mathfrak { q } }$(resp.$K _ { 0 } [ \mathfrak { q } ^ { e _ { q } } ] \subset K _ { \mathfrak { q } } )$to be the be the kernel of$\mathrm { G L } _ { 2 } \big ( \mathfrak { o } _ { \mathfrak { q } } \big ) \longrightarrow \mathrm { G L } _ { 2 } \big ( \mathfrak { o } _ { \mathfrak { q } } \big / \varpi _ { \mathfrak { q } } ^ { m } \big )$(resp. the preimage, under this map, of the upper triangular matrices). Thus

$$
K _ {0} [ \mathfrak {q} ^ {e _ {\mathfrak {q}}} ] = \{\left( \begin{array}{c c} a & b \\ c & d \end{array} \right): a, b, d \in \mathfrak {o} _ {\mathfrak {q}}, c \in \mathfrak {q} ^ {e _ {\mathfrak {q}}}, a d - b c \in \mathfrak {o} _ {\mathfrak {q}} ^ {\times} \}.
$$

Now let f be a fractional ideal, not necessarily prime, of F. Factorize$\mathfrak { f } = \Pi _ { \mathfrak { q } } \mathfrak { q } ^ { e _ { \mathfrak { q } } }$ into prime ideals. We define elements$[ \mathfrak { f } ] \in \mathbb { A } _ { F } ^ { \times } , a ( [ \mathfrak { f } ] ) , n ( [ \mathfrak { f } ] ) \in \mathrm { G L } _ { 2 } ( \mathbb { A } _ { F } )$via:

$$
[ \mathfrak {f} ] = \prod_ {\mathfrak {q} | \mathfrak {f}} [ \varpi_ {\mathfrak {q}} ] ^ {- e _ {\mathfrak {q}}}, \quad n ([ \mathfrak {f} ]) := \prod_ {\mathfrak {q} | \mathfrak {f}} n _ {\mathfrak {q}} (\varpi_ {\mathfrak {q}} ^ {- e _ {\mathfrak {q}}}), \quad a ([ \mathfrak {f} ]) = \prod_ {\mathfrak {q} | \mathfrak {f}} a _ {\mathfrak {q}} (\varpi_ {\mathfrak {q}} ^ {- e _ {\mathfrak {q}}}).\tag{2.4}
$$

Suppose$\chi : \mathbb { A } _ { F } ^ { \times } / F ^ { \times } \to \mathbb { C } ^ { \times }$is a character. We define

$$
\chi (\mathfrak {f}) = \left\{ \begin{array}{l} 0, \chi \text { ramified   at   any   place   dividing } \mathfrak {f}, \\ \prod_ {\mathfrak {q} | \mathfrak {f}} \chi (\varpi_ {\mathfrak {q}}) ^ {e _ {\mathfrak {q}}}, \text { else }. \end{array} \right.
$$

2.6. Measures. The choice of measure is not especially important, as we are only interested in upper bounds; thus, so long as we are consistent, the precise selection does not matter. We choose a “standard” set of measures here; at times in the text, especially when carrying out equidistribution arguments, it will be more convenient to use probability measures, and we will indicate when this is the case.

We denote by$\mu \mathbf { x }$the$\mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$-invariant probability measure on X. We shall sometimes simply denote it by dx.

Let v be a finite place of$F$. Unless explicitly stated otherwise, the measures on${ \mathrm { G L } } _ { 2 } ( F _ { v } ) , { \mathrm { P G L } } _ { 2 } ( F _ { v } ) , F _ { v }$and$F _ { v } ^ { \times }$are the Haar measure which assigns$\mathrm { G L } _ { 2 } ( \mathfrak { o } _ { F _ { v } } )$ (resp.$\mathrm { P G L _ { 2 } } \big ( \mathfrak { o } _ { F _ { v } } \big ) , \ \mathfrak { o } _ { F _ { v } } , \ \mathfrak { o } _ { F _ { \tau } } ^ { \times } \big )$the total mass 1.

For v archimedean, endow$F _ { v }$with a multiple of Lebesgue measure$c _ { v } d x$, where the constants$c _ { v }$are fixed arbitrarily in such a way that the induced product measure on$F _ { \infty }$satisfies vo${ \left( F _ { \infty } / 0 _ { F } \right) = 1 }$; equivalently, the product measure on$\mathbb { A } _ { F }$satisfies $\mathrm { v o l } ( \mathbb { A } _ { F } / F ) = 1$. In particular, this product measure on$\mathbb { A } _ { F }$is self-dual with respect to e<sub>F</sub>. We endow$F _ { v } ^ { \times }$with the measure$\begin{array} { r } { d ^ { \times } x = \frac { d x } { | x | _ { v } } } \end{array}$, where dx is Lebesgue measure.

These choices induce a Haar measure on$N ( \dot { F _ { v } } )$, by means of the identification $x \mapsto n ( x )$; similarly, the identifications$( y , y ^ { \prime } ) \mapsto a ( y ) a ^ { \prime } ( y ^ { \prime } )$and$y \mapsto z ( y )$induce Haar measures on$A ( F _ { v } )$and$Z ( F _ { v } )$. Equip$K _ { v }$with the measure of mass 1, and give ${ \mathrm { G L } } _ { 2 } ( F _ { v } )$the measure arising from the Iwasawa decomposition$N ( F _ { v } ) \times A ( F _ { v } ) \times K _ { v }$ Equip$\mathrm { P G L _ { 2 } } ( F _ { v } ) = \mathrm { G L _ { 2 } } ( F _ { v } ) / Z ( F _ { v } )$with the “quotient” measure.

We then take the measures on$\mathrm { G L } _ { 2 } ( \mathbb { A } _ { F } ) , \mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } ) , \mathbb { A } _ { F } , \mathbb { A } _ { F } ^ { \times }$to be the corresponding product measures.

The measure on any discrete group$( \mathrm { e . g . \ P G L _ { 2 } } ( F )$, considered as a subgroup of ${ \mathrm { P G L } } _ { 2 } { \left( \mathbb { A } _ { F } \right) } \rangle$will be counting measure.

Usually (indeed, unless otherwise specified) we shall use the$\mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$-invariant probability measure on$\mathbf { X } = \mathrm { P G L } _ { 2 } ( F ) \backslash \mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$. This does not coincide with the quotient measure induced from$\mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$, but they difer by some constant depending only on$F .$. On the few occasions we shall have occasion to use the latter measure, we will indicate this.

2.7. Projection onto locally constant functions. For equidistribution questions it is usually convenient to deal with the constant function and its orthogonal complement separately. Some minor complications arise in our case since the ambient spaces are not connected. In fact: The space$C ^ { \infty } ( \mathbf { X _ { G } } )$is a direct limit of function spaces$C ^ { \infty } ( \mathbf { X _ { G } } / K )$where$K \subset K _ { \operatorname* { m a x } , \mathbf { G } }$has finite index. Unless G is simply connected, the manifolds$\mathbf { X _ { G } } / K$need not be connected.

Of course, to deal with this, one can (if G is semisimple) simply replaces the notion of constant function by locally constant function. However, in the general case of G reductive, matters are slightly complicated by the necessity of dealing with central characters.

Since we will only use this definition when G is a product of$\mathrm { G L } ( 2 ) \mathrm { s }$, we restrict ourselves to that setting. First suppose that$\mathbf { G } = \mathrm { G L } ( 2 )$. We define a projection $\mathscr { P } : C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathrm { G L } ( 2 ) } ) \to C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathrm { G L } ( 2 ) } )$via

$$
\mathcal {P} f (x) = \int_ {h \in S L _ {2} (F) \backslash \mathrm{SL} _ {2} (\mathbb {A} _ {F})} f (h x) d h = \sum_ {\chi^ {2} = \omega} \chi (x) \int_ {\mathbf {X}} f (y) \overline {{\chi (y)}} d y,\tag{2.5}
$$

where$d h$is the$\mathrm { S L } _ { 2 } ( \mathbb { A } _ { F } )$-invariant probability measure,$d y$the${ \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$-invariant probability measure on X, χ ranges over characters of$\mathbb { A } _ { F } ^ { \times } / F ^ { \times }$with square$\omega , \chi ( y )$ the function on$\mathbf { X } _ { \mathrm { G L } ( 2 ) }$defined by$g \mapsto \chi ( \operatorname* { d e t } ( g ) )$, and the second equality is easily verified. We note, in particular, that the$\chi$sum is finite$( \mathrm { a n y ~ } \chi$for which the corresponding term is nonvanishing must be unramified outside Supp(f)).

Then$\| \mathcal { P } f \| _ { L ^ { \infty } } \leq \| f \| _ { L ^ { \infty } }$, as is clear from the first equality of (2.5), and$\mathcal { P }$is a self-adjoint projection w.r.t.$L ^ { 2 }$, as is clear from the second equality. We say a function f is totally nondegenerate if$\mathcal { P } f = 0$

If$\mathbf { G } = \mathrm { G L } ( 2 ) \times \mathrm { G L } ( 2 )$, and$\omega = ( \omega _ { 1 } , \omega _ { 2 } )$is a character of the center$\mathbf { Z } ( \mathbb { A } _ { F } ) =$ $\mathbb { A } _ { F } ^ { \times } \times \mathbb { A } _ { F } ^ { \times }$, we denote by$\mathcal { P } _ { 1 }$the operator on$C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$given by

$$
\mathscr {P} _ {1} f (x _ {1}, x _ {2}) = \int_ {h \in S L _ {2} (F) \backslash \mathrm{SL} _ {2} (\mathbb {A} _ {F})} f (h x _ {1}, x _ {2}) d h = \sum_ {\chi^ {2} = \omega_ {1}} \chi (x _ {1}) \int_ {\mathbf {X}} f (y, x _ {2}) \overline {{\chi (y)}} d y.
$$

We define$\mathcal { P } _ { 2 }$similarly, interchanging the role of the first and second coordinate. The operators$\mathcal { P } _ { j }$for$j = 1 , 2$commute, satisfy$\| \mathcal { P } _ { j } f \| _ { L ^ { \infty } } \leq \| f \| _ { L ^ { \infty } }$and are commuting self-adjoint projections on$L ^ { 2 }$. We say that a function f is totally nondegenerate if$\mathcal { P } _ { 1 } f = \mathcal { P } _ { 2 } f = 0$

Lemma 2.1. Let v be a place of F. The projection$\mathcal { P }$acts by the identity on the subspace$W \subset L _ { \omega } ^ { 2 } ( \mathbf { X _ { G } } )$spanned by one-dimensional representations of${ \mathrm { G L } } _ { 2 } ( F _ { v } )$ occurring in$L _ { \omega } ^ { 2 } ( \mathbf { X } _ { \mathbf { G } } )$

Similarly,$\mathcal { P } _ { 1 } \left( r e s p . \quad \mathcal { P } _ { 2 } \right)$acts by the identity on the space$W _ { 1 } \quad ( r e s p . \quad W _ { 2 } )$ spanned by one-dimensional representations of${ \mathrm { G L } } _ { 2 } ( F _ { v } )$occurring in$L ^ { 2 } ( \mathbf { X } \times \mathbf { X } )$ for the action on the first (resp. second) factor.

Proof. This follows from the spectral decomposition for${ \mathrm { G L } } ( 2 )$. For instance, it is known that the space$W$is precisely the span of functions of the form$g \mapsto \chi ( \operatorname* { d e t } ( g ) )$, where$\chi$ranges over characters of$\mathbb { A } _ { F } ^ { \times } / F ^ { \times }$satisfying$\chi ^ { 2 } = \omega$

2.8. Hecke operators and bounds towards the Ramanujan conjecture. Let l be a prime ideal of$\mathfrak { o } _ { F }$and r an integer$\geq 1$. Let$F _ { \mathrm { I } }$be the completion of F at the prime l. Take the Haar measure on$\mathrm { G L _ { 2 } } ( F _ { \mathrm { [ } } )$so that it assigns mass 1 to$\mathrm { G L } _ { 2 } ( \mathfrak { o } _ { F _ { \mathrm { l } } } )$ Define the measure$\mu _ { { \scriptscriptstyle [ r } } ^ { * }$on$\mathrm { G L _ { 2 } } ( F _ { \mathrm { l } } )$to the restriction of Haar measure to the set $\mathrm { G L } _ { 2 } \big ( \mathfrak { o } _ { F _ { \mathrm { l } } } \big ) \cdot \left( \begin{array} { c c } { \varpi _ { l } ^ { r } } & { 0 } \\ { 0 } & { 1 } \end{array} \right) \mathrm { G L } _ { 2 } \big ( \mathfrak { o } _ { F _ { \mathrm { l } } } \big )$, so that the total mass of$\mu _ { { \scriptscriptstyle [ r } } ^ { * }$<sub>r</sub> is$\mathrm { N } ( \mathfrak { l } ) ^ { r - 1 } ( \mathrm { N } ( \mathfrak { l } ) + 1 )$. Moreover, set

$$
\mu_ {l ^ {r}} = \frac {1}{\mathrm{N} (l) ^ {r / 2}} \sum_ {k \leq \frac {r}{2}} \mu_ {r - 2 k} ^ {*}, \overline {{\mu}} _ {l ^ {r}} := \frac {\mu_ {l ^ {r}}}{\| \mu_ {l ^ {r}} \|},\tag{2.6}
$$

where$\| \cdot \|$denotes total variation. Thus$\overline { { \mu } } _ { l } ,$is a probability measure. Via the natural inclusion of$\mathrm { G L _ { 2 } } ( F _ { \mathrm { l } } )$in$\mathrm { G L _ { 2 } } ( \mathbb { A } _ { F , f } )$, we may regard$\mu _ { \ell ^ { r } }$as a compactly supported measure on$\mathrm { G L _ { 2 } } ( \mathbb { A } _ { F , f } ) ;$; by abuse of notation, we will not introduce a diferent symbol for this measure. If n is an integral ideal of${ \mathfrak { o } } _ { F }$, factorize$\begin{array} { r } { \mathfrak { n } = \prod _ { i } \mathfrak { l } _ { i } ^ { r _ { i } } } \end{array}$ and put$\mu _ { \mathfrak { n } } = \prod \mu _ { \mathfrak { l } _ { i } ^ { r _ { i } } } , \overline { { \mu } } _ { \mathfrak { n } } = \prod \overline { { \mu } } _ { \mathfrak { l } _ { i } ^ { r _ { i } } }$. Here is taken to mean convolution of measures on$\mathrm { G L _ { 2 } } ( \mathbb { A } _ { F , f } )$

Convolution by$\mu _ { \mathfrak { n } }$on$L ^ { 2 } ( \mathbf { X } )$corresponds to the nth Hecke operator; in this normalization the Ramanujan conjecture corresponds to it having eigenvalues$\leq 2$ in absolute value.

The adelic measures$\mu _ { \mathfrak { n } }$satisfy the usual multiplication laws, appropriately interpreted: if n and m are ideals, then

$$
\int_ {\mathrm{PGL} _ {2} (\mathbb {A} _ {F})} h (x) d \left(\mu_ {\mathfrak {n}} \star \mu_ {\mathfrak {m}}\right) (x) = \sum_ {\mathfrak {d} | (\mathfrak {m}, \mathfrak {n})} \int_ {\mathrm{PGL} _ {2} (\mathbb {A} _ {F})} h (x) d \mu_ {\mathfrak {n m d} ^ {- 2}} (x),\tag{2.7}
$$

whenever h is a function on$\mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$that is invariant under$\mathrm { P G L } _ { 2 } ( \mathfrak { o } _ { v } )$for all <sup>v</sup>|<sup>nm.</sup>

Definition 2.1. Set α be a bound towards Ramanujan for$\mathrm { G L _ { 2 } }$over$F ,$i.e. α is so that$\mu _ { l }$acts on any$\mathrm { P G L _ { 2 } } ( \mathfrak { o } _ { F _ { l } } )$)-invariant cuspidal eigenfunction by an eigenvalue $\leq \mathrm { N } ( l ) ^ { \alpha } + \mathrm { N } ( l ) ^ { - \alpha }$in absolute value.

Thus$\alpha = 0$corresponds to the Ramanujan conjecture,$\alpha = 1 / 2$the trivial bound. $\mathrm { B y }$work of Kim and Kim-Shahidi, we can take$\alpha = 3 / 2 6$. For our applications, any value of α less than$1 / 4$would sufice.

Note that we shall slightly vary this notation (but in a reasonably compatiable way) in Section 3.1 and Section 9.3.1. In those parts, we shall deal with a (not necessarily arithmetic) quotient$\Gamma \backslash \mathrm { S L _ { 2 } } ( \mathbb { R } )$, and α will denote a number so that $L ^ { 2 } ( \Gamma \backslash \mathrm { S L _ { 2 } } ( \mathbb { R } ) )$) does not contain any complementary series with parameter$\geq \alpha$ (Here the complementary series is understood to be parameterized by$\left( 0 , 1 / 2 \right) )$. This is compatible with the above notation, however; e.g. if Γ were a congruence subgroup,$\alpha = 3 / 2 6$would again be admissible.

## 2.9. Sobolev-type norms on real and adelic quotients.

2.9.1. General comments. Let M be a real manifold. Recall that the Sobolev norm on$C ^ { \infty } ( M )$controls, roughly speaking, the$L ^ { p }$norm of a function together with the$L ^ { p }$norms of certain derivatives. These norms will be tremendously useful throughout the paper to control equidistribution rates. We shall use both the relatively simple definition when$M = \Gamma \backslash G$and an adelic variant.

First let us remark on the use of L<sup>p</sup>-Sobolev norms for$p > 2$. This is solely to do with noncompactness. If we were to deal only with compact quotients, then the$L ^ { 2 } .$-Sobolev theory would always sufice. However, in the noncompact case, the $L ^ { 2 } .$-Sobolev norms do not$\left( \mathrm { e . g . } \right)$give good bounds on the size of a function high in a cusp. There are, of course, various ways to rectify this; for example we could include weights that measure the height into the cusp. We have chosen instead to use$L ^ { p _ { - } }$ norms with$p > 2$, which is technically very simple, but has some disadvantages (e.g. it does not induce a Hilbert space structure).

Note that we will allow our seminorms and norms to take the value . Thus a seminorm on a complex vector space V will be a function from V to$\textstyle \mathbb { R } _ { \geq 0 } \cup \{ \infty \}$ satisfying

(1)$\| \lambda v \| = | \lambda | \| v \|$, for any$v \in V$such that$\left\| v \right\| < \infty ;$

(2)$\| v _ { 1 } + v _ { 2 } \| \leq \| v _ { 1 } \| + \| v _ { 2 } \|$if both$\| v _ { 1 } \|$and$\| v _ { 2 } \|$are not infinite.

It is a norm if additionally$\| v \| = 0$implies$v ~ = ~ 0$. Note that giving such a seminorm on V is equivalent to giving a subspace$V _ { f } \subset V$together with a finitevalued seminorm on$V _ { f }$. Indeed take$V _ { f } = \{ v \in V : \| v \| < \infty \}$, equipped with the restriction of$\| \cdot \|$

We remark that we do not require that our norms be complete.

2.9.2. Non-adelic setting. Suppose$\Gamma \subset G$is a lattice in a connected semisimple Lie group. Fix for all time a basis for the Lie algebra g of G and a norm$\| \cdot \|$on g. For$g \in G$, we denote by g the operator norm of$\operatorname { A d } ( g ^ { - 1 } ) : { \mathfrak { g } } \to { \mathfrak { g } } .$, i.e. the map $X \mapsto g ^ { - 1 } X g$

For$f \in C ^ { \infty } ( \Gamma \backslash G )$, and$1 \leq p \leq \infty$, we put

$$
S _ {p, d} = \sum_ {\operatorname{ord} (\mathcal {D}) \leq d} \| \mathcal {D} f (g) \| _ {L ^ {p} (\Gamma \backslash G)}.\tag{2.8}
$$

Here$\mathcal { D }$ranges over all monomials in  of order$\leq d ,$and$\mathcal { D }$acts on f by right diferentiation. (For example,$X \in { \mathfrak { g } }$acts on$f$via$\begin{array} { r } { X f ( g ) = \frac { d } { d t } f ( g e ^ { t X } ) . ) } \end{array}$

Changing only distorts$S _ { p , d }$by a bounded factor. (That is to say, if$S _ { p , d } ^ { \prime }$is the norm obtained by replacing by another basis, then there are positive reals$c _ { 1 } , c _ { 2 }$ possibly depending on$d ,$such that$c _ { 1 } S _ { p , d } \leq S _ { p , d } ^ { \prime } \leq c _ { 2 } S _ { p , d } . \ )$

We will often use the following simple remark: Fix a Riemannian metric$d ( \cdot , \cdot )$ on$G$and suppose$g ~ \in ~ G$belongs to some fixed compact set. Then, for$f \in$ $C ^ { \infty } ( \Gamma \backslash G ) , x \in \Gamma \backslash G .$, we have$| f ( \bar { x } g ) - f ( x ) | \ll S _ { \infty , 1 } ( \bar { f } ) d ( g , 1 )$. Indeed, we may assume that$g$is close to the identity and write$g = \exp ( X )$, with$X \in { \mathfrak { g } } ;$; now apply the mean value theorem to$t \mapsto f ( x e ^ { t X } )$

Moreover, the following elementary properties are easily verified (we only need them in the case$p = \infty )$

Lemma 2.2. Let$f _ { 1 } , f _ { 2 } \in C ^ { \infty } ( \Gamma \backslash G )$and$g \in G$. Then

$$
\begin{array}{c} S _ {\infty , d} (f _ {1} f _ {2}) \ll_ {d} S _ {\infty , d} (f _ {1}) S _ {\infty , d} (f _ {2}) \\ S _ {\infty , d} (g \cdot f _ {1}) \ll_ {d} \| g \| ^ {d} S _ {\infty , d} (f _ {1}) \end{array}\tag{2.9}
$$

We remark that, in the case$p = 2$, the rule (2.8) also defines a system of Sobolev norms on any unitary G-representation; the case discussed above corresponds to the unitary representation$L ^ { 2 } ( \Gamma \backslash G )$).

2.9.3. Adelic Sobolev norms. Let’s first describe what the point is intended to be (evidently there are many ways of implementing it, cf. Rem. 2.1). We would like to put a norm on the adelic function space, suitable for controlling e.g. period integrals. Consider$C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$in the case of$\mathbf { G } = \mathrm { S L _ { 2 } } , F = \mathbb { Q } , \omega = 1$as a direct limit of spaces$C ^ { \infty } ( \Gamma _ { i } \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } ) )$, where$\Gamma _ { i }$ranges over some class of congruence subgroups of$\Gamma _ { 0 } : = \mathrm { S L } _ { 2 } ( \mathbb { Z } )$We equip each quotient$\Gamma _ { i } \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } )$with the$\operatorname { S L } _ { 2 } ( \mathbb { R } )$invariant probability measure. Then, on each space$C ^ { \infty } ( \Gamma _ { i } \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } ) )$) we have the norm$S _ { p , d }$ defined in the previous section. On the other hand, typical bounds on automorphic forms have an implicit dependence on the “level”, i.e. the index$[ \Gamma : \Gamma _ { i } ]$, so one would like to have a norm that increases with the level. The most naive candidate is, fixing a real number$\beta > 0$, to define the “norm” of$f \in C ^ { \infty } ( \Gamma _ { i } \backslash \mathrm { { S L } _ { 2 } } ( \mathbb { R } ) )$) to be $[ \Gamma : \Gamma _ { i } ] ^ { \beta } S _ { p , d } ( f )$. This unfortunately does not quite make sense when we pass to the direct limit: however, we can “force it to make sense” by considering the maximal norm on the direct limit whose restriction to each$C ^ { \infty } ( \Gamma _ { i } \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } ) )$) is bounded above by$[ \Gamma : \Gamma _ { i } ] ^ { \beta } S _ { p , d } ( f )$. This will sufice for our purposes.

Let us formalize these ideas. In what follows we return to the setting of G a reductive group over F. The adelic Sobolev norms will be a family of norms on$C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$indexed by a triple$( p , d , \beta )$. The d and$\beta$indicate, approximately speaking, how stringently one should “penalize” rapid variation at the infinite and finite places respectively.

Let$p \ge 1 , k \in \mathbb { N } , \beta \ge 0$. Fix a basis$\boldsymbol { B } = \{ \boldsymbol { X } _ { i } \}$for the real Lie group$\operatorname { L i e } ( \mathbf { G } ( F _ { \infty } ) )$ Recalling the definition of$K _ { \psi }$from (2.1), we define the pre-Sobolev functions $P S _ { p , d , \beta }$on$C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$via:

$$
\begin{array}{l} P S _ {p, d, \beta} (\psi) = [ K _ {\max, \mathbf {G}}: K _ {\psi} ] ^ {\beta} \sum_ {\operatorname{ord} (\mathcal {D}) \leq d} \| \mathcal {D} \psi \| _ {L ^ {p} (\mathbf {X} _ {\mathbf {G}, \mathrm{ad}})} \\ \qquad = \prod_ {v \text {   finite }} [ K _ {v, \mathbf {G}}: K _ {v, \psi} ] ^ {\beta} \sum_ {\operatorname{ord} (\mathcal {D}) \leq d} \| \mathcal {D} \psi \| _ {L ^ {p} (\mathbf {X} _ {\mathbf {G}, \mathrm{ad}})}, \end{array}\tag{2.10}
$$

where the sum ranges over  that are monomials in  of order$\leq d .$

The function$P S _ { p , d , \beta }$does not satisfy the triangle inequality. We define the $( p , d , \beta )$-Sobolev norm$S _ { p , d , \beta }$to be the maximal seminorm on$C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$satisfying $S _ { p , d , \beta } ( \psi ) \leq P S _ { p , d , \beta } ( \psi )$. Explicitly,

$$
S _ {p, d, \beta} (\psi) = \inf \left\{\sum_ {i = 1} ^ {n} P S _ {p, d, \beta} \left(\psi_ {j}\right): \sum_ {i = 1} ^ {n} \psi_ {j} = \psi , \psi_ {j} \in C _ {\omega} ^ {\infty} \left(\mathbf {X} _ {\mathbf {G}}\right). \right\}\tag{2.11}
$$

In fact, it is clear that the right-hand side of (2.11) defines a seminorm that is dominated by$P S _ { p , d , \beta }$(take the collection$\{ \psi _ { i } \}$to consist of ψ alone); moreover, it is evidently maximal in the class of such seminorms. Finally, as$P S _ { p , d , \beta } ( \psi ) \geq$ $\| \psi \| _ { L ^ { p } }$, the$S _ { p , d , \beta }$are in fact norms on$C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$

It will often be useful to omit the argument β and set it to a “default” value of $1 / p$. We therefore define$S _ { p , d } : = S _ { p , d , 1 / p } ,$, for$p \neq 0 ,$, and$S _ { \infty , d } : = S _ { \infty , d , 0 }$

Notational convention: We will very often have cause to bound linear functionals$L$on$C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$by Sobolev norms. In writing statements of the form $| L ( f ) | \ll S _ { p , d , \beta } ( f )$, we will always allow the implicit constant to depend on$p ,$d and$\beta$without explicitly saying so.

2.10. Adelic Sobolev norms – a slight generalization. The notations of this section will only be required in Sec. 7. We recommend it be omitted at a first reading.

In the discussion at the start of Sec. 2.9.3, we did not address what class of subgroups$\Gamma _ { i }$to consider (should we take all finite index subgroups of a fixed$\Gamma _ { 0 }$or some subclass?) Implicitly, such a choice was made in defining the Sobolev norms of the previous section. The Sobolev norms introduced in the previous section are good for most of our purposes. However, roughly speaking, they have the following defect: they only measure the index of a stabilizer of a function$f \in C _ { \omega } ^ { \infty } ( \mathbf { X _ { G } } )$.

That this definition might lead to some peculiar results can be already seen in the case$\mathbf { G } = \mathrm { P G L } ( 2 ) , F = \mathbb { Q }$. Let$\chi _ { p }$be the character of$\mathbb { A } _ { \mathbb { Q } } ^ { \times } / \mathbb { Q } ^ { \times }$that corresponds to the quadratic Dirichlet character of$\mathbb { Q }$with conductor$p ,$a prime number. Then the function$g \mapsto \chi _ { p } ( \operatorname* { d e t } ( g ) )$descends to a function$f$on$\mathbf { X } ,$, and it is easy to check that$[ K _ { \operatorname* { m a x } } : K _ { f } ] = \bar { 2 }$, for any$p .$Thus the index of this stabilizer does not reflect the conductor of the underlying representation (which, by any reasonable definition of conductor, should grow as p increases). In this section we shall introduce a slight modification of the definitions which avoids this problem. (This problem would not occur for${ \mathrm { S L } } ( 2 ) ,$).

This is a purely technical matter, and it seems there is much scope for giving better and more natural definitions. We restrict ourselves to the case$\mathbf { G } = { \mathrm { G L } } ( n )$. For a finite place q and$m \geq 0$, we put$K [ \mathfrak { q } ^ { m } ] \ { \stackrel { \mathrm { d e f } } { = } } \ \ker ( \operatorname { G L } ( n , \mathfrak { o } _ { \mathfrak { q } } ) \longrightarrow \operatorname { G L } ( n , \mathfrak { o } _ { \mathfrak { q } } / \varpi _ { \mathfrak { q } } ^ { m } \mathfrak { o } _ { F _ { \mathfrak { q } } } )$ where$\varpi _ { \mathfrak { q } }$is a uniformizer in$F _ { \mathfrak { q } }$. Now, for ψ$\in C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$, put$K _ { \mathfrak { q } , \psi } ^ { * }$to be the largest subgroup$K [ \mathfrak { q } ^ { m } ]$which stabilizes$\psi _ { ; }$and put$\begin{array} { r } { K _ { \psi } ^ { * } = \prod _ { \mathfrak { q } } K _ { \mathfrak { q } , \psi } ^ { * } , } \end{array}$

We define the ⋆-pre-Sobolev norm$P S _ { p , d , \beta } ^ { * }$by the rule

$$
P S _ {p, d, \beta} ^ {\star} (\psi) = [ K _ {\max, \mathbf {G}}: K _ {\psi} ^ {*} ] ^ {\beta} \sum_ {\operatorname{ord} (\mathcal {D}) \leq d} \| \mathcal {D} \psi \| _ {L ^ {p} (\mathbf {X} _ {\mathbf {G}, \mathrm{ad}})}
$$

and we define the ⋆-Sobolev norm$S _ { p , d , \beta } ^ { * }$to be the maximal seminorm dominated by$P S _ { p , d , \beta } ^ { * } .$Clearly$S _ { p , d , \beta } ^ { * } \geq S _ { p , d , \beta }$

The eventual purpose of this is that$S _ { p , d , \beta } ^ { * }$(unlike$S _ { p , d , \beta } )$will never be “too small” on an automorphic representation whose conductor is large. This can be quantified, although we do not do so in the present document.

Remark 2.1. Evidently the definitions of this section and the previous are not the only “sensible” way of defining a notion of adelic Sobolev norms. The results of this paper do not require any more sophisticated definition, although this would certainly be of help in optimizing the results.

However, it would be interesting to impose a system of Sobolev-type norms in a less ad hoc fashion. Moreover, it would be pleasant if the system of norms had nice interpolation properties (this often is very helpful for getting sharp results). For example it would be nice if as one varied$\beta$one got a family of interpolation spaces.

We remark on a simple way of defining Hilbertian norms which seems (more) appropriate to the adelic context. Let$\bar { K } [ \mathfrak { q } ^ { m } ]$be as above, and let$E _ { \mathfrak { q } ^ { m } }$be the averaging projection onto the$K [ \mathfrak { q } ^ { m } ]$-fixed vectors, i.e.$\begin{array} { r } { E _ { \mathfrak { q } ^ { m } } ( v ) = \int _ { k \in K [ \mathfrak { q } ^ { m } ] } k \cdot v d k } \end{array}$, where the measure is the Haar probability measure. Then$e _ { \mathbf q ^ { m } } : = E _ { \mathbf q ^ { m } } - E _ { \mathbf q ^ { m - 1 } }$is a projection. If$\textstyle { \mathfrak { f } } = \prod _ { i } { \mathfrak { q } } _ { i } ^ { m _ { i } }$is an arbitrary integral ideal, put$\begin{array} { r } { e _ { \mathfrak { f } } : = \prod _ { i } e _ { \mathfrak { q } _ { i } ^ { m _ { i } } } } \end{array}$. Now put $\begin{array} { r } { P ( s ) = \sum _ { \mathfrak { f } } e _ { \mathfrak { f } } \mathrm { N } ( \mathfrak { f } ) ^ { s } } \end{array}$. Then$\begin{array} { r } { f \mapsto \sum _ { \mathrm { o r d } ( \mathcal { D } ) \leq d } \| \mathcal { D } \cdot P ( s ) \cdot f \| _ { L ^ { 2 } } } \end{array}$defines a Hilbert norm which seems to have reasonably pleasant formal properties. In fact it is majorized (up to constants) by a norm of the type described above,.

J. Bernstein has a more canonical notion of norms on representation spaces of p-adic groups, and he has informed me that these norms have adelic analogues. I do not know the relation. The norms arising from his constructions are Hilbertian.

2.11. Some properties and uses of the Sobolev norms. We briefly summarize certain results that will be used in the text. Detailed proofs are given in Sec. 8.

For general$\mathbf { G } , \omega$we have:

(2.12)

$$
S _ {p, d, \beta} (F _ {1} F _ {2}) \ll_ {d} S _ {2 p, d, \beta} (F _ {1}) S _ {2 p, d, \beta} (F _ {2}).\tag{2.13}
$$

$$
S _ {p, d, \beta} (g \cdot F) \ll \| g _ {\infty} \| ^ {d} \| g _ {f} \| ^ {\beta} S _ {p, d, \beta} (F).
$$

(2.12), proved in Lem. 8.1, and (2.13), proved in Lem.$8 . 2 ,$give some basic stability properties of Sobolev norms.

Now we specialize to some results for${ \mathrm { G L } } ( 2 )$and PGL(2). Let$F \in C ^ { \infty } ( \mathbf { X } \times \mathbf { X } )$ let q be a prime ideal of$\mathfrak { o } _ { F } .$, and suppose$F$is invariant by$\mathrm { P G L _ { 2 } } \big ( \mathfrak { o } _ { F _ { q } } \big ) \times \mathrm { P G L _ { 2 } } \big ( \mathfrak { o } _ { F _ { q } } \big )$ Then:

$$
\left| \int_ {\mathbf {X}} F (x, x a ([ \mathfrak {q} ])) d x - \sum_ {\chi^ {2} = 1} \chi ([ \mathfrak {q} ]) \int_ {\mathbf {X}} F (x, y) \chi (x) \chi (y) d \mu_ {\mathbf {X}} (x) d \mu_ {\mathbf {X}} (y) \right|\tag{2.14}
$$

$$
\ll_ {\epsilon} \mathrm{N} (\mathfrak {q}) ^ {\frac {2 \alpha - 1}{p} + \epsilon} S _ {p, d} (F).
$$

(2.14), proved in Lem. 9.8, quantifies Hecke equidistribution. To understand the relation, take$F$to be a pure tensor:$F ( x , y ) = f _ { 1 } ( x ) f _ { 2 } ( y )$. Then (2.14) in efect bounds the inner product$\langle T _ { \mathfrak { q } } f _ { 1 } , f _ { 2 } \rangle$, where$T _ { \mathfrak { q } }$is the Hecke operator corresponding to q.

2.12. Cusp forms, L-functions and the analytic conductor. As a general remark on notation – and a mild abuse of notation– by cuspidal representation we shall always mean unitary cuspidal representation. This is automatic for PGL(2) but not for GL(2).

2.12.1. L-functions. Let$\pi = \otimes _ { v } \pi _ { v }$be an automorphic cuspidal representation of ${ \mathrm { G L } } ( n )$over F. We denote by$L _ { v } ( s , \pi _ { v } )$the local L-factor of the representation$\pi _ { v }$ when it causes no confusion, we will sometimes abbreviate this to$L ( s , \pi _ { v } )$

We write$\begin{array} { r } { L ( s , \pi ) : = \prod _ { v \mathrm { f i n i t e } } L _ { v } ( s , \pi _ { v } ) } \end{array}$for the (finite part of) the global L-function attached to π, and$\begin{array} { r } { \Lambda ( s , \pi ) : = \prod _ { v } L _ { v } ( s , \pi _ { v } ) } \end{array}$for the (completed) L-function attached to π.

2.12.2. The analytic conductor of Iwaniec-Sarnak. We recall the definition in the context where it will arise. Let$\pi = \otimes \pi _ { v }$be a cuspidal representation of$\operatorname { G L } ( n )$over $F$

For each finite place v we denote by Cond (π) the conductor, in the sense of Jacquet, Piatetski-Shapiro, and Shalika, of$\pi _ { v } ;$thus$\mathrm { C o n d } _ { v } ( \pi ) = q _ { v } ^ { m _ { v } }$, where$m _ { v }$is the smallest non-negative integer such that$\pi _ { v }$possesses a fixed vector under the subgroup of${ \mathrm { G L } } _ { n } ( \mathfrak { o } _ { F _ { v } } )$consisting of matrices whose bottom row is congruent to $( 0 , 0 , \ldots , 0 , 1 )$modulo$\varpi _ { v } ^ { m }$

For each infinite place$v ,$let$\Gamma _ { v } ( s ) = \pi ^ { - s / 2 } \Gamma ( s / 2 )$or$( 2 \pi ) ^ { - s } \Gamma ( s )$according to whether v is real or complex respectively, and put$\deg ( v ) = [ F _ { v } : \mathbb { R } ]$. Let$\mu _ { j , v } \in \mathbb { C }$ satisfy$L ( s , \pi _ { v } ) = \prod \Gamma _ { v } ( s + \mu _ { j , v } )$, and put Cond$\begin{array} { r } { \mathbf { \Sigma } _ { v } ( \pi ) = \prod _ { v } ( 1 + | \mu _ { j , v } | ) ^ { \mathrm { d e g } ( v ) } } \end{array}$. We then put$\begin{array} { r } { \mathrm { C o n d } ( \pi ) = \prod _ { v } \mathrm { C o n d } _ { v } ( \pi ) } \end{array}$(this is within a constant factor of the Iwaniec-Sarnak definition). Moreover, we put$\begin{array} { r } { \mathrm { C o n d } _ { \infty } ( \pi ) = \prod _ { v \mathrm { i n f i n i t e } } \mathrm { C o n d } _ { v } ( \pi ) } \end{array}$and$\mathrm { C o n d } _ { f } ( \pi ) =$ $\Pi _ { v \mathrm { f i n i t e } } \mathrm { C o n d } _ { v } ( \pi )$(the “infinite” and “finite” parts of the conductor).

We will occasionally refer to the “finite conductor” of π as the ideal$\Pi _ { v } \mathfrak { q } _ { v } ^ { m _ { v } }$2 where$\mathfrak { q } _ { v }$is the prime ideal corresponding to the finite place$v ;$then$\operatorname { C o n d } _ { f } ( \pi )$is the norm of this ideal. Hopefully the distinction between the two usages will be clear from context.

Remark 2.2. (Explication for$\operatorname { G L } ( 1 )$in the archimedean case) Let us be slightly more explicit in the case of a unitary character$\omega$of$\mathbb { A } _ { F } ^ { \times } / F ^ { \times }$. If v is real, then there is$t \in \mathbb { R }$such that$\omega ( x ) = | x | ^ { i t }$for$x > 0$; then Cond$\begin{array} { r } { | \mathbf { \sigma } _ { v } ( \omega ) \asymp ( 1 + | t | ) } \end{array}$. If v is complex, then there is$t \in \mathbb { R } , N \in \mathbb { Z }$such that$\omega ( r e ^ { i \theta } ) ~ = ~ | r | ^ { i t } e ^ { i N \theta }$; then $\mathrm { C o n d } _ { v } ( \omega ) \asymp ( 1 + | t | + N ) ^ { 2 }$

We can heuristically summarize this: in the real case, ω is approximately constant in a neighbourhood of the identity of size$\mathrm { C o n d } _ { v } ( \omega ) ^ { - 1 }$; in the complex, case ω is approximately constant in a disc around the identity of area$\mathrm { C o n d } _ { v } ( \omega ) ^ { - 1 }$

2.12.3. Cusp forms. If π is a cuspidal representation of${ \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$or$\mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$, it will be convenient to denote by$\pi _ { \infty }$the archimedean representation$\left( \mathrm { o f \ G L _ { 2 } } ( F _ { \infty } ) \right.$ or$\mathrm { P G L _ { 2 } } ( F _ { \infty } ) )$that corresponds to π.

By the dual$\widehat { \mathrm { G L _ { 2 } } ( F _ { \infty } } )$or$\widehat { \mathrm { P G L _ { 2 } } } ( F _ { \infty } )$, we shall mean the space of irreducible, admissible representations. We say a subset of this dual is bounded if the corresponding set of Langlands parameters is bounded. We may define, in an evident way, the conductor$\mathrm { C o n d } ( \pi _ { \infty } )$for$\pi _ { \infty } \in \widetilde { \mathrm { G L } _ { 2 } } ( \widehat { F _ { \infty } } )$; with this definition, a subset is bounded exactly when Cond takes bounded values on it.

In a similar fashion, we define the notion of a bounded subset of$\widehat { G L _ { 2 } ( F _ { v } } )$or ${ \widehat { P G L } } _ { 2 } ( { \widehat { F } } _ { v } )$for any place$v ,$where, again$\widehat { \mathrm { G L _ { 2 } } ( F _ { v } } )$denotes the set of irreducible, admissible representations.

## 3. Unipotent periods.

In this section, we will make systematic use of the (nonadelic) Sobolev norms $S _ { \infty , d }$on homogeneous spaces$\Gamma \backslash G$. In rough terms,$S _ { \infty , d }$controls the$L ^ { \infty }$norm of the first d derivatives. See Sec. 2.9.2. Note in particular that$S _ { \infty , 0 }$is just the$L ^ { \infty }$ norm.

3.1. Equidistribution of sparse subsets of horocycles. Let$\Gamma \subset \operatorname { S L } _ { 2 } ( \mathbb { R } )$be a cocompact lattice. For this section alone, we will use mildly diferent notation to that of Sec. 2.5, to accommodate the fact we deal with$\mathrm { { S L _ { 2 } } }$and not with$\mathrm { P G L _ { 2 } }$ For$x \in \mathbb { R }$, put

$$
n (x) = \left( \begin{array}{c c} 1 & x \\ 0 & 1 \end{array} \right), a (x) = \left( \begin{array}{c c} x ^ {1 / 2} & 0 \\ 0 & x ^ {- 1 / 2} \end{array} \right), \bar {n} (x) = \left( \begin{array}{c c} 1 & 0 \\ x & 1 \end{array} \right).\tag{3.1}
$$

We denote by$C ( \Gamma \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } ) )$(resp.$C ^ { \infty } ( \Gamma \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } ) ) )$the space of continuous (resp. smooth) functions on the compact real manifold$\Gamma \backslash \mathrm { S L _ { 2 } } ( \mathbb { R } )$. We denote by dg the measure on$\operatorname { S L _ { 2 } } ( \mathbb { R } )$that descends to a probability measure on the quotient $\Gamma \backslash \mathrm { S L _ { 2 } } ( \mathbb { R } )$. Finally, we denote by H the usual upper half plane$\{ z : \mathbb { S } ( z ) > 0 \}$with the standard action of$\operatorname { S L _ { 2 } } ( \mathbb { R } )$

Theorem 3.1. There exists$\gamma _ { \mathrm { m a x } } > 0$, depending on Γ, such that$\{ x _ { 0 } n ( j ^ { 1 + \gamma } ) : j \in$ N is equidistributed, for any$x _ { 0 } \in \Gamma \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } )$and any$0 \leq \gamma < \gamma _ { \mathrm { m a x } }$. In other words, for any$f \in C ( \Gamma \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } ) )$,

$$
\lim _ {N \to \infty} \frac {\sum_ {j = 1} ^ {N} f (x _ {0} n (j ^ {1 + \gamma}))}{N} = \int_ {\Gamma \backslash \mathrm{SL} _ {2} (\mathbb {R})} f (g) d g.
$$

If$\lambda _ { 1 }$is the smallest nonzero eigenvalue of the Laplacian on$\Gamma \backslash \mathbb { H }$, put$\alpha =$ $\left\{ \begin{array} { l l } { 0 , \quad } & { \lambda _ { 1 } \geq 1 / 4 } \\ { \sqrt { 1 / 4 - \lambda _ { 1 } } , \quad e l s e . } \end{array} \right.$. Then we can take$\begin{array} { r } { \gamma _ { \operatorname* { m a x } } = \frac { ( 1 - 2 \alpha ) ^ { 2 } } { 1 6 ( 3 - 2 \alpha ) } } \end{array}$

This result represents (extremely modest) progress towards a conjecture of N.Shah, which asserts that the statement should remain valid for any$\gamma > 0$. The method is not restricted to sequences of the specific type in Thm. 3.1, and we have also not optimized the maximal value for$\gamma _ { \mathrm { m a x } }$. Nevertheless the method is fundamentally limited. As it presently stands, it does not seem capable of achieving even$\gamma = 1$ See also Remark 3.1 (page 26).

The dependence of$\gamma _ { \mathrm { m a x } }$on Γ can likely be removed, but this seems to require using further input (cf. last paragraph of Section$1 . 3 . 4 )$

The proof follows the line of Sec. 1.3.1, with$G _ { 1 } = \mathrm { S L } _ { 2 } ( \mathbb { R } ) , G _ { 2 } = \{ n ( x ) : x \in \mathbb { R } \}$ The$Y _ { i }$are not quite closed$G _ { \mathrm { 2 ^ { - O r b i t s } } }$, but rather long pieces of general$G _ { \mathrm { 2 ^ { - O r b i t s } } }$ The basis$\{ \psi _ { i , j } \}$for$Y _ { i }$will correspond to additive characters of$G _ { 2 } \cong \mathbb { R }$

Let$f \in C ^ { \mathsf { i o } } ( \Gamma \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } ) )$, and let α be as in the statement of Thm. 3.1. Let $T \geq 1$. Let ψ be a fixed nontrivial character of the additive group of R. Let$g$be a fixed smooth function of compact support on R satisfying$\begin{array} { r } { { \bf \bar { \rho } } _ { - \infty } ^ { \infty } { \bf \bar { \rho } } _ { g } ( x ) d x = 1 } \end{array}$. We denote by$\langle \cdot , \cdot \rangle _ { L ^ { 2 } ( \Gamma \backslash G ) }$the inner product in the Hilbert space$L ^ { 2 } ( \Gamma \backslash G )$

We set:

$$
\nu_ {T} (f) = \frac {1}{T} \int_ {0} ^ {T} f (x _ {0} n (t)) d t, \mu_ {T, \psi} (f) = \frac {1}{T} \int_ {0} ^ {T} \psi (t) f (x _ {0} n (t)) d t.\tag{3.2}
$$

Remark first that the measures$\nu _ { T }$are equidistributed as$T \to \infty$, in the following quantitative sense: for$f \in C ^ { \infty } ( \Gamma \backslash { \mathrm { S L } } _ { 2 } ( \mathbb R ) )$,

$$
\left| \nu_ {T} (f) - \int_ {\Gamma \backslash \mathrm{SL} _ {2} (\mathbb {R})} f (g) d g \right| \ll T ^ {- \kappa_ {1}} S _ {\infty , 1} (f),\tag{3.3}
$$

for any$\kappa _ { 1 } ~ < ~ \frac { 1 / 2 - \alpha } { 2 }$. This is proven in Lem. 9.4, without taking any pains to optimize the exponent. (We prove it to keep the paper self-contained. However, we emphasize that neither result nor proof is new; see [25] and [26]. A precise analysis of the equidistribution of long horocycles is carried out in [11].)

Lemma 3.1. Suppose$\begin{array} { r } { \int _ { \Gamma \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } ) } f ( g ) d g = 0 } \end{array}$. Then:

$$
| \mu_ {T, \psi} (f) | \ll T ^ {- b} S _ {\infty , 1} (f),\tag{3.4}
$$

whenever$\begin{array} { r } { b < \frac { ( 1 - 2 \alpha ) ^ { 2 } } { 8 ( 3 - 2 \alpha ) } } \end{array}$and the implicit constant is independent of$\psi$

Remark that if ψ is wildly oscillatory, cancellation in$\mu _ { T , \psi }$can be proved directly by integration by parts; on the other hand, if ψ is almost constant, the cancellation in$\mu _ { T , \psi }$arises from the equidistribution of the horocycle$x _ { 0 } G _ { 2 }$. It is therefore the intermediate case in which (3.4) is of interest.

Proof. Let$H \geq 1$, and let$\sigma _ { H }$be the measure on$N ( \mathbb { R } )$defined by$\sigma _ { H } ( g ) =$ $\begin{array} { r } { \frac { 1 } { H } \int _ { 0 } ^ { H } \psi ( x ) g ( n ( x ) ) d x } \end{array}$, for$g \mathrm { ~ a ~ }$function on$N ( \mathbb { R } )$

For$f \in C ^ { \infty } ( \Gamma \backslash G )$, we denote by$f \star \sigma _ { H }$the right convolution of$f$by$\sigma _ { H }$. Then it is easy to verify that$\begin{array} { r } { | \mu _ { T , \psi } ( f ) - \mu _ { T , \psi } ( f \star \sigma _ { H } ) | \ll \frac { H } { T } S _ { \infty , 0 } ( f ) } \end{array}$. Here ⋆σ<sub>H</sub> denotes right convolution by$\sigma _ { H }$. On the other hand, by Cauchy-Schwarz,$| \mu _ { T , \psi } ( f \star \sigma _ { H } ) | ^ { 2 } \leq$ $\nu _ { T } ( | f \star \sigma _ { H } | ^ { 2 } )$. Thus, expanding$| f \star \sigma _ { H } | ^ { 2 }$and applying (3.3), we conclude (3.5)

$$
\begin{array}{c} | \mu_ {T, \psi} (f) | \ll \frac {H}{T} S _ {\infty , 0} (f) + \left(\frac {1}{H ^ {2}} \int_ {(h _ {1}, h _ {2}) \in [ 0, H ] ^ {2}} \left| \nu_ {T} (n (h _ {1}) f \cdot \overline {{n (h _ {2}) f}}) \right| d h _ {1} d h _ {2}\right) ^ {1 / 2} \\ \ll \frac {H}{T} S _ {\infty , 0} (f) + \left(\frac {1}{H ^ {2}} \int_ {(h _ {1}, h _ {2}) \in [ 0, H ] ^ {2}} \left| \langle n (h _ {1} - h _ {2}) f, f \rangle_ {L ^ {2} (\Gamma \setminus G)} \right| d h _ {1} d h _ {2}\right) ^ {1 / 2} \\ + \left(T ^ {- \kappa_ {1}} \sup _ {(h _ {1}, h _ {2}) \in [ 0, H ] ^ {2}} S _ {\infty , 1} (n (h _ {1}) f \cdot \overline {{n (h _ {2}) f}})\right) ^ {1 / 2} \end{array}
$$

Utilising bounds towards matrix coeficients – see Sec. 9.1.2, esp. (9.6) – and basic properties of Sobolev norms (see <sup>7</sup> Lem. 2.2), we note:

$$
\begin{array}{r l} \langle n (h) f, f \rangle & \ll_ {\epsilon} (1 + | h |) ^ {2 \alpha - 1 + \epsilon} S _ {\infty , 1} (f) ^ {2}, \\ & | S _ {\infty , 1} (n (h _ {1}) f \cdot \overline {{n (h _ {2}) f}}) | \ll (1 + | h _ {1} | + | h _ {2} |) ^ {2} S _ {\infty , 1} (f) ^ {2}. \end{array} \tag {3.6}
$$

Thus,$\begin{array} { r } { | \mu _ { T , \psi } ( f ) | \ll _ { \epsilon } \left( \frac { H } { T } + H ^ { \alpha - 1 / 2 + \epsilon } + T ^ { - \kappa _ { 1 } / 2 } H \right) S _ { \infty , 1 } ( f ) } \end{array}$. Choose H so that$H ^ { \alpha - 1 / 2 } =$ $H T ^ { - \kappa _ { 1 } / 2 }$to obtain the claimed result.

Proof. (of Thm. 3.1). Given Lem. 3.1, the Theorem follows quite readily by Fourier-expanding the measure on R that is a sum of point masses at$j ^ { \gamma }$, for$j \in$ N. The argument that follows formalizes a minor variant of this argument (we first consider instead a sum of point masses along arithmetic progressions which approximate$\{ j ^ { \gamma } : j \in \mathbb { N } \} ,$).

Let$x _ { 0 } \in \Gamma \backslash { \mathrm { S L } } _ { 2 } ( \mathbb { R } ) , f \in C ^ { \infty } ( \Gamma \backslash { \mathrm { S L } } _ { 2 } ( \mathbb { R } ) )$. We first claim that, if b is as in the previous Lemma,$f$so that$\begin{array} { r } { \int _ { \Gamma \backslash \mathrm { S L 2 } ( \mathbb { R } ) } f ( g ) d g = 0 . } \end{array}$and$K \geq 1$, then:

$$
\frac {\sum_ {0 \leq j <   K ^ {1 / b - 1}} f (x _ {0} n (K j))}{K ^ {1 / b - 1}} \rightarrow 0,\tag{3.7}
$$

as$K  \infty$. In other words,$K ^ { 1 / b - 1 }$points, distributed along a horocycle with spacing$K .$, become equidistributed.

This follows from Lem. 3.1: put$g _ { \delta } ( x ) = \operatorname* { m a x } ( \delta ^ { - 2 } ( \delta - | x | ) , 0 )$, a function on R. For$\lambda \in \mathbb { R }$, write$\begin{array} { r } { a _ { \lambda } = K ^ { - 1 } \int _ { \mathbb { R } } \exp ( - 2 \pi i K ^ { - 1 } \lambda t ) g _ { \delta } ( t ) d t } \end{array}$. Then$\begin{array} { r l } { \sum _ { j \in \mathbb { Z } } g _ { \delta } ( t + K j ) = } & { { } } \end{array}$ $\begin{array} { r l } & { \sum _ { k \in \mathbb { Z } } \exp ( 2 \pi i K ^ { - 1 } k t ) a _ { k } } \\ & { \delta ^ { - 1 } . } \end{array}$. Moreover, a simple computation shows that$\textstyle \sum _ { k \in \mathbb { Z } } \left| a _ { k } \right| \ll$

Choose$\varepsilon > 0$so that$b + \varepsilon$still satisfies the inequality of Lem. 3.1. By Lem. 3.1,

$$
\left| \int_ {t = 0} ^ {T} d t \left(\sum_ {j \in \mathbb {Z}} g _ {\delta} (t + K j)\right) f (x _ {0} n (t)) \right| \ll_ {f} T ^ {1 - b - \varepsilon} \sum_ {k} | a _ {k} | \ll T ^ {1 - b - \varepsilon} \delta^ {- 1}.\tag{3.8}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1 + |h1| + |h2|)4</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>7</sup>Lem. 2.2 would actually give the exponent (1 + |h<sub>1</sub>| + |h<sub>2</sub>|)<sup>4</sup> in the latter inequality, but it is easy to see directly the stronger result.</span></small>

$g _ { \delta }$has integral 1 and is supported in a δ-neighbourhood of 0; in particular, the left-hand side of (3.8) difers from$\begin{array} { r } { \sum _ { j \in \mathbb { Z } , 0 \le K j \le T } f ( x _ { 0 } n ( K j ) ) } \end{array}$by an error that is $\ll _ { f } \left( 1 + T K ^ { - 1 } \delta \right)$. Thus$\begin{array} { r } { \left| \sum _ { j \in \mathbb { Z } , 0 \le K j \le T } f ( x _ { 0 } n ( K j ) ) \right| \ll _ { f } ( 1 + T K ^ { - 1 } \delta + T ^ { 1 - b - \varepsilon } \delta ^ { - 1 } ) } \end{array}$ from which (3.7) readily follows.

We now deduce the Theorem from (3.7). Let$T _ { 0 } \in \mathbb { N }$be large. Then, for t small, we have$( T _ { 0 } + t ) ^ { 1 + \gamma } = T _ { 0 } ^ { 1 + \gamma } + ( 1 + \gamma ) T _ { 0 } ^ { \gamma } t + O ( t ^ { 2 } T _ { 0 } ^ { \gamma - 1 } )$. In particular,$( T _ { 0 } + t ) ^ { 1 + \gamma }$ is well-approximated by the linear function$T _ { 0 } ^ { 1 + \gamma } + ( 1 + \gamma ) T _ { 0 } ^ { \gamma } t$in the range where $| t | \ll T _ { 0 } ^ { \frac { 1 - \gamma } { 2 } }$

The claim of Thm. 3.1 follows from (3.7) as long as$\begin{array} { r } { \frac { 1 - \gamma } { 2 \gamma } > 1 / b - 1 } \end{array}$; in particular, any$\gamma < b / 2$will do.

Remark 3.1. The applicability of this method is not, of course, restricted to sequences of the form$t ^ { 1 . 0 1 } , \ t \ \in \ \mathbb { N } .$. In certain (very artificial) settings, one can prove some efective instances of Ratner’s theorem in non-horospherical cases by the same technique. The question of proving such results, even in very special cases, was raised by Margulis in his talk in the workshop “Emerging applications of measure rigidity.”

For instance, let$r \ > \ 1$be an integer, and let Γ be a cocompact lattice in $\mathrm { S L _ { 2 } } ( \mathbb { R } ) ^ { r }$For concreteness, let us suppose that Γ is a congruence lattice. Let $\mathbf { n } ( x _ { 1 } , \ldots , x _ { r } ) = ( n ( x _ { 1 } ) , n ( x _ { 2 } ) , \ldots , n ( x _ { r } ) ) \in { \mathrm { S L } } _ { 2 } ( \mathbb { R } ) ^ { r }$. Then it is well-known that one can give an efective version of the equidistribution of$\mathbf { n } ( \mathbb { R } ^ { r } )$, since$\mathbf { n } ( \mathbb { R } ^ { r } )$is horospherical. Using the method described above, one can extend this slightly: let$V \subset \mathbb { R } ^ { r }$be a linear subspace. One may show that n(V)-orbits are efectively equidistributed if$\dim ( V ) / r$is suficiently close to 1. However, the small codimension condition is crucial for this method and it does not seem that it would extend beyond this case.

3.2. Fourier coeficients of automorphic forms. In the notations of Sec. 1, if we take for$Y _ { i }$the closed orbits of a unipotent group, the resulting periods are socalled “Fourier coeficients of automorphic forms.” We shall give a general nontrivial bound in that context. (The word “nontrivial” must be interpreted with care; see the discussion at the end of this section.) Our methods are restricted to the case of horospherical unipotent subgroups.

We have made no efort to optimize the exponents of the results, nor even to state a result of maximal generality. In fact, one can considerably increase the scope of Thm. 3.2, since we deal in the present section only with closed orbits of horospherical subgroups, one can profitably apply spectral theory. We do not carry this out, instead using [18] to give equidistribution statements in a fairly soft fashion.

Let G be a connected semisimple real Lie group,$\Gamma \subset G$a lattice,$K \subset G$ the maximal compact subgroup, g the Lie algebra of$G ,$and$H \in { \mathfrak { g } }$a semisimple element. Fix a norm$\| \cdot \|$on the real vector space g. Let exp$\colon { \mathfrak { g } }  G$be the exponential map. Fix a Haar measure on$G$so that$\Gamma \backslash G$has volume 1. Let u be the sum of all negative root spaces for H and let$U = \exp ( \mathfrak { u } ) \subset G$. Let$x _ { 0 } \in \Gamma \backslash G$ be so that$x _ { 0 } U$is compact. Let$x _ { t } = x _ { 0 } \exp ( t H )$, and let$\Delta _ { t }$be the stabilizer of$x _ { t }$ in U. We denote by$\langle \cdot , \cdot \rangle _ { L ^ { 2 } ( \Gamma \backslash G ) }$the inner product in the Hilbert space$L ^ { 2 } ( \Gamma \backslash G )$

We shall analyze periods of a fixed function along$x _ { t } U$as t varies. The proofs follow Sec. 1.3.1 with$G _ { 1 } = G , G _ { 2 } = U , Y _ { i } = x _ { t } U$, and$\psi _ { i , j }$corresponding to characters of U.

Let$T > 0$and let ψ be any character of U trivial on$\Delta _ { T } \left( : = \exp ( - T H ) \Delta _ { 0 } \exp ( T H ) \right)$ We define$\nu _ { T } , \mu _ { T , \psi }$in a closely analogous fashion to (3.2):

$$
\nu_ {T} (f) = \frac {\int_ {\Delta_ {T} \setminus U} f (x _ {T} u) d u}{\mathrm{vol} (\Delta_ {T} \setminus U)}, \mu_ {T, \psi} (f) = \frac {\int_ {\Delta_ {T} \setminus U} f (x _ {T} u) \psi (u) d u}{\mathrm{vol} (\Delta_ {T} \setminus U)}.\tag{3.9}
$$

Let$f , g \in C ^ { \infty } ( \Gamma \backslash G )$. Let$E \in { \mathfrak { u } }$have unit length w.r.t. the fixed norm$\| \cdot \|$on g. It is proven by Kleinbock-Margulis in [18] – see also Lem. 9.5 and Lem.$9 . 6 -$ that there are$\kappa _ { 1 } , \kappa _ { 2 } > 0$such that:

(3.10)

$$
\left| \langle \exp (s E) \cdot f, g \rangle_ {L ^ {2} (\Gamma \backslash G)} - \int_ {\Gamma \backslash G} f \int_ {\Gamma \backslash G} g \right| \ll (1 + | s |) ^ {- \kappa_ {1}} S _ {\infty , \dim (K)} (f) S _ {\infty , \dim (K)} (g)\tag{3.11}
$$

$$
| \nu_ {T} (f) - \int_ {\Gamma \backslash G} f | \ll e ^ {- \kappa_ {2} T} S _ {\infty , \dim (K)} (f).
$$

(3.10) and (3.11) assert, respectively, quantitative mixing of the flow generated by $U$on$\Gamma \backslash G .$, and the equidistribution of the orbit$x _ { T } U$as$T \to \infty$. We may assume that$\kappa _ { 1 } < 1$(since making$\kappa _ { 1 }$smaller does not change the truth of (3.10)). This will ease the notation in the proof of the Theorem.

Theorem 3.2. There exists$\kappa _ { 3 } > 0$such that, for any$f \in C ^ { \infty } ( \Gamma \backslash G )$satisfying $\textstyle \int _ { \Gamma \backslash G } f = 0$, we have:

$$
| \mu_ {T, \psi} (f) | \ll \exp (- T \kappa_ {3}) S _ {\infty , \dim (K)} (f)\tag{3.12}
$$

for all$T \geq 0$, and for all characters ψ of U trivial on$U _ { T }$

Indeed,$i f o$is the order of the polynomial map$\mathbb { R }  \operatorname { E n d } ( { \mathfrak { g } } )$defined by$s \mapsto$ $\operatorname { A d } ( \exp ( s H ) )$), then any$\kappa _ { 3 } < \frac { \kappa _ { 1 } \kappa _ { 2 } } { 2 ( 2 o \dim ( K ) + \kappa _ { 1 } ) }$is admissible,$\kappa _ { 1 , 2 }$being as in$\it { \left( 3 . 1 0 \right) }$ and (3.11).

The relevance to this to “Fourier coeficients” in the classical sense may not be immediately clear; after the proof, we give the example of$\operatorname { S L _ { 2 } } ( \mathbb { R } )$to illustrate.

Also, observe that the estimate (3.12) is uniform in ψ. In fact, just as in Lem. 3.1, the case when$\psi$is constant amounts to (3.11), whereas the case where$\psi$ is highly oscillatory could be handled by integration by parts. It is, again, the intermediate case where (3.12) has content.

Proof. We first remark that, other than being in a slightly more general setting, the proof is almost exactly the same as the proof of Lem. 3.1.

The signed measure$\mu _ { T , \psi }$satisfies$\mu _ { T , \psi } ( u \cdot f ) = \overline { { \psi ( u ) } } \mu _ { T , \psi } ( f )$, for$u \in U$

Take$E \in { \mathfrak { u } }$of unit length w.r.t. the norm$\| \cdot \|$on g. Fix$H \geq 1$. Let$\sigma$be the measure on$U$defined via the rule

$$
\sigma (h) = \frac {1}{H} \int_ {s = 0} ^ {H} \psi (\exp (s E)) h (\exp (s E)) d s,
$$

for h any continuous compactly supported function on U. Then$\mu _ { T , \psi } ( f ) = \mu _ { T , \psi } ( f \star$ σ); thus:

$$
\begin{array}{r l} & {| \mu_ {T, \psi} (f) | ^ {2} = | \mu_ {T, \psi} (f \star \sigma) | ^ {2} \leq \nu_ {T} (| f \star \sigma | ^ {2})} \\ & {\quad \ll \int_ {\Gamma \backslash G} | f \star \sigma | ^ {2} + e ^ {- \kappa_ {2} T} S _ {\infty , \dim (K)} (| f \star \sigma | ^ {2})} \\ & {\qquad \leq \int_ {\Gamma \backslash G} | f \star \sigma | ^ {2} + H ^ {2 o \dim (K)} \exp (- \kappa_ {2} T) S _ {\infty , \dim (K)} (f) ^ {2}.} \end{array}\tag{3.13}
$$

where we have applied Cauchy-Schwarz followed by (3.11), noting that by Lem. 2.2, we have that$S _ { \infty , \dim ( K ) } ( | f \star \sigma | ^ { 2 } ) \ll S _ { \infty , \dim ( K ) } ( f \star \sigma ) ^ { 2 } \ll H ^ { 2 o \dim ( K ) } S _ { \infty , \dim ( K ) } ( f ) ^ { 2 }$ Here o is chosen as in the statement of the Theorem.

By (3.10), we see that

$$
\begin{array}{c} \int_ {\Gamma \backslash G} | f \star \sigma | ^ {2} \ll \left(\frac {1}{H} \int_ {0} ^ {H} (1 + | t |) ^ {- \kappa_ {1}} d t\right) S _ {\infty , \dim (K)} (f) ^ {2} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad H ^ {- \kappa_ {1}} S _ {\infty , \dim (K)} (f) ^ {2}. \end{array}\tag{3.14}
$$

Indeed, this follows simply by expanding the leftmost expression. Thus

$$
| \mu_ {T, \psi} (f) | ^ {2} \ll (H ^ {- \kappa_ {1}} + H ^ {2 o \dim (K)} \exp (- \kappa_ {2} T)) S _ {\infty , \dim (K)} (f) ^ {2}.
$$

We choose H so that$H ^ { 2 o \dim ( K ) + \kappa _ { 1 } } = \exp ( \kappa _ { 2 } T )$to conclude.

Remark 3.2. We now explain, when we specialize$G = \mathrm { { S L } _ { 2 } ( \mathbb { R } ) }$, why this recovers Sarnak’s result [30], which was the first improvement of the Hecke bound for nonarithmetic groups. Take$H = \left( \begin{array} { c c } { - 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) \in \mathfrak { s l } _ { 2 }$, so that$U = \left( \begin{array} { l l } { 1 } & { * } \\ { 0 } & { 1 } \end{array} \right)$. Let $\Gamma \subset G$be a nonuniform lattice so that$\Gamma \cap U = \{ \left( \begin{array} { l l } { 1 } & { n } \\ { 0 } & { 1 } \end{array} \right) , n \in \mathbb { Z } \}$, and take $x _ { 0 } = { \left( \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) }$. Let$\begin{array} { r } { f ( x + i y ) = \sum _ { n \ne 0 } a _ { n } \sqrt { y } K _ { i \nu } ( 2 \pi n y ) e ^ { 2 \pi i n x } } \end{array}$be a Maass cusp form of eigenvalue$1 / 4 + \nu ^ { 2 }$on$\Gamma \backslash \mathbb { H } .$, where H denotes the upper half-plane; it lifts to a function on$\Gamma \backslash \mathrm { S L _ { 2 } } ( \mathbb { R } )$, viz.$g \mapsto f ( g . i )$

Then the Theorem implies (in concrete language) that there exists$\delta > 0$such that, for any$y \le 1$and any$n \in \mathbb { Z }$,

$$
\int_ {0 \leq x \leq 1} f (x + i y) e (n x) d x \ll y ^ {\delta}.\tag{3.15}
$$

Taking$y \asymp n ^ { - 1 }$in (3.15), one easily deduces that the Fourier coeficients$a _ { n }$satisfy the “nontrivial” bound$| a _ { n } | \leq n ^ { 1 / 2 - \delta }$

Remark 3.3. The bound Thm. 3.2 is nontrivial in that it improves, as$t \to \infty$on the trivial bound:

$$
\left| \frac {\int_ {\Delta_ {t} \backslash U} f (x u) \psi (u) d u}{\operatorname{vol} (\Delta_ {t} \backslash U)} \right| \ll_ {f} 1,
$$

which follows from Cauchy-Schwarz.

However, if there is another interpretation for the Fourier coeficients, it is not always the case that Thm. 3.2 improves on “trivial” bounds arising from that interpretation.

For instance, Fourier coeficients of cusp forms on$\mathrm { G L } _ { n }$admit a spectral interpretation, that is to say, they are connected to the eigenvalues of Hecke operators. In that case, Thm. 3.2 does not give anything even approaching the bounds of Jacquet-Piatetski-Shalika. Another example is when$G = \widetilde { \mathrm { S L } } _ { 2 } ( \mathbb { R } )$, and one takes for$f$fthe Shimura lift of a cusp form of integral weight. In that case the (absolute values of the squares$\mathrm { o f } )$square-free Fourier coeficients of$f$are given by special values of a twisted L-function; but the estimate above does not even recover the convexity bound (in fact, the method as indicated cannot recover this bound, even under optimal assumptions.)

It seems as though, in these cases, there is extra cancellation in the unipotent integrals for subtle arithmetic reasons. The crude methods indicated above do not detect this.

Remark 3.4. We remark that, in the proof just given, the constant$\kappa _ { 3 }$depends on the spectral gap for Γ G. This dependence can very likely be removed in many cases, including the case of$G = \mathrm { { S L } _ { 2 } ( \mathbb { R } ) }$, but we do not carry this out; again, cf. the last paragraph of Section 1.3.4. In the higher rank case, if G has property (T), one has in any case a uniform spectral gap and this point becomes irrelevant.

It seems worthwhile to remark that, whereas the proof above is clearly not unrelated to that of Sarnak, it does not require any information on the decay of triple products (in particular, the deep “exponential decay” results proved by Sarnak and Bernstein-Reznikov).

We also remark that the proof indicated above, although it can be optimized in various ways, probably does not lead to as good an exponent as the work of Good, and the later refinement of Sarnak’s result due to Bernstein-Reznikov. Its advantage lies, rather, in its robustness and general applicability.

## 4. Semisimple periods: triple products in the level aspect.

In this section, we will give bounds for the triple product period on$\mathrm { P G L _ { 2 } }$over a number field F. We will use the notation of Sec.$2 ;$in particular,$\mathbb { A } _ { F }$is the adele ring of$F$and and$\mathbf { X } = \mathrm { P G L } _ { 2 } ( F ) \backslash \mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$

In Sec. 4.1, we will give a special case of the triple product bound (Prop. 4.1) which does not require Sobolev norms to state. For some applications we will require a slight generalization, which will require the Sobolev norms of Sec. 2.9.3. This will be carried out in Sec. 4.2 (see Prop. 4.2).

4.1. Period bound for triple products. We now give a period bound for triple products on$\mathrm { P G L _ { 2 } }$. Although it is unfortunately somewhat disguised in the adelic language, the situation and method corresponds to that of Sec. 1.3.1 with$G _ { 1 } =$ $\mathrm { P G L _ { 2 } } ( F _ { S } ) \times \mathrm { P G L _ { 2 } } ( F _ { S } ) , G _ { 2 } = \mathrm { P G L _ { 2 } } ( F _ { S } )$embedded diagonally. Here$S$is a set of places of$F$containing all infinite places, and$\textstyle F _ { S } = \prod _ { v \in S } F _ { v }$

For$1 ~ \leq ~ p ~ \leq ~ \infty$we will write$L ^ { p }$for$L ^ { p } ( \mathbf { X } )$Q ∈<sub>. Thus,</sub>$\mathrm { e . g . } , \ \| f _ { 1 } \| _ { L ^ { 4 } }$denotes $\begin{array} { r } { \left( \int _ { \mathbf { X } } | f _ { 1 } ( x ) | ^ { 4 } d x \right) ^ { 1 / 4 } } \end{array}$

Proposition 4.1. (“Subconvexity for the triple product period.”) Let$\pi$be an automorphic cuspidal representation of$\mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$with prime finite conductor p.

Let$f _ { 1 } , f _ { 2 } \in C ^ { \infty } ( \mathbf { X } )$be totally nondegenerate<sup>8</sup> and such that$f _ { 1 } , f _ { 2 }$are$\mathrm { P G L _ { 2 } } ( \mathfrak { o } _ { F _ { \mathfrak { p } } } )$ invariant. Let$\varphi \in \pi$and suppose<sup>9</sup> that there exists$b \in \mathbb { R }$such$t h a t ^ { 1 0 }$

$$
\prod_ {\mathfrak {q} \in \operatorname{Supp} (\varphi) \cup \operatorname{Supp} (f _ {1}) \cup \operatorname{Supp} (f _ {2})} N (\mathfrak {q}) \leq N (\mathfrak {p}) ^ {b}\tag{4.1}
$$

Put$\begin{array} { r } { I ( \varphi ) = \int _ { \mathbf { X } } f _ { 1 } ( g ) f _ { 2 } ( g a ( [ \mathfrak { p } ] ) ) \varphi ( g ) d g } \end{array}$, where$a ( [ { \mathfrak { p } } ] )$is as in$( 2 . 4 )$and$d g$is the $\mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$-invariant probability measure. Then

$$
| I (\varphi) | \ll_ {b, \epsilon , F} \| f _ {1} \| _ {L ^ {4}} \| f _ {2} \| _ {L ^ {4}} \| \varphi \| _ {L ^ {2}} N (\mathfrak {p}) ^ {\epsilon - \frac {(1 - 4 \alpha) (1 - 2 \alpha)}{4 (3 - 4 \alpha)}}\tag{4.2}
$$

We refer to Prop. 4.1 as subconvexity$f o r$the triple product period, cf. first assertion of Theorem 5.1. We note that, with$\alpha = 3 / 2 6$(Kim’s bound) we have $\frac { ( 1 - 4 \alpha ) ( 1 - 2 \alpha ) } { 4 ( 3 - 4 \alpha ) } > 1 / 2 6$. As we will see, Prop. 4.1 is a very strong result that implies many subconvexity results on$\mathrm { P G L } ( 2 )$

First let us explain the content of Prop. 4.1 in a classical setting, and how it can be regarded as the type of period bound discussed in the introduction. Suppose $F = \mathbb { Q } ;$let$p \geq 1$and let

$$
\Gamma_ {0} (p) = \{\left( \begin{array}{c c} a & b \\ c & d \end{array} \right) \in \operatorname{GL} _ {2} (\mathbb {Z}): p | c \},
$$

and put$Y ( p ) = \Gamma _ { 0 } ( p ) \backslash \mathrm { P G L } _ { 2 } ( \mathbb { R } )$. Then there is an embedding$Y ( p )  Y ( 1 ) \times Y ( 1 )$ which corresponds to the graph of the pth Hecke correspondence on$Y ( 1 ) ;$the image is a certain closed orbit of the diagonal$\mathrm { P G L _ { 2 } ( \mathbb { R } ) }$. Let$f _ { 1 } , f _ { 2 }$be fixed functions on$Y ( 1 )$and$\varphi$a Maass form on$Y _ { 0 } ( p )$. Then the function$f _ { 1 } \times f _ { 2 } : ( x _ { 1 } , x _ { 2 } )$↓ $f _ { 1 } ( x _ { 1 } ) f _ { 2 } ( x _ { 2 } )$is a function on$Y ( 1 ) \times Y ( 1 )$, and we can construct its restriction $f _ { 1 } \times f _ { 2 } | _ { Y ( p ) }$by means of the embedding indicated above. Then, translating from adelic to classical, one finds that (4.2) furnishes precisely an estimate for$\int _ { Y ( p ) } ( f _ { 1 } \times$ $f _ { 2 } ) | _ { Y ( p ) } \varphi$. When we vary$p , \varphi$and hold$( f _ { 1 } , f _ { 2 } )$fixed, such an estimate falls precisely into the pattern described in the introduction: we are computing the periods of the fixed function$f _ { 1 } \times f _ { 2 }$along the varying sequence of sets$Y ( p )$. The fact that the$Y ( p )$ become equidistributed in$Y ( 1 ) \times Y ( 1 )$is precisely equivalent to the equidistribution of p-Hecke orbits on$Y ( 1 )$. Moreover, the key property of$\varphi$that is used is the fact that$\varphi$is an eigenfunction of many Hecke operators; this is used to construct the measure$\sigma ,$in the notation of Sec. 1.3.

Prior to beginning the proof, we make some comments about applications and generalizations; for details, we refer to Sec. 5. The implicit constant of$( 4 . 2 )$is independent of$f _ { 1 } , \ f _ { 2 }$. Taking$f _ { 1 } , f _ { 2 }$to be a pair of cusp forms Prop. 4.1 implies (conditional on some computations of p-adic integrals that we state as Hypothesis Prop. 11.1) subconvexity for certain triple product L-functions. Similarly, taking $f _ { 1 } , f _ { 2 }$to be a cusp form and an Eisenstein series, resp. a pair of Eisenstein series,

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f ∈ C∞(X)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">PGL2(ov)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>9</sup>Recall that a finite place v belongs to the support of f ∈ C<sup>∞</sup>(X) exactly when PGL<sub>2</sub>(o<sub>v</sub>) does not fix</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>8</sup>See Sec. 2.7; equivalent to “orthogonal to locally constant functions” in this case.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">4</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f<sub>1</sub>, f<sub>2</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f<sub>1</sub>, f<sub>2</sub>, ϕ</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>10</sup>This assumption (4.1) is purely technical and the reader may safely assume that ϕ is spherical at all places away from p and are everywhere spherical without losing the gist of the argument. It is not used in the present document, but will probably be of use in establishing polynomial dependence of subconvex bounds. (4.1) ensures, among other things, that there are many places when all of are unramified, so that we can use the Hecke operators at those places.</span></small>

Prop. 4.1 implies subconvexity for Rankin-Selberg convolutions and standard Lfunctions.

The latter applications are rather delicate because Eisenstein series are not in$L ^ { 4 }$ To get around this we will eventually replace the Eisenstein series by an appropriate wave-packet (cf. proof of Thm. 5.1).

Proof. Clearly we may assume that$\| \varphi \| _ { L ^ { 2 } } = \| f _ { 1 } \| _ { L ^ { 4 } } = \| f _ { 2 } \| _ { L ^ { 4 } } = 1$. It follows that $\| f _ { 1 } \| _ { L ^ { 2 } } \leq 1$and$\| f _ { 2 } \| _ { L ^ { 2 } } \leq 1$

We shall moreover assume, for simplicity, that$\varphi$is spherical at all finite places $v \neq { \mathfrak { p } }$. The reader may verify that the proof carries through to the more general situation of Prop. 4.1 without modification.

Put$q = \mathrm { N } ( { \mathfrak { p } } )$. Let σ be a (signed real) measure on$\mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$such that$\varphi { \star } \breve { \sigma } =$ $\lambda \varphi ,$, for some$\lambda \in \mathbb { C }$. We shall assume that supp(σ) commutes with$\operatorname { P G L _ { 2 } } ( \mathbb { Q } _ { \mathfrak { p } } )$; we will choose σ later. Set further$\Psi ( x ) = f _ { 1 } ( x ) f _ { 2 } ( x a ( [ \mathfrak { p } ] ) ) \in C ^ { \infty } ( \mathbf { X } )$. Then

$$
\begin{array}{l} \lambda \cdot I (\varphi) = \int_ {\mathbf {X}} \Psi (x) \cdot (\varphi \star \check {\sigma}) (x) d x = \int_ {\mathbf {X}} (\Psi \star \sigma) (x) \cdot \varphi (x) d x \leq \left(\int_ {\mathbf {X}} | \Psi \star \sigma | ^ {2} d x\right) ^ {1 / 2} \\ = \left(\int_ {\mathbf {X}} \int_ {(g, g ^ {\prime}) \in \mathrm{PGL} _ {2} (\mathbb {A} _ {F}) ^ {2}} (g \cdot \Psi) \overline {{(g ^ {\prime} \cdot \Psi)}} d \sigma (g) d \sigma (g ^ {\prime}) d x\right) ^ {1 / 2} \\ = \left(\int_ {\mathbf {X}} \int_ {(g, g ^ {\prime}) \in \mathrm{PGL} _ {2} (\mathbb {A} _ {F}) ^ {2}} f _ {1} (x g) f _ {2} (x a ([ \mathfrak {p} ]) g) \overline {{f _ {1} (x g ^ {\prime}) f _ {2} (x a ([ \mathfrak {p} ]) g ^ {\prime})}} d \sigma (g) d \sigma (g ^ {\prime}) d x\right) ^ {1 / 2} \\ = \left(\int_ {\mathbf {X}} \int_ {(g, g ^ {\prime}) \in \mathrm{PGL} _ {2} (\mathbb {A} _ {F}) ^ {2}} f _ {1} (x g) f _ {2} (x g a ([ \mathfrak {p} ])) \overline {{f _ {1} (x g ^ {\prime}) f _ {2} (x g ^ {\prime} a ([ \mathfrak {p} ]))}} d \sigma (g) d \sigma (g ^ {\prime}) d x\right) ^ {1 / 2} \end{array}\tag{4.3}
$$

In the last step, we have used the fact that$\operatorname { P G L _ { 2 } } ( \mathbb { Q } _ { \mathfrak { p } } )$, and thus$a ( [ { \mathfrak { p } } ] )$, commutes with$\operatorname { s u p p } ( \sigma )$

For any two functions$h _ { 1 } , h _ { 2 }$on X, both right invariant by$\mathrm { P G L _ { 2 } } ( \mathfrak { o } _ { F _ { \mathfrak { p } } } )$, the assumed bound on Ramanujan (Def. 2.1) implies:

$$
\left| \begin{array}{c} \int_ {\mathbf {X}} h _ {1} (x) h _ {2} (x a ([ \mathfrak {p} ])) d x - \sum_ {\chi^ {2} = 1} \chi (\mathfrak {p}) \int_ {\mathbf {X}} h _ {1} (x) \chi (x) d x \int_ {\mathbf {X}} h _ {2} (x) \chi (x) d x \\ \leq 2 q ^ {\alpha - 1 / 2} | | h _ {1} | | _ {L ^ {2}} | | h _ {2} | | _ {L ^ {2}} \end{array} \right|\tag{4.4}
$$

Here$\chi$ranges over all characters of$\mathbb { A } _ { F } ^ { \times } / F ^ { \times }$such that$\chi ^ { 2 } = 1$, and$\chi ( x )$denotes the function$g \mapsto \chi ( \operatorname* { d e t } ( g ) )$on$\mathrm { P G L _ { 2 } } ( F ) \bar { \backslash } \mathrm { P G L _ { 2 } } ( \mathbb { A } _ { F } )$. Indeed, to see (4.4), we note that the quantity inside the absolute value on the left hand side of (4.4) equals $\langle h _ { 1 } - \mathcal { P } h _ { 1 } , a ( [ { \mathfrak { p } } ] ) \cdot ( h _ { 2 } - \mathcal { P } h _ { 2 } ) \rangle _ { L ^ { 2 } }$, where$\mathcal { P }$is as in Sec. 2.7 (in this case, the orthogonal projection onto the locally constant functions). But the$L ^ { 2 }$orthogonal projection$\operatorname { I d } - \mathcal { P }$kills all one-dimensional$\mathrm { P G L _ { 2 } } ( F _ { \mathfrak { p } } )$representations, from which the result follows easily.

The functions$h _ { j } ( x ) ~ = ~ f _ { j } ( x g ) \overline { { { f _ { j } ( x g ^ { \prime } ) } } } ( j ~ = ~ 1 , 2 )$are$\mathrm { P G L _ { 2 } } ( \mathfrak { o } _ { F _ { \mathfrak { p } } } )$)-invariant for $g , g ^ { \prime } \in \mathrm { \ s u p p } ( \sigma )$since supp(σ) commutes with$\mathrm { P G L _ { 2 } } ( F _ { \mathfrak { p } } )$and${ \mathfrak { p } } \not \in \ { \mathrm { S u p p } } ( f _ { 1 } ) \cup$ $\operatorname { S u p p } ( f _ { 2 } )$. Moreover,$\| h _ { j } \| _ { L ^ { 2 } } \leq \| f _ { j } \| _ { L ^ { 4 } } ^ { 2 }$. Apply (4.4) to these$h _ { j }$, and substitute

in (4.3). It results:

$$
\begin{array}{l} | \lambda \cdot I (\varphi) | ^ {2} \ll q ^ {\alpha - 1 / 2} \| \sigma \| ^ {2} \\ + \sum_ {\chi^ {2} = 1} \int_ {(g, g ^ {\prime})} | \langle g ^ {- 1} g ^ {\prime} \cdot f _ {1}, f _ {1} \otimes \chi \rangle | \langle g ^ {- 1} g ^ {\prime} \cdot f _ {2}, f _ {2} \otimes \chi \rangle d | \sigma | (g) d | \sigma | (g ^ {\prime}) \end{array}\tag{4.5}
$$

where$| \sigma |$is the total variation measure associated to$\sigma , \| \sigma \| = | \sigma | ( \mathbf { X } )$is the total variation of$\sigma , f _ { i } \otimes \chi$is the function$x \mapsto f _ { i } ( x ) \chi ( \operatorname* { d e t } ( x ) )$, and brackets$\langle \cdot , \cdot \rangle$denote inner product in the Hilbert space$L ^ { 2 } ( \mathbf { X } )$; we will suppress the reference to$L ^ { 2 } ( \mathbf { X } )$ here and in the rest of the argument.

Put$\sigma ^ { ( 2 ) } = | \check { \sigma } | \star | \sigma |$. We may rewrite the previous result as:

$$
\begin{array}{l} | \lambda | ^ {2} | I (\varphi) | ^ {2} \ll q ^ {\alpha - 1 / 2} \| \sigma \| ^ {2} \\ \qquad + \left(\int_ {g} \sum_ {\chi^ {2} = 1} | \langle g \cdot f _ {1}, f _ {1} \otimes \chi \rangle | \cdot | \langle g \cdot f _ {2}, f _ {2} \otimes \chi \rangle | d \sigma^ {(2)} (g)\right) \end{array}\tag{4.6}
$$

We shall take$\sigma$in (4.6) to be a linear combination of Hecke operators. We follow the notations introduced in Sec. 2.8. For n$\notin \mathrm { S u p p } ( \varphi )$, we denote by$\lambda ( \mathfrak { n } )$ be the nth Hecke eigenvalue of$\varphi _ { : }$i.e.$\varphi \star \mu _ { \mathfrak { n } } = \lambda ( \mathfrak { n } ) \varphi .$With our normalizations, the Ramanujan conjecture amounts to$| \lambda ( [ \boldsymbol { \mathbf { \rho } } ] | \leq 2$for l prime.

Let$a _ { \mathfrak { n } }$be a sequence of complex numbers indexed by integral ideals of${ \mathfrak { o } } _ { F }$ Assume moreover that$a _ { \mathfrak { n } } = 0$whenever n is divisible by any place in$\operatorname { S u p p } ( \varphi ) \cup$ $\operatorname { S u p p } ( f _ { 1 } ) \cup \operatorname { S u p p } ( f _ { 2 } )$. Let$\sigma$be the measure on$\mathrm { P G L _ { 2 } } ( \mathbb { A } _ { F , f } )$defined by$\sum _ { \mathfrak { n } } a _ { \mathfrak { n } } \mu _ { \mathfrak { n } }$ Then σ is symmetric under$g \mapsto g ^ { - 1 }$, and$\begin{array} { r } { | \sigma | = \sum _ { \mathfrak { n } } | a _ { \mathfrak { n } } | \mu _ { \mathfrak { n } } . } \end{array}$. Moreover,$\varphi \star \sigma = \lambda \varphi _ { 3 }$ where$\begin{array} { r } { \lambda = \sum _ { n } a _ { \mathfrak { n } } \lambda ( \mathfrak { n } ) } \end{array}$. From the assumed bound on Ramanujan (see Sec. 9.1, esp. equation$( 9 . 1 ) ) ^ { 1 1 }$, an elementary computation shows:

$$
\left| \int_ {g \in \mathrm{PGL} _ {2} (\mathbb {A} _ {F})} | \langle g \cdot f _ {1}, f _ {1} \otimes \chi \rangle \langle g \cdot f _ {2}, f _ {2} \otimes \chi \rangle | d \mu_ {\mathfrak {n}} (g) \right| \ll_ {\epsilon} \mathrm{N} (\mathfrak {n}) ^ {2 \alpha - 1 / 2 + \epsilon}\tag{4.7}
$$

Moreover, for fixed$g \in \mathrm { S u p p } ( \mu _ { \mathfrak { n } } )$, the inner product$\langle g f _ { 1 } , f _ { 1 } \otimes \chi \rangle$is nonvanishing only if$\chi$is unramified at those places at all places not in$\operatorname { S u p p } ( f _ { 1 } )$and not dividing n. The number of such quadratic characters is$O _ { \epsilon } ( \mathrm { N } ( \mathfrak { n } ) ^ { \epsilon } q ^ { \epsilon } )$, where the implicit constant (as always) is allowed to depend on the base field$F .$. Thus:

$$
\left| \sum_ {\chi^ {2} = 1} \int_ {g} | \langle g \cdot f _ {1}, f _ {1} \otimes \chi \rangle \langle g \cdot f _ {2}, f _ {2} \otimes \chi \rangle | d \mu_ {\mathfrak {n}} (g) \right| \ll_ {\epsilon} q ^ {\epsilon} \mathrm{N} (\mathfrak {n}) ^ {2 \alpha - 1 / 2 + \epsilon}\tag{4.8}
$$

The total variation of σ may be computed:

$$
\| \sigma \| \ll_ {\epsilon} \sum_ {\mathfrak {n}} N (\mathfrak {n}) ^ {1 / 2 + \epsilon} | a _ {\mathfrak {n}} |\tag{4.9}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>11</sup>A</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">X</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f₁∅x</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f2∅x</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">GL<sub>2</sub>(o<sub>Fp</sub> ),</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">GL<sub>2</sub>(o<sub>Fp</sub>)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">GL<sub>2</sub>(o<sub>Fp</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">small caution here is that the vectors f<sub>1</sub> ⊗χ and f<sub>2</sub> ⊗χ need not be invariant by if p|n, because χ may be ramified. However, always fixes the line spanned by either of these vectors, and the bound of (9.1) depends only on the dimension of the )-span of the vectors in question.</span></small>

Using (2.7) to compute$\sigma ^ { ( 2 ) }$, and combining (4.6), (4.7) and (4.9), we conclude: (4.10)

$$
| I (\varphi) | \ll_ {\epsilon} q ^ {\epsilon} \frac {\left(\left(\sum_ {\mathfrak {n}} N (\mathfrak {n}) ^ {1 / 2 + \epsilon} | a _ {\mathfrak {n}} |\right) ^ {2} q ^ {\alpha - 1 / 2} + \sum_ {\mathfrak {n} , \mathfrak {m}} \sum_ {\mathfrak {d} | (\mathfrak {n} , \mathfrak {m})} \left(N \left(\frac {\mathfrak {n m}}{\mathfrak {d} ^ {2}}\right)\right) ^ {2 \alpha - 1 / 2} | a _ {\mathfrak {n}} | | a _ {\mathfrak {m}} |\right) ^ {1 / 2}}{| \sum_ {n} a _ {\mathfrak {n}} \lambda (\mathfrak {n}) |}
$$

The choice of$a _ { \mathfrak { n } }$follows an idea of Iwaniec; we slightly modify the standard choice so that we do not need to appeal to Ramanujan on average. <sup>12</sup> Fix K with $q ^ { 1 / 1 0 0 0 } \leq K \leq q ^ { 1 0 0 0 }$. Let S be the set of prime ideals l such that$\mathrm { N } ( \mathfrak { l } ) \in [ K , 2 K ]$ and l$\not \in \operatorname { S u p p } ( f _ { 1 } ) \cup \operatorname { S u p p } ( f _ { 2 } ) \cup \operatorname { S u p p } ( \varphi )$. In view of the assumptions,$| \dot { S } | \gg K ^ { 1 - \epsilon }$ For$z \in \mathbb { C }$we put sign$( z ) = z / | z |$for$z \neq 0$and$\mathrm { s i g n } ( 0 ) = 1$. Put

$$
a _ {\mathfrak {n}} = \left\{ \begin{array}{l} \overline {{\operatorname{sign} (\lambda (\mathfrak {n}))}}, \mathfrak {n} \in S \\ \overline {{\operatorname{sign} (\lambda (\mathfrak {n} ^ {2}))}}, \mathfrak {n} = \mathfrak {l} ^ {2}, \mathfrak {l} \in S \\ 0, \text {else.} \end{array} \right.\tag{4.11}
$$

Then$\begin{array} { r } { \left| \sum _ { n } a _ { \mathfrak n } \lambda ( \mathfrak n ) \right| \gg _ { \epsilon , F } K ^ { 1 - \epsilon } , ( \sum _ { \mathfrak n } \mathrm { N } ( \mathfrak n ) ^ { 1 / 2 + \epsilon } | a _ { \mathfrak n } | ) \ll _ { \epsilon } K ^ { 2 + \epsilon } } \end{array}$, and

$$
\sum_ {\mathfrak {n}, \mathfrak {m}} \sum_ {\mathfrak {d} | (\mathfrak {n}, \mathfrak {m})} \left(\mathrm{N} \left(\frac {\mathfrak {n m}}{\mathfrak {d} ^ {2}}\right)\right) ^ {2 \alpha - 1 / 2} | a _ {\mathfrak {n}} | | a _ {\mathfrak {m}} | \ll K ^ {4 \alpha + 1}.\tag{4.12}
$$

We deduce from (4.10) that

$$
| I (\varphi) | \ll_ {\epsilon , F} (q K) ^ {\epsilon} \frac {\left(K ^ {4} q ^ {\alpha - 1 / 2} + K ^ {1 + 4 \alpha}\right) ^ {1 / 2}}{K}\tag{4.13}
$$

Taking$K = q ^ { \frac { 1 / 2 - \alpha } { 3 - 4 \alpha } }$, we obtain$| I ( \varphi ) | \ll _ { \epsilon , F } q ^ { \epsilon + { \frac { ( 2 \alpha - 1 / 2 ) ( 1 / 2 - \alpha ) } { 3 - 4 \alpha } } }$

4.2. A technical generalization. For certain applications, we shall require a slight generalization of Prop. 4.1 in which the role of$g \ \mapsto \ f _ { 1 } ( g ) f _ { 2 } ( g a ( [ { \mathfrak { p } } ] ) )$is replaced by$g \mapsto F ( g , g a ( [ { \mathfrak { p } } ] ) )$, where F is a function on$\mathbf { X } \times \mathbf { X }$that is not necessarily of product type. Although the method of proof is identical to Prop. 4.1 the details are slightly more technical; in particular, to state the result we will have need of the adelic Sobolev norms discussed in Sec. 2.9.3. We shall also use the notion of totally nondegenerate for functions on$\mathbf { X } \times \mathbf { X } \colon$see Sec. 2.4.

Proposition 4.2. Suppose${ \cal F } \in C ^ { \infty } ( { \bf X } \times { \bf X } )$is totally nondegenerate. Suppose moreover that there is$b \in \mathbb { R }$with

$$
\prod_ {\mathfrak {q} \in \operatorname{Supp} (F) \cup \operatorname{Supp} (\varphi)} \mathrm{N} (\mathfrak {q}) \leq \mathrm{N} (\mathfrak {p}) ^ {b}\tag{4.14}
$$

Let$\pi$be a cuspidal representation of$\mathrm { P G L _ { 2 } }$over$F _ { z }$, with conductor p, and put $\begin{array} { r } { I ( \varphi ) = \int _ { \mathbf { X } } F ( x , x a ( [ \mathfrak { p } ] ) ) \varphi ( x ) d x , } \end{array}$for$\varphi \in \pi$. Then, for any$p > 4 , d \gg 1$

$$
| I (\varphi) | \ll_ {b, \epsilon} \mathrm{N} (\mathfrak {p}) ^ {- \beta + \epsilon} \| \varphi \| _ {L ^ {2}} S _ {p, d, 2 / p} (F),
$$

where$\begin{array} { r } { \beta = \frac { ( 1 - 2 \alpha ) ( 1 - 4 \alpha ) } { p ( 7 - 4 \alpha ) } } \end{array}$

With Kim’s bound$\alpha = 3 / 2 6$, we obtain$\textstyle { \frac { ( 1 - 2 \alpha ) ( 1 - 4 \alpha ) } { 7 - 4 \alpha } } > 1 / 1 7 .$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>12</sup>The argument that follows was improved by a suggestion of P. Michel.</span></small>

Proof. The proof follows closely the proof of Prop. 4.1; the only diference is that we apply (2.14) (proved in Lem. 9.8) in place of (4.4). Again, we may freely assume that$\| \varphi \| _ { L ^ { 2 } } = 1 ;$; again we put$q = \mathrm { N } ( { \mathfrak { p } } )$

Let notations be as in the proof of Prop. 4.1; in particular,$\sigma$is a signed real measure on$\mathrm { P G L _ { 2 } } ( \mathbb { A } _ { F , f } )$whose support commutes with$\mathrm { P G L _ { 2 } } ( F _ { \mathfrak { p } } )$, and$\lambda \ \in \ \mathbb { C }$ satisfies$\varphi \star \check { \sigma } = \lambda \varphi$. Proceeding as in that proof, and in particular as in (4.3), we obtain:

$$
| \lambda I (\varphi) | ^ {2} \leq \int_ {\mathbf {X}} \int_ {(g, g ^ {\prime}) \in \mathrm{PGL} _ {2} (\mathbb {A} _ {F, f}) ^ {2}} F ((x, x) (g, g) (1, a ([ \mathfrak {p} ]))) \cdot   \overline {{F ((x , x) (g ^ {\prime} , g ^ {\prime}) (1 , a ([ \mathfrak {p} ])))}} d \sigma (g) d \sigma (g ^ {\prime})\tag{4.15}
$$

For any$g , g ^ { \prime } \in \mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$, set$F _ { g , g ^ { \prime } } ( x _ { 1 } , x _ { 2 } ) = F ( ( x _ { 1 } , x _ { 2 } ) ( g , g ) ) \overline { { F ( ( x _ { 1 } , x _ { 2 } ) ( g ^ { \prime } , g ^ { \prime } ) ) } } .$ Then$F _ { g , g ^ { \prime } }$is invariant by$\mathrm { P G L _ { 2 } } ( \mathfrak { o } _ { F _ { \mathfrak { p } } } ) \times \mathrm { P G L _ { 2 } } ( \mathfrak { o } _ { F _ { \mathfrak { p } } } )$for$g , g ^ { \prime } \in \mathrm { s u p p } ( \sigma )$. By Hecke equidistribution in the form of (2.14) (proved in Lem. 9.8) we see that for$p >$ $2 , d \gg 1$

$$
\left| \int_ {\mathbf {X}} F _ {g, g ^ {\prime}} ((x, x) (1, a ([ \mathfrak {p} ]))) d x - \sum_ {\chi^ {2} = 1} \chi (\mathfrak {p}) \int_ {\mathbf {X} \times \mathbf {X}} F _ {g, g ^ {\prime}} (x _ {1}, x _ {2}) \chi (x _ {1}) \chi (x _ {2}) d x _ {1} d x _ {2} \right|   \ll_ {\epsilon} q ^ {(2 \alpha - 1) / p + \epsilon} S _ {p, d} (F _ {g, g ^ {\prime}}).\tag{4.16}
$$

$$
\chi (x)
$$

$$
g \mapsto \chi (\det (g))
$$

$$
\left| \int_ {\mathbf {X} \times \mathbf {X}} F _ {g, g ^ {\prime}} \left(\left(x _ {1}, x _ {2}\right)\right) \chi \left(x _ {1}\right) \chi \left(x _ {2}\right) \right| = \left| \left\langle \left(g ^ {\prime - 1} g, g ^ {\prime - 1} g\right) F, F \otimes (\chi , \chi) \right\rangle_ {L ^ {2} (\mathbf {X} \times \mathbf {X})} \right|
$$

By the basic properties of adelic Sobolev norms ((2.12) and (2.13), proofs in Lem. 8.1 and Lem. 8.2)

$$
\begin{array}{r l} S _ {p, d} (F _ {g, g ^ {\prime}}) := & S _ {p, d, 1 / p} (F _ {g, g ^ {\prime}}) \ll S _ {2 p, d, 1 / p} ((g, g) \cdot F) S _ {2 p, d, 1 / p} ((g ^ {\prime}, g ^ {\prime}) \cdot F) \\ & \leq \| g \| ^ {2 / p} \| g ^ {\prime} \| ^ {2 / p} S _ {2 p, d, 1 / p} (F) ^ {2}. \end{array}\tag{4.17}
$$

Let us remark that the factors$\| g \| ^ { 2 / p }$and$\| g ^ { \prime } \| ^ { 2 / p }$arises in the following way: Lem. 8.2 actually gives a factor$\| ( g , g ) \| ^ { 1 / p } ,$, where the norm$\| \cdot \|$(as in Sec. 2.4) is computed in$\mathrm { P G L _ { 2 } } ( \mathbb { A } _ { F , f } ) ^ { 2 }$; this equals$\| g \| ^ { 1 / p }$where the norm is computed in $\mathrm { P G L _ { 2 } } ( \mathbb { A } _ { F , f } )$

Choose σ as in the proof of Prop. 4.1 (see esp. paragraph before$( 4 . 7 ) )$and choose the coeficients$a _ { \mathfrak { n } }$as in that proof (see (4.11)). In particular,$\lVert \boldsymbol { \sigma } \rVert \ll K ^ { 2 + \epsilon }$ Since$F$is totally nondegenerate, the matrix coeficients$\langle ( g ^ { \prime - 1 } g , g ^ { \prime - 1 } g ) F , F \rangle$satisfy bounds that are of the same quality as in the proof of Prop. 4.1; in particular, as in (4.8):

$$
\sum_ {\chi^ {2} = 1} \int_ {g} | \langle (g, g) F, F \otimes (\chi , \chi) \rangle | d \mu_ {\mathfrak {n}} (g) \ll q ^ {\epsilon} \mathrm{N} (\mathfrak {n}) ^ {2 \alpha - 1 / 2 + \epsilon} \| F \| ^ {2}
$$

Finally$\| g \| \ll _ { \epsilon } K ^ { 2 + \epsilon }$for all$g \in \operatorname { s u p p } ( \sigma )$. Proceeding just as in the previous proof,

$$
| I (\varphi) | \ll_ {\epsilon} (q K) ^ {\epsilon} \frac {\left(K ^ {4} q ^ {(2 \alpha - 1) / p} K ^ {8 / p} S _ {2 p , d , 1 / p} (F) ^ {2} + K ^ {1 + 4 \alpha} \| F \| _ {L ^ {2} (\mathbf {X} \times \mathbf {X})} ^ {2}\right) ^ {1 / 2}}{K}.
$$

Consequently, for any$p > 2 ,$

$$
| I (\varphi) | \ll_ {\epsilon} (q K) ^ {\epsilon} \frac {\left(K ^ {8} q ^ {(2 \alpha - 1) / p} S _ {2 p , d , 1 / p} (F) ^ {2} + K ^ {1 + 4 \alpha} \| F \| _ {L ^ {2}} ^ {2}\right) ^ {1 / 2}}{K}
$$

To conclude, choose$K = q ^ { \frac { 1 - 2 \alpha } { p ( 7 - 4 \alpha ) } }$and replace p by$p / 2$(thus,$\mathrm { e . g . , } p > 2$becomes $p > 4 )$

## 5. Application to L-functions.

We now present the first applications to subconvexity. The rough idea is simply that certain L-functions are expressed as period integrals of the type that are bounded by Prop. 4.1 and Prop. 4.2. There is one significant issue in implementing this (rather evident) idea: namely, the integral representation that we use for Rankin-Selberg and the standard L-functions involve Eisenstein series, which are not in$L ^ { 2 } ;$this causes problems in applying Prop. 4.1!

Thus we need to regularize. Two natural ways of doing this are to replace an Eisenstein series by a “wave-packet”; or to use a suitable form of truncation in the defining integrals. In the present paper we will use the wave-packet technique; in the paper [23] we shall also use truncation.

Let us briefly describe the wave packet technique in a classical language. Roughly speaking we can express the Rankin-Selberg L-function of two classical forms$f , g$ via an integral of the form$\begin{array} { r } { L ( s , f \times g ) = \int _ { z } f ( z ) g ( z ) E ( s , z ) } \end{array}$, for some Eisenstein series$E ( s )$. We now regularize, replacing$E ( s , z )$by a wave packet. Let$h ( s )$be any holomorphic function: then

$$
\int_ {R e (s) = 1 / 2} h (s) L (s, f \times g) d s = \int_ {z} f (z) g (z) \int_ {\Re (s) = 1 / 2} h (s) E (s, z).\tag{5.1}
$$

We wish to eventually recover an upper bound for$L ( 1 / 2 , f \times g ) \ ( \mathrm { s a y } )$from the left-hand side, so we take$h ( s ) = \overline { { L ( 1 - \overline { { s } } , f \times g ) } }$. Then$h ( s ) L ( s , f \times g )$is positive along$\Re ( s ) = 1 / 2$. To apply Prop. 4.1 to the right-hand side of (5.1), we shall moreover need to control the behavior of the regularized Eisenstein series$E _ { h } =$ $\begin{array} { r } { \int _ { \mathfrak { R } ( s ) = 1 / 2 } h ( s ) E ( s , z ) } \end{array}$; this type of analysis is carried out in Sec. 10.2 and Sec. 10.3, the main point being that the divergence of the Eisenstein series comes entirely from the constant term.

It is worth remarking that Iwaniec’s bounds for the L-function near 1 enter rather crucially in this analysis: in efect, we bound$E _ { h }$by an easy argument involving shift of contours; this necessitates that h be estimated on a line$\Re ( s ) = - \varepsilon$, which amounts to estimating$L ( s , f \times g )$for$\Re ( s ) = 1 + \varepsilon$

In what follows we have not attempted to obtain polynomial dependence in all parameters. This is not hard to do — and, at its essence, a statement that one can find analytically suitable test vectors in a Rankin-Selberg integral; but we have not done so here. On the other hand, we give full details of this procedure in the proof of Thm. 6.1 (in which the polynomial dependence is particularly useful for applications).

Theorem 5.1. Let$\pi _ { 1 } , \pi _ { 2 }$be fixed automorphic cuspidal representations of$\mathrm { P G L _ { 2 } }$ over$F ; \mathcal { f } x t \in \mathbb { R }$. Let π be an automorphic cuspidal representation with conductor p, a prime ideal that is prime to the conductors of$\pi _ { 1 }$and$\pi _ { 2 }$.

Then, assuming Hypothesis 11.1:

$$
L (\frac {1}{2}, \pi_ {1} \otimes \pi_ {2} \otimes \pi) \ll_ {\pi_ {\infty}} N (\mathfrak {p}) ^ {1 - \frac {1}{1 3}}\tag{5.2}
$$

and, unconditionally:

(5.3)

$$
| L (\frac {1}{2} + i t, \pi_ {1} \otimes \pi) | ^ {2} \ll_ {\pi_ {\infty}} N (\mathfrak {p}) ^ {1 - \frac {1}{1 0 0}}\tag{5.4}
$$

$$
| L (\frac {1}{2} + i t, \pi) | ^ {4} \ll_ {\pi_ {\infty}} \mathrm{N} (\mathfrak {p}) ^ {1 - \frac {1}{6 0 0}}
$$

In these statements, the notation${ \ll } _ { \pi _ { \infty } }$indicates an implicit constant that depends continuously on the local archimedean representation$\pi _ { \infty }$of$\mathrm { G L _ { 2 } } ( F _ { \infty } )$underlying π.

Note we make no claim about the dependency of the implicit constant on$t , \pi _ { 1 } , \pi _ { 2 } ;$ as remarked above, this dependence could be made polynomial in the conductors, but this would require more careful analysis of the archimedean integrals. <sup>13</sup>

We remark that we have used H.Kim’s bound$\alpha = 3 / 2 6 ;$any value of α less than$1 / 4$would give subconvexity and under Ramanujan one obtains for (5.2) the exponent$5 / 6 .$The exponents for (5.3) and (5.4) can be improved, e.g. the present proof does not take into account the fact that unitary Eisenstein series satisfy Ramanujan!

5.1. Results relating periods and integral representations. For the convenience of the reader, we summarize here the results that relate periods and integral representations (proved in later sections). Roughly speaking, any integral representation for an L-function expresses it as a period integral with certain test vectors belonging to the space of an automorphic cuspidal representation.

A delicate point, which is quite relevant to issues of polynomial dependence in auxiliary parameters, is precisely which test vectors. In principle, the proofs of results about integral representation give explicit test vectors. In practice, it is tedious to extract these explicit test vectors. Our policy throughout this paper is the lazy one: to deduce results, as far as possible, by formal arguments and without choosing explicit test vectors. The price of this is that we will not obtain not quite the L-function, but rather a holomorphic function that difers from the L-function by some harmless factors.

More precisely, the content of the Proposition (Prop. 5.1) that follows is that one can write down an integral representation$I ( s )$for the L-functions of interest, so that:

(1)$I ( 1 / 2 )$is not too much smaller than$L ( 1 / 2 )$– or with$1 / 2$replaced by the point of interest – so that a bound for$I ( 1 / 2 )$gives a bound for$L ( 1 / 2 )$

(2) I(s) is not too much bigger than$L ( s )$for any s. This type of control will be useful in shifting contours.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>13</sup>It is important to note, however, that this is an entirely local problem; it is intended that this will be carried out in a more general context in [23]. Both for applications and to illustrate procedure, we have carried out this type of analysis for the results on subconvexity of character twists in Section 6. Those results are proved with polynomial dependence on all parameters.</span></small>

One might prefer to get$I ( s ) = L ( s )$but we don’t need this stronger statement.

As is discussed at length in Sec. 10, to a Schwarz function$\Psi$on$\mathbb { A } _ { F } ^ { 2 }$is associated a family of Eisenstein series$E _ { \Psi } ( s , g )$on X, which varies meromorphically in the parameter$s \in \mathbb { C }$

Proposition 5.1. Let$s _ { 0 } , t _ { 0 } , t _ { 0 } ^ { \prime } \in \mathbb { C }$. Let$\pi _ { 1 }$be a fixed automorphic cuspidal representation of$\mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$and π an automorphic cuspidal representation of prime conductor${ \mathfrak { p } } ;$assume that the finite conductors$o f \pi , \pi _ { 1 }$are coprime.

Denoting by$\pi _ { \infty }$the representation of$\mathrm { P G L _ { 2 } } ( F _ { \infty } )$corresponding to$\pi ,$suppose that$\mathrm { C o n d } ( \underline { { \pi } } _ { \infty } )$is bounded above; equivalently,$\pi _ { \infty }$belongs to a bounded subset<sup>14</sup> of the dual$\widehat { \mathrm { P G L _ { 2 } } } ( F _ { \infty } )$(in what follows the implicit constants may depend on these bounds).

There exists a fixed finite set  of Schwarz Bruhat functions on$\mathbb { A } _ { F } ^ { 2 }$and a real number$C > 0$so that:

There exist vectors$\varphi _ { 1 } \in \pi _ { 1 } , \varphi \in \pi$and$\Psi \in { \mathcal { F } }$so that

$$
\Phi (s) := \mathrm{N} (\mathfrak {p}) ^ {1 - s} \frac {\int_ {\mathbf {X}} \varphi (g) \varphi_ {1} (g a ([ \mathfrak {p} ])) E _ {\Psi} (s , g) d g}{\Lambda (s , \pi_ {1} \otimes \pi)}
$$

is holomorphic and satisfies:

(1)$| \Phi ( s _ { 0 } ) | \gg 1$and$| \Phi ( s ) | \ll C ^ { | \Re ( s ) | } ( 1 + | s | ) ^ { C } ;$

(2) At any nonarchimedean place v such that$\pi _ { 1 }$is unramified,$\Psi _ { v }$is invariant by${ \mathrm { P G L } } _ { 2 } { \left( \mathfrak { o } _ { F _ { v } } \right) } ,$; at any nonarchimedean place v such that$\pi _ { 1 }$and π are both unramified, ϕ, ϕ<sub>1</sub> are both invariant by$\mathrm { P G L } _ { 2 } ( \pmb { \mathscr { o } } _ { F _ { v } } )$

(3)$\| \varphi _ { 1 } \| _ { L ^ { \infty } } \ll 1$and$\| \varphi \| _ { L ^ { 2 } ( \mathbf { X } ) } \ll _ { \epsilon } \mathrm { N } ( \mathfrak { p } ) ^ { \epsilon }$

Moreover, there exist vectors$\varphi \in \pi , \Psi _ { 1 } , \Psi _ { 2 } \in \mathcal { F }$so that:

$$
\Phi (t, t ^ {\prime}) = \mathrm{N} (\mathfrak {p}) ^ {1 / 2 - t} \frac {\int_ {\mathbf {X}} \varphi (g) E _ {\Psi_ {1}} (g , \frac {1}{2} + t) E _ {\Psi_ {2}} (g a ([ \mathfrak {p} ]) , \frac {1}{2} + t ^ {\prime}) d g}{\Lambda (\frac {1}{2} + t + t ^ {\prime} , \pi) \Lambda (\frac {1}{2} + t - t ^ {\prime} , \pi)}\tag{5.5}
$$

is holomorphic and satisfies:

$$
\left| \Phi \left(t _ {0}, t _ {0} ^ {\prime}\right) \right| \gg 1 a n d \left| \Phi \left(t, t ^ {\prime}\right) \right| \ll C ^ {| \Re (t) | + C | \Re \left(t ^ {\prime}\right) |} \left(1 + | t | + | t ^ {\prime} |\right) ^ {C}.
$$

(2) For any nonarchimedean place$v ,$each$\Psi _ { 1 }$and$\Psi _ { 2 }$is invariant by$\mathrm { P G L } _ { 2 } ( \mathfrak { o } _ { F _ { v } } ) _ { \mathrm { ~ } }$ for each place at which$\pi$is unramified, the same is true of$\varphi$.

<sup>(3)</sup> k<sup>ϕ</sup>k$L ^ { 2 } ( \mathbf { X } ) \ll _ { \epsilon } \mathrm { N } ( \mathfrak { p } ) ^ { \epsilon }$

Proof. Lem. 11.4 and Lem. 11.5.

In efect, we could achieve$\mathbf { \hat { \Phi } } ^ { \mathrm { 6 } } \Phi = 1 \mathbf { \vec { \rho } } ^ { \mathrm { 5 } }$in Prop. 5.1 by a more careful choice of local data; but this is irrelevant for the purpose of global estimation.

## 5.2. Proof of Thm. 5.1.

Proof. (of (5.2)). It follows from Hypothesis 11.1 and Proposition 4.1.

Proof. (of (5.3)). The basic idea is that the Rankin-Selberg convolution is a triple product, with one factor being an Eisenstein series. However, one cannot naively apply Prop. 4.1 since Eisenstein series do not belong to$L ^ { 4 } ( \mathbf { X } )$. To avoid this, we will use a wave-packet of Eisenstein series.

First, we can assume from the start that$\pi _ { \infty }$belongs to a bounded subset of the dual$\operatorname { P G L } _ { 2 } ( { \widehat { F } } _ { \infty } )$. The implicit constants in the proof that follow depend on this subset. We denote by Λ the completed L-function. We begin by remarking that since$\mathrm { N } ( { \mathfrak { p } } ) \to \infty$we may assume that$\pi _ { 1 }$is not isomorphic to$\pi ,$or to any quadratic twist of$\pi .$. In particular, we are free to assume that$\Lambda ( s , \pi _ { 1 } \otimes \pi )$has no poles. Moreover, the finite conductor of$\Lambda ( s , \pi _ { 1 } \otimes \pi )$difers from$\mathrm { { N } } ( { \mathfrak { p } } ) ^ { 2 }$by an absolutely bounded constant.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>14</sup>See Section 2.12.3 for definition</span></small>

Fixing$t _ { 0 } \in \mathbb { R }$, let$\Psi , \varphi , \varphi _ { 1 } , E _ { \Psi } ( g , s )$, Φ be as in Prop. 5.1 with$s _ { 0 } = 1 / 2 + i t _ { 0 }$ so that$| \Phi ( 1 / 2 + i t _ { 0 } ) | \gg 1$. For simplicity we write simply$E ( g , s )$for$E _ { \Psi } ( g , s )$ Fix$\kappa > 0$. In the rest of the proof we omit the subscript$\kappa , \epsilon$from$\ll$, with the understanding that all implicit constants depend on κ and ǫ. Put

$$
I (s) = \mathrm{N} (\mathfrak {p}) ^ {s - 1} \Lambda (s, \pi_ {1} \otimes \pi) \Phi (s) = \int_ {\mathbf {X}} \varphi_ {1} (g a ([ \mathfrak {p} ])) E (s, g) \varphi (g) d g
$$

From Iwaniec’s upper bounds for L-functions [15, Chapter$8 ]$, the functional equation for$\Lambda _ { ; }$, and the bounds on Φ furnished by Prop. 5.1,

$$
| I (1 + \kappa + i t) | \ll (1 + | t |) ^ {- 4} \mathrm{N} (\mathfrak {p}) ^ {\kappa + \epsilon}, | I (- \kappa + i t) | \ll (1 + | t |) ^ {- 4} \mathrm{N} (\mathfrak {p}) ^ {\kappa + \epsilon}.\tag{5.6}
$$

Put$\begin{array} { r } { h ( s ) = s ( 1 - s ) ( s - \frac { 1 } { 2 } ) ^ { 2 } \overline { { I ( 1 - \overline { { s } } ) } } } \end{array}$. Then$h ( s )$is holomorphic in$- \kappa \leq \Re ( s ) \leq$ $1 + \kappa$and$h ( \textstyle { \frac { 1 } { 2 } } ) = 0 . ^ { 1 5 }$Moreover$h ( s )$has rapid decay as$\Im ( s )  \infty$, in view of the Γ-factors of the completed L-function. Put$\begin{array} { r } { E _ { h } ( g ) = \int _ { \mathfrak { R } ( s ) = 1 + \kappa } h ( s ) E ( s , g ) } \end{array}$. It is proved in Lem. 10.6 that, for such$\begin{array} { r } { h , \| E _ { h } ( g ) \| _ { L ^ { \infty } } \ll \int _ { - \infty } ^ { \infty } \left( | h ( - \kappa + i t ) | + | h ( 1 + \kappa + i t ) | \right) d t . } \end{array}$ Applying (5.6), we conclude that$\| E _ { h } ( g ) \| _ { L ^ { \infty } } \ll \mathrm { N } ( \mathfrak { p } ) ^ { \kappa + \epsilon }$

On the other hand, we see from the definition of$I ( s )$that

$$
\int_ {\Re (s) = 1 + \kappa} h (s) I (s) = \int_ {\Re (s) = 1 + \kappa} h (s) d s \int_ {\mathbf {X}} \varphi_ {1} (g a ([ \mathfrak {p} ])) E (s, g) \varphi (g) d g.\tag{5.7}
$$

The double integral on the right hand side of (5.7) is absolutely convergent and orders may be switched; thus

$$
\int_ {\Re (s) = 1 + \kappa} h (s) I (s) = \int_ {\mathbf {X}} \varphi_ {1} (g a ([ \mathfrak {p} ])) E _ {h} (g) \varphi (g) d g = \int_ {\mathbf {X}} \varphi_ {1} (g a ([ \mathfrak {p} ])) E _ {h} ^ {0} (g) \varphi (g) d g,
$$

where$E _ { h } ^ { 0 } : = \mathcal { P } ( E _ { h } )$is totally nondegenerate (see Section 2.7) and satisfies$\| E _ { h } ^ { 0 } \| _ { L ^ { \infty } } \ll _ { \epsilon }$ǫ $\mathrm { N } ( \mathfrak { p } ) ^ { \kappa + \epsilon }$

We then deduce from Prop. 4.1 that:

$$
\left| \int_ {\Re (s) = 1 + \kappa} h (s) I (s) \right| \ll \| \varphi_ {1} \| _ {L ^ {4} (\mathbf {X})} \mathrm{N} (\mathfrak {p}) ^ {- \frac {1}{2 6} + \kappa + \epsilon}\tag{5.8}
$$

$I ( s )$and$h ( s )$both decay exponentially rapidly as$\Im ( s )  \infty$. It is therefore simple to justify shifting the line of integration in (5.8) to$\Re ( s ) = 1 / 2$. We deduce thereby that

$$
\left| \int_ {\Re (s) = \frac {1}{2}} t ^ {2} | I (\frac {1}{2} + i t) | ^ {2} d t \right| \ll \| \varphi_ {1} \| _ {L ^ {4} (\mathbf {X})} N (\mathfrak {p}) ^ {\kappa - \frac {1}{2 6} + \epsilon}.\tag{5.9}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">h(1/2) = 0</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">t ∈ R.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Fix,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sub>g</sub> |L( <sup>1</sup> + it, f ⊗ g)|<sup>2</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">N</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">g(N)<sup>3</sup>.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">h(1/2) = 0</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">N</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">t = 0,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">t 6= 0,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>15</sup> The fact that we impose h(1/2) = 0 has a very concrete meaning in classical terms. Fix, for example, a form and  Consider  where the sum is taken over a basis of holomorphic Hecke eigenforms of level  and trivial Nebentypus. If  this has the asymptotic behaviour N lo On the other hand, if it behaves like  ForcingN log(N). “counteracts” this extra singularity.</span></small>

From (5.6) we deduce bounds on I and I′ inside the strip$0 \leq \Re ( s ) \leq 1$by the maximal modulus principle. In particular,

$$
| I ^ {\prime} (\frac {1}{2} + i t) | \ll_ {t} N (\mathfrak {p}) ^ {\kappa + \epsilon}.\tag{5.10}
$$

Combining (5.9) and (5.10), and recalling that κ is arbitrary, we obtain$\lvert I ( 1 / 2 +$ $i t ) | \ll _ { t } \mathrm { N } ( \mathfrak { p } ) ^ { \frac { 1 } { 5 \cdot 2 6 } + \epsilon }$. Thus$\begin{array} { r } { | \Lambda ( \frac { 1 } { 2 } + i t _ { 0 } , \pi _ { 1 } \otimes \pi ) | \ll _ { \epsilon , t } \mathrm { N } ( \mathfrak { p } ) ^ { \frac { 1 } { 2 } - \frac { 1 } { 1 3 0 } + \epsilon } } \end{array}$

Proof. (of (5.4).) The proof is similar to that of (5.3), but a slightly more elaborate regularization is required, since we shall proceed from the expression (5.5) of$L ( s , \pi )$ as a triple product against two Eisenstein series. Again we may assume from the start that$\pi _ { \infty }$is confined to a bounded subset of$\widehat { \mathrm { G L _ { 2 } } } ( \widehat { F _ { \infty } } )$; the implicit constants will, again, depend on this subset.

Let$\Lambda ( s , \pi )$be the completed L-function attached to π. Fixing$t _ { 0 } , t _ { 0 } ^ { \prime } \in i \mathbb { R }$, Prop. 5.1 gives the existence of Eisenstein series$E _ { \Psi _ { 1 } } ( g , s ) = E _ { 1 } ( g , s ) , E _ { \Psi _ { 2 } } ( g , s ) = E _ { 2 } ( g , s )$ on$\mathbf { X } .$, and$\varphi \in \pi$so that

$$
\Phi (t, t ^ {\prime}) := \mathrm{N} (\mathfrak {p}) ^ {1 / 2 - t} \frac {\int_ {\mathbf {X}} \varphi (g) E _ {1} (g , \frac {1}{2} + t) E _ {2} (g a ([ \mathfrak {p} ]) , \frac {1}{2} + t ^ {\prime}) d g}{\Lambda (\frac {1}{2} + t + t ^ {\prime} , \pi) \Lambda (\frac {1}{2} + t - t ^ {\prime} , \pi)}
$$

satisfies$| \Phi ( t _ { 0 } , t _ { 0 } ^ { \prime } ) | \gg 1$and$\Phi ( t , t ^ { \prime } ) \ll C ^ { | \Re ( t ) | + | \Re ( t ^ { \prime } ) | } ( 1 + | t | + | t | ^ { \prime } | ) ^ { C }$

We put

$$
\begin{array}{c} I (z _ {1}, z _ {2}) = \Phi (z _ {1}, z _ {2}) \mathrm{N} (\mathfrak {p}) ^ {z _ {1} - 1 / 2} \Lambda (\frac {1}{2} + z _ {1} + z _ {2}, \pi) \Lambda (\frac {1}{2} + z _ {1} - z _ {2}) \\ = \Phi (z _ {1}, z _ {2}) \mathrm{N} (\mathfrak {p}) ^ {\frac {z _ {1} + z _ {2}}{2} - 1 / 4} \Lambda (\frac {1}{2} + z _ {1} + z _ {2}, \pi) \mathrm{N} (\mathfrak {p}) ^ {\frac {z _ {1} - z _ {2}}{2} - 1 / 4} \Lambda (\frac {1}{2} + z _ {1} - z _ {2}, \pi) \end{array}\tag{5.11}
$$

Then$I ( z _ { 1 } , z _ { 2 } )$is a holomorphic function of$( z _ { 1 } , z _ { 2 } ) \in \mathbb { C } ^ { 2 } . \ I ( z _ { 1 } , z _ { 2 } )$has rapid decay along “vertical lines”, that is, for$\sigma , \sigma ^ { \prime }$in a fixed compact set and$( t , t ^ { \prime } ) \in \mathbb { R }$we have$I ( \sigma + i t , \sigma ^ { \prime } + i t ^ { \prime } ) \ll _ { N } ( 1 + | t | + | t ^ { \prime } | ) ^ { - N }$

Let$\kappa > 0$be fixed. From (5.11), Iwaniec’s bounds for L-functions near 1, and the rapid decay of I along “vertical lines,” we obtain by the maximal modulus principle:

$$
(1 + | z _ {1} | + | z _ {2} |) ^ {N} \max (| I (z _ {1}, z _ {2}) |, | \partial_ {1} I (z _ {1}, z _ {2}) |, | \partial_ {2} I (z _ {1}, z _ {2}) |) \ll_ {N} N (\mathfrak {p}) ^ {\kappa}, | \Re (z _ {1}) | + | \Re (z _ {2}) | \leq 1 / 2 + \kappa ,
$$

where$\partial _ { 1 } \ ( \mathrm { r e s p . } \ \partial _ { 2 } )$is the operator of diferentiation w.r.t.$z _ { 1 } \ ( \mathrm { r e s p . } \ z _ { 2 } )$. Put

$$
h (z _ {1}, z _ {2}) = z _ {1} ^ {2} z _ {2} ^ {2} (1 / 4 - z _ {1} ^ {2}) (1 / 4 - z _ {2} ^ {2}) \overline {{I (- \overline {{z _ {1}}} , - \overline {{z _ {2}}})}}.\tag{5.12}
$$

Then, in the notation of Sec. 10.3 (esp. Def. 10.1) , h belongs to the space$\mathcal { H } ^ { ( 2 ) } ( \kappa )$ and satisfies$\| h \| _ { N } \ll _ { N } \mathrm { N } ( \mathfrak { p } ) ^ { \kappa }$

Put$\begin{array} { r } { I = \int _ { \Re ( z _ { 1 } ) = \Re ( z _ { 2 } ) = 0 } h ( z _ { 1 } , z _ { 2 } ) I ( z _ { 1 } , z _ { 2 } ) d z _ { 1 } d z _ { 2 } } \end{array}$. Then:

$$
\begin{array}{c} I = \int_ {\Re (z _ {1}) = 0, \Re (z _ {2}) = 0} h (z _ {1}, z _ {2}) d z _ {1} d z _ {2} \int_ {\mathbf {X}} \varphi (g) E _ {1} (g, 1 / 2 + z _ {1}) E _ {2} (g a ([ \mathfrak {p} ]), 1 / 2 + z _ {2}) d g \\ = \int_ {\mathbf {X}} \varphi (x) E _ {h} ((x, x) (1, a ([ \mathfrak {p} ]))) d x \end{array}\tag{5.13}
$$

where the function$E _ { h }$on$\mathbf { X } \times \mathbf { X }$is defined by

$$
E _ {h} (g _ {1}, g _ {2}) = \int_ {\Re (z _ {1}) = 0, \Re (z _ {2}) = 0} h (z _ {1}, z _ {2}) E _ {1} (g _ {1}, 1 / 2 + z _ {1}) E _ {2} (g _ {2}, 1 / 2 + z _ {2}),
$$

and the interchange of orders is justified by the (easily verified) absolute convergence of the double integral defining I. Note that$E _ { h } ( g _ { 1 } , g _ { 2 } )$is totally nondegenerate (see Section 2.7 for definition). We now apply Prop. 4.2 to conclude that$| I | \ll _ { p , d }$ $S _ { p , d , 2 / p } ( E _ { h } ) \| \varphi \| _ { L ^ { 2 } } \mathrm { N } ( \mathfrak { p } ) ^ { - \frac { 1 } { 1 7 p } }$for any$p > 4 , d \gg 1$. We note at this point that the requirement$p > 4$makes it critical that the regularized Eisenstein series$E _ { h }$belong to$L ^ { 4 } ;$the trivial fact that Eisenstein series belong to$L ^ { 2 - \epsilon }$is far from suficient.

On the other hand, by Lem. 10.9,$S _ { p , d , 2 / p } ( E _ { h } ) \ll \| h \| _ { N }$for some$N$, possibly depending on$p , d .$By Prop. 5.1,$\| \varphi \| _ { L ^ { 2 } } \ll _ { \epsilon } \mathrm { N } ( \mathfrak { p } ) ^ { \epsilon }$

Thus$\begin{array} { r } { | I | \ll _ { \epsilon } \ N ( \mathfrak { p } ) ^ { \epsilon - 1 / 6 8 } } \end{array}$. Now, by the definition of h (5.12) we have$I \ =$ $\begin{array} { r } { \mathrm { N } ( \mathfrak { p } ) ^ { - 1 } \int _ { ( t , t ^ { \prime } ) \in \mathbb { R } ^ { 2 } } ( 1 / 4 + t _ { 1 } ^ { 2 } ) ( 1 / 4 + t _ { 2 } ^ { 2 } ) t _ { 1 } ^ { 2 } t _ { 2 } ^ { 2 } | I ( i t _ { 1 } , i t _ { 2 } ) | ^ { 2 } d t _ { 1 } d t _ { 2 } } \end{array}$. Thus we obtain:

$$
\int_ {(t, t ^ {\prime}) \in \mathbb {R} ^ {2}} | I (i t _ {1}, i t _ {2}) | ^ {2} t _ {1} ^ {2} t _ {2} ^ {2} d t _ {1} d t _ {2} \ll_ {\epsilon} \mathrm{N} (\mathfrak {p}) ^ {1 - 1 / 6 8 + \epsilon}.\tag{5.14}
$$

Using (5.14), and the given properties of Φ, we deduce that$\begin{array} { r } { | \Lambda ( \frac { 1 } { 2 } + t _ { 0 } + t _ { 0 } ^ { \prime } ) \Lambda ( \frac { 1 } { 2 } + } \end{array}$ $t _ { 0 } - t _ { 0 } ^ { \prime } ) | ^ { 2 } \ll _ { t _ { 0 } , t _ { 0 } ^ { \prime } } \mathrm { N } ( \mathfrak { p } ) ^ { 1 - 1 / 6 0 0 }$in a similar fashion to the conclusion of the proof of (5.3). We take$t _ { 0 } ^ { \prime } = 0$to conclude.

## 6. Torus periods (I): subconvex bounds for character twists over a number field.

In this section we shall work in considerable generality; we shall derive subconvex bounds without any assumptions of prime or squarefree conductor, and obtaining polynomial dependence in all auxiliary parameters. This is useful for applications, but will involve some notational overhead. As a result, we have sacrificed good exponents for simplicity at many steps.

Theorem 6.1. Let π be a (unitary) cuspidal representation of${ \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$, and$\chi \textit { a }$ unitary character of$\mathbb { A } _ { F } ^ { \times } / F ^ { \times }$, with finite conductor f. Then there is$N > 0$such that

(6.1)

$$
L (\frac {1}{2}, \pi \times \chi) \ll \mathrm{Cond} (\pi) ^ {N} \mathrm{Cond} _ {\infty} (\chi) ^ {N} \mathrm{N} (\mathfrak {f}) ^ {1 / 2 - \frac {1}{2 4}},\tag{6.2}
$$

$$
L (\frac {1}{2}, \chi) \ll \mathrm{Cond} _ {\infty} (\chi) ^ {N} \mathrm{N} (\mathfrak {f}) ^ {1 / 4 - \frac {1}{2 0 0}}
$$

Note that the result also implies a corresponding statement for the L-functions evaluated at$\begin{array} { r } { \frac { 1 } { 2 } + i t } \end{array}$, since one may replace$\chi$by$\chi | \cdot | ^ { i t }$

Since it is perhaps hidden in the proof where the polynomial dependence on conductor arises, we would like to explicate it now. If$\pi$is an automorphic cuspidal representation with analytic conductor Cond(π), there exists a vector$\psi \in \pi$with Sobolev norms$S _ { 2 , d , \beta } ( \psi ) \ll \mathrm { C o n d } ( \pi ) ^ { \mathrm { c o n s t } \operatorname* { m a x } ( \dot { \beta } , d ) }$. Moreover, one can choose such a$\psi$to be$\mathrm { ~ a ~ } \ \mathrm  \text' { g o o d } \mathrm  \text' { }$test vector w.r.t. certain toral periods. Thus the analytic conductor enters precisely through the minimal Sobolev norm of a suitable vector belonging to the space of π. We note that the test vectors we choose are smooth but not K-finite at infinite places; this idea has been heavily exploited in the previous work of Bernstein and Reznikov.

Note that some cases of Thm. 6.1 – where π has trivial central character and π is quadratic – are subsumed by the previous result Thm. 5.1. Nevertheless, we have chosen to give a distinct presentation since the method is entirely diferent, it is simpler in the present method to deal with the case of noncuspidal π. Also, we shall consistently deal in the present section with${ \mathrm { G L } } ( 2 )$, rather than$\mathrm { P G L _ { 2 } }$. Thus ω will be a unitary character of$\mathbb { A } _ { F } ^ { \times } / F ^ { \times }$, and$C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathrm { G L } ( 2 ) } )$the space of functions on$\begin{array} { r } { \mathbf { X } _ { \mathrm { G L } ( 2 ) } = \mathrm { G L } _ { 2 } ( F ) \backslash \mathrm { G L } _ { 2 } ( \mathbb { A } _ { F } ) } \end{array}$with central character ω.

In the case$F = \mathbb { Q }$, the subconvexity result (6.2) for characters is due to Burgess. Burgess’ method gives a much better exponent; of course there is considerable scope for improvement in the present technique also.

For the ease of the reader, we briefly explain in advance the points of our proof in classical language. The discussion that follows is not a completely faithful rendition of the proof, but it hopefully conveys the main ideas. While it follows the pattern of all the proofs in this paper, one minor complication is that we deal with integrals w.r.t. certain measures of infinite mass.

(1) If f is a Maass form on$\operatorname { S L _ { 2 } } ( \mathbb { Z } ) \backslash \mathbb { H }$, the integral

$$
\frac {1}{q} \int_ {y = 0} ^ {\infty} \sum_ {x = 1} ^ {q} \chi (x) f (\frac {x}{q} + i y) \frac {d y}{y}\tag{6.3}
$$

equals, up to some Γ-factors,$\begin{array} { r } { { \frac { 1 } { \sqrt { q } } } L ( { \frac { 1 } { 2 } } , f \times \chi ) } \end{array}$. This is an exercise in Hecke-Jacquet-Langlands theory. The version of this equality that we shall use is proved in Lem. 11.8 when$f$is a cusp form and Lem. 11.10 when$f$is Eisenstein.

(2) It will then sufice to bound$\textstyle \sum _ { x = 1 } ^ { q } \chi ( x ) f ( { \frac { x } { q } } + i y )$for each fixed value of$y .$ As it turns out, the crucial range of y is around$y = q ^ { - 1 }$; the contribution of other ys are small for relatively trivial reasons (use the Fourier expansion). This is roughly a geometric form of the approximate functional equation: it says that the Fourier coeficients$a _ { n } ( f )$with$n \asymp q$are most important to determining the L-function. The general version of this fact is proven in Lem. 11.9.

(3) In the range when$y \asymp q ^ { - 1 }$, the set$\textstyle { \left\{ { \frac { x } { q } } + i y \right\} } _ { \left\{ 1 \leq x \leq q - 1 \right\} }$is roughly equidistributed, because it is (with the exception of two points) the orbit of$i q y \in \mathbb { H }$ by the qth Hecke operator. This is easy to quantify and actually can be regarded as a statement about equidistribution of p-adic horocycles.The general version of this is proved in Lem. 9.10.

(4) We are now in a situation where we are trying to bound the period of$f$ along the roughly equidistributed set$\textstyle { \left\{ { \frac { x } { q } } + i y \right\} } _ { \left\{ 1 \leq x \leq q - 1 \right\} }$. To do this, we apply mixing properties of the adelic torus flow, in the same fashion as the previous proofs of this paper. This shows that$\textstyle \sum _ { x = 1 } ^ { q } \chi ( x ) f ( { \frac { x } { q } } + i y )$is small.

The computations that underlie steps (1), (2) and (3) are fairly routine but technically complicated. We have therefore carried them out in Sec. 11.4. In the sections that follow, we merely quote the results and carry out what amounts to step (4).

6.1. Relating integral representations and periods. Let$z \in \mathbb { R }$and let$\mu _ { z } , \nu _ { z } , \mu , \nu$ be the measures on$\mathbf { X } _ { \mathrm { G L } ( 2 ) }$defined by

$$
\begin{array}{c} \mu_ {z} (f) = \int_ {| y | = z} f (a (y) n ([ \mathfrak {f} ])) \chi (y) d ^ {\times} y, \mu = \int_ {z \in \mathbb {R} ^ {\times}} \mu_ {z} d ^ {\times} z, \\ \nu_ {z} (f) = \int_ {| y | = z} f (a (y) n ([ \mathfrak {f} ])) d ^ {\times} y, \nu = \int_ {z \in \mathbb {R} ^ {\times}} \nu_ {z} d ^ {\times} z. \end{array}\tag{6.4}
$$

In both cases, the measure$d ^ { \times } y$is the probability measure invariant by$\mathbb { A } _ { F } ^ { 1 } / F ^ { \times }$and the measure$d ^ { \times } z$is a Haar measure on$\mathbb { R } ^ { \times }$. Thus$\mu _ { z } , \nu _ { z }$are probability measures, whereas$\mu , \nu$have infinite mass. It is simple to see that the integrals defining $\mu ( f ) , \nu ( f )$converge absolutely if$f$is a function decaying rapidly enough at the cusps, e.g. satisfying$| f ( x ) | \ll \mathrm { h t } ( x ) ^ { - \varepsilon }$(notation of Sec. 8.2), for any$\varepsilon > 0$ Note also the analogy between these measures and those used in the analysis of unipotent periods (cf. (3.2).) Classically,$\nu _ { z } ( f )$should be thought of the measure on$\operatorname { S L _ { 2 } } ( \mathbb { Z } ) \backslash$H defined by$\begin{array} { r } { \sum _ { 0 \leq x \leq q - 1 } f ( \frac { x } { q } + i z ) } \end{array}$, and$\mu _ { z } ( f )$the measure on$\operatorname { S L _ { 2 } } ( \mathbb { Z } ) \backslash$H defined by$\begin{array} { r } { \sum _ { 0 \leq x \leq q - 1 } f ( \frac { x } { q } + \overline { { i z ) } } \overline { { \chi } } ( x ) } \end{array}$. (These statements are not to be interpreted precisely; they are for intuition only).

Here is the Proposition that formalizes (1) and (2) of the discussion above, in the cuspidal case.

Proposition 6.1. Let π be a cuspidal representation on${ \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$, χ a character of$\mathbb { A } _ { F } ^ { \times } / F ^ { \times }$of finite conductor f. Write$\begin{array} { r } { L _ { u n r } ( s , \pi \times \chi ) = \prod _ { \chi , \mathrm { u n r a m . } } L _ { v } ( s , \pi \times \chi ) } \end{array}$ where the product is taken over all finite places at which χ is not ramified.

Let$d , \beta \geq 0$. Let$g _ { + } , g _ { - }$be positive smooth functions on$\mathbb { R } _ { \geq 0 }$such that$g _ { + } + g _ { - } =$ $1 , g _ { + } ( t ) = 1 f o r t \ge 2$and$g _ { - } ( t ) = 1$for all$t \leq 1 / 2$

Then there exists$\varphi \in \pi$such that, with

$$
\Phi (s) = \mathrm{N} (\mathfrak {f}) ^ {1 / 2} \frac {\int_ {z} \mu_ {z} (\varphi) | z | ^ {s - 1 / 2} d ^ {\times} z}{L _ {u n r} (s , \pi \times \chi)}\tag{6.5}
$$

then$\Phi ( s )$is holomorphic and satisfies:

(1)$| \Phi ( s ) | \ll _ { \mathfrak { R } ( s ) , \epsilon } \mathrm { N } ( \mathfrak { f } ) ^ { \epsilon }$and$| \Phi (  { { \frac { 1 } { 2 } } } ) | \gg _ { \epsilon } \mathrm { N } ( \mathfrak { f } ) ^ { - \epsilon }$

(2) ϕ is new at every finite place (i.e., for each finite prime q it is invariant by $K _ { 0 } [ \mathfrak { q } ^ { s _ { \mathfrak { q } } } ]$, where$s _ { \mathfrak { q } }$is the local conductor of π).

(3) The Sobolev norms of ϕ satisfy the bounds

$$
S _ {2, d, \beta} (\varphi) \ll_ {\epsilon} \operatorname{Cond} _ {\infty} (\pi) ^ {2 d + \epsilon} \operatorname{Cond} _ {f} (\pi) ^ {\beta + \epsilon} \operatorname{Cond} _ {\infty} (\chi) ^ {1 / 2 + 2 d}\tag{6.6}
$$

(4) The integration of (6.5) may be “truncated without significant change” to the region z around$\mathrm { { N } } ( \mathfrak { f } ) ^ { - 1 }$; more formally:

$$
\left| \int_ {z} \mu_ {z} (\varphi) g _ {+} (z / T) d ^ {\times} z \right| \ll (\mathrm{N} (\mathfrak {f}) T) ^ {- 1 / 2} (T \mathrm{Cond} (\pi) \mathrm{Cond} (\chi)) ^ {\epsilon}
$$

$$
\left| \int_ {z} \mu_ {z} (\varphi) g _ {-} (z / T) d ^ {\times} z \right| \ll (\mathrm{N} (\mathfrak {f}) T) ^ {1 / 2} (T \operatorname{Cond} (\chi)) ^ {\epsilon} (\operatorname{Cond} _ {\infty} (\chi) \operatorname{Cond} (\pi)) ^ {1 + \epsilon}
$$

Proof. Lem. 11.8 and Lem. 11.9.

We next give the corresponding result for the “noncuspidal case.” We recall that the Eisenstein series$E _ { \Psi } ( s , g )$associated to a Schwarz function Ψ on$\mathbb { A } _ { F } ^ { 2 }$are discussed in Sec. 10. The normalization is so that the functional equation interchanges s and$1 - s . \bar { E } ( s , g )$denotes, as explained in that section (cf. (10.9)) the truncated Eisenstein series obtained by subtracting the constant term; it is a function on$B ( F ) \backslash { \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$

Proposition 6.2. Let$s _ { 0 } , s _ { 0 } ^ { \prime } \in \mathbb { C }$, and suppose that$\chi$is ramified at at least one finite place. Let$g _ { \pm }$be as in Prop. 6.1. There is an absolute$C > 0 \ ( i . e .$. depending only on$F )$and a choice of$K _ { \mathrm { m a x } }$-invariant Schwarz function Ψ (depending on$\chi )$ so that if we put

$$
\Phi (s, s ^ {\prime}) := \mathrm{N} (\mathfrak {f}) ^ {1 / 2} \frac {\int_ {y \in \mathbb {A} _ {F} ^ {\times} / F ^ {\times}} \bar {E} _ {\Psi} (s , a (y) n ([ \mathfrak {f} ])) \chi (y) | y | ^ {s ^ {\prime}} d ^ {\times} y}{L (\chi , s + s ^ {\prime}) L (\chi , 1 - s + s ^ {\prime})}
$$

where$\bar { E }$is defined as in$( \boldsymbol { { 1 0 . 9 } } )$, then the integral defining Φ is absolutely convergent when$\Re ( s ) , \Re ( s ^ { \prime } ) \gg 1$. Moreover, Φ extends from$\Re ( s ) , \Re ( s ^ { \prime } ) \gg 1$to a holomorphic function on$\mathbb { C } ^ { 2 }$, satisfying

$$
(1) | \Phi (s _ {0}, s _ {0} ^ {\prime}) | \gg 1 a n d | \Phi (s, s ^ {\prime}) | \ll C ^ {1 + | \Re (s) | + | \Re (s ^ {\prime}) |} (1 + | s | + | s ^ {\prime} |) ^ {C}.
$$

Moreover, given$N > 0$we have that

$$
| \Phi (s, s ^ {\prime}) | (1 + | s | + | s ^ {\prime} |) ^ {N} \ll_ {\Re (s), \Re (s ^ {\prime}), N} \mathrm{Cond} _ {\infty} (\chi) ^ {N ^ {\prime}}\tag{6.7}
$$

where$N ^ { \prime }$and the implicit constant may be taken to depend continuously on $N , \Re ( s ) , \Re ( s ^ { \prime } )$

(2) Ψ, and so also$E _ { \Psi } ( s , g )$is invariant by$K _ { \mathrm { m a x } } ;$

(3) Let$h \in { \mathcal { H } } ( \kappa )$be as in$( 1 0 . 1 8 )$, and put$\begin{array} { r } { E _ { h } : = \int _ { \mathfrak { R } ( s ) \gg 1 } h ( s ) E _ { \Psi } ( s , g ) d g . } \end{array}$ Then, for each$d , \beta$, there is$N > 0$such that$S _ { \infty , d , \beta } ( E _ { h } ) \ll _ { \kappa } \| h \| _ { 0 } \mathrm { C o n d } _ { \infty } ( \chi ) ^ { N }$ where the norm$\| h \| _ { 0 }$is defined in$( 1 0 . 1 8 )$

(4) We have$\mu _ { z } ( E _ { h } ) \ll _ { K , \Psi , h }$min$( \vert z \vert ^ { K } , \vert z \vert ^ { - K } )$for$e a c h ^ { 1 6 } \ K \ \ge \ 1$. Moreover, there is$N > 0$such that

$$
\left| \int_ {z} \mu_ {z} (E _ {h}) g _ {+} (z / T) d ^ {\times} z \right| \ll (\mathrm{N} (\mathfrak {f}) T) ^ {- 1 / 2} (T \mathrm{Cond} (\chi)) ^ {\epsilon} \| h \| _ {N}
$$

$$
\left| \int_ {z} \mu_ {z} (E _ {h}) g _ {-} (z / T) d ^ {\times} z \right| \ll (\mathrm{N} (\mathfrak {f}) T) ^ {1 / 2} (T \mathrm{Cond} (\chi)) ^ {\epsilon} \mathrm{Cond} _ {\infty} (\chi) ^ {1 + \epsilon} \| h \| _ {N}
$$

Proof. Lem. 11.10 and Lem. 11.11.

6.2. Proof of theorem – cuspidal case. Let$\chi$be a character of$\mathbb { A } _ { F } ^ { \times } / F ^ { \times }$, of varying conductor f. Put$q = \mathrm { N } ( \mathfrak { f } )$.

We shall need the following estimate, proved in Lem. 9.10. It amounts in essence to a statement about the equidistribution of p-adic horocycles (classically, these roughly correspond to a statement about the equidistribution of$\{ { \textstyle { \frac { x } { q } } } + i z \} _ { 0 \leq x \leq q - 1 }$2 ${ \mathrm { i f ~ } } z \asymp q ^ { - 1 } )$

For any function f that is invariant by$\Pi _ { \mathfrak { q } } K _ { 0 } [ { \mathfrak { q } } ^ { s _ { \mathfrak { q } } } ]$, we have (with$\begin{array} { r } { \mathfrak { m } = \prod _ { \mathfrak { q } } \mathfrak { q } ^ { s _ { \mathfrak { q } } } ) } \end{array}$

$$
\left| \nu_ {z} (f) - \int_ {\mathbf {X}} f \right| \ll_ {\epsilon} q ^ {\alpha - 1 / 2 + \epsilon} \mathrm{N} (\mathfrak {m}) ^ {3 / 2 + \epsilon} \max (q z, \frac {1}{q z}) ^ {1 / 2} S _ {2, d} (f), f \in C ^ {\infty} (\mathbf {X})\tag{6.8}
$$

Proof. (of Thm. 6.1 – cuspidal case.) Choose$f \in \pi$to be the$^ { 6 6 } \varphi ^ { , 5 }$of Prop. 6.1, so that$| \mu ( f ) | \gg _ { \epsilon } \mathrm { N } ( \mathfrak { f } ) ^ { - 1 / 2 - \epsilon } | L _ { u n r } ( 1 / 2 , \pi \times \chi ) |$. For each ramified prime q of$\pi ,$let${ \mathfrak { q } } ^ { s _ { \mathfrak { q } } }$ be the local conductor of the local representation$\pi _ { \mathfrak { q } }$. Set$\begin{array} { r } { \mathfrak { m } : = \prod _ { \mathfrak { q } } \mathfrak { q } ^ { s _ { \mathfrak { q } } } } \end{array}$, the finite conductor of π.

Let$K \geq 1$be an integer satisfying$K \le \mathrm { N } ( \mathfrak { f } )$. Let$s$be the set of prime ideals of${ \mathfrak { o } } _ { F } .$, with norm lying in$[ K , 2 K ]$, and satisfying$( { \mathfrak { n } } , { \mathfrak { f } } ) = 1$and$( \mathfrak { n } , \mathrm { S u p p } ( f ) ) = 1$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>16</sup>The implicit constants here are totally unimportant; this estimate will be used only to verify that certain integrals converge.</span></small>

Fix${ \mathfrak { n } } _ { 0 } \in S$. For each prime ideal${ \mathfrak { n } } \in S .$, let$\varpi _ { \mathfrak { n } } \in F _ { \mathfrak { n } }$be a uniformizer. We define a measure σ on${ \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$so that

$$
\sigma = | \mathcal {S} | ^ {- 1} \sum_ {\mathfrak {n} \in \mathcal {S}} \chi (\varpi_ {\mathfrak {n}}) \chi (\varpi_ {\mathfrak {n} _ {0}}) ^ {- 1} \delta_ {a _ {\mathfrak {n}} (\varpi_ {\mathfrak {n}}) a _ {\mathfrak {n} _ {0}} (\varpi_ {\mathfrak {n} _ {0}}) ^ {- 1}}.\tag{6.9}
$$

Clearly$\sigma$has total mass 1. Moreover,$\mu ( f ) = \mu ( f \star \sigma )$and$f \star \sigma$is invariant by $K _ { 0 } [ { \mathfrak { q } } ^ { s _ { \mathfrak { q } } } ]$for each q m.

Choose κ “slightly smaller than${ 1 , } ^ { \dag }$to be specified later. Our aim is now to cut the z integration in$\begin{array} { r } { \mu = \int _ { z } \mu _ { z } d ^ { \times } z } \end{array}$into three ranges, the crucial range of which will be $q ^ { - 2 + \kappa } \ll z \ll q ^ { - \kappa }$; this avoids the pain of dealing with the infinite mass measure$\mu .$ Let$g _ { + } , g _ { - }$be as in Prop. 6.1. Define$h ( t )$by the rule$\begin{array} { r } { g _ { - } ( \frac { z } { q ^ { - 2 + \kappa } } ) + h ( t ) + g _ { + } ( \frac { t } { q ^ { - \kappa } } ) = 1 } \end{array}$

$$
\begin{array}{r l} & {(6. 1 0) \quad | \mu (f) | ^ {2} = | \mu (f \star \sigma) | ^ {2} = \left| \int_ {z} \mu_ {z} (f \star \sigma) d ^ {\times} z \right| ^ {2}} \\ & {\ll \left| \int g _ {-} (\frac {z}{q ^ {- 2 + \kappa}}) \mu_ {z} (f \star \sigma) \right| ^ {2} + \left| \int h (z) \mu_ {z} (f \star \sigma) d ^ {\times} z \right| ^ {2} + \left| \int g _ {+} (\frac {z}{q ^ {- \kappa}}) \mu_ {z} (f \star \sigma) d ^ {\times} z \right| ^ {2}} \end{array}
$$

By Prop. 6.1, the first and last term (without the square,$\begin{array} { r } { \mathrm { e . g . } \ \left| \int g _ { + } ( \frac { z } { q ^ { - \kappa } } ) \mu _ { z } ( f \star \sigma ) d ^ { \times } z \right| ) } \end{array}$ are$\ll \mathrm { C o n d } ( \pi ) ^ { 1 + \epsilon } \mathrm { C o n d } _ { \infty } ( \chi ) ^ { 1 + \epsilon } q ^ { \frac { \kappa - 1 } { 2 } + \epsilon }$. More explicitly, we note that

$$
\mu_ {z} (f \star \sigma) = | S | ^ {- 1} \sum_ {\mathfrak {n} \in \mathcal {S}} \mu_ {\mathrm{N} (\mathfrak {n}) ^ {- 1} \mathrm{N} (\mathfrak {n} _ {0}) z} (f)\tag{6.11}
$$

Now$1 / 2 \le \mathrm { N } ( \mathfrak { n } ) \mathrm { N } ( \mathfrak { n } _ { 0 } ) ^ { - 1 } \le 2$for all n – this was the purpose of the factors involving $\mathfrak { n } _ { 0 }$in (6.9) – and so one easily deduces a bound on$\begin{array} { r } { \int g _ { - } \big ( \frac { z } { q ^ { - 2 + \kappa } } \big ) \mu _ { z } ( f \star \sigma ) d ^ { \times } z } \end{array}$from the final assertion of Prop. 6.1. Similarly for the term involving$g _ { + }$

That the first and last terms of (6.10) should be less significant may be seen in the classical setting from the Fourier expansion; it should be regarded as a geometric version of the approximate functional equation).

As for the intermediate term, we note

$$
\int_ {z} h (z) \mu_ {z} (f) = \int_ {y \in \mathbb {A} _ {F} ^ {\times} / F ^ {\times}} h (| y |) \chi (y) f (a (y) n ([ \mathfrak {f} ])) d ^ {\times} y.
$$

Applying Cauchy-Schwarz, and the fact that$\begin{array} { r } { \int _ { \mathbb { A } _ { F } ^ { \times } / F ^ { \times } } h ( | y | ) d ^ { \times } y \ll \log ( q ) } \end{array}$, we get:

$$
\begin{array}{r l} & {\left| \int_ {z} h (z) \mu_ {z} (f \star \sigma) \right| ^ {2} \ll_ {\epsilon} q ^ {\epsilon} \int_ {z} h (z) \nu_ {z} (| f \star \sigma | ^ {2}) d ^ {\times} z} \\ & {\qquad \ll_ {\epsilon} q ^ {\epsilon} \int_ {\mathbf {X}} | f \star \sigma | ^ {2} d \mu_ {\mathbf {X}} + q ^ {\alpha - \kappa / 2 + \epsilon} \mathrm{N} (\mathfrak {m}) ^ {3 / 2 + \epsilon} S _ {2, d} (| f \star \sigma | ^ {2}),} \end{array}\tag{6.12}
$$

where we have applied (6.8). By Lemmas 8.1 and 8.2,

$$
\begin{array}{r l} & S _ {2, d, \beta} (| f \star \sigma | ^ {2}) \ll S _ {4, d, \beta} (f \star \sigma) ^ {2} \\ & \qquad \ll (\sup _ {g \in \operatorname{supp} (\sigma)} \| g \|) ^ {2 \beta} S _ {4, d, \beta} (f) ^ {2} \ll K ^ {4 \beta} S _ {2, d ^ {\prime}, \beta + 3 / 2} (f) ^ {2}. \end{array}\tag{6.13}
$$

where the last line holds for$d ^ { \prime } \gg d .$, and we have used Lem. 9.3 (which bounds the $L ^ { \infty }$norm of a cusp form in terms of$L ^ { 2 }$norms), together with the easily verified fact that$\begin{array} { r } { \operatorname* { s u p } _ { g \in \mathrm { s u p p } ( \sigma ) } \lVert g \rVert \ll K ^ { 2 } } \end{array}$

By bounds towards Ramanujan,

$$
\| f \star \sigma \| _ {L ^ {2}} ^ {2} = \int_ {g, g ^ {\prime}} \langle g ^ {- 1} g ^ {\prime} f, f \rangle d \sigma (g) d \sigma (g ^ {\prime}) \ll K ^ {2 \alpha - 1} \| f \| _ {L ^ {2}} ^ {2}.\tag{6.14}
$$

Thus:

$$
\begin{array}{r l} & {| \mu (f) | \ll_ {\epsilon} \mathrm{Cond} (\pi) \mathrm{Cond} _ {\infty} (\chi) (\mathrm{Cond} (\chi) \mathrm{Cond} (\pi)) ^ {\epsilon} q ^ {\frac {\kappa - 1}{2}}} \\ & \qquad + \left(K ^ {\alpha - 1 / 2} q ^ {\epsilon} + \mathrm{N} (\mathfrak {m}) ^ {3 / 4 + \epsilon} q ^ {- \kappa / 4 + \alpha / 2 + \epsilon} K\right) S _ {2, d, 2} (f) \\ & \qquad \ll q ^ {\epsilon} (q ^ {(\kappa - 1) / 2} + K ^ {\alpha - 1 / 2} + q ^ {\alpha / 2 - \kappa / 4} K) \mathrm{Cond} _ {\infty} (\chi) ^ {N} \mathrm{Cond} (\pi) ^ {N}, \end{array}\tag{6.15}
$$

for appropriate$N > 0$. We have used Prop. 6.1, (3) at the last step.

Prop. 6.1 guarantees that$| L _ { u n r } ( 1 / 2 , \pi \times \chi ) | \ll _ { \epsilon } q ^ { 1 / 2 + \epsilon } | \mu ( f ) |$. From this, optimizing$\kappa , K$, and applying trivial bounds at ramified places, we obtain the conclusion, taking$\alpha = 3 / 2 6$

6.3. Proof of theorem – noncuspidal case. We turn to the proof of (6.2). This is very similar, but we implement a mild regularization procedure to deal with the Eisenstein series, just as in the case of Rankin-Selberg L-functions.

Proof. (of (6.2).) We may assume that$\chi$ramifies at least at one finite place.

Let Ψ be a Schwarz function on$\mathbb { A } _ { F } ^ { 2 } , \ E ( g , s ) \ : = \ E _ { \Psi } ( g , s )$the corresponding Eisenstein series, chosen as in Prop. 6.2 with$s _ { 0 } = 1 / 2 , s _ { 0 } ^ { \prime } = 0 .$

Let$\kappa ^ { \prime } > 0$, let h be holomorphic in an open neighbourhood of the vertical strip$- \kappa ^ { \prime } \le \Re ( s ) \le 1 + \kappa ^ { \prime }$and put$\begin{array} { r } { E _ { h } ( s ) = \int _ { \Re ( s ) = 1 + \kappa ^ { \prime } } h ( s ) E ( g , s ) d s } \end{array}$. Then if $\begin{array} { r } { h ( 0 ) = h ( \frac { 1 } { 2 } ) = h ( 1 ) = 0 . } \end{array}$, it follows from the third assertion of Prop. 6.2 that

$$
S _ {\infty , d, \beta} (E _ {h}) \ll_ {\epsilon , d} \mathrm{Cond} _ {\infty} (\chi) ^ {N} \| h \| _ {0}
$$

for appropriate$N = N ( d , \beta ) > 0$. Here, as in (10.18) with κ replaced by$\kappa ^ { \prime } .$, the norm$\| h \| _ { N }$is defined to be$\begin{array} { r } { \int _ { - \infty } ^ { \infty } \left( | h ( 1 + \kappa ^ { \prime } + i t ) | + | h ( - \kappa ^ { \prime } + i t ) | \right) ( 1 + | t | ) ^ { N } d t } \end{array}$

Put, in the notation of Prop. 6.2,$I ( s ) = \Phi ( s , 0 ) L ( \chi , s ) L ( \chi , 1 - s )$. Then:

$$
\int_ {z} \mu_ {z} (E _ {h}) d ^ {\times} z = \mathrm{N} (\mathfrak {f}) ^ {- 1 / 2} \int_ {\Re (s) = 1 / 2} h (s) I (s) d s.\tag{6.16}
$$

This is established in (11.31); for now, we remark that that this is “almost” obvious from Proposition 6.2, the only additional point being that one can replace $E$by$\bar { E }$, and this is exactly where the fact that$\chi$is ramified at a finite place comes in – to kill the constant term of the Eisenstein series.17

Take$h = ( s - 1 / 2 ) ^ { 2 } s ( 1 - s ) { \overline { { I ( 1 - { \overline { { s } } } } } ) }$. The “good” analytic properties of$h ,$, e.g. rapid decay along vertical lines, follow<sup>18</sup> from$( 6 . 7 )$. In particular, h belongs to the function spaces$\mathcal { H } ( \kappa )$defined in (10.18) for any$\kappa > 0$, and the norms$\| h \| _ { N }$are all bounded by suitable powers of$\mathrm { C o n d } _ { \infty } ( \chi ) . q .$

Then (6.16) becomes

$$
\int_ {t = - \infty} ^ {\infty} t ^ {2} (1 / 4 + t ^ {2}) | I (\frac {1}{2} + i t) | ^ {2} = q ^ {1 / 2} \int_ {z} \mu_ {z} (E _ {h}) d ^ {\times} z\tag{6.17}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">X</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>17</sup>The classical version of this fact – see (6.3) – it is clear that the χ-sum will kill any constant term of  as long as χ is not trivial.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>18</sup>This point was not clear in a previous version; thanks to N. Bergeron for pointing this out.</span></small>

To bound the right-hand side, we proceed as in Sec. 6.2, but with f replaced by$E _ { h }$. We use notation as in that Section, except replacing the$^ { 6 6 } h ^ { \prime \prime }$defined before (6.10) by$1 - g _ { - } - g _ { - }$<sub>+</sub> to avoid clashing with its alternate usage here.

One proves as in that Section, that for$d \gg 1$

$$
\begin{array}{c} \left| \int_ {z} (1 - g _ {-} - g _ {+}) \mu_ {z} (E _ {h} \star \sigma) \right| \ll_ {\epsilon} q ^ {\epsilon} \Big (K ^ {\alpha - 1 / 2} + q ^ {\alpha / 2 - \kappa / 4} (\sup _ {g \in \operatorname{supp} (\sigma)} \| g \|) ^ {1 / 2} \Big) S _ {4, d, 1 / 2} (E _ {h}) \\ \ll q ^ {\epsilon} \left(K ^ {\alpha - 1 / 2} + q ^ {\alpha / 2 - \kappa / 4} K\right) \| h \| _ {0} \mathrm{Cond} _ {\infty} (\chi) ^ {N} \end{array}\tag{6.18}
$$

for some appropriate$N > 0$. At the last stage we have applied Prop. 6.2 to control the Sobolev norm.

Prop. 6.2 also guarantees that, for appropriate$N > 0$, we have:

$$
\begin{array}{r l r} & & {\left| \int g _ {-} (\frac {z}{q ^ {- 2 + \kappa}}) \mu_ {z} (E _ {h} \star \sigma) \right| + \left| \int g _ {+} (\frac {z}{q ^ {- \kappa}}) \mu_ {z} (E _ {h} \star \sigma) d ^ {\times} z \right|} \\ & & {\ll \mathrm{Cond} _ {\infty} (\chi) ^ {1 + \epsilon} q ^ {\frac {\kappa - 1}{2} + \epsilon} \| h \| _ {N},} \end{array}\tag{6.19}
$$

Combining (6.17) and (6.19), we obtain as in the previous Section the bound, for suficiently large$N { : }$

$$
\begin{array}{l} \int_ {t = - \infty} ^ {\infty} t ^ {2} (\frac {1}{4} + t ^ {2}) | L (\frac {1}{2} + i t, \chi) L (\frac {1}{2} - i t, \chi) | ^ {2} | \Phi (1 / 2 + i t, 0) | ^ {2} \\ \qquad \ll_ {\epsilon} \left(q ^ {\frac {\kappa - 1}{2}} + K ^ {\alpha - 1 / 2} + q ^ {\alpha / 2 - \kappa / 4} K\right) \| h \| _ {N} q ^ {1 / 2 + \epsilon} \mathrm{Cond} _ {\infty} (\chi) ^ {N} \end{array}\tag{6.20}
$$

One applies the convexity bound to bound$\| h \| _ { N }$, obtaining

$$
\int_ {- \infty} ^ {\infty} t ^ {2} | L (\frac {1}{2} + i t, \chi) | L (\frac {1}{2} - i t, \chi) | ^ {2} | \Phi (1 / 2 + i t, 0) | ^ {2} \ll \mathrm{Cond} _ {\infty} (\chi) ^ {N} q ^ {2 4 / 2 5},
$$

where we have increased N as necessary. From this we get$L ( \frac { 1 } { 2 } , \chi ) \ll \mathrm { C o n d } _ { \infty } ( \chi ) ^ { N } q ^ { 1 / 4 - 1 / 2 0 0 }$

## 7. Torus periods (II): equidistribution of compact torus orbits.

It has been independently shown by Zhang [39], Clozel-Ullmo [7] and P. Cohen [9] that the subconvexity result Thm. 6.1 implies the equidistribution of Heegner points over totally real fields; in particular, they pointed out that GRH implies this equidistribution. Thm. 6.1 makes this result unconditional.

The main aim of this section is to explain how one can obtain certain conditional results about equidistribution of subsets of Heegner points, and how this fits into the general framework of “sparse equidistribution questions.” In particular, this approach does not rely on reducing questions about subsets of Heegner points to subconvexity, but rather approaches the equidistribution question directly.

The proofs of the results (and various supporting Lemmas) will only be sketched, and we will confine ourselves for simplicity to the case of narrow class number 1; we will in any case present an unconditional approach, based on combining the ideas of this paper with the ideas of Michel, in the paper [23] (joint with P. Michel). We nevertheless feel that the ideas presented here may be of use in other contexts. Indeed, this section is of a diferent flavor to the other Sections; it uses “adelic analysis” more genuinely.

In fact, we shall need a mild refinement of the results of [7], which allow better control of the dependence on the test vectors. We state this refinement without proof in Thm. 7.1; the proof is an exercise in explicating some of the proofs in [7].

7.1. Equidistribution of Heegner points. We recall the definition of Heegner points. Let F be a totally real number field of degree d over$\mathbb { Q } .$. For simplicity we shall confine ourselves to the case where the ring of integers of F has narrow class number 1. This assumption does not change any of the technical details, which are in any case carried out adelically; it simply allows us to be a little more explicit about the torus orbits we consider. Let$\dot { E } = F ( \sqrt { - { \bf d } } )$be a totally imaginary quadratic extension of$F _ { \mathrm { { ; } } }$, where d$\in ~ \mathfrak { o } _ { F }$is totally positive and squarefree. Here “squarefree” means that it is of valuation$\leq 1$at all finite places.

Let$T _ { E }$be the torus Res$\phantom { } \cdot \phantom { } _ { E } / F \bigl ( \mathbb { G } _ { m } \bigr ) / \mathbb { G } _ { m } ;$we embed$T _ { E }$in$\mathrm { P G L _ { 2 } }$via (in obvious notation):

$$
\iota_ {E}: x + y \sqrt {- \mathbf {d}} \mapsto \left( \begin{array}{c c} x & y \\ - y \mathbf {d} & x \end{array} \right).\tag{7.1}
$$

Regard d as an element of$F \otimes \mathbb { R }$via the inclusion$F \hookrightarrow F \otimes \mathbb { R }$. Since it is totally positive, it possesses a unique totally positive square root,$\sqrt { \mathbf { d } } \in F \otimes \mathbb { R }$. Set $[ \mathbf { d } ] _ { \infty } = \left( \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { \sqrt { \mathbf { d } } } \end{array} \right) \in \mathrm { P G L } _ { 2 } ( F \otimes \mathbb { R } )$. We define a map$\mathcal { H } : T _ { E } ( \mathbb { A } _ { F } ) / T _ { E } ( F )  \mathbf { X }$ via

$$
\mathscr {H}: x \mapsto \iota_ {E} (x) [ \mathbf {d} ] _ {\infty},\tag{7.2}
$$

where we regard$\mathsf { \Gamma } [ \mathbf { d } ] _ { \infty } \subset \mathrm { P G L } _ { 2 } ( F \otimes \mathbb { R } ) \subset \mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$acting by right translation on X. Denote by$\mathrm { N } ( \mathbf { d } )$the absolute norm of d, i.e.$\mathrm { N } ( { \bf d } ) = | \pmb { \sigma } _ { F } / { \bf d } \pmb { \sigma } _ { F } |$

The$F _ { - }$-torus$T _ { E }$is anisotropic, and there is a unique$T _ { E } ( \mathbb { A } _ { F } )$-invariant probability measure on$T _ { E } ( \mathbb { A } _ { F } ) / T _ { E } ( F )$. Let$\nu _ { E }$be its image by the map$\mathcal { H }$

Theorem 7.1. Set$E = F ( { \sqrt { - \mathbf { d } } } )$, where d$\in \mathfrak { o } _ { F }$is totally positive and squarefree. The measures ν become equidistributed as$\mathrm { N } ( \mathbf { d } )  \infty$. Indeed, there exist$\delta >$ $0 , d , \beta$such that for$f \in C ^ { \infty } ( \mathbf { X } )$we have

$$
\left| \int f d \nu_ {E} - \int_ {\mathbf {X}} f (x) d x \right| \ll \mathrm{N} (\mathbf {d}) ^ {- \delta} S _ {\infty , d, \beta} ^ {*} (f).
$$

Recall the definition of$S ^ { * }$from Sec. 2.10. We do not give the proof; as we have remarked it can be obtained by following the computations of [7] a little more explicitly.

One recovers from Thm. 7.1 the equidistribution of certain Heegner points associated to$E = F ( { \sqrt { - \mathbf { d } } } )$as d varies. Thm. 7.1 also gives an efective rate of equidistribution for Heegner points with polynomial dependence on the level and the eigenvalue of a test function. This rather innocuous polynomial dependence (in the level aspect, at least) will in fact play a crucial role in our deduction of the equidistribution of sparse subsets in the following section.

7.2. Equidistribution of subsets of Heegner points. We turn to certain conditional results on equidistribution of sparse subsets. F being as in Sec. 7.1, let $E _ { i } = F ( { \sqrt { \mathbf { d } _ { i } } } )$be a sequence of distinct quadratic, totally imaginary, extensions of $F .$For each$E _ { i }$, let$S _ { i } \subset T _ { E _ { i } } ( \mathbb { A } _ { F } ) / T _ { E _ { i } } ( F )$be a subgroup of finite index$m _ { i }$. Let $\mu _ { E _ { i } } ^ { S _ { i } }$be the image of the Haar probability measure on$S _ { i }$by the map$\mathcal { H }$

The import of the next theorem is that, if$E _ { i }$has enough small split primes, one can obtain the equidistribution of the measures$\mu _ { E _ { i } } ^ { S _ { i } }$as$i \to \infty$. This result is quite similar to the results of Duke-Friedlander-Iwaniec [10] in the case$F = \mathbb { Q }$, although the method is at least superficially rather diferent. One can also contrast with Michel’s striking result, for$F = \mathbb { Q }$, that gives a comparable result but without the condition on enough small split primes. Our method is diferent to Michel, who deduces the result from his subconvexity bound for Rankin-Selberg L-functions. 19In the present approach, we prove the equidistribution theorem directly. In a sequel to this paper, the author and P. Michel combine the methods here with some methods developed by Michel to make the results of this section unconditional.

To quantify the existence of enough small split primes, one might impose the condition (as does Linnik [20]) that the$E _ { i }$vary through a sequence of quadratic extensions that split at a fixed prime of$F .$. We will prefer to take a more quantitative approach, which will yield a stronger result at the price of a stronger assumption. In that regard we introduce the following notation: For$\delta > 0$, we put

wt$( E _ { i } , \delta ) = \# \{ \mathfrak { q } \subset \mathfrak { o } _ { F }$prime and split in$E _ { i } , \mathrm { N } ( \mathbf { d } _ { i } ) ^ { \delta } \leq \mathrm { N } ( \ P ) \leq 2 \mathrm { N } ( \mathbf { d } _ { i } ) ^ { \delta } \}$

Theorem 7.2. There exists$\delta _ { 1 } > 0$such that,$\begin{array} { r } { i f \frac { m _ { i } } { \operatorname* { m i n } ( \mathrm { N } ( \mathbf { d } _ { i } ) ^ { \delta _ { 1 } ( 1 / 2 - \alpha ) } , \mathrm { w t } ( E _ { i } , \delta _ { 1 } ) ^ { 1 / 2 } ) } \to 0 _ { } } \end{array}$ the sequence$\mu _ { E _ { i } } ^ { S _ { i } }$converges, as$i  \infty ,$, to the invariant measure on$\mathbf { X }$.

Proof. This is deduced from Thm. 7.1 by using the mixing properties of the $T _ { E } ( \mathbb { A } _ { F } ) { \mathrm { - } } \mathbb { A } \mathrm { o w }$. Indeed, we fix an index i and a corresponding field$E _ { i }$. Let$\delta _ { 1 } > 0$ be fixed. Let  be the set of prime ideals of$F$which split in$E _ { i }$and with norm in $[ \mathrm { N } ( \mathbf { d } _ { i } ) ^ { \delta _ { 1 } } , 2 \mathrm { N } ( \mathbf { d } _ { i } ) ^ { \delta _ { 1 } } ]$. For each${ \mathfrak { q } } \in S$, the torus$T _ { E _ { i } } ( F _ { \mathfrak { q } } )$is isomorphic to$F _ { \mathfrak { q } } ^ { \times }$. Fix an isomorphism$\Upsilon _ { \mathfrak { q } } : T _ { E _ { i } } ( F _ { \mathfrak { q } } ) \longrightarrow F _ { \mathfrak { q } } ^ { \times }$, and let$\varpi _ { \mathfrak { q } }$be an element in$T _ { E _ { i } } ( F _ { \mathfrak { q } } )$such that $\Upsilon _ { \mathfrak { q } } ( \varpi _ { \mathfrak { q } } )$has valuation 1 in$F _ { \mathfrak { q } } ^ { \times }$

Let$\chi$be a character of$T _ { E _ { i } } ( \mathbb { A } _ { F } ) / T _ { E _ { i } } ( F )$, trivial on$S _ { i }$. Let$\nu _ { E _ { i } }$be as defined prior to Thm. 7.1, and define

$$
\mu_ {E _ {i}} (f) = \int_ {t \in T _ {E _ {i}} (\mathbb {A} _ {F}) / T _ {E _ {i}} (F)} f (\mathcal {H} (t)) \chi (t) d t,
$$

where$d t$is the Haar probability measure on$T _ { E _ { i } } ( \mathbb { A } _ { F } ) / T _ { E _ { i } } ( F )$. Let σ be the probability measure$\begin{array} { r } { \frac { 1 } { | \mathcal { S } | } \sum _ { \mathfrak { q } \in \mathcal { S } } \chi ( \varpi _ { \mathfrak { q } } ) \delta _ { \varpi _ { \mathfrak { q } } } } \end{array}$on$T _ { E _ { i } } ( \mathbb { A } _ { F } )$. Then$\mu _ { E _ { i } } ( f ) = \mu _ { E _ { i } } ( f \star { \mathcal { H } } _ { * } \sigma )$ where$\mathcal { H } _ { * } \sigma$denotes the image of σ by the map$\mathcal { H }$

By Cauchy-Schwarz, and Thm. 7.1,

$$
\begin{array}{r l} & {| \mu_ {E _ {i}} (f \star \mathcal {H} _ {*} \sigma) | ^ {2} \leq \nu_ {E _ {i}} (| f \star \mathcal {H} _ {*} \sigma | ^ {2})} \\ & {\qquad \leq \| f \star \mathcal {H} _ {*} \sigma \| _ {L ^ {2}} ^ {2} + O \left(\mathrm{N} (\mathbf {d} _ {i}) ^ {- \delta} S _ {\infty , d, \beta} ^ {*} (| f \star \mathcal {H} _ {*} \sigma | ^ {2})\right),} \end{array}\tag{7.3}
$$

where$\delta , d , \beta$are as in Thm. 7.1. Now, appropriate variants of Lem. 8.1 and 8.2 (for$S ^ { * }$instead of S) show that

$$
\begin{array}{r l} & S _ {\infty , d, \beta} ^ {*} (| f \star \mathcal {H} _ {*} \sigma | ^ {2}) \ll S _ {\infty , d, \beta} ^ {*} (f \star \mathcal {H} _ {*} \sigma) ^ {2} \\ & \qquad \ll \sup _ {g \in \operatorname{supp} \mathcal {H} _ {*} \sigma} \| g \| ^ {6 \beta} S _ {\infty , d, \beta} ^ {*} (f) ^ {2} \ll \mathrm{N} (\mathbf {d} _ {i}) ^ {6 \delta_ {1} \beta} S _ {\infty , d, \beta} ^ {*} (f) ^ {2} \end{array}\tag{7.4}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>19</sup>We note that this bound of Michel is considerably deeper than (5.3), since it deals with varying central character. For some speculative discussion on the “reason” that Michel’s method can avoid this condition, see the last paragraph of [24].</span></small>

and bounds towards Ramanujan show that

$$
\left\| f \star \mathscr {H} _ {*} \sigma \right\| _ {L ^ {2}} ^ {2} \ll \left(\mathrm{N} (\mathbf {d} _ {i}) ^ {\delta_ {1} (2 \alpha - 1)} + | \mathcal {S} | ^ {- 1}\right) \| f \| _ {L ^ {2}} ^ {2}.\tag{7.5}
$$

We note that (7.4) and (7.5) are very closely analogous to (6.13) and (6.14), with K replaced by$\mathrm { N } \big ( \mathbf { d } _ { i } \big ) ^ { \delta _ { 1 } }$. In the context of (6.14), the set$s$has size$K ^ { 1 - \epsilon }$; thus the term$| S | ^ { - 1 }$that appears in$( 7 . 5 )$could be neglected.

Recalling the definition of$\mu _ { E _ { i } }$, we conclude

$$
\begin{array}{c} \left| \int_ {t \in T _ {E _ {i}} (\mathbb {A} _ {F}) / T _ {E _ {i}} (F)} f (\mathcal {H} (t)) \chi (t) d t \right| \\ \ll \left(\mathrm{N} (\mathbf {d} _ {i}) ^ {3 \delta_ {1} \beta - \delta / 2} + \mathrm{N} (\mathbf {d} _ {i}) ^ {\delta_ {1} (\alpha - 1 / 2)} + | \mathcal {S} | ^ {- 1 / 2}\right) S _ {\infty , d, \beta} ^ {*} (f). \end{array}\tag{7.6}
$$

Summing the left-hand side of$( 7 . 6 )$over all$m _ { i }$characters$\chi$of$T _ { E _ { i } } ( \mathbb { A } _ { F } ) / T _ { E _ { i } } ( F )$ that are trivial on$S _ { i }$, and substituting$\vert \boldsymbol { S } \vert = \mathrm { w t } ( E _ { i } , \delta _ { 1 } )$, we obtain:

$$
\left| \mu_ {E _ {i}} ^ {S _ {i}} (f) \right| \ll m _ {i} \left(\mathrm{N} (\mathbf {d} _ {i}) ^ {3 \delta_ {1} \beta - \delta / 2} + \mathrm{N} (\mathbf {d} _ {i}) ^ {\delta_ {1} (\alpha - 1 / 2)} + \mathrm{wt} (E _ {i}, \delta_ {1}) ^ {- 1 / 2}\right) S _ {\infty , d, \beta} ^ {*} (f).
$$

Choosing$\delta _ { 1 }$suficiently small (the exact value will depend on the value of$\beta , \delta$ from Thm. 7.1) we obtain the claimed conclusion.

## 8. Background on Sobolev norms and reduction theory.

The rest of the paper consists of technical Lemmas. The sections that follow are arranged to be used as a reference, rather than to be read through.

8.1. Formal properties of the Sobolev norms. We begin by explicating certain formal properties of the Sobolev norms defined in Sec. 2.9.3.

Remark 8.1. The following properties of this definition are formal and will be repeatedly used:

(1) Translations by$K _ { \operatorname* { m a x } , \mathbf { G } }$preserve$S _ { p , d , \beta }$, i.e.$S _ { p , d , \beta } ( k \cdot f ) = S _ { p , d , \beta } ( f )$for $k \in K _ { \operatorname* { m a x } , \mathbf { G } }$

(2) If$L : C _ { \omega } ^ { \infty } ( \mathbf { X _ { G } } ) \ \to \ \mathbb { C }$is a linear functional and$| L ( \psi ) | \le P S _ { p , d , \beta } ( \psi )$ then also$| L ( \psi ) | \ \leq \ S _ { p , d , \beta } ( \psi )$. Indeed$\psi \mapsto | L ( \psi ) |$is itself a seminorm on$C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$

(3) Suppose that$E : C _ { \omega } ^ { \infty } ( \mathbf { X _ { G } } ) \to C _ { \omega } ^ { \infty } ( \mathbf { X _ { G } } )$is a linear endomorphism satisfying$P S _ { p , d , \beta } ( E f ) \le A \cdot P S _ { p , d , \beta } ( f )$, for some$A \in \mathbb { R }$. Then also$S _ { p , d , \beta } ( E f ) \le$ $A S _ { p , d , \beta } ( f )$. Indeed,$f \mapsto A ^ { - 1 } S _ { p , d , \beta } ( E f )$is a seminorm dominated by $P S _ { p , d , \beta }$

(4) We shall need a slight variant of (3) in the case where we are studying only the space of f with some invariance property.

Suppose that$E : C _ { \omega } ^ { \infty } ( \mathbf { X _ { G } } ) \to C _ { \omega } ^ { \infty } ( \mathbf { X _ { G } } )$is a linear endomorphism, M is a finite set of finite places, and for each$v \in M$we are given an open compact$K _ { 1 , v } \subset K _ { v } .$. Suppose moreover that$P S _ { p , d , \beta } ( E f ) \le A \cdot P S _ { p , d , \beta } ( f )$ for some$A \in \mathbb { R }$and for all$f$which are$\textstyle \prod _ { v \in M } K _ { 1 , v } { \mathrm { - f i x e d } }$. Then, for all$f$ which are$\prod _ { v \in M } K _ { 1 , v }$-fixed, we have in fact

$$
S _ {p, d, \beta} (E f) \leq A \prod_ {v \in M} [ K _ {v}: K _ {1, v} ] ^ {\beta} S _ {p, d, \beta} (f).
$$

Indeed, put$\begin{array} { r } { K _ { 1 , M } \ = \ \prod _ { v \in M } K _ { 1 , v } } \end{array}$and let Π be the averaging operator $\textstyle \int _ { k \in K _ { 1 , M } } \pi ( k ) d k$, where$K _ { 1 , M }$is endowed with the Haar probability measure. Then apply (3) above to the operator$f \mapsto E ( \Pi f )$.

Lemma 8.1. Let$F _ { 1 } \in C _ { \omega _ { 1 } } ^ { \infty } ( \mathbf { X _ { G } } ) , F _ { 2 } \in C _ { \omega _ { 2 } } ^ { \infty } ( \mathbf { X _ { G } } )$. Then

$$
S _ {p, d, \beta} (F _ {1} F _ {2}) \ll_ {d} S _ {2 p, d, \beta} (F _ {1}) S _ {2 p, d, \beta} (F _ {2}).
$$

Note that$F _ { 1 } F _ { 2 } \in C _ { \omega _ { 1 } \omega _ { 2 } } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$

Proof. Put$F ~ = ~ F _ { 1 } F _ { 2 }$. For any monomial  of degree d in , we can write $\begin{array} { r } { \mathcal { D } ( F _ { 1 } F _ { 2 } ) = \sum _ { \alpha \in \mathbb { Z } } ( \mathcal { D } _ { \alpha , 1 } F _ { 1 } ) ( \mathcal { D } _ { \alpha , 2 } F _ { 2 } ) } \end{array}$, where α range over an index set whose size is bounded by a constant depending only on d, and the$\mathcal { D } _ { \alpha , \star }$are certain monomials in satisfying$\mathrm { o r d } ( \mathcal { D } _ { \alpha , 1 } ) + \mathrm { o r d } ( \mathcal { D } _ { \alpha , 2 } ) = d .$It follows that

$$
\| \mathcal {D} F \| _ {L ^ {p} (\mathbf {X} _ {\mathbf {G}, \mathrm{ad}})} \leq \sum_ {\alpha \in \mathcal {I}} \left(\int_ {\mathbf {X} _ {\mathbf {G}, \mathrm{ad}}} | \mathcal {D} _ {\alpha , 1} F _ {1} | ^ {p} | \mathcal {D} _ {\alpha , 2} F _ {2} | ^ {p}\right) ^ {1 / p}.
$$

Applying Cauchy-Schwarz, we conclude

$$
\| \mathcal {D} F \| _ {L ^ {p} (\mathbf {X} _ {\mathbf {G}, \mathrm{ad}})} \leq \sum_ {\alpha \in \mathcal {I}} \| \mathcal {D} _ {\alpha , 1} F _ {1} \| _ {L ^ {2 p} (\mathbf {X} _ {\mathbf {G}, \mathrm{ad}})} \| \mathcal {D} _ {\alpha , 2} F _ {2} \| _ {L ^ {2 p} (\mathbf {X} _ {\mathbf {G}, \mathrm{ad}})}\tag{8.1}
$$

Clearly, for each finite place v, we have$K _ { v , F } \supset K _ { v , F _ { 1 } } \cap K _ { v , F _ { 2 } }$; in particular $[ K _ { \mathrm { m a x } , \mathbf { G } } : K _ { F } ] \le [ K _ { \mathrm { m a x } , \mathbf { G } } : K _ { F _ { 1 } } ] [ K _ { \mathrm { m a x } , \mathbf { G } } : K _ { F _ { 2 } } ]$. It follows that

$$
\begin{array}{l} [ K _ {\max, \mathbf {G}}: K _ {F} ] ^ {\beta} \sum_ {\mathcal {D}} \| \mathcal {D} F \| _ {L ^ {p} (\mathbf {X} _ {\mathbf {G}, \mathrm{ad}})} \\ \ll \left([ K _ {\max, \mathbf {G}}: K _ {F _ {1}} ] ^ {\beta} \sum_ {\mathcal {D}} \| \mathcal {D} F _ {1} \| _ {L ^ {2 p}}\right) \left([ K _ {\max, \mathbf {G}}: K _ {F _ {2}} ] ^ {\beta} \sum_ {\mathcal {D}} \| \mathcal {D} F _ {2} \| _ {L ^ {2 p}}\right), \end{array}\tag{8.2}
$$

where the implicit constant depends only on$d ,$and in all three instances varies over the set of monomials in$\boldsymbol { B }$of degree$\leq d$

That is to say, there is a constant$C = C ( d )$such that

$$
P S _ {p, d, \beta} (F _ {1} F _ {2}) \leq C \cdot P S _ {2 p, d, \beta} (F _ {1}) P S _ {2 p, d, \beta} (F _ {2}).
$$

From (2.11) we deduce

$$
S _ {p, d, \beta} (F _ {1} F _ {2}) \leq C \cdot S _ {2 p, d, \beta} (F _ {1}) S _ {2 p, d, \beta} (F _ {2}),
$$

as required.

We recall the definition of$\| g \|$for$g \in { \bf G } ( F _ { \infty } ) , { \bf G } ( \mathbb { A } _ { F } )$etc. from Sec. 2.4.

Lemma 8.2. Let$F \in C ^ { \infty } ( \mathbf { X _ { G } } )$and$g = ( g _ { \infty } , g _ { f } ) \in \mathbf { G } ( \mathbb { A } _ { F } )$

$$
S _ {p, d, \beta} (g \cdot F) \ll \| g _ {\infty} \| ^ {d} \| g _ {f} \| ^ {\beta} S _ {p, d, \beta} (F).
$$

Proof. Put$F ^ { \prime } = ( g _ { \infty } , g _ { f } ) \cdot F$, where$g _ { f } = ( g _ { v } ) _ { v } { \mathrm { f i n i t e } }$. For each finite place$v ,$we note that$K _ { v , F ^ { \prime } } \supseteq g _ { v } K _ { v , F } g _ { v } ^ { - 1 } \cap K _ { v , \mathbf { G } }$. The index$[ K _ { v , \mathbf { G } } : K _ { v , F ^ { \prime } } ]$is therefore bounded above by the number of cosets$x g _ { v } K _ { v , F }$in$K _ { v , \mathbf G } g _ { v } K _ { v , F }$. Clearly this is bounded above by the number of left$K _ { v , F }$cosets in$K _ { v , \mathbf G } g _ { v } K _ { v , \mathbf G } ;$but the number of such cosets is precisely$\lVert g _ { v } \rVert \cdot [ K _ { v , \mathbf { G } } : K _ { v , F } ]$. It now follows easily from the definitions that $P S _ { d , \beta , f } ( F ^ { \prime } ) \ll \| g _ { \infty } \| ^ { d } \| g _ { f } \| ^ { \beta } P S _ { d , \beta , f } ( F )$. Applying Rem. 8.1 to the endomorphism $F \mapsto ( g _ { \infty } , g _ { f } ) \cdot F$, we obtain the claim.

The following crude Lemma is as much of interpolation as we need. It will be applied, in practice, where$E$is a composite of a Hecke operator and a certain $L ^ { 2 } \mathrm { - p r o j e c t i o n }$

Lemma 8.3. Let E be a linear endomorphism of$C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$which commutes with $\mathbf { G } ( F _ { \infty } ) \times K _ { \operatorname* { m a x } , \mathbf { G } }$. Suppose there are real numbers A,$B > 0$such that for any$f \in$ $C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$, we have$\| E f \| _ { L ^ { 2 } } \leq A \| f \| _ { L ^ { 2 } } , \| E f \| _ { L ^ { \infty } } \leq B \| f \| _ { L ^ { \infty } }$. Then for$2 \leq p \leq \infty { : }$

$$
S _ {p, d, \beta} (E v) \leq A ^ {2 / p} B ^ {1 - \frac {2}{p}} S _ {p, d, \beta} (v).
$$

(We admit also$B = \infty ,$, in which case the$L ^ { \infty }$hypothesis should be seen as void, and the result becomes$S _ { 2 , d , \beta } ( E v ) \le A S _ { 2 , d , \beta } ( v ) . \jmath$

Proof.$\mathrm { B y }$interpolation, the operator norm of E w.r.t. the$L ^ { p }$norm on$C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathbf { G } } )$ is$\leq A ^ { 2 / p } B ^ { 1 - 2 / p }$. Moreover, the assumption on E shows that$K _ { E f } \supset K _ { f }$

It follows that for$f \in C _ { \omega } ^ { \infty } ( \mathbf { X _ { G } } )$we have the inequality

$$
P S _ {p, d, \beta} (E f) \leq A ^ {2 / p} B ^ {1 - 2 / p} P S _ {p, d, \beta} (f).
$$

Rem. 8.1 implies the conclusion.

8.1.1. Computing Sobolev norms in the Kirillov model. In the present section, let v be an archimedean place of$F .$

Let$\pi _ { v }$be a generic unitary irreducible representation of${ \mathrm { G L } } _ { 2 } ( F _ { v } )$. Recall that this means that$\pi _ { v }$is realized in a space of functions$\mathcal { H }$(the Kirillov model, consisting of restrictions of functions in the Whittaker model to the diagonal torus) on $F _ { v } ^ { \times }$. Recall also the definition of the local conductor$\mathrm { C o n d } _ { v } ( \pi _ { v } )$from Sec. 2.12.2.

In this model, the diagonal torus acts by translation and upper triangular matrices act through multiplication by characters: that is to say, for$f \in \mathcal { H } , y _ { 1 } , y _ { 2 } \in F _ { v } ^ { \times }$ $z \in F _ { v }$we have the rules

$$
\pi (a (y _ {1})) f: y _ {2} \mapsto f (y _ {1} y _ {2}), \pi (n (z)) f: y _ {2} \mapsto f (y _ {2}) e _ {F _ {v}} (z y _ {2}).\tag{8.3}
$$

From these facts it is easy to verify that the space of smooth vectors in$\pi _ { v }$contains all compactly supported smooth functions on$F _ { v } ^ { \times }$. Moreover,

$$
\| f \| _ {2} ^ {2} = \int_ {F _ {v} ^ {\times}} | f (y) | ^ {2} d ^ {\times} y\tag{8.4}
$$

defines a${ \mathrm { G L } } _ { 2 } ( F _ { v } )$-invariant inner product on${ \mathcal { H } } .$

We will eventually have occasion to choose test vectors in$\pi _ { v }$in this model, and wish to evaluate the “Sobolev norms” of the resulting vectors.

Lemma 8.4. Suppose$F _ { v } \cong \mathbb { R }$. Let$f \in \mathcal { K }$be$C ^ { \infty }$and compactly supported. Then

$$
\sum_ {\operatorname{ord} (\mathcal {D}) \leq k} \| \mathcal {D} f \| _ {2} \ll \operatorname{Cond} _ {v} \left(\pi_ {v}\right) ^ {2 k} \left(\sum_ {j = 0} ^ {2 k} \int_ {\mathbb {R} ^ {\times}} \left(| y | + | y | ^ {- 1}\right) ^ {2 k} \left| \frac {d ^ {j} f}{d ^ {j} y} \right| ^ {2} d ^ {\times} y\right) ^ {1 / 2},
$$

where the$\mathcal { D }$sum ranges over all monomials in a fixed basis for$\mathrm { L i e } ( \mathrm { G L } _ { 2 } ( F _ { v } ) )$) of degree$\leq k$

Suppose$F _ { v } \cong \mathbb { C } ,$and suppose$f \in \mathcal { K }$is$C ^ { \infty }$and compactly supported. Then

$$
\sum_ {\operatorname{ord} (\mathcal {D}) \leq k} \| \mathcal {D} f \| _ {2} \ll \operatorname{Cond} _ {v} \left(\pi_ {v}\right) ^ {k} \left(\sum_ {0 \leq i + j \leq 2 k} \int_ {\mathbb {C} ^ {\times}} \left(| z | + | z | ^ {- 1}\right) ^ {2 k} \left| \frac {\partial^ {i + j} f}{\partial^ {i} z \partial^ {j} \bar {z}} \right| ^ {2} d ^ {\times} z\right) ^ {1 / 2}
$$

Proof. We prove only the case with$F _ { v } \cong \mathbb { R }$, the complex case being similar.

Let$h , e , f , z$be nonzero elements of the (real) Lie algebras of$\operatorname { G L _ { 2 } } ( \mathbb { R } )$, defined via

$$
h = \left( \begin{array}{c c} 1 & 0 \\ 0 & - 1 \end{array} \right), e = \left( \begin{array}{c c} 0 & 1 \\ 0 & 0 \end{array} \right), f = \left( \begin{array}{c c} 0 & 0 \\ 1 & 0 \end{array} \right), z = \left( \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right)
$$

These satisfy the usual commutation relations$[ h , e ] = 2 e , [ h , f ] = 2 f , [ e , f ] = h$ Let λ be the scalar by which the Casimir operator$\textstyle { \frac { 1 } { 2 } } h ^ { 2 } + e f + f e$acts, and ν the scalar by which z acts; then$1 + | \lambda | + | \nu | ^ { 2 } \ll \mathrm { C o n d } _ { v } ( \bar { \pi } _ { v } ) ^ { 2 }$

It is easy to see how$h , e$act on$\mathcal { H } : ~ h$acts by a multiple of the diferential operator$c _ { 1 } \nu + y \frac { d } { d y }$and e acts by multiplication by c<sub>3</sub>y, for some constants$c _ { 1 } , c _ { 2 } , c _ { 3 }$ The Casimir operator$\begin{array} { r } { \frac { 1 } { 2 } h ^ { 2 } + e f + f e = \frac { 1 } { 2 } h ^ { 2 } + 2 e f - h } \end{array}$acts by the scalar$\lambda ;$so it follows that for$v \in \mathcal { H }$we have$\scriptscriptstyle { \mathcal { I } v } = { \frac { 1 } { 2 } } ( \bar { \lambda } + h - h ^ { 2 } ) v$. In particular, e acts on any compactly supported function via the diferential operator$\begin{array} { r } { c _ { 1 } ^ { \prime } y ^ { - 1 } + c _ { 2 } ^ { \prime } \frac { d } { d y } + c _ { 3 } ^ { \prime } y \frac { d ^ { 2 } } { d y ^ { 2 } } } \end{array}$ for certain constants$c _ { 1 } ^ { \prime } , c _ { 2 } ^ { \prime } , c _ { 3 } ^ { \prime }$, satisfying$| c _ { 1 } ^ { \prime } | , | c _ { 2 } ^ { \prime } | , | c _ { 3 } ^ { \prime } | \ll \mathrm { C o n d } _ { v } ( \pi _ { v } ) ^ { 2 }$. (In fact, $| c _ { i } ^ { \prime } | \ll \mathrm { C o n d } _ { v } ( \pi _ { v } ) ^ { 3 - i } . )$1

Any monomial of degree k in$h , e , f , z$is therefore a sum of terms$c _ { \gamma \delta } y ^ { \gamma } \partial _ { y } ^ { \delta } .$, where $| c _ { \gamma \delta } | \ll \mathrm { C o n d } _ { v } ( \pi _ { v } ) ^ { 2 k } , | \gamma | \leq k , \delta \leq 2 k$. The claimed result follows in the case$F _ { v } \cong \mathbb { R }$ A similar proof holds for$F _ { v } \cong \mathbb { C }$

8.2. Reduction theory. Recall that$F _ { \infty } : = F \otimes _ { \mathbb { Q } } \mathbb { R }$. Let$K _ { \infty } , K _ { v } , K _ { \operatorname* { m a x } }$be as in Sec. 2.5. Then$K _ { \infty } \times K _ { \operatorname* { m a x } }$is a maximal compact subgroup of${ \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$. Given $g \in { \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$) we may always write$g = { \left( \begin{array} { l l } { 1 } & { t } \\ { 0 } & { 1 } \end{array} \right) } { \left( \begin{array} { l l } { x } & { 0 } \\ { 0 } & { y } \end{array} \right) }$k, with$t \in \mathbb { A } _ { F } , x , y \in$ $\mathbb { A } _ { F } ^ { \times } , k \in K _ { \infty } \times K _ { \operatorname* { m a x } }$. We set$\mathrm { h t } ( g ) = | x y ^ { - 1 } | _ { \mathbb { A } } ;$this is well-defined, although$x , y$are not unique.

Then ht descends to a function$B ( F ) \backslash { \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )  \mathbb { R } _ { > 0 }$. Explicitly,

$$
\operatorname{ht} \left( \begin{array}{c c} a & b \\ c & d \end{array} \right) = \frac {| a d - b c | _ {\mathbb {A}}}{\prod_ {v} \| (c _ {v} , d _ {v}) \| ^ {2}},\tag{8.5}
$$

where one defines$\lVert ( c _ { v } , d _ { v } ) \rVert = \operatorname* { m a x } ( | c _ { v } | _ { v } , | d _ { v } | _ { v } )$for v finite, and

$$
\left\| \left(c _ {v}, d _ {v}\right) \right\| = \left(\left| c _ {v} \right| _ {v} ^ {2 / \deg (v)} + \left| d _ {v} \right| _ {v} ^ {2 / \deg (v)}\right) ^ {\deg (v) / 2}\tag{8.6}
$$

for v infinite, where$\deg ( v ) = [ F _ { v } : \mathbb { R } ]$

Define$\mathfrak { S } ( T ) \subset B ( F ) \backslash \mathrm { G L } _ { 2 } ( \mathbb { A } _ { F } )$to be${ \mathfrak { S } } ( T ) : = \{ g : \mathrm { h t } ( g ) \geq T \}$. Then, for all $T > 0$the natural projection Π$: \mathfrak { S } ( T ) \to \mathrm { G L } _ { 2 } ( F ) \backslash \mathrm { G L } _ { 2 } ( \mathbb { A } _ { F } )$has finite fibers; for suficiently large$T _ { \ast }$, it is injective, and for suficiently small$T$it is surjective. This is the content of reduction theory for$\mathrm { G L _ { 2 } }$. As a consequence, the complement of $\Pi ( { \mathfrak { S } } ( T ) )$has compact closure, modulo the center, for each$T .$

Fix$T _ { 0 }$such that Π :$\mathfrak { S } ( T _ { 0 } ) \to \mathrm { G L } _ { 2 } ( F ) \backslash \mathrm { G L } _ { 2 } ( \mathbb { A } _ { F } )$is injective. Then we define a function ht :$\mathrm { G L } _ { 2 } ( F ) \backslash \mathrm { G L } _ { 2 } ( \mathbb { A } _ { F } )$R via the rule

$$
\operatorname{ht} (g) = \left\{ \begin{array}{l} \operatorname{ht} (g ^ {\prime}), \text {if} g = \Pi (g ^ {\prime}) \text {for some} g ^ {\prime} \in \mathfrak {S} (T _ {0}), \\ T _ {0}, \text {else}. \end{array} \right.
$$

In fact, it is clear that ht descends to a function$\begin{array} { r } { \mathbf { X } = \mathrm { P G L } _ { 2 } ( F ) \backslash \mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } ) \ \longrightarrow \ } \end{array}$ $\mathbb { R } _ { \geq T _ { 0 } }$

Lemma 8.5. Let$U \subset \mathrm { G L } _ { 2 } ( F _ { \infty } )$be compact and$x \in \mathbf { X } _ { \mathrm { G L } ( 2 ) }$. The fibers of the map$U \times K _ { \operatorname* { m a x } } \longrightarrow \mathbf { X } _ { \mathrm { G L } ( 2 ) }$defined by$( u , k ) \mapsto$xuk have size bounded by$O ( \mathrm { h t } ( x ) )$, where the implicit constant depends on$U$

Proof. Suppose$g \in { \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$is a lift of$x \in \mathbf { X } _ { \mathrm { G L } ( 2 ) }$. Consider the map$U \times K _ { \operatorname* { m a x } } \to$ $\mathbf { X } _ { \mathrm { G L } ( 2 ) }$given by$( u , k ) \mapsto g u k$, as above. Let$( u , k )$belong to a fiber of maximal size. Call this size M. Then

$$
\begin{array}{l} (8. 7) \quad M = \# \{\gamma \in \mathrm{GL} _ {2} (F): g u k = \gamma g u ^ {\prime} k ^ {\prime}, \exists u ^ {\prime} \in U, k ^ {\prime} \in K _ {\max} \} \\ \qquad \leq \# \{\gamma : g u ^ {\prime \prime} k ^ {\prime \prime} = \gamma g, \exists u ^ {\prime \prime} \in U \cdot U ^ {- 1}, k ^ {\prime \prime} \in K _ {\max} \}. \end{array}
$$

Set$V = U \cdot U ^ { - 1 }$, a compact subset of$\mathrm { G L _ { 2 } } ( F _ { \infty } )$. The definition of${ \mathfrak { S } } ( T )$shows that there exists a constant$c < 1$, depending on$V$, such that$\mathfrak { S } ( T ) \cdot V \cdot K _ { \operatorname* { m a x } } \subset$ ${ \mathfrak { S } } ( c T )$. Choose$T$so large that the projection${ \mathfrak { S } } ( c T ) \to \mathbf { X } _ { \mathrm { G L } ( 2 ) }$is injective. It will sufice to show, for each$g \in { \mathfrak { S } } ( T )$), that

$$
\# \{\gamma \in \operatorname{GL} _ {2} (F): \gamma g \in g V K _ {\max} \} \ll \operatorname{ht} (g).\tag{8.8}
$$

Both$g$and$g V K$belong entirely to${ \mathfrak { S } } ( c T )$. By the choice of$T , \gamma g \in g V K _ { \operatorname* { m a x } }$ implies$\gamma$in$B ( F )$. Write$\gamma = a _ { \gamma } n _ { \gamma }$, with$a _ { \gamma } ~ \in ~ A ( F )$and$n _ { \gamma } ~ \in ~ N ( F )$; also, write$g = n _ { g } a _ { g } k _ { g }$with$\begin{array} { r } { n _ { g } \in N ( \mathbb { A } _ { F } ) , a _ { g } \in A ( \mathbb { A } _ { F } ) , k _ { g } \in K _ { \infty } \times K _ { \operatorname* { m a x } } } \end{array}$. We are free to adjust$g$on the left by an element of$N ( F )$, since doing so will not afect the cardinality of the set$\{ \gamma \in \mathrm { G L } _ { 2 } ( F ) : \gamma g \in g V K _ { \operatorname* { m a x } } \}$. We may thereby assume that $n _ { g }$lies in a fixed compact subset of$N ( \mathbb { A } _ { F } )$. Thus we can write$g = a _ { g } k _ { g } ^ { \prime } ;$, where $k _ { g } ^ { \prime } : = a _ { g } ^ { - 1 } n _ { g } a _ { g } k _ { g }$lies in a certain fixed compact subset Ω of${ \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$

Now,$\gamma g \in g V K$implies that$a _ { q } ^ { - 1 } a _ { \gamma } n _ { \gamma } a _ { g } \in \Omega V K _ { \operatorname* { m a x } } \Omega ^ { - 1 }$. Noting that$a _ { g } ^ { - 1 } a _ { \gamma } n _ { \gamma } a _ { g } =$ $a _ { \gamma } a _ { g } ^ { - 1 } n _ { \gamma } a _ { g } .$, we deduce that$a _ { \gamma }$lies in a fixed compact subset of${ \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$, depending only on$U ;$thus the number of possibilities for$a _ { \gamma }$are${ \ll } _ { U } 1$. Moreover, it now follows that$a _ { g } ^ { - 1 } n _ { \gamma } a _ { g }$lies in a compact subset of$\mathbb { A } _ { F }$depending only on$U .$

Thus, if we write$a _ { g } = \left( \begin{array} { c c } { { x } } & { { 0 } } \\ { { 0 } } & { { y } } \end{array} \right) , n _ { \gamma } = \left( \begin{array} { c c } { { 1 } } & { { \beta } } \\ { { 0 } } & { { 1 } } \end{array} \right)$, then$\beta \in x y ^ { - 1 } \Omega ^ { \prime }$, where $\Omega ^ { \prime } \subset \mathbb { A } _ { F }$is a compact subset that depends only on$\dot { U } .$. It is easy to see that the number of possibilities for$\beta$is${ \ll } _ { U } 1 + { | x y ^ { - 1 } | } _ { \mathbb { A } _ { F } }$. But$| x y ^ { - 1 } | _ { \mathbb { A } _ { F } } = \mathrm { h t } ( g )$, which is a function that is bounded away from zero, and we are done.

Lemma 8.6. Let notations be as in the previous Lemma$8 . 5$. Consider the composite map$U \cdot K _ { \mathrm { m a x } } \stackrel { \Pi } { \longrightarrow } \mathbf { X } _ { \mathrm { G L ( 2 ) } } \longrightarrow \mathbf { X }$. Each fiber of this map may be written as the union of at most$O ( \operatorname { h t } ( x ) )$sets each of the form$y Z ( \mathbb { A } _ { F } ) \cap U K _ { \operatorname* { m a x } }$, where$Z$is the center of GL<sub>2</sub> and$y \in \operatorname { G L } _ { 2 } ( \mathbb { A } _ { F } )$

Proof. Let$\bar { x }$be the image of x in X. Let$u , u ^ { \prime } \in U , k , k ^ { \prime } \in K _ { \operatorname* { m a x } }$. Suppose that $\bar { x } u k = \bar { x } u ^ { \prime } k ^ { \prime }$in X. Then there is$z \in \mathbb { A } _ { F } ^ { \times }$and$\gamma \in \operatorname { G L } _ { 2 } ( F )$such that

$$
x u k = \gamma x u ^ {\prime} k ^ {\prime} a (z, z), \text {   equality   in   } \mathrm{GL} _ {2} (\mathbb {A} _ {F})\tag{8.9}
$$

For fixed$u , k$and$\gamma _ { \mathrm { { i } } }$, the set of$u ^ { \prime } k ^ { \prime }$satisfying (8.9) is visibly the intersection of $U K _ { \operatorname* { m a x } }$with a fixed$Z ( \mathbb { A } _ { F } )$-coset. This coset depends only on the class of$\gamma$in $\mathrm { P G L _ { 2 } } ( F )$, so it sufices to show that those$\gamma \in \operatorname { G L } _ { 2 } ( F )$that occur in equalities such as (8.9) for varying$u , k , u ^ { \prime } , k ^ { \prime }$represent at most$O ( \mathrm { h t } ( x ) )$) distinct cosets$\gamma Z ( F )$in $\mathrm { P G L _ { 2 } } ( F )$

Taking determinant followed by the norm$\mathbb { A } _ { F } ^ { \times } / F ^ { \times } \to \mathbb { R }$, we conclude that$| z | _ { \mathbb { A } }$ belongs to a compact subset of$\mathbb { R } ^ { \times }$that depends only on$U$. The norm map $\mathbb { A } _ { F } ^ { \times } / F ^ { \times } \to \mathbb { R } ^ { \times }$being proper, it follows that z itself belongs to a compact subset $\mathbb { A } _ { F } ^ { \times } / F ^ { \times }$that depends only on$U$.

In particular, there is a compact subset$\Omega \subset F _ { \infty } ^ { \times }$, depending only on$U _ { : }$, and a finite subset$P \subset \mathbb { A } _ { F } ^ { \times }$, containing 1 and also depending only on$U ,$such that $\begin{array} { r } { z \in { \cal F } ^ { \times } \Omega . { \cal P } . \prod _ { v \mathrm { f i n i t e } } \mathfrak { o } _ { { \cal F } , v } ^ { \times } } \end{array}$. Let$\tilde { U } = U \cdot \{ a ( z _ { \infty } , z _ { \infty } ) : z _ { \infty } \in \Omega \}$. Given a solution to (8.9), write$z = \delta z _ { \infty } p o$, with$\begin{array} { r } { \delta \in F ^ { \times } , z _ { \infty } \in \Omega , p \in P , o \in \prod _ { v \mathrm { f i n i t e } } \boldsymbol { \vartheta } _ { F , v } ^ { \times } } \end{array}$. Then

$$
x u k = \gamma a (\delta , \delta) x a (p, p) u ^ {\prime} a (z _ {\infty}, z _ {\infty}) k ^ {\prime} a (o, o),
$$

in particular, taking$\tilde { u } = u ^ { \prime } a ( z _ { \infty } , z _ { \infty } ) \in \tilde { U } , k ^ { \prime \prime } = k ^ { \prime } a ( o , o ) \in K _ { \operatorname* { m a x } } .$, the image of $x a ( p , p ) \tilde { u } k ^ { \prime \prime }$in$\mathbf { X _ { G } }$coincides with xuk. So the number of possibilities for the$Z ( F ) .$ coset of γ is bounded above by the fibers of the map$P \times \tilde { U } \times K _ { \mathrm { m a x } } \to \mathbf { X _ { G } }$given by$( p , \tilde { u } , k ) \to x a ( p , p ) \tilde { u } k$. The result follows from Lem. 8.5.

We shall now need a quantitative version of certain statements in reduction theory. The subsequent Lemma is a fancier version of the following statement: the number of$\gamma \in \mathrm { S L } ( 2 , \mathbb { Z } )$that map a fixed$z \in \mathbb { H }$to the Siegel set

$$
\{x + i y: 0 \leq x \leq 1, y \geq T \}
$$

is$\ll 1 + T ^ { - 1 }$

Lemma 8.7. Let$g \in { \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$and$Y > 0$a positive real number. Then

$$
\# \{\gamma \in B (F) \backslash \mathrm{GL} _ {2} (F): \operatorname{ht} (\gamma g) \geq Y \} \ll_ {\epsilon} 1 + Y ^ {- 1 - \epsilon}.\tag{8.10}
$$

Here the implicit constant is independent of$g .$. Moreover, suppose$g \in { \mathfrak { S } } ( T )$with $T \geq 1$. Then:

$$
\sup \{\mathrm{ht} (\gamma g): \gamma \notin B (F) \} \leq T ^ {- 1}.\tag{8.11}
$$

Proof. The proof of (8.10) is not dificult, generalizing in a straightforward way the proof with$F = \mathbb { Q }$. However, it is somewhat notationally tedious; the (hypothetical) reader may wish to simply work out the proof for$F = \mathbb { Q }$, where it is equivalent to the following fact: the number of primitive vectors in a unimodular sublattice of$\mathbb { R } ^ { 2 }$ that are contained in an R-ball is$\ll ( 1 + R ^ { 2 } )$, uniformly in the lattice. (The result also be deduced if one admits some basic facts from the theory of Eisenstein series over$F ,$, but we wish to rather deduce these basic facts from the present Lemma). We also remark that the entire content of (8.10) lies in the uniformity in$g .$

Without loss of generality, we take$g ~ \in \mathfrak { S } ( T _ { 0 } )$, where$T _ { 0 }$is suficiently small that the map$\Im ( T _ { 0 } )  \mathbf { X } _ { \mathrm { G L } ( 2 ) }$is surjective. So$g = { \left( \begin{array} { l l } { 1 } & { t } \\ { 0 } & { 1 } \end{array} \right) } { \left( \begin{array} { l l } { x } & { 0 } \\ { 0 } & { y } \end{array} \right) }$k with $\vert x y ^ { - 1 } \vert _ { \mathbb { A } } \ge T _ { 0 }$. Moreover, replacing$g$by$_ { g z , \mathrm { ~ ~ } }$for any$z \in Z ( \mathbb { A } _ { F } )$does not afect the problem, so we may take$y = 1$. Then, for$\gamma = { \left( \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right) } \in { \mathrm { G L } } _ { 2 } ( F )$, we have

$$
\mathrm{ht} (\gamma g) = \frac {| x | _ {\mathbb {A}}}{\prod_ {v} \| (x _ {v} c , c t _ {v} + d) \| _ {v} ^ {2}},\tag{8.12}
$$

The equivalence class of$\gamma$in$B ( F ) \backslash \mathrm { G L } _ { 2 } ( F )$depends only the pair$( c , d ) \in F ^ { 2 }$2 considered up to$F ^ { \times }$equivalence (i.e., it depends only on$c / d \in F \cup \{ \infty \} . )$It sufices, then, to estimate the number

$$
\# \{[ c: d ] \in \mathbb {P} ^ {1} (F), \prod_ {v} \| x _ {v} c, c t _ {v} + d \| _ {v} ^ {2} \leq Y ^ {- 1} | x | _ {\mathbb {A}} \},\tag{8.13}
$$

If Ω is any fixed compact subset of$\mathbb { A } _ { F } ^ { \times }$, then for$\omega \in \Omega$we have$\begin{array} { r } { \prod _ { v } \| x _ { v } \omega c , c t _ { v } + } \end{array}$ $\begin{array} { r } { d \| _ { v } \asymp _ { \Omega } \prod _ { v } \| x _ { v } c , c t _ { v } + d \| _ { v } } \end{array}$. Consider$\mathbb { R } _ { > 0 }$as embedded in$\mathbb { A } _ { F } ^ { \times }$via$\mathbb { R } _ { > 0 } \hookrightarrow \mathbb { A } _ { \mathbb { O } } ^ { \times } \hookrightarrow \mathbb { A } _ { F } ^ { \times }$ Then there is a compact subset$\Omega \in \mathbb { A } _ { F } ^ { \times }$such that$\mathbb { A } _ { F } ^ { \times } = F ^ { \times } \cdot \Omega \cdot \mathbb { R } _ { > 0 }$

The size of (8.13) is unafected by the substitution$( x , t ) \mapsto ( x \tau , t \tau )$, for any $\tau \in \ F ^ { \times }$. In view of the above remarks we may assume – decreasing Y by a constant that depends only on$F -$that$x \in \mathbb { R } _ { > 0 }$. Moreover, the size of$_ { ( 8 . 1 3 ) }$is also unafected by the substitution$t \mapsto t + \tau$, for$\tau \in F$. We may therefore assume that$| t | _ { v } \leq 1$for all finite places v.

Fix a set of representatives$\mathfrak { J } _ { 1 } , \ldots , \mathfrak { J } _ { h }$for the class group of${ \mathfrak { o } } _ { F } ;$we will assume each${ \mathfrak { J } } _ { i }$is integral. For any$[ c : d ] \in \mathbb { P } ^ { 1 } ( F )$, we may find a representative$( c , d )$so that the ideal$c { \pmb { 0 } } _ { F } + d { \pmb { 0 } } _ { F }$is one of the${ \mathfrak { J } } _ { i } ;$; moreover, replacing$( c , d ) \in \Im _ { i } ^ { 2 }$by$( \epsilon c , \epsilon d )$ for$\epsilon \in \mathfrak { o } _ { F } ^ { \times }$does not change the class$[ c : d ]$

The restrictions on$x , \imath$imply that$\| ( x _ { v } c , c t _ { v } + d ) \| _ { v } = \| ( c , d ) \| _ { \colon }$<sub>v</sub> for all finite v. Then$\begin{array} { r } { \prod _ { v \mathrm { f i n i t e } } \| ( c , d ) \| _ { v } = \mathrm { N } ( \mathfrak { I } _ { i } ) ^ { - 1 } } \end{array}$, the inverse of the norm of$\Im _ { i } = c \pmb { \ 0 } _ { F } + d \pmb { \ 0 } _ { F }$. So it will sufice to bound, for each$1 \leq i \leq h$, the quantity

$$
\# \{(c, d) \in \mathfrak {J} _ {i} ^ {2} / \mathfrak {o} _ {F} ^ {\times}: c \mathfrak {o} _ {F} + d \mathfrak {o} _ {F} = \mathfrak {J} _ {i}: \prod_ {\infty | v} (| x _ {v} | ^ {2} | c | _ {v} ^ {2} + | c t _ {v} + d | _ {v} ^ {2}) \leq Y ^ {- 1} | x | _ {\mathbb {A}} N (\mathfrak {J}) _ {i} ^ {2} \}.
$$

Since${ \mathfrak { J } } _ { i }$belongs to a finite set, the quantity$\mathrm { N } ( \Im )$is bounded; thus, decreasing $Y$again as necessary, it sufices to estimate for each$1 \leq i \leq h$

$$
\# \{(c, d) \in \mathfrak {J} _ {i} ^ {2} / \mathfrak {o} _ {F} ^ {\times}: c \mathfrak {o} _ {F} + d \mathfrak {o} _ {F} = \mathfrak {J} _ {i}, \prod_ {\infty | v} \| (x _ {v} c, c t _ {v} + d) \| _ {v} ^ {2} \leq Y ^ {- 1} | x | _ {\mathbb {A}} \}
$$

There is only one term corresponding to$c = 0$. Otherwise, (c) is a principal ideal divisible by${ \mathfrak { J } } _ { i } ;$let$\mathcal { P }$be the set of integral principal ideals. Then the size of the set above is precisely

$$
\sum_ {(c) \in \mathcal {P}} \# \{d \in \mathfrak {J} _ {i}: (c) + d \mathfrak {o} _ {F} = \mathfrak {J} _ {i}, \prod_ {\infty | v} \| (x _ {v} c, c t _ {v} + d) \| _ {v} ^ {2} \leq Y ^ {- 1} | x | _ {\mathbb {A}} \}\tag{8.14}
$$

We note that the size of the inner set is independent of the choice of generator for the principal ideal (c). Moreover, the inequality of$_ { ( 8 . 1 4 ) }$implies that the norm $\mathrm { N } ( ( c ) )$of the principal ideal (c) satisfies$\begin{array} { r } { \mathrm { N } ( \bar { ( } c ) ) ^ { 2 } \leq Y ^ { \dot { - } 1 } | x | _ { \mathbb { A } } ^ { \dot { - } 1 } } \end{array}$

Let us estimate the number of d that can correspond to a fixed principal ideal (c) in (8.14). Recall that$| x | _ { \mathbb { A } } \geq T _ { 0 }$and that$x _ { \mathbb { A } }$is in the image of the embedding $\mathbb { R } _ { > 0 } \hookrightarrow \mathring { \mathbb { A } } _ { Q } ^ { \times } \hookrightarrow \mathring { \mathbb { A } } _ { F } ^ { \times }$. In particular,$| x | _ { \imath }$is bounded below at each infinite place. Moreover, since${ \mathfrak { o } } _ { F } ^ { \times }$is a cocompact subgroup of the elements of$F _ { \infty } ^ { \times }$with norm 1, we can choose a representative for the principal ideal$( c )$so the same is true of$| c | _ { v }$ Note that (cf. 8.6) that$\| ( x _ { v } c , c t _ { v } + d ) \| _ { v } \asymp ( | x _ { v } c | _ { v } + | c t _ { v } + d _ { v } | _ { v } )$

So in fact, again decreasing Y as necessary, it will sufice to estimate

$$
\sum_ {(c) \in \mathcal {P}: N (c) \leq Y ^ {- 1 / 2} | x | _ {\mathbb {A}} ^ {- 1 / 2}} \# \{d \in \mathfrak {J} _ {i}: \prod_ {\infty | v} (1 + | c t + d | _ {v}) ^ {2} \leq Y ^ {- 1} | x | _ {\mathbb {A}} \}\tag{8.15}
$$

To estimate the right-hand side, first observe that if$\{ M _ { v } \} _ { \infty | v }$is any set of positive real numbers indexed by the infinite places of$F .$, then #$\{ d \in \mathfrak { I } _ { i } : | c t + d | _ { v } \leq$ $M _ { v }$for$\begin{array} { r } { \infty | v \} \ll \prod _ { \infty | v } ( 1 + M _ { v } ) } \end{array}$. Indeed, by subtraction, it will sufice to estimate $\# \{ d \in \mathfrak { I } _ { i } : | d | _ { v } \leq 2 M _ { v }$for$\infty | v \}$; this amounts to counting points in the lattice $\Im _ { i } \subset F _ { \infty }$in a region that is the product of a box and a disc; the result is then clear.

Next, if$T \geq 1$, then the subset$\{ ( y _ { 1 } , \dotsc , y _ { d } ) : \prod _ { i } ( 1 + y _ { i } ) \leq T \}$in$\mathbb { R } _ { > 0 } ^ { d }$is contained in the union of$O _ { \epsilon } ( T ^ { \epsilon } )$boxes$\left\{ \left( y _ { 1 } , \dots , y _ { d } \right) : y _ { i } \le M _ { i } \right\}$, where$\Pi _ { i } ( 1 + \dot { M } _ { i } ) \ll T$. We may assume$Y ^ { - 1 } | x | _ { \mathbb { A } } \geq 1$, else (8.15) has no solutions. We conclude that the number of d attached to each principal ideal (c) in (8.15) is${ \ll } _ { \epsilon } ~ ( { Y } ^ { - 1 / 2 } | x | _ { \mathbb { A } } ^ { 1 / 2 } ) ^ { 1 + \epsilon }$

The number of possibilities for (c) is bounded by the number of integral ideals with norm$\leq Y ^ { - 1 / 2 } | x | _ { \mathbb { A } } ^ { - 1 / 2 }$, which is$\ll _ { \epsilon } ~ ( Y ^ { - 1 / 2 } | x | _ { \mathbb { A } } ^ { - 1 / 2 } ) ^ { 1 + \epsilon }$. Finally there is one class with$c = 0$. We conclude that the number of pairs$( c , d )$up to equivalence is $\ll Y ^ { - 1 - \epsilon } + 1$. This proves (8.10).

As for (8.11), suppose$g \in { \mathfrak { S } } ( T )$, so we may write$g = { \left( \begin{array} { l l } { x } & { z } \\ { 0 } & { y } \end{array} \right) }$k with$k \in$ $K _ { \infty } \times K _ { \operatorname* { m a x } } .$, and$| x y ^ { - 1 } | _ { \mathbb { A } } \geq T$. Suppose$\gamma = { \left( \begin{array} { l l } { \alpha } & { \beta } \\ { \alpha ^ { \prime } } & { \beta ^ { \prime } } \end{array} \right) } . { \mathrm { ~ I f ~ } } \gamma \notin B ( F )$, then $\alpha ^ { \prime } \neq 0$. In that case, following the notation of (8.5), we have:

$$
\prod_ {v} \| \left(\alpha_ {v} ^ {\prime}, \beta_ {v} ^ {\prime}\right) g _ {v} \| \geq \prod_ {v} \left| \alpha_ {v} ^ {\prime} x _ {v} \right| _ {v} = | x | _ {\mathbb {A}}.
$$

and therefore, by (8.5), ht$( \gamma g ) \leq | \operatorname* { d e t } ( g ) x ^ { - 2 } | _ { \mathbb { A } } \leq T ^ { - 1 }$

## 9. Background on quantitative equidistribution results.

The aim of this section is to quantify various standard equidistribution results (equidistribution of long horocycles, Hecke points, etc.), using the adelic Sobolev norms. As such neither the results nor the methods are new; we just collect together those results we need and provide brief proofs.

As regards the origin of the ideas used here, we have drawn in particular from the work of Clozel-Ullmo, Linnik, Oh, Margulis, Ratner and Sarnak.

## 9.1. Decay of matrix coeficients.

9.1.1. Local setting. Our fundamental tool in establishing all these results is the spectral gap, i.e., quantitative mixing properties of real and p-adic flow. As such, we begin by recalling the basic relevant bound on matrix coeficients.

Let$0 \leq \alpha \leq 1 / 2$. Let v be a place of F, and suppose that$( V , \pi )$is a unitary representation of$\mathrm { G L _ { 2 } } ( F _ { v } )$which does not contain, in its spectral decomposition, any complementary series with parameter$\geq \alpha$. (More formally: V does not weakly contain such a representation). Thus$\alpha = 0$corresponds to$V$being tempered, and $\alpha = 1 / 2$corresponds to V having no almost invariant vectors.

Then for w<sub>1</sub>, w<sub>2</sub> any two$K _ { v }$-finite elements of$V ,$, satisfying$\langle w _ { 1 } , w _ { 1 } \rangle = \langle w _ { 2 } , w _ { 2 } \rangle =$ 1, and any$x \in F _ { v }$we have the bound on matrix coeficients given by

$$
\langle \pi (a (x) w _ {1}, w _ {2} \rangle \ll_ {\epsilon , F} \dim (K _ {v} w _ {1}) ^ {1 / 2} \dim (K _ {v} w _ {2}) ^ {1 / 2} (1 + | x | _ {v}) ^ {\alpha - 1 / 2 + \epsilon}.\tag{9.1}
$$

The implicit constant of (9.1) depends only on ǫ. Since we do not know of an available reference, we briefly sketch an argument for (9.1). In the case where $\alpha = 0 ,$, i.e. V is tempered, then (9.1) is proven in [8]. In the general case, let $( \sigma _ { 1 / 2 - \alpha } , W )$be the complementary series with parameter$1 / 2 - \alpha ;$let$\boldsymbol { v } ^ { 0 } \in W$be a unitary spherical vector. Then the representation$V \otimes W$is tempered. Indeed it sufices – again by [8] – to verify that a dense set of matrix coeficients are in $L ^ { 2 + \epsilon }$, which follows by direct computation. Now one may estimate the matrix coeficient$\langle a ( x ) w _ { 1 } \otimes \bar { v ^ { 0 } } , w _ { 2 } \otimes v ^ { 0 } \rangle$by appealing again to [8]. On the other hand $\langle a ( x ) w _ { 1 } \otimes v ^ { 0 } , w _ { 2 } \otimes v ^ { 0 } \rangle = \langle a ( x ) w _ { 1 } , w _ { 2 } \rangle \langle a ( x ) v ^ { 0 } , v ^ { 0 } \rangle$, and an easy computation shows that$\langle a ( x ) v ^ { 0 } , v ^ { 0 } \rangle \gg _ { \epsilon } ( 1 + | x | _ { v } ) ^ { - \alpha - \epsilon }$. Thus (9.1) follows. (This argument is a variant of an argument that appears at the end of$[ 8 ] .$)

Let us record a useful further variant. Suppose v is finite. Let$K _ { 1 } , K _ { 2 } \subset K _ { v }$be subgroups and let$\sigma$be the$( K _ { 1 } , K _ { 2 } )$-bi-invariant probability measure supported on $K _ { 1 } a ( x ) K _ { 2 }$

Then

$$
\| v \star \sigma \| _ {2} \ll [ K _ {v}: K _ {1} ] ^ {1 / 2} [ K _ {v}: K _ {2} ] ^ {1 / 2} (1 + | x | _ {v}) ^ {\alpha - 1 / 2 + \epsilon} \| v \| _ {2}.\tag{9.2}
$$

Indeed, for$i = 1 , 2$let$\Pi _ { K _ { i } }$be the projection operator$w \mapsto \int _ { K _ { i } }$kw on$V ,$where$K _ { i }$ is endowed with the Haar probability measure. Then:

$$
\begin{array}{l} \| v \star \sigma \| _ {2} = \sup _ {w \in V} \frac {\langle v \star \sigma , w \rangle}{\| w \| _ {2}} \\ = \sup _ {w \in V} \frac {\langle a (x) \Pi_ {K _ {1}} v , \Pi_ {K _ {2}} w \rangle}{\| w \| _ {2}} \leq [ K _ {v}: K _ {1} ] ^ {1 / 2} [ K _ {v}: K _ {2} ] ^ {1 / 2} (1 + | x | _ {v}) ^ {\alpha - 1 / 2 + \epsilon} \| v \| _ {2} \end{array}\tag{9.3}
$$

9.1.2. Variant for$\Gamma \backslash \mathrm { S L _ { 2 } } ( \mathbb { R } )$. Let$0 \le \alpha \le 1 / 2$, suppose$G = \mathrm { S L } _ { 2 } ( \mathbb { R } )$, and let$V$be a unitary representation of G such that$V$does not weakly contain any complementary series with parameter$\geq \alpha$. The normalization is again so that$\alpha = 0$corresponds to tempered and$\alpha = 1 / 2$corresponds to V not having almost invariant vectors.

Then one has the following variant of (9.1), proved by the same method:

$$
\langle \pi (\left( \begin{array}{c c} y ^ {1 / 2} & 0 \\ 0 & y ^ {- 1 / 2} \end{array} \right) w _ {1}, w _ {2} \rangle \ll_ {\epsilon} \dim (\mathrm{SO} (2) \cdot w _ {1}) ^ {1 / 2} \dim (\mathrm{SO} (2) \cdot w _ {2}) ^ {1 / 2} (1 + | y |) ^ {\alpha - 1 / 2 + \epsilon}. \tag {3.4}\tag{9.4}
$$

It is convenient to extend the validity of (9.4) beyond the K-finite space by replacing dim$. ( \mathrm { S O } ( 2 ) w _ { i } )$by appropriate Sobolev norms. We confine ourselves to the case of main interest, where$V$is the orthogonal complements of the constants in$L ^ { 2 } ( \Gamma \backslash \mathrm { S L _ { 2 } } ( \mathbb { R } ) )$), where Γ is a lattice in$\operatorname { S L _ { 2 } } ( \mathbb { R } )$. The estimates we are about to describe are, again, not new; estimates for efective mixing of geodesic and horocycle flows in this setting are contained in [27].

For our purposes it would be optimal to use fractional Sobolev norms; since we have not defined these, we shall use a rather crude form of interpolation instead.

Thus let$f _ { 1 } , f _ { 2 } \in C ^ { \infty } ( \Gamma \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } ) )$. One expands both$f _ { 1 }$and$f _ { 2 }$into a sum of SO(2)-types and applies (9.4). Indeed, write for$i \in \{ 1 , 2 \}$an expansion$f _ { i } =$ $\scriptstyle \sum _ { n = - \infty } ^ { \infty } f _ { i } ^ { ( n ) }$, where$f _ { i } ^ { ( n ) }$transforms under the character$\left( \begin{array} { c c } { \cos ( \theta ) } & { \sin ( \theta ) } \\ { - \sin ( \theta ) } & { \cos ( \theta ) } \end{array} \right) \mapsto$ $e ^ { i n \theta }$. Expanding:

$$
\begin{array}{l} \langle \left( \begin{array}{c c} y ^ {1 / 2} & 0 \\ 0 & y ^ {- 1 / 2} \end{array} \right) f _ {1}, f _ {2} \rangle = \sum_ {n, m \in \mathbb {Z}} \langle \left( \begin{array}{c c} y ^ {1 / 2} & 0 \\ 0 & y ^ {- 1 / 2} \end{array} \right) f _ {1} ^ {(n)}, f _ {2} ^ {(m)} \rangle \\ \ll_ {\epsilon} (1 + | y |) ^ {\alpha - 1 / 2 + \epsilon} \sum_ {n, m} \| f _ {1} ^ {(n)} \| _ {2} \| f ^ {(m)} \| _ {2} = (1 + | y |) ^ {\alpha - 1 / 2 + \epsilon} \left(\sum_ {n} \| f _ {1} ^ {(n)} \| _ {2}\right) \left(\sum_ {m} \| f _ {2} ^ {(m)} \| _ {2}\right) \end{array} \tag {9.5}
$$

Our definitions of the Sobolev norms (Sec. 2.9.2) are so that$\begin{array} { r } { S _ { 2 , 1 } ( f _ { 1 } ) ^ { 2 } \gg \sum _ { n } ( 1 + } \end{array}$ $| n | ) ^ { 2 } \| f _ { 1 } ^ { ( n ) } \| _ { 2 } ^ { 2 }$, and similarly for$f _ { 2 }$. On the other hand, it is an elementary estimate

that

$$
\left(\sum_ {n} \| f _ {1} ^ {(n)} \| _ {2}\right) ^ {2} \ll_ {\epsilon} \left(\sum_ {n} \| f _ {1} ^ {(n)} \| _ {2} ^ {2} (1 + | n |) ^ {2}\right) ^ {1 / 2 + \epsilon} \left(\sum_ {n} \| f _ {1} ^ {(n)} \| _ {2} ^ {2}\right) ^ {1 / 2 - \epsilon}
$$

It follows from this that for any$k , k ^ { \prime } \in \mathrm { S O } ( 2 )$we have the matrix coeficient bound:

$$
\begin{array}{l} | \langle k \left( \begin{array}{c c} y ^ {1 / 2} & 0 \\ 0 & y ^ {- 1 / 2} \end{array} \right) k ^ {\prime} f _ {1}, f _ {2} \rangle | \\ \qquad \qquad \qquad \ll (1 + | y |) ^ {\alpha - 1 / 2 + \epsilon} (S _ {2, 1} (f _ {1}) S _ {2, 1} (f _ {2})) ^ {1 / 2 + \epsilon} \| f _ {1} \| ^ {1 / 2 - \epsilon} \| f _ {2} \| ^ {1 / 2 - \epsilon}, \end{array}\tag{9.6}
$$

at least for$f _ { 1 } , f _ { 2 }$which are$\mathrm { S O } ( 2 )$-finite. But the general case of smooth$f _ { 1 } , f _ { 2 }$ follows from density.

Note that in (9.6) that the factor$\| f _ { 1 } \| ^ { 1 / 2 - \epsilon } S _ { 2 , 1 } ( f _ { 1 } ) ^ { 1 / 2 + \epsilon }$is a crude substitute for the fractional$( 1 / 2 + \epsilon { - } )$Sobolev norm of$f _ { 1 }$.

9.2. Pointwise bounds. In this section, we make free use of the adelic Sobolev norms introduced in Sec. 2.9.3. We recall the definition$S _ { p , d } : = S _ { p , d , 1 / p }$. We also recall that in statements of the form$| L ( f ) | \ll S _ { p , d } ( f )$, for certain linear functionals $L ,$we shall allow the implicit constant of$\ll$to depend on p and d without explicit mention.

Lemma 9.1. Let$f \in C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathrm { G L } ( 2 ) } )$and let$x \in \mathbf { X } _ { \mathrm { G L } ( 2 ) }$. Then, for any$p \geq 2$and $d \gg 1$，

$$
| f (x) | \ll \mathrm{ht} (x) ^ {1 / p} S _ {p, d} (f)\tag{9.7}
$$

Moreover, if$F \in C ^ { \infty } ( \mathbf { X } \times \mathbf { X } )$, and$p > 2 , d \gg 1$

$$
\int_ {\mathbf {X}} | F (x, x) | d x \ll S _ {p, d} (F)\tag{9.8}
$$

Proof. As in (2.1), set$\begin{array} { r } { K _ { f } = \prod _ { v \mathrm { f i n i t e } } K _ { v , f } } \end{array}$, where$K _ { v , f }$is the stabilizer of$f$in $K _ { v }$. Fix an open neighbourhood of the identity$U \subset \mathrm { G L } _ { 2 } ( F _ { \infty } )$. Consider the map $\Pi : U \cdot K _ { f } \to \mathbf { X }$defined by$( u , k ) \mapsto x u k$. By Lem.$8 . 6 ,$, the fibers are unions of at most$O ( \mathrm { h t } ( x ) )$sets, each of the form$y Z ( \mathbb { A } _ { F } ) \cap U K _ { f }$. Moreover, for any$y \in U \cdot K _ { f }$ the measure of$\{ z \in \mathbb { A } _ { F } ^ { \times } : y a ( z , z ) \in U \cdot K _ { f } \}$is bounded above by a constant depending only on$U$. Indeed, the set of such$z$is contained in a fixed compact subset of$\mathbb { A } _ { F } ^ { \times }$that depends only on$U$

Equip$U \cdot K _ { f }$with the restriction of Haar measure from${ \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$. From the preceding paragraph, one easily deduces that the push-forward of this measure to $\mathbf { X }$, under$( u , k ) \mapsto x u k$, is bounded above by$C \cdot \operatorname { h t } ( x )$times the measure on$\mathbf { X } .$ where the constant C depends only on$U$

Then:

$$
\begin{array}{c} \int_ {u \in U} | f (x u) | ^ {p} = \operatorname{vol} (K _ {f}) ^ {- 1} \int_ {u \in U, k \in K _ {f}} | f (x u k) | ^ {p} d u d k \\ \ll \operatorname{ht} (x) [ K _ {\max}: K _ {f} ] \int_ {\mathbf {X}} | f (x) | ^ {p} d \mu_ {\mathbf {X}} (x) \end{array}\tag{9.9}
$$

(9.9) holds with f replaced by$\mathcal { D } f ,$, for$\mathcal { D }$any fixed monomial in$\mathrm { L i e } ( \mathrm { G L _ { 2 } } ( F _ { \infty } ) )$. The standard Sobolev estimate, applied to the function$u \mapsto f ( x u )$on the real manifold $U _ { ; }$, implies that$| f ( x ) | \ll \mathrm { h t } ( x ) ^ { 1 / p } P S _ { p , d , 1 / p } ( f )$for suficiently large d. (Indeed, it sufices to take any$d > \dim ( U ) / 2 = 2 [ F : \mathbb { Q } ] . )$Then Remark 8.1, (2) implies the conclusion.

As for the second conclusion, we proceed in a similar fashion as above (with X replaced by$\mathbf { X } \times \mathbf { X } )$to obtain the estimate$| F ( x , y ) | \ll \mathrm { h t } ( x ) ^ { 1 / p } \mathrm { h t } ( y ) ^ { 1 / p } S _ { p , d } ( F )$. It is easy to see that$\textstyle \int _ { \mathbf { X } } \mathrm { h t } ( x ) ^ { 2 / p } d x < \infty$for$p > 2 ,$and the conclusion follows.

The next lemma quantifies the rapid decay of a cuspidal function, or more generally a truncated automorphic function, in the cusp. Recall that for$T _ { 0 } > 0$we have defined the Siegel domain${ \mathfrak { S } } ( T _ { 0 } )$in Section 8.2.

Lemma 9.2. Let$f \in C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathrm { G L } ( 2 ) } )$. Put$\begin{array} { r } { f ^ { N } ( g ) = \int _ { N ( F ) \backslash N ( \mathbb { A } _ { F } ) } f ( n g ) d n } \end{array}$, where the measure on${ N ( F ) \backslash N ( \mathbb { A } _ { F } ) }$is the$N ( \mathbb { A } _ { F } )$-invariant probability measure. Then for $x \in \mathfrak { S } ( T _ { 0 } ) , p \geq 2 , k \geq 0$and$d \gg 1$

$$
| f (x) - f ^ {N} (x) | \ll_ {T _ {0}} \mathrm{ht} (x) ^ {1 / p - k} S _ {p, d, 1 / p + k} (f)\tag{9.10}
$$

Proof. We may assume that$x \in N ( \mathbb { A } _ { F } ) A ( \mathbb { R } ) \Omega ( K _ { \infty } \times K _ { \operatorname* { m a x } } )$, for some fixed compact set$\Omega \subset A ( \mathbb { A } _ { F } )$Here$A ( \mathbb { R } )$is regarded as a subset of$A ( F _ { \infty } )$via the natural inclusion$\mathbb { R } \hookrightarrow F _ { \infty }$. Write accordingly$x = n a \omega k$, where$\omega \in \Omega$

Consider the function on$F _ { \infty }$defined by$g ( t ) = f ( n ( t ) x ) - f ^ { N } ( x )$. It is invariant by the lattice$\Lambda = \{ t \in \mathfrak { o } _ { F } : n ( t ) \in \mathrm { G L } _ { 2 } ( F _ { \infty } ) \omega K _ { f } \omega ^ { - 1 } \} ,$, , where$K _ { f }$is again as in $( 2 . 1 )$. One sees that, since ω belongs to the fixed compact$\Omega ,$, the covolume bound vol$( F _ { \infty } / \Lambda ) \ll [ K _ { \operatorname* { m a x } } : K _ { f } ]$. Moreover, since$\Lambda$may be regarded as a fractional ideal of${ \mathfrak { o } } _ { F }$, the homothety class of Λ lies in a fixed compact set in the space of homothety classes of lattices in$F _ { \infty }$. Also,$g ( t )$defines a function on$F _ { \infty } / \Lambda$, with integral 0.

Suppose now that G is a smooth function on$\mathbb { R } ^ { d } / L$, for some$d > 1$and some lattice$L \subset \mathbb { R } ^ { d }$, with integral 0. Let$\| G \| _ { ( i ) } = \operatorname* { s u p } _ { z \in \mathbb { R } ^ { d } / L } | { \mathcal { D } } G |$, where varies over all monomials in$\partial _ { 1 } , \ldots , \partial _ { d }$of exact order i. Then an elementary argument shows that$\| G \| _ { ( 0 ) } \ll \mathrm { v o l } ( \mathbb { R } ^ { d } / L ) ^ { i / d } \| G \| _ { ( i ) }$, and the implicit constant may be taken to vary continuously with the homothety class of L.

Apply this lemma to the function g on$F _ { \infty } / \Lambda$, with$i = k [ F : \mathbb { Q } ]$for some$k \geq 1$ The norm$\left\| g \right\| _ { ( k [ F : \mathbb { Q } ] ) }$, in the sense of the above paragraph, is bounded, by Lem. 9.1 and an elementary computation, by h$\mathrm { t } ( x ) ^ { - k } ( \mathrm { h t } ( x ) ^ { 1 / p } P S _ { p , d ^ { \prime } } ( f ) )$, for some$d ^ { \prime } \gg 1$ It follows that

$$
\sup | g (t) | \ll \mathrm{ht} (x) ^ {1 / p - k} P S _ {p, d ^ {\prime}} (f) [ K _ {\max}: K _ {f} ] ^ {k} = \mathrm{ht} (x) ^ {1 / p - k} P S _ {p, d ^ {\prime}, 1 / p + k} (f).
$$

Applying Rem. 8.1, (2), we conclude$| f ( x ) - f ^ { N } ( x ) | \ll \mathrm { h t } ( x ) ^ { 1 / p - k } S _ { p , d ^ { \prime } , 1 / p + k } ( f )$. 

Lemma 9.3. Suppose$f \in C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathrm { G L } ( 2 ) } )$is cuspidal. Then$S _ { \infty , d , \beta } ( f ) \ll S _ { 2 , d ^ { \prime } , \beta + 3 / 2 } ( f )$，for suficiently large d′.

Proof. By Lem. 9.2 for f cuspidal, applied with$p = 2 , k = 1$, we see that$| f ( x ) | \ll$ $S _ { 2 , d , 3 / 2 } ( f )$for$d \gg 1 . \mathrm { ~ A ~ }$pplying this inequality to$\mathcal { D } f .$, for in the universal enveloping algebra of${ \mathrm { G L } } _ { 2 } ( F _ { \infty } )$, we see that$P S _ { \infty , d , \beta } ( f ) \ll P S _ { 2 , d ^ { \prime } , \beta + 3 / 2 } ( f )$, for$d ^ { \prime }$ suficiently large. This equality holds for cuspidal$f .$

Let Π be the L<sup>2</sup>-orthogonal projection onto the space of cuspidal functions; then Π commutes with${ \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$, and it follows that

$$
P S _ {\infty , d, \beta} (\Pi f) \ll P S _ {2, d ^ {\prime}, \beta + 3 / 2} (\Pi f) \leq P S _ {2, d ^ {\prime}, \beta + 3 / 2} (f)
$$

for arbitrary$f \in C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathrm { G L } ( 2 ) } )$. Now Rem. 8.1, (3) (or, more precisely, a trivial modification thereof) implies the conclusion.

9.3. Equidistribution of long horocycles and closed horospheres. Let G be a semisimple group,$\Gamma \subset G :$a lattice, U a unipotent subgroup of$G .$It is well-known that one can prove, in a quantitative fashion, the equidistribution of$U -$-orbits on $\Gamma \backslash G$if U is a horospherical subgroup, i.e. the unipotent radical of a proper parabolic subgroup. We shall quantify two instances of this that will be of interest to us.

We emphasize that neither the results nor the techniques of this section are new; we have included proofs only to keep the present paper as self-contained as possible.

Efective estimates for equidistribution of long horocycles on quotients of$\operatorname { S L _ { 2 } } ( \mathbb { R } )$ are already implicit in the work of Ratner [25] and [26], where the efective mixing of the horocycle flow is used. We will proceed in a closely related fashion, using the mixing property of the Cartan action; again, this is definitely not new and appears already, although in a diferent context, in the doctoral thesis of Margulis (reprinted in [21]).

9.3.1. Equidistribution of long horocycles in hyperbolic 2-space. Let$\Gamma \subset \mathrm { S L } ( 2 , \mathbb { R } )$ be a lattice such that$L ^ { 2 } ( \Gamma \backslash \mathrm { S L } ( 2 , \mathbb { R } ) )$does not contain any complementary series representation with parameter$\geq \alpha$, for any$0 \leq \alpha < 1 / 2$. (That is:$\alpha \in [ 0 , 1 / 2 )$ is such that all nonzero eigenvalues of the hyperbolic Laplacian$- y ^ { 2 } ( \partial _ { x x } + \partial _ { y y } )$on $\Gamma \backslash \mathbb { H } ^ { 2 }$are bounded below by$1 / 4 - \alpha ^ { 2 } )$.

We define$n , a , \bar { n }$as in (3.1).

The following Lemma quantifies the equidistribution of long horocycles. Results of this type are already implicit in [25] and [26]. This problem is analyzed in much more detail than we go into, in [35] and [11].

Lemma 9.4. Assume Γ is cocompact, and let$x _ { 0 } \in \Gamma \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } )$).

$$
\left| \frac {1}{T} \int_ {t = 0} ^ {T} f (x _ {0} n (t)) d t - \int_ {\Gamma \backslash \mathrm{SL} _ {2} (\mathbb {R})} f (g) d g \right| \ll_ {\epsilon} T ^ {\frac {\alpha - 1 / 2}{2} + \epsilon} S _ {\infty , 1} (f).\tag{9.11}
$$

Proof. The idea (which is certainly not new – cf. remarks at start of Section 9.3) is that, upon flowing a small ball in$\Gamma \backslash G$for a long time by the geodesic flow, it turns into a narrow neighbourhood of a long horocycle. One thereby can deduce the equidistribution of the long horocycle from the mixing properties of the geodesic flow.

Let$N , A , \bar { N }$be the images of$n , a , { \bar { n } }$respectively. Let$g _ { 1 }$be a smooth function of compact support on the real line, with integral$\begin{array} { r } { \int _ { - \infty } ^ { \infty } g _ { 1 } ( x ) d x = 1 } \end{array}$. It will remain fixed for all time throughout our arguments. Fix$1 > \delta > 0$and let$g _ { \delta } : \mathbb { R } \to \mathbb { R }$be the convolution of the characteristic function of [0, 1] with$g _ { 1 } ( x / \delta ) \delta ^ { - 1 }$; that is to say

$$
g _ {\delta} (x) = \delta^ {- 1} \int_ {t = 0} ^ {1} g _ {1} (\frac {x - t}{\delta}) d t.
$$

Then$g _ { \delta }$is a smooth function of integral 1, which is supported in a small interval around [0, 1].

Define a probability measure$\mu _ { \delta }$on$\Gamma \backslash \mathrm { S L _ { 2 } } ( \mathbb { R } )$via the rule

$$
\mu_ {\delta} (f) = \delta^ {- 1} \int_ {x, y, z \in \mathbb {R}} f (x _ {0} n (x) a (e ^ {y}) \bar {n} (z)) g _ {\delta} (x) g _ {1} (y / \delta) g _ {1} (z) d x d y d z.
$$

In words,$\mu _ { \delta }$is a measure supported on a small box around$x _ { 0 } ;$this box has width $O ( 1 )$in the$N$and$\bar { N }$directions, and$O ( \delta )$in the A direction. When we flow this by A, it will become a measure supported along a box that closely approximates an N-orbit.

We observe that

$$
\mu_ {\delta} (a (T ^ {- 1}) f) = \frac {1}{\delta} \int_ {x, y, z} f (x _ {0} a (T) ^ {- 1} n (x) a (e ^ {y}) \bar {n} (z)) g _ {\delta} (x / T) g _ {1} (y / \delta) g _ {1} (T z) d x d y d z.
$$

On the other hand, for any fixed$x _ { 1 } \in \Gamma \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } )$), we note that

$$
\left| \delta^ {- 1} T \int f (x _ {1} a (e ^ {y}) \bar {n} (z)) g _ {1} (y / \delta) g _ {1} (T z) d y d z - f (x _ {1}) \right| \ll \max (T ^ {- 1}, \delta) S _ {\infty , 1} (f).\tag{9.12}
$$

Indeed, (9.12) merely quantifies the fact that the right-hand side integral is against a probability measure supported in a very small ball (of size min$\left( \delta , T ^ { - 1 } \right) )$around $x _ { 1 } .$. Since$\Gamma \backslash \mathrm { S L _ { 2 } } ( \mathbb { R } )$is assumed compact, the implicit constant of$\left( 9 . 1 2 \right)$may be taken independent of$x _ { 1 }$

Consequently,

(9.13)

$$
\left| \frac {1}{T} \int_ {t \in \mathbb {R}} g _ {\delta} (t / T) f (x _ {0} a (T) ^ {- 1} n (t)) d t - \mu_ {\delta} (a (T) ^ {- 1} f) \right| \ll \max (T ^ {- 1}, \delta) S _ {\infty , 1} (f).
$$

On the other hand, the measure$\mu _ { \delta }$has a continuous distribution function$h _ { \delta }$, i.e. $\begin{array} { r } { \mu _ { \delta } ( f ) = \int _ { \Gamma \backslash \mathrm { S L } _ { 2 } ( \mathbb { R } ) } f ( g ) \cdot h _ { \delta } ( g ) d g } \end{array}$, and$\mu _ { \delta } ( a ( T ) ^ { - 1 } f )$may be estimated using (9.6), i.e. the decay of matrix coeficients.

A routine computation shows that$\| h _ { \delta } \| _ { L ^ { 2 } } \ll \delta ^ { - 1 / 2 }$and$S _ { 2 , 1 } ( h _ { \delta } ) \ll \delta ^ { - 3 / 2 } ;$on account of the cocompactness of$\Gamma \backslash \mathrm { S L _ { 2 } } ( \mathbb { R } )$, both these are estimates are uniform in$x _ { 0 }$

Using (9.6) now yields:

$$
\left| \mu_ {\delta} (a (T) ^ {- 1} f) - \int_ {\Gamma \backslash \mathrm{SL} _ {2} (\mathbb {R})} f (g) d g \right| \ll_ {\epsilon} T ^ {\alpha - 1 / 2} S _ {2, 1} (f) \delta^ {- 1 - \epsilon}.\tag{9.14}
$$

Finally, note that if$\chi _ { [ 0 , T ] }$denotes the characteristic function of$[ 0 , T ]$in the real line, then$\begin{array} { r } { \frac { 1 } { T } \int _ { t \in \mathbb { R } } | g _ { \delta } ( t / T ) - \chi _ { [ 0 , T ] } ( t ) | d t \ll \delta } \end{array}$. It follows that

$$
\frac {1}{T} \left| \int_ {0} ^ {T} f (x _ {0} a (T) ^ {- 1} n (t)) d t - \int_ {t} g _ {\delta} (t / T) f (x _ {0} a (T) ^ {- 1} n (t)) d t \right| \ll \delta \cdot S _ {\infty , 0} (f).\tag{9.15}
$$

Combining (9.13), (9.14) and (9.15), and replacing$x _ { 0 }$by$x _ { 0 } a ( T )$, we conclude that the left hand side of (9.11) is bounded by

$$
O _ {\epsilon} \left(S _ {\infty , 1} (f) (\max (T ^ {- 1}, \delta) + T ^ {\alpha - 1 / 2} \delta^ {- 1 - \epsilon} + \delta)\right).
$$

We choose$\delta ^ { 2 } = T ^ { \alpha - 1 / 2 }$to obtain the claimed conclusion.

9.3.2. Equidistribution of large horospheres on higher rank groups. We now prove quantitative equidistribution of large closed horospheres. This result is well-known and generalizes the result of Sarnak, that the closed horocycle$\{ x + i y \} _ { 0 \leq x \leq 1 }$is equidistributed in$\mathrm { S L _ { 2 } ( Z ) } \backslash \mathbb { H }$, as$y  0$

We shall follow the notation of Sec. 3.2, which we briefly reprise. Let$G$be a connected semisimple (real) Lie group,$\Gamma \subset G$a lattice,$K \subset G$the maximal compact subgroup, g the Lie algebra of$G ,$, and$H \in { \mathfrak { g } }$a semisimple element. Fix arbitrarily a norm$\| \cdot \|$on g. We equip$G$with the Haar measure in which$\Gamma \backslash G$ has volume 1. Let$\exp : { \mathfrak { g } } \to G$be the exponential map. Let u be the sum of all negative root spaces for$H ,$and let$U = \exp ( \mathfrak { u } ) \subset G$. Let$x _ { 0 } \in \Gamma \backslash G$be so that$x _ { 0 } U$ is compact; note that the existence of such$x _ { 0 }$implies that$\Gamma \backslash G$is noncompact.

Let$x _ { t } = x _ { 0 } \exp ( t H )$, and let$\Delta _ { t }$be the stabilizer of$x _ { t }$in U. We denote by $\langle \cdot , \cdot \rangle _ { L ^ { 2 } ( \Gamma \backslash G ) }$the inner product in the Hilbert space$L ^ { 2 } ( \Gamma \backslash G )$

Lemma 9.5. There is$\kappa _ { 1 } > 0$such that, for any$f , g \in C ^ { \infty } ( \Gamma \backslash G )$and for any $U \in \mathfrak { u }$with unit length (w.r.t. the fixed norm$\| \cdot \|$on${ \mathfrak { g } } )$we have:

$$
\begin{array}{l} \left| \langle \exp (t H) \cdot f, g \rangle - \int_ {\Gamma \backslash G} f \int_ {\Gamma \backslash G} g \right| \ll \exp (- \kappa_ {1} | t |) S _ {\infty , \dim (K)} (f) S _ {\infty , \dim (K)} (g) \\ \left| \langle \exp (s U) \cdot f, g \rangle - \int_ {\Gamma \backslash G} f \int_ {\Gamma \backslash G} g \right| \ll (1 + | s |) ^ {- \kappa_ {1}} S _ {\infty , \dim (K)} (f) S _ {\infty , \dim (K)} (g) \end{array}\tag{9.16}
$$

Of course the constant$\kappa _ { 1 }$will depend on the choice of the norm$\| \cdot \|$

Proof. This follows from a nice result of Kleinbock and Margulis: see [18]. (The orthogonal complement$L _ { 0 } ^ { 2 }$of the identity representation in$L ^ { 2 } ( \Gamma \backslash G )$is isolated, by [18, Thm 1.12], from the trivial representation in the unitary dual of${ \widehat { G } } .$. A suficiently high tensor power of$L _ { 0 } ^ { 2 }$bis therefore tempered, whereupon one applies the bounds of$[ 8 ] . )$Note that [18] only claims the result (in efect) with$S _ { \infty , d }$for some$d ;$the fact that we can take$d = \dim ( K )$follows by explicating the argument just sketched.

Recall the definition of$\nu _ { T }$from Sec. 3.2, that is to say:$\begin{array} { r } { \nu _ { T } ( f ) = \frac { \int _ { \Delta _ { T } \backslash U } f ( x _ { T } u ) d u } { \mathrm { v o l } ( \Delta _ { T } \backslash U ) } . } \end{array}$ Thus$\nu _ { T }$is the measure supported on a closed horosphere, and this horosphere expands as$T \to \infty$. One deduces from Lem. 9.5 that the measures$\nu _ { T }$are equidistributed as$T \to \infty :$

Lemma 9.6. Set$\begin{array} { r } { \kappa _ { 2 } = \frac { \kappa _ { 1 } } { \dim ( G ) + \dim ( K ) + 1 } , \kappa } \end{array}$<sub>1</sub> being as in the previous Lemma. Then, for$T \geq 0$and$f \in C ^ { \infty } ( \Gamma \backslash { \dot { G } } )$

$$
| \nu_ {T} (f) - \int_ {\Gamma \backslash G} f | \ll e ^ {- \kappa_ {2} T} S _ {\infty , d} (f).
$$

Proof. The idea is identical to Lem. 9.4 and we refer to the first paragraph of that proof for a description of it.

Fix a left-invariant Riemannian metric on$G .$. This descends to a metric on $\Gamma \backslash G$. We first choose some “smoothing kernels” on G. For each$\epsilon > 0$, choose a function$k _ { \epsilon } \in C ^ { \infty } ( G )$such that$k _ { \epsilon }$is positive, supported in an ǫ-neighbourhood of the identity,$\textstyle \int _ { G } k _ { \epsilon } = 1$, and so that for any$X _ { 1 } , X _ { 2 } , \ldots , X _ { l } \in { \mathfrak { g } }$we have:

$$
\sup _ {g \in G} | X _ {1} \dots X _ {l} k _ {\epsilon} | \ll_ {X _ {1}, \dots , X _ {l}} \epsilon^ {- l - \dim (G)}.\tag{9.17}
$$

It is easy to see this is possible (for example: choose an appropriate sequence of functions on g and transport to$G$via the exponential map.)

The measure$\nu _ { 0 }$is a U-invariant probability measure supported on the closed orbit$x _ { 0 } U . \quad \nu _ { 0 } \star k _ { \epsilon }$is supported in an ǫ-neighbourhood of$x _ { 0 } U$and is given by integration against$\mathrm { ~ a ~ } C ^ { \infty }$density function$g _ { \epsilon }$, that is:$\begin{array} { r } { \nu _ { 0 } \star k _ { \epsilon } ( f ) = \int _ { \Gamma \backslash G } f g _ { \epsilon } } \end{array}$

Moreover, it follows from (9.17) that$g _ { \epsilon }$satisfies the bounds$S _ {  \infty , l } ( g _ { \epsilon } ) \stackrel { \cdot } { \ll } \epsilon ^ { - l - \dim ( G ) }$2 for any$l \geq 0$

The translate of$\nu _ { 0 } \star k _ { \epsilon }$by$\exp ( - T H )$is supported in an ǫ-neighbourhood of $x _ { T } U ;$note it is essential that$T \geq 0$for this. (Recall – Sec. 2.1 – our conventions are such that the right translate of the point mass at x by$g \in G$is the point mass at$x g ^ { - 1 } . )$)

In fact, one verifies that

$$
\left| \nu_ {T} (f) - \nu_ {0} \star k _ {\epsilon} (\exp (T H) \cdot f) \right| \ll \epsilon S _ {\infty , 1} (f).\tag{9.18}
$$

(Indeed, let$g \in \mathrm { s u p p } ( k _ { \epsilon } )$and let$\delta _ { g }$be the point mass at g. It sufices to check that the identical bound holds for$| \nu _ { T } ( f ) - \nu _ { 0 } \star \delta _ { g } ( \exp ( T H ) \cdot f ) |$, which equals $\left| \nu _ { T } ( f ) - \nu _ { 0 } ( g \exp ( T H ) \cdot f ) \right|$. Let b the sum of non-negative root spaces for H on g. If ǫ is suficiently small, we may write$g = u m$, with$u \in \exp ( \mathfrak { u } )$and$m \in \exp ( { \mathfrak { b } } )$ Moreover, again if ǫ is suficiently small,$u , m$lie in a Cǫ-neighbourhood of the identity, for some fixed constant$C .$Then$\exp ( - T H ) g \exp ( T H ) = u ^ { \prime } m ^ { \prime }$, with $u ^ { \prime } \in \exp ( \mathfrak { u } )$and where$m ^ { \prime } \in \exp ( { \mathfrak { b } } )$is in a$C ^ { \prime }$ǫ-neighbourhood of the identity, for some absolute$C ^ { \prime }$. Also,$\nu _ { 0 } ( g \exp ( T H ) \cdot f ) = \nu _ { T } ( m ^ { \prime } f )$. Thus it sufices to bound $\left| \nu _ { T } ( f ) - \nu _ { T } ( m ^ { \prime } f ) \right|$. But the$L ^ { \infty }$norm of$f - m ^ { \prime } \cdot f$is$\ll \epsilon S _ { \infty , 1 } ( f ) . )$0

On the other hand, by Lem. 9.5, for$T \geq 0 { : }$: we have

$$
\begin{array}{c} \left| \nu_ {0} \star k _ {\epsilon} (\exp (T H) \cdot f) - \int_ {\Gamma \backslash G} f \right| = \left| \langle g _ {\epsilon}, \exp (T H) f \rangle_ {L ^ {2} (\Gamma \backslash G)} - \int_ {\Gamma \backslash G} f \right| \\ \ll \exp (- \kappa_ {1} T) S _ {\infty , \dim (K)} (f) \epsilon^ {- \dim (G) - \dim (K)}. \end{array}\tag{9.19}
$$

It follows from this and (9.18) that

$$
| \nu_ {T} (f) - \int_ {\Gamma \backslash G} f | \ll (\epsilon + \exp (- \kappa_ {1} T) \epsilon^ {- \dim (G) - \dim (K)}) S _ {\infty , \dim (K)} (f).
$$

To conclude, take$\begin{array} { r } { \epsilon = \exp ( - \frac { \kappa _ { 1 } T } { \mathrm { d i m } ( G ) + \mathrm { d i m } ( K ) + 1 } ) . } \end{array}$

9.4. The equidistribution of Hecke orbits and p-adic horocycles. In this section, we prove some “p-adic” equidistribution statements, pertaining to the equidistribution of Hecke points and p-adic horocycles.

In the Lemmas that follow, f will be a prime ideal of$F , { \overline { { \mu } } } _ { \mathfrak { f } }$, the normalized Hecke measure defined subsequent to (2.6), and [f] as defined in Sec. 2.5.

The first Lemma is an adelic version of the fact that the Hecke orbit$T _ { q } ( z )$of a point$z \in \mathrm { S L } ( 2 , \mathbb { Z } ) \backslash \mathbb { H }$is equidistributed, as$z  \infty$

Lemma 9.7. Let$f \in C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathrm { G L } ( 2 ) } )$and f an ideal of$F .$. Then, for$x _ { 0 } \in \mathbf { X } _ { \mathrm { G L } ( 2 ) }$ $d \gg 1$

$$
\left| f \star \overline {{\mu}} _ {\mathfrak {f}} (x _ {0}) - \sum_ {\chi^ {2} = \omega} \chi ([ \mathfrak {f} ]) \chi (x _ {0}) \int_ {x \in \mathbf {X}} f (x) \chi (x) d \mu_ {\mathbf {X}} (x) \right| \ll \mathrm{N} (\mathfrak {f}) ^ {\alpha - 1 / 2 + \epsilon} \mathrm{ht} (x) ^ {1 / 2} S _ {2, d} (f). \tag {9.20}
$$

Here$\chi ( x )$denotes the function$g \mapsto \chi ( \operatorname* { d e t } ( g ) )$on$\mathbf { X }$

Proof. Let$\mathcal { P }$be the projection defined in Sec. 2.7. Let E be the endomorphism $f \mapsto ( f - \mathcal { P } f ) \star \overline { { \mu } } _ { \mathfrak { f } }$of$C _ { \omega } ^ { \infty } ( \mathbf { X } _ { \mathrm { G L } ( 2 ) } )$. The operator E has norm${ \ll } _ { \epsilon } \mathrm { ~ N ( f ) ^ { \alpha - 1 / 2 + } }$ǫ w.r.t. the$L ^ { 2 }$norm (this follows from Lem. 2.1 and the bounds of Sec. 9.1). By Lem. 8.3 it follows that the operator norm of$E \mathrm { w . r . t } S _ { 2 , d , \beta }$is also${ \ll } _ { \epsilon } \mathrm { ~ N ( f ) } ^ { \alpha - 1 / 2 + \epsilon }$

The left hand side of (9.20) is exactly$E f ( x _ { 0 } )$. Now apply Lem. 9.1, with$p = 2$, to conclude.

The next Lemma is an adelic version of the following (again closely connected to equidistribution of Hecke points). Let$Y ( p )$be embedded in$Y ( 1 ) \times Y ( 1 )$(notation of discussion after Prop. 4.1). Then$Y ( p )$is equidistributed as$p  \infty$. The quantification of this is slightly complicated by noncompactness; in particular, we must use Sobolev norms$S _ { p , d }$for$p > 2$. (Cf. discussion in Sec. 2.9.1).

Lemma 9.8. Let q be a prime ideal of${ \mathfrak { o } } _ { F }$. Let$F \in C ^ { \infty } ( \mathbf { X } \times \mathbf { X } )$be$\mathrm { P G L } _ { 2 } ( \mathfrak { o } _ { F _ { \mathfrak { q } } } ) \ \times$ $\mathrm { P G L _ { 2 } } ( \mathfrak { o } _ { F _ { \mathfrak { q } } } )$invariant.Then, for any$d \gg 1 , p > 2$

$$
\left| \int_ {\mathbf {X}} F (x, x a ([ \mathfrak {q} ])) d x - \sum_ {\chi^ {2} = 1} \chi ([ \mathfrak {q} ]) \int_ {\mathbf {X}} F (x, y) \chi (x) \chi (y) d \mu_ {\mathbf {X}} (x) d \mu_ {\mathbf {X}} (y) \right|\tag{9.21}
$$

$$
\ll_ {\epsilon} \mathrm{N} (\mathfrak {q}) ^ {\frac {2 \alpha - 1}{p} + \epsilon} S _ {p, d} (F).
$$

Proof. Let$\sigma$be the measure$\delta _ { 1 } \times \overline { { \mu } } _ { \mathfrak { q } }$on$\mathrm { P G L _ { 2 } } ( F _ { \mathfrak { q } } ) \times \mathrm { P G L _ { 2 } } ( F _ { \mathfrak { q } } )$, where$\delta _ { 1 }$is the measure consisting of a point mass at the identity. Recalling (see (2.6) in the case of a prime ideal, and Section 2.5 for the definition of$K _ { \mathfrak { q } } )$that$\overline { { \mu } } _ { \mathfrak { q } }$is the$K _ { \mathfrak { q } }$-bi-invariant probability measure supported on$K _ { \mathfrak { q } } a ( [ \mathfrak { q } ] ) K _ { \mathfrak { q } }$, we note that

$$
(F \star \sigma) (x, x) = \int_ {k _ {1}, k _ {2} \in K _ {\mathfrak {q}}} F (x, x k _ {1} a ([ \mathfrak {q} ]) k _ {2}) d k _ {1} d k _ {2} = \int_ {K _ {\mathfrak {q}}} F (x k, x k a ([ \mathfrak {q} ])) d k,
$$

where we equip$K _ { \mathfrak { q } }$with the Haar measure of mass 1, and we use the$\mathrm { P G L } _ { 2 } ( \mathfrak { o } _ { F _ { \mathfrak { q } } } ) .$ invariance of$F$at the second step. It follows that

$$
\int_ {\mathbf {X}} F (x, x a ([ \mathfrak {q} ])) d x = \int_ {\mathbf {X}} (F \star \sigma) (x, x) d x.\tag{9.22}
$$

Let$\mathcal { P } _ { 2 }$be as in Sec. 2.7. Let E be the endomorphism of$C ^ { \infty } ( \mathbf { X } \times \mathbf { X } )$defined by$E ( F ) = ( F - \mathcal { P } _ { 2 } F ) \star \sigma$. Combining (9.22) and the easily verified equality

$$
\int_ {\mathbf {X}} \left(\mathscr {P} _ {2} F \star \sigma\right) (x, x) d x = \sum_ {\chi^ {2} = 1} \chi ([ \mathfrak {q} ]) \int_ {\mathbf {X}} F (x, y) \chi (x) \chi (y) d \mu_ {\mathbf {X}} (x) d \mu_ {\mathbf {X}} (y),
$$

we see that the left hand side of (9.21) is precisely$\textstyle \int _ { \mathbf { X } } E F ( x , x ) d x$

Since$\mathcal { P } _ { 2 }$does not increase$L ^ { \infty }$norms, and σ is a probability measure, it follows that the operator norm of$E$w.r.t the$L ^ { \infty }$norm is$\leq 2$. Moreover, the operator norm of$E$w.r.t the$L ^ { 2 }$norm is${ \mathfrak { \ll } } \mathrm { N } ( { \mathfrak { q } } ) ^ { \alpha - 1 / 2 }$, as follows from Lem. 2.1.

Lem. 8.3 now implies that for$2 \leq p \leq \infty$we have the majorization$S _ { p , d } ( E F ) \ll$ $\mathrm { N } ( \mathfrak { q } ) ^ { \frac { 2 \alpha - 1 } { p } + \epsilon } S _ { p , d } ( F )$. Now Lem. 9.1 shows that

$$
| \int_ {\mathbf {X}} E F (x, x) d x | \ll S _ {p, d} (E F) \ll \mathrm{N} (\mathfrak {q}) ^ {\frac {2 \alpha - 1}{p} + \epsilon} S _ {p, d} (F)
$$

for$p > 2 , d \gg 1 ;$whence the conclusion of the Lemma.

The next Lemma shows the equidistribution of certain p-adic horocycle orbits, as p varies. The idea will be as follows: (speaking very loosely, in the case of $\mathrm { S L _ { 2 } ) }$a typical p-adic horocycle orbit, when projected to$\operatorname { S L } ( 2 , \mathbb { Z } ) \backslash$H, looks like$\{ z +$ $\frac { i } { p } \Bigr \} 0 \le i \le p - 1$. This set looks very much like the image, under the p-Hecke operator, of the point$p z$. Thus one can deduce distribution properties of the p-adic horocycle orbit from some standard facts about Hecke operators.

This is a rather ad hoc argument. Let us say a few words about why this problem does not quite fit into the usual setup of such questions. We are proving statements about the distribution of$\mathrm { e . g . }$. p-adic horocycles when p varies. This does not fit easily into the usual context of such matters, where one considers$\mathrm { e . g }$. a fixed unipotent flow on an S-arithmetic homogeneous space. It would be interesting to have a more conceptual and natural way of treating such questions, in the aspect where$^ { 6 6 } p$varies.”

Lemma 9.9. Let$f \in C ^ { \infty } ( \mathbf { X } )$and let f be an integral ideal of${ \mathfrak { o } } _ { F } ,$factorizing as $\begin{array} { r } { \mathfrak { f } = \prod _ { \mathfrak { q } } \mathfrak { q } ^ { e _ { \mathfrak { q } } } } \end{array}$. For each q f, let$s _ { \mathfrak { q } } \geq 0$be a non-negative integer, and suppose$f$is invariant by$\Pi _ { { \mathfrak { q } } | { \mathfrak { f } } } K _ { 0 } [ { \mathfrak { q } } ^ { s _ { \mathfrak { q } } } ]$. Put$\begin{array} { r } { \mathfrak { m } = \prod _ { \mathfrak { q } | \mathfrak { f } } \mathfrak { q } ^ { s _ { \mathfrak { q } } } } \end{array}$. Let η<sub>f</sub> be the Haar probability measure on$\begin{array} { r } { \prod _ { \mathfrak { q } | \mathfrak { f } } N ( \mathfrak { q } ^ { - e _ { \mathfrak { q } } } \mathfrak { o } _ { \mathfrak { q } } ) } \end{array}$and dh the Haar probability measure on$\mathrm { S L } _ { 2 } ( F ) \backslash \mathrm { S L } _ { 2 } ( \mathbb { A } _ { F } )$

Then, for$y \in F ^ { \times } \backslash \mathbb { A } _ { F } ^ { \times }$

$$
\begin{array}{r l} & {\left| f \star \eta_ {\mathfrak {f}} (a (y)) - \int_ {h \in S L _ {2} (F) \backslash \mathrm{SL} _ {2} (\mathbb {A} _ {F})} f (h a (y)) d h \right|} \\ & {\quad \ll_ {\epsilon} \mathrm{N} (\mathfrak {f}) ^ {\alpha - 1 / 2 + \epsilon} \max (\mathrm{N} (\mathfrak {f}) | y |, \frac {1}{\mathrm{N} (\mathfrak {f}) | y |}) ^ {1 / 2} \mathrm{N} (\mathfrak {m}) ^ {3 / 2 + \epsilon} S _ {2, d} (f)} \end{array}\tag{9.23}
$$

Proof. As usual let$K _ { v , f }$be the stabilizer of f in$K _ { v } \ = \ \mathrm { G L } _ { 2 } ( \mathfrak { o } _ { v } )$, so that$K _ { \mathfrak { q } , f }$ contains$K _ { 0 } [ { \mathfrak { q } } ^ { s _ { \mathfrak { q } } } ]$for each q f.

We now define a measure$\tilde { \eta } _ { \mathfrak { q } }$on$\mathrm { P G L _ { 2 } } ( F _ { \mathfrak { q } } )$for each q f. It will “approximate”$\eta _ { \mathfrak { f } }$ but will be composed of Hecke operators.

For those q such that$s _ { \mathfrak { q } } = 0$, put

$$
\tilde {\eta} _ {\mathfrak {q}} = \mathrm{N} (\mathfrak {q}) ^ {- e _ {\mathfrak {q}} / 2} \delta_ {a (\varpi^ {- e _ {\mathfrak {q}}})} \star \mu_ {\mathfrak {q} ^ {e _ {\mathfrak {q}}}} - \mathrm{N} (\mathfrak {q}) ^ {\frac {- e _ {\mathfrak {q}} - 1}{2}} \delta_ {a (\varpi^ {- e _ {\mathfrak {q}} - 1})} \star \mu_ {\mathfrak {q} ^ {e _ {\mathfrak {q}} - 1}}.\tag{9.24}
$$

(We refer to Sec. 2.8 for definitions of µ<sub>?</sub> appearing above.) For q such that $s _ { \mathfrak { q } } ~ \geq ~ 1$, we set$\sigma _ { \mathfrak { q } }$to be the unique bi-$K _ { 0 } [ \mathsf { q } ^ { s _ { \mathsf { q } } } ]$-invariant probability measure on $\dot { K _ { 0 } } [ \mathfrak { q } ^ { s _ { q } } ] a ( \varpi ^ { e _ { q } } ) K _ { 0 } [ \dot { \mathfrak { q } } ^ { s _ { q } } ]$, normalized to have mass 1, and we put$\tilde { \eta } _ { \mathfrak { q } } = \delta _ { a ( \mathfrak { w } ^ { - e _ { \mathfrak { q } } } ) } \star \sigma _ { \mathfrak { q } }$ Finally, set$\begin{array} { r } { \tilde { \eta } _ { \mathfrak { f } } = \prod _ { \mathfrak { q } | \mathfrak { f } } \tilde { \eta } _ { \mathfrak { q } } } \end{array}$

One then verifies by a direct computation that

$$
f \star \eta_ {\mathrm{f}} = f \star \tilde {\eta} _ {\mathrm{f}}\tag{9.25}
$$

The intuition for this statement, in the classical setting, as as follows: let$z \in$ $\mathrm { S L _ { 2 } ( Z ) \backslash \mathbb { H } }$. Then (for a prime number$p )$the set$\{ z + i / p \} _ { 0 \leq i \leq p - 1 }$is the p-Hecke orbit of$p z$, with the point$p ^ { 2 } z$removed. In the case$e _ { \mathfrak { q } } = 1$, the first term on the right hand side of (9.24) corresponds to the p-Hecke orbit of$p z$, and the second term corresponds to removing the point$p ^ { 2 } z$

More formally, to verify (9.25), the unramified computation, at those places where$s _ { \mathfrak { q } } = 0$, is easy; the ramified computation is just Hecke theory at ramified primes, see e.g. [33, Prop 3.33]. <sup>20</sup>

The projection$\mathcal { P }$of Sec. 2.7 commutes with the action of${ \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$, and so (9.25) holds also with f replaced by$\mathcal { P } f$or$f - \mathcal { P } f$. Moreover,$\mathcal { P } f \star \eta _ { \mathfrak { f } } = \mathcal { P } f$. It

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>20</sup>For</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">B = PGL<sub>2</sub>(F<sub>q</sub>)/K<sub>q</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">x0 ∈ B</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">B</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">e<sub>q</sub> − 2i</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">i ≥ 0)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">qv + 1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">S<sub>1</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">≤ e<sub>q</sub> − 1 − 2i</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">a(̟<sup>−e</sup>q )x<sub>0</sub>.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">i ≥ 0)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">S<sub>2</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">a(̟<sup>−e</sup>q<sup>−1</sup>)x<sub>0</sub>.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">S<sub>2</sub> ⊂ S<sub>1</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">n(q<sup>−e</sup>q )-</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">the unramified assertion, let and let x<sub>0</sub> ∈ B be the identity coset. The set has the structure of the vertices of a q<sub>v</sub> + 1-valent tree. Let be the set of all vertices at distance  (some from  Let be the set of all vertices at even distance (some  from  Then and is precisely theS<sub>1</sub> − S<sub>2</sub> orbit of x<sub>0</sub>. As for the ramified case: one notes that, if s<sub>q</sub> > 0, the Haar measure onsq > 0 K<sub>0</sub>[q<sup>s</sup>q ]is just the pushforward of the Haar measure on  by the productn(o<sub>q</sub> ) × a(o<sup>×</sup><sub>q</sub> ) × n¯(q<sup>s</sup>q ) map .(n, a, n¯) 7→ nan¯</span></small>

follows that

$$
f \star \eta_ {\mathrm{f}} (x) = \int_ {h \in S L _ {2} (F) \backslash \mathrm{SL} _ {2} (\mathbb {A} _ {F})} f (h x) d h + (f - \mathscr {P} f) \star \tilde {\eta} _ {\mathrm{f}} (x).\tag{9.26}
$$

Set$\bar { f } = f - \mathcal { P } f$. Then, expanding the term$\bar { f } \star \tilde { \eta } _ { \mathfrak { f } }$

$$
\begin{array}{l} \bar {f} \star \tilde {\eta} _ {\mathfrak {f}} = \sum_ {S \subset \{\mathfrak {q} | \mathfrak {f}, s _ {\mathfrak {q}} = 0 \}} \bar {f} \star \prod_ {\mathfrak {q} | \mathfrak {f}: s _ {\mathfrak {q}} \geq 1} \delta_ {a (\varpi^ {- e _ {\mathfrak {q}}})} \star \sigma_ {\mathfrak {q}} \star \\ \prod_ {\mathfrak {q} | \mathfrak {f}: s _ {\mathfrak {q}} = 0, \mathfrak {q} \notin S} \left(\mathrm{N} (\mathfrak {q}) ^ {- e _ {\mathfrak {q}} / 2} \delta_ {a (\varpi^ {- e _ {\mathfrak {q}}})} \star \mu_ {\mathfrak {q} ^ {e _ {\mathfrak {q}}}}\right) \star \prod_ {\mathfrak {q} \in S} \left(- \mathrm{N} (\mathfrak {q}) ^ {- \frac {e _ {\mathfrak {q}} + 1}{2}} \delta_ {a (\varpi^ {- e _ {\mathfrak {q}} - 1})} \star \mu_ {\mathfrak {q} ^ {e _ {\mathfrak {q}} - 1}}\right) \end{array} \tag {9.27}
$$

We now specialize to the case under consideration where$x = a ( y )$for some $y \in \mathbb { A } _ { F } ^ { \times }$. For$S \subset \{ { \mathfrak { q } } | { \mathfrak { f } } , s _ { \mathfrak { q } } = 0 \}$set

$$
\sigma_ {S} = \prod_ {\mathfrak {q} | \mathfrak {f}: s _ {\mathfrak {q}} \geq 1} \sigma_ {\mathfrak {q}} \prod_ {\mathfrak {q} | \mathfrak {f}: s _ {\mathfrak {q}} = 0, \mathfrak {q} \notin S} \mathrm{N} (\mathfrak {q}) ^ {- e _ {\mathfrak {q}} / 2} \mu_ {\mathfrak {q} ^ {e _ {\mathfrak {q}}}} \star \prod_ {s _ {\mathfrak {q}} = 0, \mathfrak {q} \in S} - \mathrm{N} (\mathfrak {q}) ^ {- \frac {e _ {\mathfrak {q}} + 1}{2}} \mu_ {\mathfrak {q} ^ {e _ {\mathfrak {q}}} - 1}.
$$

With this notation, we have:

$$
\bar {f} \star \tilde {\eta} _ {\mathfrak {f}} (a (y)) = \sum_ {S \subset \{\mathfrak {q} | \mathfrak {f}, s _ {\mathfrak {q}} = 0 \}} \bar {f} \star \sigma_ {S} \left(a (y [ \mathfrak {f} ]) \prod_ {s _ {\mathfrak {q}} = 0, \mathfrak {q} \in S} a ([ \mathfrak {q} ])\right)\tag{9.28}
$$

Now apply Lem. 9.1 to see that, for any$z \in \mathbb { A } _ { F } ^ { \times }$and$d \gg 1$, we have

$$
\bar {f} \star \sigma_ {S} (a (z)) \ll \max (| z |, | z | ^ {- 1}) ^ {1 / 2} P S _ {2, d} (\bar {f} \star \sigma_ {S}),\tag{9.29}
$$

where we have used the easily verified fact that ht$( a ( z ) ) \asymp \operatorname* { m a x } ( \vert z \vert , \vert z \vert ^ { - 1 } )$

Now, for any$f \in C ^ { \infty } ( \mathbf { X } )$, we have

$$
\left[ K _ {\max}: K _ {\bar {f} \star \sigma_ {S}} \right] \leq \prod_ {s _ {\mathfrak {q}} \geq 1} \left[ K _ {\mathfrak {q}}: K _ {0} [ \mathfrak {q} ^ {s _ {\mathfrak {q}}} ] \right] \left[ K _ {\max}: K _ {f} \right] \ll_ {\epsilon} \mathrm{N} (\mathfrak {m}) ^ {1 + \epsilon} \left[ K _ {\max}: K _ {f} \right].
$$

By the bounds on matrix coeficients (9.2), and recalling that$\begin{array} { r } { \mathfrak { m } = \prod _ { \mathfrak { q } | \mathfrak { f } } \mathfrak { q } ^ { s _ { \mathfrak { q } } } } \end{array}$, we compute that

$$
P S _ {2, d} (\bar {f} \star \sigma_ {S}) \ll_ {\epsilon} \mathrm{N} (\mathfrak {m}) ^ {3 / 2 + \epsilon} (\mathrm{N} (\mathfrak {f}) \prod_ {\mathfrak {q} \in S} \mathrm{N} (\mathfrak {q}) ^ {- 1}) ^ {\alpha - 1 / 2 + \epsilon} \prod_ {\mathfrak {q} \in S} \mathrm{N} (\mathfrak {q}) ^ {- 1} P S _ {2, d} (f).
$$

Combining this with (9.28) and (9.29), we find that for each$S \subset \{ { \mathfrak { q } } : s _ { \mathfrak { q } } \geq 1 \}$

$$
\left| \bar {f} \star \tilde {\eta} _ {\mathfrak {f}} (a (y)) \right| \ll_ {\epsilon} \mathrm{N} (\mathfrak {f}) ^ {\alpha - 1 / 2 + \epsilon} \mathrm{N} (\mathfrak {m}) ^ {3 / 2 + \epsilon} \max (\mathrm{N} (\mathfrak {f}) | y |, \mathrm{N} (\mathfrak {f}) ^ {- 1} | y | ^ {- 1}) ^ {1 / 2} P S _ {2, d} (f)\tag{9.30}
$$

This bound is valid for all$f \in C ^ { \infty } ( \mathbf { X } )$, not merely those f that are invariant by $\Pi _ { { \mathfrak { q } } | { \mathfrak { f } } } K _ { 0 } [ { \mathfrak { q } } ^ { s _ { \mathfrak { q } } } ]$. Apply Rem. 8.1, (3) to the endomorphism$f \mapsto \bar { f } \star \tilde { \eta } _ { \mathfrak { f } } ;$this shows that (9.30) remains valid, for any$f \in C ^ { \infty } ( \mathbf { X } )$, if we replace$P S _ { 2 , d }$by$S _ { 2 , d }$on the right hand side. Now, specialize to the case where$f \in C ^ { \infty } ( \mathbf { X } )$is actually $\Pi _ { { \mathfrak { q } } | { \mathfrak { f } } } K _ { 0 } [ { \mathfrak { q } } ^ { s _ { \mathfrak { q } } } ]$-invariant and apply (9.26) to obtain the conclusion of the Lemma.  The Lemma that follows states an adelic version of the following fact: the measure on$\mathrm { S L _ { 2 } ( Z ) \backslash l }$H defined by$\begin{array} { r } { \nu _ { y } : = q ^ { - 1 } \sum _ { 0 \leq x \leq q - 1 } \delta _ { \frac { x } { q } + i y } . } \end{array}$, approximates the uniform measure if$y \asymp q ^ { - 1 }$; more precisely we have an inequality that$\begin{array} { r } { \left| \nu _ { y } ( f ) - \int _ { \mathrm { S L } _ { 2 } ( \mathbb { Z } ) \backslash \mathbb { H } } f \right| } \end{array}$ is bounded by max$( q y , \frac { 1 } { q y } ) ^ { 1 / 2 } q ^ { - \delta } S ( f )$, where S is an appropriate Sobolev norm and $\delta > 0$

Lemma 9.10. Let$f \in C ^ { \infty } ( \mathbf { X } )$and let notations be as in$S e c$. 6(see esp. (6.4)). In particular, f is an integral ideal of${ \mathfrak { o } } _ { F } , q = \mathrm { N } ( { \mathfrak { f } } )$, [f] is as in$( 2 . 4 )$and

$$
\nu_ {z} (f) = \int_ {| y | = z, y \in \mathbb {A} _ {F} ^ {\times} / F ^ {\times}} f (a (y) n ([ \mathfrak {f} ])) d ^ {\times} y.
$$

Suppose f is invariant by$K _ { 0 } [ { \mathfrak { q } } ^ { s _ { \mathfrak { q } } } ] _ { \mathfrak { i } }$, for each${ \mathfrak { q } } | { \mathfrak { f } }$, and put$\begin{array} { r } { \mathfrak { m } = \prod _ { \mathfrak { q } | \mathfrak { f } } \mathfrak { q } ^ { s _ { \mathfrak { q } } } } \end{array}$. Then

$$
\begin{array}{c} \left| \nu_ {z} (f) - \int_ {\mathbf {X}} f (x) d \mu_ {\mathbf {X}} (x) \right| \\ \ll_ {\epsilon} \mathrm{N} (\mathfrak {f}) ^ {\alpha - 1 / 2 + \epsilon} \mathrm{N} (\mathfrak {m}) ^ {3 / 2 + \epsilon} \max (\mathrm{N} (\mathfrak {f}) z, \frac {1}{\mathrm{N} (\mathfrak {f}) z}) ^ {1 / 2} S _ {2, d} (f). \end{array}\tag{9.31}
$$

Proof. For each q f and integer$0 \leq e \in \mathbb { Z }$, let$\eta _ { \mathfrak { q } ^ { e } }$be the Haar probability measure on the group$N ( { \mathfrak { q } } ^ { - e } { \mathfrak { o } } _ { \mathfrak { q } } )$. Then, since the assumption implies that$f$is right invariant by$a _ { \mathfrak { q } } \big ( \mathfrak { o } _ { \mathfrak { q } } ^ { \times } \big )$, for each q dividing f, we see that for any$x \in \mathbf { X }$:

$$
\begin{array}{c} \int_ {y \in \mathfrak {o} _ {F _ {\mathfrak {q}}} ^ {\times}} f (x a (y) n _ {\mathfrak {q}} (\varpi_ {\mathfrak {q}} ^ {- e})) d ^ {\times} y = \int_ {y \in \mathfrak {o} _ {F _ {\mathfrak {q}}} ^ {\times}} f (x n _ {\mathfrak {q}} (y \varpi_ {\mathfrak {q}} ^ {- e})) d ^ {\times} y \\ = \frac {f \star (\eta_ {\mathfrak {q} ^ {e}} - \mathrm{N} (\mathfrak {q}) ^ {- 1} \eta_ {\mathfrak {q} ^ {e - 1}}) (x)}{1 - \mathrm{N} (\mathfrak {q}) ^ {- 1}} \end{array}\tag{9.32}
$$

It follows that

$$
\nu_ {z} (f) = \prod_ {\mathfrak {q} | \mathfrak {f}} (1 - \mathrm{N} (\mathfrak {q}) ^ {- 1}) ^ {- 1} \cdot \int_ {y \in \mathbb {A} _ {F} ^ {\times} / F ^ {\times}, | y | = z} f \star \prod_ {\mathfrak {q} | \mathfrak {f}} (\eta_ {\mathfrak {q} _ {\mathfrak {q}} ^ {e}} - \mathrm{N} (\mathfrak {q}) ^ {- 1} \eta_ {\mathfrak {q} ^ {e _ {\mathfrak {q}} - 1}}) (a (y)).
$$

We conclude by applying the previous Lemma.

## 10. Background on Eisenstein series.

This section essentially develops the theory of Eisenstein series on$\mathrm { P G L _ { 2 } }$over a number field. This is needed for the Rankin-Selberg method that we reprise in the next section, which in turn is used in the text to relate a period integral with an L-function.

Let$Z$be a topological space. In this section, we will often speak – in various contexts, often with$Z = \bf { X } \mathrm { ~ o r ~ G L _ { 2 } ( A _ { F } ) } - \mathrm { o f ~ a }$function$F ( s , z )$on$\mathbb { C } \times Z$being “holomorphic” or “holomorphic in$s . \mathbf { \mu } ^ { \mathfrak { s } }$For the purposes of this document, this can be assumed to mean that the function is jointly continuous and holomorphic for each z individually.

Note that$\begin{array} { r } { s \mapsto \int _ { Z } F ( s , z ) d z } \end{array}$, if absolutely convergent and uniformly so in s, defines a holomorphic function. Indeed, it sufices to verify that its integral over a closed curve in the s-variable is zero, which follows by Fubini’s theorem.

Similarly, we will say that$F ( s , z )$is meromorphic if there exists a holomorphic function$h ( s )$so that$h ( s ) F ( s , z )$is holomorphic.

10.1. Construction and basic properties of the Eisenstein series. We recall the Eisenstein series that we shall have need of and its basic properties, following Jacquet [17, 19]. We will need Eisenstein series only on$\mathrm { P G L _ { 2 } }$

10.1.1. Schwarz functions. Let Ψ be a Schwarz-Bruhat function on$\mathbb { A } _ { F } ^ { 2 }$, i.e. Ψ is a finite linear combination of functions$\prod _ { v } \Psi _ { v }$, where each$\Psi _ { v }$is locally constant of compact support, for v finite,$\Psi _ { v }$is a Schwarz function on$F _ { v } ^ { 2 }$for v infinite, and$\Psi _ { v }$ is the characteristic function of$\mathfrak { o } _ { v } ^ { 2 }$for almost all v.

If v is a real place, choose$a _ { v } \in F _ { v }$so that$e _ { F _ { v } } ( x ) \ = \ e ^ { 2 \pi i a _ { v } x }$, and say a Schwarz function$\Psi _ { v }$on$F _ { v } ^ { 2 }$is standard if it is the product of a polynomial and $e ^ { - \pi | a _ { v } | _ { v } ( | x | _ { v } ^ { 2 } + | y | _ { v } ^ { 2 } ) }$. If v is a complex place, choose$a _ { v } \in F _ { v }$so that$e _ { F _ { v } } ( x ) \ =$ $e ^ { 2 \pi i \mathrm { T r } _ { \mathbb { C } / \mathbb { R } } \left( a _ { v } x \right) }$; we say that a Schwarz function$\Psi _ { v }$is standard if it is the product of a polynomial and$e ^ { - 2 \pi | a | _ { v } ^ { 1 / 2 } ( | x | _ { v } + | y | _ { v } ) }$. The significance of this normalization is twofold: a standard function is automatically$K _ { v }$-finite and also the class of standard functions is self-dual under the Fourier transform corresponding to the character$e _ { F _ { v } }$

If V is a real vector space, then by a Schwarz norm on the space of Schwarz functions on$V ,$, we shall mean a norm$s$of the form

$$
\mathcal {S} (\Psi) = \sup _ {\mathcal {D}} \sup _ {x} | (1 + \| x \|) ^ {M} \mathcal {D} \Psi |,\tag{10.1}
$$

for some finite collection of constant-coeficients diferential operators$\mathcal { D }$on$V$and some norm$\lVert x \rVert$on$V$

Put, for$g \in { \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$，

$$
f _ {\Psi} (s, g) = | \det (g) | ^ {s} \int_ {t \in \mathbb {A} _ {F} ^ {\times}} \Psi ((0, t) g) | t | ^ {2 s} d ^ {\times} t.
$$

The integral converges absolutely for$\Re ( s ) > 1 / 2$and extends to a meromorphic function of s with possible poles at most at$s = 0 , 1 / 2$. Moreover, for all$s ,$

$$
f _ {\Psi} (\left( \begin{array}{c c} a & x \\ 0 & b \end{array} \right) g) = | a / b | ^ {s} f (g).\tag{10.2}
$$

Put$\begin{array} { r } { E _ { \Psi } ( s , g ) = \sum _ { \gamma \in B ( F ) \backslash \mathrm { G L } _ { 2 } ( F ) } f ( s , \gamma g ) } \end{array}$. This converges when$\operatorname { R e } ( s ) > 1$, extends to a meromorphic function of s with a simple pole at$s = 0 , 1$and satisfies the functional equation

$$
E _ {\Psi} (s, g) = E _ {\hat {\Psi}} (1 - s, g),
$$

where$\widehat { \Psi }$is the Fourier transform

$$
\widehat {\Psi} (x _ {1}, y _ {1}) = \int_ {\mathbb {A} _ {F} ^ {2}} \Psi (x, y) e _ {F} (x _ {1} y - y _ {1} x) d x d y.\tag{10.3}
$$

Moreover, the pole at$s = 1$is the constant function with value$\begin{array} { r } { c _ { 1 } \int _ { \mathbb { A } _ { E } ^ { 2 } } \Psi ( x , y ) d x d y } \end{array}$ and the pole at$s = 0$is the constant function with value$c _ { 2 } \Psi ( 0 )$, where$c _ { 1 } , c _ { 2 }$are constants (depending only on the choice of measure). Finally, for any fixed g the function$s \mapsto s ( 1 - s ) E _ { \Psi } ( s , g )$decays rapidly in vertical strips, i.e.$( 1 + | s | ) ^ { N } | s ( 1 -$ $s ) E _ { \Psi } ( s , g ) ($is bounded in any strip$A \leq \Re ( s ) \leq B$. The proof of all these properties follows from “Poisson summation” for$F ^ { 2 } \dot { \subset } \mathbb { A } _ { F } ^ { 2 }$, and we omit them.

Moreover, the association$\Psi \mapsto E _ { \Psi }$is twisted-equivariant for the natural${ \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } ) .$ action on the space of Schwarz functions and on$C ^ { \infty } ( \mathbf { X } )$: that is to say,

$$
E _ {h. \Psi} (s, g) = | \det (h) | ^ {- s} (h \cdot E _ {\Psi} (s, g)),\tag{10.4}
$$

where$h \cdot$denotes right translation by h.

We give an example with$F = \mathbb { Q } \ ( \mathrm { c f . \ [ 1 5 , ( 3 . 2 9 ) ] ) }$.

Example 10.1. Suppose$\begin{array} { r } { { \cal F } = \mathbb { Q } , \Psi = \prod _ { v } \Psi . } \end{array}$where, for each finite$v , \ \Psi _ { v }$is the characteristic function of the maximal compact of$F _ { v } ,$, and$\Psi _ { \infty } ( x , y ) = e ^ { - \pi ( x ^ { 2 } + y ^ { 2 } ) }$ Then$E _ { \Psi } ( g )$is determined by its restriction to$\operatorname { S L _ { 2 } } ( \mathbb { R } )$

Moreover,$E _ { \Psi } ( s , g )$descends from a function of$\dot { \cdot } g \in \mathrm { S L } _ { 2 } ( \mathbb { R } )$to a function$E ^ { * } ( s , z )$ on$\mathbb { H } = \mathrm { S L _ { 2 } ( \mathbb { R } ) / S O _ { 2 } }$, where the identification is$g \mapsto g \cdot i . ~ I n ~ f a c t ,$

$$
E ^ {*} (s, z) = \pi^ {- s} \Gamma (s) \zeta (2 s) \sum_ {[ c: d ] \in \mathbb {P} ^ {1} (\mathbb {Q})} \frac {y ^ {s}}{| c z + d | ^ {2 s}}.\tag{10.5}
$$

If we put$\xi ( s ) = \pi ^ { - s / 2 } \Gamma ( s / 2 ) \zeta ( s )$, then$E ^ { * } ( s , z )$has the Fourier expansion (10.6)

$$
E ^ {*} (s, z) = \xi (2 s) y ^ {s} + \xi (2 - 2 s) y ^ {1 - s} + 4 \sqrt {y} \sum_ {n \in \mathbb {N}} K _ {s - 1 / 2} (2 \pi n y) \cos (2 \pi n y) \sum_ {a b = n} \left(\frac {a}{b}\right) ^ {s - 1 / 2}
$$

It satisfies the functional equation$E ^ { * } ( s , z ) = E ^ { * } ( 1 - s , z )$. Moreover it is a meromorphic function of s with poles precisely at$s = 0$and$s = 1$. In both cases the residue is the constant function.

Motivated by this example, the reader may find it helpful to keep in mind the “dictiona${ \mathrm {  ~ \cdot ~ } }  { \mathbf { y } } ^ { \prime \prime } : f _ { \Psi } ( s , g )$corresponds to$\pi ^ { - s } \Gamma ( s ) \zeta ( 2 s ) y ^ { s } = \xi ( 2 s ) y ^ { s }$, and$E _ { \Psi } ( s , g )$to $E ^ { * } ( s , z )$as defined in (10.5).

Remark 10.1. Suppose Ψ is invariant by$K _ { \infty } \times K _ { \operatorname* { m a x } }$. Then$f _ { \Psi }$is a multiple of $g \mapsto \mathrm { h t } ( g ) ^ { s }$, as follows from the uniqueness of spherical functions satisfying (10.2). Thus, for$\begin{array} { r } { \Re ( s ) > 1 , E _ { \Psi } ( s , g ) = c ( s ) \sum _ { \gamma \in B ( F ) \backslash \mathrm { G L } _ { 2 } ( F ) } \mathrm { h t } ( \gamma g ) ^ { s } } \end{array}$

We now proceed to establish the “standard” properties of the Eisenstein series for${ { \cal E } } _ { \Psi }$. It is convenient to first recall an explicit bound for archimedean Mellin transforms; the first part is Tate’s thesis, and the second will only be needed much later.

Lemma 10.1. Let v be archimedean and let$\Psi _ { v }$be a Schwarz function on$F _ { v }$. The integral$\begin{array} { r } { G ( s ) : = \int _ { x \in F _ { \ast } ^ { \times } } \Psi _ { v } ( x ) \vert x \vert ^ { s } d ^ { \times } \colon } \end{array}$x extends to a meromorphic function and:

(1)$\frac { G ( s ) } { \zeta _ { F , v } ( s ) }$is holomorphic, where$\zeta _ { F , v } ( s )$is the local factor of the Dedekind ζ-function$o f F a t v$

(2) For any$N \geq 0$, the function$\begin{array} { r } { G _ { N } ( s ) : = \prod _ { i = 0 } ^ { N } ( s + i ) G ( s ) } \end{array}$is holomorphic in$\Re ( s ) \geq - N$, and the absolute value of$( 1 + | s | ) ^ { M } G _ { N } ( s )$in any strip $- N \leq \Re ( s ) \leq A$is bounded by some Schwarz norm (depending on$A , N , M ,$ see (10.1) for the definition) of$\Psi _ { v }$

Proof. The first assertion is Tate’s thesis, and we leave the second to the reader (if any).

Lemma 10.2. The function$s \mapsto s ( 1 / 2 - s ) f _ { \Psi } ( s , g )$extends to a holomorphic function of s. It decays rapidly along vertical lines:

$$
\left| \left(1 + \left| \Im (s) \right|\right) ^ {N} s (1 / 2 - s) f _ {\Psi} (s, g) \right| \ll_ {\Psi} \operatorname{ht} (g) ^ {\Re (s)},\tag{10.7}
$$

where the implicit constant is uniform for$\Re ( s )$in a compact set.

Proof. By (10.2) and the Iwasawa decomposition, it will sufice to prove the assertions in the special case$g \in K _ { \infty } \times K _ { \operatorname* { m a x } }$. So we write$g = k \in K _ { \infty } \times K _ { \operatorname* { m a x } }$and denote by$k _ { v }$the component of k in$\mathrm { P G L } _ { 2 } ( F _ { v } )$. Moreover, without loss of generality, we may assume$\Psi$is a product of Schwarz functions at each place, i.e.$\begin{array} { r } { \Psi = \prod _ { v } \Psi _ { v } } \end{array}$ Then

$$
f _ {\Psi} (s, g) = \prod_ {v \text {infinite}} \int_ {F _ {v} ^ {\times}} \Psi_ {v} ((0, t) k) | t | ^ {2 s} d ^ {\times} t \prod_ {v \text {finite}} \int_ {F _ {v} ^ {\times}} \Psi_ {v} ((0, t) k _ {v}) | t | ^ {2 s} d ^ {\times} t
$$

By Tate’s thesis, it follows that that the product over finite places is of the form $\zeta _ { F } ( 2 s ) h ( s )$, where$\zeta _ { F } ( \cdot )$is the (finite part of the) Dedekind ζ-function of the number field F and$h ( s )$is a holomorphic function with at most polynomial growth in vertical strips (indeed, a polynomial in$q ^ { \pm s }$for various$q )$. All the assertions of the Lemma now follow from Lem. 10.1, and standard facts about the analytic properties of$\zeta _ { F }$

In fact, if the$\Psi _ { v }$for v finite are regarded as fixed, then the implicit constant in$( 1 0 . 7 )$is bounded by an appropriate Schwarz norm, depending on N and the compact set to which$\Re ( s )$is constrained, of$\prod _ { v \mathrm { i n f i n i t e } } \Psi _ { v }$. This follows from the second assertion of Lem. 10.1.

Lemma 10.3. The constant term$\begin{array} { r } { E _ { \Psi } ^ { N } ( s , g ) : = \int _ { x \in F \backslash \mathbb { A } _ { F } } E _ { \Psi } ( s , n ( x ) g ) d \array} \end{array}$dx equals$f _ { \Psi } ( s , g ) +$ $f _ { \widehat { \Psi } } ( 1 - s , g )$

Proof. (Sketch). A double coset decomposition shows that, for$s \gg 1 , E _ { \Psi } ^ { N } ( s , g ) =$ $\begin{array} { r } { f _ { \Psi } ( s , g ) + \int _ { n \in N ( \mathbb { A } _ { F } ) } f _ { \Psi } ( s , w n g ) d n } \end{array}$. So it will sufice to show that$\begin{array} { r l } { \int _ { n \in N ( \mathbb { A } _ { F } ) } f _ { \Psi } ( s , w n g ) \ d s = } & { { } } \end{array}$ $f _ { \widehat { \Psi } } ( 1 - s , g )$. The left-hand side may be expressed as

$$
\begin{array}{r l} & {| \det (g) | ^ {s} \int_ {t \in \mathbb {A} _ {F} ^ {\times}} \int_ {x \in \mathbb {A} _ {F}} \Psi ((t, t x) g) | t | ^ {2 s} d ^ {\times} t d x} \\ & {\qquad = | \det (g) | ^ {s} \int_ {t \in \mathbb {A} _ {F} ^ {\times} / F ^ {\times}} \int_ {x \in \mathbb {A} _ {F}} \sum_ {\delta \in F ^ {\times}} \Psi (t (\delta , x) g) | t | ^ {2 s} d ^ {\times} t d x} \end{array}\tag{10.8}
$$

For any Schwarz function Ψ on$\mathbb { A } _ { F } ^ { 2 }$, one has$\begin{array} { r } { \sum _ { \alpha \in F } \int _ { y \in \mathbb { A } _ { F } } \Psi ( \alpha , y ) = \sum _ { \beta \in F } \widehat { \Psi } ( 0 , \beta ) } \end{array}$ bThe result follows from routine manipulation and use of Tate’s functional equation.

We set

$$
\bar {E} _ {\Psi} (s, g) = E _ {\Psi} (s, g) - f _ {\Psi} (s, g) - f _ {\hat {\Psi}} (1 - s, g),\tag{10.9}
$$

so${ \bar { E } } _ { \Psi }$defines a function on$B ( F ) \backslash P G L _ { 2 } ( \mathbb { A } _ { F } )$. It is a “truncated” Eisenstein series where we have removed the constant term. Moreover,$\bar { E } _ { \Psi } ( s , g )$is holomorphic in s (this follows, for example, by computing residues at each of the points$s = 0 , 1 / 2 ,$, 1 and seeing they are all zero). By definition, for$g \in { \mathrm { G L } } _ { 2 } ( \mathbb { A } _ { F } )$we have an equality

$$
E _ {\Psi} (s, g) = \bar {E} _ {\Psi} (s, g) + f _ {\Psi} (s, g) + f _ {\hat {\Psi}} (1 - s, g).\tag{10.10}
$$

Lemma 10.4. Let$T , N > 0$and let$\Re ( s )$lie in a fixed compact subset of R. Then

$$
(1 + | s |) ^ {4} \bar {E} _ {\Psi} (s, g) \ll_ {\Psi , N, T} \mathrm{ht} (g) ^ {- N},\tag{10.11}
$$

for$g \in { \mathfrak { S } } ( T )$. In particular,$i f \Omega \subset \mathbf { X }$is compact, then$s ( 1 - s ) E _ { \Psi } ( s , g )$is uniformly bounded in$| \Re ( s ) | \leq 2 , g \in \Omega$

Proof. We first claim that, for$t \in \mathbb { R }$, we have$| ( 1 + t ^ { 4 } ) \bar { E } _ { \Psi } ( N + 1 + i t , g ) | \ \ll _ { \Psi }$ $\mathrm { h t } ( g ) ^ { - N + \epsilon }$. Indeed, by definition,

$$
\bar {E} _ {\Psi} (s, g) = \sum_ {\gamma \in B (F) \backslash \mathrm{PGL} _ {2} (F), \gamma \notin B (F)} f _ {\Psi} (s, \gamma g) - f _ {\widehat {\Psi}} (1 - s, g).
$$

In view of Lem. 10.2, it will sufice to show that

$$
\sum_ {\gamma \in B (F) \backslash \mathrm{PGL} _ {2} (F), \gamma \notin B (F)} \mathrm{ht} (\gamma g) ^ {\sigma} \ll_ {\epsilon} \mathrm{ht} (g) ^ {1 - \sigma + \epsilon},\tag{10.12}
$$

which follows from (8.10) and (8.11).

Now (10.11) follows at once from the functional equation$\bar { E } _ { \Psi } ( s , g ) = \bar { E } _ { \widehat { \Psi } } ( 1 - s , g )$ the maximal modulus principle in the strip$| \Re ( s ) | \ \leq \ N + 1$b, and the previous Lemma.<sup>21</sup>

The second assertion (involving Ω) follows from (10.7) and (10.11).

We now compute the Fourier coeficients of the Eisenstein series in general. Recall that$e _ { F }$is a fixed additive character of$\mathbb { A } _ { F } / F$

Lemma 10.5. Set$\begin{array} { r } { W _ { \Psi } ( s , g ) = \int _ { x \in F \backslash \mathbb { A } _ { F } } E _ { \Psi } ( s , n ( x ) g ) e _ { F } ( x ) d x } \end{array}$. Then, for$\Re ( s ) > 1$

$$
W _ {\Psi} (a (y)) = | y | ^ {1 - s} \int_ {t \in \mathbb {A} _ {F} ^ {\times}, x \in \mathbb {A} _ {F}} \Psi (t, t x) e _ {F} (x y) | t | ^ {2 s} d x d ^ {\times} t.\tag{10.13}
$$

In particular, if$\Psi = \otimes _ { v } \Psi _ { v }$, then$\begin{array} { r } { W _ { \Psi } = \prod _ { v } W _ { \Psi _ { v } } } \end{array}$, where for$\Re ( s ) > 1$，

$$
W _ {\Psi_ {v}} (a (y)) = | y | _ {v} ^ {1 - s} \int_ {t \in F _ {v} ^ {\times}, x \in F _ {v}} \Psi_ {v} (t, t x) e _ {F} (x y) | t | _ {v} ^ {2 s} d x d ^ {\times} t,
$$

for$y \in F _ { v }$. Finally,$i f \Psi _ { v } ( x , y ) = \varphi _ { 1 } ( x ) \varphi _ { 2 } ( y )$$\omega _ { v }$a character of$F _ { v }$, and$\Re ( s ^ { \prime } ) +$ $| \Re ( s ) | \gg 1$

$$
\begin{array}{r l} & {\int_ {y \in F _ {v} ^ {\times}} W _ {\Psi_ {v}} (a (y)) | y | ^ {s ^ {\prime}} \omega_ {v} (y) d ^ {\times} y} \\ & {\qquad = \int_ {y \in F _ {v} ^ {\times}} \varphi_ {1} (y) | y | ^ {s ^ {\prime} + s} \omega_ {v} (y) d ^ {\times} y \int_ {y \in F _ {v} ^ {\times}} \widehat {\varphi_ {2}} (y) | y | ^ {1 + s ^ {\prime} - s} \omega_ {v} (y) d ^ {\times} y,} \end{array}\tag{10.14}
$$

where$\widehat { \varphi _ { 2 } }$is the Fourier transform, defined by$\begin{array} { r } { \widehat { \varphi _ { 2 } } ( y ) = \int _ { F _ { v } } \varphi _ { 2 } ( y ) e _ { F _ { v } } ( y t ) d t } \end{array}$

Proof. By the Bruhat decomposition,

$$
\begin{array}{r l r} & & W _ {\Psi} (s, g) = \int_ {F \setminus \mathbb {A} _ {F}} e _ {F} (x) \sum_ {\gamma \in B (F) \setminus \mathrm{PGL} _ {2} (F)} f _ {\Psi} (\gamma n (x) g) \\ & & = \int_ {\mathbb {A} _ {F}} f _ {\Psi} (w n (x) g) e _ {F} (x) d x. \end{array}\tag{10.15}
$$

Thus

$$
\begin{array}{r l} & W _ {\Psi} (s, g) = | \det (g) | ^ {s} \int_ {x \in \mathbb {A} _ {F}} \int_ {t \in \mathbb {A} _ {F} ^ {\times}} \Psi ((t, 0) n (x) g) d ^ {\times} t | t | ^ {2 s} e _ {F} (x) \\ & \qquad = | \det (g) | ^ {s} \int_ {t \in \mathbb {A} _ {F}, x \in \mathbb {A} _ {F} ^ {\times}} \Psi ((t, t x) g) | t | ^ {2 s} e _ {F} (x) d x d ^ {\times} t. \end{array}\tag{10.16}
$$

The claimed conclusion follows upon substituting$g = a ( y )$, together with some routine computations.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">E<sup>¯</sup><sub>Ψ</sub>,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f<sub>Ψ</sub>.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">E<sub>Ψ</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^ { 2 1 } \mathrm { T } _ { 0 }$apply the maximal modulus principle in this context, one needs some a priori decay of which follows easily from the corresponding properties of and</span></small>

Remark 10.2. Remark that$W _ { \Psi } ( s , g )$belongs to the Whittaker model of a certain induced representation of$\mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$, namely that representation$\pi ( s )$induced from the character$a ( y ) \mapsto | y | ^ { s - 1 / 2 }$of the maximal torus (unitary induction, so$\pi ( s )$is tempered for$\Re ( s ) = 1 / 2 )$. This representation is the tensor product of local representations$\pi _ { v } ( s )$, analogously defined; these local representations are irreducible and generic for all s.

Thus (10.13) determines$W _ { \Psi }$uniquely (the theory of the Kirillov model). Similarly the condition$W _ { \Psi _ { v } , s } ( 1 ) = 1$uniquely determines the (spherical) vector$W _ { \Psi _ { v } , s }$

We finally remark that$W _ { \Psi _ { v } , s } ,$, as$\Psi _ { v }$ranges over all Schwarz-Bruhat functions on$F _ { v } ^ { 2 }$if v is nonarchimedean, or over all standard functions if v is archimedean, exhausts the Whittaker model of$\pi ( s )$. Indeed, the set of such functions$W _ { \Psi _ { v } , s }$is a subspace of the Whittaker model of$\pi ( s )$that is stable under the action of the Hecke algebra of$\mathrm { P G L _ { 2 } } ( F _ { v } )$; this action is irreducible, whence the result.

We recall that d denotes the diferent (Sec. 2.3) and we denote by$\zeta _ { F , v } ( s )$or simply$\zeta _ { v } ( s )$the local factor of the Dedekind ζ-function of$F$at the place v.

Corollary 10.1. Suppose v is nonarchimedean, and$\Psi _ { v }$the characteristic function $o f \ { \mathfrak { o } } _ { v } ^ { 2 }$. Then$W _ { v } ( a ( y ) )$satisfies

$$
\int_ {F _ {v} ^ {\times}} W _ {v} (a (y)) | y | ^ {s ^ {\prime}} d ^ {\times} y = q _ {v} ^ {d _ {v} (1 + s ^ {\prime} - s)} \zeta_ {v} (s + s ^ {\prime}) \zeta_ {v} (1 - s + s ^ {\prime}),\tag{10.17}
$$

with$d _ { v } = v ( \mathfrak { d } )$. Note that this specifies$W _ { v }$, because it is$K _ { v }  – i n v a r i a n t$

In particular, for each finite v with$v ( \mathfrak { d } ) = 0$, the function$W _ { v } ( g )$is the unique spherical Whittaker function on$\mathrm { G L _ { 2 } } ( F _ { v } )$with Hecke eigenvalue$q _ { v } ^ { s } + q _ { v } ^ { 1 - s }$, and with $W _ { v } ( 1 ) = 1$

As is evident from$( 1 0 . 6 )$, the Eisenstein series themselves are not bounded. They belong to$L ^ { 2 - \varepsilon }$, but not$L ^ { 2 }$. To avoid some dificulties with growth, we shall use wave-packets of Eisenstein series. We now turn to their analysis.

10.2. Regularization of Eisenstein series on$\mathrm { P G L _ { 2 } }$. Our aim in this section is to show that an appropriate “wave packet” of the Eisenstein series$E _ { \Psi } ( g , s )$ constructed in the previous section lies in$L ^ { \infty }$

Note that, in Example 10.1 above$E ^ { * } ( s , z )$difers from the usual unitary Eisenstein series by a factor$\xi ( 2 s )$. This factor ensures that$E ^ { * } ( s , z )$is holomorphic, but this causes an inconvenience at$s = 1 / 2$, which will manifest itself in our construction of bounded wave-packets. Recall that this pole can be interpreted rather naturally: see footnote on p. 38.

Let$\kappa > 0 .$, and let$\mathcal { H } ( \kappa )$be the family of functions holomorphic in an open neighbourhood of the strip$- \kappa \leq \Re ( s ) \leq 1 + \kappa .$, with rapid polynomial decay in vertical strips (i.e.$\begin{array} { r } { \operatorname* { s u p } _ { t \in \mathbb { R } } ( 1 + | t | ) ^ { N } | h ( \sigma + i t ) | } \end{array}$is bounded, for each$N .$, by a continuous function of$\sigma )$and satisfying$\begin{array} { r } { h ( 0 ) = h ( \frac { 1 } { 2 } ) = h ( 1 ) = 0 } \end{array}$. For each$N \in \mathbb { Z }$we have a norm$\| \cdot \| _ { N }$on$\textstyle { \mathcal { H } } ( \kappa )$defined via:

$$
\| h \| _ {N} = \int_ {- \infty} ^ {\infty} \left(| h (1 + \kappa + i t) | + | h (- \kappa + i t) |\right) (1 + | t |) ^ {N} d t.\tag{10.18}
$$

Lemma 10.6. Let$h \in { \mathcal { H } } ( \kappa )$, and set$\begin{array} { r } { E _ { h , \Psi } ( g ) = \int _ { \mathfrak { R } ( s ) = 1 + \kappa } h ( s ) E _ { \Psi } ( g , s ) d s } \end{array}$. Then:

$$
\left\| E _ {h, \Psi} (g) \right\| _ {L ^ {\infty}} \ll_ {\Psi , \kappa , F} \| h \| _ {0}
$$

Proof. In the notation of (10.10)

$$
\begin{array}{l} E _ {h, \Psi} (g) = \int_ {\Re (s) = 1 + \kappa} \bar {E} _ {\Psi} (s, g) h (s) d s + \int_ {\Re (s) = 1 + \kappa} h (s) f _ {\Psi} (s, g) d s \\ \qquad \qquad \qquad + \int_ {\Re (s) = 1 + \kappa} h (s) f _ {\hat {\Psi}} (1 - s, g) d s. \end{array}\tag{10.19}
$$

Fix$T > 0$so that${ \mathfrak { S } } ( T )$surjects onto X (see Section 8.2 for definitions). We will bound each term on the right-hand side of the above equation for$g \in { \mathfrak { S } } ( T )$

By Lem. 10.4, the first term on the right-hand side is$O _ { \Psi , \kappa } ( \| h \| _ { 0 } )$. By Lem. $1 0 . 2 ,$the function$f _ { \widehat { \Psi } } ( 1 - s , g )$is uniformly bounded above in the region$\Re ( s ) =$ $1 + \kappa , g \in \mathfrak { S } ( T )$b; thus the third term on the right-hand side is also$O _ { \Psi , \kappa } ( \| h \| _ { 0 } )$

As for the second term, we shift contours to the line$\Re ( s ) = - \kappa .$. The shift of contours is justified by the rapid decay of$h ( s )$along vertical lines and Lem. 10.2. Moreover, since$h ( 0 ) = h ( 1 / 2 ) = 0$, the function$s \mapsto h ( s ) f _ { \Psi } ( s , g )$has no poles in between the contours.

Applying Lem. 10.2 one more time to control the contour integral along$\Re ( s ) =$ $- \kappa .$, we conclude.

Remark 10.3. Suppose$\begin{array} { r } { \Psi = \prod _ { v } \Psi _ { v } , \Psi _ { v } , } \end{array}$, and the$\Psi _ { v }$are regarded as fixed for v finite. Put$\begin{array} { r } { \Psi _ { f } = \prod _ { v \mathrm { f i n i t e } } \Psi _ { v } , \mathrm { ~ a ~ } } \end{array}$Schwarz function on$\mathbb { A } _ { F , f } ^ { 2 } ,$, and$\begin{array} { r } { \Psi _ { \infty } = \prod _ { v \mathrm { i n f i n i t e } } \Psi _ { v } } \end{array}$. Then the above argument gives the slightly more explicit bound

$$
\left\| E _ {h, \Psi} \right\| _ {L ^ {\infty}} \ll_ {\kappa , \Psi_ {f}} \| h \| _ {0} \mathcal {S} (\Psi_ {\infty})\tag{10.20}
$$

where$s$is a Schwarz norm on$F _ { \infty } ^ { 2 }$. This follows by explicating the above argument, taking into account the last sentence of the proof of Lem. 10.2. Indeed, one obtains even the corresponding bound for Sobolev norms, namely

$$
S _ {\infty , d, \beta} (E _ {h, \Psi}) \ll_ {\kappa , \Psi_ {f}} \| h \| _ {0} \mathcal {S} (\Psi_ {\infty})\tag{10.21}
$$

for an appropriate Schwarz norm of$F _ { \infty } ^ { 2 }$. One deduces this from (10.20) upon noting that, if belongs to the universal enveloping algebra of$\mathrm { S L } _ { 2 } ( F _ { \infty } )$, then, by$( 1 0 . 4 )$ $\mathcal { D } E _ { \Psi } ( s , g ) = E _ { \mathcal { D } \Psi } ( s , g )$, so also$\mathcal { D } E _ { h , \Psi } = E _ { h , D \Psi }$. It is then easy to check that a Schwarz norm of$\mathcal { D } \Psi _ { \infty }$is bounded by a Schwarz norm of$\Psi _ { \infty }$

10.3. Regularization of Eisenstein series on$\mathrm { P G L _ { 2 } \times P G L _ { 2 } }$. In this section we carry out the analogue of Lem. 10.6 in the context of$\mathrm { P G L _ { 2 } \times P G L _ { 2 } }$(this amounts to regularizing the rank 2 Eisenstein series on$\mathrm { P G L _ { 2 } } \times \mathrm { P G L _ { 2 } } )$

To ease the reader’s path, we briefly mention what the point of this section is in classical notation: Suppose$h ( s _ { 1 } , s _ { 2 } )$is holomorphic in two variables inside the square$| \Re ( s _ { 1 } ) | + | \Re ( s _ { 2 } ) | \leq 1 / 2 + \kappa$, and, moreover,$h ( s _ { 1 } , s _ { 2 } )$has zeroes along the six planes defined by any of the linear constraints$s _ { 1 } = 0 , s _ { 1 } = 1 / 2 , s _ { 1 } = - 1 / 2 , s _ { 2 } =$ $0 , s _ { 2 } = - 1 / 2 , s _ { 2 } = 1 / 2$

Define the wave-packet$E _ { h } ( z _ { 1 } , z _ { 2 } )$on$\mathrm { S L _ { 2 } ( \mathbb { Z } ) } \backslash \mathbb { H } \times \mathrm { S L _ { 2 } ( \mathbb { Z } ) } \backslash \mathbb { F }$via

$$
E _ {h} (z _ {1}, z _ {2}) = \int_ {t, t ^ {\prime} \in \mathbb {R}} h (i t _ {1}, i t _ {2}) E ^ {*} (1 / 2 + i t, z _ {1}) E ^ {*} (1 / 2 + i t ^ {\prime}, z _ {2}) d t d t ^ {\prime}.
$$

Here$E ^ { * }$is as in Example 10.1. We shall show – under mild decay conditions on h –that$E _ { h } ( z _ { 1 } , z _ { 2 } )$is majorized, on the product of two fundamental regions, by $\begin{array} { r } { A ( y _ { 1 } , y _ { 2 } ) : = \frac { \sqrt { y _ { 1 } y _ { 2 } } } { y _ { 1 } ^ { 1 / 2 + \kappa } + y _ { 2 } ^ { 1 / 2 + \kappa } } } \end{array}$. Since$\begin{array} { r } { \int _ { y _ { 1 } \geq 1 , y _ { 2 } \geq 1 } A ( y _ { 1 } , y _ { 2 } ) ^ { 4 } \frac { d y _ { 1 } d y _ { 2 } } { y _ { 1 } ^ { 2 } y _ { 2 } ^ { 2 } } } \end{array}$is finite,$E _ { h }$lies in$L ^ { 4 } .$ and even in$L ^ { 4 + \epsilon }$for ǫ small.

As the reader may verify at this point, the majorization is little more than an exercise in complex integration, using the fact that the large contribution to the Eisenstein series comes from the constant term.

We will need to repeatedly shift contours in the setting of a function of two complex variables. To clarify matters, we state the following Lemma, which we will use repeatedly without explicitly invoking it.

Lemma 10.7. Suppose$U \subset \mathbb { R } ^ { 2 }$is an open domain and$f ( z _ { 1 } , z _ { 2 } )$a holomorphic function on the complex domain$\{ ( z _ { 1 } , z _ { 2 } ) \in \mathbb { C } ^ { 2 } : ( \Re ( z _ { 1 } ) , \Re ( z _ { 2 } ) ) \in U \}$. Suppose moreover that there$i s ,$a continuous function$M : U  \mathbb { R }$such that

$$
\sup _ {(t _ {1}, t _ {2}) \in \mathbb {R} ^ {2}} | f (\sigma_ {1} + i t _ {1}, \sigma_ {2} + i t _ {2}) | (1 + | t _ {1} | + | t _ {2} |) ^ {3} \leq M (\sigma_ {1}, \sigma_ {2}).\tag{10.22}
$$

Then the function

$$
\left(\sigma_ {1}, \sigma_ {2}\right) \mapsto \int_ {\Re (z _ {1}) = \sigma_ {1}, \Re (z _ {2}) = \sigma_ {2}} f (z _ {1}, z _ {2}) d z _ {1} d z _ {2}\tag{10.23}
$$

is locally constant on$U$

We omit the easy proof.

We will now introduce a family of normed spaces$\mathcal { H } ^ { ( 2 ) } ( \kappa )$. In fact, the spaces themselves are independent of$\kappa ,$but the norm depends on$\kappa .$These are spaces of holomorphic functions in two variables$z _ { 1 } , z _ { 2 } ;$and the norm, roughly speaking, controls the behavior of h when the real parts of$( z _ { 1 } , z _ { 2 } )$lie in the square$\left| \Re ( z _ { 1 } ) \right| +$ $| \Re ( z _ { 2 } ) | \le 1 / 2 + \kappa$

Definition 10.1. Let$0 < \kappa < 1$. Let$\mathcal { H } ^ { ( 2 ) } ( \kappa )$be the family of functions$h ( z _ { 1 } , z _ { 2 } )$ in two complex variables, holomorphic in a neighbourhood of$( 0 , 0 )$, and satisfying:

(1) Write$\begin{array} { r } { h ^ { \prime } = \frac { h ( z _ { 1 } , z _ { 2 } ) } { z _ { 1 } z _ { 2 } ( 1 / 4 - z _ { 1 } ^ { 2 } ) ( 1 / 4 - z _ { 2 } ^ { 2 } ) } } \end{array}$. Then$h ^ { \prime } { } _ { \mathrm { i } }$, originally a meromorphic function in a neigbourhood$o f 0$, extends to a holomorphic function in the strip $\{ z _ { 1 } : | \Re ( z _ { 1 } ) | \le 2 \} \times \{ z _ { 2 } : | \Re ( z _ { 2 } ) | \le 2 \}$

(2) Growth condition: for every$N \geq 0$

$$
\sup _ {(\sigma , \sigma^ {\prime}) \in [ - 2, 2 ] ^ {2}} \sup _ {t, t ^ {\prime} \in \mathbb {R} ^ {2}} (1 + | t | + | t ^ {\prime} |) ^ {N} h (\sigma + i t, \sigma^ {\prime} + i t) <   \infty
$$

For each$N \in \mathbb { Z }$we introduce a norm on$H ^ { ( 2 ) } ( \kappa )$via:

$$
\| h \| _ {N} = \int_ {(t, t ^ {\prime}) \in \mathbb {R} ^ {2}} \sum_ {\epsilon_ {1}, \epsilon_ {2} \in \{\pm 1 \}} (1 + | t | + | t ^ {\prime} |) ^ {N}\tag{10.24}
$$

$$
\left(\left| h ^ {\prime} \left(\epsilon_ {1} (1 / 2 + \kappa) + i t, i t ^ {\prime}\right) \right| + \left| h ^ {\prime} \left(i t, \epsilon_ {2} (1 / 2 + \kappa) + i t ^ {\prime}\right) \right|\right) d t d t ^ {\prime}.
$$

Lemma 10.8. For$h \in H ^ { ( 2 ) } ( \kappa )$, put

$$
E _ {h, \Psi , \Psi^ {\prime}} (g _ {1}, g _ {2}) = \int_ {\Re (t) = 0} \int_ {\Re (t ^ {\prime}) = 0} h (t, t ^ {\prime}) E _ {\Psi} (g _ {1}, 1 / 2 + t) E _ {\Psi^ {\prime}} (g _ {2}, 1 / 2 + t ^ {\prime}).
$$

Then

$$
E _ {h, \Psi , \Psi^ {\prime}} (x _ {1}, x _ {2}) \ll_ {\Psi , \Psi^ {\prime}} \| h \| _ {0} \frac {\mathrm{ht} (x _ {1}) ^ {1 / 2} \mathrm{ht} (x _ {2}) ^ {1 / 2}}{\mathrm{ht} (x _ {1}) ^ {1 / 2 + \kappa} + \mathrm{ht} (x _ {2}) ^ {1 / 2 + \kappa}}.
$$

Proof. We may assume that$\| h \| _ { 0 } = 1$. Let notations be as established prior to Lem. 10.4. We will proceed as in Lem. 10.6, expanding${ { \cal E } } _ { \Psi }$via (10.10).

It will sufice to give an upper bound, in absolute value, for each of:

(10.25)

$$
I _ {0} (g _ {1}, g _ {2}) = \int_ {t, t ^ {\prime}} h (t, t ^ {\prime}) \bar {E} _ {\Psi_ {1}} (g _ {1}, 1 / 2 + t) \bar {E} _ {\Psi_ {2}} (g _ {2}, 1 / 2 + t ^ {\prime}) d t d t ^ {\prime}\tag{10.26}
$$

$$
I _ {1} (g _ {1}, g _ {2}) = \int_ {t, t ^ {\prime}} h (t, t ^ {\prime}) \bar {E} _ {\Psi_ {1}} (g _ {1}, 1 / 2 + t) f _ {\Psi_ {2}} (g _ {2}, 1 / 2 \pm t ^ {\prime}) d t d t ^ {\prime}\tag{10.27}
$$

$$
I _ {2} (g _ {1}, g _ {2}) = \int_ {t, t ^ {\prime}} h (t, t ^ {\prime}) f _ {\Psi_ {1}} (g _ {1}, 1 / 2 \pm t) \bar {E} _ {\Psi_ {2}} (g _ {2}, 1 / 2 + t ^ {\prime}) d t d t ^ {\prime}\tag{10.28}
$$

$$
I _ {3} (g _ {1}, g _ {2}) = \int_ {t, t ^ {\prime}} h (t, t ^ {\prime}) f _ {\Psi_ {1}} (g _ {1}, 1 / 2 \pm t) f _ {\Psi_ {2}} (g _ {2}, 1 / 2 \pm t ^ {\prime}) d t d t ^ {\prime},
$$

whenever$\Psi _ { 1 } , \Psi _ { 2 }$are Schwarz functions on$\mathbb { A } _ { F } ^ { 2 }$, and in each case the contour of integration is the surface$\Re ( t ) = \Re ( t ^ { \prime } ) = 0$. Moreover, in view of condition (1) in Def. 10.1, each integrand extends to a holomorphic function of$( t , t ^ { \prime } )$in the region $| \mathfrak { R } ( t ) | \le 1 / 2 + \kappa , | \mathfrak { R } ( t ^ { \prime } ) | \le 1 / 2 + \kappa .$

The bound$| I _ { 0 } | \ \ll \ \mathrm { h t } ( g _ { 1 } ) ^ { - N } \mathrm { h t } ( g _ { 2 } ) ^ { - N }$follows from Lem. 10.4, whereas the bounds$| I _ { 1 } | \ll \mathrm { h t } ( g _ { 1 } ) ^ { - N } \mathrm { h t } ( g _ { 2 } ) ^ { - \kappa }$and$| I _ { 2 } | \ll \mathrm { h t } ( g _ { 2 } ) ^ { - N } \mathrm { h t } ( g _ { 1 } ) ^ { - \kappa }$follow from moving the$t ^ { \prime }$(in the case of$I _ { 1 } )$integral to the contour$\Re ( t ^ { \prime } ) = \pm ( 1 / 2 + \kappa )$, applying Lem. 10.4 and Lem. 10.2.

We now turn to$I _ { 3 }$. We shall consider the case where both signs are +, the other cases being similar with appropriate interchanges of sign. Thus set

$$
Z (t, t ^ {\prime}) = h (t, t ^ {\prime}) f _ {\Psi_ {1}} (g _ {1}, 1 / 2 + t) f _ {\Psi_ {2}} (g _ {2}, 1 / 2 + t ^ {\prime})\tag{10.29}
$$

$$
= h ^ {\prime} (t, t ^ {\prime}) t (1 / 4 - t ^ {2}) f _ {\Psi_ {1}} (g _ {1}, 1 / 2 + t) t ^ {\prime} (1 / 4 - t ^ {\prime 2}) f _ {\Psi_ {2}} (g _ {2}, 1 / 2 + t ^ {\prime})
$$

In view of Lem. 10.2, the function$Z ( t , t ^ { \prime } )$satisfies the conditions for$f$in Lem. 10.7. We apply Lem. 10.7 to shift the contour to$\Re ( t ) = - 1 / 2 - \kappa , \Re ( t ^ { \prime } ) = 0$ Now Lem. 10.2 implies that$\mid \int _ { \Re ( t ) = - 1 / 2 - \kappa , \Re ( t ^ { \prime } ) = 0 } Z ( t , t ^ { \prime } ) \mid \ll \mathrm { h t } ( g _ { 2 } ) ^ { 1 / 2 } \mathrm { h t } ( g _ { 1 } ) ^ { - \kappa } . \mathrm { A }$ similar bound holds with$( g _ { 1 } , g _ { 2 } )$interchanged, so in fact we have the stronger bound$\vert Z ( t , t ^ { \prime } ) \vert \ll \mathrm { m i n } ( \mathrm { h t } ( g _ { 2 } ) ^ { 1 / 2 } \mathrm { h t } ( g _ { 1 } ) ^ { - \kappa } , \mathrm { h t } ( g _ { 1 } ) ^ { 1 / 2 } \mathrm { h t } ( g _ { 2 } ) ^ { - \kappa } )$. This may also be written$\begin{array} { r } { | Z ( t , t ^ { \prime } ) | \ll \frac { \mathrm { h t } ( g _ { 1 } ) ^ { 1 / 2 } \mathrm { h t } ( g _ { 2 } ) ^ { 1 / 2 } } { \mathrm { h t } ( g _ { 1 } ) ^ { 1 / 2 + \kappa } + \mathrm { h t } ( g _ { 2 } ) ^ { 1 / 2 + \kappa } } } \end{array}$

Similar considerations apply to the terms in$I _ { 3 }$corresponding to other choices of sign, so we conclude that$\begin{array} { r } { | I _ { 3 } | \ll \frac { \mathrm { h t } ( g _ { 1 } ) ^ { 1 / 2 } \mathrm { h t } ( g _ { 2 } ) ^ { 1 / 2 } } { \mathrm { h t } ( g _ { 1 } ) ^ { 1 / 2 + \kappa } + \mathrm { h t } ( g _ { 2 } ) ^ { 1 / 2 + \kappa } } } \end{array}$

Lemma 10.9. Let notations be as in the previous Lemma. For any$\textstyle p < { \frac { 4 } { 1 - 2 \kappa } }$, any $d , \beta > 0$, there exists N such that

$$
S _ {p, d, \beta} (E _ {h, \Psi}) \ll_ {\Psi , \kappa , p, \beta} \| h \| _ {N}
$$

Proof. Indeed, we note that

$$
\int_ {y _ {1}, y _ {2} \geq 1} \left(\frac {\sqrt {y _ {1} y _ {2}}}{y _ {1} ^ {1 / 2 + \kappa} + y _ {2} ^ {1 / 2 + \kappa}}\right) ^ {p} \frac {d y _ {1} d y _ {2}}{y _ {1} ^ {2} y _ {2} ^ {2}} <   \infty
$$

whenever$\textstyle p < { \frac { 4 } { 1 - 2 \kappa } }$. We apply the previous Lemma and reduction theory to conclude.

## 11. Background on integral representations of L-functions.

The purpose of this section is as follows. The geometric method we have explained in the text yields upper bounds for certain periods; to obtain subconvexity, we need to know that L-functions can be expressed in terms of these periods. This is the whole point of the theory of integral representations of L-functions; however, we cannot quite simply quote from that theory, as we often need e.g. some analytic control on the choice of test vector for which there is no readily available reference.

On occasion we have only sketched proofs in this section, as they amount to simple explications of standard techniques such as the Rankin-Selberg method, and moreover they are in some sense irrelevant to the main point of this paper (which is to bound periods, not L-functions!)

## 11.1. Cuspidal triple product L-functions.

Hypothesis 11.1. Let$\pi _ { 2 }$and$\pi _ { 3 }$be fixed automorphic cuspidal representations of$\mathrm { P G L _ { 2 } }$over$F$. Let$\pi _ { 1 }$be an automorphic cuspidal representation, whose finite conductor is a prime ideal, prime to the finite conductors of$\pi _ { 2 }$and$\pi _ { 3 }$. Suppose that$\pi _ { 1 , \infty }$(the representation of$\mathrm { P G L _ { 2 } } ( F _ { \infty } )$underlying$\pi _ { 1 } )$is restricted to a bounded set; let$\varphi _ { 1 }$be the new vector in$\pi _ { 1 }$

Then there exists finite collections of vectors$\mathcal { F } _ { 2 } \subset \pi _ { 2 } , \mathcal { F } _ { 3 } \subset \pi _ { 3 }$so that, for any such$\pi _ { 1 } ,$, there exist$\varphi _ { j } \in \mathcal { F } _ { j } \ ( j = 2 , 3 )$with

$$
\frac {L (\frac {1}{2} , \pi_ {1} \otimes \pi_ {2} \otimes \pi_ {3})}{\left| \int_ {\mathbf {X}} \varphi_ {2} (x a ([ \mathfrak {p} ])) \varphi_ {3} (x) \varphi_ {1} (x) d x \right| ^ {2}} \ll_ {\epsilon , F, \pi_ {1, \infty}} N (\mathfrak {p}) ^ {1 + \epsilon}\tag{11.1}
$$

Note that no claim is made about the dependence of the constants in (11.1) on $\pi _ { 2 } , \pi _ { 3 }$or the bounded set containing$\pi _ { 1 , \infty } ;$presumably with enough efort one could obtain polynomial dependence on the conductors.

The proof of Hypothesis 11.1 should be, we believe, an elaborate but routine computation of certain p-adic integrals; this has not carried out, but we expect it to be valid.

In the case when$F = \mathbb { Q }$and$\pi _ { 1 } , \pi _ { 2 }$, π holomorphic Hypothesis 11.1 may follow (in a slightly modified form, replacing$\mathrm { P G L _ { 2 } }$by a division algebra) from the work of B¨ocherer and Schulze-Pillot. In any case, there exist good heuristic reasons to believe the Hypothesis: based on a computation of the size of the relevant family, or alternately it is true if one of the$\pi _ { j }$is Eisenstein.

## 11.2. Rankin-Selberg convolutions.

11.2.1. The Rankin-Selberg integral representation. Let$\pi _ { 1 } , \pi _ { 2 }$be two automorphic representations, with$\pi _ { 2 }$cuspidal.

Let$\Psi _ { v }$be a Schwarz-Bruhat function on$F _ { v } ^ { 2 }$such that, for almost all$v , \ \Psi _ { v }$is the characteristic function of$\mathfrak { o } _ { F _ { v } } ^ { 2 }$. Put$\begin{array} { r } { \Psi = \prod _ { v } \Psi _ { v } , \mathrm { ~ a ~ } } \end{array}$Schwarz function on$\mathbb { A } _ { F } ^ { 2 }$. Let $\varphi _ { j }$belong to the space of$\pi _ { j }$for$j = 1 , 2$and put

$$
I (\varphi_ {1}, \varphi_ {2}, \Psi , s) = \int_ {\mathbf {X}} \varphi_ {1} (g) \varphi_ {2} (g) E _ {\Psi} (s, g) d g\tag{11.2}
$$

Unwinding, we see that for$\Re ( s ) > 1$

$$
\begin{array}{l} I (\varphi_ {1}, \varphi_ {2}, \Psi , s) = c _ {F} \int_ {B (F) \backslash \mathrm{PGL} _ {2} (\mathbb {A} _ {F})} f _ {\Psi} (s, g) \varphi_ {1} (g) \varphi_ {2} (g) \\ = c _ {F} \int_ {B (F) \backslash \mathrm{PGL} _ {2} (\mathbb {A} _ {F})} f _ {\Psi} (s, g) \left(\int_ {n \in N (F) \backslash N (\mathbb {A} _ {F})} \varphi_ {1} (n g) \varphi_ {2} (n g) d n\right) d g \end{array}\tag{11.3}
$$

Here the constant$c _ { F }$arises from change of measure: the measure on$\mathbf { X }$is the $\mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$-invariant probability measure, which is not the same as the quotient measure from$\mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$. Note that$c _ { F }$will be unimportant in our arguments, as it depends only on F and we are only interested in bounds.

Put$\begin{array} { r } { W _ { 1 } ( g ) = \int _ { F \backslash \mathbb { A } _ { F } } \varphi _ { 1 } ( n ( x ) g ) e _ { F } ( x ) d x } \end{array}$, and define$W _ { 2 }$similarly but with$e _ { F }$ replaced by$\overline { { e _ { F } } }$. Recall that our normalizations are so that the volume of$\mathbb { A } _ { F } / F$is 1. Fourier inversion shows that$\begin{array} { r } { \varphi _ { i } ( g ) = \sum _ { \alpha \in F ^ { \times } } W _ { i } ( a ( \alpha ) g ) } \end{array}$if$\varphi _ { i }$is cuspidal. Thus, as long as one of$\varphi _ { 1 } , \varphi _ { 2 }$is cuspidal, we see that:

$$
\begin{array}{r} I (\varphi_ {1}, \varphi_ {2}, \Psi , s) = c _ {F} \int_ {B (F) \backslash \mathrm{PGL} _ {2} (\mathbb {A} _ {F})} f _ {\Psi} (s, g) \left(\sum_ {\alpha \in F ^ {\times}} W _ {1} (a (\alpha) g) W _ {2} (a (\alpha) g)\right) \\ = c _ {F} \int_ {N (\mathbb {A} _ {F}) \backslash \mathrm{PGL} _ {2} (\mathbb {A} _ {F})} W _ {1} (g) W _ {2} (g) f _ {\Psi} (s, g) d g \end{array}\tag{11.4}
$$

If$\varphi _ { 1 } , \varphi _ { 2 }$are pure tensors, then there is a corresponding product decomposition $\begin{array} { r } { W _ { 1 } = \prod _ { v } W _ { 1 , v } , W _ { 2 } = \prod _ { v } W _ { 2 , v } , } \end{array}$, where$W _ { j , \ l }$<sub>v</sub> belongs to the local Whittaker model of$\pi _ { j , v } , \mathrm { a }$representation of$\mathrm { P G L _ { 2 } } ( F _ { v } )$. In that case,

$$
I (\varphi_ {1}, \varphi_ {2}, \Psi , s) = c _ {F} \prod_ {v} I _ {v} (W _ {1, v}, W _ {2, v}, \Psi_ {v}, s),\tag{11.5}
$$

where

$$
\begin{array}{l} I _ {v} (W _ {1, v}, W _ {2, v}, \Psi_ {v}, s) = \\ \int_ {N (F _ {v}) \backslash \mathrm{PGL} _ {2} (F _ {v})} W _ {1} (g _ {v}) W _ {2} (g _ {v}) \left(| \det (g _ {v}) | _ {v} ^ {s} \int_ {t \in F _ {v} ^ {\times}} \Psi ((0, t) g _ {v}) | t | ^ {2 s} d ^ {\times} t\right) \end{array}\tag{11.6}
$$

We note that the bracketed quantity, defined a priori for$g _ { v } \in \mathrm { G L } _ { 2 } ( F _ { v } )$, descends to$\mathrm { P G L } _ { 2 } ( F _ { v } )$

Lemma 11.1. Suppose$W _ { 1 , v } , W _ { 2 , \imath }$the new vectors associated to spherical representations$\pi _ { 1 , v } , \pi _ { 2 , v } , \Psi _ { v }$is the characteristic function of$\mathfrak { o } _ { v } ^ { 2 } ,$, and$e _ { F _ { v } }$is unramified. Then$I _ { v } ( W _ { 1 , v } , W _ { 2 , v } , \Psi _ { v } ) = L _ { v } ( s , \pi _ { 1 , v } \otimes \pi _ { 2 , v } )$

If$W _ { 1 , v } , W _ { 2 , v }$are nonzero and$\mathrm { P G L } _ { 2 } ( \mathfrak { o } _ { v } )$)-invariant,$\Psi _ { v }$as above, but$e _ { F _ { v } }$is possibly ramified, then$I _ { v } ( W _ { 1 , v } , W _ { 2 , v } , \Psi _ { v } ) = a q _ { v } ^ { k s } L _ { v } ( s , \pi _ { 1 , v } \times \pi _ { 2 , v } )$where$k \in  { \mathbb { Z } }$ is so that$e _ { F _ { v } }$is trivial on$\varpi _ { v } ^ { - k } \mathfrak { o } _ { \iota }$but not on${ \varpi _ { v } ^ { - k - 1 } } \mathfrak { o } _ { v }$. Moreover,$\textit { a } = 1 \textit { i f }$ $W _ { 1 , v } ( \varpi _ { v } ^ { - k } ) = \bar { W } _ { 2 , v } ( \varpi _ { v } ^ { - k } ) = 1$

Suppose$W _ { 1 , v } , W _ { 2 , v }$are the new vectors associated to$\pi _ { 1 , v }$spherical and$\pi _ { 2 , v }$a Steinberg representation, and that$e _ { F _ { v } }$is unramified. Then, with$\Psi _ { v }$the characteristic function of$\mathfrak { o } _ { v } ^ { 2 }$, we have:

$$
I _ {v} (\pi_ {1, v} \left( \begin{array}{c c} 1 & 0 \\ 0 & \varpi_ {v} \end{array} \right) W _ {1, v}, W _ {2, v}, \Psi_ {v}) = \pm \frac {q _ {v} ^ {s}}{q _ {v} + 1} L (s, \pi_ {1, v} \otimes \pi_ {2, v}).
$$

Proof. See [17, Thm 15.9] for the first assertion. The second assertion is an easy consequence. See Sec. 11.3 for the final assertion.

Applying the Iwasawa decomposition to (11.6) yields the equivalent

$$
\begin{array}{c} I _ {v} (W _ {1, v}, W _ {2, v}, \Psi_ {v}, s) = \int_ {y \in F _ {v} ^ {\times}, k \in K _ {v}} W _ {1} (a (y) k) W _ {2} (a (y) k) | y | ^ {s - 1} d ^ {\times} y \\ \cdot \left(\int_ {t \in F _ {v} ^ {\times}} \Psi ((0, t) k) | t | ^ {2 s} d ^ {\times} t\right) \end{array}\tag{11.7}
$$

11.2.2. Topologizing the space of local representations. The results in [17] provide $\mathrm { \Delta ^ { * } g o o d } ^ { * }$test vectors for the functionals$I _ { v }$when the local representations$\pi _ { 1 , v } , \pi _ { 2 , v }$ are fixed. On the other hand, we will need such results with some mild uniformity in$\pi _ { 1 , v } .$. One can certainly extract the stronger results from the proofs in [17]. For now, we will proceed by deducing the results “by continuity”; to do this, we will need to define the topology on the space of possible$\pi _ { 1 , v }$. The considerations that follow are not really very crucial; it would be better simply to explicate the implicit dependences in [17].

Let$\mathcal { S }$be a finite set of irreducible (continuous) representations of$K _ { v } = \mathrm { P G L } _ { 2 } ( \mathfrak { o } _ { v } )$ For any representation W of$K _ { v } .$we denote by$\dot { W } ^ { \mathcal { S } }$that subspace of W consisting of vectors whose K -span contains only irreducibles that belong to$\mathcal { S }$. We shall say that elements of$\bar { W } ^ { \mathcal { S } }$are of type${ \mathcal { S } } .$

Let$\mathcal { G } _ { v }$be the set of isomorphism classes of generic irreducible representations of $\mathrm { P G L } _ { 2 } ( F _ { v } )$. If π is a generic irreducible representation which is a discrete series or supercuspidal, we shall define it to be isolated. Otherwise, π is induced from two quasicharacters$\mu , \nu : F _ { v } ^ { \times } \to \mathbb { C }$. For$s \in \mathbb { C }$, let$( \pi ( s ) , V ( s ) )$be the representation induced from the quasicharacters$\boldsymbol { \mu } | \cdot | _ { v } ^ { s } , \boldsymbol { \nu } | \cdot | _ { v } ^ { - s }$. Then$\pi ( s )$is generic for all$s \in \mathbb { C }$ and irreducible in a neighbourhood of 0. We shall topologize$\mathcal { G } _ { v }$in such a way that sets of the form$[ \pi ( s ) ]$, for$| s | < \varepsilon$form a basis.

If$E \subset { \mathcal { G } } _ { v }$is a closed subset that is bounded (when considered as a subset of the set of isomorphism classes of irreducible admissible representations, and bounded in the sense of Sec. 2.12.3), then$E$is compact, as one checks by direct verification.

For each$\pi \in \mathcal { G }$, we have a Whittaker model$\mathcal { W } ( \pi )$. Consider a function$\pi \mapsto W _ { \pi }$ that assigns to each$\pi \in \mathcal { G } _ { v }$an element$W _ { \pi }$of its Whittaker model. We shall say that such an assignment π$\mapsto W _ { \pi }$is continuous if there exists a neighbourhood of each π, which we may assume to be of the form,$\{ \pi ( s ) : | s | < \varepsilon \}$, and a set$\mathcal { S }$of irreducible representations of$K _ { v }$so that:

(1)$W _ { \pi ( s ) }$is of type$\mathcal { S }$, for each$| s | < \varepsilon$ (2) The assignment$s \mapsto W _ { \pi ( s ) } ( g )$is continuous for each$g \in \mathrm { P G L } _ { 2 } ( F _ { v } )$, uniformly for$g$in any fixed compact.

It can be verified that if$W _ { 0 }$is an element of the Whittaker model of$\pi _ { 0 }$, there exists a continuous assignment$\pi \mapsto W _ { \pi }$in a neighbourhood of$\pi _ { 0 }$which has the value$W _ { 0 }$at$\pi _ { 0 }$

The requirement (2) is not very strong, as it does not impose any uniformity on all of$\mathrm { P G L } _ { 2 } ( F _ { v } )$. However, in every context we shall consider, the necessary uniformity in$g$is automatic. Let us sketch how one can prove such results. Assume that v is finite; the infinite case is similar although more technically involved. One first observes that if$\pi \mapsto W _ { \pi }$is a continuous assignment on some open set, then, for a fixed character$\chi _ { v }$of$F _ { v } ^ { \times }$, the quotient$\frac { \int _ { y \in F _ { v } ^ { \times } } \tilde { W } _ { \pi } ( a ( y ) ) \chi _ { v } ( y ) | y | ^ { s - 1 / 2 } \tilde { d } ^ { \times } y } { L _ { v } \bigl ( s , \pi _ { v } \otimes \chi _ { v } \bigr ) }$is a polynomial of the form$\scriptstyle \sum _ { k = - N } ^ { N } c _ { k } q _ { v } ^ { k s }$; moreover, the degree N is locally bounded as π varies, and all the coeficients$c _ { k }$can be taken to depend continuously on$\pi$. To verify the local boundedness of the degree – which requires only property (1) above – one just notes that there is (locally) a fixed M such that$W _ { \pi } ( a ( y ) )$vanishes for $| y | _ { v } > M ;$this, together with the functional equation, gives the local boundedness. To see that the coeficients vary continuously, it sufices to check that, for any fixed integer t, the integral$\begin{array} { r } { \int _ { v ( y ) = t } W _ { \pi } ( a ( y ) ) \chi _ { v } ( y ) | y | ^ { s - 1 / 2 } d ^ { \times } y } \end{array}$varies continuously, which follows from the definition of continuity for the assignment$\pi \mapsto W _ { \pi }$. The archimedean case proceeds similarly, but one replaces the role of polynomials in $q _ { v } ^ { \pm s }$by functions of the form$c ^ { s } P ( s )$, where P is a polynomial and$c \in \mathbb { R }$

In the next few pages, we will make certain claims regarding the continuity of various integrals involving$W _ { \pi }$if$\pi \mapsto W _ { \pi }$is a continuous assignment. One can reduce all the claimed continuity statements (by standard “Mellin transform” arguments) to the result just discussed. We will omit the details.

## 11.2.3. Choice of test vectors.

## Lemma 11.2. Let notation be as above.

(1) The quotient

$$
\Xi_ {v} (W _ {1, v}, W _ {2, v}, \Psi_ {v}, s) := \frac {I _ {v} (W _ {1 , v} , W _ {2 , v} , \Psi_ {v} , s)}{L _ {v} (s , \pi_ {1 , v} \otimes \pi_ {2 , v})}
$$

is holomorphic in s. If v is nonarchimedean,$\Xi _ { v }$is a polynomial in$q _ { v } ^ { \pm s } ; i f$ v is archimedean and$\Psi _ { v }$is standard, then$\Xi _ { v } | a _ { v } | _ { v } ^ { 2 s }$is a polynomial in s.

(2) For any fixed$s _ { 0 } ~ \in ~ \mathbb { C }$we may choose data$\left( W _ { 1 , v } , W _ { 2 , v } , \Psi _ { v } \right)$of the type described in (1) with$\Xi _ { v } ( W _ { 1 , v } , W _ { 2 , v } , \Psi _ { v } , s _ { 0 } ) \not = 0$

(3)$I f \pi _ { 2 , v }$is regarded as fixed, and$\pi _ { 1 , v }$remains within a fixed compact subset of$\mathcal { G } _ { v }$consisting entirely of unitarizable representations, then there exists a constant C depending on the compact set so that one may choose data as in$( { \boldsymbol { \mathscr { Z } } } )$in such a way that:

(a)$\Psi _ { v }$and$W _ { 2 , v }$may both be chosen from a finite list of size$\leq C _ { i }$

(b)$\begin{array} { r } { \int _ { F _ { \ast } ^ { \times } } | W _ { 1 , v } ( a ( y ) ) | ^ { 2 } d ^ { \times } y \leq C ; } \end{array}$

(c)$| \Xi _ { v } ( s _ { 0 } ) | \geq 1$and, for all$s \in \mathbb { C } .$, we have$| \Xi _ { v } ( s ) | \ll C ^ { | \Re ( s ) | } ( 1 + | s | ) ^ { C }$

Proof. The first two assertions are in [17].

We will only sketch the last assertion. It can be also be proved directly by exhibiting such data by explicating the arguments of [17]. In any case, we start by noting: Given any continuous assignment$\pi _ { 1 , v } \mapsto W _ { 1 , v } , \pi _ { 2 , v } \mapsto W _ { 2 , v } ,$the function $\Xi _ { v } ( W _ { 1 , v } , W _ { 2 , v } , \Psi _ { v } , s )$and$\begin{array} { r } { \int | W _ { i , v } ( a ( y ) | ^ { 2 } d ^ { \times } y } \end{array}$all varies continously in$\pi _ { 1 , v } , \pi _ { 2 , v }$. This assertion can be deduced by the methods explained in Section 11.2.2. Here, when we speak of$\Xi _ { v } ( W _ { 1 , v } , W _ { 2 , v } , \Psi _ { v } , s )$varying continuously, we mean this in the “strong sense”, i.e the statement that$\Xi _ { v }$can be expressed as a polynomial in$q _ { v } ^ { s }$(nonarchimedean case) or$b ^ { s } P ( s )$where P is polynomial (archimedean case), so that all coeficients vary continuously with$\pi _ { 1 , v } , \pi _ { 2 , v }$

Now, given fix momentarily$\pi _ { 1 , v }$and$\pi _ { 2 , \boldsymbol { \tau } }$and suppose we have chosen data $\left( W _ { 1 , v } , W _ { 2 , v } , \Psi _ { v } \right)$as in (2). Extend$W _ { 1 , v }$to a continuous assignment$\pi \mapsto W _ { \pi }$in a neighbourhood of$\pi _ { 1 , v }$. By the remarks above,$( W _ { \pi } , W _ { 2 , v } , \Psi _ { v } )$will satisfy (3b) and (3c), for a suitable constant$C _ { i }$, whenever π belongs to a suficiently small neighbourhood of$\pi _ { 1 , v }$. Now a compactness argument demonstrates (3).

We emphasize again that (11.6) is valid so long as one of$\pi _ { 1 } , \pi _ { 2 }$is cuspidal.

Lemma 11.3. Let π be an automorphic cuspidal representation in$L ^ { 2 } ( \mathbf { X } )$, and let $\varphi \in \pi$be so that$\begin{array} { r } { W _ { \varphi } : = \int _ { F \backslash \mathbb { A } _ { F } } e _ { F } ( x ) \varphi ( n ( x ) g ) } \end{array}$factorizes as a product$\Pi _ { v } W _ { v } ( g )$ Then, for a certain constant absolute constant c

$$
\int_ {\mathbf {X}} | \varphi (g) | ^ {2} d g = c \mathrm{Res} _ {s = 1} \Lambda (s, \pi \otimes \tilde {\pi}) \prod_ {v} \frac {\int_ {F _ {v} ^ {\times}} | W _ {v} (a (y)) | ^ {2} d ^ {\times} y}{L _ {v} (s , \pi_ {v} \otimes \tilde {\pi} _ {v})}\tag{11.8}
$$

Proof. This follows by taking the residue of$I ( \varphi , \bar { \varphi } , \Psi , s )$at$s = 1$. Indeed, this residue equals, up to a constant depending only on the measure normalization, $\begin{array} { r } { \left( \int _ { \mathbf { X } } | \varphi ( g ) | ^ { 2 } d g \right) \left( \int _ { \mathbb { A } _ { \mathbf { r } } ^ { 2 } } \Psi ( x , y ) d x d y \right) } \end{array}$(see discussion of properties of$E _ { \Psi }$after (10.3).

On the other hand, by (11.5) and (11.6)$I ( \varphi , \bar { \varphi } , \Psi , s )$may be written as a product$\begin{array} { r } { c _ { F } \prod _ { v } I _ { v } ( W _ { v } , \overline { { W _ { v } } } , \Psi _ { v } , s ) } \end{array}$, where each$I _ { v }$is given by$( 1 1 . 7 )$. The integral $\begin{array} { r } { \int _ { F _ { v } ^ { \times } } | W _ { v } ( a ( y ) k ) | ^ { 2 } d ^ { \times } y } \end{array}$is independent of$k \in K _ { v } .$so$I _ { v } ( W _ { v } , \overline { { W _ { v } } } , \Psi _ { v } , 1 )$factors as the product of$\begin{array} { r } { \int _ { y \in F _ { v } ^ { \times } } | W _ { v } ( a ( y ) ) | ^ { 2 } d ^ { \times } y } \end{array}$and$\textstyle \int _ { t \in F _ { v } ^ { \times } , k \in K _ { v } } \Psi _ { v } ( ( 0 , t ) k ) | t | ^ { 2 } d t$. The latter integral difers from$\int _ { F _ { v } ^ { 2 } } \Psi _ { v } ( x , y ) d x d y$by a factor that depends only on the normalizations of measure; moreover, this factor equals$( 1 - q _ { v } ^ { - 2 } ) ^ { - 1 }$for almost all$v ,$so the product of these factors is convergent. The conclusion easily follows.

We now specialize to the cases of interest. Fix$\pi _ { 1 }$. We vary$\pi _ { 2 } : = \pi$through a sequence of automorphic cuspidal representations with prime conductor p, prime to the conductor of$\pi _ { 1 }$. In particular, the local constituent of π at p is a special representation. We denote by$\pi _ { \infty }$the representation of$\mathrm { G L _ { 2 } } ( F _ { \infty } )$underlying the representation π.

Lemma 11.4. Suppose the archimedean constituent$\pi _ { \infty }$belongs to a bounded subset $o f \mathrm { P G L _ { 2 } } ( \widehat { F } _ { \infty } )$(in what follows the implicit constants may depend on this subset) and regard$\pi _ { 1 }$as being fixed.

Let$s _ { 0 } \in \mathbb { C }$. There exists a fixed finite set$\mathcal { F }$of Schwarz Bruhat functions and a real num$\imath b e r ^ { 2 2 } C > 0$so that, for any such$\pi ,$

There exist vectors$\varphi _ { 1 } \in \pi _ { 1 } , \varphi \in \pi$and$\Psi \in { \mathcal { F } }$so that

$$
\Phi (s) := \mathrm{N} (\mathfrak {p}) ^ {1 - s} \frac {I (a ([ \mathfrak {p} ]) \cdot \varphi_ {1} , \varphi , \Psi , s)}{\Lambda (s , \pi_ {1} \otimes \pi)}
$$

is holomorphic and satisfies:

(1)$| \Phi ( s _ { 0 } ) | \gg 1$and$| \Phi ( s ) | \ll C ^ { | \Re ( s ) | } ( 1 + | s | ) ^ { C } ,$

(2) At any nonarchimedean place v such that$\pi _ { 1 }$and$\pi$are both unramified, both$\varphi$and$\varphi _ { 1 }$are invariant by$\mathrm { P G L } _ { 2 } ( \mathfrak { o } _ { F _ { v } } )$;

(3)$\| \varphi _ { 1 } \| _ { L ^ { \infty } } \ i s \ O ( 1 )$

(4)$\| \varphi \| _ { L ^ { 2 } ( \mathbf { X } ) } \ll _ { \epsilon } \mathrm { N } ( \mathfrak { p } ) ^ { \epsilon } .$

Proof. We first choose local data. For each place where$e _ { F , v }$and$\pi _ { 1 }$are not ramified, we take$W _ { v }$(resp.$W _ { v , 1 } )$to be the new vector in the Whittaker model of$\pi _ { v }$(resp $\pi _ { 1 , v } )$. We put$\Psi _ { v }$to be the characteristic function of${ \mathfrak { o } } _ { v } ^ { 2 }$

Let be the set of remaining v. For$v \in B$, the assumptions show that$\pi _ { v }$ is restricted to a bounded set. We choose$W _ { v } , \ W _ { v , 1 } , \Psi _ { v }$for$v \in B$according to Lem. 11.2. Finally we choose$\varphi$so that$\begin{array} { r } { \int _ { x \in F \backslash \mathbb { A } _ { F } } e _ { F } ( x ) \varphi ( n ( x ) g ) = \prod _ { v } W _ { v } ( g ) } \end{array}$, and similarly for$\varphi _ { 1 }$, and take$\begin{array} { r } { \Psi = \prod _ { v } \Psi _ { v } } \end{array}$. The first two assertions of the Lemma are immediate.

To bound the$L ^ { 2 }$norm of$\varphi ,$, use Lem. 11.2 (3b), Lem. 11.3, and Iwaniec’s bounds on L-functions near 1. As for$\varphi _ { 1 }$, it in fact belongs to a fixed finite set of cusp forms, so the third assertion is immediate.

We continue to keep π an automorphic cuspidal representation of$\mathrm { P G L } _ { 2 } ( \mathbb { A } _ { F } )$ with prime conductor.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>22</sup>depending on π<sub>1</sub> and the choice of bounded subset of$\widehat { \mathrm { F G L } _ { 2 } ( F _ { \infty } } )$</span></small>

Lemma 11.5. Suppose$\pi _ { \infty }$belongs to a bounded subset of$\widehat { \mathrm { P G L _ { 2 } } ( F _ { \infty } ) }$(in what follows the implicit constants may depend on this bounded subset).

Let$t _ { 0 } , t _ { 0 } ^ { \prime } \in \mathbb { C }$. There exists a fixed finite set$\mathcal { F }$of Schwarz Bruhat functions and a real number$C > 0$so that:

There exist vectors$\varphi \in \pi , \Psi _ { 1 } , \Psi _ { 2 } \in \mathcal { F }$so that:

$$
\Phi (t, t ^ {\prime}) = \mathrm{N} (\mathfrak {p}) ^ {1 / 2 - t} \frac {\int_ {\mathbf {X}} \varphi (g) E _ {\Psi_ {1}} (g , \frac {1}{2} + t) E _ {\Psi_ {2}} (g a ([ \mathfrak {p} ]) , \frac {1}{2} + t ^ {\prime}) d g}{\Lambda (\frac {1}{2} + t + t ^ {\prime} , \pi) \Lambda (\frac {1}{2} + t - t ^ {\prime} , \pi)}\tag{11.9}
$$

is holomorphic and satisfies:

$$
\left| \Phi (t _ {0}, t _ {0} ^ {\prime}) \right| \gg 1 a n d \left| \Phi (t, t ^ {\prime}) \right| \ll (1 + | t | + | t ^ {\prime} |) ^ {C} C ^ {| \Re (t) | + | \Re (t ^ {\prime}) |}.
$$

(2) For any nonarchimedean place$v ,$each$\Psi _ { 1 }$and$\Psi _ { 2 }$is invariant by$\mathrm { P G L } _ { 2 } ( \mathfrak { o } _ { F _ { v } } )$ (3)$\| \varphi \| _ { L ^ { 2 } ( \mathbf { X } ) } \ll _ { \epsilon } \mathrm { N } ( \mathfrak { p } ) ^ { \epsilon }$

Proof. The proof is similar to that of the previous Lemma; recall that (11.6) was valid as long as one of$\pi _ { 1 } , \pi _ { 2 }$were cuspidal.

Let$\Psi _ { 2 } ^ { \prime }$be the translate of the Schwarz function$\Psi _ { 2 }$by$a ( [ { \mathfrak { p } } ] )$. Then by (10.4),

$$
E _ {\Psi_ {2} ^ {\prime}} (s, g) = \mathrm{N} (\mathfrak {p}) ^ {- s} E _ {\Psi_ {2}} ^ {a ([ \mathfrak {p} ])} (s, g)
$$

Suppose$\Psi _ { 1 } , \Psi _ { 2 }$factorize as$\prod _ { v } \Psi _ { 1 , v } , \prod _ { v } \Psi _ { 2 , v } ,$, and define$W _ { \Psi _ { 1 , v } } ( s , g )$and$W _ { \Psi _ { 2 , v } } ( s , g )$ as in Lem. 10.5. Suppose moreover that$\begin{array} { r } { \int _ { x \in F \backslash \mathbb { A } _ { F } } e _ { F } ( x ) \varphi ( n ( x ) g ) } \end{array}$factorizes as $\Pi _ { v } W _ { v } ( g )$. Then we can express the global integral of$( 1 1 . 9 )$as a product in two different ways, depending on whether we let$E _ { \Psi _ { 1 } }$or$E _ { \Psi _ { 2 } }$play the role of$\pi _ { 2 }$. Namely, as in (11.7):

$$
\begin{array}{l} \int_ {\mathbf {X}} \varphi (g) E _ {\Psi_ {1}} (g, \frac {1}{2} + t) E _ {\Psi_ {2}} (g a ([ \mathfrak {p} ]), \frac {1}{2} + t ^ {\prime}) d g \\ = c _ {F} \mathrm{N} (\mathfrak {p}) ^ {1 / 2 + t ^ {\prime}} \prod_ {v} I _ {v} (W _ {v}, W _ {\Psi_ {1, v}} (1 / 2 + t, \cdot), \Psi_ {2, v} ^ {\prime}, 1 / 2 + t ^ {\prime}) \\ = c _ {F} \prod_ {v} I _ {v} (W _ {v}, W _ {\Psi_ {2, v}} (1 / 2 + t ^ {\prime}, \cdot) ^ {a ([ \mathfrak {p} ]) _ {v}}, \Psi_ {1, v}, 1 / 2 + t) \end{array}\tag{11.10}
$$

Here$W _ { \Psi _ { 2 , v } } ( 1 / 2 + t ^ { \prime } , \cdot ) ^ { a ( [ \mathfrak { p } ] ) _ { \mathfrak { c } } }$denotes the translate of$W _ { \Psi _ { 2 , v } }$by the vth component of$a ( [ { \mathfrak { p } } ] )$

For v nonarchimedean (notations being similar to that of the previous Lemma) we take$\Psi _ { 1 , v }$and$\Psi _ { 2 , v }$to be the characteristic function of$\mathfrak { o } _ { v } ^ { 2 }$for every finite$v ,$and $W _ { v }$to be the new vector.

For v archimedean we first apply Lem. 11.2 with$s _ { 0 } = 1 / 2 + t _ { 0 }$, and$\pi _ { 2 , v }$the representation of$\mathrm { P G L } _ { 2 } ( F _ { v } )$spanned by$E _ { \Psi _ { 2 } } ( 1 / 2 + t _ { 0 } ^ { \prime } , g )$, i.e. the representation unitarily induced from the character$a ( y ) \mapsto | y | _ { v } ^ { i t _ { 0 } ^ { \prime } }$. Lem. 11.2 provides$W _ { v }$in the Whittaker model of$\pi _ { v } , \ W _ { 2 , v }$in the Whittaker model of$\pi _ { 2 , v } ,$, and a Schwarz function$\Psi _ { 1 , v }$with$| I _ { v } ( W _ { v } , W _ { 2 , v } , \Psi _ { 1 , v } , 1 / 2 + t _ { 0 } ) | \geq 1$. The last comment of Rem. 10.2 shows that there is a standard$\Psi _ { 2 , v }$so that$W _ { \Psi _ { 2 , v } } ( 1 / 2 + t _ { 0 } ^ { \prime } , g _ { v } ) = W _ { 2 , v } ( g _ { v } )$ (notation of Lem. 10.5). Moreover, Lemma 11.2 also shows that$\Psi _ { 1 , v }$and$W _ { 2 , v }$ (so also$\Psi _ { 2 , v } )$may be chosen from a fixed finite set of possibilities (depending, of course, on the original bounded set to which$\pi _ { \infty }$belongs, as well as$t _ { 0 }$and$t _ { 0 } ^ { \prime } )$.

Again we put$\begin{array} { r } { \Psi _ { i } = \prod _ { v } \Psi _ { i , v } } \end{array}$for$i = 1 , 2$and take$\varphi$with$\begin{array} { r l } { \int _ { x \in F \backslash \mathbb { A } _ { F } } \varphi ( n ( x ) g ) = } \end{array}$ $\Pi _ { v } W _ { v } ( g )$. From (11.10) we deduce that, with our choices,$| \Phi ( t _ { 0 } , \dot { t } _ { 0 } ^ { \prime } ) | \gg 1$. The assertion about$\| \varphi \| _ { L ^ { 2 } }$follows as in the proof of the previous Lemma. The second assertion of the Lemma (concerning invariance of$\Psi _ { 1 } , \Psi _ { 2 } )$is immediate.

It remains to prove that Φ is actually holomorphic in$( t , t ^ { \prime } )$and that$| \Phi ( t , t ^ { \prime } ) | \ll$ $( 1 + | t | + | t ^ { \prime } | ) ^ { C } e ^ { C | \Re ( t ) | + C | \Re ( t ^ { \prime } ) | }$. Put$\begin{array} { r } { \Xi _ { v } = \frac { I _ { v } } { L _ { v } \left( \frac { 1 } { 2 } + t + t ^ { \prime } , \pi _ { v } \right) L _ { v } \left( \frac { 1 } { 2 } + t - t ^ { \prime } , \pi _ { v } \right) } } \end{array}$. It is simple to explicitly compute$\Xi _ { v }$for nonarchimedean$v ,$, using Cor. 10.1 and Lem. 11.1. One thereby sees that it will sufice to check, by similar arguments to those used in Lem. 11.2, the following statement for v archimedean:$\Xi _ { v } = c ^ { s } c ^ { \prime s ^ { \prime } } P ( s , s ^ { \prime } )$, where $P$is a polynomial, and moreover$c , c ^ { \prime } , P$vary continuously in$\pi _ { v }$, if$\pi _ { v } \mapsto W _ { v }$is a continuous assignment. We only sketch the proof of this. From (11.7) and the fact that$W _ { v } , \Psi _ { 1 , v } , \Psi _ { 2 , v }$are all$K _ { v } .$-finite, it sufices to prove the corresponding assertions for$\begin{array} { r } { \int _ { \cal F _ { \eta } ^ { \times } } { W _ { v } ( a ( y ) ) W _ { \Psi _ { 1 , v } } ( s , a ( y ) ) | y | ^ { s ^ { \prime } - 1 } d ^ { \times } y } } \end{array}$. For this we use Barnes’ formula as in [17].

11.3. Local Rankin-Selberg convolutions. Let v be a nonarchimedean place of$F$with residue characteristic$q _ { v }$. Let$\pi _ { 1 } , \pi _ { 2 }$be generic irreducible admissible representations of${ \mathrm { G L } } ( 2 , F _ { v } )$with trivial central character. (Since we shall work purely locally over$F _ { v }$throughout the present subsection, we shall use the notation $\pi _ { 1 }$rather than$\mathrm { e . g . } ~ \pi _ { 1 , v } )$

Then$\pi _ { 1 } , \pi _ { 2 }$are self-dual. We assume that$\pi _ { 2 }$is unramified and$\pi _ { 1 }$has conductor $q _ { v } ,$, and denote by$L ( s , \pi _ { j } )$the local L-factors.

Fix once and for all an additive unramified character ψ of$F _ { v }$. Let$v : F _ { v } ^ { \times } \to \mathbb { Z }$be the valuation, put$\mathfrak { o } _ { F _ { v } } = \{ x \in F _ { v } ^ { \times } : v ( x ) \geq 0 \}$, and choose a uniformizer$\varpi \in F _ { v } ^ { \times }$ Let${ \mathfrak { o } } _ { F _ { v } } ^ { \times }$be the multiplicative group of units in$\mathfrak { o } _ { F _ { v } }$. Let$d ^ { \times } x .$dx be Haar measures on$F _ { v } ^ { \times } , F _ { v }$respectively, assigning mass 1 to${ \mathfrak { o } } _ { F _ { \tau } } ^ { \times }$and$\mathfrak { o } _ { F _ { v } }$respectively. For$x \in F _ { v } .$ put$n ( x ) = { \left( \begin{array} { l l } { 1 } & { x } \\ { 0 } & { 1 } \end{array} \right) }$. Also let$w = \left( \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { - 1 } } & { { 0 } } \end{array} \right)$. We choose a Whittaker model for$\pi _ { 1 }$transforming by the character$n ( x ) \mapsto \psi ( x )$, and a Whittaker model for$\pi _ { 2 }$ transforming by the character$n ( x ) \mapsto { \overline { { \psi ( x ) } } }$

Let$\Psi _ { v }$be the characteristic function of$\mathfrak { o } _ { F _ { v } } ^ { 2 }$. Set$W _ { 1 }$to be the new vector in the Kirillov model of$\pi _ { 1 }$, let$W _ { 2 } ^ { * }$be the new vector in the Kirillov model of$\pi _ { 2 }$, and set $W _ { 2 } = \pi _ { 2 } ( \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { \varpi } } \end{array} \right) ) W _ { 2 } ^ { * }$. Then both$W _ { 1 } , W _ { 2 }$are invariant by the subgroup

$$
K _ {0} = \{\left( \begin{array}{c c} a & b \\ c & d \end{array} \right): a, b, d \in \mathfrak {o} _ {F _ {v}}, c \in \varpi \mathfrak {o} _ {F _ {v}} \}.\tag{11.11}
$$

Moreover$W _ { 2 }$is invariant by$n ( \varpi ^ { - 1 } \mathfrak { o } _ { F _ { v } } )$

Lemma 11.6. Notations being as in$( 1 1 . 6 )$, let$L ( s , \pi _ { 1 } \times \pi _ { 2 } )$be the local L-factor. Then:

$$
\frac {I _ {v} (W _ {1 , v} , W _ {2 , v} , \Psi_ {v})}{L (s , \pi_ {1} \times \pi_ {2})} = \pm \frac {q _ {v} ^ {s}}{q _ {v} + 1}
$$

Proof. We shall often use the following shorthand: if W is a function in the Whittaker model of$\pi \in \{ \pi _ { 1 } , \pi _ { 2 } \}$and for$z \in F _ { v } ^ { \times }$, we write$W ( z )$for$W ( { \left( \begin{array} { l l } { z } & { 0 } \\ { 0 } & { 1 } \end{array} \right) } )$ Thus, for instance,$W _ { 2 } ( z ) = W _ { 2 } ^ { * } ( z \varpi ^ { - 1 } )$. The function$z \mapsto W ( z )$belongs to the Kirillov model of π.

Let$\epsilon \in \{ - 1 , 1 \}$be the local root number of$\pi _ { 1 }$(it lies in$\{ - 1 , 1 \}$since$\pi _ { 1 }$is self-dual). Then:

$$
\begin{array}{r l r} & & {\int_ {a \in F _ {v} ^ {\times}} W _ {1} (a) | a | ^ {s - 1 / 2} d ^ {\times} a = L (s, \pi_ {1}),} \\ & & {\int_ {a \in F _ {v} ^ {\times}} W _ {2} (a) | a | ^ {s - 1 / 2} d ^ {\times} a = q _ {v} ^ {- (s - 1 / 2)} L (s, \pi_ {2}),} \end{array}\tag{11.12}
$$

as follows from defining properties of newforms and the fact$W _ { 2 } ( z ) = W _ { 2 } ^ { * } ( z \varpi ^ { - 1 } )$; moreover

$$
\begin{array}{r l} & {\int_ {a \in F _ {v} ^ {\times}} \pi_ {1} (w) W _ {1} (a) | a | ^ {s - 1 / 2} d ^ {\times} a = \epsilon q _ {v} ^ {(s - 1 / 2)} L (s, \pi_ {1}),} \\ & {\int_ {a \in F _ {v} ^ {\times}} \pi_ {2} (w) W _ {2} (a) | a | ^ {s - 1 / 2} d ^ {\times} a = q _ {v} ^ {(s - 1 / 2)} L (s, \pi_ {2}),} \end{array}\tag{11.13}
$$

as follows from local functional equation for the standard L-function on${ \mathrm { G L } } ( 2 )$: see [16, 2.18]. <sup>23</sup>

Note moreover that$W _ { 1 } , \ W _ { 2 } , \ \pi _ { 1 } ( w ) W _ { 1 }$, and$\pi _ { 2 } ( w ) W _ { 2 }$are all invariant by the maximal compact subgroup of the diagonal torus of$\mathrm { G L _ { 2 } }$. Thus (11.12) and (11.13) completely determine their restriction to the diagonal torus; we now explicate this.

Choose$\alpha \in \mathbb { C }$so that$L ( s , \pi _ { 1 } ) = ( 1 - \alpha q _ { v } ^ { - s } ) ^ { - 1 }$. In fact,$\alpha = - \epsilon q _ { v } ^ { - 1 / 2 }$, by$[ 1 6 ,$ Prop. 3.6]. Choose$\gamma _ { 1 } , \gamma _ { 2 }$so that$L ( s , \pi _ { 2 } ) = ( ( 1 - \gamma _ { 1 } q _ { v } ^ { - s } ) ( 1 - \gamma _ { 2 } q _ { v } ^ { - s } ) ) ^ { - 1 }$. Recalling the notational convention established in the paragraph prior to (11.12), we see: (11.14)

$$
W _ {1} (\varpi^ {r}) = \left\{ \begin{array}{l} \alpha^ {r} q _ {v} ^ {- r / 2}, r \geq 0 \\ 0, r <   0 \end{array} \right., \quad \pi_ {1} (w) W _ {1} (\varpi^ {r}) = \left\{ \begin{array}{l} \epsilon \alpha^ {r + 1} q _ {v} ^ {- \frac {r + 1}{2}}, r \geq - 1 \\ 0, r <   - 1 \end{array} \right.
$$

$$
W _ {2} (\varpi^ {r}) = \left\{ \begin{array}{l} 0, r \leq 0 \\ 1, r = 1 \\ (\gamma_ {1} ^ {r - 1} + \gamma_ {1} ^ {r - 2} \gamma_ {2} + \dots + \gamma_ {2} ^ {r - 1}) q _ {v} ^ {- \frac {r - 1}{2}}, r \geq 2 \end{array} \right.
$$

$$
\pi_ {2} (w) W _ {2} (\varpi^ {r}) = \left\{ \begin{array}{l} 0, r <   - 1 \\ 1, r = - 1 \\ (\gamma_ {1} ^ {r + 1} + \gamma_ {1} ^ {r} \gamma_ {2} + \dots + \gamma_ {2} ^ {r + 1}) q _ {v} ^ {- \frac {r + 1}{2}}, r \geq 0 \end{array} \right.
$$

The local integral we wish to evaluate is the right hand side of (11.6). In the case at hand, with$N , G , Z$denoting the$F _ { v } .$-points of the respective groups, we have:

$$
I (s) := \int_ {Z N \backslash G} W _ {1} (g) W _ {2} (g) | \det (g) | ^ {s} \left(\int_ {t} \Psi_ {v} ((0, t) \cdot g) | t | ^ {2 s} d ^ {\times} t\right) d g\tag{11.15}
$$

Using the Iwasawa decomposition, and recalling$\Psi _ { v }$was the characteristic function of$\mathfrak { o } _ { v } ^ { 2 }$one finds:

$$
I (s) = (1 - q _ {v} ^ {- 2 s}) ^ {- 1} \int_ {A \times K _ {v}} \pi_ {1} (k) W _ {1} (a) \pi_ {2} (k) W _ {2} (a) | a | ^ {s - 1} d ^ {\times} a d k,
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>23</sup>That is, <sub>×</sub> W(a)|a|<sup>s−1/2</sup>d<sup>×</sup>a =∫a∈F× W(a)|a|s−1/2d×a =<sub>ǫ(s,π)L(1−s,π˜) F×</sub> W(aw)|a|<sup>1/2−s</sup>ω<sup>−1</sup>(a)d<sup>×</sup>a. In∈(s,π)L(1−s,π) ∫F× W(aw)|a|1/2−sω−1(a)d×a.L(s,π)L(s,π)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">χ a</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L( <sup>1</sup><sub>2</sub> ,π⊗χ)L(2, π∅χ) ∫a∈F× W(a)χ(a)d× a =<sub>×</sub> W(a)χ(a)d<sup>×</sup>a =ǫ( <sup>1</sup> ,π⊗χ)L( <sup>1</sup> ,π˜⊗χ¯)∈(=, π⊗χ)L(=, 元⊗x)<sub>×</sub> W(aw)χ<sup>−1</sup>(a)d<sup>×</sup>a.∫F× W(aw)χ−1(a)d× a.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">F<sup>×</sup>,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">particular, if π is a representation with trivial central character, and χ a character of</span></small>

where the measure dk is the Haar measure of total mass 1, and$d ^ { \times } a$assigns mass 1 to$A \cap K _ { v }$

The function$k \mapsto \pi _ { 1 } ( k ) W _ { 1 } ( a ) \pi _ { 2 } ( k ) W _ { 2 } ( a )$is right invariant by$K _ { 0 }$(see (11.11) for definition) and left invariant by$N \cap K _ { v }$. There are two$( N \cap K _ { v } , K _ { 0 } )$double cosets in$K _ { v } .$and we may therefore express$I ( s )$as a sum:

$$
\begin{array}{l} (1 - q _ {v} ^ {- 2 s}) I (s) = \frac {1}{q _ {v} + 1} \int_ {F _ {v} ^ {\times}} W _ {1} (a) W _ {2} (a) | a | ^ {s - 1} d ^ {\times} a \\ \quad + \frac {q _ {v}}{q _ {v} + 1} \int_ {a \in F _ {v} ^ {\times}} \pi_ {1} (w) W _ {1} (a) \pi_ {2} (w) W _ {2} (a) | a | ^ {s - 1} d ^ {\times} a \end{array}\tag{11.16}
$$

To evaluate$I ( s )$, we use (11.14). Noting that$\begin{array} { r } { L ( s , \pi _ { 1 } \times \pi _ { 2 } ) = \frac { 1 } { ( 1 - \alpha \gamma _ { 1 } q _ { v } ^ { - s } ) ( 1 - \alpha \gamma _ { 2 } q _ { v } ^ { - s } ) } , } \end{array}$ an easy computation shows

$$
I (s) = \frac {L (s , \pi_ {1} \times \pi_ {2})}{(q _ {v} + 1) (1 - q _ {v} ^ {- 2 s})} \left(\alpha q _ {v} ^ {- 1 / 2} q _ {v} ^ {- (s - 1)} + \epsilon q _ {v} q _ {v} ^ {s - 1}\right)
$$

from where we obtain$\begin{array} { r } { I ( s ) = \epsilon \frac { q _ { v } ^ { s } } { q _ { v } + 1 } L ( s , \pi _ { 1 } \times \pi _ { 2 } ) } \end{array}$. Note also that$I ( s )$satisfies the necessary functional equation.

11.4. Hecke-Jacquet-Langlands integral representations for standard$L -$ functions. Our goal here is to prove Prop. 6.1 and 6.2, used in the text. This amounts to explicit computations connected to Hecke-Jacquet-Langlands integral representations. Since, in the main text, we obtain subconvexity for GL(1) twists of GL(2) L-functions, with polynomial dependence in all parameters, we will have to be somewhat more precise than in the case of Rankin-Selberg L-functions.

Let π be a cuspidal representation of$\mathrm { G L _ { 2 } }$over$\mathbb { A } _ { F }$. Let$\chi$be a unitary character of$\mathbb { A } _ { F } ^ { \times } / F ^ { \times }$of finite conductor f. Put${ \cal L } _ { u n r } ( s , \pi \times \chi )$to be the unramified part of the (finite) standard L-function:

$$
L _ {u n r} (s, \pi \times \chi) := \prod_ {v \text { finite }, \chi_ {v} \text { unramified }} L _ {v} (s, \pi_ {v} \times \chi_ {v}).
$$

Define$\mu _ { z }$as in (6.4), i.e. the measure on$\mathbf { X } _ { \mathrm { G L } ( 2 ) }$defined as

$$
\mu_ {z} (f) = \int_ {| y | = z} f (a (y) n ([ f ])) \chi (y) d ^ {\times} y.
$$

We refer to Sec. 2.3 and Sec. 2.5 for notation, as well as the start of Section 6 for a discussion of the meaning of$\mu _ { z }$in classical terms.

Lemma 11.7. Let v be a nonarchimedean place of F with residue characteristic$q _ { v } ,$ and$\pi _ { v }$an irreducible generic representation of$\mathrm { G L _ { 2 } } ( F _ { v } )$. Let$\psi _ { v }$be an unramified additive character of$F _ { v }$. Let$\chi _ { v } : F _ { v } ^ { \times } \to \mathbb { C }$a multiplicative character of conductor $r , W _ { v }$be the new vector in the$\psi _ { v } -$Whittaker model of$\pi _ { v }$. Then

$$
\int_ {y \in F _ {v} ^ {\times}} W _ {v} (a (y) n (\varpi_ {v} ^ {- r})) \chi_ {v} (y) | y | ^ {s - 1 / 2} d ^ {\times} y = \left\{ \begin{array}{l} L _ {v} (s, \pi_ {v} \times \chi_ {v}),   r = 0. \\ \theta ,   r \geq 1, \end{array} \right.
$$

where$\theta$is a scalar of absolute value$q _ { v } ^ { - r / 2 } ( 1 - q _ { v } ^ { - 1 } ) ^ { - 1 }$

Proof. If$r ~ = ~ 0$, then$\chi _ { v }$is unramified, the result follows immediately from the definition of the new vector. Otherwise,$\chi _ { v }$is ramified, and we rewrite the integral under consideration as

$$
\int_ {y \in F _ {v} ^ {\times}} W _ {v} (a (y)) \psi_ {v} (\varpi_ {v} ^ {- r} y) \chi_ {v} (y) | y | ^ {s - 1 / 2} d ^ {\times} y.\tag{11.17}
$$

Now$W _ { v } ( a ( y ) )$vanishes when$v ( y ) ~ < ~ 0$and it is${ \mathfrak { o } } _ { F _ { v } } ^ { \times } { \mathrm { - i n v a r i a n t } }$. The integral $\begin{array} { r } { \int _ { v ( y ) = k } \chi _ { v } ( y ) \psi _ { v } ( \varpi _ { v } ^ { - r } y ) d ^ { \times } y } \end{array}$is nonvanishing only when$k = 0$. In that case, it is a Gauss sum with absolute value$\frac { q _ { v } ^ { - r / 2 } } { ( 1 - q _ { v } ^ { - 1 } ) }$, where the factor$( 1 - q _ { v } ^ { - 1 } ) ^ { - 1 }$arises from the measure normalization (cf. Sec. 2.6) namely$\begin{array} { r } { \int _ { v ( y ) = 0 } d ^ { \times } y = 1 } \end{array}$. The result follows.

## Lemma 11.8. Let$d , \beta \geq 0$. Then there exists$\varphi \in \pi$such that, with

$$
\Phi (s) = \mathrm{N} (\mathfrak {f}) ^ {1 / 2} \frac {\int_ {z} \mu_ {z} (\varphi) | z | ^ {s - 1 / 2} d ^ {\times} z}{L _ {u n r} (s , \pi \times \chi)}\tag{11.18}
$$

then$\Phi ( s )$is holomorphic and satisfies:

(1)$| \Phi ( s ) | \ll _ { \mathfrak { R } ( s ) , \epsilon } \mathrm { N } ( \mathfrak { f } ) ^ { \epsilon }$and$| \Phi (  { { \frac { 1 } { 2 } } } ) | \gg _ { \epsilon } \mathrm { N } ( \mathfrak { f } ) ^ { - \epsilon }$

(2)$\varphi$is new at every finite place$( i . e . , f o r$each finite prime q it is invariant by $K _ { 0 } [ \mathfrak { q } ^ { s _ { \mathfrak { q } } } ]$, where$s _ { \mathfrak { q } }$is the local conductor of the local constituent$\pi _ { \mathfrak { q } } )$

(3) The Sobolev norms of ϕ satisfy the bounds (conductor notation as in$S e c$ $\it 2 . 1 2 . 2 )$

$$
S _ {2, d, \beta} (\varphi) \ll_ {\epsilon} \operatorname{Cond} _ {\infty} (\pi) ^ {2 d + \epsilon} \operatorname{Cond} _ {f} (\pi) ^ {\beta + \epsilon} \operatorname{Cond} _ {\infty} (\chi) ^ {1 / 2 + 2 d}\tag{11.19}
$$

Proof. For each infinite place w of$F ,$, denote by$\mathrm { C o n d } _ { w } ( \chi )$the contribution from w to the Iwaniec-Sarnak analytic conductor of$\chi$(see Sec. 2.12.2.)

The map$\begin{array} { r } { \varphi \mapsto W _ { \varphi } = \int _ { F \backslash \mathbb { A } _ { F } } e _ { F } ( x ) \varphi ( n ( x ) g ) } \end{array}$is an isomorphism between the space of$\pi$and the Whittaker model of$\pi .$. For each finite$v ,$take$W _ { v }$to be a new vector in the Whittaker model of$\pi _ { v } . \ \mathrm { A }$point of caution is that$e _ { F }$may not be unramified on$F _ { v } ;$to be absolutely concrete, we set$W _ { v } ( g ) = W _ { v , \mathrm { n e w } } ( a ( \varpi ^ { \dot { d } _ { v } } ) g )$, where$W _ { v , \mathrm { n e w } }$ is the new vector in the Whittaker model of$\pi _ { v }$taken w.r.t an unramified additive character of$F _ { v } { } _ { : }$, and$d _ { v } = v ( \mathfrak { d } )$is the local valuation of the diferent.

Let us now choose$W _ { v }$at the infinite places. Let$g _ { 1 }$be a smooth positive function of compact support on$F _ { v }$. Let$\deg ( v ) = 2 { \mathrm { ~ i f ~ } } v$is complex and$\deg ( v ) = 1 { \mathrm { ~ i f ~ } } v$is real. For$\infty | v$, define

$$
W _ {v} (y) = \operatorname{Cond} _ {v} (\chi) g _ {1} \left(\operatorname{Cond} _ {v} (\chi) ^ {1 / \deg (v)} (y - 1)\right).
$$

This is possible by the theory of the Kirillov model; thus$W _ { v }$is a smooth (but not$K _ { v } \mathrm { - f i n i t e } )$vector. In words, if v is real, the function$W _ { v }$is supported in a neighbourhood of the identity of size$\mathrm { C o n d } _ { v } ( \chi ) ^ { - 1 }$and takes values of size$| \mathrm { C o n d } _ { v } ( \chi ) |$ there; if v is complex, a similar statement holds but now$W _ { v }$is supported in a disc around the identity with area$\mathrm { C o n d } _ { v } ( \chi ) ^ { - 1 }$

Then there exists$\varphi \in \pi$with$\begin{array} { r } { W _ { \varphi } = \prod _ { v } W _ { v } } \end{array}$. By unfolding, it follows that for $\Re ( s ) \gg 1$

$$
\int_ {z} \mu_ {z} (\varphi) | z | ^ {s - 1 / 2} d ^ {\times} z = c _ {F} \prod_ {v} \int_ {y \in F _ {v} ^ {\times}} W _ {v} (a (y) n ([ \mathfrak {f} ])) | y | ^ {s - 1 / 2} \chi_ {v} (y) d ^ {\times} y\tag{11.20}
$$

Here$c _ { F }$is a constant depending only on$F ,$arising from change of measure; it is entirely unimportant as we will be only interested in bounds.<sup>24</sup>

By Lem. 11.7, with$\Phi ( s )$as in the statement of the Lemma,

$$
\Phi (s) = c _ {F} \theta^ {\prime} \cdot \mathrm{N} (\mathfrak {d}) ^ {s - 1 / 2} \prod_ {\mathrm{infinite} v} \int_ {F _ {v} ^ {\times}} W _ {v} (a (y)) | y | ^ {s - 1 / 2} \chi_ {v} (y)\tag{11.21}
$$

where$\begin{array} { r } { | \theta ^ { \prime } | = \prod _ { { \mathfrak { q } } | \mathfrak { f } } ( 1 - \mathrm { N } ( { \mathfrak { q } } ) ^ { - 1 } ) ^ { - 1 } } \end{array}$. For this choice of$\varphi ,$the second assertion if the Lemma is clear, and, if we choose the support of$g _ { 1 }$to be small enough, the first assertion also follows easily.25

(11.19) follows from Lem. 8.4, together with Lem. 11.3 and the upper bound for L-functions near 1 due to Iwaniec. See [15, Chapter 8] for this bound.

The previous Lemma shows that${ \cal L } ( 1 / 2 , \pi \times \chi )$may be “well-approximated” by an appropriate period integral. Unfortunately, this period integral is against a measure of infinite mass, since$\mathbb { A } _ { F } ^ { \times } / F ^ { \times }$is of infinite volume. It is, therefore, convenient to know that the$\mu _ { z } \mathrm { - i n t e g r a l }$of (11.18) can be truncated to a compact range without afecting the answer too much. This is, roughly speaking, the geometric equivalent of the approximate functional equation in the classical theory, and is provided by the next Lemma. It says, roughly speaking, that the integral of (11.18) can be truncated to the range where$z$is around$\mathrm { { N } } ( \mathfrak { f } ) ^ { - 1 }$

Lemma 11.9. Let notation be as in Lem. 11.8. Let$g _ { + } , g _ { - }$be positive smooth functions on$\mathbb { R } _ { \geq 0 }$such that$g _ { + } + g _ { - } = 1 , g _ { + } ( t ) = 1$for$t \geq 2$and$g _ { - } ( t ) = 1$for all $t \leq 1 / 2$. Then

$$
I _ {+} := \int_ {z} \mu_ {z} (\varphi) g _ {+} (z / T) d ^ {\times} z \ll_ {g _ {+}, \epsilon} (\mathrm{N} (\mathfrak {f}) T) ^ {- 1 / 2} (T \mathrm{Cond} (\pi) \mathrm{Cond} (\chi)) ^ {\epsilon}
$$

$$
I _ {-} := \int_ {z} \mu_ {z} (\varphi) g _ {-} (z / T) d ^ {\times} z \ll_ {g _ {-}, \epsilon} (\mathrm{N} (\mathfrak {f}) T) ^ {1 / 2} (T \mathrm{Cond} (\chi)) ^ {\epsilon} (\mathrm{Cond} _ {\infty} (\chi) \mathrm{Cond} (\pi)) ^ {1 + \epsilon}
$$

Proof. Recall the definition of$\mu _ { z }$from (6.4). Put$\begin{array} { r } { \widehat { g _ { \pm } } ( s ) = \int g _ { \pm } ( x ) x ^ { s - 1 } d x . } \end{array}$, the Mellin transform of$g _ { \pm } ;$then$g _ { \pm }$is holomorphic in$\pm \Re ( s ) < 0$and for any$M \geq$ $0 , \pm \sigma < 0$the integral$\begin{array} { r } { \int _ { \Re ( s ) = \sigma } | \widehat { g _ { \pm } } ( s ) | ( 1 + | s | ) ^ { M } d s } \end{array}$is convergent. Then, for any $\pm \sigma > 0$c, we have, by the Plancherel formula on$\mathbb { R } ^ { \times }$, that:

$$
\int_ {z} \mu_ {z} (\varphi) g _ {\pm} (z / T) d ^ {\times} z = \frac {1}{2 \pi i} \int_ {\Re (s) = - \sigma} \left(\int \mu_ {z} (\varphi) | z | ^ {- s} d ^ {\times} z\right) T ^ {s} \widehat {g _ {\pm}} (s) d s.
$$

So for any$M > 0$

$$
\left| I _ {\pm} \right| \ll_ {\sigma , g _ {\pm}, M} T ^ {- \sigma} \mathrm{N} (\mathfrak {f}) ^ {- 1 / 2} \sup _ {\Re (s) = 1 / 2 + \sigma} \frac {\left| L _ {u n r} (s) \Phi (s) \right|}{(1 + | s |) ^ {M}}
$$

where$\Phi$is as in the previous Lemma.Take$\sigma = 1 / 2 + \varepsilon { \mathrm { ~ i n ~ t h e } } + { \mathrm { c a s e , } } - 1 / 2 - \varepsilon$in ${ \mathrm { t h e ~ - ~ } } \mathrm { c a s e } .$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">µz</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">ΠvFX</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>24</sup>The measure µ<sub>z</sub> is normalized as a probability measure, whereas to unfold from A<sup>×</sup><sub>F</sub> toAF <sub>v</sub> F<sup>×</sup><sub>v</sub> we use the measures previously set up there (see Section 2.6).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">|Φ(1/2)|</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Xv</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">W<sub>v</sub>,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">e.g.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">W<sub>v</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>25</sup>For the assertion concerning the lower bound for |Φ(1/2)|, the point, in words, is that our choices are so that χ<sub>v</sub> does not oscillate over the support of cf. Remark 2.2. Note how convenient it is, here and elsewhere, to use smooth vectors rather than finite vectors; oneK<sub>∞</sub>- could not achieve of compact support with finite vectors.K<sub>∞</sub>-</span></small>

Using Iwaniec’s bounds on L-functions near 1 [15, Chapter 8] and the functional equation, we see that for suficiently large$M \colon$

$$
\begin{array}{l} (1 1. 2 2) \sup _ {\Re (s) = 1 + \varepsilon} | L _ {u n r} (s, \pi \times \chi) | \ll \operatorname{Cond} (\pi \otimes \chi) ^ {\varepsilon} \\ \frac {\sup _ {\Re (s) = - \varepsilon} | L _ {u n r} (s , \pi \times \chi) |}{(1 + | s |) ^ {M}} \ll_ {M} \operatorname{Cond} (\pi \otimes \chi) ^ {1 / 2 + \varepsilon} \prod_ {\chi_ {v} \text { ramified   finite }} \sup _ {\Re (s) = - \varepsilon} | L _ {v} (s, \pi_ {v} \times \chi_ {v}) | ^ {- 1} \end{array}
$$

For each v where$\chi _ { v }$is ramified and$L _ { v } ( s , \pi _ { v } \times \chi _ { v } )$is not identically 1, the representation$\pi _ { v }$must also be ramified$( { \mathrm { i . e . } }$, not spherical). So one can bound the product on the second line on (11.22), using trivial bounds towards the Ramanujan conjecture, by$\operatorname { C o n d } ( \pi ) ^ { 1 / 2 + 2 \varepsilon }$. The fact that$\mathrm { C o n d } ( \chi ) = \mathrm { C o n d } _ { \infty } ( \chi ) \mathrm { N } ( \mathfrak { f } )$, the bound [6]$\operatorname { C o n d } ( \pi \otimes \chi ) \ll \operatorname { C o n d } ( \pi ) \operatorname { C o n d } ( \chi ) ^ { 2 }$, and the (easily verified) analogue of this bound of [6] at archimedean places, allows one to conclude.

We now address the analogue of the previous Lemmas when π is noncuspidal. <sup>26</sup>

Lemma 11.10. Let$s _ { 0 } , s _ { 0 } ^ { \prime } \in \mathbb { C }$. There is an absolute$C > 0 \ ( i . e .$, depending only on$F )$and a Schwarz function Ψ (depending on$\chi )$so that if we put

$$
\Phi (s, s ^ {\prime}) := N (\mathfrak {f}) ^ {1 / 2} \frac {\int_ {y \in \mathbb {A} _ {F} ^ {\times} / F ^ {\times}} \bar {E} _ {\Psi} (s , a (y) n ([ \mathfrak {f} ])) \chi (y) | y | ^ {s ^ {\prime}} d ^ {\times} y}{L (\chi , s + s ^ {\prime}) L (\chi , 1 - s + s ^ {\prime})}
$$

where$\bar { E }$is defined as in$( \mathit { 1 0 . 9 } )$, then the integral defining Φ is absolutely convergent in a right half-plane$\Re ( s ) \gg 1$. Moreover, Φ extends from$\Re ( s ) , \Re ( s ^ { \prime } ) \gg 1$to a holomorphic function on$\mathbb { C } ^ { 2 }$, satisfying

(1)$| \Phi ( 1 / 2 , 0 ) | \gg 1$and$| \Phi ( s , s ^ { \prime } ) | \ll C ^ { 1 + | \Re ( s ) | + | \Re ( s ^ { \prime } ) | } ( 1 + | s | + | s ^ { \prime } | ) ^ { C } .$

Moreover, given$N > 0$we have that

$$
| \Phi (s, s ^ {\prime}) | (1 + | s | + | s ^ {\prime} |) ^ {N} \ll_ {\Re (s), \Re (s ^ {\prime}), N} \mathrm{Cond} _ {\infty} (\chi) ^ {N ^ {\prime}}\tag{11.23}
$$

where$N ^ { \prime }$and the implicit constant may be taken to depend continuously on $N , \Re ( s ) , \Re ( s ^ { \prime } )$

(2) Ψ, and so also$E _ { \Psi } ( s , g )$is invariant by$K _ { \mathrm { m a x } } ,$ (3) Let$h \in { \mathcal { H } } ( \kappa )$be as in (10.18), and put$\begin{array} { r } { E _ { h } : = \int _ { \mathfrak { R } ( s ) \gg 1 } h ( s ) E _ { \Psi } ( s , g ) d g } \end{array}$. For each$d , \beta$there is N such that$S _ { \infty , d , \beta } ( E _ { h } ) \ll _ { \kappa } \| h \| _ { 0 } \mathrm { C o n d } _ { \infty } ( \chi ) ^ { N }$

Proof. We shall not explicitly address details of convergence. The manipulations that follow may be justified by similar reasoning to that of Lem. 10.6.

We now define a Schwarz function$\Psi _ { v }$on$F _ { v } ^ { \bar { 2 } }$for each place v. For each finite place$v ,$let$\Psi _ { v }$be the characteristic function of$\mathfrak { o } _ { v } ^ { 2 }$

For infinite v, we will first define a Schwarz function$\rho _ { v }$on$F _ { v }$, and then take $\Psi _ { v } ( x , y ) = \rho _ { v } ( x ) \widehat { \rho _ { v } } ( y ) ;$; here$\widehat { \rho _ { v } }$is the inverse Fourier transform of$\rho _ { v }$, satisfying $\begin{array} { r } { \int _ { F _ { v } } \widehat { \rho _ { v } } ( y ) e _ { F _ { v } } ( x y ) d y = \rho _ { v } ( x ) } \end{array}$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">X</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">iy)y<sup>s′</sup>d<sup>×</sup>y</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">E<sup>∗</sup>(s, z)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">q,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Λ(χ, s)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>E¯∗(s,</sup> <sup>z)</sup> <sup>:=</sup> <sup>E∗(s,</sup> <sup>z)</sup> <sup>−</sup> <sup>ξ(2s)ys</sup> <sup>−</sup> <sup>ξ(2(1</sup> <sup>−</sup> <sup>s))y1−s,</sup> <sup>then</sup> <sup>1</sup>q R <sup>∞</sup>0 1≤x≤q−1 <sup>E¯∗(s,</sup> <sup>x</sup>q <sup>+</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">q<sup>−1/2</sup>Λ(χ, s + s<sup>′</sup>)Λ(χ, 1 − s + s<sup>′</sup>))</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>26</sup>The content of the following Lemma, in classical language, is related to the following observation. Let χ be an even Dirichlet character mod q, and let to be the Eisenstein series coincides, up to some harmless factor, with , where is the usual Dirichlet L-function completed to include the Γ-factor at ∞. This particular expression is actually not quite suitable for our needs, because of the rapid decay of the Γ-factor swamps information about the finite L-function, and in fact the Lemma uses (the equivalent of) a diferent test vector belonging to the automorphic representation underlyingE<sup>∗</sup>(z, s).</span></small>

Let$g _ { 1 }$be a smooth positive function of compact support on$F _ { v }$. Let$\deg ( v ) = 2$ if v is complex and$\deg ( v ) = 1$if v is real. For$\infty | v$, define

$$
\rho_ {v} (y) = \operatorname{Cond} _ {v} (\chi) g _ {1} \left(\operatorname{Cond} _ {v} (\chi) ^ {1 / \deg (v)} (y - 1)\right).
$$

In words: in the real (resp. complex) case,$\rho _ { v }$is localized in a real (resp. complex) interval (resp. disc) around 1, of length (resp. area)$\mathrm { C o n d } _ { v } ( \chi ) ^ { - 1 }$. Now put $\Psi _ { v } ( x , y ) = \rho _ { v } ( x ) \widehat { \rho _ { v } } ( y )$. The function$\Psi _ { v }$is not compactly supported; however, it is bof rapid decay. Indeed for each Schwarz norm${ \mathbf { } } S .$, there is$M > 0$such that

$$
\mathcal {S} (\Psi_ {v}) \ll \mathrm{Cond} _ {v} (\chi) ^ {M}\tag{11.24}
$$

Define a Schwarz function on$\mathbb { A } _ { F } ^ { 2 }$via$\begin{array} { r } { \Psi ( x , y ) = \prod _ { v } \Psi _ { v } ( x , y ) } \end{array}$. Define$W _ { \Psi } ( s , g )$as in Lem. 10.5 to be the Fourier coeficient of$E _ { \Psi } ( s , g )$. The choice of$\Psi$and Lem. 10.5 shows that$\begin{array} { r } { W _ { \Psi } ( s , g ) = \prod _ { v } W _ { v } ( g ) } \end{array}$, where, for each finite$v , W _ { v }$is given by Cor. 10.1, and satisfies

$$
\int_ {F _ {v} ^ {\times}} W _ {v} (a (y)) | y | ^ {s ^ {\prime}} d ^ {\times} y = q _ {v} ^ {d _ {v} (1 + s ^ {\prime} - s)} L _ {v} (| \cdot | ^ {s}, s ^ {\prime}) L _ {v} (| \cdot | ^ {1 - s}, s ^ {\prime}),\tag{11.25}
$$

For infinite$v , W _ { v }$satisfies (Lem. 10.5)

$$
\int_ {F _ {v} ^ {\times}} W _ {v} (a (y)) \omega (y) | y | ^ {s ^ {\prime}} d ^ {\times} y = \int_ {F _ {v} ^ {\times}} \rho_ {v} (x) \omega (x) | x | ^ {s + s ^ {\prime}} d ^ {\times} x \int_ {F _ {v} ^ {\times}} \rho_ {v} (x) \omega (x) | x | ^ {1 - s + s ^ {\prime}} d ^ {\times} x\tag{11.26}
$$

By Fourier analysis and Lem. 10.3,$\begin{array} { r } { \bar { E } _ { \Psi } ( s , g ) = \sum _ { \alpha \in F ^ { \times } } W _ { \Psi } ( a ( \alpha ) g ) } \end{array}$. Thus, for $\Re ( s ) \gg 1$9

$$
\begin{array}{c} \int_ {y \in \mathbb {A} _ {F} ^ {\times} / F ^ {\times}} \bar {E} _ {\Psi} (s, a (y) n ([ \mathfrak {f} ])) \chi (y) | y | ^ {s ^ {\prime}} d ^ {\times} y = \int_ {y \in \mathbb {A} _ {F} ^ {\times}} W _ {\Psi} (s, a (y) n ([ \mathfrak {f} ])) \chi (y) | y | ^ {s ^ {\prime}} d ^ {\times} y \\ = \prod_ {v} \int_ {y \in F _ {v} ^ {\times}} W _ {v} (a (y) n ([ \mathfrak {f} ])) \chi (y) | y | ^ {s ^ {\prime}} d ^ {\times} y \end{array}\tag{11.27}
$$

For$s \gg 1$, we use (10.17), (11.26) and Lemma 11.7 to evaluate the local factors, obtaining:

$$
\begin{array}{l} \Phi (s, s ^ {\prime}) = \theta^ {\prime} \cdot \mathrm{N} (\mathfrak {d}) ^ {1 + s ^ {\prime} - s} \prod_ {v \text {infinite}} \int_ {y \in F _ {v} ^ {\times}} W _ {v} (a (y)) \chi (y) | y | ^ {s ^ {\prime}} d ^ {\times} y \\ = \theta^ {\prime} \cdot \mathrm{N} (\mathfrak {d}) ^ {1 + s ^ {\prime} - s} \int_ {F _ {v} ^ {\times}} \rho_ {v} (x) \chi (x) | x | ^ {s + s ^ {\prime}} d ^ {\times} x \int_ {F _ {v} ^ {\times}} \rho_ {v} (x) \chi (x) | x | ^ {1 - s + s ^ {\prime}} d ^ {\times} x \end{array}\tag{11.28}
$$

where$\begin{array} { r } { | \theta ^ { \prime } | \ = \ \prod _ { { \mathfrak { q } } | { \mathfrak { f } } } ( 1 - \mathrm { N } ( { \mathfrak { q } } ) ^ { - 1 } ) ^ { - 1 } } \end{array}$. Now, by choice of$\varphi _ { v } ,$the integral$I _ { v } ( s ) : =$ $\begin{array} { r } { \int _ { y \in F _ { v } ^ { \times } } \rho _ { v } ( y ) \chi ( y ) | y | ^ { s } d ^ { \times } y } \end{array}$satisfies$| I _ { v } ( 1 / 2 ) | \gg 1$and$| I _ { v } ( s ) | \ll ( 1 + | s | ) ^ { C } C ^ { 1 + | \Re ( s ) } |$ at least when we choose the support of$g _ { 1 }$to be suficiently small. It also satisfies $| I _ { v } ( s ) | ( 1 + | s | ) ^ { N } \ll _ { N , \Re ( s ) } \mathrm { C o n d } _ { \infty } ( \chi ) ^ { N ^ { \prime } }$, where$N ^ { \prime }$and the implicit constant may be taken to depend continuously on$N , \Re ( s )$

The corresponding facts (i.e. the first assertion of the Lemma) about Φ follow immediately. The second assertion of the Lemma is immediate from our choice of Ψ.

As for the third and final assertion, it follows from Rem. 10.3 and (11.24).

Lemma 11.11. Let notations be as in the previous Lemma. Assume χ is ramified at at least one finite place. Let$g _ { + } , g _ { - }$be positive smooth functions on$\mathbb { R } _ { \geq 0 }$such that$g _ { + } + g _ { - } = 1 , g _ { + } ( t ) = 1 f o r t \geq 2$and$g _ { - } ( t ) = 1$for all$t \leq 1 / 2$

$$
\mu_ {z} (E _ {h}) \ll_ {K, \Psi , h} \min (z ^ {K}, z ^ {- K})\tag{11.29}
$$

for any$K \geq 1$

Moreover, there is an absolute$N > 0$such that

$$
I _ {+} := \int_ {z} \mu_ {z} (E _ {h}) g _ {+} (z / T) d ^ {\times} z \ll (\mathrm{N} (\mathfrak {f}) T) ^ {- 1 / 2} (T \mathrm{Cond} (\chi)) ^ {\epsilon} \| h \| _ {N}
$$

$$
I _ {-} := \int_ {z} \mu_ {z} (E _ {h}) g _ {-} (z / T) d ^ {\times} z \ll (\mathrm{N} (\mathfrak {f}) T) ^ {1 / 2} (T \mathrm{Cond} (\chi)) ^ {\epsilon} \mathrm{Cond} _ {\infty} (\chi) ^ {1 + \epsilon} \| h \| _ {N}
$$

(Here the norms$\| \cdot \| _ { N }$are as in$( 1 0 . 1 8 ) . )$

Proof. Again, we shall leave verification of convergence to the reader. Recall that, with the relevant measure on$\mathbb { A } _ { F } ^ { \times } / F ^ { \times }$having mass 1:

$$
\begin{array}{r l} & {\mu_ {z} (E _ {h}) = \int_ {y \in \mathbb {A} _ {F} ^ {\times} / F ^ {\times}, | y | = z} E _ {h} (a (y) n [ \mathfrak {f} ]) \chi (y) d ^ {\times} y} \\ & {\qquad = \int_ {y \in \mathbb {A} _ {F} ^ {\times} / F ^ {\times}, | y | = z} \int_ {\Re (s) \gg 1} h (s) E _ {\Psi} (s, a (y) n ([ \mathfrak {f} ])) \chi (y) d ^ {\times} y} \\ & {\qquad = \int_ {y \in \mathbb {A} _ {F} ^ {\times} / F ^ {\times}, | y | = z} \int_ {\Re (s) \gg 1} h (s) \bar {E} _ {\Psi} (s, a (y) n ([ \mathfrak {f} ])) \chi (y) d ^ {\times} y} \end{array}\tag{11.30}
$$

Here, the last equality is justified by the fact that$( E _ { \Psi } - \bar { E } _ { \Psi } ) ( s , a ( y ) n ( [ \mathfrak { f } ] ) )$is invariant under$y \mapsto y y ^ { \prime }$, for$y ^ { \prime } \in \prod _ { v } \pmb { \sigma } _ { v } ^ { \times }$. On the other hand,$\chi$is nontrivial on$\Pi _ { v } \mathfrak { o } _ { v } ^ { \times }$ by assumption.

Combining (11.30) with Lem. 11.10, we have

$$
\int_ {z} \mu_ {z} (E _ {h}) | z | ^ {s ^ {\prime}} d ^ {\times} z = c _ {F} \mathrm{N} (\mathfrak {f}) ^ {- 1 / 2} \int_ {\Re (s) \gg 1} h (s) L (\chi , 1 - s + s ^ {\prime}) L (\chi , s + s ^ {\prime}) \Phi (s, s ^ {\prime}) d s.\tag{11.31}
$$

Here$c _ { F }$is an (unimportant) constant arising from measure normalization, as in (11.20).

The assertion (11.29) follows immediately from this, inverse Mellin transform, and analytic properties of the right-hand side.

Now proceed as in Lem. 11.9; it follows that (for any M)

$$
| I _ {\pm} | \ll T ^ {\mp (1 / 2 + \varepsilon)} \mathrm{N} (\mathfrak {f}) ^ {- 1 / 2} \sup _ {\Re (s ^ {\prime}) = \pm (1 / 2 + \varepsilon)} (1 + | s ^ {\prime} |) ^ {- M} \int h (s) L (\chi , 1 - s + s ^ {\prime}) L (\chi , s + s ^ {\prime}) \Phi (s, s ^ {\prime}) d s.
$$

We deal with the case of$I _ { - }$. In that case, we take the inner integral to be over $\Re ( s ) = 1 / 2 { . }$, and put$s ^ { \prime } = - 1 / 2 - \varepsilon - i t ^ { \prime }$, and it will sufice to bound$\int h ( 1 / 2 +$ $i t ) L ( \chi , - \varepsilon - i t - i t ^ { \prime } ) L ( \chi , - \varepsilon + i t - i t ^ { \prime } ) ( 1 + | t | + | t ^ { \prime } | ) ^ { C }$. This is bounded, up to an implicit constant depending on ε, by Cond$( \dot { \chi } ) ^ { 1 + \dot { 2 } \varepsilon } \| h \| _ { M ^ { \prime } } ( 1 + | t ^ { \prime } | ) ^ { C ^ { \prime } }$for suficiently big$M ^ { \prime } , C ^ { \prime }$, whence the result.

## References

[1] Joseph Bernstein and Andr´e Reznikov. Sobolev norms of automorphic functionals and Fourier coeficients of cusp forms. C. R. Acad. Sci. Paris S´er. I Math., 327(2):111–116, 1998.

[2] Joseph Bernstein and Andr´e Reznikov. Sobolev norms of automorphic functionals. International Math Research Notices, 40 (2155–2174), 2002.

[3] Joseph Bernstein and Andr´e Reznikov. Periods, subconvexity of L-functions and representation theory. arxiv: math.RT/0504411

[4] Jean Bourgain. Pointwise ergodic theorems for arithmetic sets. Inst. Hautes Etudes Sci.<sup>´</sup> Publ. Math., (69):5–45, 1989. With an appendix by the author, Harry Furstenberg, Yitzhak Katznelson and Donald S. Ornstein.

[5] Jean Bourgain and Elon Lindenstrauss. Entropy of quantum limits. Comm. Math. Phys., 233(1):153–171, 2003.

[6] C. Bushnell and G. Henniart. An upper bound on conductors for pairs. J. Number Theory 65: 183–196, 1997.

[7] L. Clozel and E. Ullmo. Equidistribution de mesures alg´ebriques. preprint.

[8] M. Cowling, U. Haagerup, and R. Howe. Almost L<sup>2</sup> matrix coeficients. J. Reine Angew. Math., 387:97–110, 1988.

[9] P. Cohen Hyperbolic distribution problems on Siegel 3-folds and Hilbert modular varieties. Duke Math. Journal, to appear.

[10] W. Duke, J. Friedlander and H. Iwaniec. Class group L-functions. Duke Math. Journal 79: 1–56, 1995.

[11] L. Flaminio and G. Forni. Invariant distributions and time averages for horocycle flows. Duke Math. Journal, 119: 465–526, 2003.

[12] J. Friedlander and H. Iwaniec. A mean-value theorem for character sums. Michigan Math. J., 39(1):153–159, 1992.

[13] Anton Good. Cusp forms and eigenfunctions of the Laplacian. Math. Ann, 255: 523–438, 1981.

[14] D. Hejhal. On the value distribution properties of automorphic functions along closed horocycles. XVI Rolf Nevanlinna Colloquium, I. Laine and O. Martio (ed), deGruyter 1996, 39–52.

[15] H. Iwaniec. Introduction to the spectral theory of automorphic forms. Revista Matematica Iberoamericana, Madrid, 1995.

[16] H. Jacquet and R. P. Langlands. Automorphic forms on GL(2). Springer-Verlag, Berlin, 1970. Lecture Notes in Mathematics, Vol. 114.

[17] Herv´e Jacquet. Automorphic forms on GL(2). Part II. Springer-Verlag, Berlin, 1972. Lecture Notes in Mathematics, Vol. 278.

[18] D. Y. Kleinbock and G. A. Margulis. Logarithm laws for flows on homogeneous spaces. Invent. Math., 138(3):451–494, 1999.

[19] Serge Lang Algebraic number fields.

[20] Yu. Linnik. Ergodic properties of algebraic fields.

[21] Gregory Margulis. On some aspects of the theory of Anosov systems. Springer monographs in mathematics, 2004.

[22] Philippe Michel. The subconvexity problem for Rankin-Selberg L functions and equidistribution of Heegner points. Annals of Math. 160:185–236, 2004.

[23] Philippe Michel and Akshay Venkatesh. Periods, equidistribution and subconvexity. In preparation.

[24] Philippe Michel and Akshay Venkatesh. Equidistribution, L-functions and ergodic theory: on some problems of Yu. V. Linnik. Proceedings of the Madrid ICM, to appear.

[25] Marina Ratner. Rigidity of time changes for horocycle flows. Acta. Math. 156, 1–32, 1986.

[26] Marina Ratner. Raghunathan’s conjectures for SL(2, R). Israel. J. Math 80, 1–31, 1992.

[27] Marina Ratner. The rate of mixing for the geodesic and horocycle flows. Ergodic Theory and Dynamical Systems 7, 267–288, 1987.

[28] Andre Reznikov. Rankin-Selberg without unfolding. Preprint available at www.math.biu.ac.il/ \~reznikov/publications.html.

[29] Peter Sarnak. Fourth moments of Gr¨ossencharakteren zeta functions. Comm. Pure Appl. Math., 38(2):167–178, 1985.

[30] Peter Sarnak. Integrals of products of eigenfunctions. Internat. Math. Res. Notices, (6):251 f., approx. 10 pp. (electronic), 1994.

[31] Peter Sarnak. Asymptotic behavior of periodic orbits of the horocycle flow and Eisenstein series. Comm. Pure Appl. Math, 34: 719–739, 1981.

[32] Nimish A. Shah. Limit distributions of polynomial trajectories on homogeneous spaces. Duke Math. J., 75(3):711–732, 1994.

[33] Goro Shimura. Introduction to the arithmetic theory of automorphic forms. 1971.

[34] Kannan Soundararajan. Nonvanishing of quadratic Dirichlet L-functions at$\begin{array} { r } { s = \frac { 1 } { 2 } . } \end{array}$. Ann. of Math. 152 (2), 447–488, 2000.

[35] Andreas Str¨ombergsson. On the uniform equidistribution of long closed horocycles. Duke. Math. Journal 123: 507–547, 2004.

[36] Terence Tao. The ergodic and combinatorial approaches to Szemer´edi’s theorem. math.CO/0604456.

[37] Jean-Loup Waldspurger. Quelques propri´et´es arithm´etiques de certaines formes automorphes sur GL(2). Compositio. Math., 54: 121–171, 1985. Sur les valeurs de certaines fonctions L automorphhes en leur centre de sym´etrie. Compositio. Math. 54: 173-242, 1985.

[38] Vinayak Vatsal. Uniform distribution of Heegner points. Invent. Math. 148 (1): 1–46, 2002

[39] S. Zhang Equidistribution of CM points on quaternion Shimura varieties. Preprint.