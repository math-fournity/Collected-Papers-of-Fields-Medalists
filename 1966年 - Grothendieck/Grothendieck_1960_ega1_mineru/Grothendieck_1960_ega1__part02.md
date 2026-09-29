(10.1.5) En tant que faisceau d'anneaux sans topologie, le faisceau structural $\mathcal{O}_{\mathfrak{x}}$ de $\operatorname{Spf}(\mathbf{A})$ admet pour tout $x \in \mathfrak{X}$ une fibre qui, en vertu de (10.1.4), s'identifie à la limite inductive $\lim_{\substack{\mathbf{A}_{\{f\}} \\ \longrightarrow}} \mathbf{A}_{\{f\}}$ pour les $f \notin \mathbf{j}_x$. Par suite (0, 7.6.17 et 7.6.18):

Proposition (10.1.6). — Pour tout  $x \in \mathfrak{X} = \text{Spf}(A)$ , la fibre  $O_x$  est un anneau local dont le corps résiduel est isomorphe à  $\boldsymbol{k}(x) = \mathbf{A}_x / \mathbf{j}_x \mathbf{A}_x$ . Si en outre A est adique et noethérien,  $O_x$  est un anneau noethérien.

Comme $\boldsymbol{k}(x)$ n'est pas réduit à o, on conclut de ce résultat que le support du faisceau d'anneaux $\mathcal{O}_{\mathfrak{X}}$ est égal à $\mathfrak{X}$.

## 10.2. Morphismes de schémas formels affines.

(10.2.1) Soient A, B deux anneaux admissibles, et soit $\varphi: B \to A$ un homomorphisme continu. L'application continue $^a\varphi: \operatorname{Spec}(A) \to \operatorname{Spec}(B)$ (1.2.1) applique alors $\mathfrak{X} = \operatorname{Spf}(A)$ dans $\mathfrak{Y} = \operatorname{Spf}(B)$, car l'image réciproque par $\varphi$ d'un idéal premier ouvert de A est un idéal premier ouvert de B. D'autre part, pour tout $g \in B$, $\varphi$ définit un homomorphisme continu $\Gamma(\mathfrak{D}(g), \mathcal{O}_{\mathfrak{Y}}) \to \Gamma(\mathfrak{D}(\varphi(g)), \mathcal{O}_{\mathfrak{X}})$ en vertu de (10.1.4), (10.1.3) et (0, 7.6.7); comme ces homomorphismes satisfont aux conditions de compatibilité pour les restrictions correspondant au passage de $g$ à un multiple de $g$, et que $\mathfrak{D}(\varphi(g)) = ^a\varphi^{-1}(\mathfrak{D}(g))$, ils définissent un homomorphisme continu de faisceaux d'anneaux topologiques $\mathcal{O}_{\mathfrak{Y}} \to ^a\varphi_*(\mathcal{O}_{\mathfrak{X}})$ (0, 3.2.5), que nous noterons encore $\widetilde{\varphi}$; on a ainsi obtenu un morphisme $\Phi = (^a\varphi, \widetilde{\varphi})$ d'espaces topologiquement annelés $\mathfrak{X} \to \mathfrak{Y}$. On notera qu'en tant qu'homomorphisme de faisceaux d'anneaux sans topologie, $\widetilde{\varphi}$ définit un homomorphisme $\widetilde{\varphi}_x^\sharp: \mathcal{O}_{a_{\varphi(x)}} \to \mathcal{O}_x$ sur les fibres, pour tout $x \in \mathfrak{X}$.

Proposition (10.2.2). — Soient A, B deux anneaux topologiques admissibles, et soient $\mathfrak{X} = \operatorname{Spf}(A)$, $\mathfrak{Y} = \operatorname{Spf}(B)$. Pour qu'un morphisme $u = (\psi, \theta) : \mathfrak{X} \to \mathfrak{Y}$ d'espaces topologiquement annelés soit de la forme $(^a\varphi, \widetilde{\varphi})$, où $\varphi$ est un homomorphisme continu d'anneaux B→A, il faut et il suffit que pour tout $x \in X$, $\theta_x^\sharp$ soit un homomorphisme local $\mathcal{O}_{\psi(x)} \to \mathcal{O}_x$.

La condition est nécessaire : en effet, soit $\mathfrak{p} = \mathrm{j}_x \in \operatorname{Spf}(\mathrm{A})$, et soit $\mathfrak{q} = \varphi^{-1}(\mathrm{j}_x)$; si $g \notin \mathfrak{q}$, on a donc $\varphi(g) \notin \mathfrak{p}$, et il est immédiat que l'homomorphisme $\mathbf{B}_{\{g\}} \to \mathbf{A}_{\{\varphi(g)\}}$ déduit de $\varphi(0, 7.6.7)$ transforme $\mathfrak{q}_{\{g\}}$ en une partie de $\mathfrak{p}_{\{\varphi(g)\}}$; passant à la limite inductive, on voit donc (compte tenu de (10.1.5) et de (0, 7.6.17)) que $\widetilde{\varphi}_x^\sharp$ est un homomorphisme local.

Inversement, soit $(\psi, \theta)$ un morphisme vérifiant la condition de l'énoncé; en vertu de (10.1.3), $\theta$ définit un homomorphisme continu d'anneaux

$$
\varphi = \Gamma (\theta): B = \Gamma (\mathfrak {Y}, \mathcal {O} _ {\mathfrak {Y}}) \rightarrow \Gamma (\mathfrak {X}, \mathcal {O} _ {\mathfrak {X}}) = A.
$$

En vertu de l'hypothèse sur $\theta$, pour que la section $\varphi(g)$ de $\mathcal{O}_{\mathfrak{x}}$ au-dessus de $\mathfrak{X}$ ait un germe inversible au point $x$, il faut et il suffit que $g$ ait un germe inversible au point $\psi(x)$. Mais en vertu de (0, 7.6.17), les sections de $\mathcal{O}_{\mathfrak{X}}$ (resp. $\mathcal{O}_{\mathfrak{Y}}$) au-dessus de $\mathfrak{X}$ (resp. $\mathfrak{Y}$) dont le germe n'est pas inversible au point $x$ (resp. $\psi(x)$) sont exactement les éléments de $\mathbf{j}_x$

(resp.  $\mathrm{i}_{\psi(x)}$ ); la remarque précédente montre donc que  $^{a}\varphi=\psi$ . Enfin, pour tout  $g\in B$ , le diagramme

$$
\begin{array}{c} \mathrm{B} = \Gamma (\mathfrak {Y}, \mathcal {O} _ {\mathfrak {Y}}) \xrightarrow {\varphi} \Gamma (\mathfrak {X}, \mathcal {O} _ {\mathfrak {X}}) = \mathrm{A} \\ \downarrow \qquad \qquad \qquad \qquad \qquad \downarrow \\ \mathrm{B} _ {\{g \}} = \Gamma (\mathfrak {D} (g), \mathcal {O} _ {\mathfrak {Y}}) \xrightarrow [ \Gamma (\theta_ {\mathfrak {D} (g)}) ]{} \Gamma (\mathfrak {D} (\varphi (g)), \mathcal {O} _ {\mathfrak {X}}) = \mathrm{A} _ {\{\varphi (g) \}} \end{array}
$$

est commutatif ; d'après la propriété universelle des anneaux complets de fractions (0, 7.6.6), $\theta_{\mathfrak{D}(g)}$ est égale à $\widetilde{\varphi}_{\mathfrak{D}(g)}$ pour tout $g \in \mathbf{B}$, donc (0, 3.2.5) on a $\theta = \widetilde{\varphi}$.

Nous dirons qu'un morphisme $(\psi, \theta)$ d'espaces topologiquement annelés vérifiant la condition de (10.2.2) est un morphisme de schémas formels affines. On peut dire que les foncteurs Spf(A) en À et $\Gamma(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}})$ en $\mathfrak{X}$ définissent une équivalence de la catégorie des anneaux admissibles et de la catégorie duale de la catégorie des schémas formels affines (T, I, 1.2).

(10.2.3) Comme cas particulier de (10.2.2), notons que, pour $f\in A$, l'injection canonique du schéma formel affine induit par $\mathfrak{X}$ sur $\mathfrak{D}(f)$ correspond à l'homomorphisme continu canonique $\mathrm{A}\to\mathrm{A}_{\{f\}}$. Sous les hypothèses de (10.2.2), soient $h$ un élément de B, $g$ un élément de A, multiple de $\varphi(h)$; on a alors $\psi(\mathfrak{D}(g))\subset\mathfrak{D}(h)$; la restriction de $u$ à $\mathfrak{D}(g)$, considérée comme morphisme de $\mathfrak{D}(g)$ dans $\mathfrak{D}(h)$, est l'unique morphisme $v$ rendant commutatif le diagramme

$$
\begin{array}{c} \mathfrak {D} (g) \stackrel {{v}} {{\to}} \mathfrak {D} (h) \\ \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \downarrow \\ \mathfrak {X} \xrightarrow [ u ]{} \mathfrak {Y} \end{array}
$$

Ce morphisme correspond à l'unique homomorphisme continu $\varphi':\mathbf{B}_{\{h\}}\to\mathbf{A}_{\{g\}}$ (0, 7.6.7) rendant commutatif le diagramme

$$
\begin{array}{c} \mathbf {A} \stackrel {{\varphi}} {{\leftarrow}} \mathbf {B} \\ \downarrow \qquad \qquad \downarrow \\ \mathbf {A} _ {\{g \}} \stackrel {{\varphi^ {\prime}}} {{\leftarrow}} \mathbf {B} _ {\{h \}} \end{array}
$$

## 10.3. Idéaux de définition d'un schéma formel affine.

(10.3.1) Soient A un anneau admissible, $\mathfrak{J}$ un idéal ouvert de A, $\mathfrak{X}$ le schéma formel affine Spf(A). Soit $(\mathfrak{J}_{\lambda})$ l'ensemble des idéaux de définition de A contenus dans $\mathfrak{J}$; alors $\widetilde{\mathfrak{J}}/\widetilde{\mathfrak{J}}_{\lambda}$ est un faisceau d'idéaux de $\widetilde{\mathrm{A}}/\widetilde{\mathfrak{J}}_{\lambda}$. Désignons par $\mathfrak{J}^{\Delta}$ la limite projective des faisceaux induits sur $\mathfrak{X}$ par $\widetilde{\mathfrak{J}}/\widetilde{\mathfrak{J}}_{\lambda}$, qui s'identifie à un faisceau d'idéaux de $\mathcal{O}_{\mathfrak{X}}$ (0, 3.2.6). Pour tout $f\in\mathrm{A}$, $\Gamma(\mathfrak{D}(f),\mathfrak{J}^{\Delta})$ est la limite projective de $\mathrm{S}_{f}^{-1}\mathfrak{J}/\mathrm{S}_{f}^{-1}\mathfrak{J}_{\lambda}$, autrement dit s'identifie à l'idéal ouvert $\mathfrak{J}_{\{f\}}$ de l'anneau $\mathrm{A}_{\{f\}}$ (0, 7.6.9), et en particulier $\Gamma(\mathfrak{X},\mathfrak{J}^{\Delta})=\mathfrak{J}$; on en conclut (les $\mathfrak{D}(f)$ formant une base de la topologie de $\mathfrak{X}$) que l'on a

$$
\mathfrak {I} ^ {\Delta} | \mathfrak {D} (f) = (\mathfrak {I} _ {\{f \}}) ^ {\Delta}\tag{10.3.1.1}
$$

(10.3.2) Avec les notations de (10.3.1), pour tout $f\in\mathbf{A}$, l'application canonique de $\mathbf{A}_{\{f\}}=\Gamma(\mathfrak{D}(f),\mathcal{O}_{\mathfrak{X}})$ dans $\Gamma(\mathfrak{D}(f),(\widetilde{\mathbf{A}}/\widetilde{\mathfrak{J}})|\mathfrak{X})=\mathrm{S}_{f}^{-1}\mathrm{A}/\mathrm{S}_{f}^{-1}\mathfrak{J}$ est surjective et a pour noyau $\Gamma(\mathfrak{D}(f),\mathfrak{J}^{\Delta})=\mathfrak{J}_{\{f\}}$ (0, 7.6.9); ces applications définissent donc un homomorphisme surjectif continu, dit canonique, du faisceau d'anneaux topologiques $\mathcal{O}_{\mathfrak{X}}$ sur le faisceau d'anneaux discrets $(\widetilde{\mathbf{A}}/\widetilde{\mathfrak{J}})|\mathfrak{X}$, dont le noyau est $\mathfrak{J}^{\Delta}$; cet homomorphisme n'est autre d'ailleurs que $\widetilde{\varphi}$ (10.2.1), où $\varphi$ est l'homomorphisme continu $\mathbf{A}\to\mathbf{A}/\mathfrak{J}$; le morphisme ($^a\varphi,\widetilde{\varphi}$): $\operatorname{Spec}(\mathbf{A}/\mathfrak{J})\to\mathfrak{X}$ de schémas formels affines (où $^a\varphi$ est d'ailleurs l'homéomorphisme identique de $\mathfrak{X}$ sur lui-même) est encore dit canonique. On a donc, d'après ce qui précède, un isomorphisme canonique

$$
\mathcal {O} _ {\mathfrak {X}} / \mathfrak {J} ^ {\Delta} \simeq (\widetilde {\mathrm{A}} / \widetilde {\mathfrak {J}}) | \mathfrak {X}\tag{10.3.2.1}
$$

Il est clair (en vertu de $\Gamma(\mathfrak{X},\mathfrak{J}^{\Delta})=\mathfrak{J}$) que l'application $\mathfrak{J}\to\mathfrak{J}^{\Delta}$ est strictement croissante; d'après ce qui précède, pour $\mathfrak{J}\subset\mathfrak{J}'$, le faisceau $\mathfrak{J}'^{\Delta}/\mathfrak{J}^{\Delta}$ est canoniquement isomorphe à $\widetilde{\mathfrak{J}}'/\widetilde{\mathfrak{J}}=(\mathfrak{J}'/\mathfrak{J})\sim$.

(10.3.3) Les hypothèses et notations étant toujours celles de (10.3.1), nous dirons qu'un faisceau d'idéaux J de  $O_{X}$  est un faisceau d'idéaux de définition de X (ou un Idéal de définition de X) si, pour tout  $x \in X$ , il existe un voisinage ouvert de x de la forme  $\mathfrak{D}(f)$ , où  $f \in A$ , tel que  $\mathcal{J}| \mathfrak{D}(f)$  soit de la forme  $H^{\Delta}$ , où H est un idéal de définition de  $A_{\{f\}}$ .

Proposition (10.3.4). — Pour tout  $f \in A$ , tout Idéal de définition de X induit un Idéal de définition de  $\mathfrak{D}(f)$ .

Cela résulte de (10.3.1.1).

Proposition (10.3.5). — Si A est un anneau admissible, tout Idéal de définition de $\mathfrak{X}=\mathrm{Spf}(A)$ est de la forme $\mathfrak{J}^{\Delta}$, où $\mathfrak{J}$ est un idéal de définition de A, uniquement déterminé.

En effet, soit $\mathcal{J}$ un Idéal de définition de $\mathfrak{X}$; par hypothèse, et puisque $\mathfrak{X}$ est quasi-compact, il y a un nombre fini d'éléments $f_i \in \mathbf{A}$ tels que les $\mathfrak{D}(f_i)$ recouvrent $\mathfrak{X}$ et que $\mathcal{J}|\mathfrak{D}(f_i) = \mathfrak{H}_i^\Delta$, où $\mathfrak{H}_i$ est un idéal de définition de $\mathrm{A}_{\{f_i\}}$. Pour tout $i$, il existe donc un idéal ouvert $\mathfrak{R}_i$ de A tel que $(\mathfrak{R}_i)_{\{f_i\}} = \mathfrak{H}_i$ (0, 7.6.9); soit $\mathfrak{R}$ un idéal de définition de A contenu dans tous les $\mathfrak{R}_i$. L'image canonique de $\mathcal{J}/\mathfrak{R}^\Delta$ dans le faisceau structural $(\mathrm{A}/\mathfrak{R})^\sim$ de $\operatorname{Spec}(\mathrm{A}/\mathfrak{R})$ (10.3.2) est donc telle que sa restriction à $\mathfrak{D}(f_i)$ soit égale à celle de $(\mathfrak{R}_i/\mathfrak{R})^\sim$; on en conclut que cette image canonique est un faisceau quasi-cohérent sur $\operatorname{Spec}(\mathrm{A}/\mathfrak{R})$, donc de la forme $(\mathfrak{J}/\mathfrak{R})^\sim$, où $\mathfrak{J}$ est un idéal de A contenant $\mathfrak{R}$ (1.4.1) d'où $\mathcal{J} = \mathfrak{J}^\Delta$ (10.3.2); en outre, comme pour tout $i$ il existe un entier $n_i$ tel que $\mathfrak{H}_i^{n_i} \subset \mathfrak{R}_{\{f_i\}}$, on aura, en désignant par $n$ le plus grand des $n_i$, $(\mathcal{J}/\mathfrak{R}^\Delta)^n = 0$, et par suite (10.3.2) $((\mathfrak{J}/\mathfrak{R})^\sim)^n = 0$, d'où finalement $(\mathfrak{J}/\mathfrak{R})^n = 0$ (1.3.13), ce qui prouve que $\mathfrak{J}$ est un idéal de définition de A (0, 7.1.4).

Proposition (10.3.6). — Soient A un anneau adique, $\mathfrak{J}$ un idéal de définition de A tel que $\mathfrak{J}/\mathfrak{J}^2$ soit un A/$\mathfrak{J}$-module de type fini. Pour tout entier $n>0$, on a alors $(\mathfrak{J}^\Delta)^n=(\mathfrak{J}^n)^\Delta$.

En effet, pour tout $f\in\mathbf{A}$, on a (puisque $\mathfrak{J}^{n}$ est un idéal ouvert)

$$
(\Gamma (\mathfrak {D} (f), \mathfrak {I} ^ {\Delta})) ^ {n} = (\mathfrak {I} _ {\{f \}}) ^ {n} = (\mathfrak {I} ^ {n}) _ {\{f \}} = \Gamma (\mathfrak {D} (f ^ {n}), (\mathfrak {I} ^ {n}) ^ {\Delta})
$$

en vertu de (10.3.1.1) et de (0, 7.6.12). Comme $(\mathfrak{J}^{\Delta})^{n}$ est associé au préfaisceau $U \to (\Gamma(U, \mathfrak{J}^{\Delta}))^{n}$ (0, 4.1.6), le corollaire en résulte, puisque les $\mathfrak{D}(f)$ forment une base de la topologie de X.

(10.3.7) On dit qu'une famille  $(\mathcal{J}_{\lambda})$  d'Idéaux de définition de X est un système fondamental d'Idéaux de définition si tout Idéal de définition de X contient un des  $J_{\lambda}$ ; comme  $J_{\lambda} = J_{\lambda}^{\Delta}$ , il revient au même de dire que les  $J_{\lambda}$  forment un système fondamental de voisinages de o dans A. Soit  $(f_{\alpha})$  une famille d'éléments de A tels que les  $\mathfrak{D}(f_{\alpha})$  recouvrent X. Si  $(\mathcal{J}_{\lambda})$  est une famille filtrante décroissante d'idéaux de  $O_{x}$  telle que pour tout  $\alpha$ , la famille  $(\mathcal{J}_{\lambda} | \mathfrak{D}(f_{\alpha}))$  soit un système fondamental d'Idéaux de définition de  $\mathfrak{D}(f_{\alpha})$ , alors  $(\mathcal{J}_{\lambda})$  est un système fondamental d'Idéaux de définition de X. En effet, pour tout Idéal de définition J de X, il y a un recouvrement fini de X par des  $\mathfrak{D}(f_{i})$  tel que, pour tout i,  $\mathcal{J}_{\lambda_{i}} | \mathfrak{D}(f_{i})$  soit un Idéal de définition de  $\mathfrak{D}(f_{i})$  contenu dans  $\mathcal{J} | \mathfrak{D}(f_{i})$ . Si  $\mu$  est un indice tel que  $J_{\mu} \subset J_{\lambda_{i}}$  pour tout i, il résulte de (10.3.3) que  $J_{\mu}$  est un Idéal de définition de X, évidemment contenu dans J, d'où notre assertion.

## 10.4. Préschémas formels et morphismes de préschémas formels.

(10.4.1.) Étant donné un espace topologiquement annelé $\mathfrak{X}$, on dit qu'un ouvert $U \subset \mathfrak{X}$ est un ouvert formel affine (resp. un ouvert formel affine adique, resp. un ouvert formel affine noethérien) si l'espace topologiquement annelé induit par $\mathfrak{X}$ sur $U$ est un schéma formel affine (resp. un tel schéma dont l'anneau est adique, resp. adique et noethérien).

Définition (10.4.2). — On appelle préschéma formel un espace topologiquement annelé X dont tout point admet un voisinage ouvert formel affine. On dit que le préschéma formel X est adique (resp. localement noethérien) si tout point de X admet un voisinage ouvert formel affine adique (resp. noethérien). On dit que X est noethérien s'il est localement noethérien et si son espace sous-jacent est quasi-compact (donc noethérien).

Proposition (10.4.3). — Si X est un préschéma formel (resp. localement noethérien), les ensembles ouverts formels affines (resp. affines noethériens) forment une base de la topologie de X.

Cela résulte de (10.4.2) et (10.1.4) en tenant compte de ce que si A est un anneau adique noethérien, il en est de même de  $A_{\{f\}}$  pour tout  $f \in A$  (0, 7.6.11).

Corollaire (10.4.4). — Si X est un préschéma formel (resp. un préschéma formel localement noethérien, resp. noethérien), l'espace topologiquement annelé induit sur tout ouvert de X est encore un préschéma formel (resp. un préschéma formel localement noethérien, resp. noethérien).

Définition (10.4.5). — Étant donnés deux préschémas formels $\mathfrak{X}$, $\mathfrak{Y}$, on appelle morphisme (de préschémas formels) de $\mathfrak{X}$ dans $\mathfrak{Y}$ tout morphisme $(\psi, \theta)$ d'espaces topologiquement annelés tel que, pour tout $x \in \mathfrak{X}$, $\theta_x^\sharp$ soit un homomorphisme local $\mathcal{O}_{\psi(x)} \to \mathcal{O}_x$.

Il est immédiat que le composé de deux morphismes de préschémas formels est encore un tel morphisme ; les préschémas formels forment donc une catégorie, et on notera Hom(X, Y) l'ensemble des morphismes d'un préschéma formel X dans un préschéma formel Y.

Si U est une partie ouverte de $\mathfrak{X}$, l'injection canonique dans $\mathfrak{X}$ du préschéma formel induit par $\mathfrak{X}$ sur U est un morphisme de préschémas formels (et même un monomorphisme d'espaces topologiquement annelés (0, 4.1.1)).

Proposition (10.4.6). — Soient $\mathfrak{X}$ un préschéma formel, $\mathfrak{S} = \operatorname{Spf}(A)$ un schéma formel affine. Il existe une correspondance biunivoque canonique entre les morphismes du préschéma formel $\mathfrak{X}$ dans le préschéma formel $\mathfrak{S}$ et les homomorphismes continus de l'anneau A dans l'anneau topologique $\Gamma(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}})$.

La démonstration est la même que celle de (2.2.4), en remplaçant « homomorphisme » par « homomorphisme continu », « ouvert affine » par « ouvert formel affine », et en utilisant (10.2.2) au lieu de (1.7.3) ; nous en laissons les détails au lecteur.

(10.4.7) Étant donné un préschéma formel S, on dit que la donnée d'un préschéma formel X et d'un morphisme $\varphi: \mathfrak{X} \to \mathfrak{S}$ définit un préschéma formel X au-dessus de S ou un S-préschéma formel, $\varphi$ étant appelé le morphisme structural du S-préschéma X. Si $S = Spf(A)$, où A est un anneau admissible, on dit aussi que le S-préschéma formel X est un A-préschéma formel ou un préschéma formel au-dessus de A. Un préschéma formel quelconque peut toujours être considéré comme un préschéma formel au-dessus de Z (muni de la topologie discrète).

Si X, Y sont deux S-préschémas formels, on dit qu'un morphisme  $u : X \to Y$  est un S-morphisme si le diagramme

![](images/page_4_image_5.jpg)

(où les flèches obliques sont les morphismes structuraux) est commutatif. Avec cette définition, les S-préschémas formels (pour S fixé) forment une catégorie. On désigne par $\mathrm{Hom}_{\mathfrak{S}}(\mathfrak{X},\mathfrak{Y})$ l'ensemble des S-morphismes du S-préschéma formel $\mathfrak{X}$ dans le S-préschéma formel $\mathfrak{Y}$. Lorsque $S = Spf(A)$, on dit aussi A-morphisme au lieu de S-morphisme.

(10.4.8) Comme tout schéma affine peut être considéré comme un schéma formel affine (10.1.2), tout préschéma (usuel) peut être considéré comme un préschéma formel. Il résulte en outre de (10.4.5) que pour les préschémas usuels, les morphismes (resp. S-morphismes) de préschémas formels coïncident avec les morphismes (resp. S-morphismes) définis au § 2.

## 10.5. Idéaux de définition des préschémas formels.

(10.5.1) Soit $\mathfrak{X}$ un préschéma formel ; on dit qu'un $\mathcal{O}_{\mathfrak{x}}$-Idéal $\mathcal{J}$ est un faisceau d'idéaux de définition (ou un Idéal de définition) de $\mathfrak{X}$ si tout $x \in \mathfrak{X}$ possède un voisinage ouvert formel affine U tel que $\mathcal{J}|\mathrm{U}$ soit un Idéal de définition du schéma formel affine induit par $\mathfrak{X}$ sur U (10.3.3) ; en vertu de (10.3.1.1) et (10.4.3), pour tout ouvert V⊂$\mathfrak{X}$, $\mathcal{J}|\mathrm{V}$ est alors un Idéal de définition du préschéma formel induit par $\mathfrak{X}$ sur V.

On dit qu'une famille $(\mathcal{J}_{\lambda})$ d'Idéaux de définition de $\mathfrak{X}$ est un système fondamental

d'Idéaux de définition s'il existe un recouvrement  $(\mathbf{U}_{\alpha})$  de X par des ouverts formels affines tel que, pour tout  $\alpha$, la famille des  $J_{\lambda}|U_{\alpha}$  soit un système fondamental d'Idéaux de définition (10.3.6) du schéma formel affine induit par X sur  $U_{\alpha}$. Il résulte de la remarque finale de (10.3.7) que lorsque X est un schéma formel affine, cette définition coïncide avec la définition donnée dans (10.3.7). Pour tout ouvert V de X, les restrictions  $J_{\lambda}|V$  forment alors un système fondamental d'Idéaux de définition du préschéma formel induit sur V, en vertu de (10.3.1.1). Si X est un préschéma formel localement noethérien, et J un Idéal de définition de X, il résulte de (10.3.6) que les puissances  $J^{n}$  forment un système fondamental d'Idéaux de définition de X.

(10.5.2) Soient $\mathfrak{X}$ un préschéma formel, $\mathcal{J}$ un Idéal de définition de $\mathfrak{X}$. Alors l'espace annelé $(\mathfrak{X},\mathcal{O}_{\mathfrak{X}}/\mathcal{J})$ est un préschéma (usuel), qui est affine (resp. localement noethérien, resp. noethérien) lorsque $\mathfrak{X}$ est un schéma formel affine (resp. un préschéma formel localement noethérien, resp. noethérien); on est en effet aussitôt ramené au cas affine, et alors la proposition a déjà été démontrée dans (10.3.2). En outre, si $\theta:\mathcal{O}_{\mathfrak{X}}\to\mathcal{O}_{\mathfrak{X}}/\mathcal{J}$ est l'homomorphisme canonique, $u=(\mathrm{I}_{\mathfrak{X}},\theta)$ est un morphisme (dit canonique) de préschémas formels $(\mathfrak{X},\mathcal{O}_{\mathfrak{X}}/\mathcal{J})\to(\mathfrak{X},\mathcal{O}_{\mathfrak{X}})$, car ici encore, cela a été vu dans le cas affine (10.3.2), auquel on se ramène aussitôt.

Proposition (10.5.3). — Soient $\mathfrak{X}$ un préschéma formel, $(\mathcal{J}_{\lambda})$ un système fondamental d'Idéaux de définition de $\mathfrak{X}$. Alors le faisceau d'anneaux topologiques $\mathcal{O}_{\mathfrak{X}}$ est limite projective des faisceaux d'anneaux pseudo-discrets (0, 3.8.1) $\mathcal{O}_{\mathfrak{X}} / \mathcal{J}_{\lambda}$.

Comme la topologie de $\mathfrak{X}$ admet une base d'ouverts formels affines quasi-compacts (10.4.3), on est ramené au cas affine, où la proposition est conséquence de (10.3.5), (10.3.2) et de la définition (10.1.1).

Il n'est pas certain que tout préschéma formel admette des Idéaux de définition. Toutefois :

Proposition (10.5.4). — Soit X un préschéma formel localement noethérien. Il existe un plus grand Idéal de définition T de X ; c'est le seul Idéal de définition J tel que le préschéma (X, O\_x|J) soit réduit. Si J est un Idéal de définition de X, T est l'image réciproque par O\_x→O\_x|J du Nilradical de O\_x|J.

Supposons d'abord que $\mathfrak{X} = \operatorname{Spf}(A)$, où $A$ est un anneau adique noethérien. L'existence et les propriétés de $\mathcal{T}$ résultent immédiatement de (10.3.4) et (5.1.1), compte tenu de l'existence et des propriétés du plus grand idéal de définition de $A$ (0, 7.1.6 et 7.1.7).

Pour prouver l'existence et les propriétés de $\mathcal{T}$ dans le cas général, il suffit de montrer que si U$\supset$V sont deux ouverts formels affines noethériens de X, le plus grand Idéal de définition $\mathcal{T}_{\mathrm{U}}$ de U induit le plus grand Idéal de définition $\mathcal{T}_{\mathrm{V}}$ de V; mais comme $(\mathrm{V}, (\mathcal{O}_{\mathfrak{x}}|\mathrm{V}) / (\mathcal{T}_{\mathrm{U}}|\mathrm{V}))$ est réduit, cela résulte de ce qui précède.

On désigne par $\mathfrak{X}_{\mathrm{red}}$ le préschéma (usuel) réduit $(\mathfrak{X},\mathcal{O}_{\mathfrak{x}}/\mathcal{T})$.

Corollaire (10.5.5). — Soient $\mathfrak{X}$ un préschéma formel localement noethérien, $\mathcal{T}$ le plus grand Idéal de définition de $\mathfrak{X}$; pour tout ouvert V de $\mathfrak{X}$, $\mathcal{T}|\mathrm{V}$ est le plus grand Idéal de définition du préschéma formel induit par $\mathfrak{X}$ sur V.

Proposition (10.5.6). — Soient $\mathfrak{X}$, $\mathfrak{Y}$ deux préschémas formels, $\mathcal{J}$ (resp. $\mathcal{K}$) un Idéal de définition de $\mathfrak{X}$ (resp. $\mathfrak{Y}$), $f: \mathfrak{X} \to \mathfrak{Y}$ un morphisme de préschémas formels.

(i) Si $f^{*}(\mathcal{K})\mathcal{O}_{\mathfrak{x}}\subset\mathcal{J}$, il existe un unique morphisme $f^{\prime}:(\mathfrak{x},\mathcal{O}_{\mathfrak{x}}/\mathcal{J})\to(\mathfrak{Y},\mathcal{O}_{\mathfrak{Y}}/\mathcal{K})$ de préschémas usuels rendant commutatif le diagramme

$$
\begin{array}{c} (\mathfrak {X}, \mathcal {O} _ {\mathfrak {X}}) \xrightarrow {f} (\mathfrak {Y}, \mathcal {O} _ {\mathfrak {Y}}) \\ \uparrow \qquad \qquad \qquad \qquad \qquad \qquad \uparrow \\ (\mathfrak {X}, \mathcal {O} _ {\mathfrak {X}} / \mathcal {J}) \xrightarrow [ t ^ {\prime} ]{} (\mathfrak {Y}, \mathcal {O} _ {\mathfrak {Y}} / \mathcal {K}) \end{array}\tag{10.5.6.1}
$$

où les flèches verticales sont les morphismes canoniques.

(ii) Supposons que $\mathfrak{X} = \operatorname{Spf}(A), \mathfrak{Y} = \operatorname{Spf}(B)$ soient des schémas formels affines, $\mathcal{J} = \mathfrak{J}^{\Delta}$, $\mathcal{K} = \mathfrak{K}^{\Delta}$, où $\mathfrak{J}$ (resp. $\mathfrak{K}$) est un idéal de définition de A (resp. B), et $f = (^{a}\varphi, \widetilde{\varphi})$, où $\varphi : B \to A$ est un homomorphisme continu; pour que $f^{*}(\mathcal{K})\mathcal{O}_{\mathfrak{X}} \subset \mathcal{J}$, il faut et il suffit que $\varphi (\mathfrak{K}) \subset \mathfrak{J}$, et $f'$ est alors le morphisme ($^{a}\varphi', \widetilde{\varphi'}$), où $\varphi': B / \mathfrak{K} \to A / \mathfrak{J}$ est l'homomorphisme déduit de $\varphi$ par passage aux quotients.

(i) Si $f=(\psi,\theta)$, l'hypothèse entraîne que l'image par $\theta^{\sharp}:\psi^{*}(\mathcal{O}_{\mathfrak{Y}})\to\mathcal{O}_{\mathfrak{X}}$ du faisceau d'idéaux $\psi^{*}(\mathcal{K})$ de $\psi^{*}(\mathcal{O}_{\mathfrak{Y}})$ est contenue dans $\mathcal{J}(0,4\cdot3\cdot5)$. Par passage aux quotients, on déduit donc de $\theta^{\sharp}$ un homomorphisme de faisceau d'anneaux

$$
\omega : \psi^ {*} (\mathcal {O} _ {\mathfrak {Y}} / \mathscr {K}) = \psi^ {*} (\mathcal {O} _ {\mathfrak {Y}}) / \psi^ {*} (\mathscr {K}) \rightarrow \mathcal {O} _ {\mathfrak {X}} / \mathscr {J}
$$

en outre, comme pour tout $x\in\mathbf{X}$, $\theta_{x}^{\sharp}$ est un homomorphisme $local$, il en est de même de $\omega_{x}$. Le morphisme d'espaces annelés $(\psi,\omega^{\flat})$ est donc (2.2.1) l'unique morphisme $f'$ d'espaces annelés répondant à la question.

(ii) La correspondance canonique fonctorielle entre morphismes de préschémas formels affines et homomorphismes continus d'anneaux (10.2.2) montre que dans le cas considéré, la relation $f^{*}(\mathcal{K})\mathcal{O}_{\mathfrak{X}} \subset \mathcal{J}$ entraîne que l'on a $f' = (^{a}\varphi', \widetilde{\varphi'})$, où $\varphi': B / \Re \to A / \Im$ est l'unique homomorphisme rendant commutatif le diagramme

$$
\begin{array}{c} \mathrm{B} \xrightarrow {\varphi} \mathrm{A} \\ \downarrow \qquad \qquad \qquad \downarrow \\ \mathrm{B} / \mathfrak {R} \xrightarrow [ \varphi^ {\prime} ]{} \mathrm{A} / \mathfrak {J} \end{array}\tag{10.5.6.2}
$$

L'existence de $\varphi'$ implique donc que $\varphi(\mathfrak{K})\subset\mathfrak{J}$. Inversement, si cette condition est vérifiée, en désignant par $\varphi'$ l'unique homomorphisme rendant commutatif le diagramme (10.5.6.2) et posant $f'=(^{a}\varphi',\widetilde{\varphi}')$, il est clair que le diagramme (10.5.6.1) est commutatif; la considération des homomorphismes $^{a}\varphi^{*}(\mathcal{O}_{\mathfrak{Y}})\to\mathcal{O}_{\mathfrak{X}}$ et $^{a}\varphi'^{*}(\mathcal{O}_{\mathfrak{Y}}/\mathcal{K})\to\mathcal{O}_{\mathfrak{X}}/\mathcal{J}$ correspondant à $f$ et $f'$ respectivement, montre alors que cela entraîne la relation $f^{*}(\mathcal{K})\mathcal{O}_{\mathfrak{X}}\subset\mathcal{J}$.

Il est clair que la correspondance  $f \rightarrow f'$  définie ci-dessus est fonctorielle.

## 10.6. Préschémas formels comme limites inductives de préschémas.

(10.6.1) Soient $\mathfrak{X}$ un préschéma formel, $(\mathcal{J}_{\lambda})$ un système fondamental d'Idéaux de définition de $\mathfrak{X}$; pour tout $\lambda$, soit $f_{\lambda}$ le morphisme canonique $(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}} / \mathcal{J}_{\lambda}) \to \mathfrak{X}$ (10.5.2); pour $\mathcal{J}_{\mu} \subset \mathcal{J}_{\lambda}$, l'homomorphisme canonique $\mathcal{O}_{\mathfrak{X}} / \mathcal{J}_{\mu} \to \mathcal{O}_{\mathfrak{X}} / \mathcal{J}_{\lambda}$ définit un morphisme

canonique $f_{\mu\lambda}:(\mathfrak{X},\mathcal{O}_{\mathfrak{x}}/\mathcal{J}_{\lambda})\to(\mathfrak{X},\mathcal{O}_{\mathfrak{x}}/\mathcal{J}_{\mu})$ de préschémas (usuels) tel que l'on ait $f_{\lambda}=f_{\mu}\circ f_{\mu\lambda}$. Les préschémas $\mathrm{X}_{\lambda}=(\mathfrak{X},\mathcal{O}_{\mathfrak{x}}/\mathcal{J}_{\lambda})$ et les morphismes $f_{\mu\lambda}$ constituent donc (en vertu de (10.4.8)) un système inductif dans la catégorie des préschémas formels.

Proposition (10.6.2). — Avec les notations de (10.6.1), le préschéma formel X et les morphismes  $f_{\lambda}$  constituent une limite inductive (T, I, 1.8) du système  $(\mathbf{X}_{\lambda}, f_{\mu\lambda})$  dans la catégorie des préschémas formels.

Soit Y un préschéma formel, et pour chaque indice λ, soit

$$
g _ {\lambda} = \left(\psi_ {\lambda}, \theta_ {\lambda}\right): \mathrm{X} _ {\lambda} \rightarrow \mathfrak {Y}
$$

un morphisme, tel que l'on ait $g_{\lambda} = g_{\mu} \circ f_{\mu \lambda}$ pour $\mathcal{J}_{\mu} \subset \mathcal{J}_{\lambda}$. Cette dernière condition et la définition des $X_{\lambda}$ entraînent d'abord que tous les $\psi_{\lambda}$ sont identiques à une même application continue $\psi : \mathfrak{X} \to \mathfrak{Y}$ des espaces sous-jacents ; en outre, les homomorphismes $\theta_{\lambda}^{\sharp} : \psi^{*}(\mathcal{O}_{\mathfrak{Y}}) \to \mathcal{O}_{X_i} = \mathcal{O}_{\mathfrak{X}} / \mathcal{J}_{\lambda}$ forment un système projectif d'homomorphismes de faisceaux d'anneaux. Par passage à la limite projective, on en déduit donc un homomorphisme $\omega : \psi^{*}(\mathcal{O}_{\mathfrak{Y}}) \to \varprojlim \mathcal{O}_{\mathfrak{X}} / \mathcal{J}_{\lambda} = \mathcal{O}_{\mathfrak{X}}$, et il est clair que le morphisme $g = (\psi, \omega^b)$ d'espaces annelés est le seul rendant commutatif les diagrammes

$$
\begin{array}{c} \mathbf {X} _ {\lambda} \stackrel {{g _ {\lambda}}} {{\to}} \mathfrak {Y} \\ f _ {\lambda} \searrow \nearrow_ {g} \\ \mathfrak {X} \end{array}\tag{10.6.2.1}
$$

Il reste donc à prouver que $g$ est un morphisme de préschémas formels ; la question étant locale sur $\mathfrak{X}$ et $\mathfrak{Y}$, on peut donc supposer $\mathfrak{X} = \mathrm{Spf}(A), \mathfrak{Y} = \mathrm{Spf}(B)$, A et B étant des anneaux admissibles, avec $\mathcal{J}_{\lambda} = \mathfrak{J}_{\lambda}^{\Delta}$, où $(\mathfrak{J}_{\lambda})$ est un système fondamental d'idéaux de définition de A (10.3.5) ; comme $A = \varprojlim A / \mathfrak{J}_{\lambda}$, l'existence d'un morphisme de schémas formels affines $g$ rendant commutatifs les diagrammes (10.6.2.1) résulte alors de la correspondance biunivoque (10.2.2) entre morphismes de schémas formels affines et homomorphismes continus d'anneaux, et de la définition de la limite projective. Mais l'unicité de $g$ en tant que morphisme d'espaces annelés montre qu'il coïncide avec le morphisme noté de même au début de la démonstration.

La proposition suivante établit, sous certaines conditions supplémentaires, l'existence de la limite inductive d'un système inductif donné de préschémas (usuels) dans la catégorie des préschémas formels :

Proposition (10.6.3). — Soient $\mathfrak{X}$ un espace topologique, $(\mathcal{O}_i, u_{ji})$ un système projectif de faisceaux d'anneaux sur $\mathfrak{X}$, ayant $\mathbf{N}$ pour ensemble d'indices. Soit $\mathcal{J}_i$ le noyau de $u_{0i}: \mathcal{O}_i \to \mathcal{O}_0$. On suppose que :

a) L'espace annelé (X, O$_{i}$) est un préschéma X$_{i}$.

b) Pour tout $x \in \mathbf{X}$ et tout $i$, il existe un voisinage ouvert $\mathbf{U}_i$ de $x$ dans $\mathfrak{X}$ tel que la restriction $\mathcal{J}_i | \mathbf{U}_i$ soit nilpotente.

c) Les homomorphismes $u_{ji}$ sont surjectifs.

Soit $\mathcal{O}_{\mathfrak{X}}$ le faisceau d'anneaux topologiques limite projective des faisceaux d'anneaux pseudodiscrets $\mathcal{O}_{i}$, et soit $u_{i}:\mathcal{O}_{\mathfrak{X}}\to\mathcal{O}_{i}$ l'homomorphisme canonique. Alors l'espace topologiquement annelé $(\mathfrak{X},\mathcal{O}_{\mathfrak{X}})$ est un préschéma formel; les homomorphismes $u_{i}$ sont surjectifs; leurs noyaux $\mathcal{J}^{(i)}$ forment un système fondamental d'Idéaux de définition de $\mathfrak{X}$, et $\mathcal{J}^{(0)}$ est la limite projective des faisceaux d'idéaux $\mathcal{J}_{i}$.

Notons d'abord que sur chaque fibre, $u_{ji}$ est un homomorphisme surjectif et a fortiori un homomorphisme local ; donc $v_{ij} = (\mathbf{1}_{\mathfrak{X}}, u_{ji})$ est un morphisme de préschémas $\mathbf{X}_j \to \mathbf{X}_i$ ($i \geqslant j$) (2.2.1). Supposons d'abord que chaque $\mathbf{X}_i$ soit un schéma affine d'anneau $\mathbf{A}_i$. Il existe un homomorphisme d'anneaux $\varphi_{ji}: \mathbf{A}_i \to \mathbf{A}_j$ tel que $u_{ji} = \widetilde{\varphi}_{ji}$ (1.7.3) ; par suite (1.6.3), le faisceau $\mathcal{O}_j$ est un $\mathcal{O}_i$-Module quasi-cohérent sur $\mathbf{X}_i$ (pour la loi externe définie par $u_{ji}$), associé à $\mathbf{A}_j$ considéré comme $\mathbf{A}_i$-module à l'aide de $\varphi_{ji}$. Pour tout $f \in \mathbf{A}_i$, soit $f' = \varphi_{ji}(f)$; par hypothèse, les ouverts $\mathbf{D}(f)$ et $\mathbf{D}(f')$ sont identiques dans $\mathfrak{X}$, et l'homomorphisme de $\Gamma(\mathbf{D}(f), \mathcal{O}_i) = (\mathbf{A}_i)_f$ dans $\Gamma(\mathbf{D}(f), \mathcal{O}_j) = (\mathbf{A}_j)_{f'}$ correspondant à $u_{ji}$ n'est autre que $(\varphi_{ji})_f$ (1.6.1). Mais lorsqu'on considère $\mathbf{A}_j$ comme $\mathbf{A}_i$-module, $(\mathbf{A}_j)_{f'}$ est le $(\mathbf{A}_i)_f$-module $(\mathbf{A}_j)_f$, donc on a aussi $u_{ji} = \widetilde{\varphi}_{ji}$, lorsque $\varphi_{ji}$ est cette fois considéré comme homomorphisme de $\mathbf{A}_i$-modules. Alors, comme $u_{ji}$ est surjectif, on en conclut que $\varphi_{ji}$ l'est aussi (1.3.9) et si $\mathfrak{J}_{ji}$ est le noyau de $\varphi_{ji}$, le noyau de $u_{ji}$ est un $\mathcal{O}_i$-Module quasi-cohérent égal à $\widetilde{\mathfrak{J}}_{ji}$. En particulier, on a $\mathcal{J}_i = \widetilde{\mathfrak{J}}_i$, où $\mathfrak{J}_i$ est le noyau de $\varphi_{0i}: \mathbf{A}_i \to \mathbf{A}_0$. L'hypothèse b) entraîne que $\mathcal{J}_i$ est nilpotent : en effet, comme X est quasicompact, on peut recouvrir X par un nombre fini d'ouverts $U_k$ tels que $(\mathcal{J}_i | U_k)^n_k = o$ et en prenant pour n le plus grand des $n_k$, on a $\mathcal{J}_i^n = o$. On en conclut que $\mathfrak{J}_i$ est nilpotent (1.3.13). Alors l'anneau $A = \lim_{\leftarrow} A_i$ est admissible (0, 7.2.2), l'homomorphisme canonique $\varphi_i: A \to A_i$ est surjectif et son noyau $\mathfrak{J}^{(i)}$ est égal à la limite projective des $\mathfrak{J}_{ik}$ pour $k \geqslant i$; les $\mathfrak{J}^{(i)}$ forment un système fondamental de voisinages de o dans A. Les assertions de (10.6.3) résultent dans ce cas de (10.1.1) et (10.3.2), $(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}})$ n'étant autre que Spf(A).

Toujours dans ce même cas particulier, notons que si $f=(f_{i})$ est un élément de la limite projective $\mathbf{A}=\lim_{\leftarrow}\mathbf{A}_{i}$, tous les ouverts $\mathbf{D}(f_{i})$ (ouvert affine dans $\mathbf{X}_{i}$) s'identifient à l'ouvert $\mathfrak{D}(f)$ de $\mathfrak{X}$, le préschéma induit par $\mathbf{X}_{i}$ sur $\mathfrak{D}(f)$ s'identifiant donc au schéma affine $\operatorname{Spec}((\mathbf{A}_{i})_{f_{i}})$.

Dans le cas général, remarquons d'abord que pour tout ouvert quasi-compact U de $\mathfrak{X}$, chacun des $\mathcal{J}_i|U$ est nilpotent, comme le montre le raisonnement fait ci-dessus. Nous allons voir que pour tout $x\in\mathfrak{X}$, il y a un voisinage ouvert U de $x$ dans $\mathfrak{X}$ qui est un ouvert affine pour tous les $X_i$. En effet, prenons U ouvert affine pour $X_0$, et observons que $\mathcal{O}_{X_0}=\mathcal{O}_{X_i}/\mathcal{J}_i$. Comme $\mathcal{J}_i|U$ est nilpotent, en vertu de ce qui précède, U est ouvert affine aussi pour chaque $X_i$ en vertu de (5.1.9). Cela étant, pour tout U satisfaisant aux conditions précédentes, l'étude du cas affine faite plus haut montre que $(U,\mathcal{O}_X|U)$ est un préschéma formel dont les $\mathcal{J}^{(i)}|U$ forment un système fondamental d'idéaux de définition et $\mathcal{J}^{(0)}|U$ est limite projective des $\mathcal{J}_i|U$; d'où la conclusion.

Corollaire (10.6.4). — Supposons que pour $i \geqslant j$, le noyau de $u_{ji}$ soit $\mathcal{J}_i^{j+1}$ et que $\mathcal{J}_1 / \mathcal{J}_1^2$

soit de type fini sur $\mathcal{O}_{0}=\mathcal{O}_{1}/\mathcal{J}_{1}$. Alors $\mathfrak{X}$ est un préschéma formel adique, et si $\mathcal{J}^{(n)}$ est le noyau de $\mathcal{O}_{\mathfrak{X}}\to\mathcal{O}_{n}$, on a $\mathcal{J}^{(n)}=\mathcal{J}^{n+1}$ et $\mathcal{J}/\mathcal{J}^{2}$ est isomorphe à $\mathcal{J}_{1}$. Si en outre $\mathrm{X}_{0}$ est localement noethérien (resp. noethérien), $\mathfrak{X}$ est localement noethérien (resp. noethérien).

Comme les espaces sous-jacents à $\mathfrak{X}$ et $X_0$ sont les mêmes, la question est locale et l'on peut supposer tous les $X_i$ affines; compte tenu des relations $\mathcal{J}_{ij} = \widetilde{\mathfrak{J}}_{ji}$ (avec les notations de (10.6.3)), on est aussitôt ramené aux assertions correspondantes de (0, 7.2.7 et 7.2.8), en notant que $\mathfrak{J}_1 / \mathfrak{J}_1^2$ est alors un $A_0$-module de type fini (1.3.9).

En particulier, tout préschéma formel localement noethérien $\mathfrak{X}$ est limite inductive d'une suite $(\mathbf{X}_n)$ de préschémas (usuels) localement noethériens vérifiant les conditions de (10.6.3) et (10.6.4): il suffit de considérer un Idéal de définition $\mathcal{J}$ de $\mathfrak{X}$ (10.5.4) et de prendre $\mathbf{X}_n = (\mathfrak{X}, \mathcal{O}_{\mathfrak{X}} / \mathcal{J}^{n+1})$ ((10.5.1) et (10.6.2)).

Corollaire (10.6.5). — Soit A un anneau admissible. Pour que le schéma formel affine $\mathfrak{X} = \operatorname{Spf}(A)$ soit noethérien, il faut et il suffit que A soit adique et noethérien.

La condition est évidemment suffisante. Inversement, supposons que $\mathfrak{X}$ soit noethérien, et soient $\mathfrak{J}$ un idéal de définition de A, $\mathcal{J} = \mathfrak{J}^{\Delta}$ l'Idéal de définition correspondant de $\mathfrak{X}$. Les préschémas (usuels) $X_{n} = (\mathfrak{X},\mathcal{O}_{\mathfrak{X}} / \mathcal{J}^{n + 1})$ sont alors affines et noethériens, donc les anneaux $A_{n} = A / \mathfrak{J}^{n + 1}$ sont noethériens (6.1.3), d'où on conclut que $\mathfrak{J} / \mathfrak{J}^2$ est un A/$\mathfrak{J}$-module de type fini. Comme les $\mathcal{J}^n$ forment un système fondamental d'Idéaux de définition de $\mathfrak{X}$ (10.5.1), on a $\mathcal{O}_{\mathfrak{X}} = \varprojlim (\mathcal{O}_{\mathfrak{X}} / \mathcal{J}^n)$ (10.5.3); on en conclut (10.1.3) que A est topologiquement isomorphe à $\varprojlim A / \mathfrak{J}^n$, donc est adique et noethérien (0, 7.2.8).

Remarque (10.6.6). — Avec les notations de (10.6.3), soit $\mathcal{F}_i$ un $\mathcal{O}_i$-Module, et supposons donné, pour $i \geqslant j$, un $v_{ij}$-morphisme $\theta_{ji}: \mathcal{F}_i \to \mathcal{F}_j$, de sorte que $\theta_{kj} \circ \theta_{ji} = \theta_{ki}$ pour $k \leqslant j \leqslant i$. Comme l'application continue sous-jacente à $v_{ij}$ est l'identité, $\theta_{ji}$ est un homomorphisme de faisceaux de groupes abéliens sur l'espace $\mathfrak{X}$; en outre, si $\mathcal{F}$ est la limite projective du système projectif ($\mathcal{F}_i$) de faisceaux de groupes abéliens, le fait que les $\theta_{ji}$ sont des $v_{ij}$-morphismes permet de définir sur $\mathcal{F}$ une structure de $\mathcal{O}_{\mathfrak{x}}$-Module par passage à la limite projective; muni de cette structure, nous dirons que $\mathcal{F}$ est la limite projective (pour les $\theta_{ji}$) du système de $\mathcal{O}_i$-Modules ($\mathcal{F}_i$). Dans le cas particulier où $v_{ij}^*(\mathcal{F}_i) = \mathcal{F}_j$ et où $\theta_{ji}$ est l'identité, nous dirons pour abréger, que $\mathcal{F}$ est la limite projective d'un système ($\mathcal{F}_i$) tel que $v_{ij}^*(\mathcal{F}_i) = \mathcal{F}_j$ pour $j \leqslant i$ (sans mentionner les $\theta_{ji}$).

(10.6.7) Soient $\mathfrak{X},\mathfrak{Y}$ deux préschémas formels, $\mathcal{J}$ (resp. $\mathcal{K}$) un Idéal de définition de $\mathfrak{X}$ (resp. $\mathfrak{Y}$), $f:\mathfrak{X}\to\mathfrak{Y}$ un morphisme tel que $f^{*}(\mathcal{K})\mathcal{O}_{\mathfrak{X}}\subset\mathcal{J}$. On a alors pour tout entier $n>0$, $f^{*}(\mathcal{K}^{n})\mathcal{O}_{\mathfrak{X}}=(f^{*}(\mathcal{K})\mathcal{O}_{\mathfrak{X}})^{n}\subset\mathcal{J}^{n}$; on peut donc (10.5.6) déduire de $f$ un morphisme de préschémas (usuels) $f_{n}:X_{n}\to Y_{n}$, en posant $X_{n}=(\mathfrak{X},\mathcal{O}_{\mathfrak{X}}/\mathcal{J}^{n+1})$, $Y_{n}=(\mathfrak{Y},\mathcal{O}_{\mathfrak{Y}}/\mathcal{K}^{n+1})$, et il résulte aussitôt des définitions que les diagrammes

$$
\begin{array}{c c c} \mathbf {X} _ {m} & \stackrel {{f _ {m}}} {{\to}} & \mathbf {Y} _ {m} \\ \downarrow & & \downarrow \\ \mathbf {X} _ {n} & \stackrel {{f _ {n}}} {{\to}} & \mathbf {Y} _ {n} \end{array}\tag{10.6.7.1}
$$

sont commutatifs pour $m \leqslant n$; autrement dit, $(f_n)$ est un système inductif de morphismes. (10.6.8) Inversement, soit $(\mathbf{X}_n)$ (resp. $(\mathbf{Y}_n)$) un système inductif de préschémas (usuels) satisfaisant aux conditions $b$ et $c$) de (10.6.3), et soit $\mathfrak{X}$ (resp. $\mathfrak{Y}$) sa limite inductive. Par définition des limites inductives, toute suite $(f_n)$ de morphismes $\mathbf{X}_n \to \mathbf{Y}_n$ formant un système inductif admet une limite inductive $f: \mathfrak{X} \to \mathfrak{Y}$, qui est l'unique morphisme de préschémas formels rendant commutatifs les diagrammes

$$
\begin{array}{c} \mathbf {X} _ {n} \xrightarrow {f _ {n}} \mathbf {Y} _ {n} \\ \downarrow \qquad \qquad \qquad \qquad \qquad \downarrow \\ \mathfrak {X} \xrightarrow [ t ]{} \mathfrak {Y} \end{array}
$$

Proposition (10.6.9). — Soient $\mathfrak{X}$, $\mathfrak{Y}$ deux préschémas formels localement noethériens, $\mathcal{J}$ (resp. $\mathcal{K}$) un Idéal de définition de $\mathfrak{X}$ (resp. $\mathfrak{Y}$); l'application $f\to(f_n)$ définie dans (10.6.7) est une bijection de l'ensemble des morphismes $f:\mathfrak{X}\to\mathfrak{Y}$ tels que $f^{*}(\mathcal{K})\mathcal{O}_{\mathfrak{X}}\subset\mathcal{J}$, sur l'ensemble des suites ($f_n$) de morphismes rendant commutatifs les diagrammes (10.6.7.1).

Si $f$ est la limite inductive d'une telle suite, il faut montrer que $f^{*}(\mathcal{K})\mathcal{O}_{\mathfrak{X}} \subset \mathcal{J}$. La question étant locale sur $\mathfrak{X}$ et $\mathfrak{Y}$, on peut se borner au cas où $\mathfrak{X} = \operatorname{Spf}(A)$, $\mathfrak{Y} = \operatorname{Spf}(B)$ sont affines, $A$ et $B$ étant adiques noethériens, $\mathcal{J} = \mathfrak{J}^{\Delta}, \mathcal{K} = \mathfrak{R}^{\Delta}$, où $\mathfrak{J}$ (resp. $\mathfrak{R}$) est un idéal de définition de $A$ (resp. $B$). On a alors $X_{n} = \operatorname{Spec}(A_{n})$, $Y_{n} = \operatorname{Spec}(B_{n})$, avec $A_{n} = A / \mathfrak{J}^{n+1}$ et $B_{n} = B / \mathfrak{R}^{n+1}$, en vertu de (10.3.6) et (10.3.2); $f_{n} = (^{a}\varphi_{n}, \widetilde{\varphi}_{n})$, où les homomorphismes $\varphi_{n}: B_{n} \to A_{n}$ forment un système projectif, donc $f = (^{a}\varphi, \widetilde{\varphi})$, où $\varphi = \varprojlim \varphi_{n}$. La commutativité du diagramme (10.6.7.1) pour $m = 0$ donne alors la condition $\varphi_{n}(\mathfrak{R}/\mathfrak{R}^{n+1}) \subset \mathfrak{J}/\mathfrak{J}^{n+1}$ pour tout $n$, donc, en passant à la limite projective, $\varphi(\mathfrak{R}) \subset \mathfrak{J}$, et cela entraîne $f^{*}(\mathcal{K})\mathcal{O}_{\mathfrak{X}} \subset \mathcal{J}$ (10.5.6, (ii)).

Corollaire (10.6.10). — Soient $\mathfrak{X}$, $\mathfrak{Y}$ deux préschémas formels localement noethériens, $\mathcal{T}$ le plus grand Idéal de définition de $\mathfrak{X}$ (10.5.4).

(i) Pour tout Idéal de définition $\mathcal{K}$ de $\mathfrak{Y}$ et tout morphisme $f:\mathfrak{X}\to\mathfrak{Y}$, on a $f^{*}(\mathcal{K})\mathcal{O}_{\mathfrak{X}}\subset\mathcal{T}$.

(ii) Il y a correspondance biunivoque canonique entre $\operatorname{Hom}(\mathfrak{X},\mathfrak{Y})$ et l'ensemble des suites $(f_n)$ de morphismes rendant commutatifs les diagrammes (10.6.7.1), où $\mathbf{X}_n = (\mathfrak{X},\mathcal{O}_{\mathfrak{X}} / \mathcal{T}^{n + 1}),$$\mathrm{Y}_n = (\mathfrak{Y},\mathcal{O}_{\mathfrak{Y}} / \mathcal{K}^{n + 1})$

(ii) résulte aussitôt de (i) et de (10.6.9). Pour démontrer (i), on peut se borner au cas où $\mathfrak{X} = \operatorname{Spf}(A)$, $\mathfrak{Y} = \operatorname{Spf}(B)$, A et B étant noethériens, $\mathcal{T} = \mathfrak{T}^{\Delta}$, $\mathcal{K} = \mathfrak{K}^{\Delta}$, où $\mathfrak{T}$ est le plus grand idéal de définition de A et $\mathfrak{K}$ un idéal de définition de B. Soit $f = (^{a}\varphi, \widetilde{\varphi})$, où $\varphi : B \to A$ est un homomorphisme continu ; comme les éléments de $\mathfrak{K}$ sont topologiquement nilpotents (0, 7.1.4, (ii)), il en est de même de ceux de $\varphi(\mathfrak{K})$, donc $\varphi(\mathfrak{K}) \subset \mathfrak{T}$ puisque $\mathfrak{T}$ est l'ensemble des éléments topologiquement nilpotents de A (0, 7.1.6) ; d'où la conclusion en vertu de (10.5.6, (ii)).

Corollaire (10.6.11). — Soient S, X, Y trois préschémas formels localement noethériens,  $f: X \to S$ ,  $g: Y \to S$  des morphismes faisant de X et Y des S-préschémas formels. Soit J (resp. K, L) un Idéal de définition de S (resp. X, Y), et supposons que  $f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}} \subset \mathcal{K}$ ,  $g^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{Y}} = \mathcal{L}$ ; posons  $S_{n} = (\mathfrak{S}, \mathcal{O}_{\mathfrak{S}} / \mathcal{J}^{n+1})$ ,  $X_{n} = (\mathfrak{X}, \mathcal{O}_{\mathfrak{X}} / \mathcal{K}^{n+1})$ ,  $Y_{n} = (\mathfrak{Y}, \mathcal{O}_{\mathfrak{Y}} / \mathcal{L}^{n+1})$ . Il y a alors correspondance

biunivoque canonique entre $\mathrm{Hom}_{\mathfrak{S}}(\mathfrak{X},\mathfrak{Y})$ et l'ensemble des suites $(u_n)$ de $\mathbf{S}_n$-morphisms $u_n: \mathbf{X}_n \to \mathbf{Y}_n$ rendant commutatifs les diagrammes (10.6.7.1).

Pour tout S-morphisme  $u : X \to Y$ , on a par définition  $f = g \circ u$ , donc

$$
u ^ {*} (\mathcal {L}) \mathcal {O} _ {\mathfrak {X}} = u ^ {*} (g ^ {*} (\mathcal {J}) \mathcal {O} _ {\mathfrak {Y}}) \mathcal {O} _ {\mathfrak {X}} = f ^ {*} (\mathcal {J}) \mathcal {O} _ {\mathfrak {X}} \subset \mathscr {K}
$$

le corollaire découle donc de (10.6.9).

On notera que, pour $m \leqslant n$, la donnée d'un morphisme $f_n: \mathbf{X}_n \to \mathbf{Y}_n$ détermine un morphisme et un seul $f_m: \mathbf{X}_m \to \mathbf{Y}_m$ rendant commutatif le diagramme (10.6.7.1), comme on le voit aussitôt en se ramenant au cas affine ; on a ainsi défini une application $\varphi_{mn}: \operatorname{Hom}_{\mathrm{S}_n}(\mathbf{X}_n, \mathbf{Y}_n) \to \operatorname{Hom}_{\mathrm{S}_m}(\mathbf{X}_m, \mathbf{Y}_m)$ et les $\operatorname{Hom}_{\mathrm{S}_n}(\mathbf{X}_n, \mathbf{Y}_n)$ forment pour les $\varphi_{mn}$ un système projectif d'ensembles ; (10.6.11) s'énonce encore en disant qu'il existe une bijection canonique

$$
\operatorname{Hom} _ {\mathfrak {S}} (\mathfrak {X}, \mathfrak {Y}) \xrightarrow [ \leftarrow n ]{\sim} \lim _ {\mathrm{Hom} _ {\mathrm{S} _ {n}}} (\mathrm{X} _ {n}, \mathrm{Y} _ {n}).
$$

## 10.7. Produit de préschémas formels.

(10.7.1) Soit S un préschéma formel; les S-préschémas formels formant une catégorie, on peut définir la notion de produit de S-préschémas formels.

Proposition (10.7.2). — Soient $\mathfrak{X} = \operatorname{Spf}(B)$, $\mathfrak{Y} = \operatorname{Spf}(C)$ deux schémas formels affines au-dessus d'un schéma formel affine $\mathfrak{S} = \operatorname{Spf}(A)$. Soient $3 = \operatorname{Spf}(B\widehat{\otimes}_{A}C)$, $p_1, p_2$ les $\mathfrak{S}$-morphismes correspondant (10.2.2) aux A-homomorphismes canoniques (continus) $\rho$ et $\sigma$ de B et C dans $B\widehat{\otimes}_{A}C$; alors $(3, p_1, p_2)$ est un produit des $\mathfrak{S}$-schémas formels affines $\mathfrak{X}$ et $\mathfrak{Y}$.

En vertu de (10.4.6), tout revient à vérifier que si, à tout A-homomorphisme continu $\varphi : B\widehat{\otimes}_{A}C \to D$, où $D$ est un anneau admissible qui est une A-algèbre topologique, on associe le couple ($\varphi \circ \rho$, $\varphi \circ \sigma$), on définit une bijection

$$
\operatorname{Hom} _ {\mathrm{A}} (\mathrm{B} \widehat {\otimes} _ {\mathrm{A}} \mathrm{C}, \mathrm{D}) \xrightarrow {\sim} \operatorname{Hom} _ {\mathrm{A}} (\mathrm{B}, \mathrm{D}) \times \operatorname{Hom} _ {\mathrm{A}} (\mathrm{C}, \mathrm{D})
$$

ce qui n'est autre que la propriété universelle du produit tensoriel complété (0, 7.7.6).

Proposition (10.7.3). — Étant donnés deux S-préschémas formels X, Y, le produit  $X \times_{\otimes} Y$  existe.

La démonstration est identique à celle de (3.2.6), en y remplaçant les schémas affines (resp. les ouverts affines) par les schémas formels affines (resp. les ouverts formels affines), et la prop. (3.2.2) par (10.7.2).

Toutes les propriétés formelles du produit de préschémas (3.2.7 et 3.2.8, 3.3.1 à 3.3.12) sont valables sans aucune modification pour le produit de préschémas formels.

(10.7.4) Soient S, X, Y trois préschémas formels et soient $f: \mathfrak{X} \to \mathfrak{S}$, $g: \mathfrak{Y} \to \mathfrak{S}$ deux morphismes. Supposons qu'il existe dans S, X, Y respectivement, trois systèmes fondamentaux d'Idéaux de définition $(\mathcal{J}_{\lambda})$, $(\mathcal{K}_{\lambda})$, $(\mathcal{L}_{\lambda})$ respectivement, ayant même ensemble d'indices I, tels que $f^{*}(\mathcal{J}_{\lambda})\mathcal{O}_{\mathfrak{X}} \subset \mathcal{K}_{\lambda}$ et $g^{*}(\mathcal{J}_{\lambda})\mathcal{O}_{\mathfrak{Y}} \subset \mathcal{L}_{\lambda}$ pour tout λ. Posons $S_{\lambda} = (\mathfrak{S}, \mathcal{O}_{\mathfrak{S}} / \mathcal{J}_{\lambda})$, $X_{\lambda} = (\mathfrak{X}, \mathcal{O}_{\mathfrak{X}} / \mathcal{K}_{\lambda})$, $Y_{\lambda} = (\mathfrak{Y}, \mathcal{O}_{\mathfrak{Y}} / \mathcal{L}_{\lambda})$; pour $\mathcal{J}_{\mu} \subset \mathcal{J}_{\lambda}, \mathcal{K}_{\mu} \subset \mathcal{K}_{\lambda}, \mathcal{L}_{\mu} \subset \mathcal{L}_{\lambda}$, notons que $S_{\lambda}$ (resp. $X_{\lambda}, Y_{\lambda}$) est un sous-préschéma fermé de $S_{\mu}$ (resp. $X_{\mu}, Y_{\mu}$) ayant même

espace sous-jacent (10.6.1). Comme  $S_{\lambda}\rightarrow S_{\mu}$  est un monomorphisme de préschémas, on voit donc d'abord que les produits  $X_{\lambda}\times_{S_{\lambda}}Y_{\lambda}$  et  $X_{\lambda}\times_{S_{\mu}}Y_{\lambda}$  sont identiques (3.2.4), puis que  $X_{\lambda}\times_{S_{\mu}}Y_{\lambda}$  s'identifie à un sous-préschéma fermé de  $X_{\mu}\times_{S_{\mu}}Y_{\mu}$  ayant même espace sous-jacent (4.3.1). Cela étant, le produit  $X\times_{S}Y$  est la limite inductive des préschémas usuels  $X_{\lambda}\times_{S_{\lambda}}Y_{\lambda}$  : en effet, on voit comme dans (10.6.2) qu'on peut se ramener au cas où S, X et Y sont des schémas formels affines. Compte tenu de (10.5.6, (ii)) et de l'hypothèse sur les systèmes fondamentaux d'Idéaux de définition de S, X et Y, on voit aussitôt que notre assertion résulte de la définition du produit tensoriel complété de deux algèbres (0, 7.7.1).

En outre, soit 3 un S-préschéma formel,  $(\mathcal{M}_{\lambda})$  un système fondamental d'Idéaux de définition de 3 ayant I comme ensemble d'indices,  $u:3\to X, v:3\to Y$  deux S-morphismes tels que  $u^{*}(\mathcal{K}_{\lambda})\mathcal{O}_{3}\subset\mathcal{M}_{\lambda}$  et  $v^{*}(\mathcal{L}_{\lambda})\mathcal{O}_{3}\subset\mathcal{M}_{\lambda}$ . Si l'on pose  $Z_{\lambda}=(3,\mathcal{O}_{3}/\mathcal{M}_{\lambda})$ , et si  $u_{\lambda}:Z_{\lambda}\to X_{\lambda}$  et  $v_{\lambda}:Z_{\lambda}\to Y_{\lambda}$  sont les  $S_{\lambda}$ -morphismes correspondant à u et v (10.5.6), on vérifie aussitôt que  $(u,v)_{\mathfrak{S}}$  est la limite inductive des  $S_{\lambda}$ -morphismes  $(u_{\lambda},v_{\lambda})_{S_{\lambda}}$ .

Les considérations de ce numéro s'appliquent en particulier lorsque $\mathfrak{S}$, $\mathfrak{X}$ et $\mathfrak{Y}$ sont localement noethériens, en prenant comme systèmes fondamentaux d'Idéaux de définition les systèmes formés des puissances d'un Idéal de définition (10.5.1). Mais on notera que $\mathfrak{X} \times_{\mathfrak{S}} \mathfrak{Y}$ n'est pas nécessairement localement noethérien (voir toutefois (10.13.5)).

## 10.8. Complété formel d'un préschéma le long d'une partie fermée.

(10.8.1) Soient X un préschéma (usuel) localement noethérien, X' une partie fermée de l'espace sous-jacent à X ; désignons par Φ l'ensemble des faisceaux cohérents d'idéaux J dans Ox, tels que le support de Ox/J soit X'. L'ensemble Φ n'est pas vide (5.2.1, 4.1.4 et 6.1.1) ; nous l'ordonnerons par la relation ⊃.

Lemme (10.8.2). — L'ensemble ordonné $\Phi$ est filtrant; si X est noethérien, pour tout $\mathcal{J}_{0}\in\Phi$, l'ensemble des puissances $\mathcal{J}_{0}^{n}$ ($n>0$) est cofinal à $\Phi$.

En effet, si $\mathcal{J}_1$ et $\mathcal{J}_2$ appartiennent à $\Phi$, et si on pose $\mathcal{J} = \mathcal{J}_1 \cap \mathcal{J}_2$, $\mathcal{J}$ est cohérent puisque $\mathcal{O}_{\mathrm{X}}$ est cohérent (6.1.1 et 0, 5.3.4), et l'on a $\mathcal{J}_x = (\mathcal{J}_1)_x \cap (\mathcal{J}_2)_x$, pour tout $x \in \mathrm{X}$, donc $\mathcal{J}_x = \mathcal{O}_x$ pour $x \notin \mathrm{X}'$ et $\mathcal{J}_x \neq \mathcal{O}_x$ pour $x \in \mathrm{X}'$, ce qui prouve que $\mathcal{J} \in \Phi$. D'autre part, si X est noethérien, et si $\mathcal{J}_0$ et $\mathcal{J}$ appartiennent à $\Phi$, il existe un entier $n > o$ tel que $\mathcal{J}_0^n (\mathcal{O}_{\mathrm{X}} / \mathcal{J}) = o$ (9.3.4), ce qui signifie que $\mathcal{J}_0^n \subset \mathcal{J}$.

(10.8.3) Soit maintenant $\mathcal{F}$ un $\mathcal{O}_{\mathrm{X}}$-Module cohérent; pour tout $\mathcal{J} \in \Phi$, $\mathcal{F} \otimes_{\mathcal{O}_{\mathrm{X}}} (\mathcal{O}_{\mathrm{X}} / \mathcal{J})$ est un $\mathcal{O}_{\mathrm{X}}$-Module cohérent (9.1.1), de support contenu dans $\mathbf{X}'$, et que nous identifierons le plus souvent à sa restriction à $\mathbf{X}'$. Lorsque $\mathcal{J}$ parcourt $\Phi$, ces faisceaux forment un système projectif de faisceaux de groupes abéliens.

Définition (10.8.4). — Étant donnés une partie fermée X' d'un préschéma localement noethérien X et un O$_{X}$-Module cohérent F, on appelle complété de F le long de X' et on désigne par F$_{|X'}$ ou par F (lorsqu'aucune confusion n'est possible) la restriction à X' du faisceau

$\lim_{\overleftarrow{\Phi}}(\mathcal{F}\otimes_{\mathcal{O}_{X}}(\mathcal{O}_{X}/\mathcal{J}))$ ; on dit que ses sections au-dessus de $\mathbf{X}'$ sont les sections formelles de $\mathcal{F}$

$$
\mathbf {X} ^ {\prime}
$$

Il est immédiat que pour tout ouvert $\mathrm{U} \subset \mathrm{X}$, on a $(\mathcal{F} | \mathrm{U})_{/(\mathrm{U} \cap \mathrm{X}')} = (\mathcal{F}_{/\mathrm{X}'}) | (\mathrm{U} \cap \mathrm{X}')$.

Par passage à la limite projective, il est clair que  $(\mathcal{O}_{\mathrm{X}})_{/ \mathrm{X}'}$  est un faisceau d'anneaux, et que  $F_{/X'}$  peut être considéré comme un  $(\mathcal{O}_{\mathrm{X}})_{/ \mathrm{X}'}$ -Module. En outre, comme il existe une base de la topologie de  $X'$  formée d'ouverts quasi-compacts, on peut considérer  $(\mathcal{O}_{\mathrm{X}})_{/ \mathrm{X}'}$  (resp.  $F_{/X'}$ ) comme un faisceau d'anneaux topologiques (resp. de groupes topologiques) limite projective des faisceaux d'anneaux (resp. groupes) pseudo-discrets  $O_{X}/J$  (resp.  $\mathcal{F}\otimes_{\mathcal{O}_{\mathrm{X}}}(\mathcal{O}_{\mathrm{X}}/\mathcal{J})=\mathcal{F}/\mathcal{J}\mathcal{F}$ ), et, par passage à la limite projective,  $F_{/X'}$  devient alors un  $(\mathcal{O}_{\mathrm{X}})_{/ \mathrm{X}'}$ -Module topologique (0, 3.8.1 et 3.8.2); rappelons que pour tout ouvert quasi-compact  $U\subset X$,  $\Gamma(\mathrm{U}\cap\mathrm{X}', (\mathcal{O}_{\mathrm{X}})_{/ \mathrm{X}'})$  (resp.  $\Gamma(\mathrm{U}\cap\mathrm{X}', \mathcal{F}_{/ \mathrm{X}'})$ ) est alors limite projective des anneaux (resp. groupes) discrets  $\Gamma(\mathrm{U}, \mathcal{O}_{\mathrm{X}}/\mathcal{J})$  (resp.  $\Gamma(\mathrm{U}, \mathcal{F}/\mathcal{J}\mathcal{F})$ ).

Si maintenant $u: \mathcal{F} \to \mathcal{G}$ est un homomorphisme de $\mathcal{O}_{\mathrm{X}}$-Modules, on en déduit canoniquement des homomorphismes $u_{\mathfrak{J}}: \mathcal{F} \otimes_{\mathcal{O}_{\mathrm{X}}} (\mathcal{O}_{\mathrm{X}} / \mathcal{J}) \to \mathcal{G} \otimes_{\mathcal{O}_{\mathrm{X}}} (\mathcal{O}_{\mathrm{X}} / \mathcal{J})$ pour tout $\mathcal{J} \in \Phi$, et ces homomorphismes forment un système projectif. Par passage à la limite projective et restriction à $\mathrm{X}'$, ils donnent donc un $(\mathcal{O}_{\mathrm{X}})_{/ \mathrm{X}'}$-homomorphisme continu $\mathcal{F}_{| \mathrm{X}'} \to \mathcal{G}_{| \mathrm{X}'}$, noté $u_{| \mathrm{X}'}$ ou $\hat{u}$, et appelé le complété de l'homomorphisme $u$ le long de $\mathrm{X}'$. Il est clair que si $v: \mathcal{G} \to \mathcal{H}$ est un second homomorphisme de $\mathcal{O}_{\mathrm{X}}$-Modules, on a $(v \circ u)_{/ \mathrm{X}'} = (v_{| \mathrm{X}'}) \circ (u_{| \mathrm{X}'})$ donc $\mathcal{F}_{| \mathrm{X}'}$ est un foncteur additif covariant en $\mathcal{F}$, de la catégorie des $\mathcal{O}_{\mathrm{X}}$-Modules cohérents, à valeurs dans la catégorie des $(\mathcal{O}_{\mathrm{X}})_{/ \mathrm{X}'}$-Modules topologiques.

Proposition (10.8.5). — Le support de  $(\mathcal{O}_{\mathrm{X}})_{/ \mathrm{X}'}$  est  $X'$ ; l'espace topologiquement annelé  $(\mathrm{X}', (\mathcal{O}_{\mathrm{X}})_{/ \mathrm{X}'})$  est un préschéma formel localement noethérien, et si  $J \in \Phi$ ,  $J_{/X'}$  est un Idéal de définition de ce préschéma formel. Si  $\mathrm{X} = \operatorname{Spec}(\mathrm{A})$  est un schéma affine d'anneau noethérien,  $J = \widetilde{J}$ , où J est un idéal de A, et  $\mathrm{X}' = \mathrm{V}(\mathfrak{J})$ ,  $(\mathrm{X}', (\mathcal{O}_{\mathrm{X}})_{/ \mathrm{X}'})$  s'identifie canoniquement à Spf( $\hat{A}$ ), où  $\hat{A}$  est le séparé complété de A pour la topologie J-préadique.

On peut évidemment se borner à prouver la dernière assertion. On sait (0, 7.3.3) que le séparé complété $\hat{\mathfrak{J}}$ de $\mathfrak{J}$ pour la topologie $\mathfrak{J}$-préadique s'identifie à l'idéal $\mathfrak{J}\hat{\mathbf{A}}$ de $\hat{\mathbf{A}}$, et que $\hat{\mathbf{A}}$ est un anneau $\hat{\mathfrak{J}}$-adique noethérien tel que $\hat{\mathbf{A}}/\hat{\mathfrak{J}}^{n}=\mathbf{A}/\mathfrak{J}^{n}$ (0, 7.2.6). Cette dernière relation montre que les idéaux premiers ouverts de $\hat{\mathbf{A}}$ sont les idéaux $\hat{\mathfrak{p}}=\mathfrak{p}\hat{\mathfrak{J}}$, où $\mathfrak{p}$ est un idéal premier de A contenant $\mathfrak{J}$, et que l'on a $\hat{\mathfrak{p}}\cap\mathbf{A}=\mathfrak{p}$, d'où $\operatorname{Spf}(\hat{\mathbf{A}})=\mathbf{X}'$. Comme $\mathcal{O}_{\mathrm{X}}/\mathcal{J}^{n}=(\mathrm{A}/\mathfrak{J}^{n})\sim$, la proposition découle aussitôt des définitions.

On dit que le préschéma formel ainsi défini est le complété de X le long de X' et on le note  $X_{/X'}$  ou  $\hat{X}$  si aucune confusion n'est à craindre. Lorsque l'on prend  $X'=X$, on peut prendre J=0, et on a donc  $X_{/X}=X$.

Il est clair que si U est un sous-préschéma induit sur un ouvert de X,  $\mathrm{U}_{/(\mathrm{U}\cap\mathrm{X}^{\prime})}$  s'identifie canoniquement au sous-préschéma formel induit par  $X_{/X'}$  sur l'ouvert  $U\cap X'$  de  $X'$ .

Corollaire (10.8.6). — Le préschéma (usuel) $\hat{\mathbf{X}}_{\mathrm{red}}$ est l'unique sous-préschéma réduit de X ayant pour espace sous-jacent $\mathbf{X}'$ (5.2.1). Pour que $\hat{\mathbf{X}}$ soit noethérien, il faut et il suffit que $\hat{\mathbf{X}}_{\mathrm{red}}$ le soit, et il suffit que X le soit.

La détermination de $\hat{\mathbf{X}}_{\mathrm{red}}$ étant locale (10.5.4), on peut encore supposer que $\mathbf{X}$ est un schéma affine d'anneau noethérien; avec les notations de (10.8.5), l'idéal $\mathfrak{T}$ des éléments topologiquement nilpotents de $\hat{\mathbf{A}}$ est l'image réciproque par l'application canonique $\hat{\mathbf{A}}\to\hat{\mathbf{A}}/\hat{\mathfrak{J}}=\mathbf{A}/\mathfrak{J}$ du nilradical de A/$\mathfrak{J}$ (0, 7.1.3), donc $\hat{\mathbf{A}}/\mathfrak{T}$ est isomorphe au quotient de A/$\mathfrak{J}$ par son nilradical. La première assertion résulte donc de (10.5.4) et (5.1.1). Si $\hat{\mathbf{X}}_{\mathrm{red}}$ est noethérien, son espace sous-jacent $\mathbf{X}'$ l'est aussi, donc les $\mathbf{X}_{n}^{\prime}=\operatorname{Spec}(\mathcal{O}_{\mathbf{X}}/\mathcal{J}^{n})$ sont noethériens (6.1.2) et il en est de même de $\hat{\mathbf{X}}$ (10.6.4); la réciproque est immédiate, en vertu de (6.1.2).

(10.8.7) Les homomorphismes canoniques $\mathcal{O}_{\mathrm{X}} \to \mathcal{O}_{\mathrm{X}} / \mathcal{J}$ (pour $\mathcal{J} \in \Phi$) forment un système projectif et donnent donc, par passage à la limite projective, un homomorphisme de faisceau d'anneaux $\theta: \mathcal{O}_{\mathrm{X}} \to \psi_{*}((\mathcal{O}_{\mathrm{X}})_{/ \mathrm{X}^{\prime}}) = \varprojlim_{\Phi} (\mathcal{O}_{\mathrm{X}} / \mathcal{J})$, en désignant par $\psi$ l'injection canonique $\mathrm{X}^{\prime} \to \mathrm{X}$ des espaces sous-jacents. Nous désignerons par $i$ (ou $i_{\mathrm{X}}$) le morphisme (dit canonique)

$$
(\psi , \theta): \mathrm{X} _ {/ \mathrm{X} ^ {\prime}} \rightarrow \mathrm{X}
$$

d'espaces annelés.

Par tensorisation, pour tout $\mathcal{O}_{\mathrm{x}}$-Module cohérent $\mathcal{F}$, les homomorphismes canoniques $\mathcal{O}_{\mathrm{x}} \to \mathcal{O}_{\mathrm{x}} / \mathcal{J}$ donnent des homomorphismes $\mathcal{F} \to \mathcal{F} \otimes_{\mathcal{O}_{\mathrm{x}}} (\mathcal{O}_{\mathrm{x}} / \mathcal{J})$ de $\mathcal{O}_{\mathrm{x}}$-Modules qui forment encore un système projectif, et donnent donc, par passage à la limite projective, un homomorphisme canonique fonctoriel $\gamma: \mathcal{F} \to \psi_{*}(\mathcal{F}_{|\mathrm{X}^{\prime}})$ de $\mathcal{O}_{\mathrm{x}}$-Modules.

Proposition (10.8.8). — (i) Le foncteur $\mathcal{F}_{\mathrm{|X^{\prime}}}$ (en $\mathcal{F}$) est exact.

(ii) L'homomorphisme fonctoriel $\gamma^{\sharp}:i^{*}(\mathcal{F})\to \mathcal{F}_{/X'}$ de $(\mathcal{O}_{\mathrm{X}})_{/X'}$-Modules est un isomorphisme.

(i) Il suffit de prouver que si $o \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to o$ est une suite exacte de $\mathcal{O}_X$-Modules cohérents, et U un ouvert affine de X, d'anneau noethérien A, la suite

$$
0 \rightarrow \Gamma (\mathrm{Un} \mathrm{X} ^ {\prime}, \mathscr {F} _ {/ \mathrm{X} ^ {\prime}} ^ {\prime}) \rightarrow \Gamma (\mathrm{Un} \mathrm{X} ^ {\prime}, \mathscr {F} _ {/ \mathrm{X} ^ {\prime}}) \rightarrow \Gamma (\mathrm{Un} \mathrm{X} ^ {\prime}, \mathscr {F} _ {/ \mathrm{X} ^ {\prime}} ^ {\prime \prime}) \rightarrow 0
$$

est exacte. On a alors $\mathcal{F}|\mathrm{U} = \widetilde{\mathbf{M}},\mathcal{F}'|\mathrm{U} = \widetilde{\mathbf{M}}',\mathcal{F}''|\mathrm{U} = \widetilde{\mathbf{M}}'',$ où $\mathbf{M},\mathbf{M}',\mathbf{M}''$ sont trois A-modules de type fini tels que la suite $0\to M'\to M\to M''\to 0$ soit exacte (1.5.1 et 1.3.11); soit $\mathcal{J}\in \Phi$ et soit $\Im$ un idéal de A tel que $\mathcal{J}|\mathrm{U} = \widetilde{\Im}$. On a alors

$$
\Gamma (\mathrm{U} \cap \mathrm{X} ^ {\prime}, \mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{X}}} \mathcal {O} _ {\mathrm{X}} / \mathcal {J} ^ {n}) = \mathrm{M} \otimes_ {\mathrm{A}} (\mathrm{A} / \mathfrak {I} ^ {n})
$$

(1.3.12) ; donc, par définition de la limite projective, on a

$$
\Gamma (\mathrm{U} \cap \mathrm{X} ^ {\prime}, \mathscr {F} _ {/ \mathrm{X} ^ {\prime}}) = \varprojlim_ {n} (\mathrm{M} \otimes_ {\mathrm{A}} (\mathrm{A} / \Im^ {n})) = \hat {\mathrm{M}}
$$

séparé complété de M pour la topologie ℑ-préadique, et de même

$$
\Gamma (\mathrm{U} \cap \mathrm{X} ^ {\prime}, \mathcal {F} _ {/ \mathrm{X} ^ {\prime}} ^ {\prime}) = \hat {\mathrm{M}} ^ {\prime}, \Gamma (\mathrm{U} \cap \mathrm{X} ^ {\prime}, \mathcal {F} _ {/ \mathrm{X} ^ {\prime}} ^ {\prime \prime}) = \hat {\mathrm{M}} ^ {\prime \prime}
$$

notre assertion résulte alors de ce que lorsque A est noethérien, le foncteur $\hat{M}$ en M est exact sur la catégorie des A-modules de type fini (0, 7.3.3).

(ii) La question étant locale, on peut supposer que l'on a une suite exacte $\mathcal{O}_{\mathrm{X}}^{m}\to\mathcal{O}_{\mathrm{X}}^{n}\to\mathcal{F}\to\mathrm{o}\quad(\mathbf{0},5.3.2)$; comme $\gamma^{\sharp}$ est fonctoriel, et que les foncteurs $i^{*}(\mathcal{F})$ et $\mathcal{F}_{/X'}$ sont exacts à droite (d'après (i) et ($\mathbf{0},4.3.\mathrm{i}$)), on a le diagramme commutatif

$$
\begin{array}{c c c} i ^ {*} (\mathcal {O} _ {\mathrm{X}} ^ {m}) & \to i ^ {*} (\mathcal {O} _ {\mathrm{X}} ^ {n}) & \to i ^ {*} (\mathcal {F}) \to 0 \\ \gamma^ {\#} \Bigg \downarrow & \gamma^ {\#} \Bigg \downarrow & \gamma^ {\#} \Bigg \downarrow \\ (\mathcal {O} _ {\mathrm{X}} ^ {m}) _ {/ \mathrm{X} ^ {\prime}} & \to (\mathcal {O} _ {\mathrm{X}} ^ {n}) _ {/ \mathrm{X} ^ {\prime}} & \to \mathcal {F} _ {/ \mathrm{X} ^ {\prime}} \to 0 \end{array}\tag{10.8.8.1}
$$

dont les lignes sont exactes. En outre, les deux foncteurs $i^{*}(\mathcal{F})$ et $\mathcal{F}_{/X'}$ commutent aux sommes directes finies (0, 3.2.6 et 4.3.2) et on est donc ramené à démontrer notre assertion pour $\mathcal{F}=\mathcal{O}_{\mathrm{X}}$. On a alors $i^{*}(\mathcal{O}_{\mathrm{X}})=(\mathcal{O}_{\mathrm{X}})_{/X'}=\mathcal{O}_{\widehat{\mathrm{X}}} \quad(0, 4.3.4)$, et $\gamma^{\sharp}$ est un homomorphisme de $\mathcal{O}_{\widehat{\mathrm{X}}}$-Modules; il suffit donc de vérifier que $\gamma^{\sharp}$ transforme la section unité de $\mathcal{O}_{\widehat{\mathrm{X}}}$ au-dessus d'un ouvert de $\mathrm{X}'$ en elle-même, ce qui est immédiat et montre donc que dans ce cas $\gamma^{\sharp}$ est l'identité.

Corollaire (10.8.9). — Le morphisme d'espaces annelés i : X/$_{X'}$→X est plat.

Cela résulte en effet de (0, 6.7.3) et de (10.8.8, (i)).

Corollaire (10.8.10). — Si F et G sont des  $O_{X}$ -Modules cohérents, il existe des isomorphismes canoniques fonctoriels (en F et G)

(10.8.10.1)

$$
(\mathcal {F} _ {/ \mathrm{X} ^ {\prime}}) \otimes_ {(\mathcal {O} _ {\mathbf {x}}) / \mathrm{X} ^ {\prime}} (\mathcal {G} _ {/ \mathrm{X} ^ {\prime}}) \stackrel {\sim} {\to} (\mathcal {F} \otimes_ {\mathcal {O} _ {\mathbf {X}}} \mathcal {G}) _ {/ \mathrm{X} ^ {\prime}}\tag{10.8.10.2}
$$

$$
\left(\mathcal {H} o m _ {\mathcal {O} _ {\mathrm{X}}} (\mathcal {F}, \mathcal {G})\right) _ {/ \mathrm{X} ^ {\prime}} \xrightarrow {\sim} \mathcal {H} o m _ {(\mathcal {O} _ {\mathrm{x}}) / \mathrm{X} ^ {\prime}} \left(\mathcal {F} _ {/ \mathrm{X} ^ {\prime}}, \mathcal {G} _ {/ \mathrm{X} ^ {\prime}}\right)
$$

Cela résulte de l'identification canonique de $i^{*}(\mathcal{F})$ et de $\mathcal{F}/_{\mathrm{X}^{\prime}}$; l'existence du premier isomorphisme est alors un résultat valable pour tous les morphismes d'espaces annelés (0, 4.3.3.1) et celle du second est un résultat valable pour tous les morphismes plats (0, 6.7.6), donc découle de (10.8.9).

Proposition (10.8.11). — Pour tout $\mathcal{O}_{\mathrm{X}}$-Module cohérent $\mathcal{F}$, le noyau de l'homomorphisme canonique $\Gamma(\mathrm{X}, \mathcal{F}) \to \Gamma(\mathrm{X}', \mathcal{F}_{|\mathrm{X}'})$ déduit de $\mathcal{F} \to \mathcal{F}_{|\mathrm{X}'}$ est formé des sections nulles dans un voisinage de $\mathrm{X}'$.

Il résulte de la définition de $\mathcal{F}_{/X'}$ que l'image canonique d'une telle section est nulle. Réciproquement, si $s\in\Gamma(X,\mathcal{F})$ a une image nulle dans $\Gamma(X',\mathcal{F}_{/X'})$, il suffit de voir que tout $x\in X'$ admet un voisinage dans X dans lequel $s$ est nulle, et on peut donc se ramener au cas où $X=\text{Spec}(A)$ est affine, A noethérien, $X'=V(\mathfrak{J})$, où $\mathfrak{J}$ est un idéal de A, et $\mathcal{F}=\widetilde{M}$, où M est un A-module de type fini. Alors $\Gamma(X',\mathcal{F}_{/X'})$ est le séparé complété $\hat{M}$ de M pour la topologie $\mathfrak{J}$-préadique, et l'homomorphisme $\Gamma(X,\mathcal{F})\to\Gamma(X',\mathcal{F}_{/X'})$ est l'homomorphisme canonique $M\to\hat{M}$. On sait (0, 7.3.7) que le noyau de cet homomorphisme est l'ensemble des $z\in M$ annulés par un élément de $1+\mathfrak{J}$. On a donc $(1+f)s=0$ pour un $f\in\mathfrak{J}$; pour tout $x\in X'$ on en déduit $(1_x+f_x)s_x=0$, et comme $1_x+f_x$ est inversible dans $\mathcal{O}_x$ ($\mathfrak{J}_x\mathcal{O}_x$ étant contenu dans l'idéal maximal de $\mathcal{O}_x$), on a $s_x=0$, ce qui démontre la proposition.

Corollaire (10.8.12). — Le support de $\mathcal{F}_{/X'}$ est égal à $\operatorname{Supp}(\mathcal{F})\cap X'$.

Il est clair que $\mathcal{F}_{/X'}$ est un $(\mathcal{O}_X)_{/X'}$-Module de type fini (10.8.8, (ii)) et (0, 5.2.4),

donc son support est fermé (0, 5.2.2) et évidemment contenu dans $\operatorname{Supp}(\mathcal{F}) \cap \mathrm{X}'$. Pour montrer qu'il est égal à ce dernier ensemble, on est aussitôt ramené à prouver que la relation $\Gamma(\mathrm{X}', \mathcal{F}_{/ \mathrm{X}'}) = 0$ entraîne $\operatorname{Supp}(\mathcal{F}) \cap \mathrm{X}' = \emptyset$; or cela résulte de (10.8.11) et de (1.4.1).

Corollaire (10.8.13). — Soit $u: \mathcal{F} \to \mathcal{G}$ un homomorphisme de $\mathcal{O}_{\mathrm{X}}$-Modules cohérents. Pour que $u_{/X'}: \mathcal{F}_{/X'} \to \mathcal{G}_{/X'}$ soit nul, il faut et il suffit que u soit nul dans un voisinage de $\mathrm{X}'$. En effet, d'après (10.8.8, (ii)), $u_{/X'}$ s'identifie à $i^*(u)$, donc si on considère $u$ comme une section au-dessus de X du faisceau $\mathcal{H} = \mathcal{H}om_{\mathcal{O}_{\mathrm{X}}}(\mathcal{F}, \mathcal{G})$, $u_{/X'}$ est la section de $i^*(\mathcal{H}) = \mathcal{H}_{/X'}$ au-dessus de $\mathrm{X}'$ qui lui correspond canoniquement ((10.8.10.2) et (0, 4.4.6)). Il suffit donc d'appliquer (10.8.11) au $\mathcal{O}_{\mathrm{X}}$-Module cohérent $\mathcal{H}$.

Corollaire (10.8.14). — Soit $u: \mathcal{F} \to \mathcal{G}$ un homomorphisme de $\mathcal{O}_{\mathrm{X}}$-Modules cohérents. Pour que $u_{|\mathrm{X}'}$ soit un monomorphisme (resp. un épimorphisme), il faut et il suffit que u soit un monomorphisme (resp. un épimorphisme) dans un voisinage de $\mathrm{X}'$.

Soient $\mathcal{P}$ et $\mathcal{N}$ le conoyau et le noyau de $u$, de sorte qu'on a la suite exacte $0 \to \mathcal{N} \xrightarrow{v} \mathcal{F} \xrightarrow{u} \mathcal{G} \xrightarrow{w} \mathcal{P} \to 0$, d'où (10.8.8, (i)) la suite exacte

$$
0 \rightarrow \mathcal {N} _ {| X ^ {\prime}} \stackrel {{v _ {| X ^ {\prime}}}} {{\longrightarrow}} \mathcal {F} _ {| X ^ {\prime}} \stackrel {{u _ {| X ^ {\prime}}}} {{\longrightarrow}} \mathcal {G} _ {| X ^ {\prime}} \stackrel {{w _ {| X ^ {\prime}}}} {{\longrightarrow}} \mathcal {P} _ {| X ^ {\prime}} \rightarrow 0.
$$

Si $u_{/X'}$ est un monomorphisme (resp. un épimorphisme), on a $v_{/X'} = 0$ (resp. $w_{/X'} = 0$), donc il y a un voisinage de $X'$ dans lequel $v = 0$ (resp. $w = 0$) en vertu de (10.8.13).

## 10.9. Prolongement d'un morphisme aux complétés.

(10.9.1) Soient X, Y deux préschémas (usuels) localement noethériens, $f: \mathbf{X} \to \mathbf{Y}$ un morphisme, $\mathbf{X}'$ (resp. $\mathbf{Y}'$) une partie fermée de l'espace sous-jacent X (resp. Y), telles que $f(\mathbf{X}') \subset \mathbf{Y}'$. Soit $\mathcal{J}$ (resp. $\mathcal{K}$) un faisceau d'idéaux de $\mathcal{O}_{\mathbf{X}}$ (resp. $\mathcal{O}_{\mathbf{Y}}$) tel que le support de $\mathcal{O}_{\mathbf{X}} / \mathcal{J}$ (resp. $\mathcal{O}_{\mathbf{Y}} / \mathcal{K}$) soit $\mathbf{X}'$ (resp. $\mathbf{Y}'$) et que $f^*(\mathcal{K})\mathcal{O}_{\mathbf{X}} \subset \mathcal{J}$; on notera qu'il existe toujours de tels faisceaux d'idéaux, car on peut par exemple prendre pour $\mathcal{J}$ le plus grand faisceau d'idéaux de $\mathcal{O}_{\mathbf{X}}$ définissant un sous-préschéma de X ayant $\mathbf{X}'$ pour espace sous-jacent (5.2.1), et l'hypothèse $f(\mathbf{X}') \subset \mathbf{Y}'$ entraîne alors $f^*(\mathcal{K})\mathcal{O}_{\mathbf{X}} \subset \mathcal{J}$ (5.2.4). On a donc pour tout entier $n > 0$, $f^*(\mathcal{K}^n)\mathcal{O}_{\mathbf{X}} \subset \mathcal{J}^n$ (0, 4.3.5); par suite (4.4.6), si on pose $\mathbf{X}_n' = (\mathbf{X}', \mathcal{O}_{\mathbf{X}} / \mathcal{J}^{n+1})$, $\mathbf{Y}_n' = (\mathbf{Y}', \mathcal{O}_{\mathbf{Y}} / \mathcal{K}^{n+1})$, on déduit de $f$ un morphisme $f_n: \mathbf{X}_n' \to \mathbf{Y}_n'$, et il est immédiat que les $f_n$ forment un système inductif. Nous désignerons sa limite inductive (10.6.8) par $\hat{f}: \mathbf{X}_{/X'} \to \mathbf{Y}_{/Y'}$, et nous dirons (par abus de langage) que $\hat{f}$ est le prolongement de $f$ aux complétés de X et Y le long de $\mathbf{X}'$ et $\mathbf{Y}'$. Il est immédiat de vérifier que ce morphisme ne dépend pas du choix des faisceaux d'idéaux $\mathcal{J}$, $\mathcal{K}$ vérifiant les conditions ci-dessus. Il suffit de le voir en effet lorsque X et Y sont des schémas affines noethériens d'anneaux A, B; alors $\mathcal{J} = \widetilde{\mathfrak{I}}, \mathcal{K} = \widetilde{\mathfrak{R}}$, où $\mathfrak{I}$ (resp. $\mathfrak{R}$) est un idéal de A (resp. B), $f$ correspond à un homomorphisme d'anneaux $\varphi: \mathrm{B} \to \mathrm{A}$ tel que $\varphi(\mathfrak{R}) \subset \mathfrak{I}$ (4.4.6 et 1.7.4); $\hat{f}$ est alors le morphisme qui correspond (10.2.2) à l'homomorphisme continu $\hat{\varphi}: \hat{\mathrm{B}} \to \hat{\mathrm{A}}$, où $\hat{\mathrm{A}}$ (resp. $\hat{\mathrm{B}}$) est le séparé complété de A (resp. B) pour la topologie $\mathfrak{I}$-préadique (resp. $\mathfrak{R}$-préadique) (10.6.8); et on sait que si on remplace $\mathcal{J}$ par un autre

faisceau d'idéaux $\mathcal{J}^{\prime} = \widetilde{\mathfrak{J}}^{\prime}$ tel que le support de $\mathcal{O}_{\mathrm{X}} / \mathcal{J}^{\prime}$ soit encore $\mathbf{X}^{\prime}$, les topologies $\mathfrak{J}$-préadique et $\mathfrak{J}^{\prime}$-préadique sur A sont les mêmes (10.8.2).

On notera que, d'après cette définition, l'application continue  $X'\to Y'$  des espaces sous-jacents à  $X_{/X'}$  et  $Y_{/Y'}$, qui correspond à  $\hat{f}$, n'est autre que la restriction à  $X'$  de f.

(10.9.2) Il résulte aussitôt de la définition précédente que le diagramme de morphismes d'espaces annelés

![](images/page_17_image_2.jpg)

est commutatif, les flèches verticales étant les morphismes canoniques (10.8.7).

(10.9.3) Soient Z un troisième préschéma, $g: \mathrm{Y} \to \mathrm{Z}$ un morphisme, $\mathrm{Z}'$ une partie fermée de Z telle que $g(\mathrm{Y}') \subset \mathrm{Z}'$. Si $\hat{g}$ désigne le complété le long de $\mathrm{Y}'$ et $\mathrm{Z}'$ du morphisme $g$, il résulte aussitôt de (10.9.1) que l'on a $(g \circ f)^{\wedge} = \hat{g} \circ \hat{f}$.

Proposition (10.9.4). — Soient X, Y deux S-préschémas localement noethériens, Y étant de type fini sur S. Soient f, g, deux S-morphismes de X dans Y tels que  $f(\mathbf{X}') \subset \mathbf{Y}'$ ,  $g(\mathbf{X}') \subset \mathbf{Y}'$ . Pour que  $\hat{f} = \hat{g}$ , il faut et il suffit que f et g coïncident dans un voisinage de  $X'$ .

La condition est évidemment suffisante (sans hypothèse de finitude sur Y). Pour voir qu'elle est nécessaire, remarquons d'abord que l'hypothèse $\hat{f} = \hat{g}$ implique $f(x) = g(x)$ pour tout $x \in \mathbf{X}'$. D'autre part, la question étant locale, on peut supposer que X et Y sont des voisinages ouverts affines respectifs de $x$ et de $y = f(x) = g(x)$, d'anneaux noethériens, que S est affine et que $\Gamma(\mathrm{Y}, \mathcal{O}_{\mathrm{Y}})$ est une $\Gamma(\mathrm{S}, \mathcal{O}_{\mathrm{S}})$-algèbre de type fini (6.3.3). Alors $f$ et $g$ correspondent à deux $\Gamma(\mathrm{S}, \mathcal{O}_{\mathrm{S}})$-homomorphismes $\rho, \sigma$ de $\Gamma(\mathrm{Y}, \mathcal{O}_{\mathrm{Y}})$ dans $\Gamma(\mathrm{X}, \mathcal{O}_{\mathrm{X}})$ (1.7.3), et par hypothèse, les prolongements par continuité de ces homomorphismes au séparé complété de $\Gamma(\mathrm{Y}, \mathcal{O}_{\mathrm{Y}})$ sont les mêmes. On conclut de (10.8.11) que pour toute section $s \in \Gamma(\mathrm{Y}, \mathcal{O}_{\mathrm{Y}})$, les sections $\rho(s)$ et $\sigma(s)$ coïncident dans un voisinage de $\mathbf{X}'$ (dépendant de $s$); comme $\Gamma(\mathrm{Y}, \mathcal{O}_{\mathrm{Y}})$ est une algèbre de type fini sur $\Gamma(\mathrm{S}, \mathcal{O}_{\mathrm{S}})$, on en déduit aussitôt qu'il existe un voisinage V de $\mathbf{X}'$ tel que $\rho(s)$ et $\sigma(s)$ coïncident dans V pour toute section $s \in \Gamma(\mathrm{Y}, \mathcal{O}_{\mathrm{Y}})$. Si $h \in \Gamma(\mathrm{Y}, \mathcal{O}_{\mathrm{X}})$ est tel que D(h) soit un voisinage de $x$ contenu dans V, on conclut de ce qui précède et de (1.4.1, d)) que $f$ et $g$ coïncident dans D(h).

Proposition (10.9.5). — Sous les hypothèses de (10.9.1), pour tout $\mathcal{O}_{\mathrm{Y}}$-Module cohérent $\mathcal{G}$, il existe un isomorphisme canonique fonctoriel de $(\mathcal{O}_{\mathrm{X}})_{/ \mathrm{X}'}$-Modules

$$
\left(f ^ {*} (\mathcal {G})\right) _ {\mid \mathrm{X} ^ {\prime}} \xrightarrow {\sim} \hat {f} ^ {*} \left(\mathcal {G} _ {\mid \mathrm{Y} ^ {\prime}}\right)
$$

Si on identifie canoniquement $(f^{*}(\mathcal{G}))_{/X'}$ à $i_X^*(f^*(\mathcal{G}))$ et $\hat{f}^*(\mathcal{G}_{/Y'})$ à $\hat{f}^*(i_Y^*(\mathcal{G}))$ (10.8.8), la proposition résulte aussitôt de la commutativité du diagramme de (10.9.2).

(10.9.6) Soient maintenant $\mathcal{F}$ un $\mathcal{O}_{\mathrm{X}}$-Module cohérent, $\mathcal{G}$ un $\mathcal{O}_{\mathrm{Y}}$-Module cohérent. Si $u: \mathcal{G} \to \mathcal{F}$ est un $f$-morphisme de $\mathcal{G}$ dans $\mathcal{F}$, il lui correspond un $\mathcal{O}_{\mathrm{X}}$-homomorphisme $u^{\sharp}: f^{*}(\mathcal{G}) \to \mathcal{F}$, donc par complétion un $(\mathcal{O}_{\mathrm{X}})_{/ \mathrm{X}'}$-homomorphisme continu $(u^{\sharp})_{/ \mathrm{X}'}: (f^{*}(\mathcal{G}))_{/ \mathrm{X}'} \to \mathcal{F}_{/ \mathrm{X}'}$, et en vertu de (10.9.5) il existe un $\hat{f}$-morphisme $v: \mathcal{G}_{/ \mathrm{Y}'} \to \mathcal{F}_{/ \mathrm{X}'}$,

et un seul, tel que $v^{\sharp} = (u^{\sharp})_{/X'}$. Si on considère les triplets $(\mathcal{F}, X, X')$ ($\mathcal{F}$ étant un $\mathcal{O}_X$-Module cohérent et $X'$ une partie fermée de $X$) comme une catégorie, les morphismes $(\mathcal{F}, X, X') \to (\mathcal{G}, Y, Y')$ consistant en un morphisme de préschémas $f: X \to Y$ tel que $f(X') \subset Y'$ et en un $f$-morphisme $u: \mathcal{G} \to \mathcal{F}$, on peut donc dire que $(X_{/X'}, \mathcal{F}_{/X'})$ est un foncteur en $(\mathcal{F}, X, X')$, prenant ses valeurs dans la catégorie des couples $(3, \mathcal{H})$ formés d'un préschéma formel localement noethérien 3 et d'un $\mathcal{O}_3$-Module $\mathcal{H}$, les morphismes de cette dernière catégorie consistant en les couples formés d'un morphisme $g$ de préschémas formels et d'un $g$-morphisme.

Proposition (10.9.7). — Soient S, X, Y trois préschémas localement noethériens, $g: \mathbf{X} \to \mathbf{S}$, $h: \mathbf{Y} \to \mathbf{S}$ deux morphismes, $\mathbf{S}'$ une partie fermée de S, $\mathbf{X}'$ (resp. $\mathbf{Y}'$) une partie fermée de X (resp. Y) telle que $g(\mathbf{X}') \subset \mathbf{S}'$ (resp. $h(\mathbf{Y}') \subset \mathbf{S}'$); soit $\mathbf{Z} = \mathbf{X} \times_{\mathbb{S}} \mathbf{Y}$; supposons Z localement noethérien, et soit $\mathbf{Z}' = p^{-1}(\mathbf{X}') \cap q^{-1}(\mathbf{Y}')$, où $p$ et $q$ sont les projections de $\mathbf{X} \times_{\mathbb{S}} \mathbf{Y}$. Dans ces conditions, le complété $\mathbf{Z}_{/Z'} s'$ identifie au produit des $\mathbf{S}_{/S'}$-préschémas formels $(\mathbf{X}_{/X'}) \times_{\mathbb{S}_{/S'}} (\mathbf{Y}_{/Y'})$ les morphismes structuraux s'identifiant à $\hat{g}$ et $\hat{h}$, et les projections à $\hat{p}$ et $\hat{q}$.

Il est immédiat que la question est locale pour S, X et Y, et on est donc ramené au cas où  $\mathrm{S}=\mathrm{Spec}(\mathrm{A})$ ,  $\mathrm{X}=\mathrm{Spec}(\mathrm{B})$ ,  $\mathrm{Y}=\mathrm{Spec}(\mathrm{C})$ ,  $\mathrm{S}'=\mathrm{V}(\mathfrak{J})$ ,  $\mathrm{X}'=\mathrm{V}(\mathfrak{K})$ ,  $\mathrm{Y}'=\mathrm{V}(\mathfrak{L})$ , où J, R, L sont trois idéaux tels que  $\varphi(\mathfrak{J})\subset\mathfrak{K}$  et  $\psi(\mathfrak{J})\subset\mathfrak{L}$ , en désignant par  $\varphi$  et  $\psi$  les homomorphismes A→B et A→C qui correspondent à g et h. Alors on sait que  $\mathrm{Z}=\mathrm{Spec}(\mathrm{B}\otimes_{\mathrm{A}}\mathrm{C})$  et que  $\mathrm{Z}'=\mathrm{V}(\mathfrak{M})$ , où M est l'idéal  $\operatorname{Im}(\mathfrak{R}\otimes_{\mathrm{A}}\mathrm{C})+\operatorname{Im}(\mathrm{B}\otimes_{\mathrm{A}}\mathfrak{L})$ . La conclusion résulte (10.7.2) de ce que le produit tensoriel complété  $(\hat{\mathbf{B}}\otimes_{\hat{\mathbf{A}}} \hat{\mathbf{C}})^{\wedge}$  (où  $\hat{\mathbf{A}}$ ,  $\hat{\mathbf{B}}$ ,  $\hat{\mathbf{C}}$  sont respectivement les séparés complétés de A, B, C pour les topologies J-, R- et L-préadiques) est le séparé complété du produit tensoriel  $B\otimes_{A}C$  pour la topologie M-préadique (0, 7.7.2).

On notera en outre que si T est un S-préschéma localement noethérien, $u: \mathrm{T} \to \mathrm{X}$, $v: \mathrm{T} \to \mathrm{Y}$ deux S-morphismes, $\mathrm{T}'$ une partie fermée de T telle que $u(\mathrm{T}') \subset \mathrm{X}', v(\mathrm{T}') \subset \mathrm{Y}'$, alors le prolongement aux complétés $((u, v)_{\mathrm{s}})^{\wedge}$ s'identifie à $(\hat{u}, \hat{v})_{\mathrm{S}/\mathrm{s}'}$.

Corollaire (10.9.8). — Soient X, Y deux S-préschémas localement noethériens tels que  $X \times_{s} Y$  soit localement noethérien; soient  $S'$  une partie fermée de S,  $X'$  (resp.  $Y'$ ) une partie fermée de X (resp. Y) dont l'image dans S est contenue dans  $S'$ . Pour tout S-morphisme  $f: X \to Y$  tel que  $f(X') \subset Y'$ , le morphisme graphe  $\Gamma_{\hat{f}}$  s'identifie au prolongement  $(\Gamma_{\hat{f}})^{\wedge}$  du morphisme graphe de f.

Corollaire (10.9.9). — Soient X, Y deux préschémas localement noethériens,  $f: X \to Y$  un morphisme,  $Y'$  une partie fermée de Y,  $X' = f^{-1}(Y')$ . Alors le préschéma  $X_{|X'}$  s'identifie par le diagramme commutatif

![](images/page_18_image_5.jpg)

au produit $\mathbf{X} \times_{\mathrm{Y}} (\mathbf{Y}_{/ \mathrm{Y}^{\prime}})$ de préschémas formels.

Il suffit d'appliquer (10.9.7) en remplaçant S et S' par Y, X et X' par X.

201

Remarque (10.9.10). — Si X est la somme  $X_{1}$  II  $X_{2}$  (3.1),  $X'$  la réunion  $X_{1}' \cup X_{2}'$ , où  $X_{i}'$  est une partie fermée de  $X_{i}$  (i=1,2), on voit aussitôt que l'on a  $X_{/X'} = X_{1/X_{1}}$  II  $X_{2/X_{2}}$ .

## 10.10. Application aux faisceaux cohérents sur les schémas formels affines.

(10.10.1) Dans tout ce paragraphe, A désignera un anneau adique noethérien, $\mathfrak{J}$ un idéal de définition de A. Soit $\mathrm{X} = \operatorname{Spec}(\mathrm{A})$, $\mathfrak{X} = \operatorname{Spf}(\mathrm{A})$, qui s'identifie à la partie fermée $\mathrm{V}(\mathfrak{J})$ de $\mathrm{X}$ (10.1.2). En outre, la définition (10.1.2) et la définition (10.8.4) montrent que le schéma formel affine $\mathfrak{X}$ est identique au complété $\mathrm{X}_{/x}$ du schéma affine $\mathrm{X}$ le long de la partie fermée $\mathfrak{X}$ de son espace sous-jacent. A tout $\mathcal{O}_{\mathrm{X}}$-Module cohérent $\mathcal{F}$ correspond donc un $\mathcal{O}_{x}$-Module de type fini $\mathcal{F}_{/x}$, qui est d'ailleurs un faisceau de modules topologiques sur le faisceau d'anneaux topologiques $\mathcal{O}_{x}$. Mais tout $\mathcal{O}_{\mathrm{X}}$-Module cohérent $\mathcal{F}$ est de la forme $\widetilde{\mathbf{M}}$, où $\mathbf{M}$ est un A-module de type fini (1.5.1); nous poserons $(\widetilde{\mathbf{M}})_{/X} = \mathbf{M}^{\Delta}$. En outre, si $u: \mathbf{M} \to \mathbf{N}$ est un A-homomorphisme de A-modules de type fini, il lui correspond un homomorphisme $\widetilde{u}: \widetilde{\mathbf{M}} \to \widetilde{\mathbf{N}}$, et par suite aussi un homomorphisme continu $\widetilde{u}_{/X'}: (\widetilde{\mathbf{M}})_{/X'} \to (\widetilde{\mathbf{N}})_{/X'}$, que nous noterons $u^{\Delta}$. Il est immédiat que $(vou)^{\Delta} = v^{\Delta} \circ u^{\Delta}$; on a ainsi défini un foncteur additif covariant $\mathbf{M}^{\Delta}$ de la catégorie des A-modules de type fini dans celle des $\mathcal{O}_{x}$-Modules de type fini. Lorsque A est un anneau discret, on a $\mathbf{M}^{\Delta} = \widetilde{\mathbf{M}}$. Proposition (10.10.2). — (i) $\mathbf{M}^{\Delta}$ est un foncteur exact en $\mathbf{M}$, et il existe un isomorphisme canonique fonctoriel de A-modules $\Gamma(\mathfrak{X}, \mathbf{M}^{\Delta}) \cong \mathbf{M}$.

(ii) Si M et N sont deux A-modules de type fini, il existe des isomorphismes canoniques fonctoriels

(10.10.2.1)

$$
(\mathbf {M} \otimes_ {\mathrm{A}} \mathbf {N}) ^ {\Delta} \xrightarrow {\sim} \mathbf {M} ^ {\Delta} \otimes_ {\mathcal {O} _ {\mathfrak {X}}} \mathbf {N} ^ {\Delta}\tag{10.10.2.2}
$$

$$
(\operatorname{Hom} _ {\mathrm{A}} (\mathbf {M}, \mathbf {N})) ^ {\Delta} \stackrel {{\sim}} {{\to}} \mathcal {H} o m _ {\mathcal {O} _ {\mathfrak {X}}} (\mathbf {M} ^ {\Delta}, \mathbf {N} ^ {\Delta})
$$

(iii) $L^{\prime}$ application $\pmb {u}\rightarrow \pmb{u}^{\Delta}$ est un isomorphisme fonctoriel

$$
\operatorname{Hom} _ {\mathrm{A}} (\mathbf {M}, \mathrm{N}) \xrightarrow {\sim} \operatorname{Hom} _ {\mathcal {O} _ {\mathrm{X}}} (\mathbf {M} ^ {\Delta}, \mathrm{N} ^ {\Delta})\tag{10.10.2.3}
$$

L'exactitude de $\mathbf{M}^{\Delta}$ résulte de l'exactitude des foncteurs $\widetilde{\mathbf{M}}$ (1.3.5) et $\mathcal{F}_{/X'}$ (10.8.8). Par définition, $\Gamma(\mathbf{X},\mathbf{M}^{\Delta})$ est le séparé complété du A-module $\Gamma(\mathbf{X},\widetilde{\mathbf{M}})=\mathbf{M}$ pour la topologie $\mathfrak{J}$-préadique; mais comme A est complet et M de type fini, on sait (0, 7.3.6) que M est séparé et complet, ce qui achève de prouver (i). L'isomorphisme (10.10.2.1) (resp. (10.10.2.2)) provient de la composition des isomorphismes (1.3.12, (i)) et (10.8.10.1) (resp. (1.3.12, (ii)) et (10.8.10.2)). Enfin, comme $\mathrm{Hom}_{\mathrm{A}}(\mathbf{M},\mathbf{N})$ est un A-module de type fini, on peut lui appliquer (i), qui identifie $\Gamma(\mathfrak{X},(\mathrm{Hom}_{\mathrm{A}}(\mathbf{M},\mathbf{N}))^{\Delta})$ à $\mathrm{Hom}_{\mathrm{A}}(\mathbf{M},\mathbf{N})$, et utiliser (10.10.2.2), qui prouve que l'homomorphisme (10.10.2.3) est un isomorphisme.

On déduit de (10.10.2) toute une série de conséquences analogues à celles déduites de (1.3.7) et (1.3.12), que nous laissons au lecteur le soin de formuler.

Notons que la propriété d'exactitude de  $M^{\Delta}$ , appliqué à la suite exacte  $o\to J\to A\to A/J\to o$  montre que le faisceau d'idéaux de  $O_{x}$  désigné ici par  $J^{\Delta}$  coïncide avec celui qui avait été noté de la même façon en (10.3.1), en vertu de (10.3.2).

Proposition (10.10.3). — Sous les hypothèses de (10.10.1), $\mathcal{O}_{\mathfrak{X}}$ est un faisceau cohérent d'anneaux.

Si $f \in \mathbf{A}$, on sait que $\mathrm{A}_{\{f\}}$ est un anneau adique noethérien (0, 7.6.11) et comme la question est locale, on est ramené (10.1.4) à prouver que le noyau d'un homomorphisme $v: \mathcal{O}_{\mathfrak{x}}^{n} \to \mathcal{O}_{\mathfrak{x}}$ est un $\mathcal{O}_{\mathfrak{x}}$-Module de type fini. On a alors $v = u^{\Delta}$, où $u$ est un A-homomorphisme $\mathrm{A}^{n} \to \mathrm{A}$ (10.10.2); comme A est noethérien, le noyau de $u$ est de type fini, autrement dit on a un homomorphisme $\mathrm{A}^{m} \xrightarrow{w} \mathrm{A}^{n}$ tel que la suite $\mathrm{A}^{m} \xrightarrow{w} \mathrm{A}^{n} \xrightarrow{u} \mathrm{A}$ soit exacte. On en conclut (10.10.2) que la suite $\mathcal{O}_{\mathfrak{x}}^{m} \xrightarrow{w^{\Delta}} \mathcal{O}_{\mathfrak{x}}^{n} \xrightarrow{v} \mathcal{O}_{\mathfrak{x}}$ est exacte, ce qui prouve que le noyau de $v$ est de type fini.

(10.10.4) Avec les notations précédentes, posons  $A_{n}=A/J^{n+1}$ , et soit  $X_{n}$  le schéma affine  $\operatorname{Spec}(A_{n})=(\mathfrak{X},\mathcal{O}_{\mathfrak{X}}/\mathcal{J}^{n+1})$ ,  $J=J^{\Delta}$  étant le faisceau d'idéaux de définition de  $O_{X}$  correspondant à l'idéal J. Soit  $u_{mn}$  le morphisme de préschémas  $X_{m}\to X_{n}$  correspondant à l'homomorphisme canonique  $A_{n}\to A_{m}$  pour  $m\leqslant n$ ; le schéma formel X est limite inductive des  $X_{n}$  pour les  $u_{mn}$  (10.6.3).

Proposition (10.10.5). — Sous les hypothèses de (10.10.1), soit $\mathcal{F}$ un $\mathcal{O}_{\mathfrak{X}}$-Module. Les conditions suivantes sont équivalentes :

a) $\mathcal{F}$ est un $\mathcal{O}_{\mathfrak{X}}$-Module cohérent.

b) $\mathcal{F}$ est isomorphe à la limite projective (10.6.6) d'une suite $(\mathcal{F}_n)$ de $\mathcal{O}_{\mathrm{X}_n}$-Modules cohérents tels que $u_{nm}^{*}(\mathcal{F}_{n}) = \mathcal{F}_{m}$.

c) Il existe un A-module de type fini M (déterminé à un isomorphisme canonique près par (10.10.2, (i))) tel que $\mathcal{F}$ soit isomorphe à $\mathbf{M}^{\Delta}$.

Montrons d'abord que $b)$ implique $c)$. On a $\mathcal{F}_{n}=\widetilde{\mathbf{M}}_{n}$, où $\mathbf{M}_{n}$ est un $\mathbf{A}_{n}$-module de type fini, et l'hypothèse entraîne que $\mathbf{M}_{m}=\mathbf{M}_{n}\otimes_{\mathbb{A}_{n}}\mathbf{A}_{m}$ pour $m\leqslant n$ (1.6.5); les $\mathbf{M}_{n}$ forment donc un système projectif pour les di-homomorphismes canoniques $\mathbf{M}_{n}\to\mathbf{M}_{m}$ ($m\leqslant n$), et il résulte aussitôt de la définition des $\mathbf{A}_{n}$ que ce système projectif vérifie les conditions de (0, 7.2.9); sa limite projective M est par suite un A-module de type fini tel que $\mathbf{M}_{n}=\mathbf{M}\otimes_{\mathbb{A}}\mathbf{A}_{n}$ pour tout $n$. On en déduit que $\mathcal{F}_{n}$ est induit sur $\mathbf{X}_{n}$ par $\widetilde{\mathbf{M}}\otimes_{\mathcal{O}_{\mathbf{X}}}\left(\mathcal{O}_{\mathbf{X}}/\widetilde{\mathfrak{J}}^{n+1}\right)$, donc $\mathcal{F}=\mathbf{M}^{\Delta}$ par définition (10.8.4).

Inversement, c) entraîne b); en effet, si $u_n$ est le morphisme d'immersion $\mathbf{X}_n \to \mathbf{X}$, $u_n^*(\widetilde{\mathbf{M}}) = (\mathbf{M} \otimes_{\mathbf{A}} \mathbf{A}_n)^\sim$ est induit sur $\mathbf{X}_n$ par $\widetilde{\mathbf{M}} \otimes_{\mathcal{O}_\mathbf{X}} (\mathcal{O}_{\mathbf{X}} / \widetilde{\mathfrak{J}}^{n+1})$, et $\mathbf{M}^\Delta = \varprojlim u_n^*(\widetilde{\mathbf{M}})$ par définition (10.8.4); comme $u_m = u_n \circ u_{mn}$ pour $m \leqslant n$, les $\mathcal{F}_n = u_n^*(\widetilde{\mathbf{M}})$ vérifient les conditions de $b$), d'où notre assertion.

Montrons maintenant que $c)$ implique $a)$: en effet, on a par définition $\mathcal{O}_{\mathfrak{x}} = \mathrm{A}^{\Delta}$; $\mathbf{M}$ étant conoyau d'un homomorphisme $\mathrm{A}^{m} \to \mathrm{A}^{n}$, il résulte de (10.10.2) que $\mathbf{M}^{\Delta}$ est conoyau d'un homomorphisme $\mathcal{O}_{\mathfrak{x}}^{m} \to \mathcal{O}_{\mathfrak{x}}^{n}$, et comme le faisceau d'anneaux $\mathcal{O}_{\mathfrak{x}}$ est cohérent (10.10.3), il en est de même de $\mathbf{M}^{\Delta}$ (0, 5.3.4).

Enfin, a) entraîne b). Considéré comme $\mathcal{O}_{\mathfrak{x}}$-Module, on a $\mathcal{O}_{\mathrm{X}_n} = \mathcal{O}_{\mathfrak{x}} / \mathcal{J}^{n+1} = \mathrm{A}_n^\Delta$; $\mathcal{F}_n = \mathcal{F} \otimes_{\mathcal{O}_{\mathfrak{x}}} \mathcal{O}_{\mathrm{X}_n}$ est un $\mathcal{O}_{\mathfrak{x}}$-Module cohérent (0, 5.3.5), et comme c'est aussi un $\mathcal{O}_{\mathrm{X}_n}$-Module et que $\mathcal{J}^{n+1}$ est cohérent, on en conclut que $\mathcal{F}_n$ est un $\mathcal{O}_{\mathrm{X}_n}$-Module cohérent (0, 5.3.10), et il est immédiat que $u_{mn}^*(\mathcal{F}_n) = \mathcal{F}_m$ pour $m \leqslant n$ (en se souvenant que l'application continue $\mathrm{X}_m \to \mathrm{X}_n$ des espaces sous-jacents est l'identité de $\mathfrak{X}$). Le faisceau $\mathcal{G} = \varprojlim \mathcal{F}_n$ est donc un $\mathcal{O}_{\mathfrak{x}}$-Module cohérent, puisqu'on a vu que b) entraîne a). Les homomorphismes canoniques $\mathcal{F} \to \mathcal{F}_n$ forment un système projectif, qui par passage à la limite donne un homomorphisme canonique $w: \mathcal{F} \to \mathcal{G}$, et tout revient à démontrer que $w$ est bijectif. La question étant maintenant locale, on peut se borner au cas où $\mathcal{F}$ est conoyau d'un homomorphisme $\mathcal{O}_{\mathfrak{x}}^p \to \mathcal{O}_{\mathfrak{x}}^q$; cet homomorphisme étant de la forme $v^\Delta$, où $v$ est un homomorphisme $\mathrm{A}^m \to \mathrm{A}^n$ (10.10.2), $\mathcal{F}$ est isomorphe à $\mathrm{M}^\Delta$, où $\mathrm{M} = \mathrm{Coker} v$ (10.10.2). On a alors, en vertu de (10.10.2), $\mathcal{F}_n = \mathrm{M}^\Delta \otimes_{\mathcal{O}_{\mathfrak{x}}} \mathrm{A}_n^\Delta = (\mathrm{M} \otimes_{\mathrm{A}} \mathrm{A}_n)^\Delta$, et comme la topologie \$\mathfrak{J}\$-adique sur $\mathrm{M} \otimes_{\mathrm{A}} \mathrm{A}_n$ est discrète, on a $(\mathrm{M} \otimes_{\mathrm{A}} \mathrm{A}_n)^\Delta = (\mathrm{M} \otimes_n \mathrm{A}_n)^\sim$ (en tant que $\mathcal{O}_{\mathrm{X}_n}$-Module); on a vu plus haut que $\mathrm{M}^\Delta = \varprojlim \mathcal{F}_n$ et $w$ est donc bien dans ce cas l'identité. C.Q.F.D.

Corollaire (10.10.6). — Si $\mathcal{F}$ vérifie la condition b) de (10.10.5), le système projectif $(\mathcal{F}_n)$ est isomorphe au système des $\mathcal{F} \otimes_{\mathcal{O}_{\mathfrak{X}}} \mathcal{O}_{\mathrm{X}_n}$.

(10.10.7) Soient maintenant A, B deux anneaux adiques noethériens, $\varphi: B \to A$ un homomorphisme continu ; on désignera par $\mathfrak{J}$ (resp. $\mathfrak{R}$) un idéal de définition de A (resp. B), tels que $\varphi(\mathfrak{R}) \subset \mathfrak{J}$, et on posera $X = \text{Spec}(A)$, $Y = \text{Spec}(B)$, $\mathfrak{X} = \text{Spf}(A)$, $\mathfrak{Y} = \text{Spf}(B)$. Soient $f: X \to Y$ le morphisme de préschémas correspondant à $\varphi$ (1.6.1), $\hat{f}: \mathfrak{X} \to \mathfrak{Y}$ son prolongement aux complétés (10.9.1), qui est aussi le morphisme de préschémas formels correspondant à $\varphi$ (10.2.2).

Proposition (10.10.8). — Pour tout B-module N de type fini, il existe un isomorphisme canonique fonctoriel de $\mathcal{O}_{\mathfrak{x}}$-Modules

$$
\hat {f} ^ {*} (\mathbf {N} ^ {\Delta}) \xrightarrow {\sim} (\mathbf {N} \otimes_ {\mathrm{B}} \mathbf {A}) ^ {\Delta}
$$

En effet, en désignant par $i_{\mathrm{X}}:\mathfrak{X}\to\mathrm{X}$ et $i_{\mathrm{Y}}:\mathfrak{Y}\to\mathrm{Y}$ les morphismes canoniques, on a (10.8.8), à des isomorphismes canoniques fonctoriels près, $\mathrm{N}^{\Delta}=i_{\mathrm{Y}}^{*}(\widetilde{\mathrm{N}})$ et

$$
(\mathbf {N} \otimes_ {\mathrm{B}} \mathbf {A}) ^ {\Delta} = i _ {\mathrm{X}} ^ {*} ((\mathbf {N} \otimes_ {\mathrm{B}} \mathbf {A}) \sim) = i _ {\mathrm{X}} ^ {*} (f ^ {*} (\widetilde {\mathbf {N}}))
$$

(1.6.5); la proposition résulte donc de la commutativité du diagramme (10.9.2). Corollaire (10.10.9). — Pour tout idéal b de B, on a $\hat{f}^{*}(\mathfrak{b}^{\Delta})\mathcal{O}_{\mathfrak{x}}=(\mathfrak{b}\mathbf{A})^{\Delta}$.

En effet, soit $j$ l'injection canonique $\mathfrak{b}\to\mathbf{B}$, à laquelle il correspond l'injection canonique $j^{\Delta}:\mathfrak{b}^{\Delta}\to\mathcal{O}_{\mathfrak{Y}}$ de faisceaux de $\mathcal{O}_{\mathfrak{Y}}$-Modules ; par définition, $\hat{f}^{*}(\mathfrak{b}^{\Delta})\mathcal{O}_{\mathfrak{x}}$ est l'image de l'homomorphisme $\hat{f}^{*}(j^{\Delta}): \hat{f}^{*}(\mathfrak{b}^{\Delta})\to\mathcal{O}_{\mathfrak{x}}=\hat{f}^{*}(\mathcal{O}_{\mathfrak{Y}})$ ; mais cet homomorphisme s'identifie à $(j\otimes\mathrm{i})^{\Delta}:(\mathfrak{b}\otimes_{\mathrm{B}}\mathrm{A})^{\Delta}\to\mathcal{O}_{\mathfrak{x}}=(\mathrm{B}\otimes_{\mathrm{B}}\mathrm{A})^{\Delta}$ d'après (10.10.8). Comme l'image de $j\otimes\mathrm{i}$ est l'idéal $\mathfrak{b}\mathrm{A}$ de A, l'image de $(j\otimes\mathrm{i})^{\Delta}$ est donc $(\mathfrak{b}\mathrm{A})^{\Delta}$ en vertu de (10.10.2), d'où la conclusion.

## 10.11. Faisceaux cohérents sur les préschémas formels.

Proposition (10.11.1). — Si X est un préschéma formel localement noethérien, le faisceau d'anneaux $\mathcal{O}_{\mathfrak{x}}$ est cohérent et tout faisceau d'idéaux de définition de X est cohérent.

La question étant locale, on est ramené au cas d'un schéma formel affine noethérien, et la proposition résulte donc de (10.10.3) et (10.10.5).

(10.11.2) Soient $\mathfrak{X}$ un préschéma formel localement noethérien, $\mathcal{J}$ un faisceau d'idéaux de définition de $\mathfrak{X},\mathbf{X}_{n}$ le préschéma (usuel) localement noethérien ($\mathfrak{X},\mathcal{O}_{\mathfrak{X}}/\mathcal{J}^{n+1}$), de sorte que $\mathfrak{X}$ est limite inductive de la suite ($\mathbf{X}_{n}$) pour les morphismes canoniques $u_{mn}:\mathbf{X}_{m}\to\mathbf{X}_{n}$ (10.6.3). Avec ces notations :

Théorème (10.11.3). — Pour qu'un $\mathcal{O}_{\mathfrak{X}}$-Module $\mathcal{F}$ soit cohérent, il faut et il suffit qu'il soit isomorphe à une limite projective d'une suite $(\mathcal{F}_n)$, où $\mathcal{F}_n$ est un $\mathcal{O}_{\mathrm{X}_n}$-Module cohérent, tel que $u_{mn}^*(\mathcal{F}_n) = \mathcal{F}_n$ pour $m \leqslant n$ (10.6.6). Le système projectif $(\mathcal{F}_n)$ est alors isomorphe au système des $u_n^*(\mathcal{F}) = \mathcal{F} \otimes_{\mathcal{O}_{\mathfrak{X}}} \mathcal{O}_{\mathrm{X}_n}$, $u_n$ étant le morphisme canonique $\mathrm{X}_n \to \mathfrak{X}$.

La question étant locale, on est ramené au cas où $\mathfrak{X}$ est un schéma formel affine noethérien, et le théorème est alors conséquence de (10.10.5) et (10.10.6).

On peut donc dire que la donnée d'un $\mathcal{O}_{\mathfrak{x}}$-Module cohérent équivaut à celle d'un système projectif $(\mathcal{F}_n)$ de $\mathcal{O}_{\mathrm{X}_n}$-Modules cohérents tels que $u_{nm}^{*}(\mathcal{F}_{n}) = \mathcal{F}_{m}$ pour $m \leqslant n$.

Corollaire (10.11.4). — Si F et G sont deux  $O_{x}$ -Modules cohérents, on peut (avec les notations de (10.11.3)) définir un isomorphisme canonique fonctoriel

$$
\operatorname{Hom} _ {\mathcal {O} _ {\mathfrak {X}}} (\mathcal {F}, \mathcal {G}) \xrightarrow {\sim} \lim _ {\leftarrow \overline {{n}}} \operatorname{Hom} _ {\mathcal {O} _ {\mathrm{X} _ {n}}} (\mathcal {F} _ {n}, \mathcal {G} _ {n})\tag{10.11.4.1}
$$

La limite projective du second membre doit s'entendre pour les applications $\theta_n \to u_{mn}^*(\theta_n) (m \leqslant n)$ de $\mathrm{Hom}_{\mathcal{O}_{X_n}}(\mathcal{F}_n, \mathcal{G}_n)$ dans $\mathrm{Hom}_{\mathcal{O}_{X_m}}(\mathcal{F}_m, \mathcal{G}_m)$. L'homomorphisme (10.11.4.1) fait correspondre à un élément $\theta \in \mathrm{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F}, \mathcal{G})$ la suite $(u_n^*(\theta))$; on voit aussitôt qu'on en définit un homomorphisme réciproque du précédent en faisant correspondre au système projectif $(\theta_n) \in \varprojlim_n \mathrm{Hom}_{\mathcal{O}_{X_n}}(\mathcal{F}_n, \mathcal{G}_n)$ sa limite projective dans $\mathrm{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F}, \mathcal{G})$, compte tenu de (10.11.3).

Corollaire (10.11.5). — Pour qu'un homomorphisme $\theta : \mathcal{F} \to \mathcal{G}$ soit surjectif, il faut et il suffit que l'homomorphisme correspondant $\theta_0 = u_0^*(\theta) : \mathcal{F}_0 \to \mathcal{G}_0$ le soit.

La question étant locale, on est ramené au cas où $\mathfrak{X} = \mathrm{Spf}(\mathbf{A})$, A étant adique noethérien, $\mathcal{F} = \mathbf{M}^{\Delta}$, $\mathcal{G} = \mathbf{N}^{\Delta}$ et $\theta = u^{\Delta}$, où $\mathbf{M}$ et $\mathbf{N}$ sont des A-modules de type fini et $u$ un homomorphisme $\mathbf{M} \to \mathbf{N}$; on a en outre alors $\theta_0 = \widetilde{u}_0$, où $u_0$ est l'homomorphisme $u \otimes \mathrm{i}: \mathbf{M} \otimes_{\mathrm{A}} \mathrm{A} / \mathfrak{J} \to \mathrm{N} \otimes_{\mathrm{A}} \mathrm{A} / \mathfrak{J}$; la conclusion résulte de ce que $\theta$ et $u$ (resp. $\theta_0$ et $u_0$) sont simultanément surjectifs (1.3.9 et 10.10.2) et de ce que $u$ et $u_0$ sont simultanément surjectifs (0, 7.1.14).

(10.11.6) Le th. (10.11.3) montre qu'on peut considérer tout $\mathcal{O}_{\mathfrak{x}}$-Module cohérent $\mathcal{F}$ comme un $\mathcal{O}_{\mathfrak{x}}$-Module topologique, en le considérant comme limite projective des faisceaux de groupes pseudo-discrets $\mathcal{F}_n$ (0, 3.8.1). Il résulte alors de (10.11.4) que tout homomorphisme $u: \mathcal{F} \to \mathcal{G}$ de $\mathcal{O}_{\mathfrak{x}}$-Modules cohérents est automatiquement continu

(0, 3.8.2). En outre, si H est un sous- $O_{x}$ -Module cohérent d'un  $O_{x}$ -Module cohérent F, pour tout ouvert  $U \subset X$ ,  $\Gamma(U, \mathcal{H})$  est un sous-groupe fermé du groupe topologique  $\Gamma(U, \mathcal{F})$  car le foncteur  $\Gamma$  étant exact à gauche,  $\Gamma(U, \mathcal{H})$  est le noyau de l'homomorphisme  $\Gamma(U, \mathcal{F}) \to \Gamma(U, \mathcal{F}/\mathcal{H})$ , qui est continu d'après ce qui précède, puisque F/H est cohérent (0, 5.3.4); notre assertion résulte de ce que  $\Gamma(U, \mathcal{F}/\mathcal{H})$  est un groupe topologique séparé.

Proposition (10.11.7). — Soient $\mathcal{F}$ et $\mathcal{G}$ deux $\mathcal{O}_{\mathfrak{x}}$-Modules cohérents. On peut définir (avec les notations de (10.11.3)) des isomorphismes canoniques fonctoriels de $\mathcal{O}_{\mathfrak{x}}$-Modules topologiques (10.11.6)

(10.11.7.1)

$$
\mathcal {F} \otimes_ {\mathcal {O} _ {\mathfrak {X}}} \mathcal {G} \simeq \varprojlim_ {n} (\mathcal {F} _ {n} \otimes_ {\mathcal {O} _ {\mathrm{X} _ {n}}} \mathcal {G} _ {n})\tag{10.11.7.2}
$$

$$
\mathcal {H} o m _ {\mathcal {O} _ {\mathfrak {X}}} (\mathcal {F}, \mathcal {G}) \xrightarrow {\sim} \varprojlim_ {n} \mathcal {H} o m _ {\mathcal {O} _ {\mathrm{X} _ {n}}} (\mathcal {F} _ {n}, \mathcal {G} _ {n})
$$

L'existence de l'isomorphisme (10.11.7.1) résulte de la formule

$$
\mathcal {F} _ {n} \otimes_ {\mathcal {O} _ {\mathrm{X} _ {n}}} \mathcal {G} _ {n} = (\mathcal {F} \otimes_ {\mathcal {O} _ {\mathfrak {X}}} \mathcal {O} _ {\mathrm{X} _ {n}}) \otimes_ {\mathcal {O} _ {\mathrm{X} _ {n}}} (\mathcal {G} \otimes_ {\mathcal {O} _ {\mathfrak {X}}} \mathcal {O} _ {\mathrm{X} _ {n}}) = (\mathcal {F} \otimes_ {\mathcal {O} _ {\mathfrak {X}}} \mathcal {G}) \otimes_ {\mathcal {O} _ {\mathfrak {X}}} \mathcal {O} _ {\mathrm{X} _ {n}}
$$

et de (10.11.3). L'isomorphisme (10.11.7.2) où les deux membres sont considérés comme faisceaux de modules sans topologie, résulte de la définition des sections de $\mathcal{H}om_{\mathcal{O}_{\mathfrak{X}}}(F, G)$ et $\mathcal{H}om_{\mathcal{O}_{\mathbb{X}_n}}(\mathcal{F}_n, \mathcal{G}_n)$ et de l'existence de l'isomorphisme (10.11.4.1), appliqué au préschéma induit sur un ouvert formel affine noethérien arbitraire de $\mathfrak{X}$. Reste à prouver que l'isomorphisme (10.11.7.2) est bicontinu au-dessus d'un ensemble quasi-compact, et on est donc ramené au cas où $\mathfrak{X} = \mathrm{Spf(A)}$, A étant adique noethérien, d'où (10.10.5) $F = M^{\Delta}$, $G = N^{\Delta}$, M, N étant des A-modules de type fini; compte tenu de (10.10.2.1), (10.10.2.3) et (1.3.12, (ii)), on est ramené à montrer que l'isomorphisme canonique $\mathrm{Hom}_{\mathrm{A}}(\mathrm{M}, \mathrm{N}) \xrightarrow{\sim} \lim_{\substack{n \\ \longrightarrow}} \mathrm{Hom}_{\mathrm{A}_n}(\mathrm{M}_n, \mathrm{N}_n)$ (avec $\mathrm{M}_n = \mathrm{M} \otimes_{\mathrm{A}} \mathrm{A}_n$, $\mathrm{N}_n = \mathrm{N} \otimes_{\mathrm{A}} \mathrm{A}_n$) est continu, ce qui a été prouvé dans (0, 7.8.2).

(10.11.8) Comme $\operatorname{Hom}_{\mathcal{O}_{\mathfrak{X}}}(F, G)$ est le groupe des sections du faisceau de groupes topologiques $\operatorname{Hom}_{\mathcal{O}_{\mathfrak{X}}}(F, G)$, il est muni d'une topologie de groupe. Si $\mathfrak{X}$ est noethérien, il résulte de (10.11.7.2) qu'un système fondamental de voisinages de o dans ce groupe s'obtient en prenant les sous-groupes $\operatorname{Hom}_{\mathcal{O}_{\mathfrak{X}}}(F, J^{n}G)$ ($n$ arbitraire).

Proposition (10.11.9). — Soient $\mathfrak{X}$ un préschéma formel noethérien, $\mathcal{F}$ et $\mathcal{G}$ deux $\mathcal{O}_{\mathfrak{X}}$-Modules cohérents. Dans le groupe topologique $\mathrm{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F},\mathcal{G})$ les homomorphismes surjectifs (resp. injectifs, bijectifs) forment une partie ouverte.

En vertu de (10.11.5), l'ensemble des homomorphismes surjectifs dans $\mathrm{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F},\mathcal{G})$ est l'image réciproque par l'application continue $\mathrm{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F},\mathcal{G})\to \mathrm{Hom}_{\mathcal{O}_{\mathfrak{X}_0}}(\mathcal{F}_0,\mathcal{G}_0)$ d'une partie du groupe discret $\mathrm{Hom}_{\mathcal{O}_{\mathfrak{X}_0}}(\mathcal{F}_0,\mathcal{G}_0)$ d'où la première assertion. Pour démontrer la seconde, recouvrons $\mathfrak{X}$ par un nombre fini d'ouverts formels affines noethériens $U_i$. Pour que $\theta \in \mathrm{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F},\mathcal{G})$ soit injectif, il faut et il suffit que toutes ses images par les applications (continues) de restriction $\mathrm{Hom}_{\mathcal{O}_{\mathfrak{X}}}(\mathcal{F},\mathcal{G})\to \mathrm{Hom}_{\mathcal{O}_{\mathfrak{X}}|U_i}(\mathcal{F}|U_i,\mathcal{G}|U_i)$ le soient; on est donc ramené au cas affine, et alors cela a déjà été prouvé dans (0, 7.8.3).

## 10.12. Morphismes adiques de préschémas formels.

(10.12.1) Soient $\mathfrak{X}$, $\mathfrak{S}$ deux préschémas formels localement noethériens; nous dirons qu'un morphisme $f: \mathfrak{X} \to \mathfrak{S}$ est adique s'il existe un Idéal de définition $\mathcal{J}$ de $\mathfrak{S}$ tel que $\mathcal{K} = f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}}$ soit un Idéal de définition de $\mathfrak{X}$; on dit aussi alors que $\mathfrak{X}$ est un $\mathfrak{S}$-préschéma adique (pour $f$). Lorsqu'il en est ainsi, pour tout Idéal de définition $\mathcal{J}_{1}$ de $\mathfrak{S}$, $\mathcal{K}_{1} = f^{*}(\mathcal{J}_{1})\mathcal{O}_{\mathfrak{X}}$ est un Idéal de définition de $\mathfrak{X}$. En effet, la question étant locale, on peut supposer $\mathfrak{X}$ et $\mathfrak{S}$ affines noethériens; il existe donc un entier $n$ tel que $\mathcal{J}^{n} \subset \mathcal{J}_{1}$ et $\mathcal{J}_{1}^{n} \subset \mathcal{J}$ (10.3.6 et 0, 7.1.4), d'où $\mathcal{K}^{n} \subset \mathcal{K}_{1}$ et $\mathcal{K}_{1}^{n} \subset \mathcal{K}$. La première de ces relations prouve que $\mathcal{K}_{1} = \mathfrak{R}_{1}^{\Delta}$, où $\mathfrak{R}_{1}$ est un idéal ouvert de A=Γ($\mathfrak{X}$, $\mathcal{O}_{\mathfrak{X}}$), et la seconde prouve que $\mathfrak{R}_{1}$ est un idéal de définition de A (0, 7.1.4), d'où notre assertion.

Il résulte aussitôt de ce qui précède que si $\mathfrak{X}$ et $\mathfrak{Y}$ sont deux $\mathfrak{S}$-préschémas adiques, tout $\mathfrak{S}$-morphisme $u: \mathfrak{X} \to \mathfrak{Y}$ est adique : en effet, si $f: \mathfrak{X} \to \mathfrak{S}$, $g: \mathfrak{Y} \to \mathfrak{S}$ sont les morphismes structuraux, et $\mathcal{J}$ un Idéal de définition de $\mathfrak{S}$, on a $f = g \circ u$, donc $u^{*}(g^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{Y}})\mathcal{O}_{\mathfrak{x}} = f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{x}}$ est un Idéal de définition de $\mathfrak{X}$, et par hypothèse $g^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{Y}}$ est un Idéal de définition de $\mathfrak{Y}$.

(10.12.2) Dans ce qui suit, nous supposerons fixé un préschéma formel localement noethérien S et un Idéal de définition J de S; nous poserons  $\mathrm{S}_{n}=(\mathfrak{S},\mathcal{O}_{\mathfrak{S}}/\mathcal{J}^{n+1})$ . Les S-préschémas adiques (localement noethériens) forment évidemment une catégorie. Nous dirons qu'un système inductif  $(\mathrm{X}_{n})$  de  $S_{n}$ -préschémas (usuels) localement noethériens est un  $(\mathrm{S}_{n})$ -système inductif adique si les morphismes structuraux  $f_{n}:X_{n}\to S_{n}$  sont tels que, pour  $m\leqslant n$ , les diagrammes

$$
\begin{array}{c} \mathrm{X} _ {n} \leftarrow \mathrm{X} _ {m} \\ f _ {n} \Bigg \downarrow \qquad \qquad \qquad \qquad \Bigg \downarrow f _ {m} \\ \mathrm{S} _ {n} \leftarrow \mathrm{S} _ {m} \end{array}\tag{10.12.2.1}
$$

soient commutatifs et identifient  $X_{m}$  au produit  $\mathbf{X}_{n}\times_{\mathrm{S}_{n}}\mathbf{S}_{m}=(\mathbf{X}_{n})_{(\mathrm{S}_{n})}$ . Les systèmes inductifs adiques forment une catégorie : il suffit en effet de définir un morphisme  $(\mathbf{X}_{n})\to(\mathbf{Y}_{n})$  de tels systèmes comme un système inductif de  $S_{n}$ -morphismes  $u_{n}:X_{n}\to Y_{n}$  tel que  $u_{m}$  s'identifie à  $(u_{n})_{(\mathrm{S}_{m})}$  pour  $m\leqslant n$ . Cela étant :

Théorème (10.12.3). — Il y a équivalence canonique entre la catégorie des S-préschémas adiques et la catégorie des  $(\mathrm{S}_{n})$ -systèmes inductifs adiques.

L'équivalence en question s'obtient de la façon suivante : si $\mathfrak{X}$ est un $\mathfrak{S}$-préschéma adique, $f: \mathfrak{X} \to \mathfrak{S}$ le morphisme structural, $\mathcal{K} = f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}}$ est un Idéal de définition de $\mathfrak{X}$ et on fait correspondre à $\mathfrak{X}$ le système inductif des $\mathrm{X}_{n} = (\mathfrak{X}, \mathcal{O}_{\mathfrak{X}} / \mathcal{K}^{n+1})$, le morphisme structural $f_{n}: \mathrm{X}_{n} \to \mathrm{S}_{n}$ correspondant à $f$ (10.5.6). Montrons d'abord que $(\mathrm{X}_{n})$ est un système inductif adique : si $f = (\psi, \theta)$, on a $\psi^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}} = \mathcal{K}$, donc $\psi^{*}(\mathcal{J}^{n})\mathcal{O}_{\mathfrak{X}} = \mathcal{K}^{n}$ pour tout $n$, et (par l'exactitude du foncteur $\psi^{*}$) $\mathcal{K}^{m+1} / \mathcal{K}^{n+1} = \psi^{*}(\mathcal{J}^{m+1} / \mathcal{J}^{n+1})(\mathcal{O}_{\mathfrak{X}} / \mathcal{K}^{n+1})$ pour $m \leqslant n$; notre conclusion résulte donc de (4.4.5). Il est immédiat en outre de vérifier qu'à un $\mathfrak{S}$-morphisme $u: \mathfrak{X} \to \mathfrak{Y}$ de $\mathfrak{S}$-préschémas adiques correspond (avec des notations évidentes)

un système inductif de  $S_{n}$ -morphismes  $u_{n}: X_{n} \to Y_{n}$  tel que  $u_{m}$  s'identifie à  $(u_{n})_{(S_{m})}$  pour  $m \leqslant n$ .

Le fait qu'on a bien défini ainsi une équivalence résultera de la proposition plus précise suivante :

Proposition (10.12.3.1). — Soit  $(\mathbf{X}_{n})$  un système inductif de  $S_{n}$ -préschémas; on suppose que les morphismes structuraux  $f_{n}: X_{n} \to S_{n}$  sont tels que les diagrammes (10.12.2.1) soient commutatifs et identifient  $X_{m}$  à  $X_{n} \times_{S_{n}} S_{m}$  pour  $m \leqslant n$ . Alors le système inductif  $(\mathbf{X}_{n})$  vérifie les conditions b) et c) de (10.6.3); soient X sa limite inductive,  $f: X \to S$  le morphisme limite inductive du système inductif  $(f_{n})$ . Alors, si  $X_{0}$  est localement noethérien, X est localement noethérien et f est un morphisme adique.

Comme le faisceau d'idéaux de $\mathcal{O}_{\mathrm{S}_n}$ qui définit le sous-préschéma $\mathrm{S}_m$ de $\mathrm{S}_n$ est nilpotent, il en est de même, en vertu de (4.4.5) du faisceau d'idéaux de $\mathcal{O}_{\mathrm{X}_n}$ définissant le sous-préschéma $\mathrm{X}_m$ de $\mathrm{X}_n$, donc les conditions de (10.6.3) sont bien vérifiées. La question est par suite locale sur $\mathfrak{X}$ et $\mathfrak{S}$ et on peut supposer que $\mathfrak{S} = \operatorname{Spf}(\mathrm{A})$, $\mathcal{J} = \mathfrak{J}^{\Delta}$, A étant un anneau $\mathfrak{J}$-adique noethérien, et $\mathrm{X}_n = \operatorname{Spec}(\mathrm{B}_n)$; si $\mathrm{A}_n = \mathrm{A} / \mathfrak{J}^{n+1}$, l'hypothèse entraîne que $\mathrm{B}_0$ est noethérien et que si on pose $\mathfrak{J}_n = \mathfrak{J} / \mathfrak{J}^{n+1}$, $\mathrm{B}_m = \mathrm{B}_n / \mathfrak{J}_n^{m+1}\mathrm{B}_n$. Le noyau de $\mathrm{B}_n \to \mathrm{B}_0$ est donc $\mathfrak{R}_n = \mathfrak{J}_n\mathrm{B}_n$ et le noyau de $\mathrm{B}_n \to \mathrm{B}_m$ est $\mathfrak{R}_n^{m+1}$ pour $m \leqslant n$; en outre, comme $\mathrm{A}_1$ est noethérien, $\mathfrak{J}_1$ est de type fini sur $\mathrm{A}_1$, donc $\mathfrak{R}_1 = \mathfrak{R}_1 / \mathfrak{R}_1^2$ est de type fini sur $\mathrm{B}_1$, et a fortiori sur $\mathrm{B}_0 = \mathrm{B}_1 / \mathfrak{R}_1$; le fait que $\mathfrak{X}$ soit noethérien résulte alors de (10.6.4); si $\mathrm{B} = \lim_{\mathbf{B} \to 0} \mathrm{B}_n$, on a $\mathfrak{X} = \operatorname{Spf}(\mathrm{B})$, et si $\mathfrak{X}$ est le noyau de $\mathrm{B} \to \mathrm{B}_0$, $\mathrm{B}_n = \mathrm{B} / \mathfrak{R}^{n+1}$. Si $\rho_n: \overleftarrow{\mathrm{A}}/\overleftarrow{\mathfrak{J}}^{n+1} \to \overline{\mathrm{B}}/\mathfrak{R}^{n+1}$ est l'homomorphisme correspondant à $f_n$, on a donc

$$
\Re / \Re^ {n + 1} = (\mathrm{B} / \Re^ {n + 1}) \rho_ {n} (\Im / \Im^ {n + 1})
$$

comme l'homomorphisme $\rho: A \to B$ correspondant à $f$ est égal à $\varprojlim \rho_n$, l'idéal $\mathfrak{J}B$ de $B$ est dense dans $\mathfrak{K}$, et comme tout idéal de $B$ est fermé (0, 7.3.5), on a $\mathfrak{K} = \mathfrak{J}B$. Si $\mathcal{K} = \mathcal{K}^{\Delta}$, la relation $f^{*}(\mathcal{J})\mathcal{O}_{\mathfrak{X}} = \mathcal{K}$ résulte alors de (10.10.9) et achève la démonstration. (10.12.3.2) L'équivalence précédente fournit, pour deux $\mathfrak{S}$-préschémas adiques $\mathfrak{X}$, $\mathfrak{Y}$, une bijection canonique

$$
\operatorname{Hom} _ {\mathfrak {S}} (\mathfrak {X}, \mathfrak {Y}) \simeq \varprojlim_ {n} \operatorname{Hom} _ {\mathrm{S} _ {n}} (\mathrm{X} _ {n}, \mathrm{Y} _ {n})
$$

la limite projective étant relative aux applications  $u_{n}\to(u_{n})_{(S_{m})}$  pour  $m\leqslant n$ .

## 10.13. Morphismes de type fini.

Proposition (10.13.1). — Soient $\mathfrak{Y}$ un préschéma formel localement noethérien, $\mathcal{K}$ un Idéal de définition de $\mathfrak{Y}$, $f: \mathfrak{X} \to \mathfrak{Y}$ un morphisme de préschémas formels. Les conditions suivantes sont équivalentes :

a) $\mathfrak{X}$ est localement noethérien, $f$ est un morphisme adique (10.12.1) et si l'on pose $\mathcal{J} = f^{*}(\mathcal{K})\mathcal{O}_{\mathfrak{X}}$, le morphisme $f_{0}: (\mathfrak{X}, \mathcal{O}_{\mathfrak{X}} / \mathcal{J}) \to (\mathfrak{Y}, \mathcal{O}_{\mathfrak{Y}} / \mathcal{K})$ déduit de $f$ est de type fini.

b) $\mathfrak{X}$ est localement noethérien, et est limite inductive d'un $(\mathbf{Y}_n)$-système inductif adique $(\mathbf{X}_n)$ tel que le morphisme $\mathbf{X}_0 \to \mathbf{Y}_0$ soit de type fini.

c) Tout point de $\mathfrak{V}$ possède un voisinage ouvert formel affine noethérien V ayant la propriété suivante :

(Q) $f^{-1}(V)$ est réunion d'une famille finie d'ouverts formels affines noethériens $U_i$ tels que l'anneau adique noethérien $\Gamma(U_i, \mathcal{O}_{\mathfrak{X}})$ soit topologiquement isomorphe au quotient d'une algèbre de séries formelles restreintes (0, 7.5.1) sur $\Gamma(V, \mathcal{O}_{\mathfrak{Y}})$, par un idéal (nécessairement fermé).

Il est immédiat que $a)$ entraîne $b)$ en vertu de (10.12.3). Pour montrer que $b)$ entraîne $c)$, on peut, puisque la question est locale sur $\mathfrak{Y}$, supposer que $\mathfrak{Y}=\mathrm{Spf}(B)$, où $B$ est adique noethérien; soit $\mathcal{K}=\mathfrak{R}^{\Delta}$, $\mathfrak{R}$ étant un idéal de définition de $B$. Comme par hypothèse, $\mathbf{X}_{0}$ est de type fini sur $\mathbf{Y}_{0}$, $\mathbf{X}_{0}$ est réunion finie d'ouverts affines $\mathbf{U}_{i}$ tels que l'anneau $\mathbf{A}_{i0}$ du schéma affine induit par $\mathbf{X}_{0}$ sur $\mathbf{U}_{i}$ soit une algèbre de type fini sur l'anneau $\mathbf{B}/\mathfrak{R}$ de $\mathbf{Y}_{0}$ (6.3.2). En vertu de (5.1.9), $\mathbf{U}_{i}$ est aussi un ouvert affine dans chacun des préschémas noethériens $\mathbf{X}_{n}$, et si $\mathbf{A}_{in}$ est l'anneau du schéma affine induit par $\mathbf{X}_{n}$ sur $\mathbf{U}_{i}$, l'hypothèse $b)$ entraîne que pour $m\leqslant n$, $\mathbf{A}_{im}$ est isomorphe à $\mathbf{A}_{in}/\mathfrak{R}^{m+1}\mathbf{A}_{in}$. Par suite, le préschéma formel induit sur $\mathbf{U}_{i}$ par $\mathfrak{X}$ est isomorphe à $\mathrm{Spf}(\mathbf{A}_{i})$, où $\mathbf{A}_{i}=\varprojlim\mathbf{A}_{in}$

(10.6.4) ;  $A_{i}$  est un anneau  $R A_{i}$ -adique, et  $A_{i}/R A_{i}$ , isomorphe à  $A_{i0}$ , est une algèbre de type fini sur B/R. On en conclut (0, 7.5.5) que  $A_{i}$  est topologiquement isomorphe à un quotient d'une algèbre de séries formelles restreintes sur B (par un idéal nécessairement fermé, puisqu'une telle algèbre est noethérienne (0, 7.5.4)).

Pour démontrer que c) entraîne a), on peut se limiter au cas où $\mathfrak{X}=\mathrm{Spf}(A)$ est aussi affine, A étant un anneau adique noethérien, isomorphe au quotient d'une algèbre de séries formelles restreintes sur B par un idéal fermé. Alors (0, 7.5.5), A/RA est une algèbre de type fini sur B/R, et RA=J est un idéal de définition de A, donc, en vertu de (10.10.9), les conditions de a) sont satisfaites.

On notera que si les conditions de la prop. (10.13.1) sont remplies, la propriété $a$) est valable pour tout Idéal de définition $\mathcal{K}$ de $\mathfrak{Y}$ (en vertu de $c$), et par suite, dans la propriété $b$), tous les $f_n$ sont des morphismes de type fini.

Corollaire (10.13.2). — Si les conditions de (10.13.1) sont vérifiées, tout ouvert formel affine noethérien V de Y possède la propriété (Q) et si Y est noethérien, il en est de même de X.

Cela résulte aussitôt de (10.13.1) et de (6.3.2).

Définition (10.13.3). — Lorsque les propriétés équivalentes a), b), c) de (10.13.1) sont vérifiées, on dit que le morphisme f est de type fini, ou que X est un Y-préschéma formel de type fini, ou un préschéma formel de type fini au-dessus de Y.

Corollaire (10.13.4). — Soient $\mathfrak{X} = \operatorname{Spf}(A)$, $\mathfrak{Y} = \operatorname{Spf}(B)$ deux schémas formels affines noethériens ; pour que $\mathfrak{X}$ soit de type fini sur $\mathfrak{Y}$, il faut et il suffit que l'anneau adique noethérien A soit isomorphe au quotient d'une algèbre de séries formelles restreintes sur B par un idéal fermé.

En effet, avec les notations de (10.13.1), si $\mathfrak{X}$ est de type fini sur $\mathfrak{Y}$, A/KA est alors une (B/$\mathfrak{X}$)-algèbre de type fini en vertu de (6.3.3) et RA est un idéal de définition de A (10.10.9). On conclut donc par (0, 7.5.5).

Proposition (10.13.5). — (i) Le composé de deux morphismes de préschémas formels qui sont de type fini est de type fini.

(ii) Soient $\mathfrak{X}$, $\mathfrak{S}$, $\mathfrak{S}'$ trois préschémas formels localement noethériens (resp. noethériens), $f: \mathfrak{X} \to \mathfrak{S}$, $g: \mathfrak{S}' \to \mathfrak{S}$ deux morphismes. Si $f$ est de type fini, $\mathfrak{X} \times_{\mathfrak{S}} \mathfrak{S}'$ est localement noethérien (resp. noethérien) et est de type fini sur $\mathfrak{S}'$.

(iii) Soient S un préschéma formel localement noethérien,  $X'$ ,  $Y'$  deux S-préschémas formels localement noethériens tels que  $X' \times_{\otimes}Y'$  soit localement noethérien. Si X, Y sont des S-préschémas formels localement noethériens,  $f : X \to X'$ ,  $g : Y \to Y'$  deux S-morphismes de type fini,  $X \times_{\otimes}Y$  est localement noethérien et  $f \times_{\otimes}g$  est un S-morphisme de type fini.

(iii) se déduit de (i) et (ii) par le raisonnement formel de (3.5.1) et il suffit donc de prouver (i) et (ii).

Soient $\mathfrak{X},\mathfrak{Y},\mathfrak{Z}$ trois préschémas formels localement noethériens, $f:\mathfrak{X}\to\mathfrak{Y},g:\mathfrak{Y}\to\mathfrak{Z}$ deux morphismes de type fini. Si $\mathcal{L}$ est un Idéal de définition de $\mathfrak{Z}$, $\mathcal{K}=g^{*}(\mathcal{L})\mathcal{O}_{\mathfrak{Y}}$ en est un pour $\mathfrak{Y}$ et $\mathcal{J}=f^{*}(g^{*}(\mathcal{L}))\mathcal{O}_{\mathfrak{X}}$ en est un pour $\mathfrak{X}$. Posons $X_{0}=(\mathfrak{X},\mathcal{O}_{\mathfrak{X}}/\mathcal{J})$, $Y_{0}=(\mathfrak{Y},\mathcal{O}_{\mathfrak{Y}}/\mathcal{K})$, $Z_{0}=(3,\mathcal{O}_{3}/\mathcal{L})$ et soient $f_{0}:X_{0}\to Y_{0}$, $g_{0}:Y_{0}\to Z_{0}$ les morphismes correspondant à $f$ et $g$. Comme par hypothèse $f_{0}$ et $g_{0}$ sont de type fini, il en est de même de $g_{0}o f_{0}$ (6.3.4) qui correspond à $gof$; donc $gof$ est de type fini par (10.13.1).

Sous les conditions de (ii), $\mathfrak{S}$ (resp. $\mathfrak{X},\mathfrak{S}^{\prime}$) est limite inductive d'une suite $(\mathbf{S}_n)$ (resp. $(\mathbf{X}_n),(\mathbf{S}_n^{\prime}))$ de préschémas localement noethériens et on peut supposer (10.13.1) que $\mathbf{X}_m = \mathbf{X}_n\times_{\mathbb{S}_n}\mathbf{S}_m$ pour $m\leqslant n$. Le préschéma formel $\mathfrak{X}\times_{\mathfrak{S}}\mathfrak{S}^{\prime}$ est alors limite inductive des préschémas $\mathbf{X}_n\times_{\mathbb{S}_n}\mathbf{S}_n^{\prime}$ (10.7.4), et on a

$$
\mathbf {X} _ {m} \times_ {\mathrm{S} _ {m}} \mathrm{S} _ {m} ^ {\prime} = (\mathbf {X} _ {n} \times_ {\mathrm{S} _ {n}} \mathrm{S} _ {m}) \times_ {\mathrm{S} _ {m}} \mathrm{S} _ {m} ^ {\prime} = (\mathbf {X} _ {n} \times_ {\mathrm{S} _ {n}} \mathrm{S} _ {n} ^ {\prime}) \times_ {\mathrm{S} _ {n} ^ {\prime}} \mathrm{S} _ {m} ^ {\prime}.
$$

En outre,  $X_{0} \times_{S_{0}} S_{0}'$  est localement noethérien puisque  $X_{0}$  est de type fini sur  $S_{0}$  (6.3.8). On en conclut d'abord (10.12.3.1) que  $X \times_{S} S'$  est localement noethérien ; en outre, comme  $X_{0} \times_{S_{0}} S_{0}'$  est de type fini sur  $S_{0}'$  (6.3.8), il résulte de (10.12.3.1) et de (10.13.1) que  $X \times_{S} S'$  est de type fini sur  $S'$, ce qui achève de prouver (ii) (l'assertion relative aux préschémas noethériens étant conséquence immédiate de (6.3.8)).

Corollaire (10.13.6). — Sous les hypothèses de (10.9.9), si f est un morphisme de type fini, il en est de même de son prolongement $\hat{f}$ aux complétés.

## 10.14. Sous-préschémas fermés des préschémas formels.

Proposition (10.14.1). — Soient $\mathfrak{X}$ un préschéma formel localement noethérien, $\mathcal{A}$ un faisceau d'idéaux cohérent de $\mathcal{O}_{\mathfrak{X}}$. Si $\mathfrak{Y}$ est le support (fermé) de $\mathcal{O}_{\mathfrak{X}}/\mathcal{A}$, l'espace topologiquement annelé $(\mathfrak{Y}, (\mathcal{O}_{\mathfrak{X}}/\mathcal{A})|\mathfrak{Y})$ est un préschéma formel localement noethérien, qui est noethérien si $\mathfrak{X}$ l'est.
Notons que $\mathcal{O}_{\mathfrak{X}}/\mathcal{A}$ est cohérent en vertu de (10.10.3) et (0, 5.3.4), donc son support $\mathfrak{Y}$ est fermé (0, 5.2.2). Soit $\mathcal{J}$ un Idéal de définition de $\mathfrak{X}$, et soit $X_{n}=(\mathfrak{X},\mathcal{O}_{\mathfrak{X}}/\mathcal{J}^{n+1})$; le faisceau d'anneaux $\mathcal{O}_{\mathfrak{X}}/\mathcal{A}$ est limite projective des faisceaux $\mathcal{O}_{\mathfrak{X}}/(\mathcal{A}+\mathcal{J}^{n+1})=(\mathcal{O}_{\mathfrak{X}}/\mathcal{A})\otimes_{\mathcal{O}_{\mathfrak{X}}(\mathcal{O}_{\mathfrak{X}}/\mathcal{J}^{n+1})}$ (10.11.3), qui ont tous pour support $\mathfrak{Y}$. Le faisceau $(\mathcal{A}+\mathcal{J}^{n+1})/\mathcal{J}^{n+1}$ est un $\mathcal{O}_{\mathfrak{X}}$-Module cohérent, puisque $\mathcal{J}^{n+1}$ est cohérent, donc $(\mathcal{A}+\mathcal{J}^{n+1})/\mathcal{J}^{n+1}$ est aussi un $(\mathcal{O}_{\mathfrak{X}}/\mathcal{J}^{n+1})$-Module cohérent (0, 5.3.10); si $Y_{n}$ est le sous-préschéma fermé de $X_{n}$ défini par ce faisceau d'idéaux, il est immédiat que $(\mathfrak{Y}, (\mathcal{O}_{\mathfrak{X}}/\mathcal{A})|\mathfrak{Y})$

est le préschéma formel limite inductive des  $Y_{n}$ , et comme les conditions de (10.6.4) sont satisfaites, cela prouve que ce préschéma formel est localement noethérien, et noethérien si X l'est (puisque alors  $Y_{0}$  l'est en vertu de (6.1.4)).

Définition (10.14.2). — On appelle sous-préschéma fermé d'un préschéma formel $\mathfrak{X}$ tout préschéma formel $(\mathfrak{Y}, (\mathcal{O}_{\mathfrak{X}} / \mathcal{A}) | \mathfrak{Y})$ où $\mathcal{A}$ est un $\mathcal{O}_{\mathfrak{X}}$-Module cohérent ; on dit que ce préschéma est le sous-préschéma fermé défini par $\mathcal{A}$.

Il est clair que la correspondance ainsi définie entre $\mathcal{O}_{\mathfrak{X}}$-Modules cohérents et sous-préschémas fermés de $\mathfrak{X}$ est biunivoque.

Le morphisme d'espaces topologiquement annelés $j = (\psi, \theta) : \mathfrak{Y} \to \mathfrak{X}$, où $\psi$ est l'injection $\mathfrak{Y} \to \mathfrak{X}$ et $\theta^{\#}$ l'homomorphisme canonique $\mathcal{O}_{\mathfrak{x}} \to \mathcal{O}_{\mathfrak{x}} / \mathcal{A}$, est évidemment (10.4.5) un morphisme de préschémas formels, qu'on appelle l'injection canonique de $\mathfrak{Y}$ dans $\mathfrak{X}$. On notera que si $\mathfrak{X} = \text{Spf}(A)$, où $A$ est adique noethérien, on a $\mathcal{A} = a^{\Delta}$, où $a$ est un idéal de $A$ (10.10.5), et il résulte aussitôt de ce qui précède que l'on a alors $\mathfrak{Y} = \text{Spf}(A/a)$ à un isomorphisme près, et que $j$ correspond (10.2.2) à l'homomorphisme canonique $A \to A/a$.

On dit qu'un morphisme $f: \mathfrak{Z} \to \mathfrak{X}$ de préschémas formels localement noethériens est une immersion fermée si elle se factorise en $\mathfrak{Z} \xrightarrow{g} \mathfrak{Y} \xrightarrow{j} \mathfrak{X}$, où $g$ est un isomorphisme de $\mathfrak{Z}$ sur un sous-préschéma fermé $\mathfrak{Y}$ de $\mathfrak{X}$ et $j$ l'injection canonique. Comme $j$ est un monomorphisme d'espaces annelés, $g$ et $\mathfrak{Y}$ sont nécessairement uniques.

Proposition (10.14.3). — Une immersion fermée est un morphisme de type fini.

On se ramène aussitôt au cas où $\mathfrak{X}$ est un schéma formel affine $\operatorname{Spf}(A)$ et $\mathfrak{Y} = \operatorname{Spf}(A/a)$; la proposition résulte de (10.13.1, c)).

Lemme (10.14.4). — Soit $f: \mathfrak{Y} \to \mathfrak{X}$ un morphisme de préschémas formels localement noethériens, et soit $(\mathrm{U}_{\alpha})$ un recouvrement de $f(\mathfrak{Y})$ par des ouverts formels affines noethériens de $\mathfrak{X}$, tels que les $f^{-1}(\mathrm{U}_{\alpha})$ soient des ouverts formels affines noethériens de $\mathbf{Y}$. Pour que $f$ soit une immersion fermée, il faut et il suffit que $f(\mathfrak{Y})$ soit une partie fermée de $\mathfrak{X}$ et que, pour tout $\alpha$, la restriction de $f$ à $f^{-1}(\mathrm{U}_{\alpha})$ corresponde (10.4.6) à un homomorphisme surjectif $\Gamma(\mathrm{U}_{\alpha}, \mathcal{O}_{\mathfrak{X}}) \to \Gamma(f^{-1}(\mathrm{U}_{\alpha}), \mathcal{O}_{\mathfrak{Y}})$.

Les conditions sont évidemment nécessaires. Inversement, si elles sont remplies, et si on désigne par $\mathfrak{a}_{\alpha}$ le noyau de $\Gamma(\mathrm{U}_{\alpha},\mathcal{O}_{\mathfrak{x}})\to\Gamma(f^{-1}(\mathrm{U}_{\alpha}),\mathcal{O}_{\mathfrak{y}})$, on définit un faisceau cohérent d'idéaux $\mathscr{A}$ de $\mathcal{O}_{\mathfrak{x}}$ en prenant $\mathscr{A}|U_{\alpha}=a_{\alpha}^{\Delta}$, et en prenant $\mathscr{A}$ nul dans le complémentaire de la réunion des $U_{\alpha}$. En effet, puisque $f(\mathfrak{Y})$ est fermé et que le support de $a_{\alpha}^{\Delta}$ est $U_{\alpha}\cap f(\mathfrak{Y})$, tout revient à vérifier que $a_{\alpha}^{\Delta}$ et $a_{\beta}^{\Delta}$ induisent le même faisceau sur un ouvert formel affine noethérien $V\subset U_{\alpha}\cap U_{\beta}$. Or, la restriction de $f$ à $f^{-1}(U_{\alpha})$ étant une immersion fermée de ce préschéma formel dans $U_{\alpha},f^{-1}(V)$ est un ouvert formel affine noethérien dans $f^{-1}(U_{\alpha})$ et la restriction de $f$ à $f^{-1}(V)$ est une immersion fermée; si b est le noyau de l'homomorphisme surjectif $\Gamma(V,\mathcal{O}_{\mathfrak{x}})\to\Gamma(f^{-1}(V),\mathcal{O}_{\mathfrak{y}})$ correspondant à cette restriction, il est immédiat (10.10.2) que $a_{\alpha}^{\Delta}$ induit $b^{\Delta}$ sur V. Le faisceau d'idéaux $\mathscr{A}$ étant ainsi défini, il est alors clair que $f=goj$, où $j:3\to\mathfrak{X}$ est l'injection canonique du sous-préschéma fermé 3 de $\mathfrak{X}$ défini par $\mathscr{A}$, et g un isomorphisme de $\mathfrak{Y}$ sur 3.

Proposition (10.14.5). — (i) Si $f:3\to\mathfrak{Y}$, $g:\mathfrak{Y}\to\mathfrak{X}$ sont des immersions fermées de préschémas formels localement noethériens, gof est une immersion fermée.

(ii) Soient $\mathfrak{X}$, $\mathfrak{Y}$, $\mathfrak{S}$ trois préschémas formels localement noethériens, $f: \mathfrak{X} \to \mathfrak{S}$ une immersion fermée, $g: \mathfrak{Y} \to \mathfrak{S}$ un morphisme. Alors le morphisme $\mathfrak{X} \times_{\mathfrak{S}} \mathfrak{Y} \to \mathfrak{Y}$ est une immersion fermée.

(iii) Soient S un préschéma formel localement noethérien,  $X'$ ,  $Y'$  deux S-préschémas formels localement noethériens tels que  $X' \times_{S}Y'$  soit localement noethérien. Si X, Y sont des S-préschémas formels localement noethériens,  $f : X \to X'$ ,  $g : Y \to Y'$  deux S-morphismes qui sont des immersions fermées, alors  $f \times_{S}g$  est une immersion fermée.

En vertu de (3.5.1), il suffit encore de prouver (i) et (ii).

Pour démontrer (i), on peut supposer que $\mathfrak{Y}$ (resp. 3) est un sous-préschéma fermé de $\mathfrak{X}$ (resp. $\mathfrak{Y}$) défini par un faisceau cohérent $\mathcal{J}$ (resp. $\mathcal{K}$) d'idéaux de $\mathcal{O}_{\mathfrak{X}}$ (resp. $\mathcal{O}_{\mathfrak{Y}}$); si $\psi$ est l'injection $\mathfrak{Y} \to \mathfrak{X}$ des espaces sous-jacents, $\psi_{*}(\mathcal{K})$ est un faisceau cohérent d'idéaux de $\psi_{*}(\mathcal{O}_{\mathfrak{Y}}) = \mathcal{O}_{\mathfrak{X}} / \mathcal{J}$ (0, 5.3.12), donc aussi un $\mathcal{O}_{\mathfrak{X}}$-Module cohérent (0, 5.3.10); le noyau $\mathcal{K}_1$ de $\mathcal{O}_{\mathfrak{X}} \to (\mathcal{O}_{\mathfrak{X}} / \mathcal{J}) / \psi_{*}(\mathcal{K})$ est donc un faisceau cohérent d'idéaux de $\mathcal{O}_{\mathfrak{X}}$ (0, 5.3.4), et $\mathcal{O}_{\mathfrak{X}} / \mathcal{K}_1$ est isomorphe à $\psi_{*}(\mathcal{O}_{\mathfrak{Y}} / \mathcal{K})$, ce qui prouve que 3 est isomorphe à un sous-préschéma fermé de $\mathfrak{X}$.

Pour démontrer (ii), il est immédiat qu'on peut se limiter au cas où $\mathfrak{S}=\mathrm{Spf}(A)$, $\mathfrak{X}=\mathrm{Spf}(B)$, $\mathfrak{Y}=\mathrm{Spf}(C)$, A étant un anneau $\mathfrak{J}$-adique noethérien, $B=A/a$, où $a$ est un idéal de A, C une A-algèbre topologique adique et noethérienne. Tout revient à prouver que l'homomorphisme $C\to C\widehat{\otimes}_{A}(A/a)$ est surjectif : or, A/a est un A-module de type fini, et sa topologie est la topologie $\mathfrak{J}$-adique ; il résulte alors de (0, 7.7.8) que $C\widehat{\otimes}_{A}(A/a)$ s'identifie à $C\otimes_{A}(A/a)=C/aC$, d'où notre assertion.

Corollaire (10.14.6). — Sous les hypothèses de (10.14.5, (ii)), soient $p: \mathfrak{X} \times_{\mathfrak{S}} \mathfrak{Y} \to \mathfrak{X}$, $q: \mathfrak{X} \times_{\mathfrak{S}} \mathfrak{Y} \to \mathfrak{Y}$ les projections, de sorte que le diagramme

![](images/page_29_image_6.jpg)

est commutatif. Pour tout $\mathcal{O}_{\mathfrak{x}}$-Module cohérent $\mathcal{F}$, on a alors un isomorphisme canonique de $\mathcal{O}_{\mathfrak{y}}$-Modules

$$
u: g ^ {*} (f _ {*} (\mathcal {F})) \stackrel {{\sim}} {{\to}} q _ {*} (p ^ {*} (\mathcal {F})).\tag{10.14.6.1}
$$

Pour définir un homomorphisme $g^{*}(f_{*}(\mathcal{F})) \to q_{*}(p^{*}(\mathcal{F}))$, on sait qu'il revient au même de définir un homomorphisme $f_{*}(\mathcal{F}) \to g_{*}(q_{*}(p^{*}(\mathcal{F}))) = f_{*}(p_{*}(p^{*}(\mathcal{F})))$ (0, 4.4.3): nous prendrons $u = f_{*}(\rho)$, où $\rho$ est l'homomorphisme canonique $\mathcal{F} \to p_{*}(p^{*}(\mathcal{F}))$ (0, 4.4.3). Pour voir que $u$ est un isomorphisme, on se ramène aussitôt au cas où $\mathfrak{S}, \mathfrak{X}, \mathfrak{Y}$ sont des spectres formels d'anneaux adiques noethériens A, B, C, avec les conditions vues ci-dessus dans (10.14.5, (ii)); on a alors $\mathcal{F} = \mathrm{M}^{\Delta}$, où M est un (A/a)-module de type fini (10.10.5), et les deux membres de (10.14.6.1) s'identifient respectivement, en vertu de (10.10.8), à $(\mathrm{C} \otimes_{\mathrm{A}} \mathrm{M})^{\Delta}$ et à $((\mathrm{C}/\mathfrak{a}\mathrm{C}) \otimes_{\mathrm{A}/\mathfrak{a}} \mathrm{M})^{\Delta}$, d'où le corollaire, puisque $(\mathrm{C}/\mathfrak{a}\mathrm{C}) \otimes_{\mathrm{A}/\mathfrak{a}} \mathrm{M} = (\mathrm{C} \otimes_{\mathrm{A}} (\mathrm{A}/\mathfrak{a})) \otimes_{\mathrm{A}/\mathfrak{a}} \mathrm{M}$ s'identifie canoniquement à $\mathrm{C} \otimes_{\mathrm{A}} \mathrm{M}$.

Corollaire (10.14.7). — Soient X un préschéma usuel localement noethérien, Y un sous-préschéma fermé de X, j l'injection canonique Y→X, X' une partie fermée de X et Y'=Y∩X'; alors  $\hat{j}:Y_{/Y'}\to X_{/X'}$  est une immersion fermée, et pour tout O$_{Y}$-Module cohérent F, on a

$$
\hat {j} _ {*} (\mathcal {F} _ {/ \mathrm{Y} ^ {\prime}}) = (j _ {*} (\mathcal {F})) _ {/ \mathrm{X} ^ {\prime}}.
$$

Comme  $Y' = j^{-1}(X')$ , il suffit d'utiliser (10.9.9) et d'appliquer (10.14.5) et (10.14.6).

## 10.15. Préschémas formels séparés.

Définition (10.15.1). — Soient S un préschéma formel, X un S-préschéma formel,  $f: X \to S$  le morphisme structural. On appelle morphisme diagonal  $\Delta_{X|S}: X \to X \times_{S} X$  (noté aussi  $\Delta_{X}$ ) le morphisme  $(\mathrm{I}_{\mathfrak{X}}, \mathrm{I}_{\mathfrak{X}})_{\mathfrak{S}}$ . On dit que X est séparé sur S, ou un S-schéma formel, ou que f est un morphisme séparé, si l'image par  $\Delta_{X}$  de l'espace sous-jacent X est une partie fermée de l'espace sous-jacent à  $X \times_{S} X$ . On dit qu'un préschéma formel X est séparé, ou est un schéma formel, s'il est séparé sur Z.

Proposition (10.15.2). — Supposons que les préschémas formels S, X soient respectivement limites inductives de suites  $(\mathbf{S}_{n})$ ,  $(\mathbf{X}_{n})$  de préschémas usuels, et que le morphisme  $f: X \to S$  soit limite inductive d'une suite de morphismes  $f_{n}: X_{n} \to S_{n}$ . Pour que f soit séparé, il faut et il suffit que le morphisme  $f_{0}: X_{0} \to S_{0}$  le soit.

En effet, $\Delta_{\mathfrak{X}|\mathfrak{S}}$ est alors limite inductive de la suite de morphismes $\Delta_{\mathrm{X}_{n}|\mathrm{S}_{n}}$ (10.7.4), et l'image par $\Delta_{\mathfrak{X}|\mathfrak{S}}$ de l'espace sous-jacent $\mathfrak{X}$ (resp. l'espace sous-jacent $\mathfrak{X}\times_{\mathfrak{S}}\mathfrak{X}$) est identique à l'image par $\Delta_{\mathrm{X}_{0}|\mathrm{S}_{0}}$ de l'espace sous-jacent $\mathrm{X}_{0}$ (resp. à l'espace sous-jacent $\mathrm{X}_{0}\times_{\mathrm{S}_{0}}\mathrm{X}_{0}$); d'où la conclusion.

Proposition (10.15.3). — On suppose dans ce qui suit que tous les préschémas formels (resp. morphismes de préschémas formels) considérés soient limites inductives de suites de préschémas usuels (resp. de morphismes de préschémas usuels).

(i) Le composé de deux morphismes séparés est séparé.

(ii) Si $f: \mathfrak{X} \to \mathfrak{X}', g: \mathfrak{Y} \to \mathfrak{Y}'$ sont deux $\mathfrak{S}$-morphisms séparés, $f \times_{\mathfrak{S}} g$ est séparé.

(iii) Si $f: \mathfrak{X} \to \mathfrak{Y}$ est un $\mathfrak{S}$-morphisme séparé, le $\mathfrak{S}'$-morphisme $f_{(\mathfrak{S}')}$ est séparé pour toute extension $\mathfrak{S}' \to \mathfrak{S}$ du préschéma formel de base.

(iv) Si le composé gof de deux morphismes est séparé, f est séparé.

(On sous-entend dans cet énoncé que si un même préschéma formel 3 intervient plusieurs fois dans une même proposition, on le considère comme limite inductive de la même suite ( $Z_{n}$ ) de préschémas usuels partout où il figure, et les morphismes de 3 dans un préschéma formel (resp. d'un préschéma formel dans 3) comme limites inductives de morphismes des  $Z_{n}$  dans des préschémas usuels (resp. de préschémas usuels dans les  $Z_{n}$ )).

Avec les notations de (10.15.2), on a en effet $(g_0f)_0 = g_0\circ f_0$, et $(f\times_{\mathfrak{S}}g)_0 = f_0\times_{\mathbb{S}_0}g_0$; les assertions de (10.15.3) sont alors conséquences immédiates de (10.15.2) et des assertions correspondantes de (5.5.1) pour les préschémas usuels.

Nous laissons au lecteur le soin d'énoncer pour la même espèce de préschémas formels et de morphismes que dans (10.15.3) les propositions correspondant à (5.5.5),

(5.5.9) et (5.5.10) (en y remplaçant « ouvert affine » par « ouvert formel affine vérifiant la condition b) de (10.6.3) »).

Un raisonnement analogue montre aussi que tout schéma formel affine noethérien est séparé, ce qui justifie la terminologie.

Proposition (10.15.4). — Soient S un préschéma formel localement noethérien, X, Y deux S-préschémas formels localement noethériens, tels que X ou Y soit de type fini sur S (de sorte que  $X \times_{S} Y$  est localement noethérien) et que Y soit séparé sur S. Soit f :  $X \to Y$  un S-morphisme ; alors le morphisme graphe  $\Gamma_{f} = (\mathrm{I}_{\mathfrak{X}}, f)_{\mathfrak{S}} : \mathfrak{X} \to \mathfrak{X} \times_{\mathfrak{S}} \mathfrak{Y}$  est une immersion fermée.

On peut supposer que $\mathfrak{S}$ est limite inductive d'une suite $(\mathrm{S}_n)$ de préschémas localement noethériens, $\mathfrak{X}$ (resp. $\mathfrak{Y}$) limite inductive d'une suite $(\mathrm{X}_n)$ (resp. $(\mathrm{Y}_n)$) de $\mathrm{S}_n$-préschémas, $f$ limite inductive d'une suite de $\mathrm{S}_n$-morphismes $f_n: \mathrm{X}_n \to \mathrm{Y}_n$; alors $\mathfrak{X} \times_{\mathfrak{S}} \mathfrak{Y}$ est limite inductive de la suite $(\mathrm{X}_n \times_{\mathrm{S}_n} \mathrm{Y}_n)$ et $\Gamma_f$ de la suite $(\Gamma_{f_n})$ (10.7.4); par hypothèse, $\mathrm{Y}_0$ est séparé sur $\mathrm{S}_0$ (10.15.2), donc l'espace $\Gamma_{f_0}(\mathrm{X}_0)$ est un sous-espace fermé de $\mathrm{X}_0 \times_{\mathrm{S}_0} \mathrm{Y}_0$; comme les espaces sous-jacents de $\mathfrak{X} \times_{\mathfrak{S}} \mathfrak{Y}$ (resp. $\Gamma_f(\mathfrak{X})$) et $\mathrm{X}_0 \times_{\mathrm{S}_0} \mathrm{Y}_0$ (resp. $\Gamma_{f_0}(\mathrm{X}_0)$) sont les mêmes, on voit déjà que $\Gamma_f(\mathfrak{X})$ est un sous-espace fermé de $\mathfrak{X} \times_{\mathfrak{S}} \mathfrak{Y}$. Remarquons maintenant que lorsque (U, V) parcourt l'ensemble des couples formés d'un ouvert formel affine noethérien U (resp. V) de $\mathfrak{X}$ (resp. Y) tels que $f(\mathrm{U}) \subset \mathrm{V}$, les ouverts $\mathrm{U} \times_{\mathrm{S}} \mathrm{V}$ forment un recouvrement de $\Gamma_f(\mathfrak{X})$ dans $\mathfrak{X} \times_{\mathfrak{S}} \mathfrak{Y}$, et si $f_{\mathrm{U}}: \mathrm{U} \to \mathrm{V}$ est la restriction de $f$ à U, $\Gamma_{f_v}: \mathrm{U} \to \mathrm{U} \times_{\mathfrak{S}} \mathrm{V}$ est la restriction de $\Gamma_f$ à U. Si nous montrons que $\Gamma_{f_u}$ est une immersion fermée, il en sera donc de même de $\Gamma_f$ (10.14.4), autrement dit, on est ramené au cas où $\mathfrak{S} = \operatorname{Spf}(\mathrm{A})$, $\mathfrak{X} = \operatorname{Spf}(\mathrm{B})$, $\mathfrak{Y} = \operatorname{Spf}(\mathrm{C})$ sont affines (A, B, C adiques noethériens), $f$ correspondant à un A-homomorphisme continu $\varphi: \mathrm{C} \to \mathrm{B}$; $\Gamma_f$ correspond alors à l'unique homomorphisme continu $\omega: \mathrm{B}^{\widehat{\otimes}}_{\mathrm{A}}\mathrm{C} \to \mathrm{B}$ qui, composé avec les homomorphismes canoniques $\mathrm{B} \to \mathrm{B}^{\widehat{\otimes}}_{\mathrm{A}}\mathrm{C}$ et $\mathrm{C} \to \mathrm{B}^{\widehat{\otimes}}_{\mathrm{A}}\mathrm{C}$, donne respectivement l'identité et $\varphi$. Or, il est clair que $\omega$ est surjectif, d'où notre assertion.

Corollaire (10.15.5). — Soient S un préschéma formel localement noethérien, X un S-préschéma de type fini; pour que X soit séparé sur S, il faut et il suffit que le morphisme diagonal $\mathfrak{X} \to \mathfrak{X} \times_{\mathfrak{S}} \mathfrak{X}$ soit une immersion fermée.

Proposition (10.15.6). — Une immersion fermée $j: \mathfrak{Y} \to \mathfrak{X}$ de préschémas formels localement noethériens est un morphisme séparé.

Avec les notations de (10.14.2), $j_0: \mathrm{Y}_0 \to \mathrm{X}_0$ est une immersion fermée, donc un morphisme séparé, et il suffit d'appliquer (10.15.2).

Proposition (10.15.7). — Soient X un préschéma (usuel) localement noethérien, X' une partie fermée de X et $\hat{\mathbf{X}} = \mathbf{X}_{/X'}$. Pour que $\hat{\mathbf{X}}$ soit séparé, il faut et il suffit que $\hat{\mathbf{X}}_{\text{red}}$ le soit, et il suffit que X le soit.

En effet, avec les notations de (10.8.5), pour que $\hat{\mathbf{X}}$ soit séparé, il faut et il suffit que $\mathbf{X}_{0}^{\prime}$ le soit (10.15.2), et comme $\hat{\mathbf{X}}_{\mathrm{red}} = (\mathbf{X}_{0}^{\prime})_{\mathrm{red}}$, il est équivalent de dire que $\hat{\mathbf{X}}_{\mathrm{red}}$ l'est (5.5.1, (vi)).

## BIBLIOGRAPHIE

[1] H. CARTAN et C. CHEVALLEY, Séminaire de l'École Normale Supérieure, 8$^{e}$ année (1955-56), Géométrie algébrique.

[2] H. CARTAN and S. EILENBERG, Homological Algebra, Princeton Math. Series (Princeton University Press), 1956.

[3] W. L. Chow and J. IGUSA, Cohomology theory of varieties over rings, Proc. Nat. Acad. Sci. U.S.A., t. XLIV (1958), p. 1244-1248.

[4] R. GODEMENT, Théorie des faisceaux, Actual. Scient. et Ind., n° 1252, Paris (Hermann), 1958.

[5] H. GRAUERT, Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen, Publ. Math. Inst. Hautes Études Scient., n° 5, 1960.

[6] A. GROTHENDIECK, Sur quelques points d'algèbre homologique, Tôhoku Math. Journ., t. IX (1957), p. 119-221.

[7] A. GROTHENDIECK, Cohomology theory of abstract algebraic varieties, Proc. Intern. Congress of Math., p. 103-118, Edinburgh (1958).

[8] A. GROTHENDIECK, Géométrie formelle et géométrie algébrique, Séminaire Bourbaki, 11 $^{e}$ année (1958-59), exposé 182.

[9] M. NAGATA, A general theory of algebraic geometry over Dedekind domains, Amer. Math. Journ.: I, t. LXXVIII, p. 78-116 (1956); II, t. LXXX, p. 382-420 (1958).

[10] D. G. Northcott, Ideal theory, Cambridge Univ. Press, 1953.

[11] P. SAMUEL, Commutative algebra (Notes by D. Herzig), Cornell Univ., 1953.

[12] P. SAMUEL, Algèbre locale, Mém. Sci. Math., n° 123, Paris, 1953.

[13] P. SAMUEL and O. ZARISKI, Commutative algebra, 2 vol., New York (Van Nostrand), 1958-60.

[14] J.-P. SERRE, Faisceaux algébriques cohérents, Ann. of Math., t. LXI (1955), p. 197-278.

[15] J.-P. SERRE, Sur la cohomologie des variétés algébriques, Journ. de Math. (9), t. XXXVI (1957), p. 1-16.

[16] J.-P. SERRE, Géométrie algébrique et géométrie analytique, Ann. Inst. Fourier, t. VI (1955-56), p. 1-42.

[17] J.-P. SERRE, Sur la dimension homologique des anneaux et des modules noethériens, Proc. Intern. Symp. on Alg. Number theory, p. 176-189, Tokyo-Nikko, 1955.

[18] A. WEIL, Foundations of algebraic geometry, Amer. Math. Soc. Coll. Publ., n° 29, 1946.

[19] A. WEIL, Numbers of solutions of equations in finite fields, Bull. Amer. Math. Soc., t. LV (1949), p. 497-508.

[20] O. ZARISKI, Theory and applications of holomorphic functions on algebraic varieties over arbitrary ground fields, Mem. Amer. Math. Soc., n° 5 (1951).

[21] O. ZARISKI, A new proof of Hilbert's Nullstellensatz, Bull. Amer. Math. Soc., t. LIII (1947), p. 362-368.

[22] E. KÄHLER, Geometria Arithmetica, Ann. di Mat. (4), t. XLV (1958), p. 1-368.

## INDEX DES NOTATIONS

$\mathbf{M}[\varphi]$ (M B-module, $\varphi : A \to B$ homomorphisme d'anneaux) : 0, 1.0.2.

B $\mathfrak{J}$, $\mathfrak{JB}$ ( $\mathfrak{J}$ idéal d'un anneau A dont un homomorphisme dans B est donné): 0, i.o.3.

r(a) (a idéal) : 0, i.i.i.

$\Re(\mathbf{A})$  (A anneau) : 0, i.1.2.

$S_{f}$  (f élément d'un anneau commutatif A) : 0, 1.2.1.

$\mathrm{S}^{-1}\mathrm{A}, \mathrm{S}^{-1}\mathrm{M}, m/s, i_{\mathrm{A}}^{\mathrm{S}}, i_{\mathrm{M}}^{\mathrm{S}}, i^{\mathrm{S}}$ (A anneau, M A-module, S partie multiplicative de A): 0, 1.2.2.

$A_{f}, M_{f}, A_{p}, M_{p}$  (M A-module,  $f \in A$ , p idéal premier de A): 0, 1.2.3.

$S^{-1}u$  (u homomorphisme de A-modules, S partie multiplicative de A) : 0, 1.3.1.

$\rho_{\mathbf{A}}^{\mathrm{T},\mathrm{S}}, \rho_{\mathbf{M}}^{\mathrm{T},\mathrm{S}}, \rho^{\mathrm{T},\mathrm{S}}$ (M A-module, S, T parties multiplicatives de A) : 0, I.4.I.

Supp(M) (M A-module) : 0, 1.7.1.

$\mathcal{F}|\mathrm{U},u|\mathrm{U}$ (F faisceau sur $\mathbf{X}$, $u$ morphisme de faisceaux sur $\mathbf{X}$, U ouvert de $\mathbf{X}) : \mathbf{0},3,1,5$.

$\mathcal{F}_x, s_x, \Gamma(\mathrm{U}, \mathcal{F}), u(s), \operatorname{Supp}(\mathcal{F})$ ($\mathcal{F}$ faisceau d'ensembles sur X, $x$ point de X, U ouvert de X, $s$ élément de $\Gamma(\mathrm{U}, \mathcal{F})$,

u homomorphisme de faisceaux sur X) : 0, 3.1.6.

$\psi_{*}(\mathcal{F})$ ( $\mathcal{F}$ faisceau sur $\mathbf{X},\psi :\mathbf{X}\to \mathbf{Y}$ application continue):0,3.4.1.

$\psi_{*}(u)$ ( $u$ homomorphisme de faisceaux sur $\mathbf{X}$): $\mathbf{0}$, 3.4.2.

$$
\psi_ {x}: \mathbf {0}, 3. 4. 4.
$$

$\mathcal{G} \to \mathcal{F}$ ($\mathcal{F}$ faisceau sur X, $\mathcal{G}$ faisceau sur Y): 0, 3.5.1.

$$
u ^ {\sharp}, v ^ {b}, \rho_ {\mathcal {G}}: \mathbf {0}, 3 \cdot 5 \cdot 3.
$$

$$
\psi^ {*} (\mathcal {G}), \psi^ {*} (v), \sigma_ {\mathcal {F}}: 0, 3. 5. 5.
$$

$\mathcal{O}_{\mathrm{X}}, \mathcal{O}_{\mathrm{X},x}, \mathcal{O}_{x}, \text{I, } e \ (\mathrm{X} \ \text{espace annelé)} : \mathbf{0}, 4.1.1.$

$$
\check {\mathcal {F}}, \bigwedge^ {p} \mathcal {F} (\mathcal {F} \circ_ {\mathrm{X}} \text {-Module}): \mathbf {0}, 4. 1. 4.
$$

$\mathcal{J}\mathcal{F}$ ( $\mathcal{J}$ faisceau d'idéaux de $\mathcal{O}_{\mathrm{X}}$, $\mathcal{F}\mathcal{O}_{\mathrm{X}}$-Module) : 0, 4.1.5.

$\Psi^{*}(\mathcal{C})$ ($\mathcal{C}$$\mathcal{O}_{\mathrm{Y}}$-Algèbre): 0, 4.3.4.

$\Psi^{*}(\mathcal{G}), \Psi^{*}(v) (\mathcal{G} \mathcal{O}_{\mathrm{Y}}\text{-Module}, v \text{ homomorphisme de } \mathcal{O}_{\mathrm{Y}}\text{-Modules}) : \mathbf{0}, 4.3.1.$

$\Psi_{*}^{\prime}(\mathcal{F}), \Psi_{*}^{\prime}(u) (\mathcal{F} \mathcal{O}_{X}\text{-Module}, u \text{ homomorphisme de } \mathcal{O}_{X}\text{-Modules}) : 0, 4.2.1.$

$\Psi^{*}(\mathfrak{I})\mathcal{O}_{\mathrm{X}}, \mathfrak{I}\mathcal{O}_{\mathrm{X}} (\mathfrak{I} \text{ Idéal de } \mathcal{O}_{\mathrm{Y}}) : \mathbf{0}, 4.3.5.$

$\Psi_{*}(\mathcal{C})$ ($\mathcal{C}$$\mathcal{O}_{\mathbf{X}}$-Algèbre): 0, 4.2.4.

$\mathcal{G} \to \mathcal{F}$ ($\mathcal{F} \circ_{\mathrm{X}}$-Module, $\mathcal{G} \circ_{\mathrm{Y}}$-Module): 0, 4.4.1.

$$
u _ {0} ^ {\sharp}, u ^ {\sharp}, v _ {0} ^ {\flat}, v ^ {\flat}, \rho_ {\mathcal {G}}, \sigma_ {\mathcal {F}}: 0, 4 \cdot 4 \cdot 3.
$$

$u_{1}\otimes u_{2}$$(u_{1},u_{2}$ homomorphismes de $\mathcal{O}_{\mathrm{Y}}$ -Modules dans des $\mathcal{O}_{\mathrm{X}}$ -Modules):0,4.4.4.

$$
\mathscr {L} ^ {- 1} \left(\mathscr {L} \circ_ {\mathrm{X}} \right.
$$

$$
\mathbf {0}, 5 \cdot 4 \cdot 3 \cdot
$$

$$
\mathscr {L} ^ {\otimes n} \left(\mathscr {L} \circ_ {\mathrm{X}} \text {-Module   invertible}\right): \mathbf {0}, 5 \cdot 4 \cdot 4.
$$

$\Gamma_{*}(\mathcal{L}),\Gamma_{*}(\mathcal{L},\mathcal{F})$ ($\mathcal{L}\circ_{\mathrm{X}}$-Module invertible, $\mathcal{F}\circ_{\mathrm{X}}$-Module): 0, 5.4.6.

$$
\mathcal {O} _ {\mathrm{X}} ^ {*}: \mathbf {0}, 5. 4. 7.
$$

$m_{x}, \boldsymbol{k}(x), f(x) : 0, 5.5.1.$

$$
\mathbf {X} _ {f}: \mathbf {0}, 5. 5. 2.
$$

$\operatorname{Im}(\mathbf{M}' \otimes_{\mathbf{A}} \mathbf{N}')$ ($\mathbf{M}'$, $\mathbf{N}'$ sous-A-modules de $\mathbf{M}$, $\mathbf{N}$): $\mathbf{0}$, 6.o.

$\widehat{\mathbf{A}}, \widehat{\mathbf{M}} : \mathbf{0}, 7.2.3 \text{ et } 7.3.1.$

$\mathrm{A}\left\{\mathrm{T}_{1},\dots ,\mathrm{T}_{r}\right\} :\mathbf{0},7.5.\mathrm{I}.$

A $\{S^{-1}\}$ : 0, 7.6.1.

$a\left\{S^{-1}\right\}$  (a idéal ouvert de A) : 0, 7.6.9.

$$
\mathrm{A} _ {\{f \}}, \mathrm{a} _ {\{f \}}: 0, 7. 6. 1 4.
$$

$$
\mathrm{A} _ {\{\mathrm{S} \}}: \mathbf {0}, 7. 6. 1 4.
$$

$$
(\mathbf {M} \widehat {\otimes} _ {\mathrm{A}} \mathbf {N}) ^ {\wedge}, \mathbf {M} \widehat {\otimes} _ {\mathrm{A}} \mathbf {N}: \mathbf {0}, 7. 7. \mathrm{i}.
$$

$$
u \widehat {\otimes} v: 0, 7. 7. 3.
$$

$\operatorname{Spec}(\mathbf{A}), \mathrm{i}_x, \mathfrak{m}_x, \boldsymbol{k}(x), f(x), \mathbf{M}_x, \mathrm{r}(\mathrm{E}), \mathrm{V}(\mathrm{E}), \mathrm{V}(f), \mathrm{D}(f) (\text{A anneau}, \text{M A-module}, f \in \mathbf{A}, \text{E} \subset \mathbf{A}, x \in \operatorname{Spec}(\mathbf{A})) : \mathbf{I}, \text{I.I.I.}$$\mathrm{i}(\mathrm{Y}) (\mathrm{Y} \subset \operatorname{Spec}(\mathrm{A})) : \mathbf{I}, \text{I.I.3.}$

$^{a}\varphi$  ( $\varphi$  homomorphisme d'anneaux): I, 1.2.1.

$S_{f}^{\prime}$  (f élément d'un anneau): I, I.3.I.

$\rho_{g,f}(f,g\text{ éléments d'un anneau}):\mathbf{I},\mathrm{I}.3.3.$

$\mathbf{A}, \mathbf{M}, \theta_f$ (A anneau, $f \in \mathbf{A}$, M A-module) : $\mathbf{I}$, 1.3.4.

$\widetilde{u}$ (u homomorphisme de A-modules): I, 1.3.5.

$\widetilde{\varphi}$ ($\varphi$ homomorphisme d'anneaux): $\mathbf{I}$, i.6.i.

A(X) (X schéma affine) : I, 1.7.1.

$\mathcal{O}_{\mathrm{X/Y}}$ (X préschéma) : I, 2.1.6.

Hom(X, Y) (X, Y préschémas) : I, 2.2.1.

$\text{Hom}_{\mathbb{S}}(\mathbf{X}, \mathbf{Y}), \text{i}_{\mathbf{X}}(\mathbf{X}, \mathbf{Y} \text{ S-préschémas}) : \mathbf{I}, 2.5.2.$

$\Gamma(\mathbf{X}/\mathbf{S})$ (S préschéma, X S-préschéma) : I, 2.5.5.

XIIY (X, Y préschémas) : I, 3.1.1.

$\mathbf{X} \times_{\mathbb{S}} \mathbf{Y}, \mathbf{X} \times \mathbf{Y}, (g, h)_{\mathbb{S}}, u \times_{\mathbb{S}} v, u \times v$ ($\mathbf{X}, \mathbf{Y}$ S-préschémas, $g, h, u, v$ S-morphismes): $\mathbf{I}, 3.2.1$.

$X \times _{A} Y, X \otimes _{A} B (g, h)_{A}, u \times _{A} v (X, Y A-préschémas (A anneau), B A-algèbre, g, h, u, v A-morphismes) : I, 3.2.1.$$X = (X S' S préschémas) : I a a 6.$

$X_{(S')}$  (X, S' S-préschémas) : I, 3.3.6.

$f_{(\mathbf{S}^{\prime})}^{(N)}(\mathbf{S}^{\prime}\mathbf{S}\text{-préschéma}, f\mathbf{S}\text{-morphisme}) : \mathbf{I}, 3.3.7.$

$\Gamma_{f}(f\mathbf{S}\text{-morphisme}):\mathbf{I},3.3.14.$

X(T) (X, T préschémas) : I, 3.4.1.

$\mathbf{P} \times_{\mathbb{R}} \mathbf{Q}$ (P, Q, ensembles sur R): I, 3.4.2.

$\mathbf{X}(\mathbf{T})_{\mathbf{S}}(\mathbf{X},\mathbf{T}\mathbf{S}\text{-préschémas)}:\mathbf{I},3.4.3.$

$\mathrm{X(B), X(B)_{A} (X A-préschéma, B A-algèbre)} : I, 3.4.4.$

$\mathbf{X}\otimes_{\mathrm{Y}}\mathbf{B},\mathbf{X}\otimes_{\mathcal{O}_{\mathrm{V}}}\mathbf{B}$ (B $\mathcal{O}_{y}$-algèbre, où $y\in \mathbf{Y}$): $\mathbf{I},3.6.3$.

$Z \leqslant Y$ (Y, Z sous-préschémas d'un préschéma) : I, 4.1.10.

$f^{-1}(\mathbf{Y})$ ( $f$ morphisme, $\mathbf{Y}$ sous-préschéma): $\mathbf{I}, 4.4.1$.

$\mathcal{N}_{\mathrm{X}}$ (X préschéma) : I, 5.1.1.

$X_{\text{red}}$ (X préschéma) : I, 5.1.3.

$f_{\mathrm{red}}$ ( $f$ morphisme): I, 5.1.5.

$\Delta_{\mathrm{X|S}}, \Delta_{\mathrm{X}}, \Delta (\mathrm{X S-préschéma}) : \mathbf{I}, 5.3.1.$

$rg_{K}(X)$  (K corps, X K-schéma fini) : I, 6.4.5.

$n(\mathbf{X})$ (X schéma fini sur un corps) : I, 6.4.8.

$\Gamma_{\mathrm{rat}}(\mathbf{X} / \mathbf{Y}):\mathbf{I},7.1.2.$

R(X) (X préschéma) : I, 7.1.3.

$\mathcal{R}(\mathbf{X})$  (X préschéma) : I, 7.3.1.

L(A) (A anneau intègre) : I, 8.1.2.

$\delta(f)$ ( $f$ application rationnelle): I, 8.2.1.

$\mathcal{F} \otimes_{\mathcal{O}_{\mathrm{S}} \mathcal{G}}, \mathcal{F} \otimes_{\mathrm{S}} \mathcal{G}$ ($\mathcal{F}, \mathcal{G}$ Modules sur des S-préschémas): I, 9.1.2.

$\overline{\mathcal{G}}$ ($\mathcal{G}$$\mathcal{O}_{\mathrm{X}}$-Module): I, 9.4.1.

$\overline{Y}$  (Y sous-préschéma) : I, 9.5.11.

$\operatorname{Spf}(\mathbf{A}), \mathcal{O}_{\mathfrak{X}}$ (A anneau admissible, $\mathfrak{X} = \operatorname{Spf}(\mathbf{A})) : \mathbf{I}, 10.1.2.$

$\mathfrak{D}(f)$ ( $f$ élément d'un anneau admissible) : I, 10.1.4.

$^{a}\varphi,\widetilde{\varphi},(\varphi\ homomorphisme\ continu\ d'anneaux\ admissibles):\mathbf{I},10.2.1.$

$\mathfrak{I}^{\Delta}$ ( $\mathfrak{I}$ idéal de définition) : I, 10.3.1.

$\mathfrak{X} \times_{\mathfrak{S}} \mathfrak{Y}$ ($\mathfrak{X}, \mathfrak{Y}$ S-préschémas formels) : I, 10.7.3.

$\mathcal{F}_{/X^{\prime}}, \widehat{\mathcal{F}}, u_{/X^{\prime}}, \widehat{u}$ ($\mathcal{F} \circ_{X}$-Module, $u$ homomorphisme de $\mathcal{O}_X$-Modules, $X^{\prime}$ partie fermée de $X$): I, 10.8.4.

$\mathrm{X}_{/ \mathrm{X}^{\prime}}$, $\hat{\mathrm{X}}$ (X préschéma, $\mathrm{X}^{\prime}$ partie fermée de $\mathrm{X}$): $\mathbf{I}$, 10.8.5.

$\widehat{f}$ ( $f$ morphisme de préschémas): I, 10.9.1.

$M^{\Delta}, u^{\Delta}$  (M module sur un anneau adique A, u homomorphisme continu de A-modules): I, 10.10.1.

$\Delta_{\mathfrak{S}|\mathfrak{X}}, \Delta_{\mathfrak{X}} (\mathfrak{X} \mathfrak{S}$-préscHEMA formel) : I, 10.15.1.

## INDEX TERMINOLOGIQUE

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Adhérence d'un sous-préschéma : I, 9.5.11.
$\mathcal{O}_{X}$-Algèbre : 0, 4.1.3.
Anneau adique, — 3-adique : 0, 7.1.9.
Anneau admissible : 0, 7.1.2.
Anneau complet de fractions : 0, 7.6.5.
Anneau de fractions : 0, 1.2.2.
Anneau des fonctions rationnelles : I, 2.1.6 et 7.1.3.
Anneau d'un schéma affine : I, 1.7.1.
Anneau intègre : 0, 1.0.6.
Anneau linéairement topologisé : 0, 7.1.1.
Anneau local : 0, 1.0.7.
Anneau local dominant : I, 8.1.1.
Anneau local de X le long de Y, — — de Y dans X : I, 2.1.6.
Anneau préadique, — 3-préadique : 0, 7.1.9.
Anneau préadmissible : 0, 7.1.2.
Anneau réduit : 0, 1.1.1.
Anneau régulier : 0, 4.1.3.
Anneaux locaux apparentés : I, 8.1.4.
Annulateur d'un $\mathcal{O}_{X}$-Module : 0, 5.3.7.
Application de spectres d'anneaux associée à un homomorphisme d'anneaux : I, 1.2.1.
Application rationnelle, S-application rationnelle : I, 7.1.2.
Application rationnelle définie en un point : I, 7.2.1.
Application rationnelle induite sur un ouvert : I, 7.1.2.
Application rationnelle induite sur $\text{Spec}(\mathcal{O}_{x})$ : I, 7.2.8.

Cohérent ($\mathcal{O}_{X}$-Module) : 0, 5.3.1.
Cohérente ($\mathcal{O}_{X}$-Algèbre) : 0, 5.3.6.
Complété d'un $\mathcal{O}_{X}$-Module, d'un homomorphisme de $\mathcal{O}_{X}$-Modules le long d'une partie fermée : I, 10.8.4.
Complété d'un préschéma le long d'une partie fermée : I, 10.8.5.
Composante irréductible : 0, 2.1.5.
Composé d'un $\psi$-morphisme et d'un $\psi'$-morphisme : 0, 3.5.2.
Composé d'un $\Psi'$-morphisme et d'un $\Psi'$-morphisme : 0, 4.4.2.
Condition de recollement : 0, 3.3.1 et 4.1.6.
Corps de base d'un préschéma algébrique : I, 6.4.1.
Corps des valeurs d'un point géométrique : I, 3.4.5.

Diagonale de X$\times_{S}$X : I, 5.3.9.
Di-homomorphisme : 0, 1.0.2.
Domaine de définition d'une application rationnelle : I, 7.2.1.
Dual d'un $\mathcal{O}_{X}$-Module : 0, 4.1.4.

Élément topologiquement nilpotent : 0, 7.1.1.
Engendré par une famille de sections ($\mathcal{O}_{X}$-Module) : 0, 5.1.2.
Ensemble où s'annule une section : 0, 5.5.1.
Entière, entière finie (algèbre) : 0, 1.0.5.
Espace annelé : 0, 4.1.1.
</div>

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Espace annelé en anneaux locaux : 0, 5.5.1.
Espace annelé induit sur un ouvert : 0, 4.1.2.
Espace annelé normal, — réduit, — régulier : 0, 4.1.3.
Espace annelé obtenu par recollement : 0, 4.1.6.
Espace de Kolmogoroff : 0, 2.1.2.
Espace irréductible : 0, 2.1.1.
Espace noethérien : 0, 2.2.1.
Espace quasi-compact : 0, 2.2.4.
Espace sous-jacent à un espace annelé : 0, 4.1.1.
Espace topologiquement annelé : 0, 4.1.1.

Faisceau algébrique sur un espace annelé : 0, 4.1.3.
Faisceau associé à un préfaisceau : 0, 3.5.7.
Faisceau associé à un A-module sur Spec(A) : I, 1.3.4.
Faisceau à valeurs dans une catégorie : 0, 3.1.1.
Faisceau cohérent d'anneaux : 0, 5.3.5.
Faisceau d'anneaux normal en un point, — normal, — réduit en un point, — réduit, — régulier en un point, — régulier : 0, 4.1.3.
Faisceau d'anneaux gradués : 0, 4.1.3.
Faisceau des fonctions rationnelles : I, 7.3.1.
Faisceau de torsion : I, 7.4.1.
Faisceau d'idéaux : 0, 4.1.3.
Faisceau d'idéaux de définition : I, 10.3.3 et 10.5.1.
Faisceau induit : 0, 3.7.1.
Faisceau localement simple : 0, 3.6.1.
Faisceau obtenu par recollement : 0, 3.3.1.
Faisceau pseudo-discret : 0, 3.8.1.
Faisceau simple : 0, 3.6.1.
Faisceau structural d'un espace annelé : 0, 4.1.1.
Faisceau structural d'un schéma affine : I, 1.3.4.
Faisceau sur une base d'ouverts : 0, 3.2.2.
Fibre d'un faisceau : 0, 3.1.6.
Fibre d'un morphisme de préschémas : I, 3.6.3.
Finie (algèbre) : 0, 1.0.5.
Fonction rationnelle : I, 7.1.2.

Générisation d'un point : 0, 2.1.2.
Gradué ($\mathcal{O}_{X}$-Module) : 0, 4.1.3.
Graphe d'un morphisme : I, 5.3.11.

Homomorphisme continu de faisceaux d'anneaux topologiques : 0, 3.1.4.
Homomorphisme défini par une section : 0, 5.1.1.
Homomorphisme local d'anneaux locaux : 0, 1.0.7.
$\varphi$-homomorphisme de modules : 0, 1.0.2.

Idéal de définition d'un anneau admissible : 0, 7.1.2.
$\mathcal{O}_{X}$-Idéal : 0, 4.1.3.
$\mathcal{O}_{\overline{x}}$-Idéal de définition d'un préschéma formel $\overline{x}$ : I, 10.3.3 et 10.5.1.
Idéal premier : 0, 1.0.6.
Image directe d'un $\mathcal{O}_{X}$-Module : 0, 4.2.1.
Image directe d'un préfaisceau : 0, 3.4.1.
Image d'une S-section : I, 5.3.11.
Image fermée d'un préschéma par un morphisme : I, 9.5.3.
Image réciproque d'un $\mathcal{O}_{Y}$-Module : 0, 4.3.1.
</div>

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Image réciproque d'un S-morphisme : I, 3.3.7.
Image réciproque d'un préfaisceau : 0, 3.5.3.
Image réciproque d'un S-préschéma : I, 3.3.6.
Image réciproque d'un sous-préschéma : I, 4.4.1.
Immersion, immersion fermée, immersion ouverte de préschémas : I, 4.2.1.
Immersion fermée de préschémas formels : I, 10.14.2.
Immersion locale de préschémas : I, 4.5.1.
Injection canonique d'un espace annelé induit sur un ouvert : 0, 4.1.2.
Injection canonique d'un sous-préschéma : I, 4.1.7.
Injection canonique d'un sous-préschéma formel : I, 10.14.2.
Injection géométrique : I, 3.5.4.
Inverse d'un $\mathcal{O}_{\mathrm{X}}$-Module inversible : 0, 5.4.3.
Inversible ($\mathcal{O}_{\mathrm{X}}$-Module) : 0, 5.4.1.
Isomorphisme associé à une immersion : I, 4.2.1.
Isomorphisme local de préschémas : I, 4.5.1.

Limite projective de $\mathcal{O}_{\mathrm{X}_{n}}$-Modules : I, 10.6.6.
Localement libre ($\mathcal{O}_{\mathrm{X}}$-Module) : 0, 5.4.1.
Localité d'un point à valeurs dans un anneau local : I, 3.4.5.

Module des fractions : 0, 1.2.2.
Module fidèlement plat : 0, 6.4.1.
Module plat : 0, 6.1.1.
Module A-plat : 0, 6.2.
Module quasi-fini : 0, 7.4.1.
$\mathcal{O}_{\mathrm{X}}$-Module : 0, 4.1.3.
Morphisme d'espaces annelés, d'espaces topologiquement annelés : 0, 4.1.1.
Morphisme fidèlement plat : 0, 6.7.8.
Morphisme plat : 0, 6.7.1.
Morphisme de préfaisceaux définis sur une base d'ouverts : 0, 3.2.3.
Morphisme de préschémas : I, 2.2.1.
Morphisme de S-préschémas, de A-préschémas : I, 2.5.2.
Morphisme birationnel : I, 6.5.6.
Morphisme de type fini : I, 6.3.1.
Morphisme diagonal : I, 5.3.1.
Morphisme dominant : I, 2.2.6.
Morphisme fermé : I, 2.2.6.
Morphisme graphe d'un morphisme : I, 3.3.14.
Morphisme localement de type fini : I, 6.6.2.
Morphisme majoré par un autre : I, 4.1.8.
Morphisme ouvert : I, 2.2.6.
Morphisme quasi-compact : I, 6.6.1.
Morphisme radiciel : I, 3.5.4.
Morphisme réduit : I, 5.1.5.
Morphisme séparé : I, 5.4.1.
Morphisme structural d'un S-préschéma : I, 2.5.1.
Morphisme surjectif : I, 2.2.6.
Morphisme universellement injectif : I, 3.5.4.
Morphismes équivalents : I, 7.1.1.
A-morphisme, S-morphisme de préschémas : I, 2.5.2.
Morphisme de préschémas formels : I, 10.4.5.
Morphisme adique de préschémas formels : I, 10.12.1.
Morphisme diagonal de préschémas formels : I, 10.15.1.
Morphisme de type fini de préschémas formels : I, 10.13.3.
</div>

```txt
Morphisme séparé de préschémas formels : I, 10.15.1.
Morphisme structural d'un S-préschéma formel : I, 10.4.7.
A-morphisme, S-morphisme de préschémas formels : I, 10.4.7.
ψ-morphisme de préfaisceaux : 0, 3.5.1.
Ψ-morphisme d'un O_Y-Module dans un O_X-Module : 0, 4.4.1.
Nilradical d'un anneau : 0, 1.1.1.
Nilradical d'une O_X-Algèbre : I, 5.1.1.
Nombre géométrique de points d'un préschéma : I, 6.4.8.
Ouvert affine : I, 2.1.1.
Ouvert formel affine, ouvert formel affine adique, ouvert formel affine noethérien : I, 10.4.1.
Partie multiplicative d'un anneau : 0, 1.2.1.
Partie multiplicative saturée : 0, 1.4.3.
f-plat (O_X-Module) : 0, 6.7.1.
Point d'un préschéma à valeurs dans un anneau : I, 3.4.4.
Point d'un préschéma à valeurs dans un préschéma : I, 3.4.1.
Point d'un A-préschéma à valeurs dans une A-algèbre : I, 3.4.4.
Point d'un S-préschéma au-dessus d'un point s∈S : I, 2.5.1.
Point d'un S-préschéma à valeurs dans un S-préschéma : I, 3.4.3.
Point fermé : 0, 2.2.6.
Point générique : 0, 2.1.2.
Point géométrique d'un préschéma : I, 3.4.5.
Point géométrique au-dessus de s : I, 3.4.5.
Point géométrique localisé en x : I, 3.4.5.
Point rationnel sur K : I, 3.4.5.
Préfaisceau constant : 0, 3.6.1.
Préfaisceau sur une base d'ouverts : 0, 3.2.1.
Préschéma : I, 2.1.2.
Préschéma artinien : I, 6.2.1.
Préschéma connexe : I, 2.1.7.
Préschéma de base : I, 2.5.1.
Préschéma déduit par réduction mod. J : I, 3.7.1.
Préschéma induit sur un ouvert : I, 2.1.8.
Préschéma intègre : I, 2.1.7.
Préschéma irréductible : I, 2.1.7.
Préschéma localement intègre : I, 2.1.7.
Préschéma localement noethérien : I, 6.1.1.
Préschéma réduit associé à un préschéma : I, 5.1.3.
A-préschéma, préschéma au-dessus de A : I, 2.5.1.
K-préschéma algébrique : I, 6.4.5.
S-préschéma, préschéma au-dessus de S : I, 2.5.1.
S-préschéma dominant : I, 2.5.1.
Préschéma de type fini au-dessus de S, S-préschéma de type fini : I, 6.3.1.
Préschéma obtenu par extension du préschéma de base : I, 3.3.6.
Préschéma séparé au-dessus de S : I, 5.4.1.
Préschéma formel : I, 10.4.2.
Préschéma formel adique : I, 10.4.2.
Préschéma formel localement noethérien : I, 10.4.2.
Préschéma formel noethérien : I, 10.4.2.
Préschéma formel au-dessus de A, A-préschéma formel : I, 10.4.7.
Préschéma formel au-dessus de S, S-préschéma formel : I, 10.4.7.
Préschéma formel de type fini sur S, S-préschéma formel de type fini : I, 10.13.3.
```

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Préschéma formel séparé sur S : I, 10.15.1.
Présentation finie (module ayant une) : 0, 1.0.5.
Présentation finie ($\mathcal{O}_{X}$-Module ayant une) : 0, 5.2.5.
Principe de récurrence noethérienne : 0, 2.2.2.
Produit de S-préschémas : I, 3.2.1.
Produit de $\mathfrak{S}$-préschémas formels : I, 10.7.1.
Produit fibré d'ensembles : I, 3.4.2.
Produit tensoriel de faisceaux sur des préschémas distincts : I, 9.1.2.
Produit tensoriel complété d'algèbres : 0, 7.7.5.
Produit tensoriel complété de modules : 0, 7.7.2.
Projections canoniques d'un produit : I, 3.2.1.
Prolongement canonique d'un sous-Module : I, 9.4.1.
Prolongement d'un morphisme aux complétés : I, 10.9.1.
Puissance extérieure p-ème d'un $\mathcal{O}_{X}$-Module : 0, 4.1.4.

Quasi-cohérent ($\mathcal{O}_{X}$-Module) : 0, 5.1.3.
Quasi-cohérente ($\mathcal{O}_{X}$-Algèbre) : 0, 5.1.3.

Racine d'un idéal : 0, 1.1.1.
Radical d'un anneau : 0, 1.1.2.
Rang d'un $\mathcal{O}_{X}$-Module localement libre : 0, 5.4.1.
Rang d'un $\mathcal{O}_{X}$-Module sans torsion : I, 7.4.2.
Rang d'un K-schéma fini : I, 6.4.5.
Rang séparable d'un K-schéma fini : I, 6.4.8.
Restriction d'un espace annelé à un ouvert : 0, 4.1.2.
Restriction d'un morphisme à un ouvert : 0, 4.1.2.
Restriction d'un morphisme de préschémas à un sous-préschéma : I, 4.1.7.
Restriction d'un préschéma à un ouvert : I, 2.1.8.
Restriction d'une application rationnelle à un ouvert : I, 7.1.2.

Schéma : I, 5.4.1.
Schéma affine : I, 1.7.1.
Schéma local, schéma local en un point d'un préschéma : I, 2.4.1.
K-schéma algébrique : I, 6.4.1.
Schéma fini sur K, K-schéma fini : I, 6.4.5.
S-schéma : I, 5.4.1.
Schéma formel affine : I, 10.1.2.
$\mathfrak{S}$-schéma formel : I, 10.15.1.
Sections d'un faisceau : 0, 3.1.6.
S-section d'un S-préschéma : I, 2.5.5 et 5.3.11.
S-section rationnelle d'un S-préschéma : I, 7.1.2.
Section unité de $\mathcal{O}_{X}$ : 0, 4.1.1.
Séries formelles restreintes : 0, 7.5.1.
Somme de préschémas : I, 3.6.1.
Sous-$\mathcal{O}_{X}$-Algèbre engendrée par un sous-Module : 0, 4.1.3.
Sous-préschéma : I, 4.1.3.
Sous-préschéma associé à une immersion : I, 4.2.1.
Sous-préschéma fermé : I, 4.1.3.
Sous-préschéma fermé défini par un faisceau d'idéaux : I, 4.1.2.
Sous-préschéma formel fermé : I, 10.14.2.
Spécialisation d'un point : 0, 2.1.2.
Spectre d'un anneau : I, 1.1.1.
Spectre formel d'un anneau admissible : I, 10.1.2.
Support d'un module : 0, 1.7.1.
</div>

Support d'un faisceau de groupes : 0, 3.1.6.

Système fondamental d'Idéaux de définition : I, 10.3.6 et 10.5.1.

Système inductif adique de préschémas : I, 10.12.2.

Topologie J-adique (1), topologie J-préadique : 0, 7.1.9 et 7.2.3.

Topologie spectrale : I, 1.1.2.

Trivial ( $O_{X}$ -Module invertible): I, 2.4.8.

Type fini ( $O_{X}$ -Module de): 0, 5.2.1.

Valeur d'une section en un point : 0, 5.5.1.

(1) Observons que notre terminologie s'écarte quelque peu des définitions usuelles : nous n'employons le terme « adique » que lorsqu'il s'agit d'anneaux ou modules séparés et complets.

## TABLE DES MATIÈRES

INTRODUCTION.... 5
CHAPITRE O. — Préliminaires.... 11
§ 1. Anneaux de fractions .... 11
1.0. Anneaux et algèbres .... 11
1.1. Racine d'un idéal. Nilradical et radical d'un anneau.... 12
1.2. Modules et anneaux de fractions .... 13
1.3. Propriétés fonctorielles .... 14
1.4. Changement de partie multiplicative .... 15
1.5. Changement d'anneau.... 17
1.6. Identification du module M$_{f}$ à une limite inductive .... 19
1.7. Support d'un module .... 20
§ 2. Espaces irréductibles. Espaces noethériens .... 21
2.1. Espaces irréductibles .... 21
2.2. Espaces noethériens .... 23
§ 3. Compléments sur les faisceaux .... 23
3.1. Faisceaux à valeurs dans une catégorie .... 23
3.2. Préfaisceaux sur une base d'ouverts .... 25
3.3. Recollement de faisceaux .... 28
3.4. Images directes de préfaisceaux .... 29
3.5. Images réciproques de préfaisceaux .... 30
3.6. Faisceaux simples et faisceaux localement simples .... 33
3.7. Images réciproques de préfaisceaux de groupes ou d'anneaux.. 34
3.8. Faisceaux d'espaces pseudo-discrets .... 35
§ 4. Espaces annelés.... 35
4.1. Espaces annelés, A-Modules, A-Algèbres .... 35
4.2. Image directe d'un A-Module .... 39
4.3. Image réciproque d'un A-Module.... 40
4.4. Relations entre images directes et images réciproques .... 42
§ 5. Faisceaux quasi-cohérents et faisceaux cohérents .... 44
5.1. Faisceaux quasi-cohérents .... 44
5.2. Faisceaux de type fini.... 45
5.3. Faisceaux cohérents .... 47
5.4. Faisceaux localement libres .... 48
5.5. Faisceaux sur un espace annelé en anneaux locaux .... 53

§ 6. Platitude....54
6.1. Modules plats....55
6.2. Changement d'anneaux....55
6.3. Localisation de la platitude....56
6.4. Modules fidèlement plats....57
6.5. Restriction des scalaires....58
6.6. Anneaux fidèlement plats....58
6.7. Morphismes plats d'espaces annelés....59
§ 7. Anneaux adiques....60
7.1. Anneaux admissibles....60
7.2. Anneaux adiques et limites projectives....62
7.3. Anneaux préadiques noethériens....66
7.4. Modules quasi-finis sur les anneaux locaux....68
7.5. Anneaux de séries formelles restreintes....69
7.6. Anneaux complets de fractions....72
7.7. Produits tensoriels complétés....75
7.8. Topologies sur les modules d'homomorphismes....77
APITRE PREMIER.—Le langage des schémas....79
§ 1. Schémas affines....80
1.1. Le spectre premier d'un anneau....80
1.2. Propriétés fonctorielles des spectres premiers d'anneaux....83
1.3. Faisceau associé à un module....84
1.4. Faisceaux quasi-cohérents sur un spectre premier....90
1.5. Faisceaux cohérents sur un spectre premier....92
1.6. Propriétés fonctorielles des faisceaux quasi-cohérents sur un spectre premier....93
1.7. Caractérisation des morphismes de schémas affines....96
§ 2. Préschémas et morphismes de préschémas....97
2.1. Définition des préschémas....97
2.2. Morphismes de préschémas....98
2.3. Recollement de préschémas....101
2.4. Schémas locaux....101
2.5. Préschémas au-dessus d'un préschéma....103
§ 3. Produit de préschémas....104
3.1. Somme de préschémas....104
3.2. Produit de préschémas....104
3.3. Propriétés formelles du produit ; changement de préschéma de base....108
3.4. Points d'un préschéma à valeurs dans un préschéma ; points géométriques....111
3.5. Surjections et injections....114
3.6. Fibres....117
3.7. Application : réduction d'un préschéma mod. J.....118
§ 4. Sous-préschémas et morphismes d'immersion....119
4.1. Sous-préschémas....119
4.2. Morphismes d'immersion....122

4.3. Produit d'immersions ..... 124
4.4. Image réciproque d'un préschéma ..... 125
4.5. Immersions locales et isomorphismes locaux ..... 126

§ 5. Préschémas réduits ; condition de séparation ..... 127
5.1. Préschémas réduits ..... 127
5.2. Existence d'un sous-préschéma d'espace sous-jacent donné... 131
5.3. Diagonale ; graphe d'un morphisme ..... 132
5.4. Morphismes et préschémas séparés ..... 135
5.5. Critères de séparation ..... 136

§ 6. Conditions de finitude..... 140
6.1. Préschémas noethériens et localement noethériens ..... 140
6.2. Préschémas artiniens ..... 143
6.3. Morphismes de type fini ..... 144
6.4. Préschémas algébriques ..... 147
6.5. Détermination locale d'un morphisme ..... 150
6.6. Morphismes quasi-compacts et morphismes localement de type fini..... 152

§ 7. Applications rationnelles ..... 155
7.1. Applications rationnelles et fonctions rationnelles ..... 155
7.2. Domaine de définition d'une application rationnelle ..... 158
7.3. Faisceau des fonctions rationnelles ..... 161
7.4. Faisceaux de torsion et faisceaux sans torsion..... 163

§ 8. Les schémas de Chevalley ..... 164
8.1. Anneaux locaux apparentés ..... 164
8.2. Anneaux locaux d'un schéma intègre ..... 165
8.3. Les schémas de Chevalley ..... 168

§ 9. Compléments sur les faisceaux quasi-cohérents ..... 169
9.1. Produit tensoriel de faisceaux quasi-cohérents ..... 169
9.2. Image directe d'un faisceau quasi-cohérent ..... 171
9.3. Prolongement des sections de faisceaux quasi-cohérents..... 172
9.4. Prolongement des faisceaux quasi-cohérents ..... 174
9.5. Image fermée d'un préschéma; adhérence d'un sous-préschéma ..... 176
9.6. Faisceaux quasi-cohérents d'algèbres ; changement de faisceau structural ..... 179

§ 10. Schémas formels ..... 180
10.1. Schémas formels affines..... 180
10.2. Morphismes de schémas formels affines..... 182
10.3. Idéaux de définition d'un schéma formel affine ..... 183
10.4. Préschémas formels et morphismes de préschémas formels .. 185
10.5. Idéaux de définition des préschémas formels ..... 186
10.6. Préschémas formels comme limites inductives de préschémas.. 188
10.7. Produit de préschémas formels ..... 193
10.8. Complété formel d'un préschéma le long d'une partie fermée.. 194
10.9. Prolongement d'un morphisme aux complétés ..... 198
10.10. Application aux faisceaux cohérents sur les schémas formels affines ..... 201

10.11. Faisceaux cohérents sur les préschémas formels.... 204
10.12. Morphismes adiques de préschémas formels .... 206
10.13. Morphismes de type fini .... 207
10.14. Sous-préschémas fermés des préschémas formels .... 209
10.15. Préschémas formels séparés .... 212
BIBLIOGRAPHIE .... 215
INDEX DES NOTATIONS .... 217
INDEX TERMINOLOGIQUE .... 219

Reçu le 17 octobre 1959.