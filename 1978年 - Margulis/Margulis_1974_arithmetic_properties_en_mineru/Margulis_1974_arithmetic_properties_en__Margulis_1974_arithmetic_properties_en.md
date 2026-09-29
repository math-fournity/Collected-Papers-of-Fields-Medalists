to Israil Moiseevich Gel'fand
on his sixtieth birthday

# ARITHMETIC PROPERTIES OF DISCRETE SUBGROUPS $^{1}$

## G. A. Margulis

That the factor space of a semisimple Lie group by an arithmetic subgroup has finite volume with respect to Haar measure is well known. In this paper we study results related to the converse of this theorem. In particular, under some rather weak assumptions on a semisimple Lie group G we prove that every discrete subgroup of G with a non-compact factor space of finite volume that satisfies some natural irreducibility conditions, is an arithmetic subgroup of G. In this paper we also study various results from the theory of algebraic groups and their arithmetic and discrete subgroups. In the proof of one theorem we use a construction from representation theory that is of independent interest. At the end we state some unsolved problems in the theory of discrete subgroups.

## Contents

Introduction 108  
§ 0. Notation and terminology 112  
§ 1. The intersections of discrete subgroups with normal subgroups 113  
§ 2. Some preliminary information 115  
§ 3. Unipotent discrete subgroups 116  
§ 4. Some information from the theory of algebraic groups and their arithmetic subgroups 118  
§ 5. Unipotent subgroups of $\Gamma$ and subgroups associated with them 122  
§ 6. Horosphericity of the maximal unipotent subgroups of $\Gamma$ 125  
§ 7. Opposite horospherical subgroups and their intersections with $\Gamma$ 126  
§ 8. A construction from representation theory 130  
§ 9. Proof of the "rationality" theorem 133  
§ 10. Proof of the main theorem 138  
§ 11. $p$-adic and adelic points of algebraic groups 139  
§ 12. Unipotent elements in $\Gamma$ and $G_{Z}$ 142  
§ 13. Some auxiliary results 142  
§ 14. Groups $G$ of Q-rank $\geqslant 2$ 145  
§ 15. Groups of Q-rank 1 146  
§ 16. Groups of Q-rank 1 (conclusion) 150  
§ 17. Some unsolved problems of the theory of discrete subgroups 152  
Appendix. Properties of root decompositions 152  
References 153

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  This paper is an expanded version of a lecture given by the author at the meeting of the Moscow Mathematical Society on 23 April 1973.</span></small>

## Introduction

1. In the 1880's Klein and Poincaré discovered that the classification of Riemann surfaces of genus greater than 1 reduces to that of the discrete subgroups of the group of real unimodular matrices of order two [43]. The group $SL_{2}(\mathbf{R})$ acts on the upper half-plane $X = \{z; \operatorname{Im} z > 0\}$ by the formula

$$
z \rightarrow g z = \frac {a z + c}{b z + d}, \text {   where   } g = \left(\begin{array}{c c}a&b\\c&d\end{array}\right).
$$

It turns out that for any Riemann surface M, except for some very simple cases, $^{1}$ there is a discrete subgroup of $SL_{2}(\mathbf{R})$ (more accurately, of the factor group $SL_{2}(\mathbf{R})/\pm E$), defined up to conjugacy and acting on X without fixed points, such that $X/\Gamma$ as a Riemann surface is isomorphic to M. It is clear that compact Riemann surfaces correspond to discrete subgroups $\Gamma$ such that $SL_{2}(\mathbf{R})/\Gamma$ is compact. But if M is obtained from a compact Riemann surface by deleting finitely many points (and is not a sphere with one or two points deleted), then, although the factor space $SL_{2}(\mathbf{R})/\Gamma$ is not compact, it has finite volume with respect to the invariant measure on $SL_{2}(\mathbf{R})$. Conversely, if $\Gamma$ is a discrete subgroup of $SL_{2}(\mathbf{R})$, acting without fixed points on X and such that $SL_{2}(\mathbf{R})/\Gamma$ has finite volume, then $X/\Gamma$ is obtained from the compact Riemann surface M by deleting finitely many points. We see that the group $SL_{2}(\mathbf{R})$ has very many different discrete subgroups with compact factor space, and also very many whose factor space is not compact, yet has finite volume. In fact, there exists a $(6g-6)$-dimensional family of non-isomorphic Riemann surfaces of genus g. Since each of them corresponds to a discrete subgroup of $SL_{2}(\mathbf{R})$, there exists a $(6g-6)$-dimensional family of pairwise non-conjugate discrete subgroups of $SL_{2}(\mathbf{R})$, each of which is isomorphic to the fundamental group of a compact Riemann surface of genus g. Similarly, by considering families of Riemann surfaces with deleted points, we see that there are families $\{\Gamma_{t}\}$ of pairwise non-conjugate discrete subgroups such that the factor space $SL_{2}(\mathbf{R})/\Gamma_{t}$ is not compact, but has finite volume.

Now let G be a simple Lie group. A natural question arises: Does G have discrete subgroups  $\Gamma$  such that  $G/\Gamma$  is compact or has finite volume, and how many such subgroups are there? When  $G = SL_{n}(\mathbf{R})$  is the group of real unimodular matrices of order n, there is the natural discrete subgroup  $SL_{n}(\mathbf{Z})$  consisting of the integral matrices in  $SL_{n}(\mathbf{R})$ . The factor space  $SL_{n}(\mathbf{R})/SL_{n}(\mathbf{Z})$  can be interpreted as the space of lattices with determinant 1 in an n-dimensional (Euclidean) space. Hence it is not compact. As was, in fact, proved by Hermite, the factor space  $SL_{n}(\mathbf{R})/SL_{n}(\mathbf{Z})$  has finite volume ([41], [7], [21]). This discrete subgroup  $SL_{n}(\mathbf{Z})$  is the simplest

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1 Namely, the complex plane, the plane without points, the extended plane, and the torus.</span></small>

example of an arithmetic subgroup. In order to give a general definition of an arithmetic subgroup we must introduce some concepts. A linear algebraic group (or simply an algebraic group) is an algebraic subgroup of the group  $GL_{n}$  of invertible  $n \times n$ -matrices. We recall that an algebraic subgroup G is defined by giving a system of polynomial equations  $\{P_{l}(x_{ij})\}$  in the coefficients of a matrix such that the quotient of any pair of matrices satisfying the system  $\{P_{l}\}$  also satisfies this system. We say that an algebraic group G is defined over the field of rational numbers (or simply that G is a Q-group) if the polynomials  $P_{l}$  defining G have rational coefficients. In this case we denote by  $G_{R}$  (respectively, by  $G_{Z}$ ) the set of real (respectively, integral) solutions of the system of equations  $\{P_{l}\}$ ; by definition,  $G_{R}$  is a subgroup of  $GL_{n}(R)$ . We say that a Q-group G is semisimple if its set of real points  $G_{R}$  is a semisimple Lie group.  $G_{Z}$  is an arithmetic subgroup of  $G_{R}$ . Any discrete subgroup  $\Gamma$  of  $G_{R}$  whose intersection with  $G_{Z}$  is of finite index in both  $\Gamma$  and  $G_{Z}$  is also called an arithmetic subgroup. To state the main property of arithmetic subgroups we make the following definition. Let H be a Lie group. A discrete subgroup  $\Gamma$  of H is said to be a lattice if the factor space  $H/\Gamma$  has finite volume. A lattice is uniform if  $H/\Gamma$  is compact, and non-uniform otherwise. The following fundamental result holds ([7], [42]). Suppose that G is a semisimple algebraic Q-group and  $\Gamma$  an arithmetic subgroup of G. Then  $\Gamma$  is a lattice in  $G_{R}$, and  $\Gamma$  is uniform if and only if  $\Gamma$  contains no unipotent elements.

We give another definition. A lattice  $\Gamma$  in a Lie group H is said to be irreducible if for any continuous epimorphism  $f: H \to F, 0 < \dim F < \dim H$ , the subgroup  $f(\Gamma)$  is not discrete in F.

For a long time there were no examples of non-arithmetic irreducible lattices in semisimple Lie groups other than $^{1}$$SL_{2}(\mathbb{R})$ . This led to the conjecture, first expressed by A. Selberg, that if  $H \neq SL_{2}(\mathbb{R})$  is a semisimple Lie group, then any irreducible lattice  $\Gamma$  in H is an arithmetic subgroup (when  $\Gamma$  is uniform, we must use a more general definition of arithmetic subgroup than the one given above (see §17.3)). $^{2}$  Selberg [39] obtained the first result towards a proof of this conjecture, by proving that any uniform lattice in  $SL_{n}(\mathbb{R})$  is conjugate to a subgroup consisting of matrices with algebraic coefficients. Later, André Weil [40] generalized Selberg's result on irreducible uniform lattices to an arbitrary semisimple Lie group. We mention that although at first sight these results seem to be equivalent to the arithmeticity conjecture, this impression is wrong. Selberg's results are based on the following important rigidity theorem.

WEAK RIGIDITY THEOREM. Let $H \neq SL_2(\mathbb{R})$ be a semisimple Lie group without compact factors, and $\Gamma \xrightarrow{i} H$ an irreducible uniform lattice

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1 Strictly speaking, "not locally isomorphic to".</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2 Selberg himself stated this conjecture for non-uniform lattices only. The general statement is due to I. I. Pyatetskii-Shapiro [28], [35].</span></small>

in H. Then any homomorphism  $i'$ :  $\Gamma \to H$  close to i has the form  $i'(\gamma) = hi(\gamma)h^{-1}$ , where h is some element of H independent of  $\gamma$ .

Mostow (in a lecture at the Nice congress [48] and [48a]), on the basis of his important ideas on the extension of isomorphisms of discrete subgroups to compactifications of symmetric spaces, has obtained the following result.

STRONG RIGIDITY THEOREM. $^{1}$  Let H and  $H'$  be semisimple Lie groups with trivial centre and without compact factors, and not equal to  $SL_{2}(\mathbf{R})/\pm E$ , and let  $\Gamma$  and  $\Gamma'$  be irreducible uniform lattices in H and  $H'$ . Then any isomorphism  $\varphi\colon\Gamma\to\Gamma'$  extends to a continuous homomorphism of H into  $H'$ .

For the case of non-uniform lattices and under the assumption that the R-rank of H (that is, the dimension of a maximal R-split torus) is greater than 1, this theorem was proved by the present author [29] using a method completely different from that of Mostow. In a recent paper [49] Prasad has shown that Mostow's method is also applicable to the case of non-uniform lattices if the R-rank of H is assumed to be equal to 1.

The rigidity theorem shows that if H is a semisimple Lie group other than  $SL_{2}(\mathbb{R})$ , then H contains no families of irreducible uniform lattices. However, Makarov [34] and Vinberg [33] have shown that there exist non-arithmetic lattices, both uniform and non-uniform, in the groups of motions of 3-, 4-, and 5-dimensional Lobachevskii spaces. This shows that for Selberg's conjecture on the arithmeticity of lattices to hold, we must put some additional restrictions on the semisimple group H (apart from  $H \neq SL_{2}(\mathbb{R})$ ). Various authors (in particular, Selberg himself [15]) have suggested the following condition A on H: the rank of the symmetric space associated with H is greater than 1. It turns out that condition A on H guarantees the validity of Selberg's conjecture for irreducible non-uniform lattices. Namely, we have the following main theorem. $^{2}$

MAIN THEOREM. Let G be a connected semisimple algebraic R-group without compact factors and with trivial centre, of R-rank greater than 1, and let  $\Gamma$  be an irreducible non-uniform lattice in  $G_{R}$ . Then  $\Gamma$  is an arithmetic subgroup of G. More accurately, G can be given a Q-structure such that the groups  $\Gamma$  and  $G_{Z}$  are commensurable.

The main theorem together with the above-mentioned theorem on the finiteness of the volume of the factor space  $G_{R}/G_{Z}$  gives a classification up to commensurability of all the non-uniform lattices in G. The main theorem can be rephrased in the language of symmetric spaces (see [15] and [31] for the necessary definitions).

THEOREM. Let S be a Riemannian symmetric space of non-compact type, of rank greater than 1, and  $\Lambda$  an irreducible discrete group of motions

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$n\geqslant 3$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">If $H$ is the group of motions of an $n$-dimensional Lobachevskii space, $n > 3$, this theorem was previously obtained by the present author [44], using the ideas of Moscow's paper [45].</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2. obtained by the present author [44], using the ideas of Mostow's paper [45].</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2 This theorem was announced by the author in [46].</span></small>

of S for which  $S/\Lambda$  has finite volume but is not compact. Then  $\Lambda$  is an arithmetic subgroup of the group of motions of S.

NOTE. In §15.3 of this paper, in the proof of Lemma 12.2.1, it is assumed that G is a so-called strongly non-compact group. We mention that when G is simple over R, then G is strongly non-compact if it is isomorphic to one of the four groups listed in Lemma 15.4.2. The case when G is not strongly non-compact requires additional arguments, which we do not give here because they are too cumbersome.

2. The proof of the main theorem is divided into two steps: the proof of a “rationality” theorem, and the proof of the main theorem proper. The “rationality” theorem $^{1}$  (Theorem 9.7.1), whose proof is outlined at the beginning of §5, states, briefly speaking, that G can be given a Q-structure for which  $\Gamma \subset G_{Q}$ . We shall now assume that the “rationality” theorem has been proved, $^{2}$  that is, that  $\Gamma \subset G_{Q}$ . The proof of the main theorem rests upon Lemma 10.1.

There exists an $n$ such that $\Gamma$ contains all the unipotent elements of $G_{n\mathbf{Z}}$. Lemma 10.1 is proved in §§11-16. At the beginning of §12 this lemma is reduced to the corresponding $p$-adic Lemmas 12.1.11 and 12.2.1. In §14 Lemmas 12.1.1 and 12.2.1 are proved in the simplest case when $\mathrm{rank}_{\mathbf{Q}}G \geqslant 2$. In the much more difficult case $\mathrm{rank}_{\mathbf{Q}}G = 1$, Lemma 12.2.1 is proved in §15 by using the strong approximation theorem ([22], [24], [25]) for strongly non-compact groups $G$.

3. We do not give a section-by-section description of the paper. We draw attention to §8, which contains a construction from representation theory. This section is independent of the others. The construction in §8 turns out to be useful not only in the proof of the “rationality” theorem, but also in proving various theorems on isomorphisms between subgroups of algebraic groups [29]. We also note that §17 contains some unsolved problems of the theory of discrete subgroups.

The author thanks L. N. Vasershtein, B. Yu. Veisfeiler, E. B. Vinberg, and D. A. Kazhdan for valuable conversations, and I. I. Pyatetskii-Shapiro for his interest in this work. The author is also grateful to L. N. Vasershtein and E. B. Vinberg for communicating to him some of their unpublished results.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1 This theorem was announced by the author (in a slightly weaker form) in [36] and proved in the recent paper [29]. The proof of the “rationality” theorem in the present paper is a modification of that in [29].</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2 ADDED IN PROOF. The author has received a preprint from Raghunathan containing a proof of the “rationality” theorem, and also a proof of the main theorem in the case rank $Q^{G} > 2$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Raghunathan's proof differs considerably from that of the present paper, although it is also based on a study of the unipotent subgroups of $\Gamma$.</span></small>

## §0. Notation and terminology

0.1. Except in §8 all the fields throughout this paper are assumed to be of characteristic zero. By an algebraic group over a field k, or a group defined over k, or an algebraic k-group we mean a linear algebraic group defined over k, that is, an algebraic subgroup of  $GL_{n}$  that is defined over k. If K is a normal extension of the field k, then  $\operatorname{Gal}(K/k)$  denotes the Galois group of K over k. As usual, when H is an algebraic group,  $H^{0}$  denotes the connected component of the identity.

0.2. As usual, C, R, Q, Z,  $N^{+}$ ,  $Q_{p}$ , and  $Z_{p}$  denote the complex numbers, the reals, the rationals, the rational integers, the positive integers, the p-adic numbers, and the p-adic integers.

0.3. For any algebraic $k$-group $N$ and any ring $K$ that can be imbedded into a ring into which $k$ can also be embedded, we denote by $N_K$ the set of points of $N$ that are defined over $K$ and whose determinant is an invertible element of $K$. For any algebraic $\mathbf{Q}$-group $H$ and any natural number $n$ we denote by $H_{n\mathbf{Z}}$ the subgroup of points in $H_{\mathbf{Z}}$ that are congruent to 1 modulo $n$. In what follows, an algebraic $k$-group $H$ is always identified with $H_K$, where $K$ is an algebraically closed field containing all the extensions of $k$ that occur. If $k'$ is an extension of $k$, then rank$_{k'}H$ denotes the $k'$-rank of $H$ (that is, the dimension of a maximal $k'$-split torus). By $M^u$, where $M \subset H$, we denote the set of unipotent elements of $M$. By $R_u(H)$ we denote the unipotent radical of $H$, and by $R_n(H)$ the nilpotent radical of $H$ (that is, the maximal connected nilpotent normal subgroup of $H$).

0.4. Except when the contrary is stated explicitly, throughout this paper G is a connected semisimple R-group without compact factors and with trivial centre, of R-rank greater than 1, and  $\Gamma$  is an irreducible non-uniform lattice in  $G_{R}$ . We note that G is an adjoint group because its centre is trivial.  $\pi$  denotes the natural projection of  $G_{R}$  on  $G_{R}/\Gamma$ .

0.5. Let $H$ be a group. Then $Z(H)$ denotes the centre of $H$. For any $F \subset H$, $N(F)$ and $C(F)$ denote, respectively, the normalizer and centralizer of a subset $F$ in $H$. If $H$ is a Lie group with Lie algebra $\mathfrak{H}$, and $\mathfrak{A}$ is a subset of $\mathfrak{H}$, then $N(\mathfrak{A})$ denotes the normalizer of $\mathfrak{A}$ in $H$, that is, $N(\mathfrak{A}) = \{n \in H; \operatorname{Ad} n\mathfrak{A} = \mathfrak{A}\}$ and $C(\mathfrak{A})$ the centralizer of $\mathfrak{A}$ in $H$, that is

$$
C (\mathfrak {A}) = \{n \in H; (\operatorname{Ad} n) a = a \text {   for   every   } a \in \mathfrak {A} \}.
$$

The commutator of two elements x and y of H is denoted by  $(x, y)$ , and that of two elements u and v of the Lie algebra  $\mathfrak{H}$  by  $[u, v]$ . For any two subsets A and B of H we put

$$
\{A, B \} = \{a b a ^ {- 1} b ^ {- 1}; a \in A, b \in B \}
$$

and let $(A, B)$ denote the subgroup generated by $\{A, B\}$. For any two subsets $A$ and $B$ of the Lie algebra $\mathfrak{H}$, $[A, B]$ denotes the linear subspace

generated by all the commutators $[a, b]$, $a \in A$, $b \in B$. For any integer $n$ and any $M \subset H$ (respectively, $M \subset \mathfrak{H}$) we put

$$
n M = \{m ^ {n}; m \in M \} (\text { respectively }, n M = \{n m; m \in M \}).
$$

Two subgroups of an arbitrary group are said to be commensurable if their intersection has finite index in each of them. For any subset M let  $\overline{M}$  denote the closure of M (usually, in the Zariski topology). The unit element of a group is denoted by e and the unit matrix by E (although the letter E is also used to denote other objects).

0.6.  $H_{1} \times H_{2}$  denotes the direct product of two groups  $H_{1}$  and  $H_{2}$ .  $L \widetilde{\times} N$  denotes the semidirect product of a subgroup L and a normal subgroup N. If we consider algebraic groups (Lie groups, etc.), then direct, almost direct, and semidirect products are understood in the sense of the theory of algebraic groups (Lie groups, etc.).

0.7. We say that an algebraic $k$-group $H$ has a $K$-structure ($k \supset K$) if there is an algebraic $K$-group $\widetilde{H}$ and an isomorphism $f \colon H \to \widetilde{H}$ defined over $k$. If $H$ has a $K$-structure, then we identify $H$ with $\widetilde{H}$ by means of $f$, and for any ring $L$ we set $H_L = f^{-1}(\widetilde{H}_L)$.

0.8. Let X be a locally compact topological space, and  $x(t)$ ,  $0 \leqslant t < \infty$ , a curve in X. We say that  $x(t)$  tends to infinity in X if for any compact set  $K \subset X$  there is a  $t(K)$  such that  $x(t) \notin K$  for  $t > t(K)$ . Let H be a locally compact group, F a closed subgroup of H,  $\varphi: H \to H/F$  the natural map, and  $h(t)$ ,  $0 \leqslant t < \infty$ , a curve in H. We say that  $h(t)$  tends to infinity in H if  $x(t) = \varphi(h(t))$  tends to infinity in H/F. If  $A \subset H$ , then we say that A is relatively compact in H/F if  $\varphi(A)$  is relatively compact in H/F.

0.9. If F is a subgroup of H, then  $|H/F|$  denotes the index of F in H, that is, the number of cosets of F in H.

0.10. For any set $M$ and any natural number $n$, we denote by $M^n$ the direct product of $n$ copies of $M$.

0.11. If $\mathfrak{H}$ is the Lie algebra of an algebraic $k$-group $H$ and $K$ is a field extension of $k$, then $\mathfrak{H}_K$ denotes the set of $K$-points of $\mathfrak{H}$.

0.12. We freely use the terminology of the theory of algebraic groups ([4], [10], [26]).

## § 1. The intersections of discrete subgroups with normal subgroups

In this section we denote by  $I(M)$ , for any subgroup M of an arbitrary Lie group, the connected component of the identity of the closure of M, and any algebraic R-group H will be identified with  $H_{R}$ .

1.1. LEMMA. Let $H$ be a Lie group, $Q \subset H$ a closed soluble normal subgroup with finitely many connected components, and $\varphi: H \to H / Q$ the natural homomorphism. Then for any discrete subgroup $\Lambda$ of $H$ the group $I(\varphi(\Lambda))$ is soluble.

When $Q$ is connected and simply-connected, this lemma was proved for

commutative Q by Zassenhaus [17], and for all soluble Q by L. Auslander ([37], [38]). Let Q be arbitrary. Since Q has finitely many connected components, we can replace Q by its connected component of the identity. Now we must apply Auslander's method, which carries over to non simply-connected Q almost without change.

1.2. We state some results of Mostow ([1], [2]) as lemmas.

1.2.1. LEMMA. Let Q be a soluble Lie group, N an arbitrary closed subgroup that is commensurable with the nilpotent radical of Q. Then 1) every lattice in Q is uniform; 2) if  $\Lambda$  is a lattice in Q, then  $N \cap \Lambda$  is a uniform lattice in N.

1.2.2. REMARK. In [1] and [2] it is assumed that Q is connected and that N is the nilpotent radical. But it is easy to see that these restrictions are not essential.

1.3. Let H be an algebraic R-group, A the soluble radical of H, N the nilpotent radical of H,  $\Lambda$  a discrete subgroup of H, and f the natural map  $H \rightarrow H/A$ .

1.3.1. LEMMA. If $\Lambda$ is Zariski-dense in $H$, then $f(\Lambda)$ is a discrete subgroup of $H/A$.

PROOF. If  $f(\Lambda)$  is not discrete, then  $\dim I(f(\Lambda)) > 0$ . Since  $f(\Lambda)$  normalizes  $I(f(\Lambda))$  and  $\Lambda$  is Zariski-dense in H,  $I(f(\Lambda))$  is a normal subgroup of H/A. But H/A is semisimple (because A is the soluble radical of H). Hence  $I(f(\Lambda))$  is a semisimple Lie group of positive dimension. On the other hand, since A regarded as a Lie group has only finitely many connected components, by Lemma 1.1,  $I(f(\Lambda))$  is soluble. This contradiction proves the lemma.

From Lemma 1.3.1 we immediately obtain the next result.

1.3.2. LEMMA. If $\Lambda$ is a Zariski-dense lattice in $H$, then $A \cap \Lambda$ is a lattice in $A$.

Since N, regarded as a Lie group, has finitely many connected components, Lemmas 1.3.1 and 1.3.2 lead to:

1.3.3. LEMMA. If $\Lambda$ is a Zariski-dense lattice in $H$, then $N \cap \Lambda$ is a uniform lattice in $N$.

1.4. We shall repeatedly use the following lemma, due to A. Borel [3].

1.4.1. LEMMA. Let H be a connected semisimple algebraic R-group without compact factors, and  $\Lambda$  a lattice in H. Then  $\Lambda$  is Zariski-dense in H.

1.5. LEMMA. Let H be a semisimple algebraic R-group with trivial centre and without compact factors,  $\Lambda$  an irreducible lattice in H. Then the intersection of  $\Lambda$  with any non-trivial algebraic subgroup of H is trivial.

PROOF. Assume the contrary and let $H'$ be a minimal non-trivial algebraic normal subgroup for which $H' \cap \Lambda \neq \{e\}$. Since $H$ is semisimple with trivial centre, $H = H' \times H''$. Let $f$ denote the natural projection $H \to H'$. Since the lattice $\Lambda$ is irreducible and (by Lemma 1.4.1) Zariski-dense in $H$, $I(f(\Lambda))$ is a connected normal subgroup of $H$ of positive dimension. On the other hand, since the centre of the semisimple group $H'$ is trivial, $H' \cap \Lambda \neq \{e\}$, and since, by the minimality of $H'$, $H' \cap \Lambda$ is not contained

in any non-trivial algebraic normal subgroup of $H'$, the centralizer $C(H' \cap \Lambda)$ does not contain any non-trivial normal subgroup of $H'$. Therefore, $\{H' \cap \Lambda, I(f(\Lambda))\}$ is a connected subset of $H$ of positive dimension. Now, since $\{H' \cap \Lambda, f(\Lambda)\} = \{H' \cap \Lambda, \Lambda\}$, the closure of $\{\hat{H}' \cap \Lambda, \Lambda\}$ contains the connected set $\{H' \cap \Lambda, I(f(\Lambda))\}$ of positive dimension, which contradicts the fact that $\Lambda$ is discrete. This proves the lemma.

## §2. Some preliminary information

2.1. Let $H$ be a locally compact topological group, and $D$ and $F$ closed subgroups of $H$. We say that $D$ is $F$-proper if the natural map $D / D \cap F \to H / F$ is proper, and $F$-compact if the factor space $D / D \cap F$ is compact. Every $F$-compact subgroup is obviously $F$-proper.

2.1.1. LEMMA. If $D$ is $F$-proper, then $F$ is $D$-proper.

PROOF. We must prove that for every compact set $K \subset H$ the subset $(K \cdot D) \cap F$ is contained in $K'(D \cap F)$, where $K'$ is compact. Let $K \subset H$ be an arbitrary compact set. Then $(K \cdot D) \cap F \subset K^{-1}F$. Since $D$ is $F$-proper and $K^{-1}$ is compact, $D \cap K^{-1}F \subset K''(F \cap D)$, where $K''$ is compact. Therefore, $(K \cdot D) \cap F \subset K^{-1}K''(F \cap D)$, which proves the lemma.

Since any compact subset of a discrete subgroup is finite, from Lemma 2.1.1 we obtain the following result.

2.1.2. LEMMA. If $F$ is a discrete subgroup of $H$, then $D$ is $F$-proper if and only if for any compact $K \subset D$ there is a finite subset $M \subset F$ such that $(K \cdot D) \cap F = M(D \cap F)$.

2.1.3. LEMMA. If $F$ is discrete, and if $D_1$ and $D_2$ are $F$-proper, then $D_1 \cap D_2$ is also an $F$-proper subgroup.

PROOF. Let $K \subset H$ be a compact set. Then, by 2.1.2, $(K \cdot D_1) \cap F$ is the union of a finite number of left cosets of $D_1 \cap F$, and $(K \cdot D_2) \cap F$ of $D_2 \cap F$. But the intersection of left cosets with respect to two subgroups is a left coset with respect to their intersection. Therefore,

$(K(D_{1} \cap D_{2})) \cap F \subset ((K \cdot D_{1}) \cap F) \cap ((K \cdot D_{2}) \cap F)$ is contained in the union of a finite number of left cosets of $D_{1} \cap D_{2} \cap F$, and since $(K(D_{1} \cap D_{2})) \cap F$ is a union of left cosets of $D_{1} \cap D_{2} \cap F$, we see that $(K(D_{1} \cap D_{2})) \cap F = M(D_{1} \cap D_{2} \cap F)$, where $M$ is finite. Therefore, by 2.1.2, $D_{1} \cap D_{2}$ is $F$-proper.

From Lemma 2.1.3 we immediately deduce:

2.1.4. LEMMA. If $F$ is discrete, $D_1$ is $F$-proper and $D_2$ is $F$-compact, then $D_1 \cap D_2$ is $F$-compact.

2.1.5. LEMMA. Let $F$ be a discrete subgroup of $H$, and $E, D$, and $N$ closed subgroups of $H$. If $E = D \widetilde{\times} N$, $D$ is $F$-proper, and $N$ is $F$-compact, then $(D \cap F) \widetilde{\times} (N \cap F)$ is a subgroup of finite index in $E \cap F$.

PROOF. Since $N$ is $F$-compact, $N = (N \cap F)K$, where $K \subset N$ is compact.

Then, by 2.1.2, $(K\cdot D)\cap F = M\cdot (D\cap F)$, where $M$ is finite. Since $(K\cdot D)\cap F\subset (N\cdot D)\cap F = E\cap F$ and $D\cap F\subset E\cap F$, we see that $M\subset E\cap F$ and, hence, that $M$ normalizes $N\cap F$. Therefore,

$$
E \cap F = (N \cdot D) \cap F = ((N \cap F) \cdot K \cdot D) \cap F \subset (N \cap F) \cdot ((K \cdot D \cap F) =
$$

$$
= (N \cap F) \cdot M \cdot (D \cap F) = M \cdot (N \cap F) \cdot (D \cap F).
$$

2.2. Let $H$ and $S$ be algebraic $\mathbf{R}$-groups, $f$ an $\mathbf{R}$-morphism $H \to S$, $F$ the kernel of the homomorphism $f$. Then $f$ naturally induces a homomorphism $\varphi$ of Lie groups $H_{\mathbf{R}} / F_{\mathbf{R}} \to S_{\mathbf{R}}$.

2.2.1. LEMMA. 1) $f(H)$ is an algebraic R-subgroup and

$\dim f(H) = \dim H - \dim F; 2)\varphi$ effects a bicontinuous isomorphism of the Lie group $H_{\mathbf{R}} / F_{\mathbf{R}}$ onto some closed subgroup of finite index in $(f(H))_{\mathbf{R}}$.

PROOF. 1) is a special case of Corollary 1.4 of Ch. I in [4]. We prove 2). Let D and E denote the connected components of the identity of the Lie groups  $H_{R}/F_{R}$  and  $(f(H))_{R}$ . Since F is the kernel of f, the differential of  $\varphi$  at the identity gives an isomorphism of the Lie algebras of  $H_{R}/F_{R}$  and  $(f(H))_{R}$ . Therefore, D is a covering of E, and since the kernel of  $\varphi$  is trivial (because F is the kernel of f), the restriction of  $\varphi$  to D is a homomorphism onto E. To finish the proof, it remains to note that  $\varphi$  is a monomorphism and that D and E are closed subgroups of finite index in  $H_{R}/F_{R}$  and  $(f(H))_{R}$  (since the number of connected components of  $A_{R}$  is finite for any algebraic R-group A).

2.3. LEMMA. Let $H$ be an algebraic $\mathbf{R}$-group, $D$ an algebraic $\mathbf{R}$-subgroup of $H$, and $F$ an algebraic normal subgroup of $H$ defined over $\mathbf{R}$. Then the natural map $F_{\mathbf{R}} / F_{\mathbf{R}} \cap D_{\mathbf{R}} \to H_{\mathbf{R}} / D_{\mathbf{R}}$ is proper.

PROOF. By Theorem 6.8 of Ch. II in [4], H/F is an algebraic R-group, and the natural map  $f: H \to H/F$  is an R-morphism. Therefore, using Lemma 2.1.2, we see that  $D_{R}$  is  $F_{R}$ -proper. Consequently, by 2.1.1,  $F_{R}$  is a  $D_{R}$ -proper subgroup, which proves the lemma.

2.4. LEMMA (Zassenhaus [17], see also [11]). In any Lie group H there is a neighbourhood V of the identity such that for any discrete subgroup  $\Lambda$  of H the subgroup generated by  $\Lambda \cap V$  is nilpotent.

A neighbourhood that satisfies the conclusion of this lemma will be called a Zassenhaus neighbourhood of H.

## §3. Unipotent discrete subgroups

For any unipotent matrix u we denote by  $\ln u$  the unique nilpotent matrix for which  $\exp(\ln u) = u$ .

3.1. Let $V$ be a unipotent algebraic $\mathbf{R}$-group, $\mathfrak{W}$ the Lie algebra of $V$, $\mathfrak{W}_{\mathbb{R}}$ the set of $\mathbf{R}$-points of $\mathfrak{W}$, and $\Lambda$ a discrete subgroup of $V_{\mathbb{R}}$. For any subset $M \subset \mathfrak{W}$ and any constant $b$ we put $bM = \{bm; m \in M\}$. Now $V_{\mathbb{R}}$ is a simply-connected nilpotent Lie group. Therefore, we can associate with $\Lambda$ a lattice $\Delta_{\Lambda} \subset \mathfrak{W}_{\mathbb{R}}$, just as in §1 of [5]. We note [5] that $b(n)\ln \Lambda \subset \Delta_{\Lambda} \subset \ln \Lambda$, where $b(n) \in \mathbf{Z}$ depends only on $n = \dim V$, and

$$
\Delta_ {\Lambda}
$$

$$
\exp . \mathfrak {W} \rightarrow V
$$

$$
V \rightarrow \mathfrak {W}
$$

$$
\Delta_ {\Lambda} \supset b (n) \ln
$$

$$
\mathfrak {W} _ {\mathbf {R}}
$$

3.2. Let $V$ and $\Lambda$ be as in 3.1.

3.2.1. LEMMA OF RAGHUNATHAN [6]. The following conditions are equivalent:

1) $\Lambda$ is Zariski-dense in $V$;

2) the factor space $V_{\mathbb{R}} / \Lambda$ is compact.

3.3. Let $V$ be a unipotent $\mathbf{Q}$-group.

3.3.1. LEMMA. For any natural number $n$, 1) the factor space $V_{\mathbf{R}} / V_{n\mathbf{Z}}$ is compact; 2) the subgroup $V_{n\mathbf{Z}}$ is Zariski-dense in $V$.

PROOF. 1) follows from 6.10 in [7], and 2) from 1) and Lemma 3.2.1.

3.3.2. LEMMA. If $\Lambda \subset V_{\mathbf{Q}}$, and $\Lambda$ is discrete in $V_{\mathbf{R}}$ and Zariski-dense in $V$, then 1) $\Delta_{\Lambda}$ and $\Delta_{V_{\mathbf{Z}}}$ are commensurable, 2) $\Lambda$ is commensurable with $V_{\mathbf{Z}}$.

PROOF. Since $\Lambda \subset V_{\mathbf{Q}}$, we have $\Delta_{\Lambda} \subset \mathfrak{W}_{\mathbf{Q}}$. Therefore, the lattices $\Delta_{\Lambda}$ and $\Delta_{V_{\mathbf{Z}}}$ are commensurable (this is 1)). Then there exists a natural number $d$ such that $\Delta_{\Lambda} \supset d\Delta_{V_{\mathbf{Z}}}$, and, hence (§3.1), $\ln \Lambda \supset db(n)\ln V_{\mathbf{Z}}$ ($n = \dim V$). Therefore, $\Lambda \supset db(n)V_{\mathbf{Z}}$. Since $V$ is unipotent, the mapping

$f: V \to V (f(u) = u^{db(n)})$ is rational and biregular. But, by 3.3.1, $V_{\mathbf{Z}}$ is Zariski-dense in $V$. Therefore, $db(n)V_{\mathbf{Z}}$ is Zariski-dense in $V$, and hence, so is $\Lambda \cap V_{\mathbf{Z}}$. Now (see 3.2.1) $\Lambda \cap V_{\mathbf{Z}}$ is a uniform lattice in $V_{\mathbf{R}}$, consequently, $\Lambda \cap V_{\mathbf{Z}}$ is of finite index in $V_{\mathbf{Z}}$. Similarly, $\Lambda \cap V_{\mathbf{Z}}$ is of finite index in $\Lambda$, which proves the lemma.

The following result is well known (for example, see [19]).

3.3.3. LEMMA. Every subgroup of finite index in  $V_{Z}$  contains a  $V_{nZ}$  for some n.

3.4. Let V be a unipotent R-group,  $\Lambda$  a discrete subgroup of  $V_{R}$  that is Zariski-dense in V, and Z the centre of V.

3.4.1. LEMMA. $\Lambda$ is an arithmetic subgroup of $V$.

PROOF. Since (§3.1) $\Delta_{\Lambda}$ is a lattice of full dimension in $\mathfrak{W}_{\mathbb{R}}$. $\Delta_{\Lambda}$ gives a Q-structure on $\mathfrak{W}$. But $\exp: \mathfrak{W} \to V$ is a biregular rational map (because $V$ is unipotent). Therefore, a Q-structure on $\mathfrak{W}$ gives a Q-structure on $V$, and since $b(n)\ln \Lambda \subset \Delta_{\Lambda}$, we have $\Lambda \subset V_{\mathbf{Q}}$. Since $\Delta$ is contained in $V_{\mathbf{Q}}$ and is Zariski-dense in $V$, the mappings $\mu: V \times V \to V$, $\mu(v_1, v_2) = v_1 \cdot v_2$ and $i: V \to V$, $i(v) = v^{-1}$, are defined over $\mathbf{Q}$, hence, $V$ is an algebraic Q-group with respect to the given Q-structure. But $A \subset V_{\mathbf{Q}}$, consequently (see 3.3.2), $\Lambda$ is commensurable with $V_{\mathbf{Z}}$, which proves the lemma.

3.4.2. REMARK. In the proof of Lemma 3.4.1 we did not use explicitly the fact ([4], Ch. I, Proposition 1.10) that an affine k-group is k-isomorphic to a closed subgroup of  $GL_{n}$  defined over k (for a suitable n).

3.4.3. LEMMA. The subgroup  $Z \cap \Lambda$  is Zariski-dense in Z and is a uniform lattice in  $Z_{R}$ .

PROOF. By Lemma 3.4.1, we can introduce a Q-structure on V for which  $\Lambda$  is commensurable with  $V_{Z}$, and hence,  $Z \cap \Lambda$  is commensurable with  $Z_{Z}$. The centre Z of V is defined over Q. Therefore (see 3.3.3 and 3.3.1),  $Z \cap \Lambda$  is a uniform lattice in  $Z_{R}$, and  $Z \cap \Lambda$  is Zariski-dense in Z.

## §4. Some information from the theory of algebraic groups and their algebraic subgroups

4.1. For any algebraic Q-group F we denote by  $\chi_{\mathbf{Q}}(F)$  the group of Q-rational characters of F. Let H be an algebraic Q-group and  $H^{0}$  the connected component of the identity of H.

4.1.1. LEMMA. If $\Lambda \subset H$ is commensurable with $H_{\mathbf{Z}}$ and if $\Lambda$ is Zariskidense in $H$, then $\Lambda \cap H_{\mathbf{R}}$ is a lattice in $H_{\mathbf{R}}$.

PROOF. Since $\Lambda$ is dense in $H$ and $H_{\mathbf{Z}}$ is commensurable with $\Lambda$, $H_{\mathbf{Z}}^{0}$ is dense in $H^{0}$. Let $\chi \in \chi_{\mathbf{Q}}(H^{0})$. It is clear that $\chi(H_{\mathbf{Z}}^{0})$ consists of numbers with bounded denominators. But $\chi(H_{\mathbf{Z}}^{0})$ is a group. Therefore, $\chi(H_{\mathbf{Z}}^{0}) \subset \pm 1$, and since $H_{\mathbf{Z}}^{0}$ is dense in $H^{0}$, we see that $\chi(H^{0}) \subset \pm 1$. But $H^{0}$ is connected, so that $\chi(H^{0}) = 1$. Hence, $\chi_{\mathbf{Q}}(H^{0}) = 1$. Therefore ([7], Theorem 9.4), $H_{\mathbf{Z}}$ is a lattice in $H_{\mathbf{R}}$, and since $\Lambda$ and $H_{\mathbf{Z}}$ are commensurable, $\Lambda \cap H_{\mathbf{R}}$ is a lattice in $H_{\mathbf{R}}$.

4.2. A unipotent algebraic subgroup V of an algebraic k-group G is called horospherical if  $V = R_{u}(N(V))$ .

4.2.1. LEMMA ([8] or [9], 3.2). If $V$ is a horospherical subgroup of $G$, then $N(V)$ is a parabolic subgroup of $G$.

4.3. Let k be a field of characteristic zero, and H an algebraic k-group.

Then for any $u \in H^u$ and any integer $n$ we have $u^{1/n} = \exp\left(\frac{1}{n}\ln u\right) \subset H^u$, and hence, $nH^u = H^u$. From this and the finiteness of the index $|H / H^0|$ we obtain:

4.3.1. LEMMA. $H^{u} \subset H^{0}$.

4.3.2. LEMMA. Let S be a soluble subgroup of H generated by unipotent elements. Then S is unipotent.

PROOF. Let $\overline{S}$ be the Zariski-closure of $S$ in $H$. Since $S$ is soluble, so is $\overline{S}$. By Lemma 4.3.1 the soluble algebraic group $\overline{S}$ is connected. Therefore, $\overline{S} = T \widetilde{\times} W$, where $T$ is a torus and $W$ is unipotent. Then $\overline{S}^u \subset W$, and since $S$ is generated by unipotent elements, $S \subset W$, that is, $S$ is unipotent.

4.4. From Lemma 1.6 of the paper by Garland and Raghunathan [12] we easily derive:

4.4.1. LEMMA. Let k be a field of characteristic zero, H a connected semisimple algebraic k-group, and  $V \subset H$  a non-trivial unipotent algebraic subgroup. We put  $W = R_{u}(C(V))$ . If V is not contained in any non-trivial normal subgroup of H, then  $C(V) \cap C(W)$  contains no tori of positive dimension.

4.5. Let $G$ be a connected semisimple algebraic $k$-group, $S$ a maximal

$k$-split torus of $G$, $k\Phi$ the set of roots of $G$ relative to $S$. Let $\mathfrak{G}$ be the Lie algebra of $G$. For any $\alpha \in k\Phi$ we denote by $_k\mathfrak{G}_\alpha \subset \mathfrak{G}$ the root space corresponding to $\alpha$, and we put $k G_{\alpha}' = \exp_k \mathfrak{G}_\alpha$. For any subset $\psi \subset_k \Phi$, we denote by $G_{\psi}$ the subgroup generated by $C(S)$ and by all the $k G_{\alpha}'$ ($\alpha \in_k \Phi$), by $G_{\psi}^*$ or $U_{\psi}$ the subgroup generated by all the $k G_{\alpha}'$ ($\alpha \in \psi$), and by $G_{\psi}'$ the union $\bigcup_{\alpha \in \psi} G_{\alpha}'$. One verifies immediately that the $G_{\psi}$ and

$G_{\psi}^{*}$ defined here mean the same as in [10] (3.8). Therefore, ([10], 3.8) $G_{\psi} = C(S) \cdot G_{\psi}^{*}$. We fix an order in $k\Phi$ and denote by $k\Phi^{+}, k\Phi^{-}$, and $k\Delta$, respectively, the sets of positive, negative, and simple roots with respect to this order. For any $\theta \subset_{k}\Delta$ we denote by $[\theta]$ the set of roots that are linear combinations of elements of $\theta$ with integral coefficients, and we put $\pi_{\theta} = [\theta] \cup \Phi^{+}, \pi_{\bar{\theta}}^{-} = [\theta] \cup \Phi^{-}, \alpha_{\theta} = C[\theta] \cap \Phi^{+}, \overline{\theta} = [\theta] \cap \Phi^{+}, \alpha_{\theta}^{-} = C[\theta] \cap \Phi^{-}, \overline{\theta}^{-} = [\theta] \cap \Phi^{-}$. For any $\theta \subset_{k}\Delta$ we write $kP_{\theta}, kP_{\bar{\theta}}, kV_{\theta}, kV_{\theta}^{-}, kB_{\theta}, kB_{\bar{\theta}}, kZ_{\theta}$ instead of $G_{\pi_{\theta}}, G_{\pi_{\bar{\theta}}}, U_{\alpha_{\theta}}, U_{\alpha_{\bar{\theta}}}, U_{\bar{\theta}}, U_{\bar{\theta}-}$ and $C(S_{\theta})$, respectively ($S_{\theta}$ denotes the connected component of the identity in the intersection of the kernels of the characters $\alpha \in \theta$). If it is clear what field $k$ is being discussed, we simply write $\Phi, \mathfrak{G}_{\alpha}, P_{\theta}$, etc. instead of $k\Phi, k\mathfrak{G}_{\alpha}, kP_{\theta}$, etc. The subgroups $kP_{\theta}$ ($\theta \subset \Delta$) are called standard parabolic $k$-subgroups.

A subset $\psi \subset \Phi$ is said to be closed if $\alpha_{1} \in \psi$, $\alpha_{2} \in \psi$ and $\alpha_{1} + \alpha_{2} \in \Phi$ together imply that $\alpha_{1} + \alpha_{2} \in \psi$. It is easy to verify that if $\psi \subset \Phi$ is closed and $G_{\beta}' \subset G_{\psi}^{*} = U_{\psi}$ (or $G_{\beta}' \subset G_{\psi} = C(S) \cdot U_{\psi}$), then $\beta \in \psi$. All the subsets $\pi_{\theta}, \pi_{\theta}^{-}$, etc. defined earlier are closed. Therefore, for any $\theta \subset \Phi$ we have

$$
B _ {\theta} = P _ {\theta} ^ {-} \cap V _ {\varnothing}, \quad B _ {0} ^ {-} = P _ {\theta} \cap V _ {\varnothing} ^ {-}.\tag{1}
$$

We have the Levi decomposition ([10], 5.12 and 4.2)

$$
P _ {\theta} = Z _ {\theta} \widetilde {\times} V _ {\theta}, P _ {\theta} ^ {-} = Z _ {\theta} \widetilde {\times} V _ {\theta} ^ {-}.\tag{2}
$$

For any $\theta \subset \Delta$ the groups $P_{\theta}$ and $P_{\theta}^{-}$ are parabolic $k$-subgroups of $G$ ([10], 5.12 and 4.2). But $N(V_{\theta}) \supset P_{\theta} \supset P_{\phi}$. Therefore ([10], 5.14) $N(V_{\theta}) = P_{\theta'}$, where $\theta' \supset \theta$. Then by (2), $V_{\theta} \subset R_u(N(V_{\theta})) = R_u(P_{\theta'}) = V_{\theta'}$, and hence $\theta \supset \theta'$. Therefore, $\theta = \theta'$ and

$$
N (V _ {\theta}) = P _ {\theta}, \quad V _ {\theta} = R _ {u} (N (V _ {\theta})).\tag{3}
$$

Similarly,

$$
N \left(V _ {\theta} ^ {-}\right) = P _ {\theta} ^ {-}, \quad V _ {\theta} ^ {-} = R _ {u} \left(N \left(V _ {\theta} ^ {-}\right)\right).\tag{4}
$$

Hence, $V_{\theta}$ and $V_{\theta}^{-}$ are horospherical subgroups of $G$.

We denote the Lie algebras of the groups $S$ and $C(S)$ by $\mathfrak{S}$ and $\mathfrak{C}$, respectively. For any linear subspace $\mathfrak{H} \subset \mathfrak{G}$ we denote by $\mathfrak{H}_k$ the set of $k$-points of $\mathfrak{H}$. We now state some results of Vinberg (see the Appendix) on root subspaces as a lemma.

4.5.1. LEMMA. 1) For any $\alpha \in \Phi$ and any non-zero $x \in (\mathfrak{G}_{\alpha})_k$ there exists a unique $w(x) = y \in (\mathfrak{G}_{-\alpha})_k$, for which $[x, y] = h \in \mathfrak{S}$, $\alpha(h) = 2$; 2) for any $\alpha \in \Phi$ and any non-zero element $x \in (\mathfrak{G}_{\alpha})_k$ we have

$$
[ \mathfrak {C}, x ] = \mathfrak {G} _ {\alpha}
$$

$$
(\operatorname{Ad} C (S)) x \supset (\mathfrak {G} _ {\alpha}) _ {h};
$$

3) if $\alpha, \beta, \alpha + \beta \in \Phi$, then $[\mathfrak{G}_{\alpha}, \mathfrak{G}_{\beta}] = \mathfrak{G}_{\alpha + \beta}$ and moreover, for any non-zero $x \in (\mathfrak{G}_{\alpha})_k$ we have $[x, \mathfrak{G}_{\beta}] \neq 0$.

From Lemma 4.5.1, 3), we obtain:

4.5.2. LEMMA. For any $\theta \subset \Delta$, 1) the subgroup generated by $G_{\theta}^{\prime}$ (respectively, $G_{-\theta}^{\prime}$) coincides with $B_{\theta}$ (respectively, $B_{\theta}^{\prime}$); 2) the normal subgroup of $V_{\phi}$ (respectively, $V_{\phi}^{-}$) generated by $G_{\theta}^{\prime}$ (respectively, by $G_{-\theta}^{\prime}$) coincides with $V_{\Delta - \theta}$ (respectively, $V_{\Delta - \theta}^{-}$).

4.5.3. LEMMA. Let $V$ and $V'$ be maximal unipotent $k$-subgroups of $G$. Then $N(V) \cap N(V')$ contains a maximal $k$-split torus $S$ of $G$.

PROOF. Since V and  $V'$  are maximal, by ([9], 3.7),  $N(V)$  and  $N(V')$  are minimal parabolic k-subgroups of G. Hence ([10], 4.18)  $N(V) \cap N(V')$  contains the required torus S.

Let $_{k}W = _{k}W(S, G) = N(S)/C(S)$ be the relative Weyl group. For any subgroup $H \subset G$ that is normalized by $C(S)$ and any $w \in _{k}W$ we denote by $wHw^{-1}$ the subgroup $n_{w}Hn_{w}^{-1}$, where $n_{w}$ is a representative of w in $N(S)$. Since $C(S)$ normalizes H, $wHw^{-1}$ is independent of the choice of $n_{w}$ and depends only on w.

4.5.4. LEMMA. Let $V$ and $V'$ be maximal unipotent $k$-subgroups of $G$, $S$ a maximal $k$-split torus of $G$, and $S \subset N(V) \cap N(V')$. Then on the sets of roots $\Phi = {}_k\Phi(S, G)$ of $G$ relative to $S$ we can introduce an order such that 1) $V = V_{\varnothing}$ and $V' = wV_{\varnothing}w^{-1}$, where $w \in {}_kW(S, G)$; 2) if $V \cap V' = \{e\}$, then $V = V_{\varnothing}$ and $V' = V_{\varnothing}'$.

PROOF. Since ([9], 3.7) $N(V)$ and $N(V')$ are minimal parabolic $k$-subgroups of $G$, we can put an order on $\Phi$ ([10], 5.9) such that $N(V) = G_{\Phi^+} = P_{\varnothing}$ and $N(V') = wP_{\varnothing}w^{-1}$, where $w \in {}_k W(S, G)$. Therefore, $V = R_u(N(V)) = R_u(P_{\varnothing}) = V_{\varnothing}$, $V' = wV_{\varnothing}w^{-1}$ (this is 1)). If $V \cap V' = \{e\}$, then $w$ takes $\Phi^+$ into $\Phi^-$, and hence $V' = V_{\varnothing}'$ (this is 2)).

4.5.5. LEMMA. Let $V$ and $V'$ be maximal unipotent $k$-subgroups of $G$, and $F$ the normal subgroup of $V$ generated by the intersection $V \cap V'$. Then 1) $F$ is a horospherical subgroup; 2) if $V \neq V'$, then $F \neq V$; 3) $N(F) \supset N(V)$.

PROOF. By Lemmas 4.5.2 and 4.5.3 we may assume that $V = V_{\phi} = U_{\Phi^{+}}$, $V' = wV_{\phi}w^{-1}$, where $w \in {}_k W(S, G)$. We denote by $w\Phi^{+}$ the image of $\Phi^{+}$ under the action of $w$ ($V' = U_{w\Phi^{+}}$), and we put $\theta = \Delta \cap \Phi^{+} \cap w\Phi^{+}$, $\rho = \Delta - \theta$. Since for any $\alpha \in \Phi$ either $\alpha \in w\Phi^{+}$ or $-\alpha \in w\Phi^{+}$, we have $-\rho \subset -\Delta \cap w\Phi^{+}$. But $w\Phi^{+}$ is closed. Hence $-\rho \subset w\Phi^{+}$, and so $-\rho \cap w\Phi^{+} \subset w\Phi^{-} \cap w\Phi^{+} = \varnothing$. But then $\Phi^{+} \cap w\Phi^{+} \subset \alpha_{\theta}$, and $V \cap V' = U_{\Phi^{+}} \cap U_{w\Phi^{+}} = U_{\Phi^{+}\cap w\Phi^{+}} \subset V_{\theta}$, and since $V_{\theta}$ is normal in $V = V_{\phi}, F \subset V_{\theta}$. On the other hand, $F \supset G_{\theta}'$ and hence (by Lemma 4.5.2, 1)), $F \supset V_{\theta}$. Thus, $F = V_{\theta}$, and hence $F$ is horospherical (this is 1)). Suppose

that $V \neq V'$. Then $w\Phi^{+} \neq \Phi^{+}$. Hence, $\theta \neq \Delta$ and $F = V_{\theta} \neq V$ (this is 2)). Finally, by (3) on p. 119, $N(F) = N(V_{\theta}) = P_{\theta} \supset P_{\phi} = N(V_{\phi}) = N(V)$ (this is 3)).

4.5.6. LEMMA. For any $\theta \subset \Delta$ the subgroups $B_{\theta}$ and $B_{\theta}^{-}$ are conjugate in $Z_{\theta}$.

PROOF. By (1) and (2), $V_{\phi} \cap Z_{\theta} = B_{\theta}$. Therefore, by (2), $V_{\phi} = B_{\theta} \widetilde{\times} V_{\theta}$. Since $V_{\phi} \subset Z_{\theta} \widetilde{\times} V_{\theta}$ is a maximal unipotent $k$-subgroup of $G$, and hence, of $Z_{\theta} \widetilde{\times} V_{\theta}$, $B_{\theta}$ is a maximal unipotent $k$-subgroup of $Z_{\theta}$. Similarly, $B_{\theta}^{-}$ is a maximal unipotent $k$-subgroup of the reductive group $Z_{\theta}$. Therefore ([9], 3.7), $B_{\theta}$ and $B_{\theta}^{-}$ are conjugate in $Z_{\theta}$.

4.5.7. LEMMA. If $P$ is a parbolic $k$-subgroup of $G$, then $R_{u}(P)$ is a horospherical subgroup of $G$ and $P = N(R_{u}(P))$.

PROOF. Since (by [10], 5.14) every parabolic k-subgroup is conjugate to a standard one, it suffices to prove the lemma for  $P = P_{\theta} (\theta \subset \Delta)$ . But in this case the assertion follows from (3).

4.5.8. LEMMA. If $P$ and $P'$ are opposite parabolic $k$-subgroups of $G$, then $gPg^{-1} = P_{\theta}$ and $gP'g^{-1} = P_{\theta}$ for some $g \in G_k$ and $\theta \subset \Delta$.

PROOF. Since (by [10], 5.14) P is conjugate over k to some standard parabolic k-subgroup, we may assume that  $P = P_{\theta}$ . Then  $P_{\theta}^{-}$  and  $P'$  are parabolic k-subgroups opposite to P. Therefore (by [10], 4.8),  $P_{\theta}^{-}$  and  $P'$  are conjugate via  $u \in R_{u}(P)_{k}$ . This proves the lemma.

4.6. Let G be a connected semisimple algebraic R-group.

4.6.1. LEMMA. For any compact set  $K \subset G_{R}$  lying in a unipotent subgroup U of G, and any neighbourhood W of the identity of  $G_{R}$  there is a  $g \in G_{R}$  such that  $gKg^{-1} \subset W$ .

PROOF. Let $V$ be a maximal unipotent $\mathbf{R}$-subgroup containing $U$. Then (see 4.5.3 and 4.5.4) there are a maximal $\mathbf{R}$-split torus $S$ in $G$ and an order in $\Phi = \Phi(S, G)$ such that $V = V_{\phi}$. Let $s \in S_{\mathbf{R}}$ be such that $\alpha(s) > 0$ for any $\alpha \in \Phi^{+}$ (for $s$ we can take $\exp \{i, s\}$, where $\{i\}$ is an arbitrary element of the open Weyl chamber corresponding to $\Phi^{+}$). Since $V$ is connected and $V = V_{\phi}$, there is a negative integer $n$ such that $s^{n} Ks^{-n} \subset W$.

4.6.2. LEMMA. For any discrete unipotent subgroup U of  $G_{R}$  there is a neighbourhood W of the identity of  $G_{R}$  such that if  $w \in W \cap G^{u}$  and the subgroup F generated by  $w \cup U$  is discrete, then F is unipotent.

PROOF. Let (see 2.4) V be a Zassenhaus neighbourhood of  $G_{R}$ . Since (see 3.2)  $U_{R}/U$  is compact, U contains a finite subset K generating U. Then (see 4.6.1) there is a  $g \in G_{R}$  for which  $gKg^{-1} \subset V$ . If  $v \in V \cap G^{u}$  and the subgroup F generated by  $v \cup gKg^{-1}$  is discrete, then (see 2.4) F is nilpotent, and hence (see 4.3.2), unipotent. Therefore,  $W = g^{-1}Vg$  is the required neighbourhood.

4.7. Let $G$ be a connected semisimple algebraic $\mathbf{Q}$-group. Since (by [10], 4.13) any two minimal parabolic $\mathbf{Q}$-subgroups of $G$ are conjugate over $\mathbf{Q}$ in $G$, and ([21], §14, Corollary to Proposition 3) the set of double cosets $P_{\mathbf{Q}} \backslash G_{\mathbf{Q}} / G_{\mathbf{Z}}$ is finite, where $P$ is a minimal parabolic $\mathbf{Q}$-subgroup, the following lemmas are true.

4.7.1. LEMMA. There is a finite number of minimal parabolic Q-subgroups $P_{1}, \ldots, P_{i}$ of $G$ such that any minimal parabolic Q-subgroup $P \subset G$ coincides with $g^{-1}(P)P_{j(P)}g(P)$ for some $j(P)$, $1 \leqslant j(P) \leqslant i$, and some $g(P) \in G_{\mathbf{Z}}$.

4.7.2. LEMMA. In $G_{\mathbf{Q}}$ there is a finite subset $M$ such that if $P$ and $P'$ are minimal parabolic Q-subgroups of $G$, then $P' = gPg^{-1}$, where $g \in G_{\mathbf{Z}} \cdot M$.

## §5. Unipotent subgroups of Γ and subgroups associated with them

Here are the main assertions for the proof of the “rationality” Theorem 9.7.1 and the interdependence among them:

![](images/page_15_image_4.jpg)

In this section U denotes a unipotent subgroup of  $\Gamma$ . The expression “U is maximal” means that U is a maximal unipotent subgroup of  $\Gamma$ .

5.1. Let $\overline{U}$ denote the Zariski closure of $U$ in $G$. The algebraic subgroup $\overline{U}$ is unipotent and defined over $\mathbf{R}$. Unless the contrary is stated, we assume throughout (and not only in this section) that $U = \overline{U} \cap \Gamma$. Let $\mathfrak{u}$ be the Lie algebra of $\overline{U}$ and $\mathfrak{u}_{\mathbb{R}}$ the set of real points in $\mathfrak{u}$. The group $N(\overline{U})$ acts in a natural fashion on $\mathfrak{u}$ (this action is obtained by restriction of the adjoint representation of $N(\overline{U})$ to $\mathfrak{u}$). The algebraic subgroup of $N(\overline{U})$ that consists of the elements whose determinant under this action is equal to $\pm 1$ is denoted by $S(\overline{U})$. With the subgroup $U$ we associate (see 3.1) a lattice $\Delta_U$ in $\mathfrak{u}_{\mathbb{R}}$. If it is clear what group $U$ is under discussion, then we simply write $N, S, C, \Delta$ for $N(\overline{U}), S(\overline{U}), C(\overline{U}), \Delta_U$.

REMARK. In [5] §5, instead of $U$ we considered the minimal connected closed unipotent subgroup $U_G$ of $G$ containing $U$. But since $U$ is unipotent, $\overline{U} = U_G$. Therefore, we can apply the results of §5 of [5] (in which it is nowhere used that $G = SL(3, \mathbb{R})$).

5.2. We introduce a Euclidean metric on the Lie algebra $\mathfrak{G}$ of $G$ and denote by $D(\Delta_U)$ the volume of the factor space $\mathfrak{u}_{\mathbb{R}} / \Delta_U$ relative to this metric. It is easy to see that the following lemmas are true ([5], Lemma 5.2).

5.2.1. LEMMA. For any positive constant $c$, the set $A_{c}$ of subgroups $U$ such that $D(\Delta_U) < c$ is finite.

5.2.2. LEMMA. The subgroup $S_{\mathbf{R}}$ is $\Gamma$-proper.

PROOF. Let K be compact in  $G_{R}$ . We consider the set E of lattices of

the form  $(\operatorname{Ad} m)\Delta_{U}$ , where  $m \in (K \cdot S_{\mathbf{R}}) \cap \Gamma$ . Since  $m \in K \cdot S$ , we have  $D((\operatorname{Ad} m)\Delta_{U}) < d(K)$ , where  $d(K)$  depends only on K. Therefore (see 5.2.1), E is finite. On the other hand, if  $m \in (K \cdot S_{\mathbf{R}}) \cap \Gamma$  and  $(\operatorname{Ad} m)\Delta_{U} = \Delta_{U}$ , then  $m \in S$ , and hence,  $m \in S_{R} \cap \Gamma$ . Therefore,  $(K \cdot S_{\mathbf{R}}) \cap \Gamma = M(S_{\mathbf{R}} \cap \Gamma)$ , where  $M \subset \Gamma$  is a finite set such that  $(\operatorname{Ad} M)\Delta_{U} = E$ . This proves the lemma.

Similarly ([5], Lemma 5.7) one proves:

5.2.3. LEMMA. The subgroup $C_{\mathbf{R}}$ is $\Gamma$-proper.

If $\gamma \in N \cap \Gamma$, and (see 5.1) $U = \overline{U} \cap \Gamma$, then $\gamma U \gamma^{-1} = \gamma (\overline{U} \cap \Gamma) \gamma^{-1} = \gamma \overline{U} \gamma^{-1} \cap \gamma \Gamma \gamma^{-1} = \overline{U} \cap \Gamma = U$. Since (see 3.1) $\Delta_U$ is uniquely determined by $U$, (Ad $\gamma$) $\Delta_U = \Delta_U$, and hence $\gamma \in S$. Thus, we have the next results.

5.2.4. LEMMA. 1) (Ad(N ∩ Γ)) ΔU = ΔU; 2) N ∩ Γ = S ∩ Γ.

5.2.5. LEMMA. 1) $N^u = S^u$; 2) $R_u(N) = R_u(S)$.

PROOF. 1) follows from the fact that Ad is a rational representation, and the image of a unipotent element under a rational representation is unipotent, and 2) follows from 1) and the fact that the unipotent radical of any algebraic group coincides with the intersection of all maximal unipotent subgroups.

5.3. In [11] (see also [12] the following is essentially proved.

5.3.1. LEMMA. In $\Gamma$ we can choose a non-empty finite set $H$ with the following properties: 1) every element of $H$ is not equal to $e$ and is unipotent; 2) for any neighbourhood $V \subset G_{\mathbf{R}}$ of the identity there is a compact $K(V) \subset G_{\mathbf{R}} / \Gamma$ for which, if $\pi(g) \notin K(V)$, then $g\Gamma g^{-1} \cap V$ contains a non-identity unipotent element $\gamma_g(V)$ such that $\gamma_g(V) = g\gamma h\gamma^{-1}g^{-1}$ for some $h \in H$ and $\gamma \in \Gamma$.

5.4. As before, $N = N(\overline{U})$, $S = S(\overline{U})$, $C = C(\overline{U})$, $\Delta = \Delta_U$. We denote the space of lattice in $\mathfrak{U}_{\mathbb{R}}$ by $L(\mathfrak{U}_{\mathbb{R}})$. A unipotent subgroup $U \subset \Gamma$ is said to be quasimaximal if $(C \cap \Gamma)^u \subset U$. Let $M \subset N_{\mathbb{R}}$. In [5] (Theorem 2) the following is proved.

5.4.1. LEMMA. If $U$ is quasimaximal and (Ad $M)U$ is relatively compact in $L(\mathfrak{U}_{\mathbb{R}})$, then $\pi(N)$ is relatively compact in $G_{\mathbb{R}}/\Gamma$.

5.4.2. LEMMA. If $U$ is maximal, then $(N \cap \Gamma)^u = U$, and hence, $U$ is quasimaximal.

PROOF. Assume the contrary and let  $u \in (N \cap \Gamma)^{u}$ , but  $u \notin U$ . Since  $u \in N$  and U is nilpotent, the subgroup S generated by  $u \cup U$  is soluble. Therefore (see 4.3.2), S is unipotent, and since  $S \subset \Gamma$  and  $S \supset U$  but  $S \neq U$ , U is not maximal, which is a contradiction.

5.4.3. LEMMA. If $U$ is quasimaximal, then $C_{\mathbf{R}}$ is $\Gamma$-compact.

PROOF. It follows from Lemma 5.4.1 that $\pi(C_{\mathbf{R}})$ is relatively compact in $G_{\mathbf{R}}/\Gamma$. On the other hand (see 5.2.3), $C_{\mathbf{R}}$ is $\Gamma$-proper. Therefore, $C_{\mathbf{R}}$ is $\Gamma$-compact.

5.5. We denote by $A(U)$ the Zariski closure of $N(\overline{U}) \cap \Gamma$, and by $A^0(U)$ the connected component of the identity of $A(U)$. If it is clear what subgroup

U we mean, we simply write A and  $A^{0}$  instead of  $A(U)$  and  $A^{0}(U)$ . An algebraic subgroup H of G is said to be  $\Gamma$ -regular if  $H_{R}$  is  $\Gamma$ -proper and  $H \cap \Gamma$  is Zariski dense in H.

5.5.1. LEMMA. Suppose that $U$ is quasimaximal, $H \subset N$, and $H$ is $\Gamma$-regular. Put $B = H / H \cap C$ and let $f$ denote the natural homomorphism $H \to B$: 1) $f(H \cap \Gamma)$ is a Zariski-dense arithmetic subgroup of $B$; 2) if $H \cap C = \{e\}$, then $H \cap \Gamma$ is a Zariski-dense arithmetic subgroup of $H$.

$\mathfrak{U} = \{T_h(u) = (\operatorname{Ad} h)u, h \in H, u \in \mathfrak{U}\}$. Since $\overline{U}$ is connected, $C = C(\mathfrak{U})$ and hence $H \cap C$ is the kernel of $T$. Therefore, $T$ induces a faithful representation $T'$ of $B$ in $\mathfrak{U}$. We identify $B$ with $T'(B)$ and put

$B_{\mathbf{Z}} = \{b \in B; (\operatorname{Ad} b)\Delta = \Delta\}$. By Lemma 5.2.4, $f(H \cap \Gamma) \subset B_{\mathbf{Z}}$. Since $H \cap \Gamma$ is Zariski-dense in $H$, we see that $f(H \cap \Gamma)$, and hence also $B_{\mathbf{Z}}$, is Zariski-dense in $B$. Therefore ([4], AG, 14.4), the group $B$ is defined over $\mathbf{Q}$ and $B_{\mathbf{Z}}$ is an arithmetic subgroup of $B$. Since $U$ is quasimaximal and $H_{\mathbf{R}}$ is $\Gamma$-proper, (see 5.4.1) $H_{\mathbf{R}} \cap f^{-1}(B_{\mathbf{Z}})$ is relatively compact in $H_{\mathbf{R}} / H \cap \Gamma$. On the other hand (see 2.2.1), $f(H_{\mathbf{R}})$ is a subgroup of finite index in $B_{\mathbf{R}}$, and hence $f(H_{\mathbf{R}} \cap f^{-1}(B_{\mathbf{Z}}))$ is of finite index in $B_{\mathbf{Z}}$. Therefore, $B_{\mathbf{Z}}$ is relatively compact in $B_{\mathbf{R}} / f(H \cap \Gamma)$, and since $B_{\mathbf{Z}}$ and $f(H \cap \Gamma)$ are discrete, and $f(H \cap \Gamma) \subset B_{\mathbf{Z}}$, $f(H \cap \Gamma)$ is a subgroup of finite index in $B_{\mathbf{Z}}$, which completes the proof of 1). If $H \cap C = \{e\}$, then $f$ is an isomorphism of algebraic groups, and therefore 2) follows from 1).

5.5.2. LEMMA. If $U$ is quasimaximal, $H \subset N$, and $H$ is $\Gamma$-regular, then $H_{\mathbf{R}} \cap \Gamma$ is a Zariski-dense lattice in $H_{\mathbf{R}}$.

PROOF. Let $B$ and $f$ be as in Lemma 5.5.1. Then (see 5.5.1 and 4.1.1) $f(H \cap \Gamma)$ is a lattice in $B_{\mathbb{R}}$. But (see 2.2) the homomorphism

$\varphi: H_{\mathbf{R}}/H_{\mathbf{R}} \cap C_{\mathbf{R}} \rightarrow B_{\mathbf{R}}$ induced by $f$ is a bicontinuous isomorphism of the Lie group $H_{\mathbf{R}}/H_{\mathbf{R}} \cap C_{\mathbf{R}}$ onto a closed subgroup of finite index in $B_{\mathbf{R}}$. Therefore, $\varphi(A \cap \Gamma)$ is a lattice in $B_{\mathbf{R}}$. On the other hand, since (see 5.4.3) $C_{\mathbf{R}}$ is $\Gamma$-compact, and $H_{\mathbf{R}}$ is $\Gamma$-proper, (see 2.1.4) $H_{\mathbf{R}} \cap C_{\mathbf{R}}$ is $\Gamma$-compact. Therefore $H_{\mathbf{R}} \cap \Gamma$ is a lattice in $H_{\mathbf{R}}$.

5.5.3. LEMMA. 1) $A \subset S$; 2) $A$ is $\Gamma$-regular; 3) $A \cap \Gamma = S \cap \Gamma$.

PROOF. 1) and 3) follow from Lemma 5.2.4. From 1), Lemma 5.2.2 and the fact that $A \cap \Gamma = S \cap \Gamma$, it follows that $A_{\mathbf{R}}$ is $\Gamma$-proper, and since $A \cap \Gamma$ is Zariski-dense in $A$, $A$ is $\Gamma$-regular.

From Lemmas 5.5.2 and 5.5.3 we deduce:

5.5.4. LEMMA. If $U$ is quasimaximal, then $A_{\mathbf{R}} \cap \Gamma$ is a Zariski-dense lattice in $A_{\mathbf{R}}$.

5.5.5. LEMMA. Suppose that $U$ is quasimaximal, $H \subset N$, $H$ is $\Gamma$-proper, and $H \cap C = \{e\}$. We put $H_{\mathbf{Z}} = \{h \in H; (\operatorname{Ad} h)\Delta = \Delta\}$. Then $H \cap \Gamma$ and $H_{\mathbf{Z}}$ are commensurable.

PROOF. Since  $H \cap C = \{e\}$ , the homomorphism  $f: H \to B = H/H \cap C$  defined in Lemma 5.5.1 is an isomorphism of algebraic groups. Repeating the proof of Lemma 5.5.1 verbatim, we find that  $H_{Z} = B_{Z}$  and  $H \cap \Gamma = f(H \cap \Gamma)$  are commensurable.

## §6. Horosphericity of the maximal unipotent subgroups of Γ

6.1. LEMMA. Let V be a unipotent algebraic R-group, W a proper algebraic subgroup of V defined over R. Then 1)  $V_{R}$  contains a one-parameter subgroup  $v(t)$  that tends to infinity in  $V_{R}/W_{R}$ ; 2)  $V_{R}/W_{R}$  is non-compact.

PROOF. We denote by $V'$ the factor group of $V$ by its derived group, and by $f$ the natural homomorphism $V \to V'$. Since $V$ is a unipotent algebraic $\mathbf{R}$-group, $V'$ is also a unipotent algebraic $\mathbf{R}$-group. On the other hand, since $W$ is a proper subgroup of the nilpotent group $V$, (by [13], Corollary 10.3.3) $f(W)$ is a proper subgroup of $V'$, and, since the homomorphism $f$ is defined over $\mathbf{R}$ (by [4], Chapter I, 1.4), $f(W)$ is an algebraic subgroup of $V'$ defined over $\mathbf{R}$. We also note that since $V'$ is unipotent, the Lie group $V_{\mathbf{R}}'$ is connected and, therefore, (by 2.2) $f(V_{\mathbf{R}}) = V_{\mathbf{R}}'$. Hence it suffices to prove the lemma for commutative $V$. But then $V_{\mathbf{R}}$ is isomorphic to $\mathbf{R}^n$ (for some $n$), and $W_{\mathbf{R}}$ to a proper linear subspace of $\mathbf{R}^n$, and the existence of $v(t)$ is obvious in this case. Thus, 1) is proved. Now 2) follows immediately from 1).

6.2. Let  $T^{t}$  be a one-parameter group of unipotent linear transformations of the Euclidean space  $R^{n}$ . The group  $T^{t}$  induces a group of continuous transformations in the space  $A_{n}$  of lattices of full dimension in  $R^{n}$  (with the natural topology of  $A_{n}$ ). We note that  $A_{n}$  can be identified with  $GL_{n}(\mathbf{R})/GL_{n}(\mathbf{Z})$ . In [14] the following is proved.

6.2.1. LEMMA. The trajectory of any point  $x \in A_{n}$  under the action of the semigroup  $T^{t}$  ( $t \geqslant 0$ ) does not tend to infinity in  $A_{n}$ .

6.3. As before, let U be a unipotent subgroup of  $\Gamma$ .

6.3.1. LEMMA. Let $v(t)$ be a one-parameter unipotent subgroup of $N_{\mathbf{R}}$. If $U$ is quasimaximal, then $v(t)$ does not tend to infinity in $N_{\mathbf{R}} / A_{\mathbf{R}}$.

PROOF. Since (Ad $v(t)$) is a one-parameter unipotent subgroup (because $v(t)$ is unipotent), (Ad $v(t)$) $\mathfrak{U}_{\mathbf{R}} = \mathfrak{U}_{\mathbf{R}}$ and (see 3.1) $\Delta$ is a lattice of full dimension in $\mathfrak{U}_{\mathbf{R}}$, we see that (see 6.2.1) (Ad $v(t)$) $\Delta$ does not tend to infinity in $L(\mathfrak{U}_{\mathbf{R}})$. Therefore (see 5.4.1), $v(t)$ does not tend to infinity in $G_{\mathbf{R}} / \Gamma$. But (see 5.2.5) $v(t) \subset V \subset S$, and (see 5.2.2) $S_{\mathbf{R}}$ is $\Gamma$-proper. Therefore $v(t)$ does not tend to infinity in $S_{\mathbf{R}} / S_{\mathbf{R}} \cap \Gamma$ and (see 5.5.3) $A \subset S$. Therefore, $v(t)$ does not tend to infinity in $N_{\mathbf{R}} / A_{\mathbf{R}}$.

6.3.2. LEMMA. If $U$ is quasimaximal, then $A \supset R_{u}(N)$, and hence, $R_{u}(A) \supset R_{u}(N)$.

PROOF. We put  $V = R_{u}(N)$  and assume the contrary, that is, that  $A \cap V$  is a proper subgroup of V. Then (see 6.1)  $V_{R}$  contains a one-parameter unipotent subgroup  $v(t)$  tending to infinity in  $V_{R}/A_{R} \cap V_{R}$ . By Lemma 2.3  $v(t)$  tends to infinity in  $N_{R}/A_{R}$ , which contradicts Lemma 6.3.1.

6.3.3. LEMMA. If $U$ is quasimaximal, then $R_{n}(A) = R_{u}(A)$.

PROOF. Since  $R_{n}(A)$  is unipotent and connected,  $R_{n}(A) = T \times R_{u}(A)$ , where T is a torus. Since  $R_{n}(A)$  is a normal subgroup of A, and T is the unique maximal torus in  $R_{n}(A)$ , T is normal in A. But the group of

automorphisms of $T$ is countable. Therefore, $T \subset C(A^{0})$. On the other hand, 1) since (see 6.3.2) $A \supset R_{u}(N) \supset R_{u}(C)$ and the unipotent group $R_{u}(C)$ is connected, $A^{0} \supset R_{u}(C)$; 2) since the unipotent group $\overline{U}$ is connected and $N \cap \Gamma \supset U$, $A^{0} \supset \overline{U}$. Therefore,

$$
T \subset C (\overline {{U}}) \cap C (R _ {u} (C)).\tag{1}
$$

By Lemma 5.3.1 and the quasimaximality of $U$, $U \neq \{e\}$. Therefore (see 1.5), $U$, and hence, also $\overline{U}$ is not contained in any non-trivial normal algebraic subgroup of $G$. From this, (1), and Lemma 4.4.1 it follows that $T = \{e\}$, that is, that $R_{n}(A) = R_{u}(A)$.

6.4. THEOREM. Let $U$ be a maximal unipotent subgroup of $\Gamma$. Then $\overline{U}$ is a horospherical subgroup of $G$.

PROOF. Put $D = R_n(A)$, $V = R_n(A)$. Since (by 5.4.2) $U$ is quasimaximal, (see 5.5.4) $A_{\mathbf{R}} \cap \Gamma$ is a Zariski-dense lattice in $A_{\mathbf{R}}$. Therefore (see 1.3.2) $D_{\mathbf{R}}$ is $\Gamma$-compact, and since (see 6.3.3) $D = V$, $V_{\mathbf{R}}$ is $\Gamma$-compact. On the other hand, since $U$ is maximal, and $V \supset U$ (because $A$ contains and normalizes $\overline{U}$), $V_{\mathbf{R}} \cap \Gamma = U$. Therefore, $V_{\mathbf{R}} / \overline{U}_{\mathbf{R}}$ is compact, and hence (see 6.1), $V = \overline{U}$. But (see 6.3.2) $\overline{U} \subset R_u(N) \subset R_u(A) = V$. Therefore, $\overline{U} = R_u(N)$, This proves the theorem.

## §7. Opposite horospherical subgroups and their intersections with Γ

In this section we use the notation introduced in §5.

7.1. Two horospherical subgroups of G are said to be opposite if their normalizers are opposite parabolic subgroups of G. The main aim of this section is to prove the following theorem.

7.1.1. THEOREM. $\Gamma$ contains non-trivial unipotent subgroups $U_{1}$ and $U_{2}$ such that $\overline{U}_{1}$ and $\overline{U}_{2}$ are opposite horospherical subgroups of $G$ and $\dim A(U_{1}) > \dim \overline{U}_{1}$, $\dim A(U_{2}) > \dim \overline{U}_{2}$.

7.1.2. REMARK. The following conditions are equivalent:

1) $\dim A(U) > \dim \overline{U}$; 2) $A^0 (U)\neq \overline{U}$; 3) $U$ has infinite index in $N(\overline{U})\cap \Gamma$; 4) $\overline{U}$ has infinite index in $A(U)$.

7.2. Let $U$ and $U'$ be unipotent subgroups of $\Gamma$. We put $N = N(\overline{U})$, $N' = N(\overline{U}')$, $S = S(\overline{U})$, $S' = S(\overline{U}')$, $A = A(U)$, $A' = A(\overline{U}')$. Since (see 5.2.5) $N^u = S^u$, (by 5.2.2) $S_{\mathbf{R}}$ is $\Gamma$-proper, and (by 3.2.1) $\overline{U}_{\mathbf{R}}'$ is $\Gamma$-compact, we have:

7.2.1. LEMMA. The subgroup $N_{\mathbf{R}} \cap \overline{U}_{\mathbf{R}}'$ is $\Gamma$-compact and hence, (by 3.2) $N \cap \overline{U}' \cap \Gamma$ is Zariski-dense in $N \cap \overline{U}'$.

7.2.2. LEMMA. If $U$ and $U'$ are maximal and $U \cap U' = \{e\}$, then $\overline{U}$ and $\overline{U}'$ are opposite horospherical subgroups of $G$.

PROOF. Since (by 5.4.2) $(N\cap \Gamma)^{u} = U$, (by 5.1) $\overline{U}'\cap \Gamma = U'$, and $U\cap U' = \{e\}$, we have $N\cap \overline{U}'\cap \Gamma = \{e\}$. On the other hand, (by 7.2.1) $N\cap \overline{U}'\cap \Gamma$ is Zariski-dense in $N\cap \overline{U}'$. Therefore, $N\cap \overline{U}' = \{e\}$.

Similarly, $N' \cap \overline{U} = \{e\}$. Thus, (see 6.4 and 4.2.1), $N$ and $N'$ are parabolic

subgroups of G, and  $N \cap R_{u}(N') = N' \cap R_{u}(N) = \{e\}$ . Therefore, ([10], 4.10) N and  $N'$  are opposite parabolic subgroups of G. This proves the lemma.

DEFINITION 1. A maximal unipotent subgroup U of  $\Gamma$  is said to be ultramaximal if  $\dim A(U) = \dim U$  or, equivalently, if U is a subgroup of finite index in  $A(U)$ .

DEFINITION 2. We say that $\Gamma$ is split if all the maximal unipotent subgroups of $\Gamma$ are ultramaximal.

7.2.3. LEMMA. If $U$ is ultramaximal, then $U$ is a maximal unipotent $\mathbf{R}$-subgroup of $G$.

PROOF. We assume that U is a proper subgroup of some maximal unipotent R-subgroup V of the group G. Since V is nilpotent, and ([13], Corollary 10.3.1) since any proper subgroup of a nilpotent subgroup is a proper subgroup of its normalizer,  $\overline{U}$  is a proper subgroup of  $V \cap N$ . Therefore (by 6.1),  $(V \cap N)_{\mathbb{R}}$  contains a one-parameter unipotent subgroup  $v(t)$ , tending to infinity in  $(V \cap N)_{\mathbb{R}} / \overline{U}_{\mathbb{R}}$ , and hence, also in  $N_{R} / \overline{U}_{R}$ . But since U is ultramaximal,  $A / \overline{U}$  is finite. Therefore,  $v(t)$  tends to infinity in  $N_{R} / A_{R}$ , which contradicts Lemma 6.3.1 and the fact that U is quasi-maximal (see 5.4.2). This proves the lemma.

7.3. Just as  $S(U)$  was defined (in 5.1), so we denote for any algebraic subgroup V of G by  $S(V)$  the subgroup of  $N(V)$  consisting of the elements whose determinant under the natural action on the Lie algebra of V is equal to  $\pm1$ .

7.3.1. LEMMA. Let $V$ and $V'$ be opposite horospherical subgroups of $G$. Then $S(V) \cap N(V') = N(V) \cap S(V') = S(V) \cap S(V')$.

PROOF. We put $P = N(V)$, $P' = N(V')$, $L = P \cap P'$. Since $P$ and $P'$ are opposite parabolic subgroups, by §4.8 of [10], there exist a maximal torus $T \subset G$ and an order on the set $\Phi$ of roots of $G$ with respect to $T$ such that $P = P_{\theta}$, $P' = P_{\theta}^{-}$, $V = R_{u}(P) = R_{u}(P_{\theta}) = V_{\theta}$, $V' = V_{\theta}^{-}$ for some $\theta \subset \Delta$. There is an automorphism $f$ of $G$ preserving $T$ and inducing the automorphism $t \to t^{-1}$ on $T$ ([20], exposé 24, part I, or [10], 3.8). It is clear that $f(G_{\alpha}') = G_{-\alpha}'$ for any $\alpha \in \Phi$, and therefore $f(V) = f(V_{\theta}) = V_{\theta}^{-}$, $f(V') = V$. From this it follows that $T \cap S(V) = T \cap S(V')$, and since $T \cap S(V) = T \cap S(V')$, and since $T \supset R(L) = R_n(L)$ (because $T$ is a maximal torus in $G$),

$$
R (L) \cap S (V) = R (L) \cap S (V ^ {\prime}).\tag{1}
$$

Let $F$ be a maximal connected semisimple subgroup of $L$. Since $F$ has no non-trivial characters,

$$
F \cap S (V) = F \cap S (V ^ {\prime}).\tag{2}
$$

Since ([10], 4.3) P is connected and L is the Levi subgroup of P, L is reductive and connected. Therefore ([10], 2.2), L is the almost direct product of  $R(L)$  and F. The assertion of the lemma follows from this and

from (1) and (2).

7.4. LEMMA. For any unipotent subgroup $U$ of $\Gamma$ there is a $\gamma \in \Gamma$ such that $\gamma \overline{U}\gamma^{-1} \cap \overline{U} = \{e\}$.

PROOF. Since $R_{u}(G) = \{e\}$, there exists ([9], 2.2) a non-empty open subset $X$ of $G$ such that for each $x \in X$ we have $x\overline{U}x^{-1} \cap \overline{U} = \{e\}$. But (by 1.4) $\Gamma$ is dense in $G$. Therefore, $\Gamma \cap X \neq \emptyset$, which proves the lemma. 7.5. We prove two lemmas.

7.5.1. LEMMA. For any ultramaximal unipotent subgroup $U$ of $\Gamma$ there is a unipotent subgroup $W$ of $\Gamma$ such that $U \cap W \neq \{e\}$ and $W \subset U$.

PROOF. By Lemma 7.4, there is a $\gamma \in \Gamma$ such that $\gamma U\gamma^{-1} \cap U = \{e\}$. We put $U' = \gamma U\gamma^{-1}$, $N = N(\overline{U})$, $N' = N(\overline{U}')$, $S = S(\overline{U})$, $S' = S(\overline{U}')$, $L = N \cap N'$, $F = S \cap S'$. Since $U$ is ultramaximal, so is $U'$. Since (see 7.2.2) $N$ and $N'$ are opposite parabolic subgroups, 1) ([10]. 4.18) $L$ contains a maximal $\mathbf{R}$-split torus $T$ of $G$; 2) (see 7.3) $F = S \cap N'$. On the other hand, 1) $\dim T \geqslant 2$ (because $\operatorname{rank}_{\mathbb{R}} G \geqslant 2$); 2) $\dim S \geqslant \dim N - 1$, consequently, $\dim(S \cap N') \geqslant \dim L - 1$. Therefore, $\dim(T \cap F) \geqslant 1$, and so $T \cap F$ contains an $\mathbf{R}$-split torus $D$ of positive dimension. Because of this property of $D$, $D_{\mathbb{R}}$ is non-compact.

Since (by 5.2.2) $S_{\mathbf{R}}$ and $S_{\mathbf{R}}^{\prime}$ are $\Gamma$-proper subgroups, (see 2.1.3) $F_{\mathbf{R}}$ is $\Gamma$-proper. On the other hand, since $U$ is of finite index in $N \cap \Gamma$ (because $\dim A(U) = \dim \overline{U}$), and $F \cap U = \{e\}$ (because $N$ and $N^{\prime}$ are opposite and $F \subset L$), $F \cap \Gamma$ is finite. Therefore, the restriction of $\pi$ to $F_{\mathbf{R}}$ is a proper map, and hence, the restriction of $\pi$ to $D_{\mathbf{R}}$ is proper ($\pi: G_{\mathbf{R}} \to G_{\mathbf{R}} / \Gamma$). Let $V$ be a Zassenhaus neighbourhood in $G_{\mathbf{R}}$ and $\widetilde{W}$ a neighbourhood of zero in $\mathfrak{G}_{\mathbf{R}}$, such that $\exp \widetilde{W} \subset V$. Since the restriction of $\pi$ to $D_{\mathbf{R}}$ is proper and $D \subset S$, by Lemmas 5.4.1 and 5.4.2 and Mahler's compactness criterion, there is a compact $K \subset D_{\mathbf{R}}$ such that if $g \in D_{\mathbf{R}} - K$, then $\widetilde{W} \cap (\operatorname{Ad} g)\Delta_U \neq \{0\}$. Since (see 3.1) $\Delta_U \subset \ln U$, we see that $V \cap gUg^{-1} \neq e$ for $g \in D_{\mathbf{R}} - K$. Similarly, there exists a compact $K^{\prime} \subset D_{\mathbf{R}}$ such that if $g \in D_{\mathbf{R}} - K^{\prime}$, then $V \cap gU^{\prime}g^{-1} \neq \{e\}$. Since $D_{\mathbf{R}}$ is non-compact, $D_{\mathbf{R}} - (K \cup K^{\prime}) \neq \emptyset$. Suppose that $g \in D_{\mathbf{R}} - (K \cup K^{\prime})$. Then (by 2.4) the subgroup $\Lambda$ generated by $V \cap (gUg^{-1} \cup gU^{\prime}g^{-1})$ is nilpotent, and hence (see 4.3.2) is unipotent. We put $W = g^{-1}\Lambda g$. Then: 1) $W$ is unipotent 2) $W \cap U \neq \{e\}$ (because $V \cap gUg^{-1} \neq \{e\}$); 3) $W \not\subset U$ (because $W \cap gU^{\prime}g^{-1} \neq \{e\}$ and $U \cap U^{\prime} = \{e\}$). This proves the lemma.

7.5.2. LEMMA. If $\Gamma$ is split, and $U$ is a maximal unipotent subgroup of $\Gamma$, then $U$ contains a subgroup $V$ such that $\{e\} \neq \overline{V} \neq \overline{U}$, $\overline{V}$ is a horospherical subgroup of $G$, and $N(\overline{V}) \supset N(\overline{U})$.

PROOF. Since $\Gamma$ is split, $U$ is ultramaximal. Therefore, (by 7.5.1) there is a maximal unipotent subgroup $W \subset \Gamma$ such that $U \cap W \neq \{e\}$ and $W \neq \overline{U}$. We denote by $\overline{V}$ the normal subgroup of $\overline{U}$ generated by $\overline{U} \cap \overline{W}$. Since (by 3.2.1) $\overline{U}_{\mathbf{R}}$ and $\overline{W}_{\mathbf{R}}$ are $\Gamma$-compact, (by 2.1.4) ($\overline{U} \cap \overline{W}$)$_{\mathbf{R}}$ is $\Gamma$-compact, and hence (by 3.2.1) $\overline{U} \cap \overline{W} \cap \Gamma$ is Zariski-dense in $\overline{U} \cap \overline{W}$. Therefore, $V = \overline{V} \cap \Gamma$ is Zariski-dense in $\overline{V}$. Like $U$, the subgroup $W$ is

ultramaximal. Therefore, (see 7.2.3) $\overline{U}$ and $\overline{W}$ are maximal unipotent R-subgroups of $G$, with $\overline{U} \cap \overline{W} \neq \{e\}$, $\overline{U} = \overline{W}$, and hence (by 4.5.4) $\overline{V}$ is a non-trivial horospherical subgroup of $G$, with $\overline{V} \neq \overline{U}$ and $N(\overline{V}) \supset N(\overline{U})$. This proves the lemma.

7.6. PROOF OF THEOREM 7.1.1 IN CASE $\Gamma$ IS SPLIT. Let $U$ be a maximal unipotent subgroup of $\Gamma$. By Lemma 7.4, there is a $\gamma \in \Gamma$ such that $\gamma \overline{U}\gamma^{-1} \cap \overline{U} = \{e\}$. We put $U' = \gamma U\gamma^{-1}$. Since $\Gamma$ is split, $U$ and $U'$ are ultramaximal, and (by 7.2.3) $\overline{U}$ and $\overline{U}'$ are maximal unipotent R-subgroups of $G$. Therefore, (by 4.5.3) $N(\overline{U}) \cap N(\overline{U}')$ contains a maximal R-split torus $S$ of $G$. We use the notation of §4.5. Since $\overline{U} \cap \overline{U}' = \{e\}$, (by 4.5.4) we may assume that $\overline{U} = V_{\varnothing}, \overline{U}' = V_{\varnothing'}$. Let $V$ be a subgroup satisfying the conclusion of Lemma 7.5.2. Since $N(\overline{V}) \supset N(\overline{U}) = N(V_{\varnothing}) = P_{\varnothing}$, ([10], 5.14) $N(\overline{V}) = P_{\theta}$ and $\overline{V} = R_u(N(\overline{V})) = R_u(P_\theta) = V_\theta$. Since $\overline{V} \neq \overline{U} = V_{\varnothing}$, we have $\theta \neq \emptyset$.

Let $W_1$ and $W_2$ be the normal subgroups of $V_{\varnothing}^{-} = \overline{U}'$ and $B_{\theta}^{-} \widetilde{\times} \overline{V} = B_{\theta}^{-} \widetilde{\times} V_{\theta}$, respectively, generated by $B_{\theta}^{-} = P_{\theta} \cap V_{\varnothing}^{-}$. Let (see 4.5.6) $z \in Z_{\theta}$ be such that $zB_{\theta}^{-}z^{-1} = B_{\theta}$. Then $zW_2z^{-1}$ is the normal subgroup of $zB_{\theta}^{-}z^{-1}\widetilde{\times}z\overline{V}z^{-1} = B_{\theta}\widetilde{\times}V_{\theta}$ generated by $zB_{\theta}^{-}z^{-1} = B_{\theta}$. Therefore, (by 4.5.2) $zW_2z^{-1} = V_{\Delta - \theta}$. From Lemma 4.5.2 it also follows that $W_1 = V_{\Delta - \theta}^{-}$. Using (3) and (4) of §4.5 (p. 119) we find that $zN(W_2)z^{-1} = N(zW_2z^{-1}) = N(V_{\Delta - \theta}) = P_{\Delta - \theta}, N(W_1) = N(V_{\Delta - \theta}^{-}) = P_{\Delta - \theta}^{-}$, and hence, $zN(W_2)z^{-1}$ and $N(W_1)$ are opposite parabolic subgroups. Therefore, ([10], 4.12 and 4.10) the set $M$ of those $g \in G$ for which $gN(W_2)g^{-1}$ and $N(W_1)$ are opposite parabolic subgroups, is non-empty and Zariski-open in $G$. But (by 1.4) $\Gamma$ is Zariski-dense in $G$. Therefore, there is a $\gamma \in \Gamma$ such that $\gamma N(W_2)\gamma^{-1}$ and $N(W_1)$ are opposite parabolic subgroups of $G$. Then $\gamma W_2\gamma^{-1}$ and $W_1$ are opposite horospherical subgroups of $G$. Since (by 7.2.1) $N(\overline{V}) \cap \overline{U}' \cap \Gamma = P_{\theta} \cap V_{\theta}^{-} \cap \Gamma = B_{\theta}^{-} \cap \Gamma$ is Zariski-dense in $N(\overline{V}) \cap \overline{U}' = P_{\theta} \cap V_{\theta}^{-} = B_{\theta}^{-}$, we see that $W_1 \cap \Gamma$ and $W_2 \cap \Gamma$ are Zariski-dense in $W_1$ and $W_2$. We put $U_1 = W_1 \cap \Gamma, U_2 = \gamma W_2\gamma^{-1} \cap \Gamma$. Since $\gamma \in \Gamma, U_2$ is Zariski-dense in $\gamma W_2\gamma^{-1}$. Therefore, $\overline{U}_1$ and $\overline{U}_2$ are opposite horospherical subgroups of $G$. Since $\theta \neq \emptyset, \overline{U}_1 = W_1 = V_{\Delta - \theta}^{-}$ is a proper normal subgroup of $\overline{U}' = V_{\varnothing}^{-}$. Therefore, $dim A(U_1) \geqslant dim U' > dim \overline{U}_1$. Similarly, $dim A(U_2) = dim A(W_2 \cap \Gamma) \geqslant dim(B_\theta\widetilde{\times}V_\theta) = dim(B_\theta\widetilde{\times}V_\theta) = dim V_\varnothing > dim V_{\Delta - \theta} = dim W_2 = dim \overline{U}_2$. This completes the proof of Theorem 7.1.1 when $\Gamma$ is split.

7.7. PROOF OF THEOREM 7.1.1 WHEN $\Gamma$ IS NOT SPLIT. Let $U_{1}$ be a maximal unipotent subgroup of $\Gamma$ that is not ultramaximal. Then (by 7.4) there is a $\gamma \in \Gamma$ such that

$$
\gamma \overline {{{U}}} _ {1} \gamma^ {- 1} \cap \overline {{{U}}} _ {1} = \{e \}.
$$

We put $U_{2} = \gamma U_{1}\gamma^{-1}$. By Lemma 7.2.2, $\overline{U}_{1}$ and $\overline{U}_{2}$ are opposite horospherical subgroups of $G$. But $U_{1}$ and $U_{2} = \gamma U_{1}\gamma^{-1}$ are not ultramaximal, hence $\dim A(U_{1}) > \dim \overline{U}_{1}$, and $\dim A(U_{2}) > \dim \overline{U}_{2}$.

## §8. A construction from representation theory

In this section $K$ denotes an algebraically closed field.

8.1. For any finite-dimensional linear space D over K and any natural number  $n (0 \leqslant n \leqslant \dim D)$  we denote by  $G_{n}(D)$  the algebraic variety of all the n-dimensional linear subspaces of D, and by  $G_{D}$  or  $G(D)$  the disjoint union of all the  $G_{n}(D)$ .

Let $A$ be a finite-dimensional space over $K$, and $B$ a linear subspace of $A$. For any natural number $l$ ($0 \leqslant l \leqslant \dim B$) we put $G(B, l) = \{g \in G_A; \dim(g \cap B) = l\}$. It is easy to see that the following lemmas are true.

8.1.1. LEMMA. For any $l$ ($0 \leqslant l \leqslant \dim A$): 1) $\bigcup_{\tilde{l} > l} G(B, \tilde{l})$ is an

algebraic subvariety of $G_A$; 2) the mapping of algebraic varieties $G(B, l) \to G_B$ that associates with $g \in G(B, l)$ the intersection $g \cap B$ is regular.

8.1.2. LEMMA. For any $l$ ($0 \leqslant l \leqslant \dim A$) and any $g \in G_l(A)$ there is a neighbourhood of $g$ in $G_l(A)$ and $l$ regular rational maps $f_1(u), \ldots, f_l(u)$ form a basis at $u$ for any $u \in U$.

8.1.3. LEMMA. For any $l$ the set of those $(g_1, \ldots, g_l) \in G_A^l$ for which $\bigcup_{1 \leq i \leq l} g_i$ generates $A$ as a linear space is Zariski-open in $A$.

8.2. NOTATION AND ASSUMPTIONS. Let $H$ be a connected algebraic $K$-group, $\Lambda \subset H$ a Zariski-dense subgroup, $T$ a faithful linear representation of $H$ in a finite-dimensional linear space $L$ over $K$, $M$ and $N$ linear subspaces of $L$, and $W$ a non-empty Zariski-open subset of $H$. We put $d = \min_{h \in H} \dim (N \cap T_h M)$ and assume that $\dim(M \cap T_w N) = \dim(N \cap T_{w^{-1}} M) = d$ for any $w \in W$. In addition, we assume that as linear spaces $M, N$ and $L$ are generated by the unions $\bigcup_{w \in W} (M \cap T_w N), \bigcup_{w^{-1} \in W} (N \cap T_w M)$ and $\bigcup_{h \in H} T_h M$.

respectively.

8.3. CONSTRUCTION OF THE SPACE $\Psi$ AND THE REPRESENTATION $T^{\Psi}$. We denote by $L_{M}$ and $L_{N}$ the direct sums $\bigoplus_{\lambda \in \Lambda} T_{\lambda} M$ and $\bigoplus_{\lambda \in \Lambda} T_{\lambda} N$ (we emphasize that they are direct sums, not direct products). For any $\lambda \in \Lambda$ we denote by $\alpha_{\lambda}$ and $\varphi_{\lambda}$ the natural embeddings of $T_{\lambda} M$ and $T_{\lambda} N$ into $L_{M} \oplus L_{N}$. By $E$ we denote the linear subspace of $L_{M} \oplus L_{N}$ generated by all the elements of the form $\alpha_{\lambda}(x) - \varphi_{\lambda'}(x)$, where $\lambda \in \Lambda$, $\lambda' \in \Lambda$, $\lambda^{-1} \lambda' \in W$, $x \in T_{\lambda} M \cap T_{\lambda'} N$, and we put $\Psi = (L_{M} \oplus L_{N}) / E$. We define a representation $P$ of $\Lambda$ in $L_{M} \oplus L_{N}$ by the formulae:

(1)

$$
P _ {\lambda^ {\prime}} \left(\alpha_ {\lambda} (x)\right) = \alpha_ {\lambda^ {\prime} \lambda} \left(T _ {\lambda^ {\prime}} x\right); \lambda^ {\prime} \in \Lambda , \lambda \in \Lambda , x \in T _ {\lambda} M,\tag{2}
$$

$$
P _ {\lambda^ {\prime}} \left(\varphi_ {\lambda} (y)\right) = \varphi_ {\lambda^ {\prime} \lambda} \left(T _ {\lambda^ {\prime}} y\right); \lambda^ {\prime} \in \Lambda , \lambda \in \Lambda , y \in T _ {\lambda} N.
$$

From (1) and (2) it is clear that $E$ is invariant under $P_{\lambda}$ for any $\lambda \in \Lambda$. Therefore, $P$ induces a representation $T^{\Psi}$ of $\Lambda$ in $\Psi$.

8.4. We prove two lemmas.

8.4.1. LEMMA. Let $H$ act rationally on an algebraic variety $X$ and let $U$ be a non-empty open subset of $X$. For any natural number $n$ we put

$$
U _ {n} = \{(x _ {1}, \dots , x _ {n}) \in X ^ {n}; \forall h \in H \exists i, 1 \leqslant i \leqslant n, h x _ {i} \in U \}.
$$

Then for some $n$ the subset $U_{n}$ is non-empty and open in $X^{n}$.

PROOF. For any $x \in X$ we put $H_x = \{h \in H; hx \notin U\}$. Then $H_x$ is closed and $\bigcap_{x \in X} H_x = \varnothing$. Since $H$ is compact in the Zariski topology, $\exists x_1, \ldots, x_n \in X$ such that $\bigcap_{1 \leqslant i \leqslant n} H_{x_i} = \varnothing$. Therefore, $U_x$ is non-empty

8.4.2. LEMMA. $\Lambda$ contains a finite set $\lambda_1, \ldots, \lambda_s$ such that for any $\lambda \in \Lambda$ the union $\bigcup_{\lambda^{-1}\lambda_i \in W} (T_\lambda M \cap T_{\lambda_i N})$ generates $T_\lambda M$ as a linear space.

PROOF. For any natural number $l$ we denote by $V_{l}$ the subset of $W^{l}$ consisting of all the $(w_{1},\ldots ,w_{l})$ such that $\bigcup_{1\leqslant i\leqslant l}(M\cap T_{w_i}N)$ generates $M$ as a linear space. Since $\bigcup_{h\in W}(M\cap T_hN)$ generates $M$, $V_{m}$ is non-empty, where $m = \dim M$. The dimension $\dim (M\cap T_wN) = d$ does not depend on $w\in W$. Therefore, (see 8.1.1 and 8.1.3) $V_{m}$ is open in $W^{m}$. Now $H$ acts naturally on the left on $H^{m}$ (by $h(h_{1},\dots,h_{m}) = (hh_{1},\dots,hh_{m})$). Since $V_{m}$ is open and non-empty and $\Lambda$ is dense in $H$, (by 8.4.1) there are sets $x_{j} = (\lambda_{1,j},\dots,\lambda_{m,j})$, $1\leqslant j\leqslant n$, such that for any $h\in H$ there is a $j$, $1\leqslant j\leqslant n$, for which $h^{-1}x_j\in V_m$. Let $\lambda_1,\ldots ,\lambda_s$ be the union of the sets $x_{j}$. Then for any $\lambda \in \Lambda$ the union $\bigcup_{\lambda^{-1}\lambda_i\in W}(M\cap T_{\lambda^{-1}\lambda_i}N)$ generates $M$, and

hence $\bigcup_{\lambda^{-1}\lambda_i\in W}(T_\lambda M\cap T_{\lambda_i}N)$ generates $T_{\lambda}M$.

8.5. Let $\beta$ be the natural map $L_M \oplus L_N \to (L_M \oplus L_N) / E = \Psi$, and let $\lambda_1, \ldots, \lambda_s$ be the set from Lemma 8.4.2. We put $\mathfrak{N} = \bigoplus_{1 \leqslant i \leqslant s} T_{\lambda_i} N$ and assume $\mathfrak{N}$ to be naturally embedded in $L_N \subset L_M \oplus L_N$. It follows from Lemma 8.4.2 that $\beta(L_M) \subset \beta(\mathfrak{N}) \subset \beta(L_N)$. Similarly, $\beta(L_N) \subset \beta(L_M) \subset \beta(\mathfrak{N})$. Thus, we have:

8.5.1. LEMMA. The space $\Psi$ is finite-dimensional. Moreover,

$$
\Psi = \beta (L _ {M}) = \beta (L _ {N}) = \beta (\mathfrak {N}).
$$

We denote by $t_M$ the natural linear map $L_M \to L$ defined by

We denote by $t_M$ the natural linear map $L_M \to L$ defined by $t_M(\alpha_\lambda(m)) = m (\lambda \in \Lambda, m \in T_\lambda M)$, and similarly we define $t_N: L_N \to L$. The mappings $t_M$ and $t_N$ give a linear map $t: L_M \oplus L_N \to L$. It is clear that $E \subset \operatorname{Ker} t$. Therefore, $t$ induces a linear map $p: \Psi \to L$ where for any $\lambda \in \Lambda$,

(3)

$$
p T _ {\lambda} ^ {\Psi} = T _ {\lambda} p.
$$

As before, $e$ is the identity of $H$. We put $M_e = \alpha_e(M)$.

8.5.2. LEMMA. Let $x \in \beta(M_e)$. We put $\omega_x(\lambda) = T_\lambda^\Psi(x), \lambda \in \Lambda$. Then the

map $\omega_{x}\colon\Lambda\to\Psi$ extends to a rational map $\omega_{x}^{\prime}\colon H\to\Psi$.

PROOF. We put $V = \bigcap_{1 \leqslant i \leqslant s} W^{-1} \lambda_i$ and note that $V = \{h \in H;$

$h^{-1}\lambda_{i}\in W\forall i,1\leqslant i\leqslant s\}$ . Since W is non-empty and Zariski-open in H, and since H is connected, V is non-empty and open. For any  $v\in V$  and any  $i(1\leqslant i\leqslant s)$  we put  $g_{i}(v)=T_{v}M\cap T_{\lambda_{i}}N\in G(T_{\lambda_{i}}N)$ . Since  $V^{-1}\lambda_{i}\subset W$ , we see that  $\dim g_{i}(v)=\dim(M\cap T_{v^{-1}\lambda_{i}}N)=d$ , hence (by 8.1.1) the map  $g_{i}:V\to G(T_{\lambda_{i}}N),1\leqslant i\leqslant s$ , is rational. Therefore, by Lemma 8.1.2, for any  $i(1\leqslant i\leqslant s)$  there are a non-empty open subset  $V_{i}$  of V and  $r=\dim N$  rational maps  $f_{i,1},\ldots,f_{i,r}$  of  $V_{i}$  into  $G(T_{\lambda_{i}}N)$  such that, for any  $v\in V_{i},f_{i,1}(v),\ldots,f_{i,r}(v)$  belong to  $T_{v}M\cap T_{\lambda_{i}}N$  and form a basis of  $T_{v}M\cap T_{\lambda_{i}}N$ . We put  $V^{\prime}=\bigcap_{1\leqslant i\leqslant s}V_{i}$ . Since the  $V_{i}$  are non-empty and open in H, and since H is connected,  $V^{\prime}$  is non-empty and open. For any  $v\in V^{\prime},\bigcup_{1\leqslant i\leqslant s}(T_{v}M\cap T_{\lambda_{i}}N)$  generates  $T_{v}M$ , and hence,  $\bigcup_{1\leqslant i\leqslant s,1\leqslant j\leqslant r}f_{i,j}(v)$  generates  $T_{v}M$ . Since the  $f_{i,j}(v)$  depend rationally on v, among the  $f_{i,j}$  we can choose m=dim M mappings  $f_{1},\ldots,f_{m}$  such that  $f_{1}(v),\ldots,f_{m}(v)$  form a basis of  $T_{v}M$  for any  $v\in V^{\prime\prime}$ , where  $V^{\prime\prime}$  is a non-empty open subset of  $V^{\prime}$ .

We put $x' = p(x) \in M$, and for any $v \in V''$ we express $T_v(x') \in T_vM$ in the basis $f_1(v), \ldots, f_m(v)$: $T_v(x') = c_1(v)f_1(v) + \ldots + c_m(v)f_m(v)$. Since $T_v(x')$ and $f_k(v)$ ($1 \leqslant k \leqslant m$) depend rationally on $v \in V''$, so do the $c_k(v)$ ($1 \leqslant k \leqslant m$). For any $k$ ($1 \leqslant k \leqslant m$) there is an $i(k)$ ($1 \leqslant i(k) \leqslant s$) such that $f_k(V'') \subset T_{\lambda_i(k)}N$.

We put $\omega_x'(v) = \sum_{k=1}^{m} c_k(v) \cdot \beta(\varphi_{\lambda i(k)}(f_k(v)))$, where $v \in V''$. If $\lambda \in \Lambda \cap V''$, then $\lambda \in \Lambda \cap V$ and, therefore, $\alpha_{\lambda}(y) = \varphi_{\lambda_i}(y)$ for any $i$ ($1 \leqslant i \leqslant s$) and any $y \in T_{\lambda}M \cap T_{\lambda_i}N$. On the other hand, it follows from the definition of $T^{\Psi}$ that $T_{\lambda}^{\Psi}(x) = \beta(\alpha_{\lambda}(T_{\lambda}(x')))$ for any $\lambda \in \Lambda$. Therefore, for any $\lambda \in \Lambda \cap V''$,

$$
\begin{array}{r l} \omega_ {x} ^ {\prime} (\lambda) & = \sum_ {k = 1} ^ {m} c _ {k} (\lambda) \cdot \beta \left(\varphi_ {\lambda i (k)} \left(f _ {k} (\lambda)\right)\right) = \\ & = \sum_ {k = 1} ^ {m} c _ {k} (\lambda) \cdot \beta \left(\alpha_ {\lambda} \left(f _ {k} (\lambda)\right)\right) = \beta \left(\alpha_ {\lambda} \left(\sum_ {k = 1} ^ {m} c _ {k} (\lambda) f _ {k} (\lambda)\right)\right) = \\ & = \beta \left(\alpha_ {\lambda} \left(T _ {\lambda} \left(x ^ {\prime}\right)\right)\right) = T _ {\lambda} ^ {\Psi} (x) = \omega_ {\lambda} (x). \end{array} \tag {4}
$$

Since $c_k(v)$ and $f_k(v)$ depend rationally on $v$, $\omega_x'(v)$ depends rationally on $v \in V''$. From this and from (4) it follows that $\omega_x(\lambda)$ extends to a rational map $\omega_x' \colon V'' \to \Psi$ on $V''$. On the other hand, since $V''$ is non-empty and open in the irreducible algebraic variety $H$, $\omega_x'$ is the restriction of a rational map of $H$ into $\Psi$. This proves the lemma.

8.5.3. LEMMA.  $T^{\Psi}$  extends to a faithful rational representation  $\overline{T}^{\Psi}$  of H.

PROOF. Since (by 8.5.1) $\Psi = \beta(L_M)$ and $\Psi$ is finite-dimensional, we can choose $\lambda_1, \ldots, \lambda_n \in \Lambda$ ($n = \dim \Psi$) and $z_i \in \alpha_{\lambda_i}(T_{\lambda_i}M) (1 \leqslant i \leqslant n)$ such that the $s_i$ form a basis of $\Psi$. We put

$$
\omega_ {i} (\lambda) = T _ {\lambda} ^ {\Psi} (z _ {i}) = T _ {\lambda \lambda_ {i}} ^ {\Psi} (T _ {\lambda_ {i} ^ {- 1}} ^ {\Psi} (z _ {i})), 1 \leqslant i \leqslant n, \lambda \in \Lambda .
$$

Then (by 8.5.2) the $\omega_{i}(\Lambda)\colon \Lambda \to \Psi$ extend to rational maps of $H$ into $\Psi$, and since the $z_{i}$ form a basis of $\Psi$, $T^{\Psi}$ extends to a rational map $\overline{T}^{\Psi}$ of $H$ into the algebraic group $GL(\Psi)$ of non-singular linear transformations of $\Psi$. Since the restriction of $\overline{T}^{\Psi}$ to a Zariski-dense subgroup is a homomorphism, $\overline{T}^{\Psi}$ itself is a homomorphism of $H$ into $GL(\Psi)$, that is, $\overline{T}^{\Psi}$ is a rational representation of $H$ in $\Psi$. Since $\bigcup_{h\in H}T_hM$ generates $L$, and $\Lambda$ is dense in $H$, $\bigcup_{\lambda \in \Lambda}T_\lambda M$ generates $L$. Therefore, the map $p\colon \Psi \to L$ defined previously is

an epimorphism. On the other hand, since $\Lambda$ is dense in $H$ and $\overline{T}^{\Psi}$ is a rational extension of $\overline{T}^{\Psi}$, by (3),

$$
p \overline {{T}} _ {h} ^ {\Psi} = T _ {h} p
$$

for any $h \in H$. Therefore, $T$ is a factor of $\Psi$, and since $T$ is faithful, so is $\overline{T}^{\Psi}$. This proves the lemma.

8.6. Let k be a subfield of K. Any k-structure on M (respectively, N) for any  $\lambda \in \Lambda$  induces in a natural way a k-structure on  $T_{\lambda}M$  (respectively,  $T_{\lambda}N$ ). We say that two k-structures on M and N are compatible if  $M \cap T_{\lambda}N$  for any  $\lambda \in \Lambda \cap W$  is a k-subspace of both M and  $T_{\lambda}N$ .

8.6.1. LEMMA. If there exist compatible k-structures on M and N, then there exists a  $T^{\Psi}(\Lambda)$ -invariant k-structure on  $\Psi$ .

PROOF. The k-structures on M and N induce in a natural way a  $P(\Lambda)$ -invariant k-structure on  $L_{M} \oplus L_{N}$ . Since the k-structures on M and N are compatible, E is a k-subspace of  $L_{M} \oplus L_{N}$ . Therefore, the k-structure on  $L_{M} \oplus L_{N}$  induces a  $T^{\Psi}(\Lambda)$ -invariant k-structure on  $\Psi$ .

8.6.2. LEMMA. If there exist compatible k-structures on M and N, then H can be given a k-structure such that  $\Lambda \subset H_{k}$ .

PROOF. Since  $T^{\Psi}$  is a faithful rational representation,  $\overline{T}^{\Psi}$  effects an isomorphism of the algebraic groups H and  $\overline{T}^{\Psi}(H)$ . On the other hand, (by 8.6.1)  $\overline{T}^{\Psi}(\Lambda) \subset (\overline{T}^{\Psi}(H))_{k}$ , and since  $\Lambda$  is dense in H, ([4], Ch. I, Proposition 1.3)  $\overline{T}^{\Psi}(H)$  is defined over k. Thus, the pair  $(\overline{T}^{\Psi}(H), (\overline{T}^{\Psi})^{-1})$  gives the required k-structure on H.

## §9. Proof of the “rationality” theorem

9.1. Let V be a horospherical subgroup of G, L an arbitrary Levi subgroup of  $N(V)$ .

9.1.1. LEMMA. If $V \neq \{e\}$ and $V$ is not contained in any non-trivial normal subgroup of $G$, then $L \cap C(V) = \{e\}$.

PROOF. We put $F = L \cap C(V)$. Since $C(V)$ is normal in $N(V)$, $L \subset N(F)$.

On the other hand, $V \subset C(F) \subset N(F)$. Since $V$ is horospherical, $N(V) = L \widetilde{\times} V$ and, therefore, $N(V) \subset N(F)$. But (see 4.2.1) $N(V)$ is parabolic. Therefore, $N(F)$ is parabolic. Now $F$ is normal in the reductive group $L$, and hence, $F$ is reductive. Therefore, the normalizer $N(F)$ of the reductive subgroup $F$ in the reductive group $G$ is reductive. Thus, $N(F)$ is a reductive parabolic subgroup of $G$. But from the classification of parabolic subgroups ([10], 4.3) it follows that any reductive parabolic subgroup of $G$ coincides with $G$. Therefore $F$ is normal in $G$. Assume that $F \neq \{e\}$. Since $F$ is normal in $G$ and $G$ is a connected semisimple group with trivial centre, we see that $F \supset G'$, $G = G' \times G''$, $G' \neq \{e\}$, $G'$ is simple. Since $G'' \neq G$, $V \notin G''$. But $G'$ is simple. Therefore, $C(V) \cap G' \neq G'$, and hence, $F \subset C(V) \not\supset G'$. This is a contradiction, and the lemma is proved.

9.2. LEMMA. Let $H$ be an algebraic group, $H = L \tilde{\times} N$, $\Lambda$ a Zariski-dense arithmetic subgroup of $L$, $\Psi$ a Zariski-dense arithmetic subgroup of $N$, where $\Lambda$ normalizes $\Psi$. Then $\Lambda \cdot \Psi$ is a Zariski-dense arithmetic subgroup of $H$.

PROOF. Let $\alpha: L \times N \to N$ be an action of $L$ on $N$ (defined by $\alpha(l, n) = \ln l^{-1}$). Since $\Lambda$ normalizes $\Psi$, we have $\alpha(\Lambda \times \Psi) \subset \Psi$. But $\Lambda$ and $\Psi$ are dense arithmetic subgroups of $L$ and $N$. Therefore, $\alpha$ takes a dense set of integral points in $L \times N$ to a set of integral points in $N$. Therefore, $\alpha$ is defined over $\mathbf{Q}$. Hence, we can put a $\mathbf{Q}$-structure on $L \widetilde{\times} N$, inducing $\mathbf{Q}$-structures on $L$ and $N$, relative to which $\Lambda$ and $\Psi$ are arithmetic subgroups (see Remark 3.4.2). Then ([7], 6.4) $L_{\mathbf{Z}} \cdot N_{\mathbf{Z}}$ is of finite index in $H_{\mathbf{Z}}$. Also, $\Lambda \cdot \Psi$ is dense in $H = L \cdot N$, since $\Lambda$ is dense in $L$ and $\Psi$ in $N$.

9.3. Let $U$ and $U'$ be unipotent subgroups of $\Gamma$ (as before, $U = \overline{U} \cap \Gamma$, $U' = \overline{U'} \cap \Gamma$). We put $N = N(\overline{U})$, $N' = N(\overline{U'})$, $S = S(\overline{U})$, $S' = S(\overline{U'})$, $A = A(U)$, $A' = A(U')$, $A_0 = A^0(U)$, $A_0' = A^0(U')$ (§§5.1 and 5.5).

9.3.1. LEMMA. If $\overline{U}$ and $\overline{U}'$ are opposite horospherical subgroups of $G$, then $(N \cap N' \cap \Gamma) \cdot U$ is of finite index in $N \cap \Gamma$.

PROOF. Since $N$ and $N'$ are opposite parabolic subgroups and $U$ is horospherical, $N = (N \cap N') \tilde{\times} \overline{U}$. But by Lemma 5.2.5, $\overline{U} = R_u(N) = R_u(S)$. Therefore, $S = (S \cap N') \tilde{\times} \overline{U}$, and since (by 7.3) $S \cap N' = S \cap S'$, we have $S = (S \cap S') \tilde{\times} \overline{U}$ and $S_R = (S \cap S')_R \tilde{\times} \overline{U}_R$. Since (by 5.2.2) $S_R$ and $S'_R$ are $\Gamma$-proper, (by 2.1.3) $(S \cap S')_R$ is also $\Gamma$-proper. On the other hand (see 3.2), $\overline{U}_R$ is $\Gamma$-compact and $U = \overline{U}_R \cap \Gamma$. Therefore (by 2.1.5), $(S \cap S' \cap \Gamma) \cdot U = ((S \cap S')_R \cap \Gamma) \cdot (\overline{U}_R \cap \Gamma)$ is of finite index in $S \cap \Gamma$. But (see 5.2.4) $N \cap \Gamma = S \cap \Gamma$, $N' \cap \Gamma = S' \cap \Gamma$, hence $N \cap N' \cap \Gamma = S \cap S' \cap \Gamma$. Therefore, $(N \cap N' \cap \Gamma) \cdot U$ is of finite index in $N \cap \Gamma$.

9.3.2. LEMMA. If $U \neq \{e\}$, and if $\overline{U}$ and $\overline{U}'$ are opposite horospherical subgroups of $G$, then 1) $A_0 \cap A_0' \cap \Gamma$ is a Zariski-dense arithmetic subgroup of $A_0 \cap A_0'$; 2) $A_0 = (A_0 \cap A_0') \tilde{\times} \overline{U}$; 3) $A_0 \cap A_0'$ is connected; 4) $\dim(A_0 \cap A_0') = \dim \overline{U}$.

PROOF. Let $D$ denote the closure of $A_{0} \cap A_{0}^{\prime} \cap \Gamma$. Since

\( A \cap A' \cap \Gamma = (N \cap \Gamma) \cap (N' \cap \Gamma) = N \cap N' \cap \Gamma, \text{ and } A\_0 \cap A'\_0 \text{ is of finite index in } A \cap A' \text{ (because } A/A\_0 \text{ and } A'/A'\_0 \text{ are finite), using Lemma 9.3.1, we see that } D\tilde{\times}\bar{U} \text{ is of finite index in } A\_0. \text{ But } A\_0 \text{ is connected. Therefore, } A\_0 = D\tilde{\times}\bar{U}, \text{ and since } D \subset A\_0 \cap A'\_0, \text{ we have } D = A\_0 \cap A'\_0 \text{ and } A\_0 = (A\_0 \cap A'\_0)\tilde{\times}\bar{U} \text{ (this is 2)). Since } A\_0 \text{ is connected and } A\_0 = (A\_0 \cap A'\_0)\tilde{\times}\bar{U}, A\_0 \cap A'\_0 \text{ is connected (this is 3)). 4) follows immediately from 2). Since (by 5.2.2) \( S\_R \) and \( S'\_R \) are \( \Gamma \)-proper, (by 2.1.3) \( (S \cap S')\_R \) is \( \Gamma \)-proper. But \( A \cap A' \subset S \cap S' \) and (see 5.5.3) \( A \cap A' \cap \Gamma = (S \cap \Gamma) \cap (S' \cap \Gamma) = S \cap S' \cap \Gamma. \text{ Therefore, } (A \cap A')\_R \) is \( \Gamma \)-proper, and since \( A\_0 \cap A'\_0 \) is of finite index in \( A \cap A', (A\_0 \cap A'\_0)\_R \) is \( \Gamma \)-proper. But \( D = A\_0 \cap A'\_0. \text{ Therefore, } A\_0 \cap A'\_0 \text{ is } \Gamma \)-regular. Since \( U \neq e, (\text{ by 1.5})\bar{U} \) is not contained in any non-trivial normal subgroup of \( G, \text{ and hence (by 9.1), } C(\bar{U}) \cap A\_0 \cap A'\_0 \subset C(\bar{U}) \cap N \cap N' = \{e\} (N \cap N' \text{ is a Levi subgroup of } N, \text{ because } N \text{ and } N' \text{ are opposite). Thus, } A\_0 \cap A'\_0 \text{ satisfies the conditions of Lemma 5.5.1, 2). Therefore } A\_0 \cap A'\_0 \cap \Gamma \text{ is a dense arithmetic subgroup of } A\_0 \cap A'\_0 (\text{ this is 1)), and the lemma is proved.}

9.3.3. LEMMA. If $U \neq \{e\}$, and $\overline{U}$ and $\overline{U}'$ are opposite horospherical subgroups of $G$, then $A_0 \cap \Gamma$ is a Zariski-dense arithmetic subgroup of $A_0$.

PROOF. Since (by 9.3.2) $A_0 = (A_0 \cap A_0') \tilde{\times} \overline{U}$, $A_0 \cap A_0' \cap \Gamma$ is a dense arithmetic subgroup of $A_0 \cap A_0'$ and (by 3.4.1) $U = \overline{U} \cap \Gamma$ is a dense arithmetic subgroup of $\overline{U}$, (by 9.2) $\Phi = (A_0 \cap A_0' \cap \Gamma) \cdot U$ is a dense arithmetic subgroup of $A_0$. Then (by 4.1) $\Phi$ is a lattice in $(A_0)_R$, and since $A_0 \cap \Gamma \supset \Phi$ is discrete, $\Phi$ is of finite index in $A_0 \cap \Gamma$. This proves the lemma.

9.3.4. LEMMA. Let $U \neq \{e\}$, let $\overline{U}$ and $\overline{U}'$ be opposite horospherical subgroups of $G$, and suppose that a $\mathbf{Q}$-structure is given on $A_0$ such that $(A_0)_\mathbf{Q} \cap \Gamma$ is of finite index in $A_0 \cap \Gamma$. Then $A_0 \cap A_0'$ is a $\mathbf{Q}$-subgroup of $A_0$.

PROOF. Since $A_0$ is connected, $A_0 \cap A_0' \cap \Gamma$ is dense in $A_0 \cap A_0'$ (see 9.3.2) and $(A_0)_Q \cap A_0' \cap \Gamma$ is of finite index in $A_0 \cap A_0' \cap \Gamma$, we know that $(A_0)_Q \cap A_0'$ is dense in $A_0 \cap A_0'$. Therefore, ([4], Ch. AG, 14.4) $A_0 \cap A_0'$ is a Q-subgroup of $A_0$.

9.4. Let $U$ and $U'$ be non-trivial unipotent subgroups of $\Gamma$ such that $\overline{U}$ and $\overline{U}'$ are opposite horospherical subgroups. We use the notation of §9.3. We denote by $B \subset G$ the set of $g \in G$ such that $g\overline{U}'g^{-1}$ and $\overline{U}$ are opposite horospherical subgroups, by $\mathfrak{A}$ and $\mathfrak{A}'$ the Lie algebras of $A_0$ and $A_0'$, by $M$ and $N$ the subspaces of the Lie algebra $\mathfrak{G}$ of $G$, generated, respectively, by $\bigcup_{\gamma \in B \cap \Gamma} (\mathfrak{A} \cap \operatorname{Ad} \gamma \mathfrak{A}')$ and $\bigcup_{\gamma^{-1} \in B \cap \Gamma} (\mathfrak{A}' \cap \operatorname{Ad} \gamma \mathfrak{A})$, and by $V \subset G$ the set

of $g_0 \in G$ for which $\dim (M \cap \operatorname{Ad} g_0 N) = \min_{g \in G} \dim (M \cap \operatorname{Ad} gN) = d$.

We put $W = B \cap V$.

9.4.1. LEMMA. If $\dim A > \dim \overline{U}$, then the assumptions in §8.2 hold

for $G = H$, $\mathrm{Ad} = T$, $L = \mathfrak{G}$, $M$, $N$ and $W$.

PROOF. 1. G is connected and (by 1.4.1)  $\Gamma$  is Zariski-dense in G. By Propositions 4.10 and 4.12 of [10], B is non-empty and open in G. By Lemma 8.1.1, V is non-empty and open in G. Since B and V are non-empty and Zariski-open in G, and since G is connected,  $W = B \cap V$  is non-empty and open in G. Since the centre of G is trivial, Ad is a faithful rational representation.

2. Since $\dim A_0 = \dim A > \dim \overline{U}$, (by 9.3.2) $\dim(A_0 \cap A_0') > 0$. But (see 9.3.2) $A_0 \cap A_0' \cap \Gamma$ is dense in $A_0 \cap A_0'$. Therefore, $A_0 \cap A_0' \cap \Gamma \neq \{e\}$. Hence (by 1.5), $A_0 \cap A_0'$ is not contained in any non-trivial algebraic normal subgroup of $G$, and since (see 9.3.2) $A_0 \cap A_0'$ is connected, $\mathfrak{A} \cap \mathfrak{A}'$ is not contained in any non-zero ideal of $\mathfrak{G}$. But $\mathfrak{G}$ is semisimple. Therefore, $\bigcup_{g \in G} \operatorname{Ad} g(\mathfrak{A} \cap \mathfrak{A}')$ generates $\mathfrak{G}$ as a linear space.

We may assume that $e \in B$ (otherwise we could replace $U'$ by $\gamma U' \gamma^{-1}$).

Therefore, $M \supset \mathfrak{A} \cap \mathfrak{A}'$. Hence $\bigcup_{g \in G} \operatorname{Ad} gM$ generates $\mathfrak{G}$ as a linear space.

$$
g \in G
$$

3. It is clear that for any $\gamma \in B\cap \Gamma$

$$
M \cap \operatorname{Ad} \gamma N = \mathfrak {A} \cap \operatorname{Ad} \gamma \mathfrak {A} ^ {\prime}; \quad N \cap \operatorname{Ad} \gamma^ {- 1} M = \mathfrak {A} ^ {\prime} \cap \operatorname{Ad} \gamma^ {- 1} \mathfrak {A}, \tag {1}
$$

and hence (by 9.3.2), $\dim(M \cap \operatorname{Ad} \gamma N) = \dim(\mathfrak{A} \cap \operatorname{Ad} \gamma \mathfrak{A}') = \dim(A \cap \gamma A_0' \gamma^{-1}) = \dim \overline{U}$. But $B \supset W$, $W$ is open, and $\Gamma'$ is dense in $G$. Therefore, $d = \dim \overline{U}$, and so $B \cap \Gamma = W \cap \Gamma$. From this and from (1) it follows that

$\bigcup_{w\in W}(M\cap\operatorname{Ad}wN)$  and  $\bigcup_{w^{-1}\in W}(N\cap\operatorname{Ad}wM)$  generate M and N, respectively.
This completes the proof of the lemma.

9.5. In this section we use the notation of §§9.3 and 9.4.

9.5.1. THEOREM. A Q-structure can be given on $G$ such that $\Gamma \subset G_0$.

PROOF. By Theorem 7.11, there exist non-trivial unipotent subgroups $U$ and $U'$ of $\Gamma$ such that $\overline{U}$ and $\overline{U}'$ are opposite horospherical subgroups and $\dim A > \dim \overline{U}$, $\dim A' > \dim \overline{U'}$. Then (by 9.3.3) on $A_0$ and $A_0'$ Q-structures can be given with respect to which $A_0 \cap \Gamma$ and $A_0' \cap \Gamma$ are arithmetic subgroups. In a natural way these Q-structures induce Q-structures on $\mathfrak{A}$ and $\mathfrak{A}'$. If $\gamma \in B \cap \Gamma$, then (by 9.3.4) $A_0 \cap \gamma A_0' \gamma^{-1}$ is a Q-subgroup of $A_0$, and $\mathfrak{A} \cap \operatorname{Ad} \gamma \mathfrak{A}'$ is a Q-subspace of $\mathfrak{A}$. Since (1) holds for any $\gamma \in W' \cap \Gamma \subset B \cap \Gamma$, and since $\mathfrak{A} \cap \operatorname{Ad} \gamma \mathfrak{A}'$ is a Q-subspace of $\mathfrak{A}$, the Q-structures on $M$ and $N$ are compatible in the sense of §8.6. Hence by Lemmas 9.4.1 and 8.6.2, we find that a Q-structure can be given on $G$ such that $\Gamma \subset G_{\mathbf{Q}}$. This proves the theorem.

9.6. Beginning here we assume that a Q-structure has been given on G for which  $\Gamma \subset G_{Q}$ . Then (5.3)  $(G_{\mathbf{Q}})^{u} \neq \{e\}$  and hence ([10], 8.5) we have:

9.6.1. LEMMA. The group $G$ is isotropic over $\mathbf{Q}$, that is, $\operatorname{rank}_{\mathbf{Q}} G > 0$.  
9.6.2. LEMMA. If $P$ and $P'$ are opposite parabolic $\mathbf{Q}$-subgroups of $G$, $P \neq G$, and $R_u(P) \cap \Gamma$ and $R_u(P') \cap \Gamma$ are Zariski-dense in $R_u(P)$ and

$$
R _ {u} (P ^ {\prime})
$$

$$
P _ {\mathbf {Z}} = P \cap G _ {\mathbf {Z}}
$$

$$
P \cap \Gamma
$$

$$
U = R _ {u} (P) \cap \Gamma , U ^ {\prime} = R _ {u} \left(P ^ {\prime}\right) \cap \Gamma , N = N (\bar {U})
$$

$N' = N(\overline{U}')$, $S = S(\overline{U})$, $S' = S(\overline{U}')$, $\Delta = \Delta_U$, $\overline{\Delta} = \Delta_{\overline{U}_Z}$, $C = C(\overline{U})$, $D = S \cap S'$. Since $\overline{U} = R_u(P)$ is defined over $\mathbf{Q}$, (see 3.3.1) $\overline{U}_{\mathbf{Z}}$ is dense in $\overline{U}$. Therefore (see 3.1) $\overline{\Delta}$ is a lattice of full dimension in the Lie algebra $\mathfrak{u}_{\mathbf{R}}$ of $U_{\mathbf{R}}$. But (Ad $N_{\mathbf{Z}}$) $\overline{\Delta} = \overline{\Delta}$. Therefore

$$
N _ {\mathbf {Z}} = S _ {\mathbf {Z}}.\tag{2}
$$

By Lemma 4.5.7, $P = N$, $P' = N'$, and hence, $\overline{U}$ and $\overline{U}'$ are opposite horospherical subgroups. Since $P \neq G$ and $P = N$, $\overline{U} \neq \{e\}$. Therefore, (by 1.5 and 9.1.1) $D \cap C \subset N \cap N' \cap C = \{e\}$. But (by 5.2.2 and 2.1.3) $D_{\mathbf{R}}$ is $\Gamma$-proper. We put $D_{\mathbf{Z}}' = \{d \in D; (\operatorname{Ad} d)\Delta = \Delta\}$. Then (by 5.5.5) $D_{\mathbf{Z}}'$ and $D \cap \Gamma$ are commensurable.

We put $D_{\mathbf{Z}}^{\prime \prime} = \{d \in D; (\operatorname{Ad} d) \overline{\Delta} = \overline{\Delta}\}$. Then: 1) the subgroup $D = S \cap S'$ is defined over $\mathbf{Q}$; 2) since $U$ is connected and $D \cap C = \{e\}$, $D \cap C(\mathfrak{U}) = \{e\}$; 3) the lattice $\overline{\Delta}$ has full dimension in $\mathfrak{U}_{\mathbf{R}}$ and $\overline{\Delta} \subset \mathfrak{U}_{\mathbf{Q}}$. Therefore, the natural representation $T$ of $D$ in $\mathfrak{U}$ (defined by $T_d(u) = (\operatorname{Ad} d)u$, $d \in D$, $u \in \mathfrak{U}$) is faithful and $T$ is defined over $\mathbf{Q}$ in any basis of the lattice $\overline{\Delta}$, and so ([7], 6.11) $D_{\mathbf{Z}}^{\prime \prime}$ and $D_{\mathbf{Z}} = D \cap G_{\mathbf{Z}}$ are commensurable. Since $U \subset \overline{U}_{\mathbf{Q}}$ and $U$ is discrete, (3.3.2) $\Delta$ and $\overline{\Delta}$ are commensurable. Therefore, $D_{\mathbf{Z}}'$ and $D_{\mathbf{Z}}''$ are commensurable. But, as we have already shown, $D_{\mathbf{Z}}'$ is commensurable with $D \cap \Gamma$, and $D_{\mathbf{Z}}''$ with $D_{\mathbf{Z}}$. Therefore, $D \cap \Gamma$ and $D_{\mathbf{Z}}$ are commensurable.

Since $U$ and $U'$ are opposite horospherical subgroups, (by 7.3.1) $D = S \cap S' = S \cap N'$, and since $S \supseteq \overline{U}$, $S = D \widetilde{\times} \overline{U}$, and $S_{\mathbf{R}} = D_{\mathbf{R}} \widetilde{\times} \overline{U}_{\mathbf{R}}$. But $D_{\mathbf{R}}$ is $\Gamma$-proper and (by 3.2) $\overline{U}_{\mathbf{R}}$ is $\Gamma$-compact. Therefore, (see 2.1.5) $(D \cap \Gamma) \cdot (\overline{U} \cap \Gamma) = (D \cap \Gamma) \cdot U$ is of finite index in $S \cap \Gamma$. On the other hand, 1) (by [7], 6.4) $D_{\mathbf{Z}} \cdot \overline{U}_{\mathbf{Z}}$ is commensurable with $S_{\mathbf{Z}}$; 2) as proved above, $D_{\mathbf{Z}}$ and $D \cap \Gamma$ are commensurable; 3) since $U$ is discrete and lies in $\overline{U}_{\mathbf{Q}}$, (3.3.2) $\overline{U}_{\mathbf{Z}}$ and $U \cap \Gamma$ are commensurable. Therefore, $S_{\mathbf{Z}}$ and $S \cap \Gamma$ are commensurable. But, since by (2) $N_{\mathbf{Z}} = S_{\mathbf{Z}}$, we have (by 5.2.4) $N \cap \Gamma = S \cap \Gamma$, and (by 4.5.7) $P = N$. This proves the lemma.

We use the notation of §4.5.

9.6.3. LEMMA. There exist a maximal Q-split torus S and an order on the set of roots  $\Phi =_{\mathbf{Q}} \Phi(S, G)$  such that for any  $\theta \subset \Delta =_{\mathbf{Q}} \Delta(S, G)$ ,  $\theta \neq \Delta$ , the subgroup  $P_{\theta} \cap G_{Z}$  is commensurable with  $P_{\theta} \cap \Gamma$ , and  $P_{\theta}^{-} \cap G_{Z}$  with  $P_{\theta}^{-} \cap \Gamma$ .

PROOF. By Theorem 7.1.1, $\Gamma$ contains non-trivial unipotent subgroups $U$ and $U'$ such that $\overline{U}$ and $\overline{U}'$ are opposite horospherical subgroups. Since $U \cup U' \subset \Gamma \subset G_{\mathbf{Q}}$, ([4], Ch. AG, 14.4) $\overline{U}$ and $\overline{U}'$ are defined over $\mathbf{Q}$, and hence, $N(\overline{U})$ and $N(\overline{U}')$ are opposite parabolic $\mathbf{Q}$-subgroups of $G$. Therefore, by Lemma 4.5.8, there is a maximal $\mathbf{Q}$-split torus $S$ of $G$ and an order on the set of roots $\Phi = _{\mathbf{Q}} \Phi(S, G)$ such that

$$
N (\overline {{{U}}}) = P _ {\theta^ {\prime}}, N (\overline {{{U}}} ^ {\prime}) = P _ {\theta^ {\prime}} ^ {-}, \theta^ {\prime} \subset_ {\mathbf {Q}} \Delta (S, G).
$$

Let $\theta \subset \Delta$. Since $V_{\theta} \subset P_{\varnothing'} \subset P_{\theta'}$, $V_{\theta}^{-} \subset P_{\theta}^{-}$, and (by 9.5.2) the subgroup $P_{\theta'} \cap G_{\mathbf{Z}}$ is commensurable with $P_{\theta'} \cap \Gamma$, and $P_{\theta'}^{-} \cap G_{\mathbf{Z}}$ with $P_{\theta'}^{-} \cap \Gamma$, we see that $V_{\theta} \cap G_{\mathbf{Z}}$ is commensurable with $V_{\theta} \cap \Gamma$, and $V_{\theta}^{-} \cap G_{\mathbf{Z}}$ with $V_{\theta}^{-} \cap \Gamma$. Then 1) (by (1), 3.3.3, and 3.3.1) $V_{\theta} \cap \Gamma$ is dense in $V_{\theta}$, and $V_{\theta}^{-} \cap \Gamma$ in $V_{\theta}^{-}$; 2) $P_{\theta} \neq G$, $P_{\theta}^{-} \neq G$ (since $\theta \neq \Delta$). Therefore, (see 9.5.2) $P_{\theta} \cap G_{\mathbf{Z}}$ is commensurable with $P_{\theta} \cap \Gamma$, and $P_{\theta}^{-} \cap G_{\mathbf{Z}}$ with $P_{\theta}^{-} \cap \Gamma$. This proves the lemma.

9.6.4. LEMMA. G is simple over Q.

PROOF. Since (by 9.6.1) $\operatorname{rank}_{\mathbf{Q}} G > 0$, (by 9.6.3) there is a minimal parabolic Q-subgroup $P$ of $G$ such that $P_{\mathbf{Z}}$ and $P \cap \Gamma$ are commensurable. We put $U = R_u(P)$. Since $G$ is connected and has trivial centre, it suffices to show that if $G = G' \times G''$, where $G'$ and $G''$ are defined over $\mathbf{Q}$, then either $G' = \{e\}$ or $G'' = \{e\}$. Let $G = G' \times G''$, with $G'$ and $G''$ defined over $\mathbf{Q}$. Since $P$ is minimal, ([9], 3.7) $U$ is a maximal unipotent Q-subgroup of $G$. Therefore, $U = U' \times U'', U' = U \cap G', U'' = U \cap G''$. Since $U' \subset U \subset P$, $U_{\mathbf{Z}}'$ is commensurable with $U' \cap \Gamma$. Therefore, (by 3.3.3 and 3.3.1) $U' \cap \Gamma$ is dense in $U'$. Similarly $U'' \cap \Gamma$ is dense in $U''$. From this, using Lemma 1.5, we find that either one of the subgroups $G'$ and $G''$ reduces to $\{e\}$, or $U = \{e\}$. But since $\operatorname{rank}_{\mathbf{Q}} G > 0$, ([10], 8.5) $U \neq \{e\}$. This proves the lemma.

9.7. We combine Lemmas 9.5.1, 9.6.1, 9.6.3, 9.6.4 into a single theorem.
9.7.1. THEOREM. A Q-structure can be given on G such that the following conditions hold simultaneously: 1)  $\Gamma \subset G_{Q}$ ; 2) G is simple over Q; 3) there are a maximal Q-split torus S and an order on the set of roots  $\Phi = _{Q} \Phi(S, G)$  such that for any  $\theta \subset \Delta = _{Q} \Delta(S, G)$ ,  $\theta \neq \Delta$ , the subgroup  $P_{\theta} \cap G_{Z}$  is commensurable with  $P_{\theta} \cap \Gamma$ , and  $P_{\theta}^{-} \cap G_{Z}$  with  $P_{\theta}^{-} \cap \Gamma$ ; 4)  $\operatorname{rank}_{Q} G > 0$ .

## § 10. Proof of the main theorem

Beginning here we assume that $G$ and $\Gamma$ satisfy the conclusions of Theorem 9.7.1.

10.1. LEMMA. There is an $n$ such that $\Gamma \supset (G_{n\mathbf{Z}})^u$.

This lemma will be proved in the following sections, and in this section we show how the assertion of the main theorem follows from it.

10.2. If $H_{2}$ is a subgroup of $H_{1}$, then, as before, $|H_{1} / H_{2}|$ denotes the index of $H_{2}$ in $H_{1}$.

10.2.1. LEMMA. Let $P$ and $P'$ be opposite minimal parabolic $\mathbf{Q}$-subgroups of $G$, $U = R_u(P)$, and $U' = R_u(P')$. Then for any natural number $n$ there is an $N(n, P, P')$ such that if $\Lambda$ is a discrete subgroup of $G_{\mathbf{R}}$, $\Lambda \subset G_{\mathbf{Q}}$, and $\Lambda \supset U_{n\mathbf{Z}} \cup U_{n\mathbf{Z}}'$, then $|U \cap \Lambda / U_{n\mathbf{Z}}| < N(n, P, P')$.

PROOF. By Lemma 4.6.2 there is a neighbourhood $W$ of the identity in $G_{\mathbf{R}}$ such that if $\lambda \in \Lambda \cap U \cap W$, then the subgroup $F_{\lambda}$ generated by $\lambda \cup U_{n\mathbf{Z}}'$ is unipotent. Let $\lambda \in \Lambda \cap U \cap W$. Then $F_{\lambda}$ is unipotent, and

hence, the Zariski-closure $\overline{F}_{\lambda}$ of $F_{\lambda}$ is also unipotent. But $F_{\lambda} \subset G_{\mathbf{Q}}$ (since $\Lambda \subset G_{\mathbf{Q}}$). Therefore ([4], Ch. AG, 14.4) $\overline{F}_{\lambda}$ is a unipotent algebraic $\mathbf{Q}$-subgroup of $G$. On the other hand, 1) since $\Lambda \cap U' \supset U_{n\mathbf{Z}}'$, we have (by 3.3.1) $\overline{F}_{\lambda} \supset U'$; 2) since $P'$ is a minimal parabolic $\mathbf{Q}$-subgroup of $G$, (by [9], 3.7) $U'$ is a maximal unipotent $\mathbf{Q}$-subgroup of $G$. Therefore, $\overline{F}_{\lambda} = U'$ and hence, $\lambda \in U'$. But $U \cap U' = \{e\}$ (because $P$ and $P'$ are opposite). Thus, $\lambda = e$ and hence, $\Lambda \cap U \cap W = \{e\}$. But (by 3.3.1) $U_{\mathbf{R}} / U_{n\mathbf{Z}}$ is compact. Therefore, $|U \cap \Lambda / U_{n\mathbf{Z}}| < N(n, P, P')$, where $N(n, P, P')$ is the quotient of the volumes $v(U_{\mathbf{R}} / U_{n\mathbf{Z}}) / v(U \cap W)$.

10.3. LEMMA. There is an integer $m$ such that $u^m \in G_{\mathbf{Z}}$ for any $u \in \Gamma^u$

PROOF. Let $P_1, \ldots, P_j$ be minimal parabolic Q-subgroups satisfying the conclusion of Lemma 4.7.1, and $P$ any minimal parabolic Q-subgroup of $G$. For any $j, 1 \leqslant j \leqslant i$, there exists ([10], 4.14) an opposite minimal parabolic Q-subgroup $P_j'$ to $P_j$. We put $U_j = R_u(P_j)$, $U_j' = R_u(P_j')$, $U = R_u(P)$. Then (by 4.7)

$$
U = g ^ {- 1} (P) U _ {j (P)} g (P), \quad g (P) \in G _ {\mathbf {Z}}, \quad 1 \leqslant j (P) \leqslant i.
$$

Since (by 10.1) $\Gamma \supset (G_{n\mathbf{Z}})^u$ and $g(P) \in G_{\mathbf{Z}}$, $g(P)\Gamma g^{-1}(P)$ contains $(U_{j(P)})_{n\mathbf{Z}} \cup (U_{j(P)}^{\prime})_{n\mathbf{Z}}$. By Lemma 10.2.1, $|U_{j(P)} \cap g(P)\Gamma g^{-1}(P)/(U_{j(P)})_{n\mathbf{Z}}| < N(n)$, where $N(n) = \max_{1 \leqslant j \leqslant i} N(n, P_j, P_j')$, hence $|U \cap \Gamma/U_{n\mathbf{Z}}| < N(n)$. To conclude the proof of the lemma it remains to set $m = N(n)!$ and to use part 1) of Theorem 9.7.1 and the fact that any unipotent element of $G_{\mathbf{Q}}$ is contained in some maximal unipotent $\mathbf{Q}$-subgroup of $G$, and hence ([9], 3.7) in the unipotent radical of some minimal parabolic $\mathbf{Q}$-subgroup of $G$.

10.4. PROOF OF THE MAIN THEOREM. We denote by $\Delta$ and $\Delta'$, the $Z$-modulus generated, respectively, by $\ln((G_{\mathbf{Z}})^u)$ and $\ln(\Gamma^u)$. Since there is a natural number $n$ such that $(E - u)^n = 0$ for any $u \in G^u$, using the Taylor formula for $\ln(E + (u - E))$ we find that the denominators of the entries of the matrices in $\ln((G_{\mathbf{Z}})^u)$ are uniformly bounded. Therefore, $\Delta$ is a lattice in $\mathfrak{G}$. On the other hand, by Lemmas 10.1 and 10.3, we see that the lattices $\Delta$ and $\Delta'$ are commensurable. Therefore, $\Delta'$ is also a lattice in $\mathfrak{G}$. But Ad $\Gamma$ leaves $\Delta'$ invariant; Ad is an isomorphism of the algebraic groups $G$ and Ad $G$ (because the centre of $G$ is trivial), and (by 1.4) $\Gamma$ is Zariski-dense in $G$. From this, using [4], Ch. AG, Theorem 14.4, we see that $\Gamma$ is contained in some arithmetic subgroup $\Lambda$ of $G$. But $G_{\mathbf{R}} / \Gamma$ has finite volume. Therefore, $\Gamma$ is commensurable with $\Lambda$, and hence, $\Gamma$ is an arithmetic subgroup of $G$.

## § 11. p-adic and adelic points of algebraic groups

11.1. NOTATION. As usual,  $Q_{p}$  is the field of p-adic numbers,  $Z_{p}$  the ring of p-adic integers. We denote by A the ring of R-adèles of the field Q, that is, the restricted direct product of the  $Q_{p}$  over all finite primes p. For any algebraic Q-group H and any  $M \subset H_{Q}$ , we denote by  $M_{Q_{p}}$  the closure of M

in  $H_{Q_{p}}$  in the p-adic topology.  $H_{A}$  denotes the set of A-points of H with the topology induced by A, and  $M_{A}$  the closure of  $M \subset H_{Q}$  in  $H_{A}$ . For any rational r and any prime p, we denote by  $v_{p}(r)$  the value of the p-adic valuation at r, and we put  $p(r) = p^{v_{p}(r)}$ . For any p-adic matrix h, let  $v_{p}(h)$  denote the minimum of the values of the p-adic valuation on the entries of h.

11.2. Let $H$ be an algebraic $\mathbf{Q}$-group. For any rational number $d$ we put

$$
H _ {d \mathbf {Z}} = \left\{h \in H _ {\mathbf {Q}}; (h - E) / d \text {   is   an   integral   matrix } \right\}.
$$

11.2.1. LEMMA. 1) For any two rational numbers $d_1$ and $d_2$ there is a natural number $i$ such that $i(H_{d_1\mathbf{Z}})^u \supset (H_{d_2\mathbf{Z}})^u$; 2) for any rational number $d$ and any natural number $m$ there is a natural number $j$ such that $m(H_{d_{\mathbf{Z}}})^u \supset (H_{j_{\mathbf{Z}}})^u$.

PROOF. $H \subset GL_n(\mathbf{Q})$ for some $n$. Then for any $u \in H^u$ we have $(u - E)^n = 0$. To complete the proof of the lemma, we have to represent any $u \in (H_{d_1\mathbf{Z}})^u$ and $u \in (H_{j\mathbf{Z}})^u$ in the form $u = E + v$, and to expand $(E + v)^m$ and $(E + v)^{1/m}$ by Newton's binomial formula.

11.3. Let $V$ be a unipotent algebraic $\mathbf{Q}$-group. The following lemma is well known and easy to prove.

11.3.1. LEMMA. $V_{\mathbf{Q}}$ is dense in $V_{A}$.

Let $k$ be a natural number, and $p$ a prime. From Lemma 11.3.1 we immediately derive:

11.3.2. LEMMA. $(V_{k\mathbf{Z}})_{\mathbf{Q}_p} = (V_{p(k)\mathbf{Z}})_{\mathbf{Q}_p}$.

11.3.3. LEMMA. If $F$ and $F'$ are open subgroups of $V_{\mathbf{Q}_p}$ (in the p-adic topology), and if $F$ is a subgroup of finite index in $F'$, then $|F'|/F|$ is a power of $p$.

PROOF. If $v \in V$, then $(v - E)^n = 0$ for some $n$. From this, using Newton's binomial formula, we find that $v^{p^l} \to E$ as $l \to +\infty$ for $v \in V_{\mathbf{Q}_p}$. Therefore, since $F$ is open, the order of any element of $F'/F$ is a power of $p$ and hence ([13], Theorem 4.1.1), the order of $F'/F$ is a power of $p$.

11.3.4. LEMMA. If the subgroup $M \subset V_{\mathbf{Q}}$ is commensurable with $V_{\mathbf{Z}}$, then there is a $j$ and a normal subgroup $\Lambda$ of $M$ such that $V_{\mathbf{Z}} \supset \Lambda \supset V_{j\mathbf{Z}}$.

PROOF. Since $M$ is commensurable with $V_{\mathbf{Z}}$, we have 1) $kM \subset V_{\mathbf{Z}}$ for some $k$; 2) (by 3.3.3) $M \supset V_{s\mathbf{Z}}$ for some $s$. Let $M_k$ be the subgroup generated by $kM$. Then: 1) $M_s \supset V_{\mathbf{Z}}$; 2) $M_s$ is a normal subgroup of $M$ (because $M$ normalizes $sM$); 3) by Lemma 11.2.1, there is a $j$ such that $M_k \supset kM \supset kV_{s\mathbf{Z}} \supset V_{j\mathbf{Z}}$. This proves the lemma.

11.3.5. LEMMA. For any subgroup $M \subset V_{\mathbf{Q}}$ commensurable with $V_{\mathbf{Z}}$: 1) $M_A$ is open in $V_A$; 2) $M_A = \prod_p M_{\mathbf{Q}_p}$; 3) $M = M_A \cap V_{\mathbf{Q}}$.

PROOF. Since for  $M = V_{jZ}$  the assertion of the lemma immediately follows from Lemma 11.3.1, by Lemma 11.3.4 it suffices to show that if the assertion of the lemma is true for  $M'$ , a normal subgroup of  $M''$ , then

it is also true for $M''$. But $M'' / M'$ is naturally mapped into $\prod_{p} (M_{\mathbf{Q}_p}'' / M_{\mathbf{Q}_p}')$,

and since (see 11.3.3) for any p the order of  $M_{Q_{p}}^{\prime\prime}/M_{Q_{p}}^{\prime}$  is a power of p, this embedding is an epimorphism, from which it easily follows that the lemma is also true for  $M^{\prime\prime}$ . This proves the lemma.

From Lemmas 11.3.5 and 3.3.3 we easily obtain:

11.3.6. LEMMA. If $M \subset V_{\mathbf{Q}}$ is commensurable with $V_{\mathbf{Z}}$ and

$M_{\mathbf{Q}_p} \supset (V_{p^k\mathbf{Z}})_{\mathbf{Q}_p}$, then $M \supset V_{n\mathbf{Z}}$, where $v_p(n) \leqslant k$.

11.3.7. LEMMA. If $M \subset V_{\mathbf{Q}}$ and $M_{\mathbf{Q}_p}$ is open in $V_{\mathbf{Q}_p}$ for some $p$, then $M$ is Zariski-dense in $V$.

PROOF. Since  $M_{Q_{p}}$  is open in  $V_{Q_{p}}$ , the Lie algebra of  $\overline{M}$  coincides with the Lie algebra of V. But V is connected (because V is unipotent), so that  $\overline{M} = V$ .

11.4. LEMMA. Let F be a p-adic Lie group, V a neighbourhood of the identity in F, and n a natural number. Then nV contains a neighbourhood of the identity in F.

PROOF. Let $\mathfrak{F}$ be the Lie algebra of $F$, $W$ a neighbourhood of zero in $\mathfrak{F}$ such that the exponential mapping $\exp_W: W \to \exp W$ is a homeomorphism, and let $\ln_W: \exp W \to W$ be the inverse to $\exp_W W$. We may assume that $V$ is small enough so that $V \subset \exp W$ and $n \ln_W V \subset W$. Since $\exp_W$ and $\ln_W$ are homeomorphisms, we see that $nV = \exp(n \ln_W V)$ contains a neighbourhood of zero in $F$.

11.5. STRONG APPROXIMATION THEOREM. Let H be a connected simply-connected almost Q-simple algebraic Q-group. If  $H_{R}$  is not compact, then  $H_{Q}$  is dense in  $H_{A}$ .

The strong approximation theorem was proved by M. Kneser [22] for $H$ not of type $E_8$. In [24] and [25] Platonov proved it (without using Kneser's proof) for all $H$. We observe that usually the strong approximation theorem is stated and proved in a more general form. The transition from the case of an absolutely almost simple group in [24] and [25] to the case of an arbitrary almost Q-simple group is realized by means of the well-known procedure of restriction of the field of scalars (see [26], §3.1.2 and [28], Theorems 1.3.2 and 1.3.3).

11.5.1. LEMMA. Let $H$ be a connected almost $\mathbf{Q}$-simple algebraic $\mathbf{Q}$-group (not necessarily simply-connected) such that $H_{\mathbf{R}}$ is not compact. Then for any prime $p$ and any natural numbers $n$ and $r$ there is a neighbourhood $V_{H}(p, n, r)$ of the identity in $H_{\mathbf{Q}_p}$ such that if $m \in \mathbf{N}^+$, $v_p(m) < r$, and $\Lambda$ is a subgroup of $H_{m\mathbf{Z}}$ of index at most $n$, then $\Lambda_{\mathbf{Q}_p} \supset V_H(p, n, r)$.

PROOF. If $H$ is simply-connected and $n = 1$, then the assertion of the lemma follows immediately from the strong approximation theorem. Suppose that $H$ is not simply-connected. Then ([26], Proposition 2) there exists a simply-connected almost Q-simple algebraic Q-group $H'$ and a Q-isogeny (that is, a surjective homomorphism defined over $\mathbf{Q}$ with finite kernel) $f\colon H' \to H$. The Q-isogeny $f$ is given by polynomials with coefficients in $\mathbf{Q}$. We denote

the product of the denominators of all the coefficients of these polynomials by $d$. Then $H_{k\mathbf{Z}} \supset f(H_{dk\mathbf{Z}}^{\prime})$ for any $k \in \mathbf{N}^{+}$. For any prime $p$, the homomorphism $f$ defined over $\mathbf{Q}$ induces a continuous homomorphism $f_{p}: H_{\mathbf{Q}_{p}}^{\prime} \to H_{\mathbf{Q}_{p}}$. Since the kernel of $f$ is finite, the differential of $f_{p}$ at the identity gives an isomorphism of the Lie algebras of $H_{\mathbf{Q}_{p}}^{\prime}$ and $H_{\mathbf{Q}_{p}}$. Therefore, the restriction of $f_{p}$ to any sufficiently small neighbourhood of the identity in $H_{\mathbf{Q}_{p}}^{\prime}$ is a homeomorphism. Then $(H_{m\mathbf{Z}})_{\mathbf{Q}_{p}} \supset (f(H_{dm\mathbf{Z}}^{\prime}))_{\mathbf{Q}_{p}} \supset f_{p}((H_{dm\mathbf{Z}}^{\prime})_{\mathbf{Q}_{p}}) \supset f_{p}(V_{H^{\prime}}(p, 1, r + v_{p}(d))) = V_{H}(p, 1, r)$ and $V_{H}(p, 1, r)$ is open in $H_{\mathbf{Q}_{p}}$, that is, for $n = 1$ the lemma is proved. But if $n$ is arbitrary, then $n!(H_{m\mathbf{Z}}) \subset \Lambda$, because the index of $\Lambda$ in $H_{n\mathbf{Z}}$ is less than $n$. Therefore, $\Lambda_{\mathbf{Q}_{p}} \supset (n!H_{m\mathbf{Z}})_{\mathbf{Q}_{p}} \supset n!(H_{m\mathbf{Z}})_{\mathbf{Q}_{p}} \supset n!V_{H}(p, 1, r) = V_{H}(p, n, r)$, and since (by 11.4) $n!V_{H}(p, 1, r)$ contains a neighbourhood of the identity in $H_{\mathbf{Q}_{p}}$, we obtain the assertion of the lemma for any $n$.

## § 12. Unipotent elements in Γ and Gz

12.1. In §§ 14 and 16 we shall prove the following result:

12.1.1. LEMMA. There is a finite subset $B \subset \mathbf{Z}$ such that

$(U_{\mathbf{Z}} \cap \Gamma)_{\mathbf{Q}_p} = (U_{\mathbf{Z}})_{\mathbf{Q}_p}$ for any prime $p \notin B$ and any maximal unipotent $\mathbf{Q}$-subgroup $U$ of $G$.

12.2. In §§ 14 and 15 we shall prove the following result:

12.2.1. LEMMA. For any prime $p$ there is an $s(p)$ such that

$(U_{\mathbf{Z}} \cap \Gamma)_{\mathbf{Q}_p} \supset (U_{p^{s(p)}\mathbf{Z}})_{\mathbf{Q}_p}$ for any maximal unipotent $\mathbf{Q}$-subgroup $U$ of $G$.

12.3. PROOF OF LEMMA 10.1. Let $u \in (G_{n\mathbf{Z}})^u$, and let $U$ be a maximal unipotent $\mathbf{Q}$-subgroup of $G$ containing $u$. By Lemmas 12.1.1 and 12.2.1, $(U_{\mathbf{Z}} \cap \Gamma)_{\mathbf{Q}_p} \supset (U_{n\mathbf{Z}})_{\mathbf{Q}_p}$, where $n = \prod_{p \in B} p^{s(p)}$. On the other hand, by Lemmas 11.3.7 and 3.3.2, $U_{\mathbf{Z}} \cap \Gamma$ is commensurable with $U_{\mathbf{Z}}$. Therefore (by 11.3.5), $(U_{\mathbf{Z}} \cap \Gamma) \supset U_{n\mathbf{Z}} \ni u$, which proves the lemma.

## § 13. Some auxiliary results

13.1. NOTATION. According to Theorem 9.7.1, there is a maximal Q-split torus $S$ in $G$ and an order on the set of roots $\Phi =_{\mathbf{Q}}\Phi(S, G)$ such that for any $\theta \subset \Delta =_{\mathbf{Q}}\Delta(S, G)$, $\theta \neq \Delta$, the subgroup $P_{\theta} \cap G_{\mathbf{Z}}$ is commensurable with $P_{\theta} \cap \Gamma$, and $P_{\theta}^{-} \cap G_{\mathbf{Z}}$ with $P_{\theta}^{-} \cap \Gamma$. We put (§4.5) $P' = P_{\varnothing}, P'' = P_{\varnothing}^{-}$, $U' = R_u(P') = V_{\varnothing'}$, $U'' = R_u(P'') = V_{\varnothing}^{-}$. By $\mathfrak{U}'$ and $\mathfrak{U}''$ we denote the Lie algebras of $U'$ and $U''$. As before, $\mathfrak{G}$ is the Lie algebra of $G$. 13.2. We prove several lemmas.

13.2.1. LEMMA. 1) The subgroup $F$ generated by $U' \cup U''$ coincides with $G$; 2) the subalgebra generated by $\mathfrak{A}' \cup \mathfrak{A}''$ coincides with $\mathfrak{G}$.

PROOF. By [10], Proposition 4.11, $F$ is a normal subgroup of $G$ defined

over Q. But (by 9.7) G is simple over Q. Therefore, F = G, that is, 1) is true. Since the subgroups  $U'$  and  $U''$  are unipotent, they are connected. Therefore, 2) follows from 1).

13.2.2. LEMMA. The subgroup  $G_{Z} \cap \Gamma$  is Zariski-dense in G.

13.2.2. LEMMA. The subgroup $U_{\mathbf{Z}}' \cap \Gamma$ is Zariski-dense in $G$. PROOF. Since $P_{\mathbf{Z}}'$ is commensurable with $P' \cap \Gamma$, and $P_{\mathbf{Z}}''$ with $P'' \cap \Gamma$, $U_{\mathbf{Z}}' \cap \Gamma$ has finite index in $U_{\mathbf{Z}}'$, and $U_{\mathbf{Z}}'' \cap \Gamma$ in $U_{\mathbf{Z}}''$. Therefore (by 3.3.3 and 3.3.1), $U_{\mathbf{Z}}' \cap \Gamma$ and $U_{\mathbf{Z}}'' \cap \Gamma$ are dense in $U'$ and $U''$. It follows that $G_{\mathbf{Z}} \cap \Gamma$ is dense in the subgroup $F$ generated by $U' \cup U''$, which (by 13.2.1) coincides with $G$.

13.2.3. LEMMA. For any prime $p$ the subgroup $(G_{\mathbf{Z}} \cap \Gamma)_{\mathbf{Q}_p}$ is open in $G_{\mathbf{Q}_p}$.

PROOF. Since $U_{\mathbf{Z}}' \cap \Gamma$ is of finite index in $U_{\mathbf{Z}}'$, and $U_{\mathbf{Z}}'' \cap \Gamma$ in $U''$, (by 3.3.3) $U_{\mathbf{Z}}' \cap \Gamma \supset U_{n\mathbf{Z}}'$ and $U_{\mathbf{Z}}'' \cap \Gamma \supset U_{n\mathbf{Z}}''$ for some $n \in \mathbb{N}^+$. From Lemma 11.3.1 it follows that $(U_{n\mathbf{Z}}')_{\mathbf{Q}_p}$ is open in $U_{\mathbf{Q}_p}'$, and $(U_{n\mathbf{Z}}'')_{\mathbf{Q}_p}$ in $U_{\mathbf{Q}_p}''$. On the other hand (by 13.2.1), the subalgebra generated by $\mathfrak{u}' \cup \mathfrak{u}''$ coincides with $\mathfrak{G}$. Therefore, the subgroup $(G_{\mathbf{Z}} \cap \Gamma)_{\mathbf{Q}_p}$, which contains $(U_{\mathbf{Z}}' \cap \Gamma)_{\mathbf{Q}_p} \cup (U_{\mathbf{Z}}'' \cap \Gamma)_{\mathbf{Q}_p} \supset (U_{n\mathbf{Z}}')_{\mathbf{Q}_p} \cup (U_{n\mathbf{Z}}'')_{\mathbf{Q}_p}$, is open in $G_{\mathbf{Q}_p}$.

13.3. From Theorem 9.7.1, Lemma 11.2.1, and since there are only finitely many subgroups  $P_{\theta}$  and  $P_{\theta}^{-}$ , we obtain the next result.

13.3.1. LEMMA. There is a natural number $r$ such that $\Gamma \supset ((P_{\theta})_{r\mathbf{Z}})^u$ and $\Gamma \supset ((P_{\theta}^{-})_{r\mathbf{Z}})^u$ for any $\theta \neq \Delta$.

13.4. LEMMA. The product map is an isomorphism of the algebraic variety $U' \times P''$ onto a Zariski-dense open subset $W$ of $G$.

This lemma is a special case of Proposition 4.10 of [10] (that W is dense in G follows from the fact that G is connected). We denote by f and q the natural projections of W on  $U'$  and  $P''$ , respectively.

13.5. Since ([9], 3.7) any maximal unipotent Q-subgroup of G is the unipotent radical of some minimal parabolic Q-subgroup,  $P' = P_{\theta}$  and  $P'' = P_{\theta}^{-}$  are minimal parabolic Q-subgroups, and  $U' = R_{u}(P')$ ,  $U'' = R_{u}(P'')$ , from Lemma 4.7.2 we derive:

13.5.1. LEMMA. In $G_{\mathbf{Q}}$ there are finite subsets $M$ and $M$ such that for any maximal unipotent $\mathbf{Q}$-subgroup $U$ of $G$ there exist $g_U \in G_{\mathbf{Z}} \cdot M$ and $\widetilde{g}_U \in G_{\mathbf{Z}} \cdot \widetilde{M}$ such that $U = g_U U'' g_U^{-1}$ and $U = \widetilde{g}_U U' \widetilde{g}_U^{-1}$.

13.6. For any $X \subset \mathbf{Z}$, $X \neq \{0\}$, we denote by $\mathfrak{x}(X) \in \mathbb{N}^+$ the greatest common divisor of the elements of $X$. If $X = \{0\}$, then we put $\mathfrak{x}(X) = \infty$. For any integral-valued function $f$ on an arbitrary set $A$ and any subset $B \subset A$ we put $\alpha(f, B) = \mathfrak{x}(X)$, where $X = \{f(b); b \in B\}$. We say that a function $f$ on a set $E$ is not equal to zero and we write $f \neq 0$ if $f$ does not vanish identically on $E$.

13.6.1. LEMMA. Let A be a set, B a subset of A, L a finite-dimensional linear space (over Q) of functions on A taking rational values. We assume that for any  $f \in L$ ,  $f \neq 0$ , the restriction  $f_{B}$  of f to B is not equal to zero.

Then there is a $k \in \mathbf{N}^{+}$ such that $\alpha(f, B) \leqslant k\alpha(f, A)$ for any integral-valued function $f \in L$.

PROOF. It is clear that the set  $L_{Z}$  of integral-valued functions in L is a lattice of full dimension in  $L_{R} \otimes_{Q} R$ . Let  $L_{R}'$  be the dual space to  $L_{R}$ ,  $L_{Z}' \subset L_{R}'$  the dual lattice to  $L_{Z}$ , and  $M \subset L'$  the Z-module spanned by the functionals  $l_{b}(f) = f(b)$ ,  $b \in B$ . Since  $f_{B} \neq 0$ , if  $f \in L$ ,  $f \neq 0$ , then M is a lattice of full dimension in  $L_{R}'$ , and M and  $L_{Z}'$  are commensurable. Therefore,  $M \supset kL_{Z}'$  for some  $k \in N^{+}$ , which is easily seen to be equivalent to the assertion of the lemma.

13.7. Let H be an algebraic Q-group, y a non-zero regular rational function on H defined over Q, D a subset of  $H_{Z}$ , and M a subset of  $H_{Q}$ . We assume that  $y(h) \in \mathbf{Z}$  if  $h \in H_{Z} \cdot M$ . For any  $h \in H_{Z} \cdot M$  we put

$$
y _ {h} (h ^ {\prime}) = y (h ^ {\prime} h) \quad (h ^ {\prime} \in H _ {\mathbf {Z}}), \quad \psi (h) = \mathfrak {x} (y _ {h}, D)
$$

and $\omega(h) = \xi(y_h, H_{\mathbf{Z}})$.

13.7.1. LEMMA. If $D$ is Zariski-dense in $H$, then the function $\psi(h)$ defined on $H_{\mathbf{Z}} \cdot M$ is bounded.

PROOF. If $h' \in H_{\mathbf{Z}}$ and $h \in H_{\mathbf{Z}} \cdot M$, then $H_{\mathbf{Z}} \cdot h'h = H_{\mathbf{Z}} \cdot h$. Therefore, $\omega(h'h) = \omega(h)$ for any $h' \in H_{\mathbf{Z}}$, $h \in H_{\mathbf{Z}} \cdot M$. On the other hand, since $H_{\mathbf{Z}}$ is Zariski-dense in $H$ (because $H_{\mathbf{Z}} \supset D$), and $y \neq 0$, for any $h \in H_{\mathbf{Z}} \cdot M$ the restriction of $y_h$ to $H_{\mathbf{Z}}$ is not equal to zero, and hence, $\omega(h) < \infty$ for any $h \in H_{\mathbf{Z}} \cdot M$. From this, using the finiteness of $M$, we obtain

$$
\sup _ {h \in H _ {\mathbf {Z}} \cdot M} \omega (h) = \sup _ {h \in M} \omega (h) = B <   \infty .\tag{1}
$$

For some $n$ the algebraic $\mathbf{Q}$-group $H$ is an algebraic subvariety of the linear space $L(n, \mathbf{Q})$ of all $n \times n$-matrices with coefficients in $\mathbf{Q}$. Since $y$ is a regular function on $H$, ([23], §45, Corollary 3) $y$ is the restriction to $H$ of some polynomial on $L(n, \mathbf{Q})$. Therefore the linear space $L$ generated by the functions $y_h$ (for $h \in H_{\mathbf{Z}} \cdot M$) is finite-dimensional. On the other hand, since $D$ is Zariski-dense in $H$, that is, $f \neq 0$ for $f \in L$, the restriction of $f$ to $D$ is not equal to zero. Therefore, (see 13.6) there is a $k$ such that $\psi(h) = \chi(y_h, D) < k\xi(y_h, H_{\mathbf{Z}}) = \omega(h)$ for any $h \in H_{\mathbf{Z}} \cdot M$. From this and from (1) the assertion of the lemma follows.

13.8. Here we use the notation of §11.1.

13.8.1. LEMMA. There exists a natural number $m$ such that for any maximal unipotent $\mathbf{Q}$-subgroup $U$ of $G$ and any prime $p$ there is a $\gamma_{U,p} \in G_{\mathbf{Z}} \cap \Gamma$ such that $\gamma_{U,p} U \gamma_{U,p}^{-1} p = u U'' u^{-1}$, where $u \in U_{\mathbf{Q}}'$ and $v_p(u) \geqslant -v_p(m)$, $v_p(u^{-1}) \geqslant -v_p(m)$.

PROOF. Let $f, q$ and $W$ be as in §13.4. Since $U'$ and $P''$ are defined over $\mathbf{Q}$, the entries of $f(g)$ and $f(g)^{-1}, g \in W$, are rational functions on $G$ defined over $\mathbf{Q}$. We denote these functions by $a_1, \ldots, a_l$. Since $U'$ and $P''$ are defined over $\mathbf{Q}$, the subvariety $G - W$ is defined over $\mathbf{Q}$. But $G$ is an affine variety. Therefore, for some non-constant regular function on $G$

defined over $\mathbf{Q}$ we have $W\supset G_F$, where $G_{F} = \{g\in G; F(g)\neq 0\}$. Let $M$ be the same as in §13.5. Since $M\subset G_{\mathbf{Q}}$ is finite, after multiplying $b_i$, $c_i$ and $F$ by a non-zero constant, we may assume that these functions take integral values on $G_{\mathbf{Z}}\cdot M$. We put $y = F\cdot \prod_{i=1}^{l} c_i$. Since (see 13.2.2) $G_{\mathbf{Z}}\cap \Gamma$ is Zariski-dense in $G$, (by 13.7.1) for any $g\in G_{\mathbf{Z}}\cdot M$ the greatest common divisor of the numbers $y_g(\gamma) = y(\gamma g)$, $\gamma \in G_{\mathbf{Z}}\cap \Gamma$, is less than a certain $t$ that does not depend on $g$. Therefore, for any $g\in G_{\mathbf{Z}}\cdot M$ and any prime $p$ there is a $\gamma (g,p)\in G_{\mathbf{Z}}\cap \Gamma$ such that $v_{p}(y(\gamma (g,p)\cdot g)\geqslant -v_{p}(m)$, where $m = t!$. Since $y(\gamma (g,p)\cdot g)\neq 0$, $\gamma (g,p)\in W$ for any $g\in G_{\mathbf{Q}}$. Let $U$ be a maximal unipotent $\mathbf{Q}$-subgroup of $G$, and $p$ a prime number. We put $\gamma_{U,p} = \gamma (g_U,p)$, $f(\gamma_{U,p}\cdot g_U) = u$, $q(\gamma_{U,p}\cdot g_U) = s$. Then, since $s\in P''$ normalizes $U'',\gamma_{U,p}U\gamma_{U,p}^{-1} = \gamma_{U,p}g_U U''g_U^{-1}\gamma_{U,p}^{-1} = usU''s^{-1}u^{-1} = uU''u^{-1}$. Using the definition of $y$, it now remains to note that $\min [v_p(u),v_p(u^{-1})]\geqslant -v_p(y(\gamma_U,p\cdot g_U))\geqslant -v_p(m)$, and the lemma is proved.

## § 14. Groups G of Q-rank ≥ 2

In this and the following sections we use the notation of §§4.5, 11.1, and 13.1.

14.1. In this section we assume that $\mathrm{rank}_{\mathbf{Q}}G\geqslant 2$. For any natural number $k$, we denote by $\Omega_k$ the subgroup generated by the union $\bigcup_{\theta \neq \Delta}(B_{\theta}^{-})_{k\mathbb{Z}}$. Since the subgroups $B_{\theta}^{-}$ are unipotent, (by 11.3.2)

$((B_{\theta}^{-})_{k\mathbf{Z}})_{\mathbf{Q}_{p}} = ((B_{\theta}^{-})_{p(k)\mathbf{Z}})_{\mathbf{Q}_{p}}$ for any prime $p$ and any $\theta$. Therefore we have: 14.1.1. LEMMA. For any prime $p$ and any $k \in \mathbf{N}^{+}$, $(\Omega_k)_{\mathbf{Q}_p} = (\Omega_{p(k)})_{\mathbf{Q}_p}$.

14.1.2. LEMMA. For any natural number $k$ there is a $t(k)$ such that $\Omega_k \supset U_{t(k)\mathbf{Z}}''$.

PROOF. Since $\operatorname{rank}_{\mathbf{Q}} G \geqslant 2$, $\bigcup_{\alpha \in \Delta} G_{\alpha}' \subset \bigcup_{\theta \neq \Delta} B_{\theta}^{-}$. Therefore, (by 4.5.2)

$\bigcup_{\theta \neq \Delta} B_{\theta}^{-}$ generates $U'' = V_{\phi}^{-}$. On the other hand, (by 3.3.1) $(B_{\theta}^{-})_{k\mathbf{Z}}$ is dense in $B_{\theta}^{-}$ for any $\theta$. Therefore, $\Omega_k \subset U_{k\mathbf{Z}}''$ is Zariski-dense in $U''$. Hence, (see 3.3.2) $\Omega_k$ is commensurable with $U_{\mathbf{Z}}''$, and therefore, (by 3.3.3) contains $U_{t(k)\mathbf{Z}}''$.

14.2. Let $t(k)$ and $r$ be the same as in Lemmas 13.3.1 and 14.1.2.

14.2.1. LEMMA. If $u \in U_{\mathbf{Q}}'$, $p$ is a prime and $l$ a non-negative integer, $v_p(u) \geqslant -l$, $v_p(u^{-1}) \geqslant -l$, then $((uU''u^{-1})_{\mathbf{Z}} \cap \Gamma)_{\mathbf{Q}_p} \supset ((uU''u^{-1})_{p(t(rp^2l))_p^2l_\mathbf{Z}})_{\mathbf{Q}_p}$.

PROOF. Since for any $\theta \subset \Delta$, $\theta \neq \Delta$, $B_{\theta}^{-} \subset (P_{\theta})^{u}$, $u \in P_{\phi} \subset P_{\theta}$, and (by 13.3) $\Gamma \supset ((P_{\theta})_{r\mathbf{Z}})^{u}$, for any $\theta \subset \Delta$, $\theta \neq \Delta$,

$$
(u B _ {\theta} ^ {-} u ^ {- 1}) \cap \Gamma \supset (u B _ {\theta} ^ {-} u ^ {- 1}) _ {r \mathbf {Z}}.\tag{1}
$$

Since $v_{p}(u) \geqslant -l$ and $v_{p}(u^{-1}) \geqslant -l$, there is an $s$, $v_{p}(s) < 2l$, such that $(uB_{\theta}^{-}u^{-1})_{r\mathbf{Z}} \supset u(B_{\theta}^{-})_{sr\mathbf{Z}}u^{-1}$ for any $\theta \subset \Delta$. From this and from (1), and Lemmas 14.1.1 and 14.1.2 we obtain

$$
\begin{array}{r l} (2) & ((u U ^ {\prime \prime} u ^ {- 1}) _ {\mathbf {Z}} \cap \Gamma) _ {\mathbf {Q} _ {p}} \supset (u \Omega_ {s r} u ^ {- 1}) _ {\mathbf {Q} _ {p}} = u (\Omega_ {s r}) _ {\mathbf {Q} _ {p}} u ^ {- 1} = u (\Omega_ {p (s r)}) _ {\mathbf {Q} _ {p}} u ^ {- 1} \supset \\ & \supset u (\Omega_ {r p ^ {2 l}}) _ {\mathbf {Q} _ {p}} u ^ {- 1} \supset u (U _ {a \mathbf {Z}} ^ {\prime \prime}) _ {\mathbf {Q} _ {p}} u ^ {- 1}, \end{array}
$$

where $a = t(rp^{2l})$. Since $v_{p}(u) \geqslant -l$ and $v_{p}(u^{-1}) \geqslant -l$,

$U_{a\mathbf{Z}} = (u^{-1}(uU''u^{-1})u)_{a\mathbf{Z}} \supset u^{-1}(uU''u^{-1})_{ba\mathbf{Z}}u,$ where $v_p(b) \leqslant 2l$. From this and from (2) and Lemma 11.3.2 we obtain

$$
\begin{array}{r l} & ((u U ^ {\prime \prime} u ^ {- 1}) _ {\mathbf {Z}} \cap \Gamma) _ {\mathbf {Q} _ {p}} \supset u (U _ {a \mathbf {Z}} ^ {\prime \prime}) _ {\mathbf {Q} _ {p}} u ^ {- 1} = \\ & \qquad = (u U _ {a \mathbf {Z}} ^ {\prime \prime} u ^ {- 1}) _ {\mathbf {Q} _ {p}} \supset ((u U ^ {\prime \prime} u ^ {- 1}) _ {b a \mathbf {Z}}) _ {\mathbf {Q} _ {p}} = \\ & \qquad = ((u U ^ {\prime \prime} u ^ {- 1}) _ {p (b a) \mathbf {Z}}) _ {\mathbf {Q} _ {p}} \supset ((u U ^ {\prime \prime} u ^ {- 1}) _ {p (t (r p ^ {2 l})) p ^ {2 l} \mathbf {Z}}) _ {\mathbf {Q} _ {p}}. \end{array}\tag{3}
$$

14.3. PROOF OF LEMMAS 12.1 AND 12.2.1 IN CASE $\mathrm{rank}_{\mathbf{Q}}G\geqslant 2$. Let $m$ be the same as in Lemma 13.8.1 and let $U$ be an arbitrary maximal unipotent $\mathbf{Q}$-subgroup of $G$. Then (by 13.8) for any prime $p$ there is a $\gamma_{U,p}\in G_{\mathbf{Z}}\cap \Gamma$ such that $\gamma_{U,p}U\gamma_{U,p}^{-1} = uU^{\prime \prime}u^{-1}$, where $u\in U_{\mathbf{Q}}$ and $v_{p}(u)\geqslant -v_{p}(m)$, $v_{p}(u^{-1})\geqslant -v_{p}(m)$. By Lemma 14.2.1,

$$
((\gamma_ {U, p} U \gamma_ {U, p} ^ {- 1}) _ {\mathbf {Z}} \cap \Gamma) _ {\mathbf {Q} _ {p}} = ((u U ^ {\prime \prime} u ^ {- 1}) _ {\mathbf {Z}} \cap \Gamma) _ {\mathbf {Q} _ {p}} \supset ((u U ^ {\prime \prime} u ^ {- 1}) _ {p (t (r p (m ^ {2}))) p (m ^ {2}) \mathbf {Z}}) _ {\mathbf {Q} _ {p}} =
$$

$$
= (\gamma_ {U, p} U \gamma_ {U, p} ^ {- 1}) _ {p (t (r p (m ^ {2}))) p (m ^ {2}) \mathbf {Z}}) _ {\mathbf {Q} p}
$$

and since $\gamma_{U,p} \in G_{\mathbf{Z}} \cap \Gamma$, we have

$$
(U _ {\mathbf {z}} \cap \Gamma) _ {\mathbf {Q} _ {p}} \supset (U _ {p (t (r p (m ^ {2}))) p (m ^ {2}) \mathbf {Z}}) _ {\mathbf {Q} _ {p}}.\tag{4}
$$

The assertions of Lemmas 12.1.1 and 12.2.1 follow immediately from (4).

## § 15. Groups G of Q-rank 1

15.1. In this section we use the notation of §§4.5, 11.1, and 13.1 and assume that $\operatorname{rank}_{\mathbf{Q}} G = 1$.

We put $C = P' \cap P'' = P_{\phi} \cap P_{\phi}^{-} = C(S)$. Since $P'$ and $P''$ are opposite, $C$ is a Levi Q-subgroup of $P'$. We denote by $F$ the semisimple part of the reductive group $C$, that is, the maximal connected semisimple normal subgroup of $C$.

15.1.1. DEFINITION. G is called weakly non-compact if  $F_{R}$  is compact, or, equivalently, if  $(F_{\mathbf{R}})^{u} = (C_{\mathbf{R}})^{u} = \{e\}$ , and strongly non-compact otherwise.

Since  $\operatorname{rank}_{\mathbf{Q}} G = 1$ ,  $\Phi^{+}$  contains precisely one indivisible root, which will be denoted throughout this section by  $\alpha$ . (Indivisible means that  $\alpha$  is a root,

but $\alpha / 2$ is not.) Then $\Delta = \{\alpha\}$. Since $\alpha$ is indivisible, by the Proposition in [18], Ch. VI, §1, we have the following result.

15.1.2. LEMMA. Either $\Phi^{+} = \{\alpha\}$ or $\Phi^{+} = \{\alpha, 2\alpha\}$, and hence, either $\mathfrak{U}' = \mathfrak{G}_{\alpha}$ or $\mathfrak{U}' = \mathfrak{G}_{\alpha} \oplus \mathfrak{G}_{2\alpha}$:

We note that since (by [10], 4.3) $P'$ is connected, $C$ is connected.

15.2. Let $N$ be a connected normal subgroup of $C$ defined over $\mathbf{Q}$, $\mathfrak{N}$ the Lie algebra of $N, \mathfrak{M}$ the subalgebra generated by $[\mathfrak{N}, \mathfrak{U}']$.

15.2.1. LEMMA. If $\mathfrak{N} \neq \{0\}$ then $[\mathfrak{N}, \mathfrak{G}_{\alpha}] = \mathfrak{G}_{\alpha}$.

PROOF. Since $C = C(S)$, (Ad $C$)$\mathfrak{G}_{\alpha} = \mathfrak{G}_{\alpha}$. But $C$ normalizes $N$, hence (Ad $C$)$\mathfrak{N} = \mathfrak{N}$. Therefore, (Ad $C$)[$\mathfrak{N}$, $\mathfrak{G}_{\alpha}$] = [$\mathfrak{N}$, $\mathfrak{G}_{\alpha}$]. On the other hand, 1) since $N \subset C = C(S)$, [$\mathfrak{N}$, $\mathfrak{G}_{\alpha}$] ⊂ $\mathfrak{G}_{\alpha}$; 2) since $N$ is defined over $\mathbf{Q}$, the subspace [$\mathfrak{N}$, $\mathfrak{G}_{\alpha}$] is defined over $\mathbf{Q}$. Therefore, by Lemma 4.5.1, 2) either [$\mathfrak{N}$, $\mathfrak{G}_{\alpha}$] = $\mathfrak{G}_{\alpha}$, or [$\mathfrak{N}$, $\mathfrak{G}_{\alpha}$] = {0}. Assume that [$\mathfrak{N}$, $\mathfrak{G}_{\alpha}$] ≠ $\mathfrak{G}_{\alpha}$. Then [$\mathfrak{N}$, $\mathfrak{G}_{\alpha}$] = {0}. Since (by 4.5.1) $\mathfrak{G}_{2\alpha} = [\mathfrak{G}_{\alpha}, \mathfrak{G}_{\alpha}]$ and $\mathfrak{U}' = \mathfrak{G}_{\alpha} \oplus \mathfrak{G}_{2\alpha}$, we see that [$\mathfrak{N}$, $\mathfrak{U}'$] = {0}. But $N$ and $U'$ are connected. Therefore, $N \subset C(U')$. Since $G$ is simple over $\mathbf{Q}$, the maximal unipotent $\mathbf{Q}$-subgroup $U'$ is not contained in any non-trivial normal subgroup of $G$, hence (see 9.1), $C \cap C(U') = \{e\}$. Therefore, $N = \{e\}$ and $\mathfrak{N} = \{0\}$. This is a contradiction, and the lemma is proved.

15.2.2. LEMMA. If $\mathfrak{N} \neq \{0\}$ then $\mathfrak{M} = \mathfrak{U}'$.

PROOF. By 15.1, either $\mathfrak{U}' = \mathfrak{G}_{\alpha}$ or $\mathfrak{U}' = \mathfrak{G}_{\alpha} \oplus \mathfrak{G}_{2\alpha}$. If $\mathfrak{U}' = \mathfrak{G}_{\alpha}$ then (see 15.2.1) $\mathfrak{M} \supset \mathfrak{G}_{\alpha} = \mathfrak{U}'$. If $\mathfrak{U}' = \mathfrak{G}_{\alpha} \oplus \mathfrak{G}_{2\alpha}$, then, since $\mathfrak{G}_{2\alpha} = [\mathfrak{G}_{\alpha}, \mathfrak{G}_{\alpha}]$ we have (see 15.2.1) $\mathfrak{M} \supset \mathfrak{G}_{\alpha} \oplus \mathfrak{G}_{2\alpha} = \mathfrak{U}'$.

15.3. In this subsection we assume that $G$ is strongly non-compact.

15.3.1. LEMMA. Let $K$ be a non-empty open subset of $U_{\mathbf{Q}_p}'$, and $n \in \mathbb{N}^+$. Then there is a neighbourhood $V(K, n)$ of the identity in $U_{\mathbf{Q}_p}'$ such that if $\Lambda$ is a subgroup of $P_{\mathbf{Z}}$, $A$ a subset of $K \cap U_{\mathbf{Q}}'$ that is dense in $K$ (in the p-adic topology), and $(aCa^{-1})_{\mathbf{Z}} \cap \Lambda$ is of index at most $n$ in $(aCa^{-1})_{\mathbf{Z}}$ for any $a \in A$, then $(U' \cap \Lambda)_{\mathbf{Q}_p} \supset V(K, n)$.

PROOF. Since  $F_{R}$  is non-compact and F is semisimple, in F there is a Q-simple connected normal subgroup N defined over Q, such that  $N_{R}$  is non-compact. Since (by 15.1) C is connected and normalizes F, and since the semisimple group F has only finitely many normal subgroups, C normalizes N. Therefore, (see 15.2.2)

$$
\mathfrak {M} = \mathfrak {U} ^ {\prime},\tag{1}
$$

where $\mathfrak{M}$ is the subalgebra generated by $[\mathfrak{N},\mathfrak{U}']$. Without loss of generality we may assume that $K$ is relatively compact in $U_{\mathbf{Q}_p}'$. Then there exists a constant $d(K)\in \mathbf{N}^{+}$ such that $v_{p}(u) > - d(K)$ for any $u\in U_{\mathbf{Q}_p}'$. Therefore, for any $u\in K\cap U_{\mathbf{Q}}'$

$$
(u N u ^ {- 1}) _ {\mathbf {Z}} \supset u N _ {m (u) \mathbf {Z}} u ^ {- 1}; v _ {p} (m (u)) <   d (K).\tag{2}
$$

(4)

For $a_1 \in A$, $a_2 \in A$ we put $\Lambda_{a_1} = (a_1 Ca_1^{-1}) \cap \Lambda$, $\Lambda_{a_1, a_2} = F_{m(a_1)m(a_2)\mathbf{Z}} \cap a_1^{-1} \Lambda_{a_1} a_1 \cap a_2^{-1} \Lambda_{a_2} a_2$. Since $A \subset K \cap U_{\mathbf{Q}}'$, the subgroup $\Lambda_{a_1, a_2}$ is of index at most $n^2$ in $F_{m(a_1)m(a_2)\mathbf{Z}}$. Therefore (11.5.1),

$$
(\Lambda_ {a _ {1}, a _ {2}}) _ {\mathbf {Q} _ {p}} \supset V ^ {\prime},\tag{3}
$$

where $V' = V_N(p, n^2, 2d(K))$. For any $\lambda \in \Lambda_{a_1, a_2}$ we have $(a_1\lambda a_1^{-1})(a_2\lambda a_2^{-1})^{-1} = a_1(\lambda, a_1^{-1}a_2)a_1^{-1}$. But $\Lambda_{a_1, a_2} \subset N$ normalizes $U'$. Therefore,

$$
\begin{array}{r l} (U ^ {\prime} \cap \Lambda) \supset U ^ {\prime} \cap (\Lambda_ {a _ {1}} \cdot \Lambda_ {a _ {2}} ^ {- 1}) \supset U ^ {\prime} \cap ((a _ {1} \Lambda_ {a _ {1}, a _ {2}} a _ {1} ^ {- 1}) \cdot (a _ {2} \Lambda_ {a _ {1}, a _ {2}} a _ {2} ^ {- 1}) ^ {- 1}) \supset \\ & \supset U ^ {\prime} \cap a _ {1} \left\{\Lambda_ {a _ {1}, a _ {2}}, a _ {1} ^ {- 1} a _ {2} \right\} a _ {1} ^ {- 1} = a _ {1} \left\{\Lambda_ {a _ {1}, a _ {2}}, a _ {1} ^ {- 1} a _ {2} \right\} a _ {1} ^ {- 1}. \end{array}
$$

From this and from (3) we derive

$$
(U ^ {\prime} \cap \Lambda) _ {\mathbf {Q} _ {p}} \supset a _ {1} \left\{V ^ {\prime}, a _ {1} ^ {- 1} a _ {2} \right\} a _ {1} ^ {- 1}.
$$

Since $K$ is open in $U_{\mathbf{Q}_p}'$ and $A$ is dense in $K$, there is a neighbourhood $W$ of the identity in $U_{\mathbf{Q}_p}'$ (depending on $K$, but not on $A$) and an $a_1 \in A$ such that $(a_1^{-1}A) \cap W$ is dense in $W$. From this and from (4) we obtain

$$
(U ^ {\prime} \cap \Lambda) _ {\mathbf {Q} _ {p}} \supset a _ {1} \left\{V ^ {\prime}, W \right\} a _ {1} ^ {- 1}.\tag{5}
$$

We denote by $E$ the closure in $U_{\mathbf{Q}_p}'$ of the subgroup generated by $\{V', W\}$. Since $V'$ is open in $N_{\mathbf{Q}_p}$ and $W$ in $U_{\mathbf{Q}_p}'$, and by (1) $\mathfrak{M} = \mathfrak{U}', E$ is open in $U_{\mathbf{Q}_p}'$. Since $K$ is compact, it follows that $V(K, n) = \bigcap_{k \in K} kEk^{-1}$ is open

in $U_{\mathbf{Q}_p}'$. On the other hand, it follows from (5) that $(U' \cap \Lambda)_{\mathbf{Q}_p} \supset V(K, n)$, and the lemma is proved.

15.3.2. LEMMA. For any finite subset $E \subset G_{\mathbf{Q}}$ there is a neighbourhood $V(E)$ of the identity in $U_{\mathbf{Q}_p}'$ such that

$$
(U _ {\mathbf {Z}} ^ {\prime} \cap g \Gamma g ^ {- 1}) _ {\mathbf {Q} _ {p}} \supset V (E) f o r a n y g \in E \cdot G _ {\mathbf {Z}}.
$$

PROOF. Let $f, q$ and $W$ be as in §13.4. We fix $g_0 \in E \cdot G_{\mathbf{Z}}$ and put $A'(g_0) = g_0 \cdot (G_{\mathbf{Z}} \cap \Gamma)$, $K'(g_0) = (A'(g_0))_{\mathbf{Q}_p}$, $A(g_0) = f(W \cap A'(g_0))$,

and $K(g_0) = f(W \cap K'(g_0))$. Since (by 13.2.3) ($G_{\mathbf{Z}} \cap \Gamma$)$_{\mathbf{Q}_p}$ and (by 13.4) $W$ is a dense Zariski-open subset of $G$, $W \cap K'(g_0)$ is non-empty and open in $G_{\mathbf{Q}_p}$, and since (see 13.4) the map of the product $U' \times P''$ onto $W$ is an isomorphism of algebraic varieties, $K(g_0) = f(W \cap K'(g_0))$ is open in $U'_{\mathbf{Q}_p}$. We also note that since $A'(g_0)$ is dense in $K'(g_0)$ and $W$ is open in $G$, $A(g_0)$ is dense in $K(g_0)$.

We denote by $a$ the product of the entries of all the matrices of the finite set $E \cup E^{-1}$, and by $k$ the index of $G_{a^2\mathbf{Z}}$ in $G_{\mathbf{Z}}$. Then for any $g \in A'(g_0) = g_0 \cdot (G_{\mathbf{Z}} \cap \Gamma)$ we have $(gP''g^{-1})_{\mathbf{Z}} \supset gP_{a\mathbf{Z}}''g^{-1}$, and

$$
g P _ {a \mathbf {Z}} ^ {\prime \prime} g ^ {- 1} \supset (g P ^ {\prime \prime} g ^ {- 1}) _ {a ^ {2} \mathbf {Z}}
$$

$$
g P _ {a \mathbf {Z}} ^ {\prime \prime} g ^ {- 1}
$$

$$
(g P ^ {\prime \prime} g ^ {- 1}) _ {Z}
$$

But (by 9.7.1) $P_{\mathbf{Z}}'' \cap \Gamma = (P_{\varnothing})_{\mathbf{Z}} \cap \Gamma$ is of finite index, say $t$, in $P_{\mathbf{Z}}''$. Therefore, for any $g \in A'(g_0) = g_0 \cdot (G_{\mathbf{Z}} \cap \Gamma)$ the subgroup $(gP''g^{-1})_{\mathbf{Z}} \cap g\Gamma g^{-1} = (gP_{\varnothing}g^{-1})_{\mathbf{Z}} \cap g\Gamma g^{-1} \supset gP_{a\mathbf{Z}}''g^{-1} \cap g\Gamma g^{-1} \supset g(P_{a\mathbf{Z}}'' \cap \Gamma)g^{-1}$ is of index at most $T = kt$ in $(gP''g^{-1})_{\mathbf{Z}}$. But

$$
\begin{array}{r l} f (g) C f (g) ^ {- 1} & = f (g) \left(P ^ {\prime} \cap P ^ {\prime \prime}\right) f (g) ^ {- 1} = P ^ {\prime} \cap f (g) P ^ {\prime \prime} f (g) ^ {- 1} = \\ & = P ^ {\prime} \cap f (g) q (g) P ^ {\prime \prime} q (g) ^ {- 1} f (g) ^ {- 1} = P ^ {\prime} \cap g P ^ {\prime \prime} g ^ {- 1}. \end{array}
$$

Therefore, for any $g \in A'(g_0)$ the subgroup $(f(g)Cf(g)^{-1})_{\mathbf{Z}} \cap g_0\Gamma g_0^{-1}$ is of index at most $T$ in $(f(g)Cf(g)^{-1})_{\mathbf{Z}}$. From this and Lemma 15.3.1 it follows that

$$
(U _ {\mathbf {z}} ^ {\prime} \cap g _ {0} \Gamma g _ {0} ^ {- 1}) _ {\mathbf {Q} _ {p}} \supset V (K (g _ {0}), T).\tag{6}
$$

If $g_1 \in E \cdot G_{\mathbf{Z}}$, $g_2 \in E \cdot G_{\mathbf{Z}}$ and $g_1^{-1}g_2 \in (G_{\mathbf{Z}} \cap \Gamma)_{\mathbf{Q}_p}$, then $K'(g_1) = K'(g_2)$ and $K(g_1) = K(g_2)$. On the other hand, since $E$ is finite, $(E \cdot G_{\mathbf{Z}})_{\mathbf{Q}_p}$ is compact; 2) (by 13.2.3) $(G_{\mathbf{Z}} \cap \Gamma)_{\mathbf{Q}_p}$ is open in $G_{\mathbf{Q}_p}$. Therefore, the number of distinct sets $K(g)$, $g \in E \cdot G_{\mathbf{Z}}$, is finite. From this and (6) the assertion of the lemma follows.

PROOF OF LEMMA 12.2.1 FOR STRONGLY NON-COMPACT GROUPS. Let $U$ be a maximal unipotent $\mathbf{Q}$-subgroup of $G$, and let $\widetilde{M}$ and $\widetilde{g}_U$ be the same as in Lemma 13.5.1, Then (by 15.3.2) $(U_{\mathbf{Z}}' \cap g_{U}^{-1}\Gamma g_U)_{\mathbf{Q}_p} \supset V(\widetilde{M}^{-1})$. But $V(\widetilde{M}^{-1})$ is open in $U_{\mathbf{Q}_p}'$ and hence, contains $(U_{p^s(M)}' \mathbf{Q}_p)$ for some $s(M) \in \mathbb{N}^+$. Therefore,

$$
(U _ {\mathbf {Z}} ^ {\prime} \cap \widetilde {g} _ {U} ^ {- 1} \Gamma \widetilde {g} _ {U}) _ {\mathbf {Q} _ {p}} \supset (U _ {p ^ {s (M)} \mathbf {Z}} ^ {\prime}) _ {\mathbf {Q} _ {p}}.\tag{7}
$$

We denote by $d$ the product of the matrix entries of all the elements of the finite set $\widetilde{M} \cup \widetilde{M}^{-1}$. Then from (7) and Lemma 11.3.2 we obtain

$$
\begin{array}{r l} & {(U _ {\mathbf {Z}} \cap \Gamma) _ {\mathbf {Q} _ {p}} = ((\widetilde {g} _ {U} \Gamma \widetilde {g} _ {U} ^ {- 1}) _ {\mathbf {Z}} \cap \Gamma) _ {\mathbf {Q} _ {p}} \supset (\widetilde {g} _ {U} U _ {d \mathbf {Z}} ^ {\prime} \widetilde {g} _ {U} ^ {- 1} \cap \Gamma) _ {\mathbf {Q} _ {p}} =} \\ & {\qquad = \widetilde {g} _ {U} (U _ {d \mathbf {Z}} ^ {\prime} \cap \widetilde {g} _ {U} ^ {- 1} \Gamma \widetilde {g} _ {U}) _ {\mathbf {Q} _ {p}} \widetilde {g} _ {U} ^ {- 1} \supset \widetilde {g} _ {U} (U _ {d p ^ {s (M)} \mathbf {Z}} ^ {\prime}) _ {\mathbf {Q} _ {p}} \widetilde {g} _ {U} ^ {- 1} =} \\ & {\qquad \qquad = (\widetilde {g} _ {U} U _ {d p ^ {s (M)} \mathbf {Z}} ^ {\prime} \widetilde {g} _ {U} ^ {- 1}) _ {\mathbf {Q} _ {p}} \supset (U _ {d ^ {2} p ^ {s (M)} \mathbf {Z}}) _ {\mathbf {Q} _ {p}} = (U _ {p (d ^ {2}) p ^ {s (M)} \mathbf {Z}}) _ {\mathbf {Q} _ {p}},} \end{array}\tag{8}
$$

which proves the lemma (with $s(p) = 2v_{p}(d) + s(M)$).

15.4. CLASSIFICATION OF R-SIMPLE WEAKLY NON-COMPACT GROUPS. In this subsection we assume that G is weakly non-compact and use the notation of 15.1.

For a semisimple $k$-group $H$ and a field $K \supset k$ we denote by $\Delta_K(H)$ the subset of the Dynkin diagram of $H$ obtained by deleting the distinguished orbits in the $K$-index ([26], 2.3) of $H$. By considering Tits' classification table for the $k$-indices of absolutely simple groups ([26], Table II) we deduce:

15.4.1. LEMMA. Let $k$ be a finite extension of $\mathbf{Q}$ and $H$ an absolutely simple algebraic $k$-group. 1) If $H$ is quasi-split over $k$, that is, $\Delta_k(H) = \emptyset$. and $\operatorname{rank}_k H = 1$, then in the notation of Table II of [26] $H$ is either of

type $^{1}A_{1,1}^{(1)}$ or of type $^{2}A_{2,1}^{(1)}$; 2) if $k \subset \mathbf{R}$, $\Delta_k(H) = \Delta_\mathbf{R}(H)$, $\mathrm{rank}_k H = 1$, $\mathrm{rank}_\mathbf{R} H \geqslant 2$, then $H$ is over $k$ of one of the following types: $^{2}A_{2,1}^{(1)}$, $^{2}A_{5,2}^{(2)}$, $^{2}E_{6,1}^{29}$, and over $\mathbf{R} ^{1}A_{2,2}^{(1)}$, $^{1}A_{5,2}^{(1)}$, $^{1}E_{6,2}^{28}$ respectively.

From the fact that  $(C_{\mathbf{R}})^{u} = \{e\}$  it follows that a minimal parabolic Q-subgroup  $P'$  is a minimal parabolic R-subgroup of G. From this and the classification of parabolic k-subgroups ([10], 5.14) we find that

$$
\Delta_ {\mathbf {R}} (G) = \Delta_ {\mathbf {Q}} (G).\tag{9}
$$

Since G is an adjoint group, ([26], 3.1.2) there is a finite extension k of Q and an absolutely simple adjoint k-group H such that  $G = R_{k/Q}H$ , where, as in [26],  $R_{k/k'}$  denotes the functor of “restriction of the field of scalars” from k to  $k'$ .

15.4.2. LEMMA. If $G$ is simple over $\mathbf{R}$ or, what is the same, $k = \mathbf{Q}$, or if $k$ is an imaginary quadratic extension of $\mathbf{Q}$, then $G$ is locally isomorphic over $\mathbf{R}$ to one of the following groups: 1) $SL_3(\mathbf{R})$; 2) $SL_3(D)$, where $D$ is a quaternion algebra over $\mathbf{R}$; 3) a group of type $^1E_{6,2}^{28}$; 4) $R_{\mathbf{C} / \mathbf{R}}SL_3(\mathbf{C})$. Here $G$ is isomorphic over $\mathbf{Q}$, respectively, to groups of the type $^2A_{2,1}^{(1)}$, $^2A_{5,1}^{(2)}$, $^2E_{6,1}^{29}$ or to the group $R_{k / \mathbf{Q}}H$, where $k$ is an imaginary quadratic extension of $\mathbf{Q}$, and $H$ is isomorphic over $k$ to a group of type $^2A_{2,1}^{(1)}$.

PROOF. For $k = \mathbf{Q}$ the assertion of the lemma follows from (9) and Lemma 15.4.1 (and also the classification of the absolutely simple $k$-groups given in [26]). Suppose that $k$ is an imaginary quadratic extension of $\mathbf{Q}$. Then by Theorem 1.3.1 (or 1.3.2) of [27] $G$ is isomorphic over $\mathbf{R}$ to $R_{\mathbf{C} / \mathbf{R}}H$. Using the description of the $\mathbf{Q}$-index of $G$ in terms of the $k$-index of $H$, and also the description of the $\mathbf{R}$-index of $R_{\mathbf{C} / \mathbf{R}}H$ ([26], 3.1.2), and the fact that $\operatorname{rank}_{\mathbf{R}}G = 2$, we obtain from this and from (9) that $H$ is quasi-split over $k$ and $\operatorname{rank}_{\mathbf{C}}H = 2$. Now it remains to apply Lemma 15.4.1.

15.4.3. REMARK. We do not give a classification of all the weakly non-compact groups G, although it would not be hard to do so. We only observe that if  $G = R_{k/Q}H$  is weakly non-compact and H is absolutely simple, then H is of one of the types described in Lemma 15.4.1.

15.5. The proof of Lemma 12.2.1 for weakly non-compact groups is more complicated than for strongly non-compact groups and will be given elsewhere.

## § 16. Groups G of Q-rank 1 (conclusion)

In this section we assume that $\operatorname{rank}_{\mathbf{Q}} G = 1$.

16.1. Since $\operatorname{rank}_{\mathbf{Q}} G = 1$, by Lemmas 4.5.3 and 4.5.4 the intersection of any two distinct maximal unipotent $\mathbf{Q}$-subgroups of $G$ is $\{e\}$. But $\Gamma \subset G_{\mathbf{Q}}$. Therefore we have:

16.1.1. LEMMA. Every non-trivial unipotent element v of  $\Gamma$  is contained in precisely one maximal unipotent subgroup  $U(v)$  of  $\Gamma$ .

16.2. Let $U$ be a maximal unipotent subgroup of $\Gamma$, and (see 5.1) $N = N(\overline{U})$, $S = S(\overline{U})$.

16.2.1. LEMMA. 1) $\overline{U}$ is a maximal unipotent and $N$ a minimal parabolic Q-subgroup of $G$; 2) $N_{\mathbf{Z}}$ and $N \cap \Gamma$ are commensurable; 3) $S_{\mathbf{R}} / S \cap \Gamma$ is compact.

PROOF. By Theorem 6.4, $\overline{U}$ is a horospherical Q-subgroup of $G$ and $N$ a parabolic Q-subgroup of $G$. But $\operatorname{rank}_{\mathbf{Q}} G = 1$, and (by 5.3.1) $\overline{U} \neq \{e\}$, and we have 1). By Lemmas 7.4 and 7.2.2, there is a $\gamma \in \Gamma$ such that $\overline{U}$ and $\gamma \overline{U}\gamma^{-1}$ are opposite horospherical subgroups. Applying Lemma 9.6.2, we now obtain 2). Let $S^0$ be the connected component of the identity of $S$, and $X_{\mathbf{Q}}(S^0)$ the group of rational Q-characters of $S^0$. Let $T$ be an arbitrary Q-split torus in $S$. Since $\operatorname{rank}_{\mathbf{Q}} G = 1$ and $\overline{U}$ is a maximal unipotent Q-subgroup of $G$, using Lemma 4.5.4, we see that $\dim(T \cap S) = 0$. Therefore, $\operatorname{rank}_{\mathbf{Q}} S^0 = 0$, from which it follows that $X_{\mathbf{Q}}(S^0) = \{e\}$, and hence, ([7], 11.8), $S_{\mathbf{R}} / S_{\mathbf{Z}}$ is compact. From this and 2) we obtain 3).

16.3. LEMMA. 1) The number of conjugacy classes of maximal unipotent subgroups of $\Gamma$ is finite; 2) the group $\Gamma$ is finitely generated.

PROOF. In [16] (13.3) it is shown that if $\Gamma$ is a lattice in $G$ satisfying the conclusion of Lemma 16.1.1, then the assertion of 1) is true. At the same place ([16], (13.15)) it is shown that if $\Gamma$ is a lattice in $G$ satisfying the conclusion of Lemma 16.1.1 and Lemma 16.2.1, 3), then 2) is true.

16.4. Since Lemma 12.2.1 has already been proved, (by Lemma 11.3.7) we have:

16.4.1. LEMMA. For any maximal unipotent Q-subgroup U of G the subgroup  $U_{Z} \cap \Gamma$  is Zariski-dense in U.

16.4.2. REMARK. In fact, Lemma 16.4.1 is significantly simpler than Lemma 12.2.1 and can be deduced (see [29]) immediately from Theorem 9.7.1.

From Lemmas 16.3, 1) and 16.4.1 we deduce:

16.4.3. LEMMA. G has finitely many maximal unipotent Q-subgroups  $U_{1}, \ldots, U_{j}$  such that any maximal unipotent Q-subgroup U of G coincides with  $\gamma U_{i}\gamma^{-1}$  for some  $\gamma \in \Gamma$  and  $1 \leqslant i \leqslant j$ .

PROOF OF LEMMA 12.1.1. Let $U_1, \ldots, U_j$ be the subgroups in Lemma 16.4.3. For any $i, 1 \leqslant i \leqslant j$, the subgroup $(U_i)_\mathbf{Z} \cap \Gamma$ is dense in $U_i$ (see 16.4.1), and hence, (by 3.3.2 and 3.3.3) $(U_i)_\mathbf{Z} \cap \Gamma \supset U_{n(i)\mathbf{Z}}$. Let $B_1$ be the set of prime factors of $n(1) \cdot \ldots \cdot n(j)$. Since $\Gamma \subset G_{\mathbf{Q}}$ and (by 16.3) $\Gamma$ is finitely generated, there is a finite set $B_2$ of prime numbers such that $v_p(\gamma) > 0$ for any $\gamma \in \Gamma$ and $p \notin B_2$. Then it follows from Lemma 11.3.2 that $B = B_1 \cup B_2$ is the required set.

## § 17. Some unsolved problems in the theory of discrete subgroups

17.1. Using algebraic methods, Selberg proved in [39] that if $\Lambda$ is a discrete group of motions of a symmetric space $X$ of non-compact type with compact factor space $X / \Lambda$, then $\Lambda$ contains a subgroup of finite index, $\Lambda'$ acting on $X$ without fixed-points (that is, $\lambda x \neq x$ if $\lambda \in \Lambda'$, $x \in X'$$\lambda \neq e$). Can this theorem be proved geometrically? Is the analogous theorem true when $X$ is an arbitrary Riemannian manifold of non-positive curvature (not necessarily symmetric)?

17.2. It follows from the classical Gauss–Bonnet formula that if G is the group of motions of the Lobachevskii plane (that is,  $G = SL_{2}(\mathbf{R})/\pm E$ ), and  $\Gamma_{1}$  and  $\Gamma_{2}$  are lattices in G, then the ratio of the volumes  $v(G/\Gamma_{1})/v(G/\Gamma_{2})$  is rational. Is the analogous assertion true for an arbitrary semisimple group G? The answer to this question is not clear even in the simplest cases, when  $G = SL_{3}(\mathbf{R})$  and when G is the group of motions of 3-dimensional Lobachevskii space.

17.3. First we give a more general definition (see [35]) of an arithmetic subgroup than in the introduction. Let $H$ be a semisimple algebraic $\mathbf{R}$-group and let $H_{\mathbf{R}}$ be the direct product of a compact group $K$ and some group $H_{1}$. Let $\varphi$ denote the natural projection of $H_{\mathbf{R}}$ onto $H_{1}$. It is not difficult to see that $\varphi$ takes a discrete set in $H_{\mathbf{R}}$ to a discrete set in $H_{1}$. Hence, $\varphi(\Lambda)$, where $\Lambda$ is an arbitrary subgroup commensurable with $H_{\mathbf{Z}}$, is a discrete subgroup of $H_{1}$. Discrete subgroups that can be obtained by such a construction are also called arithmetic subgroups. Is a theorem analogous to the main theorem of the present paper true in case $\Gamma$ is a uniform lattice in $G_{\mathbf{R}}$, that is, is every uniform lattice in $G_{\mathbf{R}}$ an arithmetic subgroup ($G$ is assumed to satisfy the same conditions as in the main theorem)?

17.4. Let G be a semisimple algebraic R-group without compact factors and with trivial centre, of R-rank greater than 1, and let  $\Gamma$  be an irreducible lattice in G. Is every normal subgroup of  $\Gamma$  of finite index in  $\Gamma$ ? So far it is only known ([30]) that for “almost all” G the derived group of  $\Gamma$  is of finite index in  $\Gamma$ .

## Appendix. Properties of root decompositions

We give a short proof of Lemma 4.5.1. We keep to the notation of §4.5. Let $(u, v)$ be an invariant scalar product on $\mathfrak{G}$, given by the Killing form, $\mathfrak{G}_0$ the orthogonal complement to $\mathfrak{S}$ in $\mathfrak{C}$, $x \in (\mathfrak{G}_{\alpha})_h$, $x \neq 0$, $h$ an element of $\mathfrak{S}$, such that $\alpha(s) = 2(h, s)/(h, h)$ for all $s \in \mathfrak{S}$. Since $\mathfrak{S}$ is an ideal in $\mathfrak{C}$, $\mathfrak{G}_0$ is an ideal in $\mathfrak{C}$. Let $C_0$ be the subgroup corresponding to $\mathfrak{G}_0$. Let $A = \{g \in C_0; (\operatorname{Ad} g)_x$ is collinear with $x\}$, $A' = \{g \in C_0; (\operatorname{Ad} g)x = x\}$. Since $S$ is a maximal $k$-split torus, $\mathfrak{S} \cap \mathfrak{G}_0 = \{0\}$ and the group $C_0$ is anisotropic over $k$. Therefore, the connected component $A^0$ of $A$ coincides with $A'$ (since otherwise $A^0$ would have a non-trivial rational character

defined over $k$, which contradicts the fact that $C_0$ is $k$-anisotropic). Hence (1) $[\mathfrak{G}_0, x] \nmid x$.

From standard properties of the Killing form on a semisimple Lie algebra it follows that the equality $[x, y] = h$, $y \in \mathfrak{G}_{-\alpha}$, is equivalent to the following two conditions: $2(x, y) = (h, h)$, $([x, y], \mathfrak{G}_0) = ([\mathfrak{G}_0, x], y) = 0$. Hence, using (1), we find that there exists an $\omega(x) = y \in (\mathfrak{G}_{-\alpha})_k$, for which $[x, y] = h \in \mathfrak{S}$. The elements $x, y$ and $h$ form a basis of a canonical three-dimensional simple split subalgebra $\mathfrak{A}$.

LEMMA. In $\mathfrak{G}_{-\alpha}$ there is no non-zero element commuting with $x$.

PROOF. Let z be such an element. Then z is the highest weight vector of some irreducible representation of A contained in its adjoint representation in G. Hence,  $[h, z] = nz$ , where n is a non-negative integer. On the other hand,  $[h, z] = -\alpha(h)z = -2z$ . This contradiction proves the lemma.

From the lemma and standard properties of the Killing form we deduce the uniqueness of $y$. Thus, part 1) is proved. From the invariance of the scalar product it follows that the annihilator of the space $[\mathfrak{C}, x]$ in $\mathfrak{G}_{-\alpha}$ consists precisely of the $z \in \mathfrak{G}_{-\alpha}$ for which $([x, z], \mathfrak{C}) = 0$. Hence and from the lemma proved above we see that $[\mathfrak{C}, x] = \mathfrak{G}_{\alpha}$. Let $x', x''$ be nonzero elements of $(\mathfrak{G}_{\alpha})_k$. Since $[\mathfrak{C}, x'] = [\mathfrak{C}, x''] = \mathfrak{G}_{\alpha}$, the orbits of $x'$ and $x''$ under the action of $C(S)$ are Zariski-open in $\mathfrak{G}_{\alpha}$ and hence, have a non-empty intersection; but then they simply coincide. Thus, part 2) is proved.

We now prove part 3). By 2) it suffices to show that $[\mathfrak{G}_{\alpha},\mathfrak{G}_{\beta}]\neq 0$. Suppose that $[\mathfrak{G}_{\alpha},\mathfrak{G}_{\beta}] = 0$. Then any non-zero element of the space $\mathfrak{G}_{\beta}$ is a highest vector of some irreducible representation of the three-dimensional algebra $\mathfrak{A}$ defined earlier, with highest weight $\beta (h)\geqslant 0$. From the relations

$([\mathfrak{G}_{\alpha}, \mathfrak{G}_{-\alpha - \beta}], \mathfrak{G}_{\beta}) = ([\mathfrak{G}_{\alpha}, \mathfrak{G}_{\beta}], \mathfrak{G}_{-\alpha - \beta}) = 0$ it follows that $[\mathfrak{G}_{\alpha}, \mathfrak{G}_{-\alpha - \beta}] = 0$. As above, we find that $(- \alpha - \beta)(h) = 2 - \beta(h) \geqslant 0$. This is obviously false. Therefore, $[\mathfrak{G}_{\alpha}, \mathfrak{G}_{\beta}] = \mathfrak{G}_{\alpha + \beta}$. Since (by 2)) (Ad $C(S))x \supset (\mathfrak{G}_{\alpha})_h$ from $[\mathfrak{G}_{\alpha}, \mathfrak{G}_{\beta}] = \mathfrak{G}_{\alpha + \beta}$ it follows that $[x, \mathfrak{G}_{\beta}] \neq 0$. The proof of Lemma 4.5.1 is now complete.

## References

[1] G. D. Mostow, Factor spaces of solvable groups, Ann. of Math. (2) 60 (1954), 1–27. MR 15–853.

[2] G. D. Mostow, Homogeneous spaces with finite invariant measure, Ann. of Math. (2) 75 (1962), 17–37. MR 26 # 2546.

[3] A. Borel, Density properties for certain subgroups of semisimple groups without compact components, Ann. of Math. (2) 72 (1960), 179–188. MR 23 # A964.

[4] A. Borel, Linear algebraic groups, W. A. Benjamin, New York 1969. MR 40 #4273. Translation: Lineinye algebraicheskie gruppy, Izdat. Mir, Moscow 1972.

[5] G. A. Margulis, Discrete subgroups of real semisimple Lie groups, Mat. Sb. 80 (1969), 600–615. MR 40 # 7385.
= Math. USSR-Sb. 9 (1969), 555–568.

[6] M. S. Raghunathan, Cohomology of arithmetic subgroups of algebraic groups. I, II. Ann. of Math. (2) 86 (1967), 409–424; 87 (1968), 279–304. MR 37 # 2898.

[7] A. Borel and Harish-Chandra, Arithmetic subgroups of algebraic groups, Ann. of Math. (2) 75 (1962), 485–535. MR 26 #5081.
= Matematika 8: 2 (1964); 19–71.

[8] B. Yu. Veisfeiler, On a class of unipotent subgroups of semisimple algebraic groups, Uspekhi Mat. Nauk 21:2 (1966), 222–223. MR 33 # 2634.

[9] A. Borel and J. Tits, Éléments unipotents et sous-groupes paraboliques de groupes réductifs. I. Invent. Math. 12 (1971), 95–104. MR 45 #3419.
= Matematika 16:3 (1972), 3–12.

[10] A. Borel and J. Tits, Groupes réductifs, Publ. Math. Inst. Hautes Etudes Sci. 27 (1965), 55–150. MR 34 # 7527.
= Matematika 11:1 (1967), 43–111; 11:2, 3–31.

[11] D. A. Kazhdan and G. A. Margulis, A proof of Selberg's conjecture, Mat. Sb. 75 (1968), 163–168. MR 36 #6535.
= Math. USSR-Sb. 4 (1968), 147–152.
(See also A. Borel, Sous-groupes discrets de groupes semisimples (d'après D. A. Kajdan et G. A. Margoulis), Sém. Bourbaki, exposé no. 358, juin 1969; Lecture Notes in Math. No. 179. Springer-Verlag, Berlin–Heidelberg–New York, 1971.)

[12] H. Garland and M. S. Raghunathan, Fundamental domains for lattices in (R-)rank 1 semisimple groups, Ann. of Math. (2) 92 (1970), 279–326. MR 42 # 1943.

[13] M. Hall, The theory of groups, Macmillan, New York 1959. MR 21 # 1996. Translation: Teoriya grupp, Izdat. Inost. Lit., Moscow 1962.

[14] G. A. Margulis, On the action of unipotent groups in the space of lattices, Mat. Sb. 86 (1971), 552–556. MR 45 # 445.
= Math. USSR-Sb. 15 (1971), 549–554.

[15] A. Selberg, Recent developments in the theory of discontinuous groups of motions of symmetric spaces, Proc. 15th Scandinavian Congress (Oslo 1968), Lecture Notes in Math. No. 118, 99–120, Springer-Verlag, Berlin--Heidelberg-New York 1970. MR 41 #8595.

[16] M. S. Raghunathan, Discrete subgroups of Lie groups, Springer-Verlag, Berlin–Heidelberg–New York 1972.

[17] H. Zassenhaus, Beweis eines Satzes über diskrete Gruppen, Abh. Math. Sem. Hamburg Univ. 19 (1938), 289–312.

[18] N. Bourbaki, Groupes et algèbres de Lie, Chap. IV–V–VI, Hermann, Paris 1968. MR 39 #1590.
Translation: Gruppy Li i algebry Li, Izdat. Mir, Moscow 1972.

[19] L. N. Vasershtein, Subgroups of finite index of a spinor group of rank greater than or equal to 2, Mat. Sb. 75 (1968), 178–184. MR 37 # 1475.
= Math. USSR-Sb. 4 (1968), 161–166.

[20] C. Chevalley, Séminaire sur la classification des groupes de Lie algébriques (1956/58), 2 vol., Secrétariat mathématique, Paris, 1958 (notes polycopiées). MR 21 # 5696.

[21] A. Borel, Ensembles fondamentaux pour les groupes arithmétiques et formes automorphes, Faculté des sciences de Paris, cours miméographié, 1967.
= Matematika 12:4 (1968), 80–103; 12:5, 34–91, and 12:6, 3–30.
(This is a preliminary version of A. Borel, Introduction aux groupes arithmétiques, Hermann, Paris 1969. MR 39 #5577.)

[22] M. Kneser, Strong approximation. Proc. Symp. Pure Math. 9 (1966), 187–196, Amer. Math. Soc. Providence, R. I. MR 35 #4225.

[23] J.-P. Serre, Faisceaux algébriques cohérents, Ann. of Math. (2) 61 (1955), 197–278. MR 16–953.
= Kogerentnye algebraicheskie puchki. In the coll. “Rassloennye prostranstva i ikh prilozheniya” (Fibre spaces and their applications), 372–450. Izdat. Inost. Lit., Moscow 1958.

[24] V. P. Platonov, The problem of strong approximation and the Kneser–Tits conjecture for algebraic groups, Izv. Akad. Nauk SSSR Ser. Mat. 33 (1969), 1211–1219.
MR 41 # 3485.
= Math. USSR-Izv. 3 (1969), 1139–1147.

[25] V. P. Platonov, Addendum to the paper: “The problem of strong approximation and the Kneser–Tits conjecture for algebraic groups”, Izv. Akad. Nauk SSSR Ser. Mat. 34 (1970), 775–777. MR 42 # 7670.
= Math. USSR-Izv. 4 (1970), 784–786.

[26] J. Tits, Classification of algebraic semisimple groups, Proc. Symp. Pure Math. 9 (1966), 33–62, Amer. Math. Soc., Providence, R.I. MR 37 #309.
= Matematika 12:2 (1968), 110–143.

[27] A. Weil, Adèles and algebraic groups, Lecture notes, The Institute for Advanced Study, Princeton, N.J. 1961.
= Matematika 8: 4 (1964), 3–74.

[28] I. I. Pyatetskii-Shapiro, Discrete subgroups of Lie groups, Trudy Moskov. Mat. Obshch. 18 (1968), 3–18. MR 39 # 2908.
= Trans. Moscow Math. Soc. 18 (1968), 1–18.

[29] G. A. Margulis, Non-uniform latticee in semisimple algebraic groups, “Lie groups and their representations”, Summer school Bolyai Janos Math. Soc., Budapest.

[30] D. A. Kazhdan, On the connection of the dual space of a group with the structure of its closed subgroups, Funktsional. Anal. i Prilozhen. 1:1 (1967), 71–74. MR 35 # 288. = Functional Anal. Appl. 1 (1967), 63–65.

[31] S. Helgason, Differential geometry and symmetric spaces, Academic Press, New York–London 1962. MR 26 # 2986.
Translation: Differentsial'naya geometriya i simmetricheskie prostranstva, Izdat. Mir, Moscow 1964.

[32] A. Selberg, Discontinuous groups and harmonic analysis, Proc. Internat. Congress Mathematicians, Stockholm 1962, 177–189. MR 31 #372.

[33] E. B. Vinberg, Discrete groups generated by reflections in Lobachevskii spaces, Mat. Sb. 72 (1967), 471–488. MR 34 #7667.
= Math. USSR-Sb. 1 (1967), 429–444.

[34] V. S. Makarov, On a class of discrete groups of Lobachevskii space having an infinite fundamental domain of finite measure Dokl. Akad. Nauk SSSR 167 (1966), 30–33. MR 34 #244.
= Soviet Math. Dokl. 7 (1966), 328–331.

[35] I. I. Pyatetskii-Shapiro, Automorphic functions and arithmetic groups, Proc. Internat. Congress Mathematicians, Moscow 1966, 232–247; Izdat. Mir, Moscow 1968. MR 38 # 5719.
= Amer. Math. Soc. Transl. (2) 70 (1968), 185–201. (NB: The translation is of a preliminary version.)

[36] G. A. Margulis, On the problem of the arithmeticity of discrete groups, Dokl. Akad. Nauk SSSR 187 (1969), 518–520. MR 45 # 2088.
= Soviet Math. Dokl. 10 (1969), 900–902.

[37] L. Auslander, On radicals of discrete subgroups of Lie groups, Amer. J. Math. 85 (1963), 145–150. MR 27 # 2583.

[38] H. C. Wang, On the deformations of lattices in Lie groups, Amer. J. Math. 85 (1963), 189–212. MR 27 # 2582.

[39] A. Selberg, On discontinuous groups in higher-dimensional symmetric spaces. Contributions to function theory (Internat. Colloq. Function Theory, Bombay 1960), 147–164. Tata Institute of Fundamental Research, Bombay 1960. MR 24 #A188. = Matematika 6:3 (1963), 3–15.

[40] A. Weil, On discrete subgroups of Lie groups. I, II. Ann. of Math. (2) 72 (1960), 369–384; MR 25# 1241; 75 (1962) 570–602; MR 25 # 1242.
= Matematika 7:1 (1963), 3–41.

[41] C. Hermite, Oeuvres complètes. I. Gauthier-Villars, Paris 1905.

[42] R. Godement, Domaines fondamentaux des groupes arithmétiques. Sém. Bourbaki, exposé 257, Paris 1962–1963.

[43] G. Springer, Introduction to Riemann surfaces, Addison-Wesley, Reading, Mass., 1957. MR 19–1169.
Translation: Vvedenie v teoriyu rimanovykh poverkhnostei, Izdat. Inost. Lit., Moscow 1960.

[44] G. A. Margulis, The isometry of closed manifolds of constant negative curvature with the same fundamental group, Dokl. Akad. Nauk SSSR, 192 (1970), 736–737.
MR 42 # 1012.
= Soviet Math. Dokl. 11 (1970), 722–723.

[46] G. A. Margulis, Arithmeticity of non-uniform lattices, Funktsional. Anal. i Prilozhen.
7:3 (1973), 88–89. MR 48 # 8651.
= Functional Anal. Appl. 7 (1973), 245–246.

[47] C. Delaroche and A. Kirillov, Sur les relations entre l'espace dual d'un groupe et la structure de ses sous-groupes fermés (d'après D. A. Kajdan), Sém. Bourbaki, exposé 343, June 1968.

[48] G. D. Mostow, Strong rigidity of locally symmetric spaces, Ann. of Math. Studies No. 78, Princeton, N.J., 1973.

[48a] G. D. Mostow, The rigidity of locally symmetric spaces, Proc. Congrès Internat. Math., Nice 1970, vol. 2, 187–197; Gauthiers-Villars, Paris 1971.

[49] G. Prasad, Strong rigidity of Q-rank 1 lattices, Invent. Math. 21 (1973), 255–286.