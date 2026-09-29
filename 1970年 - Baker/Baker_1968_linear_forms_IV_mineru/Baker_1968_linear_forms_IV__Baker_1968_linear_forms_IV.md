# LINEAR FORMS IN THE LOGARITHMS OF ALGEBRAIC NUMBERS (IV)

## A. BAKER

1. Introduction. As a consequence of the methods developed in the earlier papers of this series  $[1, 2, 3]$ , an effective algorithm has recently been established for solving many Diophantine equations in two unknowns (see  $[4, 5, 6, 7]$ ). The algorithm leads to an explicit bound for the size of all the solutions, and, in principle therefore, it enables any specific equation of the type considered to be fully resolved by a finite amount of computation. On examining the various estimates occurring in the course of the exposition, however, it at once became apparent that the computation would involve a very large number of operations and would scarcely be practicable even with a modern machine. It was clear, on the other hand, that a modified version of the fundamental inequality involving the logarithms of algebraic numbers would much facilitate the computational work, and it was in the light of this observation that the researches discussed herein were begun. The object has been to obtain a theorem of an essentially practical nature which may be found useful in application to a wide variety of different problems. The result which we shall establish is neither the most precise nor the most general that can be obtained in this direction, but it would seem to be the most serviceable of its kind, and it would apparently make feasible many calculations which would otherwise have seemed quite out of the question.

Throughout the paper,  $\alpha_{1},\ldots,\alpha_{n}$  will denote  $n\geqslant2$  non-zero algebraic numbers. The heights and degrees of  $\alpha_{1},\ldots,\alpha_{n}$  will be supposed not to exceed integers A, d respectively, where  $A\geqslant4$ ,  $d\geqslant4$ . It will further be supposed that  $0<\delta\leqslant1$ . By  $\log\alpha_{1},\ldots,\log\alpha_{n}$  will be meant the principal values of the logarithms. Our purpose is to prove the following theorem.

THEOREM. If rational integers $b_{1}, \ldots, b_{n}$ exist, with absolute values at most $H$, such that

$$
0 <   \left| b _ {1} \log \alpha_ {1} + \dots + b _ {n} \log \alpha_ {n} \right| <   e ^ {- \delta H},\tag{1}
$$

then

$$
H <   (4 ^ {n ^ {2}} \delta^ {- 1} d ^ {2 n} \log A) ^ {(2 n + 1) ^ {2}}.\tag{2}
$$

The demonstration follows, in general outline, the arguments of  $[4]$  and  $[5]$ , but, as will be apparent later, there is a considerable difference in detail. The present work has therefore been made largely self-contained with only a few results of an auxiliary nature cited without proof. The exposition is also slightly simpler than that given previously for there is here no need to distinguish between the heights of the various algebraic numbers, a feature which played an important rôle in the earlier work.

As a particular application, the theorem has recently been employed to prove that the only solutions in positive integers x, y, z of the equations

$$
3 x ^ {2} - 2 = y ^ {2}, \quad 8 x ^ {2} - 7 = z ^ {2},
$$

are given by x = 1 and x = 11; this has been carried out in a paper by H. Davenport and the author which has been submitted to the Quarterly J. Math. Oxford.

2. Preliminaries. First we note that if  $\alpha$  is an algebraic number, other than 0 or 1, with height at most  $A(\geqslant4)$  and with degree at most  $d(\geqslant4)$ , and if  $\log\alpha$  denotes the principal value of the logarithm, then

$$
(2 d A) ^ {- d - 4} \leqslant | \log \alpha | \leqslant 4 \log (d A).\tag{3}
$$

The right-hand inequality is easily verified, for we have $|\alpha| \leqslant dA$, $|\alpha|^{-1} \leqslant dA$ (see [1; §2]), and

$$
| \log \alpha | \leqslant \{(\log | \alpha |) ^ {2} + \pi^ {2} \} ^ {\frac {1}{2}}.
$$

The left-hand inequality follows from the estimate  $\left|\operatorname{norm}\left(\alpha-1\right)\right| \geqslant A^{-1}$  together with the observation that each conjugate of  $\alpha-1$  has absolute value at most 2dA; this gives  $\left|\alpha-1\right| \geqslant (2dA)^{-d}$  and since, for any complex number z,

$$
\left| e ^ {z} - 1 \right| \leqslant | z | e ^ {| z |},\tag{4}
$$

we see that

$$
| \alpha - 1 | = | e ^ {\log \alpha} - 1 | \leqslant | \log \alpha | e ^ {| \log \alpha |} \leqslant | \log \alpha | (d A) ^ {4}.
$$

We now assume the hypotheses of the theorem and we proceed to prove that either (2) holds or there exists an integer $k$ with $2 \leqslant k \leqslant n$ for which the following conditions are satisfied: (i) There are rational integers $b_{1}''$, ..., $b_{n}''$ with absolute values at most $(2H)^{n - k + 1}$ such that

$$
0 <   \left| b _ {1} ^ {\prime \prime} \log \alpha_ {1} + \dots + b _ {n} ^ {\prime \prime} \log \alpha_ {n} \right| <   H ^ {n - k} e ^ {- \delta H},\tag{5}
$$

(ii) at least $n - k$ of the integers $b_{1}^{\prime \prime}, \ldots, b_{n}^{\prime \prime}$ are 0, (iii) the only rational integers $b_{1}^{\prime}, \ldots, b_{n}^{\prime}$ with absolute values at most $H$ such that

$$
b _ {1} ^ {\prime} \log \alpha_ {1} + \dots + b _ {n} ^ {\prime} \log \alpha_ {n} = 0,\tag{6}
$$

and such that also $b_{j'} = 0$ whenever $b_{j}'' = 0$, are given by $b_{1}' = \ldots = b_{n}' = 0$. Clearly (i) and (ii) are valid for $k = n$, since then (5) reduces to (1) with $b_{j}'' = b_{j}$. If also (iii) were valid for $k = n$ then there would be nothing to prove, and we assume therefore that (iii) does not hold in this case. There is then a least integer $k \geqslant 2$ for which (i) and (ii) hold, but (iii) does not. Let $b_{1}''$, ..., $b_{n}''$ denote the corresponding integers satisfying (i) and (ii), and let $b_{1}', \ldots, b_{n}'$ denote integers with the properties specified by (iii) other than $b_{1}' = \ldots = b_{n}' = 0$. Suppose in fact that $b_{l}' \neq 0$ and put

$$
b _ {j} ^ {\prime \prime \prime} = b _ {j} ^ {\prime \prime} b _ {l} ^ {\prime} - b _ {j} ^ {\prime} b _ {l} ^ {\prime \prime} \quad (1 \leqslant j \leqslant n).
$$

Clearly (5) and (6) imply that

$$
0 <   \left| b _ {1} ^ {\prime \prime \prime} \log \alpha_ {1} + \dots + b _ {n} ^ {\prime \prime \prime} \log \alpha_ {n} \right| <   \left| b _ {l} ^ {\prime} \right| H ^ {n - k} e ^ {- \delta H} \leqslant H ^ {n - k + 1} e ^ {- \delta H}.
$$

Further we have $b_{j}''' = 0$ whenever $b_{j}'' = 0$, and since also $b_{l}''' = 0$, $b_{l}'' \neq 0$ we see that at least $n - k + 1$ of the integers $b_{1}'''$, ..., $b_{n}'''$ are 0. Moreover, the $b_{j}'''$ have absolute values at most $(2H)^{n - k + 2}$. Thus (i) and (ii) hold with $k$ replaced by $k - 1$. But now the minimal choice of $k$ implies that either (iii) holds with $k$ replaced by $k - 1$ or $k - 1 = 1$. By (i) and (ii) we see that if the second alternative holds then

$$
0 <   | b _ {j} ^ {\prime \prime} \log \alpha_ {j} | <   H ^ {n - 1} e ^ {- \delta H}
$$

for some integer $b_{j}^{\prime \prime}$, and so from (3) with $\alpha = \alpha_{j}$ we obtain

$$
\delta H - (n - 1) \log H <   (d + 4) \log (2 d A),
$$

whence (2) follows. Otherwise the first alternative holds and $k - 1$ has all the required properties.

Henceforth it will be assumed that $\alpha_{1},\ldots,\alpha_{n},d,A$ and $\delta$ are defined as in §1, that $b_{1},\ldots,b_{n}$ are rational integers with absolute values at most $H^{n'}$ such that (1) holds, $n'$ denoting an integer $\geqslant n$, and that there are no rational integers $b_{1}',\ldots,b_{n}'$ with absolute values at most $H$ such that (6) holds, other than $b_{1}'=\ldots=b_{n}'=0$. It will further be assumed that

$$
H \geqslant (4 ^ {n ^ {\prime} 2 - \frac {1}{2}} \delta^ {- 1} d ^ {2 n ^ {\prime}} \log A) ^ {(2 n + 1) ^ {2}},\tag{7}
$$

and it will ultimately be shown that this assumption leads to a contradiction. The contradiction suffices to establish the theorem; for if (1) holds for some integers $b_{1}, \ldots, b_{n}$ with absolute values at most $H$, but (2) is not satisfied, then clearly, for any $k \geqslant 2$, we have $(2H)^{n - k + 1} \leqslant H^{n}$ and $H^{n - k}e^{-\delta H} \leqslant e^{-\frac{1}{4}\delta H}$; by virtue of the preceding discussion, we see that all the assumptions made above are satisfied with the $\alpha_{j}$ given by a subset of the original $\alpha_{1}, \ldots, \alpha_{n}$, defined by those $j$ for which $b_{j}'' \neq 0$, consequently with the new value of $n$ given by the number of these $b_{j}''$, with $n'$ defined by the former value of $n$, and with $\frac{1}{2}\delta$ in place of $\delta$; the inference that (7) is not valid plainly implies the conclusion of the theorem.

3. Lemmas. We suppose, without loss of generality, that $b_{n} \neq 0$, and we write

$$
\beta_ {j} = - b _ {j} / b _ {n} \quad (1 \leqslant j <   n).
$$

Then $\beta_{1},\ldots ,\beta_{n - 1}$ satisfy

$$
0 <   \left| \beta_ {1} \log \alpha_ {1} + \dots + \beta_ {n - 1} \log \alpha_ {n - 1} - \log \alpha_ {n} \right| <   e ^ {- \delta H},\tag{8}
$$

and, from (4), we see that

$$
\left| \alpha_ {1} ^ {\beta_ {1}} \dots \alpha_ {n - 1} ^ {\beta_ {n - 1}} - \alpha_ {n} \right| <   \left| \alpha_ {n} \right| e ^ {- \delta H + 1}.\tag{9}
$$

We define

$$
k = \left[ H ^ {2 / (2 n + 1)} \right], \quad h = \left[ k ^ {1 / (4 n + 2)} \right], \quad L = \left[ k ^ {(2 n - 1) / (2 n + 1)} \right],
$$

where, as usual, [x] denotes the integral part of x. By virtue of (7) we have then

$$
k > H ^ {2 / (2 n + 1)} - 1 > \frac {3}{4} H ^ {2 / (2 n + 1)},\tag{10}
$$

$$
h > k ^ {1 / (4 n + 2)} - 1 > \frac {3}{4} k ^ {1 / (4 n + 2)},\tag{11}
$$

whence

$$
h > 4 ^ {n ^ {\prime} 2 - 1} \delta^ {- 1} d ^ {2 n ^ {\prime}} \log A.\tag{12}
$$

For brevity we write $D = d^n$ and, for any integral function $f(z_1, \ldots, z_{n-1})$ of the complex variables $z_1, \ldots, z_{n-1}$ and any non-negative integers $m_1, \ldots, m_{n-1}$, we put

$$
f _ {m _ {1}, \dots , m _ {n - 1}} (z _ {1}, \dots , z _ {n - 1}) = \frac {\partial^ {m _ {1} + \dots + m _ {n - 1}}}{\partial z _ {1} ^ {m _ {1}} \dots \partial z _ {n - 1} ^ {m _ {n - 1}}} f (z _ {1}, \dots , z _ {n - 1}).
$$

LEMMA. 1. Let $M, N$ denote integers with $N > M > 0$ and let $u_{ij} (1 \leqslant i \leqslant M, 1 \leqslant j \leqslant N)$ denote integers with absolute values at most $U (\geqslant 1)$. Then there exist

integers $x_{1}, \ldots, x_{N}$, not all 0, with absolute values at most $(NU)^{M/(N-M)}$, such that

$$
\sum_ {j = 1} ^ {N} u _ {i j} x _ {j} = 0 \quad (1 \leqslant i \leqslant M).
$$

Proof. See [1; Lemma 1].

LEMMA 2. There are integers $p(\lambda_1, \ldots, \lambda_n)$, not all 0, with absolute values at most $e^{hk}$, such that the function

$$
\Phi (z _ {1}, \dots , z _ {n - 1}) = \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) \alpha_ {1} ^ {\gamma_ {1} z _ {1}} \dots \alpha_ {n - 1} ^ {\gamma_ {n - 1} z _ {n - 1}},
$$

where $\gamma_r = \lambda_r + \lambda_n\beta_r$ (1 ≤ r < n), satisfies

$$
\left| \Phi_ {m _ {1}, \dots , m _ {n - 1}} (l, \dots , l) \right| <   e ^ {- \frac {1}{2} \delta H}\tag{13}
$$

for all integers $l$ with $1 \leqslant l \leqslant Dh$ and all non-negative integers $m_1, \ldots, m_{n-1}$ with $m_1 + \ldots + m_{n-1} \leqslant k$.

Proof. We shall determine the $p(\lambda_1, \ldots, \lambda_n)$ such that

$$
\sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) \alpha_ {1} ^ {\lambda_ {1} l} \dots \alpha_ {n} ^ {\lambda_ {n} l} \gamma_ {1} ^ {m _ {1}} \dots \gamma_ {n - 1} ^ {m _ {n - 1}} = 0\tag{14}
$$

for the above ranges of $l$ and $m_1, \ldots, m_{n-1}$ and we shall verify subsequently that (14) implies (13). Let $a_1, \ldots, a_n$ denote the leading coefficients (supposed positive) in the minimal defining polynomials of $\alpha_1, \ldots, \alpha_n$ respectively. Then for any nonnegative integer $j$ we have

$$
(a _ {r} \alpha_ {r}) ^ {j} = \sum_ {s = 0} ^ {d - 1} a _ {r s} ^ {(j)} \alpha_ {r} ^ {s},\tag{15}
$$

where the $a_{rs}^{(j)}$ denote rational integers with absolute values at most $(2A)^{j}$ (see [1; §2]). Thus multiplying (14) by

$$
(a _ {1} \dots a _ {n}) ^ {L l} b _ {n} ^ {m _ {1} + \dots + m _ {n - 1}},
$$

and substituting from (15) for the powers of  $a_{r}\alpha_{r}$  which result, we obtain the equation

$$
\sum_ {s _ {1} = 0} ^ {d - 1} \dots \sum_ {s _ {n} = 0} ^ {d - 1} V (s) \alpha_ {1} ^ {s _ {1}} \dots \alpha_ {n} ^ {s _ {n}} = 0,
$$

where

$$
V (s) = \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) v (\lambda , s),
$$

and

$$
v (\lambda , s) = a _ {n} ^ {(L - \lambda n) l} a _ {n, s _ {n}} ^ {(\lambda_ {n} l)} \prod_ {r = 1} ^ {n - 1} \left\{a _ {r} ^ {(L - \lambda_ {r}) l} a _ {r, s _ {r}} ^ {(\lambda_ {r} l)} \left(b _ {n} \lambda_ {r} - b _ {r} \lambda_ {n}\right) ^ {m _ {r}} \right\}.
$$

Hence (14) will be satisfied if the D equations  $V(s) = 0$  hold. Now these represent linear equations in the  $p(\lambda_{1}, \ldots, \lambda_{n})$  with integer coefficients. Further since

$$
l \leqslant D h, \quad m _ {1} + \dots + m _ {n - 1} \leqslant k,
$$

and, by hypothesis, the integers $b_r$ have absolute values at most $H^{n'}$, we deduce easily that the coefficient $v(\lambda, s)$ of $p(\lambda_1, \ldots, \lambda_n)$ in the linear form $V(s)$ has absolute value at most

$$
U = (2 A) ^ {n L D h} \left(2 L H ^ {n ^ {\prime}}\right) ^ {k}.
$$

Now there are at most $Dh(k + 1)^{n - 1}$ distinct sets of integers $l, m_1, \ldots, m_{n-1}$, and hence there are $M \leqslant D^2 h(k + 1)^{n - 1}$ equations $V(s) = 0$ corresponding to them. Further there are $N = (L + 1)^n$ unknowns $p(\lambda_1, \ldots, \lambda_n)$ and from (12) we see that

$$
N > k ^ {n (2 n - 1) / (2 n + 1)} = k ^ {n - 1 + 1 / (2 n + 1)} \geqslant h ^ {2} k ^ {n - 1} > 2 ^ {n} D ^ {2} h k ^ {n - 1} > 2 M.
$$

It follows from Lemma 1 that the system of equations $V(s) = 0$ can be solved nontrivially, and indeed the integers $p(\lambda_1, \ldots, \lambda_n)$ can be chosen to have absolute values at most $NU$. Now from (10), (11), (12) and the estimate $L \leqslant kh^{-4}$ we obtain

$$
(2 A) ^ {n L D h} \leqslant (2 A) ^ {n D k / h ^ {3}} <   e ^ {\frac {1}{4 0} h k},
$$

$$
(2 L H ^ {n ^ {\prime}}) ^ {k} <   H ^ {(n ^ {\prime} + 1) k} <   (2 h) ^ {(2 n ^ {\prime} + 1) ^ {3} k} <   e ^ {\frac {1 9}{2 0} h k};\tag{16}
$$

the final inequality follows from the observation that, for a given  $n'$ , the function

$$
\frac {1 9}{2 0} x - (2 n ^ {\prime} + 1) ^ {3} \log (2 x)
$$

increases for $x \geqslant \frac{20}{19}(2n' + 1)^3$, and is positive when

$$
x = 4 ^ {n ^ {\prime} 2 + n ^ {\prime} - 1} <   4 ^ {n ^ {\prime} 2 - 1} d ^ {2 n ^ {\prime}} <   h;
$$

and the last assertion is a consequence of the fact that the function

$$
f (y) = \frac {1 9}{2 0} 4 ^ {y ^ {2} + y - 1} \{(2 y + 1) ^ {3} \log (4 ^ {y ^ {2} + y - \frac {1}{2}}) \} ^ {- 1}
$$

exceeds 1 when $y = 2$ and increases for $y \geqslant 2$, the derivative being

$$
f (y) (2 y + 1) \left\{\log 4 - 6 (2 y + 1) ^ {- 2} - \left(y ^ {2} + y - \frac {1}{2}\right) ^ {- 1} \right\}.
$$

Since also $N < k^n < e^{\frac{1}{40} hk}$, we see that $NU < e^{hk}$, as required.

It remains only to verify that (14) implies (13). Now it is clear that the left-hand side of (14) is obtained from $\Phi_{m_1,\ldots,m_{n-1}}(l,\ldots,l)$, apart from a factor

$$
P = (\log \alpha_ {1}) ^ {m _ {1}} \dots (\log \alpha_ {n - 1}) ^ {m _ {n - 1}}\tag{17}
$$

in the latter, by substituting $\alpha_{n}$ for $\alpha_{1}^{\beta_{1}}\ldots \alpha_{n - 1}^{\beta_{n - 1}}$. From (9) we deduce that

$$
| (\alpha_ {1} ^ {\beta_ {1}} \dots \alpha_ {n - 1} ^ {\beta_ {n - 1}}) ^ {\lambda_ {n} l} - \alpha_ {n} ^ {\lambda_ {n} l} | \leqslant \lambda_ {n} l (| \alpha_ {n} | + 1) ^ {\lambda_ {n} l} | \alpha_ {1} ^ {\beta_ {1}} \dots \alpha_ {n - 1} ^ {\beta_ {n - 1}} - \alpha_ {n} | \leqslant (4 d A) ^ {2 L l} e ^ {- \delta H},
$$

and from (3) we obtain

$$
\left| P \alpha_ {1} ^ {\lambda_ {1} l} \dots \alpha_ {n - 1} ^ {\lambda_ {n - 1} l} \gamma_ {1} ^ {m _ {1}} \dots \gamma_ {n - 1} ^ {m _ {n - 1}} \right| \leqslant (4 d A) ^ {n (k + L l)} \left(2 L H ^ {n ^ {\prime}}\right) ^ {k}.
$$

Now clearly $Ll < k$ and from (12) we see that $(4dA)^{2nk} < e^{hk}$. Thus, on using (16) and the trivial estimate $(L + 1)^n < e^{hk}$, it follows at once that

$$
\left| \Phi_ {m _ {1}, \dots , m _ {n - 1}} (l, \dots , l) \right| <   e ^ {5 h k - \delta H},
$$

and this plainly gives (13), since $h \leqslant k^{\frac{1}{10}} \leqslant H^{\frac{1}{2k}}$, whence, from (7), $5hk < 5H^{\frac{1}{2}} < \frac{1}{2}\delta H$.

LEMMA 3. For any non-negative integers $m_1, \ldots, m_{n-1}$ with $m_1 + \ldots + m_{n-1} \leqslant k$ and any complex number $z$ we have

$$
\left| \Phi_ {m _ {1}, \dots , m _ {n - 1}} (z, \dots , z) \right| <   e ^ {2 h k} (d A) ^ {5 n L | z |}.\tag{18}
$$

Further, for any integer $l$ with $1 \leqslant l \leqslant k^{(2n^2 + 1) / (2n + 1)}$, either (13) holds or

$$
\left| \Phi_ {m _ {1}, \dots , m _ {n - 1}} (l, \dots , l) \right| > \left\{e ^ {2 h k} (d A) ^ {3 n L l} \right\} ^ {- D}.\tag{19}
$$

Proof. We have

$$
\Phi_ {m _ {1}, \dots , m _ {n - 1}} (z, \dots , z) = P \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) q (\lambda , z),
$$

where $P$ is given by (17) and

$$
q (\lambda , z) = \alpha_ {1} ^ {\gamma_ {1} z} \dots \alpha_ {n - 1} ^ {\gamma_ {n - 1} z} \gamma_ {1} ^ {m _ {1}} \dots \gamma_ {n - 1} ^ {m _ {n - 1}}.
$$

Now (3) and (8) imply that

$$
\begin{array}{r l} | \alpha_ {r} ^ {\lambda_ {r} z} | \leqslant & e ^ {\lambda_ {r} | \log \alpha_ {r} | z |} \leqslant (d A) ^ {4 L | z |} \quad (1 \leqslant r <   n), \\ & | (\alpha_ {1} ^ {\beta_ {1} z} \dots \alpha_ {n - 1} ^ {\beta_ {n - 1} z}) ^ {\lambda_ {n}} | \leqslant e ^ {\lambda_ {n} (| \log x _ {n} | + 1) | z |} \leqslant (d A) ^ {5 L | z |}, \end{array}
$$

and thus from (16) we obtain

$$
| P q (\lambda , z) | <   (d A) ^ {(4 n + 1) L | z |} \{4 e ^ {\frac {1 9}{2 0} h} \log (d A) \} ^ {m _ {1} + \dots + m _ {n - 1}}.
$$

Then (18) follows on noting that there are at most $k^n < e^{\frac{1}{\delta} hk}$ terms in the above multiple sum, that the $p(\lambda_1, \ldots, \lambda_n)$ have absolute values at most $e^{hk}$, and that, by (12), we have $4\log (dA) < e^{\frac{1}{\delta} h}$.

To prove the second assertion we begin by defining

$$
Q = P ^ {\prime} \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) q ^ {\prime} (\lambda , l),
$$

where

$$
P ^ {\prime} = \left(a _ {1} \dots a _ {n}\right) ^ {L l} b _ {n} ^ {m _ {1} + \dots + m _ {n - 1}}, q ^ {\prime} (\lambda , l) = \alpha_ {1} ^ {\lambda_ {1} l} \dots \alpha_ {n} ^ {\lambda_ {n} l} \gamma_ {1} ^ {m _ {1}} \dots \gamma_ {n - 1} ^ {m _ {n - 1}},
$$

and the $a_r$ are given as in the proof of Lemma 2. Then it is clear that $Q$ represents an algebraic integer with degree at most $D$. Further, by (16), we have

$$
\left| b _ {n} ^ {m _ {1} + \dots + m _ {n - 1}} \gamma_ {1} ^ {m _ {1}} \dots \gamma_ {n - 1} ^ {m _ {n - 1}} \right| <   e ^ {\frac {1 9}{2 0} h k},
$$

and so any conjugate of Q, obtained by substituting arbitrary conjugates for  $\alpha_{r}$ , has absolute value at most

$$
(L + 1) ^ {n} (d A) ^ {2 n L l} e ^ {\left(\frac {1 9}{2 0} + 1\right) h k} <   (d A) ^ {2 n L l} e ^ {2 h k}.
$$

Thus if $Q \neq 0$ we have $|\mathrm{norm}Q| \geqslant 1$ and hence

$$
| Q | \geqslant \{e ^ {2 h k} (d A) ^ {2 n L l} \} ^ {- D + 1}.
$$

Now from (9) we obtain (cf. the end of the proof of Lemma 2)

$$
| q (\lambda , l) - q ^ {\prime} (\lambda , l) | <   (4 d A) ^ {(n + 2) L l} e ^ {h k - \delta H},
$$

and, by virtue of (7) and the inequalities

$$
L l \leqslant k ^ {2 n (n + 1) / (2 n + 1)} \leqslant H ^ {1 - 1 / (2 n + 1) ^ {2}}, h k <   H ^ {\frac {1}{2}},\tag{20}
$$

it follows that the number on the right is at most  $e^{-\frac{3}{4}\delta H}$ . Hence we deduce that

$$
\left| P ^ {- 1} \Phi_ {m _ {1}, \dots , m _ {n - 1}} (l, \dots , l) - P ^ {\prime - 1} Q \right| \leqslant (L + 1) ^ {n} e ^ {h k - \frac {3}{4} \delta H} \leqslant e ^ {- \frac {5}{8} \delta H}.
$$

But since, again from (16),

$$
\left| P ^ {\prime} \right| \leqslant A ^ {n L l} H ^ {n ^ {\prime} k} <   A ^ {n L l} e ^ {h k},
$$

and, from (3) and (12),

$$
| P | \geqslant (2 d A) ^ {- (d + 4) k} > e ^ {- h k},
$$

we see that either $Q = 0$ or

$$
\left| P P ^ {\prime - 1} Q \right| > \left\{e ^ {2 h k} (d A) ^ {2 n L l} \right\} ^ {- D}.
$$

Now, by (7) and (20), it is clear that $e^{2Dhk}$ and $(dA)^{2nDLl}$ cannot exceed $e^{\frac{1}{2}\delta H}$, and thus the number on the right of the last inequality is at least $2e^{-\frac{1}{2}\delta H}$. Further, from (3),

we have

$$
| P | \leqslant (4 \log (d A)) ^ {k} <   e ^ {\frac {1}{8} \delta H}.
$$

This immediately implies the second part of the lemma, the asserted alternatives corresponding to the cases $Q = 0$ and $Q \neq 0$.

LEMMA 4. Let $J$ be any integer satisfying $0 < J < \frac{1}{2} n(4n - 1)$. Then (13) holds for all integers $l$ with $1 \leqslant l \leqslant k^{(2J + 1) / (4n + 2)}$ and each set of non-negative integers $m_1, \ldots, m_{n-1}$ with $m_1 + \ldots + m_{n-1} \leqslant k / 2^J$.

Proof. We suppose that $K$ is an integer satisfying $0 \leqslant K \leqslant \frac{1}{2} n(4n - 1) - 1$, and we assume that the lemma is true for $J = 0, 1, \ldots, K$; the assertion in the case $J = 0$ is understood to mean the conclusion of Lemma 2, namely that (13) holds for all integers $l$ with $1 \leqslant l \leqslant Dh$ and all non-negative integers $m_1, \ldots, m_{n-1}$ with $m_1 + \ldots + m_{n-1} \leqslant k$. We proceed to prove the validity of the lemma for $J = K + 1$.

We begin by defining $R_0 = Dh$, $S_0 = k$ and

$$
R _ {J} = [ k ^ {(2 J + 1) / (4 n + 2)} ], \quad S _ {J} = [ k / 2 ^ {J} ] \quad (J = 1, 2, \dots).
$$

It suffices then to prove that for any integer $l$ with $R_{K} < l \leqslant R_{K + 1}$ and any set of non-negative integers $m_{1},\ldots ,m_{n - 1}$ with $m_{1} + \ldots +m_{n - 1}\leqslant S_{K + 1}$ we have

$$
| f (l) | <   e ^ {- \frac {1}{2} \delta H},\tag{21}
$$

where

$$
f (z) = \Phi_ {m _ {1}, \dots , m _ {n - 1}} (z, \dots , z).
$$

By our inductive hypothesis we see that for each integer $r$ with $1 \leqslant r \leqslant R_K$ and each integer $m$ satisfying $0 \leqslant m \leqslant S_{K+1}$ we have

$$
\left| f _ {m} (r) \right| <   n ^ {k} e ^ {- \frac {1}{2} \delta H};\tag{22}
$$

for $f_{m}(r)$ is given by

$$
\left(\frac {\partial}{\partial z _ {1}} + \dots + \frac {\partial}{\partial z _ {n - 1}}\right) ^ {m} \Phi_ {m _ {1}, \dots , m _ {n - 1}} (z _ {1}, \dots , z _ {n - 1}),
$$

evaluated at the point $z_{1} = \ldots = z_{n - 1} = r$, that is by

$$
\sum_{\substack{j_{1} = 0\\ j_{1} + \ldots +j_{n - 1} = m}}^{m}\ldots \sum_{\substack{j_{n - 1} = 0\\ }}^{m}m!\left(j_{1}!\ldots j_{n - 1}!\right)^{-1}\Phi_{m_{1} + j_{1},\ldots ,m_{n - 1} + j_{n - 1}}(r,\ldots ,r),
$$

and the absolute values of the derivatives here are at most  $e^{-\frac{1}{2}\delta H}$  since

$$
m _ {1} + \dots + m _ {n - 1} + j _ {1} + \dots + j _ {n - 1} \leqslant k / 2 ^ {K}.
$$

We write, for brevity,

$$
F (z) = \{(z - 1) \dots (z - R _ {K}) \} ^ {S _ {K + 1} + 1},
$$

and we denote by $\Gamma$ the circle in the complex plane, described in the positive sense, with centre the origin and with radius $R_{K+1}h$. Then by Cauchy's residue theorem we have

$$
\frac {1}{2 \pi i} \int_ {\Gamma} \frac {f (z)}{(z - l) F (z)} d z = \frac {f (l)}{F (l)} + \frac {1}{2 \pi i} \sum_ {r = 1} ^ {R _ {K}} \sum_ {m = 0} ^ {S _ {K + 1}} \frac {f _ {m} (r)}{m !} \int_ {\Gamma_ {r}} \frac {(z - r) ^ {m} d z}{(z - l) F (z)},\tag{23}
$$

where  $\Gamma_{r}$  denotes the circle in the complex plane, described in the positive sense,

with centre $r$ and radius $\frac{1}{2}$ (see [1; Lemma 4]). Since, for $z$ on $\Gamma_r$,

$$
\left| (z - r) ^ {m} / F (z) \right| <   8 ^ {S _ {K + 1} + 1},
$$

we deduce from (22) and the inequalities

$$
R _ {K} \left(S _ {K + 1} + 1\right) \leqslant k ^ {1 + (2 K + 1) / (4 n + 2)} \leqslant k ^ {(4 n ^ {2} + 3 n + 1) / (4 n + 2)} \leqslant H ^ {1 - n / (2 n + 1) ^ {2}},\tag{24}
$$

that $1 / 2\pi$ times the absolute value of the double sum on the right of (23) is at most

$$
R _ {K} \left(S _ {K + 1} + 1\right) 8 ^ {S _ {K + 1} + 2} n ^ {k} e ^ {- \frac {1}{2} \delta H} <   H (8 n) ^ {k} e ^ {- \frac {1}{2} \delta H} <   e ^ {- \frac {1}{4} \delta H},
$$

the final inequality following at once from (7) and the estimates  $H < e^{h}$ ,  $hk < H^{\frac{1}{2}}$  included in (16) and (20). Further it is clear that

$$
| F (l) | \leqslant l ^ {R _ {K} (S _ {K + 1} + 1)} \leqslant R _ {K + 1} ^ {R _ {K} (S _ {K + 1} + 1)}.\tag{25}
$$

Also, since $R_{K + 1} \leqslant k^{(4n^2 - n + 1) / (4n + 2)}$, we see that $l$ satisfies the condition of Lemma 3, and thus either (21) holds or, by (19),

$$
| f (l) | > \{e ^ {2 h k} (d A) ^ {3 n L l} \} ^ {- D}.\tag{26}
$$

We show that the assumption that (26) is valid leads to a contradiction.

By (24), (25) and the trivial estimate $R_{K + 1} < H$ we obtain

$$
| F (l) | <   H ^ {R _ {\mathbf {K}} \left(S _ {\mathbf {K} + 1} + 1\right)} <   e ^ {\frac {1}{8} \delta H};
$$

for the latter inequality requires only that

$$
H ^ {n / (2 n + 1) ^ {2}} > 8 \delta^ {- 1} \log H,\tag{27}
$$

and by (12), the definitions of $h$ and $k$, and the inequality $H < e^h$ noted above, we have $h > 8\delta^{-1}$ and

$$
H ^ {1 / (2 n + 1) ^ {2}} \geqslant h > \log H.
$$

Further, from (7) and (20), we see that $e^{2Dhk}$ and $(dA)^{4nDLl}$ cannot exceed $e^{\frac{1}{16}\delta H}$, and hence (26) implies that

$$
| f (l) | > 2 e ^ {- \frac {1}{8} \delta H}.
$$

Thus we have

$$
| f (l) / F (l) | > 2 e ^ {- \frac {1}{4} \delta H},
$$

and, by virtue of the estimate for the double sum established above, it follows that the absolute value of the number on the right of (23) exceeds  $\frac{1}{2}|f(l)/F(l)|$ . Now let  $\theta$  and  $\Theta$  denote respectively the upper bound of  $|f(z)|$  and the lower bound of  $|F(z)|$  with z on  $\Gamma$ . Since  $2|z-l|$ , with z on  $\Gamma$ , exceeds the radius of  $\Gamma$ , we obtain from (23)

$$
4 \theta | F (l) | > \Theta | f (l) |.\tag{28}
$$

It is clear that

$$
\Theta \geqslant (\frac {1}{2} R _ {K + 1} h) ^ {R _ {K} (S _ {K + 1} + 1)},
$$

and, by (18) of Lemma 3, we have

$$
\theta \leqslant e ^ {2 h k} (d A) ^ {5 n L R _ {K + 1} h}.
$$

Thus from (25) we deduce that

$$
\Theta | F (l) | ^ {- 1} \geqslant (\frac {1}{2} h) ^ {R _ {K} (S _ {K + 1} + 1)},
$$

and from (26) we obtain

$$
\theta | f (l) | ^ {- 1} \leqslant \left\{e ^ {2 h k} (d A) ^ {5 n L R _ {K + 1} h} \right\} ^ {D + 1}.
$$

Then (28) gives

$$
\log 4 + (D + 1) \{2 h k + 5 n L R _ {K + 1} h \log (d A) \} \geqslant R _ {K} \left(S _ {K + 1} + 1\right) \log (\frac {1}{2} h).
$$

When $K = 0$ we obtain

$$
\log 4 + (D + 1) \{2 h k + 5 n k \log (d A) \} \geqslant \frac {1}{2} D h k \log (\frac {1}{2} h).
$$

But, by (12), the number on the left is at most 4Dhk, and since

$$
\log \left(\frac {1}{2} h\right) > \log \left(2 ^ {5} d ^ {4}\right) > 9,
$$

this is clearly incompatible with the number on the right. When K > 0 we obtain

$$
\log 4 + (D + 1) \{2 h k + 5 n k ^ {1 + K / (2 n + 1)} \log (d A) \} \geqslant 2 ^ {- (K + 1)} k R _ {K} \log (\frac {1}{2} h).
$$

But $R_{K} \geqslant \frac{8}{9} k^{(2K + 1) / (4n + 2)}$ and we have $k^{1 / (4n + 2)} \geqslant h, \log (\frac{1}{2} h) > 9$ and $K \leqslant 2(n^2 - 1)$. Thus it follows from (12) that the number on the right is at least

$$
2 ^ {- K + 2} h k ^ {1 + K / (2 n + 1)} > 4 D ^ {2} k ^ {1 + K / (2 n + 1)} \log A.
$$

On the other hand, since $D \geqslant 16$ and $k^{1/(2n+1)} \geqslant h^2$, we have

$$
\log 4 + 2 h k (D + 1) <   4 D h k \leqslant \frac {1}{4} D ^ {2} k ^ {1 + K / (2 n + 1)},
$$

and, since also $D \geqslant d^{n-1} \log d \geqslant 2n \log d$ and $D \geqslant 4^n \geqslant 8n$, we see that

$$
\begin{array}{r l} 5 n (D + 1) \log (d A) & \leqslant 5 \times \frac {1 7}{1 6} n D (\log d + \log A) \\ & \leqslant 6 D ^ {2} (\frac {1}{2} + \frac {1}{8} \log A) <   \frac {1 5}{4} D ^ {2} \log A. \end{array}
$$

Hence the inequality is inconsistent also in the case when K > 0 and the discussion of Lemma 4 is complete.

LEMMA 5. For each integer $j$ with $0 \leqslant j \leqslant k^n$ we have

$$
\log | \phi_ {j} (0) | <   - 2 ^ {- \frac {1}{2} n (4 n - 1)} k ^ {n (4 n + 3) / (4 n + 2)},\tag{29}
$$

where

$$
\phi (z) = \Phi (z, \dots , z).
$$

Proof. We write, for brevity,

$$
X = [ k ^ {(4 n ^ {2} - n - 2) / (4 n + 2)} ], \quad Y = [ 2 ^ {- \frac {1}{2} n (4 n - 1)} k ].
$$

Then clearly $[k^{(2J + 1) / (4n + 2)}] \geqslant X$ and $[k / 2^J] \geqslant Y$, where $J$ denotes the largest integer $< \frac{1}{2} n(4n - 1)$, and so, by Lemma 4, we see that (13) holds for each integer $l$ with $1 \leqslant l \leqslant X$ and each set of non-negative integers $m_1, \ldots, m_{n-1}$ satisfying $m_1 + \ldots + m_{n-1} \leqslant Y$. Hence we have

$$
| \phi_ {m} (r) | \leqslant n ^ {k} e ^ {- \frac {1}{2} \delta H}\tag{30}
$$

for each integer $r$ with $1 \leqslant r \leqslant X$ and each integer $m$ satisfying $0 \leqslant m \leqslant Y$ (cf. the proof of Lemma 4). Let $\Gamma$ and $\Lambda$ denote circles in the complex plane, described in the positive sense, with centres the origin and with radii $Xh$ and $\frac{1}{4}$ respectively. Suppose further that $w$ is any complex number on $\Lambda$. We proceed to calculate an upper bound for $|\phi(w)|$.

We write, for brevity,

$$
E (z) = \{(z - 1) \dots (z - X) \} ^ {Y + 1}.
$$

By Cauchy's residue theorem we have (cf. Lemma 4)

$$
\frac {1}{2 \pi i} \int_ {\Gamma} \frac {\phi (z)}{(z - w) E (z)} d z = \frac {\phi (w)}{E (w)} + \frac {1}{2 \pi i} \sum_ {r = 1} ^ {X} \sum_ {m = 0} ^ {Y} \frac {\phi_ {m} (r)}{m !} \int_ {\Gamma_ {r}} \frac {(z - r) ^ {m} d z}{(z - w) E (z)},\tag{31}
$$

where, as before,  $\Gamma_{r}$  denotes the circle in the complex plane, described in the positive sense, with centre r and radius  $\frac{1}{2}$ . Since, for z on  $\Gamma_{r}$ ,

$$
\left| (z - r) ^ {m} / E (z) \right| <   8 ^ {Y + 1},
$$

and since also

$$
X (Y + 1) \leqslant k ^ {n (4 n + 3) / (4 n + 2)} \leqslant H ^ {1 - (n + 1) / (2 n + 1) ^ {2}},\tag{32}
$$

it follows, on using (30), that $1/2\pi$ times the absolute value of the double sum on the right of (31) is at most

$$
X (Y + 1) 8 ^ {Y + 2} n ^ {k} e ^ {- \frac {1}{2} \delta H} <   H (8 n) ^ {k} e ^ {- \frac {1}{2} \delta H} <   e ^ {- \frac {1}{4} \delta H}.
$$

Now let  $\xi$  and  $\Xi$  denote respectively the upper bound of  $|\phi(z)|$  and the lower bound of  $|E(z)|$  with z on  $\Gamma$ . From (31) we have

$$
| \phi (w) | \leqslant (2 \xi \Xi^ {- 1} + e ^ {- \frac {1}{4} \delta H}) | E (w) |,
$$

and it is clear that

$$
| E (w) | \leqslant (X + 1) ^ {X (Y + 1)}, \quad | \Xi | \geqslant (\frac {1}{2} X h) ^ {X (Y + 1)}.
$$

Since also, by (18) of Lemma 3,

$$
\xi \leqslant e ^ {2 h k} (d A) ^ {5 n L X h},
$$

we obtain

$$
| \phi (w) | \leqslant 2 e ^ {2 h k} (d A) ^ {5 n L X h} (\frac {1}{4} h) ^ {- X (Y + 1)} + (2 X) ^ {2 X Y} e ^ {- \frac {1}{4} \delta H}.
$$

The second term on the right is at most $e^{-\frac{1}{6}\delta H}$, since plainly, by (7), (27) and (32),

$$
2 X Y \log (2 X) <   2 H ^ {1 - (n + 1) / (2 n + 1) ^ {2}} \log H <   \frac {1}{8} \delta H.
$$

Also from the estimates

$$
L \leqslant k h ^ {- 4}, \quad X > k, \quad Y + 1 > 2 ^ {- \frac {1}{2} n (4 n - 1)} h ^ {4 n + 2},
$$

together with (12), we deduce easily that $2e^{2hk}$ and $(dA)^{5nLXh}$ cannot exceed $e^{\frac{1}{2}X(Y + 1)}$. Thus we obtain

$$
| \phi (w) | <   (\frac {1}{1 6} h) ^ {- X (Y + 1)} + e ^ {- \frac {1}{8} \delta H};
$$

and the number on the right is at most $h^{-\frac{1}{2}X(Y + 1)}$, for it follows from (27) and (32) that $h^{X(Y + 1)} < e^{\frac{1}{2}\delta H}$, and, by (12), we have $h^{\frac{1}{2}} > 32$.

Let now $j$ be any integer satisfying $0 \leqslant j \leqslant k^n$. By Cauchy's residue theorem we have

$$
\phi_ {j} (0) = \frac {j !}{2 \pi i} \int_ {\Lambda} \frac {\phi (w)}{w ^ {j + 1}} d w.
$$

Thus from the bound for  $|\phi(w)|$  established above we obtain

$$
| \phi_ {j} (0) | <   j! 4 ^ {j} h ^ {- \frac {1}{2} X (Y + 1)}.
$$

Now clearly

$$
j! 4 ^ {j} \leqslant (4 j) ^ {j} \leqslant (4 k) ^ {n k n} \leqslant e ^ {2 n k n \log k},
$$

and, by (11), we see that the exponent of the number on the right is at most $8n(2n + 1)k^n\log h$. But we have

$$
X (Y + 1) > 2 ^ {- \frac {1}{2} n (4 n - 1) - 1} k ^ {n (4 n + 3) / (4 n + 2)},
$$

and, since $k^{1 / (4n + 2)} \geqslant h$, it follows from (12) that $X(Y + 1) > 8hk^n$. Since also, from (16), $h > (2n + 1)^3\log h$, we obtain $j!4^j < e^{\frac{1}{4} X(Y + 1)}$ and hence

$$
| \phi_ {j} (0) | <   h ^ {- \frac {1}{4} X (Y + 1)}.
$$

Then (29) follows in view of the estimate $\log h > 9$.

LEMMA 6. Let $t_1, \ldots, t_n$ denote rational integers with absolute values at most $T$, and let

$$
W = t _ {1} \log \alpha_ {1} + \dots + t _ {n} \log \alpha_ {n}.
$$

Then either $W = 0$ or $|W| > (dA)^{-4nDT}$.

Proof. Let $a_1, \ldots, a_n$ be defined as in the proof of Lemma 2 but with $\alpha_j^{-1}$ read for $\alpha_j$ whenever $t_j < 0$. Then

$$
\omega = a _ {1} ^ {| t _ {1} |} \dots a _ {n} ^ {| t _ {n} |} (\alpha_ {1} ^ {t _ {1}} \dots \alpha_ {n} ^ {t _ {n}} - 1)
$$

represents an algebraic integer with degree at most $D$. Further, by the first observation recorded in [1; §2], we see that any conjugate of $\omega$, obtained by substituting arbitrary conjugates for $\alpha_{1}, \ldots, \alpha_{n}$, has absolute value at most $2(dA)^{2nT}$. If $\omega = 0$ then $W$ is a multiple of $2\pi i$ and obviously the lemma is valid. Otherwise we have $|\text{norm } \omega| \geqslant 1$ and hence

$$
| \omega | \geqslant (d A) ^ {- 4 n T (D - 1)}.
$$

But since

$$
a _ {1} ^ {| t _ {1} |} \dots a _ {n} ^ {| t _ {n} |} \leqslant A ^ {n T},
$$

we deduce from (4) that

$$
| \omega | \leqslant | W | e ^ {| W |} A ^ {n T},
$$

whence assuming, as we may, that  $|W| < 1$ , the assertion follows.

4. Proof of the theorem. We proceed to prove that the inequalities (29) cannot all be valid. This will suffice to establish the theorem.

We write, for brevity, $R = (L + 1)^n - 1$. Then any integer $r$ with $0 \leqslant r \leqslant R$ can be expressed uniquely in the form

$$
r = \lambda_ {1} + \lambda_ {2} (L + 1) + \dots + \lambda_ {n} (L + 1) ^ {n - 1},
$$

where $\lambda_1, \ldots, \lambda_n$ denote integers satisfying $0 \leqslant \lambda_j \leqslant L$ ($1 \leqslant j \leqslant n$). For each such $r$ we define

$$
p _ {r} = p \left(\lambda_ {1}, \dots , \lambda_ {n}\right), \quad \psi_ {r} = \lambda_ {1} \log \alpha_ {1} + \dots + \lambda_ {n} \log \alpha_ {n},
$$

and we write

$$
\Psi_ {j} = \sum_ {r = 0} ^ {R} p _ {r} \psi_ {r} ^ {j} \quad (0 \leqslant j \leqslant R).
$$

We show first that $\Psi_{j}$ differs from $\phi_j(0)$ by at most an amount $e^{-\frac{1}{2}\delta H}$.

Clearly we have

$$
\phi_ {j} (0) = \sum_ {\lambda_ {1} = 0} ^ {L} \dots \sum_ {\lambda_ {n} = 0} ^ {L} p (\lambda_ {1}, \dots , \lambda_ {n}) (\gamma_ {1} \log \alpha_ {1} + \dots + \gamma_ {n - 1} \log \alpha_ {n - 1}) ^ {j}.
$$

From (3) we obtain $|\psi_r| < 4nL \log(dA)$, and thus it follows from (8) that, for any $j \leqslant R$,

$$
\left| \left(\gamma_ {1} \log \alpha_ {1} + \dots + \gamma_ {n - 1} \log \alpha_ {n - 1}\right) ^ {j} - \psi_ {r} ^ {j} \right| <   (1 6 n L \log (d A)) ^ {R} e ^ {- \delta H}.
$$

Now $L \leqslant kh^{-4}$ and hence (12) shows that the number on the right certainly cannot exceed $k^R e^{-\delta H}$. Thus we have

$$
\left| \phi_ {j} (0) - \Psi_ {j} \right| <   (R + 1) k ^ {R} e ^ {h k - \delta H}.
$$

But clearly

$$
(R + 1) k ^ {R} \leqslant (2 k) ^ {R} \leqslant e ^ {2 k n \log k}, H \geqslant k ^ {n + \frac {1}{2}}, k ^ {\frac {1}{2}} \geqslant h ^ {2 n + 1},
$$

and, in view of (12) again, these give

$$
\left| \phi_ {j} (0) - \Psi_ {j} \right| <   e ^ {- \frac {1}{2} \delta H},
$$

as asserted (cf. the end of the proof of Lemma 5). We note that, as a consequence of the latter estimate and (29) (which is applicable since $j \leqslant k^n$) we have

$$
\log | \Psi_ {j} | <   - 2 ^ {- \frac {1}{2} n (4 n - 1) - 1} k ^ {n (4 n + 3) / (4 n + 2)}.\tag{33}
$$

We now observe that each integer $p_r$ ($0 \leqslant r \leqslant R$) satisfies an equation of the form

$$
p _ {r} \Delta_ {r} (\psi_ {r}) = \sum_ {j = 0} ^ {R} \sigma_ {r, j} \Psi_ {j},\tag{34}
$$

where  $\Delta_{r}(x)$  and  $\sigma_{r,0},\ldots,\sigma_{r,R}$  are defined by the identities

$$
\Delta_{r}(x) = \prod_{\substack{s = 0\\ s\neq r}}^{R}(x - \psi_{s}) = \sigma_{r, 0} + \sigma_{r, 1}  x + \ldots +\sigma_{r,R}  x^{R}.
$$

We shall compare estimates for the numbers on either side of (34). Clearly  $\psi_{r}-\psi_{s}$  ( $r\neq s$ ) is a linear form in  $\log\alpha_{1},\ldots,\log\alpha_{n}$  with integer coefficients, each coefficient having absolute value at most  $L\leqslant k^{1-\varepsilon}<H$ , and not all the coefficients vanishing. Thus by the hypothesis made at the outset, that the only integers  $b_{1}^{\prime},\ldots,b_{n}^{\prime}$ , with absolute values at most H, such that (6) holds, are given by  $b_{1}^{\prime}=\ldots=b_{n}^{\prime}=0$ , we see that  $\psi_{r}-\psi_{s}\neq0$  and so, by Lemma 6,

$$
\left| \psi_ {r} - \psi_ {s} \right| > (d A) ^ {- 4 n D L}.
$$

On noting that there are $R < (2L)^n$ factors in the product defining $\Delta_r$, and using also the inequality $L \leqslant k^{(2n-1)/(2n+1)}$, it follows easily that

$$
\log \left| \Delta_ {r} (\psi_ {r}) \right| > - 2 ^ {2 n + 2} D k ^ {(n + 1) (2 n - 1) / (2 n + 1)} \log (d A).\tag{35}
$$

We proceed now to calculate an upper bound for  $\log|\Delta_{r}(\psi_{r})|$  for any r such that  $p_{r} \neq 0$ ; there is certainly at least one r with this property. We have

$$
|\sigma_{r,j}| \leqslant \prod_{\substack{s = 0\\ s\neq r}}^{R}(1 + |\psi_{s}|) \quad (0\leqslant j\leqslant R),
$$

and, by virtue of the trivial estimate $|\psi_j| \leqslant k$, we see that the product on the right does not exceed $(2k)^R$. Hence from (33) and (34) we obtain

$$
\log \left| p _ {r} \Delta_ {r} (\psi_ {r}) \right| \leqslant \log (R + 1) + R \log (2 k) - 2 ^ {- \frac {1}{2} n (4 n - 1) - 1} k ^ {n (4 n + 3) / (4 n + 2)}.
$$

Since $R \leqslant k^n$ and $k^{1/(4n+2)} \geqslant h$, it is clear from (12) that the sum of the first two terms on the right cannot exceed one half of the absolute value of the final term.

Thus we have

$$
\log | \Delta_ {r} (\psi_ {r}) | \leqslant - 2 ^ {- \frac {1}{2} n (4 n - 1) - 2} k ^ {n (4 n + 3) / (4 n + 2)}.
$$

But now (35) implies that

$$
k ^ {(n + 2) / (4 n + 2)} <   2 ^ {2 n ^ {2} + \frac {3}{2} n + 4} D \log (d A),
$$

and, since again $k^{1 / (4n + 2)} \geqslant h$, this is plainly inconsistent with (12). The contradiction proves the theorem.

## References

1. A. Baker, “Linear forms in the logarithms of algebraic numbers”, Mathematika, 13 (1966), 204–216.

2. ——, “Linear forms in the logarithms of algebraic numbers (II)”, Mathematika, 14 (1967), 102–107.

3. ——, “Linear forms in the logarithms of algebraic numbers (III)”, Mathematika, 14 (1967), 220–228.

4. ——, “Contributions to the theory of Diophantine equations: I. On the representation of integers by binary forms”, Phil. Trans. Royal Soc., A, 263 (1968), 173–191.

5. ——, “Contributions to the theory of Diophantine equations: II. The Diophantine equation  $y^{2} = x^{3} + k$ ”, Phil. Trans. Royal Soc., A, 263 (1968), 193–208.

6. ——, “The Diophantine equation  $y^{2} = ax^{3} + bx^{2} + cx + d$ ”, J. London Math. Soc., 43 (1968), 1–9. Dedicated to Prof. L. J. Mordell on his 80th birthday.

7. ——, “Bounds for the solutions of the hyperelliptic equation”, Proc. Cambridge Phil. Soc. To appear.

Trinity College,
Cambridge.