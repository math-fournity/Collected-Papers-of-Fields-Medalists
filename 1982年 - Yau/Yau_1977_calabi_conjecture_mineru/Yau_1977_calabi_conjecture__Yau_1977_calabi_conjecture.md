# Calabi's conjecture and some new results in algebraic geometry

(Kähler manifold/Chern class/Ricci tensor/complex structure)

SHING-TUNG YAU

Mathematics Department, Stanford University, Stanford, California 94305

Communicated by S. S. Chern, January 31, 1977

ABSTRACT We announce a proof of Calabi's conjectures on the Ricci curvature of a compact Kähler manifold and then apply it to prove some new results in algebraic geometry and differential geometry. For example, we prove that the only Kähler structure on a complex projective space is the standard one.

Let $M$ be a compact Kähler manifold with Kähler metric $\Sigma g_{ij} dz^i \otimes d\overline{z}^j$. Let $\Sigma R_{ij} dz^i \otimes d\overline{z}^j$ be the Ricci tensor of $M$. Then, according to Chern (ref. 1), the (1,1) form $\sqrt{-1}/2\pi \Sigma R_{ij} dz^i \Lambda d\overline{z}^j$ is closed and represents the first Chern class of $M$. Hence, there is a natural obstruction for a tensor to be the Ricci tensor of some Kähler metric. In refs. 2 and 3, Calabi asked whether this is the only obstruction. Namely, given a closed (1,1) form $\sqrt{-1}/2\pi \Sigma \widetilde{R}_{ij} dz^i \Lambda d\overline{z}^j$, which represents the first Chern class of $M$, can one find a Kähler metric $\Sigma \tilde{g}_{ij} dz^i \otimes d\overline{z}^j$ such that $\Sigma \tilde{R}_{ij} dz^i \otimes d\overline{z}^j$ is the Ricci tensor of this metric and that $\sqrt{-1}/2 \Sigma \tilde{g}_{ij} dz^i \Lambda d\overline{z}^j$ determines the same cohomology class as $\sqrt{-1/2} \Sigma g_{ij} dz^i \Lambda d\overline{z}^j$. Calabi (ref. 3) establishes the uniqueness of such a metric $\Sigma \tilde{g}_{ij} dz^i \otimes d\overline{z}^j$ and proved the existence under the assumption that $\tilde{R}_{ij}$ is close to $R_{ij}$. The existence of $\Sigma \tilde{g}_{ij} dz^i \otimes d\overline{z}^j$, without any assumption on $M$ or $\tilde{R}_{ij}$, is known as Calabi's conjecture.

Since $\sqrt{-1}/2\pi \Sigma \tilde{R}_{ij} dz^i \Lambda d\bar{z}^j = -\sqrt{-1}/2\pi \partial \overline{\sigma} \log \det [g_{ij} + (\partial^2 \varphi / \partial z^i \partial \bar{z}^j)]$, the condition that $\sqrt{-1}/2\pi \Sigma R_{ij} dz^i \Lambda d\bar{z}^j$ is cohomologous to $\sqrt{-1}/2\pi \Sigma R_{ij} dz^i \Lambda d\bar{z}^j$ implies that we can find a smooth function $F$ on $M$ so that

$$
\begin{array}{r l} - \frac {\sqrt {- 1}}{2 \pi} \partial \overline {{\sigma}} \log \det \left(g _ {i \bar {j}} + \frac {\partial^ {2} \varphi}{\partial z ^ {i} \partial \bar {z} ^ {j}}\right) \\ & + \frac {\sqrt {- 1}}{2 \pi} \partial \overline {{\sigma}} \log \det (g _ {i \bar {j}}) = \frac {\sqrt {- 1}}{2 \pi} \partial \overline {{\sigma}} F. \end{array}\tag{[1]}
$$

The conjecture of Calabi is therefore equivalent to solving [1] with $F$ and $g_{ij}$ given. Here $\varphi$ is required to be smooth so that $\Sigma_{r,j}[g_{ij} + (\partial^2\varphi/\partial z^i\partial\bar{z}^j)]dz^i \otimes d\bar{z}^j$ defines a metric tensor. Adding $F$ by a known constant, we see that it is sufficient to solve the following equation

$$
\det \left(g _ {i \bar {j}} + \frac {\partial^ {2} \varphi}{\partial z ^ {i} \partial \bar {z} ^ {j}}\right) \det \left(g _ {i \bar {j}}\right) ^ {- 1} = \exp (F)\tag{[2]}
$$

where

$$
\int_ {M} \exp (F) = \operatorname{Vol} (M).\tag{[3]}
$$

In ref. 2, Calabi also conjectured the existence of Kähler Einstein metric on a Kähler manifold whose first Chern class is negative, zero, or positive and which does not admit any holomorphic vector field. (A theorem of Nakano says that negativity of the first Chern class implies the nonexistence of holomorphic vector field.) Kähler Einstein metrics are the Kähler metrics whose Ricci form is proportional to the Kähler form. If the first Chern class is negative, then by definition we can choose Kähler metric so that $\sqrt{-1}/2\Sigma g_{ij}dz^{i}\Lambda d\bar{z}^{j}$ represents $-c_{1}(M)$. If $c_{1}(M)$ is zero, we choose $\sqrt{-1}/2\pi\Sigma g_{ij}dz^{i}$

$\Lambda\,d\bar{z}^{j}$ to be arbitrary Kähler form. If $c_{1}(M)$ is positive, we choose $\sqrt{-1/2}\,\Sigma\,g_{ij}^{i}\,dz^{i}\,\Lambda\,d\bar{z}^{j}$ to represent $c_{1}(M)$. In these cases, the existence of Kähler Einstein metric is equivalent to solving the following equation

$$
\det \left(g _ {i j} + \frac {\partial^ {2} \varphi}{\partial z ^ {i} \partial \bar {z} ^ {j}}\right) \det (g _ {i j}) ^ {- 1} = \exp (c \varphi + F)\tag{[4]}
$$

where $c = +1, 0$, or $-1$, and $F$ is a smooth function defined on $M$ that satisfies [3] when $c = 0$.

In this note, we announce the following solution of Calabi's conjecture.

THEOREM 1. Let M be a compact Kähler manifold with Kähler metric $\Sigma g_{ij} dz^i \otimes d\overline{z}^j$. Then when $c \geq 0$, eqs. 2 and 4 can be solved with a smooth $\varphi$. In particular, any (1,1) form on M that represents $c_1(M)$ can be realized as the Ricci form of a unique Kähler metric whose Kähler class is that of $\sqrt{-1/2} \Sigma g_{ij} dz^i \Lambda d\overline{z}^j$. If the first Chern class of M is zero and negative, then there exists a Kähler Einstein metric on M. In the latter case, if we require the Ricci curvature to be $-1$, the metric is unique, depending only on the complex structure of M.

We shall discuss Eq. 4 with c < 0 on a latter occasion. We should mention that if the bisectional curvature of M is nonnegative, then T. Aubin (ref. 4) has solved eq. 2. However, the class of such manifolds is rather restrictive. Very recently he also announced (ref. 5) a solution of a special case of [4] when c > 0.

Instead of giving details of how to prove Theorem 1, which will appear elsewhere, we shall now give some applications of Theorem 1. Some other applications will be published elsewhere also.

THEOREM 2. There are compact simply-connected Kähler manifolds whose Ricci curvature is identically zero and whose curvature tensor is not identically zero.

Proof: It is well known that for n > 1, every complex hypersurface of degree  $n + 2$  in the complex projective space  $Cp^{n+1}$  is simply connected and has zero first Chern class. Hence by Theorem 1, we can represent the zero (1,1) form as the Ricci tensor of some Kähler metric.

THEOREM 3. There are compact simply-connected Kähler manifolds whose Ricci curvature is negative everywhere.

Proof: For n > 1, any complex hypersurface of  $CP^{n+1}$  with degree greater than  $n + 2$  is simply connected and has negative first Chern class. Using Theorem 1, we can find a Kähler metric with negative Ricci curvature on them.

THEOREM 4. Let $\mathbf{M}$ be a Kähler surface with ample canonical bundle. Then $3\mathrm{c}_2(\mathbf{M}) \geq \mathrm{c}_1(\mathbf{M})^2$ and the equality holds if and only if $\mathbf{M}$ is covered biholomorphically by the ball in $C^2$.

Proof: According to Theorem 1, we can find a Kähler Einstein metric on $M$ whose Ricci curvature is a negative constant. By Chern's theorem (ref. 1), we can write $3c_{2}(M) - c_{1}^{2}(M)$ as the integral of a function that depends only on the curvature tensor of the above Einstein metric. This function can be described as follows. Let $\{e_1, e_2 = Je_1, e_3, e_4 = Je_3\}$ be a uni-

tary frame at a point $p$. Then the value of the function at $p$ is given by $1/4\pi^2\{[R_{1212} - 2(R_{1313} + R_{1414})]^2 + 3(R_{1313} - R_{1414})^2 + 6(R_{1312}^2 + R_{1412}^2 + R_{1413}^2)\}$. Since this function is non-negative, we have established the inequality $3c_2(M) \geq c_1^2(M)$. Furthermore, the equality holds iff the function is zero identically. As the Ricci curvature $R_{1212} + R_{1313} + R_{1414}$ is a negative constant, we see that in this case, the holomorphic sectional curvature of $M$ is a negative constant. Therefore, $M$ is covered by the ball holomorphically.

Remarks: (i) Under the assumption that $M$ is a surface of general type, Van de Ven (ref. 6) proved the inequality $8c_{2}(M) \geq c_{1}^{2}(M)$. Recently D. Mumford informed us that F. Bogomolv improved the inequality to $4c_{2}(M) \geq c_{1}^{2}(M)$ while Y. Miyaoka improved Bogomolov's argument to obtain $3c_{2}(M) \geq c_{1}^{2}(M)$. However, Miyaoka's argument does not give information for the case $3c_{2}(M) = c_{1}^{2}(M)$. We believe our method can be generalized to cover the case of general type. This will be discussed later.

(ii) Assuming the surface is Kähler Eistein, we knew the inequality  $3c_{2}(M) \geq c_{1}^{2}(M)$  about 4 years ago. However, it was pointed out by D. Mumford that more than 20 years ago, Guggenheimer (ref. 7) had already found the inequality, assuming the existence of Kähler Einstein metric.

(iii) We can generalize the above inequality to other inequalities for higher dimensional manifolds with ample canonical class. We can prove, for example, the inequality  $(-1)^{n}c_{1}^{n-2}c_{2}(M)\geq(-1)^{n}n/2(n+1)c_{1}^{n}(M)$ , and the equality holds only if M is covered by the ball holomorphically.

An important application of Theorem 4 is the following resolution of a conjecture of Severi (ref. 8)

THEOREM 5. Every complex surface that is homotopic to the complex projective plane $\mathbf{CP}^2$ is biholomorphic to $\mathbf{CP}^2$.

Proof: Since the index of a four-dimensional (real) manifold is invariant (up to sign) under homotopic equivalence, we conclude that  $\frac{1}{3}[c_{1}^{2}(M)-2c_{2}(M)]=\pm1$ . As  $c_{2}(M)=3$ , this shows immediately that  $c_{1}^{2}(M)>0$ . By a theorem of Kodaira (ref. 9) this implies that M is algebraic.

Let O be the structure sheaf of M. Then the exact sequence

$$
1 \rightarrow Z \rightarrow \mathcal {O} \rightarrow \mathcal {O} ^ {*} \rightarrow 1\tag{[5]}
$$

induces the long exact sequence

$$
H ^ {1} (M, Z) \rightarrow H ^ {1} (M, \mathcal {O}) \rightarrow H ^ {1} (M, \mathcal {O} ^ {*}) \rightarrow H ^ {2} (M, Z) \rightarrow\tag{[6]}
$$

Since  $H^{1}(M,Z)=0$  and  $H^{2}(M,Z)=Z$ , we have  $H^{1}(M,\mathcal{O})=0$  and  $H^{1}(M,\mathcal{O}^{*})$  is infinitely cyclic. Therefore, line bundles of M are multiples of each other. As M is algebraic, the canonical line bundle of M is a multiple of some positive line bundle. Therefore, the canonical line bundle is either negative or positive. In the previous case, Hirzebruch and Kodaira (ref. 9) already established that M is biholomorphic to  $CP^{2}$ . In both cases, they also established  $c_{1}(M)^{2}=9$ . Therefore, in the latter case  $3c_{2}(M)=c_{1}^{2}(M)$  and we can apply Theorem 4 to conclude that M is covered by the ball. As M is simply connected, we conclude that the latter case cannot happen and M is biholomorphic to  $CP^{2}$ .

Remark: We can apply the remark in Theorem 4 to prove that any Kähler manifold that is homeomorphic to  $CP^{n}$  is bi-holomorphic to  $CP^{n}$ . One can also prove that  $CP^{2}$  is the only

simply connected algebraic surface with positive definite index form (see ref. 6).

THEOREM 6. Let N be a compact complex surface that is covered by the ball in  $C_{2}$ . Then any complex surface M that is oriented homotopic to N is biholomorphic to N.

Proof: Since N is Kähler, the first Betti number of N, and hence M, is even. According to a result of Y. Miyaoka (ref. 10), our complex surface that is not covered by the K-3 surface is Kähler. We claim that the first Chern class of M is negative.

To see this, we notice the obvious fact that every compact holomorphic curve in a Kähler manifold is not homologous to zero in that manifold. We use this to show that M admits no rational curves or elliptic curves. In fact, it is well known that topologically, M is a  $K(\pi,1)$  whose fundamental group contains no nontrivial abelian subgroup besides the integers. Hence topologically, every continuous map from the rational curve or the elliptic curve into M must be homotopic to a map whose image is either a point or a circle. As a consequence, no nontrivial holomorphic map from a rational curve or elliptic curve into M is possible. According to the classification of complex surfaces, we conclude that M must be an algebraic surface of general type. On the other hand, for an algebraic surface of general type that contains no rational curves, the first Chern class is negative (see ref. 9).

Since $M$ is oriented homotopic to $N$, the index of $M$ is equal to that of $N$. One concludes immediately $c_1^2(M) = c_1^2(N)$ and $c_2(M) = c_2(N)$. Therefore, $3c_2(M) = c_1^2(M)$. Theorem 4 then shows that $M$ is covered by the ball in $\mathbf{C}^2$. By Mostow's rigidity theorem (ref. 11), $M$ is in fact biholomorphic to $N$.

This research was partially supported by a Sloan fellowship.

The costs of publication of this article were defrayed in part by the payment of page charges from funds made available to support the research which is the subject of the article. This article must therefore be hereby marked “advertisement” in accordance with 18 U. S. C. §1734 solely to indicate this fact.

1. Chern, S. S. (1946) "Characteristic classes of Hermitian manifolds," Ann. Math. 47, 85-121.

2. Calabi, E. (1954) "The space of Kähler metrics," Proc. Int. Congr. Math. Amsterdam 2, 206–207.

3. Calabi, E. (1955) On Kähler Manifolds with Vanishing Canonical Class, Algebraic Geometric and Topology, A Symposium in Honor of S. Lefschitz (Princeton Univ. Press, Princeton, NJ), pp. 78–89.

4. Aubin, T., (1970) "Métriques riemanniennes et courbure," J. Diff. Geom. 4, 383–424.

5. Aubin, T. (1976) "Equations du type Mongi-Ampère sur les variétés kähleriennes compactes," C. R. Acad. Sci. Hebd. Seances 283, 119–121.

6. Van de Ven, A. (1976) "On the Chern numbers of surfaces of general type," Invent. Math. 36, 285-293.

7. Guggenheimer, H. (1952) "Über vierdimensionale Einsteinräume," Experientia 8, 420–421.

8. Severi, F. (1954) Some remarks on the topological characterization of algebraic surfaces, in Studies presented to R. von Mises (Academic Press, New York), pp. 54–61; MR 16, p. 397.

9. Kodaira, K. (1975) Collected Works (Princeton Univ. Press, Princeton, NJ), Vols. II and III.

10. Miyaoka, Y. (1974) "Kähler metrics on elliptic surfaces," Proc. Jpn. Acad. Sci., 50.

11. Mostow, G. D. (1973) Strong Rigidity of Locally Symmetric Spaces (Princeton Univ. Press, Princeton, NJ).