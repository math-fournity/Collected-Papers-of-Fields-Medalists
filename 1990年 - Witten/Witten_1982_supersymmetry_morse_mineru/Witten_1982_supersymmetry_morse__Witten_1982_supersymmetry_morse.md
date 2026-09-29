# SUPERSYMMETRY AND MORSE THEORY

EDWARD WITTEN

## Abstract

It is shown that the Morse inequalities can be obtained by consideration of a certain supersymmetric quantum mechanics Hamiltonian. Some of the implications of modern ideas in mathematics for supersymmetric theories are discussed.

## 1. Introduction

Supersymmetry is a relatively recent development in theoretical physics which has attracted considerable interest and has been actively developed in several different directions [17], [18].

A number of concepts in modern mathematics have significant applications to supersymmetric quantum field theory  $[22]$ . Conversely, as we will see in this paper, supersymmetry has some interesting applications in mathematics. The purpose of this paper is to describe some of those applications and to make the notions of “supersymmetric quantum mechanics” and “supersymmetric quantum field theory” accessible to a mathematical audience.

The mathematical applications in §§2 and 3 will be self-contained. However, it may be useful to first make a few remarks about some of the relevant aspects of supersymmetry.

In any quantum field theory, the Hilbert space  $K = K^{+} \oplus K^{-}$ , where  $K^{+}$  and  $K^{-}$  are the spaces of “bosonic” and “fermionic” states respectively. A supersymmetry theory is by definition a theory in which there are (Hermitian) symmetry operators  $Q_{i}, i = 1, \cdots, N$ , which map  $K^{+}$  into  $K^{-}$  and vice-versa.

Let us define the operator  $(-1)^{F}$  which distinguishes  $K^{+}$  from  $K^{-}$  (and counts the number of fermions modulo two). Thus we define  $(-1)^{F}\psi = \psi$  for  $\psi \in K^{+}$ , and  $(-1)^{F}\chi = -\chi$  for  $\chi \in K^{-}$ . The first basic condition which must be satisfied by the supersymmetry operators  $Q_{i}$  is that they each anticommute with  $(-1)^{F}$ :

$$
(- 1) ^ {F} Q _ {i} + Q _ {i} (- 1) ^ {F} = 0.\tag{1}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Received March 26, 1982. Supported in part by the National Science Foundation under Grant No. PHY80-19754. The author would like to thank R. Bott, W. Browder, S. Graffi, J. Milnor, and D. Sullivan for discussions.</span></small>

Second, the supersymmetry operators, like any other symmetry operators, must all commute with the Hamiltonian operator H which generates time translations:

$$
Q _ {i} H - H Q _ {i} = 0.\tag{2}
$$

An additional condition is needed to specify the algebraic structure. In supersymmetric quantum mechanics in its simplest form one requires that for any $i$,

$$
Q _ {i} ^ {2} = H,\tag{3}
$$

while for $i \neq j$

$$
Q _ {i} Q _ {j} + Q _ {j} Q _ {i} = 0.\tag{4}
$$

In §2 we will study the supersymmetry algebra in this form.

The above stated algebra must be generalized when one comes to relativistic quantum field theory. The reason for this is that Lorentz transformations relate the Hamiltonian H to the momentum operators which generate spatial translations, so that the algebraic relations (3) and (4) are not compatible with Lorentz invariance. We will restrict ourselves in this paper to the simplest case of a world with one space and one time dimension, so that there is only a single momentum operator P. In the simplest situation there are two supersymmetry operators,  $Q_{1}$  and  $Q_{2}$ , and they satisfy

$$
Q _ {1} ^ {2} = H + P, \quad Q _ {2} ^ {2} = H - P, \quad Q _ {1} Q _ {2} + Q _ {2} Q _ {1} = 0.\tag{5}
$$

From (5) one can deduce (essentially by means of the Jacobi identity) that

$$
[ Q _ {i}, H ] = [ Q _ {i}, P ] = 0.\tag{6}
$$

The algebraic structure (5), which obviously reduces to (3) and (4) if P = 0, is compatible with Lorentz invariance, $^{1}$ but we will make no reference to Lorentz invariance in this paper.

By adding the first two equations in (5), we learn that the Hamiltonian

$$
H = \frac {1}{2} \left(Q _ {1} ^ {2} + Q _ {2} ^ {2}\right)\tag{7}
$$

can be expressed in terms of the  $Q_{i}$  and is positive semi-definite (being a sum of squares of Hermitian operators).

Since $H$ and $P$ are quadratic in the $Q_i$, the fact that the $Q_i$ are odd (equation (1)) implies that $H$ and $P$ are even, $[H, (-1)^F] = [P, (-1)^F] = 0$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$-\frac{1}{2} Q_{2}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$[M,H] = P,[M,P] = H,[M,Q_1] = \frac{1}{2} Q_1,[M,Q_2] =$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(H, P)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$(Q_{1}, Q_{2})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$ In a world with one space and one time dimension, there is a single (anti-Hermitian) generator M of Lorentz transformations. It satisfies  $[M, H] = P$ ,  $[M, P] = H$ ,  $[M, Q_{1}] = \frac{1}{2}Q_{1}$ ,  $[M, Q_{2}] = -\frac{1}{2}Q_{2}$ . These relations, which say that  $(H, P)$  transform like a vector and  $(Q_{1}, Q_{2})$  like a spinor under Lorentz transformations, are compatible with (5).</span></small>

We are now almost ready to understand why it is that modern mathematics has something to say about supersymmetry. The most important question about a supersymmetric theory is the question of whether there exists in the Hilbert space $\mathcal{H}$ a state $|\Omega\rangle$ which is annihilated by the supersymmetry operators $Q_{i}$,

$$
Q _ {i} | \Omega \rangle = 0.\tag{8}
$$

This question is important for the following reasons. Such a state, if it exists, necessarily has zero energy, in view of (7). Moreover, (7) shows that no state could have negative energy. Therefore a state  $|\Omega\rangle$  which obeys (8), if it exists, is necessarily the minimum energy state or “vacuum state” of the system. If there are several states  $|\Omega_{\alpha}\rangle$  which obey (8), they are equally good zero energy vacuum states (except possibly for questions involving cluster decomposition).

Now in any quantum field theory if a symmetry operator (an operator which commutes with the Hamiltonian) annihilates the vacuum state, then the one particle states furnish a representation of the symmetry. In the case of a supersymmetric theory, if a solution of (8) does exist, then the Hilbert space of the theory contains bosons and fermions of equal mass.

The bosons and fermions which are observed to exist in nature do not have equal masses, so if supersymmetry really does play a role in nature, the world is described by a theory in which (8) has no solutions. In such a case, it is said that supersymmetry is “spontaneously broken”. If supersymmetry is spontaneously broken, there still exists a vacuum state—a state of minimum energy—but its energy is strictly positive, and it is not annihilated by the supersymmetry charges. In such a case, the bosons and fermions are not equal in mass, despite the underlying supersymmetry.

The spontaneous breaking of supersymmetry which occurs if (8) has no solution is somewhat analogous to the spontaneous breaking of gauge invariance in the Weinberg-Salam model, or to the spontaneous breakdown of chiral symmetry in quantum chromodynamics. In each case a symmetry of the underlying equations is not manifest in the particle spectrum because the symmetry operator does not annihilate the vacuum.

It should be emphasized that for applications in physics, what is important is primarily the question of whether a solution of (8) does exist. The number of solutions—assuming that one or more solutions does exist—is not so important.

In some cases, methods which are standard in physics suffice to show that a supersymmetrically invariant state—a solution of (8)—does or does not exist [21]. (A solution may be shown not to exist by calculating a reliable, positive lower bound to the energy eigenvalues. It may be shown that a solution does

exist by showing that the theory has a mass gap so that there is no potential "Goldstone fermion".) In general, though, it is far too difficult to show by direct methods whether (8) has a solution, much as it is too difficult to determine directly whether, say, the Dirac operator on a compact manifold has a zero eigenvalue. But the indirect methods that are effective in the latter case can usefully be applied to supersymmetry.

The simplest indirect method is to calculate the index of one of the supersymmetry operators. In view of (5), any state  $|\Omega\rangle$  with  $Q_{i}|\Omega\rangle=0$  also obeys  $P|\Omega\rangle=0$ . In looking for states  $|\Omega\rangle$  which obey  $Q_{i}|\Omega\rangle=0$ , we therefore lose nothing by restricting ourselves to the subspace  $H_{0}$  consisting of states annihilated by P. Like the full Hilbert space H,  $H_{0}$  has a decomposition  $H_{0}=H_{0}^{+}\oplus H_{0}^{-}$  into bosonic and fermionic states.

Within  $K_{0}$  the simplest supersymmetry algebra of (3) and (4) is obeyed. In particular,  $Q_{i}^{2} = Q_{j}^{2} = H$  for any i or j. Hence a state in  $K_{0}$  annihilated by one of the  $Q_{i}$  is annihilated by all of them.

Choosing one of the  $Q_{i}$  and denoting it simply as Q, we want to know whether Q restricted to  $K_{0}$  has a zero eigenvalue. This of course can be partially addressed as an index problem. We write the restriction of Q to  $K_{0}$  as  $Q_{+} + Q_{-}$, where  $Q_{+}$ maps  $K_{0}^{+}$ into  $K_{0}^{-}$, and  $Q_{-}$ is the adjoint of  $Q_{+}$. A nonzero index of  $Q_{+}$ would ensure that Q does have a zero eigenvalue within  $K_{0}$. The index of  $Q_{+}$ may usefully be referred to as  $\operatorname{Tr}(-1)^{F}$, the trace of the operator  $(-1)^{F}$  which distinguishes bosons from fermions.

In [21] the index was calculated and shown to be nonzero in a number of interesting cases, including supersymmetric  $\phi^{4}$  theory and supersymmetric non-Abelian gauge theories (both in four dimensions). Therefore supersymmetry is not spontaneously broken in any of these theories.

Other “deformation invariants” which appear in conventional problems in mathematics have analogues in supersymmetry quantum field theories. We will return to this later.

In §§2 and 3 of this paper we will consider supersymmetric quantum mechanics systems with a finite number of degrees of freedom. In §2 we will discuss systems which obey the simplest supersymmetry algebra of (1)-(4). We will see that such systems have a very surprising connection with Morse theory. In fact, we will be led to a new way of looking at the Morse inequalities, and to a conjectured generalization of them. In §3 we will discuss supersymmetric quantum mechanics systems which obey the more elaborate algebra of (5). We will see that such systems are related to the fixed point theorems for Killing vector fields, much as the systems of §2 are related to Morse theory. Finally, in §4 we will discuss the extension from supersymmetric quantum mechanics to supersymmetric quantum field theory.

The results of §2 have an analogue for complex manifolds, which will be discussed in a separate paper.

## 2. Morse theory

The simplest example of supersymmetric quantum mechanics is a system which is very well known in mathematics. Let M be a Riemannian manifold of dimension n. Let  $V_{p}, p = 0, 1, \cdots, n$ , be the space of p-forms. Let d and  $d^{*}$  be the usual exterior derivative and its adjoint. Define

$$
Q _ {1} = d + d ^ {*}, \quad Q _ {2} = i (d - d ^ {*}), \quad H = d d ^ {*} + d ^ {*} d,\tag{9}
$$

so that $H$ is the usual Laplacian acting on forms. Then by virtue of the fact that $d^2 = d^{*2} = 0$ we have the supersymmetry relations

$$
Q _ {1} ^ {2} = Q _ {2} ^ {2} = H, \quad Q _ {1} Q _ {2} + Q _ {2} Q _ {1} = 0.\tag{10}
$$

We must interpret p-forms as being bosonic or fermionic depending on whether p is even or odd, so that the  $Q_{i}$  map bosonic states into fermionic states and vice-versa.

This theory has a simple generalization, which appears widely (in a different form, which we will discuss later) in the physics literature. Let h be a smooth (real-valued) function on M, and t a real number. Define

$$
d _ {t} = e ^ {- h t} d e ^ {h t}, \quad d _ {t} ^ {*} = e ^ {h t} d ^ {*} e ^ {- h t}.\tag{11}
$$

Evidently, $d_{t}^{2} = d_{t}^{*2} = 0$, so if we define

$$
Q _ {1 t} = d _ {t} + d _ {t} ^ {*}, \quad Q _ {2 t} = i \left(d _ {t} - d _ {t} ^ {*}\right), \quad H _ {t} = d _ {t} d _ {t} ^ {*} + d _ {t} ^ {*} d _ {t},\tag{12}
$$

the algebra (10) is still satisfied for any t. As we will see, h plays the role of a Morse function, and consideration of this system will lead us to a new proof of the Morse inequalities.

We may define a Betti number  $B_{p}(t)$  as the number of linearly independent p-forms which obey  $d_{t}\psi = 0$  but cannot be written as  $\psi = d_{t}\chi$  for any  $\chi$ . However, it is almost obvious that  $B_{p}(t)$  is independent of t, and therefore equal to the usual Betti number  $B_{p}$ . This follows immediately from the fact that  $d_{t}$  differs from d only by conjugation by the invertible operator  $e^{th}$ , so that the mapping  $\psi \to e^{th}\psi$  is an invertible mapping from p-forms which are closed but not exact in the usual sense to p-forms which are closed but not exact in the sense of  $d_{t}$ .

It then follows from standard arguments that the number of zero eigenvalues of  $H_{t}$  acting on p-forms is, just as at t = 0, equal to  $B_{p}$ . This is useful because, as we will see, the spectrum of  $H_{t}$  simplifies dramatically for large t. We will be

able to place upper bounds on the  $B_{p}$  in terms of the critical points of h, by studying the spectrum of  $H_{t}$  for large t.

To understand why the critical points of h enter, it is useful to work out an explicit formula for  $H_{t}$ . Some notation is useful. At each point p on M choose an orthonormal basis of tangent vectors  $a^{k}(p)$ . The  $a^{k}(p)$  can be regarded as operators on the exterior algebra at p, the operation being interior multiplication,  $\psi \to i(a^{k})\psi$ . Let  $a^{k*}$  be the adjoint operators. Thus  $a^{k*}$  is exterior multiplication by the one-form dual to  $a^{k}$ . The  $a^{k*}$  and  $a^{k}$  would be called “fermion creation and annihilation operators” in the physics literature. Also on a Riemannian manifold it makes sense to speak of the covariant second derivative of h with components  $D^{2}h/D\phi^{i}D\phi^{j}$  in the basis dual to the  $a^{k}$ .

With these conventions, one may readily calculate that

$$
H _ {t} = d d ^ {*} + d ^ {*} d + t ^ {2} (d h) ^ {2} + \sum_ {i, j} t \frac {D ^ {2} h}{D \phi^ {i} D \phi^ {j}} [ a ^ {* i}, a ^ {j} ].\tag{13}
$$

Here  $(dh)^{2}=\gamma^{ij}(\partial h/\partial\phi^{i})(\partial h/\partial\phi^{j})$  is the square of the gradient of h, evaluated with respect to the Riemannian metric  $\gamma$  of M.

We can now see why the critical points are important. For very large t, the “potential energy”  $V(\phi) = t^{2}(dh)^{2}$  becomes very large, except in the vicinity of the critical points where dh = 0. Therefore the eigenfunctions of  $H_{t}$  are, for large t, concentrated near the critical points of h, and an asymptotic expansion for the eigenvalues in powers of 1/t can be explicitly calculated in terms of local data at the critical points.

Let us first consider the case of a nondegenerate Morse function h, so that dh = 0 only at isolated points  $p^{a}$ , and at each of those points the matrix of second derivatives  $D^{2}h/D\phi^{i}D\phi^{j}$  is nonsingular. Let  $M_{p}$  be the number of critical points whose Morse index is p—that is, the number of critical points at which the matrix  $D^{2}h/D\phi^{i}D\phi^{j}$  has p negative eigenvalues. We will first prove the Morse inequalities in the weak form  $M_{p} \geqslant B_{p}$ .

Let $\lambda_p^{(n)}(t)$ be the $n$th smallest eigenvalue of $H_{t}$ acting on $p$-forms. We will see that there is an asymptotic expansion for large $t$

$$
\lambda_ {p} ^ {(n)} (t) = t \left(A _ {p} ^ {(n)} + \frac {B _ {p} ^ {(n)}}{t} + \frac {C _ {p} ^ {(n)}}{t ^ {2}} + \dots\right).\tag{14}
$$

We will calculate explicitly the  $A_{p}$  below. As has been argued above, the Betti number  $B_{p}$  is equal to the number of  $\lambda_{p}^{(n)}(t)$  which are equal to zero. For large t, the number of  $\lambda_{p}^{(n)}$  which vanish is no larger than the number of vanishing  $A_{p}^{(n)}$ . We will see below that the number of  $A_{p}^{(n)}$  vanish is equal to the Morse number  $M_{p}$ , that is, the number of critical points of Morse index p. This shows

that  $M_{p} \geqslant B_{p}$ . The stronger form of the Morse inequalities will require a slight further argument.

As t becomes large, the low-lying eigenvalues of  $H_{t}$  can be calculated by expanding about the critical points  $p^{a}$ . In the vicinity of any critical point, one can introduce locally Euclidean coordinates  $\phi_{i}$  (chosen so that the critical point is at  $\phi_{i}=0$  and so that in terms of the  $\phi_{i}$  the metric tensor  $\gamma$  is Euclidean up to terms of order  $\phi^{2}$ ). The  $\phi_{i}$  can be chosen so that, near the critical point,  $h(\phi_{i})=h(0)+\frac{1}{2}\sum\lambda_{i}\phi_{i}^{2}+0(\phi^{3})$  for some  $\lambda_{i}$ .

Near the critical point  $p^{a}$ ,  $H_{t}$  can be approximated as

$$
\overline {{{H}}} _ {t} = \sum_ {i} \left(- \frac {\partial^ {2}}{\partial \phi_ {i} ^ {2}} + t ^ {2} \lambda_ {i} ^ {2} \phi_ {i} ^ {2} + t \lambda_ {i} [ a ^ {i *}, a ^ {i} ]\right).\tag{15}
$$

There are corrections to this formula of higher order in $\phi$, but they can be neglected in calculating the $A_{p}^{(n)}$. The reason for this is that for large $t$ the eigenfunctions are concentrated very near the critical point. The corrections to (15) enter in calculating the higher order terms $B_{p}^{(n)}, C_{p}^{(n)}$, and so on.

It is very easy to calculate the spectrum of the operator which appears in (14). This operator is

$$
\overline {{{H}}} _ {t} = \sum \left(H _ {i} + t \lambda_ {i} K _ {i}\right),\tag{16}
$$

where

$$
H _ {i} = - \frac {\partial^ {2}}{\partial \phi_ {i} ^ {2}} + t ^ {2} \lambda_ {i} ^ {2} \phi_ {i} ^ {2}, K _ {j} = [ a ^ {j *}, a ^ {j} ].\tag{17}
$$

The  $H_{i}$  and  $K_{j}$  mutually commute and can be simultaneously diagonalized. As is well known  $H_{i}$, which is the Hamiltonian of the simple harmonic oscillator, has the eigenvalues  $t|\lambda_{i}|(1+2N_{i})$,  $N_{i}=0,1,2,\cdots$, each of which appears with multiplicity one. The eigenfunctions of  $H_{i}$  vanish rapidly if  $|\lambda_{i}\phi_{i}| \gg 1/\sqrt{t}$, and this is the reason that the approximation (15) is valid to lowest order in 1/t. The operator  $K_{j}$  has eigenvalues  $\pm1$. The eigenvalues of  $H_{t}$  are therefore

$$
t \sum_ {i} \left(\left| \lambda_ {i} \right| \left(1 + 2 N _ {i}\right) + \lambda_ {i} n _ {i}\right), \quad N _ {i} = 0, 1, 2, \dots , n _ {i} = \pm 1.\tag{18}
$$

This is the spectrum of  $H_{t}$  acting on the exterior algebra as a whole. If we wish to restrict  $H_{t}$  to act on p-forms, a moment's thought about the operators  $K_{i}$  shows that we must require that the number of positive  $n_{i}$  be equal to p.

For (18) to vanish, we must set all  $N_{i}$  to zero, and we must choose  $n_{i}$  to be +1 if and only if  $\lambda_{i}$  is negative. This means that, expanding around any given critical point,  $H_{t}$  has precisely one zero eigenvalue, which is a p-form if the critical point has Morse index p. All other eigenvalues of  $H_{t}$  are proportional to t with positive coefficients.

(18) gives explicitly the leading coefficients  $A_{p}^{(n)}$  in the spectrum of  $H_{t}$  near any critical point. The higher order coefficients  $B_{p}^{(n)}$ ,  $C_{p}^{(n)}$ , and so on could be straightforwardly calculated according to the standard rules of Rayleigh-Schrödinger perturbation theory. $^{2}$

We have been discussing the states localized near one critical point, but the low-lying eigenstates of  $H_{t}$  for large t may of course be localized near any critical point on the manifold. Taking account of all the critical points we see that for every critical point A,  $H_{t}$  has just one eigenstate  $|a\rangle$  whose energy does not diverge with t. Moreover,  $|a\rangle$  is a p-form if A has Morse index p. It is not necessarily the case that  $H_{t}$  annihilates all the states  $|a\rangle$ ; we have only shown that the leading coefficients in perturbation theory vanish. But  $H_{t}$  certainly does not annihilate any of the other states, whose energy is proportional to t for large t. So at most the number of zero energy p-forms equals the number of critical points of Morse index p, and we have established the Morse inequalities in the weak form  $M_{p} \geqslant B_{p}$ .

What about the strong form of the Morse inequalities? We wish to show that

$$
\sum M _ {p} t ^ {p} - \sum B _ {p} t ^ {p} = (1 + t) \sum Q _ {p} t ^ {p},\tag{19}
$$

where all  $Q_{p}$  are nonnegative integers. It is well known that (19) is equivalent to the assertion that the critical points form a model of the cohomology of the manifold M in the following sense. For every p,  $p = 0, 1, \cdots, n$ , let  $X_{p}$  be a vector space of dimension  $M_{p}$ . One may think of  $X_{p}$  as a vector space spanned by the critical points of Morse index p. Then (19) means precisely that there exists a coboundary operator  $\delta: X_{p} \to X_{p+1}$ , where  $\delta^{2} = 0$  and the Betti numbers associated with the cohomology of  $\delta$  equal those of the manifold M. The existence of such a coboundary operator is equivalent to the Morse inequalities, but the Morse inequalities give no canonical form for it.

We have actually constructed the required coboundary operator. In fact, the space of low energy p-forms  $|a\rangle$  localized near the critical points A of index p may be identified with  $X_{p}$ , and  $d_{t}$  restricted to the  $X_{p}$  is the required coboundary operator whose existence establishes the Morse inequalities in their strong form.

Since we have now a canonical form for the coboundary operator (canonical except that it depends on the choice of a Riemannian metric for $M$), we can go

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{2}$ For a rigorous justification of Rayleigh-Schrödinger perturbation theory for operators in Euclidean space, see Reed and Simon [16]. Although the rigorous theory has apparently not been developed for operators acting on vector bundles on manifolds, the method used in Reed and Simon, pp. 34–38, to treat the double well potential should suffice with some elaboration for this case. The essential point is that only local data enters in the Rayleigh-Schrödinger perturbation theory.</span></small>

further and attempt to refine the Morse inequalities by calculating the action of  $d_{t}$  on the  $X_{p}$ .

To put it differently we have obtained the Morse inequalities from an approximate calculation of the spectrum of  $H_{t}$ . From a more accurate calculation of the spectrum we can hope to get a better upper bound on the number of zero eigenvalues and thereby to strengthen the Morse inequalities.

One's first thought might be to try to improve on the Morse inequalities by calculating the higher order terms in perturbation theory. However, it is easily seen that the $B_{p}^{(n)}$, $C_{p}^{(n)}$ and all other terms in the asymptotic expansion vanish for all those states whose energy vanishes in lowest order. This really follows from the fact that the coefficients in perturbation theory can all be calculated in terms of local data at the critical points. From local data one cannot tell whether a given critical point is required by the topology or is “removable”. So all of the states which have zero energy in the first approximation remain at zero energy to all orders in $1/t$.

To learn something new we must perform a calculation which is sensitive to the existence on the manifold of more than one critical point. Since the “potential energy” in our problem,  $V(\phi) = t^{2}(dh)^{2}$ , has more than one minimum (one for each critical point), we must allow for the possibility of “tunneling” from one critical point to another.

The effect of tunneling can be calculated in the WKB approximation, or, in a current language, by means of instantons [14]. Tunneling effects often remove spurious degeneracies which exist in perturbation theory, and so it is in this case.

It may be useful to first state the result which emerges from the instanton analysis. The relevant instantons or tunneling paths are the paths of steepest descent leading from one critical point B to another critical point A. They are the solutions, in other words, of the equation

$$
\frac {d \phi_ {i}}{d \lambda} = \gamma^ {i j} \frac {\partial h}{\partial \phi_ {j}}.\tag{20}
$$

Moreover, the instanton calculation shows that the only relevant solutions of (20) are the ones which correct two critical points whose Morse indices differ by one.

Now to each such path  $\Lambda$  we must associate a sign  $\pm1$ . This may be done as follows. At each critical point A we have a state  $|a\rangle$  of approximately zero energy. It is a p-form, if A has index p, and we may think of it as furnishing an orientation of the p dimensional vector space  $V_{A}$  of negative eigenvectors at A of  $D^{2}h/D\phi^{i}D\phi^{j}$ .

Now consider a path $\Gamma$ of steepest descent from a critical point $B$ of Morse index $p + 1$ to a critical point $A$ of Morse index $p$. Let $v$ be the tangent vector to $\Gamma$ at $B$, and $\tilde{V}_B$ the subspace of $V_B$ orthogonal to $v$. The orientation of $V_B$ given by $|b\rangle$ induces an orientation of $\tilde{V}_B$ (by interior multiplication of $v$ with the $(p + 1)$-form corresponding to $|b\rangle$).

By considering paths of steepest descent which run near to  $\Gamma$  from points near B to points near A, we get a mapping from  $\tilde{V}_{B}$  to  $V_{A}$ . Since  $\tilde{V}_{B}$  is oriented, this mapping induces an orientation of  $V_{A}$ . We define  $n_{\Gamma}$  to be +1 or -1 depending on whether that orientation agrees or disagrees with the orientation corresponding to  $|a\rangle$ .³

Define

$$
n (a, b) = \sum_ {\Gamma} n _ {\Gamma},\tag{21}
$$

where the sum runs over all paths $\Gamma$ of steepest descent from $B$ to $A$. We are now ready to define a coboundary operator $\delta: X_p \to X_{p+1}$. For any basis element $|a\rangle$ of $X_p$, define

$$
\delta \mid a \rangle = \sum_ {b} n (a, b) \mid b \rangle ,\tag{22}
$$

where the sum runs over all basis elements  $|b\rangle$  of  $X_{p+1}$ . The definition does not make it obvious that  $\delta^{2}=0$ , but this follows from the considerations below, in which we will extract  $\delta$  from the large t limit of  $d_{t}$ , whose square certainly vanishes.

The instanton calculation shows that all states in  $X_{p}$ , which are not annihilated by  $\delta\delta^{*} + \delta^{*}\delta$ , do not have zero energy. For large t their energies are roughly  $\exp - 2t |h(A) - h(B)|$ .

Consequently, if we denote as  $Y_{p}$  the number of zero eigenvalues of  $\delta\delta^{*} + \delta^{*}\delta$  acting on  $X_{p}$ , then the  $Y_{p}$  furnish upper bounds on the Betti numbers of our manifold M, just as the Morse numbers  $M_{p}$  do. (19) remains valid if one replaces  $M_{p}$  by  $Y_{p}$ .

Actually, it is reasonable to conjecture that the  $Y_{p}$  are in fact always equal to the Betti numbers  $B_{p}$  of M. This does not follow from instanton considerations alone. It is conceivable that some states which really do not have zero energy nonetheless remain at zero energy not just in perturbation theory but also in

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$M_{x}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$M_{x} = D^{2}h / D\phi_{i}D\phi_{j}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$V_{x}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">p</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$V_{s}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\tilde{V}_B$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$V_{A}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{3}$ Another way to define this is as follows. As we are working on a Riemannian manifold, we have at each point x on  $\Gamma$  a well-defined matrix  $M_{x}=D^{2}h/D\phi_{i}D\phi_{j}$  of second derivatives of h. For generic h,  $M_{x}$  has nondegenerate eigenvalues for every x on  $\Gamma$, so there is a well-defined vector space  $V_{x}$  consisting of the p lowest eigenvectors. As  $V_{s}$  interpolates smoothly from  $\tilde{V}_{B}$  to  $V_{A}$, we may transport the orientation of  $\tilde{V}_{B}$  to  $V_{A}$  via  $V_{x}$. (It is essential here that generically the tangent vector v to  $\Gamma$  at B is always the element of  $V_{B}$  corresponding to the largest eigenvalue.)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\tilde{V}_B$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$V_{x}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$V_{B}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$V_{A}$</span></small>

the simplest instanton calculation which leads to (22). Their energies would in that case vanish even more rapidly for large $t$ than $\exp - 2t | h(A) - h(B)|$.

However, one frequently finds that in the spectrum of a system all degeneracies which exist in perturbation theory but are not exact are eliminated by the simplest tunneling calculation. This motivates the guess that in general  $Y_{p} = B_{p}$ . This is certainly true in simple examples.

Actually, the integer  $n(a, b)$  defined above appears in other contexts. It is the intersection number of the ascending sphere from A and the descending sphere from B [13]. It is plausible that the integer-valued coboundary operator  $\delta$  actually gives the integral cohomology of the manifold M, but this statement could not be proved with the methods of this paper.

Let us now discuss the derivation of (22). The system described by  $d_{t}$ ,  $d_{t}^{*}$ , and  $H_{t}$  can be obtained by canonical quantization of

$$
\begin{array}{r} \mathcal {L} = \frac {1}{2} \int d \lambda \Bigg [ \sum_ {i j} \gamma_ {i j} \bigg (\frac {d \phi^ {i}}{d \lambda} \frac {d \phi^ {j}}{d \lambda} + \overline {{\psi}} ^ {i} i \frac {D \psi^ {j}}{D \lambda} \bigg) + \frac {1}{4} R _ {i j k l} \overline {{\psi}} ^ {i} \psi^ {k} \overline {{\psi}} ^ {j} \psi^ {l} \\ - t ^ {2} \gamma^ {i j} \frac {\partial h}{\partial \phi^ {i}} \frac {\partial h}{\partial \phi^ {j}} - t \frac {D ^ {2} h}{D \phi^ {i} D \phi^ {j}} \overline {{\psi}} ^ {i} \psi^ {j} \Bigg ], \end{array}\tag{23}
$$

and it is in this form that the theory appears in the physics literature. $^{4}$  In (23),  $\phi^{i}$  are local coordinates of M,  $\gamma_{ij}$  and  $R_{ijkl}$  are the metric and curvature tensors of M, and the  $\psi^{i}$  are anti-commuting fields tangent to M. $^{5}$  How canonical quantization of (23) leads to the exterior algebra was discussed in [21]. Instanton solutions or tunneling paths in this theory would be extrema of this Lagrangian, written with a Euclidean metric and with the fermions discarded. So we write the relevant action:

$$
\bar {\mathfrak {L}} = \frac {1}{2} \int d \lambda \left(\gamma_ {i j} \frac {d \phi^ {i}}{d \lambda} \frac {d \phi^ {j}}{d \lambda} + t ^ {2} \gamma^ {i j} \frac {\partial h}{\partial \phi^ {i}} \frac {\partial h}{\partial \phi^ {j}}\right).\tag{24}
$$

It is easy to prove that minimum action extrema of $\mathcal{L}$ with given initial and final conditions are paths of steepest descent. In fact after simple manipulations one finds

$$
\bar {\mathfrak {L}} = \frac {1}{2} \int d \lambda \left| \frac {d \phi^ {i}}{d \lambda} \pm t \gamma^ {i j} \frac {\partial h}{\partial \phi^ {j}} \right| ^ {2} \mp t \int d \lambda \frac {d h}{d \lambda}.\tag{25}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\psi^i$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{4}$  This Lagrangian is a simplification of the supersymmetric nonlinear sigma model which we will discuss in §4. It is obtained by requiring the fields in the sigma model to be functions only of the “time”,  $\lambda$ .</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{5}$  After quantization the  $\psi^{i}$  become the creation and annihilation operators of (13).</span></small>

From (25) we see that for any trajectory

$$
\bar {\mathcal {L}} \geqslant t | h (\lambda = + \infty) - h (\lambda = - \infty) |,\tag{26}
$$

with equality only if

$$
\frac {d \phi^ {i}}{d \lambda} \pm t \gamma^ {i j} \frac {\partial h}{\partial \phi^ {j}} = 0,\tag{27}
$$

which (apart from a rescaling of $\lambda$) is the equation of steepest descent considered earlier.

We thus see that the minimum action paths between any two critical points A and B are paths of steepest descent. Moreover, the action for each such path is

$$
I = t \left| h (B) - h (A) \right|.\tag{28}
$$

The instantons contributions to matrix elements of  $d_{t}$  are of order  $\exp - I$  for large t, and the contributions to matrix elements of  $H_{t} = d_{t}d_{t}^{*} + d_{t}^{*}d_{t}$  are of order  $\exp - 2I$ , explaining a remark made earlier.

The next step in an instanton calculation would usually be the evaluation of the Fredholm determinant for small fluctuations about the classical solution. However, in this case the nonzero eigenvalues cancel between bosons and fermions, due to supersymmetry. We are left with the zero eigenvalues of the fermions. For a trajectory running from A to B, the index of the Dirac operator equals the Morse index of A minus the Morse index of B.

We are interested in the case in which the Dirac operator has exactly one zero mode, because we want to evaluate the action of  $d_{t}$ , which is linear in fermi fields, on the states of very low energy. This explains why the relevant paths connect critical points whose Morse indices differ by one. (As long as the paths of steepest descent A and B are isolated, there is always precisely one Dirac zero mode; it can be given explicitly because it can be obtained from the classical solution by a supersymmetry transformation.)

The normalization factor associated with the fermion zero mode cancels in magnitude against the normalization factor associated with the fact that our classical solution is really a one-parameter family of solutions (because of the trivial invariance under  $\lambda\to\lambda+$  constant). Finally we see that all details having disappeared, the amplitude  $\langle b,d_{t}a\rangle$  due to a path  $\Gamma$  of steepest descent is just  $\exp-t|h(B)-h(A)|$ ; it is assumed here that  $|a\rangle$  and  $|b\rangle$  are normalized in the  $L^{2}$  norm.

However, it remains to determine the sign of the amplitude, which is absolutely crucial when we add the contributions of different paths to obtain  $n(a, b)$ . It actually is somewhat awkward to determine the sign from the

instanton point of view, because of the notorious minus signs associated with fermions. A straightforward way to determine the sign is provided by the WKB approach which is worth describing in its own right.

For a problem like this one, the basic idea of the WKB approximation is the following. We have seen that the states  $|a\rangle$  and  $|b\rangle$  decay rapidly upon departing from their respective critical points A and B. However, $^{6}$  the rate of decay is slowest along paths corresponding to solutions of the Euclidean equations of motion, which interpolate between two minima of the potential. We are thus led back to the paths  $\Gamma$  of steepest descent.

The state  $|a\rangle$  is small where  $|b\rangle$  is large, and vice-versa, because  $|a\rangle$  is localized near A while  $|b\rangle$  is localized near B. However, the overlap between  $|a\rangle$  and  $|b\rangle$  is greatest along the paths  $\Gamma$  connecting A and B, so a knowledge of  $|a\rangle$  and  $|b\rangle$  along these paths is enough to determine the dominant large t contribution to  $\langle b|d_{t}a\rangle$ . To determine the behavior of  $|a\rangle$  and  $|b\rangle$  along  $\Gamma$  is effectively a one-dimensional problem, because the fall-off upon departing from  $\Gamma$  is even more rapid than the fall-off along  $\Gamma$ . The one-dimensional problem is exactly soluble, and one finds, for instance, the  $|a\rangle$  falls off like  $\exp - th(\phi)$  in ascending along  $\Gamma$  from A to B.

Having determined  $|a\rangle$  and  $|b\rangle$  to a sufficient approximation, it is straightforward to evaluate  $\langle b|d_{t}a\rangle$  and in particular to determine the sign. The result is easily understood. The state  $|b\rangle$  starts out at B with a sign corresponding to an orientation of what previously was called  $V_{B}$ . Propagating  $|b\rangle$  continuously along  $\Gamma$  by solving the WKB equation, we eventually arrive at A with an orientation of  $V_{A}$ . The sign of  $\langle b|d_{t}a\rangle$  depends on comparing this orientation to the orientation of  $V_{A}$  corresponding to  $|a\rangle$ . In this way we obtain the result stated earlier for the sign. (The tangent vector to  $\Gamma$ , which entered our previous discussion, appears in acting with  $d_{t}$  on the wave-functions.)

This discussion would suggest that the boundary operator should be

$$
\tilde {\partial} \mid a \rangle = \sum_ {b} e ^ {- t (h (B) - h (A))} n (a, b) \mid b \rangle ,\tag{29}
$$

where  $n(a,b)$  was defined earlier. $^{7}$  However, the factors of  $e^{th}$, which obviously carry no essential information, can be eliminated by redefining the states  $e^{-th(A)}|a\rangle Z\to|a\rangle$. In so doing we are simply undoing the conjugation by  $e^{th}$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$h(B) > h(A)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">p</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$p + 1$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$(h(B) - h(A))$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{6}$ For the WKB treatment of tunneling through a barrier in one dimension, see, for example, [13, 171–178]. For a discussion of the multi-dimensional case, see [19].</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{7}$ Note that the absolute value sign can be dropped here from  $(h(B) - h(A))$ , because if A and B have Morse index p and  $p + 1$  respectively, then paths  $\Gamma$  from A and B only exist for  $h(B) > h(A)$ .</span></small>

which originally brought us from d to  $d_{t}$ . After this redefinition we arrive at the form given in (22) for the coboundary operator.

This completes our discussion of nondegenerate Morse theory. Let us now discuss how one would treat the degenerate case in this framework.

Let us thus assume that the critical point set of h is a manifold N with connected components  $N_{i}$ . We assume that at any point on one of the  $N_{i}$ , the matrix  $D^{2}h/D\phi^{i}D\phi^{j}$  restricted to the directions orthogonal to  $N_{i}$  is nonsingular. The number of negative eigenvalues of this matrix is then a constant, the Morse index  $p_{i}$  of  $N_{i}$ . The negative eigenvectors form a  $p_{i}$ -dimensional vector bundle over  $N_{i}$ , which we will call the negative bundle  $\Lambda(N_{i})$ .

The potential energy  $V(\phi) = t^{2}(dh)^{2}$  now vanishes on the  $N_{i}$ , but is, for large t, very large elsewhere. The wave functions therefore have a complicated dependence on the  $N_{i}$  but vanish very rapidly on departing from them. Let us discuss the states localized near one of the  $N_{i}$ , which we will call  $N_{0}$ . We will see that for large t the low-lying spectrum of  $H_{t}$ , acting on states localized near  $N_{0}$ , converges to the spectrum of the Laplacian on  $N_{0}$ .

A small neighborhood of  $N_{0}$  in our manifold M can be regarded as a fiber bundle  $M(N_{0})$  over  $N_{0}$  by projecting each point in M onto the point in N to which it is closest. Because M is endowed with a Riemannian structure, it makes sense to think of the exterior derivative  $\tilde{d}$  of  $N_{0}$  as acting on the de Rham complex of the whole neighborhood  $M(N_{0})$ .

For $H_{t}$ one finds a formula

$$
H _ {t} = \left(\tilde {d} \tilde {d} ^ {*} + \tilde {d} ^ {*} \tilde {d}\right) + H ^ {\prime},\tag{30}
$$

where the first term is just the Laplacian of  $N_{0}$  considered to act on the de Rham complex of  $M(N_{0})$ , and  $H'$  contains all terms which act in the directions transverse to  $N_{0}$ .

For large $t$, $H'$ can be approximated by a formula similar to (15). Fixing a point $n$ of $N_0$, one can think of $H'$ as a differential operator acting on the differential forms of the fiber over $n$ in $M(N_0)$. $H'$ so restricted has a single zero energy state—all other states have energy of order $t$. We will call this zero energy state $|\alpha(m; n)\rangle - n$ denoting a point in $N$ and $m$ denoting a point in the fiber over $n$ in $M(N)$. This state $|\alpha\rangle$ is a $p$-form ($p$ being the index of $N_0$). Moreover, rather as in the nondegenerate case, $|\alpha(n)\rangle$ gives an orientation of the fiber over $n$ of the negative bundle $\Lambda(N_0)$.

Now we restore the n dependence. Rather as in the Born-Oppenheimer approximation in molecular physics, the degrees of freedom transverse to  $N_{0}$  are frozen into their ground state  $|\alpha\rangle$ , because of the large energy associated

with any excitation. It therefore is appropriate to write the low-lying states $|\psi \rangle$ of $H_{t}$ in the form

$$
| \psi (n, m) \rangle = | \chi (n) \rangle \otimes | \alpha (m; n) \rangle .\tag{31}
$$

Here  $|\psi\rangle$  is a differential form of N (with boundary conditions to be discussed shortly). The tensor product of a differential form  $|\chi\rangle$  of  $N_{0}$  with a differential form  $|\alpha\rangle$  of the fiber in  $M(N)$  to make a differential form  $|\psi\rangle$  on the total space makes sense because of the Riemannian structure of M.

The proper global conditions on  $|\chi\rangle$  depend on the question of whether the negative bundle  $\Lambda(N_{0})$  is orientable. This is so because, at each point n,  $|\alpha(m;n)\rangle$  furnishes an orientation of the fiber over n in  $\Lambda(N_{0})$ . If  $\Lambda(N_{0})$  is orientable,  $|\chi\rangle$  is simply a differential form; if not,  $|\chi\rangle$  is a section of the de Rham complex of N twisted with the orientation bundle of  $\Lambda(N_{0})$ . The cohomology corresponding to this twisted de Rham complex we will refer to as the “twisted cohomology” of  $N_{0}$ .

Since $|\alpha(m; n) \rangle$ is annihilated by $H'$, the eigenvalue problem $H_t | \psi \rangle = \lambda | \psi \rangle$ reduces for large $t$ to the problem

$$
\left(\tilde {d} \tilde {d} ^ {*} + \tilde {d} ^ {*} \tilde {d}\right) | \chi \rangle = \lambda | \chi \rangle\tag{32}
$$

on  $N_{0}$ . The zero eigenvalues correspond of course to the cohomology (or twisted cohomology) of  $N_{0}$ . The approximation which is being made here is to ignore the  $N_{0}$  dependence of  $|\alpha(m;n)\rangle$ . The approximation is valid to lowest order in 1/t; the corrections could be systematically calculated, by analogy with the corrections to the Born-Oppenheimer approximation in molecular physics.

In particular, the states which have nonzero energy in this approximation really have nonzero energy for large enough t. However, their energies are of order one and equal (for large t) to the nonzero eigenvalues of the Laplacian on N.

States that really have zero energy must have zero energy in this leading approximation. We thus obtain the inequalities of degenerate Morse theory—which bound the Betti numbers of M in terms of those of the critical point set. The contribution of  $N_{0}$  to the Morse polynomial is  $t^{P}\overline{P}_{t}(N_{0})$ , where  $\overline{P}$  refers to the ordinary Poincaré polynomial or the Poincaré polynomial appropriate to the twisted de Rham complex, depending on whether  $\Lambda(N_{0})$  is orientable.

The subtlety that arises when  $\Lambda(N_{0})$  is not orientable is analogous to what occurs in the diatomic molecule when the electrons have nonzero angular momentum about the axis between the nuclei. The quantum numbers of the nuclear motion are then shifted, because the nuclear wave-function is a section of a twisted bundle, even though the interaction of the nuclei with the electron angular momentum might have appeared negligible.

## 3. Killing vector fields

Let M be a compact Riemannian manifold of dimension n, which admits the action of a continuous group of isometries. Let K be a Killing vector field—the infinitesimal generator of an isometry of M. Let N be the space of zeros of K—not necessarily connected, and not necessarily consisting of isolated points.

We can regard K as an operator  $i(K)$  on differential forms acting by interior multiplication. With this in mind, we modify the usual exterior derivative d and define

$$
d _ {s} = d + s i (K),\tag{33}
$$

s being an arbitrary real number. Note that while d maps a p-form into a  $(p+1)$ -form,  $d_{s}$  maps a p-form into a linear combination of a  $(p+1)$ -form and a  $(p-1)$ -form. We therefore split the de Rham complex V into the spaces  $V_{+}$  and  $V_{-}$  consisting of the p-forms of even and odd p respectively. Then  $d_{s}$  maps  $V_{+}$  into  $V_{-}$  and  $V_{-}$  into  $V_{+}$ .

One straightforwardly calculates that

$$
d _ {s} ^ {2} = - d _ {s} ^ {* 2} = s \mathscr {L} _ {K},\tag{34}
$$

where $d_s^*$ is the adjoint of $d_s$, and $\mathcal{L}_K$ is the Lie derivative along $K$. Only in verifying that $d_s^{*2} = -d_s^2$ do we need the fact that $K$ is a Killing vector field.

In this section, we will primarily study the “Hamiltonian”

$$
H _ {s} = d _ {s} d _ {s} ^ {*} + d _ {s} ^ {*} d _ {s}.\tag{35}
$$

Our main results will concern the number of zero eigenvalues of  $H_{s}$ . We will see that this number is independent of s as long as  $s \neq 0$  and independent of the choice of a K-invariant Riemannian structure for M. The number of zero eigenvalues of  $H_{s}$  always equals the sum of the Betti numbers of N.

This implies, in particular, an alternative proof of a bound [8] on the sum of the Betti numbers of the fixed point set. Indeed, for s = 0,  $H_{s}$  is the Laplacian of M, and the number of zero eigenvalues of  $H_{s}$  equals the sum of the Betti numbers of M. The eigenvalues of  $H_{s}$  are smooth functions of s, since the s-dependent terms are bounded operators. Hence the number of zero eigenvalues is no bigger for very small nonzero s than it is for s = 0. So our result on the number of zero eigenvalues for  $s \neq 0$  implies that the sum of the Betti numbers of N is not bigger than the sum of the Betti numbers of M.

In the course of determining the number of zero eigenvalues of  $H_{s}$ , we will also see that the study of  $H_{s}$  for large s can be used to express the Hirzebruch signature of M in terms of the fixed point set N. One obtains the fixed point theorem [2], [3], [9] in a version in which the contribution of each connected

component of N is an integer (its own signature). Also, dropping the requirement that K should be a Killing vector field, one can obtain from the large s limit of  $H_{s}$  a proof of Hopf's theorem expressing the Euler characteristic of M in terms of the zeros of any vector field. The proofs of these theorems which we will extract from the large s behavior of  $H_{s}$  are really variants of the proofs based on the index theorem [6], [7], [5].

Turning to our main goal—counting the zero eigenvalues of  $H_{s}=d_{s}d_{s}^{*}+d_{s}^{*}d_{s}$ —clearly any zero eigenvalue  $\psi$  of  $H_{s}$  must obey  $d_{s}\psi=d_{s}^{*}\psi=0$ . It must therefore also be annihilated by  $d_{s}^{2}=sL_{K}$ . We therefore lose nothing by restricting ourselves to the subspace  $\overline{V}$  of the de Rham complex consisting of states which are annihilated by  $L_{K}$ —states which are invariant under the isometry generated by K.

Within  $\overline{V}$ ,  $d_{s}^{2}=0$ , and we can view  $d_{s}$  as a sort of generalized coboundary operator. By standard arguments the number of zero eigenvalues of  $d_{s}d_{s}^{*}+d_{s}^{*}d_{s}$  equals the maximum number of linearly independent states which are closed but not exact in the sense of  $d_{s}$ . In other words, it equals the dimension of  $(\ker d_{s}/\operatorname{im}d_{s})$ .

Since  $d_{s}$ , like d itself, can be defined purely in terms of differential topology without choosing a metric on M, this shows that the number of zero eigenvalues of  $H_{s}$  does not depend on the choice of K-invariant Riemannian metric on M.

We can likewise easily show that the number of zero eigenvalues is independent of s as long as s is nonzero. Let  $e^{\lambda P}$  be the linear operator which multiplies every p-form by  $e^{\lambda P}$ . Conjugation by  $e^{\lambda P}$  cannot change the dimension of  $(\ker d_{s}/\operatorname{im}d_{s})$ . Under conjugation we find  $e^{-\lambda P}d_{s}e^{\lambda P}=e^{-\lambda}d_{s}$ , where  $s' = se^{2\lambda}$ . Since s can be changed in an arbitrary way by conjugation (but always remaining nonzero), the number of zero energy states is independent of s for  $s \neq 0$ .

The above arguments can of course be refined to refer separately to the number of even or odd zero energy states. Thus let  $n_{+}$  and  $n_{-}$  be the number of zero eigenvalues of  $H_{s}$  in  $V_{+}$  and  $V_{-}$  respectively. Then  $n_{+}$  and  $n_{-}$  are separately independent of s and of the choice of metric on M. In fact  $n_{+}-n_{-}=\chi(M)$ , the Euler characteristic of M.

Our next goal is to prove a lower bound on  $n_{+}$  and  $n_{-}$ . Let  $N_{+}$  and  $N_{-}$  be the sum of the even and odd Betti numbers of N respectively. We will show  $n_{+} \geqslant N_{+}$  and  $n_{-} \geqslant N_{-}$ . In fact, it is sufficient to prove one of these inequalities; the other one then follows from the fixed point theorem for the Euler characteristic, which states that  $n_{+} - n_{-} = N_{+} - N_{-} = \chi(M)$ . (We actually will show later that this formula can be proved by studying the large s behavior of

$H_{s}$.) Depending on whether $M$ is even dimensional or odd dimensional we will concentrate on proving that $n_{+} \geqslant N_{+}$ or that $n_{-} \geqslant N_{-}$.

Let $N_{0}$ be any connected component of N. Let $\psi$ be any differential form on $N_{0}$ which is a representative of the cohomology of $N_{0}$. Our strategy will be to construct for each such $\psi$ a corresponding $\overline{\psi}$ defined on M which is closed but not exact in the sense of $d_{s}$.

A neighborhood  $M(N_{0})$  of  $N_{0}$  in M can be regarded as a fiber bundle over  $N_{0}$  by projecting each point in M onto the point in  $N_{0}$  to which it is closest. Making use of the fiber bundle structure we obtain from  $\psi$  a differential form  $\tilde{\psi}$  defined on  $M(N_{0})$ . Then  $d\tilde{\psi}=0$  in  $M(N_{0})$ , and  $i(K)\tilde{\psi}=0$ , because the projection from  $M(N_{0})$  onto  $N_{0}$  commutes with the action of K. So in  $M(N_{0})$ ,  $d_{s}\tilde{\psi}=0$ . Moreover, it is impossible in  $M(N_{0})$  to satisfy  $\tilde{\psi}=d_{s}\alpha$ ; on  $N_{0}$ , since K vanishes, this equation would reduce to  $\psi=d\alpha$ , which by hypothesis has no solution.

However, on the boundary of $M(N_0)$, $d\tilde{\psi}$ and hence also $d_s\tilde{\psi}$ are nonzero. We must modify $\tilde{\psi}$ to avoid this problem. This can be done in an explicit way.

From the vector field $K$ and the Riemannian metric we form the scalar function $K^2 = (K, K)$ which vanishes only on the fixed point set $N$. Let $M_{\varepsilon}$ be the set of all points on $M$ with $K^2 \leqslant \varepsilon$. Choose some $\varepsilon > 0$ such that the component of $M_{\varepsilon}$ containing $N_0$ is contained in $M(N_0)$.

Let $\phi(x)$ be a smooth function of a real variable with $\phi(0)=1$ and $\phi(x)=0$ for $x\geqslant\varepsilon$.

Making use of the Riemannian metric, there is a definite one-form  $\tilde{K}$  which is dual to K. Since K is a Killing vector field,  $i(K)(d\tilde{K}) = -d(K^{2})$ .

We now define

$$
\begin{array}{l} \sigma = \phi (K ^ {2}) + \frac {1}{s} \phi^ {\prime} (K ^ {2}) d \tilde {K} + \frac {1}{2 s ^ {2}} \phi^ {\prime \prime} (K ^ {2}) d \tilde {K} \wedge d \tilde {K} \\ \qquad + \frac {1}{3 s ^ {3}} \phi^ {\prime \prime \prime} (K ^ {2}) d \tilde {K} \wedge d \tilde {K} \wedge d \tilde {K} + \dots . \end{array}\tag{36}
$$

The series terminates because $M$ has finite dimension $n$. One readily sees that $d_{s}\sigma = 0$ if $n$ is even, while if $n$ is odd, $d_{s}\sigma$ is zero except in dimension $n$.

$$
\chi = \tilde {\psi} \wedge \sigma .\tag{37}
$$

Let us assume now that for even (respectively odd) n,  $\psi$  is a representative of the even (respectively odd) dimensional cohomology of N. Under this restriction one may readily see that  $d_{s}\chi = 0$ . (Otherwise, it is true except in the highest dimension.) Moreover,  $\chi$  is not exact in the sense of  $d_{s}$ . The equation  $\chi = d_{s}\alpha$  would again reduce on  $N_{0}$  to  $\psi = d\alpha$ .

For every even (or odd) dimensional cohomology class of N we have produced an object  $\chi$  which is closed but not exact in the sense of  $d_{s}$ . Depending on whether n is even or odd, we have proved that  $n_{+} \geqslant N_{+}$  or that  $n_{-} \geqslant N_{-}$ . As noted earlier, consideration of the Euler characteristic shows that both of these inequalities hold if one does.

Now let us prove the converse inequalities  $N_{+} \geqslant n_{+}$  and  $N_{-} \geqslant n_{-}$ . This will be done by studying the large s behavior of the spectrum of  $H_{s}$ . One straightforwardly calculates that

$$
H _ {s} = d d ^ {*} + d ^ {*} d + s ^ {2} K ^ {2} + s \left(\left(d \tilde {K}\right) \wedge + i (d \tilde {K})\right).\tag{38}
$$

Here  $d\tilde{K}$  is regarded as an operator acting on differential forms by exterior multiplication, and (using the Riemannian metric) by interior multiplication also.

In this case, the “potential energy” is  $V(\phi) = s^{2}K^{2}$ . For large s the eigenstates are therefore concentrated near the zeros of K. As in §3 this makes it possible to obtain detailed information about the spectrum for large s. As the arguments will be somewhat repetitious of §2, we will be brief.

Assume first that K has only isolated zeros. This of course is possible only if the dimension n is even. In this case,  $N_{-}=0$  and  $N_{+}$ equals the number of zeros of K for reasons which will now be sketched.

Near any zero $A$ of $K$, there are locally Euclidean coordinates centered at $A$ in which

$$
K = \sum_ {i = 1} ^ {n / 2} \lambda_ {i} \left(x _ {2 i - 1} \frac {\partial}{\partial x _ {2 i}} - x _ {2 i} \frac {\partial}{\partial x _ {2 i - 1}}\right)\tag{39}
$$

with some constants  $\lambda_{1},\cdots,\lambda_{n/2}$ . Near A,  $H_{s}$  can be approximated by

$$
\begin{array}{l} \overline {{H}} _ {s} = - \sum_ {i = 1} ^ {n} \frac {\partial^ {2}}{\partial x _ {i} ^ {2}} + s ^ {2} \sum_ {r = 1} ^ {n / 2} \lambda_ {r} ^ {2} \left(\left((x _ {2 r - 1}) ^ {2} + x _ {2 r}\right) ^ {2}\right) \\ \qquad + 2 s \sum_ {r = 1} ^ {n} \lambda_ {r} \left(a _ {2 r - 1} ^ {*} a _ {2 r} ^ {*} - a _ {2 r - 1} a _ {2 r}\right), \end{array}\tag{40}
$$

where the  $a_{i}$  and  $a_{j}^{*}$  are the “creation and annihilation operators” introduced in (13).

As in §2 (40) can be diagonalized explicitly. There is again precisely one zero eigenvalue, all other eigenvalues being of order $s$. The one zero eigenvector of $\overline{H}_s$ lies in $V_+$ regardless of the values of the $\lambda_i$.

We have thus altogether  $N_{+}$  states in  $V_{+}$  whose energy does not diverge as s is increased, and none in  $V_{-}$ . As in our discussion of Morse theory, this implies  $n_{+} \leqslant N_{+}$ ,  $n_{-} = N_{-} = 0$ . Combining this with our previous inequality, we have  $n_{+} = N_{+}$ .

Now let us consider the general case in which the zeros of K are not isolated points. This is just analogous to our discussion of degenerate Morse theory. For large s the low-lying eigenstates are concentrated near N. The eigenvalue problem associated with  $H_{s}$  reduces for large s (and for the states whose energy does not grow with s) to the eigenvalue problem of the ordinary Laplacian  $H_{N} = dd^{*} + d^{*}d$  on N.  $H_{s}$  has, in lowest order in 1/s, one zero eigenvalue for every zero eigenvalue of  $H_{N}$ . This statement holds separately for the forms of even and of odd dimension.

Consequently,  $H_{s}$  has  $N_{+}$ even eigenvalues and  $N_{-}$ odd eigenvalues which vanish in the large s limit. Since an eigenvalue which is actually zero for all s certainly must vanish as s becomes large, we get as usual an upper bound on the number of zero eigenvalues of  $H_{s}$ . In fact, we obtain the desired upper bounds  $n_{+} \leqslant N_{+}$ ,  $n_{-} \leqslant N_{-}$ .

This completes our determination of the number of zero eigenvalues of  $H_{s}$ . Let us now discuss how the fixed point theorems for the Euler characteristic and the Hirzebruch signature emerge in this framework. As noted previously, we will obtain essentially an explicit realization of the proofs based on the index theorem.

Considering first the Euler characteristic, we have  $H_{s}=d_{s}d_{s}^{*}+d_{s}d_{s}^{*}=(d_{s}+d_{s}^{*})^{2}$  since  $d_{s}^{2}+d_{s}^{*2}=0$ . Hence zero eigenvalues of  $H_{s}$  are zero eigenvalues of the Hermitian operator  $D_{s}=d_{s}+d_{s}^{*}$ . Using the decomposition  $V=V_{+}+V_{-}$  for the de Rham complex, we may write  $D_{s}=D_{s+}+D_{s-}$ , where  $D_{s+}$  maps  $V_{+}$  into  $V_{-}$ , and  $D_{s-}$  is its adjoint.

By standard arguments the index of  $D_{s+}$  is independent of s and hence equal to the Euler characteristic of M just as at s=0. On the other hand, we can calculate the index of  $D_{s+}$  from our knowledge of the spectrum of  $H_{s}$  in the limit of large s. As there are  $N_{+}$ even eigenvalues and  $N_{-}$ odd eigenvalues of  $H_{s}$  which vanish as s becomes large, the index of  $D_{s+}$  is  $N_{+}-N_{-}$, which is just the Euler characteristic of N. So M and N have equal Euler characteristics,

$$
\chi (M) = \chi (N),\tag{41}
$$

As it stands this is a less than satisfactory result, since it is, according to Hopf's theorem, possible to express the Euler characteristic of M in terms of the zeros of any vector field, not necessarily a Killing vector field.

Actually, it is possible to obtain the more general result in this framework. Letting K be an arbitrary vector field, we may still define  $d_{s}$  as before, and let  $D_{s}=d_{s}+d_{s}^{*}$  and  $H_{s}=D_{s}^{2}$ .  $H_{s}$  is now given by a formula similar to (38) but slightly more complicated. It is no longer true that  $H_{s}=d_{s}d_{s}^{*}+d_{s}^{*}d_{s}$ , because  $d_{s}^{2}+d_{s}^{*2}=0$  only for Killing vector fields. Because of this, it is no

longer true that the zero eigenvectors of  $H_{s}$  are annihilated by the Lie derivative along K, and there is no general formula for the total number of zero eigenvalues of  $H_{s}$ .

However, it is still possible to calculate the Euler characteristic of M as the number of even eigenvalues of  $H_{s}$  which vanish for large s minus the number of odd eigenvalues of  $H_{s}$  which vanish for large s. The potential energy is still  $V(\phi) = s^{2}K^{2}$ , so the low-lying eigenvalues are still localized, for large s, near the zeros of K. One may therefore associate an integer  $\alpha(N_{i})$  with each connected component  $N_{i}$  of the space N of zeros of K. Here  $\alpha(N_{i}) = \alpha_{+}(N_{i}) - \alpha_{-}(N_{i})$ , where  $\alpha_{\pm}(N_{i})$  are the number of even (or odd) states localized near  $N_{i}$  whose energy vanishes for large s. Each  $\alpha(N_{i})$  may be determined from local data near  $N_{i}$ . For an isolated zero of K it can be easily shown that  $\alpha$  equals the degree or index of the zero. (In the generic case of a zero of degree  $\pm1$ , the leading large s approximation is again an exactly soluble harmonic oscillator Hamiltonian.) We have now  $\chi(M) = \Sigma_{i} \alpha(N_{i})$ .

Let us now return to the case in which K is a Killing vector field. Assuming that M is even dimensional and orientable with orientation form  $\omega$ , let us discuss, from this point of view, the fixed point theorems for the Hirzebruch signature of M.

The de Rham complex has the decomposition  $V = \tilde{V}_{+} + \tilde{V}_{-}$  into states which are even or odd under the duality operation\*. Define the Hermitian operator  $Q_{s} = i^{1/2}d_{s} + i^{-1/2}d_{s}^{*}$ . With appropriate conventions in defining \*,  $Q_{s}$  is odd under \*, so we may write  $Q_{s} = \tilde{Q}_{s+} + \tilde{Q}_{s-}$  where  $\tilde{Q}_{s+}$  maps  $\tilde{V}_{+}$  into  $\tilde{V}_{-}$ , and  $\tilde{Q}_{s-}$  is its adjoint. By standard arguments the index of  $\tilde{Q}_{s+}$  is independent of s and equal to the Hirzebruch signature of M.

At $s = 0$, all states annihilated by $Q_{s}$ are also annihilated by $\mathfrak{L}_K$. Hence, for any $s$, in calculating the index of $Q_{s}$ we may restrict ourselves to the space $\overline{V}$ of states annihilated by $\mathfrak{L}_K$.

Since  $Q_{s}^{2}=H_{s}+2$  is  $L_{K}$ , as one may readily calculate, any zero eigenvector of  $Q_{s}$  which is annihilated by  $L_{K}$  is also annihilated by  $H_{s}$ . Therefore we may calculate the signature of M as the number of zero eigenvalues of  $H_{s}$  in  $\tilde{V}_{+}$ minus the number in  $\tilde{V}_{-}$ .

For example, we have seen that near an isolated zero of K,  $H_{s}$  has a single zero energy state. It is straightforward to determine, by further study of (40), whether this state is even or odd under \*. Choosing the  $\lambda_{r}$  of (39) to be all positive, the zero energy state near a given fixed point  $A_{i}$  is even or odd under \* depending on whether  $dx_{1} \wedge dx_{2} \wedge \cdots dx_{n}$  is a positive or negative multiple, at  $A_{i}$ , of the orientation form  $\omega$  of M. Defining  $n_{i} = \pm 1$  accordingly,

we have

$$
\operatorname{sign} (M) = \sum_ {i} n _ {i}\tag{42}
$$

for the signature of $M$.

The generalization to the case where the fixed point set N does not consist of isolated points is the following. One may assign to each component  $N_{i}$  of N an orientation  $\tau$  by requiring that  $\tau \wedge d\tilde{K} \wedge \cdots \wedge d\tilde{K}$  (the right number of factors to make an n-form) is, on  $N_{i}$, a positive multiple of  $\omega$. We have seen that the zero eigenvalues of  $H_{s}$  near  $N_{i}$  are in direct correspondence with the zero eigenvalues of the Laplacian on  $N_{i}$. The correspondence maps states even (or odd) under \*into states even (or odd) under \*if  $N_{i}$  is oriented in the way just indicated. Hence each  $N_{i}$  contributes its own signature to the signature of M. Adding up the contributions we find that N and M have the same signature,

$$
\operatorname{sign} M = \operatorname{sign} N.\tag{43}
$$

These considerations may be sharpened by thinking of the signature as a character of the group generated by  $L_{K}$ . Thus for any real  $\theta$  let  $I(\theta) = \operatorname{Tr} * \exp\theta\mathcal{L}_{K}$ ; the trace is to be evaluated among the states annihilated by  $Q_{s}$ . Actually  $I(\theta)$  is independent of  $\theta$ ; this must be true for any s, since it is certainly true at s = 0. However, the contribution from states localized near any given fixed point is not independent of  $\theta$ . An isolated point  $A_{i}$  contributes

$$
I _ {i} (\theta) = n _ {i} \prod_ {r} \frac {\left(1 + e ^ {i \theta \lambda_ {i r}}\right)}{\left(1 - e ^ {i \theta \lambda_ {i r}}\right)},\tag{44}
$$

where the  $\lambda_{ir}, r = 1, 2, \cdots, n/2$ , are the “rotation angles” at the ith zero of K; (it is assumed again that they are defined to be all positive). (44) can be calculated by study of  $Q_{s}$  in the approximation of (40).

The calculation of (44) is somewhat delicate and must be done by fixing a given Fourier component of  $I(\theta)$  (in other words, a given eigenvalue of  $iL_{K}$ ) and calculating the spectrum of  $Q_{s}$  and  $H_{s}$  in the large s limit. The convergence is not uniform for the different Fourier components. A more extensive discussion and an analogous treatment of certain problems on complex manifolds will appear in a forthcoming paper.

Adding the contributions of all the fixed points (which we assume to be isolated, for simplicity), we have

$$
\text { sign   } M = \sum_ {i} I _ {i} (\theta),\tag{45}
$$

for any $\theta$. This formula was originally given by Atiyah and Bott [2], [3], [9]. The fact that (45) is independent of $\theta$ gives strong relations among the $\lambda_{ir}$.

This reasoning can also be applied to obtain the fixed point theorems for the twisted signature complex. One can also use this approach to obtain the theorem of Atiyah and Hirzebruch  $[4]$  concerning the vanishing of the (character-valued) index of the Dirac operator on manifolds which admit a Killing vector. This theorem is of interest in connection with the question  $[20]$  of obtaining realistic fermion quantum numbers in Kaluza-Klein theories.

Let us now make a few remarks preliminary to our discussion of quantum field theory in §4. We define

$$
\begin{array}{l} Q _ {1 s} = i ^ {1 / 2} d _ {s} + i ^ {- 1 / 2} d _ {s} ^ {*}, \quad Q _ {2 s} = i ^ {- 1 / 2} d _ {s} + i ^ {1 / 2} d _ {s} ^ {*}, \\ H _ {s} = d _ {s} d _ {s} ^ {*} + d _ {s} ^ {*} d _ {s}, \quad P = 2 i s \mathcal {L} _ {K}. \end{array}\tag{46}
$$

One readily sees that for any $s$ these operators satisfy the supersymmetry algebra in the form

$$
Q _ {1} ^ {2} = H + P, \quad Q _ {2} ^ {2} = H - P, \quad Q _ {1} Q _ {2} + Q _ {2} Q _ {1} = 0.\tag{47}
$$

As discussed in the introduction, this is the (simplest) form of the supersymmetry algebra which is consistent with special relativity.

A slight generalizations is possible. Let $h$ be any function invariant under the action of $K$; that is, $i(K)dh = 0$. Let $d_{s,t} = e^{-ht}d_s e^{ht}$. Defining

$$
\begin{array}{c} Q _ {1 s, t} = i ^ {1 / 2} d _ {s, t} + i ^ {- 1 / 2} d _ {s, t} ^ {*}, \\ Q _ {2 s, t} = i ^ {- 1 / 2} d _ {s, t} + i ^ {1 / 2} d _ {s, t} ^ {*}, \\ H _ {s, t} = d _ {s, t} d _ {s, t} ^ {*} + d _ {s, t} ^ {*} d _ {s, t}, \\ P = 2 i s \mathscr {L} _ {K}, \end{array}\tag{48}
$$

it is evident that the supersymmetry algebra is still satisfied. (47) and (48) will be our starting point in formulating supersymmetric quantum field theory.

We have so far assumed that $M$ is compact. But in discussing quantum field theory we will be interested in cases in which this is not so.

There will be two interesting cases. If N, the space of fixed points, is compact, M is geodesically complete, and the asymptotic behavior of M is such that  $H_{s}$  has a discrete spectrum, then most of our considerations apply. Our determination of the number of zero eigenvalues of  $H_{s}$  in terms of the topology of N is still valid.

Also, as long as N is compact and  $H_{s}$  has a discrete spectrum, the operators  $H_{s}$  and  $H_{s,t}$  always have the same number of zero eigenvalues. This is because the passage from  $d_{s}$  to  $d_{s,t}$  is achieved by conjugation and the number of zero eigenvalues of  $H_{s}$  or of  $H_{s,t}$  can be characterized as the number of states which are closed but not exact in the sense of  $d_{s}$  or  $d_{s,t}$ . It does not matter here whether M is compact.

If N is not compact, then  $H_{s}$  has a continuous spectrum, and most of our considerations do not apply. However, for suitable choices of h,  $H_{s,t}$  may have a discrete spectrum. This is so if, on  $N, (dh)^{2}$  is bounded away from zero on the complement of some compact set. In that situation there is an important version of the fixed point theorems which can be applied.

As in §2, define on $N$ the operators $d_{t} = e^{-ht}de^{ht}$ and $H_{t} = d_{t}d_{t}^{*} + d_{t}^{*}d_{t}$. Then in the large $s$ limit (with $t$ fixed), the low-lying spectrum of $H_{s,t}$ on $M$ coincides with the spectrum of $H_{t}$ on $N$. Consequently, any deformation invariant associated with the system $(d_{s,t}, H_{s,t})$ on $M$ equals the corresponding invariant for the system $(d_{t}, H_{t})$ on $N$. This is true, for example, for the index related to the decomposition $V = V_{+} \oplus V_{-}$. That index in the quantum field theory case is the quantity referred to as $\operatorname{Tr}(-1)^F$ in the introduction.

In quantum field theory, M will be infinite dimensional and N finite dimensional. The reduction of a problem on M to a problem on N is crucial to make computations possible.

## 4. Quantum field theory

We will now formulate supersymmetric quantum field theory by generalizing the previous considerations to certain Riemannian manifolds of infinite dimension (function spaces).

We will limit ourselves to the simplest case of a world with one spatial dimension. Thus space will be a circle S. S is endowed with a Riemannian metric and has a circumference L. We eventually wish to take the limit  $L \to \infty$  and replace the circle by the real line. But it is most convenient to begin with a finite L.

Now let $B$ be a finite dimensional complete Riemannian manifold, and $\Omega(B; S)$ the space of maps from $S$ to $B$. Then $\Omega$ has a natural Riemannian structure $(,)$ obtained by combining the Riemannian structure of $B$ with that of $S: (\delta\sigma, \delta\tau) = \int dx\langle\delta\sigma(x), \delta\tau(x)\rangle$ where $x$ parametrizes arc length on $S$, and $\langle , \rangle$ is the Riemannian structure of $B$.

As the loop space  $\Omega$  is an (infinite dimensional) Riemannian manifold, one may think of introducing the de Rham complex of  $\Omega$  and the de Rham operators d and  $d^{*}$ . However, these operators do not really make sense. In particular, one could hardly make sense of the nonzero spectrum of  $H = dd^{*} + d^{*}d$ , although one could try to formally associate the zero eigenvalues of H with the cohomology of  $\Omega$  (defined by other means).

It is perhaps rather surprising that a relatively slight modification of the de Rham operators of  $\Omega$  gives rise to something meaningful. Indeed, the group

$U(1)$ of rotations of the circle $S$ can be considered to act on $\Omega$ (the action being simply $\sigma(x) + \sigma(x + a)$ for any loop $\sigma$ in $\Omega$). Let $K$ be the corresponding Killing vector field—the infinitesimal generator of the group action on $\Omega$.

Then following §3 we introduce a real number $s$ and define on the de Rham complex of $\Omega$ the operators

$$
d _ {s} = d + s i (K), \quad H _ {s} = d _ {s} d _ {s} ^ {*} + d _ {s} ^ {*} d _ {s}.\tag{49}
$$

This system defines the “supersymmetric nonlinear sigma model” (in one space, one time dimension, and based on the manifold B).  $H_{s}$  is the Hamiltonian of the theory, while  $d_{s}$  and  $d_{s}^{*}$  are the supersymmetry operators (the connection with the conventional supersymmetry algebra is given in (46) and (47)).

If B is R or  $S^{1}$ , (49) describes massless supersymmetric free field theory and is exactly soluble. Otherwise, it is a rather challenging problem, part of the program of “constructive quantum field theory”, to put (49) on a mathematically sound footing. This problem is rather delicate and involves “renormalization”, which is a sort of limiting procedure to define the operators acting on the infinite dimensional function space. The supersymmetric nonlinear sigma model is “asymptotically free” if B is, for example, a homogeneous space of positive curvature. There are very strong arguments to believe that the renormalization program can be carried out successfully in asymptotically free theories, so that such theories are in fact capable of being made mathematically well-defined.

With any choice of B, the spectrum of  $H_{s}$  can be calculated for large s as an asymptotic expansion in powers of 1/s. In certain cases, other methods are available. For instance, if B is  $S^{N}$  or  $CP^{N}$, the spectrum of  $H_{s}$  may be calculated for large N, independent of s [1], [10], [19]. These calculations incidentally give strong support to the idea that the supersymmetric nonlinear sigma is mathematically well-defined after renormalization. The nonzero energy spectrum of  $H_{s}$  describes particles, bound states, collisions—the whole range of phenomena of quantum field theory.

Since (49) is not the usual formulation in the physics literature of the supersymmetric nonlinear sigma model, the following remarks may be useful. Ordinary quantum mechanics is (in the simplest case) described by the Hamiltonian operator  $H = -\nabla^{2} + V$ , where  $\nabla^{2}$  is the Laplacian (or Laplace-Beltrami operator) on some manifold B, and V is a potential energy function. Quantum field theory with bosons only is a sort of infinite dimensional generalization of that construction. The Hamiltonian is still of the general form  $H = -\nabla^{2} + V$ , but  $\nabla^{2}$  is now formally the Laplace-Beltrami operator on an infinite dimensional function space  $\Omega$ , and V is a potential energy function

defined on  $\Omega$ . This point of view, which goes back to the early days of quantum field theory, is for some purposes extremely clumsy, but for other purposes it is useful to be able to think of quantum field theory as an infinite dimensional generalization of ordinary quantum mechanics.

Supersymmetric theories involve in many ways objects which might be regarded as the square roots of the objects appearing in theories of bosons only. The de Rham operators are in some sense the square roots of the Laplace-Beltrami operator. Therefore given that quantum field theories of bosons only are based (in one viewpoint) on the Laplace-Beltrami operator on function spaces, it is not too surprising that the de Rham operators d and  $d^{*}$  on function spaces are the starting point for (one formulation of) supersymmetric quantum field theory. The main points in the connection between the de Rham operators and conventional formulations of supersymmetric theories were pointed out at the end of [22].

Let us now discuss some of the interesting questions to which this point of view can usefully be applied. We assume first that $B$ is compact.

As explained in the introduction the most important question is whether  $H_{s}$  has one or more zero eigenvalues. The states annihilated by  $H_{s}$ , if they exist, are supersymmetrically invariant vacuum states, and their existence means that supersymmetry is not spontaneously broken.

Counting the zero eigenvalues of  $H_{s}$  is precisely the problem we solved in §3, for the case of a finite dimensional manifold M. In that case we showed that the number of zero eigenvalues equals the sum of the Betti numbers of N, the space of zeros of the Killing vector field which enters in the definition of  $H_{s}$ .

In the quantum field theory considered here, M is replaced by the infinite dimensional loop space  $\Omega(B)$ . A zero of K would be a map from S into B which is invariant under rotations of S. It would be, in other words, a constant map from S into B. The space of zeros can thus be identified with B itself.

Assuming that the results of §3 apply in the infinite dimensional situation, we conclude that in the quantum field theory the number of zero eigenvalues of  $H_{s}$  equals the sum of the Betti numbers of B. In particular, for compact B we conclude that  $H_{s}$  always has at least two zero energy states if B is orientable, and that supersymmetry is never spontaneously broken in the supersymmetric nonlinear sigma model.

Results from the 1/N expansion are entirely consistent [1], [11], [19], [22] with the idea that the results of §3 do apply in the infinite dimensional context. However, to establish this on a firm footing one would have to exhibit a regularization of the infinite dimensional system within the context of which the considerations of §3 apply. As it is not clear how this can be done, it is worth while to state some more modest conclusions which can be drawn on the

basis of arguments which are more clearly applicable. Let us thus discuss what can be learned about the supersymmetric nonlinear sigma model by consideration of index theorems.

There are two relevant decompositions of the Hilbert space $\mathcal{H}$ of this theory. We first may write $\mathcal{H} = \mathcal{H}_{+} \oplus \mathcal{H}_{-}$, where $\mathcal{H}_{+}$ and $\mathcal{H}_{-}$ are the bosonic and fermionic spaces (corresponding in the finite dimensional case to $p$-forms of even or odd $p$, respectively). Relative to this decomposition one may define an index (the number of zero eigenvalues of $H_{s}$ in $\mathcal{H}_{+}$ minus the number in $\mathcal{H}_{-}$). As in the introduction this index may be viewed as the trace of the operator $(-1)^F$, which assigns the value $+1$ to every state in $\mathcal{H}_{+}$, and $-1$ to every state in $\mathcal{H}_{-}$.

It is also possible in the supersymmetry nonlinear sigma model to define an operation which generalizes the notion of duality on finite dimensional manifolds. One may be surprised that it makes sense to formulate duality on the infinite dimensional space  $\Omega$ . Very roughly, this may be understood as follows. If one chooses an N-dimensional approximation to  $\Omega$ , the low-lying spectrum of  $H_{s}$  is dominated by p-forms with p of order  $\frac{1}{2}N$ . Letting N become larger and larger, the relevant values of p increase in such a way that the duality operation which exists in the finite dimensional case has a smooth limit when one finally defines the theory on the infinite dimensional manifold  $\Omega$ .

In any case, the supersymmetric nonlinear sigma model admits a symmetry operation which in the physics literature is usually referred to as the discrete chiral symmetry  $Q_{5}$ , and which has all the algebraic properties of duality on finite dimensional manifolds. Thus  $Q_{5}$  commutes with  $H_{s}$ , and  $Q_{5}^{2}=1$ , so K has a decomposition  $K=\tilde{K}_{+}\oplus\tilde{K}_{-}$ , where  $\tilde{K}_{+}$  and  $\tilde{K}_{-}$  contain respectively the states even and odd under  $Q_{5}$ . Also the Hermitian operator  $Q=i^{1/2}d_{s}+i^{-1/2}d_{s}^{*}$  anti-commutes with  $Q_{s}$ . So for the same reasons as in the finite dimensional case, the difference between the number of zero eigenvalues of  $H_{s}$  in  $\tilde{K}_{+}$  and the number in  $\tilde{K}_{-}$  is a deformation invariant, which we may think of as the trace of  $Q_{5}$ .

These invariants  $\operatorname{Tr}(-1)^{F}$  and  $TrQ_{5}$  may be viewed as providing a definition of the Euler characteristic and Hirzebruch signature of the function space  $\Omega$ . In the finite dimensional case, we can identify  $\operatorname{Tr}(-1)^{F}$  and  $TrQ_{5}$  with the Euler characteristic and Hirzebruch signature of the space of zeros of K. We have seen that in the quantum field theory the space of zeros can be naturally identified with B itself, so we expect

$$
\operatorname{Tr} (- 1) ^ {F} = \chi (B), \quad \operatorname{Tr} Q _ {5} = \operatorname{sign} (B).\tag{50}
$$

Actually, these results are on a rather solid footing for the following reason. As in our discussions in §§2 and §3, to evaluate $\mathrm{Tr}(-1)^F$ and $\mathrm{Tr}Q_5$ it is enough

to have an asymptotic expansion in powers of 1/s for the spectrum of  $H_{s}$ . Such an expansion is provided by perturbation theory, which is the basis for most of what we know about the supersymmetric nonlinear sigma model (and quantum field theory in general). The results (50) can be obtained [22] just as in the finite dimensional case by studying the spectrum of  $H_{s}$  for very large s. No non-perturbative questions of regularization and renormalization are relevant; the only assumptions required to justify (50) are that the supersymmetric nonlinear sigma model does exist and that—as every physicist supposes—perturbation theory gives correctly an asymptotic expansion for the behavior of the spectrum at large s.

We actually can go somewhat further along these lines. Let $t \colon B \to B$ be any isometry. There is then a corresponding isometry $T \colon \Omega \to \Omega$ in the loop space ($T$ is the mapping $\sigma \to t \cdot \sigma$ for any $\sigma \colon S \to B$). Since $T$ commutes with $d_s$ and $H_s$, we can define the deformation invariants $\mathrm{Tr}(-1)^F T$ and $\mathrm{Tr}Q_5T$, which in a finite dimensional setting would equal the Lefschetz number and the signature of $T$, respectively.

In the finite dimensional case, the Lefschetz number and signature of T can be identified with the Lefschetz number and signature of the restriction of T to the space of zeros of the Killing vector field K. In the quantum field theory the restriction of T to the space of zeros can be identified with  $t: B \rightarrow B$ . So we conclude

$$
\operatorname{Tr} (- 1) ^ {F} T = \operatorname{Lef} (f), \quad \operatorname{Tr} Q _ {5} T = \operatorname{sign} (t).\tag{51}
$$

Again (51) can be justified by studying the spectrum of  $H_{s}$  for large s and so requires only very weak assumptions.

The importance of (50) and (51) is that if any of these deformation invariants are nonzero,  $H_{s}$  must have zero eigenvalues, so supersymmetry is not spontaneously broken.

To summarize then, we may conclude in a quite reliable way that in the supersymmetric nonlinear sigma model, supersymmetry is not spontaneously broken if B has a nonzero Euler characteristic or Hirzebruch signature, or admits an isometry of nonzero Lefschetz number or signature. On a more speculative basis we may claim that supersymmetry is never spontaneously broken in this theory, the number of zero eigenvalues of  $H_{s}$  being always equal to the sum of the Betti numbers of B. The latter claim is more speculative, because it does not follow just from a knowledge of the large s behavior of the spectrum, but requires considerations which are more delicate and less obviously valid in the infinite dimensional situation.

Let us now leave aside the nonlinear sigma model, and consider the supersymmetric version of  $\phi^{4}$  theory and some of its generalizations. We

choose for B the real line R. The system based on  $d_{s}$  and  $H_{s}$  is then relatively trivial—supersymmetric massless free field theory.

However, as discussed at the end of §3, we may introduce a function $h$ on $\Omega$ and pass from $d_s$ to $d_{s,t} = e^{-th}d_s e^{th}$. The Hamiltonian is now $H_{s,t} = d_{s,t}d_{s,t}^* + d_{s,t}^*, d_{s,t}$. With suitable choices of $h$, this gives the supersymmetric version of the usual scalar field theories.

The appropriate choices of h are as follows. Let  $\phi: S \rightarrow R$  be a real-valued function on S— that is, a point in  $\Omega$ . Let W be a smooth real-valued function of a real variable. Then define

$$
h (\phi) = \int_ {S} d x W (\phi (x)).\tag{52}
$$

If  $W(\phi) = m\phi^{2}$ , this describes supersymmetric massive free field theory. For  $W(\phi) = a\phi^{3} + b\phi$ , we obtain the supersymmetric  $\phi^{4}$  theory. Letting W be an arbitrary polynomial, we obtain the supersymmetric field theories with polynomial interaction.

We now wish to discuss the question of most crucial physical interest—whether  $H_{s,t}$  has zero eigenvalues. For reasons discussed in §3, the number of such zero eigenvalues, if any, is independent of s and t. The space of zeros of the Killing vector field can now be identified as R, and because this is not compact, many of the considerations of §3 do not apply. However, there is one useful tool in discussing the zero eigenvalues of  $H_{s,t}$ . This is the index  $\operatorname{Tr}(-1)^{F}$ .

As discussed at the end of §3, there is a version of the fixed point theorems which applies in this situation. By consideration of the large s behavior of the spectrum, one may reduce the index problem on  $\Omega$  to an immensely simpler index problem on the space R of zeros of the Killing vector field. In fact, we may replace  $d_{s,t}$  by its restriction to R, which is just the operator  $d_{t}=e^{-ht}de^{ht}$  acting on the de Rham complex of R.

As R is one-dimensional, the index problem associated with  $d_{t}$  and  $H_{t}=d_{t}d_{t}^{*}+d_{t}^{*}d_{t}$  is particularly simple. In fact,  $d_{t}$  is equivalent to the ordinary differential operator

$$
D = \frac {d}{d \phi} + t L \frac {d W}{d \phi}\tag{53}
$$

acting on real valued functions of a real variable  $\phi$  (recall that L is the circumference of S; it appears because of the integration over S in (52)).

Determining the index of D is a trivial and well-known special case of the Atiyah-Singer index theorem. The index is 1,0, or -1 depending on the behavior of W for large  $\phi$ . For instance, if W is a polynomial of leading term  $+\phi^{n}$ , the index is 1 or 0 depending on whether n is even or odd. In particular,

if W is a polynomial of even order,  $\operatorname{Tr}(-1)^{F}=1$  and supersymmetry is unbroken regardless of the values of the “coupling constants” (coefficients of various terms in W). This is a remarkable result in the sense that, in this generality, it could hardly have been obtained by means of conventional arguments in particle physics.

If W is a polynomial of odd order, or more generally if the index is zero, the situation is more complicated. One may readily show that the one-dimensional operator  $H_{t}$  has no zero eigenvalues when the index is zero. As the low-lying spectrum of  $H_{s,t}$  converges to that of  $H_{t}$  in the large s limit,  $H_{s,t}$  also has no zero eigenvalues for large enough s. This conclusion actually holds for all s, since we know that the number of zero eigenvalues of  $H_{s,t}$  is independent of s. However, this conclusion must be interpreted with care, for reasons which will now be explained.

In this section, we have always taken S to be a circle of arbitrary circumference L. However, physical interest really centers on the “infinite volume limit”  $L \to \infty$ . This limit is not straightforward, and, for instance, our index theorems are not directly applicable when  $L = \infty$ .

The relevance of our considerations as  $L \rightarrow \infty$  is really the following. If it can be shown, for instance by means of an index theorem, that the energy of the vacuum (the lowest eigenvalue of the Hamiltonian) vanishes for every finite L, then, as the large L limit of zero is zero, the vacuum energy also vanishes in the large L limit. This conclusion holds even if the mathematical structure used to prove that the vacuum energy vanishes for finite L is ill-defined for  $L = \infty$ .

No such general conclusion can be drawn if it is known that the minimum eigenvalue of the Hamiltonian is not zero for finite L. One must then face the question of whether the minimum eigenvalue converges to zero as  $L \to \infty$ . For instance, we have shown above that if the ordinary differential operator D has zero index, then the lowest eigenvalue of  $H_{s,t}$  is nonzero for any L. However, for  $W = \phi^{3} + b\phi$  (a typical case in which the index is zero), conventional methods in particle physics [22] show that if b is large and negative the minimum eigenvalue converges to zero as  $L \to \infty$ , while if b is large and positive the minimum eigenvalue does not converge to zero and supersymmetry is spontaneously broken in the infinite volume limit.

## 5. Conclusions

It is not at all clear whether supersymmetry plays a role in nature. But if it does, this is a field in which mathematical input may make a significant contribution to physics.

One outstanding mathematical problem is certainly the problem of giving a sound mathematical formulation to the infinite dimensional structures discussed in §4. This is (part of) “constructive field theory”.

Another outstanding question is the generalization of the considerations of §4 to other theories. Supersymmetric scalar field theory in the interesting case of three space dimensions may be formulated by analogy with the discussion in §4 but with one essential difference. The starting point is Kähler geometry rather than real differential geometry. However, for supersymmetric gauge theories it is not at all clear what the right mathematical structure is, and this is even less clear in the case of supersymmetric theories of gravity. If supersymmetry does play a role in physics, many other questions calling for a significant application of mathematical ideas are bound to emerge in the course of time.

## References

[1] O. Alvarez, Dynamical symmetry breakdown in the supersymmetric nonlinear  $\sigma$  model, Phys. Rev. D 17 (1978) 1123–1130.

[2] M. F. Atiyah & R. Bott, A Lefschetz fixed point formula for elliptic complexes: I, Ann. of Math. 86 (1967) 374-407.

[3] \_\_\_\_, A Lefschetz fixed point formula for elliptic complexes. II. Applications, Ann. of Math. 88 (1968) 451–491.

[4] M. F. Atiyah & F. Hirzebruch, in Essays on topology and related topics, ed. A. Haefliger & R. Narasimhan, Springer, Berlin, 1970.

[5] M. F. Atiyah and G. B. Segal, The index of elliptic operators. II, Ann. of Math. 87 (1968) 531-545.

[6] M. F. Atiyah & I. M. Singer, The index of elliptic operators. I, Ann. of Math. 87 (1968) 484-530.

[7] \_\_\_\_, The index of elliptic operators. III, Ann. of Math. 87 (1968) 546–604.

[8] T. Banks, C. M. Bender & T. T. Wu, Coupled anharmonic oscillators. I. Equal-mass case, Phys. Rev. D8 (1973) 3346–3366.

[9] R. Bott, Vector fields and characteristic numbers, Mich. Math. J. 14 (1967) 231–244.

[10] G. Bredon, Introduction to compact transformation groups, Academic Press, New York, 1972.

[11] A. D'Adda, P. Di Vecchia & M. Lüscher, Confinement and chiral symmetry breaking in  $CP^{n-1}$  models with quarks, Nuclear Phys. B152 (1979) 125–144.

[12] Y. A. Gol'fand & E. P. Likhtman, Extension of the algebra of Poincaré group generators and violation of $P$ invariance, JETP Lett. 13 (1971) 323-326.

[13] L. D. Landau & E. M. Lifschitz, Quantum mechanics, Pergamon Press, London, 1958.

[14] J. Milnor, Lectures on h-cobordism, Math. Notes, Princeton University Press, Princeton, 1965.

[15] A. M. Polyakov, Quark confinement and topology of gauge theories, Nuclear Phys. B120 (1977) 429–458.

[16] M. Reed & B. Simon, Methods of modern mathematical physics, Vol. IV, Academic Press, New York, 1978.

[17] D. V. Volkov & V. P. Akulov, Is the neutrino a goldstone particle? Phys. Lett. 46B (1973) 109–110.

[18] J. Wess & B. Zumino, Supergauge transformations in four dimensions, Nuclear Phys. B70 (1974) 39–50.

[19] E. Witten, Instantons, the quark model, and the 1/N expansion, Nuclear Phys. B149 (1979) 285–320.

[20] \_\_\_\_, Search for a realistic Kaluza-Klein theory, Nuclear Phys. B186 (1981) 412–428.

[21] \_\_\_\_, Dynamical breaking of supersymmetry, Nuclear Phys. B188 (1981) 513–555.

[22] \_\_\_\_, Constraints on supersymmetry breaking, Preprint, Princeton University, 1982, to appear in Nuclear Phys. B.

PRINCETON UNIVERSITY