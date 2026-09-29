# LINEAR FORMS IN THE LOGARITHMS OF ALGEBRAIC NUMBERS

## A. BAKER

1. Introduction. In 1934 Gelfond [2] and Schneider [6] proved, independently, that the logarithm of an algebraic number to an algebraic base, other than 0 or 1, is either rational or transcendental and thereby solved the famous seventh problem of Hilbert. Among the many subsequent developments (cf. [4, 7, 8]), Gelfond [3] obtained, by means of a refinement of the method of proof, a positive lower bound for the absolute value of $\beta_{1} \log \alpha_{1} + \beta_{2} \log \alpha_{2}$, where $\beta_{1}, \beta_{2}$ denote algebraic numbers, not both 0, and $\alpha_{1}, \alpha_{2}$ denote algebraic numbers not 0 or 1, with $\log \alpha_{1}/\log \alpha_{2}$ irrational. Of particular interest is the special case in which $\beta_{1}, \beta_{2}$ denote integers. In this case it is easy to obtain a trivial positive lower bound (cf. [1; Lemma 2]), and the existence of a non-trivial bound follows from the Thue-Siegel-Roth theorem (see [4; Ch. I]). But Gelfond's result improves substantially on the former, and, unlike the latter, it is derived by an effective method of proof. Gelfond [4; p. 177] remarked that an analogous theorem for linear forms in arbitrarily many logarithms of algebraic numbers would be of great value for the solution of some apparently very difficult problems of number theory. It is the object of this paper to establish such a result.

We define, as usual, the height of an algebraic number to be the maximum of the absolute values of the relatively prime integer coefficients in its minimal defining polynomial. Let $n$ denote an integer $\geqslant 2$ and let $\alpha_1, \ldots, \alpha_n$ denote algebraic numbers, not 0 or 1, such that $\dagger \log \alpha_1, \ldots, \log \alpha_n$ and $\ddagger 2\pi i$ are linearly independent over the rationals. Further suppose that

$$
\kappa > n + 1\tag{1}
$$

and let d be any positive integer. We shall prove the following theorem.

THEOREM. There is an effectively computable number

$$
C = C (n, \alpha_ {1}, \dots , \alpha_ {n}, \kappa , d) > 0
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† For log z we take any fixed determination of the logarithm; and then  $z^{w}$  means  $e^{w \log z}$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$z^{\prime \prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\alpha_{n}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\alpha_{1},\ldots,$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">‡ A similar theorem holds if  $2\pi i$  is excluded and we merely postulate that  $\log \alpha_{1}, \ldots, \log \alpha_{n}$  are linearly independent over the rationals, but the proof is more complicated.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\kappa > 2$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">§ The precise rôle played by this inequality will be apparent later. The number  $n+1$  arises naturally from the argument, but it is not to be regarded as best possible; indeed it is known that  $\kappa>2$  suffices when n=2.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">n = 2.</span></small>

such that for all algebraic numbers $\beta_{1},\ldots ,\beta_{n}$, not all 0, with degrees at most $d$, we have

$$
\left| \beta_ {1} \log \alpha_ {1} + \dots + \beta_ {n} \log \alpha_ {n} \right| > C e ^ {- (\log H) ^ {\kappa}},\tag{2}
$$

where $H$ denotes the maximum of the heights of $\beta_{1},\ldots ,\beta_{n}$

The inequality (2) implies, in particular, that the number on the left is not 0. This immediately gives the first of the following corollaries, and we obtain the second as a direct deduction (see §5).

COROLLARY 1. If $\alpha_{1},\ldots,\alpha_{n}$ denote non-zero algebraic numbers and $\log\alpha_{1},\ldots,\log\alpha_{n}$ and $2\pi i$ are linearly independent over the rationals then $\log\alpha_{1},\ldots,\log\alpha_{n}$ are linearly independent over the field of all algebraic numbers.

COROLLARY 2. If $\alpha_{1},\ldots,\alpha_{n}$ denote positive real algebraic numbers other than 1 and $\beta_{1},\ldots,\beta_{n}$ denote real algebraic numbers with 1, $\beta_{1},\ldots,\beta_{n}$ linearly independent over the rationals then $\alpha_{1}^{\beta_{1}}\ldots\alpha_{n}^{\beta_{n}}$ is transcendental.

The detailed discussion of other applications of the theorem will be deferred to later papers. It is well known, however, that the theorem can be employed to give explicit upper bounds for the size of all the solutions of Diophantine equations of the type $f(x,y) = 1$, where $f$ denotes any irreducible binary form with integer coefficients and degree at least 3 (see [4; p. 176]). Furthermore it follows from work of Gelfond and Linnik [5] that the theorem suffices, at least in principle, to settle the celebrated conjecture, dating back to Gauss (cf. Disquisitiones Arithmeticae §303), that there are only nine imaginary quadratic fields with class number 1.$\dagger$

Finally, as regards the proof of the theorem, our method depends on the construction of an auxiliary function of several complex variables which would seem to be the natural generalisation of the function of a single variable used in Gelfond's original work. The subsequent treatment employed by Gelfond, however, is not applicable in the more general context and so it has been necessary to devise a new technique. Nevertheless it will be appreciated that the argument involves many familiar ideas. The method will probably be capable of considerable development for it applies in principle to many other auxiliary functions apart from the one constructed here.

The author is grateful to Prof. H. Davenport, who read the original draft of this paper, for his helpful criticism.

2. Preliminary simplification. It will be apparent from the nature of the proof that the number c specified in the theorem is effectively computable and no further reference will be made to this fact. The purpose of the present section is to show that it suffices to establish the following modified form of the theorem, which relates to only n-1 numbers  $\beta_{1}, \ldots, \beta_{n-1}$ .

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Added in proof. I understand that Dr. H. Stark of the University of Michigan has recently proved this conjecture by a different method.</span></small>

Assume the hypotheses of the theorem. Then there is a number $c > 0$ such that for all algebraic numbers $\beta_{1}, \ldots, \beta_{n-1}$ with degrees at most $d$ we have

$$
\left| \beta_ {1} \log \alpha_ {1} + \dots + \beta_ {n - 1} \log \alpha_ {n - 1} - \log \alpha_ {n} \right| \geqslant e ^ {- (\log H) ^ {\kappa}},
$$

where $H$ denotes any number not less than $c$ and the heights of $\beta_{1},\ldots,\beta_{n-1}$.

We proceed to prove that this implies the assertion of the theorem. First we note that if  $\alpha$  is an algebraic number with degree d and height H then  $|\alpha| \leqslant dH$ . For if  $\alpha$  satisfies an equation of the form

$$
a _ {0} \alpha^ {d} + a _ {1} \alpha^ {d - 1} + \ldots + a _ {d} = 0,
$$

where the $a_{j}$ denote integers with absolute values at most $H$ and $a_0 \geqslant 1$, then either $|\alpha| < 1$ or

$$
\left| \alpha \right| \leqslant \left| a _ {0} \alpha \right| = \left| a _ {1} + a _ {2} \alpha^ {- 1} + \dots + a _ {d} \alpha^ {- d + 1} \right| \leqslant d H.
$$

We observe also that for each non-negative integer j we have

$$
(a _ {0} \alpha) ^ {j} = a _ {0} ^ {(j)} + a _ {1} ^ {(j)} \alpha + \ldots + a _ {d - 1} ^ {(j)} \alpha^ {d - 1},
$$

where the integers  $a_{m}^{(j)}$  have absolute values at most  $(2H)^{j}$ ; this follows easily from the recurrence relations

$$
a _ {m} ^ {(j)} = a _ {0} a _ {m - 1} ^ {(j - 1)} - a _ {d - 1} ^ {(j - 1)} a _ {d - m}, \quad (0 \leqslant m <   d, j \geqslant d)
$$

where  $a_{-1}^{(j-1)}=0.\dagger$  Further we note that, if  $\alpha,\beta$  are algebraic numbers with degrees at most d and heights at most H, then  $\alpha\beta$  has degree at most  $d^{2}$  and height at most  $H'$, where  $\log H'/\log H$  is bounded above by a number depending only on d. For let a,b denote the leading coefficients in the minimal defining polynomials of  $\alpha,\beta$  and let  $\alpha^{(i)},\beta^{(j)}$  denote their respective conjugates. Then  $\alpha\beta$  is a root of the polynomial

$$
(a b) ^ {d ^ {2}} \prod_ {i, j} (x - \alpha^ {(i)} \beta^ {(j)})
$$

which clearly has integer coefficients‡ and degree at most  $d^{2}$ . The roots of the minimal polynomial of  $\alpha\beta$  are thus given by some subset of the  $\alpha^{(i)}\beta^{(j)}$ , and the leading coefficient divides  $(ab)^{d^{2}}$ . The assertion now follows from the fact that the  $\alpha^{(i)},\beta^{(j)}$  have absolute values at most dH.

We suppose now that $\beta_{1},\ldots,\beta_{n}$ denote algebraic numbers, not all 0, with degrees at most $d$, and we proceed to prove the validity of (2) for some $C>0$. Without loss of generality we can assume that $\beta_{n}\neq0$. We write $\beta_{r}^{\prime}=-\beta_{r}/\beta_{n}$ ($1\leqslant r<n$) and we denote by $H$ and $H^{\prime}$ the maximum of the heights of $\beta_{1},\ldots,\beta_{n}$ and $\beta_{1}^{\prime},\ldots,\beta_{n-1}^{\prime}$ respectively. Now $\beta_{1}^{\prime},\ldots,\beta_{n-1}^{\prime}$ have

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$d^{2}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† The result will not be needed until the next section, but it is convenient to record it here.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">‡ The same is true, though it is not quite so obvious, if the exponent $d^2$ of $ab$ is replaced by $d$.</span></small>

degrees at most  $d^{2}$  and  $\log H^{\prime}/\log H$  is bounded above by a number depending only on d. Further, on writing  $\kappa^{\prime}=\frac{1}{2}(\kappa+n+1)$ , so that  $\kappa>\kappa^{\prime}>n+1$ , we deduce from the modified result enunciated above that

$$
\left| \beta_ {1} ^ {\prime} \log \alpha_ {1} + \dots + \beta_ {n - 1} ^ {\prime} \log \alpha_ {n - 1} - \log \alpha_ {n} \right| > e ^ {- (\log H ^ {\prime \prime}) ^ {\kappa^ {\prime}}},
$$

where  $H''$  denotes the greater of  $H'$  and some positive number depending only on  $n, \alpha_{1}, \ldots, \alpha_{n}, \kappa, d$ . Since  $|\beta_{n}| \geqslant (dH)^{-1}$ , it follows that the number on the left of (2) exceeds  $(dH)^{-1} e^{-(\log H'')^{\kappa'}}$ , and this is certainly greater than  $Ce^{-(\log H)^{\kappa}}$  for a suitable C. The assertion is thus proved.

3. Lemmas. This section establishes four lemmas preliminary to the proof of the theorem.

We use the following notation. The numbers $n, \alpha_1, \ldots, \alpha_n, \kappa, d$ are defined as in §1, except that it will be assumed that $d$ is not less than the degrees of $\alpha_1, \ldots, \alpha_n$; this will involve no loss of generality. By $c, c_1, c_2, \ldots$ we denote numbers, greater than 1, which depend only on $n, \alpha_1, \ldots, \alpha_n, \kappa, d$. The number $c$, which will finally represent the constant specified in the modified form of the theorem given in §2, will be supposed sufficiently large throughout.

We assume that the modified form of the theorem is not valid and we shall ultimately deduce a contradiction. Thus we assume that there exist algebraic numbers  $\beta_{1}, \ldots, \beta_{n-1}$  with degrees at most d such that

$$
\left| \beta_ {1} \log \alpha_ {1} + \dots + \beta_ {n - 1} \log \alpha_ {n - 1} - \log \alpha_ {n} \right| <   e ^ {- (\log H) ^ {\kappa}},\tag{3}
$$

where H denotes some number not less than c and the heights of  $\beta_{1}, \ldots, \beta_{n-1}$ . Since, for any complex number z,

$$
\left| e ^ {z} - 1 \right| \leqslant | z | e ^ {| z |},
$$

we obtain from (3)

$$
\left| \alpha_ {1} ^ {\beta_ {1}} \dots \alpha_ {n - 1} ^ {\beta_ {n - 1}} - \alpha_ {n} \right| <   \left| \alpha_ {n} \right| e ^ {- (\log H) ^ {\kappa} + 1}.\tag{4}
$$

We write, for brevity,

$$
\zeta = \frac {1}{2} \{1 + \kappa / (n + 1) \}, \quad \epsilon = (1 - 1 / \zeta) / (2 n).\tag{5}
$$

Then from (1) we have

$$
1 <   \zeta <   \kappa / (n + 1) \text {   and   } 0 <   \epsilon <   1 / (2 n).
$$

We define

$$
h = [ \log H ], \quad k = [ h ^ {\zeta} ],
$$

where, as usual, $[x]$ denotes the integral part of $x$. We write also $D = d^{2n - 1}$.

Finally, for any integral function $f(z_{1}, \ldots, z_{n-1})$ of the complex variables $z_{1}, \ldots, z_{n-1}$ and any non-negative integers $m_{1}, \ldots, m_{n-1}$ we put

$$
f _ {m _ {1}, \dots , m _ {n - 1}} (z _ {1}, \dots , z _ {n - 1}) = \frac {\partial^ {m _ {1} + \dots + m _ {n - 1}}}{\partial z _ {1} ^ {m _ {1}} \dots \partial z _ {n - 1} ^ {m _ {n - 1}}} f (z _ {1}, \dots , z _ {n - 1}).
$$

LEMMA 1. Let $M, N$ denote integers with $N > M > 0$ and let $u_{ij} (1 \leqslant i \leqslant M, 1 \leqslant j \leqslant N)$ denote integers with absolute values at most $U$. Then there exist integers $x_1, \ldots, x_N$, not all 0, with absolute values at most $(NU)^{M/(N-M)}$ such that

$$
\sum_ {j = 1} ^ {N} u _ {i j} x _ {j} = 0 \quad (1 \leqslant i \leqslant M).\tag{6}
$$

Proof. The lemma is well known, but to avoid reference to external results we give the following proof.

We put $B = [(NU)^{M / (N - M)}]$ and note that there are $(B + 1)^N$ different sets of integers $x_1, \ldots, x_N$ with $0 \leqslant x_j \leqslant B$ ($1 \leqslant j \leqslant N$). For each such set we have

$$
- V _ {i} B \leqslant y _ {i} \leqslant W _ {i} B \quad (1 \leqslant i \leqslant M)
$$

where  $y_{i}$  denotes the left-hand side of (6), and  $-V_{i}$ ,  $W_{i}$  denote the sum of the negative and positive  $u_{ij}$  ( $1 \leqslant j \leqslant N$ ) respectively. Since  $V_{i} + W_{i} \leqslant NU$  there are at most  $(NUB + 1)^{M}$  different sets  $y_{1}, \ldots, y_{M}$ . Now

$$
(B + 1) ^ {N - M} > (N U) ^ {M}
$$

and so  $(B+1)^{N}>(NUB+1)^{M}$ . Hence there are two distinct sets  $x_{1},\ldots,x_{N}$  which correspond to the same set  $y_{1},\ldots,y_{M}$ , and their difference gives the required solution of (6).

LEMMA 2. There are integers $p(\lambda_1, \ldots, \lambda_n)$, not all 0, with absolute values at most $e^{2hk}$, such that the function

$$
\Phi (z _ {1}, \dots , z _ {n - 1}) = \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) \alpha_ {1} ^ {\gamma_ {1} z _ {1}} \dots \alpha_ {n - 1} ^ {\gamma_ {n - 1} z _ {n - 1}},
$$

where $L = [k^{1 - \epsilon}]$ and $\gamma_r = \lambda_r + \lambda_n\beta_r$$(1\leqslant r < n)$, satisfies

$$
\left| \Phi_ {m _ {1}, \dots , m _ {n - 1}} (l, \dots , l) \right| <   e ^ {- \frac {1}{2} h ^ {\kappa}}\tag{7}
$$

for all integers $l$ with $1 \leqslant l \leqslant h$ and all non-negative integers $m_1, \ldots, m_{n-1}$ with $m_1 + \ldots + m_{n-1} \leqslant k$.

Proof. We shall determine the $p(\lambda_1, \ldots, \lambda_n)$ such that

$$
\sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) \alpha_ {1} ^ {\lambda_ {1} l} \dots \alpha_ {n} ^ {\lambda_ {n} l} \gamma_ {1} ^ {m _ {1}} \dots \gamma_ {n - 1} ^ {m _ {n - 1}} = 0\tag{8}
$$

for the above ranges of $l$ and $m_1, \ldots, m_{n-1}$, and we shall verify subsequently that (8) implies (7). Let $a_1, \ldots, a_n, b_1, \ldots, b_{n-1}$ denote the leading coefficients (supposed positive) in the minimal defining polynomials of $\alpha_1, \ldots, \alpha_n, \beta_1, \ldots, \beta_{n-1}$ respectively. Then $a_1\alpha_1, \ldots, a_n\alpha_n, b_1\beta_1, \ldots, b_{n-1}\beta_{n-1}$ represent algebraic integers and $b_1, \ldots, b_{n-1}$ do not exceed $H$. Now for any non-negative integer $j$ we have

$$
(a _ {r} \alpha_ {r}) ^ {j} = \sum_ {s = 0} ^ {d - 1} a _ {r s} ^ {(j)} \alpha_ {r} ^ {s}, (b _ {r} \beta_ {r}) ^ {j} = \sum_ {t = 0} ^ {d - 1} b _ {r t} ^ {(j)} \beta_ {r} ^ {t},\tag{9}
$$

where the $a_{rs}^{(j)}$, $b_{rt}^{(j)}$ denote rational integers with absolute values at most $c_1^j$ and $(2H)^j$ respectively (see §2). Thus multiplying (8) by

$$
(a _ {1} \dots a _ {n}) ^ {L l} b _ {1} ^ {m _ {1}} \dots b _ {n - 1} ^ {m _ {n - 1}},
$$

writing

$$
\gamma_ {r} ^ {m _ {r}} = \sum_ {\mu_ {r} = 0} ^ {m _ {r}} \binom{m _ {r}}{\mu_ {r}} \lambda_ {r} ^ {m _ {r} - \mu_ {r}} (\lambda_ {n} \beta_ {r}) ^ {\mu_ {r}}
$$

and substituting from (9) for the powers of  $a_{r}\alpha_{r}$  and  $b_{r}\beta_{r}$  which result, we obtain the equation

$$
\sum_ {s _ {1} = 0} ^ {d - 1} \dots \sum_ {s _ {n} = 0} ^ {d - 1} \sum_ {t _ {1} = 0} ^ {d - 1} \dots \sum_ {t _ {n - 1} = 0} ^ {d - 1} A (s, t) \alpha_ {1} ^ {s _ {1}} \dots \alpha_ {n} ^ {s _ {n}} \beta_ {1} ^ {t _ {1}} \dots \beta_ {n - 1} ^ {t _ {n - 1}} = 0,
$$

where

$$
A (s, t) = \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} \sum_ {\mu_ {1} = 0} ^ {m _ {1}} \dots \sum_ {\mu_ {n - 1} = 0} ^ {m _ {n - 1}} p (\lambda_ {1}, \dots , \lambda_ {n}) v (\lambda) w (\lambda , \mu)
$$

and

$$
v (\lambda) = \prod_ {r = 1} ^ {n} \left\{a _ {r} ^ {(L - \lambda_ {r}) l} a _ {r, s _ {r}} ^ {(\lambda_ {r} l)} \right\},
$$

$$
w (\lambda , \mu) = \prod_ {r = 1} ^ {n - 1} \left\{\binom{m _ {r}}{\mu_ {r}} (b _ {r} \lambda_ {r}) ^ {m _ {r} - \mu_ {r}} \lambda_ {n} ^ {\mu_ {r}} b _ {r, t _ {r}} ^ {(\mu_ {r})} \right\}.
$$

Thus (8) will be satisfied if the D equations  $A(s, t)=0$  hold. Now these represent linear equations in the  $p(\lambda_{1}, \ldots, \lambda_{n})$  with integer coefficients. Further, since

$$
l \leqslant h, \quad m _ {1} + \ldots + m _ {n - 1} \leqslant k \text {and} \binom{m _ {r}}{\mu_ {r}} \leqslant 2 ^ {m _ {r}},
$$

we have

$$
\left| v (\lambda) \right| \leqslant \prod_ {r = 1} ^ {n} \left\{a _ {r} ^ {(L - \lambda_ {r}) l} c _ {1} ^ {\lambda_ {r} l} \right\} \leqslant c _ {2} ^ {L h},
$$

$$
\left| w (\lambda , \mu) \right| \leqslant \prod_ {r = 1} ^ {n - 1} (4 H L) ^ {m _ {r}} \leqslant (4 H L) ^ {k}.
$$

Hence the coefficient of $p(\lambda_1, \ldots, \lambda_n)$ in the linear form $A(s, t)$, namely

$$
\sum_ {\mu_ {1} = 0} ^ {m _ {1}} \dots \sum_ {\mu_ {n - 1} = 0} ^ {m _ {n - 1}} v (\lambda) w (\lambda , \mu),
$$

has absolute value at most $U = c_{2}^{L\mathbf{h}}(8HL)^{k}$; for clearly

$$
(m _ {1} + 1) \dots (m _ {n - 1} + 1) \leqslant 2 ^ {m _ {1} + \dots + m _ {n - 1}} \leqslant 2 ^ {k}.
$$

Now there are at most $(k + 1)^{n - 1}h$ distinct sets of integers $l, m_1, \ldots, m_{n - 1}$ and hence $M \leqslant D(k + 1)^{n - 1}h$ equations $A(s,t) = 0$ corresponding to them. Further, there are $N = (L + 1)^n$ unknowns $p(\lambda_1,\dots,\lambda_n)$ and $N > k^{n - n\epsilon} > 2M$ since $k > \frac{1}{2} h^{\zeta}$ and, by (5), $n\epsilon < 1 - 1 / \zeta$. It follows from Lemma 1 that the system of equations $A(s,t) = 0$ can be solved non-trivially and indeed the

integers $p(\lambda_1, \ldots, \lambda_n)$ can be chosen to have absolute values at most $NU$. Since $L \leqslant k^{1 - \epsilon}$, $\log H < \frac{3}{2} h$ and $k \leqslant h^\zeta$ we have

$$
N U \leqslant k ^ {n} c _ {2} ^ {L h} (8 k e ^ {(3 / 2) h}) ^ {k} \leqslant e ^ {2 h k}
$$

if $h$ is sufficiently large, as required.

It remains only to verify that (8) implies (7). Now it is clear that the left-hand side of (8) is obtained from $\Phi_{m_1,\ldots,m_{n-1}}(l,\ldots,l)$, apart from a factor $(\log \alpha_1)^{m_1}\ldots (\log \alpha_{n-1})^{m_n - 1}$ in the latter, by substituting $\alpha_{n}$ for $\alpha_{1}^{\beta_{1}}\ldots \alpha_{n-1}^{\beta_{n-1}}$. From (4) we deduce that

$$
\left| \left(\alpha_ {1} ^ {\beta_ {1}} \dots \alpha_ {n - 1} ^ {\beta_ {n - 1}}\right) ^ {\lambda_ {n} l} - \alpha_ {n} ^ {\lambda_ {n} l} \right| \leqslant c _ {3} ^ {L l} e ^ {- (\log H) ^ {\kappa}} \leqslant c _ {3} ^ {L h} e ^ {- h ^ {\kappa}}.
$$

Further, since $|\beta_r| \leqslant dH$, we have $|\gamma_r| \leqslant 2dLH$ and so

$$
\left| \left(\log \alpha_ {1}\right) ^ {m _ {1}} \dots \left(\log \alpha_ {n - 1}\right) ^ {m _ {n - 1}} \alpha_ {1} ^ {\lambda_ {1} l} \dots \alpha_ {n - 1} ^ {\lambda_ {n - 1} l} \gamma_ {1} ^ {m _ {1}} \dots \gamma_ {n - 1} ^ {m _ {n - 1}} \right| \leqslant c _ {4} ^ {k + L l} (2 d L H) ^ {k} <   e ^ {2 h k}.
$$

Thus we obtain

$$
\left| \Phi_ {m _ {1}, \dots , m _ {n - 1}} (l, \dots , l) \right| \leqslant (L + 1) ^ {n} e ^ {4 h k} c _ {3} ^ {L h} e ^ {- h ^ {\kappa}}
$$

and (7) follows since $L \leqslant k$, $Lh \leqslant hk \leqslant h^{1 + \zeta}$ and $\kappa > 1 + \zeta$. This completes the proof of the lemma.

LEMMA 3. For any non-negative integers $m_1, \ldots, m_{n-1}$ with

$$
m _ {1} + \dots + m _ {n - 1} \leqslant k
$$

and any complex number $z$ we have

$$
\left| \Phi_ {m _ {1}, \dots , m _ {n - 1}} (z, \dots , z) \right| \leqslant e ^ {4 h k} c _ {5} ^ {L | z |}.\tag{10}
$$

Further, for any integer $l$ with $0 < l \leqslant h^{\kappa - \zeta + \frac{1}{2}\epsilon \zeta}$, either (7) holds or

$$
\left| \Phi_ {m _ {1}, \dots , m _ {n - 1}} (l, \dots , l) \right| > (e ^ {6 h k} c _ {6} ^ {L l}) ^ {- D}.\tag{11}
$$

Proof. We have

$$
\Phi_ {m _ {1}, \dots , m _ {n - 1}} (z, \dots , z) = P \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) q (\lambda , z),
$$

where

$$
P = (\log \alpha_ {1}) ^ {m _ {1}} \dots (\log \alpha_ {n - 1}) ^ {m _ {n - 1}}, q (\lambda , z) = \alpha_ {1} ^ {\gamma_ {1} z} \dots \alpha_ {n - 1} ^ {\gamma_ {n - 1} z} \gamma_ {1} ^ {m _ {1}} \dots \gamma_ {n - 1} ^ {m _ {n - 1}}.
$$

Now (3) implies that

$$
\left| \alpha_ {1} ^ {\beta_ {1} z} \dots \alpha_ {n - 1} ^ {\beta_ {n - 1} z} \right| \leqslant e ^ {(| \log \alpha_ {n} | + 1) | z |}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$|x^{\lambda} - y^{\lambda}| = |x - y| |x^{\lambda - 1}y + \ldots + xy^{\lambda - 1}| \leqslant \lambda |x - y| (|y| + 1)^{\lambda}$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† If $x = \alpha_{1}^{\beta_{1}} \ldots \alpha_{n-1}^{\beta_{n-1}}$, $y = \alpha_{n}$, $\lambda = \lambda_{n} l$ then $|x| < |y| + 1$ and</span></small>

and since also $|\gamma_r| \leqslant 2dLH$, we obtain

$$
\mid P q (\lambda , z) \mid \leqslant \prod_ {r = 1} ^ {n - 1} \left\{c _ {7} ^ {L | z |} (2 c _ {8} d L H) ^ {m _ {r}} \right\} \leqslant c _ {5} ^ {L | z |} (2 c _ {8} d L H) ^ {k}.
$$

Thus the number on the left of (10) is at most

$$
(L + 1) ^ {n} e ^ {2 h k} c _ {5} ^ {L | z |} (2 c _ {8} d L H) ^ {k} \leqslant e ^ {4 h k} c _ {5} ^ {L | z |},
$$

as required.

To prove the second assertion we begin by defining

$$
Q = P ^ {\prime} \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) q ^ {\prime} (\lambda , l),
$$

where

$$
P ^ {\prime} = (a _ {1} \dots a _ {n}) ^ {L l} b _ {1} ^ {m _ {1}} \dots b _ {n - 1} ^ {m _ {n - 1}}, q ^ {\prime} (\lambda , l) = \alpha_ {1} ^ {\lambda_ {1} l} \dots \alpha_ {n} ^ {\lambda_ {n} l} \gamma_ {1} ^ {m _ {1}} \dots \gamma_ {n - 1} ^ {m _ {n - 1}}
$$

and the  $a_{r}, b_{r}$  are given as in the proof of Lemma 2. Then it is clear that Q represents an algebraic integer with degree at most D. Further, any conjugate of Q, obtained by substituting arbitrary conjugates for  $\alpha_{r}, \beta_{r}$ , has absolute value at most

$$
(L + 1) ^ {n} e ^ {2 h k} c _ {9} ^ {L l} (2 d L H) ^ {2 k} \leqslant e ^ {6 h k} c _ {9} ^ {L l}.
$$

If $Q \neq 0$ we have $|\operatorname{Norm} Q| \geqslant 1$ and hence

$$
\mid Q \mid \geqslant (e ^ {6 h k} c _ {9} ^ {L l}) ^ {- D + 1}.
$$

Now by (4) we see that (cf. the end of the proof of Lemma 2)

$$
\left| q (\lambda , l) - q ^ {\prime} (\lambda , l) \right| \leqslant c _ {1 0} ^ {L l} (2 d L H) ^ {k} e ^ {- h ^ {\kappa}}
$$

and, by virtue of the inequalities $L \leqslant h^{\zeta(1 - \epsilon)}$, $\kappa > 1 + \zeta$ and the supposition $l \leqslant h^{\kappa - \zeta + \frac{1}{2}\epsilon\zeta}$, the number on the right is at most $e^{-\frac{1}{2}h\kappa}$. Hence we deduce that

$$
\left| P ^ {- 1} \Phi_ {m _ {1}, \dots , m _ {n - 1}} (l, \dots , l) - P ^ {\prime - 1} Q \right| \leqslant (L + 1) ^ {n} e ^ {2 h k - \frac {3}{4} h ^ {\kappa}} <   e ^ {- \frac {5}{8} h ^ {\kappa}}.
$$

The second part of the lemma now follows on using the trivial inequalities

$$
\mid P / P ^ {\prime} \mid > c _ {1 1} ^ {- L l - k} H ^ {- k}, \quad \mid P \mid <   c _ {1 2} ^ {k},
$$

the asserted alternatives corresponding to the cases Q=0 or  $Q\neq0$ .

LEMMA 4. Let $J$ be any integer satisfying $0 \leqslant J < \tau$, where

$$
\tau = 2 \epsilon^ {- 1} \left\{\left(\kappa - 1\right) \zeta^ {- 1} - 1 \right\} + 1.\tag{12}
$$

Then (7) holds for all integers $l$ with $1 \leqslant l \leqslant hk^{\frac{1}{2} \epsilon J}$ and each set of non-negative integers $m_1, \ldots, m_{n-1}$ with $m_1 + \ldots + m_{n-1} \leqslant k / 2^J$.

Proof. The lemma is true for J=0 by Lemma 2. We suppose that K is an integer satisfying  $0 \leqslant K < \tau - 1$  and we assume that the lemma is true for  $J=0, 1, \ldots, K$ . We proceed to prove the validity of the lemma for  $J=K+1$ .

We begin by defining

$$
R _ {J} = [ h k ^ {\frac {1}{2} \epsilon J} ], \quad S _ {J} = [ k / 2 ^ {J} ] \quad (J = 0, 1, \dots).
$$

It suffices then to prove that for any integer $l$ with $R_K < l \leqslant R_{K+1}$ and any set of non-negative integers $m_1, \ldots, m_{n-1}$ with $m_1 + \ldots + m_{n-1} \leqslant S_{K+1}$ we have

$$
\mid f (l) \mid <   e ^ {- \frac {1}{2} h ^ {\kappa}},\tag{13}
$$

where

$$
f (z) = \Phi_ {m _ {1}, \dots , m _ {n - 1}} (z, \dots , z).
$$

By our inductive hypothesis we see that for each integer r with  $1 \leqslant r \leqslant R_{K}$  and each integer m satisfying  $0 \leqslant m \leqslant S_{K+1}$  we have

$$
\left| f _ {m} (r) \right| <   n ^ {k} e ^ {- \frac {1}{2} h ^ {\kappa}};\tag{14}
$$

for $f_{m}(r)$ is given by

$$
\left(\frac {\partial}{\partial z _ {1}} + \dots + \frac {\partial}{\partial z _ {n - 1}}\right) ^ {m} \Phi_ {m _ {1}, \dots , m _ {n - 1}} (z _ {1}, \dots , z _ {n - 1})
$$

evaluated at the point $z_{1} = \ldots = z_{n - 1} = r$, that is by

$$
\sum_{\substack{j_{1} = 0\\ j_{1} + \ldots +j_{n - 1} = m}}^{m}\dots \sum_{j_{n - 1} = 0}^{m}\frac{m!}{j_{1}!\cdots j_{n - 1}!}\Phi_{m_{1} + j_{1},\ldots ,m_{n - 1} + j_{n - 1}}(r,\ldots ,r),
$$

and the absolute values of the derivatives here are at most  $e^{-\frac{1}{2}h\kappa}$  since

$$
m _ {1} + \dots + m _ {n - 1} + j _ {1} + \dots + j _ {n - 1} \leqslant k / 2 ^ {K}.
$$

We write, for brevity,

$$
F (z) = \{(z - 1) \dots (z - R _ {K}) \} ^ {S _ {\mathbb {R} + 1} + 1}
$$

and we denote by $C$ the circle in the complex plane, described in the positive sense, with centre the origin and with radius $R_{K+1} \log h$. Then by Cauchy's residue theorem we have

$$
\frac {1}{2 \pi i} \int_ {C} \frac {f (z)}{(z - l) F (z)} d z = \frac {f (l)}{F (l)} + \frac {1}{2 \pi i} \sum_ {r = 1} ^ {R \pi} \sum_ {m = 0} ^ {S _ {K + 1}} \frac {f _ {m} (r)}{m !} \int_ {\Gamma_ {r}} \frac {(z - r) ^ {m} d z}{(z - l) F (z)},\tag{15}
$$

where  $\Gamma_{r}$  denotes the circle in the complex plane, described in the positive sense, with centre r and radius  $\frac{1}{2}$ ; for the residue of the pole of the integrand on the left at z=r is given by

$$
\frac {1}{S _ {K + 1} !} \frac {d ^ {S _ {K + 1}}}{d z ^ {S _ {K + 1}}} \left\{\frac {(z - r) ^ {S _ {K + 1} + 1} f (z)}{(z - l) F (z)} \right\}
$$

evaluated at $z=r$, and the integral over $\Gamma_{r}$ on the right is given by

$$
\frac {2 \pi i}{(S _ {K + 1} - m) !} \frac {d ^ {S _ {K + 1} - m}}{d z ^ {S _ {K + 1} - m}} \left\{\frac {(z - r) ^ {S _ {K + 1} + 1}}{(z - l) F (z)} \right\}
$$

again evaluated at $z = r$, and (15) now follows by Leibnitz's theorem. Since, for $z$ on $\Gamma_r$,

$$
\left| (z - r) ^ {m} / F (z) \right| \leqslant 8 ^ {S _ {K + 1} + 1},
$$

we deduce from (14) and the inequalities

$$
R _ {K} (S _ {K + 1} + 1) \leqslant h k ^ {\frac {1}{2} \epsilon (\tau - 1) + 1} \leqslant h ^ {\kappa},
$$

that the absolute value of the double sum on the right of (15) is at most

$$
R _ {K} (S _ {K + 1} + 1) 8 ^ {S _ {K + 1} + 1} n ^ {k} e ^ {- \frac {1}{2} h ^ {\kappa}} \leqslant h ^ {\kappa} (8 n) ^ {k} e ^ {- \frac {1}{2} h ^ {\kappa}} <   e ^ {- \frac {1}{4} h ^ {\kappa}}.
$$

Further it is clear that

$$
\left| F (l) \right| \leqslant l ^ {R _ {K} (S _ {K + 1} + 1)} \leqslant R _ {K + 1} ^ {R _ {K} (S _ {K + 1} + 1)}\tag{16}
$$

Also since, from (12),

$$
R _ {K + 1} \leqslant h k ^ {\frac {1}{2} \epsilon \tau} \leqslant h ^ {\kappa - \zeta + \frac {1}{2} \epsilon \zeta},\tag{17}
$$

the condition of Lemma 3 is satisfied, we see that either (13) holds or, by (11),

$$
\mid f (l) \mid > (e ^ {6 h k} c _ {6} ^ {L R _ {K + 1}}) ^ {- D}.\tag{18}
$$

We show that the assumption that (18) is valid leads to a contradiction. By (12), (16), (17), (18) and the inequalities

$$
R _ {K} \leqslant h k ^ {\frac {1}{2} \epsilon K}, \quad S _ {K + 1} + 1 \leqslant k \leqslant h ^ {\zeta}, \quad L \leqslant h ^ {\zeta (1 - \epsilon)},
$$

where $K < \tau - 1$, we have $\dagger$

$$
\left| F (l) \right| \leqslant e ^ {\frac {1}{4} h ^ {\kappa}}, \quad \left| f (l) \right| > 2 e ^ {- \frac {1}{4} h ^ {\kappa}}
$$

if $h$ is sufficiently large, and thus

$$
\left| f (l) / F (l) \right| > 2 e ^ {- \frac {1}{4} h ^ {\kappa}}.
$$

It follows that the right-hand side of (15) is at least  $\frac{1}{2}|f(l)/F(l)|$ . Now let  $\theta$  and  $\Theta$  denote respectively the upper bound of  $|f(z)|$  and the lower bound of  $|F(z)|$  with z on C. Since  $2|z-l|$  with z on C exceeds the radius of C, we obtain from (15)

$$
4 \theta | F (l) | > \Theta | f (l) |.
$$

It is clear that

$$
\Theta \geqslant (\frac {1}{2} R _ {K + 1} \log h) ^ {R _ {K} (S _ {K + 1} + 1)}\tag{19}
$$

and, by (10) of Lemma 3,

$$
\theta \leqslant e ^ {4 h k} c _ {5} ^ {L R _ {K + 1} \log h}.
$$

Thus from (16) we obtain

$$
\Theta | F (l) | ^ {- 1} \geqslant (\frac {1}{2} \log h) ^ {R _ {K} (S _ {K + 1} + 1)},
$$

and from (18)

$$
\theta \mid f (l) \mid^ {- 1} \leqslant (e ^ {6 h k} c _ {5} ^ {L R _ {K + 1} \log h}) ^ {D + 1}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$R_{\pmb{K}}(S_{\pmb{K} + 1} + 1)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† As regards the first of these inequalities note that $R_{K}(S_{K+1} + 1)$ is at most</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$-\frac{1}{2}\epsilon \text{ or } -\frac{1}{2}\epsilon (\tau - [\tau])$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$h k^{\frac{1}{2} \epsilon K + 1} = k^{\frac{1}{2} \epsilon (K + 1 - \tau)} (h k^{1 + \frac{1}{2} \epsilon (\tau - 1)}) \leqslant k^{\frac{1}{2} \epsilon (K + 1 - \tau)} h^{\kappa}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">τ-1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">and, since $K$ is an integer less than $\tau - 1$, the exponent of $k$ on the right does not exceed $-\frac{1}{2}\epsilon$ or $-\frac{1}{2}\epsilon (\tau - [\tau])$ according as $\tau$ is or is not an integer; thus, in either case, the exponent of $k$ is a negative number depending only on $n$ and $\kappa$.</span></small>

Hence (19) implies that

$$
\log 4 + (D + 1) \left\{6 h k + c _ {1 3} L R _ {K + 1} \log h \right\} \geqslant R _ {K} \left(S _ {K + 1} + 1\right) \left\{\log \log h - \log 2 \right\}.\tag{20}
$$

Now $LR_{K+1} \leqslant h^{\frac{1}{2}\epsilon\zeta(K-1)+1+\zeta}$ and, since $hk \leqslant h^{1+\zeta}$, it follows that the number on the left of (20) is at most

$$
c _ {1 4} h ^ {1 + \zeta} \text {   or   } c _ {1 4} h ^ {\frac {1}{2} \epsilon \zeta (K - 1) + 1 + \zeta} \log h
$$

according as $K = 0$ or $K > 0$. On the other hand we have

$$
R _ {K} (S _ {K + 1} + 1) \geqslant \frac {1}{2} h k ^ {\frac {1}{2} \epsilon K} (k / 2 ^ {K + 1})
$$

and, since $K + 1 < \tau$ and $k > \frac{1}{2} h^{\zeta}$, we see that the number on the right of (20) exceeds

$$
c _ {1 5} ^ {- 1} h ^ {\frac {1}{2} \epsilon \zeta K + 1 + \zeta} \log \log h.
$$

The contradiction implies the validity of (13) and the lemma follows by induction.

4. Proof of the Theorem. It is clear from Lemma 4, on taking J to be the largest integer less than  $\tau$ , that

$$
\left| \Phi (l, \dots , l) \right| <   e ^ {- \frac {1}{2} h ^ {\kappa}}\tag{21}
$$

for each integer $l$ satisfying $1 \leqslant l \leqslant \frac{1}{2} h^{\kappa - \zeta}$. We proceed to verify that the inequalities (21) cannot all be valid. This will suffice to establish the theorem.

Since $\kappa > \zeta(n + 1)$ we have $(L + 1)^n < k^n < \frac{1}{2} h^{\kappa - \zeta}$, and so (21) certainly holds for all $l$ with $1 \leqslant l \leqslant (L + 1)^n$. For this range of values of $l$ we define

$$
\Psi (l) = \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) \alpha_ {1} ^ {\lambda_ {1} l} \dots \alpha_ {n} ^ {\lambda_ {n} l}.
$$

Now from (4) and the estimate

$$
\left| \alpha_ {1} ^ {\lambda_ {1}} \dots \alpha_ {n - 1} ^ {\lambda_ {n - 1}} \right| <   c _ {1 6} ^ {L},
$$

we obtain (cf. the proof of Lemma 2)

$$
\left| \alpha_ {1} ^ {\gamma_ {1} l} \dots \alpha_ {n - 1} ^ {\gamma_ {n - 1} l} - \alpha_ {1} ^ {\lambda_ {1} l} \dots \alpha_ {n} ^ {\lambda_ {n} l} \right| <   c _ {1 7} ^ {L l} e ^ {- \hbar \kappa},
$$

and hence

$$
\left| \Phi (l, \dots , l) - \Psi (l) \right| \leqslant (L + 1) ^ {n} e ^ {2 h k} c _ {1 7} ^ {L l} e ^ {- h ^ {\kappa}}.
$$

Further, the number on the right of the last inequality is at most  $e^{-h^{\kappa}}$ , since clearly

$$
L l \leqslant L (L + 1) ^ {n} \leqslant 2 ^ {n} h ^ {\zeta (n + 1) (1 - \epsilon)} <   2 ^ {n} h ^ {\kappa (1 - \epsilon)}.
$$

It follows therefore from (21) that

$$
\left| \Psi (l) \right| <   2 e ^ {- \frac {1}{2} h ^ {\kappa}}.\tag{22}
$$

Let now $a_1, \ldots, a_n$ be defined as in the proof of Lemma 2 and write

$$
\omega = (a _ {1} \dots a _ {n}) ^ {L l} \Psi (l).
$$

Clearly  $\omega$  represents an algebraic integer with degree at most D. Further, any of its conjugates, obtained by substituting arbitrary conjugates for  $\alpha_{1}, \ldots, \alpha_{n}$ , has absolute value at most

$$
(L + 1) ^ {n} e ^ {2 h k} c _ {1 8} ^ {L l} <   c _ {1 9} ^ {h \kappa (1 - \epsilon)}.
$$

It follows easily, on using (22), that

$$
\left| \mathbf {N o r m} \omega \right| <   1,
$$

whence  $\omega$ , and thus also  $\Psi(l)$ , must be 0.† Now the equations

$$
\Psi (l) = 0 \quad \left(1 \leqslant l \leqslant (L + 1) ^ {n}\right)
$$

are linear in the  $p(\lambda_{1}, \ldots, \lambda_{n})$  and, since the latter are not all 0, we see that the determinant of coefficients must vanish. But the determinant is of Vandermonde type, and its vanishing would imply

$$
\alpha_ {1} ^ {\lambda_ {1}} \dots \alpha_ {n} ^ {\lambda_ {n}} = \alpha_ {1} ^ {\lambda_ {1} ^ {\prime}} \dots \alpha_ {n} ^ {\lambda_ {n} ^ {\prime}}
$$

for distinct sets of integers  $\lambda_{1},\ldots,\lambda_{n}$  and  $\lambda_{1}^{\prime},\ldots,\lambda_{n}^{\prime}$ . This is contrary to the hypothesis that  $\log\alpha_{1},\ldots,\log\alpha_{n}$  and  $2\pi i$  are linearly independent over the rationals, and the contradiction proves the theorem.

5. Proof of Corollary 2. It is clear that Corollary 1 (used with the real value of $\log \alpha_{1}$) implies the validity of Corollary 2 for $n = 1$. We suppose that Corollary 2 is true for $n = m - 1$, where $m$ denotes an integer $\geqslant 2$, and we proceed to prove the validity for $n = m$.

Suppose the contrary, namely that

$$
\alpha_ {1} ^ {\beta_ {1}} \dots \alpha_ {m} ^ {\beta_ {m}} = \alpha_ {m + 1}
$$

for some algebraic number $\alpha_{m+1}$. We cannot have $\alpha_{m+1} = 1$; for then, on writing $\gamma_j = -\beta_j / \beta_m$ ($1 \leqslant j < m$), as we may since $\beta_m \neq 0$, we would obtain

$$
\alpha_ {1} ^ {\gamma_ {1}} \dots \alpha_ {m - 1} ^ {\gamma_ {m - 1}} = \alpha_ {m},
$$

where  $1, \gamma_{1}, \ldots, \gamma_{m-1}$  are linearly independent over the rationals, contrary to the inductive hypothesis. We put  $\beta_{m+1} = -1$ . Then

$$
\alpha_ {1} ^ {\beta_ {1}} \dots \alpha_ {m + 1} ^ {\beta_ {m + 1}} = 1
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\Psi (l)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$Q = 0$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† The vanishing of $\Psi(l)$ corresponds to the alternative $Q = 0$ at the end of the proof of Lemma 3.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\dagger$ This is in fact the Gelfond–Schneider theorem for real numbers.</span></small>

and $\beta_{1},\ldots ,\beta_{m + 1}$ are linearly independent over the rationals. Now, by Corollary 1, there exist rationals $\rho_{1},\dots,\rho_{m + 1}$, not all 0, such that

$$
\alpha_ {1} ^ {\rho_ {1}} \dots \alpha_ {m + 1} ^ {\rho_ {m + 1}} = 1.
$$

By a suitable permutation of suffixes we can suppose that  $\rho_{m+1} \neq 0$ . Then the numbers

$$
\delta_ {j} = \rho_ {m + 1} \beta_ {j} - \beta_ {m + 1} \rho_ {j} \quad (1 \leqslant j \leqslant m)
$$

are linearly independent over the rationals (in particular $\delta_{m} \neq 0$) and

$$
\alpha_ {1} ^ {\delta_ {1}} \dots \alpha_ {m} ^ {\delta_ {m}} = 1.
$$

Hence, writing $\epsilon_{j} = -\delta_{j} / \delta_{m}$ ($1 \leqslant j < m$), we see that $1, \epsilon_{1}, \ldots, \epsilon_{m-1}$ are linearly independent over the rationals and

$$
\alpha_ {1} ^ {\epsilon_ {1}} \dots \alpha_ {m - 1} ^ {\epsilon_ {m - 1}} = \alpha_ {m},
$$

again contrary to the inductive hypothesis. This proves the corollary.

A more general result, relating to real or complex algebraic numbers, follows from the more general theorem mentioned in the footnote on page 204.

## References

1. N. I. Feldman, “Approximation by algebraic numbers to the logarithms of algebraic numbers”, Izv. Akad. Nauk SSSR, 24 (1960), 475–492 (in Russian).

2. A. O. Gelfond, “On Hilbert’s seventh problem”, Doklady Akad. Nauk SSSR, 2 (1934), 1–6; Izv. Akad. Nauk SSSR, 7 (1934), 623–634 (in Russian and French).

3. ——, “On the approximation of the ratio of logarithms of two algebraic numbers by algebraic numbers”, Izv. Akad. Nauk SSSR, 5–6 (1939), 509–518 (in Russian).
4. ——, Transcendental and algebraic numbers (New York, 1960).

5. —— and Yu. V. Linnik “On Thue’s method and the problem of effectiveness in quadratic fields”, Doklady Akad. Nauk SSSR, 61 (1948), 773–776 (in Russian).

6. Th. Schneider, “Transzendenzuntersuchungen periodischer Funktionen I. Transzendenz von Potenzen”, J. Reine Angew. Math. 172 (1934), 65–69.

7. ——, Einführung in die transzendenten Zahlen (Berlin, Göttingen, Heidelberg, 1957).

8. C. L. Siegel, Transcendental numbers (Princeton, 1949).

Trinity College,
Cambridge.

(Received on the 17th of October, 1966.)