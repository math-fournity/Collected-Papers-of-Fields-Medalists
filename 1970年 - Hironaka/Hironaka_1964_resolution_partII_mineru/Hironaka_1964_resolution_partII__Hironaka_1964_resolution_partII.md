## Annals of Mathematics

Resolution of Singularities of an Algebraic Variety Over a Field of Characteristic Zero: II Author(s): Heisuke Hironaka  
Source: Annals of Mathematics, Second Series, Vol. 79, No. 2 (Mar., 1964), pp. 205-326  
Published by: Annals of Mathematics  
Stable URL: http://www.jstor.org/stable/1970547  
Accessed: 08/09/2013 03:49

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# RESOLUTION OF SINGULARITIES OF AN ALGEBRAIC VARIETY OVER A FIELD OF CHARACTERISTIC ZERO: II

BY HEISUKE HIRONAKA
(Part I appeared in the preceding issue of this Journal)

## CHAPTER III. EFFECTS OF PERMISSIBLE MONOIDAL TRANSFORMATIONS ON SINGULARITIES.

## 1. The numerical characters $\nu^{*}(\mathbf{J})$ and $\nu(\mathbf{J})$ of a local ideal J, and a standard base of J

Let R be a regular local ring and J an ideal in R. Let M be the maximal ideal of R. We have defined the homogeneous ideal  $\mathrm{gr}_{\mathbf{M}}(\mathbf{J}, \mathbf{R})$  in the graded R/M-algebra  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ .

DEFINITION 1. Given R and J as above, we define $\nu^{(i)}(\mathbf{J})$, (a non-negative integer or infinity, $\infty$ in symbol) for every positive integer $i$ as follows: $\nu^{(i)}(\mathbf{J})$ is the maximal integer $\nu$, if it exists, such that there exists a system of homogeneous elements $(\varphi_1,\varphi_2,\cdots,\varphi_{i-1})$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{J},\mathbf{R})$ having the property that

$$
\left(\varphi_ {1}, \dots , \varphi_ {i - 1}\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}) \cap \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {R}) = \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {J}, \mathbf {R})
$$

for all $\mu < \nu$; and, if such $\nu$ does not exist, we set $\nu^{(i)}(\mathbf{J}) = \infty$. (An empty system of elements generates the zero ideal.)

LEMMA 1. Let $(\varphi_{1},\cdots,\varphi_{m})$ be a system of homogeneous elements of $\mathrm{gr}_{\mathbf{M}}(\mathbf{J},\mathbf{R})$ such that

(i)  $\mathrm{gr}_{\mathbf{M}}(\mathbf{J},\mathbf{R})=(\varphi_{1},\cdots,\varphi_{m})\mathrm{gr}_{\mathbf{M}}(\mathbf{R}),$

(ii) if $\nu_{i} = \deg \varphi_{i}(1\leq i\leq m)$, then $\nu_{1}\leq \nu_{2}\leq \dots \leq \nu_{m}$, and

(iii) for every  $i \geq 1$ ,  $\varphi_{i} \notin (\varphi_{1}, \cdots, \varphi_{i-1}) \operatorname{gr}_{\mathbf{M}}(\mathbf{R})$  (where the empty system of elements generates the zero ideal). Then we have  $\nu^{(i)}(\mathbf{J}) = \nu_{i}$  for  $1 \leq i \leq m$  and  $\nu^{(i)}(\mathbf{J}) = \infty$  for all i > m.

PROOF. Let $\mu_{i} = \nu^{(i)}(\mathbf{J})$. In view of (i) and (ii), it is clear from Definition 1 that $\nu_{i} \leq \mu_{i}$ for all $i$ ($1 \leq i \leq m$), and also that $\mu_{i} = \infty$ for all $i > m$. Suppose we have $i$ ($1 \leq i \leq m$) such that $\mu_{i} > \nu_{i}$. Let $i$ be the smallest integer with this property. By Definition 1, we have homogeneous elements $\psi_{1}, \cdots, \psi_{i-1}$ such that

$$
\left(\psi_ {1}, \dots , \psi_ {i - 1}\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}) \cap \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {R}) = \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {J}, \mathbf {R})
$$

for all  $\mu < \mu_{i}$ . We may assume that  $\deg \psi_{1} \leq \cdots \leq \deg \psi_{i-1}$ . Then, for every j < i, we have

$$
\left(\psi_ {1}, \dots , \psi_ {j - 1}\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}) \cap \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {R}) = \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {J}, \mathbf {R})
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  cf. §2, Chap. II.</span></small>

for all $\mu < \deg \psi_j$. Hence, by Definition 1, we have $\deg \psi_j \leq \mu_j = \nu_j$. Thus $\deg \psi_j \leq \nu_j$ for all $j < i$. Let $k$ be the largest integer such that $\nu_i = \nu_k$. We have $k \geq i$ and

$$
\left(\varphi_ {1}, \dots , \varphi_ {k}\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}) \cap \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {R}) = \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {J}, \mathbf {R})
$$

for all $\mu \leq \nu_{i} = \nu_{k} < \mu_{i}$. Hence we have

$$
\left(\psi_ {1}, \dots , \psi_ {i - 1}\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}) \cap \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {R}) = \left(\varphi_ {1}, \dots , \varphi_ {k}\right) \operatorname{gr} (\mathbf {R}) \cap \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {R})
$$

for all $\mu \leq \nu_{k}$. Let $s$ be the smallest positive integer such that $\nu_{s} = \nu_{i} (= \nu_{k})$. Then $s \leq i$. Let $\{\psi_{t}\}$ be those which have $\deg \psi_{t} = \nu_{i}$. Then for each $j$ with $s \leq j \leq k$, there exists a linear combination $L_{j}$ of those $\psi_{t}$ with coefficients in $\mathbf{R} / \mathbf{M}$ such that $\varphi_{j} - L_{j}$ is contained in the ideal in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ generated by those $\psi_{n}$ with $\deg \psi_{n} < \nu_{i}$. Hence by the above equality for $\mu < \nu_{i} = \nu_{k}$, $\varphi_{j} - L_{j}$ is contained in $(\varphi_{1}, \cdots, \varphi_{s-1})\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$. (Here, any linear combination of empty set of elements means to be zero.) Since we have $\deg \psi_{j} \leq \nu_{j}$ for all $j$, the number of elements in $\{\psi_{t}\}$ is less than $k - s + 1$. Therefore, some non-zero linear combination of $\varphi_{s}, \varphi_{s+1}, \cdots, \varphi_{k}$ with coefficients in $\mathbf{R} / \mathbf{M}$ must be in the ideal $(\varphi_{1}, \cdots, \varphi_{s-1})\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$. Hence, there exists $j (s \leq j \leq k)$ such that

$$
\varphi_ {j} \in (\varphi_ {1}, \dots , \varphi_ {j - 1}) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}).
$$

This contradicts (iii). q.e.d.

LEMMA 2. Let A be a noetherian ring, J and I ideals in A. Let $\alpha: \mathbf{A} \to \mathbf{A}'$ be a homomorphism of noetherian rings such that $\alpha(\mathbf{I})$ is contained in the Jacobson radical of $\mathbf{A}'$. Let $\mathbf{J}' = \mathbf{J}\mathbf{A}'$ and $\mathbf{I}' = \mathbf{I}\mathbf{A}'$. Let $\tilde{\alpha}$ be the canonical homomorphism of graded algebras $\mathrm{gr}_{\mathbf{I}}(\mathbf{A}) \to \mathrm{gr}_{\mathbf{I}'}(\mathbf{A}')$ which is induced by $\alpha$. If $\mathbf{A}'$ is flat over $\mathbf{A}$, then $\tilde{\alpha}(\mathrm{gr}_{\mathbf{I}}(\mathbf{J}, \mathbf{A}))$ generates the ideal $\mathrm{gr}_{\mathbf{I}'}(\mathbf{J}', \mathbf{A}')$.

PROOF. We have the following commutative diagram of canonical homomorphisms:

![](images/page_2_image_9.jpg)

where the right vertical sequence is exact while the left vertical sequence is also exact because  $\mathrm{gr}_{\mathrm{I}}^{0}(\mathbf{A}^{\prime}) = \mathbf{A}^{\prime}/\mathbf{I}^{\prime}$  is flat over A/I. (See Lemma 5, §2, Ch. II.) By Lemma 2, §1, Ch. II,  $\varphi$  is an isomorphism, because  $A^{\prime}$  is flat over A and  $\alpha(\mathbf{I})$  is contained in the Jacobson radical of  $A^{\prime}$ . By the same reason applied to  $A/J \to A^{\prime}/J^{\prime}$  (induced by  $\alpha$ ),  $\varphi^{\prime}$  must be an isomorphism. Therefore the mapping  $\varphi^{\prime\prime}$  must be surjective. This means that the image of  $\mathrm{gr}_{\mathrm{I}}(\mathbf{J}, \mathbf{A})$  by the canonical homomorphism  $\tilde{\alpha}: \mathrm{gr}_{\mathrm{I}}(\mathbf{A}) \to \mathrm{gr}_{\mathrm{I}^{\prime}}(\mathbf{A}^{\prime})$  generates the ideal  $\mathrm{gr}_{\mathrm{I}^{\prime}}(\mathbf{J}^{\prime}, \mathbf{A}^{\prime})$ . q.e.d.

COROLLARY. Let $\alpha: \mathbf{R} \to \mathbf{R}'$ be a local homomorphism of regular local rings which transforms a regular system of parameters of $\mathbf{R}$ into such a system of parameters of $\mathbf{R}'$. Let $\mathbf{J}$ be an ideal in $\mathbf{R}$ and $\mathbf{J}'$ the ideal in $\mathbf{R}'$ generated by $\alpha(\mathbf{J})$. Then we have $\nu^{(i)}(\mathbf{J}) = \nu^{(i)}(\mathbf{J}')$ for all $i$.

PROOF. Let M (resp. M') denote the maximal ideal of R (resp. R'). The local homomorphism  $\alpha$  induces a canonical homomorphism  $\tilde{\alpha}:\mathrm{gr}_{\mathbf{M}}(\mathbf{R})\to\mathrm{gr}_{\mathbf{M}'}(\mathbf{R}')$ . The assumption on  $\alpha$  implies that  $R'$  is flat over R. Therefore  $\tilde{\alpha}(\mathrm{gr}_{\mathbf{M}}(\mathbf{J},\mathbf{R}))$  generates the ideal  $\mathrm{gr}_{\mathbf{M}'}(\mathbf{J}',\mathbf{R}')$ . We have a system of elements  $(f_{1},\cdots,f_{m})$  of J such that: if  $\varphi_{j}=$  the initial form of  $f_{j}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  for  $1\leq j\leq m$ , then the system  $(\varphi_{1},\varphi_{2},\cdots,\varphi_{m})$  possesses the properties (i), (ii), and (iii) of Lemma 1. We can easily see that  $\tilde{\alpha}(\varphi_{j})=$  the initial form of  $\alpha(f_{j})$  in  $\mathrm{gr}_{\mathbf{M}'}(\mathbf{R}')$  for  $1\leq j\leq m$ . Then we claim that the system  $(\tilde{\alpha}(\varphi_{1}),\cdots,\tilde{\alpha}(\varphi_{m}))$  possesses the properties (i), (ii), and (iii) of Lemma 1 for  $\mathrm{gr}_{\mathbf{M}'}(\mathbf{J}',\mathbf{R}')$ , too. In fact, (i) and (ii) are clear from the canonical isomorphism

$$
\varphi \colon \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}) \otimes_ {\mathbf {R} / \mathbf {M}} \mathbf {R} ^ {\prime} / \mathbf {M} ^ {\prime} \longrightarrow \operatorname{gr} _ {\mathbf {M} ^ {\prime}} (\mathbf {R} ^ {\prime}),
$$

and (iii) is clear from the fact that $\tilde{\alpha} (\mathrm{gr}_{\mathbf{M}}(\mathbf{J},\mathbf{R}))$ generates $\mathrm{gr}_{\mathbf{M}^{\prime}}(\mathbf{J}^{\prime},\mathbf{R}^{\prime})$. q.e.d.

DEFINITION 2. Given an ideal J in a regular local ring R, the sequence $\{\nu^{(i)}(\mathbf{J})\}_{i\in \mathbf{Z}^{+}}(\mathbf{Z}^{+} =$ the ordered set of positive integers) will be denoted by $\nu^{*}(\mathbf{J})$. We define the lexicographical ordering in the set of sequences $\nu^{*} = \{\nu^{(i)}\}_{i\in \mathbf{Z}^{+}}$ where $\nu^{(i)}$ are either integers or $\infty$; namely, for given $\nu_{1}^{*} = \{\nu_{1}^{(i)}\}$ and $\nu_{2}^{*} = \{\nu_{2}^{(i)}\}$, we say that $\nu_{1}^{*} > \nu_{2}^{*}$ if there exists a positive integer $i$ such that $\nu_{1}^{(j)} = \nu_{2}^{(j)}$ for all $j < i$ and $\nu_{1}^{(i)} > \nu_{2}^{(i)}$

LEMMA 3. Let $\mathbf{J}_1$ and $\mathbf{J}_2$ be the two ideals in a regular local ring $\mathbf{R}$ such that $\mathbf{J}_1 \subseteq \mathbf{J}_2$. Let $\nu_i^* = \{\nu^{(j)}(\mathbf{J}_i)\}_{j \in \mathbb{Z}^+}$ for $i = 1, 2$. Then we have $\nu_1^* \geq \nu_2^*$. Moreover, $\nu_1^* = \nu_2^*$ if and only if $\mathbf{J}_1 = \mathbf{J}_2$.

PROOF. It is clear that  $\mathrm{gr}_{\mathbf{M}}(\mathbf{J}_{1},\mathbf{R})\subseteq\mathrm{gr}_{\mathbf{M}}(\mathbf{J}_{2},\mathbf{R})$ . If  $\mathrm{gr}_{\mathbf{M}}(\mathbf{J}_{1},\mathbf{R})=\mathrm{gr}_{\mathbf{M}}(\mathbf{J}_{2},\mathbf{R})$ , then  $\nu_{1}^{*}=\nu_{2}^{*}$ . Suppose  $\mathrm{gr}_{\mathbf{M}}(\mathbf{J}_{1},\mathbf{R})\neq\mathrm{gr}_{\mathbf{M}}(\mathbf{J}_{2},\mathbf{R})$ . Let  $(\varphi_{1},\cdots,\varphi_{m})$  be a system of elements of  $\mathrm{gr}_{\mathbf{M}}(\mathbf{J}_{1},\mathbf{R})$  which has the properties (i), (ii),

and (iii) of Lemma 1. Let $\nu_{i} = \nu^{(i)}(\mathbf{J}_{1})$ which is $\deg \varphi_{i}$ for $1 \leq i \leq m$ and $\infty$ for $i > m$. Let $s$ be the smallest integer such that $\mathrm{gr}_{\mathbf{M}}^{s}(\mathbf{J}_{1}, \mathbf{R}) \neq \mathrm{gr}_{\mathbf{M}}^{s}(\mathbf{J}_{2}, \mathbf{R})$. Let $j$ be the largest integer such that $\nu_{j} \leq s$. Then

$$
\operatorname{gr} _ {\mathbf {M}} ^ {\mu} \left(\mathbf {J} _ {2}, \mathbf {R}\right) = \operatorname{gr} _ {\mathbf {M}} ^ {\mu} \left(\mathbf {J} _ {1}, \mathbf {R}\right) = \left(\varphi_ {1}, \dots , \varphi_ {j}\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}) \cap \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {R}),
$$

for all $\mu < s$, and

$$
\operatorname{gr} _ {\mathbf {M}} ^ {s} \left(\mathbf {J} _ {2}, \mathbf {R}\right) \supseteq \operatorname{gr} _ {\mathbf {M}} ^ {s} \left(\mathbf {J} _ {1}, \mathbf {R}\right) = \left(\varphi_ {1}, \dots , \varphi_ {j}\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}) \cap \operatorname{gr} _ {\mathbf {M}} ^ {s} (\mathbf {R}).
$$

Therefore, we have $\psi \in \mathrm{gr}_{\mathbf{M}}^{s}(\mathbf{J}_{2}, \mathbf{R})$ such that $(\varphi_{1}, \cdots, \varphi_{j}, \psi)$ can be extended to a system of elements of $\mathrm{gr}_{\mathbf{M}}(\mathbf{J}_{2}, \mathbf{R})$ which has the properties (i), (ii), and (iii) of Lemma 1. Thus we have $\nu^{(i)}(\mathbf{J}_{2}) = \nu^{(i)}(\mathbf{J}_{1})$ for $i \leq j$ and $\nu^{(j+1)}(\mathbf{J}_{2}) = s < \nu^{(j+1)}(\mathbf{J}_{1})$, so that $\nu_{2}^{*} < \nu_{1}^{*}$. In particular, $\nu_{2}^{*} = \nu_{1}^{*}$ implies $\mathrm{gr}_{\mathbf{M}}(\mathbf{J}_{1}, \mathbf{R}) = \mathrm{gr}_{\mathbf{M}}(\mathbf{J}_{2}, \mathbf{R})$. We then claim $\mathbf{J}_{1} = \mathbf{J}_{2}$. It is sufficient to show that $\mathbf{J}_{2} \subseteq \mathbf{J}_{1} + \mathbf{M}^{n}$ for all positive integer $n$. For this, we have only to prove that, if $\mathbf{J}_{2} \subseteq \mathbf{J}_{1} + \mathbf{M}^{n}$ for a certain $n$, then $\mathrm{gr}_{\mathbf{M}}(\mathbf{J}_{1}, \mathbf{R}) = \mathrm{gr}_{\mathbf{M}}(\mathbf{J}_{2}, \mathbf{R})$ implies $\mathbf{J}_{2} \subseteq \mathbf{J}_{1} + \mathbf{M}^{n+1}$. Let $g$ be any element of $\mathbf{J}_{2}$. Then we have $f_{1} \in \mathbf{J}_{1}$ such that $g - f_{1} \in \mathbf{M}^{n}$. Therefore to prove that $g \in \mathbf{J}_{1} + \mathbf{M}^{n+1}$, we may assume that $\nu_{\mathbf{M}}(g) = n$. Let $\psi$ be the initial form of $g$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$, which is of degree $n$. Then $\psi \in \mathrm{gr}_{\mathbf{M}}^{n}(\mathbf{J}_{2}, \mathbf{R}) = \mathrm{gr}_{\mathbf{M}}^{n}(\mathbf{J}_{1}, \mathbf{R})$. Hence there exists $f \in \mathbf{J}_{1}$ such that $\psi =$ the initial form of $f$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$. Clearly $g - f \in \mathbf{M}^{n+1}$. Thus $\mathbf{J}_{2} \subseteq \mathbf{J}_{1} + \mathbf{M}^{n+1}$. q.e.d.

COROLLARY. If  $(f_{1},\cdots,f_{m})$  is a system of elements of J such that their initial forms  $(\varphi_{1},\cdots,\varphi_{m})$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  have the properties (i), (ii), and (iii) of Lemma 1, then  $\mathbf{J}=(f_{1},\cdots,f_{m})\mathbf{R}$ .

DEFINITION 3. Let J be an ideal in a regular local ring R. Then a system of elements  $(f_{1},\cdots,f_{m})$  of J  $(m\geq0)$  is called a standard base of J if the system of their initial forms in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  has the properties (i), (ii), and (iii) of Lemma 1.

REMARK. As is easily seen, we have $\nu^{(1)}(\mathbf{J}) = \min_{f\in \mathbf{J}}\{\nu_{\mathbf{M}}(f)\}$, i.e., $\nu^{(1)}(\mathbf{J}) = \nu (\mathbf{J})$. Moreover, we can see that $\nu^{(2)}(\mathbf{J})$ is the largest integer $\nu (\mathrm{or}\infty)$ such that there exists $f_{1}\in \mathbf{J}$ with the property: $\mathbf{J}\subseteq (f_1)\mathbf{R} + \mathbf{M}^{\nu}$. In fact, it is trivial if $\mathbf{J} = (0)$. So we assume that $\mathbf{J}\neq (0)$. Let $\nu_{1} = \nu^{(1)}(\mathbf{J}) = \nu (\mathbf{J})$. Suppose we have $f_{1}\in \mathbf{J}$ such that $\mathbf{J}\subseteq (f_1)\mathbf{R} + \mathbf{M}^{\nu}$ with $\nu \geq \nu_{1}$. We claim $\nu^{(2)}(\mathbf{J})\geq \nu$. If $\nu = \nu_{1}$, then $\nu^{(2)}(\mathbf{J})\geq \nu$ is clear. We may assume that $\nu >\nu_{1}$ and hence $\nu_{\mathbf{M}}(f_1) = \nu_{1}$. Let $g$ be any element of $\mathbf{J}$. We have $h\in \mathbf{R}$ such that $g - hf_1\in \mathbf{M}^\nu$. Hence the initial form of $g$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ is equal to the product of the initial forms of $h$ and $f_{1}$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$, provided $\nu_{\mathbf{M}}(g) < \nu$. Hence, if $\varphi_{1}$ is the initial form of $f_{1}$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$, then $\mathrm{gr}_{\mathbf{M}}^{\mu}(\mathbf{J},\mathbf{R}) = (\varphi_{1})\mathrm{gr}_{\mathbf{M}}(\mathbf{R})\cap \mathrm{gr}_{\mathbf{M}}^{\mu}(\mathbf{R})$ for all $\mu < \nu$. Hence $\nu \leq \nu^{(2)}(\mathbf{J})$. For the converse,

the following is true in general. Given a positive integer $i$, $\nu^{(i)}(\mathbf{J})$ is at most the maximum (or $\infty$), $\nu_{(i)}(\mathbf{J})$ in symbol, of those $\nu$ for which there exists a system of elements $(f_1, \cdots, f_{i-1})$ of $\mathbf{J}$ such that

$$
\mathbf {J} \subseteq (f _ {1}, \dots , f _ {i - 1}) \mathbf {R} + \mathbf {M} ^ {\nu}.
$$

In fact, we take a standard base  $(f_{1}, \cdots, f_{m})$  of J, which necessarily has the property that

$$
(f _ {1}, \dots , f _ {i - 1}) \mathbf {R} + \mathbf {M} ^ {\nu^ {(i)} (\mathbf {J})} \supseteq \mathbf {J}.
$$

(See the proof of Lemma 3.) The assertion is clear. We remark that $\nu^{(3)}(\mathbf{J})$ can be smaller than $\nu_{(3)}(\mathbf{J})$, and the same for $\nu^{(i)}(\mathbf{J})$ and $\nu_{(i)}(\mathbf{J})$ if $i > 2$. For example, let $\mathbf{R} = \mathbf{k}\{x, y, z_1, z_2\}$ be a formal power series ring of four variables over a field $\mathbf{k}$. Let $\mathbf{J}$ be the ideal generated by $f_1 = z_1z_2 + x^3$ and $f_2 = z_1(z_1 + z_2) + y^3$. Then we have $h = (z_1 + z_2)f_1 - z_2f_2 = (z_1 + z_2)x^3 - z_2y^3 \in \mathbf{J}$. We can prove that $\nu^{(1)}(\mathbf{J}) = \nu_{(1)}(\mathbf{J}) = 2$, $\nu^{(2)}(\mathbf{J}) = \nu_{(2)}(\mathbf{J}) = 2$ but $\nu^{(3)}(\mathbf{J}) = 4$ while $\nu_{(3)}(\mathbf{J}) = \infty$.

DEFINITION 4. Let V be a subscheme of a non-singular algebraic scheme X. Let x be a point of V,  $R_{x}$  the local ring of X at x (which is regular) and  $J_{x}$  the ideal of V in  $R_{x}$ . Then we shall denote  $\nu^{*}(J_{x})$  by  $\nu_{x}^{*}(V/X)$ .

## 2. The strict and weak transforms of a local ideal

Let R be a regular local ring and P a prime ideal in R such that  $P \neq (0)$  and S = R/P is regular. By a monoidal transform of R with center P, we shall mean a local ring in the field of quotients of R which is obtained as a localization of a ring of the form  $R[x^{-1}P]$  with  $x \in P$  with respect to a prime ideal in  $R[x^{-1}P]$  containing the maximal ideal of R. In this definition of monoidal transform, it is convenient to include the case in which P = R. In this case, the monoidal transform of R is canonically isomorphic to R. Note that we have also such an isomorphism when P is principal. If  $(x_{1}, \cdots, x_{r})$  is a minimal base of the prime ideal P and if  $R'$  is a monoidal transform of R with center P, then there exist an index  $i (1 \leq i \leq r)$  and a prime ideal  $M'$  in  $R[x_{1}/x_{i}, x_{2}/x_{i}, \cdots, x_{r}/x_{i}]$  such that  $R' = R[x_{1}/x_{i}, \cdots, x_{r}/x_{i}]_{M'}$  and  $M' \supseteq MR'[x_{1}/x_{i}, \cdots, x_{r}/x_{i}]$  where M = the maximal ideal of R. It is clear that the canonical injection  $R \to R'$  is a local homomorphism.

Let  $A' = R[x_{2}/x_{1}, \cdots, x_{r}/x_{1}]$  and  $R' = A'M'$  with a prime ideal  $M'$  in  $A'$  which contains  $MA'$ . It is well known that:  $\mathbf{PA}' = (x_{1})\mathbf{A}'$  and  $\mathbf{A}'/(x_{1})\mathbf{A}'$  is canonically isomorphic to a polynomial ring of  $(r - 1)$  variables  $S[X_{2}, \cdots, X_{r}]$  over S = R/P, where the residue class of  $x_{i}/x_{1}$  corresponds to  $X_{i}$  ( $2 \leq i \leq r$ ). Let us identify  $\mathbf{A}'/(x_{1})\mathbf{A}'$  with  $S[X_{2}, \cdots, X_{r}]$ . Then

$\bar{\mathbf{M}}' = \mathbf{M}'/(x_1)\mathbf{A}'$ is a prime ideal in $S[X_2, \cdots, X_r]$ which contains the maximal ideal of S. Since S is regular, the polynomial ring $S[X_2, \cdots, X_r]$ over S is also regular. Hence $S[X_2, \cdots, X_r]_{\bar{\mathbf{M}}'} = \mathbf{R}'/(x_1)\mathbf{R}'$ is regular and so is $R'$. Let $\bar{\mathbf{M}} = \mathbf{M}/\mathbf{P}$, $k = S/\bar{\mathbf{M}} = R/M$, and $\bar{\mathbf{m}}' = \bar{\mathbf{M}}'/\bar{\mathbf{MS}}[X_2, \cdots, X_r]$. $S[X_2, \cdots, X_r]/\bar{\mathbf{MS}}[X_2, \cdots, X_r]$ can be identified with the polynomial ring $k[X_2, \cdots, X_r]$ of (r-1) variables over the field $k$, and $\bar{\mathbf{m}}'$ is then a prime ideal in $k[X_2, \cdots, X_r]$. Let $t = \dim(k[X_2, \cdots, X_r]_{\bar{\mathbf{m}}'})$, and choose a system of elements $(f_1, \cdots, f_t)$ of $M'$ such that their images in $k[X_2, \cdots, X_r]$ form a regular system of parameters of $k[X_2, \cdots, X_r]_{\bar{\mathbf{m}}'}$. Let us also choose a system of elements $(y_1, \cdots, y_s)$ of R such that their images in S form a regular system of parameters of S. Then we can easily see that $(x_1, y_1, \cdots, y_s, f_1, \cdots, f_t)$ is a regular system of parameters of $R'$. It follows that, for $M'$ and $R'$ as above, $\dim R' = \dim R$ if and only if $M'$ is a maximal ideal in $A'$.

Let $\mathbf{R}'$ be a monoidal transform of $\mathbf{R}$ with center $\mathbf{P}$ as above. Then we see that $\dim \mathbf{R} = \dim \mathbf{R}'$ if and only if the residue field of $\mathbf{R}'$ is algebraic (necessarily, of finite degree) over that of $\mathbf{R}$. In general for a pair of local rings $\mathbf{R}$ and $\mathbf{R}'$ with a local homomorphism of $\mathbf{R}$ into $\mathbf{R}'$, $\mathbf{R}'$ will be said to be residually algebraic (resp. residually rational) over $\mathbf{R}$ if the residue field of $\mathbf{R}'$ is algebraic (resp. algebraic of degree 1) over that of $\mathbf{R}$. By the above argument, we can easily show that if $\mathbf{R}'$ is a monoidal transform of $\mathbf{R}$ with center $\mathbf{P}$ which is residually rational over $\mathbf{R}$, then there exists a regular system of parameters $(x_1, x_2, \cdots, x_r, y_1, y_2, \cdots, y_s)$ of $\mathbf{R}$, where $r + s = \dim \mathbf{R}$, such that $\mathbf{P} = (x_1, x_2, \cdots, x_r)\mathbf{R}$ and that $(x_1, x_2 / x_1, \cdots, x_r / x_1, y_1, \cdots, y_s)$ is a regular system of parameters of $\mathbf{R}'$.

Let $\alpha: \mathbf{R} \to \widetilde{\mathbf{R}}$ be a local homomorphism of regular local rings $\mathbf{R}$ and $\widetilde{\mathbf{R}}$ such that $\alpha$ transforms a regular system of parameters of $\mathbf{R}$ to such a system of $\widetilde{\mathbf{R}}$. Then we can easily show that if $\mathbf{P}$ is a prime ideal in $\mathbf{R}$ such that $\mathbf{R}/\mathbf{P}$ is regular, then $\widetilde{\mathbf{P}} = \mathbf{P}\widetilde{\mathbf{R}}$ is a prime ideal of $\widetilde{\mathbf{R}}$ such that $\widetilde{\mathbf{R}}/\widetilde{\mathbf{P}}$ is regular. Let $(x_1, \cdots, x_r)$ be a minimal base of $\mathbf{P}$ and extend it to a regular system of parameters of $\mathbf{R}$, say $(x_1, \cdots, x_r, y_1, \cdots, y_s)$. Then $(\alpha(x_1), \cdots, \alpha(x_r))$ is a minimal base of the ideal $\widetilde{\mathbf{P}}$ and $(\alpha(x_1), \cdots, \alpha(x_r), \alpha(y_1), \cdots, \alpha(y_s))$ is a regular system of parameters of $\widetilde{\mathbf{R}}$. Let $\mathbf{A}' = \mathbf{R}[x_2/x_1, \cdots, x_r/x_1]$ and $\widetilde{\mathbf{A}}' = \widetilde{\mathbf{R}}[\alpha(x_2)/\alpha(x_1), \cdots, \alpha(x_r)/\alpha(x_1)]$. Let $\mathbf{M}'$ be a prime ideal in $\mathbf{A}'$ which contains $\mathbf{MA}'$, where $\mathbf{M} =$ the maximal ideal of $\mathbf{R}$. Let $\bar{\mathbf{m}}' = \mathbf{M}'/(x_1, y_1, \cdots, y_s)\mathbf{A}' = \mathbf{M}'/\mathbf{MA}' (= \bar{\mathbf{M}}'/\bar{\mathbf{MS}}[X_2, \cdots, X_r])$ as before. The local homomorphism $\alpha$ induces a monomorphism of the residue field $\mathbf{k}$ of $\mathbf{R}$ into the residue field $\widetilde{\mathbf{k}}$ of $\widetilde{\mathbf{R}}$. We can identify $\mathbf{A}'/(x_1, y_1, \cdots, y_s)\mathbf{A}'$ with $\mathbf{k}[X_2, \cdots, X_r]$ as above, and similarly $\widetilde{\mathbf{A}}'/(a(x_1), a(y_1), \cdots, a(y_s))\widetilde{\mathbf{A}}'$

with  $\widetilde{k}[X_{2},\cdots,X_{r}]$ . The homomorphism  $A'\to\widetilde{A}'$ , induced by  $\alpha$ , induces a homomorphism of  $k[X_{2},\cdots,X_{r}]$  into  $\widetilde{k}[X_{2},\cdots,X_{r}]$  which maps k into  $\widetilde{k}$  as above and  $X_{j}$  into itself for  $2\leqq j\leqq r$ . The associated prime ideals of  $M'\widetilde{A}'$  correspond to the associated prime ideals of  $\bar{m}'k[X_{2},\cdots,X_{r}]$  in a one to one fashion by the natural homomorphism of  $\widetilde{A}'$  onto  $\widetilde{k}[X_{2},\cdots,X_{r}]$ . We note here that all the associated prime ideals of  $\bar{m}'\widetilde{k}[X_{2},\cdots,X_{r}]$  are isolated because  $\bar{m}'$  is a prime ideal in  $k[X_{2},\cdots,X_{r}]$ . It is easily seen that if  $\widetilde{M}'$  is an associated prime ideal of  $M'\widetilde{A}'$ , then we have a canonical local homomorphism of  $R'=A'_{M'}$  into  $\widetilde{R}'=\widetilde{A}'_{\widetilde{M'}}$ , and that if either  $\widetilde{k}$  or  $R'/M'R'$  is algebraic over k, then every monoidal transform  $\widetilde{R}'$  of  $\widetilde{R}$  with center  $\widetilde{P}$ , which admits a canonical local homomorphism  $R'\to\widetilde{R}'$ , can be obtained in this manner. Here, given a monoidal transform  $R'$  (resp.  $\widetilde{R}'$ ) of R (resp.  $\widetilde{R}$ ) with center P (resp.  $\widetilde{P}$ ), we say that a local homomorphism  $R'\to\widetilde{R}'$  is canonical if the following diagram is commutative:

![](images/page_7_image_1.jpg)

Therefore, if either $\widetilde{\mathbf{R}}$ or $\mathbf{R}'$ is residually algebraic over $\mathbf{R}$, then the number of $\widetilde{\mathbf{R}}'$ which admit a canonical local homomorphism $\mathbf{R}' \to \widetilde{\mathbf{R}}'$ is equal to the number of the associated prime ideals of $\overline{\mathbf{m}}' \widetilde{\mathbf{k}}[X_2, \cdots, X_r]$, which is obviously finite. In particular, if $\widetilde{\mathbf{R}}$ is residually algebraic over $\mathbf{R}$, then this number does not exceed the separable degree of the residue field extension $\mathbf{k} \to \widetilde{\mathbf{k}}$. Let $\mathbf{k}[\bar{X}_2, \cdots, \bar{X}_r]$ (resp. $\widetilde{\mathbf{k}}[\bar{X}_2, \cdots, \bar{X}_r]$) denote the residue class ring of $\mathbf{k}[X_2, \cdots, X_r]$ modulo $\overline{\mathbf{m}}' \mathbf{k}[X_2, \cdots, X_r]$ (resp. $\widetilde{\mathbf{k}}[X_2, \cdots, X_r]$ modulo $\overline{\mathbf{m}}' \widetilde{\mathbf{k}}[X_2, \cdots, X_r]$). Then we have a canonical isomorphism of $\widetilde{\mathbf{k}} \otimes_{\mathbf{k}} \mathbf{k}[\bar{X}_2, \cdots, \bar{X}_r]$ to $\widetilde{\mathbf{k}}[\bar{X}_2, \cdots, \bar{X}_r]$. Let $\widetilde{\mathbf{M}}'$ be a prime ideal in $\widetilde{\mathbf{A}}'$ such that $\widetilde{\mathbf{R}}' = \widetilde{\mathbf{A}}'_{\widetilde{\mathbf{M}}}.$ admits a canonical local homomorphism $\mathbf{R}' \to \widetilde{\mathbf{R}}'$. Then $\widetilde{\mathbf{M}}'$ contains the kernel of the natural homomorphism of $\widetilde{\mathbf{A}}'$ to $\widetilde{\mathbf{k}}[\bar{X}_2, \cdots, \bar{X}_r]$. Let $\widetilde{\mathbf{q}}$ denote the image of $\widetilde{\mathbf{M}}'$ by this natural homomorphism. Then $\widetilde{\mathbf{q}}$ is a prime ideal in $\widetilde{\mathbf{k}}[\bar{X}_2, \cdots, \bar{X}_r]$ with $\widetilde{\mathbf{q}} \cap \mathbf{k}[\bar{X}_2, \cdots, \bar{X}_r] = (0)$. In this manner, the set of those prime ideals $\widetilde{\mathbf{q}}$ with this property is in a one to one correspondence with the set of those $\widetilde{\mathbf{R}}'$ which admit a canonical local homomorphism $\mathbf{R}' \to \widetilde{\mathbf{R}}'$. If $\widetilde{\mathbf{R}}$ is residually separable over $\mathbf{R}$, i.e., $\widetilde{\mathbf{k}}$ is separable over $\mathbf{k}$ in the sense that for every purely inseparable

extension $\mathbf{k}'$ over $\mathbf{k}$ the tensor product $\widetilde{\mathbf{k}}\otimes_{\mathbf{k}}\mathbf{k}'$ has no nilpotent elements, then for every prime ideal $\widetilde{\mathbf{q}}$ in $\widetilde{\mathbf{k}}[\bar{X}_2,\cdots,\bar{X}_r]$ such that $\widetilde{\mathbf{q}}\cap\mathbf{k}[\bar{X}_2,\cdots,\bar{X}_r]=(0)$, the localization of $\widetilde{\mathbf{k}}[\bar{X}_2,\cdots,\bar{X}_r]$ with respect to $\widetilde{\mathbf{q}}$ is regular. It follows that if $\widetilde{\mathbf{R}}$ is residually separable over $\mathbf{R}$, then for every monoidal transform $\widetilde{\mathbf{R}}'$ of $\widetilde{\mathbf{R}}$ with center $\widetilde{\mathbf{P}}$ which admits a canonical homomorphism $\mathbf{R}'\to\widetilde{\mathbf{R}}'$, the image of a regular system of parameters of $\mathbf{R}'$ can be extended to a regular system of parameters of $\widetilde{\mathbf{R}}'$.

We summarize the above results in the following

LEMMA 4. Let $\mathbf{R} \to \widetilde{\mathbf{R}}$ be a local homomorphism of regular local rings such that a regular system of parameters of $\mathbf{R}$ is transformed into such a system of parameters of $\widetilde{\mathbf{R}}$. Let $\mathbf{P}$ be a prime ideal in $\mathbf{R}$ such that $\mathbf{R} / \mathbf{P}$ is regular. Then $\widetilde{\mathbf{P}} = \mathbf{P}\widetilde{\mathbf{R}}$ is a prime ideal and $\widetilde{\mathbf{R}} / \widetilde{\mathbf{P}}$ is regular. Let $\mathbf{R}'$ be a monoidal transform of $\mathbf{R}$ with center $\mathbf{P}$. We consider those monoidal transforms, denoted by $\widetilde{\mathbf{R}}'$, of $\widetilde{\mathbf{R}}$ with center $\widetilde{\mathbf{P}}$ such that we have the following commutative diagram of canonical local homomorphisms:

![](images/page_8_image_3.jpg)

We then have the following facts:

(1) If either $\widetilde{\mathbf{R}}$ or $\mathbf{R}'$ is residually algebraic over $\mathbf{R}$, then there exist only a finite number of $\widetilde{\mathbf{R}'}$, all the $\widetilde{\mathbf{R}'}$ have the same dimension as $\mathbf{R}'$, and if $\widetilde{\mathbf{R}}$ is residually algebraic over $\mathbf{R}$ the number of $\widetilde{\mathbf{R}'}$ does not exceed the separable degree of the residue field of $\widetilde{\mathbf{R}}$ over that of $\mathbf{R}$.

(2) All the local homomorphisms of the above diagram are injective, and the residue field of  $\widetilde{R}'$  is generated by those of  $R'$  and  $\widetilde{R}$  over that of R.

(3) If $\widetilde{\mathbf{R}}$ is residually separable (resp. separable algebraic) over $\mathbf{R}$, then the image of a regular system of parameters of $\mathbf{R}'$ by any of the local homomorphisms $\mathbf{R}' \to \widetilde{\mathbf{R}}'$ can be extended to (resp. the image is) a regular system of parameters of $\widetilde{\mathbf{R}}'$.

COROLLARY 1. Let $\mathbf{R}$ and $\mathbf{P}$ be as in Lemma 4. Let $\hat{\mathbf{R}}$ be the completion of $\mathbf{R}$ and $\hat{\mathbf{P}} = \mathbf{P}\hat{\mathbf{R}}$. Then $\hat{\mathbf{P}}$ is a prime ideal of $\hat{\mathbf{R}}$ such that $\hat{\mathbf{R}}/\hat{\mathbf{P}}$ is regular. For a given monoidal transform $\mathbf{R}'$ of $\mathbf{R}$ with center $\mathbf{P}$, there exists a unique monoidal transform $\hat{\mathbf{R}'}$ of $\hat{\mathbf{R}}$ with center $\hat{\mathbf{P}}$ which admits the following commutative diagram of canonical local homomorphisms:

![](images/page_9_image_0.jpg)

Moreover, the local homomorphism $\mathbf{R}' \to \hat{\mathbf{R}}'$ induces an isomorphism of the residue fields of $\mathbf{R}'$ and $\hat{\mathbf{R}}'$, and it transforms a regular system of parameters of $\mathbf{R}'$ into such a system of parameters of $\hat{\mathbf{R}}'$.

COROLLARY 2. The notation and assumptions being the same as in Corollary 1, the completions of $\mathbf{R}'$ and $\hat{\mathbf{R}}'$ are canonically isomorphic to each other, and $\mathbf{R}$ is a topological subspace of $\mathbf{R}'$.

PROOF.  $R'$  and  $\hat{R}'$  have the same residue field. Hence, the fact that  $R'$  and  $\hat{R}'$  have a common regular system of parameters implies the first statement of Corollary 2. As for the second, it suffices to note that, if T denotes the common completion of  $R'$  and  $\hat{R}'$, then the diagram of Corollary 1 can be extended to the following commutative diagram of canonical local homomorphisms, all injective:

![](images/page_9_image_4.jpg)

q.e.d.

DEFINITION 5. Let R be a regular local ring, P a prime ideal in R such that R/P is regular, and J an ideal in R. We also consider the special case in which R = P. Let R' be a monoidal transform of R with center P. We define the strict transform of J in R' (with respect to the center P) to be the ideal in R' which is generated by those elements of the form  $x^{-\nu}f$  with  $x \in R'$  such that  $(x)R' = PR'$  and with  $f \in J$  such that  $\nu_{\mathrm{P}}(f) \geq \nu$ . We define the weak transform of J in R' (with respect to the center P) to be the ideal in R' which is generated by those elements of the form  $x^{-\nu}f$  with  $x \in R'$  such that  $(x)R = PR'$ , with  $f \in J$  and with  $\nu \leq \nu_{\mathrm{P}}(\mathbf{J})$ . (Here,  $\nu_{\mathrm{P}}(\mathbf{J}) = \infty$  if P = R.)

REMARK 0. In the above definition of the strict (resp. the weak) transform J' of J in the monoidal transform R' of R with center P, the reference to the center P is essential. A simple example shows that we can have one and the same local ring R' (in the field of quotients of R) which is the monoidal transforms of R with two different centers P and Q. Moreover, the transform J' of J in R' with respect to P may not be the same as that of J in R' with respect to Q. However, by an abuse of language, if the center in R with which R' is a monoidal transform of

R is specified in the same context, we shall speak of the strict (resp. the weak) transform of J in  $R'$  (with respect to the same center as for  $R'$ ) without explicitly mentioning the reference to the center.

REMARK 1. Let us take an element $x \in \mathbf{R}'$ such that $(x)\mathbf{R}' = \mathbf{PR}'$. Then the strict transform $\mathbf{J}_s'$ of $\mathbf{J}$ in $\mathbf{R}'$ is the increasing union of the ideals

$$
x ^ {- \nu} (\mathbf {J} \cap \mathbf {P} ^ {\nu}) \mathbf {R} ^ {\prime}
$$

for all non-negative integers $\nu$. Since $\mathbf{R}'$ is noetherian, we have $\mathbf{J}_s' = x^{-\nu}(\mathbf{J} \cap \mathbf{P}^{\nu})\mathbf{R}'$ for all sufficiently large $\nu$. On the other hand, the weak transform $\mathbf{J}_w'$ of $\mathbf{J}$ in $\mathbf{R}'$ is the union of the ideals

$$
x ^ {- \nu} \mathbf {J R} ^ {\prime}
$$

for all non-negative integers $\nu$ such that $\mathbf{P}^{\nu} \supseteq \mathbf{J}$. In particular, if $\mathbf{J} \neq (0)\mathbf{R}$ and $\mathbf{P} \neq \mathbf{R}$, then we have an integer $\nu_{\mathbf{P}}(\mathbf{J}) = \operatorname{Min}_{f \in \mathbf{J}} \{\nu_{\mathbf{P}}(f)\}$ and $\mathbf{J}_{w}' = x^{-\nu} \mathbf{JR}'$ with $\nu = \nu_{\mathbf{P}}(\mathbf{J})$.

REMARK 2. Let X be a non-singular algebraic scheme, B an irreducible non-singular subscheme of X and J a coherent sheaf of ideals on X. Let $f: X' \to X$ be the monoidal transformation of X with center B. The total pre-image $E = f^{-1}(B)$ is a non-singular subscheme of $X'$ of codimension 1. Let $P_E$ denote the sheaf of ideals on $X'$ which define E. Let $f^{-1}(J)$ denote the sheaf of ideals on $X'$ which are generated by the ideals of J. Let x be the generic point of B; we assume that B is not empty. Then for every non-negative integer $\nu \leq \nu(J_x)$, $f^{-1}(J)$ is contained in $P_E^\nu$. Let $J'$ be the sheaf of ideals on $X'$ which is the increasing union of $f^{-1}(J)P_E^{-\nu}$ for all $\nu \leq \nu(J_x)$. Then $J'$ is a coherent sheaf of ideals on $X'$. If $J_x$ is not a zero ideal then $\nu(J_x)$ is a non-negative integer and we have $J' = f^{-1}(J)P_E^{-\nu}$ with $\nu = \nu(J_x)$. If B is empty, we have $X' = X$ with the identity f and we put $J' = J$. We shall call $J'$ the weak transform of J on $X'$ by the monoidal transformation f. Let $y'$ be any point of $X'$, $y = f(y')$, R the local ring of X at y, R' the local ring of $X'$ at $y'$, and P the ideal in R which defines the subscheme B of X. Then we see that R' is a monoidal transform of R with center P and that $J_{y'}'$ is the weak transform of $J_y$ in R'.

REMARK 3. Let X, B and J be as above. Let  $P_{B}$  denote the sheaf of ideals on X which define the subscheme B of X. Then for every non-negative integer  $\nu$ ,  $J(\nu) = J \cap P_{B}^{\nu}$  is a coherent sheaf of ideals on X. Let  $J'(\nu)$  denote the weak transform of  $J(\nu)$  on  $X'$ . Then  $\{J'(\nu)\}$  is an increasing sequence of coherent sheaves of ideals on  $X'$ . Therefore the union  $J''$  of these  $J'(\nu)$  for all non-negative integers  $\nu$  is a coherent sheaf of ideals on  $X'$ . This sheaf of ideals  $J''$  on  $X'$  will be called the strict

transform of J on  $X'$  by the monoidal transformation f. Let  $y'$  be any point of  $X'$,  $y = f(y')$, R the local ring on X at y,  $R'$  the local ring of  $X'$  at  $y'$, and P the ideal in R which defines the subscheme B of X. Then  $J_{y'}'$  is the strict transform of  $J_y$  in  $R'$.

REMARK 4. Let $X, B$ and $f: X' \to X$ be as above. Let $V$ be a subscheme of $X$ which contains $B$. Let $V'$ be the strict transform of $V$ on $X'$ by $f$, that is, the smallest subscheme of $X'$ which induces $f^{-1}(V - B)$ in $X' - f^{-1}(B)$. Let $J$ be the sheaf of ideals of $V$ on $X$. Then we see that the strict transform $J''$ of $J$ on $X'$ by $f$ is equal to the sheaf of ideals of $V'$ on $X'$. (See the paragraphs preceding Def. 6, § 1, Ch. I, and also § 2, Ch. 0.)

LEMMA 5. Let $\mathbf{A} \to \mathbf{A}'$ be a homomorphism of noetherian rings such that $\mathbf{A}'$ is flat over $\mathbf{A}$. Then if $\mathbf{I}$ and $\mathbf{J}$ are ideals in $\mathbf{A}$, we have $(\mathbf{J} \cap \mathbf{I})\mathbf{A}' = \mathbf{J}\mathbf{A}' \cap \mathbf{I}\mathbf{A}'$.

PROOF. $^{2}$  We have the exact sequence

$$
0 \longrightarrow \mathbf {J} \cap \mathbf {I} \longrightarrow \mathbf {A} \stackrel {\alpha} {\longrightarrow} \mathbf {A} / \mathbf {J} \oplus \mathbf {A} / \mathbf {I}
$$

where the homomorphism  $\alpha$  is the direct sum of the natural homomorphisms of A to A/J and to A/I. Since  $A'$  is flat over A, the sequence

$$
0 \longrightarrow (\mathbf {J} \cap \mathbf {I}) \otimes_ {\mathbf {A}} \mathbf {A} ^ {\prime} \longrightarrow \mathbf {A} \otimes_ {\mathbf {A}} \mathbf {A} ^ {\prime} \longrightarrow (\mathbf {A} / \mathbf {J} \oplus \mathbf {A} / \mathbf {I}) \otimes_ {\mathbf {A}} \mathbf {A} ^ {\prime}
$$

that is,

$$
0 \longrightarrow (\mathbf {J} \cap \mathbf {I}) \mathbf {A} ^ {\prime} \longrightarrow \mathbf {A} ^ {\prime} \longrightarrow \mathbf {A} ^ {\prime} / \mathbf {J} \mathbf {A} ^ {\prime} \oplus \mathbf {A} ^ {\prime} / \mathbf {I} \mathbf {A} ^ {\prime}
$$

is exact. This implies that

$$
(\mathbf {J} \cap \mathbf {I}) \mathbf {A} ^ {\prime} = \mathbf {J A} ^ {\prime} \cap \mathbf {I A} ^ {\prime}.
$$

COROLLARY. Let  $R \rightarrow \widetilde{R}$  be a local homomorphism of regular local rings which transforms a regular system of parameters of R into such a system of parameters of  $\widetilde{R}$ . Let P be a prime ideal in R such that R/P is regular, and  $\widetilde{P} = P\widetilde{R}$ . Let J be an ideal in R and  $\widetilde{J} = J\widetilde{R}$ . Let  $R'$  (resp.  $\widetilde{R}'$ ) be a monoidal transform of R (resp.  $\widetilde{R}$ ) with center P (resp.  $\widetilde{P}$ ) such that we have the commutative diagram of canonical local homomorphisms

![](images/page_11_image_12.jpg)

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{2}$  This proof was provided by D. S. Rim.</span></small>

Let $\mathbf{J}'$ (resp. $\widetilde{\mathbf{J}}'$) be the strict transform of $\mathbf{J}$ (resp. $\widetilde{\mathbf{J}}$) in $\mathbf{R}'$ (resp. $\widetilde{\mathbf{R}}'$). Then we have $\widetilde{\mathbf{J}}' = \mathbf{J}'\widetilde{\mathbf{R}}'$.

PROOF. By the assumption on the local homomorphism $\mathbf{R} \to \widetilde{\mathbf{R}}$, we can apply Lemma 5 to $\mathbf{A} = \mathbf{R}$ and $\widetilde{\mathbf{A}} = \widetilde{\mathbf{R}}$ and get

$$
(\mathbf {J} \cap \mathbf {P} ^ {\nu}) \widetilde {\mathbf {R}} = \widetilde {\mathbf {J}} \cap \widetilde {\mathbf {P}} ^ {\nu}
$$

for all non-negative integers $\nu$. On the other hand, if $x$ is an element of $\mathbf{P}$ such that $\mathbf{PR}' = (x)\mathbf{R}'$, then $\widetilde{\mathbf{P}}\widetilde{\mathbf{R}}' = (x)\widetilde{\mathbf{R}}'$. Thus $\widetilde{\mathbf{J}}' = \bigcup_{\nu=0}^{\infty} x^{-\nu} (\widetilde{\mathbf{J}} \cap \widetilde{\mathbf{P}}^{\nu}) \widetilde{\mathbf{R}}' = \bigcup_{\nu=0}^{\infty} x^{-\nu} (\mathbf{J} \cap \mathbf{P}^{\nu}) \widetilde{\mathbf{R}}' = \mathbf{J}'\widetilde{\mathbf{R}}'$. q.e.d.

LEMMA 6. Let R be a regular local ring, J an ideal in R, and P a prime ideal in R such that R/P is regular. Let  $(f_{1}, \cdots, f_{m})$  be a system of elements of J such that their initial forms in  $\mathrm{gr}_{\mathrm{P}}(\mathbf{R})$  generate the ideal  $\mathrm{gr}_{\mathrm{P}}(\mathbf{J}, \mathbf{R})$ . Let  $R'$  be a monoidal transform of R with center P, and x an element of P such that  $\mathbf{PR}' = (x)\mathbf{R}'$ . Let  $\nu_{i} = \nu_{\mathrm{P}}(f_{i})$  for  $1 \leq i \leq m$ . Then the strict transform of J in  $R'$  is generated by the elements  $x^{-\nu_{i}}f_{i}$  for  $1 \leq i \leq m$ .

PROOF. Let us take a minimal base  $(x, x_{1}, \cdots, x_{r})$  of the prime ideal P, where  $r + 1 = \dim R - \dim R/P$ . Let  $A' = R[x_{1}/x, \cdots, x_{r}/x]$ . By the definition of the strict transform of J in  $R'$ , it suffices to prove that

$$
x ^ {- \nu} (\mathbf {J} \cap \mathbf {P} ^ {\nu}) \mathbf {A} ^ {\prime} \subseteq (x ^ {- \nu_ {1}} f _ {1}, \dots , x ^ {- \nu_ {m}} f _ {m}) \mathbf {A} ^ {\prime}
$$

for all sufficiently large integers $\nu$. Let $\mathbf{I}_{\nu} = \sum_{i=1}^{m} \mathbf{P}^{\nu - \nu_i} f_i$ for every $\nu \geq \max \{\nu_i\}$. The above inclusion will follow if we can prove

$$
\mathbf {J} \cap \mathbf {P} ^ {\nu} \subseteq \mathbf {I} _ {\nu}
$$

for all positive integers $\nu \geq \max \{\nu_i\}$. We shall first prove that

$$
\mathbf {J} \cap \mathbf {P} ^ {\nu} \subseteq \mathbf {I} _ {\nu} + \mathbf {P} ^ {\nu + 1}.
$$

Let $f$ be any element of $\mathbf{J} \cap \mathbf{P}^{\nu}$ which is not in $\mathbf{P}^{\nu+1}$. Let $\varphi$ be the initial form of $f$ in $\mathrm{gr}_{\mathbf{P}}(\mathbf{R})$. Then $\varphi$ is in $\mathrm{gr}_{\mathbf{P}}(\mathbf{J}, \mathbf{R})$. If $\varphi_{i} =$ the initial form of $f_{i}$ in $\mathrm{gr}_{\mathbf{P}}(\mathbf{R})$ for $1 \leq i \leq m$, then $\mathrm{gr}_{\mathbf{P}}(\mathbf{J}, \mathbf{R}) = (\varphi_{1}, \cdots, \varphi_{m}) \mathrm{gr}_{\mathbf{P}}(\mathbf{R})$. Therefore we have

$$
\varphi = \sum_ {i} \psi_ {i} \mathcal {P} _ {i}
$$

with forms $\psi_i \in \mathrm{gr}_{\mathbf{P}}^{\nu - \nu_i}(\mathbf{R})$ for those $i$ with $\nu - \nu_i \geq 0$. Let $h_i$ be an element of $\mathbf{R}$ such that $\psi_i$ is the initial form of $h_i$ in $\mathrm{gr}_{\mathbf{P}}(\mathbf{R})$. Then $h_i \in \mathbf{P}^{\nu - \nu_i}$ and $f - \sum_{i} h_i f_i \in \mathbf{P}^{\nu + 1}$. Thus $f \in \mathbf{I}_\nu + \mathbf{P}^{\nu + 1}$. Now we have $\mathbf{J} \cap \mathbf{P}^\nu \subseteq \mathbf{I}_\nu + \mathbf{P}^{\nu + 1}$ for all $\nu \geq \max \{\nu_i\}$. Since $\mathbf{I}_{\nu + n} = \mathbf{P}^n \mathbf{I}_\nu \subseteq \mathbf{I}_\nu \subseteq \mathbf{J}$ for all $\nu \geq \max \{\nu_i\}$ and all positive integers $n$, this result implies immediately

$$
\mathbf {J} \cap \mathbf {P} ^ {\nu} \subseteq \mathbf {I} _ {\nu} + \mathbf {P} ^ {\nu + n}
$$

for all $\nu \geq \max \{\nu_i\}$ and all $n \geq 0$. Hence

$$
\mathbf {J} \cap \mathbf {P} ^ {\nu} \subseteq \mathbf {I} _ {\nu}
$$

which completes the proof. q.e.d.

## 3. The upper semi-continuity of  $\nu(\mathbf{J})$  of local ideals J

Let $\mathbf{R}$ be a regular local ring, $\mathbf{M}$ the maximal ideal of $\mathbf{R}$, $\mathbf{P}$ a prime ideal in $\mathbf{R}$, and $\mathbf{J}$ a non-zero ideal in $\mathbf{R}$. Then $\nu_{\mathrm{P}}(\mathbf{J})$ is the maximal integer $\nu (\geq 0)$ such that $\mathbf{P}^{\nu}$ contains $\mathbf{J}$. We write $\nu (\mathbf{J})$ for $\nu_{\mathrm{M}}(\mathbf{J})$. It is clear that $\nu_{\mathrm{P}}(\mathbf{J}) \leq \nu (\mathbf{J})$ and $\nu_{\mathrm{P}}(\mathbf{J}) \leq \nu (\mathbf{JR}_{\mathrm{P}})$. If $\mathbf{R} / \mathbf{P}$ is regular, then we have $\mathbf{P}^{\nu} = \mathbf{P}^{\nu}\mathbf{R}_{\mathrm{P}} \cap \mathbf{R}$ for all non-negative integer $\nu$. Therefore we have $\nu_{\mathrm{P}}(\mathbf{J}) = \nu (\mathbf{JR}_{\mathrm{P}})$. Thus:

LEMMA 7. Let R, J and P be as above. If R/P is regular, then we have

$$
\nu (\mathbf {J} \mathbf {R} _ {\mathrm{P}}) \leq \nu (\mathbf {J}).
$$

LEMMA 8. Let R be a regular local ring, J a non-zero ideal in R, and P a prime ideal in R. Assume that R/P is regular and that  $\nu_{\mathrm{P}}(\mathbf{J}) = \nu(\mathbf{J})$ . Let  $R'$  be a monoidal transform of R with center P which is residually algebraic over R. If  $J'$  is the weak transform of J in  $R'$  then we have

$$
\nu (\mathbf {J} ^ {\prime}) \leq \nu (\mathbf {J}).
$$

PROOF. Let M (resp. M') denote the maximal ideal of R (resp. R'). Let us take an element f of J such that  $\nu_{\mathbf{M}}(f)=\nu(\mathbf{J})$ . Then we have  $\nu_{\mathbf{M}}(f)=\nu_{\mathbf{P}}(f)$ . Let us choose  $x\in P$  such that  $\mathbf{PR}^{\prime}=(x)\mathbf{R}^{\prime}$ . Then  $x^{-\nu}f\in J^{\prime}$  where  $\nu=\nu_{\mathbf{P}}(f)=\nu_{\mathbf{M}}(f)$ . Therefore it suffices to show that  $\nu_{\mathbf{M}^{\prime}}(x^{-\nu}f)\leq\nu$ . We have a minimal base of P including the element x, say  $(x,z_{1},\cdots,z_{r})$  where  $r+1=\dim R_{P}$ . We can write the element f in the form  $\sum a_{(i)}x^{i_{0}}z_{1}^{i_{1}}z_{2}^{i_{2}}\cdots z_{r}^{i_{r}}$  where the summation is for all distinct systems  $(i_{0},i_{1},\cdots,i_{r})$  such that  $i_{0}+i_{1}+\cdots+i_{r}=\nu$ , and  $a_{(i)}\in R$ . Then some of the  $a_{(i)}$  must be units in R because  $\nu_{\mathbf{M}}(f)=\nu$ . Then  $x^{-\nu}f$  can be written in the form

$$
\sum a _ {(i)} (z _ {1} / x) ^ {i _ {1}} (z _ {2} / x) ^ {i _ {2}} \dots (z _ {r} / x) ^ {i _ {r}}.
$$

Let  $A' = R[z_{1}/x, \cdots, z_{r}/x]$  and N the maximal ideal in  $A'$  such that  $R' = A_{N}'$ . Then N contains  $MA'$ . We have seen in §2 that  $A'/MA'$  is isomorphic to a polynomial ring  $k[Z_{1}, \cdots, Z_{r}]$  of r-variables corresponding to the  $z_{i}/x (1 \leq i \leq r)$  over the field k = R/M. Let F be the class of  $x^{-\nu}f$  in  $k[Z_{1}, \cdots, Z_{r}]$ , which is of the form

$$
\sum \bar {a} _ {(i)} Z _ {1} ^ {i _ {1}} Z _ {2} ^ {i _ {2}} \dots Z _ {r} ^ {i _ {r}},
$$

where  $\bar{a}_{(i)}$  is the residue class of  $a_{(i)}$  in k. Let  $\bar{N}=N/MA'$ , which is a maximal ideal in  $k[Z_{1},\cdots,Z_{r}]$ . If  $\nu'=\nu_{M'}(x^{-\nu}f)$ , then  $x^{-\nu}f\in N^{\nu'}$  and

hence $F \in \overline{\mathbf{N}}^{\nu'}$. Since some of the $a_{(i)}$ are units in $\mathbf{R}$, hence, in $\mathbf{R}'$, some of the $\overline{a}_{(i)}$ are not zero. In view of the above expression of $F$, we see that $F$ is a non-zero polynomial in the $Z_j$'s of degree at most $\nu$. Hence $F$ is not contained in the $(\nu + 1)^{\text{th}}$ power of any maximal ideal in $\mathbf{k}[Z_1, \cdots, Z_r]$. (This is easily shown if $\mathbf{k}$ is algebraically closed, and the assertion for an arbitrary $\mathbf{k}$ follows immediately.) Thus we have $\nu_{\mathbf{M}'}(x^{-\nu}f) = \nu' \leq \nu$. q.e.d.

THEOREM 1 (Zariski-Nagata). $^{3}$  Let R be a regular local ring and J a non-zero ideal in R. Let P be any prime ideal in R. Then we have  $\nu(\mathbf{J}) \geq \nu(\mathbf{JR}_{\mathbf{P}})$ .

PROOF. We have a chain of prime ideals  $P = P_{0} \subset P_{1} \subset \cdots \subset P_{s} = M$  where M is the maximal ideal of R and  $\dim (\mathbf{R}_{\mathbf{P}_{i}} / \mathbf{P}_{i-1} \mathbf{R}_{\mathbf{P}_{i}})$  for  $i = 1, 2, \cdots, s$  are all equal to one. Therefore it suffices to prove the inequality for the case in which  $\dim (\mathbf{R} / \mathbf{P}) = 1$ . On the other hand, let  $\hat{R}$  be the completion of R,  $\hat{P}$  any minimal prime ideal associated with  $P\hat{R}$ , and  $\hat{J} = J\hat{R}$ . Then we have a canonical local homomorphism  $R_{P} \to \hat{R}_{\hat{P}}$ . Hence  $\nu(\hat{J}\hat{R}_{\hat{P}}) = \nu(J\hat{R}_{\hat{P}}) \geq \nu(JR_{P})$ , while  $\nu(\hat{J}) = \nu(J)$  as is easily seen. Therefore, it suffices to show  $\nu(\hat{J}) \geq \nu(\hat{J}\hat{R}_{\hat{P}})$ . In other words, we may assume that R is complete. Thus we shall assume that R is complete and  $\dim (\mathbf{R} / \mathbf{P}) = 1$ . Let S = R/P. Then we know that the derived normal ring of S in its field of quotients is an S-module of finite type and that every localization of the derived normal ring is regular. In view of these facts, it is not difficult to show that there exists a finite sequence of successive monoidal transforms with center the maximal ideals,  $R = R_{0} \to R_{1} \to \cdots \to R_{s}$ , such that:

(i)  $R_{i}$  is residually algebraic over  $R_{i-1}$  for  $i = 1, 2, \cdots, s$ ,

(ii) for each $i \geq 1$, there exists a prime ideal $\mathbf{P}_i$ in $\mathbf{R}_i$ such that $\mathbf{R}_{\mathbf{P}} = (\mathbf{R}_i)_{\mathbf{P}_i}$, and

(iii) $\mathbf{R}_s / \mathbf{P}_s$ is regular.

Let $\mathbf{J}_i$ be the ideals in $\mathbf{R}_i$ ($0 \leq i \leq s$) such that $\mathbf{J} = \mathbf{J}_0$, and that $\mathbf{J}_i$ is the weak transform of $\mathbf{J}_{i-1}$ in $\mathbf{R}_i$ ($1 \leq i \leq s$). Then by Lemma 8, we have $\nu(\mathbf{J}) \geq \nu(\mathbf{J}_1) \geq \cdots \geq \nu(\mathbf{J}_s)$; and, by Lemma 7, we have $\nu(\mathbf{J}_s) \geq \nu(\mathbf{J}_s(\mathbf{R}_s)_{\mathbf{P}_s}) = \nu(\mathbf{JR}_\mathbf{p})$. Hence $\nu(\mathbf{J}) \geq \nu(\mathbf{JR}_\mathbf{p})$. q.e.d.

LEMMA 9. Let R be a regular local ring, J an ideal in R, and P a prime ideal in R such that  $P \supset J$  and R/P is regular. Let O = R/J and P = P/J. Assume that  $\mathrm{gr}_{P}(\mathbf{O})$  is flat over O/P. If  $(f_{1}, \cdots, f_{m})$  is a system of elements of J such that

(i)  $(f_{1}, \cdots, f_{m})$  is a standard base of  $JR_{P}$ , and

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{3}$  This theorem and the proof are O. Zariski's. It was pointed out by A. Grothendieck that the theorem has also been given a proof by M. Nagata.</span></small>

(ii) the initial forms $\Phi_j$ of $f_j$ in $\mathbf{gr}_{\mathbf{P}}(\mathbf{R})$ ($1 \leq j \leq m$) generate the ideal $\mathbf{gr}_{\mathbf{P}}(\mathbf{J}, \mathbf{R})$,

then  $(f_{1}, f_{2}, \cdots, f_{m})$  is a standard base of J, and if M = the maximal ideal of R, we have  $\nu_{\mathbf{M}}(f_{j}) = \nu_{\mathbf{P}}(f_{j})$  for  $1 \leq j \leq m$ .

PROOF. Let $\mathbf{R}' = \mathbf{R} / \mathbf{P} = \mathbf{O} / P$ and $\mathbf{M}' = \mathbf{M} / \mathbf{P}$. Since $\mathrm{gr}_P(\mathbf{O})$ is flat over $\mathbf{O} / P$, $\mathrm{gr}_{\mathbf{M}}(\mathbf{J}, \mathbf{R})$ is generated by the initial forms of those $g \in \mathbf{J}$ which have the property that $\nu_{\mathbf{P}}(g) = \nu_{\mathbf{M}}(g)$. (See Cor. 1 to Th. 2, § 2, Ch. II.) Take any $g \in \mathbf{J}$ with this property. Let $\Psi$ be the initial form of $g$ in $\mathrm{gr}_{\mathbf{P}}(\mathbf{R})$. Let $\nu = \deg \Psi = \nu_{\mathbf{P}}(g) = \nu_{\mathbf{M}}(g)$. Then by (ii), if $\nu_j = \deg \Phi_j$ ($1 \leq j \leq m$), we have $\Lambda_j \in \mathrm{gr}_{\mathbf{P}}^{\nu - \nu_j}(\mathbf{R})$ such that $\Psi = \sum_j \Lambda_j \Phi_j$. Let us take $h_j \in \mathbf{P}^{\nu - \nu_j}$ such that $\Lambda_j =$ the initial form of $h_j$ in $\mathrm{gr}_{\mathbf{P}}(\mathbf{R})$. Then we have $g - \sum_j h_j f_j \in \mathbf{P}^{\nu + 1}$, hence, $\in \mathbf{M}^{\nu + 1}$. Therefore the initial form of $g$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ is equal to that of $\sum_j h_j f_j$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$, which can be written as $\sum_j \lambda_j \varphi_j$ where $\lambda_j =$ the class of $h_j$ in $\mathrm{gr}_{\mathbf{M}}^{\nu - \nu_j}(\mathbf{R})$, and $\varphi_j =$ the class of $f_j$ in $\mathrm{gr}_{\mathbf{M}}^{\nu_j}(\mathbf{R})$. Thus we have seen that if $\varphi_j =$ the class of $f_j$ in $\mathrm{gr}_{\mathbf{M}}^{\nu_j}(\mathbf{R})$ ($1 \leq j \leq m$) then

$$
\mathrm{(a)} \operatorname{gr} _ {\mathbf {M}} (\mathbf {J}, \mathbf {R}) = \left(\varphi_ {1}, \dots , \varphi_ {m}\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}).
$$

We note that $\varphi_{j} \neq 0$ if and only if $\nu_{\mathbf{M}}(f_{j}) = \nu_{j} = \nu_{\mathbf{P}}(f_{j})$. Now we claim that:

$$
\varphi_ {i} \notin (\varphi_ {1}, \dots , \varphi_ {i - 1}) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}) \quad \text { for } 1 \leq i \leq m.
$$

Suppose we have  $i \geq 1$  such that  $\varphi_{i} \in (\varphi_{1}, \cdots, \varphi_{i-1}) \operatorname{gr}_{\mathbf{M}}(\mathbf{R})$ . Let i be the smallest one which has this property, so that we have  $\nu_{\mathbf{M}}(f_{j}) = \nu_{\mathbf{P}}(f_{j})$  for  $1 \leq j \leq i - 1$ . In view of this, we must have  $h_{j} \in P^{\nu_{i}-\nu_{j}} (1 \leq j \leq i - 1)$  such that  $f_{i} - \sum_{j=1}^{i-1} f_{j} h_{j} \in M^{\nu_{i+1}}$ . This means that, if  $\Lambda_{j}$  is the image of  $h_{j}$  in  $\operatorname{gr}_{\mathbf{P}}^{\nu_{i}-\nu_{j}}(\mathbf{R}) (1 \leq j \leq i - 1)$ , then  $\Phi_{i} - \sum_{j=1}^{i-1} \Lambda_{j} \Phi_{j} \in M' \operatorname{gr}_{\mathbf{P}}(\mathbf{R})$ . Since we have  $\mathbf{M}' \operatorname{gr}_{\mathbf{P}}(\mathbf{R}) \cap \operatorname{gr}_{\mathbf{P}}(\mathbf{J}, \mathbf{R}) = \mathbf{M}' \operatorname{gr}_{\mathbf{P}}(\mathbf{J}, \mathbf{R})$  by the flatness of  $\operatorname{gr}_{P}(\mathbf{O})$  over O/P, we get

$$
\Phi_ {i} - \sum_ {j = 1} ^ {i - 1} \Lambda_ {j} \Phi_ {j} \in \mathbf {M} ^ {\prime} \mathrm{gr} _ {\mathbf {P}} (\mathbf {J}, \mathbf {R}).
$$

(See, for instance, Lemma 7, § 2, Ch. II.) Hence, if I denotes the ideal  $(\Phi_{1}, \cdots, \Phi_{i-1}, \Phi_{i+1}, \cdots, \Phi_{m}) \operatorname{gr}_{\mathbf{P}}(\mathbf{R})$ , then  $\operatorname{gr}_{\mathbf{P}}(\mathbf{J}, \mathbf{R}) = \mathbf{I} + \mathbf{M}' \operatorname{gr}_{\mathbf{P}}(\mathbf{J}, \mathbf{R})$ . It follows immediately that

$$
\operatorname{gr} _ {\mathrm{P}} (\mathbf {J}, \mathbf {R}) = \mathbf {I} + (\mathbf {M} ^ {\prime}) ^ {n} \operatorname{gr} _ {\mathrm{P}} (\mathbf {J}, \mathbf {R})
$$

for all positive integer n. Since each homogeneous part of  $\mathrm{gr}_{\mathbf{P}}(\mathbf{J},\mathbf{R})$  is an  $R'$ -module of finite type, Nakayama's lemma gives us

$$
\operatorname{gr} _ {\mathbf {P}} (\mathbf {J}, \mathbf {R}) = \mathbf {I}.
$$

However, this contradicts the assumption (i). Thus (b) is established.

In particular,  $\nu_{\mathbf{M}}(f_{j}) = \nu_{\mathbf{P}}(f_{j})$  for all  $j (1 \leq j \leq m)$ , and therefore  $\varphi_{j}$  is the initial form of  $f_{j}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ . It is clear that  $\deg \varphi_{j} \leq \deg \varphi_{j+1}$  for all  $j (1 \leq j \leq m-1)$ . By (a) and (b),  $(f_{1}, \cdots, f_{m})$  is a standard base of J. q.e.d.

THEOREM 2. Let A be a noetherian regular ring, J an ideal in A, and Q a prime ideal in A which contains J. Suppose A/Q is also a regular ring. Then there exists a non-empty open subset U of  $\text{Spec}(A/Q)$  such that we have

$$
\nu^ {*} (\mathbf {J A} _ {\mathrm{P}}) = \nu^ {*} (\mathbf {J A} _ {\mathrm{Q}}),
$$

for every prime ideal $\mathbf{P}$ in $\mathbf{A}$ such that $\mathbf{P} \supseteq \mathbf{Q}$ and $\mathbf{P} / \mathbf{Q} \in U$.

PROOF. Let us take a system of elements  $f_{1}, \cdots, f_{m}$  of A such that  $(f_{1}, \cdots, f_{m})$  (or, the system of the canonical images of the  $f_{j}$  in  $A_{Q}$ ) is a standard base of  $JA_{Q}$. Let  $\Phi_{j}$  be the initial form of  $f_{j}$  in  $\mathrm{gr}_{\mathbf{Q}}(\mathbf{A})$. We have  $\mathrm{gr}_{\mathbf{Q}}(\mathbf{J}, \mathbf{A})_{\mathbf{Q}} = \mathrm{gr}_{\mathbf{QA}_{\mathbf{Q}}}(\mathbf{JA}_{\mathbf{Q}}, \mathbf{A}_{\mathbf{Q}}) = (\Phi_{1}, \cdots, \Phi_{m}) \mathrm{gr}_{\mathbf{Q}}(\mathbf{A})_{\mathbf{Q}}$. Since  $\mathrm{gr}_{\mathbf{Q}}(\mathbf{A})$  is an A/Q-algebra of finite type and hence noetherian, the ideal  $\mathrm{gr}_{\mathbf{Q}}(\mathbf{J}, \mathbf{A})$  in  $\mathrm{gr}_{\mathbf{Q}}(\mathbf{A})$  has a finite system of generators. Therefore, we can find an element  $f \in A - Q$  such that  $\mathrm{gr}_{\mathbf{Q}}(\mathbf{J}, \mathbf{A})_{f} (= \text{the localization of } \mathrm{gr}_{\mathbf{Q}}(\mathbf{J}, \mathbf{A}) \text{ with respect to the multiplicatively closed set of the powers of } f)$  is equal to  $(\Phi_{1}, \cdots, \Phi_{m}) \mathrm{gr}_{\mathbf{Q}}(\mathbf{A})_{f}$. By replacing A by  $A[f^{-1}]$  and J by  $JA[f^{-1}]$, we may assume that  $\mathrm{gr}_{\mathbf{Q}}(\mathbf{J}, \mathbf{A}) = (\Phi_{1}, \cdots, \Phi_{m}) \mathrm{gr}_{\mathbf{Q}}(\mathbf{A})$. Let  $A' = A/J$  and  $Q' = Q/J$. Then  $\mathrm{gr}_{\mathbf{Q}'}(\mathbf{A}')$  is a graded  $A'/Q' (= A/Q)$-algebra of finite type and, by Theorem 1, §1, Ch. II, we have an open subset U of  $\operatorname{Spec}(\mathbf{A}/\mathbf{Q})$  such that, if P is a prime ideal in A containing Q, we have:  $P/Q \in U \Leftrightarrow gr_{Q'}(\mathbf{A}')_{P}$  is flat over  $A'_P/Q'A'_P = A_P/QA_P$. If P = Q, then  $A_P/QA_P$  is a field, and hence it is clear that  $\mathrm{gr}_{\mathbf{Q}}(\mathbf{A}')_{P}$  is flat over  $A_P/QA_P$; i.e.,  $P/Q \in U$. Thus U is a non-empty open subset of  $\operatorname{Spec}(\mathbf{A}/\mathbf{Q})$. By applying Lemma 9 to  $R = A_P$, JR, QR, and  $(f_1, \cdots, f_m)$, we see immediately that this non-empty open subset U of  $\operatorname{Spec}(\mathbf{A}/\mathbf{Q})$  has the property stated in Theorem 2. q.e.d.

COROLLARY 1. Let X be a non-singular algebraic scheme and J a coherent sheaf of ideals of X. Then, for every non-negative integer ν, there exists an open subset  $U_{\nu}$  of X such that a point x of X belongs to  $U_{\nu}$  if and only if  $\nu(J_{x}) \leq \nu$ .

COROLLARY 2. Let X and J be as above. Then, given a sequence  $\nu^{*}$  of non-negative integers, or  $\infty$ , the set of those points  $x \in X$  with  $\nu^{*}(J_{x}) = \nu^{*}$  is a constructible set, i.e., it is a finite union of locally closed subsets of X.

REMARK. It is not true in general that, if  $x' \in X$  is a specialization of

$x \in X$, then $\nu^{*}(J_{x'}) \geq \nu^{*}(J_{x})$. For example, let $X = \text{Spec}(\mathbf{k}[z_1, z_2, x, y])$ where $(z_1, z_2, x, y)$ is a system of four independent variables over any field $\mathbf{k}$, and let $J$ be the sheaf of ideals on $X$ which is generated by $f_1 = z_1z_2 + (z_1 + y)^2x$, $f_2 = z_1(z_1 + z_2) + (z_2 + y)^2x$ and $f_3 = (z_1 + y)^2(z_1 + z_2) - (z_2 + y)^2z_2$. Let $x$ (resp. $x'$) be the point of $X$ which corresponds to the prime ideal $(z_1, z_2, y)\mathbf{k}[z_1, z_2, x, y]$ (resp. to $(z_1, z_2, y, x)\mathbf{k}[z_1, z_2, y, x]$). Then $x'$ is a specialization of $x$ on $X$, and $\nu^{*}(J_x) = (2, 2, \infty, \infty, \cdots)$ while $\nu^{*}(J_{x'}) = (2, 2, 3, \infty, \infty, \cdots)$, so that $\nu^{*}(J_x) > \nu^{*}(J_{x'})$.

## 4. The numerical characters $\tau^{*}(\mathbf{J})$ of a local ideal J, and a regular system of $\tau$-parameters for J.

Let R be a regular local ring, M the maximal ideal of R, and J an ideal in R. Let  $(\mu_{1}, \cdots, \mu_{t})$  be the system of distinct integers which appear in the sequence  $\nu^{*}(\mathbf{J})$ , and which are arranged in the increasing order:  $\mu_{1} < \mu_{2} < \cdots < \mu_{t}$ . The system of integers  $(\mu_{1}, \cdots, \mu_{t})$  is uniquely determined by the ideal J and is non-empty unless J = (0).

DEFINITION 6. The number t of distinct integers which appear in the sequence  $\nu^{*}(\mathbf{J})$  will be denoted by  $t(\mathbf{J})$ . The integer  $\mu_{a}(1\leq a\leq t)$  will be denoted by  $\mu^{(a)}(\mathbf{J})$ , and the system  $(\mu_{1},\cdots,\mu_{t})$  by  $\mu^{*}(\mathbf{J})$ . For every positive integer  $a\leq t$ , we define  $\tau^{(a)}(\mathbf{J})$  to be the smallest integer  $\tau_{a}(\geq0)$  such that: There exists a system of  $\tau_{a}$  linear forms  $W_{1},\cdots,W_{\tau_{a}}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  which has the property that

$$
\operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {J}, \mathbf {R}) = \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {R}) \cap \left(\operatorname{gr} _ {\mathbf {M}} (\mathbf {J}, \mathbf {R}) \cap \mathbf {K} [ W _ {1}, \dots , W _ {\tau_ {a}} ]\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R})
$$

for all non-negative integers  $\mu\leq\mu_{a}=\mu^{(a)}(\mathbf{J})$ , where K=R/M and  $\mathbf{K}[W_{1},\cdots,W_{\tau_{a}}]$  denotes the K-subalgebra of  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  generated by  $W_{1},\cdots,W_{\tau_{a}}$ . (We have  $\tau_{a}>0$  for all a unless J=R. If J=R, then  $\mu^{*}(\mathbf{J})=(\mu_{1})$  with  $\mu_{1}=0$ , and  $\tau_{1}=0$ . The empty system generates the K-subalgebra K of  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ .) We denote by  $\tau^{*}(\mathbf{J})$  the system  $(\tau^{(1)}(\mathbf{J}),\cdots,\tau^{(t)}(\mathbf{J}))$ .

LEMMA 10. Let G be a polynomial ring over a field K, graded in a natural way. Let  $G_{\mu}$  denote the homogeneous part of degree  $\mu \geq 0$ . Let  $\overline{\mu}$  be a positive integer. Let I be a homogeneous ideal in G and  $I_{\mu}$  the homogeneous part of degree  $\mu \geq 0$  of I. Let T and  $T'$  be two K-submodules of  $G_{1}$  which have the property that

$$
\mathbf {I} _ {\mu} = \mathbf {G} _ {\mu} \cap (\mathbf {I} \cap \mathbf {K} [ \mathbf {T} ]) \mathbf {G} = \mathbf {G} _ {\mu} \cap (\mathbf {I} \cap \mathbf {K} [ \mathbf {T} ^ {\prime} ]) \mathbf {G}
$$

for all $\mu \leq \bar{\mu}$, where $\mathbf{K}[\mathbf{T}]$ (resp. $\mathbf{K}[\mathbf{T}']$) denotes the $\mathbf{K}$-subalgebra of $\mathbf{G}$ generated by the elements of $\mathbf{T}$ (resp. $\mathbf{T}'$). Then we have

$$
\mathbf {I} _ {\mu} = \mathbf {G} _ {\mu} \cap (\mathbf {I} \cap \mathbf {K} [ \mathbf {T} \cap \mathbf {T} ^ {\prime} ]) \mathbf {G}
$$

for all $\mu \leq \overline{\mu}$.

PROOF. We may assume that T and T' generate the whole K-module  $G_{1}$ . (If otherwise, enlarge  $T'$  in such a way that  $T \cap T'$  remains the same, and  $T + T' = G_{1}$ .) Let  $T''$  be the K-submodule of  $T'$  such that  $G_{1}$  is a direct sum of T and  $T''$ . Let  $\rho$  be the natural homomorphism  $\mathbf{G} \to \mathbf{G}/(\mathbf{T}'')\mathbf{G}$  where  $(\mathbf{T}'')\mathbf{G}$  is the ideal in G generated by the elements of  $T''$ . Then  $\rho$  induces an isomorphism of graded K-algebras  $\mathbf{K}[\mathbf{T}] \to \mathbf{G}/(\mathbf{T}'')\mathbf{G}$ . Therefore, we may view  $\rho$  as an endomorphism of G which maps G onto K[T] in a natural way. Now, we have

$$
\mathbf {I} _ {\mu} = \mathbf {G} _ {\mu} \cap (\mathbf {I} \cap \mathbf {K} [ \mathbf {T} ]) \mathbf {G}
$$

for all $\mu \leq \bar{\mu}$ and therefore

$$
\rho (\mathbf {I}) _ {\mu} = \left(\mathbf {I} \cap \mathbf {K} [ \mathbf {T} ]\right) _ {\mu} \subseteq \mathbf {I} _ {\mu}
$$

for all $\mu \leq \bar{\mu}$. (The suffix $\mu$ indicates the homogeneous part of degree $\mu$.) On the other hand, we have

$$
\mathbf {I} _ {\mu} = \mathbf {G} _ {\mu} \cap (\mathbf {I} \cap \mathbf {K} [ \mathbf {T} ^ {\prime} ]) \mathbf {G}
$$

for all $\mu \leq \bar{\mu}$ and therefore, in view of $\rho(\mathbf{I}_{\nu}) \subseteq \mathbf{I}_{\nu}$ for all $\nu \leq \bar{\mu}$, we get

$$
\rho (\mathbf {I}) _ {\mu} \subseteq \left\{\left(\mathbf {I} \cap \mathbf {K} [ \mathbf {T} \cap \mathbf {T} ^ {\prime} ]\right) \mathbf {K} [ \mathbf {T} ] \right\} _ {\mu}
$$

for all $\mu \leq \bar{\mu}$. Thus we get

$$
\left(\mathbf {I} \cap \mathbf {K} [ \mathbf {T} ]\right) _ {\mu} \subseteq \left\{\left(\mathbf {I} \cap \mathbf {K} [ \mathbf {T} \cap \mathbf {T} ^ {\prime} ]\right) \mathbf {K} [ \mathbf {T} ] \right\} _ {\mu}
$$

for all  $\mu \leq \bar{\mu}$ . Here the reversed inclusion is obvious. Hence

$$
\{(\mathbf {I} \cap \mathbf {K} [ \mathbf {T} \cap \mathbf {T} ^ {\prime} ]) \mathbf {G} \} _ {\mu} = \{(\mathbf {I} \cap \mathbf {K} [ \mathbf {T} ]) \mathbf {G} \} _ {\mu} = \mathbf {I} _ {\mu}
$$

for all $\mu \leq \overline{\mu}$. q.e.d.

COROLLARY. The notation and assumptions being the same as in Definition 6, the K-submodule  $\mathbf{T}_{a}$  of  $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$  generated by  $W_{1}, \cdots, W_{\tau_{a}}$  is uniquely determined by the given ideal J in R and  $T_{a}$  is the smallest K-submodule of  $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$  such that

$$
\operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {J}, \mathbf {R}) = \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {R}) \cap \left(\operatorname{gr} _ {\mathbf {M}} (\mathbf {J}, \mathbf {R}) \cap \mathbf {K} [ \mathbf {T} _ {a} ]\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R})
$$

for all $\mu \leq \mu^{(a)}(\mathbf{J})$. In particular, $\mathbf{T}_a \supseteq \mathbf{T}_{a-1}$ and $\tau^{(a)}(\mathbf{J}) \geq \tau^{(a-1)}(\mathbf{J})$ for all $a > 1$.

DEFINITION 7. Let R, M, J,  $\mu^{*}(\mathbf{J})$ , and  $\tau^{*}(\mathbf{J})$  be the same as in Definition 6. Let  $\tau_{a}=\tau^{(a)}(\mathbf{J})$  for  $1\leqq a\leqq t=t(\mathbf{J})$ . Then a system of elements  $(z_{1},\cdots,z_{\tau_{a}})$  of M will be called a regular system of  $a^{th}\tau$ -parameters of R for J if we have, for every positive integer  $b\leqq a$ ,

$$
\operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {J}, \mathbf {R}) = \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {R}) \cap \left(\operatorname{gr} _ {\mathbf {M}} (\mathbf {J}, \mathbf {R}) \cap \mathbf {K} [ \mathbf {T} _ {b} ]\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R})
$$

for all  $\mu\leq\mu^{(b)}(\mathbf{J})$ , where  $T_{b}$  is the K-submodule of  $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$  generated by the classes of  $z_{1},\cdots,z_{\tau_{b}}$  in  $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$  with  $\tau_{b}=\tau^{(b)}(\mathbf{J})$ . If  $t=t(\mathbf{J})$ , a regular system of  $t^{th}\tau$ -parameters of R for J will be simply called a regular system of  $\tau$ -parameters of R for J. Note that any regular system of  $a^{th}\tau$ -parameters of R for J ( $1\leqq a\leqq t$ ) can be extended to a regular system of parameters of R.

LEMMA 11. Let R, M, and J be as above. Let P be a prime ideal in R such that  $P \supseteq J$  and R/P is regular. Suppose we have a system of elements  $(f_{1}, \cdots, f_{m})$  of J such that

(i) $\nu_{\mathbf{M}}(f_j) = \nu_{\mathbf{P}}(f_j)$ for $1 \leq j \leq m$, and

(ii) the initial forms of the  $f_{j}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  generate the ideal  $\mathrm{gr}_{\mathbf{M}}(\mathbf{J},\mathbf{R})$ . Then we have a regular system of  $\tau$ -parameters  $(z_{1},\cdots,z_{\tau})$  of R for J, where  $\tau=\tau^{(t)}(\mathbf{J})$  with  $t=t(\mathbf{J})$ , such that  $z_{j}\in P$  for  $1\leq j\leq\tau$ .

PROOF. Let  $(z_{1},\cdots,z_{r})$  be a minimal base of P, where  $r=\dim R-\dim R/P$ . Let T be the K-submodule of  $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$  generated by the initial forms of  $z_{1},\cdots,z_{r}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ , which are all forms in  $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$ . By (i), it is clear that the initial form of  $f_{j}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  belongs to the K-subalgebra K[T] of  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  for all  $j(1\leq j\leq m)$ . Hence by (ii), we have

$$
\operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {J}, \mathbf {R}) = \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {R}) \cap \left(\operatorname{gr} _ {\mathbf {M}} (\mathbf {J}, \mathbf {R}) \cap \mathbf {K} [ \mathbf {T} ]\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R})
$$

for all  $\mu$ . Hence the K-modules  $T_{i}$  ( $1 \leq i \leq t$ ) defined in Lemma 10, are all contained in T. Since every non-zero element of T is the initial form of an element of P, the assertion of the lemma is clear. q.e.d.

An extension of fields,  $k'$  over k, is separable if and only if every k-subfield of finite type of  $k'$  is separably algebraic over a purely transcendental extension of k in  $k'$ .⁴

LEMMA 12. Let $\mathbf{k}[X] = \mathbf{k}[X_1, \cdots, X_n]$ be a polynomial ring of $n$ indeterminates over a field $\mathbf{k}$. Let $\mathbf{I}$ be a homogeneous ideal in $\mathbf{k}[X]$. Let $\mathbf{k}'$ be a field extension of $\mathbf{k}$ which is separable over $\mathbf{k}$. Let $\mathbf{I}' = \mathbf{I}\mathbf{k}'[X]$. We denote by $\mathbf{k}[X]_{\mu}, \mathbf{I}_{\mu}, \mathbf{k}'[X]_{\mu}, \mathbf{I}_{\mu}'$ the homogeneous parts of degree $\mu$ of $\mathbf{k}[X]$, $\mathbf{I}, \mathbf{k}'[X]$, $\mathbf{I}'$ respectively. Let $\mathbf{L}'$ be a $\mathbf{k}'$-submodule of $\mathbf{k}'[X]_{1}$, and let $\mathbf{L} = \mathbf{L}' \cap \mathbf{k}[X]_{1}$. Let $\bar{\mu}$ be a positive integer. Then we have

$$
\mathbf {k} ^ {\prime} [ X ] _ {\mu} \cap (\mathbf {I} ^ {\prime} \cap \mathbf {k} ^ {\prime} [ \mathbf {L} ^ {\prime} ]) \mathbf {k} ^ {\prime} [ X ] = \mathbf {I} _ {\mu} ^ {\prime}
$$

for all $\mu \leq \overline{\mu}$, if and only if

$$
\mathbf {k} [ X ] _ {\mu} \cap (\mathbf {I} \cap \mathbf {k} [ \mathbf {L} ]) \mathbf {k} [ X ] = \mathbf {I} _ {\mu}
$$

for all $\mu \leq \bar{\mu}$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{4}$  cf. Modular fields, I., by S. MacLane, Duke Math. J., 5 (1939), 372–393. Nagata [15, §39, Ch. IV].</span></small>

PROOF. The if-part of the assertion is clear. We shall prove the only-if-part of the assertion. Since  $L'$  is a  $k'$ -module of finite type, there exists a subfield  $k_{1}$  of  $k'$  which is finitely generated over k and such that the same equalities for  $\mu \leq \bar{\mu}$  remain valid if we replace  $k'$  by  $k_{1}$  and  $L'$  by  $L' \cap k_{1}[X]_{1}$ . Therefore, we may and shall assume that  $k'$  is finitely generated over k. Since  $k'$  is then finitely separably algebraic over an extension of k by a finite number of independent variables, it is sufficient to prove the assertion in two cases; one in which  $\mathbf{k}' = \mathbf{k}(u)$  with a variable u, and the other in which  $k'$  is finitely separably algebraic over k. Let us first consider the case in which  $\mathbf{k}' = \mathbf{k}(u)$  with a variable u over k. Let O be the localization of  $k[u]$  with respect to the prime ideal  $(u)\mathbf{k}[u]$ . Let  $L'' = L' \cap O[X]_{1}$  and  $I'' = IO[X]$ . It is clear that  $I_{\mu}'' = I_{\mu}' \cap O[X]_{\mu}$  for all  $\mu$ , because a k-free base of  $I_{\mu}$  is necessarily a  $k'$ -free base of  $I_{\mu}'$  and can be extended to a k-free base of  $k[X]_{\mu}$  which is necessarily an O-free base of  $O[X]_{\mu}$ . We claim that

$$
\mathbf {O} [ X ] _ {\mu} \cap (\mathbf {I} ^ {\prime \prime} \cap \mathbf {O} [ \mathbf {L} ^ {\prime \prime} ]) \mathbf {O} [ X ] = \mathbf {I} _ {\mu} ^ {\prime \prime} (= \mathbf {I} _ {\mu} ^ {\prime} \cap \mathbf {O} [ X ] _ {\mu})\tag{1}
$$

for all $\mu \leq \bar{\mu}$. It suffices to show

$$
\left(\mathbf {I} ^ {\prime} \cap \mathbf {k} ^ {\prime} [ \mathbf {L} ^ {\prime} ]\right) \mathbf {k} ^ {\prime} [ X ] \cap \mathbf {O} [ X ] = \left(\mathbf {I} ^ {\prime \prime} \cap \mathbf {O} [ \mathbf {L} ^ {\prime \prime} ]\right) \mathbf {O} [ X ].
$$

Since O is a valuation ring,  $L''$  must be a direct summand of the free O-module  $O[X]_{1}$ . Let  $(Z_{1},\cdots,Z_{r})$  be an O-free base of  $L''$ , and let us extend it to an O-free base

$$
\left(Z _ {1}, \dots , Z _ {r}, Y _ {1}, \dots , Y _ {s}\right)
$$

of $\mathbf{O}[X]_{1}$. Then $r + s = n$ and $\mathbf{O}[X] = \mathbf{O}[Z, Y]$. Thus

$$
\begin{array}{r l} (\mathbf {I} ^ {\prime} \cap \mathbf {k} ^ {\prime} [ \mathbf {L} ^ {\prime} ]) \mathbf {k} ^ {\prime} [ X ] \cap \mathbf {O} [ X ] & = (\mathbf {I} ^ {\prime} \cap \mathbf {k} ^ {\prime} [ Z ]) \mathbf {k} ^ {\prime} [ Z, Y ] \cap \mathbf {O} [ Z, Y ] \\ & = (\mathbf {I} ^ {\prime} \cap \mathbf {k} ^ {\prime} [ Z ] \cap \mathbf {O} [ Z ]) \mathbf {O} [ Z, Y ] \\ & = (\mathbf {I} ^ {\prime} \cap \mathbf {O} [ Z, Y ] \cap \mathbf {O} [ Z ]) \mathbf {O} [ Z, Y ] \\ & = (\mathbf {I} ^ {\prime \prime} \cap \mathbf {O} [ Z ]) \mathbf {O} [ Z, Y ] \\ & = (\mathbf {I} ^ {\prime \prime} \cap \mathbf {O} [ \mathbf {L} ^ {\prime \prime} ]) \mathbf {O} [ X ]. \end{array}
$$

Thus we have established (1). Now, let $\beta$ be the homomorphism of $\mathbf{O}$ onto $\mathbf{k}$ which induces the identity in $\mathbf{k}$ and annihilates $u$. This $\beta$ can be extended to a homomorphism of $\mathbf{O}[X]$ onto $\mathbf{k}[X]$ in such a way that $\beta(X_i) = X_i$ for all $i$. Then we have, by (1),

$$
\mathbf {I} _ {\mu} = \beta (\mathbf {I} _ {\mu} ^ {\prime \prime}) \subseteq \mathbf {k} [ X ] _ {\mu} \cap (\mathbf {I} \cap \mathbf {k} [ \beta (\mathbf {L} ^ {\prime \prime}) ]) \mathbf {k} [ X ],
$$

for all $\mu \leq \bar{\mu}$. Hence,

$$
\mathbf {I} _ {\mu} = \mathbf {k} [ X ] _ {\mu} \cap (\mathbf {I} \cap \mathbf {k} [ \beta (\mathbf {L} ^ {\prime \prime}) ]) \mathbf {k} [ X ]\tag{2}
$$

for all $\mu \leq \bar{\mu}$. Since $\mathbf{L}''$ is a direct summand of $\mathbf{O}[X]_{1}$, the $\mathbf{k}$-module $\beta(\mathbf{L}'')$ has the same rank as the $\mathbf{k}'$-module $\mathbf{L}'$. Moreover, by the if-part of the assertion, if $\mathbf{L}_1'$ is the $\mathbf{k}'$-module generated by $\beta(\mathbf{L}'')$ then $\mathbf{L}_1'$ has the same property as $\mathbf{L}'$. If $\mathbf{L}'$ is the smallest $\mathbf{k}'$-submodule of $\mathbf{k}'[X]_{1}$ with the property, then we must have $\mathbf{L}' = \mathbf{L}_1'$; hence, $\beta(\mathbf{L}''') = \mathbf{L}' \cap \mathbf{k}[X]_{1} = \mathbf{L}$. Therefore, in this case, (2) implies the lemma. Now, in general, $\mathbf{L}'$ must contain the smallest one with the same property, by Lemma 10, and therefore $\mathbf{L}' \cap \mathbf{k}[X]_{1} = \mathbf{L}$ must have the required property. This completes the proof for the purely transcendental case. Now, let us consider the case in which $\mathbf{k}'$ is finitely separably algebraic. We may assume that $\mathbf{k}'$ is Galois extension of $\mathbf{k}$. We may also assume that $\mathbf{L}'$ is the smallest $\mathbf{k}'$-submodule of $\mathbf{k}'[X]_{1}$ with the property. Such $\mathbf{L}'$ is unique (see Lemma 10) and therefore $\mathbf{L}'$ must be invariant under the operation of Galois group of the extension $\mathbf{k}'$ over $\mathbf{k}$ which operates on $\mathbf{k}'[X]$ in a natural way. Since $\mathbf{k}'$ is separable over $\mathbf{k}$, the invariance of $\mathbf{L}'$ implies that $\mathbf{L}'$ is generated by $\mathbf{L} = \mathbf{L}' \cap \mathbf{k}[X]_{1}$ over the field $\mathbf{k}'$. Then the assertion follows without difficulty. q.e.d.

LEMMA 13. Let $\alpha: \mathbf{R} \to \mathbf{R}'$ be a local homomorphism of regular local rings such that $\alpha$ transforms a regular system of parameters of $\mathbf{R}$ into such a system of $\mathbf{R}'$. Assume that the residue field of $\mathbf{R}'$ is separable over that of $\mathbf{R}$. Let $\mathbf{J}$ be an ideal in $\mathbf{R}$ and $\mathbf{J}'$ the ideal in $\mathbf{R}'$ generated by $\alpha(\mathbf{J})$. Then we have $t(\mathbf{J}') = t(\mathbf{J})$ and

$$
\tau^ {(i)} (\mathbf {J} ^ {\prime}) = \tau^ {(i)} (\mathbf {J})
$$

for all  $i \geq 0$ , and a regular system of  $\tau$ -parameters of R for J is transformed into such a system of  $R'$  for  $J'$ .

PROOF. Let  $(x_{1},\cdots,x_{n})$  be a regular system of parameters of R. Let M (resp.  $M'$ ) be the maximal ideal of R (resp.  $R'$ ). Then  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  can be identified with a polynomial ring  $k[X]=k[X_{1},\cdots,X_{n}]$  with k=R/M, in such a way that  $X_{j}$  corresponds to the class of  $x_{j}$  in  $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$ . Accordingly, we identify  $\mathrm{gr}_{\mathbf{M}'}(\mathbf{R}')$  with a polynomial ring  $k'[X]=k'[X_{1},\cdots,X_{n}]$  with  $k'=R'/M'$ , in such a way that  $X_{j}$  corresponds to the class of  $\alpha(x_{j})$  in  $\mathrm{gr}_{\mathbf{M}'}^{1}(\mathbf{R}')$ . The canonical homomorphism  $\tilde{\alpha}: \mathrm{gr}_{\mathbf{M}}(\mathbf{R})\to\mathrm{gr}_{\mathbf{M}'}(\mathbf{R}')$ , induced by  $\alpha$ , induces the canonical homomorphism of k into  $k'$  and leaves the  $X_{j}$  fixed. By Lemma 2, §1, we have that  $\tilde{\alpha}(\mathrm{gr}_{\mathbf{M}}(\mathbf{J},\mathbf{R}))$  generates  $\mathrm{gr}_{\mathbf{M}'}(\mathbf{J}',\mathbf{R}')$ . Applying Lemma 12 to the homogeneous ideal I= $\mathrm{gr}_{\mathbf{M}}(\mathbf{J},\mathbf{R})$  in k[X], we see that for every positive integer  $\bar{\mu}$ , if T is the smallest k-submodule of  $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$  such that

$$
\operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {J}, \mathbf {R}) = \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {R}) \cap \left(\operatorname{gr} _ {\mathbf {M}} (\mathbf {J}, \mathbf {R}) \cap \mathbf {k} [ \mathbf {T} ]\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R})
$$

for all $\mu \leq \overline{\mu}$, then the $\mathbf{k}'$-submodule $\mathbf{T}'$ of $\mathrm{gr}_{\mathbf{M}'}(\mathbf{R}')$ generated by $\mathbf{T}$ is the

smallest one such that

$$
\operatorname{gr} _ {\mathbf {M} ^ {\prime}} ^ {\mu} \left(\mathbf {J} ^ {\prime}, \mathbf {R} ^ {\prime}\right) = \operatorname{gr} _ {\mathbf {M} ^ {\prime}} ^ {\mu} \left(\mathbf {R} ^ {\prime}\right) \cap \left(\operatorname{gr} _ {\mathbf {M} ^ {\prime}} \left(\mathbf {J} ^ {\prime}, \mathbf {R} ^ {\prime}\right) \cap \mathbf {k} ^ {\prime} \left[ \mathbf {T} ^ {\prime} \right]\right) \operatorname{gr} _ {\mathbf {M} ^ {\prime}} \left(\mathbf {R} ^ {\prime}\right)
$$

for all $\mu \leq \bar{\mu}$. The assertions of Lemma 13 follow immediately. q.e.d.

## 5. Effects of permissible monoidal transformations on

$\nu^{*}(\mathbf{J})$ and $\tau^{*}(\mathbf{J})$

Let R be a regular local ring, and J an ideal in R. Let M be the maximal ideal of R.

DEFINITION 8. A prime ideal P in R is called a permissible center (of monoidal transformation) for J, if it satisfies the following conditions:

(i) $\mathbf{P} \cong \mathbf{J}$ and $\mathbf{R} / \mathbf{P}$ is regular,

(ii)  $\mathrm{gr}_{\mathrm{P}/\mathrm{J}}(\mathbf{R}/\mathbf{J})$  is flat over R/P.

The condition (ii) is proved equivalent to

(ii)\* there exists a system of element  $(f_{1},\cdots,f_{m})$  of J such that  $\nu_{\mathbf{M}}(f_{j})=\nu_{\mathbf{P}}(f_{j})$  for all j, and the initial forms of the  $f_{j}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  generate the ideal  $\mathrm{gr}_{\mathbf{M}}(\mathbf{J},\mathbf{R})$ ,

and equivalent to

(ii)\*\* there exists a standard base  $(f_{1},\cdots,f_{m})$  of J such that  $\nu_{\mathbf{P}}(f_{j})=\nu^{(j)}(\mathbf{J})$  for all j.

(See Cor. 1 of Th. 2, § 2, Ch. II.) For the sake of convenience, we agree that $\mathbf{P} = \mathbf{R}$ is a permissible center for every ideal $\mathbf{J}$ in $\mathbf{R}$.

REMARK 1. Let R be a regular local ring, J an ideal in R, and P a prime ideal in R which contains J. Let  $R \rightarrow R'$  be a local homomorphism of regular local rings which transforms a regular system of parameters of R into such a system of parameters of  $R'$ . Let  $P' = PR'$  and  $J' = JR'$ . Then  $R'$  is faithfully flat over R, and therefore  $R'/J'$  (resp.  $R'/P'$ ) is so over R/J (resp. R/P). It follows that P is a permissible center for J if and only if  $P'$  is such for  $J'$ . (See Lemma 9, § 3, Ch. II.)

REMARK 2. Let $\mathbf{R} \to \mathbf{R}'$, $\mathbf{J}$, $\mathbf{J}'$, $\mathbf{P}$ and $\mathbf{P}'$ be the same as in Remark 1. Let us assume that $\mathbf{R}/\mathbf{P}$ is regular, hence, so is $\mathbf{R}'/\mathbf{P}'$. Let $\mathbf{R}_1$ (resp. $\mathbf{R}_1'$) be a monoidal transform of $\mathbf{R}$ (resp. $\mathbf{R}'$) with center $\mathbf{P}$ (resp. $\mathbf{P}'$) such that we have the commutative diagram of canonical local homomorphisms:

$$
\begin{array}{c} \mathbf {R} _ {1} \longrightarrow \mathbf {R} _ {1} ^ {\prime} \\ \Big \uparrow \qquad \qquad \qquad \qquad \Big \uparrow \\ \mathbf {R} \longrightarrow \mathbf {R} ^ {\prime}. \end{array}
$$

Let $\mathbf{J}_1$ (resp. $\mathbf{J}_1'$) be the strict transform of $\mathbf{J}$ (resp. $\mathbf{J}'$) in $\mathbf{R}_1$ (resp. $\mathbf{R}_1'$). By Corollary to Lemma 5, §2, we have $\mathbf{J}_1' = \mathbf{J}_1\mathbf{R}_1'$. If the residue field of

$\mathbf{R}'$ is separable algebraic over that of $\mathbf{R}$, then we have

$$
\nu^ {(i)} (\mathbf {J}) = \nu^ {(i)} (\mathbf {J} ^ {\prime})
$$

and

$$
\nu^ {(i)} (\mathbf {J} _ {1}) = \nu^ {(i)} (\mathbf {J} _ {1} ^ {\prime})
$$

for all positive integers i. In fact, by Lemma 4 of §2, the local homomorphism $\mathbf{R}_1 \to \mathbf{R}_1'$ transforms a regular system of parameters of $\mathbf{R}_1$ into such a system of parameters of $\mathbf{R}_1'$. The assertion then follows by Corollary to Lemma 2, §1. Moreover, the residue field of $\mathbf{R}_1'$ is separable over that of $\mathbf{R}_1$ and we have

$$
\tau^ {(i)} (\mathbf {J}) = \tau^ {(i)} (\mathbf {J} ^ {\prime})
$$

and

$$
\tau^ {(i)} (\mathbf {J} _ {1}) = \tau^ {(i)} (\mathbf {J} _ {1} ^ {\prime})
$$

for all positive integers $i$. (See Lemma 13 of § 4.)

LEMMA 14. Let R be a regular local ring, P a prime ideal in R such that R/P is regular, and J an ideal in R which is contained in P. Let  $R_{1}$  be a monoidal transform of R with center P which is residually rational over R, and  $J_{1}$  the strict transform of J in  $R_{1}$ . Suppose that there exists a system of elements  $(f_{1}, \cdots, f_{m})$  of J and a positive integer  $i \leq m$  such that

(i) $(f_{1},\dots ,f_{m})$ is a standard base of $\mathbf{J}$;

(ii) if $\nu_{j} = \nu^{(j)}(\mathbf{J})$ for $1 \leq j \leq m$, then we have $\nu_{\mathbf{P}}(f_j) = \nu_j$ for $1 \leq j \leq i$. Suppose, furthermore, we have

$$
\left(\nu^ {(1)} (\mathbf {J}), \dots , \nu^ {(i)} (\mathbf {J})\right) \leq \left(\nu^ {(1)} \left(\mathbf {J} _ {1}\right), \dots , \nu^ {(i)} \left(\mathbf {J} _ {1}\right)\right)
$$

in the sense of lexicographical ordering. $^{5}$  Then we can find a system of elements  $(f_{1},\cdots,f_{m})$  of J which has the properties (i), (ii) as above and, in addition to these,

(iii) if $x$ is an element of $\mathbf{P}$ such that $\mathbf{PR}_1 = (x)\mathbf{R}_1$, and if $\mathbf{M}_1$ is the maximal ideal of $\mathbf{R}_1$, then $\nu_{\mathbf{M}_1}(x^{-\nu_j}f_j) = \nu_j$ for all $j \leq i$;

(iv) if  $g_{j} = x^{-\nu j}f_{j}$  for  $j \leq i$ , then  $(g_{1}, \cdots, g_{i})$  can be extended to a standard base of  $J_{1}$ .

In particular, we have

$$
\boldsymbol {\nu} ^ {(j)} (\mathbf {J}) = \boldsymbol {\nu} ^ {(j)} (\mathbf {J} _ {1})
$$

for all $j \leq i$.

PROOF. Let us choose a minimal base  $(x, x_{1}, \cdots, x_{r})$  of P, where  $r + 1 =$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{5}$  cf. Def. 2, §1, of this chapter.</span></small>

dim R - dim R/P.⁶ Then, assuming that PR₁ = (x)R₁, R₁ is a localization of the ring A₁ = R[x₁/x, ··, xᵣ/x] with respect to a maximal ideal N of A₁. Since R₁ is residually rational over R, we have the canonical isomorphism A₁/N ≈ R/M, where M denotes the maximal ideal of R. Therefore, we can find a suitable system of elements (u₁, ··, uᵣ) of R such that xⱼ/x ≡ uⱼ mod N. By replacing xⱼ by xⱼ - uⱼx for 1 ≤ j ≤ r, we may assume that xⱼ/x ∈ N for 1 ≤ j ≤ r. Then, if (y₁, ··, yₛ) is a system of elements of R such that their images in R/P form a regular system of parameters of R/P, it follows that the system of elements of R₁

$$
(x, x _ {1} / x, \dots , x _ {r} / x, y _ {1}, \dots , y _ {s})
$$

is a regular system of parameters of $\mathbf{R}_1$. (See the paragraphs of §2 preceding Lemma 4.) Let us identify $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ with $\mathbf{k}[X, X_1, \cdots, X_r, Y_1, \cdots, Y_s]$, the polynomial ring of $(r + s + 1)$ independent variables over the field $\mathbf{k} = \mathbf{R}/\mathbf{M}$, in such a way that $X, X_a, Y_b$ correspond to the classes of $x, x_a, y_b$ in $\mathrm{gr}_{\mathbf{M}}^1(\mathbf{R})$ respectively. Let us also identify $\mathrm{gr}_{\mathbf{M}_1}(\mathbf{R}_1)$ with $\mathbf{k}[X, \bar{X}_1, \cdots, \bar{X}_r, Y_1, \cdots, Y_s]$, the polynomial ring of $(r + s + 1)$ independent variables over the field $\mathbf{k} = \mathbf{R}_1/\mathbf{M}_1$, in such a way that $X, \bar{X}_a, Y_b$ correspond to the classes of $x, x_a/x, y_b$ in $\mathrm{gr}_{\mathbf{M}_1}^1(\mathbf{R}_1)$ respectively.

Now we shall carry out the proof of Lemma 14 by induction on the integer $i$. Let us first consider the case in which $i=1$. By Lemma 8 of §3, we must have $\nu_{\mathbf{M}_{1}}(x^{-\nu_{1}}f_{1}) \leq \nu_{1}$. Hence the assumption $\nu^{(1)}(\mathbf{J}) \leq \nu^{(1)}(\mathbf{J}_{1})$ implies that $\nu_{\mathbf{M}_{1}}(x^{-\nu_{1}}f_{1}) = \nu_{1}$, and that $g_{1}$ can be extended to a standard base of $\mathbf{J}_{1}$. Let us consider the case of $i>1$, and assume that the lemma is verified for smaller $i$. Thus we may assume that

(iii)' $\nu_{\mathbf{M}_1}(x^{-\nu_j}f_j) = \nu_j$ for $j\leq i - 1$ , and

(iv)'  $(g_{1},\cdots,g_{i-1})$  can be extended to a standard base of  $J_{1}$ , where  $g_{j}=x^{-\nu_{j}}f_{j}$  for all j.

Let $\varphi_{j}$ (resp. $\psi_{j}$) denote the initial form of $f_{j}$ (resp. $g_{j}$) in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R}) = \mathbf{k}[X, X_{1}, \cdots, X_{r}, Y_{1}, \cdots, Y_{s}]$ (resp. $\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1}) = \mathbf{k}[X, \bar{X}_{1}, \cdots, \bar{X}_{r}, Y_{1}, \cdots, Y_{s}]$). By (ii) and (iii)', $\varphi_{j}$ must be a form only in $X_{1}, \cdots, X_{r}$, and $\psi_{j}$ must be of the form

$$
\psi_ {j} = \varphi_ {j} (\bar {X} _ {1}, \dots , \bar {X} _ {r}) + \lambda_ {j},
$$

for all $j \leq i - 1$

where  $\lambda_{j}$  is (either 0 or) a form of degree  $\nu_{j}$  which is contained in the ideal  $(X, Y_{1}, \cdots, Y_{s})\mathbf{k}[X, \bar{X}_{1}, \cdots, \bar{X}_{r}, Y_{1} \cdots, Y_{s}]$ . In fact, we can write  $f_{j} (j \leq i - 1)$  in the form

$$
\left(\sum_ {(a)} c _ {(a)} x ^ {a _ {0}} x _ {1} ^ {a _ {1}} \dots x _ {r} ^ {a _ {r}}\right) + h
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{P}\mathbf{R}_1 = (x)\mathbf{R}_1,\mathbf{R}_1 / (x)\mathbf{R}_1$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$M_{1}^{2}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$x \notin M^{2}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{6}$  Since  $\mathbf{P}\mathbf{R}_{1}=(x)\mathbf{R}_{1},\mathbf{R}_{1}/(x)\mathbf{R}_{1}$  is regular and therefore  $x\notin M_{1}^{2}$ . Hence  $x\notin M^{2}$ , where M denotes the maximal ideal of R, so that x can be a member of a minimal base of the ideal P.</span></small>

where  $a_{0} + a_{1} + \cdots + a_{r} \geq \nu_{j}, c_{(a)} \in (y_{1}, \cdots, y_{s})^{\mu(a)} R$  with  $\mu_{(a)} = \nu_{\mathbf{M}}(c_{(a)})$  and  $h \in P^{2\nu_{j}+1}$ . Then the assumption  $\nu_{\mathbf{M}_{1}}(g_{j}) = \nu_{j}$  implies that

$$
\mu_ {(a)} + a _ {0} + 2 \left(a _ {1} + \dots + a _ {r}\right) - \nu_ {j} \geq \nu_ {j}\tag{*}
$$

for all  $(a)$  which appear in  $\sum_{(a)}$ . This means that if  $\overline{c}_{(a)}$  denotes the initial form of  $c_{(a)}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  which is a form in  $k[Y_{1},\cdots,Y_{s}]$ , then  $\psi_{j}$  is the sum of those terms  $\overline{c}_{(a)}X^{b}\overline{X}_{1}^{a_{1}}\cdots\overline{X}_{r}^{a_{r}}$  which have  $b=a_{0}+a_{1}+\cdots+a_{r}-\nu_{j}$  and  $\mu_{(a)}+b+a_{1}+\cdots+a_{r}=\nu_{j}$ . On the other hand,  $\varphi_{j}$  is the sum of those terms  $\overline{c}_{(a)}X^{a_{0}}X_{1}^{a_{1}}\cdots X_{r}^{a_{r}}$  which have  $\mu_{(a)}+a_{0}+a_{1}+\cdots+a_{r}=\nu_{j}$ , hence, in view of (\*),  $\mu_{(a)}=a_{0}=0$  and  $a_{1}+\cdots+a_{r}=\nu_{j}$ . Thus we obtain the expressions of  $\psi_{j}$  in terms of  $\varphi_{j}$  as above for  $j\leq i-1$ . We remark that if  $f_{i}$  is also such that  $\nu_{\mathbf{M}_{1}}(g_{i})=\nu_{i}$ , then we will have a similar expression for  $\psi_{i}$  in terms of  $\varphi_{i}$  and, in view of the inequality between  $\nu^{(i)}(\mathbf{J})$  and  $\nu^{(i)}(\mathbf{J}_{1})$ , we can prove (iv) by means of Lemma 1 and Definition 3 of §1.

Now suppose $\nu_{\mathbf{M}_1}(g_i) = \mu < \nu_i$. (Note that we have always $\mu \leq \nu_i$ by virtue of Lemma 8 of §3.) By the above assumption (iv)', we have

$$
\operatorname{gr} _ {\mathbf {M} _ {1}} ^ {\mu} \left(\mathbf {J} _ {1}, \mathbf {R} _ {1}\right) = \operatorname{gr} _ {\mathbf {M} _ {1}} ^ {\mu} \left(\mathbf {R} _ {1}\right) \cap \left(\psi_ {1}, \dots , \psi_ {i - 1}\right) \operatorname{gr} _ {\mathbf {M} _ {1}} \left(\mathbf {R} _ {1}\right).
$$

Therefore, we have linear combinations $h_j$ of monomials of degree $\mu - \nu_j$ ($\geq 0$) in

$$
x, x _ {1} / x, \dots , x _ {r} / x, y _ {1}, \dots , y _ {s}
$$

with coefficients in $\mathbf{R}$, such that if $\lambda_j' =$ the class of $h_j$ in $\mathrm{gr}_{\mathbf{M}_1}^{\mu - \nu_j}(\mathbf{R}_1)$, then $\psi_i = \sum_j \lambda_j' \psi_j$. This means that $g_i - \sum_k h_j g_j \in \mathbf{M}_1^{\mu + 1}$. Let $f_i' = x^{\nu_i}(g_i - \sum_j h_j g_j) = f_i - \sum_j (x^{\mu - \nu_j} h_j) x^{\nu_i - \mu} f_j$. By the above selection of $h_j$, we have $x^{\mu - \nu_j} h_j \in \mathbf{P}^{\mu - \nu_j}$. Therefore, we see that $f_i' \in \mathbf{P}^{\nu_i}$, and the class of $f_i'$ in $\mathrm{gr}_{\mathbf{M}}^{\nu_i}(\mathbf{R})$ is of the form $\varphi_i - \sum_j \delta_j \varphi_j$ with forms $\delta_j$ of degree $\nu_i - \nu_j (>0)$. It is clear that if we replace $f_i$ by $f_i'$ then the assumptions (i) and (ii) of the lemma remain valid. However, we have $\nu_{\mathbf{M}_1}(x^{-\nu_i} f_i) < \nu_{\mathbf{M}_1}(x^{-\nu_i} f_i)$. The above modification of $f_i$ can be repeated until we achieve the situation in which $\nu_{\mathbf{M}_1}(x^{-\nu_i} f_i) = \nu_i$. q.e.d.

Let R be a regular local ring, and J an ideal in R. In § 4, we have introduced the system of integers  $(\mu^{(1)}(\mathbf{J}),\cdots,\mu^{(t)}(\mathbf{J}))$  and  $(\tau^{(1)}(\mathbf{J}),\cdots,\tau^{(t)}(\mathbf{J}))$  where  $t=t(\mathbf{J})$ .

LEMMA 15. Let R, J, P, R₁, J₁ be the same as in Lemma 14. Suppose we have a system of elements  $(f_{1}, \cdots, f_{m})$  of J and a positive integer  $a \leq t(\mathbf{J})$  such that

(i) $(f_{1},\dots ,f_{m})$ is a standard base of $\mathbf{J}$, and

(ii) if $i$ is the largest integer such that $\nu^{(i)}(\mathbf{J}) = \mu^{(a)}(\mathbf{J})$, then we have

$\nu_{\mathbf{P}}(f_j) = \nu^{(j)}(\mathbf{J})$ for all $j \leq i$.

If $(\nu^{(1)}(\mathbf{J}),\dots ,\nu^{(i)}(\mathbf{J})) = (\nu^{(1)}(\mathbf{J}_1),\dots ,\nu^{(i)}(\mathbf{J}_1))$ we have

$$
\tau^ {(b)} (\mathbf {J}) \leq \tau^ {(b)} (\mathbf {J} _ {1})
$$

for all positive integer $b \leq a$

PROOF. By Lemma 14, we assume that

(iii) if $x$ is an element of $\mathbf{P}$ such that $\mathbf{PR}_1 = (x)\mathbf{R}_1$, and if $g_j = x^{-\nu_j}f_j$ with $\nu_j = \nu^{(j)}(\mathbf{J})$, then $\nu_{\mathbf{M}_1}(g_j) = \nu_j$ for all $j \leq i$, where $\mathbf{M}_1$ denotes the maximal ideal of $\mathbf{R}_1$, and

(iv)  $(g_{1}, \cdots, g_{i})$  can be extended to a standard base of  $J_{1}$ .

Let $\mathbf{k} = \mathbf{R} / \mathbf{M} = \mathbf{R}_1 / \mathbf{M}_1$ and, as in the proof of Lemma 14, let us choose a regular system of parameters $(x, x_1, \cdots, x_r, y_1, \cdots, y_s)$ of $\mathbf{R}$ such that $\mathbf{P} = (x, x_1, \cdots, x_r) \mathbf{R}$ and that $(x, x_1 / x, \cdots, x_r / x, y_1, \cdots, y_s)$ is a regular system of parameters of $\mathbf{R}_1$. Moreover, as in the proof of Lemma 14, we identify $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ with the polynomial ring $\mathbf{k}[X, X_1, \cdots, X_r, Y_1, \cdots, Y_s]$ and $\mathrm{gr}_{\mathbf{M}_1}(\mathbf{R}_1)$ with $\mathbf{k}[X, \bar{X}_1, \cdots, \bar{X}_r, Y_1, \cdots, Y_s]$. It is clear that, for the proof of Lemma 15, we have only to show that $\tau^{(a)}(\mathbf{J}) \leq \tau^{(a)}(\mathbf{J}_1)$. Let $\varphi_j$ be the initial form of $f_j$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$, and $\psi_j$ the initial form of $g_j$ in $\mathrm{gr}_{\mathbf{M}_1}(\mathbf{R}_1)$. First of all, the assumptions (ii) and (iii) imply that $\varphi_1, \cdots, \varphi_i$ are forms only in $X_1, \cdots, X_r$, and, as was seen in the proof of Lemma 14, that $\psi_j = \varphi_j(\bar{X}_1, \cdots, \bar{X}_r) + \lambda_j$ for all $j \leq i$ where $\lambda_j$ is (either 0 or) a form of degree $\nu_j$ which is contained in the ideal $(X, Y_1, \cdots, Y_s) \mathbf{k}[X, \bar{X}_1, \cdots, \bar{X}_r, Y_1, \cdots, Y_s]$. The assumption $(\nu^{(1)}(\mathbf{J}), \cdots, \nu^{(i)}(\mathbf{J})) = (\nu^{(1)}(\mathbf{J}_1), \cdots, \nu^{(i)}(\mathbf{J}_1))$ implies that $\mu^{(a)}(\mathbf{J}) = \mu^{(a)}(\mathbf{J}_1)$. Let $\bar{\mu} = \mu^{(a)}(\mathbf{J}) = \mu^{(a)}(\mathbf{J}_1)$. By (i), the above selection of the integer $i$ implies that $\mathrm{gr}_{\mathbf{M}}^{\mu}(\mathbf{J}, \mathbf{R}) = \mathrm{gr}_{\mathbf{M}}^{\mu}(\mathbf{R}) \cap (\varphi_1, \cdots, \varphi_i) \mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ for all $\mu \leq \bar{\mu}$. Therefore, we see that, if $\mathbf{I} = (\varphi_1, \cdots, \varphi_i) \mathrm{gr}_{\mathbf{M}}(\mathbf{R})$, then $\tau^{(a)}(\mathbf{J})$ is the rank of the smallest k-submodule T of $\mathrm{gr}_{\mathbf{M}}^1 (\mathbf{R})$ such that

$$
\mathbf {I} _ {\mu} = \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {R}) \cap \left(\mathbf {I} \cap \mathbf {k} [ \mathbf {T} ]\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R})
$$

for all  $\mu\leq\bar{\mu}$ , where  $I_{\mu}$  denotes the homogeneous part of degree  $\mu$  of I. Since  $\varphi_{1},\cdots,\varphi_{i}$  are all forms only in  $X_{1},\cdots,X_{r}$ , the above smallest k-submodule T with the property must be contained in the linear homogeneous part of  $k[X_{1},\cdots,X_{r}]$ . Therefore, if  $I^{0}$  denotes the homogeneous ideal in  $k[X_{1},\cdots,X_{r}]$  generated by  $\varphi_{1},\cdots,\varphi_{i}$ , then the above property of T is equivalent to the following:

$$
\mathbf {I} _ {\mu} ^ {0} = \mathbf {k} [ X _ {1}, \dots , X _ {r} ] _ {\mu} \cap (\mathbf {I} ^ {0} \cap \mathbf {k} [ \mathbf {T} ]) \mathbf {k} [ X _ {1}, \dots , X _ {r} ]
$$

for all $\mu \leq \bar{\mu}$, where $\mathbf{I}_{\mu}^{0} =$ the homogeneous part of degree $\mu$ of $\mathbf{I}^{0}$ and $\mathbf{k}[X_{1},\cdots,X_{r}]_{\mu} =$ the same of $\mathbf{k}[X_{1},\cdots,X_{r}]$. Thus $\tau^{(a)}(\mathbf{J})$ is the rank of the smallest k-submodule T of $\mathbf{k}[X_{1},\cdots,X_{r}]_{1}$ having this property. On the other hand, the assumption (iv) implies that if $\bar{\mathbf{I}} = (\psi_1,\cdots,\psi_i)\operatorname{gr}_{\mathbf{M}_1}(\mathbf{R}_1)$,

then $\overline{\mathbf{I}}_{\mu} = \mathrm{gr}_{\mathbf{M}_1}^{\mu}(\mathbf{J}_1, \mathbf{R}_1)$ for all $\mu < \bar{\mu}$. For $\mu = \bar{\mu}$, we have $\overline{\mathbf{I}}_{\bar{\mu}} \subseteq \mathrm{gr}_{\mathbf{M}_1}^{\bar{\mu}}(\mathbf{J}_1, \mathbf{R}_1)$. The integer $\tau^{(a)}(\mathbf{J}_1)$ is by definition the rank of the smallest k-submodule $\overline{\mathbf{T}}$ of $\mathrm{gr}_{\mathbf{M}_1}^1 (\mathbf{R}_1)$ which has the property that

$$
\operatorname{gr} _ {\mathbf {M} _ {1}} ^ {\mu} \left(\mathbf {J} _ {1}, \mathbf {R} _ {1}\right) = \operatorname{gr} _ {\mathbf {M} _ {1}} ^ {\mu} \left(\mathbf {R} _ {1}\right) \cap \left(\operatorname{gr} _ {\mathbf {M} _ {1}} \left(\mathbf {J} _ {1}, \mathbf {R} _ {1}\right) \cap \mathbf {k} [ \bar {\mathbf {T}} ]\right) \operatorname{gr} _ {\mathbf {M} _ {1}} \left(\mathbf {R} _ {1}\right)
$$

for all $\mu \leq \overline{\mu}$. Let $\bar{\mathbf{T}}$ denote the smallest one having this property. Then we claim that

$$
(\mathrm{v}) \overline {{\mathbf {I}}} _ {\mu} = \operatorname{gr} _ {\mathbf {M} _ {1}} ^ {\mu} (\mathbf {R} _ {1}) \cap (\overline {{\mathbf {I}}} \cap \mathbf {k} [ \overline {{\mathbf {T}}} ]) \operatorname{gr} _ {\mathbf {M} _ {1}} (\mathbf {R} _ {1})
$$

for all $\mu \leq \bar{\mu}$. This equality is clear for $\mu < \bar{\mu}$ because we have $\overline{\mathbf{I}}_{\mu} = \mathrm{gr}_{\mathbf{M}_1}^{\mu}(\mathbf{J}_1, \mathbf{R}_1)$ for all $\mu < \bar{\mu}$. Let us study the equality for $\mu = \bar{\mu}$. We have

$$
\begin{array}{l} \overline {{\mathbf {I}}} _ {\bar {\mu}} \subseteq \mathrm{gr} _ {\mathbf {M} _ {1}} ^ {\bar {\mu}} (\mathbf {R}) \cap \left(\mathrm{gr} _ {\mathbf {M} _ {1}} (\mathbf {J} _ {1}, \mathbf {R} _ {1}) \cap \mathbf {k} [ \overline {{\mathbf {T}}} ]\right) \mathrm{gr} _ {\mathbf {M} _ {1}} (\mathbf {R} _ {1}) \\ = \sum_ {\mu = 0} ^ {\bar {\mu} - 1} \left(\mathrm{gr} _ {\mathbf {M} _ {1}} ^ {\mu} (\mathbf {J} _ {1}, \mathbf {R} _ {1}) \cap \mathbf {k} [ \overline {{\mathbf {T}}} ]\right) \mathrm{gr} _ {\mathbf {M} _ {1}} ^ {\bar {\mu} - \mu} (\mathbf {R} _ {1}) + \mathrm{gr} _ {\mathbf {M} _ {1}} ^ {\mu} (\mathbf {J} _ {1}, \mathbf {R} _ {1}) \cap \mathbf {k} [ \overline {{\mathbf {T}}} ] \\ \subseteq \sum_ {\mu = 0} ^ {\bar {\mu} - 1} \left(\overline {{\mathbf {I}}} _ {\mu} \cap \mathbf {k} [ \overline {{\mathbf {T}}} ]\right) \mathrm{gr} _ {\mathbf {M} _ {1}} ^ {\bar {\mu} - \mu} (\mathbf {R} _ {1}) + \mathbf {k} [ \overline {{\mathbf {T}}} ] _ {\bar {\mu}}. \end{array}
$$

Hence

$$
\begin{array}{l} \overline {{\mathbf {I}}} _ {\bar {\mu}} \subseteq \sum_ {\mu = 0} ^ {\bar {\mu} - 1} \left(\overline {{\mathbf {I}}} _ {\mu} \cap \mathbf {k} [ \overline {{\mathbf {T}}} ]\right) \mathrm{gr} _ {\mathbf {M} _ {1}} ^ {\bar {\mu} - \mu} (\mathbf {R} _ {1}) + \overline {{\mathbf {I}}} _ {\bar {\mu}} \cap \mathbf {k} [ \overline {{\mathbf {T}}} ] \\ = \mathrm{gr} _ {\mathbf {M} _ {1}} ^ {\bar {\mu}} (\mathbf {R}) \cap \left(\overline {{\mathbf {I}}} \cap \mathbf {k} [ \overline {{\mathbf {T}}} ]\right) \mathrm{gr} _ {\mathbf {M} _ {1}} (\mathbf {R} _ {1}). \end{array}
$$

The reversed inclusion is obvious and we get

$$
\overline {{{\mathbf {I}}}} _ {\mu} ^ {-} = \operatorname{gr} _ {\mathbf {M} _ {1}} ^ {\overline {{{\mu}}}} (\mathbf {R}) \cap \left(\overline {{{\mathbf {I}}}} \cap \mathbf {k} [ \overline {{{\mathbf {T}}}} ]\right) \operatorname{gr} _ {\mathbf {M} _ {1}} (\mathbf {R} _ {1}).
$$

Now, let us consider the homomorphism $\rho$ of graded k-algebras $\mathrm{gr}_{\mathbf{M}_1}(\mathbf{R}_1)$$(= \mathbf{k}[X,\bar{X}_1,\dots ,\bar{X}_r,Y_1,\dots ,Y_s])\to \mathbf{k}[X_1,\dots ,X_r]$ such that $\rho (X) = \rho (Y_{1}) =$$\dots = \rho (Y_s) = 0$ and $\rho (\bar{X}_j) = X_j$ for $1\leq j\leq r$. From the relation between $\varphi_{j}$ and $\psi_{j}$ obtained before, we get $\rho (\psi_j) = \varphi_j$ for all $j\leq i$, hence, $\rho (\bar{\mathbf{I}}) =$$\mathbf{I}^0$. Therefore, applying $\rho$ to the both sides of the equality (v) obtained above, we get

$$
\mathbf {I} _ {\mu} ^ {0} \subseteq \mathbf {k} [ X _ {1}, \dots , X _ {r} ] _ {\mu} \cap (\mathbf {I} ^ {0} \cap \mathbf {k} [ \rho (\bar {\mathbf {T}}) ]) \mathbf {k} [ X _ {1}, \dots , X _ {r} ],
$$

and hence

$$
\mathbf {I} _ {\mu} ^ {0} = \mathbf {k} [ X _ {1}, \dots , X _ {r} ] _ {\mu} \cap (\mathbf {I} ^ {0} \cap \mathbf {k} [ \rho (\bar {\mathbf {T}}) ]) \mathbf {k} [ X _ {1}, \dots , X _ {r} ]
$$

for all $\mu \leq \bar{\mu}$. Therefore the k-module $\rho(\bar{\mathbf{T}})$ must contain the previous k-module $\mathbf{T}$. Thus we get $\tau^{(a)}(\mathbf{J}) = \text{rank of } \mathbf{T} \leq \text{rank of } \rho(\bar{\mathbf{T}}) \leq \text{rank } \bar{\mathbf{T}} = \tau^{(a)}(\mathbf{J}_1)$. q.e.d.

LEMMA 16. Let R, J, P, R₁, J₁ be the same as in Lemma 15. Let k = R/M = R₁/M₁, where M (resp. M₁) denotes the maximal ideal of R (resp. R₁). Suppose we have a system of elements (f₁, ⋯, fₘ) of J and a positive

integer $a \leq t(\mathbf{J})$ such that

(i)  $(f_{1}, \cdots, f_{m})$  is a standard base of J,

(ii) if $i$ is the largest integer such that $\nu^{(i)}(\mathbf{J}) = \mu^{(a)}(\mathbf{J})$, then $\nu_{\mathbf{P}}(f_j) = \nu^{(j)}(\mathbf{J})$ for all $j \leq i$.

Suppose furthermore  $(\nu^{(1)}(\mathbf{J}),\cdots,\nu^{(i)}(\mathbf{J}))=(\nu^{(1)}(\mathbf{J}_{1}),\cdots,\nu^{(i)}(\mathbf{J}_{1})),\;\mu^{(a)}(\mathbf{J})<\nu^{(i+1)}(\mathbf{J}_{1}),\;\mathrm{and}\;\tau^{(b)}(\mathbf{J}_{1})=\tau^{(b)}(\mathbf{J})\;\mathrm{for}\;1\leqq b\leqq a.$  Then there exists an isomorphism  $\sigma$  of graded k-algebras  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})\to\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$  such that  $\sigma(\mathrm{gr}_{\mathbf{M}}^{\mu}(\mathbf{J},\mathbf{R}))=\mathrm{gr}_{\mathbf{M}_{1}}^{\mu}(\mathbf{J}_{1},\mathbf{R}_{1})$  for all  $\mu\leqq\mu^{(a)}(\mathbf{J})$ .

PROOF. Let  $(x, x_{1}, \cdots, x_{r}, y_{1}, \cdots, y_{s})$  be a regular system of parameters of R such that  $(x, x_{1}/x, \cdots, x_{r}/x, y_{1}, \cdots, y_{s})$  is a regular system of parameters of  $R_{1}$ . As in the proof of Lemma 14, we make the identifications:  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R}) = \mathbf{k}[X, X_{1}, \cdots, X_{r}, Y_{1}, \cdots, Y_{s}]$  and  $\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1}) = \mathbf{k}[X, \bar{X}_{1}, \cdots, \bar{X}_{r}, Y_{1}, \cdots, Y_{s}]$ . Let  $g_{j} = x^{-\nu j} f_{j}$  with  $\nu_{j} = \nu^{(j)}(\mathbf{J})$  and assume that

(iii) $\nu_{\mathbf{M}_1}(g_j) = \nu_j$ for all $j \leq i$,

(iv)  $(g_{1},\cdots,g_{i})$  can be extended to a standard base of  $J_{1}$ . Let  $\varphi_{j}$  be the initial form of  $f_{j}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  and  $\psi_{j}$  that of  $g_{j}$  in  $\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ . Let  $\bar{\mu}=\mu^{(a)}(\mathbf{J})=\mu^{(a)}(\mathbf{J}_{1})$ . Then we have

$$
\psi_ {j} = \varphi_ {j} (\bar {X} _ {1}, \dots , \bar {X} _ {r}) + \lambda_ {j}
$$

for $j \leq i$,

where  $\lambda_{j}$  is a form of degree  $\nu_{j}$  contained in  $(X, Y_{1}, \cdots, Y_{s})\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ . In view of the assumption  $\nu^{(i+1)}(\mathbf{J}_{1}) > \overline{\mu}$ , we have

$$
\mathbf {g r} _ {\mathbf {M} _ {1}} ^ {\mu} (\mathbf {J} _ {1}, \mathbf {R} _ {1}) = \bar {\mathbf {I}} _ {\mu}
$$

for all $\mu \leq \bar{\mu}$

where $\overline{\mathbf{I}} = (\psi_1, \dots, \psi_i) \operatorname{gr}_{\mathbf{M}_1}(\mathbf{R}_1)$, while

$$
\operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {J}, \mathbf {R}) = \mathbf {I} _ {\mu}
$$

for all $\mu \leq \bar{\mu}$

where  $\mathbf{I}=(\varphi_{1},\cdots,\varphi_{i})\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ . Therefore it is sufficient to prove that there exists an isomorphism  $\sigma$  of graded k-algebras  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})\to\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$  such that  $\sigma(\mathbf{I})=\bar{\mathbf{I}}$ . Let  $\mu_{b}=\mu^{(b)}(\mathbf{J})=\mu^{(b)}(\mathbf{J}_{1})$  for  $1\leqq b\leqq a$  ( $\bar{\mu}=\mu_{a}$ ), and let  $j(b)$  be the largest integer such that  $\nu_{j(b)}=\mu_{b}$ . Let  $\tau_{b}=\tau^{(b)}(\mathbf{J})=\tau^{(b)}(\mathbf{J}_{1})$  for  $1\leqq b\leqq a$ . Let  $\rho$  be the homomorphism of graded k-algebras  $\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})\to\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  such that  $\rho(X)=\rho(Y_{1})=\cdots=\rho(Y_{s})=0$ , and  $\rho(\bar{X}_{j})=X_{j}$  for  $1\leqq j\leqq r$ . Let  $\bar{T}_{b}$  be the smallest k-submodule of  $\mathrm{gr}_{\mathbf{M}_{1}}^{\mathrm{i}}(\mathbf{R}_{1})$  such that

$$
\operatorname{gr} _ {\mathbf {M} _ {1}} ^ {\mu} \left(\mathbf {J} _ {1}, \mathbf {R} _ {1}\right) = \operatorname{gr} _ {\mathbf {M} _ {1}} ^ {\mu} \left(\mathbf {R} _ {1}\right) \cap \left(\operatorname{gr} _ {\mathbf {M} _ {1}} \left(\mathbf {J} _ {1}, \mathbf {R} _ {1}\right) \cap \mathbf {k} \left[ \bar {\mathbf {T}} _ {b} \right]\right) \operatorname{gr} _ {\mathbf {M} _ {1}} \left(\mathbf {R} _ {1}\right)
$$

for all $\mu \leq \mu_b$, i.e.,

$$
\overline {{{\mathbf {I}}}} _ {\mu} = \operatorname{gr} _ {\mathbf {M} _ {1}} ^ {\mu} (\mathbf {R} _ {1}) \cap \left(\overline {{{\mathbf {I}}}} \cap \mathbf {k} [ \overline {{{\mathbf {T}}}} _ {b} ]\right) \operatorname{gr} _ {\mathbf {M} _ {1}} (\mathbf {R} _ {1})
$$

for all $\mu \leq \mu_b$. Similarly, let $\mathbf{T}_b$ be the smallest $\mathbf{k}$-submodule of $\mathrm{gr}_{\mathbf{M}}^1 (\mathbf{R})$ such that

$$
\operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {J}, \mathbf {R}) = \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {R}) \cap \left(\operatorname{gr} _ {\mathbf {M}} (\mathbf {J}, \mathbf {R}) \cap \mathbf {k} [ \mathbf {T} _ {b} ]\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R})
$$

for all $\mu \leq \mu_b$, i.e.,

$$
\mathbf {I} _ {\mu} = \operatorname{gr} _ {\mathbf {M}} ^ {\mu} (\mathbf {R}) \cap \left(\mathbf {I} \cap \mathbf {k} [ \mathbf {T} _ {b} ]\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R})
$$

for all  $\mu\leq\mu_{b}$ . Then, as was seen near the end of the proof of Lemma 15, we have  $T_{b}\subseteq\rho(\bar{T}_{b})$  and  $\tau_{b}=rank of T_{b}\leq rank of \rho(\bar{T}_{b})\leq rank of \bar{T}_{b}=\tau_{b}$ . Hence we have  $T_{b}=\rho(\bar{T}_{b})$  and rank of  $\bar{T}_{b}=rank of \rho(\bar{T}_{b})$  for  $1\leq b\leq a$ . First of all, it follows that  $X,Y_{1},\cdots,Y_{s}$  are linearly independent modulo  $\bar{T}_{a}$ . Hence we can choose a linearly independent base

$$
(\bar {Z} _ {1}, \dots , \bar {Z} _ {r} X, Y _ {1}, \dots , Y _ {s})
$$

of the k-module  $\mathrm{gr}_{\mathbf{M}_{1}}^{1}(\mathbf{R}_{1})$  such that  $\bar{T}_{b}$  is generated by  $\bar{Z}_{1},\cdots,\bar{Z}_{\tau_{b}}$  for  $1\leq b\leq a$ .

Now, by the definition of  $\bar{T}_{b}$  ( $1 \leq b \leq a$ ), we can write each  $\psi_{j}$  in the following form:

$$
\psi_ {j} = \psi_ {j} ^ {\prime} + \sum_ {d = 1} ^ {j (b - 1)} \bar {\delta} _ {j d} \psi_ {d}
$$

for  $j(b-1)<j\leq j(b)$  and  $1\leq b\leq a$ , where  $\psi_{j}^{\prime}$  is a form only in  $\bar{Z}_{1},\cdots,\bar{Z}_{\tau_{b}}$  and  $\bar{\delta}_{jd}$  is a form of degree  $\nu_{j}-\nu_{d}$ . Let  $\delta_{jd}=\rho(\bar{\delta}_{jd})$ , which is a form only in  $X_{1},\cdots,X_{r}$ , and let

$$
\varphi_ {j} = \varphi_ {j} ^ {\prime} + \sum_ {d = 1} ^ {j (b - 1)} \delta_ {j d} \varphi_ {d}
$$

for $j(b - 1) < j \leq j(b)$ and $1 \leq b \leq a$. Then we see that

(1) $\overline{\mathbf{I}} = (\psi_1', \dots, \psi_i')\mathbf{k}[\bar{Z}_1, \dots, \bar{Z}_r, X, Y_1, \dots, Y_s]$

(2) $\mathbf{I} = (\varphi_1', \dots, \varphi_i')\mathbf{k}[X_1, \dots, X_r, X, Y_1, \dots, Y_s]$

(3) $\rho(\psi_j') = \varphi_j'$ for all $j \leq i$.

Let us define an isomorphism $\sigma_0$ of graded k-algebras $\mathrm{gr}_{\mathbf{M}_1}(\mathbf{R}_1) \to \mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ in such a way that

$$
\sigma_ {0} (\bar {Z} _ {j}) = \rho (\bar {Z} _ {j})
$$

$$
\text { for } 1 \leq j \leq r
$$

and

$$
\sigma_ {0} (X) = X, \quad \sigma_ {0} (Y _ {j}) = Y _ {j}
$$

$$
\text { for } 1 \leq j \leq s.
$$

Then we have $\sigma_0(\psi_j') = \rho (\psi_j') = \varphi_j'$ for all $j\leq i$; hence, $\sigma_0(\overline{\mathbf{I}}) = \mathbf{I}$. Let $\sigma$ be the inverse of this isomorphism $\sigma_0$. Then it has the property stated in Lemma 16. q.e.d.

THEOREM 3. Let R be a regular local ring, P a prime ideal in R and J an ideal in R which is contained in P. Let  $R_{1}$  be a monoidal transform of R with center P which is residually separable algebraic over R, and  $J_{1}$  the strict transform of J in  $R_{1}$ . Suppose P is a permissible center

for J. Then we have $\nu^{*}(\mathbf{J}_{1}) \leq \nu^{*}(\mathbf{J})$ and if $\nu^{*}(\mathbf{J}_{1}) = \nu^{*}(\mathbf{J})$, we have $\tau^{(i)}(\mathbf{J}_{1}) \geq \tau^{(i)}(\mathbf{J})$ for $1 \leq i \leq t(\mathbf{J}) = t(\mathbf{J}_{1}).^{7}$

PROOF. In a fixed algebraic closure of the field of quotients of R, we shall take a maximal local extension  $R'$  of R such that the local homomorphism  $R \rightarrow R'$  transforms a regular system of parameters of R into such a system of parameters of  $R'$  and induces a separable algebraic extension of the residue fields. The existence of such  $R'$  can be proved by means of Zorn's lemma and, if  $R'$  is such, then the residue field of  $R'$  does not admit any separable algebraic extension. Now, let  $R_{1}'$  be a monoidal transform of  $R'$  with center  $P' = PR'$  such that there exists a commutative diagram of canonical local homomorphisms

$$
\begin{array}{c} \mathbf {R} _ {1} \longrightarrow \mathbf {R} ^ {1}, \\ \uparrow \\ \mathbf {R} \longrightarrow \mathbf {R} ^ {\prime}. \end{array}
$$

As we have seen in Remark 1 and Remark 2 following Definition 8 of this section, if $\mathbf{J}' = \mathbf{JR}'$ and $\mathbf{J}_1'$ is the strict transform of $\mathbf{J}'$ in $\mathbf{R}_1'$, then $\nu^*(\mathbf{J}) = \nu^*(\mathbf{J}')$, $\nu^*(\mathbf{J}_1) = \nu^*(\mathbf{J}_1')$, $\tau^{(j)}(\mathbf{J}) = \tau^{(j)}(\mathbf{J}')$ for all $1 \leq j \leq t(\mathbf{J}) = t(\mathbf{J}')$, and $\tau^{(j)}(\mathbf{J}_1) = \tau^{(j)}(\mathbf{J}_1')$ for all $1 \leq j \leq t(\mathbf{J}_1) = t(\mathbf{J}_1')$. Moreover, by Lemma 4 of §2, the assumption that $\mathbf{R}_1$ is residually separable algebraic over $\mathbf{R}$ implies that $\mathbf{R}_1'$ is residually rational over $\mathbf{R}'$. Therefore, by replacing $\mathbf{R}$, $\mathbf{J}$, $\mathbf{P}$, $\mathbf{R}_1$, $\mathbf{J}_1$ by $\mathbf{R}'$, $\mathbf{J}'$, $\mathbf{P}'$, $\mathbf{R}_1'$, $\mathbf{J}_1'$ respectively, we may assume that $\mathbf{R}_1$ is residually rational over $\mathbf{R}$. In this case, the inequality $\nu^*(\mathbf{J}_1) \leq \nu^*(\mathbf{J})$ follows Lemma 14, and $\tau^{(i)}(\mathbf{J}_1) \geq \tau^{(i)}(\mathbf{J})$ for $1 \leq i \leq t(\mathbf{J}) = t(\mathbf{J}_1)$, when $\nu^*(\mathbf{J}_1) = \nu^*(\mathbf{J})$, follows Lemma 15. q.e.d.

THEOREM 4. Let $\mathbf{R}$ be a regular local ring, and $\mathbf{J}$ an ideal in $\mathbf{R}$. Let $\{\mathbf{R}_{\alpha}, \mathbf{J}_{\alpha}\}_{\alpha \geq 0}$ be an infinite sequence of regular local rings $\mathbf{R}_{\alpha}$ and ideals $\mathbf{J}_{\alpha}$ in $\mathbf{R}_{\alpha}$ such that

(1) $\mathbf{R}_0 = \mathbf{R}$, $\mathbf{J}_0 = \mathbf{J}$, $\mathbf{R}_{\alpha}$ is a monoidal transform of $\mathbf{R}_{\alpha - 1}$ with a permissible center $\mathbf{P}_{\alpha - 1}$ for $\mathbf{J}_{\alpha - 1}$ and $\mathbf{J}_{\alpha}$ is the strict transform of $\mathbf{J}_{\alpha - 1}$ in $\mathbf{R}_{\alpha}$ for all $\alpha \in \mathbf{Z}^{+}$, and

(2) $\mathbf{R}_{\alpha}$ is residually separable algebraic over $\mathbf{R}_{\alpha - 1}$ for all $\alpha \in \mathbf{Z}^{+}$. Then there exists a positive integer $\bar{\alpha}$ such that

$$
\nu^ {*} (\mathbf {J} _ {\alpha}) = \nu^ {*} (\mathbf {J} _ {\bar {\alpha}} ^ {-})
$$

for all $\alpha \geq \bar{\alpha}$

and

$$
\tau^ {(i)} (\mathbf {J} _ {\alpha}) = \tau^ {(i)} (\mathbf {J} _ {\alpha} ^ {-})
$$

for all $\alpha \geq \overline{\alpha}$

and for  $1 \leq i \leq t(\mathbf{J}_{\alpha}^{-}) = t(\mathbf{J}_{\alpha})$ .

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$t(\mathbf{J})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\nu^{*}(\mathbf{J})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\nu^{*}(\mathbf{J}) = \nu^{*}(\mathbf{J}_{1})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$t(\mathbf{J}) = t(\mathbf{J}_1)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{8}$  See the footnote  $^{7}$ .</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{7}$  The integer  $t(\mathbf{J})$  being defined as the number of distinct integers in the sequence  $\nu^{*}(\mathbf{J})$ , if  $\nu^{*}(\mathbf{J}) = \nu^{*}(\mathbf{J}_{1})$ , then  $t(\mathbf{J}) = t(\mathbf{J}_{1})$ .</span></small>

PROOF. As in the proof of Theorem 3, we again take a local extension $\mathbf{R} \to \mathbf{R}'$ such that a regular system of parameters of $\mathbf{R}$ is transformed into such a system of parameters of $\mathbf{R}'$, that the residue field of $\mathbf{R}'$ is separable algebraic over that of $\mathbf{R}$, and that the residue field of $\mathbf{R}'$ does not admit any separable algebraic extension. By induction, we choose a sequence of regular local rings $\mathbf{R}_{\alpha}'$ and ideals $\mathbf{J}_{\alpha}'$ in $\mathbf{R}_{\alpha}'$ ($\alpha \in \mathbf{Z}^{+}$) such that: $\mathbf{R}_{0}' = \mathbf{R}'$, $\mathbf{J}_{0}' = \mathbf{J}' = \mathbf{JR}'$, $\mathbf{J}_{\alpha}' = \mathbf{J}_{\alpha}\mathbf{R}'$, $\mathbf{P}_{\alpha-1}' = \mathbf{P}_{\alpha-1}\mathbf{R}_{\alpha-1}'$, and $\mathbf{R}_{\alpha}'$ is a monoidal transform of $\mathbf{R}_{\alpha-1}'$ with center $\mathbf{P}_{\alpha-1}'$ which admits a commutative diagram of canonical local homomorphisms

$$
\begin{array}{c c c} \mathbf {R} _ {\alpha} & \longrightarrow & \mathbf {R} _ {\alpha} ^ {\prime} \\ \uparrow & & \uparrow \\ \mathbf {R} _ {\alpha - 1} & \longrightarrow & \mathbf {R} _ {\alpha - 1} ^ {\prime} \end{array}
$$

for all $\alpha \in \mathbf{Z}^{+}$. Here we note that by virtue of Lemma 4 of §2, $\mathbf{R}_{\alpha} \to \mathbf{R}_{\alpha}'$ transforms a regular system of parameters of $\mathbf{R}_{\alpha}$ into such a system of parameters of $\mathbf{R}_{\alpha}'$, and the residue field of $\mathbf{R}_{\alpha}'$ is separable algebraic over that of $\mathbf{R}_{\alpha}$. By Corollary of Lemma 5 of §2, $\mathbf{J}_{\alpha}'$ is the strict transform of $\mathbf{J}_{\alpha-1}'$ in $\mathbf{R}_{\alpha}'$ for all $\alpha \in \mathbf{Z}^{+}$. As was seen in Remarks 1 and 2 following Definition 8 of this section, we have $\nu^{*}(\mathbf{J}_{\alpha}) = \nu^{*}(\mathbf{J}_{\alpha}')$ and $\tau^{(i)}(\mathbf{J}_{\alpha}) = \tau^{(i)}(\mathbf{J}_{\alpha}')$ for all $\alpha$ and for $1 \leq i \leq t(\mathbf{J}_{\alpha}) = t(\mathbf{J}_{\alpha}')$. Moreover, by Lemma 4 of §2, the assumption of separable algebraic closedness of the residue field of $\mathbf{R}'$ implies that $\mathbf{R}_{\alpha}'$ is residually rational over $\mathbf{R}_{\alpha-1}'$ for all $\alpha$. Thus we may assume that $\mathbf{R}_{\alpha}$ is already so over $\mathbf{R}_{\alpha-1}$ for all $\alpha \in \mathbf{Z}^{+}$.

Now, we shall assume this residual rationality for all $\alpha \in \mathbf{Z}^{+}$. Let $\nu_{\alpha}^{*} = \nu^{*}(\mathbf{J}_{\alpha})$, $\nu_{\alpha}^{(i)} = \nu^{(i)}(\mathbf{J}_{\alpha})$ and $\tau_{\alpha}^{(j)} = \tau^{(j)}(\mathbf{J}_{\alpha})$. By Theorem 3, the sequence $\{\nu_{\alpha}^{*}\}_{\alpha \in \mathbf{Z}^{+}}$ is monotone decreasing in the sense of Definition 2 of §1. Hence, for every positive integer $i$, the sequence of the systems $(\nu_{\alpha}^{(1)}, \cdots, \nu_{\alpha}^{(i)})$, $\alpha \in \mathbf{Z}^{+}$, is also monotone decreasing in the sense of lexicographical ordering. It is clear that this sequence must be stationary for all sufficiently large $\alpha$. Let $\nu^{(i)}$ denote the limit of $\nu_{\alpha}^{(i)}$ with respect to $\alpha \in \mathbf{Z}^{+}$, for each $i$, which is equal to $\nu_{\alpha}^{(i)}$ for all sufficiently large $\alpha$. Then we have $\nu^{(i+1)} \geq \nu^{(i)}$ for all $i \geq 1$ by the definition of $\nu^{*}(\mathbf{J})$. First of all, we note that for every positive integer $\mu$ the number of those $\nu^{(i)} = \mu$ is bounded by the rank of $\mathrm{gr}_{\mathbf{M}_{\alpha}}^{\mu}(\mathbf{R}_{\alpha})$, where $\mathbf{M}_{\alpha} =$ the maximal ideal of $\mathbf{R}_{\alpha}$, which is equal to $\binom{n + \mu - 1}{n - 1}$ if $n = \dim \mathbf{R}_{\alpha} = \dim \mathbf{R}$. Let $(\mu_1, \mu_2, \cdots)$ be the sequence of the distinct integers which appear in the sequence $(\nu^{(1)}, \nu^{(2)}, \cdots)$. For each positive integer $a$, if $\mu_a$ exists, then we must have a positive integer $i(a)$ such that $\nu^{(i)} \leq \mu_a$ for $i \leq i(a)$ and $\nu^{(i)} > \mu_a$ for $i > i(a)$. This means that, if $\mu_a$ exists, there exists a positive integer $\alpha(a)$ such that

$$
\nu^ {(i)} = \nu_ {\alpha} ^ {(i)} \leq \mu_ {a}
$$

for all $i \leq i(a)$,

and for all $\alpha \geq \alpha(a)$, and

$$
\nu_ {\alpha} ^ {(i)} > \mu_ {a}
$$

$$
\text { for   } i = i (a) + 1  ,
$$

and for all $\alpha \geq \alpha(a)$. By replacing $\alpha(a)$ by a suitably bigger integer, if necessary, we may assume that

$$
\tau_ {\alpha} ^ {(b)} = \tau_ {\alpha + 1} ^ {(b)}
$$

for all $b \leq a$,

and for all $\alpha \geq \alpha(a)$. (See Lemma 15; note that the numbers $\tau_{\alpha}^{(b)}$ are all bounded by $\dim \mathbf{R} = \dim \mathbf{R}_{\alpha}$.) Now, we arrange the integers $\alpha(a), a \in \mathbf{Z}^+$, in such a way that $\alpha(a) < \alpha(a + 1)$ for all $a$.

The proof of Theorem 4 will be completed if the sequence $(\mu_1, \mu_2, \cdots)$ is finite. Suppose the contrary. Lemma 16 implies that for each $\alpha$ such that $\alpha(a) \leq \alpha < \alpha(a+1)$, there exists an isomorphism of graded k-algebras $\sigma(\alpha): \mathrm{gr}_{\mathbf{M}_\alpha}(\mathbf{R}_\alpha) \to \mathrm{gr}_{\mathbf{M}_{\alpha+1}}(\mathbf{R}_{\alpha+1})$ such that $\sigma(\alpha)(\mathrm{gr}_{\mathbf{M}_\alpha}^\mu(\mathbf{J}_\alpha, \mathbf{R}_\alpha)) = \mathrm{gr}_{\mathbf{M}_{\alpha+1}}^\mu(\mathbf{J}_{\alpha+1}, \mathbf{R}_{\alpha+1})$ for all $\mu \leq \mu_a$, where $\mathbf{k}$ denotes the common residue field of $\mathbf{R}_\alpha$, and $\mathbf{M}_\alpha$ the maximal ideal of $\mathbf{R}_\alpha$. We can choose and fix, for each $\alpha \geq \alpha(1)$, an isomorphism of graded k-algebras $\lambda(\alpha): \mathrm{gr}_{\mathbf{M}_\alpha}(\mathbf{R}_\alpha) \to \mathbf{k}[X_1, \cdots, X_n]$ where $\mathbf{k}[X_1, \cdots, X_n]$ is a polynomial ring of $n (= \dim \mathbf{R})$ variables such that

$$
\begin{array}{l} \operatorname{gr} _ {\mathbf {M} _ {\alpha + 1}} (\mathbf {R} _ {\alpha + 1}) \\ \sigma (\alpha) \Bigg | \quad \begin{array}{c} \lambda (\alpha + 1) \\ \hline \\ \hline \mathbf {k} [ X _ {1}, \dots , X _ {r} ] \\ \hline \lambda (\alpha) \end{array} \\ \operatorname{gr} _ {\mathbf {M} _ {\alpha}} (\mathbf {R} _ {\alpha}) \end{array}
$$

is commutative for all $\alpha$. Then the images $\lambda(\alpha)(\mathrm{gr}_{\mathbf{M}_{\alpha}}^{\mu}(\mathbf{J}_{\alpha},\mathbf{R}_{\alpha}))$ in the polynomial ring are the same for all $\alpha \geq \alpha(a)$ if $\mu \leq \mu_{a}$. Call this image $\mathbf{H}_{\mu}$, and let $\mathbf{I}(a)$ be the ideal in the polynomial ring generated by $\mathbf{H}_{\mu}$ for all $\mu \leq \mu_{a}$. Clearly, $\mathbf{H}_{\mu}$ is the homogeneous part of degree $\mu$ of $\mathbf{I}(a)$. By the definition of $\mu_{a+1}$, it follows that $\mathbf{I}(a+1)$ contains $\mathbf{I}(a)$ and $\mathbf{I}(a+1) \neq \mathbf{I}(a)$. In fact, the homogeneous part of degree $\mu_{a+1}$ of $\mathbf{I}(a+1)$ is not contained in $\mathbf{I}(a)$. Thus we get an infinite sequence of strictly growing ideals $\mathbf{I}(a)$, $a \in \mathbf{Z}^{+}$. This contradicts the noetherian property of a polynomial ring. q.e.d.

PROPOSITION 1. Let R be a regular local ring, P and Q prime ideals in R, and J an ideal in R. Suppose:

(i) $\mathbf{P} \supset \mathbf{Q} \cong \mathbf{J}$ and $\mathbf{P} \neq \mathbf{Q}$,

(ii) $\mathbf{R} / \mathbf{Q}$ is regular, and

(iii) $\mathbf{P}$ is a permissible center for $\mathbf{J}$.

Let $\mathbf{R}_1$ be a monoidal transform of $\mathbf{R}$ with center $\mathbf{P}$ which is residually separable algebraic over $\mathbf{R}$, and $\mathbf{J}_1$ the strict transform of $\mathbf{J}$ in $\mathbf{R}_1$. Let us assume that there exists a prime ideal $\mathbf{Q}_1$ in $\mathbf{R}_1$ such that $\mathbf{Q}_1 \cap \mathbf{R} = \mathbf{Q}$. If $\nu^*(\mathbf{J}_1) = \nu^*(\mathbf{J})$ and $\mathbf{Q}_1$ is a permissible center for $\mathbf{J}_1$, then $\tau^*(\mathbf{J}_1) = \tau^*(\mathbf{J})$.

PROOF. As in the proof of Theorem 3, we may assume that  $R_{1}$  is residually rational over R. Then, by the assumptions on P, Q and  $Q_{1}$  we have a regular system of parameters  $(x, x_{1}, \cdots, x_{r}, y_{1}, \cdots, y_{s})$  of R such that

(1) $\mathbf{P} = (x, x_1, \cdots, x_r)\mathbf{R}$,

(2) $\mathbf{Q} \subseteq (x_1, \cdots, x_r)\mathbf{R}$, and

(3)  $(x, x_{1}/x, \cdots, x_{r}/x, y_{1}, \cdots, y_{s})$  is a regular system of parameters of  $R_{1}$ , so that  $\mathbf{Q}_{1} \subseteq (x_{1}/x, \cdots, x_{r}/x)\mathbf{R}_{1}$ . Let  $\nu_{i} = \nu^{(i)}(\mathbf{J}) = \nu^{(i)}(\mathbf{J}_{1})$ . By virtue of Lemma 14, the assumption  $\nu^{*}(\mathbf{J}_{1}) = \nu^{*}(\mathbf{J})$  implies that there exists a standard base of J, say  $(f_{1}, \cdots, f_{m})$ , such that

(4) $\nu_{\mathbf{P}}(f_j) = \nu_j$ for $1 \leq j \leq m$,

(5) $\nu_{\mathbf{P}}(g_j) = \nu_j$ for $1 \leq j \leq m$, where $g_j = f_j x^{-\nu_j}$, and

(6) $(g_{1},\dots ,g_{m})$ is a standard base of $\mathbf{J}_1$

Let us identify  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  with  $k[X, X_{1}, \cdots, X_{r}, Y_{1}, \cdots, Y_{s}]$  and  $\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$  with  $k[X, \bar{X}_{1}, \cdots, \bar{X}_{r}, Y_{1}, \cdots, Y_{s}]$  in the same way as we did in the proof of Lemma 14, where M (resp.  $M_{1}$ ) denotes the maximal ideal of R (resp.  $R_{1}$ ) and  $k = R/M = R_{1}/M_{1}$ . Let  $\varphi_{j}$  (resp.  $\psi_{j}$ ) denote the initial form of  $f_{j}$  (resp.  $g_{j}$ ) in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  (resp.  $\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ ). Then, as is easily seen, the  $\varphi_{j}$  are all forms only in  $X_{1}, \cdots, X_{r}$  by (4) and (5). Therefore, first applying a suitable linear transformation to  $(x_{1}, \cdots, x_{r})$  with coefficients in R, we may assume that  $(x_{1}, \cdots, x_{\tau_{a}})$  is a regular system of  $a^{th}\tau$ -parameters of R for J, where  $\tau_{a} = \tau^{(a)}(\mathbf{J})$  for  $1 \leq a \leq t(\mathbf{J})$ . Then, replacing each  $f_{j}$  by  $f_{j} - \sum_{i=1}^{j-1} p_{ji} f_{i}$  with suitable  $p_{ji} \in (x_{1}, \cdots, x_{r})^{\nu_{j}-\nu_{i}} R$ , we may assume that  $\varphi_{j}$  is a form only in  $X_{1}, \cdots, X_{\tau_{a}}$  for every  $(j, a)$  such that  $\nu_{j} \leq \mu^{(a)}(\mathbf{J})$ . As was seen in the proof of Lemma 14, if we write  $\varphi_{j}$  in the form  $\varphi_{j}(X_{1}, \cdots, X_{\tau_{a}})$  with  $\nu_{j} = \mu^{(a)}(\mathbf{J})$ , then we can express  $\psi_{j}$  in the form

$$
\psi_ {j} = \varphi_ {j} (\bar {X} _ {1}, \dots , \bar {X} _ {\tau_ {a}}) + \lambda_ {j}
$$

where  $\lambda_{j}$  is a form of degree  $\nu_{j}$  contained in the ideal  $(X, Y_{1}, \cdots, Y_{s})\mathbf{k}[X, \bar{X}_{1}, \cdots, \bar{X}_{r}, Y_{1}, \cdots, Y_{s}]$ . Proposition 1 follows if  $\lambda_{j}=0$  for all  $j(1 \leq j \leq m)$ . Suppose we have  $j(1 \leq j \leq m)$  such that  $\lambda_{i}=0$  for  $1 \leq i < j$  and  $\lambda_{j} \neq 0$ . The assumption that  $Q_{1}$  is a permissible center for  $J_{1}$  implies that there exist forms  $\delta_{ji}$  of degree  $\nu_{j}-\nu_{i}$  in  $(X, Y_{1}, \cdots, Y_{s})\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ , where  $\delta_{ji}=0$  for those i with  $\nu_{j}-\nu_{i}=0$ , such that  $\psi_{j}-\sum_{i=1}^{j-1}\delta_{ji}\psi_{i}\left(=\psi_{j}-\sum_{i=1}^{j-1}\delta_{ji}\varphi_{i}(\bar{X}_{1},\cdots,\bar{X}_{\tau_{a}})\right)$  is a form only in  $\bar{X}_{1},\cdots,\bar{X}_{r}$ . In view of the ex-

pression $\psi_j = \varphi_j(\bar{X}_1, \cdots, \bar{X}_r) + \lambda_j$, we see that $\lambda_j = \sum_{i=1}^{j-1} \delta_{ji} \mathcal{P}_i(\bar{X}_1, \cdots, \bar{X}_{\tau_a})$. For each $\delta_{ji} \neq 0$, we take a form $h_{ji}$ of degree $\nu_j - \nu_i$ in $(x, x_1 / x, \cdots, x_r / x, y_1, \cdots, y_s)$ with coefficients in $\mathbf{R}$ such that $\delta_{ji}$ is the initial form of $h_{ji}$ in $\mathrm{gr}_{\mathbf{M}_1}(\mathbf{R}_1)$. We let $h_{ji} = 0$ if $\delta_{ji} = 0$. Then we have $x^{\nu_j - \nu_i} h_{ji} \in \mathbf{P}^{\nu_j - \nu_i}$ for all $i (1 \leq i \leq j)$. We may replace $f_j$ by

$$
f _ {j} - \sum_ {i = 1} ^ {j - 1} (x ^ {\nu_ {j} - \nu_ {i}} h _ {j i}) f _ {j}
$$

without affecting the assumptions (4), (5) and (6). Then, after this replacement, we get that  $\lambda_{i}=0$  for all i such that  $1\leq i\leq j$ . By repeating this process (at most m times), we can get  $(f_{1},\cdots,f_{m})$  with  $\lambda_{j}=0$  for all  $j(1\leq j\leq m)$ . q.e.d.

## 6. A stability theorem of a standard base

REMARK. Let $\mathbf{R} \to \mathbf{R}'$ be a local homomorphism of regular local rings which transforms a regular system of parameters of $\mathbf{R}$ into such a system of parameters of $\mathbf{R}'$. Let $\mathbf{J}$ be an ideal in $\mathbf{R}$ and $\mathbf{J}' = \mathbf{J}\mathbf{R}'$. Let $(f_1, \cdots, f_m)$ be a system of elements of $\mathbf{J}$, and $(f_1', \cdots, f_m')$ the image of the system in $\mathbf{R}'$. The local homomorphism induces a canonical homomorphism of graded algebras $\mathrm{gr}_{\mathbf{M}}(\mathbf{R}) \to \mathrm{gr}_{\mathbf{M}'}(\mathbf{R}')$, where $\mathbf{M}$ (resp. $\mathbf{M}'$) denotes the maximal ideal of $\mathbf{R}$ (resp. $\mathbf{R}'$), and the image of $\mathrm{gr}_{\mathbf{M}}(\mathbf{J}, \mathbf{R})$ by this homomorphism generates $\mathrm{gr}_{\mathbf{M}'}(\mathbf{J}', \mathbf{R}')$. (See Lemma 2 and its Corollary of §1.) We know that $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ and $\mathrm{gr}_{\mathbf{M}'}(\mathbf{R}')$ are polynomial rings over fields, and the homomorphism $\mathrm{gr}_{\mathbf{M}}(\mathbf{R}) \to \mathrm{gr}_{\mathbf{M}'}(\mathbf{R}')$ is obtained by the coefficient field extension $\mathbf{R}/\mathbf{M} \to \mathbf{R}'/\mathbf{M}'$. In view of these facts, we can easily show that $(f_1, \cdots, f_m)$ is a standard base of $\mathbf{J}$ if and only if $(f_1', \cdots, f_m')$ is such a base of $\mathbf{J}'$.

THEOREM 5. Let R be a regular local ring, J an ideal in R, and P a prime ideal in R such that R/P is regular and  $P \supseteq J$ . Let  $R_{1}$  be a monoidal transform of R with center P which is residually separable algebraic over R, and  $J_{1}$  the strict transform of J in  $R_{1}$ . Let M (resp.  $M_{1}$ ) be the maximal ideal of R (resp.  $R_{1}$ ). Let x be an element of P such that  $PR_{1} = (x)R_{1}$ . Suppose we have a system of elements  $(f_{1}, \cdots, f_{m})$  of J such that the following conditions are satisfied:

(i) $(f_{1},\dots ,f_{m})$ is a standard base of $\mathbf{J}$,

(ii) $\nu_{\mathbf{P}}(f_j) = \nu_{\mathbf{M}}(f_j)$ for $1 \leq j \leq m$, and

(iii) $\nu_{\mathbf{M}_1}(x^{-\nu_j}f_j) = \nu_{\mathbf{M}}(f_j)$ for $1 \leq j \leq m$, where $\nu_j = \nu_{\mathbf{M}}(f_j) = \nu^{(j)}(\mathbf{J})$.

Let $g_{j} = x^{-\nu_{j}}f_{j}$ for $1 \leq j \leq m$. Then $(g_{1}, \cdots, g_{m})$ is a standard base of $\mathbf{J}_{1}$. In particular, $\nu^{*}(\mathbf{J}_{1}) = \nu^{*}(\mathbf{J})$.

PROOF. In view of the above remark, the same argument as in the proof of Theorem 3 can be used to reduce the problem to the case in which

$R_{1}$  is residually rational over R. We shall assume this. We have a regular system of parameters  $(x, x_{1}, \cdots, x_{r}, y_{1}, \cdots, y_{s})$  of R such that  $\mathbf{P} = (x, x_{1}, \cdots, x_{r})\mathbf{R}$ , and  $(x, x_{1}/x, \cdots, x_{r}/x, y_{1}, \cdots, y_{s})$  is a regular system of parameters of  $R_{1}$ . As in the proof of Lemma 14 of §5, we make the following identifications:

$$
\begin{array}{l} \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}) = \mathbf {k} [ X, X _ {1}, \dots , X _ {r}, Y _ {1}, \dots , Y _ {s} ] \\ \operatorname{gr} _ {\mathbf {M} _ {1}} (\mathbf {R} _ {1}) = \mathbf {k} [ X, \bar {X} _ {1}, \dots , \bar {X} _ {r}, Y _ {1}, \dots , Y _ {s} ] \end{array}
$$

where  $k = R/M = R_{1}/M_{1}$ . Let  $\varphi_{j}$  (resp.  $\psi_{j}$ ) be the initial form of  $f_{j}$  (resp.  $g_{j}$ ) in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  (resp.  $\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ ) for  $1 \leq j \leq m$ . By the assumptions (ii) and (iii), the  $\varphi_{j}$  are all forms only in  $X_{1}, \cdots, X_{r}$ , and the forms  $\psi_{j}$  can be written as

$$
\psi_ {j} = \varphi_ {j} (\bar {X} _ {1}, \dots , \bar {X} _ {r}) + \lambda_ {j}
$$

where  $\lambda_{j}$  is a form of degree  $\nu_{j}$  and is contained in the ideal  $(X, Y_{1}, \cdots, Y_{s})\operatorname{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ . Therefore, the proof of Theorem 5 will follow if we can show that  $\operatorname{gr}_{\mathbf{M}_{1}}(\mathbf{J}_{1}, \mathbf{R}_{1}) = (\psi_{1}, \cdots, \psi_{m})\operatorname{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ . Since  $J_{1}$  is obtained by localization from the ideal  $\bigcup_{\nu=1}^{\infty} x^{-\nu}(\mathbf{J} \cap \mathbf{P}^{\nu})$  in the ring  $A_{1} = R[x_{1}/x, \cdots, x_{r}/x]$  with respect to the prime ideal  $A_{1} \cap M_{1}$ , it is sufficient to show that for every  $f \in J$  with  $\nu_{\mathrm{P}}(f) \geq \nu > 0$ , the initial form of  $x^{-\nu}f$  in  $\operatorname{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$  belongs to the ideal  $I = (\psi_{1}, \cdots, \psi_{m})\operatorname{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ .

Now, take an arbitrary element $f \in \mathbf{J}$ such that $\nu_{\mathbf{P}}(f) \geq \nu > 0$. Let $\nu_{\mathbf{M}}(f) = \mu$. Let $g = x^{-\nu}f$ and $\mu_1 = \nu_{\mathbf{M}_1}(g)$. We shall prove that we have then an element $h \in \mathbf{J}$ such that

(1) $\nu_{\mathbf{P}}(h)\geq \nu ,$

(2) $\nu_{\mathbf{M}}(f - h) > \mu,$

(3) $\nu_{\mathbf{M}_1}(g - x^{-\nu}h) \geq \mu_1$, and

(4) the initial form of $x^{-\nu}h$ in $\mathrm{gr}_{\mathbf{M}_1}(\mathbf{R}_1)$ is in I if $\nu_{\mathbf{M}_1}(x^{-\nu}h) = \mu_1$. Suppose this is proved. If $\nu_{\mathbf{M}_1}(g - x^{-\nu}h) > \mu_1$, then $g$ and $x^{-\nu}h$ should have the same initial form in $\mathrm{gr}_{\mathbf{M}_1}(\mathbf{R}_1)$, and hence the initial form of $g$ in $\mathrm{gr}_{\mathbf{M}_1}(\mathbf{R}_1)$ must be in I by (4). If $\nu_{\mathbf{M}_1}(g - x^{-\nu}h) = \mu_1$, then we replace $f$ by $f - h$ (and $g$ by $g - x^{-\nu}h$) and apply the same result. As long as $\nu_{\mathbf{M}_1}(g - x^{-\nu}h)$ remains to be $\mu_1$, we repeat this process. But this process cannot be repeated infinitely, for the number $\nu_{\mathbf{M}}(f)$ will be then made arbitrarily big while it should be bounded by $\nu_{\mathbf{M}_1}(g) + \nu = \mu_1 + \nu$. Thus it follows that the initial form of $g$ in $\mathrm{gr}_{\mathbf{M}_1}(\mathbf{R}_1)$ is in the ideal I.

We shall prove the existence of an element $h \in \mathbf{J}$ with the properties (1)-(4) for a given element $f \in \mathbf{J}$ such that $\nu_{\mathrm{P}}(f) \geq \nu > 0$. Let $\varphi$ be the initial form of $f$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$. Then it can be written in the form

$$
\varphi = \sum_ {\alpha} \xi_ {\alpha} T _ {\alpha} (Y)
$$

where  $T_{\alpha}(Y)$  are distinct monomials in  $Y_{1}, \cdots, Y_{s}$  of degree  $t_{\alpha} (\leq \mu)$ , and  $\xi_{\alpha}$  are forms of degree  $\mu - t_{\alpha}$  only in  $X, X_{1}, \cdots, X_{r}$ . Since  $\nu_{\mathrm{P}}(f) \geq \nu$ , we have  $\mu - t_{\alpha} \geq \nu$  for all  $\alpha$ . We write each  $\xi_{\alpha}$  in the form

$$
\xi_ {\alpha} = \sum_ {\beta} \xi_ {\alpha \beta} X ^ {\beta}
$$

where  $\xi_{\alpha\beta}$  are forms of degree  $\mu - t_{\alpha} - \beta (\geq 0)$  only in  $X_{1}, \cdots, X_{r}$  for all  $\alpha$  and  $\beta$ . Then we claim the following inequalities:

$$
2 (\mu - t _ {\alpha} - \beta) + \beta + t _ {\alpha} \geq \nu + \mu_ {1}
$$

for all $\alpha$ and $\beta$. In fact, we write $f$ in the form

$$
f = \left(\sum_ {(a), \beta} c _ {(a)} \beta x ^ {\beta} x _ {1} ^ {a _ {1}} \dots x _ {r} ^ {a _ {r}}\right) + f ^ {\prime},
$$

where  $c_{(a)\beta}\in(y_{1},\cdots,y_{s})^{t(a),\beta}\mathbf{R}$  with  $t_{(a)\beta}=\nu_{\mathbf{M}}(c_{(a)\beta})$  and  $f'\in\mathbf{P}^{\nu+\mu_{1}+1}$ . Then we have  $t_{(a),\beta}+\beta+a_{1}+\cdots+a_{r}\geq\mu$  for all  $((a),\beta)$  and, since  $f'\in\mathbf{M}^{\nu+\mu_{1}+1}\subseteq\mathbf{M}^{\mu+1}$ , the initial form  $\varphi$  is the sum of those  $\overline{c}_{(a)\beta}X^{\beta}X_{1}^{a_{1}}\cdots X_{r}^{a_{r}}$  such that  $t_{(a)\beta}+\beta+a_{1}+\cdots+a_{r}=\mu$ , where  $\overline{c}_{(a)\beta}$  is the initial form of  $c_{(a)\beta}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  which is obviously a form only in  $Y_{1},\cdots,Y_{s}$ . The assumption  $\nu_{\mathbb{P}}(f)\geq\nu$  implies that  $\beta+a_{1}+\cdots+a_{r}\geq\nu$  for all  $((a),\beta)$ . If we write  $\beta'$  for  $\beta+a_{1}+\cdots+a_{r}-\nu$  for each  $((a),\beta)$ , then

$$
g = \left(\sum_ {(a), \beta} c _ {(a) \beta} x ^ {\beta^ {\prime}} (x _ {1} / x) ^ {a _ {1}} \dots (x _ {r} / x) ^ {a _ {r}}\right) + x ^ {- \nu} f ^ {\prime}.
$$

Since $x^{-\nu}f' \in \mathbf{M}_1^{\mu_1 + 1}$, the assumption $\mu_1 = \nu_{\mathbf{M}_1}(g)$ implies that

$$
t _ {(a) \beta} + \beta^ {\prime} + a _ {1} + \dots + a _ {r} \geq \mu_ {1}
$$

for all $((\alpha),\beta)$

i.e.,

( \* )

$$
2 \left(a _ {1} + \dots + a _ {r}\right) + \beta + t _ {(a) \beta} \geq \nu + \mu_ {1}
$$

for all $((\alpha),\beta)$.

Comparing the expression:

$$
\varphi = \sum_ {(a), \beta} \overline {{{c}}} _ {(a), \beta} X ^ {\beta} X _ {1} ^ {a _ {1}} \dots X _ {r} ^ {a _ {r}},
$$

obtained above, with the expression

$$
\varphi = \sum_ {\alpha , \beta} \xi_ {\alpha , \beta} X ^ {\beta} T _ {\alpha} (Y),
$$

previously given, we get from (\*) the claimed inequalities:

$$
2 (\mu - t _ {\alpha} - \beta) + \beta + t _ {\alpha} \geq \nu + \mu_ {1}
$$

for all $\alpha$ and $\beta$.

Now,  $\varphi$  belongs to  $\mathrm{gr}_{\mathbf{M}}(\mathbf{J},\mathbf{R})=(\varphi_{1},\cdots,\varphi_{m})\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ , and the  $\varphi_{j}$  are forms only in  $X_{1},\cdots,X_{r}$ . Therefore we can write

$$
\xi_ {\alpha \beta} = \sum_ {i} \xi_ {\alpha , \beta i} \mathcal {P} _ {i}
$$

where  $\xi_{\alpha\beta i}$  are forms in  $X_{1},\cdots,X_{r}$  of degree  $\mu-t_{\alpha}-\beta-\nu_{i}\left(\geq0\right)$ . Let us choose, for each  $\xi_{\alpha\beta,i}\neq0$ , an element  $h_{\alpha\beta,i}\in(x_{1},\cdots,x_{r})^{\mu-t_{\alpha}-\beta-\nu_{i}}R$  whose initial form in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  is equal to  $\xi_{\alpha\beta i}$ . Let

$$
h = \sum_ {\alpha , \beta , i} h _ {\alpha , \beta , i} f _ {i} x ^ {\beta} T _ {\alpha} (y)
$$

where  $T_{\alpha}(y)$  denotes the monomial in  $y_{1}, \cdots, y_{s}$  obtained from  $T_{\alpha}(Y)$  by replacing  $Y_{j}$  by  $y_{j} (1 \leq j \leq s)$ . Then  $\nu_{\mathbf{M}}(h) \geq (\mu - t_{\alpha} - \beta - \nu_{i}) + \nu_{i} + \beta + t_{\alpha} = \mu$ , and h has the same initial form as f. Therefore we have (2).  $\nu_{\mathbf{P}}(h) \geq \operatorname{Min} (\mu - t_{\alpha} - \beta - \nu_{i} + \nu_{i} + \beta) = \operatorname{Min} (\mu - t_{\alpha}) \geq \nu$ , hence we have (1). We can express  $x^{-\nu}h$  in the form

$$
x ^ {- \nu} h = \sum_ {\alpha , \beta , i} h _ {\alpha , \beta , i} ^ {\prime} g _ {i} x ^ {\beta^ {\prime \prime}} T _ {\alpha} (y),
$$

where $h_{\alpha, \beta, i}^{\prime} = h_{\alpha, \beta, i} / x^{\mu - t_{\alpha} - \beta - \nu_i}$, and $\beta'' = (\mu - t_{\alpha} - \beta - \nu_i) + \nu_i + \beta - \nu = (\mu - t_{\alpha} - \beta) + \beta - \nu$. Hence $\nu_{\mathbf{M}_1}(x^{-\nu}h) \geq \text{Min}(\mu - t_{\alpha} - \beta - \nu_i + \nu_i + \beta'' + t_{\alpha}) = \text{Min}(2(\mu - t_{\alpha} - \beta) + \beta + t_{\alpha} - \nu) \geq \mu_1$. Hence (3). Moreover, the above expression of $x^{-\nu}h$ tells us that, if $\nu_{\mathbf{M}_1}(x^{-\nu}h) = \mu_1$, then the initial form of $x^{-\nu}h$ in $\text{gr}_{\mathbf{M}_1}(\mathbf{R}_1)$ belongs to the ideal I generated by the initial forms of the $g_i$. Thus (4). q.e.d.

COROLLARY 1. Let $\mathbf{R}$ be a regular local ring, $\mathbf{J}$ an ideal in $\mathbf{R}$, and $\mathbf{P}$ a prime ideal in $\mathbf{R}$ such that $\mathbf{R} / \mathbf{P}$ is regular. Let $\mathbf{Q}$ be a prime ideal in $\mathbf{R}$. We assume that $\mathbf{P} \supset \mathbf{Q} \supseteq \mathbf{J}$, that $\mathbf{Q} \neq \mathbf{P}$, and that $\mathbf{Q}$ is a permissible center for $\mathbf{J}$. Let $\mathbf{R}_1$ be a monoidal transform of $\mathbf{R}$ with center $\mathbf{P}$ which is residually separable algebraic over $\mathbf{R}$, and $\mathbf{J}_1$ the strict transform of $\mathbf{J}$ in $\mathbf{R}_1$. We assume that there exists a prime ideal $\mathbf{Q}_1$ in $\mathbf{R}_1$ such that $\mathbf{Q} = \mathbf{Q}_1 \cap \mathbf{R}$. Then $\mathbf{Q}_1$ is a permissible center for $\mathbf{J}_1$. Moreover, $\nu^*(\mathbf{J}) = \nu^*(\mathbf{J}_1)$, and $\tau^*(\mathbf{J}) = \tau(\mathbf{J}_1)$.

PROOF. Let M (resp.  $M_{1}$ ) be the maximal ideal of R (resp.  $R_{1}$ ). The assumption that Q is a permissible center for J means that

(i) $\mathbf{R} / \mathbf{Q}$ is regular, and

(ii) there exists a standard base  $(f_{1},\cdots,f_{m})$  of J such that  $\nu_{\mathbf{M}}(f_{j})=\nu_{\mathbf{Q}}(f_{j})$  for  $1\leq j\leq m$ .

Since we have $\mathbf{Q}_1$ such that $\mathbf{Q}_1 \cap \mathbf{R} = \mathbf{Q} \subsetneq \mathbf{P}$, we have $x \in \mathbf{P} - \mathbf{Q}$ such that $(x)\mathbf{R}_1 = \mathbf{PR}_1$. It follows that $\mathbf{R}_Q = (\mathbf{R}_1)_{\mathbf{Q}_1}$ and that $\mathbf{R}_1 / \mathbf{Q}_1$ is a monoidal transform of $\mathbf{R} / \mathbf{Q}$ with center $\mathbf{P} / \mathbf{Q}$. Hence

(i)\* $\mathbf{R}_1 / \mathbf{Q}_1$ is regular.

Moreover, if $g_{j} = f_{j} / x^{\nu_{j}}$ with $\nu_{j} = \nu^{(j)}(\mathbf{J}) = \nu_{\mathbf{M}}(f_{j})$, then $\nu_{\mathbf{Q}_{1}}(g_{j}) = \nu_{\mathbf{Q}_{1}(\mathbf{R}_{1})\mathbf{Q}_{1}}(g_{j}) = \nu_{\mathbf{QR}_{\mathbf{Q}}} (g_{j}) = \nu_{\mathbf{QR}_{\mathbf{Q}}} (f_{j}) = \nu_{j}$. Therefore $\nu_{\mathbf{M}_{1}}(g_{j}) = \nu_{\mathbf{M}}(f_{j})$ for $1 \leq j \leq m$. By Theorem 5, $(g_{1}, \dots, g_{m})$ is a standard base of $\mathbf{J}_{1}$ and

$$
\left(\mathrm{ii}\right) ^ {*} \nu_ {\mathbf {M} _ {1}} \left(g _ {j}\right) = \nu_ {\mathbf {Q} _ {1}} \left(g _ {j}\right) (= \nu_ {j}) \text {for} 1 \leq j \leq m.
$$

By (i)\* and (ii)\*, $\mathbf{Q}_1$ is a permissible for $\mathbf{J}_1$. Moreover we have $\nu^{(j)}(\mathbf{J}) = \nu_{\mathrm{M}_1}(g_j) (= \nu_j)$ for all $j, 1 \leq j \leq m$. Since $(g_1, \cdots, g_m)$ is a standard base of $\mathbf{J}_1$, we get $\nu^*(\mathbf{J}) = \nu^*(\mathbf{J}_1)$. In view of Proposition 1, §5, it follows that $\tau^*(\mathbf{J}) = \tau^*(\mathbf{J}_1)$. q.e.d.

COROLLARY 2. Let X be an irreducible non-singular algebraic scheme, V a subscheme of X, W a subscheme of V, and B a non-singular irreducible subscheme of W such that W - B is dense in W. Let $f: X' \to X$ be the monoidal transformation of X with center B. Let $V'$ (resp. $W'$) be the strict transform of V (resp. W) on $X'$ by f. Let x be a point of B. If x is a simple point of W and if V is normally flat along W at x, then $V'$ is normally flat along $W'$ at every point $x'$ of $W'$ with $f(x') = x$.

PROOF. Let R be the local ring of X at x, J the ideal of V in R, P the prime ideal of B in R and Q the ideal of W in R. By the assumption that x is a simple point of W and V is normally flat along W at x, Q is a prime ideal in R which is a permissible center for J. By the assumption that B is non-singular, R/P is regular. Let  $x_{1}$  be a point in the closure of  $x'$  in  $X'$  such that  $f(x_{1}) = x$  and the residue field at  $x_{1}$  is algebraic (hence separable algebraic) over that at x. Let  $R_{1}$  be the local ring of  $X'$  at  $x_{1}$, and  $Q_{1}$  the prime ideal of  $W'$  in  $R_{1}$. (Note that  $x_{1}$  is a simple point of  $W'$.)  $R_{1}$  is a monoidal transform of R with center P and the ideal  $J_{1}$  of  $V'$  in  $R_{1}$  is the strict transform of J in  $R_{1}$. Now, applying Corollary 1 to R, J, P, Q,  $R_{1}$,  $J_{1}$  and  $Q_{1}$, we see that  $V'$  is normally flat along  $W'$  at  $x_{1}$. It follows that  $V'$  is normally flat along  $W'$  at  $x'$. q.e.d.

COROLLARY 3. Let R be a regular local ring, and M the maximal ideal of R. Let Q be a prime ideal in R, and J an ideal in R such that  $Q \supseteq J$ . Suppose we have a system of elements  $(g_{1}, \cdots, g_{m})$  of J such that

(i) the initial forms of the $g_{j}$ ($1 \leq j \leq m$) in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ generate the ideal $\mathrm{gr}_{\mathbf{M}}(\mathbf{J}, \mathbf{R})$, and

(ii) $\nu_{\mathbf{M}}(g_j) = \nu_{\mathrm{QRQ}}(g_j)$ for all $j$ ($1 \leq j \leq m$).

Then we have the following facts:

(a) If $\mathbf{P}$ is any prime ideal in $\mathbf{R}$ such that $\mathbf{P} \supseteq \mathbf{Q}$ and $\mathbf{R} / \mathbf{P}$ is regular, then $\mathbf{P}$ is a permissible center for $\mathbf{J}$.

(b) Let $\mathbf{P}$ be a permissible center for $\mathbf{J}$ such that $\mathbf{P} \supset \mathbf{Q}$ and $\mathbf{P} \neq \mathbf{Q}$, $\mathbf{R}_1$ a monoidal transform of $\mathbf{R}$ with center $\mathbf{P}$ which is residually separable algebraic over $\mathbf{R}$, and $\mathbf{J}_1$ the strict transform of $\mathbf{J}$ in $\mathbf{R}_1$. Suppose we have a prime ideal $\mathbf{Q}_1$ in $\mathbf{R}_1$ such that $\mathbf{Q}_1 \cap \mathbf{R} = \mathbf{Q}$. Let $x$ be an element of $\mathbf{P}$ such that $\mathbf{PR}_1 = (x)\mathbf{R}_1$, and $h_j = x^{-\nu_j}g_j$ with $\nu_j = \nu_{\mathbf{P}}(g_j)$ for each $j$ ($1 \leq j \leq m$). Then the system $(h_1, \cdots, h_m)$ of elements in $\mathbf{J}_1$ has the properties (i) and (ii) with respect to $\mathbf{R}_1$, $\mathbf{M}_1$ (= the maximal ideal of $\mathbf{R}_1$), $\mathbf{Q}_1$, and $\mathbf{J}_1$. Moreover, we have $\nu^*(\mathbf{J}) = \nu^*(\mathbf{J}_1)$.

(c) If the residue field of $\mathbf{R}$ is of characteristic zero, and there exists a prime ideal $\hat{\mathbf{Q}}$ in the completion $\hat{\mathbf{R}}$ of $\mathbf{R}$ such that $\hat{\mathbf{Q}} \cap \mathbf{R} = \mathbf{Q}$ and that $\mathbf{Q}\hat{\mathbf{R}}_{\hat{\mathbf{Q}}} = \hat{\mathbf{Q}}\hat{\mathbf{R}}_{\hat{\mathbf{Q}}}$, then the initial forms of the elements $g_j$ ($1 \leq j \leq m$) in $\mathrm{gr}_{\mathrm{QR_Q}}(\mathbf{R_Q})$ generate the ideal $\mathrm{gr}_{\mathrm{QR_Q}}(\mathbf{JR_Q}, \mathbf{R_Q})$.

PROOF. For the assertion (a), it suffices to prove that $\nu_{\mathbf{M}}(g_j) = \nu_{\mathbf{P}}(g_j)$ for all $j$. This follows Theorem 1, §3, by the fact that the regularity of $\mathbf{R} / \mathbf{P}$ implies $\nu_{\mathbf{P}}(g_j) = \nu_{\mathrm{PRP}}(g_j)$. To prove (b), we have only to show that $\nu_{\mathbf{M}}(g_j) = \nu_{\mathbf{M}_1}(h_j)$ for all $j$. In fact, if this is done, the property (i) of $(h_1, \cdots, h_m)$ follows from Theorem 5, for the reason that a suitably reordered subsystem of $(g_1, \cdots, g_m)$ is a standard base of $\mathbf{J}$ by the property (i) of this system. Moreover, (ii) of $(h_1, \cdots, h_m)$ also follows, because $x$ is a unit in $(\mathbf{R}_1)_{\mathbf{Q}_1}$ and $\mathbf{R}_{\mathbf{Q}} = (\mathbf{R}_1)_{\mathbf{Q}_1}$, so that $\nu_{\mathrm{QRQ}}(g_j) = \nu_{\mathrm{Q}_1(\mathbf{R}_1)_{\mathbf{Q}_1}}(h_j)$ for all $j$. Now, the equality $\nu_{\mathbf{M}}(g_j) = \nu_{\mathbf{M}_1}(h_j)$ for each $j$ is easily obtained by means of Lemma 8 and Theorem 1, §3. The assertion (c) follows Lemma 7, §2, Ch. II, if $\mathbf{R} / \mathbf{Q}$ is regular. The proof of (c) for the general case can first be reduced to the case in which $\mathbf{R}$ is complete. In fact, by assumption, we have a prime ideal $\hat{\mathbf{Q}}$ in the completion $\hat{\mathbf{R}}$ of $\mathbf{R}$ such that $\hat{\mathbf{Q}} \cap \mathbf{R} = \mathbf{Q}$, and that the local homomorphism of $\mathbf{R}_{\mathbf{Q}}$ into $\hat{\mathbf{R}}_{\hat{\mathbf{Q}}}$ transforms a regular system of parameters of the first local ring into such a system of parameters of the second.$^9$ It is easily seen that, if we replace $\mathbf{R}$, $\mathbf{M}$, $\mathbf{J}$ and $\mathbf{Q}$ by $\hat{\mathbf{R}}$, $\hat{\mathbf{M}}\hat{\mathbf{R}}$, $\hat{\mathbf{J}} = \hat{\mathbf{J}}\hat{\mathbf{R}}$ and $\hat{\mathbf{Q}}$ respectively, then the conditions (i) and (ii) remain satisfied by $(g_1, \cdots, g_m)$, viewed as a system of elements of $\hat{\mathbf{J}}$; and moreover the conclusion in (c) is changed into an equivalent one. Therefore, we assume that $\mathbf{R}$ is complete. We then see that $\mathbf{R}$ is a formal power series ring over a field of characteristic zero. From this, we can first deduce that if $\mathbf{Q}'$ and $\mathbf{Q}''$ are any pair of prime ideals in $\mathbf{R}$ such that $\mathbf{Q}' \supset \mathbf{Q}''$, then the integral closure of $\mathbf{R}_{\mathbf{Q}'} / \mathbf{Q}''\mathbf{R}_{\mathbf{Q}'}$ in its field of quotients is a finite module over this ring.$^{10}$ Thus, to prove (c), we shall assume that $\mathbf{R}$ has this property which obviously remains valid if we replace $\mathbf{R}$ by a ring of quotients of $\mathbf{R}$ with respect to any prime ideal. Now, by an obvious induction on the dimension of $\mathbf{R} / \mathbf{Q}$, the proof of (c) can be reduced to the case in which dim $(\mathbf{R} / \mathbf{Q}) = 1$. Assume that dim $(\mathbf{R} / \mathbf{Q}) = 1$. Let $\mathbf{R}_1$ be any monoidal transform of $\mathbf{R}$ with center $\mathbf{M}$ which is residually algebraic (hence, separable algebraic) over $\mathbf{R}$, and such that there exists a prime ideal $\mathbf{Q}_1$ in $\mathbf{R}_1$ such that $\mathbf{Q}_1 \cap \mathbf{R} = \mathbf{Q}$. Let $\mathbf{J}_1$ be the strict transform of $\mathbf{J}$ in $\mathbf{R}_1$, $x$ an element of $\mathbf{M}$ such that $\mathbf{MR}_1 = (x)\mathbf{R}_1$, and $h_j = x^{-\nu_j}g_j$ with $\nu_j = \nu_{\mathbf{M}}(g_j)$ for each $j$. Then we have $\mathbf{R}_{\mathbf{Q}} =$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Q\$\hat{R}\$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\hat{Q}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{9}$  We recall the fact that a localization of a regular local ring by any prime ideal is regular. (This fact is due to J. P. Serre, Sur la dimension homologique des anneaux et des modules noethériens, Proc. of the International Symposium, Tokyo-Nikko (1955), Scientific Council of Japan, 1956, pp. 175–189.) Replace  $\hat{Q}$ , if necessary, by a minimal divisor of  $Q\hat{R}$  which is contained in it.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$R / Q^{\prime \prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{10}$  This follows from the fact that  $R/Q''$  satisfies the finiteness condition. (Recall the fact that this condition is satisfied by every complete noetherian local ring without nilpotent elements.)</span></small>

$(\mathbf{R}_{1})_{\mathbf{Q}_{1}}, \mathbf{J}\mathbf{R}_{\mathbf{Q}} = \mathbf{J}_{1}(\mathbf{R}_{1})_{\mathbf{Q}_{1}}$, and $(g_{j})\mathbf{R}_{\mathbf{Q}} = (h_{j})(\mathbf{R}_{1})_{\mathbf{Q}_{1}}$ for each $j$. Therefore, in view of (b), the assertion (c) remains equivalent if we replace $\mathbf{R}, \mathbf{J}, \mathbf{Q}, \mathbf{M}$ and $(g_{1}, \cdots, g_{m})$ by $\mathbf{R}_{1}, \mathbf{J}_{1}, \mathbf{Q}_{1}, \mathbf{M}_{1}$, and $(h_{1}, \cdots, h_{m})$ respectively. Therefore, if $\mathbf{R}_{1}/\mathbf{Q}_{1}$ is regular, then the proof is done. If otherwise, we repeat the same process. As is easily seen, this process cannot be repeated infinitely many times, because the integral closure of $\mathbf{R}/\mathbf{Q}$ in its field of quotients is a finite $\mathbf{R}/\mathbf{Q}$-module. q.e.d.

## 7. A regular frame, a regular  $\tau$ -frame, and a normalized standard base with respect to a regular frame

Let $Z^{r}$ denote the r times direct product of the additive group of integers Z with itself, and $Z_{0}^{r}$ the subset of $Z^{r}$ consisting of those $A = (a_{1}, \cdots, a_{r}) \in Z^{r}$ which have $a_{i} \geq 0$ for all $i(1 \leq i \leq r)$. A subset E of $Z_{0}^{r}$ will be called an E-subset of $Z_{0}^{r}$ if $A + B \in E$ for every pair of $A \in E$ and $B \in Z_{0}^{r}$. (The empty subset is an E-subset of $Z_{0}^{r}$.) A subset F of an E-subset E of $Z_{0}^{r}$ will be called a bound of E if every element A of E can be written in the form $A = A_{0} + B$ with $A_{0} \in F$ and $B \in Z_{0}^{r}$. If this is the case, we shall also say that E is bounded by F. If F is any subset of $Z_{0}^{r}$, then there exists a unique E-subset E of $Z_{0}^{r}$ such that E contains F, and F is a bound of E. Moreover, if E is an E-subset of $Z_{0}^{r}$, then there exists a finite subset F of E which is a bound of E. This fact can be verified by induction on r. If r = 1, then it is clear. Suppose it is proved for every E-subset of $Z_{0}^{r-1}$, where $r \geq 2$. Let E be an arbitrary E-subset of $Z_{0}^{r}$. Let p be the projection map of $Z^{r}$ onto the product $Z^{r-1}$ of the first r - 1 factors of $Z^{r}$. Then we can easily show that $p(E)$ is an E-subset of $Z_{0}^{r-1}$. Then, by the induction assumption, $p(E)$ is bounded by a finite subset of $p(E)$. Take $A_{1}, \cdots, A_{p} \in E$ such that $p(E)$ is bounded by $\{p(A_{1}), \cdots, p(A_{p})\}$. Let $\bar{a}$ be the maximum of the last components of the $A_{i}(1 \leq i \leq p)$. By the same reason, for each integer a with $0 \leq a < \bar{a}$, we can find a finite number of elements $A_{i}^{a}(1 \leq i \leq p_{a})$ of E such that $A_{i}^{a} \in E \cap (Z_{0}^{r-1} \times a)$ and $\{p(A_{1}^{a}), \cdots, p(A_{p_{a}}^{a})\}$ is a bound of $p(E \cap (Z_{0}^{r-1} \times a))$. Then, as is easily seen, the finite set of elements of E $\{A_{1}, \cdots, A_{p}, A_{i}^{a},$ with $0 \leq a < \bar{a}$ and $1 \leq i \leq p_{a}\}$ is a bound of E.

Let S be a noetherian ring, and G a polynomial ring over S. Let  $(Z_{1},\cdots,Z_{r})$  be a system of independent variables over S such that  $G = S[Z_{1},\cdots,Z_{r}]$ . If  $A = (a_{1},\cdots,a_{r})$  is an element of  $Z_{0}^{r}$ , then we shall write  $Z^{A}$  for the monomial  $Z_{1}^{a_{1}}\cdots Z_{r}^{a_{r}}$  in the ring G. We shall view  $Z_{0}^{r}$  as an ordered set by means of the lexicographic ordering. Namely, for  $A = (a_{1},\cdots,a_{r}) \in \mathbf{Z}_{0}^{r}$  and  $A' = (a_{1}',\cdots,a_{r}') \in \mathbf{Z}_{0}^{r}$ , we say that  $A < A'$  if there exists an index  $i(1 \leq i \leq r)$  such that  $a_{j} = a_{j}'$  for all j < i and  $a_{i} < a_{i}'$ .

Let $\varphi$ be a non-zero form of $Z_{1},\cdots,Z_{r}$ in G. Then it can be written in a unique manner as a linear combination of monomials $Z^{A}(A\in\mathbf{Z}_{0}^{r})$ with coefficients in S. Let us denote by $A^{r}(\varphi)$ the largest element in $\mathbf{Z}_{0}^{r}$ such that the monomial $Z^{A^{r}(\varphi)}$ appears in the above expression of $\varphi$ with a non-zero coefficient in S. If I is a homogeneous ideal in $\mathbf{G}=\mathbf{S}[Z_{1},\cdots,Z_{r}]$, then we denote by $E^{r}(\mathbf{I})$ the $E$-subset of $\mathbf{Z}_{0}^{r}$ bounded by the set consisting of $A^{r}(\varphi)$ with homogeneous $\varphi\in\mathbf{I}$; $E^{r}(\mathbf{I})$ is empty if $\mathbf{I}=(0)$. Here we view G as a graded S-algebra in such a way that the homogeneous part of degree $n$ of G consists of the forms of degree $n$ in $Z_{1},\cdots,Z_{r}$ with coefficients in S. We see that $A\in E^{r}(\mathbf{I})$ if and only if $A=A^{r}(\varphi)$ with a form $\varphi$ in I. We shall call $A^{r}$ the $E$-function of G (or, of the forms in G) with respect to $(\mathbf{S};Z_{1},\cdots,Z_{r})$ (or, with respect to the coefficient ring S and the system of indeterminates $(Z_{1},\cdots,Z_{r}))$. We shall call $E^{r}(\mathbf{I})$ the $E$-set of the homogeneous ideal I in G with respect to $(\mathbf{S};Z_{1},\cdots,Z_{r})$ (or, with respect to the coefficient ring S and the system of indeterminates $(Z_{1},\cdots,Z_{r}))$.

REMARK 1. Let  $S_{0} \rightarrow S$  be a monomorphism of noetherian rings. Let  $G_{0} = S_{0}[Z_{1}, \cdots, Z_{r}]$ , and  $G = S[Z_{1}, \cdots, Z_{r}]$  with r independent variables  $Z_{1}, \cdots, Z_{r}$ . View  $G_{0}$  and G as graded algebras over  $S_{0}$  and S, respectively, in such a way that the homogeneous part of degree n is the submodule over  $S_{0}$  and S, respectively, generated by the monomials of degree n in  $Z_{1}, \cdots, Z_{r}$ . The monomorphism  $S_{0} \rightarrow S$  can be extended in a canonical way to a monomorphism of graded algebras  $G_{0} \rightarrow G$ . Let  $I_{0}$  be a homogeneous ideal in  $G_{0}$  and  $I = I_{0}G$ . Then, as is easily seen, the E-set  $E^{r}(I)$  of the ideal I in G with respect to  $(S; Z_{1}, \cdots, Z_{r})$  contains the E-set  $E^{r}(I_{0})$  of  $I_{0}$  in  $G_{0}$  with respect to  $(S_{0}; Z_{1}, \cdots, Z_{r})$ . We have  $E^{r}(I) = E^{r}(I_{0})$  if  $S_{0}$  does not contain any zero-divisor of S (except the zero element). In fact, the equality can be easily proved when S is a ring of fractions of  $S_{0}$  with respect to a multiplicatively closed subset of  $S_{0}$  which does not contain any zero-divisor of  $S_{0}$ . So the proof in the general case is reduced to the case in which  $S_{0}$  is a field. In this case, S is a free  $S_{0}$-module. Every homogeneous element  $\varphi'$  of I is then written in the form

$$
\varphi^ {\prime} = \sum_ {i} a _ {i} \varphi_ {i}
$$

where the  $a_{i}$  are elements of S which are linearly independent over  $S_{0}$ , and the  $\varphi_{i}$  are homogeneous elements of  $I_{0}$  which have the same degree as  $\varphi'$ . Then one can easily see that  $A^{r}(\varphi') = \max\{A^{r}(\varphi_{i})\}$ .

REMARK 2. Let S be a noetherian ring. Let  $(Z_{1},\cdots,Z_{r})$  be a system of independent variables over S. Let t be an integer such that  $1\leq t<r$ . Let  $G_{0}=S[Z_{1},\cdots,Z_{t}]$  and  $G=S[Z_{1},\cdots,Z_{r}]$ . Let  $I_{0}$  be a homogeneous

ideal in  $G_{0}$  and  $I = I_{0}G$ . Let  $E^{t}(I_{0})$  be the E-set of  $I_{0}$  with respect to  $(\mathbf{S}, Z_{1}, \cdots, Z_{t})$ , and  $E^{r}(\mathbf{I})$  the E-set of I with respect to  $(\mathbf{S}; Z_{1}, \cdots, Z_{r})$ . Then  $E^{t}(I_{0})$  is an E-subset of  $Z_{0}^{t}$  and  $E^{r}(\mathbf{I})$  an E-subset of  $Z_{0}^{r}$ . We have a canonical injection  $q: Z_{0}^{t} \to Z_{0}^{r}$  such that, if  $A = (a_{1}, \cdots, a_{t}) \in \mathbf{Z}_{0}^{t}$ , then  $q(A) = (a_{1}, \cdots, a_{t}, 0, \cdots, 0) \in \mathbf{Z}_{0}^{r}$ . We can prove that  $E^{r}(\mathbf{I})$  is bounded by  $q(E^{t}(I_{0}))$ . In fact, let  $G'$  be the graded S-subalgebra of G generated by  $Z_{t+1}, \cdots, Z_{r}$ . Let  $\mathbf{I}(n), \mathbf{I}_{0}(n), \mathbf{G}'(n)$  denote the homogeneous part of degree n of  $I, I_{0}, G'$  respectively. Then we have  $\mathbf{I}(n) = \sum_{i=0}^{n} \mathbf{I}_{0}(i)\mathbf{G}'(n - i)$ . Let  $\varphi'$  be an arbitrary element of I which is homogeneous of degree n. If we write  $\varphi' = \sum_{i=0}^{n} \varphi_{i}$  with  $\varphi_{i} \in \mathbf{I}_{0}(i)\mathbf{G}'(n - i)$ . Then we see that no two of the  $\varphi'_{i}$  have a common monomial with non-zero coefficients. Hence  $A^{r}(\varphi_{i}') = A^{r}(\varphi')$  for some i, where  $A^{r}$  denotes the E-function of G with respect to  $(\mathbf{S}; Z_{1}, \cdots, Z_{r})$ . Moreover, if  $\varphi' \in I_{0}(i)\mathbf{G}'(n - i)$  and if  $\varphi'$  is written in the form  $\varphi' = \sum_{j} \varphi_{j} T_{j}$  where  $T_{j}$  are distinct monomials of degree n - i in  $Z_{t+1}, \cdots, Z_{r}$ , and  $\varphi_{i} \in I_{0}(i)$ , then we have

$$
\begin{array}{r l} A ^ {r} (\varphi^ {\prime}) & = \max \left\{A ^ {r} (\varphi_ {j} T _ {j}) \right\} \\ & = \max \left\{q (A ^ {t} (\varphi_ {j})) + A ^ {r} (T _ {j}) \right\}, \end{array}
$$

where  $A^{t}$  denote the E-function of  $G_{0}$  with respect to  $(\mathbf{S}, Z_{1}, \cdots, Z_{t})$ .

Let S be a noetherian ring, and R a formal power series ring of r independent variables over S. Say  $R = S\{z_{1}, \cdots, z_{r}\}$ . Then every element f of R can be uniquely expressed in a formal power series:

$$
f = \sum_ {A \in \mathbf {Z} _ {0} ^ {r}} c _ {A} z ^ {A}
$$

with $c_{A}\in \mathbf{S}$

where  $z^{A}$  with  $A = (a_{1}, \cdots, a_{r})$  denotes the monomial  $z_{1}^{a_{1}} \cdots z_{r}^{a_{r}}$  in the variables  $z_{j}$ . This expression will be called the power series expansion of f with respect to  $(\mathbf{S}; z_{1}, \cdots, z_{r})$ . If  $A = (a_{1}, \cdots, a_{r})$ , we shall denote by  $|A|$  the sum  $a_{1} + \cdots + a_{r}$ . By the homogeneous part of degree n of f, we shall mean the sum of those terms  $c_{A}z^{A}$  in the above expansion which have  $|A| = n$ .

LEMMA 17. Let S be a complete local ring, and R a formal power series ring  $S\{z_{1},\cdots,z_{r}\}$  of r variables  $z_{j}(1\leq j\leq r)$  over S. Let N be the maximal ideal of S and M the maximal ideal of R, i.e.,  $\mathbf{M}=(\mathbf{N},z_{1},\cdots,z_{r})\mathbf{R}$ . Let  $k=R/M=S/N$  and  $k[Z_{1},\cdots,Z_{r}]$  the graded k-subalgebra of  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  which is generated by the initial forms  $Z_{j}$  of  $z_{j}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  for  $1\leq j\leq r$ . Let  $(f_{1},\cdots,f_{m})$  be a system of elements of R such that the initial form  $\varphi_{j}$  of  $f_{j}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  belongs to  $k[Z_{1},\cdots,Z_{r}]$  for  $1\leq j\leq m$ . Let  $\mathbf{I}=(\varphi_{1},\cdots,\varphi_{m})\mathbf{k}[Z_{1},\cdots,Z_{r}]$ , and E=the E-set  $E^{r}(\mathbf{I})$  of I with respect to  $(\mathbf{k};Z_{1},\cdots,Z_{r})$ . Then, for each element f of R, we can find a system of elements  $(h_{1},\cdots,h_{m})$  of R such that

(1) $\nu_{\mathbf{M}}(h_i) \geq \nu_{\mathbf{M}}(f) - \nu_{\mathbf{M}}(f_i)$ for $1 \leq i \leq m$, and

(2) in the power series expansion (with respect to  $(\mathbf{S}; z_{1}, \cdots, x_{r})$ ):

$$
f - \sum_ {i = 1} ^ {m} h _ {i} f _ {i} = \sum_ {A \in \mathbf {Z} _ {0} ^ {r}} c _ {A} z ^ {A},
$$

with $c_{A}\in \mathbf{S}$

we have $c_A = 0$ for all $A \in E$.

PROOF. For each element $g$ of $\mathbf{R}$, we define the symbol $e(g)$ as follows: Let $g = \sum_{A \in \mathbf{Z}_0^r} d_A z^A$ be the power series expansion of $g$. Then $e(g)$ is the minimum of the integers $|A| + \nu_{\mathbf{N}}(d_A)$, such that $d_A \neq 0$ and $A \in E$, if it exists, and $e(g) = \infty$ if $d_A = 0$ for all $A \in E$.

Now, let $f$ be an arbitrary element of $\mathbf{R}$, we shall prove the existence of $(h_1, \cdots, h_m)$ having the properties (1) and (2). If $e(f) = \infty$, then we set $h_i = 0$ for $1 \leq i \leq m$ and the assertion is trivially valid. Let us assume that $e(f) < \infty$. Clearly $e(f) \geq \nu_{\mathrm{M}}(f)$. In view of the completeness of the local ring $\mathbf{R}$, it suffices to show that there exists a system of elements $(h_1, \cdots, h_m)$ of $\mathbf{R}$ such that

(1)' $\nu_{\mathbf{M}}(h_i) \geq e(f) - \nu_{\mathbf{M}}(f_i)$ for $1 \leq i \leq m$, and

$$
(2) ^ {\prime} e \big (f - \sum_ {i = 1} ^ {m} h _ {i} f _ {i} \big) > e (f).
$$

Let $\sum_{A\in \mathbf{Z}_0^r}c_Az^A$ be the power series expansion of $f$. Let $e = e(f)$ and $E(e)$ be the subset of $E$ consisting of those $A\in E$ which have $|A|\leq e$. Then $E(e)$ is a finite ordered set. Let $\bar{A}$ be the largest element of $E(e)$ such that $|\bar{A}| + \nu_{\mathbf{N}}(c_{\bar{A}}) = e$. We have a form $\varphi \in \mathbf{I}$ such that $\bar{A} = A^{r}(\varphi)$. By replacing $\varphi$ by its multiple by a non-zero element of $\mathbf{k}$, if necessary, we may assume that the coefficient of $Z^{\bar{A}}$ in $\varphi$ is equal to one. We can write

$$
\varphi = \sum_ {i} \lambda_ {i} \varphi_ {i}
$$

where  $\lambda_{i}$  is a form in  $k[Z_{1},\cdots,Z_{r}]$  of degree  $|\bar{A}|-\deg\varphi_{i}=|\bar{A}|-\nu_{M}(f_{i})$  ( $\geq0$ ). For each  $\lambda_{i}$ , we choose

$$
h _ {i} ^ {0} \in (z _ {1}, \dots , z _ {r}) ^ {| \overline {{{A}}} | - \nu_ {\mathbf {M}} (f _ {i})} \mathbf {R}
$$

which has $\lambda_{i}$ as its initial form in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$. Let $h_i = c_A h_i^0$ for $1 \leq i \leq m$. These $h_i$ have the property (1)$^{\prime}$. If they have the property (2)$^{\prime}$, then the proof is done. In any case, we have $\nu_{\mathbf{M}}(\sum_{i=1}^{m} h_i f_i) \geq e(f)$ and therefore

$$
e \big (f - \sum_ {i = 1} ^ {m} h _ {i} f _ {i} \big) \geq e (f).
$$

Let $f' = f - \sum_{i=1}^{m} h_i f_i$, and assume that $e(f') = e(f)$. We then claim that if $\sum_{A \in Z_0^r} c_A' z^A$ is the power series expansion of $f'$, we have $\bar{A} > A$ for every $A \in E(e)$ such that $|A| + \nu_{\mathrm{N}}(c_A') = e$. This property of $f'$ can be easily verified by showing that both $f - c_{\bar{A}} z^{\bar{A}}$ and $c_{\bar{A}} z^{\bar{A}} - \sum_{i=1}^{m} h_i f_i$ have the property. Now, if $e(f') = e(f)$ then we replace $f$ by $f'$ and repeat the same process as above. Since $E(e)$ is a finite set, the above fact

shows that we come to the situation in which  $e(f') > e(f)$  after a finite number of times. q.e.d.

DEFINITION 9. (1) Let R be a regular local ring. Let  $S \rightarrow R$  be a local homomorphism of regular local rings, and  $(z_{1}, \cdots, z_{r})$  a system of elements of R which can be extended to a regular system of parameters of R. (This system may be empty, i.e., r = 0.) If  $\mathbf{R}/(z_{1}, \cdots, z_{r})\mathbf{R}$  is canonically isomorphic to S, then the system  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  will be called a regular frame of R. If  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  is a regular frame of R, then  $\mathbf{P} = (z_{1}, \cdots, z_{r})\mathbf{R}$  is a prime ideal of R and the completion of R with respect to the powers of P is canonically isomorphic to the formal power series ring  $\mathbf{S}\{z_{1}, \cdots, z_{r}\}$  of the r independent variables over the ring S. Let N (resp. M) be the maximal ideal of S (resp. R),  $k = S/N = R/M$ , and  $k[Z] = k[Z_{1}, \cdots, Z_{r}]$  the graded k-subalgebra of  $\mathrm{gr}_{\mathrm{M}}(\mathbf{R})$  generated by the initial forms  $Z_{i}$  of  $z_{i}$  in  $\mathrm{gr}_{\mathrm{M}}(\mathbf{R})$  for  $1 \leq i \leq r$ . This k-subalgebra  $k[Z]$  of  $\mathrm{gr}_{\mathrm{M}}(\mathbf{R})$  will be called the associated (graded) subalgebra of the regular frame  $(\mathbf{S}; z_{1}, \cdots, z_{r})$ .

(2) Let  $(f_{1},\cdots,f_{i})$  be a system of elements of R whose initial forms in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  belong to the associated subalgebra  $\mathbf{k}[Z]$  of  $(\mathbf{S};z_{1},\cdots,z_{r})$ . (The system  $(f_{1},\cdots,f_{i})$  may be empty, i.e., i=0.) Let I denote the ideal in  $\mathbf{k}[Z]$  generated by the initial forms of  $f_{j}(1\leq j\leq i)$ . Let E denote the E-set of I in  $\mathbf{k}[Z]$  with respect to  $(\mathbf{k};Z_{1},\cdots,Z_{r})$ . We say that an element g of R is normalized by the system  $(f_{1},\cdots,f_{i})$  with respect to the regular frame  $(\mathbf{S};z_{1},\cdots,z_{r})$  of R, if in the power series expansion

$$
\sum_ {A \in Z _ {0} ^ {r}} c _ {A} z ^ {A},
$$

$$
\boldsymbol {c} ^ {A} \in \mathbf {S}
$$

of the element $g$ in $\mathbf{S}\{z_1, \cdots, z_r\}$ we have $c_A = 0$ for all $A \in E$.

(3) A system of elements  $(f_{1}, \cdots, f_{m})$  of R will be said to be normalized with respect to  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  if the following conditions are satisfied:

(i) the initial form of $f_{i}$ in $\mathbf{gr}_{\mathbf{M}}(\mathbf{R})$ belongs to the associated subalgebra of $(\mathbf{S}; z_1, \cdots, z_r)$ for $1 \leq i \leq m$, and

(ii)  $f_{i}$  is normalized by  $(f_{1},\cdots,f_{i-1})$  with respect to  $(\mathbf{S};z_{1},\cdots,z_{r})$  for  $1\leq i\leq m$ .

(4) A standard base of an ideal J in R will be called a normalized standard base of J with respect to  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  if it is normalized with respect to  $(\mathbf{S}; z_{1}, \cdots, z_{r})$ .

LEMMA 18. Let R be a regular local ring,  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  a regular frame of R, and J an ideal in R. Let  $(f_{1}, \cdots, f_{i})$  be a system of elements of J such that

(i) $(f_{1},\dots ,f_{i})$ can be extended to a standard base of $\mathbf{J}$, and

(ii) the initial forms of $f_{j}(1 \leq j \leq i)$ belong to the associated sub-

algebra of $(\mathbf{S};z_1,\dots ,z_r)$

Let $f$ be an element of $\mathbf{J}$ such that

(iii) $f$ is normalized by $(f_{1},\cdots,f_{i})$ with respect to $(\mathbf{S};z_{1},\cdots,z_{r})$. Let $\mathbf{P}$ be a prime ideal in $\mathbf{R}$ such that

(iv)  $\mathbf{P} \cong (z_{1}, \cdots, z_{r})\mathbf{R},$

(v) $\mathbf{P}$ is a permissible center for $\mathbf{J}$, and

(vi) $\nu_{\mathbf{P}}(f_j) = \nu^{(j)}(\mathbf{J})$ for $1 \leq j \leq i$.

Then we have

$$
\nu_ {\mathbf {P}} (f) \geq \nu^ {(i + 1)} (\mathbf {J}).
$$

Moreover,  $\nu_{\mathbf{M}}(f)=\nu^{(i+1)}(\mathbf{J})$  for the maximal ideal M of R if and only if  $(f_{1},\cdots,f_{i},f)$  can be extended to a standard base of J.

PROOF. Let $\hat{\mathbf{R}}$ be the completion of $\mathbf{R}$ with respect to the topology defined by the powers of the ideal $(z_1, \cdots, z_r)\mathbf{R}$. Then we have $\hat{\mathbf{R}} = \mathbf{S}\{z_1, \cdots, z_r\}$. The local homomorphism $\mathbf{R} \to \hat{\mathbf{R}}$ transforms a regular system of parameters of $\mathbf{R}$ into such a system of parameters of $\hat{\mathbf{R}}$, so that the assumptions (i)-(vi) remain valid for $\hat{\mathbf{R}}$, $(\mathbf{S}; z_1, \cdots, z_r)$, $\mathbf{J}\hat{\mathbf{R}}$, $(f_1, \cdots, f_i, f)$ and $\mathbf{P}\hat{\mathbf{R}}$, and that the conclusion is replaced by an equivalent one. Therefore we may assume that $\mathbf{R} = \mathbf{S}\{z_1, \cdots, z_r\}$. We can write in a unique way

$$
f = \sum_ {A \in \mathbf {Z} _ {0} ^ {r}} c _ {A} z ^ {A},
$$

with $c_{A}\in \mathbf{S}$

Let $\overline{\nu} = \nu^{(i+1)}(\mathbf{J})$. First we want to show that $\nu_{\mathrm{P}}(c_A) \geq \overline{\nu} - |A|$ for all $A \in \mathbf{Z}_0^r$, or equivalently, $\nu_{\mathrm{P}}(f) \geq \overline{\nu}$. Let us choose a system of elements $(y_1, \cdots, y_t)$ of $\mathbf{R}$ such that their residue classes modulo $\mathbf{P}$ form a regular system of parameters of $\mathbf{R}/\mathbf{P}$. By means of this system we get an isomorphism of simply graded k-algebras

$$
\psi \colon \mathrm{gr} _ {\overline {{\mathbf {M}}}} ^ {0} \big (\mathrm{gr} _ {\mathbf {P}} (\mathbf {R}) \big) \otimes_ {\mathbf {k}} \mathrm{gr} _ {\overline {{\mathbf {M}}}} (\bar {\mathbf {R}}) \longrightarrow \mathrm{gr} _ {\mathbf {M}} (\mathbf {R}),
$$

where $\mathbf{M} =$ the maximal ideal of $\mathbf{R}$, $\overline{\mathbf{M}} = \mathbf{M} / \mathbf{P}$, $\overline{\mathbf{R}} = \mathbf{R} / \mathbf{P}$, and $\mathbf{k} = \mathbf{R} / \mathbf{M} = \overline{\mathbf{R}} / \overline{\mathbf{M}}$. (See the paragraph preceding Lemma 8 of §2, Ch. II.) We also have the canonical isomorphism of doubly graded k-algebras

$$
\varphi \colon \operatorname{gr} _ {\overline {{\mathbf {M}}}} ^ {0} \bigl (\operatorname{gr} _ {\mathbf {P}} (\mathbf {R}) \bigr) \otimes_ {\mathbf {k}} \operatorname{gr} _ {\overline {{\mathbf {M}}}} (\overline {{\mathbf {R}}}) \to \operatorname{gr} _ {\overline {{\mathbf {M}}}} \bigl (\operatorname{gr} _ {\mathbf {P}} (\mathbf {R}) \bigr).
$$

(See the paragraph preceding Lemma 2 of §1, Ch. II.) Thus we get an isomorphism of simply graded k-algebras

$$
\lambda = \psi \circ \varphi^ {- 1} \colon \operatorname{gr} _ {\overline {{\mathbf {M}}}} (\operatorname{gr} _ {\mathbf {P}} (\mathbf {R})) \to \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}).
$$

Let $\Phi_0$ be the initial form of $f$ in $\mathrm{gr}_{\overline{\mathbf{M}}}(\mathrm{gr}_{\mathbf{P}}(\mathbf{R}))$. (See the paragraph preceding Lemma 10 of §3, Ch. II.) By virtue of Lemma 10 of §3, Ch. II, the assumption (v) implies that $\lambda (\Phi_0)\in \mathrm{gr}_{\mathbf{M}}(\mathbf{J},\mathbf{R})$. Let $\mu$ be the minimum of the integers $|A| + \nu_{\mathbf{P}}(c_A)$ for $A\in \mathbf{Z}_0^r$. We want to show that $\mu \geq \overline{\nu}$.

Suppose  $\mu < \bar{\nu}$ . Then the initial form  $\Phi$  of f in  $\mathrm{gr}_{\mathrm{P}}(\mathbf{R})$  can be written in the form

$$
\Phi = \sum \Gamma_ {A} \hat {Z} ^ {A}
$$

$$
\text { for } | A | + \nu_ {\mathrm{P}} (c _ {A}) = \mu
$$

where  $\Gamma_{A}$  denotes the initial form of  $c_{A}$  in  $\mathrm{gr}_{\mathrm{P}}(\mathbf{R})$ , and  $(\hat{Z}) = (\hat{Z}_{1}, \cdots, \hat{Z}_{r})$  is the system of initial forms of  $z_{1}, \cdots, z_{r}$  in  $\mathrm{gr}_{\mathrm{P}}(\mathbf{R})$ . Let n be the maximal integer such that  $\Phi \in \bar{\mathbf{M}}^{n} \operatorname{gr}_{\mathrm{P}}(\mathbf{R})$ , i.e.,  $\Gamma_{A} \in \bar{\mathbf{M}}^{n} \operatorname{gr}_{\mathrm{P}}(\mathbf{R})$  for all A with  $|A| + \nu_{\mathrm{P}}(c_{A}) = \mu$ . Let  $\gamma_{A}$  be the  $\lambda$ -image of the class of  $\Gamma_{A}$  in  $\mathrm{gr}_{\overline{\mathbf{M}}}^{n}(\mathrm{gr}_{\mathrm{P}}(\mathbf{R}))$ , and  $(Z_{1}, \cdots, Z_{r})$  the system of initial forms of  $z_{1}, \cdots, z_{r}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ . Then we have

$$
\lambda (\Phi_ {0}) = \sum \gamma_ {A} Z ^ {A}
$$

$$
\text { for } | A | + \nu_ {\mathrm{P}} (c _ {A}) = \mu .
$$

Let us choose a minimal base  $(z_{1},\cdots,z_{r},x_{1},\cdots,x_{s})$  of P, which is an extension of the system  $(z_{1},\cdots,z_{r})$ . Then  $(z_{1},\cdots,z_{r},x_{1},\cdots,x_{s},y_{1},\cdots,y_{t})$  is a regular system of parameters of R. Let us identify  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  with the polynomial ring  $\mathbf{k}[Z_{1},\cdots,Z_{r},X_{1},\cdots,X_{s},Y_{1},\cdots,Y_{t}]$  of  $r+s+t(=\dim\mathbf{R})$  indeterminates, where  $Z_{j}$  (resp.  $X_{j}$ , resp.  $Y_{j}$ ) is the initial form of  $z_{j}$  (resp.  $x_{j}$ , resp.  $y_{j}$ ) in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ . Then we see that  $\gamma_{A}$  is doubly homogeneous of degree  $\mu-|A|$  in  $X_{1},\cdots,X_{s}$  and of degree n in  $Y_{1},\cdots,Y_{t}$ . The assumption (v) implies that  $\mathrm{gr}_{\mathbf{M}}(\mathbf{J},\mathbf{R})$  is generated by forms in  $Z_{1},\cdots,Z_{r},X_{1},\cdots,X_{s}$ .  $\lambda(\Phi_{0})$  is homogeneous of degree  $\mu$  in these variables. Therefore  $\lambda(\Phi_{0})\in\mathrm{gr}_{\mathbf{M}}^{\mu}(\mathbf{J},\mathbf{R})\mathrm{gr}_{\mathbf{M}}^{n}(\mathbf{R})$ . Since  $\mu<\overline{\nu}=\nu^{(i+1)}(\mathbf{J}),\lambda(\Phi_{0})\in(\varphi_{1},\cdots,\varphi_{i})\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  because of the assumption (i), where  $\varphi_{j}=$  the initial form of  $f_{j}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  for  $1\leq j\leq i$ . Let  $E^{r}$  be the E-set of the ideal  $(\varphi_{1},\cdots,\varphi_{i})\mathbf{k}[Z_{1},\cdots,Z_{r}]$  with respect to  $(\mathbf{k};Z_{1},\cdots,Z_{r})$ . Let  $E^{r+s}$  be the E-set of  $(\varphi_{1},\cdots,\varphi_{i})\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  with respect to  $(\mathbf{k}[Y];Z_{1},\cdots,Z_{r},X_{1},\cdots,X_{s})$ . Let  $A^{r+s}$  be the E-function of  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  with respect to  $(\mathbf{k}[Y];Z_{1},\cdots,Z_{r},X_{1},\cdots,X_{s})$ . Then  $A^{r+s}(\lambda(\Phi_{0}))\in E^{r+s}$ . It is clear from the expression

$$
\lambda (\Phi_ {0}) = \sum \gamma_ {A} Z ^ {A}
$$

$$
\text { for } | A | + \nu_ {\mathrm{P}} (c _ {A}) = \mu ,
$$

that, if $q$ is the canonical injection $\mathbf{Z}_0^r \to \mathbf{Z}_0^{r + s} = \mathbf{Z}_0^r \times \mathbf{Z}_0^s$, then

$$
A ^ {r + s} \left(\lambda \left(\Phi_ {0}\right)\right) = q (\bar {A}) + B
$$

with some $\bar{A}$ with $|\bar{A}| + \nu_{\mathbf{P}}(c_{\bar{A}}) = \mu$ and $B \in (0) \times \mathbf{Z}_0^s$. By Remark 1, $E^{r+s}$ is also the $E$-set of $(\varphi_1, \cdots, \varphi_i)\mathbf{k}[Z_1, \cdots, Z_r, X_1, \cdots, X_s]$ with respect to $(\mathbf{k}; Z_1, \cdots, Z_r, X_1, \cdots, X_s)$; and, by Remark 2, $E^{r+s}$ is bounded by $q(E^r)$. It follows that the above $\bar{A} \in E^r$. However $|\bar{A}| + \nu_{\mathbf{P}}(c_{\bar{A}}) = \mu$ implies that $c_{\bar{A}} \neq 0$. This is a contradiction to (iii). Thus $\nu_{\mathbf{P}}(f) \geq \nu^{(i+1)}(\mathbf{J})$. Now the assumptions (i)-(vi) and the above argument remain valid for $\mathbf{M} = \mathbf{P}$. In this case, $\Phi = \Phi_0 = \lambda(\Phi_0)$, and it is the initial form of $f$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$. The argument in this case shows that the initial form of $f$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$

should not belong to  $(\varphi_{1},\cdots,\varphi_{i})\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ . Therefore  $\nu^{(i+1)}(\mathbf{J})=\nu_{\mathbf{M}}(f)$  implies that  $(f_{1},\cdots,f_{i},f)$  can be extended to a standard base of J. q.e.d.

THEOREM 6. Let R be a regular local ring,  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  a regular frame of R, and J an ideal in R. Let  $(f_{1}, \cdots, f_{m})$  be a normalized standard base of J with respect to  $(\mathbf{S}; z_{1}, \cdots, z_{r})$ . Let P be a prime ideal in R such that R/P is regular and  $\mathbf{P} \supseteq (z_{1}, \cdots, z_{r})\mathbf{R}$ . Then P is a permissible center for J if and only if  $\nu_{\mathbf{P}}(f_{j}) = \nu^{(j)}(\mathbf{J})$  for  $1 \leq j \leq m$ .

PROOF. The if-part is trivial, and the only-if-part is an immediate consequence of Lemma 18.

DEFINITION 10\*. Let R be a regular local ring, M the maximal ideal of R, and  $(z_{1}, \cdots, z_{r})$  a system of elements of R which can be extended to a regular system of parameters of R. (This system may be empty.) Let  $Z_{j}$  be the initial form of  $z_{j}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  for  $1 \leq j \leq r$ . Then  $(Z) = (Z_{1}, \cdots, Z_{r})$  is a system of linearly independent linear forms in  $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$ . Let k = R/M. Let  $(f_{1}, \cdots, f_{i})$  be a system of elements of R and  $(\varphi_{1}, \cdots, \varphi_{i})$  the system of the initial forms of  $f_{j}$  ( $1 \leq j \leq i$ ) in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ . Let T denote the smallest k-submodule of  $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$  such that

$$
\left(\left(\varphi_ {1}, \dots , \varphi_ {i}\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}) \cap \mathbf {k} [ \mathbf {T} ]\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}) = \left(\varphi_ {1}, \dots , \varphi_ {i}\right) \operatorname{gr} _ {\mathbf {M}} (\mathbf {R}).
$$

Let $\mathbf{T}^{*}$ be the k-submodule of $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$ generated by $\mathbf{T}$ and $Z_{1},\cdots,Z_{r}$. We define the integer $\tau_{(z)}(f_1,\cdots,f_i)$ to be the rank of $\mathbf{T}^{*}$ minus $r$. A system of elements $(x_{1},\cdots,x_{\tau})$ of $\mathbf{M}$ with $\tau=\tau_{(z)}(f_{1},\cdots,f_{i})$ will be called a regular system of $\tau_{(z)}$-parameters of $\mathbf{R}$ for $(f_{1},\cdots,f_{i})$ if the classes of $x_{1},\cdots,x_{\tau}$ in $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$ and $Z_{1},\cdots,Z_{r}$ generate the k-submodule $\mathbf{T}^{*}$ of $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$. Note that $\mathbf{T},\mathbf{T}^{*}$ and $\tau_{(z)}(f_1,\cdots,f_i)$ are uniquely determined by the given systems $(z_{1},\cdots,z_{r})$ and $(f_{1},\cdots,f_{i})$. (See Lemma 10, §4.) If $(z)$ is an empty system, then we write $\tau(f_1,\cdots,f_i)$ for $\tau_{(z)}(f_1,\cdots,f_i)$ and we call the above $(x_{1},\cdots,x_{\tau})$ a regular system of $\tau$-parameters of $\mathbf{R}$ for $(f_{1},\cdots,f_{i})$.

LEMMA 19. Let R be a regular local ring,  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  a regular frame of R, and J an ideal in R. Let  $(f_{1}, \cdots, f_{i})$  be a system of elements of J such that  $\tau_{(z)}(f_{j}) = 0$  for  $1 \leq j \leq i$ . Let f be an element of J. Let a be the positive integer such that  $\mu^{(a)}(\mathbf{J}) = \nu^{(i+1)}(\mathbf{J})$ . Suppose:

(i) $(f_{1},\dots ,f_{i},f)$ can be extended to a standard base of $\mathbf{J}$, and

(ii) $f$ is normalized by $(f_{1},\cdots,f_{i})$ with respect to $(\mathbf{S};z_{1},\cdots,z_{r})$. Let $\mathbf{T}^{*}$ be the $\mathbf{k}$-submodule of $\mathrm{gr}_{\mathbf{M}}^{\mathrm{l}}(\mathbf{R})$ which is generated by the initial forms of a regular system of $a^{\text{th}}$$\tau$-parameters of $\mathbf{J}$ and those of $(z)=(z_{1},\cdots,z_{r})$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$. Then the initial form of $f$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ is contained in the $\mathbf{k}$-subalgebra $\mathbf{k}[\mathbf{T}^{*}]$ of $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$, where $\mathbf{k}=$ the residue field of $\mathbf{R}$.

PROOF. Let us choose a system of elements  $(x_{1}, \cdots, x_{t})$  of S such that

$(z_{1},\cdots,z_{r},x_{1},\cdots,x_{t})$  can be extended to a regular system of parameters of R, and that  $T^{*}$  is generated by the initial forms  $Z_{1},\cdots,Z_{r},X_{1},\cdots,X_{t}$  of  $z_{1},\cdots,z_{r},x_{1},\cdots,x_{t}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ . Let  $(y_{1},\cdots,y_{s})$  be a system of elements of S such that

$$
(z _ {1}, \dots , z _ {r}, x _ {1}, \dots , x _ {t}, y _ {1}, \dots , y _ {s})
$$

is a regular system of parameters of $\mathbf{R}$. Let $Y_{j}$ be the initial form of $y_{j}$ ($1 \leq j \leq s$) in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$. Then we have $\mathrm{gr}_{\mathbf{M}}(\mathbf{R}) = \mathbf{k}[Z_1, \cdots, Z_r, X_1, \cdots, X_t, Y_1, \cdots, Y_s]$. Let $\varphi_j$ (resp. $\varphi$) be the initial form of $f_j$ (resp. $f$) in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ for $1 \leq j \leq i$. We have $\varphi_j \in \mathbf{k}[Z]$ for all $j$, $1 \leq j \leq i$. Let $E^r$ be the $E$-set of $(\varphi_1, \cdots, \varphi_i)\mathbf{k}[Z]$ with respect to $(\mathbf{k}; Z_1, \cdots, Z_r)$. Let

$$
f = \sum_ {A \in \mathbf {Z} _ {0} ^ {r}} c _ {A} z ^ {A}
$$

with $c_{A}\in \mathbf{S}$

be the power series expansion of f in  $S\{z_{1}, \cdots, z_{r}\}$ . Then, by (ii),  $c_{A} = 0$  for all  $A \in E$ . Let  $\mu = \nu^{(j+1)}(\mathbf{J})$ . We have  $\nu_{\mathbf{M}}(c_{A}) \geq \mu - |A|$  for all  $A \in Z_{0}^{r}$ . Let  $\overline{c}_{A}$  denote the initial form of  $c_{A}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ . Then we have

$$
\varphi = \sum \overline {{c}} _ {A} Z ^ {A}
$$

$$
\text { for } | A | + \nu_ {\mathbf {M}} (c _ {A}) = \mu .
$$

We want to show that  $\bar{c}_{A}$  with those A are all forms in  $X_{1}, \cdots, X_{t}$ . Let us write

$$
\overline {{{c}}} _ {A} = \overline {{{c}}} _ {A} ^ {\prime} + \overline {{{c}}} _ {A} ^ {\prime \prime}
$$

where  $\overline{c}_{A}^{\prime}\in\mathbf{k}[X_{1},\cdots,X_{t}]$ , and  $\overline{c}_{A}^{\prime\prime}\in(Y_{1},\cdots,Y_{s})\mathbf{k}[X,Y]$ . Then, by the selection of  $(x_{1},\cdots,x_{t})$  we must have that the form

$$
\varphi^ {\prime \prime} = \sum \bar {c} _ {A} ^ {\prime \prime} Z ^ {A}
$$

$$
\text { for } | A | + \nu_ {\mathbf {M}} (c _ {A}) = \mu
$$

belongs to the ideal  $(\varphi_{1},\cdots,\varphi_{i})\operatorname{gr}_{\mathbf{M}}(\mathbf{R})$ . Let  $E^{r+t+s}$  be the E-set of  $(\varphi_{1},\cdots,\varphi_{i})\operatorname{gr}_{\mathbf{M}}(\mathbf{R})$  with respect to  $(\mathbf{k};Z_{1},\cdots,Z_{r},X_{1},\cdots,X_{t},Y_{1},\cdots,Y_{s})$ . Let q be the canonical injection of  $Z_{0}^{r}$  into  $Z_{0}^{r}\times Z_{0}^{t+s}=Z_{0}^{r+t+s}$ . Let  $A^{r+t+s}$  be the E-function of k[Z, X, Y] with respect to  $(\mathbf{k};Z_{1},\cdots,Z_{r},X_{1},\cdots,X_{t},Y_{1},\cdots,Y_{s})$ . If  $\varphi^{\prime\prime}\neq0$ , then we have

$$
A ^ {r + t + s} \left(\varphi^ {\prime \prime}\right) \in E ^ {r + t + s}.
$$

It is clear from the above expression of $\varphi''$ that we have $\bar{A}$ such that $|\bar{A}| + \nu_{\mathbf{M}}(c_{\bar{A}}) = \mu$, and that

$$
A ^ {r + t + s} (\varphi^ {\prime \prime}) = q (\bar {A}) + B,
$$

where $B \in (0) \times \mathbf{Z}_0^{t+s}$. However, by Remark 2, $E^{r+t+s}$ is bounded by $q(E^r)$ and hence we should have $\bar{A} \in E^r$, which is impossible. We conclude that $\varphi'' = 0$ and $\bar{c}_A = \bar{c}_A' \in \mathbf{k}[X]$ for all $A$ with $|A| + \nu_{\mathbf{M}}(c_A) = \mu$. q.e.d.

DEFINITION 10. Let R be a regular local ring, and J an ideal in R. A regular frame  $(\mathbf{S}; z_{1}, \cdots, z_{\tau})$  of R will be called a regular  $\tau$ -frame

of R for J if  $(z_{1}, \cdots, z_{\tau})$  is a regular system of  $\tau$ -parameters of R for J. (See Definition 7, § 4.)

THEOREM 7. Let R be a regular local ring, J an ideal in R and  $(\mathbf{S}; z_{1}, \cdots, z_{\tau})$  a regular  $\tau$ -frame of R for J. Let  $t = t(\mathbf{J})$ , so that  $\tau = \tau^{(t)}(\mathbf{J})$ . Let  $\tau_{a} = \tau^{(a)}(\mathbf{J})$  for  $1 \leq a \leq t$ . Let  $m_{a}$  be the maximal integer such that  $\nu^{(m_{a})}(\mathbf{J}) = \mu^{(a)}(\mathbf{J})$  for  $1 \leq a \leq t$ . If  $(f_{1}, \cdots, f_{m})$  is a normalized standard base of J with respect to  $(\mathbf{S}; z_{1}, \cdots, z_{\tau})$ , then for every  $a (1 \leq a \leq t)$  the initial forms of  $f_{1}, \cdots, f_{m_{a}}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  are all contained in the k-subalgebra of  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  generated by the initial forms of  $z_{1}, \cdots, z_{\tau_{a}}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ , where M denotes the maximal ideal of R and k = R/M.

PROOF. First of all, R may be assumed to be complete with respect to the topology defined by the powers of  $(z_{1},\cdots,z_{\tau})\mathbf{R}$ . (Namely, the proof in the general case can be easily reduced to this special case.) Hence  $R = S\{z_{1},\cdots,z_{\tau}\}$ . We shall prove the assertion of the theorem by induction on a. For a = 1, the assertion is clear from the definition of a regular system of  $\tau$ -parameters of R for J. Assume that the assertion is verified for a certain  $a \geq 1$ . By the completeness of R, if  $S_{a} = S\{z_{\tau_{a}+1},\cdots,z_{\tau}\}$ , then  $(\mathbf{S}_{a}; z_{1},\cdots,z_{\tau_{a}})$  is a regular frame of R. By the induction assumption, the initial forms of  $f_{1},\cdots,f_{m_{a}}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  belong to the associated k-subalgebra of  $(\mathbf{S}_{a}; z_{1},\cdots,z_{\tau_{a}})$ . We can easily see that if j is any integer such that  $1 \leq j \leq m_{a+1} - m_{a}$  then  $(f_{1},\cdots,f_{m_{a}},f_{m_{a}+j})$  can be extended to a standard base of J. Moreover, as is easily seen,  $f_{m_{a}+j}$  is normalized by  $(f_{1},\cdots,f_{m_{a}})$  with respect to  $(\mathbf{S}; z_{1},\cdots,z_{\tau})$  and therefore, in view of Remarks 1 and 2,  $f_{m_{a}+j}$  is normalized by  $(f_{1},\cdots,f_{m_{a}})$  with respect to  $(\mathbf{S}_{a}; z_{1},\cdots,z_{\tau_{a}})$ . Therefore, by Lemma 19, the initial form of  $f_{m_{a}+j}$  ( $1 \leq j \leq m_{a+1} - m_{a}$ ) in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  belongs to the k-subalgebra of  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  generated by the initial forms of  $z_{1},\cdots,z_{\tau_{a+1}}$ . q.e.d.

## 8. Effects of permissible monoidal transformations on a normalized standard base

Let $(\mathbf{S}; z_{1}, \cdots, z_{r})$ be a regular frame of R, and P a prime ideal in R such that R/P is regular. Let $R_{1}$ be a monoidal transform of R with center P. We have an element x of $R_{1}$ such that $\mathbf{PR}_{1} = (x)\mathbf{R}_{1}$. Such an element x of $R_{1}$ is uniquely determined up to a unit multiple of $R_{1}$. We shall say that $(\mathbf{S}; z_{1}, \cdots, z_{r})$ admits a frame transform in $R_{1}$ if there exist $x \in R_{1}$ with $(x)\mathbf{R}_{1} = \mathbf{PR}_{1}$ and a monoidal transform $S_{1}$ of S with center $P \cap S$ such that $(\mathbf{S}_{1}; z_{1}/x, \cdots, z_{r}/x)$ is a regular frame of $R_{1}$ in a canonical manner. Clearly, these conditions imply that $z_{i} = x(z_{i}/x) \in \mathbf{PR}_{1} \cap \mathbf{R}_{1} = \mathbf{P}$ for all i, i.e., $P \supseteq (z_{1}, \cdots, z_{r})\mathbf{R}$, and hence that $S/P \cap S$ is regular. Moreover, $S_{1}$ is then the unique monoidal transform of S with center $P \cap S$.

which admits a canonical local homomorphism  $S_{1} \rightarrow R_{1}$ . We see that  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  admits a frame transform in  $R_{1}$  if and only if there exist  $x \in P \cap S$  such that  $\mathbf{PR}_{1} = (x)\mathbf{R}_{1}$  and  $(z_{1}/x, \cdots, z_{r}/x)$  are all non-units of  $R_{1}$ . We shall call  $(\mathbf{S}_{1}; z_{1}/x, \cdots, z_{r}/x)$  the frame transform of  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  in  $R_{1}$  (with denominator x).

LEMMA 20. Let R be a regular local ring, J an ideal in R and  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  a regular frame in R. Let  $(f_{1}, \cdots, f_{i}, f)$  be a system of elements of J such that

(1) $(f_{1},\dots ,f_{i},f)$ can be extended to a standard base of $\mathbf{J}$,

(2) $\tau_{(z)}(f_j) = 0$ for $1 \leq j \leq i$ where $(z) = (z_1, \dots, z_r)$, and

(3) $f$ is normalized by $(f_{1},\dots ,f_{i})$ with respect to $(\mathbf{S};z_1,\dots ,z_r)$.

Let $\mathbf{P}$ be a prime ideal in $\mathbf{R}$ such that

(4) $\mathbf{P}$ is a permissible center for $\mathbf{J}$,

(5) $\mathbf{P} \cong (z_1, \cdots, z_r)\mathbf{R}$, and

(6) $\nu_{\mathbf{P}}(f_j) = \nu^{(j)}(\mathbf{J})$ for $1 \leq j \leq i$ and $\nu_{\mathbf{P}}(f) = \nu^{(i+1)}(\mathbf{J})$.

Let $\mathbf{R}_1$ be a monoidal transform of $\mathbf{R}$ with center $\mathbf{P}$ which is residually separable algebraic over $\mathbf{R}$, and $\mathbf{J}_1$ the strict transform of $\mathbf{J}$ in $\mathbf{R}_1$. Suppose we have an element $x \in \mathbf{P} \cap \mathbf{S}$ such that

(7)  $\mathbf{P}\mathbf{R}_{1} = (x)\mathbf{R}_{1}$  and  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  admits a frame transform  $(\mathbf{S}_{1}; w_{1}, \cdots, w_{r})$  in  $R_{1}$  with denominator x ( $w_{j} = z_{j}/x$  for  $1 \leq j \leq r$ ),

(8)  $\tau_{(w)}(g_{j})=0$  for  $1\leq j\leq i$  where  $g_{j}=x^{-\nu_{j}}f_{j}$  with  $\nu_{j}=\nu^{(j)}(\mathbf{J})$  and  $(w)=(w_{1},\cdots,w_{r})$ , and

(9) $\nu_{\mathbf{M}_1}(g_j) = \nu^{(j)}(\mathbf{J})$ for $1 \leq j \leq i$, where $\mathbf{M}_1$ denotes the maximal ideal of $\mathbf{R}_1$.

Let $g = x^{-\nu_{i+1}}f$ with $\nu_{i+1} = \nu^{(i+1)}(\mathbf{J})$. Then we have that

(a) $g$ is normalized by $(g_{1},\dots ,g_{i})$ with respect to $(\mathbf{S}_1;w_1,\dots ,w_r)$.

If we assume, in addition, that

(10) $\nu^{(j)}(\mathbf{J}_1) = \nu^{(j)}(\mathbf{J})$ for $1 \leq j \leq i + 1$, then we have that

(b)  $(g_{1}, \cdots, g_{i}, g)$  can be extended to a standard base of  $J_{1}$ .

PROOF. Let  $S \rightarrow \widetilde{S}$  be any local homomorphism such that a regular system of parameters of S is transformed into such a system of parameters of  $\widetilde{S}$  and that the residue field of  $\widetilde{S}$  is separable algebraic over that of  $\widetilde{S}$ . Then  $S \rightarrow \widetilde{S}$  induces in a canonical manner a local homomorphism  $R \rightarrow \widetilde{S}\{z_{1}, \cdots, z_{r}\}$  which also has the same properties as  $S \rightarrow \widetilde{S}$ . If we replace S by  $\widetilde{S}$ , R by  $\widetilde{R} = \widetilde{S}\{z_{1}, \cdots, z_{r}\}$ , and P and J by their extensions in  $\widetilde{R}$ , and  $R_{1}$  by a monoidal transform  $\widetilde{R}_{1}$  of  $\widetilde{R}$  with center  $PR$  which admits a canonical local homomorphism  $R_{1} \rightarrow \widetilde{R}_{1}$ , all the assumptions (1)–(10) remain valid, and the conclusions (a) and (b) are replaced by equivalent ones. Therefore we may assume that R and S are complete and that

$R_{1}$ is residually rational over R. Let M be the maximal ideal of R and $k = R/M$. Let $(Z) = (Z_{1}, \cdots, Z_{r})$ be the system of initial forms of $(z_{1}, \cdots, z_{r})$ in $gr_{M}(R)$. Let $\varphi_{j}$ be the initial form of $f_{j}$ in $gr_{M}(R)$, which by (2) belongs to the k-subalgebra $k[Z]$ of $gr_{M}(R)$ for $1 \leq j \leq i$. Let $I = (\varphi_{1}, \cdots, \varphi_{i})k[Z]$, and E the E-set of I with respect to $(k; Z_{1}, \cdots, Z_{r})$. By (3), in the power series expansion

$$
f = \sum_ {A \in \mathbf {Z} _ {0} ^ {r}} c _ {A} z ^ {A}
$$

with $c_{A}\in \mathbf{S}$

we have $c_A = 0$ for all $A \in E$. Then we have

$$
g = \sum_ {A \in \mathbf {Z} _ {0} ^ {r}} d _ {A} w ^ {A}
$$

with  $d_{A}=c_{A}x^{|A|-\nu_{i+1}}\in S_{1}$ . Hence  $d_{A}=0$  for all  $A\in E$ . Hence, to prove (a), we have only to show that, if  $\psi_{j}$  is the initial form of  $g_{j}$  in  $\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$  where  $M_{1}$  denotes the maximal ideal of  $R_{1}$  and if  $\mathbf{I}'=(\psi_{1},\cdots,\psi_{i})\mathbf{k}[W]$ , then E is also the E-set of  $I'$  with respect to  $(\mathbf{k},W_{1},\cdots,W_{r})$ , where  $(W_{1},\cdots,W_{r})$  is the system of initial forms of  $(w_{1},\cdots,w_{r})$  in  $\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ . We have assumed that  $R_{1}$  is residually rational over R, hence,  $S_{1}$  is so over S. Hence we can find a minimal base  $(x,x_{1},\cdots,x_{t})$  of  $P\cap S$  such that  $x_{j}/x$  is a non-unit of  $S_{1}$  for  $1\leq j\leq t$ . Then we can extend  $(x,x_{1},\cdots,x_{t})$  to a regular system of parameters  $(x,x_{1},\cdots,x_{t},y_{1},\cdots,y_{s})$  of S, so that  $(z_{1},\cdots,z_{r},x,x_{1},\cdots,x_{t},y_{1},\cdots,y_{s})$  is a regular system of parameters of R and that

$$
(w _ {1}, \dots , w _ {r}, x, u _ {1}, \dots , u _ {t}, y _ {1}, \dots , y _ {s})
$$

is a regular system of parameters of  $R_{1}$ , where  $u_{j} = x_{j}/x$  for  $1 \leq j \leq t$ . (See (7).) Let  $Z_{j}$  (resp. X, resp.  $X_{j}$ , resp.  $Y_{j}$ ) be the initial form of  $z_{j}$  (resp. x, resp.  $x_{j}$ , resp.  $y_{j}$ ) in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ . Then

$$
\operatorname{gr} _ {\mathbf {M}} (\mathbf {R}) = \mathbf {k} \left[ Z _ {1}, \dots , Z _ {r}, X, X _ {1}, \dots , X _ {t}, Y _ {1}, \dots , Y _ {s} \right].
$$

Let $W_{j}$ (resp. $X$, resp. $U_{j}$, resp. $Y_{j}$) be the initial form of $w_{j}$ (resp. $x$, resp. $u_{j}$, resp. $y_{j}$) in $\mathrm{gr}_{\mathbf{M}_1}(\mathbf{R}_1)$. Then

$$
\operatorname{gr} _ {\mathbf {M} _ {1}} \left(\mathbf {R} _ {1}\right) = \mathbf {k} \left[ W _ {1}, \dots , W _ {r}, X, U _ {1}, \dots , U _ {t}, Y _ {1}, \dots , Y _ {s} \right].
$$

By (9), we have

$$
\psi_ {j} = \varphi_ {j} (W _ {1}, \dots , W _ {r}) + \lambda_ {j}
$$

$$
\text { for   } 1 \leq j \leq i
$$

where  $\lambda_{j}\in(X,Y_{1},\cdots,Y_{s})\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ . (See the proof of Lemma 14 of §5.) Therefore the assumption (8) implies that

$$
\psi_ {j} = \varphi_ {j} (W _ {1}, \dots , W _ {r})
$$

$$
\text { for   } 1 \leq j \leq i.
$$

This is enough for that we have the same E-set of I with respect to  $(\mathbf{k}; Z_{1}, \cdots, Z_{r})$  as that of  $I'$  with respect to  $(\mathbf{k}; W_{1}, \cdots, W_{r})$ . Hence (a)

is proved. Now, in view of the first assertion of Lemma 18 of §7 (for the case in which $\mathbf{P} =$ the maximal ideal $\mathbf{M}_1$ of $\mathbf{R}_1$), (a) and (10) imply $\nu_{\mathbf{M}_1}(g)\geq \nu_{i + 1}$. But, since $\nu_{\mathbf{M}}(f) = \nu_{i + 1}$, this implies $\nu_{\mathbf{M}_1}(g) = \nu_{i + 1}$. (See Lemma 8 of §3.) Then (b) follows by the second assertion of Lemma 18 of §7. q.e.d.

LEMMA 21. Let the notation and assumptions be as in Lemma 20 (up to the assumption (10)). Let $a$ be the integer such that $\mu^{(a)}(\mathbf{J}) = \nu^{(i+1)}(\mathbf{J})$ and assume, in addition, that

(11) $\tau(f_1, \cdots, f_i) = r$, and

(12) $\tau^{(a)}(\mathbf{J}_1) = \tau^{(a)}(\mathbf{J})$.

Then we conclude

(c) $\tau_{(z)}(f) = \tau_{(w)}(g)$.

PROOF. As in the proof of Lemma 20, we may assume that S and R are complete, and that  $R_{1}$  is residually rational over R. Let M (resp.  $M_{1}$ ) be the maximal ideal of R (resp.  $R_{1}$ ) and  $k = R/M = R_{1}/M_{1}$ . We choose a regular system of parameters of R, say

$$
\left(z _ {1}, \dots , z _ {r}, x, x _ {1}, \dots , x _ {t}, y _ {1}, \dots , y _ {s}\right),
$$

such that  $\mathbf{P} \cap \mathbf{S} = (x, x_{1}, \cdots, x_{t})\mathbf{S}$ , that  $y_{j} \in S$  for  $1 \leq j \leq s$ , and that  $u_{j} = x_{j}/x \in M_{1}$  for  $1 \leq j \leq t$ . Then

$$
(w _ {1}, \dots , w _ {r}, x, u _ {1}, \dots , u _ {t}, y _ {1}, \dots , y _ {s})
$$

is a regular system of parameters of $\mathbf{R}_1$. Let $Z_j$ (resp. $X$, resp. $X_j$, resp. $Y_j$) denote the initial form of $z_j$ (resp. $x$, resp. $x_j$, resp. $y_j$) in $\mathrm{gr}_{\mathbb{M}}(\mathbf{R})$, so that we have

$$
\operatorname{gr} _ {\mathbf {M}} (\mathbf {R}) = \mathbf {k} \left[ Z _ {1}, \dots , Z _ {r}, X _ {1}, \dots , X _ {t}, X, Y _ {1}, \dots , Y _ {s} \right].
$$

Let $W_{j}$ (resp. $X$, resp. $U_{j}$, resp. $Y_{j}$) be the initial form of $w_{j}$ (resp. $x$, resp. $u_{j}$, resp. $y_{j}$) in $\mathrm{gr}_{\mathbf{M}_1}(\mathbf{R}_1)$, so that we have

$$
\operatorname{gr} _ {\mathbf {M} _ {1}} \left(\mathbf {R} _ {1}\right) = \mathbf {k} \left[ W _ {1}, \dots , W _ {r}, U _ {1}, \dots , U _ {t}, X, Y _ {1}, \dots , Y _ {s} \right].
$$

Let $\mathbf{T}_a$ denote the k-submodule of $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$ which is generated by the initial forms of a regular system of $a^{\text{th}}\tau$-parameters of $\mathbf{R}$ for $\mathbf{J}$. $\mathbf{T}_a$ must contain $Z_1, \cdots, Z_r$, by (1), (2) and (11). We claim that $\mathbf{T}_a$ is contained in the k-submodule of $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$ generated by $Z_1, \cdots, Z_r, X_1, \cdots, X_t$. To prove this, let $p$ be the maximal integer such that $\nu^{(i+p)}(\mathbf{J}) = \mu^{(a)}(\mathbf{J})$. By means of Lemma 17 of § 7, we can choose elements $f_{i+j}(1 \leq j \leq p)$ of $\mathbf{J}$ such that each of the $f_{i+j}(1 \leq j \leq p)$ is normalized by $(f_1, \cdots, f_i)$ with respect to $(\mathbf{S}; z_1, \cdots, z_r)$ and that $(f_1, \cdots, f_i, f_{i+1}, \cdots, f_{i+p})$ can be extended to a standard base of $\mathbf{J}$. Note that any permutation of the $p$ elements $f_{i+1}, \cdots, f_{i+p}$ preserves these properties. By Lemma 18 of § 7, we have $\nu_{\mathbf{P}}(f_{i+j}) = \mu^{(a)}(\mathbf{J})$ for $1 \leq j \leq p$. Let $\bar{\mu} = \mu^{(a)}(\mathbf{J}) = \nu^{(i+j)}(\mathbf{J})(1 \leq j \leq p)$.

By Lemma 20, we have $\nu_{\mathbf{M}_1}(x^{-\overline{\mu}}f_{i+j}) = \overline{\mu}$ for $1 \leq j \leq p$. This shows that the initial forms of $f_{i+j}$ ($1 \leq j \leq p$) are contained in $\mathbf{k}[Z_1, \cdots, Z_r, X_1, \cdots, X_t]$. In view of (2), it follows that $\mathbf{T}_a$ is contained in the k-module generated by $Z_1, \cdots, Z_r, X_1, \cdots, X_t$. Now that we have this result, we could choose the system $(x_1, \cdots, x_t)$ in such a way that for the integer $\tau = \tau^{(a)}(\mathbf{J}) - r$ ($0 \leq \tau \leq t$), $\mathbf{T}_a$ is generated by $Z_1, \cdots, Z_r, X_1, \cdots, X_\tau$. Let $\varphi$ (resp. $\varphi_j$ for $1 \leq j \leq i$) be the initial form of $f$ (resp. $f_j$) in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$. We have $\varphi_j$ ($1 \leq j \leq i$) $\in \mathbf{k}[Z_1, \cdots, Z_r]$ and, by Lemma 19 of §7, $\varphi \in \mathbf{k}[Z_1, \cdots, Z_r, X_1, \cdots, X_\tau]$. Let $\overline{\tau} = \tau_{(z)}(f)$. We have $0 \leq \overline{\tau} \leq \tau$. We may assume that $\varphi \in \mathbf{k}[Z_1, \cdots, Z_r, X_1, \cdots, X_\overline{\tau}]$. Let $\psi$ (resp. $\psi_j$ for $1 \leq j \leq i$) be the initial form of $g$ (resp. $g_j$) in $\mathrm{gr}_{\mathbf{M}_1}(\mathbf{R}_1)$. Then, by (8) and (9), we have

$$
\psi_ {j} = \varphi_ {j} (W _ {1}, \dots , W _ {r})
$$

$$
\text { for } 1 \leq j \leq i
$$

and, by (10) and (b),

$$
\psi = \varphi (W _ {1}, \dots , W _ {r}, U _ {1}, \dots , U _ {\tau} ^ {-}) + \lambda ,
$$

where  $\lambda\in(X,Y_{1},\cdots,Y_{s})\operatorname{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ . Let  $T_{a}^{*}$  be the k-submodule of  $\operatorname{gr}_{\mathbf{M}_{1}}^{\mathrm{i}}(\mathbf{R}_{1})$  generated by the initial forms of a regular system of  $a^{th}\tau$ -parameters of  $R_{1}$  for  $J_{1}$ . We claim that  $T_{a}^{*}$  contains  $W_{1},\cdots,W_{r}$ , and that there exists a system of linear forms in  $X,Y_{1},\cdots,Y_{s}$ , say  $(L_{1},\cdots,L_{\bar{\tau}})$ , such that  $T_{a}^{*}$  is generated by  $\{W_{1},\cdots,W_{r},U_{1}+L_{1},\cdots,U_{\bar{\tau}}+L_{\bar{\tau}}\}$ . In fact, in view of the equalities  $\psi_{j}=\varphi_{j}(W_{1},\cdots,W_{r})$  for  $1\leq j\leq i$ , (11) implies that  $\tau(g_{1},\cdots,g_{i})=r$ . Hence, by (8) and (b), the first assertion on  $T_{a}^{*}$  follows. To prove the second, we take  $f_{i+j}$  and  $g_{i+j}=x^{-\overline{\mu}}f_{i+j}(1\leq j\leq p)$  in the same way as above. Let  $\varphi_{i+j}$  (resp.  $\psi_{i+j}$ ) be the initial form of  $f_{i+j}$  (resp.  $g_{i+j}$ ) in  $\operatorname{gr}_{\mathbf{M}}(\mathbf{R})$  (resp.  $\operatorname{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ ). Then we have

$$
\psi_ {i + j} = \varphi_ {i + j} \left(W _ {1}, \dots , W _ {r}, U _ {1}, \dots , U _ {\bar {\tau}}\right) + \lambda_ {j},
$$

with  $\lambda_{j}\in(X,Y_{1},\cdots,Y_{s})\operatorname{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ . By Lemma 20,  $g_{i+j}$  is normalized by  $(g_{1},\cdots,g_{i})$  with respect to  $(\mathbf{S}_{1};w_{1},\cdots,w_{r})$  for  $1\leq j\leq p$ . Hence, by Lemma 19 of §7, we must have

$$
\psi_ {i + j} \in \mathbf {k} [ \mathbf {T} _ {a} ^ {*} ]
$$

$$
\text { for   } 1 \leq j \leq p.
$$

In view of the above expression of  $\psi_{i+j}$  in terms of  $\varphi_{i+j}$, the homomorphism  $\mathbf{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})\to\mathbf{k}[Z_{1},\cdots,Z_{r},X_{1},\cdots,X_{t}]$  which maps  $W_{j}$  to  $Z_{j}(1\leq j\leq r)$,  $U_{j}$  to  $X_{j}(1\leq j\leq t)$,  $X\to0$  and  $Y_{j}\to0(1\leq j\leq s)$, should induce a surjective homomorphism  $T_{a}^{*}\to T_{a}$. But  $T_{a}^{*}$  has the same rank as  $T_{a}$  by (12). This homomorphism  $T_{a}^{*}\to T_{a}$  is an isomorphism of k-modules. The existence of  $(L_{1},\cdots,L_{\tau^{-}})$  follows. Now, by Lemma 19 of §7, we have

$$
\psi \in \mathbf {k} [ \mathbf {T} _ {a} ^ {*} ] = \mathbf {k} [ W _ {1}, \dots , W _ {r}, U _ {1} + L _ {1}, \dots , U _ {\overline {{\tau}}} + L _ {\overline {{\tau}}} ].
$$

On the other hand,

$$
\begin{array}{r l} \psi - \varphi (W _ {1}, \dots , W _ {r}, U _ {1} + L _ {1}, \dots , U _ {\bar {\tau}} + L _ {\bar {\tau}}) \\ = \varphi (W _ {1}, \dots , W _ {r}, U _ {1}, \dots , U _ {\bar {\tau}}) + \lambda \\ & - \varphi (W _ {1}, \dots , W _ {r}, U _ {1} + L _ {1}, \dots , U _ {\bar {\tau}} + L _ {\bar {\tau}}) \\ & \in (X, Y _ {1}, \dots , Y _ {s}) \mathbf {g r} _ {\mathbf {M} _ {1}} (\mathbf {R} _ {1}). \end{array}
$$

It is, however, clear that zero is the only element in the intersection of the algebra  $k[W_{1},\cdots,W_{r},U_{1}+L_{1},\cdots,U_{\bar{\tau}}+L_{\bar{\tau}}]$ , and of the ideal  $(X,Y_{1},\cdots,Y_{s})\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ . Therefore we must have

$$
\psi = \varphi (W _ {1}, \dots , W _ {r}, U _ {1} + L _ {1}, \dots , U _ {\bar {\tau}} + L _ {\bar {\tau}}).
$$

This shows that $\tau_{(w)}(g) = \tau_{(z)}(f) = \overline{\tau}$, i.e., (c). q.e.d.

PROPOSITION 2. Let R be a regular local ring which has the same characteristic as its residue field. Let J be an ideal in R and P, Q prime ideals in R such that

(i) $\mathbf{Q} \supset \mathbf{P} \supseteq \mathbf{J}$ and $\mathbf{Q} \neq \mathbf{P}$,

(ii) $\mathbf{R} / \mathbf{P}$ is regular, and

(iii) $\mathbf{Q}$ is a permissible center for $\mathbf{J}$.

Let $\mathbf{R}_1$ be a monoidal transform of $\mathbf{R}$ with center $\mathbf{Q}$ which is residually separable algebraic over $\mathbf{R}$, and $\mathbf{J}_1$ the strict transform of $\mathbf{J}$ in $\mathbf{R}_1$. Suppose we have a prime ideal $\mathbf{P}_1$ in $\mathbf{R}_1$ such that $\mathbf{P}_1 \cap \mathbf{R} = \mathbf{P}$. If $\nu^*(\mathbf{J}_1) = \nu^*(\mathbf{J})$ and $\mathbf{P}_1$ is a permissible center for $\mathbf{J}_1$, then $\mathbf{P}$ is a permissible center for $\mathbf{J}$.

PROOF. We may assume that $\mathbf{R}$ is complete, and that $\mathbf{R}_1$ is residually rational over $\mathbf{R}$. Then $\mathbf{R}$ is a formal power series ring over a field, by Cohen's structure theorem. Since $\nu^{*}(\mathbf{J}_{1}) = \nu^{*}(\mathbf{J})$, there can be found a regular $\tau$-frame ($\mathbf{S}; z_{1}, \cdots, z_{r}$) of $\mathbf{R}$ for $\mathbf{J}$, which admits a frame transform ($\mathbf{S}_{1}; z_{1}/x, \cdots, z_{r}/x$) in the monoidal transform $\mathbf{R}_{1}$ with denominator $x \in \mathbf{S}$. In fact, let us choose a minimal base ($x, z_{1}, \cdots, z_{t}$) of $\mathbf{Q}$, where $t = \dim (\mathbf{R}_{\mathbf{Q}}) - 1$, such that $(x)\mathbf{R}_{1} = \mathbf{QR}_{1}$ and all the $z_{i}/x$ ($1 \leq i \leq t$) are contained in the maximal ideal of $\mathbf{R}_{1}$. Let $(y_{1}, \cdots, y_{s})$ be a system of elements of $\mathbf{R}$ such that $(x, z_{1}, \cdots, z_{t}, y_{1}, \cdots, y_{s})$ is a regular system of parameters of $\mathbf{R}$. We have a subfield $\mathbf{k}$ of $\mathbf{R}$ such that $\mathbf{R} = \mathbf{k}\{x, z_{1}, \cdots, z_{t}, y_{1}, \cdots, y_{s}\}$. By Lemma 14, §5, we have a standard base $(h_{1}, \cdots, h_{m})$ of $\mathbf{J}$ such that, if $\nu_{j} = \nu_{\mathbf{M}}(h_{j}) = \nu^{(j)}(\mathbf{J})$, then $\nu_{\mathbf{Q}}(h_{j}) = \nu_{j}$ and $\nu_{\mathbf{M}_{1}}(x^{-\nu_{j}}h_{j}) = \nu_{j}$ for all $j (1 \leq j \leq m)$, where $\mathbf{M}(\text{resp. } \mathbf{M}_{1})$ denotes the maximal ideal of $\mathbf{R} (\text{resp. } \mathbf{R}_{1})$. Therefore, the initial forms of the $h_{j}$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ must belong to the $(\mathbf{R}/\mathbf{M})$-subalgebra of $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ generated by the initial forms of the $z_{i}$ ($1 \leq i \leq t$). It is then easily seen that, by applying a suitable k-linear transformation to the system $(z_{1}, \cdots, z_{t})$, we can assume $(z_{1}, \cdots, z_{r})$ ($r \leq t$) to be a regu-

lar system of $\tau$-parameters of $\mathbf{R}$ for $\mathbf{J}$. Let $\mathbf{S} = \mathbf{k}\{z_{r+1}, \cdots, z_t, x, y_1, \cdots, y_s\}$. Then $(\mathbf{S}; z_1, \cdots, z_r)$ is a regular $\tau$-frame of $\mathbf{R}$ for $\mathbf{J}$ having the required property as above. Moreover, by Proposition 1, §5, we have $\tau^*(\mathbf{J}_1) = \tau^*(\mathbf{J})$, and therefore we can choose the above $(z_1, \cdots, z_r)$ in such a way that the transform $(\mathbf{S}_1; z_1/x, \cdots, z_r/x)$ is a regular $\tau$-frame of $\mathbf{R}_1$ for $\mathbf{J}_1$. (See the proof of Lemma 16, §5.) By the assumption that $\mathbf{P}_1$ is a permissible center for $\mathbf{J}_1$, we can choose it in such a way that $z_j/x \in \mathbf{P}_1$ for all $j$ ($1 \leq j \leq r$). (See Lemma 11, §4.) Now, let $(f_1, \cdots, f_m)$ be a normalized standard base of $\mathbf{J}$ with respect to $(\mathbf{S}; z_1, \cdots, z_r)$. (For the existence, see Lemmas 17 and 19 of §7.) Let $g_j = x^{-\nu_j} f_j$ with $\nu_j = \nu^{(j)}(\mathbf{J})$ for $1 \leq j \leq m$. Then, in view of Lemmas 20 and 21, we see that $(g_1, \cdots, g_m)$ is again a normalized standard base of $\mathbf{J}_1$ with respect to $(\mathbf{S}_1; z_1/x, \cdots, z_r/x)$. By Theorem 6, §7, we conclude that $\nu_{\mathrm{P}_1}(g_j) = \nu_j$ for all $j$ ($1 \leq j \leq m$). However, $x$ is a unit in $\mathbf{R}_{\mathrm{P}} = (\mathbf{R}_1)_{\mathrm{P}_1}$, and therefore $\nu_{\mathrm{PR}_{\mathrm{P}}} (f_j) = \nu_j$ for all $j$ ($1 \leq j \leq m$) which implies $\nu_{\mathrm{P}}(f_j) = \nu_j$ for all $j$ ($1 \leq j \leq m$) by the assumption (ii). It follows that $\mathbf{P}$ is a permissible center for $\mathbf{J}$. q.e.d.

COROLLARY 1. Let R be a regular local ring whose residue field is a perfect field of the same characteristic as that of R. Let J be an ideal in R, and P, Q prime ideals in R such that

(i) $\mathbf{Q} \supset \mathbf{P} \supseteq \mathbf{J}$ and $\mathbf{Q} \neq \mathbf{P}$, and

(ii) both $\mathbf{R} / \mathbf{P}$ and $\mathbf{R} / \mathbf{Q}$ are regular.

Let $(f_{1},\cdots,f_{m})$ be a system of elements of J such that, M denoting the maximal ideal in R,

(iii) $\nu_{\mathbf{M}}(f_j) = \nu_{\mathbf{Q}}(f_j)$ for all $j$ ($1 \leq j \leq m$), and

(iv) the initial forms of  $f_{j}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  generate the ideal  $\mathrm{gr}_{\mathbf{M}}(\mathbf{J}, \mathbf{R})$ . Let  $R_{1}$  be any monoidal transform of R with center Q,  $M_{1}$  the maximal ideal of  $R_{1}$ , and  $J_{1}$  the strict transform of J in  $R_{1}$ , such that

(v) there exists a prime ideal $\mathbf{P}_1$ in $\mathbf{R}_1$ with $\mathbf{P}_1 \cap \mathbf{R} = \mathbf{P}$, and

(vi) $\nu_{\mathbf{M}_1}(f_j x^{-\nu_j}) = \nu_j$ where $\nu_j = \nu_{\mathbf{Q}}(f_j)$ ($1 \leq j \leq m$) and $x$ is an element of $\mathbf{Q}$ such that $(x)\mathbf{R}_1 = \mathbf{QR}_1$.

If $\mathbf{P}_1$ is a permissible center for $\mathbf{J}_1$, then $\mathbf{P}$ is a permissible center for $\mathbf{J}$.

$^{11}$  S is complete and R is the formal power series ring  $S\{z_{1},\cdots,z_{r}\}$ . Let  $(f_{1},\cdots,f_{i})$  be a system of elements of J which can be extended to a standard base of J and which is normalized with respect to  $(\mathbf{S};z_{1},\cdots,z_{r})$ . (cf. Definition 9 (3).) Take g to be any element of J such that  $(f_{1},\cdots,f_{r},g)$  can be extended to a standard base of J. Then, by Lemma 17, we can find a system of elements of R, say  $(h_{1},\cdots,h_{i})$ , such that  $\nu_{\mathbf{M}}(h_{p})\geq\nu_{i+1}-\nu_{p}(1\leq p\leq i)$  and that  $g-\sum_{p}h_{p}f_{p}$  (call it  $f_{i+1}$ ) is normalized by  $(f_{1},\cdots,f_{i})$  with respect to  $(\mathbf{S};z_{1},\cdots,z_{r})$ . Since  $(\mathbf{S};z_{1},\cdots,z_{r})$  is a regular  $\tau$ -frame of R for J, Lemma 19 implies that  $(f_{1},\cdots,f_{i},f_{i+1})$  is normalized with respect to  $(\mathbf{S};z_{1},\cdots,z_{r})$ . It is clear from the above properties of the  $h_{p}$  that  $(f_{1},\cdots,f_{i},f_{i+1})$  can be extended to a standard base of J. We can thus prove the existence of a normalized standard base of J with respect to any regular  $\tau$ -frame of R for J, when R is complete.

PROOF. We first remark that Q is a permissible center for J by (ii), (iii) and (iv). Let us choose an element x of Q in such a way as in (vi). We then take a minimal base  $(x, x_{1}, \cdots, x_{r})$  of the prime ideal Q. Let  $A = R[x_{1}/x, \cdots, x_{r}/x]$ . Then there exists a prime ideal N in A such that  $R_{1} = A_{N}$ . We have  $N \cap R = M$ , and therefore  $\bar{A} = A/N$  is an algebra of finite type over the residue field of R. We then know that the singular locus of  $\operatorname{Spec}(\bar{A})$  is a nowhere dense closed subset. $^{12}$  Therefore we can find a maximal ideal  $N'$  in A such that  $N'$  contains N and that  $A_{N'} / NA_{N'}$  is regular. Let  $R_{1}' = A_{N'}$ . Then  $R_{1}'$  is a monoidal transform of R with center Q such that  $R_{1}'$  is residually algebraic (hence, separable algebraic) over R, and that there exists a prime ideal H in  $R_{1}'$  such that  $\mathbf{R}_{1} = (\mathbf{R}_{1}')_{\mathbf{H}}$ . Moreover, we have that  $R_{1}' / H$  is regular. Let  $J_{1}'$  be the strict transform of J in  $R_{1}'$ . We have  $(x)R_{1}' = QR_{1}'$  and hence, if  $g_{j} = f_{j}x^{-\nu_{j}} (1 \leq j \leq m)$ , these  $g_{j}$  are elements of  $J_{1}'$ . The assumption (vi) is equivalent to saying that  $\nu_{\mathrm{H}}(g_{j}) = \nu_{j}$  for all j. It follows, by Theorem 5, §6, that  $\nu^{*}(\mathbf{J}) = \nu^{*}(\mathbf{J}_{1}')$ , that a suitable subsystem (suitably reordered) of  $(g_{1}, \cdots, g_{m})$  is a standard base of  $J_{1}'$ , and that H is a permissible center for  $J_{1}'$ . We have  $\mathbf{R}_{1} = (\mathbf{R}_{1}')_{\mathbf{H}}$ ,  $J_{1} = (\mathbf{J}_{1}')R_{1}$  and  $P_{1} = (P_{1})R_{1}$  with  $P_{1} = P_{1} \cap R_{1}'$ . Therefore, by Theorem 3, §3, Ch. II, if  $P_{1}$  is a permissible center for  $J_{1}$ , then  $P_{1}'$  is a permissible center for  $J_{1}'$ . (It should be noted that the regularity of  $R_{1}' / P_{1}'$  is clear because it is a monoidal transform of R/P with center Q/P.) This implies, by Proposition 2, that P is a permissible center for J. q.e.d.

COROLLARY 2. Let R be a regular local ring and M the maximal ideal in R. Let us assume that the residue field R/M has characteristic zero. Let Q be a prime ideal in R, and J an ideal in R such that  $Q \supseteq J$ . Suppose we have a system of elements  $(g_{1}, \cdots, g_{m})$  of J such that

(i) the initial forms of $g_{j}$ ($1 \leq j \leq m$) in $\mathbf{gr}_{\mathbf{M}}(\mathbf{R})$ generate the ideal $\mathbf{gr}_{\mathbf{M}}(\mathbf{J}, \mathbf{R})$, and

(ii) $\nu_{\mathbf{M}}(g_j) = \nu_{\mathrm{QR}_0}(g_j)$ for all $j$ ($1 \leq j \leq m$).

Let $\mathbf{P}$ be a prime ideal in $\mathbf{R}$ such that $\mathbf{Q} \supseteq \mathbf{P} \supseteq \mathbf{J}$ and that $\mathbf{R} / \mathbf{P}$ is regular. If $\mathrm{gr}_{\mathrm{PR}_0}(\mathbf{R}_Q / \mathbf{JR}_Q)$ is flat over $\mathbf{R}_Q / \mathbf{PR}_Q$, then $\mathrm{gr}_{\mathrm{P}}(\mathbf{R} / \mathbf{J})$ is flat over $\mathbf{R} / \mathbf{P}$.

PROOF. Let $\hat{\mathbf{R}}$ be the completion of $\mathbf{R}$, and $\hat{\mathbf{P}} = \mathbf{P}\hat{\mathbf{R}}$. We see that $\hat{\mathbf{P}}$ is a prime ideal in $\hat{\mathbf{R}}$ such that $\hat{\mathbf{R}} / \hat{\mathbf{P}}$ is regular. Let $\hat{\mathbf{Q}}$ be a minimal prime ideal associated with $\mathbf{Q}\hat{\mathbf{R}}$, i.e., $\hat{\mathbf{Q}} \cap \mathbf{R} = \mathbf{Q}$ and $\mathbf{Q}\hat{\mathbf{R}}_{\hat{\mathbf{Q}}}$ is primary to the maximal ideal. We have $\nu_{\hat{\mathbf{Q}}\hat{\mathbf{R}}_{\hat{\mathbf{Q}}}}(g_j) \geq \nu_{\mathbf{Q}\mathbf{R}_{\mathbf{Q}}}(g_j)$, and $\nu_{\hat{\mathbf{M}}}(g_j) = \nu_{\mathbf{M}}(g_j)$ where $\hat{\mathbf{M}} = \mathbf{M}\hat{\mathbf{R}}$ which is the maximal ideal of $\hat{\mathbf{R}}$. Therefore, by Theorem 1, §3, (ii) implies that $\nu_{\hat{\mathbf{M}}}(g_j) = \nu_{\hat{\mathbf{Q}}\hat{\mathbf{R}}_{\hat{\mathbf{Q}}}}(g_j)$ for all $j$. Moreover, it is clear that (i) implies that the initial forms of $g_j$ ($1 \leq j \leq m$) in $\mathrm{gr}_{\hat{\mathbf{M}}}(\hat{\mathbf{R}})$ generate the ideal

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{12}$  cf. Zariski [29].</span></small>

\( \mathrm{gr}\_{\hat{\mathbf{M}}}(\hat{\mathbf{J}},\hat{\mathbf{R}}) \), where \( \hat{\mathbf{J}}=\mathbf{J}\hat{\mathbf{R}} \). (See Lemma 2, § 1.) We know that \( \hat{\mathbf{R}}\_{\hat{\mathbf{Q}}} \) is faithfully flat over \( \mathbf{R}\_{\mathbf{Q}} \). Hence, by Lemma 9, § 3, Ch. II, \( \mathrm{gr}\_{\mathrm{PR}\_{\mathbf{Q}}}(\mathbf{R}\_{\mathbf{Q}}/\mathbf{J}\mathbf{R}\_{\mathbf{Q}}) \) is flat over \( \mathbf{R}\_{\mathbf{Q}}/\mathbf{P}\mathbf{R}\_{\mathbf{Q}} \) if and only if \( \mathrm{gr}\_{\mathrm{PR}\_{\hat{\mathbf{Q}}}}(\hat{\mathbf{R}}\_{\hat{\mathbf{Q}}}/\mathbf{J}\hat{\mathbf{R}}\_{\hat{\mathbf{Q}}}) \) is flat over \( \hat{\mathbf{R}}\_{\hat{\mathbf{Q}}}/\mathbf{P}\hat{\mathbf{R}}\_{\hat{\mathbf{Q}}} \). Here we have \( \mathrm{P}\hat{\mathbf{R}}\_{\hat{\mathbf{Q}}}=\hat{\mathrm{P}}\hat{\mathrm{R}}\_{\hat{\mathbf{Q}}} \) and \( \mathrm{J}\hat{\mathrm{R}}\_{\hat{\mathbf{Q}}}=\hat{\mathrm{J}}\hat{\mathrm{R}}\_{\hat{\mathbf{Q}}} \). For the same reason, \( \mathrm{gr}\_{\mathrm{P}}(\mathbf{R}/\mathbf{J}) \) is flat over \( \mathbf{R}/\mathbf{P} \) if and only if \( \mathrm{gr}\_{\hat{\mathbf{P}}}(\hat{\mathbf{R}}/\hat{\mathbf{J}}) \) is flat over \( \hat{\mathbf{R}}/\hat{\mathbf{P}} \). We can assume that \( \dim(\hat{\mathbf{R}}/\hat{\mathbf{Q}})=\dim(\mathbf{R}/\mathbf{Q}) \). Now, the proof of Corollary 2 is done by induction on \( \dim(\mathbf{R}/\mathbf{Q}) \). Let us first consider the case of \( \dim(\mathbf{R}/\mathbf{Q})=1 \). By the above arguments, we may assume that \( \mathbf{R} \) is complete. Therefore, the integral closure of \( \mathbf{R}/\mathbf{Q} \) in its field of quotients is a finite \( \mathbf{R}/\mathbf{Q} \)-module. Let us take a monoidal transform \( \mathbf{R}\_{1} \) of \( \mathbf{R} \) with center \( \mathbf{M} \) which is residually algebraic over \( \mathbf{R} \) and such that there exists a prime ideal \( \mathbf{Q}\_{1} \) in \( \mathbf{R}\_{1} \) with \( \mathbf{Q}\_{1}\cap\mathbf{R}=\mathbf{Q} \). Let \( \mathbf{J}\_{1} \) be the strict transform of \( \mathbf{J} \) in \( \mathbf{R}\_{1} \). Let x be an element of \( \mathbf{M} \) such that \( (x)\mathbf{R}\_{1}=\mathbf{M}\mathbf{R}\_{1} \), and \( g\_{j}^{\prime}=g\_{j}x^{-\nu\_{j}} \) for each j, where \( \nu\_{j}=\nu\_{\mathrm{M}}(g\_{j}) \). Then, by Corollary 3 (b) of Theorem 5, § 6, the assumptions (i) and (ii) remain valid for \( \mathbf{R}\_{1},\mathbf{M}\_{1}(=\text {the maximal ideal of } \mathbf{R}\_{1}),\mathbf{Q}\_{1},\mathbf{J}\_{1} \), and the system \( (g\_{1}^{\prime},\cdots,g\_{m}^{\prime}) \). Moreover, if \( P\_{1} \) is the prime ideal in \( R\_{1} \) with \( P\_{1}\cap R=P \), then Proposition 2 shows that the flatness of \( \mathrm{gr}\_{\mathrm{P}}(\mathrm{R}/\mathrm{J}) \) over \( R/P \) follows the same of \( \mathrm{gr}\_{\mathrm{P}\_{1}}(\mathrm{R}\_{1}/\mathrm{J}\_{1}) \) over \( R\_{1}/P\_{1} \). (See Corollary 3 (b) of Theorem 5, § 6.) Furthermore, \( R\_{Q}=(R\_{1})\_{Q\_{1}},JR\_{Q}=J\_{1}(R\_{1})\_{Q\_{1}} \), and \( PR\_{Q}=P\_{1}(R\_{1})\_{Q\_{1}} \). Therefore, in order to prove the assertion of Corollary 2, we may replace \( R,J,Q, and P by R\_{1},J\_{1},Q\_{1}, and P\_{1} respectively. We know that the assertion is verified if \( R/Q \) is regular, by Theorem 3, § 3, Ch. II, combined with Corollary 1 of Theorem 2, § 2, Ch. II and therefore, it is also done if \( R\_{1}/Q\_{1}is regular. If R\_{1}/Q\_{1}is regular, we repeat the same process as above. As is easily seen, the process cannot be repeated infinitely many times. Let us consider the case of dim (\( R/Q)>1. We may again assume that R is complete. By the dimension assumption, we can find a prime ideal Q' in R such that Q' contains Q and dim (\( R/Q')=1. By Corollary 3 (c) of Theorem 5, § 6, the assumptions (i) and (ii) remain valid if we replace R,Q,J,and M by R\( \_{Q'} \),QR\( \_{Q'} \),JR\( \_{Q'} \), and Q'R\( \_{Q'} \), respectively. Therefore, by the induction assumption, the flatness of gr\( \_{\mathrm{PR}\_{Q}}(\mathrm{R}\_{Q}/\mathrm{JR}\_{Q}) \) over R\( \_{Q}/PR\_{Q} \) implies the same of gr\( \_{\mathrm{PR}\_{Q'}}(\mathrm{R}\_{Q'}/\mathrm{JR}\_{Q'}) \) over R\( \_{Q'}/PR\_{Q'}. By the above result for the 1-dimensional case, the flatness of gr\( \_{\mathrm{P}}(\mathrm{R}/\mathrm{J})\) over R/P follows. q.e.d.

## 9. The notion of J-stability with reference to a local ideal J

Let $\mathbf{R}$ be a regular local ring. By a sequence of monoidal transforms of $\mathbf{R}$, we shall mean a sequence (finite or infinite) of pairs, say $\{(\mathbf{R}_{\alpha}, \mathbf{P}_{\alpha-1})\}$ ($1 \leq \alpha < e$, where $e$ is either a positive integer or $\infty$), which has the following properties:

(1) If $\mathbf{R}_0$ denotes $\mathbf{R}$, $\mathbf{P}_{\alpha}$ is a non-zero ideal in $\mathbf{R}_{\alpha}$ such that either $\mathbf{P}_{\alpha} = \mathbf{R}_{\alpha}$ or $\mathbf{R}_{\alpha} / \mathbf{P}_{\alpha}$ is regular, for all $\alpha \geq 0$, and

(2) $\mathbf{R}_{\alpha}$ is a monoidal transform of $\mathbf{R}_{\alpha - 1}$ with center $\mathbf{P}_{\alpha - 1}$ for every $\alpha \geq 1$. Let $\mathbf{J}$ be an ideal in $\mathbf{R}$. By a sequence of strict monoidal transforms of $(\mathbf{J}, \mathbf{R})$, we shall mean a sequence of triples, say $\{(\mathbf{J}_{\alpha}, \mathbf{R}_{\alpha}, \mathbf{P}_{\alpha - 1})\} (1 \leq \alpha < e$, where $e$ is either a positive integer or $\infty$), such that $\{(\mathbf{R}_{\alpha}, \mathbf{P}_{\alpha - 1})\}$ is a sequence of monoidal transforms of $\mathbf{R}$ and that, if $\mathbf{J}_0$ denotes $\mathbf{J}$, $\mathbf{J}_{\alpha}$ is the strict transform of $\mathbf{J}_{\alpha - 1}$ in $\mathbf{R}_{\alpha}$ for every $\alpha \geq 1$. If $\{(\mathbf{J}_{\alpha}, \mathbf{R}_{\alpha}, \mathbf{P}_{\alpha - 1})\}$ is such, we shall say that, for each $\alpha \geq 1$, $\mathbf{J}_{\alpha}$ is the strict transform of $\mathbf{J}$ in $\mathbf{R}_{\alpha}$ along the sequence of monoidal transforms $\{(\mathbf{R}_{\alpha}, \mathbf{P}_{\alpha - 1})\}$ of $\mathbf{R}$. We shall say that a sequence of monoidal transforms $\{(\mathbf{R}_{\alpha}, \mathbf{P}_{\alpha - 1})\}$ of $\mathbf{R}$ is permissible for $\mathbf{J}$ if $\mathbf{P}_{\alpha - 1}$ is a permissible center for $\mathbf{J}_{\alpha - 1}$ for every $\alpha \geq 1$, where $\mathbf{J}_0 = \mathbf{J}$, and $\mathbf{J}_{\alpha}$ is the strict monoidal transform of $\mathbf{J}$ in $\mathbf{R}_{\alpha}$ along the sequence. If this is the case, we shall also say that the sequence of strict monoidal transforms $\{(\mathbf{J}_{\alpha}, \mathbf{R}_{\alpha}, \mathbf{P}_{\alpha - 1})\}$ of $(\mathbf{J}, \mathbf{R})$ is permissible. Let $f$ be a non-zero element of $\mathbf{R}$. If $\mathbf{J} = (f)\mathbf{R}$, and if $\{(\mathbf{J}_{\alpha}, \mathbf{R}_{\alpha}, \mathbf{P}_{\alpha - 1})\}$ is a sequence of strict monoidal transforms of $(\mathbf{J}, \mathbf{R})$, then $\mathbf{J}_{\alpha}$ is a principal ideal of $\mathbf{R}_{\alpha}$, for every $\alpha \geq 1$. A generator $f_{\alpha}$ of the principal ideal $\mathbf{J}_{\alpha}$ will be called a strict transform of the element $f$ in $\mathbf{R}_{\alpha}$ along the sequence of monoidal transforms $\{\mathbf{R}_{\alpha}, \mathbf{P}_{\alpha - 1}\}$ of $\mathbf{R}$. Note that $f_{\alpha}$ is unique only up to a unit multiple in $\mathbf{R}_{\alpha}$.

DEFINITION 11. Let $\mathbf{R}$ be a regular local ring, and $\mathbf{J}$ an ideal in $\mathbf{R}$. Let $f$ be an element of $\mathbf{R}$. Let $\mathbf{M}$ be the maximal ideal of $\mathbf{R}$ and $\nu = \nu_{\mathbf{M}}(f)$. We say that $f$ is $\mathbf{J}$-stable (or, stable with respect to $\mathbf{J}$) if the following condition is satisfied: Let $\{\mathbf{R}_{\alpha}, \mathbf{P}_{\alpha-1}\}$ be any permissible sequence (finite or infinite) of monoidal transforms of $\mathbf{R}$ for $\mathbf{J}$ such that $\mathbf{R}_{\alpha}$ is residually separable algebraic over $\mathbf{R}_{\alpha-1} (= \mathbf{R}\text{ if } \alpha = 1)$. Let $\mathbf{J}_{\alpha}$ be the strict transform of $\mathbf{J}$ in $\mathbf{R}_{\alpha}$ along the sequence, and $f_{\alpha}$ a strict transform of $f$ in $\mathbf{R}_{\alpha}$ along the sequence. Then, for every $\bar{\alpha} \geq 0$, such that $\nu^{*}(\mathbf{J}_{\bar{\alpha}}) = \nu^{*}(\mathbf{J})$ and that $\tau^{(a)}(\mathbf{J}_{\bar{\alpha}}) = \tau^{(a)}(\mathbf{J})$ for $1 \leq a \leq t(\mathbf{J}) = t(\mathbf{J}_{\bar{\alpha}})$ (where $\mathbf{J}_{\bar{\alpha}} = \mathbf{J}$ if $\bar{\alpha} = 0$), we have $\nu_{\mathrm{M}_{\bar{\alpha}}} (f_{\bar{\alpha}}) = \nu$ and $\nu_{\mathrm{P}_{\bar{\alpha}}} (f_{\bar{\alpha}}) = \nu$ (provided $\mathbf{P}_{\bar{\alpha}}$ exists and is different from $\mathbf{R}_{\bar{\alpha}}$), where $\mathbf{M}_{\bar{\alpha}}$ denotes the maximal ideal of $\mathbf{R}_{\bar{\alpha}}$ and $f_0 = f$.

A system of elements  $(f_{1}, \cdots, f_{m})$  of R is said to be J-stable (or, stable with respect to J) if  $f_{j}$  is so for all  $j (1 \leq j \leq m)$ . A regular frame  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  of R is said to be J-stable (or, stable with respect to J) if the system  $(z_{1}, \cdots, z_{r})$  is so.

REMARK 1. Let $\mathbf{R} \to \mathbf{R}'$ be a local homomorphism of regular local rings such that a regular system of parameters of $\mathbf{R}$ is transformed into such a system of parameters of $\mathbf{R}'$, and that the residue field of $\mathbf{R}'$ is separable over that of $\mathbf{R}$. Given a sequence $\{(\mathbf{R}_{\alpha}, \mathbf{P}_{\alpha-1})\}$ of monoidal transforms of

R, there exists always a sequence of monoidal transforms  $\{(\mathbf{R}_{\alpha}^{\prime}, \mathbf{P}_{\alpha-1}^{\prime})\}$  of  $R^{\prime}$  such that we have a commutative diagram of canonical local homomorphisms

![](images/page_59_image_1.jpg)

for all $\alpha$, where $\mathbf{R}_0 = \mathbf{R}$, $\mathbf{R}_0' = \mathbf{R}'$ and $\mathbf{P}_{\alpha - 1}' = \mathbf{P}_{\alpha - 1}\mathbf{R}'$. If $\mathbf{R}_{\alpha}$ is residually algebraic over $\mathbf{R}_{\alpha - 1}$, then $\mathbf{R}_{\alpha}'$ is so over $\mathbf{R}_{\alpha - 1}'$. Let us assume this. By Lemma 4, §2, $\mathbf{R}_{\alpha} \to \mathbf{R}_{\alpha}'$ has the same properties as $\mathbf{R} \to \mathbf{R}'$ for every $\alpha$. Let $\mathbf{J}$ be an ideal in $\mathbf{R}$ and $\mathbf{J}' = \mathbf{JR}$. Then $\{(\mathbf{R}_{\alpha}', \mathbf{P}_{\alpha - 1}')\}$ is permissible for $\mathbf{J}'$ if and only if $\{(\mathbf{R}_{\alpha}, \mathbf{P}_{\alpha - 1})\}$ is so for $\mathbf{J}$. Moreover, the strict transform $\mathbf{J}_{\alpha}'$ of $\mathbf{J}'$ in $\mathbf{R}_{\alpha}'$ along $\{(\mathbf{R}_{\alpha}', \mathbf{P}_{\alpha - 1}')\}$ is equal to $\mathbf{J}_{\alpha}\mathbf{R}_{\alpha}'$ where $\mathbf{J}_{\alpha}$ is the strict transform of $\mathbf{J}$ in $\mathbf{R}_{\alpha}$ along $\{(\mathbf{R}_{\alpha}, \mathbf{P}_{\alpha - 1})\}$, by Corollary to Lemma 5, §2, so that we have $\nu^{*}(\mathbf{J}_{\alpha}) = \nu^{*}(\mathbf{J})$ if and only if $\nu^{*}(\mathbf{J}_{\alpha}') = \nu^{*}(\mathbf{J}')$, and that $\tau^{(a)}(\mathbf{J}_{\alpha}) = \tau^{(a)}(\mathbf{J})$ if and only if $\tau^{(a)}(\mathbf{J}_{\alpha}') = \tau^{(a)}(\mathbf{J}')$ provided $\nu^{*}(\mathbf{J}_{\alpha}) = \nu^{*}(\mathbf{J})$. (See Corollary to Lemma 2, §1, and Lemma 13, §4.) We can easily see that if an element $f$ of $\mathbf{R}$ (viewed as an element of $\mathbf{R}'$) is $\mathbf{J}'$-stable then $f$ is $\mathbf{J}$-stable.

REMARK 2. Let $(f_1, \cdots, f_m)$ be a standard base of an ideal $\mathbf{J}$ in $\mathbf{R}$. If the system $(f_1, \cdots, f_m)$ is $\mathbf{J}$-stable, if $\{(\mathbf{J}_\alpha, \mathbf{R}_\alpha, \mathbf{P}_{\alpha-1})\}$ is a sequence of strict monoidal transforms of $(\mathbf{J}, \mathbf{R})$ such that the sequence $\{(\mathbf{R}_\alpha, \mathbf{P}_{\alpha-1})\}$ is permissible for $\mathbf{J}$ and that $\mathbf{R}_\alpha$ is residually separable algebraic over $\mathbf{R}_{\alpha-1}$ for all $\alpha$, where $\mathbf{R}_0 = \mathbf{R}$, and if $\bar{\alpha}$ is an index such that $\nu^*(\mathbf{J}_{\bar{\alpha}}) = \nu^*(\mathbf{J})$ and $\tau^*(\mathbf{J}_{\bar{\alpha}}) = \tau^*(\mathbf{J})$, then $(f_1^{(\bar{\alpha})}, \cdots, f_m^{(\bar{\alpha})})$ with a strict transform $f_j^{(\bar{\alpha})}$ of $f_j$ in $\mathbf{R}_{\bar{\alpha}}$ along $\{(\mathbf{R}_\alpha, \mathbf{P}_{\alpha-1})\}$ for $1 \leq j \leq m$ is a standard base of $\mathbf{J}_{\bar{\alpha}}$. (See Theorem 5 of § 6.)

REMARK 3. Let  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  be a regular frame of R. Let J be an ideal in R. Suppose  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  is J-stable. Then for every prime ideal  $P_{0}$  in R which is a permissible center for J we have  $\mathbf{P}_{0} \supseteq (z_{1}, \cdots, z_{r})\mathbf{R}$ . Moreover, for every strict monoidal transform  $(\mathbf{J}_{1}, \mathbf{R}_{1}, \mathbf{P}_{0})$  of  $(\mathbf{J}, \mathbf{R})$  which is permissible for J and such that  $R_{1}$  is residually separable algebraic over R, and that  $\nu^{*}(\mathbf{J}_{1}) = \nu^{*}(\mathbf{J})$ , and  $\tau^{*}(\mathbf{J}_{1}) = \tau^{*}(\mathbf{J})$ , we have that  $(\mathbf{S}, z_{1}, \cdots, z_{r})$  admits a frame transform  $(\mathbf{S}_{1}; z_{1}/x, \cdots, z_{r}/x)$  in  $R_{1}$  with a denominator  $x \in P_{0} \cap S$ . Moreover, if  $\{(\mathbf{J}_{\alpha}, \mathbf{R}_{\alpha}, \mathbf{P}_{\alpha-1})\}$  is a sequence of strict monoidal transforms of  $(\mathbf{J}, \mathbf{R})$  such that the sequence  $\{(\mathbf{R}_{\alpha}, \mathbf{P}_{\alpha-1})\}$  is permissible for J and that  $R_{\alpha}$  is residually separable algebraic over  $R_{\alpha-1}$  for all  $\alpha \geq 1 (\mathbf{R}_{0} = \mathbf{R})$ , and if an index  $\bar{\alpha} (\geq 1)$  is such that  $\nu^{*}(\mathbf{J}_{\bar{\alpha}}) = \nu^{*}(\mathbf{J})$  and  $\tau^{*}(\mathbf{J}_{\bar{\alpha}}) = \tau^{*}(\mathbf{J})$ , then we can find a sequence of regular frames  $(\mathbf{S}_{\beta}; z_{1}^{(\beta)}, \cdots, z_{r}^{(\beta)})$  of  $R_{\beta}$  for all  $\beta \leq \bar{\alpha}$  such

that  $(\mathbf{S}_{\beta}; z_{1}^{(\beta)}, \cdots, z_{r}^{(\beta)})$  is a frame transform of  $(\mathbf{S}_{\beta-1}; z_{1}^{(\beta-1)}, \cdots, z_{r}^{(\beta-1)})$  in  $R_{\beta}$  for all  $\beta \geq 1$ , where  $(\mathbf{S}_{0}; z_{1}^{(0)}, \cdots, z_{r}^{(0)})$  denotes  $(\mathbf{S}; z_{1}, \cdots, z_{r})$ . Here the denominator of the above frame transform  $(\mathbf{S}_{\beta}; z_{1}^{(\beta)}, \cdots, z_{r}^{(\beta)})$  of  $(\mathbf{S}_{\beta-1}; z_{1}^{(\beta-1)}, \cdots, z_{r}^{(\beta-1)})$  can be taken in  $P_{\beta-1} \cap S_{\beta-1}$ . We shall call  $(\mathbf{S}_{\bar{x}}; z_{1}^{(\bar{\alpha})}, \cdots, z_{r}^{(\bar{\alpha})})$  a frame transform of  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  in  $R_{\bar{\alpha}}$  along the sequence  $\{(\mathbf{R}_{\alpha}, \mathbf{P}_{\alpha-1})\}$ .

DEFINITION 12. A regular $\tau$-frame of $\mathbf{R}$ for $\mathbf{J}$, say $(\mathbf{S}; z_1, \cdots, z_r)$, is said to be $\mathbf{J}$-stable (or, stable with respect to $\mathbf{J}$) if it is a $\mathbf{J}$-stable regular frame of $\mathbf{R}$ and if, at the same time, it satisfies the following condition: For every permissible sequence of strict monoidal transforms $\{(\mathbf{J}_{\alpha}, \mathbf{R}_{\alpha}, \mathbf{P}_{\alpha-1})\}$ of $(\mathbf{J}, \mathbf{R})$ such that $\mathbf{R}_{\alpha}$ is residually separable algebraic over $\mathbf{R}_{\alpha-1}$ for all $\alpha \geq 1$ ($\mathbf{R}_0 = \mathbf{R}$) and for every index $\bar{\alpha} \geq 1$ such that $\nu^*(\mathbf{J}_{\bar{\alpha}}) = \nu^*(\mathbf{J})$ and $\tau^*(\mathbf{J}_{\bar{\alpha}}) = \tau^*(\mathbf{J})$, we have a regular $\tau$-frame $(\mathbf{S}_{\bar{\alpha}}; z_1^{(\bar{\alpha})}, \cdots, z_r^{(\bar{\alpha})})$ of $\mathbf{R}_{\bar{\alpha}}$ for $\mathbf{J}_{\bar{\alpha}}$, which is a frame transform of $(\mathbf{S}; z_1, \cdots, z_r)$ in $\mathbf{R}_{\bar{\alpha}}$ along the sequence $\{(\mathbf{R}_{\alpha}, \mathbf{P}_{\alpha-1})\}$.

THEOREM 8. Let R be a regular local ring, J an ideal in R, and  $(\mathbf{S}; z_{1}, \cdots, z_{\tau})$  a J-stable regular  $\tau$ -frame of R for J. Then every normalized standard base of J with respect to  $(\mathbf{S}; z_{1}, \cdots, z_{\tau})$  is J-stable.

PROOF. Let P be a prime ideal in R which is a permissible center for J. Let  $R_{1}$  be a monoidal transform of R with center P which is residually separable algebraic over R, and  $J_{1}$  the strict transform of J in  $R_{1}$. Assume that  $\nu^{*}(J_{1}) = \nu^{*}(J)$, and  $\tau^{*}(J_{1}) = \tau^{*}(J)$. Let  $(\mathbf{S}_{1}; w_{1}, \cdots, w_{\tau})$  be a frame transform of  $(\mathbf{S}; z_{1}, \cdots, z_{\tau})$  in  $R_{1}$  with denominator  $x \in P \cap S$  (such that  $(x)R_{1} = PR_{1}$). Let  $(f_{1}, \cdots, f_{m})$  be a normalized standard base of J with respect to  $(\mathbf{S}; z_{1}, \cdots, z_{\tau})$. Let  $\nu_{j} = \nu^{(j)}(\mathbf{J})$  for  $1 \leq j \leq m$, and  $g_{j} = x^{-\nu_{j}}f_{j}$  for  $1 \leq j \leq m$. It is sufficient to show that  $(g_{1}, \cdots, g_{m})$  is a normalized standard base of  $J_{1}$  with respect to  $(\mathbf{S}_{1}; w_{1}, \cdots, w_{\tau})$. First of all, by Theorem 6 of §7,  $\nu_{\mathrm{P}}(f_{j}) = \nu_{j}$  for all  $j (1 \leq j \leq m)$, so that  $g_{j} \in J_{1}$  for  $1 \leq j \leq m$. To prove that  $(g_{1}, \cdots, g_{m})$  is a normalized standard base of  $J_{1}$, we may assume that R is complete with respect to the topology defined by the powers of  $(z_{1}, \cdots, z_{\tau})\mathbf{R}$, so that  $R = S\{z_{1}, \cdots, z_{\tau}\}$. Let  $t = t(\mathbf{J})$, so that  $\tau = \tau^{(t)}(\mathbf{J})$. Let  $\tau_{a} = \tau^{(a)}(\mathbf{J})$  for  $1 \leq a \leq t$. Let  $m_{a} = t$  the maximal integer such that  $\nu^{(ma)}(\mathbf{J}) = \mu^{\varepsilon(a)}(\mathbf{J})$  for  $1 \leq a \leq t$. Let  $S^{(a)} = S\{z_{\tau_{a+1}}, \cdots, z_{\tau}\}$. Let  $(\mathbf{S}_{1}^{(a)}; w_{1}, \cdots, w_{\tau_{a}})$  be the frame transform of  $(\mathbf{S}^{(a)}; z_{1}, \cdots, z_{\tau_{a}})$  in  $R_{1}$  with the denominator x. We shall prove, by induction on a ( $1 \leq a \leq t$), that  $(g_{1}, \cdots, g_{m_{a}})$  can be extend to a standard base of  $J_{1}$, that  $\tau_{(w)_{a}}(g_{1}, \cdots, g_{m_{a}}) = 0$  where  $(w)_{a} = (w_{1}, \cdots, w_{\tau_{a}})$, and that  $g_{m_{a+1}}, \cdots, g_{m_{a+1}}$  are all normalized by  $(g_{1}, \cdots, g_{m_{a}})$  with respect to  $(\mathbf{S}_{1}^{(a)}; w_{1}, \cdots, w_{\tau_{a}})$. The first two assertions are clear for a = 1. For an

arbitrary  $a \geq 1$ , the last assertion follows from the first two by Lemma 20 of §8. This lemma also shows that  $(g_{1}, \cdots, g_{m_{a+1}})$  can be extended to a standard base of  $J_{1}$ , i.e., the first assertion for a increased by 1. Then the second assertion for a increased by 1 follows by virtue of Lemma 19 of §7. Thus  $\tau_{(w)}(g_{1}, \cdots, g_{m}) = 0$  for  $(w) = (w_{1}, \cdots, w_{\tau})$ , and  $(g_{1}, \cdots, g_{m})$  is a normalized standard base of  $J_{1}$ . q.e.d.

## 10. The existence of a J-stable regular  $\tau$ -frame and a J-stable standard base

DEFINITION 13. Let $\mathbf{R}$ be a regular local ring, and $\mathbf{J}$ an ideal in $\mathbf{R}$. Let $(z) = (z_1, \cdots, z_r)$ be a system of elements of $\mathbf{R}$ which can be extended to a regular system of parameters of $\mathbf{R}$. Let us assume that $(z)$ is $\mathbf{J}$-stable. Then we say that an element $f$ of $\mathbf{R}$ is $(\mathbf{J}; \tau_{(z)})$-stable if it has the following property: Let $\{(\mathbf{J}_{\alpha}, \mathbf{R}_{\alpha}, \mathbf{P}_{\alpha-1})\}$ be any permissible sequence of strict monoidal transforms of $(\mathbf{J}, \mathbf{R})$, such that $\mathbf{R}_{\alpha}$ is residually separable algebraic over $\mathbf{R}_{\alpha-1} (= \mathbf{R}$ if $\alpha = 1$) for all $\alpha$. Let $\bar{\alpha}$ be any index $\geq 0$ such that $\nu^*(\mathbf{J}_{\bar{\alpha}}) = \nu^*(\mathbf{J})$ and $\tau^*(\mathbf{J}_{\bar{\alpha}}) = \tau^*(\mathbf{J})$, where $\mathbf{J}_{\bar{\alpha}} = \mathbf{J}$ if $\bar{\alpha} = 0$. Let $(z^{(\bar{\alpha})}) = (z_1^{(\bar{\alpha})}, \cdots, z_r^{(\bar{\alpha})})$ be a system of strict monoidal transforms $z_j^{(\bar{\alpha})}$ of $z_j (1 \leq j \leq r)$ in $\mathbf{R}_{\bar{\alpha}}$ along the sequence $\{(\mathbf{R}_{\alpha}, \mathbf{P}_{\alpha-1})\}$, if $\bar{\alpha} \geq 1$, and $(z^{(0)}) = (z)$. (Note that $(z^{(\bar{\alpha})})$ can be extended to a regular system of parameters of $\mathbf{R}_{\bar{\alpha}}$, for $(z)$ is J-stable.) Let $f^{(\bar{\alpha})}$ be a strict transform of $f$ in $\mathbf{R}_{\bar{\alpha}}$ along the sequence $\{(\mathbf{R}_{\alpha}, \mathbf{P}_{\alpha-1})\}$, if $\bar{\alpha} \geq 1$, and $f^{(0)} = f$. Then we have $\nu_{\mathrm{M}_{\bar{\alpha}}} (f^{(\bar{\alpha})}) = \nu_{\mathrm{M}}(f)$, $\nu_{\mathrm{P}_{\bar{\alpha}}} (f^{(\bar{\alpha})}) = \nu_{\mathrm{M}}(f)$ (provided $\mathbf{P}_{\bar{\alpha}}$ exists and is different from $\mathbf{R}_{\bar{\alpha}}$) $\tau_{(z^{(\bar{\alpha})})}(f^{(\bar{\alpha})}) = \tau_{(z)}(f)$, where $\mathbf{M}_{\bar{\alpha}}$ (resp. M) denotes the maximal ideal of $\mathbf{R}_{\bar{\alpha}}$ (resp. R) and $\mathbf{M}_0 = \mathbf{M}$.

An element f of R will be said to be  $(\mathbf{J}, \tau)$ -stable if it is  $(\mathbf{J}; \tau_{(z)})$ -stable with an empty system  $(z)$ .

LEMMA 22. Let R be a regular local ring, M the maximal ideal of R and (S; x) a regular frame of R. Let f be an element of R which can be written in the form

$$
f = x ^ {\nu} + g _ {2} x ^ {\nu - 2} + \dots + g _ {\nu}\tag{\((\nu >0)\}
$$

where  $g_{j} \in S$  for  $2 \leq j \leq \nu$ . If the residue field k of S is of characteristic zero, then x is contained in every prime ideal P in R such that  $\nu_{\mathrm{PRP}}(f) \geq \nu$ , where f is viewed as an element of  $R_{P}$ .

PROOF. We shall first prove the assertion under the additional assumptions that there exists a non-unit element h of S such that  $x - h \in P$  and that R is complete. In fact, let z = x - h. We write f in the form:

$$
f = z ^ {\nu} + g _ {1} ^ {\prime} z ^ {\nu - 1} + \dots + g _ {\nu} ^ {\prime}
$$

with $g_j' \in \mathbf{S}(1 \leq j \leq \nu)$.

Then $g_1' = \nu h$. Let $\mathbf{R}' = \mathbf{R}_{\mathbf{P}}$ and $\mathbf{S}' = \mathbf{S}_{\mathbf{P} \cap \mathbf{S}}$. Obviously $(\mathbf{S}', z)$ is a regular frame of $\mathbf{R}'$. Let $\mathbf{P}' = \mathbf{P}\mathbf{R}'$ and $\mathbf{Q}' = (\mathbf{P} \cap \mathbf{S})\mathbf{S}'$. We have $\mathbf{P}' = (z, \mathbf{Q}')\mathbf{R}'$. The assumption that $\nu_{\mathrm{PRP}}(f) \geq \nu$ implies that $f \in (z, \mathbf{Q}')'\mathbf{R}'$. Hence, by the uniqueness of the above expression of $f$ in terms of $z$ and $g_j' \in \mathbf{S}$, we have $\nu_{\mathbf{Q}'}(g_j') \geq j$ for $1 \leq j \leq \nu$. In particular, $\nu h = g_1' \in \mathbf{P}'$, hence $h \in \mathbf{P}' \cap \mathbf{R} = \mathbf{P}$. Hence $x = z + h \in \mathbf{P}$.

Next we shall prove the assertion for the case in which R/P is regular. In this case,  $\nu_{\mathrm{PRP}}(f) \geq \nu$  is equivalent to saying that  $f \in P^{\nu}$ . Let  $(w_{1}, \cdots, w_{r})$  be a minimal base of P, and  $W_{j}$  the initial form of  $w_{j}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ , which is in  $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$ , for  $1 \leq j \leq r$ . The assumption  $f \in P^{\nu}$  implies that the initial form  $\varphi$  of f in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  is a form only in  $W_{1}, \cdots, W_{r}$ . On the other hand, if  $(y_{1}, \cdots, y_{s})$  is a regular system of parameters of S, and if  $X(\text{resp. } Y_{j})$  is the initial form of x (resp.  $y_{j}$ ) in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ , then  $\varphi$  can be written as

$$
\varphi = X ^ {\nu} + \lambda_ {2} X ^ {\nu - 2} + \dots + \lambda_ {\nu},
$$

where  $\lambda_{j}$  is a form of degree j only in  $Y_{1},\cdots,Y_{s}$ . Comparing these two expressions of  $\varphi$ , we see that one of the  $W_{j}$ , say  $W_{1}$ , can be written as

$$
W _ {1} = b X + \sum_ {j} a _ {j} Y _ {j}
$$

where $b$ and $a_{j}$ are in $\mathbf{k}(=\mathbf{R}/\mathbf{M})$ and $b \neq 0$. Let $\hat{\mathbf{S}}$ and $\hat{\mathbf{R}}$ be the completions of $\mathbf{S}$ and $\mathbf{R}$. Then the above result shows that $\hat{\mathbf{R}} = \hat{\mathbf{S}}\{w_{1}\}$. Hence we have $h \in \hat{\mathbf{S}}$ such that $x - h \in (w_{1})\hat{\mathbf{R}} \subseteq \mathbf{P}\hat{\mathbf{R}}$. We know that $\mathbf{P}\hat{\mathbf{R}}$ is a prime ideal in $\hat{\mathbf{R}}$ and that $\nu_{\mathrm{PRP}}(f) \geq \nu$ implies that $\nu_{\mathrm{PRP}\hat{\mathbf{R}}}(f) \geq \nu$. Hence, by the first result, we have $x \in \mathbf{P}\hat{\mathbf{R}}$. Hence $x \in \mathbf{P}\hat{\mathbf{R}} \cap \mathbf{R} = \mathbf{P}$.

Next we shall reduce the proof to the case in which k is algebraically closed and R is complete. We have a complete local ring  $\widetilde{S}$  and a local monomorphism  $S \to \widetilde{S}$  which transforms a regular system of parameters of S into such a system of  $\widetilde{S}$, and such that the residue field of  $\widetilde{S}$  is algebraically closed. Let  $\widetilde{R} = \widetilde{S}\{x\}$. We have a canonical local monomorphism  $R \to \widetilde{R}$. Let  $\widetilde{P}$  be a prime ideal in  $\widetilde{R}$  such that  $\widetilde{P} \cap R = P$. In fact, such  $\widetilde{P}$  exists because  $\widetilde{R}$  is faithfully flat over R. As is easily seen, the assumptions of the lemma remain valid if we replace  $\{R, (S; x), P\}$  by  $\{\widetilde{R}, (\widetilde{S}; x), \widetilde{P}\}$. Therefore, if the lemma was proved for the case in which k is algebraically closed and R is complete, then  $x \in \widetilde{P} \cap R = P$.

We shall assume that k is algebraically closed and that R is complete. We shall reduce the proof in this case to the case in which R/P is regular. First of all, by induction on dim R/P, we can reduce the proof to the case in which dim R/P = 1. So we shall assume this. Suppose R/P is not regular. Then we have  $y \in S$  such that  $y \notin P$ , and that  $(y)$  can be extended to

a regular system of parameters of S. In fact, if otherwise, P should contain the maximal ideal N of S. But NR is a prime ideal, and R/NR is a regular local ring of dimension 1, so that P = NR which is a contradiction. So we take such an element y of S. Let  $R_{1}$  be a monoidal transform of R with center M such that:  $(y)\mathbf{R}_{1} = \mathbf{MR}_{1}, \mathbf{R}_{\mathbf{P}} \supseteq \mathbf{R}_{1}$ , and  $R_{1}$  is residually algebraic (hence, rational) over R. Let  $P_{1}$  be the prime ideal in  $R_{1}$  with  $\mathbf{R}_{\mathbf{P}} = (\mathbf{R}_{1})_{\mathbf{P}_{1}}$  and  $M_{1}$  the maximal ideal of  $R_{1}$ . We claim that  $x/y \in M_{1}$ . In fact, if otherwise, there exists a unit element u in S such that  $x/y - u \in M_{1}$ . Let  $x^{*} = x/y - u$ . Let  $S_{1}$  be the monoidal transform of S with center N (=the maximal ideal of S) = M ∩ S, such that we have a local canonical homomorphism  $S_{1} \to R_{1}$ . Then  $(\mathbf{S}_{1}; x^{*})$  is a regular frame of  $R_{1}$ . The element  $y^{-\nu}f$  can be written as

$$
y ^ {- \nu} f = (x ^ {*}) ^ {\nu} + g _ {1} ^ {*} (x ^ {*}) ^ {\nu - 1} + \dots + g _ {\nu} ^ {*}
$$

where  $g_{j}^{*}\in S_{1}$  for  $1\leq j\leq\nu$ . We have  $g_{1}^{*}=\nu u$ , which is a unit of  $S_{1}$ . On the other hand, we have  $(\mathbf{R}_{1})_{\mathbf{P}_{1}}=\mathbf{R}_{\mathbf{P}}$ , hence  $\nu_{\mathbf{P}_{1}(\mathbf{R}_{1})\mathbf{P}_{1}}(y^{-\nu}f)\geq\nu$ . By Theorem 1 of §3, we then have  $\nu_{\mathbf{M}_{1}}(y^{-\nu}f)\geq\nu$ . Since  $(\mathbf{S}_{1};x^{*})$  is a regular frame of  $R_{1}$ , we must have  $\nu_{\mathbf{M}_{1}}(g_{j}^{*})\geq j$  for  $1\leq j\leq\nu$ . This inequality for j=1 contradicts the fact that  $g_{1}^{*}=\nu u$  which is a unit in  $R_{1}$ . Now that we have  $x_{1}=x/y\in M_{1}$ , the assumptions of the lemma remain valid if we replace  $(\mathbf{R},\mathbf{S},x,f,\mathbf{P})$  by  $(\mathbf{R}_{1},\mathbf{S}_{1},x_{1},f_{1},\mathbf{P}_{1})$  where  $f_{1}=y^{-\nu}f$ . Note that if we can prove  $x_{1}\in P_{1}$ , then it follows that  $x\in P$ , because  $(\mathbf{R}_{1})_{\mathbf{P}_{1}}=\mathbf{R}_{\mathbf{P}}$ . Hence, if  $R_{1}/P_{1}$  is regular, then the proof is done. If  $R_{1}/P_{1}$  is not regular, we repeat the same process as above. Since R/P is of dimension 1, and its integral closure in its field of quotients is a finite R/P-module (by the completeness of R/P) the process cannot be repeated infinitely. q.e.d.

LEMMA 23. Let $\mathbf{S} = \mathbf{k}[X_0, X_1, \cdots, X_n]$ be a polynomial ring of $n + 1$ indeterminates over a perfect field $\mathbf{k}$. Let $F$ be a form of degree $\nu > 0$ in $\mathbf{S}$. Let $\mathbf{T}$ be the smallest $\mathbf{k}$-module of linear forms in $\mathbf{S}$ such that $\mathbf{k}[\mathbf{T}]$ contains $F$. Let $\mathbf{A} = \mathbf{k}[X_1 / X_0, \cdots, X_n / X_0]$, $F_0 = F / X_0^\nu \in \mathbf{A}$, and $\mathbf{I}_0$ the ideal in $\mathbf{A}$ generated by the elements of the form $Y / X_0$ with $Y \in \mathbf{T}$. If $\mathbf{N}$ is any prime ideal in $\mathbf{A}$ such that $\nu_{\mathrm{NAN}}(F_0) \geq \nu$, then $\mathbf{N}$ contains $\mathbf{I}_0$.

PROOF. The proof can be easily reduced to the case in which N is a maximal ideal in A. Let  $\tilde{k}$  be an algebraic closure of k. Let  $\widetilde{S} = \widetilde{k}S = \widetilde{k}[X_{0}, X_{1}, \cdots, X_{n}]$ . Since k is perfect,  $\widetilde{k}$  is separable over k and, by Lemma 12, §4, we see that if  $\widetilde{T}$  is the smallest  $\widetilde{k}$ -module of linear forms in  $\widetilde{S}$  such that  $\widetilde{k}[\widetilde{T}]$  contains F, then we have  $\widetilde{T} \cap S = T$ . In view of this fact, we can easily conclude that we may assume the algebraic closedness of k in the proof of Lemma 23. (In fact, replace k by  $\widetilde{k}$ .) Then every

maximal ideal N in A has a base of the form  $(X_{1}/X_{0}-c_{1},\cdots,X_{n}/X_{0}-c_{n})$ , where  $c_{j}\in k$ . The assumption  $\nu_{\mathrm{NAN}}(F_{0})\geq\nu$  is equivalent to saying that  $N^{\nu}$  contains  $F_{0}$ . This implies that F is contained in  $(X_{1}-c_{1}X_{0},\cdots,X_{n}-c_{n}X_{0})^{\nu}\mathbf{S}$ , so that F is a form in  $k[X_{1}-c_{1}X_{0},\cdots,X_{n}-c_{n}X_{0}]$ . Thus N contains  $I_{0}$ . (See Lemma 10, § 4.) q.e.d.

This lemma has the following geometric interpretation, which is interesting in its own right: Let X be a projective linear scheme over a perfect field k, i.e.,  $X = \text{Proj}(S)$  with a graded polynomial ring  $S = k[X_{0}, X_{1}, \cdots, X_{n}]$  of  $n + 1$  indeterminates over k. Let V be a subscheme of X defined by a form of degree  $\nu > 0$  in S, i.e., a hypersurface of order  $\nu$  in X. Then there exists a linear subscheme L of X which has the following property: a point x of X belongs to L if and only if x is a point of V at which V has multiplicity  $\nu$ . (L can be empty.)

LEMMA 24. Let R be a regular local ring, M the maximal ideal of R and  $(z_{1},\cdots,z_{r})$  a system of elements of M which can be extended to a regular system of parameters of R. Let f be an element of R, and  $(y_{1},\cdots,y_{\tau})$  a regular system of  $\tau_{(z)}$ -parameters of R for f, where  $\tau=\tau_{(z)}(f)$ . Let P be a prime ideal in R such that

(i)  $\mathbf{P} \cong (z_{1}, \cdots, z_{r}, y_{1}, \cdots, y_{\tau})\mathbf{R},$

(ii) $\mathbf{R} / \mathbf{P}$ is regular and $\nu_{\mathbf{P}}(f) = \nu_{\mathbf{M}}(f)$.

We assume that the residue field $\mathbf{R} / \mathbf{M}$ of $\mathbf{R}$ is perfect. Let $\mathbf{R}_1$ be a monoidal transform of $\mathbf{R}$ with center $\mathbf{P}$, and $\mathbf{M}_1$ the maximal ideal of $\mathbf{R}_1$. Let $x \in \mathbf{P}$ such that $(x)\mathbf{R}_1 = \mathbf{PR}_1$. Let $\nu = \nu_{\mathbf{M}}(f)$, $\bar{f} = fx^{-\nu}$, $\bar{z}_j = z_j x^{-1}$ ($1 \leq j \leq r$) and $\bar{y}_j = y_j x^{-1}$ ($1 \leq j \leq \tau$).

We assume that

(iii) $\overline{z}_j\in \mathbf{M}_1$ for all $j(1\leq j\leq r)$.

If $\nu_{\mathbf{M}_1}(\bar{f}) = \nu_{\mathbf{M}}(f)$, then we have $\bar{y}_i \in \mathbf{M}_1$ for all $i$ ($1 \leq i \leq \tau$).

PROOF. Suppose we have an index i such that  $y_{i}x^{-1}$  is a unit in  $R_{1}$ , say  $i=\tau$ . Then we may take  $y_{\tau}$  to be the element x in the assertion. We then have a minimal base of P of the form:  $(z_{1},\cdots,z_{r},y_{1},\cdots,y_{\tau-1},x,x_{1},\cdots,x_{s})$ . Let  $\overline{z}_{j}$  and  $\overline{y}_{i}$  be the same as in the assertion, and  $\overline{x}_{k}=x_{k}x^{-1}$  for  $1\leq k\leq s$ . Let  $A=R[\overline{z}_{1},\cdots,\overline{z}_{r},\overline{y}_{1},\cdots,\overline{y}_{\tau},\overline{x}_{1},\cdots,\overline{x}_{s}]$ . We have a prime ideal N in A such that  $R_{1}=A_{N}$ . Then we have  $N\supseteq MA$  and  $NA_{N}=M_{1}$ . We can identify A/MA with the following polynomial ring of  $(r+\tau+s-1)$  indeterminates over the residue field k of R:

$$
k \left[ \bar {Z} _ {1}, \dots , \bar {Z} _ {r}, \bar {Y} _ {1}, \dots , \bar {Y} _ {\tau - 1}, \bar {X} _ {1}, \dots , \bar {X} _ {s} \right],
$$

where  $\bar{Z}_{i}$  (resp.  $\bar{Y}_{j}$ , resp.  $\bar{X}_{k}$ ) denotes the image of  $\bar{z}_{i}$  (resp.  $\bar{y}_{j}$ , resp.  $\bar{x}_{k}$ ) in A/MA. Let  $Z_{i}$  (resp.  $Y_{j}$ , resp.  $X_{k}$ ) be the initial form of  $z_{i}$  (resp.  $y_{j}$ , resp.  $x_{k}$ ) in gr $_{\mathbf{M}}(\mathbf{R})$ . Let X be also the same of x in gr $_{\mathbf{M}}(\mathbf{R})$ . By the choice

of  $(y_{1},\cdots,y_{\tau}=x)$ , if  $\varphi$  denotes the initial form of f in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ , then  $\varphi$  is a form of degree  $\nu$  only in  $Z_{1},\cdots,Z_{r},X,Y_{1},\cdots,Y_{\tau-1}$ . Moreover, by (ii), if  $\Phi$  denotes the initial form of f in  $\mathrm{gr}_{\mathbf{P}}(\mathbf{R})$ , then the canonical homomorphism of  $\mathrm{gr}_{\mathbf{P}}(\mathbf{R})$  into  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  maps  $\Phi$  to  $\varphi$ . From this, it follows that the image of  $\bar{f}$  in A/MA is equal to

$$
\varphi (\bar {Z} _ {1}, \dots , \bar {Z} _ {r}, 1, \bar {Y} _ {1}, \dots , \bar {Y} _ {\tau - 1}),
$$

i.e., it is obtained by replacing  $Z_{i}/X$  by  $\bar{Z}_{i}$  and  $Y_{j}/X$  by  $\bar{Y}_{j}$  in the quotient  $\varphi/X^{\nu}$ . ( $\varphi$  is viewed as a form in  $Z_{1},\cdots,Z_{r},X,Y_{1},\cdots,Y_{r}$  with coefficients in k.) Now, the assumption that  $\nu_{\mathbf{M}_{1}}(\bar{f})=\nu_{\mathbf{M}}(f)$  should imply that  $\nu_{\mathbf{N}\overline{\mathbf{A}}\overline{\mathbf{N}}}(\bar{F})\geq\nu$  where  $\bar{A}=A/MA$ ,  $\bar{N}=N/MA$  and  $\bar{F}$  the image of  $\bar{f}$  in  $\bar{A}$ . In view of Lemma 23, if T is the smallest k-submodule of  $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R})$  such that  $\varphi\in\mathbf{k}[T]$ , which is contained in the module generated by  $Z_{1},\cdots,Z_{r},X,Y_{1},\cdots,Y_{\tau-1}$ , then we have  $W/X\in\bar{N}$  for all  $W\in T$  in the sense of the above identifications among indeterminates. On the other hand, (iii) shows that  $\bar{N}$  contains all the  $\bar{Z}_{i}$ . Since X is contained in the module generated by T and the  $Z_{i}$ , we should have  $1=X/X\in\bar{N}$ , which is absurd. q.e.d.

LEMMA 25. Let R be a complete regular local ring whose residue field has characteristic zero, and J an ideal in R. Let  $(z_{1}, \cdots, z_{r})$  be a system of elements of R, and f an element of R such that

(i)  $(z)=(z_{1},\cdots,z_{r})$  is J-stable and can be extended to a regular system of parameters of R, and

(ii) $f$ is $(\mathbf{J},\tau_{(z)})$-stable.

If $\tau_{(z)}(f) \geq 1$, then there exists an element $w$ of $\mathbf{R}$ such that

(1)  $(z, w) = (z_{1}, \cdots, z_{r}, w)$  is J-stable and can be extended to a regular system of parameters of R,

(2) $\tau_{(z w)}(f) = \tau_{(z)}(f) - 1, a n d$

(3) $f$ is $(\mathbf{J},\tau_{(z w)})$-stable.

PROOF. Let us take a regular system of parameters

$$
(z _ {1}, \dots , z _ {r}, x _ {1}, \dots , x _ {s})
$$

of $\mathbf{R}$ such that, if $t = \tau_{(z)}(f)$, $(x_1, \cdots, x_t)$ is a regular system of $\tau_{(z)}$-parameters of $\mathbf{R}$ for $f$. We have a subfield $\mathbf{k}$ of $\mathbf{R}$ such that $\mathbf{R} = \mathbf{k}\{z_1, \cdots, z_r, x_1, \cdots, x_s\}$ by the structure theorem of a complete regular local ring (equi-characteristic). Let $\mathbf{M}$ be the maximal ideal of $\mathbf{R}$ and $\nu = \nu_{\mathbf{M}}(f)$. By the symbol $\mathbf{k}$, we shall also denote the residue field $\mathbf{R}/\mathbf{M}$ which is canonically isomorphic to the coefficient field $\mathbf{k}$ of $\mathbf{R}$. The graded k-algebra $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ can be identified with the polynomial ring

$$
\mathbf {k} \left[ Z _ {1}, \dots , Z _ {r}, X _ {1}, \dots , X _ {s} \right],
$$

where  $Z_{j}$  (resp.  $X_{j}$ ) denotes the initial form of  $z_{j}$  (resp.  $x_{j}$ ) in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ . Let  $\varphi$  be the initial form of f in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ . Then  $\varphi$  is a form of degree  $\nu$  in  $Z_{1}, \cdots, Z_{r}, X_{1}, \cdots, X_{t}$ . Let  $S = k\{x_{1}, \cdots, x_{s}\}$  and  $S_{0} = k\{x_{2}, \cdots, x_{s}\}$  (=k if s = 1). Let us write

$$
f = \sum_ {A \in \mathbf {Z} _ {0} ^ {r}} h _ {A} z ^ {A}
$$

with $h_A \in \mathbf{S}$.

Let $\varphi_{A}$ be the initial form of $h_A$ in $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ only for those $A$ with $|A| + \nu_{\mathbf{M}}(h_A) = \nu$. Then

$$
\varphi = \sum_ {A} \varphi_ {A} Z ^ {A} \quad \text { for } | A | + \nu_ {\mathrm{M}} (h _ {A}) = \nu .
$$

Since  $(x_{1},\cdots,x_{t})$  is a regular system of  $\tau_{(z)}$ -parameters of R for f, those  $\varphi_{A}$  are forms in  $X_{1},\cdots,X_{t}$ , and there exists  $\bar{A}\in Z_{0}^{r}$  such that  $|\bar{A}|+\nu_{\mathbf{M}}(h_{\bar{A}})=\nu$  and that  $\deg\varphi_{\bar{A}}>0$ . Let  $\deg\varphi_{\bar{A}}=\nu_{\mathbf{M}}(h_{\bar{A}})=e$ . By taking a suitable linear (non-singular) transformation of  $(x_{1},\cdots,x_{t})$  with coefficients in k, we may assume that  $\varphi_{\bar{A}}$  has the term of  $X_{1}^{e}$  with non-zero coefficient in k. Then by the Weierstrass preparation theorem, we can write

$$
h _ {\overline {{{A}}}} = u (x _ {1} ^ {e} + p _ {1} ^ {\prime} x _ {1} ^ {e - 1} + \dots + p _ {e} ^ {\prime}),
$$

where u is a unit element of S and  $p_{j}^{\prime} \in S_{0}$  for  $1 \leq j \leq e$ . Since  $P_{A}$  is a form in  $X_{1}, \cdots, X_{t}$ , the class of  $p_{1}^{\prime}$  in  $\mathrm{gr}_{\mathbf{M}}^{1}(\mathbf{R}) = \mathbf{M}/\mathbf{M}^{2}$  must be a form only in  $X_{2}, \cdots, X_{t}$ , which may be zero. Therefore, we may replace  $x_{1}$  by  $x_{1} + e^{-1}p_{1}^{\prime}$  without affecting the assumption that  $(x_{1}, \cdots, x_{t})$  is a regular system of  $\tau_{(z)}$ -parameters of R for f. Thus we may assume that

$$
h _ {\overline {{{A}}}} = u (x _ {1} ^ {e} + p _ {2} x _ {1} ^ {e - 2} + \dots + p _ {e}),
$$

where $p_j \in \mathbf{S}_0$ for $2 \leq j \leq e$. We shall prove that $w = x_1$ has the property required in the Lemma. The property (2) is clear from our selection of $w$.

In order to prove (1) and (3), we reformulate the assertion in the following form:

Let R be a regular local ring whose residue field has characteristic zero, J an ideal in R,  $(\mathbf{S}; z_{1}, \cdots, z_{r})$  a regular frame of R and  $(\mathbf{S}_{0}; w)$  a regular frame of S. Let f be an element of R. Suppose:

(1) $(z_{1},\dots ,z_{r})$ is J-stable, i.e., (S; $z_{1},\dots ,z_{r})$ is J-stable,

(2) $f$ is $(\mathbf{J},\tau_{(z)})$-stable,

(3) (w) can be extended to a regular system of $\tau_{(z)}$-parameters of $\mathbf{R}$ for $f$, and

(4) $f$ can be written in the form:

$$
f = g + u z ^ {\overline {{{A}}}} \left(w ^ {e} + p _ {2} w ^ {e - 2} + \dots + p _ {e}\right)
$$

where

$$
\left\{ \begin{array}{l} g = \sum_ {\substack {A \in Z _ {0} ^ {r} \\ A \neq \overline {A}}} h _ {A} z ^ {A} \\ u = a \text {unit in S}, \\ e = \nu_ {\mathrm{M}} (f) - | \overline {A} | > 0, \text {and} \\ p _ {j} \in \mathbf {S} _ {0} \end{array} \right.
$$

with $h_A \in \mathbf{S}$,

$$
f o r 2 \leq j \leq e.
$$

Let $\mathbf{P}$ be any prime ideal in $\mathbf{R}$ which is a permissible center for $\mathbf{J}$, $\mathbf{R}_1$ a monoidal transform of $\mathbf{R}$ with center $\mathbf{P}$ which is residually algebraic (necessarily, separable algebraic) over $\mathbf{R}$, and $\mathbf{J}_1$ the strict transform of $\mathbf{J}$ in $\mathbf{R}_1$. We shall prove that

(a)  $\mathbf{P} \supseteq (z_{1}, \cdots, z_{r}, w)\mathbf{R},$

(b) $\nu_{\mathbf{P}}(f) = \nu$ (throughout, $\nu$ denotes $\nu_{\mathbf{M}}(f)$),

(c) if $\nu^{*}(\mathbf{J}_{1}) = \nu^{*}(\mathbf{J})$ and $\tau^{*}(\mathbf{J}_{1}) = \tau^{*}(\mathbf{J})$, then there exists $y \in \mathbf{P} \cap \mathbf{S}_{0}$ such that $\mathbf{PR}_{1} = (y)\mathbf{R}_{1}$ and such that:

(i)  $\overline{z}_{j}=z_{j}/y\ (1\leq j\leq r)$  and  $\overline{w}=w/y$  are non-units in  $R_{1}$ , hence,  $(\mathbf{S};z_{1},\cdots,z_{r})$  admits a frame transform  $(\mathbf{S}_{1};\overline{z}_{1},\cdots,\overline{z}_{r})$  in  $R_{1}$ , and  $(\mathbf{S}_{0};w)$  admits a frame transform  $(\mathbf{S}_{01};\overline{w})$  in  $S_{1}$ ,

(ii) if $\overline{f} = x^{-\nu}f$, then $(\overline{w})$ can be extended to a regular system of $\tau_{(\overline{z})}$-parameters of $\mathbf{R}_1$ for $\overline{f}$ and $\tau_{(\overline{z},\overline{w})}(\overline{f}) = \tau_{(z,w)}(f)$, and

(iii) $\bar{f}$ can be written in the same form as $f$ in (4) where $(z, w)$ and $(\mathbf{S}, \mathbf{S}_0)$ are replaced by $(\bar{z}, \bar{w})$ and $(\mathbf{S}_1, \mathbf{S}_{01})$ respectively.

One can easily see that, if we prove these facts, then the proof of the lemma is completed. Now, (1) implies that  $\mathbf{P} \supseteq (z_{1}, \cdots, z_{r})\mathbf{R}$ . By (2), we have  $\nu_{\mathbf{p}}(f) = \nu$ , i.e., (b), and therefore by (4) we have

$$
w ^ {e} + p _ {2} w ^ {e - 2} + \dots + p _ {e} \in \mathbf {Q} ^ {e},
$$

where Q is the prime ideal  $P \cap S$  in S. (Note that S/Q is regular.) By Lemma 22, we then have  $w \in Q \subseteq P$ . Thus (a). Let  $Q_{0} = Q \cap S_{0} = P \cap S_{0}$ . We have  $y \in Q_{0}$  such that  $(y)R_{1} = PR_{1}$ . In fact, if y is any element of P such that  $(y)R_{1} = PR_{1}$ , then we have  $z_{j}/y \in M_{1}$  for all j, where  $M_{1}$  denotes the maximal ideal of  $R_{1}$ . (See (1).) Moreover, by Lemma 24, (2) implies that  $w/y \in M_{1}$ . We thus see that  $y \in Q_{0}$  exists and that all the  $\bar{z}_{j}$  and  $\bar{w}$  are non-units in  $R_{1}$ , i.e., (i) of (c). (iii) of (c) is clear, and we have only to show (ii) of (c). As in the proof of Lemma 22, the proof of (ii) of (c) can be reduced to the case in which the residue field k of  $S_{0}$  is algebraically closed, so that  $R_{1}$  is residually rational over R. Let us choose a minimal base  $(y_{1}, \cdots, y_{i})$  of  $Q_{0}$  in such a way that  $y = y_{i}$  and  $\bar{y}_{j} = y_{j}/y \in M_{1}$  for  $1 \leq j \leq i - 1$ . Lemma 24 shows that, if  $\tau = \tau_{(z)}(f) - 1 (= \tau_{(z,w)}(f))$ , there exist  $\tau$  independent linear combinations of  $y_{1}, \cdots, y_{i-1}$  with coefficients in  $S_{0}$  which form a regular system of  $\tau_{(z,w)}$-parameters of R for f. Therefore, we may assume that  $(w, y_{1}, \cdots, y_{\tau})$  is a regular system of

$\tau_{(z)}$ -parameters of R for  $f(\tau \leq i - 1)$ . Let b = i - 1. Let us choose a regular system of parameters  $(y_{1}, \cdots, y_{b}, y, x_{1}, \cdots, x_{a})$  of  $S_{0}$ . Then  $(z_{1}, \cdots, z_{r}, w, y_{1}, \cdots, y_{b}, y, x_{1}, \cdots, x_{a})$  is a regular system of parameters of R, and  $(\overline{z}_{1}, \cdots, \overline{z}_{r}, \overline{w}, \overline{y}_{1}, \cdots, \overline{y}_{b}, y, x_{1}, \cdots, x_{a})$  is a regular system of parameters of  $R_{1}$ . Then

$$
\operatorname{gr} _ {\mathbf {M}} (\mathbf {R}) = \mathbf {k} \left[ Z _ {1}, \dots , Z _ {r}, W, Y _ {1}, \dots , Y _ {b}, Y, X _ {1}, \dots , X _ {a} \right]
$$

where  $Z_{j}$  (resp. W, resp.  $Y_{j}$ , resp. Y, resp.  $X_{j}$ ) denotes the initial form of  $z_{j}$  (resp. w, resp.  $y_{j}$ , resp. y, resp.  $x_{j}$ ) in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$ , and

$$
\operatorname{gr} _ {\mathbf {M} _ {1}} (\mathbf {R} _ {1}) = \mathbf {k} [ \bar {Z} _ {1}, \dots , \bar {Z} _ {r}, \bar {W}, \bar {Y} _ {1}, \dots , \bar {Y} _ {b}, Y, X _ {1}, \dots , X _ {a} ],
$$

where  $\bar{Z}_{j}$  (resp.  $\bar{W}$ , resp.  $\bar{Y}_{j}$ , resp. Y, resp.  $X_{j}$ ) denotes the initial form of  $\bar{z}_{j}$  (resp.  $\bar{w}$ , resp.  $\bar{y}_{j}$ , resp. y, resp.  $x_{j}$ ) in  $\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ . Let  $\varphi$  (resp.  $\bar{\varphi}$ ) denote the initial form of  $f(\mathrm{resp.}\bar{f})$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  (resp.  $\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ ). Then  $\deg\varphi = \deg\bar{\varphi} = \nu$ ,  $\varphi$  is a form only in  $Z_{1}, \cdots, Z_{r}, W, Y_{1}, \cdots, Y_{\tau}$ , and

$$
\bar {\varphi} = \varphi (\bar {Z} _ {1}, \dots , \bar {Z} _ {r}, \bar {W}, \bar {Y} _ {1}, \dots , \bar {Y} _ {\tau}) + \bar {\varphi} ^ {*}
$$

with  $\bar{\varphi}^{*}\in(Y,X_{1},\cdots,X_{a})\operatorname{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ . By the assumption (2), we can find a system of linear forms  $(L,L_{1},\cdots,L_{\tau})$  in  $Y,X_{1},\cdots,X_{a}$  with coefficients in k such that

$$
\bar {\varphi} = \varphi (\bar {Z} _ {1}, \dots , \bar {Z} _ {r}, \bar {W} + L, \bar {Y} _ {1} + L _ {1}, \dots , \bar {Y} _ {\tau} + L _ {\tau}).
$$

We can find linear combinations  $v_{1}, \cdots, v_{\tau}$  of  $y, x_{1}, \cdots, x_{a}$  with coefficients in  $S_{0}$  such that  $L_{j}$  is the initial form of  $v_{j}$  in  $\mathrm{gr}_{\mathbf{M}}(\mathbf{R})$  (hence, in  $\mathrm{gr}_{\mathbf{M}_{1}}(\mathbf{R}_{1})$ ) for  $1 \leq j \leq \tau$ . We may replace  $y_{j}$  by  $y_{j} + v_{j}y$  for  $1 \leq j \leq \tau$  without affecting any of the assumptions on  $(y_{1}, \cdots, y_{b})$  in the above argument, so that we may assume that  $L_{1} = \cdots = L_{\tau} = 0$ . We then have

$$
\bar {\varphi} = \varphi (\bar {Z} _ {1}, \dots , \bar {Z} _ {r}, \bar {W} + L, \bar {Y} _ {1}, \dots , \bar {Y} _ {\tau}).
$$

On the other hand, we can write,

$$
\bar {f} = \bar {g} + u \bar {z} ^ {\bar {A}} (\bar {w} ^ {e} + \bar {p} _ {2} \bar {w} ^ {e - 2} + \dots \bar {p} _ {e})
$$

where

$$
\left\{ \begin{array}{l} \bar {g} = \sum_ {\substack {A \in Z _ {0} ^ {r} \\ A \neq \bar {A}}} \bar {h} _ {A} \bar {z} ^ {A} \\ u = \textbf {a unit in S} _ {1}, \\ e = \nu - | \bar {A} |, \text {and} \\ \bar {p} _ {j} = y ^ {- j} p _ {j} \in \mathbf {S} _ {0 1} \end{array} \right.
$$

$$
\text { with } \bar {h} _ {A} = h _ {A} y ^ {- (\nu - | A |)} \in \mathbf {S _ {1}}
$$

$$
(2 \leq j \leq e).
$$

Hence $\overline{\varphi}$ is of the form

$$
\bar {\varphi} = \bar {\psi} + c \bar {Z} ^ {\tilde {A}} (\bar {W} ^ {e} + \bar {\lambda} _ {2} \bar {W} ^ {e - 2} + \dots + \bar {\lambda} _ {e}),
$$

where

$$
\left\{ \begin{array}{l l} \bar {\psi} = \sum_ {A \neq \bar {A}} \bar {\delta} _ {A} \bar {Z} ^ {A} & \text { with } \bar {\delta} _ {A} \in \mathbf {k} [ \bar {W}, \bar {Y} _ {1}, \dots , \bar {Y} _ {b}, \bar {Y}, \bar {X} _ {1}, \dots , \bar {X} _ {a} ] \\ c \neq 0 & (\text { a   constant   in   k }) \\ \bar {\lambda} _ {j} \in \mathbf {k} [ \bar {Y} _ {1}, \dots , \bar {Y} _ {b}, \bar {Y}, \bar {X} _ {1}, \dots , \bar {X} _ {a} ]. \end{array} \right.
$$

On the other hand, $\varphi$ is of the form

$$
\varphi = \psi + c Z ^ {\bar {A}} (W ^ {e} + \lambda_ {2} W ^ {e - 2} + \dots + \lambda_ {e})
$$

where

$$
\left\{ \begin{array}{l} \psi = \sum_ {A \neq \bar {A}} \delta_ {A} Z ^ {A} \quad \text {with} \delta_ {A} \in \mathbf {k} [ W, Y _ {1}, \dots , Y _ {b}, Y, X _ {1}, \dots , X _ {a} ] \\ c = \text {the same non - zero constant in k as above} \\ \lambda_ {j} \in \mathbf {k} [ Y _ {1}, \dots , Y _ {b}, Y, X _ {1}, \dots , X _ {a} ]. \end{array} \right.
$$

Therefore the equality

$$
\bar {\varphi} = \varphi (\bar {Z} _ {1}, \dots , \bar {Z} _ {r}, \bar {W} + L, \bar {Y} _ {1}, \dots , \bar {Y} _ {\tau})
$$

implies that

$$
\bar {W} ^ {e} + \bar {\lambda} _ {2} \bar {W} ^ {e - 2} + \dots + \bar {\lambda} _ {e} = (\bar {W} + L) ^ {e} + \lambda_ {2} (\bar {W} + L) ^ {e - 2} + \dots + \lambda_ {e}.
$$

It follows that $eL = 0$, hence $L = 0$. Thus

$$
\bar {\varphi} = \varphi (\bar {Z} _ {1}, \dots , \bar {Z} _ {r}, \bar {W}, \bar {Y} _ {1}, \dots , \bar {Y} _ {\tau}).
$$

It follows that $(\overline{w})$ can be extended to a regular system of $\tau_{(\overline{z})}$-parameters of $\mathbf{R}_1$ for $\overline{f}$, and that $\tau_{(\overline{z},\overline{w})}(\overline{f}) = \tau_{(z w)}(f)(= \tau)$. q.e.d.

THEOREM 9. Let R be a complete regular local ring whose residue field has characteristic zero, and J an ideal in R. Then there exists a J-stable regular τ-frame of R for J and a J-stable standard base of J.

PROOF. We may assume that  $\mathbf{J} \neq (0)$ . Let us assume that there exists a system of elements  $(f_{1}, \cdots, f_{i})$  of J and  $(z_{1}, \cdots, z_{r})$  of the maximal ideal M of R  $(i \geq 0, r \geq 0)$  such that

(1) $(f_{1},\dots ,f_{i})$ is extendable to a standard base of $\mathbf{J}$,

(2)  $(z) = (z_{1}, \cdots, z_{r})$  can be extended to a regular system of  $\tau$ -parameters of R for the system  $(f_{1}, \cdots, f_{i})$ ,

(3) $\tau_{(z)}(f_j) = 0 (1 \leq j \leq i - 1)$, and $\tau(f_1, \cdots, f_i) = r + \tau_{(z)}(f_i)$,

(4) the extension of  $(z)$  by a regular system of  $\tau_{(z)}$ -parameters of R for  $(f_{i})$  is extendable to a regular system of  $\tau$ -parameters of R for J,

(5) $(z)$ is J-stable, and finally

(6) $f_{j}$ is $(\mathbf{J},\tau_{(z)})$ -stable for all $j$$(1\leq j\leq i)$

(Recall Definitions 7 (§ 4), 10\* (§ 7), 11 (§ 9) and 13 (§ 10).) We then claim: (A) If $\tau_{(z)}(f_i) > 0$, then there exists an element $z_{r+1} \in \mathbf{M}$ such that replacing $(z)$ by $(z_1, \cdots, z_r, z_{r+1})$ we maintain (1)-(6).

(B) If  $\tau_{(z)}(f_i)=0$ , then there exists an element  $f_{i+1}\in J$  such that replacing  $(f_1,\cdots,f_i)$  by  $(f_1,\cdots,f_i,f_{i+1})$  we maintain (1)-(6).

(A) is immediate from Lemma 25. To prove (B), take a regular frame of R of the form  $(\mathbf{S}; z_{1}, \cdots, z_{r})$ . Then take an element  $f_{i+1}$  of J such that  $(f_{1}, \cdots, f_{i}, f_{i+1})$  is extendable to a standard base of J and that  $f_{i+1}$  is normalized by  $(f_{1}, \cdots, f_{i})$  with respect to  $(\mathbf{S}; z_{1}, \cdots, z_{r})$ . (We should refer to Lemma 17, § 7. See also the footnote 11 of this chapter.) The proof of (B) for this  $f_{i+1}$  can be obtained by Lemmas 18–19, § 7, and Lemmas 20–21, § 8.

## CHAPTER IV. THE FUNDAMENTAL THEOREMS AND THEIR PROOFS

For the language of algebraic schemes, one should refer to the paragraphs in the beginning of Chapter I in addition to Grothendieck [6, Ch. I.]. We have fixed a class of local rings, $\mathcal{B}$ in symbol, in the beginning of Chapter I. In this chapter we shall only be concerned with algebraic schemes and morphisms of algebraic schemes: an algebraic scheme is by definition a scheme which admits a morphism of finite type from itself to a prime spectrum $\operatorname{Spec}(\mathbf{S})$ with $\mathbf{S} \in \mathcal{B}$, and a morphism of algebraic schemes is by definition any morphism of schemes from an algebraic scheme to another algebraic scheme. For the definitions of resolution data and permissible transformations, the first section of Chapter I should be referred to. We have stated the fundamental theorems $\mathrm{I}_1^{N,n}, \mathrm{I}_2^{N,n}, \Pi_1^N$ and $\Pi_2^N$ in the second section of Ch. I. They assert the resolution of resolution data by means of a finite succession of monoidal transformations which are permissible. We have also indicated the basic inductive implications (A), (B), (C), and (D) which complete the inductive proofs of the fundamental theorems. (See § 2, Ch. I.) The purpose of this chapter is to establish the basic implications (A), (B), (C), and (D).

In this chapter, we shall often find it convenient to express a resolution datum of type  $R_{I}^{N,n}$  on a non-singular irreducible algebraic scheme X in the following form:

$$
\mathfrak {R} _ {\mathrm{I}} ^ {N, n} = \left(\bigcup_ {i = 1} ^ {\alpha} E _ {i}; V _ {1}, V _ {2}, \dots , V _ {\beta}; W\right).
$$

We agree once for all that whenever this expression is taken, all the  $E_{i}$  denote non-singular irreducible subschemes of X of codimension one. We do not require that  $E_{i}$  differ from  $E_{j}$  if  $i \neq j$ . We may find the empty subscheme of X among the  $E_{i}$ , which is a non-singular irreducible subscheme of X of codimension one according to our agreement upon the codimension of the empty subscheme. (See the introductory paragraphs of Chapter I.)

In the treatment of a resolution datum of type  $R_{II}^{N}$  on a non-singular irreducible algebraic scheme X, say

$$
\mathfrak {R} _ {\mathrm{II}} ^ {N} = \left( \begin{array}{c c c c} E _ {1}, & E _ {2}, & \dots , & E _ {\alpha} \\ a _ {1}, & a _ {2}, & \dots , & a _ {\alpha} \end{array} \bigg | J, b\right),
$$

all that are essential among its characteristics are the following ones: the set $C(\mathfrak{R}_{\mathrm{II}}^N)$ of those irreducible subschemes $E_i$ of $X$ which are not empty, the integers $a(E) = \sum_{E_i = E} a_i$ for $E \in C(\mathfrak{R}_{\mathrm{II}}^N)$, $J$ and $b$. In other words, any two resolution data of type $\mathfrak{R}_{\mathrm{II}}^N$ on the same $X$ may be considered as the same one whenever they have the same $C(\mathfrak{R}_{\mathrm{II}}^N)$, the same $a(E)$ for $E \in C(\mathfrak{R}_{\mathrm{II}}^N)$, the same $J$ and the same $b$. (Recall the definitions of a permissible monoidal transformation, the sets $S(\mathfrak{R}_{\mathrm{II}}^N)$ and $S_v(\mathfrak{R}_{\mathrm{II}}^N)$ and theorems $\Pi_1^N$ and $\Pi_2^N$. They only depend upon the above four characteristics of a resolution datum $\mathfrak{R}_{\mathrm{II}}^N$). However, we shall find it convenient to identify a resolution datum $\mathfrak{R}_{\mathrm{II}}^N$ with the above expression, and to distinguish any two resolution data with different expressions.

## 1. Localization of resolution data and resolution problems

Let $f \colon X' \to X$ be a morphism of algebraic schemes, which is of finite type; we are particularly interested in the case where $f$ is obtained by a monoidal transformation or by a finite succession of monoidal transformations. Take a point $x$ of $X$ and the local ring $S$ of $X$ at $x$. We know that $S$ belongs to the class $\mathcal{B}$, and that $\operatorname{Spec}(S)$ is an algebraic scheme. We have a canonical immersion $i \colon \operatorname{Spec}(S) \to X$, which maps the unique closed point of $\operatorname{Spec}(S)$ to the point $x$ of $X$. This permits us to identify $\operatorname{Spec}(S)$ with the restriction of $X$ to the set of those points of $X$ whose closures contain $x$, i.e., $x$ is a specialization of those points in $X$. The product of the schemes $X'$ and $\operatorname{Spec}(S)$ over $X$ (with reference to $f$ and $i$) will be denoted by $X_S'$ (or, by $(X')_S$). This is the product in the category of schemes over a fixed scheme $X$. $X_S'$ is also an algebraic scheme. We have a canonical immersion $j \colon X_S' \to X'$, which permits us to identify $X_S'$ with the restriction of $X'$ to the set of those points of $X'$ which belong to $f^{-1}(\operatorname{Spec}(S))$, where $\operatorname{Spec}(S)$ is identified with $i$ ($\operatorname{Spec}(S)$) as above. In an obvious manner, a subscheme of $X'$ induces a subscheme of $X_S'$ and every subscheme of $X_S'$ is obtained in this way. If $Y'$ is a subscheme of $X'$, then the subscheme of $X_S'$ induced by $Y'$ is canonically isomorphic to $Y_S'$ (which denotes the product $Y'$ and $\operatorname{Spec}(S)$ over $X$) so that we can view $Y_S'$ as the subscheme of $X_S'$ induced by $Y'$. For every point $y$ of $Y_S'$, which is also viewed as a point of $Y'$, the local ring of $Y_S'$ at $y$ is equal to (or, more precisely, canonically isomorphic to) the local ring of

$Y'$ at y. Hence, if $Y'$ is reduced (resp. non-singular) then $Y_{S}'$ is reduced (resp. non-singular). It is also easy to see that, if $Y'$ is irreducible, then $Y_{S}'$ is irreducible. Also in an obvious manner, an open (resp. closed) subset H of $X'$ induces an open (resp. closed) subset of $X_{S}'$, which we denote by $H_{S}$.

Let $g: X'' \to X$ be another morphism of algebraic schemes which is of finite type. If $h: X' \to X''$ is a morphism of algebraic schemes such that $f = g \circ h$, then $h$ is of finite type, and it induces a morphism of $X_S'$ to $X_S''$ which is of finite type. We shall denote by $h_S$ this canonical morphism of $X_S'$ to $X_S''$ induced by $h$. If $h$ is obtained by a monoidal transformation of $X''$ with center $B''$, then $h_S$ is obtained by the monoidal transformation of $X_S'$ with center $B_S''$. In this manner, if $h$ denotes a monoidal transformation (or, a succession of monoidal transformations) then $h_S$ will denote the corresponding monoidal transformation (or, respectively, the corresponding succession of monoidal transformations).

DEFINITION 1. Let $f \colon X' \to X$ be a morphism of algebraic schemes which is of finite type. We assume that $X'$ is non-singular irreducible. Let $\mathfrak{R}'$ be a resolution datum (with or without restriction) on $X'$, $x$ a point of $X$ and $\mathbf{S}$ the local ring of $X$ at $x$. Then we define and denote by $\mathfrak{R}_{\mathrm{S}}'(or, (\mathfrak{R}')_{\mathrm{S}})$ the resolution datum on $X_{\mathrm{S}}'$ induced by $\mathfrak{R}'$ as follows:

(I) If $\Re' = (E'; V_1', \cdots, V_\beta'; W')$, a resolution datum of type $\Re_{1}^{N,n}$ on $X'$, then $\Re_{S}' = (E_S'; (V_1')_S, \cdots, (V_\beta')_S; W_S')$. If $\Re' = (\Re_{1}^{N,n}, F')$ (resp. $= (\Re_{1}^{N,n}, U')$), a resolution datum of type $\Re_{1}^{N,n}$ with closed restriction $F'$ (resp. open restriction $U'$), then $\Re_{S}' = ((\Re_{1}^{N,n})_S, F_S')$ (resp. $= ((\Re_{1}^{N,n})_S, U_S')$).

(II) If  $\Re' = \left( E_{1'}', \cdots, E_{\alpha'}' \mid J', b \right)$ , a resolution datum of type  $R_{11}^{N}$  on  $X'$ , then

$$
\mathfrak {R} _ {\mathrm{S}} ^ {\prime} = \left( \begin{array}{c c c} (E _ {1}) _ {\mathrm{S}}, & \dots , & (E _ {\alpha} ^ {\prime}) _ {\mathrm{S}} \\ a _ {1} ^ {\prime}, & \dots , & a _ {\alpha} ^ {\prime} \end{array} \bigg | J _ {\mathrm{S}} ^ {\prime}, b\right),
$$

where  $J_{S}^{\prime}$  denotes the restriction of  $J^{\prime}$  to  $X_{S}^{\prime}$  which is a sheaf of non-zero ideals on  $X_{S}^{\prime}$ . If  $\Re^{\prime} = (\Re_{\Pi}^{N}, F^{\prime})$ , a resolution datum of type  $R_{II}^{N}$  with closed restriction  $F^{\prime}$ , then  $\Re_{S}^{\prime} = ((\Re_{\Pi}^{N})_{S}, F_{S}^{\prime})$ .

REMARK 1. Let the notation and assumptions be the same as in Definition 1. Let $\bar{N} = \dim X_{\mathrm{S}}'$ and $\bar{n} = \dim W_{\mathrm{S}}'$.

(1) If $\Re' = (\Re_{\mathrm{I}}^{N,n}, F')$ (resp. $= (\Re_{\mathrm{I}}^{N,n}, U')$) then $\Re_{\mathrm{S}}'$ is a resolution datum on $X_{\mathrm{S}}'$ of the type $\Re_{\mathrm{I}}^{\overline{N},\overline{n}}$ with closed restriction $F_{\mathrm{S}}'$ (resp. with open restriction $U_{\mathrm{S}}'$).

(II) If $\Re' = \Re_{\Pi}^{N}$ (resp. $= (\Re_{\Pi}^{N}, F')$) then $\Re_S'$ is a resolution datum on $X_S'$ of the type $\Re_{\Pi}^{\overline{N}}$ without restriction (resp. with restriction $F_S'$).

REMARK 2. Let X be an algebraic scheme. Let  $f: X' \to X$  be a morphism of algebraic schemes which is obtained by a succession of monoidal transformations with nowhere dense centers. Let x be a point of X and S the local ring of X at x. Then we have  $\dim(X_{\mathrm{S}}') = \dim(\mathrm{S})$  (the Krull dimension of the local ring S). Therefore, in the above Remark 1,  $\bar{N} \leq N$ . The equality occurs only when  $\dim(X) = \dim(\mathrm{S})$ .

LEMMA 1. Let $\mathfrak{R}_{\mathrm{I}}^{N,n} = (\bigcup_{i=1}^{\alpha} E_i; V_1, \cdots, V_\beta; W)$ be a resolution datum of type $\mathfrak{R}_{\mathrm{I}}^{N,n}$ on a non-singular irreducible algebraic scheme $X$. Let $U$ be the set of points of $W$ at which $\mathfrak{R}_{\mathrm{I}}^{N,n}$ is resolved. Then $U$ is an open subset of $W$ which has non-empty intersection with every irreducible component of $W$.

PROOF. It is clear that  $R_{i}^{N,n}$  is resolved at the generic points of irreducible components of W. We have only to prove that U is an open subset of W. First of all, we know that the set of simple points of W forms an open subset of W. By Theorem 1 of Ch. II, the set of points of W at which  $V_{1}, \cdots, V_{\beta}$  are normally flat along W is an open subset of W. All left to be proved is that, if W has only normal crossings with  $\bigcup_{i=1}^{\alpha} E_{i}$  at a point x of W, then there exists an open subset of W containing x at every point of which W has only normal crossings with  $\bigcup_{i=1}^{\alpha} E_{i}$ . Let  $\operatorname{Spec}(\mathbf{A})$  be an affine open subscheme of X which contains the given point x, where A is an algebra of finite type over a base ring of X. Let P be the prime ideal in A such that  $A_{P}$  is the local ring of X at x. We have a regular system of parameters  $(z_{1}, \cdots, z_{r})$  of  $A_{P}$  such that those  $E_{i}$  passing through x as well as W have prime ideals in  $A_{P}$  generated by subsystems of  $(z_{1}, \cdots, z_{r})$ . We arrange the indices of the  $z_{j}$  in such a way that, for a certain positive integer  $s \leq r$ ,  $(z_{1}, \cdots, z_{s})$  generates the prime ideal of W in  $A_{P}$ . By replacing A by  $A_{f}$  with a suitable  $f \in A - P$ , so that  $\operatorname{Spec}(A_{f})$  is an affine open subscheme of X containing the given point x, we may assume that:

(1) For every subsystem  $(z_{i_{1}},\cdots,z_{i_{t}})$  of  $(z_{s+1},\cdots,z_{r})$ ,  $(z_{1},\cdots,z_{s},z_{i_{1}},\cdots,z_{i_{t}})$ A is a prime ideal in A, and  $\mathbf{A}/(z_{1},\cdots,z_{s},z_{i_{1}},\cdots,z_{i_{t}})$ A is a regular ring, and,

(2)  $\operatorname{Spec}(\mathbf{A}) \cap W$  is irreducible (hence, non-singular by (1)), so that  $(z_{1}, \cdots, z_{s})\mathbf{A}$  is the prime ideal of W in the affine ring A, and

(3) $\operatorname{Spec}(\mathbf{A})$ has empty intersection with any of the $E_{j}$ which does not pass through $x$.

Now, if y is any point of  $\operatorname{Spec}(\mathbf{A}) \cap W$  and if Q denotes the prime ideal of y in A, then by (1) the subsystem of  $(z_{1}, \cdots, z_{r})$  consisting of those  $z_{j}$  contained in Q can be extended to a regular system of parameters of the local ring  $A_{Q}$  of X at y, so that, by (2) and (3), W has only normal crossings with  $\bigcup_{i=1}^{\alpha} E_{i}$  at y. q.e.d.

LEMMA 2. Let $\mathfrak{R}_{\mathrm{II}}^{N} = \left( \begin{array}{cc}E_{1},\dots ,E_{\alpha}\\ a_{1},\dots ,a_{\alpha} \end{array} \right|J,b$ be a resolution datum of the type $\mathfrak{R}_{\mathrm{II}}^{N}$ on a non-singular irreducible algebraic scheme $X$. Then $S(\mathfrak{R}_{\mathrm{II}}^N)$ and $S_{*}(\mathfrak{R}_{\mathrm{II}}^{N})$ are closed subsets of $X$ of codimension at least one.

PROOF. We recall the definition

$$
S (\mathfrak {R} _ {\mathrm{II}} ^ {N}) = \{x \in X | \sum_ {x \in E _ {i}} a _ {i} + \nu (J _ {x}) \geq b \}
$$

and, if $\overline{\nu} = \nu (\mathfrak{R}_{\mathrm{II}}^N) = \max_{x\in S(\mathfrak{R}_{\mathrm{II}}^N)}\{\nu (J_x)\}$,

$$
S _ {*} (\mathfrak {R} _ {\mathrm{II}} ^ {N}) = \left\{x \in S (\mathfrak {R} _ {\mathrm{II}} ^ {N}) \mid \nu (J _ {x}) = \overline {{{{\nu}}}} \right\}.
$$

Obviously, the generic point of $X$ does not belong to $S(\mathfrak{R}_{\mathrm{II}}^N)$, and $S_*(\mathfrak{R}_{\mathrm{II}}^N) \subseteq S(\mathfrak{R}_{\mathrm{II}}^N)$. We have only to prove that $S(\mathfrak{R}_{\mathrm{II}}^N)$ and $S_*(\mathfrak{R}_{\mathrm{II}}^N)$ are closed subsets of $X$. Let $P_i$ denote the coherent sheaf of ideals of $E_i$ on $X$ for $1 \leq i \leq \alpha$. Let $J' = \prod_{i=1}^{\alpha} P_i^{a_i} J$, which is a coherent sheaf of ideals on $X$. We have $S(\mathfrak{R}_{\mathrm{II}}^N) = \{x \in X \mid \nu(J_x') \geq b\}$, which is closed in $X$ by Corollary 1 of Theorem 2 of §3, Ch. III. We have $S_*(\mathfrak{R}_{\mathrm{II}}^N) = S(\mathfrak{R}_{\mathrm{II}}^N) \cap \{x \in X \mid \nu(J_x') \geq \overline{\nu}\}$ which is closed, by the same reason. q.e.d.

PROPOSITION 1 (Localization theorem on $(\mathfrak{R}_1^{N,n}, F)$). Let $(N, n)$ be a pair of integers such that $N > n \geq 0$. Let us assume that Theorems $\mathrm{I}_1^{N',n'}$ with $n' < N' < N$ and $n' \leq n$ and Theorems $\mathrm{I}_2^{N',n''}$ with $n'' < n$ are proved. Then, given a resolution datum $(\mathfrak{R}_1^{N,n}, F)$ with $\mathfrak{R}_1^{N,n} = (\bigcup_{i=1}^{\alpha} E_i; V_1, \cdots, V_\beta; W)$ and with closed restriction $F$ on a non-singular irreducible algebraic scheme $X$, there exists a permissible succession of monoidal transformations, say $f: X' \to X$, for $(\mathfrak{R}_1^{N,n}, F)$ such that $f(F' \cap W')$ is at most a finite number of points at which $X$ has dimension $N$, where $f^*(\mathfrak{R}_1^{N,n}) = (\bigcup_{i=1}^{\alpha'} E_i'; V_1', \cdots, V_\beta'; W')$ and $f^*(\mathfrak{R}_1^{N,n}, F) = (f^*(\mathfrak{R}_1^{N,n}), F')$.

PROOF. Let $f: X' \to X$ be any permissible succession of monoidal transformations for the given resolution datum $\Re = (\mathfrak{R}_{\mathrm{I}}^{N,n}, F)$ on $X$. Here we include the case in which $X' = X$ and $f$ is the identity isomorphism. Let us assume that $f(F' \cap W')$ has a point $x$ at which $X$ has dimension $< N$. Then we shall prove that there exists a permissible succession of monoidal transformations $f': X'' \to X'$ for the resolution datum $f^*(\Re)$ on $X'$ such that, if $g = f \circ f'$ and $g^*(\Re) = (g^*(\mathfrak{R}_{\mathrm{I}}^{N,n}), F'')$ with $g^*(\mathfrak{R}_{\mathrm{I}}^{N,n}) = (\bigcup_{i=1}^{\alpha''} E_i'; V_1', \cdots, V_\beta'; W'')$, then $g(F'' \cap W'')$ does not contain $x$. First of all, a morphism obtained by a succession of monoidal transformations is proper and therefore $f(W' \cap F')$ and $g(W'' \cap F'')$ must be closed subschemes of $X$. Obviously, we have $f(W' \cap F') \supseteq g(W'' \cap F'')$. Hence, if we could choose $g$ as above, we have $f(W' \cap F') \supsetneq g(W'' \cap F'')$. In view of the fact that we do not have any infinite sequence of strictly descending closed subsets on an algebraic scheme, the Proposition will follow im-

mediately. We shall prove the existence of $f': X'' \to X'$ having the property stated above. Let $S$ be the local ring of $X$ at the point $x$. Let $\bar{N} = \dim S$. Then $\dim X_S' = \dim S = \bar{N} < N$. Let $\Re' = f^*(\Re)$ and $\Re_S'$ the induced resolution datum on $X_S'$. Then $\Re_S' = (f^*(\Re_I^{N,n})_S, E_S')$ where $f^*(\Re_I^{N,n})_S = (\bigcup_{i=1}^{\alpha'} (E_i')_S; (V_1')_S, \cdots, (V_\beta')_S; W_S')$. Let $\bar{n} = \dim W_S'$. Then $\Re_S'$ is a resolution datum of the type $\Re_I^{N,\bar{n}}$ with closed restriction $F_S'$ on $X_S'$. By assumption, Theorem $I_1^{\bar{N},\bar{n}}$ is verified. Therefore, we can find a permissible succession of monoidal transformations $\bar{f} = \{\bar{f}_j: \bar{X}_{j+1} \to \bar{X}_j\} (0 \leq j \leq a - 1)$ of $\bar{X}_0 = X_S'$ for the resolution datum $\Re_S'$ such that, if $\bar{f}^*(\Re_S') = (^a\Re_I^{\bar{N},\bar{n}}, ^a\bar{F})$ with $^a\Re_I^{\bar{N},\bar{n}} = (\bigcup_{i=1}^\alpha (^a\bar{E}_i); ^a\bar{V}_1, \cdots, ^a\bar{V}_\beta; ^a\bar{W})$, then $^a\bar{F} \cap ^a\bar{W}$ is empty. Let $^0\Re = \Re_S'$ and, for every integer $b$ with $0 \leq b \leq a$, $^b\Re$ the transform of $^0\Re an\bar{X}_b$ by the permissible succession of monoidal transformations $\{\bar{f}_j; \bar{X}_{j+1} \to \bar{X}_j\} (0 \leq j \leq b - 1)$ for $^0\Re$. We shall prove that there exists a permissible succession of monoidal transformations of $X'$ for $\Re'$, say $f' = \{f_k': X_{k+1}' \to X_k'\}$ for $0 \leq k \leq k(a) - 1$ where $X_0' = X'$, such that we have a sequence of integers $0 = k(0) < \cdots < k(a)$ and

(1) $\bar{X}_j = (X_k')_{\mathrm{S}}$ for $k(j) \leq k \leq k(j + 1) - 1$,

(2) the center $B_k'$ of $f_k'$ in $X_k'$ for $k(j) \leq k < k(j + 1) - 1$ is such that $(B_k')_S$ is the empty subscheme of $\bar{X}_j$,

(3) the center $B_{k(j+1)-1}'$ of $f_{k(j+1)-1}'$ in $X_{k(j+1)-1}'$ induces the center of $\bar{f}_j$ in $\bar{X}_j = (X_{k(j+1)-1}')_{\mathbf{S}}$.

As is easily seen, this $f'$ together with $X'' = X_{k(a)}'$ has the property required above, and the proof of Proposition 1 is now reduced to prove the existence of such a sequence $\{f_k': X_{k+1}' \to X_k'\} (0 \leq k \leq k(a) - 1)$. This existence proof can be done by induction on $j$, $0 \leq j \leq a - 1$. Suppose we have found a permissible succession of monoidal transformations of $X'$ for $\mathfrak{R}'$,

$$
\{f _ {k} ^ {\prime}; X _ {k + 1} ^ {\prime} \rightarrow X _ {k} ^ {\prime} \}
$$

$$
(0 \leq k \leq k (b) - 1)
$$

having the properties (1)-(3) for all $j < b$, for a certain non-negative integer $b \leq a - 1$. (If $b = 0$, then this assumption is empty.) Let $^b\mathfrak{R}'$ be the transform of $\mathfrak{R}'$ on $X_{k(b)}'$ by this succession of monoidal transformations. Then we have $\bar{X}_b = (X_{k(b)}')_S$ and $^b\bar{\mathfrak{R}} = (^b\mathfrak{R}')_S$. (If $b = 0$, $X_{k(0)}' = X'$ and $^o\mathfrak{R}' = \mathfrak{R}'$.) Let us write

$$
{ } ^ { b } \Re ^ { \prime } = ( { } ^ { b } \Re _ { I } ^ { N , n } , { } ^ { b } F ^ { \prime } )
$$

with ${}^b{\mathfrak{R}}_1^{N,n} = \left( {{\bigcup  }_{i = 1}^{\alpha \left( b\right) }\left( {{}^{b}{E}_{i}^{\prime }}\right) ;{}^{b}{V}_{1}^{\prime },\cdots ,{}^{b}{V}_{\beta }^{\prime };{}^{b}{W}^{\prime }}\right)$. Let us write

$$
{ } ^ { b } \bar { \mathfrak { R } } = ( { } ^ { b } \mathfrak { R } _ { \mathrm{I} } ^ { \overline { { N } } , \overline { { n } } } , { } ^ { b } \bar { F } )
$$

with $^{b}\mathfrak{R}_{1}^{\overline{N},\overline{n}} = (\bigcup_{i=1}^{\alpha(b)}(^{b}\bar{E}_{i});^{b}\bar{V}_{1},\dots,^{b}\bar{V}_{\beta};^{b}\bar{W})$. Here $^{b}\bar{E}_{i} = (^{b}E_{i}')_{\mathrm{S}},^{b}\bar{V}_{j} = (^{b}V_{j}')_{\mathrm{S}}$

and $^b\bar{W} = (^b W')_{\mathrm{S}}$. Now, let $\bar{B}_b$ be the center of the permissible monoidal transformation $\bar{f}_b$ of $\bar{X}_b$ for $^b\bar{\Re}$. Then $\bar{B}_b$ is a non-singular irreducible subscheme of $\bar{X}_b$ such that $\bar{B}_b \subseteq {}^b\bar{W} \cap {}^b\bar{F}$. Let $B''$ be the smallest irreducible subscheme of $X_{k(b)}'$ such that $\bar{B}_b = (B'')_{\mathrm{S}}$. We then have $B'' \subseteq {}^b W' \cap {}^b F'$, and $\dim (B'') < \dim (^b W') = n$. Let $n'' = \dim (B'')$. Let us consider the resolution datum $^b\Re'' = (\Re_{1}^{N,n'',} U'')$, where $\Re_{1}^{N,n''} = (\bigcup_{i=1}^{a(b)} (^b E_i'); ^b V_1', \cdots, ^b V_\beta', ^b W'; B'')$ and $U'' =$ the set of those points of $B''$ at which $\Re_{1}^{N,n''}$ is resolved. We note that $(B'' - U'')_{\mathrm{S}}$ is the empty subset of $\bar{X}_b$ because the monoidal transformation of $\bar{X}_b$ with center $\bar{B}_b = (B'')_{\mathrm{S}}$ is permissible for $^b\bar{\Re} = (^b\Re')_{\mathrm{S}}$. (Note that $U''$ is an open dense subset of $B''$ by Lemma 1.) Now, by assumption, Theorem $I_2^{N,n''}$ is proved. Therefore, we have a permissible succession of monoidal transformations

$$
h = \left\{f _ {k} ^ {\prime}; X _ {k + 1} ^ {\prime} \rightarrow X _ {k} ^ {\prime} \right\} \quad (k (b) \leq k \leq k (b + 1) - 2)
$$

of $X_{k(b)}'$ for the resolution datum $^b\mathfrak{R}''$ with open restriction $U''$, such that $h^*(\mathfrak{R}_1^{N,n'})$ is resolved. As is easily seen, the succession $h$ is permissible for the resolution datum $^b\mathfrak{R}'$, and the centers of $f_k'(k(b) \leq k \leq k(b + 1) - 2)$ in $X_k'$ induce the empty subscheme of $(X_k')_S$ because $(B'' - U'')_S$ is the empty subset of $(X_{k(b)}')_S$. Let

$$
h ^ {*} \left(\Re_ {1} ^ {N, n ^ {\prime \prime}}\right) = \left(\bigcup_ {i = 1} ^ {\alpha^ {*}} E _ {i} ^ {*}; V _ {1} ^ {*}, \dots , V _ {\beta} ^ {*}, W ^ {*}; B ^ {*}\right)
$$

which is a resolved resolution datum on $X_{k(b + 1) - 1}^{\prime}$. We have $(X_{k(b + 1) - 1}^{\prime})_{\mathbf{S}} = \bar{X}_b$ and $(B^{*})_{\mathbf{S}} = \bar{B}_{\mathbf{b}}$. Moreover, we have that

$$
h ^ {*} \left(^ {b} \Re_ {\mathrm{I}} ^ {N, n}\right) = \left(\bigcup_ {i = 1} ^ {\alpha^ {*}} E _ {i} ^ {*}; V _ {i} ^ {*}, \dots , V _ {\beta} ^ {*}; W ^ {*}\right)
$$

is resolved at every point of $B^{*}$, and that if $F^{*}$ is the strict transform of $^b F'$ on $X_{k(b + 1) - 1}^{\prime}$, then

$$
h ^ {*} (^ {b} \mathfrak {R} ^ {\prime}) = \left(h ^ {*} (^ {b} \mathfrak {R} _ {\mathrm{I}} ^ {N, n}), F ^ {*}\right)
$$

and $B^{*} \subseteq W^{*} \cap F^{*}$. Let $f_{k(b+1)-1}' \colon X_{k(b+1)}' \to X_{k(b+1)-1}'$ be the monoidal transformation with center $B^{*}$. Then

$$
\{f _ {k} ^ {\prime}: X _ {k + 1} ^ {\prime} \rightarrow X _ {k} ^ {\prime} \}
$$

$$
(0 \leq k \leq k (b + 1) - 1)
$$

is a permissible succession of monoidal transformations of $X'$ for $\mathfrak{R}'$. We see immediately that this succession has the properties (1)-(3) for all $j \leq b$. q.e.d.

PROPOSITION 2 (Localization Theorem on $(\mathfrak{R}_1^{N,n}, U)$). Let $(N, n)$ be a pair of integers such that $N > n \geq 0$. Let us assume that Theorem $\mathrm{I}_2^{N',n'}$ with $n' < N' < N$ and $n' \leq n$ and Theorems $\mathrm{I}_2^{N, n''}$ with $n'' < n$ are proved. Then, given a resolution datum $\Re = (\mathfrak{R}_1^{N,n}, U)$ with $\mathfrak{R}_1^{N,n} = (\bigcup_{i=1}^{\alpha} E_i; V_1, \cdots, V_\beta; W)$ and with open restriction $U$ on a non-singular

irreducible algebraic scheme $X$, there exists a permissible succession of monoidal transformations, say $f: X' \to X$, for $\Re$ such that there exists a finite set of points $F$ of $X$ at which $X$ has dimension $N$ and $f^*(\mathfrak{R}_1^{N,n})$ is resolved at every point of $X' - f^{-1}(F)$.

PROOF. The proof of Proposition 2 is essentially the same as that of Proposition 1. Let $f: X' \to X$ be any permissible succession of monoidal transformations of $X$ for the given resolution datum $\mathfrak{R}$. Let $\mathfrak{R}' = f^*(\mathfrak{R})$. Let $T'$ be the closed subset of $X'$ consisting of those points at which $\mathfrak{R}'$ is not resolved. Suppose we have a point $x \in f(T')$ at which $X$ has dimension $< N$. Let S be the local ring of $X$ at $x$. Let $\bar{N} = \dim(S) = \dim X_S'$. Let us write

$$
\mathfrak {R} ^ {\prime} = \left(f ^ {*} (\mathfrak {R} _ {\mathrm{I}} ^ {N, n}), U ^ {\prime}\right)
$$

with $f^{*}(\mathfrak{R}_{\mathrm{I}}^{N,n}) = (\bigcup_{i=1}^{\alpha'} E_i'; V_1', \cdots, V_\beta'; W')$.

In the following arguments, we may replace $U'$ by $W' - T'$. Let $\bar{n} = \dim (W_{\mathrm{S}}')$. Then $\mathfrak{R}_{\mathrm{S}}'$ is a resolution datum of the type $\mathfrak{R}_{1}^{\overline{N},\overline{n}}$ with open restriction $U_{\mathrm{S}}'$ on the non-singular irreducible scheme $X_{\mathrm{S}}'$. We write

$$
\mathfrak {R} _ {\mathrm{S}} ^ {\prime} = (\mathfrak {R} _ {\mathrm{I}} ^ {\overline {{N}}, \overline {{n}}}, \bar {U})
$$

with  $\Re_{\mathrm{I}}^{\overline{{N}},\overline{{n}}}=\left(\bigcup_{i=1}^{\alpha'}\bar{E}_{i};\bar{V}_{1},\cdots,\bar{V}_{\beta};\bar{W}\right)$  where  $\bar{U}=U_{S}'$ ,  $\bar{E}_{i}=(E_{i}')_{S}$ ,  $\bar{V}_{j}=(V_{j}')_{S}$  and  $\bar{W}=(W')_{S}$ . By Theorem  $I_{2}^{\overline{{N}},\overline{{n}}}$ , we have a permissible succession of monoidal transformations

$$
\bar {f} = \{\bar {f} _ {j}: \bar {X} _ {j + 1} \rightarrow \bar {X} _ {j} \}
$$

$$
(0 \leq j \leq a - 1)
$$

of $\bar{X}_0 = X_S'$ for the resolution datum $\mathfrak{R}_{\mathrm{S}}'$ such that $\bar{f}^{*}(\mathfrak{R}_{1}^{\overline{N},\overline{n}})$ is resolved. We shall prove that there exists a permissible succession of monoidal transformations of $X_0' = X'$ for $\mathfrak{R}'$,

$$
\{f _ {k} ^ {\prime}: X _ {k + 1} ^ {\prime} \rightarrow X _ {k} ^ {\prime} \}
$$

$$
\text { for } 0 \leq k \leq k (a) - 1,
$$

such that we have a sequence of integers  $0 = k(0) < k(1) < \cdots < k(a)$  and

(1) $\bar{X}_j = (X_k')_{\mathrm{S}}$ for $k(j)\leq k\leq k(j + 1) - 1,$

(2) the center $B_k'$ of $f_k'$ in $X_k'$ induces the empty subscheme of $\bar{X}_j = (X_k')_S$ for $k(j) \leq k \leq k(j + 1) - 2$,

(3) the center $B_{k(j+1)-1}'$ of $f_{k(j+1)-1}'$ in $X_{k(j+1)-1}'$ induces the center $\bar{B}_j$ of $\bar{f}_j$ in $\bar{X}_j = (X_{k(j+1)-1}')_{\mathbf{S}}$.

Suppose we have found a permissible succession of monoidal transformations of  $X'$  for  $R'$ ,

$$
\{f _ {k} ^ {\prime}: X _ {k + 1} ^ {\prime} \rightarrow X _ {k} ^ {\prime} \}
$$

$$
\text { for   } 0 \leq k \leq k (b) - 1
$$

for a certain non-negative integer $b \leq a - 1$, which has the properties

(1)-(3) for all $j < b$. Let $^b\mathfrak{R}'$ be the transform of $\mathfrak{R}'$ on $X_{k(b)}'$ by this succession of monoidal transformations. We then have $\bar{X}_b = (X_{k(b)}')_\mathrm{S}$ and $^b\bar{\mathfrak{R}} = (^b\mathfrak{R}')_\mathrm{S}$, where $^b\bar{\mathfrak{R}}$ denotes the transform of $^0\bar{\mathfrak{R}} = \mathfrak{R}_\mathrm{S}'$ by the succession of monoidal transformations $\{\bar{f}_j: \bar{X}_{j+1} \to \bar{X}_j\}$ for $0 \leq j \leq b-1$. Let us write

$$
{ } ^ { b } \Re ^ { \prime } = ( { } ^ { b } \Re _ { I } ^ { N , n } , { } ^ { b } U ^ { \prime } )
$$

with $^{b}\mathfrak{R}_{\mathrm{I}}^{N,n} = \left( \bigcup_{i=1}^{\alpha(b)} (^{b}E_{i}') ; ^{b}V_{1}', \cdots, ^{b}V_{\beta}', ^{b}W' \right)$ and

$$
{ } ^ { b } \bar { \mathfrak { R } } = ( { } ^ { b } \mathfrak { R } _ { \mathrm{I} } ^ { \overline { { N } } , \overline { { n } } } , { } ^ { b } \bar { U } )
$$

with  ${}^{b}\mathfrak{R}_{1}^{\overline{N},\overline{n}}=(\bigcup_{i=1}^{\alpha(b)}({}^{b}\bar{E}_{i});{}^{b}\bar{V}_{1},\cdots,{}^{b}\bar{V}_{\beta};{}^{b}\bar{W})$ , where  ${}^{b}\bar{E}_{i}=({}^{b}E_{i}^{\prime})_{S}$ ,  ${}^{b}\bar{V}_{j}=({}^{b}V_{j}^{\prime})_{S}$  and  ${}^{b}\bar{W}=({}^{b}W^{\prime})_{S}$ . Let  $\bar{B}_{b}$  the center of the permissible monoidal transformation  $\bar{f}_{b}$  of  $\bar{X}_{b}$  for  ${}^{b}\overline{R}$ . Let  $B^{\prime\prime}$  be the smallest irreducible subscheme of  $X_{k(b)}^{\prime}$  such that  $\bar{B}_{b}=(B^{\prime\prime})_{S}$ . Since  $\bar{B}_{b}\subseteq{}^{b}\bar{W}-{}^{b}\bar{U}$ ,  $B^{\prime\prime}\subseteq{}^{b}W^{\prime}-{}^{b}U^{\prime}$ . Obviously  $\dim(B^{\prime\prime})<\dim({}^{b}W^{\prime})=n$ . Let  $n^{\prime\prime}=\dim(B^{\prime\prime})$ . Let us consider the resolution datum

$$
{ } ^ { b } \Re ^ { \prime \prime } = ( \Re _ { I } ^ { N , n ^ { \prime \prime } } , U ^ { \prime \prime } )
$$

with $\mathfrak{R}_{\mathrm{I}}^{N,n^{\prime \prime}} = \left(\bigcup_{i=1}^{\alpha(b)}(^{b}E_{1}^{\prime});^{b}V_{1}^{\prime},\cdots,^{b}V_{\beta}^{\prime},^{b}W^{\prime};B^{\prime \prime}\right)$ where $U^{\prime \prime}$ is the open subset of $B^{\prime \prime}$ consisting of those points of $B^{\prime \prime}$ at which $\mathfrak{R}_{\mathrm{I}}^{N,n^{\prime \prime}}$ is resolved. (See Lemma 1.) Since the monoidal transformation of $\bar{X}_b$ with center $\bar{B}_b = (B^{\prime \prime})_{\mathrm{S}}$ is permissible for $^{b}\bar{\mathfrak{R}} = (^{b}\mathfrak{R}')_{\mathrm{S}},(B^{\prime \prime} - U^{\prime \prime})_{\mathrm{S}}$ is the empty subset of $\bar{X}_b = (X_{k(b)}'\mathrm{S})$. Now, applying Theorem $\mathrm{I}_2^{N,n^{\prime \prime}}$ to the resolution datum $^{b}\mathfrak{R}''$, we can get a permissible succession of monoidal transformations

$$
h = \{f _ {k} ^ {\prime}; X _ {k + 1} ^ {\prime} \rightarrow X _ {k} ^ {\prime} \}
$$

$$
\text { for   } k (b) \leq k \leq k (b + 1) - 2
$$

of $X_{k(b)}'$ for $^{b}\mathfrak{R}''$, such that $h^{*}(\mathfrak{R}_{\mathrm{I}}^{N,n'})$ is resolved. Let $h^{*}(\mathfrak{R}_{\mathrm{I}}^{N,n'}) = (\bigcup_{i=1}^{\alpha^{*}} E_{i}^{*}; V_{1}^{*}, \cdots, V_{\beta}^{*}, W^{*}; B^{*})$. Let $f_{k(b+1)-1}' \colon X_{k(b+1)}' \to X_{k(b+1)-1}'$ be the monoidal transformation with center $B^{*}$. We get a permissible succession of monoidal transformations of $X'$ for $\mathfrak{R}'$,

$$
\{f _ {k} ^ {\prime}; X _ {k + 1} ^ {\prime} \rightarrow X _ {k} ^ {\prime} \}
$$

$$
\text { for   } 0 \leq k \leq k (b + 1) - 1
$$

which has the properties (1)-(3) for all $j \leq b$. q.e.d.

PROPOSITION 3 (Localization theorem on $(\mathfrak{R}_{\mathrm{II}}^{N}, F)$). Let $N$ be a positive integer. Let us assume that Theorems $\Pi_1^{N'}$ with $N' < N$ and Theorems $\mathbf{I}_2^{N,n}$ with $n < N$ are verified. Let $\Re = (\Re_{\mathrm{II}}^N, F)$, with $\Re_{\mathrm{II}}^N = \left( \begin{array}{cc}E_1,\dots ,E_\alpha |J,b\\ a_1,\dots ,a_\alpha | \end{array} \right)$ and with closed restriction $F$, be a resolution datum on a non-singular irreducible algebraic scheme $X$. We assume that $\nu = \nu (\Re_{\mathrm{II}}^N) > 0$. Then there exists a permissible succession of monoidal transformations of $X$ for $\Re, f: X' \to X$, such that, if we write

$$
f ^ {*} (\mathfrak {R}) = \left(f ^ {*} (\mathfrak {R} _ {\mathrm{II}} ^ {N}), F ^ {\prime}\right)
$$

with

$$
f ^ {*} (\mathfrak {R} _ {\mathrm{II}} ^ {N}) = \left( \begin{array}{c c c} E _ {1} ^ {\prime}, & \dots , & E _ {\alpha^ {\prime}} ^ {\prime} \\ a _ {1}, & \dots , & a _ {\alpha^ {\prime}} \end{array} \bigg | J ^ {\prime}, b\right),
$$

$f\big(S_{\nu}(f^{*}(\mathfrak{R}_{\mathrm{II}}^{N})) \cap F^{\prime}\big)$ is a finite set of points of $X$ at which $X$ has dimension $N$.

PROOF. The principle of the proof is the same as that for Propositions 1 and 2. Let $f: X' \to X$ be any permissible succession of monoidal transformations for the given resolution datum $\mathfrak{R}$. Let $\mathfrak{R}' = f^*(\mathfrak{R})$. Let us write

$$
\mathfrak {R} ^ {\prime} = \left(f ^ {*} (\mathfrak {R} _ {\mathrm{II}} ^ {N}), F ^ {\prime}\right)
$$

with

$$
f ^ {*} (\mathfrak {R} _ {\mathrm{II}} ^ {N}) = \left( \begin{array}{c c c} E _ {1} ^ {\prime}, & \dots , & E _ {\alpha^ {\prime}} ^ {\prime} \\ a _ {1}, & \dots , & a _ {\alpha^ {\prime}} \end{array} \right| J ^ {\prime}, b)  .
$$

We assume that $f\big(S_{\nu}(f^{*}(\mathfrak{R}_{\mathrm{II}}^{N})) \cap F'\big)$ contains a point $x$ at which $X$ has dimension $\bar{N} < N$. Let $S$ be the local ring of $X$ at $x$. Then $\dim (X_S') = \bar{N}$, and $\mathfrak{R}_S'$ is a resolution datum on $X_S'$ of the type $\mathfrak{R}_{\mathrm{II}}^{\overline{N}}$ with closed restriction $F_S'$. First of all, we remark that, for $f: X' \to X$ as above in general, if $x' \in X'$ then $\nu(J_{x'}) \leq \nu(J_{f(x')} )$ by Lemma 8 of §3, Ch. III, and that $f\big(S(f^{*}(\mathfrak{R}_{\mathrm{II}}^{N}))\big) \subseteq S(\mathfrak{R}_{\mathrm{II}}^{N})$. Moreover, in general, for every non-negative integer $\overline{\nu}, f(S_{\overline{\nu}}(f^{*}(\mathfrak{R}_{\mathrm{II}}^{N}))) \subseteq S_{\overline{\nu}}(\mathfrak{R}_{\mathrm{II}}^{N})$. Now, let $x$ and $S$ be as above. Then we must have $\nu = \nu(f^{*}(\mathfrak{R}_{\mathrm{II}}^{N})) = \nu(f^{*}(\mathfrak{R}_{\mathrm{II}}^{N})_S)$. We shall write

$$
\mathfrak {R} _ {\mathrm{S}} ^ {\prime} = \left(\mathfrak {R} _ {\mathrm{II}} ^ {\overline {{N}}}, \bar {F}\right) = \left(f ^ {*} \left(\mathfrak {R} _ {\mathrm{II}} ^ {N}\right) _ {\mathrm{S}}, F _ {\mathrm{S}} ^ {\prime}\right)
$$

with

$$
\mathfrak {R} _ {\mathrm{II}} ^ {\overline {{N}}} = \left( \begin{array}{c c c} \bar {E} _ {1}, & \dots , & \bar {E} _ {\alpha^ {\prime}} \\ a _ {1}, & \dots , & a _ {\alpha^ {\prime}} \end{array} \right| \bar {J}, b),
$$

where $\bar{F} = F_{\mathrm{S}}'$, $\bar{E}_i = (E_i')_{\mathrm{S}}$ and $\bar{J} = J_{\mathrm{S}}'$. By Theorem $\Pi_1^{\overline{N}}$, we have a permissible succession of monoidal transformations of $\bar{X}_0 = X_{\mathrm{S}}'$ for the resolution datum $\mathfrak{R}_{\mathrm{S}}'$,

$$
\bar {f} = \{\bar {f} _ {j}: \bar {X} _ {j + 1} \rightarrow \bar {X} _ {j} \}
$$

$$
(0 \leq j \leq a - 1)
$$

such that, if $\bar{f}^{*}(\mathfrak{R}_{\mathrm{S}}^{\prime}) = (^{a}\mathfrak{R}_{\mathrm{II}}^{\overline{N}}, ^{a}\bar{F}^{\prime})$, then $S_{\nu}(^{a}\mathfrak{R}_{\mathrm{II}}^{\overline{N}}) \cap {}^{a}\bar{F}$ is empty. We may assume that this last condition is not satisfied if we omit the last transformation $\bar{f}_{a-1}: \bar{X}_a \to \bar{X}_{a-1}$.

Let $^{b}\bar{\Re}$ be the transform of $^{0}\bar{\Re} = \Re_{\mathrm{S}}'$ on $\bar{X}_{b}(0 \leq b \leq a)$ by the succession

of monoidal transformations $\{\bar{f}_j\colon \bar{X}_{j + 1}\to \bar{X}_j\}$ for $0\leq j\leq b - 1$ . We now want to prove that there exists a permissible succession of monoidal transformations of $X_0' = X'$ for $\Re '$,

$$
\left\{f _ {k} ^ {\prime}: X _ {k + 1} ^ {\prime} \rightarrow X _ {k} ^ {\prime} \right\} \quad \text { for } 0 \leq k \leq k (a) - 1,
$$

such that, for  $0 \leq k(0) < k(1) < \cdots < k(a)$ ,

(1) $\bar{X}_j = (X_k')_{\mathrm{S}}$ for $k(j) \leq k \leq k(j + 1) - 1$,

(2) the center $B_k'$ of $f_k'$ in $X_k'$ induces the empty subscheme of $\bar{X}_j = (X_k')_S$ for $k(j) \leq k \leq k(j + 1) - 2$,

(3) the center $B_{k(j+1)-1}'$ of $f_{k(j+1)-1}'$ in $X_{k(j+1)-1}'$ induces the center $\bar{B}_j$ of $\bar{f}_j$ in $\bar{X}_j = (X_{k(j+1)-1}')_{\mathbf{S}}$.

Let $b$ be a non-negative integer $\leq a - 1$ and assume that we have found a permissible succession of monoidal transformations of $X'$ for $\mathfrak{R}'$,

$$
\{f _ {k} ^ {\prime}: X _ {k + 1} ^ {\prime} \rightarrow X _ {k} ^ {\prime} \}
$$

$$
\text { for } 0 \leq k \leq k (b) - 1,
$$

which has the properties (1)-(3) for all $j < b$. Let $^b\mathfrak{R}'$ be the transform of $\mathfrak{R}'$ on $X_{k(b)}'$ by this succession of monoidal transformations. We then have $\bar{X}_b = (X_{k(b)}')_\mathrm{S}$ and $^b\bar{\mathfrak{R}} = (^b\mathfrak{R}')_\mathrm{S}$. Let us write

$$
{ } ^ { b } \Re ^ { \prime } = ( { } ^ { b } \Re _ { \mathrm{II} } ^ { N } , { } ^ { b } F ^ { \prime } )
$$

with

$$
{ } ^ { b } \Re _ { \mathrm{II} } ^ { N } = \left( \begin{array} { c c c } { } ^ { b } E _ { 1 } ^ { \prime } , & \cdots , & { } ^ { b } E _ { \alpha ( b ) } ^ { \prime } \\ a _ { 1 } , & \cdots , & a _ { \alpha ( b ) } \end{array} \right| { } ^ { b } J ^ { \prime } , b)
$$

and

$$
{ } ^ { b } \bar { \mathfrak { R } } = ( { } ^ { b } \mathfrak { R } _ { \mathrm{II} } ^ { \overline { { N } } } , { } ^ { b } \bar { F } )
$$

with

$$
{ } ^ { b } \Re _ { \mathrm{II} } ^ { \bar { N } } = \left( \begin{array} { c c c } { } ^ { b } \bar { E } _ { 1 } , & \cdots , & { } ^ { b } \bar { E } _ { \alpha ( b ) } \\ a _ { 1 } , & \cdots , & a _ { \alpha ( b ) } \end{array} \right| { } ^ { b } \bar { J } ,   b)
$$

where  ${}^{b}\bar{F}=({}^{b}F')_{\mathrm{S}}$ ,  ${}^{b}\bar{E}_{i}=({}^{b}E_{i}')_{\mathrm{S}}$  and  ${}^{b}\bar{J}=({}^{b}J')_{\mathrm{S}}$ . Let  $\bar{B}_{b}$  be the center of the permissible monoidal transformation  $\bar{f}_{b}$  of  $\bar{X}_{b}$  for  ${}^{b}\Re$ . Let  $B''$  be the smallest irreducible subscheme of  $X_{k(b)}'$  such that  $\bar{B}_{b}=(B'')_{\mathrm{S}}$ . Let  $n''=\dim(B'')(<N)$ . Let us consider the following resolution datum with open restriction on  $X_{k(b)}'$

$$
{ } ^ { b } \Re ^ { \prime \prime } = ( \Re _ { I } ^ { N , n ^ { \prime \prime } } , U ^ { \prime \prime } )
$$

with

$$
\mathfrak {R} _ {\mathrm{I}} ^ {N, n ^ {\prime \prime}} = \left(\bigcup_ {i = 1} ^ {\alpha (b)} \left(^ {b} E _ {i} ^ {\prime}\right); B ^ {\prime \prime}\right)
$$

where  $U''$  is the open subset of  $B''$  consisting of those points at which  $R_{1}^{N,n''}$  is resolved. Note that  $(B'' - U'')_{\mathrm{S}}$  is empty, because  $\bar{f}_{b}$  with center

$(B'')_{\mathrm{S}}$ is permissible for $^{b}\bar{\mathfrak{R}} = (^{b}\mathfrak{R}')_{\mathrm{S}}$. Now, applying Theorem $\mathrm{I}_{2}^{N,n''}$ to the resolution datum $^{b}\mathfrak{R}'$, we get a permissible succession of monoidal transformations

$$
h = \left\{f _ {k} ^ {\prime}; X _ {k + 1} ^ {\prime} \rightarrow X _ {k} ^ {\prime} \right\} \quad \text { for } k (b) \leq k \leq k (b + 1) - 2
$$

of $X_{k(b)}'$ for ${}^b\mathfrak{R}''$, such that $h^*(\mathfrak{R}_1^N, n'')$ is resolved. We claim that the succession $h$ is permissible for ${}^b\mathfrak{R}'$. To prove this, let ${}_{k(b)}\mathfrak{R}'' = {}^b\mathfrak{R}''$ and ${}_k\mathfrak{R}''$ the transform of ${}^b\mathfrak{R}''$ on $X_k'(k(b) \leq k \leq k(b + 1) - 1)$ by the respective partial succession of the above $h$. We write

$$
{ } _ { k } \Re ^ { \prime \prime } = ( { } _ { k } \Re _ { \mathrm{I} } ^ { N , n ^ { \prime \prime } } , { } _ { k } U ^ { \prime \prime } )
$$

with

$$
{ } _ { k } \mathfrak { R } _ { \mathrm{I} } ^ { N , n ^ { \prime \prime } } = \left( \bigcup _ { i = 1 } ^ { \alpha _ { k } } ( { } _ { k } E _ { i } ^ { \prime } ) ; { } _ { k } B ^ { \prime \prime } \right) .
$$

In particular, when $k = k(b)$, $_{k(b)}\mathfrak{R}_{\mathrm{I}}^{N,n''} = \mathfrak{R}_{\mathrm{I}}^{N,n''}$, $\alpha_{k(b)} = \alpha (b)$, $_{k(b)}E_i' = {}^b E_i'$, $_{k(b)}B'' = B''$ and $_{k(b)}U'' = U''$. Let ${}_kC$ be the center of $f_k'$ for $k(b) \leq k \leq k(b + 1) - 2$. Let us denote by ${}_k\mathfrak{R}'$ the transform of ${}^b\mathfrak{R}'(k(b) \leq k \leq k(b + 1) - 1)$ by the respective partial succession of the above $h$, if this partial succession of $h$ is permissible for ${}^b\mathfrak{R}'$. In particular, we have $_{k(b)}\mathfrak{R}' = {}^b\mathfrak{R}'$. Suppose that we have

$$
{ } _ { k } \Re ^ { \prime } = ( { } _ { k } \Re _ { \mathrm{II} } ^ { N } , { } _ { k } F ^ { \prime } )
$$

with

$$
{ } _ { k } \Re _ { \mathrm{II} } ^ { N } = \left( \begin{array} { c c c } _ { k } E _ { 1 } ^ { \prime } , & \cdots , & _ { k } E _ { \alpha _ { k } } ^ { \prime } \\ a _ { 1 } , & \cdots , & a _ { \alpha _ { k } } \end{array} \bigg | _ { k } J ^ { \prime } , b \right)
$$

and that $_k B''$ is contained in $S_*(_{k} \mathfrak{R}_{\mathrm{II}}^N) = S_\nu(_k \mathfrak{R}_{\mathrm{II}}^N)$ as well as in $_k F'$. (This is certainly the case of $k(b) = k$.) The monoidal transformation $f_k'$ with center $_k C$ (which is permissible for $_k \mathfrak{R}'$) is clearly permissible for $_k \mathfrak{R}'$, because $_k C \subset _k B''$. Since $_k C \neq _k B''$ (for $_k U''$ is not empty), $_{k+1} B''$ must be contained in $S_\nu(_{k+1} \mathfrak{R}_{\mathrm{II}}^N)$, and hence $S_\nu(_{k+1} \mathfrak{R}_{\mathrm{II}}^N) = S_*(_{k+1} \mathfrak{R}_{\mathrm{II}}^N)$. Clearly, $_{k+1} \mathfrak{R}'$ can be written in the same way as $_k \mathfrak{R}'$ was written above. We thus conclude that $h$ is permissible for $^b \mathfrak{R}'$ as well as for $^b \mathfrak{R}'$, and moreover we can see, for the same reason, that if $B_* = _k B$ with $k = k(b + 1) - 1$, then the monoidal transformation

$$
f _ {k (b + 1) - 1} ^ {\prime}: X _ {k (b + 1)} ^ {\prime} \rightarrow X _ {k (b + 1) - 1} ^ {\prime}
$$

with center  $B_{*}$  is permissible for  $_{k}R'$  with  $k = k(b + 1) - 1$ . Thus we get a permissible succession of monoidal transformations of  $X'$  for  $R'$ ,

$$
\{f _ {k} ^ {\prime}: X _ {k + 1} ^ {\prime} \rightarrow X _ {k} ^ {\prime} \}
$$

$$
(0 \leq k \leq k (b + 1) - 1)
$$

which has the properties (1)-(3) for all $j \leq b$. q.e.d.

PROPOSITION 4 (Localization theorem on $\mathfrak{R}_{\mathrm{II}}^{N}$). Let $N$ be a positive integer. Let us assume that Theorems $\Pi_2^{N'}$ with $N' < N$ and Theorems $\mathbf{I}_2^{N,n}$ with $n < N$ are verified. Let $\mathfrak{R}_{\mathrm{II}}^N = \left( \begin{array}{cc} E_1, & \cdots, E_\alpha \\ a_1, & \cdots, a_\alpha \end{array} \bigg| J, b \right)$ be a resolution datum (without restriction) on a non-singular irreducible algebraic scheme $X$. We assume that $\nu(\mathfrak{R}_{\mathrm{II}}^N) > 0$. Then there exists a permissible succession of monoidal transformations of $X$ for $\mathfrak{R}_{\mathrm{II}}^N$, say $f: X' \to X$, such that, if $\nu = \nu(\mathfrak{R}_{\mathrm{II}}^N)$, then $f(S_{\nu}(f^*(\mathfrak{R}_{\mathrm{II}}^N)))$ is a finite set of points (at most) of $X$ at which $X$ has dimension $N$.

PROOF. The proof is entirely similar to that of Proposition 3.

## 2. Preparation on resolution data ( $R_{I}^{N,n}$ , U)

LEMMA 3. Let X be a non-singular irreducible algebraic scheme, W and F non-singular irreducible subschemes of X such that  $F \subseteq W$ . Let  $E_{1}, \cdots, E_{\alpha}$  be non-singular irreducible subschemes of codimension 1 of X such that:

(i)  $E_{1} \cup \cdots \cup E_{\alpha}$  has only normal crossings,

(ii) $E_{1} \cup \dots \cup E_{\alpha}$ has only normal crossings with $F$, and

(iii) any $E_{j}$ containing $F$ contains $W$.

Then  $E_{1} \cup \cdots \cup E_{\alpha}$  has only normal crossings with W at every point of F.

PROOF. Let x be any point of F. Let R be the local ring of X at x, P the prime ideal of W in R, and Q the prime ideal of F in R. We arrange the indices of the  $E_{j}$  in such a way that  $W \subseteq E_{j}$  for  $1 \leq j \leq \beta$  and  $W \not\subseteq E_{j}$  for  $j > \beta$, where  $0 \leq \beta \leq \alpha$. To prove that  $E_{1} \cup \cdots \cup E_{\alpha}$  has only normal crossings with W at x, we may assume that  $x \in E_{j}$  for  $1 \leq j \leq \alpha$. Let  $z_{j}$  be an element of R which generates the prime ideal of  $E_{j}$  in R. By (i),  $(z_{1}, \cdots, z_{\beta})$  can be extended to a minimal base of P, say  $(z_{1}, \cdots, z_{\beta}, w_{1}, \cdots, w_{s})$  where  $\beta + s = \text{the codimension of } W$  in X. Since W is non-singular,  $(z_{1}, \cdots, z_{\beta}, w_{1}, \cdots, w_{s})$  can be extended to a minimal base of Q, say  $(z_{1}, \cdots, z_{\beta}, w_{1}, \cdots, w_{s}, y_{1}, \cdots, y_{t})$. Since F is non-singular, (ii) and (iii) imply that  $(z_{1}, \cdots, z_{\beta}, w_{1}, \cdots, w_{s}, y_{1}, \cdots, y_{t}, z_{\beta+1}, \cdots, z_{\alpha})$  can be extended to a regular system of parameters of R. It follows that  $E_{1} \cup \cdots \cup E_{\alpha}$  has only normal crossings with W at x, i.e., at every point of F. q.e.d.

LEMMA 4. Let X be a non-singular irreducible algebraic scheme, W a non-singular irreducible subscheme of X, and B a non-singular irreducible subscheme of W. Let  $E_{1}, \cdots, E_{\alpha}$  be non-singular irreducible subschemes of codimension 1 of X such that

(i)  $E_{1} \cup \cdots \cup E_{\alpha}$  has only normal crossings,

(ii)  $E_{1} \cup \cdots \cup E_{\alpha}$  has only normal crossings with W as well as with B. Let  $f: X' \to X$  be the monoidal transformation of X with center B. Let  $E_{j}'(1 \leq j \leq \alpha)$ ,  $W'$  be the strict transforms of  $E_{j}$ , W respectively, and  $E'$  the total transform  $f^{-1}(B)$  of B on  $X'$ . Then  $E_{1}' \cup \cdots \cup E_{\alpha}' \cup E'$  has only normal crossings  $W'$  as well as with  $W' \cap E'$ .

PROOF. We may assume that $W \neq B$. (See Remark 1, § 1, Ch. I.) If $x' \in W' - W' \cap E'$, then morphism $f$ is locally at $x'$ an isomorphism. Therefore, we have only to consider the case in which $x' \in W' \cap E'$ to prove that $E_1' \cup \cdots \cup E_\alpha' \cup E'$ has only normal crossings with $W'$ as well as with $W' \cap E'$ at $x'$. Now, let $x = f(x')$. Let $\mathbf{R}$ (resp. $\mathbf{R}'$) be the local ring of $X$ at $x$ (resp. $X'$ at $x'$). To prove that $E_1' \cup \cdots \cup E_\alpha' \cup E'$ has only normal crossings with $W'$ as well as with $W' \cap E'$ at $x'$, we may assume that $x \in E_j$ for all $j(1 \leq j \leq \alpha)$. Let $\mathbf{P}$ (resp. $\mathbf{Q}$) be the prime ideal of $B$ (resp. $W$) in $\mathbf{R}$. By arranging the indices of the $E_j$, if necessary, we may assume that $x' \in E_j'$ for $1 \leq j \leq c$ and $x' \notin E_j'$ for $j > c$, that $E_j \supseteq W$ for $1 \leq j \leq a$ but $E_j \not\supseteq W$ for $a < j \leq c$, and that $E_j \supseteq B$ for $1 \leq j \leq b$ but $E_j \not\supseteq B$ for $b < j \leq c$, where $1 \leq a \leq b \leq c \leq \alpha$. Let $z_j(1 \leq j \leq c)$ be an element of $\mathbf{R}$ which generates the prime ideal of $E_j$ in $\mathbf{R}$. Let us take an element $w \in \mathbf{P}$ such that $(w)\mathbf{R}' = \mathbf{P}\mathbf{R}'$. Then $z_j' = z_j / w(1 \leq j \leq b)$ are non-units in $\mathbf{R}'$ and generates the prime ideal of $E_j'(1 \leq j \leq b)$ in $\mathbf{R}'$. If $Q'$ is the prime ideal of $W'$ in $R'$, then $R'/Q'$ is regular, and $(z_1',\cdots,z_a')$ can be extended to a minimal base of $Q'$. Moreover, if $\overline{z}_j'(a + 1\leq j\leq b)$, $\overline{z}_j(b + 1\leq j\leq c)$ and $\overline{w}$ denote the residue classes of $z_j'(a + 1\leq j\leq b)$, $z_j(b + 1\leq j\leq c)$ and $w$ in $R'/Q'$ respectively, then $(\overline{z}_{a+1}',\cdots,\overline{z}_b',\overline{z}_{b+1},\cdots,\overline{z}_c,\overline{w})$ can be extended to a regular system of parameters of $R'/Q'$. The conclusion of Lemma 4 follows immediately. q.e.d.

LEMMA 5. Let X be a non-singular irreducible algebraic scheme, W a non-singular irreducible subscheme of X, and E a non-singular irreducible subscheme of codimension 1 of X such that E does not contain W. Let F be a reduced irreducible component of  $W \cap E$ , and assume that F is non-singular. Let  $f: X' \to X$  be the monoidal transformation of X with center F, and let  $E'$  and  $W'$  be the strict transforms of E and W on  $X'$  respectively. Then f induces an isomorphism  $\bar{f}$  of  $W'$  to W. If  $F_1 (=F)$ ,  $\cdots$ ,  $F_m$  are the reduced irreducible components of  $W \cap E$ , then  $\text{red}(W' \cap E')$  is either  $\bigcup_{j=2}^{m} \bar{f}^{-1}(F_j)$  or  $\bigcup_{j=1}^{m} \bar{f}^{-1}(F_j)$ . Let  $F' = \bar{f}^{-1}(F)$ . If  $F' \subseteq W' \cap E'$ , then we take the monoidal transformation  $f': X'' \to X'$  with center  $F'$ . Let  $\bar{f}'$  be the induced isomorphism of the strict transform  $W''$  of  $W'$  (on  $X''$ ) to  $W'$ . If  $\bar{f}'^{-1}(F') \subseteq W'' \cap E''$  where  $E''$  is the strict transform of  $E'$  on  $X''$ , we take the monoidal transfor-

mation of $X''$ with center $F'' = \bar{f}'^{-1}(F')$ and so on. Then this process ends up by a finite number of steps.

PROOF. The monoidal transformation $f \colon X' \to X$ induces in $W$ the monoidal transformation of $W$ with center $F$, which is clearly an isomorphism because $W$ is non-singular and $F$ has codimension 1 in $W$. $W' \cap E'$ is everywhere of codimension 1 on the non-singular irreducible algebraic scheme $W'$, and $\text{red}(W' \cap E') \subseteq (\bigcup_{j=2}^{m} \bar{f}^{-1}(F_j)) \cup (W' \cap f^{-1}(F)) = \bigcup_{j=1}^{m} \bar{f}^{-1}(F_j)$. Therefore either $\text{red}(W' \cap E') = \bigcup_{j=2}^{m} \bar{f}^{-1}(F_j)$ or $= \bigcup_{j=1}^{m} \bar{f}^{-1}(F_j)$. To prove the last statement, let $\{f^{(i)} : X^{(i+1)} \to X^{(i)}\}$ be any sequence of monoidal transformations with center $F^{(i)}$ in $X^{(i)}$ where $X^{(0)} = X$, $F^{(0)} = F$, and $F^{(i+1)} = \text{the image of } F^{(i)}$ in the strict transform $W^{(i+1)}$ of $W^{(0)} (= W)$ on $X^{(i+1)} (i = 0, 1, 2, \cdots)$. Let $E^{(i+1)}$ be the strict transform of $E^{(0)} (= E)$ on $X^{(i+1)}$. We want to show that $E^{(i)} \cap W^{(i)}$ does not contain $F^{(i)}$ for sufficiently large $i$. Let $R_i$ be the local ring of $X^{(i)}$ at the generic point of $F^{(i)}$, $M_i$ the maximal ideal of $R_i$ and $P_i$ the prime ideal of $W^{(i)}$ in $R_i (i = 0, 1, 2, \cdots)$. Let $w$ be an element of $M_0$ which generates the ideal $E^{(0)}$ in $R_0$. Let $(z_1, \cdots, z_r)$ be a minimal base of the prime ideal $P_0$ in $R_0$ and $(z_1, \cdots, z_r, y)$ a regular system of parameters of $R_0$. Let $z_j^{(i)} = y^{-i} z_j (1 \leq j \leq r)$ for $i = 0, 1, 2, \cdots$. Then we can easily see that $(z_1^{(i)}, \cdots, z_r^{(i)}, y)$ is a regular system of parameters of $R_i$. Let $w^{(i)} = y^{-i} w$ for $i = 0, 1, 2, \cdots$. Then, as long as $E^{(i)}$ contains $F^{(i)}$, $w^{(i)}$ is an element of $M_i$ and it generates the prime ideal of $E^{(i)}$ in $R_i$. Since $E$ does not contain $W$, $w$ is not contained in $P_0$, hence, we have a positive integer $v$ such that $P_0 + (y^v) R_0$ contains $w$ but $P_0 + (y^{\nu+1}) R_0$ does not. Then one can easily see that $w^{(\nu)}$ is a unit of $R_\nu$. In fact, $w$ can be written in the form $w = \sum a_j z_j + uy^\nu$ with $a_j \in R_0 (1 \leq j \leq r)$ and with a unit $u$ of $R_0$. Then $w^{(\nu)} = \sum a_j z_j^{(\nu)} + u$, which is clearly a unit of $R_\nu$. q.e.d.

PROPOSITION 5 (Preparation theorem on $(\Re_{\mathrm{I}}^{N,n}, U)$).

Let $(\mathfrak{R}_{1}^{N,n}, U)$ be a resolution datum of the type $\mathfrak{R}_{1}^{N,n}$ with open restriction U on a non-singular irreducible algebraic scheme X, where $N > n \geq 0$. Let $\mathfrak{R}_{1}^{N,n} = (\bigcup_{i=1}^{\alpha} E_{i}; V_{1}, \cdots, V_{\beta}; W)$ and let us assume that $\alpha \geq 1$. Suppose that Theorems $I_{1}^{N',n'}$ with $n' < N' \leq N$ and $n' \leq n$, and Theorems $I_{2}^{N',n''}$ with $n'' < n$, are verified. Then there exists a permissible succession of monoidal transformations $f: X' \to X$ for $(\mathfrak{R}_{1}^{N,n}, U)$ such that the transform $f^{*}(\mathfrak{R}_{1}^{N,n}, U) = (f^{*}(\mathfrak{R}_{1}^{N,n}), U')$ with $f^{*}(\mathfrak{R}_{1}^{N,n}) = (\bigcup_{i=1}^{\alpha'} E_{i}', V_{1}', \cdots, V_{\beta}'; W')$ has the following property: There exists an open subset $\tilde{U}'$ of $W'$ such that

(i) $\tilde{U}^{\prime}\supseteq U^{\prime}$ and $f^{*}(\mathfrak{R}_{\mathrm{I}}^{N,n})$ is resolved at every point of $\tilde{U}^{\prime}$, and

(ii) if $W_1'$ is any irreducible component of $W'$, either $E_1' \supseteq W_1'$ or

$E_1'\cap W_1'\subseteq \tilde{U}'$ , where $E_1^\prime$ denotes the strict transform of $E_{1}$ on $X^{\prime}$

PROOF. Let $W_1, \cdots, W_a$ be those irreducible components of $W$ which are not contained in $E_1$, and $W_{a+1}, \cdots, W_b$ those irreducible components of $W$ which are contained in $E_1$. Let $W_* = W_1 \cup \cdots \cup W_a$. Let $F_1, \cdots, F_c$ be those reduced irreducible components of $W_* \cap E_1$ which have non-empty intersection with $U$. Let $F = \bigcup_{i=1}^{c} F_i$. Since $\Re_1^{N,n}$ is resolved at every point of $U$, $U$ consists of only simple points of $W$ and in particular it does not contain any common points of any two irreducible components of $W$. Moreover, the resolution datum on $X$

$$
\mathfrak {R} _ {\mathrm{I}} ^ {N, \overline {{{n}}}} = \left(\bigcup_ {i = 1} ^ {\alpha} E _ {i}; V _ {1}, \dots , V _ {\beta}, W; F\right)
$$

where  $\bar{n} = \dim F$ , is resolved at every point of  $F \cap U$ . (See Corollary 1 of Proposition 1, § 1, Ch. II.) We see that  $F \cap U$  is an open dense subset of F. We shall consider the resolution datum  $(\mathfrak{R}_{\mathrm{I}}^{N,\bar{n}}, F \cap U)$  on X with open restriction  $F \cap U$ . As is easily seen, a permissible succession of monoidal transformations of X for  $(\mathfrak{R}_{\mathrm{I}}^{N,\bar{n}}, F \cap U)$  is such a succession for  $(\mathfrak{R}_{\mathrm{I}}^{N,n}, U)$ . Since  $\bar{n} < n$ , we can apply Theorem  $I_{2}^{N,\bar{n}}$  to  $(\mathfrak{R}_{\mathrm{I}}^{N,\bar{n}}, F \cap U)$  and find a permissible succession of monoidal transformations of X for  $(\mathfrak{R}_{\mathrm{I}}^{N,\bar{n}}, F \cap U)$ , say  $f: X' \to X$ , such that  $f^{*}(\mathfrak{R}_{\mathrm{I}}^{N,\bar{n}})$  is resolved at every point of the strict transform  $F'$  of F on  $X'$ . Let  $f^{*}(\mathfrak{R}_{\mathrm{I}}^{N,n}, U) = (f^{*}(\mathfrak{R}_{\mathrm{I}}^{N,n}), U')$  with  $f^{*}(\mathfrak{R}_{\mathrm{I}}^{N,n}) = (\bigcup_{i=1}^{\alpha'} E_{i;} V_{1}', \cdots, V_{\beta}'; W')$ . Then  $f^{*}(\mathfrak{R}_{\mathrm{I}}^{N,\bar{n}}, U \cap F) = (f^{*}(\mathfrak{R}_{\mathrm{I}}^{N,\bar{n}}), U' \cap F')$  and  $f^{*}(\mathfrak{R}_{\mathrm{I}}^{N,\bar{n}}) = (\bigcup_{i=1}^{\alpha'} E_{i;} V_{1}', \cdots, V_{\beta}', W'; F')$ . Since  $f^{*}(\mathfrak{R}_{\mathrm{I}}^{N,\bar{n}})$  is resolved at every point of  $F'$ ,  $F'$  is non-singular and  $V_{1}', \cdots, V_{\beta}', W'$  are all normally flat along  $F'$ . In particular, by Corollary 4 of Proposition 1, § 1, Ch. II, every point of  $F'$  must be a simple point of  $W'$ . Moreover, by Corollary of Theorem 3, § 3, Ch. II, all the  $V_{j}'$  are normally flat along  $W'$  at every point of  $F'$ . On the other hand, since  $R_{1}^{N,n}$  is resolved at every point of U, for  $i \geq 2$  and j,  $E_{i}$  containing  $F_{j}$  must contain the unique irreducible component of W containing  $F_{j}$ . Since the above morphism f induces an isomorphism of  $X' - f^{-1}(W - U)$  onto X - (W - U), it follows that for  $i \geq 2$ ,  $E_{i}'$  containing an irreducible component  $F_{j}'$  of  $F'$  must contain the unique irreducible component of  $W'$  containing  $F_{j}'$ . In virtue of Lemma 3, the resolution datum on  $X'$

$$
\left(\bigcup_ {i = 2} ^ {\alpha^ {\prime}} E _ {i} ^ {\prime}; V _ {1} ^ {\prime}, \dots , V _ {\beta} ^ {\prime}; W ^ {\prime}\right)
$$

must be resolved at every point of  $F'$ .

Thus we may assume, without any loss of generality, that the given resolution datum  $(\mathfrak{R}_{\mathrm{I}}^{N,n}, U)$  is such that

(1) if  $W_{*}$  is the union of those irreducible components of W which are not contained in  $E_{1}$  and if  $F_{1}, \cdots, F_{c}$  are those reduced irreducible

components of  $W_{*} \cap E_{1}$  which have non-empty intersection with U, then  $F = F_{1} \cup \cdots \cup F_{c}$  is a disjoint union of non-singular schemes  $F_{1}, \cdots, F_{c}$  and  $\bigcup_{i=1}^{\alpha} E_{i}$  has only normal crossings with F,

(2) there exists an open subset  $\tilde{U}$  of W which contains U and F, and such that the resolution datum  $(\bigcup_{i=2}^{\alpha} E_{i}, V_{1}, \cdots, V_{\beta}; W)$  is resolved at every point of  $\tilde{U}$ .

Let us consider the following resolution datum  $R_{1}^{N,\bar{n}}$  with open restriction  $U \cap F$  on X:

$$
\mathfrak {R} _ {\mathrm{I}} ^ {N, \overline {{n}}} = \left(\bigcup_ {i = 1} ^ {\alpha} E _ {i}; V _ {1}, \dots , V _ {\beta}, W, W _ {*} \cap E _ {1}; F\right).
$$

By Theorem  $I_{2}^{N,\bar{n}}$ , we have a permissible succession of monoidal transformations of X for  $(\Re_{1}^{N,\bar{n}}, U \cap F)$ , say  $f: X' \to X$ , such that  $f^{*}(\Re_{1}^{N,\bar{n}})$  is resolved at every point of the strict transform  $F'$  of F on  $X'$ . It is clear that f is permissible for  $(\Re_{1}^{N,n}, U)$ . Let us write

$$
f ^ {*} \left(\mathfrak {R} _ {1} ^ {N, n}\right) = \left(\bigcup_ {i = 1} ^ {\alpha^ {\prime}} E _ {i} ^ {\prime}; V _ {1} ^ {\prime}, \dots , V _ {\beta} ^ {\prime}; W ^ {\prime}\right)
$$

and

$$
f ^ {*} (\mathfrak {R} _ {\mathrm{I}} ^ {N, n}, U) = \left(f ^ {*} (\mathfrak {R} _ {\mathrm{I}} ^ {N, n}), U ^ {\prime}\right).
$$

Let $(W_{*}\cap E_{1})'$ be the strict transform of $W_{*}\cap E_{1}$ on $X'$. Then we can write

$$
f ^ {*} \left(\Re_ {1} ^ {N, \overline {{{n}}}}\right) = \left(\bigcup_ {i = 1} ^ {\alpha^ {\prime}} E _ {i} ^ {\prime}; V _ {1} ^ {\prime}, \dots , V _ {\beta} ^ {\prime}, W ^ {\prime}, \left(W _ {*} \cap E _ {1}\right) ^ {\prime}; F ^ {\prime}\right)
$$

and

$$
f ^ {*} \left(\Re_ {I} ^ {N, \overline {{n}}}, U \cap F\right) = \left(f ^ {*} \left(\Re_ {I} ^ {N, \overline {{n}}}\right), U ^ {\prime} \cap F ^ {\prime}\right).
$$

Let $\tilde{U}'$ be the open subset $f^{-1}(\tilde{U}) \cap W'$ of $W'$ where $\tilde{U}$ is the open subset of $W$ in (2). Then in view of Lemma 4 of this section and Corollary 2 of Theorem 5, § 6, Ch. III, the resolution datum

$$
\left(\bigcup_ {i = 2} ^ {\alpha^ {\prime}} E _ {i} ^ {\prime}; V _ {1} ^ {\prime}, \dots , V _ {\beta} ^ {\prime}; W ^ {\prime}\right)
$$

is resolved at every point of $\tilde{U}'$. Moreover, as is essily seen, if $W_*$ denotes the union of those irreducible components of $W'$ which are not contained in $E_1'$ then $W_*' \cap E_1' \cong (W_* \cap E_1)'$ and every reduced irreducible component of $W_*' \cap E_1'$ is either contained in $(W_* \cap E_1)'$ or contained in $W' \cap E_j'$ with $j$ such that $\alpha < j \leq \alpha'$. Since $f^*(\mathfrak{R}_1^{N,\overline{n}})$ is resolved at every point of $F'$, $(W_* \cap E_1)'$ is normally flat along $F'$, hence, every component of $(W_* \cap E_1)'$ is either in $F'$ or has empty intersection with $F'$. Therefore, every irreducible component of $W_*' \cap E_1'$ is either a reduced irreducible component of $F'$ or such of $W' \cap E_j'$ with $j(\alpha < j \leq \alpha')$, provided it has non-empty intersection with $F'$. We can prove that $W' \cap E_j'$ for $\alpha < j \leq \alpha'$ are non-singular irreducible subschemes of $X'$ and contained in $\tilde{U}'$.

Thus, without any loss of generality, we may assume that the given resolution datum  $(\mathfrak{R}_{\mathrm{I}}^{N,n}, U)$  has the following property, in addition to (1) and (2):

(3) if $G$ is any reduced irreducible component of $W_{*} \cap E_{1}$ which is not in $F$ and has non-empty intersection with $F$, then $G$ is contained in $\tilde{U}$ and of the form $W \cap E_{j}$ with $j \geq 2$, hence, non-singular.

If $G$ is any reduced irreducible component of $W_{*} \cap E_{1}$ as above, (2) and (3) imply immediately that the monoidal transformation $f: X' \to X$ with center $G$ is permissible for the resolution datum ($\bigcup_{i=2}^{\alpha} E_{i}; V_{1}, \cdots, V_{\beta}; W$), hence, for $(\Re_{1}^{N,n}, U)$. Moreover, the conditions (1), (2) and (3) remain to be satisfied if we replace $(\Re_{1}^{N,n}, U)$ by $f^{*}(\Re_{1}^{N,n}, U)$, and $\tilde{U}$ by $f^{-1}(\tilde{U}) \cap (\text{the strict transform of } W \text{ on } X')$. Therefore, by Lemma 5, we may assume that

(3)\* Every reduced irreducible component of $W_* \cap E_1$ is either contained in $F$ (hence, it is one of the $F_j$) or has empty intersection with $F$. Then, by replacing $\tilde{U}$ by $\tilde{U} - ((W_* \cap E_1) - F)$, we may assume that

(3)\*\* $\tilde{U} \cap W_{*} \cap E_{1} = F$, where $\tilde{U} \cap W_{*}$ is an open dense subset of $W_{*}$. It follows from (1), (2) and (3)\*\*, with help of Lemma 3, that

(4)  $\Re_{1}^{N,n} = (\bigcup_{i=1}^{\alpha} E_i; V_1, \cdots, V_\beta; W)$  is resolved at every point of  $\tilde{U} \cap W_*$ .

(Here, we must use the fact that $\mathfrak{R}_i^{N,n}$ is resolved at every generic point of $F$.) Now, let us consider the following resolution datum on the nonsingular irreducible algebraic scheme $X - F$, with $N^* = \dim (X - F)$ and $n^* = \dim (W_* - F)$;

$$
\Re_ {1} ^ {N ^ {*}, n ^ {*}} = \left(\bigcup_ {i = 2} ^ {\alpha} (E _ {i} - F); V _ {1} - F, \dots , V _ {\beta} - F, W - F; W _ {*} - F\right)
$$

with closed restriction $E_1 - F$. Note that $(E_1 - F) \cap (W_* - F)$ is entirely contained in $W_* - \tilde{U}$ while $F$ is entirely contained in $\tilde{U}$. Therefore, the center of any permissible monoidal transformation for $(\mathfrak{R}_1^{N^*,n^*}, E_1 - F)$ is contained in $W_* - \tilde{U}$ and closed not only in $W_* - F$ but also in $W_*$. It follows that any permissible monoidal transformation for $(\mathfrak{R}_1^{N^*,n^*}, E_1 - F)$ is canonically induced by a permissible monoidal transformation for $(\mathfrak{R}_1^{N,n}, U)$, and that this permissible monoidal transformation for $(\mathfrak{R}_1^{N,n}, U)$ does not affect the properties (1), (2), (3)\*\* and (4) of $(\mathfrak{R}_1^{N,n}, U)$. Thus, by Theorem $I_1^{N^*,n^*}$, we may assume that

(5) $E_{1} - F$ and $W_{*} - F$ has empty intersection.

$$
(5) ^ {*} E _ {1} \cap W _ {*} = F \subset \tilde {U}.
$$

By (1), (2) and (4), $\mathfrak{R}_1^{N,n}$ is resolved at every point of $\tilde{U}$ ($\tilde{U}$ is an open subset of $W$ containing $U$), and by (1) and (5)$^*$ every irreducible com-

ponent  $W_{1}$  of W is either contained in  $E_{1}$  or such that  $E_{1} \cap W_{1} \subset \tilde{U}$ . q.e.d.

## 3. Proofs of the implications (A) and (B)

In this section, we shall give proofs to the implications (A) and (B) which were announced in Ch. I, § 2.

We first introduce certain symbols which play important roles in the proofs.

Let $X$ be a non-singular irreducible algebraic scheme. Let $V$ be a subscheme of $X$ and $x$ a point of $X$. Let $S$ be the local ring of $X$ at $x$, which is a regular local ring, and $J$ the ideal of $V$ in $S$. Then we denote by $\nu_{x}^{*}(V / X)$ the numerical character $\nu^{*}(J) = (\nu^{(1)}(J), \nu^{(2)}(J), \cdots)$ of the ideal $J$ in $S$, which was defined in § 1 of Ch. III, and by $\tau_{x}^{*}(V / X)$ the numerical character $\tau^{*}(J) = (\tau^{(1)}(J), \cdots, \tau^{(t)}(J))$ with $t = t(J)$ of the ideal $J$ in $S$, which was defined in § 3 of Ch. III. We shall also denote by $\tau_{x}^{(i)}(V / X)$ the integer $\tau^{(i)}(J)$ for $1 \leq j \leq t(J)$. We note that $\nu^{*}(J) = (0, \infty, \infty, \cdots)$ if and only if $x \notin V$, in which case $t(J) = 1$ and $\tau^{(1)}(J) = 0$. If $(V_{1}, \cdots, V_{\beta})$ is a system of subschemes of $X$, then we shall write

$$
\nu_ {x} ^ {*} \left(V _ {1}, \dots , V _ {\beta} / X\right) \quad \text { for } \left(\nu_ {x} ^ {*} \left(V _ {1} / X\right), \dots , \nu_ {x} ^ {*} \left(V _ {\beta} / X\right)\right)
$$

and

$$
\tau_ {x} ^ {*} \left(V _ {1}, \dots , V _ {\beta} / X\right) \quad \text { for } \left(\tau_ {x} ^ {*} \left(V _ {1} / X\right), \dots , \tau_ {x} ^ {*} \left(V _ {\beta} / X\right)\right).
$$

Let $f: X' \to X$ be a finite succession of monoidal transformations with non-singular centers, and $V_j'$ the strict transform of $V_j$ on $X'$ for $1 \leq j \leq \beta$. Let $x'$ be a point of $X'$ and $x = f(x') \in X$. Then by the inequality:

$$
\nu_ {x} ^ {*} (V _ {1}, \dots , V _ {\beta} / X) > \nu_ {x ^ {\prime}} ^ {*} (V _ {1} ^ {\prime}, \dots , V _ {\beta} ^ {\prime} / X ^ {\prime})
$$

we shall mean that

$$
\nu_ {x} ^ {*} (V _ {j} / X) \geq \nu_ {x ^ {\prime}} ^ {*} (V _ {j} ^ {\prime} / X ^ {\prime})
$$

(Definition 2, § 1, Ch. III.)

for all  $j(1 \leq j \leq \beta)$  where the strict inequality occurs for at least one j. And similarly, by the inequality:

$$
\tau_ {x} ^ {*} \left(V _ {1}, \dots , V _ {\beta} / X\right) <   \tau_ {x ^ {\prime}} ^ {*} \left(V _ {1} ^ {\prime}, \dots , V _ {\beta} ^ {\prime} / X ^ {\prime}\right)
$$

we shall mean that

$$
\tau_ {x} ^ {(i)} (V _ {j} / X) \leq \tau_ {x ^ {\prime}} ^ {(i)} (V _ {j} ^ {\prime} / X ^ {\prime})
$$

for all $i$ and all $j(1 \leq j \leq \beta)$ where the strict inequality occurs for at least one pair $(i, j)$.

Let $N$ denote the dimension of $X$ and let $\Re$ be any resolution datum on $X$ of the form either $\Re = (\Re_{\mathrm{I}}^{N,n}, F)$ or $\Re = (\Re_{\mathrm{I}}^{N,n}, U)$, where

$$
\mathfrak {R} _ {\mathrm{I}} ^ {N, n} = \left(\bigcup_ {i = 1} ^ {\alpha} E _ {i}; V _ {1}, \dots , V _ {\beta}; W\right).
$$

We shall assume that  $N > n \geq 0$ . We want to prove the following Theorems A and B:

THEOREM A. Let $\Re = (\mathfrak{R}_1^{N,n}, F)$ be the given resolution datum on $X$. Assume that Theorems $\mathrm{I}_1^{N',n'}$ with $n' < N' < N$, Theorems $\mathrm{I}_2^{N,n''}$ with $n'' < n$, and Theorems $\mathrm{II}_2^{N'}$ with $N' < N$ are all verified. Then we can find a permissible succession of monoidal transformations of $X$ for the datum $\Re$, say $f: X' \to X$, such that $W' \cap F'$ is empty, where

$$
f ^ {*} (\mathfrak {R}) = \left(f ^ {*} (\mathfrak {R} _ {\mathrm{I}} ^ {N, n}), F ^ {\prime}\right)
$$

with

$$
f ^ {*} \left(\mathfrak {R} _ {\mathrm{I}} ^ {N, n}\right) = \left(\bigcup_ {i = 1} ^ {\alpha^ {\prime}} E _ {i} ^ {\prime}; V _ {1} ^ {\prime}, \dots , V _ {\beta} ^ {\prime}; W ^ {\prime}\right).
$$

THEOREM B. Let $\Re = (\mathfrak{R}_1^{N,n}, U)$ be the given resolution datum on $X$. Assume that Theorems $\mathrm{I}_2^{N',n'}$ with $n' < N' < N$, Theorems $\mathrm{I}_2^{N',n''}$ with $n'' < n$, Theorems $\mathrm{I}_1^{N*,n*}$ with $n^* < N^* \leq N$ and $n^* \leq n$, and Theorems $\mathrm{II}_2^{N'}$ with $N' < N$ are all verified. Then we can find a permissible succession of monoidal transformations of $X$ for the datum $\Re$, say $f: X' \to X$, such that $f^*(\mathfrak{R}_1^{N,n})$ is resolved at every point of $W'$ where $W'$ is as in Theorem A.

To prove Theorems A and B, we introduce the symbol $S(\mathfrak{R})$ which is defined as follows: If $\mathfrak{R} = (\mathfrak{R}_1^{N,n}, F)$, then $S(\mathfrak{R})$ denotes the set of points of $W \cap F$, and if $\mathfrak{R} = (\mathfrak{R}_1^{N,n}, U)$ then $S(\mathfrak{R})$ denotes the set of points of $W$ at which the datum $\mathfrak{R}_1^{N,n}$ is not resolved. We shall first prove the following Theorems A\* and B\* which are a priori weaker than the above Theorems A and B respectively.

THEOREM A\*. Let the notation and assumptions be the same as in Theorem A. Then there exists a permissible succession of monoidal transformations of X for R, say  $f: X' \to X$ , such that if  $\Re' = f^*(\Re)$  and  $f^*(\Re_{1}^{N,n}) = (\bigcup_{i=1}^{\alpha'} E_i'; V_1', \cdots, V_\beta; W')$ , we have

(i) $f(S(\mathfrak{R}'))$ is at most a finite number of points of $X$ at which $X$ has dimension $N$, and

(ii) for every $x' \in S(\mathfrak{R}')$ at which $X'$ has dimension $N$, we have either

(a) $\nu_{x'}^{*}(V_{1}',\dots ,V_{\beta}',W'/X')<\nu_{x}^{*}(V_{1},\dots,V_{\beta},W/X),or$

$$
\nu_ {x ^ {\prime}} ^ {*} \left(V _ {1} ^ {\prime}, \dots , V _ {\beta} ^ {\prime}, W ^ {\prime} / X ^ {\prime}\right) = \nu_ {x} ^ {*} \left(V _ {1}, \dots , V _ {\beta}, W / X\right) \tag {b}
$$

and

$$
\tau_ {x ^ {\prime}} ^ {*} \left(V _ {1} ^ {\prime}, \dots , V _ {\beta} ^ {\prime}, W ^ {\prime} / X ^ {\prime}\right) > \tau_ {x} ^ {*} \left(V _ {1}, \dots , V _ {\beta}, W / X\right)
$$

where $x = f(x')$.

THEOREM B\*. Let the notation and the assumptions be the same as in Theorem B. Then there exists a permissible succession of monoidal transformations of X for R which has the same properties (i) and (ii) as in

Theorem A\*.

The notation being as in Theorems A\* and B\*, a permissible succession of monoidal transformations of X for the given resolution datum R will be called an effective modification of X for R if it has the properties (i) and (ii) of Theorems A\* and B\* respectively.

We first claim that Theorems A and B follow Theorems A\* and B\* respectively. In other words, we have

LEMMA (AB. 1). Let $X$ and $\Re$ be as above. Let $\{f_i: X_{i+1} \to X_i\}$ be any sequence of effective modifications of $X_i$ for the resolution data $\Re_i$ on $X_i$ where $X_0 = X$, $\Re_0 = \Re$ and $\Re_{i+1} = f_i^*(\Re_i)$ for all $i \geq 0$. Then $S(\Re_i)$ is empty for all sufficiently, large integers $i$.

PROOF. Let $^i\mathfrak{R}_1^{N,n}$ be the resolution datum on $X_i$ such that $^0\mathfrak{R}_1^{N,n} = \mathfrak{R}_1^{N,n}$ and $^{i+1}\mathfrak{R}_1^{N,n} = f_i^*(^i\mathfrak{R}_1^{N,n})$ for all $i \geq 0$. Let us write

$$
{ } ^ { i } \Re _ { I } ^ { N , n } = \left( \bigcup _ { j } E _ { j } ^ { ( i ) } ; V _ { j } ^ { ( i ) } , \cdots , V _ { \beta } ^ { ( i ) } ; W ^ { ( i ) } \right) .
$$

Since $f_i \colon X_{i+1} \to X_i$ is a permissible succession of monoidal transformations of $X_i$ for $\mathfrak{R}_i$, we have $f_i(S(\mathfrak{R}_{i+1})) \subseteq S(\mathfrak{R}_i)$ for all $i \geq 0$. (See Corollary 2 of Theorem 5, §6, Ch. III, and Lemma 4, §2, Ch. IV.) Therefore, if $S(\mathfrak{R}_i)$ is not empty for arbitrarily large integer $i$, then we can find a sequence of points $x_i \in S(\mathfrak{R}_i)$ such that $f_i(x_{i+1}) = x_i$, and $X_i$ has dimension $N$ at $x_i$ for all $i \geq 0$. By the property (ii) of an effective modification, we must have either

$$
\nu_ {x _ {i + 1}} ^ {*} \left(V _ {1} ^ {(i + 1)}, \dots , V _ {\beta} ^ {(i + 1)}, W ^ {(i + 1)} / X _ {i + 1}\right) <   \nu_ {x _ {i}} ^ {*} \left(V _ {1} ^ {(i)}, \dots , V _ {\beta} ^ {(i)}, W ^ {(i)} / X _ {i}\right),
$$

or these two are equal and

$$
\tau_ {x _ {i + 1}} ^ {*} \left(V _ {1} ^ {(i + 1)}, \dots , V _ {\beta} ^ {(i + 1)}, W ^ {(i + 1)} / X _ {i + 1}\right) > \tau_ {x _ {i}} ^ {*} \left(V _ {1} ^ {(i)}, \dots , V _ {\beta} ^ {(i)}, W ^ {(i)} / X _ {i}\right).
$$

As is easily seen, these inequalities for all non-negative integers i lead to a contradiction by virtue of Theorem 4, § 5, Ch. III. q.e.d.

The proofs of Theorems A\* and B\* will be divided into several lemmas and remarks.

Let us fix and study any permissible succession (finite or infinite) of monoidal transformations of X for the given resolution datum R, say

$$
\{f _ {s} \colon X _ {s + 1} \rightarrow X _ {s} \}
$$

$$
(s = 0, 1, 2, \dots)
$$

where $X_0$ denotes $X$. Let $\Re(s)$ denote the resolution datum on $X_s(s \geq 0)$ such that $\Re(0) = \Re$ and $\Re(s + 1) = f_s^*(\Re(s))$ for all $s \geq 0$. For the case in which $\Re = (\Re_1^{N,n}, F)$ (resp. $\Re = (\Re_1^{N,n}, U)$), we write $\Re(s) = (\Re_1^{N,n}(s), F(s))$ (resp. $\Re(s) = (\Re_1^{N,n}(s), U(s))$). In both cases, we write

$$
\Re_ {1} ^ {N, n} (s) = \left(\bigcup_ {i = 1} ^ {\alpha + s} E _ {i} (s); V _ {1} (s), \dots , V _ {\beta} (s); W (s)\right).
$$

Let $B_{s}$ denote the center of $f_{s}$ in $X_{s}$, and set the symbols $E_{i}(s)$ in such a way that $E_{i}(0) = E_{i}(1 \leq i \leq \alpha)$, $E_{j}(s + 1) =$ the strict transform of $E_{j}(s)(1 \leq j \leq \alpha + s)$ and $E_{\alpha + s + 1}(s + 1) =$ the total transform $f_{s}^{-1}(B_{s})$ of the center $B_{s}$.

Let us choose and fix any point $x_0$ of $W^*$ at which $X$ has dimension $N$, where $W^*$ denotes $W \cap F$ (resp. $W - U$) for the case in which $\Re = (\mathfrak{R}_1^{N,n}, F)$ (resp. $\Re = (\mathfrak{R}_1^{N,n}, U)$). Let $S$ be the local ring of $X$ at $x_0$, and $\hat{S}$ the completion of $S$. Let $\hat{X}_0 = \operatorname{Spec}(\hat{S})$. The given succession of monoidal transformations $\{f_s: X_{s+1} \to X_s\}$ of $X$ induces a succession of monoidal transformations $\{\hat{f}_s: \hat{X}_{s+1} \to \hat{X}_s\}$ of $\hat{X}_0$ such that we have the following commutative diagrams of canonical morphisms:

$$
\begin{array}{c c c} X _ {s + 1} & \xleftarrow {c _ {s + 1}} & \hat {X} _ {s + 1} \\ f _ {s} \Big \downarrow & & \Big \downarrow \hat {f} _ {s} \\ X _ {s} & \xleftarrow {c _ {s}} & \hat {X} _ {s} \end{array}
$$

where  $c_{0}$  is the morphism  $\hat{X}_{0}\to X$  induced by the canonical local homomorphism  $S\to\hat{S}$ , and  $\hat{f}_{s}$  is the monoidal transformation of  $\hat{X}_{s}$  with the non-singular center  $\hat{B}_{s}=c_{s}^{-1}(B_{s})$  for  $s\geq0$ . Here it should be noted that the monoidal transformation with the empty center is the identity isomorphism. In view of the fact that  $\hat{S}$  is faithfully flat over S, one can show that  $\hat{X}_{s}$  is canonically isomorphic to the product  $X_{s}\times_{x}\hat{X}_{0}$  in the category of schemes over X and that  $c_{s}$  is the projection to the first factor.

The algebraic scheme $\hat{X}_0 = \operatorname{Spec}(\hat{\mathbf{S}})$ has the unique closed point $\hat{x}_0$ such that $c_0(\hat{x}_0) = x_0$. We shall denote by $g_s$ (resp. $\hat{g}_s$) the morphism $X_s \to X_0$ (resp. $\hat{X}_s \to \hat{X}_0$) obtained as the composition of the $f_j$ (resp. $\hat{f}_j$) for $0 \leq j \leq s - 1$. The following lemma is an immediate consequence of Lemma 4, §2, Ch. III, and its corollaries.

LEMMA (AB. 2). The morphism $c_s$ induces a bijective mapping of the point sets $\hat{g}_s^{-1}(\hat{x}_0) \to g_s^{-1}(x_0)$. Moreover, if $\hat{y} \in \hat{g}_s^{-1}(\hat{x}_0)$ and $y = c_s(\hat{y}) \in g_s^{-1}(x_0)$, the local homomorphism induced by $c_s$ of the local ring of $X_s$ at $y$ into that of $\hat{X}_s$ at $\hat{y}$ transforms a regular system of parameters into such a system of parameters.

The following lemma is needed in later discussions.

LEMMA (AB. 3). Let $\mathbf{R} \to \mathbf{R}'$ be a local homomorphism of regular local rings, and $\mathbf{M}$ an ideal in $\mathbf{R}$, such that a regular system of parameters of $\mathbf{R}$ is transformed into such a system of parameters of $\mathbf{R}'$ and that $\mathbf{R} \to \mathbf{R}'$ induces an isomorphism $\mathbf{R} / \mathbf{M} \to \mathbf{R}' / \mathbf{MR}'$. Let $\mathbf{P}$ be a prime ideal

in R such that R/P is regular, and  $P' = PR'$ . Let  $R_{1}$  be a monoidal transform of R with center P, and  $R_{1}'$  the unique monoidal transform of  $R'$  with center  $P'$  which admits a commutative diagram of canonical local homomorphisms

![](images/page_92_image_1.jpg)

We assume that  $M \neq R$ . Then  $R_{1} \rightarrow R_{1}'$  transforms a regular system of parameters of  $R_{1}$  into such a system of parameters of  $R_{1}'$  and, moreover, it induces an isomorphism  $R_{1}/MR_{1} \rightarrow R_{1}'/MR_{1}'$ .

PROOF. The first assertion is clear from Lemma 4, § 2, Ch. III. To prove the second assertion, we take a minimal base  $(y_{1}, \cdots, y_{r})$  of P such that if  $A = R[y_{2}/y_{1}, \cdots, y_{r}/y_{1}]$ , then  $R_{1} = A_{N}$  with a prime ideal N in A. By the assumption on  $R \to R'$ ,  $(y_{1}, \cdots, y_{r})$  is also a minimal base of the prime ideal  $P'$  in  $R'$  and, if  $A' = R'[y_{2}/y_{1}, \cdots, y_{r}/y_{1}]$ ,  $R_{1}'$  is a localization of  $A'$ . Let  $N'$  be the prime ideal in  $A'$  such that  $R_{1}' = A_{N'}$ . Then  $N'$  is an associated prime ideal of  $NA'$ . (See § 2, Ch. III.) By the assumption on  $R/M \to R'/MR'$ ,  $R \to R'$  induces an isomorphism of residue fields so that  $NA'$  is a prime ideal. Thus  $N' = NA'$ . Since  $R/M \to R'/MR'$  is surjective, so is  $A/MA \to A'/MA'$ . We have  $N \supseteq MA$  and  $N' \supseteq MA'$  by the assumption on M, and therefore  $R_{1}/MR_{1} \to R_{1}'/MR_{1}'$  is surjective. By the first assertion,  $R_{1}'$  is faithfully flat over  $R_{1}$ . It follows that  $R_{1}/MR_{1} \to R_{1}'/MR_{1}'$  is injective. Thus  $R_{1}/MR_{1} \to R_{1}'/MR_{1}'$  is bijective. q.e.d.

COROLLARY. Let the notation and the assumptions be the same as before. Let $\mathbf{M}$ be the maximal ideal of $\mathbf{S}$ and $\hat{\mathbf{M}} = \mathbf{M}\hat{\mathbf{S}}$. Let $\hat{y} \in \hat{g}_s^{-1}(\hat{x}_0)$ and $y = c_s(\hat{y}) \in g_s^{-1}(x_0)$. Let $\hat{\mathbf{S}}_s$ (resp. $\mathbf{S}_s$) be the local ring of $\hat{X}_s$ at $\hat{y}$ (resp. $X_s$ at $y$). Then the local homomorphism $S_s \to \hat{S}_s$, induced by $c_s$, induces an isomorphism $S_s / MS_s \to \hat{S}_s / \hat{M}\hat{S}_s$. In particular, if $\hat{B}$ is any reduced subscheme of $\hat{X}_s$ such that $\hat{g}_s(\hat{B}) = \hat{x}_0$, then there exists a unique reduced subscheme $B$ of $X_s$ such that $g_s(B) = x_0$ and $\hat{B} = c_s^{-1}(B)$. Moreover, $c_s$ induces an isomorphism $\hat{B} \to B$.

Let  $J_{0}$  (resp.  $J_{j}$ ) denote the ideal of W (resp.  $V_{j}$ ) in the local ring S, where  $1 \leq j \leq \beta$ . Let  $\hat{J}_{j} = J_{j}\hat{S}$  for  $0 \leq j \leq \beta$ . We choose and fix a regular frame (T; z) of  $\hat{S}$  as follows:

[a] If $\Re = (\mathfrak{R}_1^{N,n}, F)$, then $z$ is an element of S which generates the prime ideal of $F$ in S.

[b] If $\Re = (\Re_{\mathrm{I}}^{N,n}, U)$, then (T; $z$) is a $\hat{\mathbf{J}}_0$-stable regular frame of $\hat{\mathbf{S}}$.

[c] We have a $\hat{\mathbf{J}}_j$-stable standard base of $\hat{\mathbf{J}}_j$,

$$
\left(g _ {j 1}, \dots , g _ {j m _ {j}}\right)
$$

for $0 \leq j \leq \beta$, such that we can write

$$
g _ {j k} = u _ {j k} \left(z ^ {\nu_ {j k}} + g _ {j k 1} z ^ {\nu_ {j k} - 1} + \dots + g _ {j k \nu_ {j k}}\right)
$$

where $\nu_{jk} = \nu^{(k)}(\mathbf{J}_j)$, $u_{jk}$ is a unit in $\hat{\mathbf{S}}$ and $g_{jki} \in \mathbf{T}$ for $0 \leq j \leq \beta$, $1 \leq k \leq m_j$ and $1 \leq i \leq \nu_{jk}$.

The existence of such a regular frame (T; z) of  $\hat{S}$  can be seen as follows: First we choose  $z \in S$  as in [a] and [b], where in the case [b] we use Theorem 9, § 10, Ch. III. We note that in [b] we may replace T by any local subring  $T'$  of  $\hat{S}$  such that the natural homomorphism  $\hat{\mathbf{S}} \to \hat{\mathbf{S}}/(z)\hat{\mathbf{S}}$  induces an isomorphism  $\mathbf{T}' \to \hat{\mathbf{S}}/(z)\hat{\mathbf{S}}$ . By Cohen's structure theorem of a complete regular local ring, we have a subfield k of  $\hat{S}$  and a regular system of parameters  $(z, y, \cdots, y_{N-1})$  of  $\hat{S}$  such that  $\hat{S} = k\{z, y_1, \cdots, y_{N-1}\}$  (the formal power series ring of N variables). Then we choose a  $\hat{J}_j$-stable standard base of  $\hat{J}_j$  for each  $j(0 \leq j \leq \beta)$ , say  $(g_{j_1}, \cdots, g_{jm_j})$ . (See Theoreme 9, § 10, Ch. III.) By replacing  $y_j$  by  $y_j + c_j z$  with suitable  $c_j \in k(1 \leq j \leq N - 1)$ , we may assume that all the  $g_{jk}$  can be written in the form described in [c], where  $T = k\{y_1, \cdots, y_{N-1}\}$ . Then we see that (T; z) with this T is a regular frame of  $\hat{S}$  having the properties [a], [b] and [c].

By replacing $g_{jk}$ by $g_{jk} / u_{jk}$ for all $j$ and $k$, we may assume that

$$
g _ {j k} = z ^ {\nu_ {j k}} + \sum_ {i = 1} ^ {\nu_ {j k}} g _ {j k i} z ^ {\nu_ {j k} - i}
$$

for $0 \leq j \leq \beta$ and $1 \leq k \leq m_j$. Let $\bar{\mathbf{T}} = \hat{\mathbf{S}} / (z)\hat{\mathbf{S}}$. We have the canonical isomorphism $\mathbf{T} \to \bar{\mathbf{T}}$. We define a positive integer $b$ and an ideal $\bar{\mathbf{J}}$ in $\bar{\mathbf{T}}$ as follows:

[d] $b = \prod_{j=0}^{\beta}\left(\prod_{k=1}^{m_j}(\nu_{jk}!)\right),$ and

[e]  $\bar{\mathbf{J}} = (g_{jk i}^{b/i})\bar{\mathbf{T}},$

which denotes the ideal in  $\bar{T}$  generated by the images in  $\bar{T}$  of the  $(b/i)^{\mathrm{th}}$  powers of  $g_{jki}$  for  $1 \leq i \leq \nu_{jk}, 1 \leq k \leq m_j,$  and  $0 \leq j \leq \beta$ .

Let $\bar{X}_0 = \operatorname{Spec}(\bar{\mathbf{T}})$, which is a non-singular subscheme of $\hat{X}_0$ of co-dimension 1 and of dimension $N - 1$. Let $\bar{X}_s(s \geq 0)$ be the strict transform of $\bar{X}_0$ in $\hat{X}_s$ by the succession of monoidal transformations $\hat{g}_s: \hat{X}_s \to \hat{X}_0$. For the case in which $\Re = (\Re_{\mathrm{I}}^{N,n}, F)$, we have

$$
\bar {X} _ {s} = c _ {s} ^ {- 1} (F (s))
$$

for all $s \geq 0$.

We define the open subscheme  $X_{s}^{\prime}$  of  $X_{s}$ ,  $\bar{X}_{s}^{\prime}$  of  $\bar{X}_{s}$ ,  $\hat{X}_{s}^{\prime}$  of  $\hat{X}_{s}$  and the coherent sheaf of ideals  $\bar{J}(s)$  on  $\bar{X}_{s}^{\prime}$ , all together by induction on  $s \geq 0$ , as follows:

[f]  $X_{0}^{\prime}=X_{0},\hat{X}_{0}^{\prime}=\hat{X}_{0},\bar{X}_{0}^{\prime}=\bar{X}_{0}$  and  $\bar{J}(0)=$  the coherent sheaf of ideals on  $\bar{X}_{0}\big(=\operatorname{Spec}(\bar{\mathbf{T}})\big)$  generated by the ideal  $\bar{J}$  in  $\bar{T}$,

[g] If $\hat{B}_s = c_s^{-1}(B_s)$ is contained in $\bar{X}_s$ and if, at the same time, the $b^{\text{th}}$ power of the sheaf of prime ideals of $\hat{B}_s$ on $\bar{X}_s'$ contain the sheaf of ideals $\bar{J}(s)$, then we define

$$
X _ {s + 1} ^ {\prime} = f _ {s} ^ {- 1} (X _ {s} ^ {\prime})
$$

(an open subscheme of $X_{s + 1}$)

$$
\hat {X} _ {s + 1} ^ {\prime} = \hat {f} _ {s} ^ {- 1} (\hat {X} _ {s} ^ {\prime}) = c _ {s + 1} ^ {- 1} (X _ {s + 1} ^ {\prime})
$$

(an open subscheme of $\hat{X}_{s + 1}$)

and

$\bar{X}_{s + 1}^{\prime} = \bar{f}_{s}^{-1}(\bar{X}_{s}^{\prime}) = \hat{X}_{s + 1}^{\prime}\cap \bar{X}_{s + 1} = \overline{c}_{s + 1}^{-1}(X_{s + 1}^{\prime})$ (an open subscheme of $\bar{X}_{s + 1})$

where $\bar{f}_s$ denotes the morphism $\bar{X}_{s+1} \to \bar{X}_s$ induced by $\hat{f}_s$, and $\bar{c}_{s+1}$ the morphism $\bar{X}_{s+1} \to X_{s+1}$ induced by $c_{s+1}$.

[h] If either one of the conditions in [g] is not satisfied, then

$$
X _ {s + 1} ^ {\prime} = f _ {s} ^ {- 1} \left(X _ {s} ^ {\prime} - B _ {s}\right) = f _ {s} ^ {- 1} \left(X _ {s} ^ {\prime}\right) - E _ {\alpha + s + 1} (s + 1)
$$

(an open subscheme of $X_{s + 1}$)

$$
\hat {X} _ {s + 1} ^ {\prime} = \hat {f} _ {s} ^ {- 1} (\hat {X} _ {s} ^ {\prime} - \hat {B} _ {s}) = c _ {s + 1} ^ {- 1} (X _ {s + 1} ^ {\prime})
$$

(an open subscheme of $\hat{X}_{s + 1}$)

and

$$
\bar {X} _ {s + 1} ^ {\prime} = \bar {f} _ {s} ^ {- 1} (\bar {X} _ {s} ^ {\prime} - \hat {B} _ {s} \cap \bar {X} _ {s} ^ {\prime}) = \hat {X} _ {s + 1} ^ {\prime} \cap \bar {X} _ {s + 1} = \bar {c} _ {s + 1} ^ {- 1} (X _ {s + 1} ^ {\prime})
$$

(an open subscheme of $\bar{X}_{s+1}$).

In both cases [g] and [h] we denote by

$$
\bar {f} _ {s} ^ {\prime}: \bar {X} _ {s + 1} ^ {\prime} \rightarrow \bar {X} _ {s} ^ {\prime}
$$

the morphism induced by $\bar{f}_s$ (hence, by $\hat{f}_s$).

We remark that, if $\bar{B}_s'$ denotes the subscheme $\hat{B}_s \cap \bar{X}_s'$ of $\bar{X}_s'$, then

$$
\bar {f} _ {s} ^ {\prime}: \bar {X} _ {s + 1} ^ {\prime} \rightarrow \bar {X} _ {s} ^ {\prime}
$$

is the monoidal transformation with a non-singular center  $\bar{B}_{s}^{\prime}$  in  $\bar{X}_{s}^{\prime}$  for the case [g], and it is an isomorphism of  $\bar{X}_{s+1}^{\prime}$  to  $\bar{X}_{s}^{\prime}-\bar{B}_{s}^{\prime}$  for the case [h]. In both cases, we set

$$
\bar {E} _ {\alpha + s + 1} ^ {\prime} (s + 1) = \left(\bar {f} _ {s} ^ {\prime}\right) ^ {- 1} \left(\bar {B} _ {s} ^ {\prime}\right) = \bar {c} _ {s + 1} ^ {- 1} \left(E _ {\alpha + s + 1} (s + 1)\right) \cap \bar {X} _ {s + 1} ^ {\prime}
$$

and $P\big(\bar{E}_{\alpha + s + 1}^{\prime}(s + 1)\big) =$ the coherent sheaf of ideals of the subscheme $\bar{E}_{\alpha + s + 1}^{\prime}(s + 1)$ of $\bar{X}_{s + 1}^{\prime}$. We see that $\bar{E}_{\alpha + s + 1}^{\prime}(s + 1)$ is a non-singular irreducible subscheme of $\bar{X}_{s + 1}^{\prime}$ of codimension 1, and that $P\big(\bar{E}_{\alpha + s + 1}^{\prime}(s + 1)\big)$ is a sheaf of principal ideals on $\bar{X}_{s + 1}^{\prime}$ whose $b^{\text{th}}$ power contains the sheaf of ideals $(\bar{f}_s')^{-1}\big(\bar{J}(s)\big)$ on $\bar{X}_{s + 1}^{\prime}$ generated by $\bar{J}(s)$ by means of $\bar{f}_{s + 1}^{\prime}$.

[i] We define the coherent sheaf of ideals

$$
\bar {J} (s + 1) = (\bar {f} _ {s} ^ {\prime}) ^ {- 1} (\bar {J} (s)) / P \big (\bar {E} _ {\alpha + s + 1} ^ {\prime} (s + 1) \big) ^ {b}
$$

on the non-singular irreducible scheme $\bar{X}_{s+1}^{\prime}$.

Now, let us recall Theorem 3, § 5, Ch. III, which shows that, if $x$ is any point of $X_s$ at which $X_s$ has dimension $N$, then

$$
\begin{array}{l} \nu_ {x} ^ {*} \big (V _ {1} (s), \dots , V _ {\beta} (s), W (s) / X _ {s} \big) \\ \leq \nu_ {f _ {s - 1} (x)} ^ {*} \big (V _ {1} (s - 1), \dots , V _ {\beta} (s - 1), W (s - 1) / W _ {s - 1} \big), \end{array}
$$

and if this equality holds, then

$$
\begin{array}{l} \tau_ {x} ^ {*} \big (V _ {1} (s), \dots , V _ {\beta} (s), W (s) / X _ {s} \big) \\ \leq \tau_ {f _ {s - 1} (x)} ^ {*} \big (V _ {1} (s - 1), \dots , V _ {\beta} (s - 1), W (s - 1) / X _ {s - 1} \big). \end{array}
$$

It follows that, if $x$ is any point of $X_{s}$ such that $X_{s}$ has dimension $N$ at $x$ and $g_{s}(x) = x_{0}$, then

$$
\nu_ {x} ^ {*} \left(V _ {1} (s), \dots , V _ {\beta} (s), W (s) / X _ {s}\right) \leq \nu_ {x _ {0}} ^ {*} \left(V _ {1}, \dots , V _ {\beta}, W / X\right)
$$

and if this equality holds, then

$$
\tau_ {x} ^ {*} \left(V _ {1} (s), \dots , V _ {\beta} (s), W (s) / X _ {s}\right) \geq \tau_ {x _ {0}} ^ {*} \left(V _ {1}, \dots , V _ {\beta}, W / X\right).
$$

LEMMA (AB. 4). Let us consider the following condition on a point x of $X_{s}$:

(1) $X_{s}$ has dimension $N$ at $x$,

(2) $g_{s}(x) = x_{0}$, and

$$
\nu_ {x} ^ {*} \left(V _ {1} (s), \dots , V _ {\beta} (s), W (s) / X _ {s}\right) = \nu_ {x _ {0}} ^ {*} \left(V _ {1}, \dots , V _ {\beta}, W / X\right) a n d
$$

$$
\tau_ {x} ^ {*} \left(V _ {1} (s), \dots , V _ {\beta} (s), W (s) / X _ {s}\right) = \tau_ {x _ {0}} ^ {*} \left(V _ {1}, \dots , V _ {\beta}, W / X\right).
$$

If $x$ is any point of $X_s$ satisfying the conditions (1), (2) and (3), then $x$ is a point of $X_s'$, and there exists a unique point $\hat{x}$ of $\hat{X}_s'$ such that $c_s(\hat{x}) = x$. If $B_s$ contains at least one point $x$ of $X_s$ satisfying the conditions (1), (2) and (3), then $\hat{B}_s = c_s^{-1}(B_s)$ is a non-singular irreducible subscheme of $\bar{X}_s$ (i.e., a non-singular irreducible subscheme of $\hat{X}_s$ which is contained in $\bar{X}_s$) and the coherent sheaf of ideals $\bar{J}(s)$ is contained in the $b^{\text{th}}$ power of the coherent sheaf of ideals of $\bar{B}_s' (= \hat{B}_s \cap \bar{X}_s')$, which is a non-singular irreducible subscheme of $\bar{X}_s'$.

PROOF. If the first and the second assertions are verified for certain  $s \geq 0$ , then the first assertion for  $s + 1$  follows immediately by the definition  $X'_{s+1}$ . The first assertion is trivially true for s = 0. Therefore, we have only to show the second assertion, assuming the first, for each  $s \geq 0$ . We first remark that, by virtue of our assumption on the class B of the base rings, the non-singularity of  $B_s$  implies that of  $\hat{B}_s = c_s^{-1}(B_s)$ . So  $\hat{B}_s$  is a non-singular irreducible subscheme of  $\hat{X}_s$ . We shall

prove that $\hat{B}_s$ is contained in $\bar{X}_s$. Let us take a point $x$ of $B_s$ satisfying the conditions (1), (2) and (3). Then we have the unique point $\hat{x}$ of $\hat{X}_s'$ such that $c_s(\hat{x}) = x$. By Theorem 3, §5, Ch. III, the image $x_t$ of $x$ in $X_t'(0 \leq t \leq s)$ satisfies also the conditions (1), (2) and (3). Let $\hat{x}_t$ be the image of $\hat{x}$ in $\hat{X}_t'$, so that we have $x_t = c_t(\hat{x}_t)$ for $0 \leq t \leq s$. We set the symbols as follows:

$\mathbf{S}_t =$ the local ring of $X_{t}$ at $x_{t}$,

$Q_{t} = \text{the ideal of } B_{t} \text{ in } S_{t},$

$$
\mathbf {J} _ {j} (t) = \text { the   ideal   of } V _ {j} (t) \text { in } \mathbf {S} _ {t} (1 \leq j \leq \beta),
$$

$$
\mathbf {J} _ {0} (t) = \text { the   ideat   of } W (t) \text { in } \mathbf {S} _ {t},
$$

$$
\hat {\mathbf {S}} _ {t} = \text { the   local   ring   of } \hat {X} _ {t} \text { at } \hat {x} _ {t},
$$

$$
\hat {\mathbf {Q}} _ {t} = \mathbf {Q} _ {t} \hat {\mathbf {S}} _ {t} = \text { the   ideal   of } \hat {B} _ {t} \text { in } \hat {\mathbf {S}} _ {t},
$$

$$
\hat {\mathbf {J}} _ {j} (t) = \mathbf {J} _ {j} (t) \hat {\mathbf {S}} _ {t} (0 \leq j \leq \beta).
$$

Then $\{(\mathbf{J}_j(t), \mathbf{S}_t, \mathbf{Q}_{t-1})\}$ is a permissible sequence of strict monoidal transforms of $(\mathbf{J}_j, \mathbf{S}) = (\mathbf{J}_j(0), \mathbf{S}_0)$ in the sense of § 9, Ch. III; note that we permit here some trivial monoidal transforms for which the centers $\mathbf{Q}_t$ are unit ideals (that is, exactly for those cases in which $x_t$ is not contained in $B_t$). We have a canonical local homomorphism $\mathbf{S}_t \to \hat{\mathbf{S}}_t$ which, by Lemma (AB. 2), transforms a regular system of parameters of $\mathbf{S}_t$ into such a system of parameters of $\hat{\mathbf{S}}_t$. Therefore, $\{(\hat{\mathbf{J}}_j(t), \hat{\mathbf{S}}_t, \hat{\mathbf{Q}}_{t-1})\}$ is a permissible sequence of strict monoidal transforms of $(\hat{\mathbf{J}}_j, \hat{\mathbf{S}}) = (\hat{\mathbf{J}}_j(0), \hat{\mathbf{S}}_0)$ for $0 \leq j \leq \beta$. For the case in which $\Re = (\Re_I^{N,n}, U)$, (T; $z$) is a $\hat{\mathbf{J}}_0$-stable regular frame of $\hat{\mathbf{S}} = \hat{\mathbf{S}}_0$, and hence it admits a frame transform $(\mathbf{T}_t; z_t)$ in $\hat{\mathbf{S}}_t$ for all $t(0 \leq t \leq s)$. (See Remark 3, § 4, Ch. III.) We can choose these $z_t$ of regular frames $(\mathbf{T}_t; z_t)$ of $\hat{\mathbf{S}}_t$ in such a way that

$$
z _ {t + 1} = z _ {t} / v _ {t}
$$

with the denominator $v_{t} \in \mathbf{T}_{t}$ for $t \geq 0$. Those $v_{t} \in \mathbf{T}_{t}$ must then have the property that $(v_{t})\hat{\mathbf{S}}_{t+1} = \hat{\mathbf{Q}}_{t}\hat{\mathbf{S}}_{t+1}$. Since $\mathbf{Q}_{s}$ is a permissible center for $\mathbf{J}_{0}(s)$, $\hat{\mathbf{Q}}_{s}$ is such for $\hat{\mathbf{J}}_{0}(s)$, and therefore we have $z_{s} \in \hat{\mathbf{Q}}_{s}$. This shows that $\hat{\mathbf{B}}_{s}$ is contained in $\bar{X}_{s}$ because $z_{s}$ clearly generates the ideal of $\bar{X}_{s}$ in $\hat{\mathbf{S}}_{s}$. We note that what we have seen above for the case in which $\Re = (\Re_{1}^{N,n}, U)$ can be trivially verified for the other case in which $\Re = (\Re_{1}^{N,n}, F)$. Also in this case, we choose $(\mathbf{T}_{t}; z_{t})$ in the same way as above. Now, in both cases, let

$\bar{\mathbf{T}}_t =$ the local ring of $\bar{X}_t$ at $x_{t}$ , and

$\bar{\mathbf{Q}}_t = \text{the ideal of } \hat{B}_t \text{ in } \bar{\mathbf{T}}_t.$

We have the canonical isomorphisms $\bar{\mathbf{T}}_t = \hat{\mathbf{S}}_t / (z_t)\hat{\mathbf{S}}_t$ and $\bar{\mathbf{Q}}_t = \hat{\mathbf{Q}}_t / (z_t)\hat{\mathbf{S}}_t$. The natural epimorphism $\hat{\mathbf{S}}_t \to \bar{\mathbf{T}}_t$ induces an isomorphism $\mathbf{T}_t \to \bar{\mathbf{T}}_t$. $\bar{\mathbf{Q}}_s$ is also

the ideal of $\bar{B}_s' = \hat{B}_s \cap \bar{X}_s'$ in $\bar{\mathbf{T}}_s$ where $\bar{\mathbf{T}}_s$ is viewed as the local ring of $\bar{X}_s'$ at $\hat{x}_s = \hat{x}$. We want to prove that the stalk $\bar{J}(s)_x$ of $\bar{J}(s)$ at $x$ is contained in the $b^{\text{th}}$ power of $\bar{\mathbf{Q}}_s$. Since $\bar{B}_s'$ is a non-singular irreducible subscheme of $\bar{X}_s'$, this suffices for the proof of the assertion that $\bar{J}(s)$ is contained in the $b^{\text{th}}$ power of the coherent sheaf of ideals of $\bar{B}_s'$ on $\bar{X}_s'$. The standard base of $\hat{\mathbf{J}}_j$

$$
\left(\mathbf {g} _ {j 1}, \dots , g _ {j m _ {j}}\right)
$$

is chosen to be $\hat{\mathbf{J}}_j$-stable for $0 \leq j \leq \beta$, and therefore, if we define the elements $g_{jk}(t) \in \hat{\mathbf{S}}_t$ for $0 \leq j \leq \beta$, $1 \leq k \leq m_j$ and $0 \leq t \leq s$, by induction on $t$ as follows:

$$
g _ {j k} (0) = g _ {j k}
$$

$$
(0 \leq j \leq \beta , 1 \leq k \leq m _ {j})
$$

and

$$
g _ {j k} (t) / v _ {t} ^ {\nu j k} = g _ {j k} (t + 1)
$$

$$
(0 \leq t \leq s - 1),
$$

then we get a $\hat{\mathbf{J}}_j(t)$-stable standard base of $\hat{\mathbf{J}}_j(t)$ of the form

$$
\left(g _ {j 1} (t), \dots , g _ {j m _ {j}} (t)\right)
$$

for  $0 \leq t \leq s$  and  $0 \leq j \leq \beta$ . Therefore, we get the elements of  $T_{t}$ ,  $g_{jki}(t)$  for  $0 \leq j \leq \beta$ ,  $1 \leq k \leq m_{j}$  and  $0 \leq t \leq s$ , defined by induction on t as follows:

$$
g _ {j k i} (0) = g _ {j k i} \quad (0 \leq j \leq \beta , 1 \leq k \leq m _ {j}, 1 \leq i \leq \nu_ {j k})
$$

and

$$
g _ {j k i} (t) / v _ {t} ^ {i} = g _ {j k i} (t + 1)
$$

$$
(0 \leq t \leq s - 1)
$$

and we can write

$$
g _ {j k} (t) = z _ {t j k} ^ {\nu} + \sum_ {i = 1} ^ {\nu_ {j k}} g _ {j k i} (t) z _ {t} ^ {\nu_ {j k} - i}
$$

for $0 \leq j \leq \beta$ and $1 \leq k \leq m_j$. We have the equalities

$$
\left(g _ {j k i} (t) ^ {b / i}\right) / v _ {t} ^ {b} = g _ {j k i} (t + 1) ^ {b / i}
$$

for $0 \leq j \leq \beta$, $1 \leq k \leq m_j$ and $1 \leq i \leq \nu_{jk}$. We have also that if $\bar{v}_t$ denotes the image of $v_t$ in $\bar{\mathbf{T}}_t$,

$\mathbf{T}_{t + 1} = \text{a monoidal transform of } \bar{\mathbf{T}}_t$ with center $\bar{\mathbf{Q}}_t$,

$$
(\bar {v} _ {t}) \bar {\mathbf {T}} _ {t + 1} = \bar {\mathbf {Q}} _ {t} \bar {\mathbf {T}} _ {t + 1},
$$

and

$$
\bar {J} (t + 1) _ {\hat {x} _ {t + 1}} = \left(\bar {v} _ {t} ^ {- b} \bar {J} (t) _ {\hat {x} _ {t}}\right) \bar {\mathbf {T}} _ {t + 1}
$$

for $0 \leq t \leq s - 1$. In view of these facts, we can write

$$
\bar {J} (t) _ {\hat {x} _ {t}} = \left(g _ {j k i} (t) ^ {b / i}\right) \bar {\mathbf {T}} _ {t}
$$

$$
\text { for } 0 \leq t \leq s
$$

i.e., the stalk of $\bar{J}(t)$ at $\hat{x}_t$ is generated by the images of the $(b / i)^{\mathrm{th}}$ powers of $g_{jki}(t)\in \mathbf{T}_t$ for $0\leq j\leq \beta,1\leq k\leq m_j$ and $1\leq i\leq \nu_{jk}$. Let us consider the case of $t = s$. We have the $\hat{\mathbf{J}}_j(s)$-stable standard base of $\hat{\mathbf{J}}_j(s)$ for $0\leq j\leq \beta$:

$$
\left(g _ {j _ {1}} (s), \dots , g _ {j _ {m _ {j}}} (s)\right)
$$

where

$$
g _ {j k} (s) = z _ {s} ^ {\nu_ {j k}} + \sum_ {i = 1} ^ {\nu_ {j k}} g _ {j k i} (s) z _ {s} ^ {\nu_ {j k} - i}
$$

for $1 \leq k \leq m_j$. The prime ideal $\hat{\mathbf{Q}}_s$ of $\bar{B}_s'$ (i.e., that of $\hat{B}_s$) in $\hat{\mathbf{S}}_s$ contains the element $z_s$ of $\hat{\mathbf{S}}_s$ and it is a permissible center for $\hat{\mathbf{J}}_j(s)$. It follows that

$$
g _ {j k} (s) \in \widehat {\mathbf {Q}} ^ {\nu_ {j k}}
$$

$$
(0 \leq j \leq \beta_ {j}, 1 \leq k \leq m _ {j})
$$

and

$$
g _ {j k i} (s) \in \hat {\mathbf {Q}} _ {s} ^ {i} \quad (0 \leq j \leq \beta , 1 \leq k \leq m _ {j}, 1 \leq i \leq \nu_ {j k}).
$$

Therefore

$$
g _ {j k i} (s) ^ {b / i} \in \hat {\mathbf {Q}} _ {s} ^ {b} \quad (0 \leq j \leq \beta , 1 \leq k \leq m _ {j}, 1 \leq i \leq \nu_ {j k})
$$

or, equivalently,

$$
\bar {\mathbf {Q}} _ {s} ^ {b} \cong (g _ {j k i} (s) ^ {b / i}) \bar {\mathbf {T}} _ {s} = \bar {J} (s) _ {\hat {x}},
$$

which completes the proof of the last assertion of the lemma. q.e.d.

COROLLARY. For the case in which $\Re = (\Re_{1}^{N,n}, U)$, if $x$ is any point of $X_s$ satisfying the conditions (1), (2) and (3) of Lemma (AB. 4), then the unique point $\hat{x}$ of $\hat{X}_s$ such that $c_s(\hat{x}) = x$ belongs to $\hat{X}_s'$, and the stalk $\bar{J}(s)_{\hat{x}}$ is contained in the $b^{\text{th}}$ power of the maximal ideal of the local ring of $\bar{X}_s'$ at $\hat{x}$. For the case in which $\Re = (\Re_{1}^{N,n}, F)$, the same is true provided $x \in F(s)$ (i.e., $\hat{x} \in \bar{X}_s$).

PROOF. In both cases, we know that $x$ is a point of $X_s'$, and $\hat{x}$ is a point of $\hat{X}_s'$. Therefore, if we know that $\hat{x}$ belongs to $\bar{X}_s$ then $\hat{x}$ must belong to $\bar{X}_s'$. For the case in which $\Re = (\Re_{1}^{N,n}, U)$, we have $g_s(x) = x_0 \in W - U$. Hence, by the condition (3) on $x$, we have $x \in W(s) - U(s)$. Then we see that the monoidal transformation of $X_s$ with center $x$ is permissible for the resolution datum $(\Re_{1}^{N,n}(s), U(s))$. Namely we can take $B_s$ to be the closed point $x$ of $X_s$. For the case in which $\Re = (\Re_{1}^{N,n}, F')$, we see, by the same argument, that the monoidal transformation of $X_s$ with center $x$ is permissible for the resolution datum $(\Re_{1}^{N,n}(s), F'(s))$ under the assumption that $x \in F(s)$. Namely, we can take $B_s$ to be the point $x$ of $X_s$. Thus

the assertions in the Corollary follow Lemma (AB. 4) applied to $B_{s} = x$. q.e.d.

LEMMA (AB. 5). Let $\hat{x}'$ be any point of $\bar{X}_s'$ and $x' = c_s(\hat{x}') \in X_s'$. Suppose $\nu(\bar{J}(s)_{\hat{x}'}) \geq b$. Then we have that:

(i) $x'$ is a point of $W(s)$. (Hence, for the case in which $\Re = (\Re_{\mathrm{I}}^{N,n}, F)$, we have $x' \in W(s) \cap F(s)$.)

(ii) If $W$ is singular at the point $x_0$, then $W(s)$ is also singular at $x'$.

(iii) If  $V_{j}$  for some  $j(1 \leq j \leq \beta)$  is not normally flat along W at  $x_{0}$ , then  $V_{j}(s)$  for the same j is not normally flat along  $W(s)$  at  $x'$ , provided  $x_{0}$  is a simple point of W.

PROOF. We set the symbols as follows:

$\hat{x}_t' =$ the image of $\hat{x}'$ in $\bar{X}_t'$ (hence, in $\hat{X}_t'$)

$x_{t}^{\prime} =$ the image of $x^{\prime}$ in $X_{t}^{\prime}$ (so that $x_{t}^{\prime} = c_{t}(\hat{x}_{t}^{\prime})$)

$\mathbf{S}_t =$ the local ring of $X_{t}^{\prime}$ at $x_{t}^{\prime}$

$\hat{\mathbf{S}}_t =$ the local ring of $\hat{X}_t^\prime$ at $\hat{x}_t^\prime$

$\bar{\mathbf{T}}_t = \text{the local ring of } \bar{X}_t'$ at $\hat{x}_t'$,

$Q_{t} = \text{the ideal of } B_{t} \text{ in } S_{t},$

$\hat{\mathbf{Q}}_t = \text{the ideal of } \hat{B}_t = c_t^{-1}(B_t) \text{ in } \hat{\mathbf{S}}_t (= \mathbf{Q}_t \hat{\mathbf{S}}_t),$

$J_{j}(t) = \text{the ideal of } V_{j}(t) \text{ in } S_{t}(1 \leq j \leq \beta),$

$\mathbf{J}_0(t) =$ the ideal of $W(t)$ in $\mathbf{S}_t$ , and

$\hat{\mathbf{J}}_j(t) = \mathbf{J}_j(t)\hat{\mathbf{S}}_t$ for $0 \leq j \leq \beta$ and $0 \leq t \leq s$.

Now, let S,  $\hat{S}$  and (T; z) be as before. Clearly,  $x_{0}$  (resp.  $\hat{x}_{0}$ ) is a specialization of  $x_{0}^{\prime}$  (resp.  $\hat{x}_{0}^{\prime}$ ) on the scheme  $X_{0}^{\prime}=X$  (resp.  $\hat{X}_{0}^{\prime}=\hat{X}_{0}$ ). Hence we have a prime ideal  $P_{0}$  (resp.  $\hat{P}_{0}$ ) in S (resp.  $\hat{S}$ ) such that  $S_{0}=S_{P_{0}}$  and  $\hat{S}_{0}=\hat{S}_{\hat{P}_{0}}$ . Since  $\hat{x}_{0}^{\prime}\in\bar{X}_{0}^{\prime}$ , we have  $z\in\hat{P}$ . Therefore, if  $T_{0}$  denote the localization of T with respect to the prime ideal  $\hat{P}_{0}\cap T$ , then ( $T_{0};z$ ) is a regular frame of  $\hat{S}_{0}$ . Moreover, we have  $\mathbf{J}_{j}(0)=\mathbf{J}_{j}\mathbf{S}_{0}$  and  $\hat{\mathbf{J}}_{j}(0)=\hat{\mathbf{J}}_{j}\hat{\mathbf{S}}_{0}$ . We have chosen a  $\hat{J}_{j}$ -stable standard base of  $\hat{J}_{j}$ ,

$$
\left(g _ {j 1}, \dots , g _ {j m _ {j}}\right)
$$

where

$$
g _ {j k} = z ^ {\nu_ {j k}} + \sum_ {i = 1} ^ {\nu_ {j k}} g _ {j k i} ^ {\nu_ {j k} - i}
$$

with $g_{jki} \in \mathbf{T}$ for $0 \leq j \leq \beta, 1 \leq k \leq m_j, 1 \leq i \leq \nu_{jk}$. We have the ideal

$$
\mathbf {\bar {J}} = (g _ {j k i} ^ {b / i}) \mathbf {\bar {T}}
$$

which generates $\bar{J}(0)$ on the scheme $\bar{X}_0'$, so that the stalk $\bar{J}(0)_{\hat{x}_0'}$ of $\bar{J}(0)$ at $\hat{x}_0'$ is given by

$$
\bar {J} (0) _ {\hat {x} _ {0} ^ {\prime}} = \left(g _ {j k i} ^ {b / i}\right) \bar {\mathbf {T}} _ {0}.
$$

Now, we claim that there exists a regular frame  $(\mathbf{T}_{t}; z_{t})$  of  $\hat{\mathbf{S}}_{t}(0 \leq t \leq s)$ , elements  $g_{jk}(t)$  of  $\hat{\mathbf{J}}_{j}(t)$  ( $0 \leq j \leq \beta$ ,  $1 \leq k \leq m_{j}$ ), and elements  $v_{t}$  of  $T_{t}$  having the following properties:

(1) $(\mathbf{T}_0;z_0) = (\mathbf{T}_0;z)$ and, in general, $(\mathbf{T}_t;z_t)$ is a regular frame of $\hat{\mathbf{S}}_t$ such that the kernel of the canonical homomorphism $\hat{\mathbf{S}}_t\to \bar{\mathbf{T}}_t$ is generated by $z_{t}$.

(2)  $g_{jk}(0) = g_{jk} \left(0 \leq j \leq \beta \text{ and } 1 \leq k \leq m_j\right)$  and, in general, the system of elements  $\left(g_{j_1}(t), \cdots, g_{jm_j}(t)\right)$  of  $\hat{\mathbf{J}}_j(t)$  has the following properties:

(a) $\hat{\mathbf{M}}_t$ being the maximal ideal of $\hat{\mathbf{S}}_t$, the initial forms of $g_{jk}(t)$ ($1 \leq k \leq m_j$) in $\mathrm{gr}_{\hat{\mathbf{M}}_t}(\hat{\mathbf{S}}_t)$ generate the ideal $\mathrm{gr}_{\hat{\mathbf{M}}_t}(\hat{\mathbf{J}}_j(t), \hat{\mathbf{S}}_t)$, and

(b) $\nu_{\widehat{\mathbf{M}}_t}\big(g_{jk}(t)\big) = \nu_{jk}\left(\text{where } \nu_{jk} = \nu^{(k)}(\widehat{\mathbf{J}}_j) = \nu^{(k)}(\mathbf{J}_j)\right)$ for $0 \leq j \leq \beta$ and $1 \leq k \leq m_j$.

(3) We can write

$$
g _ {j k} (t) = z _ {t} ^ {\nu j k} + \sum_ {i = 1} ^ {\nu j k} g _ {j k i} (t) z _ {t} ^ {\nu j k - i}
$$

where $g_{jki}(t) \in \mathbf{T}_t$ for $0 \leq j \leq \beta$, $1 \leq k \leq m_j$ and $1 \leq i \leq \nu_{jk}$,

(4) $\bar{J}(t)_{\hat{x}_t'} = (g_{jk i}(t)^{b / i})\bar{\mathbf{T}}_t$, which denotes the ideal generated by the images in $\bar{\mathbf{T}}_t$ of the $(b / i)^{\mathrm{th}}$ powers of $g_{jk i}(t)\in \mathbf{T}_t$,

(5) $(v_{t})\hat{\mathbf{S}}_{t + 1} = \hat{\mathbf{Q}}_{t}\hat{\mathbf{S}}_{t + 1}$ and $z_{t + 1} = z_t / v_t$ for $0\leq t\leq s - 1$

(6)  $g_{jk}(t+1)=g_{jk}(t)/v_{t}^{\nu_{jk}}$  for  $0\leq t\leq s-1,0\leq j\leq\beta$  and  $1\leq k\leq m_{j}$ . Their existence can be proved as follows: We first see that (1) for t=0 is clear. Let  $g_{jk}(0)=g_{jk}(0\leq j\leq\beta$  and  $1\leq k\leq m_{j}$ ), as is required in (2), and  $g_{jki}(0)=g_{jki}(0\leq j\leq\beta,1\leq k\leq m_{j}$  and  $1\leq i\leq\nu_{jk}$ ). Then (3) and (4) are clear for t=0. Next we want to show (a) and (b) of (2) for t=0. From the definition of  $X_{s}^{\prime}$  and the assumption that  $\nu(\bar{J}(s)_{x^{\prime}})\geq b$ , it is clear that we have  $\nu(\bar{J}(t)_{x_{t}^{\prime}})\geq b$  for all  $t(0\leq t\leq s)$ . Therefore, in particular if t=0, (b) of (2) follows from (3) and (4). Since  $(g_{j1}(0),\cdots,g_{jm_{j}}(0))$  is a standard base of  $\hat{J}_{j}(0\leq j\leq\beta)$ , if t=0, then (b) of (2) implies (a) of (2) by Corollary 3 of Theorem 5, §6, Ch. III. Now, assuming that we have obtained  $(\mathbf{T}_{t};z_{t})$  having the property (1) for some  $t\geq0$ , we claim that there exists  $v_{t}\in T_{t}$  such that  $\hat{\mathbf{Q}}_{t}\hat{\mathbf{S}}_{t+1}=(v_{t})\hat{\mathbf{S}}_{t+1}$ . (See (5).) In fact,  $\hat{S}_{t+1}$  is a monoidal transform of  $\hat{S}_{t}$  with center  $\hat{Q}_{t},\hat{Q}_{t}$  contains the kernel  $(z_{t})\hat{\mathbf{S}}_{t}$  of the canonical homomorphism  $\hat{S}_{t}\to\bar{T}_{t}$  by the definition of  $X_{t+1}^{\prime}$ , and finally if  $\hat{\mathbf{Q}}_{t}\hat{\mathbf{S}}_{t+1}=(w)\hat{\mathbf{S}}_{t+1}$  for some  $w\in\hat{Q}_{t}$ , then  $z_{t}w^{-1}$  is not a unit in  $\hat{S}_{t+1}$  because  $\hat{x}_{t+1}^{\prime}\in\bar{X}_{t+1}^{\prime}$ . For the same reason, moreover, we have a frame transform  $(\mathbf{T}_{t+1};z_{t+1})$  of  $(\mathbf{T}_{t};z_{t})$  in  $\hat{S}_{t+1}$  such that  $z_{t+1}=z_{t}v_{t}^{-1}$ . Thus the existence proof will be completed if, assuming that  $(\mathbf{T}_{t};z_{t})$ ,  $g_{jk}(t)$ , and  $g_{jki}(t)$  are obtained and have the properties (1), (2), (3) and (4), we show that  $(\mathbf{T}_{t+1};z_{t+1})$  with  $z_{t+1}=z_{t}/v_{t}$  and  $g_{jk}(t+1)=g_{jk}(t)/v_{t}^{\nu_{jk}}$  for

$0 \leq j \leq \beta$ and $1 \leq k \leq m_j$ have the properties (1), (2), (3) and (4). First of all, (1) for $(\mathbf{T}_{t+1}; z_{t+1})$ is clear. (4) for $\bar{J}(t)\hat{x}_t'$ implies that $g_{jki}(t)^{b/i}$ is contained in the $b^{\text{th}}$ power of $\hat{\mathbf{Q}}_t$ for $0 \leq j \leq \beta$, $1 \leq k \leq m_j$ and $1 \leq i \leq \nu_{jk}$. Hence, if we set $g_{jki}(t + 1) = g_{jki}(t)v_t^{-i}$ for $0 \leq j \leq \beta$, $1 \leq k \leq m_j$ and $1 \leq i \leq \nu_{jk}$, then (3) for $g_{jk}(t + 1)$ for $0 \leq j \leq \beta$ and $1 \leq k \leq m_j$ and (4) for $\bar{J}(t + 1)\hat{x}_{t+1}'$ follow. Since we have $\nu(\bar{J}(t + 1)\hat{x}_{t+1}') \geq b$, (4) for $\bar{J}(t + 1)\hat{x}_{t+1}'$ implies (b) of (2) for $g_{jk}(t + 1)$ ($0 \leq j \leq \beta$, $1 \leq k \leq m_j$). Finally (a) of (2) follows (b) of (2) for $g_{jk}(t + 1)$ ($0 \leq j \beta$, $1 \leq k \leq m_j$) by Corollary 3 of Theorem 5, § 6, Ch. III, and by Theorem 5, § 6, Ch. III, applied to a monoidal transform of $\hat{\mathbf{S}}_t$ with center $\hat{\mathbf{Q}}_t$ which is residually algebraic over $\mathbf{S}_t$ and such that $\mathbf{S}_{t+1}$ is a localization of the transform. We thus conclude the existence of $(\mathbf{T}_t; z_t)$, $g_{jk}(t) \in \hat{\mathbf{J}}_j(t)$ and $v_t \in \mathbf{T}_t(0 \leq t \leq s, 0 \leq j \leq \beta, 1 \leq k \leq m_j)$ having the properties (1), (2), (3), (4), (5) and (6). We are ready to prove the assertions (i), (ii) and (iii). Since $x_0$ is a point of $W$, we have $\nu_{0k} > 0$ for $1 \leq k \leq m_0$. Hence (a) and (b) of (2) for $\hat{\mathbf{J}}_0(s)$ and $g_{0k}(s)$ for $1 \leq k \leq m_0$ imply that $\hat{\mathbf{J}}_0(s)$ is contained in the maximal ideal of $\hat{\mathbf{S}}_s$ and hence $\mathbf{J}_0(s)$ contained in the maximal ideal of $\mathbf{S}_s$. This means that $x' = x_s' \in W(s)$, namely (i). If $W$ is singular at $x_0$, then the number of those indices $k$ with $\nu_{0k} = 1$ is less than codimension of $W$ in $X (= X_0 = X_0')$ at $x_0$. Here, by the condimension we mean the minimum of the codimensions of irreducible components of $W$ in $X$ at $x_0$. It is clear that the codimension of $W(s)$ in $W_s'$ at $x_s'$ is at least equal to that of $W$ in $X$ at $x_0$. Therefore, in view of (a) and (b) of (2) for $\hat{\mathbf{J}}_0(s)$ and $g_{0k}(s)$ ($1 \leq k \leq m_0$), we see that $W(s)$ is singular at the point $x' = x_s'$. (Observe that a suitably reordered subsystem of $(g_{01}(s), \cdots, g_{0m}(s))$ is a standard base of $\hat{\mathbf{J}}_0(s)$.) To prove (iii), we assume that $x_0$ is a simple point of $W$. It follows that $\hat{x}_t'$ is a simple point of $c_t^{-1}(W(t))$, for $0 \leq t \leq s$. Since $\hat{x}_t' \in \hat{X}_t'$ for all $t(0 \leq t \leq s)$, by the definition of $\hat{X}_t'$, we have $z_t \in \hat{\mathbf{Q}}_t$ and $\bar{J}(t)_{x_t'} \subseteq \bar{\mathbf{Q}}_t^b$, where $\bar{\mathbf{Q}}_t = \hat{\mathbf{Q}}_t / (z_t)\hat{\mathbf{S}}_t$, for all $t$. Therefore, by (3) and (4) we have $\nu_{\hat{\mathbf{Q}}} (g_{jk}(t)) = \nu_{jk}$ for $0 \leq j \leq \beta$ and $1 \leq k \leq m_j$. Therefore, in view of (a) and (b) of (2), we can conclude by Corollary 1 of Proposition 2, § 8, Ch. III that, if $\hat{\mathbf{J}}_0(t + 1)$ (which is a prime ideal in $\hat{\mathbf{S}}_{t+1}$ such that $\hat{\mathbf{S}}_{t+1}/\hat{\mathbf{J}}_0(t + 1)$ is regular) is a permissible center for $\hat{\mathbf{J}}_j(t + 1)$ for some $j(1 \leq j \leq \beta)$, then $\hat{\mathbf{J}}_0(t)$ (which is a prime ideal in $\hat{\mathbf{S}}_t$ such that $\hat{\mathbf{S}}_t/\hat{\mathbf{J}}_0(t)$ is regular) is a permissible center for $\hat{\mathbf{J}}_j(t)$ for the same $j$. Since $\hat{\mathbf{S}}_{t+1}$ (resp. $\hat{\mathbf{S}}_t$) is faithfully flat over $\mathbf{S}_{t+1}$ (resp. S\_t), it follows by Lemma 9 of § 3, Ch. II that, if J\_0(t + 1) is a permissible center for J\_j(t + 1) for some j(1 ≤ j ≤ \beta), then J\_0(t)\) is such for J\_j(t)$for the same j$. In other words, if V\_j(t + 1)$is normally flat along W(t + 1)\(at x_{t+1}'$ for some j(1 ≤ j ≤ \beta),

then $V_{j}(t)$ is so along $W(t)$ at $x_{t}^{\prime}$. On the other hand, $V_{j}$ is normally flat along $W$ at $x_{0}$ if and only if the same is true at $x_{0}^{\prime}$. (See Corollary 2 of Proposition 2, § 8, Ch. III.) The assertion (iii) follows. q.e.d.

LEMMA (AB. 6). Let $\bar{B}'$ be any non-singular irreducible subscheme of $\bar{X}_s'$ such that $\hat{g}_s(\bar{B}')$ consists of only the point $\hat{x}_0$, and that the stalk $\bar{J}(s)_x$ is contained in the $b^{\text{th}}$ power of the prime ideal of $\bar{B}'$ at every point $\hat{x}$ of $\bar{B}'$. Let $B_s$ be the closure of $c_s(\bar{B}')$ in $X_s$, which may be viewed as a reduced subscheme of $X_s$. Then $B_s$ is an irreducible subscheme of $X_s$ such that $\bar{B}' = c_s^{-1}(B_s) \cap \hat{X}_s'$, and there exists a non-empty open subset $U_s$ of $B_s$, containing no multiple points of $B_s$, such that

(i) $U_{s}\cong c_{s}(\bar{B}^{\prime})$ and

(ii)  $V_{1}(s), \cdots, V_{\beta}(s)$  and  $W(s)$  are all normally flat along  $B_{s}$  at every point of  $U_{s}$ .

PROOF. Let $\bar{B}$ be the closure of $\bar{B}'$ in $\bar{X}_s$ (i.e., the subscheme of $\hat{X}_s$ in which $\bar{B}'$ is dense.) Since $\hat{X}_s'$ (resp. $\bar{X}_s'$) is an open subscheme of $\hat{X}_s$ (resp. $\bar{X}_s$) and $\bar{X}_s' = \bar{X}_s \cap \hat{X}_s'$, we have $\bar{B}' = \bar{B} \cap \bar{X}_s' = \bar{B} \cap \hat{X}_s'$. Then $\bar{B}$ is a reduced irreducible subscheme of $\hat{X}_s$ and $\hat{g}_s(\bar{B}) = \hat{x}_0$. Hence by Corollary of Lemma (AB. 3) we have a unique reduced irreducible subscheme $B_s$ of $X_s$ such that $\bar{B} = c_s^{-1}(B_s)$ and $B_s = c_s(\bar{B})$. Moreover, $c_s$ induces an isomorphism $\bar{B} \to B_s$. Clearly, $B_s$ is the closure of $c_s(\bar{B}')$ in $X_s$, and $\bar{B}' = c_s^{-1}(B_s) \cap \hat{X}_s'$. Let $U_s$ be the open subset of $B_s$ consisting of those simple points of $B_s$ at which all the $V_j(s)$ ($1 \leq j \leq \beta$) and $W(s)$ are normally flat along $B_s$. We want to prove that $U_s \supseteq c_s(\bar{B}')$. Let $\hat{x}'$ be any point of $\bar{B}'$. Let $\mathbf{S}_s$ (resp. $\hat{\mathbf{S}}_s$) be the local ring of $X_s'$ at $x'$ (resp. $\hat{X}_s'$ at $\hat{x}'$), $\mathbf{J}_j(s)$ the ideal of $V_j(s)$ in $\mathbf{S}_s$, $\mathbf{J}_0(s)$ the ideal of $W(s)$ in $\mathbf{S}_s$, and $\hat{\mathbf{J}}_j(s) = \mathbf{J}_j(s)\hat{\mathbf{S}}_s$ ($0 \leq j \leq \beta$), where $x' = c_s(\hat{x}')$. Let $\bar{\mathbf{T}}_s$ be the local ring of $\bar{X}_s'$ at $\hat{x}'$. Then, by the same argument as in the proof of Lemma (AB. 5), we can find a regular frame ($\mathbf{T}_s; z_s$) of $\mathbf{S}_s$ and element $g_{jk}(s)$ of $\hat{\mathbf{J}}_j(s)$ ($0 \leq j \leq \beta$, $1 \leq k \leq m_j$), such that

(1) $z_{s}$ generates the kernel of the canonical homomorphism $\hat{\mathbf{S}}_s\to \bar{\mathbf{T}}_s$

(2) the system of elements  $(g_{j1}(s), \cdots, g_{jm_j}(s))$  of  $\hat{\mathbf{J}}_j(s)$  has the following properties:

(a) $\hat{\mathbf{M}}_s$ being the maximal ideal of $\hat{\mathbf{S}}_s$, the initial forms of $g_{jk}(s)$ ($1 \leq k \leq m_j$) in $\mathrm{gr}_{\hat{\mathbf{M}}_s}(\hat{\mathbf{S}}_s)$ generate the ideal $\mathrm{gr}_{\hat{\mathbf{M}}_s}(\hat{\mathbf{J}}_j(s), \hat{\mathbf{S}}_s)$, and

(b) $\nu_{\widehat{\mathbf{M}}_s}(g_{jk}(s)) = \nu_{jk}(\nu_{jk} = \nu^{(k)}(\mathbf{J}_j))$ for $0 \leq j \leq \beta$ and $1 \leq k \leq m_j$,

(3) we can write

$$
g _ {j k} (s) = z _ {s} ^ {\nu j k} + \sum_ {i = 1} ^ {\nu j k} g _ {j k i} (s) z _ {s} ^ {\nu j k - i}
$$

where $g_{jki}(s) \in \mathbf{T}_s$ ($0 \leq j \leq \beta$, $1 \leq k \leq m_j$ and $1 \leq i \leq \nu_{jk}$),

(4) $\bar{J} (s)_{\hat{x}^{\prime}} = (g_{jk i}(s)^{b / i})\overline{\mathbf{T}}_s.$

Now, let $\mathbf{P}(\text{resp. } \hat{\mathbf{P}})$ be the prime ideal of $B_s$ in $\mathbf{S}_s$ (resp. $\bar{B}'$ in $\hat{\mathbf{S}}_s$). Then $\hat{\mathbf{P}} = \mathbf{P}\hat{\mathbf{S}}_s$. By assumption, $\hat{\mathbf{S}}_s / \hat{\mathbf{P}}$ is regular, $z_s \in \hat{\mathbf{P}}$ and, if $\bar{\mathbf{P}} = \hat{\mathbf{P}} / (z_s)\hat{\mathbf{S}}_s$, $\bar{\mathbf{P}}^b \cong \bar{J}(s)_{\hat{x}'}$. (See (1).) Therefore, by (1), (3) and (4), we have $\nu_{\hat{\mathbf{P}}} (g_{jk}(s)) \geq \nu_{jk}$ for $0 \leq j \leq \beta$ and $1 \leq k \leq m_j$. Hence, by (a) and (b) of (2), $\hat{\mathbf{P}}$ is a permissible center for all the $\hat{\mathbf{J}}_j(s)$ ($0 \leq j \leq \beta$). Since $\mathbf{S}_s \to \hat{\mathbf{S}}_s$ is faithfully flat and $\hat{\mathbf{P}} = \mathbf{P}\hat{\mathbf{S}}_s$, $\mathbf{P}$ is a permissible center for all $\mathbf{J}_j(s)$ ($0 \leq j \leq \beta$). (See Lemma 9, § 3, Ch. II.) In other words, all the $V_j(s)$ ($1 \leq j \leq \beta$) and $W(s)$ are normally flat along $B_s$ at $x'$, i.e., $x' = c_s(\hat{x}') \in U_s$. We conclude that $c_s(\bar{B}') \subseteq U_s$. q.e.d.

Now, we are ready to prove Theorems A\* and B\*, hence, Theorems A and B.

First of all, by Localization Theorems (Propositions 1 and 2 of § 1, Ch. IV) and Preparation Theorem (Proposition 5 of § 2, Ch. IV), we can find a permissible succession of monoidal transformations $g_s = \{f_t: X_{t+1} \to X_t\}$ ($0 \leq t < s$) such that, the notations $\Re(s)$ (=either $(\Re_1^{N,n}(s), F(s))$ or $(\Re_1^{N,n}(s), U(s))$), and $\Re_1^{N,n}(s) = (\bigcup_{i=1}^{\alpha+s} E_i(s); V_1(s), \cdots, V_\beta(s); W(s))$ being as above, we have

[(1)] the image in $X = X_0$ of $S(\Re(s))$ (=either $F(s) \cap W(s)$ or the closed subset of $W(s)$ of those points at which $\Re(s)$ is not resolved) consists of a finite number of points, at which $X$ has dimension $N$,

[(2)] for the case in which $\Re = (\Re_{1}^{N,n}, U)$, if $W_{1}(s)$ is any irreducible component of $W(s)$ and if $i$ is any integer such that $1 \leq i \leq \alpha$, then either $W_{1}(s) \subseteq E_{i}(s)$ or $E_{i}(s) \cap W_{1}(s) \cap S(\Re(s))$ is empty.

(For [(2)], we apply Preparation Theorem $\alpha$ times repeatedly.) Let $x_0$ be any point of $X$ which is in the image $g_s(S(\Re(s)))$.

REMARK 1. For the case in which $\Re = (\Re_{1}^{N,n}, U)$, either $W$ is singular at $x_0$ or at least one of the $V_j(1 \leq j \leq \beta)$ is not normally flat along $W$ at $x_0$. In fact, if otherwise, for every point $x$ of $W(s)$ with $g_s(x) = x_0$, $x$ is simple point of $W(s)$ and all the $V_j(s)$ ($1 \leq j \leq \beta$) are normally flat along $W(s)$ at $x$. Moreover, by Lemma 4, § 2, $\bigcup_{i=\alpha+1}^{\alpha+s} E_i(s)$ has only normal crossings with $W(s)$ at $x$, and therefore, by [(2)], $\bigcup_{i=1}^{\alpha+s} E_i(s)$ has only normal crossings with $W(s)$ at $x$. Hence $x \notin S(\Re(s))$. This contradicts the assumption: $x_0 \in g_s(S(\Re(s)))$.

Now, with reference to the above $x_0 \in X$ and to the succession of monoidal transformations $g_s = \{f_t: X_{t+1} \to X_t\} (0 \leq t < s)$, we construct in the same process as before a new succession of monoidal transformations $\hat{g}_s = \{\hat{f}_t: \hat{X}_{t+1} \to \hat{X}_t\} (0 \leq t < s)$ together with morphisms $c_t: \hat{X}_t \to X_t (0 \leq t \leq s)$. Moreover, by means of [a], [b], [c], [d], [e], [f], [g], [h] and [i], we

construct a positive integer $b$, open subschemes $X_{t}^{\prime}$ (resp. $\hat{X}_{t}^{\prime}$) of $X_{t}$ (resp. $\hat{X}_{t}$) subschemes $\bar{X}_{t}$ (resp. $\bar{X}_{t}^{\prime}$) of $\hat{X}_{t}$ (resp. $\hat{X}_{t}^{\prime}$) and coherent sheaves of ideals $\bar{J}(t)$ on $\bar{X}_{t}^{\prime}$, for all $t$ ($0 \leq t \leq s$). We shall freely use the notations which have been used above in relation with these objects. We shall denote by $\bar{g}_{s}^{\prime} \colon \bar{X}_{s}^{\prime} \to \bar{X}_{0}^{\prime}(= \bar{X}_{0})$ the morphism induced by $\bar{g}_{s}$.

REMARK 2. Let $\hat{E}_{j}^{\prime}(s) = c_{s}^{-1}\big(E_{j}(s)\big) \cap \hat{X}_{s}^{\prime}$ for $1 \leq j \leq \alpha + s$. It is clear that $\hat{E}_{\alpha+1}^{\prime}(s) \cup \cdots \cup \hat{E}_{\alpha+s}^{\prime}(s)$ has only normal crossings with $\bar{X}_{s}^{\prime}$ on $\hat{X}_{s}^{\prime}$. For the case in which $\Re = (\mathfrak{R}_{1}^{N,n}, F)$, $E_{1}^{\prime}(s) \cup \cdots \cup E_{\alpha+s}^{\prime}(s)$ has only normal crossings with $\bar{X}_{s}^{\prime}$ on $\hat{X}_{s}^{\prime}$ because $\bar{X}_{s}^{\prime} = c_{s}^{-1}\big(F(s)\big) \cap \hat{X}_{s}^{\prime}$. We define $\tilde{E}_{j}$ for $1 \leq j \leq \tilde{\alpha}$ as follows:

(i) In case $\Re = (\Re_{\mathrm{I}}^{N,n}, F)$, $\tilde{E}_j = \hat{E}_j'(s) \cap \bar{X}_s'$ for $1 \leq j \leq \alpha + s$, and $\tilde{\alpha} = \alpha + s$;

(ii) In case $\Re = (\mathfrak{R}_1^{N,n}, U)$, $\tilde{E}_j = \hat{E}_{\alpha+j}^{\prime}(s) \cap \bar{X}_s'$ for $1 \leq j \leq s$, and $\tilde{\alpha} = s$. In both cases, we see that $\tilde{E}_1, \cdots, \tilde{E}_{\tilde{\alpha}}$ are non-singular irreducible sub-schemes of $\bar{X}_s'$ of codimension 1, and that $\tilde{E}_1 \cup \cdots \cup \tilde{E}_{\tilde{\alpha}}$ has only normal crossings on $\bar{X}_s'$.

We shall be only interested in the case in which $\bar{X}_s'$ has dimension $N-1$. This is the case, if there exists at least one point $x$ of $S(\Re(s))$ having the properties (1), (2) and (3) of Lemma (AB. 4). (See Corollary of Lemma (AB. 4).) Let us write $\tilde{X}$ for $\bar{X}_s'$. Let us consider a resolution datum $\Re_{11}^{N-1}$ on $\tilde{X}$ (without restriction) of the following form:

$$
\mathfrak {R} _ {\mathrm{II}} ^ {N - 1} = \left( \begin{array}{c c c} \widetilde {E} _ {1}, & \dots , & \widetilde {E} _ {\widetilde {\alpha}} \\ a _ {1}, & \dots , & a _ {\widetilde {\alpha}} \end{array} \right| \widetilde {J}, b),
$$

where $b$ is the positive integer defined above; the integers $a_j \geq 0 (1 \leq j \leq \tilde{\alpha})$ and the coherent sheaf of ideals $\tilde{J}$ on $\tilde{X}$ are such that

$$
\tilde {J} \left(\prod_ {j = 1} ^ {\tilde {\alpha}} \tilde {P} _ {j} ^ {a j}\right) = \bar {J} (s),
$$

where $\tilde{P}_j =$ the sheaf of prime ideals of $\tilde{E}_j$ on $\tilde{X}$. (For example, we may choose $a_{j} = 0$ for all $j$.) Here $\bar{J}(s)$ is the sheaf of ideals on $\bar{X}_{s}^{\prime}$, which was previously defined.

REMARK 3. Let us recall that $S(\mathfrak{R}_{\mathrm{II}}^{N - 1})$ denotes the closed subset of $\widetilde{X}$ of those points $\widetilde{x}$ for which

$$
\sum_ {\widetilde {x} \in \widetilde {E} _ {i}} a _ {i} + \nu_ {\widetilde {x}} (\widetilde {J}) \geq b
$$

(or, equivalently, $\nu_{\tilde{x}}(\bar{J}(s)) \geq b$). By virtue of Lemma (AB. 5), Remark 1 and the assumption [(1)],

$$
c _ {s} \left(S \left(\Re_ {\mathrm{II}} ^ {N - 1}\right)\right) \subseteq S (\Re (s)) \cap g _ {s} ^ {- 1} \left(x _ {0}\right).
$$

We shall write $S_0(\Re(s)) \cap g_s^{-1}(x_0)$, which is by the assumption [(1)] a closed

and open subset of $S(\mathfrak{R}(s))$. We shall write $\tilde{g}$ for $\overline{g}_s' \colon \widetilde{X} \to \operatorname{Spec}(\widehat{\mathbf{S}}) = \widehat{X}_0$. The above inclusion shows that if $\widetilde{B}$ is any irreducible subscheme of $\widetilde{X}$ contained in $S(\mathfrak{R}_{\mathrm{II}}^{N-1})$, we have $\tilde{g}(\widetilde{B}) = \widehat{x}_0$ (the unique chosen point of $\widehat{X}_0$) so that, by Corollary of Lemma (AB. 3), $c_s$ induces an open immersion of $\widetilde{B}$ into a reduced irreducible subscheme $B_s$ of $X_s$, where $B_s$ is obtained as the closure of $c_s(\widetilde{B})$ in $X_s$.

REMARK 4. Let $\tilde{B}$ be any non-singular irreducible subscheme of $\tilde{X}$ such that the monoidal transformation $\tilde{f}_{\tilde{B}}$ of $\tilde{X}$ with center $\tilde{B}$ is permissible for the resolution datum $\Re_{11}^{N-1}$ on $\tilde{X}$. Let $B_s$ be the reduced irreducible subscheme of $X_s$ such that $c_s$ induces an open immersion $\tilde{B} \to B_s$. Then $B_s$ is contained in $W(s)$ and there exists an open dense subset $U_s$ of $B_s$ such that $c_s(\tilde{B}) \subseteq U_s$ and that the resolution datum

$$
\Re_ {I} ^ {N, n ^ {\prime}} (s) = \left(\bigcup_ {i = 1} ^ {\alpha + s} E _ {i} (s); V _ {1} (s), \dots , V _ {\beta} (s), W (s); B _ {s}\right),
$$

where $n' = \dim B_s$, is resolved at every point of $U_s$. In fact, first of all it is clear that $B_s \subseteq W(s)$ by Lemma (AB. 5). To prove the assertion, let $U_s$ be the open subset of $B_s$ which consists of those points at which the above $\Re_1^{N,n'}(s)$ is resolved. We want to show that $U_s$ contains the image $c_s(\tilde{B})$. By Lemma (AB. 6), if $\hat{x}$ is any point of $\tilde{B}$ and $x = c_s(\hat{x})$, then we have that $x$ is a simple point of $B_s$ and that all the $V_j(s) (1 \leq j \leq \beta)$ and $W(s)$ are normally flat along $B_s$ at $x$. To show that $\bigcup_{i=1}^{\alpha+s} E_i(s)$ has only normal crossings with $B_s$ at $x$, we note that if $S_s$ (resp. $\hat{S}_s$) is the local ring of $X_s$ at $x$ (resp. $\hat{X}_s$ at $\hat{x}$) then the canonical homomorphism $S_s \to \hat{S}_s$ transforms a regular system of parameters of $S_s$ into such a system of parameters of $\hat{S}_s$. (See Lemma (AB. 2).) For the case in which $\Re = (\Re_1^{N,n}, F)$, the permissibility of $\tilde{f}_{\tilde{B}}$ for $\Re_{II}^{N-1}$ implies that $\bigcup_{i=1}^{\alpha+s} c_s^{-1}(E_i(s))$ has only normal crossings with $\tilde{B}$ at $\hat{x}$. Therefore, by the above property of the homomorphism $S_s \to \hat{S}_s$, we can conclude that $\bigcup_{i=1}^{\alpha+s} E_i(s)$ has only normal crossings with $B_s$ at $x$. For the case in which $\Re = (\Re_1^{N,n}, U)$, the same arguments as above show that $\bigcup_{i=\alpha+1}^{\alpha+s} E_i(s)$ has only normal crossings with $B_s$ at $x$. By Remark 1 and Lemma (AB. 5), the point $x$ (in fact, every point of $B_s$) is contained in $S(\Re(s))$ and therefore the assumption [(2)] on the succession $g_s$ implies that, for $1 \leq i \leq \alpha$, either $E_i(s)$ does not contain $x$ or it contains all the irreducible components of $W(s)$ which contain $x$. Since $W(s)$ contains $B_s$, either $E_i(s)$ does not contain $x$ or it contains $B_s$. In view of this fact, we can again conclude that $\bigcup_{i=1}^{\alpha+s} E_i(s)$ has only normal crossings with $B_s$ at the point $x$.

REMARK 5. $\tilde{B}$ being as in Remark 4, it is clear that $B_{s}$ is contained in $W(s)\cap F(s)$ for the case in which $\Re = (\mathfrak{R}_{\mathrm{I}}^{N,n},F)$, and that $B_{s}$ is contained

in $W(s) - U(s)$ for the case in which $\Re = (\Re_{\mathrm{I}}^{N,n}, U)$. (For the second case, we refer to Remark 1 and Lemma (AB. 5).) It follows that any permissible monoidal transformation of $X_s$ for the resolution datum $(\Re_{\mathrm{I}}^{N,n'}(s), U_s)$ with open restriction $U_s$ is a permissible monoidal transformation of $X_s$ for the resolution datum $\Re(s)$, which is either $(\Re_{\mathrm{I}}^{N,n}(s), F(s))$ or $(\Re_{\mathrm{I}}^{N,n}(s), U(s))$, and moreover that, if $\Re_{\mathrm{I}}^{N,n'}(s)$ is resolved at every point of $B_s$, then the monoidal transformation of $X_s$ with center $B_s$ is permissible for $\Re(s)$.

By applying Theorem  $I_{2}^{N,n'}$  (with  $n' < n$ ) to the resolution datum  $(\mathfrak{R}_{\mathrm{I}}^{N,n'}(s), U_{s})$ , we can resolve  $\mathfrak{R}_{\mathrm{I}}^{N,n'}(s)$  by a finite permissible succession of monoidal transformations for  $(\mathfrak{R}_{\mathrm{I}}^{N,n'}(s), U_{s})$ . These monoidal transformations are successively permissible for  $\mathfrak{R}(s)$  and induce trivial monoidal transformations of  $\tilde{X}$  by Remarks 4 and 5. Therefore, by replacing the original succession  $g_{s}: X_{s} \to X$  to include the above succession, we may assume that the monoidal transformation with center  $B_{s}$  is permissible for  $\mathfrak{R}(s)$ , while the scheme  $\tilde{X}$  and the datum  $R_{II}^{N-1}$  are kept the same. Then the permissible monoidal transformation  $f_{B_{s}}$  of  $X_{s}$  with center  $B_{s}$  for  $\mathfrak{R}(s)$  induces the given permissible monoidal transformation  $\tilde{f}_{\tilde{B}}$  of  $\tilde{X}$  for  $R_{II}^{N-1}$ . Thus, applying Theorem II $_{2}^{N-1}$  to the resolution datum  $R_{II}^{N-1}$  on  $\tilde{X}$  (without restriction), we can prove that there exists a finite permissible succession of monoidal transformations of  $X_{s}$  for  $\mathfrak{R}(s)$ , which induces a permissible succession of monoidal transformations of  $\tilde{X}$  for  $R_{II}^{N-1}$  and which resolve the datum  $R_{II}^{N-1}$ . Therefore, by replacing the original succession  $g_{s}: X_{s} \to X$  to include such an additional succession, we may assume that  $R_{II}^{N-1}$  is resolved. This means that

$$
\nu_ {x} (\bar {J} (s)) <   b
$$

for every point $x$ of $\tilde{X} = \bar{X}_s'$. By virtue of Corollary of Lemma (AB. 4), it implies that there exists no point $x$ of $X_s$ having the properties (1), (2) and (3) of Lemma (AB. 4) with reference to the point $x_0 \in g_s(S(\Re(s)))$. Or, equivalently, if $x$ is any point of $X_s$ at which $X_s$ has dimension $N$ and such that $g_s(x) = x_0$, we have either

$$
\nu_ {x} ^ {*} \left(V _ {1} (s), \dots , V _ {\beta} (s), W (s) / X _ {s}\right) <   \nu_ {x _ {0}} ^ {*} \left(V _ {1}, \dots , V _ {\beta}, W / X\right)
$$

or, if they are equal,

$$
\tau_ {x} ^ {*} \left(V _ {1} (s), \dots , V _ {\beta} (s), W (s) / X _ {s}\right) > \tau_ {x _ {0}} ^ {*} \left(V _ {1}, \dots , V _ {\beta}, W / X\right).
$$

Now,  $g_{s}(S(\Re(s)))$  consists of a finite number of points at which X has dimension N, and therefore, repeating the above process at most a finite number of times, we achieve the demonstration of Theorems A\* and B\* (hence Theorems A and B).

## 4. Proofs of the implications (C) and (D).

Let X be a non-singular irreducible algebraic scheme of dimension  $N \geq 1$ . We shall consider a resolution datum R on X which is either of the form  $(\mathfrak{R}_{\mathrm{II}}^{N}, F)$  with closed restriction F, or  $R_{II}^{N}$  without restriction, where

$$
\mathfrak {R} _ {\mathrm{II}} ^ {N} = \left( \begin{array}{c c c} E _ {1}, & \dots , & E _ {\alpha} \\ a _ {1}, & \dots , & a _ {\alpha} \end{array} \right| J, b)  .
$$

Let us recall the definition of the symbols $S(\mathfrak{R}_{\mathrm{II}}^N)$, $S_*(\mathfrak{R}_{\mathrm{II}}^N)$, and $S_{\nu}(\mathfrak{R}_{\mathrm{II}}^N)$ with a non-negative integer $\nu$.

$$
\begin{array}{l} S (\mathfrak {R} _ {\mathrm{II}} ^ {N}) = \left\{x \in X \mid \sum_ {x \in E _ {i}} a _ {i} + \nu (J _ {x}) \geq b \right\}. \\ S _ {\nu} (\mathfrak {R} _ {\mathrm{II}} ^ {N}) = \left\{x \in S (\mathfrak {R} _ {\mathrm{II}} ^ {N}) \mid \nu (J _ {x}) \geq \nu \right\}. \\ S _ {*} (\mathfrak {R} _ {\mathrm{II}} ^ {N}) = S _ {\nu} (\mathfrak {R} _ {\mathrm{II}} ^ {N}) \end{array}
$$

$$
\text { with } \nu = \nu (\mathfrak {R} _ {\mathrm{II}} ^ {N})
$$

where

$$
\nu (\mathfrak {R} _ {\mathrm{II}} ^ {N}) = \max _ {x \in S (\mathfrak {R} _ {\mathrm{II}} ^ {N})} \left\{\nu (J _ {x}) \right\}.
$$

For the case in which $\Re = (\Re_{\mathrm{II}}^N, F)$, we shall use the following symbols:

$$
\begin{array}{l} S (\mathfrak {R}) = S (\mathfrak {R} _ {\mathrm{II}} ^ {N}) \cap F \\ S _ {\nu} (\mathfrak {R}) = S _ {\nu} (\mathfrak {R} _ {\mathrm{II}} ^ {N}) \cap F \end{array}
$$

and

$$
\nu (\mathfrak {R}) = \max _ {x \in S (\mathfrak {R})} \left\{\nu (J _ {x}) \right\},
$$

which denote the respective sets of points of X.

We shall prove the following Theorems C and D, which complete the inductive proof of all the theorems stated in Ch. I.

THEOREM C. Let $X$ and $\mathfrak{R} = (\mathfrak{R}_{\mathrm{II}}^N, F)$ be as above. Suppose Theorems $\Pi_1^{N'}$ with $N' < N$, Theorems $\mathrm{I}_2^{N',n'}$ with $n' < N' \leq N$, and Theorems $\Pi_2^{N'}$ with $N' < N$ were verified. Then, assuming that $\nu = \nu(\mathfrak{R}) = \nu(\mathfrak{R}_{\mathrm{II}}^N) > 0$, there exists a permissible succession of monoidal transformations $f: X' \to X$ for $\mathfrak{R}$, such that $S_{\nu}(f^*(\mathfrak{R}))$ is empty.

THEOREM D. Let $X$ and $\mathfrak{R} = \mathfrak{R}_{\Pi}^{N}$ (without restriction) be as above. Suppose Theorems $\Pi_{2}^{N''}$ with $N'' < N$, Theorems $\mathbf{I}_2^{N',n'}$ with $n' < N' \leq N$, and Theorem $\Pi_1^N$ were verified. Then there exists a permissible succession of monoidal transformations $f: X' \to X$ for $\mathfrak{R}$ such that $f^*(\mathfrak{R})$ is resolved at every point of $X'$, i.e., $S(f^*(\mathfrak{R}))$ is empty.

We shall consider the following Theorem D\*, which is a priori weaker than Theorem D, and shall prove that Theorem D follows Theorem D\*.

THEOREM D\*. Let the notation and the assumptions be the same as in Theorem D. We assume that $\nu = \nu(\mathfrak{R}) > 0$. Then there exists a permissible succession of monoidal transformations $f: X' \to X$ for $\mathfrak{R}$ such that $S_{\nu}(f^{*}(\mathfrak{R}))$ is empty.

If Theorem D\* is verified, then we can immediately conclude that there exists a permissible succession of monoidal transformations $f: X' \to X$ for $\Re = \Re_{\Pi}^{N}$, such that $S_{1}(f^{*}(\Re))$ is empty; that is to say, if

$$
f ^ {*} (\Re) = \left( \begin{array}{c c c} E _ {1} ^ {\prime}, & \dots , & E _ {\alpha^ {\prime}} ^ {\prime} \\ a _ {1} ^ {\prime}, & \dots , & a _ {\alpha^ {\prime}} ^ {\prime} \end{array} \right| J ^ {\prime}, b)
$$

then $J_{x'}'$ is equal to the local ring of $X'$ at every point $x' \in S(f^{*}(\mathfrak{R}))$. Then Theorem D follows by virtue of the following:

LEMMA (D.1). Let $X$ and $\mathfrak{R} = \mathfrak{R}_{\mathrm{II}}^{\mathbb{N}}$ be as above. We assume that $J_{x}$ is equal to the local ring of $X$ at every point $x$ of $S(\mathfrak{R})$. Then there exists a permissible succession of monoidal transformations $f: X' \to X$ for $\mathfrak{R}$, such that $S(f^{*}(\mathfrak{R}))$ is empty.

PROOF. As is easily seen, by replacing $X$ by $X - S(J)$ where $S(J) = \{x \in X | \nu(J_x) \geq 1\}$, we may assume that $J$ is the sheaf of local rings $O_x$ of $X$. We have

$$
\Re = \binom {E _ {1}, \dots , E _ {\alpha}} {a _ {1}, \dots , a _ {\alpha}} O _ {x}, b).
$$

Moreover we may assume that  $E_{i} \neq E_{j}$  if  $i \neq j$  and if  $E_{i}$  is not empty. (See the introductory paragraph of this chapter.) Note that the transform of R by any permissible succession of monoidal transformations of X for R has also these properties. Let us first introduce the following symbols:

$K_{r}^{\circ}(\Re) = \text{the set of those non-singular subschemes of } X \text{ of codimension } r \text{ which are irreducible components of } \bigcap_{i \in T_{r}} E_{i} \text{ for a subset } T_{r} \text{ of } r \text{ indices of } \{1, \cdots, \alpha\}.$

$$
A _ {r} (\mathfrak {R}) = \max _ {H \in K _ {r} ^ {0} (\quad)} \left\{\sum_ {E _ {i} \supseteq H} a _ {i} \right\}.
$$

$K_{r}(\Re) =$ the subset of $K_{r}^{0}(\Re)$ of those $H$ such that $A_{r}(\Re) = \sum_{E_{i}\supseteq H}a_{i}$.

$k_{r}(\Re) =$ the number of subschemes of $X$ belong to $K_{r}(\Re)$.

Now, let $r$ be the smallest integer (positive) such that $A_r(\mathfrak{R}) \geq b$, so that $A_s(\mathfrak{R}) < b$ for $1 \leq s < r$. Let $H$ be any one of the subschemes in $K_r(\mathfrak{R})$. It is clear that the monoidal transformation $f_H \colon X' \to X$ with center $H$ is permissible for $\mathfrak{R}$. Let $\mathfrak{R}' = f_H^*(\mathfrak{R})$. Then we claim that

(i) $A_{s}(\Re^{\prime}) < b$ for $1 \leq s < r$ (which is trivial if $r = 1$),

(ii) if $K_{r}(\mathfrak{R})$ consists of only $H$, then $A_{r}(\mathfrak{R}') < A_{r}(\mathfrak{R})$, and

(iii) if $K_r(\mathfrak{R})$ contains subschemes other than $H$ then $A_r(\mathfrak{R}') = A_r(\mathfrak{R})$ and $k_r(\mathfrak{R}') < k_r(\mathfrak{R})$.

It is obvious that if this is proved then Lemma (D.1) follows by induction. Take $T_r = \{i_1, \cdots, i_r\}$ such that $H$ is an irreducible component of $\bigcap_{i \in T_r} E_{i}$. Then we have $A_r(\Re) = a_{i_1} + \cdots + a_{i_r}$. Let $E_i'$ be the strict transform of $E_i(1 \leq i \leq \alpha)$ on $X'$, and $E_{\alpha+1}'$ the total transform of $H$ on $X'$. In case $r = 1$, we have $H = E_{i_1}$ for some index $i_1$ and $E_{i_1}'$ is empty, so that

$$
\Re^ {\prime} = \left( \begin{array}{l l l l l} E _ {1} ^ {\prime}, & \dots , & \emptyset , & \dots , & E _ {\alpha + 1} ^ {\prime} \\ a _ {1}, & \dots , & a _ {i _ {1}}, & \dots , & a _ {i _ {1}} - b \end{array} \right) O _ {x ^ {\prime}}, b)
$$

where $a_{i_1} - b = A_1(\Re) - b < A_1(\Re)$. This shows the assertion for $r = 1$. Let us consider the case in which $r > 1$. Then

$$
\Re^ {\prime} = \left( \begin{array}{c c c} E _ {1} ^ {\prime}, & \dots , & E _ {\alpha} ^ {\prime}, \\ a _ {1}, & \dots , & a _ {\alpha}, a _ {\alpha + 1} \end{array} \right| O _ {x ^ {\prime}}, b)
$$

where $a_{\alpha+1}=A_r(\mathfrak{R})-b$. To prove (i), let us take an arbitrary subscheme $G'$ of $X'$ contained in $K_s(\mathfrak{R}')$ with $1\leq s<r$. We want to prove $\sum_{E_i' \supseteq G'} a_i<b$. This is clear if $G'\not\subseteq E_{\alpha+1}'$. Suppose $G'\subseteq E_{\alpha+1}'$. Let $G'$ be an irreducible component of $E_{j_1}' \cap \cdots \cap E_{j_{s-1}}' \cap E_{\alpha+1}'$, where the $s$ indices are necessarily distinct. The image $f(G')$ is contained in $E_{j_1} \cap \cdots \cap E_{j_{s-1}} \cap H$. Take $i_a \in T_r$ which is different from any of $j_1, \cdots, j_{s-1}$. Then $E_{j_1} \cap \cdots \cap E_{j_{s-1}} \cap E_{i_a}$ has an irreducible component $G \in K_s(\mathfrak{R})$ containing $f(G')$. Therefore we have $a_{j_1} + \cdots + a_{j_{s-1}} + a_{i_a} \leq A_s(\mathfrak{R}) < b$. On the other hand, since $\bigcap_{i_a \neq i \in T_r} E_i$ is not empty (in fact, it contains $H$), it contains a subscheme of $X$ which belongs to $K_{r-1}(\mathfrak{R})$, and therefore we have $A_r(\mathfrak{R}) - a_{i_a} = (a_{i_1} + \cdots + a_{i_r}) - a_{i_a} \leq A_{r-1}(\mathfrak{R}) < b$, so that $a_{\alpha+1} = A_r(\mathfrak{R}) - b < a_{i_a}$. Combing this with the above inequality, we get

$$
\sum_ {E _ {t} ^ {\prime} \supset G ^ {\prime}} a _ {i} = a _ {j _ {1}} + \dots + a _ {j _ {s - 1}} + a _ {\alpha + 1} <   a _ {j _ {1}} + \dots + a _ {j _ {s - 1}} + a _ {i _ {a}} <   b.
$$

To prove (ii) and (iii), it suffices to show that if $G''$ is any subscheme of $X'$ contained in $K_r(\mathfrak{R}')$ then we have

$$
\left(\mathrm{ii} ^ {*}\right) \sum_ {E ^ {\prime} := G ^ {\prime \prime}} a _ {i} <   A _ {r} (\Re), \text { provided } G ^ {\prime \prime} \subset E _ {\alpha + 1} ^ {\prime}, \text { and }
$$

$$
\left(\text { iii } ^ {*}\right) \sum_ {E _ {i} ^ {\prime} \supset G ^ {\prime \prime}} a _ {i} = \sum_ {E _ {i} \supset f (G ^ {\prime \prime})} a _ {i}, \text {   provided   } G ^ {\prime \prime} \not \subset E _ {\alpha + 1} ^ {\prime}.
$$

(iii\*) is clear. To prove (ii\*), we let $G''$ be an irreducible component of $E_{j_1}' \cap \cdots \cap E_{j_{r-1}}' \cap E_{\alpha+1}'$. As above, we have $i_a \in T_r$ such that $E_{j_1} \cap \cdots \cap E_{j_{r-1}} \cap E_{i_a}$ is not empty, and hence it has an irreducible component belonging to $K_r(\mathfrak{R})$. Hence, we have

$$
a _ {j} + \dots + a _ {j _ {r - 1}} + a _ {i _ {a}} \leq A _ {r} (\mathfrak {R}).
$$

Since $a_{\alpha + 1}(= A_r(\Re) - b) < a_{i_a}$, we get

$$
\sum_ {E _ {i} ^ {\prime} \supset G ^ {\prime \prime}} a _ {i} = a _ {j _ {1}} + \dots + a _ {j _ {r - 1}} + a _ {\alpha + 1} <   a _ {j _ {1}} + \dots + a _ {j _ {r - 1}} + a _ {i _ {a}} \leq A _ {r} (\Re).\tag{q.e.d.}
$$

The following Lemma is clear by the definition of a transform of $\mathfrak{R}_{\mathrm{II}}^N$ by a permissible monoidal transformation. (See Definition 7 (II).)

LEMMA (D.2). Let $\Re = \Re_{\Pi}^{N}$ on $X$ be as in Theorem D\*, so that $\nu = \nu(\Re) > 0$. Let $f: X' \to X$ be a permissible monoidal transformation of $X$ with center $B$ for $\Re$, and $E'$ the total transform of $B$ on $X'$. Then $E'$ is not contained in $S_{\nu}(f^{*}(\Re))$.

In view of the Localization Theorem (Proposition 4, §1), the above Lemma (D.2) implies immediately that, R and ν being as above, there exists a permissible succession of monoidal transformations  $f: X' \to X$  for R such that  $S_{\nu}(f^{*}(\mathfrak{R}))$  does not contain any non-empty component of codimension 1. Moreover, after this is done, this property continues to hold by any permissible monoidal transformation. Thus in the proof of Theorem D\*, we may assume that  $S_{\nu}(\mathfrak{R})$  has no non-empty component of codimension 1 in X. A comparatively trivial observation shows that we may also assume the same for Theorem C.

We shall prove Theorem C and Theorem D\* under the above assumption, which completes the proof of Theorem D as well.

Let us first fix and study an arbitrary permissible succession of monoidal transformations of X for R (which is either  $(\Re_{\mathrm{II}}^{N}, F)$  or  $\Re_{II}^{N}$  as above), say

$$
\{f _ {s} \colon X _ {s + 1} \rightarrow X _ {s} \}\tag{\((s \geq 0)\}
$$

where $X_0 = X$. Let $B_s$ denote the center of the monoidal transformation $f_s$ in $X_s$. Let $\Re(s)$ and $\Re_{\mathrm{II}}^N(s)$ be the resolution data on $X_s$ ($s \geq 0$) which are defined as follows: $\Re(0) = \Re$, $\Re_{\mathrm{II}}^N(0) = \Re_{\mathrm{II}}^N$, $\Re(s + 1) = f_s^*(\Re(s))$, and $\Re_{\mathrm{II}}^N(s + 1) = f_s^*(\Re_{\mathrm{II}}^N(s))$ for all $s \geq 0$. Let us write

$$
\mathfrak {R} _ {\mathrm{II}} ^ {N} (s) = \left( \begin{array}{c c c} E _ {1} (s), & \dots , & E _ {\alpha + s} (s) \\ a _ {1}, & \dots , & a _ {\alpha + s} \end{array} \right| J (s), b)
$$

where $E_{i}(0) = E_{i}(1 \leq i \leq \alpha)$, $E_{i}(s + 1) =$ the strict transform of $E_{i}(s)$ in $X_{s+1}(1 \leq i \leq \alpha + s)$, and $E_{\alpha + s + 1}(s + 1) =$ the total transform of $B_{s}$ in $X_{s+1}(s \geq 0)$. If $\Re = (\Re_{\mathrm{II}}^{N}, F)$, we shall write $\Re(s) = (\Re_{\mathrm{II}}^{N}(s), F(s))$ so that $F(s + 1) =$ the strict transform of $F(s)$ for all $s \geq 0$ where $F(0) = F$.

Let us choose and fix an arbitrary point $x_0$ of $X_0$ at which $X$ has dimension $N$ and which is contained in $S_{\nu}(\Re)(\nu = \nu(\Re) > 0)$. Let $\mathbf{S}_0$ denote the local ring of $X_0$ at $x_0$ and $\hat{\mathbf{S}}_0$ the completion of $\mathbf{S}_0$. Let $\hat{X}_0 = \operatorname{Spec}(\hat{\mathbf{S}}_0)$ and $c_0: \hat{X}_0 \to X_0$ the canonical morphism associated with the canonical local homomorphism $\mathbf{S}_0 \to \hat{\mathbf{S}}_0$. We shall denote by $\hat{x}_0$ the unique closed point of $\hat{X}_0$, so that $c_0(\hat{x}_0) = x_0$. Let us write $\mathbf{J}_0$ for the stalk $\mathbf{J}_{x_0}$ of $J$ at $x_0$. Let $\mathbf{M}_0$ denote the maximal ideal of $\mathbf{S}_0$. Then we have $\nu_{\mathbf{M}_0}(\mathbf{J}_0) = \nu$.

Let $\hat{\mathbf{J}}_0 = \mathbf{J}_0\hat{\mathbf{S}}_0$, and choose and fix a base of $\hat{\mathbf{J}}_0$, say

[0] $(g_{1},\dots ,g_{m})\hat{\mathbf{S}}_{0} = \hat{\mathbf{J}}_{0},$

such that  $\nu_{\mathbf{M}_{0}}(g_{j})=\nu$  for all j ( $1\leq j\leq m$ ). The complete regular local ring  $S_{0}$  contains a field k such that  $\hat{S}_{0}$  is a formal power series ring of N variables over k. We fix such a subfield k of  $\hat{S}_{0}$ . Let us choose and fix a regular frame  $(\mathbf{T}_{0};z_{0})$  of  $S_{0}$  as follows:

[ i ] If $\Re = (\Re_{\mathrm{II}}^N, F)$, then $z_0$ is an element of $\mathbf{S}_0$ which generates the ideal of $F$ in $\mathbf{S}_0$ (hence, the ideal of $c_0^{-1}(F)$ in $\hat{\mathbf{S}}_0$).

[ii]  $T_{0}$  is a formal power series of N-1 variables  $(y_{1},\cdots,y_{N-1})$  over k such that  $(z_{0},y_{1},\cdots,y_{N-1})$  is a regular system of parameters of  $\hat{S}_{0}$ .

[iii]  $(y_{1},\cdots,y_{N-1})$  is so chosen that each  $g_{i}$  can be written in the form

$$
g _ {j} = u _ {j} \left(z _ {0} ^ {\nu} + g _ {j 1} z _ {0} ^ {\nu - 1} + \dots + g _ {j \nu}\right)
$$

where $u_j$ is a unit of $\hat{\mathbf{S}}_0$ and $g_{ji} \in \mathbf{T}_0$ ($1 \leq j \leq m, 1 \leq i \leq \nu$).

[iv] If $\Re = \Re_{\mathrm{II}}^{N}$ without restriction, then $z_0$ is so chosen that $g_{11} = 0$, i.e.,

$$
g _ {1} = u _ {1} (z _ {0} ^ {\nu} + g _ {1 2} z _ {0} ^ {\nu - 2} + \dots + g _ {1 \nu}) .
$$

(In [iii] we replace $z_0$ by $z_0 + (1 / \nu)g_{11}$.) We may assume without any loss of generality that $u_j = 1$ for all $j(1 \leq j \leq m)$. We have

[0] $\hat{\mathbf{J}}_0 = (g_1, \dots, g_m)\hat{\mathbf{S}}_0$, and

[iii] $g_{j}=z_{0}^{\nu}+g_{j1}z_{0}^{\nu-1}+\cdots+g_{j\nu}(1\leq j\leq m)(g_{11}=0\text{ if }\Re=\Re_{11}^{N})$ where $g_{ji}\in T_{0}$.

We define a sequence of non-singular irreducible algebraic schemes  $\hat{X}_{s}(s\geq0)$  (over the complete regular local ring  $\hat{S}_{0}$ ) as follows:  $\hat{X}_{0}=\operatorname{Spec}(\hat{\mathbf{S}}_{0})$  and  $c_{0}:\hat{X}_{0}\to X_{0}$  being as above, we have commutative diagrams of canonical morphisms

$$
\begin{array}{c c c} \widehat {X} _ {s + 1} & \xrightarrow {c _ {s + 1}} & X _ {s + 1} \\ \Big \downarrow \hat {f} _ {s} & & \Big \downarrow f _ {s} \\ \widehat {X} _ {s} & \xrightarrow {c _ {s}} & X _ {s} \end{array}\tag{\((s \geq 0)\}
$$

where  $\hat{f}_{s}$  is the monoidal transformation of  $X_{s}$  with the non-singular irreducible center  $\hat{B}_{s}=c_{s}^{-1}(B_{s})$ . Here we remark, as in the previous section, the following fact.

LEMMA (CD. 3). Let $h_s$ (resp. $\hat{h}_s$) denote the succession of the monoidal transformations $f_t$ (resp. $\hat{f}_t$) for $0 \leq t \leq s - 1$. Then the canonical morphism $c_s$ induces a bijection of the points sets: $\bar{h}_{s}^{-1}(\hat{x}_0) \to h_{s}^{-1}(x_0)$, and, if $\hat{x} \in \hat{h}_s^{-1}(\hat{x}_0)$ and $x = c_s(\hat{x}) \in h_s^{-1}(x_0)$, then the local homomorphism of the

local ring of $X_s$ at $x$ into that of $\hat{X}_s$ at $\hat{x}$, induced by $c_s$, transforms a regular system of parameters into such a system of parameters. Moreover, if $\hat{B}$ is any irreducible subscheme of $\hat{X}_s$ such that that $\hat{h}_s(\hat{B}) = \hat{x}_0$, there exists a unique irreducible subscheme $B$ of $X_s$ such that $\hat{B} = c_s^{-1}(B)$, that $B = c_s(\hat{B})$ and that $c_s$ induces an isomorphism $\hat{B} \to B$.

Let $\bar{\mathbf{T}}_0 = \hat{\mathbf{S}}_0 / (z_0)\hat{\mathbf{S}}_0$, which is an isomorphic image of the subring $\mathbf{T}_0$ of $\mathbf{S}_0$. Let $\bar{X}_0 = \operatorname{Spec}(\bar{\mathbf{T}}_0)$, which is a non-singular irreducible subscheme of $\hat{X}_0$ of codimension 1. We define a positive integer $\bar{b}$ and a coherent sheaf of ideals $\bar{J}(0)$ on $\bar{X}_0$ as follows:

[v] $\bar{b} = \nu!$, and

[vi] $\bar{J} (0)$ is generated by the ideal

$$
\overline {{{{\mathbf {J}}}}} _ {0} = (g _ {j i} ^ {\bar {b} / i}) \overline {{{{\mathbf {T}}}}} _ {0}
$$

in $\bar{\mathbf{T}}_0$, which denotes the ideal generated by the images in $\bar{\mathbf{T}}_0$ of the $(\overline{b}/i)^{\mathrm{th}}$ powers of $g_{ji} \in \mathbf{T}_0$ for $1 \leq j \leq m$ and $1 \leq i \leq \nu$. Let $\bar{X}_s$ be the strict transform of $\bar{X}_0$ in $\hat{X}_s$ by the succession $\hat{h}_s: \hat{X}_s \to \hat{X}_0$ for all $s \geq 0$. Then $\bar{X}_s$ is an irreducible reduced subscheme of $\hat{X}_s$ and, for each $s \geq 0$, the morphism $\hat{f}_s: \hat{X}_{s+1} \to \hat{X}_s$ (resp. $\hat{h}_s: \hat{X}_s \to \hat{X}_0$) induces a morphism $\bar{f}_s: \bar{X}_{s+1} \to \bar{X}_s$ (resp. $\bar{h}_s: \bar{X}_s \to \bar{X}_0$).

[vii] We define a coherent sheaf of ideals $\bar{J}(s)$ on $\bar{X}_s$ by induction on $s \geq 0$ as follows: If, for a certain integer $s \geq 0$,

(1) $\bar{X}_s$ is non-singular and irreducible,

(2) $\hat{B}_s$ is contained in $\bar{X}_s$, so that the morphism $\bar{f}_s: \bar{X}_{s+1} \to \bar{X}_s$ is obtained by the monoidal transformation of $\bar{X}_s$ with the non-singular center $\hat{B}_s$, and

(3) $\bar{J}(s)$ is defined and contained in the $\bar{b}^{\text{th}}$ power of the sheaf of prime ideals of $\hat{B}_s$ on $\bar{X}_s$, then we define $\bar{J}(s+1)=\bar{f}_s^{-1}\big(\bar{J}(s)\big)/(\bar{P}_{s+1})^\bar{b}$, where $\bar{P}_{s+1}$ denotes the sheaf of invertible ideals of the subscheme

$$
c _ {s} ^ {- 1} \left(E _ {\alpha + s + 1} (s + 1)\right) \cap \bar {X} _ {s + 1}
$$

of the non-singular algebraic scheme  $\bar{X}_{s+1}$ ; this subscheme is also the total transform of  $\hat{B}_{s}$  in  $\bar{X}_{s+1}$ .

LEMMA (CD. 4). If $s$ is any non-negative integer such that $S_{\nu}(h_{s}^{*}(\mathfrak{R}))$ is not empty, the above conditions (1), (2) and (3) of [vii] are satisfied. (Note that $\hat{B}_{s}$ may be empty.)

PROOF. First of all, we remark that (1) is true for s = 0 and can be verified for  $s + 1$  if both (1) and (2) are done for some  $s \geq 0$ , and that (2) and (3) are trivially true if  $\hat{B}_{s}$  is empty. Therefore, to prove Lemma (CD. 4), we shall assume that  $\hat{B}_{s}$  is not empty. Let  $\hat{x}'$  be any point of  $\hat{B}_{s}$  and  $x' = c_{s}(\hat{x}')$ . Let  $\hat{x}_{t}'$  (resp.  $x_{t}'$ ) be the image of  $\hat{x}'$  (resp.  $x'$ ) in  $\hat{X}_{t}$  (resp.

$X_{t})$ , for  $0 \leq t \leq s$ . We have  $c_{t}(\hat{x}_{t}^{\prime}) = x_{t}^{\prime}$  for all t. We set the symbols as follows:

$\mathbf{S}_t^\prime =$ the local ring of $X_{t}$ at $x_{t}^{\prime}$

$\hat{\mathbf{S}}_t^\prime =$ the local ring of $\hat{X}_t$ at $\hat{x}_t^\prime$

$\mathbf{Q}_t^\prime =$ the ideal of $B_{t}$ in $\mathbf{S}_t^\prime$

$$
\hat {\mathbf {Q}} _ {t} ^ {\prime} = \mathbf {Q} _ {t} ^ {\prime} \hat {\mathbf {S}} _ {t} ^ {\prime} = \text { the   ideal   of } \hat {B} _ {t} \text { in } \hat {\mathbf {S}} _ {t} ^ {\prime}
$$

$$
\mathbf {J} _ {t} ^ {\prime} = J (t) _ {x _ {t} ^ {\prime}} = \text { the   stalk   of } J (t) \text { at } x _ {t} ^ {\prime}
$$

$$
\hat {\mathbf {J}} _ {t} ^ {\prime} = \mathbf {J} _ {t} ^ {\prime} \hat {\mathbf {S}} _ {t} ^ {\prime}
$$

where $0 \leq t \leq s$.

We claim that there exist a regular frame  $(\mathbf{T}_{t}^{\prime}; z_{t})$  of  $\hat{S}_{t}^{\prime}$ , elements  $g_{j}(t) \in \hat{\mathbf{S}}_{t}^{\prime} (1 \leq j \leq m)$ , and an element  $v_{t} \in T_{t}^{\prime}$  for all  $t (0 \leq t \leq s)$  such that:

(a) $_{t}$$\hat{x}_{t}^{\prime}$  is a point of  $\bar{X}_{t}$  and the regular frame  $(\mathbf{T}_{t}^{\prime}; z_{t})$  of  $\hat{S}_{t}^{\prime}$  is such that  $z_{t}$  generates the kernel of the canonical homomorphism  $\hat{S}_{t}^{\prime} \to \bar{T}_{t}^{\prime}$ , where  $\bar{T}_{t}^{\prime}$  denotes the local ring of  $\bar{X}_{t}$  at  $\hat{x}_{t}^{\prime}$ ,

(b) $_{t}\left(g_{1}(t),\cdots,g_{m}(t)\right)$ is a base of the ideal $\hat{J}_{t}^{\prime}$ and each $g_{j}(t)$ can be written as

$$
g _ {j} (t) = z _ {t} ^ {\nu} + g _ {j 1} (t) z _ {t} ^ {\nu - 1} + \dots + g _ {j \nu} (t)
$$

where $g_{ji}(t)\in \mathbf{T}_t^\prime$ for $1\leq i\leq \nu$

(c) $_{t}$  if  $R = R_{II}^{N}$  without restriction, we have  $g_{11}(t) = 0$ ,

(d) the stalk of $\bar{J}(t)$ at $\hat{x}_t'$, denoted by $\bar{\mathbf{J}}_t'$, is generated by the images of the $(\bar{b}/i)^{\text{th}}$ powers of $g_{ji}(t)$ in $\bar{\mathbf{T}}_t'$ for $1 \leq j \leq m$ and $1 \leq i \leq \nu$. In symbol,

$$
\overline {{{{\mathbf {J}}}}} _ {t} ^ {\prime} = \left(g _ {j i} (t) ^ {\bar {b} / i}\right) \overline {{{{\mathbf {T}}}}} _ {t} ^ {\prime}.
$$

(e) $z_{t+1} = z_t / v_t$, i.e., $(\mathbf{T}_{t+1}'; z_{t+1})$ is a frame transform of $(\mathbf{T}_t', z_t)$ in $\hat{\mathbf{S}}_{t+1}'$ with denominator $v_t$, provided $t + 1 \leq s$,

$$
(\mathbf {f}) _ {t} g _ {j} (t + 1) = g _ {j} (t) / v _ {t} ^ {\nu} (1 \leq j \leq m).
$$

The proof of their existence will be done by induction on  $t \geq 0$ . By assumption,  $x' \in B_s \subseteq S_\nu(h_s^*(\Re))$  and therefore  $x'_t \in S_\nu(h_t^*(\Re))$  for all  $t (0 \leq t \leq s)$ . In particular,  $x'_0 \in S_\nu(\Re)$  implies that  $J'_0$  is contained in the  $\nu^{th}$  power of the maximal ideal of  $S'_0$ . Hence  $\hat{J}_0'$  is contained in the  $\nu^{th}$  power of the maximal ideal of  $\hat{S}_0'$ . Let  $\hat{P}$  be the prime ideal of  $\hat{x}_0'$  in  $\hat{S}_0$ , so that  $\hat{S}_0' = (\hat{S}_0)_{\hat{P}}$ . We have fixed a regular frame  $(T_0; z_0)$  of  $\hat{S}_0$ , and a base  $(g_1, \cdots, g_m)$  of  $\hat{J}_0$  having the properties [i]–[iv] (including [iii]'). We want to prove that  $\hat{P}$  contains  $z_0$ . This is clear for the case in which  $R = (\Re_{II}^N, F')$ . As for the other case in which  $R = R_{II}^N$ , we refer to Lemma 22, § 10, Ch. III. Namely, we have  $g_1 = z_0^\gamma + g_{12}z_0^{\gamma-2} + \cdots + g_{1\nu}$  with  $g_{1i} \in T_0$  and  $\nu_{\hat{P}(\hat{S}_0)\hat{P}}(f_1) \geq \nu$ , so that  $z_0 \in \hat{P}$ . This shows that  $\hat{x}_0'$  is a point of  $\bar{X}_0$  and that, if  $T'_0$  is the

localization of $\mathbf{T}_0$ with respect to $\hat{\mathbf{P}} \cap \mathbf{T}_0$, $(\mathbf{T}_0'; z_0)$ is a regular frame of $\hat{\mathbf{S}}_0'$. Let $g_j(0) = g_j (1 \leq j \leq m)$ and $g_{ji}(0) = g_{ji} (1 \leq j \leq m, 1 \leq i \leq \nu)$. Then the conditions $(\mathbf{a})_0 - (\mathbf{d})_0$ are clearly satisfied. Let us assume that $(a)_t - (\mathbf{d})_t$ are verified for a certain integer $t \geq 0$. We shall prove that $(\mathbf{T}_t'; z_t)$ admits a frame transform $(\mathbf{T}_{t+1}', z_{t+1})$ in $\hat{\mathbf{S}}_{t+1}'$ where $z_{t+1} = z_t / v_t$ with a suitable element $v_t$ of $\mathbf{T}_t'$, provided $t + 1 \leq s$. We note that, the existence of $(\mathbf{T}_{t+1}', z_{t+1})$ with $v_t \in \mathbf{T}_t'$ being verified, $(\mathbf{a})_{t+1} - (\mathbf{d})_{t+1}$ follows if we define $g_j(t + 1)$ for $1 \leq j \leq m$ as in $(\mathbf{f})_t$. Now, since $B_t$ is contained in $S_\nu(h_t^*(\Re))$, $\mathbf{J}_t'$ is contained in the $\nu^{\text{th}}$ power of the ideal $\mathbf{Q}_t'$. Hence $\hat{\mathbf{J}}_t' \subseteq (\hat{\mathbf{Q}}_t')^\nu$, i.e.,

$$
g _ {j} (t) = z _ {t} ^ {\nu} + g _ {j 1} (t) z _ {t} ^ {\nu - 1} + \dots + g _ {j \nu} (t) \in (\hat {\mathbf {Q}} _ {t} ^ {\prime}) ^ {\nu}
$$

for all $j(1 \leq j \leq m)$. In view of (c)$_t$, it then follows from Lemma 22, § 10, Ch. III, that $z_t \in \hat{\mathbf{Q}}_t'$ for the case in which $\Re = \Re_{\text{II}}^N$. This is clear for the other case in which $\Re = (\Re_{\text{II}}^N, F)$. Moreover, in both cases, it then follows that $g_{ji}(t) \in (\hat{\mathbf{Q}}_t' \cap \mathbf{T}_t')^i$ for all $i$ and $j$ ($1 \leq i \leq \nu$, $1 \leq j \leq m$). To find $v_t \in \mathbf{T}_t'$ having the above properties, let us first take any element $w_t$ of $\hat{\mathbf{S}}_t'$ such that $(w_t)\hat{\mathbf{S}}_{t+1}' = \hat{\mathbf{Q}}_t\hat{\mathbf{S}}_{t+1}'$. Then the $g_j(t)/w_t^\nu$ for $1 \leq j \leq m$ should form a base of $\hat{\mathbf{J}}_{t+1}'$. Hence,

$$
g _ {j} (t) / w _ {t} ^ {\nu} = \left(z _ {t} / w _ {t}\right) ^ {\nu} + \left(g _ {j 1} (t) / w _ {t}\right) \left(z _ {t} / w _ {t}\right) ^ {\nu - 1} + \dots + g _ {j \nu} (t) / w _ {t} ^ {\nu}
$$

must be in the $\nu^{\text{th}}$ power of the maximal ideal of $\hat{\mathbf{S}}_{t+1}^{\prime}$. Hence $w_{t}^{-1}(\hat{\mathbf{Q}}_{t}^{\prime} \cap \mathbf{T}_{t}^{\prime})\hat{\mathbf{S}}_{t+1}^{\prime}$ is the unit ideal. (In fact, if otherwise, $z_{t}/w_{t}$ should be a unit and therefore $g_{j}(t)/w_{t}^{\vee}$ should be a unit. This contradicts the above fact.) Therefore we have $v_{t} \in \mathbf{T}_{t}^{\prime}$ such that $w_{t}/v_{t}$ is a unit in $\hat{\mathbf{S}}_{t+1}^{\prime}$, i.e., $(v_{t})\hat{\mathbf{S}}_{t+1}^{\prime} = \hat{\mathbf{Q}}_{t}^{\prime}\hat{\mathbf{S}}_{t+1}^{\prime}$. Now, it is clear that $z_{t+1} = z_{t}/v_{t}$ generates the ideal of $\bar{X}_{t+1}$ in $\hat{\mathbf{S}}_{t+1}^{\prime}$. Clearly $z_{t+1}$ is a non-unit for the case in which $\Re = (\Re_{\Pi}^{N}, F)$, because

$$
x _ {t + 1} ^ {\prime} \in S _ {\nu} \left(h _ {t + 1} ^ {*} (\mathfrak {R})\right) = S _ {\nu} \left(h _ {t + 1} ^ {*} \left(\mathfrak {R} _ {\mathrm{II}} ^ {N}\right)\right) \cap F (t + 1).
$$

For the other case, we apply Lemma 22, § 10, Ch. III, to

$$
g _ {1} (t) / v _ {t} = z _ {t + 1} ^ {\nu} + \left(g _ {1 2} (t) / v _ {t} ^ {2}\right) z _ {t + 1} ^ {\nu - 2} + \dots + \left(g _ {1 \nu} (t) / v _ {t} ^ {\nu}\right)
$$

which is contained in the  $\nu^{th}$  power of the maximal ideal of  $\hat{S}_{t+1}^{\prime}$ . Thus the existence proof is completed. The conditions (1), (2) and (3) of [vii] follow from the above results  $(\mathbf{a})_{s} - (\mathbf{d})_{s}$ . q.e.d.

COROLLARY. Let $x$ be any point of $h_s^{-1}(x_0) \cap S_\nu(h_s^*(\mathfrak{R}))$, and $\hat{x}$ the unique point of $\hat{h}_s^{-1}(\hat{x}_0)$ such that $c_s(\hat{x}) = x$. Then $\hat{x}$ is a point of $\bar{X}_s$ and the stalk of $\bar{J}(s)$ at $\hat{x}$ is contained in the $\overline{b}^{\text{th}}$ power of the maximal ideal, i.e., $\nu(\bar{J}(s)_\hat{x}) \geq \overline{b}$.

PROOF. The closure B of  $\{x\}$  in  $X_{s}$  may be viewed as an irreducible

reduced subscheme of $X_s$, and there exists a unique subscheme $\hat{B}$ of $\hat{X}_s$ such that $c_s \colon \hat{X}_s \to X_s$ induces an isomorphism $\hat{B} \to B$. $\hat{x}$ is the generic point of $\hat{B}$, and $\hat{B}$ is an algebraic scheme over a field (i.e., over the residue field of $\hat{\mathbf{S}}$, where $\hat{\mathbf{S}}$ is the local ring of $\hat{X}_0$ at $\hat{x}_0$). Therefore, we have only to prove the assertion for the case in which $\hat{x}$ is a closed point of $\hat{X}_s$, hence, $x$ is a closed point of $X_s$. In this case, the monoidal transformation of $X_s$ with center $x$ is permissible for the resolution datum $\Re$. Applying Lemma (CD. 4) to $B_s = x$, we get the assertion of the corollary. q.e.d.

LEMMA (CD. 5). Let $\hat{x}'$ be any point of $\bar{X}_s$ such that $\nu(\bar{J}(s)_{\hat{x}'}) \geq \bar{b}$, and $x' = c_s(\hat{x}')$. Then we have $\nu(J(s)_{x'}) \geq \nu$.

PROOF. Let $\hat{x}_t'$ (resp. $x_t'$) be the image of $\hat{x}'$ (resp. $x'$) in $\hat{X}_t$ (resp. $X_t$) for $0 \leq t \leq s$. We set the symbols $\mathbf{S}_t', \hat{\mathbf{S}}_t', \mathbf{Q}_t', \hat{\mathbf{Q}}_t', \mathbf{J}_t'$ and $\hat{\mathbf{J}}_t'$ for $0 \leq t \leq s$ as in the proof of Lemma (CD. 4). We note that $\hat{x}_t'$ is a point of $\bar{X}_t$ for all $t$ ($0 \leq t \leq s$). Let $\bar{\mathbf{T}}_t'$ be the local ring of $\bar{X}_t$ at $\hat{x}_t'$ for $0 \leq t \leq s$. We claim that there exists a regular frame $(\mathbf{T}_t'; z_t)$ of $\hat{\mathbf{S}}_t'$, elements $g_t(t) \in \hat{\mathbf{S}}_t'(1 \leq j \leq m)$, and an element $v_t \in \mathbf{T}_t'$ for all $t(0 \leq t \leq s)$ such that:

$(\mathbf{a}^{*})_{t}$$z_{t}$ generates the kernel of the canonical homomorphism $\hat{\mathbf{S}}_t^\prime \to \bar{\mathbf{T}}_t^\prime$

$(\mathbf{b}^{*})_{t}\left(g_{1}(t),\dots ,g_{m}(t)\right)$ is a base of $\widehat{\mathbf{J}}_t^\prime$ , and each $g_{j}(t)$ can be written as

$$
g _ {j} (t) = z _ {t} ^ {\nu} + g _ {j 1} (t) z _ {t} ^ {\nu - 1} + \dots + g _ {j \nu} (t),
$$

where $g_{ji}(t) \in \mathbf{T}_t'$ for $1 \leq j \leq m$ and $1 \leq i \leq \nu$,

$(\mathbf{c}^{*})_{t}$ the stalk $\bar{\mathbf{J}}_t^\prime$ of $\bar{J} (t)$ at $\hat{x}_t^\prime$ is written as

$$
\overline {{{\mathbf {J}}}} _ {t} ^ {\prime} = \left(g _ {j i} (t) ^ {\bar {b} / i}\right) \overline {{{\mathbf {T}}}} _ {t} ^ {\prime}.
$$

$(\mathrm{d}^{*})_{t} z_{t + 1} = z_{t} / v_{t}$, and $g_{j}(t + 1) = g_{j}(t) / v_{t}^{\nu}$ for $1 \leq j \leq m$, provided $t + 1 \leq s$.

The proof of their existence will be done by induction on $t$ ($0 \leq t \leq s$). We first remark that in order for $\bar{J}(s)$ to be defined, $\hat{\mathbf{Q}}_t'$ must contain the kernel of $\hat{\mathbf{S}}_t' \to \overline{\mathbf{T}}_t'$, $\overline{\mathbf{J}}_t'$ must be contained in the $\bar{b}^{\text{th}}$ power of the image $\overline{\mathbf{Q}}_t'$ of $\hat{\mathbf{Q}}_t'$ in $\overline{\mathbf{T}}_t'$, and $\overline{\mathbf{T}}_{t+1}'$ must be a monoidal transform of $\overline{\mathbf{T}}_t'$ with center $\overline{\mathbf{Q}}_t'$ for all $t \leq s - 1$. (Recall (1), (2) and (3) of (vii) in the paragraph preceding Lemma (CD. 4).) Therefore the assumption that $\nu(\bar{J}(s)_{\hat{x}'}) \geq \bar{b}$, implies that $\overline{\mathbf{J}}_t'$ is contained in the $\bar{b}^{\text{th}}$ power of the maximal ideal of $\overline{\mathbf{T}}_t'$ for all $t$ ($0 \leq t \leq s$). Let us take the regular frame $(\mathbf{T}_0'; z_0)$ of $\hat{\mathbf{S}}_0'$ and $g_j(0) = g_j \in \hat{\mathbf{S}}_0'$ ($1 \leq j \leq m$) that we defined in the proof of Lemma (CD. 4). Then $(\mathbf{a}^*)_0 - (\mathbf{c}^*)_0$ are clear. Suppose we have established $(\mathbf{a}^*)_t - (\mathbf{c}^*)_t$ for some $t$ such that $0 \leq t \leq s - 1$. We want to prove that, if $v_t$ is an element of $\mathbf{T}_t'$ such that $(v_t)\hat{\mathbf{S}}_{t+1}' = \hat{\mathbf{Q}}_t'\hat{\mathbf{S}}_{t+1}$ (such an element $v_t$ obviously exists), then the conditions $(\mathbf{a}^*)_{t+1} - (\mathbf{c}^*)_{t+1}$ are satisfied by $z_{t+1}$ and $g_j(t+1)(1 \leq j \leq m)$.

defined as in $(\mathbf{d}^*)_t$. This is trivially true if $\hat{\mathbf{Q}}_t'$ is the unit ideal. Suppose $\hat{\mathbf{Q}}_t'$ is not the unit ideal. Then $\hat{\mathbf{Q}}_t'$ is a prime ideal such that $\hat{\mathbf{S}}_t'/\hat{\mathbf{Q}}_t'$ is regular. Let $\bar{\mathbf{Q}}_t' = \hat{\mathbf{Q}}_t'/(z_t)\hat{\mathbf{S}}_t'$ as above. Then we have $\bar{\mathbf{J}}_t' \subseteq (\bar{\mathbf{Q}}_t')^\bar{b}$, i.e., $g_{ji}(t) \in (\hat{\mathbf{Q}}_t' \cap \mathbf{T}_t')^i$ for all $j$ and $i$ ($1 \leq j \leq m$, $1 \leq i \leq \nu$). Since $z_t \in \hat{\mathbf{Q}}_t'$, it follows that $g_j(t) \in (\hat{\mathbf{Q}}_t')^\nu$ for all $j$ ($1 \leq j \leq m$), i.e., $\hat{\mathbf{J}}_t' \subseteq (\hat{\mathbf{Q}}_t')^\nu$. Now that this inclusion is verified, $(\mathbf{a}^*)_{t+1} - (\mathbf{c}^*)_{t+1}$ are immediate if we define $z_{t+1}$ and $g_j(t+1)$ ($1 \leq j \leq m$) as it $(\mathbf{d}^*)_t$, and if we take the frame transform $(\mathbf{T}_{t+1}', z_{t+1})$ of $(\mathbf{T}_t'; z_t)$ in $\hat{\mathbf{S}}_{t+1}'$. We have thus established $(\mathbf{a}^*)_s - (\mathbf{c}^*)_s$. The assumption $\nu(\bar{J}(s)_{\hat{x}'}) \geq \bar{b}$ implies that, by $(\mathbf{c}^*)_s$, $g_{ji}(s)$ is contained in the $i^{th}$ power of the maximal ideal of $\hat{\mathbf{S}}_s'$ for all $j$ and $i$ ($1 \leq j \leq m$, $1 \leq i \leq \nu$). Hence, by $(\mathbf{b}^*)_s$, $\hat{\mathbf{J}}_s'$ is contained in the $\nu^{th}$ power of the maximal ideal of $\hat{\mathbf{S}}_s'$. We can see that the local homomorphism $\mathbf{S}_s' \to \hat{\mathbf{S}}_s'$ transforms a regular system of parameters of $\mathbf{S}_s'$ into a system of elements of $\hat{\mathbf{S}}_s'$ which can be extended to a regular system of parameters of $\hat{\mathbf{S}}_s'$. (This can be easily deduced from the fact that $\hat{X}_s = X_s \times_x\text{Spec}(\hat{\mathbf{S}})$ and that $\mathbf{S}$ belongs to the class $\mathcal{B}$ defined in the introductory paragraphs of Ch. I, where $\mathbf{S}$ is the local ring of $X$ at the point $x_0$, and $\hat{\mathbf{S}}$ is the completion of $\mathbf{S}$.) Since $\hat{\mathbf{J}}_s' = \mathbf{J}_s\hat{\mathbf{S}}_s'$, we can conclude that $\mathbf{J}_s'$ is contained in the $\nu^{th}$ power of the maximal ideal of $\mathbf{S}_s'$. That is to say: $\nu(J(s)_{x'}) \geq \nu$. q.e.d.

We are now ready to prove Theorems C and D\*. (As was remarked before, we may assume, as we shall do, that  $S_{\nu}(\mathfrak{R})$  does not have any non-empty component of codimension one in X.)

First of all, by localization theorems (Propositions 3 and 4 of §1, Ch. IV), we can find a permissible succession of monoidal transformations of $X = X_0$ for $\mathfrak{R}$, say

$$
h _ {s} = \{f _ {t}: X _ {t + 1} \rightarrow X _ {t} \}
$$

$$
(0 \leq t \leq s - 1)
$$

such that, notation being as above,

[(1)] $h_s(S_\nu(\Re(s)))$ consists of a finite number of points at which $X$ has dimension $N$, where $\nu = \nu(\Re) > 0$.

Moreover, for the case in which  $R = R_{II}^{N}$  without restriction, by applying Theorem  $II_{i}^{N}$  a finite number of times (in fact, at most  $\alpha$  times), we may assume that

[(2)] $E_{i}(s)\cap S_{\nu}(\Re (s))$ is empty for $1\leq i\leq \alpha$

Now, let $x_0$ be any point of $X$ which belongs to $h_s(S_{\nu}(\mathfrak{R}(s)))$. Clearly, $x_0$ belongs to $S_{\nu}(\mathfrak{R})$. With reference to the point $x_0$, we construct as above a succession of monoidal transformations

$$
\bar {h} _ {s} = \{\bar {f} _ {t}: \bar {X} _ {t + 1} \rightarrow \bar {X} _ {t} \}
$$

$$
(0 \leq t \leq s - 1)
$$

and coherent sheaves of ideals $\bar{J}(t)$ on $\bar{X}_t$ ($0 \leq t \leq s$). Let $\bar{c}_t: \bar{X}_t \to X_t$ be the morphism induced by $c_t: \hat{X}_t \to X_t$ for $0 \leq t \leq s$. We also define the positive integer $\bar{b}$ as above. (See [i], [ii], [iii], [iv] preceding Lemma (CD 3), and also [v], [vi] and [vii], preceding Lemma (CD. 4).)

Let $\tilde{X}$ denote the non-singular irreducible scheme $\bar{X}_s$ of dimension $N - 1$. Let us write

$$
\mathfrak {R} _ {\mathrm{II}} ^ {N} (s) = \left( \begin{array}{c c} E _ {1} (s), & \dots , E _ {\alpha + s} (s) \\ a _ {1}, & \dots , a _ {\alpha + s} \end{array} \right| J (s), b)
$$

as above. Let $\hat{E}_{j}(s) = c_{s}^{-1}\big(E_{j}(s)\big)$ for $1 \leq j \leq \alpha + s$. For the case in which $\Re = (\Re_{\mathrm{II}}^{N}, F)$, we see that $\hat{E}_{1}(s) \cup \dots \cup \hat{E}_{\alpha + s}(s)$ has only normal crossings with $\tilde{X}$ in $\hat{X}_{s}$. In the other case, we see that $\hat{E}_{\alpha + 1}(s) \cup \dots \cup \hat{E}_{\alpha + s}(s)$ has only normal crossings with $\tilde{X}$ in $\hat{X}_{s}$. We define in each case an integer $\tilde{\alpha}$ and non-singular irreducible subschemes $\tilde{E}_{j}$ ($1 \leq j \leq \tilde{\alpha}$) of $\tilde{X}$ as follows:

(i) If $\Re = (\Re_{\mathrm{II}}^N, F)$, then $\tilde{\alpha} = \alpha + s$ and $\tilde{E}_j = \hat{E}_j(s) \cap \tilde{X}$ for $1 \leq j \leq \tilde{\alpha}$.

(ii) If $\Re = \Re_{\mathrm{II}}^N$, then $\tilde{\alpha} = s$ and $\tilde{E}_j = \hat{E}_{\alpha + j}(s) \cap \tilde{X}$ for $1 \leq j \leq \tilde{\alpha}$.

We see that, in both cases,  $\tilde{E}_{j}$  ( $1 \leq j \leq \tilde{\alpha}$ ) are non-singular irreducible subschemes of  $\tilde{X}$  of codimension 1, and  $\tilde{E}_{1} \cup \cdots \cup \tilde{E}_{\tilde{\alpha}}$  has only normal crossings on  $\tilde{X}$ .

The proof of Theorems C and  $D^{*}$  will be divided into two cases, the one in which  $\nu \geq b$ , and the other in which  $\nu < b$ .

The case $\nu \geq b$. On the non-singular irreducible algebraic scheme $\tilde{X} = \bar{X}_s$, we have defined a coherent sheaf of ideals $\bar{J}(s)$. We have also defined a positive integer $\bar{b}$. We shall consider a resolution datum $\mathfrak{R}_{\mathrm{II}}^{N-1}$ on $\tilde{X}$ defined as follows:

$$
\mathfrak {R} _ {1 1} ^ {N - 1} = \left( \right.\begin{array}{c c c}\widetilde {E} _ {1},&\dots ,&\widetilde {E} _ {\widetilde {\alpha}}\\\widetilde {a} _ {1},&\dots ,&\widetilde {a} _ {\widetilde {\alpha}}\end{array}\left. \right| \widetilde {J}, \widetilde {b}\left. \right),
$$

where

(i) $\widetilde{b} = \overline{b} >0$

(ii) $\tilde{a}_j$ ($1 \leq j \leq \tilde{\alpha}$) are non-negative integers such that, if $\tilde{P}_j$ denotes the coherent sheaf of ideals of the subscheme $\tilde{E}_j$ of $\tilde{X}$ for $1 \leq j \leq \tilde{\alpha}$, then

$$
\bar {J} (s) = \tilde {J} \cdot \prod_ {j = 1} ^ {\tilde {\alpha}} (\tilde {P} _ {j} ^ {a _ {j}})
$$

(iii) $\tilde{J}$ is a coherent sheaf of ideals on $\tilde{X}$, subject to the above equality.

(iii) $J$ is a coherent sheaf of ideals on $X$, subject to the above equality. The above resolution datum $\mathfrak{R}_{\mathrm{II}}^{N-1}$ is not uniquely determined but will be abitrarily fixed. We can take, for example, $\tilde{J}$ to be $\bar{J}(s)$ and $\tilde{\alpha}_j = 0$ for all $j(1 \leq j \leq \tilde{\alpha})$.

REMARK 1. Let $\tilde{B}$ be a non-singular irreducible subscheme of $\tilde{X}$ such

that the monoidal transformation $\tilde{f}$ of $\tilde{X}$ with center $\tilde{B}$ is permissible for the resolution datum $\mathfrak{R}_{\mathrm{II}}^{N-1}$. Then there exists a non-singular irreducible subscheme $B$ of $X_s$ such that $c_s: \hat{X}_s \to X_s$ induces an isomorphism of $\tilde{B} \to B$, and the monoidal transformation $f_s$ of $X_s$ with center $B$ is permissible for the resolution datum $\mathfrak{R}(s)$.

PROOF. Since $\tilde{f}$ is permissible for $\mathfrak{R}_{\mathrm{II}}^{N-1}$, $\nu(\bar{J}(s)_{\hat{x}^{\prime}})\geq\bar{b}$ for all points $\hat{x}^{\prime}\in\tilde{B}$. Hence, by Lemma (CD. 5), $\nu(J(s)_{x^{\prime}})\geq\nu$ for all $x^{\prime}\in c_{s}(\tilde{B})$. Since $\nu\geq b$, $S_{\nu}(\mathfrak{R}_{\mathrm{II}}^{N}(s))=\{x\in X_{s}\mid\nu(J(s)_{x})\geq\nu\}$. Therefore, we get $c_{s}(\tilde{B})\subseteq S_{\nu}(\mathfrak{R}_{\mathrm{II}}^{N}(s))$. This shows, by the assumption [(1)], that $h_{s}(c_{s}(\tilde{B}))=x_{0}$, or equivalently, $\hat{h}_{s}(\tilde{B})=\hat{x}_{0}$. By Lemma (CD. 3), $B=c_{s}(\tilde{B})$ is an irreducible subscheme of $X_{s}$ and $c_{s}$ induces an isomorphism $\tilde{B}\to B$. Since $B\subseteq S_{\nu}(\mathfrak{R}_{\mathrm{II}}^{N}(s))=S_{*}(\mathfrak{R}_{\mathrm{II}}^{N}(s))$ and, for the case in which $\Re=(\mathfrak{R}_{\mathrm{II}}^{N},F)$, $B\subseteq F(s)$ (= the closure of $c_{s}(\tilde{X})$) in $X_{s}$, we have only to prove that $E_{1}(s)\cup\cdots\cup E_{\alpha+s}(s)$ has only normal crossings with $B$. For the case in which $\Re=(\mathfrak{R}_{\mathrm{II}}^{N},F)$, this is clear from the fact that $\tilde{E}_{1}\cup\cdots\cup\tilde{E}_{\tilde{\alpha}}$ has only normal crossings with $\tilde{B}$. For the case in which $\Re=\mathfrak{R}_{\mathrm{II}}^{N}$, we remark that, by the assumption [(2)], $E_{i}(s)\cap B$ is empty for $1\leqq i\leqq\alpha$. Hence we have only to show that $E_{\alpha+1}(s)\cup\cdots\cup E_{\alpha+s}(s)$ has only normal crossings with $B$. This is, however clear from the fact that $\tilde{E}_{1}\cup\cdots\cup\tilde{E}_{\tilde{\alpha}}$ has only normal crossings with $\tilde{B}$. q.e.d.

Now, $\tilde{B}$ and $B$ being as in Remark 1, we extend the permissible succession $h_s$ to include the monoidal transformation $f_s: X_{s+1} \to X_s$ with center $B$ and we replace $\bar{X}_s$ by the proper transform $\bar{X}_{s+1}$ of $\bar{X}_s$ in $\hat{X}_{s+1}$, so that $\hat{f}_s: \hat{X}_{s+1} \to \hat{X}_s$ is the monoidal transformation with center $\tilde{B} = c_s^{-1}(B)$. Then $\hat{f}_s$ induces the monoidal transformation $\bar{f}_s: \bar{X}_{s+1} \to \bar{X}_s$ with the non-singular irreducible center $\tilde{B}$. We can easily see that the relation between $\Re(s+1) = f_s^*(\Re(s))$ and $\bar{f}_s^*(\Re_{\Pi}^{N-1})$ is the same as that between $\Re(s)$ and $\Re_{\Pi}^{N-1}$. Thus the proof of Theorems C and D\* can be reduced to the resolution of the datum $\Re_{\Pi}^{N-1}$ on $\tilde{X}$, defined as above, which can be done by Theorem II\$\_2^{N-1}\$. (By Corollary of Lemma (CD. 4), if $\Re_{\Pi}^{N-1}$ is resolved then $S(\Re(s)) \cap h_s^{-1}(x_0)$ is empty.)

The case: $\nu < b$. ($\nu = \nu(\Re) > 0$). Let $\bar{J}(s)$ and $\bar{b}$ be as before. In this case we first define a coherent sheaf of ideals $\bar{J}^{*}(s)$ on $\bar{X}_{s}$ as follows:

$$
\bar {J} ^ {*} (s) = \left(\bar {J} (s) ^ {b - \nu}, \left(\prod_ {j = 1} ^ {\tilde {\alpha}} \tilde {P} _ {j} ^ {c _ {j}}\right) ^ {b}\right)
$$

which denotes the coherent sheaf of ideals on $\bar{X}_s$ generated by the $(b - \nu)^{\mathrm{th}}$ power of $\bar{J}(s)$ and by the $\bar{b}^{\mathrm{th}}$ power of the product $\prod_{j=1}^{\tilde{\alpha}}\tilde{P}_{ij}^{c_j}$ (in the sheaf of local rings of $\bar{X}_s$), where $\tilde{P}_j =$ the sheaf of ideals of the subscheme $\tilde{E}_j$ of $\tilde{X}$ ($1 \leq j \leq \tilde{\alpha}$) and

$c_{j} = \begin{cases} a_{j} & \text{for the case of } \Re = (\Re_{\mathrm{II}}^{N}, F) \\ a_{\alpha + j} & \text{for the case of } \Re = \Re_{\mathrm{II}}^{N} (\text{without restriction}) (1 \leq j \leq \tilde{\alpha}) . \end{cases}$

We shall consider a resolution datum $\mathfrak{R}_{\mathrm{II}}^{N - 1}$ without restriction on $\tilde{X}$ defined as follows:

$$
\mathfrak {R} _ {\mathrm{II}} ^ {N - 1} = \left( \right.\begin{array}{c c c}\widetilde {E} _ {1},&\dots ,&\widetilde {E} _ {\widetilde {\alpha}}\\\widetilde {a} _ {1},&\dots ,&\widetilde {a} _ {\widetilde {\alpha}}\end{array}\left. \right| \widetilde {J},   \widetilde {b}\left. \right)
$$

where

(i) $\tilde{b} = \bar{b} (b - \nu),$

(ii) $\tilde{a}_j$ ($1 \leq j \leq \tilde{\alpha}$) are non-negative integers, and

(iii) $\tilde{J}$ is a coherent sheaf of ideals on $\tilde{X}$ such that the following equality holds:

$$
\bar {J} ^ {*} (s) = \tilde {J} \cdot \prod_ {j = 1} ^ {\tilde {\alpha}} (\tilde {P} _ {j} ^ {\tilde {a} _ {j}}).
$$

Such a resolution datum $\mathfrak{R}_{\mathrm{II}}^{N-1}$ on $\tilde{X}$ is not uniquely determined except the last product equal to $\bar{J}^{*}(s)$. In the sequel we fix an arbitrary $\mathfrak{R}_{\mathrm{II}}^{N-1}$ on $\tilde{X}$ which is subject to the conditions. We can take, for example, $\tilde{a}_{j}=0$ for all $j$ ($1 \leq j \leq \tilde{\alpha}$) and $\tilde{J} = \bar{J}^{*}(s)$.

REMARK 2. We have $S(\mathfrak{R}_{\mathrm{II}}^{N - 1}) = \{x \in \tilde{X} | \nu(\bar{J}^*(s)_x) \geq \tilde{b}\}$. (This is clear from Definitions of Ch. I.) The morphism $c_s: \hat{X}_s \to X_s$ induces a bijection $S(\mathfrak{R}_{\mathrm{II}}^{N - 1}) \to S_v(\mathfrak{R}(s)) \cap h_s^{-1}(x_0)$. Moreover, if $\tilde{B}$ is any non-singular irreducible subscheme of $\tilde{X}$ such that the monoidal transformation

$$
\widetilde {f} \colon \widetilde {X} ^ {\prime} \to \widetilde {X}
$$

with center $\tilde{B}$ is permissible for $\Re_{\mathrm{II}}^{N-1}$, then there exists a unique nonsingular irreducible subscheme $B_s$ of $X_s$ such that $\tilde{B} = c_s^{-1}(B_s)$, that $c_s$ induces an isomorphism $\tilde{B} \to B_s$ and that the monoidal transformation

$$
f _ {s} \colon X _ {s + 1} \rightarrow X _ {s}
$$

with center $B_{s}$ is permissible for $\Re(s)$.

PROOF. Let $\hat{x}$ be any point of $\widetilde{X}$. We have that $\hat{x} \in S(\mathfrak{R}_{\Pi}^{N-1})$ if and only if the following conditions are satisfied:

(a) $\nu (\bar{J} (s)_{\hat{x}})\geq \bar{b},$ and

(b) $\sum_{\hat{x} \in \widetilde{E}_1} c_j \geq b - \nu$.

This is clear from the definition of $\bar{J}^{*}(s)$ and the fact that all the $\tilde{E}_{j}$ are non-singular. Now, let us assume that the conditions (a) and (b) are satisfied for a point $\hat{x}$ of $\bar{X}_{s} = \tilde{X}$. Let $x = c_{s}(\hat{x})$. By Lemma (CD. 5), (a) implies that $\nu(J(x)_{x}) \geq \nu$. Moreover, (b) implies that

$$
\sum_ {x \in E _ {j} (s)} a _ {j} \geq b - \nu .
$$

Therefore we conclude that $x \in S_{\nu}(\mathfrak{R}_{\mathrm{II}}^{N}(s))$. If $\Re = (\Re_{\mathrm{II}}^{N}, F)$, $S_{\nu}(\Re(s)) = S_{\nu}(\Re_{\mathrm{II}}^{N}(s)) \cap F(s)$ where $F(s) =$ the closure of $c_s(\tilde{X})$ in $X_s$. We get that $x \in S_{\nu}(\Re(s))$ in both cases, so that the assumption [(1)] on $h_s$ shows that

$x \in S_{\nu}(\Re(s)) \cap h_{s}^{-1}(x_{0})$. Conversely let us take any point $x \in S_{\nu}(\Re(s)) \cap h_{s}^{-1}(x_{0})$. By Lemma (CD. 3), we have a unique point $\hat{x}$ of $\hat{X}_{s}$ such that $c_{s}(\hat{x}) = x$. By Corollary of Lemma (CD. 4), $\hat{x}$ is a point of $\tilde{X} = \bar{X}_{s}$ and the condition (a) is satisfied. Since $\nu = \nu(\Re) \geq \nu(\Re(s)), x \in S_{\nu}(\Re(s))$ implies $\nu(J(s)_{x}) = \nu$. Hence $x \in S_{\nu}(\Re(s))$ implies also that

$$
\nu + \sum_ {x \in E _ {j} (s)} a _ {j} \geq b, \quad \text { i.e., } \sum_ {x \in E _ {j} (s)} a _ {j} \geq b - \nu .
$$

Then (b) follows immediately if $\Re = (\Re_{\mathrm{II}}^N, F)$. If $\Re = \Re_{\mathrm{II}}^N$, we need to use the assumption [(2)] on $h_s$ which says that $x \notin E_j(s)$ for any $j$ with $1 \leq j \leq \alpha$. Again (b) follows. Thus we get $x \in S(\Re_{\mathrm{II}}^{N-1})$. We want to prove the last assertion of Remark 2. By the above result, $c_s(\tilde{B}) \subseteq S_v(\Re(s)) \cap h_s^{-1}(x_0)$. By Lemma (CD. 3), we get $B_s$ such that $\tilde{B} = c_s^{-1}(B_s)$, and $c_s$ induces an isomorphism $\tilde{B} \to B_s$. Since $B_s = c_s(\tilde{B}) \subseteq S_v(\Re(s))$, it suffices to show that $E_1(s) \cup \cdots \cup E_{\alpha+s}(s)$ has only normal crossings with $B_s$. This follows from the assumption that $\tilde{E}_1 \cup \cdots \cup \tilde{E}_{\alpha}$ has only normal crossings with $\tilde{B}$. In fact, it is obvious if $\Re = (\Re_{\mathrm{II}}^N, F)$, and if $\Re = \Re_{\mathrm{II}}^N$ we recall the assumption [(2)] on $h_s$, which say that $E_j(s) \cap B_s$ is empty for all $j$ with $1 \leq j \leq \alpha$. q.e.d.

Let $\tilde{B}$ and $B_{s}$ be as in Remark 2. Let $\tilde{f}:\tilde{X}'\to \tilde{X}$ be the monoidal transformation with center $\tilde{B}$, which is permissible for the resolution datum $\mathfrak{R}_{\mathrm{II}}^{N - 1}$, and $f_{s}\colon X_{s + 1}\to X_{s}$ the one with center $B_{s}$, which is permissible for the resolution datum $\Re (s)$. We put $\Re (s + 1) = f_s^* (\Re (s))$ with

$$
\Re_ {\mathrm{II}} ^ {N} (s + 1) = f _ {s} ^ {*} \left(\Re_ {\mathrm{II}} ^ {N} (s)\right) = \left( \begin{array}{c c} E _ {1} (s + 1), & \dots , E _ {\alpha + s + 1} (s + 1) \\ a _ {1}, & \dots , a _ {\alpha + s + 1} \end{array} \right| J (s + 1), b)
$$

where $E_{\alpha + s + 1}(s + 1)$ denotes the total transform of $B_s$ in $X_{s + 1}$. We put also $\bar{X}_{s + 1} =$ the strict transform of $\bar{X}_s$ in $\hat{X}_{s + 1}$, and $\bar{J}(s + 1) =$ the coherent sheaf of ideals on $\bar{X}_{s + 1}$ defined by

$$
\bar {J} (s + 1) = \bar {f} _ {s} ^ {- 1} (\bar {J} (s)) / (\bar {P} _ {s + 1}) ^ {\bar {b}}
$$

where $\bar{f}_s$ denotes the monoidal transformation $\bar{X}_{s+1} \to \bar{X}_s$ with center $\tilde{B}$, which is induced by the monoidal transformation $\hat{f}_s: \hat{X}_{s+1} \to \hat{X}_s$, and $\bar{P}_{s+1}$ denotes the sheaf of ideals of the subscheme $c_s^{-1}(E_{\alpha+s+1}(s+1)) \cap \bar{X}_{s+1}$ of $\bar{X}_{s+1}$ (i.e., the total transform of $\tilde{B}$ in $\bar{X}_{s+1}$). We may set $\tilde{X}' = \bar{X}_{s+1}$ and $\tilde{f} = \bar{f}_s$. Now, let us define non-singular irreducible subschemes $\tilde{E}_j'$ ($1 \leq j \leq \tilde{\alpha} + 1$) for the extension $h_{s+1} (= f_s \circ h_s)$ of $h_s$ in the same way as we did $\tilde{E}_j$ ($1 \leq j \leq \tilde{\alpha}$) for $h_s$. Namely,

(i') If $\Re = (\Re_{\mathrm{II}}^N, F)$, $\tilde{E}_j' = \hat{E}_j(s + 1) \cap \tilde{X}'$ for $1 \leq j \leq \tilde{\alpha} + 1 = \alpha + s + 1$, where $\hat{E}_j(s + 1) = c_{s+1}^{-1}(E_j(s + 1))$.

(ii') If $\Re = (\Re_{\Pi}^N)$, $\tilde{E}_j' = \hat{E}_{\alpha + j}(s + 1) \cap \tilde{X}'$ for $1 \leq j \leq \tilde{\alpha} + 1 = s + 1$. Let us define

$$
c _ {j} ^ {\prime} = \left\{ \begin{array}{l l} a _ {j} & \text { for   the   case   of } \Re = (\Re_ {\mathrm{II}} ^ {N}, F) \\ a _ {\alpha + j} & \text { for   the   case   of } \Re = \Re_ {\mathrm{II}} ^ {N} (\text { without   restriction }) (1 \leq j \leq \tilde {\alpha} + 1). \end{array} \right.
$$

Let $\tilde{P}_j' =$ the sheaf of ideals of the subscheme $\tilde{E}_j'$ of $\tilde{X}' (= \bar{X}_{s+1})$. (Note that $\tilde{P}_j'$ is equal to the sheaf of local rings of $\tilde{X}'$ if $\tilde{E}_j'$ is empty.) We define $\bar{J}^*(s + 1)$ as we did $\bar{J}^*(s)$; namely,

$$
\bar {J} ^ {*} (s + 1) = \left(\bar {J} (s + 1) ^ {b - \nu}, \left(\prod_ {j = 1} ^ {\tilde {\alpha} + 1} (\tilde {P} _ {j} ^ {\prime}) ^ {c _ {j} ^ {\prime}}\right) ^ {\bar {b}}\right).
$$

REMARK 3. Notation and the assumptions being as above, $\widetilde{f}^{*}(\mathfrak{R}_{\mathrm{II}}^{N-1})$ on $\widetilde{X}'$ can be written in the form

$$
\left( \begin{array}{c c} \widetilde {E} _ {1} ^ {\prime}, & \dots ,   \widetilde {E} _ {\widetilde {\alpha} + 1} ^ {\prime} \\ \widetilde {a} _ {1}, & \dots ,   \widetilde {a} _ {\widetilde {\alpha} + 1} \end{array} \bigg |   \widetilde {J} ^ {\prime},   \widetilde {b}\right)
$$

where $\bar{J}^{*}(s + 1) = \tilde{J}^{\prime}\cdot \prod_{j = 1}^{\alpha +1}(\tilde{P}_{j}^{f\alpha_{j}})$. In other words, the relation between $\Re (s + 1)(= f_s^*(\Re (s)))$ and $\tilde{f}^{*}(\mathfrak{R}_{\mathrm{II}}^{N - 1})$ is the same as that between $\Re (s)$ and $\mathfrak{R}_{\mathrm{II}}^{N - 1}$.

PROOF. It follows from the definition of $\widetilde{f}^{*}(\mathfrak{R}_{\mathrm{II}}^{N - 1})$ that

$$
\widetilde {J} ^ {\prime} \cdot \prod_ {j = 1} ^ {\widetilde {\alpha} + 1} (\widetilde {P} _ {j} ^ {\prime \widetilde {a} _ {j}}) = \widetilde {f} ^ {- 1} \left(\widetilde {J} \cdot \prod_ {j = 1} ^ {\widetilde {\alpha}} (\widetilde {P} _ {j} ^ {\widetilde {a} _ {j}})\right) \widetilde {P} _ {\widetilde {\alpha} + 1} ^ {\prime - b}
$$

which is equal to $\widetilde{f}^{-1}(\overline{J}^{*}(s))\widetilde{P}_{\widetilde{\alpha} + 1}^{\prime -\widetilde{b}}$. Therefore, the assertion of Remark 3 is equivalent to saying that

$$
\bar {J} ^ {*} (s + 1) = \tilde {f} ^ {- 1} (\bar {J} ^ {*} (s)) \tilde {P} _ {\dot {\alpha} + 1} ^ {\prime - \tilde {b}}.
$$

Let us recall that $\tilde{b} = \bar{b} (b - \nu)$ and that

$$
\bar {J} ^ {*} (s + 1) = \left(\bar {J} (s + 1) ^ {b - \nu}, \left(\prod_ {j = 1} ^ {\tilde {\alpha} + 1} (\tilde {P} _ {j} ^ {\prime}) ^ {c _ {j} ^ {\prime}}\right) ^ {\bar {b}}\right)
$$

and

$$
\bar {J} ^ {*} (s) = \left(\bar {J} (s) ^ {b - \nu}, \left(\prod_ {j = 1} ^ {\tilde {\alpha}} (\tilde {P} _ {j}) ^ {c _ {j}}\right) ^ {\bar {b}}\right).
$$

By the definition of $\bar{J} (s + 1)$, we have

$$
\bar {J} (s + 1) = \widetilde {f} ^ {- 1} (\bar {J} (s)) \widetilde {P} _ {\widetilde {\alpha} + 1} ^ {\prime - \bar {b}}.
$$

Therefore, it is sufficient to prove that

$$
\prod_ {j = 1} ^ {\tilde {\alpha} + 1} \left(\tilde {P} _ {j} ^ {\prime}\right) ^ {c _ {j} ^ {\prime}} = \tilde {f} ^ {- 1} \left(\prod_ {j = 1} ^ {\tilde {\alpha}} \left(\tilde {P} _ {j}\right) ^ {c _ {j}}\right) \tilde {P} _ {\tilde {\alpha} + 1} ^ {\prime - (b - \nu)}.
$$

As is easily seen, the right hand side is equal to

$$
\left(\prod_ {j = 1} ^ {\widetilde {\alpha}} \left(\widetilde {P} _ {j} ^ {\prime}\right) ^ {c _ {j}}\right) \widetilde {P} _ {\widetilde {\alpha} + 1} ^ {\prime e - (b - \nu)},
$$

where

$$
e = \sum_ {\widetilde {B} \subseteq \widetilde {E} _ {j}} c _ {j}.
$$

By definition, we have $c_j' = c_j$ for $1 \leq j \leq \tilde{\alpha}$. Therefore, all that we

need to prove is the equality: $c_{\widetilde{\alpha} + 1}' = e - (b - \nu)$. Let us write, as before,

$$
\mathfrak {R} _ {\mathrm{II}} ^ {N} (s) = \left( \begin{array}{c c} E _ {1} (s), & \dots , E _ {\alpha + s} (s) \\ a _ {1}, & \dots , a _ {\alpha + s} \end{array} \right| J (s), b)
$$

and

$$
\Re_ {1 1} ^ {N} (s + 1) = \left( \begin{array}{c c} E _ {1} (s + 1), & \dots , E _ {\alpha + s + 1} (s + 1) \\ a _ {1}, & \dots , a _ {\alpha + s + 1} \end{array} \right| J (s + 1), b).
$$

Then we have $c_{\widetilde{\alpha} + 1}' = a_{\alpha + s + 1}$, which is equal to

$$
\left(\sum_ {B _ {s} \subseteq E _ {j ^ {(s)}}} a _ {j}\right) + \nu - b.
$$

Thus we have only to prove

$$
\sum_ {B _ {s} \subseteq E _ {j ^ {(s)}}} a _ {j} = \sum_ {\widetilde {B} \subseteq \widetilde {E}} c _ {j}.
$$

In view of the definition of $c_j$ and $\tilde{E}_j$, this equality is clear for the case in which $\Re = (\mathfrak{R}_{\mathrm{II}}^N, F)$, and moreover it follows for the other case if we can show that $B_s \not\subseteq E_j(s)$ for any $j$ with $1 \leq j \leq \alpha$. This is, however, a consequence of the assumption [(2)], as was already seen in the proof of Remark 2. q.e.d.

In view of Remarks 2 and 3, the proof of Theorems C and D\* can be easily reduced to the resolution of the $\mathfrak{R}_{\Pi}^{N-1}$ on $\widetilde{X}$, defined as above, which can be done by Theorem II$_2^{N-1}$.

We have now completed the proof of Theorems C and D, and combining this with the result of the preceding section we have established an inductive proof of the fundamental theorems which were announced in § 2, Ch. I.

BRANDEIS UNIVERSITY AND INSTITUTE FOR ADVANCED STUDY