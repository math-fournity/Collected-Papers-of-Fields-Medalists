An Elementary Proof of the Prime-Number Theorem
Author(s): Atle Selberg
Source: Annals of Mathematics, Second Series, Vol. 50, No. 2 (Apr., 1949), pp. 305-313
Published by: Annals of Mathematics
Stable URL: http://www.jstor.org/stable/1969455
Accessed: 04/02/2014 11:21

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# AN ELEMENTARY PROOF OF THE PRIME-NUMBER THEOREM

ATLE SELBERG

(Received October 14, 1948)

## 1. Introduction

In this paper will be given a new proof of the prime-number theorem, which is elementary in the sense that it uses practically no analysis, except the simplest properties of the logarithm.

We shall prove the prime-number theorem in the form

$$
\lim _ {x \rightarrow \infty} \frac {\vartheta (x)}{x} = 1\tag{1.1}
$$

where for $x > 0$, $\vartheta(x)$ is defined as usual by

$$
\vartheta (x) = \sum_ {\boldsymbol {p} \leq x} \log p,\tag{1.2}
$$

p denoting the primes.

The basic new thing in the proof is a certain asymptotic formula (2.8), which may be written

$$
\vartheta (x) \log x + \sum_ {\boldsymbol {p} \leq x} \log p \vartheta \left(\frac {x}{p}\right) = 2 x \log x + O (x).\tag{1.3}
$$

From this formula there are several ways to deduce the prime-number theorem. The way I present §§2–4 of this paper, is chosen because it seems at the present to be the most direct and most elementary way. $^{1}$  But for completeness it has to be mentioned that this was not my first proof. The original proof was in fact rather different, and made use of the following result by P. Erdős, that for an arbitrary, positive fixed number  $\delta$ , there exist a  $K(\delta) > 0$  and an  $x_{0} = x_{0}(\delta)$  such that for  $x > x_{0}$ , there are more than

$$
K (\delta) x / \log x
$$

primes in the interval from $x$ to $x + \delta x$.

My first proof then ran as follows: Introducing the notations

$$
\underline {{\lim}} \frac {\vartheta (x)}{x} = a, \quad \overline {{\lim}} \frac {\vartheta (x)}{x} = A,
$$

one can easily deduce from (1.3), using the well-known result

$$
\sum_ {\boldsymbol {p} \leq x} \frac {\log p}{x} = \log x + O (1),\tag{1.4}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Because it avoids the concept of lower and upper limit. It is in fact easy to modify the proof in a few places so as to avoid the concept of limit at all, of course (1.1) would then have to be stated differently.</span></small>

that

$$
a + A = 2.\tag{1.5}
$$

Next, taking a large $x$, with

$$
\vartheta (x) = a x + o (x),
$$

one can deduce from (1.3) in the modified form

$$
(\vartheta (x) - a x) \log x + \sum_ {p \leq x} \log p \left(\vartheta \left(\frac {x}{p}\right) - A \frac {x}{p}\right) = O (x),\tag{1.6}
$$

that, for a fixed positive number $\delta$, one has

$$
\vartheta \left(\frac {x}{p}\right) > (A - \delta) \frac {x}{p},\tag{1.7}
$$

except for an exceptional set of primes $\leq x$ with

$$
\sum \frac {\log p}{p} = o (\log x).
$$

Also one easily deduces that there exists an $x'$ in the range $\sqrt{x} < x' < x$, wit

$$
\vartheta (x ^ {\prime}) = A x ^ {\prime} + o (x ^ {\prime}).
$$

Again from (1.6) with $a$ and $A$ interchanged, and $x'$ instead of $x$, one deduces that

$$
\vartheta \left(\frac {x ^ {\prime}}{p}\right) <   (a + \delta) \frac {x ^ {\prime}}{p},\tag{1.8}
$$

except for an exceptional set of primes $\leq x'$ with

$$
\sum \frac {\log p}{p} = o (\log x).
$$

From Erdős' result it is then possible to show that one can chose primes $p$ and $p'$ not belonging to any of the exceptional sets, with

$$
\frac {x}{p} <   \frac {x ^ {\prime}}{p ^ {\prime}} <   (1 + \delta) \frac {x}{p}.
$$

Then we get from (1.7) and (1.8) that

$$
(A - \delta) \frac {x}{p} <   \vartheta \left(\frac {x}{p}\right) \leq \vartheta \left(\frac {x ^ {\prime}}{p ^ {\prime}}\right) <   (a + \delta) \frac {x ^ {\prime}}{p ^ {\prime}} <   (a + \delta) (1 + \delta) \frac {x}{p},
$$

so that

$$
A - \delta <   (a + \delta) (1 + \delta).
$$

or making $\delta$ tend to zero

$$
A \leq a.
$$

Hence since also $A \geq a$ and $a + A = 2$ we have $a = A = 1$, which proves our theorem.

Erdős' result was obtained without knowledge of my work, except that it is based on my formula (2.8); and after I had the other parts of the above proof. His proof contains ideas related to those in the above proof, at which related ideas he had arrived independently.

The method can be applied also to more general problems. For instance one can prove some theorems proved by analytical means by Beurling, but the results are not quite as sharp as Beurlings. $^{2}$  Also one can prove the prime-number theorem for arithmetic progressions, one has then to use in addition ideas and results from my previous paper on Dirichlets theorem. $^{3}$

Of known results we use frequently besides (1.4) also its consequence

$$
\vartheta (x) = O (x).\tag{1.9}
$$

Throughout the paper p, q and r denote prime numbers.  $\mu(n)$  denotes Möbius' number-theoretic function,  $\tau(n)$  denotes the number of divisors of n. The letter c will be used to denote absolute constants, and K to denote absolute positive constants. Some of the more trivial estimations are not carried out but left to the reader.

## 2. Proof of the basic formulas

We write, when x is a positive number and d a positive integer,

$$
\lambda_ {d} = \lambda_ {d, x} = \mu (d) \log^ {2} \frac {x}{d},\tag{2.1}
$$

and if $n$ is a positive integer,

$$
\theta_ {n} = \theta_ {n, x} = \sum_ {d / n} \lambda_ {d}.\tag{2.2}
$$

Then we have

$$
\theta_ {n} = \left\{ \begin{array}{l} \log^ {2} x, \text {   for   } n = 1, \\ \log p \log x ^ {2} / p, \text {   for   } n = p ^ {\alpha}, \alpha \geq 1, \\ 2 \log p \log q, \text {   for   } n = p ^ {\alpha} q ^ {\beta}, \alpha \geq 1, \beta \geq 1, \\ 0, \text {   for   all   other   } n. \end{array} \right.\tag{2.3}
$$

The first three of these statements follow readily from (2.2) and (2.1), the fourth is easily proved by induction. Clearly it is enough to consider n square-free, then if  $n = p_{1}p_{2} \cdots p_{k}$ ,

$$
\theta_ {n, x} = \theta_ {n / p _ {k}, x} - \theta_ {n / p _ {k}, x / p _ {k}}.
$$

From this the remaining part of (2.3) follows.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{2}$  A. BEURLING: Analyse de la loi asymptotique de la distribution des nombres premiers généralisés, Acta Math., vol. 68, pp. 255–291 (1937).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{3}$  These Annals this issue, pp. 297–304.</span></small>

Now consider the expression

$$
\begin{array}{l} \sum_ {n \leq x} \theta_ {n} = \sum_ {n \leq x} \sum_ {d / n} \lambda_ {d} = \sum_ {d \leq x} \lambda_ {d} \left[ \frac {x}{d} \right] = x \sum_ {d \leq x} \frac {\lambda_ {d}}{d} + O \left(\sum_ {d \leq x} | \lambda_ {d} |\right) \\ = x \sum_ {d \leq x} \frac {\mu (d)}{d} \log^ {2} \frac {x}{d} + O \left(\sum_ {d \leq x} \log^ {2} \frac {x}{d}\right) = x \sum_ {d \leq x} \frac {\mu (d)}{d} \log^ {2} \frac {x}{d} + O (x). \end{array}\tag{2.4}
$$

This on the other hand is equal to, by (2.3),

$$
\begin{array}{l} \sum_ {n \leq x} \theta_ {n} = \log^ {2} x + \sum_ {\boldsymbol {p} ^ {\alpha} \leq x} \log p \log \frac {x ^ {2}}{p} \\ \qquad + 2 \sum_ {\substack {\boldsymbol {p} ^ {\alpha} q ^ {\beta} \leq x \\ \boldsymbol {p} <   q}} \log p \log q = \sum_ {\boldsymbol {p} \leq x} \log^ {2} p \\ \qquad + \sum_ {\boldsymbol {p} q \leq x} \log p \log q + O \left(\sum_ {\boldsymbol {p} \leq x} \log p \log \frac {x}{p}\right) \\ \qquad + O \left(\sum_ {\substack {\boldsymbol {p} ^ {\alpha} \leq x \\ \alpha > 1}} \log^ {2} x\right) + O \left(\sum_ {\substack {\boldsymbol {p} ^ {\alpha} q ^ {\beta} \leq x \\ \alpha > 1}} \log p \log q\right) \\ \qquad + \log^ {2} x = \sum_ {\boldsymbol {p} \leq x} \log^ {2} p + \sum_ {\boldsymbol {p} q \leq x} \log p \log q + O (x). \end{array}\tag{2.5}
$$

The remainder term being obtained by use of (1.4) and (1.9). Hence from (2.4) and (2.5),

$$
\sum_ {\boldsymbol {p} \leq x} \log^ {2} p + \sum_ {\boldsymbol {p q} \leq x} \log p \log q = x \sum_ {d \leq x} \frac {\mu (d)}{d} \log^ {2} \frac {x}{d} + O (x).\tag{2.6}
$$

It remains now to estimate the sum on the right-hand-side. To this purpose we need the formulas

$$
\sum_ {\nu \leq z} \frac {1}{\nu} = \log z + c _ {1} + O (z ^ {- \frac {1}{4}}),\tag{2.7}
$$

and

$$
\sum_ {\nu \leq z} \frac {\tau (\nu)}{\nu} = \frac {1}{2} \log^ {2} z + c _ {2} \log z + c _ {3} + O (z ^ {- \frac {1}{4}})\tag{2.7'}
$$

where the c's are absolute constants, (2.7) is well known, and  $(2.7')$  may be easily derived by partial summation from the well-known result

$$
\sum_ {\nu \leq z} \tau (\nu) = z \log z + c _ {4} z + O (\sqrt {z}).
$$

From (2.7) and $(2.7')$ we get

$$
\log^ {2} z = 2 \sum_ {\nu \leq z} \frac {\tau (\nu)}{\nu} + c _ {5} \sum_ {\nu \leq z} \frac {1}{\nu} + c _ {6} + O (z ^ {- \frac {1}{4}}).
$$

By taking here $z = x / d$, we get

$$
\begin{array}{r l} \sum_ {d \leq x} \frac {\mu (d)}{d} \log^ {2} \frac {x}{d} & = 2 \sum_ {d \leq x} \frac {\mu (d)}{d} \sum_ {\nu \leq x / d} \frac {\tau (\nu)}{\nu} + c _ {5} \sum_ {d \leq x} \frac {\mu (d)}{d} \sum_ {\nu \leq x / d} \frac {1}{\nu} \\ & + c _ {6} \sum_ {d \leq x} \frac {\mu (d)}{d} + O (x ^ {- \frac {1}{4}} \sum_ {d \leq x} d ^ {- \frac {3}{4}}) = 2 \sum_ {d \nu \leq x} \frac {\mu (d) \tau (\nu)}{d \nu} \\ & + c _ {5} \sum_ {d \nu \leq x} \frac {\mu (d)}{d \nu} + c _ {6} \sum_ {d \leq x} \frac {\mu (d)}{d} + O (1) \\ & = 2 \sum_ {n \leq x} \frac {1}{n} \sum_ {d / n} \mu (d) \tau \left(\frac {n}{d}\right) + c _ {5} \sum_ {n \leq x} \frac {1}{n} \sum_ {d / n} \mu (d) \\ & + O (1) = 2 \sum_ {n \leq x} \frac {1}{n} + c _ {5} + O (1) = 2 \log x + O (1). \end{array}
$$

We used here that $\sum_{d/n} \mu(d) \tau(n/d) = 1$, and the well-known $\sum_{d \leq x} (\mu(d)) / d = O(1)$. Now (2.6) yields

$$
\sum_ {\boldsymbol {p} \leq x} \log^ {2} p + \sum_ {\boldsymbol {p q} \leq x} \log p \log q = 2 x \log x + O (x).\tag{2.8}
$$

This formula may also be written in the form given in the introduction

$$
\vartheta (x) \log x + \sum_ {p \leq x} \log p \vartheta \left(\frac {x}{p}\right) = 2 x \log x + O (x),\tag{2.9}
$$

by noticing that

$$
\sum_ {\boldsymbol {p} \leq x} \log^ {2} p = \vartheta (x) \log x + O (x).
$$

By partial summation we get from (2.8)

$$
\sum_ {\boldsymbol {p} \leq x} \log p + \sum_ {\boldsymbol {p q} \leq x} \frac {\log p \log q}{\log p q} = 2 x + O \left(\frac {x}{\log x}\right).\tag{2.10}
$$

This gives

$$
\sum_ {\boldsymbol {p} \boldsymbol {q} \leq \boldsymbol {x}} \log p \log q = \sum_ {\boldsymbol {p} \leq \boldsymbol {x}} \log p \sum_ {\boldsymbol {q} \leq \boldsymbol {x} / \boldsymbol {p}} \log q = 2 x \sum_ {\boldsymbol {p} \leq \boldsymbol {x}} \frac {\log p}{p}
$$

$$
\begin{array}{l} - \sum_ {\boldsymbol {p} \leq x} \log p \sum_ {q r \leq x / \boldsymbol {p}} \frac {\log q \log r}{\log q r} + O \left(x \sum_ {p \leq x} \frac {\log p}{p \left(1 + \log \frac {x}{p}\right)}\right) \\ = 2 x \log x - \sum_ {q r \leq x} \frac {\log q \log r}{\log q r} \vartheta \left(\frac {x}{q r}\right) + O (x \log \log x). \end{array}
$$

Inserting this for the second term in (2.8) we get

$$
\vartheta (x) \log x = \sum_ {p q \leq x} \frac {\log p \log q}{\log p q} \vartheta \left(\frac {x}{p q}\right) + O (x \log \log x).\tag{2.11}
$$

Writing now

$$
\vartheta (x) = x + R (x)
$$

, (2.9) easily gives

$$
R (x) \log x = - \sum_ {p \leq x} \log p R \left(\frac {x}{p}\right) + O (x),\tag{2.12}
$$

and (2.11) yields in the same manner

$$
R (x) \log x = \sum_ {p q \leq x} \frac {\log p \log q}{\log p q} R \left(\frac {x}{p q}\right) + O (x \log \log x),\tag{2.13}
$$

since

$$
\sum_ {p q \leq x} \frac {\log p \log q}{p q \log p q} = \log x + O (\log \log x),
$$

which follows by partial summation from

$$
\sum_ {p q \leq x} \frac {\log p \log q}{p q} = \frac {1}{2} \log^ {2} x + O (\log x),
$$

which again follows easily from (1.4).

The (2.12) and (2.13) yield

$$
\begin{array}{l} 2 \mid R (x) \mid \log x \leq \sum_ {p \leq x} \log p \left| R \left(\frac {x}{p}\right) \right| \\ \qquad + \sum_ {p q \leq x} \frac {\log p \log q}{\log p q} \left| R \left(\frac {x}{p q}\right) \right| + O (x \log \log x). \end{array}
$$

From this, by partial summation,

$$
\begin{array}{r l} 2 \mid R (x) \mid \log x & \leq \sum_ {n \leq x} \left\{\sum_ {p \leq n} \log p + \sum_ {p q \leq n} \frac {\log p \log q}{\log p q} \right\} \\ & \quad \cdot \left\{\left| R \left(\frac {x}{n}\right) \right| - \left| R \left(\frac {x}{n + 1}\right) \right| \right\} + O (x \log \log x), \end{array}
$$

or by (2.10)

$$
\begin{array}{l} 2 \mid R (x) \mid \log x \leqq 2 \sum_ {n \leq x} n \left\{\left| R \left(\frac {x}{n}\right) \right| - \left| R \left(\frac {x}{n + 1}\right) \right| \right\} \\ \quad + O \left(\sum_ {n \leq x} \frac {n}{1 + \log n} \left| R \left(\frac {x}{n}\right) - R \left(\frac {x}{n + 1}\right) \right|\right) + O (x \log \log x) \\ \quad = 2 \sum_ {n \leq x} \left| R \left(\frac {x}{n}\right) \right| + O \left(\sum_ {n \leq x} \frac {n}{1 + \log n} \left\{\vartheta \left(\frac {x}{n}\right) - \vartheta \left(\frac {x}{n + 1}\right) \right\}\right) \\ \quad + O \left(x \sum_ {n \leq x} \frac {1}{n (1 + \log n)}\right) + O (x \log \log x) = 2 \sum_ {n \leq x} \left| R \left(\frac {x}{n}\right) \right| \\ \quad + O \left(\sum_ {n \leq x} \frac {1}{1 + \log n}   \vartheta \left(\frac {x}{n}\right)\right) + O (x \log \log x) \\ \quad = 2 \sum_ {n \leq x} \left| R \left(\frac {x}{n}\right) \right| + O (x \log \log x), \end{array}
$$

or

$$
\mid R (x) \mid \leq \frac {1}{\log x} \sum_ {n \leq x} \left| R \left(\frac {x}{n}\right) \right| + O \left(x \frac {\log \log x}{\log x}\right),\tag{2.14}
$$

which is the result we will use in the following. $^{4}$

## 3. Some properties of $R(x)$

From (1.4) we get by partial summation that

$$
\sum_ {n \leq x} \frac {\vartheta (n)}{n ^ {2}} = \log x + O (1),
$$

or

$$
\sum_ {n \leq x} \frac {R (n)}{n ^ {2}} = O (1).
$$

This means there exists an absolute positive constant  $K_{1}$ , so that for all x > 4 and  $x' > x$ ,

$$
\left| \sum_ {x \leq n \leq x ^ {\prime}} \frac {R (n)}{n ^ {2}} \right| <   K _ {1}.\tag{3.1}
$$

Accordingly we have, if $R(n)$ does not change its sign between $x$ and $x'$, that there is a $y$ in the interval $x \leq y \leq x'$, so that

$$
\left| \frac {R (y)}{y} \right| <   \frac {K _ {2}}{\log \frac {x ^ {\prime}}{x}}, \quad K _ {2} \geq 1.\tag{3.2}
$$

This is easily seen to hold true if  $R(n)$  changes the sign also. $^{5}$

Thus for an arbitrary fixed positive $\delta < 1$ and $x > 4$, there will exist a $y$ in the interval $x \leq y \leq e^{\kappa_2 / \delta} x$, with

$$
\mid R (y) \mid <   \delta y.\tag{3.3}
$$

From (2.10) we see that for $y < y'$,

$$
0 \leq \sum_ {y <   p \leq y ^ {\prime}} \log p \leq 2 (y ^ {\prime} - y) + O \left(\frac {y ^ {\prime}}{\log y ^ {\prime}}\right),
$$

from which follows that

$$
\mid R (y ^ {\prime}) - R (y) \mid \leq y ^ {\prime} - y + O \left(\frac {y ^ {\prime}}{\log y ^ {\prime}}\right).
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{4}$  Apparently we have here lost something in the order of the remainder-term compared to (2.8). Actually we could instead of (2.14) have used the inequality</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">which can be proved in a similar way.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$|R(y)| < \log y.$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\left|R(x)\right| \leqslant \frac{2}{\log^2 x} \sum_{n \leqslant x} \frac{\log n}{n} \left|R\left(\frac{x}{n}\right)\right| + O\left(\frac{x}{\log x}\right),$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{5}$  Because there will then be a  $|R(y)| < \log y$ .</span></small>

Hence, if $y / 2 \leq y' \leq 2y, y > 4$,

$$
\mid R (y ^ {\prime}) - R (y) \mid \leq \mid y ^ {\prime} - y \mid + O \left(\frac {y ^ {\prime}}{\log y ^ {\prime}}\right),
$$

or

$$
\mid R (y ^ {\prime}) \mid \leq \mid R (y) \mid + \mid y ^ {\prime} - y) + O \left(\frac {y ^ {\prime}}{\log y ^ {\prime}}\right).
$$

Now consider an interval  $(x, e^{\kappa_{2}/\delta} x)$ , according to (3.3) there exists a y in this interval with

$$
\mid R (y) \mid <   \delta y.
$$

Thus for any $y'$ in the interval $y / 2 \leq y' \leq 2y$, we have

$$
\mid R (y ^ {\prime}) \mid \leq \delta y + \mid y ^ {\prime} - y \mid + \frac {K _ {3} y ^ {\prime}}{\log x},
$$

or

$$
\left| \frac {R (y ^ {\prime})}{y ^ {\prime}} \right| <   2 \delta + \left| 1 - \frac {y ^ {\prime}}{y} \right| + \frac {K _ {3}}{\log x}.
$$

Hence if $x > e^{\kappa_3 / \delta}$ and $e^{-(\delta / 2)} \leq y' / y \leq e^{\delta / 2}$, we get

$$
\left| \frac {R (y ^ {\prime})}{y ^ {\prime}} \right| <   2 \delta + (e ^ {\delta / 2} - 1) + \delta <   4 \delta .
$$

Thus for $x > e^{\kappa_2 / \delta}$ the interval $(x, e^{\kappa_2 / \delta}x)$ will always contain a sub-interval $(y_1, e^{\delta / 2}y_1)$, such that $|R(z)| < 4\delta z$ if $z$ belongs to this sub-interval.

## 4. Proof of the prime-number theorem

We are now going to prove the

THEOREM.

$$
\lim _ {x \rightarrow \infty} \frac {\vartheta (x)}{x} = 1.
$$

Obviously this is equivalent to

$$
\lim _ {x \rightarrow \infty} \frac {R (x)}{x} = 0.\tag{4.1}
$$

We know that for $x > 1$,

$$
\mid R (x) \mid <   K _ {4} x.\tag{4.2}
$$

Now assume that for some positive number $\alpha < 8$,

$$
\mid R (x) \mid <   \alpha x,\tag{4.3}
$$

holds for all $x > x_0$. Taking $\delta = \alpha / 8$, we have according to the preceding

section (since we may assume that $x_0 > e^{\kappa_3 / \delta}$), that all intervals of the type $(x, e^{\kappa_2 / \delta}x)$ with $x > x_0$, contain an interval $(y, e^{\delta / 2}y)$ such that

$$
\mid R (z) \mid <   \alpha z / 2,\tag{4.4}
$$

for $y \leq z \leq e^{\delta / 2} y$.

The inequality (2.14) then gives, using (4.2),

$$
\begin{array}{l} \mid R (x) \mid \leq \frac {1}{\log x} \sum_ {n \leq x} \left| R \left(\frac {x}{n}\right) \right| + O \left(\frac {x}{\sqrt {\log x}}\right) \\ <   K _ {4} \frac {x}{\log x} \sum_ {(x / x _ {0}) <   n \leq x} \frac {1}{n} + \frac {x}{\log x} \sum_ {n \leq (x / x _ {0})} \frac {1}{n} \left| \frac {n}{x} R \left(\frac {x}{n}\right) \right| + O \left(\frac {x}{\sqrt {\log x}}\right), \end{array}
$$

writing now $\rho = e^{\kappa_2 / \delta}$, we get further, using (4.3) and (4.4),

$$
\begin{array}{l} | R (x) | <   \frac {\alpha x}{\log x} \sum_ {n \leq (x / x _ {0})} \frac {1}{n} - \frac {\alpha x}{2 \log x} \sum_ {1 \leq \nu \leq (\log (x / x _ {0}) / \log \rho)} \\ \sum_ {\substack {y _ {\nu} \leq n \leq y _ {\nu} e ^ {(\delta / 2)} \\ \rho^ {\nu - 1} <   y _ {\nu} \leq \rho^ {\nu} e ^ {- (\delta / 2)}}} \frac {1}{n} + O \left(\frac {x}{\sqrt {\log x}}\right) = \alpha x - \frac {\alpha x}{2 \log x} \sum_ {1 \leq \nu \leq (\log (x / x _ {0}) / \log \rho)} \frac {\delta}{2} \\ + O \left(\frac {x}{\sqrt {\log x}}\right) = \alpha x - \frac {\alpha \delta}{4 \log \rho} x + O \left(\frac {x}{\sqrt {\log x}}\right) \\ = \alpha \left(1 - \frac {\alpha^ {2}}{256K _ {2}}\right) x + O \left(\frac {x}{\sqrt {\log x}}\right) <   \alpha \left(1 - \frac {\alpha^ {2}}{300K _ {2}}\right) x, \end{array}
$$

for $x > x_{1}$. Since the iteration-process

$$
\alpha_ {n + 1} = \alpha_ {n} \left(1 - \frac {\alpha_ {n} ^ {2}}{3 0 0 K _ {2}}\right),
$$

obviously converges to zero if we start for instance with $\alpha_{1} = 4$ (one sees easily that then $\alpha_{n} < K_{5} / \sqrt{n}$), this proves (4.1) and thus our theorem.

FINAL REMARK. As one sees we have actually never used the full force of (2.8) in the proof, we could just as well have used it with the remainder term $o(x \log x)$ instead of $O(x)$. It is not necessary to use the full force of (1.4) either, if we have here the remainder-term $o(\log x)$ but in addition knowing that $\vartheta(x) > Kx$ for $x > 1$ and some positive constant $K$, we can still prove the theorem. However, we have then to make some change in the arguments of §3.

THE INSTITUTE FOR ADVANCED STUDY AND
SYRACUSE UNIVERSITY