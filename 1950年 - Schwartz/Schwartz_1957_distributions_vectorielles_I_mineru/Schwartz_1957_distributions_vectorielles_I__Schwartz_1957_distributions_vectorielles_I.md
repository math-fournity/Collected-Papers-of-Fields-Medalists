LAURENT SCHWARTZ

Théorie des distributions à valeurs vectorielles. I

Annales de l'institut Fourier, tome 7 (1957), p. 1-141

&lt;http://www.numdam.org/item?id=AIF_1957__7__1_0&gt;

© Annales de l’institut Fourier, 1957, tous droits réservés.

L'accès aux archives de la revue « Annales de l'institut Fourier » (http://annalif.ujf-grenoble.fr/) implique l'accord avec les conditions générales d'utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou impression systématique est constitutive d'une infraction pénale. Toute copie ou impression de ce fichier doit contenir la présente mention de copyright.

# THÉORIE DES DISTRIBUTIONS A VALEURS VECTORIELLES (\*) par Laurent SCHWARTZ.

## INTRODUCTION

Le présent ouvrage étend aux distributions à valeurs vectorielles les principales propriétés des distributions ordinaires ou distributions à valeurs scalaires (Théorie des distributions, Paris, Hermann, 1950-51, et deuxième édition du tome I, 1957). Tant qu'il ne s'agit que de définir les distributions vectorielles, la dérivation, la transformation de Fourier ou Laplace, ou le produit scalaire, multiplicatif ou convolutif d'une distribution vectorielle et d'une distribution scalaire, ou même les propriétés topologiques des espaces de distributions, il n'y a pas de difficultés essentielles; les théorèmes sont ceux auxquels on s'attend, les démonstrations se déroulent de façon naturelle; toutes ces considérations font l'objet du chapitre 1. Au contraire, le produit scalaire, multiplicatif ou convolutif de deux distributions vectorielles sont des opérations beaucoup plus difficiles; elle ne sont possibles que moyennant des hypothèses supplémentaires, souvent inattendues. Les développements correspondants font l'objet du chapitre 11, où le lecteur vérifiera que les démonstrations sont généralement longues et pénibles. Cependant les résultats qu'on pouvait espérer sont bien vrais, si l'on consent à faire des hypothèses restrictives assez fortes, mais inévitables. Et alors les théorèmes obtenus sont des outils assez forts, et permettent de résoudre simplement beaucoup de problèmes.

(\*) On trouvera ici la première partie d'un mémoire dont la fin paraîtra dans le tome VIII des Annales de l'Institut Fourier.

Ce travail, bien que paraissant dans un périodique, a le caractère d'un livre. Il n'est absolument pas destiné à être lu de façon continue, mais plutôt à être consulté; il contient l'énoncé des conditions dans lesquelles on a le droit de faire, avec les distributions vectorielles, les diverses opérations qu'on souhaite naturellement faire.

Nous utiliserons systématiquement les propriétés des distributions scalaires, et des espaces vectoriels topologiques. En ce qui concerne les distributions scalaires, nous ne donnerons pas, en général, de référence; il est bien évident que, quand nous étudierons la dérivée d'une distribution vectorielle, le lecteur devra connaître déjà la dérivée d'une distribution scalaire et ses propriétés essentielles. Par contre, pour tout ce qui concerne les espaces vectoriels topologiques, nous donnerons partout des références très précises. A la fin de ce livre, se trouve un index de toutes les notations et expressions spéciales utilisées avec référence bibliographique pour leur définition. Signalons cependant dès maintenant que, conformément à ce qui a été dit dans SCHWARTZ [1], p. 139, nous utiliserons un accent circonflexe pour les variables muettes; $f(\hat{x})$ veut dire: la fonction $f: x \to f(x)$.

Avant chacun des deux chapitres, se trouve un résumé, suivant d'assez près le texte, et permettant de s'y retrouver plus facilement.

En principe, tous les espaces vectoriels topologiques considérés seront supposés localement convexes séparés quasi-complets, comme il est indiqué page 8, page 50 et page 52. Ces hypothèses ne seront pas répétées dans les énoncés. Par exemple l'énoncé complet de la proposition 3 du chapitre i devrait être : « Si les L$_{i}$ sont des espaces vectoriels topologiques localement convexes séparés quasi-complets, L$_{i}$ est quasi-complet, et il est complet si les L$_{i}$ sont complets ». Parfois il sera bon de ne pas faire cette hypothèse, car elle s'avère inutile; il sera alors spécifié dans l'énoncé que les espaces considérés (toujours localement convexes séparés) ne sont pas nécessairement quasi-complets; c'est ce qui est fait, par exemple, à la proposition 4 du chapitre i : les L$_{j}$, j ∈ J, ne sont pas nécessairement quasi-complets, mais les L$_{k}$, k ∈ K, sur lesquels il n'est rien dit, sont automatiquement supposés quasi-complets.

La plupart des espaces rencontrés en analyse sont quasi-

complets, c'est pourquoi notre restriction n'est pas importante. Nous ne saurions trop conseiller au lecteur de toujours supposer les espaces quasi-complets, même quand ce ne sera pas nécessaire; cela simplifie toujours les démonstrations. La raison pour laquelle, parfois, nous n'avons pas fait cette hypothèse, est que, si F et G sont des espaces localement convexes séparés quasi-complets, l'espace $\mathcal{L}_{b}(\mathrm{F};\mathrm{G})$ des applications linéaires continues de F dans G, muni de la topologie de la convergence uniforme sur les parties bornées, ou le dual fort $\mathrm{F}_{b}^{\prime}$ de F, ne sont pas nécessairement quasi-complets (ils le sont si F est tonnelé). C'est ce qui se présente, par exemple, dans la thèse de F. Bruhat (1). On trouvera les propriétés essentielles des espaces quasi-complets dans Schwartz [1], pages 90-92.

La théorie des distributions à valeurs vectorielles a été déjà exposée dans un séminaire (²), mais les démonstrations y ont été très écourtées, et sont, dans la plupart des cas, insuffisantes. Les produits tensoriels topologiques de Grothendieck (³) y jouent un rôle essentiel. Parmi les principales applications déjà publiées, nous signalerons, outre la thèse de Bruhat déjà mentionnée, celle de Lions (⁴) ainsi que les travaux ultérieurs du même auteur. La physique théorique utilise constamment des distributions à valeurs dans des espaces d'opérateurs (sous le nom de champs).

(1) F. Bruhat, [1].

(2) L. Schwartz, [2], exposés 20 à 24.

$^{4}$  Lions, [1].

(3) Grothendieck, [4] et [5].

## RÉSUMÉ DES PRÉLIMINAIRES

On donne d'abord la définition des propriétés d'approximation et d'approximation stricte (p. 5); puis la définition des espaces de distributions, des espaces de distributions normaux et strictement normaux, de la propriété d'approximation par troncature et régularisation (p. 7); il en sera fait constamment usage. Il faut alors montrer que les espaces de distributions usuels ont ces propriétés : proposition 1 (p. 6), corollaire de la proposition 3 (p. 10), corollaire 2 de la proposition 4 (p. 12); d'autre part la proposition 3 (p. 9) relie entre elles ces diverses propriétés, tandis que la proposition 4 (p. 10) et son corollaire 1 (p. 12). relient les propriétés d'approximation d'un espace et de son dual.

# PRÉLIMINAIRES

## LES PROPRIÉTÉS D'APPROXIMATION

DÉFINITION. — On dit qu'un espace vectoriel topologique localement convexe séparé E a la propriété d'approximation (1) (resp. d'approximation stricte), si l'opérateur identique I de E dans E est adhérent (resp. strictement adhérent) au sous-espace E' ⊗ E (espace des applications linéaires continues de rang fini de E dans E) dans l'espace ℒc(E; E) (espace des applications linéaires continues de E dans E, muni de la topologie de la convergence uniforme sur les parties convexes équilibrées compactes de E).

Remarque. — Si F est un espace localement convexe séparé, et si E a la propriété d'approximation (resp. d'approximation stricte),  $E' \otimes F$  (espace des applications linéaires continues de rang fini de E dans F) est dense (resp. strictement dense) dans  $\mathcal{L}_{c}(E; F)$ . En effet, soit  $u \in \mathcal{L}_{c}(E; F)$ ; l'application  $v \to u \circ v$  de  $\mathcal{L}_{c}(E; E)$  dans  $\mathcal{L}_{c}(E; F)$  est continue; comme alors  $I \in \mathcal{L}_{c}(E; E)$  est supposé adhérent (resp. strictement adhérent) à l'ensemble  $E' \otimes E$ ,  $u = u \circ I$  est adhérent (resp. strictement adhérent) à l'ensemble des  $u \circ v$ ,  $v \in E' \otimes E$ , qui est contenu dans  $E' \otimes F$ .

Dans les mêmes conditions,  $F^{\prime} \otimes E$  est dense (resp. strictement dense) dans  $\mathcal{L}_{c}(F; E)$ .

Soit en effet $u \in \mathcal{L}_{c}(\mathrm{F}; \mathrm{E})$; l'application $\nu \to \nu \circ u$ de $\mathcal{L}_{c}(\mathrm{E}; \mathrm{E})$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Cette propriété est étudiée systématiquement dans GROTHENDIECK [4], chapitre 1, § 5. C'est parce que nous avons besoin, dans le présent article, de la propriété d'approximation stricte, que nous avons écrit ces préliminaires.</span></small>

dans $\mathfrak{L}_{c}(\mathrm{F};\mathrm{E})$ est continue, d'où la conclusion par le même raisonnement que ci-dessus.

De l'ensemble de ces deux résultats on déduit que  $E' \otimes F$  est dense (resp. strictement dense) dans  $\mathcal{L}_{c}(E; F)$ , toutes les fois que E ou F a la propriété d'approximation (resp. d'approximation stricte).

PROPOSITION 1. — L'espace D des fonctions indéfiniment dérivables à support compact sur R$^{n}$ a la propriété d'approximation stricte (1).

Soit $(\alpha_{v})_{v=1,2\dots}$ une suite de fonctions de $\mathcal{D}$ telle que les $\alpha_{v}^{2}$ forment une partition de l'unité sur $R^{n}(^{2})$.

Soit $Q_{v}$ un cube de côtés parallèles aux axes de coordonnées et contenant le support de $\alpha_{v}$. Pour toute fonction $\Psi \in \mathfrak{D}_{Q_{v}}$, on peut construire une fonction $\tilde{\Psi}_{v} \in \mathcal{E}$ et une seule, périodique, de cube des périodes $Q_{v}$, et égale à $\Psi$ dans $Q_{v}$.

Alors $\tilde{\Psi}_{\nu}$ admet un développement en série de Fourier

$$
\tilde {\Psi} _ {\nu} = \sum_ {l \in Z ^ {n}} c _ {l, \nu} (\Psi) \exp (- 2 i \pi l \hat {x}),
$$

$(l = (l_1, l_2 \ldots l_n), \text{ système de } n \text{ entiers de signe quelconque}; lx = l_1 x_1 + l_2 x_2 + \cdots + l_n x_n).$

Les formes linéaires $\Psi\to c_{l,v}(\Psi)$ sont continues sur $\mathcal{D}_{Q}$. Pour toute fonction $\varphi\in\mathcal{D}$, posons alors:

$$
\mathrm{L}_{j}\varphi = \sum_{\substack{\nu <   j\\ |l|\leqslant j}}(\alpha_{\nu}(\hat{x})c_{l,\nu}(\alpha_{\nu}\varphi)\exp (-2i\pi l\hat{x})).\tag{1}
$$

Bien évidemment  $L_{j}: \varphi \to L_{j}\varphi$ , est une application linéaire continue de rang fini de D dans lui-même. Montrons que, pour j tendant vers l'infini et pour  $\varphi$  fixée,  $L_{j}\varphi$  converge vers  $\varphi$  dans D. Comme le support de  $\varphi$  est compact, il existe un entier

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$(\mathcal{H}^{n.}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{L}_c(\mathfrak{D};\mathfrak{D})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Nous avons précisément indiqué, dans un mémoire antérieur (SCHWARTZ [1], page 121, note (29)), qu'il existe une suite d'applications linéaires continues de rang fini de D dans D convergeant vers I dans $\mathcal{L}_{c}(\mathfrak{D};\mathfrak{D})$. Le résultat de la proposition 16, page 120 de ce mémoire ($\mathcal{H}^{n}$: a la propriété d'approximation stricte), est indiqué et démontré ici page 12.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$(\beta_{v})_{v} = 1,2\dots$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\alpha_{v} = \frac{\beta_{v}}{\sqrt{\sum_{\lambda}\beta_{\lambda}^{2}}}.$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{R}^n$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) Soit $(\beta_{v})_{v=1,2}\ldots$ une partition de l'unité sur $R^{n}$; il suffit de prendre</span></small>

$j_{0} \geqslant 0$ tel que $\alpha_{\nu}\varphi \equiv 0$ pour $\nu \geqslant j_{0}$; alors $L_{j}\varphi$ se réduit, quel que soit $j \geqslant j_{0}$, à la somme $\sum_{\nu < i}$.

$$
\sum_{\substack{v\leqslant j_{0}\\ |l|\leqslant j}}
$$

Mais, pour v fixé  $\leqslant j_{0}$ , la somme

$$
\sum_ {| l | \leqslant j} c _ {l, v} \left(\alpha_ {v} \varphi\right) \exp (- 2 i \pi l \hat {x})
$$

converge, pour $j \to \infty$, vers $(\alpha_{v}\varphi)_{v}^{\sim}$ dans $\mathcal{E}$; alors $\mathbf{L}_{j}\varphi$ converge dans $\mathfrak{D}$ vers $\sum_{v \leqslant j_0} \alpha_v(\alpha_v\varphi)_{v}^{\sim} = \sum_{v \leqslant j_0} \alpha_v^2\varphi = \varphi$. Si maintenant $\varphi$ parcourt une partie bornée B de $\mathfrak{D}$, on peut prendre le même $j_0$ pour toutes les $\varphi \in B$, et on sait que $\sum_{|l| \leqslant j} c_{l,v}(\alpha_v\varphi)\exp(-2i\pi l\hat{x})$ converge pour $j \to \infty$ vers $(\alpha_v\varphi)_{v}^{\sim}$ uniformément pour $\varphi \in B$, donc $\mathbf{L}_{j}\varphi$ converge vers $\varphi$ uniformément pour $\varphi \in B$ et $\mathbf{L}_j$ converge vers l'identité I dans $\mathfrak{L}_c(\mathfrak{D};\mathfrak{D})$, c.q.f.d.

PROPOSITION 2. — Soit E un espace vectoriel localement convexe séparé, F un sous-espace de E, muni d'une topologie localement convexe plus fine que la topologie induite par E. Si, dans $\mathfrak{L}_{c}(\mathrm{E};\mathrm{E})$, I est adhérent (resp. strictement adhérent) à $\mathfrak{L}(\mathrm{E};\mathrm{F})$, et si F a la propriété d'approximation (resp. d'approximation stricte), il en est de même de E.

En effet  $E' \otimes F$  est dense (resp. strictement dense) dans  $\mathcal{L}_{c}(E; F)$ , donc a fortiori dans  $\mathcal{L}(E; F)$  muni de la topologie induite par  $\mathcal{L}_{c}(E; E)$ ; et I est adhérente (resp. strictement adhérente) à  $\mathcal{L}(E; F)$  dans  $\mathcal{L}_{c}(E; E)$  d'où le résultat.

Définition. — On appelle espace de distributions sur  $R^{n}$  un sous-espace de l'espace  $D'$  des distributions sur  $R^{n}$ , muni d'une topologie localement convexe plus fine que la topologie induite par  $D'$ .

On dit qu'un espace de distributions H est normal (resp. strictement normal) s'il contient D, si D a une topologie plus fine que la topologie induite par H, et si en outre D est dense (resp. strictement dense) dans H.

On dit qu'un espace de distributions H a la propriété d'approximation par troncature, si, pour toute  $\alpha \in D$ , la multiplication [ $\alpha$ ] : T →  $\alpha T$ , est une opération continue de H dans H, et si, lorsque  $\alpha$  converge vers 1 dans E en restant bornée dans B, l'opération [ $\alpha$ ] converge vers l'identité I dans  $\mathfrak{L}_{\mathrm{e}}(\mathcal{H}; \mathcal{H})$ .

On dit qu'un espace de distributions H a la propriété d'approximation par régularisation, si, pour toute  $\rho \in D$ , la régularisation  $\{\rho\} : T \to T * \rho$ , est une opération continue de H dans H, et si, lorsque le support de  $\rho \geqslant 0$  converge vers l'origine en même temps que  $\int_{R^{n}} \rho(x) \, dx$  tend vers 1,  $\{\rho\}$  tend vers I dans  $\mathfrak{L}_{c}(\mathcal{H}; \mathcal{H})$ .

Remarques. — Si H est normal et tonnelé, il suffit, pour qu'il ait la propriété d'approximation par troncature, que [α] soit une opération continue de H dans H pour α ∈ D, et que, pour toute T ∈ H, αT parcoure une partie bornée de H lorsque α parcourt une partie bornée B de B. En effet cela signifie que les opérateurs [α], α ∈ B, forment une partie bornée de Ls(H; H), donc équicontinue puisque H est tonnelé; comme alors, lorsque α converge vers 1 dans E en restant dans B, [α] converge vers I simplement sur le sous-espace dense D de H, [α] converge vers I dans Lc(H; H) (¹).

De même, si $\mathcal{H}$ est normal et tonnelé, pour que $\mathcal{H}$ ait la propriété d'approximation par régularisation, il suffit que $\{\rho\}$ soit une opération continue de $\mathcal{H}$ dans $\mathcal{H}$ pour $\rho \in \mathfrak{D}$, et que, pour toute $T \in \mathcal{H}$, $\rho * T$ parcoure une partie bornée de $\mathcal{H}$ lorsque $\rho \geqslant 0$, $\int_{R^n} \rho(x) dx \leqslant 1$, et que $\rho \in \mathfrak{D}$ garde son support dans un compact fixe de $R^n$. Il suffit même, si $\mathcal{H}$ est en outre quasi-complet, que toute translation $T \to \tau_h T$ soit continue de $\mathcal{H}$ dans $\mathcal{H}$, et que, pour toute $T \in \mathcal{H}$, les translatées $\tau_h T$ parcourent une partie bornée de $\mathcal{H}$ lorsque $h$ reste borné dans $R^n$. Car alors l'ensemble des opérateurs $\tau_h$ est borné dans $\mathfrak{L}_s(\mathcal{H}; \mathcal{H})$ lorsque $h$ reste borné dans $R^n$, donc équicontinu puisque $\mathcal{H}$ est tonnelé; de plus, la fonction $\vec{\tau}: h \to \tau_h$, est une fonction continue sur $R^n$, lorsqu'on munit $\mathfrak{L}(\mathcal{H}; \mathcal{H})$ de la topologie de la convergence simple sur le sous-espace dense $\mathfrak{D}$ de $\mathcal{H}$, donc une fonction continue à valeur dans $\mathfrak{L}_c(\mathcal{H}; \mathcal{H})$ puisque sur une partie équicontinue la topologie de la convergence compacte est identique à la topologie de la convergence simple sur un sous-espace dense de $\mathcal{H}$. On a donc $\vec{\tau} \in \mathfrak{E}^0(\mathfrak{L}_c(\mathcal{H}; \mathcal{H}))$. Comme en outre $\mathfrak{L}_c(\mathcal{H}; \mathcal{H})$ est quasi-complet puisque $\mathcal{H}$ est quasi-complet et tonnelé ($^2$), l'intégrale $\int_{R^n} \rho(h) \tau_h dh$ a un sens pour $\rho \in \mathfrak{D}^0$ et

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) BOURBAKI [2], théorème 2, page 27, et proposition 5 page 23.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) BOURBAKI [2], corollaire 2 du théorème 4, page 31.</span></small>

représente un élément $\rho(\vec{\tau})$ de $\mathcal{L}_{c}(\mathcal{H};\mathcal{H})(^{\prime})$; cet élément n'est autre que la régularisation $\{\rho\}$, car, pour toute $T\in\mathcal{H}$, on a

$$
\rho (\vec {\tau}). \mathrm{T} = \left(\int_ {\mathbb {R} ^ {n}} \rho (h) \tau_ {h} d h\right). \mathrm{T} = \int_ {\mathbb {R} ^ {n}} \rho (h) \tau_ {h} \mathrm{T} d h (^ {2})
$$

dans $\mathcal{H}$, donc dans $\mathcal{D}'$; or dans $\mathcal{D}'$ le troisième membre vaut $\rho * T$. Alors $\{\rho\}$ est une application linéaire continue de $\mathcal{H}$ dans $\mathcal{H}$, pour $\rho \in \mathcal{D}^0$; si en outre $\rho \geqslant 0$, $\int_{\mathbb{R}^n} \rho(h) dh = 1$, et que le support de $\rho$ tende vers l'origine, $\rho$ tend vers $\delta$ dans $\mathcal{E}_c^{0}$, donc $\rho(\vec{\tau})$ tend vers $\delta(\vec{\tau}) = \tau_0 = I$ dans $\mathcal{L}_c(\mathcal{H}; \mathcal{H})(^3)$, et $\mathcal{H}$ a bien la propriété d'approximation par régularisation.

PROPOSITION 3. — Si ℗ est un espace de distributions normal, ayant la propriété d'approximation par troncature et régularisation, il est strictement normal et a la propriété d'approximation stricte.

En effet, de l'approximation par régularisation, on déduit que $\mathcal{E} \cap \mathcal{H}$ est strictement dense dans $\mathcal{H}$; par troncature on en déduit ensuite que $\mathcal{D}$ est strictement dense dans $\mathcal{E} \cap \mathcal{H}$ (muni de la topologie induite par $\mathcal{H}$); donc $\mathcal{H}$ est bien strictement normal.

Soit ensuite $(\rho_k)_{k=1,2,\ldots}$ une suite de fonctions de $\mathfrak{D}$, $\rho_k \geqslant 0$, $\int_{\mathbb{R}^n} \rho_k(x) dx = 1$, telle que le support de $\rho_k$ converge vers l'origine pour $k \to \infty$. Soit d'autre part $(\alpha_j)_{j=1,2,\ldots}$ une suite de fonctions de $\mathfrak{D}$ tendant, pour $j \to \infty$, vers 1 dans $\mathfrak{E}$ en restant bornée dans $\mathcal{B}$. Alors, dans $\mathcal{L}_c(\mathcal{H}; \mathcal{H})$, I est strictement adhérente à l'ensemble des régularisations $\{\rho_k\}$; mais $\{\rho_k\}$ est strictement adhérente dans $\mathcal{L}_c(\mathcal{H}; \mathcal{H})$ à l'ensemble des opérations $\{\rho_k\} \circ [\alpha_j]$; donc I est strictement adhérente dans $\mathcal{L}_c(\mathcal{H}; \mathcal{H})$ à l'ensemble des $\{\rho_k\} \circ [\alpha_j] \in \mathcal{L}(\mathcal{D}'; \mathcal{D}) \subset \mathcal{L}(\mathcal{H}; \mathcal{D})$ (puisque $\mathcal{H}$ a une topologie plus fine que la topologie induite par $\mathfrak{D}'$); d'où la conclusion en application de la proposition 2 ($\mathcal{H} = E$, $\mathcal{D} = F$; F est bien sous-espace de E muni d'une topo-

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\rho \in \mathcal{D}^0 \subset \mathcal{E}'^0, \vec{\tau} \in \mathcal{E}^0 (\mathcal{L}_c(\mathcal{H}; \mathcal{H}))$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Cet élément peut s'écrire $\rho\left(\vec{\tau}\right)$, au sens de Schwartz [1], théorème 2, page 122: $\rho \in \mathcal{D}^0 \subset \mathcal{E}'^0, \vec{\tau} \in \mathcal{E}^0\left(\mathcal{L}_c(\mathcal{H}; \mathcal{H})\right)$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{L}_c(\mathcal{H};\mathcal{H})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) SCHWARTZ [1], proposition 17, page 123, appliquée à l'opérateur $\nu: u \to u$. T de $\mathcal{L}_{c}(\mathcal{H}; \mathcal{H})$ dans $\mathcal{H}$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(3) SCHWARTZ [1], corollaire 2 de la proposition 19, page 130.</span></small>

logie plus fine que la topologie induite, puisque $\mathcal{H}$ est supposé normal; et $\mathcal{D}$ a la propriété d'approximation stricte (proposition 1)).

COROLLAIRE. — Les espaces $\mathfrak{D}^{m}$ et $\mathcal{E}^{m}$ ($m$ fini'ou infini); $\mathfrak{D}'$, $\mathcal{E}'$; $\mathbf{L}^{p}$, $\mathfrak{D}_{\mathbf{L}^{p}}$ et $\mathfrak{D}_{\mathbf{L}^{p}}'$ ($1 \leqslant p < +\infty$), $\mathcal{B}^{\bullet}$, $\mathcal{B}_{c}(^{1})$; $\mathcal{I}$, $\mathcal{I}'$, $\mathcal{O}_{\mathbf{M}}$, $\mathcal{O}_{\mathbf{C}}'$, $\mathcal{I}'(\Gamma)(^{2})$, sont strictement normaux, ont la propriété d'approximation par troncature et par régularisation, et la propriété d'approximation stricte.

PROPOSITION 4. — Si un espace de distribution H est normal, son dual H', muni de la topologie H'c de la convergence uniforme sur les parties convexes équilibrées compactes de H, est un espace de distributions normal. Si en outre H a la propriété d'approximation (resp. d'approximation stricte, resp. d'approximation par troncature, resp. d'approximation par régularisation) et s'il a la topologie γ de (H')c, alors H'c à la propriété d'approximation (resp. d'approximation stricte, resp. d'approximation par troncature, resp. d'approximation par régularisation).

Les injections $\mathfrak{D} \to \mathcal{H} \to \mathfrak{D}'$ ont en effet des transposées $(\mathfrak{D}')_c' \to \mathcal{H}_c' \to \mathfrak{D}_c'$ ou encore $\mathfrak{D} \to \mathcal{H}_c' \to \mathfrak{D}'$; comme $\mathfrak{D}$ est dense dans $\mathcal{H}$, et $\mathcal{H}$ dense dans $\mathfrak{D}'$ puisque $\mathfrak{D}$ est dense dans $\mathfrak{D}'$, ces transposées sont des injections, et $\mathcal{H}_c'$ est un espace de distributions; comme $\mathcal{H} \to \mathfrak{D}'$ est une injection, $\mathfrak{D}$ est dense dans $\mathcal{H}'$ pour la topologie $\sigma(\mathcal{H}', \mathcal{H})$; $\mathfrak{D}$ est donc aussi dense dans $\mathcal{H}'$ pour toute topologie compatible avec la dualité entre $\mathcal{H}'$ et $\mathcal{H}$, en particulier pour $\mathcal{H}_c'$, qui est trivialement plus fine que $\sigma(\mathcal{H}', \mathcal{H})$ et moins fine que $\tau(\mathcal{H}', \mathcal{H})(^3)$.

Si $\mathcal{H}$ a la topologie $\gamma$, la transposition $u \to {}^t u$ est un isomorphisme (algébrique et topologique) de $\mathcal{L}_c(\mathcal{H}; \mathcal{H})$ sur $\mathcal{L}_c(\mathcal{H}_c'; \mathcal{H}_c')$. Soit en effet $u \in \mathcal{L}(\mathcal{H}; \mathcal{H})$; alors ${}^t u \in \mathcal{L}(\mathcal{H}_c'; \mathcal{H}_c')$.

Réciproquement si $\nu\in\mathcal{L}(\mathcal{H}_{c}^{\prime};\mathcal{H}_{c}^{\prime})$, sa transposée $u=^{t}\nu$ est une application linéaire de $(\mathcal{H}_{c}^{\prime})^{\prime}$ dans $(\mathcal{H}_{c}^{\prime})^{\prime}$ c'est-à-dire de $\mathcal{H}$ dans $\mathcal{H}$, continue pour la topologie $\gamma$, donc pour la topologie initiale de $\mathcal{H}$ si celle-ci coïncide avec $\gamma\left(^{t}\right)$; on a alors $\nu=^{t}u$, avec $u\in\mathcal{L}(\mathcal{H};\mathcal{H})$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{B}_c$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{G}^{\prime}(\Gamma)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) $\mathcal{B}_c$ est défini dans SCHWARTZ [1], page 99, $5^{\circ}$. C'est l'espace $\mathcal{B}$ des fonctions indéfiniment dérivables, bornées ainsi que chacune de leurs dérivées, muni de la topologie de la convergence uniforme sur les parties compactes de $\mathcal{D}_{L_1}'$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{D}_{\mathbf{L}}^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) $\mathcal{G}'(\Gamma)$ est défini dans Schwartz [3], page 200.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(3) BOURBAKI [2], proposition 4, page 67, et corollaire du théorème 2, page 69.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(4) Cette topologie γ sera étudiée au chapitre 1, § 1, page 17.</span></small>

Ceci prouve que $u \to {}^t u$ est un isomorphisme algébrique de $\mathcal{L}(\mathcal{H};\mathcal{H})$ sur $\mathcal{L}(\mathcal{H}_c';\mathcal{H}_c')$.

Montrons que cet isomorphisme est aussi topologique.

Dire que $u$ converge vers 0 dans $\mathcal{L}(\mathcal{H};\mathcal{H})$, c'est dire que $\langle u(x), y' \rangle$ converge vers 0 uniformément lorsque $x$ parcourt une partie convexe équilibrée compacte de $\mathcal{H}$ et $y'$ une partie équicontinue de $\mathcal{H}'$; comme l'enveloppe convexe équilibrée faiblement fermée d'une partie équicontinue est encore équicontinue (1), on peut supposer que $y'$ parcourt une partie équicontinue convexe équilibrée faiblement fermée; une telle partie est compacte dans $\mathcal{H}_c'$ d'après le théorème d'Ascoli (2), et réciproquement toute partie convexe équilibrée compacte de $\mathcal{H}_c'$ est équicontinue sur $(\mathcal{H}_c')_c'$ c'est-à-dire sur $\mathcal{H}$ par hypothèse; ainsi dire que $u$ converge vers 0 dans $\mathcal{L}_c(\mathcal{H};\mathcal{H})$, c'est dire que $\langle u(x), y' \rangle$ converge vers 0 uniformément lorsque $x$ parcourt une partie convexe équilibrée compacte de $\mathcal{H}$ et $y'$ une partie convexe équilibrée compacte de $\mathcal{H}_c'$; mais $\langle u(x), y' \rangle = \langle x, 'u(y') \rangle$, et cela revient alors à dire que $'u$ converge vers 0 dans $\mathcal{L}_c(\mathcal{H}_c';\mathcal{H}_c')$. Ainsi $u \to 'u$ est bien un isomorphisme topologique de $\mathcal{L}_c(\mathcal{H};\mathcal{H})$ sur $\mathcal{L}_c(\mathcal{H}_c';\mathcal{H}_c')$.

Par ailleurs cet isomorphisme applique I sur I, $\mathcal{H}' \otimes \mathcal{H}$ sur $\mathcal{H} \otimes \mathcal{H}'$, la multiplication $[\alpha]$ sur la multiplication $[\alpha]$, et la régularisation $\{\rho\}$ sur la régularisation $\{\check{\rho}\} (\check{\rho}(x) = \rho(-x))$, d'où la conclusion.

Remarques. — 1° Si H est un espace de distributions normal,  $H_{b}^{\prime}$  (dual fort de H) est aussi un espace de distributions; mais il n'est pas nécessairement normal, et de propriétés d'approximation de H on ne peut pas déduire les mêmes propriétés pour  $H_{b}^{\prime}$ . Exemple:  $H = L^{1}$ ,  $H_{b}^{\prime} = L^{\infty}$ .

$2^{\circ}$ Si E et F sont des espaces localement convexes séparés, $u \to {}^{t}u$ est un isomorphisme (algébrique et topologique) de $\mathcal{L}_{c}(E;F)$ sur un sous-espace de $\mathcal{L}_{\varepsilon}(F_{c}^{\prime};E_{c}^{\prime})$ [espace des applications linéaires continues de $F_{c}^{\prime}$ dans $E_{c}^{\prime}$, muni de la topologie de la convergence uniforme sur les parties équicontinues de $F^{\prime}$],

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{H}' \subset \mathcal{H}'$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\overline{\mathbf{H}_{1}^{\prime}}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{H}_1^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$H_{1}^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Si $\mathbf{H}' \subset \mathcal{H}'$ est équicontinue, son enveloppe convexe équilibrée $\mathbf{H}_1'$ l'est aussi trivialement, donc aussi l'adhérence faible $\overline{\mathbf{H}}_1'$ de $\mathbf{H}_1'$ (BOURBAKI [2], proposition 4, page 23).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$l_{4}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{H}_c^\prime$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) Car cette partie est faiblement compacte (BOURBAKI [2], proposition 2, page 65), et sur cette partie les topologies $\sigma$ ($\mathcal{H}'$, $\mathcal{H}$) et $\mathcal{H}_c'$ sont identiques (BOURBAKI [2], proposition 5, page 23).</span></small>

et sur $\mathcal{L}_{\varepsilon}(\mathrm{F}_{c}^{\prime};\mathrm{E}_{c}^{\prime})$ tout entier si E a la topologie $\gamma$; si en outre F a la topologie $\gamma$, $\mathcal{L}_{\varepsilon}(\mathrm{F}_{c}^{\prime};\mathrm{E}_{c}^{\prime}) = \mathcal{L}_{c}(\mathrm{F}_{c}^{\prime};\mathrm{E}_{c}^{\prime})$.

3° Si H est strictement normal, il ne semble pas qu'on puisse en déduire que  $H_{c}^{\prime}$  ait la même propriété. Mais si H est normal et a la propriété d'approximation par troncature et régularisation, alors  $H_{c}^{\prime}$  est strictement normal. En effet l'identité est strictement adhérente, dans  $\mathcal{L}_{c}(\mathcal{H};\mathcal{H})$ , au sous-espace des opérateurs  $\{\rho_{\lambda}\}\circ[\alpha_{\nu}]$ ; comme  $u\to^{t}u$  est continue de  $\mathcal{L}_{c}(\mathcal{H};\mathcal{H})$  dans  $\mathcal{L}_{\varepsilon}(\mathcal{H}_{c}^{\prime};\mathcal{H}_{c}^{\prime})$  donc dans  $\mathcal{L}_{s}(\mathcal{H}_{c}^{\prime};\mathcal{H}_{c}^{\prime})$ , I est strictement adhérente dans  $\mathcal{L}_{s}(\mathcal{H}_{c}^{\prime};\mathcal{H}_{c}^{\prime})$  au sous-espace des  $\{\alpha_{\nu}\}\circ[\check{\rho}_{\lambda}]$ ; alors tout élément T de  $H_{c}^{\prime}$  est strictement adhérent au sous-espace des  $([\alpha_{\nu}]\circ\{\check{\rho}_{\lambda}\})\cdot T\in\mathfrak{D}$ , et  $H_{c}^{\prime}$  est strictement normal.

COROLLAIRE 1. — Si H est un espace de distributions normal ayant la topologie γ de (Hc')c, et la propriété d'approximation par troncature et par régularisation, alors H et Hc' sont strictement normaux, et ont la propriété d'approximation par troncature et par régularisation, et la propriété d'approximation stricte.

Il suffit d'appliquer les propositions 3 et 4.

COROLLAIRE 2. — $\mathfrak{D}_{c}^{'m}$, $\mathfrak{E}_{c}^{'m}$ sont strictement normaux, ont la propriété d'approximation par troncature et par régularisation, et la propriété d'approximation stricte.

Considérons les espaces $\mathcal{H}^{m}$ définis dans un mémoire antérieur (1).

D'après H₂ (page 97), $\mathcal{H}^m$ est un espace de distributions normal; d'après H₄ (page 98), $\mathcal{H}^m$ a la propriété d'approximation par troncature. L'application de la proposition 2 à E = $\mathcal{H}^m$, F = $\mathcal{D}^m$, montre que $\mathcal{H}^m$ à la propriété d'approximation stricte (²) puisque $\mathcal{D}^m$ a cette propriété; enfin $\mathcal{H}^m$ est strictement normal (car $\mathcal{D}^m$ est strictement dense dans $\mathcal{H}^m$ et D strictement dense dans $\mathcal{D}^m$ pour sa topologie usuelle donc a fortiori pour la topologie induite par $\mathcal{H}^m$).

Le dual $\mathcal{H}_{c}^{\prime m}$ est normal, et, si $\mathcal{H}^{m}$ a la topologie $\gamma$, $\mathcal{H}_{c}^{\prime m}$ a la propriété d'approximation par troncature et la propriété d'approximation stricte; et il est alors strictement normal (car $\mathcal{E}^{\prime m}$ est strictement dense dans $\mathcal{H}_{c}^{\prime m}$, et $\mathfrak{D}$ est strictement dense dans $\mathcal{E}_{c}^{\prime m}$ donc a fortiori dans $\mathcal{E}^{\prime m}$ muni de la topologie induite par $\mathcal{H}_{c}^{\prime m}$, donc $\mathfrak{D}$ est strictement dense dans $\mathcal{H}_{c}^{\prime m}$).

(1) Schwartz [1], page 97.

(2) Voir note (1), page 6.

# RÉSUMÉ DU CHAPITRE I

## § 1. Le produit ε d'espaces vectoriels topologiques.

Si L et M sont deux espaces vectoriels topologiques, on définit un espace  $L_{\epsilon}M$  qui leur est canoniquement attaché; plus généralement, si  $(L_{l})_{l\in I}$  est un ensemble fini d'espaces vectoriels topologiques, on peut définir  $L_{I}=\varepsilon L_{l}$  (définition, p. 18). Le produit tensoriel  $\otimes L_{l}$  est un sous-espace de  $L_{I}$  (p. 19), et sur ce produit tensoriel, la topologie induite par  $L_{I}$  est la topologie  $\varepsilon$  de Grothendieck. La définition de  $L_{I}$  à partir des  $L_{l}$  est covariante avec les applications linéaires continues (proposition 1, p. 20). La proposition 2, p. 22, caractérise les parties compactes de  $L_{I}$ .

L'espace  $L_{I}$  est quasi-complet (proposition 3, p. 29).

On peut obtenir divers espaces isomorphes à  $L_{I}$ , grâce à une partition de l'ensemble d'indices I (isomorphismes canoniques, proposition 4, p. 30); le corollaire 2 de la proposition 4, en particulier, est très important, et sera d'un usage constant. Le produit ε est associatif: si (J, K) est une partition de l'ensemble d'indices I,  $L_{I}$  est isomorphe à  $L_{J}\epsilon L_{K}$  (proposition 7, p. 38). Les propriétés particulières aux espaces complets (p. 41) sont destinées aux spécialistes, et ne seront pas utilisées dans la suite. Le cas des espaces de Banach est étudié p. 44. Nous avons vu plus haut que LεM induit sur L⊗M la topologie ε de Grothendieck; il est donc naturel de comparer LεM, qui est quasi-complet, avec le quasi-complété de L⊗M; c'est l'objet de la proposition 11 (p. 46), et de ses corollaires 1 et 2, qui seront utilisés constamment.

Dans tout ce § 1, il n'est pas question de distributions; mais le produit LεM va être la clef de voûte de toute l'étude des espaces de distributions vectorielles, qui va suivre.

## § 2. Définition des distributions à valeurs vectorielles.

Une distribution sur $\mathbb{R}^n$ à valeurs dans E est par définition une application continue de $\mathcal{D}$ dans E (p. 49); l'espace de ces distributions est $\mathfrak{L}(\mathcal{D};\mathrm{E})\asymp\mathcal{D}'_{\varepsilon}\mathrm{E}$ et sera noté $\mathcal{D}'(\mathrm{E})$.

Pour tout espace de distributions H, on peut définir un espace de distributions vectorielles  $\mathcal{H}(\mathrm{E}) = \mathcal{H}\varepsilon\mathrm{E}$  (p. 52). Pour toute distribution  $\vec{\mathrm{T}} \in \mathcal{H}(\mathrm{E})$ ,

et tout élément $\vec{e'} \in \mathbf{E}'$, on peut définir une distribution scalaire $\langle \vec{\mathrm{T}}, \vec{e'} \rangle \in \mathcal{H}$; réciproquement, si $\vec{\mathrm{T}} \in \mathcal{D}'(\mathrm{E})$ est telle que, pour tout $\vec{e'} \in \mathbf{E}'$, $\langle \vec{\mathrm{T}}, \vec{e'} \rangle$ soit dans $\mathcal{H}$, $\vec{\mathrm{T}}$ est-elle dans $\mathcal{H}(\mathrm{E})$? Il en est ainsi si $\mathcal{H}$ à la propriété $\varepsilon$, p. 53; beaucoup d'espaces usuels ont la propriété $\varepsilon$ (proposition 16, p. 59). L'espace $\mathcal{E}'(\mathrm{E})$ n'est pas l'espace des distributions à valeurs dans E, à support compact, que nous notons $\overline{\mathcal{E}'}(\mathrm{E})$ (p. 61); ils coïncident cependant si E est un espace de Banach.

## § 3. Exemples de distributions à valeurs vectorielles et propriétés algébriques et topologiques.

Une fonction scalairement localement intégrable à valeurs dans E définit une distribution, si certaines conditions supplémentaires sont vérifiées (proposition 19, p. 66, proposition 20, p. 66, proposition 21, p. 67, et ses corollaires). La dérivation des distributions est triviale (p. 68); on peut effectuer le produit multiplicatif (proposition 21 bis, p. 70) ou convolutif (p. 72) d'une distribution à valeurs vectorielles et d'une distribution scalaire, dans les conditions auxquelles on peut s'attendre à l'avance; comme nous l'avons dit dans la préface, il n'y a là aucune difficulté, alors que les produits correspondants, pour deux distributions vectorielles (étudiés au chapitre II), introduisent des difficultés très sérieuses.

La transformation de Fourier (p. 73) et de Laplace (proposition 22, p. 76) n'offrent aucune difficulté, elles non plus. Tous ces développements sont essentiels et constituent, pour l'usage courant, la partie la plus importante du chapitre.

La transformation de Laplace plus générale, développée à partir de la p. 76, est au contraire uniquement destinée aux spécialistes, et son intérêt n'est pas prouvé.

Une distribution scalaire est, localement, d'ordre fini et dérivée d'une fonction continue. Cette propriété n'est plus vraie pour les distributions vectorielles; les conditions dans lesquelles elle reste vraie sont énoncées à la proposition 23 (p. 84), et ses corollaires 1 et 2, à la proposition 24 (p. 86), et ses corollaires 1 et 2.

## § 4. Produits tensoriels topologiques d'espaces de distributions.

Un noyau est une distribution  $T_{x,y}$  sur un produit  $X^{l} \times Y^{m}$ . Il définit une opération linéaire continue  $u \to u \cdot T$  de  $D_{x}$  dans  $D_{y}^{\prime}$ , et une opération linéaire continue  $v \to T \cdot v$  de  $D_{y}$  dans  $D_{x}^{\prime}$  (p. 91). La réciproque constitue le théorème des noyaux (proposition 25, p. 93), lié au caractère nucléaire de l'espace D ou E. Si  $H_{x}$  et  $K_{y}$  sont des espaces de distributions sur  $X^{l}$  et  $Y^{m}$ , on peut alors étudier l'espace  $H_{x} \in K_{y}$  (p. 96). La proposition 28, p. 98, donne des exemples remarquables.

Dans ces conditions, la transformation de Fourier pour un produit  $X^{l} \times Y^{m}$  apparaît comme un produit tensoriel de transformations de Fourier (proposition 29, p. 98). Les propriétés liées à la régularité locale (p. 99) ou à la compacité des supports (p. 100) jouent un rôle important. Ensuite sont étudiés les noyaux définissant l'identité (p. 102), les opérations de convolution (p. 103), ou les opérateurs différentiels (p. 106), enfin les noyaux qui sont des fonctions (p. 111). Deux noyaux,  $S_{x,y}$  sur  $X^{l} \times Y^{m}$ ,  $T_{y,z}$  sur  $Y^{m} \times Z^{n}$ , peuvent être composés au sens de Volterra, s'ils ont des propriétés convenables (proposition 34, p. 114). Les lois de composition des noyaux semi-réguliers ou semi-compacts sont les plus importantes (proposition 35, p. 120). Les distributions semi-tempérées sont celles sur lesquelles on peut effectuer une transformation de Fourier partielle (p. 123). Le paragraphe se termine par une brève étude des noyaux vectoriels (p. 124), d'intérêt secondaire.

## § 5. Distributions sommables.

Une distribution à valeurs dans E est sommable si elle appartient à $\mathfrak{D}_{\mathrm{L}}^{\prime}(\mathrm{E})$ (p. 128). On peut alors définir son intégrale, qui est dans E (p. 129); la proposition 36 en donne les propriétés essentielles. La proposition 37 (p. 129) relie le produit scalaire à l'intégrale du produit multiplicatif. On étudie ensuite les distributions de $\mathfrak{D}_{x,y}^{\prime}(\mathrm{E})$ qui sont partiellement sommables en $x$ (p. 130); l'intégrale partielle permet d'exprimer, avec une notation fonctionnelle commode, les opérations définies par des noyaux. La proposition 38 (p. 135) et son corollaire (p. 136) donnent une règle de Fubini pour le calcul d'une intégrale double vectorielle par deux intégrations simples successives.

## CHAPITRE PREMIER DISTRIBUTIONS A VALEURS VECTORIELLES

## § 1. Le produit ε d'espaces vectoriels topologiques.

## Le dual  $L_{c}^{\prime}$  d'un espace localement convexe séparé L.

Soit L un espace vectoriel topologique localement convexe séparé, L' son dual. On appelle L'c le dual muni de la topologie de la convergence uniforme sur les parties convexes équilibrées compactes de L. Si L est quasi-complet, cette topologie est celle de la convergence uniforme sur les parties compactes, puisqu'alors l'enveloppe de toute partie compacte est précompacte (1) et complète donc compacte. Comme les parties convexes équilibrées compactes de L sont a fortiori convexes équilibrées faiblement compactes, il résulte du théorème de Mackey (2) que le dual (L')c de L'c est L. La topologie de L est celle de la convergence uniforme sur les parties équicontinues de L'; c'est aussi la topologie de la convergence uniforme sur les parties équicontinues convexes équilibrées faiblement fermées de L', car l'enveloppe convexe équilibrée faiblement fermée d'une partie équicontinue est encore équicontinue (3). La topologie de (L')c est celle de la convergence uniforme sur les parties convexes équilibrées compactes de L'; comme toute partie équicontinue de L' est relativement compacte dans L'c (4),

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) BOURBAKI [1], page 80, proposition 2.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) BOURBAKI [2], pages 68-69, théorème 2 et corollaire.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(3) BOURBAKI [2], proposition 4, page 23, avec E = L, F = C.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{E} = \mathbf{L},\mathbf{F} = \mathbf{C}.$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">à E = L, F = corps C</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(4) On trouvera une variante de ce théorème dans BOURBAKI [3], page 43, théorème 1 (appliqué à E = L, F = corps C des scalaires); le fait que E soit localement compact n'est utilisé que pour démontrer que la condition est nécessaire, non pour démontrer qu'elle est suffisante. On pourra aussi remarquer que si H' ⊂ L' est équi-</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{H}^{\prime}\subset \mathbf{L}^{\prime}$</span></small>

$(\mathrm{L}_{c}^{\prime})_{c}^{\prime}$ est plus fine que L. Les topologies $(\mathrm{L}_{c}^{\prime})_{c}^{\prime}$ et L seront identiques toutes les fois que les parties convexes équilibrées compactes de $\mathrm{L}_{c}^{\prime}$ seront équicontinues; c'est-à-dire si L a la topologie de la convergence uniforme sur les parties convexes équilibrées compactes de $\mathrm{L}_{c}^{\prime}$.

On appellera en général $\gamma$ cette topologie $(\mathrm{L}_c')_c'$, et on dira que L a la topologie $\gamma$ si $(\mathrm{L}_c')_c' = \mathrm{L}$. Comme les parties convexes équilibrées compactes de $\mathrm{L}_c'$ sont a fortiori convexes équilibrées faiblement compactes, $\gamma$ est moins fine que $\tau(\mathrm{L}, \mathrm{L}')$, donc intermédiaire entre la topologie initiale et $\tau(\mathrm{L}, \mathrm{L}')$. En particulier, toutes les fois que L a la topologie $\tau$ de Mackey, il a la topologie $\gamma$. Mais L peut avoir la topologie $\gamma$ sans avoir la topologie $\tau$. Par exemple, quel que soit l'espace localement convexe M, $\mathrm{L} = \mathrm{M}_c'$ a la topologie $\gamma$ (et n'a pas la topologie $\tau$ s'il y a dans M des parties convexes équilibrées faiblement compactes, mais non compactes). En effet les parties convexes équilibrées compactes de $\mathrm{L}_c' = (\mathrm{M}_c')_c'$ sont a fortiori convexes équilibrées compactes dans la topologie moins fine M, donc sont des parties équicontinues de $\mathrm{L}'$.

On a donc $((\mathrm{L}_c')_c')' = \mathrm{L}_c'$, quel que soit L. Pour que L ait la topologie $\gamma$, il faut et il suffit qu'il existe M tel que $\mathrm{L} = \mathrm{M}_c'$; nous venons de voir que c'est suffisant, et c'est nécessaire, car, si L a la topologie $\gamma$, on a $(\mathrm{L}_c')_c' = \mathrm{L}$ donc $\mathrm{L} = \mathrm{M}_c'$ avec $\mathrm{M} = \mathrm{L}_c'$. Parler d'un espace L ayant la topologie $\gamma$ ou parler de deux espaces L, M, tels que $\mathrm{L} = \mathrm{M}_c'$, $\mathrm{M} = \mathrm{L}_c'$, c'est la même chose.

Les espaces de distributions usuels ont la topologie $\gamma: \mathfrak{D}^m$ et $\mathcal{E}^m$ ($m$ fini ou infini), $\mathfrak{D}', \mathcal{E}', \mathscr{I}, \mathscr{I}', \mathcal{O}_\mathbf{M}, \mathcal{O}_\mathbf{C}', \mathbf{L}^p, \mathbf{D}_{\mathbf{L}^p}(1 \leqslant p \leqslant \infty)$, $\mathcal{B}^*$, $\mathfrak{D}_{\mathbf{L}^p}'(1 \leqslant p < +\infty)$, parce qu'ils sont tonnelés; $\mathfrak{D}_c'^m$, $\mathcal{E}_c'^m$, $\mathcal{B}_c$, puisqu'ils sont de la forme $\mathbf{M}_c'(')$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">continue, son adhérence faible $\overline{\mathbf{H}^{\prime}}$ l'est aussi, $\overline{\mathbf{H}^{\prime}}$ est compacte pour la topologie faible (BOURBAKI [2], proposition 2, page 65), et sur $\overline{\mathbf{H}^{\prime}}$ la topologie faible coïncide avec la topologie induite par $\mathrm{L}_{c}^{\prime}$, (BOURBAKI [2], proposition 5, page 23).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\overline{\mathbf{H}^{\prime}}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$L_{c}^{\prime},$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{D}^m$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{E}^{m}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">B$^{\bullet}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{D}_{\mathbf{L}}p$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2); $\mathfrak{D}^{\prime},\mathfrak{E}^{\prime},\mathfrak{S}^{\prime},\mathfrak{D}_{\mathbf{L}}^{\prime}p(1 < p < \infty)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{B}^{\bullet}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{D}_{\mathbf{L}}^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{O}_{\mathbf{M}}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) $\mathfrak{D}^m$ est un $\mathscr{L}\mathscr{F}$, $\mathscr{E}^m$ et $\mathscr{G}$ sont des espaces de Fréchet, $L^p$ est un Banach, $\mathcal{D}_L^p$ et $\mathscr{B}^\bullet$ sont des espaces de Fréchet (BOURBAKI [2], corollaire de la proposition 1, page 2, et corollaire 2 de la proposition 2, page 2); $\mathscr{D}', \mathscr{E}', \mathscr{G}', \mathscr{D}_L'^p (1 < p < \infty)$, sont des duals d'espaces semi-réflexifs (BOURBAKI [2], proposition 4, page 88); $\mathscr{D}_L'$ est le dual d'un espace de Fréchet distingué $\mathscr{B}^\bullet$ (GROTHENDIECK [2], théorème 7, page 73); donc tous ces espages sont bien tonnelés. $\mathscr{O}_M$ et $\mathscr{O}_C'$ sont tonnelés d'après GROTHENDIECK [5], théorème 16, page 131. Enfin un espace tonnelé à la topologie $\tau$ de Mackey d'après BOURBAKI [2], proposition 5, page 70. Pour l'étude des $\mathcal{D}_L^p$, $\mathscr{D}_L'^p$, $\mathscr{B}^\bullet$, $\mathscr{B}_c$, voir SCHWARTZ [1], pages 99-102, [5], chapitre vi, § 8, et le présent mémoire, début du chapitre i, § 5.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{O}_{\mathbf{c}}^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">5,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{D}_{\mathbf{L}}p,\mathcal{D}_{\mathbf{L}}^{\prime}p,\mathcal{B}^{\bullet},\mathcal{B}_{c}$</span></small>

Les espaces $\varepsilon_{i\in I}L_i = \varepsilon ((L_i)_{i\in I}) = L_I$ et $\varepsilon_{i\in I}(L_i;M)$.

DÉFINITION. — I étant un ensemble fini d'indices, les L'étant des espaces vectoriels topologiques localement convexes séparés,  $L_{I} = \varepsilon_{i \in I} L_{i}$  est l'espace vectoriel des formes multi-

$$
\prod_ {i \in I} \left(\mathbf {L} _ {i}\right) _ {c} ^ {\prime},
$$

parties équicontinues des  $L_{i}^{\prime}$ ; il est muni de la topologie (localelement convexe séparée) de la convergence uniforme sur les produits de parties équicontinues des  $L_{i}^{\prime}$ . Plus généralement, si M est localement convexe,  $\varepsilon(\mathbf{L}_{i};\mathbf{M})$  sera l'espace vectoriel des

applications multilinéaires de $\prod_{i\in I}(\mathbf{L}_{i})_{c}^{\prime}$ dans M, hypocontinues

par rapport aux parties équicontinues des  $L_{i}^{\prime}$ ; il est muni de la topologie de la convergence uniforme sur les produits de parties équicontinues des  $L_{i}^{\prime}$ .

Si I ne contient que 2 éléments i, j, nous noterons aussi par $\mathbf{L}_{i}\in\mathbf{L}_{j}$ l'espace $\mathbf{L}_{\mathrm{I}}$.

D'autre part, nous dirons, par abréviation, ε-hypocontinue, au lieu de : hypocontinue par rapport aux parties équicontinues des L$_{i}$.

Enfin, sauf mention expresse du contraire, les L, et M seront supposés séparés quasi-complets.

Nous verrons alors que $\varepsilon_{i\in I}(\mathbf{L}_{i};\mathbf{M})$ est isomorphe, algébri-

quement et topologiquement, à $\varepsilon((\mathbf{L}_{i})_{i\in I},\mathbf{M})$ et à $\mathbf{L}_{I}\in\mathbf{M}$ (corollaire 1 de la proposition 4 et corollaire 2 de la proposition 7). Ainsi la notation $\varepsilon(\mathbf{L}_{i};\mathbf{M})$ n'est-elle que provisoire.

(1) On trouvera les propriétés des applications bilinéaires $\mathfrak{S}$ — $\mathfrak{G}$-hypocontinues de E × F dans G dans BOURBAKI [2], chapitre III, § 4.

Soient  $E_{i}, i \in I$ , et F des espaces vectoriels topologiques;  $S_{i}$  une famille de parties bornées de  $E_{i}$  telle que  $\bigcup_{A_{i} \in S_{i}} A_{i} = E_{i}$ . On dit qu'une application multilinéaire u

de $\prod_{i\in I}E_i$ dans $F$ est hypocontinue par rapport aux familles $\mathfrak{S}_i$ si, pour tout $j\in I$,

tout voisinage W de O dans F, tout système de parties $\mathbf{A}_i \in \mathfrak{S}_i$, $i \in \mathbf{I}$, $i \neq j$, il existe un voisinage $\mathbf{V}_j$ de O dans $\mathbf{E}_j$ tel que $u\big((\vec{l}_i)_{i \in \mathbf{I}}\big) \in \mathbf{W}$ pour $\vec{l}_j \in \mathbf{V}_j$, $\vec{l}_i \in \mathbf{A}_i$ pour $i \neq j$.

Cela entraîne les conséquences suivantes :

a) u est séparément continue;

b) la restriction de $u$ à $\left(\prod_{i\in I, i\neq j}A_i\right)\times E_j$ est continue.

Propriétés analogues pour les ensembles $\{\mathfrak{S}_{i}\}_{i\in I}$-équihypocontinus d'applications multilinéaires.

L'injection canonique $\otimes_{i\in I}L_i\to \varepsilon L_i.$

Soient $\vec{l}_i \in L_i$ des éléments des espaces $L_i$. Ils définissent un élément de $\varepsilon L_i$, la forme $(\vec{l}')_{i \in I} \to \prod_{i \in I} \langle \vec{l}_i', \vec{l}_i \rangle$. On définit ainsi une application multilinéaire de $\prod_{i \in I} L_i$ dans $L_I$, donc une application linéaire de $\otimes L_i$ dans $L_I$. Cette application linéaire est injective, car on sait que l'application canonique de $\otimes L_i$ dans l'espace de toutes les formes multilinéaires sur $\prod_{i \in I} L_i'$ est injective. (On le voit par récurrence sur le nombre $n$ d'éléments de I. C'est évident pour $n = 1$, où les produits $\varepsilon$ et $\otimes$ se réduisent à l'unique espace L considéré. Supposons démontré que l'appli-

cation est injective lorsque l'ensemble d'indices a n—1 éléments. Pour simplifier, supposons  $I = (1, 2, \ldots, n)$ . Considérons un élément  $\lambda$  de  $\otimes_{i \in I} L_i$  dont l'image  $\tilde{\lambda}$  dans  $L_I$  soit nulle. Cet élément peut s'écrire  $\sum_{\alpha} \vec{l}_{1,\alpha} \otimes \vec{\lambda}_{\alpha}$ ,  $\vec{\lambda}_{\alpha} \in \bigotimes_{i=2}^{i=n} L_i$ , les  $\vec{l}_{1,\alpha}$  étant indépendants. La forme multilinéaire qu'il définit sur  $\prod_{i \in I} L_i'$  est

$$
\left(\vec {l} _ {1} ^ {\prime}, \vec {l} _ {2} ^ {\prime}, \dots \vec {l} _ {n} ^ {\prime}\right)\rightarrow \sum_ {\alpha} \left\langle \vec {l} _ {1} ^ {\prime}, \vec {l} _ {1, \alpha} \right\rangle \tilde {\lambda} _ {\alpha} \left(\vec {l} _ {2} ^ {\prime}, \dots \vec {l} _ {n} ^ {\prime}\right),
$$

en désignant par $\tilde{\lambda}_{\alpha}$ l'image de $\lambda_{\alpha}$ dans $\varepsilon_{i=2}^{i=n} L_{i}$.

D'après le théorème de Hahn-Banach, les $\vec{l}_{1,\alpha}$ étant indépendants, on peut, pour tout indice $\beta$, trouver $\vec{l}_{1,\beta}'$ tel que $\langle \vec{l}_{1,\beta}', \vec{l}_{1,\alpha} \rangle = 0$ pour $\alpha \neq \beta$, $= 1$ pour $\alpha = \beta$. Alors la forme multilinéaire précédente ne peut être nulle que si $\tilde{\lambda}_{\beta}$ est nulle, ce qui implique que $\lambda_{\beta}$ soit nulle d'après l'hypothèse de récurrence. Comme c'est vrai quel que soit l'indice $\beta$, l'élément considéré $\lambda$ dans $\otimes_{i \in I} L_i$ était nul). Aussi considérerons-nous désormais $\otimes_{i \in I} L_i$ comme sous-espace vectoriel de $L_1$. Dans ces conditions, l'application $(\vec{l}_i)_{i \in I} \to \otimes_{i \in I} \vec{l}_i$ de $\prod_{i \in I} L_i$ dans $L_1$ est continue. Si $L_2, \ldots, L_n$, sont identiques au corps des scalaires, $L_1$ est identique à $L_1$, algébriquement et topologiquement (en iden-

tifiant l'élément $\vec{l}_{1}$ de $L_{1}$ à l'élément $\vec{l}_{1} \otimes 1 \ldots \otimes 1$ de $\otimes_{i \in I} L_{i}$. Plus généralement si $L_{2}, \ldots, L_{n}$, sont de dimension finie, $L_{I}$ est identique à $\otimes_{i=1}^{i=n} L_{i}$ (en effet tout élément de $L_{I}$ définit une application multilinéaire de $\prod_{i=2}^{i=n} L_{i}'$ dans le dual de $(L_{1})_{c}'$ c'est-à-dire dans $L_{1}$, et une telle application est alors définie par un élément de $L_{1} \otimes \binom{i=n}{\otimes L_{i}}$).

Compatibilité avec les applications linéaires continues.

PROPOSITION 1. — Soient $L_i$, $M_i$, des espaces vectoriels localement convexes séparés (non nécessairement quasi-complets), dépendant d'un même ensemble d'indices I, et soit, pour chaque i, $u_i$ une application linéaire continue de $L_i$ dans $M_i$.

Il existe une application linéaire continue canonique, notée $u_{1}$ ou $\otimes_{i\in I} u_{i}$ ou $\varepsilon_{i\in I} u_{i}$, de $L_{I}$ dans $M_{I}$, qui prolonge l'application $\otimes_{i\in I} u_{i}$ de $\otimes_{i\in I} L_{i}$ dans $\otimes_{i\in I} M_{i}$. Si les $u_{i}$ sont injectives, $u_{1}$ est injective; si les

$$
u _ {i}
$$

$$
u _ {\mathrm{I}}
$$

Si, pour tout i,  $u_{i}$  parcourt un ensemble équicontinu  $H_{i}$  d'applications de  $L_{i}$  dans  $M_{i}$ ,  $u_{I}$  parcourt un ensemble équicontinu d'applications de  $L_{I}$  dans  $M_{I}$ .

Soit en effet $\vec{\mathbf{X}}\in\mathbf{L}_{\mathrm{I}}$. On définit $u_{\mathrm{I}}$. $\vec{\mathbf{X}}$ par

$$
\left(u _ {I}. \overrightarrow {\mathrm{X}}\right) \left(\left(\overleftarrow {m _ {i} ^ {\prime}}\right) _ {i \in I}\right) = \overrightarrow {\mathrm{X}} \left(\left(^ {t} u _ {i}. \overleftarrow {m _ {i} ^ {\prime}}\right) _ {i \in I}\right).\tag{I, 1; 1}
$$

Alors  $U_{I}$ . X est bien une forme multilinéaire sur  $\prod_{i\in I}(\mathbf{M}_{i})_{c}^{\prime}$ .

Montrons qu'elle est $\varepsilon$-hypocontinue. Pour simplifier, supposons $I = (1, 2, \ldots n)$. Si $\overleftarrow{m_i}$, $i \geqslant 2$, parcourt une partie équicontinue $B_i'$ de $M_i'$, $^t u_i \cdot \overleftarrow{m_i'}$ parcourt une partie équicontinue $^t u_i \cdot B_i'$ de $L_i'$, parce que l'image réciproque, par $u_i$, du voisinage $B_i'^0$ de O de $M_i$ est un voisinage de O de $L_i(^1)$. Si $\overleftarrow{m_i'}$ converge vers O dans $(M_1)'_c$, $^t u_1 \cdot \overleftarrow{m_i'}$ converge vers O dans $(L_1)'_c$, parce que l'image par $u_1$ de toute partie convexe équilibrée

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{B} = \mathbf{B}_i^{\prime 0},\mathbf{A} = u_i^{-1}(\mathbf{B}_i^{\prime 0})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Nous utiliserons constamment dans la suite la proposition 2, page 101 de BOURBAKI [2]. Nous l'appliquons ici pour $\mathbf{B} = \mathbf{B}_{i}^{\prime 0}, \mathbf{A} = u_{i}^{-1}(\mathbf{B}_{i}^{\prime 0})$.</span></small>

compacte de  $L_{i}$  est convexe équilibrée compacte dans  $M_{i}$ . Comme alors  $\vec{X}$  est ε-hypocontinue sur  $\prod_{i\in I}(L_{i})_{c}^{\prime}$ ,  $u_{I}\cdot\vec{X}$  est bien ε-hypo-continue sur  $\prod_{i\in I}(M_{i})_{c}^{\prime}$ , donc  $u_{I}\cdot\vec{X}\in M_{I}$ , et  $u_{I}$  est bien une application linéaire de  $L_{I}$  dans  $M_{I}$ ; elle coïncide bien, sur  $\otimes L_{i}$ , avec l'application canonique  $\otimes u_{i}$  de  $\otimes L_{i}$  dans  $\otimes M_{i}$ . Si maintenant  $\vec{X}$  converge vers O dans  $L_{I}$ ,  $u_{I}\cdot X$  converge vers O dans  $M_{I}$ ; si en effet les  $B_{i}^{\prime}$  sont des parties équicontinues des  $M_{i}^{\prime}$ ,  $(u_{I}\cdot\vec{X})(\prod_{i\in I}B_{i}^{\prime})=\vec{X}\left(\prod_{i\in I}(^{t}u_{i}\cdot B_{i}^{\prime})\right)$ , et nous venons de voir que les  $^{t}u_{i}\cdot B_{i}^{\prime}$  sont des parties équi-continues des  $L_{i}^{\prime}$ ; donc  $u_{I}$  est continue. Plus généralement soit, pour tout i,  $H_{i}$  une partie équicontinue de  $\mathcal{L}(L_{i};M_{i})$ . Alors  $\bigcup_{u_{i}\in H_{i}}^{t}u_{i}\cdot B_{i}^{\prime}$  est encore une partie équicontinue de  $L_{i}^{\prime}$ , parce que  $\bigcap_{u_{i}\in H_{i}}u_{i}^{-1}((B_{i}^{\prime})^{0})$  est un voisinage de O de  $L_{i}$  en vertu de l'équicontinuité de  $H_{i}$ ; alors, si  $\vec{X}$  converge vers O dans  $L_{I}$ ,  $u_{I}\cdot X$  converge vers 0 dans  $M_{I}$ , uniformément pour  $(u_{i})_{i\in I}\in\Pi_{i\in I}H_{i}$ ; autrement dit l'ensemble des  $u_{I}$ , pour  $(u_{i})_{i\in I}\in\Pi_{i\in I}H_{i}$ , est une partie équicontinue de  $\mathcal{L}(L_{I};M_{I})$ .

Supposons que chaque  $u_{i}$  soit injective. Montrons que  $u_{I}$  est injective. Soit en effet  $X\in L_{I}$  tel que  $u_{I}\cdot\vec{X}=O$ . Cela signifie que  $\vec{X}$  est nulle sur  $\prod_{i\in I}(^{t}u_{i}\cdot M_{i}^{\prime})$ . Mais,  $u_{i}$  étant injective,  $^{t}u_{i}\cdot M_{i}$  est faiblement dense dans  $L_{i}^{\prime}$ , donc dense dans  $(L_{i})_{c}^{\prime}$ , puisque le dual de  $(L_{i})_{c}^{\prime}$  est  $L_{i}$ . Donc  $\vec{X}$ , étant séparément continue sur  $\prod_{i\in I}(L_{i})_{c}^{\prime}$ , est nulle, et  $u_{I}$  est bien injective. Cela nous permettra, si, pour tout i,  $L_{i}$  est un sous-espace de  $M_{i}$  muni d'une topologie plus fine que la topologie induite, d'identifier  $L_{I}$  à un sous-espace de  $M_{I}$, muni d'une topologie plus fine que la topologie induite.

Supposons maintenant que  $u_{i}$  soit un monomorphisme, c'est-à-dire un isomorphisme de  $L_{i}$  sur  $u_{i}(L_{i})\subset M_{i}$ . Montrons que  $u_{I}$  est un monomorphisme. Supposons donc que  $u_{I}\cdot X$  converge vers 0 dans  $M_{I}$, nous devons montrer que  $\vec{X}$  converge vers 0 dans  $L_{I}$. Soient donc  $A_{i}^{\prime}$  des parties équicontinues des  $L_{i}^{\prime}$;

nous devons montrer que $\vec{X}$ converge vers 0 uniformément sur $\prod A_{i}^{\prime}$.

Soit $\vec{l}_{i}^{\prime}\in\mathrm{L}_{i}^{\prime}$; puisque $u_{i}$ est un isomorphisme de $\mathrm{L}_{i}$ sur $u_{i}(\mathrm{L}_{i})$, $u_{i}.\vec{l}_{i}\to\langle\vec{l}_{i}^{\prime},\vec{l}_{i}\rangle$ est une forme linéaire continue $(\vec{l}_{i}^{\prime})_{0}$ sur $u_{i}(\mathrm{L}_{i})$; de plus, lorsque $\vec{l}_{i}^{\prime}$ parcourt $\mathrm{A}_{i}^{\prime},(\vec{l}_{i}^{\prime})_{0}$ parcourt un ensemble équi-continu $(\mathrm{A}_{i}^{\prime})_{0}$ de formes linéaires sur $u_{i}(\mathrm{L}_{i})$. D'après le théorème de Hahn-Banach, $(\vec{l}_{i}^{\prime})_{0}$ peut-être prolongé en une forme linéaire continue $\overleftarrow{m}_{i}^{\prime}$ sur $\mathrm{M}_{i}$, et de manière que, lorsque $(\vec{l}_{i}^{\prime})_{0}$ parcourt $(\mathrm{A}_{i}^{\prime})_{0}$, les $\overleftarrow{m}_{i}^{\prime}$ parcourent un ensemble équicontinu $\mathrm{B}_{i}^{\prime}$ de formes linéaires sur $\mathrm{M}_{i}$. On a alors $^{t}u_{i}.\overleftarrow{m}_{i}^{\prime}= \overleftarrow{l}_{i}^{\prime}$, $^{t}u_{i}.B_{i}^{\prime}= \mathrm{A}_{i}^{\prime}$, et puisque, par hypothèse, $u_{1}.X$ converge vers 0 uniformément sur $\prod_{i\in I}\mathrm{B}_{i}^{\prime},\overrightarrow{\mathrm{X}}$ converge bien vers 0 uniformément sur $\prod_{i\in I}\mathrm{A}_{i}^{\prime}$ et $u_{1}$ est bien un monomorphisme. Cela permet, si $\mathrm{L}_{i}$ est, pour tout $i$, un sous-espace vectoriel topologique de $\mathrm{M}_{i}$, d'identifier $\mathrm{L}_{1}$ à un sous-espace vectoriel topologique de $\mathrm{M}_{1}$.

Remarques: 1° Si les $u_{i}$ sont épijectives, $u_{I}$ n'est pas nécessairement épijective, et si les $u_{i}$ sont des épimorphismes, $u_{I}$ n'est pas nécessairement un épimorphisme.

2° Si  $L_{i}$ ,  $M_{i}$ ,  $N_{i}$ , sont des espaces localement convexes séparés, non nécessairement quasi-complets, et si l'on a des applications linéaires continues  $u_{i} \in \mathcal{L}(L_{i}; M_{i})$ ,  $v_{i} \in \mathcal{L}(M_{i}; N_{i})$ ,  $w_{i} = v_{i} \circ u_{i} \in \mathcal{L}(L_{i}; N_{i})$ , on a aussi  $w_{I} = v_{I} \circ u_{I}$ .

Ensembles $\varepsilon$-équihypocontinus de formes multilineaires sur $\prod_{i\in I}(\mathbf{L}_{i})_{c}^{\prime}$ et parties relativement compactes de $\mathbf{L}_{1}$.

PROPOSITION 2. — Soit H un ensemble de formes multilinéaires sur $\prod_{i=1}^{n}(L_{i})_{c}^{\prime}$.

Les 3 propriétés suivantes relatives à H sont équivalentes :

a) H est ε-équihypocontinu;

b) H est séparément équicontinu, et équicontinu sur tout produit de parties équicontinues des  $L_{i}^{\prime}$ ;

c) H est une partie relativement compacte de $\mathbf{L}_{\mathrm{I}}$.

Le fait que $a)$ implique $b)$ est trivial (même si les $\mathbf{L}_{i}$ ne sont pas quasi-complets $(^{1})$).

Montrons que $a)$ implique $c)$ (même si les $\mathbf{L}_{i}$ ne sont pas

(1) Voir note (1) page 18.

quasi-complets). Tout d'abord si l'on a $a$), $\mathbf{H} \subset \mathbf{L}_{\mathrm{I}}$. Soit alors $\mathfrak{U}$ un ultrafiltre sur H. Comme H est borné pour la topologie de la convergence simple sur $\prod_{i \in I} \mathbf{L}_{i}'$, $\mathfrak{U}$ converge simplement vers

une forme multilinéaire $\overline{\mathbf{X}}$. Mais comme H est $\varepsilon$-équihypocontinu, $\overrightarrow{\mathbf{X}}$ est $\varepsilon$-hypocontinue donc $\overrightarrow{\mathbf{X}} \in L_{I}(1)$. Enfin, si les $A_{i}^{\prime}, i \in I$, sont des parties équicontinues, convexes équilibrées faiblement fermées, donc compactes dans les $(L_{i})_{c}^{\prime}$, H est équi-continu sur $\prod_{i \in I} A_{i}^{\prime}$ d'après $b$), et comme $\prod_{i \in I} A_{i}^{\prime}$ est compact, $\mathcal{U}$ converge vers $\overrightarrow{\mathbf{X}}$ uniformément sur $\prod_{i \in I} A_{i}^{\prime}(2)$; donc $\mathcal{U}$ converge vers $\overrightarrow{\mathbf{X}}$ dans $L_{I}$, et H est bien relativement compacte.

Supposons maintenant les  $L_{i}$  quasi-complets, et montrons que b) entraîne c) et que c) entraîne a). Soit U un ultrafiltre sur H, H vérifiant la propriété b). H est borné pour la topologie de la convergence simple, donc U converge simplement vers une forme multilinéaire  $\overrightarrow{X}$ . Puisque H est séparément équi-continu,  $\overrightarrow{X}$  est séparément continue; puisque H est équi-continu sur tout produit de parties équicontinues des  $L_{i}^{\prime}$ , X est continue sur tout produit de parties équicontinues des  $L_{i}^{\prime}$ . Par ailleurs, si les  $A_{i}^{\prime}$  sont des parties équicontinues faiblement fermées des  $L_{i}^{\prime}$ , elles sont compactes dans les  $(\mathrm{L}_{i})_{c}^{\prime}$ , H est équi-continue sur  $\prod_{i\in I}A_{i}^{\prime}$ , donc la convergence de U vers  $\overrightarrow{X}$  est uni-

forme sur $\prod_{i\in I}A_{i}^{\prime}$; si nous montrons qu'en vertu des propriétés

ci-dessus, $\vec{X}$ est dans $L_{I}$, c'est-à-dire que $\vec{X}$ est ε-hypo-continue, alors cela prouvera que H est dans $L_{I}$ et que c'est une partie relativement compacte de $L_{I}$. Pour simplifier, prenons I = (1, 2, ... n).

Considérons la forme linéaire $u_{\vec{X}}^{\rightarrow}(\vec{l}_{2}^{\prime}, \ldots, \vec{l}_{n}^{\prime})$ sur $L_1'$ définie par

$$
\langle \vec {l} _ {1}, u _ {\mathrm{X}} (\vec {l} _ {2}, \dots \vec {l} _ {n}) \rangle = \vec {\mathrm{X}} (\vec {l} _ {1}, \vec {l} _ {2}, \dots \vec {l} _ {n}) \quad \text { pour   tout } \quad l _ {1} ^ {\prime} \in \mathrm{L} _ {1} ^ {\prime}. \tag {I,1;2}
$$

Lorsque les $\vec{l}_{i}^{\prime}, i=2,\ldots n$, sont fixés, et que $\vec{l}_{i}^{\prime}$ converge vers 0 dans $(\mathrm{L}_{1})_{c}^{\prime}$, le second membre converge vers 0 puisque $\vec{\mathrm{X}}$ est séparément continue; donc $u_{\vec{\mathrm{X}}}\left(\vec{l}_{2}^{\prime},\ldots\vec{l}_{n}^{\prime}\right)$ est une forme

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) BOURBAKI [2], chapitre III, § 3, n° 5, proposition 4, page 23.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) BOURBAKI [3], chapitre x, § 3, n° 7, proposition 14, page 34.</span></small>

linéaire continue sur $(\mathrm{L}_1)_{c}^{\prime}$, autrement dit $u_{\overline{\mathbf{X}}}\left(\vec{l}_2', \ldots \vec{l}_n'\right) \in \mathrm{L}_1$. Alors $u_{\overline{\mathbf{X}}}$, définie par $\left(\vec{l}_2', \ldots \vec{l}_n'\right) \to u_{\overline{\mathbf{X}}}\left(\vec{l}_2', \ldots \vec{l}_n'\right)$, est une application multilinéaire de $\prod_{i=n}^{i=n} (\mathrm{L}_i)_{c}^{\prime}$ dans $\mathrm{L}_1$. Montrons que cette application linéaire est continue sur tout produit de parties équicontinues des $\mathrm{L}_i'$, $i=2, \ldots n$. Soient donc $\mathrm{A}_i'$, $i=2, \ldots n$ des parties équicontinues des $\mathrm{L}_i'$, faiblement fermées, donc compactes dans les $(\mathrm{L}_i)_{c}^{\prime}$. Soit aussi $\mathrm{A}_i'$ une partie équicontinue faiblement fermée dans $\mathrm{L}_1'$. Comme $\overline{\mathbf{X}}$ est supposée continue sur $\prod_{i \in I} \mathrm{A}_i'$, elle est continue sur $\prod_{i=2}^{i=n} \mathrm{A}_i'$ pour $\vec{l}_1'$ fixée dans $\mathrm{A}_1'$, et uniformément lorsque $\vec{l}_1'$ parcourt le compact $\mathrm{A}_1'$: si $(\vec{l}_2', \ldots \vec{l}_n')$ converge vers $\left((\vec{l}_2')_0, \ldots (\vec{l}_n')_0\right)$ dans $\prod_{i=2}^{i=n} \mathrm{A}_i'$, $\overline{\mathbf{X}}\left(\vec{l}_1', \vec{l}_2', \ldots \vec{l}_n'\right) - \overline{\mathbf{X}}\left(\vec{l}_1', (\vec{l}_2')_0, \ldots (\vec{l}_n')_0\right)$ converge vers 0 uniformément pour $\vec{l}_1' \in \mathrm{A}_1'$; autrement dit, puisque la topologie de $\mathrm{L}_1$ est précisément celle de la convergence uniforme sur les parties équicontinues faiblement fermées de $\mathrm{L}_1'$, $u_{\overline{\mathbf{X}}}(\vec{l}_2', \ldots \vec{l}_n') - u_{\overline{\mathbf{X}}}((\vec{l}_2')_0, \ldots (\vec{l}_n')_0)$ converge vers 0 dans $\mathrm{L}_1$, ce qui montre bien la continuité de $u_{\overline{\mathbf{X}}}$ sur $\prod_{i=2}^{i=n} \mathrm{A}_i'$. Comme alors $\prod_{i=2}^{i=n} \mathrm{A}_i'$ est compact, son image $u_{\overline{\mathbf{X}}}(\prod_{i=2}^{i=n} \mathrm{A}_i')$ est un compact de $\mathrm{L}_1$; comme la topologie de $(\mathrm{L}_1)_{c}^{\prime}$ est précisément celle de la convergence uniforme sur les parties compactes de $\mathrm{L}_1$, puisque $\mathrm{L}_1$ est quasi-complet, on voit que, si $\vec{l}_1'$ converge vers 0 dans $(\mathrm{L}_1)_{c}^{\prime}$, et que les $\vec{l}_i', i \geqslant 2$, parcourent les $\mathrm{A}_i'$, $\overline{\mathbf{X}}\left(\vec{l}_1', \vec{l}_2', \ldots \vec{l}_n'\right)$ converge vers 0. En faisant le même raisonnement pour $i=2...n$, on voit que $\overline{\mathbf{X}}$ est bien ε-hypocontinue et $b)$ entraîne $c)$.

Montrons enfin que, si les  $L_{i}$  sont quasi-complets, c) entraîne a). Soit donc H une partie compacte de  $L_{1}$ . A tout  $\vec{X} \in L_{I}$  associons l'application multilinéaire  $u_{\vec{X}}$  de  $\prod_{i=n}(L_{i})_{c}^{\prime}$  dans  $L_{1}$ . Comme la topologie de  $L_{1}$  est précisément celle de la convergence uniforme sur les parties équicontinues de  $L_{1}^{\prime}$ , la topologie de  $L_{1}$  est précisément celle de la convergence de  $u_{\vec{X}}$ , uniformément sur tout produit de parties équicontinues des  $L_{1}^{\prime}, i = 2 \ldots n$ .

Si alors les  $A_{i}^{\prime}, i = 2 \ldots n$ , sont équicontinues compactes dans les  $(\mathbf{L}_{i})_{c}^{\prime}, \prod_{i=2}^{n} \mathbf{A}_{i}^{\prime}$  est compact dans  $\prod_{i=2}^{n} (\mathbf{L}_{i})_{c}^{\prime}$ ; et comme

$$
\left(\overrightarrow {X}, \left(\overleftarrow {l _ {i} ^ {\prime}}\right) _ {i = 2, \dots n}\right)\rightarrow u _ {\overrightarrow {X}} \left(\left(\overleftarrow {l _ {i} ^ {\prime}}\right) _ {i = 2, \dots n}\right)
$$

est continu de  $L_{1} \times \prod_{i=2}^{n} A_{i}'$  dans  $L_{1}$  (puisque séparément continue en X, uniformément pour  $\left(\vec{l}_{i}'\right)_{i=2,\ldots,n} \in \prod_{i=2}^{i=n} A_{i}'$ , et séparément continue en  $\left(\vec{l}_{i}'\right)_{i=2,\ldots,n}$ ), l'image par cette application du compact  $H \times \prod_{i=2}^{i=n} A_{i}'$ , c'est-à-dire  $\bigcup_{\vec{X} \in H} u_{\vec{X}}\left(\prod_{i=2}^{i=n} A_{i}'\right)$ , est un compact de  $L_{1}$ . Comme  $L_{1}$  est quasi-complet, la topologie de  $(\mathrm{L}_{1})_{c}'$  est celle de la convergence uniforme sur les parties compactes de  $L_{1}$ , donc, si  $\vec{l}_{1}'$  converge vers 0 dans  $(\mathrm{L}_{1})_{c}'$ , et que les  $\vec{l}_{i}'$  parcourent les  $A_{i}'$ ,  $i = 2 \ldots n$ ,  $\vec{X}\left(\vec{l}_{1}', \vec{l}_{2}', \ldots, \vec{l}_{n}'\right)$  converge vers 0, uniformément pour  $X \in H$ . En faisant le même raisonnement avec  $i = 2, \ldots, n$ , on voit que H est ε-équihypocontinu, et c) entraîne bien a).

Remarques. — 1° Si l'ensemble d'indices I a au plus deux éléments, $a$, $b$, $c$) sont encore équivalentes, lorsque H est réduite à une seule forme multilinéaire $\vec{X}$ sur $\prod_{i\in I}(\mathbf{L}_{i})_{c}^{\prime}$, même si les $\mathbf{L}_{i}$ ne sont pas quasi-complets.

Soit en effet I = (1, 2), et soit $\vec{X}$ une forme multilinéaire vérifiant $b$). On peut choisir la partie équicontinue $\mathbf{A}_{2}^{\prime}$ non seulement compacte dans $(\mathrm{L}_{2})_{c}^{\prime}$, mais convexe et équilibrée. Alors $u_{\vec{X}}(\mathbf{A}_{2}^{\prime})$ est convexe équilibrée compacte dans $\mathbf{L}_{1}$. Comme la topologie de $(\mathrm{L}_{1})_{c}^{\prime}$ est celle de la convergence uniforme sur les parties convexes équilibrées compacte de $\mathbf{L}_{1}$, on voit que $\vec{X}(\hat{l}_{1}^{\prime}, \hat{l}_{2}^{\prime})$ converge vers 0 lorsque $\hat{l}_{1}^{\prime}$ converge vers 0, uniformément pour $\hat{l}_{2}^{\prime} \in \mathbf{A}_{2}^{\prime}$. En échangeant le rôle des indices 1 et 2, on voit que $X$ est bien $\varepsilon$-hypocontinue.

2° Supposons les  $L_{i}$  complets. Alors la propriété b) est entraînée par la propriété :

$b^{\prime}): \mathbf{H}$ est équicontinu sur tout produit de parties équicontinues des $\mathbf{L}_{i}^{\prime}$.

Voir corollaire 3 de la proposition 8.

$3^{\circ}$ La condition $b)$ relative à un ensemble H réduit à une seule forme $\vec{X}$ s'exprime uniquement à partir des topologies

faibles des  $L_{i}^{\prime}$ . En effet dire qu'une forme linéaire sur  $(\mathbf{L}_{i})_{c}^{\prime}$  est continue équivaut à dire qu'elle est continue sur  $\sigma(\mathbf{L}_{i}^{\prime}, \mathbf{L}_{i})$ , donc dire qu'une forme multilinéaire est séparément continue sur  $\prod_{i\in I}(\mathbf{L}_{i})_{c}^{\prime}$  équivaut à dire qu'elle est séparément faiblement

continue; d'autre part, sur les parties équicontinues de  $L_{i}^{\prime}$ ,  $(\mathbf{L}_{i})_{c}^{\prime}$  et  $\sigma(\mathbf{L}_{i}^{\prime}, \mathbf{L}_{i})$  induisent la même topologie, donc dire que  $\vec{X}$  est continue sur tout produit de parties équicontinues des  $L_{i}^{\prime}$ , pour la topologie induite par  $\prod_{i\in I}(\mathbf{L}_{i})_{c}^{\prime}$ , équivaut à dire qu'elle l'est pour les topologies faibles.

COROLLAIRE 1. — Soit M un espace vectoriel localement convexe (non nécessairement séparé ni quasi-complet). Pour qu'un ensemble H d'applications multilinéaires de $\prod_{i\in I}(\mathbf{L}_{i})_{e}^{\prime}$ dans M soit ε-équihypocontinu, il faut et il suffit que H soit séparément équicontinu, et que sa restriction à tout produit de parties équicontinues des L' soit équicontinu.

En effet, pour que H soit ε-équihypocontinu, ou séparément équicontinu, ou équicontinu sur tout produit de parties équicontinues des  $L_{i}^{\prime}$ , il faut et il suffit que, pour toute partie équicontinue  $M^{\prime}$  de  $M^{\prime}$ , l'ensemble (H;  $M^{\prime}$ ) de formes multilinéaires  $(\vec{l}_{i}^{\prime})_{i\in I}\rightarrow\left\langle\overrightarrow{X}\left(\left(\vec{l}_{i}^{\prime}\right)_{i\in I}\right),\overleftarrow{m^{\prime}}\right\rangle,\overrightarrow{X}\in H,\overleftarrow{m^{\prime}}\in\mathcal{M}^{\prime}$ , ait la même propriété.

Naturellement les propriétés de l'énoncé n'entraînent pas de propriété de compacité; pour $\left(\vec{l}_{i}\right)_{i\in I}$ donné, $\bigcup_{\vec{X}\in H}\overline{X}\left(\left(\vec{l}_{i}\right)_{i\in I}\right)$ n'est pas nécessairement relativement compact (voir page 32).

COROLLAIRE 2. — Si I est un ensemble de n indices, la forme  $(n+1)$  linéaire:  $\left(\left(\vec{l}_{i}\right)_{i\in\mathbb{I}},\vec{\mathrm{X}}\right)\rightarrow\mathrm{X}\left(\left(\vec{l}_{i}^{\prime}\right)_{i\in\mathbb{I}}\right)$ , sur  $\left(\prod_{i\in\mathbb{I}}\left(\mathrm{L}_{i}\right)_{c}^{\prime}\right)\times\mathrm{L}_{\mathbb{I}}$ , est hypocontinue par rapport aux parties équicontinues des  $L_{i}^{\prime}$  et aux parties compactes de  $L_{I}$ .

C'est une conséquence triviale de la définition de la topologie de  $L_{I}$ , et de l'équivalence de a) et c).

COROLLAIRE 3. — Soient $L_i$, $M_i$, des espaces localement convexes séparés dépendant du même ensemble d'indices, les $L_i$ étant quasi-complets. L'application multilinéaire $(u_i)_{i \in I} \to u_I$ de $\prod_{i \in I} \mathcal{L}_c(L_i; M_i)$ dans $\mathcal{L}_c(L_I; M_I)$ est $\varepsilon$-hypocontinue.

Soit $I = (1, 2 \ldots n)$. Nous allons montrer que si $u_{i}$ converge vers 0 dans $\mathcal{L}_{c}(L_{i}; M_{i})$ (c'est-à-dire uniformément sur toute partie compacte de $L_{i}$ puisque $L_{i}$ est quasi-complet), et que les $u_{i}, i = 2 \ldots n$, parcourent des parties équicontinues $H_{i}$ de $\mathcal{L}(L_{i}; M_{i})$, $u_{i}$ converge vers 0 uniformément sur toute partie compacte de $L_{i}$, donc dans $\mathcal{L}_{c}(L_{i}; M_{i})$. Soient $B_{i}'$, $i = 2 \ldots n$ des parties équicontinues des $M_{i}'$. Puisque les $H_{i}$ sont équicontinus, les $A_{i}' = \bigcup_{u_{i} \in H_{i}} {}^{t} u_{i}.B_{i}'$ sont des parties équicontinues des $L_{i}$. Soit maintenant $B_{i}'$ une partie équicontinue de $M_{i}'$; dire que $u_{i}$ converge vers 0 uniformément sur toute partie compacte de $L_{i}$, c'est dire que ${}^{t} u_{i} \in \mathcal{L}((M_{i})_{c}') ; (L_{i})_{c}')$ converge vers 0 uniformément sur toute partie équicontinue de $M_{i}'$, donc ${}^{t} u_{i}.B_{i}'$ converge vers 0 dans $(L_{i})_{c}'$.

Supposons alors que $\overline{\mathbf{X}}$ parcourt une partie compacte H de $\mathbf{L}_{\mathrm{I}}$. Cette partie est $\varepsilon$-équihypocontinue sur $\prod_{i\in\mathrm{I}}(\mathbf{L}_{i})_{c}^{\prime}$, puisque les $\mathbf{L}_{i}$ sont quasi-complets; donc $\vec{\mathbf{X}}\left(\left(^{t}u_{i}.\overleftarrow{m_{i}^{\prime}}\right)_{i\in\mathrm{I}}\right)$ converge vers 0 lorsque $u_{1}$ converge vers 0 dans $\mathcal{L}_{c}(\mathbf{L}_{1};\mathbf{M}_{1})$, uniformément pour $\vec{\mathbf{X}}\in\mathbf{H}$, $u_{i}\in\mathbf{H}_{i}$, $i=2\ldots n$, $\overleftarrow{m_{i}^{\prime}}\in\mathbf{B}_{i}^{\prime}$, $i=1,2,\ldots n$. Comme cette quantité n'est autre que $(u_{\mathrm{I}}.\vec{\mathbf{X}})\left(\left(\overleftarrow{m_{i}^{\prime}}\right)_{i\in\mathrm{I}}\right)$, cela prouve bien que $u_{\mathrm{I}}.\vec{\mathbf{X}}$ converge vers 0 dans $\mathbf{M}_{\mathrm{I}}$, uniformément pour $\mathbf{X}\in\mathbf{H}$, donc que $u_{\mathrm{I}}$ converge vers 0 dans $\mathcal{L}_{c}(\mathbf{L}_{\mathrm{I}};\mathbf{M}_{\mathrm{I}})$, c. q. f. d.

COROLLAIRE 4. — L'application multilinéaire canonique de $\prod_{i\in I}(\mathbf{L}_{i})_{c}^{\prime}$ dans $(\mathbf{L}_{1})_{c}^{\prime}$ est $\varepsilon$-hypocontinue et l'image par cette application d'un produit de parties équicontinues des $\mathbf{L}_{i}^{\prime}$ est une partie équicontinue de $\mathbf{L}_{1}^{\prime}$.

Soient $\vec{l}_{i}^{\prime}$ des éléments des $\mathbf{L}_{i}^{\prime}$. Ils définissent la forme linéaire continue $\vec{\mathbf{X}}\to\vec{\mathbf{X}}\left((\vec{l}_{i}^{\prime})_{i\in\mathbf{I}}\right)$ sur $\mathbf{L}_{\mathbf{I}}$, donc un élément de $\mathbf{L}_{\mathbf{I}}^{\prime}$. On définit ainsi une application multilinéaire dite canonique de $\prod_{i\in\mathbf{I}}(\mathbf{L}_{i})_{c}^{\prime}$ dans $(\mathbf{L}_{\mathbf{I}})_{c}^{\prime}$.

Soit $I = (1, 2, \ldots n)$. Si les $\vec{l}_i$, $i = 2 \ldots n$, parcourent des parties équicontinues des $L_i$, et que $\vec{l}_i'$ converge vers 0, $\vec{X} \left( (\vec{l}_i')_{i \in I} \right)$ converge vers 0, uniformément lorsque X parcourt une partie compacte de $L_I$, puisque cette partie est alors $\varepsilon$-équihypocon-

tinue d'après la proposition 2; donc l'image de $(\vec{l}_i')_{i\in}$ par l'application multilinéaire canonique converge vers 0 dans $(\mathrm{L_I})_c'$, ce qui prouve bien que cette application est $\varepsilon$-hypocontinue.

Si maintenant tous les $\vec{l}_{i}$, $i=1,2,\ldots n$, parcourent des parties équicontinues $\mathbf{A}_{i}^{\prime}$, et que $\vec{\mathbf{X}}$ converge vers 0 dans $\mathbf{L}_{\mathrm{I}}$, $\vec{\mathbf{X}}\left((\vec{l}_{i})_{i\in\mathrm{I}}\right)$ converge vers 0 d'après la définition de la topologie de $\mathbf{L}_{\mathrm{I}}$; donc l'image de $\prod_{i\in\mathrm{I}}\mathbf{A}_{i}^{\prime}$ par l'application multilineaire canonique est une partie équicontinue de $\mathbf{L}_{\mathrm{I}}^{\prime}$.

Remarque. — Seule l'ε-hypocontinuité de l'application multilinéaire canonique fait intervenir (par la proposition 2) le fait que les L$_{i}$ sont quasi-complets.

Parties bornées de $\varepsilon_{i\in I}(\mathbf{L}_{i};\mathbf{M})$

Soit $\vec{X} \in \underset{i \in I}{\varepsilon}(L_i; M)$; l'application multilinéaire $\vec{X}$, $\varepsilon$-hypocontinue de $\prod_{i \in I}(L_i)'_c$ dans $M$, est a fortiori $\varepsilon$-hypocontinue de $\prod_{i \in I}(L_i)'_b$ dans $M$. (La réciproque est inexacte). Nous avons vu (proposition 2) l'identité des parties relativement compactes de $L_I$ et des ensembles $\varepsilon$-équihypocontinus de formes multilinéaires sur $\prod_{i \in I}(L_i)'_c$ ($M =$ corps des scalaires); nous allons voir une propriété analogue relative aux parties bornées de $\underset{i \in I}{\varepsilon}(L_i; M)$, pour $M$ quelconque:

PROPOSITION 2 bis. — Il y a identité entre les parties bornées de $\varepsilon_{i\in I}(L_i; M)$ et les ensembles de cet espace qui sont $\varepsilon$-équihypocontinus de $\prod_{i\in I}(L_i)'_b$ dans M, même si les $L_i$ et M ne sont pas quasi-complets.

Soit en effet  $H \subset \varepsilon_{i \in I} (L_i; M)$ ,  $\varepsilon$ -équihypocontinu de  $\prod_{i \in I} (L_i)'_b$  dans M. Cela entraîne que H soit bornée sur tout produit  $\prod_{i \in I} A'_i$ , où l'une des  $A'_i \subset L'_i$  est fortement bornée, les autres équi-continues; a fortiori H est bornée sur tout produit de parties équicontinues des  $L'_i$ , donc bornée dans  $\varepsilon_{i \in I} (L_i; M)$ .

Réciproquement soit H une partie bornée de $\varepsilon_{i\in I}(\mathbf{L}_i;\mathbf{M})$. Supposons d'abord $\mathbf{M} = \mathbf{C}$, corps des scalaires. Soit $I = (1,2,\ldots,n)$, et supposons que $\widehat{l_i'}$ parcoure une partie équi- continue $\mathbf{A}_i'$ de $\mathbf{L}_i'$, pour $i\geqslant 2$. Alors $\overrightarrow{\mathbf{X}}\left(\prod_{i\in I}\mathbf{A}_i'\right)$ est borné, quelle que soit la partie équi continue $\mathbf{A}_i'$ de $\mathbf{L}_i'$, pour $\overrightarrow{\mathbf{X}}\in H$. Si $u_{\overrightarrow{\mathbf{X}}}$ est l'application de $\prod_{i=2}^{i=n}(\mathbf{L}_i)'_c$ dans $\mathbf{L}_i$ définie par $\overrightarrow{\mathbf{X}}$, ce qui précède prouve que $\bigcup_{\overrightarrow{\mathbf{X}}\in H}u_{\overrightarrow{\mathbf{X}}}^{\prime}\left(\prod_{i=2}^{i=n}\mathbf{A}_i'\right)$ est une partie de $\mathbf{L}_i$ bornée sur toute partie équi continue de $\mathbf{L}_i'$, donc bornée pour la topologie de $\mathbf{L}_i$; si alors $\widehat{l_i'}$ converge vers 0, $\mathbf{X}\left(\widehat{l_i'},\widehat{l_i'},\ldots,\widehat{l_n'}\right)$ convergera vers 0, uniformément pour $\widehat{l_i'}\in\mathbf{A}_i'$, $i\geqslant 2$. En faisant jouer à chacun des indices 2,..., $n$, le rôle que nous venons de faire jouer à l'indice 1, on voit bien que H est $\varepsilon$-équihypo continue sur $\prod_{i\in I}(\mathbf{L}_i)'_b$. Si M est quelconque, on remarquera que, quelle que soit la partie équi continue $\mathfrak{M}'$ de M', l'ensemble de formes multilinéaires $(\widehat{l_i'})_{i\in I}\to\langle\overrightarrow{\mathbf{X}}\left((\widehat{l_i'})_{i\in I}\right),m'\rangle,\quad\overrightarrow{\mathbf{X}}\in H,\quad\overleftarrow{m'}\in\mathfrak{M}'$, est borné dans $\mathbf{L}_i$, donc $\varepsilon$-équihypo continue sur $\prod_{i\in I}(\mathbf{L}_i)'_b$, ce qui prouve bien encore que H est $\varepsilon$-équihypo continue de $\prod_{i\in I}(\mathbf{L}_i)'_b$ dans M.

COROLLAIRE. — L'application multilinéaire canonique

$$
\left(\left(\vec {l} _ {i} ^ {\prime}\right) _ {i \in \mathbf {I}}, \vec {\mathrm{X}}\right)\rightarrow \vec {\mathrm{X}} \left(\left(\vec {l} _ {i} ^ {\prime}\right) _ {i \in \mathbf {I}}\right),
$$

de $\prod_{i\in I}(\mathbf{L}_{i})_{b}^{\prime}\times\underset{i\in I}{\varepsilon}(\mathbf{L}_{i};\mathbf{M})$ dans M, est hypocontinue par rapport aux parties équicontinues des $\mathbf{L}_{i}^{\prime}$ et aux parties bornées de $\underset{i\in I}{\varepsilon}(\mathbf{L}_{i};\mathbf{M})$, même si les $\mathbf{L}_{i}$ et M ne sont pas quasi-complets.

L'espace  $L_{I}$  est quasi-complet.

PROPOSITION 3. — L'espace $\mathbf{L}_{\mathbf{i}}$ est quasi-complet, et complet si les $\mathbf{L}_{\mathbf{i}}$ sont complets.

Soit en effet $\mathcal{F}$ un filtre de Cauchy sur $L_{i}$, borné (resp. quelconque). Pour la topologie de la convergence simple sur $\prod_{i\in I}L_{i}^{\prime}$, ce filtre converge vers une forme multilinéaire $\vec{X}$, du fait que le corps des scalaires est complet.

De plus, $\mathcal{F}$ converge vers $\vec{\mathbf{X}}$ uniformément sur tout produit de parties équicontinues des $L_{i}^{\prime}$. Il reste donc à montrer que $\vec{\mathbf{X}}$ est $\varepsilon$-hypocontinue. D'après la proposition 2, nous devons démontrer deux choses:

a) $\vec{\mathbf{X}}$ est continue sur tout produit de parties équicontinues des $\mathbf{L}_{i}^{\prime}$. Or cela résulte trivialement de ce que, sur un tel produit, $\vec{\mathbf{X}}$ est limite uniforme de fonctions continues.

b) $\vec{X}$ est séparément continue. Supposons, pour simplifier, $I = (1, 2, \ldots n)$. Fixons $\vec{l}_i' \in L_i'$, $i = 2, \ldots n$. L'image du filtre $\mathscr{F}$, par l'application continue de $L_I$ dans $L_1: \vec{X} \to u_{\vec{X}}(\vec{l}_2', \ldots \vec{l}_n')$ (voir notations de la démonstration de la proposition 2), est un filtre de Cauchy, borné (resp. quelconque), dans $L_1$. Comme $L_1$ est supposé quasi-complet (resp. complet), ce filtre est convergent dans $L_1$; comme il converge simplement vers $u_{\vec{X}}(\vec{l}_2', \ldots, \vec{l}_n')$ dans le dual algébrique de $L_1'$, on a $u_{\vec{X}}(\vec{l}_2', \ldots, \vec{l}_n') \in L_1$, donc $\vec{X}$ est bien séparément continue, c. q. f. d.

## Isomorphismes canoniques.

PROPOSITION 4. — Soient J et K deux sous-ensembles complémentaires de I (les $L_j$, $j \in J$ n'étant pas nécessairement quasi-complets). L'espace $L_I$ est canoniquement isomorphe, algébriquement et topologiquement, à $\varepsilon_{j \in J} (L_j; L_K)$. Les parties $\varepsilon$-équihypocontinues de $L_I$ sont $\varepsilon$-équihypocontinues dans $\varepsilon_{j \in J} (L_j; L_K)$; la réciproque est fausse en général.

Soit en effet $\overline{\mathbf{X}}$ un élément de $\mathrm{L}_{\mathrm{I}}$. A des $\widehat{l}_{j}^{\prime}$, $j \in \mathrm{J}$, donnés dans les $\mathrm{L}_{j}^{\prime}$, on peut associer la forme multilinéaire sur $\prod_{k \in \mathbb{K}} (\mathrm{L}_{k})_{c}^{\prime} : (\widehat{l}_{k}^{\prime})_{k \in \mathbb{K}} \to \overline{\mathbf{X}}\left((\widehat{l}_{i}^{\prime})_{i \in \mathbb{I}}\right)$, où $\widehat{l}_{i}^{\prime} = \widehat{l}_{j}^{\prime}$ pour $i = j \in \mathrm{J}$, et $\widehat{l}_{i}^{\prime} = \widehat{l}_{k}^{\prime}$ pour $i = k \in \mathrm{K}$. Cette forme multilinéaire est ε-hypocontinue; elle définit donc un élément $u_{\overline{\mathbf{X}}}^{\prime}\left((\widehat{l}_{j}^{\prime})_{j \in \mathbb{J}}\right)$ de $\mathrm{L}_{\mathbb{K}}$; $u_{\overline{\mathbf{X}}}^{\prime}$ est une application multilinéaire de $\prod_{j \in \mathbb{J}} (\mathrm{L}_{j})_{c}^{\prime}$ dans $\mathrm{L}_{\mathbb{K}}$. Cette application multilinéaire $u_{\overline{\mathbf{X}}}^{\prime}$ est ε-hypocontinue; en effet si l'un des éléments $\widehat{l}_{j}^{\prime}$ converge vers 0 et que les autres parcourent des parties équicontinues, $\overline{\mathbf{X}}\left((\widehat{l}_{i}^{\prime})_{i \in \mathbb{I}}\right)$ converge vers 0, unifor-

mément lorsque les $\vec{l}_{k}^{\prime}$, $k\in K$, parcourent des parties équicontinues, d'après la définition même de $\vec{X}$ comme forme multilinéaire $\varepsilon$-hypocontinue sur $\prod_{i\in I}(L_{i})_{c}^{\prime}$; cela revient précisément à dire que $u_{\vec{X}}\big((\vec{l}_{j}^{\prime})_{j\in J}\big)$ converge vers 0 dans $L_{K}$. Nous avons donc bien associé à tout élément $\vec{X}$ de $L_{I}$ une application multilinéaire $\varepsilon$-hypocontinue $u_{\vec{X}}$ de $\prod_{j\in J}(L_{j})_{c}^{\prime}$ dans $L_{K}$, c'est-à-dire un élément $u_{\vec{X}}$ de $\varepsilon_{j\in J}(L_{j};L_{K})$. Alors $\vec{X}\to u_{\vec{X}}$ est une application linéaire $u$ de $L_{I}$ dans $\varepsilon(L_{j};L_{K})$. Cette application est trivialement injective; si $u_{\vec{X}}=0$, cela veut dire que, pour tout système $(\vec{l}_{j}^{\prime})_{j\in J}$, $u_{\vec{X}}\big((\vec{l}_{j}^{\prime})_{j\in J}\big)$ est l'élément nul de $L_{K'}$, donc nul sur tout système $(\vec{l}_{k}^{\prime})_{k\in K}$, c'est-à-dire que $\vec{X}\big((\vec{l}_{i}^{\prime})_{i\in I}\big)=0$ pour tout système $(\vec{l}_{i}^{\prime})_{i\in I}$, autrement dit que $\vec{X}$ est l'élément nul de $L_{I}$. On peut donc identifier $L_{I}$ à un sous-espace vectoriel de $\varepsilon(L_{j};L_{K})$.

$$
\mathbf {L} _ {\mathrm{I}}
$$

$$
\varepsilon_ {j \in \mathbf {J}} (\mathrm{L} _ {j}; \mathrm{L} _ {\mathbf {K}})
$$

$$
\vec {\mathbf {X}}
$$

$$
\mathbf {L} _ {\mathrm{I}}
$$

$$
\mathbf {c} ^ {\prime}
$$

$$
\vec {X} \left(\left(\vec {l _ {i} ^ {\prime}}\right) _ {i \in \mathbf {I}}\right)
$$

$$
\vec {l} _ {i} ^ {\prime}
$$

$$
\mathbf {L} _ {i} ^ {\prime};
$$

$$
u _ {\overline {{X}}} \left(\left(\overleftarrow {l} _ {j} ^ {\prime}\right) _ {j \in J}\right)
$$

$$
\vec {l} _ {j} ^ {\prime}
$$

$$
\mathbf {L} _ {\mathbf {K}},
$$

$$
\mathrm{L} _ {j} ^ {\prime}.
$$

$$
\mathrm{L} _ {\mathrm{I}} = \varepsilon_ {i \in \mathrm{I}} (\mathrm{L} _ {j}; \mathrm{L} _ {\mathbf {K}})
$$

Soit alors Y un élément de $\varepsilon(L_{j}; L_{K})$.

Il définit une forme multilinéaire $\vec{X}$ sur $\prod_{i\in I} (L_i)'_c$, prenant pour valeur sur $(\vec{l}_i')_{i\in I}$ la valeur de $\vec{Y}((\vec{l}_j')_{j\in J}) \in L_K$ sur $(\vec{l}_k')_{k\in K} \in \prod_{k\in K} L_k'$. On a précisément $Y = u_{\vec{X}}$, et il nous reste à voir que $\vec{X} \in L_I$, autrement dit que la forme multilinéaire $\vec{X}$ sur $\prod_{i\in I} (L_i)'_c$ est $\varepsilon$-hypocontinue. Soit donc $\alpha$ un élément de I, et supposons que $\vec{l}_\alpha'$ converge vers 0 dans $(L_\alpha)'_c$, et que les $\vec{l}_i'$, $i \neq \alpha$, restent dans des parties équicontinues $A_i'$ des $L_i'$, parties que nous pouvons supposer faiblement fermées, donc compactes; nous devons

montrer que $\vec{\mathbf{X}}\big((\vec{l}_{i}^{\prime})_{i\in\mathbf{I}}\big)$ converge vers 0. Si $\alpha\in\mathbf{J}$, c'est évident; car alors $\vec{\mathbf{Y}}\big((\vec{l}_{j}^{\prime})_{j\in\mathbf{J}}\big)$ converge vers 0 dans $\mathbf{L}_{\mathbf{K}}$, puisque $\vec{\mathbf{Y}}$ est une application $\varepsilon$-hypocontinue; cela entraîne bien, étant donné la définition de la topologie de $\mathbf{L}_{\mathbf{K}}$, que $\vec{\mathbf{Y}}\big((\vec{l}_{j}^{\prime})_{j\in\mathbf{J}}\big)$ converge vers 0 uniformément sur $\prod_{k\in\mathbf{K}}\mathbf{A}_{k}^{\prime}$. Supposons donc $\alpha\in\mathbf{K}$. L'image B de $\prod_{j\in\mathbf{J}}\mathbf{A}_{j}^{\prime}$ par $\vec{\mathbf{Y}}$ est une partie compacte de $\mathbf{L}_{\mathbf{K}}$; en effet $\vec{\mathbf{Y}}$ est continue sur $\prod_{j\in\mathbf{J}}\mathbf{A}_{j}^{\prime}$, et cette partie est compacte dans $\prod_{j\in\mathbf{J}}(\mathbf{L}_{j})_{c}^{\prime}$. Alors d'après la proposition 2 (qui suppose que les $\mathbf{L}_{k}$, $k\in\mathbf{K}$, sont quasi-complets), B est $\varepsilon$-hypocontinue sur $\prod_{k\in\mathbf{K}}(\mathbf{L}_{k})_{c}^{\prime}$, ce qui prouve bien que $\vec{\mathbf{X}}\big((\vec{l}_{i}^{\prime})_{i\in\mathbf{I}}\big)$ converge encore vers 0. L'isomorphisme algébrique et topologique de $\mathbf{L}_{\mathbf{I}}$ et de $\varepsilon_{j\in\mathbf{J}}(\mathbf{L}_{j};\mathbf{L}_{\mathbf{K}})$ est donc démontré.

Remarques. — 1° Si $\overline{\mathbf{X}}$ parcourt un ensemble ε-équihypocontinu de formes multilinéaires sur $\prod_{i\in I}(\mathrm{L}_{i})_{c}^{\prime}$, $u_{\overline{\mathbf{X}}}$ parcourt évidemment un ensemble ε-équihypocontinu d'applications multilinéaires de $\prod_{i\in I}(\mathrm{L}_{j})_{c}^{\prime}$ dans $\mathrm{L}_{\mathbf{K}}$.

La réciproque n'est pas exacte. Soient par exemple, I = (1, 2), J = (1), K = (2). Si $u_{\widetilde{X}}$ parcourt un ensemble H équicontinu d'applications de $(\mathrm{L}_1)_c'$ dans $\mathrm{L}_2$, cela n'entraîne pas que pour toute partie équicontinue $\mathrm{A}_1'$ de $\mathrm{L}_1'$, $\bigcup_{u_{\widetilde{X}} \in \mathrm{H}} u_{\widetilde{X}}(\mathrm{A}_1')$ soit une

partie relativement compacte de  $L_{2}$ , ce qui serait nécessaire pour que les  $\overrightarrow{X}$  correspondant à  $u_{\overrightarrow{X}} \in H$  parcourent un ensemble  $\varepsilon$ -équihypocontinu de formes multilinéaires sur  $(\mathbf{L}_{1})_{c}^{\prime} \times (\mathbf{L}_{2})_{c}^{\prime}$ . Cela n'entraîne même pas que, pour tout  $\vec{l}_{1}^{\prime} \in L_{1}^{\prime}, \bigcup_{x_{\overrightarrow{X}} \in H} u_{\overrightarrow{X}}(\vec{l}_{1}^{\prime})$  soit relativement compact dans  $L_{2}$ .

Prenons par exemple un espace de Banach N de dimension infinie. Alors  $(\mathrm{N}_{c}^{\prime})_{c}^{\prime}=\mathrm{N}$  (voir page 17). Prenons  $L_{2}=N$,  $L_{1}=N_{c}^{\prime}$, donc  $\mathcal{L}((\mathrm{L}_{1})_{c}^{\prime};\mathrm{L}_{2}))=\mathcal{L}(\mathrm{N};\mathrm{N})$. L'ensemble H des endomorphismes  $\nu$  de N de norme  $\leqslant1$  est équicontinu, et, pour  $\vec{n}\in N$,  $\bigcup_{CV}\nu(\vec{n})$  n'est pas relativement compacte dans N.

$2^{0} \text{ Le cas où } I = (1, 2; \ldots n), J = (2, \ldots n), K = (1) \text{ avait}$

été partiellement vu dans la démonstration de la proposition 2. Mais dans le cas général, nous avons besoin de savoir que toute partie relativement compacte de $L_{K}$ est $\varepsilon$-équihypocontinue sur $\prod_{i\in K} (L_k)'_c$, c'est-à-dire précisément la proposition 2.

3° Si les  $L_{K}$ ,  $k \in K$ , ne sont pas quasi-complets, on peut seulement affirmer que  $L_{I}$  est un sous-espace vectoriel topologique de  $\varepsilon$  ( $L_{j}$ ;  $L_{K}$ ). Cependant des ceux espaces sont identiques si I est réduit à deux éléments j, k, avec  $J = (j)$ ,  $K = (k)$ . En effet en reprenant les notations de la démonstration, on peut toujours supposer que la partie équicontinue choisie  $A_{j}'$  est convexe équilibrée compacte dans  $(\mathbf{L}_{j})_{c}'$ . Alors  $\overrightarrow{\mathbf{Y}}(\mathbf{A}_{j}')$  est une partie convexe équilibrée compacte de  $L_{k}$ , donc équicontinue sur  $(\mathbf{L}_{k})_{c}'$  même si  $L_{k}$  n'est pas quasi-complet; cela prouve que  $\overline{X}$  est ε-hypocontinue, et  $L_{I} = \varepsilon(\mathbf{L}_{j}; \mathbf{L}_{k}) = \mathcal{L}_{\varepsilon}((\mathbf{L}_{j})_{c}'; \mathbf{L}_{k})$ .

4° Soient  $L_{i}$ ,  $M_{i}$ , des espaces dépendant du même ensemble d'indices I,  $u_{i}$  des applications linéaires continues des  $L_{i}$  dans les  $M_{i}$ , J et K deux sous-ensembles complémentaires de I (les  $L_{j}$  et  $M_{j}$ ,  $j \in J$ , n'étant pas nécessairement quasi-complets). Si l'on identifie  $L_{I}$  (resp.  $M_{I}$ ) à  $\varepsilon_{j \in J}(L_{j}; L_{K})$  (resp.  $\varepsilon_{j \in J}(M_{j}; M_{K})$ ), l'application  $u_{I}$  de  $L_{I}$  dans  $M_{I}$  (proposition 1) définit une application  $u_{I}$  de  $\varepsilon_{j \in J}(L_{j}; L_{K})$  dans  $\varepsilon_{j \in J}(M_{j}; M_{K})$ . Pour  $\vec{X} \in \varepsilon_{j \in J}(L_{j}; L_{K})$ ,  $u_{I} \cdot \vec{X}$  est l'élément de  $\varepsilon_{j \in J}(M_{j}; M_{K})$  définissant l'application  $(\overleftarrow{m}_{f}')_{j \in J} \to u_{K} \cdot [\overrightarrow{X}\big((\prime u_{j}, \overleftarrow{m}_{j})_{j \in J}\big)]$  de  $\prod_{j \in J}(M_{j})'$  dans  $M_{K}$ .

5° Soient $\vec{l}_{j}^{\prime}, j \in J$, des éléments des $L_{j}^{\prime}$. Ce sont des applications linéaires continues des $L_{j}$ dans le corps des scalaires C. Alors $\otimes \left((\vec{l}_{j}^{\prime})_{j \in J}, (I_{k})_{k \in K}\right)(I_{k} = \text{opérateur identique de } L_{k})$ est, d'après la proposition 1, une application linéaire continue de $L_{I}$ dans $\varepsilon \left( \underbrace{C, C, \ldots C}_{j \in J}, (L_{k})_{k \in K} \right) = L_{K}$. Cette application n'est autre que $\vec{X} \to u_{\vec{X}}^{\times} \left( (\vec{l}_{j}^{\prime})_{j \in J} \right)$, définie dans la démonstration. Il suffit pour le voir d'appliquer la définition de l'opérateur $\otimes u_{i}$ donnée dans la proposition 1.

COROLLAIRE 1. — L'espace $\varepsilon_{i\in\mathbf{I}}(\mathrm{L}_{i};\mathrm{M})$ est isomorphe, algébriquement et topologiquement, à $\varepsilon((\mathrm{L}_{i})_{i\in\mathbf{I}},\mathrm{M})=\underset{i\in\mathbf{I}_{0}}{\varepsilon}\mathrm{L}_{i}$, produit $\varepsilon$

relatif à un ensemble d'indices I₀, somme de I et d'un élément ω, avec Lω = M. Il est quasi-complet, et complet si les Lᵢ et M sont complets. Les parties compactes de ε (Lᵢ; M) sont ε-équihypocontinues; la réciproque est fausse en général. L'application multilinéaire ((l̂ᵢ)ᵢ∈I, X) → X((l̂ᵢ)ᵢ∈I) de ∏ᵢ∈I (Lᵢ)′ × εᵢ∈I (Lᵢ; M) dans M est hypocontinue par rapport aux parties équicontinues des Lᵢ′ et aux parties compactes de ε (Lᵢ; M). L'image par cette application d'un produit de parties équicontinues des Lᵢ′ et d'une partie relativement compacte de ε (Lᵢ; M) est relativement compacte dans M.

Il suffit d'appliquer la proposition à  $L_{I_{0}}$ , avec J = I,  $k = \{\omega\}$ . Ensuite on remarque que les parties compactes de  $\varepsilon_{i \in I}(L_{i}; M)$  sont compactes dans  $L_{I_{0}}$ , donc  $\varepsilon$ -équihypocontinues, donc sont des parties  $\varepsilon$ -équihypocontinues de  $\varepsilon_{i \in I}(L_{i}; M)$  d'après la proposition, et la réciproque est fausse en général. L'application multilinéaire considérée est hypocontinue par rapport aux parties équicontinues des  $L_{i}'$  et aux parties  $\varepsilon$ -équihypocontinues de  $\varepsilon_{i \in I}(L_{i}; M)$  donc a fortiori par rapport aux parties équicontinues  $A_{i}'$  des  $L_{i}'$  et aux parties relativement compactes H de  $\varepsilon(L_{i}; M)$ ; elle est alors continue sur  $\prod_{i \in I} \overline{A}_{i}' \times \overline{H}$ , et comme cette partie est compacte, son image est compacte dans M.

COROLLAIRE 2. — Si L et M sont des espaces vectoriels localement convexes séparés (non nécessairement quasi-complets), on a des isomorphismes canoniques

$$
\mathbf {L} \varepsilon \mathbf {M} \approx \mathscr {L} _ {\varepsilon} (\mathbf {L} _ {c} ^ {\prime}; \mathbf {M}) \approx \mathscr {L} _ {\varepsilon} (\mathbf {M} _ {c} ^ {\prime}; \mathbf {L}),
$$

$\mathcal{L}_{\epsilon}(L_{c}^{\prime}; M)$ étant l'espace des applications linéaires continues de $L_{c}^{\prime}$ dans M, muni de la topologie de la convergence uniforme sur les parties équicontinues de $L^{\prime}$.

Il suffit d'appliquer la proposition 4 au cas d'un ensemble I réduit à 2 éléments, J et K ayant un élément. La remarque 3 montre que L et M n'ont pas besoin d'être quasi-complets. Étant donné l'importance de ce cas particulier, il n'est pas inutile de détailler ces isomorphismes. Si $\overrightarrow{\mathbf{X}}\in\mathbf{L}\varepsilon\mathbf{M}$, son

image $u_{\mathbf{x}}$ dans $\mathcal{L}(\mathbf{L}_{c}^{\prime}; \mathbf{M})$ est l'application linéaire continue de $\mathbf{L}_{c}^{\prime}$ dans $\mathbf{M}$ définie par

$$
\langle u _ {\vec {X}} (\vec {l ^ {\prime}}), \overleftrightarrow {m ^ {\prime}} \rangle = \vec {X} (\vec {l ^ {\prime}}, \overleftrightarrow {m ^ {\prime}}) \quad \text { pour } \quad \vec {l ^ {\prime}} \in L ^ {\prime}, \overleftrightarrow {m ^ {\prime}} \in M ^ {\prime}. \tag {I,1;3}
$$

Son image $u_{\vec{\mathbf{x}}}$ dans $\mathfrak{L}(\mathbf{M}_{c}^{\prime}; \mathbf{L})$ est l'application linéaire continue de $\mathbf{M}_{c}^{\prime}$ dans $\mathbf{L}$ définie par

$$
(\mathrm{I}, 1; 4) \langle^ {\prime} u _ {\vec {\mathbf {X}}} (\overleftarrow {m ^ {\prime}}), \overleftarrow {l ^ {\prime}} \rangle = \overrightarrow {\mathrm{X}} (\overleftarrow {l ^ {\prime}}, \overleftarrow {m ^ {\prime}}) \quad \text { pour } \quad \overleftarrow {l ^ {\prime}} \in \mathrm{L} ^ {\prime}, \overleftarrow {m ^ {\prime}} \in \mathrm{M} ^ {\prime}.
$$

L'isomorphisme entre $\mathcal{L}_{\varepsilon}(\mathbf{L}_{c}^{\prime};\mathbf{M})$ et $\mathcal{L}_{\varepsilon}(\mathbf{M}_{c}^{\prime};\mathbf{L})$ est défini par la transposition $u\to{}^{t}u$.

Remarques. — 1° Si L₁, L₂, M₁, M₂, sont des espaces localement convexes séparés (non nécessairement quasi-complets), si u₁ (resp. u₂) est une application linéaire continue de L₁ dans M₁ (resp. de L₂ dans M₂), l'image de $\vec{X} \in \mathcal{L}((\mathrm{L}_1)_c'; \mathrm{L}_2)$ par u₁ ⊗ u₂ (proposition 1) est l'élément (u₁ ⊗ u₂). ($\vec{X}$) de $\mathcal{L}((\mathrm{M}_1)_c'; \mathrm{M}_2)$ égal à u₂∘$\vec{X}\circ^t u_1$ (voir remarque 4 page 33). L'image de $^\prime\vec{X} \in \mathcal{L}((\mathrm{L}_2)_c'; \mathrm{L}_1)$ par u₁ ⊗ u₂ est l'élément (u₁ ⊗ u₂). $^\prime\vec{X}$ de $\mathcal{L}((\mathrm{M}_2)_c'; \mathrm{M}_1)$ égal à u₁∘$^\prime\vec{X}\circ^t u_2$.

2° Quand nous avons étudié  $L_{1}$ , l'ensemble d'indices I n'était pas ordonné. Quand nous écrivons  $L\varepsilon M$ , l'ensemble I à 2 éléments, et il est ordonné. Il y a donc lieu de distinguer  $L\varepsilon M$  et  $M\varepsilon L$ , qui sont canoniquement isomorphes mais non identiques (de même que  $L \times M$  ou  $L \otimes M$ ). L'isomorphisme entre ces 2 espaces sera appelé symétrie, et jouera un rôle important au § 4 (pages 90 à 96). Si  $u_{1}$  (resp.  $u_{2}$ ) est une application continue de  $L_{1}$  dans  $M_{1}$  (resp. de  $L_{2}$  dans  $M_{2}$ ), la symétrie transforme l'application  $u_{1} \otimes u_{2}$  de  $L_{1}\varepsilon L_{2}$  dans  $M_{1}\varepsilon M_{2}$  en l'application  $u_{2} \otimes u_{1}$  de  $L_{2}\varepsilon L_{1}$  dans  $M_{2}\varepsilon M_{1}$ . En particulier, si  $L_{1}$  (resp.  $L_{2}$ ) est un sous-espace de  $M_{1}$  (resp.  $M_{2}$ ), la symétrie  $M_{1}\varepsilon M_{2} \to M_{2}\varepsilon M_{1}$  induit la symétrie  $L_{1}\varepsilon L_{2} \to L_{2}\varepsilon L_{1}$ .

Nous avons donné ailleurs des propriétés diverses de ces espaces $\mathcal{L}_{\epsilon}(\mathrm{L}_{c}^{\prime};\mathrm{M}),\mathcal{L}_{\epsilon}(\mathrm{M}_{c}^{\prime};\mathrm{L})(^{1})$.

Rappelons seulement la suivante :

PROPOSITION 5. — Pour qu'une application linéaire u de L$_{e}$ dans M soit continue (L et M non nécessairement quasi-complets), il faut et il suffit qu'elle soit continue pour les topologies faibles

(3) Schwartz [1], page 125.

$\sigma(\mathbf{L}',\mathbf{L})$ et $\sigma(\mathbf{M},\mathbf{M}')$, et que sa restriction aux parties équi- continues de $\mathbf{L}'$ soit continue de $\mathbf{L}_{c}'$ (ou $\sigma(\mathbf{L}',\mathbf{L})$) dans $\mathbf{M}$; il faut et il suffit aussi qu'elle soit continue de $\sigma(\mathbf{L}',\mathbf{L})$ dans $\sigma(\mathbf{M},\mathbf{M}')$ et que l'image par u de toute partie équicontinue de $\mathbf{L}'$ soit relativement compacte dans $\mathbf{M}$.

Les deux conditions données sont trivialement nécessaires. Car si $u$ est continue de $L_c'$ dans M, elle est continue pour les topologies affaiblies; comme le dual de $L_c'$ est L, ce sont précisément $\sigma(L', L)$ et $\sigma(M, M')$; par ailleurs, sur les parties équicontinues de $L'$, les topologies $L_c'$ et $\sigma(L', L)$ sont identiques, d'après le théorème d'Ascoli; enfin les parties équicontinues disquées de $L_c'$ sont compactes. Montrons qu'elles sont suffisantes. Si $u$ est continue de $\sigma(L', L)$ dans $\sigma(M, M')$, sa transposée 'u est continue de $\sigma(M', M)$ dans $\sigma(L, L')$. Si de plus la restriction de $u$ aux parties équicontinues de $L'$ est continue de $L_c'$ dans M, l'image par $u$ d'une partie équicontinue convexe équilibrée faiblement fermée donc compacte est convexe équilibrée compacte dans M. Alors 'u est continue de $M_c'$ dans L; et de 'u ∈ ℒ($M_c'$; L) on déduit u ∈ ℒ($L_c'$; M), c.q.f.d.

Remarque. — Si $u$ est continue de $\mathbf{L}_{c}^{\prime}$ dans M, elle est même continue de $\mathbf{L}_{c}^{\prime}$ dans $(\mathbf{M}_{c}^{\prime})_{c}^{\prime}$, topologie plus fine que L (voir page 17). En effet elle est la transposée "u de 'u, application continue de $\mathbf{M}_{c}^{\prime}$ dans L. On peut encore dire ceci: Si $u$ est continue de N dans M, elle est continue pour les topologies $\gamma$ associées, c'est-à-dire de $(\mathbf{N}_{c}^{\prime})_{c}^{\prime}$ dans $(\mathbf{M}_{c}^{\prime})_{c}^{\prime}$: en effet elle est la transposée "u de 'u, continue de $\mathbf{M}_{c}^{\prime}$ dans $\mathbf{N}_{c}^{\prime}$. Si alors N a la topologie $\gamma$, c'est-à-dire si $\mathbf{N} = \mathbf{L}_{c}^{\prime}$, u est continue de N dans $(\mathbf{M}_{c}^{\prime})_{c}^{\prime}$.

Ainsi, quels que soient L et M (non nécessairement quasi-complets), LεM et Lε(Mc')c' sont algébriquement identiques, mais le deuxième a une topologie plus fine, et identique si M a la topologie γ.

COROLLAIRE. — Si L et M sont des espaces localement convexes séparés (non nécessairement quasi-complets), l'espace $\mathfrak{L}_{\mathrm{c}}(\mathrm{L};\mathrm{M})$ des applications linéaires continues de L dans M, muni de la topologie de la convergence uniforme sur les parties convexes équilibrées compactes de L, est canoniquement isomorphe à un sous-espace vectoriel topologique de $\mathrm{L}_{\mathrm{c}}^{\prime}\in\mathrm{M}$, et à cet espace tout

entier si L a la topologie $\gamma$; $\mathbf{L}_{c}^{\prime}\varepsilon\mathbf{M}$ est canoniquement isomorphe à $\mathcal{L}_{\varepsilon}(\mathbf{M}_{c}^{\prime};\mathbf{L}_{c}^{\prime})$.

Le dernier isomorphisme est un résultat immédiat du corollaire 2 de la proposition 4. D'après ce même corollaire, $L_c' \in M$ est isomorphe à $\mathscr{L}_{\epsilon}((L_c')_c'; M)$; comme $(L_c')_c'$ est identique à $L$ mais avec une topologie plus fine, et avec la même topologie si $L$ a la topologie $\gamma$ (page 17), on a bien $\mathscr{L}(L; M) \subset L_c' \in M$ et $= \mathscr{L}_c' \in M$ si $L$ a la topologie $\gamma$. La topologie induite par $L_c' \in M$ sur $\mathscr{L}(L; M)$ est celle de la convergence uniforme sur les parties équicontinues de $(L_c')',$ ou encore sur les parties convexes équilibrées compactes de $L$; c'est donc bien par définition la topologie $\mathscr{L}_c(L; M)$.

## Associativité du produit ε.

PROPOSITION 6. — Le produit tensoriel $\otimes_{i\in I} L_i'$ est un sous-espace strictement dense de $(L_I)_c'$; pour qu'une partie de $L_I'$ soit équi-continue, il faut et il suffit qu'elle soit contenue dans l'enveloppe d'un produit tensoriel de parties équicontinues des $L_i'$.

L'application multilinéaire canonique de $\prod_{i\in I} L_i'$ dans $L_I'$ (corollaire 4 de la proposition 2) définit une application linéaire canonique de $\otimes_{i\in I} L_i'$ dans $L_I'$. Cette application est injective; si en effet l'image par cette application d'un élément $\overleftarrow{\lambda'}$ de $\otimes_{i\in I} L_i'$ est nulle, on a $\langle \overleftarrow{\lambda'}, X\rangle = 0$ pour $\overrightarrow{X} \in L_I$ et a fortiori pour $\overrightarrow{X} \in \otimes_{i\in I} L_i$; ce qui suffit déjà à assurer que $\overleftarrow{\lambda'} = 0$ (voir page 19). On peut donc considérer $\otimes_{i\in I} L_i'$ comme un sous-espace de $L_I'$. Si les $A_i'$ sont des parties équicontinues des $L_i', \otimes_{i\in I} A_i'$ est une partie équicontinue de $L_I'$ (corollaire 4 de la proposition 2). Réciproquement, soit $A'$ une partie équicontinue de $L_I'$. Son polaire $A'^0$ dans $L_I$ est un voisinage de 0; il existe donc, d'après la définition de la topologie de $L_I$, des parties équicontinues $A_i'$ des $L_i'$ telles que $\left|\overrightarrow{X}\left(\prod_{i\in I} A_i'\right)\right| \leqslant 1$ entraîne $\overrightarrow{X} \in A'^0$; cela prouve que $A'^0$ contient le polaire $(\otimes_{i\in I} A_i')^0$ de $\otimes_{i\in I} A_i' \subset L_I'$, alors $A'$ est contenu dans le bipolaire $(\otimes_{i\in I} A_i')^{00}$ de $\otimes_{i\in I} A_i'$.

Ce bipolaire est l'enveloppe convexe équilibrée faiblement fermée de $\otimes_{i\in I}A_{i}^{\prime}$; mais le dual de $(L_{I})_{c}^{\prime}$ étant $L_{I}$, il en est aussi l'enveloppe convexe équilibrée fermée pour la topologie de $(L_{I})_{c}^{\prime}$.

En particulier tout point de  $L_{I}^{\prime}$  est contenu dans l'enveloppe d'une partie  $\otimes A_{i}^{\prime}$ ; cette partie est équicontinue dans  $L_{I}^{\prime}$  donc bornée dans  $(\mathbf{L}_{\mathbf{I}})_{c}^{\prime}$ , ce qui prouve que  $\otimes L_{i}^{\prime}$  est strictement dense dans  $(\mathbf{L}_{\mathbf{I}})_{c}^{\prime}$ , c. q. f. d.

PROPOSITION 7 (Associativité). — Soit $(\mathrm{I}_{\lambda})_{\lambda \in \Lambda}$ une partition de l'ensemble d'indices I. Il existe un isomorphisme canonique, algébrique et topologique, entre $\mathrm{L}_{\mathrm{I}} = \underset{i \in \mathrm{I}}{\varepsilon} \mathrm{L}_{i}$ et $\underset{\lambda \in \Lambda}{\varepsilon} \mathrm{L}_{\mathrm{I}_{\lambda}} = \underset{\lambda \in \Lambda}{\varepsilon} \left( \underset{i \in \mathrm{I}_{\lambda}}{\varepsilon} \mathrm{L}_{i} \right)$.

Cet isomorphisme associe les ensembles $\varepsilon$-équihypocontinus de formes multilinéaires sur $\prod_{i\in I}(\mathbf{L}_{i})_{c}^{\prime}$ et les ensembles $\varepsilon$-équihypocontinus de formes multilinéaires sur $\prod_{i\in I}(\mathbf{L}_{I_{k}})_{c}^{\prime}$.

Soit en effet $\vec{X} \in \varepsilon L_{I_{\lambda}}$. $\vec{X}$ est une forme multilinéaire sur $\prod_{\lambda \in \Lambda} (L_{I_{\lambda}})'_c$. Désignons par $\theta_{\lambda}$ l'application multilinéaire canonique de $\prod_{i \in I_{\lambda}} (L_i)'_c$ dans $(L_{I_{\lambda}})'_c$ (corollaire 4 de la proposition 2). Alors $(\vec{l}_i')_{i \in I} \to \vec{X}\left(\left(\theta_{\lambda}\left((\vec{l}_i')_{i \in I_{\lambda}}\right)\right)_{\lambda \in \Lambda}\right)$ est une forme multilinéaire $\widetilde{\vec{X}}$ sur $\prod_{i \in I} (L_i)'_c$. Si l'un des $(\vec{l}_i')$ converge vers 0 et que les autres parcourent des parties équicontinues, l'un des $\theta_{\lambda}\left((\vec{l}_i')_{i \in I_{\lambda}}\right)$ converge vers 0 et les autres parcourent des parties équicontinues, puisque $\theta_{\lambda}$ est ε-hypocontinue et qu'elle applique tout produit de parties équicontinues des $L_i'$, $i \in I_{\lambda}$, dans une partie équicontinue de $(L_{I_{\lambda}})'_c$; donc, $\vec{X}$ étant ε-hypocontinue, $\widetilde{\vec{X}}\left((\vec{l}_i')_{i \in I}\right)$ converge vers 0, autrement dit $\widetilde{\vec{X}}$ est ε-hypocontinue, $\widetilde{\vec{X}} \in L_I$.

L'application linéaire $\overrightarrow{\mathbf{X}}\to\overrightarrow{\mathbf{X}}$ de $\varepsilon_{\lambda\in\Lambda}\mathbf{L}_{\mathbf{I}_{\lambda}}$ dans $\mathbf{L}_{\mathbf{I}}$ est injective; si en effet $\widetilde{\overline{\mathbf{X}}} = 0$, cela prouve que $\overline{\mathbf{X}}$ est nulle sur le sous-espace $\prod_{\lambda\in\Lambda}\left(\bigotimes_{i\in\mathbf{I}_{\lambda}}\mathbf{L}_{i}^{\prime}\right)$ de $\prod_{\lambda\in\Lambda}\langle\mathbf{L}_{\mathbf{I}_{\lambda}}\rangle_{c}^{\prime}$; comme $\otimes_{i\in\mathbf{I}_{\lambda}}\mathbf{L}_{i}^{\prime}$ est dense dans $(\mathbf{L}_{\mathbf{I}_{\lambda}})_{c}^{\prime}$ (proposition 6), cela entraîne $\overline{\mathbf{X}} = 0$.

Cette application $\overrightarrow{\mathbf{X}}\to\overrightarrow{\mathbf{X}}$ est aussi épijective. Soit en effet $\overrightarrow{\mathbf{Y}}$ une forme multilinéaire $\varepsilon$-hypocontinue sur $\prod_{i\in\mathbf{I}}(L_i)'$; elle définit une forme multilinéaire $\overrightarrow{\mathbf{Y}}_0$ sur $\prod_{\lambda\in\Lambda}\left(\otimes L_i'\right)$; montrons que cette application $\overrightarrow{\mathbf{Y}}_0$ est $\varepsilon$-hypocontinue (en appelant partie équicontinue de $\otimes L_i'$, un produit tensoriel de parties équicontinues des $L_i'$, et en munissant $\otimes L_i'$ de la topologie induite par $(L_{I_\lambda})'_c$. Soit $\Lambda=(1,2,\ldots m)$. Supposons que $\vec{\rho}_{\lambda}'$, pour $\lambda=2,\ldots m$, parcoure une partie équicontinue de $\otimes L_j'$, c'est-à-dire un produit $\otimes A_j'$, les $A_j'$ étant des parties équicontinues compactes des $(L_j)'_c$. Supposons d'autre part que $\vec{\rho}_1' \in \otimes L_k'$ converge vers 0, pour la topologie induite par $(L_{I_i})'_c$. Pour tout système de $\vec{l}_j' \in L_j'$, $j \in \bigcap_{\lambda=2,\ldots,m} I_\lambda$, appelons $u_{\overline{\mathbf{Y}}}^{\prime}\left(\left(\vec{l}_j'\right)_j \in \{I_i'\}\right)$ la forme multilinéaire sur $\prod_{k \in I_i'} (L_k)'_c: \left(\vec{l}_k'\right)_{k \in I_i'} \to \overline{\mathbf{Y}}\left(\left(\vec{l}_i'\right)_{i \in I}\right)$. Cette forme multilinéaire est $\varepsilon$-hypocontinue, c'est-à-dire définit un élément $u_{\overline{\mathbf{Y}}}^{\prime}\left(\left(\vec{l}_j'\right)_{j \in \{I_i'\}}\right)$ de $L_{I_i}$; nous avons vu (proposition 4) que $u_{\overline{\mathbf{Y}}}^{\prime}$ est une application $\varepsilon$-hypocontinue de $\prod_{i \in \{I_i'}} (L_j)'_c$ dans $L_{I_i}$. Elle est donc continue sur tout produit de parties équicontinues, et par suite $u_{\overline{\mathbf{Y}}}^{\prime}\left(\prod_{j \in \{I_i'}} A_j'\right)$ est compacte dans $L_{I_i}$.

Cela prouve que, lorsque $\vec{\rho}_{\lambda}' = \otimes l_j', \lambda = 2, \ldots m$, parcourt $\otimes A_j'$, et que $\vec{\rho}_1'$ converge vers 0 dans $\otimes L_k'$ muni de la topologie induite par $(L_{I_i})'_c$, c'est-à-dire uniformément sur toute partie compacte de $L_{I_i}$, puisque $L_{I_i}$ est quasi-complet (proposition 3), $\overline{\mathbf{Y}}_0\left(\left(\vec{\rho}_{\lambda}'\right)_{\lambda \in \Lambda}\right) = \langle \vec{\rho}_1', u_{\overline{\mathbf{Y}}}^{\prime}\left(\left(\vec{l}_j'\right)_{j \in \{I_i'}\right) \rangle$ converge vers 0.

En faisant ensuite pour $\lambda=2,\ldots m$ le raisonnement que nous venons de faire pour $\lambda=1$, on voit que $\overrightarrow{\mathbf{Y}_{0}}$ est bien $\varepsilon$-hypocontinue. Mais alors, puisque $\otimes_{i\in\mathbf{I}_{\lambda}}(\mathbf{L}_{i})_{c}^{\prime}$ est dense dans $(\mathbf{L}_{\mathbf{I}_{\lambda}})_{c}^{\prime}$, et que les parties équicontinues de $\mathbf{L}_{\mathbf{I}_{\lambda}}^{\prime}$ sont contenues dans des enveloppes de produits tensoriels de parties équi-

continues des  $L_{i}^{\prime}, i \in I_{\lambda}$  (proposition 6),  $\overrightarrow{Y}_{0}$  se prolonge en une forme multilinéaire  $\overline{\overline{Y}_{0}} = \overline{X}$ , ε-hypocontinue, sur  $\prod_{\lambda \in \Lambda} (L_{I_{\lambda}})'_{c}$  (¹); et on a  $\overrightarrow{Y} = \widetilde{\overline{X}}$ , ce qui prouve bien que l'application  $\overrightarrow{X} \to \widetilde{\overline{X}}$  est épijective.

On voit donc que $\overrightarrow{\mathbf{X}}\to\overrightarrow{\mathbf{X}}$ est un isomorphisme algébrique entre les espaces vectoriels $\varepsilon\ L_{I_{\lambda}}$ et $L_{I}$. Dire que $\widetilde{\overline{X}}$ converge vers 0 dans $L_{I}$, c'est dire qu'il converge vers 0 uniformément sur tout produit de parties équicontinues des $L_{i}^{\prime}$, donc que $\overline{X}$ converge vers 0 uniformément sur tout produit tensoriel de parties équicontinues des $\otimes L_{i}^{\prime},\ \lambda\in\Lambda$; dire que $\overline{X}$ converge vers 0 dans $\varepsilon\ L_{I_{\lambda}}$, c'est dire qu'il converge vers 0 uniformément sur tout produit de parties équicontinues des $L_{I_{\lambda}}^{\prime}$. En appliquant alors la proposition 6 à chaque ensemble d'indices $I_{\lambda}$, on voit que $\widetilde{\overline{X}}$ converge vers 0 si et seulement si $\overline{X}$ converge vers 0, $\overrightarrow{X}\to\widetilde{\overline{X}}$ est un isomorphisme topologique.

Enfin les ensembles $\varepsilon$-équihypocontinus dé formes multilinéaires sur $\prod_{\lambda \in \Lambda} (\mathrm{L}_{\mathrm{I}_{\lambda}})'_c$ (resp. sur $\prod_{i \in \mathrm{I}} (\mathrm{L}_i)'_c$) sont les parties relativement compactes de $\varepsilon \mathrm{L}_{\mathrm{I}_{\lambda}}$ (resp. $\mathrm{L}_{\mathrm{I}}$) (proposition 2), donc elles se correspondent par l'isomorphisme $\widetilde{\overline{\mathbf{X}}} \to \widetilde{\overline{\mathbf{X}}}$, et la proposition est démontrée.

COROLLAIRE 1. — Les espaces $\varepsilon_{i\in\mathbf{I}}(\mathbf{L}_{i};\mathbf{M})$ et $\varepsilon_{\lambda\in\Lambda}(\mathbf{L}_{\mathbf{I}_{\lambda}};\mathbf{M})$ sont canoniquement isomorphes, algébriquement et topologiquement. L'isomorphisme met en correspondance les ensembles $\varepsilon$-équi-hypocontinus d'applications multilinéaires de $\prod_{i\in\mathbf{I}}(\mathbf{L}_{i})_{c}^{\prime}$ dans M et de $\prod_{i\in\mathbf{I}}(\mathbf{L}_{\mathbf{I}_{\lambda}})_{c}^{\prime}$ dans M.

Le premier est en effet isomorphe à $\varepsilon((\mathrm{L}_{i})_{i\in\mathbf{I}},\mathrm{M})$, le deuxième à $\varepsilon((\mathrm{L}_{\mathrm{I}_{\lambda}})_{\lambda\in\Lambda},\mathrm{M})$ d'après la proposition 4 (appliquée respectivement à l'ensemble d'indices $\mathrm{I}_{0}$, somme de I et d'un élément $\omega$, avec $\mathrm{L}_{\omega}=\mathrm{M}$, $\mathrm{J}=\mathrm{I}$, $\mathrm{K}=\{\omega\}$, et à l'ensemble d'indices $\Lambda_{0}$,

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) BOURBAKI [2], proposition 8, page 41 et remarque en petits caractères suivant la définition 2, page 39. Il s'agit dans BOURBAKI d'applications bilinéaires, le résultat est valable pour des applications multilinéaires.</span></small>

somme de $\Lambda$ et de $\omega$, avec $L_{\omega} = M$, $J = \Lambda$, $K = \{\omega\}$. Mais alors, d'après la proposition 7 (associativité), ces espaces sont isomorphes (et ils sont aussi isomorphes à $L_{I} \in M$). La correspondance entre ensembles $\varepsilon$-équihypocontinus ne peut pas se montrer de cette manière, car ces ensembles ne sont pas les ensembles relativement compacts des espaces isomorphes considérés (voir page 32). Nous remarquerons simplement qu'un ensemble $\widetilde{H}$ (resp. H) d'applications multilinéaires de $\prod_{i \in I} (L_i)_c'$ dans $M$ (resp. de $\prod_{\lambda \in \Lambda} (L_{I_\lambda})_c'$ dans $M$) est $\varepsilon$-équihypocontinu si et seulement si, pour toute partie équicontinue $\mathfrak{M}'$ de $M'$, l'ensemble ($\widetilde{H}$, $\mathfrak{M}'$) (resp. H, $\mathfrak{M}'$) de formes multilinéaires sur $\prod_{i \in I} (L_i)_c'$ (resp. $\prod_{\lambda \in \Lambda} (L_{I_\lambda})_c'$) défini par $(\vec{l}_i')_{i \in I} \to \langle \widetilde{\overline{X}}((\vec{l}_i')_{i \in I}), \vec{m'} \rangle$ pour $\widetilde{\overline{X}} \in \widetilde{H}$, $\vec{m'} \in \mathfrak{M}'$ (resp. par $(\vec{\rho'_\lambda})_{\lambda \in \Lambda} \to \langle \widetilde{X}((\vec{\rho'_\lambda})_{\lambda \in \Lambda}), \vec{m'} \rangle$ pour $\widetilde{X} \in H$, $\vec{m'} \in \mathfrak{M}'$) est $\varepsilon$-équihypocontinu.

Il suffit alors d'appliquer à (H, M') (resp. H, M') la fin de la proposition 7.

On remarque d'ailleurs immédiatement qu'on aurait pu démontrer directement le corollaire, et que la proposition 7 en aurait été un cas particulier pour M = C, corps des scalaires.

COROLLAIRE 2. — Les espaces $\varepsilon_{i\in I}(L_i; M)$ et $L_I\varepsilon M$ sont canoniquement isomorphes.

En effet $\varepsilon_{i\in \mathbf{I}}(\hat{\mathbf{L}}_i;\mathbf{M})\approx \varepsilon ((\mathbf{L}_i)_{i\in \mathbf{I}},\mathbf{M})\approx \mathbf{L}_{\mathbf{I}}\varepsilon \mathbf{M}$ (propositions 4 et 7).

Propriétés particulières aux espaces complets.

PROPOSITION 8. — Soient L un espace localement convexe séparé complet, M un espace localement convexe non nécessairement séparé ni quasi-complet. Une application linéaire u de L' dans M, continue sur toute partie équicontinue de L', est continue sur L'.

Soit en effet  $M_{0}$  l'espace séparé associé à M. u définit alors une application  $u_{0}$  de  $L_{c}^{\prime}$  dans  $M_{0}$, dont les restrictions aux parties équicontinues de  $L^{\prime}$  sont continues. Montrons que  $u_{0}$  est continue de  $\sigma(L^{\prime}, L)$  dans  $\sigma(M_{0}, M_{0}^{\prime})$. Soit  $\overleftrightarrow{m}_{0}^{\prime} \in M_{0}^{\prime}$. Nous devons montrer que la forme linéaire  $\overleftrightarrow{l^{\prime}} \to \langle u_{0}. \overleftrightarrow{l^{\prime}}, \overleftrightarrow{m}_{0}^{\prime} \rangle$  est

faiblement continue sur L'; or elle est continue sur toute partie équicontinue de L', notre assertion résulte donc d'un théorème de Grothendieck, valable parce que L est complet (1). La proposition 5 montre alors que $u_0$ est continue de $L_c'$ dans $M_0$, donc $u$ est continue de $L_c'$ dans M.

COROLLAIRE 1. — Si L est complet, la topologie $L_c'$ est la topologie localement convexe la plus fine qui induise sur les parties équicontinues de $L'$ une topologie moins fine que $L_c'$ (ou $\sigma(L', L)$). Appelons en effet M l'espace $L'$, muni de n'importe quelle topologie localement convexe (non nécessairement séparée ni quasi-complète) qui induise sur les parties équicontinues de $L'$ une topologie moins fine que $L_c'$ ou $\sigma(L', L)$. Alors l'application identique de $L_c'$ dans M est continue sur toute partie équicontinue de $L'$, donc continue, et $L_c'$ est plus fine que M.

COROLLAIRE 2. — Si L est complet, une partie W' de L', convexe équilibrée, qui coupe toute partie équicontinue de L' suivant un voisinage de 0 dans cette partie pour la topologie L', est un voisinage de 0 pour la topologie L'.

Appelons en effet M l'espace L' muni de la topologie localement convexe ayant pour système fondamental de voisinages de 0 les ensembles $\lambda W'$, $\lambda \in C$, $\lambda \neq 0$. M induit sur les parties équicontinues de L' une topologie moins fine que L', donc M est moins fine que L' d'après le corollaire 1, et W' est bien un voisinage de 0 de L'.

COROLLAIRE 3. — Soient $L_i$ des espaces localement convexes séparés complets, M un espace localement convexe séparé (non nécessairement quasi-complet). Tout ensemble H d'applications multilinéaires de $\prod_{i \in I} (L_i)'_c$ dans M, équicontinu sur tout produit

de parties équicontinues des  $L_{i}^{\prime}$ , est ε-équihypocontinu.

C'est ce résultat que nous avions annoncé à la proposition 2 (remarque $2^{0}$) et à son corollaire 1.

La démonstration n'utilise même pas la proposition 2. Soit I = (1, 2, ... n). Soient A$_{i}$ des parties équicontinues des L$_{i}$, i = 2 ... n. A chaque $\vec{X} \in H$ et à chaque élément

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">50.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) GROTHENDIECK [1], corollaire 5°.</span></small>

$(\vec{l}_i')_{i=2,\ldots n}$ de $\prod_{i=2}^{i=n} A_i'$, associons l'application linéaire $u_{\widetilde{X}}(\vec{l}_2', \ldots \vec{l}_n')$: $\vec{l}_1' \to \vec{X}(\vec{l}_1', \vec{l}_2', \ldots \vec{l}_n')$, de $(L_1)'_c$ dans M.

Soit M un voisinage de 0 disqué dans M. Appelons W' l'ensemble des $\vec{l}_{i}^{\prime}$ de L$_{i}^{\prime}$ tels que $u_{\mathbf{X}}(\vec{l}_{2}^{\prime}, \ldots \vec{l}_{n}^{\prime}).\vec{l}_{i}^{\prime}$ soit dans M, pour tout $\overrightarrow{\mathbf{X}} \in \mathbf{H}$, et tout $(\vec{l}_{i}^{\prime})_{i=2 \ldots n} \in \prod_{i=2}^{i=n} \mathbf{A}_{i}^{\prime}$. Puisque $\overrightarrow{\mathbf{X}}$ est équicontinu sur tout produit de parties équicontinues des L$_{i}^{\prime}$, W' coupe toute partie équicontinue de L$_{i}^{\prime}$ suivant un voisinage de 0 de cette partie pour la topologie de (L$_{1}$)$_{c}^{\prime}$; donc d'après le corollaire 2, W' est un voisinage de 0 de (L$_{1}$)$_{c}^{\prime}$, ce qui prouve que H est ε-équihypocontinu.

APPLICATION. — Le dual fort d'un espace de Schwartz complet est ultrabornologique.

Un espace de Schwartz (1) L est un espace localement convexe séparé tel que, pour tout voisinage disqué V de 0, il existe un voisinage U de 0 dont l'image dans $\hat{L}_{\mathcal{V}}$ (2) soit relativement compacte. On peut encore donner une condition équivalente : pour toute partie équicontinue A' de L', il existe une partie équicontinue convexe équilibrée faiblement fermée B' telle que A' soit relativement compacte dans L'B' (3).

Un espace localement convexe séparé est ultrabornologique (') s'il est limite inductive d'espaces de Banach; tout espace ultrabornologique est bornologique et tonnelé, tout espace bornologique et quasi-complet est ultrabornologique. Considérons tous les espaces normés $L_B'$, où les B' sont les

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Cette dénomination est due à M. GROTHENDIECK! GROTHENDIECK [2], page 116.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$p(\vec{l})\leqslant 1$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">p,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\hat{\mathbf{L}}_{\mathcal{V}}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) Le voisinage disqué $\mathcal{V}$ définit une pseudo-norme $p$, telle que $\mathcal{V}$ soit la semiboule $p(\vec{l}) \leqslant 1$; L$\mathcal{V}$ est l'espace séparé normé associé, $\hat{\mathcal{L}}\mathcal{V}$ son complété, espace de BANACH.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$M_{B}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$M_{B}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(3) Si B est une partie bornée disquée d'un espace localement convexe M,  $M_{B}$  est le sous-espace de M engendré par B, muni de la norme pour laquelle B est la boule unité. On sait que  $M_{B}$  est complet, donc est un espace de Banach, toutes les fois que B est complète (voir BOURBAKI [2], page 21, démonstration du lemme 1). En particulier, toute partie équicontinue disquée  $B'$  de  $L'$  faible est complète, donc  $L'_{B'}$  est un espace de Banach.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{B}^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L'</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$L_{B'}'$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L, L'v0</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Lp</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\hat{\mathbf{L}}_{\mathbf{v}}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">W'</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Si $\mathcal{V}$ est un voisinage disqué de L, $L_{\nu 0}^{\prime}$ est le dual de Lq ou $\hat{L}\mathcal{V}$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(4) Dans BOURBAKI [2], page 34, exercice 11, on trouvera une définition légèrement différente. Ici L est ultrabornologique pour l'une ou l'autre définition, puisque nous démontrons que tout ensemble W' convexe équilibré, absorbant toutes les parties équicontinues, est un voisinage fort de 0.</span></small>

parties équicontinues convexes équilibrées faiblement fermées de L'; les B' sont alors faiblement compactes donc faiblement complètes, et par suite les L'B' sont des espaces de Banach. Soit L'la topologie limite inductive des L'B', c'est-à-dire la topologie localement convexe la plus fine telle que les injections L'B' → L'0 soient continues. Comme les injections L'B' → L'c sont continues, L'0 est plus fine que L'c. Alors, d'après le corollaire 1, valable puisque L est complet, on aura L'0 = L'c si l'on sait que ces deux topologies induisent la même topologie sur toute partie équicontinue disquée A' de L'. Or, si B' est une partie équicontinue disquée de L' telle que A' soit compacte dans L'B', (une telle partie existe puisque L est un espace de Schwartz), on sait que, sur L'B', et a fortiori sur A', L'0 et L'c sont plus faibles que L'B'; mais A' est compacte dans L'B', donc L'0 et L'c induisent bien la même topologie sur A', et on a bien L'0 = L'c.

Comme L est un espace de Schwartz, les parties bornées de L sont relativement compactes, et comme L est complet,  $L_{c}^{\prime}$  est la topologie de la convergence uniforme sur les parties relativement compactes, donc finalement  $L_{c}^{\prime}$  est la topologie forte de  $L^{\prime}$, qui est ainsi limite inductive des  $L_{B^{\prime}}^{\prime}$,

$$
\mathbf {c . q . f . d .}
$$

Conséquence: les espaces de distributions $\mathcal{E}^{\prime}$, $\mathcal{D}^{\prime}$, $\mathcal{F}^{\prime}$, sont bornologiques (1).

Cas de quelques espaces particuliers.

PROPOSITION 9. — Si les $L_i$ et M sont des espaces (non nécessairement quasi-complets) métrisables (resp. de Frechet, resp. normés, resp. de Banach), il en est de même de $\varepsilon$ ($L_i$; M).

Si les  $L_{i}$  et M sont métrisables, si  $(\mathrm{U}_{i,n})_{n=1,2,\ldots}$  (resp.  $(\mathrm{V}_{n})_{n=1,2,\ldots}$ ) est un système fondamental dénombrable de voisinages de 0 dans  $L_{i}$  (resp. M), et si  $W_{n}$  est l'ensemble des  $\overrightarrow{X}$  de  $\varepsilon_{i\in I}(L_{i};M)$  tels que  $\overrightarrow{X}\left(\prod_{i\in I}U_{i,n}^{0}\right)\subset V_{n}$ , les  $W_{n}$  forment un système fondamental dénombrable de voisinages de 0 de  $\varepsilon_{i\in I}(L_{i};M)$ , qui est ainsi métrisable. Si alors les  $L_{i}$  et M sont des

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Propriété démontrée par une autre méthode par GROTHENDIECK [2], page 85, théorème 10.</span></small>

espaces de Fréchet, $\varepsilon_{i\in I}(L_i;M)$ est métrisable et complet (corollaire 1 de la proposition 4), donc est un espace de Fréchet.

Si les  $L_{i}$  et M sont normés, il existe sur  $\varepsilon(\mathbf{L}_{i};\mathbf{M})$  une norme naturelle qui définit sa topologie :

$$
(\mathbf {I}, \dot {\mathbf {1}}; 5)
$$

$$
\| \vec {\mathrm{X}} \| = \sup _ {\| \vec {l} _ {i} ^ {\prime} \| \leqslant 1, i \in \mathbf {I}} \| \vec {\mathrm{X}} \left(\left(\vec {l} _ {i} ^ {\prime}\right) _ {i \in \mathbf {I}}\right) \|.
$$

Si alors les  $L_{i}$  et M sont des espaces de Banach,  $\varepsilon_{i\in\mathbf{I}}(\mathbf{L}_{i};\mathbf{M})$  est normé et complet, c'est donc un espace de Banach.

Dans le cas où tous les espaces considérés sont normés (ou sont des espaces de Banach, si on doit les supposer quasi-complets), les propositions démontrées s'améliorent :

a) si les $\vec{l}_{i}$ sont des éléments des $\mathbf{L}_{i}$, $\left\| \otimes \vec{l}_{i} \right\| = \prod_{i \in \mathbf{I}} \left\| \vec{l}_{i} \right\|$;

b) dans la proposition 1, $||u_{\mathrm{I}}|| = \prod_{i\in \mathrm{I}}||u_i||$

c) L'isomorphisme de la proposition 4, entre $\mathbf{L}_{\mathbf{I}}$ et $\varepsilon_{j\in\mathbf{J}}(\mathbf{L}_{j};\mathbf{L}_{\mathbf{K}})$, est une isométrie.

$d)$ dans la proposition 6, la boule unité de $\mathbf{L}_{\mathbf{I}}^{\prime}$ est l'enveloppe (dans $(\mathbf{L}_{\mathbf{I}})_{c}^{\prime})$ du produit tensoriel des boules unités des $\mathbf{L}_{i}^{\prime}$.

e) L'isomorphisme de la proposition 7, ou de son corollaire 1, est une isométrie.

f) Les isomorphismes $\varepsilon_{i\in\mathbf{I}}(\mathbf{L}_{i};\mathbf{M})\approx\varepsilon((\mathbf{L}_{i})_{i\in\mathbf{I}},\mathbf{M})\approx\mathbf{L}_{\mathbf{I}}\varepsilon\mathbf{M}$ sont des isométries.

PROPOSITION 10. — Si L et M sont des espaces de Banach, LεM est isomorphe à l'espace des applications linéaires compactes faiblement continues de L' dans M, et la norme d'un élément coïncide avec la norme de l'application linéaire correspondante; L'εM est isomorphe à l'espace Γ(L; M) des applications linéaires compactes de L dans M, et la norme d'un élément est la norme de l'application linéaire correspondante.

$L\varepsilon M$ est en effet isomorphe à $\mathcal{L}_{\varepsilon}(L_{c}^{\prime}; M)$. D'après la proposition 5, $u$ appartient à $\mathcal{L}_{\varepsilon}(L_{c}^{\prime}; M)$ si et seulement si-elle est continue de $\sigma(L^{\prime}, L)$ dans $\sigma(M, M^{\prime})$, c'est-à-dire faiblement continue, et si en outre l'image $u(B^{\prime})$ de la boule unité $B^{\prime}$ de $L^{\prime}$ est relativement compacte dans $M$, c'est-à-dire si $u$ est une application compacte ('); dans ce cas, comme $B^{\prime}$ est compacte

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Les applications compactes sont aussi appelées complètement continues.</span></small>

pour $\mathbf{L}_c'$, $u(\mathbf{B}')$ est même compacte dans M. Pour $u \in \mathbf{L}_{\epsilon} \mathbf{M}$, on a $\| u \| = \sup_{\vec{l} \in L', \| \vec{l}' \| \leq 1} \| u \cdot \vec{l}'\|$ d'après $c)$ page 45, $\| u\|$ est donc bien la norme de l'opérateur $u \in \mathfrak{L}(\mathbf{L}', \mathbf{M})$.

D'autre part L'ε M est isomorphe à ℒε((L')c; M) = ℒε(Lc'; M). Si u ∈ ℒ(Lc'; M), u définit a fortiori un opérateur u₀ de L dans M; comme la boule unité B" de L" est compacte dans Lc, son image u(B") est compacte dans M, donc l'image u₀(B) de la boule unité B de L est relativement compacte dans M, u₀ est une application linéaire compacte de L dans M. Ainsi u → u₀ est une application linéaire de ℒ(Lc'; M) dans Γ(L; M). Cette application est injective; si en effet u₀ est nulle, u est nulle puisque L est dense dans σ(L", L') donc dans Lc. Cette application est aussi épijective. Si en effet ν est une application linéaire compacte de L dans M, sa bitransposée u = "ν est continue de σ(L", L') dans σ(M", M'); comme ν(B) est relativement compacte dans M, son adhérence ν(B) est compacte dans M, donc a fortiori dans σ(M", M'), et comme B" est l'adhérence faible de B, u(B") est dans ν(B); alors u applique L" dans M, elle est continue de σ(L", L') dans σ(M, M'), et l'image u(B") est relativement compacte dans M, donc, d'après la proposition 5, u est continue de Lc' dans M (et alors u(B") est même compacte dans M; mais ν(B) n'est en général que relativement compacte), et sa restriction u₀ à L est bien ν.

Ainsi la correspondance $u \leftrightarrow u_0$ est un isomorphisme algébrique entre $\mathfrak{L}(L_c^{\prime\prime}; M)$ ou $L^{\prime}\varepsilon M$ et l'espace $\Gamma(L; M)$ des opérateurs compacts de $L$ dans $M$. La norme de $u \in L^{\prime}\varepsilon M \approx \mathcal{L}_{\varepsilon}(L_c^{\prime\prime}; M)$ est $||u|| = \sup_{\vec{l} \in B'} \|u.\vec{l}''\|$; comme $B$ est dense dans $B''$ pour $L_c^{\prime\prime}$ et que $u$ est continue de $L_c^{\prime\prime}$ dans $M$, $||u||$ est encore $\sup_{\vec{l} \in B} \|u_0.\vec{l} \|$, c'est-à-dire la norme de l'opérateur compact $u_0$, c.q.f.d.

Produit ε et produit tensoriel topologique.

PROPOSITION 11. -- Soient L, M, des espaces localement convexes séparés (non nécessairement quasi-complets). L'espace L ⊗ε M (¹) est un sous-espace vectoriel topologique de LεM. Il

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L$^{*}$⊗</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) GROTHENDIECK [3] et [4], page 89, appelle L ≡ M ce que nous appelons L ≡ M. Voir aussi SCHWARTZ [2] exposé 7.</span></small>

est strictement dense (resp. dense) pour tout M, si et seulement si L vérifie la propriété d'approximation stricte (resp. d'approximation) $^{(1)}$.

Tout d'abord on a L ⊗ M ⊂ LεM (page 19). Sur L ⊗ M, la topologie ε de Grothendieck est celle de la convergence uniforme sur les produits de parties équicontinues de L' et M', c'est-à-dire la topologie induite par LεM.

Soit $u \in \mathfrak{L}_{\varepsilon}(\mathbf{M}_{c}^{\prime}; \mathbf{L})$. L'application $0: \nu \to \nu \circ u$ de $\mathfrak{L}_{c}(\mathbf{L}; \mathbf{L})$ dans $\mathfrak{L}_{\varepsilon}(\mathbf{M}_{c}^{\prime}; \mathbf{L})$ est continue, parce que l'image par $u$ de toute partie équicontinue disquée de $\mathbf{M}_{c}^{\prime}$ est convexe équilibrée compacte dans $L$. Si $u$ est dans $L^{\prime} \otimes L$, c'est-à-dire de rang fini, $\nu \circ u$ est aussi de rang fini et faiblement continue, donc dans $M \otimes L$, autrement dit l'application $0$ appliqué $L^{\prime} \otimes L$ dans $M \otimes L$. Par ailleurs $0(I) = u$, si $I$ est l'opérateur identique de $L$. Donc si $L$ vérifie la propriété d'approximation stricte (resp. d'approximation), $I$ est strictement adhérent (resp. adhérent) à $L^{\prime} \otimes L$ dans $\mathfrak{L}_{c}(L; L)$, donc $0(I) = u$ est strictement adhérent (resp. adhérent) à $0(L^{\prime} \otimes L) \subset M \otimes L$ dans $\mathfrak{L}_{\varepsilon}(\mathbf{M}_{c}^{\prime}; L)$, c'est-à-dire $L \otimes M$ est strictement dense (resp. dense) dans $L_{\varepsilon}M$.

Réciproquement, L étant fixé, supposons que, pour tout M, L ⊗ M soit strictement dense (resp. dense) dans LεM.

Prenons  $M = L_{c}^{\prime}$ . On sait que  $\mathcal{L}_{c}(L; L)$  est un sous-espace topologique de  $L \in L_{c}^{\prime}$  (corollaire de la proposition 5).

Comme $L \otimes L' \subset \mathscr{L}_c(L; L)$, et que tout élément de $L \in L'_c$ est supposé strictement adhérent (resp. adhérent) à $L \otimes L'$, l'élément I de $\mathscr{L}_c(L; L)$ est strictement adhérent (resp. adhérent) à $L \otimes L'$, et L vérifie la propriété d'approximation stricte (resp. d'approximation), c.q.f.d.

COROLLAIRE 1. — Si L et M sont quasi-complets (resp. complets), et si l'un d'eux vérifie la propriété d'approximation stricte (resp. d'approximation), alors L ⊗ε M (resp. L ε⊗ M) est identique à LεM.

En effet LεM est alors quasi-complet (resp. complet) (proposition 3).

On en déduit que si L et M sont complets, et si l'un d'eux vérifie la condition d'approximation stricte, le quasi-complété L $\widehat{\otimes}_{\varepsilon}$ M coïncide avec le complété L $\widehat{\otimes}_{\varepsilon}$ M.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Voir Préliminaires.</span></small>

COROLLAIRE 2. — Si les $L_i$ sont quasi-complets, et si tous, sauf un au plus, vérifient la propriété d'approximation stricte (resp. d'approximation), $\otimes_{i \in I} L_i$ est strictement dense (resp. dense) dans $L_I$. Si tous les $L_i$ vérifient la propriété d'approximation stricte (resp. d'approximation), il en est de même de $L_I$.

Démontrons la première propriété par récurrence sur le nombre $n$ d'éléments de I. Elle est évidente si $n=1$. Supposons la démontrée lorsque I a $n-1$ éléments, et démontrons la pour $I=(1,2,\ldots n)$. Nous supposons que $L_{2},\ldots,L_{n}$, vérifient la propriété d'approximation stricte (resp. d'approximation).

Alors $\otimes_{i=1}^{i=n-1} L_i$ est strictement dense (resp. dense) dans $\varepsilon_{i=1}^{i=n-1} L_i$, d'après l'hypothèse de récurrence; alors $\otimes_{i \in I} L_i = \left( \begin{array}{c} i=n-1 \\ \otimes \\ i=1 \end{array} L_i \right) \otimes L_n$ est strictement dense (resp. dense) dans $\left( \begin{array}{c} i=n-1 \\ \varepsilon \\ i=1 \end{array} L_i \right) \otimes_\varepsilon L_n$; comme alors $L_n$ vérifie la propriété d'approximation stricte (resp. d'approximation), ce dernier espace est strictement dense (resp. dense) dans $\left( \begin{array}{c} i=n-1 \\ \varepsilon \\ i=1 \end{array} L_i \right) \varepsilon L_n$ d'après la proposition 11. Enfin ce dernier espace est $L_I$ puisque les $L_i$ sont quasi-complets (proposition 7). Finalement $\otimes L_i$ est strictement dense (resp. dense) dans $L_I$.

Supposons maintenant que tous les  $L_{i}$  vérifient la propriété d'approximation stricte (resp. d'approximation). Soit M un espace localement convexe séparé quelconque, non nécessairement quasi-complet.

D'après la première partie du corollaire, $\otimes_{i\in I}L_i\otimes \widehat{M}$ est strictement dense (resp. dense) dans $\varepsilon ((L_i)_{i\in I},\widehat{M}) = L_I\varepsilon \widehat{M}$ (corollaire 2 de la proposition 7), donc a fortiori $L_I\otimes \widehat{M}$ est strictement dense (resp. dense) dans $L_I\varepsilon \widehat{M}$; alors $L_I\otimes M$, strictement dense dans $L_I\otimes_{\varepsilon}\widehat{M}$, est lui aussi strictement dense (resp. dense) dans $L_I\varepsilon \widehat{M}$ donc a fortiori dans $L_I\varepsilon M$. Cela prouve, d'après la proposition 11, que $L_I$ vérifie la propriété d'approximation stricte (resp. d'approximation).

## § 2. Définition des distributions à valeurs vectorielles.

Nous avons vu dans un article antérieur (¹) que, si H est un espace de fonctions différentiables sur  $R^{n}$  à valeurs scalaires (réelles ou complexes) et E un espace vectoriel topologique localement convexe séparé quasi-complet, il y a plusieurs définitions possibles, a priori aussi naturelles les unes que les autres, pour l'espace des fonctions vectorielles définies sur  $R^{n}$  à valeurs dans E du type H. Ainsi nous avons distingué les espaces  $\mathcal{D}^{m}(E)$  et  $\widetilde{\mathcal{D}}^{m}(E)$, appelés alors  $\widetilde{\mathcal{D}}^{m}(E)$  et  $\mathcal{D}^{m}(E)$  respectivement; d'autre part nous avons défini  $\mathcal{H}^{m}(E)$  (appelé alors  $\widetilde{\mathcal{H}}^{m}(E)$) comme l'espace des fonctions m fois continuement différentiables scalairement dans  $H^{m}$, et non comme l'espace des fonctions scalairement m fois continuement différentiables et scalairement dans  $H^{m}$, ces deux espaces étant différents pour m fini. La définition que nous avons retenue est celle qui pour  $\mathcal{H}^{m}(E)$  donnait le produit tensoriel topologique quasi-complété  $H^{m}\otimes_{\varepsilon}E$. Ce sont les mêmes considérations qui nous guideront pour les distributions à valeurs vectorielles.

DÉFINITION. — Une distribution d'ordre ≤ m (fini ou infini) sur R^n à valeurs dans E, espace vectoriel topologique localement convexe séparé, sera une application linéaire continue T de $\mathfrak{D}^m$ dans E; l'espace de ces distributions, qui est donc $\mathfrak{L}(\mathfrak{D}^m; \mathrm{E})$, sera aussi noté $\mathfrak{D}'^m(\mathrm{E})$. Soit $m \leqslant m'$. Une application linéaire continue $\vec{T}$ de $\mathfrak{D}^m$ dans E définit a fortiori une application linéaire continue $\vec{T}'$ de $\mathfrak{D}^{m'}$ dans E; par ailleurs $\vec{T}'$ suffit à caractériser $\vec{T}$ car elle définit $\vec{T}$ sur le sous-espace dense $\mathfrak{D}^{m'}$ de $\mathfrak{D}^m$. On peut donc considérer (abstraction faite de toute topologie) $\mathfrak{D}'^m(\mathrm{E})$ comme sous-espace de $\mathfrak{D}'^m(\mathrm{E})$. En particulier tous ces espaces sont contenus dans $\mathfrak{D}'(\mathrm{E}) = \mathfrak{L}(\mathfrak{D}; \mathrm{E})$, espace des distributions à valeurs dans E.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\widehat{\mathcal{H}}^m$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{H}^m (\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Voir SCHWARTZ [1]; en particulier page 106, lemme 2 page 146, et théorème 1, page 111. Nous changeons ici les notations adoptées dans cet article. On voit en effet que $\widehat{\mathcal{H}}^m(E)$ est le plus usité, tandis que $\mathcal{H}^m(E)$ ne s'emploie que dans des cas exceptionnels; autant vaut prendre la notation la plus simple pour le cas le plus fréquent; nous écrirons donc désormais $\mathcal{H}^m(E)$ et $\overline{\mathcal{H}}^m(E)$ au lieu de $\widehat{\mathcal{H}}^m(E)$ et $\mathcal{H}^m(E)$ respectivement.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{H}^m (\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\overline{\mathcal{H}}^m (\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\widetilde{\mathcal{H}}^m (\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{H}^m (\mathrm{E})$</span></small>

En général nous munirons $\mathfrak{D}^{\prime m}(\mathbf{E})$ de la topologie $\mathfrak{L}_{c}(\mathfrak{D}^{m};\mathbf{E})$ ou $\mathfrak{D}_{c}^{\prime m}(\mathbf{E})$ de la convergence uniforme sur les parties compactes de $\mathfrak{D}^{m}$; parfois de la topologie $\mathbf{L}_{b}(\mathfrak{D}^{m};\mathbf{E})$ de la convergence uniforme sur les parties bornées de $\mathfrak{D}^{m}$. Pour $m$ infini, ces deux topologies n'en font qu'une et $\mathfrak{D}^{\prime}(\mathbf{E})$ sera toujours considéré comme muni de cette topologie.

Dans toute la suite, sauf mention expresse du contraire, E sera un espace vectoriel topologique localement convexe séparé quasi-complet.

PROPOSITION 12. — E n'étant pas nécessairement quasi-complet, les espaces $\mathfrak{D}_{c}^{'m}(\mathrm{E})$, $\mathscr{L}_{\varepsilon}(\mathrm{E}_{c}^{\prime};\mathfrak{D}_{c}^{'m})$ et $\mathfrak{D}_{c}^{'m}\varepsilon\mathrm{E}$ sont canoniquement isomorphes. Si E est quasi-complet, $\mathfrak{D}_{c}^{'m}\varepsilon\mathrm{E}$ est quasi-complet et identique à $\mathfrak{D}_{c}^{'m}\otimes_{\varepsilon}\mathrm{E}$; si E est complet, $\mathfrak{D}_{c}^{'m}\varepsilon\mathrm{E}$ est complet et identique à $\mathfrak{D}_{c}^{'m}\otimes_{\varepsilon}\mathrm{E}$.

DÉMONSTRATION. — $\mathfrak{D}^{m}$ a la topologie $\tau(\mathfrak{D}^{m},\mathfrak{D}^{\prime m})$ (1), donc $\mathfrak{D}^{m}=(\mathfrak{D}_{c}^{\prime m})_{c}^{\prime}$ (§ 1, page 17), alors les isomorphismes résultent du corollaire 2 de la proposition 4 du § 1; comme $\mathfrak{D}_{c}^{\prime m}$ est complet (2), et a la propriété d'approximation stricte (corollaire 2 de la proposition 4 des préliminaires), l'identité $\mathfrak{D}_{c}^{\prime m}\varepsilon\mathrm{E}=\mathfrak{D}_{c}^{\prime m}\widehat{\otimes}_{\varepsilon}\mathrm{E}$ (resp. $\mathfrak{D}_{c}^{\prime m}\widehat{\otimes}_{\varepsilon}\mathrm{E}$) si E est quasi-complet (resp. complet) résulte du corollaire 1 de la proposition 11 du § 1.

Si $\vec{T}$ est une distribution à valeurs dans E muni de sa topologie affaiblie, comme $\mathfrak{D}^m$ a la topologie $\tau(\mathfrak{D}^m, \mathfrak{D}'^m)$ de Mackey, l'application $\vec{T}$ de $\mathfrak{D}$ dans E, faiblement continue, est aussi continue, et $\vec{T}$ est aussi une distribution à valeurs dans E muni de sa topologie initiale.

D'ailleurs pour qu'une application linéaire de $\mathfrak{D}^{m}$ dans E soit continue, il faut et il suffit, puisque $\mathfrak{D}^{m}$ est bornologique (3), qu'elle transforme toute partie bornée de $\mathfrak{D}^{m}$ en une partie bornée de E : l'espace des distributions d'ordre $\leqslant m$ a valeurs dans E, abstraction faite de sa topologie, ne dépend pas de la topologie de E, mais seulement de ses parties bornées.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">5,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Un espace tonnelé a la topologie $\tau$ de Mackey (BOURBAKI [2], proposition 5, page 70); or $\mathfrak{D}_{\mathbf{K}}^{m}$ (K, compact de $\mathbb{R}^{n}$) est un espace de Fréchet, donc tonnelé, et $\mathfrak{D}^{m}$, limite inductive des $\mathfrak{D}_{\mathbf{K}}^{m}$, est aussi tonnelé (BOURBAKI [2], corollaire de la proposition 1, page 2 et corollaire 2 de la proposition 2, page 2).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Dm</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) DIEUDONNÉ-SCHWARTZ [1], proposition 12, page 82.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(3) BOURBAKI [4], théorème 3, page 11; le fait que $\mathcal{D}^{m}$ soit bornologique résulte de ce qu'il est un espace $\mathscr{L}\mathscr{F}$, voir ibidem milieu de la page 11. On trouvera aussi le résultat énoncé dans DIEUDONNÉ-SCHWARTZ [1], proposition 6, page 71.</span></small>

Maintenant, soit $\vec{T}$ une application linéaire quelconque de E' dans $\mathfrak{D}_{c}^{\prime m}$. Par transposition, elle définit une application linéaire continue de $\mathfrak{D}^{m}$ dans E', dual algébrique de E', lorsqu'on munit $\mathfrak{D}^{m}$ de sa topologie affaiblie, et E'\* de la topologie $\sigma(\mathrm{E}^{\prime*},\mathrm{E}^{\prime})$; $\vec{T}$ est une distribution d'ordre $\leqslant m$ à valeurs dans E'. Pour qu'elle soit une distribution d'ordre $\leqslant m$ à valeurs dans E (et par conséquent pour que $\vec{T}$ soit continue de E' dans $\mathfrak{D}_{c}^{\prime m}$), il suffit que, pour toute $\varphi\in\mathfrak{D}^{m}$, $\vec{T}(\varphi)$ soit dans E; car alors $\vec{T}$ est une distribution à valeurs dans E muni de sa topologie affaiblie, donc à valeurs dans E muni de sa topologie initiale.

Notation. — Nous réserverons le nom de distributions d'ordre $\leqslant m$ à valeurs dans E aux éléments de $\mathcal{L}(\mathfrak{D}^{m};\mathrm{E})$, et nous noterons $\mathfrak{D}_{c}^{\prime m}(\mathrm{E})$ l'espace $\mathfrak{L}_{c}(\mathfrak{D}^{m};\mathrm{E})$. Pour $\vec{\mathrm{T}}\in\mathcal{L}(\mathfrak{D}^{m};\mathrm{E})$, nous appellerons $^{t}\vec{\mathrm{T}}$ l'élément de $\mathcal{L}(\mathrm{E}_{c}^{\prime};\mathfrak{D}_{c}^{\prime m})$ associé à $\vec{\mathrm{T}}$ par transposition; nous noterons $\vec{\mathrm{T}}(\varphi)\in\mathrm{E}$ l'image de $\varphi\in\mathfrak{D}^{m}$ par $\vec{\mathrm{T}}$, et $\langle\vec{\mathrm{T}},\vec{e}^{\prime}\rangle\in\mathfrak{D}^{\prime m}$ l'image $^{t}\vec{\mathrm{T}}(e^{\prime})$ de $e^{\prime}\in\mathrm{E}^{\prime}$ par $^{t}\vec{\mathrm{T}}$. Nous poserons

$$
\langle \langle \vec {\mathrm{T}}, \varphi , \vec {e ^ {\prime}} \rangle \rangle = \langle \vec {\mathrm{T}} (\varphi), \vec {e ^ {\prime}} \rangle = \langle \vec {\mathrm{T}}, \vec {e ^ {\prime}} \rangle (\varphi), \tag {I,2;1}
$$

l'égalité entre les deux derniers membres marquant précisément la relation de transposition entre $\vec{T}$ et $^{t}\vec{T}$ (1).

Quant à l'espace $\mathfrak{D}_{c}^{\prime m}\widehat{\otimes}_{\varepsilon}\mathrm{E}$, il est isomorphe à chacun des deux précédents mais formellement non identique. Il n'y aura cependant pas d'inconvénient dans la suite à l'identifier complètement à $\mathcal{L}_{c}(\mathfrak{D}^{m};\mathrm{E})$. Pour $\mathbf{T}\in\mathfrak{D}^{\prime m}$ et $\vec{e}\in\mathrm{E}$, nous appellerons donc $\mathbf{T}\otimes\vec{e}$ l'élément de $\mathcal{L}(\mathfrak{D}^{m};\mathrm{E})$ défini par

$$
(\mathbf {I}, 2; 2)
$$

$$
\left(\mathbf {T} \otimes \vec {e}\right) (\varphi) = \mathbf {T} (\varphi) \vec {e},
$$

(1) Nous invertions les notations de Schwartz [1]: nous appelions  $L_{\vec{\varphi}}$  l'application  $\vec{e}' \to \langle \vec{\varphi}, \vec{e}' \rangle$ , et  ${}^{t}L_{\vec{\varphi}}$  l'application  $T \to T(\vec{\varphi})$ , page 125 de l'article cité; ici au contraire nous appelons  $\vec{T}$  ou  $L_{\vec{T}}$  l'application  $\psi \to \vec{T}(\psi)$ , et  ${}^{t}\vec{T}$  ou  ${}^{t}L_{\vec{T}}$  l'application  $\vec{e}' \to \langle \vec{T}, \vec{e}' \rangle$ . Cette modification est motivée par la considération suivante: si  $\vec{T}$  est une fonction  $\vec{\varphi} \in \mathcal{E}^{0}(E)$ , il est normal que l'application  $\vec{T}$  ou  $L_{\vec{T}}$  aille dans le même sens que l'application  $\vec{\varphi}$ ; or  $\vec{\varphi}$  applique  $R^{n}$  dans E, et si l'on identifie chaque point de  $R^{n}$  à la mesure définie par la masse unité en ce point,  $\vec{\varphi}$  devient une application d'un sous-espace de  $E^{'0}$  dans E; son extension en une application de  $E^{'0}$  tout entier dans E doit être appelée  $L_{\vec{T}}$ .

et $^{t}\left(\mathbf{T} \otimes \vec{e}\right)$ l'élément de $\mathfrak{L}(\mathrm{E}_{c}^{\prime}; \mathcal{D}_{c}^{\prime m})$ défini par

$$
(\mathbf {I}, 2; 3)
$$

$$
\langle \mathbf {T} \otimes \vec {e}, \vec {e ^ {\prime}} \rangle = \langle \vec {e}, \vec {e ^ {\prime}} \rangle \mathbf {T}.
$$

Naturellement dans bien des cas il y aura même intérêt à identifier complètement les 3 espaces isomorphes, et à ne plus distinguer $\vec{T}$ de $\vec{T}$. Dans d'autres cas il y aura intérêt à ne plus faire aucune identification.

## Autres types de distributions vectorielles.

DÉFINITION. — $\mathcal{H}$ étant un espace de distributions ('), E un espace localement convexe séparé (non nécessairement quasi-complet), on appelle $\mathcal{H}(\mathrm{E})$ l'espace $\mathcal{H}_{\varepsilon}\mathrm{E}$, identifié aussi à $\mathcal{L}_{\varepsilon}(\mathcal{H}_{c}^{\prime};\mathrm{E})$.

C'est un sous-espace de $\mathcal{D}'(E)$, muni d'une topologie plus fine que la topologie induite. C'est l'espace des distributions $\vec{T}$ à valeurs dans E, telles que $\vec{T}$ soit une application continue de $E_c'$ dans $\mathcal{H}$; sa topologie est celle de la convergence uniforme de $\vec{T}$ sur les parties équicontinues de $E'$. $\vec{T} \to \vec{T}$ est un isomorphisme, algébrique et topologique, de $\mathcal{H}(E)$ sur $\mathscr{L}_{\epsilon}'(E_c';\mathcal{H})$. $\mathcal{H}(E)$ est quasi-complet (resp. complet) si $\mathcal{H}$ et E sont quasi-complets (resp. complets). Toutes les propriétés énoncées pour $\mathcal{H}(E)$ se voient immédiatement, en appliquant les résultats du § 1, notamment la proposition 1 (injection de $\mathcal{H}(E)$ dans $\mathcal{D}'(E)$), le corollaire 2 de la proposition 4, la proposition 3.

Pour $\mathcal{H} = \mathfrak{D}_{c}^{'m}$, on trouve $\mathcal{H}(\mathrm{E}) = \mathfrak{D}_{c}^{'m}(\mathrm{E})$, d'après la proposition 12.

Dans la suite, sauf mention expresse du contraire, ℋ et E seront supposés quasi-complets.

PROPOSITION 13. — Soit K un espace de distributions normal (non nécessairement quasi-complet), et soit E un espace localement convexe séparé (non nécessairement quasi-complet). L'espace $\mathfrak{L}_{c}(\mathfrak{K};\mathrm{E})$ est un sous-espace vectoriel topologique de $\mathfrak{K}_{c}^{\prime}(\mathrm{E})$, identique à cet espace tout entier si K a la topologie $\gamma$.

D'abord $\mathfrak{K}_{c}^{\prime}$ est un espace de distributions normal (propo-

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{D}'$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Rappelons qu'un espace de distribution sur  $R^{n}$  est un sous-espace de l'espace  $D'$  des distributions sur  $R^{n}$ , muni d'une topologie localement convexe plus fine que la topologie induite par  $D'$ .</span></small>

sition 4 des préliminaires). Il suffit ensuite d'appliquer le corollaire de la proposition 5 du § 1.

Remarque. — Si E est quasi-complet (resp. complet), et si $\mathfrak{K}$ est strictement normal (resp. normal), il suffit, pour que $\vec{T} \in \mathcal{D}'(E)$ soit dans $\mathfrak{L}(\mathfrak{K}; E)$, qu'elle soit continue sur $\mathcal{D}$ muni de la topologie induite par $\mathfrak{K}$.

Les espaces usuels et la propriété (ε).

Toute distribution $\vec{T}$ de $\mathcal{H}(E)$ est « scalairement dans $\mathcal{H}$ », autrement dit $\langle\vec{T},\vec{e'}\rangle$ est dans $\mathcal{H}$ pour tout $\vec{e'}\in E'$. Mais la réciproque n'est pas nécessairement vraie (voir exemple page 56, avec $\mathcal{H}=\mathcal{H}^{m}$). Nous introduirons alors la propriété ($\varepsilon$) relative à l'espace $\mathcal{H}$ (non nécessairement quasi-complet):

Propriété (ε): Quel que soit l'espace localement convexe séparé quasi-complet E, toute distribution T à valeurs dans E, scalairement dans H, appartient à H(E); en d'autres termes toute application linéaire T de E' dans H, continue lorsqu'on munit H de la topologie induite par D', est continue pour la topologie initiale de H.

Si un espace de distributions H a la propriété (ε), H(E) (abstraction faite de sa topologie), dépend de H et non de sa topologie; en outre il ne dépend que de la topologie affaiblie de E (voir page 50).

Il nous reste à voir si les espaces H rencontrés dans la pratique vérifient la propriété (ε); celle-ci est compliquée à vérifier, puisqu'elle fait intervenir tous les espaces E; il serait utile de la remplacer par une propriété intrinsèque. Mais les critères obtenus sont alors compliqués et inapplicables. Nous allons plutôt partir de critères suffisants simples, qui montreront que certains espaces usuels vérifient (ε); et de là passer aux autres par des méthodes particulières à chaque cas.

PROPOSITION 14. — Si K est un espace de distributions normal et métrisable, $\mathfrak{K}_{c}^{\prime}$ vérifie la propriété ($\varepsilon$).

Soit en effet $\vec{T}$ une distribution à valeurs dans E, scalairement dans $\mathcal{K}'$. Nous allons montrer que, si $\varphi$ parcourt une partie $\mathcal{K}$-bornée de $\mathcal{D}$, $\vec{T}(\varphi)$ reste bornée dans E. Pour cela il

suffit de montrer que $\vec{\mathbf{T}}(\varphi)$ reste faiblement bornée (1), donc que, pour tout $\vec{e'} \in \mathrm{E}'$, $\langle \vec{\mathbf{T}}(\varphi), \vec{e'} \rangle$ reste borné; d'après (I, 2, 1) c'est évident, puisque, par hypothèse, $\langle \vec{\mathbf{T}}, \vec{e'} \rangle$ est dans $\mathfrak{K}'$, et que $\varphi$ reste bornée dans $\mathfrak{K}$. Mais alors, $\mathfrak{K}$ étant métrisable, $\mathfrak{D}$ muni de la topologie $\mathfrak{D}_{\mathfrak{K}}$ induite par $\mathfrak{K}$ est aussi métrisable, et $\vec{\mathbf{T}}$, application linéaire de $\mathfrak{D}_{\mathfrak{K}}$ dans E qui transforme toute partie bornée de $\mathfrak{D}_{\mathfrak{K}}$ en une partie bornée de E, est continue de $\mathfrak{D}_{\mathfrak{K}}$ dans E. Comme $\mathfrak{D}$ est dense, donc strictement dense dans l'espace métrisable $\mathfrak{K}$, et que E est supposé quasi-complet, $\vec{\mathbf{T}}$ se prolonge en une application linéaire continue de $\mathfrak{K}$ dans E, donc $\vec{\mathbf{T}} \in \mathfrak{L}(\mathfrak{K}; \mathrm{E})$, et $t\vec{\mathbf{T}} \in \mathfrak{L}(\mathrm{E}_c'; \mathfrak{K}_c')$, d'où le résultat.

EXEMPLES. — Les espaces $\mathfrak{K} = \mathcal{E}^{m}$, $\mathscr{S}$, $\mathrm{L}^{p}$ pour $1 \leqslant p < \infty$, $\mathfrak{D}_{\mathrm{L}^{p}}$ pour $1 \leqslant p < \infty$, $\mathscr{R}^{\bullet}$, vérifient les propriétés voulues. Donc: $\mathcal{E}_{c}^{lm}$, $\mathscr{S}'$, $\mathrm{L}_{c}^{q}$ pour $1 < q \leqslant \infty$, $(\mathfrak{D}_{\mathrm{L}}'_{q})_{c}$ pour $1 \leqslant q \leqslant \infty$, vérifient la propriété ($\varepsilon$).

Soit maintenant $\vec{T}$ une distribution scalairement dans $\mathcal{D}^{\prime m}$. Alors si $\alpha \in \mathcal{D}$, $\alpha \vec{T}$ est scalairement dans $\mathcal{E}^{\prime m}$ (le produit multiplicatif d'une distribution vectorielle par une fonction appartenant à $\mathcal{E}$ se définit sans difficulté par

$$
(1, 2, 4)
$$

$$
\alpha \vec {\mathrm{T}} (\varphi) = \vec {\mathrm{T}} (\alpha \varphi),
$$

et l'on a

$$
(1, 2, 5) \quad \alpha \langle \vec {\mathrm{T}}, \vec {e ^ {\prime}} \rangle = \langle \alpha \vec {\mathrm{T}}, \vec {e ^ {\prime}} \rangle \quad \text { pour   tout } \quad \vec {e ^ {\prime}} \in \mathrm{E} ^ {\prime}).
$$

Cela prouve que $^{t}(\alpha\vec{T})$ est continue de $E_{c}'$ dans $\mathcal{E}_{c}^{'m}$. Mais la convergence dans $\mathfrak{D}_{c}^{'m}$ est locale sur $R^{n}$, et si, pour tout $\alpha \in \mathfrak{D}$, $\alpha S$ converge vers 0 dans $\mathcal{E}_{c}^{'m}$, cela prouve que S converge vers 0 dans $\mathfrak{D}_{c}^{'m}$. Donc $^{t}\vec{T} \in \mathfrak{L}(E_{c}'; \mathfrak{D}_{c}^{'m})$, ce qui prouve que l'espace $\mathfrak{D}_{c}^{'m}$ vérifie la propriété ($\varepsilon$).

PROPOSITION 15. — Soit H un espace de distributions normal dans lequel les parties fermées bornées sont compactes, et tel que son dual $\mathcal{H}_{\epsilon}^{\prime}$ soit strictement normal. Si en outre H a un système fondamental de voisinages de O qui sont D'-fermés dans H, alors H a la propriété ε.

(1) Toute partie faiblement bornée d'un espace localement convexe est bornée pour la topologie initiale (théorème de Mackey; BOURBAKI [2], corollaire du théorème 3, page 70).

DÉMONSTRATION. — Soit $\vec{T}$ une distribution à valeurs dans E, scalairement dans $\mathcal{H}$. Soit W un voisinage de O, convexe équilibré et $\mathcal{D}'$-fermé, de $\mathcal{H}$; comme $\vec{T}$ est continue de $E_c'$ dans $\mathcal{H}$ muni de la topologie induite par $\mathcal{D}'$, l'image réciproque $\vec{T}^{-1}(W)$ est un ensemble fermé dans $E_c'$, donc faiblement fermé dans $E'$; il est de plus convexe, équilibré et absorbant, donc c'est un voisinage fort de O dans $E'$ ($^\dagger$); comme les W forment un système fondamental de voisinages de O dans $\mathcal{H}$, cela prouve que $\vec{T}$ est continue de $E_b'$ dans $\mathcal{H}$. Sa transposée $\vec{T}$ est alors définie et continue de $\mathcal{H}_c' = \mathcal{H}_b'$ dans $E_b''$, bidual de E, muni de la topologie de la convergence uniforme sur les parties fortement bornées de $E'$; a fortiori $\vec{T}$ est continue de $\mathcal{H}_c'$ dans $E_\epsilon''$, muni de la topologie de la convergence uniforme sur les parties équicontinues de $E'$, topologie induisant sur E sa topologie initiale. Mais comme $\mathcal{D}$ est strictement dense dans $\mathcal{H}_c'$, que E est quasi-complet, et que $\vec{T}$ applique $\mathcal{D}$ dans E, elle applique aussi $\mathcal{H}_c'$ continuement dans E, donc $\vec{T} \in \mathcal{H}(E)$, et $\mathcal{H}$ vérifie bien ($\varepsilon$).

Dans la pratique, on verra en général que $\mathcal{H}$ a un système fondamental de voisinages de O $\mathcal{D}'$-fermés de la façon suivante. On constatera que toute partie équicontinue H' de $\mathcal{H}'$ est contenue dans l'adhérence faible $\overline{\mathrm{K}}'$ d'une partie équicontinue K' de $\mathcal{H}'$ contenue dans $\mathcal{D}$ (des troncatures et régularisations montreront cette propriété). Alors tout voisinage de O dans $\mathcal{H}$ contient un polaire H'o, donc contient un K'o qui est fermé dans $\mathcal{H}$ pour la topologie induite par $\mathcal{D}'$ puisque K' ⊂ $\mathcal{D}$.

Rappelons aussi que, si $\mathcal{H}$ a la propriété d'approximation par troncature et par régularisation, $\mathcal{H}_{c}^{\prime}$ est strictement normal (préliminaires, remarque $3^{\circ}$ après la proposition 4).

EXEMPLES. — $\mathcal{D}'$, $\mathcal{E}'$, $\mathcal{F}'$ et surtout $\mathcal{D}$, $\mathcal{E}$, $\mathcal{F}$, que nous n'avions pas encore obtenus, vérifient la propriété ($\varepsilon$).

Les espaces que nous avons obtenus ici rejoignent ceux de notre article antérieur (2) et avec les mêmes notations. Mais

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$t_{\mathbf{T}}^{-1}$ (W)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$t_{\mathbf{T}}^{-1}$ (W)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">E'</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">70)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Le polaire de $t_{\mathbf{T}}^{-1}$ (W) est en effet faiblement borné puisque $t_{\mathbf{T}}^{-1}$ (W) est absorbant, donc aussi borné pour la topologie initiale de E d'après le théorème de Mackey (BOURBAKI [2], corollaire du théorème 3, page 70); alors son bipolaire est un voisinage fort de O dans E', mais il coïncide avec son bipolaire puisqu'il est convexe équilibré faiblement fermé.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) SCHWARTZ [1].</span></small>

ici nous démontrons plus : nous savons maintenant que toute distribution à valeurs dans E, scalairement dans  $\varepsilon$ , est une fonction indéfiniment différentiable à valeurs dans E.

Prenons maintenant plus généralement pour espace $\mathcal{H}$ un espace $\mathcal{H}^{\infty}$ ayant les propriétés définies dans notre article antérieur. Si $\vec{T}$ est une distribution scalairement dans $\mathcal{H}^{\infty}$, elle est scalairement dans $\varepsilon$, donc $\vec{T}$ est une fonction indéfiniment différentiable à valeurs dans E; étant scalairement dans $\mathcal{H}^{\infty}$, il résulte de la définition page 102 de notre article précité qu'elle est dans $\mathcal{H}^{\infty}(E)$ tel que nous l'avions défini à ce moment, c'est-à-dire $^{\prime}\vec{T} \in \mathfrak{L}(E_{c}^{\prime}; \mathcal{H}^{\infty})$ (théorème 3, page 127 de l'article cité), donc $\mathcal{H}^{\infty}$ vérifie ($\varepsilon$).

En particulier nous voyons que les espaces $\mathcal{O}_{\mathbf{M}}$, $\mathcal{B}_{c}$, vérifient la propriété $(\varepsilon)$.

Par contre les espaces $\mathcal{H}^{m}$ étudiés dans notre article antérieur ne vérifient jamais la propriété ($\varepsilon$) pour $m$ fini. Ainsi $\mathfrak{D}^{m}$, $\varepsilon^{m}$, ne vérifient pas ($\varepsilon$). Il peut en effet arriver qu'une fonction $\vec{f}$ définie sur $\mathbb{R}^{n}$ à valeurs dans E soit scalairement $m$ fois continuement différentiable sans être $m$ fois continuement différentiable. Alors $\vec{f}$, étant scalairement continue, définit une distribution à valeurs dans E, comme nous le verrons plus tard (corollaire 1 de la proposition 21); cette distribution est scalairement dans $\varepsilon^{m}$, mais n'est pas dans $\mathcal{E}^{m}(\mathbf{E})$ (Par contre, rappelons qu'on a toujours $\mathcal{H}^{m}(\mathbf{E}) = \mathcal{H}^{m} \widehat{\otimes}_{\varepsilon} \mathbf{E} \approx \mathfrak{L}_{\varepsilon}(\mathbf{E}_{c}^{\prime}; \mathcal{H}^{m}))$ (1).

On peut aller plus loin: une distribution $\vec{T} \in \mathcal{D}'(E)$, scalairement dans $\mathcal{E}^0$, n'est pas nécessairement définie par une fonction scalairement continue à valeurs dans E. Soit $\vec{T}$ une distribution à valeurs dans E, scalairement fonction continue. Comme $\mathcal{E}^0$ a un système fondamental de voisinages $\mathcal{D}'$-fermés de O, à savoir les polaires des parties $\mathcal{E}'^0$-bornées de $\mathcal{D}$ (toute partie bornée de $\mathcal{E}'^0$ est contenue, par régularisation, dans l'adhérence, pour la topologie faible $\sigma(\mathcal{E}'^0, \mathcal{E}^0)$, d'une partie $\mathcal{E}'^0$-bornée de $\mathcal{D}$), $^\vec{T}$ est continue de $E_b'$ dans $\mathcal{E}^0$, comme nous l'avons vu dans la démonstration de la proposition 15. Par transposition $\vec{T}$ définit une application linéaire de $\mathcal{E}'^0$ dans $E''$, continue pour les topo-

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) SCHWARTZ [1], théorème 1, page 111, et théorème 3, page 127.</span></small>

logies fortes, et aussi pour les topologies $\mathcal{E}_{c}^{\prime 0}$ et $\mathrm{E}_c^\prime$ de la convergence uniforme sur les parties compactes de $\mathcal{E}^0$ et $\mathrm{E}_b^\prime$. En particulier la masse unité $\delta_x(y)$, $y \in \mathbb{R}^n$, a pour image un élément $\vec{f}(y)$ de $\mathrm{E}''$; et comme $y \to \delta_x(y)$ est une fonction continue sur $\mathbb{R}^n$ à valeurs dans $\mathcal{E}_{c}^{\prime 0}$, $y \to \vec{f}(y)$ est une fonction continue sur $\mathbb{R}^n$ à valeurs dans $\mathrm{E}_{c}''$. La relation entre $\vec{T}$ et $\vec{f}$ est la suivante. Comme $\varphi$ peut s'écrire dans $\mathcal{E}_{c}^{\prime 0}$:

$$
(1, 2; 6)
$$

$$
\varphi (\hat {x}) = \int_ {\mathbf {R} ^ {n}} \delta_ {x} (y) \varphi (y) d y,
$$

on a, dans $\mathbf{E}_c^{\prime \prime}$:

$$
(1, 2; 7)
$$

$$
\vec {\mathbf {T}} (\varphi) = \int_ {\mathbb {R} ^ {n}} \vec {f} (y) \varphi (y) d y;
$$

et $\langle\vec{T},\vec{e}^{\prime}\rangle=\langle\vec{f},\vec{e}^{\prime}\rangle$ pour tout $\vec{e}^{\prime}\in\mathrm{E}^{\prime}$. On peut donc dire que la distribution $\vec{T}$ est la fonction $\vec{f}$ à valeurs dans $\mathrm{E}_{c}^{\prime\prime}$, $\vec{T}$ étant néanmoins à valeurs dans E. Le prolongement de $\vec{T}$ à $\mathcal{E}_{c}^{\prime0}$ se définit d'ailleurs aussi par une intégrale à valeur dans $\mathrm{E}^{\prime\prime}$:

$$
\vec {\mathbf {T}} (\mu) = \int_ {\mathbb {R} ^ {n}} \vec {f} (y) d \mu (y),\tag{1, 2; 8}
$$

pour toute $\mu\in\mathcal{E}_{c}^{\prime0}$.

Ce résultat ne peut pas être amélioré, et on peut voir par un exemple que $\vec{f}$ n'est pas nécessairement à valeurs dans E. Soit $E = \mathcal{R}_z^*$, espace des fonctions indéfiniment différentiables sur $Z^n$ (dual de $R^n = X^n$) tendant vers 0 à l'infini ainsi que chacune de leurs dérivées, muni de sa topologie usuelle. Soit $\vec{T}$ la distribution sur $X^n$ à valeurs dans E définie par la transformation de Fourier $\mathcal{F}$: si $\varphi \in \mathcal{D}_x$, $\vec{T}(\varphi)$ est son image de Fourier, qui est dans $\mathcal{S}_z$ et a fortiori dans $\mathcal{R}_z^*$. Un élément $\vec{e}'$ de $E'$ est une distribution $S_z$ appartenant à $(\mathcal{D}_{L'}')_z$; d'après la relation de transposition (1, 2; 1) et la définition de l'image de Fourier d'une distribution ($\mathcal{FS}(\varphi) = S(\mathcal{F}\varphi)$), $\langle T, e' \rangle$ n'est autre que la distribution en $x$ transformée de Fourier $\mathcal{FS}$ de $S_z$; c'est une fonction continue de $x$ (1), donc $\vec{T}$ est scalairement fonction continue. $\vec{T}$ se prolonge alors en une application linéaire continue de $\mathcal{E}_c^{0'}$ dans $E_c''$; l'image de $\mu$, mesure à sup-

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) SCHWARTZ [5], chapitre vii, § 7, exemple 4, page 112.</span></small>

port compact, est encore (par continuité) son image de Fourier, mais celle-ci est dans $\mathcal{B}_{z}$, bidual de $\mathcal{B}_{z}^{\bullet}$, et non dans $\mathcal{B}_{z}^{\bullet}$ lui-même. En particulier l'image de $\delta_{x}(y)$, $y \in \mathbb{R}^{n}$, est exp ($-2i\pi y\hat{z}$), qui est dans $\mathcal{B}_{z}$ mais non dans $\mathcal{B}_{z}^{\bullet}$; la formule (1, 2; 7) est celle qui définit la transformation de Fourier:

$$
\mathcal {F} \varphi = \int_ {\mathbb {R} ^ {n}} \exp (- 2 i \pi y \hat {z}) \varphi (y) d y \in \mathcal {S} _ {z} \subset \mathcal {B} _ {z} ^ {\bullet} \subset \mathcal {B} _ {z}.\tag{I, 2; 9}
$$

Au contraire pour $m \geqslant 1$, on peut arriver à une situation meilleure. Soit $\vec{T}$ une distribution à valeurs dans E, scalairement dans $\mathcal{E}^{m}$, $m \geqslant 1$. Elle se prolongera en une application linéaire continue de $\mathcal{E}_{b}^{'m}$ dans $\mathrm{E}_{b}^{\prime \prime}$. Mais $\delta_{x}(y)$, par régularisation, est limite, dans $\mathcal{E}_{b}^{'m}$, d'une suite d'éléments de $\mathfrak{D}$, donc $\vec{f}(y)$ est limite dans $\mathrm{E}_{b}^{\prime \prime}$ et a fortiori dans $\mathrm{E}_{\varepsilon}^{\prime \prime}$ d'une suite d'éléments de E; alors, comme E est quasi-complet, $\vec{f}$ est à valeurs dans E lui-même; il y a donc identité entre les distributions scalairement fonctions $m$ fois continuement différentiables et les fonctions scalairement $m$ fois continuement différentiables. Pour $m = \infty$, on retrouverait le fait que $\mathcal{E}$ vérifie ($\varepsilon$), mais c'est à peu près la démonstration même de la proposition 15.

L'analyse utilise d'autres espaces importants, notamment $\mathcal{S}'(\Gamma)$ et $\mathcal{O}_C'$. Montrons qu'ils vérifient ($\varepsilon$). Rappelons que si $\mathbf{R}^n = \mathbf{X}^n$, et si $\Xi^n$ est le dual de $\mathbf{X}^n$ et $\Gamma$ un convexe de $\Xi^n$, $\mathcal{S}'(\Gamma)$ est l'ensemble des distributions sur $\mathbf{X}^n$ dont le produit par toute fonction $\exp(-\xi \hat{x})$, $\xi \in \Gamma$, est dans $\mathcal{S}_x'$; il est muni de la topologie la moins fine rendant continues les applications $\mathbf{T} \to \exp(-\xi \hat{x})\mathbf{T}$, $\xi \in \Gamma$, de $\mathcal{S}'(\Gamma)$ dans $\mathcal{S}'$. Soit $\vec{\mathbf{T}}$ une distribution à valeurs dans E, scalairement dans $\mathcal{S}'(\Gamma)$. Pour tout $\vec{e'} \in \mathbf{E}'$, $\langle \vec{\mathbf{T}}, \vec{e'} \rangle$ est dans $\mathcal{S}'(\Gamma)$; donc, pour tout $\xi \in \Gamma$, $\exp(-\xi \hat{x})\langle\mathbf{T}, e'\rangle$, c'est-à-dire $\langle\exp(-\xi \hat{x})\vec{\mathbf{T}}, \vec{e'} \rangle$, est dans $\mathcal{S}'$; comme $\mathcal{S}'$ vérifie ($\varepsilon$), cela signifie que, si $\vec{e'}$ converge vers 0 dans $\mathbf{E}_c'$, $\langle\exp(-\xi \hat{x})\vec{\mathbf{T}}, \vec{e'} \rangle$ converge vers 0 dans $\mathcal{S}'$, donc que $\langle\vec{\mathbf{T}}, \vec{e'} \rangle$ converge vers 0 dans $\mathcal{S}'(\Gamma)$; donc $^\prime\vec{\mathbf{T}}$ applique continuement $\mathbf{E}_c'$ dans $\mathcal{S}'(\Gamma)$, et $\mathcal{S}'(\Gamma)$ vérifie la propriété ($\varepsilon$).

En outre $\vec{T} \in \mathcal{D}'(E)$ est dans $(\mathscr{S}'(\Gamma))(E)$ si et seulement si, pour tout $\xi \in \Gamma$, $\exp (-\xi \hat{x})\vec{T}$ est dans $\mathscr{S}'(E)$.

Soit maintenant $\overline{\mathbf{T}}$ une distribution à valeurs dans E, scalaire-

ment dans $\mathcal{O}_{\mathrm{G}}^{\prime}$. Elle est a fortiori scalairement dans $\mathcal{S}^{\prime}$, donc $\tilde{\mathbf{T}}$ applique continuement $\mathbf{E}_{c}^{\prime}$ dans $\mathcal{S}^{\prime}$. Soit $\mathcal{F}$ la transformation de Fourier. L'application $\mathcal{F} \circ {}^t\mathbf{T}$ de $\mathbf{E}^{\prime}$ dans $\mathcal{S}^{\prime}$ est continue, et elle applique $\mathbf{E}^{\prime}$ dans $\mathcal{O}_{\mathrm{M}}$; comme $\mathcal{O}_{\mathrm{M}}$ vérifie ($\varepsilon$), elle est continue de $\mathbf{E}_{c}^{\prime}$ dans $\mathcal{O}_{\mathrm{M}}$, donc ${}^t\mathbf{T}$ est continue de $\mathbf{E}_{c}^{\prime}$ dans $\mathcal{O}_{\mathrm{G}}^{\prime}$, et l'espace $\mathcal{O}_{\mathrm{C}}^{\prime}$ vérifie la propriété ($\varepsilon$).

On peut conclure comme suit ce que nous venons de voir (en y ajoutant les résultats des préliminaires):

PROPOSITION 16. — Les espaces $\mathfrak{D}^{m}$, $\mathfrak{E}^{m}$, $\mathcal{B}_{c}^{m}$, $\mathscr{F}$, $\mathcal{O}_{\mathrm{M}}$, $\mathrm{L}_{c}^{q}$ (pour $1 < q \leqslant \infty$), $(\mathfrak{D}_{\mathrm{L}}^{\prime q})_{c}$ (pour $1 \leqslant q \leqslant \infty$), $\mathcal{D}_{c}^{\prime m}$, $\mathfrak{E}_{c}^{\prime m}$, $\mathscr{F}^{\prime}$, $\mathscr{F}^{\prime}(\Gamma)$, $\mathcal{O}_{\mathrm{G}}^{\prime}$, sont des espaces de distributions strictement normaux, ayant les propriétés d'approximation par troncature et par régularisation, et la propriété d'approximation stricte; ils ont tous la propriété ($\varepsilon$), sauf $\mathfrak{D}^{m}$, $\mathfrak{E}^{m}$ et $\mathcal{B}_{c}^{m}$ pour $m$ fini.

Pour les différents espaces $\mathcal{H}$ donnés dans cet énoncé, on a une interprétation simple de $\mathcal{H}(\mathrm{E})$. Donnons encore l'interprétation de $\mathcal{B}^{\bullet}(\mathrm{E})$:

PROPOSITION 17. — L'espace $\mathcal{B}^{\bullet}(\mathrm{E})$ est l'espace des fonctions indéfiniment dérivables à valeurs dans E, convergeant vers 0 à l'infini ainsi que chacune de leurs dérivées : sa topologie est celle de la convergence uniforme sur $\mathbf{R}^{n}$ de chaque dérivée. Si $\mathbf{X}^{\iota}$ et $\mathbf{Y}^{m}$ sont deux espaces euclidiens, $\mathcal{B}_{x,y}^{\bullet} = \mathcal{B}_{x}^{\bullet} \widehat{\otimes}_{\varepsilon} \mathcal{B}_{y}^{\bullet}$.

1° Soit en effet $\vec{f} \in \mathcal{B}^{\bullet}(E)$. Alors $\vec{f} \in \mathcal{E}(E)$, donc c'est une fonction indéfiniment dérivable à valeurs dans E. Mais on sait que $T \to \vec{f}(T)$ est une application linéaire continue de $(\mathcal{B}^{\bullet})_{c}'$ dans E. Lorsque $\xi \in h^{n}$ s'éloigne indéfiniment dans $R^{n}$, la distribution $D^{p}(\delta(\hat{x} - \xi))$ reste dans une partie équicontinue de $\mathcal{D}_{L'}'$, et converge vers 0 simplement sur le sous-ensemble dense $\mathcal{D}$ de $\mathcal{B}^{\bullet}$, donc converge vers 0 dans $(\mathcal{B}^{\bullet})_{c}'')$; alors $\vec{f}\big(D^{p}(\delta(\hat{x} - \xi))\big) = (-1)^{|p|} D^{p} \vec{f}(\xi)$ converge vers 0 pour $|\xi| \to \infty$, donc $\vec{f}$ converge vers 0 à l'infini sur $R^{n}$, ainsi que chacune de ses dérivées; ceci ne suppose pas E quasi-complet. Réciproquement, soit $\vec{f}$ une fonction à valeurs dans E, indéfiniment dérivable, convergeant vers 0 à l'infini ainsi que chacune de ses dérivées. Alors $\vec{e}' \to \langle \vec{f}, \vec{e}' \rangle$ est une application linéaire de $E'$

(1) BOURBAKI [2], proposition 5, page 23.

dans $\mathcal{B}^{\bullet}$; comme l'ensemble des valeurs de $\mathrm{D}^{p}\vec{f}(x)$, $x\in\mathbb{R}^{n}$, pour $p$ fixé, est une partie relativement compacte de E, on voit que, si $\vec{e}^{\prime}$ converge vers 0 dans $\mathrm{E}_{c}^{\prime}$, donc uniformément sur toute partie compacte de E supposé quasi-complet, $\langle\vec{f},\vec{e}^{\prime}\rangle$ converge vers 0 dans $\mathcal{B}^{\bullet}$. Donc $\vec{f}$ est continue de $\mathrm{E}_{c}^{\prime}$ dans $\mathcal{B}^{\bullet}$ et $\vec{f}\in\mathcal{B}^{\bullet}(\mathrm{E})$.

Enfin la topologie de $\mathcal{B}^{\bullet}(\mathrm{E})\approx\mathfrak{L}_{\varepsilon}(\mathrm{E}_{c}^{\prime};\mathcal{B}^{\bullet})$ est celle de la convergence uniforme sur $\mathrm{R}^{n}$ de chaque dérivée $\mathrm{D}^{p}\langle\vec{f},\vec{e}^{\prime}\rangle$, uniformément sur toute partie équicontinue de $\mathrm{E}^{\prime}$, c'est-à-dire celle de la convergence uniforme sur $\mathrm{R}^{n}$ de chaque dérivée $\mathrm{D}^{p}\vec{f}$. 2° Si alors $\mathrm{X}^{l}$ et $\mathrm{Y}^{m}$ sont deux espaces euclidiens, $\mathcal{B}_{x}^{\bullet}\widehat{\otimes}_{\varepsilon}\mathcal{B}_{y}^{\bullet}= \mathcal{B}_{x}^{\bullet}\varepsilon\mathcal{B}_{y}^{\bullet}$ (corollaire 1 de la proposition 11) = $\mathcal{B}_{x}^{\bullet}(\mathcal{B}_{y}^{\bullet})\approx\mathcal{B}_{y}^{\bullet}(\mathcal{B}_{x}^{\bullet})$. Montrons que cet espace n'est autre que $\mathcal{B}_{x,y}^{\bullet}$. Tout d'abord, c'est un sous-espace de $\mathcal{E}_{x}\widehat{\otimes}_{\varepsilon}\mathcal{E}_{y}$, muni d'une topologie plus fine que la topologie induite (proposition 1); et on sait que $\mathcal{E}_{x}\widehat{\otimes}_{\varepsilon}\mathcal{E}_{y}$ peut être identifié à $\mathcal{E}_{x,y}(^{i})$. Soit alors $f\in\mathcal{B}_{x}^{\bullet}\widehat{\otimes}_{\varepsilon}\mathcal{B}_{y}^{\bullet}$. En la considérant comme élément de $\mathcal{B}_{x}^{\bullet}(\mathcal{B}_{y}^{\bullet})$, elle définit, d'après ce que nous avons vu, une fonction indéfiniment dérivable $\vec{f}$ sur $\mathrm{X}^{l}$, à valeurs dans $\mathcal{B}_{y}^{\bullet}$, convergeant vers 0 à l'infini sur $\mathrm{X}^{l}$, ainsi que chacune de ses dérivées ($\vec{f}(x)=f(x,\hat{y})$). Soit $\mathcal{V}_{q}$ le voisinage de 0 de $\mathcal{B}_{y}^{\bullet}$ formé des fonctions dont la dérivée $\mathrm{D}^{q}$ est majorée en module par $\varepsilon$; alors $\mathrm{D}^{p}\vec{f}(x)\in\mathcal{V}_{q}$ pour $|x|\geqslant\mathrm{A}_{p}$ convenable, autrement dit

$$
\left| \mathrm{D} _ {x} ^ {p} \mathrm{D} _ {y} ^ {q} f (x, y) \right| \leqslant \varepsilon \quad \text { pour } \quad | x | \geqslant \mathrm{A} _ {p};
$$

$f$ converge vers 0, ainsi que chacune de ses dérivées, lorsque $|x|\to\infty$. Mais $f$ définit aussi une fonction $\vec{f}$ indéfiniment dérivable sur $Y^{m}$ à valeurs dans $\mathcal{B}_{x}^{\bullet}$, convergeant vers 0 à l'infini sur $Y^{m}$ ainsi que chacune de ses dérivées $(\vec{f}(y)=f(\hat{x},y))$, et le même raisonnement que ci-dessus montre alors que $f$ converge vers 0, ainsi que chacune de ses dérivées, pour $|y|\to\infty$; finalement $f$ converge vers 0 ainsi que chacune de ses dérivées quand $|x|$ ou $|y|$ tend vers l'infini, $f\in\mathcal{B}_{x,y}^{\bullet}$.

Réciproquement, soit $f \in \mathcal{R}_{x,y}^{\bullet}$. La fonction $\vec{f}$ définie sur $X^{\iota}$ à valeurs dans $\mathcal{E}_{y}$ par la formule ci-dessus est indéfiniment dérivable. Mais chacune de ses dérivées $D^{p}\vec{f}$ est une fonction

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Schwartz [1], proposition 12, page 113.</span></small>

continue sur $X^l$ à valeurs dans $\mathcal{R}_y^\bullet$, donc, d'après un lemme (') sur la dérivation des fonctions à valeurs vectorielles, $\vec{f}$ est indéfiniment dérivable sur $X^l$ à valeurs dans $\mathcal{R}_y^\bullet$; de plus, elle converge évidemment vers 0 à l'infini sur $X^l$, ainsi que chacune de ses dérivées, puisque $f$ converge vers 0, ainsi que chacune de ses dérivées, pour $|x| \to \infty$; donc on a bien $\vec{f} \in \mathcal{R}_x^\bullet (\mathcal{R}_y^\bullet)$, ou $f \in \mathcal{R}_x^\bullet \widehat{\otimes}_{\epsilon} \mathcal{R}_y^\bullet$.

La topologie de l'espace $\mathcal{B}_{x}^{*}(\mathcal{B}_{y}^{*})$ est celle de la convergence uniforme sur $X^{l}$ de chaque dérivée $D^{p}\vec{f}$, c'est-à-dire celle de la convergence uniforme sur $X^{l}\times Y^{m}$ de chaque dérivée $D_{x}^{p}D_{y}^{q}f$, c'est-à-dire la topologie de $\mathcal{B}_{x,y}^{*}$,

c.q.f.d.

## Les espaces  $\overline{\mathcal{H}}(\mathrm{E})$  pour certains espaces H.

$1^{\circ} \overline{\mathcal{E}}^{m}(E)$ sera le sous-espace de $\mathfrak{D}^{m}(E)$ constitué par les distributions à valeurs dans $E$ à support compact (le support d'une distribution à valeurs vectorielles se définit comme pour une distribution à valeurs scalaires: une distribution est nulle dans un ouvert $\Omega$ de $R^n$ si $\vec{T}(\varphi) = 0$ toutes les fois que $\varphi$ a son support dans $\Omega$; la partition de l'unité montre que toute réunion d'ouverts où $\vec{T}$ est nulle est un ouvert où $\vec{T}$ est nulle; le support de $\vec{T}$ est le complémentaire du plus grand ouvert de $R^n$ où $\vec{T}$ soit nulle. Pour que $\vec{T}$ soit nulle dans $\Omega$, il faut et il suffit que $\langle \vec{T}, \vec{e}' \rangle$ soit nulle dans $\Omega$ pour tout $\vec{e}' \in E'$; le support de $\vec{T}$ est donc l'adhérence de la réunion des supports des distributions scalaires $\langle \vec{T}, \vec{e}' \rangle$ lorsque $\vec{e}'$ parcourt $E'$). On sait que, pour $m = \infty$, $\mathcal{E}'$ est la limite inductive des $\mathcal{E}_K'$, K compacts de $R^n$ (car la limite inductive des $\mathcal{E}_K'$ est une topologie plus fine que $\mathcal{E}'$; mais elles ont les mêmes parties bornées, les parties bornées des $\mathcal{E}_K'(2)$, et comme $\mathcal{E}'$ est bornologique ($\S 1$, page 44), il a la topologie localement convexe la plus fine compatible avec ses parties bornées, donc les deux topologies sont bien identiques).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\pmb{\varepsilon}_{\mathbf{K}}^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\bar{\mathcal{E}}^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\varepsilon_{\mathbf{k}}^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\varepsilon_{\mathbf{k}}^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Schwartz [1], lemme 1, page 145.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) Toute partie bornée de $\mathcal{E}'$ est bornée dans un $\mathcal{E}_{\mathbf{K}}'$ (Schwartz [4], remarques suivant le théorème XXV du chapitre III); une partie bornée de la limite inductive des $\mathcal{E}_{\mathbf{K}}'$ est aussi une partie bornée d'un $\mathcal{E}_{\mathbf{K}}'$ (BOURBAKI [2], proposition 6, page 8).</span></small>

On pourra donc définir aussi sur $\mathcal{E}'(E)$ la topologie limite inductive des $\mathcal{E}_{\mathbf{k}}'(E)$. Nous ne définirons pas de topologie sur $\overline{\mathcal{E}'}^{m}(E)$ pour $m$ fini. Il est clair que $\overline{\mathcal{E}'}^{m}(E) \subset \mathcal{E}_c'^{m}(E)$; mais ces espaces sont en général distincts. D'après la proposition 16, $\mathcal{E}_c'^{m}(E)$ est l'espace des distributions d'ordre $\leqslant m$ scalairement à support compact, ce qui signifie seulement que $\langle \vec{T}, \vec{e}' \rangle$ est à support compact pour tout $\vec{e}' \in E'$. Par exemple si $E = \mathcal{E}^m$, la distribution « identique », application identique de $\mathcal{E}^m$ dans $\mathcal{E}^m$, appartient à $\mathcal{E}_c'^{m}(\mathcal{E}^m) = \mathfrak{L}_c(\mathcal{E}^m; \mathcal{E}^m)$, mais son support est l'espace entier, donc elle n'appartient pas à $\overline{\mathcal{E}'}^{m}(\mathcal{E}^m)$.

L'espace $\mathcal{E}'(E)$ est lui aussi localement convexe séparé quasi-complet, et complet si $E$ est complet, car il est limite inductive stricte d'une suite d'espaces quasi-complets ou complets (1). La topologie de $\mathcal{E}'(E)$ est plus fine que la topologie induite par $\mathcal{E}'(E)$, puisque sur $\mathcal{E}_{K}'(E)$ elles coïncident; en général elle sera strictement plus fine.

Si E est un espace de Banach, ou plus généralement un espace (DF), les espaces $\mathcal{E}'(E)$ et $\bar{\mathcal{E}}'(E)$ sont algébriquement identiques. En effet, si $\vec{T} \in \mathcal{E}'(E)$, $\vec{T}$ est une application linéaire continue de $\mathcal{E}$ dans E (proposition 13), et en vertu des hypothèses faites sur E, on sait qu'il existe un ouvert U de $\mathcal{E}$ dont l'image $\vec{T}(U)$ est bornée ($^2$); mais il existe un compact K de $R^n$ tel que toute fonction $k\varphi$, où $k$ est un scalaire et où $\varphi$ a

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{K}\subset \mathbf{K}^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\pmb{\varepsilon}_{\mathbf{K}}(\dot{\mathbf{E}})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">L, c'est</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\varepsilon_{\mathbf{k}}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Une limite inductive stricte d'espaces complets est complète d'après KöTHE [1]. Une limite inductive stricte L d'espaces quasi-complets L est quasi-complète; si en effet F est un filtre de Cauchy borné sur L, c'est un filtre de Cauchy borné sur un L, (BOURBAKI [2], proposition 6, page 8 et [1], proposition 3, page 64) donc convergent. Comme, pour K ⊂ K', la topologie de $\mathcal{E}_{\mathbf{K}}$ est induite par la topologie de $\mathcal{E}_{\mathbf{K}'}$, la topologie $\mathcal{E}_{\mathbf{K}}(\mathbf{E})$ est aussi induite par $\mathcal{E}_{\mathbf{K}'}(\mathbf{E})$ (chapitre 1, § 1, proposition 1); d'ailleurs tous les $\mathcal{E}_{\mathbf{K}}(\mathbf{E})$ ont pour topologie la topologie induite par $\mathcal{D}'(\mathbf{E})$; donc la limite inductive des $\mathcal{E}_{\mathbf{K}}'$(E) est bien stricte.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\pmb{\varepsilon}_{\mathbf{K}}(\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\widetilde{\mathcal{E}}_{\mathbf{K}^{\prime}}(\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{E}_{\mathbf{K}^{\prime}}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{D}^{\prime}(\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{L}_{s}(\mathbf{L};\mathbf{M})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{L} \times \bar{\mathbf{M}}'$,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">M'</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{L} \times \mathbf{M}'$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) Si L est un espace de Fréchet, M un espace du type (DF), toute application linéaire continue de L dans M est bornée, et tout ensemble borné H de $\mathcal{L}_{s}(L;M)$ est équiborné. En effet on peut identifier H à un ensemble de formes bilinéaires séparément continues sur $L \times M'$, borné pour la topologie de la convergence simple sur $L \times M'$. Mais L et $M'$ sont des espaces de Fréchet (GROTHENDIECK [2], page 64 en haut), alors H est séparément équicontinu sur $L \times M'$ (BOURBAKI [2], théorème 2, page 27), donc équicontinu (BOURBAKI [2], proposition 10, page 43). Cela signifie bien qu'il existe un voisinage $\mathcal{U}$ de O dans L tel que $\bigcup_{u \in H} u(\mathcal{U})$ soit borné dans M, donc que H est équiborné.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{L} \times \dot{\mathbf{M}}'$</span></small>

son support dans $\int K$, soit dans $U$; alors $\vec{T}(\varphi) = 0$ si $\varphi$ a son support dans $\int K$, autrement dit $\vec{T}$ a son support dans $K$, et $\vec{T} \in \bar{\mathcal{E}}'(E)$. Dans les mêmes conditions $\mathcal{E}'(E)$ et $\bar{\mathcal{E}}'(E)$ sont topologiquement identiques, d'après un résultat de Grothendieck (1). Ceci s'applique en particulier à $E = \mathcal{E}'$, $\mathcal{F}'$, $\mathfrak{D}_{L^q}^t(1 \leqslant q \leqslant \infty)$.

Par ailleurs, si dans E il existe un voisinage de O ne contenant aucune droite issue de l'origine, $\mathcal{E}'(E)$ et $\overline{\mathcal{E}'}(E)$ sont encore algébriquement identiques. Soit en effet $\vec{T} \in \mathcal{E}'(E)$. L'application $\vec{T}$ étant continue de $E_c'$ dans $\mathcal{E}'$, $\langle \vec{T}, \vec{e}' \rangle$ reste borné dans $\mathcal{E}'$ et par suite garde son support dans un compact fixe $K(H')$ de $R^n$ lorsque $\vec{e}'$ parcourt une partie équicontinue $H'$ de $E'$; or l'hypothèse faite sur E revient à dire, par dualité, qu'il existe une partie équicontinue $H_0'$ de $E'$ qui engendre un sous-espace faiblement dense, alors $\langle \vec{T}, \vec{e}' \rangle$ a son support dans $K(H_0')$ pour tout $\vec{e}' \in E'$ et par suite $\vec{T}$ a son support dans $K(H_0')$, $\vec{T} \in \overline{\mathcal{E}'}(E)$. La propriété énoncée pour E revient à dire qu'il existe une norme continue sur E. L'espace $\mathfrak{D}^m$ (qui n'est pas du type (DF)) a cette propriété, car $\varphi \to \sup_{x \in R^n} |\varphi(x)|$ est

une norme continue. Au contraire, nous avons vu plus haut que $\overline{\mathcal{E}^{\prime}}(\mathcal{E})$ est distinct de $\mathcal{E}^{\prime}(\mathcal{E})$.

2° Nous avons déjà étudié l'espace $\mathfrak{D}^{m}(\mathrm{E})$, limite inductive

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{K}_i$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">47,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$|x| \leq i$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{E}_i = \varepsilon_{\mathbf{k}_i}^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}^{\prime}\widehat{\otimes}_{\pi}\mathbf{E}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$R^{n}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">F = E</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}_{\mathbf{K}_i}^{\prime}\widehat{\otimes}_{\pi}\mathbf{E}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{E}^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\pmb{\varepsilon}_{\mathbf{K}}^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{E}^{\prime}\widehat{\otimes}_{\pi}\mathbf{E} = \mathcal{E}^{\prime}\widehat{\otimes}_{\cdot}\mathbf{E} = \mathcal{E}^{\prime}(\widehat{\mathbf{E}})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}_{\mathbf{K}_i}^{\prime}\widehat{\otimes}_{\pi}\mathbf{E} = \mathfrak{E}_{\mathbf{K}_i}^{\prime}\widehat{\otimes}_{\varepsilon}\mathbf{E} = \mathfrak{E}_{\mathbf{K}_i}^{\prime}(\widehat{\mathbf{E}})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}_{\mathbf{k}}^{\prime}(\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) GROTHENDIECK [4], corollaire de la proposition 6, page 47, appliqué à $E_i = \mathcal{E}_{\mathbf{K}_i}^{\prime}$, où $K_i$ est le compact $|x| \leqslant i$ dans $R^n$, et $F = E$ du type (DF); ce corollaire montre que $\mathcal{E}' \widehat{\otimes}_{\pi} E$ est la limite inductive des $\mathcal{E}_{\mathbf{K}_i}' \widehat{\otimes}_{\pi} E$; mais comme $\mathcal{E}'$ et ses sous-espaces $\mathcal{E}_{\mathbf{K}}'$ sont nucléaires (donc vérifient la propriété d'approximation, SCHWARTZ [2], exposé 17, proposition 4), $\mathcal{E}' \widehat{\otimes}_{\pi} E = \mathcal{E}' \widehat{\otimes}_{:} E = \mathcal{E}'(\widehat{E})$ et $\mathcal{E}_{\mathbf{K}_i}' \widehat{\otimes}_{\pi} E = \mathcal{E}_{\mathbf{K}_i}' \widehat{\otimes}_{:} E = \mathcal{E}_{\mathbf{K}_i}'(\widehat{E})$, d'où la conclusion lorsque $E$ est complet. Pour $E$ non complet, le résultat est encore valable. En effet, nous allons montrer que le dual de $\mathcal{E}'(E)$ et de la limite inductive $G$ des $\mathcal{E}_{\mathbf{K}}'(E)$ sont les mêmes, avec les mêmes parties équicontinues, ce qui montrera l'identité des topologies de $\mathcal{E}'(E)$ et de $G$. Soit donc $u$ une forme linéaire continue sur $G$, c'est-à-dire une forme linéaire sur $\mathcal{E}'(E)$ dont la restriction à chaque $\mathcal{E}_{\mathbf{K}}(E)$ soit continue. Comme $\mathcal{E}_{\mathbf{K}}'(E)$ est dense dans $\mathcal{E}_{\mathbf{K}}'(E)$ (puisque même $\mathcal{E}_{\mathbf{K}}' \otimes E$ est dense dans $\mathcal{E}_{\mathbf{K}}'(E)$), $u$ se prolonge en une forme linéaire continue $u_{\mathbf{K}}$ sur $\mathcal{E}_{\mathbf{K}}'(E)$; si $K \subset K'$, $u_{\mathbf{K}}$ est la restriction de $u_{\mathbf{K}'}$, donc l'ensemble des $u_{\mathbf{K}}$ définit un prolongement de $u$ en une forme linéaire $u$ sur $\mathcal{E}'(E)$, dont la restriction à chaque $\mathcal{E}_{\mathbf{K}}'(E)$ est continue. Comme $\mathcal{E}'(E)$ est la limite inductive des $\mathcal{E}_{\mathbf{K}}'(E)$, $u$ est continue sur $\mathcal{E}'(E)$, et par suite $u$ est continue sur $\mathcal{E}'(E)$. Même raisonnement pour les ensembles équicontinus de formes linéaires.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">G,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}^{\prime}(\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}^{\prime}(\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">G.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}^{\prime}(\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}_{\mathbf{K}}^{\prime}(\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}_{\mathbf{K}}^{\prime}(\widehat{\mathbf{E}})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{E}_{\mathbf{k}}^{\prime}\left(\widehat{\mathbf{E}}\right)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}_{\mathbf{K}}^{\prime}\otimes \mathbf{E}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}_{\mathbf{K}}(\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$u_{\mathbf{K}}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}_{\mathbf{K}}^{\prime}\big(\widehat{\mathrm{E}}\big);\mathrm{si}\mathbf{K}\subset \mathbf{K}^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$u_{K'}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}^{\prime}(\widehat{\mathbf{E}})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$u_{\mathbf{K}}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}_{\mathbf{K}}^{\prime}(\widehat{\mathbf{E}})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}^{\prime}\big(\widehat{\mathbf{E}}\big)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\varepsilon_{\mathbf{k}}^{\prime}(\widehat{\mathbf{E}})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}^{\prime}(\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{E}^{\prime}(\widehat{\mathbf{E}})$</span></small>

des $\mathfrak{D}_{\mathbf{k}}^{m}(\mathbf{E})$ (1). Toutes les fois que $\mathcal{E}'(\mathbf{E})$ et $\overline{\mathcal{E}'}(\mathbf{E})$ coïncident algébriquement, il en est évidemment de même de $\mathfrak{D}^{m}(\mathbf{E})$ et $\overline{\mathfrak{D}^{m}}(\mathbf{E})$.

3° Nous avons étudié antérieurement l'espace  $\overline{\mathcal{B}}^{m}(\mathrm{E})$  (2).

Propriétés d'hypocontinuité.

PROPOSITION 18. — Soit H un espace de distributions normal. La forme trilinéaire

$$
(\vec {\mathrm{T}}, \varphi , \vec {e ^ {\prime}}) \rightarrow \langle \langle \vec {\mathrm{T}}, \varphi , \vec {e ^ {\prime}} \rangle \rangle = \langle \vec {\mathrm{T}} (\varphi), \vec {e ^ {\prime}} \rangle = \langle \vec {\mathrm{T}}, \vec {e ^ {\prime}} \rangle (\varphi)
$$

sur $\mathcal{H}(\mathrm{E})\times\mathcal{H}_{c}^{\prime}\times\mathrm{E}_{c}^{\prime}$ est hypocontinue par rapport aux parties compactes de $\mathcal{H}(\mathrm{E})$, et aux parties équicontinues de $\mathcal{H}^{\prime}$ et $\mathrm{E}^{\prime}$. L'application bilinéaire $(\vec{\mathrm{T}},\varphi)\to\vec{\mathrm{T}}(\varphi)$ de $\mathcal{H}(\mathrm{E})\times\mathcal{H}_{c}^{\prime}$ dans $\mathrm{E}$ est hypocontinue par rapport aux parties compactes de $\mathcal{H}(\mathrm{E})$ et aux parties équicontinues de $\mathcal{H}^{\prime}$, et l'image par cette application du produit d'une partie relativement compacte de $\mathcal{H}(\mathrm{E})$ par une partie équicontinue de $\mathcal{H}^{\prime}$ est relativement compacte dans $\mathrm{E}$. L'application bilinéaire $(\vec{\mathrm{T}},\vec{e}^{\prime})\to\langle\vec{\mathrm{T}},\vec{e}^{\prime}\rangle$ de $\mathcal{H}(\mathrm{E})\times\mathrm{E}_{c}^{\prime}$ dans $\mathcal{H}$ est hypocontinue par rapport aux parties compactes de $\mathcal{H}(\mathrm{E})$ et aux parties équicontinues de $\mathrm{E}^{\prime}$, et l'image par cette application du produit d'une partie relativement compacte de $\mathcal{H}(\mathrm{E})$ et d'une partie équicontinue de $\mathrm{E}^{\prime}$ est relativement compacte dans $\mathcal{H}$.

Il suffit d'appliquer le corollaire 1 de la proposition 4 du § 1.

Remarques. — 1° Cet énoncé suppose $\mathcal{H}$ et E quasi-complets. Toutefois, même s'ils ne le sont pas, $(\vec{\mathrm{T}}, \vec{e'}) \to \langle \vec{\mathrm{T}}, \vec{e'} \rangle$ reste hypocontinue de $(\mathcal{H}(\mathrm{E}) \approx \mathcal{L}_t(\mathrm{E}_c'; \mathcal{H})) \times \mathrm{E}_c'$ dans $\mathcal{H}$ par rapport aux parties équicontinues de $\mathcal{L}(\mathrm{E}_c'; \mathcal{H})$ et de $\mathrm{E}_c'$; elle est donc continue sur le produit de $\mathcal{H}(\mathrm{E})$ par une partie équicontinue de $\mathrm{E}'$, donc a fortiori sur le produit d'une partie relativement compacte de $\mathcal{H}(\mathrm{E})$ et d'une partie équicontinue de $\mathrm{E}'$; cela suffit pour que l'image de ce produit, relativement compact dans $\mathcal{H}(\mathrm{E}) \times \mathrm{E}_c'$, soit relativement compacte dans $\mathcal{H}$.

Dans les mêmes conditions, l'image par $(\vec{\mathrm{T}},\varphi)\to \vec{\mathrm{T}} (\varphi)$ du produit d'une partie relativement compacte de $\mathcal{H}(\mathrm{E})$ et d'une partie équicontinue de $\mathcal{H}'$ est relativement compacte dans E.

$2^{\circ}$ Si $\mathfrak{K}$ est un espace de distributions normal, ayant la topologie $\gamma$, en

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{D}^m (\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{D}^m (\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\tilde{\mathfrak{D}}^{m}(\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{B}^m (\mathbf{E})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) SCHWARTZ [1], pages 94-96. $\overline{\mathfrak{D}^{m}}(\mathrm{E})$ s'appelait alors, rappelons-le, $\mathfrak{D}^{m}(\mathrm{E})$, tandis que c'est $\mathfrak{D}^{m}(\mathrm{E})$ qui s'appelait $\tilde{\mathfrak{D}}^{m}(\mathrm{E})$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) SCHWARTZ [1], page 97. $\mathcal{B}^{m}(\mathbf{E})$ s'appelait alors $\mathcal{B}^{m}(\mathbf{E})$.</span></small>

posant $\mathcal{H} = \mathcal{K}_c'$, on a $\mathcal{H}_c' = \mathcal{K}$. Si E est quasi-complet, et si $\mathcal{K}_c'$ est quasi-complet (sans qu'il soit nécessaire de supposer $\mathcal{K}$ lui-même quasi-complet), on a un énoncé analogue à celui de la proposition 18, en remplaçant $\mathcal{H}$ par $\mathcal{K}_c'$, $\mathcal{H}_c'$ par $\mathcal{K}$, et les parties équicontinues de $\mathcal{H}'$ par les parties convexes équilibrées compactes de $\mathcal{K}$.

3° On a une proposition analogue à 18, en remplacant $\mathcal{H}_{c}^{\prime}$ et $E_{c}^{\prime}$ par $\mathcal{H}_{b}^{\prime}$ et $E_{b}^{\prime}$, et les parties relativement compactes par les parties bornées, même si $\mathcal{H}$ et E ne sont pas quasi-complets (en vertu du corollaire de la proposition $2^{bis}$).

## § 3. Exemples de distributions à valeurs vectorielles et propriétés algébriques et topologiques.

Nous avons déjà rencontré des exemples importants: si  $T \in H$ ,  $\vec{e} \in E$ ,  $T \otimes \vec{e}$  est une distribution à valeur dans E appartenant à  $\mathcal{H}(E)$ .

Distributions définies par des fonctions.

DÉFINITION. — On dit qu'une fonction $\vec{f}$, définie presque partout sur $\mathbb{R}^n$ à valeurs dans $\mathbb{E}$, définit une distribution à valeurs dans $\mathbb{E}$, si $\vec{f}$ est scalairement localement sommable, c'est-à-dire si $\langle \vec{f},\vec{e}'\rangle$ est localement sommable pour tout $\vec{e}'\in \mathbb{E}'$, et si l'application linéaire $\vec{e}'\to \langle \vec{f},\vec{e}'\rangle$ est continue de $\mathbb{E}_c'$ dans $\mathfrak{D}'$. La distribution $\vec{T}$ définie par $\vec{f}$ est l'unique distribution $\vec{T}$ telle que $\langle \vec{T},\vec{e}'\rangle = \langle \vec{f},\vec{e}'\rangle$ pour tout $\vec{e}'\in \mathbb{E}'$; on identifie $\vec{f}$ à $\vec{T}$ et l'on écrit $\vec{T} = \vec{f}$.

Remarques. — 1° Si $\vec{f}$ définit une distribution, celle-ci est scalairement une mesure, donc $\vec{f}$ définit une mesure ou distribution d'ordre 0 à valeurs dans E : $\vec{f} \in \mathcal{D}'^0(\mathrm{E})$.

Soit $\vec{f}$ une fonction scalairement localement sommable. On peut toujours définir un élément $\vec{f}(\varphi)$ du dual algébrique E' \* de E' par l'égalité

$$
\langle \vec {f} (\varphi), \vec {e ^ {\prime}} \rangle = \langle \vec {f}, \vec {e ^ {\prime}} \rangle (\varphi) = \int_ {\mathbf {R} ^ {n}} \langle \vec {f} (x), \vec {e ^ {\prime}} \rangle \varphi (x) d x\tag{I, 3; 1}
$$

pour tout $\vec{e}' \in \mathbf{E}'$.

$\vec{f}$ définit alors une application linéaire de $\mathfrak{D}$ dans $\mathrm{E}^{\prime*}$; si $\varphi$ converge vers 0 dans $\mathfrak{D}, \langle \vec{f}, \vec{e}^{\prime} \rangle(\varphi)$ converge vers 0 pour $\vec{e}^{\prime}$ fixé, donc $\vec{f}(\varphi)$ converge vers 0 dans $\mathrm{E}^{\prime*}$ pour la topologie $\sigma(\mathrm{E}^{\prime*}, \mathrm{E}^{\prime})$. Autrement dit $\vec{f}$ définit toujours une distribution à valeurs dans $\mathrm{E}^{\prime*}$ muni de la topologie $\sigma(\mathrm{E}^{\prime*}, \mathrm{E}^{\prime})$.

2º Pour que 2 fonctions $f$, $g$, définissent la même distribution, il faut et il suffit qu'elles soient scalairement presque partout égales; cela revient à dire qu'elles sont presque partout égales, s'il existe dans E' un ensemble dénombrable faiblement dense (1).

PROPOSITION 19. — Pour qu'une fonction $\vec{f}$, définie presque partout sur $\mathbf{R}^n$, à valeurs dans l'espace localement convexe séparé (non nécessairement quasi-complet) E, et scalairement localement sommable, définisse une distribution sur $\mathbf{R}^n$ à valeurs dans E, il faut et il suffit que, pour toute $\varphi \in \mathfrak{D}$, l'élément $\vec{f}$ ($\varphi$) de $\mathrm{E}'^*$ défini par (I, 3; 1) soit dans E.

Si en effet cette condition est réalisée, $\vec{f}$ définit une distribution à valeurs dans E muni de sa topologie affaiblie, donc dans E muni de sa topologie initiale (voir page 50).

PROPOSITION 20 (Gelfand-Dunford). — Si E est le dual faible G$_{s}$ d'un espace de Fréchet G (ou plus généralement d'un espace localement convexe G auquel soit applicable le théorème du graphe semi-fermé pour les applications linéaires dans les espaces de Banach) $^{(2)}$, toute fonction à valeurs dans E, scalairement localement sommable, définit une distribution à valeurs dans E.

(1) Soit en effet H cet ensemble. Pour tout $\vec{e}^{\prime} \in \mathbb{H}$, il existe un ensemble $\mathbf{N}_{\vec{e}^{\prime}}$, de mesure nulle de $\mathbb{R}^{n}$, en dehors duquel $\langle \vec{f}(x) - \vec{g}(x), \vec{e}^{\prime} \rangle = 0$. Si alors N est la réunion des $\mathbf{N}_{\vec{e}^{\prime}}$, pour $\vec{e}^{\prime} \in \mathbb{H}$, N est encore de mesure nulle; alors, pour $x \notin \mathbb{N}$, $\vec{f}(x) - \vec{g}(x)$ est une forme linéaire faiblement continue sur $\mathbf{E}^{\prime}$, nulle sur H, donc nulle sur $\mathbf{E}_{1}^{\prime}$ et $\vec{f}(x) = \vec{g}(x)$ pour $x \notin \mathbb{N}$.

(2) On dit qu'on peut appliquer à un espace localement convexe G le théorème du graphe semi-fermé pour les applications linéaires dans les espaces de Banach, si toute application linéaire de G dans un espace de Banach, dont le graphe est semi-fermé (fermé pour les suites convergentes), est continue. Il en est ainsi si G est un espace de Fréchet (BOURBAKI [1], corollaire 5 du théorème 1, page 37), et plus généralement s'il est ultrabornologique (limite inductive d'espaces de Banach), puisqu'il en est ainsi si G est un espace de Banach, et que, s'il en est ainsi pour des sous-espaces $G_{i}$ d'un espace G muni de la topologie limite inductive des $G_{i}$, il en est ainsi pour G.

Démonstration. — Soit $\varphi\in\mathfrak{D}$; nous devons montrer que $\vec{f}(\varphi)$ est dans E. Soit K le support de $\varphi$. Le dual de E est E' = G, et par hypothèse $<\vec{f},\vec{g}>$ est localement sommable pour tout $\vec{g}\in G$.

Alors $\vec{g} \to \langle \vec{f}, \vec{g} \rangle_{\mathbb{K}}$ (restriction de $\langle \vec{f}, \vec{g} \rangle$ à K) est une application linéaire de G dans l'espace de Banach L'(K) des classes de fonctions sommables sur K pour la mesure $dx$. Le graphe de cette application est semi-fermé (fermé pour les suites convergentes); car si $\vec{g}_{\nu}$ est une suite d'éléments de G convergeant vers 0 pour $\nu \to \infty$, et si $\langle \vec{f}, \vec{g}_{\nu} \rangle_{\mathbb{K}}$ converge vers un élément $h$ de L'(K), on peut extraire une suite partielle des $\vec{g}_{\nu}$ pour laquelle $\langle \vec{f}, \vec{g}_{\nu} \rangle_{\mathbb{K}}$ converge presque partout vers $h$; comme les fonctions $\langle \vec{f}, \vec{g}_{\nu} \rangle$ convergent vers 0 en tout point $x$ de R$^n$ puisque $\vec{f}(x) \in G'$, on a nécessairement $h = 0$ et le graphe est bien semi-fermé. Si alors G est un espace auquel on puisse appliquer le théorème du graphe semi-fermé pour les applications linéaires dans les espaces de Banach, l'application $\vec{g} \to \langle \vec{f}, \vec{g} \rangle_{\mathbb{K}}$ est continue. Alors la forme linéaire

$$
\overleftarrow {g} \rightarrow \int_ {\mathbf {R} ^ {n}} \langle \overrightarrow {f (x)}, \overleftarrow {g} \rangle \varphi (x) d x
$$

est continue sur G, donc $\vec{f}(\varphi) \in G' = E$,

c.q.f.d.

PROPOSITION 21. — Si $\vec{g}$ est une fonction définie presque partout sur $R^n$ à valeurs dans E, scalairement mesurable et telle que, pour tout compact K de $R^n$, l'enveloppe de $\vec{g}(K)$ soit faiblement compacte, et si h est une fonction numérique définie presque partout sur $R^n$ et localement sommable, alors $\vec{f} = \vec{g}h$ définit une distribution à valeurs dans E.

DÉMONSTRATION. — Tout d'abord $\vec{f}$ est scalairement localement sommable. Soit ensuite $\varphi\in\mathcal{D}$, de support K, et soit M=$\int_{K}|h(x)||\zeta(x)|dx$. Alors l'intégrale $\int_{R^{n}}\vec{g}(x)h(x)\varphi(x)dx$ est un élément de E'\* qui est contenu dans M fois l'enveloppe (dans E'\* muni de la topologie $\sigma(E'*,E'))$ de $\vec{g}(K)$. Comme l'enveloppe de $\vec{g}(K)$ dans E est faiblement compacte, donc est

une partie de E'\* disquée contenant $\vec{g}(\mathbf{K})$, elle est aussi son enveloppe dans E'\*, donc l'intégrale est dans E, c.q.f.d.

COROLLAIRE 1. — Une fonction f définie sur R^n à valeurs dans E, scalairement continue, définit une distribution à valeurs dans E.

En effet, en faisant $\vec{g} = \vec{f}$, $h = 1$, on voit que $\vec{g}(\mathbf{K})$ est faiblement compact dans E puisque $\vec{f}$ est faiblement continue, alors son enveloppe dans E est faiblement compacte puisque E est quasi-complet (1).

COROLLAIRE 2. — Si E est semi-réflexif, si g est une fonction définie presque partout sur R$^{n}$ à valeurs dans E, scalairement mesurable et localement bornée, et si h est une fonction numérique définie presque partout sur R$^{n}$ et localement sommable, f = gh définit une distribution à valeurs dans E.

En effet munissons E de sa topologie affaiblie $\sigma(E, E')$. Comme toute partie bornée de E est relativement compacte pour $\sigma(E, E')$ du fait que E est semi-réflexif$^{(2)}$, la proposition 21 donne la conclusion.

Dérivation des distributions.

La dérivée  $D^{p}\vec{T}$  d'une distribution  $\vec{T}$  à valeurs dans E (non nécessairement quasi-complet) est définie par :

(I, 3; 2)

$$
\left(\mathrm{D} ^ {p} \vec {\mathrm{T}}\right) (\varphi) = (- 1) ^ {| p |} \vec {\mathrm{T}} \left(\mathrm{D} ^ {p} \varphi\right),
$$

pour toute $\varphi\in\mathcal{D}$; ou

(I, 3; 3)

$$
\langle \mathrm{D} ^ {p} \vec {\mathrm{T}}, \vec {e ^ {\prime}} \rangle = \mathrm{D} ^ {p} \langle \vec {\mathrm{T}}, \vec {e ^ {\prime}} \rangle ,
$$

pour toute $\vec{e'} \in \mathrm{E}'$.

Autrement dit la dérivation n'est autre que l'opération $\mathbf{D}^p\otimes \mathbf{I}$ de $\mathcal{D}'\varepsilon \mathrm{E}$ dans $\mathcal{D}'\varepsilon \mathrm{E}$, associée, en vertu de la proposition 1 du § 1, à $\mathbf{D}^p$, opération linéaire continue de $\mathcal{D}'$ dans $\mathcal{D}'$, et I, opération linéaire continue identique de E dans E. Les formules précédentes sont celles de la remarque $1^{\circ}$ page 35 du § 1, appliquées à $\vec{\mathbf{X}} = \vec{\mathbf{T}}\in \mathfrak{L}(\mathfrak{D};\mathbb{E})$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) L'enveloppe d'une partie faiblement compacte est faiblement compacte, dans un espace quasi-complet. Voir GROTHENDIECK [6], remarque page 185.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) Théorème de Mackey, BOURBAKI [2], théorème 1, page 88.</span></small>

$D^{p}$ est une opération linéaire continue de $\mathcal{D}'(E)$ dans lui-même. C' est la seule opération linéaire continue qui vérifie

$$
\mathrm{D} ^ {p} (\mathrm{S} \otimes \vec {e}) = \mathrm{D} ^ {p} \mathrm{S} \otimes \vec {e}, \tag {I,3;4}
$$

pour toute $S \in \mathfrak{D}'$ et tout $e \in E$, puisque $\mathfrak{D}' \otimes E$ est dense dans $\mathfrak{D}'(E)$ ($\mathfrak{D}'$ ayant la propriété d'approximation, voir préliminaires corollaire de la proposition 3, et § 1 proposition 11).

## Multiplication.

Soient $\mathcal{H}$ et $\mathfrak{L}$ des espaces de distributions (non nécessairement quasi-complets) sur $R^n$, $\mathcal{H}$ normal. On dit que $S \in \mathcal{D}'$ est un multiplicateur de $\mathcal{H}$ dans $\mathfrak{L}$, s'il existe une opération linéaire continue [S] de $\mathcal{H}$ dans $\mathfrak{L}$, qui, sur $\mathcal{D} \subset \mathcal{H}$, coïncide avec la multiplication par S. On notera encore $T \to ST$ l'opération [S].

Alors on peut aussi définir $\mathbf{S}\tilde{\mathbf{T}}\in\mathfrak{L}(\mathbf{E})$ pour $\tilde{\mathbf{T}}\in\mathcal{H}(\mathbf{E})$ (E non nécessairement quasi-complet) par

$$
\langle \mathrm{S} \vec {\mathrm{T}}, \vec {e ^ {\prime}} \rangle = \mathrm{S} \langle \vec {\mathrm{T}}, \vec {e ^ {\prime}} \rangle , \quad \text { pour   tout } \quad \vec {e ^ {\prime}} \in \mathrm{E} ^ {\prime}. \tag {I,3;5}
$$

On aura aussi, si $\mathscr{L}$ est normal, donc aussi $\mathscr{L}_{c}^{\prime}$:

$$
(\mathrm{I}, 3; 6) \quad (\mathrm{S} \vec {\mathrm{T}}) (\varphi) = \vec {\mathrm{T}} (\mathrm{S} \varphi) \quad \text { pour   toute } \quad \varphi \in \mathfrak {L} ^ {\prime},
$$

S étant défini par transposition comme un multiplicateur de $\mathcal{L}_{c}^{\prime}$ dans $\mathcal{H}_{c}^{\prime}$.

L'opération linéaire continue $\vec{T} \to S\vec{T}$ de $\mathcal{H}(E) = \mathcal{H}\varepsilon E$ dans $\mathfrak{L}(E) = \mathfrak{L}\varepsilon E$ n'est autre que [S] $\otimes$ I, associée à [S] $\in$$\mathfrak{L}(\mathcal{H};\mathfrak{L})$ et $I \in \mathfrak{L}(E;E)$ d'après la proposition 1 du § 1, et les formules ci-dessus sont celles de la remarque $1^{\circ}$ page 35 du § 1. Si $\mathcal{H}$ vérifie la propriété d'approximation, c'est la seule opération linéaire continue qui vérifie

$$
\mathrm{S} (\mathrm{T} \otimes \vec {e}) = \mathrm{ST} \otimes \vec {e}, \text {   pour   toute   } \mathrm{T} \in \mathcal {H} \text {   et   tout   } \vec {e} \in \mathrm{E}. \tag {I,3;7}
$$

Soient $\mathcal{H}_1$ et $\mathcal{H}_2$ deux espaces de distributions normaux, S un multiplicateur de $\mathcal{H}_1$ dans $\mathcal{D}'$ et de $\mathcal{H}_2$ dans $\mathcal{D}'$, tel que les multiplications par S coïncident sur $\mathcal{H}_1 \cap \mathcal{H}_2$; ceci se produira sûrement si $\mathcal{D}$ est dense dans $\mathcal{H}_1 \cap \mathcal{H}_2$ muni de la borne supérieure des topologies induites par $\mathcal{H}_1$ et $\mathcal{H}_2$, puisque ces multiplications coïncident sur $\mathcal{D}$ (cette propriété de densité sera sûrement

elle-même vérifiée si $\mathcal{H}_{1}$ et $\mathcal{H}_{2}$ ont tous les deux la propriété d'approximation par troncature et par régularisation). Alors S est un multiplicateur de $\mathcal{H}_{1}$ (E) dans $\mathfrak{D}'(\mathrm{E})$ et de $\mathcal{H}_{2}$ (E) dans $\mathfrak{D}'(\mathrm{E})$, et sur $\mathcal{H}_{1}$ (E) $\cap$$\mathcal{H}_{2}$ (E) les deux multiplications par S coïncident en vertu de (1, 3; 5).

Soient maintenant $\mathcal{H}$, $\mathcal{K}$, $\mathcal{L}$, trois espaces de distributions (non nécessairement quasi-complets) sur $R^n$, $\mathcal{H}$ et $\mathcal{K}$ normaux. On appelle multiplication de $\mathcal{H} \times \mathcal{K}$ dans $\mathcal{L}$ une application bilinéaire séparément continue, dont la restriction à $\mathcal{D} \times \mathcal{D}$ soit la multiplication usuelle. Si une telle multiplication existe, elle est unique.

PROPOSITION 21 bis. — Soient H, K, L des espaces de distribution sur R$^{n}$, H et K normaux, E un espace localement convexe; ces espaces ne sont pas nécessairement quasi-complets. S'il existe une multiplication de H × K dans L, alors elle permet de définir une application bilinéaire de H(E) × K dans L(E), vérifiant (I. 3; 5) pour S ∈ K, T ∈ H(E), e' ∈ E'; cette application n'est pas nécessairement séparément continue. Si la multiplication de H × K dans L est hypocontinue par rapport aux parties compactes (resp. bornées) de H et à un ensemble S de parties bornées de K, l'application bilinéaire de H(E) × K dans L(E) est hypocontinue par rapport aux parties compactes (resp. bornées de H(E)) et à l'ensemble S de parties de K.

On remarque en effet que $S \in K$ est un multiplicateur de $\mathcal{H}$ dans $\mathfrak{L}$, au sens défini plus haut; il peut donc définir une multiplication continue de $\mathcal{H}(E)$ dans $\mathfrak{L}(E)$, vérifiant (I, 3; 5); on a donc bien défini une application bilinéaire de $\mathcal{H}(E) \times \mathfrak{K}$ dans $\mathfrak{L}(E)$.

De plus si la multiplication de $\mathcal{H} \times \mathfrak{K}$ dans $\mathfrak{L}$ est hypocontinue par rapport à un ensemble $\mathfrak{S}$ de parties de $\mathfrak{K}$, alors, pour $A \in \mathfrak{S}$, les $S \in A$ forment un ensemble équicontinu de multiplicateur de $\mathcal{H}$ dans $\mathfrak{L}$, donc de $\mathcal{H}(E)$ dans $\mathfrak{L}(E)$, d'après la proposition 1 du chapitre 1; ce qui prouve que, si $\vec{T}$ converge vers 0 dans $\mathcal{H}(E)$, et que S parcourt une partie de $\mathfrak{K}$ appartenant à $\mathfrak{S}$, $\vec{ST}$ tend vers 0 dans $\mathfrak{L}(E)$. Mais celà n'entraîne pas que l'application bilinéaire ainsi définie de $\mathcal{H}(E) \times \mathfrak{K}$ dans $\mathfrak{L}(E)$ soit séparément continue: si $\vec{T}$ est fixé dans $\mathcal{H}(E)$, et que S converge vers 0 dans $\mathfrak{K}$, il n'est pas certain que $\vec{ST}$ converge vers 0.

Mais supposons la multiplication de $\mathcal{H} \times \mathfrak{K}$ dans $\mathfrak{L}$ hypocontinue par rapport aux parties compactes de $\mathcal{H}$. Alors, si $\vec{\mathrm{T}}$ parcourt une partie compacte de $\mathcal{H}(\mathrm{E})$, et $\vec{e'}$ une partie équicontinue de $\mathrm{E}'$, $\langle \vec{\mathrm{T}}, \vec{e'} \rangle$ parcourt une partie relativement compacte de $\mathcal{H}$ (proposition 18 et remarque qui la suit); si alors S converge vers 0 dans $\mathfrak{K}$, $\mathrm{S} \langle \vec{\mathrm{T}}, \vec{e'} \rangle$ converge uniformément vers 0 dans $\mathfrak{L}$, donc $\vec{\mathrm{ST}}$ converge uniformément vers 0 dans $\mathfrak{L}(\mathrm{E})$. La continuité séparée de l'application bilinéaire de $\mathcal{H}(\mathrm{E}) \times \mathfrak{K}$ dans $\mathfrak{L}(\mathrm{E})$ permettra alors de l'appeler, elle aussi, une multiplication. Supposons enfin la multiplication de $\mathcal{H} \times \mathfrak{K}$ dans $\mathfrak{L}$ hypocontinue par rapport aux parties bornées de $\mathcal{H}$. Si alors $\vec{\mathrm{T}}$ parcourt une partie bornée de $\mathcal{H}(\mathrm{E}) \approx \mathfrak{L}_{\varepsilon}(\mathrm{E}_{\varepsilon}')$; $\mathcal{H}$), et $\vec{e'}$ une partie équicontinue de $\mathrm{E}'$, $\langle \vec{\mathrm{T}}, \vec{e'} \rangle$ parcourra une partie bornée de $\mathcal{H}$; si S converge vers 0 dans $\mathfrak{K}$, $\mathrm{S} \langle \vec{\mathrm{T}}, \vec{e'} \rangle$ convergera uniformément vers 0 dans $\mathfrak{L}$, donc $\vec{\mathrm{ST}}$ dans $\mathfrak{L}(\mathrm{E})$, c.q.f.d.

Notation fonctionnelle des distributions.

Il est commode d'avoir le plus souvent possible pour les distributions une écriture analogue à celle des fonctions. Nous adopterons les conventions suivantes :

$^{10}$ Une distribution T sur l'espace $R^{n}$ de la variable x pourra s'écrire $T(\hat{x})$ (comme une fonction pouvait s'écrire $f(\hat{x})$ (1)) et non plus seulement $T_{x}$.

$2^{0}$ Dans une formule intégrale, où la variable $x$ est muette, la même distribution pourra s'écrire $T(x)$, comme on écrit $f(x)$ avec une variable muette $x$ dans une intégrale.

Ainsi l'intégrale de T, égale à T(1), s'écrira, si $\mathbf{T} \in \mathfrak{D}_{\mathbf{L}}^{\prime}$:

$$
(\mathbf {I}, 3; 8)
$$

$$
\mathrm{T} (1) = \int_ {\mathbb {R} ^ {n}} \mathrm{T} (x) d x.
$$

Ce que nous écrivions $\mathbf{T}(\varphi)$ ou $\mathbf{T}.\varphi$ ou $\mathbf{T}_x.\varphi(x)$ pour $\varphi\in\mathcal{D}$ et $\mathbf{T}\in\mathcal{D}'$, s'écrira alors

$$
(\mathbf {I}, 3; 9)
$$

$$
\mathbf {T} (\varphi) = \int_ {\mathbf {R} ^ {n}} \mathbf {T} (x) \varphi (x) d x;
$$

c'est en effet l'intégrale, au sens de (1, 3; 8), de la distribution-produit multiplicatif T(ˆx)φ(ˆx). Si ℜ' est le dual d'un

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Cette notation a déjà été employée dans Schwartz [1], page 139.</span></small>

espace de distributions normal $\mathfrak{K}$, il arrivera fréquemment que (1, 3; 9) soit encore exacte pour $\varphi \in \mathfrak{K}$ et $T \in \mathfrak{K}'$ (nous verrons plus loin quelles conditions doivent être exigées pour cela; voir proposition 37).

Les mêmes notations seront utilisées pour des distributions à valeurs vectorielles : $\vec{T}(\hat{x})$ et $\vec{T}(x)$. Nous définirons l'intégrale de $\vec{T}$ par (I, 3; 8), au moins lorsque $\vec{T} \in \mathcal{E}'(E)$, alors (1, 3; 9) est valable, au moins pour $\varphi \in \mathcal{D}$ et $\vec{T} \in \mathcal{D}'(E)$.

La seule chose qui distinguera la distribution d'une fonction partout définie est la possibilité pour cette dernière d'écrire $f(a)$, pour $a$ donné dans $\mathbb{R}^{n}$.

Convolution. — Soient $\mathcal{H}$ et $\mathfrak{L}$ des espaces de distributions sur $\mathbb{R}^n$, $\mathcal{H}$ normal. On dit que S est un opérateur de convolution de $\mathcal{H}$ dans $\mathfrak{L}$, s'il existe une opération linéaire continue $\{\mathrm{S}\}$, notée $\mathrm{T} \to \mathrm{S} * \mathrm{T}$, de $\mathcal{H}$ dans $\mathfrak{L}$, qui, pour $\mathrm{T} = \varphi \in \mathfrak{D}$, donne $\mathrm{S} * \mathrm{T} = \mathrm{S} * \varphi$, produit de convolution. Alors on peut aussi définir $\mathrm{S} * \vec{\mathrm{T}} \in \mathfrak{L}(\mathrm{E})$, pour $\vec{\mathrm{T}} \in \mathcal{H}(\mathrm{E})$, par

(I, 3; 10) $\langle \mathrm{S} * \vec{\mathrm{T}}, \vec{e'} \rangle = \mathrm{S} * \langle \vec{\mathrm{T}}, \vec{e'} \rangle$ pour tout $\vec{e'} \in \mathbf{E}'$.

On a aussi, si $\mathscr{L}$ donc $\mathscr{L}_{c}^{\prime}$ est normal:

$$
(I, 3; 1 1) \quad (S * \vec {T}) (\varphi) = \vec {T} (\check {S} * \varphi), \text {   pour   toute   } \varphi \in \mathscr {L} ^ {\prime},
$$

Š étant par transposition un opérateur de convolution de $\mathcal{L}_{\epsilon}^{\prime}$ dans $\mathcal{H}_{\epsilon}^{\prime}$. L'opérateur $\vec{T} \to S * \vec{T}$ de $\mathcal{H}(E) = \mathcal{H} \varepsilon E$ dans $\mathcal{L}(E) = \mathcal{L} \varepsilon E$ n'est autre que $\{S\} \otimes I$, associé en vertu de la proposition 1 du § 1 à $\{S\} \in \mathcal{L}(\mathcal{H}; \mathcal{L})$ et $I \in \mathcal{L}(E; E)$.

La convolution avec $\delta$ est l'opérateur identique; la dérivation $D^{p}$ est une convolution avec $D^{p}\delta$. La convolution avec $\alpha \in \mathcal{D}$ donne une régularisation d'une distribution à valeurs vectorielles par une fonction numérique indéfiniment différentiable. On voit immédiatement que, si $\alpha_{j} \in \mathcal{D}$ converge vers $\delta$ dans $\mathcal{E}_{c}^{\prime 0}$, alors les régularisées $\alpha_{j} * \vec{T}$ convergent vers $\vec{T}$ dans $\mathcal{D}'(E)$; toute distribution est limite de ses régularisées. Ajoutons enfin que la régularisée $\vec{T} * \alpha$ de $\vec{T} \in \mathcal{D}'(E)$ par $\alpha \in \mathcal{D}$ se calcule ponctuellement par

$$
(\vec {\mathbf {T}} * \alpha) (x) = \vec {\mathbf {T}} _ {\xi} (\alpha (x - \xi)) = \int_ {\mathbb {R} ^ {n}} \alpha (x - \xi) \vec {\mathbf {T}} (\xi) d \xi .\tag{I, 3; 12}
$$

(Cette formule s'obtient en faisant le produit scalaire avec $\vec{e'} \in \mathbf{E}'$).

On peut naturellement faire des remarques analogues à celles que nous avons faites à propos de la multiplication, et donner une proposition analogue à 21 bis.

REMARQUE. — Si H possède la propriété d'approximation par troncature et régularisation, alors H(E) la possède aussi. Soit en effet ( $\alpha_{v}$ ) une suite de fonctions de D, convergeant vers 1 dans E pour  $v \to \infty$ , en restant bornée dans B. Alors les opérateurs [ $\alpha_{v}$ ] :  $\psi \to \alpha_{v}\psi$ , convergent vers I dans  $\mathcal{L}_{c}(\mathcal{H}; \mathcal{H})$ , donc les opérateurs [ $\alpha_{v}$ ]  $\otimes$  I :  $\vec{\varphi} \to \alpha_{v}\vec{\varphi}$  convergent vers I  $\otimes$  I = I dans  $\mathcal{L}_{c}(\mathcal{H}(E); \mathcal{H}(E))$  (corollaire 3 de la proposition 2 du chapitre 1). On raisonne de même pour les régularisations  $\{\rho_{v}\} : \varphi \to \varphi * \rho_{v}$ . Dans ce cas, H(E) n D(E) sera strictement dense dans H(E); si on sait que H est normal, on saura aussi que D(E) est sous-espace strictement dense de H(E), avec une topologie plus fine que la topologie induite.

Transformation de Fourier.

L'image de Fourier $\mathcal{F}\vec{T}$ d'une distribution $\vec{T} \in \mathcal{S}'(E)$ (E non nécessairement quasi-complet) se définit par:

(I, 3; 13)

$$
\left(\mathcal {F} \vec {\mathrm{T}}\right) (\varphi) = \vec {\mathrm{T}} \left(\mathcal {F} \varphi\right), \quad \text { pour   toute } \quad \varphi \in \mathcal {S};
$$

ou

$$
(\mathrm{I}, 3; 1 4) \quad \langle \mathcal {F} \vec {\mathrm{T}}, \vec {e ^ {\prime}} \rangle = \mathcal {F} \langle \mathrm{T}, \vec {e ^ {\prime}} \rangle \quad \text { pour   tout } \quad \vec {e ^ {\prime}} \in \mathrm{E} ^ {\prime}.
$$

L'opération linéaire continue $\vec{T} \to \mathcal{F}\vec{T}$ de $\mathscr{S}'(E) = \mathscr{S}'\varepsilon E$ dans $\mathscr{S}'(E) = \mathscr{S}'\varepsilon E$, quoique notée $\mathscr{F}$, est en réalité l'opération $\mathscr{F} \otimes I$, associée en vertu de la proposition 1 du § 1 à $\mathscr{F} \in \mathscr{L}(\mathscr{S}', \mathscr{S}')$ et $I \in \mathscr{L}(E; E)$. $\mathscr{F}$ applique continuement $\mathcal{O}_{M}(E)$ sur $\mathcal{O}_{C}'(E)$ et inversement. On a la formule de réciprocité de Fourier: $\overline{\mathcal{F}}\overline{\mathcal{F}}\overline{T} = \overline{\mathcal{F}}\overline{\mathcal{F}}\overline{T}$ pour toute $\vec{T} \in \mathscr{S}'(E)$. Enfin la multiplication, opération bilinéaire de $\mathcal{O}_{M}(E) \times \mathscr{S}'$ (resp. $\mathcal{O}_{M} \times \mathscr{S}'(E)$) dans $\mathscr{S}'(E)$, hypocontinue par rapport aux parties bornées, est transformée par $\mathscr{F}$ en la convolution, opération bilinéaire de $\mathcal{O}_{C}'(E) \times \mathscr{S}'$ (resp. $\mathcal{O}_{C}' \times \mathscr{S}'(E)$) dans $\mathscr{S}'(E)$, hypocontinue par rapport aux parties bornées.

Transformation de Laplace $^{1}$ .

Soit $\Gamma$ un ensemble convexe du dual $\Xi^n$ de $R^n$, et soit $\vec{T}$ une distribution de $(\mathcal{S}'(\Gamma))(E)$. Pour tout $\xi \in \Gamma$ fixé, on peut calculer l'image de Fourier, par rapport à $x$, de $\exp (-\xi \hat{x}) T(\hat{x}) \in \mathcal{S}'_x(E)$:

$$
\begin{array}{r l} \mathrm{(I,3;15)} & \mathrm{F} (\xi , \hat {\eta}) = (\mathcal {F} _ {(x)} [ \exp (- \xi \hat {x}) \vec {\mathrm{T}} (\hat {x}) ]) (\hat {\eta}) \\ & \qquad = \int_ {\mathrm{R} ^ {n}} \exp (- (\xi + i \hat {\eta}) x) \bar {\mathrm{T}} (x) d x, \end{array}
$$

élément de $\mathcal{S}_{\eta}^{\prime}(\mathrm{E})$. Nous écrivons la dernière intégrale bien qu'elle n'ait, actuellement, pas de sens; une justification sera donnée page 133 au § 5. Nous omettons le facteur $2\pi$ comme il est habituel dans la transformation de Laplace. $\mathrm{F}(\xi, \hat{\eta})$ est une distribution tempérée en $\eta$, à valeurs dans E, dépendant de $\xi \in \Gamma$. On sait que, lorsque $\xi$ décrit l'enveloppe convexe d'un nombre fini de points de $\Gamma$, la fonction $\xi \to \exp(-\xi \cdot \hat{x}) \langle \vec{T}(\hat{x}), \vec{e'} \rangle$ à valeurs dans $\mathcal{S}_{x}^{\prime}$ est indéfiniment dérivable, et sa dérivée $\mathrm{D}^{p}$ est la fonction $\xi \to (-\hat{x})^{p} \exp(-\xi \hat{x}) \langle \vec{T}(\hat{x}), \vec{e'} \rangle$; cela prouve que, si l'on identifie $\mathcal{S}_{x}^{\prime}(\mathrm{E})$ à $\mathfrak{L}(\mathrm{E}_{c}^{\prime}; \mathcal{S}_{x}^{\prime})$ et qu'on le munit de la topologie de la convergence simple sur $\mathrm{E}'$, $\xi \to \exp(-\xi \hat{x}) \vec{T}(\hat{x})$ est une fonction indéfiniment dérivable de $\xi$ à valeurs dans $\mathcal{S}_{x}^{\prime}(\mathrm{E})$, de dérivée $\mathrm{D}^{p}$ égale à $\xi \to (-\hat{x})^{p} \exp(-\xi \hat{x}) \mathrm{T}(\hat{x})$.

Mais alors, d'après un lemme général sur la dérivation (²), elle sera aussi indéfiniment dérivable pour la topologie ordinaire de $\mathfrak{S}_{x}^{\prime}(\mathrm{E})$ (qui est celle de la convergence uniforme sur les parties équicontinues de $\mathrm{E}^{\prime}$), si chaque dérivée $\xi \to (-\hat{x})^{p}\exp (-\xi \hat{x})\vec{\mathrm{T}} (\hat{x})$ est continue en $\xi$ pour la topologie ordinaire de $\mathfrak{S}_{x}^{\prime}(\mathrm{E})$ (toujours lorsque $\xi$ parcourt l'enveloppe convexe d'un nombre fini de points de $\Gamma$). Nous avons à montrer pour cela que, si $\xi \to \xi_{0}$, le produit $\langle (\exp (-\xi \hat{x}) - \exp (-\xi_{0}\hat{x}))(-\hat{x})^{p}\vec{\mathrm{T}} (\hat{x}),\vec{e}^{\prime}\rangle$ converge vers 0 dans $\mathfrak{S}_{x}^{\prime}$, uniformément lorsque $\vec{e}^{\prime}$ parcourt une partie équicontinue de $\mathrm{E}^{\prime}$; or il converge vers 0 dans $\mathfrak{D}_{x}^{\prime}$ (parce que $\langle (-\hat{x})^{p}\vec{\mathrm{T}} (\hat{x}),\vec{e}^{\prime}\rangle$ reste borné dans $\mathfrak{D}_{x}^{\prime}$ et que

$$
(\exp (- \xi \hat {x}) - \exp (- \xi_ {0} \hat {x}))
$$

converge vers 0 dans $\mathcal{E}_{x}$ et reste borné dans $\mathcal{F}_{x}^{\prime}$ (parce que

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Pour toutes les notations et propriétés relatives à la transformation de Laplace, voir SCHWARTZ [3].</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) Schwartz [1], lemme 1, page 145.</span></small>

$\langle \vec{T}, \vec{e'} \rangle$ reste borné dans $\mathcal{S}'(\Gamma)$; mais, sur toute partie bornée (donc relativement compacte) de $\mathcal{S}'$, la topologie $\mathcal{S}'$ est identique à la topologie induite par $\mathcal{D}'$, donc il converge vers 0 dans $\mathcal{S}'_x$. Ainsi nous avons bien montré que $\xi \to \exp(-\xi \hat{x})\vec{T}(\hat{x})$ est une fonction indéfiniment dérivable de $\xi$ à valeurs dans $\mathcal{S}'_x(E)$, tant que $\xi$ parcourt l'enveloppe convexe d'un nombre fini de points de $\Gamma$.

Il en résulte que $\xi \to \vec{\mathbf{F}}(\xi, \hat{\eta})$ est une application indéfiniment différentiable à valeurs dans $\mathcal{S}_{\eta}^{\prime}(\mathrm{E})$, lorsque $\xi$ parcourt l'enveloppe convexe d'un nombre fini de points de $\Gamma$.

Nous supposerons désormais $\Gamma$ ouvert. On sait qu'alors, pour tout $\xi$, et tout $\vec{e'} \in E'$, $\langle \vec{\mathrm{F}}(\xi, \hat{\eta}), \vec{e'} \rangle$ est dans $(\mathcal{O}_{\mathbf{M}})_{\eta}$, donc $\vec{\mathrm{F}}(\xi, \hat{\eta})$ est scalairement dans $(\mathcal{O}_{\mathbf{M}})_{\eta}$, et comme $\mathcal{O}_{\mathbf{M}}$ a la propriété $\varepsilon$ (proposition 16 du § 2), $\vec{\mathrm{F}}(\xi, \hat{\eta})$ est dans $(\mathcal{O}_{\mathbf{M}})_{\eta}(\mathrm{E})$ pour tout $\xi \in \Gamma$. Posors $p = \xi + i\eta$, pour $\xi \in \Gamma$ et $\eta$ quelconque, on peut écrire $\vec{\mathrm{F}}(\xi, \eta) = \vec{\mathrm{F}}(p)$. On a, pour tout $p$ tel que $\xi \in \Gamma$ et tout $\vec{e'} \in E'$:

$$
\langle \vec {\mathrm{F}} (p), \vec {e ^ {\prime}} \rangle = \int_ {\mathbf {x} ^ {n}} \exp (- p x) \langle \vec {\mathrm{T}} (x), \vec {e ^ {\prime}} \rangle d x.\tag{I, 3; 16}
$$

Comme, pour $p$ fixé, $\exp(-p\hat{x})\mathrm{T}(\hat{x})$ est scalairement dans $(\mathcal{O}_{\mathrm{C}}^{\prime})_{x}$, donc dans $(\mathcal{O}_{\mathrm{C}}^{\prime})_{x}(\mathrm{E})$ puisque $\mathcal{O}_{\mathrm{C}}^{\prime}$ a la propriété $\varepsilon$ (proposition 16), nous verrons plus tard (proposition 36 page 129 du § 5) qu'on peut écrire aussi vectoriellement :

$$
\vec {\mathrm{F}} (p) = \int_ {\mathbf {x} ^ {n}} \exp (- p x) \vec {\mathrm{T}} (x) d x.\tag{I, 3; 17}
$$

La fonction $\vec{\mathbf{F}}: p \to \vec{\mathbf{F}}(p)$ est scalairement holomorphe; comme E est quasi-complet, cela suffit à prouver qu'elle est holomorphe (1).

Cette fonction holomorphe $\vec{\mathbf{F}}$ n'est pas quelconque: pour tout $\vec{e'} \in \mathbf{E}'$, la fonction $\langle \vec{\mathbf{F}}(p), \vec{e'} \rangle$ est majorée par un polynome en $|p|$ (dont le degré peut dépendre de $\vec{e'}$) lorsque $\xi$ parcourt un compact de $\Gamma$ et que $\eta$ varie dans $\Xi^n$. On peut donc dire

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$p_{1}, p_{2}, \ldots, p_{n}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Car, étant scalairement holomorphe, elle est scalairement indéfiniment dérivable par rapport aux variables complexes $p_1, p_2, \ldots, p_n$, donc elle est indéfiniment dérivable par rapport à ces variables (Schwartz [1], lemme 2, page 146) donc holomorphe.</span></small>

que $\vec{\mathbf{F}}$ est scalairement à croissance lente en $|p|$ lorsque $\xi$ parcourt un compact de $\Gamma$. Réciproquement, soit $\vec{\mathbf{F}}$ une fonction holomorphe de $p \in \Gamma + i\Xi^n$, scalairement à croissance lente en $|p|$ lorsque $\xi$ parcourt un compact de $\Gamma$. Pour tout $\vec{e'} \in \mathbf{E}'$, $\langle \vec{\mathbf{F}}(p), \vec{e'} \rangle$ est image de Laplace d'une distribution $\langle \vec{\mathbf{T}}, \vec{e'} \rangle$ de $\mathcal{S}'(\Gamma)$. Cela définit $\vec{\mathbf{T}}$ comme distribution sur $\mathbf{R}^n$ à valeurs dans le dual algébrique $\mathbf{E}'^*$ de $\mathbf{E}'$, muni de la topologie $\sigma(\mathbf{E}'^*$, $\mathbf{E}'$ (page 51 du § 2). Montrons que $\vec{\mathbf{T}}$ est une distribution à valeurs dans E lui-même, et appartient à $(\mathcal{S}'(\Gamma))(E)$. Choissons $\xi$ dans $\Gamma$; on sait que $\langle \exp(-\xi\hat{x})\vec{\mathbf{T}}(\hat{x}), \vec{e'} \rangle$ est l'image réciproque de Fourier de $\langle \vec{\mathbf{F}}(\xi + i\hat{\eta}), \vec{e'} \rangle$. Mais $\vec{\mathbf{F}}(\xi + i\hat{\eta})$ est une fonction continue de $\eta$ à valeurs dans E, donc une distribution en $\eta$ à valeurs dans E; elle est scalairement dans $\mathcal{S}_{\eta}'$ d'après les hypothèses; donc elle est dans $\mathcal{S}_{\eta}'(E)$ puisque $\mathcal{S}'$ a la propriété ($\varepsilon$) (proposition 16 du § 2); alors $\exp(-\xi\hat{x})\mathbf{T}(\hat{x})$ est une distribution appartenant à $\mathcal{S}_{x}'(E)$; cela prouve (voir page 58 du § 2) que $\vec{\mathbf{T}}$ est bien dans $(\mathcal{S}'(\Gamma))(E)$. Enfin $\langle \vec{\mathbf{F}}, \vec{e'} \rangle$ est l'image de Laplace de $\langle \vec{\mathbf{T}}, \vec{e'} \rangle$, donc $\vec{\mathbf{F}}$ est l'image de Laplace de $\vec{\mathbf{T}}$. Ainsi nous avons démontré :

PROPOSITION 22. — Toute distribution $\vec{\Gamma} \in (\mathfrak{S}'(\Gamma))(E)$ admet une transformée de Laplace, qui, lorsque $\Gamma$ est ouvert, est une fonction holomorphe $\vec{\mathrm{F}}(\hat{p})$ de $p \in \Gamma + i\Xi^n$ à valeurs dans E, scalairement à croissance lente en $|p|$ lorsque $\xi$ décrit un compact de $\Gamma$; réciproquement, toute fonction holomorphe ayant cette propriété est transformée de Laplace d'une distribution et une seule de $(\mathfrak{S}'(\Gamma))(E)$.

Dans le cas d'une variable ($n = 1$, espace R de la variable réelle $t$) et de distributions scalairement à support limité à gauche, comme c'est le cas le plus fréquent dans les applications, nous aurons besoin d'une transformée de Laplace en un sens un peu plus général.

Nous appellerons $\mathcal{E}\mathcal{F}$ l'espace des fonctions $\varphi$ qui sont « dans $\mathcal{E}$ à gauche et dans $\mathcal{F}$ à droite », c'est-à-dire telles que, pour toute fonction $\alpha$ indéfiniment dérivable, à support limité à gauche, et appartenant à $\mathcal{B}$, $\alpha\varphi$ soit dans $\mathcal{F}$. Nous le munirons de la topologie la moins fine pour laquelle toutes les applications $\varphi \to \alpha\varphi$ ($\alpha$ du type précédent) soient continues de $\mathcal{E}\mathcal{F}$

dans $\mathcal{S}$. Nous appellerons maintenant $\mathfrak{X}(-a)$, $a$ réel, l'espace des fonctions $\varphi$ telles que $\exp (at)\varphi$ soit dans $\mathfrak{E}\mathcal{S}$, muni de la topologie pour laquelle $\varphi \to \exp (at)\varphi$ est un isomorphisme de $\mathfrak{X}(-a)$ sur $\mathfrak{E}\mathcal{S}$. Pour $a \leqslant a'$, $\mathfrak{X}(-a')$ est un sous-espace de $\mathfrak{X}(-a)$, avec une topologie plus fine que la topologie induite. On appelle $\mathcal{X}$ l'espace des fonctions indéfiniment dérivables, qui tendent vers 0 plus vite que $\exp (-at)$ lorsque $t \to +\infty$, ainsi que chacune de leurs dérivées, pour tout $a$ réel; $\mathcal{X}$ est l'intersection de tous les $\mathfrak{X}(-a)$; nous le munirons de la topologie borne supérieure des topologies induites par les $\mathfrak{X}(-a)$. $\mathcal{X}$ et les $\mathfrak{X}(-a)$ sont des espaces de Fréchet-Montel, strictement normaux, vérifiant la propriété d'approximation par troncature et par régularisation, et la propriété d'approximation stricte. $\mathfrak{E}\mathcal{S}$ n'est autre que $\mathfrak{X}(0)$. Le dual ($\mathfrak{E}\mathcal{S}$)' de $\mathfrak{E}\mathcal{S}$ est l'espace des distributions à support limité à gauche, qui sont tempérées à droite. Appelons $\mathcal{X}'$ le dual fort de $\mathfrak{X}(\mathfrak{X}' = \mathfrak{X}_c')$. C'est la réunion des $\mathfrak{X}'(a)$, où $\mathfrak{X}'(a)$ est le dual de $\mathfrak{X}(-a)$. En effet soit $T \in \mathfrak{X}'$; il existe un voisinage de 0 de $\mathcal{X}$ sur lequel T est bornée, donc T est continue sur $\mathcal{X}$ muni de la topologie induite par un $\mathfrak{X}(-a)$ convenable, donc $T \in \mathfrak{X}'(a)$. $\mathfrak{X}'(a)$ est l'espace des distributions à support limité à gauche dont le produit par $\exp (-at)$ est tempéré [soit en effet $T \in \mathfrak{X}'(a)$; si $\varphi \in \mathfrak{D}$ converge vers 0 dans $\mathfrak{E}\mathcal{S}$, $\exp (-at)\varphi$ converge vers 0 dans $\mathfrak{X}(-a)$, donc $(\exp (-at)\mathrm{T})$. ($\varphi$) = T(exp (-at)$\varphi$) converge vers 0, donc exp (-at)T est à support limité à gauche et tempérée; réciproquement si cette condition est vérifiée, et si $\psi \in \mathfrak{D}$ converge vers 0 dans $\mathfrak{X}(-a)$, exp ($at$)$\psi$ converge vers 0 dans $\mathfrak{E}\mathcal{S}$, alors $T(\psi) = (\exp (-at)\mathrm{T})$. (exp ($at$)$\psi$) converge vers 0, et T est dans $\mathfrak{X}'(a)$].

L'expression de toute  $T \in X'$  comme  $\exp{(at)}$  S,  $S \in S'$ , montre que  $X'$  est le domaine naturel de la transformation de Laplace. L'image de Laplace AT de  $T \in X'$  est définie par

(1, 3; 18)

$$
\mathfrak {L} \mathrm{T} (p) = \mathrm{T} _ {t} (\exp (- p t)) = \int_ {\mathrm{R}} \exp (- p t) \mathrm{T} (t) d t, \quad p = \xi + i \eta .
$$

Les deuxième et troisième membres n'ont pas immédiatement un sens; en effet, si grand que soit $\xi = \mathcal{R}p$, $\exp(-pt)$ n'appartient jamais à $\mathcal{R}$. Mais toute $T \in \mathcal{X}'$ appartient à un

$\mathcal{X}'(a)$ ; elle est alors une forme linéaire continue sur l'espace  $\mathcal{X}(-a)$ ; or  $\exp(-p\hat{t})$  appartient à  $\mathcal{X}(-a)$  pour  $\xi > a$ .

De plus $p \to \exp(-pt)$ est une fonction holomorphe de $p$ à valeurs dans $\mathfrak{X}(-a)$ lorsque $\xi > a$. On en déduit que $\mathfrak{A}\mathrm{T}$ est une fonction holomorphe de $p$ pour $\xi > a$. On peut encore définir $\mathfrak{A}\mathrm{T}$ dès que le $3^{\mathrm{e}}$ membre de (I, 3; 18) a un sens; or l'expression de $\mathrm{T} \in \mathfrak{A}'(a)$ comme produit de $\exp(a\hat{t})$ par une distribution tempérée à support limité à gauche montre précisément que $\exp(-p\hat{t})\mathrm{T}(\hat{t})$ est sommable en $t$ pour $\xi > a$; cela définit $\mathfrak{A}\mathrm{T}(p)$ pour $\xi > a$, et comme de plus $p \to \exp(-p\hat{t})\mathrm{T}(\hat{t})$ est une fonction holomorphe de $p$ à valeurs dans $\mathfrak{D}_{\mathrm{L}}'$ pour $\xi > a$, $\mathfrak{A}\mathrm{T}$ est aussi une fonction holomorphe de $p$. Naturellement nous rejoignons ici la théorie générale de la transformation de Laplace. Si $\Gamma_a$ est le convexe $\xi \geqslant a$ de la droite réelle duale de R, $\mathfrak{A}'(a)$ est le sous-espace de $\mathcal{S}'(\Gamma_a)$ formé des distributions à support limité à gauche.

Soit maintenant $\vec{T} \in \mathcal{D}'(E)$ une distribution sur $R$ à valeurs dans $E$. Comme $\mathcal{X}$ est métrisable et normal, $\mathcal{X}'$ a la propriété ($\varepsilon$) et $\mathcal{X}'(E)$ est $\mathcal{L}_c(\mathcal{X}; E)$; ceci vaut aussi pour $\mathcal{X}'(a)$. Si donc $\vec{T}$ est scalairement dans $\mathcal{X}'$, elle est dans $\mathcal{X}'(E)$; mais on ne peut pas pour cela définir son image de Laplace. Car si $\vec{e}' \in E'$, le domaine de définition de $\mathcal{X}\left(\langle \vec{T}, \vec{e}' \rangle\right)$ est un demi-plan $\xi > a(\vec{e}')$, où $a(\vec{e}')$ peut dépendre de $\vec{e}'$, de sorte que $\mathcal{X}T$ peut n'être défini pour aucune valeur de $p$. Nous dirons que $\vec{T} \in \mathcal{X}'(E)$ a une image de Laplace, si elle appartient à un $(\mathcal{X}'(a))(E)$ convenable (nous appellerons alors $a^0$ la borne inférieure des $a$ tels que $\vec{T} \in (\mathcal{X}'(a))(E)$; $a^0$ est éventuellement égal à —$\infty$), auquel cas son image de Laplace $\mathcal{X}\vec{T}$ est une fonction holomorphe de $p$ à valeurs dans $E$ pour $\xi > a$. Une telle circonstance aura sûrement lieu s'il existe un voisinage de 0 dans $\mathcal{X}$ dont l'image par $\vec{T}$ soit bornée dans $E$; car alors $\vec{T}$ est continue sur $\mathcal{X}$ muni de la topologie induite par un $\mathcal{X}(-a)$ convenable et comme $\mathcal{X}(-a)$ est strictement dense dans $\mathcal{X}$ et $E$ quasi-complet, $\vec{T}$ se prolonge en une application linéaire continue de $\mathcal{X}(-a)$ dans $E$, et $\vec{T} \in (\mathcal{X}'(a))(E)$. Comme $\mathcal{X}$ est un espace

de Fréchet, cette circonstance se produira toujours si E est du type (DF) (').

Si $\vec{T}$ a une image de Laplace $\vec{F}$, $\vec{F}(\hat{p})$ est une fonction holomorphe de $p$ à valeurs dans E pour $\xi > a^0$.

Le fait que, pour tout $\vec{e'} \in E'$, $\langle \vec{T}, \vec{e'} \rangle$ ait son support limité à gauche, entraîne alors que $|\langle \vec{F}(p), \vec{e'} \rangle|$ soit majoré, pour $\xi \geqslant a' > a^0$, par le produit d'une exponentielle $\exp(b\xi)$ par un polynome en $|p|(^2)$; $b$ et le degré du polynome peuvent dépendre (pour $a'$ fixé) de $\vec{e'} \in E'$; on pourra dire que, pour $\xi \geqslant a' > a^0$, $\vec{F}(p)$ est scalairement majorée par le produit d'une exponentielle en $\xi$ par un polynome en $|p|$. Réciproquement si $\vec{F}(\hat{p})$ est une fonction holomorphe pour $\xi > a$, à valeurs dans E, ayant la propriété précédente, elle est, d'après la proposition 22, transformée de Laplace d'une distribution $T \in (\mathcal{G}'(\hat{l}_a'))(E)$, où $\hat{l}_a$ est le convexe $\xi > a$; mais pour tout $\vec{e'} \in E'$, $\langle \vec{T}, \vec{e'} \rangle$ a son support limité à gauche, donc $\langle \vec{T}, \vec{e'} \rangle \in \mathcal{X}'(a)$, et par suite $\vec{T} \in (\mathcal{X}'(a))(E)$ et a fortiori $\vec{T} \in \mathcal{X}'(E)$.

Mais si nous avons introduit $\mathfrak{X}'$, c'est pour pouvoir étudier certains cas où E n'est pas du type (DF), et où par suite $\mathfrak{X}'(E)$ n'est pas la réunion des $(\mathfrak{X}'(a))(E)$.

Nous supposerons que E est la limite projective filtrante stricte d'une famille d'applications linéaires  $(\pi_{i})_{i\in I}$  dans des espaces  $E_{i}$  (E et tous les  $E_{i}$  quasi-complets). Pour  $j\geqslant i$, il existe une application linéaire continue  $\pi_{ij}$  de  $E_{j}$  dans  $E_{i}$, telle que  $\pi_{i}=\pi_{ij}\circ\pi_{j}$.

En outre, si $(\vec{e}_i)_{i \in I}$ est une famille d'éléments $\vec{e}_i \in E_i$ telle que, pour $j \geqslant i$, on ait $\vec{e}_i = \pi_{ij}(\vec{e}_j)$, il existe un $\vec{e}$ (et un seul) de E tel que, pour tout $i$, on ait $\vec{e}_i = \pi_i(\vec{e})$. Enfin E a la topologie la moins fine pour laquelle toutes les applications $\pi_i$ ($E \to E_i$) soient continues. Soit alors $\vec{T}$ une distribution à valeurs dans E; elle est dans $\mathfrak{P}'(E)$ si et seulement si, pour tout $i$, son image $\pi_i(\vec{T})$ est dans $\mathfrak{P}'(E_i)$ [si $T \in \mathfrak{P}'(E)$, $\pi_i(\vec{T}) = (I \otimes \pi_i)(\vec{T})$ est dans $\mathfrak{P}'(E_i)$ d'après la proposition 1 du § 1. Si réciproquement $\pi_i(\vec{T})$ est dans $\mathfrak{P}'(E_i)$ pour tout $i$, comme tout élément $\vec{e}'$ de $E'$ est

(i) Voir note (2), page 62.

(2) Schwartz [3], page 206.

de la forme $^{t}\pi_{i}(\vec{e}_{i}^{\prime})$ pour un i convenable $(^{i})$, on a $\langle\vec{T},\vec{e}^{\prime}\rangle=\langle\pi_{i}(\vec{T}),\vec{e}_{i}^{\prime}\rangle$, donc T est scalairement dans $\mathcal{X}'$, et par suite dans $\mathcal{X}'(E)$. Cette propriété est donc valable non seulement pour $\mathcal{H}=\mathcal{X}'$, mais pour tout espace $\mathcal{H}$ ayant la propriété $(\varepsilon)$]. Par ailleurs le système des $\vec{T}_{i}=\pi_{i}(\vec{T})$ vérifie, pour $j\geqslant i:\vec{T}_{i}=\pi_{ij}(\vec{T}_{j})$. Réciproquement si $(\vec{T}_{i})_{i\in I}$ est une famille de distributions, $\vec{T}_{i}$ à valeurs dans $E_{i}$, telle que, pour $j\geqslant i$, on ait $\vec{T}_{i}=\pi_{ij}(\vec{T}_{j})$, il existe une distribution et une seule $\vec{T}$ à valeurs dans E telle que $\vec{T}_{i}=\pi_{i}(\vec{T})$ pour tout i. En effet, pour toute $\varphi\in\mathcal{D}$, nous appellerons $\vec{T}(\varphi)$ l'unique élément $\vec{e}$ de E tel que pour tout i on ait $\pi_{i}(\vec{e})=\vec{T}_{i}(\varphi)$; l'application linéaire $\varphi\to\vec{T}(\varphi)$ est continue puisque chaque application $\pi_{i}\circ T:\varphi\to\vec{T}_{i}(\varphi)$ est continue, et que la topologie de E est limite projective de celles des $E_{i}$. Finalement la donnée d'une distribution $\vec{T}\in\mathcal{X}'(E)$ est équivalente à celle d'une famille de distributions $\vec{T}_{i}\in\mathcal{X}'(E_{i})$, telle que, pour $j\geqslant i$, on ait $\vec{T}_{i}=\pi_{ij}(\vec{T}_{j})$. Alors, d'après ce que nous avons vu plus haut, $\vec{T}_{i}$ a une transformée de Laplace si nous supposons que chaque $E_{i}$ est du type (DF): cette transformée est une fonction $\vec{F}_{i}(\hat{p})$ holomorphe pour $\xi>a_{i}^{0}$, à valeurs dans $E_{i}$, scalairement majorée par le produit d'une exponentielle en $\xi$ par un polynome en |p| pour $\xi\geqslant a^{\prime}>a_{i}^{0}$; cette famille de fonctions holomorphes est cohérente, en ce sens que, pour $j\geqslant i$, on a $a_{j}^{0}\geqslant a_{i}^{0}$, et $\vec{F}_{i}(p)=\pi_{ij}(\vec{F}_{j}(p))$ pour $\xi>a_{j}^{0}$, car $\vec{F}_{i}(p)=\vec{T}_{i}(\exp(-pt))=(\pi_{ij}\circ\vec{T}_{j})(\exp(-pt))= \pi_{ij}\bigl(\vec{T}_{j}(\exp(-pt))\bigr)=\pi_{ij}\bigl(\vec{F}_{j}(p)\bigr)$,

mais elle ne définit pas forcément une fonction holomorphe à valeurs dans E, car sup $(a_i^0)$ est peut-être $+\infty$.

Réciproquement, si $\overline{\mathbf{F}}_{i}$ est un système de fonctions holomorphes, $\overline{\mathbf{F}}_{i}(\hat{p})$ holomorphe pour $\xi > a_{i}^{0}$ à valeurs dans $\mathbf{E}_{i}$, si toute fonction $\overrightarrow{\mathbf{F}}_{i}$ est scalairement majorée pour $\xi \geqslant a' > a^{0}$ par le produit d'une exponentielle en $\xi$ par un polynome en $|p|$, et si ce système est cohérent $(a_{j}^{0} \geqslant a_{i}^{0}$ pour $j \geqslant i$, et $\overrightarrow{\mathbf{F}}_{i}(p) = \pi_{ij}(\overrightarrow{\mathbf{F}}_{j}(p))$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) BOURBAKI [2], corollaire de la proposition 10, page 76. La somme finie peut ici être remplacée par un seul terme, parce que l'ensemble d'indices est filtrant.</span></small>

pour $\xi > a_{j}^{0}$, il existe un système de distributions $\vec{T}_{i} \in \mathfrak{X}'(E_{i})$, tel que $\vec{F}_{i}$ soit l'image de Laplace de $\vec{T}_{i}$, et comme ce système est cohérent, il existe une distribution $\vec{T}$ et une seule, appartenant à $\mathfrak{X}'(E)$, telle que $\vec{F}_{i}$ soit l'image de Laplace de $\pi_{i}(\vec{T})$. C'est le système cohérent des $\vec{F}_{i}$ qui peut être appelé la transformée de Laplace de $\vec{T} \in \mathfrak{X}'(E)$.

Naturellement il n'était pas indispensable de supposer les  $E_{i}$  du type (DF); il suffit de supposer que, pour une raison quelconque,  $\vec{T}_{i} = \pi_{i}(\vec{T})$  appartienne à un  $(\mathcal{X}'(a_{i}))(\mathrm{E}_{i})$ ,  $a_{i}$  fini.

Dans les applications pratiques, E est lui-même un espace de distributions, et c'est alors fréquemment une limite projective d'espaces de Banach. Dans la transformation de Laplace partielle par rapport au temps, nous utiliserons comme espace E l'espace des distributions $\mathcal{D}_{y}^{\prime}$ sur $Y^{m}$. Il est la limite projective des $E_{K} = (\mathcal{D}_{K})'$, K compact de $Y^{m}$, l'application $\pi_{K}$ de $\mathcal{D}'$ dans $(\mathcal{D}_{K})'$ étant la transposée de l'injection de $\mathcal{D}_{K}$ dans $\mathcal{D}$. Comme $\mathcal{D}_{K}$ est un espace de Fréchet, $(\mathcal{D}_{K})'$ est du type (DF). En fait il est plus pratique d'utiliser les $E_{\Omega} = \mathcal{D}_{\Omega}'$, espaces de distributions sur les ouverts bornés $\Omega$ de $Y^{m}$. $\mathcal{D}'$ est aussi la limite projective des applications $\pi_{\Omega}$ de $\mathcal{D}'$ dans $\mathcal{D}_{\Omega}'$, transposées des injections de $\mathcal{D}_{\Omega}$ dans $\mathcal{D}$. Tout élément de E est alors une distribution S définie par le système cohérent des distributions locales $S_{\Omega}$, $S_{\Omega}$ étant la distribution induite par S sur l'ouvert $\Omega$ de $Y^{m}$.

Comme $\mathfrak{D}_{\Omega}$ n'est pas un espace de Fréchet, $\mathfrak{D}_{\Omega}^{\prime}$ n'est pas du type (DF), mais nous verrons plus loin que c'est sans importance. Soit T une distribution sur $R \times Y^{m}$, R étant la droite réelle de la variable $t$. Nous l'écrirons $\tilde{T}(\hat{t})$, distribution en $t$ à valeurs dans $\mathfrak{D}_{y}^{\prime}$, ce qui est possible en vertu de la partie triviale du théorème des noyaux (1).

Nous dirons alors qu'elle admet une transformée de Laplace partielle par rapport à $t$, si $\vec{T}(\hat{t})$ appartient à $\mathcal{P}_{t}^{\prime}(\mathcal{D}_{y}^{\prime})$. Si $\Omega$ est un ouvert borné de $Y^{m}$, et si K est un compact de $Y^{m}$ contenant $\Omega$, on peut écrire $\vec{T}_{\Omega} = \pi_{\Omega}(\vec{T}) = \pi_{\Omega,\kappa}(\pi_{\kappa}(\vec{T}))$, $\pi_{\Omega,\kappa}$ étant l'application $(\mathcal{D}_{\kappa})^{\prime} \to \mathcal{D}_{\Omega}^{\prime}$, transposée de l'injection $\mathcal{D}_{\Omega} \to \mathcal{D}_{\kappa}$. Comme alors $\vec{T}_{\kappa} = \pi_{\kappa}(\vec{T})$ appartient à un $(\mathcal{P}^{\prime}(a_{\kappa}))(\mathrm{E}_{\kappa})$ conve-

(1) Schwartz [1], page 138.

nable, on peut être sûr, bien que $\mathcal{D}_{\Omega}^{\prime}$ ne soit pas un espace du type (DF), que $\tilde{T}_{\Omega}$ appartient à $(\mathcal{X}'(a_{\mathbf{k}}))(E_{\Omega})$.

Nous considérerons donc comme transformée de Laplace de $\vec{T}$ le système cohérent des $\vec{\mathrm{F}}_{\Omega}(\hat{p})$; $\vec{\mathrm{F}}_{\Omega}(\check{p})$ est une fonction holomorphe de $p$ à valeurs dans $(\mathfrak{D}_{\Omega}^{\prime})_y$, pour $\xi > a_{\Omega}^{0}$; elle est scalairement majorée par le produit d'une exponentielle en $\xi$ par un polynome en $|p|$ pour $\xi \geqslant a' > a_{\Omega}^{0}$; le système est cohérent en ce sens que, si $\omega$ et $\Omega$ sont deux ouverts bornés de $\mathbf{Y}^{m}$ et si $\omega \subset \Omega$, on a $a_{\Omega}^{0} \geqslant a_{\omega}^{0}$, et, pour $\xi > a_{\Omega}^{0}$, $\vec{\mathrm{F}}_{\omega}(p)$ est la distribution (en $y$) induite par $\vec{\mathrm{F}}_{\Omega}(p)$ dans l'ouvert $\omega$ de $\mathbf{Y}^{m}$. Réciproquement, si les $\vec{\mathrm{F}}_{\Omega}$ forment un système cohérent de fonctions holomorphes pour les divers $\Omega$ bornés de $\mathbf{Y}^{m}$, ayant scalairement la propriété de majoration précédente, elles constituent la transformée de Laplace d'une distribution $\vec{\mathrm{T}}(\hat{t}) \in \mathcal{X}_{t}^{\prime}(\mathcal{D}_{y}^{\prime})$. Naturellement $\vec{T}$ est donnée comme distribution en $t$ à valeurs dans $\mathcal{D}_{y}^{\prime}$, et on ne peut lui associer cette fois une distribution $\mathrm{T}(\hat{t}, \hat{y}) \in \mathcal{D}_{t,y}^{\prime}$ qu'en utilisant la partie non triviale du théorème des noyaux ($^1$).

Il n'est pas inutile dans ce cas particulier de préciser à nouveau concrètement la marche des opérations. On reconnaîtra que la distribution $\vec{\mathrm{T}}(\hat{t}) = \mathrm{T}(\hat{t},\hat{y})$ appartient à $\mathfrak{X}_{i}^{\prime}(\mathfrak{D}_{y}^{\prime})$, si elle appartient scalairement à $\mathfrak{X}_{i}^{\prime}$, c'est-à-dire si, pour toute $\varphi\in\mathfrak{D}_{y}$, la distribution $\mathrm{T}\cdot\varphi=\int_{y^{m}}\mathrm{T}(\hat{t},y)\varphi(y)dy$ (notations de la théorie des noyaux, formule (I, 4; 4) du § 4) appartient à $\mathfrak{X}_{i}^{\prime}$, c'est-à-dire si la forme linéaire

$$
\Psi (\hat {t}) \rightarrow \iint \mathbf {T} (t, y) \Psi (t) \varphi (y) d t d y
$$

est continue sur $\mathfrak{D}_{t}$ muni de la topologie induite par $\mathfrak{X}_{t}$. Soit $\Omega$ un ouvert borné de $\mathbf{Y}^{m}$. La transformée de Laplace associée à $\Omega$ est une fonction $\vec{\mathrm{F}}_{\Omega}(\hat{p})$, holomorphe en $p$ pour $\xi > a_{\Omega}^{\circ}$ convenable, à valeurs dans $(\mathfrak{D}_{\Omega}')_{y}$. Elle est définie par l'intégrale

(I, 3; 19)

$$
\mathrm{F} (p, \hat {y}) = \int_ {\mathrm{R}} \mathrm{T} (t, \hat {y}) \exp (- p t) d t, \quad \xi > a _ {\Omega} ^ {0},
$$

qui a au moins un sens scalairement : pour toute $\varphi\in(\mathfrak{D}_{\Omega})_{y}$, on a

(I, 3; 20)

$$
\int_ {\mathbf {Y} ^ {m}} \mathrm{F} (p, y) \varphi (y) d y = \int_ {\mathbb {R}} \exp (- p t) d t \int_ {\mathbf {Y} ^ {m}} \mathrm{T} (t, y) \varphi (y) d y,
$$

(1) Schwartz [1], page 143.

pour $\xi > a_{\Omega}^{0}$. La deuxième intégrale du $2^{\mathrm{e}}$ membre donne une distribution de $\mathcal{X}_{t}^{\prime}$, qui appartient à $\mathcal{X}_{t}^{\prime}(a_{\Omega}^{0})$, donc son produit par $\exp(-pt)$ est dans $(\mathcal{D}_{\mathrm{L}^{\prime}}^{\prime})_{t}$ pour $\xi > a_{\Omega}^{0}$.

Tout ce que nous venons de voir trouverait en réalité sa place normale au § 4, mais nous n'avons pas voulu partager en plusieurs morceaux la transformation de Laplace, dont le mécanisme est déjà lourd (1).

Distributions d'ordre fini et dérivées de fonctions.

Une distribution $\tilde{\mathbf{T}}\in\mathcal{D}^{\prime}(\mathbf{E})$ (E non nécessairement quasi-complet) est d'ordre fini si elle appartient à un $\mathcal{D}^{\prime m}(\mathbf{E})$, $m$ fini convenable. Si E est quasi-complet, il suffit pour cela que $\tilde{\mathbf{T}}$ soit continue sur $\mathcal{D}$ muni de la topologie induite par $\mathcal{D}^{m}$, puisque $\mathcal{D}^{m}$ est strictement dense dans $\mathcal{D}$; il suffit également qu'elle soit scalairement d'ordre $m$, puisque $\mathcal{D}^{m}$ a la propriété ($\varepsilon$).

Une distribution $\widetilde{\mathbf{T}}\in\mathfrak{D}^{\prime}(\mathbf{E})$ est localement d'ordre fini si, sur tout ouvert $\Omega$ borné de $\mathbf{R}^{n}$, elle est une distribution d'ordre fini. Lorsque E est le corps des scalaires, on sait que toute distribution est localement d'ordre fini; pour E quelconque, il n'en est rien. Ainsi l'application identique de $\mathfrak{D}$ dans $\mathfrak{D}$ est une distribution à valeurs dans $\mathbf{E}=\mathfrak{D}$; elle n'est évidemment pas localement d'ordre fini, car, quels que soient l'ouvert borné $\Omega$ de $\mathbf{R}^{n}$ et l'entier $m$, elle n'est pas continue de $\mathfrak{D}_{\Omega}$ muni de la topologie induite par $\mathfrak{D}_{\Omega}^{m}$ dans $\mathfrak{D}$ muni de sa topologie usuelle.

Une application linéaire $u$ d'un espace vectoriel localement convexe L dans un espace vectoriel localement convexe M est dite bornée s'il existe un voisinage de O dans L dont l'image par $u$ soit une partie bornée de M. Une application bornée est continue; si L ou M est normé, une application continue de L dans M est bornée. Un ensemble H de $\mathfrak{L}(\mathrm{L};\mathrm{M})$ est dit équiborné s'il existe un voisinage $\mathcal{U}$ de 0 dans L tel que $\bigcup_{u\in \mathrm{H}}u(\mathrm{U})$ soit une

partie bornée de M. Un ensemble équiborné est équicontinu; si L est normé, un ensemble borné de $\mathcal{L}_{b}(L;M)$ est équiborné ($^{2}$).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(L;M)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{L}(\mathbf{L};\mathbf{M})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Cette transformation de Laplace partielle a été introduite par Garnir, dans [1]. (2) Il importe de ne pas confondre les parties bornées de $\mathcal{L}$ (L;M) pour une topologie quelconque de cet espace, et les parties équibornées, qui ne dépendent pas d'une topologie sur $\mathcal{L}$ (L; M). Dans le cas d'une seule application $u$ de L dans M, il n'y a pas d'ambiguïté à dire qu'elle est une application bornée, car un élément unique de $\mathcal{L}$ (L; M) est toujours une partie bornée et il serait sans intérêt de le constater ou d'en parler.</span></small>

Plus généralement, soit $\mathfrak{G}$ un ensemble de parties bornées de M. Une application linéaire $u$ de L dans M est dite $\mathfrak{G}$-bornée, s'il existe un voisinage de O de L dont l'image par $u$ appartienne à $\mathfrak{G}$. Une application compacte de L dans M est $\mathfrak{G}$-bornée, si $\mathfrak{G}$ est l'ensemble des parties compactes de M. Un ensemble H de $\mathfrak{L}(L; M)$ est dit $\mathfrak{G}$-équiborné, s'il existe un voisinage $\mathfrak{U}$ de O dans L tel que $\bigcup_{\mathfrak{U} \in \mathbb{W}} u(\mathfrak{U}) \in \mathfrak{G}$.

On dira donc qu'une distribution $\vec{T} \in \mathcal{D}'(E)$ est bornée, ou $\mathfrak{C}$-bornée, si l'application qu'elle définit de $\mathfrak{D}$ dans E a cette propriété; elle sera dite localement bornée, ou localement $\mathfrak{C}$-bornée, si, pour tout ouvert $\Omega$ borné de $R^n$, l'application qu'elle définit de $\mathcal{D}_{\Omega}$ dans E est bornée, ou $\mathfrak{C}$-bornée. On parlera de même d'un ensemble équiborné, $\mathfrak{C}$-équiborné, localement équiborné, localement $\mathfrak{C}$-équiborné, de $\mathcal{D}'(E)$.

PROPOSITION 23. — Soit E un espace localement convexe séparé (non nécessairement quasi-complet), $\mathfrak{G}$ un ensemble saturé de parties bornées de E, et supposons E $\mathfrak{G}$-complétant (toute partie disquée de E appartenant à $\mathfrak{G}$ est complétante). Pour qu'un ensemble H de $\mathfrak{D}'(\mathrm{E})$ soit localement $\mathfrak{G}$-équiborné, il faut et il suffit que, pour tout ouvert $\Omega$ borné de $\mathbb{R}^n$, il existe un entier m fini tel que H soit un ensemble $\mathfrak{G}$-équiborné d'applications linéaires de $\mathfrak{D}_{\Omega}^{m}$ dans E.

Dans ce cas, sur H, les topologies induites par $\mathfrak{D}_{\Omega}^{\prime}(\mathrm{E})$ et $(\mathfrak{D}_{\epsilon}^{\prime m})_{\Omega}(\mathrm{E})$ coincident.

La condition est trivialement suffisante, sans même supposer que E soit $\mathfrak{C}$-complétant. Montrons qu'elle est nécessaire.

Soit donc H un ensemble localement $\mathfrak{C}$-équiborné de $\mathfrak{D}'(E)$. Soit $\Omega$ un ouvert borné de $R^n$ et soit $\Omega'$ un autre ouvert borné contenant $\overline{\Omega}$. Il existe, par hypothèse, un voisinage $\mathcal{U}'$ de 0 dans $\mathfrak{D}_{\Omega'}$ tel que $\bigcup_{\vec{\tau} \in H} \vec{T}(\mathcal{U}')$ ait une enveloppe $B \in \mathfrak{C}$. Alors $E_B$ est

un espace de Banach.

Mais il existe un entier $m$ assez grand pour que $\mathfrak{U} = \mathfrak{U}' \cap \mathfrak{D}_{\Omega}$ soit un voisinage de O dans $\mathfrak{D}_{\Omega}$ pour la topologie induite par $\mathfrak{D}_{\Omega}^{m}$.

Alors chaque $\vec{T} \in H$ est continue de $\mathfrak{D}_{\Omega}$, muni de la topologie induite par $\mathfrak{D}_{\Omega}^{m}$, dans $E_{B}$, et, comme $\mathfrak{D}_{\Omega}$ est strictement dense dans $\mathfrak{D}_{\Omega}^{m}$, $\vec{T}$ se prolonge en une application linéaire

continue, que nous appellerons encore $\vec{T}$, de $\mathfrak{D}_{\Omega}^{m}$ dans $E_{B}$. On a alors, si $\overline{\mathcal{U}}$ est l'adhérence de $\mathcal{U}$ dans $\mathfrak{D}_{\Omega}^{m}: \bigcup_{\vec{T} \in H} \vec{T}(\overline{\mathcal{U}}) \subset B$, B étant

fermée dans  $E_{B}$ . Comme U est un voisinage de O dans  $\mathcal{D}_{\Omega}^{m}(^{1})$ , on voit que H est bien un ensemble C-équiborné d'applications linéaires de  $D_{\Omega}^{m}$  dans E.

Comme H est alors une partie équicontinue de $\mathfrak{L}(\mathcal{D}_{\Omega}^{m};\mathrm{E})$, la topologie induite sur H par $(\mathcal{D}_{c}^{\prime m})_{\Omega}(\mathrm{E}) = \mathfrak{L}_{c}(\mathcal{D}_{\Omega}^{m};\mathrm{E})$ coïncide bien avec la topologie induite par $\mathcal{D}_{\Omega}^{\prime}(\mathrm{E}) = \mathfrak{L}_{c}(\mathcal{D}_{\Omega};\mathrm{E})$, $\mathcal{D}_{\Omega}$ étant dense dans $\mathcal{D}_{\Omega}^{m}(^{2})$.

COROLLAIRE 1. — Si E est quasi-complet, pour que $\vec{T} \in \mathfrak{D}'(E)$ soit localement d'ordre fini, il faut et il suffit qu'elle soit une distribution localement bornée.

1° Soit en effet $\vec{T}$ localement d'ordre fini. Soit $\Omega$ un ouvert borné de $R^n$, et soit $\Omega'$ un autre ouvert borné contenant $\overline{\Omega}$. Dans $\Omega'$, $\vec{T}$ est d'ordre fini $\leqslant m$; elle définit donc une application linéaire continue de $\mathfrak{D}_{\Omega}^{m}$, à fortiori de $\mathfrak{D}_{\overline{\Omega}}^{m}$, dans E. Mais $\mathfrak{D}_{\overline{\Omega}}^{m}$ est un espace normé; donc $\vec{T}$ est une application bornée de $\mathfrak{D}_{\overline{\Omega}}^{m}$, et à fortiori de $\mathfrak{D}_{\Omega}$, dans E: $\vec{T}$ est une distribution localement bornée. Pour ceci, il n'est pas nécessaire de supposer E quasi-complet.

$^{20}$  Soit maintenant  $\vec{T}$  une distribution localement bornée. D'après la proposition, puisque E est quasi-complet, pour tout ouvert borné  $\Omega$, il existe un entier m tel que  $\vec{T}$  applique continuement  $D_{\Omega}^{m}$  dans E, donc  $\vec{T}$  est d'ordre  $\leqslant m$  dans  $\Omega: \vec{T}$  est localement d'ordre fini.

COROLLAIRE 2. — Si E est du type (DF) et quasi-complet, toute distribution à valeurs dans E est localement d'ordre fini; si H est une partie bornée de $\mathfrak{D}'(E)$, alors, pour tout ouvert $\Omega$ borné de $R^n$, il existe un entier m tel que H soit un ensemble équiborné d'applications de $\mathfrak{D}_\Omega^m$ dans E; alors sur H les topologies induites par $\mathfrak{D}_\Omega'(E)$ et $(\mathfrak{D}_c'^m)_\Omega(E)$ coïncident.

Soit en effet $\widetilde{T} \in \mathfrak{D}'(E)$. Soit $\Omega$ un ouvert borné de $R^n$. $\widetilde{T}$ est une application linéaire continue de $\mathfrak{D}_{\overline{\Omega}}$ dans $E$; mais $\mathfrak{D}_{\overline{\Omega}}$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) BOURBAKI [5], proposition 2, page 26.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) BOURBAKI [2], proposition 5, page 23.</span></small>

est un espace de Fréchet, alors, si E est du type (DF) $^{(1)}$, T est une application bornée de  $D_{\overline{\Omega}}$, donc de  $D_{\Omega}$, dans E; T est donc une distribution localement bornée, et par suite localement d'ordre fini d'après le corollaire 1, puisque E est quasi-complet.

Si H est une partie bornée de $\mathcal{D}'(E)$, elle est une partie bornée de $\mathfrak{I}(\mathcal{D}_{\overline{\Omega}}; E)$; comme $\mathcal{D}_{\overline{\Omega}}$ est un espace de Fréchet et E du type (DF) $^{(1)}$, H est un ensemble équiborné d'applications de $\mathcal{D}_{\overline{\Omega}}$, donc de $\mathcal{D}_{\Omega}$, dans E; H est donc une partie localement équibornée de $\mathcal{D}'(E)$, et il suffit d'appliquer la proposition, valable puisque E est quasi-complet.

PROPOSITION 24. — Soit Ω un ouvert de R$^{n}$. Toute distribution $\vec{T} \in (\mathfrak{D}_{c}^{'m})_{\Omega}(E)$ (E non nécessairement quasi-complet) est somme de dérivées d'ordre ≤ m + n + 1 de fonctions continues à valeurs dans E :

$$
\mathrm{(I,3;21)} \quad \vec {\mathrm{T}} = \sum_ {| p | \leqslant m + n + 1} \mathrm{D} ^ {p} \vec {f} _ {p}, \quad \vec {f} _ {p} \in \mathcal {E} _ {\Omega} ^ {0} (\mathrm{E}).
$$

Il existe des applications linéaires continues $u_p$ de $(\mathfrak{D}_c'^m)_\Omega$ dans $\mathcal{E}_\Omega^0$, telles que la décomposition (I, 3; 21) soit possible avec $\vec{f}_p = (u_p \otimes I)$. T.

Soit $\mathfrak{C}$ un ensemble saturé de parties bornées de E. Si H est un ensemble de $(\mathfrak{D}_c'^m)_\Omega(E)$ tel que, pour toute partie bornée B de $\mathfrak{D}_{\Omega}^{m}$, $\bigcup_{\tilde{\tau}\in H}\tilde{T}(B)$ appartienne à $\mathfrak{C}$, alors on peut, pour toutes les

$\widetilde{\mathbf{T}} \in \mathbf{H}$, choisir la décomposition (I, 3; 21) de manière que, pour tout compact K de $\Omega$, $\bigcup_{\widetilde{\mathbf{T}} \in \mathbf{H}} \widetilde{f}_{p}(\mathbf{K}) \in \mathfrak{G}$.

DÉMONSTRATION. — Nous démontrerons d'abord un lemme :

LEMME. — Dans  $R^{n}$ , δ est somme de dérivées d'ordre ≤ m + n + 1 de fonctions m fois continuement différentiables à supports compacts.

Soit en effet E une solution élémentaire de l'opérateur de Laplace itéré $\Delta^{k}$. Nous supposerons d'abord $m + n + 1$ pair, et prendrons $k = \frac{m + n + 1}{2}$.

(1) Voir note (2), page 62.

On sait que E peut être choisie proportionnelle à $r^{2k-n}$ ou $r^{2k-n} \log r$ selon que $2k - n = m + 1$ est impair ou pair (1); en tout cas elle est $m$ fois continuement différentiable dans $\mathbf{R}^n$. Alors, si $\gamma \in \mathcal{D}$ est égale à 1 au voisinage de l'origine, $\bar{\omega} = \gamma E$ est une paramétrix (2) de $\Delta^k$:

$$
\Delta^ {k} \varpi = \delta - L, \quad L \in \mathfrak {D},
$$

ce qui s'écrit précisément

$$
(I, 3; 2 3) \quad \delta = \Delta^ {k} \varpi + L = \sum_ {| p | \leqslant m + n + 1} D ^ {p} L _ {p}, \quad L _ {p} \in \mathfrak {D} ^ {m}.
$$

Si maintenant  $m + n + 1$  est impair, nous prendrons  $k = \frac{m + n + 2}{2}$ . Alors E est  $m + 1$  fois continuement différentiable, et (I, 3; 22) s'écrit

$$
\delta = \Delta^ {k} \varpi + L = \sum_ {| p | \leqslant m + | n + 2} D ^ {q} M _ {q}, \quad M _ {q} \in \mathcal {D} ^ {m + 1}, \tag {I,3;24}
$$

ce qui entraîne de nouveau (I, 3; 23), en prenant pour $\mathbf{L}_{p}$ certaines dérivées d'ordre $\leqslant 1$ des $\mathbf{M}_{q}$.

Démontrons maintenant la proposition 24. Soit d'abord $\Omega = R^{n}$. On a immédiatement:

$$
\vec {\mathrm{T}} = \delta_ {*} \vec {\mathrm{T}} = \sum_ {| p | \leqslant m + n + 1} \mathrm{D} ^ {p} \mathrm{L} _ {p} * \vec {\mathrm{T}} = \sum_ {| p | \leqslant m + n + 1} \mathrm{D} ^ {p} (\mathrm{L} _ {p} * \vec {\mathrm{T}}).\tag{I, 3; 25}
$$

La convolution avec $\mathbf{L}_p \in \mathfrak{D}^m$ est une opération linéaire continue $u_p$ de $\mathfrak{D}_c'^m$ dans $\mathcal{E}^0$ (on a $(\mathbf{T} * \mathbf{L}_p)(x) = \int_{\mathbb{R}^n} \mathbf{T}(\xi) \mathbf{L}_p(x - \xi) d\xi$; lorsque $x$ décrit un compact de $\mathbf{R}^n$, $\mathbf{L}_p(x - \hat{\xi})$ décrit un compact de $\mathfrak{L}_\xi^m$; si alors $\mathbf{T}(\hat{\xi})$ converge vers 0 dans $(\mathfrak{D}_c'^m)_\xi$, $(\mathbf{T} * \mathbf{L}_p)(x)$ converge vers 0 uniformément lorsque $x$ décrit un compact de $\mathbf{R}^n$, donc $\mathbf{T} * \mathbf{L}_p$ converge vers 0 dans $\mathcal{E}^0$), donc $(u_p \otimes \mathbf{I}) : \vec{\mathbf{T}} \to \mathbf{L}_p * \vec{\mathbf{T}}$, est une opération linéaire continue de $\mathfrak{D}_c'^m(\mathbf{E})$ dans $\mathcal{E}^0(\mathbf{E})$, et (I, 3; 25) donne (I, 3; 21) avec $\vec{f}_p = \mathbf{L}_p * \vec{\mathbf{T}}$.

Si $\vec{T} \in \mathcal{E}_{c}^{\prime m}(E)$ (resp. $\mathcal{E}^{\prime m}(E)$), les $\vec{f}_{p}$ sont dans $\mathfrak{D}^{0}(E)$ (resp. $\overline{\mathfrak{D}}^{0}(E)$), et comme les supports de $\varpi$ donc des $L_{p}$ peuvent être choisis dans un voisinage arbitraire de l'origine, les supports des $\vec{f}_{p}$ peuvent être choisis dans le voisinage d'ordre $\leqslant \varepsilon$ du

(1) Schwartz [4], formules (II, 3; 16 et 18).

(2) SCHWARTZ [5], formule (VI, 6; 22).

support de $\vec{T}$, $\varepsilon > 0$ arbitraire. De plus, $u_p \otimes I: \vec{T} \to L_p * \vec{T}$, est continue de $\mathcal{E}_c'^m(E)$ dans $\mathcal{D}^o(E)$.

Soit maintenant $\Omega$ un ouvert quelconque de $R^n$, et $\vec{T} \in (\mathcal{D}_c'^m)_\Omega(E)$. Soit $(\Omega_v)_{v=1,2,\ldots}$ un recouvrement localement fini de $\Omega$ par des ouverts $\Omega_v$ relativement compacts dans $\Omega$, et soit $(\Omega_v')_{v=1,2,\ldots}$ un recouvrement subordonné $(\overline{\Omega}_v' \subset \Omega_v)$. Soit $(\alpha_v)_{v=1,2,\ldots}$ une partition de l'unité relative au recouvrement $(\Omega_v')_{v=1,2,\ldots}$. On a $\vec{T} = \sum_{v} \alpha_v \vec{T}$, $\alpha_v T \in \overline{\mathcal{E}}'^m(E)$. Il existe alors une décomposition $\alpha_v \vec{T} = \sum_{|p| \sim m+n+1} D^p f_p, v$, où $\vec{f}_{p,v} \in \overline{\mathcal{D}}^0(E)$ a son support dans $\Omega_v$. On a alors

$$
\vec {\mathrm{T}} = \sum_ {| p | \leqslant m + n + 1} \mathrm{D} ^ {p} \vec {f} _ {p}, \quad \text { avec } \quad \vec {f} _ {p} = \sum_ {\nu = 1, 2, \dots} \vec {f} _ {p, \nu},
$$

série convergente parce que, sur tout ouvert relativement compact de $\Omega$, tous ses termes sont nuls sauf un nombre fini; ainsi la décomposition (I, 3; 21) subsiste lorsqu'on remplace $R^n$ par $\Omega$; et on forme facilement les opérateurs $u_p$, mais ce ne sont évidemment plus des convolutions.

Si $\vec{T}$ parcourt une partie bornée H de $(\mathcal{D}_{c}^{'m})_{\Omega}(\mathrm{E})$, chaque $\vec{f}_{p}$ parcourt une partie bornée de $\mathcal{E}_{\Omega}^{0}(\mathrm{E})$, puisque $u_{p}\otimes\mathrm{I}$ est continue de $(\mathcal{D}_{c}^{'m})_{\Omega}(\mathrm{E})$ dans $\mathcal{E}_{\Omega}^{0}(\mathrm{E})$; alors $\bigcup_{\vec{T}\in\mathrm{H}}\vec{f}_{p}(\mathrm{K})$, pour tout compact K

de $\Omega$, est une partie bornée de E. Plus généralement, soit $\mathfrak{G}$ un ensemble saturé de parties bornées de E, et soit H un sous-ensemble de $(\mathcal{D}_{c}^{'m})_{\Omega}(\mathrm{E})$ tel que, pour toute partie bornée B de $\mathcal{D}_{\Omega}^{m}$, $\bigcup_{\vec{\mathbf{T}}\in\mathbf{H}}\vec{\mathbf{T}}(\mathbf{B})\in\mathfrak{G}$. Cela exprime simplement qu'il est un ensemble

localement $\mathfrak{G}$-équiborné d'applications de $\mathcal{D}_{\Omega}^{m}$ dans E. Alors, pour la décomposition (I, 3; 21) trouvée dans la démonstration, $\bigcup_{\vec{\tau}\in H}\vec{f}_{p}(K)$, pour tout compact K de $\Omega$, appartient à $\mathfrak{G}$. Montrons-

le pour $\Omega = \mathbb{R}^n$. On a $\vec{f}_p(x) = (\mathrm{T} * \mathrm{L}_p)(x) = \int_{\mathbb{R}^n} \vec{\mathrm{T}}(\xi) \mathrm{L}_p(x - \xi) \, \mathrm{d}\xi$; pour $x \in \mathbb{K}$, $\mathrm{L}_p(x - \xi)$ parcourt une partie compacte donc bornée B de $\mathfrak{D}_\xi^m$, d'où le résultat. Pour $\Omega$ quelconque, on procédera encore par partition de l'unité, nous laissons au lecteur le soin de le faire; la proposition 24 est ainsi complètement démontrée.

Remarque. — On ne peut, ni dans le lemme ni dans la proposition, remplacer  $m + n + 1$  par  $m + n - 1$ .

Si en effet on le pouvait, $\delta$ serait somme de dérivées d'ordre $\leqslant n-1$ de fonctions continues (à cause du lemme, pour $m=0$; ou à cause de la proposition pour E = corps des scalaires, T = $\delta$, $m=0$); alors toute distribution S dont les dérivées d'ordre $\leqslant n-1$ sont des mesures, serait une fonction continue ($\text{car } S=\delta*S=\sum_{|p|\leqslant n-1}D^{p}L_{p}*S=\sum_{|p|\leqslant n-1}L_{p}*D^{p}S\in\mathcal{E}^{0}$); or $\frac{1}{r^{\lambda}}$, $0<\lambda<1$, n'est pas une fonction continue, et ses dérivées d'ordre $\leqslant n-1$ sont des fonctions.

Pour $n=1$ (cas de la droite R), on ne peut même pas remplacer $m+n+1$ par $m+n$. Si en effet on le pouvait, toute distribution S dont les dérivées premières sont des mesures serait une fonction continue; or S=Y, fonction d'Heaviside, de dérivée Y' = δ, donne un contre-exemple.

Pour $n \geqslant 2$, nous ignorons si on peut, dans le lemme ou la proposition, remplacer $m + n + 1$ par $m + n$; nous ignorons si $\delta$ est somme de dérivées d'ordre $\leqslant n$ de fonctions continues; nous savons qu'une conséquence qu'on pourrait tirer d'une réponse positive à ces questions, à savoir que toute distribution, dont les dérivées d'ordre $\leqslant n$ sont des mesures, serait une fonction continue, est exacte pour $n$ impair $\geqslant 3$; ce résultat est trivialement faux pour $n = 1$, nous ignorons ce qui en est pour $n$ pair, et de toute façon cela ne semble pas donner de renseignements sur les questions précédentes.

COROLLAIRE 1. — Si E est $\mathfrak{G}$-complétant, si $\vec{T} \in \mathcal{D}'(E)$ est localement $\mathfrak{G}$-bornée, $\vec{T}$ s'exprime, sur tout ouvert borné $\Omega$ de $R^n$, comme somme finie de dérivées de fonctions continues à valeurs dans E :

$$
(\mathrm{I}, 3; 2 6)
$$

$$
\vec {\mathrm{T}} = \sum_ {| p | \leqslant N (\Omega)} \mathrm{D} ^ {p} \vec {f} _ {p},
$$

avec $\vec{f}_{p}(\Omega) \in \mathfrak{C}$. Si en outre $\vec{T}$ parcourt un ensemble H localement $\mathfrak{C}$-équiborné de $\mathfrak{D}'(E)$, l'entier N($\Omega$) peut être pris le même pour toutes les $\vec{T} \in H$, et les $f_{p}$ peuvent être choisies de manière que $\bigcup_{\vec{T} \in H} \vec{f}_{p}(\Omega)$ appartienne à $\mathfrak{C}$, et que, sur H, les applications

$\vec{\mathbf{T}} \rightarrow \vec{f}_p$ de $\mathfrak{D}'_{\Omega}(\mathrm{E})$ dans $\mathcal{E}^0 (\mathrm{E})$ soient continues.

Il suffit d'appliquer les propositions 23 et 24 à un ouvert $\Omega_{1} \supset \overline{\Omega}$, avec $\mathrm{N}(\Omega) \leqslant m(\Omega_{1}) + n + 1$.

COROLLAIRE 2. — Si E est du type (DF) et quasi-complet, toute distribution à valeurs dans E est, dans tout ouvert Ω borné de R$^{n}$, somme finie de dérivées de fonctions continues à valeurs dans E. Si H est une partie bornée de D'(E), Ω un ouvert borné de R$^{n}$, la décomposition (I, 3; 26) est valable pour toutes les T ∈ H, avec le même N(Ω), et des f$_{p}$ telles que ∪ f$_{p}$(Ω) soit une partie bornée de E, et que, sur H, les applications T → f$_{p}$ soient continues de D'Ω(E) dans ε₀Ω(E).

Il suffit d'appliquer le corollaire 2 de la proposition 23, et la proposition 24.

## § 4. Produits tensoriels topologiques d'espaces de distributions.

Noyaux.

Ce paragraphe généralise le § 2 (propositions 12, 13, 14) et le § 4 (propositions 22, 23, 24, et théorème des noyaux) de notre article antérieur (¹). Soient X$^{l}$, Y$^{m}$, deux espaces euclidiens. Il existe une symétrie canonique s: (x, y) → (y, x) de X$^{l}$ × Y$^{m}$ sur Y$^{m}$ × X$^{l}$; par transport de structure, elle définit un isomorphisme canonique T → $^{s}$T de D$_{x,y}'$ sur D$_{y,x}'$; on pourra noter symboliquement

$$
(\mathrm{I}, 4; \mathrm{1})
$$

$$
{ } ^ { s } \mathrm{T} ( \hat { y } , \hat { x } ) = \mathrm{T} ( \hat { x } , \hat { y } ) .
$$

Si T est une fonction f, cette symétrie se définit aussitôt par

$$
(I, 4; 2) \quad {} ^ {s} f (y, x) = f (x, y) \quad \text { pour   tous } \quad x \in X ^ {l}, \quad y \in Y ^ {m}.
$$

Si T n'est pas une fonction, la formule (I, 4; 1) doit être interprétée, puisqu'il s'agit d'un transport de structure, et que $\mathfrak{D}'$ est défini comme dual de $\mathfrak{D}$, par :

$$
(I, 4; 3) ^ {s} T (\varphi) = T \left(^ {s - 1} \varphi\right), \quad \text { pour   toute } \quad \varphi \in \mathcal {D} _ {\mathbf {Y} ^ {m} \times \mathbf {X} ^ {l}}.
$$

(Nous avons écrit $s^{-1}$, mais il n'y a aucun inconvénient à appeler aussi $s$ la symétrie de $Y^m \times X^l$ sur $X^l \times Y^m$; si $X^l$ et

(1) SCHWARTZ [1].

$Y^{m}$  sont confondus avec un même espace  $R^{n}$ , s est une opération de  $R^{n} \times R^{n}$  sur lui-même, qui est bien sa propre inverse :  $s^{2} = identité$ .

Soit T une distribution sur  $X^{l} \times Y^{m}$ ,  $\mathrm{T}(\hat{x}, \hat{y}) \in \mathcal{D}_{x, y}^{\prime}$ . Elle définit deux opérations importantes associées au noyau T :

$1^{\circ}$ L'opération $\nu\to\mathrm{T}\cdot\nu$ ou $\mathrm{T}.\nu(^{1})$ de $\mathcal{D}_{y}$ dans $\mathcal{D}_{x}^{\prime}$:

$$
(\mathrm{I}, 4; 4) \quad (\mathrm{T} \cdot \nu) (\hat {x}) = \int_ {\mathrm{Y} ^ {m}} \mathrm{T} (\hat {x}, y) \nu (y) d y;
$$

nous mettons $\hat{x}$ parce qu'il s'agit de distributions en $x$, et qu'on ne saurait donner à $x$ une valeur particulière; nous ne mettons pas $\hat{y}$ mais $y$ parce qu'y est variable muette dans une formule d'intégration, ce qui à soi seul empêche de donner à $y$ une valeur particulière. Nous justifierons l'emploi du symbole d'intégration après (I, 4; 10).

Plus précisément, la distribution  $(\mathbf{T} \cdot \nu)(\hat{x}) \in \mathcal{D}_{x}^{\prime}$  est définie par

$$
\left\{ \begin{array}{l} (\mathrm{T} \cdot \nu) \cdot u = \mathrm{T} _ {x, y} \cdot (u (x) \nu (y)) \quad \text { pour } \quad u \in \mathcal {D} _ {x}, \\ \text { ou } \\ \int_ {\mathbf {x} ^ {l}} (\mathrm{T} \cdot \nu) (x) u (x) d x = \iint_ {\mathbf {x} ^ {l} \times \mathbf {Y} ^ {m}} \mathrm{T} (x, y) u (x) \nu (y) d x d y, \end{array} \right. \tag {I,4;5}
$$

ce qui peut s'écrire, avec la notation intégrale de (I, 4; 4):

$$
\begin{array}{r l} \int_ {\mathbf {x} ^ {l}} u (x) d x \int_ {\mathbf {y} ^ {m}} \mathrm{T} (x, y) \nu (y) d y \\ & = \iint_ {\mathbf {x} ^ {l} \times \mathbf {y} ^ {m}} \mathrm{T} (x, y) u (x) \nu (y) d x d y. \end{array} \tag {I,4;6}
$$

$2^{0}$ L'opération $u \to u \cdot T$ ou $u$.T de $\mathfrak{D}_{x}$ dans $\mathfrak{D}_{y}'$:

$$
(\mathrm{I}, 4; 7)
$$

$$
(u \cdot \mathrm{T}) (\hat {y}) = \int_ {\mathbf {x} ^ {l}} u (x) \mathrm{T} (x, \hat {y}) d x.
$$

Cette deuxième application est transposée de la précédente, et l'on a :

$$
\begin{array}{l l} \text {(I, 4; 8)} & \left\{(u \cdot T) \cdot v = u \cdot (T \cdot v) = T _ {x, y} \cdot (u (x) v (y)); \right. \\ & \left. u \cdot T = ^ {s} T \cdot u, \quad T \cdot v = v \cdot {} ^ {s} T. \right. \end{array}
$$

(1) La notation $\mathbf{T} \cdot \nu$ est peut-être préférable à la notation $\mathbf{T} \cdot \nu$, car elle indique tout de suite de quoi il s'agit, même si les variables $x, y$, ne sont pas indiquées. Mais elle est typographiquement compliquée; en outre, $\mathbf{T} \cdot \nu$, pour $\nu \in \mathfrak{D}_y$, et $\mathbf{T} \cdot \varphi$, pour $\varphi \in \mathfrak{D}_{x,y}$, marquent bien deux opérations analogues: une intégration $\int_{\mathbf{Y}^m} dy\ldots$, qui donne une distribution en $x$, et une intégration $\iint_{\mathbf{X}^l \times \mathbf{Y}^m} dx dy\ldots$, qui donne un scalaire.

Posons maintenant  $E = D_{y}^{\prime}$ . Puisque T définit une application linéaire continue de  $D_{x}$  dans  $D_{y}^{\prime}$ , elle définit une distribution sur  $X^{\prime}$  à valeurs dans E; si nous l'appelons  $\vec{T}$ , on aura :

$$
(\mathrm{I}, 4; 9) \quad \vec {\mathrm{T}} (\varphi) = \varphi \cdot \mathrm{T}, \quad \text { pour } \quad \varphi \in \mathfrak {D} _ {x}.
$$

Elle définit aussi une distribution sur  $Y^{m}$  à valeurs dans  $F = D_{x}^{\prime}$ , qui est la distribution définie par  ${}^{s}T$  à partir de la formule (I, 4; 9), et qu'on pourra donc noter  $\overrightarrow{sT}$ :

$$
(\mathrm{I}, 4; 1 0) \quad {} ^ {s} \vec {\mathrm{T}} (\varphi) = \mathrm{T} \cdot \varphi , \quad \text {   pour   } \quad \varphi \in \mathcal {D} _ {y}.
$$

Ce sont les formules (I, 4; 9 et 10) qui justifient l'écriture (I, 4; 4 et 7); $\vec{T}$ est une distribution sur $X^{\prime}$ à valeurs dans $\mathfrak{D}_{y}^{\prime}$, $u(\hat{x})\mathrm{T}(\hat{x},\hat{y})$ aussi, et $u\cdot T$ est son intégrale comme dans (I, 3; 9). Nous reverrons cette question au § 5, 1°) page 131.

La transposée $\vec{\mathbf{T}}$ de la distribution $\vec{\mathbf{T}}$ est une application de $\mathbf{E}' = \mathfrak{D}_y$ dans $\mathfrak{D}_x'$, qui n'est autre que celle qui est définie par la distribution $\vec{\mathbf{T}}$; il n'y aura donc pas d'inconvénient à identifier $\vec{\mathbf{T}}$ et $\vec{\mathbf{T}}$, et on aura aussi $\vec{\mathbf{T}} = \vec{\mathbf{T}}$.

Le théorème des noyaux indique que, réciproquement, toute application linéaire continue de $\mathfrak{D}_x$ dans $\mathfrak{D}_y'$, c'est-à-dire toute distribution sur $X^t$ à valeurs dans $\mathfrak{D}_y'$, peut être définie comme la distribution $\vec{T}$ associée à une distribution $T \in \mathfrak{D}_{x,y}'$; autrement dit (abstraction faite de la topologie, au moins provisoirement), $T \to \vec{T}$ est un isomorphisme de $\mathfrak{D}_{x,y}'$ sur $\mathfrak{D}_x'(\mathfrak{D}_y')$. De même $s^T \to s^T$ est un isomorphisme de $\mathfrak{D}_{y,x}'$ sur $\mathfrak{D}_y'(\mathfrak{D}_x')$. Poursuivant les conventions de la page 51, nous sommes amenés à identifier les 3 espaces $\mathfrak{D}_x' \widehat{\otimes}_{\varepsilon} \mathfrak{D}_y' = \mathfrak{D}_x' \varepsilon \mathfrak{D}_y'$, $\mathfrak{L}(\mathfrak{D}_x; \mathfrak{D}_y')$, $\mathfrak{D}_{x,y}'$, et par suite aussi les 3 espaces $\mathfrak{D}_y' \widehat{\otimes}_{\varepsilon} \mathfrak{D}_x' = \mathfrak{D}_y' \mathfrak{D}_x'$, $\mathfrak{L}(\mathfrak{D}_y; \mathfrak{D}_x')$, $\mathfrak{D}_{y,x}'$; l'opération $t$ ou $s$ fait passer d'un système à l'autre. En résumé, nous nous permettons d'identifier deux de ces espaces isomorphes, si et seulement si, dans l'écriture de ces espaces, l'ordre des variables $x$, $y$ est le même. Dans bien des cas il peut être plus commode de tout identifier, mais dans d'autre cas de ne faire aucune identification; d'ailleurs le caractère assez arbitraire de ces identifications saute aux yeux. Un cas important est celui ou $X^t = Y^m = R^n$. Les règles précédentes conduisent alors à ce qui suit.

Soit T une distribution sur  $R^{n} \times R^{n}$ . Elle définit deux opérations  $\varphi \to \varphi \cdot T$  et  $\varphi \to T \cdot \varphi$  de  $D_{R^{n}}$  dans  $D_{R^{n}}^{\prime}$ ; celles-ci opèrent cette fois dans les mêmes espaces, mais sont distinctes, et toujours définies par les formules (1, 4; 4) et (1, 4; 7), où n'interviennent que des variables génériques ou muettes, x, y, qui peuvent être aussi bien remplacées par d'autres. C'est toujours l'opération  $\varphi \to \varphi \cdot T$  de D dans  $D^{\prime}$  qui définit la distribution  $\vec{T}$  associée à T:  $\vec{T}$  est une distribution sur  $R^{n}$  à valeurs dans  $D_{R^{n}}^{\prime}$ . La symétrie s opère de  $R^{n} \times R^{n}$  sur lui-même, donc par transport de structure de  $D_{R^{n} \times R^{n}}^{\prime}$  sur lui-même; à T elle fait correspondre  $^{s}T$  qui est une autre distribution sur  $R^{n} \times R^{n}$ . Alors  $^{s}\vec{T}$  est la distribution sur  $R^{n}$  à valeurs dans  $D_{R^{n}}^{\prime}$  définie par  $\varphi \to \varphi \cdot ^{s}T = T \cdot \varphi$ ;  $^{s}\vec{T}$  coïncide avec  $^{t}\vec{T}$ , transposée de la distribution  $\vec{T}$  au sens de la page 51. Si maintenant U et V sont deux distributions sur  $R^{n}$ , U⊗V est une distribution bien déterminée sur  $R^{n} \times R^{n}$ , à ne pas confondre avec V⊗U, qui est sa symétrique; U⊗V est la distribution sur  $R^{n} \times R^{n}$ , qui, à la fonction  $(x, y) \to u(x)\upsilon(y)$  de  $D_{R^{n} \times R^{n}}$ , fait correspondre U(u)V( $\nu$ ). Alors la distribution ( $\overline{U\otimes V}$ ) associée à U⊗V est définie par  $\varphi \to U(\varphi)V$ , sa transposée est  $\varphi \to V(\varphi)U$ . Nous avons là un exemple typique où toutes les identifications ne sont pas souhaitables, mais où celles que nous avons adoptées ne mènent pas à contradiction.

Nous allons voir maintenant que $\mathfrak{D}_{x}^{\prime}\widehat{\otimes}_{\varepsilon}\mathfrak{D}_{y}^{\prime}=\mathfrak{D}_{x}^{\prime}(\mathfrak{D}_{y}^{\prime})$ est isomorphe à $\mathfrak{D}_{x,y}^{\prime}$, non seulement algébriquement, mais topologiquement; et nous donnerons en même temps une nouvelle démonstration de l'isomorphisme algébrique; pour tout cela, nous nous appuierons sur la théorie des espaces nucléaires de Grothendieck, qui est la clef des théorèmes relatifs aux noyaux (nucléaires vient précisément de noyaux).

## Le théorème des noyaux.

PROPOSITION 25. — (Théorème des noyaux). $\mathfrak{D}_{x,y}^{\prime}$ est identique, algébriquement et topologiquement, à $\mathfrak{D}_{x}^{\prime}(\mathfrak{D}_{y}^{\prime})=\mathfrak{D}_{x}^{\prime}\widehat{\otimes}_{\epsilon}\mathfrak{D}_{y}^{\prime}$.

DÉMONSTRATION. — Comme toute distribution  $T \in D'_{x,y}$  définit l'application linéaire continue  $\varphi \to \varphi$ . T de  $D_x$  dans  $D'_{y}$ , elle définit un élément  $\vec{T}$  de  $\mathcal{D}'_{x}(\mathcal{D}'_{y})$ ;  $T \to \vec{T}$  est injective,

parce que si $\vec{\mathbf{T}}=0$, T est nulle sur le sous-espace dense $\mathfrak{D}_{x}\otimes\mathfrak{D}_{y}$ de $\mathfrak{D}_{x,y}$. Donc il est trivial que $\mathfrak{D}^{\prime}_{x,y}$ est un sous-espace de $\mathfrak{D}^{\prime}_{x}(\mathfrak{D}^{\prime}_{y})$. D'autre part, si T converge vers 0 dans $\mathfrak{D}^{\prime}_{x,y}$, T($\varphi$) converge vers 0 uniformément quand $\varphi$ reste bornée dans $\mathfrak{D}_{x,y}$, donc a fortiori T(u$\otimes$v), u$\in\mathfrak{D}_{x}$, v$\in\mathfrak{D}_{y}$, converge vers 0 uniformément quand u et v restent bornées dans $\mathfrak{D}_{x}$ et $\mathfrak{D}_{y}$, donc $\vec{\mathbf{T}}$ converge vers 0 dans $\mathfrak{D}^{\prime}_{x}\widehat{\otimes}_{\varepsilon}\mathfrak{D}^{\prime}_{y}$; il est donc également trivial que la topologie de $\mathfrak{D}^{\prime}_{x,y}$ est plus fine que la topologie induite par $\mathfrak{D}^{\prime}_{x}(\mathfrak{D}^{\prime}_{y})$.

De la même manière, il est évident que $\mathcal{E}_{x,y}^{\prime}$ est un sous-espace de $\mathcal{E}_{x}^{\prime}(\mathcal{E}_{y}^{\prime})$ (car si $\mathbf{T} \in \mathcal{E}_{x,y}^{\prime}$, $\varphi \to \varphi$. T est continue de $\mathcal{E}_{x}$ dans $\mathcal{E}_{y}^{\prime}$), et que sa topologie est plus fine que la topologie induite.

Un élément T de $\mathcal{E}_{x}^{\prime}\widehat{\otimes}_{\varepsilon}\mathcal{E}_{y}^{\prime}=\mathcal{E}_{x}^{\prime}\varepsilon\mathcal{E}_{y}^{\prime}$ est une forme bilinéaire sur $\mathcal{E}_{x}\times\mathcal{E}_{y}$, séparément continue, donc continue puisque $\mathcal{E}_{x}$ et $\mathcal{E}_{y}$ sont des espaces de Fréchet$^{(1)}$; réciproquement toute forme bilinéaire continue sur $\mathcal{E}_{x}\times\mathcal{E}_{y}$ est a fortiori $\varepsilon$-hypocontinue sur $(\mathcal{E}_{x}^{\prime})_{c}^{\prime}\times(\mathcal{E}_{y}^{\prime})_{c}^{\prime}$, donc appartient à $\mathcal{E}_{x}^{\prime}\varepsilon\mathcal{E}_{y}^{\prime}$. Ainsi $\mathcal{E}_{x}^{\prime}\widehat{\otimes}_{\varepsilon}\mathcal{E}_{y}^{\prime}$ est, algébriquement, l'espace des formes bilinéaires continues sur $\mathcal{E}_{x}\times\mathcal{E}_{y}$, ou des formes linéaires continues sur $\mathcal{E}_{x}\widehat{\otimes}_{\pi}\mathcal{E}_{y}$, donc $\mathcal{E}_{x}^{\prime}\widehat{\otimes}_{\varepsilon}\mathcal{E}_{y}^{\prime}=(\mathcal{E}_{x}\widehat{\otimes}_{\pi}\mathcal{E}_{y})^{\prime}$. Un élément T de $\mathcal{E}_{x,y}^{\prime}$ est une forme linéaire continue sur $\mathcal{E}_{x,y}=\mathcal{E}_{x}\widehat{\otimes}_{\varepsilon}\mathcal{E}_{y}$, donc $\mathcal{E}_{x,y}^{\prime}$ est, algébriquement, $(\mathcal{E}_{x}\widehat{\otimes}_{\varepsilon}\mathcal{E}_{y})^{\prime}$ (appelé encore par Grothendieck espace des formes bilinéaires intégrales$^{(2)}$ sur $\mathcal{E}_{x}\times\mathcal{E}_{y}$). L'injection de $\mathcal{E}_{x,y}^{\prime}$ dans $\mathcal{E}_{x}^{\prime}\widehat{\otimes}_{\varepsilon}\mathcal{E}_{y}^{\prime}$ est la transposée de l'application canonique de $\mathcal{E}_{x}\widehat{\otimes}_{\pi}\mathcal{E}_{y}$ dans $\mathcal{E}_{x}\widehat{\otimes}_{\varepsilon}\mathcal{E}_{y}$.

Utilisant alors le caractère nucléaire de $\mathcal{E}_{x}$ et $\mathcal{E}_{y}(^{3})$, nous pouvons écrire que $\mathcal{E}_{x} \widehat{\otimes}_{\pi} \mathcal{E}_{y} = \mathcal{E}_{x} \widehat{\otimes}_{\epsilon} \mathcal{E}_{y}$ (que nous noterons simplement $\mathcal{E}_{x} \widehat{\otimes} \mathcal{E}_{y}$), donc $\mathcal{E}_{x,y}^{\prime}$ est algébriquement identique à $\mathcal{E}_{x}^{\prime} \widehat{\otimes}_{\epsilon} \mathcal{E}_{y}^{\prime}$. D'autre part, la topologie de $\mathcal{E}_{x,y}^{\prime}$ est celle de la convergence uniforme sur les parties compactes de $\mathcal{E}_{x,y} = \mathcal{E}_{x} \widehat{\otimes} \mathcal{E}_{y}$; la topologie de $\mathcal{E}_{x}^{\prime} \widehat{\otimes}_{\epsilon} \mathcal{E}_{y}^{\prime}$ est celle de la convergence uniforme sur les produits tensoriels de parties compactes de $\mathcal{E}_{x}$ et de $\mathcal{E}_{y}$; mais, puisque $\mathcal{E}$ est un espace de Fréchet, toute partie compacte de $\mathcal{E}_{x} \widehat{\otimes}_{\pi} \mathcal{E}_{y}$ est contenue dans l'enveloppe d'un produit tensoriel de

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) BOURBAKI [2], proposition 2, page 38.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) GROTHENDIECK [4], § 4, n°3, page 124.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(3) GROTHENDIECK [5], § 2, n° 3, théorème 10, page 55. Voir aussi SCHWARTZ [2], exposé 18, page 5, exemple a).</span></small>

parties compactes de $\mathcal{E}_{x}$ et de $\mathcal{E}_{y}(1)$, et les deux topologies sont les mêmes. Tout ce que nous venons de faire ici n'est qu'une partie de la démonstration, dans le cas particulier des espaces $\mathcal{E}_{x}$ et $\mathcal{E}_{y}$, d'une proposition générale :

Si G et H sont des espaces de Fréchet nucléaires, G' et H' sont nucléaires, et le dual fort de G⊗H est $\mathfrak{L}_{b}(\mathrm{G};\mathrm{H}')=\mathrm{G}'\otimes\mathrm{H}'(^{2})$. Nous avons préféré redonner la démonstration dans ce cas particulier, étant donné son importance.

Revenons maintenant à $\mathfrak{D}_x$ et $\mathfrak{D}_y$. Ces espaces sont bien nucléaires (3), mais ne sont plus des espaces de Fréchet. D'ailleurs la conclusion analogue à la précédente serait fausse: $\mathfrak{D}_x'(\mathfrak{D}_y') = \mathfrak{D}_x' \widehat{\otimes} \mathfrak{D}_y'$ sera bien identique, algébriquement et topologiquement, à $\mathfrak{D}_x', y$, dual fort de $\mathfrak{D}_{x,y}$; mais $\mathfrak{D}_{x,y} = \mathfrak{D}_x \widehat{\otimes}_i \mathfrak{D}_y$ (4), algébriquement identique à $\mathfrak{D}_x \widehat{\otimes}_\varepsilon \mathfrak{D}_y$, ne lui est pas identique topologiquement (5), et n'a pas le même dual, on a donc $\mathfrak{D}_x' \widehat{\otimes} \mathfrak{D}_y' \neq (\mathfrak{D}_x \widehat{\otimes} \mathfrak{D}_y)'$.

Ce que nous devons faire ici, c'est répéter la quatrième partie de la démonstration élémentaire du théorème des noyaux, donnée antérieurement (⁶). Soit T ∈ D′x ⊗ D′y. T est une forme bilinéaire hypocontinue sur Dx × Dy. Soient L et M des ouverts bornés de X' et Ym. Si α (resp. β) appartient à Dx (resp. Dy), et vaut 1 sur L (resp. M), la forme bilinéaire (u, ν) → T(αu, βν) coïncide avec (u, ν) → T(u, ν) sur le sous-espace Dx × Dy de Dx × Dy; mais comme la première est hypo-continue sur εx × εγ, il existe une distribution T̄L,M(ˆx,ˆy) telle que, pour u ∈ D\_L et ν ∈ D\_M, on ait:

$$
\mathrm{T} (u, \nu) = \overline {{\mathrm{T}}} _ {\mathrm{L}, \mathrm{M}} (u \otimes \nu).\tag{I, 4; 11}
$$

Les ouverts $\mathbf{L} \times \mathbf{M}$ forment un recouvrement de $\mathbf{X}^l \times \mathbf{Y}^m$. Si $\mathbf{L} \times \mathbf{M}$, $\mathbf{L}' \times \mathbf{M}'$, sont deux de ces ouverts, $\mathbf{L} \subset \mathbf{L}'$, $\mathbf{M} \subset \mathbf{M}'$, $\overline{\mathbf{T}}_{\mathbf{L},\mathbf{M}}$ et $\overline{\mathbf{T}}_{\mathbf{L}',\mathbf{M}'}$ coïncident sur $\mathfrak{D}_{\mathbf{L} \times \mathbf{M}}$ puisqu'elles coïncident sur le sous-espace dense $\mathfrak{D}_{\mathbf{L}} \otimes \mathfrak{D}_{\mathbf{M}}$. L'ensemble des distributions $\overline{\mathbf{T}}_{\mathbf{L},\mathbf{M}}$ définit donc une distribution $\overline{\mathbf{T}} \in \mathfrak{D}'_{x,y}$, telle que

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) GROTHENDIECK [4], § 2, n° 1, corollaire 1 du théorème 1, page 52.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) GROTHENDIECK [5], § 2, n° 1, théorème 7, page 40, et § 3, n° 2, théorème 12, page 76. Voir aussi SCHWARTZ [2], exposé 19, théorème 3, page 4.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">[5], § 2, n° 3.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(3) GROTHENDIECK [5], § 2, n° 3, théorème 10, page 55. Voir aussi SCHWARTZ [2]. exposé 18, page 5, exemple b).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(4) GROTHENDIECK [5], page 84.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(5) Schwartz [1], page 116.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(6) Schwartz [1], page 144.</span></small>

$\overline{\mathbf{T}}(u \otimes v) = \mathbf{T}(u, v)$ pour $u \in \mathfrak{D}_x$ et $v \in \mathfrak{D}_y$, et $\mathfrak{D}_{x,y}'$ est bien algébriquement identique à $\mathfrak{D}_x' \widehat{\otimes} \mathfrak{D}_y'$.

Reste à voir l'identité topologique de ces deux espaces. La convergence de T vers 0 dans $\mathfrak{D}_{x}^{\prime}\widehat{\otimes}\mathfrak{D}_{y}^{\prime}$ signifie la convergence de T(u⊗ν) vers 0, uniformément lorsque u et ν restent bornées dans $\mathfrak{D}_{x}$ et $\mathfrak{D}_{y}$; donc aussi la convergence de $\alpha(\hat{x})\beta(\hat{y})\mathrm{T}(\hat{x},\hat{y})$ dans $\mathfrak{E}_{x}^{\prime}\widehat{\otimes}\mathfrak{E}_{y}^{\prime}$, pour toute $\alpha\in\mathfrak{D}_{x}$ et $\beta\in\mathfrak{D}_{y}$. Mais nous savons que la topologie de $\mathfrak{E}_{x}^{\prime}\widehat{\otimes}\mathfrak{E}_{y}^{\prime}$ est celle de $\mathfrak{E}_{x,y}^{\prime}$, et la convergence de $\alpha\beta\mathrm{T}$ vers 0 dans $\mathfrak{E}_{x,y}^{\prime}$, pour toute $\alpha\in\mathfrak{D}_{x}$ et $\beta\in\mathfrak{D}_{y}$, est précisément la convergence de T vers 0 dans $\mathfrak{D}_{x,y}^{\prime}$, convergence qui est de nature locale sur X′×Ym; donc les topologies de $\mathfrak{D}_{x,y}^{\prime}$ et $\mathfrak{D}_{x}^{\prime}\widehat{\otimes}\mathfrak{D}_{y}^{\prime}$ sont bien identiques, c.q.f.d.

Les espaces $\mathcal{H}_{x}\in\mathcal{K}_{y}$.

Soit $\mathcal{H}_x$ (resp. $\mathfrak{K}_y$) un espace de distributions sur $\mathbf{X}^i$ (resp. $\mathbf{Y}^m$). On peut alors considérer, d'après la proposition 1, $\mathcal{H}_x \in \mathfrak{K}_y$ comme un sous-espace de $\mathcal{D}_x' \in \mathcal{D}_y' = \mathcal{D}_{x,y}'$, muni d'une topologie plus fine que la topologie induite. Pour que $\mathbf{T} \in \mathcal{D}_{x,y}'$ appartienne à $\mathcal{H}_x \in \mathfrak{K}_y$, il est nécessaire qu'il appartienne à $\mathcal{D}_x' \in \mathfrak{K}_y$, donc que $u \to u \cdot \mathbf{T}$ définisse une application linéaire continue de $\mathcal{D}_x$ dans $\mathfrak{K}_y$. Il est aussi nécessaire qu'il appartienne à $\mathcal{H}_x \in \mathcal{D}_y'$, ce qui veut dire que $\nu \to \mathbf{T} \cdot \nu$ est une application linéaire continue de $\mathcal{D}_y$ dans $\mathcal{H}_x$. Mais ces deux conditions nécessaires ne sont pas suffisantes; $\mathcal{H}_x \in \mathfrak{K}_y$ n'est pas l'intersection de $\mathcal{H}_x \in \mathcal{D}_y'$ et de $\mathcal{D}_x' \in \mathfrak{K}_y$; on sait par exemple qu'un noyau régulier, appartenant à la fois à $\mathcal{E}_x \in \mathcal{D}_y'$ et à $\mathcal{D}_x' \in \mathcal{E}_y$, n'appartient pas nécessairement à $\mathcal{E}_x \in \mathcal{E}_y = \mathcal{E}_{x,y}$, espace des noyaux régularisants, comme le montre l'exemple du noyau $\delta(\hat{x} - \hat{y})$ ($^1$).

Remarque. — La symétrie $s: \mathcal{D}_{x,y}^{\prime} \to \mathcal{D}_{y,x}^{\prime}$ induit la symétrie $\mathcal{H}_x \in \mathcal{K}_y \to \mathcal{K}_y \in \mathcal{H}_x$ (voir remarque 2°, page 35).

Critères d'appartenance à $\mathcal{H}_{x}\in\mathcal{K}_{y}$.

PROPOSITION 26. — Soient $\mathcal{H}_{x}$ et $\mathfrak{K}_{y}$ des espaces de distributions normaux ($\mathcal{H}_{x}$ n'est pas nécessairement quasi-complet), $\mathcal{H}_{x}$ vérifiant la propriété ($\varepsilon$). Toute distribution $T \in \mathfrak{D}_{x}^{\prime} \otimes \mathfrak{K}_{y}$ telle que, pour toute $\nu \in \mathfrak{K}_{y}^{\prime}$, $T \cdot \nu$ soit dans $\mathcal{H}_{x}$, appartient à $\mathcal{H}_{x} \varepsilon \mathfrak{K}_{y}$. Il suffit d'appliquer la définition de la propriété ($\varepsilon$) à $E = \mathfrak{K}_{y}$

(1) Voir plus loin, page 99 et page 102.

(rappelons que, dans la propriété $(\varepsilon)$, E est supposé quasi-complet, mais non $\mathcal{H}_x$).

Remarque. — En échangeant les rôles de x et y, on a naturellement un critère symétrique, utilisant u·T au lieu de T·v.

PROPOSITION 27. — Soit $\mathcal{H}_{x}$ un espace normal tel que, dans $\mathfrak{L}_{s}(\mathcal{H}_{x};\mathcal{H}_{x})$, l'identité soit strictement adhérente au sous-espace des restrictions d'applications linéaires continues de $\mathfrak{D}'_{x}$ dans $\mathcal{H}_{x}$; et soit $\mathfrak{M}_{y}$ un espace normal tonnelé; ces espaces ne sont pas nécessairement quasi-complets. Alors toute distribution $\mathrm{T}\in\mathfrak{D}'_{x}\varepsilon(\mathfrak{M}_{y})_{c}^{\prime}$ telle que, pour toute $\nu\in\mathfrak{M}_{y}$, $\mathrm{T}\cdot\nu$ soit dans $\mathcal{H}_{x}$, appartient à $\mathcal{H}_{x}\varepsilon(\mathfrak{M}_{y})_{c}^{\prime}$.

Rappelons d'abord qu'un espace tonnelé a la topologie $\tau$ (1), donc $a$ fortiori la topologie $\gamma$.

Appelons $\Lambda_s$ ($\mathfrak{M}_y$; $\mathcal{H}_x$) l'espace de toutes les applications linéaires de $\mathfrak{M}_y$ dans $\mathcal{H}_x$, muni de la topologie de la convergence simple. L'application $L \to L \circ {}^t\vec{T}$ est continue de $\mathscr{L}_s(\mathcal{H}_x; \mathcal{H}_x)$ dans $\Lambda_s(\mathfrak{M}_y; \mathcal{H}_x)$. On a I° $^\prime\vec{T} = {}^\prime\vec{T}$; et si L est la restriction d'une application linéaire continue de $\mathscr{D}_x'$ dans $\mathcal{H}_x$, L° $^\prime\vec{T}$ est continue de $\mathfrak{M}_y$ dans $\mathcal{H}_x$, parce que $^\prime\vec{T}$ est continue de $\mathfrak{M}_y$ dans $\mathscr{D}_x'$. Alors l'hypothèse faite sur $\mathcal{H}_x$ entraîne que $^\prime\vec{T}$ soit strictement adhérente, dans $\Lambda_s(\mathfrak{M}_y; \mathcal{H}_x)$, au sous-espace $\mathscr{L}_s(\mathfrak{M}_y; \mathcal{H}_x)$ des applications linéaires continues de $\mathfrak{M}_y$ dans $\mathcal{H}_x$. Mais comme $\mathfrak{M}_y$ est tonnelé, $\mathscr{L}_s(\mathfrak{M}_y; \mathcal{H}_x)$ est quasi-fermé dans $\Lambda_s(\mathfrak{M}_y; \mathcal{H}_x)$ (car toute partie bornée de $\mathscr{L}_s(\mathfrak{M}_y; \mathcal{H}_x)$ est équicontinue, et toute application simplement adhérente à une partie équicontinue est continue) (²), donc $^\prime\vec{T}$ est continue de $\mathfrak{M}_y$ dans $\mathcal{H}_x$, et T ∈ $\mathcal{H}_x$ ε ($\mathfrak{M}_y$)', c.q.f.d.

Remarque. — La condition de l'énoncé relative à $\mathcal{H}_{x}$ est sûrement vérifiée, si $\mathcal{H}_{x}$ (supposé normal) a la propriété d'approximation par troncature et régularisation; car alors I est strictement adhérente dans $\mathcal{L}_{c}(\mathcal{H}_{x};\mathcal{H}_{x})$, donc a fortiori dans $\mathcal{L}_{s}(\mathcal{H}_{x};\mathcal{H}_{x})$, au sous-espace des applications $\{\rho_{\lambda}\}^{\circ}[\alpha_{\nu}]$ (voir

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">F</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) BOURBAKI [2], proposition 5, page 70.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) Voir BOURBAKI [2], théorème 2, page 27; et proposition 4, page 23. Rappelons qu'une partie A d'un espace vectoriel topologique F est dite quasi-fermée, si tout point de F, adhérent à une partie bornée de A, est dans A.</span></small>

préliminaires page 9), restrictions d'applications continues de $\mathfrak{D}_x'$ dans $\mathfrak{D}_x$ donc dans $\mathcal{H}_x$.

Cas où $\mathcal{H}_x$ et $\mathcal{K}_y$ sont de même nature.

PROPOSITION 28. — On a les identités (algébriques et topologiques):

$$
\begin{array}{c} \mathcal {E} _ {x, y} = \mathcal {E} _ {x} \widehat {\otimes} \mathcal {E} _ {y}, \qquad \mathcal {I} _ {x, y} = \mathcal {I} _ {x} \widehat {\otimes} \mathcal {I} _ {y}, \\ (\mathcal {O} _ {\mathrm{M}}) _ {x, y} = (\mathcal {O} _ {\mathrm{M}}) _ {x} \widehat {\otimes} (\mathcal {O} _ {\mathrm{M}}) _ {y}, \qquad \mathfrak {D} _ {x, y} ^ {\prime} = \mathfrak {D} _ {x} ^ {\prime} \widehat {\otimes} \mathfrak {D} _ {y} ^ {\prime}, \\ \mathcal {E} _ {x, y} ^ {\prime} = \mathcal {E} _ {x} ^ {\prime} \widehat {\otimes} \mathcal {E} _ {y} ^ {\prime}, \qquad \mathcal {I} _ {x, y} ^ {\prime} = \mathcal {I} _ {x} ^ {\prime} \widehat {\otimes} \mathcal {I} _ {y} ^ {\prime}, \qquad (\mathcal {O} _ {\mathrm{C}} ^ {\prime}) _ {x, y} = (\mathcal {O} _ {\mathrm{C}} ^ {\prime}) _ {x} \widehat {\otimes} (\mathcal {O} _ {\mathrm{C}} ^ {\prime}) _ {y}, \\ \mathfrak {B} _ {x, y} ^ {*} = \mathfrak {B} _ {x} ^ {*} \widehat {\otimes} _ {\varepsilon} \mathfrak {B} _ {y} ^ {*}, \qquad (\mathfrak {B} _ {c}) _ {x, y} = (\mathfrak {B} _ {c}) _ {x} \widehat {\otimes} _ {\varepsilon} (\mathfrak {B} _ {c}) _ {y}. \end{array}
$$

DÉMONSTRATION. — A part $\mathcal{B}^{\bullet}$ et $\mathcal{B}_{c}$, tous les espaces considérés sont nucléaires, ce qui permet d'écrire $\widehat{\otimes}$ pour $\widehat{\otimes}_{\varepsilon} = \widehat{\otimes}_{\pi}(^{1})$.

Le cas de $\mathcal{B}^{\bullet}$ a été réglé à la proposition 17; celui de $\mathcal{B}_{c}, \mathcal{E}, \mathcal{F}, \mathcal{O}_{\mathbf{M}}$, dans un article antérieur $(^{2})$; nous avons aussi indiqué à ce moment que $\mathcal{D}_{x} \widehat{\otimes} \mathcal{D}_{y}$ est identique algébriquement à $\mathcal{D}_{x,y}$, mais non topologiquement, car il a une topologie moins fine, et n'a même pas le même dual.

La quatrième identité est le résultat de la proposition 25.
La cinquième a été démontrée comme résultat intermédiaire pour démontrer la proposition 25.

La sixième se démontre de la même manière que la cinquième : $\mathcal{S}_{x}$ et $\mathcal{S}_{y}$ sont des espaces de Fréchet nucléaires, donc le dual de $\mathcal{S}_{x} \widehat{\otimes} \mathcal{S}_{y} = \mathcal{S}_{x,y}$, c'est-à-dire $\mathcal{S}_{x,y}^{\prime}$, est $\mathcal{S}_{x}^{\prime} \widehat{\otimes} \mathcal{S}_{y}^{\prime}$ (voir pages 93 à 95).

Enfin la septième se démontre par transformation de Fourier à partir de la troisième. Nous utiliserons pour cela la proposition suivante :

PROPOSITION 29. — La transformation de Fourier $\mathcal{F}_{x,y}$ sur $\mathcal{F}_{x,y}^{\prime} = \mathcal{F}_{x}^{\prime} \otimes \mathcal{F}_{y}^{\prime}$ est le produit tensoriel $\mathcal{F}_{x} \otimes \mathcal{F}_{y}$ des transformations de Fourier sur $\mathcal{F}_{x}^{\prime}$ et $\mathcal{F}_{y}^{\prime}$.

En effet $\mathcal{F}_{x,y}$ et $\mathcal{F}_x\otimes \mathcal{F}_y$ sont toutes deux continues sur $\mathcal{S}'_{x,y}$, et elles coïncident sur le sous-espace dense $\mathcal{S}'_x\otimes \mathcal{S}'_y$, comme on le voit immédiatement.

Ceci nous permet de terminer la démonstration de la proposition 28. La transformation $\mathcal{F}_{\xi} \otimes \mathcal{F}_{\eta}$ de $(\mathcal{O}_{\mathbf{M}})_{\xi} \widehat{\otimes} (\mathcal{O}_{\mathbf{M}})_{\eta}$ sur $(\mathcal{O}_{\mathbf{C}}^{\prime})_{x} \widehat{\otimes} (\mathcal{O}_{\mathbf{C}}^{\prime})_{y}$ est un isomorphisme, restriction de l'isomorphisme

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) GROTHENDIECK [5], théorème 10, page 55.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) SCHWARTZ [1], proposition 12, page 113, et bas de la page 115.</span></small>

$\mathcal{F}_{\xi} \otimes \mathcal{F}_{\eta}$ de $\mathcal{S}_{\xi}^{\prime} \widehat{\otimes} \mathcal{S}_{\eta}^{\prime}$ sur $\mathcal{S}_{x}^{\prime} \widehat{\otimes} \mathcal{S}_{y}^{\prime}$ (remarque $2^{\circ}$ après la proposition 1 du § 1); mais ce dernier n'est autre que $\mathcal{F}_{\xi, \eta}$ (proposition 29), et on sait que $(\mathcal{O}_{\mathrm{M}})_{\xi} \widehat{\otimes} (\mathcal{O}_{\mathrm{M}})_{\eta} = (\mathcal{O}_{\mathrm{M}})_{\xi, \eta}$ (proposition 28), enfin $\mathcal{F}_{\xi, \eta}$ est un isomorphisme de $(\mathcal{O}_{\mathrm{M}})_{\xi, \eta}$ sur $(\mathcal{O}_{\mathrm{C}}^{\prime})_{x, y}$, donc $(\mathcal{O}_{\mathrm{C}}^{\prime})_{x} \widehat{\otimes} (\mathcal{O}_{\mathrm{C}}^{\prime})_{y} = (\mathcal{O}_{\mathrm{C}}^{\prime})_{x, y}$, c.q.f.d.

Remarque. — $\mathcal{E}_{x}^{\prime}(\mathcal{E}_{y}^{\prime})$ et $\overline{\mathcal{E}}_{x}^{\prime}(\mathcal{E}_{y}^{\prime})$ coïncident, algébriquement et topologiquement. En effet, on a $a$ priori $\overline{\mathcal{E}}_{x}^{\prime}(\mathcal{E}_{y}^{\prime})\subset\mathcal{E}_{x}^{\prime}(\mathcal{E}_{y}^{\prime})$; mais $\mathcal{E}_{x}^{\prime}(\mathcal{E}_{y}^{\prime})=\mathcal{E}_{x,y}^{\prime}\subset\overline{\mathcal{E}}_{x}^{\prime}(\mathcal{E}_{y}^{\prime})$, donc il y a bien coïncidence algébrique. Ensuite $\overline{\mathcal{E}}_{x}^{\prime}(\mathcal{E}_{y}^{\prime})$ est $a$ priori plus fine que $\mathcal{E}_{x}^{\prime}(\mathcal{E}_{y}^{\prime})$; mais $\mathcal{E}_{x}^{\prime}(\mathcal{E}_{y}^{\prime})=\mathcal{E}_{x,y}^{\prime}$, et comme $\overline{\mathcal{E}}_{x}^{\prime}(\mathcal{E}_{y}^{\prime})$ et $\mathcal{E}_{x,y}^{\prime}$ induisent la même topologie sur les $\mathcal{E}_{\mathrm{H}\times\mathrm{K}}^{\prime}$ (H et K compacts de $\mathbf{R}^{n}$), et que $\mathcal{E}_{x,y}^{\prime}$ est la limite inductive des $\mathcal{E}_{\mathrm{H}\times\mathrm{K}}^{\prime}$, $\mathcal{E}_{x,y}^{\prime}$ est plus fine, donc ces deux topologies sont identiques. Ceci est conforme à ce que nous avons vu page 62, puisque $\mathcal{E}^{\prime}$, dual d'un espace de Fréchet, est du type (DF).

Cas où  $H_{x}$  et  $K_{y}$  ne sont pas des espaces de même nature.

Noyaux semi-réguliers, réguliers, régularisants (').

$\mathcal{E}_{x}(\mathfrak{D}_{y}^{\prime}) = \mathcal{E}_{x}\widehat{\otimes}\mathfrak{D}_{y}^{\prime} = \mathfrak{L}(\mathcal{E}_{x}^{\prime};\mathfrak{D}_{y}^{\prime})$ est l'espace des noyaux semi-réguliers en $x$ ou semi-réguliers à gauche; la symétrie $s$ le transporte sur l'espace $\mathfrak{D}_{y}^{\prime}(\mathcal{E}_{x}) = \mathfrak{D}_{y}^{\prime}\widehat{\otimes}\mathcal{E}_{x} = \mathfrak{L}(\mathfrak{D}_{y};\mathcal{E}_{x})$, qui, dans $\mathfrak{D}_{y,x}^{\prime}$, est l'espace des noyaux semi-réguliers en $x$ ou semi-réguliers à droite. D'après la proposition 26, appliquée à $\mathcal{H}_x = \mathcal{E}_x,\mathfrak{K}_y = \mathfrak{D}_y^\prime$, T est semi-régulier en $x$ si et seulement si, pour toute $\nu \in \mathfrak{D}_y$, T·$\nu$ est dans $\mathcal{E}_x$.

$\mathfrak{D}_{x}^{\prime}(\mathfrak{E}_{y})=\mathfrak{D}_{x}^{\prime}\widehat{\otimes}\mathfrak{E}_{y}=\mathfrak{L}(\mathfrak{D}_{x};\mathfrak{E}_{y})$ est l'espace des noyaux semi-réguliers en $y$ ou semi-réguliers à droite; il est transporté par la symétrie $s$ sur $\mathfrak{E}_{y}(\mathfrak{D}_{x}^{\prime})=\mathfrak{E}_{y}\widehat{\otimes}\mathfrak{D}_{x}^{\prime}=\mathfrak{L}(\mathfrak{E}_{y}^{\prime};\mathfrak{D}_{x}^{\prime})$, espace des noyaux semi-réguliers en $y$ ou semi-réguliers à gauche.

Si T est semi-régulier en $x$, la formule (I, 4; 4) peut-être considérée comme définissant un élément de $\mathcal{E}_{x}$, intégrale en $y$ de $\mathrm{T}(\hat{x},\hat{y})\nu(\hat{y}) = {}^{s}\overrightarrow{\mathrm{T}}(\hat{y})\nu(\hat{y}) \in \mathcal{E}_{y}^{\prime}(\mathcal{E}_{x})$; elle peut donc être remplacée par une formule analogue où $\hat{x}$ est remplacé par $x$, elle est alors valable pour tout $x$ fixé dans $\mathrm{X}^{\prime}$, l'intégrale ayant un sens évident puisque $\mathrm{T}(x,\hat{y})$ est une distribution en $y$ et $\nu(\hat{y})$ une fonction indéfiniment différentiable à support compact.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Ces noyaux, ainsi que ceux du numéro suivant, ont été étudiés dans SCHWARTZ [6], n° 6 et 7.</span></small>

On peut aussi écrire (I, 4; 7) pour $u \in \mathcal{E}_{x}^{\prime}$, car $x \to \mathrm{T}(x, \hat{y})$ est une fonction indéfiniment différentiable de $x$ à valeurs dans $\mathfrak{D}_{y}^{\prime}$, donc on peut faire son produit par une distribution $u(\hat{x})$, et comme celle-ci est à support compact, $u(\hat{x})\mathrm{T}(\hat{x}, \hat{y})$ est une distribution à support compact en $x$ à valeurs dans $\mathfrak{D}_{y}^{\prime}$, et son intégrale a un sens comme élément de $\mathfrak{D}_{y}^{\prime}$.

L'intersection de $\mathcal{E}_{x}\widehat{\otimes}\mathcal{D}_{y}^{\prime}$ et de $\mathcal{D}_{x}^{\prime}\widehat{\otimes}\mathcal{E}_{y}$, munie de la topologie borne supérieure des topologies induites, est l'espace des noyaux réguliers. Il est distinct de $\mathcal{E}_{x}\widehat{\otimes}\mathcal{E}_{y}=\mathcal{E}_{x,\dot{y}}=\mathfrak{L}(\mathcal{E}_{x}^{\prime};\mathcal{E}_{y})\approx\mathfrak{L}(\mathcal{E}_{y}^{\prime};\mathcal{E}_{x})$, espace des noyaux régularisants.

Il faut prendre quelques précautions si  $X^{l} = Y^{m} = R^{n}$ .

On ne doit plus dire semi-régulier en x ou en y.

Dans $\mathfrak{D}_{\mathbb{R}^{n}\times \mathbb{R}^{n}}^{\prime} = \mathfrak{D}^{\prime}\widehat{\otimes}\mathfrak{D}^{\prime}$, le sous-espace $\mathcal{E}\widehat{\otimes}\mathfrak{D}^{\prime}$ est l'espace des noyaux semi-réguliers par rapport à la première variable, ou semi-réguliers à gauche; $\mathfrak{D}^{\prime}\widehat{\otimes}\mathcal{E}$ est l'espace des noyaux semi-réguliers par rapport à la deuxième variable, ou semi-réguliers à droite.

Ils sont échangés par la symétrie s; l'espace des noyaux réguliers et l'espace  $\mathscr{E}\widehat{\otimes}\mathscr{E}$  des noyaux régularisants sont globalement invariants par la symétrie s.

Noyaux semi-compacts, compacts, compactifiants.

$\mathcal{E}_{x}^{\prime}(\mathfrak{D}_{y}^{\prime}) = \mathcal{E}_{x}^{\prime}\widehat{\otimes}\mathfrak{D}_{y}^{\prime} = \mathfrak{L}(\mathcal{E}_{x};\mathfrak{D}_{y}^{\prime})$ est l'espace des noyaux semi-compacts en $x$; la symétrie $s$ le transforme en l'espace $\mathfrak{D}_{y}^{\prime}(\mathcal{E}_{x}^{\prime}) = \mathfrak{D}_{y}^{\prime}\widehat{\otimes}\mathcal{E}_{x}^{\prime} = \mathfrak{L}(\mathfrak{D}_{y};\mathcal{E}_{x}^{\prime})$, qui est encore appelé espace des noyaux semi-compacts en $x$. $\mathfrak{D}_{x}^{\prime}(\mathcal{E}_{y}^{\prime}) = \mathfrak{D}_{x}^{\prime}\widehat{\otimes}\mathcal{E}_{y}^{\prime} = \mathfrak{L}(\mathfrak{D}_{x};\mathcal{E}_{y}^{\prime})$ est l'espace des noyaux semi-compacts en $y$; la symétrie $s$ le transforme en l'espace $\mathcal{E}_{y}^{\prime}(\mathfrak{D}_{x}^{\prime}) = \mathcal{E}_{y}^{\prime}\widehat{\otimes}\mathfrak{D}_{x}^{\prime} = \mathfrak{L}(\mathcal{E}_{y};\mathfrak{D}_{x}^{\prime})$, qui est encore appelé espace des noyaux semi-compacts en $y$. L'intersection de $\mathcal{E}_{x}^{\prime}\widehat{\otimes}\mathfrak{D}_{y}^{\prime}$ et de $\mathfrak{D}_{x}^{\prime}\widehat{\otimes}\mathcal{E}_{y}^{\prime}$, munie de la topologie borne supérieure des topologies induites, est l'espace des noyaux compacts. Il est distinct de $\mathcal{E}_{x}^{\prime}\widehat{\otimes}\mathcal{E}_{y}^{\prime} = \mathcal{E}_{x,y}^{\prime} = \mathfrak{L}(\mathcal{E}_{x};\mathcal{E}_{y}^{\prime})\approx \mathfrak{L}(\mathcal{E}_{y};\mathcal{E}_{x}^{\prime})$, espace des noyaux compactifiants. Autrement dit un noyau compact n'est pas une distribution à support compact sur $\mathrm{X}^{l}\times \mathrm{Y}^{m}$.

PROPOSITION 30. — Pour qu'un noyau $\mathbf{T} \in \mathfrak{D}_{x,y}$ soit semi-compact en $x$, il faut et il suffit que l'intersection du support de $\mathbf{T}$ avec toute bande $\mathbf{X}^l \times \mathbf{K}$, $\mathbf{K}$ compact de $\mathbf{Y}^m$, soit compacte.

La condition est évidemment suffisante; car si l'intersection

précédente est contenue dans H × K, H compact de X$^{t}$, alors, pour $\nu \in \mathcal{D}_{\text{K}}$ et $u \in \mathcal{D}_{\Omega}$, $\Omega = \int_{0}^{t} \text{H}, \text{T}(u \otimes \nu) = 0$, donc T · $\nu$ est dans $\mathcal{E}_{\text{H}}'$, donc dans $\mathcal{E}'$; si $\nu$ converge vers O dans $\mathcal{D}_{\text{K}}$, T · $\nu$ converge vers 0 dans $\mathcal{E}_{\text{H}}'$ donc dans $\mathcal{E}'$; $^{t}\overrightarrow{\text{T}}$ est alors une application linéaire de $\mathcal{D}_{y}$ dans $\mathcal{E}_{x}'$, continue sur chaque $\mathcal{D}_{\text{K}}$ donc continue sur $\mathcal{D}_{y}$, et T ∈ $\mathcal{E}_{x}' \widehat{\otimes} \mathcal{D}_{y}'$.

La condition est aussi nécessaire. Car si $\mathbf{T} \in \mathcal{E}_{x}^{\prime} \widehat{\otimes} \mathfrak{D}_{y}^{\prime}$, $\vec{T}$ est une application linéaire continue de l'espace de Fréchet $\mathfrak{D}_{\mathbf{K}_1}$ ($\mathbf{K}_1$, voisinage compact de K) dans $\mathcal{E}_{x}^{\prime}$, dual de Fréchet; il existe donc un voisinage de 0 dans $\mathfrak{D}_{\mathbf{K}_1}$, d'image bornée dans $\mathcal{E}_{x}^{\prime}(1)$; comme toute partie bornée de $\mathcal{E}_{x}^{\prime}$ est contenue dans un $\mathcal{E}_{\mathbf{H}}^{\prime}$, H compact de $X^l$, $\vec{T}$ applique $\mathfrak{D}_{\mathbf{K}_1}$ dans $\mathcal{E}_{\mathbf{H}}^{\prime}$; on en déduit que $(\mathbf{T} \cdot \nu).u = \mathbf{T}(u \otimes \nu)$ est nul si $u \in \mathfrak{D}_x$ a son support dans $\int H$, et $\nu \in \mathfrak{D}_y$ dans $K_1$; si $\Omega$ est l'intérieur de $K_1$, T est nulle sur $\mathfrak{D}_{\mathfrak{H}} \times \mathfrak{D}_{\Omega}$, donc par continuité sur $\mathfrak{D}_{\mathfrak{H} \times \Omega}(2)$, autrement dit T a un support dont l'intersection avec $X^l \times \Omega$ est contenue dans $H \times \Omega$; l'intersection de ce support avec $X^l \times K$ est donc contenue dans $H \times K$, donc compacte.

Remarque. — La condition énoncée revient à dire que la projection  $(x, y) \to y$  est « propre » ou continue à l'infini quand on la restreint au support de T.

COROLLAIRE. — Si T est un noyau semi-compact en x, à tout compact K de  $Y^{m}$  on peut associer un compact H de  $X^{t}$  tel que, si  $v \in D_{y}$  a son support dans K, T·v ait son support dans H; à tout ouvert borné  $\omega$  de  $Y^{m}$  on peut associer un ouvert borné  $\Omega$  de  $X^{t}$  tel que la distribution induite par u·T sur l'ouvert  $\omega$, pour  $u \in E_{x}$, ne dépende que de la restriction de la fonction u à l'ouvert  $\Omega$.

Il suffit en effet de prendre pour H un compact tel que l'intersection du support de T avec  $X^{t} \times K$  soit contenue dans  $H \times K$ ; et pour  $\Omega$  un voisinage ouvert borné quelconque du compact H associé au compact  $K = \overline{\omega}$ , puisqu'alors, pour  $\nu \in D_{\omega}$ , u est nulle sur un voisinage du support de T.  $\nu$  quand elle est nulle dans  $\Omega : u \cdot T$  est nulle sur  $\omega$  si u est nulle sur  $\Omega$ .

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{D}_{\mathbf{K}_1}\times \varepsilon_x,$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Car T est séparément continue sur $\mathcal{D}_{\mathbf{K}_1} \times \mathcal{E}_x$, donc continue, d'après BOURBAKI [2], proposition 2, page 38.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) SCHWARTZ [4], chapitre iv, § 3, théorème III.</span></small>

PROPOSITION 31. — Si T est un noyau régulier compact, il appartient à $\mathfrak{D}_{x}\widehat{\otimes}\mathfrak{D}_{y}^{\prime},\mathfrak{D}_{x}^{\prime}\widehat{\otimes}\mathfrak{D}_{y},\mathcal{E}_{x}\widehat{\otimes}\mathcal{E}_{y}^{\prime},\mathcal{E}_{x}^{\prime}\widehat{\otimes}\mathcal{E}_{y}$.

Tout d'abord, pour $\nu \in \mathfrak{D}_y$, T·$\nu$ est dans $\mathcal{E}_x$ puisque T est semi-régulier en $x$, et dans $\mathcal{E}_x'$ puisque T est semi-compact en $x$, donc dans leur intersection $\mathfrak{D}_x$; en appliquant alors la proposition 26 à $\mathcal{H}_x = \mathfrak{D}_x$, $\mathfrak{M}_y = \mathfrak{D}_y'$, on voit que T est dans $\mathfrak{D}_x \widehat{\otimes} \mathfrak{D}_y'$. En utilisant alors le fait que T est semi-régulier en $y$ et semicompact en $y$, et en appliquant le raisonnement précédent à $^s\text{T}$, on voit que T est dans $\mathfrak{D}_x' \widehat{\otimes} \mathfrak{D}_y$.

Soit maintenant $\nu \in \mathcal{E}_y$. Comme T est semi-compact en $y$, $\mathbf{T} \cdot \nu$ a un sens; si $\omega$ est un ouvert borné de $X^t$, il existe un ouvert borné $\Omega$ de $\mathbf{Y}^m$ tel que la restriction de $\mathbf{T} \cdot \nu$ à $\omega$ ne dépende que de celle de $\nu$ à $\Omega$ (corollaire de la proposition 30, avec échange des rôles de $x$ et $y$); mais, dans $\Omega$, $\nu$ coïncide avec une fonction $\nu_1 \in \mathcal{D}_y$, donc, dans $\omega$, $\mathbf{T} \cdot \nu$ coïncide avec $\mathbf{T} \cdot \nu_1 \in \mathcal{E}_x$ (puisque T est semi-régulier en $x$); donc $\mathbf{T} \cdot \nu \in \mathcal{E}_x$, et alors la proposition 26 appliquée à $\mathcal{H}_x = \mathcal{E}_x$, $\mathfrak{M}_y = \mathcal{E}_y'$, montre que $\mathbf{T} \in \mathcal{E}_x \widehat{\otimes} \mathcal{E}_y'$.

Le même raisonnement appliqué à  ${}^{s}T$  montre que  $T \in E_{x}^{\prime} \otimes E_{y}$ .

Remarque. — On voit que, dans le cas particulier de $\mathcal{H}_{x}=\mathcal{E}_{x}^{\prime}$, $\mathcal{K}_{y}=\mathcal{E}_{y}$, ou de $\mathcal{H}_{x}=\mathcal{E}_{x}$, $\mathcal{K}_{y}=\mathcal{E}_{y}^{\prime}$, l'intersection de $\mathcal{H}_{x}\in\mathcal{D}_{y}^{\prime}$ et de $\mathcal{D}_{x}^{\prime}\in\mathcal{K}_{y}$ est $\mathcal{H}_{x}\in\mathcal{K}_{y}$.

Remarquons aussi que les propriétés énoncées dans le corollaire de la proposition 30 sont valables, par passage à la limite, pour T régulier compact, même si u et v sont des distributions.

Le noyau $\delta(\hat{x} - \hat{y})$ de l'identité.

Soit  $X^{l}=Y^{m}=R^{n}$ . L'injection canonique de D dans  $D'$  est associée à un noyau  $J(\hat{x},\hat{y})$ , qui doit vérifier

(I, 4; 12)

$J \cdot \nu = \nu, \quad \text{pour} \quad \nu \in \mathfrak{D}; \quad \text{ou} \quad J(u \otimes \nu) = \int_{\mathbb{R}^n} u(x) \nu(x) dx, \; u \in \mathfrak{D}, \; \nu \in \mathfrak{D}.$

On sait qu'un tel noyau est unique. Or le noyau défini par :

$$
(I, 4; 1 3) \quad J (\varphi) = \int_ {\mathbb {R} ^ {n}} \varphi (x, x) d x \quad \text { pour   toute } \quad \varphi \in \mathfrak {D} _ {x, y},
$$

répond à la question.

Soit $\mathcal{H}$ un espace de distributions normal; l'opérateur identique de $\mathcal{D}$ dans $\mathcal{D}'$ se prolonge en l'opérateur identique de $\mathcal{H}$ dans $\mathcal{H}$; donc $J(\hat{x},\hat{y})\in\mathfrak{L}(\mathcal{H};\mathcal{H})\subset\mathcal{H}_{c}^{\prime}\varepsilon\mathcal{H}$ (proposition 13). En

particulier, il appartient à $\mathcal{D} \widehat{\otimes} \mathcal{D}'$, $\mathcal{D}' \widehat{\otimes} \mathcal{D}$, $\mathcal{E} \widehat{\otimes} \mathcal{E}'$, $\mathcal{E}' \widehat{\otimes} \mathcal{E}$, $\mathcal{G} \widehat{\otimes} \mathcal{G}'$, $\mathcal{G}' \widehat{\otimes} \mathcal{G}$.

Donc J( $\hat{x}$ ,  $\hat{y}$ ) est régulier compact. En tant que noyau semi-régulier en x, il est défini par la fonction  $x \to \varepsilon(x) = \delta(\hat{y} - x)$  à valeurs dans  $D_{y}'$ , où  $\varepsilon(a) = \delta(\hat{y} - a)$  est la distribution définie par la masse +1 au point a de  $R^{n}$ , puisqu'on doit avoir

$$
(I, 4; 1 4) \quad \int_ {\mathbf {R} ^ {n}} J (x, y) \nu (y) d y = \nu (x) \quad \text { pour } \quad \nu \in \mathfrak {D} \quad \text { et } \quad x \in \mathbf {R} ^ {n}.
$$

C'est ce qui justifie l'écriture $J(\hat{x}, \hat{y}) = \delta(\hat{y} - \hat{x})$. (Mais une justification complète ne peut résulter que de la théorie du changement de variables pour les distributions: $\delta(\hat{y} - \hat{x})$ est le résultat du changement de variables $z = y - x$ sur la distribution $\delta(\hat{z})$. Voir au numéro suivant, page 104). En tant que noyau semi-régulier en $y$, $\delta(\hat{y} - \hat{x})$ est défini par la fonction $y \to \varepsilon(y)$. Naturellement $\delta(\hat{y} - \hat{x})$ est invariant par la symétrie $s$ (parce que la transposée de l'injection de $\mathcal{D}$ dans $\mathcal{D}'$ est l'injection de $\mathcal{D}$ dans $\mathcal{D}'$), ce qui s'écrit $\delta(\hat{x} - \hat{y}) = \delta(\hat{y} - \hat{x})$.

Remarquons que $y \to \delta(\hat{x} - y)$ est une fonction indéfiniment différentiable à valeurs dans $\mathcal{E}'$, mais que si on la considère comme distribution, elle est à valeurs dans $\mathcal{D}$.

Les noyaux de convolution.

Généralisons les résultats précédents. Soit S une distribution sur  $R^{n}$ . Nous allons définir la distribution  $\mathrm{T}(\hat{x},\hat{y})=\mathrm{S}(\hat{x}-\hat{y})$  sur  $R^{n}\times R^{n}$ .

Nous utiliserons la théorie générale du changement de variables (1). Soit $f(\hat{z})$ une fonction indéfiniment dérivable (ou simplement continue) sur $\mathbb{R}^n$; son image réciproque par l'application $(x, y) \to z = x - y$ de $\mathbb{R}^n \times \mathbb{R}^n$ dans $\mathbb{R}^n$ est $f(\hat{x} - \hat{y})$. On définit ainsi une application linéaire continue $f(\hat{z}) \to f(\hat{x} - \hat{y})$ de $\mathcal{E}_{\mathbb{R}^n}$ dans $\mathcal{E}_{\mathbb{R}^n \times \mathbb{R}^n}$. Soit $\varphi(\hat{x}, \hat{y}) d\hat{x} \wedge d\hat{y}$ une forme différentielle de degré 2n appartenant à $\mathcal{D}_{x,y}$; $f(\hat{x} - \hat{y})$ se définit en tant que courant de degré 0 sur $\mathbb{R}^n \times \mathbb{R}^n$ par

$$
\varphi (\hat {x}, \hat {y}) d \hat {x} \wedge d \hat {y} \rightarrow \iint_ {\mathbb {R} ^ {n} \times \mathbb {R} ^ {n}} f (x - y) \varphi (x, y) d x d y. \tag {I,4;15}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Dès qu'on fait un changement de variables, on doit raisonner sur les courants. Voir de RHAM [1].</span></small>

Effectuons dans cette intégrale le changement de variables $x - y = \xi, y = \eta$; elle devient

$$
\begin{array}{l} \text {(I, 4; 16)} \\ \iint_ {\mathbb {R} ^ {n} \times \mathbb {R} ^ {n}} f (\xi) \varphi (\xi + \eta , \eta) d \xi d \eta = \int_ {\mathbb {R} ^ {n}} f (\xi) d \xi \int_ {\mathbb {R} ^ {n}} \varphi (\xi + \eta , \eta) d \eta . \end{array}
$$

On voit alors que l'opération « image réciproque »:

$$
f (\hat {z}) \rightarrow f (\hat {x} - \hat {y}),
$$

s'étend aux courants de degré 0 sur $\mathbf{R}^{n}$; si $\mathrm{S}(\hat{\boldsymbol{z}})$ est un tel courant, son image réciproque, qu'on notera encore $\mathrm{S}(\hat{\boldsymbol{x}} - \hat{\boldsymbol{y}})$, est le courant de degré 0 sur $\mathbf{R}^{n} \times \mathbf{R}^{n}$, défini par :

$$
\begin{array}{l} \text {(I, 4; 17)} \\ \iint_ {\mathbb {R} ^ {n} \times \mathbb {R} ^ {n}} \mathrm{S} (x - y) \varphi (x, y) d x d y = \int_ {\mathbb {R} ^ {n}} \mathrm{S} (\xi) d \xi \int_ {\mathbb {R} ^ {n}} \varphi (\xi + \eta , \eta) d \eta , \end{array}
$$

et $\mathrm{S}(\hat{\mathbf{z}})\to\mathrm{S}(\hat{\mathbf{x}}-\hat{\mathbf{y}})$ est une opération linéaire continue de $\mathcal{D}_{\mathbb{R}^{n}}^{\prime}$ dans $\mathcal{D}_{\mathbb{R}^{n}\times\mathbb{R}^{n}}^{\prime}$.

Pour éviter les ennuis créés par la différence entre les dimensions n et 2n, nous pourrons aussi donner une autre définition de S( $\hat{x} - \hat{y}$ ). Pour cela nous effectuerons le changement de variables  $\xi = x - y$ ,  $\eta = y$ , indéfiniment différentiable ainsi que son inverse, et conservant les volumes, dx dy = dξ dη, ce qui permet de conserver l'identification des fonctions localement sommables avec des distributions. Formellement S( $\hat{x} - \hat{y}$ ) devient S( $\hat{\xi}$ ), auquel nous donnerons un sens comme distribution en  $\xi$ ,  $\eta$ , en l'identifiant à S( $\hat{\xi}$ )⊗1( $\hat{\eta}$ ). Celà donne pour S( $\hat{x} - \hat{y}$ ) la nouvelle définition suivante :

(I, 4; 18)

$$
\begin{array}{r l} & {\iint_ {\mathbb {R} ^ {n} \times \mathbb {R} ^ {n}} S (x - y) \varphi (x, y) d x d y} \\ & {\qquad = \iint_ {\mathbb {R} ^ {n} \times \mathbb {R} ^ {n}} (S (\xi) \otimes 1 (\eta)) \varphi (\xi + \eta , \eta) d \xi d \eta ,} \end{array}
$$

que l'on peut calculer par deux intégrations simples successives (1):

$$
\begin{array}{l} \text {(I, 4; 19)} \quad \iint_ {\mathbb {R} ^ {n} \times \mathbb {R} ^ {n}} S (x - y) \varphi (x, y) d x d y \\ = \int_ {\mathbb {R} ^ {n}} S (\xi) d \xi \int_ {\mathbb {R} ^ {n}} \varphi (\xi + \eta , \eta) d \eta = \int_ {\mathbb {R} ^ {n}} d \eta \int_ {\mathbb {R} ^ {n}} S (\xi) \varphi (\xi + \eta , \eta) d \xi . \end{array}
$$

On voit donc que cette définition coïncide avec la précédente. Notons qu'on peut aussi définir S( $\hat{x} - \hat{y}$ ) par le change-

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) SCHWARTZ [4], chapitre IV, § 3, théorème IV.</span></small>

ment de variables $\xi' = x$, $\eta' = x - y$; S($\hat{x} - \hat{y}$) devient formellement S($\hat{\eta}'$), qu'on identifie à 1($\hat{\xi}'$) $\otimes$ S($\hat{\eta}'$), ce qui donne la définition :

(I, 4; 20)

$$
\begin{array}{l} \iint_ {\mathbf {R} ^ {n} \times \mathbf {R} ^ {n}} \mathrm{S} (x - y) \varphi (x, y) d x d y \\ = \iint_ {\mathbf {R} ^ {n} \times \mathbf {R} ^ {n}} (1 (\xi^ {\prime}) \otimes \mathrm{S} (\eta^ {\prime})) \varphi (\xi^ {\prime}, \xi^ {\prime} - \eta^ {\prime}) d \xi^ {\prime} d \eta^ {\prime}, \end{array}
$$

calculable également par deux intégrations simples successives :

(I, 4; 21)

$$
\begin{array}{r l} \iint_ {\mathbf {R} ^ {n} \times \mathbf {R} ^ {n}} S (x - y) \varphi (x, y) d x d y \\ & = \int_ {\mathbf {R} ^ {n}} S (\eta^ {\prime}) d \eta^ {\prime} \int_ {\mathbf {R} ^ {n}} \varphi (\xi^ {\prime}, \xi^ {\prime} - \eta^ {\prime}) d \xi^ {\prime} \\ & = \int_ {\mathbf {R} ^ {n}} d \xi^ {\prime} \int_ {\mathbf {R} ^ {n}} S (\eta^ {\prime}) \varphi (\xi^ {\prime}, \xi^ {\prime} - \eta^ {\prime}) d \eta^ {\prime}. \end{array}
$$

(Les deux dernières définitions de S( $\hat{x} - \hat{y}$ ) donnent le même résultat, car, en posant  $\xi + \eta = \xi'$  dans la dernière intégrale du  $2^{e}$  membre de (I, 4; 19), on obtient une expression de  $\iint\mathrm{S}(x - y)\varphi(x, y)dx dy$ , qui n'est autre, au changement près de  $\xi$  en  $\eta'$ , que celle du  $2^{e}$  membre de (I, 4; 21).

Soit D un opérateur différentiel à coefficients constants, D son symétrique (transformé par la symétrie  $x \rightarrow -x$  de  $\mathbf{R}^{n}(^{1})$ ).

En appliquant la formule (I, 4; 18), on a

(I, 4; 22)

$$
\begin{array}{r l} & {\iint \mathrm{D} _ {x} (\mathrm{S} (x - y)) \varphi (x, y) d x d y} \\ & {= \iint \mathrm{S} (x - y) \check {\mathrm{D}} _ {x} \varphi (x, y) d x d y} \\ & {= \iint (\mathrm{S} (\xi) \otimes 1 (\eta)) (\check {\mathrm{D}} _ {x} \varphi) (\xi + \eta , \eta) d \xi d \eta} \\ & {= \iint (\mathrm{S} (\xi) \otimes 1 (\eta)) \check {\mathrm{D}} _ {\xi} (\varphi (\xi + \eta , \eta)) d \xi d \eta} \\ & {= \iint (\mathrm{DS} (\xi) \otimes 1 (\eta)) \varphi (\xi + \eta , \eta) d \xi d \eta} \\ & {= \iint (\mathrm{DS}) (x - y) \varphi (x, y) d x d y,} \end{array}
$$

d'où

(I, 4; 23)

$$
\mathrm{D} _ {x} (\mathrm{S} (x - y)) = (\mathrm{DS}) (x - y).
$$

En appliquant au contraire la définition (I, 4; 20), on a, de la même manière :

(I, 4; 24)

$$
\mathrm{D} _ {y} (\mathrm{S} (x - y)) = (\check {\mathrm{DS}}) (x - y)
$$

(parche qu'ici (D,φ)(ξ',ξ'-η') = Dη(φ(ξ',ξ'-η'))).

(1) Schwartz [5], formule (VI, 4; 7), page 23.

Ces formules sont d'ailleurs bien connues en théorie du changement de variables.

Le noyau $\mathrm{S}(\hat{x}-\hat{y})=\mathrm{T}(\hat{x},\hat{y})$, ainsi défini, est le noyau de la convolution: $\nu\to\mathrm{T}\cdot\nu=\mathrm{S}*\nu$, ou $u\to u\cdot\mathrm{T}=u*\check{\mathrm{S}}$, car, pour $u$ et $\nu\in\mathfrak{D}$, (I, 4; 21) donne:

(I, 4; 25)

$$
\begin{array}{r l} \iint \mathrm{S} (x - y) u (x) v (y) d x d y \\ & = \int u (\xi^ {\prime}) d \xi^ {\prime} \int \mathrm{S} (\eta^ {\prime}) v (\xi^ {\prime} - \eta^ {\prime}) d \eta^ {\prime}, \end{array}
$$

de sorte que

$$
(\mathrm{I}, 4; 2 6) \quad (\mathrm{T} \cdot \nu) (\hat {x}) = \int \mathrm{S} (t) \nu (\hat {x} - t) d t = (\mathrm{S} * \nu) (\hat {x}),
$$

l'égalité étant d'ailleurs valable aussi si l'on remplace $\hat{x}$ par $x$ fixé dans $\mathbb{R}^n$. Le noyau $\mathrm{S}(\hat{x}-\hat{y})$ est en effet régulier, à cause des propriétés connues de la convolution, mais le calcul (1, 4; 25), par le théorème de Fubini, montre d'avance que l'intégrale du $2^{\mathrm{e}}$ membre de (1, 4; 25) est une fonction de $\xi'$ indéfiniment différentiable. Pour $x$ fixé dans $\mathbb{R}^n$, la distribution $\mathrm{S}(x-\hat{y})$ n'est autre que la translatée $\tau(x)(\mathrm{S}(-\hat{y}))=\tau(x)(\check{\mathrm{S}}(\hat{y}))$, tandis que, pour $y$ fixé, la distribution $\mathrm{S}(\hat{x}-y)$ est $\tau(y)$$\mathrm{S}(\hat{x})$ (ce qui justifie encore l'écriture $\mathrm{S}(\hat{x}-\hat{y})$). En effet, $\mathrm{S}(x-\hat{y})$ doit être l'image $u\cdot T$ de la distribution $u$ constituée par la masse + 1 au point $x$, c'est donc bien $\tau(x)(\check{\mathrm{S}}(\hat{y}))$. La formule (I, 4; 4) s'écrit alors

$$
(\mathrm{I}, 4; 2 7) (\mathrm{S} * \nu) (x) = \int_ {\mathbb {R} ^ {n}} \mathrm{S} (x - y) \nu (y) d y = \int_ {\mathbb {R} ^ {n}} \mathrm{S} (t) \nu (x - t) d t,
$$

écriture formelle classique de la convolution.

Si S est à support compact,  $\mathrm{S}(\hat{x}-\hat{y})$  est en outre un noyau compact, comme il résulte des propriétés de la convolution, ou de la proposition 30 (le support de  $\mathrm{S}(\check{x}-\hat{y})$  étant l'ensemble des couples  $(x,y)$  vérifiant  $x-y\in L$ , L=support de S); si S est une fonction indéfiniment différentiable,  $\mathrm{S}(\hat{x}-\hat{y})$  est un noyau régularisant.

Noyaux des opérateurs différentiels; opérateurs de caractère local.

Nous dirons qu'une application linéaire continue $\nu\to\mathbf{T}$. $\nu$ de $\mathcal{D}_{\mathbf{R}^{n}}$ dans $\mathcal{D}_{\mathbf{R}^{n}}^{\prime}$ est de caractère local, si, quel que soit l'ou-

vert $\Omega$ de $R^{n}$, la distribution induite par T. $\nu$ dans $\Omega$ ne dépend que de la fonction induite par $\nu$ dans $\Omega$. Celà revient aussi à dire que le support de T. $\nu$ est contenu dans le support de $\nu$, ou que T ($u \otimes \nu$) est nul si les supports de $u$ et de $\nu$ sont sans point commun.

Soient $a$ et $b$ deux points de $\mathbb{R}^{n}$, distincts; soient A et B des ouverts contenant respectivement $a$ et $b$, et sans point commun. Alors T est nulle sur $\mathfrak{D}_{\mathbf{A}} \otimes \mathfrak{D}_{\mathbf{B}}$, et, par passage à la limite, sur $\mathfrak{D}_{\mathbf{A} \times \mathbf{B}}(1)$; son support dans $\mathbb{R}^{n} \times \mathbb{R}^{n}$ ne contient donc pas de point $(a, b)$, il est donc contenu dans la diagonale $x = y$ de $\mathbb{R}^{n} \times \mathbb{R}^{n}$ (ce qui entraîne que T soit un noyau compact, d'après la proposition 30). Réciproquement tout noyau ayant son support contenu dans la diagonale est de caractère local, car alors, si $u$ et $\nu$ ont des supports sans point commun, $u \otimes \nu$ a son support sans point commun avec la diagonale, et $\mathrm{T}(u \otimes \nu)$ est bien nulle. Cherchons alors à caractériser les distributions T dont le support est contenu dans la diagonale. Les directions des axes $Oy_{1}, Oy_{2}, \ldots Oy_{n}$, forment un système libre de directions transversales à la diagonale, et les dérivations partielles suivant ces directions commutent. Alors T s'exprime d'une manière unique comme somme (localement finie)

$$
(\mathrm{I}, 4; 2 8)
$$

$$
\mathbf {T} (\hat {x}, \hat {y}) = \sum_ {q} (- 1) ^ {| q |} \mathbf {D} _ {y} ^ {q} \overline {{\mathbf {T}}} _ {q} (\hat {x}, \hat {y}),
$$

ou $\overline{\mathbf{T}}_{q}(\hat{x},\hat{y})$ est l'extension à $\mathbf{R}^{n}\times\mathbf{R}^{n}$ d'une distribution $\mathbf{T}_{q}$ définie sur la diagonale (2). Mais, sur la diagonale, on peut prendre comme système de coordonnées $x_{1}, x_{2}, \ldots x_{n}$; une distribution $\mathbf{T}_{q}$ sur la diagonale peut donc être définie par une distribution $\mathbf{A}_{q}(\hat{x})$ sur $\mathbf{R}^{n}$, avec, pour $\varphi\in\mathfrak{D}_{\mathbf{R}^{n}\times\mathbf{R}^{n}}$:

$$
(I, 4; 2 9)
$$

$$
\overline {{{{\mathbf {T}}}}} _ {q} (\varphi) = \int_ {\mathbb {R} ^ {n}} \mathrm{A} _ {q} (x) \varphi (x, x) d x.
$$

On aura finalement

(I, 4; 30)

$$
\mathrm{T} (u \otimes v) = \sum_ {q} \int_ {\mathbb {R} ^ {n}} \mathrm{A} _ {q} (x) u (x) \mathrm{D} ^ {q} v (x) d x,
$$

(1) Schwartz [4], chapitre iv, § 3, théorème III.

(2) SCHWARTZ [4], chapitre III, § 10, théorème XXXVII.

donc T·ν est la distribution  $\sum_{q}A_{q}D^{q}\nu$ , et l'opérateur  $\nu\to T\cdot\nu$  est l'opérateur différentiel:

$$
(\mathbf {I}, 4; 3 \mathbf {1})
$$

$$
\mathbf {D} = \sum_ {q} \mathbf {A} _ {q} \mathbf {D} ^ {q},
$$

à coefficients distributions  $A_{q}$ . Cet opérateur différentiel est éventuellement d'ordre infini, mais fini sur tout ouvert borné de  $R^{n}$ . Réciproquement, tout opérateur différentiel d'ordre localement fini à coefficients distributions est évidemment de caractère local.

Si T définit un opérateur de caractère local, il en est de même de $^s\mathrm{T}$, puisque cela s'exprime par une condition symétrique (avoir son support contenu dans la diagonale de $\mathbf{R}^n\times \mathbf{R}^n$).

Si T a la décomposition (I, 4; 28) avec (I, 4; 29), on a

$$
(\mathrm{I}, 4; 3 2) \quad {} ^ {s} \mathrm{T} (\hat {x}, \hat {y}) = \sum_ {q} (- 1) ^ {| q |} \mathrm{D} _ {x} ^ {q} \overline {{\mathrm{T}}} _ {q} (\hat {x}, \hat {y}),
$$

$T_{q}(\hat{x}, \hat{y})$ étant symétrique d'après (I, 4; 29).

On a alors

(I, 4; 33)

$$
\begin{array}{r l} ^ {s} \mathbf {T} (\nu \otimes u) & = \mathbf {T} (u \otimes \nu) \\ & = \sum_ {q} \int_ {\mathbb {R} ^ {n}} \mathrm{A} _ {q} (x) u (x) \mathrm{D} ^ {q} \nu (x) d x \\ & = \sum_ {q} (- 1) ^ {| q |} \int_ {\mathbb {R} ^ {n}} \mathrm{D} ^ {q} (\mathrm{A} _ {q} (x) u (x)) \nu (x) d x, \end{array}
$$

de sorte que  $^{s}$ T définit l'opérateur

(I, 4; 34)

$$
u \rightarrow {} ^ {s} \mathbf {T} \cdot u = u \cdot \mathbf {T} = \sum_ {q} (- 1) ^ {| q |} \mathrm{D} ^ {q} (\mathrm{A} _ {q} u),
$$

opérateur 'D qui est bien le transposé de l'opérateur différentiel D de (I, 4; 31).

Supposons maintenant que T soit en outre semi-régulier à gauche. Comme il est semi-compact à droite, il appartient à $\mathcal{E} \otimes \mathcal{E}'$ (voir remarque, page 102). Alors, pour toute $\nu \in \mathcal{E}$, T.v doit être dans $\mathcal{E}$. Montrons que tous les coefficients $A_q$ appartiennent à $\mathcal{E}$ (ce qui entraînera que T soit régulier compact); la réciproque est évidente. Supposons-le démontré pour tous les $a < a_{\circ}$ et montrons-le pour $a$. Prenons $a = \frac{x^{q_0}}{x^{\circ}}$.

$q < q_{0}$, et montrons-le pour $q_{0}$. Prenons $\nu = \frac{x^{q_{0}}}{(q_{0})!}$.

Alors  $D^{q}\nu$  est nul, sauf pour  $q \leqslant q_{0}$ ; puisque les  $A_{q}$  sont dans E pour  $q < q_{0}$ , que T· $\nu$  est dans E, et que  $D^{q_{0}}\nu = 1$ , on a bien  $A_{q_{0}} \in E$ , c.q.f.d.

Si nous avions supposé T semi-régulier à droite, le même raisonnement sur 'T aurait abouti à la même conclusion.

Nous pouvons rassembler les résultats obtenus :

PROPOSITION 32. — Il y a identité entre les opérateurs linéaires continus de caractère local de D dans D' (resp. dans E), les opérateurs linéaires continus de D dans D' (resp. dans E) définis par un noyau ayant un support contenu dans la diagonale de R^n × R^n, et les opérateurs différentiels d'ordre localement fini à coefficients distributions (resp. à coefficients fonctions indéfiniment dérivables).

Remarques. — 1° Les opérateurs différentiels d'ordre 0 sont les multiplications $\nu \to A\nu$, $A \in \mathfrak{D}'$. Le noyau d'une telle opération est $T(\hat{x}, \hat{y})$ défini par

(I, 4; 35)

$$
\mathrm{T} (\varphi) = \int_ {\mathbb {R} ^ {n}} \mathrm{A} (x) \varphi (x, x) d x.
$$

On peut l'écrire

(I, 4; 36)

$$
\mathbf {T} (\hat {x}, \hat {y}) = \mathbf {A} (\hat {x}) \delta (\hat {x} - \hat {y}) = \mathbf {A} (\hat {y}) \delta (\hat {x} - \hat {y}).
$$

De tels produits n'ont pas a priori un sens; mais il y a diverses manières de leur en donner un, qui est bien celui qu'on attend. On remarquera, par exemple, que, si l'on pose $x = \xi'$, $x - y = \eta'$, comme page 105, A($\hat{x}$)$\delta(\hat{x} - \hat{y})$ devient formellement A($\hat{\xi'}$)$\delta(\hat{\eta}')$, qu'on peut définir comme le produit tensoriel A($\hat{\xi'}$)$\otimes\delta(\hat{\eta}')$. Avec cette définition, on a bien

(I, 4; 37)

$$
\begin{array}{l} \iint_ {\mathbf {R} ^ {n} \times \mathbf {R} ^ {n}} \mathbf {A} (x) \delta (x - y) \varphi (x, y) d x d y \\ = \iint_ {\mathbf {R} ^ {n} \times \mathbf {R} ^ {n}} (\mathbf {A} (\xi^ {\prime}) \otimes \delta (\eta^ {\prime})) \varphi (\xi^ {\prime}, \xi^ {\prime} - \eta^ {\prime}) d \xi^ {\prime} d \eta^ {\prime} \\ = \int_ {\mathbf {R} ^ {n}} \mathbf {A} (\xi^ {\prime}) d \xi^ {\prime} \int_ {\mathbf {R} ^ {n}} \delta (\eta^ {\prime}) \varphi (\xi^ {\prime}, \xi^ {\prime} - \eta^ {\prime}) d \eta^ {\prime} \\ = \int_ {\mathbf {R} ^ {n}} \mathbf {A} (\xi^ {\prime}) \varphi (\xi^ {\prime}, \xi^ {\prime}) d \xi^ {\prime}, \end{array}
$$

qui coïncide avec (I, 4; 35).

De la même manière, le noyau T de (I, 4; 28) peut s'écrire

(I, 4; 37)

$$
\mathrm{T} (\hat {x}, \hat {y}) = \sum_ {q} \mathrm{A} _ {q} (\hat {x}) \mathrm{D} _ {x} ^ {q} \hat {\mathcal {O}} (\hat {x} - \hat {y}).
$$

En effet, avec la définition ci-dessus, (I, 4; 37) signifie, compte tenu de (I, 4; 23):

$$
\begin{array}{r l} & {\mathrm{(I,4;38)}} \\ & {\quad \iint_ {\mathbf {R} ^ {n} \times \mathbf {R} ^ {n}} \mathbf {T} (x, y) \varphi (x, y) d x d y} \\ & {= \iint_ {\mathbf {R} ^ {n} \times \mathbf {R} ^ {n}} \Big (\sum_ {q} \mathbf {A} _ {q} (\xi^ {\prime}) \otimes \mathbf {D} ^ {q} \delta (\eta^ {\prime}) \Big) \varphi (\xi^ {\prime}, \xi^ {\prime} - \eta^ {\prime}) d \xi^ {\prime} d \eta^ {\prime}} \\ & {= \sum_ {q} \int_ {\mathbf {R} ^ {n}} \mathbf {A} _ {q} (\xi^ {\prime}) d \xi^ {\prime} \int_ {\mathbf {R} ^ {n}} (\mathbf {D} ^ {q} \delta (\eta^ {\prime})) \varphi (\xi^ {\prime}, \xi^ {\prime} - \eta^ {\prime}) d \eta^ {\prime}} \\ & {= \sum_ {q} \int_ {\mathbf {R} ^ {n}} \mathbf {A} _ {q} (\xi^ {\prime}) d \xi^ {\prime} \int_ {\mathbf {R} ^ {n}} (- 1) ^ {| q |} \delta (\eta^ {\prime}) \mathbf {D} _ {\eta^ {\prime}} ^ {q} (\varphi (\xi^ {\prime}, \xi^ {\prime} - \eta^ {\prime})) d \eta^ {\prime}} \\ & {= \sum_ {q} \int_ {\mathbf {R} ^ {n}} \mathbf {A} _ {q} (\xi^ {\prime}) d \xi^ {\prime} \int_ {\mathbf {R} ^ {n}} \delta (\eta^ {\prime}) (\mathbf {D} _ {\gamma} ^ {q} \varphi) (\xi^ {\prime}, \xi^ {\prime} - \eta^ {\prime}) d \eta^ {\prime (^ {1})}} \\ & {= \int_ {\mathbf {R} ^ {n}} \sum_ {q} \mathbf {A} _ {q} (\xi^ {\prime}) (\mathbf {D} _ {\gamma} ^ {q} \varphi) (\xi^ {\prime}, \xi^ {\prime}) d \xi^ {\prime},} \end{array}
$$

ce qui coïncide bien avec la définition de T par (I, 4; 28), compte tenu de (I, 4; 29).

On remarque aussi que le noyau T associé à l'opérateur différentiel D s'écrit

$$
\mathrm{T} (\hat {x}, \hat {y}) = \mathrm{D} _ {x} \delta (\hat {x} - \hat {y}). \tag {I,4,39}
$$

Mais encore faut-il donner un sens à cette expression. On considère $\delta(\hat{x} - \hat{y})$ comme un élément de $\mathcal{E} \otimes \mathfrak{D}'$ (noyau semi-régulier à gauche), et D comme un opérateur linéaire continu de $\mathcal{E}$ dans $\mathfrak{D}'$, de sorte que le second membre de (I, 4; 39), si l'on identifie $D_x$ à $D \otimes I$, définit un élément de $\mathfrak{D}' \otimes \mathfrak{D}'$ qui n'est autre que T; cela revient en effet à écrire (d'après la remarque $1^0$ de la page 35, avec $u_1 = D$, $u_2 = I$, $^\prime X =$ injection identique de $\mathfrak{D}$ dans $\mathcal{E}$ représentée par le noyau $\delta(\hat{x} - \hat{y})$, $L_1 = \mathcal{E}$, $L_2 = \mathfrak{D}'$, $M_1 = \mathfrak{D}'$, $M_2 = \mathfrak{D}'$) que D est identique D·I, I étant l'identité.
De la même manière, on peut écrire

$$
\mathrm{T} (\hat {x}, \hat {y}) = \sum_ {q} (- 1) ^ {| q |} \mathrm{D} _ {\hat {y}} ^ {q} (\mathrm{A} _ {q} (\hat {y}) \delta (\hat {x} - \hat {y})), \tag {I,4;40}
$$

qui n'est autre que (I, 4; 28), compte tenu de (I, 4; 36). Cela revient à écrire

$$
(\mathrm{I}, 4; 4 1)
$$

$$
\mathrm{T} (\hat {x}, \hat {y}) = ^ {t} \mathrm{D} _ {\gamma} \delta (\hat {x} - \hat {y}),
$$

où l'on considère ici $\delta(\hat{x} - \hat{y})$ comme un élément de $\mathfrak{D}' \otimes \mathfrak{E}$

(1) L'expression  $(\mathrm{D}_{y}^{q}\varphi)(a,b)$  veut dire: la valeur pour x=a, y=b, de la dérivée partielle  $\mathrm{D}_{y}^{q}\left(\varphi(\hat{x},\hat{y})\right)$ .

(semi-régulier à droite), $^{t}$D comme opérateur linéaire continu de $\mathcal{E}$ dans $\mathcal{D}'$, et $^{t}$D$_{y}$ comme représentant I $\otimes$$^{t}$D.

Pour  $^{s}$ T, on a les formules :

$$
\begin{array}{r l} (\mathrm{I}, 4; 4 2) ^ {s} \mathrm{T} (\hat {x}, \hat {y}) & = \sum_ {q} \mathrm{A} _ {q} (\hat {y}) \mathrm{D} _ {y} ^ {q} \delta (\hat {x} - \hat {y}) \\ & = \mathrm{D} _ {y} \delta (\hat {x} - \hat {y}) = \sum_ {q} (- 1) ^ {| q |} \mathrm{D} _ {x} ^ {q} (\mathrm{A} _ {q} (\hat {x}) \delta (\hat {x} - \hat {y})) \\ & = ^ {t} \mathrm{D} _ {x} \delta (\hat {x} - \hat {y}). \end{array}
$$

Remarquons que (I, 4; 39) et (I, 4; 41) donnent

$$
(\mathrm{I}, 4; 4 3) \quad \mathrm{D} _ {x} \delta (\hat {x} - \hat {y}) = ^ {\prime} \mathrm{D} _ {y} \delta (\hat {x} - \hat {y});
$$

cette relation caractérise d'ailleurs 'D à partir de D, car elle s'écrit directement

$$
(\mathrm{I}, 4; 4 4) \quad \int_ {\mathbb {R} ^ {n}} ^ {t} \mathrm{D} u (x) \nu (x) d x = \int_ {\mathbb {R} ^ {n}} u (x) \mathrm{D} \nu (x) d x,
$$

pour $u \in \mathcal{D}$, $\nu \in \mathcal{D}$.

Remarquons aussi qu'on peut généraliser les formules (I, 4; 39) et (I, 4; 41). Si $S \in \mathcal{E}_x \otimes \mathcal{D}_y'$ définit l'opération $\vec{S} : \nu \to S \cdot \nu$, de $\mathcal{D}_y$ dans $\mathcal{E}_x$, l'opération $D \circ \vec{S}$ de $\mathcal{D}_y$ dans $\mathcal{D}_x'$ est définie par un noyau qu'on peut écrire $D_x S(\hat{x}, \hat{y}) = (D \otimes I) S(\hat{x}, \hat{y})$; si $S \in \mathcal{D}_x' \otimes \mathcal{E}_y$ définit l'opération $\vec{S}$ de $\mathcal{E}_y'$ dans $\mathcal{E}_x'$, l'opération $\vec{S} \circ D$ de $\mathcal{D}_y$ dans $\mathcal{D}_x'$ est définie par un noyau qu'on peut écrire $^t D_y S(\hat{x}, \hat{y}) = (I \otimes ^t D) S(\hat{x}, \hat{y})$. On obtient toujours ces formules en appliquant la remarque 1, page 35. Elles sont valables même si $X^t$ et $Y^m$ sont distincts; elles s'écrivent:

$$
\begin{array}{l l} \text {(I, 4; 45)} & \mathrm{D} \int_ {\mathbb {Y} ^ {m}} \mathrm{S} (\hat {x}, y) \varphi (y) d y = \int_ {\mathbb {Y} ^ {m}} \mathrm{D} _ {x} \mathrm{S} (\hat {x}, y) \varphi (y) d y, \\ \text {(I, 4; 46)} & \int_ {\mathbb {Y} ^ {m}} \mathrm{S} (\hat {x}, y) \mathrm{D} \varphi (y) d y = \int_ {\mathbb {Y} ^ {m}} ^ {t} \mathrm{D} _ {y} \mathrm{S} (\hat {x}, y) \varphi (y) d y; \end{array}
$$

le lecteur justifiera aisément cette écriture.

Ces formules sont valables, si D est à coefficients indéfiniment dérivables, pour  $S \in D_{x,y}^{\prime}$  quelconque, et  $D_{x}$$S(\hat{x}, \hat{y})$  ainsi que  $^{t}D_{y}S(\hat{x}, \hat{y})$  ont alors leur signification élémentaire usuelle.

Noyaux fonctions.

Nous allons introduire des espaces fonctionnels nouveaux. $\mathcal{L}^1$ sera l'espace des classes de fonctions localement sommables sur $\mathbf{R}^n$; il sera muni de la topologie définie par la famille des

semi-normes  $N_{K}$ :  $f \to \int_{K} |f(x)| dx$ , où K parcourt la famille des parties compactes de  $R^{n}$ . Son dual sera appelé  $K^{\infty}$ : c'est l'espace des classes de fonctions bornées à support compact; nous le munirons de la topologie  $(\mathcal{L}^{1})_{c}^{\prime}$  de la convergence uniforme sur les parties compactes de  $L^{1}$ . Alors  $L^{1}$  est un espace de Fréchet,  $K^{\infty}$  est localement convexe complet (¹);  $L^{1}$ , et par conséquent  $K^{\infty}$ , sont strictement normaux, et ont la propriété d'approximation par troncature et par régularisation, et la propriété d'approximation stricte (Préliminaires, propositions 3 et 4);  $K^{\infty}$  à la propriété  $\varepsilon$  (proposition 14).

PROPOSITION 33. — Soit T une fonction localement sommable sur $\mathbf{X}^{l}\times\mathbf{Y}^{m}$. Alors $\mathbf{T}\in\mathcal{L}_{x}^{1}\otimes_{\pi}\mathcal{L}_{y}^{1}$, et $^{t}\vec{\mathbf{T}}$ se prolonge en une application linéaire continue de $\mathfrak{K}_{y}^{\infty}$ dans $\mathcal{L}_{x}^{1}$; pour toute $\nu\in\mathfrak{K}_{y}^{\infty}$, $\mathbf{T}\cdot\nu\in\mathcal{L}_{x}^{1}$ est donnée, pour presque toutes les valeurs de $x$, par l'intégrale :

$$
(\mathrm{I}, 4; 4 7) \quad (\mathrm{T} \cdot \nu) (x) = \int_ {\mathbf {Y} ^ {m}} \mathrm{T} (x, y) \nu (y) d y.
$$

On sait en effet $\mathfrak{L}_{x,y}^{1} = \mathfrak{L}_{x}^{1}\widehat{\otimes}_{\pi}\mathfrak{L}_{y}^{1}$.

Comme $\mathfrak{L}^1$ a lapropriété d'approximation et qu'il est complet, $\mathfrak{L}_x^1\otimes_\pi\mathfrak{L}_y^1$ est un sous-espace de $\mathfrak{L}_x^1\otimes_\varepsilon\mathfrak{L}_y^1$ ($^3$) = $\mathfrak{L}_x^1\varepsilon\mathfrak{L}_y^1\approx\mathfrak{L}_\varepsilon(\mathfrak{K}_y^\infty;\mathfrak{L}_x^1)$. Alors, pour $T\in\mathfrak{L}_{x,y}^1$, nous appellerons toujours $\nu\to T\cdot\nu$ le prolongement à $\mathfrak{N}_y^\infty$ de $\vec{T}\in\mathfrak{L}(\mathcal{D}_y;\mathcal{D}_x')$.

Soit maintenant $\nu\in\mathcal{K}_{y}^{\infty}$. La fonction T($\hat{x},\hat{y}$) $\nu(\hat{y})$ est sommable sur H $\times$ Y$^{m}$, où H est un compact quelconque de X$^{l}$; d'après le théorème de Fubini,

$$
(\mathrm{I}, 4; 4 8)
$$

$$
(\mathbf {T}: \nu) (x) = \int_ {\mathbf {Y} ^ {m}} \mathbf {T} (x, y) \nu (y) d y
$$

existe pour presque toutes les valeurs de $x$, et représente une fonction de $x$ localement sommable. Alors $\nu \to T: \nu$ est une application linéaire de $\mathfrak{K}_{y}^{\infty}$ dans $\mathfrak{L}_{x}^{1}$; nous devons montrer que $T: \nu = T \cdot \nu$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">71, $\mathcal{L}_x^1\otimes_\pi \mathcal{L}_y^1$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{L}_{x,y}^{1}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{X}^l$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{L}_{y}^{1}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) D'après GROTHENDIECK [4], page 71, $\mathcal{L}_{x}^{1}\otimes_{\pi}\mathcal{L}_{y}^{1}$ est identique à $\mathcal{L}_{x}^{1}(\mathcal{L}_{y}^{1})$, espace des classes de fonctions localement sommables sur $X^{l}$ à valeurs dans $\mathcal{L}_{y}^{l}$; mais $\mathcal{L}_{x}^{l}(\mathcal{L}_{y}^{l})$ et $\mathcal{L}_{x,y}^{l}$ sont tous deux complets, et induisent sur le sous-espace dense $\mathcal{L}_{x}^{l}\otimes\mathcal{L}_{y}^{l}$ la même topologie, donc sont identiques.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{L}_x^1\otimes \mathcal{L}_y^1$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) DIEUDONNÉ-SCHWARTZ [1], proposition 12, page 82.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{L}_x^1$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{L}_{\mathbf{H}}^{1}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(3) GROTHENDIECK [4], § 5, n° 1, lemme 19, page 169: $\mathcal{L}_{x}^{1}$ et $\mathcal{L}_{y}^{1}$ sont des espaces complets, et $\mathcal{L}_{x}^{1}$ est limite projective des espaces de Banach $\mathcal{L}_{H}^{1}$ (H compact de $X^{l}$), qui ont la propriété d'approximation.</span></small>

Comme T·ν est définie par prolongement, la forme bilinéaire A : (u, ν) → u. (T·ν) est la seule forme bilinéaire séparément continue sur  $\mathfrak{K}_{x}^{\infty} \times \mathfrak{K}_{y}^{\infty}$  qui coïncide avec

$$
(u, \nu) \rightarrow \mathrm{T}. (u \otimes \nu) = \iint_ {\mathbf {X} ^ {l} \times \mathbf {Y} ^ {m}} \mathrm{T} (x, y) u (x) \nu (y) d x d y
$$

sur $\mathfrak{D}_{x} \times \mathfrak{D}_{y}$. Or d'une part, pour toute $u \in \mathcal{K}_{x}^{\infty}$ et toute $\nu \in \mathcal{K}_{y}^{\infty}$, on a, d'après Fubini,

(I, 4; 49)

$$
\begin{array}{r l} u _ {\bullet} (\mathbf {T}: \nu) & = \int_ {\mathbf {X} ^ {l}} u (x) d x \int_ {\mathbf {Y} ^ {m}} \mathbf {T} (x, y) \nu (y) d y \\ & = \iint_ {\mathbf {X} ^ {l} \times \mathbf {Y} ^ {m}} \mathbf {T} (x, y) u (x) \nu (y) d x d y \\ & = \int_ {\mathbf {Y} ^ {m}} \nu (y) d y \int_ {\mathbf {X} ^ {l}} \mathbf {T} (x, y) u (x) d x = \nu_ {\bullet} (u: \mathbf {T}), \end{array}
$$

donc B : (u, v) → u. (T : v) coïncide avec A sur $\mathfrak{D}_x \times \mathfrak{D}_y$; d'autre part, cette forme bilinéaire B est séparément continue sur $\mathfrak{K}_x^\infty \times \mathfrak{K}_y^\infty$, car, pour v ∈ $\mathfrak{K}_y^\infty$, T : v est dans $\mathfrak{L}_x^1$, et, pour toute u ∈ $\mathfrak{K}_x^\infty$, u : T est dans $\mathfrak{L}_y^1$. On a donc bien A = B, et T : v = T · v.

Remarque. — Supposons que  $T \in L_{x,y}^{1}$  ait en outre la propriété suivante:

T est semi-compact en y; et, pour tout compact H de  $X^{l}$ ,  $\int_{H}|T(x,y)|dx$  est borné pour  $y \in Y^{m}$ .

Alors $\vec{T}$ est dans $\mathfrak{L}_{x}^{\prime}\in\mathfrak{D}_{y}^{\prime}$, et, pour toute $u\in\mathfrak{K}_{x}^{\infty}$, $\vec{T}(u)=u\cdot T$ est dans $\mathfrak{K}_{y}^{\infty}$: en effet $u\cdot T$ est dans $\mathfrak{L}_{y}^{\prime}$, a un support compact, et, si H est le support de $u$:

$$
(\mathrm{I}, 4; 5 0) \quad | (u \cdot \mathrm{T}) (y) | \leqslant \| u (x) \| _ {\mathrm{L} ^ {\infty}} \sup _ {y \in \mathbf {Y} ^ {m}} \int_ {\mathrm{H}} | \mathrm{T} (x, y) | d x.
$$

Alors la proposition 26 (où les rôles de $x$ et $y$ sont échangés, et où l'on remplace $\mathcal{K}_{y}$ par $\mathscr{L}_{x}^{1}$, et $\mathcal{H}_{x}$ par $\mathcal{K}_{y}^{\infty}$, ce qui est permis puisque $\mathcal{K}^{\infty}$ vérifie la propriété $\varepsilon$) montre que

$$
\mathbf {T} \in \mathfrak {L} _ {\boldsymbol {x}} ^ {1} \varepsilon \mathfrak {K} _ {\boldsymbol {y}} ^ {\infty}.
$$

$\vec{T}$ est donc continue de $\mathfrak{K}_{x}^{\infty}$ dans $\mathfrak{K}_{y}^{\infty}$. En outre $\vec{t}\vec{T}$ est une application continue de $\mathfrak{L}_{y}^{1}$ dans $\mathfrak{L}_{x}^{1}$.

Cette application peut toujours s'écrire $\nu\to\mathrm{T}$: $\nu$, avec $(\mathrm{T}:\nu)(x)=\int_{\mathbf{Y}^{m}}\mathrm{T}(x,y)\nu(y)dy$. Soit en effet H un compact de $\mathbf{X}^{l}$; le support de T coupe $\mathrm{H}\times\mathbf{Y}^{m}$ suivant un compact $\mathrm{H}\times\mathrm{K}$, K compact de $\mathbf{Y}^{m}$; alors $\mathrm{T}(\hat{x},\hat{y})\nu(\hat{y})$ est mesurable, et

$\int_{\mathbf{K}} dy \int_{\mathbf{H}} |\mathbf{T}(x, y) \nu(y)| dx < +\infty$, donc $\mathbf{T}(\hat{x}, \hat{y}) \nu(\hat{y}) \in \mathbf{L}_{\mathbf{H} \times \mathbf{Y}^m}^1$; alors $\int_{\mathbf{Y}^m} \mathbf{T}(x, y) \nu(y) dy$ a un sens pour presque toutes les valeurs de $x$ et représente une fonction $\mathbf{T}: \nu \in \mathcal{L}_x^1$; de plus

$$
(\mathrm{I}, 4; 5 1) \quad \int_ {\mathbf {H}} | (\mathbf {T}: \nu) (x) | d x \leqslant \left(\sup _ {y \in \mathbf {Y} ^ {m}} \int_ {\mathbf {H}} | \mathbf {T} (x, y) | d x\right) \int_ {\mathbf {K}} | \nu (y) | d y,
$$

donc $\nu\to\mathbf{T}:\nu$ est continue de $\mathfrak{L}_{y}^{i}$ dans $\mathfrak{L}_{x}^{i}$; $\nu\to\mathbf{T}\cdot\nu$ et $\nu\to\mathbf{T}:\nu$ sont continues sur $\mathfrak{L}_{y}^{i}$ et coincident sur $\mathfrak{K}_{y}^{\infty}$, dense dans $\mathfrak{L}_{y}^{i}$, donc partout sur $\mathfrak{L}_{y}^{i}$.

Composition des noyaux au sens de Volterra (1).

PROPOSITION 34. — Soient X$^{l}$, Y$^{m}$, Z$^{n}$, trois espaces euclidiens, et S$_{x,y} \in \mathfrak{D}_{x,y}^{l}$, T$_{y,z} \in \mathfrak{D}_{y,z}^{l}$, deux noyaux. Supposons qu'il existe au moins un espace de distributions normal K$_{v}$ sur Y$^{m}$ (non nécessairement quasi-complet), tel que

$$
\mathbf {S} \in \mathfrak {D} _ {x} ^ {\prime} \widehat {\otimes} (\mathfrak {K} _ {y}) _ {c} ^ {\prime}, \quad \mathbf {T} \in \mathfrak {K} _ {y} \widehat {\otimes} \mathfrak {D} _ {z} ^ {\prime}.
$$

Alors il existe un noyau et un seul S ⊂ T ∈ 𝒟'\_{x,z}, appelé produit de composition de Volterra de S et T relativement à l'espace ℜ\_y, tel que

$$
(I, 4; 5 2) \quad \overrightarrow {i S \circ T} = \overrightarrow {i S} \circ \overrightarrow {i T} (^ {2}), \quad o u \quad (S \circ T) \cdot w = S \cdot (T \cdot w),
$$

(1) Cette composition a déjà été sommairement étudiée dans SCHWARTZ [6], n° 8 (théorème IX, X, XI).

(2) Ces résultats, $\overrightarrow{\mathrm{S}\circ\overrightarrow{\mathrm{T}}}=\overrightarrow{\mathrm{S}}\circ\overrightarrow{\mathrm{t}}\overrightarrow{\mathrm{T}}$ et $\overrightarrow{\mathrm{S}\circ\overrightarrow{\mathrm{T}}}=\overrightarrow{\mathrm{T}}\circ\overrightarrow{\mathrm{S}}$ sont évidemment assez choquants, et indiquent que les notations ne sont pas bonnes. Pour avoir de bonnes notations partout, il aurait fallu changer beaucoup de notations déjà bien établies en mathématiques :

1° Écrire les opérations initiales par des flèches de droite à gauche, et les transposées par des flèches de gauche à droite :

$C \xleftarrow{v} B \xleftarrow{u} A$ d'où $C \xleftarrow{v \circ u} A$, et $C' \xrightarrow{t_v} B' \xrightarrow{t_u} A'$ d'où $C' \xrightarrow{t_u \circ t_v} A'$. Une fonction quelconque $f$ devrait alors s'écrire $f(x) \leftarrow x$.

2° Une distribution $\overline{\mathbf{T}}$ sur $\mathbb{R}^n$ à valeurs dans E étant une opération $\mathbf{E} \leftarrow \mathfrak{D}$, devrait définir un élément de $\mathbf{E} \in \mathcal{D}'$ et non $\mathcal{D}'(\mathbf{E})$ ou $\mathcal{D}' \in \mathbf{E}$; $\vec{\mathbf{T}}$ serait toujours l'opération $\mathbf{E}_c' \to \mathcal{D}'$.

3° En conservant la règle de la page 92, permettant d'identifier les espaces qui ne changent pas l'ordre des variables, on identifierait $\mathbf{T} \in \mathfrak{D}_{x,y}'$ à $\vec{\mathbf{T}} \in \mathfrak{D}_{x}^{\prime}\in\mathfrak{D}_{y}^{\prime}$, définissant l'opération $\mathfrak{D}_{x}^{\prime} \leftarrow \mathfrak{D}_{y}$; $\vec{\mathbf{T}}$ serait alors l'opération $\mathbf{T} \cdot v \leftarrow v$. Dans ces conditions on identifierait $^{s}\mathbf{T} \in \mathfrak{D}_{y,x}^{\prime}$ à $^{t}\mathbf{T} \in \mathfrak{D}_{y}^{\prime}\in\mathfrak{D}_{x}^{\prime}$, définissant l'opération $u \rightarrow u \cdot \mathbf{T}$ ou $^{s}\mathbf{T} \cdot u \leftarrow u$, opération $\mathfrak{D}_{x} \rightarrow \mathfrak{D}_{y}^{\prime}$ ou $\mathfrak{D}_{y}^{\prime} \leftarrow \mathfrak{D}_{x}$ (changement de l'ordre de $x$, $y$, ou du sens de la flèche).

$^{40}$  S $\otimes$ T serait défini par  $\overrightarrow{S\otimes T} = \vec{S} \circ \vec{T}$  ou  $\overrightarrow{S\otimes T} = {}^{t}T \circ {}^{t}\overrightarrow{S}$ ,  $u \cdot (\mathrm{S}\otimes\mathrm{T}) = (u \cdot \mathrm{S}) \cdot \mathrm{T}$ , et  $(\mathrm{S}\otimes\mathrm{T}) \cdot w = \mathrm{S} \cdot (\mathrm{T} \cdot w)$ . La formule intégrale (I, 4; 54) serait conservée.

C'est la non-adoption de 1° en mathématiques qui est le péché originel.

pour toute $\mathcal{W} \in \mathfrak{D}_z$, ou

$$
(\mathrm{I}, 4; 5 3) \quad \overrightarrow {\mathrm{S} \circ \mathrm{T}} = \overrightarrow {\mathrm{T}} \circ \overrightarrow {\mathrm{S}}, \quad \text { ou } \quad u \cdot (\mathrm{S} \circ \mathrm{T}) = (u \cdot \mathrm{S}) \cdot \mathrm{T},
$$

pour toute $u \in \mathfrak{D}_x$.

S o T ne dépend que de S et T, non de $\mathfrak{K}_{y}$, si $\mathfrak{K}_{y}$ a la propriété d'approximation par troncature et par régularisation; on dit alors que S et T sont composables.

Si S et T sont 2 fonctions localement sommables, S semi-compact en y, et si, pour tout compact H de X$^{t}$, $\int_{\text{H}} |S(x, y)| dx$ est borné pour $y \in Y^{m}$, alors S et T sont composables, S ∘ T est une fonction, donnée pour presque toutes les valeurs de x et z par l'intégrale

$$
(\mathrm{I}, 4; 5 4) \quad (\mathrm{S} \circ \mathrm{T}) (x, z) = \int_ {\mathbf {Y} ^ {m}} \mathrm{S} (x, y) \mathrm{T} (y, z) d y.
$$

Si $\mathcal{H}_{x},\mathfrak{M}_{y}$, sont des espaces de distributions normaux (quasi-complets), et si $\mathfrak{K}_{y}$ est quasi-complet, $(^{\prime}\vec{\mathrm{S}},\mathrm{T})\to \mathrm{S}\circ \mathrm{T}$ est l'application bilinéaire canonique $(^{\prime}\vec{\mathrm{S}},\mathrm{T})\to (^{\prime}\vec{\mathrm{S}}\otimes \mathrm{I})\mathrm{T}$ de

$$
\mathrm{L} _ {c} \left(\mathfrak {K} _ {y}; \mathcal {H} _ {x}\right) \times \left(\mathfrak {K} _ {y} \in \mathfrak {M} _ {z}\right)
$$

dans $\mathcal{H}_{x}\in\mathfrak{M}_{z}$, hypocontinue par rapport aux parties équicontinues de $\mathfrak{L}(\mathfrak{K}_{y};\mathcal{H}_{x})$ et aux parties compactes de $\mathfrak{K}_{y}\in\mathfrak{M}_{z}$; si $\mathfrak{K}_{y}$ a la topologie $\gamma$, (S, T)→ S ∘ T est une application bilinéaire de $(\mathcal{H}_{x}\in(\mathfrak{K}_{y})_{c}^{\prime})\times(\mathfrak{K}_{y}\in\mathfrak{M}_{z})$ dans $\mathcal{H}_{x}\in\mathfrak{M}_{z}$, hypocontinue par rapport aux parties compactes.

On a en effet $\mathfrak{T} \in \mathfrak{L}(\mathfrak{D}_z; \mathfrak{K}_y)$, donc aussi $\mathfrak{T} \in \mathfrak{L}\big(\mathfrak{D}_z; ((\mathfrak{K}_y)')_c'\big)$ (remarque, page 36, appliquée à $L = \mathfrak{D}_z'$, $M = \mathfrak{K}_y$), et

$$
{ } ^ { i } \vec { \mathbf { S } } \in \mathcal { L } \left( \left( \left( \mathfrak { K } _ { y } \right) _ { c } ^ { \prime } \right) _ { c } ^ { \prime } ; \mathfrak { D } _ { x } ^ { \prime } \right) , \quad \text {   ~   d   o   n   c   ~   } \quad { } ^ { i } \vec { \mathbf { S } } \circ { } ^ { i } \vec { \mathbf { T } } \in \mathcal { L } ( \mathfrak { D } _ { z } ; \mathfrak { D } _ { x } ^ { \prime } ) ,
$$

et il existe bien un noyau et un seul  $S \circ T \in D_{x,z}^{\prime}$  tel que  $\overline{S \circ T} = \overline{iS} \circ \overline{iT}$ , ce qui est (I, 4; 52).

De même

$$
\vec {\mathrm{S}} \in \mathscr {L} (\mathfrak {D} _ {x}; (\mathfrak {K} _ {y}) _ {c} ^ {\prime}), \quad \vec {\mathrm{T}} \in \mathscr {L} ((\mathfrak {K} _ {y}) _ {c} ^ {\prime}; \mathfrak {D} _ {z}), \quad \text {   donc   } \quad \vec {\mathrm{T}} \circ \vec {\mathrm{S}} \in \mathscr {L} (\mathfrak {D} _ {x}; \mathfrak {D} _ {z} ^ {\prime});
$$

cette application est transposée de $\vec{\mathbf{S}}\circ\vec{\mathbf{T}}\in\mathfrak{L}(\mathfrak{D}_{z};\mathfrak{D}_{x}^{\prime})$, donc on a $\overrightarrow{\mathbf{S}\circ\mathbf{T}}=\overrightarrow{\mathbf{T}}\circ\overrightarrow{\mathbf{S}}$, ce qui est (I, 4; 53).

A priori S $\circ$ T dépend non seulement de S et T, mais de l'espace $\mathfrak{K}_{\nu}$ considéré. Nous allons voir qu'il n'en dépend pas.

si $\mathfrak{K}_{y}$ a la propriété d'approximation par troncature et régularisation. Soit $(\alpha_{\lambda})_{\lambda = 1,2,\ldots}$ une suite de fonctions de $\mathcal{D}$, tendant vers 1 dans $\mathcal{E}$ en restant bornée dans $\mathcal{B}$; soit $(\rho_{v})_{v = 1,2,\ldots}$ une suite de fonctions $\geqslant 0$ de $\mathcal{D}$, de supports tendant vers l'origine pour $v\to \infty$, et telles que $\int_{\mathbb{T}^{m}}\rho_{v}(x)dx = +1$. Alors on a

$$
(I, 4; 5 5)
$$

$$
\mathbf {T} \cdot w = \lim _ {\nu \rightarrow \infty} \left(\lim _ {\lambda \rightarrow \infty} \left(\alpha_ {\lambda} (\rho_ {\nu} * (\mathbf {T} \cdot w))\right)\right),
$$

la limite étant prise dans $\mathfrak{K}_{y}$, donc a fortiori dans la topologie affaiblie $\sigma(\mathfrak{K}_{y};\mathfrak{K}_{y}^{\prime})$; mais $\vec{\mathrm{S}}$, continue de $((\mathfrak{K}_{y})_{c}^{\prime})_{e}^{\prime}$ dans $\mathfrak{D}_{x}^{\prime}$, est continue pour les topologies affaiblies $\sigma(\mathfrak{K}_{y},\mathfrak{K}_{y}^{\prime})$ et $\sigma(\mathfrak{D}_{x}^{\prime},\mathfrak{D}_{x})$, et par suite on a, la limite étant prise pour la topologie $\sigma(\mathfrak{D}_{x}^{\prime},\mathfrak{D}_{x})$:

$$
(\mathrm{I}, 4; 5 6) \quad (\mathrm{S} \circ \mathrm{T}) \cdot w = \lim _ {v \rightarrow \infty} \left(\lim _ {\lambda \rightarrow \infty} \left(\mathrm{S} \cdot \left(\alpha_ {\lambda} \left(\rho_ {v} * (\mathrm{T} \cdot w)\right)\right)\right)\right).
$$

Or, pour $\nu$ et $\lambda$ fixées, $\alpha_{\lambda}(\rho_{\nu}*(\mathrm{T}\cdot w))\in\mathfrak{D}_{y}$; donc son image par $|\vec{\mathbf{S}}$ est connue dès que S, T, $w$, sont données, indépendamment de $\mathfrak{K}_{y}$; et il en est de même de la limite faible dans $\mathfrak{D}_{x}^{\prime}$, quand $\lambda$ puis $\nu$ tendent successivement vers $\infty$. Alors S$\circ$T est connu comme noyau de $\mathfrak{D}_{x,z}^{\prime}$, pour S et T données, indépendamment de $\mathfrak{K}_{y}$. Mais naturellement cela ne signifie pas que deux noyaux S et T puissent toujours être composés; ils le peuvent s'il existe un espace tel que $\mathfrak{K}_{y}$, et alors S$\circ$T ne dépend pas de cette espace s'il a la propriété d'approximation par troncature et régularisation. On dira alors que S et T sont composables, et on parlera de S$\circ$T sans spécifier $\mathfrak{K}_{y}$.

Supposons que S et T soient des fonctions (localement sommables), S semi-compact en y, et que, pour tout compact H de  $X^{l}$ ,  $\int_{H}|S(x,y)|dx$  soit borné pour  $y\in Y^{m}$ . On sait que  $T\in L_{y}^{1}\in L_{z}^{1}\subset L_{y}^{1}\in D_{z}^{\prime}$ , et que  $S\in L_{x}^{1}\in K_{y}^{\infty}\subset D_{x}^{\prime}\in K_{y}^{\infty}$  (proposition 33 et remarque qui la suit), donc S et T sont composables (avec  $K_{y}=L_{y}^{1}$ ,  $(\mathcal{K}_{y})_{c}^{\prime}=\mathcal{K}_{y}^{\infty}$ ), et de plus  $\overrightarrow{S\circ T}\in\mathcal{L}(\mathcal{K}_{x}^{\infty};\mathcal{L}_{z}^{1})$  et  $\overrightarrow{S\circ T}\in\mathcal{L}(\mathcal{K}_{z}^{\infty};\mathcal{L}_{x}^{1})$ . Nous allons voir que S o T est même une fonction,  $S\circ T\in L_{x,z}^{1}$ , donnée par (I, 4; 54).

Soit en effet $w \in \mathfrak{K}_{z}^{\infty}$; on sait que T·w est donnée, pour presque toutes les valeurs de y, par

$$
(\mathrm{I}, 4; 5 7) \quad (\mathrm{T} \cdot w) (y) = \int_ {\mathbb {Z} ^ {n}} \mathrm{T} (y, z) w (z) d z.
$$

Alors $\mathbf{T} \cdot w \in \mathcal{L}_{y}^{1}$; d'après la remarque qui suit la proposition

33, S·(T·w) est donnée, pour presque toutes les valeurs de x, par

$$
(\mathrm{I}, 4; 5 8) \quad (\mathrm{S} \cdot (\mathrm{T} \cdot w)) (x) = \int_ {\mathrm{Y} ^ {m}} \mathrm{S} (x, y) d y \int_ {\mathrm{Z} ^ {n}} \mathrm{T} (y, z) w (z) d z.
$$

Soit H un compact de $\mathbf{X}^i$; alors il existe un compact K de $\mathbf{Y}^m$, tel que $\mathbf{S}(x, y) = 0$ pour $x \in \mathbf{H}$, $y \notin \mathbf{K}$, puisque S est semicompact en $y$. Soit d'autre part L un compact de $\mathbf{Z}^n$. La fonction $\mathbf{S}(\hat{x}, \hat{y}) \mathbf{T}(\hat{y}, \hat{z})$ est mesurable; on a

$$
\iint_ {\mathbf {K} \times \mathbf {L}} | \mathrm{T} (y, z) | d y d z \int_ {\mathrm{H}} | \mathrm{S} (x, y) | d x <   + \infty ,
$$

puisque la dernière intégrale est supposée bornée et que T est localement sommable; donc S(ˆx,ˆy)T(ˆy,ˆz) est sommable sur H × K × L ou H × Y$^{m}$ × L; alors, d'après le théorème de Fubini, ∫Y$^{m}$S(x, y)T(y, z) dy a un sens pour presque toutes les valeurs de x, z, et représente une fonction N localement sommable de x, z. De plus, S(ˆx,ˆy)T(ˆy,ˆz)ω(ˆz) est aussi sommable sur H × Y$^{m}$ × Z$^{n}$, de sorte que ∫Y$^{m}$×Z$^{n}$S(x, y)T(y, z)ω(z) dy dz a un sens pour presque toutes les valeurs de x. Si, pour un x déterminé, cette intégrale a un sens, celle du 2$^{e}$ membre de (I, 4; 58) en a aussi un, et elles sont égales; et elles sont alors aussi égales à

$$
\int_ {\mathbf {Z} ^ {n}} w (z) d z \int_ {\mathbf {Y} ^ {m}} \mathrm{S} (x, y) \mathrm{T} (y, z) d y.\tag{I, 4; 59}
$$

Finalement, on voit que  $(\mathbf{S} \circ \mathbf{T}) \cdot w$  est une fonction, donnée pour presque toutes les valeurs de x par

$$
((\mathrm{S} \circ \mathrm{T}) \cdot w) (x) = \int_ {\mathbb {Z} ^ {n}} \mathrm{N} (x, z) w (z) d z = (\mathrm{N} \cdot w) (x),\tag{I, 4; 60}
$$

de sorte qu'on a bien $\mathbf{S} \circ \mathbf{T} = \mathbf{N} \in \mathcal{L}_{x,z}^{1}$.

Naturellement, si S et T sont des fonctions, il y a bien d'autres cas que celui que nous venons de traiter, pour lesquels S o T est une fonction donnée par (I, 4; 54) (ne serait-ce que le cas obtenu en changeant les rôles de S et T); nous n'avons voulu ici que donner un exemple des difficultés qui se présentent: il ne s'agit pas seulement de montrer que $\int_{\mathbf{Y}^m}\mathrm{S}(x,y)\mathrm{T}(y,z)dy$ a un sens pour presque toutes les valeurs de $x,z$, et représente une fonction localement sommable de $x,z$, mais que S et T sont composables au sens indiqué ici

(avec un espace $\mathfrak{N}_y$ ayant les propriétés voulues), et que S $\circ$ T est donné par l'intégrale ci-dessus.

Soient maintenant \( ^{t}\vec{S} \in \mathscr{L}\_{c}(\mathfrak{K}\_{y}; \mathscr{H}\_{x}) \subset \mathscr{H}\_{x} \in (\mathfrak{K}\_{y})\_{c}^{\prime} \). D'après la proposition 1 du § 1, on peut définir une application linéaire continue \( ^{t}\vec{S} \otimes I \) de \( \mathfrak{K}\_{y} \in \mathfrak{M}\_{z} \) dans \( \mathscr{H}\_{x} \in \mathfrak{M}\_{z} \) (I, opérateur identique de \( \mathfrak{M}\_{z} \)); on a bien évidemment \( (^{t}\vec{S} \otimes I)T = S \circ T \) pour \( T \in \mathfrak{K}\_{y} \in \mathfrak{M}\_{z} \), d'après la remarque 1° de la page 35, puisque cela revient à dire que \( ^{t}\vec{S} \circ ^{t}\vec{T} \circ ^{t}I = ^{\overline{S} \circ \overline{T}} \). Le corollaire 3 de la proposition 2 du § 1 (valable lorsque les espaces \( \mathscr{H}, \mathfrak{K}, \mathfrak{M} \), sont quasi-complets) montre alors que \( (^{t}\vec{S}, T) \to S \circ T \) est une application bilinéaire de \( \mathscr{L}\_{c}(\mathfrak{K}\_{y}; \mathscr{H}\_{x}) \times (\mathfrak{K}\_{y} \in \mathfrak{M}\_{z}) \) dans \( \mathscr{H}\_{x} \in \mathfrak{M}\_{z} \), hypocontinue par rapport aux parties équicontinues de \( ^{\mathscr{L}}(\mathfrak{K}\_{y}; \mathscr{H}\_{x}) \) et aux parties compactes de \( \mathfrak{K}\_{y} \in \mathfrak{M}\_{z} \). On peut modifier de diverses façons ce dernier résultat. Supposons toujours \( T \in \mathfrak{K}\_{y} \in \mathfrak{M}\_{z} \), mais seulement \( S \in \mathscr{H}\_{x} \in (\mathfrak{K}\_{y})\_{c}^{\prime} \), ce qui entraîne \( ^{t}\vec{S} \in \mathscr{L}\big((\mathfrak{K}\_{y})\_{c}^{\prime}\big)\_{c}^{\prime}; \mathscr{H}\_{x}\big) \), mais non nécessairement \( ^{t}\vec{S} \in ^{\mathscr{L}}(\mathfrak{K}\_{y}; \mathscr{H}\_{x}) \). On a quand même \( ^{\vec{S}} \in ^{\mathscr{L}}((\mathscr{H}\_{x})\_{c}^{\prime}; (\mathfrak{K}\_{y})\_{c}^{\prime}),   ^{\vec{T}} \in ^{\mathscr{L}}((\mathfrak{K}\_{y})\_{c}^{\prime}; \mathfrak{M}\_{z}) \), donc \( ^{\vec{T}}\circ ^{\vec{S}}\in^{t}\mathscr{L}((\mathscr{H}\_{x})\_{c}^{\prime}; \mathfrak{M}\_{z}) \), et par suite \( S\circ T\in\mathscr{H}\_{x}\in\mathfrak{M}\_{z} \). Si S converge vers 0 dans \( H\_{x}\in(^{\mathscr{L}}(\mathfrak{K}\_{y})\_{c}^{\prime},\vec{S}\) converge vers 0 dans \( ^{\mathscr{L}}\_{\varepsilon}((\mathscr{H}\_{x})\_{c}^{\prime};(\mathfrak{K}\_{y})\_{c}^{\prime}) \); si alors T parcourt une partie compacte de \( K\_{y}\in M\_{z},\vec{T}\) parcourt une partie équi-continue de \( ^{\mathscr{L}}((\mathfrak{K}\_{y})\_{c}^{\prime};\mathfrak{M}\_{z}) \) (corollaire 1 de la proposition 4 du § 1), donc \( ^{\vec{T}}\circ ^{\vec{S}}\) converge vers 0 dans \( ^{\mathscr{L}}\_{\varepsilon}((\mathscr{H}\_{x})\_{c}^{\prime};\mathfrak{M}\_{z}) \), et par suite S\( \_o \)T converge encore vers 0 dans \( H\_{x}\in^{\mathscr{L}}\mathfrak{M}\_{z} \). Mais si T converge vers 0 dans \( K\_{y}\in M\_{z},\quad ^{\vec{T}}\text {converge vers }0\text { dans }^{\mathscr{L}}\_{\varepsilon}((\mathfrak{M}\_{z})\_{c}^{\prime};\mathfrak{K}\_{y}) ;\text {et si S est un élément fixe de }H\_{x}\in(^{\mathscr{L}}(K\_{y})\_{c}^{\prime})\_{c}^{\prime}\text { tel que }^{\vec{T}}\text {, continue de }((\mathfrak{K}\_{y})\_{c}^{\prime})\_{c}^{\prime}\text { dans }H\_{x},\text { ne soit pas continue de }K\_{y}\text { dans }H\_{x},\quad ^{\vec{T}}\circ ^{\vec{T}}\text { ne convergera pas nécessairement vers 0 dans }^{\mathscr{L}}\_{\varepsilon}((\mathfrak{M}\_{z})\_{c}^{\prime};\mathscr{H}\_{x}) ,\text { et par suite S\( \_o \)T ne convergera pas vers 0 dans }H\_{x}\in^{\mathscr{L}}\mathfrak{M}\_{z}.

Donc (S, T) → S ∘ T est une application bilinéaire de  $(\mathcal{H}_{x} \in (\mathfrak{K}_{y})_{c}^{\prime}) \times (\mathfrak{K}_{y} \in \mathfrak{M}_{z})$  dans  $H_{x} \in M_{z}$ , mais on ne peut pas affirmer que cette application soit séparément continue.

Si $\mathfrak{K}_y$ a la topologie $\gamma$, alors $((\mathfrak{K}_y)_c')_c' = \mathfrak{K}_y$ (page 17), $\mathcal{L}_c(\mathfrak{K}_y; \mathcal{H}_x) \approx \mathcal{H}_x \in (\mathfrak{K}_y)_c'$ (corollaire de la proposition 5 du § 1), et l'application bilinéaire ci-dessus est hypocontinue par rapport aux parties compactes de $\mathcal{H}_x \in (\mathfrak{K}_y)_c'$ (qui sont des parties équicontinues de $\mathcal{L}((\mathfrak{K}_y)_c')_c; \mathcal{H}_x) = \mathcal{L}(\mathfrak{K}_y; \mathcal{H}_x)$ d'après le corollaire 1 de la proposition 4) et de $\mathfrak{K}_y \in \mathfrak{M}_z$.

Remarque. — 1° S'il existe un espace normal $\mathfrak{K}_{y}$ tel que $S \in \mathcal{D}_{x}^{\prime} \varepsilon (\mathfrak{K}_{y})_{c}^{\prime}, T \in \mathfrak{K}_{y} \varepsilon \mathcal{D}_{z}^{\prime}$, on peut définir $S \circ T$ même si $\mathfrak{K}_{y}$ n'a pas la propriété d'approximation par troncature et par régularisation; les propriétés d'hypocontinuité de la proposition restent exactes; mais $S \circ T$, pour $S$ et $T$ données, peut alors dépendre de l'espace $\mathfrak{K}_{y}$ considéré. Toutefois, pour affirmer que $S \circ T$ ne dépend que de $S$ et $T$, il est beaucoup trop restrictif de supposer que $\mathfrak{K}_{y}$ a la propriété d'approximation par troncature et régularisation. Il suffira par exemple de savoir (voir la démonstration page 116) que, lorsque $\alpha \in \mathcal{D}$ converge vers 1 dans $\varepsilon$ en restant bornée dans $\mathfrak{B}$, et lorsque $\rho \in \mathcal{D}$ a son support convergeant vers l'origine tandis que $\rho \geqslant 0$ et que $\int_{\mathbf{Y}^{n}} \rho(y) dy$ converge vers 1, les opérateurs de multiplication [α] et de régularisation {ρ} convergent vers I dans $\mathscr{L}_{s}((\mathfrak{K}_{y})_{\sigma}; (\mathfrak{K}_{y})_{\sigma})$, où $\mathscr{L}_{s}$ est la topologie de la convergence simple, et où $(\mathfrak{K}_{y})_{\sigma}$ est l'espace $\mathfrak{K}_{y}$ muni de la topologie affaiblie $\sigma(\mathfrak{K}_{y}, \mathfrak{K}_{y}')$.

2° Supposons que $\mathcal{L}_{y}$ soit un espace de distributions normal, et que $S \in \mathcal{D}_{x}^{\prime} \otimes \mathcal{L}_{y}$, $T \in (\mathcal{L}_{y})_{c}^{\prime} \otimes \mathcal{D}_{z}^{\prime}$. Alors, en passant aux noyaux symétriques, on pourra montrer, en appliquant la proposition 34, l'existence d'un noyau $S \circ T = ^s(^s T \circ ^s S)$. Ce nouveau noyau est indépendant de l'espace $\mathcal{L}_{y}$, si celui-ci a la propriété d'approximation par troncature et par régularisation, ou la propriété plus faible signalée à la remarque 1°. Si S et T sont composables au sens de la proposition 34, relativement à un espace $\mathcal{K}_{y}$, ils le sont au sens symétrique indiqué ici, relativement à $\mathcal{L}_{y} = (\mathcal{K}_{y})_{c}^{\prime}$, et le produit de composition est le même. Si en effet

$$
\mathbf {S} \in \mathfrak {D} _ {x} ^ {\prime} \widehat {\otimes} (\mathfrak {K} _ {y}) _ {c} ^ {\prime}, \quad \mathbf {T} \in \mathfrak {K} _ {y} \widehat {\otimes} \mathfrak {D} _ {z} ^ {\prime},
$$

alors

$$
\mathbf {S} \in \mathfrak {D} _ {x} ^ {\prime} \widehat {\otimes} \mathfrak {L} _ {y}, \quad \mathbf {T} \in (\mathfrak {L} _ {y}) _ {c} ^ {\prime} \widehat {\otimes} \mathfrak {D} _ {z} ^ {\prime},
$$

avec $\mathfrak{L}_{y} = (\mathfrak{K}_{y})_{c}^{\prime}$ (voir remarque page 36), et on a, d'après les formules (I, 4; 52 et 53):

ou

$$
\begin{array}{c} \overrightarrow {s (s ^ {r} \mathbf {T} \circ^ {s} \mathbf {S})} = \overrightarrow {t _ {s}} \overrightarrow {\mathbf {T} \circ s} \overrightarrow {\mathbf {S}} = \overrightarrow {t _ {s}} \overrightarrow {\mathbf {T}} \circ \overrightarrow {t _ {s}} \overrightarrow {\mathbf {S}} = \overrightarrow {\mathbf {T}} \circ \overrightarrow {\mathbf {S}} = \overline {{\mathbf {S} \circ \overrightarrow {\mathbf {T}}}} \\ s (s ^ {r} \mathbf {T} \circ^ {s} \mathbf {S}) = \mathbf {S} \circ \mathbf {T}. \end{array}
$$

Les propriétés d'approximation par troncature et régularisation pour $\mathfrak{K}_{y}$ et pour $\mathfrak{L}_{y}$ ne sont pas équivalentes, mais les

propriétés plus faibles indiquées à la remarque 1° sont équivalentes, car $u \to {}^t u$ est un isomorphisme topologique de $\mathcal{L}_s((\mathfrak{K}_y)_\sigma; (\mathfrak{K}_y)_\sigma)$ sur $\mathcal{L}_s((\mathfrak{L}_y)_\sigma; (\mathfrak{L}_y)_\sigma)$.

Associativité du produit de Volterra.

Soient $X^{l}, Y^{m}, \bar{Z}^{n}, U^{p}$, des espaces euclidiens, et $R \in \mathfrak{D}_{x,y}^{\prime}$, $S \in \mathfrak{D}_{y,z}^{\prime}$, $T \in \mathfrak{D}_{z,u}^{\prime}$, 3 noyaux. Il peut fort bien arriver que les 2 produits de composition $(R \circ S) \circ T$, $R \circ (S \circ T)$, aient un sens et soient inégaux, ou qu'un seul d'entre eux ait un sens (').

Mais supposons qu'il existe des espaces de distributions normaux $\mathfrak{K}_{y}$, $\mathfrak{M}_{z}$, tels que

$$
\mathrm{R} \in \mathfrak {D} _ {x} ^ {\prime} \widehat {\otimes} (\mathfrak {K} _ {y}) _ {c} ^ {\prime}, \quad \mathrm{S} \in \mathfrak {K} _ {y} \varepsilon (\mathfrak {M} _ {z}) _ {c} ^ {\prime}, \quad \mathrm{T} \in \mathfrak {M} _ {z} \widehat {\otimes} \mathfrak {D} _ {u} ^ {\prime},
$$

alors on peut définir d'emblée un produit R $\circ$ S $\circ$ T $\in$$\mathfrak{D}'_{x,u}$, relativement à $\mathcal{K}_y$, $\mathfrak{M}_z$, par :

$$
(\mathrm{I}, 4; 6 1) \quad (\mathrm{R} \circ \mathrm{S} \circ \mathrm{T}) \cdot w = \mathrm{R} \cdot (\mathrm{S} \cdot (\mathrm{T} \cdot w))
$$

pour toute $\mathcal{W} \in \mathcal{D}_u$, ou

$$
(\mathrm{I}, 4; 6 2) \quad u \cdot (\mathrm{R} \circ \mathrm{S} \circ \mathrm{T}) = ((u \cdot \mathrm{R}) \cdot \mathrm{S}) \cdot \mathrm{T}
$$

pour toute $u \in \mathcal{D}_x$.

Si $\mathfrak{K}_{y}$ et $\mathfrak{M}_{z}$ vérifient la propriété d'approximation par troncature et régularisation, ou la propriété plus faible de la remarque $1^{\circ}$, page 119, ce produit dépend intrinsèquement de R, S, T, et non de $\mathfrak{K}_{y}$ et $\mathfrak{M}_{z}$.

D'autre part, on a dans ce cas

$$
(\mathrm{I}, 4; 6 3) \quad \mathrm{R} \circ \mathrm{S} \circ \mathrm{T} = (\mathrm{R} \circ \mathrm{S}) \circ \mathrm{T} = \mathrm{R} \circ (\mathrm{S} \circ \mathrm{T})
$$

(associativité), chacun des produits ayant un sens intrinsèque, indépendant de $\mathfrak{K}_{y}$ et $\mathfrak{M}_{z}$.

Nous laissons au lecteur le soin d'étendre le résultat à la composition d'un nombre fini de noyaux, et d'établir les propriétés d'hypocontinuité d'un tel produit.

EXEMPLES. PROPOSITION 35. — Le produit de composition de Volterra de plusieurs noyaux a un sens, si tous ceux qui sont à droite de l'un d'eux sont semi-réguliers à gauche, tous ceux qui sont à gauche semi-réguliers à droite, aucune hypothèse de régu-

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Voir exemples de noyaux de multiplication ou de convolution: SCHWARTZ [4], formules (V, 2; 9 et 10), et [5], formule (VI, 5; 3).</span></small>

larité n'étant faite sur ce noyau, et si, en même temps, tous ceux qui sont à droite de l'un d'eux sont semi-compacts à gauche, tous ceux qui sont à gauche semi-compacts à droite, aucune hypothèse de compacité n'étant faite sur ce noyau. En particulier, il a un sens si tous les noyaux sont réguliers, sauf un au plus, et tous compacts, sauf un au plus.

Si tous les noyaux sont réguliers (resp. compacts), et tous, sauf un au plus, compacts (resp. réguliers), le produit est régulier (resp. compact).

Si tous les noyaux sont réguliers, et l'un d'eux régularisant (resp. si tous sont compacts, et l'un d'eux compactifiant), et si en même temps tous, sauf un au plus, sont compacts (resp. réguliers), le produit est régularisant (resp. compactifiant).

Soient en effet  $X_{1}^{n_{l}}$ ,  $X_{2}^{n_{2}}$ ,  $\ldots$ ,  $X_{l}^{n_{l}}$  des espaces euclidiens, et soient

$$
\mathrm{T} _ {j} \in \mathcal {D} _ {x _ {j}, x _ {j + 1}} ^ {\prime}, j = 1, 2, \dots , l - 1.
$$

Supposons, pour fixer les idées,  $T_{k}$ ,  $T_{k+1}$ , ...,  $T_{l-1}$ , semi-réguliers à gauche et semi-compacts à gauche,  $T_{k-1}$  semi-compact à gauche sans hypothèse de régularité,  $T_{h}$ ,  $T_{h+1}$ , ...,  $T_{k-2}$ , semi-réguliers à droite et semi-compacts à gauche,  $T_{h-1}$  semi-régulier à droite sans hypothèse de compacité, et  $T_{1}$ ,  $T_{2}$ , ...  $T_{h-2}$ , semi-réguliers à droite et semi-compacts à droite. Alors  $T_{1} \circ T_{2} \circ \ldots \circ T_{l-1}$  a un sens intrinsèque et est associatif, grâce à une chaîne d'applications linéaires continues :

$$
\begin{array}{r l}\mathcal {D} _ {x _ {l}}&\rightarrow \mathcal {D} _ {x _ {l - 1}} \rightarrow \dots \rightarrow \mathcal {D} _ {x _ {k + 1}} \rightarrow \mathcal {D} _ {x _ {k}} \rightarrow \mathcal {E} _ {x _ {k - 1}} ^ {\prime} \rightarrow \mathcal {E} _ {x _ {k - 2}} ^ {\prime} \rightarrow \dots\\&\rightarrow \mathcal {E} _ {x _ {h + 1}} ^ {\prime} \rightarrow \mathcal {E} _ {x _ {h}} ^ {\prime} \rightarrow \mathcal {D} _ {x _ {h - 1}} ^ {\prime} \rightarrow \mathcal {D} _ {x _ {h - 2}} ^ {\prime} \dots \rightarrow \mathcal {D} _ {x _ {2}} ^ {\prime} \rightarrow \mathcal {D} _ {x _ {1}} ^ {\prime}\end{array}
$$

(voir démonstration de la proposition 31 et remarque qui la suit).

Si, au lieu de cela, nous supposons  $T_{k-1}$  semi-régulier à gauche sans hypothèse de compacté,  $T_{h}, T_{h+1}, \ldots, T_{k-2}$ , semi-compacts à droite et semi-réguliers à gauche,  $T_{h-1}$  semi-compact à droite sans hypothèse de régularité, et si nous ne changeons rien aux hypothèses relatives à  $T_{1}, \ldots, T_{h-2}$  ni  $T_{k}, \ldots, T_{l-1}$ , on aura le même résultat avec une chaîne d'applications

$$
\begin{array}{r l} \mathfrak {D} _ {x _ {l}} & \to \mathfrak {D} _ {x _ {l - 1}} \to \dots \to \mathfrak {D} _ {x _ {k + 1}} \to \mathfrak {D} _ {x _ {k}} \to \mathfrak {E} _ {x _ {k - 1}} \to \mathfrak {E} _ {x _ {k - 2}} \to \dots \\ & \to \mathfrak {E} _ {x _ {h - 1}} \to \mathfrak {E} _ {x _ {h}} \to \mathfrak {D} _ {x _ {h - 1}} ^ {\prime} \to \mathfrak {D} _ {x _ {h - 2}} ^ {\prime} \dots \to \mathfrak {D} _ {x _ {2}} ^ {\prime} \to \mathfrak {D} _ {x _ {1}} ^ {\prime}. \end{array}
$$

Dans chacune des deux hypothèses, tous les noyaux d'indice

strictement plus grand que l'un d'entre eux sont semi-réguliers à gauche, et les noyaux d'indice strictement plus petits sont semi-réguliers à droite, aucune hypothèse de régularité n'étant faite sur ce noyau; il en est de même pour les hypothèses de compacité; la position relative des deux noyaux de transition est quelconque (et ils sont confondus si h = k).

Si en particulier tous les noyaux sont réguliers, sauf un au plus, et tous compacts, sauf un au plus (les 2 noyaux exceptionnels ayant une position relative quelconque, et pouvant ou non être confondus), on se trouve dans ce cas.

Supposons maintenant tous les noyaux réguliers, et tous, sauf un au plus, par exemple  $T_{h-1}$ , compacts. On se trouve dans le cas d'une chaîne d'applications

$$
\mathcal {D} _ {x _ {l}} \rightarrow \mathcal {D} _ {x _ {l - 1}} \rightarrow \dots \rightarrow \mathcal {D} _ {x _ {h + 1}} \rightarrow \mathcal {D} _ {x _ {h}} \rightarrow \mathfrak {E} _ {x _ {h - 1}} \rightarrow \dots \rightarrow \mathfrak {E} _ {x _ {2}} \rightarrow \mathfrak {E} _ {x _ {1}},
$$

donc le produit est semi-régulier à gauche; mais on a aussi une chaîne d'applications

$$
\mathcal {E} _ {x _ {l}} ^ {\prime} \rightarrow \mathcal {E} _ {x _ {l - 1}} ^ {\prime} \rightarrow \dots \rightarrow \mathcal {E} _ {x _ {h + 1}} ^ {\prime} \rightarrow \mathcal {E} _ {x _ {h}} ^ {\prime} \rightarrow \mathfrak {D} _ {x _ {h - 1}} ^ {\prime} \rightarrow \dots \rightarrow \mathfrak {D} _ {x _ {2}} ^ {\prime} \rightarrow \mathfrak {D} _ {x _ {1}} ^ {\prime},
$$

donc le produit est semi-régulier à droite (les 2 chaînes donnent le même produit, parce que tous les espaces D, E, D', E', ont la propriété d'approximation par troncature et régularisation), et par suite il est régulier. On montrera de la même manière que si tous les noyaux sont compacts, et tous, sauf un au plus, réguliers, le produit est compact.

En particulier, si tous les noyaux sont réguliers compacts, il en est de même du produit.

Supposons maintenant tous les noyaux réguliers,  $T_{m-1}$  régularisant, et tous les noyaux compacts, sauf peut-être  $T_{h-1}$ . Si  $h \leqslant m$ , on aura une chaîne d'applications continues

$$
\begin{array}{r l}\mathcal {E} _ {x _ {l}} ^ {\prime}&\rightarrow \mathcal {E} _ {x _ {l - 1}} ^ {\prime} \rightarrow \dots \mathcal {E} _ {x _ {m}} ^ {\prime} \rightarrow \mathcal {D} _ {x _ {m - 1}} \rightarrow \mathcal {D} _ {x _ {m - 2}} \rightarrow\\&\dots \mathcal {D} _ {x _ {h + 1}} \rightarrow \mathcal {D} _ {x _ {h}} \rightarrow \mathcal {E} _ {x _ {h - 1}} \rightarrow \mathcal {E} _ {x _ {h - 2}} \rightarrow \dots \rightarrow \mathcal {E} _ {x _ {2}} \rightarrow \mathcal {E} _ {x _ {1}}\end{array}
$$

(le fait que $\mathbf{T}_{m-1}$ applique continuement $\mathcal{E}_x^{\prime}_{m}$ dans $\mathfrak{D}_{x_{m-1}}$ résulte de ce qu'il applique $\mathcal{E}_x^{\prime}_{m}$ dans $\mathcal{E}_{x_{m-1}}$ puisque régularisant, et dans $\mathcal{E}_x^{\prime}_{m-1}$ puisque compact; alors il applique $\mathcal{E}_x^{\prime}_{m}$ dans $\mathcal{E}_{x_{m-1}} \cap \mathcal{E}_{x_{m-1}}^{\prime} = \mathfrak{D}_{x_{m-1}}$, et l'application est continue en vertu de la proposition 26 ou 27), donc le produit est régularisant. Démonstration analogue pour $h > m$.

De même, si tous les noyaux sont compacts, l'un d'eux compactifiant, et si tous, sauf un au plus, sont réguliers, le produit est compactifiant.

Distributions semi-tempérées, et transformation de Fourier partielle. On dit qu'un noyau $T \in \mathcal{D}_{x,y}'$ est semi-tempéré en $x$, s'il appartient à

$$
\mathcal {S} _ {x} ^ {\prime} \varepsilon \mathfrak {D} _ {y} ^ {\prime} = \mathcal {S} _ {x} ^ {\prime} \widehat {\otimes} \mathfrak {D} _ {y} ^ {\prime} = \mathscr {L} (\mathcal {S} _ {x}; \mathfrak {D} _ {y} ^ {\prime}) \approx \mathscr {L} (\mathfrak {D} _ {y}; \mathcal {S} _ {x} ^ {\prime}).
$$

Pour qu'il en soit ainsi, il faut et il suffit qu'il vérifie l'une des 2 conditions équivalentes suivantes :

$1^{\circ}$ L'application $u \to u \cdot T$ est continue de $\mathfrak{D}_x$, muni de la topologie, induite par $\mathscr{S}_x$, dans $\mathfrak{D}_y'$ (parce que $\mathfrak{D}$ est dense dans $\mathscr{S}$, et $\mathfrak{D}'$ complet).

2° Pour toute  $\nu\in D_{y}$ , T· $\nu$  est dans  $S_{x}^{\prime}$  (propositions 26 et 27).

Pour toute T semi-tempérée en $x$, on peut effectuer la transformation de Fourier partielle $\mathcal{F}_{x}$ en $x$ [qu'on peut noter symboliquement

$$
\mathrm{T} \rightarrow \int_ {\mathbf {X} ^ {n}} \exp (- 2 i \pi x \hat {\xi}) \mathrm{T} (x, \hat {y}) d x \in \mathcal {S} _ {\xi} ^ {\prime} \otimes \mathcal {D} _ {y} ^ {\prime}; \tag {I,4;64}
$$

cette notation sera justifiée page 134].

La transformation précédente n'est autre que $\mathcal{F}_{x} \otimes I$ opérant sur $\mathcal{S}_{x}^{\prime} \otimes \mathcal{D}_{y}^{\prime}$ (proposition 1 du § 1, et transformation de Fourier page 73, avec $E = \mathcal{D}_{y}^{\prime}$).

Si en outre T est dans $\mathcal{G}_{x}^{\prime}\varepsilon\mathfrak{K}_{y}$, alors son image de Fourier est dans $\mathcal{G}_{\xi}^{\prime}\varepsilon\mathfrak{K}_{y}$.

La formule (I, 3; 13), appliquée à E = $\mathfrak{D}_{y}^{\prime}$, donne, pour toute $u \in \mathcal{S}_{\xi}$:

$$
(\mathrm{I}, 4; 6 5)
$$

$$
u \cdot \mathcal {F} _ {x} T = \mathcal {F} u \cdot T.
$$

La formule (I, 3; 14) donne, pour toute $\nu \in \mathfrak{D}_{y}$:

(I, 4; 66)

$$
\mathcal {F} _ {x} \mathrm{T} \cdot \nu = \mathcal {F} (\mathrm{T} \cdot \nu).
$$

Soit T une distribution tempérée sur  $X^{l} \times Y^{m}: T \in S_{x,y}^{\prime}$ . Elle est alors semi-tempérée en x, puisqu'elle appartient même à  $S_{x}^{\prime} \otimes S_{y}^{\prime}$  (proposition 28); on peut donc calculer sa transformée de Fourier partielle  $F_{x}T$ , qui, appartient à  $S_{\xi}^{\prime} \otimes S_{y}^{\prime}$ , donc est semi-tempérée en y; on peut alors calculer sa transformée de Fourier

partielle $\mathcal{F}_{y}(\mathcal{F}_{x}\mathrm{T})$; le résultat obtenu est simplement sa transformée de Fourier totale en $x, y$, car on a

$$
(\mathrm{I}, 4; 6 7)
$$

$$
\left(\mathrm{I} _ {\xi} \otimes \mathcal {F} _ {y}\right) \circ \left(\mathcal {F} _ {x} \otimes \mathrm{I} _ {y}\right) = \mathcal {F} _ {x} \otimes \mathcal {F} _ {y},
$$

et il suffit alors d'appliquer la proposition 29.

Noyaux à valeurs vectorielles.

Soit E un espace vectoriel localement convexe séparé (non nécessairement quasi-complet).

Une distribution $\vec{\mathbf{T}}\in\mathfrak{D}_{x,y}^{\prime}(\mathbf{E})$ sera un noyau à valeurs dans E. On devra ici distinguer soigneusement la transposition $t$ et la symétrie $s$. La symétrie $s:(x,y)\to(y,x)$, isomorphisme de $\mathbf{X}^{l}\times\mathbf{Y}^{m}$ sur $\mathbf{Y}^{m}\times\mathbf{X}^{l}$, définit, par transport de structure, un isomorphisme canonique, toujours appelé $s:\vec{\mathbf{T}}\to^{s}\vec{\mathbf{T}}$, de $\mathfrak{D}_{x,y}^{\prime}(\mathbf{E})$ sur $\mathfrak{D}_{y,x}^{\prime}(\mathbf{E})$, avec $s\circ s=\mathbf{I}$.

Un noyau $\widetilde{\mathbf{T}}\in\mathfrak{D}_{x,y}^{\prime}(\mathbf{E})$ définit les opérations suivantes :

$^{10}$ Une application linéaire continue de $\mathcal{D}_{x,y}$ dans E, appelée $\vec{T}$. Sa notation intégrale sera :

$$
(\mathrm{I}, 4; 6 8) \quad \varphi (\hat {x}, \hat {y}) \rightarrow \vec {\mathrm{T}} \cdot \varphi = \iint_ {\mathbf {X} ^ {l} \times \mathbf {Y} ^ {m}} \vec {\mathrm{T}} (x, y) \varphi (x, y) d x d y \in \mathrm{E},
$$

pour $\varphi\in\mathcal{D}_{x,y}$.

Alors la symétrique  ${}^{s}T$  est une application linéaire continue de  $D_{y,x}$  dans E.

La transposée $^{t}\vec{T}$ est une application linéaire continue: $\vec{e}' \to \langle \vec{T}, \vec{e}' \rangle$, de $E_c'$ dans $D_{x,y}'$; alors la transposée $^{ts}\vec{T} = ^{st}\vec{T}$ est une application linéaire continue: $\vec{e}' \to \langle^s\vec{T}, \vec{e}' \rangle$, de $E_c'$ dans $D_{y,x}'$.

2° Une application linéaire continue:  $u \rightarrow u \cdot \vec{T}$ , de  $D_{x}$  dans  $\mathfrak{D}_{y}^{\prime}(\mathrm{E})$  par

$$
\left(u \cdot \vec {\mathrm{T}}\right). \nu = \vec {\mathrm{T}}. (u \otimes \nu), \quad u \in \mathfrak {D} _ {x}, \quad \nu \in \mathfrak {D} _ {y}.
$$

Sa notation intégrale sera :

$$
(\mathrm{I}, 4; 7 0) \quad u (\hat {x}) \rightarrow \int_ {\mathbf {x} ^ {l}} \vec {\mathrm{T}} (x, \hat {y}) u (x) d x \in \mathfrak {D} _ {y} ^ {\prime} (\mathrm{E}),
$$

pour $u \in \mathfrak{D}_x$.

On pourra noter $\overline{\mathbf{T}}\in\mathfrak{D}_{x}^{\prime}(\mathfrak{D}_{y}^{\prime}(\mathrm{E}))$ cette application. Alors $\overline{\mathbf{T}}$ est sa transposée, application linéaire continue de $(\mathfrak{D}_{y}^{\prime}(\mathrm{E}))_{c}^{\prime}$ dans $\mathfrak{D}_{x}^{\prime}$.

3° Une application linéaire continue $\nu\to\tilde{\mathbf{T}}\cdot\nu$, de $\mathfrak{D}_{y}$ dans $\mathfrak{D}_{x}^{\prime}(\mathbf{E})$, par

$$
(I; 4, 7 1) \quad (\vec {T} \cdot \nu). u = \vec {T}. (u \otimes \nu), \quad u \in \mathfrak {D} _ {x}, \quad \nu \in \mathfrak {D} _ {\gamma}.
$$

Sa notation intégrale sera

$$
(I, 4; 7 2) \quad \nu (\hat {y}) \rightarrow \int_ {\mathbf {Y} ^ {m}} \vec {\mathrm{T}} (\hat {x}, y) \nu (y) d y \in \mathfrak {D} _ {x} ^ {\prime} (E),
$$

pour $\nu\in\mathfrak{D}_{y}$.

On pourra noter  ${}^{s}\vec{T} \in \mathfrak{D}_{y}^{\prime}(\mathfrak{D}_{x}^{\prime}(\mathrm{E}))$  cette application, car  $\nu \cdot {}^{s}\vec{T} = \vec{T} \cdot \nu$ . Alors  ${}^{t}\vec{T}$  est sa transposée, application linéaire continue de  $(\mathfrak{D}_{x}^{\prime}(\mathrm{E}))_{c}^{\prime}$  dans  $D_{y}^{\prime}$ .

On a toujours :

$$
\mathfrak {D} _ {x, y} ^ {\prime} (\mathrm{E}) = \mathscr {L} \left(\mathfrak {D} _ {x, y}; \mathrm{E}\right) = \mathfrak {D} _ {x, y} ^ {\prime} \varepsilon \mathrm{E} = \left(\mathfrak {D} _ {x} ^ {\prime} \varepsilon \mathfrak {D} _ {y} ^ {\prime}\right) \varepsilon \mathrm{E},
$$

en vertu du théorème des noyaux (proposition 25).

D'autre part, on a aussi :

$$
\mathfrak {D} _ {x} ^ {\prime} \left(\mathfrak {D} _ {y} ^ {\prime} (\mathrm{E})\right) = \mathfrak {L} \left(\mathfrak {D} _ {x}; \mathfrak {D} _ {y} ^ {\prime} (\mathrm{E})\right) = \mathfrak {D} _ {x} ^ {\prime} \in \mathfrak {D} _ {y} ^ {\prime} (\mathrm{E}) = \mathfrak {D} _ {x} ^ {\prime} \in \left(\mathfrak {D} _ {y} ^ {\prime} \in \mathrm{E}\right).
$$

Si alors E est quasi-complet, la proposition 7 du § 1 montre que tous ces espaces peuvent être identifiés, et aussi s'écrire

$$
\mathfrak {D} _ {x} ^ {\prime} \in \mathfrak {D} _ {y} ^ {\prime} \in \mathrm{E} = \varepsilon (\mathfrak {D} _ {x} ^ {\prime}, \mathfrak {D} _ {y} ^ {\prime}, \mathrm{E}), \quad \text { ou } \quad (\mathfrak {D} _ {x} ^ {\prime} \otimes \mathfrak {D} _ {y} ^ {\prime} \otimes \mathrm{E}) _ {\epsilon} ^ {\cap},
$$

parce que $\mathfrak{D}_x'$ et $\mathfrak{D}_y'$ ont la propriété d'approximation stricte (corollaire de la proposition 3 des préliminaires, et corollaire 2 de la proposition 11 du § 1).

De même on a toujours

$$
\mathfrak {D} _ {\gamma , x} ^ {\prime} (\mathrm{E}) = \mathscr {L} (\mathfrak {D} _ {\gamma , x}; \mathrm{E}) = \mathfrak {D} _ {\gamma , x} ^ {\prime} \varepsilon \mathrm{E} = (\mathfrak {D} _ {\gamma} ^ {\prime} \varepsilon \mathfrak {D} _ {x} ^ {\prime}) \varepsilon \mathrm{E},
$$

et

$$
\mathfrak {D} _ {y} ^ {\prime} \left(\mathfrak {D} _ {x} ^ {\prime} (\mathrm{E})\right) = \mathscr {L} \left(\mathfrak {D} _ {y}; \mathfrak {D} _ {x} ^ {\prime} (\mathrm{E})\right) = \mathfrak {D} _ {y} ^ {\prime} \varepsilon \mathfrak {D} _ {x} ^ {\prime} (\mathrm{E}) = \mathfrak {D} _ {y} ^ {\prime} \varepsilon \left(\mathfrak {D} _ {x} ^ {\prime} \varepsilon \mathrm{E}\right),
$$

et, si E est quasi-complet, tous ces espaces sont identiques, et identiques à

$$
\mathfrak {D} _ {\gamma} ^ {\prime} \varepsilon \mathfrak {D} _ {x} ^ {\prime} \varepsilon \mathrm{E} = \varepsilon (\mathfrak {D} _ {\gamma} ^ {\prime}, \mathfrak {D} _ {x} ^ {\prime}, \mathrm{E}) = (\mathfrak {D} _ {\gamma} ^ {\prime} \otimes \mathfrak {D} _ {x} ^ {\prime} \otimes \mathrm{E}) _ {\varepsilon} ^ {\cap},
$$

et alors la symétrie s permet de passer de la première catégorie d'espaces à la seconde.

De plus, toujours si E est quasi-complet, $\mathfrak{D}_{x,y}^{\prime}(\mathrm{E}) = \mathfrak{D}_{x}^{\prime}\in\mathfrak{D}_{y}^{\prime}\in\mathrm{E}$ n'est autre que l'espace des applications bilinéaires de $\mathfrak{D}_{x}\times\mathfrak{D}_{y}$ dans E, hypocontinues par rapport aux parties bornées, muni

de la topologie de la convergence uniforme sur les produits de parties bornées de $\mathfrak{D}_{x}$ et $\mathfrak{D}_{y}$ (corollaire 2 de la proposition 7, avec $L_{1} = \mathfrak{D}_{x}^{\prime}, L_{2} = \mathfrak{D}_{y}^{\prime}, M = E$).

Enfin rappelons que, si $\mathcal{H}_{x}$ et $\mathfrak{K}_{y}$ sont des espaces de distributions, on a les identifications et isomorphismes suivants (si E est quasi complet):

$$
\left(\mathcal {H} _ {x} \in \mathcal {K} _ {y}\right) \varepsilon \mathrm{E} = \mathcal {H} _ {x} \varepsilon \left(\mathcal {K} _ {y} \varepsilon \mathrm{E}\right) \approx \left(\mathcal {K} _ {y} \varepsilon \mathcal {H} _ {x}\right) \varepsilon \mathrm{E} = \mathcal {K} _ {y} \varepsilon \left(\mathcal {H} _ {x} \varepsilon \mathrm{E}\right),
$$

l'isomorphisme étant la symétrie s.

## § 5. Distributions sommables.

Rappelons d'abord quelques propriétés, dont nous nous servirons désormais sans référence dans tout ce paragraphe.

Le dual de l'espace $\mathcal{R}^{\bullet}$ des fonctions indéfiniment dérivables sur $R^{n}$, convergeant vers 0 à l'infini ainsi que chacune de leurs dérivées, est l'espace $\mathcal{D}_{L}^{\prime}$ des distributions sommables sur $R^{n}$.

Il pourra être muni de la topologie $(\mathfrak{D}_{\mathrm{L}^{\prime}})_{c}$ de la convergence uniforme sur les parties compactes de $\mathcal{B}^{*}$ (auquel cas son dual est $\mathcal{B}^{*}$), ou de la topologie forte $(\mathfrak{D}_{\mathrm{L}^{\prime}})_{b}$, que nous noterons simplement $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}$. Le dual de $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}$, ou bidual de $\mathcal{B}^{*}$, est l'espace $\mathcal{B}$ des fonctions indéfiniment dérivables sur $\mathbb{R}^{n}$, bornées ainsi que chacune de leurs dérivées. $\mathcal{B}$ peut être muni de la topologie forte de dual de $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}$, que nous noterons simplement $\mathcal{B}$, ou de la topologie $\mathcal{B}_{c}(^{1})$ de la convergence uniforme sur les parties compactes de $(\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}): (\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})_{c}^{\prime} = \mathcal{B}_{c}$. $\mathcal{B}$ n'est pas un espace de distributions normal, et son dual n'est pas un espace de distributions; mais $\mathcal{B}_{c}$ est strictement normal et a pour dual $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}$. Toute partie bornée de $\mathcal{B}$ est contenue dans l'adhérence, pour la topologie $\sigma(\mathcal{B}, \mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})$, donc pour la topologie $\mathcal{B}_{c}$, d'une partie $\mathcal{B}$-bornée de $\mathcal{D} \subset \mathcal{B}^{*}$ (par troncature), donc $\mathcal{B}^{*}$ est un espace de Fréchet distingué, et $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}$ est bornologique et tonnelé ($^{2}$); alors toute partie bornée de $\mathcal{B}$ est équicontinue sur $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}$. La topologie de $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}$ est indifféremment celle de la convergence uniforme sur les parties bornées de $\mathcal{B}^{*}$ ou de $\mathcal{B}$.

Les parties bornées de $\mathcal{B}_{c}$ sont identiques aux parties bornées

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{R}_c$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) L'espace $\mathcal{R}_{c}$ a été étudié systématiquement dans Schwartz [1], pages 99-102.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) GROTHENDIECK [2], théorème 7, page 73.</span></small>

de $\mathcal{R}$ (car les parties bornées de $\mathcal{R}_c$ sont a fortiori bornées dans $\sigma(\mathcal{R};\mathcal{D}_{\mathrm{L}'}')$; mais $\mathcal{D}_{\mathrm{L}'}'$ est complet comme dual de l'espace de Fréchet $\mathcal{R}^*$, et, dans le dual fort $\mathcal{R}$ de l'espace complet $\mathcal{D}_{\mathrm{L}'}'$, toute partie faiblement bornée est fortement bornée (1)), donc équicontinues sur $\mathcal{D}_{\mathrm{L}'}'$, et par suite relativement compactes dans $(\mathcal{D}_{\mathrm{L}'}')_c' = \mathcal{R}_c$ d'après Ascoli; alors, sur ces parties bornées, la topologie est identique à la topologie plus faible induite par 6 (ou $\mathcal{D}'$), et $(\mathcal{B}_c)'_c = \mathcal{D}_{\mathrm{L}'}'$.

La dualité entre $\mathcal{D}_{\mathrm{L}}^{\prime}$ et $\mathcal{B}$ peut se définir par l'intégrale

$$
(\mathbf {T}, \varphi) \rightarrow \mathbf {T} (\varphi) = \int_ {\mathbb {R} ^ {n}} \mathbf {T} (x) \varphi (x) d x.
$$

L'intégrale $\mathbf{T} \to \int_{\mathbb{R}^n} \mathbf{T} = \mathbf{T}(1)$ est une forme linéaire continue sur $\mathfrak{D}_{\mathbf{L}^1}'$ (puisque $1 \in \mathcal{B} = (\mathfrak{D}_{\mathbf{L}^1}')'$), mais discontinue sur $(\mathfrak{D}_{\mathbf{L}^1}')_c$, puisque $1 \notin \mathcal{B} = ((\mathfrak{D}_{\mathbf{L}^1}')')'$.

$\mathcal{B}^{\bullet}$ et $\mathcal{B}$ sont des espaces de Fréchet. $\mathcal{B}^{\bullet}$ a la propriété d'approximation par troncature et régularisation (corollaire de la proposition 3 des préliminaires), donc est strictement normal et a la propriété d'approximation stricte, et $(\mathcal{D}_{\mathrm{L}^{1}}^{\prime})_{\mathrm{e}}$ a les mêmes propriétés (corollaire 1 de la proposition 4 des préliminaires).

Ensuite $\mathcal{D}_{\mathrm{L}^{\prime}}$ a la propriété d'approximation par troncature et régularisation, donc est strictement normal et a la propriété d'approximation stricte, et $\mathcal{B}_c$ a les mêmes propriétés, d'après la même suite de raisonnements. $(\mathcal{D}_{\mathrm{L}^{\prime}}^{\prime})_c$ et $\mathcal{B}_c$ ont la propriété ($\varepsilon$) (voir pages 54 et 56). Enfin $\mathcal{B}^{\bullet}$, $\mathcal{B}, (\mathcal{D}_{\mathrm{L}^{\prime}}^{\prime})_c$, $\mathcal{D}_{\mathrm{L}^{\prime}}^{\prime}$, $\mathcal{B}_c$ sont complets ($^2$). La proposition 8 du § 1 montre alors qu'une application linéaire de $\mathcal{B}_c$ dans un espace localement convexe M, dont les restrictions aux parties bornées de $\mathcal{B}$ sont continues pour la topologie induite par $\varepsilon$, est continue.

Les espaces identiques ou isomorphes

$$
\left(\mathfrak {D} _ {\mathrm{L} ^ {1}} ^ {\prime}\right) _ {c} (\mathrm{E}) = \left(\mathfrak {D} _ {\mathrm{L} ^ {1}} ^ {\prime}\right) _ {c} \otimes_ {\varepsilon} \mathrm{E} (^ {3}) = \mathfrak {L} _ {c} \left(\mathfrak {B} ^ {*}; \mathrm{E}\right) (^ {4}) \approx \mathfrak {L} _ {\varepsilon} \left(\mathrm{E} _ {c} ^ {\prime}; \left(\mathfrak {D} _ {\mathrm{L} ^ {1}} ^ {\prime}\right) _ {c}\right)
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">B</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{B}_c$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) DIEUDONNÉ-SCHWARTZ [1], proposition 7 page 73, et BOURBAKI [2], proposition 1 page 86.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathfrak{D}_{\mathbf{L}}^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$(\mathfrak{D}_{\mathbf{L}^{1}}^{\prime})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) $\mathcal{B}^{\bullet}$ et $\mathcal{B}$ sont des espaces de Fréchet, $\mathcal{D}_{\mathrm{L}}^{\prime}$, est le dual fort d'un Fréchet, $(\mathcal{D}_{\mathrm{L}}^{\prime})_{\mathrm{c}}$ et $\mathcal{R}_{\mathrm{c}}$ sont des duals d'espaces bornologiques, munis de la topologie de la convergence uniforme sur les parties compactes (BOURBAKI [2], exercice 18, page 37. Voir aussi SCHWARTZ [1], page 101).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">§ 2.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(4) Proposition 13 du § 2.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(3) Corollaire 1 de la proposition 11.</span></small>

ne sont que d'un intérêt limité; car l'intégrale d'une distribution appartenant à de tels espaces n'aura pas de sens. Plus précisément, si $\vec{T} \in \mathcal{L}(\mathcal{B}^{\bullet}; E)$, sa bitransposée $^{u}\vec{T}$ sera une application linéaire continue de $(\mathcal{B}^{\bullet})'' = \mathcal{B}$ dans $E''$, et on pourra poser $\int_{\mathbb{R}^{n}} T = ^{u}\vec{T}(1) \in E''$. Il n'y aura aucun espoir de pouvoir remplacer $E''$ par $E$; car si nous prenons pour $E$ l'espace $\mathcal{B}^{\bullet}$ lui-même, et pour $\vec{T}$ l'application identique de $\mathcal{B}^{\bullet}$, alors $^{u}\vec{T}$ est l'application identique de $\mathcal{B}$, et alors $\int_{\mathbb{R}^{n}} \vec{T} = 1 \in \mathcal{B}$ mais $\in \mathcal{B}^{\bullet}$.

L'espace $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}$ a la propriété d'approximation stricte, donc $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}(\mathrm{E}) = \mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}\widehat{\otimes}_{\epsilon}\mathrm{E}\approx \mathcal{L}_{\epsilon}(\mathrm{E}_{c}^{\prime};\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})$. Mais il ne possède pas la propriété $(\varepsilon)$: si une distribution $\vec{T}$ à valeurs dans E est scalairement dans $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}$, elle est dans $(\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})_{c}(\mathrm{E})$ et non nécessairement dans $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}(\mathrm{E})$ qui est plus petit [si nous reprenons l'exemple ci-dessus où $\vec{T}$ est l'application identique de $\mathcal{B}^{\bullet}$, $t\vec{T}$ est l'application identique de $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}$, elle n'est pas continue de $\mathrm{E}_{c}^{\prime} = (\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})_{c}$ dans $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}$. Donc $\vec{T}$ est scalairement dans $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}$, mais non dans $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}(\mathrm{E})]$. Malgré ce désavantage, c'est bien $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}(\mathrm{E})$ l'espace intéressant, sur lequel on peut définir l'intégrale.

DÉFINITION. — On appelle espace des distributions sommables sur R$^{n}$, à valeurs dans E (non nécessairement quasi-complet), l'espace topologique

$$
\mathfrak {D} _ {\mathbf {L} ^ {1}} ^ {\prime} (\mathbf {E}) = \mathfrak {D} _ {\mathbf {L} ^ {1}} ^ {\prime} \varepsilon \mathbf {E} \approx \mathscr {L} _ {\varepsilon} \left(\mathrm{E} _ {c} ^ {\prime}; \mathfrak {D} _ {\mathbf {L} ^ {1}} ^ {\prime}\right) (^ {1}).
$$

C'est aussi l'espace $\mathfrak{L}_{b}(\mathfrak{R}_{c};\mathrm{E})$; si E est quasi-complet, c'est le sous-espace de $\mathfrak{D}'(\mathrm{E})$ formé des applications continues sur les parties $\mathfrak{B}$-bornées de $\mathfrak{D}$ munies de la topologie induite par $\mathcal{E}$.

La fin de la définition se voit immédiatement: on a en effet $\mathfrak{D}_{\mathrm{L}'}' \in \mathrm{E} = \mathcal{L}_{\varepsilon}((\mathfrak{D}_{\mathrm{L}'}')_{c}'; \mathrm{E})$, mais $(\mathfrak{D}_{\mathrm{L}'}')_{c}' = \mathcal{R}_{c}$, et les parties équi- continues de $(\mathfrak{D}_{\mathrm{L}'}')'$ sont les parties bornées de $\mathcal{B}$ ou $\mathcal{B}_{c}$, puisque $\mathfrak{D}_{\mathrm{L}}'$ est tonnelé. D'autre part, soit $\tilde{\mathrm{T}}$ une distribution à valeurs dans E, dont la restriction à toute partie $\mathcal{B}$-bornée B de $\mathcal{D}$ soit continue pour la topologie induite par $\varepsilon$ donc par $\mathcal{B}_{c}$.

Si E est quasi-complet, $\overline{\mathbf{T}}$ se prolonge en une application continue, de $\overline{\mathbf{B}}$, adhérence de B dans $\mathcal{R}_c$, dans E. Comme toute partie bornée de $\mathcal{R}_c$ est contenue dans l'adhérence d'une

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Nous appelons ici sommables les distributions que nous appelions strictement sommables dans SCHWARTZ [2], exposé 21, définition 8, page 5.</span></small>

(I, 5; 1)

partie B-bornée de D, T se prolonge finalement en une application linéaire de  $B_{c}$  dans E, dont les restrictions aux parties bornées de  $B_{c}$  sont continues, donc continue, et  $T \in \mathcal{L}(\mathcal{B}_{c}; E)$ .

DÉFINITION. — L'intégrale $\int_{\mathbb{R}^{n}} \vec{\mathrm{T}} = \int_{\mathbb{R}^{n}} \vec{\mathrm{T}}(x) dx$ de $\vec{\mathrm{T}} \in \mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}(\mathrm{E})$ (E non nécessairement quasi-complet) est l'élément $\vec{\mathrm{T}}(1)$ de $\mathrm{E}(1 \in \mathfrak{B}_{c})$.

PROPOSITION 36. — L'intégrale, application linéaire continue de $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}(\mathrm{E})$ dans E (E non nécessairement quasi-complet), est l'application $\int_{\mathbb{R}^{n}} \otimes \mathrm{I}_{\mathrm{E}}$ de $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime} \in \mathrm{E}$ dans C $\varepsilon \mathrm{E} = \mathrm{E}$.

Si $\nu$ est une application linéaire continue de E dans F (non nécessairement quasi-complet), alors $\nu(\vec{\mathbf{T}}) \in \mathfrak{D}_{\mathbf{L}'}^{\prime}(\mathbf{F})$, et

$$
\int_ {\mathbf {R} ^ {n}} \nu (\mathbf {T}) = \nu \left(\int_ {\mathbf {R} ^ {n}} \vec {\mathbf {T}}\right).
$$

En particulier, pour tout $\vec{e'} \in \mathbf{E}'$:

$$
\int_ {\mathbb {R} ^ {n}} \langle \vec {\mathrm{T}}, \vec {e ^ {\prime}} \rangle = \left\langle \int_ {\mathbb {R} ^ {n}} \vec {\mathrm{T}}, \vec {e ^ {\prime}} \right\rangle .\tag{I, 5; 2}
$$

Le fait que l'intégrale et l'application $\int_{\mathbb{R}^{n}} \otimes I_{E}$ coïncident est trivial (remarque 1°, page 35 du § 1).

Le fait que $\nu(\vec{\mathbf{T}}) = (\mathrm{I}_{\mathfrak{D}_{\mathrm{L}^{\prime}}}\otimes \nu)(\vec{\mathbf{T}})\in \mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}(\mathrm{F})$ résulte de la proposition 1 du § 1. D'après la remarque $1^{\circ}$ de la page 35, on a, pour toute $\vec{\mathbf{T}}\in \mathscr{L}(\mathfrak{B}_c;\mathrm{E}): \nu (\mathbf{T}) = \nu \circ \vec{\mathbf{T}}\in \mathscr{L}(\mathfrak{B}_c;\mathrm{F})$; on en déduit $\int_{\mathbb{R}^n}\nu (\vec{\mathbf{T}}) = \nu \cdot \vec{\mathbf{T}}(1) = \nu \int_{\mathbb{R}^n}\vec{\mathbf{T}}$, ce qui est (I, 5; 1).

Remarque. — Soit $\vec{T}$ une distribution scalairement sommable. Comme $(\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})_{c}$ a la propriété $(\varepsilon)$, $\vec{T}$ appartient, si E est quasi-complet, à $(\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})_{c}\mathrm{E} = \mathfrak{L}(\mathfrak{B}^{*};\mathrm{E})$. Alors sa transposée $^t\vec{T}$ est continue de $\mathrm{E}_c^\prime$ dans $(\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})_{c}$, mais aussi de $\mathrm{E}_b^\prime$ dans $(\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})_b = \mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}$; si dans E les parties bornées sont relativement compactes, en particulier si E est un espace de Montel, $\mathrm{E}_b^\prime = \mathrm{E}_c^\prime$, donc $^t\vec{T} \in \mathfrak{L}(\mathrm{E}_c^\prime; \mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})$, et $\vec{T}$ est sommable.

Nous pouvons maintenant compléter ce que nous avons dit page 72.

PROPOSITION 37. — Soit H un espace de distributions normal (non nécessairement quasi-complet), tel que tout $\alpha \in \mathcal{H}$ soit un multiplicateur (1) de $\mathcal{H}_{c}^{\prime}$ dans $\mathfrak{D}_{\mathbf{L}}^{\prime}$. Alors, pour toute $\vec{T} \in \mathcal{H}_{c}^{\prime}(\mathbf{E})$

(1) Voir page 69.

(E non nécessairement quasi-complet), $\alpha\vec{T}$ est sommable, $\vec{T} \to \alpha\vec{T}$ est continue de $\mathcal{H}_{c}^{\prime}(E)$ dans $\mathcal{D}_{L^{1}}^{\prime}(E)$, et l'on a

$$
(\mathbf {I}, 5; 3)
$$

$$
\vec {\mathrm{T}} (\alpha) = \int_ {\mathbf {R} ^ {n}} \alpha \mathrm{T}
$$

Remarquons d'abord que $\alpha$ est multiplicateur de $\mathcal{H}_{c}^{\prime}$ dans $\mathfrak{D}_{\mathrm{L}^{1}}^{\prime}$, si et seulement s'il est multiplicateur de $\mathcal{B}_{c}$ dans $\mathcal{H}$ (par transposition, si $\alpha$ est multiplicateur de $\mathcal{B}_{c}$ dans $\mathcal{H}$, il est multiplicateur de $\mathcal{H}_{c}^{\prime}$ dans $(\mathcal{B}_{c})_{c}^{\prime} = \mathcal{D}_{\mathrm{L}^{1}}^{\prime}$; si $\alpha$ est multiplicateur de $\mathcal{H}_{c}^{\prime}$ dans $\mathcal{D}_{\mathrm{L}^{1}}^{\prime}$, il est multiplicateur de $(\mathcal{D}_{\mathrm{L}^{1}}^{\prime})_{c}^{\prime} = \mathcal{B}_{c}$ dans $(\mathcal{H}_{c}^{\prime})_{c}^{\prime}$, donc a fortiori dans $\mathcal{H}$).

Alors $\alpha$ est multiplicateur de $\mathcal{H}_{c}^{\prime}(\mathrm{E})$ dans $\mathcal{D}_{\mathrm{L}^{\prime}}^{\prime}(\mathrm{E})$, de sorte que, pour toute $\vec{T} \in \mathcal{H}_{c}^{\prime}(\mathrm{E})$, $\alpha \vec{T}$ est bien sommable. On a, d'après la formule (I, 3; 6), pour toute $\varphi \in \mathcal{B}_{c}$,

$$
(\mathrm{I}, 5; 4)
$$

$$
\vec {\mathbf {T}} (\alpha \varphi) = \alpha \vec {\mathbf {T}} (\varphi),
$$

le premier membre ayant un sens parce que $\alpha\varphi\in\mathcal{H}=(\mathcal{H}_{c}^{\prime})'$ et $\vec{T}\in\mathcal{L}((\mathcal{H}_{c}^{\prime})_{c}^{\prime};\mathrm{E})$, et le deuxième parce que $\varphi\in\mathcal{B}$ et $\alpha\vec{T}\in\mathcal{D}_{L^{1}}^{\prime}(\mathrm{E})=\mathcal{L}(\mathcal{B}_{c};\mathrm{E})$.

En faisant $\varphi = 1$, on obtient (I, 5; 3).

COROLLAIRE. — Soit E quasi-complet. Si $\vec{T} \in \mathfrak{D}'(E)$ est scalairement dans $\mathfrak{D}_{L^p}'$, $1 \leqslant p \leqslant \infty$, et si $\alpha \in \mathfrak{D}_{L^p}\left(\frac{1}{p} + \frac{1}{p'} = 1\right)$ pour $p \neq 1$, $\alpha \in \mathfrak{B}'$ pour $p = 1$, alors $\alpha \vec{T}$ est sommable, et $\vec{T} \to \alpha \vec{T}$ est continue de $(\mathfrak{D}_{L^p}')_c(E)$ dans $\mathfrak{D}_{L^1}'(E)$.

Comme en effet $(\mathfrak{D}_{\mathbf{L}^p}^{\prime})_c$ a la propriété $(\varepsilon)$ (exemple, page 54), $\vec{T}$ est dans $(\mathfrak{D}_{\mathbf{L}^p}^{\prime})_e(\mathrm{E})$. Mais la multiplication par $\alpha$ est une application linéaire de $\mathcal{B}_c$ dans $\mathfrak{D}_{\mathbf{L}^p}$, pour $p \neq 1$, dans $\mathcal{B}^*$ pour $p = 1$, continue sur les parties bornées de $\mathcal{B}_c$ (comme on le voit trivialement, parce que, sur ces parties, la topologie est induite par $\mathcal{E}$), donc sur $\mathcal{B}_c$; alors $\alpha$ est un multiplicateur de $(\mathfrak{D}_{\mathbf{L}^p}^{\prime})_c$ dans $\mathfrak{D}_{\mathbf{L}'}^{\prime}$, et par suite de $(\mathfrak{D}_{\mathbf{L}^p}^{\prime})_c(\mathrm{E})$ dans $(\mathfrak{D}_{\mathbf{L}'}^{\prime})(\mathrm{E})$.

Distributions partiellement sommables en x.

DÉFINITION. — Une distribution $\mathbf{T} \in \mathcal{D}_{x,\gamma}^{\prime}(\mathbf{E})$ est dite partiellement sommable en $x$, si elle appartient à

$$
(\mathfrak {D} _ {\mathrm{L} ^ {1}} ^ {\prime}) _ {x} \varepsilon \mathfrak {D} _ {y} ^ {\prime} \varepsilon \mathrm{E} = (\mathfrak {D} _ {\mathrm{L} ^ {1}} ^ {\prime}) _ {x} (\mathfrak {D} _ {y} ^ {\prime} (\mathrm{E})) = ((\mathfrak {D} _ {\mathrm{L} ^ {1}} ^ {\prime}) _ {x} \widehat {\otimes} \mathfrak {D} _ {y} ^ {\prime}) (\mathrm{E}).
$$

L'intégrale partielle en $x$, notée $\vec{\mathbf{T}} \to \int_{\mathbf{x}^l} \vec{\mathbf{T}}(x, \hat{y}) \, dx$, est l'opération linéaire continue $\int_{\mathbf{x}^l} \otimes \mathbf{I}_{\mathfrak{D}_y^*(\mathbf{E})}$ de $(\mathfrak{D}_{\mathbf{L}^l}^{\prime})_x(\mathfrak{D}_y^{\prime}(\mathbf{E}))$ dans $\mathfrak{D}_y^{\prime}(\mathbf{E})$, c'est aussi l'application $\int_{\mathbf{x}^l} \otimes \mathbf{I}_y \otimes \mathbf{I}_\mathbf{E}$ de $(\mathfrak{D}_{\mathbf{L}^l}^{\prime})_x \in \mathfrak{D}_y^{\prime} \in \mathbf{E}$ dans $\mathfrak{D}_y^{\prime} \in \mathbf{E}$, ou l'application $\mathbf{I}_y \otimes \int_{\mathbf{x}^l} de \mathfrak{D}_y^{\prime} \in ((\mathfrak{D}_{\mathbf{L}^l}^{\prime})_x(\mathbf{E}))$ dans $\mathfrak{D}_y^{\prime} \in \mathbf{E}$.

Si E est le corps des scalaires, on remarquera que $\mathfrak{D}_{y}^{\prime}$ est un espace de Montel; donc (remarque, page 129, en y remplaçant E par $\mathfrak{D}_{y}^{\prime}$) une distribution $\mathbf{T} \in \mathfrak{D}_{x,y}^{\prime}$ est partiellement sommable en $x$, si et seulement si elle vérifie l'une quelconque des conditions équivalentes suivantes :

$1^{\circ} u \rightarrow u \cdot T$ est continue de $D_x$, muni de la topologie induite par $R_x'$, dans $D_y'$;

2° Pour toute  $\nu\in\mathfrak{D}_{y}$ , T· $\nu$  est dans  $(\mathfrak{D}_{L^{1}}^{\prime})_{x}$ .

Dans ces conditions, l'intégrale en x peut être définie par

$$
\begin{array}{r l} (I, 5; 5) & \int_ {\mathbf {Y} ^ {m}} \nu (y) d y \int_ {\mathbf {X} ^ {l}} \mathrm{T} (x, y) d x = \int_ {\mathbf {X} ^ {l}} (\mathrm{T} \cdot \nu) \\ & = \int_ {\mathbf {X} ^ {l}} d x \int_ {\mathbf {Y} ^ {m}} \mathrm{T} (x, y) \nu (y) d y, \quad \text { pour   toute } \end{array}
$$

$$
\nu \in \mathcal {D} _ {\gamma}
$$

Cette notion d'intégrale partielle permet d'écrire commodément beaucoup de formules. Par exemple :

$^{10}$ Opérations intégrales définies par les noyaux.

On désire pouvoir écrire, pour $u \in \mathfrak{D}_{x}$ et $\mathrm{T} \in \mathfrak{D}_{x,y}^{\prime}$, $u \cdot \mathrm{T}$ suivant (I, 4; 7):

$$
(u \cdot \mathbf {T}) = \int_ {\mathbf {x} ^ {l}} u (x) \mathbf {T} (x, \hat {y}) d x.
$$

Le produit multiplicatif $u(\hat{x})\mathrm{T}(\hat{x},\hat{y})$ est dans $\mathfrak{E}_x' \widehat{\otimes} \mathfrak{D}_y'$, donc partiellement sommable en $x$, et le second membre a bien un sens; cette formule est un cas particulier de (I, 5; 3) pour $\alpha = u$, $\mathcal{H} = \mathfrak{D}_x$ et $\mathrm{E} = \mathfrak{D}_y'$.

On a une écriture analogue (I, 4; 4) pour T·ν, ce qui permet d'écrire la formule (I, 4; 6). Nous avions à ce moment déjà justifié ces écritures, parce que seul $\mathcal{E}'(E)$ et non $\mathcal{D}_{L'}'(E)$ intervenait.

## $2^{0}$  Convolution.

Soient S et T deux distributions sur  $R^{n}$ . On peut définir le produit  $\mathrm{S}(\hat{x}-\hat{y})\mathrm{T}(\hat{y})$ , sans aucune condition sur S et T, comme image du produit tensoriel  $\mathrm{S}(\hat{\xi})\otimes\mathrm{T}(\hat{\eta})$  par le changement de variables

$$
\left\{ \begin{array}{l} x = \xi + \eta \\ y = \eta \end{array} \right\} \quad \text { ou } \quad \left\{ \begin{array}{l} \xi = x - y \\ \eta = y \end{array} \right\}.
$$

Autrement dit, par définition, si $u \in \mathfrak{D}_{x}$, $\nu \in \mathfrak{D}_{y}$:

$$
\begin{array}{r l} \iint_ {\mathbf {R} ^ {n} \times \mathbf {R} ^ {n}} \mathrm{S} (x - y) \mathrm{T} (y) u (x) v (y) d x d y \\ = \iint_ {\mathbf {R} ^ {n} \times \mathbf {R} ^ {n}} (\mathrm{S} (\xi) \otimes \mathrm{T} (\eta)) u (\xi + \eta) v (\eta) d \xi d \eta , \end{array} \tag {I,5;7}
$$

égal, d'après Fubini (¹), à :

$$
(I, 5; 8) \quad \int_ {\mathbb {R} ^ {n}} T (\eta) \nu (\eta) d \eta \int_ {\mathbb {R} ^ {n}} S (\xi) u (\xi + \eta) d \xi = (\check {S} * u) T \cdot \nu ,
$$

de sorte que, en tant que noyau, S( $\hat{x} - \hat{y}$ )T( $\hat{y}$ ) vérifie

$$
(\mathrm{I}, 5; 9)
$$

$$
u \cdot (\mathrm{S} (\hat {x} - \hat {y}) \mathrm{T} (\hat {y})) = (\check {\mathrm{S}} * u) \mathrm{T}.
$$

On voit alors aisément que, dans tous les cas classiques où la convolution a un sens, cette distribution  $\mathrm{S}(\hat{x}-\hat{y})\mathrm{T}(\hat{y})$  est partiellement sommable en y, et que son intégrale en y est le produit de convolution :

$$
(\mathbf {I}, 5; \mathbf {1 0})
$$

$$
\mathrm{S} * \mathrm{T} = \int_ {\mathbb {R} ^ {n}} \mathrm{S} (\hat {x} - y) \mathrm{T} (y) d y.
$$

Prenons, par exemple, $\mathbf{S} \in \mathcal{S}'$, $\mathbf{T} \in \mathcal{O}_{\mathbf{C}}'$.

Pour vérifier que $\mathrm{S}(\hat{x}-\hat{y})\mathrm{T}(\hat{y})$ est sommable en $y$, nous devons vérifier que, pour toute $u\in\mathcal{D}_{x}$, la distribution $u\cdot(\mathrm{S}(\hat{x}-\hat{y})\mathrm{T}(\hat{y}))=(\check{\mathrm{S}}*u)\mathrm{T}$ est sommable. Mais $\check{\mathrm{S}}*u$ est le produit d'un polynome par une fonction appartenant à $\mathcal{B}$; comme $\mathrm{T}\in\mathcal{O}_{\mathrm{C}}^{\prime}$, le produit ($\check{\mathrm{S}}*u$)T est aussi dans $\mathcal{O}_{\mathrm{C}}^{\prime}$ donc sommable; et l'on a même, par conséquent, $\mathrm{S}(\hat{x}-\hat{y})\mathrm{T}(\hat{y})\in\mathcal{D}_{x}^{\prime}\widehat{\otimes}(\mathcal{O}_{\mathrm{C}}^{\prime})_{y}$.

Soit S fixé, et u borné dans  $D_{x}$ ; alors  $\check{S} * u$  est le produit d'un même polynome par une fonction qui reste bornée dans R; si alors T converge vers 0 dans  $O_{C}'$ , ( $\check{S} * u$ ) T converge vers 0 dans  $O_{C}'$ . Autrement dit,  $T \to S(\hat{x} - \hat{y}) T(\hat{y})$  est continue de  $O_{C}'$  dans  $D_{x}' \otimes (O_{C}')_{y} = \mathfrak{L}(D_{x}; (O_{C}')_{y})$ ; donc  $T \to \int_{R^{n}} S(\hat{x} - y) T(y) dy$  est continue de  $O_{C}'$  dans  $D'$ . Mais  $T \to S * T$  est continue de  $O_{C}'$  dans  $F'$  donc a fortiori dans  $D'$ ; et ces 2 applications coincident visiblement pour  $T \in D$  dense dans  $O_{C}'$  (formule (I, 4; 26), avec  $T = v$ ), donc pour  $T \in O_{C}'$  quelconque, ce qui prouve bien (I, 5; 10).

Nous laisserons au lecteur le soin de montrer que $(\mathrm{S},\mathrm{T})\to \mathrm{S}(\hat{x} -\hat{y})\mathrm{T}(\hat{y})$ est même une application bilinéaire de

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Schwartz [4], chapitre iv, § 3, théorème IV.</span></small>

$\mathcal{S}' \times \mathcal{O}_{\mathbf{C}}'$ dans $\mathcal{S}_x' \widehat{\otimes} (\mathcal{O}_{\mathbf{C}}')_y$, hypocontinue par rapport aux parties bornées (1).

3° Intégrales de Fourier vectorielles.

Soit $\vec{\mathbf{U}}\in\mathcal{G}_{x}^{\prime}(\mathbf{E})$. Montrons que son image de Fourier $\vec{\mathbf{V}}=\mathcal{F}\vec{\mathbf{U}}\in\mathcal{G}_{\xi}^{\prime}(\mathbf{E})$ peut s'écrire:

$$
(\mathrm{I}, 5; 1 1)
$$

$$
\vec {\mathrm{V}} (\widehat {\xi}) = \int_ {\mathbf {x} ^ {n}} \exp (- 2 i \pi x \widehat {\xi}) \vec {\mathrm{U}} (x) d x.
$$

Nous montrerons d'abord un lemme :

LEMME: $\exp (-2i\pi \hat{x}\hat{\xi})\in \mathcal{S}_x\widehat{\otimes}\mathcal{S}_{\xi}'$ et $\in \mathcal{S}_x^\prime \widehat{\otimes}\mathcal{S}_{\xi}$

Il suffit de montrer la première propriété. Pour cela, on remarque que, si $\varphi\in\mathfrak{D}_{\xi}$, l'intégrale

$$
(\mathrm{I}, 5; 1 2)
$$

$$
\int_ {\Xi^ {n}} \exp (- 2 i \pi \hat {x} \xi) \varphi (\xi) d \xi = \exp (- 2 i \pi \hat {x} \xi) \cdot \varphi
$$

représente $\mathcal{F}\varphi\in\mathcal{G}_{x}$, et que $\varphi\to\mathcal{F}\varphi$ est continue de $\mathcal{D}_{\xi}$, muni de la topologie induite par $\mathcal{G}_{\xi}$, dans $\mathcal{G}_{x}$, donc on a bien $s\left(\exp\left(-2i\pi\hat{x}\widehat{\xi}\right)\right)\in\mathcal{L}(\mathcal{G}_{\xi};\mathcal{G}_{x})$, donc $\exp\left(-2i\pi\hat{x}\widehat{\xi}\right)\in\mathcal{G}_{x}\widehat{\otimes}\mathcal{G}_{\xi}^{\prime}$.

Remarquons que, si l'on identifie $\mathcal{G}_{x}\widehat{\otimes}\mathcal{G}_{\xi}^{\prime}$ à $\mathcal{L}(\mathcal{G}_{x}^{\prime};\mathcal{G}_{\xi}^{\prime})$, l'opération définie par le noyau étudié est la transposée de $\mathcal{F}$, c'est donc encore $\mathcal{F}$:

$$
\mathrm{U} \rightarrow \mathcal {F} \mathrm{U} = \mathrm{V} = \mathrm{U} \cdot \exp (- 2 i \pi \hat {x} \hat {\xi}).
$$

La propriété (I, 5; 11) résulte alors, dans le cas scalaire E = C, de la proposition 37: on pose

$$
\begin{array}{c c} \mathcal {H} = \mathcal {G} _ {x} ^ {\prime}, & \mathcal {H} _ {c} ^ {\prime} = \mathcal {G} _ {x}, \quad \mathrm{E} = \mathcal {G} _ {\xi} ^ {\prime}, \\ \widetilde {\mathbf {T}} = \exp (- 2 i \pi \widehat {x} \widehat {\xi}) \in \mathcal {H} _ {c} ^ {\prime} (\mathrm{E}), & \alpha = \mathrm{U} \in \mathcal {G} _ {x} ^ {\prime} = \mathcal {H}. \end{array}
$$

Le produit $\alpha\vec{T}$ est sommable en $x$, et son intégrale est $\vec{T} \cdot \alpha = \mathcal{F}U$. Il suffit seulement de vérifier: $a)$ que la proposition 37 s'applique. La multiplication $[\alpha]$ est bien continue de $\mathscr{S}$ dans $\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime}$ et même dans $\mathcal{O}_{\mathrm{C}}^{\prime}$, puisque $\alpha = U \in \mathscr{S}^{\prime}$, ce qui permet de montrer que exp $(-2i\pi\hat{x}\hat{\xi})U(\hat{x})$ est non seulement dans $(\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})_x \otimes \mathscr{S}_{\xi}^{\prime}$, mais même dans $(\mathcal{O}_{\mathrm{C}}^{\prime})_x \otimes \mathscr{S}_{\xi}^{\prime}$;

b) que le produit multiplicatif défini par la proposition 37 coïncide avec celui qui est défini ici. Ce dernier est le produit, dans $\mathfrak{D}_{x,\xi}^{\prime}$, de $\exp\left(-2i\pi\hat{x}\hat{\xi}\right)\in\mathcal{E}_{x,\xi}$ par $\mathrm{U}(\hat{x})=\mathrm{U}(\hat{x})\otimes1(\hat{\xi})\in\mathfrak{D}_{x,\xi}^{\prime}$. Mais la multiplication $[\mathrm{U}_{x}]$ de $\mathcal{E}_{x}$ dans $\mathfrak{D}_{x}^{\prime}$ est continue, et la

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Consulter, pour toutes ces propriétés, Schwartz (5), chapitre VII, notamment théorèmes VI, IX, XI.</span></small>

multiplication par $\mathrm{U}(\hat{x}) \otimes 1(\hat{\xi})$ est l'opérateur $[\mathrm{U}_x] \otimes \mathrm{I}_\xi$ sur $\mathcal{E}_x \widehat{\otimes} \mathcal{E}_\xi$. La multiplication de la proposition 37 est l'opérateur $[\alpha] \otimes \mathrm{I_E} = [\mathrm{U}_x] \otimes \mathrm{I}_\xi$ sur $\mathcal{G}_x \widehat{\otimes} \mathcal{G}_\xi'$. Alors ces 2 opérateurs coincident sur l'élément exp $(-2i\pi \hat{x}\hat{\xi})$, car celui-ci est dans $\mathcal{E}_x \widehat{\otimes} \mathcal{D}_\xi'$, et les 2 opérateurs précédents sont les restrictions, sur les espaces considérés, de l'opérateur $[\mathrm{U}_x] \otimes \mathrm{I}_\xi$ sur $\mathcal{E}_x \widehat{\otimes} \mathcal{D}_\xi'$.

Cependant la proposition 37 ne démontre pas la formule (I, 5; 11), si $\vec{U}$ est à valeurs vectorielles.

Nous remarquons alors que $\vec{U} \in \mathcal{S}_{x}^{\prime} \otimes E$ est un multiplicateur continu de $\mathcal{S}_{x}$ dans $(\mathcal{O}_{C}^{\prime})_{x} \otimes E$ (car, lorsque $\vec{e}^{\prime}$ parcourt une partie équicontinue de $E^{\prime}$, $\langle \vec{U}, \vec{e}^{\prime} \rangle$ parcourt une partie bornée de $\mathcal{S}_{x}^{\prime}$, donc un ensemble équicontinu de multiplicateurs de $\mathcal{S}_{x}$ dans $\mathcal{O}_{C}^{\prime}$); c'est donc un multiplicateur continu de $\mathcal{S}_{x} \otimes \mathcal{S}_{\xi}^{\prime}$ dans $((\mathcal{O}_{C}^{\prime})_{x} \otimes \mathcal{S}_{\xi}^{\prime} \otimes E)_{\varepsilon}^{\circ}$, de sorte que le second membre de (I, 5; 11) est dans cet espace $((\mathcal{O}_{C}^{\prime})_{x} \otimes \mathcal{S}_{\xi}^{\prime} \otimes E)_{\varepsilon}^{\circ}$, donc partiellement sommable en $x$, et son intégrale en $x$ est dans $\mathcal{S}_{\xi}^{\prime} \otimes E$ (et, comme plus haut, les divers sens possibles du produit multiplicatif coïncident, car, si [\$\vec{U}\$] est le multiplicateur défini par \$\vec{U}\$ sur $\mathcal{E}_{x}$, ils coïncident tous deux avec la valeur de l'opérateur [\$\vec{U}\$] $\otimes I_{\xi}$ sur $\exp (-2i\pi \hat{x}\hat{\xi}) \in \mathcal{E}_{x} \otimes \mathcal{D}_{\xi}^{\prime}$). Il reste à montrer que le second membre de (I, 5; 11) est \$\vec{V}(\hat{\xi})\$. Or c'est démontré pour $E = C$. Pour $E$ quelconque, prenons $\vec{e}^{\prime} \in E^{\prime}$, alors:

(I, 5; 13)

$$
\begin{array}{r l} \left\langle \vec {e ^ {\prime}}, \int_ {\mathbf {x} ^ {n}} \exp (- 2 i \pi x _ {\xi} ^ {\hat {\xi}}) \vec {\mathrm{U}} (x) d x \right\rangle & = \int_ {\mathbf {x} ^ {n}} \exp (- 2 i \pi x _ {\xi} ^ {\hat {\xi}}) \left\langle \mathrm{U} (x), \vec {e ^ {\prime}} \right\rangle d x \\ & = \mathcal {F} \left\langle \vec {\mathrm{U}}, \vec {e ^ {\prime}} \right\rangle = \left\langle \mathcal {F} \vec {\mathrm{U}}, \vec {e ^ {\prime}} \right\rangle = \left\langle \vec {\mathrm{V}}, \vec {e ^ {\prime}} \right\rangle , \end{array}
$$

ce qui démontre complètement (I, 5; 11).

En remplaçant E par $\mathfrak{D}_{y}^{\prime}(\mathrm{E})$, on justifie la définition intégrale de la transformation de Fourier partielle; pour $\overline{\mathrm{U}}\in(\mathcal{G}_{x}^{\prime}\otimes\mathfrak{D}_{y}^{\prime}\otimes\mathrm{E})_{\varepsilon}^{n}$:

$$
\mathcal {F} _ {x} \vec {\mathrm{U}} = \int_ {\mathbf {x} ^ {n}} \exp (- 2 i \pi x \hat {\xi}) \mathrm{U} (x, \hat {y}) d x, \tag {I,5;14}
$$

qui appartient à $(\mathcal{S}_{\xi}^{\prime}\otimes \mathcal{D}_{y}^{\prime}\otimes \mathrm{E})_{\varepsilon}^{\circ}$; en outre

$$
\exp (- 2 i \pi \hat {x} \hat {\xi}) U (\hat {x}, \hat {y}) \in ((\mathcal {O} _ {\mathrm{C}} ^ {\prime}) _ {x} \otimes \mathscr {S} _ {\xi} ^ {\prime} \otimes \mathscr {D} _ {\gamma} ^ {\prime} \otimes E) _ {\epsilon} ^ {\cap}.
$$

Identité des espaces $(\mathfrak{D}_{\mathbf{L}^i}^{\prime})_{x,y}$ et $(\mathfrak{D}_{\mathbf{L}^i}^{\prime})_x\widehat{\otimes}_ {\pi}(\mathfrak{D}_{\mathbf{L}^i}^{\prime})_y.$

PROPOSITION 38. — Sur $X^l \times Y^m$, les espaces $(\mathfrak{D}_{\mathbf{L}^l}^{\prime})_{x,\gamma}$ et $(\mathfrak{D}_{\mathbf{L}^l}^{\prime})_x \widehat{\otimes}_\pi (\mathfrak{D}_{\mathbf{L}^l}^{\prime})_\gamma$ peuvent être identifiés, algébriquement et topologiquement; l'intégrale $\iint_{\mathbf{X}^l \times \mathbf{Y}^m}$ est le produit tensoriel des intégrales simples $\int_{\mathbf{X}^l} \otimes \int_{\mathbf{Y}^m}$.

Tout d'abord nous avons vu (proposition 17) que $\mathcal{R}_{x,y}^{\bullet} = \mathcal{R}_{x}^{\bullet}\in\mathcal{R}_{y}^{\bullet}$. Mais alors on sait (corollaire 4 de la proposition 2) que $(S_{x},T_{y})\to S_{x}\otimes T_{y}$ est une application bilinéaire de

$$
\left((\mathcal {B} _ {x} ^ {\bullet}) _ {c} ^ {\prime} = ((\mathcal {D} _ {\mathrm{L} ^ {1}} ^ {\prime}) _ {x}) _ {c}\right) \times \left((\mathcal {B} _ {y} ^ {\bullet}) _ {c} ^ {\prime} = ((\mathcal {D} _ {\mathrm{L} ^ {1}} ^ {\prime}) _ {y}) _ {c}\right)
$$

dans $(\mathcal{B}_{x,y})_{c}^{\prime} = ((\mathcal{D}_{L^{1}}^{\prime})_{x,y})_{c}$, $\varepsilon$-hypocontinue, donc en particulier séparément faiblement continue. Cela prouve d'abord que $(\mathcal{D}_{L^{1}}^{\prime})_{x} \otimes (\mathcal{D}_{L^{1}}^{\prime})_{y}$ est contenu dans $(\mathcal{D}_{L^{1}}^{\prime})_{x,y}$. Par ailleurs il est évidemment dense dans $(\mathcal{D}_{L^{1}}^{\prime})_{x,y}$, car $\mathcal{D}_{x,y}$ est dense, et que $\mathcal{D}_{x} \otimes \mathcal{D}_{y}$ est dense dans $\mathcal{D}_{x,y}$ pour la topologie $\mathcal{D}_{x,y}$, donc a fortiori pour la topologie induite par $(\mathcal{D}_{L^{1}}^{\prime})_{x,y}$. Si on prouve que, sur $(\mathcal{D}_{L^{1}}^{\prime})_{x} \otimes (\mathcal{D}_{L^{1}}^{\prime})_{y}$, la topologie $\mathcal{C}$ induite par $(\mathcal{D}_{L^{1}}^{\prime})_{x,y}$ coïncide avec la topologie $\pi$, l'identité algébrique et topologique de $(\mathcal{D}_{L^{1}}^{\prime})_{x,y}$ et de $(\mathcal{D}_{L^{1}}^{\prime})_{x} \otimes_{\pi} (\mathcal{D}_{L^{1}}^{\prime})_{y}$ sera démontrée. Mais $(\mathcal{D}_{L^{1}}^{\prime})_{x}, (\mathcal{D}_{L^{1}}^{\prime})_{y}, (\mathcal{D}_{L^{1}}^{\prime})_{x,y}$, sont des duals forts d'espaces de Fréchet $\mathcal{B}_{x}^{\bullet}, \mathcal{B}_{y}^{\bullet}, \mathcal{B}_{x,y}^{\bullet}$; donc l'application bilinéaire $(S_x, T_y) \to S_x \otimes T_y$, séparément faiblement continue, est continue (1); et comme $\pi$ est la topologie localement convexe la plus fine sur $(\mathcal{D}_{L^{1}}^{\prime})_{x} \otimes (\mathcal{D}_{L^{1}}^{\prime})_{y}$ pour laquelle cette application soit continue, $\pi$ est plus fine que $\mathcal{C}$. Il nous reste à montrer que $\mathcal{C}$ est plus fine que $\pi$.

Appelons $\mathcal{B}_1$ l'espace des formes bilinéaires continues sur $(\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_{x}\times (\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_{y};\pi$ est la topologie de la convergence uniforme sur les parties équicontinues de $\mathcal{B}_1$, tandis que $\mathfrak{C}$ est la topologie de la convergence uniforme sur les parties bornées de $\mathcal{B}_{x,y} = \mathcal{B}$.

Il suffit donc de montrer qu'on peut identifier $\mathcal{B}_1$ à un sous-espace de $\mathcal{B}$, la dualité de $(\mathcal{D}_{\mathrm{L}^{\prime}}^{\prime})_x \otimes (\mathcal{D}_{\mathrm{L}^{\prime}}^{\prime})_y$ avec $\mathcal{B}_1$ devenant la restriction à $\mathcal{B}_1$ de sa dualité avec $\mathcal{B}$, et que les parties équi-continues de $\mathcal{B}_1$ sont des parties bornées de $\mathcal{B}$ (la proposition étant alors démontrée, il en résultera d'ailleurs que $\mathcal{B}_1 = \mathcal{B}$, et que les parties équicontinues de $\mathcal{B}_1$ sont exactement les parties bornées de $\mathcal{B}$).

(1) DIEUDONNÉ-SCHWARTZ [1], théorème VIII, page 94.

Soit $\Theta\in\mathcal{B}_{1}$. $\Theta$ définit a fortiori une forme bilinéaire continue sur $\mathcal{E}_{x}^{\prime}\times\mathcal{E}_{y}^{\prime}$, donc un élément $\theta$ de $(\mathcal{E}_{x}^{\prime}\widehat{\otimes}\mathcal{E}_{y}^{\prime})^{\prime}=(\mathcal{E}_{x,y}^{\prime})^{\prime}=\mathcal{E}_{x,y}$. De plus, $\mathcal{E}^{\prime}$ étant dense dans $(\mathcal{D}_{L}^{\prime})$, $\theta$ détermine complètement $\Theta$, autrement dit $\Theta\to\theta$ permet d'identifier $\mathcal{B}_{1}$ à un sous-espace de $\mathcal{E}_{x,y}$.

Mais, pour $p$ et $q$ fixés, lorsque $\xi$ (resp. $\eta$) parcourt $\mathbf{X}^l$ (resp. $\mathbf{Y}^m$), $\mathrm{D}_x^p\delta (\hat{x}-\xi)$ (resp. $\mathrm{D}_y^q\delta (\hat{y}-\eta)$) reste borné dans $(\mathfrak{D}_{\mathbf{L}^i})_x$ (resp. $(\mathfrak{D}_{\mathbf{L}^i})_y)$, donc $\Theta$ ($\mathrm{D}_x^p\delta (\hat{x}-\xi)$, $\mathrm{D}_y^q\delta (\hat{y}-\eta)$) reste bornée, c'est-à-dire $\mathrm{D}_\xi^p\mathrm{D}_\eta^q\theta (\xi,\eta) = (-1)^{|p + q|}\Theta$ ($\mathrm{D}_x^q\delta (\hat{x}-\xi)$, $\mathrm{D}_y^q\delta (\hat{y}-\eta)$) reste borné; donc $\theta \in \mathcal{B}$, et $\mathcal{B}_i$ est bien identifié à un sous-espace de $\mathcal{B}$. Il faut montrer que cette identification respecte la dualité avec $(\mathfrak{D}_{\mathbf{L}^i})_x \otimes (\mathfrak{D}_{\mathbf{L}^i})_y$, autrement dit que, si $\mathrm{S} \in (\mathfrak{D}_{\mathbf{L}^i})_x$ et $\mathrm{T} \in (\mathfrak{D}_{\mathbf{L}^i})_y$, on a

$$
(I, 5; 1 5) \quad \Theta (S, T) = \iint_ {\mathbf {x} ^ {t} \times \mathbf {y} ^ {m}} (S (x) \otimes T (y)) \theta (x, y) d x d y.
$$

Or cette égalité est vraie pour $S \in \mathcal{E}_x'$ et $T \in \mathcal{E}_y'$, par définition même de $\theta$; $\mathcal{E}_x'$ et $\mathcal{E}_y'$ sont denses dans $(\mathfrak{D}_{L^1}')_x$ et $(\mathfrak{D}_{L^1}')_y$; $\Theta$ est continue sur $(\mathfrak{D}_{L^1}')_x \times (\mathfrak{D}_{L^1}')_y$; si donc on prouve que la forme bilinéaire sur $(\mathfrak{D}_{L^1}')_x \times (\mathfrak{D}_{L^1}')_y$, définie par $\theta$ au 2$^{\text{e}}$ membre, est aussi continue, l'identité des 2 membres de (I, 5; 15) sera bien prouvée.

Or, si S et T convergent vers 0 dans $(\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_{x}$ et $(\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_{y}$ respectivement, on sait que $\mathrm{S} \otimes \mathrm{T}$ converge vers 0 dans $(\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_{x,y}$, ce qui démontre notre assertion, puisque $0 \in \mathcal{R}_{x,y}$.

Soit enfin H une partie équicontinue de $\mathcal{R}_{1}$. Elle est en particulier bornée. Alors $\Theta(\mathrm{D}_{x}^{p}\delta(\hat{x}-\xi), \mathrm{D}_{y}^{q}\delta(\hat{y}-\eta)$, reste borné pour $\xi \in \mathrm{X}^{i}$, $\eta \in \mathrm{Y}^{m}$, $\Theta \in \mathrm{H}$; donc $\theta$ reste bien bornée dans $\mathcal{B}$ pour $\Theta \in \mathrm{H}$, ce qui prouve que $\mathcal{C}$ est plus fine que $\pi$, et finalement prouve l'isomorphisme (algébrique et topologique) de $(\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})_{x,y}$ et $(\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})_{x}\widehat{\otimes}_{\pi}(\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})_{y}$.

Prouvons enfin la dernière partie de la proposition 38: Les formes linéaires $\iint_{\mathbf{X}^l \times \mathbf{Y}^m}$ et $\int_{\mathbf{X}^l} \otimes \int_{\mathbf{Y}^m}$ sont toutes deux continues sur $(\mathfrak{D}_{\mathbf{L}^l}^{\prime})_{x,y}$, et elles coïncident trivialement sur le sous-espace dense $\mathfrak{D}_x \otimes \mathfrak{D}_y$, donc partout sur $(\mathfrak{D}_{\mathbf{L}^l}^{\prime})_x \widehat{\otimes}_{\pi} (\mathfrak{D}_{\mathbf{L}^l}^{\prime})_y$, c. q. f. d.

COROLLAIRE (Théorème de Fubini). — Si $\vec{T} \in (\mathcal{D}_{\mathrm{L}^1})_{x,y}(\mathrm{E})$, $\vec{T}$ est partiellement sommable en $x$, son intégrale en $x$ est une distribution sommable en $y$, et

$$
\iint_ {\mathbf {X} ^ {l} \times \mathbf {Y} ^ {m}} \vec {\mathrm{T}} (x, y) d x d y = \int_ {\mathbf {Y} ^ {m}} d y \int_ {\mathbf {X} ^ {l}} \vec {\mathrm{T}} (x, y) d x.\tag{I, 5; 16}
$$

On a naturellement aussi :

$$
(\mathbf {I}, 5; 1 7) \quad \iint_ {\mathbf {x} ^ {l} \times \mathbf {Y} ^ {m}} \vec {\mathbf {T}} (x, y) d x d y = \int_ {\mathbf {x} ^ {l}} d x \int_ {\mathbf {Y} ^ {m}} \vec {\mathbf {T}} (x, y) d y.
$$

On sait qu'il existe une application linéaire continue canonique de $(\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})_{x}\widehat{\otimes}_{\pi}(\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})_{y}$ dans $(\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})_{x}\widehat{\otimes}_{\varepsilon}(\mathfrak{D}_{\mathrm{L}^{\prime}}^{\prime})_{y}$; cette application est compatible avec les injections de ces 2 espaces dans $\mathfrak{D}_{x,y}^{\prime}$, autrement dit on a le diagramme commutatif:

$$
\begin{array}{c c c} (\mathfrak {D} _ {\mathrm{L} ^ {1}} ^ {\prime}) _ {x} \widehat {\otimes} _ {\pi} (\mathfrak {D} _ {\mathrm{L} ^ {1}} ^ {\prime}) _ {y} & \longrightarrow & \mathfrak {D} _ {x} ^ {\prime} \widehat {\otimes} _ {\pi} \mathfrak {D} _ {y} ^ {\prime} \\ \Big \downarrow & & \Big \uparrow \text {I} \\ (\mathfrak {D} _ {\mathrm{L} ^ {1}} ^ {\prime}) _ {x} \widehat {\otimes} _ {\varepsilon} (\mathfrak {D} _ {\mathrm{L} ^ {1}} ^ {\prime}) _ {y} & \longrightarrow & \mathfrak {D} _ {x} ^ {\prime} \widehat {\otimes} _ {\varepsilon} \mathfrak {D} _ {y} ^ {\prime}. \end{array}
$$

Donc cette application canonique est une injection, et $(\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_{x}\widehat{\otimes}_{\pi}(\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_{y}$ est un sous-espace de $(\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_{x}\widehat{\otimes}_{\varepsilon}(\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_{y}$, muni d'une topologie plus fine que la topologie induite.

Une distribution $\mathbf{T} \in (\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_x \widehat{\otimes}_{\varepsilon} (\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_y$ n'est pas nécessairement sommable, et n'a pas d'intégrale au sens antérieur du terme; néanmoins $\int_{\mathbf{X}^{\prime}} \otimes \int_{\mathbf{Y}^{m}}$ définit sur $(\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_x \widehat{\otimes}_{\varepsilon} (\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_y$ une forme linéaire continue, qui prolonge l'intégrale définie sur $(\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_{x,y}$, et que nous appellerons intégrale double généralisée. [Noter que, pour $\mathbf{T} \in (\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_x \widehat{\otimes}_{\varepsilon} (\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_y$ et $\alpha \in \mathcal{B}_{x,y}$, $\alpha \mathbf{T}$ n'est pas nécessairement dans $(\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_x \widehat{\otimes}_{\varepsilon} (\mathfrak{D}_{\mathbf{L}^{\prime}}^{\prime})_y$, donc n'a pas d'intégrale double généralisée].

De même $((\mathfrak{D}_{\mathbf{L}^1})_x\widehat{\otimes}_{\pi}(\mathfrak{D}_{\mathbf{L}^1})_y)\widehat{\otimes}_{\varepsilon}\mathbf{E}$ est un sous-espace de $((\mathfrak{D}_{\mathbf{L}^1})_x\widehat{\otimes}_{\varepsilon}(\mathfrak{D}_{\mathbf{L}^1})_y)\widehat{\otimes}_{\varepsilon}\mathbf{E}$, avec une topologie plus fine que la topologie induite (proposition 1 du § 1); sur ce dernier existe une intégrale double généralisée $\int_{\mathbf{X}^l}\otimes \int_{\mathbf{Y}^m}\otimes \mathrm{I}_{\mathrm{E}}$, qui prolonge l'intégrale double sur le premier.

Le théorème de Fubini est alors exact même pour $\vec{T} \in ((\mathfrak{D}_{\mathrm{L}^{\prime}})_{x} \widehat{\otimes}_{\varepsilon} (\mathfrak{D}_{\mathrm{L}^{\prime}})_{y}) \widehat{\otimes}_{\varepsilon} \mathrm{E}$, le premier membre de (I, 5; 16) ou (I, 5; 17) désignant l'intégrale double généralisée.

La formule (I, 5; 16) est en effet triviale et exprime la loi de composition :

$$
\int_ {\mathbf {X} ^ {l}} \otimes \int_ {\mathbf {Y} ^ {m}} \otimes \mathrm{I} _ {\mathrm{E}} = \left(\mathrm{I} _ {\mathrm{C}} \otimes \int_ {\mathbf {Y} ^ {m}} \otimes \mathrm{I} _ {\mathrm{E}}\right) \circ \left(\int_ {\mathbf {X} ^ {l}} \otimes \mathrm{I} _ {\mathcal {Y}} \otimes \mathrm{I} _ {\mathrm{E}}\right),
$$

$I_{C}$ étant l'opérateur identique sur le corps des scalaires C.

Remarque. — Les propositions 17 et 38 montrent que $\mathcal{B}_{x}^{*}$ et $\mathcal{B}_{y}^{*}$ sont des espaces L et M tels que $(\mathrm{L}\widehat{\otimes}_{\varepsilon}\mathrm{M})' = \mathrm{L}'\widehat{\otimes}_{\pi}\mathrm{M}'$.

## INDEX BIBLIOGRAPHIQUE

## BOURBAKI.

[1] Espaces vectoriels topologiques. Chapitres I et II, Paris, Hermann, 1953.

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

[2] « Sur les espaces (F) et (DF) ». Summa Brasiliensis Mathematicae, volume 3, 1954, p. 57-123.

[3] « Résumé des résultats essentiels dans la théorie des produits tensoriels topologiques et des espaces nucléaires ». Annales de l'Institut Fourier, tome IV, 1952, p. 73-112.

[4] « Produits tensoriels topologiques et espaces nucléaires ». Préliminaires et chapitre 1, Mémoirs of the American Mathematical Society, n° 16, 1955.

[5] « Produits tensoriels topologiques et espaces nucléaires », Chapitre II, Memoirs of the American Mathematical Society, n° 16, 1955.

[6] « Critères de compacité dans les espaces fonctionnels généraux ». American Journal of Mathematics, volume LXXIV, 1952, p. 168-186.

## Коетне.

[1] « Uber die Vollständigkeit einer Klasse lokalkonvexer Raume ». Mathematische Zeitschrift, volume 52, 1950, p. 627-630.

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

Schwartz-Dieudonné.

Voir Dieudonné-Schwartz.

## TABLE DES MATIÈRES DU CHAPITRE PREMIER

Pages.
INTRODUCTION .... 1
RÉSUMÉ DES PRÉLIMINAIRES.... 4
PRÉLIMINAIRES : Les propriétés d'approximation.... 5
RÉSUMÉ DU CHAPITRE I.... 13

## CHAPITRE PREMIER.

## DISTRIBUTIONS A VALEURS VECTORIELLES

§ 1. — Le produit ε d'espaces vectoriels topologiques.... 16
Le dual L′c d'un espace localement convexe séparé L.... 16
Les espaces ε Lᵢ = ε((Lᵢ)ᵢ∈I) = L₁ et ε (Lᵢ; M).... 18
L'injection canonique ⊗Lᵢ → ε Lᵢ.... 19
Compatibilité avec les applications linéaires continues.. 20
Ensembles ε-équihypocontinus de formes multilinéaires sur ∏(Lᵢ)' et parties relativement compactes de L₁... 22
L'espace L₁ est quasi-complet.... 28
Isomorphismes canoniques.... 30
Associativité du produit ε.... 37
Propriétés particulières aux espaces complets.... 41
Cas de quelques espaces particuliers.... 44
Produit ε et produit tensoriel topologique.... 46
§ 2. — Définition des distributions à valeurs vectorielles.... 49
Autres types de distributions vectorielles.... 52
Les espaces usuels et la propriété ε.... 53
Les espaces ℤ(E) pour certains espaces ℤ.... 61
Propriétés d'hypocontinuité.... 64
§ 3. — Exemples de distributions à valeurs vectorielles et propriétés algébriques et topologiques.... 65
Distributions définies par des fonctions.... 65
Dérivation des distributions.... 68
Multiplication.... 69
Notation fonctionnelle des distributions.... 71

THÉORIE DES DISTRIBUTIONS A VALEURS VECTORIELLES 141
Convolution ..... 72
Transformation de Fourier..... 73
Transformation de Laplace..... 74
Distributions d'ordre fini et dérivées de fonctions..... 83
§ 4. — Produits tensoriels topologiques d'espaces de distributions... 90
Noyaux..... 90
Le théorème des noyaux..... 93
Les espaces $\mathcal{H}_{x\in\mathcal{K}_{y}}$..... 96
Critères d'appartenance à $\mathcal{H}_{x\in\mathcal{K}_{y}}$..... 96
Cas où $\mathcal{H}_{x}$ et $\mathcal{K}_{y}$ sont de même nature..... 98
Cas où $\mathcal{H}_{x}$ et $\mathcal{K}_{y}$ ne sont pas des espaces de même nature : noyaux semi-réguliers, réguliers, régularisants..... 99
Noyaux semi-compacts, compacts, compactifiants..... 100
Le noyau $\delta(\hat{x}-\hat{y})$ de l'identité..... 102
Les noyaux de convolution..... 103
Noyaux des opérateurs différentiels; opérateurs de caractère local..... 106
Noyaux fonctions..... 111
Composition des noyaux au sens de Volterra..... 114
Associativité du produit de Volterra..... 120
Distributions semi-tempérées et transformation de Fourier partielle..... 123
Noyaux à valeurs vectorielles..... 124
§ 5. — Distributions sommables..... 126
Distributions partiellement sommables en $x$..... 130
Identité des espaces ($\mathcal{D}_{L^{1}}^{\prime})_{x,y}$ et ($\mathcal{D}_{L^{1}}^{\prime})_{x}\otimes_{x}(\mathcal{D}_{L^{1}}^{\prime})_{y}$..... 135
DEX BIBLIOGRAPHIQUE..... 138
BLE DES MATIÈRES..... 140