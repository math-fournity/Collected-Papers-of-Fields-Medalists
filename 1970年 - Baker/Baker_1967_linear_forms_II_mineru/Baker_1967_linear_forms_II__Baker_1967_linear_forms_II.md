# LINEAR FORMS IN THE LOGARITHMS OF ALGEBRAIC NUMBERS (II)

## A. BAKER

1. Introduction. It was proved in a recent paper† that if $\alpha_{1},\ldots,\alpha_{n}$ denote nonzero algebraic numbers and if‡ log $\alpha_{1},\ldots,\log\alpha_{n}$ and $2\pi i$ are linearly independent over the rationals then log $\alpha_{1},\ldots,\log\alpha_{n}$ are linearly independent over the field of all algebraic numbers. Further it was shown that if $\alpha_{1},\ldots,\alpha_{n}$ are positive real algebraic numbers other than 1 and if $\beta_{1},\ldots,\beta_{n}$ denote real algebraic numbers with 1, $\beta_{1},\ldots,\beta_{n}$ linearly independent over the rationals then $\alpha_{1}^{\beta_{1}}\ldots\alpha_{n}^{\beta_{n}}$ is transcendental. In the present paper it will be proved that the number $2\pi i$ can be excluded from the hypotheses of the first result without invalidating the conclusion, and that the natural generalization of the second result holds, relating to both real and complex algebraic numbers. More precisely, the following theorems will be established.

THEOREM 1. If $\alpha_{1},\ldots,\alpha_{n}$ denote non-zero algebraic numbers then $\log\alpha_{1},\ldots,\log\alpha_{n}$ are linearly independent over the rationals if and only if they are linearly independent over the field of all algebraic numbers.

THEOREM 2. If $\alpha_{1},\ldots,\alpha_{n}$ denote algebraic numbers other than 0 or 1 and if $\beta_{1},\ldots,\beta_{n}$ denote algebraic numbers with 1, $\beta_{1},\ldots,\beta_{n}$ linearly independent over the rationals then $\alpha_{1}^{\beta_{1}}\ldots\alpha_{n}^{\beta_{n}}$ is transcendental.

Theorem 1 will be obtained as a special case of a more refined result (Theorem 3 below) analogous to the principal theorem proved in (I). Theorem 2 then follows as a direct deduction. Indeed it is clear that Theorem 1 implies the validity of Theorem 2 for $n = 1$ (this is in fact the Gelfond-Schneider Theorem), and the argument then proceeds as in (I) §5 by induction.

For ease of reference we shall retain the notation of (I) as far as possible. The height of an algebraic number is defined, as usual, to be the maximum of the absolute values of the relatively prime integer coefficients in its minimal defining polynomial. Let n denote an integer  $\geqslant 2$  and let  $\alpha_{1}, \ldots, \alpha_{n}$  denote non-zero algebraic numbers such that  $\log \alpha_{1}, \ldots, \log \alpha_{n}$  are linearly independent over the rationals. Further suppose that

$$
\kappa > 2 n + 1\tag{1}
$$

and let d be any positive integer. Our principal result is then as follows.

THEOREM 3. There is an effectively computable number

$$
C = C (n, \alpha_ {1}, \dots , \alpha_ {n}, \kappa , d) > 0
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$z^{w}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† A. Baker, “Linear forms in the logarithms of algebraic numbers”, Mathematika, 13 (1966), 204–216. The paper will be referred to as (I).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\ddagger$ For $\log z$ we take any fixed determination of the logarithm; and then $z^{w}$ means $e^{w\log z}$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\alpha_{1}, \ldots, \alpha_{m+1}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">In that argument equations involving $\alpha_{1},\ldots ,\alpha_{m + 1}$ are to be interpreted in terms of suitable determinations of the logarithms.</span></small>

such that for all algebraic numbers $\beta_{1},\ldots ,\beta_{n}$ , not all 0, with degrees at most $d$ , we have

$$
\left| \beta_ {1} \log \alpha_ {1} + \dots + \beta_ {n} \log \alpha_ {n} \right| > C e ^ {- (\log H) ^ {\kappa}}
$$

where $H$ denotes the maximum of the heights of $\beta_{1},\ldots ,\beta_{n}$.

It will be observed that the inequality  $\kappa > n + 1$  which occurs in (I) has been replaced by the more restrictive condition (1). The need for this restriction arises from the additional degree of complexity in the proof of the theorem due to the exclusion of  $2\pi i$  from the hypotheses. No doubt the condition could be relaxed to some extent by means of suitable refinements of the techniques employed here, but any such refinement would involve a substantial change in the basic structure of the argument and it seems best not to complicate the present exposition unduly.

The exclusion of  $2\pi i$  from the hypotheses of Theorem 3 is of particular importance in applications. The method of proof can now be used, for example, to obtain the first generally effective improvement on Liouville's Theorem, given in 1844, relating to the approximation of algebraic numbers by rationals. It is hoped to discuss this and other developments in detail later. $^{\dagger}$

2. Lemmas. We now give five lemmas preliminary to the proof of Theorem 3.

The numbers $n, \alpha_{1}, \ldots, \alpha_{n}, \kappa, d$ are defined as in §1 except that, following (I), we assume, without loss of generality, that $d$ is not less than the degrees of $\alpha_{1}, \ldots, \alpha_{n}$. By $c, c_{1}, c_{2}, \ldots$ we denote numbers, greater than 1, which depend only on $n, \alpha_{1}, \ldots, \alpha_{n}, \kappa, d$; $c$ will be supposed sufficiently large throughout.

We assume now that there exist algebraic numbers  $\beta_{1}, \ldots, \beta_{n-1}$  with degrees at most d such that

$$
\left| \beta_ {1} \log \alpha_ {1} + \dots + \beta_ {n - 1} \log \alpha_ {n - 1} - \log \alpha_ {n} \right| <   e ^ {- (\log H) ^ {\kappa}},\tag{2}
$$

where H denotes some number not less than c and the heights of  $\beta_{1}, \ldots, \beta_{n-1}$ , and ultimately we shall deduce a contradiction. The contradiction suffices [see (I), §2] to establish the theorem.

We define

$$
\zeta = \frac {1}{2} \{1 + \kappa / (2 n + 1) \}
$$

and we note that, by (1),

$$
1 <   \zeta <   \kappa / (2 n + 1).
$$

Further we define, as in (I),

$$
\varepsilon = (1 - 1 / \zeta) / (2 n), \quad h = [ \log H ], \quad k = [ h ^ {\zeta} ], \quad D = d ^ {2 n - 1},
$$

and we write

$$
f _ {m _ {1}, \ldots , m _ {n - 1}} (z _ {1}, \ldots , z _ {n - 1}) = \frac {\partial^ {m _ {1} + \ldots + m _ {n - 1}}}{\partial z _ {1} ^ {m _ {1}} \ldots \partial z _ {n - 1} ^ {m _ {n - 1}}} f (z _ {1}, \ldots , z _ {n - 1}).
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Of particular interest is the connexion, to which Prof. Ax has recently drawn my attention, between the natural p-adic analogue of Theorem 1 [or indeed the main result of (I)] and a well known problem of Leopoldt; see Ax's paper “On the units of an algebraic number field”, Illinois J. Math., 9(1965), 584–589; see also a paper by Brumer to appear in Mathematika.</span></small>

LEMMA 1. There are integers $p(\lambda_1, \ldots, \lambda_n)$, not all 0, with absolute values at most $e^{2hk}$, such that the function

$$
\Phi (z _ {1}, \dots , z _ {n - 1}) = \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) \alpha_ {1} ^ {\gamma_ {1} z _ {1}} \dots \alpha_ {n - 1} ^ {\gamma_ {n - 1} z _ {n - 1}},
$$

where $L = [k^{1 - \varepsilon}]$ and $\gamma_r = \lambda_r + \lambda_n\beta_r$$(1\leqslant r < n)$, satisfies

$$
\left| \Phi_ {m _ {1}, \dots , m _ {n - 1}} (l, \dots , l) \right| <   e ^ {- \frac {1}{2} h {\kappa}}\tag{3}
$$

for all integers $l$ with $1 \leqslant l \leqslant h$ and all non-negative integers $m_1, \ldots, m_{n-1}$ with $m_1 + \ldots + m_{n-1} \leqslant k$.

Proof. See (I), Lemma 2. The proof is unaffected by the change in the definition of $\zeta$.

LEMMA 2. For any non-negative integers $m_1, \ldots, m_{n-1}$ with

$$
m _ {1} + \dots + m _ {n - 1} \leqslant k
$$

and any complex number $z$ we have

$$
\left| \Phi_ {m _ {1}, \dots , m _ {n - 1}} (z, \dots , z) \right| \leqslant e ^ {4 h k} c _ {1} ^ {L | z |}.\tag{4}
$$

Proof. See (I), Lemma 3.

LEMMA 3. Let $J$ be any integer satisfying $0 \leqslant J < \tau$, where

$$
\tau = 2 \varepsilon^ {- 1} \{(\kappa - 1) \zeta^ {- 1} - 1 \} + 1.
$$

Then (3) holds for all integers $l$ with $1 \leqslant l \leqslant hk^{\frac{1}{2} \varepsilon J}$ and each set of non-negative integers $m_1, \ldots, m_{n-1}$ with $m_1 + \ldots + m_{n-1} \leqslant k / 2^J$.

Proof. See (I), Lemma 4.

LEMMA 4. For each integer $j$ with $0 \leqslant j \leqslant k^n$ we have

$$
\log | \phi_ {j} (0) | <   - h ^ {\kappa} / \log h,\tag{5}
$$

where

$$
\phi (z) = \Phi (z, \dots , z).
$$

Proof. We write

$$
X = [ \frac {1}{2} h ^ {\kappa - \zeta} ], \quad Y = [ k / (8 \kappa \log h) ].
$$

Then it is easily verified that $[hk^{\frac{1}{2}\varepsilon\sigma}] \geqslant X$ and $[k/2^{\sigma}] \geqslant Y$, where $\sigma$ denotes the largest integer $< \tau$, and so, by Lemma 3, we see that (3) holds for each integer $l$ with $1 \leqslant l \leqslant X$ and each set of non-negative integers $m_1, \ldots, m_{n-1}$ satisfying $m_1 + \ldots + m_{n-1} \leqslant Y$. Hence we have

$$
| \phi_ {m} (r) | <   n ^ {k} e ^ {- \frac {1}{2} h ^ {\kappa}}\tag{6}
$$

for each integer $r$ with $1 \leqslant r \leqslant X$ and each integer $m$ satisfying $0 \leqslant m \leqslant Y$ [cf. (I), the proof of Lemma 4]. Let $\Gamma$ and $\Lambda$ denote circles in the complex plane, described in the positive sense, with centres the origin and with radii $X \log h$ and $\frac{1}{4}$ respectively. Suppose further that $w$ is any complex number on $\Lambda$. We proceed to calculate an upper bound for $|\phi(w)|$.

We write, for brevity,

$$
E (z) = \{(z - 1) \dots (z - X) \} ^ {Y + 1}.
$$

By Cauchy's residue theorem we have

$$
\frac {1}{2 \pi i} \int_ {\Gamma} \frac {\phi (z)}{(z - w) E (z)} d z = \frac {\phi (w)}{E (w)} + \frac {1}{2 \pi i} \sum_ {r = 1} ^ {X} \sum_ {m = 0} ^ {Y} \frac {\phi_ {m} (r)}{m !} \int_ {\Gamma_ {r}} \frac {(z - r) ^ {m} d z}{(z - w) E (z)},\tag{7}
$$

where $\Gamma_r$ denotes the circle in the complex plane, described in the positive sense, with centre $r$ and radius $\frac{1}{2}$ [cf.(I), Lemma 4]. Since, for $z$ on $\Gamma_r$,

$$
\left| (z - r) ^ {m} / E (z) \right| <   8 ^ {Y + 1}
$$

it follows, on using (6), that the absolute value of the double sum on the right of (7) is at most

$$
X (Y + 1) 8 ^ {Y + 2} n ^ {k} e ^ {- \frac {1}{2} h ^ {\kappa}} <   (8 n) ^ {k + 2} h ^ {\kappa} e ^ {- \frac {1}{2} h ^ {\kappa}} <   e ^ {- \frac {1}{4} h ^ {\kappa}}.
$$

Now let $\xi$ and $\Xi$ denote respectively the upper bound of $|\phi(z)|$ and the lower bound of $|E(z)|$ with $z$ on $\Gamma$. From (7) we have

$$
| \phi (w) | \leqslant \{2 \xi \Xi^ {- 1} + e ^ {- \frac {1}{4} h ^ {\kappa}} \} | E (w) |.
$$

Now it is clear that

$$
| E (w) | \leqslant (X + 1) ^ {X (Y + 1)} \text {   and   } | \Xi | \geqslant (\frac {1}{2} X \log h) ^ {X (Y + 1)}.
$$

Further, by (4) of Lemma 2 we see that

$$
\xi \leqslant e ^ {4 h k} c _ {1} ^ {L X \log h}.
$$

Hence we obtain

$$
| \phi (w) | \leqslant 2 e ^ {4 h k} c _ {1} ^ {L X \log h} (\frac {1}{4} \log h) ^ {- X (Y + 1)} + (2 X) ^ {2 X Y} e ^ {- \frac {1}{4} h ^ {\kappa}}.
$$

Now

$$
2 X Y \log (2 X) \leqslant \{(\kappa - \zeta) / (8 \kappa) \} h ^ {\kappa} \leqslant \frac {1}{8} h ^ {\kappa},
$$

and so the second term on the right is at most $e^{-\frac{1}{8} h^{\kappa}}$. Further we have $L \leqslant h^{\zeta(1 - \varepsilon)}$ and

$$
X (Y + 1) \geqslant h ^ {\kappa} / (6 4 \kappa \log h).
$$

It follows easily that

$$
| \phi (w) | \leqslant (\log h) ^ {- \frac {1}{2} X (Y + 1)}.
$$

Let now $j$ be an integer satisfying $0 \leqslant j \leqslant k^n$. By Cauchy's residue theorem we have

$$
\frac {j !}{2 \pi i} \int_ {\Lambda} \frac {\phi (w)}{w ^ {j + 1}} d w = \phi_ {j} (0).
$$

Thus from the bound for  $|\phi(w)|$  deduced above we obtain

$$
| \phi_ {j} (0) | <   j! 4 ^ {j} (\log h) ^ {- \frac {1}{2} X (Y + 1)}.
$$

Clearly

$$
j! 4 ^ {j} \leqslant (4 j) ^ {j} \leqslant k ^ {k n + 1}
$$

and, since $\kappa > \zeta(2n + 1)$, we see that

$$
\frac {1}{2} X (Y + 1) \log \log h \geqslant (h ^ {\kappa} \log \log h) / (1 2 8 \kappa \log h) \geqslant 2 k ^ {n + 1} \log k.
$$

Hence we have

$$
| \phi_ {j} (0) | \leqslant (\log h) ^ {- \frac {1}{4} X (Y + 1)}
$$

and this implies (5).

LEMMA 5. Let $t_1, \ldots, t_n$ denote integers, not all 0, with absolute values at most $T$. Then

$$
\left| t _ {1} \log \alpha_ {1} + \dots + t _ {n} \log \alpha_ {n} \right| > c _ {2} ^ {- T}.
$$

Proof. Let  $a_{1}, \ldots, a_{n}$  denote the leading coefficients (supposed positive) in the minimal defining polynomials of  $\alpha_{1}, \ldots, \alpha_{n}$  respectively. Then

$$
\omega = a _ {1} ^ {t _ {1}} \dots a _ {n} ^ {t _ {n}} (\alpha_ {1} ^ {t _ {1}} \dots \alpha_ {n} ^ {t _ {n}} - 1)
$$

represents an algebraic integer with degree at most D. Further, any of its conjugates, obtained by substituting arbitrary conjugates for  $\alpha_{1}, \ldots, \alpha_{n}$ , has absolute value at most  $c_{3}^{T}$ . Since  $t_{1}, \ldots, t_{n}$  are not all 0 and  $\log\alpha_{1}, \ldots, \log\alpha_{n}$  are linearly independent over the rationals, either we have  $\omega \neq 0$  and so  $|Norm\omega| \geqslant 1$ , or

$$
t _ {1} \log \alpha_ {1} + \dots + t _ {n} \log \alpha_ {n}
$$

is a non-zero multiple of $2\pi i$. In the latter case the lemma is obviously valid. In the former case we obtain

$$
| \omega | \geqslant c _ {3} ^ {- (D - 1) T}.
$$

But since

$$
\left| \left(a _ {1} \alpha_ {1}\right) ^ {t _ {1}} \dots \left(a _ {n} \alpha_ {n}\right) ^ {t _ {n}} \right| \leqslant c _ {4} ^ {T},
$$

and, for any complex number $z$, with $|z| < \frac{1}{2}$,

$$
\left| e ^ {z} - 1 \right| \leqslant 2 | z |,
$$

we see that

$$
| \omega | \leqslant 4 \left| t _ {1} \log \alpha_ {1} + \dots + t _ {n} \log \alpha_ {n} \right| c _ {4} ^ {T},
$$

and this gives the required result.

3. Proof of Theorem 3. We proceed to verify that the inequalities (5) cannot all be valid. This will suffice to establish the theorem.

We write, for brevity, $R = (L + 1)^n - 1$. Any integer $r$ with $0 \leqslant r \leqslant R$ can be expressed uniquely in the form

$$
r = \lambda_ {1} + \lambda_ {2} (L + 1) + \dots + \lambda_ {n} (L + 1) ^ {n - 1},
$$

where $\lambda_1, \ldots, \lambda_n$ denote integers between 0 and $L$ inclusive. For each such $r$ we define

$$
p _ {r} = p \left(\lambda_ {1}, \dots , \lambda_ {n}\right) \text {   and   } \psi_ {r} = \lambda_ {1} \log \alpha_ {1} + \dots + \lambda_ {n} \log \alpha_ {n}.
$$

Further we write

$$
\Psi_ {j} = \sum_ {r = 0} ^ {R} p _ {r} \psi_ {r} ^ {j} (0 \leqslant j \leqslant R).
$$

Now we have

$$
\phi_ {j} (0) = \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) (\gamma_ {1} \log \alpha_ {1} + \dots + \gamma_ {n - 1} \log \alpha_ {n - 1}) ^ {j},
$$

and, noting that $|\psi_r| < c_5 L$ and $j \leqslant R$, we obtain from (2)

$$
\left| \left(\gamma_ {1} \log \alpha_ {1} + \dots + \gamma_ {n - 1} \log \alpha_ {n - 1}\right) ^ {j} - \psi_ {r} ^ {j} \right| <   (c _ {6} L) ^ {R} e ^ {- h ^ {\kappa}}.
$$

Hence

$$
\left| \phi_ {j} (0) - \Psi_ {j} \right| \leqslant (R + 1) e ^ {2 h k} \left(c _ {6} L\right) ^ {R} e ^ {- h \kappa}.
$$

Since $L \leqslant h^{\zeta(1 - \varepsilon)}$, $R \leqslant h^{n\zeta}$ and $\kappa > \zeta(2n + 1)$, the number on the right is at most $e^{-\frac{1}{2}h\kappa}$. Thus it follows from (5), which is applicable since $j \leqslant R \leqslant k^n$, that

$$
\log | \Psi_ {j} | <   - \frac {1}{2} h ^ {\kappa} / \log h.\tag{8}
$$

Now let  $\Delta$  denote the Vandermonde determinant of order  $(L+1)^{n}$  with  $\psi_{r}^{j}$  in the  $(r+1)$ -th row and  $(j+1)$ -th column. We clearly have

$$
\Delta = \prod_ {0 \leqslant r <   s \leqslant R} (\psi_ {s} - \psi_ {r}).
$$

Since $\log \alpha_{1},\ldots ,\log \alpha_{n}$ are linearly independent over the rationals we see that $\psi_r\neq \psi_s$ for each pair $r,s(r\neq s)$ and since also $\lambda_1,\dots ,\lambda_n$ do not exceed $L$, it follows from Lemma 5 that

$$
\left| \psi_ {s} - \psi_ {r} \right| > c _ {2} ^ {- L}.
$$

The number of pairs $r, s$ with $0 \leqslant r < s \leqslant R$ is at most $(L + 1)^{2n}$ and, noting that $L + 1 \leqslant k$, we obtain

$$
\log | \Delta | \geqslant - c _ {7} k ^ {2 n + 1} \geqslant - c _ {8} h ^ {\zeta (2 n + 1)}.
$$

On the other hand, one at least of the  $p_{r}$  is not 0 and, without loss of generality, we can suppose that  $p_{0} \neq 0$ . By a linear combination of rows we have

$$
\Delta = p _ {0} ^ {- 1} \left| \begin{array}{c c c c} \Psi_ {0} & \Psi_ {1} & \ldots & \Psi_ {R} \\ 1 & \psi_ {1} & \ldots & \psi_ {1} ^ {R} \\ & \ldots & & \\ 1 & \psi_ {R} & \ldots & \psi_ {R} ^ {R} \end{array} \right|.
$$

Hence, using (8) to estimate the elements in the first row and the trivial inequality $|\psi_j| < c_9 k$ to estimate the remaining elements, we deduce that

$$
\log | \Delta | \leqslant \log ((R + 1)!) + R ^ {2} \log (c _ {9} k) - \frac {1}{2} h ^ {\kappa} / \log h.
$$

Now $R^2 \leqslant k^{2n}$ and $(R + 1)! \leqslant k^{nk^n}$. Further we have $k \leqslant h^\zeta$ and $\kappa > \zeta(2n + 1)$. Thus

$$
\log | \Delta | \leqslant - \frac {1}{4} h ^ {\kappa} / \log h
$$

if h is sufficiently large. But this contradicts the lower bound for  $\log |\Delta|$  obtained above, and the contradiction proves the theorem.

Trinity College,

Cambridge.