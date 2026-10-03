Monstrous moonshine and monstrous Lie superalgebras.

Invent. Math. 109, 405-444 (1992).

Richard E. Borcherds,

Department of pure mathematics and mathematical statistics, 16 Mill Lane, Cambridge CB2 1SB, England.

We prove Conway and Norton’s moonshine conjectures for the infinite dimensional representation of the monster simple group constructed by Frenkel, Lepowsky and Meurman. To do this we use the no-ghost theorem from string theory to construct a family of generalized Kac-Moody superalgebras of rank 2, which are closely related to the monster and several of the other sporadic simple groups. The denominator formulas of these superalgebras imply relations between the Thompson functions of elements of the monster (i.e. the traces of elements of the monster on Frenkel, Lepowsky, and Meurman’s representation), which are the replication formulas conjectured by Conway and Norton. These replication formulas are strong enough to verify that the Thompson functions have most of the “moonshine” properties conjectured by Conway and Norton, and in particular they are modular functions of genus 0. We also construct a second family of Kac-Moody superalgebras related to elements of Conway’s sporadic simple group $Co_1$. These superalgebras have even rank between 2 and 26; for example two of the Lie algebras we get have ranks 26 and 18, and one of the superalgebras has rank 10. The denominator formulas of these algebras give some new infinite product identities, in the same way that the denominator formulas of the affine Kac-Moody algebras give the Macdonald identities.

1 Introduction.

2 Introduction (continued).

3 Vertex algebras.

4 Generalized Kac-Moody algebras.

5 The no-ghost theorem.

6 Construction of the monster Lie algebra.

7 The simple roots of the monster Lie algebra.

8 The twisted denominator formula.

9 The moonshine conjectures.

10 The monstrous Lie superalgebras.

11 Some modular forms.

12 The fake monster Lie algebra.

13 The denominator formula for fake monster Lie algebras.

14 Examples of fake monster Lie algebras.

15 Open problems.

## 1 Introduction.

The main result of the first half of this paper is the following.

Theorem 1.1. Suppose that$V = \oplus _ { n \in \mathbf { Z } } V _ { n }$is the infinite dimensional graded representation of the monster simple group constructed by Frenkel, Lepowsky, and Meurman [16,17]. Then for any element g of the monster the Thompson series$\begin{array} { r } { T _ { g } ( q ) = \sum _ { n \in \mathbf { Z } } \mathrm { T r } ( g | V _ { n } ) q ^ { n } } \end{array}$is a Hauptmodul for a genus 0 subgroup of$S L _ { 2 } ( \mathbf { R } )$, i.e., V satisfies the main conjecture in Conway and Norton’s paper [13].

We prove this by constructing a$\mathbf { Z } ^ { 2 }$-graded Lie algebra acted on by the monster, called the monster Lie algebra. This is a generalized Kac-Moody algebra, and by calculating the “twisted denominator formulas” of this Lie algebra explicitly we get enough information about the Thompson series$T _ { g } ( q )$to determine them.

In this introduction we explain this result in more detail and briefly describe the proof, which is contained in sections 6 to 9. The rest of this paper is organized as follows. Section 2 is an introduction to the second half of the paper (sections 10 to 14) which uses some of the techniques of the proof to find some new infinite product formulas and infinite dimensional Lie algebras. Sections 3, 4, and 5 summarize some known results about vertex algebras, Kac-Moody algebras, and the no-ghost theorem that we use in the proof of theorem 1.1. Section 15 contains a list of some open questions. There is a list of notation we use at the end of section 1.

The Fischer-Griess monster sporadic simple group, of order$2^{46} 3^{20} 5 ^ { 9 } 7 ^ { 6 } 11^{2} 13^{3} 17.19.23.29.31.41.47.59.71$, acts naturally and explicitly on a graded real vector space$V = \oplus _ { n \in \mathbf { Z } } V _ { n }$constructed by Frenkel, Lepowsky and Meurman$[16,17]$(The vector spaces V and$V _ { n }$are denoted by$V ^ { \natural }$and$V _ { - n } ^ { \natural }$ in [16].) The dimension of$V _ { n }$is equal to the coefficient$c ( n )$of the elliptic modular function $\begin{array} { r } { j(\tau)-744 = \sum _ { n } c ( n ) q ^ { n } = q ^ { - 1 } + 196884 q + 21493760 q ^ { 2 } + \dots . } \end{array}$(where we write q for$e ^ { 2 \pi i \tau }$ and$\mathrm { I m } ( \tau ) > 0 )$. One of the main remaining problems from [16], which theorem 1.1 solves, is to calculate the character of$V$as a graded representation of the monster, or in other words to calculate the trace${ \mathrm { T r } } ( g | V _ { n } )$of each element$g$of the monster on each space$V _ { n }$. The best way to describe this information is to define the Thompson series

$$
T _ {g} (q) = \sum_ {n \in {\bf Z}} \mathrm{Tr} (g | V _ {n}) q ^ {n}
$$

for each element$g$of the monster, so we want to calculate these Thompson series. For example, if 1 is the identity element of the monster then$\operatorname { T r } ( 1 | V _ { n } ) = \dim ( V _ { n } ) = c ( n )$, so that the Thompson series$T _ { 1 } ( q ) = j(\tau)-744$is the elliptic modular function. McKay, Thompson, Conway and Norton conjectured [13] that the Thompson series$T _ { g } ( q )$are all Hauptmoduls for certain explicitly given modular groups of genus 0. (More precisely, they only conjectured that there should be some graded module for the monster whose Thompson series are Hauptmoduls, since their conjectures came before the construction of V.) This conjecture follows from theorem 1.1. The corresponding Hauptmoduls are the ones listed in [13] (with their constant terms removed), so this completely describes$V$as a representation of the monster.

We recall the definition of a Hauptmodul. The group$S L _ { 2 } ( \mathbf { Z } )$acts on the upper half plane$H = \{ \tau \in \mathbf { C } | \mathrm { I m } ( \tau ) > 0 \}$by$\begin{pmatrix}a&b\\c&d\end{pmatrix} ( \tau ) \ = \ { \frac { a \tau + b } { c \tau + d } }$. A meromorphic function on $H$invariant under$S L _ { 2 } ( \mathbf { Z } )$and satisfying a certain regularity condition at i∞ is called a modular function of level 1. The phrase “level 1” refers to the group$S L _ { 2 } ( \mathbf { Z } )$; if this is replaced by some commensurable group we get modular functions of higher levels. The elliptic modular function$j ( \tau )$is, up to normalizations, the simplest nonconstant modular function of level 1; more precisely, the modular functions of level 1 are the rational functions of$j$. The element$\begin{pmatrix}1&1\\0&1\end{pmatrix}$of$S L _ { 2 } ( \mathbf { Z } )$takes$\tau \mapsto \tau+1$, so in particular$j ( \tau )$is periodic and can be written as a Laurent series in$q = e ^ { 2 \pi i \tau }$. An exact expression for$j$is

$$
j (\tau) = \frac {(1+240 \sum_ {n > 0} \sigma_ {3} (n) q ^ {n}) ^ {3}}{q \prod_ {n > 0} (1 - q ^ {n}) ^ {24}}
$$

where$\begin{array} { r } { \sigma _ { 3 } ( n ) = \sum _ { d \mid n } d ^ { 3 } } \end{array}$is the sum of the cubes of the divisors of$n ;$see any book on modular forms or elliptic functions, for example [30]. Another way of thinking about$j$is that it is an isomorphism from the quotient space${ H } / { S L _ { 2 } ( \mathbf { Z } ) }$to the complex plane, which can be thought of as the Riemann sphere minus the point at infinity.

We can also consider functions invariant under some group$G$commensurable with $S L _ { 2 } ( \mathbf { Z } )$acting on$H$. The quotient$H / G$is again a compact Riemann surface$\overline { { H / G } }$with a finite number of points removed. If this compact Riemann surface is a sphere, rather than something of higher genus, then we say that G is a genus 0 group. In this case a function giving an isomorphism from the compact Riemann surface$\overline { { H / G } }$to the sphere $\mathbf { C } \cup \infty$taking i∞ to$\infty$is called a Hauptmodul for the genus 0 group G; it is unique up to addition of a constant and multiplication by a nonzero constant. If a Hauptmodul can be written as$e ^ { - 2 \pi i a \tau } +a$ function vanishing at i∞ for some positive a then we say that it is normalized. Every genus 0 group has a unique normalized Hauptmodul. For example, $j(\tau)-744=e^{-2\pi i\tau}+0+196884e^{2\pi i\tau}+\cdots$ is the normalized Hauptmodul for the genus 0 group$S L _ { 2 } ( \mathbf { Z } )$.

Another example is$G = \Gamma _ { 0 } ( 2 )$, where$\Gamma _ { 0 } ( N ) = \{ { \textstyle \begin{pmatrix}a&b\\c&d\end{pmatrix} } \in S L _ { 2 } ( \mathbf { Z } ) | c \equiv 0$mod$N \}$. The quotient$H / G$is then a sphere with 2 points removed, so that$G$is a genus 0 group. Its normalized Hauptmodul is$\begin{array} { r } { T _ { 2 - } ( q ) = 24+q ^ { - 1 } \prod _ { n > 0 } ( 1 - q ^ { 2 n + 1 } ) ^{24} = q ^ { - 1 } + 276q - 2048q ^ { 2 } + . . . , } \end{array}$ and is equal to the Thompson series of a certain element of the monster of order$2$(of type 2B in atlas [14] notation). Similarly$\Gamma _ { 0 } ( N )$is a genus 0 subgroup for several other values of N which correspond to elements of the monster. (However the genus of$\Gamma _ { 0 } ( N )$tends to infinity as N increases, so there are only a finite number of integers N for which it has genus 0; more generally Thompson [31] has shown that there are only a finite number of conjugacy classes of genus 0 subgroups of$S L _ { 2 } ( \mathbf { R } )$which are commensurable with$S L _ { 2 } ( \mathbf { Z } ) . )$

So we want to calculate the Thompson series$T _ { g } ( \tau )$and show that they are Hauptmoduls of genus 0 subgroups of$S L _ { 2 } ( \mathbf { R } )$.The difficulty with doing this is as follows. Frenkel, Lepowsky, and Meurman constructed V as the sum of two subspaces$V ^ { + }$and$V ^ { - } ,$ which are the$+ 1$and −1 eigenspaces of a certain element of order$2$in the monster. If an element$g$of the monster commutes with this element of order 2, then it is not difficult to to work out its Thompson series$\begin{array} { r } { T _ { g } ( q ) = \sum _ { n } \mathrm { T r } ( g | V _ { n } ) q ^ { n } } \end{array}$as the sum of two series given by its traces on$V ^ { + }$and$V ^ { - }$(this is done in$[16,17] )$, and it would probably be tedious but straightforward to check directly that these are all Hauptmoduls. Unfortunately, if an element of the monster is not conjugate to something that commutes with this element of order 2 then there is no obvious direct way of working out its Thompson series, because it muddles up$V ^ { + }$and$V ^ { - }$in a very complicated way.

We calculate these Thompson series indirectly using the monster Lie algebra M. This is a$\mathbf { Z } ^ { 2 } = \mathbf { Z } \oplus \mathbf { Z }$graded Lie algebra, whose piece of degree$( m , n ) \in { \bf Z } ^ { 2 }$is isomorphic as a module over the monster to$V _ { m n } \mathrm { ~ i f ~ } ( m , n ) \neq ( 0 , 0 )$and to$\mathbf { R } ^ { 2 } \mathrm { ~ i f ~ } ( m , n ) = ( 0 , 0 )$, so for small

$$
\begin{array}{c c c c c c c c c} & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ \dots & 0 & 0 & 0 & 0 & V _ {3} & V _ {6} & V _ {9} & \dots \\ \dots & 0 & 0 & 0 & 0 & V _ {2} & V _ {4} & V _ {6} & \dots \\ \dots & 0 & 0 & V _ {- 1} & 0 & V _ {1} & V _ {2} & V _ {3} & \dots \\ \dots & 0 & 0 & 0 & {\bf R} ^ {2} & 0 & 0 & 0 & \dots . \\ \dots & V _ {3} & V _ {2} & V _ {1} & 0 & V _ {- 1} & 0 & 0 & \dots \\ \dots & V _ {6} & V _ {4} & V _ {2} & 0 & 0 & 0 & 0 & \dots \\ \dots & V _ {9} & V _ {6} & V _ {3} & 0 & 0 & 0 & 0 & \dots \\ & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \end{array}
$$

Very briefly, this Lie algebra is constructed as the space of physical states of a bosonic string moving in a $\mathbf{Z}_2$-orbifold of a 26-dimensional torus (or strictly speaking, about half the physical states). See section 6 for more details. The space of physical states is a subquotient of a vertex algebra constructed from the vertex algebra$V ;$vertex algebras are described in more detail in [3,16,18], and the properties we use are summarized in section 3. This subquotient can be identified using the no-ghost theorem from string theory ([21] or section 5), and is as described above.

We need to know what the structure of the monster Lie algebra is. It turns out to be something called a generalized Kac-Moody algebra, so we explain what these are.

Section 4 describes the results about generalized Kac-Moody algebras that we use. This paragraph gives a brief summary of them. Kac-Moody algebras can be thought of as Lie algebras generated by a copy of$sl_2$ for each point in their Dynkin diagram. Generalized Kac-Moody algebras are rather like Kac-Moody algebras except that we are allowed to glue together the$sl_2’s$in more complicated ways, and are also allowed to use Heisenberg Lie algebras as well as$sl_2’s$to generate the algebra. The main difference between Kac-Moody algebras and generalized Kac-Moody algebras is that the roots α of a Kac-Moody algebra may be either real$( ( \alpha , \alpha ) > 0 )$or imaginary$( ( \alpha , \alpha ) \leq 0 )$but all the simple roots must be real, while generalized Kac-Moody algebras may also have imaginary simple roots. Kac-Moody algebras have a “denominator formula”, which says that a product over positive roots is equal to a sum over the Weyl group; for example, the denominator formula for the affine Kac-Moody algebra$sl_2( \mathbf { R } [ z , z ^ { - 1 } ] )$is the Jacobi triple product identity. Generalized Kac-Moody algebras have a denominator formula which is similar to the one for Kac-Moody algebras, except that it has some extra correction terms for the imaginary simple roots. (The simple roots of a generalized Kac-Moody algebra correspond to a minimal set of generators for the subalgebra corresponding to the positive roots. For Kac-Moody algebras the simple roots also correspond to the points of the Dynkin diagram and to the generators of the Weyl group.)

We return to the monster Lie algebra. This is a generalized Kac-Moody algebra, and we will now write down its denominator formula, which says that a product over the positive roots is a sum over the Weyl group. The positive roots are the vectors$( m , n )$with m$> 0 , n > 0$, and the vector$( 1 , - 1 )$, and the root$( m , n )$has multiplicity c(mn). The Weyl group has order 2 and its nontrivial element maps (m, n) to$( n , m )$, so it exchanges $p = e ^ { ( 1 , 0 ) }$and$q = e ^ { ( 0 , 1 ) }$. The denominator formula for the monster Lie algebra is the product formula for the$j$function

$$
p ^ {- 1} \prod_ {m > 0, n \in Z} (1 - p ^ {m} q ^ {n}) ^ {c (m n)} = j (p) - j (q).
$$

(The left side is antisymmetric in$p$and$q$because of the factor of$p ^ { - 1 } ( 1 - p ^ { 1 } q ^ { - 1 } )$in the product.) The reason why we get$j ( p )$and$j ( q )$rather than monomials in$p$and$q$on the right hand side (as we would for ordinary Kac-Moody algebras) is because of the correction due to the imaginary simple roots of $M$. The simple roots of $M$ correspond to a set of generators of the subalgebra$E$of the elements of M whose degree is to the right of the y axis (so the roots of$E$are the positive roots of$M )$, and turn out to be the vectors$( 1 , n )$ each with multiplicity$c ( n )$. In the picture of the monster Lie algebra given earlier, the simple roots are given by the column just to the right of the one containing$\mathbf { R } ^ { 2 }$. The sum of the simple root spaces is isomorphic to the space $V$. The simple root$( 1 , - 1 )$is real of norm $2 ,$and the simple roots$( 1 , n )$for$n > 0$are imaginary of norm$- 2 n$and have multiplicity $c ( n ) = \dim ( V _ { n } )$. As these multiplicities are exactly the coefficients of the$j$function, it is not surprising that$j$appears in the correction caused by the imaginary simple roots. This discussion is slightly misleading because we have implied that we obtain the product formula of the$j$function as the denominator formula of the monster Lie algebra by using our knowledge of the simple roots; in fact we really have to use this argument in reverse, using the product formula for the$j$function in order to work out what the simple roots of the monster Lie algebra are. We do this in section 7.

We can now extract information about the coefficients of the Thompson series$T _ { g } ( \tau )$ from a twisted denominator formula for the monster Lie algebra as follows: for an arbitrary generalized Kac-Moody algebra there is a more general version of the Weyl denominator formula which states that

$$
\Lambda (E) = H (E),
$$

where $E$ is the subalgebra corresponding to the positive roots. Here $\Lambda(E)=\Lambda^0(E)\ominus\Lambda^1(E)\oplus\Lambda^2(E)\cdots$ is a virtual vector space which is the alternating sum of the exterior powers of $E$, and similarly $H(E)$ is the alternating sum of the homology groups $H_i(E)$ of the Lie algebra $E$ (see [10]). This identity is true for any finite dimensional Lie algebra $E$ because the $H_i(E)$'s are the homology groups of a complex whose terms are the $\Lambda^i(E)$'s. The left hand side corresponds to a product over the positive roots because $\Lambda(A\oplus B)=\Lambda(A)\otimes\Lambda(B)$, $\Lambda(A)=1-A$ if $A$ is one dimensional, and $E$ is the sum of $\operatorname{mult}(\alpha)$ one dimensional spaces for each positive root $\alpha$. For infinite dimensional Lie algebras $E$ we need to be careful that the infinite dimensional virtual vector spaces $H(E)$ and $\Lambda(E)$ are well defined; in this paper they are always differences of graded vector spaces with finite dimensional homogeneous pieces and so are well defined. It is more difficult to identify $H(E)$ with a sum over the Weyl group, and we do this roughly as follows. For Kac-Moody algebras $H_i(E)$ turns out to have dimension equal to the number of elements in the Weyl group of length $i$; for finite dimensional Lie algebras this was first observed by Bott, and was used by Kostant [26] to give a homological proof of the Weyl character formula. The sum over the homology groups can therefore be identified with a sum over the Weyl group.

For Kac-Moody algebras the same is true and was proved by Garland and Lepowsky [20]. For generalized Kac-Moody algebras things are a bit more complicated. The sum over the homology groups can still be identified with a sum over the Weyl group, but the things we sum are more complicated and contain terms corresponding to the imaginary simple roots.

We can work out the homology groups of $E$ explicitly provided we know the simple roots of our Lie algebra $M$; for example, the first homology group $H_1(E)$ is the sum of the simple root spaces. For the monster Lie algebra, we have worked out the simple roots using its denominator formula, the product formula for $j$. In section 8, we use this to work out the homology groups of $E$. They are $H_0(E)=\mathbf{R}$, $H_1(E)=\sum_{n\in\mathbf{Z}}V_npq^n$, $H_2(E)=\sum_{m>0}V_mp^{m+1}$, and all higher homology groups are 0. Each homology group is a $\mathbf{Z}^2$-graded representation of the monster, and we use the $p$'s and $q$'s to keep track of the grading. Substituting these values into $\Lambda(E)=H(E)$ gives

$$
\Lambda (\sum_ {n \in {\bf Z}, m > 0} V _ {m n} p ^ {m} q ^ {n}) = \sum_ {m} V _ {m} p ^ {m + 1} - \sum_ {n} V _ {n} p q ^ {n}.
$$

Both sides of this are virtual graded representations of the monster. If we replace everything by its dimension we recover the product formula for the$j$function. More generally, we can take the trace of some element of the monster on both sides, which after some calculation gives the identity

$$
p ^ {- 1} \exp \Bigl (- \sum_ {i > 0} \sum_ {m > 0, n \in {\bf Z}} \mathrm{Tr} (g ^ {i} | V _ {m n}) p ^ {m i} q ^ {n i} / i \Bigr) = \sum_ {m \in {\bf Z}} \mathrm{Tr} (g | V _ {m}) p ^ {m} - \sum_ {n \in {\bf Z}} \mathrm{Tr} (g | V _ {n}) q ^ {n}
$$

where${ \mathrm { T r } } ( g | V _ { n } )$is the trace of$g$on the vector space$V _ { n }$

These relations between the coefficients${ \mathrm { T r } } ( g | V _ { n } )$of the Thompson series are strong enough to determine them from their first few coefficients. Norton and Koike checked that certain modular functions of genus 0 also satisfy the same recursion relations, so we can prove that the Thompson series$T _ { g } ( q )$are these modular functions of genus 0 by checking that the first few coefficients of both functions are the same. Unfortunately this final step of the proof (in section 9) is a case by case check that the first few coefficients are the same. Norton has conjectured [28] that Hauptmoduls with integer coefficients are essentially the same as functions satisfying relations similar to the ones above, and a conceptual proof or explanation of this would be a big improvement to the final step of the proof. (It should be possible to prove Norton’s conjecture by a very long and tedious case by case check, because all functions which are either Hauptmoduls or which satisfy the relations above can be listed explicitly. In [1] the authors use a computer to find all “completely replicable” functions with integer coefficients, and they all appear to be Hauptmoduls. Roughly half of them correspond to conjugacy classes of the monster.)

I thank J. McKay, U. Tillman, J. Lepowsky, and the referee, each of whom sent me many useful remarks about a draft of this paper.

Notation. (In roughly alphabetical order.)

C The complex numbers.

c(n) are the coefficients of the elliptic modular function$j ( q ) - 744$(defined below).

$c _ { g } ( n ) = \operatorname { T r } ( g | V _ { n } )$is the n’th coefficient of the Thompson series$T _ { g } ( q )$of $g$.

$\Gamma _ { 0 } ( N )$is the subgroup of matrices${ \begin{pmatrix}a&b\\c&d\end{pmatrix} }$in$S L _ { 2 } ( \mathbf { Z } )$with$N | c ,$and $\Gamma_0(N)^+$ is its normalizer in$S L _ { 2 } ( \mathbf { R } )$; see [13].

$\delta_i^j$ is the Kronecker delta function, equal to 1 if $i=j$ and 0 otherwise.

$\Delta ( q )$is the Dedekind delta function$\begin{array} { r } { q \prod _ { n > 0 } ( 1 - q ^ { n } ) ^{24} = \eta ( q ) ^{24} } \end{array}$

E The subalgebra of a generalized Kac-Moody algebra$G = F \oplus H \oplus E$ spanned by the positive root spaces.

$E_8$ is the unique 8-dimensional positive-definite even unimodular lattice.

ε(α) is the coefficient associated with the root α in the denominator formula of a generalized Kac-Moody algebra. See section 4.

η(q) is the Dedekind eta function$q ^ { 1/24 } \prod _ { n > 0 } ( 1 - q ^ { n } )$. For$\eta _ { g }$see sections 9 or 13, and for $\eta _ { + } , \eta _ { - }$see section 11.

$\theta_\Lambda(q)=\sum_{\lambda\in\Lambda}q^{\lambda^2/2}=1+196560q^2+\cdots$ is the theta function of the Leech lattice Λ. For other theta functions see section 11.

G A generalized Kac-Moody algebra; see section 4.

H The Cartan subalgebra of a generalized Kac-Moody algebra$G = F \oplus H \oplus E$

$H _ { i } ( E )$is a homology group of the Lie algebra$E ; H ( E )$is the alternating sum of the homology groups of E.

$II_{1,1}$ is the unique even 2-dimensional unimodular Lorentzian lattice, with inner product matrix $\begin{pmatrix}0&-1\\-1&0\end{pmatrix}$. Its elements are usually represented as pairs $(m,n)\in\mathbf{Z}^2=\mathbf{Z}\oplus\mathbf{Z}$, with norm $-2mn$.

$II_{25,1}$ is the unique even 26-dimensional unimodular Lorentzian lattice, isomorphic to $\Lambda\oplus II_{1,1}$.

$j(q)$ is the elliptic modular function with $j(q)-744=q^{-1}+196884q+\cdots=\theta_\Lambda(q)/\Delta(q)-24=\sum_n c(n)q^n$.

Λ is the Leech lattice, the unique 24-dimensional even unimodular positive-definite lattice with no vectors of norm 2. Its elements are denoted by λ. Its double cover $\hat{\Lambda}$ is defined in section 12.

Λ(E) is the alternating sum of the exterior powers of the vector space E.

$\Lambda ^ { i } ( E )$is the i’th exterior power of the vector space E.

$M=\bigoplus_{m,n\in\mathbf{Z}}M_{m,n}$ is the monster Lie algebra with root lattice $II_{1,1}$, constructed in section 6.

$M _ { \Lambda }$is the fake monster Lie algebra, whose root lattice is$I I _ { 25 , 1 }$

$\mu(d)$ is the Moebius function: it equals $(-1)^k$ if $d$ is square free, where $k$ is the number of prime factors of $d$, and 0 otherwise.

mult(r) The multiplicity of the root r.

$p$ is a formal variable. It can usually be considered as a complex number with $|p|<1$. The number $p_{24}(n)$ is the number of partitions of $n$ into parts of 24 colours, so that $\sum_n p_{24}(1+n)q^n=q^{-1}\prod_{n>0}(1-q^n)^{-24}=\Delta(q)^{-1}=q^{-1}+24+324q+3200q^2+25650q^3+176256q^4+1073720q^5+\cdots$. These are the multiplicities of roots of the fake monster Lie algebra $M_\Lambda$. For $p_g$ see section 14.

$q$ is a formal variable. It can usually be thought of as a complex number with $|q|<1$, equal to $e^{2\pi i\tau}$ (i.e., the formal series usually converge for $|q|<1$).

$r ^ { 2 }$The norm (r, r) of the vector r of some lattice.

R The real numbers.

$\rho$ is the Weyl vector of a root lattice, defined by $(\rho,r)=-(r,r)/2$ for every simple root $r$. (This is the opposite sign from the usual definition.) The Weyl vector is not necessarily in the root lattice, although it is for most of the Lie algebras in this paper. This convention and the corresponding Weyl chamber are explained in section 4. For the fake monster Lie algebra, whose root lattice is $II_{25,1}=\Lambda\oplus II_{1,1}=\Lambda\oplus\mathbf{Z}^2$, $\rho$ is the vector $(0,0,1)$.

$\begin{array} { r } { \sigma _ { i } ( n ) = \sum _ { d \mid n } d ^ { i } } \end{array}$is the sum of the i’th powers of the divisors of $n$.

$T_g(q)=\sum_{n\in\mathbf{Z}}c_g(n)q^n$ is the Thompson series of an element $g$ of the monster, with $c_g(n)=\operatorname{Tr}(g|V_n)$, where $V=\bigoplus_{n\in\mathbf{Z}}V_n$ is the module constructed by Frenkel, Lepowsky and Meurman [16,17]. (The spaces $V$ and $V_n$ are denoted by $V^\natural$ and $V_{-n}^\natural$ in [16].)

$\operatorname { T r } ( g | U )$is the trace of an endomorphism g of a vector space$U$

$\tau$ is a complex number with $\operatorname{Im}(\tau)>0$.

$V = \oplus _ { n \in \mathbf { Z } } V _ { n }$is the monster vertex algebra discussed in section 3.

$V _ { I I _ { 1 , 1 } }$is the vertex algebra of the two dimensional even Lorentzian lattice$I I _ { 1 , 1 }$(or more precisely the vertex algebra of its double cover).

$V_\Lambda$ is the fake monster vertex algebra, the vertex algebra of the Leech lattice $\Lambda$ (more precisely, of its double cover $\hat{\Lambda}$). See section 12.

W is a Weyl group. Typical elements are often denoted by w. See section 4.

Z The integers.

$\psi^i$ is an Adams operation on virtual group representations, defined by $\operatorname{Tr}(g|\psi^i(V))=\operatorname{Tr}(g^i|V)$ for a virtual representation $V$ of a group containing $g$.

ω A Cartan involution (section 4) or a conformal vector of a vertex algebra (section 3).

## 2 Introduction (continued).

We describe the results in the second half of the paper (sections 10 to 14). This section can be omitted by those who are only interested in the proof of theorem 1.1.

We construct several Lie superalgebras which are similar to the monster Lie algebra. One method of constructing these is to consider the “twisted” denominator formulas of the monster Lie algebra as untwisted denominator formulas of some other Lie algebras or superalgebras; these seem to be related to other sporadic simple groups. A second method of constructing some of them is to replace the monster vertex algebra V by the vertex algebra of the Leech lattice$V _ { \Lambda }$. From this we get the fake monster Lie algebra [8] (where it is called the monster Lie algebra) and several variations of it.

The Lie superalgebras we construct form two families as follows:

(1) A Lie algebra or superalgebra of rank 2 for many conjugacy classes g of the monster simple group. The monster Lie algebra is the one corresponding to the identity element of the monster. The ones corresponding to other elements of the monster are often related to other sporadic simple groups.

(2) A Lie superalgebra for many conjugacy classes of the group $\operatorname{Aut}(\hat{\Lambda})=2^{24}.2.Co_1$, where $\hat{\Lambda}$ is the standard double cover of the Leech lattice $\Lambda$ (defined in section 12), and $\operatorname{Aut}(\hat{\Lambda})$ is the group of its automorphisms which preserve the inner product on $\Lambda$. The group $Co_1=\operatorname{Aut}(\Lambda)/\mathbf{Z}_2$ is one of Conway’s sporadic simple groups. (The symbol A.B, where A and B are groups, stands for an extension of B by A, i.e., a group with normal subgroup A such that the quotient by A is B; the notation is ambiguous.) For example, we get Lie algebras of ranks 26, 18, and 14 corresponding to certain automorphisms of $\hat{\Lambda}$ of orders 1, 2, and 3, and a Lie superalgebra of rank 10 corresponding to an automorphism of order 2. The Lie algebra of rank 26 is what we now call the fake monster Lie algebra and is studied in [8] (where it is called the monster Lie algebra, because the genuine monster Lie algebra had not been discovered then).

All of these algebras are generalized Kac-Moody algebras or superalgebras. Their root multiplicities can be described explicitly in terms of the coefficients of a finite number of modular forms of weight at most 0. (These modular forms are holomorphic on the upper half plane, and are meromorphic but not necessarily holomorphic at the cusps.) More precisely, there is a sublattice L of finite index in the root lattice, and for each coset of L in the root lattice there is a modular form, which is holomorphic except at the cusps and of weight $1-\dim(L)/2$, such that the root multiplicity of a vector r in a given coset is the coefficient of$q ^ { - ( r , r ) / 2 }$of the corresponding modular form. All the algebras have Weyl vectors$\rho$with norm$\rho ^ { 2 } = ( \rho , \rho ) = 0$, and the simple roots are the roots r with $( r , \rho ) = - ( r , r ) / 2$. In particular the simple roots and root multiplicities can be described explicitly, and we use this to obtain some infinite product identities from the denominator formulas of these algebras. These algebras are closely related to the sporadic simple groups.

We now discuss both of these families of Lie algebras in more detail. We recall from section 1 that the monster Lie algebra M, is a generalized Kac-Moody algebra whose denominator formula is

$$
p^{-1}\prod_{\substack{m > 0\\ n\in \mathbf{Z}}}(1 - p^{m}q^{n})^{c(mn)} = j(p) - j(q).\tag{2.1}
$$

In section 10 we construct a similar Lie superalgebra for many elements g of the monster. In this case the denominator formula is

$$
p^{-1}\prod_{\substack{m > 0\\ n\in \mathbf{Z}}}(1 - p^{m}q^{n})^{\mathrm{mult}(m,n)} = T_{g}(p) - T_{g}(q)\tag{2.2}
$$

where $T_g(q)=\sum_n c_g(n)q^n=\sum_n\operatorname{Tr}(g|V_n)q^n$ is the Thompson series of $g$. For example, $T_1(q)+744$ is the elliptic modular function $j(q)$. The function $T_g(q)$ is the normalized generator for the genus-zero function field of a group containing $\Gamma_0(nh)$, where $n$ is the order of $g$ and $h$ is an integer with $h|(24,n)$.

$$
\mathrm{mult} (m, n) = \sum_ {d s | (m, n)} \mu (d) \mathrm{Tr} (g ^ {s} | V _ {m n / d ^ {2} s ^ {2}}) / d s\tag{2.3}
$$

where $\mu(d)$ is the Moebius function, equal to $(-1)^k$ if $d$ is square free, where $k$ is the number of prime factors of $d$, and 0 otherwise. (The symbol $(m,n)$ under the summation sign means the greatest common divisor of $m$ and $n$, rather than the ordered pair.) For example, if $N$ is a square-free integer such that the full normalizer $\Gamma_0(N)^+$ of $\Gamma_0(N)$ has genus 0, then a special case of (2.2) is

$$
p^{-1}\prod_{\substack{m > 0\\ n\in \mathbf{Z}}}\prod_{d|(m,n,N)}(1 - p^{m}q^{n})^{c_{N}(mn / d)} = T_{N}(p) - T_{N}(q)\tag{2.4}
$$

where$\begin{array} { r } { T _ { N } ( q ) = \sum _ { n } c _ { N } ( n ) q ^ { n } } \end{array}$is the normalized generator of the function field of $\Gamma_0(N)^+$ with leading terms$q ^ { - 1 } + 0 + c _ { N } ( 1 ) q + . . .$

In section 11 to 14 we construct a second series of Lie superalgebras, which are similar to the algebras above except that they are related to the vertex algebra$V _ { \Lambda }$of the Leech lattice Λ instead of the monster vertex algebra V. The largest of these, which plays the same role for this series as the monster Lie algebra plays for the previous series, is the algebra which used to be called the monster Lie algebra in [8] and is now called the fake monster Lie algebra. (The Kac-Moody algebra whose Dynkin diagram is that of the reflection group of$I I _ { 25 , 1 }$has also been called the monster Lie algebra$( [ 7 ] )$; it is a large subalgebra of the fake monster Lie algebra, and does not seem to be interesting, except as an approximation to the fake monster Lie algebra.) The root lattice of the fake monster Lie algebra is the 26 dimensional even unimodular Lorentzian lattice$I I _ { 25 , 1 }$, and its denominator formula is

$$
e ^ {\rho} \prod_ {r \in \Pi^ {+}} (1 - e ^ {r}) ^ {p_{24} (1 - r ^ {2} / 2)} = \sum_ {w \in W} \det (w) w (e ^ {\rho} \prod_ {n > 0} (1 - e ^ {n \rho}) ^{24}).
$$

Here$\rho$is a norm 0 Weyl vector for the reflection group W of$I I _ { 25 , 1 } , \Pi ^ { + }$is the set of positive roots, which is the set of vectors r of norm at most 2 which are either positive multiples of $\rho$ or have negative inner product with $\rho$, $p_{24} ( 1 - r ^ { 2 } / 2 )$is the multiplicity of the root r and is equal to the number of partitions of the integer$1 - ( r , r ) / 2$into parts of 24 colours, and the simple roots are the norm $2$ vectors r with$( r , \rho ) = -1$ together with 24 copies of each positive multiple of $\rho$. This Lie algebra was first constructed in [3], and the properties stated above were proved in [8]; this construction depended heavily on the ideas in Frenkel [15].

The fake monster Lie algebra is acted on by the group$2^{24}\cdot2\cdot Co_1$in the same way that the monster Lie algebra is acted on by the monster group, and we construct a superalgebra for many elements of$2^{24}\cdot2\cdot Co_1$from the fake monster Lie algebra in the same way that we construct a superalgebra for every element of the monster from the monster Lie algebra. Some of the more interesting algebras we get in this way are a fake baby monster algebra of rank 18, a fake $Fi_{24}$ Lie algebra of rank 14 associated with Fischer’s sporadic simple group $Fi_{24}$, a fake $Co_1$ superalgebra of rank 10 associated with Conway’s sporadic simple group $Co_1$, and several Lie algebras of smaller rank corresponding to some of the other sporadic simple groups involved in the monster.

The superalgebra of rank 10 is particularly interesting, so we describe it explicitly. It is the superalgebra associated with an element g of$\operatorname { A u t } ( \hat { \Lambda } )$which has order 2 and fixes an 8-dimensional sublattice of Λ, isomorphic to the lattice$E _ { 8 }$with all norms doubled. Its root lattice$L$is the dual of the sublattice of even vectors of$I _ { 9 , 1 }$, so that$L$is a nonintegral lattice of determinant$1 / 4$all of whose vectors have integral norm. We represent vectors of L as triples$( v , m , n )$, where$v \in E _ { 8 }$and$m , n \in \mathbf { Z }$, and$( v , m , n )$has norm $v^2-2mn$. The lattice$I _ { 9 , 1 }$is then the set of vectors$( v , m , n )$with m + n even. We let$\rho$be the norm 0 vector$( 0 , 0 , 1 )$. We let the Weyl group W be the subgroup of$\operatorname { A u t } ( L )$generated by the reflections of norm 1 vectors, so that the simple roots of$W$are the norm 1 vectors r with $( r , \rho ) = - 1 / 2$. (Note that W is not the full reflection group of$L ,$as L also has roots of norm 2.)

The simple roots of our superalgebra are the simple roots of $W$, together with the positive multiples$n \rho \ ( n > 0 )$of$\rho$, each with multiplicity$8 ( - 1 ) ^ { n }$. Here we use the convention that multiplicity$- k < 0$means a superroot of multiplicity k, so that the odd multiples of$\rho$ are superroots. In general the vector$( v , m , n )$is an ordinary root or a superroot depending on whether$m + n$is even or odd, so the ordinary roots are those in the sublattice$I _ { 9 , 1 }$of $L$

The multiplicity of the root$r = ( v , m , n ) \in L$is equal to

$$
\mathrm{mult} (r) = (- 1) ^ {(m - 1) (n - 1)} p _ {g} ((1 - r ^ {2}) / 2) = (- 1) ^ {m + n} | p _ {g} ((1 - r ^ {2}) / 2) |,
$$

where$p _ { g } ( n )$is defined by

$$
\sum p _ {g} (n) q ^ {n} = q ^ {- 1 / 2} \prod_ {n > 0} (1 - q ^ {n / 2}) ^ {- (- 1) ^ {n} 8}
$$

and as before negative multiplicity means a superroot. The denominator formula for this Lie superalgebra is

$$
e ^ {\rho} \prod_ {r \in \Pi^ {+}} (1 - e ^ {r}) ^ {\mathrm{mult} (r)} = \sum_ {w \in W} \det (w) w (e ^ {\rho} \prod_ {n > 0} (1 - e ^ {n \rho}) ^ {(- 1) ^ {n} 8}).
$$

Similarly the denominator formula for the fake baby monster Lie algebra of rank 18 is

$$
e ^ {\rho} \prod_ {r \in L ^ {+}} (1 - e ^ {r}) ^ {p _ {g} (1 - r ^ {2} / 2)} \prod_ {r \in 2 L ^ {\prime +}} (1 - e ^ {r}) ^ {p _ {g} (1 - r ^ {2} / 4)} = \sum_ {w \in W} \det (w) w (e ^ {\rho} \prod_ {i > 0} (1 - e ^ {i \rho}) ^ {8} (1 - e ^ {2 i \rho}) ^ {8})
$$

where L is the Lorentzian lattice which is the sum of the 16-dimensional Barnes-Wall lattice$\Lambda _ { 2 } [12]$and the two dimensional even Lorentzian lattice$I I _ { 1 , 1 }$, W is its reflection group which has Weyl vector$\rho , L ^ { \prime }$is the dual of L and$p _ { g }$is defined by$\begin{array} { r } { \sum _ { n } p _ { g } ( n ) q ^ { n } = } \end{array}$ $\textstyle { \prod _ { n > 0 } ( 1 - q ^ { n } ) ^ { - 8 } ( 1 - q ^ { 2 n } ) ^ { - 8 } }$. This Lie algebra is associated with an element$g$of order 2 of $\operatorname { A u t } ( \hat { \Lambda } )$which fixes a 16-dimensional lattice of Λ isomorphic to the Barnes-Wall lattice.

There are similar Lie superalgebras associated with many other elements of$\operatorname { A u t } ( \hat { \Lambda } )$, which have denominator formulas similar to those above.

## 3 Vertex algebras.

We give a brief summary of the facts about vertex algebras that we use and list the properties of the monster vertex algebra that we need. For more information about vertex algebras, see [3], [9], [16], or [18]; the last two references contain proofs of the results quoted here.

A vertex algebra over the real numbers (which is the only case we use in this paper) is a vector space V over the real numbers with an infinite number of bilinear products, written$u _ { n } v$for$u , v \in V , n \in { \bf Z }$, such that

(1)$u _ { n } v = 0$for n sufficiently large (depending on u and v).

$$
\sum_ {i \in {\bf Z}} {\binom {m} {i}} (u _ {q + i} v) _ {m + n - i} w = \sum_ {i \in {\bf Z}} (- 1) ^ {i} {\binom {q} {i}} (u _ {m + q - i} (v _ {n + i} w) - (- 1) ^ {q} v _ {n + q - i} (u _ {m + i} w))\tag{2}
$$

for all $u,v,w\in V$ and all integers $m,n,q$.

(3) There is an element $\mathbf{1}\in V$ such that $v_n\mathbf{1}=0$ if $n\geq0$ and $v_{-1}\mathbf{1}=v$.

We often think of $u_n$ as a linear map from $V$ to $V$, taking $v$ to $u_nv$. In [16,18], these operators are combined into the “vertex operator” $V(u,z)=\sum_{n\in\mathbf{Z}}u_nz^{-n-1}$, an operator-valued formal Laurent series in $z$.

For example, if$V$is a commutative algebra over R with derivation D then we can make it into a vertex algebra by defining$u _ { n } v$to be$D ^ { - n - 1 } ( u ) v / ( - n - 1 ) !$for$n < 0$and 0 for $n \geq 0$, and conversely any vertex algebra over R for which$u _ { n } v = 0$whenever$n \geq 0$arises from a commutative algebra in this way. These are the only finite dimensional examples of vertex algebras, and seem to be the only examples which are easy to construct. The vertex algebras we use here do not have this property and are much harder to construct; for example the detailed construction of the monster vertex algebra in [16] takes up most of a rather long book. Fortunately the details of this construction are not important for this paper, so at the end of this section we list the properties of it that we need.

We define the operator D of a vertex algebra by$D ( v ) = v _ { - 2 } 1$. (In [16] and [18] D is denoted by$L _ { - 1 } . )$The vector space$V / D V$is a Lie algebra, where the bracket is defined by$[ u , v ] = u _ { 0 } v$and$D V$is the image of V under D.

There is a vertex algebra$V _ { L }$associated with any even lattice L (or more precisely with a certain central extension $\hat{L}$ of L by a group of order 2), which is constructed in [3]. The underlying vector space of this vertex algebra is the tensor product of the twisted group ring$Q ( \hat { L } )$of the double cover$\hat { L }$of L (see section 12) and the ring of polynomials $S ( \oplus _ { i > 0 } L _ { i } )$over the sum of an infinite number of copies$L _ { i }$of$L \otimes \mathbf { R }$. We often use the vertex algebra$V _ { I I _ { 1 , 1 } }$of the 2-dimensional even unimodular Lorentzian lattice$I I _ { 1 , 1 }$. There is also a monster vertex algebra $V$ [3,16] which is acted on naturally by the monster sporadic simple group. (The referee has asked me to explain why I have never published my (long and messy) proof of the assertion in [3] that the module V constructed in [17] has the structure of a vertex algebra. The reason is that my proof used many results from the announcement [17], and the only published proof of this announcement, given in the book [16], incorporates the fact that V is a vertex algebra.) The underlying vector space of the monster vertex algebra is a graded vector space$V = \oplus _ { n \in \mathbf { Z } } V _ { n }$, with homogeneous pieces of dimensions 1, 0, 196884, ... equal to the coefficients of the elliptic modular function $j(q)-744$

A conformal vector of dimension (or “central charge”) $c\in\mathbf{R}$ of a vertex algebra $V$ is an element $\omega\in V$ such that $\omega_0v=D(v)$ for any $v\in V$, $\omega_1\omega=2\omega$, $\omega_3\omega=c/2$, $\omega_i\omega=0$ if $i=2$ or $i>3$, and any element of $V$ is a sum of eigenvectors of $L_0=\omega_1$ with integral eigenvalues. If $v$ is an eigenvector of $L_0$, its eigenvalue is called its (conformal) weight. If $v$ has conformal weight $n$ in the monster vertex algebra $V$, we sometimes say it has degree $n-1 (=n-c/24)$.

The vertex algebra of any c-dimensional even lattice has a canonical conformal vector of dimension$c ,$and the monster vertex algebra has a conformal vector of dimension 24. If ω is a conformal vector of a vertex algebra V then we define operators$L _ { i }$on V for$i \in \mathbf { Z }$ by

$$
L _ {i} = \omega_ {i + 1}.
$$

These operators satisfy the relations

$$
[ L _ {i}, L _ {j} ] = (i - j) L _ {i + j} + \binom {i + 1} {3} \frac {c}{2} \delta_ {- j} ^ {i}
$$

and so make$V$into a module over the Virasoro algebra. The operator$L _ { - 1 }$is equal to $D$. We define the space$P ^ { i }$to be the space of vectors$w \in V$such that$L _ { 0 } ( w ) = i w , L _ { i } ( w ) = 0$ if$i > 0$. The space$P ^ { 1 } / ( D V \cap P ^ { 1 } )$is a subalgebra of the Lie algebra$V / D V$, which is equal to$P ^ { 1 } / D P ^ { 0 }$for the vertex algebras we use in this paper.

The vertex algebra of any even lattice and the monster vertex algebra both have a real valued symmetric bilinear form$( , )$such that the adjoint of the operator$u _ { n }$is $\begin{array} { r } { ( - 1 ) ^ { i } \sum _ { j \geq 0 } L _ { 1 } ^ { j } ( \omega ( u ) ) _ { 2 i - j - n - 2 } / j ! } \end{array}$if u has degree i, where ω is the automorphism of the vertex algebra defined by$\omega ( e ^ { w } ) = ( - 1 ) ^ { ( w , w ) / 2 } ( e ^ { w } ) ^ { - 1 }$for$e ^ { w }$an element of the twisted group ring of L corresponding to the vector$w \in L$, or is 1 in the case of the monster vertex algebra. (There is an unfortunate clash of notation here, because$\omega$is the standard notation for both the conformal vector and the Cartan automorphism of a Lie algebra. If L is the root lattice of a finite dimensional Lie algebra of type$A _ { n } , D _ { n } , E _ { 6 } , E _ { 7 }$, or$E _ { 8 }$then the Lie algebra is a subalgebra of the vertex algebra of$L$and the involution ω defined above restricts to the Cartan automorphism of the Lie algebra.) If a vertex algebra has a bilinear form with the properties above we say that the bilinear form is compatible with the conformal vector.

Frenkel, Lepowsky, and Meurman [16] use “vertex operator algebras”, rather than vertex algebras, so we explain what the difference is. A vertex operator algebra is a vertex algebra with a conformal vector such that the eigenspaces of$L _ { 0 }$are all finite dimensional with nonnegative integral eigenvalues. For example, the monster vertex algebra is a vertex operator algebra. (Its conformal vector spans the subspace of$V _ { 1 }$fixed by the monster.) The vertex algebras used in this paper all have conformal vectors but the eigenspaces of$L _ { 0 }$ are not always finite dimensional. An example of a vertex algebra without these properties is the vertex algebra$V _ { I I _ { 1 , 1 } }$of the 2-dimensional even unimodular Lorentzian lattice$I I _ { 1 , 1 }$

If V and$W$are vertex algebras, then their tensor product$V \otimes W$as vector spaces is also a vertex algebra, if$( a \otimes b ) _ { n } ( c \otimes d )$is defined to be$\begin{array} { r } { \sum _ { i \in { \bf Z } } ( a _ { i } c ) \otimes ( b _ { n - 1 - i } d ) } \end{array}$and the identity 1 is defined to be$1\otimes1$ (see [18]). If V and W have conformal vectors $\omega_V$ and $\omega_W$ of dimensions $m$ and $n$ then$\omega _ { V } \otimes 1 + 1 \otimes \omega _ { W }$is a conformal vector of$V \otimes W$of dimension $m + n$. If V and$W$have bilinear forms compatible with the conformal vectors then so does$V \otimes W ;$in fact the obvious bilinear form on the tensor product will do.

The monster vertex algebra V [3, 16] is a vertex algebra acted on by the monster. The construction given in [16] is rather long, but fortunately we do not need to know many details of its construction. We list the three properties of it we do use, in case anyone finds a simpler construction of it that they wish to prove also satisfies Conway and Norton’s moonshine conjectures.

(1) V is a vertex algebra over R with a conformal vector ω of dimension 24 and a positive definite bilinear form such that the adjoint of$u _ { n }$is given by the expression above (with the automorphism$\omega$acting trivially).

(2) $V$ is a sum of eigenspaces $V_i$ of the operator $L_0$, where $L_0$ has eigenvalue $i+1$ on $V_i$, and $\sum_i\dim(V_i)q^i=j(q)-744=q^{-1}+196884q+\cdots$.

These two conditions turn out to imply that if$g$is any automorphism of V preserving the vertex algebra structure, the conformal vector and the bilinear form then$\sum \mathrm { T r } ( g | V _ { i } ) q ^ { i }$ is a completely replicable function (which means that identity (8.3) holds).

(3) The monster simple group acts on V, preserving the vertex algebra structure, the conformal vector ω and the bilinear form. The first few representations$V _ { i }$of the monster (after$V _ { - 1 } = \chi _ { 1 } , \ V _ { 0 } = 0 )$decompose as$V _ { 1 } = \chi _ { 1 } + \chi _ { 2 } , V _ { 2 } = \chi _ { 1 } + \chi _ { 2 } + \chi _ { 3 } ,$ $V _ { 3 } = 2 \chi _ { 1 } + 2 \chi _ { 2 } + \chi _ { 3 } + \chi _ { 4 } , V _ { 5 } = 4 \chi _ { 1 } + 5 \chi _ { 2 } + 3 \chi _ { 3 } + 2 \chi _ { 4 } + \chi _ { 5 } + \chi _ { 6 } + \chi _ { 7 }$where$\chi _ { i } , 1 \leq i \leq 7$ are the first seven irreducible representations of the monster, indexed in order of increasing dimension.

The construction of the vector space V and the action of the monster on it, preserving a small part of the vertex algebra structure, were announced in [17], and the vertex algebra structure was announced in [3]. The results quoted above have all been proved in [16] and [18], apart from the explicit description of the representations in (3). We show in section 9 that condition (3) can be proved using the explicit description in [16] of the traces of certain elements of the monster acting on V. In the course of proving theorem 1.1 we show that these three conditions characterize V as a graded representation of the monster.

## 4 Generalized Kac-Moody algebras

We summarize the results about generalized Kac-Moody algebras that we use, which can be found in [4], [5], [20], and the third edition of Kac’s book [23]. We modify the original definition of generalized Kac-Moody algebras in [4] slightly so that these algebras are closed under taking universal central extensions, as in [5]. (This is not necessary for the proof of theorem 1.1, but makes the converse to theorem 4.1 slightly neater.) All Lie algebras are Lie algebras over the reals.

A Lie algebra G is defined to be a (split) generalized Kac-Moody algebra if it has an almost positive definite contravariant bilinear form, which means that G has the following three properties.

1. G can be Z-graded as$G = \oplus _ { i \in \mathbf { Z } } G _ { i }$and$G _ { i }$is finite dimensional if$i \neq 0$

2. G has an involution ω which maps$G _ { i }$into$G _ { - i }$and acts as −1 on$G _ { 0 }$, so in particular $G _ { 0 }$is abelian.

3. G has an invariant bilinear form $(\ ,\ )$ invariant under $\omega$ such that $G_i$ and $G_j$ are orthogonal if $i\neq -j$, and such that $-(g,\omega(g))>0$ if $g$ is a nonzero homogeneous element of $G$ of nonzero degree.

The bilinear form$( , ) _ { 0 }$defined by$( a , b ) _ { 0 } = - ( a , \omega ( b ) )$is called the contravariant bilinear form of$G ,$and is positive definite on$G _ { i } { \mathrm { ~ i f ~ } } i \neq 0$. For example any finite dimensional split semisimple Lie algebra over the reals has these properties, with ω equal to a Cartan involution,$( , )$equal to the Killing form, and the grading determined by the eigenvalues of some suitably normalized regular element. (If the contravariant bilinear form on G is positive semidefinite, then G is essentially a sum of affine, Heisenberg, and finite dimensional simple split Lie algebras.) In general the contravariant form can be indefinite on $G _ { 0 }$. For the algebras we use in this paper the subalgebra$G _ { 0 }$has a vector such that the contravariant form is positive semidefinite on its orthogonal complement.

Suppose that$a _ { i j } , i , j \in I$is a symmetric countable (possibly infinite) real matrix such that$a _ { i j } \leq 0 { \mathrm { ~ i f ~ } } i \neq j$and such that if$a _ { i i } > 0$then$2 a _ { i j } / a _ { i i }$is an integer for any $j$. Then the universal generalized Kac-Moody algebra G of this matrix is defined to be the Lie algebra generated by elements$e _ { i } , f _ { i } , h _ { i j }$for$i , j \in I$satisfying the following relations. (It is true but not obvious that any universal generalized Kac-Moody algebra is a generalized Kac-Moody algebra; this fact is not needed in this paper.)

1.$[ e _ { i } , f _ { j } ] = h _ { i j }$

2. [h<sub>ij</sub> , e<sub>k</sub>] = δ<sup>j</sup><sub>i</sub> a<sub>ik</sub>e<sub>k</sub>, [h<sub>ij</sub> , f<sub>k</sub>] = −δ<sup>j</sup><sub>i</sub> a<sub>ik</sub>f<sub>k</sub>

3. If$a _ { i i } > 0$and$i \neq j \mathrm { ~ t h e n ~ a d } ( e _ { i } ) ^ { n } e _ { j } = \mathrm { a d } ( f _ { i } ) ^ { n } f _ { j } = 0 ,$, where$n = 1 - 2 a _ { i j } / a _ { i i }$

4. If$a _ { i i } \leq 0 , a _ { j j } \leq 0$and$a _ { i j } = 0$then$[ e _ { i } , e _ { j } ] = [ f _ { i } , f _ { j } ] =0$.

We often write$h _ { i }$for$h _ { i i }$. There is a unique invariant bilinear form on this algebra such that$( e _ { i } , f _ { j } ) = \delta _ { i } ^ { j }$; this implies that$( h _ { i } , h _ { j } ) = a _ { i j }$

Remark. If$a _ { i i } > 0$for all$i \in I$then this algebra is the same as the Kac-Moody algebra with symmetrized Cartan matrix$a _ { i j }$. In general these algebras have almost all the properties that Kac-Moody algebras have, and the only major difference is that generalized Kac-Moody algebras are allowed to have imaginary simple roots.

The main theorem about generalized Kac-Moody algebras [4,5] says that they can all be obtained from universal generalized Kac-Moody algebras.

Theorem 4.1. Suppose that G is a generalized Kac-Moody algebra with some given grading, involution ω and bilinear form$( , )$. Then there is a unique universal generalized Kac-Moody algebra, graded by putting deg$( e _ { i } ) = - \deg ( f _ { i } ) = n _ { i }$for some positive integers $n _ { i } ,$with a homomorphism f (not necessarily unique) to G such that

(1) f preserves the gradings, involutions and bilinear forms (where the universal generalized Kac-Moody algebra is given the grading, involution and bilinear form defined above).

(2) The kernel of f is in the centre of the universal generalized Kac-Moody algebra (which is contained in the abelian subalgebra spanned by the elements$h _ { i j } )$

(3) The image of $f$ is an ideal of $G$, and $G$ is the semidirect product of this subalgebra and a subalgebra of the abelian subalgebra$G _ { 0 }$. Moreover the images of all the generators $e _ { i }$and$f _ { i }$are eigenvectors of$G _ { 0 }$

Remark. The converse of this theorem is also true (but not needed here): any universal generalized Kac-Moody algebra with a countable number of simple roots is a generalized Kac-Moody algebra. (The proof of this converse in$[ 4 ]$contains a gap which was pointed out and corrected by Kac in [23].) Theorem 4.1 says that we can construct any generalized

Kac-Moody algebra from some universal generalized Kac-Moody algebra by factoring out some of the centre and adding a commuting algebra of outer derivations.

We list some of the properties of universal generalized Kac-Moody algebras G from [4] and [5], many of which are also proved in the third edition of [23].

(1) The element$h _ { i j }$is 0 unless the$i ^ { \prime }$th and$j ^ { \prime }$’th columns of a are equal. The elements $h _ { i j }$for which the i’th and j’th columns of a are equal form a basis for an abelian subalgebra H of$G ,$called its Cartan subalgebra. In the case of Kac-Moody algebras, the i’th and j’th columns of a cannot be equal unless$i = j ,$so the only nonzero elements$h _ { i j }$are those of the form$h _ { i i }$, which are usually denoted by$h _ { i }$. Every nonzero ideal of G has nonzero intersection with H. The centre of G is contained in H and contains all the elements$h _ { i j }$ for$i \neq j$

(2) The root lattice is defined to be the free abelian group generated by elements$r _ { i }$ for $i\in I$, with the bilinear form given by$( r _ { i } , r _ { j } ) = a _ { i j }$. The elements$r _ { i }$are called the simple roots. The universal generalized Kac-Moody algebra is graded by the root lattice if we let$e _ { i }$have degree$r _ { i }$and$f _ { i }$have degree$- r _ { i }$. There is a natural homomorphism of abelian groups from the root lattice to the Cartan subalgebra H taking$r _ { i }$to$h _ { i }$which preserves the bilinear forms. If$r$is in the root lattice then the vector space of elements of the Lie algebra of that degree is called the root space of$r ;$if r is nonzero and has a nonzero root space then$r$is called a root of the generalized Kac-Moody algebra. A root $r$is called positive if it is a sum of simple roots, and negative otherwise. It is called real if it has positive norm$( r , r )$and imaginary otherwise.

(3) The Weyl vector$\rho$is the additive map from the root lattice to R taking$r _ { i }$to $- ( r _ { i } , r _ { i } ) / 2$for all$i \in I$. (This is the opposite sign from the usual definition.) We write its value on a root r as$( \rho , r )$. The fundamental Weyl chamber (which we call the Weyl chamber for short, because it is the only one we use) is the set of vectors v of the Cartan subalgebra H with$( v , r _ { i } ) \leq 0$for all real simple roots$\boldsymbol { r } _ { i } ,$where we identify real simple roots with their images in$H$. (There is a misprint in the definition of Weyl chamber in [4]; the word “real” in “real simple roots” was omitted.)

Remark. The reason why we use nonstandard sign conventions for the Weyl vector and Weyl chamber is that we are using the convention that “everything should be in the Weyl chamber if possible”. We want the imaginary simple roots to be in the Weyl chamber which forces us to use the opposite Weyl chamber from usual; similarly we change the sign of the Weyl vector to get it (or rather its image in H, when this exists) in the Weyl chamber, and we use lowest weight modules (rather than highest weight modules) because their lowest weights are in the Weyl chamber. For most of the generalized Kac-Moody algebras in this paper the Cartan subalgebra has a Lorentzian bilinear form, so that the vectors of norm at most 0 form two solid cones; our sign conventions usually make all the interesting vectors of norm at most 0 lie in the same solid cone.

(4) If a has no zero columns then$G$is perfect and equal to its own universal central extension. If a is not the direct sum of two smaller matrices, not the$1 \times 1$zero matrix, and not the matrix of an affine Kac-Moody algebra, then G modulo its centre is simple.

(5) Suppose we choose a positive integer $n_i$ for each $i\in I$. Then we can grade $G$ by $\deg(e_i)=-\deg(f_i)=n_i$. The degree-0 piece of $G$ is the Cartan subalgebra $H$.

(6) G has an involution ω with$\omega ( e _ { i } ) = - f _ { i } , \omega ( f _ { i } ) = - e _ { i }$, called the Cartan involution.

There is a unique invariant bilinear form$( , )$on$G$such that$( e _ { i } , f _ { i } ) = 1$for all$i ,$and it also has the property that −$( g , \omega ( g ) ) > 0$whenever$g$is a homogeneous element of nonzero degree. In particular the universal generalized Kac-Moody algebra of any matrix as above is a generalized Kac-Moody algebra.

(7) There is a character formula for the simple lowest weight module$M _ { \lambda }$of$G$with a lowest weight λ in the real vector space of the root lattice such that$( \lambda , r _ { i } ) \leq 0$for$i \in I$ and$2 ( \lambda , r _ { i } ) / ( r _ { i } , r _ { i } )$is integral if the simple root$r _ { i }$is real. This states that

$$
\operatorname{ch}(M_\lambda) e ^ {\rho} \prod_ {\alpha > 0} (1 - e ^ {\alpha}) ^ {\mathrm{mult} (\alpha)} = \sum_ {w \in W} \det (w) w (e ^ {\rho} \sum_ {\alpha} \epsilon (\alpha) e ^ {\alpha + \lambda})
$$

The only case of this we need is for the trivial one dimensional module with$\lambda = 0$, when it becomes the denominator formula

$$
e ^ {\rho} \prod_ {\alpha > 0} (1 - e ^ {\alpha}) ^ {\mathrm{mult} (\alpha)} = \sum_ {w \in W} \det (w) w (e ^ {\rho} \sum_ {\alpha} \epsilon (\alpha) e ^ {\alpha})
$$

Here$\rho$is the Weyl vector,$\alpha > 0$means α is a positive root, and$W$is the Weyl group, which is the group of isometries of the root lattice generated by the reflections corresponding to the real simple roots. If$w \in W$then det$( w )$is defined to be$+ 1 \ \mathrm { o r \ - 1 }$ depending on whether w is the product of an even or odd number of reflections; if the root lattice is finite dimensional this is just the usual determinant of w acting on it. We define $\epsilon ( \alpha )$for$\alpha$in the root lattice to be$( - 1 ) ^ { n }$if α is the sum of a set of n pairwise orthogonal imaginary simple roots that are all orthogonal to$\lambda ,$, and 0 otherwise. If G is a Kac-Moody algebra then there are no imaginary simple roots so the sum over α is 1 and we recover the usual character and denominator formulas.

If we have a generalized Kac-Moody algebra G then we choose some universal generalized Kac-Moody algebra mapping to$G$as in theorem 4.1, and call the Weyl group, root lattice, and so on of the universal generalized Kac-Moody algebra the Weyl group, root lattice and so on of $G$.

For the generalized Kac-Moody algebras in this paper, the Cartan subalgebra H is usually finite dimensional and its bilinear form is nonsingular. We often think of roots of $G$as vectors of H by using the natural map from the root lattice to $H$, taking$r _ { i }$to$h _ { i }$. We will often abuse terminology and call the corresponding vectors of H roots. The map from the set of roots to H is not usually injective, so we need to make a few comments to clarify what happens. It is possible for$n > 1$imaginary simple roots to have the same image $r$ in $H$; when this happens we say that r is a simple root of multiplicity $n$. (In general it is possible for the same vector of$H$to be the image of simple and nonsimple roots, but this does not happen for the Lie algebras in this paper.) The simple roots in H are usually linearly dependent so in general there is no reason why there should exist a Weyl vector$\rho$ in H such that$( \rho , r _ { i } ) = - r _ { i } ^ { 2 } / 2$for all real simple roots $r_i$; however such a vector$\rho$does exist for the Lie algebras in this paper.

The denominator formula also needs an obvious modification if roots are regarded as elements of $H$. If a simple root has multiplicity $n>1$, the “set” of simple roots should include $n$ copies of it; the “set” is really a multiset. (A multiset is a set that may contain several copies of the same object, or more precisely a map from a set to the positive integers.) The expression $\epsilon(\alpha)$ in the character formula is the sum of $(-1)^n$ over all ways of writing $\alpha$ as a multiset of pairwise orthogonal imaginary simple roots, all orthogonal to $\lambda$. For example, if there is only one simple root $r$ of norm 0 and multiplicity $n$, then $\epsilon(ir)=\binom{n}{i}(-1)^i$, because there are $\binom{n}{i}$ ways to write $ir$ as a multiset of pairwise orthogonal simple roots.

Remark. Most of these results can be extended to superalgebras with little difficulty, provided that we interpret roots of negative multiplicity as being “superroots”. The only extra detail worth pointing out is that we have to add the condition that all simple superroots are imaginary (and not real). For example, many of the finite dimensional superalgebras are generalized Kac-Moody superalgebras with simple superroots of norm 0. Warning: The Cartan matrix of a finite dimensional superalgebra may depend on the Z-grading chosen.

Any generalized Kac-Moody algebra can be written as a direct sum$E \oplus H \oplus F$of subalgebras, where H is the Cartan subalgebra and$E$and$F$are the subalgebras corresponding to the positive and negative roots. The standard sequence

$$
\dots \to \Lambda^ {2} (E) \to \Lambda^ {1} (E) \to \Lambda^ {0} (E) \to 0
$$

whose homology groups are those of the Lie algebra $E$ [10] shows that $\Lambda(E)=H(E)$, where $\Lambda(E)$ is the virtual vector space $\Lambda^0(E)\ominus\Lambda^1(E)\oplus\Lambda^2(E)\ominus\cdots$ formed from the alternating sum of the exterior powers of $E$, and $H(E)$ is the virtual vector space $H_0(E)\ominus H_1(E)\oplus H_2(E)\ominus\cdots$ formed from the alternating sum of the homology groups of $E$ with real coefficients. If $L$ is the root lattice of $M$, both sides are $L$-graded virtual vector spaces whose homogeneous pieces are finite-dimensional, so these infinite sums are meaningful.

The denominator formula for any generalized Kac-Moody algebra follows from the fact that$\Lambda ( E ) = H ( E )$as virtual L-graded vector spaces. The character of$\Lambda ( E )$is a product over positive roots. In the case of ordinary Kac-Moody algebras the vector space $H _ { i } ( E )$has a basis corresponding to the elements of the Weyl group of length$i ,$so the character of$H ( E )$is a sum over the Weyl group. If we work out everything explicitly we obtain the denominator formula

$$
e ^ {\rho} \prod_ {\alpha > 0} (1 - e ^ {\alpha}) ^ {\mathrm{mult} (\alpha)} = \sum_ {w \in W} \det (w) w (e ^ {\rho})
$$

for Kac-Moody algebras, and a similar but slightly more complicated calculation gives the denominator formula for generalized Kac-Moody algebras. For Kac-Moody algebras this calculation is carried out in Garland and Lepowsky [20] and most of their methods and results apply to generalized Kac-Moody algebras with only minor changes. They obtain a more general result which not only gives the character formula of any highest weight module, but also works if E is replaced by various other radicals of parabolic subalgebras. We do not need these more general results, but they are easily extended to the case of generalized Kac-Moody algebras.

The groups$H _ { i } ( E )$can be calculated for generalized Kac-Moody algebras in the same way that they are calculated for ordinary Kac-Moody algebras in Garland and Lepowsky [20]. The result we get is that$H _ { i } ( E )$is the subspace of$\Lambda ^ { i } ( E )$spanned by the homogeneous vectors of$\Lambda ^ { i } ( E )$whose degrees$r \in L$satisfy$( r + \rho ) ^ { 2 } = \rho ^ { 2 }$. The degree r of any homogeneous vector of$\Lambda ^ { i } ( E )$satisfies$( r + \rho ) ^ { 2 } \leq \rho ^ { 2 }$, so$H _ { i } ( E )$can be thought of as a sort of boundary of$\Lambda ^ { i } ( E )$. These homology groups are easy to work out for any generalized Kac-Moody algebra, provided that we know the simple roots and their multiplicities. For the monster Lie algebra, we carry out this calculation in section 8.

In practice it is sufficient to know the subspace of $H(E)$ of elements whose degree $r$ has the property that $r+\rho$ is in the fundamental Weyl chamber. This subspace is isomorphic to the subspace of $\Lambda(E)$ of all elements that can be written in the form $e_1\wedge e_2\wedge\cdots$, where the $e_i$ are vectors in root spaces of pairwise orthogonal imaginary simple roots, so the character of this subspace is $\sum_\alpha \epsilon(\alpha)e^\alpha$, as in the denominator formula. There is a similar description of the homology groups of $E$ with coefficients in any lowest-weight module, which can be used to prove the character formula for lowest-weight modules, but we do not use this.

## 5 The no-ghost theorem

We prove a slight extension of the no-ghost theorem. The idea of using the no-ghost theorem to prove results about Kac-Moody algebras appears in Frenkel’s paper [15], which also contains a proof of the no-ghost theorem. The original proof of Goddard and Thorn [21] works for the cases we need with only trivial modifications. For convenience we give a quick sketch of their proof.

Theorem 5.1. (The no-ghost theorem.) Suppose that V is a vector space with a nonsingular bilinear form$( , )$and suppose that V is acted on by the Virasoro algebra in such a way that the adjoint of$L _ { i }$is$L _ { - i } ,$the central element of the Virasoro algebra acts as multiplication by 24, any vector of V is a sum of eigenvectors of$L _ { 0 }$with nonnegative integral eigenvalues, and all the eigenspaces of$L _ { 0 }$are finite dimensional. We let$V ^ { i }$be the subspace of$V$ on which$L _ { 0 }$has eigenvalue i. Assume that V is acted on by a group$G$which preserves all this structure. We let$V _ { I I _ { 1 , 1 } }$be the vertex algebra of the double cover$\widehat{II}_{1,1}$of the two dimensional even unimodular Lorentzian lattice$I I _ { 1 , 1 }$(so that$V _ { I I _ { 1 , 1 } }$is II -graded, has a bilinear form$( , ) ,$, and is acted on by the Virasoro algebra as in section$3 )$. We let$P ^ { 1 }$be the subspace of the vertex algebra$V \otimes V _ { I I _ { 1 , 1 } }$of vectors v with$L _ { 0 } ( v ) = v , L _ { i } ( v ) = 0$for $i > 0$, and we let$P _ { r } ^ { 1 }$be the subspace of$P ^ { 1 }$of degree$r \in I I _ { 1 , 1 }$. All these spaces inherit an action of$G$from the action of G on V and the trivial action of G on$V _ { I I _ { 1 , 1 } }$and$\mathbf { R } ^ { 2 }$ Then the quotient of$P _ { r } ^ { 1 }$by the nullspace of its bilinear form is naturally isomorphic, as a G module with an invariant bilinear form, to$V ^ { 1 - ( r , r ) / 2 } \ i f r \neq 0$and to$V ^ { 1 } \oplus \mathbf { R } ^ { 2 } \ i f r = 0$

The name “no-ghost theorem” comes from the fact that in the original statement of the theorem in [21], V was part of the underlying vector space of the vertex algebra of a positive definite lattice so the inner product on$V ^ { i }$was positive definite, and thus$P _ { r } ^ { 1 }$had no ghosts (i.e. vectors of negative norm) for r nonzero. The space$V ^ { i }$is the space$V _ { i - 1 }$ used in the rest of this paper.

Sketch of proof (taken from Goddard and Thorn, [21]). Fix some nonzero $r\in II_{1,1}$ and some norm 0 vector $w\in II_{1,1}$ with $(r,w)\neq0$.

We use the following operators. We have an action of the Virasoro algebra on$V\otimes V_{II_{1,1}}$ generated by its conformal vector. The operators$L _ { i }$of the Virasoro algebra satisfy the relations

$$
[ L _ {i}, L _ {j} ] = (i - j) L _ {i + j} + 26 (i ^ {3} - i) \delta_ {- j} ^ {i} / 12.
$$

and the adjoint of$L _ { i }$is$L _ { - i }$. (The 26 comes from the 24 in theorem 5.1 plus the dimension of$I I _ { 1 , 1 } . )$We define operators$K _ { i } , i \in \mathbf { Z }$by$K _ { i } = v _ { i - 1 }$where v is the element${ e _ { - 2 } ^ { - w } e ^ { w } }$of the vertex algebra of$I I _ { 1 , 1 } ,$and$e ^ { w }$is an element of the group ring of the double cover of$I I _ { 1 , 1 }$ corresponding to$w \in I I _ { 1 , 1 }$and$e ^ { - w }$is its inverse. (There are in fact two possible choices for$e ^ { w }$which differ by a factor of −1, but it does not matter which we choose because this factor of −1 cancels out in the expression$e _ { - 2 } ^ { - w } e ^ { w } . )$These operators satisfy the relations

$$
\begin{array}{l} \left[ L _ {i}, K _ {j} \right] = - j K _ {i + j} \\ \left[ K _ {i}, K _ {j} \right] = 0 \end{array}
$$

because w has norm 0, and the adjoint of$K _ { i }$is $K_{-i}$.

We define the following subspaces of$V \otimes V _ { I I _ { 1 , 1 } }$

H is the subspace of$V \otimes V _ { I I _ { 1 , 1 } }$of degree$r \in I I _ { 1 , 1 } . \ H ^ { 1 }$is its subspace of vectors h with $L _ { 0 } ( h ) = h$

$P$ is the subspace of $H$ of vectors $h$ with $L_i(h)=0$ for $i>0$. $P^1=H^1\cap P$.

S, the space of spurious vectors, is the subspace of H of vectors perpendicular to P. $S ^ { 1 } = H ^ { 1 } \cap S$

$N = S \cap P$is the radical of the bilinear form of P, and$N ^ { 1 } = H ^ { 1 } \cap N$

$T ,$the transverse space, is the subspace of P annihilated by all the operators$K _ { i } , i > 0$ and$T ^ { 1 } = H ^ { 1 } \cap T$

K is the space generated by the action of the operators$K _ { i } , i \in \mathbf { Z }$on T.

$V e ^ { r }$is the subspace$V \otimes e ^ { r }$of H.

We have the following inclusions of subspaces of$H \colon$:

$$
\begin{array}{c c c c c c c c c} S & & & P & & & K \\ & \nwarrow & & \nearrow & \nwarrow & \nearrow & \nwarrow \\ & & N & & T & & & V e ^ {r} \end{array}
$$

And we construct the isomorphism from $V^{1-(r,r)/2}e^r$ to $P^1/(N\cap P^1)$ by zigzagging up and down this diagram. More precisely, $V e^r$ and $T$ are both isomorphic to $K$ modulo its nullspace, and $T^1$ is isomorphic to $P^1/(P^1\cap N)$.

Lemma 5.1. If $f$ is a vector of nonzero norm in $T$, then the vectors of the form

$$
L _ {m _ {1}} L _ {m _ {2}} \ldots K _ {n _ {1}} K _ {n _ {2}} \ldots (f)
$$

For all sequences of integers with $0>m_1\geq m_2\geq\cdots$ and $0>n_1\geq n_2\geq\cdots$, the vectors $L_{m_1}L_{m_2}\cdots K_{n_1}K_{n_2}\cdots(f)$ are linearly independent and span a space invariant under the operators $K_i$ and $L_i$, on which the bilinear form is nonsingular.

Sketch of proof: It is possible to order these elements so that the matrix of inner products is upper triangular with nonzero diagonal elements. This implies that they are independent and span a space on which the inner product is nonsingular. The other statements in the lemma are easy to prove.

Lemma 5.2. The bilinear form on$T$is nonsingular, and K is the direct sum of$T$and the nullspace of$K$.

Proof. If we choose an orthogonal basis for$T ,$then the set of all vectors generated from them as in Lemma 5.1 is a basis for H. As H is nonsingular,$T$must therefore also be nonsingular. It now follows that$K$is the direct sum of its nullspace and$T ,$because K is generated from$T$by the operators$K _ { i }$and anything generated from$T$by these operators is in the nullspace of$K$

Lemma 5.3.$V e ^ { r }$is naturally isomorphic to $T$.

Proof. K is also the subspace of H annihilated by all the operators$K _ { i } , i > 0$from which it follows that K is the direct sum of$V e ^ { r }$and the nullspace of$K$. By lemma 5.2 $K$is also the direct sum of$T$and the nullspace of$K ,$, so this gives a natural isomorphism from$V e ^ { r }$to$T$, because they are both isomorphic to the quotient of K by its nullspace.

Lemma 5.4. The associative algebra generated by the elements$L _ { i }$for$i < 0$is generated by elements mapping$S ^ { 1 }$into S.

Proof. Calculation shows that the operators$L _ { - 1 }$and$L _ { - 2 } + 3 L _ { - 1 } ^ { 2 } / 2$have this property, and they generate the algebra generated by all $L_i$'s with $i<0$. (It is in doing these calculations that we need to use the fact that the center of the Virasoro algebra acts as 24 on V and therefore as 26 on$H . )$

Lemma 5.5. $P^1$ is the direct sum of $T^1$ and $N^1$.

Proof. We have to show that any vector p of$P ^ { 1 }$can be written as$p = t + n$for $t\in T^1$ and $n\in N^1$. By lemma 5.3,$p = k + s$for some unique$k \in K ^ { 1 } , s \in S ^ { 1 }$and by lemma$5 . 4 ~ k$ and s are both mapped into K and$S$by some set of generators of the algebra generated by the $L_i$'s, $i>0$. As these generators annihilate$p ,$they must also annihilate k and s. Hence k is in$K ^ { 1 } \cap P ^ { 1 } = T ^ { 1 }$and s is in$S ^ { 1 } \cap P ^ { 1 } = N ^ { 1 }$, so that$P ^ { 1 } = T ^ { 1 } \oplus N ^ { 1 }$

The no ghost theorem now follows immediately, because by lemma 5.3$V ^ { 1 - ( r , r ) / 2 } e ^ { r }$is isomorphic to$T ^ { 1 }$, and by lemma$5 . 5 T ^ { 1 }$is isomorphic to the quotient of$P ^ { 1 }$by its nullspace.

## 6 Construction of the Monster Lie algebra.

We construct the monster Lie algebra $M$ in the proof of the following theorem. This is a generalized Kac-Moody algebra acted on by the monster simple group and graded by $II_{1,1}=\mathbf{Z}^2$. Recall that $V$ is the vertex algebra of the monster, so that $V$ is graded with pieces of dimensions 1, 0, 196884, ..., and $V_{II_{1,1}}$ is the vertex algebra of the two-dimensional even Lorentzian lattice $II_{1,1}$ with matrix $\begin{pmatrix}0&-1\\-1&0\end{pmatrix}$.

Theorem 6.1. There exists a Lie algebra M, which we will call the monster Lie algebra, with the following properties.

(1) M is$II_{1,1}$-graded.

(2) M has a contravariant bilinear form $(\ ,\ )_0$ which is positive definite on the piece of degree $(m,n)\ne(0,0)$. By “contravariant bilinear form” we mean that the $II_{1,1}$-graded Lie algebra $M$ has an involution $\omega$ which acts as $-1$ on $II_{1,1}$ and as $-1$ on the piece of degree $(0,0)$, such that $(u,v)=-(u,\omega(v))_0$ is invariant and $(u,v)=0$ unless $\deg(u)+\deg(v)=0$.

(3) M is acted on by the monster. As a representation of the monster, the piece of M of degree$( m , n )$is isomorphic to$V _ { m n } ~ i f \left( m , n \right) \neq ( 0 , 0 )$, and to the trivial representation $\mathbf { R } ^ { 2 } \ i f ( m , n ) = ( 0 , 0 )$where$V _ { n }$is the piece ofthe monster vertex algebra V ofconformal weight$n + 1$

Proof. The tensor product$V \otimes V _ { I I _ { 1 , 1 } }$of the vertex algebras V and$V _ { I I _ { 1 , 1 } }$is also a vertex algebra. If$P ^ { i }$is the space of vectors v of this vertex algebra satisfying$L _ { j } ( v ) = 0$if $j > 0 , L _ { 0 } ( v ) = v$, then$P ^ { 1 } / D P ^ { 0 }$is a Lie algebra with an invariant bilinear form (,), and an involution ω induced by the trivial automorphism of V and the involution ω of$V_{II_{1,1}}$ defined in section 3. We define the monster Lie algebra M to be the quotient of the Lie algebra$P ^ { 1 } / D P ^ { 0 }$by the kernel of the form (,). (The kernel of the bilinear form on$P ^ { 1 }$is strictly larger than $DP^0$.)

The$I I _ { 1 , 1 }$grading of the vertex algebra$V _ { I I _ { 1 , 1 } }$induces a$I I _ { 1 , 1 }$grading on the Lie algebra M. The no-ghost theorem 5.1 implies that the piece of M of degree$( m , n ) \in I I _ { 1 , 1 }$ is isomorphic to the piece of V of degree$1 - ( m , n ) ^ { 2 } / 2 = 1-mn${ \mathrm { i f ~ } } v \neq 0$and to R<sup>2</sup> if $v = 0$, and that$( g , \omega ( g ) ) > 0 \mathrm { ~ i f ~ } g \in M$is nonzero and homogeneous of nonzero degree in $I I _ { 1 , 1 }$. This proves theorem 6.1.

Remark. The construction of a Lie algebra from a vertex algebra in theorem 6.1 can be carried out for any vertex algebra$V$with a conformal vector, but it is only when this vector has dimension 24 that we can apply the no-ghost theorem to identify the homogeneous pieces of M with those of V. The important point is that the bilinear form on M is positive definite on any piece of nonzero degree, and this need not be true if the conformal vector has dimension greater than 24, even if the inner product on V is positive definite.

Theorem 6.2. The monster Lie algebra M is a generalized Kac-Moody algebra.

Proof: This follows from theorem 6.1. The only condition in the definition of a generalized Kac-Moody algebra that is not immediately obvious from the conclusion of theorem 6.1 is the one about the Z-grading of M. We can Z-grade M in a suitable way by letting elements of M of degree$( m , n ) \in I I _ { 1 , 1 }$have degree 2m$+ n \in \mathbf { Z }$

Remark. If$V _ { L }$is the vertex algebra of any positive definite even lattice L of dimension at most 24 then the bilinear form on the corresponding Lie algebra$M _ { L }$is still almost positive definite, so$M _ { L }$is a generalized Kac-Moody algebra. If$V _ { \Lambda }$is the vertex algebra of the Leech lattice Λ then$M _ { \Lambda }$is (by definition) the fake monster Lie algebra, and its simple roots are described explicitly in [8] (where it is called the monster Lie algebra, or more precisely proved to be isomorphic to something called the monster Lie algebra there). Section 12 contains a summary of results about the fake monster Lie algebra. I have not found any other lattices for which the simple roots of the corresponding Lie algebra can be found explicitly, although for the lattice$E _ { 8 } \oplus E _ { 8 }$all the simple roots of norm$0 , - 2$, or −4 have multiplicity 0 or 1 so there may be something interesting going on in this case. There are some calculations for the case when$V _ { L }$is the vertex algebra of$L = E _ { 8 }$in Kac, Moody and Wakimoto [24].

The monster Lie algebra can also be constructed as a semi-infinite cohomology group; see [19].

The construction of the monster Lie algebra above looks bizarre at first sight, so we briefly explain some of the motivation behind it. The fake monster vertex algebra$M _ { \Lambda }$[8] is the Lie algebra$P ^ { 1 }$/(kernel of bilinear form) of the vertex algebra of the lattice $II_{25,1}$. This lattice is the sum of the Leech lattice Λ and the lattice $II_{1,1}$, and the vertex algebra of the sum of two lattices Λ and$I I _ { 1 , 1 }$is the tensor product of the vertex algebras$V _ { \Lambda }$and $V_{II_{1,1}}$of the lattices, so the fake monster Lie algebra is the space$P ^ { 1 }$/kernel of$V _ { \Lambda } \otimes V _ { I I _ { 1 , 1 } }$ The monster vertex algebra V is similar to the vertex algebra$V _ { \Lambda }$, which suggests replacing $V _ { \Lambda }$by V in the construction above, and this gives the monster Lie algebra M.

## 7 The simple roots of the monster Lie algebra.

We find the simple roots of the monster Lie algebra M constructed in section 6. This algebra turns out to have a Weyl vector, i.e., a vector$\rho$with$( \rho , r ) = - ( r , r ) / 2$for all simple roots r.

We find the simple roots of the monster Lie algebra by using the following identity, which turns out to be its denominator formula.

## Lemma 7.1.

$$
p^{-1}\prod_{\substack{m > 0\\ n\in \mathbf{Z}}}(1 - p^{m}q^{n})^{c(mn)} = j(p) - j(q)\tag{7.1}
$$

where$\begin{array} { r } { j ( q ) - 744 = \sum _ { n } c ( n ) q ^ { n } = q ^ { - 1 } + 196884 q + . . . } \end{array}$

Proof. This is essentially just lemma 2 of section 4 of [8]. For convenience we recall the proof. If we multiply the left hand side by p and take its logarithm we get

$$
\begin{array}{l} - \sum_ {m > 0} \sum_ {n \in \mathbf {Z}} \sum_ {k > 0} c (m n) p ^ {m k} q ^ {n k} / k \\ = - \sum_ {m > 0} \sum_ {n \in \mathbf {Z}} \sum_ {0 <   k | (m, n)} \frac {1}{k} c (\frac {m n}{k ^ {2}}) p ^ {m} q ^ {n} \\ = - \sum_ {m > 0} T _ {m} (\sum_ {n \in \mathbf {Z}} c (n) q ^ {n}) p ^ {m} \\ = - \sum_ {m > 0} T _ {m} (j (q) - 744) p ^ {m} \\ = \sum_ {m > 0} f _ {m} (q) p ^ {m} \end{array}
$$

where$T _ { m }$is the m’th Hecke operator (see Serre [30] proposition 12, chapter VII, section 5) and each$f _ { m }$is a modular function of level 1, holomorphic on the upper half plane, and therefore a polynomial in$j ( q )$. If we exponentiate this we see that the left hand side of 7.1 is of the form$\begin{array} { r } { \sum _ { m > - 1 } g _ { m } ( q ) p ^ { m } } \end{array}$where each$g _ { m }$is a polynomial in$j ( q )$. Each coefficient of$p ^ { m }$of the right hand side of (7.1) is either a constant (if m$\neq 0 )$or$744 - j ( q )$(if $m = 0 )$and is therefore also a polynomial in$j ( q )$. Any polynomial in$j ( q )$is determined by its coefficients of$q ^ { n }$for$n \leq 0$, so to prove the lemma it is sufficient to check that the coefficients of$q ^ { n } , n \leq 0$of both sides are the same, which is easy to do. This proves lemma 7.1.

Remark. The infinite product in (7.1) converges if$| p | , | q | < e ^ { - 2 \pi }$and$p \neq q$, and the infinite series for$j ( q )$converges if$| q | < 1$

Theorem 7.2. The simple roots of the monster Lie algebra M are the vectors (1, n) $( n = - 1 \ o r \ n > 0 )$, each with multiplicity$c ( n )$

Let N be the generalized Kac-Moody algebra with root lattice$I I _ { 1 , 1 }$whose simple roots are as stated in the theorem. The simple roots of a generalized Kac-Moody algebra (with given Cartan subalgebra and choice of fundamental Weyl chamber) are determined by its root multiplicities because of the denominator formula, so it is sufficient to show that the multiplicity of the root$( m , n )$of N is equal to the multiplicity$c ( m n )$of the root $( m , n )$of the algebra M (so N is isomorphic to M). The denominator formula of the Lie algebra N is

$$
e^{\rho}\prod_{\substack{m > 0\\ n\in \mathbf{Z}}} (1 - p^{m}q^{n})^{\mathrm{mult}(m,n)} = \sum_{w\in W}\det (w)w(e^{\rho}S)\tag{7.2}
$$

where mult$( m , n )$is the multiplicity of the root$( m , n )$of$N , p$and q are the elements$e ^ { ( 1 , 0 ) }$ and$e ^ { ( 0 , 1 ) }$of the group ring of$I I _ { 1 , 1 }$, W is the Weyl group of N which is of order 2 and whose nontrivial element exchanges p and$q ,$and$e ^ { \rho }$is$e^{(-1,0)}=p^{-1}$. By the denominator formula quoted in section 4 the element$S$is

$$
S = \sum_ {A} (- 1) ^ {| A |} e ^ {\Sigma A}
$$

where the sum is over all finite subsets A of the set of simple imaginary roots such that any two distinct elements of A are orthogonal, |A| is the number of elements of A, and$\Sigma A$ is the sum of the elements of A. All the imaginary simple roots of N have nonzero inner product with each other, so$S$is equal to$\begin{array} { r } { 1 - \sum _ { n > 0 } c ( n ) p q ^ { n } = 1 - p ( j ( q ) - q ^ { - 1 } - 744 ) } \end{array}$ and hence the right hand side of the denominator formula (7.2) of$N$is

$$
\begin{array}{c} e ^ {\rho} S - w (e ^ {\rho} S) = (p ^ {- 1} - j (q) + q ^ {- 1} + 744) - (q ^ {- 1} - j (p) + p ^ {- 1} + 744) \\ = j (p) - j (q) \end{array}
$$

where$w$is the nontrivial element of the Weyl group W. This is the right hand side of (7.1), so that the left hand sides of (7.1) and (7.2) must also be the same, which implies that the multiplicity of the root$( m , n ) \neq ( 0 , 0 )$of N is c(mn). This proves theorem 7.2.

Remark. This shows that the action of the monster on M can be extended to an action of the full automorphism group of the graded vector space V on M which still preserves the grading and Lie algebra structure of M. The special property of the action of the monster on M that we use is that the pieces of degree$( a , b )$and$( c , d )$of the$II_{1,1}$-graded Lie algebra M are isomorphic as representations of the monster whenever ab$= c d \neq 0$

## 8 The twisted denominator formula.

The monster Lie algebra, like any generalized Kac-Moody algebra, can be written as a direct sum$E \oplus H \oplus F$of subalgebras, where H is the Cartan subalgebra and E and

$F$are the subalgebras corresponding to the positive and negative roots. We recall from section 4 the equality

$$
\Lambda (E) = H (E)\tag{8.1}
$$

where in the case of the monster Lie algebra both sides are virtual$I I _ { 1 , 1 }$-graded modules over the monster. In this section we calculate both sides of (8.1) explicitly and use this to obtain some relations between the coefficients of the Thompson series$T _ { g } ( q )$

For any generalized Kac-Moody algebra the homology groups can be calculated as in section 4 provided we know the simple roots. In the case of the monster Lie algebra M the simple roots are given in section$7$and are just the vectors (1, n),$n = - 1$or$n > 0$with multiplicity$c ( n )$, so we can calculate the homology groups$H _ { i } ( E )$as follows. Recall that $H _ { i } ( E )$is the subspace of elements of$\Lambda ^ { i } ( E )$whose degree r (in the root lattice) satisfies $( r , r + 2 \rho ) = 0$. For the monster Lie algebra we can think of the roots as elements of$I I _ { 1 , 1 }$ and can identify the Weyl vector$\rho$with the norm 0 vector$( - 1 , 0 )$The condition on r then says that$r + \rho$has norm$0 , \ \mathrm { i . e . , } \ r$is a vector of the form$( m , 0 )$or$( 1 , n )$, so we just have to find the elements of$\Lambda ^ { i } ( E )$of these degrees. The answers we get are as follows (where we write$M _ { m , n }$for the subspace of elements of M of degree$( m , n ) \in I I _ { 1 , 1 } )$

$H _ { 0 } ( E )$is one dimensional with character 1, because$\Lambda ^ { 0 } ( E ) = \mathbf { R }$is just a one dimensional space of degree (0, 0).

$H _ { 1 } ( E )$is the subspace of$\Lambda ^ { 1 } ( E ) = E$of elements of degree$( m , 0 )$or$( 1 , n )$. There are no elements of degree$( m , 0 )$and the space of elements of degree$( 1 , n )$is the simple root space$M _ { 1 , n } \cong V _ { n }$, so$H _ { 1 } ( E )$has character$p ( j ( q ) - 744 )$and its piece of degree$( 1 , n )$ is isomorphic to the n’th head representation$V _ { n }$of the monster. (Notice that the first homology group$H _ { 1 } ( E )$is isomorphic to the sum of the simple root spaces; the same is true for any generalized Kac-Moody algebra.)

For$i \geq 2$there are no elements in$\Lambda ^ { i } ( E )$of degree$( 1 , n )$because all elements of E have degrees of the form$( m , n )$with$m \geq 1$. Moreover they all have degrees with$n > 0$ except for the one dimensional space with degree equal to the real simple root$( 1 , - 1 )$, so the only way for an element of$\Lambda ^ { i } ( E )$to have degree$r = ( m , 0 )$is for it to be the exterior product of two elements of$E$of degrees$( 1 , - 1 )$and$( m - 1 , 1 )$. Therefore$H _ { 2 } ( E )$is the sum of pieces of degrees$( m , 0 )$for$m \geq 2$isomorphic to$M _ { m - 1 , 1 } = V _ { m - 1 }$, and$H _ { i } ( E ) = 0$ for$i \geq 3$

To summarize, the homology groups of $E$ are the following $II_{1,1}$-graded vector spaces, where $p$ and $q$ stand for one-dimensional vector spaces of degrees $(1,0)$ and $(0,1)$ in $II_{1,1}$, and each $V_i$ has degree $0\in II_{1,1}$.

$H _ { 0 } ( E ) = V _ { - 1 } = \mathbf { R }$and has character 1.

$\begin{array} { r } { H _ { 1 } ( E ) = \sum _ { n \in \mathbf { Z } } V _ { n } p q ^ { n } } \end{array}$and has character$\textstyle \sum _ { n \in Z } c ( n ) p q ^ { n } = p ( j ( q ) - 744 )$

$\begin{array} { r } { H _ { 2 } ( E ) = p \sum _ { m > 0 } V _ { m } p ^ { m } } \end{array}$and has character$p ( j ( p ) - 744 ) - 1$

$$
H _ {i} (E) = 0 \text {   if   } i \geq 3.
$$

For most interesting generalized Kac-Moody algebras there are an infinite number of nonzero homology groups. In general the largest n with$H _ { n }$nonzero is equal to (maximum length of an element of the Weyl group) + (maximum number of pairwise orthogonal imaginary simple roots) which is usually infinite; however for the monster Lie algebra both the terms in parentheses happen to be 1.

The alternating sum $\sum_i(-1)^iH_i(E)$ is therefore equal to $p\left(\sum_m V_mp^m-\sum_n V_nq^n\right)$, where we use $p$ and $q$ to stand for one-dimensional vector spaces of degrees $(1,0)$ and $(0,1)$. If we substitute these homology groups into (8.1), we find that

$$
p ^ {- 1} \Lambda (\sum_ {m > 0, n \in {\bf Z}} V _ {m n} p ^ {m} q ^ {n}) = \sum_ {m} V _ {m} p ^ {m} - \sum_ {n} V _ {n} q ^ {n}\tag{8.2}
$$

where$V _ { m }$is the m’th head representation of the monster simple group. (Both sides of (8.2) are essentially$II_{1,1}$-graded virtual representations of the monster simple group.) For any finite dimensional vector space$U , \Lambda ( U )$is naturally isomorphic to$\textstyle \exp ( - \sum _ { i > 0 } \psi ^ { i } ( U ) / i )$ (where$\psi ^ { i }$is the i’th Adams operation) by the splitting principle, because both expressions are multiplicative in$U$and are equal if$U$is one dimensional. (The splitting principle says that two natural operations on representations are equal if they are equal on sums of 1-dimensional representations,$\mathrm { i . e . }$, we can pretend that any representation is a sum of 1-dimensional ones, and the Adams operation$\psi ^ { i }$on virtual representations of a group$G$is defined by$\operatorname { T r } ( g | \psi ^ { i } ( U ) ) = \operatorname { T r } ( g ^ { i } | U )$; see [2] for more details.) The same is true for infinite dimensional vector spaces$U$graded by some lattice$L$provided that the homogeneous pieces are all finite dimensional, and the pieces of degree$a \in L$vanish unless a is in some fixed closed cone which does not contain any line and has its vertex at the origin; this condition ensures that all the virtual vector spaces$\Lambda ( U ) , \psi ^ { i } ( U )$, and so on are graded with finite dimensional pieces of each degree and are therefore meaningful. Therefore if we take the trace of some element$g$of the monster on both sides of (8.2) we find that

$$
p ^ {- 1} \exp (- \sum_ {i > 0} \sum_ {m > 0, n \in {\bf Z}} \mathrm{Tr} (g ^ {i} | V _ {m n}) p ^ {m i} q ^ {n i} / i) = \sum_ {m \in {\bf Z}} \mathrm{Tr} (g | V _ {m}) p ^ {m} - \sum_ {n \in {\bf Z}} \mathrm{Tr} (g | V _ {n}) q ^ {n}\tag{8.3}
$$

where${ \mathrm { T r } } ( g | V _ { n } )$is the trace of$g$on the vector space$V _ { n }$.

These relations between the coefficients of the functions$\textstyle \sum { \mathrm { T r } } ( g | V _ { n } ) q ^ { n }$are the same as those that Norton [28] conjectured to hold for the modular functions associated with elements of the monster in Conway and Norton [13, table$2 ]$. The identities 8.3 imply that the functions$T _ { g } ( q )$are completely replicable in the terminology of$[ 28 ] ;$in fact the definition of a completely replicable function in [28] is that the function should satisfy some identities equivalent to 8.3. Norton’s conjectures that these modular functions are completely replicable were proved by Koike [25]. In the next section we use this to prove that the functions$\textstyle \sum _ { m } \operatorname { T r } ( g | V _ { m } ) q ^ { m }$are these modular functions.

## 9 The moonshine conjectures.

In this section we complete the proof of theorem 1.1, i.e., we verify that the monster vertex algebra V satisfies Conway and Norton’s moonshine conjectures [13] that the Thompson series of elements of the monster are certain Hauptmoduls. To do this we show that the identities (8.3) in section 8 imply that the Thompson series are determined by their first 5 coefficients$c _ { g } ( i ) , 1 \leq i \leq 5$, and then use the fact that the Hauptmoduls listed by Conway and Norton in [13, table 2] satisfy the same identities ([25]) and have the same first five coefficients.

The coefficients$c _ { g } ( n ) = \operatorname { T r } ( g | V _ { n } )$of the Thompson series of elements of the monster satisfy the relations (8.3). If we compare the coefficients of$p ^ { 2 }$and$p ^ { 4 }$of both sides of 8.3 and carry out some elementary algebra we find that the coefficients$c _ { g } ( i )$satisfy the recursion formulas below for$k \geq 1$:

$$
\begin{array}{c} c _ {g} (4 k) = c _ {g} (2 k + 1) + (c _ {g} (k) ^ {2} - c _ {g ^ {2}} (k)) / 2 + \sum_ {1 \leq j <   k} c _ {g} (j) c _ {g} (2 k - j) \\ c _ {g} (4 k + 1) = c _ {g} (2 k + 3) - c _ {g} (2) c _ {g} (2 k) + (c _ {g} (2 k) ^ {2} + c _ {g ^ {2}} (2 k)) / 2 \\ \quad + (c _ {g} (k + 1) ^ {2} - c _ {g ^ {2}} (k + 1)) / 2 + \sum_ {1 \leq j \leq k} c _ {g} (j) c _ {g} (2 k - j + 2) \\ \quad + \sum_ {1 \leq j <   k} c _ {g ^ {2}} (j) c _ {g} (4 k - 4 j) + \sum_ {1 \leq j <   2 k} (- 1) ^ {j} c _ {g} (j) c _ {g} (4 k - j) \\ c _ {g} (4 k + 2) = c _ {g} (2 k + 2) + \sum_ {1 \leq j \leq k} c _ {g} (j) c _ {g} (2 k - j + 1) \\ c _ {g} (4 k + 3) = c _ {g} (2 k + 4) - c _ {g} (2) c _ {g} (2 k + 1) \\ \quad - (c _ {g} (2 k + 1) ^ {2} - c _ {g ^ {2}} (2 k + 1)) / 2 + \sum_ {1 \leq j \leq k + 1} c _ {g} (j) c _ {g} (2 k - j + 3) \\ \quad + \sum_ {1 \leq j \leq k} c _ {g ^ {2}} (j) c _ {g} (4 k - 4 j + 2) + \sum_ {1 \leq j \leq 2 k} (- 1) ^ {j} c _ {g} (j) c _ {g} (4 k - j + 2). \end{array}\tag{9.1}
$$

where$c _ { g } ( n ) = \mathrm { T r } ( g \vert V _ { n } ) , c _ { g ^ { 2 } } ( n ) = \mathrm { T r } ( g ^ { 2 } \vert V _ { n } )$. In particular if$n = 4$or$n > 5$then the coefficient$c _ { g } ( n )$is determined by the coefficients$c _ { g } ( i )$and$c _ { g ^ { 2 } } ( i )$for$1 \leq i < n$, so if we know all the coefficients$c _ { g } ( n )$for$n = 1 , 2 , 3$, and 5 and all elements g of the monster then we can work out all the coefficients$c _ { g } ( n )$. (The coefficient$c _ { g } ( 5 )$is not determined by the recursion relations because they degenerate into$c _ { g } ( 5 ) = c _ { g } ( 5 )$. The Thompson series of an element of the monster is not determined by its first 5 coefficients$c _ { g } ( i ) , 1 \leq i \leq 5$ but is determined by the coefficients$c _ { g ^ { j } } ( i ) , 1 \leq i \leq 5$of the Thompson series of all its powers$g ^ { j }$. For example, the Thompson series of the elements 60F and 93A (in ATLAS [14] notation) have the same first five coefficients$c _ { g } ( i ) , 1 \leq i \leq 5$. Norton showed in [28] that any completely replicable function$\textstyle \sum a ( n ) q ^ { n }$is determined by its 12 coefficients${ { a } _ { i } } ,$ $i = 1 , 2 , 3 , 4 , 5 , 7 , 8 , 9 , 11 , 17 , 19 , 23 . )$

For the case of the elliptic modular function$j ( q )$, where$g = 1$, these recursion formulas were discovered by Mahler [27]. We do not make any use of the formulas (9.1), apart from the fact that the coefficients for$n = 1 , 2 , 3$and 5 determine all the coefficients. (This is easy to check without calculating the formulas (9.1) explicitly. The reason for listing them explicitly is that they are a very efficient way of working out the coefficients$c _ { g }$on a computer.)

Norton [28] stated and Koike [25] proved that the modular functions associated with elements of the monster in [13, table 2] also satisfy the relations (8.3) (with$\operatorname { T r } ( g | V _ { m } )$ replaced by the coefficient of$q ^ { m }$of the modular function corresponding to$g )$and therefore also satisfy the recursion relations (9.1) above. To prove that the Thompson series of elements of the monster are these modular functions, it is therefore sufficient to check that the coefficients of$q ^ { i } , i \leq 5$of each function are the same.

The coefficients of$q ^ { i } , i \leq 5$of each modular function are in Conway and Norton [13, table 4], and they define representations of the monster which decompose as stated at the end of section 3. We can work out the coefficients$c _ { g } ( i ) , 1 \leq i \leq 5$of the Thompson series of elements of the monster as follows. Knowing the coefficients$c _ { g } ( i ) , 1 \leq i \leq 5$of the Thompson series is equivalent to knowing how the representations$V _ { i } , 1 \le i \le 5$of the monster decompose into irreducible representations of the monster. The only irreducible representations of the monster with dimension at most that of$V _ { 5 }$are the first seven, with characters$\chi _ { i } , 1 \leq i \leq 7$in atlas [14] notation. Therefore we can evaluate the coefficients $c _ { g } ( i ) , 1 \leq i \leq 5$of the Thompson series of all elements of the monster provided we can find seven elements$g _ { j } , 1 \leq j \leq 7$of the monster for which we can evaluate these coefficients, and such that the matrix$\chi _ { i } ( g _ { j } ) , 1 \leq i , j \leq 7$is nonsingular, because this determines the decomposition of$V_i$, $1\leq i\leq5$, into irreducible representations of the monster.

In their book [16] Frenkel, Lepowsky and Meurman give an explicit formula for the Thompson series of any element of the centralizer of an involution of type 2B of the monster. The elements of odd order of $2^{1+24}.Co_1$ correspond to the elements of odd order of the group $2.Co_1$ of automorphisms of the Leech lattice Λ. Frenkel, Lepowsky and Meurman’s formula is particularly easy to evaluate if the corresponding automorphism of the Leech lattice is of odd order and fixes no nonzero vectors: it becomes

$$
2 \sum_ {n} \mathrm{Tr} (g | V _ {n}) q ^ {n} = 1 / \eta_ {g} (q) + \eta_ {g} (q) / \eta_ {g} (q ^ {2}) + \eta_ {g} (q) / \eta_ {g} (q ^ {1 / 2}) + \eta_ {g} (q) / \eta_ {g} (- q ^ {1 / 2})\tag{9.2}
$$

where$\eta _ { g } ( q )$is the eta function of$g$acting on the Leech lattice, equal to$\eta ( \epsilon _ { 1 } q ) \ldots \eta ( \epsilon _{24} q )$if $g$has eigenvalues$\epsilon _ { 1 } , \ldots , \epsilon _{24}$on the vector space$\Lambda \otimes \mathbf { R }$, where$\begin{array} { r } { \eta ( q ) = q ^ { 1/24 } \prod _ { n > 0 } ( 1 - q ^ { n } ) } \end{array}$ If we put$f ( \tau ) = 1 / \eta _ { g } ( q )$(where$q = e ^ { 2 \pi i \tau } )$then$f ( \tau ) - f ( 0 )$is the modular function of genus 0 that Conway and Norton associate to the element g of the monster in [13, table 2]. The coefficients of the right hand side of the formula above are easy to evaluate explicitly, and we can check that its coefficients of$q ^ { i }$for$i \le 5$are equal to those of the modular function$f ( \tau ) - f ( 0 )$. (The right hand side of 9.2 and$f ( \tau ) - f ( 0 )$) are of course equal, as we can see directly by observing that the right hand side of (9.2) is$f ( \tau ) + T _ { 2 } f ( \tau ) / f ( \tau )$ where$T _ { 2 }$is a Hecke operator.)

For our seven elements$g _ { j }$of the monster we choose an element$g _ { 1 }$of conjugacy classes 2B (for which Frenkel, Lepowsky and Meurman explicitly evaluate the Thompson series), and 6 more elements$g _ { i }$of the monster corresponding to odd order automorphisms of the Leech lattice with no nonzero fixed vectors such that the determinant of the$7 \times 7$ matrix$\chi _ { i } ( g _ { j } )$is nonzero. A set of 6 elements satisfying these conditions are those of type

3B, 5B, 7B, 9B, 13B, and 15D in the monster (using Atlas [14] notation) correspond to conjugacy classes 3A, 5A, 7A, 9A, 13A, and 15C of $Co_1$, with cycle shapes $3^{12}1^{-12}$, $5^61^{-6}$, $7^41^{-4}$, $9^31^{-3}$, $13^21^{-2}$, and $15^23^{-2}$. The determinant of the matrix $\chi_i(g_j)$ is $35672555520=2^{22}\cdot3^5\cdot5\cdot7$, which is nonzero. The corresponding modular groups are $\Gamma_0(3)$, $\Gamma_0(5)$, $\Gamma_0(7)$, $\Gamma_0(9)$, $\Gamma_0(13)$, and $\begin{pmatrix}3&0\\0&1\end{pmatrix}^{-1}\Gamma_0(5)\begin{pmatrix}3&0\\0&1\end{pmatrix}$. (At least one element $g_i$ must have even order, because the characters of the first seven monster representations are linearly dependent on odd-order elements; in fact, the character of $S^2(V_1)-\Lambda^2(V_1)-V_1$ vanishes on all odd-order elements.)

We can use this to verify that the representations$V _ { 1 } , V _ { 2 } , V _ { 3 }$, and$V _ { 5 }$of the monster decompose as stated at the end of section 3, and this implies that the numbers $\operatorname{Tr}(g|V_n)$ are equal to the coefficients of the corresponding modular functions in [13] for$n = 1 , 2 , 3$and $5 ,$, and therefore for all n by the recursion relations (9.1). This completes the verification that the Thompson functions $\sum_n\operatorname{Tr}(g|V_n)q^n$ are modular functions of genus 0 and proves theorem 1.1.

## 10 The monstrous Lie superalgebras.

In the remainder of the paper we describe some Lie algebras similar to the monster Lie algebra. In this section we describe some associated to elements of the monster.

The twisted denominator formula for some diagram automorphism$g$of a generalized Kac-Moody algebra, which is obtained by taking the trace of$g$on both sides of the identity $H ( E ) = \Lambda ( E )$, is often the untwisted denominator formula for some generalized Kac-Moody algebra or superalgebra. For example, the twisted denominator formula for$E _ { 6 }$ is just the ordinary denominator formula for$F _ { 4 }$. We construct a family of Lie algebras and superalgebras whose denominator formulas are twisted denominator formulas of the monster Lie algebra. (Warning: unlike the case of finite dimensional Lie algebras, these are not always subalgebras of the monster Lie algebra; in fact some of them are Lie superalgebras.)

If g is an element (or conjugacy class) of the monster group M then we write$T _ { g } ( q )$for the Thompson series$\begin{array} { r } { T _ { g } ( q ) = \sum c _ { g } ( n ) q ^ { n } = \sum \operatorname { T r } ( g | V _ { n } ) q ^ { n } } \end{array}$of $g$. For example,$T _ { 1 } ( q ) +$744 is the elliptic modular function$j ( q )$. The function$T _ { g } ( q )$is the normalized generator for a genus zero function field of a group containing$\Gamma _ { 0 } ( n h )$, where n is the order of$g$and$h$is an integer with$h | ( 24 , n )$

We use the convention that for super vector spaces the dimension is defined to be the dimension of the even part minus the dimension of the odd part. For example, the multiplicity of a root is the dimension of the root space, and is therefore equal to the dimension of the even root space minus the dimension of the odd root space. This provides an interpretation of roots of negative multiplicity. With this convention for multiplicities the denominator formula for generalized Kac-Moody superalgebras is the same as for generalized Kac-Moody algebras.

We define the generalized Kac-Moody superalgebra of an element$g$of the monster to have root lattice$I I _ { 1 , 1 }$and simple roots$( 1 , n )$with multiplicity${ \mathrm { T r } } ( g | V _ { n } )$. (These multiplicities are all integers as can be seen in several ways; for example they are rational by the recursion relations 9.1 and algebraic integers because they are character values.) This is really a family of Lie superalgebras rather than a single superalgebra, because for each simple root$( 1 , n )$we can choose any two nonnegative integers a and b with$a - b = \operatorname { T r } ( g | V _ { n } )$ and take a even simple roots$( 1 , n )$and b odd ones. This only seems to be interesting if all coefficients of$T _ { g }$are positive, in which case we get a Lie algebra, or if the coefficients alternate in sign, in which case we get a superalgebra such that the super elements are those of degree$( m , n )$with m + n odd.

We can work out the root multiplicities of these superalgebras because their denominator formulas are the twisted denominator formulas of the monster Lie algebra. The denominator formula for the Lie superalgebra of$g$is

$$
p ^ {- 1} \prod_ {m > 0, n \in {\bf Z}} (1 - p ^ {m} q ^ {n}) ^ {\mathrm{mult} (m, n)} = \sum_ {m} \mathrm{Tr} (g | V _ {m}) p ^ {m} - \sum_ {n} \mathrm{Tr} (g | V _ {n}) q ^ {n} = T _ {g} (p) - T _ {g} (q)\tag{10.1}
$$

and by (8.3)

$$
T _ {g} (p) - T _ {g} (q) = p ^ {- 1} \exp (- \sum_ {i > 0} \sum_ {m > 0} \sum_ {n \in {\bf Z}} \mathrm{Tr} (g ^ {i} | V _ {m n}) p ^ {m i} q ^ {n i} / i).\tag{10.2}
$$

If we compare the logarithms of (10.1) and (10.2) we find that

$$
\sum_ {i > 0, m > 0, n \in {\bf Z}} \mathrm{Tr} (g ^ {i} | V _ {m n}) p ^ {m i} q ^ {n i} / i = \sum_ {i > 0, m > 0, n \in {\bf Z}} \mathrm{mult} (m, n) p ^ {m i} q ^ {n i} / i\tag{10.3}
$$

and applying the Moebius inversion formula to (10.3) shows that

$$
\mathrm{mult} (m, n) = \sum_ {d s | (m, n)} \frac {\mu (s)}{d s} \mathrm{Tr} (g ^ {d} | V _ {m n / d ^ {2} s ^ {2}})\tag{10.4}
$$

where $\mu$ is the Moebius function. If $f$ is any function of $n$ whose value depends only on $(n,N)$ for some $N$, then $\sum_{ds=k}\mu(s)f(d)$ is 0 unless $k|N$. The trace $\operatorname{Tr}(g^d|V_n)$ depends only on $n$ and $(d,N)$, where $N$ is the order of $g$, so $\sum_{ds=k}\mu(s)\operatorname{Tr}(g^d|V_{mn/d^2s^2})$ is 0 unless $k|N$; hence (10.4) can be simplified to

$$
\mathrm{mult} (m, n) = \sum_ {d s | (m, n, N)} \frac {\mu (s)}{d s} \mathrm{Tr} (g ^ {d} | V _ {m n / d ^ {2} s ^ {2}})\tag{10.5}
$$

This is the formula for the multiplicity of roots of the superalgebra of $g$. The sum on the right of (10.5) can often be simplified by expressing $T_{g^d}$ in terms of $T_g$. For example, suppose $N=N_1N_2$ is square-free and $\Gamma_0(N)^+_{d|N_1}$ has genus 0, where $\Gamma_0(N)^+_{d|N_1}$ is generated by $\Gamma_0(N)=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\mathbf{Z}):c\equiv0\pmod N\right\}$ together with the Atkin-Lehner involutions for all divisors of $N_1$ (see [13]). If $g$ is an element of the monster corresponding to one of these groups then so is $g^k$. By the compression formula of [13, section 8]

$$
T _ {g ^ {p}} (\tau) = T _ {g} (\tau) + T _ {g} (\tau / p) + \ldots + T _ {g} ((\tau + p - 1) / p)
$$

for any prime divisor$p$of$N _ { 1 }$, and

$$
T _ {g ^ {p}} (\tau) = T _ {g} (\tau) - T _ {g} (\tau / p ^ {2}) - \ldots - T _ {g} ((\tau + p ^ {2} - 1) / p ^ {2})
$$

for any prime divisor p of$N _ { 2 }$. These imply that

$$
\mathrm{Tr} (g ^ {d} | V _ {n}) = \sum_ {d _ {1} | (d, N _ {1})} \sum_ {d _ {2} | (d, N _ {2})} d _ {1} d _ {2} ^ {2} \mu (d _ {2}) \mathrm{Tr} (g | V _ {d _ {1} d _ {2} ^ {2} n})\tag{10.6}
$$

by induction on the number of divisors of d. If we substitute (10.6) into (10.5) and rearrange we find that

$$
\operatorname{mult} (m, n) = \sum_ {d | (m, n, N _ {1})} \operatorname{Tr} (g | V _ {m n / d}) \prod_ {p | (m, n, N _ {2})} (1 - p)\tag{10.7}
$$

where the product is over all primes p dividing$( m , n , N _ { 2 } )$

We get particularly interesting results when$N _ { 2 }$is 1 or 2. First suppose that$N _ { 2 } = 1$so that$N = N _ { 1 }$is one of the 44 squarefree integers that are orders of elements in the monster, which are the same as the integers for which $\Gamma_0(N)^+$ has genus 0. Let$g$be an element of the monster corresponding to the group $\Gamma_0(N)^+$, so that$T _ { g } ( q )$is the normalized generator of the function field of $\Gamma_0(N)^+$. Then (10.7) becomes

$$
\operatorname{mult} (m, n) = \sum_ {d | (m, n, N)} \operatorname{Tr} (g | V _ {m n / d})\tag{10.8}
$$

and if we substitute (10.8) into (10.1) we obtain the formula

$$
T _ {g} (p) - T _ {g} (q) = p ^ {- 1} \prod_ {m > 0, n \in \mathbf {Z}} \prod_ {d | N} (1 - p ^ {d m} q ^ {d n}) ^ {c _ {g} (d m n)}
$$

which generalizes the product formula for the j function. For these cases the coefficients$c _ { g }$ of the Thompson series$T _ { g } ( q )$are always nonnegative, so the algebras we get are Lie algebras rather than Lie superalgebras. This seems to happen whenever the corresponding subgroup of$P G L _ { 2 } ( R )$contains the Fricke involution$\tau \to - 1 / N \tau$. More generally, Norton has observed ([29]) that the result of applying the Fricke involution to a Thompson series always has nonnegative coefficients.

Similarly suppose that$N _ { 2 } = 2$so that$N _ { 1 }$is one of the squarefree integers 1, 3, 5, 7, 11, or 15 for which $\Gamma_0(2N_1)^+_{d|N_1}$ has genus 0. Then (10.7) becomes

$$
\operatorname{mult} (m, n) = (- 1) ^ {(m - 1) (n - 1)} \sum_ {d | (m, n, N _ {1})} \operatorname{Tr} (g | V _ {m n / d}).
$$

The coefficients of the Thompson series for these six cases alternate in sign, so the multiplicity of$( m , n )$is at least 0 or at most 0 depending on whether$m + n$is even or odd. Therefore the root$( m , n )$is an even root or an odd (super) root depending on the parity of$m + n$. The same is true for any element whose Thompson series has coefficients that alternate in sign. If the coefficients of a Thompson series are neither at least 0 nor alternating in sign, then the root space of some root$( m , n )$is in general a sum of an even space and an odd space, and the multiplicity of the root is the difference of the dimensions of these two spaces. However the Lie superalgebras are probably not very interesting unless the coefficients are either all positive or alternating in sign.

## 11 Some modular forms.

We verify some identities involving modular forms of level 2 that we use later. This section can be missed out if the reader is willing to assume these identities.

The modular forms in this section are usually forms of level 2, i.e., modular forms for $\Gamma(2)=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\mathbf{Z}):\begin{pmatrix}a&b\\c&d\end{pmatrix}\equiv\begin{pmatrix}1&0\\0&1\end{pmatrix}\pmod 2\right\}$. We recall a few facts about this group from [22]. The group $\Gamma(2)$ has no elliptic elements, 3 cusps (represented by 0, 1, and $\infty$), genus 0, and index 6 in $SL_2(\mathbf{Z})$. The dimension of the space of forms of even nonnegative weight $2k$ is $k+1$, and if $f$ and $g$ are two linearly independent forms of weight 2 then every form can be written uniquely as a polynomial in $f$ and $g$. Two modular forms of level 2 and weight $2k$ are equal if and only if their coefficients of $q^0,q^{1/2},q^1,\ldots,q^k$ are equal. The group $\Gamma(2)$ is conjugate to $\Gamma_0(4)=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\mathbf{Z}):c\equiv0\pmod4\right\}$, and $f(q)$ is a modular form for $\Gamma_0(4)$ iff $f(q^{1/2})$ is a modular form for $\Gamma(2)$.

We list several modular forms of level 2, together with enough of their Fourier coefficients to verify the identities we use later. Recall that to prove that two modular forms are equal it is sufficient to check that sufficiently many of their Fourier coefficients are equal.

The following are some forms of weight 4 and level 2.

$$
\begin{array}{l} \theta_{E_8}(q)=1+240(q+9q^2+28q^3+\cdots+\sigma_3(n)q^n+\cdots) \\ \theta_{2E_8}(q)=1+240q^2+\cdots \\ \theta_{2E_8+v_1}(q)=2q^{1/2}+56q^{3/2}+252q^{5/2}+\cdots \\ \theta_{2E_8+v_2}(q)=16q+128q^2+448q^3+\cdots \\ \eta(q)^{16}\eta(q^{1/2})^{-8}=q^{1/2}+8q+28q^{3/2}+64q^2+126q^{5/2}+224q^3+\cdots \\ \eta(q)^{16}\eta(-q^{1/2})^{-8}=-q^{1/2}+8q-\cdots \\ \eta(q)^{16}\eta(q^2)^{-8}=1-16q+112q^2-448q^3+\cdots \end{array}
$$

The form$\theta _ { E _ { 8 } } ( q )$is the theta function of the$E _ { 8 }$lattice, and the form$\theta _ { 2 E _ { 8 } + v _ { i } }$is the theta function of the coset of$2 E _ { 8 }$containing a vector$v _ { i }$of norm i in the dual of$2 E _ { 8 }$but not in $E _ { 8 }$(where$2 E _ { 8 }$is the$E _ { 8 }$lattice with all norms doubled).

Lemma 11.1. If $\eta_{2+}(q)=\eta(q)^8\eta(q^2)^8$, then

$$
\begin{array}{r} \theta_ {2 E _ {8}} (q) / \Delta (q) = 1 / \eta_ {2 +} (q) + 1 / \eta_ {2 +} (q ^ {1 / 2}) + 1 / \eta_ {2 +} (- q ^ {1 / 2}) \\ \theta_ {2 E _ {8} + v _ {1}} (q) / \Delta (q) = 1 / \eta_ {2 +} (q ^ {1 / 2}) - 1 / \eta_ {2 +} (- q ^ {1 / 2}) \\ \theta_ {2 E _ {8} + v _ {2}} (q) / \Delta (q) = 1 / \eta_ {2 +} (q ^ {1 / 2}) + 1 / \eta_ {2 +} (- q ^ {1 / 2}) \end{array}
$$

Proof. If we multiply both sides by $\Delta(q)$, then both sides are modular forms of level 2 and weight 4, so it is sufficient to check that the coefficients of $q^0$, $q^{1/2}$, and $q^1$ on both sides are equal, which we can do using the expressions above.

The following are some forms of weight 8 and level 2.

$$
\begin{array}{c} \theta_{\Lambda_2}(q)=1+4320q^2+\cdots \\ \theta_{\Lambda_2}(q^{1/2})=1+4320q+61440q^{3/2}+522720q^2+\cdots \\ \theta_{\Lambda_2}(-q^{1/2})=1+4320q-61440q^{3/2}+522720q^2+\cdots \\ \eta(q)^{32}\eta(q^2)^{-16}=1-32q+480q^2-4480q^3+\cdots \\ \eta(q)^{32}\eta(q^{1/2})^{-16}=q+16q^{3/2}+120q^2+576q^{5/2}+2060q^3+\cdots \\ \eta(q)^{32}\eta(-q^{1/2})^{-16}=q-16q^{3/2}+120q^2+\cdots \end{array}
$$

The form$\theta _ { \Lambda _ { 2 } } ( q )$is the theta function of the Barnes-Wall lattice$\Lambda _ { 2 }$of dimension 16, and is a modular form for $\Gamma_0(2)^+$. The forms$\theta _ { \Lambda _ { 2 } + v _ { i } }$are defined in the same way as for the lattice$2 E _ { 8 }$

Lemma 11. 2. Let$\eta _ { 2 - } ( q )$be the modular form$\eta ( q ) ^ { - 8 } \eta ( q ^ { 2 } ) ^ { 16 }$. Then

$$
\begin{array}{r l} & {\theta_ {\Lambda_ {2}} (q) / \Delta (q) = 1 / \eta_ {2 -} (q) - 1 / \eta_ {2 -} (q ^ {1 / 4}) - 1 / \eta_ {2 -} (i q ^ {1 / 4}) - 1 / \eta_ {2 -} (- q ^ {1 / 4}) - 1 / \eta_ {2 -} (- i q ^ {1 / 4})} \\ & {\theta_ {\Lambda_ {2} + v _ {3}} / \Delta (q) = 1 / \eta_ {2 -} (q ^ {1 / 4}) + 1 / \eta_ {2 -} (i q ^ {1 / 4}) + 1 / \eta_ {2 -} (- q ^ {1 / 4}) + 1 / \eta_ {2 -} (- i q ^ {1 / 4})} \\ & {\theta_ {\Lambda_ {2} + v _ {2}} / \Delta (q) = 1 / \eta_ {2 -} (q ^ {1 / 4}) - 1 / \eta_ {2 -} (i q ^ {1 / 4}) + 1 / \eta_ {2 -} (- q ^ {1 / 4}) - 1 / \eta_ {2 -} (- i q ^ {1 / 4})} \end{array}
$$

Proof. If we multiply both sides by $\Delta(q)$, then both sides are modular forms of weight 8 and level 2, so it is sufficient to check that the coefficients of $q^0$, $q^{1/2}$, $q^1$, $q^{3/2}$, and $q^2$ on both sides are equal.

## 12 The fake monster Lie algebra.

In the next section we construct a family of superalgebras whose denominator formulas are twisted versions of the denominator formula of the fake monster Lie algebra, in the same way that we constructed a family of algebras from the monster Lie algebra. To do this we need a detailed description of the fake monster Lie algebra, which we give in this section.

As the Leech lattice Λ is an even lattice, it has a unique central extension

$$
0 \to \{1, - 1 \} \to \hat {\Lambda} \to \Lambda \to 0
$$

by a group of order 2, such that the commutator of any inverse images of$r , s \in \Lambda$is $( - 1 ) ^ { ( r , s ) }$. This central extension is unique up to nonunique isomorphism, and its group of automorphisms$\operatorname { A u t } ( \hat { \Lambda } )$preserving the inner product is a nonsplit extension$2 ^ { 24 } . \mathrm { A u t } ( \Lambda )$ (The double cover of this nonsplit extension is isomorphic to the double cover of a centralizer of an involution of type 2B in the monster simple group.)

We start by recalling some results about the fake monster Lie algebra from [8] (where it is called the monster Lie algebra). The root lattice of the fake monster Lie algebra is the 26 dimensional even unimodular Lorentzian lattice$I I _ { 25 , 1 } = \Lambda \oplus I I _ { 1 , 1 }$, where the norm of an element$( \lambda , m , n ) \in \Lambda \oplus I I _ { 1 , 1 }$is defined to be$\lambda^2-2mn$. The real simple roots are the norm 2 vectors of the form$( \lambda , 1 , \lambda ^ { 2 } / 2 - 1 )$, and the imaginary simple roots are the positive multiples$n \rho$of the Weyl vector$\rho = ( 0 , 0 , 1 )$, each with multiplicity 24. A nonzero vector $r \in I I _ { 25 , 1 }$is a root if and only if$r ^ { 2 } \leq 2$, in which case it has multiplicity$p _ { 24 } ( 1 - r ^ { 2 } / 2 )$ where$p _ { 24 } ( n )$is the number of partitions of n into parts of 24 colours. The fake monster Lie algebra is essentially the space of physical vectors of the vertex algebra of$\hat { I I } _ { 25 , 1 }$, and can be constructed from the vertex algebra$V _ { \Lambda }$of$\hat { \Lambda }$in the same way that the monster Lie algebra M was constructed from the monster vertex algebra V in section 6.

The fake monster Lie algebra is acted on by the group of affine automorphisms of the Leech lattice, a split extension $\Lambda\cdot\operatorname{Aut}(\Lambda)$, because its Dynkin diagram may be interpreted as the Leech lattice: it has one real simple root $(\lambda,1,\lambda^2/2-1)$ for each Leech-lattice vector $\lambda$. However, this is the wrong group of automorphisms to use. A more useful group of automorphisms of the fake monster Lie algebra is the nonsplit extension $2^{24}\cdot\operatorname{Aut}(\Lambda)=\operatorname{Aut}(\hat{\Lambda})$, which acts naturally on the vertex algebra of the central extension $\hat{\Lambda}$ and therefore on the fake monster Lie algebra. The point is that the no-ghost theorem 5.1 describes how $\operatorname{Aut}(\hat{\Lambda})$ acts on the root spaces; it is not obvious how to do this using $\operatorname{Aut}(\Lambda)$.

We now describe the fake monster Lie algebra $M_\Lambda$ as a module over $\operatorname{Aut}(\hat{\Lambda})=2^{24}\operatorname{Aut}(\Lambda)$. If we forget the $\Lambda$ in the $II_{25,1}=\Lambda\oplus II_{1,1}$ grading, we can regard $M_\Lambda$ as a $II_{1,1}$-graded Lie algebra. Its degree-$(m,n)$ piece is isomorphic as a $\Lambda$-graded $2^{24}\operatorname{Aut}(\Lambda)$-module to the weight-$1-mn$ piece of the vertex algebra $V_\Lambda$ of $\hat{\Lambda}$ by Theorem 6.1, so it is sufficient to describe $V_\Lambda$ explicitly.

We let $S=S(\bigoplus_{i>0}\Lambda_i)$ be the symmetric algebra on countably many copies $\Lambda_i$ of the Leech lattice $\Lambda$, graded so elements of $\Lambda_i$ have weight $i$. The dimension of the weight-$n$ subspace is $p_{24}(n)$, the number of partitions of $n$ into parts of 24 colours, equal to the coefficient of $q^{n-1}$ in $1/\Delta(q)=q^{-1}\prod_{i>0}(1-q^i)^{-24}$. We let $\mathbf{Z}(\hat{\Lambda})$ be the twisted group ring of $\Lambda$, the group ring of $\hat{\Lambda}$ modulo the ideal $(1+\epsilon)$, where $\epsilon$ corresponds to $-1\in\hat{\Lambda}$, and grade it by giving $e^v$ weight $(v,v)/2$ for $v\in\hat{\Lambda}$. (This grading does not satisfy $\deg(ab)=\deg(a)+\deg(b)$.) Finally, $V_\Lambda\cong\mathbf{Z}(\hat{\Lambda})\otimes S$. The group $2^{24}\operatorname{Aut}(\Lambda)=\operatorname{Aut}(\hat{\Lambda})$ acts on both $\hat{\Lambda}$ and each $\Lambda_i$, and hence on $V_\Lambda$. Its $\Lambda$-grading comes from the $\Lambda$-grading on $\mathbf{Z}(\hat{\Lambda})$; the grading on $S$ is trivial. This describes $V_\Lambda$ as a $\Lambda$-graded $\operatorname{Aut}(\hat{\Lambda})$-module and therefore describes $M_\Lambda$ as a $II_{25,1}$-graded $\operatorname{Aut}(\hat{\Lambda})$-module.

We need a lemma to construct some elements of$\operatorname { A u t } ( \hat { \Lambda } )$from elements of$\operatorname { A u t } ( \Lambda )$

Lemma 12.1. Let $\sigma$ be an automorphism of $\Lambda$ of order $n$. Let $\Lambda^\sigma$ be the vectors of $\Lambda$ fixed by $\sigma$, and let $\hat{\Lambda}^\sigma$ be its inverse image in $\hat{\Lambda}$. If $n$ is odd, then $\sigma$ lifts to an element $\hat{\sigma}\in\operatorname{Aut}(\hat{\Lambda})$ of order $n$ which fixes all elements of $\hat{\Lambda}^\sigma$. If $n$ is even, then $\sigma$ lifts to an element $\hat{\sigma}\in\operatorname{Aut}(\hat{\Lambda})$ which fixes all elements of $\hat{\Lambda}^\sigma$. The automorphism $\hat{\sigma}^n$ multiplies any $v\in\hat{\Lambda}$ by $\epsilon^{(v,\sigma^{n/2}(v))}$; in particular, $\hat{\sigma}$ has order $n$ if $(v,\sigma^{n/2}(v))$ is even for all $v$, and order $2n$ otherwise.

Proof. If $n$ is odd, this is obvious because $\sigma$ has lifts of the same odd order, and every lift of odd order fixes all elements of $\hat{\Lambda}^\sigma$. If $n$ is even, multiply a lift of $\sigma$ by an element of $2^{24}$ to obtain $\hat{\sigma}$ fixing all elements of $\hat{\Lambda}^\sigma$. The element $v\sigma(v)\cdots\sigma^{n-1}(v)$ is fixed by $\sigma$ and hence equals $\sigma(v)\cdots\sigma^n(v)$. Thus $v=\sigma^n(v)$ exactly when $v$ commutes with $\sigma(v)\cdots\sigma^{n-1}(v)$, which holds exactly when $(v,\sigma(v))+\cdots+(v,\sigma^{n-1}(v))$ is even. Since $(v,\sigma^i(v))=(v,\sigma^{n-i}(v))$, this is equivalent to $(v,\sigma^{n/2}(v))$ being even. Therefore $\sigma^n(v)$ fixes $v$ exactly in that case and otherwise multiplies it by $\epsilon^{(v,\sigma^{n/2}(v))}$. This proves Lemma 12.1.

For example, if$\sigma$is an involution of$\operatorname { A u t } ( \Lambda )$whose lattice$\Lambda ^ { \sigma }$has dimension$8$or 16 then it is easy to check that$( v , \sigma ( v ) )$is even for all$v \in \Lambda$, so σ can be lifted to an element $\hat { \sigma } \in \operatorname { A u t } ( \hat { \Lambda } )$which has order 2 and fixes all elements of$\hat { \Lambda } ^ { \sigma }$. This is not possible if σ is an involution with$\Lambda ^ { \sigma }$12-dimensional, because there are vectors v such that$( v , \sigma ( v ) )$is odd.

The homology $H(E)$ of the positive-root subalgebra $E$ of $M_\Lambda$ can be described as follows. Let $e^\rho$ denote a one-dimensional $II_{25,1}$-graded vector space of degree $\rho\in II_{25,1}$. Then $e^\rho H(E)$ is antisymmetric under the Weyl group, so it is enough to describe the subspace whose degrees lie in the Weyl chamber of $II_{25,1}$. By the remarks at the end of section 4, this subspace is isomorphic to $\Lambda(\bigoplus_{i>0}\Lambda_i)$, where $\Lambda_i$ is a copy of the vector space of $\Lambda$ with degree $i\rho\in II_{25,1}$. The imaginary simple roots of $M_\Lambda$ are positive multiples of $\rho$, each of multiplicity 24, and are pairwise orthogonal; hence the required homology subspace is the exterior power of their root spaces.

## 13 The denominator formula for fake monster Lie algebras.

We can now calculate a twisted denominator formula for each element of$\operatorname { A u t } ( \hat { \Lambda } )$ which is often the denominator formula for some other Lie algebra or superalgebra. In this section we calculate a few examples of these Lie algebras.

We let $g$ be an element of $\operatorname{Aut}(\hat{\Lambda})=2^{24}\operatorname{Aut}(\Lambda)$ of order $N$, and let $L$ be the sublattice of $\Lambda$ fixed by $g$. The projection of $\Lambda$ into the vector space of $L$ is the dual lattice $L'$ because $\Lambda$ is unimodular. For simplicity, assume every power $g^n$ fixes all elements of $\hat{\Lambda}$ that lie over vectors of $\Lambda$ fixed by $g^n$. Without this assumption, most of the argument still works but keeping track of signs is harder. Lemma 12.1 provides many such elements, including every element of odd order.

We consider both sides of the formula

$$
\Lambda (E) = H (E)
$$

to be $L'$-graded virtual$g$modules. We calculate the trace of$g$on both sides, which can be thought of as an element of some completion of the group ring of$L ^ { \prime }$. We can calculate the trace of$g$on$\Lambda ( E )$provided we know exactly how$g$acts on$E$, and we can calculate the trace of$g$on$H ( E )$if we know exactly how$g$acts on the simple root spaces of$M _ { \Lambda }$

We first calculate the trace of$g$on$\begin{array} { r } { \Lambda ( E ) = \exp ( - \sum _ { i > 0 } \psi ^ { i } ( E ) / i ) } \end{array}$(where$\psi ^ { i }$are the Adams operations). This trace is equal to

$$
\exp (- \sum_ {v \in L ^ {\prime}} \sum_ {i > 0} \mathrm{Tr} (g ^ {i} | E _ {v}) e ^ {i v} / i)\tag{13.1}
$$

where $E_v$ is the subspace of $E$ whose $L'$-degree is $v$. (Note added May 1999: the published version of this formula incorrectly had a term $E_{iv}$ instead of $E_v$.) We wish to express the trace of $g$ in the form $\prod_r(1-e^r)^{\operatorname{mult}(r)}=\exp\left(-\sum_r\sum_{i>0}e^{ir}\operatorname{mult}(r)/i\right)$ for numbers $\operatorname{mult}(r)$. By applying the Moebius inversion formula to (13.1), as in section 11, we see that the numbers $\operatorname{mult}(r)$ are given by

$$
\operatorname{mult} (r) = \sum_ {d s | ((r, L), N)} \mu (s) \operatorname{Tr} \left(g ^ {d} \mid E _ {r / d s}\right) / d s\tag{13.2}
$$

where$( r , L )$is the highest common factor of the numbers$( r , a )$for$a \in L$

By Theorem 2.2 of [6], there is a reflection group $W^g$ acting on $L$, which may be taken as any of the following groups.

1 The subgroup of W of elements that commute with $g$.

2 The subgroup of$W$of elements that map$\rho$into$L$.

3 The subgroup of W of elements mapping L into $L$.

The positive roots of$W ^ { g }$are the vectors which are the sums of the conjugates of some positive real root of$I I _ { 25 , 1 }$. The simple roots of$W ^ { g }$are the sums of orbits of simple roots of$W$that have positive norm, and they are also the roots of$W ^ { g }$satisfying$( r , \rho ) = - r ^ { 2 } / 2$ so$\rho$is a norm 0 Weyl vector for$W ^ { g }$. (Warning:$W ^ { g }$is not always the full reflection group of$L . )$

From (13.2), any two positive vectors of $L'$ conjugate under $W^g$ have the same multiplicity. If $r$ is a real simple root of $W^g$, an easy calculation using (13.2) shows $\operatorname{mult}(r)=1$; therefore every positive real root of $W^g$ has multiplicity 1, since it is conjugate to a simple root. If $r$ has positive norm but is not a root of $W^g$, then $\operatorname{mult}(r)=0$.

The product

$$
e ^ {\rho} \prod_ {r \in L} (1 - e ^ {r}) ^ {\mathrm{mult} (r)}
$$

The product $e^\rho\prod_{r\in L}(1-e^r)^{\operatorname{mult}(r)}$ is therefore antisymmetric under the reflection group $W^g$, so it equals $\sum_{w\in W^g}\det(w)w(e^\rho S)$ for some $S$ with $e^\rho S$ in the Weyl chamber of $W^g$. (The determinant is that of $w$ as an automorphism of $L$, not of $\Lambda$.) This sum also equals the trace of $g$ on $e^\rho H(E)$ because it equals the trace of $g$ on $e^\rho\Lambda(E)$; hence $S$ is the trace of $g$ on the part of $H(E)$ in the Weyl chamber of $W^g$. This subspace is isomorphic to $\Lambda(\bigoplus_{i>0}\Lambda_i)$, where $\Lambda_i$ is a copy of the Leech lattice in degree $i\rho\in II_{25,1}$. Its trace is $e^{-\rho}\eta_g(e^\rho)$, where $\eta_g(q)=\eta(\epsilon_1q)\cdots\eta(\epsilon_{24}q)$ if $g$ has eigenvalues $\epsilon_1,\ldots,\epsilon_{24}$ on the Leech lattice. If $g$ has generalized cycle shape $a_1^{b_1}a_2^{b_2}\cdots$, then $\eta_g(q)=\eta(q^{a_1})^{b_1}\eta(q^{a_2})^{b_2}\cdots$. Therefore we get

$$
e ^ {\rho} \prod_ {r \in L} (1 - e ^ {r}) ^ {\mathrm{mult} (r)} = \sum_ {w \in W ^ {g}} \det (w) w (\eta_ {g} (e ^ {\rho})).\tag{13.3}
$$

The right hand side of this is exactly the denominator formula for a generalized Kac-Moody superalgebra with the following simple roots.

1 The real simple roots are the simple roots of the reflection group$W ^ { g }$, which are the roots r with$( r , \rho ) = - ( r , r ) / 2$

2 The imaginary simple roots are the positive multiples$i \rho$of the Weyl vector$\rho ,$with multiplicity equal to

$$
\operatorname{mult} (i \rho) = \sum_ {j a _ {k} = i} b _ {k}
$$

if$g$has generalized cycle shape$a _ { 1 } ^ { b _ { 1 } } a _ { 2 } ^ { b _ { 2 } } \ldots$.

Therefore the left hand side is the left hand side of the denominator formula for this generalized Kac-Moody superalgebra, so its positive roots have multiplicity mult(r).

## 14 Examples of fake monster Lie algebras.

We now evaluate both sides of the denominator formula (13.3) for several elements of $\operatorname{Aut}(\hat{\Lambda})$, obtaining examples of generalized Kac-Moody algebras whose simple roots and root multiplicities are known explicitly.

Example 1. The fake baby monster Lie algebra of rank 18. For this example we let $g \in \mathrm { A u t } ( \hat { \Lambda } )$be an element of order 2 which is the lift of an element of order 2 of$\operatorname { A u t } ( \Lambda )$ which fixes a 16 dimensional sublattice$\Lambda ^ { g }$of Λ, such that$g$fixes all elements of$\hat { \Lambda } ^ { g }$. By lemma 12.1 such an element$g$exists, and the lattice$\Lambda ^ { g }$is the Barnes-Wall lattice of dimension 16 and determinant$2 ^ { 8 } \ \mathrm { [ 12 ] }$. The root lattice L is the sum of$\Lambda ^ { g }$and the two dimensional even Lorentzian lattice$I I _ { 1 , 1 }$. The Barnes-Wall lattice$\Lambda ^ { g }$has no roots, so by theorem 3.1 of [6] the group$W ^ { g }$is the full reflection group of $L$.

We can calculate $\operatorname{mult}(r)$ explicitly. If $r\in L$ and $r\notin2L'$, then $\operatorname{mult}(r)=p_g(1-r^2/2)$. If $r\in2L'$, then $\operatorname{mult}(r)=p_g(1-r^2/2)+p_g(1-r^2/4)$; otherwise $\operatorname{mult}(r)=0$. Here $p_g(1+n)$ is the coefficient of $q^n$ in $1/\eta_g(q)=q^{-1}\prod_{i>0}(1-q^i)^{-8}(1-q^{2i})^{-8}=q^{-1}+8+44q+\cdots$. If $r\in L'$, then $\operatorname{Tr}(g|E_r)=0$ if $r\notin L$ and equals the coefficient of $q^{-r^2/2}$ in $1/\eta_g(q)$ if $r\in L$. The value of $\operatorname{Tr}(g^2|E_r)$ is $\dim E_r$, the coefficient of $q^{-r^2/2}$ in $\theta_{\Lambda^{g^\perp}+r^\perp}(q)/\Delta(q)$, where $\theta_{\Lambda^{g^\perp}+r^\perp}$ is the theta function of the coset $\Lambda^{g^\perp}+r^\perp$ and $r^\perp$ is chosen so that $r+r^\perp\in II_{25,1}$. If we substitute these values into the formula

$$
\operatorname{mult} (r) = \operatorname{Tr} (g | E _ {r}) - \operatorname{Tr} (g | E _ {r / 2}) / 2 + \operatorname{Tr} (g ^ {2} | E _ {r / 2}) / 2
$$

we find that mult(r) is equal to the coefficient of$q ^ { - r ^ { 2 } / 2 }$in

$$
\begin{array}{c} 0 \text {if} r \notin L \\ 1 / \eta_ {g} (q) \text {if} r \in L, r \notin 2 L ^ {\prime} \\ 1 / \eta_ {g} (q) + \theta_ {\Lambda^ {g \perp} + r ^ {\perp}} (q ^ {4}) / \Delta (q ^ {4}) \text {if} r \in 2 L ^ {\prime}, r \notin 2 L \\ 1 / \eta_ {g} (q) - 1 / \eta_ {g} (q ^ {4}) / 2 + \theta_ {\Lambda^ {g \perp}} (q ^ {4}) / \Delta (q ^ {4}) / 2 \text {if} r \in 2 L. \end{array}
$$

By Lemma 11.1, if $r\in2L'$, then $\operatorname{mult}(r)$ is the coefficient of $q^{-r^2/2}$ in $1/\eta_g(q)+1/\eta_g(q^2)$. Therefore the explicit product formula for the fake

baby monster Lie algebra is

$$
e ^ {\rho} \prod_ {r \in L ^ {+}} (1 - e ^ {r}) ^ {p _ {g} (1 - r ^ {2} / 2)} \prod_ {r \in 2 L ^ {\prime +}} (1 - e ^ {r}) ^ {p _ {g} (1 - r ^ {2} / 4)} = \sum_ {w \in W ^ {g}} \det (w) w (e ^ {\rho} \prod_ {i > 0} (1 - e ^ {i \rho}) ^ {8} (1 - e ^ {2 i \rho}) ^ {8})
$$

where $L$ is the Lorentzian lattice that is the sum of the Barnes-Wall lattice $\Lambda^g$ and the two-dimensional even Lorentzian lattice; $W^g$ is its reflection group with Weyl vector $\rho$, and $L'$ is the dual of $L$.

Example 2. We can construct a similar Lie algebra for any prime $p=2,3,5,7,11,$ or $23$ with $(p+1)|24$. Let $g\in\operatorname{Aut}(\hat{\Lambda})$ have order $p$ and correspond to an element of $M_{24}\subset\operatorname{Aut}(\Lambda)$ with cycle shape $1^{24/(p+1)}p^{24/(p+1)}$. We assume that the fixed lattice $\Lambda^g$ has dimension $48/(p+1)$, has no roots, and that if $r\in(\Lambda^{g^\perp})'$ then

$$
\theta_{\Lambda^{g^\perp}+r}(q)=\eta(q)^{24p/(p+1)}\left(\eta(q^p)^{-24/(p+1)}\delta(r\in\Lambda^{g^\perp})+\sum_{0\leq i<p}\epsilon^{-ipr^2/2}\eta(\epsilon^iq^{1/p})^{-24/(p+1)}\right)
$$

where $\epsilon$ is a primitive p’th root of 1 and where$\delta ( r \in \Lambda ^ { g \perp } )$is 1 if$r \in \Lambda ^ { g \perp }$and 0 otherwise. These assumptions are in principle not difficult to prove if they are true, as they are essentially just identities between modular forms. (For$p = 2$they are just lemma 12.1.)

Assuming these identities, an argument similar to the one above for$p = 2$shows that the denominator formula for the Lie algebra of G is

$$
\begin{array}{l} e^\rho\prod_{r\in L^+}(1-e^r)^{p_g(1-r^2/2)}\prod_{r\in pL^{\prime+}}(1-e^r)^{p_g(1-r^2/(2p))} \\ =\sum_{w\in W^g}\det(w)w\left(e^\rho\prod_{i>0}(1-e^{i\rho})^{24/(p+1)}(1-e^{pi\rho})^{24/(p+1)}\right)\end{array}
$$

where$\begin{array} { r } { \sum _ { i > 0 } p _ { g } ( 1 + i ) q ^ { i } = 1 / \eta _ { g } ( q ) } \end{array}$. For$p = 2 , 3 , 5 , 7$, and 11 these Lie algebras seem to correspond to the baby monster, the Fischer group$F i _ { 24 }$, the Harada Norton group, the Held group and the Mathieu group$M _ { 12 }$in the same way that the fake monster Lie algebra corresponds to the monster simple group.

Example 3. The fake Conway Lie superalgebra of rank 10. This is the algebra described at the end of section 2, and seems to correspond to Conway’s simple group $Co_1$. We let$g \in \mathrm { A u t } ( \hat { \Lambda } )$be an element of order 2 which is the lift of an element of order 2 of $\operatorname { A u t } ( \Lambda )$which fixes a lattice$\Lambda ^ { g }$of Λ of dimension 8. This lattice$\Lambda ^ { g }$is isomorphic to the $E _ { 8 }$lattice with all norms doubled, so if we halve all the norms of the lattice$\Lambda ^ { g } \oplus I I _ { 1 , 1 }$we get the nonintegral lattice of determinant$1 / 4$which is the dual of the sublattice of even vectors of$I_{9,1}$. A calculation similar to that in example 1 but using lemma 11.2 shows that the denominator formula of this Lie superalgebra is

$$
e ^ {\rho} \prod_ {r \in \Pi^ {+}} (1 - e ^ {r}) ^ {\mathrm{mult} (r)} = \sum_ {w \in W} \det (w) w (e ^ {\rho} \prod_ {n > 0} (1 - e ^ {n \rho}) ^ {(- 1) ^ {n} 8})
$$

where the multiplicity of the root$r = ( v , m , n ) \in L$is equal to

$$
\mathrm{mult} (r) = (- 1) ^ {(m - 1) (n - 1)} p _ {g} ((1 - r ^ {2}) / 2) = (- 1) ^ {m + n} | p _ {g} ((1 - r ^ {2}) / 2) |,
$$

and$p _ { g } ( n )$is defined by

$$
\sum p _ {g} (n) q ^ {n} = q ^ {- 1 / 2} \prod_ {n > 0} (1 - q ^ {n / 2}) ^ {- (- 1) ^ {n} 8}.
$$

## 15 Open questions

We list a few conjectures and open questions about the Lie algebras and superalgebras we have constructed.

(1) Prove the assumptions about the modular forms used in example 2 in section 14. In principle this should be easy (at least when they are true) because they just involve checking a finite number of identities between modular forms.

(2) Investigate the Lie algebras and superalgebras coming from other elements of the monster or$\operatorname { A u t } ( \Lambda )$and write down their denominator formulas explicitly in some nice form.

(3) Find a natural construction for these Lie algebras and superalgebras (i.e. other than by generators and relations). We used natural constructions for the monster Lie algebra and the fake monster Lie algebra from vertex algebras, but I do not know of any similar constructions for most of the other Lie algebras. The easiest case is the superalgebra of rank 10 which can be constructed from superstrings on a 10-dimensional torus. (The even part of the rank 10 superalgebra was constructed in [3, 4]; the odd part is more difficult to construct.) A natural construction should give actions of various finite groups on these Lie algebras; for example the double cover of the baby monster should act on the baby monster Lie algebra.

(4) Describe the Lie bracket from$V _ { a b } \otimes V _ { c d }$to$V _ { ( a + c ) ( b + d ) }$of the monster Lie algebra explicitly in terms of the vertex algebra operations on V.

(5) Is the baby monster Lie algebra a subalgebra of the monster Lie algebra in a way that preserves the action of the double cover of the baby monster? Similarly for the other monstrous Lie algebras.

(6) Are there any generalized Kac-Moody algebras, other than the finite dimensional, affine, monstrous or fake monstrous ones, whose simple roots and root multiplicities can both be described explicitly? The monstrous and fake monstrous algebras are both finite families, each with a few hundred members, corresponding roughly to the conjugacy classes in the monster and in$\operatorname { A u t } ( \hat { \Lambda } )$. One example of a denominator formula for a Lie superalgebra of rank 3 is the identity

$$
\sum_ {i + j + k = 0} (- p) ^ {j k} (- q) ^ {i k} (- r) ^ {i j} = \prod_ {i + j + k > 0} ((1 - p ^ {i} q ^ {j} r ^ {k}) / (1 + p ^ {i} q ^ {j} r ^ {k})) ^ {c (i j + j k + k i)}
$$

where$c ( i )$is defined by$\begin{array} { r } { \sum _ { n } c ( n ) q ^ { n } = \prod _ { n > 0 } ( 1 + q ^ { n } ) / ( 1 - q ^ { n } ) = 1 + 2 q + 4 q ^ { 2 } + 8 q ^ { 3 } + 14 q ^ { 4 } + . . . . } \end{array}$

(7) Find all completely replicable functions. (The ones with integral coefficients were found by computer in [1].) Are nontrivial completely replicable functions always modular functions of genus 0? A proof of this conjecture of Norton’s [28] which was not a case by case verification would be much neater than the argument in section 9.

(8) Is it possible to say anything interesting from Lie algebras constructed from the vertex algebras of lattices (other than the Leech lattice) as in section 6? The two obvious candidates are the lattices$E _ { 8 }$and$E _ { 8 }$⊕$E _ { 8 }$, so that the corresponding Lie algebras have root lattices$I I _ { 9 , 1 }$and$I I _ { 17 , 1 }$. The real simple roots of these Lie algebras are the Dynkin diagrams of the reflection groups of the lattices, which were described by Vinberg. There are some calculations connected with the Lie algebra of$I I _ { 9 , 1 }$in [24].

## References

[1]. D. Alexander, C. Cummins, J. McKay, C. Simons, Completely replicable functions, preprint.

[2]. M. F. Atiyah, K-theory, Benjamin, Inc. 1967.

[3]. R. E. Borcherds, Vertex algebras, Kac-Moody algebras, and the monster. Proc. Natl. Acad. Sci. USA. Vol. 83 (1986) 3068-3071.

[4]. R. E. Borcherds, Generalized Kac-Moody algebras. J. Algebra 115 (1988), 501–512.

[5]. R. E. Borcherds, Central extensions of generalized Kac-Moody algebras. J. Alg. 140, 330-335 (1991).

[6]. R. E. Borcherds, Lattices like the Leech lattice, J. Algebra, vol 130, No. 1, April 1990, 219-234.

[7]. R. E. Borcherds, J. H. Conway, L. Queen, N. J. A. Sloane, A monster Lie algebra?, Adv. Math. 53 (1984) 75-79. This paper is reprinted as chapter 30 of [12].

[8]. R. E. Borcherds, The monster Lie algebra, Adv. Math. Vol. 83, No. 1, Sept. 1990.

[9]. R. E. Borcherds, Vertex algebras, to appear.

[10]. H. Cartan, S. Eilenberg, Homological algebra, Princeton University Press 1956.

[11]. J. H. Conway, The automorphism group of the 26 dimensional even Lorentzian lattice. J. Algebra 80 (1983) 159-163. This paper is reprinted as chapter 27 of [12].

[12]. J. H. Conway, N. J. A. Sloane. Sphere packings, lattices and groups. Springer-Verlag New York 1988, Grundlehren der mathematischen Wissenschaften 290.

[13]. J. H. Conway, S. Norton, Monstrous moonshine, Bull. London. Math. Soc. 11 (1979) 308-339.

[14]. J. H. Conway, R. T. Curtis, S. P. Norton, R. A. Parker, R. A. Wilson, Atlas of finite groups, Clarendon Press, Oxford, 1985.

[15]. I. B. Frenkel, Representations of Kac-Moody algebras and dual resonance models, Applications of group theory in theoretical physics, Lect. Appl. Math. 21, A.M.S. (1985), p.325-353.

[16]. I. B. Frenkel, J. Lepowsky, A. Meurman, Vertex operator algebras and the monster, Academic press 1988.

[17]. I. B. Frenkel, J. Lepowsky, A. Meurman, A natural representation of the Fischer-Griess monster with the modular function J as character, Proc. Natl. Acad. Sci. USA 81 (1984), 3256-3260.

[18]. I. B. Frenkel, Y-Z. Huang, J. Lepowsky, On axiomatic formulations of vertex operator algebras and modules, preprint.

[19]. I. B. Frenkel, H. Garland, G. Zuckerman, Semi-infinite cohomology and string theory, Proc. Natl. Acad. Sci. U.S.A. 83 (1986), 8442-8446.

[20]. H. Garland and J. Lepowsky, Lie algebra homology and the Macdonald-Kac formulas, Invent. math. 34 (1976), p.37-76.

[21]. P. Goddard and C. B. Thorn, Compatibility of the dual Pomeron with unitarity and the absence of ghosts in the dual resonance model, Phys. Lett., B 40, No. 2 (1972), 235-238.

[22]. R. C. Gunning, Lectures on modular forms, Annals of mathematical studies, Princeton University Press, 1962.

[23]. V. G. Kac, “Infinite dimensional Lie algebras”, third edition, Cambridge University Press, 1990. (The first and second editions (Birkhauser, Basel, 1983, and C.U.P., 1985) do not contain the material on generalized Kac-Moody algebras that we need.)

[24]. V. G. Kac, R. V. Moody, M. Wakimoto, On E<sub>10</sub>, preprint.

[25]. M. Koike, On Replication Formula and Hecke Operators, Nagoya University preprint.

[26]. B. Kostant, Lie algebra cohomology and the generalized Borel-Weil theorem. Annals of Math. 74, 329-387 (1961).

[27]. K. Mahler, On a class of non-linear functional equations connected with modular functions, J. Austral. Math. Soc. 22A, (1976), 65-118.

[28]. S. P. Norton, More on moonshine, Computational group theory, Academic press, 1984, 185-193.

[29]. S. P. Norton, Generalized Moonshine, Proc. Symp. Pure Math. 47 (1987) p. 208-209.

[30]. J. P. Serre, A course in arithmetic. Graduate texts in mathematics 7, Springer-Verlag, 1973.

[31]. J. G. Thompson, A finiteness theorem for subgroups of PSL(2, R) which are commensurable with PSL(2, Z). Proc. Symp. Pure Math. 37 (1979) p. 533-555.
