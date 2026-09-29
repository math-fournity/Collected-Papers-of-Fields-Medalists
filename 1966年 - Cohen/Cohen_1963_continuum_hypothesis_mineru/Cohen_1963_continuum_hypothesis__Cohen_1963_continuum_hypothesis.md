$^{19}$  Gardner, R. S., A. J. Wahba, C. Basilio, R. S. Miller, P. Lengyel, and J. F. Speyer, these PROCEEDINGS, 48, 2087 (1962).

$^{20}$  Ralph, R. K., and H. G. Khorana, J. Am. Chem. Soc., 83, 2926 (1961).

$^{21}$  Ames, B. N., and D. T. Dubin, J. Biol. Chem., 235, 769 (1960).

$^{22}$  Chen, P. S., Jr., T. Y. Toribara, and H. Warner, Anal. Chem., 28, 1756 (1956).

$^{23}$  Heppel, L. A., D. R. Harkness, and R. J. Hilmoe, J. Biol. Chem., 237, 841 (1962).

$^{24}$  Razzell, W. E., and H. G. Khorana, J. Biol. Chem., 234, 2114 (1959).

$^{25}$  Kay, E. R. M., N. S. Simmons, and A. L. Dounce, J. Am. Chem. Soc., 74, 1724 (1952).

$^{26}$  Sherman, J. R., and J. Adler, J. Biol. Chem., 238, 873 (1962).

$^{27}$  Waley, S. G., and J. Watson, Biochem. J., 55, 328 (1953).

$^{28}$  Akabori, S., K. Ohno, and K. Narita, Bull. Chem. Soc. Japan, 25, 214 (1952).

$^{29}$  Lowry, O. H., N. J. Rosebrough, A. L. Farr, and R. J. Randall, J. Biol. Chem., 193, 265 (1951).

$^{30}$  Nakamoto, T., and S. B. Weiss, these PROCEEDINGS, 48, 880 (1962).

$^{31}$  Fox, C. F., W. S. Robinson, and S. B. Weiss, Fed. Proc., 22, 463 (1963).

$^{32}$  Krakow, J. S., and S. Ochoa, these PROCEEDINGS, 49, 88 (1963).

# THE INDEPENDENCE OF THE CONTINUUM HYPOTHESIS

By Paul J. Cohen\*

DEPARTMENT OF MATHEMATICS, STANFORD UNIVERSITY

Communicated by Kurt Gödel, September 30, 1963

This is the first of two notes in which we outline a proof of the fact that the Continuum Hypothesis cannot be derived from the other axioms of set theory, including the Axiom of Choice. Since Gödel $^{3}$ has shown that the Continuum Hypothesis is consistent with these axioms, the independence of the hypothesis is thus established. We shall work with the usual axioms for Zermelo-Fraenkel set theory, $^{2}$ and by Z-F we shall denote these axioms without the Axiom of Choice, (but with the Axiom of Regularity). By a model for Z-F we shall always mean a collection of actual sets with the usual $\epsilon$-relation satisfying Z-F. We use the standard definitions $^{3}$ for the set of integers $\omega$, ordinal, and cardinal numbers.

THEOREM 1. There are models for Z-F in which the following occur:

(1) There is a set $a, a \subseteq \omega$ such that $a$ is not constructible in the sense of reference 3, yet the Axiom of Choice and the Generalized Continuum Hypothesis both hold.

(2) The continuum (i.e., $\mathcal{P}(\omega)$ where $\mathcal{P}$ means power set) has no well-ordering.

(3) The Axiom of Choice holds, but $\aleph_1 \neq 2^{\aleph_0}$.

(4) The Axiom of Choice for countable pairs of elements in $\mathcal{P}(\mathcal{P}(\omega))$ fails.

Only part 3 will be discussed in this paper. In parts 1 and 3 the universe is well-ordered by a single definable relation. Note that 4 implies that there is no simple ordering of $\mathcal{P}(\mathcal{P}(\omega))$. Since the Axiom of Constructibility implies the Generalized Continuum Hypothesis,$^{3}$ and the latter implies the Axiom of Choice,$^{5}$ Theorem 1 completely settles the question of the relative strength of these axioms.

Before giving details, we sketch the intuitive ideas involved. The starting point is the realization $^{1,4}$ that no formula $\mathfrak{a}(x)$ can be shown from the axioms of Z-F to have the property that the collection of all x satisfying it form a model for Z-F in which the Axiom of Constructibility $(V = L,^{3})$ fails. Thus, to find such models, it seems natural to strengthen Z-F by postulating the existence of a set which is a

model for Z-F, thus giving us greater flexibility in constructing new models. (In the next paper we discuss how the question of independence, as distinct from that of models, can be handled entirely within Z-F.) The Löwenheim-Skolem theorem yields the existence of a countable model M. Let  $N_{1}, N_{2}$ , etc., denote the corresponding cardinals in M. Since M is countable, there exist distinct sets  $a_{\delta} \subseteq \omega$ ,  $0 \leq \delta \leq N_{2}$ . Put  $V = \{\langle a_{\delta}, a_{\delta'} \rangle | \delta < \delta' \}$ . We form the model N “generated” from M,  $a_{\delta}$ , and V and hope to prove that in N the continuum has cardinality at least  $N_{2}$ . Of course, N will contain many new sets and, if the  $a_{\delta}$  are chosen indiscriminately, the set  $N_{2}$  (in M) may become countable in N. Rather than determine the  $a_{\delta}$  directly, we first list all the countably many possible propositions concerning them and decide in advance which are to be true. Only those properties which are true in a “uniform” manner for “generic” subsets of  $\omega$  in M shall be true for the  $a_{\delta}$  in N. For example, each  $a_{\delta}$  contains infinitely many primes, has no asymptotic density, etc. If the  $a_{\delta}$  are chosen in such a manner, no new information will be extracted from them in N which was not already contained in M, so that, e.g.,  $N_{2}$  will remain the second uncountable cardinal. The primitive conditions  $n \in a_{\delta}$  are neither generically true nor false, and hence must be treated separately. Only when given a finite set of such conditions will we be able to speak of properties possibly being forced to hold for “generic” sets. The precise definition of forcing will be given in Definition 6.

From now on, let $\mathfrak{M}$ be a fixed countable model for Z-F, satisfying $V = L$, such that $x \in \mathfrak{M}$ implies $x \subset \mathfrak{M}$. If $\mathfrak{M}'$ is a countable model without this property, define $\Psi$ by transfinite induction on the rank of $x$, so that $\Psi(x) = \{y | \exists z \in \mathfrak{M}', z \in x, \Psi(z) = y\}$; the image $\mathfrak{M}$ of $\mathfrak{M}'$ under $\Psi$ is isomorphic to $\mathfrak{M}'$ with respect to $\epsilon$ and satisfies our requirement. Thus, the ordinals in $\mathfrak{M}$ are truly ordinals. Let $\tau > 1$ be a fixed ordinal in $\mathfrak{M}$, $\aleph_{\tau}$ the corresponding cardinal in $\mathfrak{M}$, and let $a_{\delta}, 0 \leq \delta < \aleph_{\tau}$ be subsets of $\omega$, not necessarily in $\mathfrak{M}$, $V = \{\langle a_{\delta}, a_{\delta'} \rangle | \delta < \delta'\}$.

LEMMA 1. There exist unique functions $j$, $K_{1}$, $K_{2}$, $N$, from ordinals to ordinals definable in $\mathfrak{M}$ such that

(1) $j(\alpha + 1) > j(\alpha)$ and for all $\beta$ such that $j(\alpha) + 1 < \beta < j(\alpha + 1)$ the map $\beta \to (N(\beta), K_1(\beta), K_2(\beta))$ is a 1-1 correspondence between all such $\beta$, and the set of all triples $(i, \gamma, \delta)$, $1 \leq i \leq 8$, $\gamma < j(\alpha)$, $\delta < j(\alpha)$. Furthermore, this map is order-preserving if the triples are given the natural ordering $S$ (Ref. 3, p. 36).

(2) $j(0) = 3\aleph_{\tau} + 1, j(\alpha) = \sup \{j(\beta) | \beta < \alpha\}$ if $\alpha$ is a limit ordinal.

(3) $N(j(\alpha)) = 0, N(j(\alpha) + 1) = 9, K_i = 0$ for these values.

(4) $N(\alpha), K_i(\alpha)$ are zero if $\alpha \leq 3\aleph_r$.

(5) If $\beta$ is as above, and $N(\beta) = i$, put $J(i, K_1(\beta), K_2(\beta), j(\alpha)) = \beta$. Also put $I(\beta) = j(\alpha)$.

Definition 1: For $\alpha$ an ordinal in $\mathfrak{M}$, define $F_{\alpha}$ by means of induction as follows: (1) $F_{\alpha} = \alpha$ if $\alpha \leq \omega$.

(2) For $\omega < \alpha < 3\aleph_r$, let $F_{\alpha}$ successively enumerate $a_{\delta}$, the unordered pairs $(a_{\delta}, a_{\delta'})$ and the ordered pairs $\langle a_{\delta}, a_{\delta'} \rangle$ in any standard manner (e.g., the ordering $R$ on pairs of ordinals def. 7.81$^3$).

(3) For $\alpha = 3\aleph_{\tau}, F_{\alpha} = V$.

(4) For $\alpha > 3\aleph_{\tau}$, if $K_{1}(\alpha) = \beta$, $K_{2}(\alpha) = \gamma$

$$
\text { if } N (\alpha) = 0, F _ {\alpha} = \left\{F _ {\alpha^ {\prime}} \mid \alpha^ {\prime} <   \alpha \right\}
$$

$$
\text { if   } 1 \leq i = N (\alpha) \leq 8, F _ {\alpha} = \mathfrak {F} _ {i} (F _ {\beta}, F _ {\gamma})
$$

where $\mathfrak{F}_i$ are defined as follows (Def. 9.1):

$$
\begin{array}{l} \mathfrak {F} _ {1} (x, y) = \{x, y \} \\ \mathfrak {F} _ {2} (x, y) = \{\langle s, t \rangle | s \in t, \langle s, t \rangle \in x \} \\ \mathfrak {F} _ {3} (x, y) = x - y \\ \mathfrak {F} _ {4} (x, y) = \{\langle s, t \rangle | \langle s, t \rangle \in x, t \in y \} \\ \mathfrak {F} _ {5} (x, y) = \{s | s \in x, \exists t \langle t, s \rangle \in y \} \\ \mathfrak {F} _ {6} (x, y) = \{\langle s, t \rangle | \langle s, t \rangle \in x, \langle t, s \rangle \in y \} \\ \mathfrak {F} _ {7} (x, y) = \{\langle r, s, t \rangle | \langle r, s, t \rangle \in x, \langle t, r, s \rangle \in y \} \\ \mathfrak {F} _ {8} (x, y) = \{\langle r, s, t \rangle | \langle r, s, t \rangle \in x, \langle r, t, s \rangle \in y \} \end{array}
$$

if $N(\alpha) = 9$, $F_{\alpha} = \{F_{\alpha'} | \alpha' < \alpha, N(\alpha') = 9\}$. We also define $T_{\alpha} = \{F_{\beta} | \beta < \alpha\}$. We have introduced the case $N = 9$ for the convenience of later arguments. It ensures that the ordinals in $\mathfrak{M}$ are listed among the $F_{\alpha}$ in a canonical manner. Observe that since $V = L$ holds in $\mathfrak{M}$, it is not difficult to see that this implies $\mathfrak{M} \subseteq \mathfrak{N}$.

Denote by $\mathfrak{N}$, the set of all $F_{\alpha}$ for $\alpha \in \mathfrak{M}$. Note that in $\mathfrak{N}$ each $F_{\alpha}$ is a collection of preceding $F_{\beta}$. We shall often write $\alpha$ in place of $F_{\alpha}$ if $\alpha \leq \omega$, and $a_{\delta}$ in place of $F_{\delta + \omega + 1}$, etc., if there is no danger of confusion. If $N(\alpha) = 9$, then the set $F_{\alpha}$ is defined independently of $a_{\delta}$. We shall now examine statements concerning $F_{\alpha}$ before the $a_{\delta}$ are actually determined, and thus the $F_{\alpha}$ for a while shall be considered as merely formal symbols.

Definition 2: (1) $x \in y$, $x \in F_{\alpha}$, $F_{\alpha} \in x$, $F_{\alpha} \in F_{\beta}$ are formulas; (2) if $\varphi$ and $\psi$ are formulas, so are $\neg \varphi$ and $\varphi \& \psi$; and (3) only (1) and (2) define formulas.

Definition 3: A Limited Statement is a formula $\mathfrak{a}(x_1, \ldots, x_n)$ in which all variables are bound by a universal quantifier $(x_i)_\alpha$ or an existential quantifier $\exists_{\alpha} x_i$ placed in front of it, where $\alpha$ is an ordinal in $\mathfrak{M}$. An Unlimited Statement is the same except that no ordinals are attached to the quantifiers.

Our intention is that the variable x in  $(x)_{\alpha}$  or  $\exists_{\alpha}x$  is restricted to range over all  $F_{\beta}$  with  $\beta < \alpha$ . The symbol = is not used since by means of the Axiom of Extensionality it can be avoided. We only consider statements in prenex form. Since it is clear how to reduce negations, conjunctions, etc., of such statements to prenex form, we shall not do so if there is no risk of confusion.

Definition 4: The rank of a limited statement $\mathfrak{a}$ is $(\alpha, r)$ if $r$ is the number of quantifiers and $\alpha$ is the least ordinal such that for all $\beta, \beta < \alpha$ if $F_{\beta}$ occurs in $\mathfrak{a}$, and $\beta \leq \alpha$ if $(x)_{\beta}$ or $\exists_{\beta} x$ occurs in $\mathfrak{a}$. We write $(\alpha, r) < (\beta, s)$ if $\alpha < \beta$ or $\alpha = \beta$ and $r < s$.

Thus, if $\operatorname{rank} \mathfrak{a} = (\alpha, r)$, $\mathfrak{a}$ can be formulated in $\{F_{\beta} | \beta < \alpha\}$.

Definition 5: Let $P$ denote a finite set of conditions of the form $n \in a_{\delta}$ or $\neg n \in a_{\delta}$ such that no condition and its negation are both included.

In the following definition, which is the key point of the paper, we shall define a certain concept for all limited statements by means of transfinite induction. The well-ordering we use is not, however, precisely the corresponding ordering of the ranks, but requires a slight modification. We say $\mathfrak{a}$ is of type $\mathfrak{R}$, if $\operatorname{rank} \mathfrak{a} = (\alpha + 1, r)$, $(x)_{\alpha + 1}$ and $\exists_{\alpha + 1} x$ do not occur in $\mathfrak{a}$, and no expression of the form $F_{\alpha} \epsilon(\cdot)$ occurs in $\mathfrak{a}$. We order the limited statements by saying, if $\operatorname{rank} \mathfrak{a} = (\alpha, r)$ and $\operatorname{rank} \mathfrak{b} = (\beta, s)$, $\mathfrak{a}$ precedes $\mathfrak{b}$ if and only if $\operatorname{rank} \mathfrak{a} < \operatorname{rank} \mathfrak{b}$, unless $\alpha = \beta$ and one of

the two statements a, b is of type R and the other is not of type R, in which case the former precedes the latter.

Definition 6: By induction, we define the concept of “P forces a” as follows:
I. If r > 0, P forces  $\mathfrak{a} = (x)_{\alpha}\mathfrak{b}(x)$  if for all  $P' \supset P$ ,  $P'$  does not force  $\neg\mathfrak{b}(F_{\beta})$  for  $\beta < \alpha$ . P forces  $\exists_{\alpha}x\mathfrak{b}(x)$  if for some  $\beta < \alpha$ , P forces  $\mathfrak{b}(F_{\beta})$ .

II. If r = 0, and a has propositional connectives, P forces a if for each component  $F_{\alpha} \in F_{\beta}$  or  $\neg F_{\alpha} \in F_{\beta}$  appearing in a, these, by case III of this definition, are forced to be true or their negations are forced to be true so that in the usual sense of the propositional calculus a is true.

III. If $\mathfrak{a}$ is of the form $F_{\alpha} \in F_{\beta}$ or $\neg F_{\alpha} \in F_{\beta}$, we define $P$ forces $\mathfrak{a}$ as follows:

(i) If $\alpha, \beta \leq 3\aleph_r$, then $\mathfrak{a}$ must hold as a formal consequence of $P$, i.e., $P$ forces $\mathfrak{a}$, if $\mathfrak{a}$ is true whenever $a_{\delta}$ are distinct subsets of $\omega$, satisfying $P$, different from any integer and $\omega$.

(ii) $\neg F_{\alpha} \in F_{\alpha}$ is always forced.

(iii) If $\alpha < \beta, N(\beta) = i < 9, \beta > 3\aleph_r$, $P$ forces $\mathfrak{a}$, where $\mathfrak{a} \equiv F_{\alpha} \in F_{\beta}$ or $\neg F_{\alpha} \in F_{\beta}$, if $P$ forces $\psi_i$ or $\neg \psi_i$, respectively, where $\psi_i$ is the limited statement expressing the definition of $F_{\beta}$. That is, if $K_1(\beta) = \gamma$, $K_2(\beta) = \delta$:

(0) $\psi_0$ is vacuous and always forced.

(1) $\psi_{1} \equiv F_{\alpha} = F_{\gamma} \vee F_{\alpha} = F_{\delta}$.

(2) $\psi_{2} \equiv \exists_{\beta} x \exists_{\beta} y (F_{\alpha} = \langle x, y \rangle \& x \in y \& F_{\alpha} \in F_{\gamma}).$

(3) $\psi_{3} \equiv F_{\alpha} \in F_{\gamma} \& \neg F_{\alpha} \in F_{\delta}$.

(4) $\psi_{4} \equiv \exists_{\beta} x \exists_{\beta} y (F_{\alpha} = \langle x, y \rangle \& F_{\alpha} \in F_{\gamma} \& y \in F_{\delta}).$

(5) $\psi_{5} \equiv \exists_{\beta} x (F_{\alpha} \in F_{\gamma} \& \langle x, F_{\alpha} \rangle \in F_{\delta}).$

(6), (7), (8), similarly.

Here the use of ordered pairs must eventually be replaced by their definition, and the use of equality in $x = y$ is replaced by $(z)_{\beta}(z \in x \Longleftrightarrow z \in y)$.

(iv) If $\alpha < \beta$, $N(\beta) = 9$, $\beta > 3\aleph_r$, $P$ forces $\mathfrak{a} \equiv F_{\alpha} \in F_{\beta}$ if for some $\beta' < \beta$, $N(\beta') = 9$, $P$ forces $F_{\alpha} = F_{\beta'}$. $P$ forces $\neg F_{\alpha} \in F_{\beta}$, if for all $\beta' < \beta$, $N(\beta') = 9$ and all $P' \supset P$, $P'$ does not force $F_{\alpha} = F_{\beta'}$. Again the symbol = is treated as before.

(v) If $\alpha > \beta$, we reduce the case $F_{\alpha} \in F_{\beta}$ to cases (iii) and (iv) treated above. We say $P$ forces $F_{\alpha} \in F_{\beta}$ if for some $\beta' < \beta$, $P$ forces $F_{\beta'} \in F_{\beta}$ and $P$ forces $F_{\alpha} = F_{\beta'}$ (i.e., $(x)_{\alpha}(x \in F_{\alpha} \Longleftrightarrow x \in F_{\beta'})$ which is a statement of type $\mathfrak{R}$ and hence precedes $F_{\alpha} \in F_{\beta}$). We say $P$ forces $\neg F_{\alpha} \in F_{\beta}$ if for all $\beta' < \beta$ and $P' \supset P$, $P'$ does not force both $F_{\beta'} \in F_{\beta}$ and $F_{\beta'} = F_{\alpha}$.

The most important part of Definition 6 is I, the other parts are merely obvious derivatives of it.

Definition 7: If a is an unlimited statement with r quantifiers, we define “P forces a” by induction on r. If r = 0, then a is a limited statement. If  $\mathfrak{a} \equiv (x) \mathfrak{b}(x)$ , P forces a, if for all  $P' \supset P$ , and  $\alpha$ ,  $P'$  does not force  $\neg \mathfrak{b}(F_{\alpha})$ . If  $\mathfrak{a} \equiv \exists x \mathfrak{b}(x)$ , P forces a if for some  $\alpha$ , P forces  $\mathfrak{b}(F_{\alpha})$ .

In the proofs of Lemmas 2, 3, 4, and 5, we keep the same well-ordering on limited statements as in Definition 6, and proceed by induction.

LEMMA 2. $P$ does not force $\mathfrak{a}$ and $\neg \mathfrak{a}$, for any $\mathfrak{a}$ and $P$.

Proof: Let $\mathfrak{a}$ be a limited statement with $r$ quantifiers. If $r > 0$, and $P$ forces both $\exists_{\alpha}x\mathfrak{b}(x)$ and $(x)_{\alpha}\neg \mathfrak{b}(x)$, then $P$ must force $\mathfrak{b}(F_{\beta})$ for $\beta < \alpha$ which means $P$ cannot force $(x)_{\alpha}\neg \mathfrak{b}(x)$. Case II of Definition 6 will clearly follow from case III. Parts (i) and (ii) are trivial. If $\mathfrak{a}$ is in part (iii), then $P$ forces $\mathfrak{a}$ if and only if $P$

forces a statement of lower rank and in this case the lemma follows by induction. In part (iv), if $P$ forces $F_{\alpha} \in F_{\beta}$, then for some $\beta' < \beta$, $N(\beta') = 9$, and $P$ forces $F_{\alpha} = F_{\beta'}$ which means $P$ can not force $\neg F_{\alpha} \in F_{\beta}$. In part (v) if $P$ forces $F_{\alpha} \in F_{\beta}$, for some $\beta' < \beta$, $P$ forces $F_{\beta'} \in F_{\beta}$ and $F_{\alpha} = F_{\beta'}$ which again violates $P$ forcing $\neg F_{\alpha} \in F_{\beta}$. If $\mathfrak{a}$ is an unlimited statement, the lemma follows in the same manner by induction on the number of quantifiers.

LEMMA 3. If $P$ forces $\mathfrak{a}$ and $P' \supset P$, then $P'$ forces $\mathfrak{a}$.

Proof by induction as in Lemma 2.

LEMMA 4. For any statement $\mathfrak{a}$ and condition $P$, there is $P' \supset P$ such that either $P'$ forces $\mathfrak{a}$ or $P'$ forces $\neg \mathfrak{a}$.

Proof: Let $\mathfrak{a}$ be a limited statement with $r$ quantifiers. If $r > 0$ and $P$ does not force $\mathfrak{a} \equiv (x)_{\alpha} \mathfrak{b}(x)$, then for some $P' \supset P$, $P'$ forces $\neg \mathfrak{b}(F_{\beta})$, $\beta < \alpha$, which means $P'$ forces $\neg \mathfrak{a}$. If $r = 0$, we may restrict ourselves to III, for if we enumerate the components of $\mathfrak{a}$, by defining a finite sequence $P_n$, $P_0 = P$ and $P_{n+1} \supset P_n$ we may successively force each component or its negation so that finally either $\mathfrak{a}$ or $\neg \mathfrak{a}$ is forced. Again, cases (i) and (ii) are trivially disposed of. Case (iii) is handled by induction as before. If $\mathfrak{a} \equiv F_{\alpha} \in F_{\beta}$ is in case (iv) then if $P$ does not force $\neg \mathfrak{a}$, for some $P' \supset P$ and $\beta' < \beta$, $N(\beta') = 9$, $P'$ forces $F_{\alpha} = F_{\beta'}$ so $P'$ forces $\mathfrak{a}$. If $\mathfrak{a} \equiv F_{\alpha} \in F_{\beta}$ is in case (v) if $P$ does not force $\neg \mathfrak{a}$, then for some $P' \supset P$, $\beta' < \beta$, $P'$ forces $F_{\beta'} \in F_{\beta}$ and $F_{\beta'} = F_{\alpha'}$ hence $P'$ forces $\mathfrak{a}$. Unlimited statements are handled as before.

Definition 8: Enumerate all statements $\mathfrak{a}_n$, both limited and unlimited, and all ordinals $\alpha_n$ in $\mathfrak{M}$. Define $P_{2n}$ as the first extension of $P_{2n-1}$ which forces either $\mathfrak{a}_n$ or $\neg \mathfrak{a}_n$. Define $P_{2n+1}$ as the first extension of $P_{2n}$ which has the property that it forces $F_\beta \in F_{\alpha_n}$ where $\beta$ is the least possible ordinal for which there exists such an extension of $P_{2n}$, whereas if no such $\beta$ exists, put $P_{2n+1} = P_{2n}$.

The sequence  $P_{n}$  is not definable in M. Since all statements of the form  $n \in a_{\delta}$  are enumerated,  $P_{n}$  clearly approach in an obvious sense, sets  $a_{\delta}$  of integers. With this choice of  $a_{\delta}$, let N be defined as the set of all  $F_{\alpha}$  defined by Definition 1.

LEMMA 5. All statements in $\mathfrak{N}$ which are forced by some $P_{n}$ are true in $\mathfrak{N}$ and conversely.

Proof: Let $\mathfrak{a}$ be a limited statement with $r$ quantifiers. If $r > 0$, then if $P_{n}$ forces $(x)_{\alpha} \mathfrak{b}(x)$, if $\beta < \alpha$, then some $P_{m}$ must force $\mathfrak{b}(F_{\beta})$ since no $P_{m}$ can force $\neg \mathfrak{b}(F_{\beta})$. By induction we have that $\mathfrak{b}(F_{\beta})$ holds, so that $(x)_{\alpha} \mathfrak{b}(x)$ holds in $\mathfrak{N}$. If $P_{n}$ forces $\exists_{\alpha} x \mathfrak{b}(x)$, for some $\beta < \alpha$, $P_{n}$ forces $\mathfrak{b}(F_{\beta})$ so by induction $\mathfrak{b}(F_{\beta})$ holds and hence $\exists_{\alpha} x \mathfrak{b}(x)$ holds in $\mathfrak{N}$. Case II will clearly follow from case III and (i) and (ii) are trivial. If $\mathfrak{a}$ is $F_{\alpha} \in F_{\beta}$ or $\neg F_{\alpha} \in F_{\beta}$ in case (iii) then if $P_{n}$ forces $\mathfrak{a}, P_{n}$ forces precisely the statement which because of the definition of $F_{\beta}$ is equivalent to $\mathfrak{a}$. In case (iv) if $P_{n}$ forces $F_{\alpha} \in F_{\beta}$, for some $\beta' < \beta$, $N(\beta') = 9$, $P_{n}$ forces $F_{\beta'} = F_{\alpha}$, which therefore holds by induction in $\mathfrak{N}$. If $P_{n}$ forces $\neg F_{\alpha} \in F_{\beta}$, then for each $\beta' < \beta$, $N(\beta') = 9$, $F_{\alpha} = F_{\beta'}$ is not forced by any $P_{m}$ so some $P_{m}$ must force $F_{\alpha} \neq F_{\beta'}$ which proves $\neg F_{\alpha} \in F_{\beta}$ holds in $\mathfrak{N}$. Similarly for case (v) and for unlimited statements. Since every statement or its negation is forced eventually, the converse is also true.

Lemma 5 is the justification of the definition of forcing since we can now throw back questions about N to questions about forcing which can be formulated in M.

In the next paper, we shall prove that N is a model for Z-F in which part 3 of Theorem 1 holds.

\* The author is a fellow of the Alfred P. Sloan Foundation.

$^{1}$  Cohen, P. J., “A minimal model for set theory,” Bull. Amer. Math. Soc., 69, 537–540 (1963).

$^{2}$  Fraenkel, A., and Y. Bar-Hillel, Foundations of Set Theory (1958).

$^{3}$  Gödel, K., The Consistency of the Continuum Hypothesis (Princeton University Press, 1940).

$^{4}$  Shepherdson, J. C., “Inner models for set theory,” J. Symb. Logic, 17, 225–237 (1957).

$^{5}$  Sierpinski, W., “L’hypothèse généralisée du continu et l’axiome du choix,” Fund. Math., 341-5 (1947)

# A SPECIFIC COMPLEMENT-FIXING ANTIGEN PRESENT IN SV40 TUMOR AND TRANSFORMED CELLS

BY PAUL H. BLACK, WALLACE P. ROWE, HORACE C. TURNER, AND ROBERT J. HUEBNER

LABORATORY OF INFECTIOUS DISEASES, NATIONAL INSTITUTES OF HEALTH, BETHESDA, MARYLAND

Communicated October 4, 1963

Many experimental tumors, both carcinogen-induced $^{1}$ and virus-induced, $^{2-5}$ contain new cellular antigens, generally demonstrable by transplant rejection procedures. Huebner et al. $^{6}$ first demonstrated the presence of new, noninfectious, complement-fixing (CF) antigens clearly under viral genetic control, in adenovirus-induced tumors in hamsters and rats.

A new transplantation antigen(s) has been found in SV40-induced hamster tumors, $^{7-9}$ but it is not established whether its synthesis is under viral or host cell genetic control. This paper presents evidence for a new CF antigen in SV40 tumors and transformed tissue culture cells, formed from information contained within the viral genome. Preliminary results of these studies were presented by Huebner et al. $^{6}$

Materials and Methods.—The CF procedure was identical with that used by Huebner et al.; this is a Bengtson procedure done in microplates using overnight fixation at 4°C, with two exact units of complement. Tumor extracts consisted of 10% suspensions in Eagle's basal medium, clarified by centrifugation at 2500 rpm for 30 min, and stored at -60°C. The extracts were tested for antigens only if the undiluted extract was not anticomplementary (AC). The primary SV40-induced hamster tumors used in these studies are from experiments described in detail elsewhere. $^{10}$  Tumor extracts used as standard CF antigens were selected for having high titer reactivity with sera from tumorous hamsters.

Suspensions of both normal and transformed tissue culture cells of various species, $^{[11]}$ as well as tissue culture cells from a variety of hamster tumors, were prepared in the following manner. Cells grown in 32-oz Blake bottles were washed with phosphate-buffered saline (PBS) (pH 7.2), scraped off the glass with a rubber policeman, centrifuged at 150 g for 8 min, and resuspended in 9 volumes of PBS. These suspensions were stored at $-60^{\circ}C$ before use.

"Viral antigen" was prepared by inoculating SV40 strain 776$^{12}$ into a continuous tissue culture cell line (strain BSC-1) of African green monkey kidney (AGMK) at a multiplicity of about 10$^{-4}$, and harvesting the cells and fluid together when cytopathogenicity was maximal. The cell suspension was stored at -20°C, thawed, and used without further processing.$^{13}$

Four types of sera were used as standard reagents; to avoid undue heterogeneity of antibodies, sera of individual animals generally were used: (1) serum from tumorous hamsters, selected for having high CF antibody titer against SV40 tumor extracts, and no reaction with viral antigen; (2) serum from similar hamsters, but having high CF antibody titers for both tumor extracts and