Homological Algebra 18.715 D.G. Quillen.
Algebraic H-Theory

(Notes by Howard Hiller)

$K_{0}A = \text{Grothendieck group of fin. gen. projective A-modules}$$K_{1}A = GL_{\infty}(A) / [GL_{\infty}(A), GL_{\infty}(A)]$

Look for higher K-fundors  $K_{n}A, n \in Z$ .

$K_{n}A = \pi_{n}(FA)$  FA = some space associated with A.
so part of homotopy theory, so algebraic topology.

Acyclic spaces and maps:

Let $X$ be a space. $X$ is called acyclic if $\widetilde{H}_{*}(X)=0$. (integral homology). aspherical if $\pi_{*}(X,x_{0})=0$.

If X has homotopy type of CW complex  $\Rightarrow$  X \~ \* by Whitehead's Theorem.

Assumption: All spaces have homotopy type of CW-complex, with basepoint, connected.

Poincaré:  $H_{1}(X) = \pi_{1}(X)/[\pi_{1}(X), \pi_{1}(X)]$ .

Def: A group G is perfect if G = [G, G] G → A (belian) is trivial.

X cyclic  $\Rightarrow \pi_{1}(X)$  is perfect (by Poincaré).

X acyclic and simply connected  $\Rightarrow$  X\~\* (by Whitehead.

All simple non-abelian groups are perfect; e.g. $A_n$ n > 5.

Question: Does ∃ a finite acyclic polyhedron?

Let $f: X \to Y$ be a map. TFAE:

(i) The homotopy fibre of $f$ is acyclic.
(Replace $f: X \to Y$ by a Some fibration, and all fibers have same homotopy type).

$X \leftarrow_{f}^{p_1} X_x Y^I = \{(x, \lambda): f(x) = \lambda(0)\}$$Y \leftarrow_{\overline{\lambda}} Y^I$

homotopy-fibre of $f = X_{Y}^{x} Y^{I}_{X}$ for y.3

(iii) For any local coefficient system of abelian groups L on Y

$$
f _ {*} \colon H _ {g} (X, f ^ {*} L) \xrightarrow {\approx} H _ {g} (Y, L)
$$

(ili) Let  $\tilde{Y} = universal cover of Y$ . Then:

$\sim$$\sim$

$$
(p _ {2}) _ {*}: H _ {*} (X \times \widetilde {Y}) \xrightarrow {\approx} H _ {*} (\widetilde {Y})
$$

Proof: Assume $f: X \to Y$ is fibration and put $F = f^{-1}(y, z)$.  
(ii) $\Rightarrow$ (ii) Assume $F$ is a cyclic.

Consider Serre spectral sequence:

③

$F \rightarrow X^{2}$$\downarrow$ 
Y

$$
E _ {i, g} ^ {2} = H _ {g} (Y, H _ {g} (F, i ^ {*} L ^ {\prime})) \Rightarrow H _ {p + g} (X, L ^ {\prime})
$$

universal coefficient theorem:

$H_g(F,A) \cong H_g(F) \otimes A \oplus \text{Tor}_1(H_{g-1}(F,A)) = 0, F \geq \text{cyclic.}$

Take $L' = f^*L$. Then $i^*L' \to \text{constant}$.

Thus $H_{q}(F, i^{*}L') = \begin{cases} L & q=0 \\ 0 & q>0 \end{cases}$

So spectral sequence degenerates,  $E_{p,0}^{2} \xleftarrow{\approx} H_{p}$ , yielding (ii).

(\*)

$$
\begin{array}{c} X _ {Y} \stackrel {{\sim}} {{\longrightarrow}} \stackrel {{p r _ {2}}} {{\longrightarrow}} \stackrel {{\sim}} {{\longrightarrow}} \\ p r _ {1} \downarrow \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array}
$$

vertical maps
are covering spaces.

$$
\begin{array}{r l} {\pi = \pi_ {1} Y} & {H _ {g} (X _ {y} ^ {-} \widetilde {Y}) \xrightarrow {(P _ {2}) _ {p}} H _ {g} (\widetilde {Y})} \\ & {(P _ {1}) _ {p} \downarrow 2 2} \end{array}
$$

canonical isomorphism
from Serre spectral sequence
for p.

$$
H _ {i} (X, Z [ \pi ]) \xrightarrow [ f _ {*} ]{} H _ {i} (Y, Z [ \pi ]).
$$

(ii)  $\Rightarrow$$f_{x}$  is isomorphism, so  $(p_{2})_{x}$  is.

$X_{X}(X^{\prime} \tilde{Y}) \rightarrow X^{\prime} \tilde{Y} \rightarrow \tilde{Y}$$\downarrow$$X \xrightarrow{\sim} X^{\prime} \rightarrow Y$

look at homotopy
exact sequence.

So assume $f: X \to Y$ is fibration. But then $\beta r_2$ has some fiber as $f$ by pull-back square (\*). Call it $f$.

Replace $f: X \to Y$ by $pr_2: X_x \widetilde{Y} \to \widetilde{Y}$. In which case we are trying to show if $f_*: H_*(X) \xrightarrow{\gamma} H_*(Y)$ and $Y$ simply connects $\Rightarrow F$ acyclic. This is a special case of (ii) $\to (i)$.

(ii)  $\Rightarrow (i)$$\Omega Y \longrightarrow PY_{Y} \times X \longrightarrow X$$\parallel$$\downarrow$$\Omega Y \longrightarrow PY \longrightarrow Y$

Claim: ${PY}_{Y} \times  X = F$ ,i.e. homotopy fibre of $f$ .

Show this is acyclic; Look at spectral sequence.

$E_{p,q}^{2}=H_{p}(X,H_{q}(\Omega Y))\Rightarrow H_{p+q}(PY_{x}X).$

$E_{p,q}^{2}=H_{p}(Y,H_{q}(RY))\Rightarrow H_{p+q}(PY)=0.$

F is acyclic if it satisfies conditions of Proposition.

Ex. $X \rightarrow  *$ is acyclic $\Leftrightarrow  X$ is acyclic.
trivially fibration.

(General Grothendieck method of extending properties of obj to maps)

Remarks:

(1)  $X \xrightarrow{f} Y \xrightarrow{g} Z$$f, g \text{ acyclic} \rightarrow g \cdot f \text{ acyclic.}$$f, g \cdot f \text{ acyclic} \Rightarrow g \text{ acyclic.}$

$Y' \times X \xrightarrow{g'} X$$Y' \downarrow$$Y' \xrightarrow{g} Y$

pullbect square, f,g are fibrations. then f acyclic ⇒ f' acyclic.

$X \xrightarrow{f} Y$ Assume $f, g$ are cofibrations.  
$g \downarrow \quad \downarrow g'$ then $f$ acyclic $\Rightarrow f'$ acyclic.  
$Z \xrightarrow{f'} Z \frac{U(Y)}{X} L$

Pf: Assume g cofibration.

$H(X; f(y)) \xrightarrow{f_{0}} H(Y; f^{l})$

$H(z_{i}f_{i})$$\xrightarrow{p_{x}^{\prime}}$$H(z_{11}Y;L)$

$H(Z,X; f^{\prime}L) \xrightarrow{f^{\prime}*} H(Z_{\parallel}Y; Y; L)$

$f_{x}$  iso  $\stackrel{S\ Lemma}{\Longrightarrow}$$f'_{x}$  is iso.
Local coefficient Whitehead Theorem;
④  $f: X \rightarrow Y$  is acyclic,  $\pi, f: \pi, X \stackrel{\alpha}{\rightarrow} \pi, Y$ , then f is h. eg.

Proof: Hypotheses →  $X_{\tilde{Y}}$$\tilde{Y}$  = universal cover of  $X = \tilde{X}$ 
and that  $\tilde{X} \rightarrow \tilde{Y}$  induces isomorphisms of  $H_{x}$ .
So by simply connected Whitebead Theorem:  $\tilde{X} \rightarrow \tilde{Y}$  h. eq.

Ex: Suppose X is closed n-manifold, homology n-sphere, n≥2
⇒ orientable.  $H_{n}(X)$  has fundamental class μ

$H_{n}(X) \rightarrow H_{n}(S^{n})$ maps to canonical genera

f is a cyclic map, L is constant since  $S^{n}$  is simply-connected

Poincaré' homology 3-sphere: $X = SO(3) / \text{icosahedral}_1 = S^3 / \begin{array}{c} \text{binary} \\ \text{icosahedral}_1 \\ \text{group} \end{array}$

This is a homology 3-sphere. 3-manifold with no  $H_{1}$ , so no  $H_{2}$  by Poincaré duality, and orientable.

Classification of acyclic with fixed source X.

Theorem: (i) If $f: X \to Y$ and $f': X \to Y'$ are acyclic and $\ker(\pi, (f)) = \ker(\pi, (f'))$, then $\exists$ homotopy equivalence $g: Y \to Y'$ s.t. $g \cdot f \simeq f'$

![](images/page_5_image_4.jpg)

homotopy commutes.

(ii) Given a perfect normal subgroup N of  $\pi_{1}X$ ,  $\exists$  on 24c map f;  $X \to Y$  with  $\ker(\pi_{1}(f)) = N$ .

Remark s: $f: X \to Y$ cyclic $\rightarrow$$\pi, f: \pi, X \to \pi, Y$ is onto and
ker ($\pi, (f)$) is perfect, ? $\pi, F \to \pi, X \to \pi, Y \to \pi. F$

stronger form of (i):

Proposition: Given mops:

$x \xrightarrow{f} y$

with f. acyclic.

If $\ker(\pi_{1}(f)) \subseteq \ker(\pi_{1}(g))$. Then $\exists h: Y \to Z$ st. $h \circ f \sim g$ and any two such are homotopic.

Note: Proposition $\Rightarrow$ (i) by abstract nonsense; $f$ is initial object in crops over $\mathbb{Z}$.

$X \xrightarrow{f} Y$$g \downarrow$$Z \xrightarrow{f'} Z \frac{1}{x} Y$

Van Hampen Theorem: $\pi_{1}\left(Z\frac{11}{x}Y\right)=\pi_{1}\left(Z\right)\times\pi_{1}(Y)$$= \pi_{1}(Z)$ by hypothesis on kernels.

$f'$ is acyclic and $\pi_1(f')$ is isomorphism

By Remark 5, $f'$ is homotopy equivalence.

Any $h$ is obtained from retraction of $f'$, homotopy inverses are unique, so obtain uniqueness.

classifying acyclic maps $X \rightarrow Y$, $X$ fixed

Proof of (ii): Case  $N=\pi_{1}X$ . Choose maps  $f_{i}:S^{\prime}\rightarrow X$ ,  $i\in I$  st.
 $[f_{i}]$  generate  $\pi_{1}X$ .

$\bigvee_{i\in I}S'\xrightarrow{Vf_i}X\longrightarrow X' = \text{mapping cone of } Vf_i.$

where.  $X' = \bigcup_{i \in I} X \cup f_i e^2 = X \cup (f_i) V e^2$

Van Hampen Theorem $\Rightarrow$. $\pi, X' = 0$. For homology, have long exact mapping cone sequence.

$0 \rightarrow H_{3}X \rightarrow H_{3}X' \rightarrow 0 \rightarrow H_{2}X \rightarrow H_{2}X'$$\underset{\partial}{\longrightarrow} \bigoplus_{i \in I} Z \rightarrow H_{1}X.$

$$
H _ {q} X \simeq H _ {q} X ^ {\prime} \quad q > 3.
$$

By Hurewice theorem: $\pi_{2}X^{\prime}\xrightarrow{\approx}H_{2}X^{\prime}$, since $\pi_{1}X^{\prime}=0$.

Let $g_i: S^2 \to X'$ be s.t. if maps onto $i^{th}$ generator under

Then: $H_{z}X' \cong H_{z}X \oplus \bigoplus_{i \in I} \mathbb{Z}_{j_{i,x}(b)}$ b generates $H_{z}(b)$.

$\mathop{\sum }\limits_{{i \in  I}}{S}^{2}\overset{V{g}_{i}}{{\longrightarrow}}{X}^{\prime } \rightarrow  Y = {X}^{\prime }\overset{.}{ \cup  } \underset{{Vg}_{i}}{\overset{.}{ \vee  }}{Ve}^{3}$ Then have:

$0 \rightarrow H_{3}X' \xrightarrow{\approx} H_{3}Y \rightarrow \bigoplus_{I} Z \hookrightarrow H_{2}X' \rightarrow H_{2}Y \rightarrow 0 \rightarrow \ldots$

Thus $H_g X \simeq H_g Y \quad \forall g, \quad Y$ is also simply-connected by van Kampen. Finished, $X \to Y$ is acyclic with $\ker(\pi_f) = N$.

General case: Let  $X_{0}^{\prime}=$  covering space of X with  $\pi_{1}X=$

Van Hampen $\Rightarrow$$\pi_{1}Y = \pi_{1}X \times \pi_{1}Y_{0} = N_{1}X \times 0 = N$.

For fixed target Y harder problem. In particular Y=\*.

Dror's thesis: "Acyclic spaces" M.I.T.

Remark: Any group G has a largest perfect subgroup N. normal. (G is generated by all perfect subgroups).

G/N has no non-trivial perfect subgp

Notation: $X \to X^{+} =$ acyclic map killing the largest perfect subgroup of $\pi, X$.

(1)  $X \mapsto X^{+}$  is a homotopy functor
(2)  $(X \times Y)^{+} \sim X^{+} \times Y^{+}$

$x \rightarrow  z$

↓ ↓

$$
X ^ {+} \dots \rightarrow Z ^ {+}
$$

by universal property on killing $\pi_{1}$.

(2) Convert  $X \xrightarrow{f} X^{+}$ ,  $Y \xrightarrow{g} Y^{+}$  into fibrations:

$X \times Y \xrightarrow{f \times q} X^{+} \times Y^{+}$  acyclic map.

$$
\pi_ {1} X ^ {+} = \pi_ {1} X / N
$$

$$
\begin{array}{r l} {\pi_ {1} (X ^ {+} \times Y ^ {+}) =} & {\pi_ {1} X / N \times \pi_ {1} Y / N ^ {\prime}} \\ {=} & {\pi_ {1} X \times \pi_ {1} Y / N \times N ^ {\prime}.} \end{array}
$$

$$
\pi , Y ^ {+} = \pi , Y / N ^ {\prime}.
$$

$$
N \times N ^ {\prime} \text { is   largest   perfect   subgroup. }
$$

So: $X^{+} \times Y^{+} = (X \times Y)^{+}$.

Examples: (1) X acyclic  $\Leftrightarrow$$X^{+}$  contractible (Hurewice & Whitehead)

(2) Suppose X is a closed n-manifold with  $H_{x}(X)=H_{x}(S^{n})$ ; n>2 (homology n-sphere). collapsing map  $X\to S^{n}$ .

${S}_{0}$${X}^{ + } \sim  {S}^{n}$ .

(3) $X = \text{Poincaré homology 3-sphere} = SO(3)/G. = S^3/\tilde{G}$$G = \text{symmetries of the icosahedron} \approx A_S. \quad |G| = 60.$

$\tilde{G} = \text{binary } \text{icosahedral group;} |\tilde{G}| = 120$

${X}^{ + } = {S}^{3}\;{by}\;\left( 2\right)$ .

Take space  $BG \approx K(\tilde{G}_{1})$  for  $\tilde{G}$  discrete.
What is  $(BG)^{+}$ ? Look at fibration.

$$
S ^ {3} \rightarrow S ^ {3} / \tilde {G} \rightarrow B \tilde {G} \rightarrow B S ^ {3} = Q P ^ {\infty}.
$$

$$
\begin{array}{c} \parallel \\ S ^ {3} \xrightarrow [ \text { degree } ]{1 2 0} F _ {S ^ {3}} ^ {\beta} \longrightarrow B G ^ {+} \xrightarrow [ \text { induced } ]{\alpha} B S ^ {3 +} \end{array}
$$

$H_{x}(\alpha)$ is $\Rightarrow$$H_{y}(\beta)$ is iso. $F = (S^{3}/\tilde{G})^{+} = S^{3}$.

Conclude:  $(BG\tilde{G})^{+}$  is a fibre space over  $BS^{3}$  with fibre

Let $A$ be an abelian group, $H(A,n)$. Eilenberg-Maclane space.

$$
\pi_ {g} (H (A, n)) = \left\{ \begin{array}{l l} A & n = g \\ 0 & g \neq n \end{array} \right.
$$

Hurewicz  $\Rightarrow$$H_{q}(K(A,n))=\begin{cases}0 & q<n \\A & q=n \\H_{k+1}=0 & q=n+1\end{cases}$

$$
[ X, H (A, n) ] \cong H ^ {n} (X, A).
$$

Lemma: Let $c: H_n (H(A,n)) \cong A$ be canonical Hurwicz (invers is0. The map:

$$
[ X, H (A, n) ] \longrightarrow H _ {o m} (H _ {n} X, A)
$$

$$
f \mapsto c \cdot H _ {n} (f)
$$

is onto with kernel  $\sim\operatorname{Ext}^{1}(H_{n-1}X,A)$ .

Proof: Universal coefficient formulas

$$
0 \rightarrow E x t ^ {\prime} (H _ {n - 1} X, A) \rightarrow H ^ {n} (X, A) \xrightarrow {P} H o m (H _ {n} X, A) \rightarrow 0\tag{⑪}
$$

Let $X = H(A, n)$, $\exists$ unique cohomology class $u \in H^{n}(H(A, n), A)$. with $\rho(u) = c$.

Fact:  $[X, H(A,n)] \xrightarrow{\sim} H^{n}(X,A)$$f \mapsto f^{*}(u).$

$$
H ^ {\prime \prime} (X, A) \rightarrow H o m (H _ {n} X, A)
$$

$$
f \in [ X, K (A, n) ]
$$

Dror's constructions of an acyclic space AX starting from X.

$X_{2}$  = the covering space of X with  $\pi_{1}X_{2}$  = largest perfect subgp of  $\pi_{1}X$ .

$$
\tilde {H} _ {g} X _ {n} = 0
$$

$$
\text { the   fibre   of } \quad X _ {n + 1} \rightarrow X _ {n} \quad \text { is } \quad \Pi (H _ {n} X _ {n}, n - 1).
$$

Suppose $X_{n}$ is constructed: By Lemma :

$$
[ X _ {n}, H (A, n) ] \simeq H _ {\mathrm{om}} ^ {*} (* h X _ {n}, A).
$$

Let $A = H_{n}(X_{0})$: we get a unique map: $X_{n}: X_{n} \to H(H, X_{0}, n)$. which induces the map:

$$
\overrightarrow {c ^ {\prime}}: H _ {n} X _ {n} \rightarrow H _ {n} (H (H _ {n} X _ {n}, n)).
$$

Put $X_{n+1} = \text{fibre of } x_n$.

$(**)$ is clear, since $\Omega K(A,n)=K(A,n-1)$.

$$
K (H _ {n} X _ {n}, n) = H
$$

Look at Serre spectral sequence of fibration:

$$
E _ {p g} ^ {2} = H _ {p} (K, H _ {g} X _ {n + 1}) \Rightarrow H _ {p + g} (X _ {n}).
$$

![](images/page_11_image_5.jpg)

$$
\widetilde {H} _ {g} X _ {n + 1} = 0 \quad g <   n - 1
$$

$0 \rightarrow H_{n}X_{n+1} \rightarrow H_{n}X_{n} \xrightarrow{\approx} H_{n}K \rightarrow H_{n-1}X_{n+1} \rightarrow 0$ by spectral -

sequence chasing, obtain 5-term sequence.

$$
\therefore \widetilde {H} _ {g} X _ {n + 1} = 0 \quad g <   _ {X _ {n}} ^ {n + 1} \Rightarrow (*)
$$

$$
\begin{array}{l}\vdots\\T \longrightarrow X = X _ {1}\end{array}\rightarrow X _ {2} \xrightarrow [ x _ {2} ]{H (H _ {2} X _ {2} , 2)}
$$

$$
\text { Put } A X _ {\infty} = \lim _ {n \to \infty} X _ {n}. \quad \text { Then } \quad \tilde {H} _ {x} (A X) = 0 \quad \therefore A X \text { is   a   cyclic }
$$

Proposition: For any acyclic space T, [T,AX]→[T,X].

Proof: see picture p.12.  $[T, H(A,n)] = H^{n}(T,A) = 0$ .

$[T, H(H_{n}X_{n,n-1})]\rightarrow[T, X_{n+1}]\rightarrow[T, X_{n}]\rightarrow[T, H(H_{n}X_{n},\pi)]$

Exercises: 1) Show $X^{+} = \text{Cone } (AX \to X)$  
2) Show $AX = \text{Fibre of } (X \to X^{+})$

Schur multipliers and central extensions:

G group:

$(E_{p})$ is a central extension of G if (by A)

$1 \rightarrow A \rightarrow E \rightarrow G \rightarrow 1$

and $A \subset$ center of $E$.

$(E,p)$ is a universal central extension of $G$ if far any central extension $(E',p')$$\exists !$ homomorphism $h: E \to E'$ s.t.

$E \xrightarrow{h} E'$$\downarrow_{P} \downarrow_{P'}$$G$

commutes.

Proposition: (i) If  $(E,p)$  is a universal central extension then
E is perfect :  $E = (E, E)$ .

(Hence if a universal central extension exists, G is perfect)
(ii) Any perfect G has a universal central extension.

Let $E^{ab} = E / (E, E)$.

Lemma: Let  $(E,p)$ ,  $(E',p')$  be central extensions. If E is perth then there exists at most one map  $E \rightarrow E'$  (over G).

Proof: If  $\alpha_{1},\alpha_{2}:E\Longrightarrow E^{\prime}$ , define:  $E\xrightarrow{+}\ker(p^{\prime})$ . by

$f(e) = \alpha_{1}(e) \cdot \alpha_{2}(e)^{-1}$. Then $f$ is a homomorphism.

$\alpha_{1}(e)=f(e)\cdot\alpha_{2}(e)$

$\alpha_{1}(ee') = \alpha_{1}(e)\cdot\alpha_{1}(e') = f(e)\cdot\alpha_{2}(e^{-})\cdot f(e')\cdot\alpha_{2}(e'^{2}) = f(e)f(e')\cdot\alpha_{2}(e^{-})\cdot\alpha_{2}(e'')$$f(x)(p')$$f(x) \cdot f(e') \cdot \alpha_{2}(ee')$$center E$$V.$

Then $f$ is a homomorphism to an ebelian group $\therefore f = 0$. $\therefore \alpha_{1} = \alpha_{2}$.

Proof of (ii): Write $G = F/R$, $F$ free. Put $E = F/(F,R)$. Put :

$1 \rightarrow R/(F, R) \rightarrow F/(F, R) \rightarrow F/R \rightarrow 1.$

(2) E is a central extension of G. √

(b) E maps to any other central extension  $E'$  of G.

![](images/page_13_image_10.jpg)

.by freeness

${RF} \rightarrow  G$

$$
\text { since } \alpha ((F, R)) = 0.
$$

(c) E is perfect.

(e)  $(E, E)$  has properties (1), (2).

Claim:  $(E,E)$  is perfect.

Take  $(e_{1},e_{2})\in(E,E)$$e_{1}e_{2}e_{1}^{-1}e_{2}^{-1}$

$(e_{1},c_{2})=(e_{1}^{\prime},e_{4}^{\prime\prime}),(e_{2}^{\prime},e_{3}^{\prime\prime}))$ . so: $(E,E)\subseteq((E,E),(E,E))$

Def: If  $(E_{p})$  is the universal central extension of a perfect group G, then  $\ker(p)$  is called the Schur multiplier of G.

Schur:(1) Alternating group  $A_{n}, n \geq 5$ 

Schur multiplier of  $A_{n} = Z/2Z$ .

(2)  $SL_{3}(F_{2})$  size  $(2^{3}-1)(2^{3}-2)(2^{3}-3)$ 

7.6.4 = 168

 $PSL_{2}(F_{7}) = SL_{2}(F_{7}) / \{\pm id\} = \frac{(49-1)(49-7)}{6.2} = 168$$SL_{3}(F_{2}) \cong PSL_{2}(F_{7}) = SL_{2}(F_{7}) / \{\pm 1\}$ 

universal central extension of  $PSL_{2}(F_{7})$  is  $SL_{2}(F_{7})$ 

∴ Schur multiplier is Z/2Z.

G discrete group.
BG - classifying space of topological group. (classifying principal G-bundles).
in discrete case classifies covering spaces with G acting as deck transformations.

$BE = X_{3} \rightarrow H(H_{3}X_{3}, 3)$

Dror construction:

$$
B N = \begin{array}{c} X _ {2} \\ \downarrow \end{array} \longrightarrow K (H _ {2} X _ {2}, 2).
$$

N-largest perfect subgp of G.

$$
B G = X _ {1}
$$

Have fibration:  $H(H_{2}X_{2,1}) \rightarrow X_{3} \rightarrow X_{2}.$$H(N,1)$

$$
\text { Put } \quad \pi , X _ {3} = E.
$$

$$
1 \rightarrow H _ {2} B N \rightarrow E \rightarrow N \rightarrow 1
$$

Proposition: $E$ is the universal central extension of $N$.

Proof: Recall:  $F \rightarrow E \rightarrow B$  fibration of pointed spaces.
then  $\pi_{1}E$  acts on  $\pi_{*}F$  as follows.

Loop  $\alpha:\overrightarrow{B_{1}}\mapsto E$  Map  $F\times[0,1]\xrightarrow{H}\overrightarrow{B_{2}}\mapsto B$$\downarrow$$[0,1]$

![](images/page_15_image_11.jpg)

$$
(f, t) \mapsto p (\alpha (t))
$$

![](images/page_15_image_13.jpg)

$$
F _ {x} [ 0, 1 ] \underset {p r _ {2}} {\rightarrow} [ 0, 1 ] \underset {p \cdot \alpha} {\longrightarrow} B
$$

This describes the action.

Must use homotopy extension property.

行

$\Pi(H_{2}X_{2,1}) \longrightarrow \Omega\Pi(H_{2}X_{2,2}) = \Pi(H_{2}X_{2,1})$$X_{3} \longrightarrow * = P(\Pi(H_{2}X_{2,2}))$$X_{2} \longrightarrow \Pi(H_{2}X_{2,2})$

The action of $\pi_1 X_3$ on $\pi_x (H(H_2 X_2, 1)))$ is induced by action of $\pi_x (*) = 1$. $\therefore \pi_1 X_3$ acts trivially on $H_2 X_2 = \pi_1$ and $E$ is a central extension of $N$ by $H_2 X_2 = H_2(BN)$.

Lemma: IF N is perfect s.t.  $H_{2}(BN)=0$ , then N has no non-trivial central extensions (i.e., if  $E\to N$  is a central extension, and E is perfect then  $E\cong N$ ).

Proof: Suppose E is central extension of N.
 $1 \rightarrow A \rightarrow E \xrightarrow{p} N \rightarrow 1$

Induces map: $BA \rightarrow BE \xrightarrow{B_p} BN$ 
convert Bp to fibration
$BA = IT(A, V)$ is fibre.

Obstruction theory classifies fibrations with fibre  $K(A,n)$  in terms of  $H^{m+1}(-,A)$

Fact: Given a fibration  $\pi(A,n)\rightarrow E\rightarrow B$  with  $\pi(\cdot)$  acting trivially on A is induced from:

$$
K (A, n) \longrightarrow * \longrightarrow K (A, n + 1).
$$

by a unique map $B \rightarrow  K(A, n+1)$.

$u \in [BN, K(A_2)] - H^2(BN, A) = Hom(H_2B_n, A) \oplus Ext(H, BN, A).$$0 = 0$$so u is trivial.$

This implies $B_p$ has a section and $E$ is trivial extension $\cong N \times A$.

$\widetilde{H}_{q}(X_{3})=0$  g≤2 and  $X_{3}=BE$ , we have then:

(a) E is perfect.  $(H_{1}(BE)=(\pi,(BE))^{ab}=E^{ab}\neq0)$ 

(b) E has no non-trivial central extensions by Lemma.

Pf of Prop: Have shown E is a central extension of N. Show universality. Since E is perfect, it suffices to show. E map to any other central extension (E',p').

$1 \rightarrow A' \rightarrow E' \xrightarrow{p'} N \rightarrow 1$

$1 \rightarrow A' \rightarrow E \times E' \rightarrow E \rightarrow 1$ fibre product

But $E'_{N}$ is a central extension of E via $pr_{2}$. By (b) above obtain section of $pr_{2}$, hence a map from $E \to E$ over N.

Corollary:  $H_{2}(BN)$  = Schur multiplier of N for any perfect group N.

$\pi, X_{n+1} \rightarrow \pi, X_n$  n≥3.

from fibration:  $H(H_{n}X_{n}, n-1) \rightarrow X_{n+1} \rightarrow X_{n}.$

$\pi,(AX)=\pi,X_{n}$  for n≥3
= E universal centre extension of N

Def: (Oror): G is super-perfect if it is perfect and every central extension of G is trivial. i.e.  $H_{1}(BG) = H_{2}(BG) = 0$ .

Exercise:(1) Show that if X is acyclic, then  $\pi_{1}X$  is superperfect.
(2) Conversely if G is superperfect ∃ acyclic space  $\pi_{1}X = G$ .
Let X = A (BG).

Problem: Understand the functor:  $X \mapsto X^{+}$ .

Let $G$ be finite perfect group.

Fact:  $H_{n}(BG;\mathbb{Z})$  finite abelian groups killed by |G|.

Look at  $(BG)^{+}$ , a simply-connected space with

$\widetilde{H}_{g}(BG^{+})=\widetilde{H}_{g}(BG)$  finite, killed by |G|.

$\pi_{*i}(BG^{+})$  finite, killed by  $|G|^{N_{i}}$

Homotopy theory $\Rightarrow$$\pi_{i}$$BG^{+}=\prod_{p\mid1\mid G}\mathsf{X}_{p}$.

can you tell about $X_p$ in terms of groups structure of $G$. (e.g. p-subgroups of $G$).

Let $A$ be an associative ring with 1.

Def:  $K_{0}A = \text{Grothendiecte group of f.g. projective A-modules}$

$P = \ln(A^n \to A^n) \quad c^2 = e, \quad \text{so correspond to independent matrices.}$

Two possible dfns of Grothendieck groups.

(1) Its the group having one generator [P] for each fin. gen.
projective P and the relations: [P] = [Q] if P ≈ Q.
[P⊕Q] = [P] + [Q] direct sum G. group

(2) Same generators [P] with one relation: exact sequence Gr.

$[P] = [P'] + [P'']$ for each s.e.s.

$0 \rightarrow P' \rightarrow P \rightarrow P'' \rightarrow 0.$

(z)⇒(1) easy. Remark:  $\left(\begin{array}{c} direct sum \\ Groth, gp\end{array}\right)\longrightarrow\left(\begin{array}{c} exact sequence \\ Groth, gp.\end{array}\right)$

and this map is iso in our case, since any s.e.s:

$0 \rightarrow R \rightarrow E \rightarrow P \rightarrow 0$ of A-modules

with P projective splits.

Example of a category of A-modules where two Grothendieck groups differ: Let  $A = Z/p^{2}Z$ , take category of finitely generated A-modules. (= finite abelian groups killed by  $p^{2}$ ). Call one Ms

$$
M \approx (\mathbb {Z} / _ {p} \mathbb {Z}) ^ {i} \times (\mathbb {Z} / _ {p ^ {2}} \mathbb {Z}) ^ {j}
$$

Hence  $\left(\begin{array}{c}\text { direct sum } \\ \text { Grothendieckgp }\end{array}\right) \approx Z \oplus Z$  with generators  $[Z/pZ],[Z/p^{2}Z]$$\left(\begin{array}{c}\text { exact sequence } \\ \text { Grothendieckgp }\end{array}\right) \approx Z$  with generator  $[Z/pZ]$

use Krull-Schmidt, Jorden Hölden to give most general result.
0 → Z/pZ → Z/p²Z → Z/pZ → 0
so [Z/p²Z] = 2 [Z/pZ]

Put $P(A) = \text{category of all fin-gen. projective A-modules.}$
and A-module homomorphisms
$\text{Iso } (P(A)) = \text{iso. classes of } P(A).$

Any abelian monoid M gives rise to an abelian  $\overline{M}$  described as follows.

$$
\overline {{M}} = M \times M / (m, S) = (m _ {1}, s _ {1}) \quad i j
$$

$$
+ o n \overline {{M}} i s (m, s) + (m _ {1}, s _ {1}) = (m + m _ {1}, s + s _ {1}).
$$

∃ map: M→M given by m ↦ (m,0). is universal for maps of M to a group.

Claim:  $Y_{0}A = \overline{\text{Iso}(g(A))}$

Examples: (1) A division ring or field.

$$
S _ {0}: \quad H _ {0} (A \times B) = H _ {0} A \times H _ {0} B.
$$

(3) Dedehind domain A,  $P_{ic}(A)=$  ideal class group of A.

 $I_{\infty}(P_{A}) = N \times P_{ic}(A)$$[P] \rightarrow (\text{rank}(P), \Lambda^{r}P)$ 

So  $P_{ic}(A) =$  iso classes of  $P \in P_{A}$  of rank 1.

$$
I _ {s o} (y _ {A}) = (0, 0) \cup (N - \{0 \}) \times P _ {i c} (A) \subset N \times P _ {i c} (A).
$$

$$
[ P ] \mapsto (\operatorname{rank} P, \Lambda^ {n k (P)} P).
$$

$\Rightarrow  {H}_{0}A = Z \times  {Pic}\left( A\right)$ gives complete description.

(4)  $H_{0}A[T_{1},\ldots,T_{r}]=H_{0}A$  if A regular, Noetherien (eg. A a field) (Grothendieck-Serre).

Not known if f.g. projective module over  $F[T_{1},\ldots,T_{r}]$  is free (Serre's conjecture).

$$
\begin{array}{r l} {\mathrm{Let} \quad G L _ {n} (A) = G L (n, A)} & {= \mathrm{groupofinvertible(n×n)matrices.}} \\ & {= \mathrm{Aut} (A ^ {n}).} \end{array}
$$

$$
E _ {n} (A) = \text {   subgp   generated   by   } E _ {i j} ^ {2} = I + a \left( \begin{array}{c} j ^ {\text {   column   }} \\ 1 \end{array} \right) \leftarrow i ^ {+ t}, i \neq j; a \in A.
$$

$$
(e _ {i j} ^ {2}) ^ {- 1} = e _ {i j} ^ {- 2}
$$

$$
\begin{array}{r l} {(z)} & {(e _ {i j} ^ {a}, e _ {k l} ^ {b}) = e _ {i j} ^ {a} e _ {k l} ^ {b} e _ {i j} ^ {- a} e _ {k l} ^ {- b}} \\ & {\qquad = 0. 1 \qquad y \qquad \{i, j \} \cap [ k, l ] = \phi .} \end{array}
$$

$$
(e _ {i j} ^ {2} e _ {j k} ^ {b}) = e _ {i k} ^ {2 b}
$$

$$
(e _ {i j} ^ {2}, e _ {k i} ^ {b}) = e _ {k j} ^ {- b a}
$$

$$
\begin{array}{r l}{G L _ {n} (A)}&{\rightarrow G L _ {n + 1} (A)}\\{\alpha}&{\rightarrow (\stackrel {\circ} {0};)}\end{array}
$$

$$
\checkmark \text { gives   you } E _ {n} (A) \text { perfect, for } n \geq 3.
$$

$$
E (A) = \lim _ {n \to \infty} E _ {n} (A)
$$

$$
G L (A) = \lim _ {n \to \infty} G L _ {n} (A).
$$

$$
\text { Whitehead   Lemma: } E (A) = (E (A), E (A)) = (G L (A), G L (A)) \subseteq G L (A)\tag{23}
$$

$$
\text {   To   show   } (G L (A), G L (A)) \subseteq E (A).
$$

$$
\text { Let } \alpha , \beta \in G L (A), \text { say } \alpha , \beta \in G L _ {n} (A). \text { Work   in } G L _ {2 n} (A).
$$

$$
\left( \begin{array}{l l} \alpha \beta \alpha^ {- 1} \beta^ {- 1} & \\ & 1 \\ & 1 \end{array} \right) = \left(\left( \begin{array}{l l} \alpha & \\ & \alpha^ {- 1} \\ & 1 \end{array} \right), \left( \begin{array}{l l l} \beta & & \\ & 1 & \\ & & \beta^ {- 1} \end{array} \right)\right)
$$

$$
\text {   Enough   to   show   } \left( \begin{array}{c c} \alpha & \alpha^ {- 1} \\ & 1 \end{array} \right), \left( \begin{array}{c c} \beta & \\ & \beta^ {- 1} \end{array} \right) \in E _ {\mathrm{sn}} (A).
$$

$$
\text { Proof   that } \quad \left( \begin{array}{c c} \alpha & 0 \\ 0 & \alpha^ {- 1} \end{array} \right) \in E _ {2 n} (A).
$$

$$
\left( \begin{array}{l l} 1 & \alpha \\ 0 & 1 \end{array} \right) \left( \begin{array}{l l} \alpha & 0 \\ 0 & \alpha^ {- 1} \end{array} \right) = \left( \begin{array}{l l} \alpha & 1 \\ 0 & \alpha^ {- 1} \end{array} \right) \quad ③ \quad \left( \begin{array}{l l} 1 & \alpha \\ 0 & 1 \end{array} \right) \left( \begin{array}{l l} \alpha & 1 \\ - 1 & 0 \end{array} \right) = \left( \begin{array}{l l} 0 & 1 \\ - 1 & 0 \end{array} \right)
$$

$$
Ⓩ \left( \begin{array}{l l} 1 & \\ - 1 & 1 \end{array} \right) \left( \begin{array}{l l} \alpha & 1 \\ 0 & \alpha^ {- 1} \end{array} \right) = \left( \begin{array}{l l} \alpha & 1 \\ - 1 & 0 \end{array} \right)
$$

$$
\begin{array}{r l} & {\left( \begin{array}{l l} \alpha & 0 \\ 0 & \alpha^ {- 1} \end{array} \right) = \left( \begin{array}{l l} 1 & \alpha \\ 0 & 1 \end{array} \right) \left( \begin{array}{l l} 1 & 0 \\ \alpha^ {- 1} & 1 \end{array} \right) \left( \begin{array}{l l} 1 & \alpha \\ 0 & 1 \end{array} \right) \left( \begin{array}{l l} 0 & 1 \\ - 1 & 0 \end{array} \right)} \\ & {= \frac {1}{2} \left( \begin{array}{l l} 1 & 1 \\ 0 & 0 \end{array} \right) \left( \begin{array}{l l} 1 & 0 \\ - 1 & 1 \end{array} \right) \left( \begin{array}{l l} 1 & 1 \\ 0 & 1 \end{array} \right)} \end{array}
$$

$$
\left( \begin{array}{l l} 1 _ {k} & * \\ 0 & 1 _ {n - k} \end{array} \right) \quad \text { is   a   product   of } e _ {i j} ^ {2} \quad i + 1 <   i, j \leq n - k. \text { etc. }
$$

$$
E _ {x}; \quad A := \text { skew - field } F; T h m o f D i e u d o n n e: G L _ {n} (F) / E _ {n} (F) = (F ^ {*}) ^ {2}
$$

$$
(e x c e p t f o r n = 2, F = F _ {2}).
$$

$$
K _ {1} F = F ^ {*}, \quad \text { since } \quad K _ {1} F = G L (F) / E (F) \xrightarrow [ d e t ]{\alpha} F ^ {*}
$$

1) Dieudonne's theory of non-commutative determinants, for a skew field F;

$$
G L _ {n} (F) / E _ {n} (F) \simeq (F ^ {*}) ^ {a b}
$$

2) A Euclidean domain:  $E_{n}A = SL_{n}(A)$$\forall n \geq 2$

$$
K _ {1} A = A ^ {*} = \text { units   in } A.
$$

$$
K _ {1} Z = Z ^ {*} = \{\pm 1 \}. \quad (\text { local   ring } a l s o)
$$

Def: $St(A) = \text{Steinberg group of } A$ is the group with generators $X_j^a$, $a \in A$, $i \neq j$, $1 \leq i, j \leq n$. and the relations:

$$
x _ {i j} ^ {2} x _ {i j} ^ {b} = x _ {i j} ^ {a + b}
$$

$$
(x _ {i j} ^ {2}, x _ {k l} ^ {b}) = 1 \quad i \neq l \text { and } j \neq k.
$$

$$
3 \leq n \leq \infty
$$

$$
x _ {i l} ^ {2 b} \quad i j \quad i, j = k, l d i s t i n c t
$$

$$
S t _ {w} (A) = S t (A)
$$

$$
x _ {i j} ^ {2} \mapsto e _ {j i} ^ {2}.
$$

$BG^{+}$ ; Will show that one has following:

$$
K _ {i} A = \pi_ {i} B G L (A) ^ {+}
$$

$i = 1,2.$ (not $i = 0$ since connected

This will be our definition i ≥ 1.

$$
x _ {1} = B G
$$

$$
\lim _ {\leftarrow} = A (B G).
$$

tower of fibrations.  $BN \rightarrow PIT(H_{2}BN, 2)$

$$
B N \rightarrow H (H _ {2} B N, 2)
$$

$$
X _ {n + 1} \rightarrow X _ {n} \rightarrow \pi (H _ {n} X _ {n, n})
$$

$$
\pi_ {q} X _ {n + 1} \rightarrow \pi_ {q} X _ {n} \rightarrow \pi_ {q} (H (H _ {n} X _ {n, n})) \rightarrow \pi_ {q - 1} (X _ {n + 1}).
$$

$$
\pi_ {q} (B \widetilde {N}) = \left\{ \begin{array}{l l} 0 & 0. w \\ \widetilde {N} & q = 1 \end{array} \right. \quad \pi_ {q} (X _ {4}) = \left\{ \begin{array}{l l} \widetilde {N} & q = 1 \\ H _ {5} X _ {3} & q = 2 \\ 0 & q \geqslant 3 \end{array} \right.
$$

$$
\pi_ {q} X _ {n} = \left\{ \begin{array}{l l} \tilde {N} & q = 1 \\ H _ {q + 1} X _ {q + 1} & 2 \leqslant q \leqslant n - 2 \\ 0 & o w \end{array} \right.
$$

$$
\pi_ {q} (A (B G)) = \left\{ \begin{array}{l l} \tilde {N} & q = 1 \\ H _ {q + 1} X _ {q + 1} & q \geq 2. \end{array} \right.
$$

$$
\text { by   above   result. }
$$

$$
A (B G) = \text { fibre   of } B G \rightarrow B G ^ {+}
$$

$$
A B G \rightarrow B G \rightarrow B G ^ {+}
$$

$$
\dots \rightarrow \pi_ {g} A (B G) \rightarrow \left\{\begin{array}{l l}G&g = 1\\0&g \neq 1\end{array}\right\}\rightarrow \pi_ {g} B G ^ {+} \xrightarrow {\partial} \pi_ {g - 1} (A (B G)).
$$

$$
\pi_ {g} (B G ^ {+}) = \left\{ \begin{array}{l l} G / N & q = 1 \\ H _ {2} (B N) & q = 2 \\ H _ {g} X _ {g} & q \geq 2 \end{array} \right.
$$

Exercise: Show the Dror tower is $AX \rightarrow \ldots \rightarrow X_2 \rightarrow X_1 = X$ is the Postmkov tower for $X \rightarrow X^+$.

Take $G = GL(A)$, $E(A)$ generated by $e_{ij}^{\alpha}$.

$$
E (A) = (E (A), E (A)) = (G L (A), G L (A)). \quad \mathrm{So} \quad E (A) \mathrm{islargest}   \mathrm{perfectsubgroupof} G L (A).
$$

$$
\begin{array}{l} {S t (A) = \text {   group   with   generators   } x _ {j} ^ {2} \quad 1 \neq j \quad 1 \leq i, j <   \infty . z \in A} \\ {\text {   and   relations   above.   }} \end{array}
$$

$$
\begin{array}{r l}{K _ {1} A}&{= G L (A) / E (A)}\\{K _ {2} A}&{= k e r \{\phi : S t (A) \rightarrow E (A) \}}\\&{= H _ {2} (B E (A), Z) = H _ {2} (K (E (A), 1), Z),}\end{array}
$$

$$
\pi_ {1} (B G L (A) ^ {+}) = G L (A) / E (A) \quad b y \quad e b o v e.
$$

$$
\pi_ {2} (B G L (A) ^ {+}) = H _ {3} (B E A), \mathbb {Z}). \quad \mathrm{So~we~define}
$$

$$
H _ {n} A \simeq \pi_ {n} (B G L (A)) ^ {+}.
$$

27

Don construction for BGL(A)

$$
\begin{array}{l} {B E (A) \longrightarrow K (H _ {2} B E A, 2)} \\ {\downarrow} \end{array}
$$

$$
B G L (A) \longrightarrow K (H, B G L A ^ {\bullet}, 1)
$$

$(2/48, Lee \cdot S_{379} \text{ dev})$

$$
H _ {3} A = H _ {3} (S t (A), \dot {\mathbb {Z}}).
$$

$H_{3}Z$ is unknown.

Universal property of BGL(A) $^{+}$ :

$$
B G L (A) \xrightarrow {f} B G L (A) ^ {+}
$$

![](images/page_26_image_9.jpg)

use obstruction theory.

IF  $\pi_{1}(u)(\text{当}E(A))=0$ , then  $\exists!h\Rightarrow h\cdot f\sim u$ .

月ecell

![](images/page_26_image_13.jpg)

A→B ring homomorphism induces

$$
G L (A) \rightarrow G L (B)
$$

$$
B G L (A) ^ {+} \rightarrow B G L (B) ^ {+}.
$$

$$
u _ {*}: \mathrm{IT} _ {n} A \longrightarrow \mathrm{IT} _ {n} B.
$$

$K_{n}$ is a functor from rings to abelian groups.

product of rings $A \times  {A}^{\prime }$ .

$$
G L (A \times A ^ {\prime}) = G L (A) \times G L (A).
$$

Fact:  $B(G \times G') \sim BG \times BG'$ .

$$
B G L (A \times A ^ {\prime}) \sim B G L (A) \times B G L (A ^ {\prime}).\tag{28}
$$

$$
(X \times Y) ^ {+} \sim X ^ {+} \times Y ^ {+}
$$

$$
B G L (A) \times A ^ {\prime}) ^ {+} \sim B G L (A) ^ {+} \times B G L (A ^ {\prime}) ^ {+}
$$

$$
H _ {n} (A \times A ^ {\prime}) = H _ {n} A \times H _ {n} A ^ {\prime}
$$

Theorem:  $BGL(A)^{+}$  is a homotopy associative and commutative H-space.

$$
G L _ {n} (A) \times G L _ {p} (A) \rightarrow G L _ {n + p} (A)
$$

$$
\alpha \oplus \beta \mapsto \left( \begin{array}{l l} \alpha & 0 \\ 0 & \beta \end{array} \right) \stackrel {\uparrow} {\downarrow} \quad \text { Whitney   sum. }
$$

$$
\alpha \oplus (\beta \oplus \gamma) = (\alpha \oplus \beta) \oplus \gamma
$$

$\alpha\oplus\beta\neq\beta\oplus\alpha.$  they are conjugate in  $GL_{nip}(A)$

Choose  $N = \{1, 2, 3, \ldots\}$  and choose  $N \subseteq N \xrightarrow{\varepsilon} N$$\varepsilon: GL(A) \times GL(A) \to GL(A)$

$$
\varepsilon_ {x} (\alpha , \beta) _ {k, l} = \mathrm{etc.} B G L (A) ^ {+} + B G L (A) ^ {+} \rightarrow B G L (A) ^ {+}.
$$

Reduction of theorem to:

Lemma: Given an embedding $u: N \to M$, $N = \{1,2,\ldots\}$ then the induced map $\mu_{*}: BGL(A)^{+} \to BGL(A)^{+}$ is homotopic to the identity.

Sublemmal: $u_*$ is a homotopy equivalence.

Lemma: Let M be the monoid of embeddings  $N \hookrightarrow N$ . Then any homomorphism  $M \hookrightarrow G$  with G a group is trivial.

Proof: Given any  $u, v \in M$ , define  $z_{n}$  embedding  $V_{*}(u)$

$n \notin \operatorname{Im}(V).$

Choose v so that complement of  $\operatorname{lm}(v)$  is  $\infty$ , whence  $\exists w \in M$  st.  $\operatorname{lm}(w) \cap \operatorname{lm}(v) \neq \phi$ . then  $y_{*}(u) \circ w = w$ .

$$
\rho (v _ {*} (u) \cdot w) = \rho (w)
$$

but:  $V_{*}(u) \cdot v = v \cdot u$ .  $\rho(v_{*}(u)) \rho(v) = \rho(v) \rho(u) \rightarrow \rho(u) = 1.$

(1) Proof: Step (1) $u_*$ induces homology isomorphism.  
Step (2) Show $\pi_1(BGL(A)^+)$ acts trivially on $H_*(BGLA^+)$. Then can apply a suitable version of Whitehead Theorem.  
$H_*(BGL(A)^+) = H_*(BGL(A)) = \varinjlim H_*(BGL(A))$

$H_{*}(BGL_{n}(A)) \longrightarrow H_{*}(BGL(A))$ Fact: Inner automorphisms of G
$u_{*}^{n} \downarrow u_{*}$ act trivially on $H_{*}(BG)$

Theorem. BGL(A) $^{+}$ is a homotopy commutative and 2ssociative H-sp

Key point in proof is to show $u_* \sim$ id on BGL(A)$^+$ for any embedding $u: N \hookrightarrow N$. Follows from above lemmas.

Proof of Lemma 1: By Whitehead Thm., it suffices to show $u_*$ induces on $\pi_1 (BGL(A)^+) = BL(A)/E(A) = H_1 (BGL(A))$. and on $H_*$ of universal cover $BGL(A)^+ = BE(A)$.

But: Remark:

$$
\begin{array}{c} \overbrace {B G L (A ^ {+})} = B E (A) ^ {+} \\ \overbrace {\downarrow} ^ {I} \xrightarrow [ f ]{} \overbrace {B G L (A) ^ {+}} \\ B G L (A) \xrightarrow [ f ]{} B G L (A) ^ {+}. \end{array}
$$

T must be the covering of BGL(A); with  $\pi_{1}(T)=E(A)$ 

So: T=BE(A)

f' acyclic  $\Rightarrow$  f' acyclic, so  $H_{*}(f')$  is iso.  $\Rightarrow$  BE(A) $^{T}$  = BGL

Exercise: Dror tower:

Show the tower of (A) spaces is the Postnikov system of BGL(A)$^{+}$.

$X_{4} \longrightarrow X_{4}$$X_{3} \longrightarrow B X_{3}^{+} = B S + (A)^{+} X_{3}$$BE(A) \longrightarrow BE(A)^{+} = R_{2}$$BG_{L}(A) \longrightarrow BG_{L}(A)^{+} = R_{1}$

$$
E (A) = \cup E _ {n} A.
$$

$$
\Rightarrow B E (A) = \lim _ {\rightarrow} B E _ {0} (A)
$$

$$
\begin{array}{c} \text { converts   maps   to   wifbrations   with   map } \\ B E _ {1} \xrightarrow {} B E _ {2} \xrightarrow {} B E _ {3} \xrightarrow {} \dots \end{array} \to U B
$$

$$
\Rightarrow H _ {y} (B E (A)) = \underbrace {\lambda_ {m}} _ {\rightarrow} H _ {*} (B E _ {n} (A)).
$$

$$
\begin{array}{l} \text {   mmapping   telescope.   } \\ E _ {n} = E _ {n} (A). \end{array}
$$

To show $u_*$ induces identity on $H_*(BE)$ it is enough to show $u_* \cdot i_*$ and $i_*$ induce same map from $H_*(BE_n) \to H_*(BE)$.

$$
\{1, \ldots n \} \mapsto \{u (1), \ldots , u (n) \} \leq N
$$

$$
\left( \begin{array}{l l} \sigma & 0 \\ 0 & \sigma^ {- 1} \end{array} \right) \in E _ {2 N}.
$$

FACT: Conjugation acts trivially on  $H_{*}(BG)$ .

$$
\text { One   can   take } P _ {*} = C _ {*} (\widetilde {B G}).
$$

$$
C _ {i} (B G, M) = C _ {i} (\widetilde {B G}) \otimes M
$$

$$
C _ {*} (B G, M) = C _ {*} (\widetilde {B G}) \oplus_ {\mathbb {Z} [ G ]} M
$$

$$
H _ {1} (B G, M) = H _ {1} (- 1) = H _ {1} (G M)
$$

$$
\pi_ {0} \left[ ((X, *) ^ {(z, x)}) _ {\pi , X} \right] = \pi_ {c} (X ^ {z})
$$

$\pi_{1}X \text{ acts on } [Z,X]$

[Z⊥pt, BG] → Hom(π, Z, G) / conjugation by elts of G

by above remarks.

An inner automorphism of $G$ induces a map on BG which is homotopic to the identity, (not base pt preserving $\sigma$ induces id on $H_{*}$ (BG)) $\varphi \equiv D$.

Theorem (Milnor & Moore): Suppose M is a connected H-space.

$Q \otimes _{Z} \Pi_{i} M \xrightarrow{\approx} \text{Prim}\{H_{i}(M, Q)\}$

33

Corollary:  $H_{i}A \otimes Q \simeq \operatorname{Prim} H_{i}(BG\angle A), Q)$

$$
\pi_ {i} (B G L (A) ^ {+}) \otimes Q = P _ {\mathrm{im}} (H _ {i} (B G L (A) ^ {+}, Q).
$$

Theorem of Borel: F number field with  $r_{1}$ , real,  $r_{2}$  complex absolute values.

$$
[ F: \mathbb {Q} ] = r _ {1} + 2 r _ {2}
$$

Let $A = \text{ring of integers in } F = \text{int closure}_F(Z)$

$$
\mathrm{dim} (H _ {i} A \otimes Q) = \left\{ \begin{array}{l l} 1 & i = 0. \\ r _ {1} + r _ {2} - 1 & i = 1 \\ 0 & i \equiv 2 \\ r _ {2} & i \equiv 3 \\ 0 & i \equiv 0 \\ r _ {1} + r _ {2} & i \equiv 1 \end{array} \right. (\mathrm{mod} 4)
$$

$$
K _ {0} A = \mathbb {Z} \oplus P _ {i c} (A)
$$

$$
\begin{array}{l} \text { funte   ideal } \\ \text { class   group } \end{array}
$$

$$
A = \mathbb {Z}
$$

$$
k _ {0} Z = Z
$$

$$
H _ {1} Z = Z / 2 Z \quad (u n i + s)
$$

$$
H _ {2} \mathbb {Z} = \mathbb {Z} / 2 \mathbb {Z} (M i n o r)
$$

$$
d i m (H _ {3} Z \oplus Q) = 0 - r _ {2}
$$

$$
\dim (\Pi_ {y} Z \otimes Q) = 0
$$

$$
\dim (H _ {s} ^ {\prime} \mathbb {Z} \otimes Q) = 1
$$

Ex. 2.

$$
F = Q [ \sqrt {a} ]
$$

$$
1, 1, 0 0 0 2, 0 0 0 2,
$$

$$
r _ {1} = 2
$$

$$
r _ {2} = 0
$$

$$
F = Q [ \sqrt {- q} ]
$$

$$
r _ {1} \div 0
$$

$$
1, 0, 0 1 0 1, 0 1 0 1,
$$

$$
r _ {2} = 1
$$

Let $A$ be a fixed ring, $GL_n = GL_n(A)$, $n$ fixed.

$$
G _ {n} = \left\{\left( \begin{array}{c c c} 1 _ {n} & x \\ - & - & - \\ 0 & G L _ {n} \end{array} \right) \right\} \subseteq G L _ {r + n} (A)
$$

= group of antimorphisms of exact sequences

$$
0 \rightarrow A ^ {r} \rightarrow A ^ {r + n} \rightarrow A ^ {n} \rightarrow 0
$$

which identity on subspace quotient $A^{n}$.

$$
G _ {n} = G L _ {n} (A) \times H _ {m} (A ^ {n}, A ^ {r}) \longleftrightarrow G L _ {n} (A)
$$

$$
G _ {n} \xrightarrow [ \pi \cdots s ]{P} G L _ {n} (A) \quad s (\alpha) = \left( \begin{array}{l l} 1 & 0 \\ 0 & \alpha \end{array} \right)
$$

$$
p (\cdot_ {0} ^ {1} \cdot_ {\alpha} ^ {*}) = \alpha .
$$

$$
H _ {*} (G _ {n}) = H _ {*} (G L _ {n}) \oplus [ k e r (p _ {*}) ]
$$

$$
\text { Theorem: } \quad \lim _ {n \to \infty} H _ {*} (G _ {n}) \cong \lim _ {n} H _ {*} (G L _ {n}).
$$

Topological analogue: take  $GL_{n}(\mathbb{C})$  with its topology.

$$
\beta (G _ {n} \mathbb {C}) \xleftarrow {\mathrm{Bs}} B G L _ {n} (\mathbb {C})
$$

$$
\left( \begin{array}{c c} 1 & M _ {r n} (\mathbb {C}) \\ & B L _ {n} \mathbb {C} \end{array} \right) / A L _ {n} \mathbb {C} \cong M _ {r n} (\mathbb {C}) \quad \text {   wntactite   }.
$$

Correspond to statement in vector bundle theory that:

short exact sequences of vector bundles split, use Riemania metric in standard way.

Example:  $A = F_{p}$ .  $SL_{1} = F_{p}^{*} \subseteq \begin{pmatrix} 1 & F_{p} \\ 0 & F_{p}^{*} \end{pmatrix} = G_{1}$

$H_{*}(F_{p}^{*})$ has no p-torsion

$H_{0}(G_{1})$ has p-torsion for $\infty$ many n.

Show theorem needs  $\xrightarrow{lim}$  above.

Remarks :

$$
G L _ {p} \times G L _ {q} \rightarrow G L _ {p + q}
$$

$$
(\alpha , \beta) \stackrel {\theta} {\mapsto} \left( \begin{array}{l l} \alpha & 0 \\ 0 & \beta \end{array} \right)
$$

Whitney sun

associative; commutative up to conjugacy.

$$
\left( \begin{array}{l l} 0 & 1 \\ 1 & 0 \end{array} \right) \left( \begin{array}{l l} \beta & 0 \\ 0 & \alpha \end{array} \right) \left( \begin{array}{l l} 0 & 1 \\ 1 & 0 \end{array} \right)
$$

⊕: induces products:

$$
H _ {x} (G L _ {p}) \approx H _ {x} (G L _ {b}) \xrightarrow {\mu_ {p q}} H _ {x} (G L _ {p + q})
$$

$M_{119}$

$$
H _ {x} (G L _ {p - q})
$$

$$
H _ {x} (G L _ {\rho \mu}) \otimes H _ {x} (G L _ {\beta}) \longrightarrow H _ {x} (G L _ {\rho + \varepsilon + 1}).
$$

Return to Theorem: (homology with coefficients in $\Lambda$.)

Proof: Reduce to case where  $\Lambda = F_{p}$ , Q.
(consider the category of zbelian gps for which them holds).

$0 \rightarrow  {\Lambda }^{\prime } \rightarrow  \Lambda  \rightarrow  {\Lambda }^{\prime \prime } \rightarrow  0$

1) If two are in C, so is the third. Use homology exact sequence  $\lim _{w \to \infty}$  preserves exactness and 5° Lemmz.

2) C is closed under filtered inductive limits.

Lemma: Any $C$ with properties (1) and (2) containing $F_p$, $Q$ must be all abelian groups.

Take any belief group $\Lambda : 0 \to t\Lambda \to \Lambda \to \Lambda / t\Lambda \to 0$

$0 \rightarrow \Lambda / t \Lambda \rightarrow \Lambda_{\frac{1}{2}} \oplus Q \rightarrow \text{tracing} g \rightarrow 0$

From now on  $H_{x}=H_{x}(-,\Lambda)$ ; A field. Itinneth formulaz:

$H_{x}(X) \otimes H_{x}(Y) \xrightarrow{\approx} H_{x}(X \times Y).$

Consequently for any space X;  $H_{*}(X)$  is a coalgebra coproduct induced by diagonal  $\Delta:X\to X*X$ .

$H_{x}(X) \xrightarrow{\Delta x} H_{x}(X) \times X \Rightarrow H_{x}(X) \otimes H_{x}(X).$

If X is connected;  $H_{0}(X)=\Lambda$ , so  $\exists$  distinguished generator of  $H_{0}(X)$  denoted 1.

Have algebra structures on  $H_{*}(GL)=\lim _{n\to\infty}H_{n}(GL_{n})$  induced

Easily seen that $\Delta: GL_{p} \rightarrow GL_{p} \times GL_{p}$ are compatible with $\oplus: GL_{p} \times G_{q}$$\rightarrow GL_{p+q}$, i.e.

$GL_{p} \times GL_{p} \times GL_{q} \times GL_{q} \longrightarrow GL_{p+q} \times GL_{p+q}$$\alpha \quad \beta \quad \gamma \quad \delta \quad \oplus \quad (\alpha + \gamma, \beta + \delta)$

Hence: $\Delta:H_{*}(GL)\longrightarrow H_{*}(GL\times GL)=H_{*}(GL)\otimes H_{*}(GL)$ is an algebra homomorphism $\therefore H_{*}(GL)$ is a Hopf algebra.

Define $\bot : G_{p} \times G_{q} \to G_{p+q}$$\begin{pmatrix} 1 & * \\ 0 & \alpha \end{pmatrix} \bot \begin{pmatrix} 1 & *' \\ 0 & \beta \end{pmatrix} = \begin{pmatrix} 1 & * & x' \\ & \alpha & \\ & & \beta \end{pmatrix}$

Check that this operation induces on these G-matrices induces an algebra structure on  $H_{x}(G_{\infty}) = \lim_{n \to \infty} H_{x}(G_{n})$ .  $G_{\infty} = \bigcup G_{n}$

∴  $p_{x}: H_{x}(G_{\infty}) \rightarrow H_{x}(GL_{0})$  is algebra homomorphism
∴  $s_{x}: H_{x}(GL_{0}) \rightarrow H_{x}(G_{\infty})$  “”

Hence  $p_{x} \cdot s_{x} = 1$  want  $s_{x} \cdot p_{x} = 1_{H_{x}(Gw)}$ 

Lemma:  $\begin{pmatrix} 1 & 4 \\ 0 & \alpha \end{pmatrix} \perp \begin{pmatrix} 1 & 4 \\ 0 & \alpha \end{pmatrix}$  is conjugate to  $\begin{pmatrix} 1 & 4 \\ 0 & \alpha \end{pmatrix} \perp \begin{pmatrix} 1 & 0 \\ 0 & \alpha \end{pmatrix}$ .

$$
\left( \begin{array}{c c c} 1 & u & y \\ 0 & \alpha & 0 \\ 0 & 0 & \alpha \end{array} \right) = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & - 1 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c c c} 1 & u & 0 \\ 0 & \alpha & 0 \\ 0 & 0 & \alpha \end{array} \right) \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right)
$$

$G_{p} \xrightarrow{\Delta} G_{p} \times G_{p} \xrightarrow{1 \times 1} G_{p} \times G_{p} \xrightarrow{\oplus} G_{2p}$

Lemma shows these two homomorphisms are conjugate, so:

$H_{*}(G_{p}) \xrightarrow{\Delta_{*}} H_{*}(G_{p} \times G_{p}) \approx H_{*}(G_{p}) \otimes H_{*}(G_{p}) \underset{\substack{i d \otimes s \cdot p. \\ i d \otimes s \cdot p.}}{\overset{i d \otimes i d}{\Rightarrow}} H_{*}(G_{p}) \otimes H_{*}(G_{p})$$y \downarrow \text{product}$$H_{*}(G_{2p}).$

are the same maps. Take limit, replace p by ∞.

Now we can prove $s_x \cdot p_x = 1$ on $H_n(G_\infty)$ by induction on $n$. Assume true for degrees $< n_j$; let $x \in H_n(G_\infty)$

$\Delta_{x}x=1\otimes x+\sum_{\deg(x_{i}^{\prime})<n}x_{i}^{\prime}\otimes x_{i}^{\prime\prime}$

$y(id \otimes id)(\Delta_x x) = x + \sum_{deg(x_i') < n} x_i' \cdot x_i'' \in H_x(G_\infty).$

$M(id \otimes s_x \cdot p_x)(\Delta_x x) = s_x p_x x + \sum_{\text{def}(x) < n} x_i' s_p x_i''$

$\sum  = \sum$ , so  $x = S_{x} p_{x} x$ , complete induction. QED

General fact about Hopf algebras: If C is a  $\overline{Hopf}$  toalgebra and A is an algebra, one can make  $\operatorname{Hom}(C,A)$  into a monoid.

Given $u, v: C \Rightarrow A$ define convolution

$u*v: C \xrightarrow{\Delta} C \otimes C \xrightarrow{u \otimes v} A \otimes A \xrightarrow{u} A$

If C is connected, then the algebra C has an inversion, so this monoid is a group.

id \* id = id \* s \* p. if group can cancel

$$
\text { Let } B = \left\{\left( \begin{array}{l l} a & b \\ o & d \end{array} \right) \in M _ {2} A \right\}. = \left( \begin{array}{l l} A & A \\ A & \end{array} \right).\tag{39}
$$

$$
G L _ {0} B = \left( \begin{array}{c c c c} \cdot & \cdot & \cdot & \cdot \\ \hline \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot \end{array} \right)
$$

$$
\text { conjugate   get } \left(- \frac {\vdots}{1 : :}\right)
$$

$$
G L _ {n} B \simeq \left(\frac {G L _ {A} \mid A M _ {n} A}{\mid G L _ {A}}\right)
$$

Assertion: ${K}_{n}B \cong  {K}_{n}A \oplus  {K}_{n}A.$

$$
H _ {*} \left( \begin{array}{c c} G L _ {r} & M _ {n} \\ O & G L _ {n} \end{array} \right) \longleftarrow H _ {*} \left( \begin{array}{c c} G L _ {r} & 0 \\ O & G L _ {n} \end{array} \right)
$$

induced by inclusion is isomorphism, in the limit as  $n \to \infty$ .

Proof:

$$
1 \rightarrow G _ {n} \rightarrow \left(\begin{array}{c c}G L _ {r}&M _ {n}\\&G L _ {r}\end{array}\right)\rightarrow G L _ {r} \rightarrow 1
$$

$$
\Phi \rightarrow G L _ {n} \rightarrow \left(\begin{array}{c c}G L _ {r}&0\\0&G L _ {n}\end{array}\right)\rightarrow G L _ {r} \rightarrow 1
$$

Write down group cohomology spectral sequence:

$$
E _ {p q} ^ {2} = H _ {p} (G L _ {r}, H _ {q} (G _ {n})) \Rightarrow H _ {*} (U _ {n} | ^ {T L _ {r} M _ {n}} G L)
$$

$$
E _ {p q} ^ {2} = H _ {p} (G L _ {r}, H _ {q} (G L _ {n}) \Rightarrow H _ {*} (0, 0, G L _ {n})
$$

limits precise
exadness.

isomorphism desired, by Comparison Thm.

Corollary: Now let  $r \to \infty$ .  $H_{*}\left(\bigcup_{r,n}\begin{pmatrix} GL_{n} & M_{rn} \\ & GL_{n} \end{pmatrix}\right) \approx H_{*}\left(\begin{array}{cc} GL & 0 \\ 0 & GL \end{array}\right)$ .

Thus we obtain embedding:  $\left(\begin{array}{cc}A & 0 \\ 0 & A\end{array}\right) \subset \left(\begin{array}{cc}A & A \\ 0 & A\end{array}\right) = B$  inducero isc.

![](images/page_39_image_0.jpg)

of  $H_{*}(GL(A \times A))$  with  $H_{*}(GL(B))$ .

$BGL(A \times A)^{+} \longrightarrow BGL(B)^{+}$ is a map of H spaces $(\Rightarrow \text{simple})$ which is a homology isomorphism, hence a homotopy equivalence. QED. for assertion.

A, r fixed

$$
H _ {x} \left( \begin{array}{l l} 1 & 0 \\ 0 & G L _ {n} A \end{array} \right) \subset H _ {y} \left( \begin{array}{l l} 1 & M _ {m} A \\ 0 & G L _ {n} A \end{array} \right)
$$

$$
H _ {*} \left( \begin{array}{c c} G L _ {r} A & 0 \\ 0 & G L _ {o} A \end{array} \right) \longrightarrow H _ {*} \left( \begin{array}{c c} G L _ {r} A & M _ {r n} A \\ 0 & G L _ {n} A \end{array} \right)
$$

$$
H _ {*} \left( \begin{array}{c c} G L _ {r} A & 0 \\ 0 & G L (A) \end{array} \right) H _ {*} \left( \begin{array}{c c} G L _ {r} A & G N _ {r, \infty} A \\ 0 & G L (A) \end{array} \right)
$$

Corollary  $K_{*}\begin{pmatrix} A & 0 \\ 0 & A \end{pmatrix} \rightarrow K_{*}\begin{pmatrix} A & A \\ 0 & A \end{pmatrix}$

$$
K _ {*} A \oplus K _ {*} (A).
$$

$$
G L _ {n} \left( \begin{array}{l l} A & A \\ 0 & A \end{array} \right) \simeq \left( \begin{array}{l l} G L _ {n} A & M _ {n n} A \\ O & G L _ {n} A \end{array} \right)
$$

Swan's counterexample:

Recall Milnor's Theorem: If  $D \xrightarrow{f'} C$  is a cartesian (pullback)
 $g \downarrow \quad \downarrow g$$A \xrightarrow{f} B$

square of rings and if either f or g is epic we have a Mayer-Vietoris sequence.

$K_{1}D \rightarrow K_{1}A \oplus K_{1}C \rightarrow K_{1}\beta \xrightarrow{\partial} K_{0}D \rightarrow K_{0}A \oplus K_{0}C \rightarrow K_{0}$

If both fig are epic then: can write in the $K_{2}$ terms.

$K_{2}D \rightarrow K_{2}A \oplus K_{2}C \rightarrow K_{2}\beta \xrightarrow{\partial} K_{1}D$:

Swan's Theorem: $2^{nd}$ conclusion is false if only one is surjective. There is no functor $\overline{H_2}$ s.t. for every cartesian square with g (split epic) surjective one has:

$$
\overline {{H}} _ {2} D \rightarrow \overline {{H}} _ {2} A \oplus \overline {{H}} _ {2} C \rightarrow \overline {{H}} _ {2} B \rightarrow K _ {1} D \rightarrow K _ {1} A \oplus K _ {1} C \rightarrow K _ {1}
$$

$A[\varepsilon] \xrightarrow{f'} \begin{pmatrix} 0 & A \\ A & A \end{pmatrix}$

$$
(H _ {1} = B a o o ^ {\prime} H _ {1})
$$

$$
g ^ {\prime} \downarrow \quad \downarrow g = \text { Projection }
$$

$$
A \xrightarrow [ \Delta ]{f} \left( \begin{array}{l l} A & 0 \\ 0 & A \end{array} \right)
$$

here  $A[E]=A+A\varepsilon$$\varepsilon^{2}=0$  = ring of dual numbers/A.
elts:  $a+b\varepsilon$$f'(a+b\varepsilon)=\begin{pmatrix}a&b\\o&a\end{pmatrix}.$$g'(a+b\varepsilon)=a$

Because $g$ has a section $\Rightarrow \overline{K_2}C \rightarrow \overline{K_2}B$, hence:

$$
0 \rightarrow K _ {1} (A [ \varepsilon ]) \rightarrow K _ {1} A \oplus K _ {1} \left(\begin{array}{l l}A&A\\0&A\end{array}\right)\rightarrow K _ {1} \left(\begin{array}{l l}A&0\\0&A\end{array}\right)\rightarrow 0.
$$

is exact:

$$
\Rightarrow K _ {1} (A [ \varepsilon ]) \underset {g ^ {\prime} *} {\sim} K _ {1} A. (t)
$$

Recall if A is commutative then  $H_{1}A \approx A^{*} \oplus k_{er}(det: A \to A)$$0 \rightarrow SK_{1}A \xrightarrow{def} A^{*} \rightarrow 0$

$$
A [ \varepsilon ] ^ {*} \simeq A ^ {*}.
$$

but this is false

$$
\text { Let } \rho : G \longrightarrow G L _ {n} A = A u t (A ^ {n}).
$$

$$
H _ {*} G \rightarrow H _ {*} G L _ {0} A \rightarrow H _ {*} G L (A).
$$

$$
G = \left( \begin{array}{l l} G L _ {r} & M _ {m} \\ 0 & G L _ {n} \end{array} \right) \xrightarrow [ j ]{i} G L _ {r + n}
$$

$$
g: \left( \begin{array}{l l} z & b \\ 0 & d \end{array} \right) \mapsto \left( \begin{array}{l l} x & b \\ 0 & d \end{array} \right)
$$

$$
j: \left( \begin{array}{l l} a & b \\ o & d \end{array} \right) \longmapsto \left( \begin{array}{l l} z & 0 \\ o & d \end{array} \right)
$$

$$
\text { Then } i _ {*} = j _ {*}: H _ {*} \left(\begin{array}{c c}G L _ {r}&M _ {r n}\\0&G L _ {n}\end{array}\right)\rightarrow H _ {*} (G L).
$$

Proof:

$$
\left( \begin{array}{c c} G L _ {r} & M _ {r n} \\ 0 & G L _ {n} \end{array} \right) \xrightarrow [ j ]{i} G L _ {r + n}
$$

$$
\left( \begin{array}{c c} G L _ {r} & M _ {\infty} \\ 0 & G L \end{array} \right) \xrightarrow [ j ]{i} \prod_ {G L _ {\infty}}
$$

enough to show $i_* = j_*$ as maps on bottom of square. But we know:

$$
H _ {x} \left( \begin{array}{c c} G L _ {r} & 0 \\ 0 & G L \end{array} \right) \stackrel {\sim} {\longrightarrow} H _ {x} \left( \begin{array}{c c} G L _ {r} & M _ {\infty} \\ 0 & G L \end{array} \right)
$$

$$
\text { and } i = j \text { on } \left( \begin{array}{l l} G L _ {r} & 0 \\ 0 & G L \end{array} \right)
$$

QED.

$$
\begin{array}{l} {\mathrm{Theorem:}} \\ {\mathrm{Then:}} \end{array} \quad F _ {q} = \mathrm{finitefieldwith} q = p ^ {d} \mathrm{elements,pazprime.} H _ {i} (G L (\overline {{F _ {q}}}), \mathbb {Z} / p \mathbb {Z}) = 0 \quad i \geqslant 1.
$$

43

Proof: Enough to show:  $GL_{n}(\mathbb{F}_{g}) \hookrightarrow GL(\mathbb{F}_{g})$  induces zero map on  $Z_{p}$ -homology. ∀n. Recall that  $H_{*}(P) \to H_{*}(G)$  if  $[G:P] \not\equiv 0 \pmod{p}$ , and Sylow p-sulgp of  $GL_{n}(\mathbb{F}_{g})$  is  $\begin{pmatrix} 1 & 1 & * \\ 0 & \cdots & 1 \end{pmatrix}$ .

Enough to show  $H_{*}\begin{pmatrix} 1 & * \\ 0 & 1 \end{pmatrix} \to H_{*}\begin{pmatrix} GL(\mathbb{F}_{g}) \\ \text{is zero map.} \end{pmatrix}$  x > 0

$\begin{array}{r} {T}_{n - 1}\left( \begin{array}{c:c:c} 1 & * &  \\  & \ddots &  \\  &  &  \\  &  &  \\  &  &  \\  &  &  \\  &  &  \\  &  &  \\  &  &  \\  &  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  & \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \\  &  \end{array} \right) \subseteq \left( \begin{array}{c:c:c} G L _ {n - 1} & * \\ \hdashline \vdots & G L _ {1} \\ \hdashline \end{array} \right)$$i\downarrow j$$i\downarrow j \gets$ these induce same map on $H_{*}$, by corollary.

$\text{Hom } (G, \text{Aut } (P))_{\text{Aut } (P)} = \text{iso classes of representations of}$$G \text{ on projectives } P \approx P_S. \quad (P \in \mathbb{R})$

Two representations $\rho, \rho'$ are equivalent if $\Theta \rho(g) \Theta^{-1} = \rho'(g)$.

$\text{Rep } (G, A) = \coprod_{s \in G} \text{Hom } (G, \text{Aut } (P_S))_{\text{Aut } (P_S)}.$

Goal: To any representation $E = (P, \rho)_{\text{of}} G$ I want a map (canonical).
$[E] : BG \rightarrow BGLA^{+}$.

(as based homotopy class of map).

$\rho: G \rightarrow \text{Aut}(P)$

$P \oplus Q \cong A^{n}$

$g \mapsto \rho(g) \oplus 1_{Q} \mapsto \in A_{ut}(A^{n}) = GL_{n}(A).$

Choosing $Q, \theta$ we get a homomorphism;

$BG \longrightarrow BGL_{n}A \longrightarrow BGLA \longrightarrow BGLA^{+}.$

\- Verify independent of choices, well-defined.

Point: $\pi, (BGL(A)^{+}) = \pi, A$ acts trivially on $BGL(A)^{+}$, because $BGLA^{+}$ is an H-space, hence simple.

Properties of: $\mathrm{Rep}(G;A) \rightarrow [\mathrm{BG}, \mathrm{BGL}(A^{+})]$$\mathrm{E} \mapsto [\mathrm{E}]$.

① If $T$ is a trivial representation, $\rho(g) = \frac{g}{2} d_p \forall g \in G.$
then, $T = (p, p)$

②  $[E] \oplus [E'] = [E \oplus E']$$0 - m \geq p$$+ = \text{operation on } [BG, BGLA^{+}]$ 

deduced from H-space structure of  $BG \perp LA^{+}$ .

③ If  $0 \rightarrow E' \rightarrow E \rightarrow E'' \rightarrow 0$  is a s.e.s. of representations.
then:

$[E]=[E']\oplus[E'].$

Proof of ②:

By adding trivial representations to $E', E''$ we can suppose underlying $A$-module of $E', E, E''$ are $\simeq A', A^9, A^{p+8}$.

$$
0 \rightarrow A ^ {p} \rightarrow A ^ {p + q} \rightarrow A ^ {q} \rightarrow 0.
$$

Can replace G by auto group of this exact sequences

i.e.  $G = \begin{pmatrix} GL_{q} & M_{gp} \\ O & \oplus L_{tp} \end{pmatrix}$  Have to show:

Enough to show  $[E]=[E'\oplus E'']$  assuming ②.

So we want:

$$
G = \left( \begin{array}{c c} G L _ {g} & M _ {g p} \\ 0 & G L _ {p + g} \end{array} \right) \xrightarrow [ j _ {2} E ^ {\prime} \oplus E ^ {\prime \prime} ]{i \leftrightarrow E} G L.
$$

that  $i_{*}=j_{*}:BG\rightarrow BGLA^{+}$ .
Enough to show:  $p\rightarrow\infty$$\begin{pmatrix} GL_{1}&M_{f\infty}\\ 0&GL_{\infty}\end{pmatrix}\xrightarrow{j}GL$ 
induce same map to:  $BGLA^{+}$

$$
\left( \begin{array}{c c} G L _ {q} & 0 \\ 0 & G L \end{array} \right)
$$

and we know that  $B\left(\begin{array}{c}GL_{8}\\GL\end{array}\right)\xrightarrow{\downarrow}B\left(\begin{array}{c}GL_{8}\\GL\end{array}\right)\Longrightarrow BGL(A)^{+}$

is homology iso.

Lemma: $X \xrightarrow{f} Y$ homology is $_0 \Rightarrow M$ H-space connected.  
$[X, M] \xrightarrow{\sim} [X, M].$

Proof:  $P_{uppe}:[X,M]\leftarrow[Y,M]\leftarrow[C_{s},M]\leftarrow[\Sigma X,M]\leftarrow.$

Show  $[C_{f}, M] = 0$ , but Cf is acyclic, so there are no non-trivial maps, by obstructing theory, to any space having no non-trivial

${K}_{0}A = {\pi }_{0}\left( {{BGL}{\left( A\right) }^{ + }}\right)$

Problem (vague): Describe elements of  $[X, BGL(A)^{+}]$  as some sort of geometric structures over X. (analogous to BPL etc).

$\widetilde{FU}(X) = [X, BU] = \xrightarrow{lim}[X, BU_n] =$  iso classes of n-dimensional complex vector bundles over
X = finite complex.

Attempt:  $X \xrightarrow{u} BGL_{n}(A)^{+}$ 

acyclic

 $X' \xrightarrow{v} BGL_{n}(A)$

u thus induces map $X' \to X$ acyclic together with an element of $[X', BGL_n(A)] = Hom(\pi, X', GL_n(A))$ If $X$ is finite complex, then:

$$
[ X, B G L (A) ^ {+} ] = \underline {{\lim}} [ X, B G L (A) ^ {+} ]
$$

Assertion: X finite. Then an element of  $[X, BGL(A)^{+}]$  gives rise to
 $X' \rightarrow X$  acyclic.
 $\pi_{1}X' \rightarrow GL_{n}A$ .

If you have  $X'\rightarrow X$  acyclic then,  $[X',BGL(A)^{+}]\cong[X,BGL(A)^{+}]$

Use the fact that $\pi_{1}(BGL(A)^{+})$ is obeying. & universal property of a cyclic maps. (on killing perfect subgp).

Conclusion: (For X finite) every pair  $(X'\xrightarrow{g}X,\pi,X'\to GL_{n}A)$ 
with g acidic determines an element of  $[X,BGL(A)^{+}]$ .
If finite every element of group is obtained this way.

Trouble - I don't know when two pairs give the same element of $[X, B \& L(A)^{+}]$. Case of $S^{n}$:

![](images/page_46_image_1.jpg)

This reduces to the question of when two homomorphisms $\pi, Y \to GL_N$ determine the same map as $[X, BGL(A)^+]$.

We have seen this is the case if $\alpha, \beta$ are Jordan-Hülder isomorphic. (This is the theorem: $0 \to E' \to E \to E' \to 0$ is s.e.s. of representations of $G \Rightarrow [E] = [E' \oplus E'] \in [BG, BG\&(A)^+]$.

Problem: converse.

ReczII Rep(G,A) =  $\frac{1}{s}$  Hom(G, Ant(Ps)) $_{Aut(Ps)}$ .

$R(G;A)=$  Gothendieck group of representations with:

$R'(G,A) = \text{langer Gothen dieck with relations:}$$\text{better notation:}$$R_{\oplus}(G,A). \quad [E' \oplus E"] = [E'] + [E'']. \quad \text{large we dmeet sume}$

= abelian group generated by Rep (G, A).

$$
R ^ {\prime} (G, A) \rightarrow R (G, A).
$$

$$
R ^ {\prime} (G, A) \xrightarrow [ t m i s t _ {a c t i o n} ]{f o r g e l} R ^ {\prime} (e, A) = H _ {0} A
$$

Gives splitting:

$$
R ^ {\prime} (G, A) = K _ {0} A \oplus \widetilde {R} ^ {\prime} (G, A)
$$

Similarly:

$$
R (G, A) = H _ {0} A \oplus \widetilde {R} (G, A).
$$

We have map:

$$
R e p (G, A) \rightarrow [ B G, B G L (A) ^ {+} ]
$$

$$
E \mapsto [ E ]
$$

① trivial repr. go to 0 ② $0 \to E' \to E \to E'' \to [E] = [E'] + LE''$

Lemma: M connected H-space. (\~CW complex). Then M has a homotopy inverse (so [X, M] is a group]).

$$
\begin{array}{r l} {p r _ {1}} & {\downarrow \quad \downarrow p r _ {2}} \\ {M} & {= M} \end{array}
$$

since h.equiv on fibre and base space

g is a map of fibrations, so by long exact homotopy sequence: g is weak homotopy equivalence  $\Rightarrow$  g hom. eg

$$
g _ {x} ^ {:} [ X, M ] [ X, M ] \longrightarrow [ X, M ] \times [ X, M ] \quad \text { gives   inverse. }
$$

By universal property of $R(G,A)$ we get:

$$
\overline {{R}} (G, A) = R (G, A) / \pi_ {0} A \leftrightarrow R (G, A) \rightarrow [ B G, B G L (A) ^ {+} ]
$$

$$
X \rightarrow B \pi_ {i} (X).
$$

$$
\begin{array}{r l} {\overline {{{R}}} (\pi , X, A)} & {\xrightarrow {n \star} [ B \pi , X, B G L (A) ^ {+} ]} \\ & {\to [ X, B G L (A) ^ {+} ]} \end{array}
$$

Then any natural transformation:  $h: \overline{R}(\pi, X, A) \to [X, Z]$  with Z having no non-trivial perfect subgroup of  $\pi, Z$ , extends uniquely to a net. trans:

$\tilde{f}_{h}:\ [X,BGL(A)^{+}]\rightarrow [X,Z].$

Example. $\lambda$-ring structure on $\overline{R}(\pi, X, A)$ induces operations.

$[X, BGL(A)^{+}] \longrightarrow [X, BGL(A)^{+}]$.

A representation of $\pi X$ over $A$ may be identified with a fibre bundle with fibre, a $P$ in $\mathcal{P}_A$.

## Theorems as above

Let $X$ range over the category of pointed finite complexes, morphism are homotopy classes of base point preserving maps.

Consider a natural transformation $r: F(\underline{?}) \to G(\underline{?})$ to leti. Say $r$ has property (\*) if:

$F(X) \xrightarrow{\alpha} [X, Z]$

where $Z$ is a space $r.t. \pi, Z$ has no nontrivial perfect subgroups, then;

$F(X) \xrightarrow{\alpha} [X, Z]$$r(x) \downarrow$$G(X)$$\exists! e.$

Theorem: The canonical natural transformation

$$
[ X, B G L (A) ] \rightarrow [ X, B G L (A) ^ {+} ]
$$

has property (\*).

Proof: Fact: If Y is a CW complex and  $F_{\alpha} \subseteq Y, \alpha \in J$  is a directed system of finite subcomplexes st.  $UF_{\alpha} = Y,$  then;

$$
[ X, Y ] \xleftarrow {\approx} \lim _ {\vec {v}} [ X, F _ {a} ]. \quad X \text {   finite   ,   image   caught   up   in   some   } P
$$

Take $F_0$ to be the z-skeleton of $B\Omega_5 \subseteq B\&L_s(A)$. By choosing $B\Omega_5$ suitably (Milner model), obtain finite com,

$$
\pi_ {1} (F _ {0}) = \pi_ {1} (B O I _ {5}) = O I _ {5} \quad \text {   perfect   group.   }
$$

By attaching a single $2$ & 3-cell to $F_0$. We obtain $F_0 \hookrightarrow F_0^+$. (go over proof). Form:

$$
B G L A \cup_ {F _ {0}} F _ {0} ^ {+} = B G L (A) ^ {+}
$$

![](images/page_49_image_9.jpg)

$$
\begin{array}{c} V _ {2 n} \text { Hanpen: } \\ \Pi_ {1} (B G L (A) \cup F _ {0} ^ {+}) = G L (A) / n a m o l s u k \\ g n b y - U I _ {S}. \\ \downarrow \\ t h i e i s E (A) \end{array}
$$

Because it contains $\mathcal{M}_{\text{in}}$ hence given matrices $\alpha, \beta \in GL(A)$ mod this normal subgp, $\alpha, \beta$ commute.

Now with  $Y = BGL(A)$ , take  $F_{\alpha} = all$  finite sub complexes of Y containing  $F_{0}$ .

$$
B G L (A) = U F _ {\alpha}.
$$

$$
\Rightarrow [ X, B G L (A) ] = \lim _ {\rightarrow} [ X, F _ {\alpha} ]
$$

$$
\begin{array}{r l} {\mathrm{Nat.Trans.} ([ X, B G L (A) ^ {+} ], \overline {{F}} (X)) =} & {\underset {\alpha} {\lim} N _ {\mathrm{it}} \mathrm{Transf} ([ X, F _ {\alpha} ], T)} \\ & {= \underset {\alpha} {\lim} T (F _ {\alpha}). \quad Y _ {\mathrm{onedz'sLemma.}}} \end{array}
$$

$$
\text { similarly } \quad \text { Not   Trans. } ([ X, B G L (A) ^ {+} ], T (X)) = \underbrace {\lim _ {n \to \infty} T (F _ {n} \cup F _ {0} ^ {+})}.
$$

$$
N _ {\mathrm{at.}} T r e n s. \left([ X, B G L (A) ^ {+} ], [ X, z ]\right) = \lim _ {\downarrow} \left[ F _ {\alpha} \cup F _ {0} ^ {+}, z \right].
$$

$$
N _ {\mathrm{at.}} T r a n s ([ X, B G L (A) ]. [ X, Z ]) = \lim _ {z \to 0} [ F _ {x}, Z ].
$$

We know $\pi_1(Z)$ has no nontrivial perfect subgroups. $\Rightarrow$

$$
[ F _ {\alpha}, z ] \leftarrow [ F _ {\alpha} \cup_ {F _ {0}} F _ {0} ^ {+}, z ].
$$

$$
\begin{array}{l} \text { by. } \quad \alpha \text { cyclicity } _ {2} f \text { map } \\ F _ {\alpha} \longrightarrow F _ {\alpha} \cup F _ {0} ^ {+}. \end{array}
$$

We assume finite CW complexes since now:

$$
\begin{array}{r l} {X \cdot \mathrm{finite}} & {\Rightarrow \pi_ {1} X \quad \mathrm{fin.~gen.~gp.} \quad [ X, B G L (A) ] = H _ {\mathrm{om}} (\pi_ {1} X, G L (A))} \\ & {\qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \mathrm{Imj.} H _ {\mathrm{om}} (\pi_ {1} X, G L _ {0}, A).} \end{array}
$$

$$
\begin{array}{l} {R ^ {\prime} (\pi , X, A) \longrightarrow R (\pi , X, A)} \\ {\mathrm{abeliangroupgeneratedbythemonoidofisoclassesofrep.of}} \\ {\pi , X \quad \mathrm{in} \quad \wp (A)} \end{array}
$$

$$
\widetilde {R} ^ {\prime} (\pi , X; A) = \widetilde {R} ^ {\prime} (X, A) / R ^ {\prime} (e, A) = 5 a.
$$

Exercise: Show  $\widetilde{R}^{\prime}(\pi,X,A)=\text{abelion group generated by the monoid}$$\xrightarrow{\lim }\frac{\operatorname{Hom}(\pi,X,\text{GL}_{n}A)}{130\text{ classes of rep. of }\pi,X\text{ on }A^{n}}$

$$
\lim _ {x \to 0} [ f _ {m} (\pi , X, G L _ {n} A) = [ X, B G L (A) ] \longrightarrow [ X, B G L (A) ^ {+} ]
$$

⊕  $\tilde{R}^{\prime}(\pi, X, A)^{-}$

$\therefore \rightarrow$$\Rightarrow$$\widetilde{R}^{*}(\pi,X,A)$$\downarrow$ 
O

Theorem: $f_{n}, f_{k}$ here property (\*)

Suffices to show it for $f_{0}$, by diagram chasing.

Fact. Suppose M is an abelian monoid,  $\overline{M}$  = abelian group gen by M. Grothendieck construction:

$M \times M \times M \xrightarrow{2} M \times M \rightarrow \overline{M}^{a,b}$

$$
(m _ {1}, m _ {2}, m _ {3}) \underset {b} {\overset {a} {\rightleftarrows}} (m _ {1} + m _ {2}, m _ {3} + m _ {2}) (m _ {1 1}, m _ {2}) m _ {2} + m _ {3}
$$

$$
(m _ {1} ^ {\prime}, m _ {2} ^ {\prime}) \sim (m _ {1}, m _ {2}) \leftrightarrow 3 t s t. \quad m _ {1} ^ {\prime} + m _ {2} + t = m _ {2} ^ {\prime} + m _ {1} + t.
$$

exact means: given $\varphi: M \times M \to S$$\varphi_{a} = \varphi_{b}$ then $\varphi$ factors uniquely thru $M$.

$$
M \times M \times M \xrightarrow [ b ]{a} M \times M \longrightarrow \overline {{M}}
$$

Proof that $h$ satisfies (x).

$M(X)^{\frac{3}{b}} \Rightarrow M(X)^{2} \rightarrow \widetilde{R}'(x, X; A)$$u \downarrow \quad v \downarrow \quad \downarrow$

N.T.

$[X, BGL(A)^{+}]^{3} \Rightarrow [X, BGL(A)^{+}]^{2} \rightarrow [X, BGL(A)^{+}]^{-1} \rightarrow [X, Z]^{-1}$

Both rows exact.
u,v have property. (\*) (apply previous thm to A×A, A×A×A)
Cor from above:  $\prod_{i=1}^{n}[X,BGL(A_{i})]\rightarrow\prod_{i=1}^{k}[X,BGL(A_{i})^{+}]$

$\widetilde{H}(X,A)=[X,BG[(A)^{+}]}$  analogous to  $\widetilde{H}(X)=[X,BU]$

① A  $\xrightarrow{u}$  B ring-homomorphism:

$u^{*}: P_{A} \longrightarrow P_{B}$. $u^{*}(P) = P_{A} \times B$. also,

$\widetilde{R}(\pi,X,A) \longrightarrow \widetilde{R}(\pi,X,B).$$\downarrow$$\widetilde{K}(X;A) \longrightarrow \widetilde{K}(X;B)$

$A \mapsto \widetilde{K}(X, A)$ is covariant functor. $\text{Rung} \to \mathcal{A}(t,$

② transfer:  $u:A \rightarrow B$  is a ring homomorphism st.  $B \in f_{A}^{n}$ 

Then one has "restriction of scalders"

 $u_{1}: f_{B} \rightarrow f_{A}$ .  $u_{x}(Q) = Q|_{A}$ .

You: get  $\widetilde{R}(\pi,X,B)\longrightarrow\widetilde{R}(\pi,X,A)$$\downarrow$$\widetilde{K}(X,B)\dashrightarrow\widetilde{F}(X;A)$

In particular:  $X = S^{n}$ :  $u_{*}: K_{n}B \rightarrow K_{n}A$ .

③ Products:  $\pi_{0}A \otimes \widetilde{\pi}(X;A) \rightarrow \widetilde{\pi}(X;A)$ , A commutative.
Proposition: (Projection, formula): Suppose  $u:A \rightarrow B$  as in (2), then:
 $u_{*}u^{*}:\widetilde{\pi}(X,A)\rightarrow\widetilde{\pi}(X,A).$  Forget this.

Remark: If B has a finite projective resolution.

$0 \rightarrow P_{x} \rightarrow \ldots \rightarrow P_{y} \rightarrow P_{0} \rightarrow B \rightarrow 0$ with $P_{i} \in X_{n}^{*}$

then one can define $z$ transfer. $\widetilde{H}_{\mathrm{X}}(\mathrm{B}) \longrightarrow \widetilde{H}_{\mathrm{A}}(X,A)$. (using other methods).

③ Products again:  $\gamma_{A} \times \gamma_{B} \longrightarrow \gamma_{A \otimes B}$$(P, Q) \longmapsto P \otimes Q$

$R(\pi, X, A) \otimes R(\pi, X, B) \longrightarrow R(\pi, X, A \otimes B).$$[E], [F] \mapsto [E \otimes F].$

Let $E: R(\pi, X, A) \to |\tau_0 A|$. The map to underlying modules with trivial actions.

Then: $\widetilde{R}(\pi, X; A) \otimes \widetilde{R}(\pi, X, B) \to \widetilde{R}(\pi, X, A \otimes B)$.

$[EH-[E]$ typic element. $(|E-|E|)\&(|F-|F)|)=[EQF]-|E|C(f=)-|EF|E!+CEO.$

$(E)^{-\varepsilon^{E}}$, $[F]^{-\varepsilon^{F}}$ → $[E \otimes F] - [E \otimes \varepsilon F] - [\varepsilon E \otimes F] + [\varepsilon E \otimes \varepsilon F]$. (\*)

Thus by sending a representation $E$ of $\pi_X$ over $X$ end a rep.
$F$ of $\pi_X$ over $B$ to above (x)
one gets a (representation) natural transformations

$\widetilde{R}(\pi,X,A)\otimes\widetilde{R},(\pi,X,B)\rightarrow\widetilde{R}(X,A\otimes B)$

$\widetilde{F}(X,A)\times\widetilde{F}(X,B)--\frac{1}{4}\rightarrow\widetilde{F}(X;A\otimes B)$

Properties of $y$:

Lemma ① $\mu$ is bilenear, associative, commutative.
② Proof: $\mu(\alpha+\beta,\sigma)=\mu(\alpha,\sigma)+\mu(\beta,\sigma).$

$\widetilde{K}(X,A)^{2}\times\widetilde{\Pi}(X,B)\Longrightarrow\widetilde{H}(X,A\otimes B)$

$\widetilde{R}(\pi,X,A)\times\widetilde{R}(\pi,X,B)\Rightarrow\widetilde{R}(\pi,X,A)\otimes B$

Because for $\widetilde{R}$ onches $(\alpha+\beta)\gamma=\alpha\sigma+\beta\gamma$. Then some holds for $\widetilde{R}$ by uniqueness part of theorem.

associativity: $\widetilde{H}(A,A)\times\widetilde{H}(X,B)\times\widetilde{H}(X,C)\Rightarrow\widetilde{H}(X,A\otimes B\otimes C)$$\widetilde{H}(X;B)\times\widetilde{H}(X,A)\rightarrow\widetilde{H}(X,B\otimes A)$$\widetilde{H}(X,A)\times\widetilde{H}(X,B)=\widetilde{H}(X,A\otimes B)$

Can also define products:  $\widetilde{r}_{b}A\otimes\widetilde{r}(x,B)\rightarrow\widetilde{r}(x,A\otimes B)$$\widetilde{r}(x,A)\otimes\widetilde{r}(B)\rightarrow\widetilde{r}(x,A\otimes B)$

so that putting:  $H(X,A)=H_{0}A\times\overline{F}(X,A)$ 

one gets produce:  $H(X,A)\times H(X,B)\rightarrow H(X,A)\otimes B$ .

which are associative, commutative, unitary.

Take $A$ to be commutative, so we have $A \oplus A \xrightarrow{\cdot} A$, then $\widetilde{F}(X, A)$ is commutative ring and $\widetilde{F}(X, A)$ is an ideal in $\widetilde{F}(X, A)$.

Products in H-groups.

$\widetilde{H}(r^{2})$$\leftarrow \widetilde{H}(X,A)$$\times$$\widetilde{H}(Y,B)$

$\widetilde{\Pi}(X \times Y, A) \times \widetilde{\Pi}(X \times Y - B)$$pr_{i}^{*}(x) \downarrow$$pr_{i}^{*}(y)$

$\widetilde{F}(pt \times Y, A \otimes B) \longleftarrow \widetilde{F}(X \times Y, A \otimes B) = M(pr_{1}^{*}x, pr_{2}^{*}y)_{2}$

$y(pr,x,pr,y) \cdot dies \ o, x,y \ and \ x*x* \ on \ XxY, X\vee Y$

In general.

general.
0 → [X ∧ Y, Z] → [X × Y, Z] → [X ∨ Y, Z] → 0
for H-space Z.
split by ... [X, Z], × [Y, Z].

Conclude $M(pr_{1}^{*}x, pr_{2}^{*}y) \in \widetilde{F}\Gamma(X \cap Y, A \otimes B)$$= \text{subsp of } \sum_{\substack{dying on X \times pt \sim pt \times)}} \widetilde{F}(X \times Y, A \otimes B)$

So one gets natural transformation:
$\widetilde{F}(X,A) \propto \widetilde{F}(Y,B) \rightarrow \widetilde{F}(X \cap Y, A \cap B)$
Size $X = Y^{2}$, $Y = S^{2}$, $X \cap Y = S^{2\text{时}}$ and set $H, A \cup F_{3} = 1$.

Exercise: extend this to p or q = 0. of check following properties:
① associative ② commutative.

A commutative  $\Rightarrow$  Kx A graded anticommutative king.

$\lambda$-operations and Adams operations in $K_{x}A$.

Suppose A commutative.

Recell (Atiyoh: "H-Theory"):

$$
K (X) = [ X, \mathbb {Z} \times B U ]
$$

one proves this operation
induces on bundles operations

$$
\lambda^ {k}: \Pi (X) \rightarrow \Pi (X)
$$

satisfying: let t be indeterminate.  $\lambda_{t}x=1+(\lambda x)t+(\lambda^{2}x)t^{2}+eK(X)[[t]]$

$$
\Rightarrow ① \lambda_ {t} (x + y) = \lambda_ {t} (x), \lambda_ {t} (y).
$$

$$
\lambda^ {k} (x y) = P _ {k} (\lambda^ {\prime} x, \dots , \lambda^ {k} x, \lambda^ {\prime} y, \dots , \lambda^ {k} y).
$$

$$
③ \cdot \lambda^ {k} \lambda^ {l} (x) = P _ {1 3, k} (\lambda^ {\prime} x, \dots)
$$

$$
\text { this   is   a   ring. }
$$

Adams $\psi$-operations!

$$
\lambda_ {t} (L) = 1 + t L
$$

$$
L \text { line   bundle }
$$

$$
s o \lambda_ {t} (L) = 1 - t L
$$

$$
\ln \left(\frac {1}{1 - t L}\right)
$$

$$
= t L + \frac {t ^ {2} L ^ {2}}{2} + \frac {t ^ {3} L ^ {3}}{5}
$$

$$
\frac {1}{\lambda_ {- t} (L)} = \frac {1}{1 - t L}
$$

$$
- \ln (\lambda_ {- t} (L)) = t L + \frac {t ^ {2} L ^ {2}}{2} + \dots
$$

$t \frac{d}{dt} \left( \frac{1}{\lambda_{t}(L)} \right) = t L + t^{2} L^{2} + t^{3} L^{3} + \ldots$

$$
P _ {u t} \sum_ {k \geq 1} t ^ {k} \psi^ {k} x = t \frac {d}{d t} \ln \left(\frac {i}{\lambda_ {- t} (x)}\right)
$$

$\Psi^{p}=id$  by convention

Identities: (i) $\psi^{h}(x+y)=\psi^{h}(x)+\Psi^{-h}y$

(ii)  $\psi^{k}(xy) = \psi^{k}(x)\cdot\psi^{k}(y).$

(iii)  $\Psi_{0}^{k}\Psi^{l}(x)=\Psi^{k l}(x).$

Theorem: On $\tilde{K}(X,A)$ one has Adams operations, A commicatio satisfying (i)-(ii)

$x \in V^{n}$  if  $x \in \widetilde{H}(X, A) \otimes \mathbb{Q}$$\Psi^{k}x = k^{n}x$$\forall k \geq 1.$

topological analogue: $\widetilde{H}(X) \otimes \mathbb{Q} = \bigoplus_{n \geq 1} H^{2n}(X, \mathbb{Q})$

?algebraic J-groups,

$A = \text{commutative ring. } \otimes, \Lambda^{k}.$

$R(G,A)$ is a commutative ring with identity with $\lambda^{k}: R(G,A) \rightarrow R(G,A)$.

$$
① \begin{array}{r l} {\lambda_ {t} (x + y)} & {= \lambda_ {t} (x) \cdot \lambda_ {t} (y)} \\ {\lambda_ {t} (0)} & {= 1} \end{array}
$$

$$
\lambda_ {k} (x) = \sum_ {k \geq 0} \lambda^ {k} (x) t _ {k} ^ {k}
$$

$$
② \lambda^ {k} (x y) = P _ {n} (\lambda^ {1} x, \lambda^ {k} x, \lambda^ {1} y, \dots , \lambda^ {k} y)
$$

$x^{j} \lambda^{k}(x) = Q_{jk} (\lambda'_{x}, \ldots, \lambda^{jk})$$L \quad 1-dimensional \quad \lambda_{t}(L) = 1 + t[L]$

Procedure for calculating $P_{k} \quad X_{1}, \ldots, X_{n}, Y_{1}, \ldots, Y_{m}$.

②  $\lambda^{k}(xy) \leftrightarrow k^{th}$  elementary symmetric function of  $X_{i} \times Y_{j}$ . In a vector

 $1 \leq i \leq n, \quad 1 \leq j \leq m.$$= P_{k}$  (elem. sym. ftns of  $X_{i}$ , elem. sym. ftns of  $Y_{i}$ )

 $P_{k}(\lambda'_{x}, \lambda'_{x}, \lambda'_{y}, \lambda'_{y}) \leftrightarrow P_{k}$

$x^{k}(x) \leftrightarrow k^{th}$  elementary symmetric function of  $X_{i}'$$\sum X_{i}, \ldots, X_{i_{k}}$$1 \leq i, < \ldots < i_{n} \leq n.$

Take $j^{th}$ symmetric function of $X_{i_1} \ldots X_{i_k}$ is $i_1 < \ldots < i_k \leq 1$. and write it as a polynomial in the element $\text{sym. Functions of } X_i$. $Q_{j,k}$ (elem-sym., functions of $X_i$)

$Q_{j,k}(\lambda^{\prime}x,\ldots,\lambda^{ik}x)$

Adams operations $\Psi^{k}: R(G,A) \to R(G,A)$.

$\frac{1}{2}$ )  $\Psi$  is a ring homomorphism
③  $\psi^{k}(\psi^{\prime}x) = \psi^{\prime kj}$

④  $\psi^{R}l = l \otimes \ldots \otimes l^{-}$$d_{i}=l=1.$

Fact: If $A$ is of characteristic $p$, then $\exists$ Frobenius endomorphism of $A$: $F_a = 2^p$, which induces map $F$ on $R(G, A)$. Assection: $\Psi^i P = F_1$ on $R(G, A)$.

$$
x _ {1} ^ {2} + x _ {2} ^ {2} =
$$

$p=2$$\Psi^{2}x=x^{2}-2\lambda^{2}x.$$0\rightarrow\Lambda^{2}P\rightarrow P\otimes P\rightarrow S^{2}P\rightarrow0$

$0 \rightarrow K \rightarrow S^{2}P \rightarrow \Lambda^{2}P \rightarrow 0$$<p, p_{1}>$$F(P)$$<p, p_{2}> \mapsto p_{1} \cap p_{2}.$

$E = L_1 + \ldots + L_n.$ want $r_k(E - n) = k^{\pm n}$ even symmetric for $L_i - 1$.  
want $r_t^*(E - n) = \prod (1 + t(L_i - 1)).$$r_t = \sum r^n t^n.$

$$
\begin{array}{l l} {\mathrm{want}} & {x _ {t} \quad \mathrm{to~satisfy:}} \\ & {\quad x _ {t} (x + y) - x _ {t} (x) \cdot x _ {t} (y)} \\ & {\quad x _ {t} (L - 1) = 1 + t (L - 1) = (1 - t) + t L.} \\ & {\quad \mathrm{II}} \\ & {\quad x _ {t} (L) / x _ {t} (1).} \end{array}
$$

$$
\begin{array}{r l} {r _ {t} (L)} & {= (1 - t + t L) r _ {t} (1). \quad r _ {t} (1) = \frac {1}{1 - t}} \\ & {= 1 + (\frac {t}{1 - t}) L.} \\ & {= \frac {\lambda_ {t}}{(- t)} L. \quad \Rightarrow : D _ {2 f}: \quad r _ {t} x = \lambda_ {(\frac {t}{1 - t})} (x).} \end{array}
$$

$r$-filtration:

$$
F _ {p} ^ {x} (R (G; A)) = \operatorname * {s u b g p} _ {i _ {1} + \dots + i _ {n}} x ^ {i _ {1}} (x _ {1}) \dots x ^ {i _ {n}} (x _ {n})
$$

$$
\text { Fact: } \quad O _ {n} \quad F _ {i} ^ {r} / F _ {i + 1} ^ {r} \text { one   has } \quad \psi^ {k} = k ^ {i}.
$$

Fact: In a 2-ring one has:

$\Psi^{p}$ Atiyab's book

Theorem: X finite complex. On $\tilde{F}(X,A)$, the x-filtration is locally illpote
i.e. $\forall x \in \tilde{F}(X,A)$, $\exists N_x$ s.t. $x^{i'}(x) \ldots x''(x) = 0 \quad i_1 + \ldots + i_r \geq N$.

Corollary: For any  $x \in \tilde{H}(X; A)$ ,  $k \geq 1$ :  $\exists N$  s.t.:

$(\Psi^{\underline{k}}-1)(\Psi^{\underline{k}}-\underline{k})\ldots(\Psi^{\underline{k}}-\underline{k}^{N})x=0.$

∃ formula for  $(\psi^{-1})\ldots(\psi^{k}-k^{N})$  (in terms of  $\gamma^{i}$ 's of high weight)
in terms of  $P(\gamma^{1},\ldots,\gamma^{-k})$ , involves monomials of weight  $\geq N$ .

$\mathrm{Pf:}\quad\Psi^{\prime\prime}.\quad\text{is an automorphism on}\quad\tilde{F}(X,A)\quad\text{(because}\quad\Psi^{\prime\prime}=F_{n\times b.}$

Lemma: If $A$ is an abelian $gp$ with auto, $\Psi$ satisfying:  
$A = \bigcup_{n} \ker (\Psi - p) \ldots (\Psi - p^n)$ then $p: A \stackrel{\sim}{\to} A$$X_n = \ker (\Psi - p) \ldots (\Psi - p^n)$ seem to need:  
$A^{\Psi} \xrightarrow{\approx} A^{\Psi}$

$0 \rightarrow X_{n-1} \rightarrow X_n \rightarrow X_n / X_{n-1} \rightarrow 0$$2 \downarrow \Psi \quad 2 \downarrow \Psi \quad 2 \downarrow \Psi = P^n$$0 \rightarrow X_{n-1}^{n-1} \rightarrow X_n \rightarrow X_n / X_{n-1} \rightarrow 0$

$$
x \in \tilde {K} (X, A) = \underline {{\mathrm{li}}} [ X B G L _ {R} (A) ^ {+} ]
$$

$$
\text { say } x \in [ X, B G L _ {n} (A) ^ {+} ]
$$

$$
\begin{array}{l} {\lambda^ {k} (x + n) = 0 \quad k > n.} \\ {\mathrm{proofnexttime}.} \end{array}
$$

$$
\begin{array}{l l} {\log \left(\frac {1}{\lambda - t (x)}\right) = \sum_ {m \geq 1} \psi^ {m} (x)   \frac {t ^ {n}}{m}.} \\ {= - \log (\lambda - t (x))} & {\mathrm{Differentistethis!}} \end{array}
$$

$$
\frac {1}{\lambda_ {- t} (x)} \left(\lambda_ {- t} ^ {\prime} (x)\right) = \sum_ {m >} \psi_ {(x)} ^ {m} t ^ {m - 1}.
$$

$$
\lambda_ {- t} ^ {\prime} (x) = \lambda_ {- t} (x) \cdot \sum_ {m > 1} \Psi_ {X} ^ {m} t ^ {m - 1}
$$

$$
\lambda_ {t} (x) = 1 + t x + t ^ {2} \vert x ^ {2}
$$

$$
\lambda_ {t} ^ {\prime} (x) = x + 2 t \lambda^ {2} x + \dots
$$

$$
\lambda_ {- t} ^ {\prime} (x) = x - 2 t \lambda^ {2} x + 3 t ^ {2} \lambda^ {3} x -
$$

$$
= (1 - t x + t ^ {2} \lambda^ {2} x - \dots) (\psi_ {x} ^ {\prime} t ^ {0} + \psi_ {x} ^ {2} t ^ {1} + \psi
$$

$$
\begin{array}{r l} {\psi_ {x} ^ {\prime} = x} \\ {- 2 \lambda^ {2} x =} & {\psi_ {x} ^ {2} - x \bar {\psi} _ {x} ^ {\prime}} \\ {+ 3 \lambda^ {3} x =} & {\psi_ {x} ^ {3} - x \psi_ {x} ^ {2} t + \lambda^ {2} x \cdot x.} \\ {- 4 \lambda^ {4} x =} & {\psi_ {x} ^ {4} - x \psi_ {x} ^ {3} + \lambda^ {8} x \cdot \psi_ {x} ^ {2} - \lambda^ {3} x \cdot x.} \end{array}
$$

$$
\begin{array}{l} \text { Newton } (\neg k) ^ {k - 1} x = \psi^ {k} x - x \psi^ {k - 1} x + \lambda^ {2} x \cdot \psi^ {k - 2} x - \dots + (- 1) ^ {k - 1} \lambda^ {k - 1} (x) \cdot x. \\ \text { think   of } \lambda^ {k} x = \operatorname * {e l m} _ {i, i <   \dots <   i, i} \sum_ {x _ {i}, \ldots , x _ {i, j}} \psi^ {k} x = \sum x _ {i} ^ {k}. \end{array}
$$

Theorem: A perfect $\Rightarrow K_{n}A$ uniquely $p$-divisible; $p: K_{n}A \xrightarrow{\approx} K_{n}A$$\pi \geqslant$ Proof: (1) $\Psi^{p} = Frobenius$. Hence $\Psi^{p}$ is isomorphism on $\tilde{K}(X,A)$, for any $X$, Let $X = S^{n}$$= SS^{n}$

② cup-products in $\widetilde{K}(SY;A)$ vanish.
general fact about multiplicative homology theories.
clreg cocycles to diff. sides.
Hence $(-1)^{p-1}p\cdot\lambda^{p}(x)=\psi^{p}(x)$ in $\widetilde{K}(SY;A)$.
QED.
$\lambda^{p}$ is homo now since cup-products vanish.
$\gamma_{t}(x)=1+t\gamma^{\prime}x+t^{2}\gamma^{\prime 2}x+\ldots=\frac{\lambda t}{1-t}(x)$.

$$
r _ {t} (L - 1) = \frac {(1 + \frac {t}{1 - t} L)}{(1 + \frac {t}{1 - t})} = 1 + t (L - 1).
$$

$\text{Thm: } \forall x \in \widetilde{K}(X, A), \exists n \text{ s.t. } r^{i_1}(x) \ldots r^{i_r}(x) = 0 \quad i_1 + \ldots + i_r \geq n.$$\text{Cor: } \forall x \in \widetilde{K}(X, A), \exists n \text{ s.t. } \prod_{i=1}^{n} (\psi^k - k^i)(x) = 0.$

Because formally one has identities: $[\prod_{i=1}^{n} (\psi^k - k^i)](x) \equiv 0.$

mod ideal generated by $r^{i_1}(x) \ldots r^{i_r}(x). \quad i_1 + \ldots + i_r \geq m.$

Case k=2:  $\psi^{k}L=L^{k}=(1+(L-1))^{k}=1+k(L-1)+\left(\frac{k}{2}\right)(L-1)^{2}+$$\psi^{k}[\sum(L_{i}-1)]=\sum\psi^{k}(L_{i}-1)=\sum(\psi^{k}L_{i}-1)$$=k[\sum(L_{i}-1)+\left(\frac{k}{2}\right)\sum(L_{i}-1)^{2}+\ldots]$

Proof of Theorem: First step is to show  $\gamma_{t}(x)$  is a polynomial in t.
 $\widetilde{K}(X,A)=[X,BGL(A)^{+}]$

i.e. $x^{n}(x) = 0$, n large.

$\tan(\pi, X, GL_{n}A) = [X, BGL_{n}A] \xrightarrow{①} [X, BGL_{n}(A)^{+}]$$I$$E = n$$m$$②$

It suffices to show that:  $\gamma^{k}([E]-n)=0$  in  $\widetilde{R}(\pi,X;A)$ .
if E is a representation on  $A_{j}^{n}$  for k>n.

$\gamma_{t}(1)=\frac{1}{1-t}$ ,  $\gamma_{t}([E]-n)=\gamma_{t}(E)/\gamma_{t}(n)=\gamma_{t}(E)(1-t)^{n}$$=\frac{\lambda_{t}}{1-t}(E)(1-t)^{n}=$

$= \left( {1 + {\lambda }^{\prime }\left( E\right) \frac{t}{1 - t} + \cdots  + {\lambda }^{n}E{\left( \frac{t}{1 - t}\right) }^{n}}\right) \left( {1 - t}\right) ^{n}$ . because ${\Lambda }^{k}E = 0,\;$ for $k > n,\;\operatorname{dim}E = n$

5.  $\gamma_{t}([E]-n)$  is a polynomial of degree  $\leq n$ .

$$
r _ {t} (x) \cdot r _ {t} (- x) = r _ {t} (0) = 1
$$

Lemma: If  $(f, a) = 1$ , then coefficients of  $x_{i}, i > 0$ , are nilpotent.

$\gamma$-filtration is locally nilpotent
$\Rightarrow$ (as in Atiyah's book) one gets $\widetilde{K}(X,A)\otimes\mathbb{Q}=\bigoplus_{i\geq1}V_{(i)}$

where  $V_{(i)} = \{ x \in \widetilde{F}(X, A) \otimes Q : \Psi^{k}x = k^{i}x\}$ .

So for algebraic $K$-groups: $K_{n}(A) \otimes Q \cong \oplus V_{(i)_{n}}$.

$A^{*}\rightarrow k,A$$\psi^{k}\alpha=k\alpha,\quad\alpha\in A^{*}\subseteq k,A.$

$F \text{ field: } \alpha \in K_{2}F$$\psi^{k}\alpha = k^{2}\alpha.$

Adams operations in algebraic K-groups are not well-understood.

define suspension of ring A, SA sit.  $K_{1}(SA)=K_{0}A$ .

Let $\pi: A \to B$ ring epimorphism.
Consider triples $(E, F, \alpha)$$E, F \in \mathcal{R}^{0}(A)$$\alpha: \pi E \xrightarrow{\approx} \pi F$$\pi E = E / \text{ker}(\pi)E$.

The set of 150 classes of such triples is a monoid. M
$(E,F,\alpha) \oplus (E',F',\alpha') = (E \oplus E', F \oplus F', \alpha \oplus \alpha').$

$\bigoplus_{i=1}^{n}\mathbb{Q}(A_X)\overline{Y}$  and $\text{and } (x,y,z) \in A_{\mu,0}\big| = \left\{X^2t = x^2Y : \mathbb{Q}(A_X)\overline{Y}\right\} = y$

A.  \( \overline{1} \)  是  \( ^{\*} \) A.  \( \overline{n} \) ， \( \overline{n} \)  和  \( \overline{n} \)  的值， \( \overline{1} \)  与  \( \overline{n} \)  的值  \( \overline{n} \) 

 \( x^{k}A = x^{4}y \) 

 \( \overline{n} \)  是  \( \overline{n} \)  的值， \( k \)  是  \( \overline{n} \) 

 \( b\_{0}(x, y) = b\_{1}(x, y) \) 

 \( A\_{21} = (A\_{2})A\_{1} \) 

 \( A\_{22} = A\_{21} \) 

 \( A\_{23} = A\_{22} \) 

 \( a\_{1} = A\_{1}, a\_{2} = A\_{2} \) 

 \( a\_{2} = A\_{2}, a\_{3} = A\_{3} \) 

 \( a\_{3} = A\_{3}, a\_{4} = A\_{4} \) 

 \( a\_{5} = A\_{5}, a\_{6} = A\_{6} \) 

 \( a\_{7} = A\_{7}, a\_{8} = A\_{8} \) 

 \( a\_{9} = A\_{9}, a\_{10} = A\_{10} \) 

 \( a\_{11} = A\_{11}, a\_{12} = A\_{12} \) 

 \( a\_{13} = A\_{13}, a\_{14} = A\_{14} \) 

 \( a\_{15} = A\_{15}, a\_{16} = A\_{16} \) 

 \( a\_{17} = A\_{17}, a\_{18} = A\_{18} \) 

 \( a\_{19} = A\_{19}, a\_{20} = A\_{20} \) 

 \( a\_{21} = A\_{21}, a\_{22} = A\_{22} \) 

 \( a\_{23} = A\_{23}, a\_{24} = A\_{24} \) 

 \( a\_{25} = A\_{25}, a\_{26} = A\_{26} \) 

 \( a\_{27} = A\_{27}, a\_{28} = A\_{28} \) 

 \( a\_{29} = A\_{29}, a\_{30} = A\_{30} \) 

 \( a\_{31} = A\_{31}, a\_{32} = A\_{32} \) 

 \( a\_{33} = A\_{33}, a\_{34} = A\_{34} \) 

 \( a\_{35} = A\_{35}, a\_{36} = A\_{36} \) 

 \( a\_{37} = A\_{37}, a\_{38} = A\_{38} \) 

 \( a\_{39} = A\_{39}, a\_{40} = A\_{40} \) 

 \( a\_{41} = A\_{41}, a\_{42} = A\_{42} \) 

 \( a\_{43} = A\_{43}, a\_{44} = A\_{44} \) 

 \( a\_{45} = A\_{45}, a\_{46} = A\_{46} \) 

 \( a\_{47} = A\_{47}, a\_{48} = A\_{48} \) 

 \( a\_{49} = A\_{49}, a\_{50} = A\_{50} \) 

 \( a\_{51} = A\_{51}, a\_{52} = A\_{52} \) 

 \( a\_{53} = A\_{53}, a\_{54} = A\_{54} \) 

 \( a\_{55} = A\_{55}, a\_{56} = A\_{56} \) 

 \( a\_{57} = A\_{57}, a\_{58} = A\_{58} \) 

 \( a\_{59} = A\_{59}, a\_{60} = A\_{60} \) 

 \( a\_{61} = A\_{61}, a\_{62} = A\_{62} \) 

 \( a\_{63} = A\_{63}, a\_{64} = A\_{64} \) 

 \( a\_{65} = A\_{65}, a\_{66} = A\_{66} \) 

 \( a\_{67} = A\_{67}, a\_{68} = A\_{68} \) 

 \( a\_{69} = A\_{69}, a\_{70} = A\_{70} \) 

 \( a\_{71} = A\_{71}, a\_{72}, a\_{73}, a\_{74}, a\_{75}, a\_{76}, a\_{77}, a\_{78}, a\_{79}, a\_{80}, a80, b80, b81, b82, b83, b84, b85, b86, b87, b88, b89, b90, b91, b92, b93, b94, b95, b96, b97, b98, b99, b100, b101, b102, b103, b104, b105, b106, b107, b108, b109, b110, b111, b112, b113, b114, b115, b116, b117, b118, b119, b120, b121, b122, b123, b124, b125, b126, b127, b128, b129, b130, b131, b132, b133, b134, b135, b136, b137, b138, b139, b140, b141, b142, b143, b144, b145, b146, b147, b148, b149, b150, b151, b152, b153, b154, b155, b156, b157, b158, b159, b160, b161, b162, b163, b164, b165, b166, b167, b168, b169, b170, b171, b172, b173, b174, b175, b176, b177, b178, b179, b180, b181, b182, b183, b184, b185, b186, b187, b188, b189, b190, b191, b192, b193, b194, b195, b196, b197, b198, b199, b200