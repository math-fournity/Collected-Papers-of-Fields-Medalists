# Superrigidity

# Inbo Gottlieb-Fenves

## 1 Statement and some Corollaries

Throughout, we assume that$K / \mathscr { R }$is an extension of fields, with k a local field of characteristic zero, and K algebraically closed.

Theorem 1.1 (Margulis Superrigidity). Let$G \leqslant \mathrm { S L } _ { n } ( \mathbb { R } )$be a semisimple algebraic group with$\mathbb { R } - \mathrm { r k } ( G ) \geq 2$ and no compact factors. Let$\Gamma \leqslant G$be an irreducible lattice. Let H be a simple noncompact R-algebraic group. Suppose$\pi \colon \Gamma \to H$is a homomorphism with πpΓq Zariski dense. Then π extends to a rational homomorphism $G  H$

## 2 Proof of Margulis Superrigidity for$\mathcal { k } = \mathbb { R }$

Proposition 2.1. Suppose$P < G$and$L < H$are proper algebraic R-subgroups, and there is a rational Γ-equivariant map ϕ:$G / P \to H / L$defined over R. Then π extends to a rational homomorphism$G  H$

Proof. Consider the graph-closure${ \mathcal { Z } } \subseteq G \times H$given by

$$
\mathcal {Z} = \overline {{\left\{\left(\gamma , \pi (\gamma)\right) : \gamma \in \Gamma \right\}}} ^ {\mathrm{Zar}}.
$$

We desire to show that$\mathcal { Z }$is the graph of a rational homomorphism. To see this, note first that$\Gamma \leqslant G$is Zariski dense by Borel density, and$\pi ( \Gamma ) \leqslant H$is dense by assumption. Thus, the projection maps of$\mathcal { Z }$onto each factor is surjective.

We claim that if$( g , h _ { 1 } ) , ( g , h _ { 2 } ) \in \mathcal { Z }$, then$h _ { 1 } = h _ { 2 }$. To see this, let$R = \operatorname { R a t } ( G / P , H / L )$be the space of rational maps$G / P \to H / L$. Then we have an action of$G \times H$on R given by

$$
[ (g, h) \cdot \phi ] (x) = h \phi (g ^ {- 1} x).
$$

Suppose$\phi \in R$is Γ-equivariant. Then

$$
[ (\gamma , \pi (\gamma)) \cdot \phi ] (x) = \pi (\gamma) \phi (\gamma^ {- 1} x) = \pi (\gamma) \pi (\gamma^ {- 1}) \phi (x) = \phi (x),
$$

so$\phi$is invariant under the action of the graph of π. As$\phi$is a rational map, the stabilizer of$\phi$is an R-algebraic subgroup containing the graph of π, thus$\mathcal { Z }$must stabilize ϕ. In particular, we have

$$
h _ {1} \phi (x) = \phi (g x) = h _ {2} \phi (x).
$$

Thus,$h _ { 1 } h _ { 2 } ^ { - 1 }$leaves$\phi ( G / P )$invariant pointwise, and since it acts algebraically, we have that$h _ { 1 } h _ { 2 } ^ { - 1 }$leaves ${ \overline { { \phi ( G / P ) } } } ^ { \mathrm { Z a r } }$invariant pointwise. At the same time, since$\pi ( \Gamma )$leaves$\phi ( G / P )$invariant, it also leaves${ \overline { { \phi ( G / P ) } } } ^ { \mathrm { Z a r } }$ invariant, and since$\pi ( \Gamma )$is Zariski dense in H, we have that H leaves${ \overline { { \phi ( G / P ) } } } ^ { \mathrm { Z a r } }$invariant, so in fact$\phi ( G / P )$ is Zariski dense in$H / L$, and so$h _ { 1 } h _ { 2 } ^ { - 1 }$fixes$H / L$. But then

$$
h _ {1} h _ {2} ^ {- 1} \in \bigcap_ {h \in H} h L h ^ {- 1},
$$

and since this is a proper normal subgroup of the simple group H, it follows that$h _ { 1 } = h _ { 2 }$

This implies that the projection map${ \mathcal { Z } } \to G$is in fact a bijective regular map, and so it has a rational inverse$\rho _ { 1 } \colon G \to \mathcal { Z }$. Letting$\rho _ { 2 } \colon { \mathcal { Z } } \to H$be the projection map, we see that$\rho _ { 2 } \rho _ { 1 } \colon G \to H$is a rational map which extends π. Moreover, it is a homomorphism on a Zariski dense subset, and so it is in fact a homomorphism.□

Now, let$P \leqslant G$be a minimal parabolic subgroup, i.e., the intersection in$\mathrm { S L } _ { n } ( \mathbb { R } )$of$G$with the subgroup of upper triangular matrices.

Proposition 2.2. There exists a proper algebraic R-subgroup$L < H$and a measurable Γ-equivariant map $\phi \colon G / P \to H / L$

Proof. Let$Q \textless H$be a proper parabolic subgroup defined over R. Then$H / Q$is a compact metrizable Γ-space. Consider the product space$G / P \times { \mathcal { M } } ( H / Q )$. Since$P$is minimal parabolic,$P$is solvable, hence amenable. As$\Gamma \leqslant G$is a closed subgroup, by amenability inheritance there exists a measurable Γ-equivariant section ϕ :$G / P \to \mathcal { M } ( H / Q )$

Since$Q \leqslant H$is R-cocompact, then a result of Zimmer states that H acts smoothly on$\mathcal { M } ( H / Q )$, i.e., the quotient$H \backslash { \mathcal { M } } ( H / Q )$is countably separated. Let$\bar { \phi } \colon G / P \to H \backslash \mathcal { M } ( H / Q )$be the induced map. As$\phi$is Γ-invariant (on a conull set), we have

$$
\bar {\phi} (\gamma x) = \pi (\gamma) \bar {\phi} (x) = \bar {\phi} (x),
$$

so$\bar { \phi }$is constant along Γ-orbits. But the codomain of$\bar { \phi }$is a countably separated space, and Γ acts on$G / P$ ergodically by the Howe-Moore vanishing theorem. Thus$\bar { \phi }$is a.e. constant, i.e.,$\phi$has essential range given by a single H-orbit$H \mu$. But the stabilizer L of$\mu$under the action of H is a proper algebraic R-subgroup. Again by smoothness, the map$H / L \to H \mu$is a homeomorphism, and so we may view$\phi$as a Γ-equivariant map$G / P \to H / L$, as desired.□

Proposition 2.3. Every measurable Γ-equivariant map$\phi \colon G / P \to H / L$is rational.

The proof of this proposition is by far the most dificult step in the proof, and proceed via a series of reductions. To start, we will lift$\phi$to a right P-invariant map$G  H / L$. We also let$U$denote the intersection of$G$in$\mathrm { S L } _ { n } ( \mathbb { R } )$with the subgroup of unipotent lower triangular matrices.

A rational function$U \to H / L$then defines a$P -$-invariant function$U \times P \to H / L .$, which in turn defines a map$G / P \to H / L$. Thus, if$\phi | _ { U }$is rational, then$\phi$is rational.

We have another black box from Lie theory:

Lemma 2.4. Suppose G has R-rank at least 2. There exist nonidentity elements$t _ { 1 } , . . . , t _ { n } \in A$and connected algebraic unipotent subgroups$U _ { i }$so that

(i) for each$i , U _ { i }$is contained in a semisimple R-group$C _ { i }$of elements centralizing$t _ { i } ;$

(ii) the product map$U _ { 1 } \times \cdots \times U _ { n } \to U$is an R-isomorphism of varieties;

(iii) for each$r , U _ { 1 } \cdots U _ { r }$is a subgroup of$U$, and is normal in$U _ { r + 1 }$

In the case of$\mathrm { S L _ { 3 } ( \mathbb { R } ) }$, we can take for example

$$
t _ {1} = \left[ \begin{array}{c c c} \lambda & & \\ & \lambda & \\ & & \lambda^ {- 2} \end{array} \right], \quad U _ {1} = \left[ \begin{array}{c c c} 1 & & \\ \mathbb {R} & 1 & \\ & & 1 \end{array} \right], \quad C _ {1} = \left[ \begin{array}{c c} \mathrm{GL} _ {2} (\mathbb {R}) & \\ & \det ^ {- 1} \end{array} \right],
$$

and similarly for the other elements. Note that this decomposition is not possible for$\operatorname { S L _ { 2 } } ( \mathbb { R } )$, and the higher rank condition is essential for the general proof.

Lemma 2.5. If, for$a . e . \ g \in G$and each$i ,$the map$U _ { i } \to H / L , u \mapsto \phi ( g u )$is essentially rational, then ϕ|<sub>U</sub> is essentially rational.

Proof. we induct on the following claim: for almost all$g \in G$, the map$u \mapsto \phi ( g u )$is rational on$U _ { 1 } \cdots U _ { r }$ When$r = 1$, this is exactly the assumption of the lemma. Suppose then that the statement holds for a.e. $g \in G$on$U _ { 1 } \cdots U _ { r }$. Choose$u \in U _ { 1 } \cdots U _ { r }$and$v \in U _ { r + 1 }$. For each$^ { g , }$consider the function

$$
\phi_ {g} (u, v) = \phi (g u v).
$$

By assumption, for each$u ,$this map is a.e. rational in$v ,$and so by Fubini’s theorem, for a.e.$g , \phi _ { g }$is rational in v for a.e. u. On the other hand, we have$\phi _ { g } ( u , v ) = \phi ( g v ( v ^ { - 1 } u v ) )$, and since v normalizes$\bar { U } _ { 1 } \cdots U _ { r }$, it follows that$\phi _ { g }$is also essentially rational in u for a.e. g. But then$\phi _ { g }$is essentially rational in both the u and v factor for a.e.$g .$This in turn implies that$\phi _ { g }$is essentially rational on$U _ { 1 } \cdots U _ { r + 1 }$, completing the induction.□

Lemma 2.6. Suppose that for each$1 \leqslant i \leqslant n$, there exists a measurable map$h \colon G \to H$(perhaps depending on$i )$so that$\phi ( g c ) = h ( g ) \phi ( c )$for$a . e . \ c \in C _ { i }$and$g \in G$, then$\phi | _ { U }$is rational.

Proof. Let B denote the subgroup of H fixing$C _ { i }$pointwise. Note that this subgroup is algebraic, as it is the intersection of stabilizers.

First, we show that im h normalizes B. Given$b \in B$and$c , c ^ { \prime } \in C _ { i }$, we have

$$
[ h (c) ^ {- 1} b h (c) ] \phi (c ^ {\prime}) = h (c) ^ {- 1} b \phi (c c ^ {\prime}) = h (c) ^ {- 1} \phi (c c ^ {\prime}) = \phi (c ^ {\prime}),
$$

This shows im h normalizes$B .$

Now, consider the induced map$\bar { h } \colon C _ { i } \to N _ { G } ( B ) / B$given by projection. We claim$\bar { h }$is a homomorphism. To see this, choose$c , c ^ { \prime } , c ^ { \prime \prime } \in C _ { i }$. We have

$$
h (c c ^ {\prime}) \phi (c ^ {\prime \prime}) = \phi (c c ^ {\prime} c ^ {\prime \prime}) = h (c) h (c ^ {\prime}) \phi (c ^ {\prime \prime}),
$$

and so$h ( c c ^ { \prime } ) ^ { - 1 } h ( c ) h ( c ^ { \prime } ) \in B$, proving that$\bar { h }$is a homomorphism.

Finally, recall that$C _ { i }$is semisimple, so the image of$U _ { i }$under$\bar { h }$is unipotent by automatic unipotence, and hence the restriction of$\bar { h }$to$U _ { i }$is rational by automatic rationality. Thus, for each$u \in U _ { i }$, we have

$$
\phi (g u) = h (g) \phi (u) = h (g) \bar {h} (u) \phi (1).
$$

But this map is rational for fixed$^ { g , }$and so$\phi | _ { U _ { i } }$is rational, as desired.

Proposition 2.7. Any Γ-equivariant measurable map ϕ:$G / P \to H / L$is rational.

Proof. Abusing notation, instead let ϕ denote the P-invariant map$G  H / L$. Let$\mathcal { F } ( C _ { i } , H / L )$denote the space of measurable maps$C _ { i } \to H / L$, modulo a.e. equivalence. Consider the function$\Phi \colon G \to { \mathcal { F } } ( C _ { i } , H / L )$ given by

$$
\Phi (g) (c) = \phi (g c).
$$

Then, for each$t _ { i } .$, as$C _ { i }$centralizes$t _ { i }$and$\phi$is$P -$-invariant, we have

$$
\Phi (g t _ {i}) (c) = \phi (g t _ {i} c) = \phi (g c t _ {i}) = \phi (g c) = \Phi (g) (c)
$$

for all$c \in C _ { i } .$Let$T _ { i }$denote the one-parameter subgroup of A containing$t _ { i }$. As ϕ is Γ-equivariant, the map $\bar { \Phi } \colon G / T _ { i } \to H \backslash \mathcal { F } ( C _ { i } , H / L )$is constant along Γ-orbits. But$T _ { i }$is noncompact, so Γ acts on$G / T _ { i }$ergodically by Howe-Moore. Moreover, H acts on$\mathcal { F } ( C _ { i } , H / L )$smoothly (since$C _ { i }$is σ-finite and$H / L$is an R-variety on which H acts by regular maps). Thus ergodicity of Γ implies that$\bar { \Phi }$is essentially constant, i.e., the function

$$
\Phi (g) (c) = H \phi (g c)
$$

is essentially constant in$g .$In particular, we must have$\phi ( g c ) = h ( g ) \phi ( c )$for some function$h \colon G \to H$. This finishes the proof.□

## 3 Required Results

Theorem 3.1 (Howe-Moore Vanishing Theorem). Suppose G is a semisimple connected Lie group with finite center and no compact factors. If$H \leqslant G$is a closed, noncompact subgroup, and$\Gamma \leqslant G$is a lattice, then Γ acts ergodically on$G / H$

Theorem 3.2 (Smoothness of Actions). Suppose H is k-group.

(i) Suppose Q is a k-cocompact algebraic subgroup in H. Then$H _ { \hbar }$acts smoothly on$\mathcal { M } ( H _ { \mathcal { R } } / Q _ { \mathcal { R } } )$

(ii) Suppose V is a k-variety, and H acts k-regularly on V. Then for any σ-finite measure space X, the $H _ { \hbar }$acts smoothly on${ \mathcal { F } } ( X , V _ { \mathbb { R } } )$

Theorem 3.3 (Borel Density). Suppose G is a connected semisimple algebraic R-group with no compact factors. Then any lattice in G is Zariski dense.

Theorem 3.4 (Amenability Inheritance). Suppose G is a locally compact group, and$\Gamma , H \leqslant G$are closed subgroups. If H is amenable, then the Γ action on$G / H$is amenable.

Theorem 3.5 (Automatic Rationality). Suppose U is an unipotent R-group and$\pi \colon U \to \mathrm { G L } _ { n } ( \mathbb { R } )$is a measurable homomorphism with unipotent image. Then π is a regular map.

Proof. By conjugating (which is a regular map), we may assume U is a subgroup of the group$N _ { m }$, the unipotent upper triangular matrices in${ \mathrm { G L } } _ { m } ( \mathbb { R } )$. If we let${ \mathfrak { n } } _ { m }$denote the Lie algebra of N, then the exponential map exp:${ \mathfrak { n } } _ { m } \to N _ { m }$given by

$$
\exp (g) = \sum_ {k = 0} ^ {\infty} \frac {g ^ {k}}{k !}
$$

is in fact a regular map, since a P n is nilpotent (and so the sum is zero after m terms). Moreover, exp has an inverse log :$N _ { m } \to \mathfrak { n } _ { m }$given by

$$
\log (g) = \sum_ {k = 0} ^ {\infty} (- 1) ^ {k} \frac {(g - \mathrm{id}) ^ {k}}{k !},
$$

which is again a regular map. Thus, if u is the Lie algebra of U, then$\exp \colon \mathfrak { u }  U$defines a biregular R-isomorphism of varieties.

As π is a measurable homomorphism, it is automatically continuous, hence automatically smooth. Let dπ :$\mathfrak { u } \to \mathfrak { g l } _ { n } ( \mathbb { R } )$denote the derivative of π at the identity; since π has unipotent image, the codomain of dπ may be taken to be the Lie algebra${ \mathfrak { n } } _ { n }$. Then we have a commutative diagram

$$
\begin{array}{c} U \xrightarrow {\pi} N _ {n} \\ \log \Biggl \downarrow \\ \mathfrak {u} \xrightarrow {d \pi} \mathfrak {n} _ {n} \end{array} \Bigg | _ {\text {exp}}
$$

But log and exp are regular and dπ is linear, hence π is regular.

Proposition 3.6 (Automatic Unipotence). Let$G \leqslant \mathrm { G L } _ { m } ( \mathbb { R } )$be a semisimple Lie group and suppose that $\pi \colon G \to \mathbf { G L } _ { n } ( \mathbb { R } )$is a measurable representaion.$I f U \subseteq G$is a connected unipotent subgroup, then$\pi | _ { U }$is a unipotent representation, i.e., π has unipotent image.

Proposition 3.7 (A.e. Rationality). Suppose$f \colon \mathbb { R } ^ { m } \times \mathbb { R } ^ { n } \to V$is a measurable function so that, for a.e. x,$y \mapsto f ( x , y )$is essentially rational, and for a.e.$y , x \mapsto f ( x , y )$is essentially rational, then f is essentially rational.

Proof. It sufices to show the statement for$m = n = 1$, and we may additionally assume that the maps are rational rather than just essentially rational by Fubini’s theorem. Suppose we knew that$f$agreed with a rational function$\phi$on a set$A \times \mathbb { R }$, where$A \subseteq \mathbb { R }$were a set of positive measure. But then

$$
0 = \int_ {A \times \mathbb {R}} | f - \phi | = \int_ {\mathbb {R}} \left[ \int_ {A} | f (x, y) - \phi (x, y) | d x \right] d y.
$$

But then$f ( \cdot , y ) = \phi ( \cdot , y )$a.e. on A for a.e. y. As$f ( \cdot , y )$is assumed to be rational,$f ( \cdot , y ) = \phi ( \cdot , y )$a.e. on R for a.e. y, which in turn implies$f = \phi \ \mathrm { a . e }$

Let$A _ { r , s }$denote the set of points$x _ { 0 } \in \mathbb { R }$so that$f ( x _ { 0 } , \cdot )$is, in lowest terms, of the form$P ( y ) / Q ( y )$, where $P$is of degree r and$Q$is of degree s. Note that one of these sets has positive measure; set$A = A _ { r , s }$with positive measure. Then, for$x \in A$, we have

$$
f (x, y) = \frac {y ^ {r} + \sum_ {i = 0} ^ {r - 1} a _ {i} (x) y ^ {i}}{\sum_ {i = 0} ^ {s} b _ {i} (x) y ^ {i}}.
$$

It thus sufices to show that the functions$a _ { i } , b _ { i }$are essentially rational. However, if we let$\lambda _ { 1 } , . . . , \lambda _ { r + s + 1 } \in ]$R denote a set such that, for each$j , f ( \cdot , \lambda _ { j } )$is essentially rational; then the$a _ { i } , b _ { i }$are solutions to the system of equations

$$
f _ {\lambda_ {j}} (x) = \frac {\lambda_ {j} ^ {r} + \sum_ {i = 0} ^ {r - 1} a _ {i} (x) \lambda_ {j} ^ {i}}{\sum_ {i = 0} ^ {s} b _ {i} (x) \lambda_ {j} ^ {i}}.
$$

This is a system of equations over the field$\mathbb { C } ( x )$with$r + s + 1$variables and$r + s + 1$equations, thus it has a unique solution, which is rational in x by Cramer’s rule.□

## 4 Superrigidity over General Fields

Note that the only place in which we used that H was an algebraic R-group was in the proof of Proposition 2.2., where we used the fact that L was an algebraic R-group. For general local fields k this is not true; we instead have the following result:

Proposition 4.1. Suppose H is a connected k-group, almost simple over$\mathcal { k }$, and that$Q < H$is a proper k-cocompact subgroup. Then for any$\mu \in \mathcal { M } ( H _ { \mathcal { k } } / Q _ { \mathcal { k } } )$, either

(i) the stabilizer$\left( H _ { \hbar } \right) _ { \mu }$of µ in$H _ { \hbar }$is compact, or;

(ii) there is an algebraic k-group$L < G$with dim L ă dim G and$L _ { \mathcal { k } } \supseteq ( H _ { \mathcal { k } } ) _ { \mu }$

Note that condition (ii) is suficient to conclude the same result as in proposition 2.2, as we then have a continuous Γ-equivariant surjection$H _ { \mathbb { R } } \mu \to H _ { \mathbb { R } } / L _ { \mathbb { R } } ;$: by smoothness the natural map$H _ { \hbar } \mu \to H _ { \hbar } / ( H _ { \hbar } ) _ { \mu }$ is a homeomorphism and$L _ { \mathcal { k } }$is a proper closed subgroup containing$\left( H _ { \hbar } \right) _ { \mu }$, and all maps are obviously Γ- equivariant, so we again obtain a map$G / P \to H _ { \hbar } / L _ { \hbar }$. Thus, either (i) holds or the rest of the proof follows in the same way and we get Margulis superrigidity.

Proposition 4.2. Suppose Γ is a locally compact group,$( X , \mu )$is a quasi-invariant Γ-space with quasi-invariant measure, and the action of Γ on X is weak mixing. Let$\pi \colon \Gamma  H$be a homomorphism with H also locally compact, and suppose there exists a measurable Γ-equivariant map$\phi \colon X \to H / K$, where$K \leqslant H$ is a compact subgroup. Then$\overline { { \pi ( \Gamma ) } }$is compact.

Proof. Without loss of generality, we may choose µ to be a probability measure on$X$, so that$\nu = \phi _ { * } \mu$is a probability measure on$H / K$. The map$\phi \times \phi \colon X \times X \to H / K \times H / K$is still Γ-equivariant; moreover, since the action of Γ is weak mixing,$\mu \times \mu$is ergodic, and so ν ˆ ν is ergodic. Now, the action of K on H is smooth by compactness of K, and hence the action of H on$H / K \times H / K$is smooth. Therefore, the induced map $\bar { \phi } \colon X \times X \to H \backslash ( H / K \times H / K )$is Γ-invariant, and since the quotient space is countably separated, it follows that the map is essentially constant, and so$\nu \times \nu$is supported on an H-orbit$\mathcal { O } = H ( u , v )$. By Fubini’s theorem, there must exist$x \in H$so that ν is supported on the slice$E _ { x } = \{ y K \in H / K : ( x K , y K ) \in \theta \}$

Suppose$y K , y ^ { \prime } K \in E _ { x }$. Then there exist$h , h ^ { \prime } \in H$so that

$$
(x K, y K) = (h u K, h v K) \quad \text { and } \quad (x K, y ^ {\prime} K) = (h ^ {\prime} u K, h ^ {\prime} v K).
$$

Thus$h ^ { - 1 } h ^ { \prime } \in u K u ^ { - 1 }$, and so there exists$k \in \ K$so that$y K = h v K = u k u ^ { - 1 } h ^ { \prime } v K = u k u ^ { - 1 } y ^ { \prime } K$. In particular, the set$E _ { x }$is$\mathrm { ~ a ~ } u K u ^ { - 1 }$-orbit in$H / K ;$since K is compact, so is$u K u ^ { - 1 }$, and orbits of compact groups are compact, so$E _ { x } \subseteq H / K$is compact. In other words, supp ν is compact. But ν is quasi-invariant with respect to$\pi ( \Gamma )$, and so$\pi ( \Gamma )$leaves supp ν invariant. Lifting to$H ,$we see that$\pi ( \Gamma )$leaves a compact set$B \subseteq H$invariant under translation. Thus$\pi ( \Gamma ) \subseteq B B ^ { - 1 }$, and so$\overline { { \pi ( \Gamma ) } }$is compact.□

Theorem 4.3 (The Case$\mathcal { k } = \mathbb { C } )$. Let$G \leqslant \mathrm { S L } _ { n } ( \mathbb { R } )$be a semisimple algebraic group with$\mathbb { R } - \mathrm { r k } ( G ) \geq 2$and no compact factors. Let$\Gamma \leqslant G$be an irreducible lattice. Let H be a simple noncompact C-algebraic group. Suppose$\pi \colon \Gamma  H _ { \mathbb { C } }$is a homomorphism with$\pi ( \Gamma )$Zariski dense. Then either$\overline { { \pi ( \Gamma ) } } \leqslant H _ { \mathbb { C } }$is compact in the Hausdorf topology or π extends to a rational homomorphism$G \to H _ { \mathbb { C } }$

Proof. By Howe-Moore, the action of Γ on$G / P$is weak mixing. Suppose condition (i) holds in Proposition 4.1. As in the proof of Proposition 2.2., we obtain a measurable Γ-equivariant map ϕ :$G / P \to H _ { \mathbb { C } } / ( H _ { \mathbb { C } } ) _ { \mu } .$ By the assumption that the stabilizer of$\mu$is compact, Proposition 4.2 states that$\overline { { \pi ( \Gamma ) } }$is compact.□

Theorem 4.4 (The Case of k Nonarchimedean). Let$G \leqslant \mathrm { S L } _ { n } ( \mathbb { R } )$be a semisimple algebraic group with $\mathbb { R } - \operatorname { r k } ( G ) \geq 2$and no compact factors. Let$\Gamma \leqslant G$be an irreducible lattice. Let H be a simple noncompact k-algebraic group, for k a non-Archimedean local field. Suppose$\pi \colon \Gamma  H _ { \mathcal { k } }$is a homomorphism with$\pi ( \Gamma )$ Zariski dense. Then$\overline { { \pi ( \Gamma ) } } \leqslant H _ { \mathcal { k } }$is compact.

Proof. By Propositions 4.1 and 4.2, it sufices to show that (ii) cannot occur. Suppose for sake of contradiction that, as in Proposition 4.1, there were to exist an algebraic k-group$L < G$with dim$L <$dim G such that $L _ { \mathcal { k } } \subseteq ( H _ { \mathcal { k } } ) _ { \mu }$. Then as in Proposition 2.2, there exists a Γ-invariant measurable map$\phi \colon G / P \to H / L$. The rest of the proof of superrigidity does not depend on the local field k that is chosen; at the same time, the maps$\phi | _ { U _ { i } }$as in the proof are then continuous maps from a connected set into a totally disconnected set, thus they must be constant. It then follows that$\phi | _ { U }$is constant, hence after identifying U with$G / P ,$we see that the rational map$\phi$we have constructed is in fact constant. However, Γ-equivariance implies that$\pi ( \Gamma )$ is contained in some conjugate of$L _ { \mathcal { k } }$, which contradicts Zariski density.□