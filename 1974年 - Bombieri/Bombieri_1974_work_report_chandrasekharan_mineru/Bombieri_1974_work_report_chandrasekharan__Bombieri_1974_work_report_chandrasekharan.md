made in later years by H. Rademacher, T. Estermann, G. Ricci, and A. A. Buchstab; until Atle Selberg, during the years 1946—1951, developed a sieve method more general and more powerful than Brun's and its improved versions.

We are here concerned, however, with the method of the large sieve, which is different from the small sieves of Brun and of Selberg, and which, when combined with analytical arguments, yields results that are beyond the reach of the other sieves.

The idea of the large sieve originated with Yu. V. Linnik in 1941, in his attempt to tackle I. M. Vinogradov's hypothesis (which is yet to be proved or disproved) on $h_2(p)$, the least quadratic nonresidue modulo $p$. The hypothesis is that given $\varepsilon > 0$, there exists a constant $c = c(\varepsilon)$ such that $h_2(p) < cp^\varepsilon$. Linnik sought to estimate the number of primes $p \leq x$, say, for which $h_2(p) > p^\varepsilon$, for any given $\varepsilon > 0$.

Let $n_1, n_2, \cdots, n_Z$ be $Z$ integers, such that $M + 1 \leq n_1 < n_2 < \cdots < n_Z \leq M + N$. Let the prime $p$ be called exceptional, if the number of residue classes not represented by the numbers $(n_j), j = 1, 2, \cdots, Z$, is greater than $\tau p$, where $\tau$ is a fixed number such that $0 < \tau < 1$. Linnik proved that for any such sequence $(n_j)$, the number of exceptional primes $p \leq N^{1/2}$ does not exceed $c_1 N / \tau^2 Z$, where $c_1$ is an absolute constant. As an application, he proved the striking theorem that the number of primes $p \leq N$ for which the least quadratic nonresidue is greater than $N^\epsilon$, for a fixed number $\varepsilon > 0$, is bounded. It follows that the number of primes $p \leq X$ for which the least quadratic nonresidue is greater than $p^\epsilon$ is $\ll \log \log X$.

In the context of the definition of a sieve, the sequence  $(n_{j}), j = 1, 2, \cdots, Z$ , may be looked upon as the sequence of elements left over in the interval  $[M + 1, M + N]$ , after a sieving has been effected (on the sequence of all integers in that interval, for example), with a sieving set  $\{\Omega_{p}\}$  of residue classes modulo  $p, p \leq N^{1/2}$ , which has the property that for each exceptional  $p \leq N^{1/2}$ , the corresponding  $\Omega_{p}$  has more than  $\tau p$  elements. Hence the name large sieve.

The next important step was taken by A. Rényi. If  $Z(p, a)$  denotes the number of elements in the given sequence  $(n_j)$  such that  $n_j = a \pmod{p}$ , Linnik's result takes the form: The number of primes  $p \leq N^{1/2}$  such that  $Z(p, a) = 0$  for at least  $\tau p$  values of a, where  $0 < \tau < 1$ , does not exceed

$$
c _ {1} N / \tau^ {2} Z.
$$

Rényi considered instead the sum

$$
S _ {X} = \sum_ {p \leq X} p \sum_ {a = 0} ^ {p - 1} (Z (p, a) - Z / p) ^ {2},
$$

and proved in 1950 that

$$
S _ {X} \leq 2 N Z, \quad \text { for } X = (N / 1 2) ^ {1 / 3}.\tag{2}
$$

Again, in the context of the definition of a sieve, we have $Z(p, a) = 0$ if $a \in \Omega_p$, so that

$$
S _ {X} \geq \sum_ {p \leq X} \frac {| \Omega_ {p} |}{p} Z ^ {2},
$$

which, when combined with (2), gives an upper bound for $Z$ — and also Linnik's result provided that $X = N^{1/2}$.

As an application of his inequality, Rényi proved the striking theorem that every sufficiently large even integer is the sum of a prime and an almost prime (that is, an integer which is the product of a bounded number of prime factors).

Though Rényi's inequality yields more precise information than Linnik's result for the range of primes  $p \ll N^{1/3}$ , it does not work for the wider range  $p \ll N^{1/2}$  of Linnik, which is more appropriate in the context of arithmetical applications. This defect was sought to be repaired by many mathematicians. It was not until 1965, however, that important further progress was made by K. F. Roth (Mathematika 12 (1965), 1–9) and, independently, by Bombieri (Mathematika 12 (1965), 201–225). Roth proved that Rényi's inequality (2) holds for  $X = (N/\log N)^{1/2}$ , and Bombieri that it holds for  $X = N^{1/2}$  (with  $\ll$  in place of  $\leqslant$ ).

Bombieri proceeded to place Rényi's inequality in a more general setting and proved, by a simple and ingenious argument, an inequality for trigonometrical double sums, which is as follows: Let  $x_{1}, x_{2}, \cdots, x_{R}$  be real numbers which are  $\delta$ -well-spaced, in the sense that  $\|x_{k} - x_{l}\| \geq \delta > 0$  for  $k \neq l$  (where  $\|\theta\|$ , for any real  $\theta$ , denotes the distance of  $\theta$  from the nearest integer). Let  $T(x) = \sum_{n=M+1}^{M+N} a_{n} e^{2\pi i n x}$ , where the  $(a_{n})$  are complex numbers. Then

$$
\sum_ {k = 1} ^ {R} \left| T (x _ {k}) \right| ^ {2} \leq \left(N + \frac {2}{\delta}\right) \sum_ {n = M + 1} ^ {M + N} \left| a _ {n} \right| ^ {2}\tag{3}
$$

(Acta Arith. 18 (1971), 401–404; Proc. Internat. Conf. Number Theory, Moscow, 1971). This corresponds, as Bombieri has shown, to something like Bessel's inequality in a Hilbert space.

If we take $x_{k}$ to be rational, $x_{k} = a / q$, say, where $(a, q) = 1$, $q \leq Q$, with $a_{n} = 1$ for $n = n_{j}$ and $a_{n} = 0$ for $n \neq n_{j}$, we get (more than) Rényi's inequality (2) in case $q$ is a prime, and something similar to the inequality given by Selberg's upper-bound sieve, in case $q$ is composite.

Thus many results previously obtained by Selberg's method can now be proved by using (3).

Bombieri then considered the analogue of his large-sieve inequality (3) for sums of Dirichlet characters  $\chi$  modulo q instead of trigonometrical sums. The connecting link is the Gaussian sum

$$
G (\chi) = \sum_ {a = 1} ^ {q} \chi (a) \exp (2 \pi i a / q),
$$

since

$$
\begin{array}{r l} \sum_ {\chi} \big | G (\chi) \big | ^ {2}   \chi (m) \overline {{\chi (n)}} = \varphi (q) S _ {m - n, q}, & \text { if } (m n, q) = 0, \\ = 0, & \text { if } (m n, q) > 1, \end{array}
$$

where

$$
S _ {m, q} = \sum_ {a = 1; (a, q) = 1} ^ {q} \exp (2 \pi i a m / q)
$$

is the well-known Ramanujan sum (not to be confused with  $S_{X}$  in (2)).

Vital for Bombieri's proof of his theorem on arithmetical progressions is the following inequality: Let $Q$ be any finite set of positive integers, $(a_n)$ any complex numbers. Then

$$
\sum_ {q \in Q} \frac {1}{\varphi (q)} \sum_ {\chi} | G (\chi) | ^ {2} \cdot \left| \sum_ {X <   n \leq Y} \chi (n) a _ {n} \right| ^ {2} \leq 7 D \max (Y - X, M ^ {2}) \sum_ {X <   n \leq Y} d (n) | a _ {n} | ^ {2}.\tag{4}
$$

Here $\sum_{\chi}$ denotes summation over all characters $\chi$ modulo $q, d(n)$ denotes the divisor function, $D = D(q) = \max_{q \in Q} d(q)$, $M = M(Q) = \max_{q \in Q} q$.

By skilful and repeated application of this inequality, with different choices of X, Y, and  $a_{n}$ , Bombieri deduced a new type of density theorem for the zeros of L-functions. The theorem gives an estimate for the sum

$$
\sum_ {q \in Q} \frac {1}{\varphi (q)} \sum_ {\chi} | G (\chi) | ^ {2} N (\alpha , T; \chi),
$$

which is uniform with respect to $Q$, for $\frac{1}{2} \leq \alpha \leq 1$, $T \geq 2$. Here $N(\alpha, T; \chi)$ denotes the number of zeros of Dirichlet's function $L(s, \chi)$ in the rectangle $\alpha \leq \operatorname{Re}s \leq 1$, $\frac{1}{2} \leq \alpha \leq 1$, $|\operatorname{Im}s| \leq T$, in the complex $s$-plane.

From his density theorem Bombieri deduced his theorem on primes in arithmetical progressions, by an appeal to classical arguments in the theory of L-functions, combined with an application of the Siegel-Walfisz theorem (stated at the beginning).

Bombieri's work has given rise to a general method for treating problems that were previously solved either on the assumption of the extended Riemann hypothesis, or by Linnik's 'dispersion method', or by highly complicated, ad hoc methods. It thus furnishes a new approach to such important results as I. M. Vinogradov's theorem (1937) that every sufficiently large odd integer is a sum of three primes, or Linnik's theorem (1961) that every sufficiently large integer is a sum of a prime and two squares, or Chen's result (1967) that every sufficiently large even integer is a sum of a prime and an integer with at most two prime factors. Bombieri's theorem represents a deep synthesis of the most important modern methods in prime number theory. It has not put an end to any one question; rather it has led to many new ones.

His inequality for sums of Dirichlet characters has been extended to general multiplicative characters of the form $\chi(n)n^{it}$ which are “$\delta$-well-spaced”. In consequence, the best bounds so far known have been obtained for $N(\alpha, T; \chi)$, yielding as special cases such results as the following: The difference between the consecutive primes $p_{n+1}$, $p_n$ has the estimate $p_{n+1} - p_n \ll p_n^{7/12+\varepsilon}$, for every $\varepsilon > 0$. (It is known that the Riemann hypothesis implies this with the exponent 1/2 in place of 7/12.) The “density hypothesis” $N(\alpha, T; \chi_0) \ll T^{2(1-\alpha)+\varepsilon}$ holds for $\alpha > 13/16$. (Here $\chi_0$ is the principal character, so that the zeros are those of Riemann's zeta-function.) Bombieri's method has also been generalized to algebraic number fields. Many mathematicians have played a part in the development of his method—H. Davenport, H. Halberstam, P. X. Gallagher, H. L. Montgomery,

G. Halász, M. N. Huxley, M. Jutila and, more recently, M. Forti and C. Viola, to mention but a few. There is little doubt that Bombieri's theorems have inspired that development.

2. Univalent functions and the local Bieberbach conjecture. Bombieri's work on the local validity of the Bieberbach conjecture is an impressive achievement in an altogether different branch of mathematics. It shows his power and ingenuity in attacking problems of 'hard analysis'.

Let S denote the family of functions  $f(z) = z + a_{2}z^{2} + a_{3}z^{3} + \cdots$  which are (normalized) holomorphic and univalent in the unit disc  $|z| < 1$ . Bieberbach's conjecture is that if  $f(z) \in \mathcal{S}$ , then  $\operatorname{Re} a_{n} \leq n$ , with the equality holding only if  $f(z) = z/(1 - \rho z)^{2}$ , and  $\rho^{n-1} = 1$ . The conjecture has so far been proved for  $2 \leq n \leq 6$  on the one hand, and for a large number of subfamilies of S on the other.

In 1965 P. R. Garabedian and M. Schiffer raised the question of the local validity of that conjecture, that is: If $2 - \operatorname{Re} a_2$ is small enough, is it true that $n - \operatorname{Re} a_n$ is nonnegative? They answered it in the affirmative if $n$ is even. They proved the existence of a positive constant $\varepsilon_{2m}$, say, such that if $|2 - a_2| < \varepsilon_{2m}$, then $\operatorname{Re} a_{2m} \leq 2m$, with the equality holding if and only if $f(z) = z(1 - z)^{-2} = \sum_{n=1}^{\infty} nz^n$, the Koebe function.

Bombieri proved this in 1967 for all n, odd as well as even, the case of n odd being the more difficult (Invent. Math. 4 (1967), 26–67). To be precise, he proved that

$$
\liminf _ {a _ {2} \to 2} \frac {n - \operatorname{Re} a _ {n}}{2 - \operatorname{Re} a _ {2}} > 0, \quad \text { if   } n \text {   is   even },
$$

and

$$
\liminf _ {a _ {3} \to 3} \frac {n - \operatorname{Re} a _ {n}}{3 - \operatorname{Re} a _ {3}} > 0, \quad \text { if   } n \text {   is   odd },
$$

where the 'lim inf' is taken over all functions of the family S.

An independent, though less direct, proof of this has since been published by Garabedian and Schiffer (Arch. Rational Mech. Anal. 26 (1967), 1–32).

Bombieri's proof is based on an ingenious combination of K. Löwner's 'parametric method' with the theory of the 'second variation' developed by P. L. Duren and M. Schiffer. He uses the results of A. C. Schaefer and D. C. Spencer on Löwner curves, as well as an earlier result of his own concerning a set of quadratic forms  $(Q_{n})$ , in an infinite number of variables, which had been encountered by Duren and Schiffer in their theory of the second variation. These quadratic forms  $Q_{n}$  have the property that: (a) if  $Q_{n}$  is an indefinite form, then Bieberbach's conjecture is false for that n; (b) if  $Q_{n}$  is positive definite, then every analytic variation of the Koebe function decreases Re  $a_{n}$ . Duren and Schiffer proved (1962/63) that  $Q_{n}$  is positive definite for  $n = 2, 3, \cdots, 9$ , and the same was checked with a computer for all  $n \leq 100$ . Bombieri proved that  $Q_{n}$  is positive definite for all n (Boll. Un. Mat. Ital. (3) 22 (1967), 25–32).

3. Several complex variables. Bombieri's theorem concerning algebraic values of meromorphic maps (Invent. Math. 10 (1970), 267–287; 11 (1970), 163–166), moti-