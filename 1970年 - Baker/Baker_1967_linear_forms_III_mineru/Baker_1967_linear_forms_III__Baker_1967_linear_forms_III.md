# LINEAR FORMS IN THE LOGARITHMS OF ALGEBRAIC NUMBERS (III)

## A. BAKER

1. Introduction. In the present paper the researches initiated in the two earlier papers† of this series are continued, and, by suitable generalizations of the techniques employed therein, solutions are obtained to some further well known problems from the theory of transcendental numbers. It will be proved, for example, that a nonvanishing linear form, with algebraic coefficients, in the logarithms of algebraic numbers, cannot be algebraic. This implies, in particular, that  $\pi + \log \alpha$  is transcendental for any algebraic number  $\alpha \neq 0$ , and also  $e^{\alpha\pi + \beta}$  is transcendental for all algebraic numbers  $\alpha$ ,  $\beta$  with  $\beta \neq 0$ .

Our main result may be regarded as an “inhomogeneous” analogue of the “homogeneous” inequalities given earlier. We prove:

THEOREM 1. Let $\alpha_{1},\ldots,\alpha_{n}$ and $\beta_{0},\beta_{1},\ldots,\beta_{n}$ denote non-zero algebraic numbers. Suppose that $\kappa>n+1$, and let $d$ and $H$ denote respectively the maximum of the degrees and heights$\ddagger$ of $\beta_{0},\ldots,\beta_{n}$. Then§

$$
\left| \beta_ {0} + \beta_ {1} \log \alpha_ {1} + \dots + \beta_ {n} \log \alpha_ {n} \right| > C e ^ {- (\log H) ^ {\kappa}}
$$

for some effectively computable number

$$
C = C (n, \alpha_ {1}, \dots , \alpha_ {n}, \kappa , d) > 0.
$$

It will be observed that although some or all of  $\beta_{1}, \ldots, \beta_{n}$  can be supposed zero, the condition that  $\beta_{0} \neq 0$  is necessary for the validity of Theorem 1; for  $\log \alpha_{1}, \ldots, \log \alpha_{n}$  may be linearly dependent over the rationals. However, with a suitable additional hypothesis, the method of proof applies also in the case  $\beta_{0} = 0$ , and it then enables the results established earlier to be strengthened slightly. In fact it will be apparent that the following result holds.

THEOREM 2. Let $\alpha_{1},\ldots ,\alpha_{n}$ and $\beta_{1},\ldots ,\beta_{n}$ denote non-zero algebraic numbers. Suppose that either $\log \alpha_1,\dots ,\log \alpha_n$ or $\beta_{1},\dots ,\beta_{n}$ are linearly independent over the rationals. Suppose further that $\kappa >n$ and let $d$ and $H$ denote respectively the maximum of the degrees and heights of $\beta_{1},\ldots ,\beta_{n}$. Then

$$
\left| \beta_ {1} \log \alpha_ {1} + \dots + \beta_ {n} \log \alpha_ {n} \right| > C e ^ {- (\log H) ^ {\kappa}}
$$

for some effectively computable number

$$
C = C (n, \alpha_ {1}, \dots , \alpha_ {n}, \kappa , d) > 0.
$$

From Theorem 1 it is clear that $e^{\beta_0} \alpha_1^{\beta_1} \ldots \alpha_n^{\beta_n}$ is transcendental for any non-zero algebraic numbers $\alpha_1, \ldots, \alpha_n, \beta_0, \beta_1, \ldots, \beta_n$. Furthermore, from Theorems 1 and 2,

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† A. Baker, “Linear forms in the logarithms of algebraic numbers,” Mathematika, 13 (1966), 204–216, (II) 14 (1967), 102–107. The papers will be referred to as (I) and (II) respectively.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(I),</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">‡ The height of an algebraic number is given, as in (I), by the maximum of the absolute values of the relatively prime integer coefficients in the minimal defining polynomial.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\alpha_{1},\ldots ,\log \alpha_{n}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">§ For  $\log \alpha_{1}, \ldots, \log \alpha_{n}$  we take any fixed determinations of the logarithms. The value of C depends on the choice of these determinations.</span></small>

we see that if  $\alpha_{1},\ldots,\alpha_{n}$  are non-zero algebraic numbers such that  $\log\alpha_{1},\ldots,\log\alpha_{n}$  are linearly independent over the rationals, then  $1,\log\alpha_{1},\ldots,\log\alpha_{n}$  are linearly independent over the field of all algebraic numbers. These corollaries answer, in particular, certain questions raised by Siegel in his well known monograph.†

The condition $\kappa > n$ in Theorem 2 strengthens the corresponding conditions given in (I) and (II), and, moreover, in the case $n = 2$, it agrees precisely with the best measure of transcendence for $\log \alpha_{1} / \log \alpha_{2}$ established to date. However, it is probably still far from best possible; indeed one would conjecture that Theorems 1 and 2 hold with $\kappa = 1$ provided that a suitable function of $n$ and $d$ is included in the exponent of $e$ on the right of the asserted inequalities. A significant improvement would be of interest not only from the point of view of our knowledge concerning transcendental numbers, but also in connexion with recent applications of the work of (I) and (II) relating, more especially, to the theory of Diophantine equations.

2. Notation. The remainder of the paper is devoted almost entirely to the proof of Theorem 1; in §3 we establish some preliminary lemmas, and in §4 we give the main argument. Here we introduce the notation that will be needed subsequently and we record a few preparatory observations.

Let $n$ denote any positive integer and let $\alpha_{1}, \ldots, \alpha_{n}$ denote non-zero algebraic numbers with degrees at most $d$. We shall suppose that

$$
\kappa > n + 2\tag{1}
$$

and we shall first establish Theorem 1 with this inequality in place of the condition $\kappa > n + 1$ given in the enunciation. It will be explained subsequently how the proof can be modified to obtain the asserted improvement. By $c, c_1, c_2, \ldots$ we shall denote numbers, greater than 1, which depend only on $n, \alpha_1, \ldots, \alpha_n, \kappa, d$; the number $c$ will be assumed sufficiently large throughout.

We now suppose that $\beta_0, \ldots, \beta_{n-1}$ are non-zero algebraic numbers with degrees at most $d$ such that

$$
\left| \beta_ {0} + \beta_ {1} \log \alpha_ {1} + \dots + \beta_ {n - 1} \log \alpha_ {n - 1} - \log \alpha_ {n} \right| <   e ^ {- (\log H) ^ {\kappa}},\tag{2}
$$

where $H$ denotes some number not less than $c$ and the heights of $\beta_0, \ldots, \beta_{n-1}$. We shall prove ultimately that the supposition leads to a contradiction; by arguments similar to those given in (I) §2 it follows easily that the contradiction suffices to establish the desired conclusion. We note that since, for any complex number $z$,

$$
\left| e ^ {z} - 1 \right| \leqslant | z | e ^ {| z |},
$$

we obtain from (2)

$$
\left| e ^ {\beta_ {0}} \alpha_ {1} ^ {\beta_ {1}} \dots \alpha_ {n - 1} ^ {\beta_ {n - 1}} - \alpha_ {n} \right| <   \left| \alpha_ {n} \right| e ^ {- (\log H) ^ {\kappa} + 1}.\tag{3}
$$

We now define

$$
\zeta = \frac {1}{2} \{1 + \kappa / (n + 2) \}, \varepsilon = (1 - 1 / \zeta) / (4 n)
$$

and we observe that, by virtue of (1), we have

$$
1 <   \zeta <   \kappa / (n + 2) \quad \text { and } \quad 0 <   \varepsilon <   1 / (4 n).
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">§ See A. Baker, “On the representation of integers by binary forms” to appear in Phil. Trans. Royal Society London, series A.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† C. L. Siegel, Transcendental numbers (Princeton, 1949); see pp. 84 and 97.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">‡ See A. O. Gelfond, Transcendental and algebraic numbers (New York, 1960), Theorem III, p. 134.</span></small>

We write

$$
h = [ \log H ], \quad k = [ h ^ {\zeta} ],
$$

where, as usual, $[x]$ denotes the integral part of $x$. Further, we define $L = [k^{1 - \varepsilon}]$, and we put $D = d^{2n}$.

Finally, for any integral function  $f(z_{0}, \ldots, z_{n-1})$  of the complex variables  $z_{0}, \ldots, z_{n-1}$  and any non-negative integers  $m_{0}, \ldots, m_{n-1}$  we write

$$
f _ {m _ {0}, \dots , m _ {n - 1}} (z _ {0}, \dots , z _ {n - 1}) = \frac {\partial^ {m _ {0} + \dots + m _ {n - 1}}}{\partial z _ {0} ^ {m _ {0}} \dots \partial z _ {n - 1} ^ {m _ {n - 1}}} f (z _ {0}, \dots , z _ {n - 1}).
$$

3. Lemmas. We now give seven lemmas preliminary to the proof of Theorem 1.

LEMMA 1. Let M, N denote integers with N > M > 0 and let  $u_{ij}$  denote integers with absolute values at most U. Then there exist integers  $x_{1}, \ldots, x_{N}$ , not all 0, with absolute values at most  $(NU)^{M/(N-M)}$  such that

$$
\sum_ {j = 1} ^ {N} u _ {i j} x _ {j} = 0 \quad (1 \leqslant i \leqslant M).
$$

Proof. See (I), Lemma 1.

LEMMA 2. There are integers $p(\lambda_0, \ldots, \lambda_n)$, not all 0, with absolute values at most $e^{2hk}$, such that the function

$$
\Phi \left(z _ {0}, \dots , z _ {n - 1}\right) = \sum_ {\lambda_ {0} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p \left(\lambda_ {0}, \dots , \lambda_ {n}\right) z _ {0} ^ {\lambda_ {0}} e ^ {\lambda_ {n} \beta_ {0} z _ {0}} \alpha_ {1} ^ {\gamma_ {1} z _ {1}} \dots \alpha_ {n - 1} ^ {\gamma_ {n - 1} z _ {n - 1}},
$$

where $\gamma_r = \lambda_r + \lambda_n\beta_r$ (1 ≤ r < n), satisfies

$$
\left| \Phi_ {m _ {0}, \dots , m _ {n - 1}} (l, \dots , l) \right| <   e ^ {- \frac {1}{2} h ^ {\kappa}}\tag{4}
$$

for all integers $l$ with $1 \leqslant l \leqslant h$ and all non-negative integers $m_0, \ldots, m_{n-1}$ with $m_0 + \ldots + m_{n-1} \leqslant k$.

Proof. We shall determine the  $p(\lambda_{0}, \ldots, \lambda_{n})$  such that

$$
\sum_ {\lambda_ {0} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {0}, \dots , \lambda_ {n}) q (\lambda_ {0}, \lambda_ {n}, l) \alpha_ {1} ^ {\lambda_ {1} l} \dots \alpha_ {n} ^ {\lambda_ {n} l} \gamma_ {1} ^ {m _ {1}} \dots \gamma_ {n - 1} ^ {m _ {n - 1}} = 0,\tag{5}
$$

for the above ranges of $l$ and $m_0, \ldots, m_{n-1}$, where

$$
q \left(\lambda_ {0}, \lambda_ {n}, z\right) = \sum_ {\mu_ {0} = 0} ^ {m _ {0}} \binom{m _ {0}}{\mu_ {0}} \lambda_ {0} \left(\lambda_ {0} - 1\right) \dots \left(\lambda_ {0} - \mu_ {0} + 1\right) \left(\lambda_ {n} \beta_ {0}\right) ^ {m _ {0} - \mu_ {0}} z ^ {\lambda_ {0} - \mu_ {0}},
$$

and we shall verify subsequently that (5) implies (4). Let  $a_{1}, \ldots, a_{n}, b_{0}, \ldots, b_{n-1}$  denote the leading coefficients (supposed positive) in the minimal defining polynomials of  $\alpha_{1}, \ldots, \alpha_{n}, \beta_{0}, \ldots, \beta_{n-1}$  respectively. Then for any non-negative integer j we have

$$
\left. \begin{array}{l} (a _ {r} \alpha_ {r}) ^ {j} = \sum_ {s = 0} ^ {d - 1} a _ {r s} ^ {(j)} \alpha_ {r} ^ {s} \quad (1 \leqslant r \leqslant n), \\ (b _ {r} \beta_ {r}) ^ {j} = \sum_ {t = 0} ^ {d - 1} b _ {r t} ^ {(j)} \beta_ {r} ^ {t} \quad (0 \leqslant r <   n), \end{array} \right\}\tag{6}
$$

where the $a_{rs}^{(j)}$ and $b_{rt}^{(j)}$ denote rational integers with absolute values at most $c_1^j$ and $(2H)^j$ respectively (see (I), §2). Thus multiplying (5) by

$$
(a _ {1} \dots a _ {n}) ^ {L l} b _ {0} ^ {m _ {0}} \dots b _ {n - 1} ^ {m _ {n - 1}},
$$

writing

$$
\gamma_ {r} ^ {m _ {r}} = \sum_ {\mu_ {r} = 0} ^ {m _ {r}} \binom{m _ {r}}{\mu_ {r}} \lambda_ {r} ^ {m _ {r} - \mu_ {r}} (\lambda_ {n} \beta_ {r}) ^ {\mu_ {r}}
$$

and substituting from (6) for the powers of  $a_{r}\alpha_{r}$  and  $b_{r}\beta_{r}$  which result, we obtain the equation

$$
\sum_ {s _ {1} = 0} ^ {d - 1} \dots \sum_ {s _ {n} = 0} ^ {d - 1} \sum_ {t _ {0} = 0} ^ {d - 1} \dots \sum_ {t _ {n - 1} = 0} ^ {d - 1} A (s, t) \alpha_ {1} ^ {s _ {1}} \dots \alpha_ {n} ^ {s _ {n}} \beta_ {0} ^ {t _ {0}} \dots \beta_ {n - 1} ^ {t _ {n - 1}} = 0,
$$

where

$$
A (s, t) = \sum_ {\lambda_ {0} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} \sum_ {\mu_ {0} = 0} ^ {m _ {0}} \dots \sum_ {\mu_ {n - 1} = 0} ^ {m _ {n - 1}} p (\lambda_ {0}, \dots , \lambda_ {n}) q ^ {\prime} q ^ {\prime \prime} q ^ {\prime \prime \prime}
$$

and $q', q'', q'''$ are given by

$$
q ^ {\prime} = \prod_ {r = 1} ^ {n} \{a _ {r} ^ {(L - \lambda_ {r}) l} a _ {r, s _ {r}} ^ {(\lambda_ {r} l)} \},
$$

$$
q ^ {\prime \prime} = \prod_ {r = 1} ^ {n - 1} \left\{\binom{m _ {r}}{\mu_ {r}} (b _ {r} \lambda_ {r}) ^ {m _ {r} - \mu_ {r}} \lambda_ {n} ^ {\mu_ {r}} b _ {r, t _ {r}} ^ {(\mu_ {r})} \right\},
$$

$$
q ^ {\prime \prime \prime} = \binom {m _ {0}} {\mu_ {0}} \lambda_ {0} (\lambda_ {0} - 1) \dots (\lambda_ {0} - \mu_ {0} + 1) \lambda_ {n} ^ {m _ {0} - \mu_ {0}} b _ {n} ^ {\mu_ {0}} l ^ {\lambda_ {0} - \mu_ {0}} b _ {0, t _ {0}} ^ {(m _ {0} - \mu_ {0})}.
$$

Thus (5) will be satisfied if the D equations  $A(s, t) = 0$  hold. Now these represent linear equations in the  $p(\lambda_{0}, \ldots, \lambda_{n})$  with integer coefficients. Further, since

$$
l \leqslant h \text { and } \binom{m _ {r}}{\mu_ {r}} \leqslant 2 ^ {m _ {r}}
$$

we have

$$
\left| q ^ {\prime} \right| \leqslant \prod_ {r = 1} ^ {n} \left\{a _ {r} ^ {(L - \lambda_ {r}) l} c _ {1} ^ {\lambda_ {r} l} \right\} \leqslant c _ {2} ^ {L h},
$$

$$
\left| q ^ {\prime \prime} \right| \leqslant \prod_ {r = 1} ^ {n - 1} (4 H L) ^ {m _ {r}},
$$

$$
\left| q ^ {\prime \prime \prime} \right| \leqslant 2 ^ {m _ {0}} \left(\lambda_ {0} b _ {n}\right) ^ {\mu_ {0}} \left(2 H \lambda_ {n}\right) ^ {m _ {0} - \mu_ {0}} l ^ {\lambda_ {0} - \mu_ {0}} \leqslant (4 H L) ^ {m _ {0}} h ^ {L}.
$$

Hence, by virtue of the inequalities

$$
\begin{array}{c} m _ {0} + \dots + m _ {n - 1} \leqslant k, \\ (m _ {0} + 1) \dots (m _ {n - 1} + 1) \leqslant 2 ^ {m _ {0} + \dots + m _ {n - 1}} \leqslant 2 ^ {k}, \end{array}
$$

it follows easily that the coefficient of  $p(\lambda_{0}, \ldots, \lambda_{n})$  in the linear form  $A(s, t)$ , namely

$$
\sum_ {\mu_ {0} = 0} ^ {m _ {0}} \dots \sum_ {\mu_ {n - 1} = 0} ^ {m _ {n - 1}} q ^ {\prime} q ^ {\prime \prime} q ^ {\prime \prime \prime},
$$

has absolute value at most $U = (8HL)^k c_3^{Lh}$. Now there are at most $(k + 1)^n h$ distinct sets of integers $l, m_0, \ldots, m_{n-1}$, and hence there are $M \leqslant D(k + 1)^n h$ equations $A(s, t) = 0$ corresponding to them. Further, there are $N = (L + 1)^{n+1}$ unknowns $p(\lambda_0, \ldots, \lambda_n)$, and since

$$
(n + 1) (1 - \varepsilon) \geqslant n + 1 - 2 n \varepsilon = (1 + 2 \varepsilon) n + 1 / \zeta ,
$$

and $k > \frac{1}{2} h^{\zeta}$, we see that

$$
N > k ^ {(n + 1) (1 - \varepsilon)} > \frac {1}{2} k ^ {(1 + 2 \varepsilon) n} h > 2 M.
$$

It follows from Lemma 1 that the system of equations $A(s, t) = 0$ can be solved non-trivially and indeed the integers $p(\lambda_0, \ldots, \lambda_n)$ can be chosen to have absolute values at most $NU$. Since $L \leqslant k^{1 - \varepsilon}$, $\log H < \frac{3}{2} h$ and $k \leqslant h^\zeta$ we have

$$
N U \leqslant k ^ {n + 1} c _ {3} ^ {L h} (8 k e ^ {\frac {3}{2} h}) ^ {k} \leqslant e ^ {2 h k}
$$

if $h$ is sufficiently large, as required.

It remains only to verify that (5) implies (4). Now it is clear that the left-hand side of (5) is obtained from  $\Phi_{m_{0},\ldots,m_{n-1}}(l,\ldots,l)$ , apart from a factor

$$
P = (\log \alpha_ {1}) ^ {m _ {1}} \dots (\log \alpha_ {n - 1}) ^ {m _ {n - 1}}
$$

in the latter, by substituting $\alpha_{n}$ for $e^{\beta_0}\alpha_1^{\beta_1}\ldots \alpha_{n - 1}^{\beta_{n - 1}}$. From (3) we deduce that

$$
\left| \left(e ^ {\beta_ {0}} \alpha_ {1} ^ {\beta_ {1}} \dots \alpha_ {n - 1} ^ {\beta_ {n - 1}}\right) ^ {\lambda_ {n} l} - \alpha_ {n} ^ {\lambda_ {n} l} \right| \leqslant \lambda_ {n} l \left(\left| \alpha_ {n} \right| + 1\right) ^ {\lambda_ {n} l} \left| e ^ {\beta_ {0}} \alpha_ {1} ^ {\beta_ {1}} \dots \alpha_ {n - 1} ^ {\beta_ {n - 1}} - \alpha_ {n} \right| \leqslant c _ {4} ^ {L h} e ^ {- h ^ {\kappa}}.
$$

Further, since $|\beta_r| \leqslant dH$ (see (I), §2), we have

$$
\left| \gamma_ {r} \right| \leqslant 2 d L H, \left| q \left(\lambda_ {0}, \lambda_ {n}, l\right) \right| \leqslant (2 d L H) ^ {m _ {0}} l ^ {L}
$$

and so

$$
\left| P q \left(\lambda_ {0}, \lambda_ {n}, l\right) \alpha_ {1} ^ {\lambda_ {1} l} \dots \alpha_ {n - 1} ^ {\lambda_ {n - 1} l} \gamma_ {1} ^ {m _ {1}} \dots \gamma_ {n - 1} ^ {m _ {n - 1}} \right| \leqslant c _ {5} ^ {k + L l} (2 d L H) ^ {k} <   e ^ {2 h k}.
$$

Thus we obtain

$$
\left| \Phi_ {m _ {3}, \dots , m _ {n - 1}} (l, \dots , l) \right| \leqslant (L + 1) ^ {n + 1} e ^ {4 h k} c _ {4} ^ {L h} e ^ {- h ^ {\kappa}}
$$

and (4) follows since $L \leqslant k$, $Lh \leqslant hk \leqslant h^{1 + \zeta}$ and $\kappa > 1 + \zeta$. This completes the proof of the lemma.

LEMMA 3. For any non-negative integers $m_{0}, \ldots, m_{n-1}$ with

$$
m _ {0} + \ldots + m _ {n - 1} \leqslant k,
$$

and any complex number $z$, we have

$$
\left| \Phi_ {m _ {0}, \dots , m _ {n - 1}} (z, \dots , z) \right| <   e ^ {4 h k} c _ {6} ^ {L | z |}.
$$

Further, for any integer $l$ with $0 < l \leqslant h^{\kappa - \zeta + \frac{1}{2}\varepsilon \zeta}$, either (4) holds or

$$
| \Phi_ {m _ {0}, \dots , m _ {n - 1}} (l, \dots , l) | > (e ^ {6 h k} c _ {7} ^ {L l D}) ^ {- D}.
$$

Proof. See (I), Lemma 3. The only essential variation in the previous work concerns the presence of the function  $q(\lambda_{0}, \lambda_{n}, z)$  in the expression for

$$
\Phi_ {m _ {0}, \dots , m _ {n - 1}} (z, \dots , z);
$$

the function is estimated by

$$
\left| q \left(\lambda_ {0}, \lambda_ {n}, z\right) \right| \leqslant (2 d L H) ^ {m _ {0}} | z | ^ {L}.
$$

LEMMA 4. Let $J$ be any integer satisfying $0 \leqslant J < \tau$, where

$$
\tau = 2 \varepsilon^ {- 1} \{(\kappa - 1) \zeta^ {- 1} - 1 \} + 1.
$$

Then (4) holds for all integers $l$ with $1 \leqslant l \leqslant hk^{\frac{1}{2}\varepsilon J}$ and each set of non-negative integers $m_0, \ldots, m_{n-1}$ with $m_0 + \ldots + m_{n-1} \leqslant k/2^J$.

Proof. See (I), Lemma 4. The argument is applicable in the present context almost unchanged.

It may be of interest to note that the later discussion can be modified so that it would suffice to take for  $\tau$  the slightly smaller value  $\varepsilon^{-1}\{n+(\kappa-2)\zeta^{-1}\}+1$ ; with this value, the observation given in the footnote on page 213 of (I) would no longer be required, and the number C specified in the theorem would thereby assume a simpler form.

LEMMA 5. For each integer $j$ with $0 \leqslant j \leqslant k^{n+1}$ we have

$$
\log | \phi_ {j} (0) | <   - h ^ {\kappa} / \log h,\tag{7}
$$

where

$$
\phi (z) = \Phi (z, \dots , z).
$$

Proof. See (II), Lemma 4. In a few obvious places  $n+1$  must be substituted for n, and the condition  $\kappa > \zeta(n+2)$  must now be used instead of  $\kappa > \zeta(2n+1)$ , but the proof is otherwise essentially unaltered.

LEMMA 6. Let $t_1, \ldots, t_n$ denote integers with absolute values at most $T$, and let

$$
\omega = t _ {1} \log \alpha_ {1} + \dots + t _ {n} \log \alpha_ {n}.
$$

Then either $\omega = 0$ or $|\omega| > c_8^{-T}$.

Proof. See (II), Lemma 5. It will be apparent that the proof remains valid if the condition assumed in (II), that  $\log\alpha_{1},\ldots,\log\alpha_{n}$  are linearly independent over the rationals, is replaced by  $\omega\neq0$ .

LEMMA 7. Let $R, S$ denote positive integers and let $\sigma_0, \ldots, \sigma_{R-1}$ denote distinct complex numbers. Define $\sigma$ as the maximum of 1, $|\sigma_0|, \ldots, |\sigma_{R-1}|$, and define $\rho$ as the minimum of 1, $|\sigma_i - \sigma_j|$ ($0 \leqslant i < j < R$). Further, let $r, s$ denote any integers satisfying $0 \leqslant r < R, 0 \leqslant s < S$. Then there exist complex numbers $w_i (0 \leqslant i < RS)$, with absolute values at most $(8\sigma/\rho)^{RS}$, such that the polynomial

$$
W (z) = \sum_ {j = 0} ^ {R S - 1} w _ {j} z ^ {j}
$$

satisfies $W_{j}(\sigma_{i}) = 0$ for each pair of integers $i, j$ with $0 \leqslant i < R$, $0 \leqslant j < S$, other than $i = r, j = s$, and $W_{s}(\sigma_{r}) = 1$.

Proof.† Let $W(z) = U(z)V(z)$, where

$$
U (z) = (- 1) ^ {S + s} (s!) ^ {- 1} \left\{\left(z - \sigma_ {0}\right) \dots \left(z - \sigma_ {R - 1}\right) \right\} ^ {S},
$$

$$
V(z) = \sum_{\substack{j_{0}\geqslant 0\\ j_{0} + \ldots +j_{R - 1} = S - s - 1}}\ldots \sum_{\substack{j_{R - 1}\geqslant 0\\ }}v(\sigma_{r} - z)^{-j_{r} - 1}
$$

and

$$
v = \prod_{\substack{i = 0\\ i\neq r}}^{R - 1}\binom {S + j_{i} - 1}{j_{i}}(\sigma_{r} - \sigma_{i})^{-S - j_{i}}.
$$

We proceed to verify that  $W(z)$  has all the required properties.

First we observe that the exponent of each term  $(\sigma_{r}-z)$  in  $V(z)$  lies between -1 and -S, and, since  $U(z)$  represents a polynomial in z with a zero at  $z=\sigma_{r}$  of order S, it follows that  $W(z)$  is a polynomial with degree at most RS-1. Further it is clear that the typical factor in the product defining v has absolute value at most  $2^{S-1}\rho^{-S-j_{i}}$ , and thus

$$
| v | \leqslant 2 ^ {R S} / \rho^ {(R - 1) S + j _ {0} + \dots + j _ {R - 1}} \leqslant (2 / \rho) ^ {R S}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† cf. Gelfond; loc. cit. pp. 140–142.</span></small>

On noting that the coefficients of  $(\sigma_{r}-z)^{-j_{r}-1}U(z)$  have absolute values at most  $(\sigma+1)^{RS}$  and observing, in addition, that the number of terms in the sum defining  $V(z)$  does not exceed  $S^{R}$ , it follows easily that the coefficients of  $W(z)$  have absolute values at most

$$
S ^ {R} (\sigma + 1) ^ {R S} (2 / \rho) ^ {R S} \leqslant (8 \sigma / \rho) ^ {R S},
$$

as required.

Now $V(z)$ represents a rational function of $z$, regular at all points in the complex plane, other than $z = \sigma_r$. Since $U(z)$ has a zero at $z = \sigma_i$ ($0 \leqslant i < R$) of order $S$, we see that, certainly, $W_j(\sigma_i) = 0$ for each pair of integers $i, j$ ($0 \leqslant i < R, 0 \leqslant j < S$) with $i \neq r$. Suppose now that $z \neq \sigma_i$ ($0 \leqslant i < R$) and let $C_i$ denote the circle in the complex plane, described in the positive sense, with centre $\sigma_i$ and with radius $\frac{1}{2} \min(\rho, |z - \sigma_i|)$. Then it is clear that

$$
V (z) = \frac {- 1}{s ! (S - s - 1) !} \left[ \frac {d ^ {S - s - 1}}{d \zeta^ {S - s - 1}} \frac {(\zeta - \sigma_ {r}) ^ {S}}{(\zeta - z) U (\zeta)} \right] _ {\zeta = \sigma_ {r}} = \frac {- 1}{2 \pi i} \left(\frac {1}{s !}\right) \int_ {C _ {r}} \frac {(\zeta - \sigma_ {r}) ^ {s}}{(\zeta - z) U (\zeta)} d \zeta .
$$

The absolute value of the integrand on the right, multiplied by $|\zeta|$, decreases to 0 as $|\zeta| \to \infty$, and hence, by Cauchy's residue theorem, we have

$$
W (z) = \frac {(z - \sigma_ {r}) ^ {s}}{s !} + \frac {U (z)}{s !} \frac {1}{2 \pi i} \sum_ {\substack {j = 0 \\ j \neq r}} ^ {R - 1} \int_ {C _ {j}} \frac {(\zeta - \sigma_ {r}) ^ {s}}{(\zeta - z) U (\zeta)} d \zeta .
$$

But the sum over j obviously represents a rational function of z, regular at  $z = \sigma_{r}$ , and, since  $U(z)$  has a zero at  $z = \sigma_{r}$  of order S, it follows easily that  $W_{j}(\sigma_{r}) = 1$  if j = s and 0 otherwise. This completes the proof of the lemma.

4. The principal argument. Theorem 1 has an obvious interpretation for $n = 0$, and it is clearly valid in this case. We shall prove the theorem (for $n \geqslant 1$ and with $\kappa > n + 2$) on the supposition that the result is valid for all integers less than $n$; the desired conclusion then follows by induction. The supposition enables us to assume that there are no integers $b_1, \ldots, b_n$, with absolute values at most $H$, such that

$$
b _ {1} \log \alpha_ {1} + \dots + b _ {n} \log \alpha_ {n} = 0,
$$

other than $b_{1} = \ldots = b_{n} = 0$. For if there were integers $b_{1}, \ldots, b_{n}$ with these properties, but $b_{r} \neq 0$ for some $r$, then we would have

$$
b _ {r} \left(\beta_ {0} + \beta_ {1} \log \alpha_ {1} + \dots + \beta_ {n} \log \alpha_ {n}\right) = \beta_ {0} ^ {\prime} + \beta_ {1} ^ {\prime} \log \alpha_ {1} + \dots + \beta_ {n} ^ {\prime} \log \alpha_ {n},\tag{8}
$$

where

$$
\beta_ {0} ^ {\prime} = b _ {r} \beta_ {0}, \quad \beta_ {j} ^ {\prime} = b _ {r} \beta_ {j} - b _ {j} \beta_ {r} \quad (1 \leqslant j \leqslant n).
$$

It is easily verified, by observations similar to those recorded in (I) §2, that $\beta_0'$, ..., $\beta_n'$ represent algebraic numbers with degrees at most $d^2$ and with heights at most $H'$, where $\log H'/\log H$ is bounded above by a number depending only on $d$. Since $\beta_0' \neq 0$, $\beta_r' = 0$, we could now apply the inductive hypothesis and obtain a lower bound for the expression on the right of (8) of the form $C' e^{-(\log H)\kappa'}$, where $\kappa'$ denotes any number $>n+1$; this would immediately imply the desired conclusion.

We proceed now to prove that the inequalities (7), given by Lemma 5, cannot all be valid. This will establish Theorem 1 under the condition that  $\kappa$  satisfies (1), and

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$(-1)^{\frac{1}{2}}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">† Here, as in the next displayed formula, i denotes  $(-1)^{\frac{1}{2}}$ ; otherwise i represents a variable suffix.</span></small>

we shall demonstrate subsequently how the condition can be relaxed to $\kappa > n + 1$. We begin by writing $S = L + 1$ and $R = S^n$. Then any integer $i$ with $0 \leqslant i < RS$ can be expressed uniquely in the form

$$
i = \lambda_ {0} + \lambda_ {1} S + \ldots + \lambda_ {n} S ^ {n},
$$

where $\lambda_0, \ldots, \lambda_n$ denote integers between 0 and $L$ inclusive. For each such $i$ we define

$$
v _ {i} = \lambda_ {0}, p _ {i} = p (\lambda_ {0}, \dots , \lambda_ {n}),
$$

and we put

$$
\psi_ {i} = \lambda_ {n} \beta_ {0} + \gamma_ {1} \log \alpha_ {1} + \dots + \gamma_ {n - 1} \log \alpha_ {n - 1}.
$$

From (2) we see that $\psi_{i}$ differs from $\lambda_{1} \log \alpha_{1} + \ldots + \lambda_{n} \log \alpha_{n}$ by at most an amount $Le^{-h^{\kappa}}$ and, since $L < k < H$, it follows easily from Lemma 6, together with the assumption made above, that any two $\psi_{i}$ which correspond to distinct sets $\lambda_{1}, \ldots, \lambda_{n}$ differ by at least $c_{8}^{-L} - 2Le^{-h^{\kappa}} > \frac{1}{2} c_{8}^{-L}$. In particular we see that exactly $R$ of the $\psi_{i}$ are distinct, and we denote the different values, in some order, by $\sigma_{0}, \ldots, \sigma_{R-1}$. If $\sigma, \rho$ are defined as in Lemma 7, we have then $\sigma \leqslant c_{9}k$ and $\rho > c_{10}^{-L}$.

Let now t be any suffix such that  $p_{t} \neq 0$ , let  $s = v_{t}$ , let r be that suffix for which  $\psi_{t} = \sigma_{r}$ , and let  $W(z)$  denote the polynomial given by Lemma 7. By the properties of  $W(z)$  specified in the lemma we see that

$$
p _ {t} = \sum_ {i = 0} ^ {R S - 1} p _ {i} W _ {\nu_ {i}} (\psi_ {i}).
$$

Further, by Leibnitz's theorem, we have

$$
W _ {v _ {i}} (\psi_ {i}) = \sum_ {j = 0} ^ {R S - 1} j (j - 1) \dots (j - v _ {i} + 1) w _ {j} \psi_ {i} ^ {j - v _ {i}} = \sum_ {j = 0} ^ {R S - 1} w _ {j} \left[ \frac {d ^ {j}}{d z ^ {j}} \left(z ^ {v _ {i}} e ^ {\psi_ {i} z}\right) \right] _ {z = 0},
$$

and thus, on noting that

$$
\phi (z) = \sum_ {i = 0} ^ {R S - 1} p _ {i} z ^ {\nu_ {i}} e ^ {\psi_ {i} z},
$$

we obtain

$$
p _ {t} = \sum_ {j = 0} ^ {R S - 1} w _ {j} \phi_ {j} (0).
$$

Now $RS \leqslant k^{n+1}$ and so, by Lemma 5, we see that (7) holds for all integers $j$ with $0 \leqslant j < RS$. Further, by Lemma 7, we have

$$
\left| w _ {j} \right| \leqslant (8 \sigma / \rho) ^ {R S} \leqslant \left(8 c _ {9} k c _ {1 0} ^ {L}\right) ^ {R S} \leqslant c _ {1 1} ^ {k ^ {n + 2}}.
$$

Hence, on recalling that $p_t \neq 0$, it follows that

$$
0 \leqslant \log R S + c _ {1 2} k ^ {n + 2} - h ^ {\kappa} / \log h.
$$

But since  $k \leqslant h^{\zeta}$  and  $\kappa > \zeta(n + 2)$ , the inequality is obviously impossible if h is sufficiently large, and the contradiction establishes the desired conclusion.

5. Completion of proofs. It will be apparent that the method of proof given above, applied now to the auxiliary function constructed in (I), establishes Theorem 2, provided that the condition  $\kappa > n + 1$  replaces  $\kappa > n$ . Moreover it will be clear that a similar argument enables one to obtain an improvement in Lemma 6; in fact one

can assert that either $\omega = 0$ or, for any $\kappa > n + 1$, we have $|\omega| > c_8^{-1} e^{-(\log T)\kappa}$, where $c_8 (>1)$ is an effectively computable number depending only on $n$, $\alpha_1, \ldots, \alpha_n$ and $\kappa$. The only essential variation in the proofs concerns the inductive discussion given at the beginning of §4; it must now be verified that the specific hypothesis relating to each theorem is valid for the new form

$$
\omega^ {\prime} = \beta_ {1} ^ {\prime} \log \alpha_ {1} + \dots + \beta_ {n} ^ {\prime} \log \alpha_ {n},
$$

where  $\beta_{r}^{\prime}=0$ . This is in fact easily confirmed; if  $\log\alpha_{1},\ldots,\log\alpha_{n}$  are linearly independent over the rationals the need for the inductive hypothesis does not arise; if  $\beta_{1},\ldots,\beta_{n}$  are linearly independent over the rationals then so also are

$$
\beta_ {j} ^ {\prime} = b _ {r} \beta_ {j} - b _ {j} \beta_ {r} \quad (1 \leqslant j \leqslant n, j \neq r);
$$

and, in connexion with Lemma 6, if $\omega \neq 0$ then also $\omega' = b_r\omega \neq 0$.

The strengthening of Lemma 6 leads to the desired improvements in Theorems 1 and 2. In the argument given in §4 one can now assert that

$$
\rho > c _ {1 0} ^ {- 1} e ^ {- (\log L) ^ {n + 2}},
$$

and since

$$
R S = (L + 1) ^ {n + 1} \leqslant (2 k ^ {1 - \varepsilon}) ^ {n + 1},
$$

we obtain

$$
\left| w _ {j} \right| \leqslant (8 \sigma / \rho) ^ {R S} \leqslant \left(8 c _ {9} c _ {1 0} k e ^ {(\log k) ^ {n + 2}}\right) ^ {R S} \leqslant c _ {1 1} ^ {k n + 1}.
$$

Furthermore, it was only in the final deduction that critical use was made of the inequality $\kappa > \zeta(n+2)$; at all other places in the proof (including, in particular, Lemma 5) the inequality $\kappa > \zeta(n+1)$ would suffice. Moreover, in the final deduction, the need for the stricter inequality arose only from the estimate for $|w_j|$. Hence, on re-defining $\zeta$ as $\frac{1}{2}\{1 + \kappa/(n+1)\}$, so that $\kappa > \zeta(n+1)$, all the above arguments will now be valid, and Theorem 1 follows. Similar considerations apply to Theorem 2.

Trinity College,
Cambridge.