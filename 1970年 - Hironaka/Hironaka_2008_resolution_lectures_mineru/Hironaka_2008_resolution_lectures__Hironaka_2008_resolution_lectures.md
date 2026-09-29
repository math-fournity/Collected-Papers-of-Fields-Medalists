# RESOLUTION OF SINGULARITIES

BY HEISUKE HIRONAKA

## 1. Introduction

I am much indebted to many mathematical colleagues and friends from whom I borrow precious ideas, critics, advices and comments, to name some from among them: O. Zariski, M. Nagata, S. Abhyankar, T. Oda, J. Giraud, B. Teissier, M. Lejeune, Le Dung Trang, T.T. Moh, M. Spivakovsky, H-M Aroca, F. Cano, O. Villamayer, H. Hauser, J. Cossart, D. Cutkosky, E. Bierstone, P. Milman, J. Kollar, H. Kawanoue, J. Wlodarczyk.

This work would not have been made possible without the stimulation and encouragement that I received at many international mathematical meetings I attended. Above all the following must be cited:

2005 March at Univ.Valladolid, Spain,

2006 June in Trieste Inst., Italy, and Sept. in Tordesillas Inst., Spain 2008 Spring at Seoul National Univ., Korea, and Sept. at Clay Mathematics Inst., USA, and Dec. RIMS, Kyoto, Japan

2009 May at Clay Mathematics Inst., and Harvrd Univ., USA, and Spring at Seoul National Univ., Korea

2010 Fall at at Seoul National Univ., Korea

2011 April at Clay Mathematics Inst., and Harvard Univ., USA

## 2. Ideal Exponents

Readers may refer to [22], [21] and [23].

An idealistic exponent is a pair (J, b) where

(1) J is an ideal given in an ambient scheme Z

(2) and b is a positive integer.

(a) The ambient scheme is a smooth irreducible scheme of finite type over a base field K. Our primary interest lies in the case in which K is perfect of characteristic$p > 0$. But for technical reasons we may consider imperfect cases, too.

(b) We sometimes need ambient extensions from Z to

$$
Z [ t ] = Z \times_ {\mathbb {K}} S p e c (\mathbb {K} [ t ])
$$

with a finite number of additional variables t.

(c) Define the order and singular locus by

$$
\begin{array}{c} o r d _ {\xi} (J, b) = b ^ {- 1} o r d _ {\xi} (J) a n d \\ S i n g (J, b) = \{\xi \in Z | o r d _ {\xi} (J, b) \geq 1 \}. \end{array}\tag{2.1}
$$

Definition 2.1. A blow-up$\pi : Z ^ { \prime } \to Z$with center D is said permissible for$E = ( J , b )$if D is smooth irreducible and$\subset S i n g ( E )$

Definition 2.2. The transform of$E = ( J , b )$by π is$E ^ { \prime } = \left( J ^ { \prime } , b \right)$ with$J ^ { \prime } = ( I ( D , Z ) \mathcal { O } _ { Z ^ { \prime } } ) ^ { - b } J \mathcal { O } _ { Z ^ { \prime } }$where$I ( D , Z )$denotes the ideal sheaf defining$D \subset Z .$

In other words the b-times exceptional divisor is removed from the total transform. Note that$I ( D , Z ) { \mathcal { O } } _ { Z ^ { \prime } }$is invertible as$\mathcal { O } _ { Z ^ { \prime } } { \mathrm { - m o d u l e } }$

## 3. differential operators in characteristic$p > O$

Conventional Notation:

$d i m ( Z ) = n \ge 1 , \xi \in Z$is usually a closed point,$\mathcal { O } _ { Z }$denotes the structure sheaf.$R = R _ { \xi } = \mathcal { O } _ { Z , \xi } , M = M _ { \xi } = m a x ( R ) , \kappa = \kappa _ { \xi } = R / M$

Assume that κ is separable algebraic over K and pick any regular system of parameters$x = ( x _ { 1 } , \cdots , x _ { n } )$of R. Then there exist a free base$\{ \partial ^ { ( a ) } = \partial _ { x } ^ { ( a ) } , a \in \mathbb { Z } _ { 0 } ^ { n } \}$of the R-module of diferential operators $D i f f _ { Z , \xi } = D i f f _ { R / \mathbb { K } }$, uniquely determined by the following property.

$$
\partial^ {(\alpha)} x ^ {\beta} = \left\{ \begin{array}{l l} \binom {\beta} {\alpha} x ^ {\beta - \alpha} & i f \beta \in \alpha + \mathbb {Z} _ {0} ^ {n} \\ 0 & i f o t h e r w i s e \end{array} \right.\tag{3.1}
$$

called “elementary” diferential operators with respect to x.

Using a system of indeterminates$t = ( t _ { 1 } , \cdots , t _ { n } )$we have

$$
\partial^ {(\alpha)} (f) (x) = \text {   the   coefficient   of   } t ^ {\alpha} \text {   in   } f (x + t).\tag{3.2}
$$

We pick$q = p ^ { e } , e \geq 0$, and let ρ denote the Frobenius p-th power so that$\rho ^ { e } ( f ) = f ^ { q }$

Remark 3.1. We have$D i f f _ { R / \rho ^ { e } ( R ) } \subset D i f f _ { R / \mathbb { K } }$. Let us denote

$$
\epsilon^ {n} (q) = \{a \in \mathbb {Z} _ {0} ^ {n} | 0 \leq a _ {j} \leq q - 1, \forall j \}\tag{3.3}
$$

Then$\{ \partial ^ { ( a ) } , a \in \epsilon ^ { n } ( q ) \}$is a free base of R-module$D i f f _ { R / \rho ^ { e } ( R ) }$. It is dual to the free base$\{ x ^ { b } \mid b \in \epsilon ^ { n } ( q ) \}$of R as$\rho ^ { e } ( R ) { \mathrm { - m o d u l e } }$

Let$D i f f _ { R _ { \xi } / \mathbb { K } } ^ { ( m ) }$(also$D i f f _ { Z , \xi } ^ { ( m ) } )$denote the R-submodule of$D i f f _ { Z , \xi }$ which consists of those diferentil operators of orders$\leq m$

$$
\text { Define } \quad D i f f _ {R _ {\xi} / \mathbb {K}} ^ {(m) *} = \{\partial \in D i f f _ {R _ {\xi} / \mathbb {K}} ^ {(m)} \mid \partial (\mathbb {K}) = 0 \}\tag{3.4}
$$

We let$\begin{array} { r } { D i f f _ { R _ { \xi } / \mathbb { K } } ^ { * } = D i f f _ { Z , \xi } ^ { * } = \bigcup _ { a l l \ m \geq 0 } D i f f _ { R _ { \xi } / \mathbb { K } } ^ { ( m ) * } . } \end{array}$

## 4. idempotent differential operators

Review on logarithmic diferential calculus. Refer to the work of H.Kawanoue, [27]. We then extend it to those of “idempotent” and “primitive” operators which we introduce in this section and the next.

Consider a field extension$L = K ( x )$with$\boldsymbol { x } = ( x _ { 1 } , \cdots , x _ { s } )$which is a q-independent base of$L / K$in the follwoing sense.

(1) For each$i , x _ { i } ^ { q } = a _ { i } \in K$, and

(2) every relation among x over K is generated by$X _ { i } ^ { q } - a _ { i } , 1 \leq i \leq$ $n ,$in the polynomial algebra$K [ X ]$

Definition 4.1. Define the Z/pZ-module$D l o g _ { x } ( L / K )$which is freely generated by$\{ x ^ { a } \partial ^ { ( a ) } \in D i f f _ { L / K } | a \in \epsilon ^ { s } ( q ) \}$. They will be called$q -$ logarithmic diferential operators of$L / K$with respect to$x .$

We then define “idempotent diferential operators” as folows.

$$
\mathfrak {d} ^ {(a)} = \sum_ {k \in \epsilon^ {s} (q) \cap (a + \mathbb {Z} _ {0} ^ {s})} C _ {a k} x ^ {k} \partial^ {(k)}\tag{4.1}
$$

where$C _ { a k }$are chosen as follows:$C _ { a a } = 1$and for$b \neq a$

$$
C _ {a b} = \left\{ \begin{array}{l l} - \sum_ {k \in a + \mathbb {Z} _ {0} ^ {s}, b \in k + \mathbb {Z} _ {0} ^ {s}, b \neq k} C _ {a k} \binom {b} {k} & \text {if} b \in (a + \mathbb {Z} _ {0} ^ {s}), \neq a, \\ 0 & \text {if otherwise.} \end{array} \right.
$$

We then have that

$$
\mathfrak {d} ^ {(a)} x ^ {b} = \left\{ \begin{array}{l l} x ^ {b} & \text { if   } b = a \\ 0 & \text { if   otherwise } \end{array} \right.\tag{4.2}
$$

(1)${ \mathfrak { d } } ^ { ( a ) }$is idempotent for every$a \in \epsilon ^ { s } ( q ) , \mathrm { i . e . , } \mathfrak { d } ^ { ( a ) } \mathfrak { d } ^ { ( a ) } = \mathfrak { d } ^ { ( a ) }$

(2) they are mutually independent, i.e.,${ \mathfrak { d } } ^ { ( a ) } { \mathfrak { d } } ^ { ( b ) } = 0$for all$a \neq b$

(3) and$\textstyle \sum _ { a \in \epsilon ^ { s } ( q ) } { \mathfrak { d } } ^ { ( a ) } = \mathbf { 1 }$, the identity operator in$D i f f _ { L / K }$

We then define$\begin{array} { r } { \mathfrak { d } ^ { * } \ = \ \sum _ { 1 \leq j \leq m } \mathfrak { d } _ { j } } \end{array}$and call it a \*-full ID for$L / K$

Theorem 4.1. With$L / K$Let$\mathfrak { d } ^ { * } ( i ) , i = 1 , 2$, be a pair of the$\ast _ { - } f u l l$ ID operators. We then have$\mathfrak { d } ^ { * } ( 2 ) \mathfrak { d } ^ { * } ( 1 ) = \mathfrak { d } ^ { * } ( 2 )$and also${ \mathfrak { d } } ^ { * } ( 1 ) ( h ) -$ ${ \mathfrak { d } } ^ { * } ( 2 ) ( h ) \in K$for every$h \in L$

It should be noted that those${ \mathfrak { d } } ^ { * } ( i )$may be the ones defined with respect to resular system of parameters at birationally correponding points of diferent birational models respectively. For instance think of one model and another obtained by a sequence of blowups.

## 5. primitive and nilpotent differential operators

Consider$L = K ( u )$with q-independent base u for$L / K$

Definition 5.1. For each$a \in \epsilon ^ { s } ( q )$with the length s of u we define $\delta _ { u } ^ { ( a ) } ~ = ~ u ^ { - a } \mathfrak { d } ^ { ( a ) }$. Here the division is done inside$D i f f _ { L / K }$

Theorem 5.1. With$L = K [ u ]$we have the following equality.

$$
(\mathbb {Z} / p \mathbb {Z}) [ u, \{\partial^ {(a)} \} ] = (\mathbb {Z} / p \mathbb {Z}) [ u, \{\delta^ {(a)} \} ]\tag{5.1}
$$

where the set { } is for all indices$a \in \epsilon ^ { s } ( q )$

Theorem 5.2. Consider the following special case.

(1) L and K are the fields of regular local rings R and$S \subset R .$

(2)$( u , w )$is a regular system of parameters of R while$( u ^ { q } , w )$is that of S and$R = S [ u ]$with q-independent u.

We then claim that$P = \{ \delta _ { u } ^ { ( a ) } , \forall a \in \epsilon ^ { s } ( q ) \}$has the following properties.

(1) P is a free base of the R-module Diff<sub>R/S</sub> as well as that of

L-module$D i f f _ { L / K }$

(2) P is dual to the free base$\{ u ^ { a } , a \in \epsilon ^ { s } ( q ) \}$of$L / K$, i.e, for every $a \in \epsilon ^ { s } ( q )$and for$a ^ { \prime } \in \epsilon ^ { s } ( q )$we have

$$
\delta_ {u} ^ {(a)} u ^ {a ^ {\prime}} = \left\{ \begin{array}{l l} 1 & \text {if a = a^{\prime}} \\ 0 & \text {if otherwise} \end{array} \right.\tag{5.2}
$$

Theorem 5.3. (1) For$0 \in \epsilon ^ { s } ( q )$we have

$$
\delta_ {u} ^ {(0)} = \mathfrak {d} _ {u} ^ {(0)} = i d e n t i t y - \sum_ {0 \neq a \in \epsilon^ {s} (q)} u ^ {a} \delta^ {(a)}\tag{5.3}
$$

which is idempotent and$\in H o m _ { \rho ^ { e } ( R _ { \xi } ) [ w ] } ( R _ { \xi } , \rho ^ { e } ( R _ { \xi } ) [ w ] )$

(2)$\delta _ { u } ^ { ( 0 ) } \delta _ { u } ^ { ( a ) } = \delta _ { u } ^ { ( a ) }$for every$a \in \epsilon ^ { s } ( q )$, and

$$
\delta_ {u} ^ {(a)} \delta_ {u} ^ {(0)} = \left\{ \begin{array}{l l} \delta_ {u} ^ {(0)} & \text {   if   } a = 0 \\ 0 & \text {   if   } a \neq 0 \end{array} \right.
$$

(3) If$a \neq 0$and$b \neq 0$then$\delta _ { u } ^ { ( a ) } \delta _ { u } ^ { ( b ) } = 0$. For$a \neq 0 , \delta _ { u } ^ { ( a ) }$is square nilpotent.

$$
(4) \sum_ {a \in \epsilon^ {s} (q)} \rho^ {e} (R) [ w ] \delta^ {(a)} = H o m _ {\rho^ {e} (R) [ w ]} \big (R, \rho^ {e} (R) [ w ] \big)
$$

(5)$\begin{array} { r } { \partial = \sum _ { a } \theta _ { a } ^ { q } \delta ^ { ( a ) } } \end{array}$is square-nilpotent if and only if$\partial \in D i f f _ { Z } ^ { * }$. This means$\theta _ { a } = 0$

Definition 5.2. Let us define:

$$
\mathcal {P} ^ {q} (u / w) = \sum_ {a \in \epsilon^ {s} (q)} \rho^ {e} (R) \delta^ {(a)} = H o m _ {\rho^ {e} (R) [ w ]} \big (R, \rho^ {e} (R) [ w ] \big)
$$

and

$$
\mathcal {P} ^ {* q} (u / w) = \sum_ {0 \neq a \in \epsilon^ {s} (q)} \rho^ {e} (R) \delta^ {(a)} = \mathcal {P} ^ {q} (u / w) \cap D i f f _ {Z} ^ {*}
$$

Note that they depend only on w but not on u at all.

## SINGULARITIES

## 6. infinitely near singularities

In this section we consider an arbitrary base field K.

Definition 6.1. An LSB over$Z$is defined to mean a diagram of the following form.

$$
\begin{array}{c c c} \pi_ {r - 1} & & \pi_ {r - 2} \\ Z _ {r} \to & U _ {r - 1} \subset Z _ {r - 1} & \to \\ & \bigcup \\ & D _ {r - 1} \end{array}
$$

$$
\begin{array}{c c c c} \pi_ {1} & & \pi_ {0} \\ \to & U _ {1} \subset Z _ {1} & \to & U _ {0} \subset Z _ {0} = Z \\ & \bigcup & & \bigcup \\ & D _ {1} & & D _ {0} \end{array}
$$

where$U _ { i } \subset Z _ { i }$is open,$D _ { i }$is a “regular” irreducible closed in$U _ { i }$and the$\pi _ { i } : Z _ { i + 1 } \to U _ { i }$is the blow-up with center$D _ { i }$

Any blowup with empty center is the identity morphism

Definition 6.2. We define the t-indexed disjoint union:

$$
\mathfrak {S} (E) =\tag{6.1}
$$

$$
\bigcup_ {t} \left\{\text {   the   LSBs   over   } Z [ t ] \text {   permissible   for   } E [ t ] = (J [ t ], b) \right\}
$$

which is the totality of the infinitely near singular points of E in$Z _ { i }$with arbitrary finite systems t of indeterminates. Say$^ { 6 6 } E _ { 2 }$is more singular than$E _ { 1 } { } ^ { \prime \prime } { \mathrm { ~ i f ~ } } { \mathfrak { S } } ( E _ { 2 } ) \supset { \mathfrak { S } } ( E )$, and define the equivalence relation by

$$
E _ {1} \sim E _ {2} \Longleftrightarrow \mathfrak {S} (E _ {1}) = \mathfrak {S} (E _ {2})\tag{6.2}
$$

Definition 6.3. When the base field K is arbitrary, we take its algebraic closure K<sup>˜</sup> and consider the base field extensions

$$
\tilde {Z} = Z \times_ {\mathbb {K}} \tilde {\mathbb {K}} a n d \tilde {E} = E \times_ {\mathbb {K}} \tilde {\mathbb {K}}\tag{6.3}
$$

We will let$\sigma$denote the projection$\tilde { Z }  Z$so that$\tilde { E } = \sigma ^ { - 1 } ( E )$, the pullback of$E = ( J , b )$by$\sigma$that is$( J \mathcal { O } _ { \tilde { Z } } , b )$on$\tilde { Z }$. Then we have$\mathfrak { S } ( \tilde { E } )$ which will be also written as$\tilde { \mathcal { S } } ( E )$

## 7. Three basic technical theorems

Recall what we called the Three Key Theorems which were proven in [22] and [24].

Theorem 7.1. (Diferentiation theorem )

For every$\mathcal { O } _ { Z }$-submodule D of$D i f f _ { Z } ^ { ( i ) }$, we have

$$
\mathfrak {S} (D i f f _ {Z} ^ {(i)} J, b - i) \supset \mathfrak {S} (J, b)
$$

Theorem 7.2. (Ambient Reduction Theorem)

Given an ideal exponent$E = ( J , b )$in$Z$, we let

$$
J ^ {\sharp} = \sum_ {j = 0} ^ {b - 1} \left(D i f f _ {Z} ^ {(j)} J\right) ^ {\frac {b ^ {\sharp}}{b - j}} \text {   with   } b ^ {\sharp} = b!.
$$

For any smooth subscheme$W \subset Z$, we let$F = ( J ^ { \sharp } { \mathcal { O } } _ { W } , b ^ { \sharp } )$Then F is an ambient reduction of E from Z to W in the following sense $( d e f i n i t i o n )$

Pick any t and any LSB over$Z [ t ]$, such that all of its centers are in the strict transforms of W[t]. Then we have$L S B \in { \mathfrak { S } } ( E )$if and only if the LSB induces to W the one belonging to${ \mathfrak { S } } ( F )$

Theorem 7.3. (Numerical Exponent Theorem)

Let$E _ { i } = ( J _ { i } , b _ { i } ) , i = 1 , 2$, be two ideal exponents in Z.$I f \mathfrak { S } ( E _ { 1 } ) =$ ${ \mathfrak { S } } ( E _ { 2 } )$then or$\cdot d _ { \xi } ( J _ { 1 } ) / b _ { 1 } = o r d _ { \xi } ( J _ { 2 } ) / b _ { 2 }$for every$\xi \in Z$where any one of the two$i s \geq 1$

## 8. The Characteristic Algebra

We are primarly interested in the case of a “perfect” base field K. An important point of the “perfect” case is the the geometric definition coincides with the algebraic one for the characterisitic algebra. They do not in general. The geometric and the algebraic have diferent charaters with respect to base field extenstions.

If K is imperfect we then take the algebraic closure K<sup>˜</sup> of K and the base field extention from K to K<sup>˜</sup> . We then have$\tilde { Z } = Z \times _ { \mathbb { K } } \tilde { \mathbb { K } }$, projection morphism$\sigma : \tilde { Z }  Z , \tilde { E } = E \times _ { \mathbb { K } } \tilde { \mathbb { K } }$and we let$\tilde { \mathfrak { S } } ( E ) = \mathfrak { S } ( \tilde { E } )$compared with${ \mathfrak { S } } ( E )$. We examine the “inseparable descent” with respect to$\sigma$.

Definition 8.1. The “geometric ” characteristic algebra of$E = ( J , b )$ is defined to be the following graded$\mathcal { O } _ { \mathcal { Z } ^ { - } \mathrm { a l g e b r a } }$

$$
\wp_ {g e o} (E) = \sum_ {a = 0} ^ {\infty} J _ {m a x} (a) T ^ {a}\tag{8.1}
$$

where$T$is a dummy variable to indicate homogeneous degrees and

$$
J _ {m a x} (a) = \bigcup \{I \mid \mathfrak {S} (I, a) \supset \mathfrak {S} (J, b) \}\tag{8.2}
$$

Definition 8.2. The “algebraic ” characteristic algebra$\wp _ { a l g } ( E )$of$E =$ $( J , b )$is defined to be the integral closure of the following subalgebra.

$$
\mathcal {O} _ {Z} \left[ J ^ {\sharp} T ^ {b ^ {\sharp}} \right] = \sum_ {\alpha = 0} ^ {\infty} \left(J ^ {\sharp}\right) ^ {\alpha} T ^ {b ^ {\sharp} \alpha} \subset \sum_ {\beta = 0} ^ {\infty} \mathcal {O} _ {Z} T ^ {\beta} = \mathcal {O} _ {Z} [ T ]\tag{8.3}
$$

where$b ^ { \sharp } = b !$and

$$
J ^ {\sharp} = \sum_ {0 \leq \mu \leq b - 1} \left(D i f f _ {Z / \mathbb {K}} ^ {(\mu)} J\right) ^ {b ^ {\sharp} / (b - \mu)}
$$

Thus$\wp ( E )$is clearly finitely presented as a graded O<sub>Z</sub>-algebra with globally coherent homogeneous parts.

Theorem 8.1. We always have$\wp _ { a l g } ( E ) \supset \wp _ { g e o } ( E )$If the base field mathbbK is perfect then we have$\wp _ { g e o } ( E ) \ = \ \wp _ { a l g } ( E )$

This theorem asserts that the algebraic condition Eq.(8.3) of is equivalent to the geometric one Eq.(8.1). This has been proven in my earlier paper [23]. For the detail of the proof of the algebraic characterization Eq.(8.3) of$\wp ( E )$, the reader should refer to the proofs of Lemmas 2.1 - 2.2 and the equality (♭) of page 918 of the paper [23]. They are given in the proof of the Main Theorem of [23] asserting the finite presentation of$\wp ( E )$

Theorem 8.2. The graded${ \mathcal { O } } _ { Z ^ { - } } a l g e$bra$\begin{array} { r } { \wp ( E ) = \sum _ { a } J _ { m a x } ( a ) } \end{array}$for$E =$ $( J , b )$is the smallest O<sub>Z</sub>-subalgebra of$\mathcal { O } _ { Z } [ T ]$such that

(1)$J ~ \subset ~ J _ { m a x } ( b )$

(2)$D i f f _ { Z } ^ { ( \mu ) } J _ { m a x } ( a ) ~ \subset ~ J _ { m a x } ( a - \mu ) ~ f o r ~ a l l ~ 0 \leq \mu < a$and

(3)$\wp ( E )$is integrally closed in$\mathcal { O } _ { Z } [ T ]$

For a proof of the second property above, we may use Diferentiation theorem Th.(7.1) applied to$J _ { m a x } ( a )$of Eq.(8.2) and Th.(8.1), together with the following lemma.

Lemma 8.3. For every$\begin{array} { r } { a = \sum _ { i = 0 } ^ { b - 1 } ( b - i ) \alpha _ { i } } \end{array}$with$\alpha \in \mathbb { Z } _ { 0 } ^ { b }$and for every $\mu < a$

$$
D i f f_{Z}^{(\mu)}\Big(\prod_{i = 0}^{b - 1}\bigl (D i f f_{Z}^{(i)}J \bigr)^{\alpha_{i}}\Big)\\ \subset \sum_{\substack{\beta \in \mathbb{Z}_{0}^{b}\\ \sum_{i = 0}^{b - 1}\beta_{i}(b - i) = a - \mu}}\Big(\prod_{i = 0}^{b - 1}\bigl (D i f f_{Z}^{(i)}J \bigr)^{\beta_{i}}\Big)
$$

For its proof once again we refer to Remarks (2.1)-(2.2) of [23].

Remark 8.1. For comparison we first recall the case of characteristic zero, for instance$\mathbb { K } = \mathbb { C }$. Consider a plane curve defined by

$$
f (x, y) = \sum_ {i j} c _ {i j} x ^ {i} y ^ {j} \text {with} c _ {i j} \in \mathbb {K}
$$

such that its multiplicity is$m = o r d _ { ( 0 , 0 ) } ( f )$and its first characteristic exponent is$n / m = \delta = m i n \{ i / ( m - j ) \mid j < m , c _ { i j } \neq 0 \}$

Now for$E = ( f \mathbb { K } [ x , y ] , m )$, we can prove that$\begin{array} { r } { \wp ( \dot { E } ) = \sum _ { l = 0 } ^ { \infty } J _ { m a x } ( l ) T ^ { a } } \end{array}$ is determined by δ within a neighborhood of$\xi \in Z$as follows:

$$
J _ {m a x} (l) = \{x ^ {i} y ^ {j} | \frac {i}{\delta} + j \geq l, i \geq 0, j \geq 0 \} \mathbb {K} [ x, y ], \quad \forall l \geq 0.
$$

$\mathrm { A s }$is seen below, the above assertion fails to be true in general when char$( \mathbb { K } ) = p > 0$

Next, let K be an algebraically closed field of characteristic$p > 0$ Consider a plane curve defined by$f = y ^ { q } - x ^ { n }$with$q = p ^ { e } , e > 0$, and $n > q , ( n , p ) = 1$. Then we have$\mathrm { ~ a ~ } ^ { 6 6 } \mathrm { ~ 3 ~ } ^ { \mathfrak { N } }$-dimensional Newton polygon, so to speak, in the sense that

$$
J _ {m a x} (l) =
$$

$$
\{x ^ {i} y ^ {j} f ^ {k} \mid i \geq 0, j \geq 0, k \geq 0, i n e q (l) \} \mathbb {K} [ x, y ], \forall l \geq 0
$$

where ineq(l) means

$$
i \frac {q - 1}{n - 1} + j \frac {n (q - 1)}{q (n - 1)} + k q \geq l.
$$

## 9. Comments on the imperfect base field

Consider the case of$Z$“smooth” over K which is “imperfect”.

We then use the algebraic closure K<sup>˜</sup> of K after Def.(6.3) and Eq.(6.3) with$\sigma : \tilde { Z }  Z , \tilde { E } , \tilde { \mathfrak { S } } ( E ) , \tilde { \wp } ( E ) = \wp ( \tilde { E } )$,“geometric” and “algebraic”. “Geometrically”$\wp _ { g e o } ( \tilde { E } )$is ‘ more efective than$\wp _ { g e o } ( E )$

Theorem 9.1. In general, including the cases of imperfect$\mathbb { K } , \wp _ { a l g } ( E )$ is equal to the “inseparable descent” of$\wp _ { a l g } ( \tilde { E } )$from$\tilde { \mathbb { K } }$to K in the sense of Def.(9.1) below, while$\wp _ { g e o } ( E )$contains the inseparable descent $o f \wp _ { g e o } ( \tilde { E } )$but not equal in general.

Definition 9.1. We define the “naive” inseparable descent of a${ \mathcal { O } } _ { { \tilde { Z } } ^ { - } }$ module$\tilde { A }$by σ from$\tilde { \mathbb { K } }$to K. This “descent” is defined as follows:

(1) Choose and fix a free base of$\tilde { \mathbb { K } }$as K-module including 1:

$$
\left\{c _ {i}, i \in \{1, C \} \right\} \text {   where   } C \subset \tilde {\mathbb {K}} \setminus \mathbb {K}\tag{9.1}
$$

(2) Every element$f \in { \tilde { A } }$is uniquely written as$\textstyle f _ { 1 } + \sum _ { i \in C } b _ { i } f _ { i }$with $b _ { i } \in { \mathcal { O } } _ { Z }$where$\sigma _ { * }$denotes the direct image of A<sup>˜</sup> by$\sigma$.

(3) Then the “descent” of A<sup>˜</sup> with respect to the chosen$\mathrm { E q . ( 9 . 1 ) }$to be the collection of$f _ { 1 }$for all$f \in { \tilde { A } }$

In general the “naive” descent depends upon the choice of Eq.(9.1). When it is independent of, we call it the inseparable descent of A<sup>˜</sup>.

Theorem 9.2. The “descent” defined by Def.(9.1) for$\wp _ { a l g } ( \tilde { E } )$is independent of the choice of$E q . ( 9 . 1 )$and it is equal to$\wp _ { a l g } ( E )$, which is the finitely presented graded$\mathcal { O } _ { Z ^ { - } } a l g .$ebra having the “algebrac” characterization Eq.(8.3) of Th.(8.1).

The proof is by$D i f f _ { \tilde { Z } } \ = \ D i f f _ { Z } \otimes _ { \mathcal O _ { Z } } \mathcal O _ { \tilde { Z } } \quad$and by the descent of integral closure.

Now back to the perfect K and examine the changes of$\wp$with respect to locarisaions at non-closed points, such as generic points of singular locus of E.

Pick a system of parameters$t = ( t _ { 1 } , \cdots , t _ { d } )$with$t _ { j } \in \mathcal { O } _ { Z , \xi } , \forall j$, such that

(1) the$t _ { j } , 1 \leq j \leq d _ { \ast }$, are algebraically independent over K and t is extendable to a system of “separating transcendental base of the function field$\mathbb { K } ( Z )$

(2) Let ∇ denote the multiplicative group of nonzero elements of $\mathbb { K } [ t ]$, and apply the localization$\bar { \nabla } ^ { - 1 }$to Z, E and$\wp ( E )$

Example 9.1. Let$D _ { i } , 1 \leq i \leq s .$, be the reduced irreducible components of$S i n g ( E )$having dim$. ( D _ { j } ) = d i m ( S i n g ( E )$. Then pick$t _ { j } ~ \in$ $\cap _ { 1 \leq j \leq s } { \mathcal { O } } _ { Z , \zeta _ { j } }$for everry$j$in such a way that t induces a separating transcendental base of the function field of$D _ { i }$over K for every i. Then t has the properties (1 and (2) as above.

Theorem 9.3. Consider$\nabla ^ { - 1 } E )$as an ideal exponent in$\nabla ^ { - 1 } Z$which is a smooth scheme over the new base field$\mathbb { K } ( t )$. We then claim that

(1)$\wp _ { g e o } ( \nabla ^ { - 1 } E )$is equal to$\nabla ^ { - 1 } \wp _ { g e o } ( E )$, while

(2)$\wp _ { a l g } ( \nabla ^ { - 1 } E )$is equal to the “inseparable descent”$o f _ { \mathit { \delta } ^ { \mathcal { O } } a l g } ( \widetilde { \nabla ^ { - 1 } E } )$ where the˜denote the base field extension from$\mathbb { K } ( t )$to its algebraic closure$\mathbb { K } ( t )$.

The first claim is by the fact that

$$
\nabla^ {- 1} (\mathfrak {S} (E)) = \mathfrak {S} (\nabla^ {- 1} E)\tag{9.2}
$$

where S denotes the totality of infinitely near singularities in the sense of Def.(6.2). The second claim is a special case of Th.(9.2).

## 10. Edge Decompositions

For a regular system of parameters$x = ( x _ { 1 } , \cdots , x _ { n } )$of$R _ { \xi }$, let$\bar { x } =$ $\left( { \bar { x } } _ { 1 } , \cdots , { \bar { x } } _ { n } \right)$with$\bar { x } _ { i } = i n _ { \xi } ( x _ { i } ) , 1 \leq i \leq n$. We have

$$
g r _ {\xi} (R _ {\xi}) = \bigoplus_ {d \geq 0} M _ {\xi} ^ {d} / M _ {\xi} ^ {d + 1} = \kappa_ {\xi} [ \bar {x} _ {1}, \dots , \bar {x} _ {n} ]
$$

This section along with the earlier ones on infinitely near singularities and characteristic algebra are essencially same with what have been presented at the conference June 2006 in Trieste, Italy, [25].

## Theorem 10.1. (Edge Generators Theorem)

We can find

(1) a regular system of parameters$x ~ = ~ ( y , z )$of$R _ { \xi }$where$y =$ $( y _ { 1 } , \cdots , y _ { r } )$with$0 < r \leq n$

(2) a sequence of powers$o f p \colon q _ { i } = p ^ { e _ { i } } , 0 \leq e _ { 1 } \leq \cdot \cdot \cdot \leq e _ { r } ,$

(3)$g _ { i } = y _ { i } ^ { q _ { i } } + \epsilon _ { i } \in J _ { m a x } ( q _ { i } ) _ { \xi }$with$o r d _ { \xi } ( \epsilon _ { i } ) > q _ { i }$

such that for every$a \geq 0$

$$
J_{max}(a)_{\xi}\quad \subset \quad M^{a + 1} + \sum_{\substack{\beta \in \mathbb{Z}_{0}^{r}\\ a = \sum_{j = 1}^{r}q_{j}\beta_{j}}}\Bigl (\prod_{j = 1}^{r}g_{j}^{\beta_{j}}\Bigr)R_{\xi}.\tag{10.1}
$$

Remark 10.1. If there happens to have$q _ { j } = 1$for some$j$then we may replace$y _ { j }$by$g _ { j }$, aiming a “possible” ambient reduction to$y _ { j } = 0$

## Theorem 10.2. (Edge Decomposition Theorem)

We obtain the following equivalence which holds within a suficiently small neighborhood U of$\xi \in Z$

$$
E \sim \left(\bigcap_ {i = 1} ^ {r} E _ {i}\right) \cap F\tag{10.2}
$$

$$
\mathfrak {S} (E) = \left(\bigcap_ {i = 1} ^ {r} \mathfrak {S} (E _ {i})\right) \cap \mathfrak {S} (F)
$$

where$E _ { i } = ( g _ { i } \mathcal { O } _ { U } , q _ { i } ) , 1 \leq i \leq r$, and$\boldsymbol { F } = ( I , \boldsymbol { c } )$with$o r d _ { \xi } ( I ) > c ,$

Definition 10.1. Given an ideal exponent$E$and a closed point$\xi \in \mathbf { \Xi }$ $S i n g ( E )$, a set of edge data of$E$at$\xi$will mean a combination of the following objects and their expressions:

(1) The edge parameters$y = ( y _ { 1 } , \cdots , y _ { r } )$

(2) the edge generators$g = ( g _ { 1 } , \cdots , g _ { r } )$with$g _ { i } = y _ { i } ^ { q _ { i } } + \epsilon _ { i }$and

(3) the edge decomposition

$$
E \sim \left(\bigcap_ {i = 1} ^ {r} E _ {i}\right) \bigcap F \text {where} E _ {i} = (g _ {i} \mathcal {O} _ {Z}, q _ {i})
$$

Definition 10.2. The primary inductive strategy:

Our approach to the inductive proof will be based upon the following system of numbers.

$$
\operatorname{Inv} _ {\xi} (E) = (n, n - r, q _ {1}, \dots , q _ {r}).\tag{10.3}
$$

with respect to the lexicographical ordering. The system will be called the edge invariants of$E$at$\xi .$. The first number n is$d i m _ { \xi } Z$and the other numbers$\{ r , q _ { i } =$ $p ^ { e _ { i } } , 1 \leq i \leq r , \}$are the ones defined by Th(10.1).

Remark 10.2. If$n = 1$then the problem is trivial. If$n - r = 0$, it is easy. If$n - r = 1$then it is a question similar to resolution of curve singularities. What is more, if$q _ { 1 } = 1$that is$e _ { 1 } = 0$then at least $^ { 6 } \mathrm { l o c a l l y } ^ { \mathrm { 7 } }$at$\xi$we can apply the ambient reduction theorem Th.(7.2) from$\dot { Z }$to the hypersurface$g _ { 1 } = y _ { 1 } = 0$. This provision$\mathrm { \ddot { \hbar } l o c a l l y \ ' }$will be cleared later by a “global” procedure of selecting and modifying those$y _ { i }$. The inductitive proof will thus start working.

## SINGULARITIES

## 11. Transforms of edge data

We want to examine transforms of the edge parameters y and the edge generaters g by means of permissible blowups for the given$E .$

Theorem 11.1. Pick a blowp$\pi : Z ^ { \prime } \longrightarrow Z$with center D permissible for$E$. Then the edge invariants never increases. To be precise pick any closed point$\xi ^ { \prime } \in \pi ^ { - 1 } ( \xi ) \cap S i n g ( E ^ { \prime } )$where$E ^ { \prime }$denotes the transform of E by π. Then we have$I n v _ { \xi ^ { \prime } } ( E ^ { \prime } ) \leq I n v _ { \xi } ( E )$in the lexicographical ordering.

Theorem 11.2. Let$\pi : Z ^ { \prime } \to Z$be a permssible blowup for E. Let $I = I ( Z , D ) _ { \xi }$, Pick a closed point$\xi \in D$and a closed point$\xi ^ { \prime } \in$ $\pi ^ { - 1 } ( \xi ) \cap \left( \cap _ { 1 \leq i \leq r } S i n g ( G _ { i } ^ { \prime } ) \right)$where$G _ { i } ^ { \prime }$is the transform of$G _ { i }$for each$i .$. Pick any system z such that(y, z)$( y , z )$is a regular system of parameters of $R _ { \xi }$. Then we can find an exceptional parameter z at$\xi ^ { \prime }$such that

(1)$\mathfrak { z } \in \mathbb { K } [ z ]$and$\mathfrak { z } ^ { - 1 } y _ { i } \in R _ { \xi ^ { \prime } }$<sub>′</sub> for all i,$1 \leq i \leq r .$

(2) If$I n v _ { \xi ^ { \prime } } ( E ^ { \prime } ) = I n v _ { \xi } ( E )$then there exists$c _ { i } \in \mathbb { K }$with${ \mathfrak { z } } ^ { - 1 } y _ { i } - c _ { i } \in$ $M _ { \xi ^ { \prime } } \ f o r \ a l l \ i$

The following lemmas are needed for the proofs of those theorems.

Lemma 11.3. The permissibility implies that the ideal I of the center contains$y _ { i } - \phi _ { i } , \ s a y = \mathfrak { \eta } _ { i }$, with$\phi _ { i } \in M _ { \xi } ^ { 2 }$for every i.

Lemma 11.4.$\left( \mathfrak { H } _ { 1 } , \cdots , \mathfrak { H } _ { r } , \mathfrak { z } \right)$is extendable to a base of I as well as to a regular system of parameters of$R _ { \xi }$and${ \mathfrak { z } } ^ { - 1 } \mathfrak { \mathfrak { \eta } } _ { i } \in R _ { \xi ^ { \prime } }$for all i.

Lemma 11.5.$\boldsymbol { y } ^ { \prime } = \left( \boldsymbol { \mathfrak { z } } ^ { - 1 } \mathfrak { \mathfrak { \eta } } _ { 1 } , \cdot \cdot \cdot , \boldsymbol { \mathfrak { z } } ^ { - 1 } \mathfrak { \mathfrak { u } } _ { r } , \mathfrak { z } \right)$is extendable to a regular system of parameters of$R _ { \xi ^ { \prime } }$.

Lemma 11.6. If$I n v _ { \xi ^ { \prime } } ( E ^ { \prime } ) ~ \ge ~ I n v _ { \xi } ( E )$then$I n v _ { \xi ^ { \prime } } ( E ^ { \prime } ) ~ = ~ I n v _ { \xi } ( E )$ Moreover the transform$E _ { i } ^ { \prime }$of$E _ { i }$by π is equal to$\left( g _ { i } ^ { \prime } \mathcal { O } _ { Z ^ { \prime } } , q _ { i } \right)$with$g _ { i } ^ { \prime } =$ $3 ^ { - q _ { i } } g _ { i }$for all i and we obtain an edge decomposition of the transform $E ^ { \prime }$of E by π at the point$\xi ^ { \prime }$

$$
\mathfrak {S} (E ^ {\prime}) = \left(\bigcap_ {i = 1} ^ {r} \mathfrak {S} (E _ {i} ^ {\prime})\right) \bigcap \mathfrak {S} (F ^ {\prime})\tag{11.1}
$$

where$F ^ { \prime }$is the transform of$F$by π.

Lemma 11.7. So long as$\xi ^ { \prime } \in S i n g ( E ^ { \prime } )$the exceptional parameter z of $L e m . ( 1 1 . 3 )$can be chosen from the polynomial ring$\mathbb { K } [ z ]$

## 12. Normal crossing data

From now on we assume that we are given a normal crossing data

$$
\Gamma = (\Gamma_ {1}, \dots , \Gamma_ {s})
$$

in$Z ,$called the NC-data for short.

Definition 12.1. A blow-up$\pi : Z ^ { \prime } \to Z$with center D is called permissible for Γ if D is smooth irreducible and have normal crossing with Γ.

Definition 12.2. The transform$\Gamma ^ { \prime }$of Γ by$\pi$of the above Def.(12.1) is defined to be$\Gamma ^ { \prime } = ( \Gamma _ { 1 } ^ { \prime } , \cdot \cdot \cdot , \Gamma _ { s } ^ { \prime } , \Gamma _ { s + 1 } ^ { \prime } )$where

(1)$\Gamma _ { i } ^ { \prime }$is the strict transform of$\Gamma _ { i }$by π for every i,$1 \leq i \leq s$ $( \dot { \Gamma } _ { i } ^ { \prime } = \varnothing \mathrm { ~ i f ~ } D = \Gamma _ { i } )$

(2)$\Gamma _ { s + 1 } ^ { \prime }$is the exceptional divisor$\pi ^ { - 1 } ( D )$of$\pi$.

Remark 12.1.General agreement (1):

From now on the Γ-permissibility is always imposed even when it is not mentioned.

General agreement (2):

The ordering of the components of Γ will be recorded as the history of their creation. Thus it is important to note that the new exceptional divisor is placed in the last spot of the sequence$\Gamma ^ { \prime }$

Theorem 12.1. Assume that a NC-data Γ and a smooth subscheme W are given in Z. Then there exists a naturally defined coherent ideal $F ( W / \Gamma )$in${ \mathcal { O } } _ { W }$such that

$$
\begin{array}{c} W \text {is normal crossing with} \Gamma \\ \Longleftrightarrow F (W / \Gamma) _ {\xi} = \mathcal {O} _ {W, \xi} \end{array}
$$

Definition 12.3. The ideal$F ( W / \Gamma ) _ { \xi }$is the unique ideal satisfying the following equality.

$$
\begin{array}{c} F (W / \Gamma) _ {\xi} \left(\bigwedge^ {d} \Omega_ {W, \xi}\right) \\ = \left(\bigwedge^ {d - c (\xi / W)} \Omega_ {W, \xi}\right) \left(\bigwedge^ {c (\xi / W)} \bigoplus_ {i: \xi \in W \cap \Gamma_ {i} \neq W} \delta_ {W} \big (I (\Gamma_ {i}, Z) \mathcal {O} _ {W, \xi} \big)\right) \end{array}
$$

where$d = d i m _ { \xi } W$and$c ( \xi / W )$is the number of the indices i with $\xi \in W \cap \Gamma _ { i } \neq W .$

The following lemma is useful in many inductive steps.

Lemma 12.2. (called “denominator$l i f t i n g ^ { \prime \prime } )$Compare$E = ( J , b )$with $\check { E } = ( J , m )$for some$m > b$. Then,$a f t e r$any finite sequence of permissible blowups, their transforms$E ^ { \prime } = ( J ^ { \prime } , b )$and$\check { E } ^ { \prime } = ( \check { J } ^ { \prime } , m )$by a Γ′-monomial factor$Q$in their ideals. Namely$J ^ { \prime } = Q \breve { J } ^ { \prime }$at every point $o f S i n g ( \check { E } ^ { \prime } )$. Here$\Gamma ^ { \prime }$denotes the transform of Γ

Theorem 12.3. Assume that$E = ( J , b )$has locally Γ-monomial J everywhere in Z. Write$\begin{array} { r } { J = \prod _ { 1 \leq a \leq s } J _ { a } ^ { d _ { a } } } \end{array}$where$J _ { a }$is the ideal of$\Gamma _ { a }$ in${ \mathcal { O } } _ { Z }$. Then there exists a canonical sequence of permissible blowups $\tilde { \pi } : \tilde { Z } \to Z$such that$S i n g ( \tilde { E } ) = \emptyset$with the transform$\tilde { E }$of E by$\tilde { \pi }$.

The “Canonical Procedure” is as follows.

(1) Let$\Gamma = ( \Gamma _ { 1 } , \cdot \cdot \cdot , \Gamma _ { s } )$. For each nonempty$A \subset [ 1 , s ]$, we denote $D ( A ) = \cap _ { a \in A } \Gamma _ { a }$and$\textstyle { \boldsymbol { \sigma } } ( A ) = \sum _ { a \in A } d _ { a }$

(2) Let$S _ { 0 } ( E ) = \{ A \subset [ 1 , s ] ~ | ~ \sigma ( A ) \geq b$and$D ( A ) ~ \neq ~ \varnothing ~ \}$

(3) Let$S _ { 1 } ( E ) = \{ A \in { \mathcal { S } } _ { 0 } ( E ) ~ | ~ | A | = { \bar { \lambda } } ( E ) \}$

with$\bar { \lambda } ( E ) = \operatorname* { m i n } \{ \left| A \right| \mid A \in { \mathcal { S } } _ { 0 } ( E ) \}$where$| A |$is the cardinality of A.

(4)$\operatorname { L e t } S _ { 2 } ( E ) = \{ A \in { \mathcal { S } } _ { 1 } ( E ) ~ | ~ \sigma ( A ) = { \hat { \sigma } } ( E ) \}$

with$\hat { \sigma } ( E ) = \operatorname* { m a x } \{ \sigma ( A ) | A \in \mathcal { S } _ { 1 } ( E ) \}$

(5)$\operatorname { L e t } \chi ( E )$denote the cardinality of$S _ { 2 } ( E )$

(6) The set$S _ { 2 } ( E )$has a lexicographical ordering by means of the given ordering in Γ itself.

Now choose the lexicographically smallest member B in$S _ { 2 } ( E )$and take the blowup with center$D ( B )$. This process will terminate after a finite number of repeated applications.

## 13. Cleaning in the case of$p > 0$

Recall the edge data of$\wp ( E ) \colon y = ( y _ { 1 } , \cdot \cdot \cdot , y _ { r } ) , g = ( g _ { 1 } , \cdot \cdot \cdot . g _ { r } )$with $g _ { i } = y _ { i } ^ { q _ { i } } + \epsilon _ { i }$and with$q _ { i } = p ^ { e _ { i } }$for$1 \leq i \leq r$where$e _ { i } \geq 0$

Lemma 13.1. . Let$R ( N ) = \rho ^ { N } ( R _ { \xi } )$with$N \gg 1$. Then$R _ { \xi }$is freely generated as$R ( N )$-module by

$$
y ^ {\alpha} g ^ {\beta} z ^ {\gamma} \text {with} \alpha \in \mathbb {Z} _ {0} ^ {r}, \beta \in \mathbb {Z} _ {0} ^ {r} a n d \gamma \in \mathbb {Z} _ {0} ^ {n - r}\tag{13.1}
$$

$$
w h e r e 0 \leq \alpha_ {k} <   q _ {k}, q _ {k} \beta_ {k} + \alpha_ {k} <   p ^ {N}, \forall k, \gamma_ {j} <   p ^ {N}, \forall j.
$$

Definition 13.1. Let$\hat { q } = ( q _ { 1 } , \cdots , q _ { r } )$. For an integer$c > 0$we define

$$
\mathcal {Q} _ {N} (c) ^ {\flat} = \sum_ {(1 3. 1) a n d \beta \cdot \hat {q} <   c} y ^ {\alpha} g ^ {\beta} z ^ {\gamma} R (N), a n d
$$

$$
\mathcal {Q} _ {N} (c) ^ {\sharp} = \sum_ {(1 3. 1) a n d \beta \cdot \hat {q} \geq c} y ^ {\alpha} g ^ {\beta} z ^ {\gamma} R (N) = R - \mathcal {Q} _ {N} (c) ^ {\flat}
$$

Pick and fix z such that$( y , z )$is a regular system of parameters of $R _ { \xi }$including those edge parameters y of$\wp ( E )$

Definition 13.2. Write h as$h ^ { \flat } + h ^ { \sharp }$with$h ^ { \flat } \in \mathcal { Q } _ { N } ( c ) ^ { \flat }$and$h ^ { \sharp } \in \mathcal { Q } _ { N } ( c ) ^ { \sharp }$ (which are both automatically “belonging$\mathrm { t o } ^ { \prime \prime } ~ R _ { \xi }$, not only to the completion$\hat { R } _ { \xi } \ )$. We then define$( g , N ( c ) )$-cleaning to be the map$h \mapsto h ^ { \flat }$ If$h ^ { \sharp } = \operatorname { 0 }$then h is said to be$( g , N ( c ) ) – c l e a n e d$

Definition 13.3. The$g _ { i }$is a homogeneous element of degree$q _ { i } = p ^ { e _ { i } }$ in$\wp ( E ) \subset g r _ { M } ( R )$for every i. For any homogeneous element h of degree c in$g r _ { M } ( R )$the$( g , N ( c ) )$-cleaning of h will be called$( g , N ) _ { z ^ { - } }$ cleaning or$( g , N )$-cleaning for short. For instance the$( g , N )$-cleaning of$\epsilon _ { i } = g _ { i } - y _ { i } ^ { q _ { i } }$will mean the$( g , N ( q _ { i } ) )$-cleaning.

Theorem 13.2. Any given edge generators g of ℘(E) with$g _ { i } = y _ { i } ^ { q _ { i } } + \epsilon _ { i }$ can be modified into another edge generators$g ^ { \dagger }$of$\wp ( E )$with$g _ { i } ^ { \dagger } \ =$ $y _ { i } ^ { q _ { i } } + \epsilon _ { i } ^ { \dagger }$(having the same$y )$in such a way that$\epsilon _ { i } ^ { \dagger }$is$( g ^ { \dagger } , N )$-cleaned for every$i , 1 \le i \le r$in the sense of$D e f . ( 1 3 . \mathcal { Q } )$

The modification of the theorem is obtained by repeating r-times cleanings of the kind of Def.(13.3). After the first cleaning the new$g _ { 1 }$ stays to be cleaned all the way to the end. After the second the same for the new$( g _ { 1 } , g _ { 2 } )$and so on.

Definition 13.4. We say an edge data$\{ y , q , g \}$is$( N ) _ { z }$<sub>z</sub>-cleaned if$\epsilon _ { i } ^ { \dagger } =$ $\epsilon _ { i }$for all i in the sense of Th.(13.2).

Theorem 13.3. Pick any integer N, say$> \sum _ { 1 \leq i \leq r } e _ { i }$. We are given edge data$\{ y , q , g \}$for$\wp ( E )$at$\xi$which are${ } ^ { \mathfrak { a } } ( N ) _ { z } ^ { - } { - } c l e a n e d ^ { , , }$. Let$\pi :$ $Z ^ { \prime } \to Z$with center$D \ni \xi$be permissible$f o r \ E$. Pick a closed point $\xi ^ { \prime } \in \pi ^ { - 1 } ( \xi ) \cap S i n g ( E ^ { \prime } )$such that$I n v _ { \xi ^ { \prime } } ( E ^ { \prime } ) = I n v _ { \xi } ( E )$Choose an exceptional parameter$\mathfrak { z }$at$\xi ^ { \prime }$such that$\mathfrak { z } \in \mathbb { K } [ z ]$, say${ \mathfrak { z } } \in z$. Then the transformed edge data

$$
\{\mathfrak {z} ^ {- 1} y _ {i} - c _ {i}, q _ {i}, \mathfrak {z} ^ {- q _ {i}} g _ {i}, 1 \leq i \leq r \}
$$

of$\wp ( E ^ { \prime } )$according to$T h . ( 1 1 . \mathcal { Q } )$with Lem.$( 1 1 . 7 )$is necessarily$( N ) _ { z ^ { \prime } } .$ cleaned where$z ^ { \prime }$is an appropriate transform$o f z b y \pi$. For instane$z ^ { \prime }$ is a regular system of f parameters of

$$
\operatorname{Spec} \left(\mathbb {K} \left[ \mathfrak {z} ^ {- 1} (z \setminus \mathfrak {z}), \mathfrak {z} \right]\right)
$$

at the projection of

In short the transforms of the “clean” edge data stay to be “clean” at the points where “Edge Invariants” are unchanged by the permissible blowup.

## 14. Γ-transversality

At a closed point$\xi \in Z$, we may be given a specific system of parameters of$R _ { \xi }$, say$w = ( w _ { 1 } , \cdot \cdot \cdot , w _ { r } )$. For instance w could be a system of edge parameters y of$\wp ( E )$. On the other hand we are given the NC-data Γ created by earlier blowups before the selection of$w .$

Definition 14.1. We say w is Γ-transversal at ξ if w can be extended to a regular system of parameters$\boldsymbol { x } = ( w , v )$of$R _ { \xi }$in such a way that v contains a generator of the ideal of every one of those members of Γ which go through the point$\xi .$

In the following theorem we make use of “induction hypothesis” on the dimensions of ambient spaces for the resolution of singularities applied to such ideals as$F ( W / \Gamma )$of Def.(12.3) and Th.(12.1).

Theorem 14.1. Given parameters w extendable to a regular system of$R _ { \xi }$, there exists a finite sequence of blowups$\pi : Z ^ { \prime } \to Z .$, globally successively permissible for E and Γ, such that the transform$w ^ { \prime }$of w is$\Gamma ^ { \prime } .$-transversal at every closed point$\xi ^ { \prime } \in \pi ^ { - 1 } ( \xi )$where$I n v _ { \xi ^ { \prime } } ( E ^ { \prime } ) =$ $I n v _ { \xi } ( E )$Here$\Gamma ^ { \prime }$is the transform of Γ by π and$E ^ { \prime }$is that of E. As for the choice of the transform w′ of w we make use of exceptional parameters and parameter transformations in the manner of Th.(11.2).

The locally defined ideal$F ( W / \Gamma )$can be extended globally to Z where we do not concern the loss of its property away from ξ with respect to Γ in the sense of Def.(12.3). The induction hypothesis is used inside the strict transforms of each component of the NC-data, one after another in the order of the history of creation. The point is the transversality becomes automatic with new exceptional divisor after a certain finite number of steps.

Corollary 14.2. The theorem is applicable to edge paramerters y of $\wp ( E )$. Therefore it is always enough to work with resolution problems under the assumption that the edge parameters y is Γ-transversal.

## 15. Γ-monomialization

Consider edge data of$\wp ( E )$of Def.(10.1) together with the edge decomposition of Th.(10.2), say

$$
E \sim \left(\cap_ {i = 1} ^ {r} E _ {i}\right) \cap F \text {with} E _ {i} = \left(g _ {i} \mathcal {O} _ {Z}, q _ {i}\right)
$$

where$g _ { i } = y _ { i } ^ { q _ { i } } + \epsilon _ { i }$and$\boldsymbol { F } = ( I , \boldsymbol { c } )$, o$\cdot d _ { \xi } ( I ) > c .$

Consider another ideal exponent$H = ( h , d )$in addition to$E .$. Using an inductive method on “edge invariants”, we can prove

Theorem 15.1. There exists a finite sequence of blowups, say$\hat { \pi } : \hat { Z } \to$ $Z$, globally permissible for E and H (and also for Γ as always), which has the following properties.

Letting E<sup>ˆ</sup> and H<sup>ˆ</sup> be the transforms of$E$and H by πˆ respectively, we can express$\hat { H } = ( h ^ { * } + h ^ { \dagger } , d )$in such a manner that at every closed point$\hat { \xi } \ o f \hat { \pi } ^ { - 1 } ( \xi ) \cap S i n g ( \hat { E } )$with in$v _ { \hat { \xi } } ( \hat { E } ) = i n v _ { \xi } ( E )$，

(1) the ideal$h ^ { \dagger }$is contained in

$$
\sum_{\substack{\beta \in \mathbb{Z}_{0}^{r}\text{with}\sum_{1\leq i\leq r}\beta_{i}q_{i}\geq d}}g^{\beta}R_{\xi}
$$

(2) the ideal h∗ of$H ^ { * } = ( h ^ { * } , d )$is locally generated by a Γ<sup>ˆ</sup>-monomial where$\hat { \Gamma }$denotes the transform of Γ by πˆ, and

(3) in the sense of infinitely near points we have the equalities

$$
\mathfrak {S} (\hat {E} \cap \hat {H}) _ {\hat {\xi}} = \mathfrak {S} (\hat {E} \cap H ^ {*}) _ {\hat {\xi}} = \widehat {\mathfrak {S} (E \cap H)} _ {\hat {\xi}}
$$

where$\widehat { E \cap H }$denotes the transform of$E \cap H$by$\hat { \pi }$.

A proof is basically by “denominator lift” Lem.(12.2) to which we apply the strategy Def.(10.2) of$^ { 6 6 } \mathrm { I n v } ^ { , 9 }$induction. But there is one important care-taking that is to spin away any summands of the type $h ^ { \dagger }$from the initial terms whenver these appears. (Or, we may us$( g , N ) .$ cleaning of the type Def.(13.3) in each step.)

Definition 15.1. The expression of$\hat { H }$by means$H ^ { * }$and$H ^ { \dagger }$as above will be called Γ-monomial<sup>ˆ</sup> E<sup>ˆ</sup>-division of$\hat { H }$at$\xi ^ { \prime }$.

Corollary 15.2. Let$\wp ( E ) ( a )$be the homogeneous part of degtee a of $\wp ( E )$for E as above and define the ideal exponent

$$
F (a) = (I (a), a) \text {   with   } I (a) = \{f \in \wp (E) (a) \mid o r d _ {\xi} (f) > a \}
$$

Pick and fix any integer$N > q _ { i } , \forall i$. We then claim there exists$\hat { \pi } :$ $\hat { Z }  Z$such that simultaneously for every$a ~ \leq ~ N$we have the$\hat { \Gamma } -$ monomial E<sup>ˆ</sup>-division of$\hat { E } ( a )$at$\xi ^ { \prime } { } _ { ; }$, say$E ( a ) ^ { * }$and$E ( a ) ^ { \dagger }$, in the sense of Def.(15.2) having the same property as$H ^ { * }$and H† of Th.(15.1),

## 16. /<sup>q</sup>-exponents

Recall that we had

(1) the edge parameters$y = ( y _ { 1 } , \cdots , y _ { r } )$

(2) the edge generators$g _ { i } ~ = ~ y _ { i } ^ { q _ { i } } + \epsilon _ { i }$where$q _ { i } = p ^ { e _ { i } }$and$o r d _ { \xi } ( \epsilon _ { i } ) > q _ { i }$ for$1 \leq i \leq r$where$0 \leq e _ { 1 } \leq \cdots \leq e _ { r }$

Let us observe that for each$i , 1 \leq i \leq r , y _ { i }$can be replaced by a unit multiple and accordingly$\epsilon _ { i }$by its$q _ { i } { \mathrm { - t h } }$powered unit multiple. Also that$y _ { i }$may also be replaced by$y _ { i } - \phi _ { i }$, usually with$\phi _ { i } \in M _ { \xi } ^ { 2 }$, and accordingly$\epsilon _ { i }$by$\epsilon _ { i } + \phi _ { i } ^ { q _ { i } }$

Definition 16.1. A /<sup>q</sup>-exponent G in Z is expressed as$\left( \mathbf { g } \parallel \mathbf { \Lambda } / \mathbf { \Lambda } ^ { q } \right)$locally at each point$\xi \in Z$with$\mathbf { g } \in { \mathcal { O } } _ { Z , \xi }$up to the following equivalence relation among the g. The equivalence relation is defined with reference to the given power$q = p ^ { e } , 0 \leq e \in \mathbb { Z }$, as follows:

$$
(\mathbf {g} (1) \parallel / ^ {q}) = (\mathbf {g} (2) \parallel / ^ {q}) \iff\tag{16.1}
$$

$$
\exists \text {   a   pair   of   elements   } (u, v) \in \mathcal {O} _ {Z, \xi} ^ {2}
$$

such that$\mathbf { g } ( 1 ) = u ^ { q } \mathbf { g } ( 2 ) - v ^ { q }$where u−<sup>1</sup> and$v ^ { q } \in { \mathcal { O } } _ { Z , \xi }$

Definition 16.2. For a reduced irreducible subscheme$D \subset Z$with its “generic” point ζ and for a given$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$of Def.(16.1), we define

$$
\begin{array}{rcl}ord_{D}(\mathcal{G}) & = & \max_{\substack{u,u^{-1}\in R_{\zeta}\\ v\in R_{\zeta}}}\big\{  ord_{\zeta}(u^{q}\mathbf{g} - v^{q})   \big\} \\ & = & \max_{v\in R_{\zeta}}\big\{  ord_{\zeta}(\mathbf{g} - v^{q})   \big\} \end{array}
$$

Remark 16.1. Unlike the case of ‘ideal exponents” we sometimes need to examine points$\eta \in Z$with$o r d _ { \eta } ( \mathcal { G } ) < q$. Refer to Def.(2.1), Def.(6.2), Eq.(6.2), Th.(7.1) and Def.(16.2).

In the following two examples we show two new phenomena that we must keep in mind in dealing with Zariski topology of /<sup>q</sup>-exponents.

## Example 16.1. (Generic-Down Pathology)

Let$Z ~ = ~ S p e c ( \mathbb { K } [ x , y ] )$Let$q \ : = \ : p ^ { e }$and$s ~ = ~ p ^ { c }$with integers$e \_ \mathrm { ~ > ~ }$ $c \geq 0$and$p = c h a r ( \mathbb { K } )$. Consider$D = S p e c ( \mathbb { K } [ x , y ] / ( x ) \mathbb { K } [ x , y ] )$and $\displaystyle ( \mathbf { g } \parallel / ^ { q } ) = ( x ^ { q } ( y - a ) ^ { s } \parallel / ^ { q } )$for every$a ^ { q / s } \in \mathbb { K }$. Thus we have

$o r d _ { D } ( \mathbf { g } \parallel / ^ { q } ) = q$while or$\cdot d _ { \eta } ( \mathbf { g } \parallel / ^ { q } ) = q + s$for all closed points η of D.

Observe the same phenomena for$\mathbf { g } = \ v g ( \ v x , \ v y ) ^ { q } \ v y ^ { s }$with any polynomial g and also for a finite sum of such.

## Example 16.2. (Generic-up Pathology)

Pick 5 variables$( x , y , z , w , t )$. Let$Z = S p e c ( \mathbb { K } [ x , y , z , w , t ] )$and$\eta =$ $( x , y , z , w ) \in S p e c ( Z )$. Let$\phi = x ^ { p } + t y ^ { p }$with$p = c h a r ( \mathbb { K } )$and let $\zeta = ( \phi , z , w ) \in S p e c ( Z )$which is a prime ideal. Let$\mathbf { g } = t z ^ { p } + w ^ { p + 1 }$ Then for$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( p \right) } \right)$have

(1) or$\cdot d _ { \zeta } ( \mathcal { G } ) = p + 1$while$o r d _ { \eta } ( \mathcal { G } ) = p$although η is a specialization of ζ. Thus special points can have smaller multiplicity than the generic point.

(2) Incidentally, if C denote the closure of the point${ \boldsymbol \sigma } = ( z , w )$then

$$
o r d _ {\sigma} (\mathcal {G}) = p <   o r d _ {\zeta} (\mathcal {G}) = p + 1\tag{16.2}
$$

$$
> o r d _ {\eta} (\mathcal {G}) = p <   o r d _ {\xi} (\mathcal {G}) = p + 1, \forall \xi \in C \cap Z _ {c l}
$$

in the ordering from generic to special.

Observe that the point η is a “singular point” of the closure of the point ζ and that the residue field$\kappa _ { \eta }$is not perfect. (cf. Lem(17.3), Th. (18.2), Th.(17.1) and Th.(18.1) of later sections.)

## 17. Basics of Zariski /<sup>q</sup>-topology

In spite of some “pathological” behavior of orders of$/ ^ { q } { } .$-exponents with respect to Zariski topology in$Z$we have many useful results.

Let$Z _ { c l }$denotes the set of all closed points of$Z$and the Zariski topology of$Z _ { c l }$is the one induced by that of$Z$. The specility of any closed point is its residue field is perfect.

Theorem 17.1. Consider any$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$of$D e f . ( 1 6 . 1 )$. For each integer$d > 0$, we define the set

$$
S i n g _ {c l} ^ {(d)} (\mathcal {G}) = \{\eta \in Z _ {c l} \mid o r d _ {\eta} (\mathcal {G}) \geq d \}\tag{17.1}
$$

We then assert that this set is closed in Zariski topology of$Z _ { c l }$.

Lemma 17.2. Let us pick any point$\eta \in S i n g ( \mathbf { g } \parallel / ^ { q } ) \cap Z _ { c l }$and also a regular system of parameters$x = ( x _ { 1 } , \cdots , x _ { n } )$of$R _ { \eta }$. Let$R ( q ) =$ $\rho ^ { e } ( R _ { \eta } )$with$q = p ^ { e }$so that$R _ { \eta }$is freely generated as R(q)-module by $\{ \ x ^ { \alpha } \mid \alpha \in \epsilon ^ { n } ( q ) \}$. Write$\begin{array} { r } { h = \sum _ { \alpha } h _ { \alpha } x ^ { \alpha } } \end{array}$with$h _ { \alpha } \in R ( q )$and$\alpha \in \epsilon ^ { n } ( q )$ We then claim

$$
\operatorname{ord} _ {\eta} (\mathbf {g} \parallel / ^ {q}) = \min \left\{\left. | \alpha | + \operatorname{ord} _ {\eta} \left(h _ {\alpha}\right) \mid \epsilon^ {n} (q) \ni \alpha \neq 0 \right\} \right.\tag{17.2}
$$

Moreover for each$0 \neq \alpha \in \epsilon ^ { n } ( q )$

$$
i f o r d _ {\eta} (h _ {\alpha} x ^ {\alpha}) \leq q\tag{17.3}
$$

( which can happen only if$h _ { \alpha } \in R ( q ) \backslash m a x ( R ( q ) ) \ : )$then

$$
o r d _ {\eta} (h _ {\alpha} x ^ {\alpha}) = | \alpha | = 1 + \max \{m \mid D i f f _ {Z, \eta} ^ {(m) *} (h _ {\alpha} x ^ {\alpha}) \subset M _ {\eta} \}
$$

and

$$
\begin{array}{r l} & i f o r d _ {\eta} (h _ {\alpha} x ^ {\alpha}) > q t h e n \\ & \quad o r d _ {\eta} (h _ {\alpha} x ^ {\alpha}) = o r d _ {\eta} (h _ {\alpha}) + | \alpha | = \\ & \quad 1 + | \alpha | + \max \Bigl \{\mu \mid \bigl (D i f f _ {Z, \eta} ^ {(\mu)} h _ {\alpha} \bigr) \subset M _ {\eta} \Bigr \} = \\ & \quad 1 + \max \Bigl \{\mu \mid \bigl (D i f f _ {Z, \eta} ^ {(\mu)} \partial^ {(\alpha)} (h _ {\alpha} x ^ {\alpha}) \bigr) \subset M _ {\eta} \Bigr \} = \\ & 1 + \max \Bigl \{m \mid \sum_ {1 \leq \mu <   q} \Bigl (D i f f _ {Z, \eta} ^ {(m - \mu)} D i f f _ {Z, \eta} ^ {(\mu) *} (h _ {\alpha} x ^ {\alpha}) \Bigr) \subset M _ {\eta} \Bigr \}. \end{array} \tag {4}\tag{17.4}
$$

Lemma 17.3. Let us pick a pair of points η and$\zeta$in Z such that η is a smooth point of the closure D of ζ in Z. Then we have

$$
o r d _ {\eta} (\mathcal {G}) \geq o r d _ {\zeta} (\mathcal {G}).\tag{17.5}
$$

To be explicit, let us choose a regular system of parameters$\boldsymbol { u } = ( u , v )$ of$R _ { \eta }$such that u$R _ { \eta }$is the ideal of D at η. Let${ \hat { R } } _ { \eta } = K [ [ u ] ]$denote the

$M _ { \eta } { - } a d i c$completion of$R _ { \eta }$where K is a coeficient field containing K. Let us write

$$
\mathbf {g} = \sum_ {a b} d _ {a b} u ^ {a} v ^ {b} \text { with } d _ {a b} \in K\tag{17.6}
$$

Then we have

$$
\operatorname{ord} _ {\eta} (\mathcal {G}) = \min \left\{\left| a \right| + | b | \mid d _ {a b} u ^ {a} v ^ {b} \notin \rho^ {e} (K [ [ u ] ]) \right\}\tag{17.7}
$$

and

$$
\operatorname{ord} _ {\zeta} (\mathcal {G}) = \min \left\{\left| a \right| \mid \exists b, d _ {a b} u ^ {a} v ^ {b} \notin \rho^ {e} (K [ [ u ] ]) \right\}\tag{17.8}
$$

Theorem 17.4. Let A be a positive integer. If or$d _ { \xi } ( \mathbf { g } \parallel / ^ { q } ) = A q$for a closed point$\xi \in Z$, then$\{ \eta \in Z \mid o r d _ { \eta } ( \mathbf { g } \parallel / ^ { q } ) = A q \}$is closed in$Z$ within a neighborhood of$\xi \in Z$. It should be noted that the closedness in$Z$is much stronger than the same in$Z _ { c l }$

Theorem 17.5. Let$D \subset Z$be an irreducible subscheme and let$A$ be a positive integer. If$o r d _ { \eta } ( \mathbf { g } \parallel / ^ { q } ) \geq A q$for all$\eta \in D \cap Z _ { c l }$then $o r d _ { \zeta } ( \mathbf { g } \parallel / ^ { q } ) \geq A q$for the generic point$\zeta \in D$

$$
\operatorname{ord} _ {\xi} (\mathbf {g} \parallel / ^ {q}) \geq \operatorname{ord} _ {\zeta} (\mathbf {g} \parallel / ^ {q}).
$$

Lemma 17.6.$I f \xi \in Z _ { c l }$and is contained in the closure of$\zeta \in Z$then we have

## 18. /<sup>q</sup>-permissibility and /<sup>q</sup>-transform

Definition 18.1. The singular locus$S i n g ( \mathbf { g } \parallel / ^ { q } )$of a /<sup>q</sup>-exponent is the set$\left\{ \eta \in Z \mid o r d _ { \eta } ( \mathbf { g } \parallel / ^ { q } ) \geq q \right\}$

Theorem 18.1. The$S i n g ( \mathbf { g } \parallel / ^ { q } )$is closed in the Zariski topology of Z. This closedness is stronger than the closedness within$Z _ { c l }$in the sense of$T h . ( 1 7 . 1 )$

Theorem 18.2. If D is a smooth irreducible subscheme of$Z$then $o r d _ { \eta } ( \mathbf { g } \parallel / ^ { q } ) \geq o r d _ { \zeta } ( \mathbf { g } \parallel / ^ { q } )$for every$\eta \in D$, where$\zeta$is the generic point of D.

Definition 18.2. Let$\pi : Z ^ { \prime } \longrightarrow Z$be a blowup with center D. We say that π (and also$D )$is called permissible for a /<sup>q</sup>-exponent$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$ if D is smooth irreducible and contained in$S i n g ( \mathcal { G } )$in the sense of Def.(18.1). Here and as always, the permissibility is required with respect to the given NC-system$\Gamma$in the sense of Def.(12.1).

Note that$D \subset S i n g ( \mathcal { G } )$means that every point of D (including the generic point of$D )$is in$S i n g ( \mathcal { G } )$.

Here we add one more permissibility condition as follows.

Definition 18.3. We say that$\pi$with$D$of Def.(18.2) is strongly permissible at a closed point$\xi \in D$if furthermore$o r d _ { \xi } ( \mathcal { G } ) = o r d _ { \zeta } ( \mathcal { G } )$with the generic point$\zeta \in D$

This condition is strictly stronger than that of Def.(18.2) in general because of the possibility of generic-down center.

Definition 18.4. The transform$\mathcal { G } ^ { \prime }$of$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$by a permissible π of Def.(18.2) is defined as follows:

(1) For each closed point$\xi ^ { \prime } \in Z ^ { \prime }$with$\pi ( \xi ^ { \prime } ) \in D$we let I be the ideal of D at ξ and pick any$v \in I$such that$I R _ { \xi ^ { \prime } } = v R _ { \xi ^ { \prime } }$ξ′

(2) and then locally at$\xi ^ { \prime }$we define the transform$\mathcal { G } ^ { \prime }$to be = $\left( v ^ { - q } \mathbf { g } \parallel / \mathbf { \zeta } ^ { q } \right)$

(3) We then see that above definition is independent of the choice of v due to the equivalence of Eq.(16.1) in Def.(16.1).

(4) For this reason the above definition of$\mathcal { G } ^ { \prime }$is globally well defined for all$\xi ^ { \prime } \in \pi ^ { - 1 } ( D )$. For points of$Z ^ { \prime } - \pi ^ { - 1 } ( D )$the above definition is naturally extended through the isomorphism of$\pi$ restricted to$Z ^ { \prime } - \pi ^ { - 1 } ( D )$

The permissibility can be extended for every LSB of Def.(6.1). Following Def.(6.2) words by words, we can define

Definition 18.5.

$\begin{array} { r } { \mathfrak { S } ( \mathcal { G } ) \ = \ \bigcup _ { t } \left\{ \begin{array} { r l r l } \end{array} \right. } \end{array}$LSBs over$Z [ t ]$permissible for$\mathcal { G } [ t ] = \left( \mathbf { g } [ t ] \parallel / ^ { q } \right) \left. \right\}$

We then say that${ } ^ { 6 6 } \mathcal { G } _ { 2 }$more singular than${ \mathcal G } _ { 1 } ^ { \prime \prime } \mathrm { ~ i f ~ } { \mathfrak F } ( { \mathcal G } _ { 2 } ) \supset { \mathfrak E } ( { \mathcal G } )$, and we define equivalence by$\mathcal { G } _ { 1 } \sim \mathcal { G } _ { 2 } \Leftrightarrow \mathfrak { S } ( \mathcal { G } _ { 1 } ) = \mathfrak { S } ( \mathcal { G } _ { 2 } )$. Then$\mathcal { G } \sim \mathcal { G } _ { 1 } \cap \mathcal { G } _ { 2 }$ will mean${ \mathfrak { S } } ( { \mathcal { G } } ) = { \mathfrak { S } } ( { \mathcal { G } } _ { 1 } ) \cap { \mathfrak { S } } ( { \mathcal { G } } _ { 2 } )$

Moreover the notion of equivalence can be extended to the mixed cases of ideal exponents and$/ ^ { q } .$-exponents as follows.

Definition 18.6. For a finite number of ideal exponents$E _ { i } = \left( J _ { i } , b _ { i } \right)$ with$1 \leq i \leq c$and$/ ^ { q } { - }$-exponents$\mathcal { G } _ { j } = \left( \mathbf { g } _ { j } \parallel / ^ { q _ { j } } \right)$with$1 \leq j \leq d$2

$$
G \sim \left(\cap_ {1 \leq i \leq c} E _ {i}\right) \bigcap \left(\cap_ {1 \leq j \leq d} \mathcal {G} _ {j}\right) \Longleftrightarrow\tag{18.1}
$$

$$
\mathfrak {S} (G) = \left(\cap_ {1 \leq i \leq c} \mathfrak {S} (E _ {i})\right) \bigcap \left(\cap_ {1 \leq j \leq d} \mathfrak {S} (\mathcal {G} _ {j})\right)
$$

In particular$S i n g ( G ) = \left( \cap _ { 1 \leq i \leq c } S i n g ( E _ { i } ) \right) \bigcap \left( \cap _ { 1 \leq j \leq d } S i n g ( \mathcal { G } _ { j } ) \right)$

Theorem 18.3. ( Ambient /<sup>q</sup>-Reduction Theorem ) Given a /<sup>q</sup>-exponent $\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$in$Z$, we let

$$
I ^ {+} = \sum_ {j = 1} ^ {q - 1} \left(D i f f _ {Z} ^ {(j) *} \mathbf {g}\right) ^ {\frac {b ^ {+}}{b - j}} w i t h b ^ {+} = (q - 1)!
$$

For any smooth subscheme$W \subset Z$, we let$F ^ { + } = ( I ^ { + } \mathcal { O } _ { W } , b ^ { + } )$which is an ideal exponent in W. We let$\mathcal { F } = ( \mathbf { g } \mathcal { O } _ { W } \lVert \mathbf { \rho } / ^ { q } )$which is a /<sup>q</sup>-exponent in W. Then$F ^ { + } \cap \mathcal { F }$is an ambient reduction of G from Z to W in the following sense (definition):

Pick any t and any one LSB over$Z [ t ]$such that all of its centers are in the strict transforms$o f W [ t ]$. Then the $L S B$belongs to${ \mathfrak { S } } ( { \mathcal { G } } )$if and only if it induces an$L S B$ in$W [ t ]$which belongs to${ \mathfrak { S } } ( F ^ { + } \cap { \mathcal { F } } )$

## 19. /<sup>q</sup>-divisorial factors

Theorem 19.1. Pick a regular system of parameters${ \boldsymbol { x } } = ( z , w )$with $z = ( z _ { 1 } , \cdots , z _ { s } )$at a closed point$\xi \in Z$such that those components $\Gamma _ { i } ~ o f \Gamma$passing through$\xi$are the hypersurfaces defined by the ideals $( z _ { i } ) R _ { \xi } , 1 \leq i \leq s$. Then every /<sup>q</sup>-exponent$\mathcal { G } \neq \left( 0 \| / { } ^ { q } \right)$is represented as$\left( z ^ { \hat { \alpha } } f \parallel / { } ^ { q } \right)$with$f \in R _ { \xi }$where$\hat { \alpha } = ( \hat { \alpha } _ { 1 } , \cdots , \hat { \alpha } _ { r } )$with$\hat { \alpha } _ { i } = o r d _ { \zeta _ { i } } ( \mathcal { G } )$ for all i where$\zeta _ { i }$is the generic point of$\Gamma _ { i }$.

Remark 19.1. The monomial$z ^ { \hat { \alpha } }$of Th.(19.1) is unique up to a unit multiple in$R _ { \xi }$and hence the ideal${ \mathcal P } _ { \xi } = z ^ { \hat { \alpha } } R _ { \xi }$is locally uniquely determined by$\check { \mathcal { G } }$at$\xi .$. Moreover this ideal$\mathcal { P } _ { \xi }$is the stalk at$\xi$of a global coherent ideal sheaf P within the domain of definition of$\mathcal { G }$.

Definition 19.1. The above monomial$z ^ { \hat { \alpha } }$of Th.(19.1) will be called Γ-maximal divisor of$\mathcal { G }$at$\xi .$. Write$\hat { \alpha } = q \beta + \gamma$in such a way that $0 \leq \gamma _ { i } < q , \forall i$, and call$z ^ { q \beta }$the qΓ-factor and$z ^ { \gamma }$the qΓ-cofactor of$\mathcal { G }$ at$\xi .$The global ideal$\mathcal { P }$will be called Γ-maximal divisor of$\mathcal { G }$, denoted by${ \mathcal { P } } ( { \mathcal { G } } )$. Moreover we have a coherent ideal B with stalks$B _ { \xi } = z ^ { \beta } R _ { \xi }$ and its q-th power$B ^ { q }$will be called the qΓ-factor of$\mathcal { G }$. The ideal sheaf $B ^ { - q } { \mathcal { P } }$will be called the$q \Gamma { - } c o f a c t o r$of$\mathcal { G }$

Definition 19.2. The qΓ-cofactor$z ^ { \gamma }$will be often written as$v ^ { \gamma }$with the subsystem$v \subset z$consisting of exactly those$z _ { j }$having$\gamma _ { j } > 0$

Definition 19.3. Let us write$\mathcal { G } \ = \ ( \mathcal { P } f \| / { \overset { q } { \operatorname { \rho } } } )$with the Γ-maximal divisor$\mathcal { P }$, which is locally$\mathcal { P } _ { \xi } = z ^ { \hat { \alpha } }$of Th.(19.1) at a closed point$\xi .$. Such f will be called residue of$\mathcal { G }$at$\xi .$. We define

(19.1)

$r e s o r d _ { \xi } ( \mathcal { G } ) ~ = ~ m a x \{ o r d _ { \xi } ( f ) \mid$all residues f of$\mathcal { G }$at$\xi \}$

When a residue f satisfies the equality resor$d _ { \xi } ( \mathcal { G } ) = o r d _ { \xi } ( f )$we call$f$ a Γ-residual factor or residual factor of$\mathcal { G }$at$\xi$.

Definition 19.4. We define

$$
\check {\mathcal {G}} = \left(\mathcal {P} ^ {- 1} \mathbf {g} \right\rVert / ^ {q})\tag{19.2}
$$

$$
\text { with } \Gamma \text {-maximal} \mathcal {P} \text { of } \mathcal {G} = (\mathbf {g} \| / ^ {q}),
$$

where g is chosen to be divisible by a generator$z ^ { q \mathbf { b } + \gamma }$of$\mathcal { P }$locally at $\xi$. (cf. Th.(19.1) and Def.(19.1).) We will call$\check { \mathcal { G } }$the checked associate of$\mathcal { G }$.

## 20. Standard abc-expression of$/ ^ { q } -$-exponent

Assume that we are given a$/ ^ { q } { } .$-expnent in$Z _ { i }$say$\mathcal { G }$. Then we need to choose specific parameters and detailed expressions of$\mathcal { G }$in terms of its important components. There are certain common features in the pattern of their expressions. Therefore we want to set their versatile standard form which we can later refer to.

Remark 20.1. Locally at$\xi$we choose a system of parameters z which consists of the ones defining those components$\Gamma _ { j } \subset Z$of the Γ which are passing through the point$\xi \in Z$. We then extend$z$to a regular system of parameters$x = \left( z , \omega \right)$of$R _ { \xi }$in which the choice of$\omega$may be free or may be contingent to the specifics of the given situation. In particular when we are dealing with a specific blowup π with center$D$ then we may or may not require that the ideal$I ( D , Z ) _ { \xi }$be generated by a subsystem u of$x .$. However as for the choice of$z$we should recall the universal permissibility of$\pi$with the$N C .$-data$\Gamma$so that the choice of$z$is not afected by the choice of permissible blowup so long as we focus our investigation to local problems at the given point$\xi \in Z$ Moreover, depending upon$\mathcal { G }$locally at$\xi$we choose a subsystem v of z and write$z = ( v , w )$as is done in the definition below.

Throughout this paper we will be using the following standard form of expression of any given$/ ^ { q } .$-exponent$\mathcal { G }$, which we will call abc-expression of$\mathcal { G }$at the given point$\xi .$

Definition 20.1. We define a standard abc-expression of a$/ ^ { q } .$-exponent $\mathcal { G }$at a given closed point$\xi \in S i n g ( \mathcal { G } )$as follows:

$$
\begin{array}{r} \mathcal {G} = (\mathbf {g} \| / ^ {q}) \\ w i t h \mathbf {g} = z ^ {\mathbf {a}} g = z ^ {q \mathbf {b}} v ^ {\mathbf {c}} g \end{array}\tag{20.1}
$$

where$z ^ { \mathbf { a } }$is the maximal Γ-factor of$\mathcal { G } , z ^ { q \mathbf { b } }$is the maximal$q \Gamma -$factor and $v ^ { \mathbf { c } }$is the Γ-cofactor with$0 < { \bf c } _ { j } < q$for all$j$in the sense of Def.$( 1 9 . 1 )$ Moreover$g$is a residual factor so that$o r d _ { \xi } ( g )$is equal to resor$d _ { \xi } ( \mathcal G )$. Here the parameters$x = \left( z , \omega \right)$is chosen in accord with Rem.(20.1), while the partition$z = ( v , w )$is determined by the equality$z ^ { \mathbf { a } } = z ^ { q \mathbf { b } } v ^ { \mathbf { c } }$

$\mathrm { A s }$for those important numbers a, b and$\mathbf { c } ,$they will be named diferently in accord with the specific needs. When we are dealing with many diferent$/ ^ { q } .$-exponents simultaneously we need to choose diferent naming for the numbers a, b and c.

## 21. cotangent p-flags

We introduce the notion of “cotangent$\scriptstyle { p \mathrm { - } \mathrm { f l a g s } ^ { \prime } }$for an ideal$I \subset R _ { \xi }$2 especially a principal ideal$I = g R _ { \xi }$with$g \in M _ { \xi }$. The notion is of local nature at a given closed point$\xi \in Z$and is determined by the initial of the ideal I at ξ. The initial means the$\kappa _ { \xi } .$-module$\left( I + \stackrel { \smile } { M } _ { \xi } ^ { d + 1 } \right) / M _ { \xi } ^ { d + 1 }$ with$d = o r d _ { \xi } ( I )$. Throughout this section the residue field$\kappa _ { \xi }$will be assumed to be perfect.

Remark 21.1. The cotangent$p { - } f a g s$of I at$\xi$are written as a system of$\kappa _ { \xi } .$-submodules of$M _ { \xi } / M _ { \xi } ^ { 2 } \subset g r _ { \xi } ( R _ { \xi } )$as follows:

$$
\left\{L _ {\xi} (I, a), p ^ {e _ {a}}, 1 \leq a \leq l \right\} \text {   with   } e _ {a} \in \mathbb {Z} _ {0}\tag{21.1}
$$

which we may write$L _ { \xi } ( I , a ) = L ( I , a ) = L ( a )$for short.

They are characterized by the following properties:

$$
(0) = L (0) \subsetneq L (I, 1) \subsetneq \dots \subsetneq L (I, l) \subset L = M _ {\xi} / M _ {\xi} ^ {2}\tag{21.2}
$$

subject to the following conditions.

(1) We have$1 \leq p ^ { e _ { 1 } } < \cdots < p ^ { e _ { l } }$where$p ^ { e _ { l } } \leq d = o r d _ { \xi } ( I )$

(2) If$g \in I$and$\partial \in D i f f _ { R _ { \xi } / \mathbb { K } } ^ { d - p ^ { \epsilon } }$have the following property

$$
\operatorname{ord} _ {\xi} (\partial (g)) = p ^ {\epsilon} \text { and } \bar {w} ^ {p ^ {\epsilon}} \in i n _ {\xi} (\partial (g)) + \kappa_ {\xi} [ L (b) ]\tag{21.3}
$$

where$e _ { b } < \epsilon$and$0 \neq \bar { w } \in M _ { \xi } / M _ { \xi } ^ { 2 }$, then there exists an index a such that$e _ { a } \leq \epsilon$and$\bar { w } \in L ( a )$

(3) for each$a , 1 \leq a \leq l$, the κ -module$L ( a ) / L ( a - 1 )$is generated by the images of those$\bar { w } \in \bar { L } ( a ) \subset M _ { \xi } / M _ { \xi } ^ { 2 }$for which there exist $\partial \in \mathsf { \Gamma } D i f f _ { R _ { \xi } / \mathbb { K } } ^ { ( d - p ^ { e _ { a } } ) }$and$g \in I$satisfying Eq.(21.3) with$\epsilon = e _ { a }$so that$b = a - 1$

The cotangent$p \mathrm { - } f a g$of an element$g \in M _ { \xi }$will mean that of the principal ideal$I = g R _ { \xi }$. For any$f \in M _ { \xi }$such that$o r d _ { \xi } ( g - f ) > d =$ $o r d _ { \xi } ( g ) , f$and g have the same cotangent$p { - } f a g s$

Remark 21.2. Here is a list of elementary properties of the cotangent p-flag of an ideal I at$\xi .$We only consider the nontrivial case with $M _ { \xi } \supset I \ne 0$with$o r d _ { \xi } ( I ) = d > 0$

(1) Let ϵ be the smallest non-negative integer such that

$$
\left(D i f f _ {R _ {\xi} / \mathbb {K}} ^ {(d - p ^ {\epsilon})} I + M _ {\xi} ^ {p ^ {\epsilon} + 1}\right) / M _ {\xi} ^ {p ^ {\epsilon} + 1} \neq 0.\tag{21.4}
$$

We then have$\epsilon = e _ { 1 }$and the module Eq.(21.4) is equal to $\rho ^ { e _ { 1 } } ( L ( 1 ) )$. In this case the condition Eq.(21.3) can be replaced by a “stronger” one in which we require

$$
\exists g \in I a n d \exists \partial \in D i f f _ {R _ {\xi} / \mathbb {K}} ^ {d - p ^ {\epsilon}}\tag{21.5}
$$

such that$\bar { w } ^ { p ^ { \epsilon } } = i n _ { \xi } ( \partial ( g ) )$and$o r d _ { \xi } ( \partial ( g ) ) = p ^ { \epsilon }$

Here$\epsilon = e _ { 1 }$. But in the cases of$a > 1$this condition can be too strong to produce the whole$L ( I , a ) / L ( I , a - 1 )$

Example 21.1. Consider$I = g R _ { \xi }$with$\begin{array} { r } { g = x _ { p + 1 } ^ { p } + \prod _ { 1 \leq i \leq p } x _ { i } } \end{array}$in which$\begin{array} { r } { L ( I , 1 ) = \sum _ { 1 \leq i \leq p } \kappa _ { \xi } \bar { x } _ { i } } \end{array}$and$L ( I , 2 ) = L ( I , 1 ) \bar { + } \overrightarrow { \kappa _ { \xi } } \bar { x } _ { p + 1 }$ Note that$\bar { w } = \bar { x } _ { p + 1 }$does not satisfy$\mathrm { E q . } ( 2 1 . 5 ) . \ ( \bar { x } _ { i } = i n _ { \xi } ( x _ { i } ) . )$

(2) If$d = p ^ { e _ { l } }$with the maximal index l we then have

$$
\begin{array}{c} r a n k _ {\kappa_ {\xi}} \big (L (I, l) / L (I, l - 1) \big) \\ = r a n k _ {\kappa_ {\xi}} \big (\bar {I} + \kappa_ {\xi} [ L (I, l - 1) ] / \kappa_ {\xi} [ L (I, l - 1) ] \big). \end{array}\tag{21.6}
$$

In particular when$I = g R _ { \xi }$this rank is equal to 1 thanks to the perfectness of$\kappa _ { \xi }$

Definition 21.1. We say that$g ^ { \prime }$is cotangentially subordinate to$g$if every member$L ( g ^ { \prime } , b )$of the p-flags of$g ^ { \prime }$at$\xi$is contained in some $L ( g , a )$of the p-flags of g at ξ with$e _ { a } \leq e _ { b }$

For instance, pick$g \in I$and$\partial \in D i f f _ { R _ { \xi } / \mathbb { K } } ^ { ( d - \mu ) }$such that or$d _ { \xi } ( \partial g ) = \mu$ Then$\partial g$is cotangentially subordinate to g.

Theorem 21.1. Let l be the last index of$E q . ( 2 1 . 1 )$. We then have

(21.7)$\bar { I } \subset \kappa _ { \xi } [ L ( I , l ) ]$where$\bar { I } = \left( I + M _ { \xi } ^ { d + 1 } \right) / M _ { \xi } ^ { d + 1 }$

Moreover$L ( I , l )$is the smallest having this inclusion property.

The theorem is proven by using the following lemma.

Lemma 21.2. Let$\{ L _ { \xi } ( I , a ) , p ^ { e _ { a } } , 1 \leq a \leq l \}$be the cotangent p-flags of$E q . ( 2 1 . 1 )$. Then for each a we have

$$
\begin{array}{c} o r d _ {\xi} \big (D i f f _ {R _ {\xi} / \mathbb {K}} ^ {(d - p ^ {e _ {a}})} I \big) = p ^ {e _ {a}} \\ a n d \end{array}\tag{21.8}
$$

$$
\begin{array}{r l} & i n _ {\xi} \big (D i f f _ {R _ {\xi} / \mathbb {K}} ^ {(d - p ^ {e _ {a}})} I \big) + \kappa_ {\xi} [ L (I, a - 1) ] \\ & \quad = \kappa_ {\xi} L (I, a) + \kappa_ {\xi} [ L (I, a - 1) ] \end{array}
$$

Recall that$i n _ { \xi } ( J ) = ( J + M _ { \xi } ^ { \nu + 1 } ) / M _ { \xi } ^ { \nu + 1 }$with$\nu = o r d _ { \xi } ( J )$as always.

Definition 21.2. A cotangential base of exponent$e _ { a }$of I at$\xi$is by definition a system$\bar { w } ( a )$of elements$\bar { w } ( a ) _ { j } \in M _ { \xi } / M _ { \xi } ^ { 2 }$, which induces a free base of the κ<sub>ξ</sub>-module$L ( I , a ) / L ( I , a - 1 )$. A regular system of parameters$x$of$R _ { \xi }$will be said to be cotangential of I at ξ if in<sub>ξ</sub>x contains a cotangential base of I of exponent$\scriptstyle { e _ { a } }$for all$a , 1 \leq a \leq l$

Definition 21.3. We have$q = p ^ { e }$and$q \leq d = o r d _ { \xi } ( I )$. Then define (21.9)$\ell _ { \xi , q } ( I ) = m a x \{ a | \exists e _ { a } < e \}$and$\ell _ { \xi , p ^ { + } } ( I ) = m a x \{ a l l a \} = \ell$ with reference to the$p { \cdot }$-flags Eq.(21.1).

(1)$\ell _ { \xi , q } ( I )$may be written as$\ell _ { q } ( I )$or$\ell ( I )$for short.

(2)$\ell _ { \xi , p ^ { + } } ( I )$may be written as$\ell _ { p ^ { + } } ( I )$or$\ell _ { \xi ^ { + } } ( I )$or$\ell _ { + } ( I )$

(3) Keep in mind that we always have$p ^ { e _ { a } } \leq d$

(4) And then define

$$
L _ {q - m a x} (I) = L (I, \ell_ {q}) w i t h \ell_ {q} = \ell_ {\xi , q} (I)\tag{21.10}
$$

$$
L _ {[ p ^ {+} ] - m a x} (I) = L (I, \ell_ {p ^ {+}}) w i t h \ell_ {p ^ {+}} = \ell_ {\xi , p ^ {+}} (I)
$$

## 22. p-flags of /<sup>q</sup>-exponents

We will refer to the notation of$/ ^ { q } { \mathrm { - e x p o n e n t ~ } } \mathcal { G }$and its abc-expression $\left( z ^ { \mathbf { a } } g \parallel / \mathbf { \mathit { q } } \right)$with$z ^ { \mathbf { a } } = z ^ { q \mathbf { b } } v ^ { \gamma }$in the sense of Def.(20.1), with qΓ-cofactor $v ^ { \gamma }$and residual factor$g$with reference to Rem.(19.1), Def.(19.1) and Def.(19.3). As for the choice of local parameters we refer to Rem.(20.1).

$$
x = (z, \omega) w i t h z = (v, w) a n d v = \left(v _ {1}, \dots , v _ {t}\right).\tag{22.1}
$$

For the sake of notational simplicity, we sometimes write$z ^ { \gamma }$for$v ^ { \gamma }$ meaning that$\gamma$is extended from$\mathbb { Z } _ { 0 } ^ { t }$to$\mathbb { Z } _ { 0 } ^ { s }$by placing zeros for those components corrresponding to$w .$.

Remark 22.1. Given$\mathcal { G } = ( z ^ { q \mathbf { b } } v ^ { \gamma } g \lVert / ^ { q } )$we examine the following two cases of applications of the$p { - } f l a g s .$(Refer to Eq.(21.1) and$\operatorname { E q . } ( 2 1 . 2 ) .$

(1) The case of the ideal$I = g R _ { \xi }$with a residual factor$g$of$\mathcal { G }$.

(2) The case of$I = v ^ { \gamma } R _ { \xi }$with the qΓ-cofactor$v ^ { \gamma }$of$\mathcal { G }$.

Their p-flags have diferent characters and must be treated diferently. The character concerns with the following uniquness question. Note that the case (2) is up to a unit multiple onto$v ^ { \gamma }$, while the case (1) is up to an addition of$\phi ^ { q } v ^ { \gamma * }$to$g$with$\phi \in R _ { \xi }$. Here and later as well, γ∗ denotes the q-supplement of$v ^ { \gamma }$in the following sense.

Definition 22.1. We have$\mathbf { a } = q \mathbf { b } + \gamma \in \mathbb { Z } _ { 0 } ^ { s }$with$0 \leq \gamma _ { i } < q , \forall i$. Then the q-supplement of$\gamma$is the unique element$\gamma ^ { \ast } \in \mathbb { Z } _ { 0 } ^ { s }$such that

$$
\gamma_ {j} ^ {*} = \left\{ \begin{array}{l l} q - \gamma_ {j} & \text {   if   } \gamma_ {j} \neq 0 \\ 0 & \text {   if   otherwise   } \end{array} \right. \quad \text {   where   } 1 \leq j \leq s.
$$

In other words$\alpha + \gamma ^ { * } \equiv 0$mod$( q )$and$0 \leq \gamma _ { j } ^ { * } < q$for all$i , 1 \le j \le s$

Note that having$\gamma \mathrm { ~ a s ~ } \in \mathrm { ~ } \mathbb { Z } _ { 0 } ^ { t }$we have$0 ~ < ~ \gamma _ { i } ~ < ~ q , \forall i$, and hence $0 < \gamma _ { i } ^ { * } < q \forall i$. Here t is the length of v while s is that of$z .$In the manner of Def.(22.2)$\gamma ^ { * }$is q-supplement of$\gamma$as well that of a.

Recall ℓ(I) of Eq.(21.9) and$L _ { q - m a x } ( I ) = L ( I , \ell ( I ) )$of Def.(21.3). We will use diferent symbols for the residual and cofactor cases.

$$
L (g, a) ^ {r e s i} \text { for } L (g, a)\tag{22.2}
$$

$$
a n d L _ {q - m a x} (g) ^ {r e s i} f o r L _ {q - m a x} (f)
$$

with understanding that$g$is a residual factor of the given$\mathcal { G }$.

$$
L (v ^ {\gamma}, a) ^ {c o f a} \text {   for   } L (v ^ {\gamma}, a)\tag{22.3}
$$

$$
a n d L _ {q - m a x} (v ^ {\gamma}) ^ {c o f a} f o r L _ {q - m a x} (v ^ {\gamma})
$$

with understanding that$v ^ { \gamma }$is a$q \Gamma .$-cofactor of$\mathcal { G }$.

Remark 22.2. In the cofactor case the two modules$L ( v ^ { \gamma } , a ) ^ { c o f a } , \forall a$ and$L _ { q - m a x } ( v ^ { \gamma } ) ^ { c o f a }$are independent of the choice of qΓ-cofactors$v ^ { \gamma }$ Therefore we will rewrite

$$
\begin{array}{c} L (\mathcal {G}, a) ^ {c o f a} \text {to be} L (v ^ {\gamma}, a) ^ {c o f a} \\ \text {and} L _ {q - m a x} (\mathcal {G}) ^ {c o f a} \text {to be} L _ {q - m a x} (v ^ {\gamma}) ^ {c o f a} \end{array}\tag{22.4}
$$

However in the residual case$L ( g , a ) ^ { r e s i } , \forall a .$, and$L _ { q - m a x } ( g ) ^ { r e s i }$depend on the choice of$g$.

Remark 22.3. Consider the following condition on$j$for each$a .$

$$
e (j) = \max \left\{e \in \mathbb {Z} _ {0} \mid p ^ {e} \text {divides} \gamma_ {j} \right\} \leq e _ {a}.\tag{22.5}
$$

where$1 \le j \le t$and$1 \leq a \leq l$. Since we have$0 < \gamma _ { j } < q$for all$j ,$ the κ -module$L ( v ^ { \gamma } , a )$is generated by those$i n _ { \xi } ( v _ { j } )$with$j$satisfying $\mathrm { E q . ( 2 2 . 5 ) }$. Note that if$\gamma$is replaced by the$\gamma ^ { * }$according to Def.(22.1) all the results remain unchanged because of$\gamma _ { j } ^ { \ast } = q - \gamma _ { j } , \forall j$

Lemma 22.1. For every index$a , 1 \leq a \leq l , L ( \mathcal G , a ) ^ { c o f a }$is uniquely determined$b y \mathcal { G }$and$L _ { q - m a x } ( \mathcal { G } ) ^ { c o f a }$is generated by$\{ i n _ { \xi } ( v _ { j } ) | 1 \le j \le t \}$ where$v = \left( v _ { 1 } , \cdots , v _ { t } \right)$

About the residual factors we should refer to Eq.(19.1) of (19.3).

Lemma 22.2. Pick any two presentations

$$
\mathcal {G} = \left(z ^ {q \mathbf {b}} v ^ {\gamma} f \| / ^ {q}\right) = \left(z ^ {q \mathbf {b}} v ^ {\gamma} g \| / ^ {q}\right)
$$

Then there exists$b \in R _ { \xi }$such that$f - g = b ^ { q } v ^ { \gamma ^ { * } }$

Remark 22.4. A residual factor g of G is replaceable by any$f = g + b ^ { q } v ^ { \gamma ^ { * } }$ with$b \ \in \ R _ { \xi }$so long as$o r d _ { \xi } ( b ^ { q } ) \geq d - | \gamma ^ { * } |$with$d = r e s o r d _ { \xi } ( \mathcal { G } )$ Such a replacement can change not only$i n _ { \xi } ( g )$but also$L ( g , a ) ^ { r e s i }$ However we see that for all a with$p ^ { e _ { a } } < | \gamma ^ { * } | + q$the module$L ( g , a ) ^ { r e s i } +$ $L _ { q - m a x } ( \mathcal { G } ) ^ { c o f a }$is independent of the choice of g by Lem.(22.2).

Lemma 22.3. Pick any residual factor f of G and write$\begin{array} { r } { f = \sum _ { \alpha } f _ { \alpha } ^ { q } x ^ { \alpha } } \end{array}$ with$f _ { \alpha } \in R _ { \xi }$in terms of the parameters$\boldsymbol { x } = ( w , v , \omega )$of$E q . ( 2 2 . 1 )$ where$0 \leq \alpha _ { i } < q , \forall i$$I f f _ { \alpha } = 0$for$x ^ { \alpha } = v ^ { \gamma ^ { * } }$, then for every$b \in R _ { \xi }$ such that$o r d _ { \xi } ( b ^ { q } ) + | \gamma ^ { * } | \geq o r d _ { \xi } ( f ) = d > 0$we have

$$
L (f - b ^ {q} v ^ {\gamma^ {*}}, a) \supset L (f, a)\tag{22.6}
$$

$$
f o r \forall a w i t h p ^ {e _ {a}} <   | \gamma^ {*} | + o r d _ {\xi} (b) q
$$

which implies

$$
L (f, a) = \bigcap_ {o r d _ {\xi} (b) q \geq d - | \gamma^ {*} |} L (f - b ^ {q} v ^ {\gamma^ {*}}, a) f o r \forall a w i t h p ^ {e _ {a}} <   | \gamma^ {*} | + o r d _ {\xi} (b) q
$$

and

$$
L(v^{\gamma}f,b) = \bigcap_{\substack{ord_{\xi}(\mathbf{g})\geq d\\ \mathcal{G} = (\mathbf{g}\| /^{q})}}L(\mathbf{g},b)\quad for \forall b with p^{e_{b}} <   d\tag{22.7}
$$

where Eq.(22.6) ⇔ Eq.(22.7) is proven by multiplication by$v ^ { \gamma }$.

Definition 22.2. With$d = r e s o r d _ { \xi } ( \mathcal { G } ) = o r d _ { \xi } ( f )$we define

$$
L_{q - max}(\mathcal{G})^{resi} = \bigcap_{\substack{b  \in R_{\xi}\\ ord_{\xi}(b)q\geq d - |\gamma^{*}|}}L_{q - max}(f + b^{q}v^{\gamma^{*}})^{resi}\tag{22.8}
$$

which is equal to a particular$L _ { q - m a x } ( f ) ^ { r e s i }$when$f$is chosen according to Lem.(22.3).

Definition 22.3. Furthermore we define

$$
\begin{array}{r l} & {R e s i _ {\xi , q} (\mathcal {G}) \left(o r R e s i _ {\xi} (\mathcal {G}) o r R e s i (\mathcal {G})\right)} \\ & {\quad = L _ {q - m a x} (\mathcal {G}) ^ {r e s i} + L _ {q - m a x} (\mathcal {G}) ^ {c o f a}} \\ & {\quad = L _ {q - m a x} (f) ^ {r e s i} + \sum_ {i} \kappa_ {\xi} i n _ {\xi} (v _ {i})} \\ & {= L _ {q - m a x} (f + b ^ {q} v ^ {\gamma^ {*}}) ^ {r e s i} + \sum_ {i} \kappa_ {\xi} i n _ {\xi} (v _ {i})} \end{array}\tag{22.9}
$$

where$f$is any residual factor of$\mathcal { G }$and$b \ \in \ R _ { \xi }$is any such that $o r d _ { \xi } ( b ^ { q } ) \geq d - | \gamma ^ { * } |$. The independence on the choice of residual factors $f$is due to Lem.(22.2) and to Rem.(22.4).$R e s i _ { \xi , q } ( \mathcal { G } )$will be called the residual cotangent q-module of$\mathcal { G }$or residual q-module for short.

Definition 22.4. In view of Lem.(22.3) and by use of the notation of Def.(21.3) we also define

$$
L_{[p^{+}] - max}(\mathcal{G})^{resi} = \bigcap_{\substack{b  \in R_{\xi}\\ ord_{\xi}(b^{q})\geq d - |\gamma^{*}|}}L_{[p^{+}] - max}(f + b^{q}v^{\gamma^{*}})\tag{22.10}
$$

Furthermore we define

(22.11)

$$
\begin{array}{c}R e s i_{\xi ,[p^{+}]}(\mathcal{G})\left(= R e s i_{[p^{+}]}(\mathcal{G})\right)\\ = L_{[p^{+}] - m a x}(\mathcal{G})^{r e s i} + L_{q - m a x}(\mathcal{G})^{c o f a}\\ = L_{[p^{+}] - m a x}(\mathcal{G})^{r e s i} + \sum_{i}\kappa_{\xi}in_{\xi}(v_{i})\\ \\ = \bigcap_{\substack{b\in R_{\xi}\\ o r d_{\xi}(b^{q})\geq d - |\gamma^{*}|}}L_{p^{+} - m a x}(f + b^{q}v^{\gamma^{*}})^{r e s i} + in_{\xi}(v)\kappa_{\xi} \end{array}\tag{22.12}
$$

## 23. Key parameters

Definition 23.1. We consider a$/ ^ { q } .$-exponent$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$and write its standard abc-presentation$\mathbf { g } = z ^ { q \mathbf { b } } v ^ { \gamma } .$f with a residual factor$f$

A single element z or a system${ \boldsymbol { \zeta } } = \left( \zeta _ { 1 } , \cdots , \zeta _ { k } \right)$with$\zeta _ { i } \in M _ { \xi }$will be called a key q-parameter or a system of key q-parameters of$\bar { \mathcal { G } }$at$\xi$if $\bar { \zeta } = ( \bar { \zeta } _ { 1 } , \cdots , \bar { \zeta } _ { k } )$with$\bar { \zeta } _ { i } = i n _ { \xi } ( \zeta _ { i } ) \in M _ { \xi } / M _ { \xi } ^ { 2 }$induces a nonzero image or$\kappa _ { \xi } { - } \mathrm { l i n e a r l y }$independent images inside the following module.

$$
\begin{array}{r l} & {R C _ {\xi} (\mathcal {G}) = R e s i _ {\xi , q} (\mathcal {G}) / L _ {q - m a x} (\mathcal {G}) ^ {c o f a}} \\ {=} & {\left\{L _ {q - m a x} (f) + \sum_ {i} \bar {v} _ {i} \kappa \right\} \mod \left\{\sum_ {i} \bar {v} _ {j} \kappa_ {\xi} \right\}} \end{array}\tag{23.1}
$$

Refer to$R e s i _ { \xi , q } ( \mathcal { G } )$of Def.(22.9) and$L _ { q - m a x } ( \mathcal { G } ) ^ { c o f a }$

Definition 23.2. A nonempty$\zeta$is called key$[ p ^ { + } ]$-parameters of$\mathcal { G }$at $\xi$if their images are κ<sub>ξ</sub>-linearly independent inside

$$
R C _ {\xi , [ p ^ {+} ]} (\mathcal {G}) = R e s i _ {\xi , [ p ^ {+} ]} (\mathcal {G}) / L _ {q - m a x} (\mathcal {G}) ^ {c o f a}\tag{23.2}
$$

Refer to$R e s i _ { \xi , [ p ^ { + } ] } ( \mathcal { G } )$of Eq.(22.12) of Def.(22.10).

Remark 23.1. The key parameters will be used to prevent the occurance of jumps of residual orders after permissible blowups. Normally we have many more key$[ p ^ { + }$]-parameters than key q-parameters. Every key$q -$ parameters works efectively against creation of residual jumps while key$[ p ^ { + } ]$-parameters may not always do so.

Remark 23.2. Let us consider a blowup$\pi : Z ^ { \prime } \longrightarrow Z$with a smooth center D which is “strongly permissible” for$\mathcal { G }$in the sense of Def.(18.3). This means o$\cdot d _ { \xi } ( \mathcal { G } ) = o r d _ { D } ( \mathcal { G } )$where or$\cdot d _ { D }$denotes the order at the generic point of D. Pick a closed point$\xi ^ { \prime } \in \pi ^ { - 1 } ( \xi ) \cap S i n g ( \mathcal { G } )$and choose an exceptional parameter z for$\xi ^ { \prime } ,$, that means$M _ { \xi } R _ { \xi ^ { \prime } } = \mathfrak { z } R _ { \xi ^ { \prime } }$ Let$I = I ( D ) = I ( D , Z )$denote the ideal of$D \subset Z$. Let$\check { I _ { \xi } } \stackrel { \cdot } { = } I ( D , Z ) _ { \xi }$ denote the ideal in$R _ { \xi } . ~ \mathrm { I f } ~ \xi$is understood, then we may write I for$I _ { \xi }$

Remark 23.3. In the Lem.(23.1) below, we follow the notation and the assumptions of Def.(23.1), Def.(23.2) and Rem.(23.2). Moreover assume that we are given a residual factor$f$of$\mathcal { G }$so that$r e s o r d _ { \xi } ( \mathcal { G } ) =$ $o r d _ { \xi } ( f ) = d > 0$. We then consider the p-flag of$f _ { \cdot }$, say

$$
\left\{L _ {\xi} (f, a), p ^ {e _ {a}}, 1 \leq a \leq l \right\}.\tag{23.3}
$$

Pick a system$\bar { w } = ( \bar { w } ( 1 ) , \cdots , \bar { w } ( l ) )$such that$\bar { w } ( a )$is a cotangent base $o f p \mathrm { - } e x p o n e n t e _ { a }$in the sense of Def.(21.2). We are now ready to state a lemma as follows.

Lemma 23.1. If$f \in I ^ { d }$and$o r d _ { \xi ^ { \prime } } ( \mathfrak { z } ^ { - d } f ) \geq d$then we claim:

(1) We can choose$w = ( w ( 1 ) , \cdot \cdot \cdot , w ( l ) )$in such a way that (a)$\bar { w } = i n _ { \xi } ( w )$and every member of w is contained in$I _ { \xi }$. (b) Every member$o f { \mathfrak { z } } ^ { - 1 }$w belongs to$M _ { \xi ^ { \prime } }$

(2) We write$f = f _ { \flat } + f _ { \sharp }$in such a way that$f _ { \flat }$is a homogeneous polynomial of degree d in$\mathbb { K } [ \boldsymbol { w } ]$and$f _ { \sharp } \in M _ { \xi } I ^ { d } = M _ { \xi } ^ { d + 1 } \cap I ^ { d }$

(3) z is transversal to w in the sense that$( \mathfrak { z } , w )$is extendable to a regular system of parameters of$R _ { \xi }$. Moreover${ \mathfrak { z } } ^ { - 1 } w$, say$w ^ { \prime }$, is extendable to a regular system of parameters of$M _ { \xi ^ { \prime } }$of which z is another member.

(4)${ \mathfrak { z } } ^ { - d } f _ { \flat }$is a homogeneous polynomial of degree d in$\mathbb { K } [ \boldsymbol { w } ^ { \prime } ]$while ${ \mathfrak { z } } ^ { - d } f _ { \sharp }$is divisible by z in$R _ { \xi } ^ { \prime }$. We must have or$d _ { \xi ^ { \prime } } ( \mathfrak { z } ^ { - d } \bar { f } ) \ = \ d$

(5) The p-flag of f<sub>♭</sub> is equal to that of f as was defined by$E q . ( 2 3 . 3 )$ Letting$f _ { \mathrm { b } } ^ { \prime } = \mathfrak { z } ^ { - d } f _ { \mathrm { b } }$, we can write the p-flag of f′ as follows.

$$
\{\bar {\mathfrak {z}} ^ {- 1} L _ {\xi} (f, a), p ^ {e _ {a}}, 1 \leq a \leq l \}\tag{23.4}
$$

with the notation of$E q . ( 2 3 . 3 )$

where$\bar { \mathfrak { z } } = ( { \mathfrak { z } }$mod$M _ { \xi } ^ { 2 } )$

(6)$f _ { \flat } ^ { \prime }$is cotangentially subordinate to f′ in the sense of Def.(21.1).

Theorem 23.2. Recall Rem.(23.2) wiith$\mathcal { G } ~ = ~ \left( z ^ { q \mathbf { b } } v ^ { \gamma } f \parallel / { } ^ { q } \right)$and a blowup$\pi : Z ^ { \prime } \longrightarrow Z$with center D which is “strongly permissible” for${ \mathcal { G } } . \quad . \quad A$ssume that$o r d _ { D } ( f ) \ = \ r e s o r d _ { \xi } ( \mathcal { G } )$. Refer to$D e f . ( 2 ? )$ and$D e f . ( 2 3 . 1 )$. According to$D e f . ( 2 3 . 1 )$let$\zeta$be a nonempty system of key$[ p ^ { + } ]$-parameters of G at a closed point$\xi ~ \in ~ S i n g ( \mathcal { G } )$so that $( \zeta , v )$is a subsystem of a regular system of parameters of$R _ { \xi }$. Let $\mathcal { G } ^ { \prime } = \left( z ^ { \prime } ^ { q \mathbf { b } ^ { \prime } } v ^ { \prime } ^ { \gamma ^ { \prime } } f ^ { \prime } \rVert / ^ { q } \right)$be the transform of G by π with qΓ-cofactor$v ^ { \prime \gamma ^ { \prime } }$ Pick any closed point$\xi ^ { \prime } \in \pi ^ { - 1 } ( \xi )$and an exceptional parameter${ \mathfrak { p } } \in M _ { \xi }$ for π at$\xi ^ { \prime }$. If we have

$$
| \gamma^ {\prime} | \neq 0 a n d\tag{23.5}
$$

$$
d = \operatorname{resord} _ {\xi} (\mathcal {G}) \leq \operatorname{resord} _ {\xi^ {\prime}} \left(\mathcal {G} ^ {\prime}\right) = d ^ {\prime}
$$

then we must have

(1)$\xi ^ { \prime }$is not metastable for π and$d ^ { \prime } \ = \ d$

(2)$\mathfrak { \hat { \mathfrak { \ M } } } ^ { - 1 } \zeta _ { j } \in M _ { \xi ^ { \prime } } f o r$every j and

$\mathfrak { p } ^ { - 1 } \zeta$$[ p ^ { + } ]$$\mathcal { G } ^ { \prime }$$\xi ^ { \prime }$

Theorem 23.3. If G has qΓ-cofactor$v ^ { \gamma } = 1$at ξ then there exists a nonempty system ζ of key q-parameters of G at$\xi$in the sense of $D e f . ( 2 3 . 1 )$. Let us pick any system of key q-parameters$\zeta = \left( \zeta _ { 1 } , \cdots , \zeta _ { k } \right)$ of G at ξ and any exceptional parameter y at a closed point$\xi ^ { \prime } \in \pi ^ { - 1 } ( \xi )$ by a fitted permissible blowup$\pi : Z ^ { \prime } \longrightarrow Z$for G. If resord<sub>ξ</sub>$( \mathcal { G } ) \leq$ $r e s o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } )$for the transform$\mathcal { G } ^ { \prime }$of G by π we then have$r e s o r d _ { \xi } ( \mathcal { G } ) =$ resor$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } )$and that$\mathfrak { \mathfrak { \mathfrak { \ g } } } ^ { - 1 } \zeta _ { i } , 1 \le i \le k$, form a system ofkey q-parameters of$\mathcal { G } ^ { \prime }$at$\xi ^ { \prime }$.

Theorem 23.4. Assume that we have a nonempty system of key$q -$ parameters${ \boldsymbol { \zeta } } = ( \zeta _ { 1 } , \cdots , \zeta _ { k } )$of$\mathcal { G } = ( z ^ { q \mathbf { b } } v ^ { \gamma } f \| / ^ { q } )$at$\xi \in Z$. Let$\pi :$ $Z ^ { \prime } \longrightarrow Z$with center$D$and G′ be the same as in Th.(23.2). Pick any $\xi ^ { \prime } \in \pi ^ { - 1 } ( \xi )$and an exceptional parameter$\mathfrak { p } \in M _ { \xi }$at$\xi ^ { \prime } , \ I f$we have

$$
d = \operatorname{ord} _ {\xi} (f) = \operatorname{resord} _ {\xi} (\mathcal {G}) \leq \operatorname{resord} _ {\xi^ {\prime}} \left(\mathcal {G} ^ {\prime}\right) = d ^ {\prime}
$$

then we have

(1)$\xi ^ { \prime }$is not metastable for π and$d = d ^ { \prime }$

(2)$\mathfrak { p } ^ { - 1 } \zeta _ { j } \in M _ { \xi ^ { \prime } }$for all$j$and

(3) the system$\zeta ^ { \prime }$composed of$\zeta _ { i } ^ { \prime } = \mathfrak { \eta } ^ { - 1 } \zeta _ { i } - c _ { i } , 1 \le i \le k$, is a key q-parameters for$\mathcal { G } ^ { \prime }$at$\xi ^ { \prime }$where$c _ { i }$is the value$o f { \mathfrak { \mathfrak { h } } } ^ { - 1 } \zeta _ { i }$at$\xi ^ { \prime }$.

Corollary 23.5. Consider a sequence of fitted permissible blowups$\pi _ { j }$: $Z _ { j + 1 } \longrightarrow Z _ { j }$for$\mathcal { G } _ { j }$for$j \geq 0$where$Z _ { 0 } = Z$and$\mathcal { G } _ { j + 1 }$is the transform of$\mathcal { G } _ { j }$by$\pi _ { j }$with$\mathcal { G } _ { 0 } = \mathcal { G }$. Also consider a sequence of closed points $\xi _ { j + 1 } \in \pi _ { j } ( \xi _ { j } ) \cap S i n g ( \mathcal G _ { j + 1 } )$with$\xi _ { 0 } = \xi$. Under the same assumption of Th.(23.4) on the existence of ζ with respect to$\mathcal { G }$at$\xi ,$none of the$\xi _ { j + 1 }$ can be metastable for$\pi _ { j }$if we have resor$d _ { \xi _ { j + 1 } } \mathopen { } \mathclose \bgroup \left( \mathcal { G } _ { \xi _ { j + 1 } } \aftergroup \egroup \right) \ \geq$resord<sub>ξj</sub>$( \mathcal { G } _ { \xi _ { j } } )$ for all$j$. Moreover we then have res$o r d _ { \xi _ { j + 1 } } ( \mathcal { G } _ { \xi _ { j + 1 } } ) = r e s o r d _ { \xi _ { j } } ( \mathcal { G } _ { \xi _ { j } } ) \ f o r$ all$j$. Moreover the system$\zeta$has its strict transforms$\zeta _ { j }$in$R _ { \xi _ { j } }$which are systems of key q-parameters in$Z _ { j }$

## 24. ♯-key parameters

We assume a$/ ^ { q } -$-exponent$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$with a standard abc-presentation Eq.(20.1) of Def.(20.1). Namely

$$
\mathbf {g} = z ^ {\mathbf {a}} g \text {with} z ^ {\mathbf {a}} = z ^ {q \mathbf {b}} v ^ {\mathbf {c}}\tag{24.1}
$$

with a residual factor g such that or$d _ { \xi } ( g ) = r e s o r d _ { \xi } ( \mathcal { G } )$

Definition 24.1. An element$\zeta \in M _ { \xi } \setminus M _ { \xi } ^ { 2 }$will be called a ♯-exact parameter of G if we can find

$$
\partial \in D i f f _ {Z, \xi} ^ {(d - p ^ {a})} \text {   such   that   } \partial (\mathbf {g}) = \zeta^ {q _ {a}}\tag{24.2}
$$

where$q _ { a } = p ^ { e _ { a } }$with some integer$0 \leq e _ { a } < e$so that$1 \leq q _ { a } < q$. If moreover$\zeta$induces a nonzero image in$R C _ { \xi } ( \mathcal G )$of$\mathrm { E q . ( 2 3 . 1 ) }$then$\zeta$is called$\sharp$-exact key$q \mathrm { - }$parameter, or$\sharp \cdot$-key paramter for short, of$\mathcal { G }$at$\xi .$.

Remark 24.1. The existence of the ∂ with the equality of Def.(24.1) is stronger than that of of Eq.(21.5) of Rem.(21.2), which is in turn stronger than that of Eq.(21.3) of Rem.(21.1).

Theorem 24.1. The notion of ♯-key parameter of$D e f . ( 2 4 . 1 )$is independent of whether we choose p-flag of either g or$v ^ { \mathbf { c } } g$or$g$of the standard abc-presentation Eq.(24.1) of$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$

Theorem 24.2. When$q = p o r e = 1$, every key q-parameter$\zeta$is automatically ♯-exact in the sense of$E q . ( { \mathcal { Q } } _ { 4 } . { \mathcal { Q } } )$of$D e f . ( 2 4 . 1 )$at every closed point$\xi \in S i n g ( \mathcal { G } )$

Remark 24.2. Given a /<sup>q</sup>-exponent$\mathcal { G }$of together with a ♯-key parameters$\zeta ^ { \sharp }$of$\mathcal { G }$at$\xi$we will define an idempotent diferential operator$\mathfrak { d } ^ { \sharp }$ as follows.

(1) Firstly choose a subsystem$\varpi$of ω such that$y = ( \zeta ^ { \sharp } , z , \varpi )$is a regular system of parameters of$R _ { \xi } . { \mathrm { ~ I f ~ } } \zeta ^ { \sharp }$is empty then we let $\varpi = \omega$and$y = x$

(2) Let us then define$\mathfrak { d } ^ { \sharp }$to be the$\ast _ { - } f u l l$idempotent diferential operator in$D i f f _ { R _ { \xi } / \rho ^ { e } ( R _ { \xi } ) [ z , \varpi ] }$with respect to the parameters$\zeta ^ { \sharp }$ in the sense of$\mathrm { D e f . } ( ? ? )$and Def.(??).

(3) If$\zeta ^ { \sharp } = \varnothing$then$\mathfrak { d } ^ { \sharp } = 0$

Definition 24.2. We define

$$
\mathbf {g} ^ {\sharp} = \mathfrak {d} ^ {\sharp} (\mathbf {g})\tag{24.3}
$$

with the ♯-idempotent diferential operator$\mathfrak { d } ^ { \sharp }$of Rem.(24.2).

Theorem 24.3. Assume$\zeta ^ { \sharp } \neq \emptyset$. Let$K ( Z )$be the field of fractions of $R _ { \xi }$or the function field of Z. Then

$$
K (\mathfrak {d} ^ {\sharp}) = \{\phi \in K (Z) | \mathfrak {d} ^ {\sharp} (\phi) = 0 \}
$$

is equal to$\rho ^ { e } ( K ) ( z , \varpi )$which is a proper subfield of$K ( Z )$. Moreover with$\mathbf { g } ^ { \sharp }$of$E q . ( { \mathcal { Q } } _ { 4 } . { \mathcal { Y } } )$we have$\mathfrak { d } ^ { \sharp } ( \mathbf { g } ^ { \sharp } ) = \mathbf { g } ^ { \sharp }$and$\mathbf { g } - \mathbf { g } ^ { \sharp } \in K ( \mathfrak { d } ^ { \sharp } )$

Definition 24.3. The idempotent diferential operator$\mathfrak { d } ^ { \sharp }$obtained above will be called ♯-idempotent diferential operator of$\mathcal { G }$associated with the given ♯-key parameters$\zeta ^ { \sharp }$

Remark 24.3. With$\mathfrak { d } ^ { \sharp }$of Rem.(24.2) let us define

$$
\chi = \max \{c \in \mathbb {Z} ^ {s} | i n _ {\xi} (z ^ {c}) d i v i d e s i n _ {\xi} (\mathfrak {d} ^ {\sharp} \mathbf {g}) \}\tag{24.4}
$$

where$z = ( z _ { 1 } , \cdots , z _ { s } )$is the system of equations for those members of Γ which pass through ξ. Here if$\zeta ^ { \sharp } = \emptyset$then the max does not exist or$\chi = \infty ^ { s }$. If$\zeta ^ { \sharp }$is not empty then$\chi \in \mathbb { Z } _ { 0 } ^ { s }$. Always$z ^ { \mathbf { a } }$divides$z ^ { \chi }$but they do not coincide in general. We can write

$$
\mathfrak {d} ^ {\sharp} (\mathbf {g}) = z ^ {\chi} g ^ {\circ} + \mathbf {g} ^ {+} w i t h g ^ {\circ} \in R _ {\xi}\tag{24.5}
$$

subject to the condition that we have

$$
\begin{array}{r l} {o r d _ {\xi} (\mathbf {g} ^ {+})} & {> o r d _ {\xi} (g ^ {\circ}) + | \chi |} \\ {=} & {o r d _ {\xi} (\mathfrak {d} ^ {\sharp} (\mathbf {g}))} \end{array}\tag{24.6}
$$

Throughout the rest of this section we will be assuming$\zeta ^ { \sharp } \neq \emptyset$

Theorem 24.4. All the following three

(1)$\mathbf { g } = z ^ { \mathbf { a } } \ : g$of$E q . ( 2 0 . 1 )$

(2)$\mathbf { g } ^ { \sharp } = \mathfrak { d } ^ { \sharp } \mathbf { g }$of$E q . ( { \mathcal { Q } } _ { 4 } . { \mathcal { Y } } )$

(3) and$z ^ { \chi } g ^ { \circ }$of$E q . ( 2 4 . 5 )$

have the same$\zeta ^ { \sharp }$as their ♯-key parameters according to$D e f . ( 2 ? )$after Rem.(??). Moreover$i f \zeta ^ { \sharp }$is sharp-exact for any one of the three$/ ^ { q } -$ exponents as above then it is the same for the others.

Definition 24.4. Let us define the following$/ ^ { q } .$-exponent

$$
\begin{array}{r c l} \mathcal {G} (\sharp) & = & (\mathbf {g} (\sharp) \parallel / ^ {q})   =   (z ^ {\mathbf {a} (\sharp)} g (\sharp) \parallel / ^ {q}) \\ & = & (z ^ {q \mathbf {b} (\sharp)} v (\sharp) ^ {\mathbf {c} (\sharp)} g (\sharp) \parallel / ^ {q}) \end{array}\tag{24.7}
$$

in the manner of Eq.(20.1) of Def.(20.1).

Remark 24.4. The Γ-monomial$z ^ { \chi }$of Rem.(24.3) is uniquely determined by Eq.(24.4). Now let us choose the idempotent diferential operator

$$
\mathfrak {d} ^ {(\chi)} \quad i n \quad D i f f _ {R _ {\xi} / \rho^ {e} (R _ {\xi}) [ \zeta (\sharp), v (\sharp) ^ {*} ]} \qquad (c f L e m. (\ref {e q : 1 2 . 0 5})\tag{24.8}
$$

with respect to the parameters$v ( \sharp )$where$v 0 ^ { * }$denotes the q-complement of$v ( \sharp )$in z. Recall that for every$\phi \in \rho ^ { e } ( R _ { \xi } ) [ \zeta ( \sharp ) , v ( \sharp ) ^ { * } ]$

$$
\mathfrak {d} ^ {(\chi)} (v (\sharp) ^ {\lambda} \phi) = \left\{ \begin{array}{l l} v (\sharp) ^ {\lambda} \phi & i f \lambda = \chi (\sharp) \\ 0 & i f o t h e r w i s e \end{array} \right.
$$

Let us define the following notation:

Definition 24.5.$\begin{array} { r } { \begin{array} { r } { \mathcal { D } ^ { ( A ) } \ = \ \sum _ { k \in \epsilon ^ { n } ( q ) \cap A + \mathbb { Z } _ { 0 } ^ { n } } \mathfrak { d } ^ { k } . } \end{array} } \end{array}$

Remark 24.5. We have defined$\mathbf { g } ( \sharp )$in Th.(24.3). and use it for the study done later of the protostable structure of equations. Here we define a further partial sum$\mathbf { g } ^ { \circ }$of$\mathbf { g } ( \sharp )$and hence of$\mathbf { g } .$

$$
\mathbf {g} ^ {\circ} = \mathcal {D} (\sharp) \mathbf {g} \text {   with   } \mathcal {D} (\sharp) = \mathcal {D} ^ {(x)} (\mathfrak {d} ^ {\sharp})\tag{24.9}
$$

Note that$i n _ { \xi } ( { \bf g } ^ { \circ } ) = i n _ { \xi } ( { \bf g } )$and that$\mathbf { g } ^ { \circ }$is divisible by$z ^ { \chi }$in$R _ { \xi }$. Hence, from now on, we specifically choose$g ^ { \circ }$of Eq.(24.5) to be$g ^ { \circ } = z ^ { - \chi } \mathbf { g } ^ { \circ }$ with$\mathbf { g } ^ { \circ }$of Eq.(24.9). Thus we have

$$
\mathbf {g} ^ {\circ} = z ^ {\chi} g ^ {\circ} \text {with} g ^ {\circ} = \mathfrak {d} ^ {\sharp} g ^ {*}\tag{24.10}
$$

with$g ^ { \ast } = \mathfrak { d } ^ { + } g$in the sense of$\operatorname { E q . } ( ? ? )$. Moreover it should be noted that$\mathcal { D } ^ { ( \chi ) }$and$\mathfrak { d } ^ { \sharp }$commute each other for they depend disjoint sets of variables, the former of z and the latter of$\zeta ( \sharp )$. Hence Eq.(24.9) can be written as$\mathbf { g } ^ { \circ } = \mathfrak { d } ^ { \sharp } ( \mathcal { D } ^ { ( \chi ) } \mathbf { g } )$and$\mathcal { D } ( \sharp )$is idempotent, too. Thus we have

$$
\mathfrak {d} ^ {\sharp} \mathbf {g} ^ {\circ} = \mathbf {g} ^ {\circ} = \mathcal {D} (\sharp) \mathbf {g} ^ {\circ}\tag{24.11}
$$

Lemma 24.5. The definition of χ by$E q . ( 2 4 . 4 )$produces the same result when we replace g by$\mathbf { g } ^ { \circ }$in the equation$E q . ( 2 4 . 4 )$

We now go back to$\mathbf { g } ^ { \sharp }$defined by Eq.(24.3) of Def.(24.2). We first simplify the notation by writing

$$
\mathbf {g} 0 \text {for} \mathbf {g} ^ {\sharp}\tag{24.12}
$$

and then define what will be called ♯-derivative of$\mathcal { G }$as follows. Here we are assuming$\zeta ^ { \sharp 0 } \neq \emptyset$

Definition 24.6. Let$z ^ { \mathbf { a } ( \sharp ) }$be the Γ-maximal factor of$\mathbf { g } ( \sharp ) = \mathbf { g } ^ { \sharp }$of Eq.(24.12) and let$\mathbf { g } ( \sharp ) = z ^ { - \mathbf { a } ( \sharp ) } \mathbf { g } ^ { ( \sharp ) }$. We have

$$
z ^ {\mathbf {a}} d i v i d e s z ^ {\mathbf {a} (\sharp)} w h i c h d i v i d e s z ^ {\chi}
$$

with reference to a of$\operatorname { E q . } ( ? ? )$. We define the following /<sup>q</sup>-exponent:

$$
\mathcal {G} (\sharp) = \left(\mathbf {g} (\sharp) \| / ^ {q}\right)\tag{24.13}
$$

$$
\text { with } \mathbf {a} (\sharp) = q \mathbf {b} (\sharp) + \mathbf {c} (\sharp)
$$

$$
s o t h a t \mathbf {g} (\sharp) = z ^ {\mathbf {a} (\sharp)} g (\sharp) = z ^ {q \mathbf {b} (\sharp)} v (\sharp) ^ {\mathbf {c} (\sharp)} g (\sharp)
$$

which satisfy all the conditions to be a standard abc-expression in the sense of Def.(20.1). Namely

(1)$z ^ { \mathbf { a } ( \sharp ) }$is the Γ-maximal factor,$z ^ { q \mathbf { b } ( \sharp ) }$is qΓ-factor and$v ( \sharp ) ^ { \mathbf { c } ( \sharp ) }$is qΓ-cofactor of$\mathcal { G } ( \sharp )$with a subsystem$v ( \sharp )$of$z .$

(2)$q > \mathbf { c } ( \sharp ) _ { j } > 0$for all$j$.

(3)$g ( \sharp )$is a residual factor of$\mathcal { G } ( \sharp )$

for which we should recall Th.(19.1), Rem.(19.1), Def.(19.1) and Def.(19.3). We then have

(1) Let$o r d _ { \xi } ( g ( \sharp ) ) = d ( \sharp )$and it is equal to$r e s o r d _ { \xi } ( \mathcal { G } ( \sharp ) )$

$$
\mathfrak {d} ^ {\sharp} (\mathbf {g} (\sharp)) = \mathbf {g} (\sharp)
$$

$$
\mathfrak {d} ^ {\sharp (\sharp)} (\mathbf {g} - \mathbf {g} (\sharp)) = 0
$$

Eq.(24.3). Indeed$\mathbf { g } - \mathbf { g } ( \sharp ) \in K ( \mathfrak { d } ^ { \sharp } )$in the sense of Th.(24.3). With the ♯-idempotent operator$\mathfrak { d } ^ { \sharp }$of Rem.(24.2), the couple$( \mathcal G ( \sharp ) , \mathfrak { d } ^ { \sharp } )$ will be called ♯-derivative of${ \mathcal { G } } .$. Sometime$\mathcal { G } ( \sharp )$alone is called the$\sharp -$ derivative with respect to the ♯-key parameters ζ(♯).

Theorem 24.6. Let$( \mathcal G ( \sharp ) , \mathfrak { d } ^ { \sharp } )$be the ♯-derivative of G with respect to the ♯-key parameters$\zeta ^ { \sharp } ~ o f \mathcal { G }$at$\xi$in the sense of$D e f . ( 2 4 . 6 )$. Then the same$\zeta ^ { \sharp }$is also a system of ♯-key parameters of$\mathcal { G } ( \sharp )$at$\xi$and the$\mathcal { G } ( \sharp )$ is the ♯-derivative of$\mathcal { G } ( \sharp )$itself with respect to the$\zeta ^ { \sharp }$. Conversely any system of ♯-key parameters of$\mathcal { G } ( \sharp )$is also such a system of G although $\mathcal { G } ( \sharp )$may not be the ♯-derivative of$\mathcal { G }$with respect to the new ♯-key parameters.

## Theorem 24.7. We always have

$$
d (\sharp) = \operatorname{resord} _ {\xi} (\mathcal {G} (\sharp)) \leq \operatorname{resord} _ {\xi} (\mathcal {G}) = \mathbf {d}\tag{24.14}
$$

for the ♯-derivative$\mathcal { G } ( \sharp )$of G at$\xi$. The diference of the two is$| a ( \sharp ) - \mathbf { a } |$ in the sense of$E q . ( 2 4 . 1 \mathcal { 3 } )$.

In the examples below we will follow the standard abc-expression in the sense of Eq.(20.1) with specified symbols.

Example 24.1. (Case:$\zeta ^ { \sharp 0 } \neq \varnothing )$Let us consider the case of$q = p = 2$ and$\mathcal { G } = \left( \mathbf { g } \parallel / \dot { q } \right)$with$h = ( \zeta _ { 1 } v _ { 1 } + \omega _ { 1 } ^ { 2 } ) v _ { 1 }$so that$z ^ { \mathbf { a } } = v ^ { \mathbf { c } } = v _ { 1 }$and $g = \zeta _ { 1 } v _ { 1 } + \omega _ { 1 } ^ { 2 }$. In this case$\zeta ^ { \sharp 0 } = ( \zeta _ { 1 } )$and$\mathcal { G } 0 = \left( \mathbf { g } 0 \parallel / ^ { q } \right)$with$\mathbf { g } 0 = \zeta _ { 1 } v _ { 1 } ^ { 2 }$ $z 0 ^ { a 0 } = z 0 ^ { q b 0 } = v _ { 1 } ^ { 2 }$and$v 0 ^ { c 0 } = 1$. Note that$i n _ { \xi } ( \mathbf { g } ) \neq i n _ { \xi } ( \mathbf { g } 0 )$

Example 24.2.$( \mathrm { C a s e } { : } \zeta ^ { { \sharp } { 0 } } = { \emptyset } )$Let us consider the case of$q = p = 2$ and$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$with$h = ( z _ { 1 } v _ { 1 } + v _ { 1 } ^ { 4 } + \omega _ { 1 } ^ { 3 } ) v _ { 1 }$so that$z ^ { \mathbf { a } } = v ^ { \mathbf { c } } = v _ { 1 }$and $g = z _ { 1 } v _ { 1 } + v _ { 1 } ^ { 4 } + \omega _ { 1 } ^ { 3 }$. Also$g ^ { * } = g$. In this case$\zeta ^ { \sharp 0 } = \varnothing$and${ \mathcal { G } } 0 = { \mathcal { G } }$, while

$$
\mathcal {G} (1) = \left(z ^ {a (1)} g (1) \| / ^ {q}\right) = \left(z ^ {q b (1)} v (1) ^ {c (1)} g (1) \| / ^ {q}\right)
$$

where$z ^ { a ( 1 ) } = v _ { 1 } ^ { 2 } , z ^ { q b ( 1 ) } = v _ { 1 } ^ { 2 } , v ( 1 ) ^ { c ( 1 ) } = 1$and$g ( 1 ) = z _ { 1 } + v _ { 1 } ^ { 4 }$. Moreover

$$
\mathcal {G} (2) = \left(z ^ {a (2)} g (2) \| / ^ {q}\right) = \left(z ^ {q b (1)} v (2) ^ {c (2)} g (2) \| / ^ {q}\right)
$$

where$z ^ { a ( 2 ) } = z _ { 1 } v _ { 1 } ^ { 2 } , z ^ { q b ( 2 ) } = v _ { 1 } ^ { 2 } , v ( 2 ) ^ { c ( 2 ) } = z _ { 1 }$and$g ( 2 ) = 1$. Note that $i n _ { \xi } ( { \bf g } ) = i n _ { \xi } ( { \bf g } ( 1 ) ) = i n _ { \xi } ( { \bf g } ( 2 ) )$while$h \neq \mathbf { g } ( 1 ) \neq \mathbf { g } ( 2 )$. We have$\mathcal { G } ( \sharp ^ { + } )$ is equal to all$\mathcal { G } ( k ) , k \geq 2$, but it is diferent from both$\mathcal { G }$and$\mathcal { G } ( 1 )$

## 25. /<sup>q</sup>-stratifications

We will be assuming that K is algebraically closed. We are given a /<sup>q</sup>-exponent$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$in$Z$and a Zariski-closed subset$Z ^ { \ast }$of the ambient scheme$Z$, We view$Z ^ { * }$as a closed reduced subscheme of$Z$. We then have a stratification of$Z ^ { * }$by virtue of Th.(17.1) in the following sense:

Definition 25.1. An$\mathcal { G } _ { c l } - s t r a t i f i c a t i o n$of$Z ^ { \ast }$is an expression of a finite disjoint union$Z ^ { * } = \cup _ { i } Z ( i )$such that

(1) the$Z ( i )$are smooth irreducible locally closed subschemes of$Z$ which are called strata, and

(2) or$d _ { \eta } ( \mathcal { G } )$is constant for all$\eta \in Z ( i ) \cap Z _ { c l }$for each i.

Remark 25.1. Among all possible G<sub>cl</sub>-stratifications of a given$Z ^ { \ast }$, there exists a canonical one which is constructed as follows:

Let us first define

$$
S _ {d} (\mathcal {G}, Z ^ {*}) = \{\eta \in Z _ {c l} ^ {*} | o r d _ {\eta} (\mathcal {G}) \geq d \}\tag{25.1}
$$

which is a closed subset of$Z _ { c l } ^ { * } = Z ^ { * } \cap Z _ { c l }$by$T h . ( 1 7 . 1 )$

For every integer$d \geq 1$, we let$T ( d )$denote the closure in$Z ^ { \ast }$of the subset$S _ { d } ( \mathcal { G } , Z ^ { * } )$of$\mathrm { E q . ( 2 5 . 1 ) }$. First of all let us note:

(1) For every$d \geq 1$we have${ \cal T } ( d ) \cap { \cal Z } _ { c l } ^ { * } \ = \ { \cal S } _ { d } ( { \mathcal G } , { \cal Z } ^ { * } )$because the latter is closed in$Z _ { c l } ^ { * }$

(2)$S _ { 1 } ( { \mathcal G } , Z ^ { * } ) = Z _ { c l } ^ { * }$. In fact for every$\eta \in Z _ { c l } ^ { * }$we can find$g \in R _ { \eta }$ such that$h - g ^ { q } \in m a x ( R _ { \eta } )$because the$R _ { \eta } / m a x ( R _ { \eta } )$is perfect. Therefore we have$\left( \mathbf { g } \parallel / ^ { q } \right) = \left( \mathbf { g } - g ^ { q } \parallel / ^ { q } \right)$

(3) Hence$T ( 1 ) = Z ^ { * }$

We let$d _ { 1 } = m i n \{ d > 0 | S _ { d } ( \mathcal { G } , Z ^ { * } ) \neq Z _ { c l } ^ { * } \}$and choose$C ( 1 )$to be the collection of connected (and then smooth irreducible) components of $Z ^ { * } - \left( S i n g ( Z ^ { * } ) \cup T ( d _ { 1 } ) \right)$. This$C ( 1 )$will be the first set of canonical strata. Choose the next set of strata to be the collection$C ( 2 )$of the connected components of$T ( d _ { 1 } ) \mathrm { ~ - ~ } \big ( S i n g ( T ( d _ { 1 } ) ) \cup T ( d _ { 2 } ) \big )$where$d _ { 2 }$is the smallest integer$> d _ { 1 }$such that$T ( d _ { 1 } ) \ \ne \ S i n g ( T ( d _ { 1 } ) ) \cup T ( d _ { 2 } )$ Let$S ( 1 ) = \left( S i n g ( T ( d _ { 1 } ) ) \cup T ( d _ { 2 } ) \right)$. Let$C ( 2 )$be the collection of the connected components of$S ( 1 ) - \left( S i n g ( S ( 1 ) ) \cup T ( d _ { 3 } ) \right)$where$d _ { 3 }$is the smallest integer$> \ d _ { 2 }$such that$S ( 1 ) \nearrow S i n g ( S ( 1 ) ) \cup T ( d _ { 3 } )$. Then let$S ( 2 ) = \left( S i n g ( S ( 1 ) ) \cup T ( d _ { 3 } ) \right)$. Repeat this process until we reach $S ( l ) = \emptyset$. The canonical stratification of$Z ^ { \ast }$with respect to$\mathcal { G }$is then the union of those collections$C ( j ) , j = 1 , 2 , \cdots$, which is altogether a finite collection.

The most basic case is$Z ^ { * } = Z$. However when$\mathcal { G }$is given in combination with another singular object such as an ideal exponent$E = ( J , b )$ in$Z$we often need to consider the case of$Z ^ { * } = S i n g ( E )$

Remark 25.2. By virtue of Rem.(??) we have a canonical refinement of any given$\mathcal { G } _ { c l }$-stratification in such a way that the NC-data Γ is normal crossing with every one of the strata of the refinement at every point of $Z$in the sense of Def.(??). The existence of such a refinement is proven thanks to the following fact. For every smooth irreducible locally closed subset$C$of$Z$and for the subsystem$\Gamma ( C )$of$\Gamma$consisting of those not containing$C ,$we find the smallest (an hence unique) nowhere dense closed subset$S$of$C$such that$\Gamma ( C )$is normally crossing with$C$at every point of$C \setminus S$. (See Def.(??) along with Rem.$( ? ? )$and Rem.$\left( ? ? \right) . )$ Then the final refinement can be obtained by descending induction on dimensions of strata by repeated replacement of$C$by$C \setminus S$and canonical$\mathcal { G } _ { c l }$-stratification of$S .$. (Choose$C$to be one of the biggest dimension among the given strata having non-empty$S$at each of the replacements.)

We consider a$/ ^ { q } .$-exponent$\mathcal { G }$in$Z$in the sense of Def.(16.1). Pick a closed point$\xi \in S i n g ( \mathcal { G } )$

On one hand we may choose a specific$\mathcal { G } _ { c l } { - } s t r a t i f i c a t i o n$of$Z$in the sense of Def.(25.1) and choose the stratum$T$containing$\xi .$This is a kind of top-down selection method, while it is meritably global in nature.

On the other hand we may take the set$S _ { c l } = S _ { c l } ( \xi )$of all those closed points of$S i n g ( \mathcal { G } )$at which the residual orders of$\mathcal { G }$are equal to $r e s o r d _ { \xi } ( \mathcal { G } )$This is a kind of bottom-up selection method. We have a naturally defined locally closed subscheme$S = S ( \xi )$of$Z$such that $S _ { c l } ( \xi ) = S ( \xi ) \cap Z _ { c l } = S ( \xi ) _ { c l }$. To be precise we first let C be the closure of$S _ { c l }$in$Z$and let$B$be the closure of$( C \cap Z _ { c l } ) \setminus S _ { c l }$in$Z$. Then we obtain$S$as being$C \setminus B$. (Refer Th.$( 1 7 . 1 ) . )$We then let$T$be the set of smooth points of S, which is a locally closed subscheme of$S$.

If the point$\xi$is such that

$$
\operatorname{resord} _ {\xi} (\mathcal {G}) = \max _ {\zeta \in \operatorname{Sing} (\mathcal {G}) _ {c l}} \operatorname{resord} _ {\zeta} (\mathcal {G})\tag{25.2}
$$

then$S _ { c l } ( \xi )$is a Zariski closed subset of$Z _ { c l }$and$S$is a closed subscheme of$Z$.

When we choose any straification of$Z$by means of a$/ ^ { q } .$-exponent given in$Z$it is inevitable from encountering and hence we need to deal with generic-up-down strata in the sense of Def.(??).

Let us review the example Ex.(16.2) of generic-up-down phenomena of the /<sup>q</sup>-exponent$\mathcal { G } = ( \mathbf { h } \| / ^ { p } )$with h$= t z ^ { p } + w ^ { p + 1 }$, which is given in a 5-dimensional afine space$Z = S p e c ( \mathbb { K } [ t , x , y , z , w ] )$. Let ξ be the origin at which$o r d _ { \xi } ( \mathcal { G } ) = p + 1$. In the example, our$S = S ( \xi )$turns out to be$S i n g ( \mathcal { G } )$which is 3-dimensional subspace. This is the closure $C$of the point${ \boldsymbol \sigma } = ( z , w )$The order of$\mathcal { G }$is$p + 1$at every closed point of$S$while it is$p$at the generic point$\sigma . \textit { S }$contains an irreducible surface which is the closure of$\zeta = \left( \phi , z , w \right)$with$\phi = x ^ { p } + t y ^ { p }$. Call the surface$F$. The singular locus of$F$is a line which is the closure of $\eta = ( x , y , z , w )$. Call the line$L ,$and$T = F \setminus I$is the smooth part of $F$. The order of G is$p + 1$at every point of$T$. It is also$p + 1$at every closed point of$L$but it is$p$at the generic point$\eta .$

The notable point of this example is that

$$
w e h a v e S \supsetneqq F \supsetneqq L \supsetneqq \xi w h i l e
$$

## S is generic-down ,$F$is not but L is

in the sense of generic-down subscheme defined by Def.(??). Also note that, excluding a single exception${ \cal { L } } = { \cal { S } } i n g ( F )$, we find no other irreducible curve of generic down type contained in$F$. All these claims follow from Th.(17.1) and Lem.(17.3).

The example Ex.(16.2) may be slightly modified as follows:

Example 25.1. Replace h by$\mathbf { h } ^ { * } = \mathbf { h } + \phi ^ { p + 1 } + z ^ { p + 1 }$. Let$\mathcal { G } ^ { * } = \left( \mathbf { h } ^ { * } \| / ^ { p } \right)$ Then we get$S i n g ( \mathcal { G } ^ { * } )$becomes$F$which is our new$S ( \xi )$. Every other claim made on Ex.(16.2) holds true for the points within$F$. Noteworthy point is that$S ( \xi )$is not generic-down but it contains$L$which is generic-down.

## 26. Retraction and primitive operators

In the study of efects of permissible blowup upon singularities of characteristic$p > 0$, if the centers are generic down type in the sense of Def.(??). we must then deal with some problems of special nature. Our tactics are to make use of those primitive and square nilpotent diferential operators of Th.(5.3) which are associated with local projection of the kind$v ~ : \xi \in Z  \mathbf { A } ^ { t }$in the sense of Def.(5.2) with Eq.(??). Refer to Th.(5.1) and Rem.(??).

Let us now introduce the “general” notion of local retractions and study its relation with primitive and square nilpotent diferential operators.

Definition 26.1. A local retraction at$\xi \in Z$will mean

Definition 26.2. A local retraction r of Def.(26.1) will be called separable if t is the dimension of S at$\xi$and the “induced morphism” is locally separable at$\xi .$. Note that the separability implies that S is reduced. A local reraction r will be called etale if the induced morphism is etale at$\xi \ ( \mathrm { i . e . }$, it produces an isomorphism of completed local rings).

When local retraction r is etale at$\xi \ S$is smooth and irreducible at ξ. We also have$t = d i m _ { \xi } S$

$$
\mathbf {r}: \xi \in S \subset Z \searrow \mathbb {A} ^ {t}\tag{26.1}
$$

which has the following properties.

(1) S is a locally closed subscheme and$\xi$is a closed point,

(2) r is a “smooth morphism” from an open neighborhood$U \cot \xi$in $Z$to an afine t-space$\mathbb { A } ^ { t } = S p e c ( \mathbb { K } [ \omega ] )$where$w = ( w _ { 1 } , \cdot \cdot \cdot , w _ { t } )$1 is a part of a regular system of parameters of$R _ { \xi } = \mathcal { O } _ { Z , \xi } ,$,ξ

(3) r induces a locally finite morphism$U \cap S \to \mathbb { A } ^ { t }$so that t is$\leq$ the dimension of S.

The symbol r will stand for the whole data of Eq.(26.1) called “local retraction”, as well as for the “projection morphism”$U \to \mathbb { A } ^ { t }$. This may be called “projection” for short. The morphism$S \cap U \to \mathbb { A } ^ { t }$ induced will be called the “induced morphism” of r.

Definition 26.3. Assume that we are given$q = p ^ { e }$in addition to a local separable retraction r of Def.(26.1). Such will be the case when we are working with a specific /<sup>q</sup>-exponent$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$. We then define

$$
B (q, \mathbf {r}) = (\rho^ {e} (\mathcal {O} _ {Z | U})) [ w ] c a l l e d t h e q - b a s e a l g e b r a o f \mathbf {r}\tag{26.2}
$$

which is a sheaf of subalgebras of$\mathcal { O } _ { Z | U }$. Its stalk$B ( q , \mathbf { r } ) _ { \xi }$is equal to $\rho ^ { e } ( R _ { \xi } ) [ w ]$and is called the q-base algebra of r at$\xi .$. We define

$$
Z (q, \mathbf {r}) = \operatorname{Spec} (B (q, \mathbf {r})) \text { called   the } q \text {-base scheme of } \mathbf {r}.\tag{26.3}
$$

Definition 26.4. Quite generally we define

$$
\mathcal {P} (q, \mathbf {r}) = H o m _ {B (q, \mathbf {r})} (\mathcal {O} _ {Z | U}, B (q, \mathbf {r}))\tag{26.4}
$$

where Hom denotes the sheaf of$B ( q , \mathbf { r } )$-homomorphisms. It should be noted that$\mathcal { P } ( q , \mathbf { r } )$depends on q and on r as “projection morphism”. It does not depend on S. Note that$\mathcal { P } ( q , \mathbf { r } )$is a finite$B ( q , \mathbf { r } ) – \mathrm { m o d u l e }$ We also define

$$
\begin{array}{r l} & {\mathcal {P} ^ {*} (q, \mathbf {r}) = \mathcal {P} (q, \mathbf {r}) \cap D i f f _ {Z} ^ {*}} \\ {=} & {\{\partial \in \mathcal {P} (q, \mathbf {r})   |   \partial (B (q, \mathbf {r})) = (0)   \}} \end{array}\tag{26.5}
$$

Remark 26.1. Let us consider a “retraction$\mathrm { e t a l e } ^ { \mathrm { } \dagger }$case. There then exists a regular system of parameters$( u , w )$of$R _ { \xi }$such that S is locally defined by the ideal$( u ) R _ { \xi }$and the projection morphism r is defined by w in the manner of Def.(5.2). With such a choice of$( u , w )$we claim the equalities with the symbols of the Eq.(??) of Def.(5.2) as follows

$$
\mathcal {P} (q, \mathbf {r}) _ {\xi} = \mathcal {P} ^ {q} (u / w) a n d \mathcal {P} ^ {*} (q, \mathbf {r}) _ {\xi} = \mathcal {P} ^ {* q} (u / w)\tag{26.6}
$$

Remark 26.2. Let V be the open set of those points$\eta \in S$at which$\mathbf { r } | S$ is etale. Then choose an open subset$U \subset Z$such that$V = U \cap S$and projection by w is smooth at every point of U. For notatinal simplicity we assume that the same u generates the ideal$I ( S , Z )$at every$\eta \in V$ We then have the following consequences.

(1) For every closed point$\eta \in V$we have a regular system of parameters$( u , w - w ( \eta ) )$of$R _ { \eta }$with the value$w ( \eta )$of w at$\eta .$ There Th.(5.3) and Rem.(??) are all valid for$( u , w - w ( \eta ) )$

(2) We have$\rho ^ { e } ( \mathcal { O } _ { Z } ) [ w - w ( \eta ) ] = \rho ^ { e } ( \mathcal { O } _ { Z } ) [ w ]$which is$B ( q , \mathbf { r } _ { \eta } )$with the retraction

$$
\mathbf {r} _ {\eta}: \eta \in S \subset Z \searrow \mathbb {A} ^ {t} = S p e c (\mathbb {K} [ w - w (\eta) ]
$$

(3) For the$B ( q , \mathbf { r } _ { \eta } )$given, every primitive idempotent section$\delta ( 0 ) _ { \eta }$ of$\mathcal { P } ( q , \mathbf { r } ) _ { \eta }$has the form$\begin{array} { r } { i d - \sum _ { \substack { ( 0 ) \neq a \in \epsilon ^ { s } ( q ) } } ( \theta _ { a } ) ^ { q } u ^ { a } \delta _ { u } ^ { ( a ) } } \end{array}$with$\theta _ { a } \in R _ { \eta }$ at η by Rem.(??). In order to have$\delta ( 0 ) = \delta _ { u } ^ { ( 0 ) }$we must have $\theta _ { a } = 1 , \forall a \neq 0$, and hence it is unique for a given u. However $\delta _ { u } ^ { ( 0 ) }$depends on the choice of u withn$( u ) R _ { \xi } = I ( S , Z ) _ { \eta }$for the given S. The dependence is shown by the following example.

Example 26.1. Assume$q \leq ( q - 1 ) ^ { s }$so that we have$a \in \epsilon ^ { s } ( q )$ with$| a | = q$. Let$v = ( v _ { 1 } , \cdot \cdot \cdot , v _ { s } )$be defined by$v _ { 1 } = u _ { 1 } , u _ { j } =$ $v _ { j } + v _ { 1 } , \forall j \geq 2$. Then$u _ { 1 } ^ { q } = \delta _ { v } ^ { ( 0 ) } ( u ^ { a } )$while$\delta _ { u } ^ { ( 0 ) } ( u ^ { a } ) = 1$

(4) In the “etale” case we then have

$$
B (q, \mathbf {r}) _ {\xi} = \delta (0) (R _ {\xi}) =\tag{26.7}
$$

$$
\delta_ {u} ^ {0} (\mathcal {O} _ {Z}) _ {\xi} = \mathcal {P} (q, \mathbf {r}) (\mathcal {O} _ {Z}) _ {\xi} = \mathcal {P} ^ {*} (q, \mathbf {r}) ^ {- 1} (0) _ {\xi}
$$

where we define

$$
\mathcal {P} ^ {*} (q, \mathbf {r}) ^ {- 1} (0) = \left\{f \in \mathcal {O} _ {Z} \mid \mathcal {P} ^ {*} (q, \mathbf {r}) f = (0) \right\}
$$

The point of$\mathrm { E q . ( 2 6 . 7 ) }$is that the primitive idempotent$\delta ( 0 )$is not unique but its image is unique$B ( q , \mathbf { r } ) _ { \xi }$, so long as we fix r as projection map.

Remark 26.3. Let us further examine the nature of q-base algebra $B ( q , \mathbf { r } )$in the sense of$\mathrm { E q . ( 2 6 . 2 ) }$, especially in the case of “ etale” retraction r,$B ( q , \mathbf { r } )$is “separably and integrally” closed in$R _ { \xi }$. To be precise we have the following

Lemma 26.1. With the same$\xi \in \cal { S } \subset Z$we pick any other etale retraction$\mathbf { r } ^ { \prime }$. Then$\mathbf { r } { ' }$is derived from r by composing the following two types of parameter changes.

(1) The first type is the one with$B ( q , \mathbf { r } ^ { \prime } ) = B ( q , \mathbf { r } )$

(2) The second type is the one with$w _ { i } ^ { \prime } - w _ { i } \in I ( S ) _ { \xi }$for all$1 \leq i \leq t$ where$\mathbf { r } { ' }$(respectively r) is defined by$w ^ { \prime }$(respectively w).

In both cases, we can choose$w ^ { * } \in B ( q , \mathbf { r } ) ^ { t }$with$w ^ { * } \equiv w ^ { \prime }$mod$I ( S ) ^ { t }$ and we have

$$
B (q, \mathbf {r} ^ {*}) = B (q, \mathbf {r})
$$

Definition 26.5. Consider various etale retraction

$$
\mathbf {r}: \xi \in S \subset Z \searrow \mathbb {A} ^ {t}
$$

for a fixed$S$which is smooth at$\xi .$Then the q-base algebra$B ( q , \mathbf { r } )$does depend on r as projectin morphism but the natural image of$B ( q , \mathbf { r } )$ into$R _ { \xi } / I ( S ) R _ { \xi }$is independent of the choice of r. This image will be dnoted by$\bar { B } ( \boldsymbol { S } ) _ { \xi }$. There exists a subalgebra of$B ( q , \mathbf { r } ) _ { \xi }$for any reference r having an isomrphism onto$\bar { B } ( S ) _ { \xi }$and it is often denoted by$B ( S ) _ { \xi }$

Incidentally we also consider the special case with$t = 0$in which case we should understand$S = \xi$and$\mathbb { A } ^ { t } = \mathbb { A } ^ { 0 } = S p e c ( \mathbb { K } )$. When $t = 0$we will omit the symbol r from the notation, for instances$\mathcal { P } ( q )$ for$\mathcal { P } ( q , \mathbf { r } )$and${ \mathcal { P } } ^ { * } ( q )$for${ \mathcal { P } } ^ { * } ( q , \mathbf { r } )$

Remark 26.4.

$$
\mathcal {P} (q) = H o m _ {\rho^ {e} (\mathcal {O} _ {Z})} \big (\mathcal {O} _ {Z}, \rho^ {e} (\mathcal {O} _ {Z}) \big)
$$

and

$$
\mathcal {P} ^ {*} (q) = \mathcal {P} (q) \cap D i f f _ {Z} ^ {*} = \{\partial \in \mathcal {P} (q) | \partial (\rho^ {e} (\mathcal {O} _ {Z})) = (0) \}
$$

are global cohenrent sheaf on$Z ( q ) = S p e c ( O _ { Z } )$. They are locally free of ranks$q ^ { n }$and$q ^ { n } - 1$respectively with$n = d i m ( Z )$. We have $\mathcal { P } ^ { * } ( q , \mathbf { r } ) \subset \mathcal { P } ^ { * } ( q )$as a subalgebra determined by the projection map r.

## 27. Bounding pulldown by operators

We go back to an arbitrary retraction, not necessarily “etale”, denoted by$\mathbf { r } ~ : ~ \boldsymbol { \xi } \in ~ S \subset Z \setminus \mathbb { A } ^ { t }$in the sense of Def.(26.1). Let $I ( S ) \subset { \mathcal { O } } _ { Z }$be the ideal of the subscheme$S \subset Z$Recall that we have the sheaf of primitive diferential operators, denoted by$\mathcal { P } ( q , \mathbf { r } )$R with respect to the retraction r by Def.(26.4). It is gloablly defined on U even through “non-etale” points of S. We have the q-base scheme $Z ( q , \mathbf { r } ) = S p e c ( B ( q , \mathbf { r } ) )$defined by Eq.(26.2) and Eq.(26.3), on which $\mathcal { P } ( q , \mathbf { r } )$is a coherent module.

we now introduce the way of bounding the pulldown efect on orders of functions along S when we apply primitive and square nilpotent diferential operators.

Definition 27.1. We define

$$
\mathcal {P} _ {\sigma} (q, \mathbf {r}) =\tag{27.1}
$$

$$
\bigcap_ {\nu - \sigma \geq 0} K e r \left(\mathcal {P} (q, \mathbf {r}) \rightarrow H o m _ {B (q, \mathbf {r})} \left(I (S) ^ {(\nu)}, \mathcal {O} _ {Z} / I (S) ^ {(\nu - \sigma)}\right)\right)
$$

where$J ^ { ( k ) }$denotes the k-th symbolic power of the ideal J in$R _ { \xi } , \mathrm { i . e }$

$$
\bigcap_ {\mathfrak {p} \in m a s s (J ^ {k})} \left(J ^ {k} (R _ {\xi} \setminus \mathfrak {p}) ^ {- 1}\right) \cap R _ {\xi}
$$

with$m a s s ( J ^ { k } )$is the set of minimal associated prime ideals of$J ^ { k }$

$$
\mathcal {P} _ {\sigma} ^ {*} (q, \mathbf {r}) = \mathcal {P} _ {\sigma} (q, \mathbf {r}) \cap \mathcal {P} ^ {*} (q, \mathbf {r}) = \mathcal {P} _ {\sigma} (q, \mathbf {r}) \cap D i f f _ {Z} ^ {*}\tag{27.2}
$$

The number σ can be any integer and it is called bound of degree pulldown or pulldown bound for short. Incidentally −σ may be called bound of degree pullup or pullup bound for short.

Remark 27.1. When the pulldown bound$\sigma \le 0$, we have$\mathcal { P } _ { \sigma } ( q , \mathbf { r } )$maps the unity$1 \in { \mathcal { O } } _ { Z }$to$I ( S ) ^ { ( - \sigma ) }$. For$\sigma = 0$in particular

$$
\mathcal {P} _ {0} (q, \mathbf {r}) = \{\partial \in \mathcal {P} (q, \mathbf {r}) | \partial (I (S) ^ {(\nu)}) \subset I (S) ^ {(\nu)}, \forall \nu \geq 0 \}
$$

Remark 27.2. (1) Choose any$u ^ { \circ } = \left( u _ { 1 } ^ { \circ } . \cdot \cdot , u _ { s } ^ { \circ } \right)$such that$( u ^ { \circ } , w )$ is a regular system of parameters of$R _ { \xi }$

(2) For any choice of$u ^ { \circ }$(which need not be in$I ( S ) )$we have $\mathcal { P } _ { \sigma } ( q , \mathbf { r } ) = \mathcal { P } ( q , \mathbf { r } )$so long as$\sigma \geq ( q - 1 ) ^ { s } + 1$. In fact$\mathcal { P } _ { \sigma } ( q ,  { \mathbf { r } } ) \subset$ $\mathcal { P } ( q , \mathbf { r } ) \subset D i f f _ { \mathcal { O } _ { Z } / \rho ^ { e } ( \mathcal { O } _ { Z } ) [ w ] }$and this last$\rho ^ { e } ( \mathcal { O } _ { Z } ) [ w ]$-module is generated by the elementary diferential operators$\partial _ { u } ^ { ( a ) } , a \in \epsilon ^ { s } ( q )$ We always have$\partial _ { u } ^ { ( a ) } ( I ( S ) ^ { ( \nu ) } ) \subset I ( S ) ^ { ( \nu - | a | ) }$. Note$| a | \leq ( q - 1 ) ^ { s }$

Theorem 27.1. We have

(1)${ \mathcal { P } } _ { \sigma } ( q , \mathbf { r } ) _ { \xi } \subset { \mathcal { P } } _ { \tau } ( q , \mathbf { r } ) _ { \xi }$for all$\sigma < \tau$and

(2)$\mathcal { P } _ { \sigma } ( q , \mathbf { r } ) _ { \xi } = \mathcal { P } ( q , \mathbf { r } ) _ { \xi }$<sub>ξ</sub> for all$\sigma \geq ( q - 1 ) ^ { s } + 1$

(3) For every$\sigma < 0$we have no nonzero idempotent operator belonging to$\mathcal { P } _ { \sigma } ( q , \mathbf { r } )$

Once again we go back to a “etale retraction” case in which we will use symbol D instead of S, say

$$
\mathbf {r}: \xi \in D \subset Z \searrow \mathbb {A} ^ {t}\tag{27.3}
$$

In later applications with respect to a given /<sup>q</sup>-exponent$\mathcal { G }$we often choose a smooth irreducible subscheme$D$of a stratum$S = S ( \xi , \mathcal { G } )$ which is the closure in$Z$of the set

$$
S _ {c l} = \{\eta \in Z _ {c l} | o r d _ {\eta} (\mathcal {G}) = o r d _ {\xi} (\mathcal {G}) \}\tag{27.4}
$$

Such an$S$is a reduced closed subscheme of$Z _ { i }$, which could be singular even at$\xi ,$while$D \subset S$can be a center of permissible blowup for$\mathcal { G }$.

At any rate for the above “etale” retraction we have an explict description of$\mathcal { P } _ { \sigma } ( q , \mathbf { r } )$for any given finite pulldown bound$\sigma$as follows. We choose a regular system of parmeters${ x } = ( u , w )$of$R _ { \xi }$such that D is locally defined by the ideal$( u ) R _ { \xi }$and r is defined by$w$in the manner of Def.(5.2). One notational convenience is used in what follow. Namely any negative powers means “unit” for ideals and systems of elements. For instance, if$c > 0$then$( u ) ^ { - c } R = ( 1 ) R = R$

Theorem 27.2. Assume that r of$E q . ( 2 7 . 3 )$is etale retraction in the sense of Def.(26.2). Pick$( u , w )$of$E q . ( 2 6 . 1 )$with D instead of S. Let $\delta _ { u } ^ { ( a ) }$be the primitive diferential operator sending$u ^ { a } \phi$to$\phi$for each $a \in \epsilon ^ { s } ( q )$and$\phi \in B ( q , \mathbf { r } ) = \rho ^ { e } ( R ) [ w ]$We then have the following expression of the stalk of the$B ( q , \mathbf { r } )$-module$\mathcal { P } _ { \sigma } ( q , \mathbf { r } )$at$\xi .$:

$$
\begin{array}{c} \mathcal {P} _ {\sigma} (q, \mathbf {r}) _ {\xi} = \\ \sum_ {a \in \epsilon^ {s} (q)} \Big ((u) ^ {| a | - \sigma} R _ {\xi} \cap \big (\rho^ {e} (R _ {\xi}) [ w ] \big) \Big) \delta_ {u} ^ {(a)} \end{array}\tag{27.5}
$$

which is equal to

$$
\sum_ {a \in \epsilon^ {s} (q)} \rho^ {e} \Big (I (D, Z) _ {\xi} \Big) ^ {\left.\right] \frac {| a | - \sigma}{q} \left[ \right.} \big (\rho^ {e} (R _ {\xi}) [ w ] \big) \delta_ {u} ^ {(a)}\tag{27.6}
$$

where$] * [$denotes the smallest non-negative integer$\geq *$

Corollary 27.3. We have the same result for${ \mathcal { P } } _ { \sigma } ^ { * } ( q , \mathbf { r } )$as follows.

$$
\begin{array}{c} \mathcal {P} _ {\sigma} ^ {*} (q, \mathbf {r}) _ {\xi} = \\ \sum_ {(0) \neq a \in \epsilon^ {s} (q)} \Big ((u) ^ {| a | - \sigma} R _ {\xi} \cap \big (\rho^ {e} (R _ {\xi}) [ w ] \big) \Big) \delta_ {u} ^ {(a)} \end{array}\tag{27.7}
$$

which is equal to

$$
\sum_ {(0) \neq a \in \epsilon^ {s} (q)} \rho^ {e} \Bigl (I (D, Z) _ {\xi} \Bigr) ^ {\left.\right] \frac {| a | - \sigma}{q} \left[ \right.} \bigl (\rho^ {e} (R _ {\xi}) [ w ] \bigr) \delta_ {u} ^ {(a)}\tag{27.8}
$$

Theorem 27.4. In the case of etale retraction r, there exist nonzero idempotent operators$\{ \delta ( 0 ) \}$contained in$\mathcal { P } _ { \sigma } ( q , \mathbf { r } )$if and only if$\sigma \geq 0$ Those$\delta ( 0 )$are all contained in$\mathcal { P } _ { 0 } ( q , \mathbf { r } )$. They are dependent$o f$the choice of a base u of the ideal$I ( D )$while their residue chasses modulo $\rho ^ { e } ( I ( D ) ) \mathcal { P } _ { \sigma } ( q , \mathbf { r } )$are all the same and uniquely determined by the base algebra$B ( q , { \bf r } ) _ { \xi } \subset R _ { \xi }$

Let us next consider a general case of “separable” retraction$\mathbf { r } : \xi \in \mathbf { \Xi }$ $\begin{array} { r } { S \subset Z \searrow \mathbb { A } ^ { t } = S p e c ( \mathbb { K } [ w ] ) } \end{array}$in the sense of Def.(26.2). We have

$$
\mathcal {P} _ {\sigma} (q, \mathbf {r}) \subset \mathcal {P} (q, \mathbf {r}) \subset D i f f _ {Z / Z (q)}
$$

which are modules over the q-base$B ( q , \mathbf { r } ) = \rho ^ { e } ( \mathcal { O } _ { Z } ) [ w ]$. The number $\sigma$is the pulldown bound in the sense of Def.(27.1). We now proceed to examine their algebraic structure especially in the non-etale cases.

Remark 27.3. Locally at$\xi \in Z$we set the following notation for the set of minimal associated prime divisors mass(I(S)) of$I ( S )$

$$
\text { Define   the   set } P = \{\mathfrak {p} _ {k}, 1 \leq k \leq \mu \}\tag{27.9}
$$

with all p<sub>k</sub> ∈ mass(I(S)), dim(R<sub>ξ</sub>/p) = t, and

$$
l e t \mathfrak {p} = \cap_ {k} \mathfrak {p} _ {k}
$$

$$
T _ {k} = \operatorname{Spec} \left(\mathcal {O} _ {Z} / \mathfrak {p} _ {k}\right) \text { and } T = \cap_ {1 \leq k \leq \mu} T _ {k} = \operatorname{Spec} \left(\mathcal {O} _ {Z} / \mathfrak {p}\right)
$$

which are defined within an appropriate open neighborhood of$\xi \in Z$

Assume$\mu > 0$. For every integer$\nu \geq 0$there exists an element$h ( \nu )$ such that

$$
0 \neq h (\nu) \in \mathbb {K} [ w ] \text {   such   that   } h (\nu) \mathfrak {p} ^ {(\nu)} \subset I (S) ^ {(\nu)}\tag{27.10}
$$

$$
\text { whence   we   must   have } h (\nu) \notin \mathfrak {p} _ {k}
$$

$$
b e c a u s e \mathfrak {p} _ {k} \cap \mathbb {K} [ w ] = (0) f o r e v e r y k
$$

Recall that the “induced map$\ v { r } ^ { \mathfrak { V } } \ S \to \mathbb { A } ^ { t }$is finite and separable at$\xi .$.

Theorem 27.5. Assume that$\mu > 0$in the notatin of$E q . ( 2 7 . 9 )$. Let $\mathbf { t } : \boldsymbol { \xi } \in T \searrow \mathbb { A } ^ { t }$be the retraction obtained from r replacing S by T but keeping the same “projection morphism”. Then for every integer σ we have$\mathcal { P } _ { \sigma } ( q , \mathbf { r } ) _ { \xi } = \mathcal { P } _ { \sigma } ( q , \mathbf { t } ) _ { \xi }$and$\mathcal { P } _ { \sigma } ^ { * } ( q , \mathbf { r } ) _ { \xi } = \mathcal { P } _ { \sigma } ^ { * } ( q , \mathbf { t } ) _ { \xi }$

Lemma 27.6. We have a natural birational homomorphism:

$$
B (q, \mathbf {r}) / \left(\mathfrak {p} _ {k} \cap B (q, \mathbf {r})\right)\rightarrow R _ {\xi} / \mathfrak {p} _ {k}
$$

for every${ \mathfrak { p } } _ { k }$.

Remark 27.4. Consider a retraction r which is separable in the sense of Def.(26.2). We refer to the set of prime ideals$\{ { \mathfrak { p } } _ { k } , 1 \leq k \leq \mu \}$with $\mu > 0$of Eq.(27.9) in Rem.(27.3). We then define retractions$\mathbf { t _ { k } }$and t from r by replacing S by$\dot { T } _ { k } = \dot { S } p e c ( R _ { \xi } / { \mathfrak { p } } _ { k } )$and by$T = S p e c ( R _ { \xi } / { \mathfrak { p } } )$ with${ \mathfrak { p } } = \cap _ { k } { \mathfrak { p } } _ { k }$. Let$C ( \mathbf { r } ) = \mathbb { K } [ w ] \setminus \{ 0 \}$which is a multiplicative group. Let$K ( q , \mathbf { r } )$be$C ( { \bf r } ) ^ { - 1 } B ( q , { \bf r } )$which is the field of fractions of$Z ( q , \mathbf { r } )$ Write C for$C ( \mathbf { r } )$and K for$K ( \mathbf { r } )$for short. We then have the following facts within a neighborhood of$\xi \in Z$

$$
\begin{array}{r l r} {1)} & & {C ^ {- 1} \mathcal {P} (q, \mathbf {r}) = H o m _ {B (q, \mathbf {r})} \Big (\mathcal {O} _ {Z}, K \Big)} \\ & & {C ^ {- 1} \mathcal {P} _ {\sigma} (q, \mathbf {t} _ {k}) = \{\partial \in C ^ {- 1} \mathcal {P} (q, \mathbf {t} _ {k}) | \partial (C ^ {- 1} \mathfrak {p} _ {k} ^ {\nu}) \subset C ^ {- 1} \mathfrak {p} _ {k} ^ {\nu - \sigma} \}} \\ & & {C ^ {- 1} \mathcal {P} _ {\sigma} (q, \mathbf {t}) = \{\partial \in C ^ {- 1} \mathcal {P} (q, \mathbf {t}) | \partial (C ^ {- 1} \mathfrak {p} ^ {\nu}) \subset C ^ {- 1} \mathfrak {p} ^ {\nu - \sigma} \}} \end{array}\tag{27.11}
$$

It should be noted here that by applying$C ^ { - 1 }$the prime ideals become maximal ideals and hence their “symbolic powers” are the same as ordinary powers. The same holds for the intersection of those primes.

Remark 27.5. We focus our attention to an afine open neighborhood of$\xi \in Z$, suitably small. So let us assume$Z = S p e c ( A )$with a finitely generated K-algebra A and also view${ \mathfrak { p } } _ { k }$and p as prime ideals in A. We may assume$B ( q , \mathbf { r } ) = \rho ^ { e } ( A ) [ w ]$and$\mathbf { r } : Z  \bar { \mathcal { P } } = S p e c ( \mathbb { K } [ w ] )$is smooth everywhere with$w = ( w _ { 1 } , \cdot \cdot \cdot , w _ { t } )$. Let$C = \mathbb { K } [ w ] \setminus \{ 0 \}$in accord with Rem.(27.4). Then we have

$$
\begin{array}{c} \text {For each k} \\ \exists u (k) = (u (k) _ {1}, \dots , u (k) _ {s}) \text {with} C ^ {- 1} \mathfrak {p} _ {k} = (u (k)) C ^ {- 1} A \end{array}\tag{27.12}
$$

where$s + t = n = d i m _ { \xi } ( Z )$. Let us define

$$
\delta (0) _ {k} = i d e n t i t y - \sum_ {0 \neq a \in \epsilon^ {s} (q)} u (k) ^ {a} \delta_ {u (k)} ^ {(a)}\tag{27.13}
$$

The operator$\delta ( 0 ) _ { k }$is “primitive” in the sense that it is idempotent and it annihilates all the monomials$u ( k ) ^ { a }$with$0 \neq a \in \epsilon ^ { s } ( q )$. There by chinese remainder technique we can choose the parameters$u \ =$ $\left( { { u } _ { 1 } } , \cdots , { { u } _ { t } } \right)$in the following manner:

$$
\begin{array}{c} u _ {j} \in \mathfrak {p} \subset R _ {\xi}, \forall j, a n d \\ u = u (k) o f E q s. (2 7. 1 2) + (2 7. 1 3), \forall k. \end{array}\tag{27.14}
$$

We then define the following idempotent operator.

$$
\delta_ {u} ^ {(0)} = i d - \sum_ {0 \neq a \in \epsilon^ {s} (q)} u ^ {a} \delta_ {u} ^ {(a)}\tag{27.15}
$$

which makes a good sense in$C ^ { - 1 } \mathcal { P } ( { q } , \mathbf { t } )$of Eq.(27.11).

Remark 27.6. With u of Eq,(27.14), we can have an open neighborhood $U$of$\xi \in Z$such that

(1) For every k let$V _ { k } ^ { \circ }$be the set of those points of$U \cap T _ { k }$at which the retraction$\mathbf { t } _ { k }$is etale. Then$V _ { k } ^ { \circ }$is open dense in$U \cap T _ { k }$for every$k$. (Every separable finite morphism is generically etale.)

(2) We then have an open dense subset$V _ { k }$of$V _ { k } ^ { \circ }$such that$\delta ( 0 )$of Eq.(27.15) is a primitive idempotent in$\mathcal { P } ( q , \mathbf { t } _ { k } )$with respect to the parameters$u = u ( k )$at every point of$V _ { k }$

(3) For each such$\delta ( 0 )$we define an ideal$\mathbf { \Sigma } ] \subset B ( q , \mathbf { r } )$by

$$
\rfloor = \{f \in R _ {x} i \mid f \delta (0) \in \mathcal {P} (q, \mathbf {r}).\tag{27.16}
$$

We see that$S p e c ( R _ { \xi } / \operatorname { \lrcorner } R _ { \xi } ) \cap V _ { k } = \varnothing$for every k.

## 28. Generic down theorems

The theorems in this section are used in the study of generic-down phenomena in the sense of$\operatorname { E q . } ( ? ? )$of Def.(??). It will be seen that Ex.(16.1) is a simple but typical “generic-down” case. Indeed a general “generic-down” phenomena is composed of such simple ones in a certain sense that we want to clarify in this section.

Remark 28.1. Let D be a reduced irreducible subscheme of$Z$and assume that it is a generic-down subscheme for$\mathrm { ~ a ~ } / ^ { q } .$-exponent$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$ in$Z$in the sense of Def.(??), that is

$$
0 <   l = \operatorname{ord} _ {\zeta} (\mathcal {G}) <   m = \operatorname{ord} _ {\eta} (\mathcal {G})\tag{28.1}
$$

where$\zeta$denotes the generic point of$D$and the equality for m is for all $\eta \in D \cap Z _ { c l }$in accord with Eq.(??).

Remark 28.2. Pick and fix a point$\xi \in D \cap Z _ { c l }$such that D is smooth at ξ and$o r d _ { \xi } ( \mathcal { G } ) = m$. Then pick a regular system of parameters ${ x } = ( u , w )$of$R _ { \xi }$which is subject to the following condition.

$$
(u) R _ {\xi} \text {   is   the   ideal   of   } D \subset Z \text {   at   } \xi .\tag{28.2}
$$

In later applications, D may be given as the center of a blowup permissible for$\mathcal { G }$as well as for the given NC data Γ. If this is the case we may require$( u , w )$contains z where z denotes a system of parameters defining those components of Γ passing through$\xi$. However in the following general theorems it is important that no more than Eq.(28.2) is imposed on our choice of${ x } = ( u , w )$in search of invariants and globaliation in dealing with generic down singularities.

We will write$\boldsymbol { u } = ( u _ { 1 } , \cdots , u _ { s } )$and$w = ( w _ { 1 } , \cdot \cdot \cdot , w _ { t } )$. Write$x =$ $( x _ { 1 } , \cdot \cdot \cdot , x _ { n } ) = ( u , w )$with$n = s + t = d i m Z$

The choice of$( u , w )$determines the following local$\mathrm { { \^ { 6 } e t a l e } } ^ { , 5 }$retraction.

$$
\mathbf {r}: \xi \in D \subset Z \searrow \mathbb {A} ^ {t} = S p e c (\mathbb {K} [ w ])\tag{28.3}
$$

in the sense of Def.(26.2). Recal that we then have the q-base algebra $B ( q , \mathbf { r } )$in the sense of Eq.(26.2) and the operator algebra$\mathcal { P } ( q , \mathbf { r } )$in the sense of Def.(26.4). Recall its relation with the parameters$( u , w )$in the manner of Eq.(26.6). We also have$\mathcal { P } _ { \sigma } ( q , \mathbf { r } )$with pulldown bound σ. Refer to Def.(27.1), Eq.(27.1) and Rem.(27.2).

We now proceed to state and prove the theorems and lemmas about “generic down” phenomena. We know that$R _ { \xi }$is a$\rho ^ { e } ( R )$-module freely generated by$\{ \bar { u ^ { a } w ^ { b } } , ( a b ) \in \epsilon ^ { n } ( q ) \}$. We then choose g of$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { a } ^ { q } \right)$ as follows. With repect to the$( u , w )$we have the$\ast _ { - } f u l l$idempotent q-operator${ \mathfrak { d } } ^ { * }$in the sense of Eq.(??) of Def.(??)). For the given$\mathcal { G }$we can replace g by${ \mathfrak { d } } ^ { * } ( \mathbf { g } )$. In fact${ \mathfrak { d } } ^ { * } ( \mathbf { g } ) - \mathbf { g }$belongs to$\rho ^ { q } ( R _ { \xi } )$. In efect$\mathfrak { d } ^ { * }$ annihilates all the q-the power terms and keeps the other terms with respect to the variables$( u , w )$. We thus have

$$
\mathfrak {d} ^ {*} (\mathbf {g}) = \sum_ {(a b) \in \epsilon^ {n} (q)} d _ {a b} ^ {q} u ^ {a} w ^ {b}\tag{28.4}
$$

with$d _ { 0 0 } = 0$and$d _ { a b } \in R$. We then have

$$
m = \operatorname{ord} _ {\xi} \left(\mathfrak {d} ^ {*} (\mathbf {g})\right) = \min \left\{\left| a \right| + \left| b \right| + \operatorname{ord} _ {\xi} \left(d _ {a b}\right) q \right\}
$$

$$
a n d l = o r d _ {\zeta} (\mathfrak {d} ^ {*} (\mathbf {g})) = \min \{| a | + o r d _ {\zeta} (d _ {a b}) q \}
$$

The numbers$m$and l are thus defined and indpendent of the choice of $( u , w )$so long as the condition Eq.(28.2) is satisfied.

In what follows for the sake of notational simplicity we assume to have chosen$\mathbf { g }$in such a way that${ \mathfrak { d } } ^ { * } ( \mathbf { g } ) \mathbf { g }$. With this g we proceed ou reasonings from now on.

$$
\Delta = \left\{(a b) \mid | a | + o r d _ {\zeta} (d _ {a b}) q <   m \right\}\tag{28.5}
$$

Note that the set$\Delta$is not empty because of the “generic down” assumption$l < m$

Lemma 28.1. Pick any$( a b ) \in \epsilon ^ { n } ( q )$such that$a \neq 0$. We then claim

$$
o r d _ {\zeta} (d _ {a b} ^ {q} u ^ {a} w ^ {b}) = | a | + o r d _ {\zeta} (d _ {a b}) q \geq m.
$$

Therefore we must have$a = 0$for all$( a b ) \in \Delta$and

$$
l = \min \{o r d _ {\zeta} (d _ {0 b}) q | (0 b) \in \Delta \}
$$

It follows that we have$l = A q$with an integer$A > 0$

Lemma 28.2. We have$m - l < q$. Hence m is not divisible by$q .$

Lemma 28.3. We have$l = A q = o r d _ { \zeta } ( d _ { 0 b } { } ^ { q } w ^ { b } )$for every$( 0 b ) \in \Delta$

Lemma 28.4. Pick any one$( 0 b ) \in \Delta$and write$\begin{array} { r } { w ^ { b } = \prod _ { 1 \leq j \leq t } w _ { j } ^ { b _ { j } } } \end{array}$ Then we have:

(1) There always exists at least one j with$b _ { j } > 0$

(2) If$b _ { j } > 0$then there exist integers$e ( b , j ) \geq 0$and$c ( b , j ) \geq 1$ such that$b _ { j } = c ( b , j ) p ^ { e ( b , j ) }$and$p \ \chi c ( b , j )$

(3) If$b _ { j } > 0$we have$p ^ { e ( b , j ) } \ge m - l$

(4) If$o r d _ { \xi } ( d _ { 0 b } ^ { q } w ^ { b } ) = m$then b has one and only one nonzero component$b _ { j }$which is equal to$p ^ { e _ { j } }$

Definition 28.1. With the set$\Delta$of Eq.(28.5) we define

$$
g (0) = \sum_ {(a b) \in \Delta} d _ {a b} ^ {q} u ^ {a} w ^ {b} = \sum_ {(0 b) \in \Delta} d _ {0 b} ^ {q} w ^ {b}
$$

of which the last equality if by Lem.(28.1).

Theorem 28.5. The summand$g ( 0 )$of g has the following properties.

(1)$o r d _ { \zeta } ( g ( 0 ) ) = l = A q$with a positive integer A

(2) and$A q < m \leq o r d _ { \xi } ( g ( 0 ) )$

(3) There exists a nonempty finite set B of maps from$[ 1 , t ]$to$\mathbb { Z } _ { 0 }$ which has the following properties.

$$
g (0) = \sum_ {\beta \in B} g (0) _ {\beta} \text {with} g (0) _ {\beta} = \phi_ {\beta} ^ {q} \prod_ {1 \leq i \leq t} w _ {i} ^ {q _ {*} \beta (i)}\tag{28.6}
$$

where

(a) For every$\beta \in B$there exists at least one i with$\beta ( i ) > 0$

(b)$\beta ( i )$is not divisible by p for at least one pair$( \beta , i )$

(c)$q _ { * }$is a unique power of p and we have$q > q _ { * } \geq m - A q$

(d)$\phi _ { \beta } \in I _ { \xi } { } ^ { A }$and o$\cdot d _ { \zeta } ( \phi _ { \beta } ) = A$for every$\beta \in B$

(e)$o r d _ { \xi } ( g ( 0 ) _ { \beta } ) \ge m \ f o r \ a l l \ \beta \in B$

(4) We always have$o r d _ { \xi } ( g ( 0 ) ) \ge m$ (5) Suppose we had$o r d _ { \xi } ( g ( 0 ) ) = m$. (We may not have the equality. See Ex.(28.1) below.) For$\beta \in B$with o$r d _ { \xi } ( g ( 0 ) _ { \beta } ) = m$we have one and only one index k with$\beta ( k ) \neq 0$and$\beta ( k ) = 1$, so that$g _ { \beta } = \phi _ { \beta } ^ { ~ q } w _ { k } ^ { q _ { * } }$

Let us next define

$$
\Delta^ {\dagger} = \left\{(a b) \mid m \leq | a | + o r d _ {\zeta} (d _ {a b}) q <   l + q \right\}\tag{28.7}
$$

Note that this set$\Delta ^ { \dagger }$could be empty unlike$\Delta$. Examples are easy to find either for$\Delta ^ { \dagger } = \emptyset$or for$\Delta ^ { \dagger } \neq \emptyset$

Example 28.1. Let$\begin{array} { r } { \mathbf { g } = u _ { 1 } ^ { A q } w _ { 1 } + c u _ { 2 } ^ { A q + 1 } + u _ { 3 } ^ { ( A + 1 ) q } w _ { 2 } } \end{array}$where$m = A q + 1$ and$l = A q$while we let either$c = 0 \ \mathrm { o r } \ c = 1$

Definition 28.2. With$\Delta ^ { \dagger }$as above we define

$$
\begin{array}{c} g (0) ^ {\dagger} = \sum_ {(a b) \in \Delta^ {\dagger}} d _ {a b} ^ {q} u ^ {a} w ^ {b} \\ a n d g (1) = \mathbf {g} - g (0) - g (0) ^ {\dagger} \end{array}
$$

Lemma 28.6. We have that$g ( 1 )$is the sum of those terms${ d _ { a b } } ^ { q } u ^ { a } w ^ { b }$ having or$\cdot d _ { \zeta } ( d _ { a b } ) q + | a | \geq ( A + 1 ) q$. We also have

(1)$o r d _ { \zeta } ( g ( 0 ) ) = A q = l < m = \operatorname* { m i n } \{ o r d _ { \xi } ( g ( 0 ) ) , o r d _ { \xi } ( g ( 0 ) ^ { \dagger } \}$

(2)$m \le o r d _ { \zeta } ( g ( 0 ) ^ { \dagger } ) \le o r d _ { \xi } ( g ( 0 ) ^ { \dagger } )$

$$
m <   (A + 1) q = l + q \leq o r d _ {\zeta} (g (1)) \leq o r d _ {\xi} (g (1)). \tag {3}
$$

Definition 28.3. Let us define the partial sum$g ( 1 ) ^ { + }$of$g ( 1 )$to be the sum of those terms${ d _ { a b } } ^ { q } u ^ { a } w ^ { b }$belonging to$\rho ^ { e } ( R _ { \xi } ) [ v ]$as well as having $o r d _ { \zeta } ( d _ { a b } ) q + | a | \geq ( A + 1 ) q$. Let us then define$g ( 1 ) = g ( 1 ) ^ { + } + g ( 1 ) ^ { - }$ after the notation of Def.(28.2) and Lem.(28.6). Moreover we introduce the fllowing decomposition:

$$
\begin{array}{r c l} G (+) & = & g (0) + g (1) ^ {+} \text { and } G (-) = g (0) ^ {\dagger} + g (1) \\ & & \text { so   that } \mathbf {g} = G (-) + G (+) \end{array}\tag{28.8}
$$

Theorem 28.7. We summerise the preceeding definitions.

$$
\begin{array}{c} G (+) = g (0) + g (1) ^ {+} \in \rho^ {e} (R _ {\xi}) [ v ] \\ G (-) = g (0) ^ {\dagger} + g (1) ^ {-} \in \sum_ {0 \neq a \in \epsilon^ {s} (q)} u ^ {a} \rho^ {e} (R _ {\xi}) [ v ] \end{array}\tag{28.9}
$$

and

$$
\mathfrak {d} _ {x} ^ {*} \mathbf {g} = G (+) + G (-) f o r \mathcal {G} = (\mathbf {g} \| / ^ {q})
$$

## 29. Differentiation along generic-down strata

We have defined the summand$g ( 0 )$of${ \mathfrak { d } } ^ { * } ( \mathbf { g } )$by Def.(28.1) and described its properties by Eq.(28.6) of Th.(28.5). We have then defined $G ( + )$and$G ( - )$by Eq.(28.8) and Lem.(28.6). We have thus obtained the following “structural decomposition”:

$$
\mathfrak {d} ^ {*} (\mathbf {g}) = G (+) + G (-) \text {   for   } \mathcal {G} = (\mathbf {g} \|, / ^ {q})\tag{29.1}
$$

in the sense of Def.(28.3) followed by Th.(28.7).

In search of some invariants hidden in each of the summands of Eq.(29.1), we are going to examine their characters by means of retractions r of Eq.(28.3) with the operator algebras${ \mathcal { P } } ( q , \mathbf { r } )$and${ \mathcal { P } } ^ { * } ( q , \mathbf { r } )$of Def.(26.4) with respect to “q-base algebras”$B ( q , \mathbf { r } )$of Eq.(26.2).

In the “etale” retraction case, the operator algebras and the q-base algebras depend upon the choice of the parameters${ \boldsymbol { x } } = ( u , w )$of$R _ { \xi }$ subject to Rem.(28.2). Refer to Eq.(26.6) in connection with Th.(5.3) and Eq.(??) of Def.(5.2).

We will make use of$\mathcal { P } _ { \sigma } ( q , \mathbf { r } )$and${ \mathcal { P } } _ { \sigma } ^ { * } ( q , \mathbf { r } )$with “pulldown bound” σ in the sense of$\mathrm { E q . ( 2 7 . 1 ) }$of Def.(27.1). They will be used in combination with the$\ast _ { - } f u l l$idempotent$q { \mathrm { - } } d i f f$erentiation${ \mathfrak { d } } ^ { * }$in the sense of Eq.(??) of Def.(??) with respect to${ x } = ( u , w )$. This operator$\mathfrak { d } ^ { * }$depends upon the choice of x and will be written as$\mathfrak { d } _ { x }$. Th.(4.1) describes the dependence on x.

Remark 29.1. Sometimes some symbols require clearer indication of their dependence on the choice of the parameters${ x } = ( u , w )$, while some other times we prefer to use even simpler symbols when the dependence is apparent or irrelevant for the context.

(1) For instance the q-base algebra for a retraction r may be witten $B ( q , w )$instead of$B ( q , \mathbf { r } )$when the projection map is defined by w. Note that diferent w can give the same$B ( q , w ) \subset R _ { \xi }$. If we have the same$B ( q , w )$and we are not interested in any particular w we may write$B ( q , t )$for$B ( q , w )$with the dimension t of the target space$\mathbb { A } ^ { t }$of r.

(2) The primitive operators$\delta _ { u } ^ { ( a ) } , a \in \epsilon ^ { s } ( q )$form a free base of $\mathcal { P } ( q , \mathbf { r } ) _ { \xi }$as$B ( q , t )$-module. The base depends not only upon the choice of the retraction r but also an ideal base u of$I ( S ) _ { \xi }$, although the operator algebras$\mathcal { P } ( q , \mathbf { r } ) _ { \xi }$and its subalgebra${ \mathcal { P } } ^ { * } ( q , \mathbf { r } ) _ { \xi }$ are uniquely defined by$B ( q , \mathbf { r } )$. However the primitive idempotent operators$\delta _ { u } ^ { ( a ) }$delicately depends upon the choice of u as well as$B ( q , w )$. To show the dependence we will write$\delta _ { u / w } ^ { ( a ) }$ instead of$\delta _ { u } ^ { ( a ) }$. For instance Eq.(27.15) will be written as

$$
\delta_ {u / w} ^ {(0)} = i d - \mathfrak {d} _ {u / w} ^ {*} = i d - \sum_ {0 \neq a \in \epsilon^ {s} (q)} u ^ {a} \delta_ {u / w} ^ {(a)}\tag{29.2}
$$

where the${ \mathfrak { d } } _ { u / w } ^ { * }$is the \*-full ID in the sense of of$\operatorname { E q . } ( ? ? ) )$inside $D i f f _ { R _ { \xi } / B ( q , w ) }$with respect to u.

Recall that the \*-full ID$\mathfrak { d } _ { u / w } ^ { * }$has the property:

$$
\mathfrak {d} _ {u ^ {\prime} / w} ^ {*} (h) - \mathfrak {d} _ {u / w} ^ {*} (h) \in B (q, w) \text {   for   all   } h \in R _ {\xi}\tag{29.3}
$$

for any other choice of a base$u ^ { \prime }$of$I ( S ) _ { \xi }$

Incidentally$\mathfrak { d } _ { u / w } ^ { * }$is diferent from$\mathfrak { d } _ { x } ^ { * }$with$x = ( u , v )$. The latter is the \*-full ID inside$D i f f _ { R _ { \xi } / \mathbb { K } }$with respect to x. To be precise

$$
\mathfrak {d} _ {\dot {x}} ^ {*} (h) - \mathfrak {d} _ {x} ^ {*} (h) \in \rho^ {e} (R _ {\xi}) \text {   for   all   } h \in R _ {\xi}\tag{29.4}
$$

for any other regular system of parameters ˙x of$R _ { \xi }$.

Our task is to search for some “invariants” out of$\mathcal { G } = \left( \mathbf { g } \lVert \boldsymbol { \mu } \right)$by means of the application of$\delta _ { u / w } ^ { ( 0 ) }$to$\mathbf { g } .$. We fix a smooth irreducible $S \subset Z$and focus our attention to the efect upon the operators$\delta _ { u / w } ^ { ( a ) }$ with respect to the changes of the retractions r or of the parameters $( u , w )$

By virtue of Lem.(26.1) it is enough to examine the efect by steps of the following two kinds.

## Remark 29.2. Step (1):

This is the case in which q-base algebra$B ( q , t )$is kept the same by the change of$( u , w )$

Then the operator algebras$\mathcal { P }$and${ \mathcal { P } } ^ { * }$remain the same under such a change of w. Therefore we don’t lose generality by using the same w. What should then be examined is the efect on the operators$\delta ^ { ( a ) }$by the change of the ideal base u of$I ( S ) _ { \xi }$, say from$u$to another base ˙u. The change from u to$\dot { u }$is expressed by writing each$\dot { u } _ { i }$as a$B ( q , t )$-linear combination of the$\{ u ^ { b } , b \in \epsilon ^ { s } ( q ) \}$. Recall that$R _ { \xi }$as$B ( q , t )$-module is freely generated by$\{ \dot { u } ^ { a } , a \in \epsilon ^ { s } ( q ) , \}$as well as by$\{ u ^ { b } , b \in \epsilon ^ { s } ( q ) \}$

$$
\begin{array}{c} \text {Write} \dot {u} ^ {a} = \sum_ {b \in \epsilon^ {s} (q)} c (a b) u ^ {b} \\ = c (a 0) + \sum_ {0 \neq b \in \epsilon^ {s} (q)} c (a b) u ^ {b} \\ \text {where} \\ c (a b) \in B (q, w) \cap I (D) ^ {| a | - | b |} \text {and hence} \end{array}\tag{29.5}
$$

$$
o r d _ {I (D)} (c (a b)) \geq q ] \frac {| a | - | b |}{q} [\tag{29.6}
$$

Recall that for every integer$\nu \geq 0$we have$B ( q , t ) \cap I ( D ) ^ { \nu } = \rho ^ { e } ( I ( D ) ) ^ { q ] \frac { \nu } { q } [ }$ Thus we have

$$
e i t h e r | b | \geq | a | o r c (a, b) \in \rho^ {e} (I (D)) B (q, t).\tag{29.7}
$$

Note that$\dot { u } ^ { a } \in I ( D )$if and only if$| a | > 0$. If$a = 0$then$c ( 0 0 ) ~ = ~ 1$ and$c ( 0 b ) = 0 , \forall b$

Remark 29.3. Step (2):

This is the case in which w is replaced by$w = \dot { w } - f$where$f =$ $( f _ { 1 } , \cdots , f _ { t } )$with$f _ { i } \in ( u ) R _ { \xi } , \forall i$. We are keeping the same u but the q-base algebra must be changed from$B ( q , \dot { w } )$to$B ( q , w )$

Note that$B ( q , \dot { w } ) = \rho ^ { e } ( R _ { \xi } ) [ \dot { w } ]$as$\rho ^ { e } ( R _ { \xi } )$-module is generated by monomials$\dot { w } ^ { b } , b \in \epsilon ^ { t } ( q )$. Now$\dot { w } ^ { b }$is written in terms of w as

$$
\dot {w} ^ {b} = (w + f) ^ {b} = w ^ {b} + \Phi_ {b}\tag{29.8}
$$

where

$$
\Phi_{b} = \sum_{\substack{0\neq d\in \epsilon^{t}(q)\\ b - d\in \mathbb{Z}_{0}^{t}}}\binom {b}{d}w^{b - d}f^{d}\in (f)R_{\xi}\subset I(D)
$$

For each$a \in \epsilon ^ { s } ( q )$and$0 \neq d \in \epsilon ^ { t } ( q )$we can write

$$
u ^ {a} f ^ {d} = \sum_ {k \in \epsilon^ {s} (q)} u ^ {k} \psi_ {a d k} ^ {q} w i t h \psi_ {a d k} \in R _ {\xi}\tag{29.9}
$$

and then we must have

$$
\begin{array}{r l} {| k | + o r d _ {I (D)} (\psi_ {a d k}) q \geq | a | + o r d _ {I (D)} (f ^ {d}) \geq | a | + | d |} \\ {\text {where we have only d with} | d | \geq 1} \end{array}
$$

For the inequlities above we use the fact that$u ^ { k }$are$B ( q , w )$-linearly independent. We let

$$
\Psi_{abk} = \sum_{\substack{0\neq d\in \epsilon^{t}(q)\\ b - d\in \mathbb{Z}_{0}^{t}}}\binom {b}{d}w^{b - d}\psi_{adk}^{q}\tag{29.10}
$$

and then we have

$$
\begin{array}{r c l} u ^ {a} \dot {w} ^ {b} = & u ^ {a} w ^ {b} + \sum_ {k \in \epsilon^ {s} (q)} u ^ {k} \Psi_ {a b k} \\ w h e r e & \Psi_ {a b k} \in B (q, w) a n d \end{array}\tag{29.11}
$$

$$
o r d _ {I} (\Psi_ {a b k}) \geq | a | - | k | + 1 f o r a l l (a, b, k)
$$

$$
b e c a u s e | d | \geq 1 i n E q. (2 9. 1 0)
$$

By taking$\rho ^ { e } ( R _ { \xi } )$)-linear combination we can extend the first equality of Eq.(29.11) to its full generality because we have

$$
B (q, \dot {w}) = \sum_ {b \in \epsilon^ {s} (q)} \dot {w} ^ {b} \rho^ {e} (R _ {\xi}) a n d B (q, w) = \sum_ {b \in \epsilon^ {s} (q)} w ^ {a} \rho^ {e} (R _ {\xi})
$$

Thus we pick any system$h = ( h _ { b } ) , b \in \epsilon ^ { t } ( q )$, with$h _ { b } \in R _ { \xi }$. Then let $\begin{array} { r } { \begin{array} { r } { h ( \dot { w } ) = \sum _ { b \in \epsilon ^ { t } ( a ) } \dot { w } ^ { b } ( h _ { b } ) ^ { q } } \end{array} } \end{array}$and$\begin{array} { r } { \begin{array} { r } { h ( w ) = \sum _ { b \in \epsilon ^ { t } ( q ) } w ^ { b } ( h _ { b } ) ^ { q } } \end{array} } \end{array}$. Let$\Psi _ { a k } ( h ) =$ $\begin{array} { r } { \sum _ { b \in \epsilon ^ { t } ( q ) } \Psi _ { a b k } ( h _ { b } ) ^ { q } } \end{array}$. The generalized formula is then as follows.

$$
u ^ {a} h (\dot {w}) = u ^ {a} h (w) + \sum_ {k \in \epsilon^ {s} (q)} u ^ {k} \Psi_ {a k} (h)\tag{29.12}
$$

where$h ( w ) \in B ( q , w )$and$\Psi _ { a k } ( h ) \ \in \ B ( q , w )$

$$
\operatorname{ord} _ {I (D)} \left(\Psi_ {a k} (h)\right) \geq | a | - | k | + 1 \text {   for   all   } (a, k)
$$

where we are only interested in the case of$| a | > 0$

Theorem 29.1. Assume that S is smooth irreducible with dim$S = t$ and pick a closed point$\xi \in S$. Let us choose a regular system of parameters${ x } = ( u , w )$of$R _ { \xi }$such that u is an ideal base of$I = I ( D , Z ) _ { \xi }$ $W e$also pick any other regular system of parameters$\dot { x } = ( \dot { u } , \dot { w } )$with $I = ( \dot { u } ) R _ { \xi }$. Let

$$
\nabla \left(\frac {\dot {u} / \dot {w}}{u / w}\right) = \delta_ {\dot {u} / \dot {w}} ^ {(0)} - \delta_ {u / w} ^ {(0)}
$$

Then for every$G \in I ^ { m }$we have

$$
\begin{array}{r c l} \nabla \Big (\frac {\dot {u} / \dot {w}}{u / w} \Big) (G) & \subset & \rho^ {e} (I) ^ {q ] \frac {m + 1}{q} [} R _ {\xi} \\ \delta_ {u / w} ^ {(0)} \nabla \Big (\frac {\dot {u} / \dot {w}}{u / w} \Big) (G) & \subset & \rho^ {e} (I) ^ {q ] \frac {m + 1}{q} [} B (q, w) \end{array}\tag{29.13}
$$

$$
\begin{array}{l} \text {and} \\ \bigcap_ {\dot {u} / \dot {w}} \nabla \Big (\frac {\dot {u} / \dot {w}}{u / w} \Big) (G) \in \rho^ {e} (I) ^ {q ] \frac {m + 1}{q} [} \subset \rho^ {e} (I) \end{array}
$$

Remark 29.4. Let D be a smooth irreducible subscheme of$Z$and let $\xi \in D$be a closed point. Let us pick and fix an etale retraction

$$
\mathbf {r}: \xi \in D \subset Z \searrow \mathbb {A} ^ {t} w i t h t = d i m D.\tag{29.14}
$$

Choose and fix w which defines the projection morphism r and denote the q-base algebra of r by

$$
B (q) = B (q, \mathbf {r}) = (\rho^ {e} (R _ {\xi})) [ w ]\tag{29.15}
$$

Let us then pick and fix an ideal base u of$I = I ( D , Z ) _ { \xi }$. Denote the primitive operator algebra of r with pulldown bound 0 as follows.

$$
\mathcal {P} _ {0} (q) = \mathcal {P} _ {0} (q, \mathbf {r}) = \mathcal {P} _ {0} (q, u / w)\tag{29.16}
$$

We see that this operator algebra contain the following primitive idempotent operator.

$$
\delta (0) = \delta_ {u / w} ^ {(0)} = i d - \sum_ {0 \neq a \in \epsilon^ {s} (q)} u ^ {a} \delta_ {u / w} ^ {(a)}\tag{29.17}
$$

which is determined by the choice of parameters$( u , w )$

Theorem 29.2. With the notation of R:prep-refer-notas Rem.$( 2 9 . 4 )$ the following residue class is uniquely determined by$\xi \in D$

$$
\delta (0) \text {   mod   } \rho^ {e} (I (D, Z) _ {\xi}) \mathcal {P} _ {0} (q)\tag{29.18}
$$

Namely it is independent of the choice$o f \left( w , u \right)$. The precise meaning is as follows: Pick any σ defining an etale retraction with the same $\xi \in D$(instead of w) and any ideal base v of I (instead of u) then we have

$$
\delta_ {v / \sigma} ^ {(0)} - \delta (0) \in (\rho^ {e} (I)) \mathcal {P} _ {0} (q).\tag{29.19}
$$

(29.20)

$$
\begin{array}{r} \mathcal {D} _ {u / w} (\mathbf {g}) = g (0) + \mathcal {D} _ {u / w} (g (0) ^ {\dagger} + g (1)) \\ w h e r e \mathcal {D} _ {u / w} (g (0) ^ {\dagger} + g (1)) \in \rho^ {e} (I (S)) ^ {A + 1} B (q, t) \end{array}\tag{29.21}
$$

$$
g(0) = \sum_{\substack{a\in \epsilon^{s}(q),|a| = A\\ b\in \mathbb{Z}_{0}^{t}}}d_{ab}u^{aq}w^{bq_{*}}
$$

which is the$g ( 0 )$derived from$\mathfrak { d } _ { x } ^ { * } ( \mathbf { g } )$following the procedure of Def.(28.1). Moverover we have

$$
\mathfrak {d} _ {x} ^ {*} (g (0)) = g (0)
$$

It follows that then ideal exponent

$$
\left(\left. \left(\mathcal {D} _ {u / w} (\mathbf {g}) + \rho^ {e} (I (S)) ^ {(A + 1)} B (q, \mathbf {r})\right) \mathcal {O} _ {Z}, q\right) \right.
$$

is independent of the choice of$\boldsymbol { x } = ( u , w )$and uniquely determined by $\mathcal { G }$and$S \subset Z$, provided$S$is smooth generic-down of dimension t.

## 30. /<sup>q</sup>-singular derivatives

We examine the transform of G by a permissible blowup with centers $D \ni \xi$in the sense of Def.(18.2) and Def.(18.4). Special care about permissibility is needed when D is contained in a generic down stratum $S$of$S i n g ( \mathcal { G } )$). We thus introduce the technique which will be called$/ ^ { q } -$ derivatives along$S$which is analogous to infinitesimal deformation of S inside$Z .$. The /<sup>q</sup>-derivatives will play an important role as techniques of choosing a better center for blowup in order to produce more desirable results in the transformed singularities.

To define /<sup>q</sup>-derivatives we make use of the square nilpotent diferential operators defined by Def.(5.1) with Eq.(??). We also refer to Th.(5.2) and Th.(5.3).

Let us now consider a /<sup>q</sup>-exponent$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \big / \vphantom { \left( \mathbf { g } \right) } \right)$in$Z$and a local “separable” retraction$\mathbf { r } : \boldsymbol { \xi } \in D \subset Z \setminus \mathbb { A } ^ { t }$in the sense of Def.(26.1). We propose to introduce the notion of /<sup>q</sup>-derivatives of$\mathcal { G }$with respect to a local separable retaction as above. (See Def.(30.1) and Def.(30.2) below.)

Although we need definitions with respect to general separable retractions, it is important to clarify the structure of /<sup>q</sup>-derivatives when the retractions are “etale” and hence$D$is smooth of dimension n at$\xi .$ In this case we have an open neiborhood$U$of$\xi \in Z$satisfying the conditions described in Rem.(26.2). There we can make use of Def.(5.2), Eq.(??), Eq.(??) and Def.(??). Namely the$^ { \prime \ell } e t a l e ^ { \prime \prime }$retraction properties of Def.(26.1) are maintained at every point$\eta \in D \cap U$with a chosen and fixed projection morphism$\mathbf { r } : Z \to { \mathbb { A } } ^ { t }$. Also refer to Rem.(26.2) followed by Def.(??).

Remark 30.1. We now summerize the basic assumptions and known results in the case of$\mathrm { ^ { 6 } e t a l e ^ { 9 } }$retactions as follows.

(1) The morphism$\mathbf { r } : Z  \mathbb { A } ^ { t }$is smooth at every point of$U$, and

(2) r induces an etale morphism$U \cap D \to \mathbb { A } ^ { t }$

(3) For any closed point$\eta \in U \cap D , ( u , w - w ( \eta ) )$is a regular system of parameters of$R _ { \eta }$where u generates the ideal$I ( D , Z ) _ { \eta }$and w defines the etale morphism$U \cap D \to \mathbb { A } ^ { t }$

(4)${ \mathcal { P } } ^ { * } ( q , \mathbf { r } )$is a sheaf of algebras on$Z | U$which,locally at every η as above, is freely generated by those square-nilpotent diferential operators$\delta ^ { ( a ) } , 0 \neq a \in \epsilon ^ { n } ( q )$, as$\rho ^ { e } ( R _ { \eta } ) [ w ]$

(5)${ \mathcal { P } } ^ { * } ( q , \mathbf { r } )$is a coherent sheaf of modules on the scheme$Z ( q , \mathbf { r } )$ which is$S p e c ( \rho ^ { e } ( \mathcal { O } _ { Z } ) [ w ] )$where

$$
\rho^ {e} (\mathcal {O} _ {Z}) [ w ] = \mathcal {P} ^ {*} (q, \mathbf {r}) (\mathcal {O} _ {Z}) = \mathcal {P} ^ {*} (q, \mathbf {r}) ^ {- 1} 0\tag{30.1}
$$

The last symbol means$\{ f \in \mathcal { O } _ { Z } | \mathcal { P } ^ { * } ( q , \mathbf { r } ) f ~ = ~ 0 \}$

(6) We have

$$
\mathcal {P} ^ {*} (q, \mathbf {r}) = H o m _ {\rho^ {e} (\mathcal {O} _ {Z}) [ w ]} (\mathcal {O} _ {Z}, \rho^ {e} (\mathcal {O} _ {Z}) [ w ])\tag{30.2}
$$

(7) The morphism r is factored into the following two morphisms

$$
Z | U \xrightarrow {\varrho} Z (q, \mathbf {r}) \xrightarrow {w} \mathbb {A} ^ {t}\tag{30.3}
$$

where ϱ is defined by the Frobenius$u \mapsto \rho ^ { e } ( u )$

We have thus obtained the locally free coherent modules (and algebras) of square nilpotent diferential operators${ \mathcal { P } } ^ { * } ( q , \mathbf { r } )$on the scheme $Z ( q , \mathbf { r } )$with respect to any “separable” retraction$\xi \in D \subset Z \setminus \mathbb { A } ^ { t }$of Def.(26.1). As a matter of fact, the module is independent of$D$in the retraction r of Def.(26.1). They depend only on a portion of r that is the projection morphism$Z \supset U \to \mathbf { A } ^ { t }$. For this fact we should recall Rem.(??).

Definition 30.1. Let$I ( S )$denotes the ideal of the closed subscheme $D \subset Z$in the local separable retraction r of Def.(26.1). We then define the$\mathcal { O } _ { Z \left( q , \mathbf { r } \right) }$-submodules of${ \mathcal { P } } ^ { * } ( q , \mathbf { r } )$, denoted by${ \mathcal { P } } ^ { * } ( q , \mathbf { r } ) ( - \sigma )$, for each integer$\sigma \geq 0$as follows,

$$
\mathcal {P} _ {\sigma} ^ {*} (q, \mathbf {r}) =\tag{30.4}
$$

$$
\bigcap_ {\nu - \sigma \geq 0} K e r \Big (\mathcal {P} ^ {*} (q, \mathbf {r}) \to H o m _ {\rho^ {e} (\mathcal {O} _ {Z})} \big (I (D) ^ {\nu}, \mathcal {O} _ {Z} / I (D) ^ {\nu - s} \big) \Big)
$$

Definition 30.2. Let$\mathcal { G }$be a /<sup>q</sup>-exponent in$Z$and let$D \subset Z$be denoted by the ideal$I ( D )$. Write$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$with$\mathbf { g } = z ^ { \mathbf { a } } = z ^ { q \mathbf { b } } v ^ { \mathbf { c } } g$ with a cofactor$v ^ { \mathbf { c } }$and a residual factor g at a closed point$\xi$of D. Let s be an integer with$0 \geq - s > - q$We then define the following ideal exponent in an open neiborhood of$\xi \in Z \colon$

$$
\mathcal {D} (\mathbf {r}, D) ^ {(- s)} (\mathcal {G}) = (J, \sigma)\tag{30.5}
$$

$$
w i t h J = \mathcal {P} ^ {*} (q, \mathbf {r}) (- s) (v ^ {\mathbf {c}} g) a n d \sigma = o r d _ {\xi} (J)
$$

Here the ideal$\mathcal { P } ^ { * } ( q , \mathbf { r } ) ( - s ) ( v ^ { \mathbf { b } } g )$is independent of the choice of the abcexpression of G. The ideal exponent$\mathcal { D } ( { \bf r } , D ) ^ { ( - s ) } ( \mathcal { G } )$in$Z$with various s are called /<sup>q</sup>-singular derivatives, or /<sup>q</sup>-derivatives for short, of$\mathcal { G }$with respect to the retraction r. The numbers −s are called their degrees.

We next examine the dependence of those /<sup>q</sup>-derivatives on the choices of the retractions r.

Remark 30.2. As far as${ \mathcal { D } } ( \mathbf { r } , D ) ^ { ( - s ) } ( { \mathcal { G } } )$is concerned, the question of its dependence on the retractions is only about r as projection morphism $Z \supset U \to { \mathbb { A } } ^ { t }$. Any general change of r can be decomposed into the following two kinds of changes.

(1) (The first change) Choose any regular system of parameters$w ^ { \dagger }$ of$\mathcal { O } _ { \mathbb { A } ^ { t } , 0 }$where$\mathbb { A } ^ { t } = S p e c ( \mathbb { K } [ \omega ] )$. This$w ^ { \dagger }$is identified with a systemof elements in$R _ { \xi }$by the given projection r defined by w. Then$( u , w ^ { \dag } )$is a regular system of parameters of$R _ { \xi }$. In this case the projection morphism$\mathbf { r } ^ { \dagger }$defined by$w ^ { \dagger }$is factored into the one by w and a local etale morhphism of$\mathbb { A } ^ { t }$into itself. Therefore the diferential operators$\partial ^ { ( a ) }$and hence primitive ones $d e l t a ^ { ( a ) }$remain unchanged in$D i f f _ { Z }$. We thus conclude

$$
\begin{array}{c} \mathcal {P} ^ {*} (q, \mathbf {r}) (- s) _ {\xi} = \mathcal {P} ^ {*} (q, \mathbf {r} ^ {\dagger}) (- s) _ {\xi} \\ a n d \mathcal {D} (\mathbf {r}, D) ^ {(- s)} (\mathcal {G}) = \mathcal {D} (\mathbf {r} ^ {\dagger}, D) ^ {(- s)} (\mathcal {G}) \end{array}\tag{30.6}
$$

(2) (The second change) Choose a new regular system of parameters$( u , w ^ { \ddag } )$in such a way that$w ^ { \ddagger } \equiv w$mod$( z ) R _ { \xi }$. With the retraction r‡ defined by$w ^ { \ddag }$we then have the same u generating $I ( D )$while each monomial$u ^ { a } w ^ { b }$is changed as follows.

$$
u ^ {a} (w ^ {\dagger}) ^ {b} \equiv u ^ {a} w ^ {b} \mod \sum_ {c, b \in c + \mathbb {Z} ^ {t}} x ^ {a + c} w ^ {c} \rho^ {e} (R _ {\xi}).\tag{30.7}
$$

With the new retraction r‡ defined by$w ^ { \ddag }$, the change from ${ \mathcal { D } } ( \mathbf { r } , D ) ^ { ( - s ) } ( { \mathcal { G } } )$to$\mathcal { D } ( { \bf r } ^ { \ddag } , D ) ^ { ( - s ) } ( \mathcal { G } )$is done accordingly and the details are shown in the case of generic down center$D$for$\mathcal { G }$.

The /<sup>q</sup>-derivatives of degrees −s are useful in the study of singularities along generic-down subschemes for$\mathcal { G }$, in particular if the integer s is chosen to be the one fitted to the chosen subscheme.

Remark 30.3. (1) Consider a G-stratification of Z of Def.(25.1) or more specifically the canonical one of Rem.(25.1). Then pick any generic-down one, say$D$, among its closed strata.

(2) Let$\xi$be a closed point of any generic-down irreducible subscheme$D$containing$\xi$in the sense of Def.(??). We may choose this D to be smooth at$\xi$so that Th.(27.2) is applicable along with Def.(30.1).

(3) For a closed point$\xi \in S i n g ( \mathcal { G } )$we choose the following closed subscheme of$Z$.

$$
\text { The   closure } \mathbf {S} (\mathcal {G}, \xi) \text { in } Z\tag{30.8}
$$

$$
\text {   of   the   set   } \{\eta \in Z _ {c l} | r e s o r d _ {\eta} (\mathcal {G}) = r e s o r d _ {\xi} (\mathcal {G}) \}
$$

Given a generic-down subscheme$D \subset Z$, which is contained in $S i n g ( \mathcal { G } )$, the integer s for the /<sup>q</sup>-derivative$\mathcal { D } ( { \bf r } , D ) ^ { ( - s ) } ( \mathcal { G } )$in the sense of Def.(30.2) will be chosen to be the one called significant for the relation between D and$\mathcal { G }$at the given point$\xi .$The significant number s will be selected by means of the local analysis of generic-down phenomena in view of Eq.(??) of Th.(??).

We go back to the /<sup>q</sup>-exponent$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$with$q = p ^ { e }$in virtue of Th.(??) and we follow the presentation described by$\operatorname { E q . } ( ? ? )$, although some of the symbols are changed so as to fit this section better.

We have a smooth irreducible subscheme$D \subset S i n g ( { \mathcal { G } } ) \subset Z$which is generic-down for$\mathcal { G }$. We assume that$o r d _ { \eta } ( \mathcal { G } )$is constant$m = A q + q ^ { * }$ for all points of$D \cap Z _ { c l }$where$A q = o r d _ { D } ( { \mathcal { G } } )$which means the order at the generic point of$D$, where A is a positive integer and$q ^ { * } = p ^ { e ^ { * } }$ with an integer$e ^ { * }$such that$e > e ^ { * } \geq 0$. We have$\xi \in D \cap Z _ { c l }$and pick a regular system of parameters$( u , w )$of$R _ { \xi }$such that$x = ( x _ { 1 } , \cdots , x _ { n } )$ generates$I ( D , Z ) _ { \xi }$and$w = ( w _ { 1 } , \cdot \cdot \cdot , w _ { t } )$. The generic down theorem Th.(??) asserts the following presentation:

$$
\mathbf {g} = \sum_ {1 \leq i \leq \tau} w _ {i} ^ {q ^ {*}} \phi_ {i} ^ {q} + \sum_ {b \in \epsilon^ {t} (q) \cap (q ^ {*}) \mathbb {Z} ^ {t}, | a | > q ^ {*}} w ^ {b} \psi_ {b} ^ {q} + \lambda\tag{30.9}
$$

which has the following properties:

(1)$1 \leq \tau \leq t$and$o r d _ { \xi } ( \phi _ { i } ) = o r d _ { D } ( \phi _ { i } ) = A$for all$i \le \tau$. (x is suitably reordered.)

(2)$o r d _ { D } ( \psi _ { a } ) = A$

(3) ??????

Also important are$b \equiv 0 m o d q ^ { * }$and$| b | > q ^ { * }$except for those which can be shifted into λ. (Refer to Eq.(??) and Rem.(??).)

Definition 30.3. After Th.(??) and$\mathrm { E q . ( 3 0 . 5 ) }$, the above expression Eq.(30.9) tells us that the numbers d with$0 \geq d \geq - q ^ { * }$are significant for the study of singularity of$\mathcal { G }$along a generic-down subscheme D. With these$d$the$/ ^ { q } .$-derivatives${ \mathcal { D } } _ { D } ^ { \ * } ( - r ) ( { \mathcal { G } } )$will be said significant for $\mathcal { G }$along$D$. The number d is called the degree of the /<sup>q</sup>-derivative of G along$D .$Above all$d = - q ^ { * }$is the most significant, and$\mathcal { D } _ { D } ^ { \mathrm { ~ * ~ } } ( - q ^ { * } ) ( \mathcal { G } )$ will be called the most significant /<sup>q</sup>-derivative, of$\mathcal { G }$along D. This will often be called the derivative of$\mathcal { G }$along$D$and denoted by$D e r _ { D } ( { \mathcal { G } } )$ for short.

In regards to Th.(??) we can add a little more refinements as follows.

Lemma 30.1. An expression$E q . ( 3 0 . 9 )$of h can be chosen in such a way that the following condition is satisfied in addition to all the properties of Eq.(??).

$$
\delta_ {x} ^ {(0 b)} \lambda = 0, \forall (0 b) \in \epsilon^ {n} (q)\tag{30.10}
$$

Lemma 30.2. Under the assumptions of Lem.(30.1), assume that the expression Eq.(30.9) is satsfied. Then the coherent ideal$\mathcal { P } _ { Z } ^ { ( q ) * } ( D ) h$is locally at$\xi$of the following form:

$$
\rho^ {e} \left(\{\phi_ {i} \forall i, \psi_ {b} \forall (0 b) \in \epsilon^ {n} (q) \} \mathcal {O} _ {Z, \xi}\right)\tag{30.11}
$$

## 31. fitted permissible blowups

Recall Def.(18.2) on permissibility of a blow-up$\pi : Z ^ { \prime } \longrightarrow Z$with center D for a$/ ^ { q } .$-exponent$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$and its transform Def.(18.4). Also refer to Def.(18.1), Th.(18.1) and Th.(18.2).

In some cases, however, Def.(18.2) is not strong enough for the purpose of reduction of singularities. To introduce stronger notion of permissibility, we need to recall the results on Γ-maximal divisor, obtained by Th.(19.1) and Rem.(19.1). We also need the notion of checked /<sup>q</sup>-exponent$\check { \mathcal { G } }$associated with the given$\mathcal { G }$in the sense of Eq.(19.2) of Def.(19.4). This is locally obtained from$\mathcal { G }$by dividing out its$\Gamma -$ maximal divisors.

Definition 31.1. A blowup$\pi : Z ^ { \prime } \longrightarrow Z$with center$D ,$permissible for${ \mathcal { G } } _ { : }$, is called closed-fitted or cl-fitted for short if we have$o r d _ { \eta } ( \check { g } )$is constant for$\eta \in D \cap Z _ { c l }$. Recall Eq.(19.1) of Def.(19.3) in relation with Def.(19.4). Note that we always have

$$
o r d _ {\eta} (\check {\mathcal {G}}) = r e s o r d _ {\eta} (\mathcal {G}) f o r \forall \eta \in S i n g (\mathcal {G}) \cap Z _ {c l}\tag{31.1}
$$

Thanks to Th.(17.1), we have a locally finite$\mathcal { G } _ { c l }$-stratification of

$$
S i n g (\check {\mathcal {G}}) _ {c l} = S i n g (\check {\mathcal {G}}) \cap Z _ {c l}
$$

in such a way that each member D of its strata is smooth and locally closed inside$Z _ { c l }$with Zariski topology and$o r d _ { \eta } ( \check { g } )$is constant for closed points$\eta$of$D$. It then follows that the blowup with center$D$ is cl-fitted permissible for$\mathcal { G }$in the sense of Def.(31.1) if it is permissible in the sense of Def.(18.2). However D could be of generic-down type in which case it is not fitted in the sense defined below. The fitted permissibility will be indeed a notion stronger than that of Def.(31.1).

Definition 31.2. A permissible blowup$\pi$for$\mathcal { G }$(and for Γ as always) with smooth center$D$is said to be scheme-fitted or sch-fitted for short if$o r d _ { \eta } ( \check { g } )$is constant for all$\eta \in D$, or equivalently$o r d _ { \zeta } ( \check { \mathcal { G } } ) = o r d _ { \xi } ( \check { \mathcal { G } } )$ the generic point$\zeta$of$D$and for all points$\xi$of$D \cap Z _ { c l }$

Note here that since D is smooth we have$o r d _ { \zeta } ( \check { \mathcal { G } } ) \leq o r d _ { \sigma } ( \check { \mathcal { G } } )$for every point$\sigma \in D$by Lem.(17.3). Moreover for a closed point$\xi$in the closure of$\sigma$we have$o r d _ { \sigma } ( \check { \mathcal { G } } ) \leq o r d _ { \xi } ( \check { \mathcal { G } } )$by Lem.(17.6). Thus if or$\cdot d _ { \zeta } ( \check { \mathcal { G } } ) = o r d _ { \xi } ( \check { \mathcal { G } } )$then$o r d _ { \zeta } ( \check { \mathcal { G } } ) = o r d _ { \sigma } ( \check { \mathcal { G } } )$

Theorem 31.1.$I f \pi$with center D is cl-fitted permissible but not schfitted for$\mathcal { G }$then D must be generic-down type for$\mathcal { G }$.

This theorem is nothing more than a definition by itself. What is important is its supporting background that is a criterion for “genericdown” phenomena not to happen. The reader should refer to Th.(??)

with Eq.(??). In such cases we need a diferent strategy for choosing centers of blowups toward the end of reduction of singularities. To deal with generic-down type centers, we introduce the following notion of permissibility which is weaker than being sch-fitted but generally stronger than cl-fitted.

Definition 31.3. A permissible blowup π with center$D$for$\mathcal { G }$is said to be fitted permissible for$\mathcal { G }$if there holds either one of the following two conditions:

(1)$D$is not generic-down type for$\mathcal { G }$and π is sch-fitted permissible for${ \mathcal { G } } .$.

(2) D is generic-down type for$\mathcal { G }$and the ideal exponent$D e r _ { D } ( { \mathcal { G } } )$ has a constant order along D where$D e r _ { D } ( { \mathcal { G } } )$denotes the (most significant) /<sup>q</sup>-derivative of$\mathcal { G }$along$D$in the sense of Def.(30.3). Incidentally it follows that π is cl-fitted for$\mathcal { G }$

See$\operatorname { E q . }$((30.11) of Lem.(30.2) with reference to Def.(30.3).

Remark 31.1. The center of a fitted permissible blowup for a$/ ^ { q } .$-exponent is necessarily transversal by definition to the foliational component (which exists only in the generic-down case) at every point of the center. The notion of foliational component are mentioned in the other sections such as the next one on /<sup>q</sup>-stable singularities.

## 32. /<sup>q</sup>-stable singularities

One of the most important technical elements in our approach to the problem of resolution of singularities by means of a finite sequence of permissible blowups is to search for a good definition of stable state of defining equations for the given singular data and to design a program to achieve such a stable state if possible. In the case of characteristic zero, the stable state was “normal crossings” whose stability with respect to any subsequent permissible blowups was not only useful for formulating the final state of resolution of singularities but also technically indispensable in many steps of the inductive proof of the embedded resolution in all dimensions.

In characteristics$p > 0$, “normal crossings” is also useful to some extent but it is almost always unstable and much less powerful especially in the course of our inductive proofs. We have thus chosen to introduce a new notion called$\int ^ { q } - s t a b l e$state and$\scriptstyle \int ^ { q } - s t a b l e$decompositions.

A /<sup>q</sup>-stable state in positive characteristics is not “stable” unlike the normal crossings in the zero characteristic cases. However it turns out to play an important role as a workable substitute for normal crossing in order to treat$/ ^ { q } { \mathrm { - e x p o n e n t s } }$in positive characteristics. At any rate the$\scriptstyle \int { ^ { q } - s t a b l e }$state is ubiquitous in our theory.

The adjective stable or stable should be spoken in its global sense when we are aiming for a global embedded resolution of singularities. However it seems unavoidable that our investigation of$\int ^ { q } - s t a b l e$exponents is local just as the edge decompositions of Th.(10.2). In this section our study will be local. The globalization will then be formulated in terms of the infinitely near singularities and the characteristic algebra S of Def.(6.2).

Definition 32.1. A /<sup>q</sup>-exponent P combined with an integer$0 \leq \mu <$ $e ,$where$q = p ^ { e } , e \geq 1$, is called /<sup>q</sup>-stable exponent of depth$\mu ,$or$/ ^ { q } -$ stable for short, at a closed point$\xi \in S i n g ( \mathcal { P } ) \cap Z _ { c l }$if we can choose $f \in R _ { \xi }$in such a way that within a suficiently small neighborhood of $\xi \in Z$we have

$$
\mathcal {P} = \left(f ^ {p ^ {\mu}} \| / ^ {q}\right) w i t h f = u z ^ {\alpha} \mathrm{e} ^ {\ddot {o}}\tag{32.1}
$$

where

(1)$0 \leq \mu \leq e - 1$and u is a unit in$R _ { \xi }$

(2)$z = ( z _ { 1 } , \cdots , z _ { t } )$is a system of parameters defining those components of Γ which contains ξ and$\alpha \in \mathbb { Z } _ { 0 } ^ { t }$

(3) o¨ is either zero or one,

(4) if$\ddot { o } = 0$then$\alpha \not \equiv 0$mod$p$

(5) if$\ddot { o } = 1$then æ is a parameter such that$( z , \mathrm { \alpha } \mathrm  { \alpha } \mathrm { { \alpha } \mathrm { { \it { \alpha } \it { \alpha } \mathrm { { \it { \alpha } \it { \alpha } \mathrm { { \it { \alpha } \it { \alpha } \mathrm { { \it { \alpha } \it { \alpha } \mathrm { { \it { \alpha } \it { \alpha } \mathrm { { \it { \alpha } \it { \alpha } \mathrm { { \it { \it \alpha } \it { \alpha } \mathrm { { \it { \it \alpha } \it { \alpha } \mathrm { { \it \it { \alpha } \it { \it { \alpha } \it { \it \alpha } \mathrm { { \it \it { \alpha } \it { \it \alpha } \mathrm { { \it \it { \alpha } \it { \it \alpha } \it } \mathrm { { \it \alpha } \it } \mathrm { { \it \it { \alpha } \it \it { \alpha } \it } \mathrm { \it { \alpha \it } \it { \it \alpha } \mathrm { \it { \it \alpha } \it } } } } } } } } } } } } } } } } } } } } } } } } } }$extends to a regular system of parameters of$R _ { \xi }$. Namely æ is Γ-transversal in the sense of Def.(14.1).

We call$\mu$the stable depth of$\mathcal { P }$and æ a foliational parameter of$\mathcal { P } _ { \cdot }$.

Remark 32.1. The$z _ { i }$are “geometrically rigid” in the sense that they are unique up to unit multiples. On the contrary æ is not so$\mathrm { \ddot { \ r i g i d } \mathrm { \ ' } }$ Indeed, assuming$\ddot { o } = 1$and speaking locally at ξ, we may replace æ by any element of the form

$$
\mathrm{ae} ^ {\dagger} = u \mathrm{ae} + c z ^ {\alpha^ {b}} w h e r e\tag{32.2}
$$

(1) u is the given unit element of$R _ { \xi }$

(2) c is any element of$\rho ^ { e - \mu } ( R _ { \xi } )$

(3)$\alpha ^ { \flat }$is the$p ^ { e - \mu } .$-supplement of α in the sense of Def.(22.1), i.e., $\alpha ^ { \flat }$is the smallest among those$\beta \in \mathbb { Z } _ { 0 } ^ { t }$such that$\alpha + \beta \equiv 0$ mod$( p ^ { e - \mu } )$

(4)$\begin{array} { r } { \infty ^ { \dagger } ( \xi ) = 0 , \mathrm { i . e } , c z ^ { \alpha ^ { \flat } } ( \xi ) = 0 } \end{array}$. Clearly this is automatically satisfied if$\alpha \not \equiv 0$mod$p ^ { e - \mu }$

Note that the replacement of æ by the above$\mathrm { { a } ^ { \dagger } }$does not change the /<sup>q</sup>-exponent P and that the hypersurface$\mathrm { { x } ^ { \dag } = 0 }$is smooth and$\Gamma _ { - }$ transversal at the point ξ.

Remark 32.2. In a sense the family of hypersurfaces$\smash {  { \mathrm { \ x } } ^ { \dagger } = 0 }$are a kind of foliational (or movable in a pencil) within$Z - | \Gamma |$. The idea of introducing such foliational hypersurfaces became clearer thanks to our discussions with H-M. Aroca and F. Cano at Valladolid University in March 2005 and at the Tordesillas Conference in August 2006.

Example 32.1. Let$h = z _ { 1 } ^ { p ^ { 2 } } z _ { 2 } ^ { p ^ { 3 } } z _ { 3 } ^ { p ^ { 4 } } \in \mathbb { K } [ x ]$with three variables$z =$ $\left( z _ { 1 } , z _ { 2 } , z _ { 3 } \right)$. Let$q \ = \ p ^ { 3 }$with the characteristic$p > 0$of K. Then $\mathcal { P } = \left( h \| \mathbf { \rho } / { \mathfrak { q } } \right)$is /<sup>q</sup>-stable of depth 2 at every closed point of$S i n g ( \mathcal { P } )$ which is$\{ z _ { 2 } = 0 \} \cup \{ z _ { 3 } = 0 \}$. A /<sup>q</sup>-stable exponent is$f ^ { p ^ { 2 } }$with

(1)$f = z _ { 1 } z _ { 2 } ^ { p } z _ { 3 } ^ { p ^ { 2 } }$at$( 0 , 0 , 0 )$, at$( 0 , 1 , 0 )$and at$( 0 , 0 , 1 )$

(2)$f = z _ { 2 } ^ { p } z _ { 3 } ^ { p ^ { 2 } } \mathrm { { a } } _ { 1 }$with${ \bf { x } } _ { 1 } = ( z _ { 1 } - 1 )$at$( 1 , 0 , 0 )$, and

(3)$f = z _ { 3 } ^ { p ^ { 2 } } \mathrm { { \alpha } \mathrm { { z } } }$with$\mathfrak { x } _ { 2 } = \mathfrak { x } _ { 1 } + ( \mathtt { x } _ { 1 } + 1 ) ( z _ { 2 } - 1 ) ^ { p } \mathrm { a t } ( 1 , 1 , 0 )$

(4)$f = z _ { 2 } ^ { p } \mathrm { { x } _ { 3 } }$with$\begin{array} { r } { \mathtt { x } _ { 3 } = \mathtt { x } _ { 1 } + ( \mathtt { x } _ { 1 } + 1 ) ( z _ { 3 } - 1 ) ^ { p ^ { 2 } } } \end{array}$at (1, 0, 1)

where$\operatorname { \mathrm { x } } _ { i } , 1 \leq i \leq 3$, is a foliational parameter respectively.

Example 32.2. Let us consider the case of$p > 2$and$r + 1$variables $z = ( z _ { 0 } , z _ { 1 } , · · · , z _ { r } )$with$2 r = p + 1$. Let$\begin{array} { r } { { \cal h } ~ = ~ z _ { 0 } \prod _ { i = 1 } ^ { r } z _ { i } ^ { 2 p } } \end{array}$. Then $\mathcal { P } = \left( h \| \mathbf { \rho } / \mathsf { \varepsilon } \right)$with$q = p ^ { 2 }$is /<sup>q</sup>-stable of depth 0 at the origin but it is not /<sup>q</sup>-stable at any other closed point$\eta$of$S i n g ( \mathcal { P } )$, where$S i n g ( \mathcal { P } )$ is$\{ z _ { 1 } = \cdots = z _ { r } = 0 \}$. However at η,$\mathrm { s a y } = ( 1 , 0 )$, we can write $h ~ = ~ h ^ { \sharp } ~ + ~ h ^ { \flat }$where$\begin{array} { r } { h ^ { \sharp } = \left( \prod _ { i = 1 } ^ { r } z _ { i } ^ { 2 p } \right) } \end{array}$æ with$\mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi } \mathrm { \Phi }$and$h ^ { \flat } =$ $\textstyle \prod _ { i = 1 } ^ { r } z _ { i } ^ { 2 p }$. Note that

(1)$\mathcal { P } ^ { \sharp } = ( \mathbf { g } ^ { \sharp } \rVert / ^ { q } )$is$/ ^ { q } .$-stable of depth 0 at$\eta$.

(2) With$h _ { \flat }$defined by$h _ { \flat } ^ { \flat } = h ^ { \flat } , { \mathcal { P } } ^ { \flat } = ( \mathbf { g } _ { \flat } ^ { \flat } \| / ^ { q } )$is /<sup>q</sup>-stable of depth 1 at$\eta .$.

Definition 32.2. The notion of depth is extended to an arbitrary$/ ^ { q _ { - } }$ exponent$\mathcal { G } = \left( \mathbf { g } \parallel / \vphantom { \left( \mathbf { g } \right) } \right)$by saying that the depth of$\mathcal { G }$at a closed point $\xi \in S i n g ( \mathcal { G } )$is the maximal integer$\mu \leq e$such that$h \in \rho ^ { \mu } ( R _ { \xi } )$. It should be noted that this number$\mu$is well defined in view of Eq.(16.1) of Def.(16.1).

Definition 32.3. Let$\mathcal { P }$and B be two$/ ^ { q } { } .$-exponents with depths a and b respectively. Assume$b > a . \mathrm { ~ A ~ } / { } ^ { q } .$-exponent$\mathcal { G }$is called a$/ ^ { q } .$-extension, or an extension for short, of$\mathcal { P }$by B if we can find representations ${ \mathcal { P } } = \left( f ^ { p ^ { a } } \parallel / { \vphantom { \mathcal { q } } } \right)$and$B = \left( g ^ { p ^ { b } } \parallel / ^ { q } \right)$such that$\mathcal { G } = ( f ^ { p ^ { a } } + g ^ { \bar { p } ^ { b } } \rVert / ^ { q } )$. Note that G then has depth a.

For an example of$/ ^ { q }$-extension, observe Ex.(32.2) in which$\mathcal { P }$is an extension of${ \mathcal { P } } ^ { \sharp }$of depth 0 by${ \mathcal { P } } ^ { \flat }$of depth 1.

Definition 32.4. Consider a blowup$\pi : Z ^ { \prime } \longrightarrow Z$with center D. Let G be a /<sup>q</sup>-stable exponent at a point$\xi \in D$in the sense of Def.(32.1). We say that$\pi$(and D) is$/ ^ { q }$-stable permissible for$\mathcal { G }$at$\xi$if it is fitted permissible for a /<sup>q</sup>-stable exponent ssuch as$\mathcal { G }$. Let us recall the general agreemen that D must have normal crossings with Γ as always.

Theorem 32.1. Let$\mathcal { G } ^ { \prime }$be the transform of a /<sup>q</sup>-stable exponent$\mathcal { G }$at a closed ξ by a /<sup>q</sup>-stable permissible blowup$\pi : Z ^ { \prime } \longrightarrow Z$. Then$\mathcal { G } ^ { \prime }$ is$/ ^ { q }$-stable at every point of$\pi ^ { - 1 } ( \xi )$. The depth of the transform may become deeper after the transformation. Let$\xi ^ { \prime }$be any closed point of $\pi ^ { - 1 } ( \xi )$and we have the following cases:

(1) If the center D does not contain the foliational component$\{ \mathrm { x } ^ { \ddot { o } } =$ 0} and$i f \xi ^ { \prime }$is in the strict transform of the foliational component$\{ \alpha ^ { \ddot { o } } = 0 \}$when$\ddot { o } \neq 0$then$\mathcal { G } ^ { \prime }$is /<sup>q</sup>-stable with the same depth.

(2)$I f \xi ^ { \prime }$is not in the strict transform of the foliational component $\{ \mathrm { x } ^ { \ddot { o } } = 0 \}$(automatic if$\Ddot { o } \ = \ 0 \dot { }$then$\mathcal { G } ^ { \prime }$is$/ ^ { q }$-stable while its depth may be bigger.

Definition 32.5. Consider a blowup$\pi : Z ^ { \prime } \longrightarrow Z$with center$D$. The notion of Γ-pure in Def.(??) is applicable in the case of$\big / { } ^ { q } -$exponents. Namely$\pi$(and D) is called Γ-pure if$D$is an intersection of some members of Γ locally everywhere. If moreover$\pi$is permissible for a given /<sup>q</sup>-exponent$\mathcal { G }$then it is said to be Γ-pure permissible for${ \mathcal { G } } .$ Needless to say any Γ-pure blowup is permissible for$\Gamma$

Theorem 32.2. Assume that${ \mathcal { P } } = \left( \mathbf { g } \parallel / { \vphantom { \big ( } } ^ { q } \right)$is /<sup>q</sup>-stable of depth$\mu$at a closed point$\xi \in S i n g ( \mathcal { P } )$in the sense of$E q . ( 3 2 . 1 )$. Let$\pi : Z ^ { \prime } \longrightarrow Z$ with center$D \ni \xi$be Γ-pure permissible for${ \mathcal { P } } = \left( \mathbf { g } \parallel { \big / } ^ { q } \right)$and let${ \mathcal { P } } ^ { \prime }$be the transform$o f { \mathcal { P } }$by π. Pick any closed point$\xi ^ { \prime } \mathrm { ~ } i n \mathrm { ~ } S i n g ( \mathcal { P } ^ { \prime } ) \cap \pi ^ { - 1 } ( \xi )$ Then${ \mathcal { P } } ^ { \prime }$at$\xi ^ { \prime }$is either /<sup>q</sup>-stable of the same depth µ by itself or an extension of a /<sup>q</sup>-stable of depth$\mu$by another /<sup>q</sup>-stable of depth$> \mu$

The theorem will be proven after several observations and remarks below. We refer to Def.(32.5) and our blowup$\pi : Z ^ { \prime } \longrightarrow Z$with center D is assumed to be Γ-pure permissible so that$D$is automatically transversal to every choice of the hypersurfaces$\mathrm { { x } ^ { \dag } = 0 }$of Eq.(32.2) when$\ddot { o } = 1$of Eq.(32.1).

We will prove Th.(32.2) after the Rem.(32.3), Rem.(32.4) and Rem.(32.5) below. We will be using the notation and the assumptions of Th.(32.2) and Def.(32.1).

Remark 32.3. Let us choose an exceptional parameter$\mathfrak { z }$at a closed point $\xi ^ { \prime } \in S i n g ( \mathcal { P } ^ { \prime } ) \cap \pi ^ { - 1 } ( \xi )$, in terms of which we describe the transform ${ \mathcal { P } } ^ { \prime }$of$\mathcal { P }$by$\pi$locally at$\xi ^ { \prime }$. Since$D$is Γ-pure, we may assume$z =$ $( z ( 0 ) , z ( 1 ) )$(by reordering z if necessary) in such a way that the ideal $I ( D , Z ) _ { \xi }$is generated by$z ( 0 )$and$\mathfrak { z }$is one of the members of$z ( 0 )$. Let us write$z ^ { \alpha } = z ( 0 ) ^ { \alpha 0 } z ( 1 ) ^ { \alpha ( 1 ) }$

(1) If$\ddot { o } = 1$we may assume that$u = 1$in$\mathrm { E q . ( 3 2 . 1 ) }$by replacing æ by$u ^ { - 1 } \mathrm { { \alpha } } \mathrm { { \alpha } }$. We let transforms$\mathrm { { a } ^ { \prime } = \aleph \mathrm { { a } } }$and define$z ^ { \prime }$to be the combined system of$( 3 , z ( 1 ) )$put together with all those members of$\mathfrak { z } ^ { - 1 } z ( 0 )$which vanish at$\xi ^ { \prime }$. We let$u ^ { \prime }$be the product of those$( \mathfrak { z } ^ { - 1 } z _ { i } ) ^ { \alpha _ { i } }$which do not vanish at$\xi ^ { \prime }$. With those$\operatorname { \mathbf { \mathbf { \mathbf { \mathbf { \ x } } } ^ { \prime } } } , \ z ^ { \prime }$ and$u ^ { \prime }$, we obtain a$/ ^ { q }$-stable form of$\mathcal { P } ^ { \prime } = \left( \left. f ^ { \prime } \right. { p ^ { \mu } } \right\| \left/ ^ { q } \right)$at$\xi ^ { \prime }$by choosing

$$
f ^ {\prime} = u ^ {\prime} z ^ {\prime \alpha^ {\prime}} \mathrm{ae} ^ {\prime \ddot {o}}\tag{32.3}
$$

where$\ddot { o } = 1$and$\alpha ^ { \prime }$is determined by the equality

$$
u ^ {\prime} z ^ {\alpha^ {\prime}} = \mathfrak {z} ^ {| \alpha 0 | - p ^ {e - \mu}} \left(\mathfrak {z} ^ {- 1} z 0\right) ^ {\alpha 0} z (1) ^ {\alpha (1)}\tag{32.4}
$$

Here$\operatorname { E q } .$(32.3) proves that${ \mathcal { P } } ^ { \prime }$is a /<sup>q</sup>-stable exponent at$\xi ^ { \prime }$.

(2) Assume$\ddot { o } = 0$so that$\alpha \not \equiv 0$mod$p .$. We write$\alpha = p \mathbf { b } + \gamma$where b is the integral part of$p ^ { - 1 } \alpha$so that$0 \leq \gamma _ { i } \leq p - 1$, ∀i. We write$z ^ { \mathbf { b } } = \widetilde { ( z 0 ^ { \mathbf { b } ( 0 ) } z ( 1 ) ^ { \mathbf { b } ( 1 ) } }$and$z ^ { \gamma } = z ( 0 ) ^ { \gamma ( 0 ) } z ( 1 ) ^ { \gamma ( 1 ) }$. Remember that we have$\gamma _ { k } \neq 0$for at least one k. Let us first consider the case in which$\gamma ( 1 ) \neq 0$. In this case, we define$z ^ { \prime }$and$\alpha ^ { \prime }$in the same way as was done by Eq.(32.3) and Eq.(32.13). Then we see that$z ^ { \prime \alpha ^ { \prime } }$has a factor$z ( 1 ) ^ { p \mathbf { b } ( 1 ) + \gamma ( 1 ) }$. Since$\gamma ( 1 ) \neq 0$we again conclude that Eq.(32.3) is a /<sup>q</sup>-stable form for${ \mathcal { P } } ^ { \prime }$

(3) Assume$\ddot { o } = 0$and$\gamma ( 1 ) = 0$Then we must have$\gamma 0 ~ \neq ~ 0$ In this case we have two possibility: the first one in which ${ \mathfrak { z } } ^ { - | \gamma 0 | } z ^ { \gamma 0 }$vanishes at$\xi ^ { \prime }$and the second in which it does not. Let us consider the first case. Remember that we have at least one index k such that$\gamma 0 _ { k } \neq 0$. Then following the same procedure as was done in Eq.(32.3) and Eq.(32.13), we see that$z ^ { \prime \alpha ^ { \prime } }$has a factor$z 0 _ { k } ^ { \prime } { } ^ { p \mathbf { b } _ { k } + \gamma _ { k } }$. Again since$0 < \gamma _ { k } < p$, we conclude that Eq.(32.3) is a$/ ^ { q } .$-stable form for${ \mathcal { P } } ^ { \prime }$

(4) Remaining is the case in which$\Ddot { o } = 0 , \gamma ( 1 ) = 0$and${ \mathfrak { z } } ^ { - | \gamma 0 | } z ^ { \gamma 0 }$ is a unit at$\xi ^ { \prime }$. We may then choose z to be$z 0 _ { k }$with any k such that$\gamma _ { k } \neq 0$. We divide the system$\mathfrak { z } ^ { - 1 } z 0$into two parts as follows:

$$
\mathfrak {z} ^ {- 1} z 0 = (\check {U}, z 0 ^ {\sharp})\tag{32.5}
$$

with the subsystem$z 0 ^ { \sharp }$

composed of exactly those${ \mathfrak { z } } ^ { - 1 } z _ { i } \in m a x ( R _ { \xi ^ { \prime } } )$

so that$\check { U }$is the subsystem of$\mathfrak { z } ^ { - 1 } z 0$composed of those$\mathfrak { z } ^ { - 1 } z _ { i }$ which are units in$R _ { \xi ^ { \prime } }$. We define

$$
u ^ {\prime} = u \check {U} ^ {\delta} \text {where} \check {U} ^ {\delta} = \prod_ {i: \mathfrak {z} ^ {- 1} z _ {i} \in \check {U}} (\mathfrak {z} ^ {- 1} z _ {i}) ^ {\alpha_ {i}}\tag{32.6}
$$

which is a unit in$R _ { \xi ^ { \prime } }$. We define our$z ^ { \prime }$of this case to be

$$
z ^ {\prime} = \left( \begin{array}{c c c} \mathfrak {z}, & z 0 ^ {\sharp}, & z (1) \end{array} \right)\tag{32.7}
$$

Here we have two subcases:

(a)$\vert \gamma \vert ~ = ~ \vert \gamma 0 \vert ~ \not \equiv ~ 0$mod p

(b)$| \gamma | ~ = ~ | \gamma 0 | ~ = ~ a p$with a positive integer a.

In the subcase$\mathrm { ( a ) }$we let$\ddot { o } ^ { \prime } = 0$and we define the exponent$\alpha ^ { \prime }$by setting the following equality:

$$
u ^ {\prime} z ^ {\alpha^ {\prime}} = u \mathfrak {z} ^ {| \alpha 0 | - p ^ {e - \mu}} \left(\mathfrak {z} ^ {- | \alpha 0 |} z 0 ^ {\alpha 0}\right) z (1) ^ {\alpha (1)}\tag{32.8}
$$

where$z ^ { \prime }$is the one already defined by Eq.(32.7) and$u ^ { \prime }$by Eq.(32.6). Hence the exponent of$\mathfrak { z }$in the monomial$z ^ { \prime } { } ^ { \alpha ^ { \prime } }$is equal to$| \alpha 0 | - p ^ { e - \mu }$ which is congruent to$\gamma = \gamma 0$modulo$p .$. Hence it is not congruent to 0 modulo$p .$Thus we conclude that the$p ^ { \mu \mathrm { - t h } }$power of the monomial of Eq.(32.8) is a$/ ^ { q } .$-stable form of the transform${ \mathcal { P } } ^ { \prime }$

We are now left only with the subcase (b) which is the final case and will be investigated in the next remark.

Remark 32.4. We finally have the case in which$\ddot { o } = 0 , z ^ { \gamma } = z 0 ^ { \gamma 0 }$with $\gamma ( 1 ) = 0$while$| \alpha 0 | \equiv | \gamma 0 | \equiv 0$mod$p .$. We also have

$$
o r d _ {\xi} (z 0 ^ {\gamma 0}) = o r d _ {D} (z 0 ^ {\gamma 0}) = a p
$$

with a positive integer$a .$. With$u ^ { \prime }$of$\mathrm { E q . ( 3 2 . 6 ) }$and Eq.(32.8) we define

$$
\mathrm{e} ^ {\prime} = u ^ {\prime} - v a l _ {\xi^ {\prime}} (u ^ {\prime}) \quad w h e r e\tag{32.9}
$$

$v a l _ { \xi ^ { \prime } } ( )$means evaluating at the point$\xi ^ { \prime }$

Very important is to prove the fact that$o r d _ { \xi ^ { \prime } } ( \infty ^ { \prime } ) = 1$and hence$\mathrm { { ^ x } = 0 }$ defines a smooth hypersurface in a neighborhood of$\xi ^ { \prime } \in Z ^ { \prime }$. Let us prove this. Following the notation of Eq.(32.6) we have

$$
v a l _ {\xi^ {\prime}} (u ^ {\prime}) = v a l _ {\xi^ {\prime}} (u) \prod_ {i: \mathfrak {z} ^ {- 1} z _ {i} \in \check {U}} \left(v a l _ {\xi^ {\prime}} (\mathfrak {z} ^ {- 1} z _ {i})\right) ^ {\delta_ {i}}
$$

For the sake of simplicity, we let$c _ { 0 } = v a l _ { \xi ^ { \prime } } ( u )$and$c _ { i } = v a l _ { \xi ^ { \prime } } ( \mathfrak { z } ^ { - 1 } z _ { i } )$ Let$C _ { 0 } = u$and$C _ { i } = \mathfrak { z } ^ { - 1 } z _ { i }$. Then we have

$$
\begin{array}{c} \mathrm{ae} ^ {\prime} = C _ {0} \prod_ {i} C _ {i} ^ {\delta_ {i}} - c _ {0} \prod_ {i} c _ {i} ^ {\delta_ {i}} \\ = (C _ {0} - c _ {0}) (\prod_ {i > 0} C _ {i} ^ {\delta_ {i}}) + c _ {0} (\prod_ {i > 0} C _ {i} ^ {\delta_ {i}} - \prod_ {i > 0} c _ {i} ^ {\delta_ {i}}) \\ = (C _ {0} - c _ {0}) (\prod_ {i > 0} C _ {i} ^ {\delta_ {i}}) + c _ {0} (C _ {1} ^ {\delta_ {1}} - c _ {1} ^ {\delta_ {1}}) (\prod_ {i > 1} C _ {i} ^ {\delta_ {i}}) \\ + c _ {0} c _ {1} ^ {\delta_ {1}} \Big (\prod_ {i > 1} C _ {i} ^ {\delta_ {i}} - \prod_ {i > 1} c _ {i} ^ {\delta_ {i}} \Big) \\ = \sum_ {l \leq k} \Big ((\prod_ {i <   l} c _ {i} ^ {\delta_ {i}}) (C _ {l} ^ {\delta_ {l}} - c _ {l} ^ {\delta_ {l}}) \prod_ {i > l} C _ {i} ^ {\delta_ {i}} \Big) \\ + (\prod_ {i \leq k} c _ {i} ^ {\delta_ {i}}) \Big (\prod_ {j > k} C _ {j} ^ {\delta_ {j}} - \prod_ {j > k} c _ {j} ^ {\delta_ {j}} \Big) \quad f o r e v e r y f i x e d k \\ = \sum_ {k} \Big ((\prod_ {i <   k} c _ {i} ^ {\delta_ {i}}) (C _ {k} ^ {\delta_ {k}} - c _ {k} ^ {\delta_ {k}}) \prod_ {i > k} C _ {i} ^ {\delta_ {i}} \Big) \quad s u m f o r a l l k \end{array}\tag{32.10}
$$

where we are letting$\delta _ { 0 } = 1$. Let us here remark:

(1)$\delta$is a subsystem of α and it contains all those$\alpha _ { k } = p \mathbf { b } _ { k } + \gamma _ { k }$ having$0 < \gamma _ { k } < p$. Therefore for each k,$C _ { k } ^ { \delta _ { k } } - c _ { k } ^ { \delta _ { k } }$decomposes into a sum of two summands similar to the above, one of whose is a unit multiple of$C _ { k } ^ { \gamma _ { k } } - c _ { k } ^ { \gamma _ { k } }$while the other is a unit multiple of a p-th power.

(2) For every$k \geq 1$the corresponding summand above contains a factor of the form

$$
C _ {k} ^ {\delta_ {k}} - c _ {k} ^ {\delta_ {k}} \in \mathbb {K} [ \mathfrak {z} ^ {- 1} z _ {k} ] \text {   where   } z _ {k} \in z 0
$$

and other factors of the summand are all unit.

(3) Moreover the leading term of$C _ { 0 } - c _ { 0 }$belongs to$\mathbb { K } [ \mathfrak { z } , z ( 1 ) ]$

(4) For each$k , 0 < \gamma _ { k } < p ,$

$$
o r d _ {\xi^ {\prime}} (C _ {k} ^ {\gamma_ {k}} - c _ {k} ^ {\gamma_ {k}}) = 1
$$

After all these observation we conclude that

$$
o r d _ {\xi^ {\prime}} (\mathfrak {x} ^ {\prime}) = \min _ {k} \{o r d _ {\xi^ {\prime}} (C _ {k} ^ {\gamma_ {k}} - c _ {k} ^ {\gamma_ {k}}) \} = 1
$$

With those$\mathrm { { \partial } ^ { 2 } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { } \mathrm { { } } \mathrm { { } } \mathrm { } \mathrm { { } } \mathrm { } \mathrm { { } } \mathrm \mathrm { { } } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm  \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm  \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm { } \mathrm \mathrm \mathrm \mathrm { \mathrm } \mathrm \mathrm \mathrm \mathrm  \mathrm \mathrm$and$z ^ { \prime } ,$we obtain a /<sup>q</sup>-stable exponent

$$
\mathcal {P} _ {\sharp} = \left(  f _ {\sharp} ^ {p ^ {\mu}}   \parallel   / ^ {q}  \right)\tag{32.11}
$$

which is defined locally at$\xi ^ { \prime }$by

$$
f _ {\sharp} = z ^ {\prime \alpha^ {\prime}} w ^ {\prime \ddot {o} ^ {\prime}}\tag{32.12}
$$

where$\ddot { o } ^ { \prime } = 1$and$\alpha ^ { \prime }$is determined by the equality

$$
u ^ {\prime} z ^ {\alpha^ {\prime}} = u \mathfrak {z} ^ {p | \mathbf {b} (0) | - p ^ {e - \mu}} \left(\mathfrak {z} ^ {- 1} z 0\right) ^ {p \mathbf {b} (0)} z (1) ^ {p \mathbf {b} (1)}\tag{32.13}
$$

It is clear that$\alpha ^ { \prime }$is divisible by$p .$We define$\mathbf { b } ^ { \prime }$and$c 0 \in \mathbb { K }$by

$$
\alpha^ {\prime} = p \mathbf {b} ^ {\prime} a n d v a l _ {\xi^ {\prime}} (u ^ {\prime}) = c 0 ^ {q}\tag{32.14}
$$

We next define and investigate a kind of spin-of, denoted${ \mathcal P } _ { \flat }$, out of the transformation of$\mathcal { P }$by the blowup π.

Remark 32.5. Define an integer$\mu ^ { \prime }$and a constant$v \in \mathbb { K }$by

$$
\mu^ {\prime} = \mu + \nu^ {\prime} a n d v = c 0 ^ {p ^ {e - \mu^ {\prime}}} w h e r e\tag{32.15}
$$

$$
\nu^ {\prime} = \max \left\{\nu \mid 0 <   \nu \leq e a n d z ^ {\alpha^ {\prime}} \in \rho^ {\nu} \left(R _ {\xi^ {\prime}}\right) \right\}.
$$

$$
v = c 0 ^ {p ^ {\mu - \mu^ {\prime}}} \in \mathbb {K} \text { with } c 0 \text { of } E q. (3 2. 1 4).
$$

We can then find$f _ { \mathfrak { b } } \in R _ { \xi ^ { \prime } }$such that

$$
z ^ {\prime \alpha^ {\prime}} = f _ {b} ^ {\nu^ {\prime}}\tag{32.16}
$$

The transform${ \mathcal { P } } ^ { \prime }$is then written as follows:

(1) If$\mu ^ { \prime } = e$then locally within a suficiently small neighborhood of$\xi ^ { \prime } \in Z ^ { \prime }$we have

$$
\mathcal {P} ^ {\prime} = \mathcal {P} _ {\sharp} = \left(f _ {\sharp} ^ {p ^ {\mu}} \| / ^ {q}\right)
$$

which is /<sup>q</sup>-stable.

(2) If$0 < \mu ^ { \prime } < e$then we have another /<sup>q</sup>-stable exponent${ \mathcal { P } } _ { \flat }$

$$
\begin{array}{r} \mathcal {P} _ {\flat} = (f _ {\flat} ^ {p ^ {\mu^ {\prime}}} \| / ^ {q}) \\ w i t h f _ {\flat} = v z ^ {\prime \alpha^ {\prime \prime}}, \alpha^ {\prime \prime} = \frac {\alpha^ {\prime}}{\nu^ {\prime}} (R e f e r t o E q. (3 2. 1 5)) \\ \mathcal {P} ^ {\prime} = (f _ {\sharp} ^ {p ^ {\mu}} + f _ {\flat} ^ {p ^ {\mu^ {\prime}}} \| / ^ {q}) \end{array}\tag{32.17}
$$

In the last case the transform${ \mathcal { P } } ^ { \prime }$is$\textrm { a } / { } ^ { q }$-extension of the$/ ^ { q } .$-stable$\mathcal { P } _ { \sharp }$ of depth$\mu$by the$/ ^ { q } \mathrm { - s t a b l e }$${ \mathcal { P } } _ { \flat }$of depth$\mu ^ { \prime } > \mu$. We have thus completed the proof of the theorem Th.(32.2).

We sometimes call${ \mathcal P } _ { \flat }$a spin-${ \cdot o f f }$of the transformation of$\mathcal { P }$by the blowup$\pi .$. The following special case of Th.(32.2) will be found very useful later.

Theorem 32.3. In the case of$q = p$of the theorem Th.(32.2) there exists no spin-of. Namely the transform of stable exponent by a Γ-pure permissible blowup is stable by itself.

## 33. /<sup>q</sup>-metastable Singularity

Let$\pi : Z ^ { \prime } \longrightarrow Z$with center D be a fitted permissible blowup for${ \mathcal { G } } =$ $\left( \mathbf { g } \parallel \mathbf { \Lambda } / \mathbf { \Lambda } ^ { q } \right)$in the sense of Def.(31.2) and in particular it is permissible for $\check { \mathcal { G } }$, which denotes the checked associate of$\mathcal { G }$in the sense of Def.(19.4). Let$\mathcal { G } ^ { \prime }$be the transform of$\mathcal { G }$by$\pi .$. Let$\xi \in S i n g ( \mathcal { G } ) \subset Z$be a closed point and pick a closed point$\xi ^ { \prime } \in \ . S i n g ( \mathcal { G } ^ { \prime } ) \cap \pi ^ { - 1 } ( \xi )$We want to examine the efect of such a blowup to the invariant resor$d _ { \xi } ( \mathcal G )$in the sense of Eq.(19.1) of Def.(19.3).

We normally expect resor$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) \ \leq$resord<sub>ξ</sub>(G). (The singularity did not get worse !) But sometimes it happens that resor$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) >$ resor$d _ { \xi } ( \mathcal G )$

Following is the most interesting case to be examined closely:

$$
\operatorname{resord} _ {\xi^ {\prime}} \left(\mathcal {G} ^ {\prime}\right) > \operatorname{resord} _ {\xi} (\mathcal {G}) \text {   while   } \operatorname{ord} _ {\xi} (\check {\mathcal {G}}) = \operatorname{ord} _ {D} (\check {\mathcal {G}}),\tag{33.1}
$$

where$o r d _ { D } ( \check { \mathcal { G } } ) = o r d _ { \zeta } ( \check { \mathcal { G } } )$by definition with the generic point$\zeta$of$D$.

Definition 33.1. When we have Eq.(33.1), we call$\xi ^ { \prime }$a metastable singular point of$\mathcal { G }$at$\xi$for$\pi$(in short, metastable point for π).

Remark 33.1. We follow the manner of Re.(20.1) in choosing parameters$z = ( v , w )$with$v = ( v _ { 1 } , \cdots , v _ { t } )$where$z$consists of those parameters defining the components of Γ containing$\xi$. We follow the manner of abc-expression of Def.(20.1) but here we use an expression$\mathcal { G } =$ $\left( \nabla f \parallel / \vphantom { \nabla } q \right)$locally at the point$\xi$where$\nabla = z ^ { \alpha } = z ^ { q \beta } z ^ { \gamma }$is Γ-maximal divisor and$z ^ { q \beta }$is its$q \Gamma$-factor in the sense of$( 1 9 . 1 )$. We choose$f$to be a residual factor of$\mathcal { G }$so that we have resor$d _ { \xi } ( \mathcal { G } ) = o r d _ { \xi } ( f )$according to Def.(19.3). We also write$z ^ { \gamma } = v ^ { \delta }$with$0 < \delta _ { j } < q , \forall j$

We are given a blowup$\pi$with center D with respect to which we selecting additional parameter$\omega$in such a way that$x = \left( z , \omega \right)$is a regular system of paramers of$R _ { \xi }$with the$z = ( v , w )$and moreover the following conditions are satisfied.

(1) The ideal$I _ { \xi }$of D at$\xi$is$( v ^ { \dagger } , w ^ { \dagger } , \omega ^ { \dagger } ) R _ { \xi }$where$v ~ = ~ ( v ^ { \dagger } , v ^ { \ddagger } )$ $w = ( w ^ { \dagger } , w ^ { \ddagger } )$and$\omega = ( \omega ^ { \dagger } , \omega ^ { \dagger } )$

(2)$v _ { j } R _ { \xi ^ { \prime } } = I _ { \xi } R _ { \xi ^ { \prime } } , \mathrm { i . e . , } v _ { j }$is an exceptional parameter for$\pi$at$\xi ^ { \prime }$

In this section we take the following notational simplification in our study of metastable singularity:

(1)$j = 1$

(2) all the components of$v _ { 1 } ^ { - 1 } \omega ^ { \dagger }$take zero values at$\xi ^ { \prime }$.

(3) every component of$v _ { 1 } ^ { - 1 } ( v ^ { \dagger } , w ^ { \dagger } )$takes a value at$\xi ^ { \prime }$which is either zero or 1.

These can always achieved by a simple coordinate transformation.

Proposition 33.1. ( T. Moh and H. Hauser) Assume that$\xi ^ { \prime }$is a metastable singular point of$\mathcal { G } ^ { \prime }$for π. Then we have

(1) the center D is contained in every$\Gamma _ { j }$for$1 \leq j \leq t$

(2)$\xi ^ { \prime }$is not in any of the strict transforms of$\Gamma _ { j } , 1 \leq j \leq t$, by π.

(3)$o r d _ { \xi } ( \mathcal { G } )$is divisible by q, which is equivalent to saying that$| \gamma | + d$ is divisible by q where$d = r e s o r d _ { \xi } ( \mathcal { G } )$

The first assertion implies that$v = v ^ { \dagger }$and$v ^ { \ddag } = \emptyset$

Remark 33.2.$v _ { 1 } ^ { - 1 } v _ { j } , 1 \leq j \leq t - 1$, takes nonzero values at$\xi ^ { \prime }$. With no loss of generality we may and will assume that

(33.2) the values$( v _ { 1 } ^ { - 1 } v _ { j } ) ( \xi ^ { \prime } ) = 1 , 1 \leq j \leq t - 1$, and let$\theta = t - 1$ Let us divide$w ^ { \dagger }$into two parts$w ^ { \dagger } = ( w ^ { \dagger } ( 1 ) , w ^ { \dagger } ( 2 ) )$in such a way that $v _ { 1 } ^ { - 1 } w ^ { \dagger } ( 2 )$vanish at$\xi ^ { \prime }$while none of$v _ { 1 } ^ { - 1 } w ^ { \dag } ( 1 )$does. We again assume

$$
\text {   the   values   } (v _ {1} ^ {- 1} w _ {j} ^ {\dagger}) (\xi^ {\prime}) = 1, \forall w _ {j} ^ {\dagger} \in w ^ {\dagger} (1)\tag{33.3}
$$

so that$v _ { 1 } ^ { - 1 } w ^ { \dagger } ( 1 ) - i d _ { a }$will become a part of a regular system of parameters of$R _ { \xi ^ { \prime } }$where$i d _ { a } = ( 1 , 1 , \cdots , 1 )$with the size a of$w ^ { \dagger }$

Theorem 33.2. Let$\mathbf { d } = r e s o r d _ { \xi } ( \mathcal { G } )$. If there exists a smooth subscheme$D \ni \xi$which is generic-down type for$\mathcal { G }$at$\xi$in the sense of $D e f . ( 2 ? )$then we must have

$$
\textbf {c} + \textbf {d} \equiv 1 \mod p
$$

for the c of the expression of$E q . ( 2 0 . 1 )$. It follows that if any such D exists at all then metastable singularity cannot occur with any permissible center.

Let us write$\alpha = q \beta + \gamma \in \mathbb { Z } _ { 0 } ^ { n }$with$0 \leq \gamma _ { i } < q , \forall i$. We have the q-supplement of$\gamma$in the sense of Def.(22.1), the same of$\alpha _ { \mathrm { { ; } } }$, which is to be the unique element$\gamma ^ { \ast } \in \mathbb { Z } _ { 0 } ^ { t }$such that$\alpha + \gamma ^ { * } \equiv 0$mod$( q )$and $0 \leq \gamma _ { j } ^ { * } < q$for all$i , 1 \le j \le t$

Remark 33.3. Let$d = r e s o r d _ { \xi } ( \mathcal { G } )$. We then begin with$Q _ { N } ( d )$-cleaning a given residual f of G with respect to$\{ \lambda ^ { q } v ^ { \bar { \gamma } ^ { * } } | \lambda \in R _ { \xi } \}$. ( Refer to Def.(13.2) and Def.(??). ) It follows, for instance, that or$\cdot d _ { \xi } ( f ) =$ $r e s o r d _ { \xi } ( \mathcal { G } )$

Then$\xi ^ { \prime }$is metastable if and only if we have$\sigma \in \rho ^ { e } ( R _ { \xi ^ { \prime } } )$such that

$$
\operatorname{ord} _ {\xi^ {\prime}} \left(v _ {t} ^ {- d - | \gamma |} (v ^ {\gamma} f) - \sigma^ {q}\right) > d.\tag{33.4}
$$

Remark 33.4. Here we choose$\sigma$in such a way that the left hand side is maximal among all choices, so that the left number of Eq.(33.4) is equal to$r e s o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } )$. In this way we can later readily investigate the question of how big the residual order resor$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } )$can become at the given metastable point$\xi ^ { \prime } \in \pi ^ { - 1 } ( \xi )$

We write

$$
f = f (d) + f ^ {\sharp} \text {   with   } \operatorname{ord} _ {\xi} \left(f ^ {\sharp}\right) > d\tag{33.5}
$$

where$f ( d )$is a homogeneous polynomial of degree d in the variables $( v , w ^ { \dagger } , \omega ^ { \dagger } )$. Since$v _ { 1 } ^ { - | \gamma | } v ^ { \gamma }$is a unit in$R _ { \xi ^ { \prime } }$we then have the total metastable inequality

$$
\operatorname{ord} _ {\xi^ {\prime}} \left(v _ {1} ^ {- d} f ^ {\sharp} + \left(v _ {1} ^ {- d} f (d) - \left(v _ {1} ^ {- | \gamma |} v ^ {\gamma}\right) ^ {- 1} \sigma^ {q}\right)\right) > d\tag{33.6}
$$

$$
v _ {1} ^ {- d} f ^ {\sharp} \in (v _ {1}, w ^ {\ddagger}, \omega^ {\ddagger}) R _ {\xi^ {\prime}}
$$

where the last inclusion is due to

$$
f ^ {\sharp} \in I _ {\xi} ^ {d} \cap M _ {\xi} ^ {d + 1} = M _ {\xi} I _ {\xi} ^ {d} = (w ^ {\ddagger}, \omega^ {\ddagger}) I _ {\xi} + I _ {\xi} ^ {2}.
$$

It should be noted here that we have a regular system of parameters of$R _ { \xi ^ { \prime } }$composed of the following two parts:

$$
(v _ {1}, v _ {1} ^ {- 1} w ^ {\dagger} (1) - i d _ {a}, v _ {1} ^ {- 1} w ^ {\dagger} (2), w ^ {\ddagger}, v _ {1} ^ {- 1} \omega^ {\dagger}, \omega^ {\ddagger})\tag{33.7}
$$

$$
i n a d d i t i o n t o v _ {1} ^ {- 1} v _ {j} - 1, 1 \leq j <   t
$$

where$i d _ { a } = ( 1 , 1 , \cdots , 1 )$with the size a of$w ^ { \dag } ( 1 )$

Let$\theta = t - 1$and we define what we call metastable parameters$T .$

$$
T = \left(v _ {1} ^ {- 1} v _ {1} - 1, \dots , v _ {1} ^ {- 1} v _ {\theta} - 1\right) a n d i d _ {\theta} = (1, \dots , 1)\tag{33.8}
$$

in such a way that$i d _ { \theta } + T$is$v _ { 1 } ^ { - 1 } v$of which$v _ { 1 } ^ { - 1 } v _ { 1 } ( = 1 )$is deleted.

Let us also write

$$
U = (v _ {1}, v _ {1} ^ {- 1} w ^ {\dagger} (1) - i d _ {a}, v _ {1} ^ {- 1} w ^ {\dagger} (2), w ^ {\ddagger}, v _ {1} ^ {- 1} \omega^ {\dagger}, \omega^ {\ddagger})\tag{33.9}
$$

$$
\text { which   will   be   written   as } (v _ {1}, U _ {1}, \dots , U _ {\vartheta})
$$

We divide U into 3 partitions as

$$
U = \left(v _ {1}, U (1), U (2)\right) w h e r e\tag{33.10}
$$

$$
v _ {1} \text {is the exceptional parameter for} \pi \text {at} \xi^ {\prime}
$$

$$
\begin{array}{r l} {U (1) = (v _ {1} t ^ {- 1} w ^ {\dagger} (1) - i d _ {a}, v _ {1} ^ {- 1} w ^ {\dagger} (2), v _ {1} ^ {- 1} \omega^ {\dagger})} \\ {a n d U (2) = (w ^ {\ddagger}, \omega^ {\ddagger})} \end{array}
$$

We will later make use of the above partitions of our parameters. We should keep in mind that

$$
(v _ {1}, T, U (1), U (2))\tag{33.11}
$$

is a regular system of parameters of$R _ { \xi ^ { \prime } }$

$$
s o t h a t \hat {R} _ {\xi^ {\prime}} = K [ [ v _ {1}, T, U (1), U (2) ] ]
$$

where$\hat { R } _ { { \xi } ^ { \prime } }$denotes the completion of$R _ { \xi ^ { \prime } }$and$K$is its coeficient field which is a separable algebraic extension of$\mathbb { K }$.

Remark 33.5. We let

$$
\gamma^ {*} = (\gamma^ {\flat}, \gamma_ {1}), \text { so   that } | \gamma^ {\flat} | = | \gamma^ {*} | - \gamma .\tag{33.12}
$$

Namely$V ^ { \gamma ^ { \flat } }$is the product$\textstyle \prod _ { j = 1 } ^ { \theta } V _ { j } ^ { \gamma _ { j } ^ { * } }$for a system$V$of length$\theta$and for exponent$\gamma ^ { * }$of length$t = \theta ^ { ' } + 1$, where$\gamma ^ { * }$is q-supplement to$\gamma$in the sense of Def.(22.1). For instance we have the metastable unit

$$
\left(v _ {1} ^ {- | \gamma |} v ^ {\gamma}\right) ^ {- 1} = (i d _ {\theta} + T) ^ {- \gamma} = (i d _ {\theta} + T) ^ {- q i d} (i d _ {\theta} + T) ^ {\gamma^ {\flat}}\tag{33.13}
$$

where in the middle term the last component of the exponent$- \gamma$is conventionally neglected. (Think of adding one more component$1 + T _ { 1 }$ to$( i d _ { \theta } + T )$with$T _ { 1 } = 0 . )$

Pick any$\sigma$of Rem.(33.4) and then let

$$
\tau = (i d _ {\theta} + T) ^ {- i d _ {\theta}} \sigma \text { with a chosen } \sigma .\tag{33.14}
$$

We rewrite Eq.(33.6) with this$\tau$as follows, and we have that$\xi ^ { \prime }$is metastable for$\pi$if and only if we have$\tau$such that

$$
\begin{array}{c} \text {the basic metastable inequality} \\ o r d _ {\xi^ {\prime}} \Big (v _ {1} ^ {- d} f ^ {\sharp} + \big (v _ {1} ^ {- d} f (d) - (i d _ {\theta} + T) ^ {\gamma^ {\flat}} \tau^ {q} \big) \Big) > d \\ \text {where} \\ v _ {1} ^ {- d} f ^ {\sharp} \in (v _ {1}, U (2)) R _ {\xi^ {\prime}} \end{array}\tag{33.15}
$$

where$\tau$must be chosen to make the left hand side of the inequality $\operatorname { E q } .$.(33.15) maximal among all choices. ( Respect to Rem.(33.4).)

It should also be noted that since$f ( d )$is a homogeneous polynomial of degree$d$only in the variables$( v , w ^ { \dagger } , \omega ^ { \dagger } ) , v _ { 1 } ^ { - d } f ( d )$does not have any nonzero monomial terms divisible by any of the variables$( v _ { 1 } , U ( 2 ) )$so that we have

$$
v _ {1} ^ {- d} f (d) \text {   in   } \mathbb {K} [ T, U (1) ].
$$

Let us write$\tau$in two parts

$$
\begin{array}{c} \tau = \tau (1) + \tau (2) w i t h \\ \tau (1) \in \mathbb {K} [ U (1), T ] a n d \tau (2) \in (v _ {1}, U (2)) R _ {\xi^ {\prime}} \end{array}\tag{33.16}
$$

Now, taking the inequality Eq.(33.15) modulo$( v _ { 1 } , U ( 2 ) ) R _ { \xi ^ { \prime } }$, we obtain the following key inequality

$$
\begin{array}{c} \tau (1) \in \mathbb {K} [ U (1), T ] a n d \\ o r d _ {\xi^ {\prime}} \Big (v _ {1} ^ {- d} f (d) - \big (i d _ {\theta} + T \big) ^ {\gamma^ {b}} \tau (1) ^ {q} \Big) > d \end{array}\tag{33.17}
$$

Here it is important that the combined system of Eq.(33.7) is a regular system of parameters of$R _ { \xi ^ { \prime } }$

Theorem 33.3. Let$F ( T , U ( 1 ) ) ~ = ~ v _ { 1 } ^ { - d } f ( d )$, which is a polynomial in $K [ T , U ( 1 ) ]$$I f \xi ^ { \prime }$is a metastable point of the transform G′ of G by$\pi$ then there exists$\tau = \tau ( 1 ) + \tau ( 2 ) \in R \varepsilon ^ { \prime }$with respect to Rem.$( { \it 3 3 . 4 } )$and $\tau ( 1 ) \in K [ T , U ( 1 ) ]$according to$E q . ( 3 3 . 1 6 )$in such a way that

fundamental metastable equality

$$
F (T, U (1)) = \left[ (i d _ {\theta} + T) ^ {\gamma^ {b}} \tau (1) ^ {q} \right] _ {d}\tag{33.18}
$$

where$[ ] _ { d }$means the partial obtained by summing up all the monomial terms of degrees ≤ d in a polynomial (or power series) with respect to the chosen variables. Moreover we automatically have or can choose $\tau ( 1 )$in order to have the following properties:

(1)$F ( T , U ( 1 ) )$is a polynomial of$d e g r e e \leq d ,$

(2)$\tau ( 1 ) \neq 0$because${ \cal F } ( T , { \cal U } ( 1 ) ) \not = 0 \ :$

(3) the leading homogeneous part of$F ( T , U ( 1 ) )$is a q-th power by the equality Eq.(33.18).

(4) The nonzero monomial terms of$( i d _ { \theta } + T ) ^ { \gamma ^ { \flat } }$are$\rho ^ { e } ( R _ { \xi ^ { \prime } } )$-linearly independent. In fact the components$o f \gamma ^ { \flat }$are$a l l \le q - 1$and T extends to a regular system of parameters of$R _ { \xi ^ { \prime } }$

(5) We may choose$\tau ( 1 ) \in K [ T , U ( 1 ) ]$without afecting$E q . ( 3 3 . 1 8 )$ and Rem.(33.4). (We may even choose$d e g ( \tau ( 1 ) ^ { q } ) \leq d$without afecting$E q . ( 3 3 . 1 8 )$by itself.)

(6) We have or$\cdot d _ { ( T , U ( 1 ) ) } ( \smash { \xrightarrow [ ] { T ( T , U ( 1 ) ) } } ) > d - | \gamma ^ { \flat } |$. This is due to the cleaning Rem.(33.3) of f by means$o f v ^ { \gamma ^ { \flat } }$

(7) We can choose τ (1) such that or$d _ { \xi ^ { \prime } } ( \tau ( 1 ) ^ { q } ) = o r d _ { ( T , U ( 1 ) ) } ( \tau ( 1 ) ^ { q } ) =$ $o r d _ { ( T , U ( 1 ) ) } ( F ( T , U ( 1 ) ) ) > d - | \gamma ^ { \flat } |$

(8)$W e \ h a v e \ F ( T , U ( 1 ) ) \ \in \ K [ T , \rho ^ { e } ( U ( 1 ) ) ] .$

(9)$T$is Γ′-transversal at$\xi ^ { \prime }$where Γ′ is the NC-transform of Γ by π in the sense of Def.(12.2). In fact the subsystem$( v _ { 1 } , v _ { 1 } ^ { - 1 } w ^ { \dag } ( 2 ) , w ^ { \ddag } )$ of$E q . ( 3 3 . 7 )$is the system of parameters defining those members of$\Gamma ^ { \prime }$passing through$\xi ^ { \prime }$and the combined system

$$
(T, v _ {1}, v _ {1} ^ {- 1} w ^ {\dagger} (2), w ^ {\ddagger})
$$

extends to a regular system of parameters of$R _ { \xi ^ { \prime } }$by Eq.(33.7).

Corollary 33.4. The fundamental metastable equality Eq.(33.18) is written more explicitly as follows. Let us write

$$
\tau (1) ^ {q} = \sum_ {\frac {d - | \gamma^ {*} |}{q} <   l \leq \frac {d}{q}} \tau_ {l} ^ {q}
$$

where$\tau _ { l }$is a homogeneous polynomial of degree l in$K [ T , U ( 1 ) ]$. Let us use the symbol$\{ \} _ { a }$to denote the homogeneous part of degree a. Then we have

$$
F (T, U (1)) = \sum_ {\frac {d - | \gamma^ {*} |}{q} <   l \leq \frac {d - b}{q}} \sum_ {b \leq d - l q} \left\{(i d _ {\theta} + T) ^ {\gamma^ {b}} \right\} _ {b} \tau_ {l} ^ {q}.
$$

Moreover it follows that

$$
F (T, U (1)) = \sum_ {\frac {d - | \gamma^ {*} |}{q} <   l \leq \frac {d}{q}} \left[ (i d _ {\theta} + T) ^ {\gamma^ {b}} \right] _ {d - l q} \lambda_ {l} ^ {q}
$$

with certain homogeneous polynomial$\lambda _ { l }$of degree l in$K [ T , U ( 1 ) ]$, so that

$$
f (d) = \sum_ {l q + b = d} \Lambda_ {l} ^ {q} \Phi_ {b}
$$

where$\Lambda _ { l } = v _ { 1 } ^ { l } \lambda _ { l }$and$\Phi _ { b } = v _ { 1 } ^ { b } \Bigl [ ( i d _ { \theta } + T ) ^ { \gamma ^ { \flat } } \Bigr ]$with$0 \leq b < | \gamma ^ { \flat } |$. Note b that$\Phi _ { b }$is$a$homogeneous polynomial of degree b in$K [ v ]$and that$\Phi _ { b } \notin$ $K [ v ^ { q } ]$

Theorem 33.5. Let$F ( T , U ( 1 ) ) ~ = ~ v _ { 1 } ^ { - d } f ( d )$as was in Th.(33.3). Let $\tau ^ { \sharp ^ { q } }$be the sum of those terms of$F ( T , U ( 1 ) )$which belong to$\rho ^ { e } ( R _ { \xi ^ { \prime } } )$. If $\xi ^ { \prime } \in S i n g ( \mathcal { G } ^ { \prime } )$is metastable of G for π then we can choose$\tau ^ { \sharp }$instead of τ (1) in$E q . ( 3 3 . 1 8 )$as follow.

$$
F (T, U (1)) = \left[ (i d _ {\theta} + T) ^ {\gamma^ {b}} \tau^ {\sharp q} \right] _ {d}\tag{33.19}
$$

Theorem 33.6. Under the metastable assumption, the number d of Th.(33.3) cannot have$| \gamma ^ { * } | > d \geq | \gamma ^ { \flat } |$. With respect to

$$
\check {d} = \operatorname{ord} _ {\xi^ {\prime}} \left(v _ {1} 1 ^ {- d} f (d)\right) = \operatorname{ord} _ {\xi^ {\prime}} \left(\tau (1) ^ {q}\right)\tag{33.20}
$$

the inequality$\breve { d } > d - | \gamma ^ { \flat } |$of$T h . ( 3 3 . 3 )$is useful (after the cleaning of Rem.(33.3)) when$d \geq | \gamma ^ { * } |$, while this theorem is significant when $d < | \gamma ^ { * } | = | \gamma ^ { \flat } | + \gamma _ { 1 }$

## 34. Moh’s theory for$q = p$

In this section we are primarily interested in the case of$q = p$and examine the special feature of metastable phenomena in the special case with$e = 1$of$q = p ^ { e }$. However we first start with the assumption and notation for the case of general$q = p ^ { e } , e > 0$, before we specialize our interest to the case of$q = p$. We are given a closed point$\xi \in \ S i n g ( \mathcal { G } )$.

$$
\mathcal {G} = \left(\textbf {g} \right\rVert / ^ {q}) w i t h \textbf {g} = z ^ {q \beta} v ^ {\gamma} h
$$

where$z ^ { q \beta }$is the q-factor,$v ^ { \gamma }$is the q-cofactor and h is a residual factor of$\mathcal { G }$Also${ z } = ( \boldsymbol { v } , \boldsymbol { w } )$is the system of parameters defining those components of Γ passing through$\xi ,$$0 ~ < ~ \gamma _ { i } ~ < ~ q$for every i and $d = o r d _ { \xi } ( \mathbf { g } ) = r e s o r d _ { \xi } ( \mathcal { G } )$Moreover$h$is cleaned by$v ^ { \gamma ^ { * } }$according to Rem.(33.3) with the supplement$\gamma ^ { * }$of$\gamma$in the sense of Def.(22.1). We write$h = h ( d ) + h ^ { \sharp }$with$o r d _ { \xi } ( { \bf g } ^ { \sharp } ) > d$according to Eq.(33.5).

We also have the transform$\mathcal { G } ^ { \prime }$of a given /<sup>q</sup>-exponent by a permissible blowup$\pi : Z ^ { \prime } \longrightarrow Z$with center$D$.

Attention: In this section, we are not assuming$d \ > \ 0$a priori. However if$d = 0$then we must have$\gamma \neq 0$

From now on we pick a closed point$\xi ^ { \prime }$in$S i n g ( \mathcal { G } ^ { \prime } ) \cap \pi ^ { - 1 } ( \xi )$and assume that$\xi ^ { \prime }$is a metastable point of$\mathcal { G } ^ { \prime }$for the blowup$\pi$.

We will follow the notation of the earlier sections in regards to our selection of parameters according to Rem.(20.1). We have$x = ( z , \omega )$ $z = ( v , w ) , w = ( w ^ { \dag } , w ^ { \dag } )$and$\omega = ( \omega ^ { \dagger } , \omega ^ { \ddagger } )$so that$( \boldsymbol { v } , \boldsymbol { w } ^ { \dagger } , \boldsymbol { \omega } ^ { \dagger } )$generates the ideal of$D$at$\xi$. Our exceptional parameter at$\xi ^ { \prime }$is chosen to be$v _ { 1 }$ according to Eq.(33.2) of Rem.(33.2). We let$v = \left( v _ { 1 } , \cdots , v _ { t } \right)$and let $c _ { j - 1 } \in$K denote the value of$v _ { 1 } ^ { - 1 } v _ { j }$at$\xi ^ { \prime }$for every$j > 1$. We define variables$T _ { j - 1 } = v _ { 1 } ^ { - 1 } v _ { j } - c _ { j }$and$T = ( T _ { 1 } , \cdot \cdot \cdot , T _ { \theta } )$with$\theta = t - 1$in the manner of Eq.(33.8). Write$c = ( c _ { 1 } , \cdots , c _ { \theta } )$. We choose σ by Eq.(33.4), and $\tau$by Eq.(33.14). We write$\tau = \tau ( 1 ) + \tau ( 2 )$by Eq.(33.16). We choose variables$U = ( v _ { 1 } , U ( 1 ) , U ( 2 ) )$and ϑ of Eq.(33.9) and$\mathrm { E q . ( 3 3 . 1 0 ) }$. Thus $( v _ { 1 } , T , U ( 1 ) , U ( 2 ) )$of Eq.(33.11) is the regular system of parameters Eq.(33.7) of$R _ { \xi ^ { \prime } }$

We then have the basic metastable inequality Eq.(33.15)

$$
\operatorname{ord} _ {\xi^ {\prime}} \left(v _ {1} ^ {- d} h ^ {\sharp} + \left(v _ {1} ^ {- d} h (d) - (c + T) ^ {\gamma^ {\flat}} \tau^ {q}\right)\right) > d\tag{34.1}
$$

with$\gamma ^ { \flat }$is obtained from$\gamma$by deleting its first component. Let$\tau ( * )$ denote the initial homogeneous part of$\tau ( 1 )$of$\mathrm { E q . ( 3 3 . 1 5 ) }$so that$\tau ( * ) ^ { q }$ is a homogeneous polynomial of degree$d - | \gamma ^ { \flat } | + k$with an integer k such that$0 < k \leq | \gamma ^ { \flat } |$by Th.(33.3).

For notational simplicity, let us write

$$
A _ {d + 1} = v _ {1} ^ {- d} h ^ {\sharp} - (c + T) ^ {\gamma^ {\flat}} \tau (2) ^ {q} \in (v _ {1}, U (2)) R _ {\xi^ {\prime}}\tag{34.2}
$$

$$
B _ {d + 1} = \left(\tau (1) ^ {q} (c + T) ^ {\gamma^ {b}} - \left[ \tau (1) ^ {q} (c + T) ^ {\gamma^ {b}} \right] _ {d + 1}\right)
$$

and

$$
C _ {d + 1} (1) = \tau (*) ^ {q} \bigl \{(c + T) ^ {\gamma^ {b}} \bigr \} _ {| \gamma^ {b} | - k + 1}\tag{34.3}
$$

where$\{ \ \} _ { a } = [ \ ] _ { a } - [ \ ] _ { a - 1 }$after the notation of Cor.(33.4), that is

$$
C _ {d + 1} (1) = \tau (*) ^ {q} \left(\left[ (c + T) ^ {\gamma^ {\flat}} \right] _ {| \gamma^ {\flat} | - k + 1} - \left[ (c + T) ^ {\gamma^ {\flat}} \right] _ {| \gamma^ {\flat} | - k}\right)
$$

which is in$K [ T , U ( 1 ) ^ { q } ]$

$$
\begin{array}{r l} C _ {d + 1} (2) = & [ (\tau (1) ^ {q} - \tau (*) ^ {q}) (c + T) ^ {\gamma^ {b}} ] _ {d + 1} \\ \in & \rho^ {e} (R _ {\xi^ {\prime}}) [ (c + T) ^ {\gamma^ {b}} ] _ {| \gamma^ {b} | - k} \end{array}
$$

We then rewrite the above Eq.(34.1) as

$$
\begin{array}{c} o r d _ {\xi^ {\prime}} \Big (v _ {1} ^ {- d} h - (c + T) ^ {\gamma^ {b}} \tau^ {q} \Big) > d \\ w h e r e \\ v _ {1} ^ {- d} f - (c + T) ^ {\gamma^ {b}} \tau^ {q} \\ = \left(A _ {d + 1} - B _ {d + 1} - C _ {d + 1} (2)\right) + C _ {d + 1} (1) \end{array}\tag{34.4}
$$

in which

(1)$o r d _ { \xi ^ { \prime } } ( B _ { d + 1 } ) > d + 1$

(2)$C _ { d + 1 } ( 1 )$have no nonzero common monomial terms with any one of$A _ { d + 1 } , B _ { d + 1 }$and$C _ { d + 1 } ( 2 )$

(3)$C _ { d + 1 } ( 1 )$is homogeneous of degree$d + 1$in$K [ T , U ( 1 ) ]$unless it is zero,

(4)$C _ { d + 1 } ( 1 ) \in K [ T , U ( 1 ) ^ { q } ]$and it is a partial sum of the power series expansion of

$$
\left(A _ {d + 1} - B _ {d + 1} - C _ {d + 1} (2)\right) + C _ {d + 1} (1) \in K [ [ v _ {1}, T, U (1), U (2) ] ]. \tag {34.5}
$$

Definition 34.1. The polynomial$C _ { d + 1 } ( 1 ) \in K [ T , U ( 1 ) ^ { q } ]$of$\mathrm { E q . ( 3 4 . 3 ) }$ will be called resord-core of the transform$\mathcal { G } ^ { \prime }$of G by π at the metastable point$\xi ^ { \prime }$with respect to$x ^ { \prime } = ( v _ { 1 } , T , U ( 1 ) , U ( 2 ) )$which is a regular system of parameter of$R _ { \xi ^ { \prime } }$. It is homogeneous polynomial of degree $d + 1$and a partial sum in the power series expansion of Eq.(34.5).

We have the following special case of the theorem of T.T.Moh, [29], and we reprove it in the manner which we prefer for the purpose of the subsequent$/ ^ { q } .$-reduction theorems.

Theorem 34.1. (T.T. Moh) Let us consider the case of$q = p$. Then we have resor$\cdot d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) \leq r e s o r d _ { \xi } ( \mathcal { G } ) + 1$. The essence of this assertion is that$i f \xi ^ { \prime }$is a metastable point of the the transform G′ of G by π then the resord-core$C _ { d + 1 } ( 1 )$of$D e f . ( 3 4 . 1 )$is nonzero.

In the case of$e \ = \ 1$and$q \ = \ p$the polynomial$( c + T ) ^ { \gamma ^ { \flat } }$has a special property that it has nonzero coeficients exactly to the following monomials:

$$
\left\{T ^ {\delta} \mid 0 \leq \delta_ {j} \leq \gamma_ {j} ^ {\flat} <   p \forall j, 1 \leq j \leq \theta \right\}\tag{34.6}
$$

This is by the binomial theorem. Recall$\mathrm { E q . ( 3 4 . 3 ) }$which says

$$
C _ {d + 1} (1) = \tau (*) ^ {q} \bigl \{(c + T) ^ {\gamma^ {b}} \bigr \} _ {| \gamma^ {b} | - k + 1}
$$

where$d + 1 - d e g ( \tau ( * ) ^ { q } ) = | \gamma ^ { \flat } | - k + 1$. We claim that

$$
\left| \gamma^ {b} \right| \geq d + 1 - \deg (\tau (*) ^ {q}) \geq 1 a n d C _ {d + 1} (1) \neq 0.\tag{34.7}
$$

Thanks to Th.(33.6) we have either d$< | \gamma ^ { \flat } |$or$d \geq | \gamma ^ { * } |$. We thus have to examine these two cases. Note that in any case we have$d \geq$ $d e g ( \tau ( * ) ^ { q } ) \geq 0$. First consider the case of$d < | \gamma ^ { \flat } |$and then

$$
| \gamma^ {b} | \geq d + 1 \geq d + 1 - d e g (\tau (*) ^ {q}) \geq 1
$$

As for$C _ { d + 1 } ( 1 ) \neq 0$, the inequality$| \gamma ^ { \flat } | - k + 1 = d + 1 - d e g ( \tau ( * ) ^ { q } ) \geq 1$ while$| \gamma ^ { \flat } | - k + 1 \leq | \gamma ^ { \flat } |$for$k \geq 1$. Therefore the factor of$C _ { d + 1 } ( 1 )$

$$
\left\{\left(c + T\right) ^ {\gamma^ {b}} \right\} _ {| \gamma^ {b} | - k + 1}\tag{34.8}
$$

must be a nonzero nonconstant homogeneous. Hence$C _ { d + 1 } ( 1 ) \neq 0$ Next consider the case of$d \geq | \gamma ^ { * } | = | \gamma ^ { \flat } | + \gamma _ { 1 } > | \gamma ^ { \flat } |$. We then have $d e g ( \tau ( * ) ^ { q } ) > d - | \gamma ^ { \flat } |$by Th.$. ( 3 3 . 3 ) \mathrm { \ s o \ t h a t \ } | \gamma ^ { \flat } | \geq d + 1 - d e g ( \tau ( * ) ^ { q } )$ Thus$| \gamma ^ { \flat } | \geq | \gamma ^ { \flat } | - k + 1$. Moreover$d + 1 - d e g ( \tau ( * ) ^ { q } ) = ( d - d e g ( \tau ( * ) ^ { q } ) ) +$ $1 \geq 1$. Thus$\mathrm { E q . ( 3 4 . 7 ) }$is proven. In both cases$C _ { d + 1 } ( 1 )$has a factor which is nonzero nonconstant homogeneous. We have seen by Th.(33.3) that$C _ { d + 1 } ( 1 )$is a nonzero partial sum of the power series expansion of $\left( A _ { d + 1 } - \dot { B } _ { d + 1 } - C _ { d + 1 } ( 2 ) \right) + C _ { d + 1 } ( 1 )$in$K [ [ v _ { 1 } , T , U ( 1 ) , U ( 2 ) ] ]$Hence or$\begin{array} { r } { \cdot d _ { \xi ^ { \prime } } \big ( A _ { d + 1 } - B _ { d + 1 } - C _ { d + 1 } ( 2 ) + C _ { d + 1 } ( 1 ) \big ) \leq d e g ( C _ { d + 1 } ( 1 ) ) = d + 1 } \end{array}$which proves the theorem of Moh.

Remark 34.1. We want to pay special attention to the polynomial $C _ { d + 1 } ( 1 )$called the resord-core defined by Def.$( 3 4 . 3 )$. It is nonzero homogeneous of degree$d + 1$in$\mathbb { K } [ x ^ { \prime } ]$with$x ^ { \prime } = ( v _ { 1 } , T , \dot { U } ( 1 ) , U ( 2 ) )$according to Def.(34.1) . It is a partial sum of the expansion of

$$
v _ {1} ^ {- d} h - (c + T) ^ {\gamma^ {b}} \tau^ {q} = A _ {d + 1} - B _ {d + 1} - C _ {d + 1} (2) + C _ {d + 1} (1)
$$

defined by Eq.(34.5). Recall$C _ { d + 1 } ( 1 )$of Eq.(34.3) and define

$$
\begin{array}{c} T _ {d + 1} = (v _ {1} ^ {- | \gamma |} v ^ {\gamma}) C _ {d + 1} (1) \\ = (v _ {1} ^ {- | \gamma |} v ^ {\gamma}) \Big (\tau (*) ^ {q} \big \{(c + T) ^ {\gamma^ {\flat}} \big \} _ {| \gamma^ {\flat} | - k + 1} \Big) \end{array}\tag{34.9}
$$

where it is important to note that

(1)$v _ { 1 } ^ { - | \gamma | } v ^ { \gamma }$is a unit in$R _ { \xi ^ { \prime } }$because$\xi ^ { \prime }$is metastable,

(2)$\tau ( * )$is nonzero homogeneous in$\mathbb { K } [ v _ { 1 } , T , U ( 1 ) ]$

(3)$d e g ( \tau ( * ) ^ { q } ) + ( | \gamma ^ { \flat } | - k + 1 ) = d + 1$which is resord<sub>ξ′</sub>(G′).

(4)$0 < | \gamma ^ { \flat } | - k + 1 \leq | \gamma ^ { \flat } |$

$T _ { d + 1 }$will be called the order-bounding polynomial of the transform$\mathcal { G } ^ { \prime }$ for π at the metastable point$\xi ^ { \prime }$. We sometimes write$T _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } )$for the $T _ { d + 1 }$

Remark 34.2. We start from the situation immediately after a metastable singular point$\xi ^ { \prime }$appeared according to the notation of the theorem of Moh, so that we have

$$
\operatorname{resord} _ {\xi^ {\prime}} \left(\mathcal {G} ^ {\prime}\right) = d + 1 \text {where} d = \operatorname{resord} _ {\xi} (\mathcal {G}).\tag{34.10}
$$

We refer to the regular system of parameters$x ^ { \prime } = ( v _ { 1 } , T , U ( 1 ) , U ( 2 ) )$ which are chosen according to Eq.(33.2), Eq.(33.3),Eq.(33.7), Eq.(33.8), Eq.(33.13), Eq.(33.9), Eq.(33.10), etc.

Remark 34.3. When a metastable point$\xi ^ { \prime }$is created according to Th.(34.1) we have the cases of the inequalities of$\mathrm { E q . ( 3 4 . 7 ) }$, in each of which we can choose a system of key q-parameters$T ( * )$for the transform$\mathcal { G } ^ { \prime }$at $\xi ^ { \prime } .$The$T ( * )$is extracted from$T _ { d + 1 }$of Eq.(34.9) as follows: Having always$| \gamma ^ { \flat } | \geq ( d + 1 ) - d e g \tau ( * ) ^ { p } \geq 1$, we define and examine$T ( * )$in the following two cases separately.

$$
\text { The   first   case   of } T (*) = Y (1) \text { as   follows: }\tag{34.11}
$$

This is the case of$( d + 1 ) - d e g \tau ( * ) ^ { p } = | \gamma ^ { \flat } | - k + 1 = 1$. In this case we have$d = d e g \tau ( * ) ^ { p } \equiv 0$mod$p .$. The residual factor$f$of$\mathcal { G }$have the same initial term as$v _ { 1 } ^ { d } \tau ( * ) ^ { p }$which is a p-th power. We then have

$$
i n _ {\xi^ {\prime}} (T _ {d + 1}) = i n _ {\xi^ {\prime}} \left(\tau (*) ^ {p} \{(c + T) ^ {\gamma^ {b}} \} _ {1}\right) b
$$

where$b$is the nonzero value taken by the unit$v _ { 1 } ^ { - | \gamma | } v ^ { \gamma }$at$\xi ^ { \prime }$. Hence we can choose a system$T ( * )$of key q-parameters to be the singleton:

$$
T (*) = Y (1) = \{\gamma_ {2} ^ {- 1} \sum_ {j} \gamma_ {j + 1} T _ {j} \}\tag{34.12}
$$

This parameter is indeed a generator of

$$
L _ {p - m a x} (T _ {d + 1}) = L _ {p - m a x} \left(C _ {d + 1 (1)}\right) \left(\subset L _ {p - m a x} \left(\mathbf {g} ^ {\prime}\right)\right)
$$

where$h ^ { \prime }$is a residual factor of$\mathcal { G } ^ { \prime }$at$\xi ^ { \prime }$.

(34.13)

The second case of$T ( * )$

This is the rest of the cases in which

$$
| \gamma^ {b} | \geq (d + 1) - d e g \tau (*) ^ {p} = | \gamma^ {b} | - k + 1 > 1
$$

Let$\lambda = ( d + 1 ) - d e g \tau ( * ) ^ { p }$and look for$T ( * ) = Y ( \lambda )$depending upon the number λ. For this purpose we need:

Lemma 34.2. We have$\mathbb { K } \ni c _ { j } \neq 0$for$\forall j$and we let

$$
P _ {\lambda} = \{(c + T) ^ {\gamma^ {b}} \} _ {\lambda}
$$

which is the homogeneous part of degree λ$o f \left( c + T \right) ^ { \gamma ^ { \flat } }$. We consider the case such that$| \gamma ^ { \flat } | \geq \lambda > 1$. Then there exists no proper K-submodule $L o f \sum _ { j } \mathbb { K } T _ { j }$such that$P _ { \lambda } \in \mathbb { K } [ L ]$

Thus in the second case Eq.(34.13) we can choose$T ( * ) = Y ( \lambda ) =$ $\sum _ { j } \mathbb { K } T _ { j }$to be a system of key q-parameters for$\mathcal { G } ^ { \prime }$at$\xi ^ { \prime }$.

Remark 34.4. Now for the sake of notational simplicity we drop prime from the symbols and write$\xi$for$\xi ^ { \prime } , \boldsymbol { x }$for$x ^ { \prime }$and so on. Let us then note that

$$
\begin{array}{c} \mathcal {G} = (z ^ {q \beta} h \| / ^ {p}) \text {with} v ^ {\gamma} = 1 (v = \emptyset) \\ \text {with} r e s o r d _ {\xi} (\mathcal {G}) = o r d _ {\xi} (\mathbf {g}) = d + 1 \end{array}\tag{34.14}
$$

Moreover we can choose h such that

$$
\begin{array}{c} i n _ {\xi} (\mathbf {g}) \in \mathbb {K} [ L _ {d + 1} ] \\ w i t h L _ {d + 1} = L _ {p - m a x} (\mathbf {g}) \supset T _ {d + 1} \neq 0 \end{array}\tag{34.15}
$$

in the sense of Def.(21.3) where$T _ { d + 1 }$is defined by Eq.(34.9).

Remark 34.5. We are thus in the situation in which Th.(23.4) and Cor.(23.5) are applicable to the$\mathcal { G }$of Eq.(34.14) where resor$\cdot d _ { \xi } ( \mathcal { G } ) =$ $d + 1$in this case instead of$d$of Cor.(23.5). The role of the key$q -$ parameters$\zeta$of Cor.(23.5) is played here by a nonempty system extracted from$T _ { d + 1 }$of Eq.(34.9). For instance,$\zeta = T ( * )$of Rem.(34.3). Therefore we are assured:

Theorem 34.3. In the situation of Rem.$( 3 4 . 4 )$any finite sequence of fitted permissible blowups of G does not create any more metastable points for the transforms of G within the inverse images of$\xi ^ { \prime }$, until after the residual order drops from$d + 1 \ t o \leq d$

If the residual order drops < d at any point of the transform, then we consider that our mission is accomplished by induction on d in virtue of Moh’s theorem.

## 35. q-prostable presentation

We will use the standard abc-expression of any$/ ^ { q } .$-exponent in the sense of Def.(20.1) as follows.

$$
\mathcal {G} = (\mathbf {g} \parallel / ^ {q}) = (z ^ {\mathbf {a}} g \parallel / ^ {q}) = (z ^ {q \mathbf {b}} v ^ {\mathbf {c}} g \parallel / ^ {q})\tag{35.1}
$$

with a chosen system of parameters$x = ( z , \omega ) , z = ( v , w )$. Recall that z is a system of parameters defining those components of the NC-data $\Gamma$which contain ξ and that$v \subset z$

We will then use diferent letters for g, a, b, c and g respectively to distinguish diferent$/ ^ { q } .$-exponents. In this section we will be searching for more special selection of preferable parameters which elucidate some deeper /<sup>q</sup>-cotangential structure of$\mathcal { G }$locally at a given point$\xi .$

We thus propose to introduce the notion of q-protostable presentation of a given$/ ^ { q } -$-exponent$\mathcal { G }$of$\mathrm { E q . ( 3 5 . 1 ) }$).

Consider a family of the following data given locally at the closed point$\xi \in Z$

$$
\mathfrak {F} = \{\mathcal {G}: \mathcal {G} (i), \eta (i), 1 \leq i \leq \nu + 1 \}\tag{35.2}
$$

where$\mathcal { G }$and$\mathcal { G } ( i ) , 1 \leq i \leq \nu + 1$, are$/ ^ { q } .$-exponents which are expressed in the manner of Eq.(35.1) as follows:

$$
\begin{array}{c} \mathcal {G} = (\mathbf {g} \| / ^ {q}) \\ t a k e s t h e e x p r e s s i o n E q. (3 5. 1). \end{array}\tag{35.3}
$$

And likewise the$\{ \mathcal { G } ( i ) , 1 \leq i \leq \nu + 1 \}$are expressed as follows:

$$
\begin{array}{r c l} \mathcal {G} (i) & = & (\mathbf {g} (i)   \|   / ^ {q}) = (z ^ {\mathbf {a} (i)} g (i)   \|   / ^ {q}) \\ & w i t h z ^ {\mathbf {a} (i)} & = z ^ {q \mathbf {b} (i)} v (i) ^ {\mathbf {c} (i)} \end{array}\tag{35.4}
$$

The system$\mathfrak { F }$of$\mathrm { E q . ( 3 5 . 2 ) }$will be always required to satisfy the following conditions:

(1) We are given a regular system of parameters$x = \left( z , \omega \right)$commonly for$\mathcal { G }$and for all the$\mathcal { G } ( i )$. Especially for G itself we are given$z = ( v , w )$as before.

(2) The$\eta ( i ) , 1 \leq i \leq \nu + 1$, are disjoint and together form a regular system of parameters$\eta = ( \eta ( 1 ) , \cdot \cdot \cdot , \eta ( \nu + 1 ) )$of$R _ { \xi }$2

(3) η coincides x of Eq.(35.1) for${ \mathcal { G } } .$so that z is a subsystem of$\eta .$ (From time to time we disregard the ordering of components to avoid unneccessary notaional complication.)

(4)$\eta ( i )$is a singleton for every$1 \leq i \leq \nu$but not for$i = \nu + 1$

(5)$\eta ( \nu + 1 ) = v$which could be empty but should not be disregarded.

(6) If v is not empty then it is ordered from left to right according to the history of their creation. This ordering may be at randam if no history is explicitly shown. Its significance will be recognized in later when we talk about prostable transfomation of$\mathfrak { F }$

(7) For some i, we could have$\mathcal { G } ( i ) = ( 0 \Vert / ^ { q } )$but should not be viewed as being non-existent so long as$\eta ( i )$is given.

(8) Let us recall Def.(??) for the notion of$\ast _ { - } f u l l$idempotent$q -$ diferentiation. Accordingly we let$\mathfrak { d } ( \mathfrak { i } )$denote the \*-full idempotent diferential operator in

$$
D i f f _ {\rho^ {e} (R _ {\xi}) [ \eta (i), \eta (i ^ {\triangleright}) ] / \rho^ {e} (R _ {\xi}) [ \eta (i ^ {\triangleright}) ]} ^ {*} w i t h r e s p e c t t o \eta (i)\tag{35.5}
$$

where$\eta ( i ^ { \flat } )$denotes$( \eta ( i + 1 ) , \cdot \cdot \cdot , \eta ( \nu + 1 ) )$

(a) We then require

$$
\mathfrak {d} (i) (\mathbf {g} (i)) = \mathbf {g} (i) a n d \mathfrak {d} (i) (\mathbf {g} (j)) = 0, \forall j > i.\tag{35.6}
$$

(b) Let$K ( i ) \ ( \mathrm { r e s p . } \ R ( i ) )$be the following subfield (resp. subring) of the function field$K ( Z ) = K 0$of Z (resp.$R 0 =$ $R _ { \xi } )$, defined by

$$
\begin{array}{l} K (i) = \{\phi \in K (i - 1) | \mathfrak {d} (i) (\phi) = 0 \} \\ R (i) = \{\phi \in R (i - 1) | \mathfrak {d} (i) (\phi) = 0 \} \end{array}\tag{35.7}
$$

for$1 \leq i \leq \nu + 1$

(c) so that$\mathbf { g } ( j ) \in R ( i ) \subset K ( i )$for all$j > i .$

(9) We have

$$
\mathbf {g} = \mathbf {g} (\nu + 1) + \sum_ {1 \leq i \leq \nu} \mathbf {g} (i)
$$

(10)$z ^ { \mathbf { a } }$must divide$\boldsymbol z ^ { \mathbf { a } ( i ) }$in$R _ { \xi }$for all$i$and

$$
g = \sum_ {1 \leq i \leq \nu + 1} z ^ {\mathbf {a} (i) - \mathbf {a}} g (i)\tag{35.8}
$$

(11) Finally we require

$$
\begin{array}{c} r e s o r d _ {\xi} (\mathcal {G}) = o r d _ {\xi} (g) \\ = m i n _ {1 \leq i \leq \nu + 1} \big \{o r d _ {\xi} (g (i)) + | \mathbf {a} (i) - \mathbf {a} | \big \}. \end{array}\tag{35.9}
$$

Definition 35.1. The family of data$\mathfrak { F }$of Eq.(35.2) satisfying all the conditions stated above will be called a q-prostable presentation of$\mathcal { G }$ at ξ.

Theorem 35.1. Consider any q-prostable presentation$\mathfrak { F }$of$E q . ( 3 5 . \mathcal { Q } )$ of Def.(35.1). Pick any index$i , 1 \le i \le \nu + 1$. Then we have an expression

$$
\mathbf {g} (i) \in \sum_ {0 \neq \alpha \in \epsilon^ {t (i)} (q)} \rho^ {e} (R _ {\xi}) [ \eta (i ^ {\triangleright}) ] \eta (i) ^ {\alpha}\tag{35.10}
$$

where$t ( i )$denotes the size of$\eta ( i ) ~ ( t ( i ) = 1$for all$i \leq \nu \ )$and$\epsilon ^ { t ( i ) } ( q ) =$ $\{ \alpha | 0 \leq \alpha _ { j } < q , \forall j \}$

Theorem 35.2. Under the same assumption if$i \leq \nu$(that is$i < \nu { + } 1 )$ and$o r d _ { \xi } ( \mathcal { G } ( i ) ) = o r d _ { \xi } ( \mathcal { G } )$then$\eta ( i )$is a ♯-key parameter of$\mathcal { G }$.

Remark 35.1. The last couple$( \mathcal { G } ( \nu + 1 ) , \eta ( \nu + 1 ) )$of Def.(35.1) has a special character in comparison with the other ones. It is sometimes called ♭-part of the presentation$\mathfrak { F }$of$\mathcal { G }$and denoted by$( \mathcal { G } ( \mathfrak { b } ) , \eta ( \mathfrak { d } ) )$in order to show its distinction.

Definition 35.2. Let$\zeta ~ = ~ z ~ \backslash$v so that$z ~ = ~ ( \zeta , v )$. Let us write $z ^ { \mathbf { a } ( i ) } = \zeta ^ { \beta ( i ) } v ^ { \gamma ( i ) }$in terms of${ \bf a } ( i )$of Eq.(35.4). Let$z ^ { \beta ( i ) }$mean$\zeta ^ { \beta ( i ) }$. This $z ^ { \beta ( i ) }$will be called the relative p-anafactor of$\mathcal { G } ( i ) / \mathfrak { F }$at$\xi$.

Definition 35.3. For each$\mathcal { G } ( i )$with$i ~ \le ~ \nu$of the presentation we define its$\mathsf { H } - p a r t ,$denoted by$\mathcal { G } ( \sharp i )$, which is

$$
\begin{array}{c} \mathcal {G} (\sharp i) = (\mathbf {g} (\sharp i) \| / ^ {q}) w h e r e \\ \mathbf {g} (\sharp i) = v ^ {\mathbf {c} - \gamma (i)} \mathbf {g} (i) \end{array}
$$

Here the cofactor$v ^ { \mathbf { c } }$of$\mathcal { G }$is expressed by Eq.(35.1) and$\gamma ( i )$is defined by Def.(35.2). Note that$v ^ { \mathbf { c } }$is also the cofactor of$\mathcal { G } ( \sharp i )$bacause$v ^ { - \gamma ( i ) } \mathbf { g } ( i )$ has a trivial cofactor.

Definition 35.4. We say that q-prostable presentation$\mathfrak { F }$of Def.(35.1) is ♯-exact if$\eta ( i )$is a ♯-exact parameter of$\mathcal { G } ( \sharp i )$of Def.(35.3) for every $i \le \nu$in the sense of Def.(24.1).

Theorem 35.3. If$q = p$(that is$e = 1 )$then for any given$\mathcal { G }$there exists a sharp-exact prostable p-presentation$\mathfrak { F }$of$\mathcal { G }$at any closed point $\xi ~ o f ~ S i n g ( \mathcal G )$. In fact, given any prostable$p .$-presentation

$$
\{\mathcal {G}: \mathcal {G} (i), \eta (i), 1 \leq i \leq \nu + 1 \}
$$

$\eta ( i )$is necessarily a ♯-exact parameter of the same$\mathcal { G } ( \sharp i )$for every$i \le \nu$

Definition 35.5. Given$\mathcal { G }$with the parameters${ z } = { \left( { v , w } \right) }$and a$q -$ prostable presentation$\mathfrak { F }$of$\mathcal { G }$at a closed point$\xi \in Z$in the sense of Def.(35.1), we define what we will call allowable parametric change $\eta \mapsto \eta ^ { \sim }$for$\mathfrak { F }$as follows:

(1)$\mathcal { G }$and z must remain unchanged,

(2) while$\eta ( i )$and$\mathcal { G } ( i )$are changed to$\eta ( i ) ^ { \sim }$and$\mathcal { G } ( i ) ^ { \sim }$respectively for$1 \leq i \leq \nu ,$except for$\eta ( \nu + 1 ) ^ { \sim } = \eta ( \nu + 1 ) = v$, satisfying all the requirements of Def.(35.1) in addition to the following

conditions.

$$
\eta (i) ^ {\sim} \in \rho (R _ {\xi}) [ \eta (i), \eta (i ^ {\triangleright}) ]\tag{35.11}
$$

$$
\eta (i) ^ {\sim} \equiv \eta (i) \mod \left(M _ {\xi} ^ {2} + \left(\eta (i ^ {\triangleright}) ^ {\sim}\right) R _ {\xi}\right)
$$

where we denote$\eta ( i ^ { \mathrm { p } } ) ^ { \sim } = ( \eta ( i + 1 ) ^ { \sim } , \cdots , \eta ( \nu + 1 ) ^ { \sim } )$

(3) z must stay to be a subsystem of

$$
\eta^ {\sim} = \bigl (\eta (1) ^ {\sim}, \dots , \eta (\nu + 1) ^ {\sim} \bigr).
$$

(4) The diferential operator$\mathfrak { d } ( \mathfrak { i } )$is changed into the \*-full idempotent diferential operator$\mathfrak { d } ^ { \sim } ( i )$in

(35.12) Diff ∗<sub>ρe(Rξ)[η(i)∼,η(i▷)∼]/ρe(Rξ)[η(i▷)∼]</sub> with respect to$\eta ( i ) ^ { \sim }$

(5) Accordingly${ \bf g } ( i )$and$\mathcal { G } ( i )$are changed into${ \bf g } ( i ) ^ { \sim }$and$\mathcal { G } ( i ) ^ { \sim }$by means of$\mathfrak { d } ( i ) ^ { \sim }$instead of$\mathfrak { d } ( { i } )$for$1 \leq i \leq \nu + 1$in the manner of$\mathrm { E q . ( 3 5 . 6 ) }$

Definition 35.6. An$\mathfrak { F }$of$\mathcal { G }$at$\xi$is said to be adjusted to a blowup π with smooth center D if$I = I ( D , Z ) _ { \xi }$is generated by$\eta ( i ) \cap I , 1 \leq i \leq$ $\nu + 1$, and$z \subset \eta$with reference to the notation of Def.(35.1). Here if $i \le \nu$then$\eta ( i ) \cap I$for$i \le \nu$means either the empty set when$\eta ( i ) \notin I$ or$\eta ( i )$itself when$\eta ( i ) \in I$

Theorem 35.4. If an$\mathfrak { F }$of$\mathcal { G }$at$\xi$is adjusted to a blowup$\pi$with smooth center D then or$\cdot d _ { D } ( \mathcal { G } )$is equal to the minimum of or$\cdot d _ { D } ( \mathcal { G } ( i ) )$ for$1 \leq i \leq \nu + 1$

Theorem 35.5. For a given$\mathfrak { F }$of$\mathcal { G }$in the sense of Def.(35.1), if $\pi : Z ^ { \prime } \longrightarrow Z$with center D is permissible for$\mathcal { G }$(and Γ-permissible as always) then there exists an allowable parametric change from η to$\eta ^ { \sim }$ of Def.(35.5) such that

(35.13) exactly those$\eta ( i ) ^ { \sim } \in I ( D , Z ) _ { \xi }$and$\eta ( \nu + 1 ) \widetilde { \textrm { \smallcap I } } ( D , Z ) _ { \xi }$ compose a minimal base of the ideal$I = I ( D , Z ) _ { \xi }$of$D \subset Z$at$\xi .$. Moreover we have$z \subset \eta ^ { \sim }$in accord with$D e f . ( 3 5 . 5 )$

## 36. q-prostable fronts

In this section we start with a given q-prostable presentation$\mathfrak { F }$ of$\mathcal { G }$at$\xi$in the sense of Def.(35.1) with the expressions Eq.(35.1) and$\mathrm { E q . ( 3 5 . 4 ) }$. We have the cofactor parameters$v = \eta ( \nu + 1 )$, say $\mathbf { \Psi } = \left( v _ { 1 } , \cdots , v _ { t } \right)$, of$\mathcal { G }$and the rest of the parameters$( \eta ( 1 ) , \cdots , \eta ( \nu ) )$ which consists of$w = z \setminus v$and$\omega .$.

Definition 36.1. For each i we define the relative residual factor$\mathbf f ( i )$ of$\mathcal { G } ( i ) / \mathcal { G }$, or of$\mathcal { G } ( i )$relative to$\mathcal { G }$, to be

$$
\mathbf {f} (i) = z ^ {\mathbf {a} (i) - \mathbf {a}} g (i) o f \mathcal {G} (i) = (z ^ {\mathbf {a} (i)} g (i) \| / ^ {q})\tag{36.1}
$$

with reference to$\mathcal { G } = \left( z ^ { \mathbf { a } } g \lVert / ^ { q } \right)$with$z ^ { \mathbf { a } } = z ^ { q ( b ) } v ^ { \mathbf { c } }$in the sense of the standard abc-presentations Eq.(35.4) and Eq.(35.3). Simply for the sake of comformity to those$\mathbf f ( i )$we may write

$$
\mathbf {f} = g \text {so that} \mathbf {f} = \sum_ {i} \mathbf {f} (i)\tag{36.2}
$$

in accord with Eq.(35.8).

Let us refer to Def.(35.2) for the definition of the notation of$\zeta = z \backslash v$ and$\gamma ( i )$with$z ^ { \mathbf { a } ( i ) } = \zeta ^ { \beta ( i ) } v ^ { \gamma ( i ) }$fro each$i \le \nu$. We write$z ^ { \beta ( i ) }$for$\zeta ^ { \beta ( i ) }$ which is called the relative p-anafactor of$\mathcal { G } ( i ) / \mathfrak { F }$at$\xi .$.

Definition 36.2. It should be noted that$\mathbf f ( i )$is divisible by$z ^ { \beta ( i ) }$and we let$F ( i ) = z ^ { - \beta ( i ) } ( f ) ( i )$

Let$\eta ( \sharp ) = ( \eta ( 1 ) , \cdot \cdot \cdot , \eta ( \nu ) ) = \eta \smash { \ : \backslash }$v which is a union of$w = z \mid$v and ω according to earlier notation. This$\eta ( \sharp )$is also defined by saying $x = \eta = ( \eta ( \sharp ) , v )$

Remark 36.1. With$\eta ( \sharp ) = ( \eta ( 1 ) , \cdot \cdot \cdot , \eta ( \nu ) ) = \eta \setminus \eta ( \nu + 1 )$we let$\mathfrak { d } ( \mathfrak { d } )$ denote the \*-full q-idempotent diferential operator

$$
\text { in } D i f f _ {R _ {\xi} / \rho^ {e} (R _ {\xi}) [ v ]} ^ {*} \text { with respect to } \eta (\sharp)
$$

where$R _ { \xi } = \rho ^ { e } ( R _ { \xi } ) [ v , \eta ( \sharp ) ]$. Let us note that if$i \leq \nu$we then have

$$
(v ^ {\mathbf {c}} z ^ {q \mathbf {b}}) \mathfrak {d} (b) (\mathbf {f} (i)) = \mathfrak {d} (b) (\mathbf {g} (i)) = \mathbf {g} (i)
$$

and hence$\mathfrak { d } ( \mathfrak { p } ) \mathbf { f } ( i ) = \mathbf { f } ( i )$. We also have$\mathfrak { d } ( i ) \mathbf { f } ( i ) = \mathbf { f } ( i )$with$\mathfrak { d } ( \mathfrak { i } )$of Eq.(35.5) for all$i \leq \nu + 1$

We pick any integer$\ell \geq e$where$q = p ^ { e }$. Let$r = p ^ { \ell }$

Remark 36.2. Consider the$\rho ^ { \ell } ( R _ { \xi } ) [ \eta ( \sharp ) ]$]-module, denoted by$P _ { v / \eta ( \sharp ) } ^ { \ell } ,$ which is freely generated by the p<sup>ℓ</sup>-primitive diferential operators$\delta ^ { ( \sigma / \ell ) }$

$$
i n D i f f _ {R _ {\xi} / \rho^ {\ell} (R _ {\xi}) [ \eta (\sharp) ]} w i t h r e s p e c t t o v
$$

They are$\delta ^ { ( \sigma ) }$in the sense of Def.(5.1) after Th.(5.2) where$\sigma \in \epsilon ^ { t } ( p ^ { \ell } )$

Consider the following numbers.

$$
\operatorname{ord} _ {\xi} \left(v ^ {\sigma} \delta_ {v} ^ {(\sigma / \ell)} \mathbf {f} (i)\right) = | \sigma | + \operatorname{ord} _ {\xi} \left(\delta_ {v} ^ {(\sigma / \ell)} \mathbf {f} (i)\right)\tag{36.3}
$$

which will be denoted by$b o r d _ { v } ^ { ( \sigma / \ell ) } ( \mathfrak { F } ( i ) )$for each$i \le \nu$and for every $\sigma \in \epsilon ^ { t } ( p ^ { \ell } )$. We also define the number

$$
\sharp o r d _ {v} ^ {(\sigma / \ell)} (\mathfrak {F} (i)) = o r d _ {\xi} \left(\delta_ {v} ^ {(\sigma / \ell)} \mathbf {f} (i)\right)\tag{36.4}
$$

$$
\begin{array}{c} \text {so that} \\ \mathsf {b o r d} _ {v} ^ {(\sigma / \ell)} (\mathfrak {F} (i)) = \sharp \mathsf {o r d} _ {v} ^ {(\sigma / \ell)} (\mathfrak {F} (i)) + | \sigma | \end{array}
$$

for$i \leq \nu$and$\sigma \in \epsilon ^ { t } ( p ^ { \ell } )$

There the symbol$\mathfrak { F } ( i )$should be thought of just a reference to the inclusion$\mathcal { G } ( i ) \in \mathfrak { F }$. The point is that the above numbers are not determined by$\mathcal { G } ( i )$alone.

We then define

(36.5)

$$
\mathsf {b o r d} _ {v} ^ {(\ell)} (\mathfrak {F} (i)) = \min _ {\sigma \in \epsilon^ {t} (p ^ {\ell})} \{\mathsf {b o r d} _ {v} ^ {(\sigma / \ell)} (\mathfrak {F} (i)) \}\tag{36.6}
$$

$$
\sharp o r d _ {v} ^ {(\ell)} (\mathfrak {F} (i)) = m i n _ {\sigma \in \epsilon^ {t} (p ^ {\ell})} \{\sharp o r d _ {v} ^ {(\sigma / \ell)} (\mathfrak {F} (i)) \}
$$

These numbers$\mathfrak { b o r d } _ { v } ^ { ( \ell ) } ( \mathfrak { F } ( i ) )$and$\sharp o r d _ { v } ^ { ( \ell ) } ( \mathfrak { F } ( i ) )$depend upon the choice of ℓ. However the dependence is limited in some sense. We next want to elucidate this point.

Remark 36.3. The polynomial expressions of${ \bf g } ( i )$and$\mathbf { g } ( j )$in$\rho ^ { e } ( R _ { \xi } ) [ \eta ]$ have no common nonzero monomial terms for$\nu + 1 \ge i > j \ge 1$. This is proven by the equalities Eq.(35.6) following the definition of the diferential operator$\mathfrak { d } ( \mathfrak { i } )$of Eq.(35.6). If we limit$i \leq \nu$then the same statement is also true for$\mathbf { f } \left( i \right)$and$\mathbf { f } \left( j \right)$because z and v are subsystems of η by assumption of Def.(35.1). Hence the equality$\mathbf { f } = \textstyle \sum _ { i } \mathbf { \dot { f } } ( i )$of $\mathrm { E q . ( 3 5 . 8 ) }$is a disjoint sum in the sense of nonzero monomial terms. Moreover for all$( i , \sigma )$with$i \le \nu$and with$\sigma \in \epsilon ^ { t } ( p ^ { \ell } )$, the polynomials $v ^ { \sigma } \delta _ { v } ^ { ( \sigma / \ell ) } \mathbf { f } ( i )$are mutually disjoint in the sense of nonzero monomial terms. Since the leading monomial terms of$\mathbf f ( i )$are finitely many, if$\ell \gg e$then they must be included in the leading monomial terms of $v ^ { \sigma } \delta _ { v } ^ { ( \sigma / \ell ) } \mathbf { f } ( i )$for all$\sigma \in \epsilon ^ { t } ( p ^ { \ell } )$for each$i \le \nu$. Therefore we conclude

## Lemma 36.1. We have

(36.7)$\flat o r d _ { v } ^ { ( \ell ) } ( \mathfrak { F } ( i ) ) \ = \ o r d _ { \xi } ( \mathbf { f } ( i ) )$for all$\ell \gg e$for every$i \leq \nu$ $W e$will write$\flat o r d _ { \xi } ( \mathfrak { F } ( i ) )$for this number$E q . ( 3 6 . 7 )$

Let us next examine the numbers$\sharp o r d _ { v } ^ { ( \ell ) } ( \mathfrak { F } ( i ) )$for$\ell \gg e$

Remark 36.4. Recall that$z ^ { \mathbf { a } } \mathbf { f } ( i ) = \mathbf { g } ( i )$with$z ^ { \mathbf { a } } = z ^ { q \mathbf { b } } v ^ { \mathbf { c } }$, and hence for$i \le \nu$we have$\mathfrak { d } ( i ) \mathbf { f } ( i ) = \mathbf { f } ( i )$with the opertor$\mathfrak { d } ( \mathfrak { i } )$of$\mathrm { E q . ( 3 5 . 6 ) }$ Hence the polynomial expression of$\mathbf f ( i )$$\rho ^ { \ell } ( R _ { \xi } ) [ \eta ]$does not have any nonzero monomial term belonging to$\rho ^ { \ell } ( R _ { \xi } ) [ v ]$. Therefore the same is true with the polynomial expression of$\delta _ { v } ^ { ( \sigma / \ell ) } \mathbf { f } ( i )$for every$\ell \geq e$and for every$\sigma \in \epsilon ^ { t } ( p ^ { \ell } )$, The reason is that$\delta _ { v } ^ { ( \sigma / \ell ) }$commutes with$\mathfrak { d } ( \mathfrak { i } )$. Hence we have proven

Lemma 36.2.$\sharp o r d _ { v } ^ { ( \ell ) } ( \mathfrak { F } ( i ) ) ~ > ~ 0$for every$\ell \geq e$and for every$i \le \nu$

Definition 36.3. For each$( \ell , i )$with$i \le \nu$we have a natural map

$$
s _ {i} ^ {\ell}: \sigma \in \epsilon^ {t} (p ^ {\ell}) \mapsto \delta_ {v} ^ {(\sigma / \ell)} \mathbf {f} (i) \in \rho^ {\ell} (R _ {\xi}) [ \eta (\sharp) ]
$$

This map can be extended by Z-linearity as

$$
s _ {i} ^ {\ell}: \epsilon^ {t} (p ^ {\ell}) \mathbb {Z} \to \rho^ {e} (R _ {\xi}) [ \eta (\sharp) ]
$$

with respect to the inclusion$\rho ^ { \ell } ( R _ { \xi } ) [ \eta ( \sharp ) ] \subset \rho ^ { e } ( R _ { \xi } ) [ \eta ( \sharp ) ]$because of $\ell \geq e$. We then denote by$\sharp I ^ { ( \ell ) } ( \mathfrak { F } ( i ) )$the ideal in$\rho ^ { e } ( R _ { \xi } ) [ \eta ( \sharp ) ]$generated by the image of the extended map. Namely we have

$$
\sharp I ^ {(\ell)} (\mathfrak {F} (i)) = s _ {i} ^ {\ell} \bigl (\epsilon^ {t} (p ^ {\ell}) \mathbb {Z} \bigr) \rho^ {e} (R _ {\xi}) [ \eta (\sharp) ] = \sum_ {\sigma \in \epsilon^ {t} (p ^ {\ell})} s _ {i} ^ {\ell} (\sigma) \rho^ {e} (R _ {\xi}) [ \eta (\sharp) ]\tag{36.8}
$$

Lemma 36.3. For$\textit { i } \leq \nu$the initial form$i n _ { \xi } { \left( s _ { i } ^ { \ell } ( \sigma ) \right) }$is not a$q { - } t h$ power in$g r _ { \xi } ( R _ { \xi } )$for any$\sigma ~ \in ~ \epsilon ^ { t } ( p ^ { \ell } )$unless it is zero. Moreover it contains at least one element out of$\eta ( i )$which is$\mu \sharp \ – k e y$parameter of $s _ { i } ^ { \ell } ( \sigma ) \in \rho ^ { \ell } ( R _ { \xi } ) [ \eta ( \sharp ) ]$

Lemma 36.4. Consider a pair of integers$\ell < \ell ^ { \prime }$. Then for each$\sigma \in$ $\epsilon ^ { t } ( p ^ { \ell } )$we claim to have

$$
s _ {i} ^ {\ell} (\sigma) = \sum_ {\beta \in \epsilon^ {t} (p ^ {\ell^ {\prime}} - \ell)} v ^ {p ^ {\ell} \beta} s _ {i} ^ {\ell^ {\prime}} (\sigma + p ^ {\ell} \beta)\tag{36.9}
$$

Corollary 36.5. The ideals$\sharp I _ { v } ^ { ( \ell ) } ( \mathfrak { F } ( i )$are monotone nondecreasing with respect to ℓ. Therefore for$\ell \gg e$the ideals as well as the numbers $\sharp o r d _ { v } ^ { ( \ell ) } ( \mathfrak { F } ( i ) )$become constant. Note that$\sharp o r d _ { v } ^ { ( \ell ) } ( \mathfrak { F } ( i ) ) = o r d _ { \xi } ( \sharp I _ { v } ^ { ( \ell ) } ( \mathfrak { F } ( i ) )$

Definition 36.4. Thanks to Cor.(36.5) we can now define

$$
\sharp I _ {\xi} (\mathfrak {F} (i)) = \sharp I _ {v} ^ {(\ell)} (\mathfrak {F} (i)) f o r a l l \ell \gg e\tag{36.10}
$$

By the definitions of Eq.(36.6) and Eq.(36.8) we have

$$
\operatorname{ord} _ {\xi} \left(\sharp I _ {\xi} ^ {(\ell)} (\mathfrak {F} (i))\right) = \sharp \operatorname{ord} _ {v} ^ {(\ell)} (\mathfrak {F} (i)) \text {   for   every   } \ell \geq e
$$

and therefore we obtain the following definition and equality.

$$
\sharp o r d _ {\xi} (\mathfrak {F} (i)) = \min _ {\ell \geq e} \{\sharp o r d _ {v} ^ {(\ell)} (\mathfrak {F} (i)) \} = o r d _ {\xi} (\sharp I _ {\xi} (\mathfrak {F} (i)))\tag{36.11}
$$

Definition 36.5. We define the following symbols

$$
\begin{array}{c} \sharp I _ {\xi} (\mathfrak {F}) = \sum_ {1 \leq i \leq \nu} \sharp I _ {\xi} (\mathfrak {F} (i)) \\ \sharp o r d _ {\xi} (\mathfrak {F}) = \min _ {1 \leq i \leq \nu} \sharp o r d _ {\xi} (\mathfrak {F} (i)) = o r d _ {\xi} (\sharp I _ {\xi} (\mathfrak {F})) \end{array}\tag{36.12}
$$

and after Eq.(36.7) we define

$$
\begin{array}{l} \mathsf {b o r d} _ {\xi} (\mathfrak {F}) = \min _ {1 \leq i \leq \nu} \mathsf {b o r d} _ {\xi} (\mathfrak {F} (i)) \} \\ = \min _ {1 \leq i \leq \nu} \{\mathsf {o r d} _ {\xi} \mathbf {f} (i) \} \geq \mathsf {o r d} _ {\xi} (\mathbf {f}) \end{array}\tag{36.13}
$$

It should be noted that the index$i = \nu + 1$is excluded.

Definition 36.6. Consider only the cases of$i \le \nu$. Recall the ♯-part $\mathcal { G } ( \sharp i )$of$\mathcal { G } / \mathfrak { F }$defined by Def.(35.3). Then$\mathcal { G } ( i )$is called ♯front member of$\mathfrak { F }$if we have

$$
\begin{array}{c} o r d _ {\xi} (\mathcal {G} (\sharp i)) = o r d _ {\xi} (\mathcal {G}) a n d \\ \eta (i) i s a \sharp \text {-exact parameter of} \mathcal {G} (\sharp i) \end{array}\tag{36.14}
$$

in the sense of Def.(24.1). Here it should be noted that the second condition above is automatic for the special case of$q = p$by Th.(24.2).

Definition 36.7. For$i \leq \nu , \mathcal { G } ( i )$is called ♭initial member of$\mathfrak { F }$if we have

$$
\mathsf {b o r d} _ {\xi} (\mathfrak {F} (i)) = \mathsf {b o r d} _ {\xi} (\mathfrak {F})\tag{36.15}
$$

Definition 36.8. We define the$\sharp f \eta$ront size of$\mathfrak { F }$, denoted by$\sharp ( \mathfrak { F } )$, to be the following sum:

$$
| v | + \sharp (\leq \nu)
$$

where the number$| v | = \mathbf { t } ( \mathcal { G } )$which is the number of cofactor parameters of$\mathcal { G }$and$\sharp ( \leq \nu )$denotes the number of those$\begin{array} { r } { \mathcal { G } ( i ) , i \le \nu , } \end{array}$which are ♯front members of$\mathfrak { F }$in the sense of Def.(??).

Let us next examine what we defined above from a point of view that is a step forward to become globalizable.

We introduce two kinds of diferential operators, one denoted by $\mathfrak { d } ( \mathfrak { d } )$and the other denoted by$\sharp \delta$. The first one is the \*-full idempotent diferential operator$\mathfrak { d } ( \mathfrak { d } )$

$$
\mathfrak {d} (\flat) \in D i f f _ {R _ {\xi} / \rho^ {e} (R _ {\xi}) [ v ]} ^ {*} w i t h r e s p e c t t o \eta (\sharp)\tag{36.16}
$$

where$\eta ( \sharp ) = ( \eta ( 1 ) , \cdot \cdot \cdot , \eta ( \nu ) ) = \eta \setminus v$. The second diferential operator $\sharp \delta$is actually a system of operators$\{ \sharp \delta ^ { ( \ell ) } \}$parametrized by the integers

$\ell \geq e .$, Namely we let

$$
\sharp \delta^ {(\ell)} = \sum_ {\sigma \in \epsilon^ {t} (p ^ {\ell})} \delta_ {v} ^ {(\sigma / \ell)}\tag{36.17}
$$

where$\delta _ { v } ^ { ( \sigma / \ell ) }$are the primitive diferrential operators in$D i f f _ { R _ { \xi } / \rho ^ { \ell } ( R _ { \xi } ) [ \eta ( \sharp ) ] }$ with respect to the variables v in the sense of Rem.(36.2) after Def.(5.1) and Th.(5.2).

Definition 36.9. For the q-prostable presentation$\mathfrak { F }$of Def.(35.1), let $\mathcal { F }$denote the set of those$i \le \nu$for which$\mathcal { G } ( i )$is ♯front member of$\mathfrak { F }$ in the sense of Def.(36.6). Let

$$
\mathbf {g} (\sharp) = \sum_ {i \in \mathcal {F}} \mathbf {g} (\sharp i)
$$

We then define the ideal exponent denoted by$\mathfrak { F } ( \sharp )$, locally in a neighborhood of$\xi \in Z$, as follows.

$$
\begin{array}{r c l} \mathfrak {F} (\sharp) & = & \left(\mathbf {g} (\sharp),   \sharp \mathbf {d}\right) \\ w h e r e & \sharp \mathbf {d} & = o r d _ {\xi} (\mathbf {g} (\sharp)) \end{array}\tag{36.18}
$$

Theorem 36.6.$I f \pi$with D above is permissible$f o r \mathfrak { F } ( \sharp )$then we must have$\eta ( i ) \in I ( D , Z ) _ { \xi }$for every i such that$\mathcal { G } ( i )$is ♯front of$\mathfrak { F }$at$\xi .$.

Remark 36.5. Refer to Rem.(36.1) for$\mathbf f ( i )$and f such that$\mathbf { g } = z ^ { \mathbf { a } } \mathbf { f }$ with$\begin{array} { r } { \textbf { f } = \sum _ { 1 < i < \nu + 1 } \mathbf { f } ( i ) } \end{array}$. Note that$\mathbf { f } ( \nu + 1 ) \in \rho ^ { e } ( R _ { \xi } ) [ v ]$and hence $\mathfrak { d } ( \mathfrak { p } ) ( \mathbf { f } ( \nu + 1 ) ) \overset { - } { = } 0$with$\mathfrak { d } ( \mathfrak { d } )$of$\mathrm { E q . ( 3 6 . 1 6 ) }$. It should be noted that ♯f is a partial sum of$\mathfrak { d } ( \flat ) ( \mathbf { f }$. It follows that we always have$\sharp { \bf d } > 0$by virtue of the lemma (36.2) in Rem.(36.4).

Definition 36.10. The positive integer ♯d will play an important role by itself and we write it as

$$
\begin{array}{c} \sharp \mathbf {d} (\mathfrak {F}) m e a n i n g \\ \sharp \mathbf {d} = o r d _ {\xi} (\sharp I (\mathfrak {F})) = \min _ {\ell \geq e, i \leq \nu} \sharp o r d _ {v} ^ {(\ell)} (\mathfrak {F} (i)) > 0 \end{array}\tag{36.19}
$$

in the sense of Def.(36.4) and Rem.(36.4). We also define the following number.

$$
\sharp \mathbf {r} (\mathfrak {F}) = r a n k _ {\kappa_ {\xi}} \left(\left(\sharp I + M _ {\xi} ^ {\sharp \mathrm{d} * 1}\right) / M _ {\xi} ^ {\sharp \mathrm{d} * 1}\right)\tag{36.20}
$$

where$\sharp I = \sharp I ( \mathfrak { F } )$

## 37. q-prostable transformation

We start with a given q-prostable presentation$\mathfrak { F } = \{ \mathcal { G } : \mathcal { G } ( i ) , \eta ( i ) \}$ of Def.(35.1).

Definition 37.1. A blowup$\pi : Z ^ { \prime } \longrightarrow Z$with center$D$is called prostable permissible for$\mathfrak { F }$at$\xi$if the following conditions are all satisfied:

(1)$\pi$(and D) is permissible in the sense of Def.(18.2) for the ideal exponent F(♯) defined by Eq.(36.18) of Def.(36.9),

(2)$\pi$(and D) is fitted permissible for$\mathcal { G }$in the sense of Def.(31.3). It follows that$\pi$is permissible for every one of the${ \mathcal { G } } ( i ) , 1 \leq$ $i \leq \nu + 1$, in the sense of Def.(18.2) (not necessarily fitted).

(3) It should be noted that π is permissible for the given NC-system Γ as allways.

Remark 37.1. Let us consider the situation in which we are given a$/ ^ { q _ { - } }$ exponent$\mathcal { G }$and a fitted permissible blowup$\pi : Z ^ { \prime } \to Z$with center$D$ for$\mathcal { G }$in the sense of Def.(31.3). Given any q-prostable presentation$\mathfrak { F }$of Def.(35.1), we apply a parametric adjustment to$\mathfrak { F }$in order to modify $\pi$and D to become prostable-permissible, furthermore satisfying the condition Eq.(37.1) below.

Step I : Adjusting η to the center$D$

We will make use of an allowable parametric change of$\mathfrak { F }$in the sense of Def.(35.5) in order to have the new parameters adjusted to the given center D of π in the sense of Th.(35.5). We may thus assume

$$
z \subset \eta = (\eta (1), \dots , \eta (\nu + 1)) a n d\tag{37.1}
$$

a minimal base of$I ( D , Z ) _ { \xi }$is formed by the members of

$$
\{\eta (i) \cap I (D, Z) _ {\xi} w i t h 1 \leq i \leq \nu + 1 \}
$$

Furthermore the ideal exponent$\sharp { \mathfrak { F } } = \left( \sharp I ( { \mathfrak { F } } ) , \sharp { \bf d } \right)$of Eq.(36.18) of Def.(36.9) can be kept unchanged with respect to the given the$q -$ prostable presentation${ \mathfrak { F } } .$. In fact, since D has normal clossing with the NC-data Γ, we can prove that if$\mathfrak { d } _ { v }$denotes the \*-full idempotent diferentical opperator in

$$
D i f f _ {R _ {\xi} / \rho^ {e} (R _ {\xi}) [ \eta \backslash v ]} w i t h r e s p e c t t o v
$$

then for every$\eta ( i ) \in I ( D , Z ) _ { \xi }$we have$( \mathfrak { d } _ { v } \eta ( i ) ) \in I ( D , Z ) _ { \xi }$and hence we may replace η(i) by$\eta ( i ) - \mathfrak { d } _ { v } \eta ( i )$. The claim of adjusting is obtained by modifying every$\eta ( i ) \in I ( D , Z ) _ { \xi }$in this manner.

Note that the adjustment makes the given blowup$\pi$to become$q -$ prostable-fitted permissible in the sense of Def.(37.1).

We then let

$$
\begin{array}{r l} & z _ {\dagger} (D) = z \cap I (D, Z) _ {\xi} a n d z _ {\ddagger} (D) = z \setminus z _ {\dagger} (D) \\ & \text {so that} (z) R _ {\xi} \cap I (D, Z) _ {\xi} = (z _ {\dagger} (D)) R _ {\xi} \end{array}\tag{37.2}
$$

Step II : Choose an exceptional parameter$\mathfrak { z } .$

We first define the transform$\mathcal { G } ^ { \prime }$of$\mathcal { G }$by$\pi$in the sense of Def.(18.4). The transform of$\mathfrak { F }$will be defined after some more steps, in which there will be included the definitions of$\mathcal { G } ( i ) ^ { \prime } , i = 1 , 2 , \cdots$. However $\mathcal { G } ( i ) ^ { \prime }$will be defined diferently and rarely equal to the transform of $\mathcal { G } ( i )$by$\pi$in the sense of Def.(18.4). At any rate they will be defined locally in$Z ^ { \prime }$

Remark 37.2. Pick any closed point$\xi ^ { \prime } \in \pi ^ { - 1 } ( \xi )$. We then choose and fix an exceptional parameter$\mathfrak { z }$at the point$\xi ^ { \prime } \in Z ^ { \prime }$for$\pi \ \mathrm { a s }$follows. Let $\lambda$be the last member of$\{ \eta ( 1 ) , \cdot \cdot \cdot , \eta ( \nu + 1 ) \}$which contains at least one exceptional parameter at$\xi ^ { \prime }$. Then let m be the last index such that$\lambda _ { m }$is an exceptional parameter at$\xi ^ { \prime }$. We then choose$\mathfrak { z } = \lambda _ { m }$

Remark 37.3. We can choose an abc-presentation of$\mathcal { G } ^ { \prime }$as follows:

$$
(\mathbf {g} ^ {\prime} \parallel / ^ {q}) = (z ^ {\prime \mathbf {a} ^ {\prime}} g ^ {\prime} \parallel / ^ {q}) = (z ^ {\prime q \mathbf {b} ^ {\prime}} v ^ {\prime \mathbf {c} ^ {\prime}} g ^ {\prime} \parallel / ^ {q})\tag{37.3}
$$

in such a way that$z ^ { \prime }$consists of the following

$$
z (i) _ {\ddagger}, \text {   for   all   } i \leq \nu + 1,\tag{37.4}
$$

those z$^ { - 1 } z ( i ) _ { \dag j } \in M _ { \xi ^ { \prime } } , ~ f o r ~ e v e r y ~ i \le \nu + 1 ,$

$$
a n d \mathfrak {z}
$$

while$v ^ { \prime }$consists of

$$
\begin{array}{c} \big (z (i) _ {\ddagger} \cap v \big), f o r a l l i \leq \nu + 1, \\ t h o s e \mathfrak {z} ^ {- 1} \big (z (i) _ {\dagger j} \in v \big) \in M _ {\xi^ {\prime}}, f o r e v e r y i \leq \nu + 1, \\ a n d “ m a y b e ” a l s o \mathfrak {z} \end{array}\tag{37.5}
$$

where$\mathfrak { z } \in v ^ { \prime }$if and only if$q$does not divide the order of$\mathcal { G } ^ { \prime }$at the generic point of the exceptional divisor of$\pi .$. (See Th.(19.1).) Incidentally this order is equal to$o r d _ { D } ( G )$

Step III : Intermediary parameters$\eta ^ { \circ }$

We next go on to introduce intermediary parameters$\eta ^ { \circ }$before we obtain the ultimate transforms$\eta ^ { \prime }$of the parameters$\eta$. Recall we have chosen the paramertric decompositions$\eta ( i ) = ( \eta ( i ) _ { \dagger } , \eta ( i ) _ { \ddag } )$in the manner of Def.(37.1). Let us then write

$$
\eta (i) _ {\dagger} = (\eta (i) _ {\dagger , 1}, \dots , \eta (i) _ {\dagger , t (i)}), 1 \leq i \leq \nu + 1.
$$

We firstly introduce the following symbols:

$$
\begin{array}{l} \zeta (i j) = \mathfrak {z} ^ {- 1} \eta (i) _ {\dagger , j} - \varpi (i j) w i t h \varpi (i j) \in \mathbb {K} \\ \text { such   that } \zeta (i j) \in M _ {\xi^ {\prime}} f o r a l l (i j). \end{array}\tag{37.6}
$$

where the index$( i j )$cocorresponding to$\mathfrak { z } ^ { - 1 } \mathfrak { z } = 1$should be dropped out of the list if such$( i j )$should exist. With the range of j for each i understood as above, we define

$$
\begin{array}{r c l} \eta^ {\circ} (i) & = & \big (\eta^ {\circ} (i -), \eta^ {\circ} (i +) \big) \\ & & w h e r e \end{array}\tag{37.7}
$$

$$
\eta^ {\circ} (i -) = \eta (i) _ {\ddagger} a n d \eta^ {\circ} (i +) = (\zeta (i j), f o r a l l j) 1 \leq i \leq \nu
$$

In order to define$\eta ^ { \circ } ( i )$for$i > \nu$we recall v of$\mathcal { G }$expressed as Eq.(35.1) and define the partitions of v as follows:

$$
\begin{array}{r c l} v & = & (v _ {\dagger}, v _ {\ddagger}) \text {with} v _ {\dagger} = v \cap I (D, Z) _ {\xi} \\ & & v _ {\dagger} = (v _ {\dagger , 1}, \dots , v _ {\dagger , t (\flat)}) \end{array}\tag{37.8}
$$

Here we should recall the assumption that π with$D$is Γ-permissible and hence$z \cup v _ { \ddagger }$is extendable to a regular system of parameters of$R _ { \xi }$ and so is$v _ { \ddagger }$to the same of$R _ { \xi } / I ( D , Z ) _ { \xi }$

Next define the following symbols.

$$
\begin{array}{c} \tau (j) = \mathfrak {z} ^ {- 1} v _ {\dagger , j} - \varkappa (j) w i t h \varkappa (j) \in \mathbb {K} \\ s u c h t h a t \tau (j) \in M _ {\xi^ {\prime}} f o r a l l (j), \end{array}
$$

$$
a n d t h e n d e f i n e T (b) = \{j \in [ 1, t (b) ] | \varkappa (j) \neq 0 \}
$$

Note that$\tau ( j ) \notin v ^ { \prime }$if and only if$j ~ \in ~ T ( \flat )$with reference to$v ^ { \prime }$of Eq.(37.5) for$\mathcal { G } ^ { \prime }$of Rem.(37.3). With the indices j understood as above we define$\eta ^ { \circ } ( i ) , i \geq \nu + 1$, as follows.

$$
\eta^ {\circ} (\nu + 1) = (\tau (j) \text {   for   all   } j \in T (\flat))\tag{37.9}
$$

and then

$$
\eta^ {\circ} (\nu + 2) = \left\{ \begin{array}{l l} (\mathfrak {z}) & \text { if } \mathfrak {z} \not \in v ^ {\prime} \\ \emptyset & \text { if } \mathfrak {z} \in v ^ {\prime} \end{array} \right.\tag{37.10}
$$

Recall that always$\mathfrak { z } \in z ^ { \prime }$by Eq.(37.4). We now define the last member of$\eta ^ { \circ }$simply by letting

$$
\eta^ {\circ} (\nu + 3) = v ^ {\prime}.\tag{37.11}
$$

We have a chain of inclusion as follows:

$$
v ^ {\prime} \subset z ^ {\prime} \subset \eta^ {\circ} = (\eta^ {\circ} (1), \dots , \eta^ {\circ} (\nu + 3))\tag{37.12}
$$

in which it will turn out to be very important that if$i \leq \nu$then$\eta ^ { \circ } ( i )$is divided into two parts, firstly$\eta ^ { \circ } ( i - )$and then$\eta ^ { \circ } ( i + )$, in accord with the definition of$\mathrm { E q . ( 3 7 . 7 ) }$. It should be noted that if$\eta ^ { \circ } ( \nu + 3 )$is empty then$\eta ^ { \circ } ( \nu + 2 )$is not and also that$\eta ^ { \circ }$is a regular system of parameters of$Z ^ { \prime }$at$\xi ^ { \prime }$.

Step IV : Diferentiations$\partial ^ { \circ }$

Recall that the system η is divided into an ordered set of subsystems as follows:

$$
\begin{array}{c} \eta^ {\circ} (1 -), \eta^ {\circ} (1 +), \eta^ {\circ} (2 -), \eta^ {\circ} (2 +), \dots , \\ \eta^ {\circ} (\nu -), \eta^ {\circ} (\nu +), \eta^ {\circ} (\nu + 1), \eta^ {\circ} (\nu + 2), \eta^ {\circ} (\nu + 3) \end{array}\tag{37.13}
$$

Just for the sake of notational simplicity, let us rewrite the same with new names as

$$
\begin{array}{c} \theta (1), \theta (2), \theta (3), \theta (4), \dots , \\ \theta (\mu - 1), \theta (\mu), \theta (\mu + 1), \theta (\mu + 2), \theta (\mu + 3) \end{array}\tag{37.14}
$$

After this change of notation we then define the following \*-full idempotent operators for all$j \le \mu + 3$

$$
\partial^ {\theta} (j) \text { in } \mathfrak {d} _ {\rho^ {e} (R _ {\xi}) [ \theta (j), \theta (j ^ {\triangleright}) ] / \rho^ {e} (R _ {\xi}) [ \theta (j ^ {\triangleright}) ]} \text { with   respect   to } \theta (j)\tag{37.15}
$$

in the manner of Eq.(35.5) with

$$
\theta (j ^ {\triangleright}) = \Bigl (\theta (j + 1), \dots , \theta (\mu + 3) \Bigr).\tag{37.16}
$$

Here$\theta ( j )$may be empty for some i and if it is so then we let$\partial ^ { \theta } ( j ) = 0$ Let us express the correspondence from θ-indices to η◦-indices by a map written as$j \mapsto I ( j )$where$I ( j )$is either$( i - )$or$( i + )$depending upon$j$where$j < \mu + 1$. Accordingly each${ \mathfrak { z } } ^ { - q } \mathbf { g } ( i )$is split into a sum of the form$f ( j ) + f ( j + 1 )$for each$i \leq \nu$as follows:

$$
\mathfrak {z} ^ {- q} \mathbf {g} (i) = f (j) + f (j + 1) w h e r e\tag{37.17}
$$

$$
I (j) = i - a n d f (j) = \partial^ {\theta} (j) \left(\mathfrak {z} ^ {- q} \mathbf {g} (i)\right)
$$

$$
I (j + 1) = i + \text {   and   } f (j + 1) = \mathfrak {z} ^ {- q} \mathbf {g} (i) - f (j)
$$

and we let$f ( \mu + 1 ) = { \mathfrak { z } } ^ { - q } \mathbf { g } ( \nu + 1 )$

Moreover for$i \geq \nu + 1$and$j \geq \mu + 1$we let

$$
f (\mu + k) = g (\nu + k) \text { where } k = 1, 2, 3.\tag{37.18}
$$

We define$\mathbf { g } ^ { \theta } ( j ) , 1 \leq j \leq \mu + 3$, by induction on$j$as follows.

$$
\mathbf {g} ^ {\theta} (1) = \partial^ {\theta} (1) f (1) = f (1), a n d f o r j > 1\tag{37.19}
$$

$$
\mathbf {g} ^ {\theta} (j) = \partial^ {\theta} (j) \Big (f (j) + \sum_ {1 \leq k <   j} \big (\prod_ {k \leq a <   j} \left(i d - \partial^ {\theta} (a)\right) \big) f (k) \Big),
$$

for$j \leq \mu$, while for$j \geq \mu + 1$we let

$$
F = f (\mu + 1) + \sum_ {1 \leq k <   \mu + 1} \left(\prod_ {k \leq a <   \mu + 1} (i d - \partial^ {\theta} (a)) f (k)\right)\tag{37.20}
$$

and define

$$
\begin{array}{r} \mathbf {g} ^ {\theta} (\mu + 1) = \partial^ {\theta} (\mu + 1) F \\ \mathbf {g} ^ {\theta} (\mu + 2) = \partial^ {\theta} (\mu + 2) \big (\mathbf {F} - \mathbf {g} ^ {\theta} (\mu + 1) \big) \\ \mathbf {g} ^ {\theta} (\nu + 3) = \partial^ {\theta} (\mu + 3) (\mathbf {F} - \mathbf {g} ^ {\theta} (\mu + 1) - \mathbf {g} ^ {\theta} (\mu + 2)). \end{array}\tag{37.21}
$$

Note that we may assume that

$$
\mathbf {g} ^ {\prime} = \sum_ {1 \leq i \leq \mu + 3} \mathbf {g} ^ {\theta} (i)\tag{37.22}
$$

where$\mathbf { g } ^ { \prime }$of$\mathcal { G } ^ { \prime }$is defined by Rem.(37.3) and it is only up to equivalence of Eq.(16.1). The equality$\mathrm { E q . ( 3 7 . 2 2 ) }$may be assumed because$\eta ^ { \theta }$is a regular system of parameters of$R _ { \xi ^ { \prime } }$and$K e r ( \cap _ { a l l j } \partial ^ { \theta } ( j ) ) = \rho ^ { e } ( R _ { \xi } )$

Step V : Express$\mathcal G ^ { \boldsymbol { \theta } } ( \boldsymbol { j } )$for all$j .$.

Let$\Gamma ^ { \prime }$be the transform of$\Gamma$by π and choose the system of$\Gamma ^ { \prime } { } _ { - }$ parameters$z ^ { \prime }$of Eq.$. ( 3 7 . 4 )$at$\xi ^ { \prime } \in Z ^ { \prime }$. We can then write abc-expressions of the$/ ^ { q } .$-exponents$\mathcal G ^ { \boldsymbol { \theta } } ( \boldsymbol { j } )$as follows:

$$
\begin{array}{r l} \mathcal {G} ^ {\theta} (j) & = (\mathbf {g} ^ {\theta} (j) \| / ^ {q}), 1 \leq j \leq \mu + 3, \text {   with } \\ \mathbf {g} ^ {\theta} (j) & = z ^ {\prime q \mathbf {b} ^ {\theta} (j)} v ^ {\theta} (j) ^ {\mathbf {c} ^ {\theta} (j)} g ^ {\theta} (j). \end{array}\tag{37.23}
$$

where$v ^ { \theta } ( j ) \subset z ^ { \prime } , \ \mathbf { b } ^ { \theta } ( j )$and$\mathbf { c } ^ { \theta } ( j )$are uniquely determined by the chosen$z ^ { \prime }$and$\mathbf { g } ^ { \theta } ( j )$. This is so by virtue of Def.(19.1) and Def.(19.3) following Th.(19.1).

Finaly we take the essential subsequence of

$$
\mathfrak {F} ^ {\theta} = \{\mathcal {G} ^ {\prime}: (\mathcal {G} ^ {\theta} (j), \eta^ {\theta} (j)), 1 \leq j \leq \mu + 3 \}.\tag{37.24}
$$

This simply means deleting those pairs having$\eta ^ { \theta } ( j ) = \varnothing$for$j < \mu + 3$ Note that we keep the last pair even if$\eta ^ { \theta } ( \mu + 3 ) ( = v ^ { \prime } )$happens to be empty. By doing this we lose nothing essential out Eq.(37.24). The resulting sequence will be denoted by

$$
\mathfrak {F} ^ {\prime} = \{\mathcal {G} ^ {\prime}: (\mathcal {G} ^ {\prime} (i), \eta^ {\prime} (i)), 1 \leq i \leq \nu^ {\prime} + 1 \}.\tag{37.25}
$$

Definition 37.2. We see that${ \mathfrak { F } } ^ { \prime }$of$\mathrm { E q . ( 3 7 . 2 5 ) }$is a q-prostable presentation of$\mathcal { G } ^ { \prime }$at$\xi ^ { \prime } \in Z ^ { \prime }$. We will call it the$q \cdot$-prostable transform (or simply transform) of the given$q \mathrm { . }$-prostable presentation$\mathfrak { F }$of$\mathcal { G }$at$\xi$by the blowup$\pi$. It should be noted that$\mathcal { G } ^ { \prime } ( i )$may not be the transform of$\mathcal { G } ( i )$for any i while$\mathcal { G } ^ { \prime }$is the transform of$\mathcal { G }$

## 38. p-prostable cases

Throughout this section we are primarily interested in the fitted permissible transforms of a /<sup>p</sup>-exponent, i.e,$q = p$and$e = 1 \cdot$

$$
\mathcal {G} = (\mathbf {g} \| / ^ {p}) w i t h \mathbf {g} = z ^ {\mathbf {a}} g = z ^ {p \mathbf {b}} v ^ {\mathbf {c}} g\tag{38.1}
$$

locally expressed at a given closed point$\xi \in S i n g ( \mathcal { G } ) \subset Z$in the manner of Eq.(20.1) of Def.(20.1). We also choose and fix a p-prostable pre-sentation of$\mathcal { G }$which will be assumed ♯-exact in the sense of Def.(35.4) with reference to Th.(35.3). The$\mathcal { G }$will be expressed as

$$
\mathfrak {F} = \{\mathcal {G}; \mathcal {G} (i), \eta (i), 1 \leq i \leq \nu + 1 \}\tag{38.2}
$$

locally at$\xi$in the manner of Def.(35.1), of which

$$
\mathcal {G} (i) = (\mathbf {g} (i) \| / ^ {p}) \text {   with   } \mathbf {g} (i) = z ^ {\mathbf {a} (i)} g (i) = z ^ {q \mathbf {b} (i)} v (i) ^ {\mathbf {c} (i)} g (i)
$$

in the manner of Eq.(35.4).

Consider a blowup π :$Z ^ { \prime } \longrightarrow Z$with center$D \ni \xi$which is prostablefitted permissible for$\mathfrak { F }$at$\xi .$We then examine the transforms$\mathcal { G } ^ { \prime }$of $\mathcal { G }$and${ \mathfrak { F } } ^ { \prime }$of$\mathfrak { F }$by$\pi$locally defined at any chosen closed point$\xi ^ { \prime } \in$ $\pi ^ { - 1 } ( \xi ) \cap S i n g ( \mathcal { G } ^ { \prime } )$. We write

$$
\mathfrak {F} ^ {\prime} = \{\mathcal {G} ^ {\prime}; (\mathcal {G} ^ {\prime} (i), \eta^ {\prime} (i)), 1 \leq i \leq \nu^ {\prime} \}\tag{38.3}
$$

locally at$\xi ^ { \prime }$in the manner of Eq.(37.25) of Def.(37.2), where

$$
\mathcal {G} ^ {\prime} = \left(\mathbf {g} ^ {\prime} \right\| / ^ {p}) w i t h \mathbf {g} ^ {\prime} = z ^ {\prime \mathbf {a} ^ {\prime}} g ^ {\prime} = z ^ {\prime q \mathbf {b} ^ {\prime}} v ^ {\prime \mathbf {c} ^ {\prime}} g ^ {\prime}\tag{38.4}
$$

$$
a n d \mathcal {G} ^ {\prime} (i) = (\mathbf {g} ^ {\prime} (i) \| / ^ {p})
$$

$$
w i t h \mathbf {g} ^ {\prime} (i) = z ^ {\prime \mathbf {a} ^ {\prime} (i)} g ^ {\prime} (i) = z ^ {\prime q \mathbf {b} ^ {\prime} (i)} v ^ {\prime} (i) ^ {\mathbf {c} ^ {\prime} (i)} g ^ {\prime} (i).
$$

Remark 38.1. We have the following cases:

(1) Case I: We have resor$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) > r e s o r d _ { \xi } ( \mathcal { G } )$

(2) Case II: We have resor$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = r e s o r d _ { \xi } ( \mathcal { G } )$

(3) Case III: We have resor$\cdot d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = r e s o r d _ { \xi } ( \mathcal { G } ) - 1$

(4) Case IV: We have$r e s o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) < r e s o r d _ { \xi } ( \mathcal { G } ) - 1$

If Case I happens then by Moh’s Th.(34.1) we must have$r e s o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) =$ $r e s o r d _ { \xi } ( \mathcal { G } ) + 1$and$v ^ { \prime }$of Eq.(38.4) must be empty by Prop.(33.1). It should also be kept in mind that if Case IV happens then our inductive strategy is considered successful by Moh’s theorem and by the Prop.(38.2) proven below. The undesired phenomena are any indefinite sequences of alternately repeated Case I coupled with Case III possibly having some additions of Case II inserted between such couples.

Remark 38.2. Recall the exceptional parameter z which is selected in the manner of Rem.(37.2). Here the point is that the index i with $\mathfrak { z } \in \eta ( i )$is uniquely determined by the choice of the presentation$\mathfrak { F }$of the given$\mathcal { G }$. Viewing z as an element of$R _ { \xi }$as well as that of$R _ { \xi } ^ { \prime }$we consider the following cases:

(1) Case$A \colon { \mathfrak { z } } \in v$. Equivalently$\mathfrak { z } \in \eta ( \nu + 1 )$

(2) Case$B \colon { \mathfrak { z } } \notin v$. Equivalently$\mathfrak { z } \in \eta ( i )$with some$i \leq \nu .$

(3) Case$A ^ { \prime } \colon \mathfrak { z } \in v ^ { \prime }$. Equivalently$o r d _ { \xi } ( \mathcal { G } ) \not \equiv 0$mod$p .$

(4) Case$B ^ { \prime } \colon \mathfrak { z } \notin v ^ { \prime }$. Equivalently$o r d _ { \xi } ( \mathcal { G } ) \equiv 0$mod$p .$

Proposition 38.1. If there exists$i < \nu + 1$such that or${ \mathit { l } } _ { \xi } ( \mathcal { G } ( i ) ) =$ ord<sub>ξ</sub>(G) then η(i) must contain at least one ♯-key parameter$\zeta \ o f \mathcal G \ a t$ $\xi .$. It follows that the Case I cannot happen for any fitted permissible transform of G at any closed point$\xi ^ { \prime } \in \pi ^ { - 1 } ( \xi ) \cap S i n g ( \mathcal { G } ^ { \prime } )$. Moreover the transform$\zeta ^ { \prime } = 3 ^ { - 1 } \zeta$of the given parameter$\zeta$is a ♯-key parameter of$\mathcal { G } ^ { \prime }$at$\xi ^ { \prime }$unless we have Case III or Case IV.

Proposition 38.2. Assume that v is empty. Then there exists$i < \nu { + } 1$ having the same property of Prop.(38.1) so that we have only Case II unless Case III or Case IV happens after any fitted permissible blowup for G.

Proposition 38.3. Consider a fitted permissible blowup$\pi : Z ^ { \prime } \to Z$ for G with center D and a closed point$\xi ^ { \prime } \in \pi { - } 1 ( \xi ) \cap S i n g \mathcal { G } ^ { \prime }$with the transform$\mathcal { G } ^ { \prime }$of G. Assume that the chosen exceptional parameter z for$\mathfrak { F } / \mathcal { G }$is ♯-key parameter for$\mathcal { G }$. Then either Case IV or Case III in which the residual factor f′ of the transform G′ contains a key parameter transveral to the exceptional divisor of$\pi$in$Z ^ { \prime }$

Remark 38.3. Note that the assumption of Prop.(38.2) is satisfies at any metastable point whence v is empty. Then Prop.(38.1) becomes applicable. Therefore thanks to Moh’s Th.(34.1) and Prop.(38.1), we see that after Case I have occured our next inductive objective will be accomplished if the residual order can be made to drop two or more (either once Case IV or twice Case III before the next Case I).

After Case I we may have Case II repeated and then possibly Case III followed by Case II repeated again. After such successions we may have Case I again. Such a cycle of Cases I-II-III-II-I may be repeated. Therefore our task is to show such cycles cannot repeat indefinitely in order to make a successsful step forward according to our inductive strategy. Thus our immediate interest is to clarify what are possible (or rather impossible) courses of Cases after a Case I had occured.

Keeping in mind this Rem.(38.3), we start with a situation that is immediately after Case I took place for a$/ ^ { p _ { . } }$-exponent furnished with a /<sup>p</sup>-presentation locally at a given closed point. In this sense we choose our inital assumption and the notation of$\mathcal { G }$furnished with${ \mathfrak { F } } .$, which are the ones arising in the special situation above. Their detailed expression follow Eq.(35.2), Eq.(35.3) and Eq.(35.4).

Remark 38.4. Let us introduce the following number and keep it as an important reference for comparison with corresponding numbers of subsequent transforms.

$$
\mathbf {d} = \mathbf {d} (\mathcal {G}) = \left( \begin{array}{c c} r e s o r d _ {\xi} (\mathcal {G}) & a t t h e s t a r t i n g p o i n t \end{array} \right).\tag{38.5}
$$

We will be applying a fitted permissible blowup successively one after another. However for the sake of simplicity we may choose a notational change back at the each of later steps during such a sequence of successive transformations. In any event such a notational reset should be understood only for the purpose of clarifying essential efects taking place at a particular step. However one thing we must keep in mind is that the number called d is the one chosen and fixed at the very stating point of Eq.(38.5) and the meaning the symbol will not be changed later.

Remark 38.5. Quite generally we will be working with a fitted permissible blowup denoted by

$$
\pi : Z ^ {\prime} \to Z \text {with center} D \ni \xi
$$

for$\mathcal { G }$. We then write$\mathcal { G } ^ { \prime }$for the transform of$\mathcal { G }$and pick a closed point $\xi ^ { \prime } \in \pi ^ { - 1 } ( \xi ) \cap S i n g ( \mathcal { G } ^ { \prime } )$at which we want to examine the efect of$\pi .$ We also write the transform${ \mathfrak { F } } ^ { \prime }$of$\mathfrak { F }$by$\pi$in the sense of Def.(37.2). We will also use the following symbol.

$$
\mathbf {d} ^ {\prime} = \mathbf {d} (\mathcal {G} ^ {\prime}) = \left(r e s o r d _ {\xi^ {\prime}} (\mathcal {G} ^ {\prime})\right)\tag{38.6}
$$

Remark 38.6. We have defined numbers$\flat ( d )$and$\sharp ( d )$of$\mathcal { G }$by Eq.(36.12) and Eq.(36.13). We will then write$b ( d ) ^ { \prime }$and$\sharp ( d ) ^ { \prime }$for the corresponding numbers of the transform$\mathcal { G } ^ { \prime }$, and we also write other kind of numbers in a similar way. We often talk about a sequence of permissible blowups which will be expressed as$\varpi : \tilde { Z } \to Z$. We will then write$\tilde { \mathbf { d } } , \tilde { \mathcal { G } } , \tilde { v } , \tilde { \tilde { s } }$ $\sharp ( \tilde { d } ) , \flat ( \tilde { d } )$and so on for the final transforms by$\varpi$

We now go on into results which requires somewhat delicately casedependent reasonings.

Remark 38.7. We first divide cases in terms of the$r e s o r d _ { \xi } ( \mathcal { G } )$as follows. First is the case in which resor$d _ { \xi } ( \mathcal { G } ) \equiv 0$mod$p .$

Second is the remaining case in which$r e s o r d _ { \xi } ( \mathcal { G } ) \not \equiv 0$mod$p .$.

## 39. If residual orders ≡ 0 mod$p$

Let us forcus our attention to the first case of Rem.(38.7):

$$
r e s o r d _ {\xi} (\mathcal {G}) \equiv 0 \mod p
$$

Remark 39.1. Assuming this, we have the following three cases in each of which we want to examine the transform$\mathcal { G } ^ { \prime }$of$\mathcal { G }$at a closed point $\xi ^ { \prime } \in S i n g ( \mathcal { G } ^ { \prime } ) \cap \pi ^ { - 1 } ( \xi )$

Case(a): There exists$i \le \nu$such that

$$
o r d _ {\xi} (\mathbf {f} (i)) = o r d _ {\xi} (\mathbf {f}) = r e s o r d _ {\xi} (\mathcal {G}) = \mathbf {d}
$$

with the relative residual$\mathbf { f } ( j ) , 1 \le j \le \nu + 1$, of Def.(36.1). This is the case of Prop.(38.1) after Prop.(38.2) in which Case I cannot happen, while Cases II, III, IV, can occur at$\xi ^ { \prime }$. In Case II,$\mathcal { G } ^ { \prime }$is in$\mathrm { C a s e ( a ) }$ again at$\xi ^ { \prime } .$. In Case III for the first time (possibly after having Case II repreated) we are still having Prop.(38.2) valid and Case I cannot follow. In principle it is possible to have Case(a)-Case II-Case(a) repeat indefinitely. This problem will be resolved by the setup of our global inductive strategy which will presented in later sections.

Case(b): For all$i \leq \nu$we have

$$
o r d _ {\xi} (\mathbf {f} (i)) <   o r d _ {\xi} (\mathbf {f} (\nu + 1)) = r e s o r d _ {\xi} (\mathcal {G}) = \mathbf {d}
$$

while the chosen exceptional parameter z of Rem.(37.2) belongs to$\eta ( i )$ with$i \leq \nu .$

By the definition of$\mathfrak { F }$the relative residual$\mathbf f (  { \boldsymbol \nu } + 1 )$always belongs to $\rho ( R _ { \xi } ) [ v ]$. Then by the assumption on z, we must have$\mathfrak { z } ^ { - 1 } v _ { j } \in M _ { \xi ^ { \prime } }$for at least one component$v _ { j }$of v and hence Case I cannot happen. Unless Case III or Case IV happens the transform$\mathcal { G } ^ { \prime }$keeps the same order and it stays in the first case of Rem.(38.7), either Case(a) or Case(b). If Case III happens for the first time the transform$\tilde { \mathcal { G } }$will have empty cofactor ˜v because$\mathbf { d } \equiv 0$mod$p .$We thus end up in Prop.(38.2) with $\tilde { \mathbf { d } } = \mathbf { d } - 1$which is a happy ending case by our global inductive strategy, too. However here in principle we can have the cycle Case(b)-Case II-Case(b) repeated indefinitely. This problem will be again solved by our global inductive strategy which will be shown later.

Case(c): For all$i \le \nu$we hace

$$
\operatorname{ord} _ {\xi} (\mathbf {f} (i)) <   \operatorname{ord} _ {\xi} (\mathbf {f} (\nu + 1)) = \mathbf {d} \text {while} \mathfrak {z} \in \eta (\nu + 1) = v
$$

Again Case I cannot happen until after Cases III or IV had happened because the cofactor remains empty. Even if Case III happened for the first time possiibly after repeated Case II we still have the case of empty cofactor at the step immediately after. There Prop.(38.2) and Prop.(38.1) by the same reasonings as Case (b). Thus the first case of Rem.(38.7) is the problem of the type which can be taken care of by our global inductive strategy shown later.

## 40. If residual orders$\not \equiv 0$mod$p$

Let us next examine the second case of Rem.(38.7) which assume:

$$
r e s o r d _ {\xi} (\mathcal {G}) \not \equiv 0 \mod p
$$

Remark 40.1. In this case, too, we start with empty cofactor v and hence a nonempty system of ♯-key parameters for${ \mathcal { G } } .$. Then Case I cannot happen so long as only Case II continues to occur. In fact, by Th.(23.4), the transforms of those ♯-key parameters remain to be ♯-key as long as the residual order is kept unchanged although the new cofactors will not be empty. Therefore the next change of the residual order must be either Case III or Case IV. Since Case IV means that our inductive task is accomplished by virtue of Moh’s theorem Th.(34.1), we will pay special attention to Case III occuring for the first time or more generally at a similar situation after having repeated residually up one and then down one to the original number d of Eq.(38.5).

Proposition 40.1. We start with the situation in which resor$d _ { \xi } ( \mathcal G )$ is d$\not \equiv \ 0$mod$( p )$and G possesses at least two independent ♯-key parameters, say z and$\zeta .$Moreover assume that z happen to be the chosen exceptional parameter with respect to the the closed point$\xi ^ { \prime }$in $\pi ^ { - 1 } ( \xi ) \cap \bar { \sin { g } ( \mathcal { G } ^ { \prime } ) }$where$\pi : Z ^ { \prime } \to Z$is a fitted permissible blowup for G. We then claim that the transform$\mathcal { G } ^ { \prime }$of G by π at$\xi ^ { \prime }$will have either one of the following:

(1) resord<sub>ξ</sub>$\mathbf { \nabla } \cdot ( \mathcal { G } ^ { \prime } ) < \mathbf { d } - 1$, that is Case IV and we are done.

(2) reso$\mathbf { \nabla } \cdot d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = \mathbf { d } - 1$and g of the abc-express$E q . ( 3 5 . 1 ) ~ f o r ~ \mathcal { G }$

at$\xi$can be written in the form$g \ = \ h 0 + \mathfrak { z } h ( 1 )$where

(a) letting$h 0 ^ { \prime } = \mathfrak { z } ^ { - \mathbf { d } } h 0$and$h ( 1 ) ^ { \prime } = \mathfrak { z } ^ { - \mathbf { d } + 1 } h ( 1 )$we have both h0′ and$h ( 1 ) ^ { \prime }$contained in$R ^ { \prime } = R _ { \xi ^ { \prime } }$2

(b)$\mathbf { d } - 1 \ = \ o r d _ { \xi } ( h ( 1 ) ) = o r d _ { \xi ^ { \prime } } ( h ( 1 ) ^ { \prime } )$and$o r d _ { \xi ^ { \prime } } ( h 0 ^ { \prime } ) \ge { \bf d - 1 }$

(c) letting d be the \*-full idempotent diferential operator in

$D i f f _ { R ^ { \prime } / \rho ( R ^ { \prime } ) [ \eta \backslash \{ \lambda \} ] }$with respect to z

we have$\mathfrak { d } ( h 0 ^ { \prime } ) = h 0 ^ { \prime }$and$\mathfrak { d } ( h ( 1 ) ^ { \prime } ) = 0$

Here$\eta = ( \eta ( 1 ) , \cdot \cdot \cdot , \eta ( \nu + 1 ) )$is the system of parameters$o f$a chosen$\mathfrak { F }$which is adapted to the center D and contains both z and$\zeta$.

Proposition 40.2. Assume that resor$d _ { \xi } ( \mathcal G )$is d$\not \equiv 0$mod$( p )$and$\mathcal { G }$ possesses one and only one ♯-key. If the chosen exceptional parameter is the ♯-key, then we have only Case III or Case IV. In the case of Case III we have one of the following two:

(1) the transform${ \mathcal { G } } ^ { \prime } o f { \mathcal { G } }$is prone to generic down type (depennding upon whether z vanishes on the next center or not) at$\xi ^ { \prime }$in which case we must have d$- 1 \equiv 0$mod$( p )$

(2) the transform$\mathcal { G } ^ { \prime }$has at least one$\sharp - k e y$parameter at$\xi ^ { \prime }$.

Remark 40.2. For the sake of notational simplicity we reset our symbols to those of$\mathcal { G } / \mathfrak { F }$at the step immediately before Case III happened for the first time. We also reset the other related symbols accordingly. We write the next blowup as$\pi : Z ^ { \prime } \to Z$with center$D$and then the transforma$\mathcal { G } ^ { \prime } / \mathfrak { F } ^ { \prime }$of$\mathcal { G } / \mathfrak { F }$by$\pi .$We will then examine the following cases of$\mathcal { G } ^ { \prime } / \mathfrak { F } ^ { \prime }$at a closed point$\xi ^ { \prime }$of$\pi ^ { - 1 } ( \xi ) \cap S i n g ( \mathcal { G } )$

$$
C a s e (A. 0): \mathfrak {z} \in v a n d \mathbf {d} - 1 \equiv 0 \mod p
$$

$$
C a s e (A. 1): \mathfrak {z} \in v a n d \mathbf {d} - 1 \not \equiv 0 \mod p
$$

$$
\text { Case } (B. 0): \mathfrak {z} \notin v \text { and } \mathbf {d} - 1 \equiv 0 \mod p
$$

$$
\text { Case } (B. 1): \mathfrak {z} \notin v \text { and } \mathbf {d} - 1 \not \equiv 0 \mod p
$$

We first focus our attention to the cases:$C a s e ( A . 1 )$and$C a s e ( B . 1 )$ Namely assume resor$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = \mathbf { d } - 1 \neq 0$mod$p$with d of Eq.(38.5).

In this case an imporant role is played by the$\sharp f r o n t$size$\sharp ( \mathfrak { F } )$of$\mathfrak { F }$ in the sense of Def.(36.8).

Lemma 40.3. If d$- ~ 1 \not \equiv 0$mod$p$we can then in principle have a new type of cyclic repetition:

$$
\{\mathbf {d} \dots (\mathbf {d} - 1) \dots \mathbf {d} \dots \} i n t e r m s o f r e s i d u a l o r d e r s\tag{40.1}
$$

which repeatedly involving only in the last member$\tilde { \mathcal { G } } ( \tilde { \nu } + 1 )$of the transforms$\tilde { \mathfrak { F } }$. Moreover each time we have such a cycle we have an increase of the ♯-front numver. Therefore any repetition of$E q . ( 4 0 . 1 )$ ends after a finite number of times.

Lemma 40.4. If$\mathbf { d } - 1 \equiv 0$mod$p$and${ \mathfrak { z } } \notin v$then immediately after the first Case III we have

$$
r e s o r d _ {\xi} (\mathcal {G} ^ {\prime}) = \mathbf {d} - 1\tag{40.2}
$$

$$
v ^ {\prime} = (v _ {1} ^ {\prime}. \dots , v _ {t ^ {\prime}} ^ {\prime}) w i t h t ^ {\prime} > 0
$$

$$
i n _ {\xi^ {\prime}} \Big (g ^ {\prime} (\nu^ {\prime} + 1) \Big) = i n _ {\xi^ {\prime}} (\mathfrak {z}) ^ {\mathbf {d} - 1}
$$

$$
s o t h a t w e h a v e
$$

$$
g ^ {\prime} (\nu^ {\prime} + 1) = \phi + u v _ {t ^ {\prime}} ^ {\mathfrak {d} - 1}
$$

where u is a unit of$\rho ( R _ { \xi } ) [ v ^ { \prime } ]$and$\phi \in \rho ( R _ { \xi } ) [ v _ { 1 } ^ { \prime } , \cdot \cdot \cdot , v _ { t ^ { \prime } - 1 } ^ { \prime } ]$with or$d _ { \xi ^ { \prime } } ( \phi ) \ \geq \ \mathbf { d }$

$$
\mathfrak {z} \in \eta (i) w i t h i \leq \nu
$$

in terms of the exceptional parameter z chosen by the definition of prostable transformation as follows:

$$
\operatorname{Case} (A a): \mathfrak {z} \in \eta (i) \text {with} i \leq \nu
$$

In this case$\mathfrak { z }$becomes the new member of$v ^ { \prime }$, say the last member. Since$i \le \nu$we must have

$$
\mathfrak {z} ^ {- 1} v _ {j} \in M _ {Z ^ {\prime}, \xi^ {\prime}} (s a y = M ^ {\prime}) f o r a l l \forall j
$$

It follows that z$\mathbf { \nabla } ^ { - \mathbf { d } } \mathbf { g } (  { \boldsymbol \nu } + 1 )$does contribute nothing to the initial form of $\mathbf { g } ^ { \prime }$because the former has order$\geq \mathbf { d }$while the latter has order$= \mathbf { d } - 1$ Moreover we may restrict our interest to the case in which$\mathcal { G } ^ { \prime }$does not have any ♯-key parameter for if otherwise the next residual order change would be down to$\leq \mathbf { d } - 2$. Thus the case of our interest is that any$\bar { \mathfrak { z } } ^ { - \mathbf { d } } \mathbf { g } ( j )$with$i \neq j \leq \nu$does contribute nothing to the initial form of$\mathbf { g } ^ { \prime }$. In fact

$$
o r d _ {\xi^ {\prime}} (\mathbf {f} ^ {\prime} (j)) > \mathbf {d} - 1 f o r a l l i \neq \forall j \leq \nu^ {\prime}\tag{40.3}
$$

where$\mathbf { f } ^ { \prime } ( j )$denotes the j-th relative residual factor of${ \mathfrak { F } } ^ { \prime }$. Finally the contribution of${ \mathfrak { z } } ^ { - \mathbf { d } } \mathbf { g } ( i )$into$\mathbf { g } ^ { \prime }$is exactly its partial sum of those terms belonging to$\rho ( R ^ { \prime } ) [ { \mathfrak { z } } ]$. Therefore according to the definition of prostable transformation we conclude

$$
\mathbf {g} ^ {\prime} (\nu^ {\prime} + 1) = \phi + u v _ {\mathbf {t} ^ {\prime}} ^ {\prime} ^ {\mathbf {d} - 1}\tag{40.4}
$$

$$
\phi \in \rho (R ^ {\prime}) [ v _ {1} ^ {\prime}, \dots , v _ {t ^ {\prime} - 1} ^ {\prime} ] w i t h o r d _ {\xi^ {\prime}} (\phi) \geq \mathbf {d}
$$

$$
a n d u i s a u n i t o f t h e l o c a l r i n g \rho (R ^ {\prime}) [ v ^ {\prime} ]
$$

where$R ^ { \prime } = R _ { Z ^ { \prime } , \xi ^ { \prime } }$and$t ^ { \prime }$is the size of the cofactor parameters$v ^ { \prime }$of$\mathcal { G } ^ { \prime }$. Incidentally in this case we have$\boldsymbol { v } ^ { \prime } = ( \boldsymbol { \mathfrak { z } } ^ { - 1 } \boldsymbol { v } , \boldsymbol { \mathfrak { z } } )$where$\mathfrak { z } = v _ { \mathbf { t } ^ { \prime } } ^ { \prime }$. As for the next blowup on$Z ^ { \prime }$, say$\pi ^ { \prime } : Z ^ { \prime \prime } \to Z ^ { \prime }$with center$D ^ { \prime }$, we must have

$$
v _ {\mathbf {t} ^ {\prime}} ^ {\prime} \text {vanish on} D ^ {\prime}\tag{40.5}
$$

because of Eq.(40.4). Therefore$D ^ { \prime }$cannot be generic-down type. If the chosen exceptional parameter is not$v _ { \mathbf { t } ^ { \prime } } ^ { \prime }$then Case I cannot happen for the blowup following after$\pi ^ { \prime }$. If if is then we will lose the parameter and gain ♯-key parameter while the residual order go down to the original d. This leads to a new type of cyclic repetition:

$$
\left\{\mathbf {d} \dots (\mathbf {d} - 1) \dots \mathbf {d} \dots \right\} i n t e r m s o f r e s i d u a l o r d e r s\tag{40.6}
$$

which repeatedly involving only in the last member$\tilde { \mathcal { G } } ( \tilde { \nu } + 1 )$of the transforms$\tilde { \mathfrak { F } }$

Since d$- 1 \equiv 0$mod$p ,$what follows after each Case III must be the case of blowup with generic-down center. We will set our global strategy in such a way that the cycle Eq.(40.1) cannot repeat indefinitely.

$$
\operatorname{Case} (A b): \mathfrak {z} \in v
$$

Remark 40.3. When Case III happens and Case II follows possibly repeatedly, the result becomes more delicately case-dependent. In any event we are interested in the case in which the residual order is kept equal to d − 1 after the transformation as above.

Remark 40.4. After Case III occured for the first time as above we will continue our work by dividing the problem into the following two cases.

Case(n-y): The case in which d$\not \equiv 0$mod$p$while$\mathbf { d } - 1 \equiv 0$mod$p .$

The cofactor has been augumented with one new variable created by each blowup from the very starting point untill after the occurance of the Case III, although some old cofactor variables may be removed when one of them turns out to be the exceptional parameter chosen there for the blowup. After the Case III no such new cofactor variables are created into the transforms of subsequent cofactors. This is so by $\mathbf { d } - 1 \equiv 0$mod$p .$.

$C a s e ( n - n )$: The case in which d$\not \equiv 0$mod$p$and$\mathbf { d } - 1 \not \equiv 0$mod$p .$ In this situation all the way from the beginning to the end the co-factor is augumented one by one with newly created variable while possibly some old cofactor variables may be removed when the exceptional parameter belongs to the previous cofactor.

Remark 40.5. Let us assume the$C a s e ( c )$of Rem.(??). We then have the following subcases to investigate separately.

Case(c, 1) when v is a singleton (z). Then we claim that there can occur only Cases$I V$

$C a s e ( c , 2 )$when v has more components. In this case, Case I can happen whence resor$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = r e s o r d _ { \xi } ( \mathcal { G } ) + 1$and$v ^ { \prime } = \emptyset$. We then claim that if so then$\mathcal { G } ^ { \prime }$is either in the$C a s e ( a )$or$C a s e ( b )$. Moreover if$\mathcal { G } ^ { \prime }$in$C a s e ( b )$we claim to have$\left| v ^ { \prime } \right| < \left| v \right|$where$v ^ { \prime }$is the cofactor parameter of$\mathcal { G } ^ { \prime }$and | | denotes the number of components. Therefore we claim that$C a s e ( c )$cannot occur infinitely many times.

Definition 40.1. Because an important role will be played by the number$| v |$we will denote this number by ♯t(G).

## 41. p-prostable monomialization

Theorem 41.1. Assume that$\mathbf { d } \equiv \mathbf { \boldsymbol { 0 } }$mod$p$at the starting point of $E q . ( 3 8 . 6 )$. If a global strategy is set in such a way that no sequence $o f$fitted permissible blowup is allowed to contain any infinite chain of only Case II locally above the given point$\xi$then any such a sequence must contain a step at which we have or$\mathbf { \partial } \cdot d _ { \tilde { \xi } } ( \tilde { \mathcal { G } } ) < \mathbf { d } - 1$

Recall Rem.(39.1). Thanks to the theorem we are only left with the problem in the case of d$\not \equiv \ 0$mod$p .$In this case we ask questions about what we may have and what we should then do after a finite sequence of fitted permissible blowups$\varpi : \tilde { Z } \to Z$applied to$\mathcal { G }$and${ \mathfrak { F } } .$ Although all object and numbers must be marked$\mathrm { b y } ^ { \sim } ,$we restart with all the notations simplified by droping ˜ everywhere.

Remark 41.1. We may restart with the following simplified notation but with the more general assumptions.

(1) We have

$$
\mathbf {d} \geq \mathbf {d} ^ {\prime} \geq \mathbf {d} - 1\tag{41.1}
$$

in the sense of Eq.(38.5) and$\mathrm { E q . ( 4 1 . 1 ) }$. For the inequalities we should refer to Prop.(38.1), Prop.(38.2) and Th.(34.1). We consider that our job done if$\mathbf { d } ^ { \prime } < \mathbf { d } - 1$even after a finite number of repeated blowups.

(2) We write cofactor parameters$v = ( v _ { 1 } , \cdots , v _ { \mathrm { t } } )$of$\mathcal { G }$with$\textrm { \bf t } =$ $\sharp \mathbf { t } ( \mathcal { G } )$of Def.(40.1). After a blowup we will write$\mathbf { t } ^ { \prime }$for$\sharp { \bf t } ( \mathcal { G } ^ { \prime } )$ Keep it in mind that at the very starting point we had$\mathbf { t } = 0$ and$v = \emptyset$

(3) Let us recall that by means of the relative residual factors$\mathbf F ( i )$ of Def.(36.1) we have defined the number$\flat o r d _ { \xi } ( \mathfrak { F } )$of Eq.(36.13) in terms of Eq.(36.6) and Eq.(36.7). For short we write

$$
\mathfrak {b} (d) = \mathfrak {b} o r d _ {\xi} (\mathfrak {F}) = m i n _ {i \leq \nu} o r d _ {\xi} \mathbf {F} (i) \geq o r d _ {\xi} (\mathbf {F}) \geq \mathbf {d}\tag{41.2}
$$

We will also use the number$\sharp o r d _ { \xi } ( \mathfrak { F } )$defined by$\mathrm { E q . ( 3 6 . 1 2 ) }$of Def.(36.5. For short we write

$$
\sharp (d) = \sharp o r d _ {\xi} (\mathfrak {F})\tag{41.3}
$$

Incidentally the number$\flat ( d )$and$\sharp ( d )$depends upon the choice of a prostable presentation$\mathfrak { F }$of$\mathcal { G }$at the given$\xi .$

(4) Remember that we must have

$$
\sharp (d) = \flat (d) = \mathbf {d} a t t h e s t a r t i n g p o i n t\tag{41.4}
$$

because$v = \emptyset$and$\mathbf { g } (  { \boldsymbol \nu } + 1 ) = 0$. However at any of the later steps we have only the inequlities:

$$
0 <   \sharp (d) \leq \flat (d) \leq \mathbf {d} i n g e n e r a l\tag{41.5}
$$

in virtue of Eq.(36.11) after Lem.(36.2) and in comparison of Eq.(36.5) vs Eq.(36.6).

Remark 41.2. Assume d$\not \equiv 0$mod$p$at the starting point. Prop.(38.2) holds and hence Prop.(38.1) is valid at the starting point. Namely we start with a nonempty system of ♯-key parameters of$\mathcal { G }$Hence Case I cannot happen until after Case III or Case IV occurs. Consider the case in which only Case II occur repeatedly for a finite number of times. There each time of blowup a new cofactor parameter is created while there remain ♯-key parameters which are transforms of those at the starting point. Case I cannot happen there. When Case III happens for the first time we gain a new cofactor parameter but we may or may not lose one of the earlier ♯-key parametrs. This double possibility about earlier ones will be made clearer below.

Remark 41.3. We then need to examine the following two possibilities separately.

(1) d$. - 1 \equiv 0$mod$p .$

(2)$\mathbf { d } - 1 \neq 0$mod$p .$

Now for the sake of notational simplicity, the transformed /<sup>p</sup>-exponent will be denoted by$\mathcal { G }$again though we now have$\mathbf { d } ( \mathcal { G } ) = \mathbf { d } - 1$. Similarly the transformed$/ ^ { p } .$-prostable presentation will be newly denoted by$\mathfrak { F }$.

Remark 41.4. We consider the case of$\mathbf { d } - 1 \equiv 0$mod$p .$. Since we are at the point immediate after the first Case III,$g ( \nu + 1 )$must be in the following form.

$$
g (\nu + 1) = \phi + C v ^ {\mathbf {d} - 1}
$$

where$\phi \in \rho ( R _ { \xi } ) [ v _ { l } , \cdot \cdot \cdot , v _ { \mathbf { t } - 1 } ]$with${ d e g } ( \phi ) \leq \mathbf { d } - 1$and$C \in \mathbb { K }$

Remark 41.5. We have

$$
i n _ {\xi} (g (\nu + 1)) = \sum_ {k \in \Delta} u _ {k} i n _ {\xi} (v _ {k}) ^ {\mathbf {d} - 1}
$$

where$c _ { k }$are nonzero elements in$\mathbb { K }$and$\Delta \subset [ 1 , \mathbf { t } ]$

Definition 41.1. Under this condition$\operatorname { E q . } ( ? ? )$, the set$\{ v _ { k } , k \in \Delta \}$ is uniquely determined and each$v _ { k }$of Eq.(??) is called a ♭-frontier parameter of${ \mathfrak { F } } .$. This notion, up to a unit multiple, uniquely determined by$\mathcal { G }$and independent of the choice of$\mathfrak { F }$. We thus call$\Delta$the frontier index set and$\{ v _ { k } , k \in \Delta \}$the ♭-frontier parameters of$\mathcal { G }$

Lemma 41.2. Let$\pi : Z ^ { \prime } \to Z$with center D be a fitted permissible for$\mathcal { G }$. Then every ♭-frontier parameter$v _ { j }$is in the ideal$I _ { \xi } ( D , Z ) ^ { \mathfrak { d } }$ Moreover if resor$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = r e s o r d _ { \xi } ( \mathcal { G } )$with the transform G′ of$\mathcal { G }$by $\pi$then the transform$\boldsymbol { v } _ { j } ^ { \prime } = \boldsymbol { \mathfrak { z } } ^ { - 1 } \boldsymbol { v } _ { j }$is a ♭-frontier parameter of$\mathcal { G } ^ { \prime }$at$\xi ^ { \prime }$ provided that$v _ { j } ^ { \prime } \in \boldsymbol { M } _ { \xi ^ { \prime } }$and hence$v _ { j } ^ { \prime } \in \boldsymbol { v } ^ { \prime }$

The following theorems are based upon the conditions and assumptions of Rem.(41.1).

Theorem 41.3. If resor$d _ { \xi } ( \mathcal { G } ) \ \leq$resord<sub>ξ</sub> (G′) then$\xi ^ { \prime }$is metastable of G for π at$\xi ^ { \prime }$. Moreover we have$o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = o r d _ { \xi } ( \mathcal { G } ) + 1$and the cofactor parameters$v ^ { \prime }$in the abc-expression$E q . ( 3 8 . 4 ) \ o f \ g ^ { \prime }$is empty.

Theorem 41.4. Let us assume

$$
\operatorname{resord} _ {\xi} (\mathcal {G}) = \mathfrak {d} \not \equiv 0 \mod p\tag{41.6}
$$

where d is the number ofof$E q . ( 4 1 . 3 )$. Moreover assume that the chosen exceptional parameter z is a ♯-key parameter of$\mathcal { G }$We then have that or$\cdot d _ { \xi ^ { \prime } } ( \mathcal G ^ { \prime } ) \le \mathfrak { d } - 2$

Theorem 41.5. Assume$E q . ( 4 1 . 6 )$. Moreover assume that$| v | = | \Delta | >$ $0 , i . e ,$the system v of cofactor parameters is not empty for G and every member of v is a ♯-frontier parameter of$\mathcal { G }$. Then any$\xi ^ { \prime }$cannot be metastable for$\mathcal { G } ^ { \prime }$at$\xi ^ { \prime }$.

Theorem 41.6. If the chosen exceptional parameter z is any one of the ♭-frontier parameters then we have either or$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) \leq \mathfrak { d } - 2 o r \xi ^ { \prime }$ must be metastable.

Lemma 41.7. Let us asssume

$$
o r d _ {\xi^ {\prime}} (\mathcal {G} ^ {\prime}) = \mathfrak {d} - 1 = \mathfrak {d} \equiv 0 \mod p\tag{41.7}
$$

We can then find Ambient Redutive Cleaning of which the final transform satisies the second assumption of$T h . ( 4 1 . 5 )$

Remark 41.6. (1) Ambient Redutive Cleaning.

Consider the case in which

$$
\mathbf {d} \not \equiv 0 \mod p a n d \mathfrak {d} = \mathbf {d} - 1 \equiv 0 \mod p.
$$

We then apply ambient reduction theorem to each hypersuface one of$z _ { j } = 0$with$z _ { j }$which is not any of the frontier cofactor Γ-parameters. Repeat this. We then can reach the state in which v consists of only ♭-frontiers.

(2) No problem if exceptional becomes new cofactor

Proposition 41.8. Assume that$o r d _ { \xi } ( \mathcal { G } ) = \mathbf { d } \not \equiv \ 0$mod p with d of $E q . ( 3 8 . 5 )$. Let ι be the index such that the chosen exceptional parameter z belongs to$\eta ( \iota )$. We then have the following cases.

(1)$\iota \leq \nu$and z is a ♯-key parameter of G. Assume d$\not \equiv 0$mod$p ,$in particular$\mathfrak { d } = \mathbf { d }$. In this case we claim that or${ { d } _ { \xi ^ { \prime } } ( \mathcal G ^ { \prime } ) \leq \mathfrak { d } - 2 }$ There results the case that fits our inductive proof by virtue of Moh’s theorem.

(2) Assume$\mathfrak { d } \equiv \mathrm { ~ 0 ~ }$mod$p ,$so that we must have$\mathfrak { d } = \mathbf { d } - 1$. In this case, for every sequence of fitted permissible blowups with sequence of corresponding singular points, metastable points do not occur provided that the orders do not drop below d. Moreover if the order drops below then it becomes the case that fits our inductive proof by virtue of Moh’s theorem.

(3)$\iota ~ \leq ~ \nu , ~ 3$is not any ♯-key parameter of G and o$\cdot d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) =$ or$\mathbf { \nabla } \cdot d _ { \xi } ( \mathcal { G } ) = \mathbf { d }$. Now let$\nabla ( + )$be the set of those j such that $v _ { j } \in I _ { \xi } ( D , Z )$and let$\nabla ( \overset { \cdot } { - } ) \overset { \cdot } { = } [ 1 , \ell ] \setminus \nabla ( \overset { \cdot } { + } )$. Since$\iota \leq \nu$we have$\mathfrak { z } ^ { - 1 } v _ { j } \ \in \ \mathcal { M } _ { \xi ^ { \prime } }$for all$j ~ \in ~ \nabla ( + )$Thus v′ is the union of$\{ \ r _ { \partial } ^ { - 1 } v _ { j } , \ r _ { j } ^ { - } \in \nabla ( + ) \}$and$\{ v _ { k } , k \in \nabla ( - ) \}$Moreover since or$\mathbf { \boldsymbol { \mathscr { d } } } _ { \xi } ( \mathcal { G } ) = \mathbf { \boldsymbol { \mathbf { d } } } \not \equiv \ \boldsymbol { 0 }$mod$p , ~ 3$is taken out of$\eta ( \iota )$and included into v′. We thus have$\left| { v ^ { \prime } } \right| = \left| { v } \right| + 1$

(4)$\iota ~ \leq ~ \nu , ~ 3$is not any ♯-key parameter of G and$o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) <$ $o r d _ { \xi } ( \mathcal { G } ) = \mathbf { d }$. In this case, too, we claim to have all of the same as previous case. Only diference is that in this case we gain$\mathbf { \hat { \mathbf { 0 } } } < \mathbf { d }$and

$$
g ^ {\prime} (\nu + 1) = V ^ {\prime} + u _ {0} \mathfrak {z} ^ {\mathfrak {d}} + \sum_ {k \in \Delta^ {\prime}} u _ {k} v _ {k} ^ {\prime \mathfrak {d}}
$$

with o$\cdot d _ { \xi ^ { \prime } } ( V ^ { \prime } ) > 0 , \ u _ { k }$are units in$\rho ^ { e } ( R _ { \xi } ) [ v ]$and$\Delta ^ { \prime }$is some subbset of the indexset of$v ^ { \prime }$. Incidentally if o$r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) < \mathbf { d } - 1$ then it becomes the case that fits our inductive proof by virtue of Moh’s theorem. In other words, it is enough to examine the case with$o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = \mathbf { d } - 1$. Either the set$\Delta ^ { \prime }$or$\Delta ^ { \prime } \cup \{ 0 \}$may or may not be the ♭-frontier index set of the transform${ \mathfrak { F } } ^ { \prime }$of F, but$\Delta ^ { \prime } \cup \{ 0 \}$contains the ♭-frontier index set.

(5)$\iota \leq \nu , 3$is not any ♯-key parameter of G and$\mathbf { d } - 1 = o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) =$ $o r d _ { \xi } ( \mathcal { G } )$. In this case there is no possibility of metastable points because z is not a member of v. For more details we need to examine the following two subcases separately.

(a) d$- ~ 1 \equiv ~ 0$mod p. Then z makes the singleton$\eta ^ { \prime } ( \nu ^ { \prime } ) =$ $\eta ^ { \circ } ( \nu + 2 )$of Eq.(37.10). It is not included in v′. Let$\nabla ( + )$ and$\nabla ( - )$be the same as before. Since$\iota \ \leq \ \nu$we have $\mathfrak { z } ^ { - 1 } v _ { j } \ \in \ \mathcal { M } _ { \xi ^ { \prime } }$for all$j ~ \in ~ \nabla ( + )$Thus$v ^ { \prime } \ i s$the union $o f \ \{ \ l _ { 3 } ^ { - 1 } v _ { j } , j \ \in \ \nabla ( + ) \}$and$\{ v _ { k } , k \in \nabla ( - ) \}$. Here$t h e \ b -$ frontier parameters are among those$v _ { j }$with$j \in \nabla ( + )$by Lem.$( 4 1 . 2 )$. In any event we have$| \boldsymbol { v ^ { \prime } } | = | \boldsymbol { v } |$

(b) d$- 1 \not \equiv 0$mod p. Then$\eta ^ { \circ } ( \nu { + } 2 )$is empty and z is included in$\eta ^ { \prime } ( \nu ^ { \prime } + 1 ) = v ^ { \prime }$. We have$\left| { v ^ { \prime } } \right| = \left| { v } \right| + 1$

(6)$\iota \leq \nu ,$z is not any ♯-key parameter$o f { \mathcal { G } }$and$o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) < \mathbf { d } - 1$ There results the case that fits our inductive proof by Moh’s theorem.

(7)$\textit { \textbf { 3 } } \in \textit { \textbf { v } }$(so that$\iota \ = \ \nu + 1$and v is not empty), o$\cdot d _ { \xi } ( \mathcal { G } ) =$ $o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = \mathbf { d } . \ 3$is included in v′. Let us write$v = ( v ( + ) , v ( - ) )$ with$v ( + ) = v \cap I ( D , Z )$as before. Let$v ( + ) = \{ v _ { j } , j \in \nabla ( + ) \}$ and$v ( - ) ~ = ~ \{ v _ { j } , j ~ \in ~ \nabla ( - ) \}$. Then write${ \mathfrak { z } } ^ { - 1 } v _ { j } \ = \ v _ { j } ^ { \prime } + \varpi _ { j }$ where$\boldsymbol { v } _ { j } ^ { \prime } \in \boldsymbol { M } _ { \xi ^ { \prime } }$and$\varpi \in \mathbb { K }$. Write$v ( + ) = ( v ( + 0 ) , \stackrel { . } { v } ( + * ) )$ where$\bar { v ( + 0 ) } = \left\{ v _ { i } ^ { \prime } \vert j \in \nabla ( + ) , \varpi _ { j } = 0 \right\}$and$v ( + * ) = \left\{ v _ { j } ^ { \prime } \vert j \in \right.$ $\nabla ( + ) , \varpi _ { j } \neq 0 \}$from which we exclude the one$f o r v _ { j } = { 3 }$. Then $v ^ { \prime } = ( v ( \bar { + } 0 ) , v ( - ) , \bar { \partial } )$. If$v _ { j } \neq \mathfrak { z }$is a ♭-frontier for G at ξ then $j \in \nabla ( + 0 )$by Lem.$( 4 1 . 2 )$and$\boldsymbol { v } _ { j } ^ { \prime }$is a ♭-frontier for G′ at$\xi ^ { \prime }$ However z may be or may not be a ♭-frontier parameter for$\mathcal { G } ^ { \prime }$ at ξ′.

(8)$\pmb { \mathscr { z } } \in \textit { v o r d } _ { \xi } ( \mathcal { G } ) = \mathbf { d }$and or$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = \mathbf { d } - 1$. In this case, too, z is included in v′ but it may be or may not be a ♭-frontier parameter for$\mathcal { G } ^ { \prime }$at$\xi ^ { \prime }$.

(9)$\mathfrak { z } \in \ v , \ o r d _ { \xi } ( \mathcal { G } ) = \mathbf { d }$and$o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) < \mathbf { d } - 1$. There results the case that fits our inductive proof by Moh’s theorem.

(10)$\mathfrak { z } \in \upsilon , o r d _ { \xi } ( \mathcal { G } ) = o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = \mathbf { d } - 1$. Let us then examine the followin three cases separately.

(a)$\mathbf { d } - 1 \equiv 0$mod p and z is not any of the frontier members $o f v .$

(b)$\mathbf { d } - 1 \equiv 0$mod p and z is a frontier member of v.

$$
(c) \mathbf {d} - 1 \not \equiv 0
$$

(11) z ∈ v, ord<sub>ξ</sub>(G) = d − 1 and ord<sub>ξ′</sub>(G′) < d − 1.

(12)$\mathfrak { z } \in \upsilon , o r d _ { \xi } ( \mathcal { G } ) = \mathbf { d } - 1 \equiv \ 0$mod$p$and or$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = \mathbf { d }$. This is the metastable case. However we claim that G′ has a longer system of frontier ♯-key parameters than that of the$/ ^ { p }$-exponent preceeding G.

Proposition 41.9. Under the assumption of Rem.$( 4 1 . 1 )$, the next$f i t -$ ted permissible blowup π for G cannot have any metastable point in $\pi ^ { - 1 } ( \xi )$in the following cases:

(1)$\mathbf { \hat { \mathbf { 0 } } } = \mathbf { d }$, divisible by p. Morover either v is empty or there exists a nonempty system of ♯-key parameters of G at$\xi$.

(2)$\mathfrak { d } \ = \textbf { d } - \ 1$and d is divisible by p. The reason is that the equality with the divisibility can only happen when one of the resord<sub>ξ′</sub>(G(i) with$i \ \leq \ \nu$drops to d − 1 because the new addition to$\eta ^ { \prime } ( \nu + 1 )$must be a power of a single element up to a unit-multiple. Observe this fact immediately after d drops to d − 1 and at least one ♯-key parameters of G at ξ is created and upheld afterwords. (Examine the following two cases separately: (a) z ̸∈ v

$$
(b) \mathfrak {z} \in v
$$

In this second case,

(3)$\mathfrak { d } \geq \mathbf { d } - 1$and$\mathfrak { z } \in \eta ( i )$with$i \leq \nu$is a frontier ♯-key parameter $o f { \mathcal { G } } . ~ n$

(4) the only one remaining case is that$\mathbf { \boldsymbol { \mathsf { 0 } } } = \mathbf { \boldsymbol { \mathsf { d } } } - 1$and it is not

(1)$3 \notin v$

(2)$3 \in \upsilon$

In the second subcases, investigate

$$
| f r o n t i e r \sharp - k e y s) | + l (v) |
$$

Proposition 41.10. Under the same conditions as of Prop.$( 4 0 . 2 )$then the frontier rank of${ \mathfrak { F } } ^ { \prime }$at$\xi ^ { \prime }$is bigger than that of$\mathfrak { F }$at$\xi$.

Remark 41.7. In fact, we reason as follows:

(1) Consider the case$\boldsymbol { \mathfrak { d } } \ = \ \mathbf { d }$. Then we must have a nonempty system of ♯-key system for G from among the η.

(2) Consider the case$\mathbf { \hat { \mathbf { 0 } } } = \mathbf { d } - 1$so that$\Delta$is not empty. Hence v is not empty. We have one and only one of the following two cases:

(a) d is not divisible by$p .$In this case$\pi$cannot have any metastable point in$\pi ^ { - 1 } ( \xi )$because$\textstyle \sum _ { k \in \Delta } { \bar { u } } _ { k } \theta _ { k } ^ { 0 }$cannot be any partial sum of$\prod _ { j } ( \theta _ { k } - \theta - 1 ) ^ { - \mathbf { c } _ { j } }$

(b) d is divisible by p. In this case metastable point can happen. However the transform becames generic-down case. Then the length of ♯-key parameters definitely increase. This cannot repeat indefinitely. (Use the fact that if metasta happens then all the v transform to units.

Proposition 41.11. Under the assumption of Rem.$( 4 1 . 1 )$, let us pick $\xi ^ { \prime } \in \pi ^ { - 1 } ( \xi ) \subset Z ^ { \prime } \cap S i n g ( \mathcal { G } ^ { \prime } )$for the transform$\mathcal { G } ^ { \prime }$of G by the next fitted permissible blowup$\pi : Z ^ { \prime } \to Z$with center$D \ni \xi$and we consider ι of $\mathfrak { z } \in \eta ( \mathfrak { L } )$with the chosen exceptional parameter z at$\xi ^ { \prime }$. Then always$v ^ { \prime }$ of$\mathcal { G } ^ { \prime }$is equal to the singleton (z).

Proposition 41.12. Under the same assumption of Prop.$( 4 0 . 2 )$there are the following cases on$\mathcal { G } ^ { \prime }$

(1) re${ } \cdot s o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = r e s o r d _ { \xi } ( \mathcal { G } )$and ♯-key parameters of G are transformed into those of$\dot { \mathcal { G } ^ { \prime } }$.

(2) reso$u _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) < r e s o r d _ { \xi } ( \mathcal { G } )$. There then exists the following two subcases:

(a) There exists a ♯-key parameter of G which is linearly independent of z modulo$M _ { \xi } ^ { 2 }$

(b) There is no such parameter.

In the case$( 1 - a )$(subcase (a) of case (1)) G′ possesses at least one ♯-key parameter. In the case of (1, 2) there is no other restriction on z. In (2, 1) and (2, 2) it is enough to consider the case of resor$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = r e s o r d _ { \xi } ( \mathcal { G } ) - 1$. In (2, 2) the number resord<sub>ξ</sub>$( \mathcal { G } ^ { \prime } ) ( = \mathbf { d } - 1 )$cannot be divisible by$p .$. In (2, 1) we have its subcases as follows:

(1)$\mathcal { G }$is pseudo-stable along the center D so that$\mathbf { d } = 1 + A p$with a positive integer A. Hence we have$r e s o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = A p$

(2) G) has at least two independent ♯-key parameters.

Proposition 41.13. Under the assumption of Prop.(41.11), Assuming $t h a t r e s o r d _ { \xi ^ { \prime } } ( { \mathcal G } ^ { \prime } ) \ge r e s o r d _ { \xi } ( { \mathcal G } ) - 1$we have one of the following cases:

(1) or$\cdot d _ { \xi } ( \mathcal { G } ( \iota ) ) \ = \ o r d _ { \xi } ( \mathcal { G } )$, reso$\cdot d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) ~ = ~ r e s o r d _ { \xi } ( \mathcal { G } ) - 1$and$\mathcal { G } ^ { \prime }$ contains at least one ♯-key parameter.

(2)$o r d _ { \xi } ( \mathcal { G } ( \iota ) ) \ : = \ : o r d _ { \xi } ( \mathcal { G } )$$r e s o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = r e s o r d _ { \xi } ( \mathcal { G } ) - 1$and$\mathcal { G } ^ { \prime }$ does not contain any ♯-key parameter. In this case$i n _ { \xi ^ { \prime } } ( g ^ { \prime } ) \in$ $\rho ( R _ { \xi ^ { \prime } } )$and resor$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } )$is divisible by$p .$

(3) or$d _ { \xi } ( \mathcal { G } ( \iota ) ) \ > \ o r d _ { \xi } ( \mathcal { G } )$and the same condition of Rem.(??) is maintained with the the same number d by the transforms$\mathcal { G }$ and$\mathfrak { F }$.

(4)$r e s o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) r e s o r d _ { \xi } ( \mathcal { G } )$

There exists one and only one index i with$1 \leq i \leq \nu$such that $o r d _ { \xi } ( \mathcal { G } ( i ) ) = o r d _ { \xi } ( \mathcal { G } )$

Theorem 41.14. Finally the problem boiles down to the games only to the case of$^ { \prime \ell } a l l$in$v ^ { \dprime }$

Definition 41.2. In the Case I, we must have${ \mathfrak { z } } \in v$with v of$\mathcal { G }$itself. Hence either Case A or Case B is possible.

In the (case II), every one of the (cases ABC) is possible. In both of these cases, if$o r d _ { \xi ^ { \prime } } ( \mathcal { G } ( 1 ) ^ { * } ) > o r d _ { \xi ^ { \prime } } ( \mathcal { G } ( 2 ) ^ { * } )$then we let$\eta ^ { \prime } ( i ) = \eta ^ { * } ( i )$for $i = 1 , 2 .$, and$\eta ^ { \prime } ( 3 ) = \eta ^ { * } ( 3 ) \cup \eta ^ { * } ( 4 )$. If o$\cdot d _ { \xi ^ { \prime } } ( \mathcal { G } ( 1 ) ^ { * } ) = o r d _ { \xi ^ { \prime } } ( \mathcal { G } ( 2 ) ^ { * } )$then we let$\eta ^ { \prime } ( 1 ) = \varnothing , \eta ^ { \prime } ( 2 ) = \eta ^ { * } ( 1 ) \cup \eta ^ { * } ( 2 )$and$\eta ^ { \prime } ( 3 ) = \eta ^ { \ast } ( 3 ) \cup \eta ^ { \ast } ( 4 )$ In the (case III), if o$\cdot d _ { \xi ^ { \prime } } ( \mathcal { G } ( 1 ) ^ { * } ) > o r d _ { \xi ^ { \prime } } ( \mathcal { G } ( 2 ) ^ { * } )$and$o r d _ { \xi ^ { \prime } } ( \mathcal { G } ( 2 ) ^ { * } ) =$ $o r d _ { \xi } ( \mathcal { G } ) - 1$then we let$\eta ^ { \prime } ( i ) = \eta ^ { * } ( i )$for$i = 1 , 2$, and$\eta ^ { \prime } ( 3 ) = \eta ^ { * } ( 3 ) \cup$ $\eta ^ { * } ( 4 )$. If$o r d _ { \xi ^ { \prime } } ( \mathcal { G } ( 1 ) ^ { * } ) \le o r d _ { \xi ^ { \prime } } ( \mathcal { G } ( 2 ) ^ { * } )$and$o r d _ { \xi ^ { \prime } } ( \mathcal { G } ( 1 ) ^ { * } ) = o r d _ { \xi } ( \mathcal { G } ) - 1$ then we let$\eta ^ { \prime } ( 1 )$is empty,$\eta ^ { \prime } ( 2 ) = \eta ^ { \ast } ( 1 ) \cup \eta ^ { \ast } ( 2 )$and$\eta ^ { \prime } ( 3 ) = \eta ^ { \ast } ( 3 ) \cup \eta ^ { \ast } ( 4 )$ If$o r d _ { \xi ^ { \prime } } ( \mathscr { G } ( 1 ) ^ { * } ) \geq o r d _ { \xi ^ { \prime } } ( \mathscr { G } ( 2 ) ^ { * } ) \mathrm { ~ a n d ~ } o r d _ { \xi ^ { \prime } } ( \mathscr { G } ( 1 ) ^ { * } ) = o r d _ { \xi } ( \mathscr { G } )$then it must be the (case C) and$o r d _ { \xi ^ { \prime } } ( \mathcal { G } ( 3 ) ^ { * } ) = o r d _ { \xi } ( \mathcal { G } ) - 1$. The we let$\eta ^ { \prime } ( 1 ) =$ $\eta ^ { * } ( 1 ) \cup \eta ^ { * } ( 2 )$and$\eta ^ { \prime } ( 2 ) = \eta ^ { \ast } ( 3 )$. We let$\eta ^ { \prime } ( 3 ) = \eta ^ { * } ( 4 )$

In the (case IV), we let$\eta ^ { \prime } ( 1 ) = \emptyset$and let$\eta ^ { \prime } ( 2 )$be the system of either ♯0-parameters of$\mathcal { G } ^ { \prime }$if it is not empty, or$\sharp ( 1 )$-parameters of$\mathcal { G } ^ { \prime }$if otherwise. We let$\eta ^ { \prime } ( 3 )$be the system of those parameters (free to choose) which together with$\eta ^ { \prime } ( 2 )$make up a regular system of parameters of $R _ { \xi ^ { \prime } }$

Remark 41.8. Let$\pi : Z ^ { \prime } \longrightarrow Z$be a blowup with center D which is p-prostable permissible for the given$\mathfrak { F }$in the sense of Def.(??) with $q = p$for the$\mathfrak { F }$. Let${ \mathfrak { F } } ^ { \prime }$be the transform of$\mathfrak { F }$by$\pi$in the sense of Def.(??). Namely we write

$$
\mathfrak {F} ^ {\prime} = \{\mathcal {G} ^ {\prime}; \mathcal {G} ^ {\prime} (i), \eta^ {\prime} (i), 1 \leq i \leq \nu^ {\prime} + 1 \}\tag{41.8}
$$

The following is a consequence of the theorem Th.(34.1) of T-T Moh.

Theorem 41.15. Then according to the notations of$D e f . ( 3 5 . 1 )$for $D e f . ( 2 ? )$and$D e f . ( ? ? ) f o r E q . ( 4 1 . 8 )$, we have

(41.9)

$$
\begin{array}{c} r e s o r d _ {\xi} (\mathfrak {F}) = r e s o r d _ {\xi} (\mathcal {G}) = o r d _ {\xi} (\mathbf {g}) \\ = \min _ {1 \leq i \leq \nu + 1} \{o r d _ {\xi} (\mathbf {g} (i)) \} \\ a n d \end{array}\tag{41.10}
$$

$$
\begin{array}{c} r e s o r d _ {\xi^ {\prime}} (\mathfrak {F} ^ {\prime}) = r e s o r d _ {\xi^ {\prime}} (\mathcal {G} ^ {\prime}) = o r d _ {\xi^ {\prime}} (\mathbf {g} ^ {\prime}) \\ = \min _ {1 \leq i \leq \nu^ {\prime} + 1} \{o r d _ {\xi^ {\prime}} (\mathbf {g} ^ {\prime} (i)) \} \end{array}
$$

Moreover we have either one of the following three case:.

(1) (The metastable case.) This is the case of$r e s o r d _ { \xi } ( \pmb { \mathfrak { F } } ) + 1 =$ resor$d _ { \xi ^ { \prime } } ( \pmb { \mathfrak { F } } ^ { \prime } )$which means resor$d _ { \xi } ( \mathcal { G } ) + 1 = r e s o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } )$. By Moh’s Theorem$( \it { 3 4 . 1 } )$we know that resord<sub>ξ</sub> (G′) is less or equal to resor$d _ { \xi } ( \mathcal { G } ) + 1$

(2) (The stable case.) This is the case of resor$d _ { \xi } ( \mathfrak { F } ) = r e s o r d _ { \xi ^ { \prime } } ( \mathfrak { F } ^ { \prime } )$

(3) (The improved case.) This is the case of resor$d _ { \xi } ( \mathfrak { F } ) > r e s o r d _ { \xi ^ { \prime } } ( \mathfrak { F } ^ { \prime } )$ In this case we prefer to examine the case in the following two subcases separately.

(a) The case of resor${ l } _ { \xi } ( \mathfrak { F } ) - 1 = { r e s o r } { d } _ { \xi ^ { \prime } } ( \mathfrak { F } ^ { \prime } )$

(b) The case of resord$l _ { \xi } ( \mathfrak { F } ) - 1 > r e s o r d _ { \xi ^ { \prime } } ( \mathfrak { F } ^ { \prime } )$

Theorem 41.16. In every case there always happens something favorable for not worsening the given singularities if not clear betterments.

(1) In the first case, G will have a non-empty system of ♯0-key parameters for G′ and the unit p-cofactor. Moreover its residual factor has the order ̸≡ 0 mod$q .$Therefore any sequence of fitted permissible blowup for$\mathcal { G } ^ { \prime }$creates no metastable points having residual orders$> r e s o r d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } )$. Refer to Cor.(23.5) of $T h . ( 2 3 . 4 )$

(2) In the second case, we have an inductive strategy in terms of the edge invariants of G which make it impossible to have the same case with the same residual order repeated indefinite.

(3) The third case has two subcases as follows:

(a) The case of resor$d _ { \xi } ( \mathfrak { F } ) - l = r e s o r d _ { \xi ^ { \prime } } ( \mathfrak { F } ^ { \prime } )$

(b) The case of resor$d _ { \xi } ( \mathfrak { F } ) - l > r e s o r d _ { \xi ^ { \prime } } ( \mathfrak { F } ^ { \prime } )$

Remark 41.9. Let us recall the background in which we formulate our inductive approach for reduction of singularities. Given an ideal exponent$E = ( J , b )$and a given closed point$\xi ~ \in ~ S i n g ( E )$, we have defined the graded algebra$\wp ( E )$called the characteristic algebra of$E$ at ξ by virtue of Th.(8.1). We then set an inductive stategy based upon what we called the edge-invariants defined by Th.(10.1) on$\wp ( E )$, which is called Edge Generators Theorem, Namely we have edge data of$\wp ( E )$consisting of the edge parameters$y = ( y _ { 1 } , \cdots , y _ { r } )$and the edge generators$g = ( g _ { 1 } , \cdots , g _ { r } )$. There each$g _ { i }$is writen in the form

$$
g _ {i} = y _ {i} ^ {q _ {i}} + \epsilon_ {i} \text {with} q _ {i} = p ^ {e _ {i}}
$$

in the manner of Def.(10.1) after Th.(10.1). The the edge-invariant denoted by$\operatorname { I n v } _ { \xi } ( E )$is defined to be

$$
\operatorname{Inv} _ {\xi} (E) = (n, n - r, q _ {1}, \dots , q _ {r})
$$

which has the properties of monotone behavior with respect to permissible blowups thanks to Th.(11.1) which was proven after a few lemmas (11.3)-(11.7). Incidentally the edge-invariants are compared in terms of the lexicographical ordering of Def.(??). We thus follow Inv-sequence of Def.(??) in accord with Rem.(??). Such a sequence of successive blowups will be chosen under the condition of$/ ^ { p _ { . } }$-prostable permissibility with respect to$\scriptstyle / { } ^ { p } - \mathrm { p r o s t a b l e }$presentations and their$/ ^ { p } .$-prostable transforms in the sense of Def.(37.2).

## 42. p-semistable /<sup>q</sup>-singularity

Definition 42.1. We consider a$/ ^ { q } { - }$-exponent$\mathcal { G }$with$q = p ^ { e }$with$e \geq 1$ We say that$\mathcal { G }$is p-semistable, or semistable for short, at a closed point $\xi \in S i n g ( \mathcal { G } )$if we can write it at$\xi$in the follwing form:

$$
\mathcal {G} = (h \parallel / ^ {q}) w i t h h = u \mathrm{e} ^ {\ddot {o}} v ^ {\gamma} (h ^ {\dagger}) ^ {p} + (h ^ {\ddagger}) ^ {p}
$$

where

(1) v is a subsystem of a system of parameters z defining those components of Γ containing$\xi$

(2) The exponent$\gamma$is subject to$0 < \gamma _ { j } < q - 1$for every$j .$.

(3) o¨ is either 1 or zero. If it is one then we should let$u = 1$while if it is zero we should consider æ nonexistent.

(4) If$\ddot { o } = 1$then$( z , \mathrm { \alpha } \mathrm  { \alpha } \mathrm  { \alpha } \mathrm   \it { \alpha } \mathrm { { \it { \alpha } \mathrm { { \it { \alpha } \Lambda } \mathrm { { \it { \alpha } \Lambda } \mathrm { { \it { \alpha } \Lambda } \mathrm { { \it { \alpha } \Lambda } \mathrm { { \it { \alpha } \Lambda } \mathrm { { \it { \alpha } \Lambda } \mathrm { { \it { \Lambda \it { \alpha } \Lambda } \mathrm { { \it { \Lambda \it { \alpha } \Lambda } \mathrm { { \it { \Lambda \it { \alpha } \Lambda } \mathrm { { \it { \Lambda \it { \alpha } \Lambda } \mathrm { { \it { \Lambda \it { \Lambda } \it { \alpha } \Lambda } \mathrm { { \it { \Lambda \it { \Lambda } \it { \alpha } \Lambda } \mathrm { { \it { \Lambda \it { \Lambda } \it { \Lambda } \it { \alpha } \Lambda } \mathrm { { \it { \Lambda \it { \Lambda } \it { \Lambda } \it { \Lambda } \it { \Lambda } \mathrm { \it { \Lambda } \it { \Lambda } \it { \Lambda } \it { \Lambda } \it { \Lambda } \mathrm { \it { \Lambda } \it { \Lambda } \it { \Lambda } \it } } } } } } } } } } } } } } } } } } } } } } } } } } }$is extendable to a regualar system of parameters$x = ( z , \omega )$of$R _ { \xi }$. Indeed then æ$\in \omega$and it is Γ-transversal in the sense of Def.(14.1).

(5) If$\ddot { o } = 0$then$\gamma \not \equiv 0$mod p, i.e, we have$\gamma _ { j } \not \equiv 0$mod$p$for at least one$j .$. In all cases u must be a unit in$R _ { \xi }$

Remark 42.1. Let us recall the background from which our semistable exponent G of Def.(42.1) is brought up. We start with an ideal exponent$E = ( J , b )$with$o r d _ { \xi } ( J ) = b$and follow the strategy described in Rem.(41.9). We thus refer to its characteristic algebra$\wp ( E )$of$E$ by Th.(8.1) and apply the Edge Generators Theorem of Th.(10.1) to $E$Thereby we obtain a system of parameters$y = ( y _ { 1 } , \cdots , y _ { r } )$and a system of edge equations$g _ { i } = y _ { i } ^ { q _ { i } } + \epsilon _ { i }$with$q _ { i } = p ^ { e _ { i } } , 1 \leq i \leq r .$. They are arranged so as to have$0 \leq e _ { 1 } \leq \cdots \leq e _ { r }$. We have$o r d _ { \xi } ( \epsilon _ { i } ) > q _ { i }$and may assume that these$\epsilon _ { i } , \forall i$, are cleaned by those$g _ { j } , \forall j$, in the sense of Def.(??) according to Prop.(??) under the assumption that$( y , z )$is a subsystem of$x = ( z , \omega )$. In other words$y \subset \omega$. For this assumptin we should refer to Th.(??). Moreover the members of$y$are treated in a certain previlleged way diferent from the other members of$x \setminus y$ in resgards to their transformation by permissible blowups. For this matter we should refer to lemmas Lems.(11.3)-(11.7). Namely given a permissible blowup$\pi : Z ^ { \prime } \to Z$with center$D \ni \xi$and a closed point $\xi ^ { \prime } \in S i n g ( E ^ { \prime } ) \cap \pi ^ { - 1 } ( \xi )$, we may always choose an exceptional parameter z and the transforms$y ^ { \prime }$of$y$at$\xi ^ { \prime }$as follows:

$$
\mathfrak {z} \in \varpi = x \setminus y a n d \mathfrak {z} ^ {- 1} y _ {j} - y _ {j} ^ {\prime} = \eta_ {j} \in \mathbb {K}, \forall j\tag{42.1}
$$

provided that the edge invariants stays the same, i.e, Inv$\xi ^ { \prime } ( E ^ { \prime } ) =$ $\operatorname { I n v } _ { \xi } ( E )$where$E ^ { \prime }$denotes te transform of$E$by$\pi$.

Remark 42.2. Now with this background we define$\mathcal { G } = \left( h \parallel / \vphantom { h } ^ { q } \right)$with $h = \epsilon _ { 1 }$and$q = q _ { 1 }$. We then apply Th.(??) to the combination of$E$ and H in such a way to have the end that$\mathcal { G }$becomes semistable in the sense of Def.(42.1).

Remark 42.3. It should be noted that Eq.(42.1) is a partitioning of h into a non-p-power part and a p-power part. Our idea is that given an equation

$$
g = y ^ {q} - h = y ^ {q} - (\mathrm{e} ^ {\ddot {o}} v ^ {\gamma} (h ^ {\dagger}) ^ {p} + (h ^ {\ddagger}) ^ {p})\tag{42.2}
$$

with or$\cdot d _ { \xi } ( h ) > q$, we want to reduce the order of the ideal exponent $G = ( g \mathcal { O } _ { Z } , q )$down$\mathrm { t o } < q$by means of a finite sequence of blowups, permissible both for$G$as well as for the original ideal exponent$E$of Rem.(42.1). We then make use of an inductive hypothesis of the type of Def.(10.2) applied to$E \cap G _ { \ u { \mathrm { b } } }$where the ideal exponent$G _ { \flat }$is defined as follows:

$$
G _ {\flat} = \left(g _ {\flat}, q _ {\flat}\right) w i t h g _ {\flat} = y ^ {q _ {\flat}} - h ^ {\ddagger} a n d q _ {\flat} = q / p\tag{42.3}
$$

accompanied with

$$
g - (g _ {\flat}) ^ {p} = u \mathrm{e} ^ {\ddot {o}} v ^ {\gamma} (h ^ {\dagger}) ^ {p}\tag{42.4}
$$

which will be called the p-prime-summand of$g .$. We have the follwing inclusion relation between ideal exponents in the sense of infinitely near singularities.

$$
E \cap G _ {\flat} \subset G _ {\sharp} \text {where} G _ {\sharp} = (u \mathrm{e} ^ {\ddot {o}} v ^ {\gamma} (h ^ {\dagger}) ^ {p}, q)\tag{42.5}
$$

which implies that the inclusion of$G _ { \sharp }$does not change at all the problem of resolution of singularities of$E \cap G _ { \flat }$

Remark 42.4. The inductive hypothesis is clearly applicable to$E \cap G _ { \flat }$ because of$q _ { \flat } ~ < ~ q$Its use is made in choosing a finite sequence of proper sequence of blowups over$Z$which is permissible successively for the transforms of the given$E$and makes a fitted permissible Invsequence (edge invariants sequence) for$E \cap G _ { \ u { \mathrm { b } } }$in the sense of Def.(10.2). This is subject to the conditions of Def.(??) based on Eq.(??), Eq.(??) and$\operatorname { E q . } ( ? ? )$. The consequence of the inductive hypothesis is that the final transform of$E \cap G _ { \flat }$has the empty singular locus.

Remark 42.5. Let us examine what changes upon$E$and$G _ { \flat }$will result as a consequence of the application of the inductive hypothesis to$E \cap G _ { \flat }$ along the process of Def.(10.2) We will have either one of the following three results will be achieved.

(1) the transform$\tilde { E }$will have empty singular locus.

(2) there results an HIT-sequence by which the transform of$G _ { \flat }$ will have empty singular locus.

(3) The transform of the prime-summand of$g$will have metastic jump phenomena and hence the transform of$\mathcal { G }$will have a prime summand of monogenic factor.

Remark 42.6. For this end we will make use of a “trick” which will be called$/ ^ { q }$-genemarking

Definition 42.2. A general element$\chi \in \mathbb { K } ^ { * }$will be called a$/ ^ { q _ { - } }$ genemarker in its use of acting on an equation of the form Eq.(42.2) and change it to

$$
g = y ^ {q} - h = y ^ {q} - \left(\chi^ {- 1} \mathrm{e} ^ {\ddot {o}} v ^ {\gamma}\right) \left(\chi (h ^ {\dagger}) ^ {p}\right) + (h ^ {\ddagger}) ^ {p})
$$

This does not afect the equation$\operatorname { E q } .$.(42.3) while

From now on we assume that [¨o = 1 and$u = 1$in Def.(42.1) and hence in Eq.(42.4).

Assume that$q = p ^ { e } , e \geq 1$. We start from the point where we are given a p-monogenic semistable state of$\mathcal { G } = \left( h \| / \mathfrak { q } \right)$in which h is of the form$w h ^ { \dagger ^ { p } } + h ^ { \dagger ^ { p } }$which always becomes so whenever a mettastable transformation takes place after semistable state.

In such situation, we always modify w and$h ^ { \ddag ^ { p } }$as follows:

Write

$$
h ^ {\ddagger} = \lambda h ^ {\dagger} + \sigma
$$

where$\sigma$is cleaned by$h ^ { \dagger }$, We replace w by$w + \lambda .$

Assume that

(1) and we have regular system of parameters$x$of$Z$at$\xi$which is compatible with the given NC-data Γ in$Z$and w as one of its components. Hence$o r d _ { \xi } ( w ) = 1$

(2) We have$\mathcal { P } ^ { ( p ) } ( h ) = \rho ^ { e } ( h ^ { \dagger } \mathcal { O } _ { Z } )$so that

$$
D e r (\mathcal {G}) = \left(h ^ {\dagger^ {p}} \mathcal {O} _ {Z} \mid q\right) a t \xi
$$

(3) We have a single$\partial \in D e r _ { Z , \xi }$such that$\partial h = h ^ { \dagger ^ { p } } \in \rho ( R _ { \xi } )$

We obtain another idealistic exponent$H = ( \partial h , q - 1 )$such that

$$
\mathfrak {S} (H) \supset \mathfrak {S} (\mathcal {G})\tag{42.6}
$$

which means that

The resolution problem on$\mathcal { G }$is equivalent to that of H ∩

${ \mathcal { G } } .$Namely it is enough to solve the resolution problem

on$\mathcal { G }$under the condition with the same on$H$.

There our procedure is as follows:

(1) (Step 1)

We resolve the sigularities of H unless during the process the reduction of singularities of$E$happens in the sense of the edge invariants. In the end we reach the point of the semistable case in which$h ^ { \dagger }$is Γ-monomial at$\xi ,$say$z ^ { \beta }$, so that$h = w z ^ { p \beta } + h ^ { \ddagger ^ { p } }$ (2) Then we apply the resolution to the ideal$( z ^ { \beta } , h ^ { \ddagger } )$. The end result has two cases:

(a)$z ^ { \beta }$divides$h ^ { \ddag }$after the transformation.

(b)$h ^ { \ddag }$divides$z ^ { \beta }$so that$h ^ { \ddag }$is also Γ-monomial.

the first case is when we replace w by$w + ( z ^ { - \beta } h ^ { \ddag } )$. In the second case, after any additinal transformations, “spin-$. \mathrm { o f f s } ^ { , \dag }$of the first stable term$\stackrel { \cdot } { w } z ^ { p \beta }$will be added only as multiples of the monomial$h ^ { \ddag }$

## 43. Inductive Reduction on e of$q = p ^ { e }$

The resolution problem on the ideal exponent H is reduced to that of${ \cal F } ~ = ~ ( \partial h , q )$. To be precise, Eq.(42.6) implies

$$
\mathfrak {S} (F) \supset \mathfrak {S} (\mathcal {G})\tag{43.1}
$$

because as for any$q \mathrm { - t h }$power quantity its divisibility by a$( q - 1 )$)-th power$\mathfrak { h } ^ { q - 1 }$of an exceptional parameter y implies the divisibility by the q-the power$\mathfrak { p } ^ { q }$at every point of every step of any permissible sequence of blowups.

Next let us define the$\big / { } ^ { q ( 1 ) }$-exponent$G = \big ( h ^ { \ddag } \big \| \big / { } ^ { q ( 1 ) } \big )$which is clearly equivalent to the /<sup>q</sup>-exponent$\left( h ^ { \ddag ^ { q } } \parallel / ^ { q } \right)$. Therefore Eq.(43.1) implies

$$
\mathfrak {S} (F) \cap \mathfrak {S} (\mathcal {G}) = \mathfrak {S} (F) \cap \mathfrak {S} (\mathcal {G})\tag{43.2}
$$

Now we can appeal to the induction hypothesis on such exponents as${ \mathfrak { S } } ( { \mathcal { G } } )$of edge invariants with$q ( 1 ) = p ^ { - 1 } q = p ^ { e - 1 } < q$

Note :

(1) Have(1) Have$e = 1$is done, then induction assumption foris done, then induction assumption for$e { - } 1$, then work, then work with triplet of Γ-monomials:$\begin{array} { r } { A = u _ { 1 } z ( 1 ) ^ { \alpha ( 1 ) } w _ { 1 } ^ { o _ { i } } B = \sum _ { 2 \leq i \leq e } \Bigl ( u _ { i } z ( i ) ^ { \alpha ( i ) } w _ { i } ^ { o _ { i } } \Bigr ) ^ { p ^ { ( i - 1 ) } } } \end{array}$ $A ^ { o } = z ( 1 ) ^ { p \beta ( 1 ) }$where$\alpha ( 1 ) = p \beta ( 1 ) + \gamma ( 1 )$This$A ^ { o }$is a child of A and replaced each time by a bigger one. B and$A ^ { o }$have disjoint cofactors (after common factor taken) repeatedly apply ambient reduction for members of Γ.

(2) Let$k > 0$be the biggest integer such that$u _ { k } \neq 0$. Then the dubbed$/ ^ { q } { } .$-reduction will take care of the last q-factor$z ( k ) ^ { p \beta ( k ) }$

Theorem 43.1. Let$g , v ^ { \gamma }$and$\mathcal { G }$be the same as in$T h . ( 4 ^ { 3 . 1 ) }$. Assume that we have nonempty key q-parameters$\zeta$of$\mathcal { G }$at a closed point$\xi \in \mathbf { \Xi }$ $S i n g ( \mathcal { G } ) , i . e ,$the same ofg with respect to$v ^ { \gamma }$at$\xi$. Let π :$Z ^ { \prime } \longrightarrow Z$with center D and let$\mathcal { G } ^ { \prime }$be the same as in$T h . ( ? ? )$. Pick any$\xi ^ { \prime } \in \pi ^ { - 1 } ( \xi )$ and an exceptional parameter$\mathfrak { p } \in M _ { \xi }$at$\xi ^ { \prime }$. If we have

$$
d = \operatorname{ord} _ {\xi} (g) = \operatorname{resord} _ {\xi} (\mathcal {G}) \leq \operatorname{resord} _ {\xi^ {\prime}} \left(\mathcal {G} ^ {\prime}\right)\tag{43.3}
$$

then we have

(1)$\xi ^ { \prime }$is not metastable for π and resor$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) ~ = ~ d$

(2)$\mathfrak { p } ^ { - 1 } \zeta _ { j } \in R _ { \xi ^ { \prime } }$for all j$( \in M _ { \xi ^ { \prime } }$for all j when ∃i with$\mathfrak { \mathfrak { \mathrm { ? } } } ^ { - 1 } v _ { i } \in M _ { \xi ^ { \prime } }$ $T h . ( ? ? ) . )$

(3)$\mathfrak { p } ^ { - 1 } \zeta$are key q-parameters for$\mathcal { G } ^ { \prime }$at$\xi ^ { \prime }$

Next let us consider$\mathcal { G } = \left( z ^ { q \beta } v ^ { \gamma } f \parallel / { } / { } ^ { q } \right)$and a regular system of parameters$\boldsymbol { x } ~ = ~ ( v , w , \omega )$at$\xi$in the sense of$\operatorname { E q . } ( ? ? )$. We then have the q-cofactor cotangent module$L _ { q - m a x } ( \mathcal G ) ^ { c o f a } = L _ { q - m a x } ( v ^ { \gamma } )$and the cotangent p-flag$\{ L ( f , a ) , p ^ { e _ { a } } , 1 \leq a \leq l \}$associated with the residual $f \in M _ { \xi }$. (Refer to Th.(47.2).)

Theorem 43.2. Let us have$\mathcal { G }$and${ \boldsymbol { x } } = ( v , w , \omega )$as above. Let$\zeta$be key q-parameters of$\mathcal { G }$at$\xi$. Let$\pi : Z ^ { \prime } \longrightarrow Z$be a fitted permissible blowup for G and let$\xi ^ { \prime }$be a closed point of$\pi ^ { - 1 } ( \xi ) \cap S i n g ( \mathcal { G } ^ { \prime } )$where$\mathcal { G } ^ { \prime }$ denotes the transform of G by$\pi$.

## 44. e-reduction for$q = p ^ { e }$

In this section we assume that the base field K is a finite field of characteristic$p > 0$and the ambient scheme$Z$is smooth of finite type over$\mathbb { K }$. Let$\xi \in Z$be a closed point and take the local ring$R _ { \xi } = R _ { Z , \xi }$ at the point$\xi \in Z$. For simplicity sake we assume that$\xi$is K-rational throughout this section. If not we can always replace K by its suitable finite extension$\mathbb { K } ^ { \prime }$so as to make$\xi$to be K-rational. When we

Our primary object of study in this section is an equation of the following form:

$$
y ^ {q} + \sum_ {\gamma (i)} \phi_ {i} (x) ^ {q} z ^ {q \beta (i)} v (i) ^ {\gamma (i)}
$$

where

(1) With$\boldsymbol { z } = ( v ( i ) , w ( i ) )$for each$i , x = ( y , z , t )$is a regular system of parameters of$R _ { \xi }$where z is a system of variables defining those members of the NC-data Γ in$Z$

(2) Each$\gamma ( i )$is a system of integers none of whose components is divisible by$q$.

(3)$\phi _ { i } ( x ) \in R _ { \xi }$for every i.

## 45. /<sup>p</sup>-reduction

Immediately after a metastable jump, keep applying fitted permissible blowups until next drop of the residual order from$d + 1$to$d .$At the step just before this last blowup, let us use notational simplicity and say that our$/ ^ { p }$-exponent is written as

$$
\mathcal {G} = \left(z ^ {p \beta} v ^ {\gamma} f \| / ^ {p}\right)
$$

at our chosen closed point denoted by$\xi \in S i n g ( \mathcal { G } ) ) \subset Z$. As before we have

$$
\operatorname{resord} _ {\xi} (\mathcal {G}) = \operatorname{ord} _ {\xi} (f) = d + 1
$$

and let us take a system of p-cotangent parameters of$f$at$\xi$denoted by$\check { v }$. We may then assume that$i n _ { \xi } ( \check { v } _ { \flat } )$is a smallest system in terms of which$i n _ { \xi } ( f )$is expressible as a homogeneous polynomial of degree$d { + 1 }$ in$\mathbb { K } [ i n _ { \xi } ( \check { v } ) ]$. In order to investigate how the subsequent blowups afect the transforms of$\mathcal { G }$we consider the following three cases separately.

(1)$d + 1 \equiv$mod p

item d ≡ mod p

(2) none of the above two.

The system$\check { v } ( 1 )$contains at least one metastable parameter from the preceding metastable transform and possibly others of the NC-data. Let$\hat { v } ( 1 )$be a shortest system which augments to$\check { v } ( 1 )$so as to have the augmented system contains all the metastable parameters. Then we continue to perform fitted permissible blowups until the next metastable jump takes place. Just before this second jump, express the then$/ ^ { p } .$-exponent$\mathcal { G }$as being$\big ( z ^ { p \beta } v ^ { \gamma } f \big | \big | / { } ^ { p } \big )$at$\xi$and then decompose the residual factor$f = f _ { \sharp } + f _ { \flat }$in the following manner.

(1) the transform of ˇv(1) is extended to ˇv by adding exactly (minimal) those out of the transform of$\hat { v } ( 1 )$which are needed to contain the new cotangent module subject to be contained in the transform of$\check { v } ( 1 ) \cap \hat { v } ( 1 )$(and no new variables from outside.

(2)$\begin{array} { r } { f _ { \flat } \in \sum _ { \alpha \in \epsilon ^ { n } ( \flat ) } \rho ( R _ { \xi } ) \check { v } ^ { \alpha } } \end{array}$where ˇv denotes the appropriate transform of$\check { v } ( 1 )$(of the same length) and

(3)$f _ { \sharp }$has no monomial terms belonging to$\textstyle \sum _ { \alpha \in \epsilon ^ { n } ( p ) } \rho ( R _ { \xi } ) \breve { v } ^ { \alpha }$

Then examine the nature of the next metastable jump.

Divide the cases as:

(1) d + 1 ≡ mod$p$

(2) d ≡ mod$p$

(3) none of the above two.

## 46. Primary stability conditions

Let$\mathcal { G } = \left( z ^ { q \beta } v ^ { \gamma } f \lVert / ^ { q } \right)$with q-cofactor$v ^ { \gamma }$and with a residual factor$f$ in the sense of Def.(19.1) and Def.(19.3) at a closed point$\xi \in \ S i n g ( \mathcal { G } )$ We let resor$\begin{array} { r } { \mathbf { \nabla } \cdot d _ { \xi } ( \mathcal { G } ) = o r d _ { \xi } ( f ) = d . } \end{array}$. We have a regular system of parameters$x = ( z , \omega )$of$R _ { \xi }$with$z = ( v , w )$in the manner of Eq.(??).

Remark 46.1. Assume that we are given a member

Let us then define

$$
\mathcal {G} _ {i} = \left(z ^ {q \beta + \gamma} f _ {i} \| / ^ {q}\right) f o r i = 1, 2\tag{46.1}
$$

having the same q-factor and q-cofactor as$\mathcal { G }$.

(1) ord<sub>ξ</sub>(f<sub>1</sub>) = ord<sub>ξ</sub>(ζf<sub>2</sub>) = ord<sub>ξ</sub>(f) = resord<sub>ξ</sub>(G) = d

(2)$f _ { 1 }$is a residual factor of$\mathcal { G } _ { 1 }$

(3)$\zeta$is a member of a regular system of parameters x of$R _ { \xi }$and $i n _ { \xi } ( \zeta )$is not in the expression of$i n _ { \xi } ( f _ { 1 } )$in$\kappa _ { \xi } [ i n _ { \xi } ( x ) ]$

Take any fitted permissible blowup$\pi : Z ^ { \prime } \longrightarrow Z$with center$D$for both$\mathcal { G } _ { i } , i = 1 , 2$, and pick any closed point

$$
\xi^ {\prime} \in \pi^ {- 1} (\xi) \cap \bigcap_ {i = 1, 2} S i n g (\mathcal {G} _ {i} ^ {\prime})
$$

where$\mathcal { G } _ { i } ^ { \prime }$denotes the transform of$\mathcal { G } _ { i }$by$\pi$for each i.

Theorem 46.1. Under the conditions of Rem.$( 4 6 . 1 )$let us assume

$$
i n _ {\xi} (f _ {1}) \notin \rho^ {e} (g r _ {\xi} (R _ {\xi})) w h e r e q = p ^ {e}.\tag{46.2}
$$

Then for any π ofRem.$( 4 6 . 1 )$there cannot exist any$\xi ^ { \prime }$which is metastable of G provided that any one of the following conditions is satisfied:

(1)$\zeta \not \in L _ { q - m a x } ( \mathcal { G } ) ^ { c o f a }$

(2)${ \mathfrak { M } } ( { \mathcal { G } } _ { 1 } ) ~ = ~ \emptyset .$

(3)$\delta _ { v , \zeta } ^ { 0 } ( \zeta f _ { 2 } ) \ \ne \ 0 .$

(4)$i n _ { \xi } ( \zeta f _ { 2 } ) \notin \kappa _ { \xi } [ i n _ { \xi } ( x \setminus \zeta ) , i n _ { \xi } ( \zeta ) ^ { q } ]$

Theorem 46.2. If the primary m-scheme of$\mathcal { G }$at a closed point$\xi \in \mathbf { \Xi }$ $S i n g ( \mathcal { G } )$then there exists no metastable points appears unless once the residual order drops.

## 47. prime q-summands

Definition 47.1. With respect to a regular system of parameters x of $R _ { \xi }$, we consider subsystems$T = \left( T _ { 1 } , \cdots , T _ { \theta } \right)$and$U$of x and define a prime$T / q$-element of$R _ { \xi }$which means an element of

$$
\rho^ {e} (R _ {\xi}) \diamond (T)\tag{47.1}
$$

where${ \diamondsuit ( T ) }$is a$\mathbb { Z } ( p )$-linear combination of those monomials$\{ T ^ { a } | a \in$ $\epsilon ^ { \theta } ( q ) \}$

(1) When we have an addition of a new factor of the form$U ^ { \delta }$with another subsystem$U$of x which have no common components with$T$so that Eq.(47.1) becomes

$$
\rho^ {e} (R _ {\xi}) \diamond (T) U ^ {\delta}
$$

we factor$U ^ { \delta }$as$U ^ { q \beta } U ^ { \gamma }$where$0 < \gamma _ { j } < q , \forall j$, and add$U ^ { q \beta }$to $\rho ^ { e } ( R _ { \xi } )$and add$U ^ { \gamma }$to$\diamond ( T )$. We thus change it into the form of Eq.(47.1) again.

(2) When we have a translation of the form$T _ { i } \longrightarrow T _ { i } + c _ { i } T _ { \theta } , 1 \le$ $i \le \theta - 1$, with$c _ { i } \in \mathbb { K }$and eliminate q-th powers from Eq.(47.1) the result is again of the form Eq.(47.1).

Lemma 47.1. Assume that$\pi : Z ^ { \prime } \longrightarrow Z \ i s$fitted permissible for$\mathcal { G }$ and that$\xi ^ { \prime }$is a closed point of$\pi ^ { - 1 } ( \xi ) \cap S i n g ( \mathcal { G } ^ { \prime } )$, where$\mathcal { G } ^ { \prime }$denotes the transform of G by π. If resor$d _ { \xi ^ { \prime } } ( \mathcal { G } ^ { \prime } ) = r e s o r d _ { \xi } ( \mathcal { G } )$so that$\xi ^ { \prime }$is not metastable of G for π, at least one of the following is true:

(1)$\xi ^ { \prime }$is a metastable singular point of$\mathcal { G } ( d )$for π, while we have or$d _ { \xi ^ { \prime } } ( v _ { 1 } ^ { - d } f ^ { \sharp } ) = d$

(2) or$\cdot d _ { \xi ^ { \prime } } ( v _ { 1 } ^ { - d } f ^ { \sharp } ) \geq d$and no element of$R e s i _ { \xi , q } ( \mathcal { G } )$can be the initial of any exceptional parameter for π at$\xi ^ { \prime }$. In this case$\xi ^ { \prime }$is not metastable of$\mathcal { G } ( d ) ^ { \prime } ~ f o r ~ \pi$

Again going back to the general case of Eq.(21.1) and Eq.(21.2).

Definition 47.2. Given any element$g \ \in \ R _ { \xi }$, the largest member $L ( g , l )$of$\mathrm { E q . } ( 2 1 . 1 )$will be called the cotangent module of g or same of the ideal$g R _ { \xi }$. In dealing with the$/ ^ { q } .$-exponent$\mathcal { G } = \left( z ^ { q \beta } v ^ { \gamma } f \parallel / ^ { q } \right)$of Eq.(??), we have two important special applications of the notion of cotangent module. Namely one is the case when$g$is a nonzero element of$R _ { \xi }$such as the residual factor$f$of${ \mathcal { G } } .$and the other when$g$is a monomial of some chosen parameters in$R _ { \xi }$such as the$q \mathrm { . }$-cofactor$v ^ { \gamma }$ of$\mathcal { G }$in the sense of Def.(19.1). Let us consider the case in which$g$is a monomial$x ^ { A }$of a regular system of parameters x of$R _ { \xi }$. We then write $x ^ { A } = x ^ { q B } v ^ { C }$with a subsystem v of$x$in such a way that$0 < C _ { i } < q$for all$i ,$when$v ^ { C }$is called the$q \cdot$-cofactor of$x ^ { A }$in accord with Def.(19.1). Assuming that$C \neq 0$we have the cotangent module of$v ^ { C }$which is:

$$
L (x ^ {C}, l) = L (x ^ {C}, 1) = \sum_ {i} \kappa_ {\xi} i n _ {\xi} (v _ {i})
$$

In the case of monomial$x ^ { A }$as above, the cotangent module of$x ^ { C }$is will be called as q-cofactor cotangent module of$x ^ { \overset { \triangledown } { A } }$and moreover it will be given a special symbol$L ( x ^ { C } , \dag )$. Having$q$in mind, we will write $L ( x ^ { A } , \dag )$meaning$L ( x ^ { C } , \dag )$，

The notion and symbol will be extended to any$/ ^ { q } .$-exponent$\mathcal { G } =$ $\left( z ^ { q \beta } v ^ { \gamma } f \parallel / ^ { q } \right)$satisfying the conditions of Eq.(??). Namely the cotangent module of the monomial$v ^ { \gamma }$will be called the q-cofactor cotangent module of$\mathcal { G }$and it will be denoted by$L ( { \mathcal { G } } , { \dag } )$. Thus

$$
L (\mathcal {G}, \dagger) = L (v ^ {\gamma}, \dagger) = L (v ^ {\gamma}, l) = L (v ^ {\gamma}, 1) = \sum_ {1 \leq i \leq t} \kappa_ {\xi} i n _ {\xi} (v _ {i})
$$

with the q-cofactor$v ^ { \gamma }$of$\mathcal { G }$.

Note that the number e of$q = p ^ { e }$will play an important role in the following theorem.

Theorem 47.2. Let$\{ L ( a ) = L ( f , a ) , p ^ { e _ { a } } , 1 \leq a \leq l , \}$be the cotangent p-flag of Eq.(21.2) associated with the chosen residual factor f of G according to$E q . ( ? ? )$. Let$L ( \Psi ) = L ( \mathcal { G } , \dag )$be the p-cofacter cotangent module of G which is the cotangent p-module associated with the monomial factor$v ^ { \gamma }$in the sense of Def.(47.2). If there exists an integer $a , 1 \leq a < l ,$such that$1 \leq e _ { a } < e$and$L ( a ) \not \subset L ( \dagger )$then there exist no points in$\pi ^ { - 1 } ( \xi )$which are metastable for the transform$\mathcal { G } ^ { \prime }$of G by any fitted permissible blowup$\pi$

Note that the nonzero condition of$L ( g , a ) / ( L ( g , a ) \cap L ( v ^ { A } , \dagger ) )$for some a with$e _ { a } < e$plays the key role to the conclusion of the theorem. Refer to the notion of key q-parameters of Def.(??).

## 48. NC-dubbed /<sup>q</sup>-strategy

A Γ-pure blow-up over Z will mean a blow-up whose center is an intersection of some of the members of Γ. An ideal exponent$\boldsymbol { F } = ( I , \boldsymbol { c } )$ is called Γ-pure if the ideal I is generated by a Γ-monomial at every point of$S i n g ( F )$

Definition 48.1. A Γ-dubbed /<sup>q</sup>-exponent, say$\pmb { \mathfrak { F } } = ( F ; \mathcal { G } )$, is by definition a pair of Γ-pure F and a /<sup>q</sup>-exponent$\mathcal { G } = ( \mathbf { g } , / \mathfrak { q } )$

Let us write$\Gamma = \{ \Gamma _ { i } , 1 \leq i \leq t \}$

Definition 48.2. Given a Γ-dubbed$\mathfrak { F } = ( F ; \mathcal { G } )$we define that a bowup$\pi : Z ^ { \prime } \longrightarrow Z$with center$D \subset Z$is permissible for$\mathfrak { F }$if the following conditions are satisfied

(1) π is Γ-pure, i.e., there exists a subset d of$[ 1 , s ]$such that $D \ = \ \cap _ { i \in \mathbf { d } } \Gamma _ { j } , \neq \emptyset$, which will be denoted by$D ( \mathbf { d } )$, and

(2) π is permissible for both F and G.

Definition 48.3. Let$\pi : Z ^ { \prime } \longrightarrow Z , D \subset Z$, be permissible for F. Then we define the transform$\pmb { \mathfrak { F } } ^ { \prime } = ( E ^ { \prime } , \mathcal { G } ^ { \prime } )$of F by π to be the one having

(1) the transform$F ^ { \prime }$of F by π as ideal exponents, and

(2) the transform G′ of G by π in the sense of$/ { } ^ { q } \mathrm { - s y s t e m s }$

Definition 48.4. The singular locus is defined by

$$
\operatorname{Sing} (\mathfrak {F}) = \operatorname{Sing} (F) \cap \operatorname{Sing} (\mathcal {G})
$$

where$S i n g ( \mathcal { G } ) = \{ \eta \in Z \ | \ o r d _ { \eta } ( \mathbf { g } , / ^ { q } ) \geq q \}$

Remark 48.1. All in this section and the next are applicable to the case$\mathcal { G } \ = \ ( \ 0 \| \nearrow \ )$in which case all the arguments becomes much simpler. However, what is important in the simple case is the algorithm of resolution of singularities of Γ-monomial ideal exponent. This was used already in my old resolution paper 1964.

## 49. Comments on globalization

Immediately after a metastable jump has occurred at a closed point $\xi ^ { \prime } \in \pi ^ { - 1 } ( \xi ) \cap \mathop { S i n g } ( \mathcal G ^ { \prime } )$, the ambient reduction to any center$D ^ { \prime } \subset Z ^ { \prime }$ contained in$\{ v _ { 1 } = T _ { j } = 0 , \forall j \}$is idealistic because we have$f ^ { \prime } \in ( v _ { 1 } =$ $T _ { j } = 0 , \forall j ) R _ { \xi ^ { \prime } }$

The global resolution first of all requires a precise formulation of global induction which is not presented in this note. However this is much easier than the “local” work, which we explained how to carry out through in our program. In the positive characteristic case, the essential new dificulty is all “local”. But this term “local” means “open-local” in Zariski topology which is far stronger than “wedge-local (or micro-local)” which is meant in the so called “local” uniformization theorem. The “Zariski-open-local” processing was indeed the essence of our program we developed here.

## References

[1] Abhyankar, S., Local uniformization on algebraic surfaces over ground fields of chracteristic$p \neq 0$, Annals of Mathematics, 63 (1956), pp.491-526.

[2] Abhyankar, S., Resolution of singularities of embedded algebraic surfaces, Pure and Applied Mathematics, 24 (1966), Academic Press, New York.

[3]., Desingularization of plane curves, Summer Institute on Algebraic Geometry, Arcata 1981, Proc. Symp. Pure Appl. Math.40, AMS.

[4] Aroca, Jose M., Hironaka, H., Vicente, Jose L., Desingularization theorems, vol 30 (1977), Mem. de Math., Institut Jorge Juan, Madrid

[5] Abramovich, Dan, de Jong, A. J., Smoothness, semistability, and toroidal geometry, J. Algebraic Geom. 6 (1997), no. 4 , 789-801

[6] Abramovich, Dan, Wang, Jianhua, Equivariant resolution of singularities in characteristic 0, Math. Res. Lett. 4(1997), no.2-3, 427-433

[7] Bierstone, Ed., Milman, P. D., Uniformization of algebraic spaces, J. Amer. Math. Soc. 2 (1989), no.4, 801-836

[8] Bierstone, Ed., Milman, P. D., A simple constructive proof of canonical resolution of singularities, Efective methods in algebraic geometry, (Castiglioncello, 1990). Progr. Math., vol. 94, Birkhauser Boston, Boston, MA, (1991), 11-30

[9] Bierstone, Ed., Milman, P. D., Canonical desingularization in characteristic zero by blowing up the maximum strata of a local invariant, Inven. Math. 128 (1997), no.2, 207-302

[10] Bierstone, Ed., Milman, P. D., Desingularization algorithm.I. Role of exceptional divisors, Mosc. Math. J. 3 (2003), no.3, 751-805

[11] Cano, F.,Reduction of the singularities of codeimension one singular folitions in dimension three, Ann.of math, 160(2004), 907-1011

[12] Cossart, V., Polyhedre caracteristique d’une singularite, These d’Etat, Orsay 1987

[13] Cossart, V., Giraud, J., Orbanz, U., Resolution of surface singularities, Lecture Notes in Math. vol.1101, Springer 1984

[14] Cossart, V., Galindo C. et Piltant O. Un example efectif de gradue non noetherien associe a une valuation divisorielle, Ann. de l’Inst. Fourier, Grenoble, 50, 1(2000), 105-112

[15] Giraud, J., Sur la theorie du contact maximal, Math. Z. 137(1974), 286-310.

[16]Contact maximal en caracteristique positive, Ann. Scient. E.N.S.8 (1975), 201-234

[17] Hauser, H. Seventeen obstacles for resolution of singularities, in Singularities, Oberwolfach, 1996, 289-313, Progr.Math., 162, Birkhauser, Bazel

[18], The Hironaka theorem on resolution of singularities (or: A proof we always wanted to understand),Bull.Amer.Math.Soc. (N.S.) 40 (2003), no.3, 323-403 (electronic).

[19] Hironaka, H., Resolution of singularities of an algebraic variety over a field of characteristic zero, Ann. of Math. 79(1964) pp.109-326.

[20] , Gardening of infinitely near singularities, Proc. Nordic Summer School in Math., Oslo (1970) pp.315-332.

[21], Introduction to the theory of infinitely near singular points, Mem de Mat del Inst Jorge Juan, Madrid, 28 (1974)

[22], Idealistic exponents of singularity, Algebraic Geometry, Johns Hopkins Univ. Press, Baltimore, Md. (1977) pp. 52-125 ( J.J.Sylvester Symposium, Johns Hopkins Univ., 1976 )

[23] , Theory of infinitely near singular points, J. Korean Math.Soc. 40, no.5, pp. 901-920 (Sept.2003)

[24]Three key theorems on infinitely near singularities, Semi-naires&Congres 10, Soc.Math.France, pp. 871-126 (2005)

[25], A program for resolution of singularities, in all characteristics and in all dimensions, preprint for series of lectures in “Summer School on Resolution of Singularities” at Internatioanl Center for Theoretical Physics, Trieste, June 12-30, 2006

[26] J. de Jong, Smoothness, semi-stability and alterations, Publ.IHES 83 (1996), 51-93

[27] Kawanoue, Hiraku, Toward Resolution of Singularities over a field of Positive Characteristic Publ.RIMS, Kyoto Univ. 43 (2007), 819-909

[28] Kollar,Janos,Resolutionofsingularities-Seattlelecture, arXiv:math.AG/0508332 v1, 17 Aug 2005

[29] Moh, T.T. On a stability theorem for local uniformization in characteristic p, Journal of RIMS, 23 No.6,Nov.1987

[30] Moh, T.T. On a Newton Polygon approach to the uniformization of singularities of characteristic p, Algebraic Geometry and Singularities (eds. A. Campillo, L. Narvaez). Proc. Conf. on Singularities La Rabida. Birkhauser 1996

[31] Moh, T.T. Desingularization of three-varieties in positive characteristic, Progress in Mathematics 134, pp.49-93, (year?)

[32] Moh, T.T., Zhang,Y.T. On a local uniformization theorem for 3-fold in characteristic p > 0, Lecture Note (?)

[33] Youssin, Boris, Newton Polyhedra without coordinates, Mem. AMS 433(1990), 1-74, 75-99.

[34] Spivakovsky, Mark, A solution to Hironaka’s polyhedra game, Arithmetic and Geometry, Papers dedicated to I. R. Shafarevich on the occasion of his sixtieth birthday, vol.II, Birkhauser,1983, pp.419-432

[35] Spivakovsky, Mark, A counterexample to Hironaka’s ”hard polyhedra game, Publ. RIMS Kyoto University 18,3 (1982), 1009-1012

[36] Spivakovsky, Mark, A counterexample to the theorem of Beppo Levi in three dimensions, Invent. Math 96 (1989), 181-183

[37] Spivakovsky, Mark, Resolucion de singularidades y raices aproximadas de Tschirhausen, Notes by Fernando Sanz, Seminarios tematicos - Instituto de Estudios con Iberoamerica y Portugal, Seminario Iberoamericano de Matematicas IV (1997), 3-17

[38] Zariski, O., Local uniformization on algebraic varieties, Ann. of Math., 41(1940) pp.852-896.

[39], The reduction of singularities of an algebraic three dimensional varieties, Ann. of Math., 45 (1944) pp.472-542.