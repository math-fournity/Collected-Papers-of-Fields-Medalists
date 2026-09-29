# Pacific Journal of Mathematics

CHAPTER V, FROM SOLVABILITY OF GROUPS OF ODD ORDER, PACIFIC J. MATH., VOL. 13, NO. 3 (1963)

WALTER FEIT AND JOHN GRIGGS THOMPSON

May 1963

# CHAPTER V

## 27. Statement of the Result Proved in Chapter V

The following result is proved in this chapter.

THEOREM 27.1. Let $\mathfrak{G}$ be a minimal simple group of odd order. Then $\mathfrak{G}$ satisfies the following conditions:

(i) $p$ and $q$ are odd primes with $p > q$. $\mathfrak{G}$ contains elementary abelian subgroups $\mathfrak{P}$ and $\mathfrak{Q}$ with $|\mathfrak{P}| = p^q$, $|\mathfrak{Q}| = q^p$. $\mathfrak{P}$ and $\mathfrak{Q}$ are T.I. sets in $\mathfrak{G}$.

(ii) $N(\mathfrak{P}) = \mathfrak{P}\cup \mathfrak{Q}^*$, where $\mathfrak{P}\cup$ and $\cup \mathfrak{Q}^*$ are Frobenius groups with Frobenius kernels $\mathfrak{P},\mathfrak{U}$ respectively. $|\mathfrak{Q}^{*}| = q, |\mathfrak{U}| = (p^{q} - 1) / (p - 1),$$\mathfrak{Q}^{*}\subseteq \mathfrak{Q}$ and $((p^{q} - 1) / (p - 1),p - 1) = 1.$

(iii) If $\mathfrak{P}^* = C_{\mathfrak{P}}(\mathfrak{D}^*)$, then $|\mathfrak{P}^*| = p$ and $\mathfrak{P}^*\mathfrak{D}^*$ is a self-normalizing cyclic subgroup of $\mathfrak{G}$. Furthermore, $C(\mathfrak{P}^*) = \mathfrak{P}\mathfrak{D}^*$, $C(\mathfrak{D}^*) = \mathfrak{Q}\mathfrak{P}^*$, and $\mathfrak{P}^* \subseteq N(\mathfrak{D})$.

(iv) $C(\mathfrak{U})$ is a cyclic group which is a T.I. set in $\mathfrak{G}$. Furthermore, $\mathfrak{Q}^* \subseteq N(\mathfrak{U}) = N(C(\mathfrak{U}))$, $N(\mathfrak{U}) / C(\mathfrak{U})$ is a cyclic group of order pq and $N(\mathfrak{U})$ is a Frobenius group with Frobenius kernel $C(\mathfrak{U})$.

In this chapter we take the results stated in Section 14 as our starting point. The notation introduced in that section is also used. There is no reference to any result in Chapter IV which is not contained in Section 14. The theory of group characters plays an essential role in the proof of Theorem 27.1. In particular we use the material contained in Chapter III.

Sections 28–31 consist of technical results concerning the characters of various subgroups of G. In Section 32 the troublesome groups of type V are eliminated. In Section 33 it is shown that groups of type I are Frobenius groups. By making use of the main theorem of [10] it is then easy to show that the first possibility in Theorem 14.1 cannot occur. The rest of the chapter consists of a detailed study of the groups S and T until in Section 36 we are able to supply a proof of Theorem 27.1.

## 28. Characters of Subgroups of Type I

Hypothesis 28.1.

(i) $\mathfrak{X}$ is of Frobenius type with Frobenius kernel $\mathfrak{S}$ and complement $\mathfrak{E}$.

(ii) $\mathfrak{E} = \mathfrak{A}\mathfrak{B}$, where $\mathfrak{A}$ is abelian, $\mathfrak{B}$ is cyclic, and $(|\mathfrak{A}|, |\mathfrak{B}|) = 1$.

(iii) $\mathfrak{G}_0$ is a subgroup of $\mathfrak{G}$ with the same exponent as $\mathfrak{G}$ such that $\mathfrak{G}_0\mathfrak{H}$ is a Frobenius group with Frobenius kernel $\mathfrak{H}$.

LEMMA 28.1. Under Hypothesis 28.1, $\mathfrak{X}$ has an irreducible character of degree $|\mathfrak{G}_0|$ which does not have $\mathfrak{S}$ in its kernel.

Proof. If $\mathfrak{A}$ is cyclic, then $\mathfrak{X}$ is a Frobenius group and the lemma is immediate. We may assume that $\mathfrak{A}$ is non cyclic.

Let $\mathfrak{H}_1 / D(\mathfrak{H})$ be a chief factor of $\mathfrak{A}\mathfrak{H}$ with $\mathfrak{H}_1\subseteq \mathfrak{H}$. Let $\mathfrak{A}_1 = C_{\mathfrak{A}}(\mathfrak{H}_1 / D(\mathfrak{H}))$. Then $\mathfrak{A} / \mathfrak{A}_1$ is cyclic. Since $\mathfrak{X}$ is of Frobenius type, the exponent of $\mathfrak{A} / \mathfrak{A}_1$ is the exponent of $\mathfrak{A}$. Hence, $|\mathfrak{E}:\mathfrak{A}_1| = |\mathfrak{E}_0|$. Let $\mathfrak{A}_2$ be the normal closure of $\mathfrak{A}_1$ in $\mathfrak{E}$. Then $\mathfrak{A}_2$ is abelian. Let $\mu$ be a non principal linear character of $\mathfrak{H}_1 / D(\mathfrak{H})$. Then $\mathfrak{J}(\mu) = \mathfrak{H}\mathfrak{A}_1$, so Lemma 4.5 completes the proof.

LEMMA 28.2. Suppose $\mathfrak{L}$ is of type I, and $\mathfrak{L} = \mathfrak{X}$ satisfies Hypothesis 28.1. Suppose further that $Z(\mathfrak{G})$ contains an element $E$ such that $C_{\mathfrak{H}}(E) \not\subseteq \mathfrak{H}'$ and $C_{\mathfrak{H}}(E) \neq \mathfrak{H}$. Then the set $\mathscr{L}$ of irreducible characters of $\mathfrak{L}$ which do not have $\mathfrak{H}$ in their kernel is coherent.

Proof. By Lemmas 28.1 and 4.5, it follows that Hypothesis 11.1 and (11.4) are satisfied if we take $\mathfrak{H}_0 = 1$, $\mathfrak{R} = \mathfrak{L}$, $d = |\mathfrak{E}_0|$ and let $\mathcal{L}$ play the role of $\mathcal{S}$.

Since $E$ is in the center of $\mathfrak{G}$, it follows that $\mathfrak{H}'C_{\mathfrak{H}}(E) \triangleleft \mathfrak{L}$. Thus, by assumption, $\mathfrak{H}/\mathfrak{H}'$ is not a chief factor of $\mathfrak{L}$. Therefore,

$$
\mathfrak {H}: \mathfrak {H} ^ {\prime} | > 4 | \mathfrak {G} _ {0} | ^ {2} + 1.\tag{28.1}
$$

Let $\mathcal{S}(\mathfrak{H}') = \{\lambda_{i_s}|s = 1,\dots ,n_i;i = 1,\dots ,k\}$, where the notation is chosen so that $\lambda_{i_s}(1) = \lambda_{jt}(1)$ if and only if $i = j$, and where $\lambda_{11}(1) < \dots < \lambda_{k1}(1)$. By (28.1) we get that (11.5) holds with $\mathfrak{H}_1 = \mathfrak{H}'$ and by Theorem 11.1 the lemma will follow as soon as it is shown that $\mathcal{S}(\mathfrak{H}')$ is coherent.

Set $\ell_{i} = \lambda_{ii}(1)/d$ for $1 \leq i \leq k$. Then each $\ell_{i}$ is an integer and $1 = \ell_{1} < \cdots < \ell_{k}$. By Theorem 10.1, the coherence of $\mathcal{S}(\mathfrak{S}')$ will follow once inequality (10.2) is established. Suppose (10.2) does not hold. Then for some $m$ with $1 < m \leq k$,

$$
\sum_ {i = 1} ^ {m - 1} \ell_ {i} ^ {2} n _ {i} \leq 2 / _ {m}.\tag{28.2}
$$

Every character in $\mathcal{S}(\mathfrak{H}')$ is a constituent of a character induced by a linear character of $\mathfrak{H}$. Therefore,

$$
\angle_ {k} \leq | \mathfrak {F}: \mathfrak {F} _ {0} |.\tag{28.3}
$$

Let $\bar{\mathfrak{H}} = \mathfrak{H} / \mathfrak{H}'$ and let $\bar{\mathfrak{H}}_1 = C_{\bar{\mathfrak{H}}}(\boldsymbol {E})$, $\bar{\mathfrak{H}}_2 = [\bar{\mathfrak{H}},\boldsymbol {E}]$. Thus, $\bar{\mathfrak{H}} = \bar{\mathfrak{H}}_1\times \bar{\mathfrak{H}}_2$

and $\bar{\mathfrak{H}}_i \neq 1$, $i = 1, 2$. If $\mathfrak{H}_i$ is the inverse image of $\bar{\mathfrak{H}}_i$ in $\mathfrak{H}$, then $\mathfrak{E}\mathfrak{H}_i$ is of Frobenius type and satisfies Hypothesis 28.1. Two applications of Lemma 28.1 imply that $n_1 \geq 4|\mathfrak{G} : \mathfrak{G}_0|$. Hence, (28.2) does not hold for any $m$, $1 < m \leq k$. The proof is complete.

## 29. Characters of Subgroups of Type III and IV

The following notation will be used.

$\mathfrak{S} = \mathfrak{S}'\mathfrak{Q}^*$ is a subgroup of type II, III, or IV. $\mathfrak{Q}^*$ plays the role of $\mathfrak{W}_1$ in the definition of subgroups of type II, III, and IV given in Section 14. $\mathfrak{S}, \mathfrak{U}$, and $\mathfrak{W}_2$ have the same meaning as in these definitions. $\mathfrak{T} = \mathfrak{T}'\mathfrak{W}_2$ is a subgroup of type II, III, IV, or V whose existence follows from Theorem 14.1 (ii) (b), (e).

Let $\pi(\mathfrak{H}) = \{p_1, \cdots, p_t\}$ and for $1 \leq i \leq t$, let $\mathfrak{P}_i$ be the $S_{p_i}$-subgroup of $\mathfrak{H}$. Define

$$
\mathfrak {C} _ {i} = \mathfrak {U} \cap C (\mathfrak {P} _ {i}), \quad 1 \leq i \leq t,
$$

$$
\mathfrak {C} = \bigcap_ {i = 1} ^ {t} \mathfrak {C} _ {i}.
$$

Let $|\mathfrak{Q}| = h$, $|\mathfrak{U}| = u$, $|\mathfrak{Q}^*| = q$, $|\mathfrak{C}_i| = c_i$, $1 \leq i \leq t$, and $|\mathfrak{C}| = c$. By definition, $q$ is a prime.

$S_{0}$ is the set of characters of $\mathfrak{S}$ which are induced by nonprincipal irreducible characters of $\mathfrak{S}'/\mathfrak{H}$.

$\mathcal{S}$ is the set of characters of $\mathfrak{S}$ which are induced by irreducible characters of $\mathfrak{S}'$ that do not have $\mathfrak{H}$ in their kernel.

The purpose of this section is to prove the following result.

THEOREM 29.1.

(i) If $\mathfrak{S}$ is of type III then $\mathcal{S} \cup \mathcal{S}_0$ is coherent except possibly if $|\mathfrak{H}| = p^q$ for some prime $p$ and $\mathfrak{C} = 1$.

(ii) If $\mathfrak{S}$ is of type IV, then $\mathcal{S} \cup \mathcal{S}_0$ is coherent except possibly if $|\mathfrak{H}| = p^q$ for some prime $p$, $\mathfrak{C} = \mathfrak{U}'$ and $\mathcal{S}_0$ is not coherent.

Hypothesis 29.1.

$\mathfrak{S}$ is a subgroup of type III or IV.

Throughout this section, Hypothesis 29.1 will be assumed. Thus, by Theorem 14.1 (ii) (d), $\mathfrak{T}$ is of type II. Consequently, $\mathfrak{W}_2$ has prime order $p$. Let $p = p_1$, $\mathfrak{P} = \mathfrak{P}_1$, and $\mathfrak{W}_2 = \mathfrak{P}^*$. Thus, by 3.16 (i), $\mathfrak{U} \subseteq C(\mathfrak{P}_i)$ for $2 \leq i \leq t$. Since $\mathfrak{U} \not\subseteq C(\mathfrak{G})$, this yields that $\mathfrak{U} \not\subseteq C(\mathfrak{P})$. As $\mathfrak{U}$ does not act trivially on $\mathfrak{P}/D(\mathfrak{P})$, Lemma 4.6 (i) implies that $C_{\mathfrak{U}}(\mathfrak{P}^*) = \mathfrak{C}_1 \subset \mathfrak{U}$.

For any subgroup $\mathfrak{H}_1$ of $\mathfrak{H}\mathfrak{C}$, let $\mathcal{S}(\mathfrak{H}_1)$ denote the set of characters in $\mathcal{S}_0 \cup \mathcal{S}$ which have the same degree and the same weight as some character in $\mathcal{S}_0 \cup \mathcal{S}$ that has $\mathfrak{H}_1$ in it kernel.

LEMMA 29.1. Hypothesis 11.1 is satisfied if $\mathcal{S}$ in that hypothesis is replaced by $\mathcal{S}_0\cup\mathcal{S}$, $\mathfrak{H}$ is replaced by $\mathfrak{H}\mathfrak{C}$, $\mathfrak{H}_0$ is taken as $\langle1\rangle$, $\mathfrak{L}$ is replaced by $\mathfrak{S}$, $\widehat{\mathfrak{L}}$ and $\mathfrak{R}$ are replaced by $\mathfrak{S}'$, and $d=1$.

Proof. By Theorem 14.2, Condition (i) is satisfied. Condition (ii) follows from the fact that $\mathfrak{S}$ is a three step group. Condition (iii) is immediate and Condition (vi) is simply definition (consistent with the present definition). Since $\mathfrak{U}\mathfrak{D}^*$ is a Frobenius group, $\mathcal{S}_0$ contains an irreducible character of degree $q$. Hence, Condition (iv) is satisfied. The group $\mathfrak{S}$ satisfies Hypothesis 13.2. Hence, by Theorem 14.2, Hypothesis 13.3 is satisfied with $\mathfrak{L} = \mathfrak{S}$, $\mathfrak{X} = \mathfrak{G}$, and $\hat{\mathfrak{L}} = \mathfrak{R} = \mathfrak{S}'$, and with $\mathcal{S}$ replaced by $\mathcal{S}_0 \cup \mathcal{S}$. By Lemmas 13.7, 13.9, and 13.10, Condition (v) of Hypothesis 11.1 is satisfied. The proof is complete.

LEMMA 29.2. If $\mathcal{S}((\mathfrak{H}\mathfrak{C})')$ is coherent, then $\mathcal{S}_0 \cup \mathcal{S}$ is coherent.

Proof. As $\mathfrak{U} \not\subseteq C(\mathfrak{P})$, $\mathfrak{U}$ does not act trivially on $\mathfrak{P}/D(\mathfrak{P})$. Since $\mathfrak{U}\mathfrak{Q}^*$ is a Frobenius group, 3.16 (iii) yields that $|\mathfrak{P}: D(\mathfrak{P})| \geq p^q$. As either $p \geq 3$ and $q \geq 5$ or $p \geq 5$ and $q \geq 3$, (5.9) yields that

$$
\mathfrak {H C}: (\mathfrak {H C}) ^ {\prime} \mid \geq | \mathfrak {P}: D (\mathfrak {P}) | \geq p ^ {q} > 4 q ^ {2} + 1 = 4 | \mathfrak {S}: \mathfrak {S} ^ {\prime} | ^ {2} + 1.
$$

Hence, (11.5) is satisfied with $\mathfrak{D}_1 = (\mathfrak{D}\mathfrak{C})$. By Lemma 29.1, Theorem 11.1 may be applied. This implies the required result.

LEMMA 29.3. If $\mathcal{S}((\mathfrak{H}\mathfrak{C})')$ is not coherent, then $\mathfrak{S}'' = \mathfrak{H}\mathfrak{C}$.

Proof. Let $b = |\mathfrak{H}\mathfrak{C}:\mathfrak{S}''|$. We have $\mathfrak{P}^* \subseteq \mathfrak{S}'$, as $\mathfrak{P}^* \subseteq \mathfrak{S}'$ and $\mathfrak{Q}^*$ centralizes $\mathfrak{P}^*$. Hence, $\mathfrak{S}/\mathfrak{S}''$ is a Frobenius group. Let $d_1 < \cdots < d_k$ be all the degrees of characters in $\mathcal{S}((\mathfrak{H}\mathfrak{C})')$ and let $\ell_m = d_m/q$ for $1 \leq m \leq k$. Then for each $m$, $\ell_m$ is an integer and $\ell_1 = 1$. Every character of $\mathfrak{S}/\mathfrak{S}''$ is a constituent of a character induced by a linear character of $\mathfrak{H}\mathfrak{C}$. Thus, $\ell_m \leq u/c$ for $1 \leq m \leq k$. There are at least

$$
\frac {\left(\frac {u}{c} b - 1\right)}{q}
$$

irreducible characters of degree $q$ in $\mathcal{S}((\mathfrak{H}\mathfrak{C})')$. Thus, if $\mathcal{S}((\mathfrak{H}\mathfrak{C})')$ is not coherent, inequality (10.2) must be violated for some $m$. In particular, this implies that

$$
\frac {\left(\frac {u}{c} b - 1\right)}{q} \leq 2 / _ {m} \leq 2 \frac {u}{c}
$$

Therefore, $b - (c/u) \leq 2q$, so $b < 2q + 1$, since $c < u$. As $\mathfrak{H}\mathfrak{C}/\mathfrak{S}''$ is a normal subgroup of the Frobenius group $\mathfrak{S}/\mathfrak{S}''$, we have $b \equiv 1 \pmod{q}$. Since $b$ and $q$ are both odd, this implies that $b = 1$ as required.

LEMMA 29.4. If $\mathcal{S}((\mathfrak{H}\mathfrak{C})')$ is not coherent, then $\mathfrak{H} = \mathfrak{P}$, $\mathfrak{P}' = D(\mathfrak{P})$, $|\mathfrak{P}:\mathfrak{P}'| = p^q$, $\mathfrak{P}^* \cap D(\mathfrak{P}) = 1$ and $\mathfrak{C} = \mathfrak{U}'$.

Proof. By Lemma 29.3, $\mathfrak{S}'' = \mathfrak{H}\mathfrak{C}$. If $2 \leq i \leq t$, then $\mathfrak{U}\mathfrak{H} \subseteq \mathfrak{P}_i C(\mathfrak{P}_i)$, so that $p_i | |\mathfrak{S}' : \mathfrak{S}''|$. Hence, $t = 1$ and $\mathfrak{H} = \mathfrak{P}$. $\mathfrak{C} = \mathfrak{U}'$ follows directly from the fact that $\mathfrak{H}\mathfrak{C} = \mathfrak{S}'' \subseteq \mathfrak{H}\mathfrak{U}'$. If $|\mathfrak{P} : D(\mathfrak{P})| > p^q$, then since $C_{\mathfrak{P}}(\mathfrak{Q}^*) = \mathfrak{P}^*$ is cyclic, Lemma 4.6 (i) implies that some non identity element of $\mathfrak{P}/D(\mathfrak{P})$ is in the center of $\mathfrak{P}\mathfrak{U}/D(\mathfrak{P})$. Thus, $p$ divides $|\mathfrak{U}\mathfrak{H} : \mathfrak{S}''|$ which is not the case. Since $\mathfrak{U}$ does not act trivially on $\mathfrak{P}/D(\mathfrak{P})$, 3.16 (iii) now implies that $|\mathfrak{P} : D(\mathfrak{P})| = p^q$. Since $\mathfrak{P}^*$ has prime order and lies outside $D(\mathfrak{P})$, we get that $D(\mathfrak{P})\mathfrak{U}\mathfrak{Q}^*$ is a Frobenius group. Hence, by 3.16 (i), $D(\mathfrak{P})\mathfrak{U}$ is nilpotent. Consequently, $D(\mathfrak{P})/\mathfrak{P}'$ is in the center of $\mathfrak{P}\mathfrak{U}/\mathfrak{P}'$. As the fixed points of $\mathfrak{U}$ on $\mathfrak{P}/\mathfrak{P}'$ are a direct factor of $\mathfrak{P}/\mathfrak{P}'$, and since $\mathfrak{U}$ has no fixed points on $\mathfrak{P}/D(\mathfrak{P})$, we have $\mathfrak{P}' = D(\mathfrak{P})$. The lemma is proved.

LEMMA 29.5. If $\mathcal{S}((\mathfrak{H}\mathfrak{C})')$ is not coherent then $\mathfrak{P}$ is an elementary abelian $p$-group of order $p^q$.

Proof. In view of Lemma 29.4 it suffices to show that $\mathfrak{P}' = 1$. By 3.16 (i), $\mathfrak{U} \subseteq C(\mathfrak{P}')$. Thus, if $\mathfrak{P}' \neq 1$, there exists a subgroup $\mathfrak{P}_0$ of $\mathfrak{P}'$ such that $\mathfrak{P}_0 \triangleleft \mathfrak{P}\mathfrak{U}$ and $|\mathfrak{P}' : \mathfrak{P}_0| = p$. If $\mathfrak{U}$ acts irreducibly on $\mathfrak{P}/\mathfrak{P}'$, then $\mathfrak{P}'/\mathfrak{P}_0 = Z(\mathfrak{P}/\mathfrak{P}_0)$. Hence, $\mathfrak{P}/\mathfrak{P}_0$ is an extra special $p$-group and $|\mathfrak{P} : \mathfrak{P}'| = p^{2b}$ for some integer $b$ contrary to Lemma 29.4.

Suppose that $\mathfrak{U}$ acts reducibly on $\mathfrak{P}/\mathfrak{P}'$. Since the irreducible constituents of this representation are conjugate under the action of $\mathfrak{Q}^*$, all constituents have the same dimension. As $|\mathfrak{P}:\mathfrak{P}'| = p^q$ and $q$ is a prime, this yields that they must all be one dimensional. Therefore, there exist elements $P_1,\dots,P_q$ in $\mathfrak{P}$ such that

$$
\mathfrak {P} / \mathfrak {P} ^ {\prime} = \left\langle P _ {1} \mathfrak {P} ^ {\prime} / \mathfrak {P} ^ {\prime} \right\rangle \times \dots \times \left\langle P _ {q} \mathfrak {P} ^ {\prime} / \mathfrak {P} ^ {\prime} \right\rangle
$$

and

$$
U ^ {- 1} P _ {i} \mathfrak {P} ^ {\prime} U = P _ {i} ^ {*} i ^ {(U)} \mathfrak {P} ^ {\prime}, \quad U \in \mathfrak {U}, \quad 1 \leq i \leq q,
$$

where $s_1, \cdots, s_q$ are linear characters of $\mathfrak{U} \pmod{p}$ with $s_{i+1}(U) = s_1(Q^{-i}UQ^i)$ for $U \in \mathfrak{U}$ and a suitably chosen generator $Q$ of $\mathfrak{D}^*$. Since $|\mathfrak{D}^*\mathfrak{U}|$ is odd, $s_i s_j \neq 1$ for any $i, j$ with $1 \leq i, j \leq q$. Hence, if $i, j$ are given, there exists $U \in \mathfrak{U}$ such that $s_i(U)s_j(U) \neq 1$. For $1 \leq k \leq q$, let $P_k'$ be an element of $\mathfrak{P}'$ such that

$$
U ^ {- 1} P _ {k} \mathfrak {P} _ {0} U = P _ {k} ^ {s _ {k} (U)} P _ {k} ^ {\prime} \mathfrak {P} _ {0}.
$$

Since $\mathfrak{P}' / \mathfrak{P}_0\subseteq Z(\mathfrak{P} / \mathfrak{P}_0)$ , we get that

$$
\begin{array}{r l} {[ P _ {i}, P _ {j} ] \equiv U ^ {- 1} [ P _ {i}, P _ {j} ] U \equiv [ P _ {i} ^ {* i (U)} P _ {i} ^ {\prime}, P _ {j} ^ {* j (U)} P _ {j} ^ {\prime} ]} \\ & {\equiv [ P _ {i} ^ {* i (U)}, P _ {j} ^ {* j (U)} ] \equiv [ P _ {i}, P _ {j} ] ^ {* i (U) * j (U)} (\mathrm{mod} \mathfrak {P} _ {0}) .} \end{array}
$$

Since  $s_{i}(U)s_{j}(U)\neq1$ , this yields that  $[P_{i},P_{j}]\in\mathfrak{P}_{0}$  for  $1\leq i,j\leq q$ . Since  $\mathfrak{P}=\langle P_{1},\cdots,P_{q}\rangle$ , we get that  $P'\subseteq P_{0}$  contrary to construction. Thus,  $P'=1$  as required.

LEMMA 29.6. If $\mathcal{S}((\mathfrak{H}\mathfrak{C})')$ is not coherent and $\mathfrak{C} \neq 1$, then $\mathcal{S}_0$ is not coherent.

Proof. Suppose that $\mathfrak{C} \neq 1$. Assume that $\mathcal{S}_0$ is coherent. Let $\mathcal{S}_1 = \mathcal{S}_0$. Let $\mathcal{S}_2, \cdots, \mathcal{S}_k$ be the equivalence classes of $\mathcal{S}((\mathfrak{H}\mathfrak{C})') - \mathcal{S}_0$ chosen so that every character in $\mathcal{S}_m$ has degree $\iota_m q$ for $2 \leq m \leq k$, and $\iota_2 \leq \cdots \leq \iota_k$. Suppose $\bigcup_{i=1}^k \mathcal{S}_i$ is not coherent. By Hypothesis 11.1, and Lemma 29.1, all parts of Hypothesis 10.1 are satisfied except possibly inequality (10.2). Since $\mathcal{S}((\mathfrak{H}\mathfrak{C})')$ is not coherent, inequality (10.2) must be violated for some $m$.

Every character in  $\bigcup_{i=1}^{k}S_{i}$  is a constituent of a character induced by a linear character of  $\mathfrak{G}\mathfrak{C}$ . Thus  $\ell_{m}\leq(u/c)$  for  $1<m\leq k$ . Hence, violation of inequality (10.2) yields that

$$
\frac {u - 1}{q} \leq 2 \mathscr {L} _ {m} \leq 2 \frac {u}{c}.
$$

Since $c \equiv 1 \pmod{2q}$ and $c \neq 1$, this implies that

$$
u - 1 \leq 2 q \frac {u}{c} = \frac {(2 q + 1)}{c} u - \frac {u}{c} \leq u - \frac {u}{c} <   u - 1.
$$

Hence $\bigcup_{i=1}^{k}\mathcal{S}_{i}$ is coherent. Since $\mathcal{S}((\mathfrak{H}\mathfrak{C})')=\bigcup_{i=1}^{k}\mathcal{S}_{i}$, the proof is complete.

The proof of Theorem 29.1 is now immediate. Lemmas 29.2, 29.4 and 29.5 imply statement (i). Lemmas 29.2, 29.4, 29.5, and 29.6 imply statement (ii).

## 30. Characters of Subgroups of Type II, III and IV

The notation introduced at the beginning of Section 29 is used in this section. The main purpose of this section is to prove the following result.

THEOREM 30.1. Let $\mathfrak{S}$ be a subgroup of type II, III or IV. Then $\mathcal{S}$ is coherent except possibly if $\mathfrak{S}$ is of type II, $\mathfrak{S}$ is a non abelian 3-group, $\mathfrak{H}\mathfrak{U}/\mathfrak{C}$ is a Frobenius group with Frobenius kernel $\mathfrak{H}\mathfrak{C}/\mathfrak{C}$, $u < 3^{q/2}$, $|\mathfrak{D}:\mathfrak{D}'| = 3^q$ and $\mathfrak{T}$ is a subgroup of type V.

All lemmas in this section will be proved under the following assumption.

Hypothesis 30.1.

(i) $\mathfrak{S}$ is a subgroup of type II, III, or IV.

(ii) $\mathcal{S}$ is not coherent except possibly if $\mathfrak{S}$ is of type II.

(iii) $\mathfrak{U} / \mathfrak{U}'$ has exponent $a$.

For any subgroup $\mathfrak{S}_1$ of $\mathfrak{S}'$ let $\mathcal{S}(\mathfrak{S}_1)$ be the set of characters in $\mathcal{S}$ which have $\mathfrak{S}_1$ in their kernel. Notice that this notation differs from that used in Section 29.

LEMMA 30.1. The degree of every character in S is divisible by aq.

Proof. Every character in $\mathcal{S}$ is a constituent of a character of $\mathfrak{S}$ induced by a nonprincipal character of $\mathfrak{S}$. For any character $\theta$ of $\mathfrak{S}$ let $\tilde{\theta}$ be the character of $\mathfrak{H}\mathfrak{U}$ induced by $\theta$. Set $\mathfrak{U}_1 = \mathfrak{J}(\theta) \cap \mathfrak{U}$. Let $|\mathfrak{U} : \mathfrak{U}_1| = b$. If $\mathfrak{S}$ is of type II or III, then by Lemma 4.5 it suffices to show that if $\theta \neq 1_{\mathfrak{S}}$, then $a | b$.

Let $\mathfrak{R}$ be the kernel of $\theta$ and let $H\in\mathfrak{H}-\mathfrak{R}$ such that $H\mathfrak{R}\in Z(\mathfrak{H}/\mathfrak{R})$. Then $\mathfrak{R}\triangleleft\mathfrak{H}\mathfrak{U}_{1}$ and $U^{-1}H\mathfrak{R}U=H\mathfrak{R}$ for $U\in\mathfrak{U}_{1}$. As $(u,h)=1$, if $U\in\mathfrak{U}_{1}$, then $U$ centralizes some element in $H\mathfrak{R}$. Hence, $\mathfrak{U}_{1}\subseteq\widehat{\mathfrak{S}}$. Let $\mathfrak{U}_{0}=\{U^{b}|U\in\mathfrak{U}\}$. Then $\mathfrak{U}_{0}$ char $\mathfrak{U}$ and $\mathfrak{U}_{0}\subseteq\mathfrak{U}_{1}\subseteq\widehat{\mathfrak{S}}$.

Suppose $\mathfrak{U}_0 \neq 1$. If $\mathfrak{S}$ is of type II, then $\widetilde{\mathfrak{S}}$ is a T.I. set in $\mathfrak{G}$ by Theorem 14.2. Hence, $N(\mathfrak{U}) \subseteq N(\mathfrak{U}_0) \subseteq \mathfrak{S}$ contrary to definition. If $\mathfrak{S}$ is of type III, then by Theorem 29.1, $\mathfrak{U}\mathfrak{D}^*$ is represented irreducibly on $\mathfrak{S}$. Since $\mathfrak{U}_0 \triangleleft \mathfrak{U}\mathfrak{D}^*$, $\mathfrak{U}_0$ is in the kernel of this representation. Thus, $\mathfrak{U}_0 \subseteq C(\mathfrak{H})$ contrary to Theorem 29.1. Thus, $\mathfrak{U}_0 = 1$. Therefore $U^b = 1$ for $U \in \mathfrak{U}$ and so $a|b$ in case $\mathfrak{S}$ is of type II or III.

If $\mathfrak{S}$ is of type IV, we will show that Hypothesis 11.1 and (11.2) are satisfied with $\mathfrak{H}_0$ in that hypothesis being taken as our present $\mathfrak{H},\mathfrak{L}$ being taken as $\mathfrak{S} / \mathfrak{H},\mathfrak{H}$ and $\mathfrak{R}$ being taken as $\mathfrak{S}' / \mathfrak{H}$, and $\hat{\mathfrak{L}}_0$ being taken as $\mathfrak{S}'$. Certainly (i) is satisfied. Since $\mathfrak{S} / \mathfrak{H}$ is a Frobenius group with Frobenius kernel $\mathfrak{S}' / \mathfrak{H}$, (ii) and (11.2) are satisfied, and the remaining conditions follow immediately from the fact that $\mathfrak{S} / \mathfrak{H}$ is a

Frobenius group. The present $\mathcal{S}_0$ plays the role of $\mathcal{S}$ in Hypothesis 11.1 (iii).

Notice now that Hypothesis 11.2 is satisfied. By Lemma 11.2 and the fact that $\mathcal{S}_0$ is not coherent it follows that $\mathfrak{S}'/\mathfrak{H}$ is a non abelian $r$-group for some prime $r$ whose derived group and Frattini subgroup coincide. But $\mathfrak{U} \cong \mathfrak{S}'/\mathfrak{H}$. Since $\mathfrak{C} = \mathfrak{U}'$, $\mathfrak{U}/\mathfrak{C}$ is of exponent $r$, so $a = r$. As $\mathfrak{U}$ has no fixed points on $\mathfrak{H}'$, it follows readily that every non linear character of $\mathfrak{S}'$ has degree divisible by $r$, as required.

LEMMA 30.2. For $1 \leq i \leq t$, $|\mathfrak{P}_i : D(\mathfrak{P}_i)| = p_i^q$ and $\mathfrak{U}/\mathfrak{C}_i$ has exponent $a$.

Proof. If $\mathfrak{S}$ is of type III or IV, the result follows from Theorem 29.1. Suppose $\mathfrak{S}$ is of type II. Then $\hat{\mathfrak{S}}$ is a T.I. set in $\mathfrak{G}$ by Theorem 14.2. Let $a_i$ be the exponent of $\mathfrak{U}/\mathfrak{C}_i$ for $1 \leq i \leq t$. Let $\mathfrak{U}_i = \{U^{a_i} | U \in \mathfrak{U}\}$. Then $\mathfrak{U}_i \subseteq \mathfrak{C}_i \subseteq \hat{\mathfrak{S}}$ and $\mathfrak{U}_i$ char $\mathfrak{U}$. Thus, if $\mathfrak{U}_i \neq 1$, then $N(\mathfrak{U}) \subseteq N(\mathfrak{U}_i) \subseteq \mathfrak{S}$, contrary to definition of subgroups of type II.

Suppose $|\mathfrak{P}_i : D(\mathfrak{P}_i)| > p_i^q$ for some $i$ with $1 \leq i \leq t$. Since $C_{\mathfrak{P}_i}(\mathfrak{Q}^*)$ is cyclic, this implies the existence of a subgroup $\mathfrak{H}_1$ with $\mathfrak{W}_2 \subseteq \mathfrak{H}_1 \subset \mathfrak{H}$ such that $\mathfrak{H}/\mathfrak{H}_1$ is a chief factor of $\mathfrak{S}$. By 3.16 (i), $\mathfrak{H}\mathfrak{U}/\mathfrak{H}_1$ is nilpotent. Thus, $\mathfrak{U} \subseteq \widehat{\mathfrak{S}}$ and $N(\mathfrak{U}) \subseteq \mathfrak{S}$, contrary to definition.

LEMMA 30.3. For $1 \leq i \leq t$, either $a | (p_i - 1)$ or $a | (p_i - 1)$ and $(a, p_i - 1) = 1$. In the first case, $\mathfrak{P}_i / D(\mathfrak{P}_i)$ is the direct product of $q$ groups of order $p_i$, each of which is normalized by $\mathfrak{U}$. In the second case, $\mathfrak{U} / \mathfrak{C}_i$ is cyclic of order $a$ and acts irreducibly on $\mathfrak{P}_i / D(\mathfrak{P}_i)$.

Proof. By Lemma 30.2, $\mathfrak{U}\mathfrak{D}^{*}$ is represented irreducibly on $\mathfrak{P}_{i}/D(\mathfrak{P}_{i})$. As $\mathfrak{U} \triangleleft \mathfrak{U}\mathfrak{D}^{*}$, the restriction of this representation to $\mathfrak{U}$ breaks up into a direct sum of irreducible representations all of which have the same degree $d$. By Lemma 30.2, $d|q$ and so $d=1$ or $d=q$.

If $d = 1$, the order of every element in $\mathfrak{U} / \mathfrak{C}_i$ divides $(p_i - 1)$. Hence, by Lemma 30.2, $a \mid (p_i - 1)$.

If $d = q$, then $\mathfrak{U}$ acts irreducibly on $\mathfrak{P}_i / D(\mathfrak{P}_i)$. Thus, $\mathfrak{U} / \mathfrak{C}_i$ is cyclic. By Lemma 30.2, $|\mathfrak{U} : \mathfrak{C}_i| = a$. Therefore, $a | (p_i^q - 1)$. Let $\mathfrak{U} / \mathfrak{C}_i = \langle U \rangle$. Then the characteristic roots of $U$ are algebraically conjugate over $GF(p)$. Hence, this is also the case for every power of $U$. If $(a, p_i - 1) \neq 1$, then some power $U_1 \neq 1$ of $U$ has its characteristic roots in $GF(p)$ and thus is a scalar. This violates the fact that $\mathfrak{U}\Omega^*$ is a Frobenius group.

LEMMA 30.4. Suppose $(a, p_i - 1) = 1$ for some $i$, $1 \leq i \leq t$. Let

$$
\mathfrak {H} _ {1} = \mathfrak {P} _ {i} ^ {\prime} \prod_ {j \neq i} \mathfrak {P} _ {j},
$$

and let $|\mathfrak{P}_i: \mathfrak{P}_i'| = p_i^{m_i'}$. Then $m_i' = m_i q$ for some integer $m_i$. Further more, $\mathcal{S}(\mathfrak{H}_1)$ contains at least

$$
\frac {1}{q} \left\{\frac {(p _ {i} ^ {q m _ {i}} - 1) c _ {i}}{a} - (p ^ {m _ {i}} - 1) \right\}
$$

irreducible characters of degree $aq$ and at least $(p_{i}^{m_i} - 1)$ characters of weight $q$ and degree $aq$.

Proof. By Lemma 30.3, $\mathfrak{U}/\mathfrak{C}_i$ is cyclic. By Theorem 29.1, $\mathfrak{S}$ is not of type IV, so $\mathfrak{U}$ is abelian. Hence, $\mathfrak{H}\mathfrak{U}/\mathfrak{H}_1\mathfrak{C}_i$ is a Frobenius group. By Lemma 30.2, $|\mathfrak{U}:\mathfrak{C}_i|=a$. Furthermore, since $\mathfrak{U}\mathfrak{D}^*$ acts irreducibly on $\mathfrak{P}_i/D(\mathfrak{P}_i)$, $\bar{\mathfrak{S}}=\mathfrak{H}/\mathfrak{H}_1$ is the direct product of $q$ cyclic groups of the same order $p_i^{m_i}$. Thus, $qm_i=m_i'$, and $|C_{\bar{\mathfrak{S}}}(\mathfrak{Q}^*)|=p_i^{m_i}$. By 3.16 (iii) every non principal irreducible character of $\mathfrak{H}\mathfrak{C}_i/\mathfrak{H}_1\mathfrak{C}_i$ induces an irreducible character of $\mathfrak{H}\mathfrak{U}/\mathfrak{H}_1\mathfrak{C}_i$ of degree $a$. Since $\mathfrak{U}$ is abelian, this implies that every irreducible character of $\mathfrak{H}\mathfrak{C}_i/\mathfrak{H}_1$ which does not have $\bar{\mathfrak{S}}$ in its kernel induces an irreducible character of $\mathfrak{H}\mathfrak{U}/\mathfrak{H}_1$ of degree $a$. Hence, $\mathfrak{H}\mathfrak{U}/\mathfrak{H}_1$ has at least

$$
\frac {(p _ {i} ^ {m _ {i} q} - 1) c _ {i}}{a}
$$

distinct irreducible characters of degree a.

Since $\mathfrak{S} / \mathfrak{H}_1$ satisfies Hypothesis 13.2, Lemma 13.7 implies that all but $p^{m_i} - 1$ non principal irreducible characters of $\mathfrak{SU} / \mathfrak{H}_1$ induce irreducible characters of $\mathfrak{S}$. The result now follows.

LEMMA 30.5. Suppose that $a \mid (p_i - 1)$ for some $i$ with $1 \leq i \leq t$. Let

$$
\mathfrak {H} _ {1} = \mathfrak {P} _ {i} ^ {\prime} \prod_ {j \neq i} \mathfrak {P} _ {j}
$$

and let $|\mathfrak{P}_i:\mathfrak{P}_i'| = p_i^{m_i'}$. Then $m_i = m_i' / q$ is an integer and $\mathcal{S}(\mathfrak{Q}_1)$ contains at least

$$
\frac {(p _ {i} ^ {m _ {i}} - 1)}{a} \frac {u}{a u ^ {\prime}}
$$

irreducible characters of degree $aq$, where $|\mathfrak{U}'| = u'$.

Proof. For any subgroup $\mathfrak{X}$ of $\mathfrak{S}$, let $\bar{\mathfrak{X}} = \mathfrak{X}\mathfrak{H}_1 / \mathfrak{H}_1$. By Lemma 30.3, $\bar{\mathfrak{S}}$ contains a cyclic subgroup $\mathfrak{P}_{i_1}$ which is normalized by $\mathfrak{U}$ such that

$$
\mid \mathfrak {P} _ {i 1} \mid = p _ {i} ^ {m _ {i}}
$$

and such that $\mathfrak{H} = \mathfrak{P}_{i1} \times \mathfrak{H}_0$ for some subgroup $\mathfrak{H}_0$ which is normalized by $\mathfrak{U}$. Since $\mathfrak{U}\mathfrak{Q}^*$ acts irreducibly on $\mathfrak{P}_i / D(\mathfrak{P}_i)$, it follows that $m_i = m_i' / q$. Let $\mathfrak{U}_1$ be the kernel of the representation of $\mathfrak{U}$ on $\mathfrak{P}_{i1}$. Then $\mathfrak{U} / \mathfrak{U}_1$ is cyclic and so $|\mathfrak{U} : \mathfrak{U}_1| \leq a$. There are at least

$$
\frac {(p _ {i} ^ {m _ {i}} - 1)}{u ^ {\prime}} \mid \mathfrak {N} _ {1} \mid
$$

distinct linear characters of $\mathfrak{F}\overline{\mathfrak{U}}_{1}/\mathfrak{G}_{0}$ which do not have $\mathfrak{P}_{i1}$ in their kernel. Each of these induces an irreducible character of $\mathfrak{F}\overline{\mathfrak{U}}$ of degree $|\mathfrak{U}:\mathfrak{U}_{1}|$. Thus, by Lemma 30.1, $|\mathfrak{U}:\mathfrak{U}_{1}|=a$ and there are at least

$$
\frac {(p _ {i} ^ {m _ {i}} - 1) \cdot u}{a \cdot a \cdot u ^ {\prime}}
$$

distinct irreducible characters of $\mathfrak{H}\mathfrak{U}$ of degree $a$ which have $\mathfrak{H}_1$ in their kernel, and as characters of $\mathfrak{S}'$ have $\mathfrak{H}_0$ in their kernel. If one of these induced a reducible character of $\mathfrak{S}$ or two of these induced the same character of $\mathfrak{S}$, then $\mathfrak{D}^*$ would normalize $\mathfrak{H}_0$, contrary to the fact that $\mathfrak{U}\mathfrak{D}^*$ acts irreducibly on $\mathfrak{P}_i / D(\mathfrak{P}_i)$.

LEMMA 30.6. If $\mathcal{S}$ contains no irreducible character of degree $aq$, then $t = 1$, $\mathfrak{P}_1' = D(\mathfrak{P}_1)$, $a = u = (p_1^q - 1)/(p_1 - 1)$, and $c = c_1 = 1$. Furthermore, $\mathcal{S}(\mathfrak{Q}')$ is coherent.

Proof. By Lemmas 30.3 and 30.5, $(a, p_i - 1) = 1$ and $a$ divides $(p_i^q - 1)/(p_i - 1)$ for $1 \leq i \leq t$. Suppose that for some $i$,

$$
\frac {(p _ {i} ^ {q m _ {i}} - 1) c _ {i}}{a} - (p _ {i} ^ {m _ {i}} - 1) \leq 0.
$$

Then

$$
\frac {(p _ {i} ^ {q m _ {i}} - 1)}{(p _ {i} ^ {m _ {i}} - 1)} c _ {i} \leqq a.
$$

Therefore, $c_{i} = 1$, $m_{i} = 1$, and $a = (p_{i}^{q} - 1) / (p_{i} - 1)$. Thus,

$$
\frac {(p _ {i} ^ {q m i} - 1) c _ {i}}{a} - (p _ {i} ^ {m i} - 1) = 0.\tag{30.1}
$$

Now Lemma 30.4 implies that (30.1) holds for $1 \leq i \leq t$. Thus, $t = 1$. Hence, $c = c_1 = 1$, $u = a = (p^q - 1)/(p - 1)$, $p = p_1$. Also, $m_1 = 1$, and

so $\mathfrak{P}_1' = D(\mathfrak{P}_1)$.

If a character $\theta$ in $\mathcal{S} \cup \mathcal{S}_0$ is equivalent to a character in $\mathcal{S}(\mathfrak{H}')$, then its degree is prime to $|\mathfrak{H}|$, so $\mathfrak{H}' \subseteq \ker \theta$. Thus, the equivalence relation in Hypothesis 11.1 has the property that the present set $\mathcal{S}(\mathfrak{H}')$ is a union of equivalence classes. Therefore, $\mathcal{S}(\mathfrak{H}')$ consists of $(p - 1)$ reducible characters of degree $aq$. Theorem 14.2 implies that Hypothesis 13.3 is satisfied. Hence, Lemma 13.9 implies that $\mathcal{S}(\mathfrak{H}')$ is coherent.

The remaining lemmas in this section will be proved under the following stronger assumption.

Hypothesis 30.2.

(i) Hypothesis 30.1 is satisfied.

(ii) $\mathcal{S}$ is not coherent.

LEMMA 30.7. If $\mathcal{S}(\mathfrak{S}')$ is not coherent, then $\mathfrak{S} = \mathfrak{P}_1$, $\mathfrak{C}_1 = 1$, $a = (p - 1)/2$, $p = p_1$, $u \neq a$, and $D(\mathfrak{P}_1) = \mathfrak{P}_1'$. The degree of every character in $\mathcal{S}(\mathfrak{S}')$ is either $aq$ or $uq$, and $\mathcal{S}(\mathfrak{S}')$ contains exactly $2u/a$ irreducible characters of degree $aq$.

Proof. Let $d_1 < \cdots < d_k$ be all the degrees of characters in $\mathcal{S}((\mathfrak{H}\mathfrak{C})')$. Define $\lambda_i = d_i / aq$ for $1 \leq i \leq k$. By Lemmas 13.10, 30.1 and 30.6, all the assumptions of Theorem 10.1 are satisfied except possibly inequality (10.2). Every character in $\mathcal{S}((\mathfrak{H}\mathfrak{C})')$ is a constituent of a character of $\mathfrak{S}$ which is induced by a linear character of $\mathfrak{H}\mathfrak{C}$. Hence, $d_k \leq qu / c$, and so $\lambda_k \leq u / ac$.

Choose the notation so that $a|(p_i - 1)$ for $1 \leq i \leq t_0$ and $(a, p_i - 1) = 1$ for $t_0 + 1 \leq i \leq t$. If $\mathcal{S}((\mathfrak{D}\mathfrak{C})')$ is not coherent then inequality (10.2) is violated. Lemmas 30.2 and 30.3 imply that for $t_0 + 1 \leq i \leq t$, $c_i = u / a$. Thus by Lemmas 30.4 and 30.5, there exists $m$ with $1 < m \leq k$, such that

$$
\begin{array}{r l} \sum_ {i = 1} ^ {t _ {0}} \frac {u}{a} \cdot \frac {(p _ {i} ^ {m _ {i}} - 1)}{a u ^ {\prime}} + \sum_ {i = t _ {0} + 1} ^ {t} \left\{\frac {u}{a} \cdot \frac {(p _ {i} ^ {q m _ {i}} - 1)}{q a} - \frac {(p _ {i} ^ {m _ {i}} - 1)}{q} \right\} \\ & + \sum_ {i = t _ {0} + 1} ^ {t} \frac {(p _ {i} ^ {m _ {i}} - 1)}{q} \leq 2 u _ {m} \leq \frac {2 u}{c a}. \end{array}
$$

Therefore,

$$
\sum_ {i = 1} ^ {t _ {0}} \frac {\left(p _ {i} ^ {m _ {i}} - 1\right)}{a u ^ {\prime}} + \sum_ {i = t _ {0} + 1} ^ {t} \frac {\left(p _ {i} ^ {q m _ {i}} - 1\right)}{q a} \leq 2 / _ {m} \frac {a}{u} \leq \frac {2}{c} \leq 2.\tag{30.2}
$$

For

$$
1 \leq i \leq t _ {0}, \frac {(p _ {i} ^ {m _ {i}} - 1)}{a} \geq 2 p ^ {(m _ {i} - 1)}.
$$

By Theorem 29.1, $c \geq u'$. Thus, (30.2) implies that

$$
t _ {0} \leq 1. \quad \text { If } t _ {0} = 1, \text { then } m _ {1} = 1, t = 1.\tag{30.3}
$$

Assume first that $t_0 = 0$. If $t = 1$, then since $q < p_1^q$ and $a \leq (p_1^q - 1) / (p_1 - 1)$, (30.2) yields $m_1 = 1$. Thus, every character in $\mathcal{S}((\mathfrak{H}\mathfrak{C})')$ has degree $aq$. Therefore the definition of subcoherence implies directly that $\mathcal{S}((\mathfrak{H}\mathfrak{C})')$ is coherent contrary to assumption. Suppose now that $t \geq 2$. Then (30.2) yields that $(p_1 - 1) + (p_2 - 1) \leq 2q$. Therefore,

$$
p _ {i} \not \equiv 1 (\mathrm{mod} q), \quad i = 1, 2.\tag{30.4}
$$

Further, (30.2) also implies that

$$
\frac {1}{a} \frac {(p _ {1} ^ {q} - 1)}{(p _ {1} - 1)} + \frac {1}{a} \frac {(p _ {2} ^ {q} - 1)}{(p _ {2} - 1)} \leqq q .\tag{30.5}
$$

It follows from (30.4) that

$$
\frac {1}{a} \frac {(p _ {1} ^ {q} - 1)}{(p _ {1} - 1)} \equiv \frac {1}{a} \equiv \frac {1}{a} \frac {(p _ {2} ^ {q} - 1)}{(p _ {2} - 1)} (\mathrm{mod} q).\tag{30.6}
$$

Each term on the left of (30.5) is an integer. Hence, if  $p_{1} > p_{2}$ , (30.6) yields that

$$
\frac {1}{a} \frac {(p _ {1} ^ {q} - 1)}{(p _ {1} - 1)} \geq q + \frac {1}{a} \frac {(p _ {2} ^ {q} - 1)}{(p _ {2} - 1)},
$$

contrary to (30.5). Consequently,  $t_{0} \neq 0$ .

Now (30.2) and (30.3) imply that $t = 1$, so that $\mathfrak{H} = \mathfrak{P}_1$. We also conclude that $m_1 = 1$, so that $D(\mathfrak{P}_1) = \mathfrak{P}_1'$. Furthermore, $c = c_1 = u'$, and $(p_1 - 1)/a \leq 2$. Since $ap_1$ is odd, we have $p_1 - 1 = 2a$. Finally we get that $\angle_m = u/ac$ and so $m = k$. If $k = m > 2$, or if $\mathcal{S}((\mathfrak{H}\mathfrak{C}')')$ contains more than $2u/a$ irreducible characters of degree $qa$, then (30.2) is replaced by a strict inequality which is impossible as $(p_1 - 1)/a = 2$. Thus, $k = m = 2$, and so $d_2 = uq/c$ and the degree of a character in $\mathcal{S}((\mathfrak{H}\mathfrak{C}')')$ is either $aq$ or $uq/c$. If $\mathfrak{S}$ is of type II or III, then $(\mathfrak{H}\mathfrak{C})' = \mathfrak{H}'$ and the result is proved.

Suppose that $\mathfrak{S}$ is of type IV. Since the degree of any character in $\mathcal{S}((\mathfrak{H}\mathfrak{C})')$ is either $aq$ or $uq/c$, $\mathfrak{U}/\mathfrak{C}$ is generated by two elements. Since $\mathfrak{C} = \mathfrak{U}'$, $\mathfrak{U}$ is generated by two elements. Thus, if we set $\mathfrak{H}_0 = \mathfrak{H}$, replace $\mathfrak{H}$ and $\mathfrak{R}$ by $\mathfrak{S}'/\mathfrak{H}$, and replace $\mathfrak{L}$ by $\mathfrak{S}$ in Hypothesis 11.2, then by Lemma 29.1, Hypothesis 11.2 holds and by Lemma 11.3 and Theorem 29.1, we conclude that $\mathcal{S} = \mathcal{S}(\mathfrak{H}')$ is coherent, contrary to

assumption.

LEMMA 30.8. $\mathcal{S}(\mathfrak{G}')$ is coherent.

Proof. By Lemma 30.7, it may be assumed that $\mathfrak{H} = \mathfrak{P}$ is a $p$-group for some prime $p$, that $D(\mathfrak{P}) = \mathfrak{P}'$, and that $\mathfrak{C} = 1$. Suppose that $\mathcal{S}(\mathfrak{H}')$ is not coherent. Let $\mathcal{S}_1$ be the set of irreducible characters in $\mathcal{S}(\mathfrak{H}')$ of degree $aq$. Then by Lemma 30.7

$$
\mid \mathcal {S} _ {1} \mid = \frac {2 u}{a}, \quad a = \frac {(p - 1)}{2}.\tag{30.7}
$$

Let $\mathcal{S}_2$ be the set of irreducible characters in $\mathcal{S}(\mathfrak{S}')$ of degree $uq$. The group $\mathfrak{S}/\mathfrak{S}'$ satisfies Hypothesis 13.2. Hence, by Lemmas 13.5, 13.7 and 30.7, there are $(p-1)$ reducible characters in $\mathcal{S}$ of weight $q$ and degree $uq$ which have $\mathfrak{S}'$ in their kernel. As the sum of the squares of degrees of irreducible characters of $\mathfrak{S}/\mathfrak{S}'$ is $p^q uq$, we get that

$$
u q + \left| \mathcal {S} _ {1} \right| q ^ {2} a ^ {2} + (p - 1) q u ^ {2} + \left| \mathcal {S} _ {2} \right| q ^ {2} u ^ {2} = p ^ {q} u q.\tag{30.8}
$$

Since U is abelian and is generated by two elements, we also have

$$
u \leq a ^ {2}.\tag{30.9}
$$

Now (30.7), (30.8) and (30.9) yield that

$$
\begin{array}{r l} | \mathcal {S} _ {2} | & \geq \frac {p ^ {q} - (p - 1) u - 2 q a - 1}{u q} \\ & \geq \frac {1}{a ^ {2} q} \left\{(p ^ {q} - 1) - (p - 1) q - \frac {(p - 1) ^ {3}}{4} \right\}. \end{array}\tag{30.10}
$$

Hence, by (5.8), $\mathcal{S}_2$ is non empty.

Let $\mathcal{S}_i = \{\lambda_{is} | 1 \leq s \leq n_i\}$ for $i = 1, 2$. The character $\lambda_{11}$ is induced by a linear character of some subgroup $\mathfrak{S}_0$ of index $a$ in $\mathfrak{S}'$. Define

$$
\alpha = \left(\tilde {1} _ {\mathfrak {S} _ {0}} - \lambda_ {1 1}\right),\tag{30.11}
$$

where $\widetilde{1}_{\mathfrak{S}_0}$ is the character of $\mathfrak{S}$ induced by $1_{\mathfrak{S}_0}$. Since $\mathfrak{S}_0 \triangleleft \mathfrak{S}'$, it follows that $1_{\mathfrak{S}_0}$ induces $\rho_{\mathfrak{S}' / \mathfrak{S}_0}$ on $\mathfrak{S}'$. Since $\mathfrak{D}^*$ does not normalize $\mathfrak{S}_0$, (30.11) is seen to imply that

$$
\left| \alpha \right| ^ {2} = a + 1 + (q - 1) \frac {a ^ {2}}{u}.
$$

Since $\hat{\mathfrak{S}}$ is tamely imbedded in $\mathfrak{G}$ and $\alpha$ vanishes on $\mathfrak{S} - \hat{\mathfrak{S}}$, we get that

$$
\left| \left| \alpha^ {\tau} \right| \right| ^ {2} = \left| \left| \alpha \right| \right| ^ {2} = a + 1 + (q - 1) \frac {a ^ {2}}{u}.\tag{30.12}
$$

Furthermore,

$$
\left(\alpha^ {\tau}, \lambda_ {2 i} ^ {\tau} - \lambda_ {2 j} ^ {\tau}\right) = \left(\alpha , \lambda_ {2 i} - \lambda_ {2 j}\right) = 0
$$

for all values of i and j.

Suppose that $(\alpha^{\tau},\lambda_{2i})\neq 0$ for some $i$. Then $(\alpha^{\tau},\lambda_{2i}^{\tau})\neq 0$ for all $i$. Hence (30.10) and (30.12) imply that

$$
\begin{array}{r l} \frac {p ^ {2} - 1}{q a ^ {2}} - \frac {(p - 1)}{a ^ {2}} - \frac {(p - 1)}{q} & \leq a + 1 + (q - 1) \frac {a ^ {2}}{u} \\ & = \frac {p - 1}{2} + 1 + (q - 1) \frac {a ^ {2}}{u}. \end{array}
$$

Thus

(30.13)

$$
\begin{array}{r l} 2 \{1 + \dots + p ^ {q - 1} \} & = \frac {p ^ {q} - 1}{a} \\ & \leq q \frac {(p - 1)}{2} \left\{\frac {2}{a} + \frac {p _ {\bullet} ^ {q} - 1}{q} + \frac {p - 1}{2} + 1 + (q - 1) \frac {a ^ {2}}{u} \right\} \\ & \leq q \frac {(p - 1)}{2} \left(p + q \frac {a ^ {2}}{u}\right) \\ & <   q \frac {(p - 1)}{2} \left(p + q \frac {p}{2}\right). \end{array}
$$

Therefore

$$
4 p ^ {q - 2} <   4 \frac {p ^ {q - 1} - 1}{p - 1} <   p q \left(1 + \frac {\mathrm{D}}{2}\right).
$$

Hence

$$
3 ^ {q - 2} <   4 p ^ {q - 3} <   q \left(1 + \frac {q}{2}\right) <   q ^ {2}.
$$

Thus $q = 3$ by (5.1). Now (30.13) becomes

$$
2 (1 + p + p ^ {2}) \leq \frac {3}{2} (p - 1) \left\{\frac {4}{p - 1} + \frac {5}{6} (p - 1) + 1 + \frac {2 a ^ {2}}{u} \right\}.
$$

Thus

$$
\frac {4}{3} (1 + p + p ^ {2}) \leq 4 + p - 1 + \frac {5}{6} (p - 1) ^ {2} + \frac {2 a ^ {2}}{u} (p - 1).
$$

This implies that

$$
\frac {4}{3} p ^ {2} \leq p + \frac {5}{6} p ^ {2} + \frac {2 a ^ {2}}{u} p.
$$

Therefore $(1/2)p^{2} \leq p(1 + (2a^{2}/u))$, or equivalently $(1/2)p \leq 1 + (2a^{2}/u)$. Thus (30.7) yields that

$$
u \leq \frac {2 a ^ {2}}{\frac {1}{2} p - 1} = \frac {4 a ^ {2}}{p - 2} \leq \frac {(p - 1) ^ {2}}{(p - 2)} <   p + 1 <   3 a.
$$

This is impossible since $a \mid u$, $a \neq u$ and both $a$ and $u$ are odd. Thus,

$$
\left(\alpha^ {\tau}, \lambda_ {2 i} ^ {\tau}\right) = 0 \quad \text { for } \quad \lambda_ {2 i} \in \mathscr {S} _ {2}.\tag{30.14}
$$

Define $\beta = (u / a)\lambda_{11} - \lambda_{21}\in \mathcal{I}_0(\mathcal{S})$. Suppose that $(\beta^{\tau},\lambda_{11}^{\tau}) = (u / a) - b$. As $\tau$ is an isometry on $\mathcal{I}_0(\mathcal{S})$, this yields that

$$
\left(\beta^ {\tau}, \lambda_ {i i} ^ {\tau}\right) = \frac {u}{a} \delta_ {i 1} - b \quad \text { for   all } i.
$$

Therefore,

$$
\beta^ {\tau} = \left(\frac {u}{a} - b\right) \lambda_ {1 1} ^ {\tau} - b \sum_ {i \neq 1} \lambda_ {1 i} ^ {\tau} + \Gamma + \Delta ,\tag{30.15}
$$

where $\Gamma$ is a linear combination of elements in $\mathcal{S}_2^\tau$ and $\Delta$ is orthogonal to $\mathcal{S}_1^\tau \cup \mathcal{S}_2^\tau$. Since $(\beta^\tau, \lambda_{21}^\tau - \bar{\lambda}_{21}^\tau) \neq 0$, it follows that $||\Gamma||^2 \geq 1$. Since

$$
\left| \left| \beta^ {\tau} \right| \right| ^ {2} = \left| \left| \beta \right| \right| ^ {2} = \left(\frac {u}{a}\right) ^ {2} + 1,\tag{30.16}
$$

(30.7) and (30.16) yield

$$
\left\| \Delta \right\| ^ {2} + \left(\frac {u}{a} - b\right) ^ {2} + \left(2 \frac {u}{a} - 1\right) b ^ {2} \leq \left(\frac {u}{a}\right) ^ {2}.
$$

This implies that

$$
\left| \left| \Delta \right| \right| ^ {2} + 2 \frac {u}{a} b ^ {2} - 2 \frac {u}{a} b \leq 0,
$$

or $b^2 \leq b$. Since $b$ is an integer, $b = 0$ or 1 and $A = 0$.

Suppose $b = 1$. Then (30.15) becomes

$$
\beta^ {\tau} = \left(\frac {u}{a} - 1\right) \lambda_ {1 1} ^ {\tau} - \sum_ {i \neq 1} \lambda_ {1 i} ^ {\tau} + \Gamma .\tag{30.17}
$$

As $\alpha, \beta$ vanish on $\mathfrak{S} - \widehat{\mathfrak{S}}$, we have

$$
\left(\alpha^ {\tau}, \beta^ {\tau}\right) = (\alpha , \beta) = - \frac {u}{a}.\tag{30.18}
$$

Since $(\alpha^{\tau},\lambda_{11}^{\tau} - \lambda_{1i}^{\tau}) = -1$ , we get that

$$
\alpha^ {\tau} = (x - 1) \lambda_ {1 1} ^ {\tau} + x \sum_ {i \neq 1} \lambda_ {1 i} ^ {\tau} + \Delta_ {0},\tag{30.19}
$$

for some integer $x$ and some $\Delta_0$ which is orthogonal to $\mathcal{S}_1$. Now (30.14), (30.17), (30.18) and (30.19) yield that

$$
- \frac {u}{a} = \left(\frac {u}{a} - 1\right) (x - 1) - x \left(2 \frac {u}{a} - 1\right).
$$

Reading this equality mod u/a, we get

$$
0 \equiv - (x - 1) + x \equiv 1 (\mathrm{mod} \frac {u}{a}).
$$

Thus $u = a$, contrary to Lemma 30.7. Hence, $b = 0$. Consequently $\beta^{\tau} = (u / a)\lambda_{11}^{\tau} + \Gamma$, and so $\Gamma = \pm \lambda_{2j}^{\tau}$ for some $j$. Since $(\beta^{\tau}, \lambda_{21}^{\tau} - \bar{\lambda}_{21}^{\tau}) \neq 0$, $\lambda_{2j} = \lambda_{21}$ or $\bar{\lambda}_{21}$. This implies directly that $S_1 \cup S_2$ is coherent. Lemma 13.10 and Theorem 10.1 now yield that $S(\mathfrak{S}')$ is coherent. The proof is complete.

## LEMMA 30.9. $\mathfrak{S}$ is of type II.

Proof. If $\mathfrak{S}$ is of type III or IV, then Theorem 29.1 yields that $\mathfrak{S}' = 1$. Thus, by Lemma 30.8, $\mathcal{S}$ is coherent. Hence, Hypothesis 30.2 implies that $\mathfrak{S}$ is of type II.

LEMMA 30.10. If $\mathcal{S}$ contains an irreducible character of degree $aq$, then Hypothesis 11.1 is satisfied with $\mathfrak{H}_0 = 1$, $\mathfrak{L} = \mathfrak{S}$, $\widehat{\mathfrak{L}} = \widehat{\mathfrak{S}}$, $\mathfrak{R} = \mathfrak{S}'$ and $d = a$.

Proof. By Theorem 14.2, Condition (i) is satisfied. Condition (ii) follows from the definition of three step group. Conditions (iii) and (vi) are immediate, while Condition (iv) holds by assumption. The group $\mathfrak{S}$ satisfies Hypothesis 13.2. Hence, by Theorem 14.2 Hypothesis 13.3 is satisfied with $\mathfrak{X} = \mathfrak{G}, \mathfrak{Y} = \mathfrak{S}, \hat{\mathfrak{X}} = \hat{\mathfrak{S}}$ and $\mathfrak{R} = \mathfrak{S}'$. By Lemmas 13.7, 13.9 and 13.10, Hypothesis 10.1 is satisfied. Thus, Lemma 10.1 yields that Condition (v) of Hypothesis 11.1 is satisfied. The proof is complete.

LEMMA 30.11. If S contains an irreducible character of degree aq, then

$$
\mid \mathfrak {H}: \mathfrak {H} ^ {\prime} \mid \leq 4 a ^ {2} q ^ {2} + 1.
$$

Proof. By Hypothesis 30.2, S is not coherent. Thus, Lemmas 30.8, 30.9, and 30.10, together with Theorem 11.1 yield the result.

LEMMA 30.12. For $1 \leq i \leq t$, $(a, p_i - 1) = 1$ and $\mathfrak{P}_i \mathfrak{U} / \mathfrak{C}_i$ is a Frobenius group.

Proof. Suppose that $a \mid (p_i - 1)$ for some $i$. Then Lemmas 30.2 and 30.11 yield that $p_i^q \leq 4a^2 q^2 + 1 \leq (p_i - 1)^2 q^2 + 1$. Thus, $p_i^{q-2} < q^2$. Therefore, (5.1) implies that $q = 3$. Hence, $p_i = 5$ or 7. Thus, $a$ divides 4 or 6. As $a$ is odd and $(a, q) = 1$, this implies that $a = 1$ which is not the case. Therefore, by Lemma 30.3, $\mathfrak{U}/\mathfrak{C}_i$ is cyclic of order $a$ for $1 \leq i \leq t$. If $\mathfrak{P}_i \mathfrak{U}/\mathfrak{C}_i$ were not a Frobenius group, then for some $b < a$, $\{U^b \mid U \in \mathfrak{U}\} = \mathfrak{U}_0$ would lie in $\widehat{\mathfrak{S}}$. Since $\mathfrak{U}_0 \neq 1$ and $\mathfrak{U}_0$ char $\mathfrak{U}$, this implies that $N(\mathfrak{U}) \subseteq N(\mathfrak{U}_0) \subseteq \mathfrak{S}$, contrary to Lemma 30.9.

LEMMA 30.13. $t = 1$, $p_1 = 3$, $a < 3^{q/2}$ and $\mathfrak{P}_1' = D(\mathfrak{P}_1)$.

Proof. By Lemma 30.8, $\mathfrak{P}' \neq 1$. Choose the notation so that $\mathfrak{P}_1' \neq 1$. Let $\mathfrak{P}_1 = \mathfrak{P}_{11} \supset \mathfrak{P}_{12} \cdots \supset \mathfrak{P}_{1n} = \mathfrak{P}_1' \supset \mathfrak{P}_{1,n+1}$, where $\mathfrak{P}_{1i}/\mathfrak{P}_{1,i+1}$ is a chief factor of $\mathfrak{S}$ for $1 \leq i \leq n$. Thus, $\mathfrak{P}_1/\mathfrak{P}_{1,n+1}$ is of class two and so is a regular $p$-group. By Lemma 4.6 (i) $\mathfrak{Q}^*$ centralizes an element of $\mathfrak{P}_{1i} - \mathfrak{P}_{1,i+1}$ for $1 \leq i \leq n$. Since $C_{\mathfrak{P}_1}(\mathfrak{Q}^*)$ is cyclic, this implies that $\mathfrak{P}_1/\mathfrak{P}_{1,n+1}$ has exponent $p^n$. Let $\mathfrak{U}/\mathfrak{G}_i = \langle U\rangle$. Then the regularity of $\mathfrak{P}_1/\mathfrak{P}_{1,n+1}$ yields that $U$ has the same minimal polynomial on $\mathfrak{P}_1/D(\mathfrak{P}_1)$ as on $\mathfrak{P}_1'/\mathfrak{P}_{1,n+1}$. Hence, by Lemma 6.2, $a < 3^{q/2}$. Now Lemma 30.11 implies that if $|\mathfrak{P}_1: \mathfrak{P}_1'| = p_1^{mq}$, then

$$
p _ {1} ^ {m q} \prod_ {i = 2} ^ {t} p _ {i} ^ {q} \leq 4. 3 ^ {q} q ^ {2} + 1.\tag{30.20}
$$

Since $3 \leq p_{1}$, (30.20) implies that

$$
p _ {1} ^ {(m - 1) q} \prod_ {i = 2} ^ {t} p _ {i} ^ {q} \leq 4 q ^ {2} + 1.
$$

Hence, by (5.9), $m = 1$ and $t = 1$. Thus, (30.20) becomes

$$
p _ {1} ^ {q} \leq 4. 3 ^ {q} q ^ {2} + 1.\tag{30.21}
$$

If $p_1 \geq 11$, (30.21) implies that

$$
3 ^ {q} <   \left(\frac {p _ {1}}{3}\right) ^ {q} \leq 4 q ^ {2} + 1.
$$

Thus, $3^{q-2} < q^2$ and so $q < 5$ by (5.1). Hence $q = 3$ and (30.21) yields $1331 = 11^3 < 4.3^5 + 1 < 1000$, which is not the case. If $p_1 = 7$, then (30.21) and (5.6) imply that $q < 7$. Thus, $q = 5$ or $q = 3$. If $q = 3$, then

$$
\frac {p _ {1} ^ {q} - 1}{p _ {1} - 1} = 5 7
$$

and $a < 3^{q/2} < 9$. Since $(q, a) = 1$ and $a \mid 57$, this cannot be the case. If $q = 5$, then

$$
\frac {p _ {1} ^ {q} - 1}{p _ {1} - 1} = 2 8 0 1
$$

is a prime. Thus $2801 = a < 3^{q/2} < 27$. Suppose now that $p_1 = 5$. Then by (5.7), $q < 13$. Thus, $q = 3, 7$, or 11. Let $r$ be a prime factor of $a$. Then $r < 3^{q/2}$ and $5^q \equiv 1 \pmod{r}$. Thus, $r \equiv 1 \pmod{2q}$. If $q = 3$, then $r \equiv 1 \pmod{6}$ and $r < 3^{3/2}$, which is impossible. If $q = 7$, then $r < 3^{7/2} < 50$ and $r \equiv 1 \pmod{14}$. Thus $r = 29$ or 43. Since $5^7 \equiv -1 \pmod{29}$ and $5^7 \equiv -6 \pmod{43}$, these cases cannot occur. If $q = 11$, then $r < 3^{11/2} < 437$ and $r \equiv 1 \pmod{22}$. Thus, $r = 23, 67, 89, 199, 331, 353, 397$, or 419. Since $5^{11} \equiv 1 \pmod{r}$, the quadratic reciprocity theorem implies that $(r|5) = 1$, so that $r \equiv \pm 1 \pmod{5}$. Thus, $r = 89, 199, 331$ or 419. Since $5^{11} \equiv 55 \pmod{89}$, $5^{11} \equiv 92 \pmod{199}$, $5^{11} \equiv -2 \pmod{331}$, $5^{11} \equiv -40 \pmod{419}$, these cases cannot occur. Hence, $p_1 = 3$, and the lemma is proved.

If $\mathcal{S}$ is not coherent, then Lemmas 30.8 and 30.12 imply that $|\mathfrak{W}_2|$ is not a prime. Hence, $\mathfrak{T}$ is of Type V. The other statements in Theorem 30.1 follow directly from Lemmas 30.9 and 30.13.

## 31. Characters of Subgroups of Type V

In this section $\mathfrak{T} = \mathfrak{T}'\mathfrak{W}_2$ is a subgroup of type V. Let $\mathfrak{S}$ be the subgroup of $\mathfrak{G}$ which satisfies condition (ii) of Theorem 14.1. By Theorem 14.1 (ii) (d) $\mathfrak{S}$ is of type II. The notation introduced at the beginning of Section 29 will be used.

$\mathcal{T}$ is the set of all characters of $\mathfrak{T}$ which are induced by non principal irreducible characters of $\mathfrak{T}'$. For any class function $\alpha$ of $\mathfrak{T}'$ let $\tilde{\alpha}$ be the class function of $\mathfrak{T}$ induced by $\alpha$.

For $0 \leq i \leq q - 1$, $0 \leq j \leq w_2 - 1$ let $\eta_{ij}$ be the generalized characters of $\mathfrak{G}$ defined by Lemma 13.1 and let $\nu_{ij}$ be the characters of $\mathfrak{T}$ defined by Lemma 13.3.

Hypothesis 13.2 is satisfied with $\mathfrak{L} = \mathfrak{T}$, $\mathfrak{R} = \mathfrak{T}'$ and $\mathfrak{W}_1$ replaced by $\mathfrak{W}_2$. By Lemma 13.7 $\mathfrak{T}'$ has exactly $q$ irreducible characters which induce reducible characters of $\mathfrak{T}$. Denote these by $\nu_i$ for $0 \leq i \leq q - 1$, where $\nu_0 = 1_{\mathfrak{T}'}$. Let $\zeta_i = \widetilde{\nu}_i$ for $0 \leq i \leq q - 1$. Since $q$ is a prime the characters $\nu_i$ are algebraically conjugate for $1 \leq i \leq q - 1$. Therefore

$$
\nu_ {i} (1) = \nu_ {1} (1) \quad \text { for } 1 \leq i \leq q - 1.
$$

LEMMA 31.1. $\mathcal{S}(\mathfrak{H}')$ contains an irreducible character of $\mathfrak{S}$ except possibly if $w$, is a prime and $\mathfrak{H}\mathfrak{U}$ is a Frobenius group.

Proof. If $\mathfrak{S}'$ is not a Frobenius group then there are strictly more than $w_{2}$ classes of $\mathfrak{S}' / \mathfrak{S}'$ whose order is not relatively prime to $\{\mathfrak{S}|$. The result now follows from Lemma 13.7.

Suppose that $\mathfrak{S}'$ is a Frobenius group. By Lemma 6.2 and 3.16 (iii) $\mathfrak{S}$ is abelian and $|\mathfrak{S}| = w_2^q$ if the result is false. Then Lemma 13.7 implies that $\mathfrak{S}'$ contains exactly $w_2 - 1$ conjugate classes which are in $\mathfrak{S}^{\sharp}$. Therefore

$$
\frac {| \mathfrak {S} | - 1}{u} = w _ {2} - 1.
$$

Hence

$$
u = \frac {| \mathfrak {H} | - 1}{w _ {2} - 1} = \frac {| \mathfrak {H} | - 1}{| \mathfrak {H} | ^ {1 / q} - 1} > \sqrt {| \mathfrak {H} |}.
$$

This implies that $\mathfrak{H}$ is an elementary abelian $p$-group for some prime $p$. Since $\mathfrak{W}_2$ is cyclic $w_2$ is a prime as required.

LEMMA 31.2. Let

$$
a _ {i j} = ((\nu_ {1} (1) \tilde {1} _ {\mathfrak {T} ^ {\prime}} - \zeta_ {i}) ^ {\tau}, \eta_ {0 j}) .
$$

Then $a_{ij} \neq 0$ for $1 \leq i \leq q - 1, 0 \leq j \leq w_2 - 1$.

Proof. Lemma 10.3 implies that by Lemma 9.4

$$
(\nu_ {1} (1) \tilde {1} _ {\mathfrak {T} ^ {\prime}} - \zeta_ {i}, \eta_ {0 j | \mathfrak {T}}) = ((\nu_ {1} (1) \tilde {1} _ {\mathfrak {T} ^ {\prime}} - \zeta_ {i}) ^ {\tau}, \eta_ {0 j}) = a _ {i j}.\tag{31.1}
$$

Since $\eta_{01}$ is rational on $\mathfrak{T}'$ by Lemma 13.1, $a_{ij} = a_j$ is independent of $i$. Thus (31.1) implies that

$$
\eta_ {0 j | \mathfrak {T} ^ {\prime}} = b \rho_ {\mathfrak {T} ^ {\prime}} - a _ {j} \sum_ {i = 1} ^ {q - 1} \nu_ {i 0 | \mathfrak {T} ^ {\prime}} + \alpha_ {| \mathfrak {T} ^ {\prime}},\tag{31.2}
$$

for some integer $b$, where $\alpha$ is an integral linear combination of irreducible characters of $\mathfrak{T}$ each of which vanishes on $\hat{\mathfrak{W}}$.

Let $Q \in \mathfrak{Q}^{*\#}$. Let $p$ be a prime dividing $w_2$, let $P$ be an element of order $p$ in $\mathfrak{W}_2$ and let $\mathfrak{p}$ be a prime divisor of $p$ in the ring of integers of $\mathcal{Q}_{|\mathfrak{G}|}$. Let $\omega_{ij}$ have the same meaning as in Hypothesis 13.1. Thus by Lemmas 13.1 and 13.3

$$
\eta_ {0 j} (P Q) = \omega_ {0 j} (P Q), \quad \alpha (P Q) = 0, \quad \nu_ {i 0} (P Q) = \varepsilon \omega_ {i 0} (P Q),\tag{31.3}
$$

where $\varepsilon = \pm 1$ is independent of $i$. Therefore

$$
\sum_ {i = 1} ^ {q - 1} \nu_ {i 0} (P Q) = \varepsilon \sum_ {i = 1} ^ {q - 1} \omega_ {i 0} (P Q) = \varepsilon \sum_ {i = 1} ^ {q - 1} \omega_ {i 0} (Q) = - \varepsilon .\tag{31.4}
$$

In view of Lemma 4.2 (31.3) and (31.4) imply that

$$
\begin{array}{r l} \eta_ {0 j} (Q) & \equiv \eta_ {0 j} (P Q) \equiv \omega_ {0 j} (P Q) \equiv \omega_ {0 j} (Q) \equiv 1 \pmod {\mathfrak {p}} \\ \sum_ {i = 1} ^ {q - 1} \nu_ {i 0} (Q) & \equiv - \varepsilon \pmod {\mathfrak {p}} \\ \alpha (Q) & \equiv \alpha (P Q) \equiv 0 \pmod {\mathfrak {p}}. \end{array}\tag{31.5}
$$

Thus (31.2) and (31.5) yield that $1 \equiv \varepsilon a_j \pmod{p}$. Thus $a_j \neq 0$ as required.

The main purpose of this section is to prove that T is coherent. Theorem 12.1 will play an important role in the proof of this fact. The lemmas in this section will from now on satisfy the following assumption.

Hypothesis 31.1.

$\mathcal{T}$ is not coherent.

By Grün's theorem $\mathfrak{T} / \mathfrak{T}''$ is a Frobenius group. Hence by Lemma 11.2 $\mathfrak{T}' = \mathfrak{Q}$ is a $q$-group. Define

$$
\left| \mathfrak {Q}: \mathfrak {Q} ^ {\prime} \right| = q ^ {b}, \quad \left| \mathfrak {T}: \mathfrak {Q} \right| = w _ {2} = e.\tag{31.6}
$$

Let $1 = q^{f_0} < q^{f_1} < \cdots$ be all the integers which are degrees of irreducible characters of $\mathfrak{D}$. Let

$$
\nu_ {1} (1) = q ^ {f _ {n}}, \quad n > 0.\tag{31.7}
$$

By Lemma 13.10 Hypothesis 12.1 is satisfied. Let $\mathcal{T}_s$ be defined by (12.3) for $0 \leq s \leq t$.

LEMMA 31.3. Suppose that $b = 2c$ for some integer $c$. Then $e$ is not a prime power.

Proof. Suppose that  $e = p^{h}$  for some prime p. Then by Lemma 11.5  $q^{c} + 1 = 2p^{h}$ ,  $f_{1} = c$  and Q contains a subgroup  $Q_{1}$  which is normal in T and satisfies  $|\mathfrak{Q}' : \mathfrak{Q}_{1}| = q$  and  $Q^{*} \subseteq Q - Q_{1}^{*}$ . Therefore n = 1 and T contains  $2(q^{c} - 1)$  irreducible characters  $\lambda_{1}, \lambda_{2}, \cdots$  of degree e. Define

$$
\alpha = \widetilde {1} _ {\Omega} - \lambda_ {1}, \quad \beta = q ^ {c} \lambda_ {1} - \zeta_ {1}.
$$

By Lemma 9.4 we have that

$$
\left\| \alpha^ {\tau} \right\| ^ {2} = e + 1, \quad \left\| \beta^ {\tau} \right\| ^ {2} = q ^ {2 c} + e, \quad \left(\alpha^ {\tau}, \beta^ {\tau}\right) = - q ^ {c}.\tag{31.8}
$$

Furthermore

$$
\begin{array}{l} \left(\alpha^ {\tau}, \lambda_ {i} ^ {\tau} - \lambda_ {j} ^ {\tau}\right) = \delta_ {j 1} - \delta_ {i 1}, \\ \left(\beta^ {\tau}, \lambda_ {i} ^ {\tau} - \lambda_ {j} ^ {\tau}\right) = q ^ {e} \left(\delta_ {i 1} - \delta_ {j 1}\right). \end{array}\tag{31.9}
$$

Suppose that $(\alpha^r, \lambda_i^r) \neq 0$ for some $i$ with $2 \leq i \leq 2(q^c - 1)$. Then (31.8) and (31.9) imply that

$$
\frac {q ^ {c} + 1}{2} + 1 = e + 1 = \left\| \alpha^ {\tau} \right\| ^ {2} \geq 1 + 2 (q ^ {c} - 1) - 1.
$$

Hence $q^c + 3 \geq 4q^c - 4$, or $7 \geq 3q^c$ which is not the case. Therefore

$$
\alpha^ {\tau} = 1 _ {\mathfrak {G}} - \lambda_ {i} ^ {\tau} + \Gamma , (\Gamma , \lambda_ {i} ^ {\tau}) = 0 \quad \text { for } 1 \leq i \leq 2 (q ^ {c} - 1)\tag{31.10}
$$

Equation (31.9) also yields that for some integer $x$

$$
\beta^ {\tau} = q ^ {c} \lambda_ {1} ^ {\tau} - x \sum_ {i = 1} ^ {2 (q ^ {c} - 1)} \lambda_ {i} ^ {\tau} + \Delta ,\tag{31.11}
$$

$$
(\lambda_ {i} ^ {\tau}, \Delta) = 0 \text {   for   } 1 \leq i \leq 2 (q ^ {c} - 1) .
$$

Furthermore Lemma 13.8 implies that for $2 \leq s \leq q - 1$,

$$
(\Delta , \zeta_ {s} ^ {\tau} - \zeta_ {1} ^ {\tau}) = (\beta^ {\tau}, \zeta_ {s} ^ {\tau} - \zeta_ {1} ^ {\tau}) = (\beta , \zeta_ {s} - \zeta_ {1}) = e.\tag{31.12}
$$

Since $\beta^{\mathrm{r}}$ vanishes on $\hat{\mathfrak{W}}$ and $(\beta^{\mathrm{r}},1_{\mathfrak{G}}) = 0$ Lemma 13.2 yields that

$$
\Delta = \sum_ {i = 1} ^ {q - 1} a _ {i 0} \sum_ {j = 0} ^ {e - 1} \eta_ {i j} + \sum_ {j = 1} ^ {e - 1} a _ {0 j} \sum_ {i = 0} ^ {q - 1} \eta_ {i j} + \Delta_ {0},\tag{31.13}
$$

where $(\Delta_0, \eta_{ij}) = 0$ for $0 \leq i \leq q - 1$, $0 \leq j \leq e - 1$. Now (31.12) and (31.13) imply that

$$
a _ {s 0} - a _ {1 0} = \pm 1 \quad \text { for } 2 \leq s \leq q - 1.
$$

Define $a = a_{20}$. Then (31.13) implies that

$$
\begin{array}{l} (a \pm 1) ^ {2} + (q - 2) a ^ {2} + \sum_ {j = 1} ^ {e - 1} a _ {0 j} ^ {2} \\ \quad + \sum_ {j = 1} ^ {e - 1} \{(a \pm 1 + a _ {0 j}) ^ {2} + (q - 2) (a + a _ {0 j}) ^ {2} \} \leq \| \Delta \| ^ {2}. \end{array}\tag{31.14}
$$

For any value of $j$ the term in the last summation in (31.14) is non zero. Furthermore $(a \pm 1)^2 + (q - 2)a^2 \neq 0$. Thus (31.14) implies that if there are exactly $k$ values of $j$ with $a_{0j} \neq 0$, then

$$
k + e \leq \| \Delta \| ^ {2}, k \text {   is   even. }\tag{31.15}
$$

The last statement follows from the fact that $(\eta_{0j},\Delta) = (\bar{\eta}_{0j},\Delta)$ since $\beta^{\tau}$ and thus $\Delta$ has its values in $\mathcal{Q}_{|\Omega|}$. By definition

$$
(q ^ {c} \widetilde {1} _ {\mathfrak {Q}} - \zeta_ {1}) ^ {\tau} = q ^ {c} (\widetilde {1} _ {\mathfrak {Q}} - \lambda_ {1}) ^ {\tau} + (q ^ {c} \lambda_ {1} - \lambda_ {1}) ^ {\tau} = q ^ {c} \alpha^ {\tau} + \beta^ {\tau}.
$$

Lemma 31.2 implies that for any value of $j$ with $1 \leq j \leq e - 1$

$$
\left(\alpha^ {\tau}, \eta_ {0 j}\right) \neq 0 \quad \text { or } \quad \left(\beta^ {\tau}, \eta_ {0 j}\right) \neq 0.\tag{31.16}
$$

Now (31.8), (31.11) and (31.15) yield that

$$
(q ^ {c} - x) ^ {2} + x ^ {2} \{2 (q ^ {c} - 1) - 1 \} \leq q ^ {2 c},
$$

or

$$
2 (q ^ {c} - 1) x ^ {2} \leq 2 q ^ {c} x.
$$

Therefore

$$
0 \leq x \leq \frac {q ^ {c}}{q ^ {c} - 1} <   2.
$$

Suppose that $x \neq 0$, then $x = 1$. Now (31.8) and (31.11) imply that $||\Delta||^2 \leq q^{2c} + e - \{(q^c - 1)^2 + 2(q^c - 1) - 1\} = e + 2$. By (31.15) this implies that $k = 0$ or $k = 2$. Assume first that $k = 0$, then (31.10) implies that $||\Gamma||^2 \leq e - 1$. Hence by (31.16)

$$
\Gamma = \sum_ {j = 1} ^ {e - 1} \pm \eta_ {0 j}.
$$

This implies that $(\beta^{\tau},\Gamma) = 0$ . Consequently (31.8), (31.10) and (31.11) yield that

$$
- q ^ {c} = \left(\alpha^ {\tau}, \beta^ {\tau}\right) = \left(- \lambda_ {1} ^ {\tau}, \beta^ {\tau}\right) = x - q ^ {c} = 1 - q ^ {c}
$$

which is not the case.

Assume now that $k = 2$. Choose $1', 2'$ with $1 \leq 1' < 2' \leq e - 1$ so that $a_{0j} \neq 0$ for $j = 1', 2'$. Thus $\eta_{01'} = \overline{\eta_{02'}}$, $a_{01'} = a_{02'} = \pm 1$ and by (31.16)

$$
\alpha^ {\tau} = 1 _ {\mathfrak {G}} - \lambda_ {1} ^ {\tau} + \sum_ {j \neq 1 ^ {\prime}, 2 ^ {\prime}, 0} \pm \eta_ {0 j} + \Gamma_ {0}, \| \Gamma_ {0} \| ^ {2} = 2.
$$

Since $\beta^{\tau}$ has its values in $\mathcal{Q}_{|\Omega|}$ and $\eta_{01'}$ has its values in $\mathcal{Q}_s$, $(\eta_{0j}, \beta^{\tau}) \neq 0$ for any algebraic conjugate $\eta_{0j}$ of $\eta_{01'}$. By Lemma 13.1 $\eta_{01'}$ has at least $(p - 1)$ algebraic conjugates. Hence $p = 3$, therefore $q \neq 3$. Since $\alpha^{\tau}$ vanishes on $\hat{\mathfrak{W}}$ Lemma 13.1 implies that for $1 \leq s \leq q - 1$

$$
0 = \left(\alpha^ {\tau}, 1 _ {③} - \eta_ {s 0} - \eta_ {0 1 ^ {\prime}} + \eta_ {s 1 ^ {\prime}}\right) = 1 + \left(\Gamma_ {0}, - \eta_ {s 0} + \eta_ {s 1 ^ {\prime}}\right) - \left(\Gamma_ {0}, \eta_ {0 1 ^ {\prime}}\right).
$$

Hence if $(\Gamma_0, \eta_{01'}) = 0$ then

$$
2 = \left\| \Gamma_ {0} \right\| ^ {2} \geq (q - 1) > 2.
$$

Therefore $(\Gamma_0, \eta_{01'}) \neq 0$. Hence

$$
\Gamma = \sum_ {j = 1} ^ {e - 1} \pm \eta_ {0 j}.
$$

Consequently (31.8), (31.10) and (31.11) yield that

$$
- q ^ {c} = \left(\alpha^ {\tau}, \beta^ {\tau}\right) = \left(- \lambda_ {1} ^ {\tau}, \beta^ {\tau}\right) \pm 2 = x - q ^ {c} \pm 2 = 1 - q ^ {c} \pm 2.
$$

The assumption that  $x \neq 0$  has led to a contradiction in all cases. Therefore (31.8), (31.11) and (31.15) imply that

$$
\beta^ {\tau} = q ^ {c} \lambda_ {1} ^ {\tau} + \Delta , \quad \| \Delta \| ^ {2} = e.
$$

Thus $a_{0j} = 0$ for $1 \leq j \leq e - 1$. Thus (31.14) implies that

$$
(a \pm 1) ^ {2} e + (q - 2) a ^ {2} e \leq e.
$$

Hence $a=0$ or $q=3$ and $a\pm1=0$. Thus $\beta^{\tau}=q^{o}\lambda_{1}^{\tau}-\zeta_{1}^{\tau}$ or $q=3$ and $\beta^{\tau}=q^{o}\lambda_{1}^{\tau}+\zeta_{2}^{\tau}$. In either case this implies that the set of characters consisting of $\lambda_{i},1\leqq i\leqq 2(q^{c}-1)$ and $\zeta_{s},1\leqq s\leqq q-1$ is coherent. This includes all characters in $\mathcal{T}$ which have $\mathfrak{Q}_{1}$ in their kernel. Since $|\mathfrak{Q}:\mathfrak{Q}_{1}|=q^{2c+1}>4p^{2b}$ the result now follows from Theorem 11.1 with $\mathfrak{Q}=\hat{\mathfrak{Q}}=\mathfrak{R}=\mathfrak{Q},\mathfrak{Q}_{1}=\mathfrak{Q}_{1}$ and $\mathfrak{Q}=\mathfrak{X}$.

LEMMA 31.4. S is coherent.

Proof. By Theorem 30.1 $w_{2}$ is a power of 3 if $\mathcal{S}$ is not coherent. By Lemma 31.3 $b$ is odd. Thus the lemma follows from Lemma 11.6.

LEMMA 31.5. For $0 \leq i \leq n - 1$ let $\lambda_i$ be an irreducible character of $\mathfrak{T}$ with $\lambda_i(1) = eq^{r_i}$. Let $\mathfrak{D}_0$ be the normal closure of $\mathfrak{Q}^*$ in $\mathfrak{T}$. Let $1 = q^{g_0} < \cdots < q^{g_m}$ be all the degrees of irreducible characters of $\mathfrak{D}/\mathfrak{D}_0$. Then $\mathfrak{T}/\mathfrak{D}_0$ is a Frobenius group. For any value of $j$ with $0 \leq j \leq m$ let $\theta_j$ be an irreducible character of $\mathfrak{T}/\mathfrak{D}_0$ of degree $eq^{g_j}$. Define

$$
\alpha = \widetilde {1} _ {\Omega} - \lambda_ {0},
$$

$$
\beta_ {i} = q ^ {f _ {i} - f _ {i - 1}} \lambda_ {i - 1} - \lambda_ {i} \quad f o r 1 \leq i \leq n - 1,
$$

$$
\gamma_ {j} = q ^ {q _ {j} - q _ {j - 1}} \theta_ {j - 1} - \theta_ {j} \quad f o r 1 \leq j \leq m.
$$

Then

$$
\left(\beta_ {i} ^ {\tau}, \eta_ {0 t}\right) = 0 \quad f o r 0 \leq t \leq e - 1, 1 \leq i \leq n - 1,
$$

$$
\left(\gamma_ {j} ^ {\tau}, \eta_ {0 t}\right) = 0 \quad f o r 0 \leq t \leq e - 1, 1 \leq j \leq m.
$$

Furthermore if e is a prime then one of the following possibilities must occur:

$$
\alpha^ {\tau} = 1 _ {\mathfrak {G}} - \lambda_ {0} ^ {\tau} + \sum_ {t = 1} ^ {e - 1} \eta_ {0 t},
$$

$$
\alpha^ {\tau} = 1 _ {\mathfrak {G}} + \bar {\lambda} _ {0} ^ {\tau} + \sum_ {t = 1} ^ {e - 1} \eta_ {0 t} a n d 2 e + 1 = | \mathfrak {Q}: \mathfrak {Q} ^ {\prime} |,
$$

$$
\alpha^ {\tau} = 1 _ {\mathfrak {G}} + \sum_ {s = 1} ^ {q - 1} \eta_ {s 0} + \Gamma ,
$$

with $(\Gamma, \eta_{st}) = 0$ for $0 \leq s \leq q - 1$, $0 \leq t \leq e - 1$.

Proof. For $1 \leq i \leq n - 1, 1 \leq j \leq m$ let

$$
\alpha^ {\tau} = \Gamma_ {0 0} + \Delta_ {0 0}, \quad \beta_ {i} ^ {\tau} = \Gamma_ {i 0} + \Delta_ {i 0}, \quad \gamma_ {j} ^ {\tau} = \Gamma_ {0 j} + \Delta_ {0 j},
$$

where each $\Delta_{ij}$ is a linear combination of the generalized characters $\eta_{st}$ and each $\Gamma_{ij}$ is orthogonal to each of these generalized characters. Since for $1 \leq s \leq q - 1$, $(\zeta_s - \zeta_1)^r$ is orthogonal to $\alpha^r$, $\beta_i^r$ and $\gamma_j^r$ and all of these vanish on $\hat{\mathfrak{W}}$, Lemma 13.2 implies that

$$
\Delta_ {i j} = a _ {0 0} 1 _ {\mathfrak {G}} + a \sum_ {s = 1} ^ {q - 1} \sum_ {t = 0} ^ {s - 1} \eta_ {s t} + \sum_ {t = 1} ^ {s - 1} a _ {0 t} \sum_ {s = 0} ^ {q - 1} \eta_ {s t} - a _ {0 0} \sum_ {s = 1} ^ {q - 1} \sum_ {t = 1} ^ {s - 1} \eta_ {s t},\tag{31.17}
$$

where $\{a\} \cup \{a_{st}\}$ is a set of integers depending on $(i,j)$. Since $(\lambda_0^\tau - \overline{\lambda}_0^\tau, \alpha^\tau) \neq 0$, $||\Delta_{00}||^2 \leq e$. Since $(\lambda_i^\tau - \overline{\lambda}_i^\tau, \beta_i^\tau) \neq 0$, $(\theta_j^\tau - \bar{\theta}_j^\tau, \gamma_j^\tau) \neq 0$, Theorem 12.1 implies that

$$
\left\| \Delta_ {i j} \right\| ^ {2} \leq e \quad \text { for   all } (i, j) .\tag{31.18}
$$

Assume first that $(i,j)\neq (0,0)$. Then $a_{00} = 0$. Thus (31.17) and (31.18) imply that

$$
(q - 1) a ^ {2} + (q - 1) \sum_ {t = 1} ^ {e - 1} (a + a _ {0 t}) ^ {2} + \sum_ {t = 1} ^ {e - 1} a _ {0 t} ^ {2} \leq e.
$$

If $a \neq 0$ then for each value of $t$ either $a_{0t} \neq 0$ or $a + a_{0t} \neq 0$. Thus $(q - 1)a^2 \leq 1$ which is not the case. Hence $a = 0$ and so

$$
\Delta_ {i j} = \sum_ {t = 1} ^ {s - 1} a _ {0 t} \sum_ {s = 0} ^ {q - 1} \eta_ {s t}.\tag{31.19}
$$

As $\mathcal{I}_0(\mathcal{S})^\tau$ is orthogonal to $\mathcal{I}_0(\mathcal{T})^\tau$ Lemma 31.4 yields that for all $(i,j)$

$$
(\xi_ {k} (1) \xi_ {k ^ {\prime}} ^ {\tau} - \xi_ {k ^ {\prime}} (1) \xi_ {k} ^ {\tau}, \Delta_ {i j}) = 0 \quad \text { for } 1 \leq k, k ^ {\prime} \leq e - 1.
$$

By (31.19) $(\Delta_{ij},\xi_k^{\tau}) = \pm a_{0k}q$ Hence

$$
\xi_ {k} (1) a _ {0 k ^ {\prime}} - \xi_ {k ^ {\prime}} (1) a _ {0 k} = 0.
$$

Suppose now that $a_{0t} \neq 0$ for some $t$. Then $a_{0t} \neq 0$ for all $t$ with $1 \leq t < e$. Hence (31.18) and (31.19) imply that

$$
q (e - 1) \leqq q \sum_ {t = 1} ^ {e - 1} a _ {0 t} ^ {2} \leqq e
$$

which is not the case. The result is proved in case  $(i, j) \neq (0, 0)$ .

Let $(i,j) = (0,0)$. Then $a_{00} = 1$. By assumption $\xi_k(1) = \xi_1(1)$ for $1 \leq k \leq e - 1$, since $e$ is a prime. By (31.17)

$$
\left(\Delta_ {0 0}, \xi_ {k} ^ {\tau}\right) = \pm \{a (q - 1) + a _ {0 k} q - a _ {0 0} (q - 1) \}, \quad \text { for } 1 \leq k \leq e - 1
$$

where the sign is independent of $k$. Since $(\Delta_{00}, \xi_k^r - \xi_1^r) = 0$ this yields that $a_{0k} = a_{01}$ for $1 \leq k \leq e - 1$. Hence (31.17) and (31.18) imply that

$$
(q - 1) a ^ {2} + (e - 1) a _ {0 1} ^ {2} + (e - 1) (q - 1) (a + a _ {0 1} - 1) ^ {2} \leq e - 1.
$$

If $a_{01} \neq 0$ this yields that $a = 0$ and $a_{01} = 1$ and the result follows. If $a_{01} = 0$ then we get that

$$
(q - 1) a ^ {2} + (e - 1) (q - 1) (a - 1) ^ {2} \leq e - 1.
$$

Hence $a = 1$ and the result is proved also in this case.

LEMMA 31.6. Let $\lambda = \lambda_{n-1}$ have the same meaning as in Lemma 31.5. Define

$$
\beta_ {n} = \beta = q ^ {f _ {n} - f _ {n - 1}} \lambda - \zeta_ {1}.
$$

Then $(\beta^{\tau},\eta_{0t}) = 0$ for $0\leq t\leq e - 1$

Proof. Let $\mathcal{T}_b$ be the equivalence class in $\mathcal{T}$ defined by (12.3) which contains $\lambda$. If $\zeta_1$ is in $\mathcal{T}_b$ then the result follows from the coherence of $\mathcal{T}_b$. For any $i$, let $a_i / e$ be the number of characters of degree $q^{f_i}e$ in $\mathcal{T}_b$ and define $c$ as in (12.4) by

$$
c = \sum_ {i} a _ {i} q ^ {2 (f _ {i} - f _ {m})},\tag{31.20}
$$

where  $q^{fme}$  is the minimum degree of any character in  $T_{b}$ .

Let

$$
\beta^ {\tau} = \Delta_ {0} + \Delta + \Gamma ,\tag{31.21}
$$

where $\Delta_0 \in \mathcal{I}(\mathcal{T}_b^\tau)$, $\Delta$ is an integral linear combination of the generalized characters $\eta_{st}$ and $\Gamma$ is orthogonal to $\mathcal{T}_b^\tau$ and to every $\eta_{st}$. Theorem 12.1 yields that

$$
\| \Delta \| ^ {2} + \| \Gamma \| ^ {2} \leq 2 e.\tag{31.22}
$$

$\beta^{\tau}$ vanishes on $\hat{\mathfrak{W}}$ and $(\beta^{\tau}, 1_{\mathfrak{G}}) = 0$. Furthermore $(\zeta_{s}^{\tau} - \zeta_{i}^{\tau}, \Delta) = e$ for $2 \leq s \leq q - 1$. Therefore Lemma 13.2 implies that

$$
\Delta = \varepsilon \sum_ {t = 0} ^ {s - 1} \eta_ {1 t} + a _ {1 0} \sum_ {s = 1} ^ {q - 1} \sum_ {t = 0} ^ {s - 1} \eta_ {s t} + \sum_ {t = 1} ^ {s - 1} a _ {0 t} \sum_ {s = 0} ^ {q - 1} \eta_ {s t},\tag{31.23}
$$

where $\varepsilon = \pm 1$.

Since $\mathcal{I}_0(\mathcal{S})^r$ is orthogonal to $\mathcal{I}_0(\mathcal{T})^r$. Lemma 31.4 yields that

$$
(\xi_ {k} (1) \xi_ {k ^ {\prime}} ^ {\tau} - \xi_ {k ^ {\prime}} (1) \xi_ {k} ^ {\tau}, \Delta) = 0 \quad \text { for } 1 \leq k, k ^ {\prime} \leq e - 1.
$$

By (31.23)

$$
(\xi_ {k} ^ {\tau}, \Delta) = \pm \{\varepsilon + (q - 1) a _ {1 0} + q a _ {0 k} \},
$$

where the sign is independent of k. Therefore

$$
\xi_ {k} (1) \{\varepsilon + (q - 1) a _ {1 0} + q a _ {0 k ^ {\prime}} \} = \xi_ {k ^ {\prime}} (1) \{\varepsilon + (q - 1) a _ {1 0} + q a _ {0 k} \}
$$

for $1 \leq k, k' \leq e$. By (31.22) and (31.23) we see that

$$
\begin{array}{r l} \sum_ {t = 1} ^ {\epsilon - 1} a _ {0 t} ^ {2} + (a _ {1 0} + \varepsilon) ^ {2} + (q - 2) a _ {1 0} ^ {2} + \sum_ {t = 1} ^ {\epsilon - 1} (\varepsilon + a _ {1 0} + a _ {0 t}) ^ {2} \\ & + (q - 2) \sum_ {t = 1} ^ {\epsilon - 1} (a _ {1 0} + a _ {0 t}) ^ {2} = | | \Delta | | ^ {2} \leq 2 e. \end{array}\tag{31.24}
$$

If $a_{10} \neq 0$ and $a_{10} + \varepsilon \neq 0$ then for each $t$ at most one of $a_{0t}, a_{10} + a_{0t} \varepsilon + a_{10} + a_{0t}$ vanishes. Hence (31.24) yields that

$$
(a _ {1 0} + \varepsilon) ^ {2} + (q - 2) a _ {1 0} ^ {2} \leq 2.
$$

This is impossible as either  $a_{10}$  or  $a_{10} + \varepsilon$  is even. If  $a_{10} \neq 0$  then (31.24) implies that

$$
2 \sum_ {t = 1} ^ {e - 1} a _ {0 t} ^ {2} + (q - 2) + (q - 2) \sum_ {t = 1} ^ {e - 1} (a _ {0 t} - \varepsilon) ^ {2} \leq 2 e.
$$

If $q \neq 3$, then $2a_{0t}^2 + (q - 2)(a_{0t} - \varepsilon)^2 \geq 2$ for $1 \leq t < e$. Hence $q - 2 \leq 2$ which is not the case. Thus $a_{10} = 0$ or $q = 3$ and $a_{10} + \varepsilon = 0$. Thus we get

$$
\begin{array}{c} (\xi_ {k}, \Delta) = \pm \{\pm \varepsilon + q a _ {0 k} \} \\ \xi_ {k} (1) \{\pm \varepsilon + q a _ {0 k ^ {\prime}} \} = \xi_ {k ^ {\prime}} (1) \{\pm \varepsilon + q a _ {0 k} \} \quad \text { for } 1 \leq k, k ^ {\prime} <   e. \end{array}\tag{31.25}
$$

Assume that the result is false. Then $a_{0t} \neq 0$ for some value of $t$. We will next show that $a_{0t} \neq 0$ for $1 \leq t < e$. If this is false then there exists $j$ such that $a_{0j} = 0$. If $\gamma$ is any character in $\mathcal{S}$ then $(\gamma(1)\xi_j^\tau - \xi_j(1)\gamma^\tau, \Delta + \Gamma) = 0$. Thus (31.25) implies that

$$
(\gamma^ {\tau}, \Delta + \Gamma) = \frac {\pm \gamma (1)}{\xi_ {j} (1)}.\tag{31.26}
$$

Thus $\xi_j(1) | \gamma(1)$ for every $\gamma$ in $\mathcal{S}$. Let $a$ be the exponent of $\mathfrak{U}$. By Lemmas 30.1, 30.4 and 30.5 $\xi_j(1) = aq$. Thus $\mathfrak{X}'$ is in the kernel of $\xi_j$. Define

$$
\sigma = \{t \mid 1 \leq t <   e, \xi_ {t} (1) \neq \xi_ {j} (1) \}.
$$

By (31.25)

$$
a _ {0 t} = \frac {\pm \{\xi_ {t} (1) - \xi_ {j} (1) \}}{q \xi_ {j} (1)} \text { for } 1 \leq t <   e.
$$

Thus (31.22), (31.23) and (31.26) yield that

$$
2 e (a q) ^ {2} \geq \Sigma \gamma (1) ^ {2} + \frac {1}{q ^ {2}} \sum_ {t = 1} ^ {s - 1} \{\xi_ {t} (1) - \xi_ {j} (1) \} ^ {2} \geq \sum \gamma (1) ^ {2} + \frac {x}{q ^ {2}} \sum_ {t \in \sigma} \xi_ {t} (1) ^ {2},
$$

where $x = 4/9$ if $q \neq 3$ and $x = 16/25$ if $q = 3$, and $\gamma$ ranges over the irreducible characters in $\mathcal{S}$. By Lemma 13.7 there exist irreducible characters $\mu_t$ of $\mathfrak{S}'$ which induce the characters $\xi_t$ for $1 \leq t < e$. Consequently

$$
2 e a ^ {2} q \geq \sum \chi (1) ^ {2} + x \sum_ {i \in \sigma} \mu_ {i} (1) ^ {2} \geq x \left\{\sum \chi (1) ^ {2} + \sum_ {i \in \sigma} \mu_ {i} (1) ^ {2} \right\}
$$

where $\chi$ ranges over the irreducible characters of $\mathfrak{S}'$ which are distinct from all $\mu_t$ and do not have $\mathfrak{S}$ in their kernel. Therefore $C(\mathfrak{S}) \subseteq \mathfrak{S}$ otherwise since $|\mathfrak{G}|$ is odd there are at least 2 eq characters $\chi$ of degree at least $a$. Furthermore

$$
2 e a ^ {2} q \geq x \{u (h - 1) - a ^ {2} (e - 1) \}.
$$

This implies that

(31.27)

$$
y e q a ^ {2} \geq \left\{\frac {2 e q}{x} + e - 1 \right\} a ^ {2} \geq u (h - 1),
$$

where $y=4$ if $q=3$ and $y=5$ otherwise. Let $1\subset\mathfrak{H}_{1}\subset\mathfrak{H}$, where $\mathfrak{H}_{1}\triangleleft\mathfrak{S}$. Let $h_{1}=|\mathfrak{H}_{1}|, h_{2}=|\mathfrak{H}:\mathfrak{H}_{1}|, e_{1}=|C_{\mathfrak{H}_{1}}(\mathfrak{Q}^{*})|$ and $e_{2}=|C_{\mathfrak{H}/\mathfrak{H}_{1}}(\mathfrak{Q}^{*})|$. Since $\mathfrak{S}$ is of type II $ae_{1}<2h_{1}$ and $a\leqq u$. Thus (31.27) implies that $h_{2}-1\leqq 2yqe_{2}$. Since $h_{2}\geqq p^{q-1}e_{2}$ for some prime $p$ dividing $h_{2}$ we get that $p^{q-1}\leqq 2yq$. Thus $q=3$ by (5.1). Hence $p^{2}\leqq 24$ which is not the case as $p\geqq 5$. Hence no such group $\mathfrak{H}_{1}$ exists. Thus $\mathfrak{S}$ is an elementary abelian $p$-group for some prime. Therefore $e=p$ is a prime and $\xi_{t}(1)=\xi_{1}(1)$ for $1\leqq t<e$. Consequently $a_{0t}=a_{0j}=0$ for $1\leqq t<e$ contrary to assumption.

Returning to (31.24) we see that

$$
\sum_ {t = 1} ^ {e - 1} a _ {0 t} ^ {2} \leq e + 1.
$$

Therefore $a_{0t}^{2}=1$ for $1\leq t\leq e-1$. Thus

$$
a _ {0 t} = \pm 1 \quad \text { for } 1 \leq t \leq e - 1.\tag{31.28}
$$

Now (31.24) implies that

$$
\begin{array}{r l} (a _ {1 0} + \varepsilon) ^ {2} + (q - 2) a _ {1 0} ^ {2} \\ & + (e - 1) \{(a _ {1 0} + \varepsilon + a _ {0 1}) ^ {2} + (q - 2) (a _ {1 0} + a _ {0 1}) ^ {2} \} \\ & \leq e + 1, \end{array}\tag{31.29}
$$

Suppose that $q \neq 3$. Thus $q \geq 5$ and $a_{10} = 0$. Then (31.29) implies that $(e - 1)(q - 2) \leq e + 1$. As $q \geq 5$ this implies that $3e - 3 \leq e + 1$ or $e \leq 2$ which is not the case. Therefore

$$
q = 3.\tag{31.30}
$$

By (31.29) either $a_{10} = 0$, $a_{01} = -(a_{10} + \varepsilon)$ or $a_{10} + \varepsilon = 0$, $a_{01} = -a_{10}$. Now (31.23) and (31.28) imply that

$$
\Delta = \pm \left\{\sum_ {t = 0} ^ {s - 1} \eta_ {1 t} - \sum_ {t = 1} ^ {s - 1} \sum_ {s = 0} ^ {2} \eta_ {s t} \right\}
$$

or

$$
\Delta = \pm \left\{\sum_ {t = 0} ^ {s - 1} \eta_ {2 t} - \sum_ {t = 1} ^ {s - 1} \sum_ {s = 0} ^ {2} \eta_ {s t} \right\}.
$$

This is equivalent to

$$
\Delta = \pm \left\{\eta_ {1 0} - \sum_ {t = 1} ^ {s - 1} \left(\eta_ {0 t} + \eta_ {2 t}\right) \right\}
$$

(31.31) or

$$
\Delta = \pm \left\{\eta_ {2 0} - \sum_ {t = 1} ^ {s - 1} \left(\eta_ {0 t} + \eta_ {1 t}\right) \right\}:
$$

Since $(\beta^{\tau} - \overline{\beta}^{\tau},\Gamma) = 0,\Gamma$ is a real valued generalized character. Thus $\| \Gamma \| ^2\neq 1$ . By (31.31) $\| \Delta \| ^2 = 2e - 1$ , hence by (31.22) $\Gamma = 0$ . Now (31.21) implies that

$$
\beta^ {\tau} = q ^ {J _ {n} - J _ {n - 1}} \lambda^ {\tau} - x \sum_ {i = m} ^ {n - 1} \sum_ {j = 1} ^ {a _ {i} / a} q ^ {J _ {i} - J _ {m}} \lambda_ {i j} ^ {\tau} + \Delta ,\tag{31.32}
$$

where for  $m \leq i \leq n - 1$ ,  $\lambda_{ij}$  ranges over the characters of degree  $eq^{f_i}$  in  $T_b$ .

Suppose that S contains an irreducible character  $\gamma$ . Then by Lemma 31.4

$$
(\gamma (1) \xi_ {t} ^ {\tau} - \xi_ {t} (1) \gamma^ {\tau}, \beta^ {\tau}) = 0 \quad \text { for } 1 \leq t \leq e - 1.
$$

As $\gamma^{\tau}$ is rational valued on elements of $\mathfrak{Q},\gamma^{\tau}\neq\lambda_{ij}^{i}$ for all $i,j$. Thus (31.31) and (31.32) imply that

$$
\pm 2 \gamma (1) = (\gamma (1) \xi_ {t} ^ {\tau}, \beta^ {\tau}) = (\xi_ {t} (1) \gamma^ {\tau}, \beta^ {\tau}) = 0.
$$

Therefore S contains no irreducible characters. Hence by Lemma 31.1

$$
e = p, \quad p \text {   a   prime.   }\tag{31.33}
$$

Now Lemma 31.3 implies that $b$ is odd, where $b$ is defined in (31.6). As $||\Delta ||^2 = 2p - 1 > 2p - 2$ Theorem 12.1 implies that if $c$ is

defined in (31.20) then

$$
c \equiv 0 (\mathrm{mod} q) \quad \text { or } c \geq p ^ {2}.\tag{31.34}
$$

Assume first that $m \neq 0$ in (31.32). Let $\alpha$ be defined as in Lemma 31.5. Suppose that

$$
\alpha^ {\tau} = 1 _ {\mathfrak {G}} \pm \lambda_ {0} ^ {\tau} + \sum_ {t = 1} ^ {p - 1} \eta_ {0 t}.
$$

Then (31.31) and (31.32) yield that

$$
0 = (\alpha^ {\tau}, \beta^ {\tau}) = \pm (p - 1) .
$$

Thus by Lemma 31.5

$$
\alpha^ {\tau} = 1 _ {\mathfrak {G}} \pm \lambda_ {0} ^ {\tau} + \sum_ {s = 1} ^ {2} \eta_ {s 0} + \Gamma_ {0}, \| \Gamma_ {0} \| ^ {2} \leq p - 3.\tag{31.35}
$$

Then

$$
\Gamma_ {0} = \Gamma_ {0 0} + y \sum_ {i = m} ^ {n - 1} \sum_ {j = 1} ^ {\alpha_ {i} / p} q ^ {f _ {i} - f _ {m}} \lambda_ {i j} ^ {\tau},\tag{31.36}
$$

where  $(\Gamma_{00}, \lambda_{ij}^{\tau}) = 0$  for  $m \leq i \leq n - 1$ ,  $1 \leq j \leq (a_{i}/p)$ . Suppose that y = 0. Then (31.31), (31.32) and (31.36) yield that  $0 = (\alpha^{\tau}, \beta^{\tau}) = \pm 1$ . Hence  $y \neq 0$ . Thus by (31.35) and (31.36)

$$
(p - 3) \geq y ^ {2} \frac {c}{p} \geq \frac {c}{p}.
$$

Thus (31.34) yields that

$$
\boldsymbol {c} \equiv 0 (\mathrm{mod} q).\tag{31.37}
$$

Equations (31.31), (31.32), (31.35) and (31.36) imply that

$$
0 = \left(\alpha^ {\tau}, \beta^ {\tau}\right) = \pm 1 + y q ^ {f _ {n} - f _ {n - 1}} q ^ {f _ {n - 1} - f _ {m}} - x y \frac {c}{p}.
$$

Hence (31.37) implies that $0 \equiv \pm 1 \pmod{q}$. This contradiction arose from assuming $m \neq 0$.

Assume now that $m = 0$. Then

$$
c = q ^ {b} - 1 + \sum_ {i = 1} ^ {n - 1} a _ {i} q ^ {2 f _ {i}}.
$$

Hence $c \not\equiv 0 \pmod{q}$. Thus (31.34) and 3.15 imply that

$$
c \geq p ^ {2}, \quad c + 1 \equiv 0 (\mathrm{mod} q ^ {2 f _ {n}}).\tag{31.38}
$$

Now (31.31) and (31.32) yield that

$$
q ^ {2 (f _ {n} - f _ {n - 1})} + p = | | \beta^ {\tau} | | ^ {2} = q ^ {2 (f _ {n} - f _ {n - 1})} - 2 x q ^ {f _ {n}} + x ^ {2} \frac {c}{p} + 2 p - 1.
$$

Therefore

$$
x ^ {2} c + p (p - 1) = 2 x q ^ {f _ {n}} p.\tag{31.39}
$$

By (31.38), $(c + 1) > pq^{f_n}$. Thus (31.39) yields that

$$
f (x) = x ^ {2} \left(p q ^ {f _ {n}} - 1\right) - 2 x q ^ {f _ {n}} p + p (p - 1) <   0.
$$

It is easily verified that $f(x)$ is a monotone increasing function for $x \geq 2$ and $f(2) = p(p - 1) - 4 > 0$. Thus $x < 2$. By (31.39) $x > 0$. Hence $x = 1$. Now (31.39) becomes

$$
c + p (p - 1) = 2 q ^ {f _ {n}} p,
$$

or equivalently

$$
p ^ {2} - p (1 + 2 q ^ {f _ {n}}) + c = 0.\tag{31.40}
$$

Therefore $(1 + 2q^{f_n})^2 - 4c \geq 0$, hence

$$
4 c \leq 4 q ^ {2 f _ {n}} + 4 q ^ {f _ {n}} + 1 <   8 q ^ {2 f _ {n}}.
$$

Thus $c < 2q^{2f_n}$. As $c$ is even, (31.38) now yields that $c = q^{2f_n} - 1$. Now (31.40) becomes

$$
q ^ {2 f _ {n}} - 2 q ^ {f _ {n}} p + p ^ {2} - p - 1 = 0,
$$

or

$$
(q ^ {f _ {n}} - p - 1) (q ^ {f _ {n}} - p + 1) = p.
$$

As p is a prime one of the factors is  $\pm1$  and the other is  $\pm p$ . As the factors differ by 2 this implies that  $p \pm 1 = 2$ . Hence p = 3. Since  $p \neq q$  (31.30) implies that  $p \neq 3$ . This contradiction establishes the lemma in all cases.

THEOREM 31.1. T is coherent.

Proof. Suppose that $\mathcal{T}$ is not coherent so that Hypothesis 31.1 is assumed. Let $\alpha, \beta_i, \gamma_j, \lambda_i, \theta_j$ have the same meaning as in Lemmas 31.5 and 31.6. Choose $\lambda_0 = \theta_0$. Then

(31.41)

$$
(q ^ {f _ {n}} \widetilde {1} _ {\Omega} - \zeta_ {1}) ^ {\tau} = q ^ {f _ {n}} \alpha^ {\tau} + \sum_ {i = 1} ^ {n} q ^ {f _ {n} - f _ {i}} \beta_ {i} ^ {\tau}.\tag{31.42}
$$

$$
(q ^ {f _ {n}} \lambda_ {0} - \zeta_ {1}) ^ {\tau} = \sum_ {i = 1} ^ {n} q ^ {f _ {n} - f _ {i}} \beta_ {i} ^ {\tau}.\tag{31.43}
$$

$$
(q ^ {g _ {j}} \theta_ {0} - \theta_ {j}) ^ {\tau} = \sum_ {s = 1} ^ {j} q ^ {g _ {j} - g _ {s}} \gamma_ {s} ^ {\tau} \quad \text { for } 1 \leq j \leq m.
$$

Lemmas 31.2, 31.5 and 31.6 together with (31.41) imply that

$$
\alpha^ {\tau} = 1 _ {\mathfrak {G}} - \lambda_ {0} ^ {\tau} + \sum_ {t = 1} ^ {e - 1} \eta_ {0 t}
$$

or

$$
\alpha^ {\tau} = 1 _ {\mathfrak {G}} + \overline {{\lambda}} _ {0} ^ {\tau} + \sum_ {t - 1} ^ {e - 1} \eta_ {0 t}
$$

and $2e + 1 = |\mathfrak{Q}:\mathfrak{Q}'|$. If the latter possibility occurs then by Lemma 10.1 it may be assumed after changing notation that in any case

$$
\alpha^ {\tau} = 1 _ {\mathfrak {G}} - \lambda_ {0} ^ {\tau} + \sum_ {t = 1} ^ {e - 1} \eta_ {0 t}.\tag{31.44}
$$

Now Lemma 31.5, (31.43) and (31.44) imply that

$$
\begin{array}{r l} - q ^ {g _ {s}} & = (\alpha^ {\tau}, (q ^ {g _ {s}} \theta_ {0} - \theta_ {s}) ^ {\tau}) \\ & = (- \theta_ {0} ^ {\tau}, (q ^ {g _ {s}} \theta_ {0} - \theta_ {s}) ^ {\tau}), \quad \text { for } 1 \leqq s \leqq m. \end{array}\tag{31.45}
$$

Since $||(q^{0s}\theta_0 - \theta_s)^{\tau}||^2 = q^{2\theta s} + 1$ and $((q^{0s}\theta_0 - \theta_s)^{\tau}, (\theta_s^\tau - \bar{\theta}_s^\tau)) = -1$, (31.45) implies that

$$
(q ^ {g _ {s}} \theta_ {0} - \theta_ {s}) ^ {\tau} = q ^ {g _ {s}} \theta_ {0} ^ {\tau} - \theta_ {s} ^ {\tau} \quad \text { for } 1 \leq s \leq m.\tag{31.46}
$$

Lemmas 31.2 and 31.5 and equations (31.42) and (31.44) yield that

$$
- q ^ {f _ {n}} = ((q ^ {f _ {n}} \lambda_ {0} - \zeta_ {1}) ^ {\tau}, \alpha^ {\tau}) = ((q ^ {f _ {n}} \lambda_ {0} - \zeta_ {1}) ^ {\tau}, - \lambda_ {0} ^ {\tau}).\tag{31.47}
$$

By Lemma 13.10 $\{\zeta_i | 1 \leq i \leq q - 1\}$ is subcoherent in $\mathcal{T}$. Since $\| (q^{f_n} \lambda_0 - \zeta_1)^c \|^2 = q^{2f_n} + e$ it follows from (31.47) that

$$
(q ^ {f _ {n}} \lambda_ {0} - \zeta_ {1}) ^ {\tau} = q ^ {f _ {n}} \lambda_ {0} ^ {\tau} - \zeta_ {1} ^ {\tau}.\tag{31.48}
$$

Let $\mathfrak{D}_0$ have the same meaning as in Lemma 31.5. Then there exists a subgroup $\mathfrak{D}_1$ of $\mathfrak{D}_0$ such that $\mathfrak{D}_0 / \mathfrak{D}_1$ is a chief factor of $\mathfrak{T}$ and $|\mathfrak{D}_0:\mathfrak{D}_1| = q$. Let $\mathcal{T}(\mathfrak{D}_0)$ be the irreducible characters of $\mathfrak{T}$ of degree $eq^{qj}$, $0\leq j\leq m$. Then (31.46) implies directly that $\mathcal{T}(\mathfrak{D}_0)$ is coherent. Hypothesis 11.1 is satisfied with $\mathfrak{H} = \widehat{\mathfrak{L}} = \mathfrak{R} = \mathfrak{Q}$ and $\mathfrak{T} = \mathfrak{L}$. If $\mathcal{T}$ is not coherent then Theorem 11.1 implies that $|\mathfrak{Q}:\mathfrak{D}_0| < 4e^2 +1$. As $\mathfrak{T} / \mathfrak{D}_0$ is a Frobenius group this implies that $\mathfrak{D}_0 = \mathfrak{D}'$. Therefore $\mathfrak{Q} / \mathfrak{D}_1$ is an extra special $q$-group. Thus $|\mathfrak{Q}:\mathfrak{Q}'| = q^{2c}$ for some integer $c$. Define

$$
\mathcal {T} (\mathfrak {Q} _ {1}) = \mathcal {T} (\mathfrak {Q} _ {0}) \cup \{\zeta_ {i} | 1 \leq i \leq q - 1 \}.
$$

Then $\mathcal{T}(\mathfrak{Q}_1)$ consists of all characters in $\mathcal{T}$ having the same weight and degree as some character in $\mathcal{T}$ which has $\mathfrak{Q}_1$ in its kernel. By (31.48) $\mathcal{T}(\mathfrak{Q}_1)$ is coherent. Thus if $\mathcal{T}$ is not coherent Theorem 11.1 implies that

$$
q ^ {2 c + 1} = | \mathfrak {Q}: \mathfrak {Q} _ {1} | \leq 4 e ^ {2} + 1.\tag{31.49}
$$

Lemma 13.6 applied to the group $\mathfrak{W}_2\mathfrak{Q} / \mathfrak{D}_1$ implies that $e|q^c + 1$ or $e|q^c - 1$ and $|\mathfrak{W}_2| = e$. As $e$ is odd this yields that $2e \leq q^c + 1$ in any case. Thus by (31.49)

$$
q ^ {2 c + 1} \leq 4 e ^ {2} + 1 \leq (q ^ {c} + 1) ^ {2} + 1 <   2 q ^ {2 c}.
$$

This contradiction suffices to prove Theorem 31.1.

COROLLARY 31.1.1. If $\lambda_0$ is an irreducible character of $\mathfrak{T}$ of degree $w_2$ then

$$
(\tilde {1} _ {\mathfrak {T} ^ {\prime}} - \lambda_ {0}) ^ {\tau} = 1 _ {\mathfrak {G}} - \lambda_ {0} ^ {\tau} + \sum_ {t = 1} ^ {w _ {2} - 1} \eta_ {0 t}.
$$

Proof. Let $\alpha = \tilde{1}_{\mathfrak{T}'} - \lambda_0$ and let $a_t = (\alpha^\tau, \eta_{0t})$. By Theorem 31.1

$$
\begin{array}{r l} (\nu_ {1} (1) \widetilde {1} _ {\mathfrak {T} ^ {\prime}} - \zeta_ {1}) ^ {\tau} & = \nu_ {1} (1) \alpha^ {\tau} + (\nu_ {1} (1) \lambda_ {0} - \zeta_ {1}) ^ {\tau} \\ & = \nu_ {1} (1) \lambda_ {0} ^ {\tau} - \zeta_ {1} ^ {\tau} + \nu_ {1} (1) \alpha^ {\tau}. \end{array}\tag{31.50}
$$

As $\eta_{0t}$ is rational on $\mathfrak{T}'$, $(\eta_{0t}, \lambda_0^{\mathrm{r}}) = 0$. By Lemma 13.9 $(\eta_{0t}, \zeta_1^{\mathrm{r}}) = 0$. Thus (31.50) implies that

$$
((\nu_ {1} (1) \tilde {1} _ {\mathfrak {T} ^ {\prime}} - \zeta_ {1}) ^ {\tau}, \eta_ {0 t}) = a _ {t} \nu_ {1} (1) \quad \text { for } 1 \leq t \leq w _ {2} - 1.
$$

Hence by Lemma 31.2 $(\alpha^{\tau},\eta_{0t})\neq 0$ for $1\leq t\leq w_2 - 1$ . As $|\mathcal{T}| > 2,$$(\alpha^{\tau},1_{\mathfrak{G}}) = 1$ ， $(\alpha^{\tau},\lambda_0^{\tau} - \overline{\lambda}_0^{\tau}) = -1$ and $\| \alpha^{\tau}\|^{2} = w_{2} + 1$ we get that

$$
\alpha^ {\tau} = 1 _ {6} - \lambda_ {0} ^ {\tau} + \sum_ {t = 1} ^ {w _ {2} - 1} \pm \eta_ {0 t}.
$$

As $\alpha^{\tau}$ vanishes on $\hat{\mathfrak{W}}$ Lemma 13.2 now implies the required result.

COROLLARY 31.1.2. $\mathfrak{S}'$ is a Frobenius group and $w_{2}$ is a prime.

Proof. Suppose that $\mathcal{S}$ contains an irreducible character $\theta$. Choose $\xi_j$ in $\mathcal{S}(\mathfrak{H}')$. Then $(\theta(1)\xi_j^{\tau} - \xi_j(1)\theta^{\tau}) \in \mathcal{I}_0(\mathcal{S})$. If $\mathcal{S}$ is not coherent $\theta$ may be chosen in $\mathcal{S}(\mathfrak{H}')$ by Theorem 30.1 and Lemma 31.1. Hence by Corollary 31.1.1 and Lemmas 13.9 and 30.8,

$$
\begin{array}{r l} 0 & = (\theta (1) \xi_ {j} ^ {\tau} - \xi_ {j} (1) \theta^ {\tau}, (\tilde {1} _ {\mathfrak {T} ^ {\prime}} - \lambda_ {0}) ^ {\tau}) \\ & = \theta (1) \left(\pm \sum_ {i = 0} ^ {q - 1} \eta_ {i j}, \sum_ {t = 1} ^ {w _ {2} - 1} \eta_ {0 t}\right) = \pm \theta (1). \end{array}
$$

Therefore S contains no irreducible characters. Lemma 31.1 now implies that $\mathfrak{S}'$ is a Frobenius group and $w_{2}$ is a prime.

## 32. Subgroups of Type V

THEOREM 32.1. & contains no subgroup of type V.

Proof. Suppose that the result is false and $\mathfrak{T}$ is a subgroup of type V. $\mathfrak{T}'$ is tamely imbedded in $\mathfrak{G}$ by Theorem 14.2. For $0 \leq i \leq n$ let $\mathfrak{L}_i$ have the same meaning as in Definition 9.1 and let $\mathfrak{A}_L$ be defined by (9.2). Let $\mathfrak{G}_1$ be the set of elements in $\mathfrak{G}$ which are conjugate to some element of $\mathfrak{A}_L$ for $L \in \bigcup_{i=0}^{n} \mathfrak{L}_i$. By Lemma 9.5

$$
\begin{array}{r l} \frac {1}{| \mathfrak {G} |} | \mathfrak {G} _ {1} | & = \frac {1}{| \mathfrak {G} |} \sum_ {\mathfrak {G} _ {1}} 1 _ {\mathfrak {G}} (G) \\ & = \frac {1}{| \mathfrak {T} |} \sum_ {\mathfrak {T} ^ {\prime}} 1 _ {\mathfrak {G}} (T) = \frac {1}{w _ {2}} \left(1 - \frac {1}{| \mathfrak {T} ^ {\prime} |}\right). \end{array}\tag{32.1}
$$

Let $\lambda$ be an irreducible character of degree $w_{2}$ in $\mathcal{T}$. By Theorem 31.1 and Lemmas 10.3 and 9.4

$$
\lambda^ {\tau} (T) = a + \lambda (T) \quad \text { for } T \in \mathfrak {T} ^ {\prime \sharp},\tag{32.2}
$$

where $a$ is independent of $T$. Now Theorem 31.1 and Corollary 31.1.1 imply that $a = 0$ in (32.2). Thus $\lambda^{\tau}(T) = \lambda(T)$ for $T \in \mathfrak{X}'^{*}$. Hence Theorem 31.1 and Lemmas 10.3 and 9.5 imply that

$$
\frac {1}{| \mathfrak {G} |} \sum_ {\mathfrak {G} _ {1}} | \lambda^ {\tau} (G) | ^ {2} = \frac {1}{| \mathfrak {T} |} \sum_ {\mathfrak {T} ^ {\prime 2}} | \lambda (G) | ^ {2} = 1 - \frac {w _ {2}}{| \mathfrak {T} ^ {\prime} |}.\tag{32.3}
$$

Let $\mathfrak{W}$ be defined by Theorem 14.1 (ii) (a) and let $\hat{\mathfrak{W}} = \mathfrak{W} - \mathfrak{W}_2 - \mathfrak{Q}^*$. Define

$$
\mathfrak {G} _ {2} = \bigcup_ {\theta \in \mathfrak {G}} G ^ {- 1} \widehat {\mathfrak {W}} G.
$$

Thus Theorem 14.2 (ii) (a) implies that

$$
\frac {1}{| \mathfrak {G} |} | \mathfrak {G} _ {2} | = 1 - \frac {1}{w _ {2}} - \frac {1}{q} + \frac {1}{q w _ {2}}.\tag{32.4}
$$

Let $\mathfrak{G}_3$ be the set of elements in $\mathfrak{G}$ which are conjugate to some element of $\mathfrak{H}^*$. Since $\mathfrak{H}$ is a T.I. set in $\mathfrak{G}$,

$$
\frac {1}{| \mathfrak {G} |} | \mathfrak {G} _ {\mathfrak {s}} | = \frac {1}{q u | \mathfrak {H} |} (| \mathfrak {H} | - 1).\tag{32.5}
$$

Define

$$
\mathfrak {G} _ {0} = \mathfrak {G} - \mathfrak {G} _ {1} - \mathfrak {G} _ {2} - \mathfrak {G} _ {3}.
$$

Then (32.1), (32.4) and (32.5) imply that

$$
\begin{array}{r l} \frac {1}{| \mathfrak {G} |} | \mathfrak {G} _ {0} | & \geq 1 - \left(1 - \frac {1}{w _ {2}} - \frac {1}{q} + \frac {1}{q w _ {2}}\right) - \left(\frac {1}{w _ {2}} - \frac {1}{w _ {2} | \mathfrak {T} ^ {\prime} |}\right) \\ & \quad - \left(\frac {1}{q u} - \frac {1}{q u | \mathfrak {H} |}\right) = \frac {1}{q} - \frac {1}{w _ {2} q} - \frac {1}{q u} + \frac {1}{w _ {2} | \mathfrak {T} ^ {\prime} |} \\ & \quad + \frac {1}{q u | \mathfrak {H} |} > \frac {1}{q} - \frac {1}{3 q} - \frac {1}{3 q} = \frac {1}{3 q}. \end{array}\tag{32.6}
$$

By (32.3)

$$
\frac {1}{| \mathfrak {G} |} \sum_ {\mathfrak {G} _ {0}} | \lambda^ {\tau} (G) | ^ {2} \leq 1 - \left(1 - \frac {w _ {2}}{| \mathfrak {T} ^ {\prime} |}\right) = \frac {w _ {2}}{| \mathfrak {T} ^ {\prime} |}.\tag{32.7}
$$

By Corollary 31.1.2 $w_{2}$ is a prime and $\mathfrak{SU}$ is a Frobenius group. Hence by Lemma 13.1 $\eta_{01}, \cdots, \eta_{0,w_{2}-1}$ are algebraically conjugate characters whose values lie in $\mathcal{O}_{w_{2}}$. Every element whose order is divisible by $w_{2}$ lies in $\mathfrak{G}_{2} \cup \mathfrak{G}_{3}$. Thus $\eta_{0j}(G) = \eta_{01}(G)$ is a rational integer for $G \in \mathfrak{G}_{0}$ and $1 \leq j \leq w_{2} - 1$. Now Corollary 31.1.1 implies that $1 - \lambda^{r}(G) + (w_{2} - 1)\eta_{01}(G) = 0$ for $G \in \mathfrak{G}_{0}$. Hence $\lambda^{r}(G) \equiv 1 (\text{mod } 2)$ for $G \in \mathfrak{G}_{0}$. Therefore $|\lambda^{r}(G)| \geq 1$ for $G \in \mathfrak{G}_{0}$. Now (32.6) and (32.7) imply that

$$
\frac {w _ {2}}{| \mathfrak {T} ^ {\prime} |} > \frac {1}{3 q}
$$

or

$$
3 q w _ {2} > \left| \mathfrak {T} ^ {\prime} \right|.\tag{32.8}
$$

Since $\mathfrak{T}'' \neq 1$, (32.8) yields that $3w_2 > |\mathfrak{T}' : \mathfrak{T}''|$ and $|\mathfrak{T}''| = q$. Thus, $\mathfrak{W}_2$ acts irreducibly on $\mathfrak{T}' / \mathfrak{T}''$. Therefore $\mathfrak{T}'$ is an extra special group. Let $|\mathfrak{T}' : \mathfrak{T}''| = q^{2c}$. Then by Lemma 13.6, $w_2 \leq (q^c + 1)/2$. Thus (32.8) implies that $q^{2c} < (3/2)(q^c + 1) < 2q^c$. Hence $q^c < 2$ which is not the case. The proof is complete.

COROLLARY 32.1.1. Let $\mathfrak{S}$ be a subgroup of type II, III or IV. Let $\mathcal{S}$ have the same meaning as in Section 29. Then $\mathcal{S}$ is coherent.

Proof. This is an immediate consequence of Theorems 30.1 and 32.1.

## 33. Subgroups of Type I

LEMMA 33.1. Let $\mathfrak{L}$ be a maximal subgroup of $\mathfrak{G}$ and let $\hat{\mathfrak{L}}$ have the same meaning as in section 14. If $\mathfrak{L}$ is of type I with Frobenius

kernel $\mathfrak{D}$ let $\mathcal{L}$ be the set of all irreducible characters of $\mathfrak{D}$ which do not have $\mathfrak{D}$ in their kernel. If $\mathfrak{D}$ is of type II, III or IV let $\mathcal{L}$ be the set of characters of $\mathfrak{D}$ each of which is induced by a non principal irreducible character of $\mathfrak{D}'$ which vanishes outside $\hat{\mathfrak{D}}$. Let $\mathfrak{D}_i$ have the same meaning as in section 9 and let $\mathfrak{A}_L$ be defined by (9.2). If $\lambda \in \mathcal{L}$ then $\lambda^r$ can be defined. Furthermore $\lambda^r$ is constant on $\mathfrak{A}_L$ for $L \in \bigcup_{i=0}^{n} \mathfrak{D}_i$.

Proof. Since $|\mathfrak{G}|$ is odd Lemmas 10.1 and 13.9 imply that $\lambda^r$ can always be defined as $\{\lambda, \overline{\lambda}\}$ is coherent.

If $L \in \mathfrak{L}_0$ then $\mathfrak{A}_L = \{L\}$ and there is nothing to prove. If $L \in \mathfrak{L}_i$ with $i \neq 0$ let $\mathfrak{H}_i$ be a supporting subgroup of $\widehat{\mathfrak{H}}$ such that $C(L) \subseteq \mathfrak{N}_i = N(\mathfrak{H}_i)$. If $\mathfrak{N}_i$ is of type I then the result follows from Lemmas 4.5 and 10.3. By definition $\mathfrak{N}_i$ cannot be of type III or IV. If $\mathfrak{N}_i$ is of type II then the result is a simple consequence of Corollary 32.1.1.

The main purpose of this section is to prove

## THEOREM 33.1. Every subgroup of type I is a Frobenius group.

All the remaining lemmas in this section will be proved under the following assumption.

Hypothesis 33.1.

& contains a subgroup of type I which is not a Frobenius group.

If Hypothesis 33.1 is satisfied the following notation will be used. $\sigma$ is a set of primes defined as follows: $p_i \in \sigma$ if and only if $\mathfrak{G}$ contains a subgroup $\mathfrak{M}_i$ of type I with Frobenius kernel $\mathfrak{R}_i$ such that a $S_{p_i}$-subgroup of $\mathfrak{M}_i / \mathfrak{R}_i$ is not cyclic.

$p = p_{k}$ is the smallest prime in $\sigma$. $\mathfrak{M} = \mathfrak{M}_k$; $\mathfrak{R} = \mathfrak{R}_k$.

$P_{0}$  is a  $S_{p}$ -subgroup of M.

$\mathfrak{P}$ is a $S_{p}$-subgroup of $\mathfrak{G}$ with $\mathfrak{P}_0 \subseteq \mathfrak{P}$.

$\mathfrak{L}$ is a maximal subgroup of $\mathfrak{G}$ such that $N(\Omega_1(\mathfrak{P}_0)) \subseteq \mathfrak{L}$.

L has the same meaning as in Lemma 33.1.

If $\mathfrak{L}$ is of type I let $\mathfrak{U}$ be the Frobenius kernel of $\mathfrak{L}$. Let $\mathfrak{L} = \mathfrak{U}\mathfrak{G}$ with $\mathfrak{U} \cap \mathfrak{G} = 1$.

If $\mathfrak{L}$ is of type II, III or IV let $\mathfrak{H}$ be the maximal normal nilpotent $S$-subgroup of $\mathfrak{L}$. Let $\mathfrak{U}$ be a complement of $\mathfrak{H}$ in $\mathfrak{L}'$ and let $\mathfrak{W}_1$ be a complement of $\mathfrak{L}'$ in $\mathfrak{L}$ with $\mathfrak{W}_1 \subseteq N(\mathfrak{U})$.

LEMMA 33.2. $\mathfrak{L}$ is the unique maximal subgroup of $\mathfrak{G}$ which contains $N(\Omega_1(\mathfrak{P}_0))$. Furthermore $\mathfrak{L}$ is either a Frobenius group or $\mathfrak{L}$ is of type III or IV and $\mathfrak{P}$ can be chosen to lie in $\mathfrak{U}$.

Proof. By Theorem 32.1 $\mathfrak{L}$ is not of type V. If $\mathfrak{L}$ is of type II, III or IV then $\mathfrak{P}_0 \subseteq \mathfrak{L}'$ since $\mathfrak{P}_0$ is not cyclic. Since $\mathfrak{H}$ is a T.I. set in $\mathfrak{G}$ it may be assumed that $\mathfrak{P}_0 \subseteq \mathfrak{U}$.

There exists $P \in \Omega_1(\mathfrak{P}_0)$ such that $C(P) \subseteq \mathfrak{M}$. Thus either $\mathfrak{P} = \mathfrak{P}_0$ or $Z(\mathfrak{P})$ is cyclic and $Z(\mathfrak{P}) \subseteq \mathfrak{P}_0$. If a $S_p$-subgroup of $\mathfrak{U}$ is abelian then $\mathfrak{P}_0$ is the $S_p$-subgroup of $\mathfrak{U}$. Hence $\Omega_1(\mathfrak{P}_0)$ char $\mathfrak{U}$ and so $N(\mathfrak{U}) \subseteq N(\Omega_1(\mathfrak{P}_0)) \subseteq \mathfrak{L}$. Therefore $\mathfrak{L}$ is of type III or IV and $\mathfrak{P} = \mathfrak{P}_0 \subseteq \mathfrak{U}$. By definition $\mathfrak{L}$ is the unique maximal subgroup which contains $N(\Omega_1(\mathfrak{P}_0))$. If the $S_p$-subgroup of $\mathfrak{U}$ is not abelian then $\mathfrak{L}$ is of type IV and it may be assumed that $\mathfrak{P} \subseteq \mathfrak{U}$. Then $\Omega_1(\mathfrak{P}_0) \subseteq \widehat{\mathfrak{L}}$ and in this case also $\mathfrak{L}$ is the unique maximal subgroup of $\mathfrak{G}$ which contains $N(\Omega_1(\mathfrak{P}_0))$.

Suppose that $\mathfrak{L}$ is of type I. Let $\mathfrak{P}_1$ be a $S_{p}$-subgroup of $\mathfrak{L}$ with $\mathfrak{P}_0 \subseteq \mathfrak{P}_1$. If $p \in \pi(\mathfrak{G})$, then $\mathfrak{P}_1$ is abelian. Thus, $\mathfrak{P}_0 = \mathfrak{P}_1$ and so $\mathfrak{P}_0 = \mathfrak{P}$. Hence, $\mathfrak{P}$ is an abelian $S_p$-subgroup of $\mathfrak{G}$. By construction, $N(\mathfrak{P}) \subseteq \mathfrak{L}$. Hence, $\mathfrak{P} \subseteq \mathfrak{L}'$, by Burnside's transfer theorem. Since $|\mathfrak{L}|$ is odd, if an element of $N(\mathfrak{P})$ induces an automorphism of $\mathfrak{P}$ of prime order $q$, then $q < p$. By the minimal nature of $p$, a $S_q$-subgroup of $\mathfrak{L}$ is cyclic. Let $\mathfrak{P}^* = \mathfrak{P} \cap C(\mathfrak{U})$. Since $\mathfrak{L}$ is of type I, $\mathfrak{P}^*$ is cyclic. We can now find a prime $q$ such that some element $N(\mathfrak{P})$ induces an automorphism of order $q$ on $\mathfrak{P}/\mathfrak{P}^*$. Let $\mathfrak{Q}$ be a $S_q$-subgroup of $\mathfrak{F}$ permutable with $\mathfrak{P}$. Since $q < p$, $\mathfrak{Q}$ normalizes $\mathfrak{P}$, and $\mathfrak{Q}$ is cyclic. Since $\mathfrak{U}$ is a Frobenius group, $\Omega_1(\mathfrak{Q})$ centralizes $\mathfrak{P}/\mathfrak{P}^*$. Let $\mathfrak{P}_0^* = C_{\mathfrak{P}}(\Omega_1(\mathfrak{Q}))$. Then $\mathfrak{P} = \mathfrak{P}^*\mathfrak{P}_0^*$, and $[\mathfrak{Q}, \mathfrak{P}_0^*] \not\subseteq \mathfrak{P}^*$.

Let $\mathfrak{L}^*$ be a maximal subgroup containing $N(\Omega_1(\mathfrak{D}))$. The minimal nature of $p$ implies that $\mathfrak{Q} \subseteq \mathfrak{L}^{*'}$. Hence, by Lemma 8.13, $\mathfrak{Q}$ centralizes every chief $p$-factor of $\mathfrak{L}^*$, so $\mathfrak{Q}$ centralizes $\mathfrak{P}_0^*$, which is not the case. We conclude that $p \notin \pi(\mathfrak{E})$. Therefore $p \in \pi(\mathfrak{U})$. Hence $\mathfrak{P} \subseteq \mathfrak{U}$. $\mathfrak{U}$ is not a T.I. set since $\mathfrak{P}$ is not a T.I. set in $\mathfrak{G}$. This yields that either $p \in \pi_1^*$ or $m(\mathfrak{U}) = 2$. In either case this implies that every prime divisor of $|\mathfrak{G}|$ is less than $p$. The minimal nature of $p$ now implies that $\mathfrak{L}$ is a Frobenius group.

The previous parts of the lemma imply that if $\mathfrak{L}_1$ is a maximal subgroup of $\mathfrak{G}$ which contains $N(\Omega_1(\mathfrak{P}_0))$ then $\mathfrak{L}_1$ is a Frobenius group and $p$ divides the order of the Frobenius kernel of $\mathfrak{L}_1$. If $\mathfrak{P}$ is abelian then $\mathfrak{P} = \mathfrak{P}_0$ and $\mathfrak{L} = \mathfrak{L}_1 = N(\Omega_1(\mathfrak{P}_0))$. If $\mathfrak{P}$ is non abelian then $\mathfrak{L} = \mathfrak{L}_1 = N(Z(\mathfrak{P}))$. The uniqueness of $\mathfrak{L}$ is proved.

LEMMA 33.3. There exists an irreducible character $\lambda \in \mathcal{L}$ which does not have $\mathfrak{P}$ in its kernel such that $\lambda(1) | (p - 1)$ or $\lambda(1) | (p + 1)$.

Proof. Let $\lambda$ be a character of $\mathfrak{L}$ which does not have $\mathfrak{P}$ in its kernel and is induced by a linear character of $\mathfrak{U}$ if $\mathfrak{L}$ is a Frobenius group and by a linear character of $\mathfrak{L}'$ if $\mathfrak{L}$ is of type III or IV.

Either $\mathfrak{P} = \mathfrak{P}_0$ and so $m(\mathfrak{P}) = 2$, or $Z(\mathfrak{P})$ is cyclic. In either case this implies that if $q \in \pi (N(\mathfrak{P}) / C(\mathfrak{P}))$, $q \neq p$ then $q \mid (p + 1)$ or $q \mid (p - 1)$. If $\mathfrak{L}$ is of type III or IV then $\lambda(1) = |\mathfrak{W}_1|$ is a prime and the result follows. Suppose that $\mathfrak{L}$ is a Frobenius group. If $p \in \pi_1^*$ then $|\mathfrak{G}| = \lambda(1)$ has the required properties by assumption. If $p \notin \pi_1^*$ then $\mathfrak{Q}$ is abelian since $\mathfrak{Q}$ is not a T.I. set in $\mathfrak{G}$. Thus $\mathfrak{P} = \mathfrak{P}_0$ and $m(\mathfrak{P}) = 2$. Suppose that $q_1, q_2 \in \pi(\mathfrak{G})$ where $q_1 \mid (p - 1)$ and $q_2 \mid (p + 1)$. Then an element of $\mathfrak{G}$ of order $q_1$ acts as a scalar on $\mathfrak{P}$. There exists $P \in \mathfrak{P}^*$ such that $N(< P>) \subseteq \mathfrak{M}$. Thus $\mathfrak{M}$ contains a Frobenius group of order $pq_1$ which is not the case. Therefore every prime in $\pi(\mathfrak{G})$ divides $(p - 1)$ or every prime in $\pi(\mathfrak{G})$ divides $(p + 1)$. Since $(p + 1, p - 1) = 2$ this yields that $|\mathfrak{G}||(p + 1)$ or $|\mathfrak{G}||(p - 1)$. The lemma follows since $\lambda(1) = |\mathfrak{G}|$.

LEMMA 33.4. Let $\lambda$ be the character defined in Lemma 33.3. Then

$$
\lambda^ {\tau} (L) = \lambda (L) \quad f o r L \in \hat {\mathfrak {X}} ^ {\sharp}
$$

Proof. Set $e = |\mathfrak{L} : \mathfrak{L}'|$. Observe that if $\mathfrak{L}$ is a Frobenius group, then since $p \in \pi^*$, it follows that $\mathfrak{L}' = \mathfrak{U}$, so that $\lambda(1) = e$. This equality also holds if $\mathfrak{L}$ is of type III or IV.

Set $\alpha = (\tilde{1}_{\mathfrak{g}'} - \lambda)$ so that $\alpha^{\tau} = 1_{\mathfrak{G}} - \lambda^{\tau} + \Delta$, where $\Delta$ is a generalized character of $\mathfrak{G}$ orthogonal to $1_{\mathfrak{G}}$. Let $\lambda = \lambda_1, \cdots, \lambda_f$ be the characters in $\mathscr{L}$ of degree $e$. Since $e$ divides $(p + 1)/2$ or $(p - 1)/2$, it follows that $f > e + 1$, and so $(\Delta, \lambda_i) = 0$, $1 \leq i \leq f$.

We next show that $\mathcal{L}$ is coherent. If $\mathfrak{L}$ is a Frobenius group, the coherence of $\mathcal{L}$ follows from Lemma 11.1 and the fact that $\mathfrak{L}$ is of type I.

Suppose $\mathfrak{L}$ is of type III or IV. Then Hypothesis 11.1 and (11.2) are satisfied with the present $\mathfrak{L}$ in the role of $\mathfrak{L}_0$, $\mathfrak{H}$ in the role of $\mathfrak{H}_0$, and $\mathfrak{L}' / \mathfrak{H}$ in the role of $\mathfrak{H}$. By Lemma 11.1, we may assume that $|\mathfrak{L}' : \mathfrak{L}''| \leq 4 |\mathfrak{L} : \mathfrak{L}'|^2 + 1$. Hence, $|\mathfrak{L}' : \mathfrak{L}''| = p^2$ and $e = (p + 1)/2$, so that $\mathfrak{P} = \mathfrak{U}$. If $\mathfrak{P}$ is non abelian, then $e$ divides $(p - 1)/2$. Hence, we may assume that $\mathfrak{P}$ is abelian of order $p^2$ and $\mathfrak{L}$ is of type III. By Theorem 29.1 (i), no element of $\mathfrak{P}^*$ centralizes $\mathfrak{H}$. This implies that if $\mu_1, \cdots, \mu_{f'}$ are the characters in $\mathscr{L}$ of degree $pe$, then $f' \geq 2p$. Hence, $(\Delta, \mu_j^c) = 0$, $1 \leq j \leq f'$.

Let $\beta = (p\lambda_1 - \mu_1)$, so that $\beta^{\tau} = p\lambda_{1}^{\tau} - x\sum_{i}\lambda_{i}^{\tau} - \mu_{1}^{\tau} + \Delta_{1}$, with $(\Delta_{1},\lambda_{i}^{\tau}) = 0$. If $x = 0$, the coherence of $\mathcal{L}$ follows from Theorem 30.1. As $||\beta^{\tau}||^{2} = p^{2} + 1$, and $f = 2(p - 1)$, it follows that $0 \leq x < 2$, and $||\Delta_1||^{2} \leq 2$. Hence, $x = 1$ and $(\Delta_{1},\mu_{j}^{\tau}) = 0$. But now $(\alpha^{\tau},\beta^{\tau}) = (\alpha ,\beta) = -p = -(p - 1) + (\Delta ,\Delta_{1})$, so that $(\Delta ,\Delta_{1}) = -1$. This is not the case as $\Delta$ and $\Delta_{1}$ are real valued generalized characters of $\mathfrak{G}$

orthogonal to  $1_{g}$ . The coherence of L is proved in all cases.

Since $(\Delta, \lambda^{\tau}) = 0$, the lemma follows from Lemmas 9.4 and 33.1.

LEMMA 33.5. Let $\lambda$ be the character defined in Lemma 33.3. Then

$$
\frac {1}{| \mathfrak {M} |} \Sigma_ {\mathfrak {R} ^ {k}} | \lambda^ {\tau} (K) | ^ {2} <   \frac {\lambda (1) ^ {2}}{| \mathfrak {L} |}.
$$

Proof. Let $\mathfrak{G}_0$ be the set of all elements in $\mathfrak{G}$ which are conjugate to an element of $\mathfrak{A}_L$ for some $L \in \hat{\mathfrak{X}}$. Let $\mathfrak{G}_1$ be the set of all elements in $\mathfrak{G}$ which are conjugate to an element of $\mathfrak{A}_K$ for some $K \in \mathfrak{R}^*$. No subgroup of $\mathfrak{G}$ can be a supporting subgroup for both $\hat{\mathfrak{X}}$ and $\hat{\mathfrak{M}}$. If $\mathfrak{L}$ were a supporting subgroup of $\hat{\mathfrak{M}}$ then $p$ would not be minimal in the set $\sigma$. Thus $\mathfrak{G}_0$ is disjoint from $\mathfrak{G}_1$. Therefore by Lemmas 9.5, 4.5, 10.3, 33.1 and 33.4

$$
\begin{array}{r l} \frac {1}{| \mathfrak {M} |} \Sigma_ {\mathfrak {R} ^ {\sharp}} | \lambda^ {\tau} (K) | ^ {2} & = \frac {1}{| \mathfrak {G} |} \Sigma_ {\mathfrak {G} _ {1}} | \lambda^ {\tau} (G) | ^ {2} <   1 - \frac {1}{| \mathfrak {G} |} \Sigma_ {\mathfrak {G} _ {0}} | \lambda^ {\tau} (G) | ^ {2} \\ & = 1 - \frac {1}{| \mathfrak {L} |} \Sigma_ {\hat {\mathfrak {L}} ^ {\sharp}} | \lambda^ {\tau} (G) | ^ {2} = 1 - \frac {1}{| \mathfrak {L} |} \Sigma_ {\hat {\mathfrak {L}} ^ {\sharp}} | \lambda (G) | ^ {2} \\ & = 1 - \left(1 - \frac {\lambda (1) ^ {2}}{| \mathfrak {L} |}\right) = \frac {\lambda (1) ^ {2}}{| \mathfrak {L} |}. \end{array}
$$

LEMMA 33.6. Let $\mathfrak{M} = \mathfrak{K}\mathfrak{F}$ where $\mathfrak{F} = \mathfrak{M} \cap \mathfrak{L}$. Then there exists $F$ in $(\mathfrak{P}_0 \cap Z(\mathfrak{F}))^\sharp$ such that $C_{\mathfrak{R}}(F) \not\subseteq \mathfrak{R}'$. Furthermore $\mathfrak{M}$ satisfies Hypothesis 28.1.

Proof. If $\mathfrak{S}$ is of type I, then $\mathfrak{F} \subseteq \mathfrak{U}$. Thus, $\mathfrak{F}$ is nilpotent and hence abelian. The result follows from 3.16 (ii) and the fact that $\mathfrak{P}_0$ is not cyclic.

Suppose $\mathfrak{L}$ is not of type I. If $\mathfrak{F} \not\subseteq \mathfrak{U}\mathfrak{H}$, then we may assume that $\mathfrak{W}_1 \subseteq \mathfrak{F}$. Then $\mathfrak{W}_1\mathfrak{P}_0$ is a Frobenius group and $\mathfrak{W}_1\mathfrak{P}_0 \subseteq \mathfrak{F}$. By 3.16 (ii), $\mathfrak{W}_1$ centralizes an element of $\mathfrak{R}^{\sharp}$. Since $|\mathfrak{W}_1|$ is a prime, this contradicts the fact that $\mathfrak{M}$ contains a Frobenius group of order $|\mathfrak{W}_1\mathfrak{R}|$. Thus, $\mathfrak{F} \subseteq \mathfrak{U}\mathfrak{H}$. Let $\mathfrak{F}_1 = \mathfrak{F} \cap \mathfrak{H}$. Since $\mathfrak{H}$ is a T.I. set in $\mathfrak{G}$, we get that $\mathfrak{F}_1$ is a cyclic normal $S$-subgroup of $\mathfrak{F}$. If $\mathfrak{F}_1 = 1$, then $\mathfrak{F}$ is abelian and the result follows from 3.16 (ii).

Assume now that $\mathfrak{F}_1 \neq 1$. We may assume that $\mathfrak{F} = \mathfrak{F}_1(\mathfrak{F} \cap \mathfrak{U})$. If $\Omega_1(\mathfrak{P}_0)$ does not centralize $\mathfrak{F}_1$, then there exists $\mathfrak{P}^* \subseteq \Omega_1(\mathfrak{P}_0)$ such that $\mathfrak{F}_1\mathfrak{P}^*$ is a Frobenius group. Hence, $C_{\mathfrak{F}}(\mathfrak{P}^*) \neq 1$ by 3.16 (ii). But in this case, $\mathfrak{P}^*$ lies in no normal abelian subgroup of $\mathfrak{F}$ contrary to the definition of groups of Frobenius type. Thus, $\Omega_1(\mathfrak{P}_0)$ centralizes $\mathfrak{F}_1$. Since $\mathfrak{F} \cap \mathfrak{U}$ is abelian and $\mathfrak{F} = \mathfrak{F}_1(\mathfrak{F} \cap \mathfrak{U})$, this implies that $\Omega_1(\mathfrak{P}_0) \subseteq$

$Z(\mathfrak{F})$. The lemma now follows from 3.16 (ii).

LEMMA 33.7. Let $\mathcal{M}$ be the set of all irreducible characters of $\mathfrak{M}$ which do not have $\mathfrak{R}$ in their kernel. Let $\lambda$ be the character defined in Lemma 33.3. If $\mathcal{M}$ is coherent then $\lambda^{\tau}$ is constant on $\mathfrak{R}^{\sharp}$.

Proof. Let $\mathfrak{H}_1, \cdots, \mathfrak{H}_s$ be a set of supporting subgroups of $\hat{\mathfrak{M}}$ in $\mathfrak{G}$, and let $\mathfrak{N}_i = N_{\mathfrak{G}}(\mathfrak{H}_i)$. By definition,

$$
\hat {\mathfrak {M}} = \bigcup_ {\kappa \in \mathfrak {R} ^ {\sharp}} C _ {\mathfrak {M}} (K) .
$$

Suppose $M \in \hat{\mathfrak{M}}^{\sharp}$ and $C_{\mathfrak{G}}(M) \not\subseteq \mathfrak{M}$. We will show that $M \in \mathfrak{R}$. For otherwise, some power of $M$ is $\mathfrak{M}$-conjugate to an element $A$ of $\mathfrak{F}^{\sharp}$. Since $\mathfrak{R}$ is a supporting subgroup of some tamely imbedded subset of $\mathfrak{G}$, it follows that $C_{\mathfrak{G}}(A) \subseteq \mathfrak{M}$. Hence, $M$ is in $\mathfrak{R}^{\sharp}$.

We next show that $\mathfrak{N}_i$ is of type I or II, $1 \leq i \leq s$. Suppose $\mathfrak{N}_i$ is not of type I. Then $\mathfrak{N}_i = \mathfrak{H}_i(\mathfrak{N}_i \cap \mathfrak{M})$, and we assume that $\mathfrak{N}_i \cap \mathfrak{M} = (\mathfrak{N}_i \cap \mathfrak{K})(\mathfrak{N}_i \cap \mathfrak{F})$. Since $\mathfrak{H}_i$ is a supporting subgroup of $\hat{\mathfrak{M}}$, we may choose $M$ in $\hat{\mathfrak{M}}$ so that $C_{\mathfrak{G}}(M) \subseteq \mathfrak{N}_i$, $C_{\mathfrak{G}}(M) \not\subseteq \mathfrak{M}$. By the first paragraph, $M \in \mathfrak{R}^*$. Hence, $\mathfrak{N}_i \cap \mathfrak{R} \neq 1$. If $N_{\mathfrak{G}}(\mathfrak{N}_i \cap \mathfrak{K}) \subseteq \mathfrak{N}_i$, then by a well known property of nilpotent groups, we have $\mathfrak{R} = \mathfrak{N}_i \cap \mathfrak{R}$, so that $\mathfrak{M} \subseteq \mathfrak{N}_i$, which is not the case. Hence, $N_{\mathfrak{G}}(\mathfrak{N}_i \cap \mathfrak{K}) \not\subseteq \mathfrak{N}_i$, so $\mathfrak{N}_i$ is not of type III or IV; $\mathfrak{N}_i$ is of type II.

Let $a$ be the least common multiple of the orders of all elements of $\hat{\mathfrak{L}}$. We will show that $(a, |\mathfrak{R}|) = (a, |\mathfrak{H}_i|) = 1, 1 \leq i \leq s$. If $\mathfrak{L}$ is of type I, then $\mathfrak{L}$ is a Frobenius group, so $a$ divides $|\mathfrak{U}|$, and we only need to verify that $\mathfrak{L}$ is not conjugate to $\mathfrak{M}$ or $\mathfrak{N}_i, 1 \leq i \leq s$. As none of the groups $\mathfrak{M}, \mathfrak{N}_1, \ldots, \mathfrak{N}_s$ is a Frobenius group, this is clear. Suppose $\mathfrak{L}$ is of type III of IV, so that $\mathfrak{L} = \mathfrak{HU}\mathfrak{W}_1, \hat{\mathfrak{L}} = \mathfrak{HU}$. Since none of $\mathfrak{M}, \mathfrak{N}_1, \ldots, \mathfrak{N}_s$ is of type III or IV, we have $(|\mathfrak{H}|, |\mathfrak{R}|) = (|\mathfrak{H}|, |\mathfrak{H}_i|) = 1, 1 \leq i \leq s$. Since $N_{\mathfrak{G}}(\mathfrak{U}) \subseteq \mathfrak{L}$, it is trivial that $(|\mathfrak{U}|, |\mathfrak{R}|) = (|\mathfrak{U}|, |\mathfrak{H}_i|) = 1$.

We appeal to Lemma 10.4 and conclude that $\lambda^{\tau}$ is rational on $\mathfrak{R}$ and on every supporting subgroup of $\hat{\mathfrak{M}}$.

Let $\mathfrak{H}_i$ be a supporting subgroup of $\mathfrak{M}$ and let $\alpha$ be a character of $\mathfrak{H}_i$ with $(\alpha, 1_{\mathfrak{H}_i}) = 0$. Let $\mu_1, \mu_2$ be irreducible characters of $\mathfrak{N}_i$ with $\mu_{1|\mathfrak{H}_i} = \mu_{2|\mathfrak{H}_i} = \alpha$. Then $||(\mu_1 - \mu_2)^* ||^2 = 2$ and no irreducible character of $\mathfrak{G}$ appearing in $(\mu_1 - \mu_2)^*$ is rational on $\mathfrak{H}_i$. Thus, $(\lambda^\tau, (\mu_1 - \mu_2)^*) = 0$. If $\mathfrak{N}_i$ is of type I, then Hypothesis 10.2 is satisfied with our present $\hat{\mathfrak{M}}$ in the role of $\mathfrak{L}$. If $\mathfrak{N}_i$ is of type II, then a complement to $\mathfrak{H}_i$ in $\mathfrak{N}_i'$ is abelian, and again Hypothesis 10.2 is satisfied. Hence, by Lemma 10.2, $\lambda^\tau$ is constant on the cosets of $\mathfrak{H}_i$ in $\mathfrak{N}_i - \mathfrak{H}_i$, and in particular is constant on all the sets $\mathfrak{A}_M, M \in \hat{\mathfrak{M}}$. As $\mathcal{M}$ is assumed coherent, an appeal to Lemma 10.5 completes the proof of this lemma.

Theorem 33.1 will now be proved by showing that Hypothesis 33.1 leads to a contradiction.

Choose $P \in \mathfrak{P}_0^\sharp$ and $K \in C(P) \cap \mathfrak{R}^\sharp$. By Lemmas 33.1 and 33.4

$$
\lambda^ {\tau} (K P) = \lambda^ {\tau} (P) = \lambda (P).\tag{33.2}
$$

Let $p$ be a prime divisor of $p$ in $\mathcal{Q}_{|\mathfrak{G}|}$. By Lemma 4.2

(33.3)

$$
\lambda^ {\tau} (K) \equiv \lambda^ {\tau} (P K) \pmod {p}\tag{33.4}
$$

$$
\lambda (P) \equiv \lambda (1) \pmod {p}.
$$

Now (33.2), (33.3) and (33.4) yield that

$$
\lambda^ {\tau} (K) \equiv \lambda^ {\tau} (P K) \equiv \lambda (P) \equiv \lambda (1) \pmod {p}.
$$

By Lemma 10.4 $\lambda^{\mathfrak{r}}(K)$ is rational. Thus

$$
\lambda^ {\tau} (K) \equiv \lambda (\mathbf {1}) \pmod {p}.
$$

Since $\lambda(1) \leq (p + 1)/2$ by Lemma 33.3, we get that

$$
\left| \lambda^ {\tau} (K) \right| \geq \lambda (1) - 1 \quad \text { for } K \in \mathfrak {R} ^ {\sharp}, \quad C _ {\mathfrak {P} _ {0}} (K) \neq 1.\tag{33.5}
$$

If every element in $\mathfrak{X}^{\sharp}$ commutes with an element of $\mathfrak{P}_{0}^{\sharp}$ then (33.5) implies that

$$
\mid \lambda^ {\tau} (K) \mid \geq \lambda (1) - 1 \quad \text { for } K \in \mathfrak {R} ^ {*}.\tag{33.6}
$$

If not every element in $\mathfrak{R}^{\sharp}$ commutes with an element of $\mathfrak{P}_{0}^{\sharp}$ then $\lambda^{r}$ is constant on $\mathfrak{R}^{\sharp}$ by Lemmas 28.2, 33.6 and 33.7. As (33.5) holds for at least one element in $\mathfrak{R}^{\sharp}$ we get that (33.6) holds in any case. Now Lemma 33.5 and (33.6) imply that

$$
\frac {\lambda (1) ^ {2}}{| \mathfrak {L} |} > \frac {\{| \mathfrak {R} | - 1 \}}{| \mathfrak {M} |} \{\lambda (1) - 1 \} ^ {2}.
$$

This can be written as

$$
\frac {| \mathfrak {M} : \mathfrak {R} |}{| \mathfrak {R} |} > \frac {\{| \mathfrak {R} | - 1 \}}{| \mathfrak {R} |} \left(\frac {e - 1}{e}\right) ^ {2}, \quad \text { where } e = \lambda (1).\tag{33.7}
$$

Since $|\mathfrak{L}:\mathfrak{L}\cap \mathfrak{M}| > 1$ and $\mathfrak{L}\cap \mathfrak{M}$ is a complement to $\mathfrak{R}$ in $\mathfrak{M}$, (33.7) yields that

$$
\frac {1}{3} > \frac {\{| \mathfrak {R} | - 1 \}}{| \mathfrak {R} |} \left(1 - \frac {1}{e}\right) ^ {2} \geq \frac {\{| \mathfrak {R} | - 1 \}}{| \mathfrak {R} |} \left(\frac {2}{3}\right) ^ {2}.
$$

Hence $3|\mathfrak{R}|/4>|\mathfrak{R}|-1$ or $|\mathfrak{R}|<4$. Thus $|\mathfrak{R}|=3$ and a $S_3$-subgroup of $\mathfrak{G}$ is cyclic contrary to the simplicity of $\mathfrak{G}$ and the fact that $|\mathfrak{G}|$

is odd. This contradiction completes the proof of Theorem 33.1.

## THEOREM 33.2. & contains a subgroup of type II.

Proof. Suppose false. Then by Theorems 14.1 and 33.1, every maximal subgroup of $\mathfrak{G}$ is a Frobenius group. Let $\mathfrak{M}$ be a maximal subgroup of $\mathfrak{G}$ and let $\mathfrak{C}$ be a complement to the Frobenius kernel of $\mathfrak{M}$. We will show that $\mathfrak{C}$ is abelian. Suppose false.

Let $\sigma$ be the set of primes $p$ such that for some maximal subgroup $\mathfrak{M}_1$ with Frobenius kernel $\mathfrak{G}_1$ and complement $\mathfrak{G}_1$, a $S_p$-subgroup of $\mathfrak{G}_1$ is not in $Z(\mathfrak{G}_1)$. Let $p$ be the least prime in $\sigma$. We may suppose that a $S_p$-subgroup $\mathfrak{P}$ of $\mathfrak{G}$ is not contained in $Z(\mathfrak{G})$. Then $\mathfrak{P} \cap \mathfrak{G}' = 1$. Let $\mathfrak{M}_1$ be a maximal subgroup of $\mathfrak{G}$ containing $N(\Omega_1(\mathfrak{P}))$. Since $\Omega_1(\mathfrak{P}) \subseteq Z(\mathfrak{G}), \mathfrak{G} \subseteq \mathfrak{M}_1$. If $\mathfrak{P}$ is contained in the Frobenius kernel $\mathfrak{R}$ of $\mathfrak{M}_1$, then so is $[\mathfrak{P}, \mathfrak{G}] \neq 1$. This is impossible as $\mathfrak{G}$ does not centralize $\mathfrak{P}$, while $\mathfrak{R}$ is nilpotent. Hence $\mathfrak{G} \cap \mathfrak{R} = 1$. Since $\mathfrak{M}_1'' \subseteq \mathfrak{R}$, it follows that $\mathfrak{P}$ is not contained in $\mathfrak{M}_1'$, and that a $S_p$-subgroup of $\mathfrak{M}_1$ is cyclic. Hence, by Burnside's transfer theorem, $\mathfrak{G}$ is not simple. Since this is not possible, $\mathfrak{G}$ is abelian.

Let $G \in \mathfrak{G}^*$. Let $\mathfrak{M}$ be a maximal subgroup of $\mathfrak{G}$ containing $C(G)$. It follows that $C(G)$ is nilpotent. Hence, $\mathfrak{G}$ is solvable by the main theorem of [10]. The proof is complete.

## 34. The Subgroups & and T

By Theorems 32.1 and 33.2 & contains two subgroups & and $\mathfrak{T}$, each of which is of type II, III or IV and which satisfy Condition (ii) (b) of Theorem 14.1. The following notation will be used throughout the rest of this chapter. This differs slightly from that introduced previously.

$$
\mathfrak {S} = \mathfrak {Q} ^ {*} \mathfrak {S} ^ {\prime}, \quad \mathfrak {T} = \mathfrak {P} ^ {*} \mathfrak {T} ^ {\prime}, \quad | \mathfrak {Q} ^ {*} | = q, \quad | \mathfrak {P} ^ {*} | = p.
$$

Thus $p$ and $q$ are both primes. Let $\mathfrak{P}$ be the $S_{p}$-subgroup of $\mathfrak{S}$ and let $\mathfrak{Q}$ be the $S_{q}$-subgroup of $\mathfrak{T}$. Then $\mathfrak{P}^{*} \subseteq \mathfrak{P}, \mathfrak{Q}^{*} \subseteq \mathfrak{Q}$. Let

$$
\mathfrak {W} = \mathfrak {P} ^ {*} \mathfrak {Q} ^ {*}, \quad \hat {\mathfrak {W}} = \mathfrak {W} - \mathfrak {P} ^ {*} - \mathfrak {Q} ^ {*}.
$$

Let $\mathfrak{U}$ be a complement of $\mathfrak{P}$ in $\mathfrak{S}'$ and let $\mathfrak{V}$ be a complement of $\mathfrak{Q}$ in $\mathfrak{T}'$. By 3.16 (i) $\mathfrak{U}$ and $\mathfrak{V}$ are nilpotent, thus

$$
\bigcup_ {P \in \mathfrak {P} ^ {\sharp}} C (P) = \hat {\mathfrak {S}},
$$

if $\mathfrak{S}$ is of type II and

$$
\bigcup_ {Q \in \mathfrak {D} ^ {\sharp}} C (Q) = \hat {\mathfrak {T}},
$$

if $\mathfrak{T}$ is of type II. Let

$$
\mathfrak {C} = C _ {\mathfrak {u}} (\mathfrak {P}), \quad \mathfrak {D} = C _ {\mathfrak {B}} (\mathfrak {Q}).
$$

If $\mathfrak{S}$ is of type III or IV let $\mathfrak{U}^{*} = \mathfrak{U}$. If $\mathfrak{S}$ is of type II then a maximal subgroup $\mathfrak{M}$ which contains $N(\mathfrak{U})$ is not conjugate to $\mathfrak{T}$ since $\mathfrak{M}$ is not $q$-closed. Hence by Theorem 33.1 $\mathfrak{M}$ is a Frobenius group. Let $\mathfrak{U}^{*}$ be the Frobenius kernel of $\mathfrak{M}$. Thus $\mathfrak{U} \subseteq \mathfrak{U}^{*}$. Define $\mathfrak{B}^{*}$ similarly. Let

$$
\left| \mathfrak {C} \right| = c, \quad \left| \mathfrak {D} \right| = d, \quad \left| \mathfrak {U} \right| = u c, \quad \left| \mathfrak {V} \right| = v d,
$$

$$
\left| \mathfrak {U} ^ {*} \right| = u ^ {*} c, \quad \left| \mathfrak {V} ^ {*} \right| = v ^ {*} d, \quad \left| \mathfrak {G} \right| = g.
$$

$\mathcal{S}$ is the set of characters of $\mathfrak{S}$ which are induced by irreducible characters of $\mathfrak{S}'$ which do not have $\mathfrak{P}$ in their kernel.

$\mathcal{T}$ is the set of characters of $\mathfrak{T}$ which are induced by irreducible characters of $\mathfrak{T}'$ which do not have $\mathfrak{Q}$ in their kernel.

The set S as defined here is a subset of the S as defined in Section 29. Thus by Corollary 32.1.1 S and T are coherent.

$U_{0}, V_{0}$ are the sets of irreducible characters of $N(\mathfrak{U}^{*}), N(\mathfrak{B}^{*})$ respectively which do not have $\mathfrak{U}^{*}, \mathfrak{B}^{*}$ respectively in their kernel.

For $0 \leq i \leq q - 1$, $0 \leq j \leq p - 1$, $\eta_{ij}$ are the generalized characters of $\mathfrak{G}$ defined by Lemma 13.1; $\mu_{ij}$ are the characters of $\mathfrak{S}$ defined by Lemma 13.3; $\nu_{ij}$ are the characters of $\mathfrak{T}$ defined by Lemma 13.3. For $0 \leq j \leq p - 1$, $\xi_j$ is the character of $\mathfrak{S}$ defined by Lemma 13.5. For $0 \leq i \leq q - 1$, $\zeta_i$ is the character of $\mathfrak{T}$ defined by Lemma 13.5.

If $\mathfrak{G}_1 \subseteq \mathfrak{G}_2 \subset \mathfrak{G}$, where $\mathfrak{G}_2$ is a maximal subgroup of $\mathfrak{G}$ and if $\alpha$ is a class function of $\mathfrak{G}_1$ then $\tilde{\alpha}$ denotes the class function of $\mathfrak{G}_2$ induced by $\alpha$. Whenever this notation is used $\mathfrak{G}_2$ will be uniquely determined by the context.

Throughout this section no distinction is made between S and T. Any result in this section about one of these groups is automatically valid for the other by symmetry.

LEMMA 34.1. Either

$$
u \left| \frac {p ^ {q} - 1}{p - 1} \right.
$$

and $\mathfrak{U} / \mathfrak{C}$ is cyclic or $\mathfrak{U} / \mathfrak{C}$ is the product of at most $q - 1$ cyclic groups and $u|(p - 1)^{q - 1}$. For $1 \leq j \leq p - 1$$\xi_j$ is induced by a linear character of $\mathfrak{P}\mathfrak{C}$, $\xi_j(1) = uq$. Either $\mathfrak{P}\mathfrak{U}$ is a Frobenius group with $|\mathfrak{P}| = p^q$ and

$$
u = \frac {p ^ {q} - 1}{p - 1}
$$

or S contains an irreducible character of degree uq which is induced by a linear character of PC.

Proof. If $\mathfrak{P}^* \subseteq D(\mathfrak{P})$ then by 3.16(i) $\mathfrak{P}\mathfrak{U}/D(\mathfrak{P})$ is nilpotent. Thus $\mathfrak{P}\mathfrak{U}$ is nilpotent contrary to assumption. Hence $\mathfrak{P}$ contains a subgroup $\mathfrak{P}_0$ such that $\mathfrak{P}^* \cap \mathfrak{P}_0 = 1$ and $\mathfrak{P}/\mathfrak{P}_0$ is a chief factor of $\mathfrak{S}$. Hence $\mathfrak{U}\mathfrak{Q}^*$ is represented on the elementary abelian group $\mathfrak{P}/\mathfrak{P}_0$. By 3.16 (i) $\mathfrak{P}_0\mathfrak{U}$ is nilpotent. Therefore $\mathfrak{U}\mathfrak{Q}^*/\mathfrak{C}$ is faithfully and irreducibly represented on $\mathfrak{P}/\mathfrak{P}_0$. By 3.16 (iii) $|\mathfrak{P}: \mathfrak{P}_0| = p^q$.

Let $\mathfrak{P} / \mathfrak{P}_0 = \mathfrak{P}_0\mathfrak{P}^* /\mathfrak{P}_0\times \mathfrak{P}_1 / \mathfrak{P}_0$ , where $\mathfrak{Q}^{*}\subseteq N(\mathfrak{P}_{1})$ . By Lemma 4.6 (i) $N_{\mathfrak{U}}(\mathfrak{P}_1)\subseteq C_{\mathfrak{U}}(\mathfrak{P}_1 / \mathfrak{P}_0)$ . Thus $N_{\mathfrak{U}}(\mathfrak{P}_1)\subseteq C_{\mathfrak{U}}(\mathfrak{P}) = \mathfrak{C}$ . Hence any non principal linear character of $\mathfrak{PC} / \mathfrak{P}_1\mathfrak{C}$ induces $\xi_j$ for some $j$ with $1\leq j\leq p - 1$ As $p$ is a prime the characters $\xi_j$ are algebraically conjugate for $1\leq j\leq p - 1$ . Thus $\xi_j(1) = uq$ for $1\leq j\leq p - 1$ . Let $\xi_j = \tilde{\psi}_j$ for $\psi_j$ a linear character of $\mathfrak{PC} / \mathfrak{P}_1\mathfrak{C}$

Suppose that $|\mathfrak{PC}: D(\mathfrak{PC})| > p^q$. Then PC contains a subgroup $\mathfrak{Q} \neq \mathfrak{P}_0\mathfrak{C}$ such that PC/H is a chief factor of $\mathfrak{S}$. Let $\lambda$ be a non principal linear character of PC/H. Then $\psi_1\lambda$ induces an irreducible character of $\mathfrak{S}$ of degree $uq$.

Suppose that $\mathfrak{U}$ is represented reducibly on $\mathfrak{P}/\mathfrak{P}_{0}$. Since $\mathfrak{U} \triangleleft \mathfrak{U}\mathfrak{Q}^{*}$ the irreducible constituents of this representation all have the same dimension. This dimension is 1 since $q$ is a prime. Thus $\mathfrak{U}/\mathfrak{C}$ is the direct product of $k$ cyclic subgroups for some integer $k$, each of which has order dividing $(p-1)$. No element of $\mathfrak{U}/\mathfrak{C}$ is represented as a scalar as $\mathfrak{U}\mathfrak{Q}^{*}$ is a Frobenius group. Therefore $k < q$ and $u|(p-1)^{q-1}$. The irreducible constituents of the representation of $\mathfrak{U}/\mathfrak{C}$ on $\mathfrak{P}/\mathfrak{P}_{0}$ are distinct since $\mathfrak{U}\mathfrak{Q}^{*}$ is irreducibly represented on $\mathfrak{P}/\mathfrak{P}_{0}$. Let $\mathfrak{P}/\mathfrak{P}_{0} = \mathfrak{P}_{1} \times \cdots \times \mathfrak{P}_{q}$ where $\mathfrak{P}_{i+1} = Q^{-i}\mathfrak{P}_{1}Q^{i}$ for some generator $Q$ of $\mathfrak{Q}^{*}$ and such that $\mathfrak{U}$ normalizes each $\mathfrak{P}_{i}$. Let

$$
P = \prod_ {i = 1} ^ {q} P _ {i}
$$

with $P_{1} \in \mathfrak{P}_{1}^{*}, P_{2} = Q^{-1}P_{1}^{-1}Q$ and $Q^{-i}P_{1}Q^{i} = P_{i+1}$ for $2 \leq i \leq q$ 1. Suppose $U \in \mathfrak{U}$ and $UQ^{j}$ centralizes $P$ for some $j$. Let $U^{-1}P_{i}U$$P_{i}^{a_{i}}$ then

$$
P \quad (U Q ^ {j}) ^ {- 1} P (U Q ^ {j}) = Q ^ {- j} \prod_ {i = 1} ^ {q} P _ {i} ^ {\alpha_ {i}} Q ^ {j}.
$$

Then $Q^{-j}P_{2}^{a_{2}}Q^{j}=P_{2+j}$. If $j\neq q$ then $P_{2+j}$ is conjugate to $P_{1}$. Hence $P_{2}^{a_{j}}$ is conjugate to $P_{2}^{-1}$ which is impossible as $|\mathfrak{U}\mathfrak{D}|$ is odd. Therefore $j=q$. Then $U^{-1}P_{i}U=P_{i}$ for $1\leqq i\leqq q$ and so $U\in\mathfrak{C}$. This proves that no element of $(\mathfrak{U}\mathfrak{D}/\mathfrak{C})^{\sharp}$ leaves P fixed. Let $\mu_{1}$ be a non principal linear character of $\mathfrak{P}/\mathfrak{P}_{0}$ with $\ker\mu_{1}=\mathfrak{P}_{2}\times\cdots\times\mathfrak{P}_{q}$. Let $\mu_{i}=\mu_{1}^{q^{i-1}}$; then $\mu=\mu_{1}\mu_{2}^{-1}\mu_{3}\cdots\mu_{q}$ induces an irreducible character of $\mathfrak{S}$ of degree uq.

Assume now that $\mathfrak{U}$ is irreducibly represented on $\mathfrak{P} / \mathfrak{P}_0$. Then $\mathfrak{U} / \mathfrak{C}$ is cyclic since $\mathfrak{U} / \mathfrak{C}$ is abelian. If a subgroup of $\mathfrak{U} / \mathfrak{C}$ acts reducibly on $\mathfrak{P} / \mathfrak{P}_0$ then it is represented by scalar matrices. As $\mathfrak{U}\mathfrak{Q}^*$ is a Frobenius group every non identity subgroup of $\mathfrak{U} / \mathfrak{C}$ acts irreducibly on $\mathfrak{P} / \mathfrak{P}_0$. Thus $\mathfrak{U} / \mathfrak{C}$ permutes the subgroups of order $p$ in $\mathfrak{P} / \mathfrak{P}_0$ and no element of $(\mathfrak{U} / \mathfrak{C})^*$ leaves any such subgroup fixed. Hence

$$
u \left| \frac {p ^ {q} - 1}{p - 1} \right..
$$

Suppose now that $\mathcal{S}$ contains no irreducible character of degree $uq$. By an earlier part of the lemma this implies that $|\mathfrak{P}\mathfrak{C}:D(\mathfrak{P}\mathfrak{C})|=p^{q}$. Thus $\mathfrak{C}=1$ and $|\mathfrak{P}:D(\mathfrak{P})|=p^{q}$. Since $D(\mathfrak{P})\cap\mathfrak{P}^{*}=1$, we must have $D(\mathfrak{P})=\mathfrak{P}'$. By 3.16 (i) $\mathfrak{P}'\mathfrak{U}$ is nilpotent. If $\mathfrak{P}'\neq1$ then there exists a subgroup $\mathfrak{P}_{1}$ of $\mathfrak{P}'$ such that $|\mathfrak{P}':\mathfrak{P}_{1}|=p$. Hence $\mathfrak{P}'/\mathfrak{P}_{1}$ is the center of $\mathfrak{P}/\mathfrak{P}_{1}$ since $\mathfrak{U}$ acts irreducibly on $\mathfrak{P}/\mathfrak{P}'$. Thus $\mathfrak{P}/\mathfrak{P}_{1}$ is an extra special $p$-group. This implies that $q$ is even which is not the case. Thus $\mathfrak{P}'=1$. Hence $\mathfrak{P}\mathfrak{U}$ is a Frobenius group. Consequently $\mathfrak{P}\mathfrak{U}$ contains $(p^{q}-1)/u$ irreducible characters of degree $u$. Lemma 13.7 now implies that

$$
u = \frac {p ^ {q} - 1}{p - 1}.
$$

LEMMA 34.2. Either $\mathfrak{P}\mathfrak{U}$ is a Frobenius group with $|\mathfrak{P}| = p^q$ and

$$
u = \frac {p ^ {q} - 1}{p - 1}
$$

or $\mathfrak{Q}\mathfrak{B}$ is a Frobenius group with $|\mathfrak{Q}| = q^p$ and

$$
v = \frac {q ^ {p} - 1}{q - 1}.
$$

Proof. If the result is false then Lemma 34.1 implies that S contains an irreducible character  $\lambda$  of degree uq and T contains an irreducible character  $\theta$  of degree vp. Every character in  $T^{r}$  is rational valued on P by Lemma 10.4. Since  $|G|$  is odd this implies that every generalized character of weight 1 in  $S^{r}$  is orthogonal to  $T^{r}$ . Define

$$
\alpha = \lambda - \xi_ {1}, \quad \beta = \theta - \zeta_ {1}.
$$

Then $\alpha(1) = \beta(1) = 0$ and $(\alpha^{\tau}, \beta^{\tau}) = 0$. Thus

$$
\begin{array}{r l} 0 = (\lambda^ {\tau} - \xi_ {1} ^ {\tau}, \theta^ {\tau} - \zeta_ {1} ^ {\tau}) & = \left(\pm \sum_ {i = 0} ^ {q - 1} \eta_ {i 1}, \pm \sum_ {j = 0} ^ {p - 1} \eta_ {1 j}\right) \\ & = \pm (\eta_ {1 1}, \eta_ {1 1}) = \pm 1. \end{array}
$$

This proves the lemma.

LEMMA 34.3. For $1 \leq j \leq p - 1$

$$
\sum_ {X \in (\mathfrak {P} \mathfrak {E}) ^ {\sharp}} | \eta_ {0 j} (X) | ^ {2} \geq u c | \mathfrak {P} | - u ^ {2}.
$$

Proof. Since PC is a T.I. set in G and S is coherent the Frobenius reciprocity theorem implies that for  $1 \leq j \leq p - 1$

$$
\eta_ {0 j} (X) = \varepsilon (\mu_ {0 j} (X) + \alpha (X)) \quad \text { for } X \in (\mathfrak {P C}) ^ {\sharp},
$$

where  $\alpha$  is a generalized character of  $S'/P$ , and  $\varepsilon^{2}=1$ . Therefore

$$
\begin{array}{r l} \sum_ {(\mathfrak {P} \in) ^ {\sharp}} | \eta_ {0 j} (X) | ^ {2} & = \sum_ {(\mathfrak {P} \in) ^ {\sharp}} \{\mu_ {0 j} (X) \overline {{\alpha (X)}} + \overline {{\mu_ {0 j} (X)}} \alpha (X) \} \\ & + \sum_ {(\mathfrak {P} \in) ^ {\sharp}} | \mu_ {0 j} (X) | ^ {2} + \sum_ {(\mathfrak {P} \in) ^ {\sharp}} | \alpha (X) | ^ {2}. \end{array}
$$

This implies that

$$
\begin{array}{r l} \sum_ {(\mathfrak {P} \in \mathbb {C}) ^ {\sharp}} | \eta_ {0 j} (X) | ^ {2} & = - 2 \mu_ {0 j} (1) \alpha (1) + c u | \mathfrak {P} | - u ^ {2} \\ & + | \mathfrak {P} | \sum_ {\sigma \in \mathbb {C}} | \alpha (C) | ^ {2} - \alpha (1) ^ {2}. \end{array}\tag{34.1}
$$

By Lemma 34.1, $2u + 1 \leq |\mathfrak{P}|$, thus

$$
\begin{array}{r l} - 2 \mu_ {0 j} (1) \alpha (1) + | \mathfrak {P} | \sum_ {\mathfrak {C}} | \alpha (C) | ^ {2} - \alpha (1) ^ {2} \\ & \geq | \mathfrak {P} | \sum_ {\mathfrak {C}} | \alpha (C) | ^ {2} - (2 u + 1) \alpha (1) ^ {2} \\ & \geq | \mathfrak {P} | \sum_ {\mathfrak {C} ^ {\sharp}} | \alpha (C) | ^ {2} \geq 0. \end{array}
$$

The result now follows from (34.1).

LEMMA 34.4. For $1 \leq i \leq q - 1$

$$
\sum_ {x \in \mathfrak {P} \mathfrak {C} - \mathfrak {C}} | \eta_ {i 0} (X) | ^ {2} \geq \{| \mathfrak {P} | - 1 \} c.
$$

Proof. Since PC is a T.I. set in G the coherence of S and the Frobenius reciprocity theorem imply that  $\eta_{i0}(X)=\alpha(X)$  for  $X\in P C-C$ , where  $\alpha$  is a generalized character of  $S'/P$ . Therefore for  $1\leq i\leq q-1$

$$
\begin{array}{r l} \sum_ {x \in \mathfrak {P C} - \mathfrak {C}} | \eta_ {i 0} (X) | ^ {2} & = \sum_ {x \in \mathfrak {P C} - \mathfrak {C}} | \alpha (X) | ^ {2} \\ & = \{| \mathfrak {P} | - 1 \} \sum_ {\mathfrak {C}} | \alpha (C) | ^ {2}. \end{array}\tag{34.2}
$$

If $P \in \mathfrak{P}^{**}$, $Q \in Q^{**}$ and $q$ is a prime divisor of $q$ in $\mathcal{Q}_{pq}$ then by Lemma 4.2

$$
\eta_ {i 0} (P) \equiv \eta_ {i 0} (P Q) \equiv 1 (\mathrm{mod} q).
$$

Thus the expression in (34.2) is non zero. The result now follows from the fact that

$$
\sum_ {\mathfrak {C}} | \alpha (C) | ^ {2} \equiv 0 (\mathrm{mod} c).
$$

LEMMA 34.5. Suppose that S contains an irreducible character λ of degree uq which is induced by a character of PC. Then

$$
\sum_ {X \in (\mathfrak {P} \mathbb {C}) ^ {\sharp}} | \lambda^ {\tau} (X) | ^ {2} > u q c | \mathfrak {P} | - (u q) ^ {2} - 2 u q ^ {2}.
$$

Proof. As PC is a T.I. set in G the coherence of S and the Frobenius reciprocity theorem imply that

$$
\lambda^ {\tau} (X) = \lambda (X) + \alpha (X) \quad \text { for } X \in (\mathfrak {P C}) ^ {\sharp},
$$

for some generalized character $\alpha$ of $\mathfrak{S}'/\mathfrak{P}$. Therefore

$$
\begin{array}{r l} \sum_ {(\mathfrak {P} \mathfrak {C}) ^ {\sharp}} | \lambda^ {\tau} (X) | ^ {2} & = \sum_ {(\mathfrak {P} \mathfrak {C}) ^ {\sharp}} | \lambda (X) | ^ {2} + \sum_ {(\mathfrak {P} \mathfrak {C}) ^ {\sharp}} \{\lambda (X) \alpha (\overline {{X}}) + \lambda (\overline {{X}}) \alpha (X) \} \\ & + \sum_ {(\mathfrak {P} \mathfrak {C}) ^ {\sharp}} | \alpha (X) | ^ {2} \geq u q c | \mathfrak {P} | - (u q) ^ {2} - 2 \lambda (1) \alpha (1) \\ & + \{| \mathfrak {P} | - 1 \} \sum_ {\mathfrak {C}} | \alpha (C) | ^ {2} + \sum_ {\mathfrak {C} ^ {\sharp}} | \alpha (C) | ^ {2}. \end{array}\tag{34.3}
$$

If $|\alpha(1)| \geq q$ then by Lemma 34.1

$$
2 \lambda (1) | \alpha (1) | = 2 u q | \alpha (1) | \leq 2 u \alpha (1) ^ {2} \leq \{| \mathfrak {P} | - 1 \} \alpha (1) ^ {2}.
$$

Hence the result follows from (34.3) in this case. If  $|\alpha(1)| < q$  then  $2\lambda(1)|\alpha(1)| < 2uq^{2}$  thus (34.3) also implies the result in this case.

LEMMA 34.6. Let $\mathfrak{G}_0$ be the set of elements in $\mathfrak{G}$ which are not conjugate to any element of $\mathfrak{P}\mathfrak{C}$, $\mathfrak{Q}$ or $\hat{\mathfrak{W}}$. Suppose that $\mathcal{S}$ contains an irreducible character $\lambda$ of degree $uq$. Define

$$
\begin{array}{l} \mathfrak {A} _ {1} = \{G \mid G \in \mathfrak {G} _ {0}, \lambda^ {\tau} (G) \neq 0 \} \\ \mathfrak {A} _ {2} = \{G \mid G \in \mathfrak {G} _ {0}, \eta_ {1 0} (G) \neq 0 \} \\ \mathfrak {A} _ {3} = \{G \mid G \in \mathfrak {G} _ {0}, \eta_ {0 1} (G) \neq 0, \eta_ {0 1} (G) \equiv 0 (\mathrm{mod} (q - 1)) \}. \end{array}
$$

Then

$$
\mathfrak {G} _ {0} = \mathfrak {A} _ {1} \cup \mathfrak {A} _ {2} \cup \mathfrak {A} _ {3}.
$$

Proof. Suppose that $G \in \mathfrak{G}_0 - (\mathfrak{A}_1 \cup \mathfrak{A}_2)$. Let $\alpha = \xi_1 - \lambda$. Then $(\xi_1 - \lambda)^{\tau}(G) = 0$ and

$$
(\xi_ {1} - \lambda) ^ {\tau} = \pm \sum_ {i = 0} ^ {q - 1} \eta_ {i 1} - \lambda^ {\tau}.
$$

Since $G \in \mathfrak{G}_0$, $\eta_{i1}(G)$ is rational. Thus $\eta_{i1}(G) = \eta_{i1}(G)$ for $1 \leq i \leq q - 1$. As $G \notin \mathfrak{A}_1 \cup \mathfrak{A}_2$ we must have that

$$
\begin{array}{r l} 0 \equiv \sum_ {i = 0} ^ {q - 1} \eta_ {i 1} (G) & \equiv \eta_ {0 1} (G) + (q - 1) \eta_ {1 1} (G) \\ & \equiv \eta_ {0 1} (G) (\mathrm{mod} (q - 1)). \end{array}\tag{34.4}
$$

Suppose that $\eta_{01}(G) = 0$. Then since $\alpha^{\mathrm{r}}(G) = 0$ we must have that $\eta_{i1}(G) = 0$ for $0 \leq i \leq q - 1$. Hence by Lemma 13.1

$$
0 = (1 _ {\mathfrak {G}} - \eta_ {1 0} - \eta_ {0 1} + \eta_ {1 1}) (G) = 1 - \eta_ {1 0} (G)
$$

contradicting the fact that $G \notin \mathfrak{A}_2$. Hence $\eta_{01}(G) \neq 0$ and by (34.4) $G \in \mathfrak{A}_3$ as required.

LEMMA 34.7.

(i) If $q \geq 5$ then $|\mathfrak{P}| = p^q$ and $u / c > 9p^{q-1} / 20q$.

(ii) If $p, q \geq 5$ then $c = 1$ and $u \geq (13/20)p^{q-1}/q$.

(iii) If $p = 3$ and $c \neq 1$ then $u = 121, q = 5, c = 11$.

(iv) If $q = 3$ then $c = 1$ or $c = 7$. Furthermore $u > (p^2 + p + 1)/13$.

(v) If $q = 3$ then $\mathfrak{P}$ is an elementary abelian $p$-group and $|\mathfrak{P}| = p^3$ or $p = 7, c = 1$ and $|\mathfrak{P}| = 7^4$.

(vi) If $q = 3$ and $c = 7$ then $u > (p^2 + p + 1)/2$.

Proof. If $\mathfrak{P}\mathfrak{U}$ is a Frobenius group with $|\mathfrak{P}| = p^q$, $u = (p^q - 1)/(p - 1)$ then all the statements in the lemma are immediate. Suppose that this is not the case. Then by Lemma 34.1 $\mathcal{S}$ contains an irreducible character $\lambda$ which is induced by a linear character of $\mathfrak{P}\mathfrak{C}$. By Lemma 34.2 $\mathfrak{D}\mathfrak{V}$ is a Frobenius group with $|\mathfrak{Q}| = q^p$, $v = (q^p - 1)/(q - 1)$, $d = 1$.

PC, $\mathfrak{D}$ and $\hat{\mathfrak{W}}$ are T.I. sets. Let $\mathfrak{G}_0, \mathfrak{A}_1, \mathfrak{A}_2, \mathfrak{A}_3$ have the same meaning as in Lemma 34.6. Then

$$
\begin{array}{r l} \frac {1}{g} | \mathfrak {G} _ {0} | & = 1 - \left(1 - \frac {1}{p} - \frac {1}{q} + \frac {1}{p q}\right) \\ & \quad - \frac {1}{q u c | \mathfrak {P} |} \{| \mathfrak {P} | c - 1 \} - \frac {1}{p v | \mathfrak {Q} |} \{| \mathfrak {Q} | - 1 \} \\ & = \frac {1}{p} + \frac {1}{q} - \frac {1}{p q} - \frac {1}{q u} - \frac {1}{p v} + \frac {1}{q u c | \mathfrak {P} |} + \frac {1}{p v q ^ {p}}. \end{array}\tag{34.5}
$$

Since $\lambda^{\tau}$ is rational valued on $\mathfrak{G}_0$ by Lemma 10.4, Lemma 34.5 implies that

$$
\begin{array}{l} \frac {1}{g} | \mathfrak {A} _ {1} | \leq \frac {1}{g} \sum_ {\mathfrak {A} _ {1}} | \lambda^ {\tau} (X) | ^ {2} \leq 1 - \frac {1}{| \mathfrak {P} | u c q} \sum_ {(\mathfrak {B C}) ^ {\sharp}} | \lambda^ {\tau} (X) | ^ {2} \\ <   \frac {u q}{| \mathfrak {P} | c} + \frac {2 q}{| \mathfrak {P} | c}. \end{array}\tag{34.6}
$$

If Lemma 34.3 is applied to $\mathfrak{T}$ then Lemmas 13.1 and 34.4 yield that

$$
\begin{array}{l} \frac {1}{g} | \mathfrak {A} _ {2} | \leq \frac {1}{g} \sum_ {\mathfrak {A} _ {2}} | \eta_ {1 0} (X) | ^ {2} \\ \text {(34.7)} \quad \leq 1 - \left(1 - \frac {1}{p} - \frac {1}{q} + \frac {1}{p q}\right) - \frac {1}{p v q ^ {p}} \{v q ^ {p} - v ^ {2} \} - \frac {1}{| \mathfrak {P} | u q c} \{| \mathfrak {P} | - 1 \} c \\ = \frac {1}{q} - \frac {1}{p q} + \frac {v}{p q ^ {p}} - \frac {1}{u q} + \frac {1}{| \mathfrak {P} | u q}. \end{array}
$$

Lemmas 13.1 and 34.3 also imply that

$$
\begin{array}{r l} \frac {1}{g} | \mathfrak {A} _ {3} | & \leq \frac {1}{(q - 1) ^ {2}} \frac {1}{g} \sum_ {\mathfrak {A} _ {3}} | \eta_ {0 1} (X) | ^ {2} \\ & \leq \frac {1}{(q - 1) ^ {2}} \left\{1 - \left(1 - \frac {1}{p} - \frac {1}{q} + \frac {1}{p q}\right) - \frac {1}{q u c | \mathfrak {P} |} (u c | \mathfrak {P} | - u ^ {2}) \right\} \\ & = \frac {1}{(q - 1) ^ {2}} \left\{\frac {(q - 1)}{p q} + \frac {u}{q c | \mathfrak {P} |} \right\}. \end{array}\tag{34.8}
$$

Lemma 34.6 and (34.5), (34.6), (34.7) and (34.8) now imply that

$$
\begin{array}{r l} \frac {1}{p} + \frac {1}{q u c | \mathfrak {P} |} - \frac {1}{p v q ^ {p}} (q ^ {p} - 1) + \frac {1}{q} - \frac {1}{p q} - \frac {1}{q u} & \leq \frac {u q}{| \mathfrak {P} | c} \\ & + \frac {2 q}{| \mathfrak {P} | c} + \frac {1}{| \mathfrak {P} | u q} + \frac {v}{p q ^ {p}} + \frac {1}{q} - \frac {1}{p q} - \frac {1}{q u} \\ & + \frac {1}{p q (q - 1)} + \frac {u}{q c | \mathfrak {P} | (q - 1) ^ {2}}. \end{array}
$$

Since $v = (q^p - 1) / (q - 1)$, this can be simplified to

$$
\begin{array}{r l} \frac {1}{p} & \leqslant \frac {(u + 2) q}{| \mathfrak {P} | c} + \frac {(c - 1)}{| \mathfrak {P} | q u c} + \frac {1}{p (q - 1)} - \frac {1}{p q ^ {p} (q - 1)} \\ & \quad + \frac {(q - 1)}{p q ^ {p}} + \frac {1}{p q (q - 1)} + \frac {u}{q c | \mathfrak {P} | (q - 1) ^ {2}} \\ & = \frac {(u + 2) q}{| \mathfrak {P} | c} + \frac {(c - 1)}{| \mathfrak {P} | q u c} + \frac {u}{q c | \mathfrak {P} | (q - 1) ^ {2}} \\ & \quad + \frac {(q + 1)}{p q (q - 1)} + \frac {(q - 1) ^ {2} - 1}{p q ^ {p} (q - 1)}. \end{array}\tag{34.9}
$$

By Lemma 34.1 $u \leq (p^q - 1)/(p - 1)$ and $|\mathfrak{P}| \geq p^q$; thus (34.9) implies that

'34.10)

$$
\begin{array}{r l} \frac {1}{p} & \leq \frac {(u + 2) q}{| \mathfrak {P} | c} + \frac {(q + 1)}{p q (q - 1)} + \frac {1}{c (p - 1) q (q - 1) ^ {2}} \\ & \quad + \frac {1}{p ^ {q} q} + \frac {1}{p q ^ {p - 1}}. \end{array}
$$

Let $|\mathfrak{P}| = p^q x$ then

(34.11)

$$
x \equiv c \equiv 1 (\mathrm{mod} 2 q) .
$$

Suppose first that $p, q \geq 5$. Then (34.10) implies that

$$
\frac {1}{p} \leq \frac {u q}{p ^ {a} x c} + \frac {2 q}{p ^ {a} x c} + \frac {3}{1 0 p} + \frac {1}{8 0 (p - 1)} + \frac {2}{5 ^ {4} p}.
$$

Hence by (5.2)

$$
\frac {1}{p} <   \frac {u q}{p ^ {q} x c} + \frac {1}{4 0 p} + \frac {3}{1 0 p} + \frac {3 / 2}{8 0 p} + \frac {1 / 2}{8 0 p}.
$$

Therefore

(34.12)

$$
\frac {q}{x c} \frac {u}{p ^ {q}} > \frac {1 3}{2 0 p}.
$$

Therefore

(34.13)

$$
\frac {1}{x c} u > \frac {1 3 p ^ {q - 1}}{2 0 q} > \frac {p ^ {q - 1}}{2 q}.
$$

Suppose that $cx \neq 1$. Then by (34.11) $cx > 2q$. Thus (34.12) implies that

$$
\frac {1 3}{2 0 p} <   \frac {1}{2} \frac {u}{p ^ {q}} <   \frac {1}{2} \frac {1}{(p - 1)}.
$$

Thus $13(p - 1) < 10p$ or $3p < 13$ which is not the case. Hence $c = x = 1$ and (34.13) completes the proof of statement (ii) of the lemma. Suppose now that $p = 3$. Hence (34.10) yields that

(34.14)

$$
\frac {1}{3} \leq \frac {(u + 2) q}{c x 3 ^ {q}} + \frac {(q + 1)}{3 q (q - 1)} + \frac {1}{2 q (q - 1) ^ {2}} + \frac {1}{3 ^ {q} q} + \frac {1}{3 q ^ {2}}.
$$

As $q \geq 5$ this implies that

$$
\frac {1}{3} \leq \frac {q}{c x} \frac {u}{3 ^ {q}} + \frac {1}{1 0} + \frac {1}{1 6 0} + \frac {(2 q ^ {2} + 1)}{3 ^ {q} q} + \frac {1}{7 5}.
$$

Hence by (5.3)

$$
\begin{array}{r l} \frac {q}{c x} \frac {u}{3 ^ {q}} & \geq \frac {1}{3} - \frac {1}{1 0} - \frac {1}{1 6 0} - \frac {1}{2 0} - \frac {1}{7 5} \\ & > \frac {1 6 0 - 4 8 - 3 - 2 4 - 1 0}{4 8 0} = \frac {7 5}{4 8 0} > \frac {3}{2 0}. \end{array}
$$

Thus

(34.15)

$$
\frac {u}{c x} > \frac {3}{2 0} \cdot \frac {3 ^ {q}}{q}.
$$

This yields that

$$
\frac {2 q}{c x} > \frac {9}{1 0} \cdot \frac {3 ^ {q - 1}}{u} > \frac {3}{5}.
$$

Hence $4q > cx$.

Assume that $cx \neq 1$. Then (34.11) implies that

$$
c x = 2 q + 1.\tag{34.16}
$$

Suppose first then $q \geq 11$. Then (34.14) implies that

$$
\frac {1}{3} \leq \frac {q}{c x} \frac {u}{3 ^ {q}} + \frac {2}{5 5} + \frac {1}{2 . 1 0 ^ {3}} + \frac {1}{1 0 . 3 ^ {1 0}} + \frac {2 q}{c x} \frac {1}{3 ^ {1 0}} + \frac {1}{3 0 0}.
$$

Hence

$$
\frac {q}{c x} \frac {u}{3 ^ {q}} > \frac {1}{3} - \frac {2}{5 5} - \frac {1}{6 0} > \frac {1}{3} - \frac {3}{5 4} = \frac {5}{1 8}.
$$

Therefore

$$
\frac {q}{c x} > \frac {3 ^ {q}}{u} \frac {5}{1 8} > \frac {2 . 5}{1 8} > \frac {1}{2}
$$

contrary to (34.16). Suppose that $q = 7$. Then $cx = 15$ by (34.16). Thus $x = 3$ and $c = 5$ since $x$ is a power of 3 and $(c, 3) = 1$. This contradicts (34.11). Hence $q = 5$. Thus by (34.16) $cx = 11$. Hence $x = 1$ and $c = 11$ since $x$ is a power of 3. Thus statement (i) of the lemma follows from (34.15) and statement (ii). If $c \neq 1$ then $q = 5$ and $c = 11$. By (34.15)

(34.17)

$$
u > \frac {1 1 . 3 ^ {5}}{1 0 0} > 2 ^ {4} = (p - 1) ^ {q - 1}.
$$

Hence by Lemma 34.1 $u \mid (3^5 - 1)/2 = 121$. Thus $u = 121$ by (34.17). This completes the proof of statement (iii) of the lemma.

Assume now that q = 3. Let  $y = (p^{2} + p + 1)/u$ . (y is not necessarily integral) Then (34.9) implies that

$$
\begin{array}{r l} \frac {1}{p} <   & \frac {3 (p ^ {2} + p + 1)}{c x y p ^ {3}} + \frac {6}{c x p ^ {3}} + \frac {1}{3 p ^ {3} u} \\ & + \frac {(p ^ {2} + p + 1)}{1 2 c x y p ^ {3}} + \frac {2}{3 p} + \frac {1}{2 p 3 ^ {p - 1}}. \end{array}
$$

Therefore

$$
\frac {1}{3 p} <   \frac {3 7 (p ^ {2} + p + 1)}{1 2 c x y p ^ {3}} + \frac {6}{c x p ^ {3}} + \frac {1}{3 p ^ {3} u} + \frac {1}{2 p 3 ^ {p - 1}},
$$

or

$$
1 <   \frac {3 7 (p ^ {2} + p + 1)}{4 c x y p ^ {2}} + \frac {1 8}{c x p ^ {2}} + \frac {1}{p ^ {2} u} + \frac {1}{2 \cdot 3 ^ {p - 2}}.\tag{34.18}
$$

Suppose that $cxy \geq 13$. Then (34.18) implies that

$$
\frac {3 7}{5 2} \frac {(p ^ {2} + p + 1)}{p ^ {2}} > 1 - \frac {1 9}{p ^ {2}} - \frac {1}{5 2}.
$$

Therefore $37(p^{2} + p + 1) > 51p^{2} - 52 \cdot 19$, or

$$
1 4 p ^ {2} - 3 7 p - 5 2 \cdot 1 9 - 3 7 <   0.
$$

Therefore, $p < 11$. Hence $p = 5$ or $p = 7$. Since $(6, u) = 1$, Lemma 34.1 now implies that $u | p^2 + p + 1$. Thus $u | 31$ if $p = 5$ and $u | 57$ if $p = 7$. Hence one of the following must occur:

$$
p = 5, \quad u = 3 1, \quad y = 1, \quad c x \geq 1 3
$$

or

$$
p = 7, \quad u = 1 9, \quad y = 3, \quad c x \geq 5.
$$

By (34.11)

$$
c x = 7, \quad p = 7 \text { or } c x \geq 1 3.
$$

If $cx \geq 13$ then by (34.18)

$$
1 <   \frac {3 7}{5 2} \frac {(p ^ {2} + p + 1)}{p ^ {2}} + \frac {1 9}{1 3 p ^ {2}} + \frac {1}{5 2}.
$$

Hence $p < 5$, which is not the case. Therefore we have shown that either $cxy < 13$ or $p = 7$, $u = 19$, $y = 3$ and $cx = 7$. If $cxy < 13$, then $y < 13$, and by (34.11) $cx = 7$ or $cx = 1$. Thus in any case

$$
u > \frac {p ^ {2} + p + 1}{1 3}, c x = 1 \quad \text { or } c x = 7.\tag{34.19}
$$

This proves statement (iv) of the lemma.

If $x \neq 1$ then (34.19) implies that $c = 1$ and $x = 7$, hence $p = 7$ and $|\mathfrak{P}| = 7^4$. Since $(u, 6) = 1$, Lemma 34.1 implies that $u|57$, thus $u = 19$. If $D(\mathfrak{P}) \neq 1$ then $\mathfrak{U}$ acts irreducibly on $\mathfrak{P}/D(\mathfrak{P})$ and centralizes $D(\mathfrak{P})$. If $\mathfrak{P}$ is non abelian this implies that $D(\mathfrak{P}) = Z(\mathfrak{P})$. Hence $\mathfrak{P}$ is an extra special $p$-group contrary to the fact that $|\mathfrak{P}: D(\mathfrak{P})| = p^3$. Thus $\mathfrak{P}$ is abelian. Hence $|\mathfrak{P}: \Omega_1(\mathfrak{P})| \leq p$. If $\Omega_1(\mathfrak{P}) \neq \mathfrak{P}$ this implies that $\mathfrak{U}\Omega$ is represented on $\Omega_1(\mathfrak{P})$ and so $\mathfrak{U}$ acts irreducibly on $\Omega_1(\mathfrak{P})$ contrary to $D(\mathfrak{P}) \subseteq \Omega_1(\mathfrak{P})$ and $\mathfrak{U} \subseteq C(D(\mathfrak{P}))$. Thus $\mathfrak{P}$ is elementary abelian. Statement (v) of the lemma is proved.

Suppose that $c = 7$ and $y \geq 2$; then (34.18) implies that

$$
1 <   \frac {3 7}{5 6} \frac {(p ^ {2} + p + 1)}{p ^ {2}} + \frac {1 9}{7 p ^ {2}} + \frac {1}{5 4}.
$$

Therefore, p < 5 which is impossible. Hence if c = 7 then y < 2. This proves statement (vi) of the lemma and completes the proof of Lemma 34.7.

LEMMA 34.8. If $q \geq 5$ then $\mathfrak{P}\mathfrak{U}/\mathfrak{C}$ is a Frobenius group and $u | (p^q - 1)/(p - 1)$.

Proof. By Lemma 34.7 (i) $|\mathfrak{P}| = p^q$. Thus if $\mathfrak{M} / \mathfrak{C}$ is not a Frobenius group then by Lemma 34.1 $u | [(p - 1)/2]^{q-1}$. Thus by Lemma 34.7 (i)

$$
\frac {p ^ {q - 1}}{2 ^ {q - 1}} > u > \frac {9 \cdot p ^ {q - 1}}{2 0 q}.
$$

Therefore  $q > 2^{q-2} \cdot (9/10)$  which is not the case, since  $q \geq 5$ .

LEMMA 34.9. If $p, q \geq 5$ then $c = 1$, $|\mathfrak{P}| = p^q$ and either $u = (p^q - 1) / (p - 1)$ or $p \equiv 1 (\bmod q)$ and $u = 1 / q [(p^q - 1) / (p - 1)]$.

Proof. By Lemma 34.7(ii) $c = 1$. Lemma 34.8 implies that $|\mathfrak{P}| = p^q$ and $u|(p^q - 1)/(p - 1)$. Let $ux = (p^q - 1)/(p - 1)$. If $p \not\equiv 1 \pmod{q}$ then

$$
u \equiv \frac {p ^ {q} - 1}{p - 1} \equiv 1 (\mathrm{mod} 2 q).
$$

Thus $x \equiv 1 \pmod{2q}$. If $p \equiv 1 \pmod{q}$ then $(p^q - 1) / (p - 1) \equiv 0 \pmod{q}$. Hence $x \equiv 0 \pmod{q}$ as $(u, q) = 1$. Thus in any case $x \geq 2q$ if the result is false. Now Lemma 34.7 (ii) implies that

$$
\frac {p ^ {q} - 1}{p - 1} = u x \geq 2 q u \geq \frac {1 3}{1 0} p ^ {q - 1}.
$$

Hence

$$
p ^ {q} > p ^ {q} - 1 \geq \frac {1 3}{1 0} p ^ {q} - \frac {1 3}{1 0} p ^ {q - 1}.
$$

Thus $13 > 3p$ contrary to the fact that $p \geq 5$.

LEMMA 34.10.

$$
\begin{array}{r l} | N (\mathfrak {B} ^ {*}) \colon \mathfrak {B} ^ {*} C (\mathfrak {B} ^ {*}) | & = p o r p q \quad i f p, q \geq 5 o r p = 3, q \geq 7 \\ & = 3 o r 1 5 o r 3 3 \quad i f p = 3, q = 5 \\ & = p, 3 p o r 7 p \quad i f q = 3. \end{array}
$$

Proof. Let $\mathfrak{C}$ be a complement of $\mathfrak{B}^* C(\mathfrak{B}^*)$ in $N(\mathfrak{B}^*)$ which contains $\mathfrak{P}^*$. Every Sylow subgroup of $\mathfrak{C}$ is cyclic and every subgroup of prime order is normal in $\mathfrak{C}$ by 3.16 (ii) and Theorem 33.1. Thus $\mathfrak{C} \subseteq N(\mathfrak{P}^*) = \Omega^*\mathfrak{P}\mathfrak{C}$. Hence $\mathfrak{C} = \mathfrak{P}^*$ or $|\mathfrak{C}| = pq$ or $\mathfrak{C} \subseteq \mathfrak{P}^*\mathfrak{C}$. The result now follows from Lemma 34.7.

By Theorem 33.1 $\mathfrak{U}^*$ is tamely imbedded in $\mathfrak{G}$ unless $\mathfrak{U}^* = \mathfrak{U}$ and $C_{\mathfrak{P}}(\mathfrak{U}) \neq 1$. By Lemma 34.7 this can only happen if $p = 7$ and $q = 3$. In that case let $\mathcal{U}$ be the set of characters of $\mathfrak{G}$ which are induced by non principal irreducible characters of $\mathfrak{S}' / \mathfrak{P}$. In all other cases let $\mathcal{U}_0 = \mathcal{U}$. Define $\mathcal{V}$ similarly. Then $\mathcal{I}_0(\mathcal{U})^\tau$ and $\mathcal{I}_0(\mathcal{V})^\tau$ are always defined.

LEMMA 34.11. Suppose that $\mathcal{V}$ is coherent and $p > q$. If

$$
\frac {d v ^ {*} - 1}{| N (\mathfrak {B} ^ {*}) : \mathfrak {B} ^ {*} |} > \frac {v - 1}{p}
$$

and

$$
\frac {d v ^ {*} - 1}{| N (\mathfrak {B} ^ {*}) : \mathfrak {B} ^ {*} |} > \frac {u - 1}{q}
$$

then $|N(\mathfrak{B}^*): \mathfrak{B}^*| \geqq pq$. If furthermore $|N(\mathfrak{B}^*): \mathfrak{B}^*| = pq$ then $1/p \leq pq / v^*d$.

Proof. Let $e = |N(\mathfrak{B}^*) : \mathfrak{B}^*|$. Let $\psi \in \mathcal{V}$ with $\psi(1) = e$. Let $\alpha = \widetilde{1}_{\mathfrak{B}^*} - \psi$. Then $||\alpha^\tau||^2 = ||\alpha||^2 = e + 1$. Define

$$
\beta_ {\mathfrak {S}} = \widetilde {1} _ {\mathfrak {D} ^ {*} \mathfrak {P C}} - \mu_ {0 1}, \quad \beta_ {\mathfrak {T}} = \widetilde {1} _ {\mathfrak {P} ^ {*} \mathfrak {D D}} - \nu_ {1 0}.
$$

$\beta_{\mathfrak{S}}, \beta_{\mathfrak{T}}$ vanish on $\mathfrak{S} - \hat{\mathfrak{S}}_1, \mathfrak{T} - \hat{\mathfrak{T}}_1$ respectively. As $\hat{\mathfrak{S}}_1$ and $\hat{\mathfrak{T}}_1$ are T.I. sets in $\mathfrak{G}$

(34.20) $||\beta_{\mathfrak{S}}^{*}||^{2} = ||\beta_{\mathfrak{S}}||^{2} = \frac{u - 1}{q} +2$ ， $||\beta_{\mathfrak{T}}^{*}||^{2} = ||\beta_{\mathfrak{T}}||^{2} = \frac{v - 1}{p} +2.$

Furthermore by Lemma 13.8

(34.21)

$$
\beta_ {\mathfrak {S}} ^ {*} = 1 _ {\mathfrak {S}} \pm \eta_ {0 1} + \Gamma_ {\mathfrak {S}}, \quad \beta_ {\mathfrak {T}} ^ {*} = 1 _ {\mathfrak {S}} \pm \eta_ {1 0} + \Gamma_ {\mathfrak {T}}
$$

where $\Gamma_{\mathfrak{G}}, \Gamma_{\mathfrak{T}}$ are real valued generalized characters of $\mathfrak{G}$ which are orthogonal to $1_{\mathfrak{G}}$. The assumed inequalities and (34.20) imply that $(\psi^{\tau}, \beta_{\mathfrak{G}}^{*}) = 0 = (\psi^{\tau}, \beta_{\mathfrak{T}}^{*})$. Thus if $\alpha^{\tau} = 1_{\mathfrak{G}} \pm \psi^{\tau} + \Gamma_{\mathfrak{B}}$ then

$$
0 \equiv (\alpha^ {\tau}, \beta_ {\mathfrak {G}} ^ {*}) \equiv 1 + (\eta_ {0 1}, \Gamma_ {\mathfrak {B}}) (\mathrm{mod} 2)
$$

$$
0 \equiv (\alpha^ {\tau}, \beta_ {\mathfrak {L}} ^ {*}) \equiv 1 + (\eta_ {1 0}, \Gamma_ {\mathfrak {B}}) (\mathrm{mod} 2).
$$

Since $\Gamma_{\mathfrak{B}}$ is rational valued on $\hat{\mathfrak{W}}$ this implies that

$$
(\eta_ {i 0}, \Gamma_ {\mathfrak {B}}) \equiv (\eta_ {0 j}, \Gamma_ {\mathfrak {B}}) \equiv 1 \pmod {2}
$$

for $1 \leq i \leq q - 1$, $1 \leq j \leq p - 1$. Hence by Lemma 13.1

$$
\begin{array}{r l} (1 _ {\mathfrak {G}} - \eta_ {i 0} - \eta_ {0 j} + \eta_ {i j}, \alpha^ {\mathrm{r}}) & \equiv 1 + (\eta_ {i 0}, \Gamma_ {\mathfrak {G}}) \\ & + (\eta_ {0 j}, \Gamma_ {\mathfrak {G}}) + (\eta_ {i j}, \Gamma_ {\mathfrak {G}}) \pmod 2. \end{array}
$$

Thus $(\eta_{ij},\Gamma_{\mathfrak{g}})\neq 0$ for $1\leq i\leq q - 1,1\leq j\leq p - 1.$ Hence

$$
e + 1 = \left\| \alpha^ {\tau} \right\| ^ {2} \geq p q + 1.
$$

Suppose now that $e = pq$ then

$$
\alpha^ {\tau} = 1 _ {\mathfrak {G}} \pm \psi^ {\tau} \pm \sum_ {i = 1} ^ {q - 1} \eta_ {i 0} \pm \sum_ {j = 1} ^ {p - 1} \eta_ {0 j} \pm \sum_ {i = 1} ^ {q - 1} \sum_ {j = 1} ^ {p - 1} \eta_ {i j}.\tag{34.22}
$$

Let $\mathfrak{G}_0$ be the set of elements in $\mathfrak{G}$ which are conjugate to some element of $\mathfrak{A}_{\nu}$ with $V \in \mathfrak{B}^{*\#}$. Since $\mathcal{V}$ is coherent by assumption, (34.22) Lemmas 33.1 and 9.4 imply that $\psi^{\tau}(VC) = \psi(V)$ for $VC \in \mathfrak{A}_{\nu}$, $V \in \mathfrak{B}^{*\#}$. Furthermore Lemma 9.5 and (34.22) imply that

$$
\frac {1}{g} \sum_ {\mathfrak {G} _ {0}} | \psi^ {\tau} (G) | ^ {2} = \frac {1}{p q v ^ {*} d} \sum_ {\mathfrak {B} ^ {* \sharp}} | \psi (G) | ^ {2} = 1 - \frac {p q}{v ^ {*} d}.\tag{34.23}
$$

By Lemma 9.5

$$
\frac {1}{g} \left| \mathfrak {G} _ {0} \right| = \frac {1}{g} \sum_ {\mathfrak {G} _ {0}} 1 _ {\mathfrak {G}} (G) = \frac {1}{p q v ^ {*} d} \sum_ {\mathfrak {B} ^ {* *}} 1 _ {\mathfrak {G}} (G) = \frac {(d v ^ {*} - 1)}{d v ^ {*} p q}.\tag{34.24}
$$

Let $\mathfrak{G}_1$ be the set of elements in $\mathfrak{G} - \mathfrak{G}_0$ which are not conjugate to any element of $\hat{\mathfrak{W}}$, $\mathfrak{P}\mathfrak{C}$ or $\mathfrak{Q}\mathfrak{D}$. Now (34.22) implies that if $G \in \mathfrak{G}_1$ then $\psi^{\tau}(G)$ is rational and

$$
0 \equiv \alpha^ {\tau} (G) \equiv 1 + \psi^ {\tau} (G) (\mathrm{mod} 2).
$$

Thus $|\psi^{\tau}(G)|^{2} \geq 1$ for $G \in \mathfrak{G}_{1}$. Hence (34.23) implies that

$$
\begin{array}{r l} \frac {p q}{v ^ {*} d} & \geq \frac {1}{g} | \mathfrak {G} _ {1} | \geq 1 - \frac {(v d ^ {*} - 1)}{p q v ^ {*} d} - \left(1 - \frac {1}{p} - \frac {1}{q} + \frac {1}{p q}\right) \\ & \quad - \frac {| \mathfrak {P C} | - 1}{q u | \mathfrak {P} | c} - \frac {| \mathfrak {D D} | - 1}{p v | \mathfrak {D} | d}. \end{array}
$$

Therefore

$$
\begin{array}{r l} \frac {p q}{v ^ {*} d} & \geq \frac {1}{p} + \frac {1}{q} - \frac {1}{p q} - \frac {1}{p q} + \frac {1}{p q v ^ {*} d} - \frac {1}{q u} + \frac {1}{q u | \mathfrak {P} | c} \\ & - \frac {1}{p v} + \frac {1}{p v | \mathfrak {Q} | d}. \end{array}
$$

:Since $u > 2q$, $v > 2p$ and $p > q \geq 3$

$$
\frac {1}{p q} + \frac {1}{p q} + \frac {1}{q u} + \frac {1}{p v} <   \frac {3}{q ^ {2}} \leq \frac {1}{q};
$$

thus the required inequality follows.

LEMMA 34.12. If $\mathfrak{U}^*$ is cyclic then $\mathfrak{U}^*$ is a T.I. set in $\mathfrak{G}$ unless $\mathfrak{U}^* = \mathfrak{U}$ and $N(\mathfrak{U}) \subseteq \mathfrak{S}$.

Proof. Since $\mathfrak{U}^*$ is a cyclic $S$-subgroup in $N(\mathfrak{U}^*)$, $\mathfrak{U}^*$ is a $S$-subgroup of $\mathfrak{G}$. Suppose that $\mathfrak{U}^*$ is not a T.I. set in $\mathfrak{G}$ and let $1 \neq \mathfrak{U}^* \cap G^{-1}\mathfrak{U}^*G = \mathfrak{U}_0 \subseteq \mathfrak{U}^*$. Then $\{N(\mathfrak{U}^*), N(G^{-1}\mathfrak{U}^*G)\} \subseteq N(\mathfrak{U}_0)$. Since $N(\mathfrak{U}^*)$ is a maximal subgroup of $\mathfrak{G}$ this implies that $\{\mathfrak{U}^*, G^{-1}\mathfrak{U}^*G\} \subseteq N(\mathfrak{U}^*)$. Thus $G^{-1}\mathfrak{U}^*G = \mathfrak{U}^*$ and $\mathfrak{U}^*$ is a T.I. set in $\mathfrak{G}$.

## 35. Further Results About & and T

The notation of Section 34 is used in this section. However we will destroy the symmetry of $\mathfrak{S}$ and $\mathfrak{T}$ by choosing the notation so that

(35.1)

$$
q <   p.
$$

The next three lemmas are restatements of Lemmas 34.7, 34.8, 34.9 and 34.10.

LEMMA 35.1. If $q \geq 5$ then $c = d = 1$, $v = (q^p - 1) / (q - 1)$, $|\mathfrak{P}| = p^q$ and $|\mathfrak{Q}| = q^p$. Either $u = (p^q - 1) / (p - 1)$ or $p \equiv 1 (\bmod q)$ and $u = 1 / q [(p^q - 1) / (p - 1)]$. Furthermore $\mathfrak{P}\cup$ and $\mathfrak{Q}\cup$ are Frobenius groups.

$$
\left| N \left(\mathfrak {U} ^ {*}\right): \mathfrak {U} ^ {*} \right| = q o r p q a n d \left| N \left(\mathfrak {V} ^ {*}\right): \mathfrak {V} ^ {*} \right| = p o r p q.
$$

LEMMA 35.2. Suppose that $q = 3$. Then $|\mathfrak{Q}| = 3^p$,

$$
\frac {v}{d} > \frac {9}{2 0} \cdot \frac {3 ^ {p - 1}}{p}
$$

and $\mathfrak{D}\mathfrak{B} / \mathfrak{D}$ is a Frobenius group with $v|(3^p -1) / 2$. Either $d = 1$ or $d = 11$, $p = 5$ and $v = 121$. Furthermore $\mathcal{V} = \mathcal{V}_0$ and

$$
\mid N (\mathfrak {V} ^ {*}): \mathfrak {V} ^ {*} \mid = p, 3 p o r 7 p.
$$

LEMMA 35.3. Suppose that $q = 3$. Then

$$
\begin{array}{r l} | N (\mathfrak {U} ^ {*}) \colon \mathfrak {U} ^ {*} C (\mathfrak {U} ^ {*}) | & = 3 o r 3 p \quad i f p \geq 7 \\ & = 3, 1 5 o r 3 3 \quad i f p = 5. \end{array}
$$

Furthermore one of the following possibilities occurs:

(i) $c = 1, u > (p^2 + p + 1)/13$, $\mathfrak{P}$ is an elementary abelian $p$-group with $|\mathfrak{P}| = p^3$ or $|\mathfrak{P}| = 7^4$.

(ii) $c = 7, u > (p^2 + p + 1)/2$, $\mathfrak{P}$ is an elementary abelian $p$-group with $|\mathfrak{P}| = p^3$.

LEMMA 35.4. Either $q = 3, p = 5, v = 11, u = 31$ or

$$
\frac {v - 1}{p} > \frac {u - 1}{q}.
$$

Proof. By (5.12)

$$
q ^ {2} \frac {(q ^ {p - 1} - 1)}{q - 1} > p ^ {2} \frac {(p ^ {q - 1} - 1)}{p - 1}.
$$

Therefore if $v = (q^p - 1) / (q - 1)$ then by Lemma 34.1

$$
\begin{array}{r l} \frac {v - 1}{p} & = \frac {1 + \cdots + q ^ {p - 1} - 1}{p} = \frac {q (q ^ {p - 1} - 1)}{p (q - 1)} \\ & > \frac {p (p ^ {q - 1} - 1)}{q (p - 1)} = \frac {\frac {p ^ {q} - 1}{p - 1} - 1}{q} \geq \frac {u - 1}{q}. \end{array}
$$

Suppose now that $v \neq (q^p - 1) / (q - 1)$. Then $q = 3$ by Lemma 35.1. By Lemma 35.2 $v | (3^p - 1) / 2$ and $v > 9/20 \cdot (3^{p-1} / p)$. Thus if $(v - 1) / p \leq (u - 1) / q$ then by Lemma 34.2

$$
\frac {\frac {9}{2 0} \cdot \frac {3 ^ {p - 1}}{p} - 1}{p} \leq \frac {p ^ {2} + p}{3}.
$$

Hence $p < 11$. Thus $p = 5$ or $p = 7$. If $p = 7$ then $v \mid (3^7 - 1)/2 = 1093$. As 1093 is a prime this implies that $v = (3^7 - 1)/2$ and the result follows from the first part of the lemma. If $p = 5$ then $v \mid (3^5 - 1)/2 = 121$. Thus $v = 11$ and $u \mid 31$. Thus $u = 31$. The proof is complete.

LEMMA 35.5. V is coherent.

Proof. Suppose that V is not coherent. Then by Lemma 11.2  $v^{*}d$  is a power of some prime r. As B/D is cyclic  $r \equiv 1 \pmod{p}$ . Thus

$$
r > 2 p > 2 q.\tag{35.2}
$$

Let $|\mathfrak{V}^*: D(\mathfrak{V}^*)| = r^n$, then $n \geq 3$ by Lemma 11.3. By Lemma 11.1

$$
r ^ {*} \leq 4 | N (\mathfrak {B} ^ {*}): \mathfrak {B} ^ {*} | ^ {2} + 1.\tag{35.3}
$$

Suppose that $|N(\mathfrak{B}^*):\mathfrak{B}^*| = 7p$. Then $p \neq 7$ and (35.2) and (35.3) imply that $r^n \leq 200p^2 \leq 50r^2$. If $n \geq 4$ this yields that $r \leq 7$. Then $p = 3$ by (35.2) which is not the case as $p > q$. Hence $n = 3$. Thus Lemma 11.4 implies that $r^3 \leq 2r(7p) + 1$. Hence by (35.2) $r^2 \leq 14p < 7r$ and so $r < 7$ which is impossible.

By Lemmas 35.1 and 35.2 we may assume now that $|N(\mathfrak{B}^*):\mathfrak{B}^*|\leq pq$. Thus (35.2) and (35.3) imply that

$$
r ^ {n} \leq 4 p ^ {2} q ^ {2} + 1 <   (2 p) ^ {4} <   r ^ {4},
$$

thus $n = 3$. Hence Lemma 11.4 implies that

$$
r ^ {3} \leq 2 r p q + 1 <   \frac {r ^ {3}}{2}.
$$

This completes the proof in all cases.

LEMMA 35.6. $d = 1$. If $|N(\mathfrak{B}^*):\mathfrak{B}^*|\leqq pq$ then $v^{*} = v$ or $p = 5$, $q = 3$, $v = 11$, $v^{*} = 121$.

Proof. If $|N(\mathfrak{B}^*): \mathfrak{B}^*| > pq$ then $c \neq 1$. Hence $d = 1$ by Lemma 34.2. Assume now that $|N(\mathfrak{B}^*): \mathfrak{B}^*| \leq pq$.

Assume first that $d \neq 1$. By Lemmas 35.1 and 35.2 $d = 11$, $q = 3$, $p = 5$ and $v = 121$. By Lemma 34.2 $u = (5^3 - 1) / (5 - 1) = 31$. Thus

$$
\frac {d v ^ {*} - 1}{| N (\mathfrak {B} ^ {*}) : \mathfrak {B} ^ {*} |} \geq \frac {1 1 ^ {3} - 1}{1 5} > \frac {1 1 ^ {2} - 1}{5} = \frac {v - 1}{p}
$$

and

$$
\frac {d v ^ {*} - 1}{| N (\mathfrak {B} ^ {*}) : \mathfrak {B} ^ {*} |} \geq \frac {1 1 ^ {3} - 1}{1 5} > \frac {3 1 - 1}{3} = \frac {u - 1}{q}.
$$

Hence by Lemmas 35.5 and 34.11 $1 / p \leq pq / v^{*}d$.

Thus

$$
1 1 ^ {3} \leq v ^ {*} d \leq p ^ {2} q = 7 5.
$$

Therefore d = 1.

Assume now that $q = 3, p = 5, v = 11, u = 31$. Let $v^{*} = vx$. $x \equiv 1 \pmod{10}$ as $v \equiv v^{*} \equiv 1 \pmod{10}$. If $v^{*} \neq 11$ and $v^{*} \neq 121$, then $x \geq 21$. Thus $v^{*} \geq 21.11$.

$$
\frac {v ^ {*} - 1}{| N (\mathfrak {B} ^ {*}) : \mathfrak {B} ^ {*} |} \geq \frac {2 1 . 1 1 - 1}{1 5} > \frac {1 1 - 1}{5} = \frac {v - 1}{p}
$$

and

$$
\frac {v ^ {*} - 1}{| N (\mathfrak {B} ^ {*}) : \mathfrak {B} ^ {*} |} \geq \frac {2 1 . 1 1 - 1}{1 5} > \frac {3 1 - 1}{3} = \frac {u - 1}{q}.
$$

Thus Lemmas 35.5 and 34.11 imply that $1/p \leqq pq / v^*$. Thus $21.11 \leqq v^* \leqq p^2 q = 75$ which is not the case. Therefore $v = v^* = 11$ or $v^* = 121$, and we are done in this case.

By Lemma 35.4 it may now be assumed that $(v - 1) / p > (u - 1) / q$. If $v^{*} = vx$, then $x \equiv 1 (\bmod 2p)$ since $v^{*} \equiv v \equiv 1 (\bmod 2p)$. Thus

$$
v ^ {*} = x v, x > 2 p > 2 q \quad \text { if } x \neq 1.\tag{35.4}
$$

Therefore

$$
\frac {v ^ {*} - 1}{| N (\mathfrak {B} ^ {*}) : \mathfrak {B} ^ {*} |} \geq \frac {v ^ {*} - 1}{p q} > \frac {2 v q - 1}{p q} > \frac {v - 1}{p} > \frac {u - 1}{q}.
$$

Hence by Lemmas 35.5 and 34.11 $1/p < pq/v^{*}$. Hence (35.4) and Lemmas 35.1 and 35.2 imply that

$$
q ^ {p - 1} <   \frac {2 0}{9} p v \leq \frac {1 0}{9} v ^ {*} \leq \frac {1 0}{9} p ^ {2} q.
$$

Thus $q^{p-2} < 2p^2$. Hence $p < 7$ by (5.4). Thus $p = 5$. Hence $x \geq 11$, $q = 3$ and $v \mid 121$. By assumption $v \neq 11$, hence $v = 121$. Thus $11^3 \leq v^* \leq p^2 q = 75$. This completes the proof in all cases.

LEMMA 35.7.

$$
\mid N (\mathfrak {U} ^ {*}) \colon \mathfrak {U} ^ {*} C (\mathfrak {U} ^ {*}) \mid = q o r p q.
$$

Proof. This follows directly from Lemmas 35.1, 35.2, 35.3 and 35.6..

THEOREM 35.1. If $N(\mathfrak{U}^*)$ is conjugate to $N(\mathfrak{B}^*)$ then the conclusions of Theorem 27.1 hold.

Proof. By Lemma 35.6 if $\mathfrak{B}^* \neq \mathfrak{B}$ then $p = 5, q = 3$ and $v^* = 121$. Thus $u = 31$. Hence $u$ does not divide $v^*$. Thus by Lemmas 35.1 and 35.2, $\mathfrak{B}^* = \mathfrak{B}$ is cyclic. By Theorem 33.1 $N(\mathfrak{B}^*)$ is a Frobenius group with Frobenius kernel $\mathfrak{B}^*$. Hence by Lemma 34.12 $\mathfrak{B}^*$ is a T.I. set in $\mathfrak{G}$. Since $\mathfrak{D}^* \subseteq N(\mathfrak{U}^*)$ and $p||N(\mathfrak{V}^*): \mathfrak{B}^*|$ Lemma 35.7 implies that $N(\mathfrak{U}^*) / \mathfrak{U}^*$ is a cyclic group of order $pq$. Thus condition (iv) of Theorem 27.1 holds. Since $\mathfrak{B}^*$ is cyclic so is $\mathfrak{U}$. Thus $\mathfrak{C}$ char $\mathfrak{U}$. Hence if $\mathfrak{C} \neq 1$ then $N(\mathfrak{U}) \subseteq \mathfrak{S}$ which is not the case. Hence

c = 1. By Lemma 35.6 d = 1. Thus  $C(\mathfrak{Q}^{*}) = \mathfrak{Q}\mathfrak{P}^{*}$  and  $C(\mathfrak{P}^{*}) = \mathfrak{P}\mathfrak{Q}^{*}$ . Hence condition (iii) of Theorem 27.1 holds. If  $|\mathfrak{P}| \neq p^{q}$  or  $|\mathfrak{Q}| \neq q^{p}$ , then  $N(\mathfrak{U}) \subseteq \mathfrak{S}$  or  $N(\mathfrak{V}) \subseteq \mathfrak{T}$  respectively. This implies that P is elementary abelian of order  $p^{q}$  and Q is elementary abelian of order  $q^{p}$ . Hence condition (i) of Theorem 27.1 holds.

Since $\mathfrak{U}$ is cyclic and $\mathfrak{C} = 1$, $\mathfrak{P}\mathfrak{U}$ and $\mathfrak{U}\mathfrak{Q}^*$ are Frobenius groups and $N(\mathfrak{P})' = \mathfrak{S}' = \mathfrak{P}\mathfrak{U}$. Since $\mathfrak{U}^*$ is cyclic every divisor $x$ of $|\mathfrak{U}^*|$ satisfies $x \equiv 1 \pmod{pq}$. Thus $(|\mathfrak{U}|, p - 1) = 1$. Hence by Lemma 34.1 $|\mathfrak{U}||(p^q - 1)/(p - 1)$. Let $(p^q - 1)(p - 1) = y|\mathfrak{U}|$. Suppose that $p \not\equiv 1 \pmod{q}$. Then $y \equiv 1 \pmod{pq}$ since

$$
\frac {p ^ {q} - 1}{p - 1} \equiv | \mathfrak {U} | \equiv 1 (\mathrm{mod} p q).
$$

Thus if $y \neq 1$, then $y > 2pq$. Furthermore Lemma 35.1 implies that in this case $q = 3$. Thus by Lemma 35.3 (i)

$$
1 3 > \frac {p ^ {2} + p + 1}{| \mathfrak {U} |} = y > 2 p q = 6 p
$$

which is impossible as $p > 3$. Thus $y = 1$ and so $|\mathfrak{U}| = (p^q - 1)/(p - 1)$. Suppose that $p \equiv 1 (\bmod q)$. Then $q |(p^q - 1)/(p - 1)$. Hence $u |1/q [(p^q - 1)/(p - 1)]$ since $(u, q) = 1$. As $q < p$ and $u \equiv (p^q - 1)/(p - 1) \equiv 1 (\bmod p)$ we see that $u \neq 1/q [(p^q - 1)/(p - 1)]$. Thus if $y \neq 1$, Lemma 35.1 yields that $q = 3$. Since $c = 1$, Lemma 35.3 (i) implies that $u > (p^2 + p + 1)/13$. This is impossible since $u \equiv 1 (\bmod 3p)$. This verifies condition (ii) of Theorem 27.1 and completes the proof of the theorem.

## 36. The Proof of Theorem 27.1

In this section the study of the groups $\mathfrak{S}$ and $\mathfrak{T}$ is continued. All the lemmas in this section will be proved under the following assumption.

Hypothesis 36.1

(i) $q <   p.$

(ii)  $N(\mathfrak{U}^{*})$  is not conjugate to  $N(\mathfrak{V}^{*})$ .

The following notation is used in addition to that introduced in Section 34.

$$
\phi \in \mathcal {U}, \psi \in \mathcal {V}
$$

and

$$
\phi (1) = | N (\mathfrak {U} ^ {*}) \colon \mathfrak {U} ^ {*} C (\mathfrak {U} ^ {*}) |, \quad \psi (1) = | N (\mathfrak {V} ^ {*}) \colon \mathfrak {V} ^ {*} |.
$$

If $\phi_i \in \mathcal{U}$ then $\phi_i^{\tau}$ is defined since $|\mathfrak{G}|$ is odd. Let $\mathcal{U}^{\tau} = \{\phi_i^{\tau} | \phi_i \in \mathcal{U}\}$. Then

$$
(\tilde {1} _ {\mathfrak {u} ^ {*}} - \phi) ^ {\tau} = 1 _ {\mathfrak {G}} - \phi^ {\tau} + \Gamma_ {\mathfrak {u}} + \Xi_ {\mathfrak {u}}, \quad \text { if } \mathscr {U} = \mathscr {U} _ {0}\tag{36.1}
$$

$$
(\tilde {1} _ {\mathfrak {G} ^ {\prime}} - \phi) ^ {\tau} = 1 _ {\mathfrak {G}} - \phi^ {\tau} + \Gamma_ {\mathfrak {u}} + \Xi_ {\mathfrak {u}} \quad \text {if} \mathscr {U} \neq \mathscr {U} _ {0}\tag{36.2}
$$

$$
(\tilde {1} _ {\mathfrak {B} ^ {*}} - \psi) ^ {\tau} = 1 _ {\mathfrak {G}} - \psi^ {\tau} + \Gamma_ {\mathfrak {B}} + \Xi_ {\mathfrak {B}}\tag{36.3}
$$

$$
(\tilde {1} _ {\mathfrak {P} \mathfrak {G} \mathfrak {D} ^ {*}} - \mu_ {0 j}) ^ {*} = 1 _ {\mathfrak {G}} \pm \eta_ {0 j} + \Gamma_ {\mathfrak {P}} + \Xi_ {\mathfrak {P}} \quad \text { for } 1 \leq j \leq p - 1,\tag{36.4}
$$

$$
(\tilde {1} _ {\mathbb {Q} \mathfrak {B} ^ {*}} - \nu_ {i 0}) ^ {*} = 1 _ {\mathfrak {G}} \pm \eta_ {i 0} + \Gamma_ {\mathfrak {D}} + E _ {\mathfrak {D}} \quad \text { for } 1 \leq i \leq q - 1 ,
$$

where $\mathcal{E}_{\mathfrak{U}}, \mathcal{E}_{\mathfrak{B}}$ are in $\mathcal{I}(\mathcal{U}^{\tau}), \mathcal{I}(\mathcal{V}^{\tau})$ respectively, $\Gamma_{\mathfrak{U}}, \Gamma_{\mathfrak{B}}$ are orthogonal to $\mathcal{U}^{\tau}, \mathcal{V}^{\tau}$ respectively. $\mathcal{E}_{\mathfrak{P}}, \mathcal{E}_{\mathfrak{D}}$ are linear combinations of the generalized characters $\eta_{st}$ and $\Gamma_{\mathfrak{P}}, \Gamma_{\mathfrak{D}}$ are orthogonal to each $\eta_{st}$. Then $\Gamma_{\mathfrak{U}}, \Gamma_{\mathfrak{B}}, \Gamma_{\mathfrak{P}}$ and $\Gamma_{\mathfrak{D}}$ are real valued generalized characters each of which is orthogonal to $1_{\mathfrak{G}}$. Thus

(36.5)

$$
\left(\Gamma_ {\mathfrak {U}}, \eta_ {0 1}\right) + \left(\Gamma_ {\mathfrak {P}}, \phi^ {\tau}\right) \not \equiv 0 (\mathrm{mod} 2),\tag{36.6}
$$

$$
(\Gamma_ {\mathfrak {B}}, \eta_ {0 1}) + (\Gamma_ {\mathfrak {P}}, \psi^ {\tau}) \not \equiv 0 (\mathrm{mod} 2).\tag{36.7}
$$

$$
\left(\Gamma_ {\mathfrak {U}}, \eta_ {1 0}\right) + \left(\Gamma_ {\mathfrak {Q}}, \phi^ {\tau}\right) \not \equiv 0 (\mathrm{mod} 2).
$$

It is a simple consequence of Lemma 13.1 that

(36.8)

$$
\left(\Gamma_ {\mathfrak {U}}, \eta_ {0 1}\right) + \left(\Gamma_ {\mathfrak {U}}, \eta_ {1 0}\right) + \left(\Gamma_ {\mathfrak {U}}, \eta_ {1 1}\right) \not \equiv 0 (\mathrm{mod} 2).\tag{36.9}
$$

$$
\left(\Gamma_ {\mathfrak {B}}, \eta_ {0 1}\right) + \left(\Gamma_ {\mathfrak {B}}, \eta_ {1 0}\right) + \left(\Gamma_ {\mathfrak {B}}, \eta_ {1 1}\right) \not \equiv 0 (\mathrm{mod} 2).
$$

By Hypothesis 36.1 (ii) $\mathcal{U}^{\tau}$ is orthogonal to $\mathcal{V}^{\tau}$. Thus

$$
(\Gamma_ {\mathfrak {U}}, \psi^ {\tau}) + (\Gamma_ {\mathfrak {B}}, \phi^ {\tau}) \not \equiv 0 \pmod {2}.\tag{36.10}
$$

Since $\tau$ is an isometry (36.1), (36.2), (36.3) and (36.4) yield that

(36.11)

$$
\left| \left| \Gamma_ {\mathfrak {U}} \right| \right| ^ {2} \leq \left| N (\mathfrak {U} ^ {*}): \mathfrak {U} ^ {*} C (\mathfrak {U} ^ {*}) \right| - 1\tag{36.12}
$$

$$
\left| \left| \Gamma_ {\mathfrak {B}} \right| \right| ^ {2} \leq | N (\mathfrak {B} ^ {*}): \mathfrak {B} ^ {*} | - 1\tag{36.13}
$$

$$
\left| \left| \Gamma_ {\mathfrak {P}} \right| \right| ^ {2} \leq \frac {u - 1}{q}\tag{36.14}
$$

$$
\| \Gamma_ {\mathbb {D}} \| ^ {2} \leq \frac {v - 1}{p}.
$$

LEMMA 36.1. $\mathcal{U}$ is coherent.

Proof. If $\mathfrak{S}$ is of type IV then by Lemmas 35.2 and 35.3 $c = 1$ or 7 so by Lemma 11.1 the result follows from Theorem 29.1. If $\mathfrak{S}$ is of type III then $\mathfrak{U} = \mathfrak{U}^*$ is abelian and the result follows from Lemma 11.2. Suppose that $\mathfrak{U}$ is not coherent. Then $\mathfrak{U} = \mathfrak{U}_0$ and by Lemma 11.2 $\mathfrak{U}^*$ is an $r$-group for some prime $r$. Furthermore $\mathfrak{S}$ is of type II. Let $e = |N(\mathfrak{U}^*): \mathfrak{U}^*|$ then by Lemmas 11.1, 11.3 and

11.4 $\mathfrak{U}^{*\prime} = D(\mathfrak{U}^*)\neq 1,$

$$
| \mathfrak {U} ^ {*}: \mathfrak {U} ^ {* \prime} | = r ^ {n} \quad \text { with } n \geq 3, \tag {36.15}
$$

(36.16) $r^n \leq 4e^2 + 1, n \geq 4$ or $r^3 \leq 2re + 1$ and $n = 3$.

Suppose first that $\mathfrak{U}$ is not cyclic. Then by Lemma 35.1 $q = 3$. If $c \neq 1$, then by Lemma 35.3 $\mathfrak{C}$ is cyclic and

$$
u > \frac {p ^ {2} + p + 1}{2} > \left(\frac {p - 1}{2}\right) ^ {2}.
$$

Thus by Lemma 34.1 $\mathfrak{U}/\mathfrak{C}$ is cyclic. Hence $\mathfrak{U}$ is generated by two elements. If $c=1$ then Lemma 34.1 implies that $\mathfrak{U}$ is generated by two elements. Thus $\mathfrak{U} \neq \mathfrak{U}^{*}$. As $\mathfrak{S}$ is of type II $\hat{\mathfrak{S}}$ is a T.I. set in $\mathfrak{G}$. Consequently there exists an element $R$ of order $r$ such that $\mathfrak{U}=C_{\mathfrak{U}^{*}}(R)$. Thus $Z(\mathfrak{U}^{*})$ is cyclic. Hence $r \equiv 1 \pmod{e}$. This contradicts (36.15) and (36.16).

Suppose now that $\mathfrak{U}$ is cyclic. Thus $r \equiv 1 (\bmod q)$. By (36.16) $N(\mathfrak{U}^*) / \mathfrak{U}^*$ is irreducibly represented on $\mathfrak{U}^* / D(\mathfrak{U}^*)$. Thus $\mathfrak{D}^*$ acts as a group of scalar matrices on $\mathfrak{U}^* / D(\mathfrak{U}^*)$. Hence by Lemma 6.4 $\mathfrak{U}^*$ has prime exponent. Since $\mathfrak{U}$ is a cyclic subgroup of $\mathfrak{U}^*$ this implies that

$$
| \mathfrak {U} | = r.\tag{36.17}
$$

If $q > 3$ then Lemmas 35.1, 35.7 and (36.15) and (36.16) imply that

$$
\left(\frac {p}{q} ^ {q - 1}\right) ^ {3} \leq | \mathfrak {U} | ^ {3} <   4 e ^ {2} + 1 \leq 4 p ^ {2} q ^ {2} + 1.
$$

Hence $p^{3q - 5}\leq 5q^5$ and so

$$
5 ^ {3 q - 1 0} \leq q ^ {8 q - 1 0} <   p ^ {8 q - 1 0} <   5.
$$

Thus $3q - 10 < 1$ which is not the case.

Suppose that $q = 3$: If $n \geq 4$ then (36.16) and Lemmas 35.3 and 35.7 imply that

$$
\frac {(p ^ {2} + p + 1) ^ {4}}{1 3 ^ {4}} <   | \mathfrak {U} | ^ {4} \leq 3 6 p ^ {2} + 1.
$$

Hence

$$
p ^ {8} <   (p ^ {2} + p + 1) ^ {4} <   1 3 ^ {4} (3 6 p ^ {2} + 1) <   3. 1 3 ^ {5} p ^ {2}.
$$

Thus $p^6 < 3.13^5$. Hence $p < 13$. If $n = 3$ then (36.16) and Lemmas 35.3 and 35.7 imply that

$$
\frac {(p ^ {2} + p + 1) ^ {2}}{1 3 ^ {2}} <   | \mathfrak {U} | ^ {2} \leq 6 p.
$$

Hence

$$
p ^ {4} <   (p ^ {2} + p + 1) ^ {2} <   1 3 ^ {2} \cdot 6 p <   1 3 ^ {3} p.
$$

Therefore $p < 13$ in this case also. Thus $p = 5, 7$ or 11. By Lemma 34.1 and (36.17) either $|\mathfrak{U}||(p - 1)$ or $|\mathfrak{U}||p^2 + p + 1$. If $|\mathfrak{U}||(p - 1)$ then $p = 11$ and $|\mathfrak{U}| = 5$ since $(|\mathfrak{U}|, 6) = 1$. However in this case

$$
\frac {(p ^ {2} + p + 1)}{1 3} > 1 0 > | \mathfrak {u} |
$$

which is impossible by Lemma 35.1. Thus $|\mathfrak{U}||p^2 + p + 1$. Hence by (36.17) if $p = 5, |\mathfrak{U}| = 31$, if $p = 7, |\mathfrak{U}| = 19$ and if $p = 11$ then $|\mathfrak{U}| = 7$ or $|\mathfrak{U}| = 19$. If $p = 5$ then (36.16) and (36.17) imply that

$$
3 1 ^ {3} \leq 3 6. 2 5 + 1
$$

which is not the case. If $p = 7$ then (36.16) and (36.17) imply that

$$
1 9 ^ {3} <   3 6. 4 9 + 1 <   1 8 0 0.
$$

Thus $19^2 < 100$ which is not the case. If $p = 11$ and $|\mathfrak{U}| = 19$ then (36.16) and (36.17) imply that

$$
1 5. 3 6 0 <   1 9 ^ {3} <   3 6. 1 2 1 + 1 <   4 8 0 0
$$

which is not the case.

Assume now that $p = 11$ and $|\mathfrak{U}| = r = 7$. Then (36.15) and (36.16) imply that

$$
7 ^ {n} \leq 3 6. 1 1 ^ {2} + 1, \quad 7 ^ {n} \equiv 1 (\mathrm{mod} 1 1).\tag{36.18}
$$

Since

$$
7 ^ {5} > 1 0 ^ {4} > 5 0 0 0 > 3 6. 1 1 ^ {2} + 1
$$

we must have $n \leq 4$. However

$$
7 ^ {2} \equiv 5, 7 ^ {3} \equiv 2, 7 ^ {4} \equiv 3 {\pmod {1 1}}
$$

contrary to (36.18). The proof is complete.

LEMMA 36.2. q = 3.

Proof. Suppose that $q \neq 3$. Then by (36.10) either $(\Gamma_{\mathfrak{u}}, \psi^{\tau}) \neq 0$ or $(\Gamma_{\mathfrak{B}}, \phi^{\tau}) \neq 0$. If $u = 1 / q[(p^{q} - 1) / (p - 1)]$, then $u \not\equiv 1 \pmod{p}$. Hence by Lemmas 35.1, 35.5 and 36.1,

$$
\frac {\frac {q ^ {p} - 1}{q - 1} - 1}{p q} \leq p q - 1 \quad \text { or } \quad \frac {\frac {p ^ {q} - 1}{p - 1} - q}{p q} \leq p q - 1.
$$

Therefore by (5.11) $p^{q - 1} < (p^q - 1) / (p - 1) < p^2 q^2$. Hence $p^{q - 3} < q^2 < p^2$

which is impossible for  $q \geq 5$ .

LEMMA 36.3. $c = 1, |N(\mathfrak{B}^*): \mathfrak{B}^*| = p$ or $3p$.

Proof. If $c \neq 1$ then $c = 7$ and $u > (p^2 + p + 1)/2$ by Lemma 35.3. Since $[(p - 1)/2]^2 < (p^2 + p + 1)/2$ Lemma 34.1 implies that $u | p^2 + p + 1$. Thus $u = p^2 + p + 1$. By Lemma 34.2 $v = (3^p - 1)/2$.

Suppose first that $|N(\mathfrak{U}^*):\mathfrak{U}^*| = 3$. Then by (36.8) $\Gamma_{\mathfrak{U}} = \pm (\eta_{10} + \eta_{20})$. Thus $(\Gamma_{\mathfrak{U}},\eta_{01}) = 0$. Hence $(\Gamma_{\mathfrak{P}},\phi^{\tau})\neq 0$ by (36.5). Since $\mathcal{U}$ is coherent (36.13) implies that

$$
\frac {7 u ^ {*} - 1}{3} \leq \| \Gamma_ {\mathfrak {P}} \| ^ {2} \leq \frac {u - 1}{3} \leq \frac {u ^ {*} - 1}{3},
$$

which is not the case.

Suppose now that $|N(\mathfrak{U}^*): \mathfrak{U}^*| \neq 3$. Then by Lemma 35.7 $|N(\mathfrak{U}^*): \mathfrak{U}^*| = 3p$. Let $cu^* = xu = x(1 + p + p^2)$. Then $x \equiv 1 \pmod{6p}$ since

$$
c u ^ {*} \equiv u \equiv 1 (\mathrm{mod} 6 p).
$$

As $1 < c \leq x$ this implies that $x \geq 6p + 1$. Hence by Lemma 35.2 and (36.12)

$$
\frac {c u ^ {*} - 1}{3 p} > \frac {6 p u}{3 p} \geq 2 u > 7 p - 1 \geq | | \Gamma_ {\mathfrak {B}} | | ^ {2}.\tag{36.19}
$$

Since $\mathcal{U}$ is coherent this implies that $(\Gamma_{\mathfrak{g}},\phi^{\tau}) = 0$. Thus by (36.10)

$$
\left(\Gamma_ {\mathfrak {u}}, \psi^ {\tau}\right) \neq 0.\tag{36.20}
$$

Since $\mathcal{U}$ is coherent (36.13) and (36.19) imply that $(\Gamma_{\mathfrak{P}},\phi^{\mathrm{r}}) = 0$. Thus by (36.5)

$$
(\Gamma_ {\mathfrak {U}}, \eta_ {\mathfrak {o} 1}) \not \equiv 0 (\mathrm{mod} 2).\tag{36.21}
$$

Since V is coherent (36.11), (36.20) and (36.21) imply that

$$
(p - 1) + \frac {v ^ {*} - 1}{| N (\mathfrak {B} ^ {*}) : \mathfrak {B} ^ {*} |} \leq 3 p - 1.
$$

Hence by Lemma 35.2

$$
\frac {3 ^ {p} - 1}{2} - 1 = v - 1 \leq v ^ {*} - 1 \leq 2 p | N (\mathfrak {V} ^ {*}) \colon \mathfrak {V} ^ {*} | \leq 1 4 p ^ {2}.
$$

Therefore $3^p - 3 \leq 28p^2$. Hence $p = 5$ by (5.5). Thus $u = 31$ and $v = 121$. If the $S_7$-subgroup of $\mathfrak{U}^*$ has order $7^n$, then $7^n \equiv 1 \pmod{5}$. Thus $n \geq 4$. Therefore

$$
\frac {u ^ {*} - 1}{3 p} \geq \frac {7 ^ {4} . 3 1 - 1}{1 5} > 2 4 = \frac {v - 1}{p}.
$$

Thus the coherence of $\mathcal{U}$ implies that $(\Gamma_{\Omega},\phi^{\tau}) = 0$. Hence (36.7) yields that $(\Gamma_{\mathfrak{U}},\eta_{10})\not\equiv 0$ (mod 2). Therefore (36.8), (36.11) and (36.21) imply that

$$
\Gamma_ {\mathfrak {U}} = \pm \sum_ {i = 1} ^ {q - 1} \eta_ {i 0} \pm \sum_ {j = 1} ^ {p - 1} \eta_ {0 j} \pm \sum_ {i = 1} ^ {q - 1} \sum_ {j = 1} ^ {p - 1} \eta_ {i j}
$$

contrary to (36.20). Thus $c = 1$ and consequently $|N(\mathfrak{B}^*): \mathfrak{B}^*| = p$ or $3p$.

LEMMA 36.4. $|\mathbf{N}(\mathfrak{U}^{*}):\mathfrak{U}^{*}\mathbf{C}(\mathfrak{U}^{*})| = 3p.$

Proof. If the result is false then $|N(\mathfrak{U}^*): \mathfrak{U}^* C(\mathfrak{U}^*)| = 3$ by Lemma 35.7. Thus (36.8) implies that $\Gamma_{\mathfrak{U}} = \pm (\eta_{10} + \eta_{20})$. Therefore by (36.5) and (36.10) $(\Gamma_{\mathfrak{B}}, \phi^\tau) \neq 0$ and $(\Gamma_{\mathfrak{B}}, \phi^\tau) \neq 0$. Since $u^* \geq u$ (36.13) implies that $u^* = u$ and

$$
\Gamma_ {\mathfrak {P}} = \pm \sum_ {i} \phi_ {i} ^ {\tau},\tag{36.22}
$$

where $\phi_{i}$ ranges over $\mathcal{U}$. Thus by (36.6) ($\Gamma_{\mathfrak{B}}$, $\eta_{01}$) is odd. Hence by Lemma 36.3 and (36.12)

$$
\Gamma_ {\mathfrak {B}} = b \sum \phi_ {i} ^ {\tau} \pm \sum_ {j = 1} ^ {p - 1} \eta_ {0 j} + \Delta_ {\mathfrak {B}},
$$

where $b$ is odd and $\Delta_{\mathfrak{B}}$ is orthogonal to all $\phi_i^{\tau}, \eta_{0j}$. Therefore by (36.22)

$$
0 = \left(\left(\tilde {1} _ {\mathfrak {B C} ^ {*}} - \mu_ {0 1}\right) ^ {*}, \left(\tilde {1} _ {\mathfrak {B} ^ {*}} - \psi\right) ^ {r}\right) = 1 \pm 1 \pm b \frac {(u - 1)}{3}.
$$

Since $b \neq 0$ this implies that $|b|(u - 1)/3 = 2$. Hence $u = 7$. Thus by Lemma 35.3 (i) $7 \geq (p^2 + p + 1)/13$, hence $p < 10$. Hence $p = 5$ or $p = 7$. In either of these cases $u|(p^2 + p + 1)$ by Lemma 34.1 since $(u, 6) = 1$. Thus $7|31$ or $7|57$ which is not the case.

LEMMA 36.5. $|\mathfrak{P}| = p^q$.

Proof. If $|\mathfrak{P}| \neq p^{\alpha}$ then $N(\mathfrak{U}) \subseteq \mathfrak{S}$ as $\mathfrak{P}$ is a T.I. set in $\mathfrak{G}$. This contradicts Lemma 36.4.

LEMMA 36.6. U is cyclic.

Proof. By Lemma 34.1 if $\mathfrak{U}$ is not cyclic then $\mathfrak{U} = \mathfrak{U}_1 \times \mathfrak{U}_2$, where each $\mathfrak{U}_i$ is cyclic and $|\mathfrak{U}_i||(p - 1)/2$. Let $|\mathfrak{U}_i| = (p - 1)/2y_i$ for $i = 1, 2$. If $y_1y_2 \geq 4$ then Lemma 35.3 (i) implies that

$$
\frac {p ^ {2}}{1 3} <   \frac {p ^ {2} + p + 1}{1 3} <   \frac {(p - 1) ^ {2}}{4 y _ {1} y _ {2}} \leq \frac {(p - 1) ^ {2}}{1 6} <   \frac {p ^ {2}}{1 6}
$$

which is not the case. Thus $y_1y_2 < 4$. If $y_1y_2 = 2$ then $p \equiv 1 \pmod{4}$ and so $|\mathfrak{U}| = (p - 1)^2 / 8$ is even. If $y_1y_2 = 3$ then $p \equiv 1 \pmod{3}$ and so $3|u$ which is not the case. Thus $y_1y_2 = 1$ and $u = [(p - 1)/2]^2$. Therefore $((p - 1)/2, 6) = 1$. Thus $p \geq 11$. Furthermore $u \equiv 1/4 \pmod{p}$. Since $u^* \equiv 1 \pmod{p}$ by Lemma 36.4 we have that $u^* = ux$ and $x \equiv 4 \pmod{p}$. By Lemma 34.2 $v = (3^p - 1)/2$. Hence Lemma 36.3 and (36.10), (36.11) and (36.12) imply that

$$
\frac {\frac {3 ^ {p} - 1}{2} - 1}{3 p} \leqslant 3 p - 1 \quad \text { or } \quad \frac {u ^ {*} - 1}{3 p} <   3 p - 1.\tag{36.23}
$$

The first possibility implies that $3^p - 3 \leq 18p^2 - 6p$. Thus $3^{p-2} \leq 2p^2$. Hence $p < 7$ by (5.4). The second possibility in (36.23) yields that

$$
\frac {(p - 1) ^ {2}}{4} x - 1 \leq 9 p ^ {2} - 3 p.
$$

Therefore

$$
(p - 1) ^ {2} x \leq 3 6 p ^ {2} - 1 2 p + 4 <   3 6 p ^ {2}.
$$

As $p \geq 11$ this implies that

$$
x <   3 6 \left(\frac {p}{p - 1}\right) ^ {2} = 3 6 \left(1 + \frac {1}{p - 1}\right) ^ {2} \leq 3 6 \left(\frac {1 2 1}{1 0 0}\right) <   4 5.\tag{36.24}
$$

Let $x = 4 + zp$ for some integer $z$. Then since $p \geq 11$ (36.24) yields that $z < 4$. Furthermore

$$
p <   4 1; \quad \text { if } \quad z \geq 2, \quad p <   2 0; \quad \text { if } \quad z = 3, \quad p <   1 4.\tag{36.25}
$$

As $p < 41$ and $((p - 1)/2, 6) = 1$, $p = 11$ or $p = 23$. If $p = 23$ then by (36.25) $x = 27$ which is impossible as $x \equiv 1 \pmod{3}$. If $p = 11$, then $x = 15$, 26 or 37. As $x \equiv 1 \pmod{6}$ this implies that $x = 37$. Then $u = 25$ and so $37 \equiv 1 \pmod{11}$ by Lemma 36.4 which is not the case.

$$
\begin{array}{l} \text { L   E   M   M   A } 3 6. 7. \quad u = p ^ {2} + p + 1 \quad o r \quad u = (p ^ {2} + p + 1) / 3 \quad o r \quad u = \\ (p ^ {2} + p + 1) / 7. \end{array}
$$

Proof. If $u|[(p - 1)/2]^2$ then by Lemmas 34.1 and 36.6 $u|(p - 1)/2$. Thus by Lemma 35.3 (i) $(p - 1)/2 > (p^2 + p + 1)/13$. Hence $2p^2 - 11p + 15 < 0$ which implies that $p < 5$. Therefore by Lemma 34.1 $p^2 + p + 1 = uy$, $y$ an integer. By Lemma 35.3 (i) $y < 13$. If $r$ is a prime such that $p^2 + p + 1 \equiv 0 \pmod{r}$ then either $r = 3$ or

$r \equiv 1 \pmod{3}$ . Hence y = 1, 3, 7 or 9. If y = 9 then  $p^{2} + p + 1 \equiv 0 \pmod{9}$ . Hence  $p \equiv 1 \pmod{3}$ . Thus  $p \equiv 1, 4$  or 7 (mod 9). In none of these cases is  $p^{2} + p + 1 \equiv 0 \pmod{9}$ . Hence y = 1, 3 or 7.

LEMMA 36.8. $u = u^{*} = p^{2} + p + 1.$

Proof. Let $u^{*} = ux$. Assume that $x \neq 1$. $u^{*} \equiv 1 \pmod{6p}$ by Lemma 36.4. If $u = p^{2} + p + 1$, then $u \equiv u^{*} \equiv 1 \pmod{6p}$, thus $x \equiv 1 \pmod{6p}$ and so $x \geq 1 + 6p$. If $u = (p^{2} + p + 1)/3$, then $x \equiv 3 \pmod{p}$. Furthermore $x \equiv 1 \pmod{6}$ since $u \equiv u^{*} \equiv 1 \pmod{6}$ and $p \equiv 1 \pmod{6}$ since $p^{2} + p + 1 \equiv 0 \pmod{3}$. Thus if $x = 3 + zp$ then $1 \equiv 3 + z \pmod{6}$. Hence $x \geq 3 + 4p$. If $u = (p^{2} + p + 1)/7$ then $x \equiv 7 \pmod{p}$. If $x = 7$ then by Lemma 36.6 the $S_{r}$-subgroup of $U^{*}$ is generated by two elements. Hence $7^{2} - 1 \equiv 0 \pmod{p}$ by Lemma 36.4. However $7^{2} - 1 = 48$ and $(p, 48) = 1$. Thus $x \neq 7$. Let $x = 7 + zp$. Then $p^{2} + p + 1 \equiv u \equiv 1 \pmod{6}$. Hence $p \equiv 5 \pmod{6}$. Thus $1 \equiv x \equiv 7 + 5z \pmod{6}$, hence $z \equiv 0 \pmod{6}$. Therefore $x \geq 7 + 6p$. Thus in any case

$$
u ^ {*} = u x, \quad x \geq 4 p + 3.\tag{36.26}
$$

Therefore $(u^{*} - 1) / 3p > (u - 1) / 3$. Hence by (36.13) and the coherence of $\mathcal{U}$

$$
\left(\phi^ {\tau}, \Gamma_ {\mathfrak {P}}\right) = 0.\tag{36.27}
$$

Assume first that $(\phi^{\tau},\Gamma_{\mathfrak{B}})\neq 0$ , then by (36.12) and the coherence of $\mathcal{U}$

$$
\frac {u ^ {*} - 1}{3 p} \leq 3 p - 1.\tag{36.28}
$$

Suppose now that $(\phi^{\mathrm{r}},\Gamma_{\mathfrak{B}}) = 0$ . Then by (36.10) $(\psi^{\mathrm{r}},\Gamma_{\mathfrak{U}})\neq 0.$ Hence the coherence of $\mathcal{V}$ and (36.11) imply that

$$
\frac {v ^ {*} - 1}{3 p} \leq 3 p - 1.\tag{36.29}
$$

By (36.27) and (36.5) $(\eta_{01}, \Gamma_{\mathfrak{U}}) \not\equiv 0 \pmod{2}$. If also $(\eta_{10}, \Gamma_{\mathfrak{U}})$ were odd then by (36.8) $(\eta_{ij}, \Gamma_{\mathfrak{U}}) \neq 0$ for $1 \leq i \leq q - 1$, $1 \leq j \leq p - 1$. Thus by (36.11) $(\psi^{\tau}, \Gamma_{\mathfrak{U}}) = 0$ contrary to what has been proved. Therefore $(\eta_{10}, \Gamma_{\mathfrak{U}}) \equiv 0 \pmod{2}$. Hence by (36.7) $(\Gamma_{\mathfrak{Q}}, \phi^{\tau}) \neq 0$. Thus by (36.14) and (36.29)

$$
\frac {u ^ {*} - 1}{3 p} \leq \frac {v - 1}{p} \leq \frac {v ^ {*} - 1}{p} <   9 p - 3.
$$

Now (36.28) implies that in any case

$$
\frac {u ^ {*} - 1}{9 p} \leq 3 p - 1.\tag{36.30}
$$

For any prime r let  $U_{r}$  be the  $S_{r}$ -subgroup of  $U^{*}$ .

Suppose first that $u = p^2 + p + 1$, then $x > 6p$. Hence (36.30) implies that

$$
6 (p ^ {2} + p + 1) - 1 \leq 2 7 p - 9.
$$

Therefore $2p^{2} - 7p + 4 \leq 0$ which is impossible for $p \geq 5$.

Suppose now that $u = (p^2 + p + 1)/3$ then $x \geq 4p + 3$ by (36.26). Hence (36.30) implies that

$$
4 (p ^ {2} + p + 1) <   8 1 p.
$$

Thus $4p < 81$ or $p < 22$. Since $p \equiv 1 \pmod{3}$ this yields that $p = 7$, $p = 13$ or $p = 19$.

If $p = 7$ then $u = 19$. If $|\mathfrak{U}_{19}| = 19^n$ then $n \geq 6$ as $|\mathfrak{U}_{19}| \equiv 1 \pmod{7}$. Thus (36.30) implies that $19^6 \leq 27.7^2 \leq 19^4$. If $p = 13$ then $u = 61$. Let $|\mathfrak{U}_{61}| = 61^n$, then $n \geq 3$ as $|\mathfrak{U}_{61}| \equiv 1 \pmod{13}$. Hence (36.30) implies that $61^3 \leq 27.13^2 < 61^3$. If $p = 19$ then $u = 127$. Let $|\mathfrak{U}_{127}| = 127^n$, then $n \geq 3$ as $|\mathfrak{U}_{127}| \equiv 1 \pmod{19}$. Hence (36.30) implies that $127^3 \leq 27.19^2 < 127^3$.

Assume finally that $u = (p^2 + p + 1)/7$ then $x \geq 6p + 1$. Thus (36.30) implies that

$$
\frac {6 (p ^ {2} + p + 1)}{7} \leq 2 7 p.
$$

Therefore $6p < 27.7$, so $p < 32$. Since $p^2 + p + 1 \equiv 0 \pmod{7}$, $p \equiv 2 \pmod{7}$ or $p \equiv 4 \pmod{7}$. Thus $p = 11$ or $p = 23$.

If $p = 11$ then $u = 19$. Let $|\mathfrak{U}_{19}| = 19^n$; then $n \geq 3$ as $|\mathfrak{U}_{19}| \equiv 1 \pmod{11}$. Hence (36.30) implies that $19^3 \leq 27.11^2 = 287.11 < 19^3$. If $p = 23$ then $u = 79$. As $|\mathfrak{U}_{79}| \equiv 1 \pmod{23}$, $|\mathfrak{U}_{79}| \geq 79^3$. Hence (36.30) implies that $79^3 \leq 27.23^2 < 79^3$.

Therefore $u = u^{*}$ in all cases. Hence $u \equiv 1 \pmod{p}$ by Lemmas 36.4 and 36.5. Since $(p, 6) = 1$, $7 \not\equiv 1 \pmod{p}$ and $3 \not\equiv 1 \pmod{p}$. Hence by Lemma 36.7 $u = p^{2} + p + 1$.

The proof of Theorem 27.1 under Hypothesis 36.1 is now immediate.

Let $q = 3$ and $p$ have the same meaning as in the earlier part of this section. By Lemma 35.2 $|\mathfrak{Q}| = q^p$. By Lemma 36.5 $|\mathfrak{P}| = p^q$. The other properties of Condition (i) follow from the structure of $\mathfrak{S}$ and $\mathfrak{T}$ and Theorem 14.1. Thus Condition (i) is verified. By Lemma 35.6 $C(\mathfrak{Q}) \subseteq \mathfrak{Q}$. Hence $C(\mathfrak{Q}^*) = \mathfrak{P}^*\mathfrak{Q}$. By Lemma 36.3 $C(\mathfrak{P}) \subseteq \mathfrak{P}$, hence $C(\mathfrak{P}^*) = \mathfrak{P}\mathfrak{Q}^*$ by Lemma 36.5. The other properties of Condi-

tion (iii) follow from the structure of $\mathfrak{S}$ and $\mathfrak{T}$. Thus Condition (iii) is verified. Lemmas 36.6 and 36.8 imply that $\mathfrak{U} = C(\mathfrak{U})$ is cyclic. By Lemmas 34.12 and 36.4 $\mathfrak{U} = \mathfrak{U}^*$ is a T.I. set in $\mathfrak{G}$. Hence Lemma 36.4 completes the verification of Condition (iv).

Lemmas 34.1, 36.3, 36.5 and 36.8 imply that $\mathfrak{U}$ is a Frobenius group. Lemma 36.8 implies that $|\mathfrak{U}| = (p^q - 1) / (p - 1)$. Lemmas 36.4, 36.6 and 36.8 imply that if $u_0||\mathfrak{U}|$ then $u_0 \equiv 1 \pmod{pq}$. Thus $(|\mathfrak{U}|, p - 1) = 1$. The other statements in Condition (ii) follow from the structure of $\mathfrak{S}$ and $\mathfrak{T}$.

By Theorem 35.1 this completes the proof of Theorem 27.1 in all cases.

# PACIFIC JOURNAL OF MATHEMATICS

EDITORS

RALPH S. PHILLIPS
Stanford University
Stanford, California

J. DUGUNDJI
University of Southern California
Los Angeles 7, California

M. G. ARSOVE
University of Washington
Seattle 5, Washington

LOWELL J. PAIGE
University of California
Los Angeles 24, California

E. F. BECKENBACH
T. M. CHERRY

D. DERRY
M. OHTSUKA

EDITORS
H. L. ROYDEN
E. SPANIER

E. G. STRAUS
F. WOLF

SUPPORTING INSTITUTIONS

UNIVERSITY OF BRITISH COLUMBIA
CALIFORNIA INSTITUTE OF TECHNOLOGY
UNIVERSITY OF CALIFORNIA
MONTANA STATE UNIVERSITY
UNIVERSITY OF NEVADA
NEW MEXICO STATE UNIVERSITY
OREGON STATE UNIVERSITY
UNIVERSITY OF OREGON
OSAKA UNIVERSITY
UNIVERSITY OF SOUTHERN CALIFORNIA

STANFORD UNIVERSITY
UNIVERSITY OF TOKYO
UNIVERSITY OF UTAH
WASHINGTON STATE UNIVERSITY
UNIVERSITY OF WASHINGTON
\*    \*    \*

AMERICAN MATHEMATICAL SOCIETY CALIFORNIA RESEARCH CORPORATION SPACE TECHNOLOGY LABORATORIES NAVAL ORDNANCE TEST STATION

Mathematical papers intended for publication in the Pacific Journal of Mathematics should be typewritten (double spaced), and the author should keep a complete copy. Manuscripts may be sent to any one of the four editors. All other communications to the editors should be addressed to the managing editor, L. J. Paige at the University of California, Los Angeles 24, California.

50 reprints per author of each article are furnished free of charge; additional copies may be obtained at cost in multiples of 50.

The Pacific Journal of Mathematics is published quarterly, in March, June, September, and December. Effective with Volume 13 the price per volume (4 numbers) is \$18.00; single issues, \$5.00. Special price for current issues to individual faculty members of supporting institutions and to individual members of the American Mathematical Society: \$8.00 per volume; single issues \$2.50. Back numbers are available.

Subscriptions, orders for back numbers, and changes of address should be sent to Pacific Journal of Mathematics, 103 Highland Boulevard, Berkeley 8, California.

Printed at Kokusai Bunken Insatsusha (International Academic Printing Co., Ltd.), No. 6, 2 chome, Fujimi-cho, Chiyoda-ku, Tokyo, Japan.

PUBLISHED BY PACIFIC JOURNAL OF MATHEMATICS, A NON-PROFIT CORPORATION
The Supporting Institutions listed above contribute to the cost of publication of this Journal, but they are not owners or publishers and have no responsibility for its content or policies

## Pacific Journal of Mathematics Vol. 13, No. 3 May, 1963

Walter Feit and John Griggs Thompson, Chapter I, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....775
Walter Feit and John Griggs Thompson, Chapter II, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....789
Walter Feit and John Griggs Thompson, Chapter III, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....803
Walter Feit and John Griggs Thompson, Chapter IV, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....845
Walter Feit and John Griggs Thompson, Chapter V, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....943
Walter Feit and John Griggs Thompson, Chapter VI, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....1011
Walter Feit and John Griggs Thompson, Bibliography, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....1029

# Pacific Journal of Mathematics

CHAPTER VI, FROM SOLVABILITY OF GROUPS OF ODD ORDER, PACIFIC J. MATH., VOL. 13, NO. 3 (1963)

WALTER FEIT AND JOHN GRIGGS THOMPSON

May 1963

# CHAPTER VI

## 37. Statement of the Result Proved in Chapter VI

The purpose of this chapter is to prove the following result.

THEOREM 37.1. There are no groups $\mathfrak{G}$ which satisfy conditions (i)-(iv) of Theorem 27.1.

Once it is proved, Theorem 37.1 together with Theorem 27.1 will serve to complete the proof of the main theorem of this paper. In this chapter there is no reference to anything in Chapters II–V other than the statement of Theorem 27.1. The following notation is used throughout this chapter.

⑧ is a fixed group which satisfies conditions (i)-(iv) of Theorem 27.1.

$$
| \mathfrak {U} | = u = \frac {p ^ {q} - 1}{p - 1}
$$

$$
\mathfrak {U} ^ {*} = C (\mathfrak {U}) \quad \text { and } \quad | \mathfrak {U} ^ {*} | = u ^ {*}.
$$

$$
\mathfrak {U} ^ {*} = \langle U _ {1} \rangle , U = U _ {1} ^ {* * / *} \text {. Thus } \mathfrak {U} = \langle U \rangle
$$

$$
\mathfrak {Q} _ {0} = [ \mathfrak {Q}, \mathfrak {P} ^ {*} ] \quad \text { so   that } \quad \mathfrak {Q} = \mathfrak {Q} ^ {*} \times \mathfrak {Q} _ {0}  .
$$

P and Q are fixed elements of  $P^{**}$  and  $D^{**}$  respectively.

For any integer n > 0,  $X_{n}$  is the ring of integers mod n. If n is a prime power then  $F_{n}$  is the field of n elements.

U acts as a linear transformation on P. Let  $m(t)$  be the minimal polynomial of U on P. Then  $m(t)$  is an irreducible polynomial of degree q over  $F_{p}$ . Let  $\omega$  be a fixed root of  $m(t)$  in  $F_{pq}$ . Then  $\omega$  is a primitive uth root of unity in  $F_{pq}$  and  $\omega, \omega^{p}, \cdots, \omega^{p^{q-1}}$  are all the characteristic roots of U on P.

## 38. The Sets $\mathcal{A}$ and $\mathcal{B}$

LEMMA 38.1. There exists an element $Y \in \mathfrak{Q}_0^*$ such that $\mathfrak{P}^*$ normalizes $Y\mathfrak{U}^* Y^{-1}$

Proof. $\mathfrak{Q}^*$ normalizes $\mathfrak{U}^*$ and $\mathfrak{Q}^*$ is contained in a cyclic subgroup of $N(\mathfrak{U}^*)$ of order $pq$. Hence some element of order $p$ in $C(\mathfrak{Q}^*)$ normalizes $\mathfrak{U}^*$. Since $C(\mathfrak{Q}^*) = \mathfrak{Q}\mathfrak{P}^*$ every subgroup of order $p$ in $C(\mathfrak{Q}^*)$ is of the form $Y^{-1}\mathfrak{P}^*Y$ for some $Y \in \mathfrak{Q}_0$. Hence it is possible to choose $Y \in \mathfrak{Q}_0$ such that $Y^{-1}\mathfrak{P}^*Y$ normalizes $\mathfrak{U}^*$. Since $[\mathfrak{P}^*, \mathfrak{U}] \subseteq \mathfrak{P}$,

$\mathfrak{P}^*$ does not normalize $\mathfrak{U}^*$, hence $Y \in \mathfrak{Q}_0^\sharp$ and $\mathfrak{P}^*$ normalizes $Y\mathfrak{U}^* Y^{-1}$. From now on let

$$
Z _ {1} = Y U _ {1} Y ^ {- 1}, \quad Z = Y U Y ^ {- 1} = Z _ {1} ^ {u ^ {*} / u}\tag{38.1}
$$

where Y satisfies Lemma 38.1. Notice that $\mathfrak{Q}^*$ normalizes $\langle Z_1\rangle$, since $\mathfrak{Q}^*$ normalizes $\mathfrak{U}^*$ and $Y$ centralizes $\mathfrak{Q}^*$. Define $v, w \in \mathcal{X}_u^*$ by

$$
P ^ {- 1} Z _ {1} P = Z _ {1} ^ {v}, \quad Q ^ {- 1} Z _ {1} Q = Z _ {1} ^ {w}\tag{38.2}
$$

LEMMA 38.2. If $Z_0 \in \langle Z_1 \rangle$, $a \in \mathcal{X}_p$, $b \in \mathcal{X}_q$ then $\langle Z_0 \rangle = \langle Z_0^{v^a w^b - 1} \rangle$ unless $a = 0$ and $b = 0$.

Proof. $Z_0^{-1}P^{-a}Q^{-b}Z_0Q^b P^a = Z_0^{v^{a}w^b - 1}$. Hence $P^a Q^b$ acts trivially on $\langle Z_0\rangle /\langle Z_0^{v^{a}w^b - 1}\rangle$. However if $Z_0\neq 1$ then $\mathfrak{P}^*\mathfrak{D}^*\langle Z_0\rangle$ is a Frobenius group with Frobenius kernel $\langle Z_0\rangle$. Thus $\langle Z_0\rangle = \langle Z_0^{v^a w^b - 1}\rangle$ as required.

LEMMA 38.3. Every element of $\mathfrak{M}\mathfrak{U}$ has a unique representation in the form $P^{m_1(U)}U^a$, where $a \in \mathcal{X}_u$ and $m_1(t)$ is a polynomial of degree at most $q - 1$ over $\mathcal{X}_p$.

Proof. There are $up^q$ ordered pairs $(m_1(t), a)$ with $a \in \mathcal{X}_u$ and $m_1(t)$ of degree at most $q - 1$ over $\mathcal{X}_p$. Thus it is sufficient to show the uniqueness of $(m_1(t), a)$ in such a representation.

If $P^{m_1(U)}U^a = P^{m_1'(U)}U^{a'}$. Then reading mod $\mathfrak{P}$ yields that $a = a'$. Since $m(t)$ is irreducible we get that $m_1(t) \equiv m_1'(t) (\text{mod } m(t))$. Thus $m_1(t) = m_1'(t)$ as required.

LEMMA 38.4. Every element of $\mathfrak{P}\mathfrak{U}-\mathfrak{U}$ has a unique representation in the form $U^{s}P^{v}U^{s}$, where $x,z\in\mathcal{X}_{u}$ and $y\in\mathcal{X}_{p}, y\neq0$.

Proof. If $X \in \mathfrak{P}\mathfrak{U} - \mathfrak{U}$ and

$$
X = U ^ {x} P ^ {y} U ^ {z} = U ^ {x _ {1}} P ^ {y _ {1}} U ^ {z _ {1}}
$$

then reading mod P we get that  $x + z \quad x_{1} + z_{1}$ . Hence

$$
U ^ {x - x _ {1}} P ^ {y} U ^ {- x + x _ {1}} = P ^ {y _ {1}}
$$

Since $X \notin \mathfrak{U}$, $y \neq 0$. As $(u, p - 1) = 1$ we have that $x = x_1$, and so $y = y_1$, $z = z_1$. The representation is unique. There are $u^2(p - 1)$ ordered triples $(x, y, z)$ with $x, z \in \mathcal{X}_u$ and $y \in \mathcal{X}_p$, $y \neq 0$. Each triple gives rise to an element of $\mathfrak{U} - \mathfrak{U}$ and $|\mathfrak{U} - \mathfrak{U}| = u^2(p - 1)$. The result now follows.

LEMMA 38.5. Let $x, z, g \in \mathcal{Z}_p = \mathcal{F}_p$; $y, f, h \in \mathcal{Z}_u$. Then

$$
P ^ {x} U ^ {y} P ^ {z} U ^ {f} P ^ {g} U ^ {h} = 1
$$

if and only if

(i) $y + f + h = 0$

(ii) $x\omega^{y} + z + g\omega^{y + h} = 0.$

Proof. Let $R = P^{x}U^{y}P^{s}U^{f}P^{g}U^{h}$. Then

$$
R = P ^ {x + s U ^ {- y}} + g U ^ {- y - f} U ^ {y + h + f}.
$$

Thus by Lemma 38.3 $R = 1$ if and only if

$$
y + h + f = 0, \quad x + z t ^ {- y} + g t ^ {- y - f} \equiv 0 (\mathrm{mod} m (t)).
$$

The first equation allows us to rewrite the second as

$$
x t ^ {y} + z + g t ^ {y + h} \equiv 0 (\mathrm{mod} m (t)).
$$

Thus the lemma is proved.

DEFINITION 38.1. The set $\mathcal{A}$ is defined to consist of all ordered triples $(a_{1}, a_{2}, a_{3})$ such that

(i) $a_{i}\in \mathcal{Z}_{u}, a_{i}\neq 0$ for $i = 1,2,3.$

(ii) $a_{1} + a_{2} + a_{3} = 0.$

(iii) $PU^{a_1}P^{-2}U^{a_2}PU^{a_3} = 1.$

DEFINITION 38.2. $\mathcal{B}$ is the set of all elements $a_1 \in \mathcal{X}_u$ such that $(a_1, a_2, a_3) \in \mathcal{A}$ for suitable $a_2, a_3$.

LEMMA 38.6. $|\mathcal{A}| = |\mathcal{B}|$.

Proof. If $(a_{1}, a_{2}, a_{3}) \in \mathcal{A}$ then by Lemma 38.4 $a_{2}$ and $a_{3}$ are determined by $a_{1}$.

LEMMA 38.7. $(a_{1}, a_{2}, a_{3}) \in \mathscr{A}$ if and only if

(i) $a_{i}\in \mathcal{Z}_{u}, a_{i}\neq 0$ for $i = 1,2,3$

(ii) $a_{1} + a_{2} + a_{3} = 0$

(iii) $\omega^{a_1} + \omega^{a_1 + a_3} - 2 = 0.$

Proof. By Lemma 38.5,

$$
P U ^ {a _ {1}} P ^ {- 2} U ^ {a _ {2}} P U ^ {a _ {3}} = 1
$$

if and only if  $a_{1} + a_{2} + a_{3} = 0$  and  $\omega^{a_{1}} - 2 + \omega^{a_{1} + a_{3}} = 0$ . This implies the result.

LEMMA 38.8. If $(a_{1}, a_{2}, a_{3}) \in \mathcal{A}$, then $(-a_{2}, -a_{1}, -a_{3}) \in \mathcal{A}$.

Proof. If $(a_{1}, a_{2}, a_{3}) \in \mathcal{A}$ then by Lemma 38.7 $\omega^{-a_2} - 2 + \omega^{a_1} = 0$. As $a_1 = -a_2 - a_3$ this yields that

$$
\omega^ {- a _ {2}} - 2 + \omega^ {- a _ {2} - a _ {3}} = 0.
$$

As $-a_{2} - a_{1} - a_{3} = 0$ the result follows from Lemma 38.7.

LEMMA 38.9. For $0 \leq i \leq p - 1$ let $\mathfrak{C}_i$ be the conjugate class of $\mathfrak{U}$ which contains $P^i$ and let $\mathfrak{R}_i$ be the sum of the elements in $\mathfrak{C}_i$ in the group ring of $\mathfrak{U}$ over the integers. Let

$$
\mathfrak {R} _ {1} ^ {2} = \sum_ {i = 0} ^ {p - 1} c _ {i} \mathfrak {R} _ {i}.
$$

If $q > 3$, then $c_{2} \geq 2$.

Proof. Let $\mu_0, \mu_1, \cdots$ be all the irreducible characters of $\mathfrak{P}\mathfrak{U}/\mathfrak{P}$ and let $\chi_1, \chi_2, \cdots$ be all the other irreducible characters of $\mathfrak{P}\mathfrak{U}$. It is a well known consequence of the orthogonality relations ([4] p. 316) that

$$
c _ {2} = \frac {u p ^ {q}}{p ^ {2 q}} \left\{\sum_ {i} \frac {\mu_ {i} (P) ^ {2} \overline {{\mu_ {i} (P ^ {2})}}}{\mu_ {i} (1)} + \sum_ {j} \frac {\chi_ {j} (P) ^ {2} \overline {{\chi_ {j} (P ^ {2})}}}{\chi_ {j} (1)} \right\}.
$$

Since $\mathfrak{U}$ is cyclic, $\mu_i(P) = \mu_i(P^2) = \mu_i(1) = 1$ for all $i$. By 3.16 $\chi_j(1) = u$ for all $j$. Thus

(38.3)

$$
c _ {2} = \frac {u}{p ^ {q}} \left\{u + \frac {1}{u} \sum_ {j} \chi_ {j} (P) ^ {2} \overline {{\chi_ {j} (P ^ {2})}} \right\}.
$$

By the orthogonality relations

$$
\sum_ {j} \left| \chi_ {j} (P ^ {i}) \right| ^ {2} \leq \left| C (P ^ {i}) \right| \leq p ^ {q} \quad \text { for } \quad 1 \leq i \leq p - 1.
$$

Therefore

(38.4)

$$
\left| \sum_ {j} \chi_ {j} (P) ^ {2} \overline {{\chi_ {j} (P ^ {2})}} \right| \leq \left(\max _ {j} \left| \chi_ {j} (P ^ {2}) \right|\right) \sum_ {j} \left| \chi_ {j} (P) \right| ^ {2} \leq p ^ {3 q / 2}.
$$

By (38.3) and (38.4)

$$
\mid p ^ {q} c _ {2} - u ^ {2} \mid \leq p ^ {3 q / 2}.
$$

Thus

(38.5)

$$
p ^ {q} c _ {2} \geq u ^ {2} - p ^ {3 q / 2}.
$$

Since $u = \frac{p^q - 1}{p - 1} > p^{q-1}$ (38.5) yields that

$$
c _ {2} \geq \frac {u ^ {2}}{p ^ {q}} - p ^ {q / 2} > p ^ {q - 2} - p ^ {q / 2} = p ^ {q / 2} (p ^ {q / 2 - 2} - 1).
$$

As $q > 3$ and $q$ is a prime we have $q \geq 5$, and the lemma follows.

LEMMA 38.10. $|\mathcal{A}| = |\mathcal{B}| > 0$

Proof. Assume first that q = 3. Consider the set of polynomials of the form  $f_{a}(t) = t^{3} + at^{2} + (a + 6)t - 1$  with  $a \in X_{p}$ . There are p of these and none of them has 0 as a root. Thus if  $f_{a}(t)$  were reducible for every value of a there would exist  $a \neq b$  such that  $f_{a}(t)$  and  $f_{b}(t)$  have a common root  $c \in F_{p}$ . Then

$$
a c ^ {2} + (a + 6) c = b c ^ {2} + (b + 6) c.
$$

Since $c \neq 0$ this yields that $a(c + 1) = b(c + 1)$, hence $c = -1$. However $f_{a}(-1) = -8 \neq 0$. Thus there exists some polynomial $f_{a}(t)$ which is irreducible over $\mathcal{F}_{p}$. Let $\alpha$ be a root of $f_{a}(t)$ in $\mathcal{F}_{p^{3}}$. Then

$$
\alpha^ {p ^ {2} + p + 1} = - f _ {a} (0) = 1, \quad (1 + \alpha) ^ {p ^ {2} + p + 1} = - f _ {a} (- 1) = 8.
$$

Therefore $\alpha = \omega^{a_3}$ for some $a_3 \in \mathcal{X}_u$, $a_3 \neq 0$, and $1 + \alpha = 2\omega^{-a_1}$ for some $a_1 \in \mathcal{X}_u$, $a_1 \neq 0$. Furthermore $-\omega^{a_3} + 2\omega^{-a_1} = 1$. Thus $\omega^{a_1} + \omega^{a_1 + a_3} - 2 = 0$. Since $\omega^{a_1} \neq 1$, $a_1 + a_3 \neq 0$. Hence by Lemmas 38.6 and 38.7 $|\mathscr{A}| = |\mathscr{B}| > 0$.

Assume now that q > 3. Then Lemma 38.9 implies the existence of  $a, b \in X_{u}$ , with  $a \neq 0$  or  $b \neq 0$  such that

$$
U ^ {- a} P U ^ {a} U ^ {- b} P U ^ {b} = P ^ {2}.
$$

Therefore

$$
P U ^ {b} P ^ {- 2} U ^ {- a} P U ^ {a - b} = 1.\tag{38.6}
$$

Let $a_1 = b$, $a_2 = -a$, $a_3 = a - b$. Then $a_1 + a_2 + a_3 = 0$. If $b = 0$ then (38.6) becomes $P^{-1}U^{-a}PU^a = 1$; as $\mathfrak{P}\mathfrak{U}$ is a Frobenius group this implies $a = 0$ contrary to the choice of $a$ and $b$. If $a = 0$ then (38.6) implies that $PU^bP^{-1}U^{-b} = 0$, hence $b = 0$. If $a - b = 0$ then (38.6) yields that $PU^aP^{-2}U^{-a}P = 1$ or $U^a$ commutes with $P^2$. Thus $a = 0$, hence also $b = 0$. Therefore $a_1, a_2, a_3$ are all non zero and by Definition 38.1 and Lemma 38.6 | $\mathscr{A}| = |\mathscr{B}| > 0$.

The following result about finite fields is of importance for the proof of Theorem 37.1.

LEMMA 38.11. For $x \in \mathcal{F}_{pq}$ define $N(x) = x^{1+p+\cdots+p^{q-1}}$ and for $x \neq 2$ let $x^{\sigma} = \frac{1}{2-x}$. If $\alpha \in \mathcal{F}_{pq} - \mathcal{F}_p$, then for some $i$, $N(\alpha^{\sigma i}) \neq 1$.

Proof. Assume that the result is false and  $N(\alpha^{\sigma^{i}})=1$  for all i. We will first prove by induction that

$$
\alpha^ {\sigma i} = \frac {- (i - 1) \alpha + i}{- i \alpha + (i + 1)} \quad \text { for } i = 1, 2, \dots\tag{38.7}
$$

If $i = 1$ (38.7) follows from the definition of $\sigma$. Assume now that (38.7) holds for $i = k - 1$. Then

$$
\begin{array}{r l} \alpha^ {\sigma k} & = \frac {1}{2 - \left\{\frac {- (k - 2) \alpha + k - 1}{- (k - 1) \alpha + k} \right\}} \\ & = \frac {- (k - 1) \alpha + k}{- 2 (k - 1) \alpha + 2 k + (k - 2) \alpha - (k - 1)} \\ & = \frac {- (k - 1) \alpha + k}{- k \alpha + (k + 1)}. \end{array}
$$

This establishes (38.7).

Now (38.7) implies that for $j \geq 1$,

$$
\prod_ {i = 1} ^ {j} \alpha^ {\sigma i} = \frac {\prod_ {i = 1} ^ {j} \{- (i - 1) \alpha + i \}}{\prod_ {i = 1} ^ {j} \{- i \alpha + (i + 1) \}} = \frac {1}{- j \alpha + (j + 1)}.
$$

Therefore

$$
N (- j \alpha + j + 1) = \frac {1}{\prod_ {i = 1} ^ {j} N (\alpha^ {\sigma i})} = 1.
$$

Thus

(38.8)

$$
N (- a \alpha + a + 1) = 1 \quad \text { for } a \in \mathcal {F} _ {p}.
$$

Define $f(t)$ by

$$
f (t) = (t - \alpha) (t - \alpha^ {p}) \dots (t - \alpha^ {p ^ {q - 1}}).\tag{38.9}
$$

Thus $f(t)$ has coefficients in $\mathcal{F}_p$ and (38.8) yields that

$$
a ^ {q} f \left(\frac {a + 1}{a}\right) = a ^ {q} N \left(\frac {a + 1}{a} - \alpha\right) = N (a + 1 - a \alpha) = 1\tag{38.10}
$$

$$
\text { for } a \in \mathcal {F} _ {p}, a \neq 0.
$$

Let $b = \frac{a + 1}{a}$ for $a \neq 0$, then $a = \frac{1}{b - 1}$. Hence (38.10) yields that

$$
\frac {1}{(b - 1) ^ {q}} f (b) = 1 \quad \text { for } b \in \mathcal {F} _ {p}, b \neq 1.
$$

Therefore

(38.11)

$$
f (b) - (b - 1) ^ {q} = 0 \quad \text { for } b \in \mathcal {F} _ {p}, b \neq 1.
$$

$f(t) - (t - 1)^{q}$ is a polynomial of degree at most $q$. By (38.11) $f(t) - (t - 1)^{q}$ has at least $(p - 1)$ roots. As $(p - 1) > q$ we must have that $f(t) = (t - 1)^{q}$. By (38.9) $\alpha$ is a root of $f(t)$, hence $\alpha = 1$ contrary to the choice of $\alpha$. The proof is complete.

## 39. The Proof of Theorem 37.1

LEMMA 39.1. There exist functions $f, g$, and $h$ such that

(i) $f$ and $h$ map $\mathcal{X}_p \times \mathcal{X}_u \times \mathcal{X}_p$ into $\mathcal{X}_u$,

(ii) $g$ maps $\mathcal{X}_p \times \mathcal{X}_u \times \mathcal{X}_p$ into $\mathcal{X}_p$,

(iii) $P^x U^y P^z U^{f(x,y,s)} P^{g(x,y,s)} U^{h(x,y,s)} = 1$.

Furthermore for $x \neq 0, y \neq 0, z \neq 0$ (iii) determines $f(x, y, z)$, $g(x, y, z)$ and $h(x, y, z)$ uniquely and $f(x, y, z)$, $g(x, y, z)$, $h(x, y, z)$ are all nonzero.

Proof. By Lemma 38.4 the functions exist and are uniquely defined by

$$
P ^ {x} U ^ {y} P ^ {z} U ^ {f} P ^ {g} U ^ {h} = 1
$$

provided that $P^z U^y P^z$ does not lie in $\mathfrak{U}$. It is easily seen that if $x \neq 0, y \neq 0$ and $z \neq 0, P^z U^y P^z$ does not lie in $\mathfrak{U}$.

Suppose that $f(x, y, z) = 0$. Then $P^x U^y P^{s+q} = U^{-h} \in \mathfrak{U}$. Then $y = -h$ and $U^y P^{s+q} U^{-y} = P^{-x} \in \mathfrak{P}^*$. Therefore either $y = 0$ or $x = 0$. Suppose that $g(x, y, z) = 0$. Then $P^x U^y P^z = U^{-f-h}$. Thus $y = -f - h$ and $U^y P^z U^{-y} = P^{-x}$. Hence $x = 0$ or $y = 0$.

Suppose that $h(x, y, z) = 0$. Then $U^y P^z U^f P^{g+z} = 1$. Hence $y + f = 0$, then $U^y P^z U^{-y} = P^{-g-z}$. Thus $y = 0$ or $z = 0$. This completes the proof of the lemma.

Throughout the rest of this section $f, g, h$ will denote the functions defined in Lemma 39.1. For $x \in \mathcal{X}_p$, $Y$ as in Lemma 38.1, define

$$
Y _ {x} = Y ^ {- 1} P ^ {- x} Y P ^ {x}.
$$

LEMMA 39.2.

(i) $Y_{x} = Y^{-1}P^{-x}YP^{x} = P^{-x}YP^{x}Y^{-1}$

(ii) $YP^{s}Y^{-1} = Y_{-s}^{-1}P^{s}$

(iii) $YP^{\sigma}Y^{-1} = P^{\sigma}Y_{\sigma}$

for $x, z, g \in \mathcal{Z}_p$.

Proof. Since $P \in \mathfrak{P}^* \subseteq N(\mathfrak{Q}_0)$ and $\mathfrak{Q}_0$ is abelian, (i) is immediate. (iii) is a direct consequence of (i). By definition $Y_{-z} = Y^{-1}P^zYP^{-z}$. Thus $Y_{-z}^{-1} = P^zY^{-1}P^{-z}Y = YP^zY^{-1}P^{-z}$ which implies (ii).

LEMMA 39.3. For $x \in \mathcal{X}_p$, $P^{-x}UP^x = Y_x^{-1}U^{v^x}Y_x$.

Proof. By (38.2) $P^x ZP^{-x} = Z^{v^{-x}}$. By (38.1) $Z = YUY^{-1}$. Hence

$$
Y ^ {- 1} P ^ {x} Y U Y ^ {- 1} P ^ {- x} Y = U ^ {v ^ {- x}}.
$$

Conjugating both sides by  $P^{x}$ , we get that

$$
Y _ {x} ^ {- 1} U Y _ {x} = P ^ {- x} U ^ {v ^ {- x}} P ^ {x}.
$$

If both sides are raised to the  $v^{x}$ th power, the lemma follows.

LEMMA 39.4.

$$
Y _ {x} Z ^ {y} Y _ {- s} ^ {- 1} = P ^ {- x} Z ^ {- h (x, y, s)} Y _ {g (x, y, s)} ^ {- 1} P ^ {- g (x, y, s)} Z ^ {- f (x, y, s)} P ^ {- s}.
$$

Proof. Substitute (38.1) into (iii) of Lemma 39.1 to get

$$
P ^ {x} Y ^ {- 1} Z ^ {y} Y P ^ {s} Y ^ {- 1} Z ^ {f} Y P ^ {g} Y ^ {- 1} Z ^ {h} Y = 1.
$$

Conjugate by  $Y^{-1}P^{x}$  to get

$$
(P ^ {- x} Y P ^ {x} Y ^ {- 1}) Z ^ {y} (Y P ^ {y} Y ^ {- 1}) Z ^ {f} (Y P ^ {g} Y ^ {- 1}) Z ^ {h} P ^ {z} = 1.
$$

Now use the results of Lemma 39.2 to derive that

$$
Y _ {x} Z ^ {y} Y _ {- z} ^ {- 1} P ^ {z} Z ^ {f} P ^ {g} Y _ {g} Z ^ {h} P ^ {x} = 1
$$

which implies the lemma.

LEMMA 39.5. If $(a_{1}, a_{2}, a_{3}) \in \mathcal{A}$, then

$$
Y _ {2} Z ^ {a _ {1} v} Y _ {3} ^ {- 1} Y _ {1} Z ^ {a _ {2} v ^ {3}} Y _ {2} ^ {- 1} = Y _ {1} Z ^ {- a _ {3} v ^ {2}} Y _ {3} ^ {- 1}.
$$

Proof. In the definition of $\mathcal{A}$ conjugate (iii) by $P^2$. Then

$$
P ^ {- 1} U ^ {a _ {1}} P ^ {- 2} U ^ {a _ {2}} P U ^ {a _ {3}} P ^ {2} = 1,
$$

or

$$
(P ^ {- 1} U ^ {a _ {1}} P) (P ^ {- 3} U ^ {a _ {2}} P ^ {3}) = P ^ {- 2} U ^ {- a _ {3}} P ^ {2}.
$$

Hence Lemma 39.3 yields that

$$
(Y _ {1} ^ {- 1} U ^ {a _ {1} v} Y _ {1}) (Y _ {3} ^ {- 1} U ^ {a _ {2} v ^ {3}} Y _ {3}) = Y _ {2} ^ {- 1} U ^ {- a _ {3} v ^ {2}} Y _ {2}.
$$

Since $\mathfrak{Q}$ is abelian, this implies that

$$
Y _ {2} U ^ {a _ {1} v} Y _ {3} ^ {- 1} Y _ {1} U ^ {a _ {2} v ^ {3}} Y _ {2} ^ {- 1} = Y _ {1} U ^ {- a _ {3} v ^ {2}} Y _ {3} ^ {- 1}.
$$

Conjugating by $Y^{-1}$ implies the result by (38.1) and the fact that $\Omega$ is abelian.

LEMMA 39.6. For $(a_{1}, a_{2}, a_{3}) \in \mathscr{A}$ define

$$
g _ {1} = g (2, a _ {1} v, - 3)
$$

$$
g _ {2} = g (1, - a _ {3} v ^ {2}, - 3)
$$

$$
g _ {3} = g (1, a _ {2} v ^ {3}, - 2)
$$

$$
k _ {1} = h (2, a _ {1} v, - 3) - h (1, - a _ {3} v ^ {2}, - 3) v ^ {- 1}
$$

$$
k _ {2} = - f (2, a _ {1} v, - 3) - h (1, a _ {2} v ^ {3}, - 2) v ^ {- 2}
$$

$$
k _ {3} = - f (1, a _ {2} v ^ {3}, - 2) v ^ {- 1} + f (1, - a _ {3} v ^ {2}, - 3)
$$

$$
k = - g _ {s} - 1.
$$

Then

(39.1)

$$
Y _ {g _ {1}} Z ^ {k _ {1}} P Y _ {g _ {2}} ^ {- 1} = P ^ {- g _ {1}} Z ^ {k _ {2}} P ^ {2} Y _ {g _ {3}} ^ {- 1} P ^ {k} Z ^ {k _ {3}} P ^ {g _ {2}}.
$$

Proof. Use Lemmas 39.4 and 39.5 to obtain

$$
\begin{array}{r l} & P ^ {- 2} Z ^ {- h (2, a _ {1} v, - 3)} Y _ {g (2, a _ {1} v, - 3)} ^ {- 1} P ^ {- g (2, a _ {1} v, - 3)} Z ^ {- f (2, a _ {1} v, - 3)} P ^ {3}. \\ & P ^ {- 1} Z ^ {- h (1, a _ {2} v ^ {3}, - 2)} Y _ {g (1 a _ {2} v ^ {3}, - 2)} ^ {- 1} P ^ {- g (1, a _ {2} v ^ {3}, - 2)} Z ^ {- f (1, a _ {2} v ^ {3}, - 2)} P ^ {2} \\ & = Y _ {2} Z ^ {a _ {1} v} Y _ {3} ^ {- 1} Y _ {1} Z ^ {a _ {2} v ^ {3}} Y _ {2} ^ {- 1} = Y _ {1} Z ^ {- a _ {2} v ^ {3}} Y _ {3} ^ {- 1} \\ & = P ^ {- 1} Z ^ {- h (1, - a _ {3} v ^ {2}, - 3)} Y _ {g (1 - a _ {3} v ^ {2}, - 3)} ^ {- 1} P ^ {- g (1, - a _ {3} v ^ {2}, - 3)} Z ^ {- f (1, - a _ {3} v ^ {2}, - 3)} P ^ {3}. \end{array}
$$

Multiply on the left by  $Y_{g(2,a_{1}v,-3)}Z^{h(2,a_{1}v,-3)}P^{2}$  and on the right by

$$
P ^ {- 3} Z ^ {f (1, - a _ {3} v ^ {2}, - 3)} P ^ {g (1, - a _ {3} v ^ {2}, - 3)}
$$

to get

$$
A Y _ {g (1 a _ {2} v ^ {3}, - 2)} ^ {- 1} B = Y _ {g (2, a _ {1} v, - 8)} C Y _ {g (1, - a _ {3} v ^ {2}, - 8)} ^ {- 1}
$$

where

$$
A = P ^ {- g (2, a _ {1} v, - 3)} Z ^ {- f (2, a _ {1} v, - 3) - k (1, a _ {2} v ^ {3}, - 2) v ^ {- 2}} P ^ {2}
$$

$$
B = P ^ {- g (1, a _ {2} v ^ {3}, - 2) - 1} Z ^ {- f (1, a _ {2} v ^ {3}, - 2) v ^ {- 1} + f (1, - a _ {3} v ^ {2}, - 3)} P ^ {g (1, - a _ {3} v ^ {2}, - 3)}
$$

$$
C = Z ^ {h (2, a _ {1} v, - 3) - h (1, - a _ {3} v ^ {2}, - 3) v ^ {- 1}} P,
$$

or equivalently

$$
A = P ^ {- g _ {1}} Z ^ {k _ {2}} P ^ {2}, \quad B = P ^ {k} Z ^ {k _ {3}} P ^ {g _ {2}}, \quad C = Z ^ {k _ {1}} P.
$$

The lemma follows.

LEMMA 39.7. Let $(a_{1}, a_{2}, a_{3}) \in \mathcal{A}$. Use the notation of Lemma 39.6. If $k_{1} \neq 0$, then there exist elements $c_{1}, c_{3} \in \mathcal{Z}_{p}$ such that

(i) $k_{8} \neq 0$

(ii) $k_{2} + k_{3}v^{c_{3}} = k_{1}$

(iii) $Y^{-1} P Y P^{-g_2} = P^{-c_1} Y^{-1} P^{-c_3} Y$.

Proof. Conjugate (39.1) by $Q$. Since $\mathfrak{P}^*\mathfrak{Q} = C(Q)$, this yields that

$$
Y _ {g _ {1}} Z ^ {w k _ {1}} P Y _ {g _ {2}} ^ {- 1} = P ^ {- g _ {1}} Z ^ {w k _ {2}} P ^ {2} Y _ {g _ {3}} ^ {- 1} P ^ {k} Z ^ {w k _ {3}} P ^ {g _ {2}}.
$$

Taking inverses we get

$$
Y _ {g _ {2}} P ^ {- 1} Z ^ {- w k _ {1}} Y _ {g _ {1}} ^ {- 1} = P ^ {- g _ {2}} Z ^ {- w k _ {3}} P ^ {- k} Y _ {g _ {3}} P ^ {- 2} Z ^ {- w k _ {2}} P ^ {g _ {1}}.
$$

Multiplying this by (39.1) on the left yields

$$
Y _ {g _ {1}} Z ^ {(1 - w) k _ {1}} Y _ {g _ {1}} ^ {- 1} = P ^ {- g _ {1}} Z ^ {k _ {2}} P ^ {2} Y _ {g _ {3}} ^ {- 1} P ^ {k} Z ^ {(1 - w) k _ {3}} P ^ {- k} Y _ {g _ {3}} P ^ {- 2} Z ^ {- w k _ {2}} P ^ {g _ {1}}.
$$

Conjugating by  $P^{-\theta_{1}}$  yields

$$
P ^ {g _ {1}} Y _ {g _ {1}} Z ^ {(1 - w) k _ {1}} Y _ {g _ {1}} ^ {- 1} P ^ {- g _ {1}} = Z ^ {k _ {2}} P ^ {2} Y _ {g _ {3}} ^ {- 1} P ^ {k} Z ^ {(1 - w) k _ {3}} P ^ {- k} Y _ {g _ {3}} P ^ {- 2} Z ^ {- w k _ {2}}.
$$

Use Lemma 39.2 (iii) and (38.1) to get

$$
\begin{array}{r l} & Y P ^ {g _ {1}} Y ^ {- 1} Y U ^ {(1 - w) k _ {1}} Y ^ {- 1} Y P ^ {- g _ {1}} Y ^ {- 1} \\ & = Y U ^ {k _ {2}} Y ^ {- 1} P ^ {2} Y _ {g _ {3}} ^ {- 1} P ^ {k} Y U ^ {(1 - w) k _ {3}} Y ^ {- 1} P ^ {- k} Y _ {g _ {3}} P ^ {- 2} Y U ^ {- w k _ {2}} Y ^ {- 1}. \end{array}
$$

Conjugate this by Y to obtain

$$
P ^ {g _ {1}} U ^ {(1 - w) k _ {1}} P ^ {- g _ {1}} = U ^ {k _ {2}} Y ^ {- 1} P ^ {2} Y _ {g _ {3}} ^ {- 1} P ^ {k} Y U ^ {(1 - w) k _ {3}} Y ^ {- 1} P ^ {- k} Y _ {g _ {3}} P ^ {- 2} Y U ^ {- w k _ {2}}.
$$

Multiply on the left by  $U^{-k_{2}}$  and on the right by  $U^{wk_{2}}$  to obtain

$$
U ^ {- k _ {2}} P ^ {g _ {1}} U ^ {(1 - w) k _ {1}} P ^ {- g _ {1}} U ^ {w k _ {2}} = W _ {1} U ^ {k _ {3} (1 - w)} W _ {1} ^ {- 1},\tag{39.2}
$$

$$
W _ {1} = Y ^ {- 1} P ^ {2} Y _ {g _ {3}} ^ {- 1} P ^ {k} Y.
$$

Suppose that $U^{k_3(1 - w)} = 1$. Then (39.2) implies that

$$
P ^ {g _ {1}} U ^ {(1 - w) k _ {1}} P ^ {- g _ {1}} = U ^ {(1 - w) k _ {2}}.
$$

By Hypothesis $k_{1} \neq 0$, hence by Lemma 38.2, $U^{(1-w)k_{1}} \neq 1$. By Lemma 39.1 $g_{1} \neq 0$. Thus the above equality cannot hold in the Frobenius group $\mathfrak{M}$. Hence $U^{k_{3}(1-w)} \neq 1$. This proves statement (i) of the lemma.

Let $U_0 = W_1 U^{k_3(1-w)} W_1^{-1}$. By (39.2) $U_0$ is a conjugate of $U^{k_3(1-w)}$ which lies in $\mathfrak{P}\mathfrak{U}$. All conjugates of $U^{k_3(1-w)}$ which lie in $\mathfrak{U}$ are of the form

$$
U ^ {k _ {3} (1 - w) v ^ {c _ {3}} w ^ {c _ {1}}} ,
$$

with $c_{3} \in \mathcal{X}_{p}, c' \in \mathcal{X}_{g}$. Hence

$$
U _ {0} = W _ {1} U ^ {k _ {3} (1 - w)} W _ {1} ^ {- 1} = W _ {2} ^ {- 1} U ^ {k _ {3} (1 - w) v ^ {c _ {3}} w ^ {c ^ {\prime}}} W _ {2}\tag{39.3}
$$

for some $W_{2} \in \mathfrak{P}$. Thus $W_{2}W_{1} \in N(\mathfrak{U})$. Since $Q \in N(\mathfrak{U})$, we get that $Q^{-1}W_{2}W_{1}Q \in N(\mathfrak{U})$. By (39.2) $W_{1}Q = QW_{1}$, thus $Q^{-1}W_{2}W_{1}Q = Q^{-1}W_{2}QW_{1}$. Hence

$$
W _ {2} Q ^ {- 1} W _ {2} ^ {- 1} Q = W _ {2} W _ {1} (Q ^ {- 1} W _ {1} ^ {- 1} W _ {2} ^ {- 1} Q) \in N (\mathfrak {U}).
$$

However $W_{2}Q^{-1}W_{2}^{-1}Q \in \mathfrak{P}$. Since $\mathfrak{P} \cap N(\mathfrak{U}) = 1$, this yields that $Q \in C(W_{2})$. Hence $W_{2} \in \mathfrak{P} \cap C(Q) = \mathfrak{P}^{*}$. Thus

$$
W _ {2} = P ^ {c _ {2}}\tag{39.4}
$$

for some $c_{2} \in \mathcal{X}_{p}$. Now (39.2) and (39.4) show that

$$
W _ {2} W _ {1} \in \mathfrak {Q} _ {0} \mathfrak {P} ^ {*} \cap N (\mathfrak {U}).
$$

Since $P \in N(\langle Z \rangle)$, we have $Y^{-1}PY \in N(\mathfrak{U})$, thus $\mathfrak{Q}_{\mathfrak{v}}\mathfrak{P}^{*} \cap N(\mathfrak{U}) = \langle Y^{-1}PY \rangle$. Therefore

$$
W _ {2} W _ {1} = Y ^ {- 1} P ^ {c _ {0}} Y\tag{39.5}
$$

for some $c_{0} \in \mathcal{X}_{p}$. Consequently

$$
(W _ {2} W _ {1}) ^ {- 1} U ^ {k _ {3} (1 - w) v ^ {c _ {3}} w ^ {c ^ {\prime}}} W _ {2} W _ {1} = U ^ {k _ {3} (1 - w) v ^ {c _ {3}} + c _ {0} w ^ {c ^ {\prime}}}.
$$

If this is compared with (39.3) we see that

$$
c _ {0} + c _ {3} = 0, \quad c ^ {\prime} = 0.\tag{39.6}
$$

Using (39.4) and (39.6) in (39.5) leads to

$$
W _ {1} = P ^ {- c _ {2}} Y ^ {- 1} P ^ {- c _ {3}} Y.\tag{39.7}
$$

Comparing (39.2) and (39.7), we get

$$
P ^ {- c _ {2}} Y ^ {- 1} P ^ {- c _ {3}} Y = Y ^ {- 1} P ^ {2} Y _ {g _ {3}} ^ {- 1} P ^ {k} Y.
$$

Conjugating by  $Y^{-1}$  gives

$$
Y P ^ {- c _ {2}} Y ^ {- 1} P ^ {- c _ {3}} = P ^ {2} Y _ {g _ {3}} ^ {- 1} P ^ {k}.\tag{39.8}
$$

If we substitute (39.7) into (39.2) we get

$$
U ^ {- k _ {2}} P ^ {g _ {1}} U ^ {(1 - w) k _ {1}} P ^ {- g _ {1}} U ^ {k _ {2} w} = P ^ {- c _ {2}} U ^ {k _ {3} (1 - w) v ^ {c _ {3}}} P ^ {c _ {2}}.
$$

Multiply on the left by  $U^{-k_{3}v^{c_{3}}}P^{c_{2}}$  and on the right by  $U^{-k_{2}w}P^{g_{1}}U^{k_{1}w}$  to get

$$
U ^ {- k _ {3} v ^ {c _ {3}}} P ^ {c _ {2}} U ^ {- k _ {2}} P ^ {q _ {1}} U ^ {k _ {1}} = U ^ {- w k _ {3} v ^ {c _ {3}}} P ^ {c _ {2}} U ^ {- k _ {2} w} P ^ {q _ {1}} U ^ {k _ {1} w}.
$$

Since the right hand side is the left hand side conjugated by Q, we see that Q centralizes the left hand side. Hence

$$
U ^ {- k _ {8} v ^ {c _ {3}}} P ^ {c _ {2}} U ^ {- k _ {2}} P ^ {g _ {1}} U ^ {k _ {1}} = P ^ {c _ {1}}\tag{39.9}
$$

for some $c_{1} \in \mathcal{X}_{p}$. Reading (39.9) mod $\mathfrak{P}$ yields that

$$
k _ {1} = k _ {2} + k _ {3} v ^ {c _ {3}}
$$

which proves (ii) of the lemma. Substituting (ii) of Lemma 39.2

into (39.8) we get that

$$
P ^ {2} Y _ {g _ {3}} ^ {- 1} P ^ {k} = Y _ {c _ {2}} ^ {- 1} P ^ {- c _ {2} - c _ {3}}.\tag{39.10}
$$

Substituting (39.10) into (39.1) leads to

$$
Y _ {g _ {1}} Z ^ {k _ {1}} P Y _ {g _ {2}} ^ {- 1} = P ^ {- g _ {1}} Z ^ {k _ {2}} Y _ {c _ {2}} ^ {- 1} P ^ {- c _ {2} - c _ {3}} Z ^ {k _ {3}} P ^ {g _ {2}}.
$$

Multiply on the left by  $P^{g_{1}}$  and on the right by  $P^{-g_{2}}$ . Then using Lemma 39.2 (ii) and (iii) this becomes

$$
Y P ^ {\theta_ {1}} Y ^ {- 1} Z ^ {k _ {1}} P Y P ^ {- \theta_ {2}} Y ^ {- 1} = Z ^ {k _ {2}} Y _ {c _ {2}} ^ {- 1} P ^ {- c _ {2} - c _ {3}} Z ^ {k _ {3}}.
$$

Use $Z = YUY^{-1}$ to get

$$
Y P ^ {g _ {1}} U ^ {k _ {1}} Y ^ {- 1} P Y P ^ {- g _ {2}} Y ^ {- 1} = Y U ^ {k _ {2}} Y ^ {- 1} Y _ {c _ {2}} ^ {- 1} P ^ {- c _ {2} - c _ {3}} Y U ^ {k _ {3}} Y ^ {- 1}.
$$

Conjugate by Y and multiply on the left by  $U^{-k_{2}}$  to get

$$
U ^ {- k _ {2}} P ^ {\sigma_ {1}} U ^ {k _ {1}} Y ^ {- 1} P Y P ^ {- \sigma_ {2}} = Y ^ {- 1} Y _ {c _ {2}} ^ {- 1} P ^ {- c _ {2} - c _ {3}} Y U ^ {k _ {3}}.\tag{39.11}
$$

Conjugate by Q and take inverses, then

$$
P ^ {g _ {2}} Y ^ {- 1} P ^ {- 1} Y U ^ {- k _ {1} w} P ^ {- g _ {1}} U ^ {k _ {2} w} = U ^ {- k _ {3} w} Y ^ {- 1} P ^ {c _ {2} + c _ {3}} Y _ {c _ {2}} Y.
$$

Multiply by (39.11) on the right to get

$$
P ^ {\theta_ {2}} Y ^ {- 1} P ^ {- 1} Y U ^ {- k _ {1} w} P ^ {- \theta_ {1}} U ^ {k _ {2} (w - 1)} P ^ {\theta_ {1}} U ^ {k _ {1}} Y ^ {- 1} P Y P ^ {- \theta_ {2}} = U ^ {k _ {3} (1 - w)}.
$$

Conjugate by  $W_{1}^{-1}$  to get

$$
\begin{array}{r l} & W _ {1} P ^ {\sigma_ {2}} Y ^ {- 1} P ^ {- 1} Y U ^ {- k _ {1} w} P ^ {- \sigma_ {1}} U ^ {k _ {2} (w - 1)} P ^ {\sigma_ {1}} U ^ {k _ {1}} Y ^ {- 1} P Y P ^ {- \sigma_ {2}} W _ {1} ^ {- 1} \\ & = W _ {1} U ^ {k _ {3} (1 - w)} W _ {1} ^ {- 1}. \end{array}
$$

Using (39.2) and (39.3), this yields

$$
\begin{array}{r l} & W _ {1} P ^ {g _ {2}} Y ^ {- 1} P ^ {- 1} Y \{U ^ {- k _ {1} w} P ^ {- g _ {1}} U ^ {k _ {2} (w - 1)} P ^ {g _ {1}} U ^ {k _ {1}} \} Y ^ {- 1} P Y P ^ {- g _ {2}} W _ {1} ^ {- 1} \\ & = U _ {0} = U ^ {- k _ {2}} P ^ {g _ {1}} U ^ {(1 - w) k _ {1}} P ^ {- g _ {1}} U ^ {w k _ {2}}. \end{array}\tag{39.12}
$$

Now by the second equation in (39.12)

$$
U ^ {- k _ {1} w} P ^ {- g _ {1}} U ^ {k _ {2} w} U ^ {- k _ {2}} P ^ {g _ {1}} U ^ {k _ {1}} = U ^ {- k _ {1} w} P ^ {- g _ {1}} U ^ {k _ {2} w} U _ {0} U ^ {- k _ {2} w} P ^ {g _ {1}} U ^ {k _ {1} w}.
$$

Thus the first equation in (39.12) implies that

$$
U ^ {- k _ {2} w} P ^ {g _ {1}} U ^ {k _ {1} w} Y ^ {- 1} P Y P ^ {- g _ {2}} W _ {1} ^ {- 1} \in C (U _ {0}).
$$

By (39.3) and (39.4), $C(U_0) = P^{-c_2}\mathfrak{U}^*P^{c_2}$. Hence

$$
U ^ {- k _ {2} w} P ^ {g _ {1}} U ^ {k _ {1} w} Y ^ {- 1} P Y P ^ {- g _ {2}} W _ {1} ^ {- 1} = P ^ {- c _ {2}} U _ {2} P ^ {c _ {2}}\tag{39.13}
$$

for some $U_{2} \in \mathfrak{U}^{*}$. We wish to show that $U_{2} \in \mathfrak{U}$. To do this conjugate (39.13) by $Q$ to get

$$
U ^ {- k _ {2} w ^ {2}} P ^ {g _ {1}} U ^ {k _ {1} w ^ {2}} Y ^ {- 1} P Y P ^ {- g _ {2}} W _ {1} ^ {- 1} = P ^ {- c _ {2}} U _ {2} ^ {w} P ^ {c _ {2}}\tag{39.14}
$$

by (39.7). Multiply (39.13) by the inverse of (39.14) on the right to get

$$
U ^ {- k _ {2} w} P ^ {g _ {1}} U ^ {k _ {1} w} U ^ {- k _ {1} w ^ {2}} P ^ {- g _ {1}} U ^ {k _ {2} w ^ {2}} = P ^ {- c _ {2}} U _ {2} ^ {1 - w} P ^ {c _ {2}}.\tag{39.15}
$$

By Lemma 38.2 $U_{2}$ and $U_{2}^{1-w}$ have the same order. Since the left hand side of (39.15) is in $\mathfrak{P}\mathfrak{U}$, this implies that the order of $U_{2}$ divides $u$, thus $U_{2} \in \mathfrak{U}$.

Multiply (39.13) on the left by  $U_{2}^{-1}P^{c_{2}}$  and on the right by  $W_{1}P^{g_{2}}Y^{-1}P^{-1}Y$  to get

$$
U _ {2} ^ {- 1} P ^ {c _ {2}} U ^ {- k _ {2} w} P ^ {g _ {1}} U ^ {k _ {1} w} = P ^ {c _ {2}} W _ {1} P ^ {g _ {2}} Y ^ {- 1} P ^ {- 1} Y.\tag{39.16}
$$

By (39.7) the right hand side is in $C(Q)$, while the left hand side is in $\mathfrak{P}\mathfrak{U}$. Since $C(Q) \cap \mathfrak{P}\mathfrak{U} = \mathfrak{P}^*$, this yields that

$$
U _ {2} ^ {- 1} P ^ {c _ {2}} U ^ {- k _ {2} w} P ^ {g _ {1}} U ^ {k _ {1} w} = P ^ {c ^ {\prime \prime}}\tag{39.17}
$$

for some $c'' \in \mathcal{X}_p$. Conjugate by $Q^{-1}$ to get

$$
U _ {2} ^ {- w ^ {- 1}} P ^ {c _ {2}} U ^ {- k _ {2}} P ^ {g _ {1}} U ^ {k _ {1}} = P ^ {c ^ {\prime \prime}}.
$$

Comparing this with (39.9) yields that

$$
U _ {2} ^ {w ^ {- 1}} P ^ {c ^ {\prime \prime}} = U ^ {k _ {3} v ^ {c _ {3}}} P ^ {c _ {1}},
$$

so that

$$
U _ {2} ^ {w ^ {- 1}} = U ^ {k _ {3} v ^ {c _ {3}}} , \quad c _ {1} = c ^ {\prime \prime} .
$$

Using (39.16) and (39.17) this yields

$$
P ^ {c _ {1}} = P ^ {c _ {2}} W _ {1} P ^ {g _ {2}} Y ^ {- 1} P ^ {- 1} Y
$$

or

$$
P ^ {c _ {1} - c _ {2}} Y ^ {- 1} P Y P ^ {- g _ {2}} = W _ {1}.
$$

Hence by (39.7)

$$
P ^ {c _ {1} - c _ {2}} Y ^ {- 1} P Y P ^ {- g _ {2}} = P ^ {- c _ {2}} Y ^ {- 1} P ^ {- c _ {3}} Y.
$$

This immediately implies (iii) of the lemma and thus completes the proof.

LEMMA 39.8. Let $(a_1, a_2, a_3) \in \mathcal{A}$, and let $k_1$ have the same meaning as in Lemma 39.6. Then $k_1 = 0$.

Proof. Suppose that  $k_{1} \neq 0$ , so that Lemma 39.7 may be applied. Let

$$
h _ {1} = h (2, a _ {1} v, - 3)
$$

$$
h _ {2} = h (1, a _ {2} v ^ {3}, - 2)
$$

$$
h _ {3} = h (1, - a _ {3} v ^ {2}, - 3).
$$

By Lemma 38.5 (i)

$$
\begin{array}{r l} f (2, a _ {1} v, - 3) & = - a _ {1} v - h _ {1} \\ f (1, a _ {2} v ^ {3}, - 2) & = - a _ {2} v ^ {3} - h _ {2} \\ f (1, - a _ {3} v ^ {2}, - 3) & = a _ {3} v ^ {2} - h _ {3}. \end{array}
$$

Hence in the notation of Lemma 39.6

$$
\begin{array}{l} k _ {1} = h _ {1} - h _ {3} v ^ {- 1} \\ k _ {2} = a _ {1} v + h _ {1} - h _ {3} v ^ {- 2} \\ k _ {3} = a _ {2} v ^ {2} + h _ {2} v ^ {- 1} + a _ {3} v ^ {2} - h _ {3}. \end{array}
$$

Since $a_1 + a_2 + a_3 = 0$, this yields that

$$
\begin{array}{r l} k _ {3} & = - a _ {1} v ^ {2} + h _ {2} v ^ {- 1} - h _ {3} \\ k _ {1} - k _ {2} & = - a _ {1} v + h _ {2} v ^ {- 2} - h _ {3} v ^ {- 1}. \end{array}
$$

Thus

$$
(k _ {1} - k _ {2}) v = k _ {3}
$$

or

$$
k _ {2} + k _ {3} v ^ {- 1} = k _ {1}.
$$

By Lemma 39.7 (ii) this implies that $k_{3}(v^{c_{3}} - v^{-1}) = 0$. If $c_{3} \neq -1$, then by Lemma 38.2, $(v^{c_{3}} - v^{-1})$ has an inverse in $\mathcal{X}_{u}$. Thus $k_{3} = 0$ contrary to Lemma 39.7 (i). Therefore $c_{3} = -1$. Now Lemma 39.7 (iii) becomes

(39.18)

$$
Y ^ {- 1} P Y P ^ {- g _ {2}} = P ^ {- c _ {1}} Y ^ {- 1} P Y.
$$

Reading (39.18) mod $\mathfrak{Q}$ implies that $g_{2} = c_{1}$. Thus (39.18) yields that $Y^{-1}PY$ and $P^{-g_{2}}$ commute. Since $g_{2} \neq 0$ by Lemma 39.1, this implies that

$$
P ^ {- 1} Y ^ {- 1} P Y \in \mathfrak {Q} _ {0} \cap C (P) = \{1 \}.
$$

Thus $Y \in \mathfrak{Q}_0 \cap C(P) = \{1\}$ which is not the case. Therefore $k_1 = 0$ as required.

LEMMA 39.9 Let $(a_{1}, a_{2}, a_{3}) \in \mathcal{A}$, let $k_{2}$ and $k_{3}$ have the same meaning as in Lemma 39.6. Then $k_{2} = k_{3} = 0$.

Proof. Since $k_{1} = 0$ by Lemma 39.8, (39.1) becomes

$$
Y _ {g _ {1}} P Y _ {g _ {2}} ^ {- 1} = P ^ {- g _ {1}} Z ^ {k _ {2}} P ^ {2} Y _ {g _ {3}} ^ {- 1} P ^ {k} Z ^ {k _ {3}} P ^ {g _ {2}}.\tag{39.19}
$$

Conjugating by Q and using (38.2) we get that

$$
Y _ {g _ {1}} P Y _ {g _ {2}} ^ {- 1} = P ^ {- g _ {1}} Z ^ {w k _ {2}} P ^ {2} Y _ {g _ {3}} ^ {- 1} P ^ {k} Z ^ {w k _ {3}} P ^ {g _ {2}}.\tag{39.20}
$$

Now (39.19) and (39.20) imply that

$$
Z ^ {k _ {2}} P ^ {2} Y _ {\vartheta_ {3}} ^ {- 1} P ^ {k} Z ^ {k _ {3}} = Z ^ {w k _ {2}} P ^ {2} Y _ {\vartheta_ {3}} ^ {- 1} P ^ {k} Z ^ {w k _ {3}}.
$$

'Therefore

$$
P ^ {2} Y _ {g _ {3}} ^ {- 1} P ^ {k} Z ^ {k _ {3} (1 - w)} P ^ {- k} Y _ {g _ {3}} P ^ {- 2} = Z ^ {k _ {2} (w - 1)}.\tag{39.21}
$$

Suppose that $k_{3} \neq 0$. Then by Lemma 38.2 $k_{3}(1 - w) \neq 0$. As $\langle Z \rangle$ is a T.I. set in $\mathfrak{G}$, (39.21) now implies that $P^{2}Y_{g_{3}}^{-1}P^{k} \in N(\langle Z \rangle)$. As $P \in N(\langle Z \rangle)$ this implies that

$$
Y ^ {- 1} P ^ {- \sigma_ {3}} Y P ^ {\sigma_ {3}} = Y _ {\sigma_ {3}} \in N (\langle Z \rangle) \cap \mathfrak {Q} _ {0} = \langle 1 \rangle .
$$

Therefore $P^{g_{3}}$ commutes with Y. Hence $g_{3} = 0$. This is contrary to Lemma 39.1. Thus $k_{3} = 0$.

Now (39.21) implies that $k_{2}(w - 1) = 0$. Therefore by Lemma 38.2 $k_{2} = 0$.

LEMMA 39.10. Let $(a_{1}, a_{2}, a_{3}) \in \mathcal{A}$ and $g_{3}$ have the same meaning as in Lemma 39.6. Then $g_{3} = 1$.

Proof. In view of Lemmas 39.8 and 39.9 equation (39.1) becomes

$$
Y _ {g _ {1}} P Y _ {g _ {2}} ^ {- 1} = P ^ {- g _ {1}} P ^ {2} Y _ {g _ {3}} ^ {- 1} P ^ {k} P ^ {g _ {2}}.\tag{39.22}
$$

Reading (39.22) mod $\mathfrak{D}_0$ implies that

$$
1 = - g _ {1} + 2 + k + g _ {2}
$$

or using the definition of k

$$
- 1 - g _ {3} = k = - 1 + g _ {1} - g _ {2}.\tag{39.23}
$$

Hence $g_{3} = g_{2} - g_{1}$ and (39.22) becomes

$$
Y _ {g _ {1}} P Y _ {g _ {2}} ^ {- 1} = P ^ {2 - g _ {1}} Y _ {g _ {2} - g _ {1}} ^ {- 1} P ^ {g _ {1} - 1}.\tag{39.24}
$$

P acts as a linear transformation on  $Q_{0}$ . It is convenient to use the exponential notation. Thus  $Y^{P}=P^{-1}YP$ , so that  $Y_{z}=Y^{-1+P^{2}}$ . (39.24) can be rewritten as

$$
P ^ {- 1} Y _ {g _ {1}} P Y _ {g _ {2}} ^ {- 1} = P ^ {- (g _ {1} - 1)} Y _ {g _ {2} - g _ {1}} ^ {- 1} P ^ {g _ {1} - 1}.
$$

In exponential notation this becomes

$$
Y ^ {(- 1 + P ^ {\theta 1}) P + (1 - P ^ {\theta 2})} = Y ^ {(1 - P ^ {\theta 2 - \theta 1}) P ^ {\theta 1 - 1}}.\tag{39.25}
$$

Define

$$
\begin{array}{r l} A & = (- 1 + P ^ {g _ {1}}) P + (1 - P ^ {g _ {2}}) - (1 - P ^ {g _ {2} - g _ {1}}) P ^ {g _ {1} - 1} \\ & = (1 - P) + P ^ {g _ {1} - 1} (P ^ {2} - 1) - P ^ {g _ {2} - 1} (P - 1). \end{array}\tag{39.26}
$$

Since $\mathfrak{P}^*\mathfrak{Q}_0$ is a Frobenius group with Frobenius kernel $\mathfrak{Q}_0$, $1 - P$ is an invertible linear transformation on $\mathfrak{Q}_0$. By (39.25) $A$ annihilates $Y$. Hence also $A(1 - P)^{-1}$ annihilates $Y$. By (39.26)

$$
\begin{array}{r l} A (1 - P) ^ {- 1} & = 1 - P ^ {\theta_ {1} - 1} (P + 1) + P ^ {\theta_ {2} - 1} \\ & = 1 - P ^ {\theta_ {1}} + 1 - P ^ {\theta_ {1} - 1} - 1 + P ^ {\theta_ {2} - 1}. \end{array}
$$

Therefore

$$
Y _ {\theta_ {2} - 1} Y _ {\theta_ {1} - 1} ^ {- 1} Y _ {\theta_ {1}} ^ {- 1} = Y ^ {(- 1 + P ^ {\theta_ {2} - 1}) - (- 1 + P ^ {\theta_ {1} - 1}) - (- 1 + P ^ {\theta_ {1})}} = 1.
$$

Thus

(39.27)

$$
Y _ {\theta_ {2} - 1} = Y _ {\theta_ {1}} Y _ {\theta_ {1} - 1}.
$$

By Lemma 39.3

$$
Y _ {g _ {2} - 1} ^ {- 1} U ^ {v ^ {g _ {2} - 1}} Y _ {g _ {2} - 1} = P ^ {- (g _ {2} - 1)} U P ^ {(g _ {2} - 1)}.
$$

By (39.27) this yields that

$$
Y _ {g _ {1} - 1} ^ {- 1} Y _ {g _ {1}} ^ {- 1} U ^ {v ^ {g _ {2} - 1}} Y _ {g _ {1}} Y _ {g _ {1} - 1} = P ^ {- (g _ {2} - 1)} U P ^ {(g _ {2} - 1)}.\tag{39.28}
$$

Lemma 39.2 also implies that

$$
Y _ {g _ {1}} ^ {- 1} U ^ {v ^ {g _ {1}}} Y _ {g _ {1}} = P ^ {- g _ {1}} U P ^ {g _ {1}}.
$$

Raising this to the  $v^{g_{2}-g_{1}-1}$ th power we get that

$$
Y _ {g _ {1}} ^ {- 1} U ^ {v ^ {g _ {2} - 1}} Y _ {g _ {1}} = P ^ {- g _ {1}} U ^ {v ^ {g _ {2} - g _ {1} - 1}} P ^ {g _ {1}}.\tag{39.29}
$$

Now (39.28) and (39.29) yield that

$$
Y _ {g _ {1} - 1} ^ {- 1} P ^ {- g _ {1}} U ^ {v ^ {g _ {2} - g _ {1} - 1}} P ^ {g _ {1}} Y _ {g _ {1} - 1} = P ^ {- (g _ {2} - 1)} U P ^ {(g _ {2} - 1)}.\tag{39.30}
$$

Another application of Lemma 39.3 gives

$$
Y _ {g _ {1} - 1} ^ {- 1} U ^ {v ^ {\theta_ {1} - 1}} Y _ {g _ {1} - 1} = P ^ {- (g _ {1} - 1)} U P ^ {(g _ {1} - 1)}.\tag{39.31}
$$

Thus (39.30) and (39.31) imply that

$$
\begin{array}{r l} & Y _ {\vartheta_ {1} - 1} ^ {- 1} [ P ^ {- \vartheta_ {1}} U ^ {\vartheta_ {2} - \vartheta_ {1} - 1} P ^ {\vartheta_ {1}}, U ^ {\vartheta_ {1} - 1} ] Y _ {\vartheta_ {1} - 1} \\ & \quad = [ P ^ {- (\vartheta_ {2} - 1)} U P ^ {(\vartheta_ {2} - 1)}, P ^ {- (\vartheta_ {1} - 1)} U P ^ {(\vartheta_ {1} - 1)} ]. \end{array}\tag{39.32}
$$

Since $g_1 \neq 0$, $P^{-\sigma_1} U^{v^{\sigma_2 - \sigma_1 - 1}} P^{\sigma_1} \notin \mathfrak{U}$. Therefore

$$
[ P ^ {- \sigma_ {1}} U ^ {v ^ {\sigma_ {2} - \sigma_ {1} - 1}} P ^ {\sigma_ {1}},   U ^ {v ^ {\sigma_ {1} - 1}} ] \in \mathfrak {P} ^ {\sharp}  .
$$

As $\mathfrak{P}$ is a T.I. set in $\mathfrak{G}$ (39.32) now implies that

$$
Y _ {\vartheta_ {1} - 1} \in N (\mathfrak {P}) \cap \mathfrak {Q} _ {0} = 1.
$$

Therefore $P^{g_1 - 1}$ commutes with $Y$ and so $g_1 = 1$. Now (39.27) yields that $Y_{g_2 - 1} = Y_1$, or

$$
Y ^ {- 1} P ^ {- (g _ {2} - 1)} Y P ^ {(g _ {2} - 1)} = Y ^ {- 1} P ^ {- 1} Y P.
$$

Consequently  $P^{-(g_{2}-2)}YP^{(g_{2}-2)} = Y$ . Hence  $g_{2} = 2$ . Now (39.23) implies that  $g_{3} = 1$  as required.

LEMMA 39.11. Let B have the same meaning as in Definition 38.2. If  $a \in B$  then  $-a \in B$ .

Proof. Let $a = a_1 \in \mathcal{B}$ and suppose that $(a_1, a_2, a_3) \in \mathcal{A}$. By Lemma 38.8 $(-a_2, -a_1, -a_3) \in \mathcal{A}$. Let $(-a_2, -a_1, -a_3)$ play the role of $(a_1, a_2, a_3)$. By Lemma 39.10 $g_3 = g(1, -a_1v^3, -2) = 1$. Thus Lemmas 38.5 and 39.1 imply that

(39.33)

$$
- a _ {1} v ^ {3} + f (1, - a _ {1} v ^ {3}, - 2) + h (1, - a _ {1} v ^ {3}, - 2) = 0\tag{39.34}
$$

$$
\omega^ {- a _ {1} v ^ {3}} - 2 + \omega^ {- a _ {1} v ^ {3} + h (1, - a _ {1} v ^ {3}, - 2)} = 0.
$$

Let $b_{1} = -a_{1}v^{3}$, $b_{2} = f(1, -a_{1}v^{3}, -2)$ and $b_{3} = h(1, -a_{1}v^{3}, -2)$. By Lemma 39.1 $b_{i} \neq 0$ for $i = 1, 2, 3$. By (39.33) $b_{1} + b_{2} + b_{3} = 0$. Now it follows from (39.34) and Lemma 38.7 that $(b_{1}, b_{2}, b_{3}) \in \mathcal{A}$. Thus $-av^{3} = -a_{1}v^{3} = b_{1} \in \mathcal{B}$.

Since $a$ was an arbitrary element of $\mathcal{B}$ we get that for any integer $n$, $a(-v^{3})^{n} \in \mathcal{B}$. Thus in particular, $a(-v^{3})^{p} \in \mathcal{B}$. Hence by (38.2), $-a = -av^{3p} \in \mathcal{B}$ as was to be shown.

It is now very easy to complete the proof of Theorem 37.1.

Define the set $\mathcal{C}$ by

$$
\mathcal {C} = \{\omega^ {a} | a \in \mathcal {B} \}.
$$

Since $|\mathcal{B}| = |\mathcal{C}|$, Lemma 38.10 yields that $\mathcal{C}$ is not empty. The definition of $\mathcal{B}$ and Lemma 38.7 yield that $1 \notin \mathcal{C}$ and $\alpha \in \mathcal{C}$ if and only if $2 - \alpha \in \mathcal{C}$. Lemma 39.11 implies that $\alpha \in \mathcal{C}$ if and only if $\alpha^{-1} \in \mathcal{C}$. Therefore if $\alpha \in \mathcal{C}$ then $\frac{1}{2 - \alpha} \in \mathcal{C}$. Since $u = 1 + p + \cdots + p^{q-1}$, we have $N(\alpha) = \alpha^{1+p+\cdots+p^{q-1}} = 1$ for $\alpha \in \mathcal{C}$. Thus if $\sigma$ has the same meaning as in Lemma 38.11 then there exists $\alpha \in \mathcal{F}_{p^q} - \mathcal{F}_p$ such that $N(\alpha^{\sigma^i}) = 1$ for all values of $i$. This contradicts Lemma 38.11, and completes the proof of the main theorem of this paper.

# PACIFIC JOURNAL OF MATHEMATICS

EDITORS

RALPH S. PHILLIPS
Stanford University
Stanford, California

J. DUGUNDJI
University of Southern California
Los Angeles 7, California

M. G. ARSOVE
University of Washington
Seattle 5, Washington

LOWELL J. PAIGE
University of California
Los Angeles 24, California

E. F. BECKENBACH
T. M. CHERRY

D. DERRY
M. OHTSUKA

EDITORS
H. L. ROYDEN
E. SPANIER

E. G. STRAUS
F. WOLF

SUPPORTING INSTITUTIONS

UNIVERSITY OF BRITISH COLUMBIA
CALIFORNIA INSTITUTE OF TECHNOLOGY
UNIVERSITY OF CALIFORNIA
MONTANA STATE UNIVERSITY
UNIVERSITY OF NEVADA
NEW MEXICO STATE UNIVERSITY
OREGON STATE UNIVERSITY
UNIVERSITY OF OREGON
OSAKA UNIVERSITY
UNIVERSITY OF SOUTHERN CALIFORNIA

STANFORD UNIVERSITY
UNIVERSITY OF TOKYO
UNIVERSITY OF UTAH
WASHINGTON STATE UNIVERSITY
UNIVERSITY OF WASHINGTON
\*    \*    \*

AMERICAN MATHEMATICAL SOCIETY CALIFORNIA RESEARCH CORPORATION SPACE TECHNOLOGY LABORATORIES NAVAL ORDNANCE TEST STATION

Mathematical papers intended for publication in the Pacific Journal of Mathematics should be typewritten (double spaced), and the author should keep a complete copy. Manuscripts may be sent to any one of the four editors. All other communications to the editors should be addressed to the managing editor, L. J. Paige at the University of California, Los Angeles 24, California.

50 reprints per author of each article are furnished free of charge; additional copies may be obtained at cost in multiples of 50.

The Pacific Journal of Mathematics is published quarterly, in March, June, September, and December. Effective with Volume 13 the price per volume (4 numbers) is \$18.00; single issues, \$5.00. Special price for current issues to individual faculty members of supporting institutions and to individual members of the American Mathematical Society: \$8.00 per volume; single issues \$2.50. Back numbers are available.

Subscriptions, orders for back numbers, and changes of address should be sent to Pacific Journal of Mathematics, 103 Highland Boulevard, Berkeley 8, California.

Printed at Kokusai Bunken Insatsusha (International Academic Printing Co., Ltd.), No. 6, 2 chome, Fujimi-cho, Chiyoda-ku, Tokyo, Japan.

PUBLISHED BY PACIFIC JOURNAL OF MATHEMATICS, A NON-PROFIT CORPORATION
The Supporting Institutions listed above contribute to the cost of publication of this Journal, but they are not owners or publishers and have no responsibility for its content or policies

## Pacific Journal of Mathematics Vol. 13, No. 3 May, 1963

Walter Feit and John Griggs Thompson, Chapter I, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....775
Walter Feit and John Griggs Thompson, Chapter II, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....789
Walter Feit and John Griggs Thompson, Chapter III, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....803
Walter Feit and John Griggs Thompson, Chapter IV, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....845
Walter Feit and John Griggs Thompson, Chapter V, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....943
Walter Feit and John Griggs Thompson, Chapter VI, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....1011
Walter Feit and John Griggs Thompson, Bibliography, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....1029

# Pacific Journal of Mathematics

BIBLIOGRAPHY, FROM SOLVABILITY OF GROUPS OF ODD ORDER, PACIFIC J. MATH., VOL. 13, NO. 3 (1963)

WALTER FEIT AND JOHN GRIGGS THOMPSON

May 1963

1. N. Blackburn, On a special class of p-groups, Acta Math., 100 (1958), 45-92.

2. \_\_\_\_, Generalizations of certain elementary theorems on p-groups, Proc. London Math. Soc. (3), 11 (1961), 1-22.

3. R. Brauer, On the connection between the ordinary and the modular characters of finite groups, Ann. of Math. (2), 42 (1941), 926-935.

4. W. Burnside, Theory of Groups of Finite Order, Cambridge, 1911.

5. ——, On groups of order $p^{\alpha}q^{\beta}$, Proc. London Math. Soc., (2), 2 (1904), 432-437.

6. L. E. Dickson, Linear Groups, New York, 1958.

7. W. Feit, On the structure of Frobenius groups, Can. J. Math., 9 (1958), 587-596.

8. \_\_\_\_, On a class of doubly transitive permutation groups, Ill. J. Math., 4 (1960), 170-186.

9. \_\_\_\_, Exceptional Characters, Proceedings of the Symposium in pure mathematics, A.M.S., 6 (1962), 67–70.

10. W. Feit, M. Hall, Jr. and J. G. Thompson, Finite groups in which the centralizer of any non-identity element is nilpotent, Math. Zeitschr., 74 (1960), 1-17.

11. W. Feit and J. G. Thompson, A solvability criterion for finite groups and some consequences, Proc. Nat. Acad. Sci. 48 (1962), 968-70.

12. M. Hall, Jr., The Theory of Groups, New York, 1959.

13. P. Hall, A note on soluble groups, J. London Math. Soc., 3 (1928), 98-105.

14. \_\_\_\_, A contribution to the theory of groups of prime power order, Proc. London Math. Soc., (2) 36 (1933), 29-95.

15. \_\_\_\_, A characteristic property of soluble groups, J. London Math. Soc., 12 (1937), 198-200.

16. \_\_\_\_, On the Sylow systems of a soluble group, Proc. London Math. Soc., (2) 43 (1937), 316-323.

17. \_\_\_\_, On the system normalizers of a soluble group, Proc. London Math. Soc., (2), 43 (1937), 507-528.

18. \_\_\_\_, Theorems like Sylows, Proc. London Math. Soc., (3), 6 (1956), 286-304.

19. \_\_\_\_, Some sufficient conditions for a group to be nilpotent, Ill. J. Math., 2 (1958), 787-801.

20. ——, Lecture Notes.

21. P. Hall and G. Higman, The $p$-length of a $p$-soluble group, and reduction theorems for Burnside's problem, Proc. London Math. Soc., (3), 7 (1956), 1-42.

22. B. Huppert, Subnormale untergruppen und Sylowgruppen, Acta Szeged., 22 (1961), 46–61.

23. ——, Gruppen mit modularer Sylow-Gruppe, Math. Zeitschr., 75 (1961), 140-153.

24. M. Suzuki, On finite groups with cyclic Sylow subgroups for all odd primes, Amer. J. Math., 77 (1955), 657-691.

25. \_\_\_\_, A new type of simple groups of finite order, Proc. Nat. Acad. Sci., 46 (1960), 868–870.

26. J. G. Thompson, Finite groups with fixed-point-free automorphisms of prime order, Proc. Nat. Acad. Sci., 45 (1959), 578-581.

27. ——, Normal p-complements for finite groups, Math. Zeitschr., 72 (1960), 332-354.

28. H. Zassenhaus, The Theory of Groups, Second Edition, New York, 1958.

CORNELL UNIVERSITY

UNIVERSITY OF CHICAGO

INSTITUTE FOR DEFENSE ANALYSES

HARVARD UNIVERSITY

# PACIFIC JOURNAL OF MATHEMATICS

EDITORS

RALPH S. PHILLIPS
Stanford University
Stanford, California

J. DUGUNDJI
University of Southern California
Los Angeles 7, California

M. G. ARSOVE
University of Washington
Seattle 5, Washington

LOWELL J. PAIGE
University of California
Los Angeles 24, California

E. F. BECKENBACH
T. M. CHERRY

D. DERRY
M. OHTSUKA

EDITORS
H. L. ROYDEN
E. SPANIER

E. G. STRAUS
F. WOLF

SUPPORTING INSTITUTIONS

UNIVERSITY OF BRITISH COLUMBIA
CALIFORNIA INSTITUTE OF TECHNOLOGY
UNIVERSITY OF CALIFORNIA
MONTANA STATE UNIVERSITY
UNIVERSITY OF NEVADA
NEW MEXICO STATE UNIVERSITY
OREGON STATE UNIVERSITY
UNIVERSITY OF OREGON
OSAKA UNIVERSITY
UNIVERSITY OF SOUTHERN CALIFORNIA

STANFORD UNIVERSITY
UNIVERSITY OF TOKYO
UNIVERSITY OF UTAH
WASHINGTON STATE UNIVERSITY
UNIVERSITY OF WASHINGTON
\*    \*    \*

AMERICAN MATHEMATICAL SOCIETY CALIFORNIA RESEARCH CORPORATION SPACE TECHNOLOGY LABORATORIES NAVAL ORDNANCE TEST STATION

Mathematical papers intended for publication in the Pacific Journal of Mathematics should be typewritten (double spaced), and the author should keep a complete copy. Manuscripts may be sent to any one of the four editors. All other communications to the editors should be addressed to the managing editor, L. J. Paige at the University of California, Los Angeles 24, California.

50 reprints per author of each article are furnished free of charge; additional copies may be obtained at cost in multiples of 50.

The Pacific Journal of Mathematics is published quarterly, in March, June, September, and December. Effective with Volume 13 the price per volume (4 numbers) is \$18.00; single issues, \$5.00. Special price for current issues to individual faculty members of supporting institutions and to individual members of the American Mathematical Society: \$8.00 per volume; single issues \$2.50. Back numbers are available.

Subscriptions, orders for back numbers, and changes of address should be sent to Pacific Journal of Mathematics, 103 Highland Boulevard, Berkeley 8, California.

Printed at Kokusai Bunken Insatsusha (International Academic Printing Co., Ltd.), No. 6, 2 chome, Fujimi-cho, Chiyoda-ku, Tokyo, Japan.

PUBLISHED BY PACIFIC JOURNAL OF MATHEMATICS, A NON-PROFIT CORPORATION
The Supporting Institutions listed above contribute to the cost of publication of this Journal, but they are not owners or publishers and have no responsibility for its content or policies

## Pacific Journal of Mathematics Vol. 13, No. 3 May, 1963

Walter Feit and John Griggs Thompson, Chapter I, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....775
Walter Feit and John Griggs Thompson, Chapter II, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....789
Walter Feit and John Griggs Thompson, Chapter III, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....803
Walter Feit and John Griggs Thompson, Chapter IV, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....845
Walter Feit and John Griggs Thompson, Chapter V, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....943
Walter Feit and John Griggs Thompson, Chapter VI, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....1011
Walter Feit and John Griggs Thompson, Bibliography, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....1029

# Pacific Journal of Mathematics

BIBLIOGRAPHY, FROM SOLVABILITY OF GROUPS OF ODD ORDER, PACIFIC J. MATH., VOL. 13, NO. 3 (1963)

WALTER FEIT AND JOHN GRIGGS THOMPSON

May 1963

1. N. Blackburn, On a special class of p-groups, Acta Math., 100 (1958), 45-92.

2. \_\_\_\_, Generalizations of certain elementary theorems on p-groups, Proc. London Math. Soc. (3), 11 (1961), 1-22.

3. R. Brauer, On the connection between the ordinary and the modular characters of finite groups, Ann. of Math. (2), 42 (1941), 926-935.

4. W. Burnside, Theory of Groups of Finite Order, Cambridge, 1911.

5. ——, On groups of order $p^{\alpha}q^{\beta}$, Proc. London Math. Soc., (2), 2 (1904), 432-437.

6. L. E. Dickson, Linear Groups, New York, 1958.

7. W. Feit, On the structure of Frobenius groups, Can. J. Math., 9 (1958), 587-596.

8. \_\_\_\_, On a class of doubly transitive permutation groups, Ill. J. Math., 4 (1960), 170-186.

9. \_\_\_\_, Exceptional Characters, Proceedings of the Symposium in pure mathematics, A.M.S., 6 (1962), 67–70.

10. W. Feit, M. Hall, Jr. and J. G. Thompson, Finite groups in which the centralizer of any non-identity element is nilpotent, Math. Zeitschr., 74 (1960), 1-17.

11. W. Feit and J. G. Thompson, A solvability criterion for finite groups and some consequences, Proc. Nat. Acad. Sci. 48 (1962), 968-70.

12. M. Hall, Jr., The Theory of Groups, New York, 1959.

13. P. Hall, A note on soluble groups, J. London Math. Soc., 3 (1928), 98-105.

14. \_\_\_\_, A contribution to the theory of groups of prime power order, Proc. London Math. Soc., (2) 36 (1933), 29-95.

15. \_\_\_\_, A characteristic property of soluble groups, J. London Math. Soc., 12 (1937), 198-200.

16. \_\_\_\_, On the Sylow systems of a soluble group, Proc. London Math. Soc., (2) 43 (1937), 316-323.

17. \_\_\_\_, On the system normalizers of a soluble group, Proc. London Math. Soc., (2), 43 (1937), 507-528.

18. ——, Theorems like Sylows, Proc. London Math. Soc., (3), 6 (1956), 286-304.

19. \_\_\_\_, Some sufficient conditions for a group to be nilpotent, Ill. J. Math., 2 (1958), 787-801.

20. ——, Lecture Notes.

21. P. Hall and G. Higman, The $p$-length of a $p$-soluble group, and reduction theorems for Burnside's problem, Proc. London Math. Soc., (3), 7 (1956), 1-42.

22. B. Huppert, Subnormale untergruppen und Sylowgruppen, Acta Szeged., 22 (1961), 46–61.

23. ——, Gruppen mit modularer Sylow-Gruppe, Math. Zeitschr., 75 (1961), 140-153.

24. M. Suzuki, On finite groups with cyclic Sylow subgroups for all odd primes, Amer. J. Math., 77 (1955), 657-691.

25. \_\_\_\_, A new type of simple groups of finite order, Proc. Nat. Acad. Sci., 46 (1960), 868–870.

26. J. G. Thompson, Finite groups with fixed-point-free automorphisms of prime order, Proc. Nat. Acad. Sci., 45 (1959), 578-581.

27. ——, Normal p-complements for finite groups, Math. Zeitschr., 72 (1960), 332-354.

28. H. Zassenhaus, The Theory of Groups, Second Edition, New York, 1958.

CORNELL UNIVERSITY

UNIVERSITY OF CHICAGO

INSTITUTE FOR DEFENSE ANALYSES

HARVARD UNIVERSITY

# PACIFIC JOURNAL OF MATHEMATICS

EDITORS

RALPH S. PHILLIPS
Stanford University
Stanford, California

J. DUGUNDJI
University of Southern California
Los Angeles 7, California

M. G. ARSOVE
University of Washington
Seattle 5, Washington

LOWELL J. PAIGE
University of California
Los Angeles 24, California

E. F. BECKENBACH
T. M. CHERRY

D. DERRY
M. OHTSUKA

EDITORS
H. L. ROYDEN
E. SPANIER

E. G. STRAUS
F. WOLF

SUPPORTING INSTITUTIONS

UNIVERSITY OF BRITISH COLUMBIA
CALIFORNIA INSTITUTE OF TECHNOLOGY
UNIVERSITY OF CALIFORNIA
MONTANA STATE UNIVERSITY
UNIVERSITY OF NEVADA
NEW MEXICO STATE UNIVERSITY
OREGON STATE UNIVERSITY
UNIVERSITY OF OREGON
OSAKA UNIVERSITY
UNIVERSITY OF SOUTHERN CALIFORNIA

STANFORD UNIVERSITY
UNIVERSITY OF TOKYO
UNIVERSITY OF UTAH
WASHINGTON STATE UNIVERSITY
UNIVERSITY OF WASHINGTON
\*    \*    \*

AMERICAN MATHEMATICAL SOCIETY CALIFORNIA RESEARCH CORPORATION SPACE TECHNOLOGY LABORATORIES NAVAL ORDNANCE TEST STATION

Mathematical papers intended for publication in the Pacific Journal of Mathematics should be typewritten (double spaced), and the author should keep a complete copy. Manuscripts may be sent to any one of the four editors. All other communications to the editors should be addressed to the managing editor, L. J. Paige at the University of California, Los Angeles 24, California.

50 reprints per author of each article are furnished free of charge; additional copies may be obtained at cost in multiples of 50.

The Pacific Journal of Mathematics is published quarterly, in March, June, September, and December. Effective with Volume 13 the price per volume (4 numbers) is \$18.00; single issues, \$5.00. Special price for current issues to individual faculty members of supporting institutions and to individual members of the American Mathematical Society: \$8.00 per volume; single issues \$2.50. Back numbers are available.

Subscriptions, orders for back numbers, and changes of address should be sent to Pacific Journal of Mathematics, 103 Highland Boulevard, Berkeley 8, California.

Printed at Kokusai Bunken Insatsusha (International Academic Printing Co., Ltd.), No. 6, 2 chome, Fujimi-cho, Chiyoda-ku, Tokyo, Japan.

PUBLISHED BY PACIFIC JOURNAL OF MATHEMATICS, A NON-PROFIT CORPORATION
The Supporting Institutions listed above contribute to the cost of publication of this Journal, but they are not owners or publishers and have no responsibility for its content or policies

## Pacific Journal of Mathematics Vol. 13, No. 3 May, 1963

Walter Feit and John Griggs Thompson, Chapter I, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....775
Walter Feit and John Griggs Thompson, Chapter II, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....789
Walter Feit and John Griggs Thompson, Chapter III, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....803
Walter Feit and John Griggs Thompson, Chapter IV, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....845
Walter Feit and John Griggs Thompson, Chapter V, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....943
Walter Feit and John Griggs Thompson, Chapter VI, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....1011
Walter Feit and John Griggs Thompson, Bibliography, from Solvability of groups of odd order, Pacific J. Math., vol. 13, no. 3 (1963)....1029