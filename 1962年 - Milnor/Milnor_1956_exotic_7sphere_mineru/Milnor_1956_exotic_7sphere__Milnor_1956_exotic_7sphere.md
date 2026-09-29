# ON MANIFOLDS HOMEOMORPHIC TO THE 7-SPHERE

By John Milnor $^{1}$

(Received June 14, 1956)

The object of this note will be to show that the 7-sphere possesses several distinct differentiable structures.

In §1 an invariant  $\lambda$  is constructed for oriented, differentiable 7-manifolds  $M^{7}$  satisfying the hypothesis (\*)  $H^{3}(M^{7}) = H^{4}(M^{7}) = 0$ . (Integer coefficients are to be understood.) In §2 a general criterion is given for proving that an n-manifold is homeomorphic to the sphere  $S^{n}$ . Some examples of 7-manifolds are studied in §3 (namely 3-sphere bundles over the 4-sphere). The results of the preceding two sections are used to show that certain of these manifolds are topological 7-spheres, but not differentiable 7-spheres. Several related problems are studied in §4.

All manifolds considered, with or without boundary, are to be differentiable, orientable and compact. The word differentiable will mean differentiable of class  $C^{\infty}$ . A closed manifold  $M^{n}$  is oriented if one generator  $\mu \in H_{n}(M^{n})$  is distinguished.

## §1. The invariant λ(M⁷)

For every closed, oriented 7-manifold satisfying (\*) we will define a residue class $\lambda(M^{7})$ modulo 7. According to Thom [5] every closed 7-manifold $M^{7}$ is the boundary of an 8-manifold $B^{8}$. The invariant $\lambda(M^{7})$ will be defined as a function of the index $\tau$ and the Pontrjagin class $p_{1}$ of $B^{8}$.

An orientation $\nu \in H_8(B^8, M^7)$ is determined by the relation $\partial \nu = \mu$. Define a quadratic form over the group $H^4(B^8, M^7) / (\text{torsion})$ by the formula $\alpha \to \langle \nu, \alpha^2 \rangle$. Let $\tau(B^8)$ be the index of this form (the number of positive terms minus the number of negative terms, when the form is diagonalized over the real numbers).

Let $p_1 \in H^4(B^8)$ be the first Pontrjagin class of the tangent bundle of $B^8$. (For the definition of Pontrjagin classes see [2] or [6].) The hypothesis (\*) implies that the inclusion homomorphism

$$
i \colon H ^ {4} (B ^ {8}, M ^ {7}) \to H ^ {4} (B ^ {8})
$$

is an isomorphism. Therefore we can define a “Pontrjagin number”

$$
q (B ^ {8}) = \langle \nu , (i ^ {- 1} p _ {1}) ^ {2} \rangle .
$$

THEOREM 1. The residue class of $2q(B^{8}) - \tau(B^{8})$ modulo 7 does not depend on the choice of the manifold $B^{8}$.

Define $\lambda(M^{7})$ as this residue class.$^{2}$ As an immediate consequence we have:

COROLLARY 1. If $\lambda(M^{7}) \neq 0$ then $M^{7}$ is not the boundary of any 8-manifold having fourth Betti number zero.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  The author holds an Alfred P. Sloan fellowship.</span></small>

Let $B_{1}^{8}$, $B_{2}^{8}$ be two manifolds with boundary $M^{7}$. (We may assume they are disjoint.) Then $C^{8} = B_{1}^{8} \cup B_{2}^{8}$ is a closed 8-manifold which possesses a differentiable structure compatible with that of $B_{1}^{8}$ and $B_{2}^{8}$. Choose that orientation $\nu$ for $C^{8}$ which is consistent with the orientation $\nu_{1}$ of $B_{1}^{8}$ (and therefore consistent with $-\nu_{2}$). Let $q(C^{8})$ denote the Pontrjagin number $\langle \nu, p_{1}^{2}(C^{8}) \rangle$.

According to Thom [5] or Hirzebruch [2] we have

$$
\tau (C ^ {8}) = \langle \nu , \frac {1}{4 5} (7 p _ {2} (C ^ {8}) - p _ {1} ^ {2} (C ^ {8}) \rangle ;
$$

and therefore

$$
4 5 \tau (C ^ {8}) + q (C ^ {8}) = 7 \langle \nu , p _ {2} (C ^ {8}) \rangle \equiv 0\tag{mod 7).}
$$

This implies

(1)

$$
2 q (C ^ {8}) - \tau (C ^ {8}) \equiv 0\tag{mod 7).}
$$

LEMMA 1. Under the above conditions we have

$$
\tau (C ^ {8}) = \tau (B _ {1} ^ {8}) - \tau (B _ {2} ^ {8})\tag{2}
$$

and

(3)

$$
q (C ^ {8}) = q (B _ {1} ^ {8}) - q (B _ {2} ^ {8}).
$$

Formulas 1, 2, 3 clearly imply that

$$
2 q (B _ {1} ^ {8}) - \tau (B _ {1} ^ {8}) \equiv 2 q (B _ {2} ^ {8}) - \tau (B _ {2} ^ {8})\tag{mod 7);}
$$

which is just the assertion of Theorem 1.

PROOF OF LEMMA 1. Consider the diagram

$$
\begin{array}{c} H ^ {n} (B _ {1}, M) \oplus H ^ {n} (B _ {2}, M) \xleftarrow [ \approx ]{h} H ^ {n} (C, M) \\ \Biggl \downarrow i _ {1} \oplus i _ {2} \qquad \qquad \qquad \Biggl \downarrow j \\ H ^ {n} (B _ {1}) \oplus H ^ {n} (B _ {2}) \xleftarrow {k} H ^ {n} (C) \end{array}
$$

Note that for $n = 4$, these homomorphisms are all isomorphisms. If $\alpha = jh^{-1}(\alpha_1 \oplus \alpha_2) \in H^4(C)$, then

$$
\langle \nu , \alpha^ {2} \rangle = \langle \nu , j h ^ {- 1} (\alpha_ {1} ^ {2} \oplus \alpha_ {2} ^ {2}) \rangle = \langle \nu_ {1} \oplus (- \nu_ {2}), \alpha_ {1} ^ {2} \oplus \alpha_ {2} ^ {2} \rangle = \langle \nu_ {1}, \alpha_ {1} ^ {2} \rangle - \langle \nu_ {2}, \alpha_ {2} ^ {2} \rangle . \tag {4}
$$

Thus the quadratic form of $C^8$ is the "direct sum" of the quadratic form of $B_1^8$ and the negative of the quadratic form of $B_2^8$. This clearly implies formula (2).

Define $\alpha_{1} = i_{1}^{-1}p_{1}(B_{1})$ and $\alpha_{2} = i_{2}^{-1}p_{1}(B_{2})$. Then the relation

$$
k (p _ {1} (C)) = p _ {1} (B _ {1}) \oplus p _ {1} (B _ {2})
$$

implies that

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$n = 4k - 1$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$k = 1,2,3,4$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\lambda (M^n)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$s_{k}\mu (L_k)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$s_{k}\mu (L_k) = 1,7,62,$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{2}$  Similarly for n = 4k - 1 a residue class  $\lambda(M^{n})$  modulo  $s_{k}\mu(L_{k})$  could be defined. (See [2] page 14.) For k = 1, 2, 3, 4 we have  $s_{k}\mu(L_{k}) = 1, 7, 62, 381$  respectively.</span></small>

$$
j h ^ {- 1} \left(\alpha_ {1} \oplus \alpha_ {2}\right) = p _ {1} (C).
$$

The computation (4) now shows that

$$
\langle \nu , p _ {1} ^ {2} (C) \rangle = \langle \nu_ {1}, \alpha_ {1} ^ {2} \rangle - \langle \nu_ {2}, \alpha_ {2} ^ {2} \rangle ,
$$

which is just formula (3). This completes the proof of Theorem 1.

The following property of the invariant $\lambda$ is clear.

LEMMA 2. If the orientation of $M^7$ is reversed then $\lambda(M^7)$ is multiplied by -1. As a consequence we have

COROLLARY 2. If $\lambda(M^{7}) \neq 0$ then $M^{7}$ possesses no orientation reversing diffeomorphism$^{3}$ onto itself.

## §2. A partial characterization of the n-sphere

Consider the following hypothesis concerning a closed manifold $M^n$ (where $R$ denotes the real numbers).

(H) There exists a differentiable function $f: M^n \to R$ having only two critical points $x_0, x_1$. Furthermore these critical points are non-degenerate.

(That is if  $u_{1}, \cdots, u_{n}$  are local coordinates in a neighborhood of  $x_{0}$  (or  $x_{1}$ ) then the matrix  $(\partial^{2}f/\partial u_{i}\partial u_{j})$  is non-singular at  $x_{0}$  (or  $x_{1}$ ).)

THEOREM 2. If $M^n$ satisfies the hypothesis (H) then these exists a homeomorphism of $M^n$ onto $S^n$ which is a diffeomorphism except possibly at a single point.

Added in proof. This result is essentially due to Reeb [7].

The proof will be based on the orthogonal trajectories of the manifolds $f =$ constant.

Normalize the function $f$ so that $f(x_0) = 0$, $f(x_1) = 1$. According to Morse ([3] Lemma 4) there exist local coordinates $v_1, \cdots, v_n$ in a neighborhood $V$ of $x_0$ so that $f(x) = v_1^2 + \cdots + v_n^2$ for $x \in V$. (Morse assumes that $f$ is of class $C^3$, and constructs coordinates of class $C^1$; but the same proof works in the $C^\infty$ case.) The expression $ds^2 = dv_1^2 + \cdots + dv_n^2$ defines a Riemannian metric in the neighborhood $V$. Choose a differentiable Riemannian metric for $M^n$ which coincides with this one in some neighborhood$^4$$V'$ of $x_0$. Now the gradient of $f$ can be considered as a contravariant vector field.

Following Morse we consider the differential equation

$$
\frac {d x}{d t} = \operatorname{grad} f / \| \operatorname{grad} f \| ^ {2}.
$$

In the neighborhood $V'$ this equation has solutions

$$
(v _ {1} (t), \dots , v _ {n} (t)) = (a _ {1} (t) ^ {\frac {1}{2}}, \dots , a _ {n} (t) ^ {\frac {1}{2}})
$$

for  $0 \leq t < \varepsilon$ , where  $a = (a_{1}, \cdots, a_{n})$  is any n-tuple with  $\sum a_{i}^{2} = 1$ . These can be extended uniquely to solutions  $x_{a}(t)$  for  $0 \leq t \leq 1$ . Note that these solutions satisfy the identity

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$f^{-1}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{4}$  This is possible by [4] 6.7 and 12.2.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{3}$  A diffeomorphism f is a homeomorphism onto, such that both f and  $f^{-1}$  are differentiable.</span></small>

$$
f (x _ {a} (t)) = t.
$$

Map the interior of the unit sphere of $R^n$ into $M^n$ by the map

$$
\left(a _ {1} (t) ^ {\frac {1}{2}}, \dots , a _ {n} (t) ^ {\frac {1}{2}}\right)\rightarrow x _ {a} (t).
$$

It is easily verified that this defines a diffeomorphism of the open $n$-cell onto $M^n - (x_1)$. The assertion of Theorem 2 now follows.

Given any diffeomorphism $g: S^{n-1} \to S^{n-1}$, an $n$-manifold can be obtained as follows.

CONSTRUCTION (C). Let $M^n(g)$ be the manifold obtained from two copies of $R^n$ by matching the subsets $R^n - (0)$ under the diffeomorphism

$$
u \rightarrow v = \frac {1}{\| u \|} g \left(\frac {u}{\| u \|}\right).
$$

(Such a manifold is clearly homeomorphic to $S^n$. If $g$ is the identity map then $M^n(g)$ is diffeomorphic to $S^n$.)

COROLLARY 3. A manifold $M^n$ can be obtained by the construction (C) if and only if it satisfies the hypothesis (H).

Proof. If  $M^{n}(g)$  is obtained by the construction (C) then the function

$$
f (x) = \left\| u \right\| ^ {2} / \left(1 + \left\| u \right\| ^ {2}\right) = 1 / \left(1 + \left\| v \right\| ^ {2}\right)
$$

will satisfy the hypothesis (H). The converse can be established by a slight modification of the proof of Theorem 2.

## §3. Examples of 7-manifolds

Consider 3-sphere bundles over the 4-sphere with the rotation group SO(4) as structural group. The equivalence classes of such bundles are in one-one correspondence $^{5}$ with elements of the group $\pi_{3}(\mathrm{SO}(4))\approx Z+Z$. A specific isomorphism between these groups is obtained as follows. For each $(h,j)\in Z+Z$ let $f_{hj}:\mathrm{S}^{3}\to\mathrm{SO}(4)$ be defined by $f_{hj}(u)\cdot v=u^{h}vu^{j}$, for $v\in R^{4}$. Quaternion multiplication is understood on the right.

Let $\iota$ be the standard generator for $H^{4}(S^{4})$. Let $\xi_{hj}$ denote the sphere bundle corresponding to $(f_{hj}) \in \pi_{3}(\mathrm{SO}(4))$.

LEMMA 3. The Pontrjagin class $p_1(\xi_{hj})$ equals $\pm 2(h - j)\iota$.

(The proof will be given later. One can show that the characteristic class $\bar{c}(\xi_{h_j})$ (see [4]) is equal to $(h + j)\iota$.)

For each odd integer k let  $M_{k}^{7}$  be the total space of the bundle  $\xi_{h,j}$  where h and j are determined by the equations  $h + j = 1$ , h - j = k. This manifold  $M_{k}^{7}$  has a natural differentiable structure and orientation, which will be described later.

LEMMA 4. The invariant $\lambda(M_k^7)$ is the residue class modulo 7 of $k^2 - 1$.

LEMMA 5. The manifold $M_k^7$ satisfies the hypothesis (H).

Combining these we have:

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{5}$  See [4] §18.</span></small>

THEOREM 3. For $k^2 \not\equiv 1 \mod 7$ the manifold $M_k^7$ is homeomorphic to $S^7$ but not diffeomorphic to $S^7$.

(For $k = \pm 1$ the manifold $M_k^7$ is diffeomorphic to $S^7$; but it is not known whether this is true for any other $k$.)

Clearly any differentiable structure on $S^7$ can be extended through $R^8 - (0)$. However:

COROLLARY 4. There exists a differentiable structure on $S^7$ which cannot be extended throughout $R^8$.

This follows immediately from the preceding assertions, together with Corollary 1.

PROOF OF LEMMA 3. It is clear that the Pontrjagin class $p_1(\xi_{h_j})$ is a linear function of $h$ and $j$. Furthermore it is known that it is independent of the orientation of the fibre. But if the orientation of $S^3$ is reversed, then $\xi_{h_j}$ is replaced by $\xi_{-j - h}$. This shows that $p_1(\xi_{h_j})$ is given by an expression of the form $c(h - j)\iota$. Here $c$ is a constant which will be evaluated later.

PROOF OF LEMMA 4. Associated with each 3-sphere bundle $M_k^7 \to S^4$ there is a 4-cell bundle $\rho_k: B_k^8 \to S^4$. The total space $B_k^8$ of this bundle is a differentiable manifold with boundary $M_k^7$. The cohomology group $H^4(B_k^8)$ is generated by the element $\alpha = \rho_k^*(\iota)$. Choose orientations $\mu, \nu$ for $M_k^7$ and $B_k^8$ so that

$$
\langle \nu , (i ^ {- 1} \alpha) ^ {2} \rangle = + 1.
$$

Then the index $\tau(B_k^8)$ will be $+1$.

The tangent bundle of  $B_{k}^{8}$  is the “Whitney sum” of (1) the bundle of vectors tangent to the fibre, and (2) the bundle of vectors normal to the fibre. The first bundle (1) is induced (under  $\rho_{k}$ ) from the bundle  $\xi_{hj}$ , and therefore has Pontrjagin class  $p_{1} = \rho_{k}^{*}(c(h - j)\iota) = ck\alpha$ . The second is induced from the tangent bundle of  $S^{4}$ , and therefore has first Pontrjagin class zero. Now by the Whitney product theorem ([2] or [6])

$$
p _ {1} (B _ {k} ^ {8}) = c k \alpha + 0.
$$

For the special case k = 1 it is easily verified that  $B_{1}^{8}$  is the quaternion projective plane  $P_{2}(K)$  with an 8-cell removed. But the Pontrjagin class  $p_{1}(P_{2}(K))$  is known to be twice a generator of  $H^{4}(P_{2}(K))$ . (See Hirzebruch [1].) Therefore the constant c must be  $\pm2$ , which completes the proof of Lemma 3.

Now $q(B_k^8) = \langle \nu, (i^{-1}(\pm 2k\alpha))^2 \rangle = 4k^2$; and $2q - \tau = 8k^2 - 1 \equiv k^2 - 1 \pmod{7}$. This completes the proof of Lemma 4.

PROOF OF LEMMA 5. As coordinate neighborhoods in the base space $S^4$ take the complement of the north pole, and the complement of the south pole. These can be identified with euclidean space $R^4$ under stereographic projection. Then a point which corresponds to $u \in R^4$ under one projection will correspond to $u' = u / \| u \|^2$ under the other.

The total space  $M_{k}^{7}$  can now be obtained as follows. $^{5}$  Take two copies of  $R^{4} \times S^{3}$  and identify the subsets  $(R^{4} - (0)) \times S^{3}$  under the diffeomorphism

$$
(u, v) \rightarrow (u ^ {\prime}, v ^ {\prime}) = (u / \| u \| ^ {2}, u ^ {h} v u ^ {j} / \| u \|)
$$

(using quaternion multiplication). This makes the differentiable structure of $M_k^T$ precise.

Replace the coordinates $(u', v')$ by $(u'', v')$ where $u'' = u'(v')^{-1}$. Consider the function $f: M_k^7 \to R$ defined by

$$
f (x) = \Re (v) / (1 + \| u \| ^ {2}) ^ {\frac {1}{2}} = \Re (u ^ {\prime \prime}) / (1 + \| u ^ {\prime \prime} \| ^ {2}) ^ {\frac {1}{2}};
$$

where  $\Re(v)$  denotes the real part of the quaternion v. It is easily verified that f has only two critical points (namely  $(u, v) = (0, \pm1)$ ) and that these are non-degenerate. This completes the proof.

## §4. Miscellaneous results

THEOREM 4. Either (a) there exists a closed topological 8-manifold which does not possess any differentiable structure; or (b) the Pontrjagin class $p_1$ of an open 8-manifold is not a topological invariant.

(The author has no idea which alternative holds.)

PROOF. Let  $X_{k}^{8}$  be the topological 8-manifold obtained from  $B_{k}^{8}$  by collapsing its boundary (a topological 7-sphere) to a point  $x_{0}$ . Let  $\bar{\alpha} \in H^{4}(X_{k}^{8})$  correspond to the generator  $\alpha \in H^{4}(B_{k}^{8})$ . Suppose that  $X_{k}^{8}$ , possesses a differentiable structure, and that  $p_{1}(X_{k}^{8} - (x_{0}))$  is a topological invariant. Then  $p_{1}(X_{k}^{8})$  must equal  $\pm2k\bar{\alpha}$ , hence

$$
2 q (X _ {k} ^ {8}) - \tau (X _ {k} ^ {8}) = 8 k ^ {2} - 1 \equiv k ^ {2} - 1\tag{mod 7).}
$$

But for $k^2 \not\equiv 1 \pmod{7}$ this is impossible.

Two diffeomorphisms $f, g: M_1^n \to M_2^n$ will be called differentiably isotopic if there exists a diffeomorphism $M_1^n \times R \to M_2^n \times R$ of the form $(x, t) \to (h(x, t), t)$ such that

$$
h (x, t) = \left\{ \begin{array}{l} f (x) \\ g (x) \end{array} \right.\tag{\((t \leq 0)\}
$$

$(t \geq 1)$.

LEMMA 6. If the diffeomorphisms $f, g: S^{n-1} \to S^{n-1}$ are differentiably isotopic, then the manifolds $M^n(f), M^n(g)$ obtained by the construction (C) are diffeomorphic.

The proof is straightforward.

THEOREM 5. There exists a diffeomorphism $f: S^6 \to S^6$ of degree $+1$ which is not differentiably isotopic to the identity.

Proof. By Lemma 5 and Corollary 3 the manifold $M_3^7$ is diffeomorphic to $M^7(f)$ for some $f$. If $f$ were differentiably isotopic to the identity then Lemma 6 would imply that $M_3^7$ was diffeomorphic to $S^7$. But this is false by Lemma 4.

PRINCETON UNIVERSITY

## REFERENCES

1. F. HIRZEBRUCH, Ueber die quaternionalen projektiven Räume, S.-Ber. math.- naturw. Kl. Bayer. Akad. Wiss. München (1953), pp. 301–312.

2. ——, Neue topologische Methoden in der algebraischen Geometrie, Berlin, 1956.

3. M. MORSE, Relations between the numbers of critical points of a real function of $n$ independent variables, Trans. Amer. Math. Soc., 27 (1925), pp. 345-396.

4. N. STEENROD, The topology of fibre bundles, Princeton, 1951.

5. R. THOM, Quelques propriétés globale des variétés différentiables, Comment. Math. Helv., 28 (1954), pp. 17-86.

6. WU WEN-TSUN, Sur les classes caractéristiques des structures fibrées sphériques, Actual. sci. industr. 1183, Paris, 1952, pp. 5–89.

7. G. REEB, Sur certain propriétés topologiques des variétés feuilletées, Actual. sci. industr. 1183, Paris, 1952, pp. 91–154.