compact K de $\mathbf{R}^n$, on puisse trouver une partie disquée $\mathbf{B} \in \mathfrak{C}$ pour laquelle $\vec{\mathbf{T}} \in \overline{\mathbf{L}_{\mathbf{k}}^{i}}(\mathbf{F}_{\mathbf{B}})$; $b) \theta$ soit $\mathfrak{C}$-hypocontinue.

$C') \vec{S}_{*_{t}} \vec{T}$ existe au sens de la proposition 39; il existe un ensemble saturé $\mathcal{C}$ de parties bornées complétantes de F tel que: a) $\vec{T} \in \mathcal{D}'(F_{\mathcal{G}})$ b) $\vec{S} \in \overline{\mathcal{P}^{1}}(E)$; c) $\theta$ soit $\mathcal{G}$-hypocontinue.

C'', C''' respectivement obtenues par symétrie à partir de C, C', en changeant les rôles de $\vec{S}$ et $\vec{T}$, E et F.

Notation fonctionnelle du produit de convolution.

Soient $\vec{S} \in \mathcal{D}'(E)$, $\vec{T} \in \mathcal{D}'(F)$, des distributions sur $R^n$. On peut conventionnellement donner un sens à $\vec{S}(\hat{x} - \hat{t}) \otimes \otimes_t \vec{T}(\hat{t})$; on le définit comme identique, pour le changement de variables $x - t = \xi$, $t = \eta$, à la distribution $\vec{S}_\xi \otimes \otimes_t \vec{T}_\eta$.

On peut alors se demander, dans les cas étudiés aux propositions 34, 38, 39, si $\vec{S} * \vec{T}$ coïncide avec l'intégrale partielle en $t$ du produit ainsi défini : a-t-on $(S * _{t} T)(\hat{x}) = \int_{R^{n}} (\vec{S}(\hat{x} - t) \otimes \otimes_{t} \vec{T}(t)) dt?$

Nous devons d'abord voir si le second membre a un sens, c'est-à-dire si $\vec{S}(\hat{x}-\hat{t})\otimes\otimes_{t}\vec{T}(t)$ est partiellement sommable en $t$ (chapitre 1, § 5). D'après ce que nous avons vu au chapitre 1, page 131, 2°, nous devons chercher si, pour toute $\varphi\in\mathfrak{D}_{x},\left(\vec{S}(x-\hat{t})\otimes\otimes_{t}\vec{T}(\hat{t})\right)\cdot\varphi(x)$ est dans $(\mathfrak{D}_{L^{1}}^{\prime})_{t}$; s'il en est ainsi, $\vec{S}(\hat{x}-\hat{t})\otimes\otimes_{t}\vec{T}(\hat{t})$ sera bien partiellement sommable en $t$, et on aura

$$
\begin{array}{r l} \left[ \int_ {\mathbb {R} ^ {n}} (\vec {\mathrm{S}} (x - t) \otimes \otimes_ {t} \vec {\mathrm{T}} (t)) d t \right] \cdot \varphi (x) \\ = \int_ {\mathbb {R} ^ {n}} [ (\vec {\mathrm{S}} (x - t) \otimes \otimes_ {t} \vec {\mathrm{T}} (t)) \cdot \varphi (x) ] d t. \end{array} \tag {II,7;22}
$$

Mais, d'après la définition même de $\vec{S}(\hat{x}-\hat{t})\otimes\otimes_{t}\vec{T}(\hat{t})$ par changement de variables, et d'après la règle de Fubini énoncée à la proposition 33, on a, pour toute $\psi\in\mathfrak{D}$:

$$
\begin{array}{l} \text {(II, 7; 23)} \quad \left(\vec {\mathrm{S}} (x - t) \otimes \otimes_ {t} \vec {\mathrm{T}} (t)\right) \cdot \varphi (x) \psi (t) \\ = \left(\vec {\mathrm{S}} _ {\xi} \otimes \otimes_ {t} \vec {\mathrm{T}} _ {\eta}\right) \cdot \varphi (\xi + \eta) \psi (\eta) = \vec {\mathrm{T}} _ {\eta} \cdot_ {t} \left[ \psi (\eta) \left(\vec {\mathrm{S}} _ {\xi} \cdot \varphi (\xi + \eta)\right) \right], \end{array}
$$

le produit scalaire : du dernier membre résultant de l'application de la proposition 10 à $\psi(\hat{\eta})\left(\vec{S}_{\xi}\cdot\varphi(\xi+\hat{\eta})\right)\in\mathcal{D}_{\eta}(E;\beta_{0}),\vec{T}_{\eta}\in\mathcal{D}^{\prime}(F).$

Mais $\vec{S}_{\xi} \cdot \varphi(\xi + \hat{\eta})$ n'est autre que $\left(\check{\vec{S}} * \varphi\right)(\hat{\eta})$ (formule (I, 3; 12)); alors le produit multiplicatif $\left[\left(\check{\vec{S}} * \varphi\right) \vec{T}\right]_{t}$ a un sens d'après le corollaire 1 de la proposition 32, cas 2, avec $\left(\check{\vec{S}} * \varphi\right) \in \mathcal{E}(E)$, localement $\beta_{0}$-bornée, $\vec{T} \in \mathfrak{D}'(F)$, et on a précisément (formule (II, 5; 11))

$$
\left[ \left(\check {\tilde {S}} _ {*} \varphi\right) \vec {\mathrm{T}} \right] _ {i} \cdot \psi = \vec {\mathrm{T}} \cdot_ {i} \left(\psi \left(\check {\tilde {S}} _ {*} \varphi\right)\right), \tag {II,7;24}
$$

le dernier membre étant relatif à $\psi\left(\check{\mathbf{S}}*\varphi\right)\in\mathfrak{D}(\mathrm{E};\beta_{0})$ et $\vec{\mathbf{T}}\in\mathfrak{D}^{\prime}(\mathbf{F})$. Alors (II, 7; 23) et (II, 7; 24) donnent $\left(\check{\mathbf{S}}(x-t)\otimes\otimes_{t}\vec{\mathbf{T}}(t)\right)\cdot\varphi(x)\psi(t)=\left[\left(\check{\mathbf{S}}*\varphi\right)\vec{\mathbf{T}}\right]_{t}\cdot\psi,$ de sorte que l'on a

$$
\text {(II, 7; 25)} \quad \left(\vec {\mathrm{S}} (x - \hat {t}) \otimes \otimes_ {i} \vec {\mathrm{T}} (\hat {t})\right) \cdot \varphi (x) = \left[ \left(\check {\mathrm{S}} * \varphi\right) \vec {\mathrm{T}} \right] _ {i} (\hat {t}).
$$

Nous devons donc voir si $\left[\left(\check{\mathbf{S}}*\varphi\right)\vec{\mathbf{T}}\right]_{t}$ est dans $\mathcal{D}_{\mathbf{L}^{4}}^{\prime}$; et s'il en est ainsi, $\vec{\mathbf{S}}(\hat{x}-\hat{t})\otimes\otimes_{t}\vec{\mathbf{T}}(\hat{t})$ sera partiellement sommable en $t$, et l'on aura, d'après (II, 7; 22) et (II, 7; 25):

$$
\left(\mathrm{II}, 7; 2 6\right) \left[ \int_ {\mathbb {R} ^ {n}} \left(\vec {\mathrm{S}} (x - t) \otimes \otimes_ {t} \vec {\mathrm{T}} (t)\right) d t \right] \cdot \varphi (x) = \int_ {\mathbb {R} ^ {n}} \left[ \left(\check {\mathrm{S}} * \varphi\right) \vec {\mathrm{T}} \right] _ {t} d t.
$$

A) Supposons d'abord que $\vec{S}$ et $\vec{T}$ vérifient les conditions de la proposition 39. Alors $\check{\vec{S}}*\varphi$ et $\vec{T}$ ont des supports d'intersection compacte; leur produit multiplicatif a donc un support compact (corollaire 1 de la proposition 32), donc est bien sommable; en outre, si $\alpha\in\mathcal{D}$ égale à 1 sur un voisinage de l'intersection des supports de $\check{\vec{S}}*\varphi$ et de $\vec{T}$, on a, d'après (II, 5; 12):$\left[\left(\check{\vec{S}}*\varphi\right)\vec{T}\right]_{t}=\alpha\left[\left(\check{\vec{S}}*\varphi\right)\vec{T}\right]_{t}=\left[\left(\alpha\left(\check{\vec{S}}*\varphi\right)\right)\vec{T}\right]_{t}$, avec $\alpha\left(\check{\vec{S}}*\varphi\right)\in\mathcal{D}(E;\beta_{0})$, $\vec{T}\in\mathcal{D}'(F)$. Donc $\check{\vec{S}}(\hat{x}-\hat{t})\otimes\otimes_{t}\vec{T}(\hat{t})$ est partiellement sommable en $t$, et on a (II, 7; 26), pour $\varphi\in\mathcal{D}$; par ailleurs on peut appliquer le corollaire 2 de la proposition 32, avec $\mathcal{K}_{1}=\mathcal{H}_{1}=\mathcal{M}_{1}=\mathcal{D}'$, $\mathcal{L}_{1}=\mathcal{E}$, et on aura

$$
\int_ {\mathbb {R} ^ {n}} \left[ \left(\alpha (\check {\mathbf {S}} * \varphi)\right) \vec {\mathbf {T}} \right] _ {t} d t = \left(\alpha (\check {\mathbf {S}} * \varphi)\right) \cdot_ {t} \vec {\mathbf {T}},
$$

le dernier produit scalaire étant celui de la proposition 10 relatif à $\alpha\left(\check{\mathbf{S}}*\varphi\right)\in\mathfrak{D}(\mathbf{E};\beta_{0}),\quad\vec{\mathbf{T}}\in\mathfrak{D}^{\prime}(\mathbf{F})$, ou encore le produit scalaire

$\left(\check{\vec{S}}*\varphi\right)\cdot_{t}\vec{T}$ de la remarque qui suit la proposition 20, avec $\check{\vec{S}}*\varphi\in\mathcal{E}(E)$ localement $\beta_{0}$-bornée, $\vec{T}\in\mathcal{D}'(F)$, l'intersection des supports étant compacte; et ce dernier n'est autre que le produit scalaire $\left(\vec{S}_{*_{t}}\vec{T}\right)\cdot\varphi$, où $\vec{S}_{*_{t}}\vec{T}$ est défini d'après la proposition 39 (formule (II, 7; 9)). On a donc, dans les conditions de la proposition 39:

$$
\begin{array}{r l} \int_ {\mathbb {R} ^ {n}} (\vec {\mathrm{S}} (\hat {x} - t) \otimes \otimes_ {t} \vec {\mathrm{T}} (t)) d t \\ = & (\vec {\mathrm{S}} * _ {t} \vec {\mathrm{T}}) (\hat {x}) \in \mathcal {D} ^ {\prime} (\mathrm{E} \otimes_ {t} \mathrm{F}). \end{array}\tag{II, 7; 29) (1}
$$

B) Supposons maintenant que l'on se trouve dans les conditions de la proposition 38. Supposons d'autre part qu'il existe des espaces $\mathfrak{M}_{1},\mathfrak{L}_{1}$, tels que $\mathcal{H},\mathcal{K},\mathfrak{L}_{1},\mathfrak{M}_{1}$, vérifient les conditions d'application de la proposition 32, que $\mathcal{B}_{c}\subset\mathfrak{L}_{1}$, avec une topologie plus fine que la topologie induite, et que $\tilde{\mathbf{S}}*\boldsymbol{\varphi}\in\mathfrak{M}_{1}(\mathbf{E})$.

On a donc, d'après le corollaire 2 de la proposition 32 :

$$
\int_ {\mathbb {R} ^ {n}} \left[ (\check {\vec {S}} * \varphi) \vec {T} \right] _ {t} = (\check {\vec {S}} * \varphi) \cdot_ {t} \vec {T} = (\vec {S} * _ {t} \vec {T}) \cdot \varphi ,\tag{II, 7; 30}
$$

le premier membre étant l'intégrale sur  $R^{n}$  du produit multiplicatif de  $\check{\vec{S}}*\varphi\in\mathfrak{M}_{1}(E),\vec{T}\in\mathcal{H}_{c}^{\prime}(F;\beta_{0})$ , défini par la proposition 32 à partir des espaces H, K, L, M, le deuxième étant le produit scalaire de  $\check{\vec{S}}*\varphi\in\mathfrak{K}(E),\vec{T}\in\mathcal{H}_{c}^{\prime}(F;\beta_{0})$ , défini par la proposition 10; le produit de convolution  $\check{S}_{*t}\vec{T}$  du troisième membre est celui de  $\check{S}\in\mathfrak{M}(E),\vec{T}\in\mathcal{H}_{c}^{\prime}(F;\beta_{0})$ , défini par la proposition 38 à partir des espaces H, K, L, M. En particulier  $\left[\left(\check{\vec{S}}*\varphi\right)\vec{T}\right]$ , défini par la proposition 32 est sommable.

Examinons ce produit d'un peu plus près. Pour $\psi \in \mathcal{D} \subset \mathfrak{L}_1$, on a:

$$
[ (\check {\vec {S}} * \varphi) \vec {T} ] _ {i} \cdot \psi = (\check {\vec {S}} * \varphi) \psi \cdot_ {i} \vec {T},\tag{II, 7; 31}
$$

avec $\left(\check{\mathbf{S}}*\varphi\right)\psi\in\mathcal{K}(\mathrm{E}),\quad\vec{\mathrm{T}}\in\mathcal{H}_{c}^{\prime}(\mathrm{F};\beta_{0})$, le produit scalaire étant celui de la proposition 10.

Mais on a aussi $\left(\vec{S}*\varphi\right)\psi\in\mathfrak{D}(E),\;\vec{T}\in\mathfrak{D}'(F;\beta_{0})$; et le produit scalaire qu'ils définissent de cette manière est le même (proposition 20); et ce produit scalaire est encore celui qui est défini

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Par suite d'un oubli, il n'y a pas de formule (II, 7; 28).</span></small>

par $\left(\check{\vec{S}}*\varphi\right)\psi\in\mathfrak{D}(E;\beta_{0}),\vec{T}\in\mathfrak{D}^{\prime}(F)$ (page 97). Mais alors le second membre de (II, 7; 31) est égal au premier, défini par le corollaire 1 de la proposition 32, cas 2, avec interversion des rôles de E et F, pour $\check{\vec{S}}*\varphi\in\mathcal{E}(E)$ localement $\beta_{0}$-bornée, $\vec{T}\in\mathfrak{D}^{\prime}(F)$; cela prouve donc que le produit $\left[\left(\check{\vec{S}}*\varphi\right)\vec{T}\right]_{t}$ défini par la proposition 32, à partir de $\check{\vec{S}}*\varphi\in\mathfrak{M}_{1}(E),\vec{T}\in\mathcal{H}_{c}^{\prime}(F;\beta_{0})$, et des espaces $\mathcal{H},\mathcal{K},\mathcal{L}_{1},\mathcal{M}_{1}$, est le même que le produit correspondant défini au corollaire 1 de la proposition 32, à partir de $\check{\vec{S}}*\varphi\in\mathcal{E}(E)$ localement $\beta_{0}$-bornée, $\vec{T}\in\mathfrak{D}^{\prime}(F)$; donc ce dernier produit est sommable sur $R^{n}$. Mais c'est ce dernier produit qui intervient dans (II, 7; 26); donc, dans les conditions où nous nous sommes placés, $\check{\vec{S}}(\hat{x}-\hat{t})\otimes\otimes_{t}\vec{T}(\hat{t})$ sera partiellement sommable en $t$, et alors (II, 7; 26) et (II, 7; 30) redonnent (II, 7; 29).

C) Supposons maintenant que $\mathcal{H}$, $\mathcal{K}$, soient des espaces de distributions normaux (quasi-complets); on suppose que $\mathcal{K}$ vérifie les conditions énoncées dans la proposition 4. Supposons qu'il existe une convolution de $\mathcal{H} \times \mathcal{K}$ dans $\mathcal{D}'$, hypo-continue par rapport aux parties compactes.

La proposition 34 (où l'on inverse les rôles de $\mathcal{H}$ et $\mathcal{K}$) permet alors de définir $\vec{\mathrm{S}}_{*\pi} \vec{\mathrm{T}} \in \mathcal{D}'(\mathrm{E} \otimes_{\pi} \mathrm{F})$, pour $\vec{\mathrm{S}} \in \mathcal{H}(\mathrm{E})$, $\vec{\mathrm{T}} \in \mathcal{K}(\mathrm{F})$. Si en outre $\mathcal{H}$ a la propriété d'approximation, (II, 7; 3) donne $(\vec{\mathrm{S}}_{*\pi} \vec{\mathrm{T}}) \cdot \varphi = (\check{\vec{\mathrm{S}}} * \varphi) \cdot_{\pi} \vec{\mathrm{T}}$, le produit scalaire étant celui de la proposition 4, avec $\check{\vec{\mathrm{S}}} * \varphi \in \mathcal{K}'(\mathrm{E})$, $\vec{\mathrm{T}} \in \mathcal{K}(\mathrm{F})$. Supposons maintenant qu'il existe une multiplication de $\mathcal{K} \times \mathcal{K}'$ dans $\mathcal{D}_{\mathrm{L}^1}$, hypocontinue par rapport aux parties compactes. Alors, d'après la proposition 31 (formule (II, 5; 7)]: $\int_{\mathbb{R}^n} [(\check{\vec{\mathrm{S}}} * \varphi) \vec{\mathrm{T}}]_{\pi} = (\check{\vec{\mathrm{S}}} * \varphi) \cdot_{\pi} \vec{\mathrm{T}}$; le produit multiplicatif $[(\check{\vec{\mathrm{S}}} * \varphi) \vec{\mathrm{T}}]_{\pi}$ est en particulier sommable sur $R^n$. Mais on a aussi $\check{\vec{\mathrm{S}}} * \varphi \in \mathcal{E}(\mathrm{E})$; si $\mathcal{K}$ donc $\mathcal{K}'$ (proposition 4 des préliminaires) a la propriété d'approximation par troncature et régularisation, le produit $[(\check{\vec{\mathrm{S}}} * \varphi) \vec{\mathrm{T}}]_{\pi}$ défini à partir de $\check{\vec{\mathrm{S}}} * \varphi \in \mathcal{K}'(\mathrm{E})$, $\vec{\mathrm{T}} \in \mathcal{K}(\mathrm{F})$, est le même que celui qui est défini à partir de $\check{\vec{\mathrm{S}}} * \varphi \in \mathcal{E}(\mathrm{E})$, $\vec{\mathrm{T}} \in \mathcal{D}'(\mathrm{F})$ (voir remarque $1^\circ$ page 122). Donc ce dernier produit multiplicatif est sommable.

Mais ce produit est aussi celui qui est défini par le corollaire 1 de la proposition 32, avec $\check{\mathbf{S}}*\varphi\in\mathcal{E}(\mathbf{E})$ localement $\beta_{0}$-bornée, $\vec{\mathbf{T}}\in\mathfrak{D}^{\prime}(\mathbf{F})$ ($\iota$ remplacé par $\pi$) (puisque les propositions 25 et 32, si elles sont toutes deux applicables, donnent le même résultat); et c'est celui qui intervient dans (II, 7; 26) (où $\iota$ est remplacé par $\pi$). Donc finalement $\vec{\mathbf{S}}(\hat{x}-\hat{t})\otimes\otimes_{\pi}\vec{\mathbf{T}}(\hat{t})$ est partiellement sommable en $t$, et son intégrale en $t$ est $(\vec{\mathbf{S}}*\pi\vec{\mathbf{T}})(\hat{x})$ défini par la proposition 34; on a encore (II, 7; 29), où $\iota$ est remplacé par $\pi$.

On a donc la proposition suivante :

PROPOSITION 41. — Soient E, F, des espaces localement convexes séparés, non nécessairement quasi-complets. Soient $\vec{S} \in \mathcal{D}'(E)$, $\vec{T} \in \mathcal{D}'(F)$; on peut toujours définir $\vec{S}(\hat{x} - \hat{t}) \otimes \otimes_{\iota} \vec{T}(t) \in \mathcal{D}'_{x,t}(E \widehat{\otimes}_{\iota} F)$. Cette distribution est partiellement sommable en $t$, et on a

$$
\int_ {\mathbf {R} ^ {n}} \left(\vec {\mathrm{S}} (\hat {x} - t) \otimes \otimes_ {t} \vec {\mathrm{T}} (t)\right) d t = \left(\vec {\mathrm{S}} * _ {t} \vec {\mathrm{T}}\right) (\hat {x}), \tag {II,7;29}
$$

dans l'un quelconque des cas suivants :

A) $\vec{\mathrm{S}}_{*_{t}}\vec{\mathrm{T}}$ a un sens d'après la proposition 39;

B) $\vec{S} *_{t}\vec{T}$ a un sens d'après la proposition 38, relative à 4 espaces $\mathcal{H}$, $\mathcal{K}$, $\mathcal{L}$, $\mathcal{M}$; il existe des espaces $\mathcal{L}_{1}$, $\mathcal{M}_{1}$, tels qu'on puisse définir un produit multiplicatif d'après la proposition 32, relative aux 4 espaces $\mathcal{H}$, $\mathcal{K}$, $\mathcal{L}_{1}$, $\mathcal{M}_{1}$; $\mathcal{B}_{c}$ est contenu dans $\mathcal{L}_{1}$, avec une topologie plus fine que la topologie induite; toute $\varphi \in \mathcal{D}$ est un opérateur de convolution de $\check{\mathcal{M}}$ dans $\mathcal{M}_{1}$.

D'autre part $\vec{\mathbb{S}}(\hat{x}-\hat{t})\otimes\otimes_{\pi}\vec{\mathbb{T}}(\hat{t})$ est partiellement sommable en $t$, et on a (II, 7; 29), où $\iota$ est remplacé par $\pi$, dans le cas suivant: C) $\mathcal{H}$, $\mathcal{K}$, sont des espaces de distributions normaux (quasi-complets); $\mathcal{H}$ a la propriété d'approximation; $\mathcal{K}$ a la propriété d'approximation par troncature et régularisation, la topologie $\gamma$, il est nucléaire, son dual fort est quasi-complet et nucléaire; il existe une convolution de $\mathcal{H}\times\mathcal{K}$ dans $\mathfrak{D}'$, et une multiplication de $\mathcal{K}\times\mathcal{K}'$ dans $\mathfrak{D}_{L^4}^{\prime}$, hypocontinues par rapport aux parties compactes; on a $\vec{\mathbb{S}}\in\mathcal{H}(\mathbb{E})$, $\vec{\mathbb{T}}\in\mathcal{K}(\mathbb{F})$, et $\vec{\mathbb{S}}_{*\pi}\vec{\mathbb{T}}$ est défini par la proposition 34 (où les rôles de $\mathcal{K}$ et $\mathcal{H}$ sont inversés).

Exemples. — On se trouve dans la condition B pour $\vec{S} \in \mathcal{E}'(E)$, $\vec{T} \in \mathcal{D}'(F; \beta_0)$ ($\mathcal{H} = \mathcal{K} = \mathcal{L} = \mathcal{D}$, $\mathfrak{M} = \mathcal{E}'$, $\mathfrak{M}_1 = \mathcal{D}$,

$\mathfrak{L}_1 = \mathfrak{E})$, ou $\vec{\mathrm{S}} \in \mathcal{O}_{\mathrm{C}}^{\prime}(\mathrm{E})$, $\vec{\mathrm{T}} \in \mathcal{P}^{\prime}(\mathrm{F}; \beta_0)$ (avec $\mathcal{H} = \mathfrak{K} = \mathfrak{L} = \mathfrak{S}$, $\mathfrak{M} = \mathcal{O}_{\mathrm{C}}^{\prime}$, $\mathfrak{M}_1 = \mathfrak{S}$, $\mathfrak{L}_1 = \mathcal{O}_{\mathrm{M}}$) ($^\dagger$). On se trouve dans la condition C avec $\mathrm{S} \in \mathcal{E}^{\prime}(\mathrm{F})$, $\vec{\mathrm{T}} \in \mathcal{D}^{\prime}(\mathrm{E})$, ou $\vec{\mathrm{S}} \in \mathcal{O}_{\mathrm{C}}^{\prime}(\mathrm{E})$, $\vec{\mathrm{T}} \in \mathcal{P}^{\prime}(\mathrm{F})$.

Remarques. — 1° Si la condition B ou la condition C est réalisée, le produit de convolution ne dépend que de S et T, et non des espaces de distributions qui sont intervenus, puisqu'il en est ainsi du premier membre de (II, 7; 29).

2° Contrairement à ce qui se passe pour la proposition 40, il y a dissymétrie entre les rôles de $\vec{S}$ et de $\vec{T}$ dans la proposition 41. Si $\vec{S}(\hat{x}-\hat{t})\otimes\otimes_{t}\vec{T}(\hat{t})$ est partiellement sommable en $t$, rien ne dit qu'il en soit de même pour $\vec{S}(\hat{t})\otimes\otimes_{t}\vec{T}(\hat{x}-\hat{t})$; et même s'il en est ainsi, rien ne dit que les intégrales en $t$ soient les mêmes.

Multiplication, convolution, transformations de Fourier et Laplace.

PROPOSITION 42. — Soient $\vec{S} \in \mathcal{O}_{\mathrm{M}}(\mathrm{E})$, $\vec{T} \in \mathscr{S}'(\mathrm{F})$, $\vec{\varphi} \in \mathscr{S}(\mathrm{E})$, (E, F, non nécessairement quasi-complets). On a la formule de Parseval:

$$
\text {(II, 7; 32)} \vec {\varphi} \cdot_ {\pi} \vec {T} = \mathcal {F} \vec {\varphi} \cdot_ {\pi} \overline {{\mathcal {F}}} \vec {T} \quad \left(\text {avec} \quad \overline {{\mathcal {F}}} \vec {T} = \overline {{\mathcal {F}}} \vec {T} = (\mathcal {F} \vec {T}) ^ {\vee}\right),
$$

et la formule de transformation de la multiplication en convolution:

$$
(\mathrm{II}, 7; 3 3)
$$

$$
\mathcal {F} ((\vec {\mathrm{ST}}) _ {\pi}) = \mathcal {F} \vec {\mathrm{S}} * _ {\pi} \mathcal {F} \vec {\mathrm{T}},
$$

les produits scalaires étant pris au sens de la proposition 4, le produit multiplicatif au sens de la proposition 25, le produit de convolution au sens de la proposition 34.

On démontrerait facilement cette proposition par transport de structure; mais autant vaut dire simplement que les deux membres de la première (resp. seconde) égalité définissent des applications bilinéaires séparément continues sur $\mathcal{S}(\mathrm{E})\times\mathcal{S}'(\mathrm{F})$ (resp. $\mathcal{O}_{\mathrm{M}}(\mathrm{E})\times\mathcal{S}'(\mathrm{F}))$, et coïncident sur $(\mathcal{S}\otimes\mathrm{E})\times(\mathcal{S}'\otimes\mathrm{F})$ (resp. $(\mathcal{O}_{\mathrm{M}}\otimes\mathrm{E})\times(\mathcal{S}'\otimes\mathrm{F}))$, donc partout.

(1) Tous ces espaces sont bien normaux, et ont les propriétés d'approximation requises dans la proposition 10 parce que nucléaires (voir note (1), page 58). $\mathcal{G}$ est bornologique comme espace de Frêchet; $\mathcal{O}_{\mathrm{M}}$ est bornologique d'après GROTHENDIECK [5], § 4, n° 4, théorème 16, page 131.

PROPOSITION 42 bis. — Soient $\vec{S} \in \mathcal{O}_{\mathrm{M}}(\mathrm{E})$, $T \in \mathscr{F}'(F; \beta_0)$, $\vec{\varphi} \in \mathscr{G}(E)$ (E, F, non nécessairement quasi-complets). On a (II, 7; 32 et 33), où $\pi$ est remplacé par $\iota$, les produits scalaires étant pris au sens de la proposition 10, le produit multiplicatif au sens de la proposition 32 (corollaire 1, cas 4), le produit de convolution au sens de la proposition 38 (exemple $2^{\circ}$, page 162).

L'opération $\mathcal{F}$ est en effet un automorphisme de l'espace $\mathcal{K} = \mathcal{H} = \mathcal{S}$, transformant l'identité $\Lambda = I$ en elle-même. Par transport de structure, il transforme donc l'application bilinéaire de la proposition 10 en elle-même. Mais pour faire ce transport de structure, on doit transformer $\mathcal{H}_c' = \mathcal{S}'$ en lui-même par l'opération contragrédiente $^t\mathcal{F}^{-1}$ de $\mathcal{F}$; mais on sait que $^t\mathcal{F}^{-1} = \overline{\mathcal{F}}$ (d'après la formule de Parseval dans le cas scalaire: $^t\mathcal{F}^{-1}\mathbf{T} \cdot \boldsymbol{\varphi} = \mathbf{T} \cdot \mathcal{F}^{-1}\boldsymbol{\varphi} = \mathbf{T} \cdot \overline{\mathcal{F}}\boldsymbol{\varphi} = \overline{\mathcal{F}}\mathbf{T} \cdot \boldsymbol{\varphi}$, ce qui démontre (II, 7; 33) ($\pi$ remplacé par $\iota$)). On en déduit alors (II, 7; 33) ($\pi$ remplacé par $\iota$), par:

$$
\begin{array}{r l} & \text {(II, 7; 34)} \quad \mathcal {F} [ (\vec {\mathrm{ST}}) _ {t} ] \cdot \varphi = (\vec {\mathrm{ST}}) _ {t} \cdot \mathcal {F} \varphi = \vec {\mathrm{S}} (\mathcal {F} \varphi) \cdot_ {t} \vec {\mathrm{T}} \\ & \quad = \mathcal {F} (\vec {\mathrm{S}} (\mathcal {F} \varphi)) \cdot_ {t} (\mathcal {F} \vec {\mathrm{T}}) ^ {\vee} = (\mathcal {F} \vec {\mathrm{S}} * \mathcal {F} \mathcal {F} \varphi) \cdot_ {t} (\mathcal {F} \vec {\mathrm{T}}) ^ {\vee} = (\mathcal {F} \vec {\mathrm{S}} * \check {\varphi}) \cdot_ {t} (\mathcal {F} \vec {\mathrm{T}}) ^ {\vee} \\ & \quad \quad = ((\mathcal {F} \vec {\mathrm{S}}) ^ {\vee} * \varphi) \cdot_ {t} \mathcal {F} \vec {\mathrm{T}} = (\mathcal {F} \vec {\mathrm{S}} * _ {t} \mathcal {F} \vec {\mathrm{T}}) \cdot \varphi , \end{array}
$$

pour $\varphi\in\mathcal{S}$ (en appliquant les résultats du chapitre r, page 73).

PROPOSITION 43 (1). — Soit $\Gamma$ un ensemble ouvert convexe du dual $\Xi^n$ de l'espace euclidien $X^n$. On peut définir une convolution de $(\mathcal{S}'(\Gamma))(E) \times (\mathcal{S}'(\Gamma))(F)$ dans $\mathcal{S}'(\Gamma)(E \otimes_{\pi} F)$, hypocontinue par rapport aux parties bornées. Si $\vec{A} \in (\mathcal{S}'(\Gamma))(E)$, $\vec{B} \in (\mathcal{S}'(\Gamma))(F)$, et $\vec{\alpha}(\hat{p})$ et $\vec{\mathfrak{B}}(\hat{p})$ sont leurs images de Laplace, pour $p \in \Gamma + i \Xi^n$, alors l'image de Laplace de $\vec{A}_{*\pi} \vec{B}$ est $\vec{\alpha}(\hat{p}) \otimes_{\pi} \vec{\mathfrak{B}}(\hat{p})$.

On peut être tenté de définir directement la convolution de  $(\mathcal{S}^{\prime}(\Gamma))(\mathrm{E})\times(\mathcal{S}^{\prime}(\Gamma))(\mathrm{F})$  dans  $(\mathcal{S}^{\prime}(\Gamma))(\mathrm{E}\otimes_{\pi}\mathrm{F})$ , en appliquant la proposition 3 à l'opération u de convolution de  $\mathcal{S}^{\prime}(\Gamma)\times\mathcal{S}^{\prime}(\Gamma)$  dans  $\mathcal{S}^{\prime}(\Gamma)$ . Mais alors il faudrait d'abord montrer que  $\mathcal{S}^{\prime}(\Gamma)$  est nucléaire, ce qui est aisé, mais aussi de dual nucléaire, ce qui l'est moins.

Procédons donc autrement. Choisissons une fois pour toutes

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\xi \in \Xi^{n}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$x\in \mathbf{X}^n$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Voir SCHWARTZ [3]. Pour simplifier, nous noterons par $\xi x$ le produit scalaire de $\xi \in \mathbb{E}^n$ et de $x \in \mathbf{X}^n$.</span></small>

$p_{0} \in \Gamma + i\Xi^{n}$. Alors, pour $\vec{S} \in (\mathcal{G}'(\Gamma))(E)$, $\vec{T} \in (\mathcal{G}'(\Gamma))(F)$, on peut définir $\vec{S}_{*\pi} \vec{T}$ par

$$
\mathrm{S} _ {*} \pi \mathrm{T} = \exp (p _ {0} \hat {x}) [ (\exp (- p _ {0} \hat {x}) \vec {\mathrm{S}}) * _ {\pi} (\exp (- p _ {0} \hat {x}) \vec {\mathrm{T}}) ],
$$

avec $\exp (-p_{0}\hat{x})\vec{\mathrm{S}}\in\mathcal{O}_{\mathrm{C}}^{\prime}(\mathrm{E}),\quad\exp (-p_{0}\hat{x})\vec{\mathrm{T}}\in\mathcal{O}_{\mathrm{C}}^{\prime}(\mathrm{F}),\quad\text{par la proposition 34 relative à la convolution de } \mathcal{O}_{\mathrm{C}}^{\prime}\times\mathcal{O}_{\mathrm{C}}^{\prime}\text{ dans } \mathcal{P}^{\prime}$. L'application bilinéaire $(\vec{\mathrm{S}},\vec{\mathrm{T}})\to\vec{\mathrm{S}}*_{\pi}\vec{\mathrm{T}}$ ainsi définie, de $(\mathcal{S}^{\prime}(\Gamma))(E)\times(\mathcal{S}^{\prime}(\Gamma))(F)\text{ dans }\left(\mathcal{S}^{\prime}(\{\xi_{0}\})\right)(E\otimes_{\pi}F)$, est hypocontinue par rapport aux parties bornées. Mais $\mathcal{S}^{\prime}(\Gamma)$ est trivialement normal et a la propriété d'approximation par troncature et régularisation [car il en est ainsi de $\mathcal{S}^{\prime}$. Pour la propriété d'approximation par régularisation, on remarquera que $\exp (-\xi\hat{x})(\rho_{v}*U)=\exp (-\xi\hat{x})\rho_{v}*exp(-\xi\hat{x})U,\text{ pour }U\in\mathcal{S}^{\prime}(\Gamma),$$\xi\in\Gamma;\text{ et }exp(-\xi\hat{x})\rho_{v}(\hat{x})$ a des propriétés analogues à celles de $\rho_{v}]$, donc il a la propriété d'approximation (préliminaires, proposition 3). Alors la convolution précédente de $(\mathcal{S}^{\prime}(\Gamma))(E)\times(\mathcal{S}^{\prime}(\Gamma))(F)\text{ dans } \mathcal{D}^{\prime}(E\otimes_{\pi}F)$ est entièrement connue quand elle l'est sur le sous-espace $(\mathcal{S}^{\prime}(\Gamma)\otimes E)\times(\mathcal{S}^{\prime}(\Gamma)\otimes F);$ mais sur ce sous-espace l'opération est indépendante du point $p_{0}$ choisi dans $\Gamma+i\Xi^{n}$, donc il en est de même de l'opération sur l'espace entier. De plus, on voit même qu'elle est hypocontinue par rapport aux parties bornées, de $(\mathcal{S}^{\prime}(\Gamma))(E)\times(\mathcal{S}^{\prime}(\Gamma))(F)\text{ dans }\left(\mathcal{S}^{\prime}(\{\xi_{0}\})\right)(E\otimes_{\pi}F)$, quel que soit $\xi_{0}\in\Gamma,$ donc elle est hypocontinue par rapport aux parties bornées, de $(\mathcal{S}^{\prime}(\Gamma))(E)\times(\mathcal{S}^{\prime}(\Gamma))(F)\text{ dans }\left(\mathcal{S}^{\prime}(\Gamma)\right)(E\otimes_{\pi}F)$, et c'est la seule application bilinéaire séparément continue qui, pour $A\in\mathcal{S}^{\prime}(\Gamma),B\in\mathcal{S}^{\prime}(\Gamma),\vec{e}\in E,\vec{f}\in F,$ vérifie $A\vec{e}*_{\pi}B\vec{f}=(A*B)\vec{e}\otimes\vec{f}$.

Quant à la transformation de la convolution en multiplication, elle est évidente; la valeur en $p$ de l'image de Laplace de $\vec{\mathbf{A}}_{*\pi}\vec{\mathbf{B}}$ et le produit $\vec{\alpha}(p)\otimes_{\pi}\vec{\mathcal{B}}(p)$ définissent, pour $p$ fixé, des applications bilinéaires séparément continues de $(\mathscr{S}'(\Gamma))(E)\times(\mathscr{S}'(\Gamma))(F)$ dans $E\otimes_{\pi}F$, qui coïncident sur $(\mathscr{S}'(\Gamma)\otimes E)\times(\mathscr{S}'(\Gamma)\otimes F)$, donc partout.

COROLLAIRE. — Soit n = 1. Soit a un nombre réel, et soient $\vec{\mathrm{A}}$ espaces des distributions appartenant respectivement à $(\mathfrak{X}'(a))(E) \subset \mathfrak{D}'_{+}(E)$ et $(\mathfrak{X}'(a))(F) \subset \mathfrak{D}'_{+}(F)$. Alors leur produit de convolution $\pi$ appartient à $(\mathfrak{X}'(a))(E \widehat{\otimes}_{\pi} F)$, et son image de

Laplace est le produit multiplicatif des images de Laplace $\vec{\mathfrak{a}}(\hat{p})$ et $\vec{\mathfrak{B}}(\hat{p})$ de $\vec{\mathbf{A}}$ et $\vec{\mathbf{B}}$.

On a vu au chapitre 1, page 78, que, si $\Gamma_{a}$ est le convexe $\xi \geqslant a$, $\mathcal{X}'(a)$ est l'intersection de $\mathcal{S}'(\Gamma_{a})$ et de $\mathcal{D}_{+}^{\prime}$, espace des distributions à support limité à gauche. La convolution de $\mathcal{X}'(a) \times \mathcal{X}'(a)$ dans $\mathcal{X}'(a)$ est alors indifféremment la restriction de la convolution de $\mathcal{S}'(\Gamma_{a}) \times \mathcal{S}'(\Gamma_{a})$ dans $\mathcal{S}'(\Gamma_{a})$, ou la restriction de la convolution de $\mathcal{D}_{+}^{\prime} \times \mathcal{D}_{+}^{\prime}$ dans $\mathcal{D}_{+}^{\prime}$, car tous ces espaces ont la propriété d'approximation par troncature et régularisation; de même la convolution de $(\mathcal{X}'(a))(E) \times (\mathcal{X}'(a))(F)$ dans $(\mathcal{X}'(a))(E \otimes_{\pi} F)$ est indifféremment la restriction de la convolution de $(\mathcal{S}'(\Gamma_{a}))(E) \times (\mathcal{S}'(\Gamma_{a}))(F)$ dans $(\mathcal{S}'(\Gamma_{a}))(E \otimes_{\pi} F)$, ou la restriction de la convolution de $\mathcal{D}_{+}^{\prime}(E) \times \mathcal{D}_{+}^{\prime}(F)$ dans $\mathcal{D}_{+}^{\prime}(E \otimes_{\pi} F)$ (proposition 35).

Le résultat relatif à la transformation de Laplace revient à appliquer la proposition 43 à l'ouvert convexe $\mathring{\Gamma}_{a}$.

## § 8. Étude de trois contre-exemples.

Premier contre-exemple.

Soient $\vec{\alpha} \in \mathfrak{D}(E)$, $\vec{T} \in \mathfrak{D}'(F)$. Nous pouvons calculer $\vec{\alpha} *_{\pi} \vec{T}$ par la proposition 34; le résultat est un élément de $\mathcal{E}(E \otimes_{\pi} F)$. Mais si nous essayons de remplacer $\pi$ par $\iota, \gamma$, ou $\beta$, la proposition 34 n'est plus applicable. Si nous ne supposons pas $\vec{\alpha}$ ou $\vec{T}$ bornée, nous n'avons à notre disposition que le corollaire de la proposition 39, qui, par exemple, nous montre seulement que, si $\vec{\alpha} \in \overline{\mathfrak{D}}(E)$, $\vec{\alpha} *_{\beta} \vec{T}$ est un élément de $\mathfrak{D}'(E \otimes_{\beta} F)$, c'est-à-dire une distribution à valeurs dans $E \otimes_{\beta} F$, non nécessairement une fonction. Nous allons montrer par un contre-exemple que $\vec{\alpha} *_{\beta} \vec{T}$ peut en effet n'être pas une fonction (mais son image $\vec{\alpha} *_{\pi} \vec{T}$ dans $\mathfrak{D}'(E \otimes_{\pi} F)$ est toujours une fonction indéfiniment dérivable à valeurs dans $E \otimes_{\pi} F$), de sorte qu'on ne peut plus parler ici de régularisation.

Raisonnons pour simplifier sur le tore $\mathbf{T}^{n}$ au lieu de $\mathbb{R}^{n}$. Prenons $\mathbf{E} = \mathfrak{D}'$, $\mathbf{F} = \mathfrak{D}$.

La fonction $\vec{\alpha} \in \mathcal{D}(\mathcal{D}')$ est celle qui définit l'application

identique $\mathbf{L}_{\vec{\varphi}}$ de $\mathfrak{D}'$ dans $\mathfrak{D}'$, la distribution $\vec{\mathbf{T}} \in \mathfrak{D}'(\mathfrak{D})$ est celle qui définit la symétrie $\mathbf{L}_{\vec{\mathbf{T}}}: \chi \to \check{\chi}$ de $\mathfrak{D}$ dans $\mathfrak{D}$. Appelons B la forme bilinéaire définissant la dualité entre $\mathbf{E} = \mathfrak{D}'$ et $\mathbf{F} = \mathfrak{D}$; elle est hypocontinue, donc se prolonge en une forme linéaire continue $\overline{\mathbf{B}}$ sur $\mathfrak{D}' \otimes_{\beta} \mathfrak{D}$, et pour montrer que $\vec{\alpha} *_{\beta} \vec{\mathbf{T}} \in \mathfrak{D}'(\mathfrak{D}' \otimes_{\beta} \mathfrak{D})$ n'est pas une fonction, il suffit de montrer que son image $\overline{\mathbf{B}}(\vec{\alpha} *_{\beta} \vec{\mathbf{T}}) = \vec{\alpha} *_{\mathrm{B}} \vec{\mathbf{T}} \in \mathfrak{D}'$ n'est pas une fonction. On a, d'après (II, 7; 8):

$$
(\mathrm{II}, 8; 1) \quad (\vec {\alpha} _ {*} \vec {T}) \cdot \psi = (\vec {\alpha} _ {\xi} \otimes_ {B} \vec {T} _ {\eta}) \cdot \psi (\xi + \eta), \psi \in \mathfrak {D}.
$$

Tout d'abord on a, pour $u \in \mathcal{D}_{\xi}$, $\nu \in \mathcal{D}_{\eta}$:

$$
\begin{array}{r l} \big (\vec {\alpha} _ {\xi} \otimes_ {\mathrm{B}} \vec {\mathrm{T}} _ {\eta} \big) \cdot u (\xi) \otimes \nu (\eta) & = \mathrm{B} (\mathrm{L} _ {\vec {\alpha}} (u), \mathrm{L} _ {\vec {\mathrm{T}}} (\nu)) \\ & = \mathrm{B} (u, \check {\nu}) = \int_ {\mathbf {T} ^ {n}} u (t) \nu (- t) d t. \end{array}
$$

Comme $\vec{\alpha}_{\xi} \otimes_{\mathrm{B}} \vec{T}_{\eta}$ est une distribution, donc une forme linéaire continue sur $\mathfrak{D}_{\xi,\eta}$, ce ne peut être que celle qui est définie par

$$
\text {(II, 8; 3)} \quad \left(\vec {\alpha} _ {\xi} \otimes_ {B} \vec {T} _ {\eta}\right) \cdot \theta (\xi , \eta) = \int_ {T ^ {n}} \theta (t, - t) d t, \quad \theta \in \mathfrak {D} _ {\xi , \eta},
$$

cas (II, 8; 2) et (II, 8; 3) coincident pour $\theta(\xi, \hat{\eta}) = u(\hat{\xi}) \otimes v(\hat{\eta})$. Alors on aura, pour $\psi \in \mathfrak{D}$:

$$
(\mathrm{II}, 8; 4) \quad (\vec {\alpha} * _ {\mathrm{B}} \vec {\mathrm{T}}) \cdot \psi = \int_ {\mathbf {T} ^ {n}} \psi (t - t) d t = \psi (0) \int_ {\mathbf {T} ^ {n}} d t = \psi (0)
$$

$$
\vec {\alpha} * _ {B} \vec {T} = \delta \in \mathcal {D} ^ {\prime},
$$

qui n'est pas une fonction.

Prenons maintenant pour B la forme bilinéaire $(\mathrm{S},\varphi)\to \mathrm{D}^p\mathrm{S}\cdot \varphi$ sur $\mathfrak{D}'\times \mathfrak{D}$, qui est encore hypocontinue. Alors on trouvera $\vec{\alpha}_{*\mathrm{B}}\vec{\mathrm{T}} = \mathrm{D}^{p}\delta \in \mathfrak{D}'$. Donc, en faisant varier B, on obtiendra des distributions $\vec{\alpha}_{*\mathrm{B}}\vec{\mathrm{T}}$ d'ordre arbitrairement élevé; donc $\vec{\alpha}_{*\beta}\vec{\mathrm{T}}$ est une distribution d'ordre infini à valeurs dans $\mathrm{E}\otimes_{\beta}\mathrm{F}$.

Par contre on voit bien ici que son image $\vec{\alpha} *_{\pi} \vec{T}$ dans $\mathfrak{D}'(\mathfrak{D}' \otimes_{\pi} \mathfrak{D})$ est une fonction indéfiniment dérivable. En effet $\vec{\alpha}_{\xi} \otimes_{\pi} \vec{T}_{\eta}$ définit l'application $L_{\vec{\alpha}_{\xi} \otimes_{\pi} \vec{T}_{\eta}}: \theta(\hat{\xi}, \hat{\eta}) \to \theta(\hat{\xi}, -\hat{\eta})$ de $\mathfrak{D}_{\xi, \eta}$ dans $\mathfrak{D}'_{\xi} \widehat{\otimes}_{\pi} \mathfrak{D}_{\eta}$, donc $\vec{\alpha} *_{\pi} \vec{T}$ est l'élément de $\mathfrak{D}'_{x}$ ($\mathfrak{D}'_{\xi} \widehat{\otimes}_{\pi} \mathfrak{D}_{\eta}$) qui définit l'application $\psi(\hat{x}) \to \psi(\hat{\xi} - \hat{\eta})$ de $\mathfrak{D}_{x}$ dans $\mathfrak{D}'_{\xi} \widehat{\otimes}_{\pi} \mathfrak{D}_{\eta}$.

C'est la distribution $\delta (\hat{x} -\hat{\xi} +\hat{\eta})$ , qui appartient bien à $\mathfrak{D}_x(\mathfrak{D}_\xi^\prime \widehat{\otimes}_\pi \mathfrak{D}_\eta) = \mathfrak{D}_x\widehat{\otimes}\mathfrak{D}_\xi^\prime \widehat{\otimes}\mathfrak{D}_\eta .$

Conséquence. — Nous avons défini à la proposition 4 l'élément $\vec{\varphi} \cdot_{\pi} \vec{T}$, sans restriction sur $\vec{\varphi} \in \mathcal{D}(E)$ et $\vec{T} \in \mathcal{D}'(E)$. Au contraire, pour définir $\vec{\varphi} \cdot_{\iota} \vec{T}$, $\vec{\varphi} \cdot_{\gamma} \vec{T}$, $\vec{\varphi} \cdot_{\beta} \vec{T}$, nous avons dû, par exemple, supposer T bornée (proposition 10). Un tel type de restriction était inévitable. Sans aucune restriction, $\vec{\varphi} *_{\beta} \vec{T} \in \mathcal{D}'(E \otimes_{\beta} F)$ existe toujours si $\vec{\varphi} \in \overline{\mathcal{D}}(E)$, mais ce n'est pas une fonction, et toute tentative de définir $\vec{\varphi} \cdot_{\beta} \vec{T}$ par $\vec{\varphi} \cdot_{\beta} \vec{T} = (\vec{\varphi} *_{\beta} \vec{T})(0)$ est vouée à l'échec.

## Deuxième contre-exemple.

Raisonnons encore sur le tore $\mathbf{T}^n$, au lieu de $\mathbb{R}^n$, pour simplifier. Soient E et F des espaces de Banach. Soient $\vec{\alpha} \in \mathfrak{D}^0(\mathbf{E})$, $\vec{\mu} \in \mathfrak{D}_c'^0(\mathbf{F})$. On peut définir, avec la proposition 39, leur produit de convolution $\vec{\alpha} *_{\pi} \vec{\mu} \in \mathfrak{D}'(\mathbf{E} \otimes_{\pi} \mathbf{F})$. Il est facile de voir que c'est une mesure. On pourrait appliquer en effet une proposition analogue à 38, mais s'appuyant sur la proposition 19 au lieu de la proposition 10, en prenant $\mathfrak{M} = \mathfrak{D}_c'^0$, $\mathfrak{K} = \mathfrak{D}^0$, $\mathcal{H} = \mathfrak{D}_c'^0$, $\mathscr{L} = \mathfrak{D}^0$, et en échangeant les rôles de E et F. L'injection de $\mathfrak{D}^0$ dans $\mathfrak{D}_c'^0$ est intégrale (puisqu'elle se factorise en $\mathfrak{D}^0 \to \mathbf{L}^\infty \to \mathbf{L}^1 \to \mathfrak{D}_b'^0 \to \mathfrak{D}_c'^0$).

Mais on peut définir autrement la précédente convolution. A partir de $\vec{\alpha} \in \mathfrak{D}^{0} \widehat{\otimes}_{\varepsilon} \mathrm{E}$, $\vec{\mu} \in \mathfrak{D}_{c}^{'0} \widehat{\otimes}_{\varepsilon} \mathrm{F}$, on peut définir (proposition 2) $\Gamma_{\varepsilon, \pi}(\vec{\alpha}, \vec{\mu}) \in (\mathfrak{D}^{0} \widehat{\otimes}_{\varepsilon} \mathfrak{D}_{c}^{'0}) \otimes_{\varepsilon} (\mathrm{E} \widehat{\otimes}_{\pi} \mathrm{F})$. L'application $\Gamma_{\varepsilon, \pi}$ est continue. Par ailleurs la convolution \* de $\mathfrak{D}^{0} \times \mathfrak{D}_{c}^{'0}$ dans $\mathfrak{D}_{c}^{'0}$ est $\varepsilon$-continue [en effet on peut la factoriser comme suit. On a la suite d'applications continues $\mathfrak{D}^{0} \times \mathfrak{D}_{c}^{'0} \to \mathfrak{D}^{0} \widehat{\otimes}_{\varepsilon} \mathfrak{D}_{c}^{'0} \to \mathfrak{D}_{b}^{'0} \widehat{\otimes}_{\pi} \mathfrak{D}_{c}^{'0}$, parce que $\mathfrak{D}^{0} \to L^{\infty} \to L^{1} \to \mathfrak{D}_{b}^{'0}$ est intégrale (proposition 16). Mais la convolution de $\mathfrak{D}_{b}^{'0} \times \mathfrak{D}_{c}^{'0}$ dans $\mathfrak{D}_{c}^{'0}$ est continue; car, si $\nu$ converge vers 0 dans $\mathfrak{D}_{c}^{'0}$, $\check{\nu} * \varphi$ converge vers 0 dans $\mathfrak{D}^{0}$, uniformément lorsque $\varphi$ parcourt un compact de $\mathfrak{D}^{0}$; alors, si $\lambda$ converge vers 0 dans $\mathfrak{D}_{b}^{'0}$, ($\lambda * \nu$)·$\varphi = \lambda \cdot (\check{\nu} * \varphi)$ convergera vers 0, la forme bilinéaire définissant la dualité étant continue sur $\mathfrak{D}_{b}^{'''} \times \mathfrak{D}^{0}$; alors $\lambda * \nu$ convergera bien vers 0 dans $\mathfrak{D}_{c}^{'0}$. Donc la convolution \* se prolonge en une application linéaire conti-

nue $\bar{\star}$ de $\mathfrak{D}_{b}^{\prime 0}\widehat{\otimes}_{\pi}\mathfrak{D}_{c}^{\prime 0}$ dans $\mathfrak{D}_{c}^{\prime 0}$. On a donc la suite d'applications linéaires continues:

$$
\begin{array}{c} \mathfrak {D} ^ {0} \times \mathfrak {D} _ {c} ^ {\prime 0} \longrightarrow \mathfrak {D} _ {b} ^ {\prime 0} \times \mathfrak {D} _ {c} ^ {\prime 0} \longrightarrow \mathfrak {D} _ {b} ^ {\prime 0} \widehat {\otimes} _ {\pi} \mathfrak {D} _ {c} ^ {\prime 0} \xrightarrow {\widetilde {*}} \mathfrak {D} _ {c} ^ {\prime 0}, \\ \Bigg \downarrow \quad \mathfrak {D} ^ {0} \widehat {\otimes} _ {\varepsilon} \mathfrak {D} _ {c} ^ {\prime 0} \Bigg \downarrow \end{array}
$$

d'où l'on retiendra seulement que la convolution \* se factorise en $\mathfrak{D}^{0}\times\mathfrak{D}_{c}^{\prime 0}\to\mathfrak{D}^{0}\widehat{\otimes}_{\varepsilon}\mathfrak{D}_{c}^{\prime 0}\xrightarrow{\overline{*}}\mathfrak{D}_{c}^{\prime 0}\big]$. Alors $(\ast\otimes\mathrm{I})\left(\Gamma_{\varepsilon,\pi}(\vec{\alpha},\vec{\mu})\right)$ est un élément de $\mathfrak{D}_{c}^{\prime 0}(\mathrm{E}\widehat{\otimes}_{\pi}\mathrm{F})$. L'application $(\ast\otimes\mathrm{I})\Gamma_{\varepsilon,\pi}$ est continue de $\mathfrak{D}^{0}(\mathrm{E})\times\mathfrak{D}_{c}^{\prime 0}(\mathrm{F})$ dans $\mathfrak{D}_{c}^{\prime 0}(\mathrm{E}\widehat{\otimes}_{\pi}\mathrm{F})$, et coïncide avec la convolution sur $(\mathfrak{D}^{0}\otimes\mathrm{E})\times(\mathfrak{D}_{c}^{\prime 0}\otimes\mathrm{F})$, donc partout. Ceci nous montre que la convolution précédente est même continue. Elle est enfin la restriction de la convolution de $\mathfrak{D}^{\prime}(\mathrm{E})\times\mathfrak{D}^{\prime}(\mathrm{F})$ dans $\mathfrak{D}^{\prime}(\mathrm{E}\widehat{\otimes}_{\pi}\mathrm{F})$, définie par le même procédé ou par la proposition 34 ou 39.

On pourrait naïvement s'attendre à ce que $\alpha *_{\pi} \mu$ fût même une fonction continue, pour $\vec{\alpha} \in \mathfrak{D}^0(E)$, $\mu \in \mathfrak{D}_c'^0(F)$, comme c'est le cas si E et F sont de dimension finie. Il n'en est rien ($\mathfrak{D}^0$ et $\mathfrak{D}_c'^0$ ne sont pas nucléaires, on ne peut pas leur appliquer la proposition 34).

En fait nous avons vu page 167 que, si $\vec{\alpha} \in \mathfrak{D}^{n}(\mathrm{E})$, $\mu \in \mathfrak{D}_{c}^{\prime 0}(\mathrm{F})$, alors $\vec{\alpha} *_{\pi} \mu$ est une fonction continue (F étant un espace de Banach, $\vec{\mathrm{T}}$ est sûrement bornée). Nous allons montrer que ce résultat ne peut pas être très amélioré. Nous allons donner un exemple explicite pour E, F, $\vec{\alpha}$, $\vec{\mu}$, avec $\vec{\alpha} \in \mathfrak{D}^{k}(\mathrm{E})$, $\vec{\mu} \in \mathfrak{D}_{c}^{\prime 0}(\mathrm{F})$, où $\vec{\alpha} *_{\pi} \vec{\mu}$ ne pourra être une fonction scalairement intégrable à valeurs dans E $\widehat{\otimes}_{\pi}$ F que si l'injection naturelle $\mathfrak{D}^{k+1} \to \mathfrak{D}^{0}$ est nucléaire; $\vec{\alpha} *_{\pi} \vec{\mu}$ ne sera donc sûrement pas, dans cet exemple, une fonction scalairement intégrable, si $k \leqslant n-2$, ou même si $k = n-1 = 0$ pour $n = 1$, d'après la remarque de la page 112. Le problème restera donc ouvert seulement pour $\vec{\alpha} \in \mathfrak{D}^{n-1}(\mathrm{E})$, $n > 1$ ($^{1}$).

Soit $\mathbf{E} = \mathfrak{D}^{\prime k + 1} = \mathfrak{D}_b^{\prime k + 1},\mathbf{F} = \mathfrak{D}^0.$

Prenons pour $\vec{\alpha} \in \mathfrak{D}^{k}(\mathfrak{D}^{'k+1})$ la fonction qui définit l'injection canonique $\mathbf{L}_{\vec{\alpha}}$ de $\mathfrak{D}_c^{'k}$ dans $\mathfrak{D}_b^{'k+1}$; cet opérateur est bien

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">n'y</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{D}_{\mathbf{T}}^{m + n + 1}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{D}_{\mathbf{T}^{n}}^{m}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Nous avons vu, à la proposition 23 bis, que l'injection de $\mathfrak{D}_{\mathbf{K}}^{m+n+1}$ dans $\mathfrak{D}_{\mathbf{H}}^{m}$ était nucléaire. Il est bien évident que, sur un tore, il n'y a pas de problèmes de supports, et que l'injection de $\mathfrak{D}_{\mathbf{T}^{n}}^{m+n+1}$ dans $\mathfrak{D}_{\mathbf{T}^{n}}^{m}$ est nucléaire. Nous laissons au lecteur le soin d'opérer partout ici ce genre de modifications.</span></small>

continu, comme transposé de l'identité, opérateur compact de $\mathfrak{D}^{k+1}$ dans $\mathfrak{D}^k$ (1). En tant que noyau, appartenant à $\mathfrak{D}_x'(\mathfrak{D}_\xi')$, $\vec{\alpha}$ n'est autre que $\delta(\hat{x}-\hat{\xi})$. Prenons pour $\vec{\mu} \in \mathfrak{D}_c^0(\mathfrak{D}^0)$ la distribution qui définit l'opérateur identique $\mathrm{L}_{\vec{\mu}}$ de $\mathfrak{D}^0$ dans $\mathfrak{D}^0$. En tant que noyau, appartenant à $\mathfrak{D}_x'(\mathfrak{D}_\eta')$, $\vec{\mu}$ n'est autre encore que $\delta(\hat{x}-\hat{\eta})$.

Alors $\vec{\alpha}_{\xi} \otimes \otimes_{\pi} \vec{\mu}_{\eta}$ définit l'application linéaire continue $\mathbf{L}_{\vec{\alpha}_{\xi} \otimes_{\pi} \vec{\mu}_{\eta}}$ de $\mathfrak{D}_{\xi, \eta}$ dans $\mathfrak{D}_{\xi}^{'k+1} \widehat{\otimes}_{\pi} \mathfrak{D}_{\eta}^{0}$, qui coïncide, sur $\mathfrak{D}_{\xi} \otimes \mathfrak{D}_{\eta}$, avec l'application identique. Comme $\mathfrak{D}^{0}$ a la propriété d'approximation, $\mathfrak{D}^{'k+1} \widehat{\otimes}_{\pi} \mathfrak{D}^{0}$ est un sous-espace de $\mathfrak{D}^{'k+1} \widehat{\otimes}_{\varepsilon} \mathfrak{D}^{0}$ (avec une topologie plus fine) (2), et on a les injections canoniques $\mathfrak{D}_{\xi, \eta} = \mathfrak{D}_{\xi} \widehat{\otimes}_{\pi} \mathfrak{D}_{\eta}(^{3}) \subset \mathfrak{D}_{\xi}^{'k+1} \widehat{\otimes}_{\pi} \mathfrak{D}_{\eta}^{0} \subset \mathfrak{D}_{\xi}^{'k+1} \widehat{\otimes}_{\varepsilon} \mathfrak{D}_{\eta}^{0} \subset \mathfrak{D}_{\xi}^{'} \widehat{\otimes}_{\varepsilon} \mathfrak{D}_{\eta}' = \mathfrak{D}_{\xi, \eta}'$, et $\mathbf{L}_{\vec{\alpha}_{\xi} \otimes_{\pi} \vec{\mu}_{\eta}}$ n'est autre que la première de ces injections, $\mathfrak{D}_{\xi, \eta} \to \mathfrak{D}_{\xi}^{'k+1} \widehat{\otimes}_{\pi} \mathfrak{D}_{\eta}^{0}$. La formule (II, 7; 8) qui définit la convolution montre alors que $\vec{\alpha} *_{\pi} \vec{\mu}$ est la distribution de $\mathfrak{D}_x(\mathfrak{D}_{\xi}^{'k+1} \widehat{\otimes}_{\pi} \mathfrak{D}_{\eta}^{0})$ telle que

$$
\begin{array}{l} \text {(II, 8; 6)} \\ \left(\vec {\alpha} * _ {\pi} \vec {\mu}\right) _ {x} \cdot \psi (x) = \psi (\hat {\xi} + \hat {\eta}) \in \mathfrak {D} _ {\xi} ^ {k + 1} \widehat {\otimes} _ {\pi} \mathfrak {D} _ {\eta} ^ {0}, \quad \text {et mème} \end{array} \quad \in \mathfrak {D} _ {\xi , \eta}.
$$

Supposons cette distribution $(\vec{\alpha} *_{\pi} \vec{\mu})_x$ définie par une fonction $\vec{f}(\hat{x})$, scalairement intégrable sur $T^n$ à valeurs dans $\mathcal{D}_{\xi}^{'k+1} \widehat{\otimes}_{\pi} \mathcal{D}_{\eta}^0$. Or, si on prend l'image $J(\vec{\alpha} *_{\pi} \vec{\mu})$ de $(\vec{\alpha} *_{\pi} \vec{\mu})$ par l'injection canonique $J$ de $\mathcal{D}_{\xi}^{'k+1} \widehat{\otimes}_{\pi} \mathcal{D}_{\eta}^0$ dans $\mathcal{D}_{\xi, \eta}'$, on obtient la distribution de $\mathcal{D}_x'(\mathcal{D}_{\xi, \eta}') : \psi(\hat{x}) \to \psi(\hat{\xi} + \hat{\eta})$; si $\vec{\alpha} *_{\pi} \vec{\mu}$ est une fonction $\vec{f}$, cette distribution sera définie par la fonction $(J \circ f)(\hat{x})$, scalairement intégrable sur $T^n$ à valeurs dans $\mathcal{D}_{\xi, \eta}'$. Or elle est effectivement définie par la fonction $\vec{g} \in \mathcal{D}_x(\mathcal{D}_{\xi, \eta}')$:

$$
(\mathrm{II}, 8; 7)
$$

$$
\vec {g} (x) = \delta (x - \hat {\xi} - \hat {\eta}),
$$

(1) Soient L et M des espaces vectoriels localement convexes. Si $u$ est une application linéaire continue de L dans M, transformant toute partie bornée en une partie d'enveloppe compacte, $^{t}u$ est continue de $\mathbf{M}_{c}^{\prime}$ dans $\mathbf{L}_{b}^{\prime}$, en vertu de la formule $^{t}u\big((u(\mathbf{B}))^{0}\big)\subset\mathbf{B}^{0}$, appliquée à toute partie bornée B de L ($\mathbf{B}^{0}$ est un voisinage de 0 de $\mathbf{L}_{b}^{0}$, $(u(\mathbf{B}))^{0}$ un voisinage de 0 de $\mathbf{M}_{c}^{\prime}$).

(2) GROTHENDIECK [4], §5, n°1, proposition 35, B₂; rappelons que B(F', E') admet F ∈ E comme sous-espace, et qu'en réalité il s'agit de l'application linéaire canonique de F ⊗π E dans F ∈ E ou même F ⊗ε E. Voir aussi SCHWARTZ [2], exposé 14, théorème 3, B₃.

(3) Nous avons vu que $\mathcal{E}_x\widehat{\otimes}_{\pi}\mathcal{E}_y = \mathcal{E}_{x,y}$ (chapitre 1, proposition 28), et, sur un tore, $\mathcal{E} = \mathfrak{D}$.

car on a bien (d'après le chapitre 1, page 106):

$$
\int_ {\mathbf {T} ^ {n}} \hat {\sigma} (x - \hat {\xi} - \hat {\eta}) \psi (x) d x = \psi (\hat {\xi} + \hat {\eta}) \in \mathfrak {D} _ {\xi , \eta} ^ {\prime}. \tag {II,8;8}
$$

Alors $\vec{g}$ et $J\circ\vec{f}$ définissent la même distribution en $x$ à valeurs dans $\mathfrak{D}_{\xi,\eta}^{\prime}$; comme le dual $\mathfrak{D}_{\xi,\eta}$ de $\mathfrak{D}_{\xi,\eta}^{\prime}$ est séparable, $\vec{g}(x)=(J\circ\vec{f})(x)$ pour presque toutes les valeurs de $x^{(1)}$. Cela prouve que $\delta(x-\hat{\xi}-\hat{\eta})\in\mathfrak{D}_{\xi,\eta}^{\prime}$ devra appartenir à $\mathfrak{D}_{\xi}^{\prime k+1}\widehat{\otimes}_{\pi}\mathfrak{D}_{\eta}^{0}$ pour presque toutes les valeurs de $x$.

Soit $x_0 \in \mathbf{T}^n$ un point tel que $\delta(x_0 - \hat{\xi} - \hat{\eta}) \in \mathfrak{D}_\xi^{lk+1} \pi \widehat{\otimes} \mathfrak{D}_\eta^0$. L'opération, définie par ce noyau, de $\mathfrak{D}_\xi^{lk+1}$ dans $\mathfrak{D}_\eta^0$ est

$$
\theta (\xi) \rightarrow \int_ {\mathbf {T} ^ {n}} \delta (x _ {0} - \xi - \hat {\eta}) \theta (\xi) d \xi = \theta (x _ {0} - \hat {\eta});
$$

cette opération devra être nucléaire, puisque

$$
\delta (x _ {0} - \hat {\xi} - \hat {\eta}) \in \mathfrak {D} _ {\xi} ^ {\prime k + 1} \widehat {\otimes} _ {\pi} \mathfrak {D} _ {\eta} ^ {0}.
$$

En composant l'opération précédente avec l'opération continue $\theta(x_0 - \hat{\eta}) \to \theta(\hat{\eta})$ de $\mathfrak{D}_\eta^0$ dans lui-même, on en déduira bien que l'injection canonique de $\mathfrak{D}^{k+1}$ dans $\mathfrak{D}^0$ est nucléaire, ce qui prouve notre affirmation du début: pour $k = n - 2$, $n > 1$, ou pour $k = n - 1 = 0$, $n = 1$, nous avons donné un exemple, où $\vec{\alpha} \in \mathfrak{D}^k(E)$, $\vec{\mu} \in \mathfrak{D}_c'^0(F)$, et où $\vec{\alpha} *_{\pi} \vec{\mu}$ n'est pas une fonction.

Toute tentative, dans ce cas, pour définir le produit scalaire $\vec{\varphi} \cdot_{\pi} \vec{\mu} \in (\mathrm{E} \widehat{\otimes}_{\pi} \mathrm{F})$, $\vec{\varphi} \in \mathfrak{D}^k(\mathrm{E})$, $\vec{\mathrm{T}} \in \mathfrak{D}_c'^0(\mathrm{F})$, par $\vec{\varphi} \cdot_{\pi} \vec{\mu} = (\vec{\varphi} *_{\pi} \vec{\mu})(0)$, est donc vouée à l'échec, puisque le second membre n'a pas de sens. Voilà donc un cas où on ne peut sûrement pas définir un produit scalaire « raisonnable » ($\vec{\varphi}$, $\vec{\mu}$) → $\vec{\varphi} \cdot_{\pi} \vec{\mu}$ sur $\mathfrak{D}^0(\mathrm{E}) \times \mathfrak{D}_c'^0(\mathrm{F})$ ou même sur $\mathfrak{D}^k(\mathrm{E}) \times \mathfrak{D}_c'^0(\mathrm{F})$.

Au contraire, comme nous l'avons vu en passant, $J(\vec{\alpha} *_{\pi} \vec{\mu})$ est une fonction indéfiniment dérivable $\delta(x - \hat{\xi} - \hat{\eta})$, à valeurs dans $\mathfrak{D}_{\xi,\eta}' = \mathfrak{D}_{\xi}' \widehat{\otimes}_{\pi} \mathfrak{D}_{\eta}'$. Mais ici il n'y avait aucune difficulté, car $J\vec{\alpha}$, considérée comme distribution à valeurs dans $\mathfrak{D}_{\xi}'$, est une fonction indéfiniment dérivable, donc la proposition 34 montrait bien que $J\vec{\alpha} *_{\pi} J\vec{\mu}$ est une fonction indéfiniment dérivable. Dans ce cas la formule (II, 7; 4 bis) était valable.

(1) Voici chapitre 1, remarque $2^{\circ}$, page 66.

Troisième contre-exemple.

Plaçons-nous toujours sur le tore $\mathbf{T}^{n}$. Soient E et F des espaces de Banach, $\vec{\mu}$ et $\vec{\nu}$ des mesures sur $\mathbf{T}^{n}$ à valeurs dans E et F respectivement: $\vec{\mu} \in \mathfrak{D}_{c}^{'0}(\mathbf{E})$, $\vec{\nu} \in \mathfrak{D}_{c}^{'0}(\mathbf{F})$. On sait alors que $\vec{\mu} *_{\pi} \vec{\nu}$ est dans $\mathfrak{D}_{c}^{'n}(\mathbf{E} \widehat{\otimes}_{\pi} \mathbf{F})$. C'est en effet ce qui indique la proposition 38, exemple $4^{0}$ page 163 (F étant un espace de Banach. $\vec{T}$ est bien bornée). En outre, si $\vec{\mu}$ converge vers 0 dans $\mathfrak{D}_{c}^{'n}(\mathbf{E})$, et si $\vec{\nu}$ reste dans une partie bornée de $\mathfrak{D}_{c}^{'0}(\mathbf{F})$, $\vec{\mu} *_{\pi} \vec{\nu}$ converge vers 0; mais par suite de la symétrie des rôles de $\vec{\mu}$ et $\vec{\nu}$ (les deux produits de convolution qu'on peut définir en échangeant les rôles de $\vec{\mu}$ et $\vec{\nu}$ coïncident, parce qu'ils sont tous deux la restriction de la convolution de $\mathfrak{D}'(\mathbf{E}) \times \mathfrak{D}'(\mathbf{F})$ dans $\mathfrak{D}'(\mathbf{E} \widehat{\otimes}_{\pi} \mathbf{F})$, définie par la proposition 34 ou 39), on en déduit que la convolution de $\mathfrak{D}_{c}^{'0}(\mathbf{E}) \times \mathfrak{D}_{c}^{'0}(\mathbf{F})$ dans $\mathfrak{D}_{c}^{'n}(\mathbf{E} \widehat{\otimes}_{\pi} \mathbf{F})$ est hypocontinue par rapport aux parties bornées.

Peut-on remplacer ici $n$ par $k < n$? Nous l'ignorons. Mais nous allons montrer qu'on ne peut sûrement pas le remplacer par 0; le produit de convolution de 2 mesures à valeurs dans E et F respectivement n'est pas nécessairement une mesure à valeurs dans $\mathbf{E} \widehat{\otimes}_{\pi} \mathbf{F}$. Plus précisément, soient $\mathbf{E} = \mathfrak{D}^{0}$, $\vec{\mu} \in \mathfrak{D}_{c}^{\prime 0}(\mathfrak{D}^{0})$ la mesure telle que $\mathbf{L}_{\vec{\mu}}$ soit l'application identique de $\mathfrak{D}^{0}$; et soient $\mathbf{F} = \mathfrak{D}^{0}$, $\vec{\nu} \in \mathfrak{D}_{c}^{\prime 0}(\mathfrak{D}^{0})$ la mesure telle que $\mathbf{L}_{\nu}$ soit la symétrie $\vee$ de $\mathfrak{D}^{0}$ dans lui-même. Nous allons montrer que, si $\vec{\mu} *_{\pi} \vec{\nu}$ est dans $\mathfrak{D}_{c}^{\prime k}(\mathbf{E} \widehat{\otimes}_{\pi} \mathbf{F})$, alors toute distribution S, telle que la convolution $\{\mathbf{S}\}$ opère continuement de $\mathfrak{D}^{0}$ dans $\mathfrak{D}_{b}^{\prime 0}$ est d'ordre $\leqslant k$.

Malheureusement, nous ne connaissons pas l'ordre maximum $k_{\mathrm{M}}$ de telles distributions S: on a sûrement $k \geqslant k_{\mathrm{M}}$. Pour $n = 1$, la convolution avec $\wp p \cot \frac{1}{\hat{x}}$ opère continuement de $\mathbf{L}^2$ dans $\mathbf{L}^2$, donc à fortiori de $\mathfrak{D}^0$ dans $\mathfrak{D}_b^{\prime 0}$, or cette distribution est d'ordre 1 et non d'ordre 0; donc, pour $n = 1$, $k = 0$ est impossible, et comme $k = 1$ est possible, le problème est complètement résolu pour la dimension 1. Pour la dimension $n$,

$$
\mathrm{S} = \nu p \cot \mathrm{g} \frac {1}{\hat {x} _ {1}} \otimes \nu p \cot \mathrm{g} \frac {1}{\hat {x} _ {2}} \otimes \dots \otimes \nu p \cot \mathrm{g} \frac {1}{\hat {x} _ {n}},
$$

n'est pas non plus d'ordre 0, mais nous ignorons son ordre

effectif $k_0$; on peut montrer aisément que $k_0 \leqslant \left[\frac{n}{2}\right] + 1$ (car les coefficients de Fourier de S sont bornés, donc S est somme de dérivées d'ordre $\leqslant \left[\frac{n}{2}\right] + 1$ de fonctions de L², donc d'ordre $\leqslant \left[\frac{n}{2}\right] + 1$), ce qui ne nous dit pas grand'chose; quoiqu'il en soit, on a sûrement $k \geqslant k_0$. On peut former (¹) une distribution S d'ordre effectif $k_1 = \left[\frac{n - 1}{2}\right]$, dont les coefficients de Fourier sont bornés, et telle par conséquent que {S} opère continuement de L² dans L², et par suite à fortiori de $\mathfrak{D}^0$ dans $\mathfrak{D}_b^{0}$; on a donc sûrement $k \geqslant k_1 = \left[\frac{n - 1}{2}\right]$, ce qui est très loin de n.

Démontrons donc notre assertion. Nous avons vu, au 1er contre-exemple, que $\vec{\mu} *_{\pi} \vec{\nu}$, en tant que distribution à valeurs dans $\mathfrak{D}_{\xi}' \widehat{\otimes}_{\pi} \mathfrak{D}_{\eta}'$, est $\delta(\hat{x} - \hat{\xi} + \hat{\eta})$. Elle est une fonction indéfiniment dérivable de $x$ à valeurs dans $\mathfrak{D}_{\xi, \eta}'$, donc à fortiori distribution d'ordre $\leqslant k$, et sa valeur pour $\varphi(\hat{x}) \in \mathfrak{D}^k$ est $\varphi(\hat{\xi} - \hat{\eta}) \in \mathfrak{D}_{\xi, \eta}'$. Il s'agit donc de savoir s'il est possible que, pour toute $\varphi \in \mathfrak{D}^k$, $\varphi(\hat{\xi} - \hat{\eta})$ soit dans $\mathfrak{D}_{\xi}^0 \widehat{\otimes}_{\pi} \mathfrak{D}_{\eta}^0 \subset (^2) \mathfrak{D}_{\xi}^0 \widehat{\otimes}_{\varepsilon} \mathfrak{D}_{\eta}^0 \subset \mathfrak{D}_{\xi, \eta}'$.

Mais, en tant que noyau, $\varphi\big(\hat{\xi}-\hat{\eta}\big)$ définit l'opération de convolution avec $\varphi$; si $\varphi\big(\hat{\xi}-\hat{\eta}\big)\in\mathfrak{D}_{\xi}^{0}\widehat{\otimes}_{\pi}\mathfrak{D}_{\eta}^{0}$, cette opération doit être nucléaire de $\mathfrak{D}_{b}^{'0}$ dans $\mathfrak{D}^{0}$. Donc, si $\vec{\mu}*\vec{\nu}\in\mathfrak{D}_{c}^{'k}(E\widehat{\otimes}_{\pi}F)$, la convolution $\{\varphi\}$ doit être nucléaire de $\mathfrak{D}_{b}^{'0}$ dans $\mathfrak{D}^{0}$, pour toute $\varphi\in\mathfrak{D}^{k}$. Soit alors S une distribution telle que la convolution $\{S\}$ soit continue de $\mathfrak{D}^{0}$ dans $\mathfrak{D}_{b}^{'0}$; alors la convolution $\{S*\varphi\}$:

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\geqslant 0$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$D^{p}\tau, |p| \leqslant \frac{n - 1}{2}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Soit en effet $\tau$ une mesure $\geqslant 0$ répartie de manière homogène sur la surface d'une sphère de $R^n$, de centre 0. On sait (voir SCHWARTZ [8]) que son image de Fourier est bornée, à l'infini, par une quantité de l'ordre de $\left(\frac{1}{r}\right)^{\frac{n-1}{2}}$. Donc toute dérivée $D^{p}\tau$, $|p| \leqslant \frac{n-1}{2}$, est une distribution d'ordre exactement $|p|$, d'image de Fourier bornée; la périodifiée $D^{p}\tilde{\tau}$ de $D^{p}\tau$, de période 1 par rapport à toutes les coordonnées (c'est-à-dire la somme de toute les translatées de translations entières), définit une distribution d'ordre $|p|$ sur le tore, dont les coefficients de Fourier sont bornés.<br><br>(2) Rappelons que cette relation d'inclusion résulte, par exemple, de ce que $\mathcal{D}^0$ à la propriété d'approximation (voir note (2), page 88).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$D^{p\tilde{\tau}}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\left(\frac{1}{r}\right)^{\frac{n-1}{2}}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">|p|</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">|p|</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">D$^{0}$</span></small>

$\mathfrak{D}^{0}\xrightarrow{\{\mathrm{S}\}}\mathfrak{D}_{b}^{\prime 0}\xrightarrow{\{\varphi\}}\mathfrak{D}^{0}$ sera nucléaire; d'après la proposition 23, $\mathrm{S}*\varphi$ devra être une fonction continue. S est donc une distribution telle que, pour toute $\varphi\in\mathfrak{D}^{k}$, $\mathrm{S}*\varphi$ soit une fonction continue: S est donc d'ordre $\leqslant k(1)$. Nous avons donc bien montré que, si $\vec{\mu}*\vec{\pi}\vec{\nu}\in\mathfrak{D}_{c}^{\prime k}(\mathrm{E}\widehat{\otimes}_{\pi}\mathrm{F})$, toute distribution S telle que $\{\mathrm{S}\}$ opère continuement de $\mathfrak{D}^{0}$ dans $\mathfrak{D}_{b}^{\prime 0}$, est d'ordre $\leqslant k$.

(1) SCHWARTZ [5], chapitre vi, § 7, remarque $1^{\circ}$, page 49.

# INDEX TERMINOLOGIQUE

Nous écrivons : page 75 (I), ou page 75 (II), selon qu'il s'agit de la page 75 du chapitre 1 ou du chapitrc 11.

## Convexité.

Un ensemble convexe d'un espace vectoriel sur le corps des réels ou des complexes est un ensemble qui, toutes les fois qu'il contient deux points, contient le segment qui les joint (BOURBAKI [1], chapitre II, § 1, n° 1 page 42).

Un espace vectoriel topologique sur le corps des réels ou des complexes est dit localement convexe, s'il a un système fondamental de voisinages de 0 convexes (BOURBAKI [1], chapitre II, § 2, n° 1, page 57); sa topologie est alors définie par une famille de semi-normes (BOURBAKI [1], chapitre II, § 5, n° 4, page 95)

Un ensemble équilibré d'un espace vectoriel sur un corps valué K, est un ensemble qui, toutes les fois qu'il contient un élément x, contient tous les éléments  $\lambda x, \lambda \in K, |\lambda| \leqslant 1$  (BOURBAKI [1], chap. 1, § 1, n° 3, définition 2, page 5).

Un ensemble disqué d'un espace localement convexe est un ensemble convexe équilibré fermé.

L'enveloppe convexe (resp. convexe équilibrée) d'une partie d'un espace vectoriel sur le corps des réels ou des complexes est la plus petite partie convexe (resp. convexe équilibrée) qui la contienne (BOURBAKI [1], chap. 1, § 1, n° 3, page 6; chap. 11, § 1, n° 3, page 45).

L'enveloppe d'une partie d'un espace localement convexe est la plus petite partie disquée qui la contienne. « Enveloppe » est donc une abréviation de « enveloppe disquée ».

Soit A une partie d'un espace vectoriel E sur le corps des réels ou des complexes; supposons A convexe, équilibrée, absorbante (voir plus bas). On appelle jauge de A la semi-norme p définie par

$$
p (x) = \left(\underset {\lambda x \in \Lambda} {\operatorname{Sup}} | \lambda |\right) ^ {- 1} \quad (\text { Bourbaki,   chap.   II,   } \S 5, \text { n°   3,   page   95 }).
$$

## Ensembles de parties bornées d'un espace vectoriel localement convexe.

Soient A et B deux parties d'un espace vectoriel E sur le corps des réels ou des complexes. On dit que A absorbe B, s'il existe un scalaire λ tel que λA⊃B. Une partie de E est dite absorbante, si elle absorbe toute partie réduite à un point.

Une partie d'un espace localement convexe E est dite bornée si elle est absorbée par tout voisinage de 0 (BOURBAKI [2], chap. III, § 2, n° 1, déf. 1, page 4).

L'enveloppe d'une partie bornée est bornée.

Un système fondamental C de parties bornées est un ensemble de parties bornées tel que toute partie bornée de E soit contenue dans une partie appartenant à C.

Un ensemble $\mathfrak{G}$ de parties bornées est dit saturé, si, toutes les fois que A et B appartiennent à $\mathfrak{G}$, il en est de même de $\lambda$A, $\lambda$ scalaire, ainsi que de toutes les parties contenues dans A. de l'enveloppe de A, et de la réunion A $\cup$ B, et si en outre toute partie réduite à un point appartient à $\mathfrak{G}$.

Les $\lambda$-parties ($\lambda = \iota, \gamma, \beta, \pi, \varepsilon$), et les parties $\sigma$-$\tau$-décomposables sont définies page 15 (II).

Adhérence stricte, parties strictement denses, parties quasi-fermées d'un espace localement convexe.

Une partie A d'un espace localement convexe E est dite quasi-fermée, si tout point de E, adhérent à une partie bornée de A, appartient à A. L'adhérence stricte de A dans E est la plus petite partie quasi-fermée contenant A; un point de E est strictement adhérent à A, s'il appartient à son adhérence stricte; A est strictement dense dans E si son adhérence stricte est E.

(Schwartz [1], Introduction, pages 90, 92).

Espaces complets, quasi-complets; parties complétantes.

Un espace uniforme est complet, si tout filtre de Cauchy est convergent (BOURBAKI [5], chap. II, § 3, n° 1, déf. 4, page 147).

Un espace localement convexe est quasi-complet si toute partie fermée bornée est complète. Pour les propriétés essentielles des espaces quasi-complets, voir SCHWARTZ [1], Introduction, pages 90, 92.

Une partie A d'un espace localement convexe E est dite complétante, s'il existe une partie convexe équilibrée B ⊃ A, coupant toute droite issue de l'origine suivant un segment fermé, et telle que l'espace normé  $E_{B}$  (espace vectoriel normé engendré par B, et ayant B comme boule unité) soit complet. Toute partie contenue dans une partie complétante est complétante; l'enveloppe convexe équilibrée d'une partie complétante est complétante (mais son adhérence ne l'est pas nécessairement).

Toute partie A, bornée disquée complète, est complétante, et même  $E_{A}$  est complet (BOURBAKI [2], démonstration du lemme 1, chap. III, § 3, n° 4, page 21).

Si E est quasi-complet, toute partie bornée est complétante.

Soit E localement convexe; si A est bornée disquée complétante,  $E_{A}$  est complet (car soit B ⊃ A tel que  $E_{B}$  soit complet; A est bornée disquée dans  $E_{B}$  complet, donc  $E_{A}$  est complet). Cette propriété ne subsiste pas nécessairement si A est seulement convexe équilibrée bornée complétante.

Soit A une partie bornée complétante de E. Parmi les parties B ⊃ A telles que  $E_{B}$  soit complet, il en existe au moins une  $B_{1}$  qui soit contenue dans l'enveloppe de A. Si en effet  $A_{1}$  est cette enveloppe,  $A_{1} \cap B$  est disquée bornée dans  $E_{B}$  complet, donc  $E_{A_{40B}}$  est complet, et on peut prendre  $B_{1} = A_{1} \cap B$ .

Si A est une partie complétante de E, u une application linéaire de E dans F telle que l'image par u de l'enveloppe de A soit bornée, alors  $u(\mathbf{A})$  est

complétante dans F. En effet soit B ⊃ A une partie contenue dans l'enveloppe de A, telle que  $E_{B}$  soit complet. L'espace  $F_{u(B)}$  est exactement l'espace normé quotient de  $E_{B}$  par le noyau de la restriction de u à  $E_{B}$  (comme u(B) est bornée,  $F_{u(B)}$  est séparé, donc le noyau est nécessairement fermé); donc  $F_{u(B)}$  est complet, et u(B), donc u(A), est complétante. En particulier, l'image d'une partie complétante par une application linéaire continue (ou transformant toute partie bornée en une partie bornée) est complétante. On en déduit que, pour qu'une partie de E soit complétante, il faut et il suffit qu'elle soit contenue dans l'image de la boule unité d'un Banach par une application continue (c'est nécessaire, car si A est complétante et si B ⊃ A est telle que  $E_{B}$  un soit Banach, A est contenue dans l'image de la boule unité de  $E_{B}$  par  $E_{B} \rightarrow E$ ; c'est suffisant d'après ce que nous venons de voir).

Si $\mathfrak{G}$ est un ensemble saturé de parties bornées de E, E est dit $\mathfrak{G}$-quasi-complet (resp. $\mathfrak{G}$-complétant), si toute partie appartenant à $\mathfrak{G}$ a une adhérence complète (resp. complétante).

Applications linéaires continues et homomorphismes.

Une application $u$ de E dans F est injective, si l'image réciproque d'un point ne contient pas plus d'un point; épijective ou surjective si $u(\mathrm{E}) = \mathrm{F}$; bijective si elle est injective et épijective.

Une application linéaire d'un espace vectoriel topologique E dans un espace vectoriel topologique F est un isomorphisme, si elle est bijective et si elle est un isomorphisme de la structure d'espace vectoriel topologique; elle est un monomorphisme, si elle est un isomorphisme de E sur $u(E)$, un épimor-

phisme si elle définit un isomorphisme de $\mathrm{E} / u(0)$ sur $\mathbf{F}$; un homomorphisme, si elle définit un isomorphisme de $\mathrm{E} / u(0)$ sur $u(\mathbf{E})$.

Applications continues, hypocontinues; bornées, compactes.

Application bilinéaires $\mathfrak{S}$-$\mathfrak{G}$-hypocontinues: page 9 (II).

Applications bilinéaires $\lambda$-continues ($\lambda = \iota, \gamma, \beta, \pi, \varepsilon$): page 13 (II).

Applications multilinéaires ε-hypocontinues : page 3 (I).

Quand on écrit hypocontinue, sans autre précision, cela veut dire hypo- continue par rapport aux parties bornées.

Une application linéaire u d'un espace localement convexe E dans un espace localement convexe F est dite bornée (resp. compacte), s'il existe un voisinage de 0 de E dont l'image par u soit bornée (resp. relativement compacte).

Soit $\mathfrak{G}$ un ensemble de parties bornées de F. Une application linéaire $u$ de E dans F est $\mathfrak{G}$-bornée, s'il existe un voisinage de 0 de E dont l'image par $u$ appartient à $\mathfrak{G}$. On définit de même les ensembles équibornés, $\mathfrak{G}$-équibornés, d'application linéaires de E dans F [page 83 (I)].

Diverses topologies sur un espace localement convexe et son dual. Polarité. Soit E un espace localement convexe, E' son dual. La topologie affaiblie  $\sigma(\mathrm{E}, \mathrm{E}')$ , la topologie faible  $\sigma(\mathrm{E}', \mathrm{E})$ , sont définies dans BOURBAKI [2], chap. IV, § 2, n° 1, page 63; la topologie τ de Mackey est définie dans BOURBAKI [2], chap. IV, § 2, n° 3, page 69; la topologie forte sur E' est définie dans

BOURBAKI [2], chap. iv, § 3, n° 1, page 85; la topologie $\gamma = (\mathrm{E}_{c}^{\prime})_{c}^{\prime}$ sur E est définie ici page 17 (I).

Si $A \subset E$, son polaire $A^0$ est l'ensemble des $\vec{e'} \in E'$, tels que $\langle \vec{e'}, \vec{e} \rangle \leqslant 1$ pour tout $e \in A$. Le bipolaire $A^{00}$ est $(A^0)^0$; c'est l'enveloppe de $A$ pour la topologie $\sigma(E, E')$ (BOURBAKI [2], chap. iv, § 1, n° 3, prop. 3, page 52).

Limites inductives.

Soit E un espace vectoriel, réunion d'une famille  $(\mathrm{E}_{i})_{i\in I}$  d'espaces localement convexes; on suppose que l'ensemble d'indices I est ordonné filtrant, et que, pour  $j\geqslant i$, on a  $E_{i}\subset E_{j}$, la topologie de  $E_{i}$  étant plus fine que la topologie induite par  $E_{j}$. La limite inductive des topologies des  $E_{i}$  est la topologie localement convexe la plus fine sur E, qui, sur chaque  $E_{i}$, induise une topologie moins fine que la sienne (BOURBAKI [1] chap. II, § 2, n° 4, page 61). On dit que E est limite inductive stricte des  $E_{i}$, si I est dénombrable et si, pour  $j\geqslant i$, la topologie de  $E_{i}$  est identique à la topologie induite par  $E_{j}$.

On montre alors que la topologie limite inductive de E induit sur chaque  $E_{i}$  sa propre topologie (DIEUDONNÉ-SCHWARTZ [1], proposition 2, page 68).

Applications intégrales et nucléaires, espaces nucléaires.

Application nucléaire de E dans F: GROTHENDIECK [4], § 3, n° 2, déf.

Application intégrale de E dans F: GROTHENDIECK [4], § 4, n° 3, déf. 7.2, page 127; SCHWARTZ [2], exposé 16, page 3).

Application sous-nucléaire, sous-intégrale : page 54 (II).

Espaces nucléaires : GROTHENDIECK [5], § 2, n° 1, déf. 4, page 34; Schwartz [2], exposé 17, page 2).

## Les produits tensoriels topologiques.

Indépendamment des définitions données dans GROTHENDIECK [4] et SCHWARTZ [2], on trouvera ici, page 10 (II), la définition de la topologie $\otimes_{\mathfrak{S},\mathfrak{G}}$, et des 5 topologies $\iota$, $\gamma$, $\beta$, $\pi$, $\varepsilon$, sur un produit tensoriel.

Parties σ-τ-décomposables d'un produit tensoriel complété: page 15 (II).

## Tonneaux, espaces tonnelés.

Un tonneau d'un espace localement convexe est un ensemble disqué absorbant; un espace localement convexe est tonnelé, si tout tonneau est un voisinage de 0 (BOURBAKI [2], chap. III, § 1, n° 1, déf. 1, page 1).

Un espace localement convexe est infra-tonnelé, si tout tonneau absorbant toutes les parties bornées est un voisinage de 0. Un espace tonnelé est infra-tonnelé; un espace quasi-complet infra-tonnelé est tonnelé. Un espace bornologique est infra-tonnelé; un espace ultra-bornologique est tonnelé.

## Espaces bornologiques.

Un espace localement convexe est bornologique, si toute partie convexe équilibrée, absorbant toutes les parties bornées, est un voisinage de 0 (BourBAKI [4], page 11).

Un espace localement convexe est ultra-bornologique s'il est limite induc-

tive d'espaces de Banach (voir page 43 (I)). Un espace ultrabornologique est bornologique et tonnelé; un espace bornologique et quasi-complet est ultrabornologique.

## Espaces de Montel.

Un espace de Montel est un espace localement convexe tonnelé, où les parties bornées sont relativement compactes (BOURBAKI [2], chap. iv, § 3, n° 4, page 89).

## Espaces de Schwartz.

Un espace de Schwartz est un espace localement convexe E tel que, pour tout voisinage disqué U de 0, il en existe un autre V, dont l'image dans Eq (Eq est l'espace normé séparé, associé à l'espace E muni de la seule semi-norme jauge de U) soit précompacte (GROTHENDIECK [2], déf. 5, page 117).

Espaces de Fréchet, espaces (LF), espaces (DF).

Un espace de Fréchet est un espace localement convexe, à base déombrable de voisinages de 0 et complet (BOURBAKI, chap. II, § 2, n° 1, page 59).

Un espace $\mathscr{L}\mathscr{F}$ est une limite inductive stricte d'espaces de Fréchet (Dieudonné-Schwartz [1]).

Un espace (DF) est un espace, ayant une base dénombrable de parties bornées, et tel que toute partie bornée du dual, contenue dans une réunion dénombrable de parties équicontinues, soit encore équicontinue (GROTHENDIECK [4], déf. 1, page 63).

Le dual d'un espace de Fréchet est un espace (DF); le dual d'un espace (DF) est un espace de Fréchet.

Un espace de Banach est un espace normé complet.

## Recouvrements, partition de l'unité.

Un recouvrement ouvert d'un espace topologique X est une famille  $(\mathrm{O}_{i})_{i\in\mathbf{I}}$  d'ouverts de X, dont la réunion est X.

Le recouvrement ouvert $(\mathrm{O}_i)_{i\in \mathbf{I}}$ est dit subordonné au recouvrement ouvert $(\mathrm{O}_i^{\prime})_{i\in \mathbf{I}}$ (correspondant au même ensemble d'indices), si, pour tout $i\in \mathbf{I}$, $\overline{\mathrm{O}_i}$ est contenu dans $\mathrm{O}_i^{\prime}$.

Une partition de l'unité sur X, subordonnée à un recouvrement ouvert  $(\mathrm{O}_{i})_{i\in\mathbf{I}}$ , est une famille de fonctions continues  $(\alpha_{i})_{i\in\mathbf{I}}$ , correspondant au même ensemble d'indices, et telle que: a)  $\alpha_{i}\geqslant0$ ; b) l'adhérence de l'ensemble des points où  $\alpha_{i}\neq0$  est contenu dans  $O_{i}$ ; c) la somme  $\sum_{i}\alpha_{i}$  vaut 1, chaque point de X possédant un voisinage où tous les termes de cette somme, sauf un nombre fini, sont nuls.

## Propriétés d'approximation et de densité; espaces de distributions.

Propriété d'approximation et d'approximation stricte, pour un espace localement convexe, page 5 (I); propriété d'approximation équicontinue ou métrique : page 72 (II); voir aussi GROTHENDIECK [4], § 5, n° 2, page 178.

Espaces de distributions, espaces normaux et strictement normaux: page 7 (1).

Propriété d'approximation par troncature ou par régularisation: page 7 (I).
Propriété (ε) d'un espace de distributions: page 53 (I).
Distributions sommables: page 126 (I).

Distributions bornées, ℰ-bornées.

Distribution bornée, G-bornée, ensemble équiborné ou G-équiborné de distributions, distribution localement bornée ou G-bornée : pages 83 (I) et 54 (II).

Distributions du type S, parties du type S d'un espace de distribution : page 53 (II).

Noyaux ; régularité et compacité.

Définition des noyaux : page 90 (I).

Noyaux semi-réguliers, réguliers, régularisants : page 99 (I).

Noyaux semi-compacts, compacts, compactifiants: page 100 (I).

Distributions semi-tempérées : page 123 (I).

Distributions partiellement sommables: page 130 (I).

Les espaces usuels de distributions $\mathcal{D}, \mathcal{D}^{m}, \mathcal{D}^{\prime}, \mathcal{D}^{\prime m}, \mathcal{D}^{\prime}_{+}, \mathcal{E}, \mathcal{E}^{m}, \mathcal{E}^{\prime}, \mathcal{E}^{\prime m}, L^{p}, \mathcal{D}_{L^{p}}, \mathcal{B}^{*}, \mathcal{B}, \mathcal{B}^{\prime}, \mathcal{I}, \mathcal{I}^{\prime}, \mathcal{O}_{\mathrm{M}}, \mathcal{O}_{c}^{\prime}$, sont ceux qui sont définis dans Schwartz [4] et [5] (voir index des notations à la fin de [5]); on peut y ajouter $\mathcal{O}_{\mathrm{M}}^{\prime}$ et $\mathcal{O}_{c}$, duals forts respectifs de $\mathcal{O}_{\mathrm{M}}$ et $\mathcal{O}_{c}^{\prime}$. $\mathcal{I}^{\prime}(\Gamma)$ est défini dans Schwartz [3]. Les espaces $\mathcal{X}, \mathcal{X}^{\prime}$, sont définis page 77 (I). $\mathcal{Q}_{c}^{\prime m}$ (resp. $\mathcal{E}_{c}^{\prime m}$) est l'espace $\mathcal{P}^{\prime m}$ (resp. $\mathcal{E}^{\prime m}$), muni de la topologie de la convergence uniforme sur les parties compactes de $\mathcal{D}^{m}$ (resp. $\mathcal{E}^{m}$). Les espaces $\mathcal{L}^{1}, \mathcal{K}^{\infty}$, sont définis pages 111 et 112 (I), l'espace $\mathcal{L}^{p}$ page 48 (II). Les espaces $(\mathcal{K}^{1})^{(-m)}$ et $(\mathcal{L}_{c}^{\infty})^{(m)}$ sont définis page 165 (II) et suivantes. La transformation de Fourier se note $\mathcal{F}$.

Les espaces $\mathcal{H}(\mathrm{E})$ sont définis page 49 (I) (pour $\mathcal{H} = \mathfrak{D}^{\prime m}$) et 52 (I). Les espaces $\mathcal{H}(\overline{\mathrm{E}})$ sont définis page 61 (I) (pour $\mathcal{H} = \mathcal{E}^{\prime m}$), page 63 (I) (pour $\mathcal{H} = \mathfrak{D}^{m}$), page 48 (II) (pour $\mathcal{H} = \mathbf{L}^{p}$ ou $\mathcal{L}^{p}$).

La notation $\mathcal{H}_{c}^{\prime}(\mathrm{E};\mathfrak{G})$ est définie page 54 (II), la notation $\mathcal{H}(\mathrm{E}_{\mathfrak{G}})$ page 54 (II),

On adopte la notation de la variable muette marquée par un $\wedge$ quand elle n'est écrite qu'une fois: $f(\hat{x})$ pour la fonction $x\to f(x)$, ou $\mathrm{S}(\hat{x})$ pour la distribution $\mathrm{S}_x\in \mathfrak{D}'_x$ (pages 2 (II), 71 (I)).

La distribution définie par la masse unité au point $a$ de $\mathbf{R}^{n}$ se note $\delta_{(a)}$, ou $\delta_{x-a}$, ou $\delta(\hat{x}-a)$, ou $\varepsilon(a)$.

La symétrie par rapport à l'origine de $\mathbf{R}^n$ se note par $\nu$; $\check{f}$, $\check{T}$, sont les symétriques de la fonction $f$, de la distribution T; elles sont définies par: $\check{f}(x) = f(-x)$; $\check{T}(\varphi) = T(\check{\varphi})$. Si $\mathcal{H}$ est un espace de distributions, on notera par $\check{\mathcal{H}}$ l'espace de distributions obtenu par cette symétrie (sous disons: espace de distributions, ce qui veut dire qu'il a une topologie, obtenue à partir de celle de $\mathcal{H}$ par symétrie).

$\tau_{h}$  est la translation de  $R^{n}$  par le vecteur h;  $\tau_{h}f$  est la translatée de la fonction f, définie par  $(\tau_{h}f)(x)=f(x-h)$ ;  $\tau_{h}T$  est la translatée de la distribution T, définie par  $(\tau_{h}T)(\varphi)=T(\tau_{-h}(\varphi))$ .

Le symétrique  ${}^{s}$ K d'un noyau K est défini page 90 (I).

Les notations $\mathbf{L}_{\varepsilon}\mathbf{M},\varepsilon (\mathbf{L}_i;\mathbf{M})$ , sont définies page 18 (I).

$\mathcal{L}(\mathrm{E};\mathrm{F})$ est l'espace des applications linéaires continues de E dans F; $\mathcal{L}_{c}(\mathrm{E};\mathrm{F})$ (resp. $\mathcal{L}_{b}(\mathrm{E};\mathrm{F})$, resp. $\mathcal{L}_{s}(\mathrm{E};\mathrm{F})$) veut dire qu'il est muni de la topologie de la convergence uniforme sur les parties convexes équilibrées compactes de E (resp. sur les parties bornées, resp. de la topologie de la convergence simple). $\mathcal{L}_{i}(\mathrm{L}_{c}^{\prime};\mathrm{M})$ est l'espace des applications linéaires continues de $\mathrm{L}_{c}^{\prime}$ dans

M, muni de la topologie de la convergence uniforme sur les parties équi-continues de L'.

La topologie affaiblie ou faible se note $\sigma$ (voir page 199); voir à cette même page les références relatives aux topologies $\tau$ et $\gamma$.

Si E est un espace localement convexe, U un voisinage de 0 disqué, Eq est l'espace vectoriel quotient de E par le sous-espace vectoriel $\bigcap_{\lambda \neq 0} \lambda \mathfrak{u}$, muni de

la norme pour laquelle l'image de U est la boule unité. C'est aussi l'espace séparé normé, associé à E muni de la topologie définie par la seule semi-norme jauge (voir page 197) de U.

Son complété s'écrit, par abus de langage, $\hat{\mathbf{E}}\mathfrak{u}$, au lieu de $(\mathbf{E}\mathfrak{u})^{\wedge}$ (on ne risque pas de confondre avec $(\hat{\mathbf{E}})\mathfrak{u}$, car $\mathfrak{u}$ n'est pas un voisinage de 0 de $\hat{\mathbf{E}}$, sauf si $\mathbf{E}$ est déjà complet).

Si maintenant A est une partie bornée convexe équilibrée de E,  $E_{A}$  est l'espace vectoriel engendré par A, muni de la norme jauge de A.

Si $A \subset B$, et si $\mathcal{U} \subset \mathcal{V}$, on a les applications linéaires continues canoniques :

$$
\mathrm{E} _ {\mathbf {A}} \rightarrow \mathrm{E} _ {\mathbf {B}} \rightarrow \mathrm{E} \rightarrow \mathrm{Eq} \rightarrow \mathrm{Eq}.
$$

Si $\alpha$ est une forme bilinéaire séparément continue sur $\mathbf{L} \times \mathbf{M}$, $\tilde{\alpha}$ est l'application linéaire qu'elle définit de $\mathbf{L}$ dans $\mathbf{M}'$: $\langle \tilde{\alpha}(l), m \rangle = \alpha(l, m)$. Alors $t\tilde{\alpha}$ est sa transposée, application linéaire de $\mathbf{M}'$ dans $\mathbf{L}$:

$$
\langle l, ^ {t} \tilde {\alpha} (m) \rangle = \alpha (l, m).
$$

Alors, si $\xi\in\mathbf{L}\epsilon\mathbf{M}$, $\tilde{\xi}$ est l'application linéaire continue de $\mathbf{L}_{c}^{\prime}$ dans $\mathbf{M}$, et $\tilde{\xi}$ l'application linéaire continue de $\mathbf{M}_{c}^{\prime}$ dans $\mathbf{L}$, associées à $\xi$ par le corollaire 2 de la proposition 4, page 34 (I).

Le complété d'un espace localement convexe E se note par $\hat{E}$, son quasi-complété par $\hat{E}$.

Sur un produit tensoriel E⊗F, la topologie ⊗\_{S,T} est définie page 10 (II), les topologies ⊗\_λ(λ = i, γ, β, π, ε) page 12 (II); les complétés (resp. quasi-complétés) de ces produits tensoriels topologiques se notent donc E⊗\_{S,T}F (resp. E⊗\_{S,T}F), E⊗\_λF (resp. E⊗\_λF).

L'application $\Gamma_{\mu,\lambda}$ est définie page 18 (II); l'application $\Gamma_{\mu,\tau}^{0}$, page 22 (II); l'application $\Delta_{\tau,\mu}$ page 31 (II); $\Gamma_{\varphi,\lambda;\psi,\omega}$ page 35 (II), $\Delta_{\varphi,\lambda;\psi,\omega}$ page 36 (II). La notation $\vec{\varphi}^{\bullet}_{\iota;\Lambda}\vec{T}$ est définie page 57 (II); $\vec{\varphi}^{\bullet}_{\mathfrak{S},\mathfrak{G};\Lambda}\vec{T}$ (resp. $\vec{\varphi}^{\bullet}_{\lambda;\Lambda}\vec{T}$) est l'image de $\vec{\varphi}^{\bullet}_{\iota;\Lambda}\vec{T}$ dans E $\widehat{\otimes}_{\mathfrak{S},\mathfrak{G}}$ F (resp. E $\widehat{\otimes}_{\lambda}$ F). $\vec{\varphi}^{\bullet}_{\pi}\vec{T}$ est défini aussi page 41(II). $(\vec{\alpha}\vec{T})_{\iota}$ est défini page 127 (II); $(\vec{\alpha}\vec{T})_{\lambda}$ est défini page 128 (II); $(\vec{\alpha}\vec{T})_{\pi}$ est déjà défini page 121 (II).

$\vec{S}_{*,\vec{T}}$ est défini page 159 (II); $\vec{S}_{*\lambda}\vec{T}$ est défini page 160 (II); $\vec{S}_{*\pi}\vec{T}$ est déjà défini page 151.

$\vec{S}_x \otimes \otimes_\iota \vec{T}_y$ est défini page 145 (II); $\vec{S}_x \otimes \otimes_\mu \vec{T}_y$ page 146 (II).

Si u est une application bilinéaire de $\mathcal{H}\times\mathcal{K}$ dans $\mathscr{L}$ (espaces de distributions),

θ une application bilinéaires de E × F dans G, le symbole général  $\vec{S} \cup_{\theta} \vec{T} \in \mathscr{L}(G)$  est défini page 9, pour  $\vec{S} \in \mathscr{H}(E)$ ,  $\vec{T} \in \mathscr{K}(F)$ .

# INDEX BIBLIOGRAPHIQUE

## BOURBAKI.

[1] Espaces vectoriels topologiques. Chapitres i et ii, Paris, Hermann, 1953.

[2] Espaces vectoriels topologiques. Chapitres III, IV, v, Paris Hermann, 1955.

[3] Topologie générale. Chapitre x, Paris, Hermann, 1949.

[4] « Sur certains espaces vectoriels topologiques ». Annales de l'Institut Fourier, tome II, 1950, p. 5-16.

[5] Topologie générale. Chapitres I et II, Paris, Hermann, 1951.

[6] Intégration. Chapitres I, II, III, IV, Paris, Hermann, 1952.

## Bruhat.

[1] Sur les représentations induites des groupes de Lie, Paris, Gauthiers-Villars, 1956.

## DIEUDONNÉ-SCHWARTZ.

[1] « La dualité dans les espaces (F) et (LF) ». Annales de l'Institut Fourier, tome I, 1949, p. 61-101.

## GARNIR.

[1] « Sur la transformation de Laplace des distributions ». Comptes Rendus de l'Académie des Sciences de Paris, tome 234, 1952, p. 583-585.

## GROTHENDIECK.

[1] « Sur la complétion du dual d'un espace localement convexe ». Comptes Rendus de l'Académie des Sciences de Paris, tome 230, 1950, p. 605-606.

[2] « Sur les espaces (F) et (DF) ». Summa Brasiliensis Mathematicae, volume 2, 1954, p. 57-123.

[3] « Résumé des résultats essentiels dans la théorie des produits tensoriels topologiques et des espaces nucléaires ». Annales de l'Institut Fourier, tome IV, 1952, p. 73-112.

[4] « Produits tensoriels topologiques et espaces nucléaires ». Préliminaires et chapitre 1, Mémoirs of the American Mathematical Society, n° 16, 1955.

[5] « Produits tensoriels topologiques et espaces nucléaires », Chapitre II, Memoirs of the American Mathematical Society, n° 16, 1955.

[6] « Critères de compacité dans les espaces fonctionnels généraux ». American Journal of Mathematics, volume LXXIV, 1952, p. 168-186.

## Коethe.

[1] « Uber die Vollständigkeit einer Klasse lokalkonvexer Raume ». Mathematische Zeischrift, volume 52, 1950, p. 627-630.

## Lions.

[1] « Problèmes aux limites en théorie des distributions ». Acta Mathematica, tome 94, 1955, p. 13-153.

## De RHAM.

[1] « Variétés différentiables. Formes, courants, formes harmoniques ». Paris, Hermann, 1955.

## Schwartz.

[1] « Espaces de fonctions différentiables à valeurs vectorielles ». Journal d'Analyse Mathématique, Jérusalem, volume IV, 1954-55, p. 88-148.

[2] « Produits tensoriels topologiques et espaces nucléaires ». Séminaire, Institut Henri-Poincaré, 1953-54.

[3] « Transformation de Laplace des distributions ». Communications du Séminaire Mathématique de l'Université de Lund, tome supplémentaire dédié à Marcel Riesz (1952), p. 196-206.

[4] « Théorie des Distributions », tome I, Paris, Hermann, 1957.

[5] « Théorie des Distributions », tome II, Paris, Hermann, 1951.

[6] « Théorie des noyaux ». Proceedings of the International Congress of Mathematicians, 1950, volume I, p. 220-230.

[7] « Distributions semi-régulières et changements de variables ». Journal de Mathématiques pures et appliquées, tome XXXVI, 1957, p. 109-127.

[8] « Sur une propriété de synthèse spectrale dans les groupes non compacts ». Comptes rendus de l'Académie des Sciences de Paris, tome 227, 1948, p. 424-426.

Schwartz-Dieudonné.
Voir Dieudonné-Schwartz.

## TABLE DES MATIÈRES DU CHAPITRE II

RÉSUMÉ DU CHAPITRE II.... 1
§ 1. — Introduction .... 6
Position du problème .... 6
Applications bilinéaires S-T-hypocontinues .... 9
Produits tensoriels topologiques quasi-complétés .... 10
Les topologies λ sur un produit tensoriel .... 12
Les λ-parties et les parties σ-τ-décomposables des produits tensoriels quasi-complétés .... 15
§ 2. — Les théorèmes de croisement .... 18
L'application trilinéaire Γμ,λ de L × U × (MεV) dans (L ⊗μ M) ε (U ⊗λ V) .... 19
L'application bilinéaire Γμ,λ de (L ⊗λ U) × (MεV) dans (L ⊗μ M) ε (U ⊗λ V) .... 20
Compatibilité de Γμ,λ avec les applications linéaires continues et le changement des topologies λ et μ .... 24
Continuité partielle de Γμ,λ par rapport à ξ; L, M, U, V, quasi-complets .... 25
Continuité partielle de Γμ,λ par rapport à η ; L, M, U, V, non nécessairement quasi-complets .... 29
Restriction de Γμ,λ à (L ⊗λ U) × (M ⊗V)₀ (L, M, U, V, non nécessairement quasi-complets). .... 30
λ-continuité de Γε,λ (L, M, U, V, quasi-complets) .... 31
Hypocontinuité de Γμ,λ (L, M, U, V, quasi-complets) .. 32
Cas où certains des espaces sont identiques au corps des scalaires. Nouvelles formules .... 32
Les applications Γε,λ;ψ,,ω et Δε,λ;ψ,,ω; L, M, U, V, quasi-complets .... 34
Applications aux distributions .... 37
§ 3. — Produit « scalaire » de deux distributions à valeurs vectorielles. Etude élémentaire .... 41
Indépendance de φ·π T par rapport à l'espace H ..... 43
Problèmes de supports .... 44
Calcul de φ·π T par intégration usuelle .... 46
Convolutions .... 51
Liaison avec les résultats du chapitre Ier .... 52

§ 4. — Produit « scalaire ». Etude générale .....
53
Parties du type S, parties G-équibornées; applications sous-nucléaires et sous intégrales .....
53
Le produit scalaire $\vec{\varphi} \cdot_{\mathrm{t}} \vec{T}$ .....
57
Existence de $\vec{\varphi} \cdot_{\mathrm{t};\Lambda} \vec{T}$ .....
58
Compatibilité avec les applications linéaires continues de E et F.....
61
Image de $\vec{\varphi} \cdot_{\mathrm{t}} \vec{T}$ dans E ⊗, F; la formule (II, 4; 1) .....
62
Compatibilité avec les applications linéaires continues de K et H. La formule fondamentale (II, 4; 7) .....
63
Cas où l'application Λ est nucléaire .....
67
Continuité séparée en $\vec{T}$ pour $\vec{\varphi}$ fixée .....
70
Continuité séparée par rapport à $\vec{\varphi}$ pour $\vec{T}$ fixée .....
73
Calcul de $\vec{\varphi} \cdot_{\mathcal{G};\Lambda} \vec{T}$ lorsque Λ est seulement sous-intégrale.
75
Continuité par rapport à l'ensemble des variables $\vec{\varphi}, \vec{T}$.
80
Propriétés de $\vec{\varphi} \cdot_{\pi;\Lambda} \vec{T}$ pour Λ sous-intégrale .....
80
Indépendance de $\vec{\varphi} \cdot_{\mathcal{G};\Lambda} \vec{T}$ et de $\vec{\varphi} \cdot_{\mathcal{G};\Lambda} \vec{T}$ par rapport à Λ et aux espaces K, H. Problèmes de supports .....
83
Calcul de $\vec{\varphi} \cdot_{\mathcal{G};\Lambda} \vec{T}$ et de $\vec{\varphi} \cdot_{\mathcal{G};\Lambda} \vec{T}$ par une intégrale usuelle.
87
Cas où E n'est pas quasi-complet .....
94
Intervention des rôles de E et de F, de $\vec{\varphi}$ et de $\vec{T}$ .....
97
Cas où toute application continue de H dans F est bornée.
98
Exemples et applications de la proposition 10 .....
99
Exemple 1. Cas où E = $L(F; G)$ .....
99
Exemple 2. Dual de H(E) .....
101
Exemple 3. Produit scalaire d'une fonction m + n + 1 fois continuement différentiable et d'une distribution d'ordre ≤ m .....
105
§ 5. — Produit multiplicatif .....
120
Associativité de la multiplication .....
122
Cas où l'un des facteurs est une fonction indéfiniment dérivable .....
122
Problèmes de supports .....
124
Formule de dérivation du produit .....
125
Cas où S et T sont toutes les deux des fonctions. Notation fonctionnelle du produit .....
125
Relation entre produits scalaire et multiplicatif. Notation fonctionnelle du produit scalaire .....
126
Produit multiplicatif général .....
127
Exemple 1. Produit multiplicatif d'une distribution semi-régulière en x et d'une distribution intégralement semi-régulière en y .....
138
Exemple 2. Sections-distributions d'un espace fibré à fibre vectorielle topologique .....
140

THÉORIE DES DISTRIBUTIONS A VALEURS VECTORIELLES 209
§ 6. — Produit tensoriel .....
Cas où $\vec{S}$ et $\vec{T}$ sont des fonctions .....
Produit tensoriel de plusieurs distributions .....
§ 7. — Convolution .....
Convolution élémentaire .....
Associativité de la convolution .....
Commutativité de la convolution .....
Indépendance de $\vec{S} *_{\pi} \vec{T}$ par rapport à $\mathcal{H}$ et $\mathcal{K}$ .....
Problèmes de supports .....
Relation entre produit scalaire et produit de convolution .....
Produit de convolution général .....
Définition du produit de convolution à partir du produit tensoriel .....
Cas où les distributions sont des fonctions .....
Notation fonctionnelle du produit de convolution .....
Multiplication, convolution, transformations de Fourier et Laplace .....
§ 8. — Etude de trois contre-exemples .....
Premier contre-exemple .....
Deuxième contre-exemple .....
Troisième contre-exemple .....
INDEX TERMINOLOGIQUE .....
INDEX DES NOTATIONS .....
INDEX BIBLIOGRAPHIQUE .....
TABLE DES MATIÈRES ....