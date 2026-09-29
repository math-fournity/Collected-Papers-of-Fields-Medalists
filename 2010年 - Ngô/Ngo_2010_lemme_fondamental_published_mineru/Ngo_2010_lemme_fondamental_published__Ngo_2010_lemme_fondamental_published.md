## LE LEMME FONDAMENTAL POUR LES ALGÈBRES DE LIE par BAO CHÂU NGÔ

## TABLE DES MATIÈRES

Introduction 2
1. Conjectures de Langlands-Shelstad et Waldspurger 8
    1.1. Théorème de restriction de Chevalley 8
    1.2. Section de Kostant 9
    1.3. Torsion extérieure 10
    1.4. Centralisateur régulier semi-simple 12
    1.5. Classes de conjugaison dans une classe stable 14
    1.6. Dualité de Tate-Nakayama 15
    1.7. κ-intégrales orbitales 16
    1.8. Groupes endoscopiques 17
    1.9. Transfert des classes de conjugaison stable 18
    1.10. Discriminant et résultant 20
    1.11. Le lemme fondamental pour les algèbres de Lie 21
    1.12. Le lemme fondamental non standard 23
    1.13. Formule globale de stabilisation 25
2. Centralisateur régulier et section de Kostant 29
    2.1. Centralisateur régulier 29
    2.2. Sur le quotient [g/G] 30
    2.3. Le centre de G et les composantes connexes de J 32
    2.4. Description galoisienne de J 32
    2.5. Le cas des groupes endoscopiques 37
3. Fibres de Springer affines 38
    3.1. Rappels sur la grassmannienne affine 39
    3.2. Fibres de Springer affines 40
    3.3. Symétries d'une fibre de Springer affine 41
    3.4. Quotient projectif d'une fibre de Springer affine 43
    3.5. Approximation 43
    3.6. Cas linéaire 45
    3.7. Dimension 46
    3.8. Modèle de Néron 48
    3.9. Composantes connexes 49
    3.10. Densité de l'orbite régulière 53
    3.11. Le cas d'un groupe endoscopique 54
4. Fibration de Hitchin 55
    4.1. Rappels sur BunG 56
    4.2. Construction de la fibration 57
    4.3. Symétries d'une fibre de Hitchin 58
    4.4. Cas linéaire 59
    4.5. Courbe camérale 60
    4.6. Courbe camérale connexe 63
    4.7. Courbe camérale connexe et lisse 64
    4.8. Modèle de Néron global 67
    4.9. Invariant δa 69
    4.10. Le groupe π₀(Pa) 71
    4.11. Automorphismes 73
    4.12. Module de Tate polarisable 75
    4.13. Dimensions 78
    4.14. Calcul de déformation 80
    4.15. Formule de produit 84
    4.16. Densité 86
    4.17. Le cas des groupes endoscopiques 87
    4.18. Le cas des groupes appariés 89

5. Stratification . 89
    5.1. Normalisations en famille des courbes spectrales . 90
    5.2. Normalisation en famille des courbes camérales . 92
    5.3. Stratification de l'ouvert étale $\tilde{\mathcal{A}}$ . 93
    5.4. Invariants monodromiques . 95
    5.5. Description de $\pi_0(\mathcal{P})$ . 98
    5.6. Stratification à $\delta$ constant . 100
    5.7. Stratification par les valuations radicielles . 102
6. Cohomologie au-dessus de l'ouvert anisotrope . 104
    6.1. L'ouvert anisotrope . 104
    6.2. La $\kappa$-décomposition sur $\tilde{\mathcal{A}}^{\mathrm{ani}}$ . 105
    6.3. L'immersion fermée de $\tilde{\mathcal{A}}_{\mathrm{H}}$ dans $\tilde{\mathcal{A}}$ . 106
    6.4. Stabilisation géométrique . 109
    6.5. Cohomologie ordinaire de degré maximal . 110
7. Théorème du support . 111
    7.1. Fibration abélienne . 111
    7.2. L'énoncé du théorème du support . 113
    7.3. Inégalité de Goresky-MacPherson . 115
    7.4. Cap-produit et liberté . 116
    7.5. Propriété de liberté dans le cas ponctuel . 122
    7.6. Étude sur une base hensélienne . 125
    7.7. Liberté par récurrence . 127
    7.8. Le cas de la fibration de Hitchin . 132
8. Comptage de points . 135
    8.1. Remarques générales sur le comptage . 136
    8.2. Comptage dans une fibre de Springer affine . 142
    8.3. Un cas très simple . 150
    8.4. Comptage dans une fibre de Hitchin anisotrope . 154
    8.5. Stabilisation sur $\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{ani}} - \tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{bad}}$ . 156
    8.6. Le lemme fondamental de Langlands-Shelstad . 161
    8.7. Stabilisation géométrique sur $\tilde{\mathcal{A}}^{\mathrm{ani}}$ . 164
    8.8. Conjecture de Waldspurger . 164
Remerciements . 166
Références . 166

## Introduction

Dans cet article, nous proposons une démonstration pour des conjectures de Langlands, Shelstad et Waldspurger plus connues sous le nom de lemme fondamental pour les algèbres de Lie et lemme fondamental non standard. On se reporte à 1.11.1 et à 1.12.7 pour plus de précisions dans les deux énoncés suivants.

Théorème 1. — Soient $k$ un corps fini à $q$ éléments, $\mathcal{O}$ un anneau de valuation discrète complet de corps résiduel $k$ et $F$ son corps des fractions. Soit $G$ un schéma en groupes réductifs au-dessus de $\mathcal{O}$ dont le nombre de Coxeter multiplié par deux est plus petit que la caractéristique de $k$. Soient $(\kappa, \rho_{\kappa})$ une donnée endoscopique de $G$ au-dessus de $\mathcal{O}$ et $H$ le schéma en groupes endoscopiques associé.

On a l'égalité entre la $\kappa$-intégrale orbitale et l'intégrale orbitale stable

$$
\Delta_ {\mathrm{G}} (a) \mathbf {O} _ {a} ^ {\kappa} (1 _ {\mathfrak {g}}, \mathrm{d} t) = \Delta_ {\mathrm{H}} (a _ {\mathrm{H}}) \mathbf {S O} _ {a _ {\mathrm{H}}} (1 _ {\mathfrak {h}}, \mathrm{d} t)
$$

associées aux classes de conjugaison stable semi-simples régulières a et  $a_{h}$  de g(F) et h(F) qui se correspondent, aux fonctions caractéristiques  $1_{g}$  et  $1_{h}$  des compacts g(O) et h(O) dans g(F) et h(F) et où

on a noté

$$
\Delta_ {\mathrm{G}} (a) = q ^ {- \mathrm{val} (\mathfrak {D} _ {\mathrm{G}} (a)) / 2} e t \Delta_ {\mathrm{H}} (a _ {\mathrm{H}}) = q ^ {- \mathrm{val} (\mathfrak {D} _ {\mathrm{H}} (a _ {\mathrm{H}})) / 2}
$$

$\mathfrak{D}_{\mathrm{G}}$ et $\mathfrak{D}_{\mathrm{H}}$ étant les fonctions discriminant de G et de H.

Théorème 2. — Soient  $G_{1}$ ,  $G_{2}$  deux schémas en groupes réductifs sur O ayant des données radicielles isogènes dont le nombre de Coxeter multiplié par deux est plus petit que la caractéristique de k. Alors, on a l'égalité suivante entre les intégrales orbitales stables

$$
\mathbf {S O} _ {a _ {1}} \left(1 _ {\mathfrak {g} _ {1}}, \mathrm{d} t\right) = \mathbf {S O} _ {a _ {2}} \left(1 _ {\mathfrak {g} _ {2}}, \mathrm{d} t\right)
$$

associées aux classes de conjugaison stable semi-simples régulières  $a_{1}$  et  $a_{2}$  de  $\mathfrak{g}_{1}(\mathrm{F})$  et  $\mathfrak{g}_{2}(\mathrm{F})$  qui se correspondent et aux fonctions caractéristiques  $1_{\mathfrak{g}_{1}}$  et  $1_{\mathfrak{g}_{2}}$  des compacts  $\mathfrak{g}_{1}(\mathcal{O})$  et  $\mathfrak{g}_{2}(\mathcal{O})$  dans  $\mathfrak{g}_{1}(\mathrm{F})$  et  $\mathfrak{g}_{2}(\mathrm{F})$ .

Nous démontrons ces théorèmes dans le cas d'égales caractéristiques. D'après Waldspurger, le cas d'inégales caractéristiques s'en déduit cf. [82].

Le lemme fondamental joue un rôle important dans la réalisation de certains cas particuliers du principe de fonctorialité de Langlands via la comparaison de formules des traces et dans la construction de représentations galoisiennes attachées aux formes automorphes par le biais du calcul de cohomologie des variétés de Shimura. On se réfère aux travaux d'Arthur [2] pour les applications à la comparaison de formules des traces et à l'article de Kottwitz [45] ainsi qu'au livre en préparation édité par Harris pour les applications aux variétés de Shimura.

Cas connus et réductions. — Le lemme fondamental a été établi dans un grand nombre de cas particuliers. Son analogue archimédien a été entièrement résolu par Shelstad dans [71]. Ce cas a incité Langlands et Shelstad à formuler leur conjecture pour un corps local non-archimédien. Le cas du groupe SL(2) a été traité par Labesse et Langlands dans [48]. Le cas du groupe unitaire à trois variables a été résolu par Rogawski dans [65]. Les cas assimilés aux Sp(4) et GL(4) tordu ont été résolus par Hales, Schröder et Weissauer par des calculs explicites cf. [31], [68] et [84]. Récemment, Whitehouse a poursuivi ces calculs pour démontrer le lemme fondamental pondéré tordu dans ce cas cf. [85].

Le lemme fondamental pour le changement de base stable a été établi par Clozel cf. [14] et Labesse cf. [47] à partir du cas de l'unité de l'algèbre de Hecke démontré par Kottwitz cf. [43]. Auparavant, le cas GL(2) a été établi par Saito, Shintani cf. [67] et Langlands cf. [49] et le cas GL(3) par Kottwitz cf. [39].

Un autre cas important est le cas SL(n) résolu par Waldspurger dans [79]. Le cas SL(3) avec un tore elliptique a été établi auparavant par Kottwitz cf. [40] et le cas SL(n) avec un tore elliptique par Kazhdan cf. [35].

Récemment, avec Laumon, nous avons démontré le lemme fondamental pour les algèbres de Lie des groupes unitaires dans le cas d'égale caractéristique. La méthode que nous utilisons est géométrique et ne s'applique qu'aux corps locaux d'égales caractéristiques. Comme nous l'avons déjà mentionné, le cas d'inégales caractéristiques s'en déduit grâce aux travaux de Waldspurger [82]. Le changement de caractéristiques a aussi été établi par Cluckers et Loeser [15] dans un cadre plus général mais moins précis sur la borne de la caractéristique résiduelle. Ils utilisent la logique.

Dans une série de travaux comprenant notamment [80] et [83], Waldspurger a démontré que le lemme fondamental pour les groupes ainsi que le transfert se déduisent du lemme fondamental ordinaire pour les algèbres de Lie. De même, le lemme fondamental tordu se déduit de la conjonction du lemme ordinaire pour les algèbres de Lie et de ce qu'il appelle le lemme non standard. Dans la suite de cet article, on se restreint au lemme fondamental ordinaire pour les algèbres de Lie et sa variante non standard sur un corps local d'égale caractéristique.

Approche géométrique locale. — Kazhdan et Lusztig ont introduit dans [36] les fibres de Springer affines qui sont des incarnations géométriques des intégrales orbitales. Ce travail fournit des renseignements de base sur la géométrie des fibres de Springer affines que nous rappellerons dans le chapitre 3 du présent article.

Dans l'annexe à [36], Bernstein et Kazhdan ont construit une fibre de Springer affine pour le groupe Sp(6) dont le nombre de points n'est pas un polynôme en q. En fait, le motif associé à cette fibre de Springer affine contient le motif d'une courbe hyperelliptique. Cet exemple suggère qu'il est peu probable qu'on puisse obtenir une formule explicite pour les intégrales orbitales.

L'interprétation des $\kappa$-intégrales orbitales en termes des quotients des fibres de Springer affines a été établie dans l'article de Goresky, Kottwitz et MacPherson [26]. Ils ont aussi introduit dans [26] l'usage de la cohomologie équivariante dans l'étude des fibres de Springer affines. Cette stratégie est très adaptée au cas particulier des éléments qui appartiennent à un tore non ramifié car on dispose dans ce cas d'une action d'un gros tore sur la fibre de Springer affine n'ayant que des points fixes isolés. Ils ont aussi découvert une relation remarquable entre la cohomologie équivariante d'une fibre de Springer affine pour G et la fibre correspondante pour le groupe endoscopique H dans ce cadre non ramifié. Cette relation dépend aussi d'une conjecture de pureté de la cohomologie de ces fibres de Springer affines. Cette conjecture a été vérifiée pour les éléments ayant des valuations radicielles égales dans [27].

Dans [51] et [52], Laumon a introduit une méthode de déformations des fibres de Springer dans le cas des groupes unitaires fondée sur la théorie des déformations des courbes planes. Sa stratégie consiste à introduire une courbe plane de genre géométrique nul ayant une singularité prescrite par la situation locale et ensuite à déformer cette courbe plane. Il a aussi remarqué que dans le cas unitaire, il existe un tore de dimension un agissant sur les fibres de Springer affines de U(n) associées à une classe stable

provenant de  $\mathrm{U}(n_{1})\times\mathrm{U}(n_{2})$  dont la variété des points fixes est la fibre de Springer affine correspondante de  $\mathrm{U}(n_{1})\times\mathrm{U}(n_{2})$ . En calculant la cohomologie équivariante en famille, il a démontré conditionnellement le lemme fondamental dans le cas particulier du groupe unitaire mais pour les éléments éventuellement ramifiés. Sa démonstration dépend aussi de la conjecture de pureté des fibres de Springer affines formulée par Goresky, Kottwitz et MacPherson.

Cette conjecture de pureté m'avait semblé l'obstacle principal à l'approche géométrique locale. Elle joue un rôle essentiel pour faire dégénérer certaines suites spectrales et permet d'appliquer le théorème de localisation d'Atiyah-Borel-Segal.

Il existe en fait un autre obstacle au moins aussi sérieux à l'usage de la cohomologie équivariante pour les fibres de Springer affines générales. Pour des éléments très ramifiés des groupes autres qu'unitaires, il n'y a pas d'action torique sur la fibre de Springer affine correspondante. Dans ce cas, même si on dispose de la conjecture de pureté, il n'est pas clair que les stratégies de [26] et [52] peuvent s'appliquer.

Approche géométrique globale. — Dans [34], Hitchin a démontré que le fibré cotangent de l'espace de module des fibrés stables sur une surface de Riemann compacte est un système hamiltonien complètement intégrable. Pour cela, il interprète ce fibré cotangent comme l'espace de module des fibrés principaux munis d'un champ de Higgs. Les hamiltoniens sont alors donnés par les coefficients du polynôme caractéristique du champ de Higgs. Il définit ainsi la fameuse fibration de Hitchin $f: \mathcal{M} \to \mathcal{A}$ où $\mathcal{M}$ est le fibré cotangent ci-dessus, où $\mathcal{A}$ est l'espace affine classifiant les polynômes caractéristiques à coefficients dans l'espace des sections globales de puissances convenables du fibré canonique de X et où $f$ est un morphisme dont la fibre générique est essentiellement une variété abélienne.

De notre point de vue, les fibres de la fibration de Hitchin sont des analogues globaux des fibres de Springer affines. Il est par ailleurs important dans notre approche de prendre les fibrés de Higgs non à valeurs dans le fibré canonique mais à valeurs dans un fibré inversible arbitraire de degré assez grand. Dans cette modeste généralisation, l'espace de module M n'est plus muni d'une forme symplectique mais dispose toujours d'une fibration de Hitchin  $f: M \to A$  ayant la même allure que l'originale.

Nous avons observé dans [57] qu'un comptage formel de points de $\mathcal{M}$ à coefficients dans un corps fini donne une expression quasiment identique au côté géométrique de la formule des traces pour l'algèbre de Lie. Nous nous sommes proposés dans [57] d'interpréter le processus de stabilisation de la formule des traces de Langlands et Kottwitz en termes de cohomologie $\ell$-adique de la fibration de Hitchin. Cette interprétation conduit à une formulation d'une variante globale du lemme fondamental en termes de cohomologie $\ell$-adique de la fibration de Hitchin cf. [16] et [58]. L'interprétation géométrique du processus de stabilisation avec la fibration de Hitchin ainsi que la formulation de cette variante globale du lemme fondamental est plus complexe que l'analogue local avec les fibres de Springer affines. En contrepartie, on dispose d'une géométrie plus riche.

L'interprétation géométrique du processus de stabilisation est fondée sur l'action d'un champ de Picard $\mathcal{P} \to \mathcal{A}$ sur $\mathcal{M}$ qui est en quelque sorte le champ des symétries naturelles de la fibration de Hitchin. Le comptage de points avec l'aide de $\mathcal{P}$ fait dans le paragraphe 9 de [57] est repris de façon plus systématique dans le dernier chapitre 8 du présent article. La construction de $\mathcal{P}$ est fondée sur celle du centralisateur régulier que nous rappelons dans le chapitre 2. L'observation qui joue un rôle clé dans le comptage est que pour tout $a \in \mathcal{M}(k)$, le quotient $[\mathcal{M}_a / \mathcal{P}_a]$ s'exprime en un produit de quotients locaux des fibres de Springer affines $\mathcal{M}_v(a)$ par leurs groupes de symétries naturelles $\mathcal{P}_v(\mathrm{J}_a)$ cf. 4.15.1 et [57, 4.6]. Cette formule de produit apparaît en filigrane tout le long de l'article.

Le champ algébrique M n'est pas de type fini. Il existe néanmoins un ouvert anisotrope  $A^{ani}$  de A, construit dans le chapitre 6, au-dessus duquel  $f^{ani}: M^{ani} \to A^{ani}$  est un morphisme propre. On sait par ailleurs que  $M^{ani}$  est lisse sur le corps de base k. D'après Deligne [18], l'image directe dérivée  $f_{*}^{ani} Q_{\ell}$  est un complexe pur c'est-à-dire que les faisceaux pervers de cohomologie

$$
{ } ^ { p } \mathrm{H} ^ { n } ( f _ { * } ^ { \text {   a   n   i   } } \bar { \mathbf { Q } } _ { \ell } )
$$

sont des faisceaux pervers purs. D'après le théorème de décomposition, ceux-ci deviennent semi-simples après le changement de base à $\mathcal{A}^{\mathrm{ani}}\otimes_{k}\overline{k}$. En vue de démontrer le lemme fondamental, il est essentiel de comprendre les facteurs géométriquement simples dans cette décomposition.

L'action de $\mathcal{P}$ sur $\mathcal{M}$ induit une action de $\mathcal{P}^{\mathrm{ani}}$ sur les faisceaux pervers $^{b}\mathrm{H}^{n}(f_{*}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})$ et décompose ceux-ci en composantes isotypiques

$$
{ } ^ { p } \mathrm{H} ^ { n } ( f _ { * } ^ { \text {   a   n   i   } } \bar { \mathbf { Q } } _ { \ell } ) = \bigoplus _ { [ \kappa ] } { } ^ { p } \mathrm{H} ^ { n } ( f _ { * } ^ { \text {   a   n   i   } } \bar { \mathbf { Q } } _ { \ell } ) _ { [ \kappa ] } .
$$

Ici, l'indice $[\kappa]$ parcourt l'ensemble des classes de conjugaison semi-simples dans le groupe dual $\hat{\mathbf{G}}$, seul un nombre fini d'entre elles ayant une contribution non triviale. On note $^b\mathrm{H}^n (f_*^{\mathrm{ani}}\bar{\mathbf{Q}}_\ell)_{\mathrm{st}}$ le facteur direct correspondant à $\kappa = 1$. L'apparition du groupe dual ici résulte du calcul du faisceau des composantes connexes des fibres de $\mathcal{P}$ à la Tate-Nakayama qui a été entamé dans [57, 6] et est complété dans les paragraphes 4.10 et 5.5 du présent article. Dans [57] et [58], nous avons montré que cette décomposition correspond exactement à la décomposition endoscopique du côté géométrique de la formule des traces qui a été établie par Langlands et Kottwitz cf. [50] et [44].

Dans ce travail, nous changeons légèrement de point de vue. Au lieu de travailler sur  $A^{ani}$ , nous passons à un revêtement étale  $\tilde{A}^{ani}$  dépendant du choix d'un point  $\infty \in X$  tout comme dans [54]. Au-dessus de cet ouvert étale, on a une décomposition plus fine

$$
{ } ^ { p } \mathrm{H} ^ { n } ( \tilde { f } _ { * } ^ { \text {   a   n   i   } } \bar { \mathbf { Q } } _ { \ell } ) = \bigoplus _ { [ \kappa ] } { } ^ { p } \mathrm{H} ^ { n } ( \tilde { f } _ { * } ^ { \text {   a   n   i   } } \bar { \mathbf { Q } } _ { \ell } ) _ { \kappa }
$$

où $\kappa$ parcourt un sous-ensemble fini du tore maximal $\hat{\mathbf{T}}$ du groupe dual $\hat{\mathbf{G}}$. Nous ne nous collons plus exactement à la formule des traces, mais en contrepartie nous nous

débarrassons de quelques difficultés accessoires. Notre théorème de stabilisation géométrique 6.4.1 consiste à exprimer la pièce $^{p}\mathrm{H}^{n}(\tilde{f}_{*}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})_{\kappa}$ en termes des groupes endoscopiques. En fait, on l'exprime comme une somme directe des pièces stables c'est-à-dire correspondant à $\kappa = 1$ mais pour les groupes H associés à des données endoscopiques pointées cf. 1.8.2. On a une variante arithmétique 6.4.2 de 6.4.1 dont le lemme fondamental de Langlands-Shelstad est une conséquence.

Dans [57], on a démontré que  ${}^{p}\mathrm{H}^{n}(\tilde{f}_{*}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})_{\kappa}$  est supporté par la réunion des images des morphismes  $\tilde{A}_{H}^{ani} \to \tilde{A}^{ani}$  ou plutôt une variante. Nous reprenons ces arguments dans 6.3. Comme nous l'avons observé dans [57] et [54], cet énoncé peut remplacer la conjecture de pureté de Goresky, Kottwitz et MacPherson dans le contexte de la fibration de Hitchin. Par ailleurs, il est très tentant de conjecturer que tous les facteurs simples de  ${}^{p}\mathrm{H}^{n}(\tilde{f}_{*}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})_{\kappa}$  ont comme support l'image de l'une des immersions fermées  $\tilde{A}_{H}^{ani} \to \tilde{A}^{ani}$ . Remarquons que le théorème de stabilisation géométrique se déduit de cette conjecture du support car en effet il n'est pas difficile de l'établir sur un ouvert dense de  $\tilde{A}_{H}^{ani}$ .

Dans le cas unitaire, Laumon et moi avons utilisé la suite exacte d'Atiyah-Borel-Segal en cohomologie équivariante pour démontrer une variante faible de l'énoncé de support ci-dessus. Mes tentatives ultérieures de généraliser cette méthode équivariante à d'autres groupes se sont heurtées à l'absence de l'action torique dans certaines fibres de Hitchin associées aux éléments très ramifiés.

Dans ce travail, on démontre pour tous les groupes une forme faible de cette conjecture du support. Dans le chapitre 7, nous démontrons qu'on peut déterminer tous les supports dans le cas d'une fibration abélienne δ-régulière cf. 7.2.1. Comme il n'est pas possible pour l'instant de démontrer que la fibration de Hitchin est δ-régulière, voir toutefois cf. [60, p. 4], nous utilisons certains énoncés intermédiaires 7.2.2 et 7.2.3 combinés avec ce qui est disponible en caractéristique positive en direction de la δ-régularité 5.7.2 et un comptage intensif au chapitre 8 pour conclure la démonstration de 6.4.2.

L'inégalité delta 7.2.2 dont la démonstration occupe le chapitre 7 permet de minorer la codimension des supports dans le cas d'une fibration abélienne. Il s'agit en fait d'une variante élaborée de l'inégalité sur la codimension des supports due à Goresky et MacPherson qu'on rappellera en 7.3.

Passons maintenant en revue l'organisation de l'article. Le premier chapitre contient l'énoncé du lemme fondamental pour les algèbres de Lie ainsi que sa variante non standard. Le cœur de l'article est l'avant-dernier chapitre 7 où on démontre les inégalités 7.2.2 et 7.2.3 dont se déduira un théorème du support 7.8.5. Le dernier chapitre 8 contient l'argument de comptage qui permet de déduire le lemme fondamental à partir du théorème du support 7.8.5. Les autres chapitres sont de nature préparatoire. Le chapitre 3 contient une étude de la géométrie des fibres de Springer affines. Le chapitre suivant 4 contient une étude parallèle de la géométrie de la fibration de Hitchin. Notre outil favori est ici l'action des symétries naturelles fondée sur la construction du centralisateur régulier rappelée dans le chapitre 2. Dans le chapitre 5, on définit diverses stratifications de la base de Hitchin. Dans le chapitre suivant 6, on définit l'ouvert anisotrope de la base

de Hitchin au-dessus duquel la fibration a toutes les bonnes propriétés pour qu'on puisse formuler le théorème de stabilisation géométrique 6.4.2 qui sera démontré dans les deux derniers chapitres 7 et 8.

## 1. Conjectures de Langlands-Shelstad et Waldspurger

Dans ce chapitre, on rappelle l'énoncé du lemme fondamental pour les algèbres de Lie conjecturé par Langlands et Shelstad cf. 1.11.1 ainsi que la variante non standard conjecturée par Waldspurger cf. 1.12.7. Dans le dernier paragraphe de ce chapitre, nous rappelons où intervient le lemme fondamental de Langlands-Shelstad dans le processus de stabilisation du côté géométrique de la formule des traces. Notre étude de la fibration de Hitchin qui sera faite ultérieurement dans cet article est directement inspirée de ce processus de stabilisation. Nous nous efforçons de maintenir l'exposition de ce chapitre dans un langage aussi élémentaire que possible.

1.1. Théorème de restriction de Chevalley. — Soient k un corps et G un groupe réductif déployé sur k. Notre définition est celle de [21] : réductif implique affine lisse et connexe. On fixera un tore maximal déployé T et un sous-groupe de Borel B contenant T. Soient  $\mathrm{N}_{\mathrm{G}}(\mathbf{T})$  le normalisateur de T et  $\mathbf{W} = \mathrm{N}_{\mathrm{G}}(\mathbf{T}) / \mathbf{T}$  le groupe de Weyl. On notera g l'algèbre de Lie de G et k[g] l'algèbre des fonctions régulières sur g. De même, on notera t = Spec(k[t]) l'algèbre de Lie de T. Soit r le rang de G.

L'action de T sur l'algèbre de Lie g définit un ensemble de racines  $\Phi$  sur lequel agit le groupe de Weyl W. Le choix du sous-groupe de Borel B définit un ensemble de racines simples  $\Delta$ . Toute racine s'écrit de façon unique sous la forme  $\sum_{\alpha\in\Delta}n_{\alpha}\alpha$  avec  $n_{\alpha}\in Z$ . On appelle alors  $\sum_{\alpha\in\Delta}n_{\alpha}$  la hauteur de cette racine. On note h-1 la hauteur maximale d'une racine. Si le système de racines est simple, h est son nombre de Coxeter. Nous supposerons dans tout ce travail que la caractéristique p est soit nulle, soit plus grande que 2h. Comme l'ordre du groupe de Weyl est un produit d'entiers naturels ne dépassant pas h, cette hypothèse implique en particulier que p ne divise pas l'ordre du groupe de Weyl. Elle implique aussi que p est un bon nombre premier au sens de [12, 1.14] et donc que la forme de Killing est non dégénérée dans le cas semi-simple.

Le groupe G agit sur son algèbre de Lie par l'action adjointe. Voici l'énoncé du théorème de restriction de Chevalley dont on peut trouver une démonstration dans le cas semi-simple adjoint [75, 3.17]. Le cas général s'en déduit sous l'hypothèse p > 2 [55, 0.8].

Théorème 1.1.1. — La restriction de g à t induit un isomorphisme d'algèbres k[g]G = k[t]W.

On notera $\mathbf{c} = \operatorname{Spec}(k[\mathbf{t}]^{\mathbf{W}}) = \operatorname{Spec}(k[\mathbf{g}]^{\mathbf{G}})$. On notera $\chi : \mathbf{g} \to \mathbf{c}$ le morphisme caractéristique de Chevalley qui se déduit de l'inclusion d'algèbres $k[\mathbf{g}]^{\mathbf{G}} \subset k[\mathbf{g}]$. Par analogie avec le cas des matrices, on appellera $\chi(x)$ le polynôme caractéristique de $x$ et $\mathbf{c}$

l'espace des polynômes caractéristiques. L'action de  $G_{m}$  par homothétie sur g commute à l'action adjointe de G et donc induit une action sur c. On dispose des morphismes de champs algébriques

$$
[ \chi ]: [ \mathbf {g} / \mathbf {G} ] \to \mathbf {c} \quad \text { et } \quad [ \chi / \mathbf {G} _ {m} ]: [ \mathbf {g} / \mathbf {G} \times \mathbf {G} _ {m} ] \to [ \mathbf {c} / \mathbf {G} _ {m} ].
$$

L'inclusion  $k[t]^{\mathbf{W}} \subset k[t]$  définit un morphisme  $\pi : t \to c$ . C'est un morphisme fini et plat qui réalise c comme le quotient au sens des invariants de t par l'action de W. De plus, il existe un ouvert non vide  $c^{rs}$  de c au-dessus duquel  $\pi$  est un morphisme fini étale galoisien de groupe de Galois W. Ce morphisme est compatible avec l'action de  $G_{m}$  par homothétie sur t et l'action de  $G_{m}$  sur c.

1.2. Section de Kostant. — Le morphisme  $\chi : g \to c$  admet des sections. Dans [38], Kostant a construit de façon uniforme une telle section. Bien qu'il suppose que le corps de base est de caractéristique zéro, sa construction se généralise en caractéristique positive p > 2h. Dans [78], Veldkamp cherchait à construire la section de Kostant sous l'hypothèse plus faible à savoir p ne divisant pas l'ordre du groupe de Weyl, mais comme me l'a fait remarqué Deligne, l'argument de Veldkamp semble incomplet.

Fixons un épinglage de $\mathbf{G}$ qui contient en plus de $\mathbf{T}$ et de $\mathbf{B}$, un vecteur $\mathbf{x}_{+} \in \operatorname{Lie}(\mathbf{U})$ de la forme $\mathbf{x}_{+} = \sum_{\alpha \in \Delta} \mathbf{x}_{\alpha}$ où $\Delta$ est l'ensemble des racines simples et où $\mathbf{x}_{\alpha}$ est un vecteur non nul du sous-espace propre $\operatorname{Lie}(\mathbf{U})_{\alpha}$ de $\operatorname{Lie}(\mathbf{U})$ correspondant à la valeur propre $\alpha$ pour l'action de $\mathbf{T}$. Ici $\mathbf{U}$ a désigné le radical unipotent de $\mathbf{B}$.

Il existe alors un unique $\mathfrak{sl}_2$-triplet $(h, \mathbf{x}_+, \mathbf{x}_-)$ dans $\mathbf{g}$ avec l'élément semi-simple $h \in \mathbf{t} \cap \operatorname{Lie}(\mathbf{G}^{\mathrm{der}})$. En effet, en raisonnant sur la hauteur des racines, on peut montrer $\operatorname{ad}(\mathbf{x}_+)^{2\mathbf{h}-1} = 0$ comme dans [12, 5.5.2]. On dispose alors d'un théorème du type Jacobson-Morozov [12, 5.3.2] sous l'hypothèse $p > 2\mathbf{h}$. On sait même que la représentation principale de $\mathfrak{sl}_2$ sur $\mathfrak{g}$ est complètement réductible sous l'hypothèse $p > 2\mathbf{h}$ d'après [12, 5.4.8].

Lemme 1.2.1. — Soit $\mathbf{g}^{\mathbf{x}_{+}}$ le centralisateur de $\mathbf{x}_{+}$ dans $\mathbf{g}$. La restriction du morphisme caractéristique $\chi : \mathbf{g} \to \mathbf{c}$ au sous-espace affine $\mathbf{x}_{-} + \mathbf{g}^{\mathbf{x}_{+}}$ du vectoriel $\mathbf{g}$ est un isomorphisme.

Cet énoncé a été démontré par Kostant en caractéristique zéro [38, théorème 0.10]. Il observe d'abord $\mathrm{Lie(B) = [\mathbf{x}_{-},\mathrm{Lie(U)}]\oplus\mathbf{g}^{\mathbf{x}_{+}}}$. Cette égalité découle de la complète réductibilité de la représentation principale de $\mathfrak{sl}_2$ dans $\mathbf{g}$ qui est valide sous l'hypothèse $p > 2\mathbf{h}$. Son argument [38, Prop. 19] pour déduire le lemme de cette observation est en fait indépendant de la caractéristique. Il a aussi été exposé à la dernière page de [6].

L'inverse de cet isomorphisme

$$
\epsilon : \mathbf {c} \rightarrow \mathbf {x} _ {-} + \mathbf {g} ^ {\mathbf {x} _ {+}} \hookrightarrow \mathbf {g}\tag{1.2.2}
$$

définit une section du morphisme de Chevalley $\chi : \mathbf{g} \to \mathbf{c}$. C'est la section de Kostant.

Pour les groupes classiques, il est également possible de construire des sections explicites  $c \rightarrow g$  à l'aide de l'algèbre linéaire sans utiliser l'épinglage cf. [59]. Ces sections, qui généralisent la matrice compagnon dans le cas linéaire, sont probablement plus adaptées aux calculs explicites des fibres de Springer affines et des fibres de Hitchin.

Revenons à la section construite par Kostant. Il résulte de 1.2.1 que c est isomorphe à un espace affine. L'action de  $G_{m}$  sur G induit une action de c. En utilisant la complète réductibilité de la représentation principale de  $sl_{2}$  dans g, on peut choisir des coordonnées de c de sorte que cette action s'écrit

$$
t (a _ {1}, \dots , a _ {r}) = (t ^ {e _ {1}} a _ {1}, \dots , t ^ {e _ {r}} a _ {r}).
$$

Les entiers $e_1 - 1, \ldots, e_r - 1$ sont les exposants du système de racines voir [11].

Soit  $g^{reg}$  l'ouvert de g des points  $x \in g$  dont le centralisateur  $I_{x}$  est de dimension r. Il a été démontré dans [38, Lemma 10] que l'image de la section de Kostant est contenue dans l'ouvert  $g^{reg}$ . Kostant démontre que si  $x, x' \in g^{\mathrm{reg}}(\bar{k})$  ont le même polynôme caractéristique  $\chi(x) = \chi(x')$ , alors ils sont conjugués cf. [38, Th. 2]. En combinant avec l'existence de la section, il obtient l'énoncé suivant.

Lemme 1.2.3. — La restriction de $\chi$ à $\mathbf{g}^{\mathrm{reg}}$ est un morphisme lisse. Ses fibres géométriques sont des espaces homogènes sous l'action de G.

1.3. Torsion extérieure. — Pour les applications arithmétiques, il est nécessaire de considérer les formes quasi-déployées du groupe G. Fixons un épinglage  $(\mathbf{T}, \mathbf{B}, \mathbf{x}_{+})$  de G comme dans 1.2. Notons Out(G) le groupe des automorphismes de G qui fixent cet épinglage. C'est un groupe discret qui peut être éventuellement infini. Il agit sur l'ensemble des racines  $\Phi$  en laissant stable le sous-ensemble des racines simples. Il agit aussi sur le groupe de Weyl W de façon compatible c'est-à-dire le produit semi-direct  $\mathbf{W} \times \text{Out}(\mathbf{G})$  qui s'en déduit agit sur T et sur l'ensemble  $\Phi$  des racines en combinant l'action de W avec celle de Out(G).

Définition 1.3.1. — Une forme quasi-déployée de G sur un k-schéma X est la donnée d'un Out(G)-torseur  $\rho_{G}$  sur X localement trivial pour la topologie étale.

1.3.2. — La donnée de  $\rho_{G}$  permet de tordre G pour obtenir un X-schéma en groupes réductif lisse  $G = \rho_{G} \wedge^{\mathrm{Out}(G)} G$  qui est muni d'un épinglage défini sur X, c'est-à-dire un triplet (T, B,  $x_{+}$ ), où B est un sous-schéma en groupes fermé de G lisse au-dessus de X, T est un sous-tore de B et  $x_{+}$ est une section globale de Lie(B), tel que fibre par fibre (T, B,  $x_{+}$ ) est isomorphe à l'épinglage (T, B,  $x_{+}$ ). Inversement tout X-schéma en groupes lisse réductif muni d'un épinglage (T, B,  $x_{+}$ ) qui est localement pour la topologie étale isomorphe à G épinglé, définit un torseur sous le groupe Out(G). Nous nous permettrons l'abus de langage qui consiste à dire que G est une forme quasi-déployée en oubliant l'épinglage attaché.

1.3.3. — Soient $\rho_{\mathrm{G}}$ un Out(G)-torseur sur X et G la forme quasi-déployée attachée avec l'épinglage (T, B, $\mathbf{x}_{+}$). Les structures mentionnées dans les deux paragraphes précédents se transposent à la forme quasi-déployée. Soient $\mathfrak{g} = \operatorname{Lie}(\mathbf{G})$ et $t = \operatorname{Lie}(T)$. L'action de $\mathbf{W} \rtimes \operatorname{Out}(\mathbf{G})$ sur t induit une action de Out(G) sur $\mathbf{c} = \mathbf{t}/\mathbf{W}$. On définit donc l'espace des polynômes caractéristiques de $\mathfrak{g} = \operatorname{Lie}(\mathbf{G})$ comme le X-schéma

$$
\mathfrak {c} = \rho_ {\mathrm{G}} \wedge^ {\mathrm{Out} (\mathbf {G})} \mathbf {c}.
$$

Il est muni d'un morphisme

$$
\chi : \mathfrak {g} \rightarrow \mathfrak {c}
$$

qui se déduit du morphisme de Chevalley $\chi : \mathbf{g} \to \mathbf{c}$. Comme $\operatorname{Out}(\mathbf{G})$ fixe le $\mathfrak{sl}_2$-triplet $(h, \mathbf{x}_+, \mathbf{x}_-)$, la section de Kostant $\epsilon : \mathbf{c} \to \mathbf{g}$ est $\operatorname{Out}(\mathbf{G})$-équivariant. Par torsion, on obtient un X-morphisme

$$
\epsilon : \mathfrak {c} \to \mathfrak {g}\tag{1.3.4}
$$

section du morphisme de Chevalley $\chi : \mathfrak{g} \to \mathfrak{c}$ qu'on appellera aussi section de Kostant. On a par ailleurs un morphisme fini plat

$$
\pi : \mathfrak {t} \to \mathfrak {c}
$$

qui se déduit de $\pi : \mathbf{t} \to \mathbf{c}$. Le X-schéma en groupes fini étale

$$
\mathbf {W} = \rho_ {\mathrm{G}} \wedge^ {\mathrm{Out} (\mathbf {G})} \mathbf {W}
$$

agit sur t. Comme c est le quotient de t par W au sens des invariants, c est aussi le quotient de t par W au sens des invariants. Au-dessus de l'ouvert  $\mathfrak{c}^{\mathrm{rs}} = \rho_{\mathrm{G}} \wedge^{\mathrm{Out}(\mathbf{G})} \mathbf{c}$ , le morphisme  $\pi : t^{rs} \to c^{rs}$  est un torseur sous le schéma en groupes fini étale W.

1.3.5. — Il est souvent commode de passer du langage des torseurs au langage plus concret des représentations du groupe fondamental. Soient x un point géométrique de X et  $\pi_{1}(X, x)$  le groupe fondamental profini de X pointé par x. On supposera dans la suite que X est connexe et normal.

On appellera forme quasi-déployée pointée de G un homomorphisme continu

$$
\rho_ {\mathrm{G}} ^ {\bullet}: \pi_ {1} (\mathrm{X}, x) \to \operatorname{Out} (\mathbf {G}).
$$

Le Out(G)-torseur  $\rho_{G}$  qui s'en déduit est équipé d'un point géométrique  $x_{G}$  au-dessus de x.

1.3.6. — Le pointage permet une description galoisienne des torseurs sous W qui est lui-même une forme tordue de W. Soient  $\rho_{\mathrm{G}}^{\bullet}:\pi_{1}(\mathrm{X},x)\to\mathrm{Out}(\mathbf{G})$  un homomorphisme continu, G et W les groupes qui se déduisent de G et W par torsion.

Soit  $X_{\bullet}$  le revêtement profini étale galoisien universel de X qui par construction est la limite projective sur tous les revêtements finis étales galoisiens  $X_{1} \rightarrow X$  munis d'un point géométrique  $x_{1}$  au-dessus de x. La limite  $X_{\bullet}$  est munie d'un point géométrique  $x_{\bullet}$  au-dessus de x. Le couple  $(\mathbf{X}_{\bullet}, x_{\bullet})$  est l'objet initial de la catégorie des revêtements profinis étales galoisiens pointés de  $(\mathbf{X}, x)$ .

L'image réciproque de W au revêtement universel X. est canoniquement isomorphe au groupe constant W.

Soient $\pi : \tilde{\mathbf{X}} \to \mathbf{X}$ un W-torseur, $\tilde{x}$ un point géométrique de $\tilde{\mathbf{X}}$ au-dessus de $x$. Le produit fibré $\tilde{\mathbf{X}}_{\bullet} = \tilde{\mathbf{X}} \times_{\mathbf{X}} \mathbf{X}_{\bullet}$ est alors muni d'un point géométrique $\tilde{x}_{\bullet} = (\tilde{x}, x_{\bullet})$. On a une action de $\pi_1(\mathbf{X}, x)$ et de $\mathbf{W}$ sur $\tilde{\mathbf{X}}_{\bullet}$ qui se combinent en une action du produit semi-direct $\mathbf{W} \rtimes \pi_1(\mathbf{X}, x)$ transitive sur les fibres du morphisme profini étale $\tilde{\mathbf{X}}_{\bullet} \to \mathbf{X}$. Par la propriété universelle de $\mathbf{X}_{\bullet}$, la donnée de $\tilde{\mathbf{X}}_{\bullet}$ comme ci-dessus revient à la donnée d'une section $\pi^{\bullet}$

$$
\mathbf {W} \rtimes \pi_ {1} (\mathrm{X}, x) \stackrel {{\pi^ {\bullet}}} {{\longrightarrow}} \pi_ {1} (\mathrm{X}, x).
$$

Rappelons que le produit semi-direct $\mathbf{W} \rtimes \pi_1(\mathbf{X}, x)$ a été formé à l'aide de l'homéomorphisme $\rho_{\mathrm{G}}^{\bullet} : \pi_1(\mathbf{X}, x) \to \operatorname{Out}(\mathbf{G})$, construire une section comme ci-dessus revient à solidifier la flèche en pointillé dans le diagramme :

![](images/page_11_image_5.jpg)

Nous utiliserons la même notation $\pi^{\bullet}$ pour désigner l'homomorphisme

$$
\pi^ {\bullet}: \pi_ {1} (\mathrm{X}, x) \to \mathbf {W} \rtimes \operatorname{Out} (\mathbf {G}).
$$

Cet abus de notations ne devrait pas causer de confusion.

1.4. Centralisateur régulier semi-simple. — Comme dans le paragraphe précédent, soit G une forme quasi-déployée du groupe réductif G sur un schéma X.

Notons $\mathfrak{g}^{\mathrm{rs}}$ l'image réciproque de l'ouvert $\mathfrak{c}^{\mathrm{rs}}$ par le morphisme $\chi : \mathfrak{g} \to \mathfrak{c}$. Pour tout $a \in \mathfrak{c}^{\mathrm{rs}}(\bar{k})$, il est bien connu que la fibre $\chi^{-1}(a)$ est formée d'une seule orbite sous l'action adjointe de G. Pour tout $\gamma \in \mathfrak{g}^{\mathrm{rs}}(\bar{k})$, le centralisateur I$_{\gamma}$ de $\gamma$ est un tore maximal de G $\otimes_{k} \bar{k}$.

1.4.1. — Soient  $a \in \mathfrak{c}^{\mathrm{rs}}(\bar{k})$  et  $\gamma, \gamma' \in \chi^{-1}(a)$ . Il existe alors  $g \in \mathrm{G}(\bar{k})$  qui transporte  $\gamma$  sur  $\gamma'$  c'est-à-dire tel que  $\operatorname{ad}(g)\gamma = \gamma'$ . L'automorphisme intérieur  $\operatorname{ad}(g)$  définit donc

un isomorphisme  $\mathrm{ad}(g):\mathbf{I}_{\gamma}\stackrel{\sim}{\to}\mathbf{I}_{\gamma^{\prime}}$ . De plus, si g et  $g^{\prime}$  sont deux éléments de  $\mathbf{G}(\bar{k})$  qui transportent  $\gamma$  sur  $\gamma^{\prime}$ , alors g et  $g^{\prime}$  diffèrent par un élément de  $I_{\gamma}$ . Comme  $I_{\gamma}$  est un tore, en particulier commutatif, les deux isomorphismes

$$
\operatorname{ad} (g) \quad \text {et} \quad \operatorname{ad} (g ^ {\prime}): \mathrm{I} _ {\gamma} \stackrel {{\sim}} {{\to}} \mathrm{I} _ {\gamma^ {\prime}}
$$

sont les mêmes. Ceci démontre que les tores  $I_{\gamma}$  et  $I_{\gamma'}$  sont canoniquement isomorphes. Ceci définit donc un tore qui ne dépend que de a et qui est canoniquement isomorphe à  $I_{\gamma}$  pour tout  $\gamma \in \chi^{-1}(a)$ . Ce tore peut être décrit directement à partir de a à coefficients arbitraires de la façon suivante.

Soient S un X-schéma et $a \in \mathfrak{c}^{\mathrm{rs}}(\mathrm{S})$ un S-point de $\mathfrak{c}^{\mathrm{rs}}$. On appellera revêtement caméral associé à $a$ le W-torseur $\pi_a: \tilde{\mathrm{S}}_a \to \mathrm{S}$ obtenu en formant le diagramme cartésien :

![](images/page_12_image_4.jpg)

Posons

$$
\mathrm{J} _ {a} = \pi_ {a} \wedge^ {\mathrm{W}} \mathrm{T}.\tag{1.4.2}
$$

Le lemme suivant est un cas particulier d'un résultat de Donagi et Gaitsgory qui était probablement bien connu. On rappellera l'énoncé général dans le paragraphe 2.4.

Lemme 1.4.3. — Soient S un X-schéma et $a \in \mathfrak{c}^{\mathrm{rs}}(\mathrm{S})$ un S-point de $\mathfrak{c}^{\mathrm{rs}}$. Soient $x$ un S-point de $\mathfrak{g}^{\mathrm{rs}}(\mathrm{S})$ tel que $\chi(x) = a$ et $\mathrm{I}_x$ l'image réciproque du centralisateur sur $\mathfrak{g}$. Alors on $a$ un isomorphisme canonique $\mathrm{J}_a = \mathrm{I}_x$.

1.4.4. — Considérons une variante pointée de la construction ci-dessus. Choisissons un point géométrique s de S au-dessus de x et  $\tilde{s}$  de  $\tilde{S}_{a}$  au-dessus de s. Comme dans 1.3.6, on a un diagramme commutatif :

![](images/page_12_image_10.jpg)

Le tore  $J_{a}$  s'obtient alors en tordant le tore constant T par l'action de  $\pi_{1}(S, s)$  sur T qui se déduit de l'homomorphisme

$$
\pi_ {a} ^ {\bullet}: \pi_ {1} (\mathrm{S}, s) \to \mathbf {W} \rtimes \operatorname{Out} (\mathbf {G})
$$

c'est-à-dire

$$
\mathrm{J} _ {a} = \mathrm{S} _ {\bullet} \wedge^ {\pi_ {1} (\mathrm{S}, s), \pi_ {a} ^ {\bullet}} \mathbf {T}\tag{1.4.5}
$$

où  $(\mathrm{S}_{\bullet}, s_{\bullet})$  est le revêtement profini étale galoisien universel de  $(\mathrm{S}, s)$ .

1.5. Classes de conjugaison dans une classe stable. — Dans ce paragraphe, G sera une forme quasi-déployée de G sur un corps F contenant k. Nous entendrons par classe de conjugaison stable semi-simple régulière de g sur F un élément  $a \in \mathfrak{c}^{\mathrm{rs}}(\mathrm{F})$ . La définition originale de Langlands des classes de conjugaison stable est plus compliquée mais une fois restreinte aux éléments semi-simples réguliers de l'algèbre de Lie, elle coïncide avec la nôtre. Comme nous nous limitons aux classes de conjugaison stable semi-simples régulières, dans la suite de l'article, par classe de conjugaison stable, nous entendrons semi-simple régulière sauf mention expresse du contraire.

1.5.1. — Soit  $a \in \mathfrak{c}^{\mathrm{rs}}(\mathrm{F})$  une classe de conjugaison stable. Soit  $\gamma_{0} = \epsilon(a) \in \mathfrak{g}(\mathrm{F})$  l'image de a par la section de Kostant. Le centralisateur  $I_{\gamma_{0}}$  de  $\gamma_{0}$  est un tore défini sur F canoniquement isomorphe au tore  $J_{a}$  défini dans le paragraphe précédent cf. 1.4.3. Soit  $\gamma$  un autre F-point de  $\chi^{-1}(a)$ . Comme éléments de  $\mathfrak{g}(\overline{\mathrm{F}})$ ,  $\gamma_{0}$  et  $\gamma$  sont conjugués c'est-à-dire qu'il existe  $g \in \mathrm{G}(\overline{\mathrm{F}})$  tel que  $\gamma = \operatorname{ad}(g)\gamma_{0}$ . Cette identité implique que pour tout  $\sigma \in \operatorname{Gal}(\overline{\mathrm{F}}/\mathrm{F})$ ,  $g^{-1}\sigma(g) \in I_{\gamma_{0}}(\overline{\mathrm{F}})$ . L'application  $\sigma \mapsto g^{-1}\sigma(g)$  définit un élément

$$
\operatorname{inv} \left(\gamma_ {0}, \gamma\right) \in \mathrm{H} ^ {1} \left(\mathrm{F}, \mathrm{I} _ {\gamma_ {0}}\right)
$$

qui ne dépend que de la classe de G(F)-conjugaison de  $\gamma$  et non du choix du transporteur g. L'image de cette classe dans H $^{1}$ (F, G) est triviale par construction. D'après Langlands, l'application  $\gamma \mapsto \text{inv}(\gamma_{0}, \gamma)$  définit une bijection de l'ensemble des classes de G(F)-conjugaison dans l'ensemble des F-points de  $\chi^{-1}(a)$  sur la fibre de l'application H $^{1}$ (F, I $_{\gamma_{0}}$ ) → H $^{1}$ (F, G) au-dessus de l'élément neutre cf. [50]. Cette fibre sera notée

$$
\ker (\mathrm{H} ^ {1} (\mathrm{F}, \mathrm{I} _ {\gamma_ {0}}) \rightarrow \mathrm{H} ^ {1} (\mathrm{F}, \mathrm{G})).
$$

1.5.2. — Au lieu de $\mathfrak{g}(\mathrm{F})$, il est souvent nécessaire de considérer le groupoïde $[\mathfrak{g}/\mathrm{G}](\mathrm{F})$ des couples $(\mathrm{E},\phi)$ composés d'un G-torseur E sur F et d'un F-point $\phi$ de $\mathrm{ad}(\mathrm{E})=\mathrm{E}\wedge^{\mathrm{G}}\mathfrak{g}$. Le morphisme de Chevalley définit un foncteur $[\chi]$ de $[\mathfrak{g}/\mathrm{G}](\mathrm{F})$ dans l'ensemble $\mathfrak{c}(\mathrm{F})$. Soit $a\in\mathfrak{c}^{\mathrm{rs}}(\mathrm{F})$. Considérons le groupoïde des F-points de $[\chi]^{-1}(a)$. Les objets de $[\chi]^{-1}(a)(\mathrm{F})$ sont localement isomorphes pour la topologie étale. Par ailleurs, on a un point base $(\mathrm{E}_{0},\gamma_{0})$ du groupoïde où $\mathrm{E}_{0}$ est le G-torseur trivial et où $\gamma_{0}\in\mathfrak{g}(\mathrm{F})$ est l'élément $\gamma_{0}=\epsilon(a)$ défini par la section de Kostant. Pour tout F-point $(\mathrm{E},\phi)$ de $[\chi]^{-1}(a)$, on obtient un invariant

$$
\operatorname{inv} ((\mathrm{E} _ {0}, \gamma_ {0}), (\mathrm{E}, \phi)) \in \mathrm{H} ^ {1} (\mathrm{F}, \mathrm{I} _ {\gamma_ {0}}).
$$

L'application  $(\mathrm{E},\phi)\mapsto\mathrm{inv}((\mathrm{E}_{0},\gamma_{0}),(\mathrm{E},\phi))$  définit une bijection de l'ensemble des classes d'isomorphisme de  $[\chi]^{-1}(a)(\mathrm{F})$  sur  $\mathrm{H}^{1}(\mathrm{F},\mathrm{I}_{\gamma_{0}})$ .

Soient  $(\mathrm{E},\phi)$  un F-point de  $[\chi]^{-1}(a)$  et  $\operatorname{inv}((\mathrm{E}_{0},\gamma_{0}),(\mathrm{E},\phi))$  son invariant. La classe d'isomorphisme de E correspond alors à l'image de cet invariant dans  $\mathrm{H}^{1}(\mathrm{F},\mathrm{G})$  par l'application

$$
\mathrm{H} ^ {1} (\mathrm{F}, \mathrm{I} _ {\gamma_ {0}}) \rightarrow \mathrm{H} ^ {1} (\mathrm{F}, \mathrm{G}).
$$

On retrouve ainsi la bijection mentionnée plus haut entre les classes de G(F)-conjugaison dans $\chi^{-1}(a)(\mathrm{F})$ et le sous-ensemble de $\mathrm{H}^{1}(\mathrm{F},\mathrm{I}_{\gamma_{0}})$ des éléments d'image triviale dans $\mathrm{H}^{1}(\mathrm{F},\mathrm{G})$.

1.6. Dualité de Tate-Nakayama. — La discussion du paragraphe précédent prend une forme très explicite dans le cas d'un corps local non-archimédien grâce à la dualité de Tate-Nakayama. Soient  $F_{v}$  un corps local non-archimédien,  $O_{v}$  son anneau des entiers et v la valuation. Soit  $F_{v}^{sep}$  une clôture séparable de  $F_{v}$ . Notons  $\Gamma_{v}$  le groupe de Galois  $\mathrm{Gal}(\mathrm{F}_{v}^{\mathrm{sep}}/\mathrm{F}_{v})$ . Notons  $X = \mathrm{Spec}(\mathrm{F}_{v})$  et  $x = \mathrm{Spec}(\mathrm{F}_{v}^{\mathrm{sep}})$  le point géométrique choisi.

1.6.1. — Soit G la forme quasi-déployée sur  $F_{v}$  de G associée à un homomorphisme  $\rho_{\mathrm{G}}^{\bullet}:\Gamma_{v}\to\mathrm{Out}(\mathbf{G})$ . Soit  $\hat{G}$  le dual complexe de G. Par définition il est muni d'un épinglage ( $\hat{T},\hat{B},\hat{x}$ ) dont la donnée radicielle associée s'obtient à partir de celle de G en échangeant les racines et les coracines. En particulier  $\mathrm{Out}(\mathbf{G})=\mathrm{Out}(\hat{\mathbf{G}})$ . On dispose donc d'une action  $\rho_{G}^{\bullet}$  de  $\Gamma_{v}$  sur  $\hat{G}$  fixant l'épinglage.

D'après Kottwitz cf. [41] et [44], H$^{1}$(F, G) est fini et a une structure naturelle de groupe abélien. De plus, son dual de Pontryagin est donné par

$$
\mathrm{H} ^ {1} (\mathrm{F}, \mathrm{G}) ^ {*} = \pi_ {0} ((Z _ {\hat {\mathbf {G}}}) ^ {\rho_ {\mathrm{G}} ^ {\bullet} (\Gamma_ {v})})
$$

où  $(\mathrm{Z}_{\hat{\mathbf{G}}})^{\rho_{\mathrm{G}}^{\bullet}(\Gamma_{v})}$  est le sous-groupe des points fixes dans le centre  $Z_{\hat{G}}$  de  $\hat{G}$  sous l'action de  $\rho_{\mathrm{G}}^{\bullet}(\Gamma_{v})$ . En particulier,  $\mathrm{H}^{1}(\mathrm{F}_{v},\mathrm{G})^{*}$  est un groupe abélien de type fini. Ici, l'exposant \* désigne la dualité de Pontryagin.

1.6.2. — Mettons-nous dans la situation de 1.4.4 avec S = Spec(F$_{v}$) et s = Spec(F$_{v}^{\text{sep}}$). Pour tout a ∈ c$^{\text{rs}}$(F$_{v}$) et γ ∈ t$^{\text{rs}}$(F$_{v}^{\text{rs}}$) au-dessus de a, on a construit comme dans 1.3.6 un homomorphisme de groupes

$$
\pi_ {a} ^ {\bullet}: \Gamma_ {v} \to \mathbf {W} \rtimes \operatorname{Out} (\mathbf {G})
$$

au-dessus de $\rho_{\mathrm{G}}^{\bullet}:\Gamma_{v}\to\mathrm{Out}(\mathbf{G})$. D'après le lemme 1.4.3, on a

$$
\mathrm{I} _ {\gamma} = \mathrm{J} _ {a} = \operatorname{Spec} (\mathrm{F} _ {v} ^ {\text {sep}}) \wedge^ {\Gamma_ {v}, \pi_ {a} ^ {\bullet}} \mathbf {T}.
$$

D'après la dualité de Tate et Nakayama locale [44, 1.1], on a alors

$$
\mathrm{H} ^ {1} (\mathrm{F} _ {v}, \mathrm{J} _ {a}) ^ {*} = \pi_ {0} (\hat {\mathbf {T}} ^ {\pi_ {a} ^ {\bullet} (\Gamma_ {v})}).\tag{1.6.3}
$$

Autrement dit le groupe des caractères complexes de  $\mathrm{H}^{1}(\mathrm{F}_{v},\mathrm{J}_{a})$  coïncide avec le groupe des composantes connexes du groupe des points fixes de  $\pi_{a}^{\bullet}(\Gamma_{v})$  dans  $\hat{T}$ . Bien entendu,  $\hat{T}$  désigne le tore complexe dual de T défini par échange du groupe des caractères et du groupe des cocaractères.

1.6.4. — L'inclusion $\iota: \hat{\mathbf{T}} \hookrightarrow \hat{\mathbf{G}}$ est $\Gamma$-équivariante modulo conjugaison c'est-à-dire que pour tout $t \in \hat{\mathbf{T}}$ et pour tout $\sigma \in \Gamma_v$, $\rho^\bullet(\sigma)(\iota(t))$ et $\iota(\pi_a^\bullet(\sigma)(t))$ sont conjugués dans $\hat{\mathbf{G}}$. On en déduit l'inclusion

$$
(\mathrm{Z} _ {\hat {\mathbf {G}}}) ^ {\rho_ {\mathrm{G}} ^ {\bullet} (\Gamma_ {v})} \subset \hat {\mathbf {T}} ^ {\pi_ {a} ^ {\bullet} (\Gamma_ {v})}
$$

qui induit un homomorphisme entre les groupes de composantes connexes

$$
\pi_ {0} ((Z _ {\hat {\mathbf {G}}}) ^ {\rho_ {\mathrm{G}} ^ {\bullet} (\Gamma_ {v})}) \to \pi_ {0} (\hat {\mathbf {T}} ^ {\pi_ {a} ^ {\bullet} (\Gamma_ {v})}).
$$

Par dualité on retrouve la flèche  $\mathrm{H}^{1}(\mathrm{F}_{v},\mathrm{I}_{\gamma_{0}})\to\mathrm{H}^{1}(\mathrm{F}_{v},\mathrm{G})$  définie dans le paragraphe précédent.

1.7. $\kappa$-intégrales orbitales. — Gardons les notations du paragraphe précédent. Supposons en plus que G soit donné comme forme quasi-déployée de G sur $\mathcal{O}_v$. Le groupe localement compact G(F$_v$) est alors muni d'un sous-groupe ouvert compact maximal G($\mathcal{O}_v$). Soit dg$_v$ la mesure de Haar de G(F$_v$) normalisée de sorte que G($\mathcal{O}_v$) soit de volume un.

Pour $a \in \mathfrak{c}^{\mathrm{rs}}(\mathrm{F}_v)$, donnons-nous une mesure de Haar $\mathrm{dt}_v$ sur le tore $\mathrm{J}_a(\mathrm{F}_v)$. Pour tout $\gamma \in \mathfrak{g}(\mathrm{F}_v)$ avec $\chi(\gamma) = a$, l'isomorphisme canonique $\mathrm{J}_a = \mathrm{I}_\gamma$ permet de transporter la mesure de Haar $\mathrm{dt}_v$ de $\mathrm{J}_a(\mathrm{F}_v)$ en une mesure de Haar sur $\mathrm{I}_\gamma(\mathrm{F}_v)$.

Pour tout $\gamma$ comme ci-dessus, pour toute fonction localement constante $f$ à support compact sur $\mathfrak{g}(\mathrm{F}_{v})$, on peut alors définir l'intégrale orbitale

$$
\mathbf {O} _ {\gamma} (f, \mathrm{d} t _ {v}) = \int_ {\mathrm{I} _ {\gamma} (\mathrm{F} _ {v}) \backslash \mathrm{G} (\mathrm{F} _ {v})} f (\mathrm{ad} (g _ {v}) ^ {- 1} \gamma) \frac {\mathrm{d} g _ {v}}{\mathrm{d} t _ {v}}.
$$

Définition 1.7.1. — Soit $\kappa$ un élément de $\hat{\mathbf{T}}^{\pi_{a}^{\bullet}(\Gamma_{v})}$. Pour toute fonction $f$ localement constante à support compact dans $\mathfrak{g}(\mathrm{F}_{v})$, on définit la $\kappa$-intégrale orbitale de $f$ sur la classe de conjugaison stable $a \in \mathfrak{c}(\mathrm{F}_{v})$ par la formule

$$
\mathbf {O} _ {a} ^ {\kappa} (f, \mathrm{d} t _ {v}) = \sum_ {\gamma} \langle \mathrm{inv} (\gamma_ {0}, \gamma), \kappa \rangle \mathbf {O} _ {\gamma} (f, \mathrm{d} t _ {v})
$$

où $\gamma$ parcourt l'ensemble des classes de $\mathbf{G}(\mathbf{F}_v)$-conjugaison dans la classe stable de caractéristique $a$, où le point base $\gamma_0 = \epsilon(a)$ est défini par la section de Kostant et où $\mathrm{dt}_v$ est une mesure de Haar du tore $\mathrm{J}_a(\mathrm{F}_v)$.

Notons pour mémoire que la définition de la $\kappa$-intégrale orbitale dépend du choix du point géométrique $x_{\rho,a}$ dans $\tilde{\mathbf{X}}_{\rho,a}$ sans lequel on ne peut pas relier le groupe de cohomologie $\mathrm{H}^1 (\mathrm{F}_v,\mathrm{J}_a)$ avec le tore dual $\hat{\mathbf{T}}$ et donc exprimer la dualité de Tate-Nakayama sous la forme 1.6.3.

1.8. Groupes endoscopiques. — Par construction, le groupe dual $\hat{\mathbf{G}}$ est muni d'un épinglage $(\hat{\mathbf{T}},\hat{\mathbf{B}},\hat{\mathbf{x}}_{+})$.

Soit $\kappa$ un élément du tore maximal $\hat{\mathbf{T}}$ dans cet épinglage. La composante neutre du centralisateur de $\kappa$ dans $\hat{\mathbf{G}}$ est un sous-groupe réductif qu'on notera $\hat{\mathbf{H}}$. L'épinglage de $\hat{\mathbf{G}}$ munit à $\hat{\mathbf{H}}$ un tore maximal et un sous-groupe de Borel le contenant. Soit $\mathbf{H}$ le groupe déployé sur $k$ dont la donnée radicielle est duale à celle de $\hat{\mathbf{H}}$. On a en particulier $\mathrm{Out}(\mathbf{H}) = \mathrm{Out}(\hat{\mathbf{H}})$.

Considérons le centralisateur  $(\hat{\mathbf{G}} \rtimes \text{Out}(\mathbf{G}))_{\kappa}$  de  $\kappa$  dans le produit semi-direct  $\hat{G} \rtimes \text{Out}(\mathbf{G})$ . On a la suite exacte

$$
1 \to \hat {\mathbf {H}} \to (\hat {\mathbf {G}} \rtimes \mathrm{Out} (\mathbf {G})) _ {\kappa} \to \pi_ {0} (\kappa) \to 1
$$

où $\pi_0(\kappa)$ est le groupe des composantes connexes de $(\hat{\mathbf{G}} \rtimes \mathrm{Out}(\mathbf{G}))_{\kappa}$. On a alors des homomorphismes canoniques :

![](images/page_16_image_6.jpg)

Définition 1.8.1. — Soit G une forme quasi-déployée de G sur X donnée par un Out(G)-torseur $\rho_{\mathrm{G}}$. Une donnée endoscopique de G sur X est un couple $(\kappa, \rho_{\kappa})$ avec $\kappa$ comme ci-dessus et où $\rho_{\kappa}$ est un $\pi_0(\kappa)$-torseur qui induit $\rho_{\mathrm{G}}$ par le changement de groupes de structure $\mathbf{o}_{\mathbf{G}}(\kappa)$.

Le groupe endoscopique associé à la donnée endoscopique  $(\kappa, \rho_{\kappa})$  est la forme quasi-déployée H sur X de H donnée par le Out(H)-torseur  $\rho_{H}$  obtenu à partir de  $\rho_{\kappa}$  par le changement de groupes de structure  $\mathbf{o}_{\mathbf{H}}(\kappa)$ .

Il y a une variante pointée utile de la notion de donnée endoscopique. Soit X un schéma avec un point géométrique x. Soit G un groupe réductif connexe X forme quasi-déployée du groupe constant G définie par un homomorphisme  $\rho_{\mathrm{G}}^{\bullet}:\pi_{1}(\mathrm{X},x)\to\mathrm{Out}(\mathbf{G})$ .

Définition 1.8.2. — On appelle donnée endoscopique pointée de G sur X un couple  $(\kappa, \rho_{\kappa}^{\bullet})$  où  $\kappa \in \hat{T}$  et  $\rho_{\kappa}^{\bullet}$  est un homomorphisme

$$
\rho_ {\kappa} ^ {\bullet}: \pi_ {1} (\mathrm{X}, x) \to \pi_ {0} (\kappa)
$$

au-dessus de $\rho_{\mathrm{G}}^{\bullet}$.

Avec une donnée endoscopique pointée, on peut former un diagramme commutatif :

![](images/page_17_image_1.jpg)

Le groupe endoscopique H associé à la donnée endoscopique pointée  $(\kappa, \rho_{\kappa}^{\bullet})$  peut être alors formé à l'aide de l'homomorphisme  $\rho_{H}^{\bullet}$ .

1.9. Transfert des classes de conjugaison stable. — Soit  $(\kappa, \rho_{\kappa})$  une donnée endoscopique comme dans 1.8.1. Soit H le groupe endoscopique associé. On va maintenant définir le transfert des classes de conjugaison stable de H à G en construisant un morphisme  $\nu : c_{H} \to c$ .

Par construction, on dispose d'une réduction simultanée des torseurs  $\rho_{G}$  et  $\rho_{H}$  au torseur

$$
\rho_ {\kappa} \rightarrow \mathrm{X}
$$

sous le groupe $\pi_0(\kappa)$. On peut alors réaliser $\mathfrak{c}$ comme le quotient au sens des invariants de $\rho_{\kappa} \times \mathbf{t}$ par l'action de $\mathbf{W} \rtimes \pi_0(\kappa)$. De même, on peut réaliser $\mathfrak{c}_{\mathrm{H}}$ comme le quotient au sens des invariants de $\rho_{\kappa} \times \mathbf{t}$ par l'action de $\mathbf{W}_{\mathbf{H}} \rtimes \pi_0(\kappa)$. Pour définir le morphisme $\mathfrak{c}_{\mathrm{H}} \to \mathfrak{c}$ il suffit de définir un homomorphisme

$$
\mathbf {W} _ {\mathbf {H}} \rtimes \pi_ {0} (\kappa) \rightarrow \mathbf {W} \rtimes \pi_ {0} (\kappa)
$$

compatible avec l'action sur $\rho_{\kappa} \times \mathbf{t}$ ce qui nous conduit au lemme suivant.

Lemme 1.9.1. — Soit $\mathbf{W}_{\mathbf{H}} \rtimes \pi_0(\kappa)$ le produit semi-direct défini par $\mathbf{o}_{\mathbf{H}}(\kappa): \pi_0(\kappa) \to \operatorname{Out}(\mathbf{H})$. Soit $\mathbf{W} \rtimes \pi_0(\kappa)$ le produit semi-direct défini par $\mathbf{o}_{\mathbf{G}}(\kappa): \pi_0(\kappa) \to \operatorname{Out}(\mathbf{G})$. Il existe un homomorphisme canonique

$$
\mathbf {W} _ {\mathbf {H}} \rtimes \pi_ {0} (\kappa) \rightarrow \mathbf {W} \rtimes \pi_ {0} (\kappa)
$$

qui induit l'homomorphisme évident sur les sous-groupes normaux  $W_{H} \subset W$ , induit l'identité sur le quotient  $\pi_{0}(\kappa)$  et qui est compatible avec les actions de  $W_{H} \rtimes \pi_{0}(\kappa)$  et  $W \rtimes \pi_{0}(\kappa)$  sur T.

Démonstration. — Rappelons que le centralisateur  $(\mathbf{W} \rtimes \operatorname{Out}(\mathbf{G}))_{\kappa}$  de  $\kappa$  dans  $\mathbf{W} \rtimes \operatorname{Out}(\mathbf{G})$  est canoniquement isomorphe au produit semi-direct  $\mathbf{W}_{\mathbf{H}} \rtimes \pi_{0}(\kappa)$  cf. [57,

lemme 10.1]. On en déduit un homomorphisme $\theta : \pi_0(\kappa) \to \mathbf{W} \rtimes \mathrm{Out}(\mathbf{G})$ de sorte qu'on a un homomorphisme de groupes

$$
\mathbf {W} _ {\mathbf {H}} \rtimes \pi_ {0} (\kappa) \rightarrow \mathbf {W} \rtimes^ {\theta} \pi_ {0} (\kappa)
$$

où le second produit semi-direct est formé à l'aide de l'action de $\pi_0(\kappa)$ sur $\mathbf{W}$ définie par l'homomorphisme $\theta : \pi_0(\kappa) \to \mathbf{W} \rtimes \operatorname{Out}(\mathbf{G})$ et de l'action de $\mathbf{W} \rtimes \operatorname{Out}(\mathbf{G})$ sur $\mathbf{W}$. Cet homomorphisme est visiblement compatible avec les actions sur $\mathbf{t}$.

Il reste à construire un isomorphisme entre produits semi-directs

$$
\mathbf {W} \rtimes^ {\theta} \pi_ {0} (\kappa) \rightarrow \mathbf {W} \rtimes \pi_ {0} (\kappa)
$$

dont le second est formé à l'aide de l'homomorphisme  $\mathbf{o}_{\mathbf{G}}(\kappa):\pi_{0}(\kappa)\to\mathrm{Out}(\mathbf{G})$ . Pour tout  $\alpha\in\pi_{0}(\kappa)$ , l'élément  $\theta(\alpha)\in\mathbf{W}\rtimes\mathrm{Out}(\mathbf{G})$  s'écrit de manière unique sous la forme  $\theta(\alpha)=w(\alpha)\mathbf{o}_{\mathbf{G}}(\alpha)$  où  $w(\alpha)\in\mathbf{W}$ . Ceci nous permet de définir un homomorphisme

$$
\pi_ {0} (\kappa) \rightarrow \mathbf {W} \rtimes \pi_ {0} (\kappa)
$$

par la formule $\alpha \mapsto w(\alpha)\alpha$. Cet homomorphisme induit un isomorphisme $\mathbf{W} \rtimes^{\theta} \pi_{0}(\kappa) \to \mathbf{W} \rtimes \pi_{0}(\kappa)$ qui rend le diagramme

![](images/page_18_image_8.jpg)

commutatif. En particulier, cet isomorphisme est compatible avec les actions sur t. □

Au-dessus de l'ouvert semi-simple régulier  $c^{rs}$  de c, on a un morphisme fini et étale

$$
\nu^ {\mathrm{rs}}: \mathfrak {c} _ {\mathrm{H}} ^ {\mathrm{G} - \mathrm{rs}} \to \mathfrak {c} ^ {\mathrm{rs}}
$$

où on a noté  $c_{H}^{G-rs}$  l'image réciproque de  $c^{rs}$  dans  $c_{H}$ . Ce morphisme réalise le transfert des classes de conjugaison stable de H qui sont semi-simples et G-régulières vers les classes de conjugaison stable de G qui sont semi-simples régulières.

Lemme 1.9.2. — Soient $a_{\mathrm{H}} \in \mathfrak{c}_{\mathrm{H}}^{\mathrm{G} - \mathrm{rs}}(\mathrm{S})$ un point à valeur dans un schéma S et $a \in \mathfrak{c}^{\mathrm{rs}}(\mathrm{S})$ son image. Alors, on a un isomorphisme canonique entre le tore $\mathbf{J}_a$ défini par la formule (1.4.2) et le tore $\mathbf{J}_{\mathrm{H},a_{\mathrm{H}}}$ défini par la même formule appliquée à H.

Démonstration. — Après avoir choisi les pointages, on peut appliquer la formule (1.4.5) pour décrire  $J_{a}$  et  $J_{a_{H}}$ . Pour construire l'isomorphisme entre ces deux tores, il faut démontrer que les homomorphismes  $\rho_{\kappa}^{\bullet}\circ\pi_{a}^{\bullet}:\pi_{1}(S,s)\to\mathbf{W}\rtimes\pi_{0}(\kappa)$  et  $\rho_{\kappa}^{\bullet}\circ\pi_{a_{H}}^{\bullet}:\pi_{1}(S,s)\to\mathbf{W}_{\mathbf{H}}\rtimes\pi_{0}(\kappa)$  construits comme dans 1.3.6 définissent la même action de  $\pi_{1}(S,s)$  sur Aut(T). Mais ceci résulte directement du lemme précédent 1.9.1. ☐

Remarque 1.9.3. — Soit maintenant S = Spec(F$_{v}$) où F$_{v}$ est un corps local comme dans 1.6. En choisissant un F$_{v}^{\text{sep}}$-point dans le torseur $\pi_{a_{\text{H}}}$, on obtient un homomorphisme $\rho_{\kappa}^{\bullet} \circ \pi_{a_{\text{H}}}^{\bullet} : \Gamma_{v} \to \mathbf{W}_{\text{H}} \rtimes \pi_{0}(\kappa)$. On a alors la dualité de Tate-Nakayama 1.6.3

$$
\mathrm{H} ^ {1} (\mathrm{F} _ {v}, \mathrm{J} _ {a}) ^ {*} = \mathrm{H} ^ {1} (\mathrm{F} _ {v}, \mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}}}) ^ {*} = \hat {\mathbf {T}} ^ {\pi_ {a _ {\mathrm{H}}} ^ {\bullet} (\Gamma_ {v})}.
$$

Par construction, $\kappa \in \hat{\mathbf{T}}^{\mathbf{W}_{\mathrm{H}} \rtimes \pi_0(\kappa)}$ de sorte qu'on peut définir la $\kappa$-intégrale orbitale $\mathbf{O}_a^\kappa(f, \mathrm{d}t_v)$ suivant 1.7.1.

1.10. Discriminant et résultant. — Soit  $\Phi$  le système de racines associé au groupe déployé G. Pour toute racine  $\alpha \in \Phi$ , on note  $d\alpha \in k[t]$  la dérivée du caractère  $\alpha : T \to G_{m}$ . Formons le discriminant

$$
\underline {{\mathfrak {D}}} _ {\mathbf {G}} = \prod_ {\alpha \in \Phi} \mathrm{d} \alpha \in k [ \mathbf {t} ]
$$

qui est clairement un élément W-invariant de cette algèbre de polynômes. Il définit donc une fonction sur l'espace des polynômes caractéristiques  $\mathbf{c} = \operatorname{Spec}(k[\mathbf{t}]^{\mathbf{W}})$ . Soit  $D_{G}$  le diviseur de c défini par cette fonction. Rappelons l'énoncé bien connu.

Lemme 1.10.1. — Le diviseur $\mathfrak{D}_{\mathbf{G}}$ est un diviseur réduit de $\mathbf{c}$. Le morphisme $\pi_{\mathbf{t}}: \mathbf{t} \to \mathbf{c}$ est étale au-dessus du complément de ce diviseur qui n'est autre que l'ouvert $\mathbf{c}^{\mathrm{rs}}$. De plus, ce diviseur est stable sous l'action de $\operatorname{Out}(\mathbf{G})$.

Démonstration. — La seule chose non triviale à vérifier ici est que $\mathfrak{D}_{\mathbf{G}}$ est un diviseur réduit. Puisqu'il s'agit d'une intersection complète, il suffit de montrer qu'un ouvert dense de $\mathfrak{D}_{\mathbf{G}}$ est réduit. On peut donc ôter de $\mathfrak{D}_{\mathbf{G}}$ l'image des points de t appartenant à plus de deux hyperplans de racine. On se ramène alors au cas d'un groupe de rang semi-simple un où l'assertion peut être vérifiée à la main.

Soient X un k-schéma et G une forme quasi-déployée de G sur X donnée par un Out(G)-torseur  $\rho_{G}$ . En tordant  $D_{G}$  par  $\rho_{G}$ , on obtient un diviseur réduit  $D_{G}$  de c dont l'ouvert complémentaire est  $c^{rs}$ . Soit  $(\kappa, \rho_{\kappa})$  une donnée endoscopique cf. 1.8.1 de G. On a un diviseur  $D_{H}$  de  $c_{H}$  et par torsion un diviseur  $D_{H}$  de  $c_{H}$ .

L'énoncé suivant m'a été indiqué par deux des référés anonymes.

Lemme 1.10.2. — Choisissons un sous-ensemble $\Psi \subset \Phi - \Phi_{\mathbf{H}}$ tel que pour toute paire de racines opposées $\pm \alpha \in \Phi - \Phi_{\mathbf{H}}$, le cardinal de $\{\pm \alpha\} \cap \Psi$ vaut un. La fonction $\prod_{\alpha \in \Psi} d\alpha \in k[\mathbf{t}]$ est alors stable sous l'action de $\mathbf{W}_{\mathbf{H}}$.

Démonstration. — Un élément  $w \in W_{H}$  agit sur  $\Phi - \Phi_{H}$  en envoyant une paire de racines opposées  $\{\pm\alpha\} \subset \Phi - \Phi_{H}$  sur une paire généralement différente de racines opposées dans le même ensemble. Il s'ensuit qu'il existe un signe  $\epsilon(w)$  tel que

$w(\prod_{\alpha \in \Psi} \mathrm{d}\alpha) = \epsilon(w) \prod_{\alpha \in \Psi} \mathrm{d}\alpha$ et que ce signe ne dépend pas du choix de l'ensemble $\Psi$. Il reste à démontrer que ce signe vaut un.

Choisissons un sous-ensemble $\Psi_{\mathbf{G}} \subset \Phi$ tel que pour toute paire de racines opposées $\pm \alpha \in \Phi$, le cardinal de $\{\pm \alpha\} \cap \Psi_{\mathbf{G}}$ vaut un. Soit $\Psi_{\mathbf{H}} = \Psi_{\mathbf{G}} \cap \Phi_{\mathbf{H}}$. On peut aussi supposer que $\Psi_{\mathbf{G}} = \Psi_{\mathbf{H}} \cup \Psi$. Pour tout $w \in \mathbf{W}$, il existe un signe $\epsilon_{\mathbf{G}}(w)$ tel que $w(\prod_{\alpha \in \Psi_{\mathbf{G}}} \mathrm{d}\alpha) = \epsilon_{\mathbf{G}}(w) \prod_{\alpha \in \Psi_{\mathbf{G}}} \mathrm{d}\alpha$ et ce signe ne dépend pas du choix de $\Psi_{\mathbf{G}}$. En prenant $\Psi_{\mathbf{G}}$ l'ensemble des racines positives, on voit que $\epsilon_{\mathbf{G}}(w) = (-1)^{\ell_{\mathbf{G}}(w)}$ où $\ell_{\mathbf{G}}(w)$ est la longueur habituelle de $w$ dans le groupe de Coxeter $\mathbf{W}_{\mathbf{G}}$. Si $w \in \mathbf{W}_{\mathbf{H}}$, on a aussi la formule $w(\prod_{\alpha \in \Psi_{\mathbf{H}}} \mathrm{d}\alpha) = \epsilon_{\mathbf{H}}(w) \prod_{\alpha \in \Psi_{\mathbf{H}}} \mathrm{d}\alpha$ avec $\epsilon_{\mathbf{G}}(w) = (-1)^{\ell_{\mathbf{H}}(w)}$.

Pour démontrer que $\epsilon(w)=1$, il nous reste à démontrer l'égalité

$$
(- 1) ^ {\ell_ {\mathbf {G}} (w)} = (- 1) ^ {\ell_ {\mathbf {H}} (w)}.
$$

Notons que ces signes peuvent tous les deux s'interpréter comme le déterminant de la représentation de réflexion. L'égalité de signes résulte de ce que la représentation de réflexion de  $W_{H}$  s'obtient de celle de  $W_{G}$  par restriction. ☐

1.10.3. — Soit $\mathfrak{R}_{\mathbf{H}}^{\mathbf{G}}$ le diviseur effectif de $\mathbf{c}_{\mathbf{H}}$ défini par la fonction invariante $\prod_{\alpha \in \Psi} \mathrm{d}\alpha \in k[\mathbf{t}]^{\mathbf{W}_{\mathbf{H}}}$ du lemme précédent. On a alors l'égalité de diviseurs

$$
\nu^ {*} \mathfrak {D} _ {\mathbf {G}} = \mathfrak {D} _ {\mathbf {H}} + 2 \mathfrak {R} _ {\mathbf {H}} ^ {\mathbf {G}}.
$$

Soit $(\kappa, \rho_{\kappa})$ une donnée endoscopique cf. 1.8.1 de G. En tordant $\mathfrak{R}_{\mathbf{H}}^{\mathbf{G}}$ par $\rho_{\kappa}$, on obtient un diviseur effectif $\mathfrak{R}_{\mathrm{H}}^{\mathrm{G}}$ sur $\mathfrak{c}_{\mathrm{H}}$ qui vérifie la relation

$$
\nu^ {*} \mathfrak {D} _ {\mathrm{G}} = \mathfrak {D} _ {\mathrm{H}} + 2 \mathfrak {R} _ {\mathrm{H}} ^ {\mathrm{G}}.
$$

1.11. Le lemme fondamental pour les algèbres de Lie. — On est maintenant en position d'énoncer le lemme fondamental pour les algèbres de Lie, conjecturé par Langlands, Shelstad et sa variante de Waldspurger.

Soient  $F_{v}$  un corps local non-archimédien,  $O_{v}$  son anneau des entiers et  $v : F_{v}^{\times} \to Z$  la valuation discrète. Soit  $F_{q}$  le corps résiduel de  $O_{v}$ . Soit  $X_{v} = \text{Spec}(\mathcal{O}_{v})$ . Soit  $F_{v}^{sep}$  une clôture séparable de  $F_{v}$ . Celle-ci définit un point géométrique x de  $X_{v}$ .

Soit G une forme quasi-déployée de G sur  $O_{v}$  définie par un homomorphisme  $\rho_{\mathrm{G}}^{\bullet}:\pi_{1}(\mathrm{X}_{v},x)\to\mathrm{Out}(\mathbf{G})$ . Considérons une donnée endoscopique pointée  $(\kappa,\rho_{\kappa}^{\bullet})$  formée d'un élément  $\kappa\in\hat{T}$  et d'un homomorphisme  $\rho_{\kappa}^{\bullet}:\pi_{1}(\mathrm{X}_{v},x)\to\pi_{0}(\kappa)$  au-dessus de  $\rho_{G}^{\bullet}$  cf. 1.8.2. On a alors un schéma en groupes réductifs H au-dessus de  $X_{v}$  et un morphisme de  $X_{v}$ -schémas  $c_{H}\to c$ .

Soit $a_{\mathrm{H}} \in \mathfrak{c}_{\mathrm{H}}(\mathcal{O}_{v})$ d'image $a \in \mathfrak{c}(\mathcal{O}_{v}) \cap \mathfrak{c}^{\mathrm{rs}}(\mathrm{F}_{v})$. Choissons une mesure de Haar $\mathrm{dt}_{v}$ sur le tore $\mathrm{J}_{a}(\mathrm{F}_{v})$. D'après le lemme 1.9.2, on a un isomorphisme entre les tores $\mathrm{J}_{a}$ et $\mathrm{J}_{\mathrm{H},a_{\mathrm{H}}}$ de sorte qu'on peut transporter la mesure de Haar $\mathrm{dt}_{v}$ sur $\mathrm{J}_{\mathrm{H},a_{\mathrm{H}}}(\mathrm{F}_{v})$.

En choisissant un  $F_{v}^{sep}$ -point  $x_{a}$  comme dans 1.9.3, on peut définir la  $\kappa$ -intégrale orbitale  $O_{a}^{\kappa}$  de n'importe quelle fonction localement constante à support compact dans

$\mathfrak{g}(\mathrm{F}_{v})$ . Notons  $l_{g_{v}}$  la fonction caractéristique de  $\mathfrak{g}(\mathcal{O}_{v})$  dans  $\mathfrak{g}(\mathrm{F}_{v})$  et  $l_{h_{v}}$  la fonction caractéristique de  $\mathfrak{h}(\mathcal{O}_{v})$  dans  $\mathfrak{h}(\mathrm{F}_{v})$ .

## Théorème 1.11.1. — Avec les notations ci-dessus, on a l'égalité

$$
\mathbf {O} _ {a} ^ {\kappa} (1 _ {\mathfrak {g} _ {v}}, \mathrm{d} t _ {v}) = q ^ {r _ {\mathrm{H}, v} ^ {\mathrm{G}} (a _ {\mathrm{H}})} \mathbf {S O} _ {a _ {\mathrm{H}}} (1 _ {\mathfrak {h} _ {v}}, \mathrm{d} t _ {v})
$$

$o\dot{u} r_{\mathrm{H},v}^{\mathrm{G}}(a_{\mathrm{H}})=\deg_{v}(a_{\mathrm{H}}^{*}\mathfrak{R}_{\mathrm{H}}^{\mathrm{G}}).$

Ce théorème est la variante pour les algèbres de Lie de la conjecture originale de Langlands et Shelstad qui porte sur les groupes de Lie sur un corps local non-archimédien. Cette variante a été formulée par Waldspurger qui a démontré qu'elle implique la conjecture originale pour les groupes de Lie. Il a aussi démontré que le cas où F est un corps local de caractéristique positive ne divisant pas l'ordre de W implique le cas où F est un corps local de caractéristique nulle et dont la caractéristique résiduelle ne divise pas l'ordre de W cf. [82]. Nous nous limitons au premier cas.

L'énoncé original de Langlands-Shelstad est sensiblement plus compliqué notamment à cause de la présence d'un signe dans le facteur de transfert. Dans [46], Kottwitz a établi le lien entre le facteur de transfert de Langlands-Shelstad et la section de Kostant qui nous permet d'énoncer la conjecture de Langlands et Shelstad sous cette forme plus simple. Dans le cas des groupes classiques, Waldspurger a donné une forme plus explicite de cette conjecture dans [81]. Hales a également écrit un article d'exposition fort agréable [32] sur l'énoncé de la conjecture de Langlands-Shelstad.

1.11.2. — Notons que l'énoncé ci-dessus s'étend trivialement au cas où on part d'un élément  $a_{\mathrm{H}} \in \mathfrak{c}^{\mathrm{G-rs}}(\mathrm{F}_{v})$  qui n'est pas dans  $\mathfrak{c}_{\mathrm{H}}(\mathcal{O}_{v})$ . Dans ce cas, on a également  $a \notin \mathfrak{c}(\mathcal{O}_{v})$ . Ceci se déduit en effet du critère valuatif de propreté appliqué au morphisme fini  $\nu_{\mathrm{H}} : \mathfrak{c}_{\mathrm{H}} \to \mathfrak{c}$ . Il est alors évident que les intégrales orbitales  $\mathbf{O}_{a}^{\kappa}(1_{\mathfrak{g}_{v}}, dt_{v})$  et  $\mathbf{SO}_{a_{\mathrm{H}}}(1_{\mathfrak{h}_{v}}, dt_{v})$  sont nulles.

## 1.11.3. — Notons enfin que l'égalité de diviseurs

$$
a _ {*} \mathfrak {D} _ {\mathrm{G}} = a _ {\mathrm{H}} ^ {*} \mathfrak {D} _ {\mathrm{H}} + 2 a _ {\mathrm{H}} ^ {*} \mathfrak {R} _ {\mathrm{G}} ^ {\mathrm{H}}
$$

qui se déduit de 1.10.3, implique

$$
\Delta_ {\mathrm{H}} (a _ {\mathrm{H}}) \Delta_ {\mathrm{G}} (a) ^ {- 1} = q ^ {\deg_ {v} (a _ {\mathrm{H}} ^ {*} \mathfrak {R} _ {\mathrm{G}} ^ {\mathrm{H}})}
$$

avec $\Delta_{\mathrm{H}}(a_{\mathrm{H}}) = q^{-\deg (a_{\mathrm{H}}^{*}\mathfrak{D}_{\mathrm{H}}) / 2}$ et $\Delta_{\mathrm{G}}(a) = q^{-\deg (a^{*}\mathfrak{D}_{\mathrm{G}}) / 2}$. Ceci permet de réécrire la formule 1.11.1 sous la forme plus habituelle

$$
\Delta_ {\mathrm{G}} (a) \mathbf {O} _ {a} ^ {\kappa} (1 _ {\mathfrak {g} _ {v}}, \mathrm{d} t _ {v}) = \Delta_ {\mathrm{H}} (a _ {\mathrm{H}}) \mathbf {S O} _ {a _ {\mathrm{H}}} (1 _ {\mathfrak {h} _ {v}}, \mathrm{d} t _ {v}).
$$

1.12. Le lemme fondamental non standard. — Dans [83], Waldspurger a formulé une variante de la conjecture de Langlands-Shelstad qu'il appelle le lemme fondamental non standard. Dans ce paragraphe, nous allons rappeler cette conjecture.

Soient  $G_{1}$  et  $G_{2}$  deux groupes réductifs déployés sur k avec épinglages. Pour tout  $i \in \{1, 2\}$ , on a en particulier un tore maximal  $T_{i}$  de  $G_{i}$ , l'ensemble des racines  $\Phi_{i} \subset \mathbf{X}^{*}(\mathbf{T}_{i})$ , l'ensemble des racines simples  $\Delta_{i} \subset \Phi_{i}$  ainsi que l'ensemble des coracines  $\Phi_{i}^{\vee} \subset \mathbf{X}_{*}(\mathbf{T}_{i})$ . Le quintuple

$$
(\mathbf {X} ^ {*} (\mathbf {T} _ {i}), \mathbf {X} _ {*} (\mathbf {T} _ {i}), \Phi_ {i}, \Phi_ {i} ^ {\vee}, \Delta_ {i})
$$

est la donnée radicielle associée au groupe épinglé  $G_{i}$  et qui le détermine à isomorphisme unique près.

Définition 1.12.1. — Une isogénie de données radicielles entre $\mathbf{G}_{1}$ et $\mathbf{G}_{2}$ consiste en un couple d'isomorphismes de $\mathbf{Q}$-espaces vectoriels

$$
\psi^ {*}: \mathbf {X} ^ {*} (\mathbf {T} _ {2}) \otimes \mathbf {Q} \longrightarrow \mathbf {X} ^ {*} (\mathbf {T} _ {1}) \otimes \mathbf {Q}
$$

et

$$
\psi_ {*}: \mathbf {X} _ {*} (\mathbf {T} _ {1}) \otimes \mathbf {Q} \longrightarrow \mathbf {X} _ {*} (\mathbf {T} _ {2}) \otimes \mathbf {Q}
$$

transposés l'un de l'autre tels que $\psi^{*}$ met en bijection l'ensemble des $\mathbf{Q}$-droites de la forme $\mathbf{Q}\alpha_{2}$ avec $\alpha_{2} \in \Phi_{2}$ sur l'ensemble des $\mathbf{Q}$-droites de la forme $\mathbf{Q}\alpha_{1}$ avec $\alpha_{1} \in \Phi_{1}$ en faisant correspondre les droites des racines simples aux droites des racines simples. La même propriété est exigée pour $\psi_{*}$ vis-à-vis de l'ensemble des $\mathbf{Q}$-droites engendrées par les coracines.

Exemple 1.12.2. — Deux groupes semi-simples ayant le même groupe adjoint ont des données radicielles isogènes. En effet dans ce cas, on a un isomorphisme canonique $\mathbf{X}^{*}(\mathbf{T}_{1})\otimes\mathbf{Q}\to\mathbf{X}^{*}(\mathbf{T}_{2})\otimes\mathbf{Q}$ qui respecte l'ensemble des racines et celui des racines simples et dont l'isomorphisme dual respecte les coracines.

Exemple 1.12.3. — L'exemple le plus intéressant est celui de deux groupes réductifs duaux au sens de Langlands. Supposons que G est un groupe simple pour simplifier. Par définition, la donnée radicielle du groupe dual $\hat{\mathbf{G}}$ s'obtient à partir de celle de G en échangeant le groupe des caractères avec le groupe des cocaractères, l'ensemble des racines avec l'ensemble des coracines. On a alors un isomorphisme d'espaces vectoriels $\mathbf{X}^{*}(\mathbf{T})\otimes\mathbf{Q}\to\mathbf{X}_{*}(\mathbf{T})\otimes\mathbf{Q}$ qui envoie une racine courte $\alpha$ sur la coracine $\check{\alpha}$ correspondante, et une racine longue $\alpha$ sur $n\check{\alpha}$ où $n=|\alpha_{\mathrm{long}}|^{2}/|\alpha_{\mathrm{court}}|^{2}$. Au cas où il n'y a qu'une seule longueur de racines, on les voit toutes comme courtes. Les cas les plus intéressants sont $\mathrm{B}_{n}\leftrightarrow\mathrm{C}_{n},\mathrm{F}_{4}$ et $\mathrm{G}_{2}$ où il existe des racines de longueur différente. On se réfère à [83, page 14] pour une discussion plus détaillée.

1.12.4. — Puisque la réflexion associée à une racine  $\alpha$  ne dépend que de la Q-droite passant par  $\alpha$, les isomorphismes  $\psi^{*}$  et  $\psi_{*}$  induisent un isomorphisme entre les groupes de Weyl  $W_{1} \stackrel{\sim}{\to} W_{2}$  de deux groupes réductifs  $G_{1}$  et  $G_{2}$  appariés.

1.12.5. — Soient  $G_{1}$  et  $G_{2}$  deux groupes déployés dont les données radicielles sont isogènes. Soit  $Out_{12}$  le groupe des automorphismes de  $\mathbf{X}_{*}(\mathbf{T}_{1}) \otimes \mathbf{Q}$  qui laissent stables  $\Phi_{1}, \Delta_{1}$  mais également  $\mathbf{X}^{*}(\mathbf{T}_{2}), \Phi_{2}, \Delta_{2}$  vu comme sous-ensembles de  $\mathbf{X}_{*}(\mathbf{T}_{1}) \otimes \mathbf{Q}$  et de même pour les automorphismes duaux de  $\mathbf{X}_{*}(\mathbf{T}_{1}) \otimes \mathbf{Q}$ . Pour tout k-schéma X, pour tout  $Out_{12}$  torseur  $\rho_{12}$ , on peut tordre  $G_{1}$  et  $G_{2}$  munis de leurs épinglages par  $\rho_{12}$  pour obtenir des formes quasi-déployées  $G_{1}$  et  $G_{2}$ . Les couples des formes quasi-déployées obtenus par ce procédé sont appelés appariés.

Étant donné l'isomorphisme $\psi^{*}$ entre les $\mathbf{Q}$-espaces vectoriels

$$
\mathbf {X} ^ {*} (\mathbf {T} _ {1}) \otimes \mathbf {Q} \simeq \mathbf {X} ^ {*} (\mathbf {T} _ {2}) \otimes \mathbf {Q},
$$

on peut comparer la position de deux réseaux  $\mathbf{X}^{*}(\mathbf{T}_{1})$  et  $\mathbf{X}^{*}(\mathbf{T}_{2})$  vus comme réseaux dans un même Q-espace vectoriel. Un nombre premier p est dit bon par rapport à  $\psi^{*}$  si p ne divise pas les entiers

$$
\left| \mathbf {X} ^ {*} (\mathbf {T} _ {1}) / \left(\mathbf {X} ^ {*} (\mathbf {T} _ {1}) \cap \mathbf {X} ^ {*} (\mathbf {T} _ {2})\right) \right| \quad \text {et} \quad \left| \mathbf {X} ^ {*} (\mathbf {T} _ {2}) / \left(\mathbf {X} ^ {*} (\mathbf {T} _ {2}) \cap \mathbf {X} ^ {*} (\mathbf {T} _ {1})\right) \right|.
$$

Si k est un corps de caractéristique bonne par rapport à  $\psi^{*}$ , celui-ci induira un isomorphisme  $\mathbf{X}^{*}(\mathbf{T}_{1})\otimes k\stackrel{\sim}{\to}\mathbf{X}^{*}(\mathbf{T}_{2})\otimes k$ .

Lemme 1.12.6. — Soient  $G_{1}$  et  $G_{2}$  deux groupes appariés au-dessus d'une base X de bonnes caractéristiques résiduelles. Soient  $T_{1}$  et  $T_{2}$  les tores maximaux des épinglages de  $G_{1}$  et  $G_{2}$  et  $t_{1}$,  $t_{2}$  leurs algèbres de Lie. Alors il existe un isomorphisme canonique  $t_{1} \rightarrow t_{2}$  et un isomorphisme compatible  $v : c_{G_{1}} \stackrel{\sim}{\rightarrow} c_{G_{2}}$.

Démonstration. — On a

$$
\mathbf {t} _ {i} = \mathrm{Spec} (\mathrm{Sym} _ {\mathcal {O} _ {\mathrm{X}}} (\mathbf {X} ^ {*} (\mathbf {T} _ {i}) \otimes \mathcal {O} _ {\mathrm{X}}))
$$

où  $\text{Sym}_{\mathcal{O}_{\mathrm{X}}}(X^{*}(T_{i}) \otimes \mathcal{O}_{\mathrm{X}})$  est la  $O_{X}$ -algèbre symétrique associée au  $O_{X}$ -module libre  $\mathbf{X}^{*}(T_{i}) \otimes \mathcal{O}_{\mathrm{X}}$ . Si les caractéristiques résiduelles de X sont bonnes,  $\psi^{*}$  induit un isomorphisme de  $O_{X}$ -modules libres

$$
\mathbf {X} ^ {*} (\mathbf {T} _ {2}) \otimes \mathcal {O} _ {\mathrm{X}} \longrightarrow \mathbf {X} ^ {*} (\mathbf {T} _ {1}) \otimes \mathcal {O} _ {\mathrm{X}}
$$

et donc un isomorphisme $\mathbf{t}_1 \xrightarrow{\sim} \mathbf{t}_2$. On a déjà vu que $(\psi^*, \psi_*)$ induit un isomorphisme $\mathbf{W}_1 \xrightarrow{\sim} \mathbf{W}_2$ qui est visiblement compatible avec leurs actions sur $\mathbf{t}_1 \xrightarrow{\sim} \mathbf{t}_2$. Il en résulte un isomorphisme entre

$$
\mathbf {c} _ {1} = \operatorname{Spec} (\operatorname{Sym} _ {\mathcal {O} _ {\mathrm{X}}} (\mathbf {X} ^ {*} (\mathbf {T} _ {i}) \otimes \mathcal {O} _ {\mathrm{X}})) ^ {\mathbf {w} _ {1}}
$$

et

$$
\mathbf {c} _ {2} = \operatorname{Spec} (\operatorname{Sym} _ {\mathcal {O} _ {\mathrm{X}}} (\mathbf {X} ^ {*} (\mathbf {T} _ {i}) \otimes \mathcal {O} _ {\mathrm{X}})) ^ {\mathbf {w} _ {2}}.
$$

En appliquant la torsion extérieure par $\rho_{12}$, on obtient l'isomorphisme $\mathfrak{c}_1 = \mathfrak{c}_2$ qu'on voulait.

Mettons-nous sous l'hypothèse du lemme précédent. Soit X le disque  $\operatorname{Spec}(\mathcal{O}_{v})$  où  $O_{v}=k[[\epsilon_{v}]]$  avec k un corps fini de caractéristique bonne par rapport à  $\psi^{*}$ . Soient  $a_{1}\in\mathfrak{c}_{\mathrm{G}_{1}}(\mathcal{O}_{v})$  et  $a_{2}\in\mathfrak{c}_{\mathrm{G}_{2}}(\mathcal{O}_{v})$  tels que  $\nu(a_{1})=a_{2}$ . L'isogénie  $T_{1}\to T_{2}$  donnée par  $\psi^{*}$  induit par torsion une isogénie des tores  $J_{a_{1}}\to J_{a_{2}}$  d'après 1.4.3. De plus, l'isogénie induit un isomorphisme entre les algèbres de Lie de ces tores sous l'hypothèse que la caractéristique est bonne par rapport à  $\psi$ . On peut donc transporter des mesures de Haar de  $J_{a_{1}}(F_{v})$  à  $J_{a_{2}}(F_{v})$  et inversement. On va utiliser la même notation  $dt_{v}$  pour ces mesures de Haar compatibles.

Théorème 1.12.7. — Supposons que la caractéristique résiduelle est supérieure à deux fois le nombre de Coxeter de  $G_{1}$  et de  $G_{2}$ . On a l'égalité suivante entre les intégrales orbitales stables

$$
\mathbf {S O} _ {a _ {1}} (1 _ {\mathrm{G} _ {1}}, \mathrm{d} t _ {v}) = \mathbf {S O} _ {a _ {2}} (1 _ {\mathrm{G} _ {2}}, \mathrm{d} t _ {v})
$$

où $1_{\mathbf{G}_i}$ est la fonction caractéristique du compact $\mathfrak{g}_i(\mathcal{O}_v)$ dans $\mathfrak{g}_i(\mathrm{F}_v)$.

Cette égalité a été conjecturée par Waldspurger qui l'appelle le lemme fondamental non standard. Dans [83], il a démontré que la conjonction du lemme fondamental ordinaire 1.11.1 et du lemme non standard ci-dessus implique le lemme fondamental tordu.

1.13. Formule globale de stabilisation. — Revenons à la conjecture de Langlands-Shelstad. Le lemme fondamental consiste en une identité d'intégrales orbitales locales. Il sera néanmoins nécessaire de le replacer dans son contexte global d'origine qui est la stabilisation de la formule des traces. Nous allons donc passer en revue la structure de la partie anisotrope sur un corps global de caractéristique positive. Cette revue nous servira de guide plus tard pour étudier la structure de la cohomologie de la fibration de Hitchin.

Soient  $k = F_{q}$  et F le corps des fonctions rationnelles sur une courbe projective lisse géométriquement connexe X sur k. Pour tout point fermé  $v \in |X|$ , notons  $F_{v}$  la complétion de F selon la valuation définie par v et  $O_{v}$  son anneau des entiers. Pour simplifier, nous allons supposer dans cette discussion que G est un groupe semi-simple déployé.

Pour toute classe $\xi\in\mathrm{H}^{1}(\mathrm{F},\mathrm{G})$, on note $\mathrm{G}^{\xi}$ la forme intérieure de $\mathrm{G}$ définie par l'image de $\xi$ dans $\mathrm{H}^{1}(\mathrm{F},\mathrm{G}^{\mathrm{ad}})$. On appellera la forme $\mathrm{G}^{\xi}$ ainsi définie une forme intérieure forte. Au lieu de considérer la formule des traces de $\mathrm{G}$, on va considérer la somme des formules des traces sur les formes intérieures fortes qui sont localement triviales. La

stabilisation de la somme devient plus simple et admet une interprétation géométrique plus directe. Le processus de stabilisation qu'on va présenter est dû à Langlands et Kott-witz cf. [50] et [44]. Nous reprenons ici l'exposition de [58].

Considérons donc la somme

$$
\sum_ {\xi \in \ker^ {1} (\mathrm{F}, \mathrm{G})} \sum_ {\gamma \in \mathfrak {g} ^ {\xi , \operatorname{ani} (\mathrm{F}) / \sim}} \mathbf {O} _ {\gamma} (1 _ {\mathrm{D}})\tag{1.13.1}
$$

où

(1) $\ker^1 (\mathbf{F},\mathbf{G})$ est l'ensemble des classes d'isomorphisme des G-torseurs sur F d'image triviale dans les $\mathrm{H}^1 (\mathrm{F}_v,\mathrm{G})$ pour tous $v\in |\mathbf{X}|$.

(2) $\mathfrak{g}^{\xi}$ est la forme de $\mathfrak{g}$ sur F définie par $\xi$.

(3) $\gamma$ parcourt l'ensemble des classes de conjugaison régulières semi-simples de $\mathfrak{g}^{\xi}(\mathrm{F})$ dont le centralisateur dans $\mathfrak{g}^{\xi}(\mathrm{F}\otimes_{k}\bar{k})$ est un tore anisotrope.

(4)  $\mathbf{O}_{\gamma}(1_{\mathrm{D}})$  est l'intégrale orbitale globale

$$
\mathbf {O} _ {\gamma} (1 _ {\mathrm{D}}) = \int_ {\mathrm{G} _ {\gamma} ^ {\xi} (\mathrm{F}) \backslash \mathrm{G} (\mathbf {A})} 1 _ {\mathrm{D}} (a \mathrm{d} (g) ^ {- 1} \gamma) d g
$$

de la fonction

$$
\mathrm{l} _ {\mathrm{D}} = \bigotimes_ {v \in | \mathrm{X} |} \mathrm{l} _ {\mathrm{D} _ {v}}: \mathfrak {g} (\mathbf {A}) \longrightarrow \mathbf {C}
$$

D étant un diviseur  $\sum_{v\in|X|}d_{v}v$ ,  $1_{D_{v}}$  étant la fonction caractéristique du compact ouvert  $\varepsilon^{-d_{v}}\mathfrak{g}(\mathcal{O}_{v})$  de  $\mathfrak{g}(\mathrm{F}_{v})$ , les entiers  $d_{v}$  étant des entiers pairs, nuls sauf pour un nombre fini de places v. L'intégrale est convergente pour les classes anisotropes  $\gamma$ .

(5) dg est la mesure de Haar normalisée de  $\mathrm{G}(\mathbf{A})$  de telle façon que  $\mathrm{G}(\mathcal{O}_{\mathbf{A}})$  soit de volume un.

Considérons le morphisme caractéristique de Chevalley $\chi : \mathfrak{g} \to \mathfrak{c}$ ainsi que ses formes tordues

$$
\chi^ {\xi}: \mathfrak {g} ^ {\xi} \longrightarrow \mathfrak {c}
$$

par les classes $\xi \in \mathrm{H}^1 (\mathrm{F},\mathrm{G})$. Notons que le groupe des automorphismes de G agit sur $\mathfrak{c}$ à travers le groupe des automorphismes extérieurs de sorte que la torsion par les $\xi$ n'affecte pas $\mathfrak{c}$. Toute classe de conjugaison $\gamma$ de $\mathfrak{g}^{\xi}(\mathrm{F})$ définit donc un élément $a\in \mathfrak{c}(\mathrm{F})$. Comme le centralisateur de $\gamma$ semi-simple régulier ne dépend que de $a$, il existe un sous-ensemble $\mathfrak{c}^{\mathrm{ani}}(\mathrm{F})$ de $\mathfrak{c}(\mathrm{F})$ des éléments $a$ provenant des classes $\gamma$ semi-simples régulières et anisotropes dans $\mathfrak{g}^{\xi}(\mathrm{F}\otimes_{k}\bar{k})$. La somme (1.13.1) peut se réécrire comme une somme sur les $a\in \mathfrak{c}^{\mathrm{ani}}(\mathrm{F})$:

$$
\sum_ {a \in \mathfrak {c} ^ {\text {ani}} (\mathrm{F})} \sum_ {\xi \in \ker^ {1} (\mathrm{F}, \mathrm{G})} \sum_ {\gamma \in \mathfrak {g} ^ {\xi} (\mathrm{F}) / \sim ,   \chi (\gamma) = a} \mathbf {O} _ {\gamma} (1 _ {\mathrm{D}}).\tag{1.13.2}
$$

Pour chaque élément $a \in \mathfrak{c}^{\mathrm{ani}}(\mathrm{F})$, la section de Kostant 1.2.1 produit un élément $\gamma_0 = \epsilon(a) \in \mathfrak{g}(\mathrm{F})$ d'image $\chi(\gamma_0) = a$. On a noté $\mathrm{J}_a$ le centralisateur $\mathrm{I}_{\gamma_0}$ de $\gamma_0$. Puisqu'on s'est restreint à la partie semi-simple régulière anisotrope, $\mathrm{J}_a$ est un tore anisotrope. Le tore dual $\hat{\mathrm{J}}_a$ défini sur $\bar{\mathbf{Q}}_\ell$ est muni d'une action finie de $\Gamma = \mathrm{Gal}(\bar{\mathrm{F}}/\mathrm{F})$ telle que le groupe $\hat{\mathrm{J}}_a^\Gamma$ des points fixes est un groupe fini.

Pour tout $\xi \in \ker^{1}(\mathrm{F},\mathrm{G})$, les classes de conjugaison $\gamma \in \mathfrak{g}^{\xi}(\mathrm{F})$ telles que $\chi (\gamma) = a$ sont en bijection avec les classes de cohomologie

$$
\alpha = \mathrm{inv} (\gamma_ {0}, \gamma) \in \mathrm{H} ^ {1} (\mathrm{F}, \mathrm{J} _ {a})
$$

dont l'image dans  $\mathrm{H}^{1}(\mathrm{F},\mathrm{G})$  est l'élément  $\xi$ . Ainsi l'ensemble des paires  $(\xi,\gamma)$  de la somme (1.13.2) où  $\xi\in\ker^{1}(\mathrm{F},\mathrm{G})$  et  $\gamma$  est une classe de conjugaison de  $\mathfrak{g}^{\xi}(\mathrm{F})$  d'image  $a\in\mathfrak{c}^{\mathrm{ani}}(\mathrm{F})$  est en bijection avec

$$
\ker \left[ \mathrm{H} ^ {1} (\mathrm{F}, \mathrm{J} _ {a}) \rightarrow \bigoplus_ {v \in | \mathrm{X} |} \mathrm{H} ^ {1} (\mathrm{F} _ {v}, \mathrm{G}) \right].
$$

Pour qu'une collection de classes de conjugaison $(\gamma_v)_{v\in |\mathrm{X}|}$ de $\mathfrak{g}(\mathrm{F}_v)$ avec $\chi (\gamma_v) = a$ provienne d'une paire $(\xi ,\gamma)$ de la somme (1.13.2), il faut et il suffit que $\gamma_{v} = \gamma_{0}$ pour presque tout $v$ et que

$$
\sum_ {v \in | \mathrm{X} |} \alpha_ {v} | _ {\hat {\mathrm{I}} _ {a} ^ {\Gamma}} = 0\tag{1.13.3}
$$

où $\alpha_v = \mathrm{inv}_v(\gamma_0, \gamma_v)$ d'après [41]. Si c'est le cas, le nombre de paires $(\xi, \gamma)$ qui s'envoient sur cette collection $(\gamma_v)_{v \in |\mathbf{X}|}$ est égal au cardinal du groupe

$$
\ker^ {1} (\mathrm{F}, \mathrm{J} _ {a}) = \ker \left[ \mathrm{H} ^ {1} (\mathrm{F}, \mathrm{J} _ {a}) \rightarrow \bigoplus_ {v \in | \mathrm{X} |} \mathrm{H} ^ {1} (\mathrm{F} _ {v}, \mathrm{J} _ {a}) \right].
$$

On va maintenant faire entrer en jeu les intégrales orbitales locales. Soit $\bigotimes_{v\in|\mathbf{F}|}dt_v$ la mesure de Tamagawa sur $\mathrm{J}_a(\mathbf{A})$ cf. [62]. Dans le cas où $\mathrm{J}_a$ est un tore anisotrope, le quotient $\mathrm{J}_a(\mathrm{F})\backslash \mathrm{J}_a(\mathbf{A}_{\mathrm{F}})$ est compact. Son volume

$$
\tau (\mathrm{J} _ {a}) = \operatorname{vol} \left(\mathrm{J} _ {a} (\mathrm{F}) \backslash \mathrm{J} _ {a} (\mathbf {A}), \bigotimes_ {v \in | \mathrm{X} |} \mathrm{d} t _ {v}\right)
$$

est le nombre de Tamagawa. Rappelons la formule d'Ono [62]

$$
\left| \ker^ {1} (\mathrm{F}, \mathrm{J} _ {a}) \right| \tau (\mathrm{J} _ {a}) = \left| \pi_ {0} (\hat {\mathrm{J}} _ {a} ^ {\Gamma}) \right|.\tag{1.13.4}
$$

La somme (1.13.2) se réécrit maintenant comme suit

$$
\sum_ {a \in \mathfrak {c} ^ {\mathrm{ani}} (\mathrm{F})} \left| \ker^ {1} (\mathrm{F}, \mathrm{J} _ {a}) \right| \tau (\mathrm{J} _ {a}) \sum_ {(\gamma_ {v}) _ {v \in | \mathrm{X} |}} \prod_ {v} \mathbf {O} _ {\gamma_ {v}} (1 _ {\mathrm{D} _ {v}}, \mathrm{d} t _ {v})\tag{1.13.5}
$$

où les $\gamma_v$ sont des classes de conjugaison de $\mathfrak{g}(\mathrm{F}_v)$ vérifiant l'équation (1.13.3). En mettant en facteur le nombre de Tamagawa $\tau(\mathrm{J}_a)$, on trouve une somme de produits d'intégrales orbitales locales $\prod_v \mathbf{O}_{\gamma_v}(1_{\mathrm{D}_v}, \mathrm{d}t_v)$ au lieu des intégrales orbitales globales $\mathbf{O}_{\gamma}(1_{\mathrm{D}})$. En appliquant la formule d'Ono (1.13.4), la somme (1.13.2) devient

$$
\sum_ {a \in \mathfrak {c} ^ {\mathrm{ani}} (\mathrm{F})} \left| \pi_ {0} (\hat {\mathrm{J}} _ {a} ^ {\Gamma}) \right| \sum_ {(\gamma_ {v}) _ {v \in | \mathrm{X} |}} \prod_ {v} \mathbf {o} _ {\gamma_ {v}} (1 _ {\mathrm{D} _ {v}}, \mathrm{d} t _ {v})\tag{1.13.6}
$$

où les $(\gamma_v)$ vérifient la condition (1.13.3). Notons qu'avec l'hypothèse $J_a$ anisotrope, le groupe $\hat{J}_a^\Gamma$ est un groupe fini de sorte que $\pi_0(\hat{J}_a^\Gamma) = \hat{J}_a^\Gamma$.

En utilisant la transformation de Fourier sur le groupe fini $\hat{\mathbf{J}}_a^\Gamma$, la somme (1.13.2) devient

$$
\sum_ {a \in \mathfrak {c} ^ {\mathrm{ani}} (\mathrm{F})} \sum_ {\kappa \in \hat {\mathrm{J}} _ {a} ^ {\Gamma}} \mathbf {O} _ {a} ^ {\kappa} \left(1 _ {\mathrm{D}}, \bigotimes_ {v \in | \mathrm{X} |} \mathrm{d} t _ {v}\right)\tag{1.13.7}
$$

avec

$$
\mathbf{O}_{a}^{\kappa}\Bigg(1_{\mathrm{D}},\bigotimes_{v\in |\mathrm{X}|}\mathrm{d}t_{v}\Bigg) = \prod_{v\in |\mathrm{X}|}\sum_{\substack{\gamma_{v}\in \mathfrak{g}(\mathrm{F}_{v}) / \sim \\ \chi (\gamma_{v}) = a}}\langle \operatorname{inv}_{v}(\gamma_{0},\gamma_{v}),\kappa \rangle \mathbf{O}_{\gamma_{v}}(1_{\mathrm{D}_{v}},\mathrm{d}t_{v}).\tag{1.13.8}
$$

L'opération suivante consiste à permuter la sommation sur les $a$ et la sommation sur les $\kappa$. En choisissant un plongement de $\hat{\mathbf{J}}_a$ dans $\hat{\mathbf{G}}$, $\kappa$ définit une classe de conjugaison semi-simple $[\kappa]$. L'intersection $\hat{\mathbf{J}}_a^\Gamma \cap [\kappa]$ de $\hat{\mathbf{J}}_a^\Gamma$ avec la classe de conjugaison $[\kappa]$ ne dépend pas du choix de plongement de $\hat{\mathbf{J}}_a$ dans $\hat{\mathbf{G}}$. La somme (1.13.2) devient maintenant

$$
\sum_ {[ \kappa ] \in \hat {\mathrm{G}} / \sim} \sum_ {a \in \mathfrak {c} ^ {\text {ani}} (\mathrm{F})} \sum_ {\kappa \in \hat {\mathrm{J}} _ {a} ^ {\Gamma} \cap [ \kappa ]} \mathbf {O} _ {a} ^ {\kappa} \left(1 _ {\mathrm{D}}, \bigotimes_ {v \in | \mathrm{X} |} \mathrm{d} t _ {v}\right).\tag{1.13.9}
$$

Rappelons qu'on a supposé que G est un groupe semi-simple adjoint. Pour chaque classe de conjugaison  $[\kappa]$  on choisit un représentant  $\kappa \in \hat{G}$ . Comme  $\hat{G}$  est un groupe semi-simple simplement connexe,  $\hat{G}_{\kappa}$  est un groupe réductif connexe. Soit  $\hat{H} = \hat{G}_{\kappa}$  et H le groupe réductif dual de  $\hat{H}$ . Comme on ne s'intéresse qu'à la partie anisotrope on écarte tous les H qui ne sont pas semi-simples. Supposons donc H semi-simple et regardons le morphisme

$$
\nu_ {\mathrm{H}}: \mathfrak {c} _ {\mathrm{H}} ^ {\text { ani }} (\mathrm{F}) \longrightarrow \mathfrak {c} ^ {\text { ani }} (\mathrm{F}).
$$

Un élément $a$ est dans l'image de $\nu_{\mathrm{H}}$ si et seulement si $\hat{\mathsf{J}}_a^\Gamma \cap [\kappa]$ est non-vide. En général, on a une bijection canonique entre l'ensemble $\hat{\mathsf{J}}_a^\Gamma \cap [\kappa]$ et l'ensemble des $a_{\mathrm{H}} \in \mathfrak{c}_{\mathrm{H}}^{\mathrm{ani}}(\mathrm{F})$ dans la préimage de $a$.

En supposant le lemme fondamental, la somme (1.13.2) devient

$$
\sum_ {\mathrm{H}} \sum_ {a _ {\mathrm{H}} \in \mathfrak {c} _ {\mathrm{H}} ^ {\text {ani}} (\mathrm{F})} \mathbf {s o} _ {a} \left(1 _ {\mathrm{D}}, \bigotimes_ {v \in | \mathrm{X} |} \mathrm{d} t _ {v}\right)\tag{1.13.10}
$$

où la première somme porte sur l'ensemble des classes d'équivalence des groupes endoscopiques elliptiques de G.

Comme nous l'avons remarqué dans [57, 1], le comptage des points à valeurs dans un corps fini de l'espace de module des fibrés de Higgs donne essentiellement l'expression (1.13.2). On y a d'ailleurs proposé une interprétation géométrique du processus de stabilisation (1.13.2)=(1.13.7) comme une décomposition de la cohomologie de la fibration de Hitchin par rapport à l'action de ses symétries naturelles. Il s'agit donc d'une décomposition en somme directe d'un complexe pur sur la base de la fibration de Hitchin.

L'égalité  $(1.13.2)=(1.13.10)$  sera interprétée comme une égalité dans un groupe de Grothendieck entre deux complexes purs. Le théorème 6.4.2 est une variante précise de cette interprétation dont on déduira le lemme fondamental de Langlands-Shelstad 1.11.1.

## 2. Centralisateur régulier et section de Kostant

Nous rappelons ici la construction du centralisateur régulier et du morphisme du centralisateur régulier vers le centralisateur de [57]. Nous rappelons aussi la description galoisienne du centralisateur régulier de Donagi et Gaitsgory [23].

On garde les notations de 1.3. En particulier, G est un groupe réductif déployé sur un corps k et G est une forme quasi-déployée de G sur un k-schéma X. On suppose que la caractéristique de k ne divise pas l'ordre de W.

2.1. Centralisateur régulier. — Soit I le schéma en groupes des centralisateurs au-dessus de g. La fibre de I au-dessus d'un point x de g est le sous-groupe de G qui centralise x

$$
\mathrm{I} _ {x} = \{g \in \mathrm{G} | \mathrm{ad} (g) x = x \}.
$$

La dimension de  $I_{x}$  dépend en général de x de sorte que I n'est pas plat sur g mais la restriction  $I^{reg}$  de I à l'ouvert  $g^{reg}$  est un schéma en groupes lisse de dimension relative r. Puisque sa fibre générique est un tore, c'est un schéma en groupes commutatif lisse.

Le lemme [57, 3.2] suivant est le point de départ de notre étude de la fibration de Hitchin. Pour la commodité du lecteur, nous allons rappeler brièvement sa démonstration.

Lemme 2.1.1. — Il existe un unique schéma en groupes lisse commutatif J sur c muni d'un isomorphisme G-équivariant

$$
(\chi^ {*} \mathrm{J}) | _ {\mathfrak {g} ^ {\mathrm{reg}}} \stackrel {{\sim}} {{\to}} \mathrm{I} | _ {\mathfrak {g} ^ {\mathrm{reg}}}.
$$

De plus, cet isomorphisme se prolonge en un homomorphisme $\chi^{*}\mathrm{J}\to\mathrm{I}$.

Démonstration. — Soient  $x_{1}, x_{2}$  deux points de  $\mathfrak{g}^{\mathrm{reg}}(\bar{k})$  tels que  $\chi(x_{1}) = \chi(x_{2}) = a$ . Soient  $I_{x_{1}}$  et  $I_{x_{2}}$  les fibres de I en  $x_{1}$  et  $x_{2}$ . Il existe  $g \in \mathrm{G}(\bar{k})$  tel que  $\operatorname{ad}(g)x_{1} = x_{2}$ . La conjugaison par g induit un isomorphisme  $I_{x_{1}} \to I_{x_{2}}$  qui de surcroît ne dépend pas du choix de g puisque  $I_{x_{1}}$  est commutatif. Ceci permet de définir la fibre  $J_{a}$  de J en a.

La définition de J comme un schéma en groupes affine au-dessus de c procède par descente fidèlement plate. Notons  $I_{1}^{reg}$  et  $I_{2}^{reg}$  les schémas en groupes sur  $g^{reg} \times_{c} g^{reg}$  images réciproques de  $I^{reg} = I|_{g^{reg}}$  par la première et la deuxième projection. La donnée de descente de  $I^{reg}$  le long du morphisme  $\chi^{reg} : g^{reg} \to c$  consiste en un isomorphisme  $\sigma_{12} : I_{2}^{reg} \to I_{1}^{reg}$  qui vérifie une condition de cocycle. Nous allons construire  $\sigma_{12}$  en laissant le soin de vérifier la condition de cocycle au lecteur.

La construction de l'isomorphisme  $\sigma_{12}$  se fait aussi par descente. Considérons le morphisme

$$
\mathrm{G} \times \mathfrak {g} ^ {\text { reg }} \rightarrow \mathfrak {g} ^ {\text { reg }} \times_ {\mathfrak {c}} \mathfrak {g} ^ {\text { reg }}
$$

défini par  $(g, x) \to (x, \operatorname{ad}(g)x)$ . C'est un morphisme lisse surjectif donc a fortiori fidèlement plat. Au-dessus de  $G \times g^{reg}$ , on a un isomorphisme canonique entre  $I_{1}^{reg}$  et  $I_{2}^{reg}$  qui consiste en la structure G-équivariante de I. Pour que cet isomorphisme descendé à  $g^{reg} \times_{c} g^{reg}$ , il faut vérifier une identité au-dessus du carré de  $G \times g^{reg}$  au-dessus de  $g^{reg} \times_{c} g^{reg}$ . Après avoir identifié ce carré à  $G \times I_{1}^{reg}$ , l'identité à vérifier se déduit de la commutativité du  $g^{reg}$ -schéma en groupes  $I_{1}^{reg}$ .

On a donc construit un schéma en groupes lisse commutatif J au-dessus de c muni d'un isomorphisme G-équivariant  $\chi^{*}J|_{g^{reg}} \to I|_{g^{reg}}$ . Cet isomorphisme s'étend en un homomorphisme de schéma en groupes  $\chi^{*}J \to I$  puisque  $\chi^{*}J$  est un k-schéma lisse, I est un k-schéma affine et de plus  $\chi^{*}J - \chi^{*}J|_{g^{reg}}$  est un fermé de codimension trois de  $\chi^{*}J$ . ☐

Nous appelons J le centralisateur régulier. On peut en fait prendre comme définition  $J := \epsilon^{*}I$  où  $\epsilon$  est la section de Kostant de 1.2. Notons que J est muni d'une structure  $G_{m}$ -équivariante pour l'action de  $G_{m}$  sur c définie par les exposants. Par descente, on a un schéma en groupes sur  $[c/G_{m}]$  qu'on notera également J, voir [57, 3.3].

2.2. Sur le quotient  $[g/G]$ . — Le morphisme de Chevalley  $\chi : g \to c$  étant G-invariant, il se factorise par le champ quotient  $[g/G]$  et le morphisme

$$
[ \chi ]: [ \mathfrak {g} / \mathrm{G} ] \to \mathfrak {c}.
$$

Rappelons que  $[\mathfrak{g}/G]$  associe à tout k-schéma S le groupoïde des couples  $(E, \phi)$  où E est un G-torseur sur S et où  $\phi$  est une section du fibré adjoint ad(E) associée à la représentation adjointe de G.

Au-dessus de c, on a défini un schéma en groupes commutatif lisse J. Soit BJ le classifiant de J qui associe à tout c-schéma S le groupoïde de Picard des J-torseurs sur S. Le lemme 2.1.1 montre qu'on a une action de BJ sur [g/G] au-dessus de c. En effet, on peut tordre un couple (E,  $\phi \in [\mathfrak{g}/\mathrm{G}](\mathrm{S})$  par un J-torseur à l'aide de l'homomorphisme  $\chi^{*}J \to I$  de 2.1.1.

Proposition 2.2.1. — Le morphisme $[\chi^{\mathrm{reg}}]:[\mathfrak{g}^{\mathrm{reg}} / \mathrm{G}]\to \mathfrak{c}$ est une gerbe liée par le centralisateur régulier J. De plus, cette gerbe est neutre.

Démonstration. — L’assertion que  $[\chi^{reg}]$  est une gerbe se déduit du fait que la restriction de l’homomorphisme  $\chi^{*}J\to I$  à  $g^{reg}$  est un isomorphisme G-équivariant par construction de J. La section de Kostant  $\epsilon:c\to g^{reg}$  composée avec le morphisme quotient  $g^{reg}\to[g^{reg}/G]$  neutralise la gerbe. Nous noterons ce point  $[\epsilon]:c\to[g^{reg}/G]$ . ☐

2.2.2. — Il n'est donc pas déraisonnable de penser  $[g/G]$  comme une sorte de compactification du champ de Picard BJ. C'est un moule avec lequel on fabrique des situations géométriques plus concrètes comme la fibre de Springer affine et la fibration de Hitchin en évaluant sur différents schémas S. Pour les fibres de Springer affines, on l'évalue sur l'anneau des séries formelles à une variable cf. 3. Pour la fibration de Hitchin, on l'évalue sur une courbe projective lisse cf. 4. Pour cette dernière, on a besoin de tenir compte aussi de l'action de  $G_{m}$  qui agit par homothétie sur g.

2.2.3. — Le centralisateur régulier J est muni d'une action de  $G_{m}$  qui relève l'action de  $G_{m}$  sur c. Le classifiant BJ au-dessus de  $[c/G_{m}]$  agit sur  $[g/G \times G_{m}]$ . Ce dernier contient comme ouvert  $[g^{reg}/G \times G_{m}]$ . Le morphisme

$$
[ \chi^ {\mathrm{reg}} / \mathbf {G} _ {m} ]: [ \mathfrak {g} ^ {\mathrm{reg}} / \mathrm{G} \times \mathbf {G} _ {m} ] \to [ \mathfrak {c} / \mathbf {G} _ {m} ]\tag{2.2.4}
$$

est encore une gerbe liée par J. Cette gerbe n'est pas neutre en général. Elle le devient néanmoins après l'extraction d'une racine carrée du fibré inversible universel sur  $BG_{m}$ . Considérons l'homomorphisme [2]:  $G_{m} \rightarrow G_{m}$  défini par  $t \mapsto t^{2}$ . Il induit un morphisme B[2]:  $BG_{m} \rightarrow BG_{m}$  qui consiste en l'extraction d'une racine carrée du fibré inversible universel sur  $BG_{m}$ . Nous indiquons par un exposant [2] le changement de base par ce morphisme. En particulier, on a un morphisme

$$
[ \chi / \mathbf {G} _ {m} ] ^ {[ 2 ]}: [ \mathfrak {g} / \mathrm{G} \times \mathbf {G} _ {m} ] ^ {[ 2 ]} \to [ \mathfrak {c} / \mathbf {G} _ {m} ] ^ {[ 2 ]}.
$$

En effet,  $[\mathfrak{c}/\mathbf{G}_{m}]^{[2]}$  est le quotient de c par l'action de  $G_{m}$  définie comme le carré de l'action par les exposants et  $[\mathfrak{g}/\mathrm{G}\times\mathbf{G}_{m}]^{[2]}$  est le quotient de g par l'action adjointe de G et le carré de l'homothétie. Considérons le composé de deux homomorphismes

$$
\mathbf {G} _ {m} \rightarrow \mathrm{T} \times \mathbf {G} _ {m} \rightarrow \mathrm{G} \times \mathbf {G} _ {m}
$$

dont le premier est défini par $t \mapsto (2\rho(t), t)$ où $2\rho$ est la somme des coracines positives. La section de Kostant $1.2 \epsilon : \mathfrak{c} \to \mathfrak{g}$ est équivariante par rapport à cet homomorphisme de sorte qu'il induit une section de $[\chi / \mathbf{G}_m]^{[2]}$. Nous pouvons reformuler ce qui précède d'une façon plus commode.

Lemme 2.2.5. — Soient S un k-schéma muni d'un fibré inversible D et  $h_{D}: S \to BG_{m}$  le morphisme associé vers le classifiant de  $G_{m}$ . Soit  $a: S \to [c/G_{m}]$  un morphisme au-dessus de  $h_{D}$ . La section de Kostant et le choix d'une racine carrée D' de D nous permettent de définir une section

$$
[ \epsilon ] ^ {\mathrm{D} ^ {\prime}} (a): \mathrm{S} \to [ \mathfrak {g} ^ {\mathrm{reg}} / \mathrm{G} \times \mathbf {G} _ {m} ].
$$

2.3. Le centre de G et les composantes connexes de J. — Le contenu de ce paragraphe est bien connu.

Proposition 2.3.1. — Si G est un groupe de centre connexe, le centralisateur régulier J a des fibres connexes.

Démonstration. — Dans le cas d'un élément nilpotent régulier, il s'agit d'un théorème de Springer cf. [75, III, 3.7 et 1.14] et [73, théorème 4.11]. Le cas général s'y ramène par la décomposition de Jordan. Soit $x \in \mathfrak{g}(\bar{k})$ un point géométrique de $\mathfrak{g}$ qui est régulier. Soit $x = s + n$ sa décomposition de Jordan où $s \in \mathfrak{g}(\bar{k})$ est un élément semi-simple et $n \in \mathfrak{g}(\bar{k})$ est un élément nilpotent tel que $[s, n] = 0$. D'après [38, 3, lemme 8], le centralisateur $G_s$ de $s$ est un sous-groupe réductif connexe de $G$ et de plus, son centre est connexe. On applique donc le théorème de Springer à l'élément nilpotent régulier $n$ de $\text{Lie}(G_s)$.

Corollaire 2.3.2. — Pour tout $x \in \mathfrak{g}^{\mathrm{reg}}(\bar{k})$, l'homomorphisme canonique $Z_{G} \to I_{x}$ induit un homomorphisme surjectif $\pi_0(Z_G) \to \pi_0(I_x)$.

Démonstration. — Soient  $G^{ad}$  le groupe adjoint de G et  $I_{x}^{ad}$  le centralisateur de x dans  $G^{ad}$ . On a la suite exacte

$$
1 \to \mathrm {Z_ {G}} \to \mathrm{I} _ {x} \to \mathrm{I} _ {x} ^ {\mathrm{ad}} \to 1.
$$

Puisque  $I_{x}^{ad}$  est un groupe connexe par la proposition qui précède, la flèche canonique  $\pi_{0}(Z_{\mathrm{G}})\to\pi_{0}(\mathrm{I}_{x})$  est surjective. ☐

2.4. Description galoisienne de J. — A la suite de Donagi et Gaitsgory [23], on peut décrire le schéma en groupes J au-dessus de c à l'aide du revêtement fini et plat  $\pi : t \to c$ . Notre présentation sera un peu différente de la leur.

Considérons la restriction à la Weil du tore T × t sur t

$$
\Pi := \prod_ {t / c} (T \times t) = \pi_ {*} (T \times t).
$$

Comme schéma en groupes sur c et pour tout c-schéma S, on a

$$
\Pi (\mathrm{S}) = \operatorname{Hom} _ {\mathfrak {t}} (\mathrm{S} \times_ {\mathfrak {c}} \mathfrak {t}, \mathrm{T} \times \mathfrak {t}).
$$

La représentabilité se déduit de ce que le morphisme $\mathfrak{t} \to \mathfrak{c}$ est fini et plat cf. [10, 7.6]. Comme la restriction à la Weil préserve la lissité, $\Pi$ est un schéma en groupes lisse et commutatif au-dessus de $\mathfrak{c}$ de dimension relative $r\sharp\mathbf{W}$. Au-dessus de l'ouvert $\mathfrak{c}^{\mathrm{rs}}$, le revêtement $\mathfrak{t}^{\mathrm{rs}} \to \mathfrak{c}^{\mathrm{rs}}$ est fini étale de sorte que la restriction de $\Pi$ à cet ouvert est un tore.

Le S-schéma en groupes fini étale W agit simultanément sur T et t. L'action diagonale de W sur  $T \times t$  induit une action de W sur  $\Pi$ . Les points fixes par W définissent un sous-foncteur fermé  $J^{1}$  de  $\Pi$ .

Lemme 2.4.1. — Le sous-schéma fermé J$^{1}$ de Π est un schéma en groupes commutatif et lisse au-dessus de c.

Démonstration. — Puisque la restriction de scalaires à la Weil préserve la lissité, Π est lisse au-dessus de c. Puisque l'ordre de W est premier à la caractéristique, les points fixes de W dans le schéma lisse Π forment un sous-schéma fermé J$^{1}$ lisse sur c. □

La proposition qui suit est un renforcement de (1.4.2).

Proposition 2.4.2. — Il existe un homomorphisme canonique  $J \rightarrow J^{1}$  qui de plus est un isomorphisme au-dessus de l'ouvert  $c^{rs}$  de c.

Démonstration. — Commençons par construire un homomorphisme de J dans la restriction à la Weil  $\pi_{*}(T \times t)$ . Par adjonction, il revient au même de construire un homomorphisme

$$
\pi^ {*} \mathrm{J} \rightarrow \mathrm{T} \times \mathfrak {t}
$$

de schémas en groupes au-dessus de t.

Rappelons la résolution simultanée de Grothendieck et Springer. Soit $\tilde{\mathfrak{g}}$ le schéma des couples $(x,g\mathrm{B})$ où $x\in \mathfrak{g}$ et $g\mathrm{B}\in \mathrm{G / B}$ qui vérifie $\mathrm{ad}(g)^{-1}(x)\in \mathrm{Lie}(\mathrm{B})$. Ici, B désigne le sous-groupe de Borel de l'épinglage de G. Notons $\pi_{\mathfrak{g}}:\tilde{\mathfrak{g}}\to \mathfrak{g}$ la projection sur la variable $x$. La projection $\operatorname {Lie}(\mathrm{B})\to t$ définit un morphisme $\tilde{\chi}:\tilde{\mathfrak{g}}\to t$ qui complète le carré commutatif:

$$
\begin{array}{c} \tilde {\mathfrak {g}} \xrightarrow {\tilde {\chi}} \mathfrak {t} \\ \pi_ {\mathfrak {g}} \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow \pi \\ \mathfrak {g} \xrightarrow {\chi} \mathfrak {c} \end{array}
$$

De plus, si on se restreint à l'ouvert  $g^{reg}$  de g, on obtient un diagramme cartésien :

$$
\begin{array}{c c c} \tilde {\mathfrak {g}} ^ {\text {reg}} & \xrightarrow {\tilde {\chi} ^ {\text {reg}}} & \mathsf {t} \\ \pi_ {\mathfrak {g}} ^ {\text {reg}} \Big \downarrow & & \Big \downarrow \pi \\ \mathfrak {g} ^ {\text {reg}} & \xrightarrow {\chi^ {\text {reg}}} & \mathsf {c} \end{array}
$$

D'après 2.1.1, $(\chi^{\mathrm{reg}})^{*}\mathrm{J} = \mathrm{I}|_{\mathfrak{g}^{\mathrm{reg}}}$ si bien que pour construire un homomorphisme de t-schémas en groupes $\pi^{*}\mathrm{J}\to (\mathrm{T}\times \mathfrak{t})$, il suffit de construire un homomorphisme de $\tilde{\mathfrak{g}}^{\mathrm{reg}}$-schémas en groupes

$$
(\pi_ {\mathfrak {g}} ^ {\mathrm{reg}}) ^ {*} (\mathrm{I} | _ {\mathfrak {g} ^ {\mathrm{reg}}}) \to \mathrm{T} \times \tilde {\mathfrak {g}} ^ {\mathrm{reg}}
$$

qui soit G-équivariant. Nous avons besoin d'un lemme.

Lemme 2.4.3. — Pour tout  $(x, gB) \in \tilde{\mathfrak{g}}^{\mathrm{reg}}(\bar{k})$ , on a  $I_{x} \subset \operatorname{ad}(g)B$ .

Démonstration. — L'assertion est claire pour les éléments $x$ qui sont réguliers semi-simples. En effet, pour ceux-ci, le centralisateur $\mathrm{I}_{x}$ est un tore qui agit sur la fibre $\pi_{\mathfrak{g}}^{-1}(x)$. Puisque celle-ci est un ensemble discret, l'action du tore est nécessairement triviale.

Considérons le schéma en groupes H au-dessus de $\tilde{\mathfrak{g}}^{\mathrm{reg}}$ dont la fibre au-dessus de $(x,g\mathrm{B})\in \tilde{\mathfrak{g}}^{\mathrm{reg}}$ est le sous-groupe de $\mathrm{I}_x$ des éléments $h$ tels que $h\in g\mathrm{Bg}^{-1}$. Par construction, c'est un sous-schéma en groupes fermés de $(\pi_{\mathfrak{g}}^{\mathrm{reg}})^*\mathrm{I}$ qui coïncide avec $(\pi_{\mathfrak{g}}^{\mathrm{reg}})^*\mathrm{I}|_{\mathfrak{g}^{\mathrm{reg}}}$ au-dessus de l'ouvert dense des couples $(x,g\mathrm{B})$ avec $x$ réguliers semi-simples. Or $(\pi_{\mathfrak{g}}^{\mathrm{reg}})^*\mathrm{I}|_{\mathfrak{g}^{\mathrm{reg}}}$ est plat sur $\tilde{\mathfrak{g}}^{\mathrm{reg}}$, ce sous-schéma en groupes est nécessairement égal à $(\pi_{\mathfrak{g}}^{\mathrm{reg}})^*\mathrm{I}|_{\mathfrak{g}^{\mathrm{reg}}}$.

Considérons le schéma en groupes $\underline{\mathbf{B}}$ au-dessus de G/B dont la fibre au-dessus de gB est le sous-groupe ad(g)B de G. Notons $\underline{\mathbf{B}}|_{\tilde{\mathfrak{g}}^{\mathrm{reg}}}$ le changement de base de $\underline{\mathbf{B}}$ à $\tilde{\mathfrak{g}}^{\mathrm{reg}}$. Le lemme ci-dessus montre qu'au-dessus de $\tilde{\mathfrak{g}}^{\mathrm{reg}}$, on a un homomorphisme

$$
\mathrm{I} | _ {\tilde {\mathfrak {g}} ^ {\text { reg }}} \rightarrow \underline {{\mathrm{B}}} | _ {\tilde {\mathfrak {g}} ^ {\text { reg }}}.
$$

Par ailleurs, on dispose d'un homomorphisme de B dans le G/B-tore T × G/B. En composant, on obtient un homomorphisme G-équivariant

$$
\mathrm{I} | _ {\tilde {\mathfrak {g}} ^ {\mathrm{reg}}} \rightarrow \mathrm{T} \times \tilde {\mathfrak {g}} ^ {\mathrm{reg}}
$$

qui est un isomorphisme au-dessus du lieu régulier semi-simple. Au-dessus du lieu régulier semi-simple, l'action de W sur  $I|_{\tilde{g}^{reg}}$  se transporte sur l'action diagonale de  $T \times g^{rs}$ . Par adjonction, on obtient un homomorphisme

$$
\mathrm{I} | _ {\mathfrak {g} ^ {\mathrm{reg}}} \rightarrow (\pi_ {\mathfrak {g}}) _ {*} (\mathrm{T} \times \tilde {\mathfrak {g}} ^ {\mathrm{reg}})
$$

qui se factorise par le sous-foncteur des points fixes sous l'action diagonale de W sur  $(\pi_{\mathfrak{g}})_{*}(\mathrm{T}\times\tilde{\mathfrak{g}}^{\mathrm{reg}})$ .

Par descente, on obtient un homomorphisme  $J \rightarrow J^{1}$  qui est un isomorphisme au-dessus de  $c^{rs}$ .

Signalons une variante de la description de  $J^{1}$ .

Lemme 2.4.4. — Soit $\rho: X_{\rho} \to X$ un revêtement fini étale galoisien de groupe de Galois $\Theta_{\rho}$ qui trivialise le torseur $\rho_{G}$. Alors $J^{1}$ est canoniquement isomorphe au sous-schéma des points fixes dans la restriction des scalaires à la Weil

$$
\prod_ {(\mathrm{X} _ {\rho} \times \mathbf {t}) / \mathfrak {c}} (\mathbf {T} \times \mathrm{X} _ {\rho} \times \mathbf {t})
$$

pour l'action diagonale de $\mathbf{W} \rtimes \Theta_{\rho}$ sur $\mathbf{T} \times \mathrm{X}_{\rho} \times \mathbf{t}$.

Démonstration. — L'assertion à démontrer étant locale pour la topologie étale de X, on peut supposer que  $\rho_{G}$  et  $\rho$  sont triviaux. Dans ce cas, elle est immédiate. ☐

En suivant [23], nous allons définir un sous-faisceau $J'$ de $J^1$ que nous démontrerons qu'il coïncide avec l'image de $J \to J^1$. Cette définition nécessitera un peu de préparations. La construction qui suit est locale pour la topologie étale de la base X de sorte qu'on peut supposer G déployé. Pour toute racine $\alpha \in \Phi$, soit $h_\alpha$ l'hyperplan de t noyau de l'application linéaire $d\alpha : t \to G_a$. Soit $s_\alpha \in W$ la réflexion par rapport à l'hyperplan $h_\alpha$. Soit $T^{s_\alpha}$ le sous-groupe de T des éléments fixes par $s_\alpha$. On a alors l'inclusion

$$
\alpha \left(\mathrm{T} ^ {s _ {\alpha}}\right) \subset \{\pm 1 \}.
$$

Soient $x$ un point géométrique de $\mathfrak{t}$ tel que $s_{\alpha}(x) = x$ et $a$ son image dans $\mathfrak{c}$. Puisque $\mathbf{J}^1$ est la partie W-invariante du faisceau $\prod_{\mathfrak{t}/\mathfrak{c}}(\mathrm{T} \times \mathfrak{t})$, on a un homomorphisme canonique de $\mathrm{J}_a^1$ dans la fibre $\mathrm{T} \times \{x\}$ dont l'image est contenue dans $\mathrm{T}^{s_{\alpha}} \times \{x\}$. En composant avec la racine $\alpha : \mathrm{T} \to \mathbf{G}_m$, on obtient un homomorphisme $\alpha_x : \mathrm{J}_a^1 \to \mathbf{G}_m$ d'image contenue dans $\{\pm 1\}$.

Soit  $J^{0}$  le sous-schéma en groupes ouvert des composantes neutres de  $J^{1}$ . Par construction  $J_{a}^{0}$  est la composante neutre de  $J_{a}^{1}$  de sorte que  $J_{a}^{0}$  est contenu dans le noyau de  $\alpha_{x}$ .

Définition 2.4.5. — Soit J' le sous-foncteur de J$^{1}$ qui associe à tout c-schéma S, est le sous-ensemble J'(S) de J$^{1}$(S) des morphismes W-équivariants

$$
f: \mathrm{S} \times_ {\mathfrak {c}} \mathfrak {t} \rightarrow \mathrm{T}
$$

tel que pour tout point géométrique x de  $S \times_{c} t$  stable sous une involution  $s_{\alpha}(x) = x$  attachée à une certaine racine  $\alpha$ , on a  $\alpha(f(x)) \neq -1$ .

Lemme 2.4.6. — Le sous-foncteur J' de J$^{1}$ est représentable par un sous-schéma en groupes ouvert affine de J$^{1}$. De plus, on a des inclusions J$^{0}$ ⊂ J' ⊂ J$^{1}$.

Démonstration. — On va commencer par démontrer que le sous-foncteur  $J'$  est représentable par un sous-schéma ouvert affine de  $J^{1}$ . Comme le morphisme  $t \to c$  est fini et plat, il suffit de démontrer cette assertion après un changement de base à t. Il suffit donc de démontrer que  $J' \times_{c} t$  est le complément d'un diviseur de Cartier de  $J^{1} \times_{c} t$ .

Pour tout t-schéma S, les S-points de J' sont des morphismes W-équivariants f : S ×\_c t → T. Un tel morphisme induit pour tout t-schéma S un morphisme f\_Δ : S → T par restriction à la diagonale.

Il est loisible ici de se restreindre au cas déployé. L'image inverse du diviseur discriminant $\mathfrak{D}_{\mathrm{G}}$ de $\mathfrak{c}$ est une réunion des hyperplans de racine $h_{\alpha}$. La restriction de $\mathbf{J}^{1}$ à chaque hyperplan $h_{\alpha}$ admet alors un morphisme canonique sur le sous-groupe $\mathrm{T}^{\mathrm{s}\alpha}$ de T. En composant avec la racine $\alpha$, on obtient donc un morphisme $\mathbf{J}^{1} \times_{\mathfrak{c}} h_{\alpha} \to \{\pm 1\}$. L'image inverse de $-1$ est alors une partie ouverte et fermée de $\mathbf{J}^{1} \times_{\mathfrak{c}} h_{\alpha}$, éventuellement vide, et est donc un diviseur de Cartier de $\mathbf{J}^{1} \times_{\mathfrak{c}} t$. Par définition, $\mathbf{J}' \times_{\mathfrak{c}} t$ est le complément de la réunion de ces diviseurs.

Il résulte du même argument que  $J' \times_{c} t$  est un sous-schéma en groupes ouverts de  $J^{1}$ . Il s'ensuit que  $J'$  est un sous-schéma en groupes ouvert de  $J^{1}$ . Il contient donc le schéma en groupes des composantes neutres  $J^{0}$ .

L'énoncé suivant est une variante d'un théorème de Donagi et Gaitsgory [23, théorème 11.6]. On propose ici une démonstration un peu différente.

Proposition 2.4.7. — L'homomorphisme J → J$^{1}$ de 2.4.2 se factorise par le sous-schéma en groupes ouvert J' de 2.4.5 et induit un isomorphisme J → J'.

Démonstration. — Pour démontrer que  $J \to J^{1}$  se factorise par  $J'$ , il suffit de démontrer que pour tout  $a \in \mathfrak{c}(\bar{k})$ , l'homomorphisme  $\pi_{0}(J_{a}) \to \pi_{0}(J_{a}^{1})$  se factorise par  $\pi_{0}(J_{a}')$ . Il suffit de vérifier que fibre par fibre l'homomorphisme  $\pi_{0}(J_{a}) \to \pi_{0}(J_{a}^{1})$  se factorise par  $\pi_{0}(J')$ . Rappelons que l'homomorphisme  $Z_{G} \to J_{a}$  induit un homomorphisme surjectif  $\pi_{0}(Z_{G}) \to \pi_{0}(J_{a})$  d'après 2.3.2. Il suffit donc de vérifier que l'homomorphisme  $Z_{G} \to J_{a}^{1}$  se factorise par  $J_{a}'$ . Mais ceci est évident car la restriction de n'importe quelle racine à  $Z_{G}$  est triviale.

Puisque J et J' sont des schémas affines qui sont lisses au-dessus de c, pour démontrer que l'homomorphisme  $J \rightarrow J'$  est un isomorphisme, il suffit de le faire au-dessus d'un ouvert de c dont le complément est un fermé de codimension deux. L'image inverse de  $D_{G}$  dans t est la réunion des hyperplans  $h_{\alpha}$  de racine. Soit  $D_{G}^{sing}$  le fermé de  $D_{G}$  dont l'image inverse est le lieu des points appartenant à au moins deux hyperplans  $h_{\alpha}$ . Il est clair que  $D_{G}^{sing}$  est un fermé de codimension deux de c. Il suffit de démontrer que l'isomorphisme entre J et J' sur  $c - D_{G}$  se prolonge en un isomorphisme sur  $c - D_{G}^{sing}$ .

Soit $a \in (\mathfrak{c} - \mathfrak{D}_{\mathrm{G}}^{\mathrm{sing}})(\bar{k})$. Il suffit de démontrer que l'homomorphisme $J \to J'$ est un isomorphisme au-dessus d'un voisinage étale de $a$. Si $a \notin \mathfrak{D}_{\mathrm{G}}$, il n'y a rien à démontrer car on a vu que $J = J' = J^1$ sur l'ouvert $\mathfrak{c} - \mathfrak{D}_{\mathrm{G}}$. Si maintenant $a \in \mathfrak{D}_{\mathrm{G}} - \mathfrak{D}_{\mathrm{G}}^{\mathrm{sing}}$, on peut trouver $s \in \mathfrak{t}(\bar{k})$ d'image $a$ tel que $s$ annulé par une unique racine $\alpha$. Soient $T_{\alpha}$ le noyau de $\alpha : T \to G_m$ et $H_{\alpha}$ le centralisateur de $T_{\alpha}$. Soit $n$ un élément nilpotent régulier de l'algèbre de Lie $h_{\alpha}$ de $H_{\alpha}$ qui s'identifie à une sous-algèbre de Lie de $g$. L'élément $x = s + n$ est un élément régulier de $g$ d'image $a$ dans $\mathfrak{c}$. Il est aussi un élément régulier de $h_{\alpha}$ d'image $a_{H_{\alpha}}$ dans l'espace des polynômes caractéristiques $c_{H_{\alpha}}$ de $H_{\alpha}$. On vérifie que le morphisme $c_{H_{\alpha}} \to c$ envoie $a_{H_{\alpha}}$ en $a$ et est étale en ce point. On peut aussi vérifier que dans un voisinage de $a_{H_{\alpha}}$, les images réciproques de $J, J'$ et $J^1$ à $c_{H_{\alpha}}$ coïncident avec les mêmes groupes mais associés à $H_{\alpha}$. On peut ainsi ramener le problème au cas particulier d'un groupe dont le rang semi-simple vaut un.

Un groupe de rang semi-simple un est isomorphe à un produit de  $SL_{2}$ ,  $PGL_{2}$  ou  $GL_{2}$  avec un tore. Il suffit donc de se restreindre à ces trois groupes. Par un calcul direct, on vérifie que le centralisateur J a une fibre non-connexe dans le cas  $SL_{2}$  alors que dans les deux autres cas, ses fibres sont toutes connexes. Il en est de même pour  $J'$ .

Corollaire 2.4.8. — L'homomorphisme J → J$^{1}$ de cf. 2.4.7, induit un isomorphisme sur leurs sous-schémas ouverts des composantes neutres des fibres.

2.5. Le cas des groupes endoscopiques. — Considérons une donnée endoscopique  $(\kappa, \rho_{\kappa})$  de G et le groupe endoscopique associé H cf. 1.8.1. On a défini un morphisme fini plat  $\nu : c_{H} \to c$  entre les X-schémas des polynômes caractéristiques de H et de G cf. 1.9. Le centralisateur régulier J sur c et le centralisateur  $J_{H}$  régulier de H sur  $c_{H}$  sont reliés de la façon suivante.

## Proposition 2.5.1. — Il existe un homomorphisme canonique

$$
\mu : \nu^ {*} J \longrightarrow J _ {H}
$$

qui est un isomorphisme au-dessus de l'ouvert $\mathfrak{c}_{\mathrm{H}}^{\mathrm{G-rs}} = \nu^{-1}(\mathfrak{c}^{\mathrm{rs}})$.

Démonstration. — Reprenons les notations de 1.9. En particulier, on a un revêtement fini plat $\rho_{\kappa} \times \mathbf{t} \to \mathfrak{c}$ qui permet de réaliser $\mathfrak{c}$ comme le quotient invariant de $\rho_{\kappa} \times \mathbf{t}$ par $\mathbf{W} \rtimes \pi_0(\kappa)$. De même, $\mathfrak{c}_{\mathrm{H}}$ est le quotient invariant de $\rho_{\kappa} \times \mathbf{t}$ par $\mathbf{W}_{\mathbf{H}} \rtimes \pi_0(\kappa)$. Rappelons aussi que le morphisme $\nu : \mathfrak{c}_{\mathrm{H}} \to \mathfrak{c}$ a été construit dans 1.9 en produisant un homomorphisme

$$
\mathbf {W} _ {\mathbf {H}} \rtimes \pi_ {0} (\kappa) \rightarrow \mathbf {W} \rtimes \pi_ {0} (\kappa)
$$

compatible avec les actions de ces deux groupes sur $\rho_{\kappa} \times \mathbf{t}$.

D'après 2.4.4, on a les descriptions suivantes de  $J^{1}$  et  $J_{H}^{1}$

$$
J ^ {1} = \prod_ {\rho_ {\kappa} \times \mathbf {t} / \mathfrak {c}} (\rho_ {\kappa} \times \mathbf {t} \times \mathbf {T}) ^ {\mathbf {W} \rtimes \pi_ {0} (\kappa)}
$$

et son analogue pour H

$$
J _ {H} ^ {1} = \prod_ {\rho_ {\kappa} \times \mathbf {t} / \mathfrak {c} _ {H}} (\rho_ {\kappa} \times \mathbf {t} \times \mathbf {T}) ^ {\mathbf {W} _ {H} \rtimes \pi_ {0} (\kappa)}.
$$

Le morphisme évident

$$
\rho_ {\kappa} \times \mathbf {t} \rightarrow (\rho_ {\kappa} \times \mathbf {t}) \times_ {\mathfrak {c}} \mathfrak {c} _ {\mathrm{H}}
$$

qui est  $\mathbf{W}_{\mathbf{H}} \rtimes \pi_{0}(\kappa)$ -équivariant par 1.9.1, induit un homomorphisme  $\nu^{*}J^{1} \to J_{H}^{1}$ . On a vérifié que cet homomorphisme est un isomorphisme au-dessus de l'ouvert  $c_{H}^{G-rs}$  dans 1.9.2.

D'après 2.4.8, on a un homomorphisme $\mathrm{J} \to \mathrm{J}^{1}$ qui induit un isomorphisme entre leur sous-schéma ouvert des composantes neutres des fibres. Pour vérifier que l'homomorphisme $\nu^{*}\mathrm{J}^{1} \to \mathrm{J}_{\mathrm{H}}^{1}$ se restreint en un homomorphisme $\nu^{*}\mathrm{J} \to \mathrm{J}_{\mathrm{H}}$, il suffit de démontrer que pour tout $a_{\mathrm{H}} \in \mathfrak{c}_{\mathrm{H}}(\bar{k})$ d'image $a \in \mathfrak{c}(\bar{k})$, l'homomorphisme

$$
\pi_ {0} (\mathrm{J} _ {a} ^ {1}) \rightarrow \pi_ {0} (\mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}}} ^ {1})
$$

qui se déduit de  $J_{a}^{1} \to J_{H,a_{H}}^{1}$ , envoie le sous-groupe  $\pi_{0}(J_{a}) \subset \pi_{0}(J_{a}^{1})$  dans le sous-groupe  $\pi_{0}(J_{\mathrm{H},a_{\mathrm{H}}}) \subset \pi_{0}(J_{\mathrm{H},a_{\mathrm{H}}}^{1})$ . Puisque l'ensemble des racines de H est un sous-ensemble de l'ensemble des racines pour G, les conditions qui délimitent le sous-groupe  $\pi_{0}(J_{\mathrm{H},a_{\mathrm{H}}})$  dans le groupe  $\pi_{0}(J_{\mathrm{H},a_{\mathrm{H}}}^{1})$  sont satisfaites par les éléments de  $\pi_{0}(J_{a})$  cf. 2.4.5. La proposition suit. □

## 3. Fibres de Springer affines

Par analogie avec les fibres de Springer dans la résolution simultanée de Grothen-dieck-Springer, Kazhdan et Lusztig ont introduit les fibres de Springer affines et ont étudié leur propriété géométrique. Goresky, Kottwitz et MacPherson ont réalisé le lien entre les fibres de Springer affines et les intégrales orbitales stables via le comptage de points de certain quotient des fibres de Springer affines. Dans ce chapitre, nous allons passer en revue les propriétés géométriques des fibres de Springer affines suivant Kazhdan et Lusztig en donnant quelques compléments. Le comptage de points sera revu dans le chapitre 8.

Voici les notations qui seront utilisées dans ce chapitre. Soient $k$ un corps fini à $q$ éléments et $\bar{k}$ une clôture séparable de $k$. L'hypothèse que la caractéristique de $k$ soit plus grande que deux fois le nombre de Coxeter est toujours en vigueur. Soient $\mathrm{F}_v$ un corps local d'égales caractéristiques, $\mathcal{O}_v$ son anneau des entiers dont le corps résiduel $k_v$ est une

extension finie de $k$. On notera $\mathbf{X}_v = \operatorname{Spec}(\mathcal{O}_v)$ le disque formel associé et $\mathbf{X}_v^\bullet$ le disque formel épointé. Soient $v$ le point fermé de $\mathbf{X}_v$ et $\eta_v$ son point générique.

Soient $\bar{\mathcal{O}}_{v} = \mathcal{O}_{v}\hat{\otimes}_{k}\bar{k}$ et $\bar{\mathrm{X}}_v = \mathrm{Spec}(\bar{\mathcal{O}}_v)$. L'ensemble des composantes connexes de $\bar{\mathrm{X}}_v$ est en bijection avec l'ensemble des plongements de l'extension $k_v$ de $k$ dans $\bar{k}$

$$
\bar {\mathrm{X}} _ {v} = \bigsqcup_ {\bar {v}: k _ {v} \to \bar {k}} \bar {\mathrm{X}} _ {\bar {v}}.
$$

On choisit une uniformisante $\epsilon_v$.

En choisissant un point géométrique  $\bar{\eta}_{v}$  dans la fibre géométrique de  $\bar{X}_{\bar{v}}$ , on obtient la suite exacte habituelle

$$
1 \to \mathrm{I} _ {v} \to \Gamma_ {v} \to \operatorname{Gal} (\bar {k} / \bar {k} _ {v}) \to 1
$$

où $\Gamma_v = \pi_1(\eta_v, \bar{\eta}_v)$ est le groupe de Galois de $F_v$ et $I_v = \pi_1(\bar{X}_{\bar{v}}, \bar{\eta}_v)$ son sous-groupe d'inertie.

Soit G une forme quasi-déployée de G sur  $X_{v}$  associée à un Out(G)-torseur  $\rho_{G}$ . En choisissant un point géométrique de  $\rho_{G}$  au-dessus de  $\bar{\eta}_{v}$ , on obtient un homomorphisme  $\rho_{G}^{\bullet}:\Gamma_{v}\to\mathrm{Out}(\mathbf{G})$  qui se factorise à travers  $\mathrm{Gal}(\bar{k}/k_{v})$ . Au-dessus de  $\bar{X}_{v}$ ,  $\rho_{G}$  est le torseur trivial.

3.1. Rappels sur la grassmannienne affine. — Pour tout k-schéma affine S = Spec(R), notons  $X_{v} \hat{\times} S = \text{Spec}(\mathcal{O}_{v} \hat{\otimes}_{k} R)$  où  $O_{v} \hat{\otimes} R$  est la complétion v-adique de  $O_{v} \otimes R$ . Notons  $X_{v}^{\bullet} \hat{\times} S$  l'ouvert complémentaire de  $\{v\} \times S$  dans  $X_{v} \hat{\times} S$ .

La grassmannienne affine est le foncteur $\mathcal{G}_{v}$ qui associe à tout $k$-schéma affine noethérien le groupoïde des G-torseurs $\mathrm{E}_v$ sur $\mathrm{X}_v\hat{\times}\mathrm{S}$ munis d'une trivialisation sur $\mathrm{X}_v^{\bullet}\hat{\times}\mathrm{S}$ [33, Prop. 2]. Notons qu'un automorphisme de $\mathrm{E}_v$, trivial sur $\mathrm{X}_v^{\bullet}\hat{\times}\mathrm{S}$ est nécessairement trivial de sorte que ce groupoïde est une catégorie discrète. On pourra aussi bien le remplacer par l'ensemble des classes d'isomorphisme.

D'après [33, Prop. 2], $\mathcal{G}_{v}$ est représentable par un ind-schéma sur $k$: il existe un système inductif de $k$-schémas projectifs indexés par les entiers dont les flèches de transition sont des immersions fermées et dont la limite inductive représente le foncteur $\mathcal{G}_{v}$. Comme G est un schéma en groupes lisse de fibres connexes, l'ensemble des $k$-points de $\mathcal{G}_{v}$ s'exprime comme un quotient

$$
\mathcal {G} _ {v} (k) = \mathrm{G} (\mathrm{F} _ {v}) / \mathrm{G} (\mathcal {O} _ {v}).
$$

Quand  $G = GL_{r}$ , cet ensemble s'identifie naturellement à l'ensemble des  $O_{v}$ -réseaux dans le  $F_{v}$ -espace vectoriel  $F_{v}^{\oplus r}$ .

La même définition vaut quand on remplace $k$ par $\bar{k}$, $\mathbf{X}_{v}$ par $\bar{\mathbf{X}}_{\bar{v}}$ pour tout plongement $\bar{v}: k_{v} \to \bar{k}$. On a alors la grassmannienne affine $\mathcal{G}_{\bar{v}}$ définie sur $\bar{k}$. On a la formule

$$
\mathcal {G} \otimes_ {k} \bar {k} = \prod_ {\bar {v}: k _ {v} \to \bar {k}} \mathcal {G} _ {\bar {v}}.
$$

3.2. Fibres de Springer affines. — Nous gardons les notations de 1.3. En particulier, on a un schéma c au-dessus de  $X_{v}$  obtenu par torsion extérieure de l'espace des polynômes caractéristiques c de g comme dans le théorème de Chevalley 1.1.1.

Notons

$$
\mathfrak {c} ^ {\heartsuit} (\mathcal {O} _ {v}) = \mathfrak {c} (\mathcal {O} _ {v}) \cap \mathfrak {c} ^ {\mathrm{rs}} (\mathrm{F} _ {v})
$$

l'ensemble des $\mathcal{O}_{v}$-points de $\mathfrak{c}$ dont la fibre générique est régulière semi-simple. Rappelons qu'on a la section de Kostant $\epsilon : \mathfrak{c} \to \mathfrak{g}^{\mathrm{reg}}$ cf. 1.3.4. Pour tout $a \in \mathfrak{c}^{\heartsuit}(\mathcal{O}_{v})$, on a un point

$$
[ \epsilon ] (a) \in [ \mathfrak {g} ^ {\text { reg }} / G ]
$$

qui consiste en le G-torseur trivial  $E_{0}$  sur  $X_{v}$  et une section

$$
\gamma_ {0} \in \Gamma (\mathrm{X} _ {v}, \operatorname{ad} (\mathrm{E} _ {0}))
$$

ayant a comme polynôme caractéristique.

Pour chaque $a \in \mathfrak{c}^{\heartsuit}(\mathcal{O}_{v})$, on définit la fibre de Springer affine $\mathcal{M}_{v}(a)$ comme suit. Le foncteur $\mathcal{M}_{v}(a)$ associe à tout $k$-schéma affine noethérien S le groupoïde des couples (E, $\phi$) formés d'un G-torseur E sur $\mathrm{X}_{v}\hat{\times}\mathrm{S}$ et d'une section $\phi$ de ad(E), munis d'un isomorphisme avec $(\mathrm{E}_{0},\gamma_{0})$ sur $\mathrm{X}_{v}^{\bullet}\hat{\times}\mathrm{S}$. En particulier

$$
[ \chi ] (\mathrm{E}, \phi) = [ \chi ] (\mathrm{E} _ {0}, \gamma_ {0}) = a.
$$

Notons que par construction, le G-torseur  $E_{0}$  est le torseur trivial si bien que E détermine un point de la grassmannienne affine.

Proposition 3.2.1. — Le foncteur d'oubli (E, $\phi$) $\mapsto$ E définit un morphisme de la fibre de Springer affine $\mathcal{M}_{v}(a)$ dans la grassmannienne affine $\mathcal{G}_{v}$ qui est une immersion fermée. En particulier, $\mathcal{M}_{v}(a)$ est strictement représentable par un ind-schéma. De plus, le réduit $\mathcal{M}_{v}^{\mathrm{red}}(a)$ de $\mathcal{M}_{v}(a)$ est représentable par un schéma localement de type fini.

Démonstration. — La première assertion est immédiate. La seconde assertion a été démontrée par Kazhdan et Lusztig [36].

Considérons l'ensemble des $k$-points de $\mathcal{M}_v(a)$. Soit (E, $\phi$) un objet de $\mathcal{M}_v(a, k)$. Les fibres génériques de E et de $\mathrm{E}_0$ étant identifiées, la donnée de E consiste en une classe $g \in \mathrm{G}(\mathrm{F}_v) / \mathrm{G}(\mathcal{O}_v)$. Puisque $\phi$ est identifiée à $\gamma_0$ sur la fibre générique, pour que $\phi$ définisse une section sur $\mathrm{X}_v$ de $\mathrm{ad}(\mathrm{E}) \otimes \mathrm{D}$, il faut et il suffit que $\mathrm{ad}(g)^{-1} \gamma_0 \in \mathfrak{g}(\mathcal{O}_v)$. On a donc

$$
\mathcal {M} _ {v} (a, k) = \{g \in \mathrm{G} (\mathrm{F} _ {v}) / \mathrm{G} (\mathcal {O} _ {v}) \mid \mathrm{ad} (g) ^ {- 1} \gamma_ {0} \in \mathfrak {g} (\mathcal {O} _ {v}) \}.
$$

Nous allons maintenant considérer une variation triviale de la construction précédente en présence d'un faisceau inversible D' sur  $X_{v}$ . Cette variation sera nécessaire pour réaliser le passage entre les fibres de Springer affines et les fibres de Hitchin.

Soient  $D = D'^{\otimes 2}$  et  $h_{D}: X_{v} \to BG_{m}$  le morphisme dans le classifiant de  $G_{m}$  correspondant au fibré en droites D. Fixons un morphisme  $h_{a}: X_{v} \to [\mathfrak{c}/\mathbf{G}_{m}]$  qui s'insère dans le diagramme commutatif :

![](images/page_40_image_1.jpg)

Notons  $[\epsilon]^{D'}(a)$  le point de Kostant de a construit comme dans le lemme 2.2.5. On notera  $a^{\bullet}$  et  $h_{a}^{\bullet}$  les restrictions de a et de  $h_{a}$  à  $X_{v}^{\bullet}$  et on notera le point de Kostant associé  $[\epsilon]^{D'}(a^{\bullet})$ .

Définition 3.2.2. — On définit la fibre de Springer $\mathcal{M}_{v}(a)$ comme le foncteur qui associe à tout $k$-schéma affine noethérien S l'ensemble $\mathcal{M}_{v}(a, S)$ des classes d'isomorphisme des morphismes $h_{\mathrm{E},\phi}:\mathrm{X}_{v}\hat{\times}\mathrm{S}\to[\mathfrak{g}/\mathrm{G}\times\mathbf{G}_{m}]$ s'insérant dans le diagramme commutatif

$$
\begin{array}{c} \mathrm{X} _ {v} \hat {\times} \mathrm{S} \xrightarrow {h _ {\mathrm{E} , \phi}} [ \mathfrak {g} / \mathrm{G} \times \mathbf {G} _ {m} ] \\ \Biggl \downarrow_ {h _ {a}} \qquad \qquad \qquad \qquad \Biggl \downarrow_ {[ \chi ]} \\ [ \mathfrak {c} / \mathbf {G} _ {m} ] \end{array}
$$

munis d'un isomorphisme entre la restriction de  $h_{E,\phi}$  à  $X_{v}^{\bullet}\hat{\times}S$ , et le point de Kostant  $[\epsilon]^{D'}(a^{\bullet})$ .

La même définition vaut quand on remplace $k$ par $\bar{k}$, $\mathrm{X}_{v}$ par $\bar{\mathrm{X}}_{\bar{v}}$ pour tout plongement $\bar{v}: k_{v} \to \bar{k}$. Pour tout $a \in \mathfrak{c}(\bar{\mathcal{O}}_{\bar{v}}) \cap \mathfrak{c}^{\mathrm{rs}}(\bar{\mathrm{F}}_{\bar{v}})$, on a alors la fibre de Springer affine $\mathcal{M}_{\bar{v}}(a)$ définie sur $\bar{k}$. Pour tout $a \in \mathfrak{c}(\mathcal{O}_v) \cap \mathfrak{c}^{\mathrm{rs}}(\mathrm{F}_v)$, on a la formule

$$
\mathcal {M} _ {v} (a) \otimes_ {k} \bar {k} = \prod_ {\bar {v}: k _ {v} \to \bar {k}} \mathcal {M} _ {\bar {v}} (a).
$$

3.3. Symétries d'une fibre de Springer affine. — Le centralisateur régulier permet de définir le groupe des symétries d'une fibre de Springer affine. Soient  $a \in \mathfrak{c}^{\heartsuit}(\mathcal{O}_{v})$  et  $h_{a}: X_{v} \to c$  le morphisme correspondant. Soit  $J_{a} = h_{a}^{*}J$  l'image réciproque du centralisateur régulier.

Considérons le groupoïde de Picard $\mathcal{P}_{v}(\mathrm{J}_{a})$ fibré au-dessus de $\operatorname{Spec}(k)$ qui associe à tout $k$-schéma affine noethérien S le groupoïde de Picard $\mathcal{P}_{v}(\mathrm{J}_{a}, \mathrm{S})$ des $\mathrm{J}_{a}$-torseurs sur $\mathrm{X}_{v} \hat{\times} \mathrm{S}$ munis d'une trivialisation sur $\mathrm{X}_{v}^{\bullet} \hat{\times} \mathrm{S}$. On peut vérifier que pour tout $k$-schéma S, $\mathcal{P}_{v}(\mathrm{J}_{a}, \mathrm{S})$ est une catégorie de Picard discrète. De plus, le foncteur qui associe à S le

groupe des classes d'isomorphisme de $\mathcal{P}_{v}(\mathrm{J}_{a},\mathrm{S})$ est représentable par un ind-schéma en groupes sur $k$ qu'on notera $\mathcal{P}_{v}(\mathrm{J}_{a})$. Le groupe des $\bar{k}$-points $\mathcal{P}_{v}(\mathrm{J}_{a},k)$ s'identifie canoniquement au quotient $\mathrm{J}_{a}(\bar{\mathrm{F}}_{v}) / \mathrm{J}_{a}(\bar{\mathcal{O}}_{v})$. Si les fibres de $\mathrm{J}_{a}$ sont connexes, l'ensemble des $k$-points de $\mathcal{P}_{v}(\mathrm{J}_{a})$ s'identifie au quotient $\mathrm{J}_{a}(\mathrm{F}_{v}) / \mathrm{J}_{a}(\mathcal{O}_{v})$.

Le lemme 2.1.1 permet de définir une action de $\mathcal{P}_{v}$ sur $\mathcal{M}_{v}$. En effet, pour tout $(\mathrm{E},\phi)\in \mathcal{M}_{a}(\mathrm{S})$, on a un homomorphisme de faisceaux en groupes au-dessus de $\mathrm{X}_v\hat{\times}\mathrm{S}$

$$
\mathrm{J} _ {a} \longrightarrow \underline {{\mathrm{Aut}}} (\mathrm{E}, \phi)
$$

qui se déduit de 2.1.1. Ceci permet de tordre (E, $\phi$) par un $J_a$-torseur sur $\mathbf{X}_v \hat{\times} \mathbf{S}$ qui est trivialisé sur $\mathbf{X}_v^\bullet \hat{\times} \mathbf{S}$.

Sur les $k$-points, on peut décrire concrètement cette action. Pour simplifier l'exposition, supposons que $\mathrm{J}_a$ a des fibres connexes. L'action du groupe $\mathcal{P}_v(\mathrm{J}_a,k) = \mathrm{J}_a(\mathrm{F}_v) / \mathrm{J}_a(\mathcal{O}_v)$ sur l'ensemble

$$
\mathcal {M} _ {v} (a, k) = \{g \in \mathrm{G} (\mathrm{F} _ {v}) / \mathrm{G} (\mathcal {O} _ {v}) \mid \operatorname{ad} (g) ^ {- 1} \gamma_ {0} \in \mathfrak {g} (\mathcal {O} _ {v}) \}
$$

se décrit concrètement comme suit. D'après 2.1.1, il existe un isomorphisme canonique de $\mathrm{J}_a(\mathrm{F}_v)$ sur le centralisateur $\mathrm{G}_{\gamma_0}(\mathrm{F}_v)$ de $\gamma_0$ qu'on va noter $j\mapsto \theta (j)$. On fait $\operatorname {agir}\mathrm{J}_a(\mathrm{F}_v)$ sur l'ensemble des $g\in \mathrm{G}(\mathrm{F}_v)$ tels que $\operatorname {ad}(g)^{-1}(\gamma_0)\in \mathfrak{g}(\mathcal{O}_v)$ par $j.g = \theta (j)g$. Pour que ceci induise une action de $\mathrm{J}_a(\mathrm{F}_v) / \mathrm{J}_a(\mathcal{O}_v)$ sur $\mathcal{M}_v(a,k)$, il faut et il suffit que pour tout $g\in$$\mathcal{M}_v(a,k)$, on aie l'inclusion

$$
\theta \left(\mathrm{J} _ {a} \left(\mathcal {O} _ {v}\right)\right) \subset \operatorname{ad} (g) \mathrm{G} \left(\mathcal {O} _ {v}\right).
$$

Soit $\gamma = \mathrm{ad}(g)^{-1}\gamma_0\in \mathfrak{g}(\mathcal{O}_v)$. D'après 2.1.1, l'isomorphisme $\mathrm{ad}(g)^{-1}\circ \theta :\mathrm{I}_a\to \mathrm{G}_{\gamma_0}$ se prolonge en un homomorphisme de $\mathbf{X}_v$-schémas en groupes sur

$$
\mathrm{ad} (g) ^ {- 1} \circ \theta : \mathrm{J} _ {a} \longrightarrow \mathrm{I} _ {\gamma}
$$

ce qui implique en particulier que

$$
\theta \left(\mathrm{J} _ {a} \left(\mathcal {O} _ {v}\right)\right) \subset \operatorname{ad} (g) \left(\mathrm{I} _ {\gamma_ {0}} \left(\mathcal {O} _ {v}\right)\right) \subset \operatorname{ad} (g) \mathrm{G} \left(\mathcal {O} _ {v}\right).
$$

Nous considérons le sous-foncteur  $\mathcal{M}_{v}^{\mathrm{reg}}(a)$  de la fibre de Springer affine  $\mathcal{M}_{v}(a)$  dont les points sont les morphismes  $h_{\mathrm{E},\phi}:X_{v}\to[\mathfrak{g}/G\times\mathbf{G}_{m}]$  qui se factorisent par l'ouvert  $[\mathfrak{g}^{\mathrm{reg}}/\mathrm{G}\times\mathbf{G}_{m}]$ . Il est clair que  $\mathcal{M}_{v}^{\mathrm{reg}}(a)$  est un ouvert de  $\mathcal{M}_{v}(a)$ .

Lemme 3.3.1. — L'ouvert $\mathcal{M}_{v}^{\mathrm{reg}}(a)$ est un espace principal homogène sous l'action de $\mathcal{P}_{v}(\mathrm{J}_{a})$.

Démonstration. — C'est une conséquence du lemme 2.2.1.

Soit $\bar{v}: k_v \to \bar{k}$. Pour tout $a \in \mathfrak{c}(\bar{\mathcal{O}}_{\bar{v}}) \cap \mathfrak{c}^{\mathrm{rs}}(\bar{\mathrm{F}}_{\bar{v}})$, on a le groupe des symétries $\mathcal{P}_{\bar{v}}(\mathrm{J}_a)$ défini sur $\bar{k}$ de la fibre affine $\mathcal{M}_{\bar{v}}(a)$. Si $a \in \mathfrak{c}(\mathcal{O}_v) \cap \mathfrak{c}^{\mathrm{rs}}(\mathrm{F}_v)$, on a la formule

$$
\mathcal {P} _ {v} (\mathrm{J} _ {a}) \otimes_ {k} \bar {k} = \prod_ {\bar {v}: k _ {v} \to \bar {k}} \mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a}).
$$

Dans la suite du chapitre, on va passer à  $\bar{k}$  et discuter des propriétés géométriques de  $\mathcal{P}_{\bar{v}}(\mathrm{J}_{a})$ . Rappelons qu'au-dessus de  $\bar{X}_{\bar{v}}$ , G est un groupe déployé.

3.4. Quotient projectif d'une fibre de Springer affine. — Soit  $a \in \mathfrak{c}(\bar{\mathcal{O}}_{\bar{v}})$  dont la fibre générique est dans  $\mathfrak{c}^{\mathrm{rs}}(\bar{\mathrm{F}}_{\bar{v}})$ . D'après Kazhdan et Lusztig, le foncteur  $\mathcal{M}_{\bar{v}}(a)$  a un schéma réduit sous-jacent  $\mathcal{M}_{\bar{v}}^{\mathrm{red}}(a)$  qui est localement de type fini cf. 3.2.1 et [36]. Ils ont aussi démontré que  $\mathcal{M}_{\bar{v}}^{\mathrm{red}}(a)$ , quotienté par un groupe discret convenable, est un schéma projectif. Rappelons leur énoncé de façon plus précise.

Soit $\Lambda$ le quotient libre maximal de $\pi_0(\mathcal{P}_{\bar{v}}(\mathrm{J}_a))$. Choissons un relèvement arbitraire $\Lambda \to \mathcal{P}_{\bar{v}}(\mathrm{J}_a)$ qui induit une action de $\Lambda$ sur $\mathcal{M}_{\bar{v}}(a)$ et $\mathcal{M}_{\bar{v}}^{\mathrm{red}}(a)$.

Proposition 3.4.1. — Le groupe discret $\Lambda$ agit librement sur $\mathcal{M}_{\bar{v}}^{\mathrm{red}}(a)$ et le quotient $\mathcal{M}_{\bar{v}}^{\mathrm{red}}(a)/\Lambda$ est un $\bar{k}$-schéma projectif.

Démonstration. — La proposition 1 de [36, page 138] montre que $\Lambda$ agit librement sur $\mathcal{M}_{\bar{v}}^{\mathrm{red}}(a)$ et qu'en tronquant la fibre de Springer affine réduite $\mathcal{M}_{\bar{v}}^{\mathrm{red}}(a)$, on obtient des schémas projectifs qui se surjectent sur le quotient $\mathcal{M}_{\bar{v}}^{\mathrm{red}}(a)/\Lambda$. Il s'ensuit que le quotient est également un schéma projectif.

3.5. Approximation. — D'après un théorème bien connu de Harish-Chandra, les intégrales orbitales semi-simples régulières sont localement constantes. Dans ce paragraphe, nous allons montrer une variante géométrique, légèrement plus forte, de ce théorème.

Proposition 3.5.1. — Soient $a \in \mathfrak{c}(\mathcal{O}_{v}) \cap \mathfrak{c}^{\mathrm{rs}}(\mathrm{F}_{v})$, $\mathcal{M}_{a}$ la fibre de Springer affine et $\mathcal{P}_{v}(\mathrm{J}_{a})$ le groupe des symétries de $\mathcal{M}_{v}(a)$. Il existe un entier naturel N tel que pour toute extension finie $k'$ de $k$, pour tout $d' \in \mathfrak{c}(\mathcal{O}_{v} \otimes_{k} k')$ tel que

$$
a \equiv a ^ {\prime} \mod \epsilon_ {v} ^ {\mathrm{N}},
$$

la fibre de Springer affine $\mathcal{M}_{v}(a')$ munie de l'action de $\mathcal{P}_{v}(\mathrm{J}_{a'})$ est isomorphe à $\mathcal{M}_{v}(a) \otimes_{k} k'$ munie de l'action de $\mathcal{P}_{v}(\mathrm{J}_{a}) \otimes_{k} k'$.

Démonstration. — Considérons le revêtement caméral $\tilde{\mathbf{X}}_{a,v}$ de $\mathbf{X}_v$ associé à $a$ construit en formant le diagramme cartésien :

$$
\begin{array}{c c c} \tilde {\mathrm{X}} _ {a, v} & \longrightarrow & \mathfrak {t} \\ \pi_ {a} \Big \downarrow & & \Big \downarrow \\ \mathrm{X} _ {v} & \xrightarrow [ a ] & \mathfrak {c} \end{array}
$$

Le morphisme $\pi_{a}$ est fini plat et génériquement étale. Le revêtement $\tilde{\mathbf{X}}_{a,v}$ est muni d'une action de W qui se déduit de l'action de W sur t. On associe aussi à $a' \in \mathfrak{c}(\mathcal{O}_v \otimes_k k')$ son revêtement caméral $\tilde{\mathbf{X}}_{a',v} \to \mathbf{X}_v \otimes_k k'$.

Lemme 3.5.2. — Soit $a \in \mathfrak{c}(\mathcal{O}_{v}) \cap \mathfrak{c}^{\mathrm{rs}}(\mathrm{F}_{v})$. Pour tout entier positif $\mathrm{N}_{1}$, il existe un entier $\mathrm{N} > \mathrm{N}_{1}$ tel que pour toute extension finie $k'$ de $k$, pour tout $a' \in \mathfrak{c}(\mathcal{O}_{v} \otimes_{k} k')$ tel que

$$
a \equiv a ^ {\prime} \mod \epsilon_ {v} ^ {\mathrm{N}},
$$

le revêtement $\tilde{\mathbf{X}}_{a',v}$ de $\mathbf{X}_v\otimes_k k'$ muni de l'action de W est isomorphe au revêtement $\tilde{\mathbf{X}}_{a,v}\otimes_k k'$ muni de l'action de W. On peut demander en plus que l'isomorphisme relève l'isomorphisme évident modulo $\epsilon_v^{\mathrm{N}_1}$.

Démonstration. — C'est un cas particulier d'un lemme d'Artin-Hironaka [3, lemme 3.12]. La seconde assertion est implicite dans la démonstration d'Artin.

Supposons que les revêtements caméraux $\tilde{\mathbf{X}}_{a,v}$ et $\tilde{\mathbf{X}}_{a',v}$ de $\mathbf{X}_v\otimes_kk'$ sont isomorphes, démontrons que $\mathcal{M}_v(a)\otimes_kk'$ munie de l'action de $\mathcal{P}_v(\mathrm{J}_a)\otimes_kk'$ et $\mathcal{M}_v(a')$ munie de l'action de $\mathcal{P}_v(\mathrm{J}_{a'})$ sont isomorphes. En remplaçant $k$ par $k'$, on peut désormais supposer $k = k'$.

Pour cela, il nous faut une description de la fibre de Springer affine en termes du centralisateur régulier. Soit $\gamma_0 = \epsilon(a): \mathrm{X}_v \to \mathfrak{g}$ la section de Kostant de $a$. On a alors un isomorphisme canonique entre $\mathrm{J}_a$ et le $\mathrm{X}_v$-schéma en groupes $\mathrm{I}_{\gamma_0} = \gamma_0^* \mathrm{I}$ où $\mathrm{I}$ est le schéma en groupes des centralisateurs au-dessus de $\mathfrak{g}$. L'homomorphisme évident $\mathrm{I}_{\gamma_0} \to \mathrm{G}$ induit un homomorphisme injectif de fibrés vectoriels sur $\mathrm{X}_v$

$$
\operatorname{Lie} \left(\mathrm{I} _ {\gamma_ {0}}\right)\rightarrow \mathfrak {g}.
$$

L'énoncé suivant montre que la fibre de Springer affine $\mathcal{M}_{v}(a)$ ne dépend pas de $\gamma_{0}$ mais seulement de la sous-algèbre de Lie commutative $\operatorname{Lie}(\mathrm{I}_{\gamma_{0}})$ de $\mathfrak{g}$.

Lemme 3.5.3. — Soit $g \in \mathrm{G}(\mathrm{F}_v)$. Alors on a $\operatorname{ad}(g)^{-1}(\gamma_0) \in \mathfrak{g}(\mathcal{O}_v)$ si et seulement si $\operatorname{ad}(g)^{-1}\operatorname{Lie}(\mathrm{I}_{\gamma_0}) \subset \mathfrak{g}(\mathcal{O}_v)$.

Démonstration. — Comme $\gamma_0 \in \mathrm{Lie}(\mathrm{I}_{\gamma_0})$, $\mathrm{ad}(g)^{-1}\mathrm{Lie}(\mathrm{I}_{\gamma_0}) \subset \mathfrak{g}(\mathcal{O}_v)$ implique immédiatement $\mathrm{ad}(g)^{-1}(\gamma_0) \in \mathfrak{g}(\mathcal{O}_v)$. Inversement, soit $g \in \mathrm{G}(\mathrm{F}_v)$ tel que $\gamma = \mathrm{ad}(g)^{-1}(\gamma_0) \in \mathfrak{g}(\mathcal{O}_v)$. Soit $\mathrm{I}_{\gamma} = \gamma^*\mathrm{I}$. Le fait cf. 2.1.1 que l'isomorphisme en fibre générique

$$
\mathrm{ad} (g) ^ {- 1}: \mathrm{J} _ {a, \mathrm{F} _ {v}} = \mathrm{I} _ {\gamma_ {0}, \mathrm{F} _ {v}} \to \mathrm{I} _ {\gamma , \mathrm{F} _ {v}}
$$

se prolonge en un homomorphisme  $J_{a} \to I_{\gamma}$  implique en particulier que  $\operatorname{ad}(g)^{-1}\operatorname{Lie}(I_{\gamma_{0}}) \subset \mathfrak{g}(\mathcal{O}_{v})$ . □

Pour terminer la démonstration de la proposition 3.5.1, il suffit de démontrer le lemme suivant.

Lemme 3.5.4. — Soient $a, a' \in \mathfrak{c}(\mathcal{O}_v) \cap \mathfrak{c}_{\mathrm{rs}}(\mathrm{F}_v)$ tels que $a \equiv a'\mod \epsilon_v$. Supposons qu'il existe un isomorphisme entre les revêtements caméraux $\tilde{\mathrm{X}}_{a,v}$ et $\tilde{\mathrm{X}}_{a',v}$ munis de l'action de W qui relève l'isomorphisme évident dans la fibre spéciale. Soient $\gamma_0 = \epsilon(a)$ la section de Kostant de $a$ et $\gamma_0' = \epsilon(a')$ la section de Kostant de $a'$. Soient $\mathrm{I}_{\gamma_0}$ et $\mathrm{I}_{\gamma_0'}$ les sous-schémas en groupes de G centralisateurs des sections $\gamma_0$ et $\gamma_0'$. Alors il existe $g \in \mathrm{G}(\mathcal{O}_v)$ tel que

$$
\mathrm{ad} (g) ^ {- 1} \mathrm{I} _ {\gamma_ {0}} = \mathrm{I} _ {\gamma_ {0} ^ {\prime}}.
$$

Démonstration. — Ce lemme est une conséquence d'un résultat de Donagi et Gaitsgory [23, théorème 11.8]. Pour la commodité du lecteur, nous allons en extraire la portion utile à notre propos. Puisque les schémas en groupes $\mathrm{I}_{\gamma_0}$ et $\mathrm{I}_{\gamma_0'}$ sont complètement déterminés par les revêtements caméraux $\tilde{\mathbf{X}}_{a,v}$ respectivement $\tilde{\mathbf{X}}_{a',v}$ cf. 2.4.7, l'isomorphisme entre $\tilde{\mathbf{X}}_{a,v}$ et $\tilde{\mathbf{X}}_{a',v}$ induit un isomorphisme $\iota : \mathrm{I}_{\gamma_0} \to \mathrm{I}_{\gamma_0'}$. Cet isomorphisme transporte $\gamma_0 \in \operatorname{Lie}(\mathrm{I}_{\gamma_0})$ en un élément $\iota(\gamma_0) \in \operatorname{Lie}(\mathrm{I}_{\gamma_0'})$. Puisque les fibres spéciales de $\iota(\gamma_0)$ et $\gamma_0'$ coïncident, $\iota(\gamma_0) : \mathrm{X}_v \to \mathfrak{g}$ se factorise par l'ouvert $\mathfrak{g}^{\text{reg}}$. On en déduit l'égalité $\mathrm{I}_{\iota(\gamma_0)} = \mathrm{I}_{\gamma_0'}$ de sous-schémas en groupes de G.

On dispose de deux sections

$$
\gamma_ {0}, \iota (\gamma_ {0}): \mathrm{X} _ {v} \to \mathfrak {g} ^ {\text { reg }}
$$

qui ont le même polynôme caractéristique a et qui sont égales modulo  $\epsilon_{v}$ . Puisque le morphisme

$$
\mathbf {G} \times_ {\mathrm{X}} \mathfrak {g} ^ {\mathrm{reg}} \rightarrow \mathfrak {g} ^ {\mathrm{reg}} \times_ {\mathfrak {c}} \mathfrak {g} ^ {\mathrm{reg}}
$$

est un morphisme lisse, il existe  $g \in \mathrm{G}(\mathcal{O}_{v})$  tel que  $g \equiv 1 \mod \epsilon_{v}$  et tel que  $\operatorname{ad}(g^{-1}(\gamma_{0})) = \iota(\gamma_{0})$ . On en déduit que

$$
\mathrm{ad} (g) ^ {- 1} (\mathrm{I} _ {\gamma_ {0}}) = \mathrm{I} _ {\iota (\gamma_ {0})} = \mathrm{I} _ {\gamma_ {0} ^ {\prime}}.
$$

C'est ce qu'on voulait.

3.6. Cas linéaire. — Examinons maintenant les fibres de Springer affines du groupe linéaire en suivant la présentation de Laumon [51]. Nous référons à [59] pour une discussion similaire dans le cas des groupes classiques. Soit  $\mathrm{G} = \mathrm{GL}(r)$  avec r < p.

On garde les notations fixées au début de ce chapitre. Un point $a \in \mathfrak{c}(\bar{\mathcal{O}}_{\bar{v}})$ est représenté par un polynôme unitaire de degré $r$ de variable $t$

$$
\mathrm{P} (a, t) = t ^ {r} - a _ {1} t ^ {r - 1} + \dots + (- 1) ^ {r} a _ {r} \in \bar {\mathcal {O}} _ {\bar {v}} [ t ].
$$

Formons la  $\bar{O}_{\bar{v}}$ -algèbre finie et plate de rang r

$$
\mathrm{B} = \bar {\mathcal {O}} _ {\bar {v}} [ t ] / \mathrm{P} (a, t)
$$

et notons  $E = B \otimes_{\bar{\mathcal{O}}_{\bar{v}}} \bar{F}_{\bar{v}}$ . L'hypothèse  $a \in \mathfrak{c}^{\circ}(\bar{\mathcal{O}}_{\bar{v}})$  implique que E est une  $\bar{F}_{\bar{v}}$ -algèbre finie étale de dimension r. On peut écrire E comme un produit  $E_{1} \times \cdots \times E_{s}$  de s extensions séparables de  $\bar{F}_{\bar{v}}$  avec  $s \leq r$ .

3.6.1. — Dans cette situation, on a une description de la fibre de Springer en termes des réseaux. Les  $\bar{k}$ -points de la fibre de Springer  $\mathcal{M}_{\bar{v}}(a)$  sont des B-réseaux dans E c'est-à-dire des sous-B-modules du  $\bar{F}_{\bar{v}}$ -espace vectoriel E qui sont en même temps des  $\bar{O}_{\bar{v}}$ -réseaux. Les  $\bar{k}$ -points de la partie régulière  $\mathcal{M}_{\bar{v}}^{\mathrm{reg}}(a)$  consistent en des B-réseaux de E qui sont des B-modules libres. Le groupe des  $\bar{k}$ -points de  $\mathcal{P}_{\bar{v}}(\mathrm{J}_{a})$  est le groupe  $E^{\times}/B^{\times}$ .

3.6.2. — La normalisation  $B^{b}$  de B est l'anneau des entiers de  $E_{\bar{v}}$ . On a alors un dévissage de  $E^{\times}/B^{\times}$

$$
1 \rightarrow (\mathrm{B} ^ {\flat}) ^ {\times} / \mathrm{B} ^ {\times} \rightarrow \mathrm{E} ^ {\times} / \mathrm{B} ^ {\times} \rightarrow \mathrm{E} ^ {\times} / (\mathrm{B} ^ {\flat}) ^ {\times} \rightarrow 1
$$

où  $(\mathrm{B}^{\flat})^{\times}/\mathrm{B}^{\times}$  est le groupe des  $\bar{k}$ -points de la composante neutre du groupe  $\mathcal{P}_{\bar{v}}(\mathrm{J}_{a})$ . Par conséquent, le groupe des composantes connexes  $\pi_{0}(\mathcal{P}_{\bar{v}}(\mathrm{J}_{a}))$  est canoniquement isomorphe à  $\mathrm{E}^{\times}/(\mathrm{B}^{\flat})^{\times}$  qui est un groupe abélien libre muni d'une base indexée par l'ensemble des composantes connexes de  $\operatorname{Spec}(\mathrm{B}^{\flat})$ .

3.6.3. — Dans ce cas, la dimension de  $\mathcal{P}_{\bar{v}}(\mathrm{J}_{a})$  est égale à l'invariant  $\delta$  de Serre

$$
\delta_ {\bar {v}} (a) = \dim (\mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a})) = \dim_ {k} (\mathrm{B} ^ {\flat} / \mathrm{B}).
$$

Par ailleurs, cet entier peut être exprimé en fonction du discriminant. Soit $d_{\bar{v}}(a) = \text{val}_{\bar{v}}(\mathfrak{D}(a))$ la valuation $\bar{v}$-adique du discriminant de $a$. En utilisant [70, III.3 proposition 5 et III.6 corollaire 1] et l'hypothèse $r < p$, on obtient la formule

$$
\delta_ {\bar {v}} (a) = (d _ {\bar {v}} (a) - c _ {\bar {v}} (a)) / 2
$$

$\mathrm{ou} c_{\bar{v}}(a) = r - s.$

## 3.7. Dimension. — Dans [36], Kazhdan et Lusztig ont montré que

$$
\dim (\mathcal {M} _ {\bar {v}} (a)) = \dim (\mathcal {M} _ {\bar {v}} ^ {\mathrm{reg}} (a)).
$$

On peut en fait déduire un énoncé plus précis à partir de leurs résultats.

Proposition 3.7.1. — Le complémentaire de l'ouvert régulier $\mathcal{M}_{\bar{v}}^{\mathrm{reg}}(a)$ de la fibre de Springer $\mathcal{M}_{\bar{v}}(a)$ est de dimension strictement plus petite que celle de $\mathcal{M}_{\bar{v}}(a)$.

Démonstration. — Pour discuter de la dimension, on peut négliger les nilpotents dans les anneaux structuraux de  $\mathcal{M}_{\bar{v}}(a)$ . Comme rappelé dans le paragraphe 3.2,  $\mathcal{M}_{\bar{v}}(a)$  est la sous-variété de la grassmannienne affine des  $g \in \mathrm{G}(\mathrm{F}_{\bar{v}})/\mathrm{G}(\mathcal{O}_{\bar{v}})$  tels que  $\operatorname{ad}(g)^{-1}(\gamma_{0}) \in \mathfrak{g}(\mathcal{O}_{\bar{v}})$ .

A la suite de Kazhdan et Lusztig, considérons aussi la sous-variété des points fixes $\mathcal{B}_{\bar{v}}(a)$ des drapeaux affines fixes sous $\gamma_0$ c'est-à-dire $g \in \mathrm{G}(\mathrm{F}_{\bar{v}})/\mathrm{Iw}_{\bar{v}}$ tel que $\mathrm{ad}(g)^{-1}\gamma_0 \in$

Lie(Iw$_{\bar{v}}$). Ici Iw$_{\bar{v}}$ est un sous-groupe d'Iwahori de G($\mathcal{O}_{\bar{v}}$). Dans [36], Kazhdan et Lusz-tig ont démontré que les fibres de Springer affines pour les sous-groupes d'Iwahori sont équidimensionnelles. L'équidimensionalité des fibres de Springer classiques a été démon-trée auparavant par Spaltenstein [72].

Le morphisme $\mathcal{B}_{\bar{v}}(a) \to \mathcal{M}_{\bar{v}}(a)$ est un morphisme fini au-dessus de $\mathcal{M}_{\bar{v}}^{\mathrm{reg}}(a)$. Les fibres au-dessus des points $x \in \mathcal{M}_{\bar{v}} - \mathcal{M}_{\bar{v}}^{\mathrm{reg}}$ sont non vides et de dimension supérieure ou égale à un. L'équidimensionalité de $\mathcal{B}_{\bar{v}}(a)$ implique donc que les composantes irréductibles de $\mathcal{M}_a - \mathcal{M}_a^{\mathrm{reg}}$ sont de dimension strictement plus petite que $\dim(\mathcal{M}_a^{\mathrm{reg}})$.

Corollaire 3.7.2. — Si $\dim(\mathcal{M}_{v}(a)) = 0$, alors l'ouvert dense $\mathcal{M}_{v}^{\text{reg}}(a)$ est $\mathcal{M}_{v}(a)$ tout entier.

Kazhdan et Lusztig ont aussi conjecturé une formule qui exprime la dimension ci-dessus en fonction du discriminant et d'un terme défectif relié à la monodromie. Cette formule a été démontrée plus tard par Bezrukavnikov dans [8]. Rappelons-la.

Gardons les notations fixées au début de ce chapitre. Soit $a: \bar{X}_{\bar{v}} \to \mathfrak{c}$ un morphisme dont l'image n'est pas contenue dans le diviseur du discriminant $\mathfrak{D}_{\mathrm{G}}$. En prenant l'image réciproque de $\mathfrak{D}_{\mathrm{G}}$, on obtient un diviseur de Cartier effectif de $\bar{X}_{\bar{v}}$ supporté par son point fermé. Son degré est un entier naturel que nous allons noter

$$
d _ {\bar {v}} (a) := \deg_ {\bar {v}} (a ^ {*} \mathfrak {D} _ {\mathrm{G}}).
$$

En prenant l'image réciproque du revêtement $\pi : \mathfrak{t}^{\mathrm{rs}} \to \mathfrak{c}^{\mathrm{rs}}$ par le morphisme $a: \bar{\mathbf{X}}_{\bar{v}}^{\bullet} \to \mathfrak{c}^{\mathrm{rs}}$, on obtient un W-torseur $\pi_a$ sur $\bar{\mathbf{X}}_{\bar{v}}^{\bullet}$. Rappelons qu'au-dessus de $\bar{\mathbf{X}}_{\bar{v}}$ la forme quasi-déployée se déploie canoniquement de sorte qu'après le changement de base à $\bar{\mathbf{X}}_{\bar{v}}$, on a $\mathbf{W} = \mathbf{W}$. En choisissant un point géométrique de ce torseur au-dessus du point géométrique $\bar{\eta}_{\bar{v}}$ de $\bar{\mathbf{X}}_{\bar{v}}$, on obtient un homomorphisme

$$
\pi_ {a} ^ {\bullet}: \mathrm{I} _ {v} \to \mathbf {W}.\tag{3.7.3}
$$

Puisque $p$ ne divise pas l'ordre de $\mathbf{W}$, $\pi_{a}^{\bullet}$ se factorise par le quotient modéré $\mathrm{I}_{v}^{\mathrm{tame}}$ de $\mathrm{I}_{v}$ de sorte que son image est un sous-groupe cyclique. Notons

$$
c _ {\bar {v}} (a) := \dim (\mathbf {t}) - \dim (\mathbf {t} ^ {\pi_ {a} ^ {\bullet} (\mathrm{I} _ {v})}).\tag{3.7.4}
$$

L'énoncé suivant a été démontré dans [8] par Bezrukavnikov.

Proposition 3.7.5. — On a les égalités

$$
\dim (\mathcal {M} _ {\bar {v}} ^ {\mathrm{reg}} (a)) = \dim (\mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a})) = \frac {d _ {\bar {v}} (a) - c _ {\bar {v}} (a)}{2}.
$$

Nous allons noter $\delta_{\bar{v}}(a) = \dim (\mathcal{P}_{\bar{v}}(\mathrm{J}_a))$ et l'appeler l'invariant $\delta$ local.

3.8. Modèle de Néron. — La dimension de  $\mathcal{P}_{\bar{v}}(J_{a})$  peut être calculée autrement à l'aide du modèle de Néron de  $J_{a}$ . En fait, le modèle de Néron nous permet d'analyser complètement la structure de  $\mathcal{P}_{\bar{v}}(J_{a})$ . D'après Bosch, Lutkebohmer et Raynaud [10, ch. 10], voir aussi [13, section 3], il existe un unique schéma en groupes lisse de type fini  $J_{a}^{b}$  sur  $\bar{X}_{\bar{v}}$  de même fibre générique que  $J_{a}$  et maximal pour cette propriété c'est-à-dire pour tout autre schéma en groupes lisse de type fini  $J'$  sur  $\bar{X}_{\bar{v}}$  de même fibre générique, il existe un homomorphisme canonique  $J' \to J_{a}^{b}$  qui induit l'identité sur les fibres génériques. En particulier, on a un homomorphisme canonique  $J_{a} \to J_{a}^{b}$ . Au niveau des points entiers, cet homomorphisme définit les inclusions

$$
\mathrm{J} _ {a} (\bar {\mathcal {O}} _ {\bar {v}}) \subset \mathrm{J} _ {a} ^ {\flat} (\bar {\mathcal {O}} _ {\bar {v}}) \subset \mathrm{J} _ {a} (\bar {\mathrm{F}} _ {\bar {v}})
$$

où  $\mathrm{J}_{a}^{\mathrm{b}}(\bar{\mathcal{O}}_{\bar{v}})$  est le sous-groupe borné maximal de  $\mathrm{J}_{a}(\mathrm{F}_{\bar{v}})$ . On appellera  $J_{a}^{b}$  le modèle de Néron de  $J_{a}$ . Remarquons que dans la terminologie de [13],  $J_{a}^{b}$  sera appelé le modèle de Néron de type fini à distinguer avec le modèle de Néron localement de type fini de [10]. En fait, le modèle de Néron de type fini est un ouvert de Zariski du modèle de Néron localement de type fini qui est construit dans [10, ch. 10].

En remplaçant dans la définition 3.3 de $\mathcal{P}_{\bar{v}}(\mathrm{J}_a)$ le schéma en groupes $\mathrm{J}_a$ par son modèle de Néron $\mathrm{J}_a^{\flat}$, on obtient un ind-schéma en groupes $\mathcal{P}_{\bar{v}}(\mathrm{J}_a^{\flat})$ sur $\bar{k}$. L'homomorphisme de schémas en groupes $\mathrm{J}_a \to \mathrm{J}_a^{\flat}$ induit un homomorphisme de ind-groupes

$$
\mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a}) \to \mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a} ^ {\flat})
$$

qui induit un dévissage de $\mathcal{P}_{\bar{v}}(J_a)$.

Lemme 3.8.1. — Le groupe $\mathcal{P}_{\bar{v}}(\mathrm{J}_{a}^{\flat})$ est homéomorphe à un groupe abélien libre de type fini. L'homomorphisme $p_{\bar{v}}: \mathcal{P}_{\bar{v}}(\mathrm{J}_{a}) \to \mathcal{P}_{\bar{v}}(\mathrm{J}_{a}^{\flat})$ est surjectif. Le noyau $\mathcal{R}_{\bar{v}}(a)$ de $p_{\bar{v}}$ est un schéma en groupes affine de type fini sur $\bar{k}$.

Démonstration. — Puisque  $\mathrm{J}_{a}^{\flat}(\bar{\mathcal{O}}_{\bar{v}})$  est le sous-groupe borné maximal dans le tore  $\mathrm{J}_{a}(\bar{\mathrm{F}}_{\bar{v}})$ , le quotient  $\mathrm{J}_{a}(\bar{\mathrm{F}}_{\bar{v}})/\mathrm{J}_{a}^{\flat}(\bar{\mathcal{O}}_{\bar{v}})$  est un groupe abélien libre de type fini. L'homomorphisme

$$
\mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a}) (\bar {k}) = \mathrm{J} _ {a} (\bar {\mathrm{F}} _ {\bar {v}}) / \mathrm{J} _ {a} (\bar {\mathcal {O}} _ {\bar {v}}) \rightarrow \mathrm{J} _ {a} (\bar {\mathrm{F}} _ {\bar {v}}) / \mathrm{J} _ {a} ^ {\flat} (\bar {\mathcal {O}} _ {\bar {v}}) = \mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a} ^ {\flat}) (\bar {k})
$$

est manifestement surjectif.

Pour un entier N assez grand,  $\mathrm{J}_{a}(\mathcal{O}_{\bar{v}})$  contient le noyau de l'homomorphisme  $\mathrm{J}_{a}^{\flat}(\bar{\mathcal{O}}_{\bar{v}})\longrightarrow\mathrm{J}_{a}^{\flat}(\bar{\mathcal{O}}_{\bar{v}}/\varepsilon_{\bar{v}}^{\mathrm{N}}\bar{\mathcal{O}}_{\bar{v}})$ . Il s'ensuit que  $\mathcal{R}_{\bar{v}}(a)$  est un quotient de la restriction à la Weil

$$
\prod_ {\operatorname{Spec} (\bar {\mathcal {O}} _ {\bar {v}} / \varepsilon_ {\bar {v}} ^ {\mathrm{N}} \bar {\mathcal {O}} _ {\bar {v}}) / \operatorname{Spec} (\bar {k})} J _ {a} ^ {b} \otimes_ {\bar {\mathcal {O}} _ {\bar {v}}} (\bar {\mathcal {O}} _ {\bar {v}} / \varepsilon_ {\bar {v}} ^ {\mathrm{N}} \bar {\mathcal {O}} _ {\bar {v}})
$$

qui est un  $\bar{k}$ -groupe algébrique affine lisse de type fini. Le lemme s'en déduit.

Le modèle de Néron peut être explicitement construit à l'aide de la normalisation du revêtement caméral. Notons $\tilde{\mathbf{X}}_{a,\bar{v}}$ l'image réciproque de $\mathfrak{t} \to \mathfrak{c}$ par le morphisme $a: \bar{\mathbf{X}}_{\bar{v}} \to \mathfrak{c}$. Considérons la normalisation $\tilde{\mathbf{X}}_{a,\bar{v}}^{\flat}$ de $\tilde{\mathbf{X}}_{a,v}$ qui est un schéma fini et plat au-dessus de $\bar{\mathbf{X}}_{\bar{v}}$ muni d'une action de W. Puisque le corps résiduel de $\bar{\mathbf{X}}_{\bar{v}}$ est algébriquement clos, $\tilde{\mathbf{X}}_{a,\bar{v}}^{\flat}$ est un schéma semi-local complet régulier de dimension un.

Proposition 3.8.2. — Soit $\tilde{\mathrm{X}}_{a,\bar{v}}^{\flat} = \mathrm{Spec}(\widetilde{\mathcal{O}}_{\bar{v}}^{\flat})$ la normalisation de $\tilde{\mathrm{X}}_{a,\bar{v}}$. Alors le modèle de Néron $\mathrm{J}_a^\flat$ de $\mathrm{J}_a$ est le groupe des points fixes sous l'action diagonale de W dans la restriction des scalaires de $\tilde{\mathrm{X}}_{a,\bar{v}}^{\flat}$ à $\bar{\mathrm{X}}_{\bar{v}}$ du tore $\mathrm{T} \times_{\bar{\mathrm{X}}_{\bar{v}}} \tilde{\mathrm{X}}_{a,\bar{v}}^{\flat}$

$$
J _ {a} ^ {\flat} = \prod_ {\tilde {X} _ {a, \bar {v}} ^ {\flat} / \tilde {X} _ {\bar {v}}} (T \times_ {\bar {X} _ {\bar {v}}} \tilde {X} _ {a, \bar {v}} ^ {\flat}) ^ {W}.
$$

Démonstration. — Notons $\pi_{a}^{\flat}$ le morphisme $\tilde{\mathrm{X}}_{a,\bar{v}}^{\flat}\to\bar{\mathrm{X}}_{\bar{v}}$. Comme dans le lemme 2.4.1, le schéma des points fixes sous l'action diagonale de W sur la restriction des scalaires à la Weil $\prod_{\tilde{\mathrm{X}}_{\bar{v}}^{\flat}/\tilde{\mathrm{X}}_{\bar{v}}}(\mathrm{T}\times_{\bar{\mathrm{X}}_{\bar{v}}}\tilde{\mathrm{X}}_{\bar{v}}^{\flat})$ est un schéma en groupes lisse de type fini sur $\bar{\mathrm{X}}_{\bar{v}}$. Il sera plus commode de raisonner avec le faisceau ($\pi_{a*}^{\flat}\mathrm{T})^{\mathrm{W}}$ que représente la restriction à la Weil ci-dessus.

D'après la description galoisienne du centralisateur régulier 2.4, la restriction de $\pi_{a}^{\flat *}J_{a}$ à $\tilde{X}_{a,\bar{v}}^{\flat \bullet} = \tilde{X}_{a,\bar{v}}^{\flat}\times_{\bar{X}_{\bar{v}}}\bar{X}_{\bar{v}}^{\bullet}$ est canoniquement isomorphe au tore $T\times_{\bar{X}_{\bar{v}}^{\bullet}}\tilde{X}_{a,\bar{v}}^{\flat \bullet}$. Le modèle de Néron de $T\times_{\bar{X}_{\bar{v}}^{\bullet}}\tilde{X}_{a,\bar{v}}^{\flat \bullet}$ étant le tore $T\times_{\bar{X}_{\bar{v}}}\tilde{X}_{a,\bar{v}}^{\flat}$, on a un homomorphisme canonique

$$
\pi_ {a} ^ {\flat *} \mathrm{J} _ {a} \longrightarrow \mathrm{T} \times_ {\bar {\mathrm{X}} _ {\bar {v}}} \tilde {\mathrm{X}} _ {a, \bar {v}} ^ {\flat}.
$$

Par adjonction, on a un homomorphisme  $J_{a} \longrightarrow \pi_{a*}^{b} T$ . En fibre générique, cet homomorphisme se factorise par le sous-tore des points fixes sous l'action diagonale W dans  $T \times_{\bar{X}_{v}^{\bullet}} \tilde{X}_{a,\bar{v}}^{b\bullet}$ . On en déduit un homomorphisme  $J_{a} \longrightarrow (\pi_{a*}^{b} T)^{W}$ . Le même raisonnement s'applique en fait à n'importe quel schéma en groupes lisse de type fini ayant la même fibre générique que  $J_{a}$ . Le lemme en résulte donc.

Corollaire 3.8.3. — On a la formule

$$
\dim (\mathcal {P} _ {\bar {v}} (J _ {a})) = \dim_ {\bar {k}} (\mathfrak {t} \otimes_ {\tilde {\mathcal {O}} _ {\bar {v}}} \tilde {\mathcal {O}} _ {\bar {v}} ^ {\flat} / \widetilde {\mathcal {O}} _ {\bar {v}}) ^ {W}.
$$

On obtient ainsi une autre formule pour l'invariant $\delta_{\bar{v}}(a)$. Notons au passage que l'entier $c_{\bar{v}}(a)$ de 3.7.4 est égale à la chute du rang torique du modèle de Néron $\mathrm{J}_{a}^{\flat}$ c'est-à-dire la différence entre $r$ et le rang torique de la fibre spéciale de $\mathrm{J}_{a}^{\flat}$.

3.9. Composantes connexes. — Dans ce paragraphe, nous allons décrire le groupe des composantes connexes  $\pi_{0}(\mathcal{P}_{\bar{v}}(a))$ .

Soit $a: \bar{X}_{\bar{v}} \to \mathfrak{c}$ un morphisme dont l'image n'est pas contenue dans le diviseur discriminant. On a alors un schéma en groupes lisse $J_a$ sur $\bar{X}_{\bar{v}}$ dont la fibre générique est un

tore. Soit  $J_{a}^{0}$  le sous-schéma en groupes ouvert des composantes neutres de  $J_{a}$ . Au-dessus de  $\bar{F}_{\bar{v}}$ ,  $J_{a}$  est connexe de sorte que l'homomorphisme  $J_{a}^{0} \rightarrow J_{a}$  induit un isomorphisme au-dessus de  $\bar{F}_{\bar{v}}$ . En tant qu'homomorphisme de faisceaux en groupes abéliens, c'est un homomorphisme injectif dont le conoyau est supporté par la fibre spéciale de  $\bar{X}_{\bar{v}}$  avec comme fibre

$$
\pi_ {0} (\mathrm{J} _ {a, \bar {v}}) = \mathrm{J} _ {a} (\bar {\mathcal {O}} _ {\bar {v}}) / \mathrm{J} _ {a} ^ {0} (\bar {\mathcal {O}} _ {\bar {v}}).
$$

Les inclusions  $\mathrm{J}_{a}^{0}(\bar{\mathcal{O}}_{\bar{v}})\subset\mathrm{J}_{a}(\bar{\mathcal{O}}_{\bar{v}})\subset\mathrm{J}_{a}(\bar{\mathrm{F}}_{\bar{v}})$  induisent une suite exacte

$$
1 \to \pi_ {0} (\mathrm{J} _ {a, \bar {v}}) \to \mathrm{J} _ {a} (\bar {\mathrm{F}} _ {\bar {v}}) / \mathrm{J} _ {a} ^ {0} (\bar {\mathcal {O}} _ {\bar {v}}) \to \mathrm{J} _ {a} (\bar {\mathrm{F}} _ {\bar {v}}) / \mathrm{J} _ {a} (\bar {\mathcal {O}} _ {\bar {v}}) \to 1.
$$

On a donc un homomorphisme surjectif

$$
\mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a} ^ {0}) \rightarrow \mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a})\tag{3.9.1}
$$

dont le noyau est le groupe fini $\pi_{0}(\mathrm{J}_{a,\bar{v}})$. On en déduit une suite exacte

$$
\pi_ {0} (\mathrm{J} _ {a, \bar {v}}) \to \pi_ {0} (\mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a} ^ {0})) \to \pi_ {0} (\mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a})) \to 1.
$$

Pour déterminer $\pi_0(\mathcal{P}_{\bar{v}}(\mathrm{J}_a))$, il suffit donc de décrire le groupe $\pi_0(\mathcal{P}_{\bar{v}}(\mathrm{J}_a^0))$ et l'image de la flèche $\pi_0(\mathrm{J}_{a,\bar{v}}) \to \pi_0(\mathcal{P}_{\bar{v}}(\mathrm{J}_a^0))$.

Comme dans le cas de la dualité de Tate-Nakayama, le groupe des composantes connexes  $\pi_{0}(\mathcal{P}_{\bar{v}}(J_{a}))$  s'exprime plus aisément à l'aide de la dualité. Pour tout groupe abélien de type fini  $\Lambda$ , nous notons

$$
\Lambda^ {*} = \mathrm{Spec} (\bar {\mathbf {Q}} _ {\ell} [ \Lambda ])
$$

le $\bar{\mathbf{Q}}_{\ell}$-groupe diagonalisable de groupe des caractères $\Lambda$ et inversement pour tout $\bar{\mathbf{Q}}_{\ell}$-groupe diagonalisable A, nous notons A\* son groupe des caractères qui est un groupe abélien de type fini.

Pour écrire des formules explicites, fixons une trivialisation de $\rho_{\mathrm{Out}}$ au-dessus de $\bar{\mathbf{X}}_{\bar{v}}$. Ceci permet en particulier d'identifier W et $\mathbf{W}$. Soit $\tilde{\mathbf{X}}_{a,\bar{v}}^{\bullet}$ l'image réciproque du revêtement fini étale $\pi : \mathfrak{t}^{\mathrm{rs}} \to \mathfrak{c}^{\mathrm{rs}}$ par le morphisme $a: \bar{\mathbf{X}}_{\bar{v}} \to \mathfrak{c}$. En choisissant un point géométrique de $\tilde{\mathbf{X}}_{a,\bar{v}}$ au-dessus du point géométrique $\bar{\eta}_{\bar{v}}$ de $\bar{\mathbf{X}}_{\bar{v}}$, on obtient un homomorphisme $\pi_{a}^{\bullet}: \mathbf{I}_{v} \to \mathbf{W}$.

Proposition 3.9.2. — Avec le choix d'un point géométrique de $\tilde{\mathbf{X}}_{a,\bar{v}}$ au-dessus du point géométrique $\bar{\eta}_{v}$ de $\tilde{\mathbf{X}}_{\bar{v}}$, on a un isomorphisme canonique entre groupes diagonalisables

$$
\pi_ {0} (\mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a} ^ {0})) ^ {*} = \hat {\mathbf {T}} ^ {\pi_ {a} ^ {\bullet} (\mathrm{I} _ {v})}.
$$

De même, on a un isomorphisme

$$
\pi_ {0} (\mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a})) ^ {*} = \hat {\mathbf {T}} (\pi_ {a} ^ {\bullet} (\mathrm{I} _ {v}))
$$

où $\hat{\mathbf{T}}(\pi_{a}^{\bullet}(\mathbf{I}_{v}))$ est le sous-groupe de $\hat{\mathbf{T}}^{\pi_{a}^{\bullet}(\mathbf{I}_{v})}$ formé des éléments $\kappa\in\hat{\mathbf{T}}$ tel que $\pi_{0}(\mathcal{P}_{\bar{v}}(\mathbf{J}_{a}^{0}))$ est contenu dans le groupe de Weyl de la composante neutre $\hat{\mathbf{H}}$ du centralisateur de $\kappa$ dans $\hat{\mathbf{G}}$.

Démonstration. — Considérons le schéma en groupes des composantes neutres  $J_{a}^{b,0}$  du modèle de Néron  $J_{a}^{b}$ . Dans la terminologie de [10], c'est le modèle de Néron connexe. Puisque  $J_{a}^{0}$  a des fibres connexes, l'homomorphisme  $J_{a}^{0} \rightarrow J_{a}^{b}$  se factorise par  $J_{a}^{b,0}$ .

Lemme 3.9.3. — L'homomorphisme $\mathcal{P}_{\bar{v}}(\mathrm{J}_{a}^{0}) \to \mathcal{P}_{\bar{v}}(\mathrm{J}_{a}^{\flat,0})$ induit un isomorphisme de $\pi_{0}(\mathcal{P}_{\bar{v}}(\mathrm{J}_{a}^{0}))$ sur $\mathrm{J}_{a}(\bar{\mathrm{F}}_{\bar{v}})/\mathrm{J}_{a}^{\flat,0}(\bar{\mathcal{O}}_{\bar{v}})$.

Démonstration. — Comme  $J_{a}^{0}$  et  $J_{a}^{b,0}$  ont des fibres connexes, l'homomorphisme  $\mathcal{P}_{\bar{v}}(\mathrm{J}_{a}^{0}) \to \mathcal{P}_{\bar{v}}(\mathrm{J}_{a}^{\mathrm{b},0})$  induit un isomorphisme sur les groupes des composantes connexes. Topologiquement,  $\mathcal{P}_{\bar{v}}(\mathrm{J}_{a}^{\mathrm{b},0})$  est le groupe discret  $\mathrm{J}_{a}(\bar{\mathrm{F}}_{\bar{v}})/\mathrm{J}_{a}^{\mathrm{b},0}(\bar{\mathcal{O}}_{\bar{v}})$ . □

Pour tout tore A sur  $\bar{F}_{\bar{v}}$ , on va considérer le modèle de Néron connexe  $A^{b,0}$  de A sur  $\bar{\mathcal{O}}_{\bar{v}}$  et le groupe abélien de type fini  $\mathrm{A}(\bar{\mathrm{F}}_{\bar{v}})/\mathrm{A}^{\mathrm{b},0}(\bar{\mathcal{O}}_{\bar{v}})$ . On peut vérifier cf. [63] que le foncteur  $\mathrm{A}\mapsto\mathrm{A}(\bar{\mathrm{F}}_{\bar{v}})/\mathrm{A}^{\mathrm{b},0}(\bar{\mathcal{O}}_{\bar{v}})$  vérifie les axiomes du lemme [42, 2.2]. Suivant Kottwitz, on obtient une formule générale pour  $\mathrm{A}(\bar{\mathrm{F}}_{\bar{v}})/\mathrm{A}^{\mathrm{b},0}(\bar{\mathcal{O}}_{\bar{v}})$  et en particulier, on obtient le lemme suivant.

Lemme 3.9.4. — Avec les notations ci-dessus, on a un isomorphisme  $\mathrm{J}_{a}(\bar{\mathrm{F}}_{\bar{v}})/\mathrm{J}_{a}^{\flat,0}(\bar{\mathcal{O}}_{\bar{v}})=(\mathbf{X}_{*})_{\pi_{a}^{\bullet}(\mathrm{I}_{v})}.$

La conjonction des deux lemmes précédents donne l'isomorphisme

$$
\pi_ {0} (\mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a} ^ {0})) = (\mathbf {X} _ {*}) _ {\pi_ {a} ^ {\bullet} (\mathrm{I} _ {v})}
$$

qui induit par dualité la première assertion du théorème

$$
\pi_ {0} (\mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a} ^ {0})) ^ {*} = \hat {\mathbf {T}} ^ {\pi_ {a} ^ {\bullet} (\mathrm{I} _ {v})}.
$$

La démonstration de la deuxième assertion utilise l'astuce des z-extensions. Suivant [44, 7.5], il existe une suite exacte

$$
1 \rightarrow \mathrm{G} \rightarrow \mathrm{G} _ {1} \rightarrow \mathrm{C} \rightarrow 1
$$

de schémas en groupes réductifs au-dessus de X qui se déduit par torsion extérieure d'une suite exacte de groupes réductifs déployés

$$
1 \rightarrow \mathbf {G} \rightarrow \mathbf {G} _ {1} \rightarrow \mathbf {C} \rightarrow 1
$$

où $\mathbf{C}$ est un tore et où $\mathbf{G}_1$ est un groupe réductif de centre connexe. Son groupe dual $\hat{\mathbf{G}}_1$ a un groupe dérivé simplement connexe. Il existe un tore maximal $\mathbf{T}_1$ de $\mathbf{G}_1$ tel qu'on a une suite exacte

$$
1 \rightarrow \mathbf {T} \rightarrow \mathbf {T} _ {1} \rightarrow \mathbf {C} \rightarrow 1.
$$

En remplaçant G par  $G_{1}$ , on va noter  $c_{1}$  à la place de c. L'homomorphisme  $G \rightarrow G_{1}$  induit un morphisme  $\alpha : c \rightarrow c_{1}$ . Au-dessus de  $c_{1}$ , on a le schéma en groupes des centralisateurs réguliers  $J_{1}$  qui est un schéma en groupes lisse à fibres connexes puisque le centre de  $G_{1}$  est connexe cf. 2.3.1. On a une suite exacte de schémas en groupes lisses commutatifs

$$
1 \rightarrow J \rightarrow \alpha^ {*} J _ {1} \rightarrow C \rightarrow 1.
$$

Soit $a: \bar{\mathbf{X}}_{\bar{v}} \to \mathfrak{c}$ tel que $a|_{\bar{\mathbf{X}}_{\bar{v}}^{\bullet}}$ est à l'image dans $\mathfrak{c}^{\mathrm{rs}}$. Notons encore $\alpha(a): \bar{\mathbf{X}}_{\bar{v}} \to \mathfrak{c}_1$ le morphisme obtenu en composant $a$ avec $\alpha$. Sur $\bar{\mathbf{X}}_{\bar{v}}$, on a une suite exacte

$$
1 \to J _ {a} \to J _ {1, \alpha (a)} \to C \to 1
$$

$\operatorname{avec} J_a = a^* J \text{ et } (J_1)_{\alpha(a)} = \alpha(a)^* J_1.$

Proposition 3.9.5. — L'homomorphisme

$$
\pi_ {0} (\mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a})) \rightarrow \pi_ {0} (\mathcal {P} _ {\bar {v}} (\mathrm{J} _ {1, \alpha (a)}))
$$

est injectif.

Démonstration. — Puisque  $J \to \alpha^{*}J_{1}$  est une immersion fermée, en particulier propre, on a  $\mathrm{J}_{a}(\bar{\mathcal{O}}_{\bar{v}}) = \mathrm{J}_{a}(\bar{\mathrm{F}}_{\bar{v}}) \cap (\mathrm{J}_{1})_{\alpha(a)}(\bar{\mathcal{O}}_{\bar{v}})$ . Il s'ensuit que l'homomorphisme

$$
j _ {\alpha (a)}: \mathrm{J} _ {a} (\bar {\mathrm{F}} _ {\bar {v}}) / \mathrm{J} _ {a} (\bar {\mathcal {O}} _ {\bar {v}}) \rightarrow \mathrm{J} _ {1, \alpha (a)} (\bar {\mathrm{F}} _ {\bar {v}}) / \mathrm{J} _ {1, \alpha (a)} (\bar {\mathcal {O}} _ {\bar {v}})
$$

est injectif. Puisque C est un tore sur  $\bar{X}_{\bar{v}}$ ,  $\mathrm{C}(\bar{\mathrm{F}}_{\bar{v}})/\mathrm{C}(\bar{\mathcal{O}}_{\bar{v}})$  est un groupe abélien libre de type fini et discret. La composante neutre de

$$
\mathrm{J} _ {1, \alpha (a)} (\bar {\mathrm{F}} _ {\bar {v}}) / \mathrm{J} _ {1, \alpha (a)} (\bar {\mathcal {O}} _ {\bar {v}})
$$

appartient donc à l'image de $j_{\alpha(a)}$. Par conséquent, $j_{\alpha(a)}$ induit un isomorphisme entre la composante neutre de $\mathrm{J}_{a}(\bar{\mathrm{F}}_{\bar{v}})/\mathrm{J}_{a}(\bar{\mathcal{O}}_{\bar{v}})$ et celle de $\mathrm{J}_{1,\alpha(a)}(\bar{\mathrm{F}}_{\bar{v}})/\mathrm{J}_{1,\alpha(a)}(\bar{\mathcal{O}}_{\bar{v}})$. Il en résulte que l'homomorphisme $\pi_{0}(\mathcal{P}_{\bar{v}}(\mathrm{J}_{a}))\to\pi_{0}(\mathcal{P}_{\bar{v}}((\mathrm{J}_{1})_{\alpha(a)}))$ est injectif.

Corollaire 3.9.6. — Le groupe $\pi_0(\mathcal{P}_{\bar{v}}(\mathrm{J}_a))$ s'identifie canoniquement à l'image de l'homomorphisme $\pi_0(\mathcal{P}_{\bar{v}}(\mathrm{J}_a^0)) \to \pi_0(\mathcal{P}_{\bar{v}}(\mathrm{J}_{1,\alpha(a)})).$

Démonstration. — En plus de la proposition précédente, il suffit d'invoquer la surjectivité de $\pi_{0}(\mathcal{P}_{\bar{v}}(\mathrm{J}_{a}^{0})) \to \pi_{0}(\mathcal{P}_{\bar{v}}(\mathrm{J}_{a}))$.

En choisissant un point géométrique de $\tilde{\mathbf{X}}_{a,\bar{v}}^{\bullet}$, on peut identifier le groupe $\pi_0(\mathcal{P}_{\bar{v}}(\mathrm{J}_a))$ à l'image de l'homomorphisme

$$
(\mathbf {X} _ {*}) _ {\mathrm{I} _ {v}} \rightarrow (\mathbf {X} _ {1, *}) _ {\mathrm{I} _ {v}}
$$

où $\mathbf{X}_{1,*} = \mathrm{Hom}(\mathbf{G}_m, \mathbf{T}_1)$. Notons que l'égalité $\pi_0(\mathcal{P}_{\bar{v}}(\mathbf{J}_{1,\alpha(a)})) = (\mathbf{X}_{1,*})_{\mathrm{I}_v}$ résulte de la connexité des fibres de $\mathrm{J}_1$ et de 3.9.4. Dualement, il existe un isomorphisme entre le sous-groupe $\mathrm{Spec}(\bar{\mathbf{Q}}_\ell[\pi_0(\mathcal{P}_{\bar{v}}(\mathbf{J}_a))])$ de $\hat{\mathbf{T}}^{\mathrm{I}_v}$ et l'image de l'homomorphisme

$$
\hat {\mathbf {T}} _ {1} ^ {\mathrm{I} _ {v}} = \operatorname{Spec} (\bar {\mathbf {Q}} _ {\ell} [ (\mathbf {X} _ {1, *}) _ {\mathrm{I} _ {v}} ]) \to \operatorname{Spec} (\bar {\mathbf {Q}} _ {\ell} [ (\mathbf {X} _ {*}) _ {\mathrm{I} _ {v}} ]) = \hat {\mathbf {T}} ^ {\mathrm{I} _ {v}}.
$$

Il reste maintenant à démontrer que l'image de $\hat{\mathbf{T}}_{1}^{\mathrm{I}_{v}}$ dans $\hat{\mathbf{T}}^{\mathrm{I}_{v}}$ est bien le sous-groupe des éléments $\kappa\in\hat{\mathbf{T}}$ tels que $\pi_{a}^{\bullet}(\mathrm{I}_{v})$ soit contenu dans le groupe de Weyl de la composante neutre $\hat{\mathbf{H}}$ du centralisateur $\hat{\mathbf{G}}_{\kappa}$. Pour tout $\kappa\in\hat{\mathbf{T}}$, pour tout $\kappa_{1}\in\hat{\mathbf{T}}_{1}$ d'image $\kappa$, le centralisateur $\hat{\mathbf{H}}_{1}$ de $\kappa_{1}$ dans $\hat{\mathbf{G}}_{1}$ est connexe et son image dans $\hat{\mathbf{G}}$ est $\hat{\mathbf{H}}$. En effet, $\hat{\mathbf{G}}_{1}$ a un groupe dérivé simplement connexe de sorte que le centralisateur d'un élément semi-simple de $\hat{\mathbf{G}}_{1}$ est connexe. On en déduit ce qu'on voulait.

On a une autre description de $\pi_0(\mathcal{P}_{\bar{v}}(J_a))$ plus explicite mais finalement moins commode à l'usage.

Proposition 3.9.7. — Avec le choix d'un point géométrique de $\tilde{\mathbf{X}}_{a,\bar{v}}$ au-dessus du point géométrique $\bar{\eta}_{v}$ de $\tilde{\mathbf{X}}_{\bar{v}}$, on a un isomorphisme entre $\pi_{0}(\mathcal{P}_{\bar{v}}(\mathbf{J}_{a}))$ et le conoyau du composé des deux flèches

$$
\pi_ {0} (\mathrm{Z} _ {\mathbf {G}}) \rightarrow \pi_ {0} (\mathbf {T} ^ {\pi_ {a} ^ {\bullet} (\mathrm{I} _ {v})}) \rightarrow (\mathbf {X} _ {*}) _ {\pi_ {a} ^ {\bullet} (\mathrm{I} _ {v})}
$$

dont la première se déduit de l'homomorphisme évident  $Z_{\mathbf{G}} \to \mathbf{T}^{\pi_{a}^{\bullet}(\mathrm{I}_{v})}$  et dont la seconde est un isomorphisme canonique de  $\pi_{0}(\mathbf{T}^{\pi_{a}^{\bullet}(\mathrm{I}_{v})})$  sur la partie de torsion de  $(\mathbf{X}_{*})_{\pi_{a}^{\bullet}(\mathrm{I}_{v})}$ .

Démonstration. — On sait que $\pi_0(\mathcal{P}_{\bar{v}}(\mathrm{J}_a))$ est le conoyau de l'homomorphisme $\pi_0(\mathrm{J}_{a,v}) \to \pi_0(\mathcal{P}_{\bar{v}}(\mathrm{J}_a^0))$. D'après 2.3.2, on sait que $\pi_0(\mathrm{J}_{a,v})$ et $\pi_0(\mathrm{Z}_{\mathbf{G}})$ ont la même image dans $(\mathbf{X}_*)_{\pi_a^\bullet (\mathrm{I}_v)}$.

3.10. Densité de l'orbite régulière. — On reporte à la section 4.16 pour une esquisse de la démonstration de la proposition suivante. Elle se déduira de son analogue global qui seul sera démontré de manière détaillée. Seul l'analogue global sera utilisé dans la suite de l'article.

Proposition 3.10.1. — L'ouvert $\mathcal{M}_{v}^{\mathrm{reg}}(a)$ est dense dans $\mathcal{M}_{v}(a)$.

Notons qu'on sait déjà que le fermé complémentaire $\mathcal{M}_{v}(a) - \mathcal{M}_{v}^{\mathrm{reg}}(a)$ est de dimension strictement plus petite que $\dim (\mathcal{M}_v^{\mathrm{reg}}(a))$ cf. 3.7.1.

Corollaire 3.10.2. — L'ensemble des composantes irréductibles de la fibre de Springer affine $\mathcal{M}_{v}(a)$ est en bijection canonique avec le groupe des composantes connexes du groupe $\mathcal{P}_{v}(\mathrm{J}_{a})$.

Démonstration. — On a en effet un isomorphisme  $\mathcal{P}_{v}(J_{a})\to\mathcal{M}_{v}^{\mathrm{reg}}(a)$  en faisant agir  $\mathcal{P}_{v}(J_{a})$  sur le point de Kostant. □

3.11. Le cas d'un groupe endoscopique. — Soit H un groupe endoscopique de G au sens de 1.8. Soit $a_{\mathrm{H}} \in \mathfrak{c}_{\mathrm{H}}(\bar{\mathcal{O}}_{\bar{v}})$ d'image $a \in \mathfrak{c}(\bar{\mathcal{O}}_{\bar{v}}) \cap \mathfrak{c}^{\mathrm{rs}}(\bar{\mathrm{F}}_{\bar{v}})$. S'il n'y a pas de relation directe entre les fibres de Springer affines $\mathcal{M}_{\mathrm{H},v}(a_{\mathrm{H}})$ et $\mathcal{M}_v(a)$, leurs groupes de symétries sont reliés.

On alors deux $\bar{\mathrm{X}}_{\bar{v}}$-schémas en groupes $\mathrm{J}_a = a^*\mathrm{J}$ et $\mathrm{J}_{\mathrm{H},a_{\mathrm{H}}} = a_{\mathrm{H}}^{*}\mathrm{J}_{\mathrm{H}}$ qui sont reliés par un homomorphisme

$$
\mu_ {a _ {\mathrm{H}}}: \mathrm{J} _ {a} \rightarrow \mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}}}
$$

qui est un isomorphisme au-dessus du disque épointé $\bar{\mathbf{X}}_{\vec{v}}^{\bullet}$. Cet homomorphisme est construit en prenant l'image réciproque par $a_{\mathrm{H}}$ de l'homomorphisme $\mu$ construit dans 2.5.1.

Soit $\mathcal{R}_{\mathrm{H},\bar{\nu}}^{\mathrm{G}}(a_{\mathrm{H}})$ le groupe algébrique affine sur $\bar{k}$ dont le groupe des $\bar{k}$-points est

$$
\mathcal {R} _ {\bar {v}} (a _ {\mathrm{H}}) (\bar {k}) = \mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}}} (\bar {\mathcal {O}} _ {\bar {v}}) / \mathrm{J} _ {a} (\bar {\mathcal {O}} _ {\bar {v}}).
$$

On a alors la suite exacte

$$
1 \to \mathcal {R} _ {\mathrm{H}, \bar {v}} ^ {\mathrm{G}} (a _ {\mathrm{H}}) \to \mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a}) \to \mathcal {P} _ {\bar {v}} (\mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}}}) \to 1.\tag{3.11.1}
$$

Lemme 3.11.2. — On a

$$
\dim (\mathcal {R} _ {\mathrm{H}, \bar {v}} ^ {\mathrm{G}} (a _ {\mathrm{H}})) = r _ {\mathrm{H}, \bar {v}} ^ {\mathrm{G}} (a _ {\mathrm{H}})
$$

$où r_{\mathrm{H},\bar{v}}^{\mathrm{G}}(a_{\mathrm{H}})=\deg_{\bar{v}}(a_{\mathrm{H}}^{*}\mathfrak{R}_{\mathrm{G}}^{\mathrm{H}}), \text{ le diviseur } \mathfrak{R}_{\mathrm{G}}^{\mathrm{H}} \text{ de } \mathfrak{c}_{\mathrm{H}} \text{ étant défini dans 1.10.3.}$

Démonstration. — En vertu de la suite exacte 3.11.1, on a

$$
\dim (\mathcal {R} _ {\mathrm{H}, \bar {v}} ^ {\mathrm{G}} (a _ {\mathrm{H}})) = \dim (\mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a})) - \dim (\mathcal {P} _ {\bar {v}} (\mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}}})).
$$

Comme l'homomorphisme  $J_{H,a_{H}} \rightarrow J_{a}$  est un isomorphisme dans la fibre générique, on l'égalité

$$
c _ {\bar {v}} (a _ {\mathrm{H}}) = c _ {\bar {v}} (a)
$$

où  $c_{\bar{v}}(a_{\mathrm{H}})$  et  $c_{\bar{v}}(a)$  sont les invariants galoisiens qui apparaissent dans la formule de dimension de Bezrukavnikov cf. 3.7.5. En appliquant cette formule à a et  $a_{H}$ , on trouve

$$
\dim (\mathcal {R} _ {\mathrm{H}, \bar {v}} ^ {\mathrm{G}} (a _ {\mathrm{H}})) = \deg_ {\bar {v}} (a ^ {*} \mathfrak {D} _ {\mathrm{G}}) - \deg_ {\bar {v}} (a _ {\mathrm{H}} ^ {*} \mathfrak {D} _ {\mathrm{H}}).
$$

Il suffit maintenant d'évoquer 1.10.3 pour conclure.

Soit maintenant $a_{\mathrm{H}} \in \mathfrak{c}_{\mathrm{H}}(\mathcal{O}_{v})$ d'image $a \in \mathfrak{c}(\mathcal{O}_{v}) \cap \mathfrak{c}^{\mathrm{rs}}(\mathrm{F}_{v})$. Avec la même définition que ci-dessus, on obtient un groupe $\mathcal{R}_{v}(a_{\mathrm{H}})$ défini sur $k$. On a la formule

$$
\mathcal {R} _ {\mathrm{H}, v} ^ {\mathrm{G}} (a _ {\mathrm{H}}) \otimes_ {k} \bar {k} = \prod_ {\bar {v}: k _ {v} \to \bar {k}} \mathcal {R} _ {\bar {v}} (a)
$$

qui implique la formule de dimension

$$
\dim \mathcal {R} _ {\mathrm{H}, v} ^ {\mathrm{G}} (a _ {\mathrm{H}}) = \deg (k _ {v} / k) \deg_ {v} (a _ {\mathrm{H}} ^ {*} \mathfrak {R} _ {\mathrm{G}} ^ {\mathrm{H}}).
$$

En identifiant  $\mathcal{P}_{v}(\mathrm{J}_{a})$  avec l'ouvert  $\mathcal{M}_{v}^{\mathrm{reg}}(a)$  de  $\mathcal{M}_{v}(a)$  et en identifiant  $\mathcal{P}_{v}(\mathrm{J}_{\mathrm{H},a_{\mathrm{H}}})$  avec l'ouvert  $\mathcal{M}_{\mathrm{H},v}(a_{\mathrm{H}})$ , puis en prenant l'adhérence du graphe de l'homomorphisme  $\mu_{a_{H}}$  dans  $\mathcal{M}_{v}(a)\times\mathcal{M}_{v}(a_{\mathrm{H}})$ , on obtient une correspondance intéressante entre ces deux fibres de Springer affines. Nous n'allons pas utiliser cette correspondance dans ce travail.

## 4. Fibration de Hitchin

Dans son article mémorable [34], Hitchin a observé que le fibré cotangent de l'espace de module des fibrés stables sur une courbe forme un système hamiltonien complètement intégrable. Pour cela, il construit explicitement une famille de fonctions commutantes pour le crochet de Poisson en nombre égal à la moitié de la dimension de ce cotangent. Ces fonctions définissent un morphisme vers un espace affine dont la fibre générique est essentiellement une variété abélienne. Ce morphisme particulièrement joli est la fibration de Hitchin.

Nous adopterons un point de vue différent en considérant les fibres de la fibration de Hitchin comme l'analogue global des fibres de Springer affines. En particulier, nous remplaçons le fibré canonique de la courbe par un fibré inversible de degré très grand. En faisant ainsi, nous perdons la forme symplectique tout en gardant une fibration ayant la même allure que la fibration originale de Hitchin.

Comme nous l'avons observé dans [57], le comptage des points dans un corps fini de la fibration de Hitchin généralisée dans ce sens donne formellement le côté géométrique de la formule des traces pour l'algèbre de Lie. Ceci continue à nous servir de guide dans ce chapitre pour étudier les propriétés géométriques de la fibration de Hitchin. Le comptage de points sera passé en revue dans le chapitre 8.

Notre outil favori pour explorer la géométrie de la fibration de Hitchin $f: \mathcal{M} \to \mathcal{A}$ est un champ de Picard $\mathcal{P} \to \mathcal{A}$ agissant sur $\mathcal{M}$. Cette action est fondée sur la construction du centralisateur régulier du chapitre 2. On démontre en particulier qu'il existe un ouvert $\mathcal{M}^{\text{reg}}$ de $\mathcal{M}$ cf. 4.3.3 sur lequel $\mathcal{P}$ agit simplement transitivement et qui est dense dans chaque fibre $\mathcal{M}_a$ cf. 4.16.1. On peut analyser la structure de $\mathcal{P}_a$ en détails grâce à la courbe camérale et à la théorie du modèle de Néron. Ceci permet en particulier de définir un ouvert $\mathcal{A}^\diamond$ au-dessus duquel $\mathcal{M}$ est essentiellement un schéma abélien.

On fera aussi certains calculs utiles pour la suite comme le calcul des dimensions 4.13, celui du groupe des composantes connexes de $\mathcal{P}_a$ cf. 4.10 et celui du groupe des automorphismes des fibrés de Higgs cf. 4.11.

Le point clé de ce chapitre est la formule de produit 4.15.1 qui établit la relation entre la fibre de Hitchin et les fibres de Springer affines. Cette formule a été démontrée dans [57]. Elle joue un rôle crucial dans le chapitre sur le comptage 8 et elle est en filigrane dans la démonstration du théorème du support dans le chapitre 7.

On établit enfin un lien entre la fibration de Hitchin de G et celle d'un groupe endoscopique. Il existe un morphisme canonique $\nu : \mathcal{A}_{\mathrm{H}} \to \mathcal{A}$ et si $a_{\mathrm{H}} \mapsto a$, on a un homomorphisme canonique $\mu : \mathcal{P}_a \to \mathcal{P}_{\mathrm{H}, a_{\mathrm{H}}}$. En revanche, il n'y a pas de relation directe entre les fibres de Hitchin $\mathcal{M}_a$ et $\mathcal{M}_{\mathrm{H}, a_{\mathrm{H}}}$ mais une correspondance qui se déduit de $\mu$ par adhérence schématique. On n'utilisera pas cette correspondance dans la suite de l'article mais il vaut probablement le coup de l'exploiter davantage.

Voici les notations qui seront utilisées dans ce chapitre. On fixe une courbe X propre lisse et géométriquement connexe de genre g sur un corps fini k. Soit  $\bar{k}$  une clôture algébrique de k. On note  $\bar{X}=X\otimes_{k}\bar{k}$ .

On note F le corps des fonctions rationnelles sur X. Soit  $|X|$  l'ensemble des points fermés de X. Chaque élément  $v \in |X|$  définit une valuation  $v : F^{\times} \to Z$ . Notons  $F_{v}$  la complétion de F par rapport à cette valuation,  $O_{v}$  son anneau des entiers et  $k_{v}$  son corps résiduel. On note  $X_{v} = \text{Spec}(\mathcal{O}_{v})$  le disque formel en v et  $X_{v}^{\bullet} = \text{Spec}(F_{v})$  le disque formel épointé.

Soit $\mathbf{G}$ un groupe de Chevalley dont le nombre de Coxeter $\mathbf{h}$ satisfait l'inégalité $2\mathbf{h} < p$ où $p$ est la caractéristique de $k$. Soit $\mathbf{G}$ un X-schéma en groupes réductif qui est une forme quasi-déployée de $\mathbf{G}$ définie par un $\operatorname{Out}(\mathbf{G})$-torseur $\rho_{\mathrm{G}}$ comme dans 1.3. Le schéma en groupes $\mathbf{G}$ est alors muni d'un épinglage (T, B, $\mathbf{x}_{+}$). En particulier, on a un X-schéma des polynômes caractéristique $\mathfrak{c}$, le morphisme de Chevalley $\chi : \mathfrak{g} \to \mathfrak{c}$ où $\mathfrak{g} = \operatorname{Lie}(\mathbf{G})$ et un morphisme fini plat $\pi : \mathfrak{t} \to \mathfrak{c}$ qui au-dessus de l'ouvert $\mathfrak{c}^{\mathrm{rs}}$ est un torseur sous le schéma en groupes fini étale W obtenu en tordant $\mathbf{W}$ par $\rho_{\mathrm{G}}$.

Nous fixons un fibré inversible D sur X qui est le carré  $D = D'^{\otimes 2}$  d'un autre fibré inversible  $D'$ . De règle générale, nous supposons que le degré de D sera plus grand que 2g où g est le genre de X ce qui est contraire à [34] où D est le fibré canonique. Nous indiquerons néanmoins les endroits où cette hypothèse est vraiment nécessaire.

Notons que  $G_{m}$  agit sur g et t par homothétie, et agit sur c de façon compatible. On notera  $g_{D} = g \otimes_{O_{X}} D$ ,  $t_{D} \otimes_{O_{X}} D$ . Il revient au même de définir  $g_{D}$  et  $t_{D}$  en tordant les vectoriels g et t munis de l'homothétie par le  $G_{m}$ -torseur attaché au fibré inversible D. De même, on construit  $c_{D}$  en tordant c par le même  $G_{m}$ -torseur.

4.1. Rappels sur Bun$_G$. — Nous considérons le champ Bun$_G$ qui associe à tout $k$-schéma S le groupoïde des G-torseurs sur X $\times$ S. Le champ Bun$_G$ est un champ algébrique au sens d'Artin cf. [53] et [33, Prop. 1]. Le groupoïde des $k$-points de Bun$_G$ peut s'exprimer comme une réunion disjointe des doubles quotients

$$
\operatorname{Bun} _ {\mathrm{G}} (k) = \bigsqcup_ {\xi \in \ker^ {1} (\mathrm{F}, \mathrm{G})} \left[ \mathrm{G} ^ {\xi} (\mathrm{F}) \backslash \overset {\vee} {\prod} _ {v \in | \mathrm{X} |} \mathrm{G} (\mathrm{F} _ {v}) / \mathrm{G} (\mathcal {O} _ {v}) \right]
$$

sur l'ensemble $\ker^{1}(\mathrm{F},\mathrm{G})$ des G-torseurs sur F qui sont localement triviaux. Ici, $\mathbf{G}^{\xi}$ désigne la forme intérieure forte de G sur F donnée par la classe $\xi\in\ker^{1}(\mathrm{F},\mathrm{G})$ et le produit

$\check{\Pi}$ désigne un produit restreint. Ici nous avons choisi pour chaque $\xi \in \ker^{1}(\mathrm{F},\mathrm{G})$ un G-torseur sur F ayant $\xi$ pour classe d'isomorphisme et qui est muni d'une trivialisation sur chaque corps local $\mathrm{F}_v$.

Pour tout $v \in |\mathbf{X}|$, on dispose comme dans 3.1 de la grassmannienne affine $\mathcal{G}_v$ et d'un morphisme

$$
\zeta : \mathcal {G} _ {v} \longrightarrow \mathrm{Bun} _ {\mathrm{G}}
$$

qui consiste à recoller le G-torseur sur  $X_{v} \hat{\times} S$  muni d'une trivialisation sur  $X_{v}^{\bullet} \hat{\times} S$ , avec le G-torseur trivial sur  $(X - v) \times S$ . L'existence de ce recollement formel est démontré d'abord par Beauville et Laszlo dans le cas des fibrés vectoriels cf. [4] et dans le cas général par Heinloth [33, Lem. 5]. Au niveau des k-points, ce morphisme est le foncteur évident

$$
\mathrm{G} (\mathrm{F} _ {v}) / \mathrm{G} (\mathcal {O} _ {v}) \longrightarrow \left[ \mathrm{G} (\mathrm{F}) \backslash \overset {\checkmark} {\prod_ {v \in | \mathrm{X} |}} \mathrm{G} (\mathrm{F} _ {v}) / \mathrm{G} (\mathcal {O} _ {v}) \right]
$$

qui envoie  $g_{v} \in \mathrm{G}(\mathrm{F}_{v}) / \mathrm{G}(\mathcal{O}_{v})$  sur l'uplet constitué de  $g_{v}$  et des éléments neutres de  $\mathrm{G}(\mathrm{F}_{v'}) / \mathrm{G}(\mathcal{O}_{v'})$  pour toutes les places  $v' \neq v$ .

4.2. Construction de la fibration. — Rappelons la définition de l'espace de module de Hitchin.

Définition 4.2.1. — L'espace total de Hitchin est le groupoïde fibré M qui associe à tout k-schéma S le groupoïde M(S) des couples (E,  $\phi$ ) constitués d'un G-torseur E sur X × S et d'une section

$$
\phi \in \mathrm{H} ^ {0} (\mathrm{X} \times \mathrm{S}, \mathrm{ad(E)} \otimes_ {\mathcal {O} _ {\mathrm{X}}} \mathrm{D})
$$

où ad(E) est le fibré en algèbres de Lie obtenu en tordant g muni de l'action adjointe par le G-torseur E.

4.2.2. — Il revient au même de dire que $\mathcal{M}(\mathrm{S})$ est le groupoïde des morphismes $h_{\mathrm{E},\phi}:\mathrm{X}\times \mathrm{S}\to [\mathfrak{g}_{\mathrm{D}} / \mathrm{G}]$. Ce champ est un fibré vectoriel au-dessus du champ algébrique $\mathrm{Bun}_{\mathrm{G}}$ classifiant les G-torseurs au-dessus de X si bien qu'il est lui-même un champ algébrique localement de type fini.

4.2.3. — Le morphisme caractéristique de Chevalley  $\chi : g \to c$  induit un morphisme

$$
[ \chi ]: [ \mathfrak {g} _ {\mathrm{D}} / \mathrm{G} ] \to \mathfrak {c} _ {\mathrm{D}}.
$$

On obtient un morphisme

$$
f \colon \mathcal {M} \to \mathcal {A}
$$

où pour tout $k$-schéma S, $\mathcal{A}(\mathrm{S})$ est le groupoïde des morphismes $a: \mathrm{X} \times \mathrm{S} \to \mathfrak{c}_{\mathrm{D}}$. Il revient au même de dire que $\mathcal{A}$ est l'ensemble des sections globales $\mathfrak{c}_{\mathrm{D}}$ au-dessus de X. Si on veut, on peut munir $\mathfrak{c}_{\mathrm{D}}$ d'une structure de fibré vectoriel fondée sur la structure affine de la section de Kostant. Dans ce cas $\mathcal{A}$ sera muni d'une structure de $k$-espace vectoriel de dimension finie. Cette structure n'est pas vraiment utile sauf afin de simplifier certain calcul de dimension.

4.2.4. — Étant donnée une racine carrée D' de D, on obtient une section  $\epsilon_{D'} : A \to M$  du morphisme  $f : M \to A$  en utilisant 2.2.5. Cette section est essentiellement la même que la section construite par Hitchin de façon plus explicite dans le cas des groupes classiques. On l'appellera la section de Kostant-Hitchin. En fait, Hitchin a utilisé la matrice compagnon au lieu de la section de Kostant.

4.2.5. — En écrivant D sous la forme  $\mathrm{D} = \mathcal{O}_{\mathrm{X}}(\sum_{v \in |\mathrm{X}|} d_v v)$ , l'ensemble  $\mathfrak{c}_{\mathrm{D}}(k)$  s'identifie à un sous-ensemble fini de  $\mathfrak{c}(\mathrm{F})$ . D'après [57, 1.3], pour  $a \in \mathfrak{c}_{\mathrm{D}}(k)$  semi-simple régulier et anisotrope, le nombre de points à valeurs dans k de la fibre  $M_a$  s'exprime en termes de sommes d'intégrales orbitales globales

$$
\sum_ {\xi \in \ker^ {1} (\mathrm{F}, \mathrm{G})} \sum_ {\gamma \in \mathfrak {g} ^ {\xi} (\mathrm{F}) / \sim , \chi (\gamma) = a} \mathbf {0} _ {\gamma} (1 _ {\mathrm{D}})\tag{4.2.6}
$$

qui est une partie de la formule cf. 1.13.2. Dans [57], nous avons construit une interprétation géométrique du processus de stabilisation de cette formule cf. 1.13. Ce processus de comptage et stabilisation sera examiné de façon plus systématique dans le chapitre 8.

Dans la suite de ce chapitre, nous allons rappeler cette géométrie et l'étudier de façon plus détaillée.

4.3. Symétries d'une fibre de Hitchin. — Comme pour les fibres de Springer affines, la construction des symétries naturelles d'une fibre de Hitchin est fondée sur le lemme 2.1.1.

4.3.1. — Pour tout S-point $a$ de $\mathcal{A}$, on a un morphisme $h_a: \mathrm{X} \times \mathrm{S} \to [\mathfrak{c}/\mathbf{G}_m]$. On note $\mathrm{J}_a = h_a^* \mathrm{J}$ l'image réciproque de J sur $[\mathfrak{c}/\mathbf{G}_m]$ et on considère le groupoïde de Picard $\mathcal{P}_a(\mathrm{S})$ des $\mathrm{J}_a$-torseurs au-dessus de $\mathrm{X} \times \mathrm{S}$. C'est un $\mathrm{X} \times \mathrm{S}$-schéma en groupes lisse car J est un $\mathfrak{c}$-schéma en groupes lisse. Quand $a$ varie, cette construction définit un groupoïde de Picard $\mathcal{P}$ fibré au-dessus de $\mathcal{A}$.

4.3.2. — L'homomorphisme $\chi^{*}\mathrm{J}\rightarrow\mathrm{I}$ du lemme 2.2.1 induit pour tout S-point (E, $\phi$) au-dessus de $a$ un homomorphisme

$$
\mathrm{J} _ {a} \rightarrow \mathrm{Aut} _ {\mathrm{X} \times \mathrm{S}} (\mathrm{E}, \phi) = h _ {\mathrm{E}, \phi} ^ {*} \mathrm{I}.
$$

Par conséquent, on peut tordre (E,  $\phi$ ) par n'importe quel  $J_{a}$ -torseur. Ceci définit une action du groupoïde de Picard  $\mathcal{P}_{a}(S)$  fibré sur le groupoïde  $\mathcal{M}_{a}(S)$ . En laissant le point a varier, on obtient une action de P sur M relativement à la base A.

Comme pour les fibres de Springer affines, nous considérons l'ouvert  $M^{reg}$  de M dont les points sont les morphismes  $h_{E,\phi}: X \times S \to [g_{D}/G]$  qui se factorisent par l'ouvert  $[g_{D}^{reg}/G]$ .

Proposition 4.3.3. — $\mathcal{M}^{\mathrm{reg}}$ est un ouvert de $\mathcal{M}$ ayant des fibres non vides au-dessus de $\mathcal{A}$. De plus, c'est un torseur sous l'action de $\mathcal{P}$.

Démonstration. — Pour tout  $a \in \mathcal{A}(\bar{k})$ , le point  $[\epsilon]^{\mathrm{D}'}(a)$  construit dans cf. 2.2.5 est dans l'ouvert régulier. Ceci montre que le morphisme  $M^{\mathrm{reg}} \to A$  a les fibres non vides. On déduit du lemme 2.2.1 que  $M_{a}^{reg}$  est un torseur sous  $P_{a}$ .

4.3.4. — La section de Kostant-Hitchin 4.2.4 $\epsilon_{\mathrm{D}^{\prime}}: \mathcal{A} \to \mathcal{M}$ se factorise par l'ouvert $\mathcal{M}^{\mathrm{reg}}$ car la section de Kostant $\epsilon: \mathfrak{c} \to \mathfrak{g}$ se factorise à travers $\mathfrak{g}^{\mathrm{reg}}$. Cette section définit un isomorphisme de $\mathcal{P}$ sur l'ouvert $\mathcal{M}^{\mathrm{reg}}$ de $\mathcal{M}$.

Proposition 4.3.5. — Le champ de Picard P est lisse au-dessus de A.

Démonstration. — Puisque  $J_{a}$  est un schéma en groupes lisse commutatif, l'obstruction à la déformation d'un  $J_{a}$ -torseur gît dans le groupe  $\mathrm{H}^{2}(\bar{\mathrm{X}},\mathrm{Lie}(\mathrm{J}_{a}))$ . Or, celui-ci est nul car  $\bar{X}$  est un schéma de dimension un.

4.4. Cas linéaire. — On va analyser les fibres de M et de P au-dessus d'un point  $a \in \mathcal{A}^{\heartsuit}(\bar{k})$ . Commençons par le cas du groupe linéaire : soit  $G = \mathrm{GL}(r)$ . Dans ce cas, on peut décrire les fibres de Hitchin à l'aide des courbes spectrales en suivant Hitchin [34] et Beauville-Narasimhan-Ramanan [5]. On pourrait faire de même pour les groupes classiques cf. [34] et [59].

## 4.4.1. — Dans le cas G = GL(r), l'espace affine A est l'espace vectoriel

$$
\mathcal {A} = \bigoplus_ {i = 1} ^ {r} \mathrm{H} ^ {0} (\mathrm{X}, \mathrm{D} ^ {\otimes i}).
$$

La donnée d'un point $a = (a_{1}, \ldots, a_{r}) \in \mathcal{A}(\bar{k})$ détermine une courbe spectrale $\mathrm{Y}_{a}$ tracée sur l'espace total $\Sigma_{\mathrm{D}}$ du fibré en droites D. Cette courbe est donnée par l'équation

$$
t ^ {r} - a _ {1} t ^ {r - 1} + \dots + (- 1) ^ {r} a _ {r} = 0.
$$

On définit un ouvert $\mathcal{A}^{\heartsuit}$ de $\mathcal{A}$ dont les points géométriques $a\in\mathcal{A}^{\heartsuit}(\bar{k})$ définissent une courbe spectrale réduite. Si $a\in\mathcal{A}^{\heartsuit}(\bar{k})$, la fibre de Hitchin $\mathcal{M}_{a}$ est le groupoïde $\overline{\mathrm{Pic}}(\mathrm{Y}_{a})$ des $\mathcal{O}_{\mathrm{Y}_{a}}$-modules sans torsion de rang un d'après [5]. La fibre $\mathcal{P}_{a}$ est le groupoïde $\mathrm{Pic}(\mathrm{Y}_{a})$ des $\mathcal{O}_{\mathrm{Y}_{a}}$-modules inversibles. $\mathrm{Pic}(\mathrm{Y}_{a})$ agit sur $\overline{\mathrm{Pic}}(\mathrm{Y}_{a})$ par produit tensoriel et $\overline{\mathrm{Pic}}(\mathrm{Y}_{a})$ contient $\mathrm{Pic}(\mathrm{Y}_{a})$ comme un ouvert.

4.4.2. — Si la courbe spectrale  $Y_{a}$  est lisse, il n'y pas de différence entre  $\operatorname{Pic}(Y_{a})$  et  $\overline{\operatorname{Pic}}(Y_{a})$  c'est-à-dire  $P_{a}$  agit simplement transitivement sur  $M_{a}$ . De plus, dans ce cas, la structure de  $P_{a}$  est aussi simple que possible. Le groupe des composantes connexes de  $P_{a}$  est isomorphe à Z par l'application degré car  $Y_{a}$  est connexe. La composante neutre de  $P_{a}$  est isomorphe au quotient de la jacobienne de  $Y_{a}$  par le groupe  $G_{m}$  agissant trivialement.

4.4.3. — Soit $\xi : \mathrm{Y}_{a}^{\flat} \to \mathrm{Y}_{a}$ la normalisation de $\mathrm{Y}_{a}$. Le foncteur d'image réciproque induit un homomorphisme

$$
\xi^ {*}: \operatorname{Pic} (\mathrm{Y} _ {a}) \to \operatorname{Pic} (\mathrm{Y} _ {a} ^ {\flat})
$$

qui induit un isomorphisme

$$
\pi_ {0} (\mathrm{Pic} (\mathrm{Y} _ {a})) \stackrel {\sim} {\to} \pi_ {0} (\mathrm{Pic} (\mathrm{Y} _ {a} ^ {\flat})) = \mathbf {Z} ^ {\pi_ {0} (\mathrm{Y} _ {a} ^ {\flat})}.
$$

Le noyau de $\xi^{*}$ est un groupe affine commutatif de dimension

$$
\delta_ {a} = \dim \mathrm{H} ^ {0} (\mathrm{Y} _ {a}, \xi_ {*} \mathcal {O} _ {\mathrm{Y} _ {a} ^ {\flat}} / \mathcal {O} _ {\mathrm{Y} _ {a}}).
$$

4.4.4. — Par construction,  $Y_{a}$  est une courbe tracée sur une surface lisse qui en particulier n'a que des singularités planes. D'après Altman, Iarrobino et Kleiman [1],  $\operatorname{Pic}(Y_{a})$  est alors un ouvert dense de  $\overline{\operatorname{Pic}}(Y_{a})$ .

Nous allons maintenant généraliser la discussion ci-dessus à un groupe réductif général.

4.5. Courbe camérale. — L'outil de base pour étudier  $P_{a}$  est la construction de la courbe camérale due à Donagi. Considérons le diagramme cartésien

![](images/page_59_image_10.jpg)

dont le morphisme de la ligne inférieure associe à un couple  $(x, a)$  formé de  $x \in X$  et de  $a \in A$ , le point  $a(x) \in \mathfrak{c}_{\mathrm{D}}$ . Le morphisme de gauche qui se déduit de  $\pi$  par changement de base est un morphisme fini et plat muni d'une action de W.

En prenant la fibre en chaque point  $a \in \mathcal{A}(\bar{k})$ , on obtient le revêtement caméral  $\pi_{a}: \tilde{\mathrm{X}}_{a} \to \bar{\mathrm{X}}$  de Donagi. Dans la suite, on va se restreindre aux paramètres a tels que  $\pi_{a}$  est génériquement un revêtement étale. Ces paramètres forment un ouvert de A qui peut être décrit comme suit.

Considérons l'image inverse U de  $c_{D}^{rs} \subset c_{D}$  dans  $X \times A$ . Le morphisme de  $U \to A$  étant lisse, son image est un ouvert de A que nous allons noter  $A^{\heartsuit}$ . Ses  $\bar{k}$ -points sont décrits comme suit

$$
\mathcal {A} ^ {\heartsuit} (\bar {k}) = \{a \in \mathcal {A} (\bar {k}) \mid a (\bar {\mathrm{X}}) \not \subset \mathfrak {D} _ {\mathrm{G,D}} \}.
$$

Si $\deg(D) > 2g$, l'ouvert $\mathcal{A}^{\heartsuit}$ est non vide. La borne $2g$ n'a rien d'optimal ici, le cas original étant le fibré canonique de degré $2g - 2$. On reporte la démonstration à 4.7.1 où on démontre un énoncé plus fort.

Lemme 4.5.1. — Pour tout point géométrique $a \in \mathcal{A}^{\heartsuit}(\bar{k})$, le revêtement $\pi_{a}: \tilde{\mathrm{X}}_{a} \to \mathrm{X} \otimes_{k} \bar{k}$ est génériquement un torseur sous W. De plus, $\tilde{\mathrm{X}}_{a}$ est une courbe réduite.

Démonstration. — Par définition de $\mathcal{A}^{\heartsuit}$, l'intersection $\mathrm{U}_{a}$ de U avec la fibre $\mathrm{X} \times \{a\}$ est un ouvert non vide de $\bar{\mathrm{X}}$. Par construction, $\pi_{a}$ est un W-torseur au-dessus de cet ouvert dense. Puisque $\pi_{a}$ est un morphisme fini plat, $\pi_{a*}\mathcal{O}_{\tilde{\mathrm{X}}_{a}}$ est un $\mathcal{O}_{\bar{\mathrm{X}}}$-module sans torsion. S'il est génériquement réduit, il est partout réduit.

4.5.2. — Pour tout  $a \in \mathcal{A}^{\heartsuit}(\bar{k})$ , on a une flèche injective de faisceaux pour la topologie étale

$$
\mathrm{J} _ {a} \rightarrow \mathrm{J} _ {a} ^ {1} = (\pi_ {a, *} (\tilde {\mathrm{X}} _ {a} \times_ {\mathrm{X}} \mathrm{T})) ^ {\mathrm{W}}
$$

qui se déduit de 2.4.2 et dont le noyau est un faisceau fini de support fini entièrement explicite. Cette flèche permet de contrôler  $J_{a}$  et donc  $P_{a}$  à l'aide de la courbe camérale.

Le tore T n'est pas nécessairement trivial au-dessus de $\tilde{\mathbf{X}}_a$. Il est parfois nécessaire de passer à un revêtement étale pour le rendre trivial. C'est pour cette raison qu'on va introduire certaines variantes de la courbe camérale que voici. Considérons un revêtement fini connexe étale galoisien $\rho : \bar{\mathbf{X}}_{\rho} \to \bar{\mathbf{X}}$ de groupe de Galois $\Theta_{\rho}$ qui rend le torseur $\rho_{\mathrm{G}}$ trivial. On a alors un diagramme cartésien :

$$
\begin{array}{c} \bar {\mathbf {X}} _ {\rho} \times \mathbf {t} \xrightarrow {\pi} \bar {\mathbf {X}} _ {\rho} \times \mathbf {c} \\ \Biggl \downarrow \\ \mathbf {t} \xrightarrow {\pi} \mathbf {c} \end{array}\tag{4.5.3}
$$

dont les flèches verticales se déduisent de $\rho$ par changement de base et donc finies et étales. Pour tout $a \in \mathcal{A}(\bar{k})$, construisons le revêtement $\pi_{\rho,a}: \tilde{\mathrm{X}}_{\rho,a} \to \bar{\mathrm{X}}$ en formant le

produit cartésien :

$$
\begin{array}{c} \tilde {\mathrm{X}} _ {\rho , a} \longrightarrow \bar {\mathrm{X}} _ {\rho} \times \mathbf {t} _ {\mathrm{D}} \\ \pi_ {\rho , a} \Big \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \pi_ {\rho} \\ \bar {\mathrm{X}} \xrightarrow [ a ]{} \mathfrak {c} _ {\mathrm{D}} \end{array}\tag{4.5.4}
$$

On a alors la formule

$$
\mathbf {J} _ {a} ^ {1} = \pi_ {\rho , a, *} (\mathbf {T}) ^ {\mathbf {W} \rtimes \Theta_ {\rho}}
$$

suivant 2.4.4.

Proposition 4.5.5. — Supposons que $\deg(\mathrm{D}) > 2g$. Notons $\Theta$ l'image de l'homomorphisme $\rho_{\mathrm{G}}^{\bullet} : \pi_{1}(\overline{\mathrm{X}}, \infty) \to \operatorname{Out}(\mathbf{G})$. Supposons que $\Theta$ est un groupe fini d'ordre premier à la caractéristique. Pour tout $a \in \mathcal{A}^{\infty}(\bar{k})$, on $a$

$$
\mathrm{H} ^ {0} (\bar {\mathrm{X}}, \mathrm{J} _ {a}) = (\mathrm{ZG}) ^ {\Theta}
$$

et

$$
\mathrm{H} ^ {0} (\bar {\mathrm{X}}, \operatorname{Lie} (\mathrm{J} _ {a})) = \operatorname{Lie} (\mathrm{ZG}) ^ {\Theta}.
$$

En particulier, si au-dessus de $\bar{\mathbf{X}}$ le centre de $\mathbf{G}$ ne contient pas de tore déployé, alors $\mathcal{P}_a$ est un champ de Picard de Deligne-Mumford.

Démonstration. — Le point clé que la courbe $\tilde{\mathbf{X}}_{\rho,a}$ est connexe sera reporté à 4.6.1. Admettons-le pour l'instant. On a alors

$$
\mathrm{H} ^ {0} (\bar {\mathrm{X}}, \mathrm{J} _ {a} ^ {1}) = \mathbf {T} ^ {\mathbf {W} \rtimes \Theta}
$$

qui est un groupe fini non ramifié sous l'hypothèse que ZG ne contient pas de tores déployés. Le groupe  $\mathrm{H}^{0}(\bar{\mathrm{X}},\mathrm{J}_{a})$  en est un sous-groupe. En utilisant la description explicite de  $J\to J^{1}$  cf. 2.4.7 et le fait que la section a rencontre toutes les composantes irréductibles du lieu de discriminant, on peut montrer que

$$
\mathrm{H} ^ {0} (\bar {\mathrm{X}}, \mathrm{J} _ {a}) = \mathrm{Z} \mathbf {G} ^ {\Theta}.
$$

Comme cette description explicite ne sera pas utilisée dans la suite, on laisse au lecteur le soin de reconstituer les détails.

4.5.6. — Il n'est pas difficile d'introduire un rigidificateur pour bénéficier de la représentabilité. Soit  $\infty \in X$  un point fixé et soit  $A^{\infty}$  l'ouvert de A des points a qui sont réguliers semi-simples en  $\infty$ . Pour tout  $a \in A^{\infty}$ , notons  $P_{a}^{\infty}$  le champ de Picard classifiant des  $J_{a}$ -torseurs munis d'une trivialisation en  $\infty$ .

Proposition 4.5.7. — Le foncteur $\mathcal{P}^{\infty}$ est représentable par un schéma en groupes lisse localement de type fini au-dessus de $\mathcal{A}^{\infty}$. Pour tout $a \in \mathcal{A}^{\infty}$, le tore $\mathrm{J}_{a,\infty}$ agit sur $\mathcal{P}^{\infty}$ en modifiant la rigidification et induit un isomorphisme canonique du champ quotient $[\mathcal{P}_a^\infty / \mathrm{J}_{a,\infty}]$ et $\mathcal{P}_a$.

Démonstration. — La première assertion se déduit de la représentabilité du schéma de Picard du revêtement étale de la courbe camérale  $\tilde{X}_{\rho,a}$ . La seconde assertion est immédiate.

4.6. Courbe camérale connexe. — Sous l'hypothèse deg(D) > 2g, on peut démontrer que la courbe camérale $\tilde{\mathbf{X}}_a$ est connexe. Mais ce dont on a besoin dans la suite est un énoncé de connexité légèrement plus fort. Considérons un revêtement fini connexe étale galoisien $\rho : \bar{\mathbf{X}}_{\rho} \to \bar{\mathbf{X}}$ qui rend le torseur $\rho_{\mathrm{G}}$ trivial. On a alors construit un revêtement

$$
\pi_ {\rho , a}: \tilde {\mathrm{X}} _ {\rho , a} \to \bar {\mathrm{X}}
$$

comme dans 4.5.4.

Proposition 4.6.1. — Supposons que $\deg(\mathrm{D}) > 2g$. Alors pour tout $a \in \mathcal{A}^{\heartsuit}(\bar{k})$, les courbes $\tilde{\mathbf{X}}_a$ et $\tilde{\mathbf{X}}_{\rho,a}$ sont connexes.

Démonstration. — Quitte à remplacer  $\bar{X}$  par  $\bar{X}_{\rho}$ , il suffit de démontrer que la courbe camérale  $\tilde{X}_{a}$  est connexe dans le cas où G est déployé. Dans ce cas, on fait appel au théorème suivant dû à Debarre [17, th. 1.4] qui généralise un théorème de Bertini.

Théorème 4.6.2. — Soient M une variété irréductible et m : M → P un morphisme de M dans un produit d'espaces projectifs  $P = P^{n_{1}} \times \cdots \times P^{n_{r}}$ . Dans chaque  $P^{n_{i}}$ , on se donne un sous-espace linéaire  $L_{i} \subset P^{n_{i}}$  tel que pour tout sous-ensemble I  $\subset \{1, \ldots, n\}$ , on a

$$
\dim (p _ {\mathrm{I}} (m (\mathbf {M}))) > \sum_ {i \in \mathrm{I}} \operatorname{codim} (\mathrm{L} _ {i})
$$

où  $p_{I}$  est la projection de P sur  $\prod_{i\in I}P^{n_{i}}$ . Supposons aussi que m est propre au-dessus d'un ouvert V de P et que  $L=L_{1}\times\cdots\times L_{r}$  est contenu dans V. Alors,  $m^{-1}(L)$  est connexe.

Voici comment appliquer ce résultat à notre cas particulier. Puisque G est déployé,  $c_{D}$  en tant que schéma est un produit fibré au-dessus de  $\bar{X}$  de fibrés en droites  $D^{\otimes e_{i}}$ . On peut compactifier chacun de ces fibrés en droites  $D^{\otimes e_{i}}$  en un fibré en droites projectives

$$
\bar {\mathrm{D}} ^ {\otimes e _ {i}} = \operatorname{Proj} _ {\bar {\mathrm{X}}} (\operatorname{Sym} _ {\mathcal {O} _ {\bar {\mathrm{X}}}} (\mathrm{D} ^ {\otimes - e _ {i}} \oplus \mathcal {O} _ {\mathrm{X} _ {\rho}}))
$$

qui est une  $\bar{k}$ -surface projective. On note  $Z_{i} = \bar{D}^{e_{i}} - D^{e_{i}}$  le diviseur à l'infini. Le fibré inversible  $\mathcal{O}(1)$  attaché à ce Proj est très ample par hypothèse  $\deg(D) > 2g$  et induit un plongement projectif

$$
\bar {\mathbf {D}} ^ {\otimes e _ {i}} \hookrightarrow \mathbf {P} ^ {n _ {i}}
$$

de cette surface.

Le sous-schéma localement fermé  $\prod_{i=1}^{r}D^{\otimes e_{i}}$  de  $P=\prod_{i=1}^{r}P^{n_{i}}$  est un sous-schéma fermé de V où

$$
\mathrm{V} = \prod_ {i = 1} ^ {r} \mathbf {P} ^ {n _ {i}} - \bigcup_ {i = 1} ^ {r} \left(\mathrm{Z} _ {i} \times \prod_ {j \neq i} \bar {\mathrm{D}} ^ {\otimes e _ {j}}\right).
$$

Il en est de même de $\mathfrak{c}_{\mathrm{D}}$ qui est un sous-schéma fermé de $\prod_{i=1}^{r} \mathrm{D}^{\otimes e_i}$. Ce qui joue le rôle de la variété irréductible M dans le théorème de Debarre est $\mathfrak{t}_{\mathrm{D}}$ qui est fini au-dessus de $\mathfrak{c}_{\mathrm{D}}$ de sorte que M est de dimension $r+1$ et que le morphisme composé $m: \mathrm{M} \to \mathrm{V}$ est un morphisme propre.

La composante $a_{i}\in \mathrm{H}^{0}(\bar{\mathrm{X}},\mathrm{D}^{\otimes e_{i}})$ de $a$ définit un hyperplan $\mathbf{L}_i$ de $\mathbf{P}^{n_i}$ car

$$
(a _ {i}, 1) \in \mathrm{H} ^ {0} (\mathbf {P} ^ {n _ {i}}, \mathcal {O} (1)) = \mathrm{H} ^ {0} (\bar {\mathrm{X}}, \mathrm{D} ^ {\otimes e _ {i}}) \oplus \mathrm{H} ^ {0} (\bar {\mathrm{X}}, \mathcal {O} _ {\bar {\mathrm{X}}})
$$

dont l'intersection avec la surface $\bar{\mathbf{D}}^{\otimes e_i}$ ne rencontre pas le diviseur à l'infini $\mathbf{Z}_i$, autrement dit, est contenue dans la surface ouverte $\mathbf{D}^{\otimes e_i}$. Comme $\mathbf{L}_i \cap \mathbf{Z}_i = \emptyset$, le produit $\mathbf{L} = \prod_{i=1}^{r} \mathbf{L}_i$ est contenu dans l'ouvert $\mathbf{V}$.

Comme $\tilde{\mathrm{X}}_a = m^{-1}(\mathrm{L})$, il ne reste qu'à vérifier que pour tout sous-ensemble $\mathrm{I} \subset \{1, \ldots, n\}$, on a

$$
\dim (p _ {\mathrm{I}} (m (\mathrm{M}))) > \sum_ {i \in \mathrm{I}} \operatorname{codim} (\mathrm{L} _ {i}).
$$

Mais on vérifie immédiatement que la dimension de  $p_{\mathrm{I}}(m(\mathbf{M}))$  est égale à  $\sharp I + 1$  ce qui termine la démonstration du lemme.

4.7. Courbe camérale connexe et lisse. — Nous allons étudier l'ouvert $\mathcal{A}^{\diamond}$ où les fibres de $\mathcal{M}_{a}$ sont aussi simples que possible. Cet ouvert est défini comme suit. Un point $a\in\mathcal{A}(\bar{k})$ appartient à cet ouvert si la section $h_{a}:\bar{\mathbf{X}}\to\mathfrak{c}_{\mathrm{D}}$ coupe transversalement le diviseur $\mathfrak{D}_{\mathrm{D}}$. Ici $\mathfrak{D}_{\mathrm{D}}$ désigne le diviseur de $\mathfrak{c}_{\mathrm{D}}$ obtenu en tordant le diviseur $\mathfrak{D}\subset\mathfrak{c}$ par le $\mathbf{G}_{m}$-torseur $\mathrm{L}_{\mathrm{D}}$ associé au fibré inversible D. Comme on le verra dans 4.7.3, il revient au même de demander que la courbe camérale soit lisse.

Proposition 4.7.1. — Si deg(D) > 2g, l'ouvert $\mathcal{A}^{\diamond}$ est non vide.

La démonstration est complètement similaire à celle du théorème de Bertini due à Zariski. Commençons par démontrer un lemme.

Lemme 4.7.2. — Supposons deg(D) > 2g où g est le genre de X. Pour tout  $x \in \bar{\mathbf{X}}(\bar{k})$  défini par un idéal  $m_{x}$ . La flèche

$$
\mathrm{H} ^ {0} (\bar {\mathrm{X}}, \mathfrak {c}) \to \mathfrak {c} \otimes_ {\mathcal {O} _ {\bar {\mathrm{X}}}} \mathcal {O} _ {\bar {\mathrm{X}}} / \mathfrak {m} _ {x} ^ {2}
$$

est surjective. Ici le fibré vectoriel c est vu comme un  $O_{X}$ -module localement libre de rang r.

Démonstration. — En passant au revêtement fini étale $\rho : \mathrm{X}_{\rho} \to \mathrm{X}$, $\mathfrak{c}$ devient isomorphe à une somme directe

$$
\rho^ {*} \mathfrak {c} = \bigoplus_ {i = 1} ^ {r} \rho^ {*} \mathrm{D} ^ {\otimes e _ {i}}
$$

où les $e_i$ sont définis dans 1.2 et en particulier sont des entiers plus grands ou égaux à 1. Comme $\mathfrak{c}$ est un facteur direct de $\rho_*\rho^*\mathfrak{c}$, il suffit de démontrer la surjectivité de la flèche

$$
\mathrm{H} ^ {0} \left(\bar {\mathrm{X}} ^ {\prime}, \rho^ {*} \mathfrak {c}\right)\rightarrow \rho^ {*} \mathfrak {c} \otimes_ {\mathcal {O} _ {\bar {\mathrm{X}}}} \mathcal {O} _ {\bar {\mathrm{X}}} / \mathfrak {m} _ {x} ^ {2}.
$$

Il suffit de démontrer cette surjectivité pour chacun des facteurs directs $\rho^{*}\mathrm{D}^{\otimes e_{i}}$.

Il est loisible de supposer ici que  $X_{\rho}$  est géométriquement connexe. Notons  $g'$  son genre. On a alors  $2g' - 2 = n(2g - 2)$  où n est le degré de  $\rho$ . La surjectivité ci-dessus se déduit de l'inégalité

$$
\deg (\mathrm{D} ^ {\otimes e _ {i}}) > 2 n g = (2 g ^ {\prime} - 2) + 2 n.
$$

Le lemme en résulte.

Démonstration. — Revenons à la proposition 4.7.1. Dans $\mathfrak{D}_{\mathrm{G,D}}$, on a un ouvert lisse $\mathfrak{D}_{\mathrm{D}} - \mathfrak{D}_{\mathrm{D}}^{\mathrm{sing}}$ complément d'un fermé $\mathfrak{D}_{\mathrm{D}}^{\mathrm{sing}}$ de codimension 2 dans $\mathfrak{c}_{\mathrm{D}}$.

Considérons le sous-schéma  $Z_{1}$  de  $(\mathfrak{D}_{\mathrm{G,D}} - \mathfrak{D}_{\mathrm{G,D}}^{\mathrm{sing}}) \times \mathcal{A}$  constitué des couples  $(c, a)$  tels que la section  $a(\bar{\mathbf{X}})$  passe par le point c et intersecte avec le diviseur  $D_{G}$  en ce point avec une multiplicité au moins 2. D'après le lemme ci-dessus

$$
\dim (Z _ {1}) \leq \dim (\mathcal {A}) - 1
$$

de sorte que la projection $Z_{1}\to\mathcal{A}$ n'est pas surjective.

Considérons le sous-schéma  $Z_{2}$  de  $D_{G}^{sing} \times A$  des couples  $(c, a)$  tels que la section  $a(\bar{\mathbf{X}})$  passe par c. De nouveau d'après le lemme, on a une estimation de dimension

$$
\dim (\mathrm{Z} _ {2}) \leq \dim (\mathcal {A}) - 1
$$

de sorte que la réunion des images de  $Z_{1}$  et de  $Z_{2}$  est contenue dans un sous-schéma fermé strict de A. Il existe donc un point  $a \in A^{\heartsuit}$  tel que la section  $a(\bar{\mathbf{X}})$  ne coupe pas le lieu singulier  $D_{G,D}^{sing}$  du discriminant et coupe le lieu lisse de ce diviseur transversalement. □

Lemme 4.7.3. — Un point $a \in \mathcal{A}(\bar{k})$ est dans l'ouvert $\mathcal{A}^{\diamond}(\bar{k})$ si et seulement si la courbe camérale $\tilde{\mathbf{X}}_a$ est lisse.

Démonstration. — Supposons que $a \in \mathcal{A}^{\diamond}(\bar{k})$ c'est-à-dire la section $a(\bar{\mathrm{X}})$ dans $\mathfrak{c}_{\mathrm{D}}$ coupe transversalement le diviseur $\mathfrak{D}_{\mathrm{G,D}}$. Montrons que l'image inverse de cette section sur le revêtement $\mathrm{X}_{\rho} \times \mathbf{t}_{\mathrm{D}}$ est lisse. En dehors du diviseur $\mathfrak{D}_{\mathrm{G,D}}$, ce revêtement est étale

si bien qu'il n'y a rien à vérifier. La condition que l'image $a(\bar{\mathbf{X}})$ coupe transversalement le diviseur $\mathfrak{D}_{\mathrm{G,D}}$ implique qu'elle ne rencontre pas le lieu singulier $\mathfrak{D}_{\mathrm{G,D}}^{\mathrm{sing}}$ de $\mathfrak{D}_{\mathrm{G,D}}$. Un couple $(v,x)\in \mathfrak{t}_{\mathrm{D}}(\bar{k})$ est composé d'un point $v\in \mathbf{X}(\bar{k})$ et d'un point $x$ dans la fibre de $\mathfrak{t}_{\mathrm{D}}$ au-dessus de $x$. Au-dessus de $v$, le groupe $\mathbf{G}$ est déployé de sorte qu'on peut parler des hyperplans de racine dans la fibre de $\mathfrak{t}_{\mathrm{D}}$ au-dessus de $v$. Si $(v,x)\in \mathfrak{t}_{\mathrm{D}}(\bar{k})$ est au-dessus d'un point d'intersection de $a(\bar{\mathbf{X}})$ avec $\mathfrak{D}_{\mathrm{G,D}} - \mathfrak{D}_{\mathrm{G,D}}^{\mathrm{sing}}$, $x$ appartient à un unique hyperplan de racine. On peut donc se ramener au cas d'un groupe de rang semi-simple un. Dans ce cas, un calcul direct montre que le complété formel $\tilde{\mathbf{X}}_a$ en $(v,x)$ est de la forme $\bar{k}[[\epsilon_v]][[t] / (t^2 -\epsilon_v^m)$ où $\epsilon_v$ est un uniformisant de $\bar{\mathbf{X}}$ en le point $v$ et $m$ est la multiplicité d'intersection de $a(\bar{\mathbf{X}})$ avec $\mathfrak{D}_{\mathrm{G,D}}$ en ce point. Dans le cas transversal $m = 1$, ceci implique que $\tilde{\mathbf{X}}_a$ est lisse en $(\tilde{v},x)$.

Supposons maintenant que $a \notin \mathcal{A}^{\diamond}(\bar{k})$. Si $a(\bar{\mathbf{X}})$ coupe le lieu lisse de $\mathfrak{D}_{\mathrm{G,D}}$ avec une multiplicité au moins deux, le calcul ci-dessus montre que $\tilde{\mathbf{X}}_a$ n'est pas lisse. Supposons maintenant que $a(\bar{\mathbf{X}})$ coupe le lieu $\mathfrak{D}_{\mathrm{G,D}}^{\mathrm{sing}}$ en un point $v \in \bar{\mathbf{X}}$. Supposons que $\tilde{\mathbf{X}}_a$ est lisse en le point $(v, x) \in \mathfrak{t}_{\mathrm{D}}(\bar{k})$ au-dessus de $v$. Le point $x$ appartient alors à au moins deux hyperplans de racine différents de sorte que le groupe de monodromie locale $\pi_a^\bullet(\mathbf{I}_v)$ cf. 3.7.3 contient deux involutions différentes. Ceci n'est pas possible car sous l'hypothèse que la caractéristique de $k$ ne divise pas l'ordre de $\mathbf{W}$, le groupe de monodromie locale $\pi_a^\bullet(\mathbf{I}_v)$ est un groupe cyclique.

Corollaire 4.7.4. — Soit $\bar{\mathbf{X}}_{\rho} \to \bar{\mathbf{X}}$ un revêtement fini étale galoisien connexe qui déploie G. Supposons deg(D) > 2g. Alors pour tout $a \in \mathcal{A}^{\diamond}(\bar{k})$, la courbe $\tilde{\mathbf{X}}_{\rho,a}$ est irréductible.

Démonstration. — D'après 4.6.1, $\tilde{\mathbf{X}}_{\rho,a}$ est connexe. Comme $\tilde{\mathbf{X}}_a$ est lisse, le revêtement étale $\tilde{\mathbf{X}}_{\rho,a}$ l'est aussi. Elle est donc irréductible.

Voici la traduction galoisienne de cet énoncé. Soit U l'ouvert de $\bar{\mathbf{X}}$ au-dessus duquel le revêtement $\tilde{\mathbf{X}}_a\to \bar{\mathbf{X}}$ est un W-torseur. Soient $\infty$ un point géométrique de U et $\tilde{\infty}$ un point géométrique de $\tilde{\mathbf{X}}_a$ au-dessus de $u$. Comme dans 1.3.6, on a alors un homomorphisme

$$
\pi_ {a} ^ {\bullet}: \pi_ {1} (\mathrm{U}, \infty) \rightarrow \mathbf {W} \rtimes \operatorname{Out} (\mathbf {G})
$$

au-dessus de

$$
\rho_ {\mathrm{G}} ^ {\bullet}: \pi_ {1} (\bar {\mathrm{X}}, \infty) \to \operatorname{Out} (\mathbf {G}).
$$

Notons $\Theta$ l'image de l'homomorphisme $\rho_{\mathrm{G}}^{\bullet}$.

Corollaire 4.7.5. — Si $a \in \mathcal{A}^{\diamond}(\bar{k})$, alors l'image de $\pi_{a}^{\bullet}$ est $\mathbf{W} \rtimes \Theta$.

Définition 4.7.6. — Un $\bar{k}$-champ abélien est le quotient d'une $\bar{k}$-variété abélienne par l'action triviale d'un groupe diagonalisable.

L'exemple typique d'un champ abélien est le champ classifiant les fibrés inversibles de degré zéro sur une courbe projective lisse connexe définie sur  $\bar{k}$ . Si cette courbe est munie d'une action d'un groupe fini d'ordre premier à la caractéristique, les composantes neutres des champs de Prym associés sont des champs abéliens.

Proposition 4.7.7. — Pour tout $a \in \mathcal{A}^{\diamond}(\bar{k})$, l'ouvert $\mathcal{M}_{a}^{\text{reg}}$ est $\mathcal{M}_{a}$ tout entier de sorte que $\mathcal{M}_{a}$ est un torseur sous $\mathcal{P}_{a}$. La composante neutre de $\mathcal{P}_{a}$ est un champ abélien.

Démonstration. — On renvoie à [57, pr. 4.2] pour la démonstration de la première assertion.

Considérons un revêtement connexe fini étale galoisien  $\tilde{X}_{\rho} \rightarrow \tilde{X}$  de groupe de Galois  $\Theta$  qui trivialise  $\rho_{G}$ . On a construit le revêtement étale  $\tilde{X}_{\rho,a}$  de la courbe camérale  $\tilde{X}$  qui est alors une courbe projective lisse et connexe cf. 4.6.1. La seconde assertion résulte de ce que la composante neutre du champ des T-torseurs sur  $\tilde{X}_{\rho,a}$  est alors un champ abélien.

Rappelons que si le centre G ne contient pas de tores déployés sur  $\bar{X}$ , la composante neutre de  $P_{a}$  est en plus de Deligne-Mumford d'après 4.5.5.

4.7.8. — Pour tout  $a \in \mathcal{A}^{\heartsuit}(\bar{k})$ , on a vu que le groupe d'inertie de  $P_{a}$  s'identifie à  $ZG^{\Theta}$ . On verra dans 4.10.4 que pour  $a \in \mathcal{A}^{\diamondsuit}(\bar{k})$  le groupe des composantes connexes  $\pi_{0}(\mathcal{P}_{a})$  s'identifie à  $Z\hat{G}^{\Theta}$ . On peut observer que si  $G_{1}$  et  $G_{2}$  sont duaux l'un de l'autre et si  $a \in \mathcal{A}_{G_{1}}^{\diamondsuit}(\bar{k}) = \mathcal{A}_{G_{2}}^{\diamondsuit}(\bar{k})$ , le groupe d'inertie de  $P_{G_{1},a}$  est isomorphe au groupe des composantes connexes de  $P_{G_{2},a}$  et vice versa.

4.8. Modèle de Néron global. — Soient $a \in \mathcal{A}^{\heartsuit}(\bar{k})$ et U l'image réciproque de l'ouvert $\mathfrak{c}_{\mathrm{D}}^{\mathrm{rs}}$ par le morphisme $a: \bar{\mathrm{X}} \to \mathfrak{c}_{\mathrm{D}}^{\mathrm{rs}}$.

Comme dans le cas local 3.8, la structure du champ de Picard $\mathcal{P}_a$ des $J_a$-torseurs sur $\bar{\mathbf{X}}$ peut être analysée à l'aide du modèle de Néron $J_a^b$ de $J_a$. C'est un schéma en groupes lisse de type fini au-dessus de $\bar{\mathbf{X}}$ muni d'un homomorphisme $J_a \to J_a^b$ qui est un isomorphisme au-dessus de U. Il est de plus caractérisé par la propriété suivante : pour tout schéma en groupes lisse de type fini $J'$ sur $\bar{\mathbf{X}}$ avec un homomorphisme $J_a \to J'$ qui est un isomorphisme sur U, il existe un unique homomorphisme $J' \to J_a^b$ tel que le triangle évident commute. L'existence de ce modèle de Néron est un résultat de Bosch, Lutkebohmer et Raynaud cf. [10, ch. 10, pr. 6]. De nouveau, le modèle de Néron de type fini n'est qu'un sous-schéma ouvert du modèle de Néron localement de type fini qu'ils ont construit.

Ce modèle de Néron global s'obtient à partir des modèles de Néron locaux cf. 3.8 comme suit. Pour tout $v \in \bar{\mathbf{X}} - \mathbf{U}$, on note $\bar{\mathbf{X}}_v$ la complétion de $\bar{\mathbf{X}}$ en $v$ et $\bar{\mathbf{X}}_v^\bullet = \bar{\mathbf{X}}_v - \{v\}$. Considérons le modèle de Néron du tore $\mathrm{J}_a|_{\bar{\mathbf{X}}_v^\bullet}$. En recollant les modèles de Néron en les différents points $v \in \bar{\mathbf{X}} - \mathbf{U}$ avec le tore $\mathrm{J}_a|_{\mathrm{U}}$, on obtient un schéma en

groupes commutatifs lisse  $J_{a}^{b}$  au-dessus de  $\bar{X}$  muni d'un homomorphisme de schémas en groupes  $J_{a} \rightarrow J_{a}^{b}$ .

Comme dans 3.8.2, $J_{a}^{\flat}$ peut être exprimé à l'aide de la normalisation $\tilde{X}_{a}^{\flat}$ de la courbe camérale $\tilde{X}_{a}$. L'action de W sur $\tilde{X}_{a}$ induit une action de ce groupe sur $\tilde{X}_{a}^{\flat}$. Notons $\pi_{a}^{\flat}: \tilde{X}_{a}^{\flat} \to \bar{X}$ le morphisme vers $\bar{X}$. Voici la conséquence globale de l'énoncé local 3.8.2.

Corollaire 4.8.1. — $J_{a}^{b}$ s'identifie au sous-groupe des points fixes sous l'action diagonale de W dans $\prod_{\tilde{X}_{a}^{\flat}/\tilde{X}}(T \times_{\tilde{X}} \tilde{X}_{a}^{\flat})$.

Considérons le groupoïde de Picard $\mathcal{P}_{a}^{\flat}$ des $J_{a}^{\flat}$-torseurs. L'homomorphisme de schémas en groupes $J_{a} \to J_{a}^{\flat}$ induit un homomorphisme de groupoïdes de Picard $\mathcal{P}_{a} \to \mathcal{P}_{a}^{\flat}$. Cet homomorphisme réalise essentiellement la structure générale d'un groupe algébrique sur un corps algébriquement clos comme l'extension d'une variété abélienne par un groupe algébrique affine cf. [66]. La démonstration qui suit s'inspire d'un argument de Raynaud [64].

## Proposition 4.8.2.

(1) L'homomorphisme $\mathcal{P}_a(\bar{k})\to \mathcal{P}_a^{\flat}(\bar{k})$ est essentiellement surjectif.

(2) La composante neutre $(\mathcal{P}_a^b)^0$ de $\mathcal{P}_a^b$ est un champ abélien.

(3) Le noyau $\mathcal{R}_a$ de $\mathcal{P}_a \to \mathcal{P}_a^\flat$ est un produit de groupes algébriques affines de type fini $\mathcal{R}_v(a)$ qui sont définis dans le lemme 3.8.1. Ceux-ci sont triviaux sauf en un nombre fini de points $v \in |\bar{\mathbf{X}}|$.

## Démonstration.

1. Par la construction du modèle de Néron, l'homomorphisme  $J_{a} \rightarrow J_{a}^{b}$  est injectif en tant qu'homomorphisme entre faisceaux en groupes abéliens pour la topologie étale de  $\bar{X}$ . Considérons la suite exacte

$$
1 \rightarrow J _ {a} \rightarrow J _ {a} ^ {\flat} \rightarrow J _ {a} ^ {\flat} / J _ {a} \rightarrow 1\tag{4.8.3}
$$

où le quotient  $J_{a}^{b}/J_{a}$  est supporté par le fermé fini  $\bar{X}-U$  et la suite exacte longue de cohomologie qui s'en déduit. Comme  $H^{1}(\bar{X},J_{a}^{b}/J_{a})=0$ , l'homomorphisme

$$
\mathrm{H} ^ {1} (\bar {\mathrm{X}}, \mathrm{J} _ {a}) \rightarrow \mathrm{H} ^ {1} (\bar {\mathrm{X}}, \mathrm{J} _ {a} ^ {\flat})
$$

est surjectif.

2. Soit $\tilde{\mathbf{X}}_a$ l'image réciproque du revêtement $\mathfrak{t}_{\mathrm{D}} \to \mathfrak{c}_{\mathrm{D}}$ par le morphisme $h_a: \bar{\mathbf{X}} \to \mathfrak{c}_{\mathrm{D}}$. Soit $\tilde{\mathbf{X}}_a^{\flat}$ la normalisation de $\tilde{\mathbf{X}}_a$. D'après la proposition 3.8.2, le modèle de Néron $\mathbf{J}_a^{\flat}$ ne dépend que du revêtement $\tilde{\mathbf{X}}_a^{\flat}$. Plus précisément $\mathbf{J}_a^{\flat}$ consiste en les points fixes sous l'action diagonale de W dans la restriction à la Weil $\prod_{\tilde{\mathbf{X}}_a^{\flat}/\bar{\mathbf{X}}} (\mathrm{T} \times_{\bar{\mathbf{X}}} \tilde{\mathbf{X}}_a^{\flat})$. Il en résulte qu'à isogénie près, $\mathcal{P}_a^{\flat}$ est un facteur

du groupoïde des T-torseurs sur $\tilde{\mathbf{X}}_a^{\flat}$ lequel est isomorphe au produit de $r$ copies du $\mathrm{Pic}(\tilde{\mathbf{X}}_a^{\flat})$. Puisque $\tilde{\mathbf{X}}_a^{\flat}$ est une courbe projective lisse éventuellement non connexe, la composante neutre de $\mathrm{Pic}(\tilde{\mathbf{X}}_a^{\flat})$ est le quotient d'un produit de variétés jacobiennes par un produit de $\mathbf{G}_m$ agissant trivialement.

3. La dernière assertion résulte aussi de la suite exacte longue de cohomologie qui se déduit de la suite exacte courte (4.8.3). Ayant défini le noyau comme la catégorie des  $J_{a}$ -torseurs munis d'une trivialisation du  $J_{a}^{b}$ -torseur qui s'en déduit, on n'a pas en fait à se préoccuper des  $H^{0}$  dans la suite longue.

Considérons un revêtement fini étale galoisien connexe $\rho : \bar{\mathbf{X}}_{\rho} \to \bar{\mathbf{X}}$ de groupe de Galois $\Theta$ qui trivialise le torseur $\rho_{\mathrm{G}}$. Pour tout $a \in \mathcal{A}^{\heartsuit}(\bar{k})$, on a un revêtement fini plat $\pi_{\rho,a}: \tilde{\mathbf{X}}_{\rho,a} \to \bar{\mathbf{X}}$ comme dans 4.5.4 qui est génériquement étale galoisien de groupe de Galois $\mathbf{W} \rtimes \Theta$. Soit $\tilde{\mathbf{X}}_{\rho,a}^{\flat}$ la normalisation de $\tilde{\mathbf{X}}_{\rho,a}$ qui est aussi munie d'une action de $\mathbf{W} \rtimes \Theta$. Soit $\pi_{\rho,a}^{\flat}$ sa projection sur $\bar{\mathbf{X}}$. On a alors une description galoisienne de $\mathrm{J}_a^\flat$

$$
\mathrm{J} _ {a} ^ {\flat} = \prod_ {\tilde {\mathrm{X}} _ {\rho , a} ^ {\flat} / \bar {\mathrm{X}}} (\mathbf {T} \times \tilde {\mathrm{X}} _ {\rho , a} ^ {\flat}) ^ {\mathbf {W} \rtimes \Theta}
$$

dont le lemme suivant résulte.

Lemme 4.8.4. — Soient  $C_{\tilde{a}}$  une composante connexe de  $\tilde{X}_{\rho,a}$  et  $W_{\tilde{a}}$  le sous-groupe des éléments de  $W \rtimes \Theta$  qui stabilisent  $C_{\tilde{a}}$ . Si  $T^{W_{\tilde{a}}}$  est fini non-ramifié,  $P_{a}^{b}$  est un champ abélien de Deligne-Mumford.

4.9. Invariant $\delta_{a}$. — Un invariant numérique important qu'on peut attacher à $a \in \mathcal{A}^{\heartsuit}(\bar{k})$ est l'invariant delta.

4.9.1. — Pour tout  $a \in \mathcal{A}^{\heartsuit}(\bar{k})$ , considérons le noyau

$$
\mathcal {R} _ {a} := \ker [ \mathcal {P} _ {a} \longrightarrow \mathcal {P} _ {a} ^ {\flat} ]\tag{4.9.2}
$$

qui classifie les  $J_{a}$ -torseurs sur X munis d'une trivialisation du  $J_{a}^{\flat}$ -torseur qui s'en déduit. C'est un groupe algébrique affine de type fini qui se décompose en produit

$$
\mathcal {R} _ {a} = \prod_ {v \in \bar {\mathrm{X}} - \mathrm{U}} \mathcal {R} _ {v} (a)
$$

où $\mathcal{R}_v(a)$ est le groupe défini en 3.8.1. On définit l'invariant $\delta_a$ comme la dimension de $\mathcal{R}_a$.

4.9.3. — Rappelons qu'en prenant un rigidificateur cf. 4.5.6, on a défini un groupe algébrique lisse commutatif  $P_{a}^{0}$  qui se surjecte sur la composante neutre  $P_{a}^{0}$ . D'après le théorème de structure de Chevalley, on dispose d'une suite exacte canonique

$$
1 \rightarrow \mathrm{R} _ {a} \rightarrow \mathrm{P} _ {a} ^ {0} \rightarrow \mathrm{A} _ {a} \rightarrow 1
$$

où  $A_{a}$  est une variété abélienne et où  $R_{a}$  est un groupe affine connexe. L'homomorphisme  $R_{a} \to P_{a}^{b,0}$  étant nécessairement trivial, on dispose d'un homomorphisme surjectif  $A_{a} \to P_{a}^{b,0}$ . Sous l'hypothèse de 4.8.4, c'est en fait une isogénie étale. Il s'ensuit la formule

$$
\dim (\mathrm{A} _ {a}) = d - \delta_ {a}.
$$

Dans ce cas et dans ce cas seulement, il est justifié d'appeler  $\delta_{a}$  la dimension de la partie affine de  $P_{a}$ .

L'invariant $\delta_{a}$ s'écrit comme une somme d'invariants $\delta$ locaux

$$
\delta_ {a} := \dim (\mathcal {R} _ {a}) = \sum_ {v \in \bar {\mathrm{X}} - \mathrm{U}} \delta_ {v} (a).
$$

La conjonction de 4.8.2 et de la formule de dimension du groupe des symétries locales 3.8.3 donne une formule pour l'invariant $\delta$ global.

Corollaire 4.9.4. — Pour tout $a \in \mathcal{A}^{\heartsuit}(\bar{k})$, l'invariant $\delta_{a}$ défini comme ci-dessus est égal à

$$
\delta_ {a} = \dim \mathrm{H} ^ {0} (\bar {\mathrm{X}}, \mathfrak {t} \otimes_ {\mathcal {O} _ {\bar {\mathrm{X}}}} (\pi_ {a *} ^ {\flat} \mathcal {O} _ {\tilde {\mathrm{X}} _ {a} ^ {\flat}} / \pi_ {a *} \mathcal {O} _ {\tilde {\mathrm{X}} _ {a}})) ^ {\mathrm{W}}.
$$

De nouveau, on a une autre formule qui exprime l'invariant  $\delta$  global en fonction du discriminant corrigé par des invariants monodromiques locaux comme dans la formule de Bezrukavnikov.

Rappelons que le discriminant $\mathfrak{D}_{\mathrm{G}}$ est un polynôme homogène de degré $\sharp \Phi$ sur $\mathfrak{c}$, $\sharp \Phi$ étant le nombre de racines dans le système de racines $\Phi$. Il s'ensuit que pour tout $a \in \mathcal{A}^{\heartsuit}(\bar{k})$, $a^{*}\mathfrak{D}_{\mathrm{G},\mathrm{D}}$ est un diviseur linéairement équivalent à $\mathrm{D}^{\otimes (\sharp \Phi)}$ de sorte que

$$
\deg (a ^ {*} \mathfrak {D} _ {\mathrm{G,D}}) = \sharp \Phi \deg (\mathrm{D}).
$$

Écrivons

$$
a ^ {*} \mathfrak {D} _ {\mathrm{G,D}} = d _ {1} v _ {1} + \dots + d _ {n} v _ {n}
$$

où $v_1, \ldots, v_n$ sont des points deux à deux distincts de $\bar{\mathbf{X}}$ et où $d_i$ est la multiplicité de $v_i$. Pour tout $i = 1, \ldots, n$, notons $c_i$ la chute du rang torique de $\mathrm{J}_a^\flat$ en le point $v_i$. La formule suivante est un corollaire immédiat de 3.7.5.

Proposition 4.9.5. — On a l'égalité

$$
2 \delta_ {a} = \sum_ {i = 1} ^ {n} (d _ {i} - c _ {i}) = \sharp \Phi \deg (\mathrm{D}) - \sum_ {i = 1} ^ {n} c _ {i}.
$$

4.10. Le groupe  $\pi_{0}(\mathcal{P}_{a})$ . — Dans ce paragraphe, nous allons décrire le groupe de composantes connexes de  $P_{a}$  dans l'esprit de la dualité de Tate-Nakayama. Pour cela, il est nécessaire de faire un certain nombre de choix et de fixer quelques notations.

Fixons un point $\infty\in\mathbf{X}(\bar{k})$. Considérons l'ouvert $\mathcal{A}^{\infty}$ de $\mathcal{A}\otimes_{k}\bar{k}$ qui consiste en les points $a\in\mathcal{A}(\bar{k})$ tels que $a(\infty)\in\bar{\mathfrak{c}}_{\mathrm{D}}^{\mathrm{rs}}$. C'est un sous-schéma ouvert de $\mathcal{A}^{\heartsuit}\otimes_{k}\bar{k}$. Si $\infty$ est défini sur $k$, l'ouvert $\mathcal{A}^{\infty}$ est aussi défini sur $k$.

Fixons un point $a \in \mathcal{A}^{\infty}(\bar{k})$. Notons U l'ouvert maximal de $\bar{\mathbf{X}}$ au-dessus duquel le revêtement caméral $\tilde{\mathbf{X}}_a \to \bar{\mathbf{X}}$ est étale. Par construction $\infty \in \mathbf{U}$. Supposons que G est défini par un homomorphisme continu

$$
\rho_ {\mathrm{G}} ^ {\bullet}: \pi_ {1} (\mathrm{X}, \infty) \to \operatorname{Out} (\mathbf {G}).
$$

Ayant choisi un point géométrique $\tilde{\infty}$ de la courbe camérale $\tilde{\mathbf{X}}_a$ au-dessus de $\infty$, on a comme dans 1.4.4 un homomorphisme continu $\pi_{\tilde{a}}^{\bullet}$ qui s'insère dans un diagramme commutatif

$$
\begin{array}{c} \pi_ {1} (\mathrm{U}, \infty) \xrightarrow {\pi_ {a} ^ {\bullet}} \mathbf {W} \rtimes \operatorname{Out} (\mathbf {G}) \\ \Bigg \downarrow \\ \pi_ {1} (\bar {\mathrm{X}}, \infty) \xrightarrow {\rho_ {\mathrm{G}} ^ {\bullet}} \operatorname{Out} (\mathbf {G}) \end{array}\tag{4.10.1}
$$

où $\tilde{a} = (a, \tilde{\infty})$. Notons $W_{\tilde{a}}$ l'image de $\pi_{\tilde{a}}^{\bullet}$ dans $\mathbf{W} \rtimes \operatorname{Out}(\mathbf{G})$ et $I_{\tilde{a}}$ l'image du noyau de $\pi_1(U, \infty) \to \pi_1(\bar{X}, \infty)$. La commutativité du diagramme ci-dessus implique $I_{\tilde{a}} \subset W$.

Soit maintenant  $J_{a}^{0}$  le sous-schéma en groupes des composantes neutres de  $J_{a}$ . Considérons le champ de Picard  $P_{a}^{\prime}$  des  $J_{a}^{0}$ -torseurs sur  $\bar{X}$ . L'homomorphisme de faisceaux  $J_{a}^{0} \to J_{a}$  induit un homomorphisme de champs de Picard  $P_{a}^{\prime} \to P_{a}$ .

Lemme 4.10.2. — L'homomorphisme $\mathcal{P}_{a}^{\prime}\to\mathcal{P}_{a}$ est surjectif et a un noyau fini. Il en est de même de l'homomorphisme $\pi_{0}(\mathcal{P}_{a}^{\prime})\to\pi_{0}(\mathcal{P}_{a})$ qui s'en déduit.

Démonstration. — On a une suite exacte courte de faisceaux

$$
0 \to \mathrm{J} _ {a} ^ {0} \to \mathrm{J} _ {a} \to \pi_ {0} (\mathrm{J} _ {a}) \to 0
$$

où $\pi_0(\mathrm{J}_a)$ est un faisceau de support fini dont la fibre en un point $v\in \bar{\mathbf{X}}$ est le groupe $\pi_0(\mathrm{J}_a)_v$ des composantes connexes de la fibre $\mathrm{J}_{a,v}$ de $\mathrm{J}_a$. On en déduit une suite exacte longue

$$
\mathrm{H} ^ {0} (\bar {\mathrm{X}}, \pi_ {0} (\mathrm{J} _ {a})) \rightarrow \mathrm{H} ^ {1} (\bar {\mathrm{X}}, \mathrm{J} _ {a} ^ {0}) \rightarrow \mathrm{H} ^ {1} (\bar {\mathrm{X}}, \mathrm{J} _ {a}) \rightarrow \mathrm{H} ^ {1} (\bar {\mathrm{X}}, \pi_ {0} (\mathrm{J} _ {a})) = 0.
$$

L'annulation du dernier terme résulte du fait que $\pi_0(\mathbf{J}_a)$ est supporté par un schéma de dimension zéro. On en déduit la surjectivité de $\mathcal{P}_a' \to \mathcal{P}_a$ de noyau $\mathrm{H}^0(\bar{\mathrm{X}}, \pi_0(\mathbf{J}_a))$. La

finitude de ce noyau vient de la finitude des fibres de $\pi_{0}(\mathrm{J}_{a})$. L'assertion sur $\pi_{0}(\mathcal{P}_{a}^{\prime}) \to \pi_{0}(\mathcal{P}_{a})$ s'ensuit immédiatement.

Au lieu des groupes abéliens $\pi_0(\mathcal{P}_a')$ et $\pi_0(\mathcal{P}_a)$, il sera plus commode de décrire les groupes diagonalisables duaux. Dualement, on a une inclusion des groupes diagonalisables

$$
\pi_ {0} (\mathcal {P} _ {a}) ^ {*} \subset \pi_ {0} (\mathcal {P} _ {a} ^ {\prime}) ^ {*}
$$

où on a noté

$$
\begin{array}{l} \pi_ {0} (\mathcal {P} _ {a}) ^ {*} = \mathrm{Spec} (\bar {\mathbf {Q}} _ {\ell} [ \pi_ {0} (\mathcal {P} _ {a}) ]) \\ \pi_ {0} (\mathcal {P} _ {a} ^ {\prime}) ^ {*} = \mathrm{Spec} (\bar {\mathbf {Q}} _ {\ell} [ \pi_ {0} (\mathcal {P} _ {a} ^ {\prime}) ]). \end{array}
$$

On a utilisé l'exposant $(\_)^{*}$ pour désigner la dualité entre les groupes abéliens de type fini et les groupes diagonalisables de type fini sur $\bar{\mathbf{Q}}_{\ell}$.

Proposition 4.10.3. — Pour tout $\tilde{a} = (a, \tilde{\infty})$ comme ci-dessus, on a des isomorphismes de groupes diagonalisables

$$
\pi_ {0} (\mathcal {P} _ {a} ^ {\prime}) ^ {*} = \hat {\mathbf {T}} ^ {\mathrm{W} _ {\tilde {a}}}
$$

et

$$
\pi_ {0} (\mathcal {P} _ {a}) ^ {*} = \hat {\mathbf {T}} (\mathrm{I} _ {\tilde {a}}, \mathrm{W} _ {\tilde {a}})
$$

où $\hat{\mathbf{T}}(\mathrm{I}_{\tilde{a}},\mathrm{W}_{\tilde{a}})$ est le sous-groupe de $\hat{\mathbf{T}}^{\mathrm{W}_{\tilde{a}}}$ formé des éléments $\kappa$ tels que $\mathrm{W}_{\tilde{a}}\subset (\mathbf{W}\rtimes \mathrm{Out}(\mathbf{G}))_{\kappa}$ et $\mathrm{I}_{\tilde{a}}\subset \mathbf{W}_{\mathbf{H}}$ où $\mathbf{W}_{\mathbf{H}}$ est le groupe de Weyl de la composante neutre du centralisateur de $\kappa$ dans $\hat{\mathbf{G}}$.

Démonstration. — D'après [57, corollaire 6.7], on a un isomorphisme canonique

$$
(\mathbf {X} _ {*}) _ {\mathrm{W} _ {\tilde {a}}} \longrightarrow \pi_ {0} (\mathcal {P} _ {a} ^ {\prime})
$$

du groupe des  $W_{\tilde{a}}$ -coinvariants de  $X_{*} = \text{Hom}(\mathbf{G}_{m}, \mathbf{T})$  dans le groupe des composantes connexes de  $P_{a}^{\prime}$ . Ceci est essentiellement un cas particulier d'un lemme de Kottwitz [42, lemme 2.2]. Dualement, on a un isomorphisme de groupes diagonalisables

$$
\pi_ {0} (\mathcal {P} _ {a} ^ {\prime}) ^ {*} = \hat {\mathbf {T}} ^ {W _ {\tilde {a}}}
$$

où $\hat{\mathbf{T}}$ est le $\bar{\mathbf{Q}}_{\ell}$-tore dual de $\mathbf{T}$.

Notons  $U = a^{-1}(\overline{\mathfrak{c}}_{\mathrm{D}}^{\mathrm{rs}})$ . Comme dans la démonstration de 4.10.2, on a une suite exacte

$$
\mathrm{H} ^ {0} (\bar {\mathrm{X}}, \pi_ {0} (\mathrm{J} _ {a})) \rightarrow \pi_ {0} (\mathcal {P} _ {a} ^ {\prime}) \rightarrow \pi_ {0} (\mathcal {P} _ {a}) \rightarrow 0
$$

où  $\mathrm{H}^{0}(\bar{\mathrm{X}},\mathrm{J}_{a}/\mathrm{J}_{a}^{0})=\bigoplus_{v\in\bar{\mathrm{X}}-\mathrm{U}}\pi_{0}(\mathrm{J}_{a,v})$  où  $\pi_{0}(\mathrm{J}_{a,v})$  désigne le groupe des composantes connexes de la fibre de  $J_{a}$  en v. Pour tout  $v\in\bar{X}-U$ , on a une suite exacte locale analogue

$$
\pi_ {0} (\mathrm{J} _ {a, v}) \to \pi_ {0} (\mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0})) \to \pi_ {0} (\mathcal {P} _ {v} (\mathrm{J} _ {a})) \to 0
$$

compatible avec la suite globale. Considérons les suites duales des groupes diagonalisables

$$
0 \to \pi_ {0} (\mathcal {P} _ {v} (\mathrm{J} _ {a})) ^ {*} \to \pi_ {0} (\mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0})) ^ {*} \to \pi_ {0} (\mathrm{J} _ {a, v}) ^ {*}.
$$

Le sous-groupe

$$
\pi_ {0} (\mathcal {P} _ {a}) ^ {*} \subset \pi_ {0} (\mathcal {P} _ {a} ^ {\prime}) ^ {*}
$$

est alors l'intersection des images inverses des sous-groupes

$$
\pi_ {0} (\mathcal {P} _ {v} (J _ {a})) ^ {*} \subset \pi_ {0} (\mathcal {P} _ {v} (J _ {a} ^ {0})) ^ {*}
$$

pour tout $v \in \bar{\mathbf{X}} - \mathbf{U}$. La proposition se déduit maintenant de 3.9.2.

Corollaire 4.10.4. — Pour $a \in \mathcal{A}^{\diamond}(\bar{k})$, on a $\pi_0(\mathcal{P}_a) = Z\hat{\mathbf{G}}^\ominus$.

Démonstration. — Pour $\tilde{a} = (a, \tilde{\infty})$ avec $a \in \mathcal{A}^{\diamond}(\bar{k})$, on a vu que $W_{\tilde{a}} = W \rtimes \Theta$ et $I_{\tilde{a}} = W$ cf. 4.7.5. Le corollaire résulte donc de 4.10.3.

4.10.5. — Soit  $\mathcal{A}^{\mathrm{ani}}(\bar{k})$  le sous-ensemble des  $a \in \mathcal{A}^{\heartsuit}(\bar{k})$  tels que  $\pi_{0}(\mathcal{P}_{a})$  est fini. D'après 4.10.3, ceci est équivalent à la finitude de  $\hat{T}^{W_{\tilde{a}}}$ . On démontrera dans 5.4.7 que  $\mathcal{A}^{\mathrm{ani}}(\bar{k})$  est l'ensemble des  $\bar{k}$ -points d'un ouvert  $A^{ani}$  de  $A^{\heartsuit}$ .

4.11. Automorphismes. — Soit  $(\mathrm{E},\phi)\in\mathcal{M}(\bar{k})$  d'image  $a\in\mathcal{A}^{\heartsuit}(\bar{k})$ . Nous allons déterminer des bornes pour le groupe des automorphismes  $\operatorname{Aut}(\mathrm{E},\phi)$  en fonction de a. Soit U l'ouvert de  $\bar{X}$  où a est semi-simple régulier.

Considérons le faisceau des automorphismes $\underline{\mathrm{Aut}}(\mathrm{E},\phi)$ qui associe à tout $\bar{\mathbf{X}}$-schéma S le groupe $\mathrm{Aut}((\mathrm{E},\phi)|_{\mathrm{S}})$. Ce faisceau est représentable par le schéma en groupes $\mathrm{I}_{(\mathrm{E},\phi)} = h_{(\mathrm{E},\phi)}^{*}\mathrm{I}$ qui est l'image réciproque du centralisateur I sur $\mathfrak{g}$ par la flèche $h_{(\mathrm{E},\phi)}:\bar{\mathbf{X}}\to [\mathfrak{g}_{\mathrm{D}} / \mathrm{G}]$. La restriction de $\mathrm{I}_{(\mathrm{E},\phi)}$ à l'ouvert U est un tore mais au-dessus de $\bar{\mathbf{X}}$, le schéma en groupes $\mathrm{I}_{(\mathrm{E},\phi)}$ n'est ni lisse ni même plat. On peut néanmoins considérer sa lissification au sens de [10]. D'après loc. cit., il existe un unique schéma en groupes lisse $\mathrm{I}_{(\mathrm{E},\phi)}^{\mathrm{lis}}$ au-dessus de $\bar{\mathbf{X}}$ tel que pour tout $\bar{\mathbf{X}}$-schéma S lisse on a

$$
\operatorname{Aut} ((\mathrm{E}, \phi) | _ {\mathrm{S}}) = \operatorname{Hom} _ {\mathrm{X}} (\mathrm{S}, \mathrm{I} _ {(\mathrm{E}, \phi)} ^ {\text { lis }}).
$$

La flèche tautologique  $\mathrm{I}_{(\mathrm{E},\phi)}^{\mathrm{lis}}\rightarrow\mathrm{I}_{(\mathrm{E},\phi)}$  est un isomorphisme au-dessus de l'ouvert U. Notons que la caractérisation de  $\mathrm{I}_{(\mathrm{E},\phi)}^{\mathrm{lis}}$  implique l'égalité

$$
\operatorname{Aut} (\mathrm{E}, \phi) = \mathrm{H} ^ {0} (\bar {\mathrm{X}}, \mathrm{I} _ {(\mathrm{E}, \phi)} ^ {\text { lis }}).\tag{4.11.1}
$$

Puisque  $J_{a}$  est lisse, l'homomorphisme canonique  $J_{a} \rightarrow I_{(E,\phi)}$  induit un homomorphisme

$$
\mathrm{J} _ {a} \rightarrow \mathrm{I} _ {(\mathrm{E}, \phi)} ^ {\mathrm{lis}}
$$

qui est un isomorphisme au-dessus de U. Par la propriété universelle du modèle de Néron, on a un homomorphisme

$$
\mathrm{I} _ {(\mathrm{E}, \phi)} ^ {\mathrm{lis}} \rightarrow \mathrm{J} _ {a} ^ {\flat}
$$

qui est un isomorphisme sur U.

Proposition 4.11.2. — Pour tout (E, $\phi$) $\in$$\mathcal{M}(\bar{k})$ au-dessus d'un point $a \in \mathcal{A}^{\heartsuit}(\bar{k})$, on a des inclusions canoniques

$$
\mathrm{H} ^ {0} (\bar {\mathrm{X}}, \mathrm{J} _ {a}) \subset \operatorname{Aut} (\mathrm{E}, \phi) \subset \mathrm{H} ^ {0} (\bar {\mathrm{X}}, \mathrm{J} _ {a} ^ {\flat}).
$$

Démonstration. — Il suffit de vérifier que les flèches  $J_{a} \to I_{(E,\phi)}^{\mathrm{lis}}$  et  $I_{(E,\phi)}^{\mathrm{lis}} \to J_{a}^{\flat}$  sont injectives en tant qu'homomorphisme de faisceaux pour la topologie étale. Pour cela, il suffit de vérifier l'injectivité sur les voisinages formels en chaque point  $v \in \bar{X} - U$ . Notons  $\bar{O}_{v}$  le complété formel de  $O_{\bar{X}}$  en v et  $F_{v}$  le corps des fractions de  $\bar{O}_{v}$ . On a alors les inclusions

$$
\mathrm{J} _ {a} (\bar {\mathcal {O}} _ {v}) \subset \mathrm{I} _ {(\mathrm{E}, \phi)} ^ {\mathrm{lis}} (\bar {\mathcal {O}} _ {v}) \subset \mathrm{J} _ {a} ^ {\flat} (\bar {\mathcal {O}} _ {v})
$$

de sous-groupes de $\mathrm{J}_a(\bar{\mathrm{F}}_v)$.

Reprenons les notations de 4.10. Fixons un couple $\tilde{a} = (a, \tilde{\infty})$ avec $a \in \mathcal{A}^{\infty}(\bar{k})$ et $\infty \in \tilde{\mathrm{X}}_a$ au-dessus de $\infty$. On y a défini un sous-groupe $\mathrm{W}_{\tilde{a}}$ de $\mathbf{W} \rtimes \operatorname{Out}(\mathbf{G})$. Avec 4.8.1 et 2.4.4, on a la formule

$$
\mathrm{H} ^ {0} (\bar {\mathrm{X}}, \mathrm{J} _ {a} ^ {\flat}) = \mathbf {T} ^ {\mathrm{W} _ {\tilde {a}}}.
$$

On en déduit le corollaire suivant.

Corollaire 4.11.3. — Soit $\tilde{a} = (a, \tilde{\infty})$ comme ci-dessus. Pour tout $(\mathrm{E}, \phi) \in \mathcal{M}(\bar{k})$ au-dessus d'un point $a \in \mathcal{A}^{\heartsuit}(\bar{k})$, $\operatorname{Aut}(\mathrm{E}, \phi)$ s'identifie à un sous-groupe de $\mathbf{T}^{\mathrm{W}_{\tilde{a}}}$.

Les travaux récents de Frenkel et Witten suggèrent que cette borne n'est pas optimale. En fait, on devrait avoir l'inclusion

$$
\operatorname{Aut} (\mathrm{E}, \phi) \subset \mathbf {T} (\mathrm{I} _ {\tilde {a}}, \mathrm{W} _ {\tilde {a}})
$$

où  $\mathbf{T}(\mathrm{I}_{\tilde{a}},\mathrm{W}_{\tilde{a}})$  est le sous-groupe de  $T^{W_{\tilde{a}}}$  défini comme dans 4.10.3 en remplaçant  $\hat{T}$  par T. De plus, l'égalité devrait être atteinte aux points les plus singuliers de la fibre  $M_{a}$ .

4.11.4. — Au-dessus de l'ouvert  $A^{ani}$  cf. 4.10.5, le groupe  $\hat{T}^{W_{\tilde{a}}}$  est fini. Il en est de même pour  $T^{W_{\tilde{a}}}$ . En supposant l'ordre de  $W \rtimes \Theta$  premier à la caractéristique  $T^{W_{\tilde{a}}}$  sera fini non ramifié. La restriction de M à  $A^{ani}$  est donc de Deligne-Mumford d'après le corollaire ci-dessus.

4.12. Module de Tate polarisable. — Mettons-nous sous l'hypothèse de 4.5.5 de sorte que P est un champ de Picard de Deligne-Mumford lisse au-dessus de  $A^{\heartsuit}$ . Notons  $P^{0}$  le sous-champ de Picard des composantes neutres de P. Notons g le morphisme structural  $P^{0} \to A^{\heartsuit}$  qui est lisse de dimension relative d. Considérons le module de Tate

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathcal {P} ^ {0}) = \mathrm{H} ^ {2 d - 1} (g _ {!} \bar {\mathbf {Q}} _ {\ell})
$$

qui est un $\bar{\mathbf{Q}}_{\ell}$-faisceau sur $\mathcal{A}^{\heartsuit}$.

La façon plus élémentaire de présenter ce faisceau consiste à utiliser des rigidificateurs. Comme dans 4.5.6, on a défini sur l'ouvert $\mathcal{A}^{\infty}$ des schémas en groupes lisses à fibres connexes $\mathrm{P}_{-1}$ et $\mathrm{P}_0$, $\mathrm{P}_{-1}$ étant affine tel qu'on a un suite exacte

$$
1 \to \mathrm{P} _ {- 1} \to \mathrm{P} _ {0} \to \mathcal {P} ^ {0} | _ {\mathcal {A}} \to 1.
$$

Il s'ensuit une suite exacte de $\bar{\mathbf{Q}}_{\ell}$-modules de Tate

$$
0 \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P} _ {- 1}) \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P} _ {0}) \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathcal {P} ^ {0} | _ {\mathcal {A}}) \to 0.
$$

Pour tout point géométrique $a \in \mathcal{A}^{\infty}(\bar{k})$, notons $\mathrm{A}_{a}$ le quotient abélien maximal de $\mathrm{P}_{0,a}$. Comme $\mathrm{P}_{-1,a}$ est affine, la flèche $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P}_{0,a}) \to \mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{a})$ se factorise par $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathcal{P}_{a}^{0})$. On en déduit une suite exacte

$$
0 \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{R} _ {a}) \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathcal {P} _ {a} ^ {0}) \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{A} _ {a}) \to 0
$$

qui ne dépend pas en fait du choix du rigidificateur. Bien qu'on ne dispose pas du dévissage canonique de Chevalley pour le champ de Picard Deligne-Mumford  $P_{a}^{0}$ , on dispose donc d'un dévissage canonique de son  $\bar{Q}_{\ell}$ -module de Tate.

Proposition 4.12.1. — Il existe une forme alternée

$$
\psi : \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathcal {P} ^ {\heartsuit}) \times \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathcal {P} ^ {\heartsuit}) \rightarrow \bar {\mathbf {Q}} _ {\ell} (- 1)
$$

telle qu'en chaque point géométrique $a \in \mathcal{A}^{\heartsuit}(\bar{k})$, la forme $\psi_{a}$ est nulle sur la partie affine $\mathrm{T}_{\tilde{\mathbf{Q}}_{\ell}}(\mathrm{R}_{a})$ et induit un accouplement parfait sur la partie abélienne $\mathrm{T}_{\tilde{\mathbf{Q}}_{\ell}}(\mathrm{A}_{a})$.

La démonstration de cette proposition est fondée sur la théorie de l'accouplement de Weil que nous allons rappeler pour la commodité du lecteur. Soit S un schéma local strictement hensélien. Soit  $c: C \rightarrow S$  un morphisme propre plat de fibres géométriquement réduites de dimension un.

Supposons que C est connexe. Considérons la factorisation de Stein  $C \rightarrow S' \rightarrow S$  où  $C \rightarrow S'$  est un morphisme propre de fibres connexes non vide et  $S' \rightarrow S$  est un morphisme fini. Puisque la fibre spéciale de c est réduite, le morphisme  $S' \rightarrow S$  est fini et étale. Puisque C est connexe,  $S'$  l'est aussi. Puisqu'on a supposé que S est strictement hensélien, on a alors  $S' = S$ . Autrement dit les fibres de  $c : C \rightarrow S$  sont connexes.

Considérons le S-champ d'Artin $\mathrm{Pic}_{\mathrm{C / S}}$ qui associe à tout S-schéma Y le groupoïde des fibrés inversibles sur $\mathrm{C} \times_{\mathrm{S}} \mathrm{Y}$. Il est lisse au-dessus de S. Considérons sa composante neutre $\mathrm{Pic}_{\mathrm{C / S}}^{0}$. Pour tout point $\mathrm{L} \in \mathrm{Pic}_{\mathrm{X / S}}(\mathrm{Y})$, pour tout $y \in \mathrm{Y}$, on peut définir la caractéristique d'Euler-Poincaré $\chi_y(\mathrm{L})$ de la restriction de $\mathrm{L} \dot{\alpha} \mathrm{C}_y$. Si Y est connexe, cet entier est indépendant de $y$ et nous le notons $\chi(\mathrm{L})$. Si $\mathrm{L} \in \mathrm{Pic}_{\mathrm{C / S}}^{0}$, on a $\chi(\mathrm{L}) = \chi(\mathcal{O}_{\mathrm{C}})$.

Pour tout couple de L,  $L' \in Pic_{C/S}^{0}$ , nous définissons leur accouplement de Weil par la formule

$$
\begin{array}{c} \langle \mathrm{L}, \mathrm{L} ^ {\prime} \rangle_ {\mathrm{C/S}} = \det (\mathrm{R} c _ {*} (\mathrm{L} \otimes \mathrm{L} ^ {\prime})) \otimes \det (\mathrm{R} c _ {*} \mathrm{L}) ^ {\otimes - 1} \\ \otimes \det (\mathrm{R} c _ {*} \mathrm{L} ^ {\prime}) ^ {\otimes - 1} \otimes \det (\mathrm{R} c _ {*} \mathcal {O} _ {\mathrm{C}}) \end{array}
$$

en utilisant le déterminant de cohomologie. Si t est un automorphisme de L qui est alors un scalaire, t agit sur  $\det(\mathrm{R}c_{*}\mathrm{L})$  par le scalaire  $t^{\chi(\mathrm{L})}$ . En utilisant les égalités

$$
\chi (\mathrm{L} \otimes \mathrm{L} ^ {\prime}) = \chi (\mathrm{L}) = \chi (\mathrm{L} ^ {\prime}) = \chi (\mathcal {O} _ {\mathrm{C}})
$$

pour L,  $L' \in \operatorname{Pic}_{X/S}^{0}$ , on vérifie que pour tout couple de scalaires  $(t, t')$  l'action de t sur L et l'action de  $t'$  sur  $L'$  induisent l'identité sur  $\langle L, L' \rangle_{C/S}$ .

Si N est un entier inversible sur S et L est un fibré inversible muni d'un isomorphisme $\iota_{\mathrm{L}}:\mathrm{L}^{\otimes \mathrm{N}}\to \mathcal{O}_{\mathrm{C}}$ , on a un isomorphisme

$$
\langle \mathrm{L}, \mathrm{L} ^ {\prime} \rangle_ {\mathrm{C/S}} ^ {\otimes \mathrm{N}} = \mathcal {O} _ {\mathrm{S}}.
$$

Si en plus L' est aussi muni d'un isomorphisme  $\iota_{L'} : L'^{\otimes N} \to O_{C}$ , on a un autre isomorphisme  $\langle L, L' \rangle_{C/S}^{\otimes N} = O_{S}$ . La différence de ces deux isomorphismes définit une racine Nième de l'unité. Cette racine ne dépend que des classes d'isomorphisme de L et de L' en vertu de la discussion sur l'effet des scalaires.

Supposons maintenant que C est une courbe projective connexe sur un corps algébriquement clos k. Le champ  $Pic_{C}^{0}$  est alors isomorphe au quotient d'un k-groupe algébrique commutatif connexe  $Jac_{C}$  par  $G_{m}$  agissant trivialement. La construction ci-dessus définit une forme alternée

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} \left(\operatorname{Jac} _ {\mathrm{C}}\right) \times \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} \left(\operatorname{Jac} _ {\mathrm{C}}\right) \longrightarrow \bar {\mathbf {Q}} _ {\ell} (- 1)
$$

qui est non-dégénérée lorsque C est lisse. Pour terminer cette digression, il reste à considérer le comportement de l'accouplement de Weil vis-à-vis de la normalisation.

Lemme 4.12.2. — Soit C une courbe projective réduite sur un corps algébriquement clos k. Soit $\mathbf{C}^{\flat}$ sa normalisation et $\xi : \mathbf{C}^{\flat} \to \mathbf{C}$ le morphisme de normalisation. Soient L, L' deux fibrés inversibles sur C. On a alors un isomorphisme canonique de k-espaces vectoriels de dimension un

$$
\langle \mathrm{L}, \mathrm{L} ^ {\prime} \rangle_ {\mathrm{C}} = \left\langle \xi^ {*} \mathrm{L}, \xi^ {*} \mathrm{L} ^ {\prime} \right\rangle_ {\mathrm{C} ^ {\flat}}.
$$

Démonstration. — On a une suite exacte

$$
0 \longrightarrow \mathcal {O} _ {\mathrm{C}} \longrightarrow \xi_ {*} \mathcal {O} _ {\mathrm{C} ^ {\flat}} \longrightarrow \mathcal {D} \longrightarrow 0
$$

où $\mathcal{D}$ est un $\mathcal{O}_{\mathrm{C}}$-modules fini supporté par une collection finie de points $\{c_{1},\ldots,c_{n}\}$ de C. Notons $\mathcal{D}_{i}$ le facteur direct de $\mathcal{D}$ supporté par $c_{i}$ et $d_{i}$ sa longueur. La multiplicativité du déterminant nous fournit alors un isomorphisme

$$
\det (c _ {*} ^ {\flat} \mathcal {O} _ {\mathrm{C} ^ {\flat}}) = \det (c _ {*} \xi_ {*} \mathcal {O} _ {\mathrm{C} ^ {\flat}}) = \det (c _ {*} \mathcal {O} _ {\mathrm{C}}) \otimes \bigotimes_ {i = 1} ^ {r} \wedge^ {d _ {i}} \mathcal {D} _ {i}
$$

où on a noté $c: \mathrm{C} \to \operatorname{Spec}(k)$ et $c^{\flat}: \mathrm{C}^{\flat} \to \operatorname{Spec}(k)$ les morphismes structuraux.

Soit L un fibré inversible sur C. En utilisant la formule de projection $\xi_{*}\xi^{*}\mathrm{L} = (\xi_{*}\mathcal{O})\otimes \mathrm{L}$, on obtient la formule

$$
\det (c _ {*} ^ {\flat} \xi^ {*} \mathrm{L}) = \det (c _ {*} \mathrm{L}) \otimes \bigotimes_ {i = 1} ^ {r} (\mathrm{L} _ {c _ {i}} ^ {\otimes d _ {i}} \otimes \wedge^ {d _ {i}} \mathcal {D} _ {i})
$$

où  $L_{c_{i}}$  est la fibre de L en  $c_{i}$ . En appliquant cette formule à  $L \otimes L'$ , L et à  $L'$ , on obtient le lemme.

On est maintenant en mesure de démontrer la proposition 4.12.1.

Démonstration. — Rappelons que pour tout point $a \in \mathcal{A}^{\heartsuit}$, $\mathcal{P}_{a}$ est le champ de Picard des $J_{a}$-torseurs sur X. Soit $\pi_{a}: \tilde{\mathrm{X}}_{a} \to \mathrm{X}$ le revêtement caméral associé à $a$. D'après la description galoisienne du centralisateur régulier, on a un homomorphisme de faisceaux en groupes cf. 2.4.2

$$
\mathrm{J} _ {a} \rightarrow \pi_ {a, *} (\mathrm{T} \times_ {\mathrm{X}} \tilde {\mathrm{X}} _ {a})
$$

où T est le tore maximal de G dans l'épinglage fixé. En considérant un déploiement  $X_{\rho} \rightarrow X$  de G, on obtient un revêtement fini étale  $\tilde{X}_{\rho,a} \rightarrow \tilde{X}_{a}$  par changement de base. Notons  $\pi_{\rho,a}: \tilde{X}_{\rho,a} \rightarrow X$  le morphisme composé. On a donc un homomorphisme

$$
\mathbf {J} _ {a} \rightarrow \pi_ {\rho , a, *} (\mathbf {T} \times \tilde {\mathbf {X}} _ {\rho , a})
$$

où $\mathbf{T}$ est un tore déployé. La donnée d'un point de $\ell^n$-torsion de $\mathcal{P}_a$ induit donc un point de $\ell^n$-torsion de $\mathrm{Pic}_{\tilde{\mathbf{X}}_{\rho,a}} \otimes \mathbf{X}_*(\mathbf{T})$. En choisissant une forme symétrique invariante

sur  $\mathbf{X}_{*}(\mathbf{T})\otimes\bar{\mathbf{Q}}_{\ell}$  et en utilisant l'accouplement de Weil sur  $Pic_{\tilde{X}_{\rho,a}}^{0}$ , on obtient une forme alternée

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} \left(\mathcal {P} _ {a} ^ {0}\right) \otimes \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} \left(\mathcal {P} _ {a} ^ {0}\right) \longrightarrow \bar {\mathbf {Q}} _ {\ell} (- 1).
$$

Il reste à démontrer qu'en chaque point géométrique $a$, cette forme symplectique est nulle sur la partie affine de $\mathrm{T}_{\ell}(\mathcal{P}_{a})$ et induit un accouplement non dégénéré sur sa partie abélienne. Ceci se déduit du lemme 4.12.2.

4.13. Dimensions. — Nous allons utiliser la même notation  $c_{D}$  pour désigner le X-schéma en vectoriels et le  $O_{X}$ -module localement libre. Si G est déployé, le  $O_{X}$ -module  $c_{D}$  a une expression explicite

$$
\mathfrak {c} _ {\mathrm{D}} = \bigoplus_ {i = 1} ^ {r} \mathrm{D} ^ {\otimes e _ {i}}
$$

où $e_1, \ldots, e_r$ sont des entiers naturels qui apparaissent dans 1.2. Par définition, le X-schéma en vectoriel $\mathfrak{c}_{\mathrm{D}}$ est

$$
\mathfrak {c} _ {\mathrm{D}} = \mathrm{Spec} (\mathrm{Sym} _ {\mathcal {O} _ {\mathrm{X}}} (\mathfrak {c} _ {\mathrm{D}} ^ {*}))
$$

où  $Sym_{\mathcal{O}_{X}}[\mathfrak{c}_{D}^{*}]$  est le faisceau en  $O_{X}$ -algèbre puissance symétrique du  $O_{X}$ -module dual  $c_{D}^{*}$ . En général,  $c_{D}$  prend cette forme après un changement de base fini étale galoisien  $\rho:X_{\rho}\to X$  qui déploie G.

Lemme 4.13.1. — Si deg(D) > 2g - 2, A est un k-espace affine de dimension

$$
\dim (\mathcal {A}) = \sharp \Phi \deg (D) / 2 + r (1 - g + \deg (D))
$$

où r est le rang de G et  $\sharp\Phi$  est le nombre de ses racines.

Démonstration. — Soit $\rho : \mathrm{X}_{\rho} \to \mathrm{X}$ le revêtement fini étale galoisien qui déploie G. Alors $\rho^{*}\mathfrak{c}_{\mathrm{D}}$ est isomorphe à une somme directe $\rho^{*}\mathrm{D}^{\otimes e_{i}}$. Il s'ensuit que

$$
\deg (\mathfrak {c} _ {\mathrm{D}}) = (e _ {1} + \dots + e _ {r}) \deg (\mathrm{D}).
$$

On a l'égalité

$$
\dim \mathrm{H} ^ {0} (\mathrm{X}, \mathfrak {c} _ {\mathrm{D}}) - \dim \mathrm{H} ^ {1} (\mathrm{X}, \mathfrak {c} _ {\mathrm{D}}) = (e _ {1} + \dots + e _ {r}) \deg (\mathrm{D}) + r (1 - g)
$$

par le théorème de Riemann-Roch. On sait d'après Kostant que les entiers $e_i - 1$ sont les exposants du système de racines $\Phi$ de sorte que

$$
e _ {1} + \dots + e _ {r} = r + \sharp \Phi / 2.
$$

Il suffit donc de démontrer que  $\mathrm{H}^{1}(\mathrm{X},\mathfrak{c}_{\mathrm{D}})=0$ . Puisque  $\deg(\mathrm{D})>2g-2$  et puisque  $\rho$  est fini étale, on a

$$
\deg (\rho^ {*} \mathrm{D}) > \deg (\rho^ {*} \Omega_ {\mathrm{X} / k}) = \deg (\Omega_ {\mathrm{X} _ {\rho / k}})
$$

d'où résulte l'annulation de  $\mathrm{H}^{1}(\mathrm{X}_{\rho}, \rho^{*}\mathrm{D}^{\otimes e_{i}})$ . Pour démontrer l'annulation de  $\mathrm{H}^{1}(\mathrm{X}, \mathfrak{c}_{\mathrm{D}})$ , il suffit de remarquer que  $\mathrm{H}^{1}(\mathrm{X}, \mathfrak{c}_{\mathrm{D}})$  est un facteur direct de  $\mathrm{H}^{1}(\mathrm{X}_{\rho}, \rho^{*}\mathfrak{c}_{\mathrm{D}})$ . □

Si deg(D) est un entier fixé plus grand que 2g - 2, la dimension de la base de Hitchin A ne dépend donc ni de D ni de la forme quasi-déployée.

Proposition 4.13.2. — Pour tout $a \in \mathcal{A}(\bar{k})$, on a un isomorphisme canonique $\operatorname{Lie}(\mathrm{J}_a) = \mathfrak{c}_{\mathrm{D}}^* \otimes \mathrm{D}$.

Dans la démonstration qui suit lorsque  $f: X \to Y$  et si L est un  $O_{Y}$ -module, on écrira simplement L pour désigner aussi son image inverse  $f^{*}L$ . Cet abus de notation ne devrait pas causer de confusion car le schéma qui porte le module sera toujours clair par le contexte.

Démonstration. — D'après 2.4.7, l'homomorphisme  $J_{a} \to J_{a}^{1}$  induit un isomorphisme  $\operatorname{Lie}(J_{a}) \to \operatorname{Lie}(J_{a}^{1})$  sur les algèbres de Lie. Par construction de  $J^{1}$ ,  $\operatorname{Lie}(J_{a}^{1})$  peut se calculer à l'aide du revêtement caméral  $\pi_{a}: \tilde{X}_{a} \to \bar{X}$  par la formule

$$
\operatorname{Lie} \left(\mathrm{J} _ {a} ^ {1}\right) = \left(\left(\pi_ {a}\right) _ {*} \mathbf {t}\right) ^ {\mathrm{W}}.
$$

Rappelons que le revêtement caméral est défini en formant le diagramme cartésien :

$$
\begin{array}{c} \tilde {\mathbf {X}} _ {a} \longrightarrow \mathfrak {t} _ {\mathrm{D}} \\ \pi_ {a} \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \pi \\ \bar {\mathbf {X}} \xrightarrow [ a ]{} \mathfrak {c} _ {\mathrm{D}} \end{array}
$$

Puisque $\pi$ est fini et plat, la formation de $\pi_{*}\mathfrak{t}$ commute à tout changement de base en particulier $(\pi_{a})_{*}\mathfrak{t}=a^{*}\pi_{*}\mathfrak{t}$. Il suffit donc de calculer $(\pi_{*}\mathfrak{t})^{\mathrm{W}}$.

Puisque  $c_{D}$  est le quotient invariant de  $t_{D}$  par l'action de W, il en est de même pour les espaces totaux des fibrés tangents  $T_{t_{D}/X}$  et  $T_{c_{D}/X}$ . On en déduit

$$
(\pi_ {*} \Omega_ {\mathfrak {t} _ {\mathrm{D}} / \mathrm{X}}) ^ {\mathrm{W}} = \Omega_ {\mathfrak {c} _ {\mathrm{D}} / \mathrm{X}}.
$$

Par ailleurs, comme  $t_{D}$  est un fibré vectoriel sur X, on a  $\Omega_{t_{D}/X} = t_{D^{-1}}$ . De même, on a  $\Omega_{c_{D}/X} = c_{D}^{*}$ . On obtient finalement une égalité de  $O_{c_{D}}$ -modules  $(\pi_{*}t_{D^{-1}})^{W} = c_{D}^{*}$  d'où

$$
(\pi_ {*} t) ^ {W} = \mathfrak {c} _ {D} ^ {*} \otimes D.
$$

En prenant l'image inverse de cette égalité par la section  $a: \bar{X} \to c_{D}$ , on obtient l'égalité  $\text{Lie}(J_a) = c_{D}^* \otimes_{\mathcal{O}_X} D$ .

Dans le cas où G est déployé, le lemme permet d'exprimer  $\operatorname{Lie}(\mathbf{J}_{a})$  en termes de D et des exposants du système de racines  $\Phi$ . Soient  $e_{1},\ldots,e_{r}$  les degrés des polynômes invariants homogènes comme dans l'énoncé de 1.1.1, on a

$$
\operatorname{Lie} \left(\mathrm{J} _ {a}\right) = \mathrm{D} ^ {- e _ {1} + 1} \oplus \dots \oplus \mathrm{D} ^ {- e _ {r} + 1}.
$$

Si G n'est pas déployé, Lie(J$_{a}$) devient isomorphe à la somme directe de droite sur un revêtement fini étale galoisien de X qui déploie G. En particulier

$$
\deg (\operatorname{Lie} \left(\mathrm{J} _ {a}\right)) = \sum_ {i = 1} ^ {r} \left(- e _ {r} + 1\right) \deg (\mathrm{D}) = - \sharp \Phi \deg (\mathrm{D}) / 2.
$$

Corollaire 4.13.3. — Pour tout $a \in \mathcal{A}^{\heartsuit}(\bar{k})$,

$$
\dim (\mathcal {P} _ {a}) = \sharp \Phi \deg (D) / 2 + r (g - 1).
$$

Démonstration. — On a

$$
\dim (\mathcal {P} _ {a}) = \dim (\mathrm{H} ^ {1} (\bar {\mathrm{X}}, \operatorname{Lie} (\mathrm{J} _ {a}))) - \dim (\mathrm{H} ^ {0} (\bar {\mathrm{X}}, \operatorname{Lie} (\mathrm{J} _ {a})))
$$

de sorte que l'égalité à démontrer résulte de la formule de Riemann-Roch.

4.13.4. — On notera $d = \sharp \Phi \deg(\mathrm{D}) / 2 + r(g - 1)$ la dimension relative de $\mathcal{P}$ au-dessus de $\mathcal{A}$. En comparant avec la formule 4.13.1, on obtient

$$
\dim (\mathcal {P}) = (r + \sharp \Phi) \deg (\mathrm{D}).
$$

Dans 4.16.1, on démontrera que $\mathcal{M}_a^{\mathrm{reg}}$ est dense dans $\mathcal{M}_a$ de sorte qu'on aura alors les mêmes formules de dimension pour $\mathcal{M}$. En particulier $\dim(\mathcal{M}_a) = d$ et $\dim(\mathcal{M}) = (r + \sharp \Phi)\deg(\mathrm{D})$.

4.14. Calcul de déformation. — Les déformations des fibrés de Higgs ont été étudiées par Biswas et Ramanan dans [9]. Pour la commodité du lecteur, nous allons reprendre leur calcul.

Rappelons d'abord le calcul usuel des déformations d'un torseur sous un groupe lisse. Soient S un k-schéma et G un S-schéma en groupes lisse. Soit BG le classifiant de G. Le G-torseur universel EG est alors S au-dessus de [S/G]. Notons

$$
\pi_ {\mathbf {E G}}: \mathbf {E G} \longrightarrow \mathbf {B G}
$$

le G-torseur tautologique. Considérons le triangle distingué des complexes cotangents

$$
\pi_ {\mathbf {E G}} ^ {*} \mathrm{L} _ {\mathbf {B G} / \mathrm{S}} \longrightarrow \mathrm{L} _ {\mathbf {E G} / \mathrm{S}} \longrightarrow \mathrm{L} _ {\mathbf {E G} / \mathbf {B G}} \longrightarrow \pi_ {\mathbf {E G}} ^ {*} \mathrm{L} _ {\mathbf {B G} / \mathbf {S}} [ 1 ].
$$

Puisque S = EG, le complexe cotangent  $L_{EG/S}$  est nul alors que  $L_{EG/BG}$  est le fibré vectoriel  $g^{*}$  placé en degré 0. Il en résulte un isomorphisme

$$
\mathrm{L} _ {\mathbf {E G / B G}} \stackrel {\sim} {\to} \pi_ {\mathbf {E G}} ^ {*} \mathrm{L} _ {\mathbf {B G / S}} [ 1 ].
$$

On en déduit un isomorphisme

$$
\mathfrak {g} ^ {*} [ - 1 ] \stackrel {\sim} {\to} \pi_ {\mathbf {E G}} ^ {*} \mathrm{L} _ {\mathbf {B G / S}}
$$

qui par descente le long de  $\pi_{EG}$  induit un isomorphisme

$$
(\mathbf {E G} \wedge^ {\mathrm{G}} \mathfrak {g} ^ {*}) [ - 1 ] \stackrel {\sim} {\to} \mathrm{L} _ {\mathbf {B G / S}}.
$$

Le complexe cotangent  $L_{BG/k}$  du classifiant de G est donc le fibré vectoriel obtenu en tordant par le torseur EG l'espace vectoriel  $g^{*}$  muni de la représentation coadjointe, placé en degré 1.

Ainsi, pour tout S-schéma X, pour tout G-torseur E sur X correspondant à une flèche  $h_{E}: X \rightarrow BG$ , l'obstruction à la déformation de E gît dans le groupe

$$
\mathrm{H} ^ {1} (\mathrm{X}, \underline {{\mathrm{RHom}}} (h _ {\mathrm{E}} ^ {*} \mathrm{L} _ {\mathbf {B G / S}}, \mathcal {O} _ {\mathrm{X}})) = \mathrm{H} ^ {2} (\mathrm{X}, \mathrm{E} \wedge^ {\mathrm{G}} \mathfrak {g})
$$

et si cette obstruction s'annule, les déformations forment un espace principal homogène sous le groupe

$$
\mathrm{H} ^ {0} (\mathrm{X}, \underline {{\mathrm{RHom}}} (h _ {\mathrm{E}} ^ {*} \mathrm{L} _ {\mathbf {B G / S}}, \mathcal {O} _ {\mathrm{X}})) = \mathrm{H} ^ {1} (\mathrm{X}, \mathrm{E} \wedge^ {\mathrm{G}} \mathfrak {g})
$$

alors que le groupe des automorphismes infinitésimaux est  $H^{0}(X, E \wedge^{G} \mathfrak{g})$ .

Soit maintenant V un fibré vectoriel sur S muni d'une action de G et considérons le champ quotient [V/G]. Le G-torseur  $\pi_{V}: V \rightarrow [V/G]$  définit un morphisme  $[\nu]: [V/G] \rightarrow BG$  qui s'insère dans un diagramme cartésien :

$$
\begin{array}{c} \mathrm{V} \xrightarrow {\nu} \mathbf {E G} \\ \pi_ {\mathrm{V}} \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow \pi_ {\mathbf {E G}} \\ [ \mathrm{V} / \mathrm{G} ] \xrightarrow {[ \nu ]} \mathbf {B G} \end{array}
$$

Considérons le triangle distingué des complexes cotangents

$$
\pi_ {\mathrm{V}} ^ {*} \mathrm{L} _ {[ \mathrm{V} / \mathrm{G} ] / \mathrm{S}} \longrightarrow \mathrm{L} _ {\mathrm{V} / \mathrm{S}} \longrightarrow \mathrm{L} _ {\mathrm{V} / [ \mathrm{V} / \mathrm{G} ]} \longrightarrow \pi_ {\mathrm{V}} ^ {*} \mathrm{L} _ {[ \mathrm{V} / \mathrm{G} ] / k} [ 1 ].
$$

Le terme  $L_{V/S}$  est le fibré vectoriel constant de valeur  $v^{*}V^{*}$  placé en degré 0 où  $V^{*}$  est le S-fibré vectoriel dual de V et  $v: V \to S$  est la projection sur S. Le terme  $L_{V/[V/G]}$  se calcule par changement de base  $L_{V/[V/G]} = v^{*}L_{EG/BG}$  et est donc le fibré vectoriel  $v^{*}g^{*}$  placé aussi en degré 0. Au-dessus de chaque point  $v \in V$ , l'action de G au voisinage de v définit une application linéaire

$$
\alpha_ {v}: \mathfrak {g} \longrightarrow \mathrm{T} _ {v} \mathrm{V} = \mathrm{V}
$$

dont le dual est la fibre en v

$$
\alpha_ {v} ^ {*}: (\mathrm{L} _ {\mathrm{V/S}}) _ {v} = \mathrm{V} ^ {*} \longrightarrow (\mathrm{L} _ {\mathrm{V/[V/G]}}) _ {v} = \mathfrak {g} ^ {*}
$$

de la flèche  $L_{V/k} \rightarrow L_{V/[V/G]}$  du triangle distingué. Cette flèche descend à [V/G] en une flèche

$$
\alpha_ {v} ^ {*} \wedge^ {\mathrm{G}} \pi_ {\mathrm{V}}: \pi_ {\mathrm{V}} \wedge^ {\mathrm{G}} \mathrm{V} ^ {*} \longrightarrow \pi_ {\mathrm{V}} \wedge^ {\mathrm{G}} \mathfrak {g} ^ {*}
$$

dont le cône est isomorphe à  $L_{[V/G]/S}$ .

Appliquons le calcul ci-dessus pour calculer les déformations des paires de Hitchin. Reprenons les notations fixées au début du chapitre 3. En particulier, G est le schéma en groupes réductif sur la courbe X et g son algèbre de Lie qui est munie de l'action adjointe de G et de l'action de  $G_{m}$  par homothétie. Le fibré inversible D définit un  $G_{m}$  torseur  $L_{D}$ . Considérons le champ  $[g_{D}/G]$  obtenu en tordant g par  $L_{D}$  puis divisé par G. Le complexe cotangent  $L_{[g_{D}/G]/X}$  s'identifie donc à

$$
\mathrm{L} _ {[ \mathfrak {g} / \mathrm{G} ] / \mathrm{X}} \wedge^ {\mathbf {G} _ {m}} \mathrm{L} _ {\mathrm{D}}
$$

qui est le cône de

$$
(\pi_ {\mathrm{D}, \mathfrak {g}} \wedge^ {\mathrm{G}} \mathfrak {g} ^ {*}) \otimes \mathrm{D} ^ {- 1} \longrightarrow \pi_ {\mathrm{D}, \mathfrak {g}} \wedge^ {\mathrm{G}} \mathfrak {g} ^ {*}
$$

où $\pi_{\mathrm{D},\mathfrak{g}}$ est le G-torseur évident sur le quotient $[\mathfrak{g}_{\mathrm{D}} / \mathrm{G}]$.

Soit (E, $\phi$) un champ de Higgs sur X à valeur dans $\bar{k}$. Elle correspond à une flèche

$$
h _ {\mathrm{E}, \phi}: \bar {\mathrm{X}} \to [ \mathfrak {g} _ {\mathrm{D}} / \mathrm{G} ].
$$

La déformation de (E,  $\phi$ ) est contrôlée par le complexe

$$
\underline {{\mathrm{RHom}}} (h _ {\mathrm{E}, \phi} ^ {*} (\mathrm{L} _ {\mathrm{D}} \wedge^ {\mathbf {G} _ {m}} \mathrm{L} _ {[ \mathfrak {g} / \mathrm{G} ] / \mathrm{X}}), \mathcal {O} _ {\mathrm{X}})
$$

qui s'exprime maintenant simplement

$$
\operatorname{ad} (\mathrm{E}, \phi) := [ \operatorname{ad} (\mathrm{E}) \to \operatorname{ad} (\mathrm{E}) \otimes \mathrm{D} ]
$$

où

\- ad(E) est le fibré vectoriel $\mathfrak{g} \wedge^{\mathrm{G}} \mathrm{E}$;

\- ad(E) est placé en degré -1 et ad(E) ⊗ D est placé en degré 0 ;

\- la flèche est donnée par $x \mapsto [x, \phi]$.

Rappelons la proposition 5.3 de [57]. Le lecteur notera une différence dans le décalage de ad(E, $\phi$) par rapport à loc. cit. Nous donnerons ici une démonstration un peu différente.

Théorème 4.14.1. — Soit (E, $\phi$) $\in$$\mathcal{M}(\bar{k})$ un point au-dessus d'un point $a \in \mathcal{A}^{\heartsuit}(\bar{k})$. Alors le groupe H$^{1}$(X, ad(E, $\phi$)) où gît l'obstruction à la déformation de la paire (E, $\phi$) est nul dans l'un des cas suivants

$$
\begin{array}{l} - \deg (\mathrm{D}) > 2 g - 2, \\ - \deg (\mathrm{D}) = 2 g - 2 e t a \in \mathcal {A} ^ {\mathrm{ani}} (\bar {k}). \end{array}
$$

Si l'une de ces deux hypothèses est satisfaite, M est lisse au point (E,  $\phi$ ).

Démonstration. — Fixons une forme symétrique non dégénérée et invariante sur g. On identifie alors le dual du complexe ad(E,  $\phi$ ) à

$$
\operatorname{ad} (\mathrm{E}, \phi) ^ {*} = [ \operatorname{ad} (\mathrm{E}) \otimes \mathrm{D} ^ {- 1} \rightarrow \operatorname{ad} (\mathrm{E}) ]
$$

dont les deux termes non nuls sont placés en degrés -1 et 0 et dont la différentielle est donnée par $x \mapsto [x, \phi]$. Le faisceau de cohomologie $\mathrm{H}^{-1}$ de ce complexe s'identifie à

$$
\operatorname{Lie} \left(\mathrm{I} _ {\mathrm{E}, \phi} ^ {\text {lis}}\right) \otimes \mathrm{D} ^ {- 1}
$$

où  $I_{E,\phi}^{lis}$  est le schéma en groupes lisse sur  $\bar{X}$  introduit dans le paragraphe 4.11. Par dualité de Serre, le groupe  $\mathrm{H}^{1}(\mathrm{X},\mathrm{ad}(\mathrm{E},\phi))$  est dual du groupe

$$
\mathrm{H} ^ {0} (\bar {\mathrm{X}}, \operatorname{Lie} \left(\mathrm{I} _ {\mathrm{E}, \phi} ^ {\text { lis }}\right) \otimes \mathrm{D} ^ {- 1} \otimes \Omega_ {\mathrm{X} / k}).
$$

Comme dans 4.11, on a un homomorphisme injectif de $\mathcal{O}_{\bar{\mathrm{X}}}$-modules

$$
\operatorname{Lie} \left(\mathrm{I} _ {\mathrm{E}, \phi} ^ {\text {lis}}\right)\rightarrow \operatorname{Lie} \left(\mathrm{J} _ {a} ^ {\flat}\right)
$$

de sorte que pour démontrer la nullité du groupe des obstructions envisagée, il suffit de démontrer que

$$
\mathrm{H} ^ {0} (\bar {\mathrm{X}}, \operatorname{Lie} (\mathrm{J} _ {a} ^ {\flat}) \otimes \mathrm{D} ^ {- 1} \otimes \Omega_ {\mathrm{X} / k}) = 0.
$$

On est donc amené à démontrer le lemme suivant.

Lemme 4.14.2. — Pour tout $a \in \mathcal{A}^{\heartsuit}(\bar{k})$, $\mathrm{H}^{0}(\bar{\mathrm{X}}, \operatorname{Lie}(\mathrm{J}_{a}^{\mathrm{b}}) \otimes \mathrm{L}) = 0$ pour tout fibré en droite L de degré strictement négatif. La même conclusion vaut sous l'hypothèse $a \in \mathcal{A}^{\mathrm{ani}}(\bar{k})$ et $\deg(\mathrm{L}) \leq 0$.

Démonstration. — Choisissons des pointages comme dans 4.10 et notons $\Theta$ l'image de $p_1(\bar{\mathbf{X}},\infty)$ dans $\operatorname{Out}(\mathbf{G})$. On a alors un revêtement fini étale galoisien connexe $\rho : \bar{\mathbf{X}}_{\rho}\to \bar{\mathbf{X}}$ de groupe de Galois $\Theta_{\rho} = \Theta$ qui déploie $\rho_{\mathrm{G}}$. On a alors un revêtement fini plat $\tilde{\mathbf{X}}_{\rho,a}\to \bar{\mathbf{X}}$ cf. 4.5.4 qui est génériquement étale galoisien de groupe de Galois $\mathbf{W}\rtimes \Theta_{\rho}$. Notons $\tilde{\mathbf{X}}_{\rho,a}^{\flat}$ la normalisation de $\tilde{\mathbf{X}}_{\rho,a}$ et $\pi_{\rho,a}^{\flat}$ la projection $\tilde{\mathbf{X}}_{\rho,a}^{\flat}\to \bar{\mathbf{X}}$. D'après 4.8.1, $\operatorname{Lie}(\mathbf{J}_a^\flat)$ peut être calculé à partir de $\tilde{\mathbf{X}}_{\rho,a}^{\flat}$ avec la formule

$$
\operatorname{Lie} \left(\mathrm{J} _ {a} ^ {\flat}\right) = \left(\pi_ {\rho , a} ^ {\flat}\right) _ {*} \left(\mathcal {O} _ {\tilde {\mathrm{X}} _ {\rho , a} ^ {\flat}} \otimes \mathbf {t}\right) ^ {\mathbf {W} \rtimes \Theta_ {\rho}}
$$

de sorte que

$$
\operatorname{Lie} \left(\mathrm{J} _ {a} ^ {\flat}\right) \otimes \mathrm{L} = \left(\pi_ {a} ^ {\flat}\right) _ {*} \left(\left(\pi_ {a} ^ {\flat}\right) ^ {*} \mathrm{L} \otimes \mathbf {t}\right) ^ {\mathbf {W} \rtimes \Theta_ {\rho}}.
$$

Si $\deg(\mathrm{L}) < 0$, $(\pi_{a}^{\flat})^{*}\mathrm{L}$ est un fibré en droites de degré strictement négatif sur chaque composante connexe de $\tilde{\mathrm{X}}_{\rho,a}^{\flat}$ et ne peut pas avoir de sections globales non nulles.

Si $\deg(\mathrm{L}) = 0$, $(\pi_{a}^{\flat})^{*}\mathrm{L}$ a des sections globales non nulles si et seulement s'il est isomorphe à $\mathcal{O}_{\tilde{\mathrm{X}}_{o,a}^{\flat}}$. On a dans ce cas

$$
\mathrm{H} ^ {0} (\tilde {\mathrm{X}} _ {\rho , a} ^ {\flat}, ((\pi_ {\rho , a} ^ {\flat}) ^ {*} \mathrm{L} \otimes \mathbf {t}) ^ {\mathbf {W} \rtimes \Theta_ {\rho}}) = \mathbf {t} ^ {\mathrm{W} _ {\tilde {a}}}
$$

où  $W_{\tilde{a}}$  est le sous-groupe de  $W \rtimes \Theta_{\rho}$  et donc de  $\mathbf{W} \rtimes \operatorname{Out}(\mathbf{G})$  défini comme dans le paragraphe 4.10. Sous l'hypothèse  $a \in \mathcal{A}^{\mathrm{ani}}(\bar{k})$ , le groupe des  $W_{\tilde{a}}$ -invariants  $t^{W_{\tilde{a}}}$  est nul cf. 4.10.5.

4.15. Formule de produit. — Nous allons à présent rappeler le lien entre les fibres de Hitchin et les fibres de Springer affines qui en sont des analogues locaux.

Soit $a \in \mathcal{A}^{\heartsuit}(\bar{k})$. Soit U l'image réciproque de l'ouvert régulier semi-simple $\mathfrak{c}^{\mathrm{rs}}$ de $\mathfrak{c}$ par le morphisme $a: \bar{\mathbf{X}} \to [\mathfrak{c}/\mathbf{G}_m]$. Le recollement avec la section de Kostant définit un morphisme

$$
\prod_ {v \in \bar {\mathrm{X}} - \mathrm{U}} \mathcal {M} _ {v} (a) \to \mathcal {M} _ {a}.
$$

De même, on a un homomorphisme de groupes $\prod_{v\in\bar{\mathrm{X}}-\mathrm{U}}\mathcal{P}_{v}(\mathrm{J}_{a})\longrightarrow\mathcal{P}_{a}$. Ceux-ci induisent un morphisme

$$
\zeta : \prod_ {v \in \bar {\mathrm{X}} - \mathrm{U}} \mathcal {M} _ {v} (a) \wedge^ {\prod_ {v \in \bar {\mathrm{X}} - \mathrm{U}} \mathcal {P} _ {v} (\mathrm{J} _ {a})} \mathcal {P} _ {a} \longrightarrow \mathcal {M} _ {a}.
$$

D'après le théorème 4.6 de [57], ce morphisme induit une équivalence sur la catégorie des $\bar{k}$-points. Le lecteur remarquera des changements de notations par rapport à loc. cit.: $\mathcal{M}_v(a)$ y était désigné par $\mathcal{M}_{v,a}^\bullet$ et ce qui y était désigné par $\mathcal{M}_{v,a}$ n'apparaîtra plus ici.

Proposition 4.15.1. — Pour tout $a \in \mathcal{A}^{\mathrm{ani}}(\bar{k})$, le quotient de

$$
\prod_ {v \in \bar {\mathrm{X}} - \mathrm{U}} \mathcal {M} _ {v} ^ {\mathrm{red}} (a) \times \mathcal {P} _ {a}
$$

par l'action diagonale de $\prod_{v\in\bar{X}-U}\mathcal{P}_{v}^{\mathrm{red}}(J_{a})$ est un champ de Deligne-Mumford propre. De plus, le morphisme

$$
\prod_ {v \in \bar {\mathrm{X}} - \mathrm{U}} \mathcal {M} _ {v} ^ {\mathrm{red}} (a) \wedge^ {\prod_ {v \in \bar {\mathrm{X}} - \mathrm{U}} \mathcal {P} _ {v} ^ {\mathrm{red}} (\mathrm{J} _ {a})} \mathcal {P} _ {a} \to \mathcal {M} _ {a}
$$

est un homéomorphisme.

Démonstration. — L'homomorphisme  $\mathcal{P}_{v}(\mathrm{J}_{a})\to\mathcal{P}_{a}$  induit un homomorphisme  $\pi_{0}(\mathcal{P}_{v}(\mathrm{J}_{a}))\to\pi_{0}(\mathcal{P}_{a})$  sur les groupes des composantes connexes. Puisque  $a\in\mathcal{A}^{\mathrm{ani}}(\bar{k})$ ,  $\pi_{0}(\mathcal{P}_{a})$  est un groupe fini, le noyau de cet homomorphisme est un sous-groupe d'indice fini de  $\pi_{0}(\mathcal{P}_{v}(\mathrm{J}_{a}))$ . Il existe donc un sous-groupe abélien libre d'indice fini  $\Lambda_{v}$  de  $\pi_{0}(\mathcal{P}_{v}(\mathrm{J}_{a}))$  contenu dans ce noyau.

Choisissons un relèvement $\Lambda_v \to \mathcal{P}_v(\mathrm{J}_a)$. Puisque $a$ est défini sur un corps fini, quitte à remplacer $\Lambda_v$ par un sous-groupe d'indice fini, on peut supposer que $\Lambda_v$ est contenu dans le noyau de $\mathcal{P}_v(\mathrm{J}_a) \to \mathcal{P}_a$.

Le groupe $\prod_{v\in\bar{\mathrm{X}}-\mathrm{U}}\Lambda_v$ agit sur $\prod_{v\in\bar{\mathrm{X}}-\mathrm{U}}\mathcal{M}_v^{\mathrm{red}}(a)\times\mathcal{P}_a$ en agissant librement sur le premier facteur et trivialement sur le second facteur. Le quotient est

$$
\prod_ {v \in \bar {\mathrm{X}} - \mathrm{U}} (\mathcal {M} _ {v} ^ {\mathrm{red}} (a) / \Lambda_ {v}) \times \mathcal {P} _ {a}
$$

où chaque $\mathcal{M}_{v}^{\mathrm{red}}(a)/\Lambda_{v}$ est un $\bar{k}$-schéma projectif d'après Kazhdan et Lusztig cf. 3.4.1. Il reste à quotient par $\prod_{v\in\bar{\mathrm{X}}-\mathrm{U}}(\mathcal{P}_{v}(\mathrm{J}_{a})/\Lambda_{v})$. Pour tout $v$, l'homomorphisme $\mathcal{R}_{v}(a)\to\mathcal{P}_{v}(\mathrm{J}_{a})/\Lambda_{v}$ est injectif et de noyau fini. Rappelons qu'on a une suite exacte

$$
1 \to \mathcal {R} _ {a} \to \mathcal {P} _ {a} \to \mathcal {P} _ {a} ^ {\flat} \to 1
$$

où  $P_{a}^{b}$  est un champ de Deligne-Mumford propre. Le quotient de

$$
\prod_ {v \in \bar {\mathrm{X}} - \mathrm{U}} (\mathcal {M} _ {v} ^ {\mathrm{red}} (a) / \Lambda_ {v}) \times \mathcal {P} _ {a}
$$

par l'action diagonale de $\mathcal{R}_{a}=\prod_{v}\mathcal{R}_{v}(a)$ est donc une fibration localement triviale au-dessus de $\mathcal{P}_{a}^{\flat}$ de fibres isomorphes à

$$
\prod_ {v \in \bar {\mathrm{X}} - \mathrm{U}} (\mathcal {M} _ {v} ^ {\mathrm{red}} (a) / \Lambda_ {v}).
$$

Ce quotient est donc un champ de Deligne-Mumford propre.

Il reste donc à quotient par le groupe fini  $\prod_{v}\mathcal{P}_{v}(\mathrm{J}_{a})/(\mathcal{R}_{v}(a)\times\Lambda_{v})$ . Le quotient final est aussi un champ de Deligne-Mumford propre.

Puisque  $M_{a}$  est un champ de Deligne-Mumford, en particulier séparé, le morphisme

$$
\zeta : \prod_ {v \in \bar {\mathrm{X}} - \mathrm{U}} \mathcal {M} _ {v} ^ {\mathrm{red}} (a) \wedge^ {\prod_ {v \in \bar {\mathrm{X}} - \mathrm{U}} \mathcal {P} _ {v} ^ {\mathrm{red}} (\mathrm{J} _ {a})} \mathcal {P} _ {a} \to \mathcal {M} _ {a}
$$

est un morphisme propre. Puisqu'il induit une équivalence sur les $\bar{k}$-points, c'est donc un homéomorphisme. En particulier, $\mathcal{M}_a$ est un champ de Deligne-Mumford propre.

On s'attend à ce que l'énoncé ci-dessus s'étende à $a \in \mathcal{A}^{\heartsuit}(\bar{k})$.

Corollaire 4.15.2. — Pour tout $a \in \mathcal{A}^{\mathrm{ani}}(\bar{k})$, $\mathcal{M}_a$ est homéomorphe à un schéma projectif. De plus, pour tout $m \in \mathcal{M}_a(\bar{k})$, le stabilisateur de $m$ dans $\mathcal{P}_a$ est un groupe affine.

4.16. Densité. — On va maintenant énoncer et démontrer l'analogue global de 3.10.1.

Proposition 4.16.1. — Pour tout point géométrique $a \in \mathcal{A}^{\heartsuit}(\bar{k})$, $\mathcal{M}_{a}^{\text{reg}}$ est dense dans la fibre $\mathcal{M}_{a}$.

Démonstration. — La formule de produit 4.15.1 implique que le fermé complémentaire $\mathcal{M}_{a}^{\mathrm{reg}}$ dans $\mathcal{M}_{a}$ est de dimension strictement plus petite que $\mathcal{M}_{a}^{\mathrm{reg}}$. Comme l'espace total de Hitchin $\mathcal{M}$ est lisse sur $k$ d'après 4.14.1, les fibres de Hitchin $\mathcal{M}_{a}$ sont localement une intersection complète. En particulier, elles ne peuvent pas admettre des composantes irréductibles de dimension strictement plus petite que la sienne. Ceci démontre que $\mathcal{M}_{a}^{\mathrm{reg}}$ est dense dans $\mathcal{M}_{a}$.

La démonstration ci-dessus est essentiellement la même que celle de Altman, Iarrobino et Kleiman dans [1] pour la densité de la jacobienne dans la jacobienne compactifiée d'une courbe projective réduite irréductible ayant des singularités planes.

Corollaire 4.16.2. — La partie régulière $\mathcal{M}_{v}^{\mathrm{reg}}(a)$ de la fibre de Springer $\mathcal{M}_{v}(a)$ est dense.

On commence par construire une situation globale à partir de la situation locale donnée en procédant comme dans cf. 8.6. L'assertion locale se déduit alors de l'assertion globale à l'aide de la formule de produit cf. 4.15.1. Nous laissons au lecteur les détails de la démonstration de ce corollaire qui ne sera pas utilisé dans la suite de l'article.

Corollaire 4.16.3. — Pour tout $a \in \mathcal{A}^{\heartsuit}(\bar{k})$, $\mathcal{M}_{a}$ est équidimensionnelle de dimension égale à

$$
\sharp \Phi \deg (\mathrm{D}) / 2 + r (g - 1).
$$

De plus, l'ensemble des composantes irréductibles de $\mathcal{M}_{a}$ s'identifie au groupe $\pi_{0}(\mathrm{P}_{a})$.

Démonstration. — La formule de dimension résulte de 4.13.3. L'identification de l'ensemble des composantes irréductibles de $\mathcal{M}_{a}$ avec le groupe $\pi_{0}(\mathrm{P}_{a})$ est rendue possible par la section de Kostant.

Corollaire 4.16.4. — Si deg(D) > 2g-2, le morphisme $f^{\heartsuit} : \mathcal{M}^{\heartsuit} \to \mathcal{A}^{\heartsuit}$ est un morphisme plat de dimension relative d. Ses fibres sont géométriquement réduites.

Démonstration. — D'après 4.14.1, $\mathcal{M}^{\heartsuit}$ et $\mathcal{A}^{\heartsuit}$ sont lisses sur $k$. Pour démontrer que $f$ est plat, il suffit alors de démontrer que la dimension des fibres vérifie l'égalité

$$
\dim (\mathcal {M} _ {a}) = \dim (\mathcal {M}) - \dim (\mathcal {A}).
$$

Ceci découle des égalités  $\dim(\mathcal{M}_{a})=\dim(\mathrm{P}_{a})$ ,  $\dim(\mathcal{M})=\dim(\mathrm{P})$  et pour P lisse sur A cf. 4.3.5, on a l'égalité

$$
\dim (\mathcal {P} ^ {\heartsuit}) = \dim (\mathcal {A} ^ {\heartsuit}) + \dim (\mathcal {P} _ {a}).
$$

Comme dans la démonstration de 4.16.1, on sait que la fibre $\mathcal{M}_{a}$ est localement une intersection complète. Puisqu'elle admet un ouvert dense lisse $\mathcal{M}_{a}^{\mathrm{reg}}$, elle est nécessairement réduite.

4.17. Le cas des groupes endoscopiques. — Soit  $(\kappa, \rho_{\kappa})$  une donnée endoscopique de G au-dessus de X cf. 1.8.1. Soit H le groupe endoscopique associé. Comme dans 1.9, on a un morphisme  $\nu : c_{H} \to c$ . En tordant par D, on obtient un morphisme  $\nu : c_{H,D} \to c_{D}$ . En prenant les points à valeurs dans X, on obtient un morphisme qu'on note encore

$$
\nu : \mathcal {A} _ {\mathrm{H}} \to \mathcal {A}.
$$

On sait d'après [57, 7.2] que la restriction de ce morphisme à l'ouvert $\mathcal{A}^{\heartsuit}$ est un morphisme fini et non ramifié.

4.17.1. — Notons

$$
r _ {\mathrm{H}} ^ {\mathrm{G}} (\mathrm{D}) = (| \Phi | - | \Phi_ {\mathrm{H}} |) \deg (\mathrm{D}) / 2.
$$

D'après 4.13.1, on sait que

$$
\dim (\mathcal {A}) - \dim (\mathcal {A} _ {\mathrm{H}}) = r _ {\mathrm{H}} ^ {\mathrm{G}} (\mathrm{D})
$$

de sorte que l'image de $\mathcal{A}_{\mathrm{H}}^{\mathrm{G}-\heartsuit}=\nu^{-1}(\mathcal{A}^{\heartsuit})$ dans $\mathcal{A}^{\heartsuit}$ est un sous-schéma fermé de codimension $r_{\mathrm{H}}^{\mathrm{G}}(\mathrm{D})$.

4.17.2. — Au-dessus de  $A_{H}$ , on a la fibration de Hitchin du groupe H

$$
f _ {\mathrm{H}}: \mathcal {M} _ {\mathrm{H}} \to \mathcal {A} _ {\mathrm{H}}.
$$

On a également le champ de Picard $\mathcal{P}_{\mathrm{H}} \to \mathcal{A}_{\mathrm{H}}$ agissant sur $\mathcal{M}_{\mathrm{H}}$. Il n'y a pas de relation directe entre $\mathcal{M}$ et $\mathcal{M}_{\mathrm{H}}$ mais $\mathcal{P}$ et $\mathcal{P}_{\mathrm{H}}$ sont reliés de façon simple. Soit $a_{\mathrm{H}} \in \mathcal{A}_{\mathrm{H}}(\bar{k})$ d'image $a \in \mathcal{A}^{\heartsuit}(\bar{k})$. L'homomorphisme $\mu : \nu^{*}\mathrm{J} \to \mathrm{J}_{\mathrm{H}}$ de 2.5.1 induit un homomorphisme $\mathrm{J}_{a} \to \mathrm{J}_{\mathrm{H},a_{\mathrm{H}}}$ qui est génériquement un isomorphisme. On obtient donc un homomorphisme surjectif

$$
\mathcal {P} _ {a} \rightarrow \mathcal {P} _ {\mathrm{H}, a _ {\mathrm{H}}}
$$

de noyau

$$
\mathcal {R} _ {\mathrm{H}, a _ {\mathrm{H}}} ^ {\mathrm{G}} = \mathrm{H} ^ {0} (\overline {{\mathrm{X}}}, \mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}}} / \mathrm{J} _ {a})
$$

qui est un groupe affine de dimension

$$
\dim (\mathcal {R} _ {\mathrm{H}, a _ {\mathrm{H}}} ^ {\mathrm{G}}) = \dim (\mathcal {P} _ {a}) - \dim (\mathcal {P} _ {\mathrm{H}, a _ {\mathrm{H}}}).
$$

D'après la formule 4.13.3, on également

$$
\dim (\mathcal {R} _ {\mathrm{H}, a _ {\mathrm{H}}} ^ {\mathrm{G}}) = (| \Phi | - | \Phi_ {\mathrm{H}} |) \deg (\mathrm{D}) / 2 = r _ {\mathrm{H}} ^ {\mathrm{G}} (\mathrm{D}).
$$

4.17.3. — Soit  $J_{H,a_{H}}^{b}$  le modèle de Néron de  $J_{H,a_{H}}$ . On a des homomorphismes

$$
\mathrm{J} _ {a} \rightarrow \mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}}} \rightarrow \mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}}} ^ {\flat}
$$

qui sont des isomorphismes sur un ouvert non-vide de $\overline{\mathbf{X}}$. Il s'ensuit que $J_{H,a_H}^b$ est aussi le modèle de Néron de $J_a$. En combinant avec 4.9.2, on a la suite exacte

$$
1 \to \mathcal {R} _ {\mathrm{H}, a _ {\mathrm{H}}} ^ {\mathrm{G}} \to \mathcal {R} _ {a} \to \mathcal {R} _ {\mathrm{H}, a _ {\mathrm{H}}} \to 1.
$$

On en déduit la formule de dimension

$$
\delta_ {a} - \delta_ {\mathrm{H}, a _ {\mathrm{H}}} = r _ {\mathrm{H}} ^ {\mathrm{G}} (\mathbf {D})
$$

où $\delta_{a}=\dim(\mathcal{R}_{a})$ et $\delta_{\mathrm{H},a_{\mathrm{H}}}=\dim(\mathcal{R}_{\mathrm{H},a_{\mathrm{H}}})$ sont les invariants delta de $a$ et de $a_{\mathrm{H}}$ par rapport aux groupes G et H respectivement.

4.18. Le cas des groupes appariés. — Soient  $G_{1}$  et  $G_{2}$  deux X-schémas en groupes appariés au sens de 1.12.5. On a alors un isomorphisme  $c_{G_{1}} = c_{G_{2}}$  cf. 1.12.6. On en déduit un isomorphisme  $c_{G_{1},D} = c_{G_{2},D}$  puis un isomorphisme entre les bases des fibrations de Hitchin

$$
\mathcal {A} = \mathcal {A} _ {1} = \mathcal {A} _ {2}.
$$

Il n'y a pas de relation directe entre les fibrations $f_{1}:\mathcal{M}_{1}\to\mathcal{A}_{1}$ et $f_{2}:\mathcal{M}_{2}\to\mathcal{A}_{2}$ de $\mathrm{G}_{1}$ et $\mathrm{G}_{2}$ mais une relation entre les champs de Picard associés $\mathcal{P}_{1}$ et $\mathcal{P}_{2}$.

Proposition 4.18.1. — Il existe un homomorphisme entre A-champs de Picard

$$
\mathcal {P} _ {1} \to \mathcal {P} _ {2}
$$

qui induit une isogénie entre leurs composantes neutres.

Démonstration. — Comme dans la démonstration de 1.12.6, on a un isomorphisme  $t_{1} \stackrel{\sim}{\to} t_{2}$  au-dessus de l'isomorphisme  $c_{G_{1}} \stackrel{\sim}{\to} c_{G_{2}}$ . En vertu de 2.4.7, on en déduit un isomorphisme entre les composantes neutres  $J_{G_{1}}^{0} \stackrel{\sim}{\to} J_{G_{2}}^{0}$  des centralisateurs réguliers de  $G_{1}$  et  $G_{2}$ . Puisque  $J_{G_{1}}$  et  $J_{G_{2}}$  sont des schémas en groupes de type fini, en composant l'isomorphisme  $J_{G_{1}}^{0} \stackrel{\sim}{\to} J_{G_{2}}^{0}$  avec la multiplication par un entier N assez divisible, on obtient un homomorphisme  $J_{G_{1}}^{0} \to J_{G_{2}}^{0}$  qui s'étend en un homomorphisme  $J_{G_{1}} \to J_{G_{2}}^{0}$  de noyau et de conoyau finis. On en déduit un homomorphisme entre  $P_{1} \to P_{2}$  qui induit une isogénie entre les composantes neutres.

## 5. Stratification

Nous allons construire dans ce chapitre deux stratifications de la base de Hitchin dont l'une est relative au groupe des composantes connexes de la fibre  $P_{a}$  et l'autre est relative à l'invariant  $\delta_{a}$  qui est en quelques sortes la dimension de la partie affine de  $P_{a}$ .

L'existence de ces stratifications résulte du caractère semi-continu de ces deux invariants et d'un résultat de constructibilité.

Le résultat de constructibilité est fondé sur l'existence de l'espace de module de normalisation des courbes camérales en famille. En effet, il n'est pas difficile de voir que les deux invariants  $\delta_{a}$  et  $\pi_{0}(\mathcal{P}_{a})$  sont localement constants en présence d'une telle normalisation en famille.

On va définir ensuite une stratification adaptée à l'invariant $\pi_0(\mathcal{P}_a)$. Il sera commode de passer à un ouvert étale $\tilde{\mathcal{A}}$ de la base de Hitchin $\mathcal{A}$. Le faisceau $\pi_0(\mathcal{P})$ des groupes de composantes connexes des fibres de $\mathcal{P}$ devient constant au-dessus des strates de $\tilde{\mathcal{A}}$ au lieu d'être seulement localement constant. On va même se restreindre à un ouvert $\tilde{\mathcal{A}}^{\mathrm{ani}}$ de $\tilde{\mathcal{A}}$ où le faisceau $\pi_0(\mathcal{P})$ est fini.

On va ensuite étudier la stratification de $\tilde{\mathcal{A}}^{\mathrm{ani}}$ adaptée à l'invariant delta $\tilde{\mathcal{A}}^{\mathrm{ani}} = \bigsqcup_{\delta} \tilde{\mathcal{A}}_{\delta}^{\mathrm{ani}}$ avec $a \in \tilde{\mathcal{A}}_{\delta}^{\mathrm{ani}}$ si et seulement si $\delta_a = \delta$. Le résultat clé de ce chapitre est l'inégalité 5.7.2 codim($\tilde{\mathcal{A}}_{\delta}^{\mathrm{ani}}$) $\geq \delta$ sous l'hypothèse que deg(D) est grand par rapport à $\delta$. En caractéristique 0, on dispose d'une démonstration de cette inégalité fondée sur le caractère symplectique de la fibration de Hitchin sans recours à l'hypothèse sur deg(D) cf. [60]. Malheureusement, cette démonstration ne semble pas transposable en caractéristique positive. Nous contournons cet obstacle par un argument local-global. Goresky, Kottwitz et MacPherson ont fait des calculs de codimension similaires dans le cadre local cf. [28]. Le calcul global se ramène au calcul local pourvu que deg(D) soit grand par rapport à $\delta$.

Il n'y pourtant guère de doute que cette hypothèse est superflue. Comme on n'est pas parvenu pour l'instant à s'en débarrasser, nous serons forcés à recourir aux arguments de comptage plus compliqués au chapitre 8.

5.1. Normalisations en famille des courbes spectrales. — Ce paragraphe ne servira que de modèle pour la suite du chapitre. Il fait aussi le pont avec la théorie classique des déformations des courbes planes. Le lecteur pourra consulter l'article de Laumon [51] pour plus d'informations.

Dans le cas  $\mathrm{G} = \mathrm{GL}(r)$ , on peut associer à tout point  $a \in \mathcal{A}^{\heartsuit}(\bar{k})$  une courbe réduite  $Y_{a}$  tracée sur l'espace total du fibré en droites D cf. 4.4. Le groupe de symétries  $P_{a}$  est alors le champ de Picard  $\operatorname{Pic}(\mathrm{Y}_{a})$  des  $O_{Y_{a}}$ -modules inversibles. La structure de  $\operatorname{Pic}(\mathrm{Y}_{a})$  peut être analysée à l'aide de la normalisation de  $Y_{a}$ . Soit  $\xi : Y_{a}^{\flat} \to Y_{a}$  la normalisation de  $Y_{a}$ . Le foncteur  $L \mapsto \xi^{*}L$  qui associe à tout  $O_{Y_{a}}$ -module inversible son image inverse par  $\xi$  définit un homomorphisme  $\operatorname{Pic}(\mathrm{Y}_{a}) \to \operatorname{Pic}(\mathrm{Y}_{a}^{\flat})$ . La suite exacte longue de cohomologie associée à la suite exacte courte de faisceaux sur  $Y_{a}$

$$
1 \to \mathcal {O} _ {\mathrm{Y} _ {a}} ^ {\times} \to \xi_ {*} \mathcal {O} _ {\mathrm{Y} _ {a} ^ {\flat}} ^ {\times} \to \xi_ {*} \mathcal {O} _ {\mathrm{Y} _ {a} ^ {\flat}} ^ {\times} / \mathcal {O} _ {\mathrm{Y} _ {a}} ^ {\times} \to 1
$$

nous fournit les renseignements suivants. Le noyau de $\xi^{*}$ qui consiste en la catégorie des $\mathcal{O}_{\mathrm{Y}_{a}}$-modules inversibles $\mathcal{L}$ munis d'une trivialisation de $\xi^{*}\mathcal{L}$, est un groupe algébrique dont l'ensemble des points est $\mathrm{H}^{0}(\mathrm{Y}_{a}, \xi_{*}\mathcal{O}_{\mathrm{Y}_{a}}^{\times}/\mathcal{O}_{\mathrm{Y}_{a}}^{\times})$. De plus, le foncteur $\xi^{*}$ est essentiellement surjectif.

On peut attacher à cette situation deux invariants :

\- l'ensemble $\pi_0(\mathbf{Y}_a^b)$ des composantes connexes de $\mathbf{Y}_a^b$;

\- l'entier $\delta_{a} = \dim \mathrm{H}^{0}(\mathrm{Y}_{a},\xi_{*}\mathcal{O}_{\mathrm{Y}_{a}^{\flat}} / \mathcal{O}_{\mathrm{Y}_{a}})$ appelé l'invariant $\delta$ de Serre.

En prenant le degré sur les composantes de  $Y_{a}^{b}$ , on obtient un homomorphisme

$$
\pi_ {0} (\mathrm{Pic} (\mathrm{Y} _ {a})) \to \mathbf {Z} ^ {\pi_ {0} (\mathrm{Y} _ {a} ^ {\flat})}
$$

qui est un isomorphisme. Quant à l'invariant  $\delta$ , il mesure la dimension du groupe affine  $\ker(\xi^{*})$ .

Teissier a introduit dans [77] l'espace de module des normalisations en famille d'une famille de courbes planes. Rappelons d'abord la définition d'une normalisation en famille.

Définition 5.1.1. — Soit $y: Y \to S$ un morphisme projectif, plat et de fibres réduites de dimension un. Une normalisation en famille de $Y$ est un morphisme propre birationnel $\xi: Y^{\flat} \to Y$ qui est un isomorphisme au-dessus d'un ouvert $U$ de $Y$, dense dans chaque fibre de $Y$ au-dessus de $S$ tel que le composé $y \circ \xi$ est un morphisme propre et lisse.

Dans une normalisation en famille les invariants  $\delta$  et  $\pi_{0}(\mathcal{P})$  demeurent localement constants.

Proposition 5.1.2. — Avec les notations comme dans la définition ci-dessus :

(1) L'image directe $y_{*}(\xi_{*}\mathcal{O}_{\mathrm{Y}^{\flat}} / \mathcal{O}_{\mathrm{Y}})$ est un $\mathcal{O}_{\mathrm{S}}$-module localement libre de type fini.

(2) Il existe un faisceau $\pi_0(\mathbf{Y}^\flat/\mathbf{S})$ localement constant pour la topologie étale de S dont la fibre en chaque point géométrique $s \in \mathbf{S}$ est l'ensemble des composantes connexes de $\mathbf{Y}_s^\flat$.

Démonstration. — Soit $s$ un point géométrique de S. La restriction de $\xi_{*}\mathcal{O}_{\mathrm{Y}^{\flat}}/\mathcal{O}_{\mathrm{Y}}$ est supportée par $\mathrm{Y}_{s}-\mathrm{U}_{s}$ qui est un schéma de dimension zéro. Il s'ensuit que $\mathrm{H}^{1}(\mathrm{Y}_{s},\xi_{*}\mathcal{O}_{\mathrm{Y}^{\flat}}/\mathcal{O}_{\mathrm{Y}})=0$ et

$$
\dim \mathrm{H} ^ {0} (\mathrm{Y} _ {s}, \xi_ {*} \mathcal {O} _ {\mathrm{Y} ^ {\flat}} / \mathcal {O} _ {\mathrm{Y}})
$$

est la différence entre le genre arithmétique de  $Y_{s}$  et celui de  $Y_{s}^{\flat}$ . C'est donc une fonction localement constante en s. Il reste à appliquer le théorème de changement de base pour les faisceaux cohérents [56, cor. 2, p. 50].

Considérons la factorisation de Stein  $Y^{b} \rightarrow S' \rightarrow S$  où  $S' \rightarrow S$  est un morphisme fini et  $Y^{b} \rightarrow S'$  est un morphisme projectif ayant des fibres géométriques connexes. L'hypothèse de lissité de  $Y^{b} \rightarrow S$  implique que le morphisme  $S' \rightarrow S$  est fini et étale. Le faisceau  $\pi_{0}(Y^{b}/S)$  désiré est celui représentable par  $S'$ .

Nous allons nous restreindre aux cas des courbes spectrales. Soit $\mathcal{B}$ l'espace de module des normalisations en famille des courbes spectrales $\mathrm{Y}_{a}$. Il associe à tout $k$-schéma S le groupoïde $\mathcal{B}(\mathrm{S})$ des triplets $(a, \mathrm{Y}_{a}^{\flat}, \xi)$ où $a \in \mathcal{A}^{\heartsuit}(\mathrm{S})$ est un S-point de $\mathcal{A}^{\heartsuit}$, où $\mathrm{Y}_{a}^{\flat}$ est une S-courbe projective lisse et où $\xi: \mathrm{Y}_{a}^{\flat} \to \mathrm{Y}_{a}$ est une normalisation en famille de la courbe spectrale $\mathrm{Y}_{a}$ associée à $a$. Le foncteur $\mathcal{B}$ est représentable par un $k$-schéma de type fini.

Le morphisme d'oubli $\mathcal{B} \to \mathcal{A}^{\heartsuit}$ induit une bijection au niveau des $\bar{k}$-points. En effet, pour tout $a \in \mathbf{A}^{\heartsuit}(\bar{k})$, la normalisation $\mathrm{Y}_{a}^{\flat}$ de $\mathrm{Y}_{a}$ est uniquement déterminée. Toutefois, $\mathcal{B}$ a plus de composantes connexes que $\mathcal{A}$. En effet, les deux invariants $\pi_{0}(\tilde{\mathrm{Y}}_{a})$ et $\delta_{a}$ sont localement constants d'après la proposition précédente. Le fait que l'invariant $\delta$ est semi-continu supérieurement induit une stratification adaptée à cet invariant.

Comme les courbes spectrales sont tracées sur une surface, ses singularités sont planes. L'analogue de l'égalité de type 5.7.2 remonte en fait à l'étude des familles de courbes planes Severi. Les variantes modernes et rigoureuses peuvent être trouvées dans Teissier cf. [77], Diaz, Harris cf. [22], Fantechi, Gottsche, Van Straten cf. [25].

5.2. Normalisation en famille des courbes camérales. — Bien que dans le cas des groupes classiques, on dispose encore des courbes spectrales [34], [59], il est plus uniforme d'utiliser l'espace de module des normalisations des courbes camérales munies de l'action de W.

Soit S un k-schéma. Un S-point a de  $A^{\heartsuit}$  définit un morphisme  $a: X \times S \to c_{D}$ . En prenant l'image réciproque du revêtement  $\pi: t_{D} \to c_{D}$ , on obtient un revêtement fini plat  $\tilde{X}_{a}$  de  $X \times S$  qui dans chaque fibre est génériquement un torseur sous W.

Considérons le foncteur $\mathcal{B}$ qui associe à tout $k$-schéma S le groupoïde des triplets $(a, \tilde{\mathrm{X}}_a^{\flat}, \xi)$ où :

\- $a \in \mathcal{A}^{\heartsuit}(\mathrm{S})$ est un S-point de $\mathcal{A}^{\heartsuit}$.

\- $\tilde{\mathbf{X}}_{a}^{\flat}$ est une S-courbe propre et lisse munie d'une action de W.

\- $\xi : \tilde{\mathbf{X}}_a^b \to \tilde{\mathbf{X}}_a$ est une normalisation en famille W-équivariante cf. 5.1.1.

Soit $b = (a, \tilde{\mathrm{X}}_a^{\flat}, \xi) \in \mathcal{B}(\mathrm{S})$ un point de $\mathcal{B}$ à valeur dans un schéma connexe S. Soit $\mathrm{pr}_{\mathrm{S}}: \mathrm{X} \times \mathrm{S} \to \mathrm{S}$ la projection sur S. D'après 5.1.1, l'image directe $(\mathrm{pr}_{\mathrm{S}})_*(\xi_*\mathcal{O}_{\tilde{\mathrm{X}}_a^{\flat}}/\mathcal{O}_{\mathrm{X}_a^{\flat}})$ est un $\mathcal{O}_{\mathrm{S}}$-module localement libre. Il en est de même de

$$
((\mathrm{pr} _ {\mathrm{S}}) _ {*} (\xi_ {*} \mathcal {O} _ {\tilde {\mathrm{X}} _ {a} ^ {\flat}} / \mathcal {O} _ {\mathrm{X} _ {a} ^ {\flat}}) \otimes_ {\mathcal {O} _ {\mathrm{X}}} \mathfrak {t}) ^ {\mathrm{W}}
$$

sous l'hypothèse que l'ordre de W est premier à la caractéristique de k. Puisque S est connexe, ce  $O_{S}$ -module localement libre a un rang qu'on notera  $\delta(b)$ .

Pour tout $a \in \mathcal{A}^{\heartsuit}(\bar{k})$, la courbe camérale $\tilde{\mathrm{X}}_a$ admet une unique normalisation $\tilde{\mathrm{X}}_a^{\flat}$ qui est alors une courbe lisse sur $\bar{k}$. Il en résulte que le morphisme d'oubli $\mathcal{B} \to \mathcal{A}^{\heartsuit}$ induit une bijection au niveau des points à valeur dans un corps algébriquement clos.

Proposition 5.2.1. — Le foncteur B défini ci-dessus est représentable par un k-schéma de type fini.

Démonstration. — Considérons le foncteur $\mathcal{B}'$ qui associe à tout schéma S l'ensemble des couples $(\tilde{\mathrm{X}}_a^\flat, \gamma)$ où :

\- $\tilde{\mathbf{X}}_a^{\flat}$ est une courbe propre et lisse au-dessus de S muni d'une action de W munie d'un morphisme $\pi_{a}^{\flat}:\tilde{\mathbf{X}}_{a}^{\flat}\to \mathbf{X}\times \mathbf{S}$ qui est fini, plat et même un torseur sous W au-dessus d'un ouvert U de $\mathbf{X}\times \mathbf{S}$ qui se surjecte sur S.

\- $\gamma : \tilde{\mathrm{X}}_{a}^{\flat} \to \mathfrak{t}_{\mathrm{D}} \times \mathrm{S}$ est un S-morphisme W-équivariant tel que l'image inverse de l'ouvert régulier semi-simple de $\mathfrak{t}_{\mathrm{D}}$ est dense dans chaque fibre.

Soit H le foncteur qui associe à tout schéma S l'ensemble des classes d'isomorphisme de courbes projectives lisses  $\tilde{X}_{a}^{b}$  sur S muni d'une action de W et d'un morphisme  $\pi_{a}^{b}: \tilde{X}_{a}^{b} \to X \times S$  comme ci-dessus. Ce foncteur est représentable par un k-schéma quasi-projectif de la même manière que le schéma de Hurwitz. Le morphisme  $h: B' \to H$  est également représentable par un ouvert d'un fibré vectoriel au-dessus de H si bien que  $B'$  est représentable par un k-schéma quasi-projectif.

Par ailleurs, on a un morphisme $\mathcal{B} \to \mathcal{B}'$. Il associe au point $b = (a, \tilde{\mathrm{X}}_a^\flat, \xi) \in \mathcal{B}(\mathrm{S})$ le point $b' = (\tilde{\mathrm{X}}_a^\flat, \gamma)$ où $\gamma$ est le composé de $\xi : \tilde{\mathrm{X}}_a^\flat \to \tilde{\mathrm{X}}_a$ et de l'immersion fermée $\tilde{\mathrm{X}}_a \to \mathrm{t}_{\mathrm{D}} \times \mathrm{S}$. Pour démontrer la représentabilité de $\mathcal{B}$, il suffit de vérifier l'assertion suivante.

Lemme 5.2.2. — Le morphisme $\mathcal{B} \to \mathcal{B}'$ est un isomorphisme.

Démonstration. — Pour démontrer que le morphisme $\mathcal{B} \to \mathcal{B}'$ est un isomorphisme, on va en construire un inverse. Soit $b' = (\tilde{\mathrm{X}}_a^b, \gamma) \in \mathcal{B}'(\mathrm{S})$. Considérons la partie W-invariante dans l'image directe $(\pi_a^b)_*\mathcal{O}_{\mathrm{X}_a^b}$. C'est un faisceau en $\mathcal{O}_{\mathrm{X} \times \mathrm{S}}$-algèbres finies qui fibre par fibre au-dessus de S est isomorphe génériquement à $\mathcal{O}_{\mathrm{X}}$. Puisque X est normal, ceci implique que

$$
((\pi_ {a} ^ {\flat}) _ {*} \mathcal {O} _ {\tilde {\mathrm{X}} _ {a} ^ {\flat}}) ^ {\mathrm{W}} = \mathcal {O} _ {\mathrm{X} \times \mathrm{S}}.
$$

En utilisant l'égalité $k[\mathbf{t}]^{\mathbf{W}} = k[\mathbf{c}]$ cf. 1.1.1, le morphisme W-équivariant $\gamma : \tilde{\mathbf{X}}_a^b \to \mathfrak{t}_\mathrm{D}$ induit un morphisme $a: \mathbf{X} \times \mathbf{S} \to \mathfrak{c}_{\mathrm{D}}$. Soit $\tilde{\mathbf{X}}_a$ la courbe camérale associée à $a$. Le morphisme $\gamma$ se factorise alors par un morphisme

$$
\xi : \tilde {\mathrm{X}} _ {a} ^ {\flat} \to \tilde {\mathrm{X}} _ {a}
$$

qui est fibre par fibre au-dessus de S une normalisation de  $\tilde{X}_{a}$ . On a donc construit un point  $b = (a, \tilde{\mathrm{X}}_{a}^{\flat}, \xi) \in \mathcal{B}(\mathrm{S})$ . Le morphisme  $B' \to B$  ainsi construit est l'inverse du morphisme  $B \to B'$  dans l'énoncé du lemme.

5.3. Stratification de l'ouvert étale $\tilde{\mathcal{A}}$. — Dans la suite de l'article, nous ne travaillerons pas directement sur la base de Hitchin $\mathcal{A}$ mais sur un ouvert étale de celle-ci. Ce choix altère notre prétention de géométriser la stabilisation de la formule des traces 1.13 mais nous débarrasse de quelques difficultés accessoires.

5.3.1. — Soit $\infty \in \mathrm{X}(\bar{k})$. Considérons l'ouvert étale $\tilde{\mathcal{A}}$ de $\mathcal{A} \otimes_k \bar{k}$ dont les points sont des couples $(a, \tilde{\infty})$ avec $a \in \mathcal{A}$ tel que le revêtement caméral $\tilde{\mathrm{X}}_a \to \mathrm{X}$ est étale au-dessus de $\infty$ et où $\tilde{\infty}$ est un point de $\tilde{\mathrm{X}}_a$ au-dessus de $\infty$. Notons que si $\infty \in \mathrm{X}(k)$, $\tilde{\mathcal{A}}$ a une $k$-structure évidente.

La construction ci-dessus peut être reformulée en termes diagrammatiques comme suit. Le choix du point $\infty \in \mathrm{X}(\bar{k})$ définit un morphisme $\mathcal{A} \otimes_{k} \bar{k} \to \mathfrak{c}_{\mathrm{D},\infty}$ où $\mathfrak{c}_{\mathrm{D},\infty}$ est la fibre

de $\mathfrak{c}_{\mathrm{D}}$ au-dessus de $\infty$ qui associe à $a \in \mathcal{A}$ le point $a(\infty)$. Notons $\mathcal{A}^{\infty}$ l'image réciproque de l'ouvert régulier semi-simple $\mathfrak{c}_{\mathrm{D},\infty}^{\mathrm{rs}}$ de $\mathfrak{c}_{\mathrm{D},\infty}$. On a en fait un diagramme cartésien

![](images/page_93_image_1.jpg)

qui fait de  $\tilde{A}$  un  $W_{\infty}$ -torseur sur  $A^{\infty}$  où  $W_{\infty}$  est la fibre du X-schéma en groupes fini étale W au-dessus de  $\infty$ .

Lemme 5.3.2. — Supposons que $\deg(\mathrm{D}) > 2g$. Alors $\tilde{\mathcal{A}}$ est lisse et géométriquement irréductible.

Démonstration. — Sous l'hypothèse deg(D) > 2g, l'application linéaire $\mathcal{A} \to \mathfrak{c}_{\mathrm{D},\infty}$ dans le diagramme ci-dessus, est surjective cf. 4.7.2. On en déduit que la flèche du haut du diagramme est un morphisme lisse de fibres connexes. Puisque $\mathfrak{t}_{\mathrm{D},\infty}$ est un vectoriel, $\tilde{\mathcal{A}}$ est lisse et géométriquement irréductible.

Nous allons maintenant former le diagramme cartésien :

$$
\tilde {\mathcal {B}} = \mathcal {B} \times_ {\mathcal {A}} \tilde {\mathcal {A}}
$$

où B est l'espace de module des normalisations en famille des courbes camérales cf. 5.2.1. Ce morphisme définit une bijection au niveau des points géométriques. L'image d'une composante connexe de  $\tilde{B} \otimes_{k} \bar{k}$  dans  $\tilde{A} \otimes_{k} \bar{k}$  est une partie constructible. Une partie constructible est par définition une réunion finie de parties localement fermées irréductibles. Soit  $\tilde{A}'$  l'une de ces parties localement fermées irréductibles et  $\tilde{B}'$  son image réciproque. Le morphisme  $\tilde{B}' \to \tilde{A}'$  induit une bijection au niveau des points géométriques, en particulier, il est quasi-fini. En appliquant le théorème principal de Zariski, on voit qu'il existe un ouvert dense  $\tilde{A}''$  de  $\tilde{A}'$  au-dessus duquel le morphisme  $\tilde{B}' \to \tilde{A}'$  est fini radiciel. En subdivisant davantage et en procédant par récurrence noethérienne, on obtient une stratification en parties localement fermées irréductibles

$$
\tilde {\mathcal {A}} \otimes_ {k} \bar {k} = \bigsqcup_ {\psi \in \Psi} \tilde {\mathcal {A}} _ {\psi}\tag{5.3.3}
$$

telle que si $\tilde{\mathcal{B}}_{\psi}$ désigne l'image inverse de $\tilde{\mathcal{A}}_{\psi}$ dans $\tilde{\mathcal{B}}$, le morphisme $\tilde{\mathcal{B}}_{\psi} \to \tilde{\mathcal{A}}_{\psi}$ est un morphisme fini radiciel.

Quitte à subdiviser encore plus, on peut supposer que l'adhérence d'une strate $\tilde{\mathcal{A}}_{\psi}$ est une réunion d'autres strates. Ceci permet de définir une relation d'ordre partiel sur l'ensemble $\Psi$ des strates. Puisque $\tilde{\mathcal{A}}$ est géométriquement irréductible, l'ensemble $\Psi$ admet un élément maximal qu'on notera $\psi_{\mathrm{G}}$.

5.4. Invariants monodromiques. — On va maintenant construire un invariant monodromique associé à chaque strate de la stratification 5.3.3.

Rappelons que la forme G de G est donnée par un homomorphisme  $\rho_{G}^{\bullet}:\pi_{1}(X,\infty)\to\operatorname{Out}(\mathbf{G})$ . Notons  $\Theta$  l'image du groupe fondamental géométrique  $\pi_{1}(\bar{X},\infty)$  dans  $\operatorname{Out}(\mathbf{G})$  qui en est un sous-groupe d'ordre fini.

5.4.1. — Soit $\tilde{a} = (a, \tilde{\infty}) \in \tilde{\mathcal{A}}(\bar{k})$. Soit U l'ouvert maximal de $\bar{\mathrm{X}}$ au-dessus duquel le revêtement caméral $\tilde{\mathrm{X}}_a \to \bar{\mathrm{X}}$ est étale. Il contient en particulier $\infty$. D'après 1.3.6, on a un diagramme cartésien :

$$
\begin{array}{c} \pi_ {1} (\mathrm{U}, \infty) \xrightarrow {\pi_ {a} ^ {\bullet}} \mathbf {W} \rtimes \operatorname{Out} (\mathbf {G}) \\ \Bigg \downarrow \\ \pi_ {1} (\bar {\mathrm{X}}, x) \xrightarrow [ \rho_ {\mathrm{G}} ^ {\bullet} ]{} \operatorname{Out} (\mathbf {G}) \end{array}
$$

Notons  $W_{\tilde{a}}$  l'image de  $\pi_{\tilde{a}}^{\bullet}$  dans  $\mathbf{W} \rtimes \operatorname{Out}(\mathbf{G})$  et  $I_{\tilde{a}}$  est l'image du noyau de l'homomorphisme  $\pi_{1}(\mathrm{U}, \infty) \to \pi_{1}(\bar{\mathrm{X}}, \infty)$ . Par construction,  $W_{\tilde{a}}$  est contenu dans le sous-groupe fini  $W \rtimes \Theta$  et  $I_{\tilde{a}}$  est un sous-groupe normal de  $W_{\tilde{a}}$  qui est contenu dans  $W_{\tilde{a}} \cap W$ .

5.4.2. — Reprenons la définition ci-dessus dans le langage des revêtements. Soit  $X_{\rho} \rightarrow \bar{X}$  le revêtement fini étale galoisien connexe de groupe de Galois  $\Theta$  qui correspond à l'homomorphisme surjectif

$$
\rho_ {\mathrm{G}} ^ {\bullet}: \pi_ {1} (\bar {\mathrm{X}}, \infty) \to \Theta .
$$

Par construction, il dispose d'un point $\infty_{\rho}$ au-dessus de $\infty$. Formons le produit cartésien

$$
\tilde {\mathbf {X}} _ {\rho , a} = \tilde {\mathbf {X}} _ {a} \times_ {\mathrm{X}} \mathbf {X} _ {\rho}
$$

de la courbe camérale $\tilde{\mathbf{X}}_a$ avec le revêtement fini étale $\mathbf{X}_{\rho} \to \mathbf{X}$. La courbe $\tilde{\mathbf{X}}_{\rho,a}$ est alors munie d'une action de $\mathbf{W} \rtimes \Theta$. Il en est de même de sa normalisation $\tilde{\mathbf{X}}_{\rho,a}^{\flat}$. Soit $\mathbf{C}_{\tilde{a}}$ la composante connexe de $\tilde{\mathbf{X}}_{\rho,a}^{\flat}$ qui contient $\tilde{\infty}_{\rho} = (\tilde{\infty}, \infty_{\rho})$. Le groupe $\mathrm{W}_{\tilde{a}}$ est le sous-groupe de $\mathbf{W} \rtimes \Theta$ constitué des éléments qui laissent stable cette composante. Le groupe $\mathrm{I}_{\tilde{a}}$ est alors le sous-groupe engendré par les éléments de $\mathrm{W}_{\tilde{a}}$ qui admettent au moins un point fixe dans $\mathrm{C}_{\tilde{a}}$. Puisque la projection de $\mathrm{C}_{\tilde{a}}$ sur $\mathbf{X}_{\rho}$ où le groupe $\Theta_{\rho}$ agit librement, $\mathrm{I}_{\tilde{a}}$ est contenu dans le noyau de la projection $\mathrm{W}_{\tilde{a}} \to \Theta$. Il s'ensuit aussi que $\mathrm{I}_{\tilde{a}} \subset \mathrm{W}_{\tilde{a}} \cap \mathbf{W}$.

Proposition 5.4.3. — L'application $\tilde{a} \to (\mathrm{I}_{\tilde{a}}, \mathrm{W}_{\tilde{a}})$ est constante sur chaque strate $\tilde{\mathcal{A}}_{\rho}$ de la stratification 5.3.3.

Démonstration. — Par construction de la stratification 5.3.3, le morphisme $\tilde{\mathcal{B}}_{\psi} \to \tilde{\mathcal{A}}_{\psi}$ est un morphisme fini radiciel. Au-dessus du schéma connexe $\tilde{\mathcal{B}}_{\psi}$, la normalisation de la courbe camérale $\tilde{\mathrm{X}}_a^{\mathrm{b}} \to \tilde{\mathrm{X}}_a$ se met en famille ainsi que toute la construction qui précède l'énoncé de cette proposition. On a donc une courbe relative propre et lisse

$$
\tilde {\mathbf {X}} _ {\rho , \psi} \rightarrow \tilde {\mathcal {B}} _ {\psi}
$$

munie d'une action de $\mathbf{W} \rtimes \Theta$ et d'une section $\tilde{\infty}_{\rho}$. Comme dans le lemme 5.1.2, il existe un faisceau localement constant $\pi_0(\tilde{\mathrm{X}}_{\rho,\psi}/\mathcal{B}_{\psi})$ pour la topologie étale de $\mathcal{B}_{\psi}$ qui interpole les ensembles des composantes irréductibles des fibres de $\tilde{\mathrm{X}}_{\rho,\psi}/\mathcal{B}_{\psi}$. Le groupe $\mathbf{W} \rtimes \Theta$ agit sur ce faisceau et induit une action transitive sur ses fibres. La donnée d'une section qui se déduit de $\tilde{\infty}_{\rho}$ implique que ce faisceau est constant. La proposition en résulte.

## 5.4.4. — Il résulte de la proposition précédente une application

$$
\psi \rightarrow (\mathrm{I} _ {\psi}, \mathrm{W} _ {\psi})
$$

définie sur l'ensemble $\Psi$ des strates de la stratification 5.3.3 qui est compatible avec l'application $\tilde{a} \mapsto (\mathrm{I}_{\tilde{a}}, \mathrm{W}_{\tilde{a}})$ définie au niveau des points géométriques.

Lemme 5.4.5. — Considérons l'ensemble des couples  $(\mathrm{I}_{1},\mathrm{W}_{1})$  constitués d'un sous-groupe  $W_{1}$  de  $W \rtimes \Theta_{\rho}$  et d'un sous-groupe normal  $I_{1}$  de  $W_{1}$  et l'ordre partiel sur celui-ci défini par  $(\mathrm{I}_{1},\mathrm{W}_{1}) \leq (\mathrm{I}_{2},\mathrm{W}_{2})$  si et seulement si  $W_{1} \subset W_{2}$  et  $I_{1} \subset I_{2}$ . L'application  $\psi \mapsto (\mathrm{I}_{\psi},\mathrm{W}_{\psi})$  est alors une application croissante.

Démonstration. — Soit S = Spec(R) un trait formel de point générique  $\eta = \text{Spec}(k(\eta))$  et de point fermé  $s = \text{Spec}(k(s))$  géométrique. Soit  $\tilde{a}: S \to \tilde{A}$  un morphisme avec  $\tilde{a}(\eta) \in \tilde{\mathcal{A}}_{\psi}$  et  $\tilde{a}(s) \in \tilde{\mathcal{A}}_{\psi'}$ . On doit démontrer

$$
\left(\mathrm{I} _ {\psi^ {\prime}}, \mathrm{W} _ {\psi^ {\prime}}\right) \leq \left(\mathrm{I} _ {\psi}, \mathrm{W} _ {\psi}\right).
$$

Considérons le revêtement $\tilde{\mathbf{X}}_{\rho,a}$ de $\mathbf{X} \times \mathbf{S}$ qui est défini comme l'image réciproque par $a$ du revêtement $\mathbf{X}_{\rho} \times \mathbf{t}_{\mathrm{D}} \to \mathfrak{c}_{\mathrm{D}}$. Considérons la normalisation $\tilde{\mathbf{X}}_{\rho,a}^{\flat}$ de $\tilde{\mathbf{X}}_{\rho,a}$. Quitte à faire un changement radiciel du trait, on peut supposer que la fibre générique $(\tilde{\mathbf{X}}_{\rho,a}^{\flat})_{\eta}$ est une courbe lisse sur $k(\eta)$ de sorte qu'on peut calculer $(\mathrm{I}_{\psi}, \mathrm{W}_{\psi})$ à partir de cette fibre générique. En revanche, la fibre spéciale $(\tilde{\mathbf{X}}_{\rho,a}^{\flat})_s$ n'est pas normale en général et il faut prendre sa normalisation $(\tilde{\mathbf{X}}_{\rho,a}^{\flat})_s^{\flat}$ pour calculer $(\mathrm{I}_{\psi'}, \mathrm{W}_{\psi'})$.

Le point $\tilde{a}$ définit une section de $(\tilde{\mathrm{X}}_{\rho,a}^{\flat})_{\eta}$. Notons $\mathrm{C}_{\tilde{a}}$ la composante connexe de $(\tilde{\mathrm{X}}_{\rho,a}^{\flat})_{\eta}$ contenant cette section. Le groupe $\mathrm{W}_{\psi}$ est alors le sous-groupe de $\mathbf{W} \rtimes \Theta$ formé des éléments qui laissent stable cette composante. Soit $\mathrm{C}_{\tilde{a}(s)}$ la composante connexe de $(\tilde{\mathrm{X}}_{\rho,a}^{\flat})_{s}^{\flat}$ contenant le point définit par $\tilde{a}(s)$. Le groupe $\mathrm{W}_{\psi'}$ est le sous-groupe de $\mathbf{W} \rtimes \Theta$

formé des éléments qui laissent stable  $\mathrm{C}_{\tilde{a}(s)}$ . Comme  $\mathrm{C}_{\tilde{a}(s)}$  est une composante connexe de la normalisation de la fibre spéciale de  $C_{\tilde{a}}$ , on a l'inclusion  $W_{\psi'} \subset W_{\psi}$ . Un élément de  $W_{\psi'}$  ayant un point fixe dans  $\mathrm{C}_{\tilde{a}(s)}$  a nécessairement un point fixe dans  $C_{\tilde{a}}$  d'où la seconde inclusion  $I_{\psi'} \subset I_{\psi}$ .

5.4.6. — Pour tout couple  $(\mathrm{I}_{-},\mathrm{W}_{-})$  formé d'un sous-groupe  $W_{-}$  de  $W \times \Theta$  et d'un sous-groupe normal  $I_{-}$  de  $W_{-}$  contenu dans W, il résulte de ce lemme que la réunion des strates  $\tilde{A}_{\psi}$  telles que  $W_{\psi} \subset W_{-}$  et  $I_{\psi} \subset I_{-}$  est un sous-schéma fermé de  $\tilde{A}$ . Il en résulte aussi que la réunion des strates  $\tilde{A}_{\psi}$  telles que  $W_{\psi} = W_{-}$  et  $I_{\psi} = I_{-}$  est un ouvert du fermé ci-dessus mentionné. Nous noterons  $\tilde{\mathcal{A}}_{(\mathrm{I}_{-},\mathrm{W}_{-})}$  ce sous-schéma localement fermé de  $\tilde{A}$ . On a alors la stratification

$$
\tilde {\mathcal {A}} = \bigsqcup_ {(I _ {-}, W _ {-})} \tilde {\mathcal {A}} _ {(I _ {-}, W _ {-})}.
$$

Rappelons que si $\infty\in\mathbf{X}(k)$, $\tilde{\mathcal{A}}$ est défini sur $k$ mais la stratification ci-dessus n'est pas nécessairement définie sur $k$.

5.4.7. — Il résulte aussi du lemme 5.4.5 que la réunion des strates $\tilde{\mathcal{A}}_{\psi}$ avec $\psi \in \Psi$ tel que $\mathbf{t}^{\mathrm{W}_{\psi}} = 0$ est un ouvert de $\tilde{\mathcal{A}}$. D'après 4.10.3, un point $\tilde{a} = (a, \tilde{\infty}) \in \tilde{\mathcal{A}}(\bar{k})$ est dans cet ouvert si et seulement si $a$ appartient à l'ensemble $\mathcal{A}^{\mathrm{ani}}(\bar{k})$ défini dans 4.10.5. La stratification de $\tilde{\mathcal{A}}$ induit sur $\tilde{\mathcal{A}}^{\mathrm{ani}}$ une stratification

$$
\tilde {\mathcal {A}} ^ {\mathrm{ani}} = \bigsqcup_ {\psi \in \Psi^ {\mathrm{ani}}} \tilde {\mathcal {A}} _ {\psi}
$$

où $\Psi^{\mathrm{ani}}$ est un sous-ensemble de $\Psi$. Si $\infty \in \mathrm{X}(k)$, $\tilde{\mathcal{A}}^{\mathrm{ani}}$ est défini sur $k$ mais la stratification ci-dessus n'est pas nécessairement définie sur $k$.

Lemme 5.4.8. — Supposons que $\deg(\mathrm{D}) > 2g$. Soit $\psi_{\mathrm{G}}$ l'élément maximal de $\Psi$. On a alors

$$
(\mathrm{I} _ {\psi_ {\mathrm{G}}}, \mathrm{W} _ {\psi_ {\mathrm{G}}}) = (\mathbf {W}, \mathbf {W} \rtimes \Theta).
$$

Démonstration. — Par construction,  $W_{\psi} \subset W \rtimes \Theta$  et  $I_{\psi} \subset W$ . Il suffit donc de démontrer que cette borne est atteinte. On va démontrer qu'elle l'est en un point  $\tilde{a} = (a, \tilde{\infty})$  avec a dans l'ouvert  $A^{\diamond}$ . On a vu que celui-ci est non vide sous l'hypothèse  $\deg(D) > 2g$  cf. 4.7.1.

D'après cf. 4.7.5, on sait déjà que $W_{\tilde{a}} = \mathbf{W} \rtimes \Theta$ si $a \in \mathcal{A}^{\diamond}$. Le sous-groupe $I_{\tilde{a}}$ est alors un sous-groupe normal de $\mathbf{W}$. La courbe $\tilde{X}_{\rho,a}$ coupe transversalement tous les murs de $h_{\alpha}$ dans $X_{\rho} \times t$ associés aux racines $\alpha$ de $\mathbf{g}$, le groupe $I_{\tilde{a}}$ est un sous-groupe normal de $\mathbf{W}$ contenant toutes les réflexions $s_{\alpha}$ associées aux murs $h_{\alpha}$. Il s'ensuit que $I_{a} = \mathbf{W}$.

5.5. Description de $\pi_0(\mathcal{P})$. — Dans ce paragraphe, on va décrire le faisceau $\pi_0(\mathcal{P})$ le long des strates $\tilde{\mathcal{A}}_{(I-,W-)}$ de la stratification 5.4.6. Rappelons la définition de ce faisceau. Le champ de Picard $\mathcal{P} \to \mathcal{A}^{\heartsuit}$ étant lisse 4.3.5, il existe un unique faisceau $\pi_0(\mathcal{P})$ pour la topologie étale de $\mathcal{A}^{\heartsuit}$ tel que la fibre de $\pi_0(\mathcal{P})$ en un point $a \in \mathcal{A}^{\heartsuit}(\bar{k})$ est le groupe $\pi_0(\mathcal{P}_a)$ des composantes connexes de $\mathcal{P}_a$. Ceci est une conséquence d'un théorème de Grothendieck cf. [30, 15.6.4], voir aussi [57, 6.2].

On va aussi considérer le problème intermédiaire de déterminer le faisceau $\pi_0(\mathcal{P}')$ des composantes connexes du champ de Picard $\mathcal{P}'$ dont la fibre en chaque point $a \in \mathcal{A}^\heartsuit(\bar{k})$ classifie des $\mathrm{J}_a^0$ torseurs sur $\bar{\mathrm{X}}$. L'homomorphisme surjectif $\mathcal{P}' \to \mathcal{P}$ induit un homomorphisme surjectif $\pi_0(\mathcal{P}') \to \pi_0(\mathcal{P})$. Notons $\tilde{\mathcal{P}}$ et $\tilde{\mathcal{P}}'$ les restrictions de $\mathcal{P}$ et $\mathcal{P}'$ à $\tilde{\mathcal{A}}$.

D'après 4.10.3, pour tout point $\tilde{a} \in \tilde{\mathcal{A}}(\bar{k})$, la fibre de $\pi_0(\mathcal{P}_{\tilde{a}}')$ admet la description

$$
\pi_ {0} (\mathcal {P} _ {a} ^ {\prime}) = (\hat {\mathbf {T}} ^ {\mathrm{W} _ {\tilde {a}}}) ^ {*}
$$

où l'exposant $(\_)^{*}$ désigne la dualité entre les groupes abéliens de type fini et les groupes diagonalisables de type fini sur $\bar{\mathbf{Q}}_{\ell}$. De même, $\pi_0(\mathcal{P}_a)$ s'identifie au quotient de $\pi_0(\mathcal{P}_a')$ dual au sous-groupe $\hat{\mathbf{T}}(\mathrm{I}_{\tilde{a}},\mathrm{W}_{\tilde{a}})$ défini dans 4.10.3. L'énoncé suivant permet de déterminer complètement les faisceaux $\pi_0(\tilde{\mathcal{P}}')$ et $\pi_0(\tilde{\mathcal{P}})$.

Proposition 5.5.1. — Les flèches surjectives de la proposition 4.10.3

$$
\mathbf {X} _ {*} \rightarrow \pi_ {0} (\mathcal {P} _ {a} ^ {\prime}) = (\mathbf {X} _ {*}) _ {\mathrm{W} _ {\tilde {a}}}
$$

définies pour tout $\tilde{a} = (a, \tilde{\infty}) \in \tilde{\mathcal{A}}(\bar{k})$ s'interpolent en un homomorphisme surjectif canonique du faisceau constant $\mathbf{X}_*$ dans $\pi_0(\tilde{\mathcal{P}}')$.

Démonstration. — Soit $\tilde{a} = (a, \tilde{\infty}) \in \tilde{\mathcal{A}}(\bar{k})$. Le point géométrique $\tilde{\infty}_{\rho} = (\tilde{\infty}, \infty_{\rho})$ de $\tilde{\mathrm{X}}_{\rho,a}$ permet d'identifier la fibre de $\mathrm{J}_a$ en $\infty$ avec le tore fixe $\mathbf{T}$ cf. 2.4.7. D'après [57, 6.8], cette identification définit un homomorphisme du faisceau constant $\mathbf{X}_*$ dans $\tilde{\mathcal{P}}'$ et donc un homomorphisme

$$
\mathbf {X} _ {*} \times \tilde {\mathcal {A}} \rightarrow \pi_ {0} (\tilde {\mathcal {P}} ^ {\prime}).
$$

Fibre par fibre c'est l'homomorphisme surjectif de 4.10.3.

5.5.2. — A l'aide de ce lemme, on obtient une description explicite des restrictions de  $\pi_{0}(\mathcal{P}')$  et de  $\pi_{0}(\mathcal{P})$  à  $\tilde{A}$ . Pour tout ouvert étale U de  $\tilde{A}$ , la stratification 5.4.6 induit sur U une stratification

$$
\mathrm{U} = \bigsqcup_ {(\mathrm{I} _ {-}, \mathrm{W} _ {-})} \mathrm{U} _ {(\mathrm{I} _ {-}, \mathrm{W} _ {-})}.
$$

Pour tout couple  $(\mathrm{I}_{1},\mathrm{W}_{1})$  formé d'un sous-groupe  $W_{1}$  de  $W\times\Theta$  et d'un sous-groupe normal  $I_{1}$  de  $W_{1}$, U sera dit un petit ouvert de type  $(\mathrm{I}_{1},\mathrm{W}_{1})$  si  $\mathrm{U}_{(\mathrm{I}_{1},\mathrm{W}_{1})}$  est l'unique strate fermée non vide dans la stratification ci-dessus. Il est clair que les petits ouverts de différents types forment une base de la topologie étale de  $\tilde{A}$  dans le sens que tout ouvert peut être recouvert par une famille de petits ouverts. Pour définir un faisceau pour la topologie étale de  $\tilde{A}$, il suffit donc de spécifier ses sections sur les petits ouverts et les flèches de transition.

Considérons les faisceaux $\Pi'$ et $\Pi$ qui sont des quotients du faisceau constant $\mathbf{X}_{*}$ définis comme suit. Pour un petit ouvert $\mathrm{U}_{1}$ de type $(\mathrm{I}_{1},\mathrm{W}_{1})$, on pose

$$
\begin{array}{l} \Gamma (\mathrm{U}, \Pi^ {\prime}) = (\hat {\mathbf {T}} ^ {\mathrm{W} _ {1}}) ^ {*} = (\mathbf {X} _ {*}) _ {\mathrm{W} _ {1}} \\ \Gamma (\mathrm{U}, \Pi) = \hat {\mathbf {T}} (\mathrm{I} _ {1}, \mathrm{W} _ {1}) ^ {*}. \end{array}
$$

Soit  $U_{2}$  un petit ouvert étale de  $U_{1}$  de type  $(I_{2}, W_{2})$ . Puisque  $U_{(I_{1}, W_{1})}$  est l'unique strate fermée non vide de  $U_{1}$ , on a l'inégalité

$$
\left(\mathrm{I} _ {1}, \mathrm{W} _ {1}\right) \leq \left(\mathrm{I} _ {2}, \mathrm{W} _ {2}\right).
$$

On a alors une inclusion évidente des sous-groupes des invariants de $\hat{\mathbf{T}}$ sous $\mathrm{W}_1$ et $\mathrm{W}_2$

$$
\hat {\mathbf {T}} ^ {W _ {2}} \subset \hat {\mathbf {T}} ^ {W _ {1}}
$$

d'où la flèche de transition

$$
\Gamma (\mathrm{U} _ {1}, \Pi^ {\prime}) \rightarrow \Gamma (\mathrm{U} _ {2}, \Pi^ {\prime}).
$$

La définition des flèches de transition du faisceau  $\Pi$  résulte du lemme suivant.

Lemme 5.5.3. — Si (I$_{1}$, W$_{1}$) ≤ (I$_{2}$, W$_{2}$), on a l'inclusion

$$
\hat {\mathbf {T}} \left(\mathrm{I} _ {2}, \mathrm{W} _ {2}\right) \subset \hat {\mathbf {T}} \left(\mathrm{I} _ {1}, \mathrm{W} _ {1}\right).
$$

Démonstration. — Soient $\kappa$ un élément de $\hat{\mathbf{T}}$, $\hat{\mathbf{G}}_{\kappa}$ son centralisateur dans $\hat{\mathbf{G}}$ et $\hat{\mathbf{H}}$ la composante neutre de celui-ci. Soient $(\mathbf{W} \rtimes \Theta)_{\kappa}$ le centralisateur de $\kappa$ dans $\mathbf{W} \rtimes \Theta$ et $\mathbf{W}_{\mathbf{H}}$ le groupe de Weyl de $\hat{\mathbf{H}}$. Si $\kappa \in \hat{\mathbf{T}}(\mathrm{I}_2, \mathrm{W}_2)$ alors $\mathrm{I}_2 \subset \mathbf{W}_{\mathbf{H}}$ et $\mathrm{W}_2 \subset (\mathbf{W} \rtimes \Theta)_{\kappa}$. On en déduit que $\mathrm{I}_1 \subset \mathbf{W}_{\mathbf{H}}$ et $\mathrm{W}_1 \subset (\mathbf{W} \rtimes \Theta)_{\kappa}$.

L'énoncé suivant est une conséquence immédiate de 5.5.1 et 4.10.3.

Corollaire 5.5.4. — L'homomorphisme surjectif 5.5.1 induit par passage au quotient des isomorphismes $\pi_0(\mathcal{P}')|_{\tilde{\mathcal{A}}} = \Pi'$ et $\pi_0(\mathcal{P})|_{\tilde{\mathcal{A}}} = \Pi$.

Au-dessus de l'ouvert $\tilde{\mathcal{A}}^{\mathrm{ani}}$ de $\tilde{\mathcal{A}}$ cf. 5.4.7, ce sont des faisceaux en groupes abéliens finis.

5.6. Stratification à δ constant. — Pour tout  $a \in \mathcal{A}^{\heartsuit}(\bar{k})$ , on a défini dans 4.9 un entier  $\delta(a)$ . Ceci induit une fonction  $\tilde{a} \mapsto \delta(a)$  pour  $\tilde{a} = (a, \tilde{\infty}) \in \tilde{\mathcal{A}}(\bar{k})$ .

Lemme 5.6.1. — La fonction $\tilde{a} \mapsto \delta(a)$ est constante sur chaque strate $\tilde{\mathcal{A}}_{\psi}$ pour tout $\psi \in \Psi$.

Démonstration. — Après le changement de base fini radiciel, $\tilde{\mathcal{B}}_{\psi} \to \tilde{\mathcal{A}}_{\psi}$, la restriction de la courbe camérale à $\tilde{\mathcal{B}}_{\psi}$ admet une normalisation en famille. Notons $\pi_{\psi}: \tilde{\mathrm{X}}_{\psi} \to \tilde{\mathcal{B}}_{\psi}$ la restriction de la courbe camérale à $\tilde{\mathcal{B}}_{\psi}$ et $\xi: \tilde{\mathrm{X}}_{\psi}^{\flat} \to \tilde{\mathrm{X}}_{\psi}$ la normalisation en famille. D'après 5.1.2 le faisceau

$$
\pi_ {\psi , *} (\xi_ {*} \mathcal {O} _ {\tilde {\mathrm{X}} _ {\psi} ^ {\flat}} / \mathcal {O} _ {\tilde {\mathrm{X}} _ {\psi}})
$$

est un $\mathcal{O}_{\tilde{\mathcal{B}}_{\psi}}$-module localement constant de type fini. Ce module est muni d'une action de W. Puisque l'ordre de $\mathbf{W}$ est premier à la caractéristique

$$
(\mathcal {O} _ {\tilde {\mathcal {B}} _ {\psi}} \otimes \mathfrak {t}) ^ {W}
$$

est également localement constant. On conclut par la formule 4.9.4.

## 5.6.2. — On en déduit une application

$$
\delta : \Psi \to \mathbf {N}
$$

dans N tel que pour tout  $\tilde{a}=(a,\tilde{\infty})\in\tilde{\mathcal{A}}_{\psi}(\bar{k})$ , on a  $\delta_{a}=\delta(\psi)$ . Cette fonction est décroissante c'est-à-dire si  $\psi\geq\psi'$ , on a  $\delta(\psi)\leq\delta(\psi')$ . Il s'agit d'un cas particulier de l'énoncé bien connu sur les schémas en groupes lisses commutatifs. On ne peut pas l'appliquer directement à P qui n'est pas un schéma en groupes mais un champ de Picard. Néanmoins, il s'applique si on considère le champ des  $J_{a}$ -torseurs munis d'une trivialisation au point  $\infty$ . La propriété de décroissance de  $\psi\mapsto\delta(\psi)$  s'en déduit.

Lemme 5.6.3. — Soit P → S un schéma en groupes lisse commutatif de type fini. La fonction  $s \mapsto \tau_{s}$  qui associe à un point géométrique s la dimension de la partie abélienne de  $P_{s}$  est une fonction semi-continue inférieurement. Inversement, la fonction  $s \mapsto \delta_{s}$  qui associe à un point géométrique s la dimension de la partie affine de  $P_{s}$  est une fonction semi-continue supérieurement.

Démonstration. — On peut supposer que P n'a que des fibres connexes. On peut aussi supposer que S est strictement hensélien. Choissons un nombre premier  $\ell$  premier à la caractéristique résiduelle de S. Le noyau P[ $\ell$ ] de la multiplication par  $\ell$  est représentable par un sous-schéma en groupes étale et quasi fini. Pour tout point géométrique s de S, la longueur de P $_{s}$ [ $\ell$ ] est donnée par la formule

$$
\mathrm{lg} (\mathrm{P} _ {s} [ \ell ]) = \mu_ {s} \ell + \tau_ {s} \ell^ {2}
$$

où $\mu_{s}$ est la dimension de la partie multiplicative de $\mathrm{P}_{s}$, $\tau_{s}$ est la dimension de sa partie abélienne. Si $s_{0}$ désigne le point fermé géométrique de S et $s_{1}$ le point générique géométrique, on a l'inégalité

$$
\lg \left(\mathrm{P} _ {s _ {0}} [ \ell ]\right) \leq \lg \left(\mathrm{P} _ {s _ {1}} [ \ell ]\right)
$$

puisque P[ℓ] étant étale au-dessus de la base hensélienne S, tout point dans la fibre spéciale s'étend en une S-section. L'inégalité

$$
\mu_ {s _ {0}} \ell + \tau_ {s _ {0}} \ell^ {2} \leq \mu_ {s _ {1}} \ell + \tau_ {s _ {1}} \ell^ {2}
$$

étant vraie pour tout nombre premier $\ell$ premier à la caractéristique résiduelle de S, on a

$$
\tau_ {s _ {0}} \leq \tau_ {s _ {1}}.
$$

L'autre inégalité s'en déduit car $\delta_{s} + \tau_{s} = \dim(P_{s})$ ne dépend pas du point $s$.

Lemme 5.6.4. — Supposons que $\deg(\mathrm{D}) > 2g$. Alors $\delta(\psi_{\mathrm{G}}) = 0$ où $\psi_{\mathrm{G}}$ est l'élément maximal de $\Psi$.

Démonstration. — C'est immédiat à partir de 4.9.4.

5.6.5. — Il résulte de 5.6.2 que pour tout entier $\delta \in \mathbf{N}$, la réunion des strates $\tilde{\mathcal{A}}_{\psi}$ avec $\psi \in \Psi$ tel que $\delta(\psi) \geq \delta$ est un fermé de $\tilde{\mathcal{A}}$. Il s'ensuit que

$$
\tilde {\mathcal {A}} _ {\delta} = \bigsqcup_ {\delta (\psi) = \delta} \tilde {\mathcal {A}} _ {\psi}
$$

est un ouvert dans le sous-schéma fermé ci-dessus mentionné. C'est donc un sous-schéma localement fermé de $\tilde{\mathcal{A}}$. On obtient ainsi une stratification

$$
\tilde {\mathcal {A}} = \bigsqcup_ {\delta \in \mathbf {N}} \tilde {\mathcal {A}} _ {\delta}
$$

appelée la stratification à δ constant.

5.6.6. — On en déduit une stratification sur l'ouvert  $\tilde{A}^{ani}$

$$
\tilde {\mathcal {A}} ^ {\mathrm{ani}} = \bigsqcup_ {\delta \in \mathbf {N}} \tilde {\mathcal {A}} _ {\delta} ^ {\mathrm{ani}}.
$$

Notons que pour tout $\tilde{a} = (a, \tilde{\infty}) \in \tilde{\mathcal{A}}_{\delta}^{\mathrm{ani}}(\bar{k})$, d'après 4.9.3, la dimension de la partie affine de $\mathcal{P}_a^0$ vaut $\delta$.

5.7. Stratification par les valuations radicielles. — Soit  $\bar{v}$  un point géométrique de  $\bar{X}$  et notons  $\bar{\mathcal{O}}_{\bar{v}}$  la complétion de  $\bar{X}$  en  $\bar{v}$  et  $\bar{F}_{\bar{v}}$  son corps des fractions. En choisissant un uniformisant  $\varepsilon_{\bar{v}}$ , on peut identifier  $\bar{\mathcal{O}}_{\bar{v}}$  avec l'anneau  $\bar{k}[[\varepsilon_{\bar{v}}]]$ . Nous choisissons une trivialisation de la restriction  $\rho_{G}$  à  $\bar{\mathcal{O}}_{\bar{v}}$  qui déploie G et qui fournit en particulier un isomorphisme W = W.

Nous allons passer brièvement en revue l'analyse [28] de la stratification de $\mathfrak{c}^{\heartsuit}(\mathcal{O}_{\bar{v}})$ par les valuations radicielles, due à Goresky, Kottwitz et MacPherson. Leurs strates de valuations radicielles sont plus fines que nos strates définies par les normalisations en familles et a fortiori plus fines que les strates à $\delta$ constant.

Soient $a \in \mathfrak{c}^{\heartsuit}(\bar{\mathcal{O}}_{\bar{v}})$ et $J_a = a^* J$ le schéma en groupes lisse sur $\bar{\mathcal{O}}_{\bar{v}}$ qui s'en déduit. La fibre générique de $J_a$ est un tore dont la monodromie peut être décrite à l'aide du revêtement caméral cf. 2.4.7. Soit $\bar{\mathrm{F}}_{\bar{v}}^{\mathrm{sep}}$ la clôture séparable de $\bar{\mathrm{F}}_{\bar{v}}$. Soit $x \in \mathfrak{t}(\bar{\mathrm{F}}_{\bar{v}}^{\mathrm{sep}})$ un $\bar{\mathrm{F}}_{\bar{v}}^{\mathrm{sep}}$-point de $\mathfrak{t}$ d'image $a \in \mathfrak{c}(\bar{\mathrm{F}}_{\bar{v}})$. Le choix de ce point définit un homomorphisme

$$
\pi_ {a} ^ {\bullet}: \mathrm{I} _ {\bar {v}} \to \mathbf {W}
$$

où  $\mathrm{I}_{\bar{v}}=\mathrm{Gal}(\bar{\mathrm{F}}_{\bar{v}}^{\mathrm{sep}}/\bar{\mathrm{F}}_{\bar{v}})$ . Puisque la caractéristique de k ne divise par l'ordre de W,  $\pi_{a}^{\bullet}$  se factorise par le quotient modéré  $I_{\bar{v}}^{tame}$  de  $I_{\bar{v}}$ . Pour adhérer aux notations de [28], choisissons un générateur topologique de  $I_{\bar{v}}^{tame}$  et notons  $w_{a}$  l'image de ce générateur par  $\pi_{a}^{\bullet}$ .

Pour toute racine $\alpha\in\Phi$, on a un entier

$$
r (\alpha) := \operatorname{val} _ {\bar {v}} (\alpha (x))
$$

où val$_{\bar{v}}$ est l'unique prolongement de la valuation val$_{\bar{v}}(\varepsilon_{\bar{v}}) = 1$ sur $\bar{\mathrm{F}}_{\bar{v}}$ à $\bar{\mathrm{F}}_{\bar{v}}^{\mathrm{sep}}$. On obtient ainsi une fonction $r: \Phi \to \mathbf{Q}_{+}$.

Le couple  $(w_{a}, r)$  dépend du choix de x mais l'orbite sous W de ce couple n'en dépend pas. Nous allons noter  $[w_{a}, r]$  l'orbite sous W du couple  $(w_{a}, r)$ .

On a l'égalité évidente

$$
\sum_ {\alpha \in \Phi} r (\alpha) = \deg_ {\bar {v}} (a ^ {*} \mathfrak {D} _ {\mathrm{G}}) = d _ {\bar {v}} (a).
$$

L'invariant

$$
c _ {\bar {v}} (a) = \dim (\mathbf {t}) - \dim (\mathbf {t} ^ {w _ {a}})
$$

est la chute du rang torique du modèle de Néron de  $J_{a}$ . D'après la formule de Bezrukavnikov, on a

$$
\delta_ {\bar {v}} (a) = \frac {d _ {\bar {v}} (a) - c _ {\bar {v}} (a)}{2}.
$$

Soit $\mathfrak{c}^{\heartsuit}(\mathcal{O}_{\bar{v}})_{[w,r]}$ le sous-ensemble des $a\in \mathfrak{c}^{\heartsuit}(\mathcal{O}_{\bar{v}})$ avec l'invariant $[w,r]$ donné. D'après [28], cet ensemble est admissible c'est-à-dire il existe un entier N et un sous-schéma localement fermé Z de $\mathfrak{c}(\mathcal{O}_{\bar{v}} / \varepsilon_{\bar{v}}^{\mathrm{N}}\mathcal{O}_{\bar{v}})$ vu comme $\bar{k}$-schéma tel que $\mathfrak{c}^{\heartsuit}(\mathcal{O}_{\bar{v}})_{[w,r]}$

soit l'image réciproque de  $Z(\bar{k})$  par l'application  $\mathfrak{c}(\mathcal{O}_{\bar{v}})\to\mathfrak{c}(\mathcal{O}_{\bar{v}}/\varepsilon_{\bar{v}}^{\mathrm{N}}\mathcal{O}_{\bar{v}})$ . On dira que  $\mathfrak{c}^{\heartsuit}(\mathcal{O}_{\bar{v}})_{[w,r]}$  est admissible d'échelon N.

Ils définissent alors la codimension de la strate $\mathfrak{c}^{\heartsuit}(\mathcal{O}_{\bar{v}})_{[w,r]}$ comme la codimension de $Z$ dans $\mathfrak{c}(\mathcal{O}_{\bar{v}} / \varepsilon_{\bar{v}}^{\mathrm{N}}\mathcal{O}_{\bar{v}})$ vue comme $\bar{k}$-schémas. Cette codimension ne dépend visiblement pas de l'échelon N choisi pourvu que celui-ci soit assez grand. Notons $\operatorname{codim}[w,r]$ cette codimension. D'après [28, 8.2.2] on a la formule explicite

$$
\operatorname{codim} [ w, r ] = d (w, r) + \frac {d _ {\bar {v}} (a) + c _ {\bar {v}} (a)}{2}
$$

où l'entier $d(w,r)$ est la codimension de $\mathfrak{t}_{w}(\mathcal{O})_{r}$ dans $\mathfrak{t}_{w}(\mathcal{O})$ dans les notations de loc. cit. Nous nous contenterons d'une estimation plus grossière.

Proposition 5.7.1. — Si $\delta_{a}>0$, on a l'inégalité

$\operatorname{codim}[w, r] \geq \delta_a + 1$.

Démonstration. — Il est clair que

$$
\operatorname{codim} [ w, r ] = \delta_ {\bar {v}} (a) + c _ {\bar {v}} (a) + d (w, r)
$$

où $\delta_{\bar{v}}(a) = (d_{\bar{v}}(a) - c_{\bar{v}}(a))/2$. Si $w$ n'est pas l'élément trivial de W, on a $c_{\bar{v}}(a) \geq 1$. Si $w = 1$, par définition de [28, 8.2.2], $d(w, r)$ est la codimension de $\mathfrak{t}(\bar{\mathcal{O}}_{\bar{v}})_r$ dans $\mathfrak{t}(\bar{\mathcal{O}}_{\bar{v}})$ où $\mathfrak{t}(\bar{\mathcal{O}}_{\bar{v}})_r$ est la partie admissible de $\mathfrak{t}(\bar{\mathcal{O}}_{\bar{v}})$ constituée des éléments ayant la valuation radicielle $r$. Si $\delta_{\bar{v}}(a) > 0$, alors $r \neq 0$ de sorte que cette partie est de codimension strictement positive. Donc $d(w, r) \geq 1$. Dans les deux cas, on obtient donc l'inégalité qu'on voulait. $\square$

Proposition 5.7.2. — Pour un groupe G fixé, pour tout $\delta \in \mathbf{N}$, il existe un entier N dépendant de G et de $\delta$ tel que si $\deg(\mathrm{D}) > \mathrm{N}$, la strate à $\delta$ constant $\mathcal{A}_{\delta}$ est de codimension plus grande ou égale à $\delta$.

Démonstration. — Pour toute partition  $\delta_{\bullet}$  de  $\delta$  en une somme d'entiers naturels  $\delta = \delta_{1} + \cdots + \delta_{n}$ , considérons le sous-schéma  $Z_{\delta_{\bullet}}$  de  $A^{\heartsuit} \times X^{j}$  qui consiste en les uplets  $(a; x_{1}, \ldots, x_{n})$  avec  $a \in \mathcal{A}^{\heartsuit}(\bar{k})$  et  $x_{1}, \ldots, x_{n} \in \mathrm{X}(\bar{k})$  tels que l'invariant  $\delta$  local  $\delta_{x_{i}}(a)$  vaut  $\delta_{i}$ . On peut stratifier  $Z_{\delta_{\bullet}}$  en réunion des strates  $Z_{[w_{\bullet}, r_{\bullet}]}$  des  $(a; x_{1}, \ldots, x_{n})$  tels que l'image de a dans  $\mathfrak{c}^{\heartsuit}(\bar{\mathcal{O}}_{x_{i}})$  soit dans la strate de valuation radicielle  $\mathfrak{c}^{\heartsuit}(\bar{\mathcal{O}}_{x_{i}})_{[w_{i}, r_{i}]}$ . Supposons que cette strate est admissible d'échelon  $N_{i}$ . Si deg(D) est grand par rapport à  $\delta$ , l'application linéaire

$$
\mathcal {A} \longrightarrow \prod_ {i = 1} ^ {n} \mathfrak {c} (\bar {\mathcal {O}} _ {x _ {i}} / \varepsilon^ {\mathrm{N} _ {i}} \bar {\mathcal {O}} _ {x _ {i}})
$$

$$
\sum_ {i = 1} ^ {n} (\delta_ {i} + 1)
$$

est surjective. Il s'ensuit que  $Z_{[w_{\bullet},r_{\bullet}]}$  est de codimension au moins égale à

dans $\mathcal{A} \times \mathrm{X}^n$. Il s'ensuit que son image dans $\mathcal{A}$ est de codimension au moins égale à $\delta = \sum_{i=1}^{n} \delta_i$. La proposition s'en déduit.

On pense que cette inégalité est valide sans l'hypothèse que deg(D) soit très grand par rapport à $\delta$. Un calcul de l'action infinitésimale de $\mathcal{P}_a$ sur $\mathcal{M}_a$ montre que c'est vrai en caractéristique zéro, voir cf. [60, p. 4].

## 6. Cohomologie au-dessus de l'ouvert anisotrope

Dans ce chapitre, nous allons énoncer les théorèmes de stabilisation géométrique 6.4.1 et 6.4.2. Il s'agit d'une description endoscopique d'une composante isotypique des faisceaux pervers de cohomologie de l'image directe

$$
{ } ^ { p } \mathrm{H} ^ { n } ( \tilde { f } _ { * } ^ { \text {   a   n   i   } } \bar { \mathbf { Q } } _ { \ell } )
$$

par rapport à l'action de $\pi_0(\tilde{\mathcal{P}}^{\mathrm{ani}})$. Bien que l'énoncé 6.4.2 implique le lemme fondamental de Langlands et Shelstad 1.11.1, la démonstration de 1.11.1 forme une étape de celle de 6.4.2.

6.1. L'ouvert anisotrope. — En faisant varier le point $\infty$, il résulte de 5.4.7 et de 5.5.4 qu'il existe un ouvert $\mathcal{A}^{\mathrm{ani}}$ de $\mathcal{A}^{\heartsuit}$ dont les points sont $a \in \mathcal{A}^{\mathrm{ani}}$ si et seulement si le groupe des composantes connexes $\pi_0(\mathcal{P}_a)$ est fini. Il résulte de 4.11.2 que pour tout $a \in \mathcal{A}^{\mathrm{ani}}(\bar{k})$ et $(\mathrm{E}, \phi) \in \mathcal{M}_a(\bar{k})$, $\operatorname{Aut}(\mathrm{E}, \phi)$ est un groupe fini réduit sous l'hypothèse que l'ordre de $\mathbf{W} \rtimes \Theta$ est premier à la caractéristique.

6.1.1. — Dans [24, II.4], Faltings a démontré le théorème de réduction semistable pour les fibrés de Higgs qui dit qu'un fibré de Higgs semi-stable sur X à coefficients dans le corps des fractions d'un anneau de valuation discrète peut s'étendre en un fibré de Higgs sur l'anneau après une extension finie séparable et de plus, si le fibré de Higgs dans la fibre spéciale est stable, cette extension est unique. Nous renvoyons à [24] pour la définition des fibrés de Higgs semi-stables et stables. Disons seulement que c'est exactement la même définition que pour les G-torseurs sauf qu'on ne considère que les réductions paraboliques de E compatibles avec le champ de Higgs $\phi$. Ceci suffit pour démontrer le lemme suivant.

$$
L e m m e \mathbf {6 . 1 . 2 .} - S o i e n t a \in \mathcal {A} ^ {\mathrm{ani}} (\bar {k}) e t (\mathrm{E}, \varphi) \in \mathcal {M} ^ {\mathrm{ani}} (\bar {k}). A l o r s (\mathrm{E}, \phi) e s t s t a b l e.
$$

Démonstration. — Puisque  $a \in \mathcal{A}^{\mathrm{ani}}(\bar{k})$ , E n'a pas de réduction parabolique compatible à  $\phi$ .

On peut maintenant appliquer les résultats de Faltings dans [24] pour avoir l'énoncé suivant.

Proposition 6.1.3. — La restriction $\mathcal{P}^{\mathrm{ani}}$ du champ de Picard $\mathcal{P}$ à $\mathcal{A}^{\mathrm{ani}}$ est un champ de Deligne-Mumford séparé lisse de type fini au-dessus de $\mathcal{A}^{\mathrm{ani}}$. L'ouvert $\mathcal{M}^{\mathrm{ani}} := \mathcal{M} \times_{\mathcal{A}} \mathcal{A}^{\mathrm{ani}}$ de $\mathcal{M}$ est un champ de Deligne-Mumford séparé lisse de type fini au-dessus de $k$.

De plus, il existe un espace de module grossier  $M^{ani}$  tel que le morphisme  $f^{ani}: M^{ani} \to A^{ani}$  se factorise en un homéomorphisme  $M^{ani} \to M^{ani}$  suivi d'un morphisme projectif  $M^{ani} \to A^{ani}$ .

Démonstration. — On sait déjà que P est un champ de Picard lisse au-dessus de  $A^{\heartsuit}$  cf. 4.3.5 et M est lisse sur k cf. 4.14.1.

D'après [24, II.4] et 6.1.2, $\mathcal{M}^{\mathrm{ani}}$ est séparé. Autrement dit le morphisme diagonal de $\mathcal{M}^{\mathrm{ani}}$ est universellement fermé. On sait qu'il est quasi-fini et de fibres réduites. On en déduit qu'il est fini et non ramifié. Par conséquent $\mathcal{M}^{\mathrm{ani}}$ est un champ de Deligne-Mumford séparé. Il en est de même de $\mathcal{P}^{\mathrm{ani}}$ car $\mathcal{P}^{\mathrm{ani}}$ s'identifie à un ouvert de $\mathcal{M}^{\mathrm{ani}}$.

Il reste à démontrer que $\mathcal{P}$ est de type fini et $\mathcal{M}$ est propre sur $\mathcal{A}^{\mathrm{ani}}$. Disposant du critère valuatif de propreté cf. [24, II.4], il suffit de démontrer qu'il est de type fini sur $\mathcal{A}^{\mathrm{ani}}$. On sait que $\mathcal{M}$ est localement de type fini. Pour tout $a \in \mathcal{A}^{\mathrm{ani}}(\bar{k})$, on peut choisir une famille d'ouverts de type fini de $\mathcal{M}^{\mathrm{ani}}$ qui recouvrent la fibre $\mathcal{M}^{\mathrm{ani}}$. D'après la formule de produit 4.15.1, la fibre $\mathcal{M}_a$ est noethérienne si bien qu'il existe une famille finie d'ouverts de type fini de $\mathcal{M}^{\mathrm{ani}}$ qui recouvre $\mathcal{M}_a$. Puisque $f: \mathcal{M}^{\mathrm{ani}} \to \mathcal{A}^{\mathrm{ani}}$ est plat, l'image de ceux-ci sont des ouverts de $\mathcal{A}^{\mathrm{ani}}$ contenant $a$. Si on note $\mathrm{V}_a$ leur intersection, l'ouvert $f^{-1}(\mathrm{V}_a)$ de $\mathcal{M}^{\mathrm{ani}}$ peut être recouvert par une famille finie d'ouverts de type fini. Il reste à remarquer que $\mathcal{A}^{\mathrm{ani}}$ est aussi noethérien de sorte qu'il existe un nombre fini de points $a$ tels que les ouverts $\mathrm{V}_a$ comme ci-dessus recouvrent $\mathcal{A}^{\mathrm{ani}}$. La proposition s'en déduit.

L'assertion sur l'espace de module grossier se déduit maintenant de [24, II.5] et [61].

6.2. La $\kappa$-décomposition sur $\tilde{\mathcal{A}}^{\mathrm{ani}}$. — Rappelons les notations $\tilde{\mathcal{M}}^{\mathrm{ani}} = \mathcal{M} \times_{\mathcal{A}} \tilde{\mathcal{A}}^{\mathrm{ani}}$, $\tilde{\mathcal{P}}^{\mathrm{ani}} = \mathcal{P} \times_{\mathcal{A}} \tilde{\mathcal{A}}^{\mathrm{ani}}$ et $\tilde{f}^{\mathrm{ani}}: \tilde{\mathcal{M}}^{\mathrm{ani}} \to \tilde{\mathcal{P}}^{\mathrm{ani}}$. D'après 6.1.3, ce morphisme est propre et sa source est un champ de Deligne-Mumford lisse. D'après le théorème de pureté de Deligne [18], $\tilde{f}_{*}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell}$ est un complexe pur. D'après [7, 5.4.5], au-dessus de $\tilde{\mathcal{A}}^{\mathrm{ani}}$ il est isomorphe à la somme directe de ses faisceaux pervers de cohomologie

$$
\tilde {f} _ {*} ^ {\mathrm{ani}} \bar {\mathbf {Q}} _ {\ell} \simeq \bigoplus_ {n} ^ {p} \mathrm{H} ^ {n} (\tilde {f} _ {*} ^ {\mathrm{ani}} \bar {\mathbf {Q}} _ {\ell}) [ - n ]
$$

$\mathrm{ou}^p\mathrm{H}^n (\tilde{f}_*^{\mathrm{ani}}\bar{\mathbf{Q}}_\ell)$ est un faisceau pervers pur de poids $n$.

6.2.1. — Puisque  $\tilde{P}^{ani}$  agit sur  $\tilde{M}^{ani}$  au-dessus de  $\tilde{A}^{ani}$ ,  $\tilde{P}^{ani}$  agit sur l'image directe  $\tilde{f}_{*}^{ani}\bar{\mathbf{Q}}_{\ell}$ . D'après le lemme d'homotopie cf. [54, 3.2.3], l'action de  $\tilde{P}^{ani}$  sur les faisceaux pervers de cohomologie  $^{p}\mathrm{H}^{n}(f_{*}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})$  se factorise par le faisceau en groupes abéliens finis  $\pi_{0}(\tilde{\mathcal{P}}^{\mathrm{ani}})$ . D'après 5.5.1, on a un homomorphisme surjectif

$$
\mathbf {X} _ {*} \times \tilde {\mathcal {A}} ^ {\mathrm{ani}} \to \pi_ {0} (\tilde {\mathcal {P}} ^ {\mathrm{ani}})
$$

qui identifie $p_0(\tilde{\mathcal{P}}^{\mathrm{ani}})$ à un quotient fini explicite du faisceau constant $\mathbf{X}_*$. En particulier, pour tout $\kappa \in \hat{\mathbf{T}}$, on peut définir un facteur direct $^p\mathrm{H}^n (\tilde{f}_*^{\mathrm{ani}}\bar{\mathbf{Q}}_\ell)_\kappa$ sur lequel $\mathbf{X}_*$ agit à travers le caractère $\kappa : \mathbf{X}_* \to \bar{\mathbf{Q}}_\ell^\times$ de sorte qu'il y ait une décomposition en somme directe

$$
{ } ^ { p } \mathrm{H} ^ { n } ( \tilde { f } _ { * } ^ { \text {   a   n   i   } } \bar { \mathbf { Q } } _ { \ell } ) _ { \kappa } = \bigoplus _ { \kappa \in \hat { \mathbf { T } } } { } ^ { p } \mathrm{H} ^ { n } ( \tilde { f } _ { * } ^ { \text {   a   n   i   } } \bar { \mathbf { Q } } _ { \ell } ) _ { \kappa }
$$

n'ayant qu'un nombre fini de facteurs non nuls.

6.2.2. — Rappelons qu'on a une stratification $\tilde{\mathcal{A}}^{\mathrm{ani}} = \bigsqcup_{\psi \in \Psi^{\mathrm{ani}}} \tilde{\mathcal{A}}_{\psi}$ cf. 5.4.7. Pour tout $\kappa \in \hat{\mathbf{T}}$, la réunion des strates $\tilde{\mathcal{A}}_{\psi}$ avec $\psi \in \Psi$ tel que $\kappa \in \hat{\mathbf{T}}(\mathrm{I}_{\psi}, \mathrm{W}_{\psi})$ est un fermé de $\tilde{\mathcal{A}}$ d'après 5.5.3 et 5.4.5. Notons $\tilde{\mathcal{A}}_{\kappa}^{\mathrm{ani}} = \tilde{\mathcal{A}}_{\kappa} \cap \tilde{\mathcal{A}}^{\mathrm{ani}}$ la trace de ce fermé sur $\tilde{\mathcal{A}}^{\mathrm{ani}}$.

Proposition 6.2.3. — Le support du faisceau pervers $^{p}\mathrm{H}^{n}(\tilde{f}_{*}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})_{\kappa}$ est contenu dans $\tilde{\mathcal{A}}_{\kappa}^{\mathrm{ani}}$.

Démonstration. — Il résulte de la description explicite 5.5.4 de $\pi_0(\tilde{\mathcal{P}}^{\mathrm{ani}})$ que la restriction de $^p\mathrm{H}^n (\tilde{f}_*^{\mathrm{ani}}\bar{\mathbf{Q}}_\ell)_\kappa$ à l'ouvert $\tilde{\mathcal{A}}^{\mathrm{ani}} - \tilde{\mathcal{A}}_{\kappa}^{\mathrm{ani}}$ est nulle.

6.3. L'immersion fermée de $\tilde{\mathcal{A}}_{\mathrm{H}}$ dans $\tilde{\mathcal{A}}$. — Soit $(\kappa, \rho_{\kappa}^{\bullet})$ une donnée endoscopique pointée de G sur $\bar{\mathbf{X}}$ c'est-à-dire un homomorphisme continu $\pi_1(\bar{\mathbf{X}}, \infty) \to \pi_0(\kappa)$ comme dans cf. 1.8.2. On a alors un $\pi_0(\kappa)$-torseur $\rho_{\kappa}: \bar{\mathbf{X}}_{\rho_{\kappa}} \to \bar{\mathbf{X}}$ avec un point $\infty_{\rho_{\kappa}}$ au-dessus de $\infty$. Rappelons qu'on peut identifier $\mathfrak{c}_{\mathrm{D}}$ avec le quotient au sens invariant de $\bar{\mathbf{X}}_{\rho_{\kappa}} \times_{\bar{\mathbf{X}}} \mathbf{t}_{\mathrm{D}}$ par l'action de $\mathbf{W} \rtimes \pi_0(\kappa)$. On a aussi construit un homomorphisme $\mathbf{W}_{\mathbf{H}} \rtimes \pi_0(\kappa) \to \mathbf{W} \rtimes \pi_0(\kappa)$ cf. 1.9.1 tel que le quotient au sens des invariants de $\bar{\mathbf{X}}_{\rho_{\kappa}} \times_{\bar{\mathbf{X}}} \mathbf{t}_{\mathrm{D}}$ par $\mathbf{W}_{\mathbf{H}} \rtimes \pi_0(\kappa)$ soit $\mathfrak{c}_{\mathrm{H},\mathrm{D}}$. On en a déduit ainsi un morphisme $\mathfrak{c}_{\mathrm{H},\mathrm{D}} \to \mathfrak{c}_{\mathrm{D}}$ et donc un morphisme $\nu: \mathcal{A}_{\mathrm{H}} \to \mathcal{A}$ cf. 4.17.

6.3.1. — Pour tout  $a \in \mathcal{A}^{\infty}(\bar{k})$ , on forme comme dans 4.5.4 le produit cartésien

$$
\tilde {\mathrm{X}} _ {\rho_ {\kappa}, a} = \tilde {\mathrm{X}} _ {a} \times_ {\bar {\mathrm{X}}} \bar {\mathrm{X}} _ {\rho_ {\kappa}}.
$$

C'est une courbe tracée sur $\bar{\mathbf{X}}_{\rho_{\kappa}} \times_{\bar{\mathbf{X}}} \mathbf{t}_{\mathrm{D}}$ dont la projection sur $\bar{\mathbf{X}}$ est génériquement étale galoisienne de groupe de Galois $\mathbf{W} \rtimes \pi_0(\kappa)$. Le choix d'un point $\tilde{\infty} \in \tilde{\mathbf{X}}_a$ au-dessus de $\infty$ est équivalent au choix d'un point $\tilde{\infty}_{\rho_{\kappa}}$ au-dessus de $\infty_{\rho_{\kappa}}$ de sorte qu'il est légitime d'écrire $\tilde{a} = (a, \tilde{\infty}_{\rho_{\kappa}}) \in \tilde{\mathcal{A}}$ avec $a \in \mathcal{A}^{\infty}$ et $\tilde{\infty}_{\rho_{\kappa}}$ comme ci-dessus.

Par construction du morphisme $\nu : \mathcal{A}_{\mathrm{H}} \to \mathcal{A}$, si $a_{\mathrm{H}} \in \mathcal{A}_{\mathrm{H}}$ et si $\nu(a_{\mathrm{H}}) = a$, on a un plongement $\tilde{\mathrm{X}}_{\rho_{\kappa}, a_{\mathrm{H}}} \to \tilde{\mathrm{X}}_{\rho_{\kappa}, a}$ qui réalise le premier comme une réunion de certaines composantes irréductibles du dernier. On définit un morphisme

$$
\tilde {\nu}: \tilde {\mathcal {A}} _ {\mathrm{H}} \to \tilde {\mathcal {A}}
$$

par la recette  $(a_{\mathrm{H}}, \tilde{\infty}_{\rho_{\kappa}}) \mapsto (\nu(a_{\mathrm{H}}), \tilde{\infty}_{\rho_{\kappa}})$ . Remarquons que si le point  $\infty_{\rho_{\kappa}}$  est défini sur k, ce morphisme est aussi défini sur k.

## Proposition 6.3.2. — Le morphisme $\tilde{\nu}:\tilde{\mathcal{A}}_{\mathrm{H}}\to \tilde{\mathcal{A}}$ est une immersion fermée.

Démonstration. — On sait par [57, 10.3] que c'est un morphisme fini non ramifié. Il suffit maintenant de vérifier qu'il induit une injection au niveau des points géométriques.

Supposons qu'un point $\tilde{a} = (a, \tilde{\infty}_{\rho_{\kappa}}) \in \tilde{\mathcal{A}}(\bar{k})$ est dans l'image de $\tilde{\nu}$. Nous allons montrer qu'il provient d'un unique point $\tilde{a}_{\mathrm{H}} = (a_{\mathrm{H}}, \tilde{\infty}_{\rho_{\kappa}}) \in \tilde{\mathcal{A}}_{\mathrm{H}}$. Pour cela, nous remarquons que $a_{\mathrm{H}}$ est complètement déterminé par la courbe $\tilde{\mathbf{X}}_{\rho_{\kappa}, a_{\mathrm{H}}}$ et cette courbe est la plus petite réunion de composantes irréductibles de $\tilde{\mathbf{X}}_{\rho_{\kappa}, a}$ qui soit stable sous $\mathbf{W}_{\mathbf{H}} \rtimes \pi_0(\kappa)$ et qui contienne le point $\tilde{\infty}_{\rho_{\kappa}}$.

Proposition 6.3.3. — Le sous-schéma fermé $\tilde{\mathcal{A}}_{\kappa}$ de $\tilde{\mathcal{A}}$ défini dans 6.2.2 est la réunion disjointe des fermés $\tilde{\nu}(\tilde{\mathcal{A}}_{\mathrm{H}})$ associés aux homomorphismes $\rho_{\kappa}^{\bullet}:\pi_{1}(\bar{\mathrm{X}},\infty)\to\pi_{0}(\kappa)$.

Démonstration. — Dans 5.4.1, on a associé à un point géométrique $\tilde{a} = (a, \tilde{\infty}) \in \mathcal{A}(\bar{k})$ un diagramme :

$$
\begin{array}{c} \pi_ {1} (\mathrm{U}, \infty) \xrightarrow {\pi_ {a} ^ {\bullet}} \mathbf {W} \rtimes \operatorname{Out} (\mathbf {G}) \\ \Bigg \downarrow \\ \pi_ {1} (\bar {\mathrm{X}}, x) \xrightarrow {\rho_ {\mathrm{G}} ^ {\bullet}} \operatorname{Out} (\mathbf {G}) \end{array}
$$

Ici U est le plus grand ouvert de $\bar{\mathbf{X}}$ contenant $\infty$ au-dessus duquel le revêtement caméral $\tilde{\mathbf{X}}_a \to \bar{\mathbf{X}}$ est étale. On y a noté $\mathrm{W}_{\tilde{a}}$ l'image de $\pi_{\tilde{a}}^{\bullet}$ dans $\mathbf{W} \rtimes \operatorname{Out}(\mathbf{G})$ et $\mathrm{I}_{\tilde{a}}$ l'image du noyau de l'homomorphisme $\pi_1(\mathrm{U}, \infty) \to \pi_1(\bar{\mathbf{X}}, \infty)$.

Par définition,  $(a, \tilde{\infty})$  appartient à  $\tilde{A}_{\kappa}$  si et seulement si  $W_{\tilde{a}}$  est contenu dans  $(\mathbf{W} \rtimes \operatorname{Out}(\mathbf{G}))_{\kappa}$  et  $I_{\tilde{a}}$  est contenu dans le groupe de Weyl  $W_{H}$  de composante neutre  $\hat{H}$  du centralisateur de  $\kappa$  dans  $\hat{G}$ . Rappelons qu'on a une suite exacte

$$
1 \to \mathbf {W} _ {\mathbf {H}} \to (\mathbf {W} \rtimes \operatorname{Out} (\mathbf {G})) _ {\kappa} \to \pi_ {0} (\kappa) \to 1.\tag{6.3.4}
$$

D'après [57, lemme 10.1], il existe un scindage canonique qui permet d'identifier $(\mathbf{W} \rtimes \mathrm{Out}(\mathbf{G}))_{\kappa}$ à un produit semi-direct $\mathbf{W}_{\mathbf{H}} \rtimes \pi_0(\kappa)$.

Soit H le groupe endoscopique associé à un homomorphisme $\rho_{\kappa}^{\bullet}:\pi_{1}(\bar{\mathrm{X}},\infty)\to$$\pi_0(\kappa)$. Soit $\tilde{a}_{\mathrm{H}}\in \tilde{\mathcal{A}}_{\mathrm{H}}(\bar{k})$. Soit U l'ouvert de $\bar{\mathrm{X}}$ contenant $\infty$ au-dessus duquel le revêtement caméral $\tilde{\mathrm{X}}_{a_{\mathrm{H}}}\rightarrow \bar{\mathrm{X}}$ est étale. L'homomorphisme

$$
\pi_ {\tilde {a} _ {\mathrm{H}}} ^ {\bullet}: \pi_ {1} (\mathrm{U}, \infty) \rightarrow \mathbf {W} _ {\mathbf {H}} \rtimes \operatorname{Out} (\mathbf {H})
$$

induit un homomorphisme

$$
\pi_ {\tilde {a} _ {\mathrm{H}}} ^ {\kappa , \bullet}: \pi_ {1} (\mathrm{U}, \infty) \to \mathbf {W} _ {\mathbf {H}} \rtimes \pi_ {0} (\kappa)
$$

au-dessus de $\rho_{\kappa}^{\bullet}:\pi_{1}(\bar{\mathbf{X}},\infty)\to\pi_{0}(\kappa)$. Par construction de $\tilde{a}=\tilde{\nu}(\tilde{a}_{\mathrm{H}})$, l'homomorphisme $\pi_{\tilde{a}}^{\bullet}$ s'obtient en composant $\pi_{\tilde{a}_{\mathrm{H}}}^{\kappa,\bullet}$ avec le plongement $\mathbf{W}_{\mathbf{H}}\rtimes\pi_{0}(\kappa)\to\mathbf{W}\rtimes\mathrm{Out}(\mathbf{G})$ via l'identification $(\mathbf{W}\rtimes\mathrm{Out}(\mathbf{G}))_{\kappa}=\mathbf{W}_{\mathbf{H}}\rtimes\pi_{0}(\kappa)$. On a donc $\mathrm{W}_{\tilde{a}}\subset(\mathbf{W}\rtimes\mathrm{Out}(\mathbf{G}))_{\kappa}$ et $\mathrm{I}_{\tilde{a}}\subset\mathbf{W}_{\mathbf{H}}$ c'est-à-dire $\tilde{a}\in\tilde{\mathcal{A}}_{\kappa}(\bar{k})$.

Inversement soit $\tilde{a} \in \tilde{\mathcal{A}}_{\kappa}(\bar{k})$. Puisque $W_{\tilde{a}} \subset (\mathbf{W} \rtimes \mathrm{Out}(\mathbf{G}))_{\kappa}$ et $I_{\tilde{a}} \subset W_{\mathbf{H}}$, $\pi_{\tilde{a}}^{\bullet}$ induit un homomorphisme

$$
\rho_ {\kappa} ^ {\bullet}: \pi_ {1} (\bar {\mathrm{X}}, \infty) \to \mathrm{W} _ {\tilde {a}} / \mathrm{I} _ {\tilde {a}} \to \pi_ {0} (\kappa).
$$

Soit H le groupe endoscopique associé à ce $\rho_{\kappa}^{\bullet}$. Il reste à construire un point $\tilde{a}_{\mathrm{H}} \in \tilde{\mathcal{A}}_{\mathrm{H}}(\bar{k})$ tel que $\tilde{\nu}(\tilde{a}_{\mathrm{H}}) = \tilde{a}$. Cette construction est identique à celle qui apparaît dans la démonstration de la proposition précédente.

Les arguments similaires permettent une interprétation naturelle du complément de l'ouvert $\tilde{\mathcal{A}}^{\mathrm{ani}}$.

Proposition 6.3.5. — Le complément de l'ouvert $\tilde{\mathcal{A}}^{\mathrm{ani}}$ dans $\tilde{\mathcal{A}}$ est la réunion des images des immersions fermées

$$
\tilde {\mathcal {A}} _ {\mathrm{M}} \rightarrow \tilde {\mathcal {A}}
$$

sur l'ensemble des sous-groupes de Levi M contenant le tore maximal T.

Démonstration. — Soit $\tilde{a} \in (\tilde{\mathcal{A}} - \tilde{\mathcal{A}}^{\mathrm{ani}})(\bar{k})$. Par définition, le groupe $\mathbf{T}^{\mathrm{W}_{\tilde{a}}}$ n'est pas fini, donc contient un tore $\mathbf{S}$. Le centralisateur de ce tore dans $\mathbf{G}$ est un sous-groupe de Levi $\mathbf{M}$ de $\mathbf{G}$. Le groupe $\mathrm{W}_{\tilde{a}}$ est un sous-groupe du fixateur de $\mathbf{S}$ dans $\mathbf{W} \rtimes \mathrm{Out}(\mathbf{G})$. Le groupe $\mathrm{I}_{\tilde{a}}$ est contenu dans l'intersection du fixateur de $\mathbf{M}$ avec $\mathbf{W}$, donc contenu dans $\mathbf{W}_{\mathbf{M}}$. Le même argument que celui utilisé dans la démonstration de 6.3.3 montre que $\tilde{a}$ provient d'un point $\tilde{a}_{\mathrm{M}} \in \tilde{\mathcal{A}}_{\mathrm{M}}(\bar{k})$.

Corollaire 6.3.6. — La codimension de $\mathcal{A}^{\heartsuit}-\mathcal{A}^{\mathrm{ani}}$ dans $\mathcal{A}^{\heartsuit}$ est plus grande ou égale à $\deg(\mathrm{D})$.

Démonstration. — D'après la description du complément de $\tilde{\mathcal{A}}^{\mathrm{ani}}$ et la formule de dimension 4.13.1, on a

$$
\dim (\mathcal {A}) - \dim (\mathcal {A} _ {\mathrm{M}}) = (\sharp \Phi - \sharp \Phi_ {\mathrm{M}}) \deg (\mathrm{D}) / 2 \geq \deg (\mathrm{D})
$$

d'où la proposition.

6.4. Stabilisation géométrique. — D'après 6.2.3, le support du faisceau pervers $^{p}\mathrm{H}^{n}(\tilde{f}_{*}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})_{\kappa}$ est contenu dans $\tilde{\mathcal{A}}_{\kappa}^{\mathrm{ani}}$. D'après la description de $\tilde{\mathcal{A}}_{\kappa}^{\mathrm{ani}}$ en fonction des groupes endoscopiques cf. 6.3.3, ce faisceau pervers se décompose en somme directe de facteurs paramétrés par l'ensemble des données endoscopiques pointées $(\kappa, \rho_{\kappa,\xi}^{\bullet})$, le facteur direct paramétré par $\xi$ étant supporté par le fermé $\tilde{\nu}_{\xi}(\tilde{\mathcal{A}}_{\mathrm{H}_{\xi}}) \cap \tilde{\mathcal{A}}^{\mathrm{ani}}$ où $\mathrm{H}_{\xi}$ est le groupe endoscopique attaché à $(\kappa, \rho_{\kappa,\xi}^{\bullet})$ et $\tilde{\nu}_{\xi}$ est l'immersion fermée de $\tilde{\mathcal{A}}_{\mathrm{H}_{\xi}}$ dans $\tilde{\mathcal{A}}$. Notre résultat principal est une description de chacun de ces facteurs directs.

## Théorème 6.4.1. — Il existe un isomorphisme entre les faisceaux pervers gradués

$$
\bigoplus_ {n} ^ {p} \mathrm{H} ^ {n} (\tilde {f} _ {*} ^ {\mathrm{ani}} \bar {\mathbf {Q}} _ {\ell}) _ {\kappa} [ 2 r _ {\mathbf {H}} ^ {\mathbf {G}} (\mathrm{D}) ] (r _ {\mathbf {H}} ^ {\mathbf {G}} (\mathrm{D}))
$$

et

$$
\bigoplus_ {n} \bigoplus_ {(\kappa , \rho_ {\kappa , \xi} ^ {\bullet})} \tilde {\nu} _ {\xi , *} ^ {p} H ^ {*} (\tilde {f} _ {H _ {\xi}, *} ^ {\text { ani }} \bar {\mathbf {Q}} _ {\ell}) _ {\text { st }}
$$

où la dernière somme directe porte sur l'ensemble de toutes les données endoscopiques pointées  $(\kappa, \rho_{\kappa,\xi}^{\bullet})$  ayant la composante  $\kappa$  fixée. Ici, l'indice st signifie le facteur direct où  $\tilde{P}_{H_{\xi}}$  agit trivialement et l'entier  $r_{\mathbf{H}}^{\mathbf{G}}(\mathbf{D})$  est la codimension de  $\tilde{A}_{H_{\xi}}$  dans  $\tilde{A}$  qui est donnée par la formule

$$
r _ {\mathbf {H}} ^ {\mathbf {G}} (\mathrm{D}) = (\sharp \Phi - \sharp \Phi_ {\mathbf {H}}) \deg (\mathrm{D}) / 2.
$$

Bien que l'énoncé ci-dessus est sur $\bar{k}$, notre démonstration est en partie arithmétique. Supposons maintenant qu'on a une donnée endoscopique pointée ($\kappa$, $\rho_{\kappa}^{\bullet}$) définie sur X c'est-à-dire $\rho_{\kappa}^{\bullet}$ s'étend en un homomorphisme

$$
\pi_ {1} (\mathrm{X}, \infty) = \pi_ {1} (\bar {\mathrm{X}}, \infty) \rtimes \operatorname{Gal} (\bar {k} / k) \rightarrow \pi_ {0} (\kappa).
$$

Le groupe endoscopique associé H est alors défini sur X. On dispose d'une fibration de Hitchin  $f^{H}: M_{H} \to A_{H}$  pour le groupe H et d'un revêtement étale  $\tilde{A}_{H}$  de  $A_{H}$ . L'immersion fermée  $\tilde{\nu}: \tilde{A}_{H} \to \tilde{A}_{G}$  de 6.3.2 est alors définie sur k.

Théorème 6.4.2. — Il existe un isomorphisme défini sur k entre les semi-simplifications des faisceaux pervers gradués

$$
\bigoplus_ {n} \tilde {\nu} ^ {*   p} \mathrm{H} ^ {n} (\tilde {f} _ {*} ^ {\mathrm{ani}} \bar {\mathbf {Q}} _ {\ell}) _ {\kappa} [ 2 r _ {\mathrm{H}} ^ {\mathrm{G}} (\mathrm{D}) ] (r _ {\mathrm{H}} ^ {\mathrm{G}} (\mathrm{D})) \simeq \bigoplus_ {n} ^ {p} \mathrm{H} ^ {*} (\tilde {f} _ {\mathrm{H}, *} ^ {\mathrm{ani}} \bar {\mathbf {Q}} _ {\ell}) _ {\mathrm{st}}.
$$

Notons que les deux membres de l'égalité étant des faisceaux pervers purs gradués, ils sont géométriquement semi-simples cf. [7]. Il s'ensuit que les faisceaux pervers gradués ci-dessus sont isomorphes au-dessus de $\mathcal{A}^{\mathrm{ani}}\otimes_{k}\bar{k}$. Par ailleurs, comme toute donnée endoscopique sur $\bar{\mathbf{X}}$ est définie sur $\mathbf{X}\otimes_k k'$ pour une extension finie $k'$ de $k$, le théorème 6.4.1

est une conséquence de 6.4.2. La démonstration de ce dernier ne se termine qu'au paragraphe 8.7. On obtiendra en particulier la conjecture de Langlands-Shelstad 1.11.1 en cours de sa démonstration.

6.5. Cohomologie ordinaire de degré maximal. — Dans ce paragraphe, nous démontrons une variante élémentaire du théorème de stabilisation géométrique 6.4.1 où au lieu des faisceaux pervers de cohomologie, on considère le faisceau de cohomologie ordinaire de degré maximal.

Notons $d$ la dimension relative du morphisme $\tilde{f}^{\mathrm{ani}}: \tilde{\mathcal{M}}^{\mathrm{ani}} \to \tilde{\mathcal{A}}^{\mathrm{ani}}$. D'après le lemme d'homotopie, l'action de $\tilde{\mathcal{P}}^{\mathrm{ani}}$ sur $\mathrm{R}^{2d}\tilde{f}_{*}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell}$ se factorise par le faisceau fini $\pi_0(\tilde{\mathcal{P}}^{\mathrm{ani}})$. Rappelons aussi que ce dernier est un quotient du faisceau constant $\mathbf{X}_*$. Notons $(\mathrm{R}^{2d}\tilde{f}_{*}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})_{\mathrm{st}}$ le plus grand facteur direct où $\mathbf{X}_*$ agit trivialement et $(\mathrm{R}^{2d}\tilde{f}_{*}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})_{\kappa}$ celui où il agit à travers le caractère $\kappa: \mathbf{X}_* \to \bar{\mathbf{Q}}_\ell^\times$ que nous avons fixé.

Proposition 6.5.1. — On a un isomorphisme entre la partie stable  $(\mathrm{R}^{2d}\tilde{f}_{*}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})_{\mathrm{st}}$  et le faisceau constant  $\bar{Q}_{\ell}$ . On a aussi un isomorphisme entre  $(\mathrm{R}^{2d}\tilde{f}_{*}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})_{\kappa}$  et la somme directe

$$
\bigoplus_ {(\kappa , \rho_ {\kappa , \xi} ^ {\bullet})} \tilde {\nu} _ {\xi , *} \bar {\mathbf {Q}} _ {\ell}
$$

étendue sur l'ensemble des données endoscopiques pointées  $(\kappa, \rho_{\kappa,\xi}^{\bullet})$  ayant la composante  $\kappa$  fixée, où  $\tilde{\nu}_{\xi}$  désigne l'immersion fermée de  $\tilde{A}_{H_{\xi}}^{ani}$  dans  $\tilde{A}^{ani}$,  $H_{\xi}$  étant le groupe endoscopique attaché à  $(\kappa, \rho_{\kappa,\xi}^{\bullet})$.

Démonstration. — La section de Hitchin-Kostant définit une immersion ouverte $\tilde{\mathcal{P}}^{\mathrm{ani}}\to \tilde{\mathcal{M}}^{\mathrm{ani}}$ dont le complémentaire fermé est de dimension relative $\leq d - 1$ cf. 4.16.1. Il s'ensuit un isomorphisme

$$
\mathrm{R} ^ {2 d} g _ {!} \bar {\mathbf {Q}} _ {\ell} \rightarrow \mathrm{R} ^ {2 d} \tilde {f} _ {*} ^ {\mathrm{ani}} \bar {\mathbf {Q}} _ {\ell}
$$

compatible à l'action de $\pi_0(\tilde{\mathcal{P}}^{\mathrm{ani}})$. Ici $g$ a désigné le morphisme $\tilde{\mathcal{P}}^{\mathrm{ani}} \to \tilde{\mathcal{A}}^{\mathrm{ani}}$.

Le morphisme trace permet d'identifier  $R^{2d}g_{l}\bar{Q}_{\ell}$  au faisceau associé au préfaisceau

$$
\mathrm{U} \mapsto \bar {\mathbf {Q}} _ {\ell} ^ {\pi_ {0} (\tilde {\mathcal {P}} ^ {\mathrm{ani}}) (\mathrm{U})}.
$$

La proposition résulte donc de la description explicite du faisceau $\pi_0(\tilde{\mathcal{P}}^{\mathrm{ani}})$ donnée dans 5.5.4. En effet $\pi_0(\tilde{\mathcal{P}}^{\mathrm{ani}})$ est un quotient du faisceau constant $\mathbf{X}_*$. On peut remplacer $\mathbf{X}_*$ par un quotient fini $\mathbf{X}$. Ainsi $\mathrm{R}^{2d}g!\bar{\mathbf{Q}}_\ell$ est un quotient du faisceau constant $\bar{\mathbf{Q}}_\ell^{\mathbf{x}}$. Les parties isotypiques $(\mathrm{R}^{2d}g!\bar{\mathbf{Q}}_\ell)_{\mathrm{st}}$ et $(\mathrm{R}^{2d}g!\bar{\mathbf{Q}}_\ell)_\kappa$ sont quotients des parties isotypiques correspondants de $\bar{\mathbf{Q}}_\ell^{\mathbf{x}}$ lesquels sont des faisceaux constants de rang un. Les assertions à démontrer sont maintenant réduites à une vérification fibre par fibre qui est facile.

## 7. Théorème du support

Soient S un $k$-schéma de type fini, $f: \mathbf{M} \to \mathbf{S}$ un morphisme propre de source lisse. D'après les théorèmes de pureté [18] et de décomposition [7], le complexe $f_*\bar{\mathbf{Q}}_\ell$ est pur et est isomorphe au-dessus de $\mathbf{S} \otimes_k \bar{k}$ à une somme directe de faisceaux pervers géométriquement simples avec décalage. Leurs supports constituent un invariant topologique important de $f$. En général, il est difficile de déterminer explicitement cet invariant.

On introduit une notion de fibration abélienne δ-régulière cf. 7.1.5 pour laquelle il est possible de déterminer les supports cf. 7.2.1. Comme on ne sait pas démontrer la δ-régularité de la fibration de Hitchin en caractéristique positive, nous formulons des énoncés 7.2.2 et 7.2.3 qui donnent un contrôle suffisant en vue de la démonstration des théorèmes 6.4.1 et 6.4.2. A l'exception du dernier paragraphe, le chapitre est rédigé dans la situation générale des fibrations abéliennes faibles.

7.1. Fibration abélienne. — Nous allons formaliser les propriétés observées sur la fibration de Hitchin pour axiomatiser une notion de fibration abélienne algébrique. Nous allons en fait introduire d'une part la notion de fibration abélienne faible qui regroupe les propriété stables par changement de base arbitraire et d'autre part celle de fibration abélienne δ-régulière qui est préservée seulement par changement de base plat. La bonne notion de fibration abélienne devrait se situer entre les deux.

7.1.1. — Une fibration abélienne faible sur un k-schéma S consiste en un morphisme propre  $f: M \rightarrow S$  et un schéma en groupes lisse commutatif  $g: P \rightarrow S$  muni d'une action

$$
\mathrm{act}: \mathrm{P} \times_ {\mathrm{S}} \mathrm{M} \rightarrow \mathrm{M}
$$

qui satisfait les trois propriétés 7.1.2, 7.1.3 et 7.1.4 qui suivent :

7.1.2. — Les morphismes f et g ont la même dimension relative d. $^{1}$

7.1.3. — L'action de P sur M n'a que des stabilisateurs affines c'est-à-dire pour tout point géométrique  $m \in M$  au-dessus de  $s \in S$ , le stabilisateur de m dans  $P_{s}$  est un sous-groupe affine.

7.1.4. — Soit  $P^{0}$  le sous-schéma en groupes ouvert des composantes neutres des fibres de P et notons  $g^{0}:P^{0}\rightarrow S$ . Considérons le faisceau des modules de Tate

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P} ^ {0}) = \mathrm{H} ^ {2 d - 1} (g _ {!} ^ {0} \bar {\mathbf {Q}} _ {\ell}) (d)
$$

dont la fibre au-dessus de chaque point géométrique $s$ de S est le $\bar{\mathbf{Q}}_{\ell}$-module de Tate $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P}_{s}^{0})$. Pour tout point géométrique $s$ de S, le dévissage canonique de Chevalley de $\mathrm{P}_{s}^{0}$

$$
1 \rightarrow \mathrm{R} _ {s} \rightarrow \mathrm{P} _ {s} ^ {0} \rightarrow \mathrm{A} _ {s} \rightarrow 1
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Cette hypothèse n'est nullement nécessaire mais elle simplifie la numérologie.</span></small>

où  $A_{s}$  est une variété abélienne et où  $R_{s}$  est un groupe algébrique affine commutatif connexe induit un dévissage de module de Tate voir [29]

$$
0 \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{R} _ {s}) \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P} _ {s} ^ {0}) \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{A} _ {s}) \to 0.
$$

On dira que  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P}^{0})$  est polarisable si localement pour la topologie étale de S, il existe une forme bilinéaire alternée

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P} ^ {0}) \times \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P} ^ {0}) \rightarrow \bar {\mathbf {Q}} _ {\ell}
$$

dont la fibre en chaque point géométrique $s$ a comme noyau $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{R}_{s})$ c'est-à-dire qu'elle annule $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{R}_{s})$ et induit un accouplement parfait sur $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{s})$.

Les trois propriétés 7.1.2, 7.1.3 et 7.1.4 sont préservées par un changement de base arbitraire. En particulier, la fibre générique d'une fibration abélienne faible ne sera pas nécessairement une variété abélienne. Nous allons maintenant introduire une restriction forte appelée δ-régularité qui garantira entre autres cette propriété.

7.1.5. — Pour tout point géométrique  $s \in S$ , notons  $\delta_{s} = \dim(R_{s})$  la dimension de la partie affine de  $P_{s}$ . Si  $s \in S$  un point quelconque, le dévissage de Chevalley de  $P_{s}$  existe et est unique après un changement de base radiciel de sorte que l'entier  $\delta_{s}$  est bien défini. La fonction  $\delta$  définie sur l'espace topologique sous-jacent à S à valeurs dans les entiers naturels est semi-continue cf. 5.6.2. En supposant cette fonction constructible, il existe une stratification de S en des sous-schémas localement fermés  $S_{\delta}$  tels que pour tout point géométrique  $s \in S_{\delta}$ , on a  $\delta_{s} = \delta$ .

On dira que le S-schéma en groupes commutatif lisse P est $\delta$-régulier si pour tout $\delta \in \mathbf{N}$, on a

$$
\mathrm{codim} _ {\mathrm{S}} (\mathrm{S} _ {\delta}) \geq \delta .
$$

Si  $S_{\delta}$  est vide, notre convention attribue à la codimension la valeur infinie.

Une fibration abélienne faible dont la composante P jouit de la  $\delta$ -régularité sera appelée fibration abélienne  $\delta$ -régulière.

7.1.6. — Il y une autre formulation de la notion de  $\delta$ -régularité. Soit Z un sous-schéma fermé irréductible de S. Soit  $\delta_{Z}$  la valeur minimale que prend la fonction  $\delta$  sur Z. Alors, P est  $\delta$ -régulier si et seulement si pour tout sous-schéma fermé irréductible Z de S, on a codim(Z)  $\geq \delta_{Z}$ .

En effet, comme la valeur $\delta_{\mathrm{Z}}$ est atteinte sur un ouvert dense de Z, Z est contenu dans l'adhérence de la strate $\mathrm{S}_{\delta_{\mathrm{Z}}}$. Si P est $\delta$-régulier, alors $\operatorname{codim}(\mathrm{S}_{\delta_{\mathrm{Z}}}) \geq \delta_{\mathrm{Z}}$ a fortiori $\operatorname{codim}(\mathrm{Z}) \geq \delta_{\mathrm{Z}}$. L'autre implication est aussi évidente.

Notons que la  $\delta$ -régularité est préservée par changement de base plat. Remarquons aussi que la  $\delta$ -régularité implique que

$$
\operatorname{codim} (\mathrm{S} _ {1}) \geq 1
$$

de sorte que  $S_{0} \neq \emptyset$ . Il s'ensuit que  $P^{0}$  est génériquement une variété abélienne.

7.2. L'énoncé du théorème du support. — Soient S un k-schéma de type fini et f : M → S un morphisme propre. Supposons que le faisceau constant  $\bar{Q}_{\ell}$  sur M est autodual et donc pur. En particulier, c'est le cas si M est un k-schéma lisse. D'après le théorème de pureté de Deligne, le complexe d'image directe  $f_{*}\bar{Q}_{\ell}$  est pur. En appliquant le théorème de décomposition [7], on sait qu'au-dessus de S ⊗k k, le complexe  $f_{*}\bar{Q}_{\ell}$  est isomorphe à la somme directe de ses faisceaux pervers de cohomologie avec des décalages évidents

$$
f _ {*} \bar {\mathbf {Q}} _ {\ell} \simeq \bigoplus_ {n} ^ {p} \mathrm{H} ^ {n} (f _ {*} \bar {\mathbf {Q}} _ {\ell}) [ - n ]
$$

et de plus, les faisceaux pervers  ${}^{b}\mathrm{H}^{n}(f_{*}\bar{\mathbf{Q}}_{\ell})$  sont semi-simples. D'après [7], pour tout faisceau pervers géométriquement simple K sur  $S\otimes_{k}\bar{k}$ , il existe un sous-schéma fermé réduit irréductible  $i:Z\hookrightarrow S\otimes_{k}\bar{k}$ , un ouvert dense  $U\hookrightarrow Z$  et un système local irréductible K sur U tel que

$$
\mathrm{K} = i _ {*} j _ {! *} \mathcal {K} [ \dim (\mathrm{Z}) ].
$$

Le sous-schéma fermé Z est complètement déterminé par K et sera appelé le support de K. En général, le problème de déterminer les supports des faisceaux pervers simples présents dans la décomposition de  $f_{*}\bar{Q}_{\ell}$  est un problème très difficile. On peut cependant le résoudre dans le cas d'une fibration abélienne  $\delta$ -régulière.

Théorème 7.2.1. — Soit S un k-schéma de type fini géométriquement irréductible. Soit f : M → S un morphisme projectif purement de dimension relative d muni d'une action d'un schéma en groupes lisse g : P → S qui forme une fibration abélienne δ-régulière. Supposons que le faisceau constant $\mathbf{Q}_{\ell}$ sur M est auto-dual et donc pur.

Soient K un faisceau pervers géométriquement simple présent dans la décomposition d'un faisceau pervers de cohomologie  ${}^{p}\mathrm{H}^{n}(f_{*}\bar{\mathbf{Q}}_{\ell})$  et Z son support. Il existe alors un ouvert U de  $S \otimes_{k} \bar{k}$  tel que  $U \cap Z$  est non vide et un système local non trivial L sur  $U \cap Z$  tel que  $i_{*}L$ , i étant l'immersion fermée  $U \cap Z \to U$ , soit un facteur direct de la restriction du faisceau de cohomologie ordinaire de degré maximal  $\mathrm{H}^{2d}(f_{*}\bar{\mathbf{Q}}_{\ell})$  à U.

Malgré l'apparence compliquée, cet énoncé est en réalité effectif dans la détermination des supports car le faisceau de cohomologie ordinaire de degré maximal est en général connu cf. 6.5 ainsi que ses facteurs directs locaux. Remarquons aussi qu'il n'y a rien de commun entre K et L à l'exception du support. La démonstration du théorème passe par l'énoncé suivant.

Proposition 7.2.2. — Soient S un k-schéma de type fini géométriquement irréductible, $f: \mathbf{M} \to \mathbf{S}$ un morphisme projectif purement de dimension relative d muni d'une action d'un schéma en groupes lisse $g: \mathbf{P} \to \mathbf{S}$ qui forme une fibration abélienne faible. Supposons que le faisceau constant $\bar{\mathbf{Q}}_{\ell}$ sur M est auto-dual et donc pur.

Soient K un faisceau pervers géométriquement simple présent dans la décomposition d'un faisceau pervers de cohomologie  ${}^{p}\mathrm{H}^{n}(f_{*}\bar{\mathbf{Q}}_{\ell})$  et Z son support. Soit  $\delta_{Z}$  la valeur minimale que la fonction  $\delta$  attachée à P prend sur Z. Alors on a l'inégalité

$$
\operatorname{codim} (Z) \leq \delta_ {Z}.
$$

Si l'égalité est atteinte, il existe un ouvert U de S ⊗k k tel que U ∩ Z est non vide et un système local non trivial L sur U ∩ Z tel que i\*L, i étant l'immersion fermée U ∩ Z → U, soit un facteur direct de la restriction du faisceau de cohomologie ordinaire de degré maximal H$^{2d}$(f\*Q$_{\ell}$) à U.

Il est clair que 7.2.2 implique 7.2.1 car l'hypothèse de $\delta$-régularité implique l'inégalité opposée $\mathrm{codim}(\mathbf{Z}) \geq \delta_{\mathbf{Z}}$ cf. 7.1.6.

Considérons une variante de l'inégalité delta 7.2.2 où l'on tient compte aussi des groupes de composantes connexes des fibres de P. Soit $\pi_0(P)$ le faisceau des groupes de composantes connexes des fibres de P. Supposons qu'il est quotient d'un faisceau constant ayant comme fibre le groupe fini abélien $\mathbf{X}$ comme par exemple 5.5.4.

Le schéma en groupes P agit sur le faisceau pervers de cohomologie  ${}^{p}\mathrm{H}^{n}(f_{*}\bar{\mathbf{Q}}_{\ell})$  à travers  $\pi_{0}(\mathrm{P})$ . Le groupe X agit donc sur  ${}^{p}\mathrm{H}^{n}(f_{*}\bar{\mathbf{Q}}_{\ell})$ . Pour tout caractère  $\kappa:X\to\bar{\mathbf{Q}}_{\ell}^{\times}$ , on a le plus grand facteur direct  ${}^{p}\mathrm{H}^{n}(f_{*}\bar{\mathbf{Q}}_{\ell})_{\kappa}$  de  ${}^{p}\mathrm{H}^{n}(f_{*}\bar{\mathbf{Q}}_{\ell})$  où X agit à travers  $\kappa$ . De même, on a le facteur direct  $\mathrm{H}^{2d}(f_{*}\bar{\mathbf{Q}}_{\ell})_{\kappa}$  du faisceau de cohomologie ordinaire  $\mathrm{H}^{2d}(f_{*}\bar{\mathbf{Q}}_{\ell})$ .

En fait, il existe un entier naturel N et une décomposition du complexe borné constructible  $f_{*}\bar{Q}_{\ell}$

$$
f _ {*} \bar {\mathbf {Q}} _ {\ell} = \bigoplus_ {\kappa \in \mathbf {X} ^ {*}} (f _ {*} \bar {\mathbf {Q}} _ {\ell}) _ {\kappa}
$$

tels que pour tout $\alpha\in\mathbf{X},(\alpha-\kappa(\alpha)\mathrm{id})^{\mathrm{N}}$ est nul sur le facteur direct $(f_{*}\bar{\mathbf{Q}}_{\ell})_{\kappa}$ cf. [54, 3.2.5].

Si on remplace $f_{*}\bar{\mathbf{Q}}_{\ell}$ par $(f_{*}\bar{\mathbf{Q}}_{\ell})_{\kappa}$ dans la démonstration de 7.2.2, on obtiendra la variante suivante.

Proposition 7.2.3. — On peut remplacer dans 7.2.2, le faisceau pervers $^{p}\mathrm{H}^{n}(f_{*}\bar{\mathbf{Q}}_{\ell})$ par son facteur isotypique $^{p}\mathrm{H}^{n}(f_{*}\bar{\mathbf{Q}}_{\ell})_{\kappa}$ et le faisceau ordinaire $\mathrm{H}^{2d}(f_{*}\bar{\mathbf{Q}}_{\ell})$ par son facteur isotypique $\mathrm{H}^{2d}(f_{*}\bar{\mathbf{Q}}_{\ell})_{\kappa}$.

Le lecteur notera que tout comme dans 7.2.2, on ne suppose pas ici que P est $\delta$-régulier.

Dans le dernier paragraphe de ce chapitre, nous allons appliquer 7.2.3 au cas de la fibration de Hitchin, plus précisément au morphisme $\tilde{f}^{\mathrm{ani}}: \tilde{\mathcal{M}}^{\mathrm{ani}} \to \tilde{\mathcal{A}}^{\mathrm{ani}}$. Le reste du chapitre est consacré à démontrer l'inégalité delta 7.2.2.

7.3. Inégalité de Goresky-MacPherson. — Goresky et MacPherson ont observé que la dualité de Poincaré impose une contrainte sur la codimension de support des faisceaux pervers simples présents dans le théorème de décomposition. C'est une observation cruciale dont notre inégalité delta 7.2.2 constitue une variante. Nous commençons par rappeler leur inégalité originale.

Théorème 7.3.1. — Soit S un k-schéma de type fini géométriquement irréductible. Soit f : M → S un morphisme propre, purement de dimension relative d. Supposons que le faisceau constant $\bar{\mathbf{Q}}_{\ell}$ sur M est auto-dual et donc pur.

Soit K un faisceau pervers irréductible sur  $S \otimes_{k} \bar{k}$  présent dans la décomposition de l'un des faisceaux pervers de cohomologie  ${}^{p}H^{n}(f_{*}\bar{\mathbf{Q}}_{\ell})$ . Soit Z le support de K. Alors on a l'inégalité

$$
\operatorname{codim} (Z) \leq d.
$$

Supposons que l'égalité a lieu. Il existe alors un ouvert U de S ⊗k k tel que U ∩ Z est non vide et un système local non trivial L sur U ∩ Z tel que i\*L, i étant l'immersion fermée U ∩ Z → U, soit un facteur direct de la restriction du faisceau de cohomologie ordinaire de degré maximal H$^{2d}$(f\*Qℓ) à U.

Démonstration. — Soit Z un sous-schéma fermé irréductible de  $S \otimes_{k} \bar{k}$ . On définit l'ensemble  $\operatorname{occ}(Z)$  des entiers n tels qu'il existe un facteur direct irréductible du faisceau pervers de cohomologie  ${}^{p}\mathrm{H}^{n}(f_{*}\bar{\mathbf{Q}}_{\ell})$  de support Z. D'après la dualité de Poincaré,  ${}^{p}\mathrm{H}^{n}(f_{*}\bar{\mathbf{Q}}_{\ell})$  est le dual de  ${}^{p}\mathrm{H}^{2\dim(\mathrm{M})-n}(f_{*}\bar{\mathbf{Q}}_{\ell})$  de sorte que l'ensemble  $\operatorname{occ}(Z)$  est symétrique par rapport à l'entier  $\dim(M)$ .

Si $\mathrm{occ}(\mathbf{Z}) \neq \emptyset$, il existe un entier $n \geq \dim(\mathbf{M})$ appartenant à $\mathrm{occ}(\mathbf{Z})$. Il existe un ouvert U de $\mathbf{S} \otimes_k \bar{k}$ et un système local irréductible L sur $\mathbf{U} \cap \mathbf{Z}$ tel que $i_*\mathrm{L}[\dim(\mathbf{Z})]$ soit un facteur direct de $^p\mathrm{H}^n(f_*\bar{\mathbf{Q}}_\ell)|_{\mathrm{U}}$. Ceci implique que $i_*\mathrm{L}[\dim(\mathbf{Z}) - n]$ est un facteur direct du complexe $f_*\bar{\mathbf{Q}}_\ell|_{\mathrm{U}}$ puisque celui-ci est pur. En prenant maintenant le faisceau de cohomologie ordinaire, le faisceau $i_*\mathrm{L}$ devient un facteur direct de $\mathrm{H}^{n-\dim(\mathbf{Z})}(f_*\bar{\mathbf{Q}}_\ell)$. Comme les fibres du morphisme $f: \mathbf{M} \to \mathbf{S}$ sont purement de dimension $d$, on a $\dim(\mathbf{M}) = d + \dim(\mathbf{S})$. D'autre part, la non-annulation de $\mathrm{H}^{n-\dim(\mathbf{Z})}(f_*\bar{\mathbf{Q}}_\ell)$ implique que

$$
\dim (\mathrm{M}) - \dim (\mathrm{Z}) \leq n - \dim (\mathrm{Z}) \leq 2 d
$$

d'après le théorème d'amplitude cohomologique. En combinant les deux informations, on obtient l'inégalité désirée

$$
\operatorname{codim} (Z) \leq d
$$

ainsi que la condition nécessaire pour que l'égalité ait lieu.

Dans la situation plus spécifique d'une fibration abélienne faible, il est en fait possible d'améliorer l'inégalité de Goresky-MacPherson

$$
\operatorname{codim} (Z) \leq d
$$

en l'inégalité delta 7.2.2

$$
\operatorname{codim} (Z) \leq \delta_ {Z}.
$$

Bien que la démonstration de cette dernière est sensiblement plus difficile, l'idée topologique sous-jacente est très simple.

L'inégalité delta peut se ramener à celle de Goresky-MacPherson si on admet l'existence de certains relèvements locaux. Soit $s$ un point géométrique de Z tel que $\delta_s = \delta_Z$. Notons $A_s$ le quotient abélien maximal de $P_s^0$. Supposons qu'il existe un voisinage étale $S'$ de $s$ dans S tel qu'au-dessus de $S'$, la variété abélienne $A_s$ puisse s'étendre en un schéma abélien $A_{S'}$ et de plus, il existe un homomorphisme $A_{S'} \to P_{S'}^0$ tel qu'en le point $s$, la composition $A_s \to P_s^0 \to A_s$ soit une isogénie de $A_s$. Au-dessus de $S'$, le schéma abélien $A_{S'}$ agit sur $M_{S'}$ avec stabilisateurs finis compte tenu de l'hypothèse 7.1.3. En formant le quotient $[M_{S'} / A_{S'}]$, on factorise le morphisme $M_{S'} \to S'$ en un morphisme $M_{S'} \to [M_{S'} / A_{S'}]$ qui est propre et lisse suivi d'un morphisme $[M_{S'} / A_{S'}] \to S'$ qui est purement de dimension relative $\delta_s$. On peut alors appliquer l'inégalité de Goresky-MacPherson au second morphisme.

En général, ces relèvements n'existent pas. La démonstration de 7.2.2 consiste en fait à transposer l'argument géométrique ci-dessus au niveau cohomologique.

Soit Z un sous-schéma fermé irréductible de S. Nous avons introduit dans la démonstration de 7.3.1, l'ensemble $\mathrm{occ}(\mathbf{Z})$ des occurrences de Z comme support des facteurs irréductibles des faisceaux pervers de cohomologie $^b\mathrm{H}^n (f_*\bar{\mathbf{Q}}_\ell)$. Dans le cas où cet ensemble est non vide, on définit

$$
\operatorname{amp} (Z) = \max (\operatorname{occ} (Z)) - \min (\operatorname{occ} (Z)).
$$

Proposition 7.3.2. — Mettons-nous sous les hypothèses de 7.2.2. En particulier, occ(Z) ≠ ∅. On a alors l'inégalité

$$
\mathrm{amp} (\mathbf {Z}) \geq 2 (d - \delta_ {\mathbf {Z}}).
$$

Nous démontrons maintenant 7.2.2 en admettant 7.3.2. La dualité de Poincaré implique que l'ensemble $\mathrm{occ}(\mathbf{Z})$ est symétrique par rapport à $\dim(\mathbf{M})$. La contrainte supplémentaire $\mathrm{amp}(\mathbf{Z}) \geq 2(d - \delta_{\mathbf{Z}})$ force l'existence d'un entier $n \geq \dim(\mathbf{M}) + d - \delta_{\mathbf{Z}}$ appartenant à $\mathrm{occ}(\mathbf{Z})$. La suite de la démonstration de 7.2.2 est maintenant exactement la même que la fin de la démonstration de 7.3.1.

Le reste du chapitre est consacré à la démonstration de l'inégalité d'amplitude 7.3.2.

7.4. Cap-produit et liberté. — Nous allons développer la construction du cap-produit et énoncer une propriété de liberté qui implique l’inégalité d’amplitude 7.3.2.

7.4.1. — Nous nous plaçons dans la situation générale suivante. Soit S un schéma quelconque. Soit  $g: P \rightarrow S$  un S-schéma en groupes de type lisse commutatif de fibres connexes de dimension d. Considérons le complexe d'homologie de P sur S défini par la formule

$$
\Lambda_ {\mathrm{P}} = g _ {!} \bar {\mathbf {Q}} _ {\ell} [ 2 d ] (d).
$$

Ce complexe est concentré en degrés négatifs. En degré 0, on a  $H^{0}(\Lambda_{\mathrm{P}})=\bar{\mathbf{Q}}_{\ell}$ . La partie la plus importante de  $\Lambda_{P}$  est

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P}) := \mathrm{H} ^ {- 1} (\Lambda_ {\mathrm{P}})
$$

où  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P})$  est un faisceau dont la fibre en chaque point géométrique  $s \in S$  est le  $\bar{Q}_{\ell}$ -module de Tate  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P}_{s})$  de la fibre de P en s. Plus généralement, le théorème de changement de base nous fournit un isomorphisme

$$
\mathrm{H} ^ {- i} (\Lambda_ {\mathrm{P}}) _ {s} = \mathrm{H} _ {c} ^ {2 d - i} (\mathrm{P} _ {s}) (d)
$$

entre la fibre en s de  $\mathrm{H}^{-i}(\Lambda_{\mathrm{P}})$  et le  $(2d-i)$ -ième groupe de cohomologie à support compact

$$
\mathrm{H} _ {i} (\mathrm{P} _ {s}) = \mathrm{H} _ {c} ^ {2 d - i} (\mathrm{P} _ {s}) (d)
$$

de la fibre de P en s.

7.4.2. — Soit  $f: M \rightarrow S$  un morphisme de type fini muni d'une action de P relativement à la base S

$$
\mathrm{act}: \mathrm{P} \times_ {\mathrm{S}} \mathrm{M} \rightarrow \mathrm{M}.
$$

Puisque P est lisse de dimension relative d sur S, le morphisme act est aussi lisse de même dimension relative. On a donc un morphisme de trace

$$
\mathrm{act} _ {!} \bar {\mathbf {Q}} _ {\ell} [ 2 d ] (d) \rightarrow \bar {\mathbf {Q}} _ {\ell}
$$

au-dessus de M. En poussant ce morphisme de trace par $f_{!}$, on obtient un morphisme

$$
(g \times_ {\mathrm{S}} f)! \bar {\mathbf {Q}} _ {\ell} [ 2 d ] (d) \rightarrow f! \bar {\mathbf {Q}} _ {\ell}.
$$

En utilisant maintenant l'isomorphisme de Kunneth, on obtient un morphisme de cap-produit

$$
\Lambda_ {\mathrm{P}} \otimes f _ {!} \bar {\mathbf {Q}} _ {\ell} \rightarrow f _ {!} \bar {\mathbf {Q}} _ {\ell}.
$$

7.4.3. — Cette construction s'applique en particulier à f = g. Elle définit alors un morphisme de complexes

$$
\Lambda_ {\mathrm{P}} \otimes \Lambda_ {\mathrm{P}} \to \Lambda_ {\mathrm{P}}.
$$

On en déduit une structure d'algèbres graduées sur les faisceaux de cohomologie de $\Lambda_{\mathrm{P}}$

$$
\mathrm{H} ^ {- i} (\Lambda_ {\mathrm{P}}) \otimes \mathrm{H} ^ {- j} (\Lambda_ {\mathrm{P}}) \rightarrow \mathrm{H} ^ {- i - j} (\Lambda_ {\mathrm{P}})
$$

qui est commutative au sens gradué. On en déduit en particulier un morphisme de faisceaux

$$
\wedge^ {i} \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P}) \rightarrow \mathrm{H} ^ {- i} (\Lambda_ {\mathrm{P}})
$$

qui est en fait un isomorphisme. Pour le vérifier, il suffit de le faire fibre par fibre où on retrouve les groupes d'homologie de  $P_{s}$  munis du produit de Pontryagin.

7.4.4. — La multiplication par un entier  $N \neq 0$  dans P induit la multiplication par N sur le module de Tate  $T_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P})$  de P et induit donc la multiplication par  $N^{i}$  sur  $H^{-i}(\Lambda_{\mathrm{P}}) = \wedge^{i}T_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P})$ . L'astuce de Lieberman [37, 2A11] qui consiste à construire des projecteurs à partir des combinaisons linéaires de ces endomorphismes de  $\Lambda_{P}$ , associés à différents N, permet de décomposer canoniquement ce complexe

$$
\Lambda_ {\mathrm{P}} = \bigoplus_ {i \geq 0} \wedge^ {i} \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P}) [ i ]
$$

de façon compatible à la multiplication.

7.4.5. — On va maintenant étudier l'action par cap-produit de  $\Lambda_{P}$  sur  $f_{!}\bar{Q}_{\ell}$  dans la situation de 7.2.2. Rappelons que le morphisme f étant supposé projectif, on a  $f_{!}=f_{*}$ . Par ailleurs, le faisceau constant  $\bar{Q}_{\ell}$  sur M étant supposé pur, l'image directe  $f_{*}\dot{\bar{Q}}_{\ell}$  est aussi pure et se décompose au-dessus de  $S\otimes_{k}\bar{k}$  en somme directe de faisceaux pervers irréductibles avec décalage.

Pour tout fermé irréductible Z de  $S \otimes_{k} \bar{k}$ , on a introduit l'ensemble  $\operatorname{occ}(Z)$  dans la démonstration de 7.3.1. Comme  $f_{*}\bar{\mathbf{Q}}_{\ell}$  est un complexe borné constructible, l'ensemble  $\operatorname{occ}(Z)$  est vide sauf pour un nombre fini de sous-schémas fermés irréductibles Z de  $S \otimes_{k} \bar{k}$ . Nous numérotons ceux-ci par un ensemble fini A et pour tout  $\alpha \in A$ , nous notons  $Z_{\alpha}$  le fermé irréductible correspondant. Pour tout n, on a alors la décomposition canonique

$$
{ } ^ { p } \mathrm{H} ^ { n } ( f _ { * } \bar { \mathbf { Q } } _ { \ell } ) = \bigoplus _ { \alpha \in \mathfrak { A } } \mathrm{K} _ { \alpha } ^ { n }
$$

où  $K_{\alpha}^{n}$  est la somme directe des facteurs pervers irréductibles de  ${}^{b}\mathrm{H}^{n}(f_{!}\bar{\mathbf{Q}}_{\ell})$  ayant pour support le fermé irréductible  $Z_{\alpha}$ . Nous notons

$$
\mathrm{K} _ {\alpha} = \bigoplus_ {n \in \mathbf {Z}} \mathrm{K} _ {\alpha} ^ {n} [ - n ].
$$

Supposons que  $K_{\alpha}$  est non nul pour tout  $\alpha \in A$ .

7.4.6. — Compte tenu de la décomposition 7.4.4, on dispose d'un cap-produit par le module de Tate 7.4.2

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P}) \otimes f _ {!} \bar {\mathbf {Q}} _ {\ell} \rightarrow f _ {!} \bar {\mathbf {Q}} _ {\ell} [ - 1 ].
$$

En appliquant le foncteur  $^{p}\tau^{\leq n}$  à  $f_{!}\bar{Q}_{\ell}$ , on dispose d'un morphisme

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P}) \otimes {} ^ {p} \tau^ {\leq n} (f _ {!} \bar {\mathbf {Q}} _ {\ell}) \rightarrow f _ {!} \bar {\mathbf {Q}} _ {\ell} [ - 1 ]
$$

pour tout n. En appliquant le foncteur  $^{p}H^{n}$ , on obtient maintenant une flèche

$$
{ } ^ { p } \mathrm{H} ^ { n } ( \mathrm{T} _ { \bar { \mathbf { Q } } _ { \ell } } ( \mathrm{P} ) \otimes { } ^ { p } \tau ^ { \leq n } ( f _ { ! } \bar { \mathbf { Q } } _ { \ell } ) ) \to { } ^ { p } \mathrm{H} ^ { n - 1 } ( f _ { ! } \bar { \mathbf { Q } } _ { \ell } ) .
$$

Remarquons maintenant que  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P})\otimes{}^{p}\tau^{\leq n-1}(f_{!}\bar{\mathbf{Q}}_{\ell})\in{}^{p}\mathrm{D}_{c}^{\leq n-1}(\mathrm{S},\bar{\mathbf{Q}}_{\ell})$  si bien que la flèche

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P}) \otimes {} ^ {p} \tau^ {\leq n} (f _ {!} \bar {\mathbf {Q}} _ {\ell}) \rightarrow \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P}) \otimes {} ^ {p} \mathrm{H} ^ {n} (f _ {!} \bar {\mathbf {Q}} _ {\ell}) [ - n ]
$$

induit un isomorphisme au niveau des n-ièmes faisceaux pervers de cohomologie

$$
{ } ^ { p } \mathrm{H} ^ { n } ( \mathrm{T} _ { \bar { \mathbf { Q } } _ { \ell } } ( \mathrm{P} ) \otimes { } ^ { p } \tau ^ { \leq n } ( f _ { ! } \bar { \mathbf { Q } } _ { \ell } ) ) \to { } ^ { p } \mathrm{H} ^ { 0 } ( \mathrm{T} _ { \bar { \mathbf { Q } } _ { \ell } } ( \mathrm{P} ) \otimes { } ^ { p } \mathrm{H} ^ { n } ( f _ { ! } \bar { \mathbf { Q } } _ { \ell } ) ) .
$$

On en déduit une flèche

$$
{ } ^ { p } \mathrm{H} ^ { 0 } ( \mathrm{T} _ { \bar { \mathbf { Q } } _ { \ell } } ( \mathrm{P} ) \otimes { } ^ { p } \mathrm{H} ^ { n } ( f _ { ! } \bar { \mathbf { Q } } _ { \ell } ) ) \to { } ^ { p } \mathrm{H} ^ { n - 1 } ( f _ { ! } \bar { \mathbf { Q } } _ { \ell } ) .
$$

De nouveau, comme  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P})\otimes{}^{p}\mathrm{H}^{n}(f_{!}\bar{\mathbf{Q}}_{\ell})\in{}^{p}\mathrm{D}_{c}^{\leq0}(\mathrm{S},\bar{\mathbf{Q}}_{\ell})$ , on a une flèche de cet objet dans son  ${}^{p}H^{0}$  laquelle induit donc une flèche canonique

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P}) \otimes {} ^ {p} \mathrm{H} ^ {n} (f _ {!} \bar {\mathbf {Q}} _ {\ell}) \rightarrow {} ^ {p} \mathrm{H} ^ {n - 1} (f _ {!} \bar {\mathbf {Q}} _ {\ell}).
$$

7.4.7. — Considérons la décomposition par les supports

$$
\bigoplus_ {\alpha \in \mathfrak {A}} \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P}) \otimes \mathrm{K} _ {\alpha} ^ {n} \rightarrow \bigoplus_ {\alpha \in \mathfrak {A}} \mathrm{K} _ {\alpha} ^ {n - 1}.
$$

Pour tout $\alpha\in\mathfrak{A}$, on a donc une flèche diagonale

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P}) \otimes \mathrm{K} _ {\alpha} ^ {n} \to \mathrm{K} _ {\alpha} ^ {n - 1}.
$$

Notons qu'il n'est pas exclu que les flèches non diagonales

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P}) \otimes \mathrm{K} _ {\alpha} ^ {n} \rightarrow \mathrm{K} _ {\alpha^ {\prime}} ^ {n - 1}
$$

soient non nulles.

7.4.8. — Pour tout $\alpha \in \mathfrak{A}$, il existe un ouvert dense $V_{\alpha}$ de $Z_{\alpha}$ tel que la restriction du faisceau pervers $K_{\alpha}^{n}$ à $V_{\alpha}$ soit de la forme $\mathcal{K}_{\alpha}^{n}[\dim(V_{\alpha})]$ où $\mathcal{K}_{\alpha}^{n}$ est un système local pur de poids $n$.

Quitte à rétrécir l'ouvert  $V_{\alpha}$ , il existe un changement de base fini radiciel  $V'_{\alpha} \to V_{\alpha}$  tel que le schéma en groupes  $P|_{V'_{\alpha}}$  admet un dévissage

$$
1 \to \mathrm{R} _ {\alpha} \to \mathrm{P} | _ {\mathrm{V} _ {\alpha} ^ {\prime}} \to \mathrm{A} _ {\alpha} \to 1
$$

où  $A_{\alpha}$  est un  $V'_{\alpha}$ -schéma abélien et où  $R_{\alpha}$  est un  $V'_{\alpha}$ -schéma en groupes affine lisse commutatif à fibres connexes. On en déduit une suite exacte de modules de Tate

$$
0 \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{R} _ {\alpha}) \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P} | _ {\mathrm{V} _ {\alpha} ^ {\prime}}) \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{A} _ {\alpha}) \to 0.
$$

Puisque le morphisme  $V_{\alpha}^{\prime} \rightarrow V_{\alpha}$  est un homéomorphisme, il est légitime de considérer  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{R}_{\alpha})$  et  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{\alpha})$  ainsi que la suite exacte ci-dessus comme objets existant sur  $V_{\alpha}$ . Comme  $A_{\alpha}$  est un schéma abélien, le module de Tate  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{\alpha})$  est un système local pur de poids -1. Quitte à rétrécir davantage  $V_{\alpha}$  si nécessaire, on peut supposer que  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{R}_{\alpha})$  qui est le module de Tate de la partie torique de  $R_{\alpha}$ , est un système local pur de poids -2. Ici, le poids dont on parle est relatif à une extension suffisamment grande du corps fini de base k sur lequel nos objets sont définis.

Quitte à rétrécir  $V_{\alpha}$  si nécessaire, on peut supposer que sauf si  $Z_{\alpha}$  est entièrement contenu dans  $Z_{\alpha'}$ , on a  $V_{\alpha} \cap Z_{\alpha'} = \emptyset$ .

7.4.9. — Soit  $V_{\alpha}$  un ouvert dense de  $Z_{\alpha}$  comme dans 7.4.8. Pour tout  $\alpha \in A$ , choisissons un ouvert de Zariski  $U_{\alpha}$  de  $S \otimes_{k} \bar{k}$  contenant  $V_{\alpha}$  comme un sous-schéma fermé. Notons  $i_{\alpha}: V_{\alpha} \to U_{\alpha}$  l'immersion fermée. En restreignant la flèche diagonale construite dans 7.4.7 à l'ouvert  $U_{\alpha}$ , on obtient une flèche

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P}) \otimes i _ {\alpha *} \mathcal {K} _ {\alpha} ^ {n} [ \dim (\mathrm{V} _ {\alpha}) ] \rightarrow i _ {\alpha *} \mathcal {K} _ {\alpha} ^ {n - 1} [ \dim (\mathrm{V} _ {\alpha}) ].
$$

Par la formule de projection, on a

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P}) \otimes i _ {\alpha *} \mathcal {K} _ {\alpha} ^ {n} = i _ {\alpha *} (i _ {\alpha} ^ {*} \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P} _ {\alpha}) \otimes \mathcal {K} _ {\alpha}).
$$

En appliquant le foncteur $i_{\alpha}^{*}$ à

$$
i _ {\alpha *} (i _ {\alpha} ^ {*} \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P} _ {\alpha}) \otimes \mathcal {K} _ {\alpha} ^ {n}) \to i _ {\alpha *} \mathcal {K} _ {\alpha} ^ {n - 1}
$$

on obtient un morphisme

$$
i _ {\alpha} ^ {*} \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P} _ {\alpha}) \otimes \mathcal {K} _ {\alpha} ^ {n} \to \mathcal {K} _ {\alpha} ^ {n - 1}
$$

sur  $V_{\alpha}$ .

D'après 7.4.8, on a un dévissage de $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P}_{\alpha})$

$$
0 \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{R} _ {\alpha}) \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P} _ {\alpha}) \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{A} _ {\alpha}) \to 0
$$

où  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{\alpha})$  est un système local pur de poids -1 et  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{R}_{\alpha})$  est un système local pur de poids -2. Puisque  $K_{\alpha}^{n}$  est pur de poids n et  $K_{\alpha}^{n-1}$  est pur de poids n-1, l'action de  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P}_{\alpha})$  se factorise par  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{\alpha})$

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{A} _ {\alpha}) \otimes \mathcal {K} _ {\alpha} ^ {n} \to \mathcal {K} _ {\alpha} ^ {n - 1}.
$$

On a donc muni la somme directe de systèmes locaux $\mathcal{K}_{\alpha} = \bigoplus_{n}\mathcal{K}_{\alpha}^{n}[-n]$ d'une structure de module gradué sur l'algèbre graduée de systèmes locaux $\Lambda_{\mathrm{A}_{\alpha}}$

$$
\Lambda_ {\mathrm{A} _ {\alpha}} \otimes \mathcal {K} _ {\alpha} \to \mathcal {K} _ {\alpha}.
$$

En particulier, pour tout point géométrique  $u_{\alpha}$  de  $V_{\alpha}$ , la fibre  $K_{\alpha,u_{\alpha}}$  est un module gradué sur l'algèbre graduée de  $\Lambda_{A_{\alpha},u_{\alpha}}$ .

Proposition 7.4.10. — Mettons-nous sous les hypothèses de 7.2.2 et les notations de 7.4.5, 7.4.8 et 7.4.9. Pour tout point géométrique $u_{\alpha}$ de $\mathrm{V}_{\alpha}$, la fibre $\mathcal{K}_{\alpha,u_{\alpha}}$ de $\mathcal{K}_{\alpha}$ est un module gradué libre sur l'algèbre graduée $\Lambda_{\mathrm{A}_{\alpha},u_{\alpha}}$.

L'inégalité d'amplitude 7.3.2 est une conséquence immédiate de cette propriété de liberté. En effet, $\mathrm{amp}(Z_{\alpha})$ est alors au moins égale à

$$
2 \dim (\mathrm{A} _ {\alpha}) = 2 (d - \delta_ {\alpha}).
$$

Le reste du chapitre est consacré à la démonstration de la propriété de liberté 7.4.10. Mais avant d'entamer la démonstration proprement dite de 7.4.10, nous observons que la propriété $\mathcal{K}_{\alpha,u_{\alpha}}$ est un module libre sur $\Lambda_{\alpha,u_{\alpha}}$ est indépendante du choix du point géométrique $u_{\alpha}\in\mathrm{V}_{\alpha}$. On va démontrer l'énoncé suivant qui permet de formuler cette propriété de liberté de façon indépendante du point base. Observons que sous les hypothèses de pureté de 7.4.10, les systèmes locaux $\mathcal{K}_{\alpha}^{n}$ sont géométriquement semi-simples.

Lemme 7.4.11. — Soit U un $\bar{k}$-schéma connexe. Soit $\Lambda$ un système local gradué en un nombre fini de degrés négatifs avec $\Lambda^0 = \bar{\mathbf{Q}}_\ell$ et qui est muni d'une structure d'algèbres graduées $\Lambda \otimes \Lambda \to \Lambda$. Soit L un système local gradué muni d'une structure de module gradué

$$
\Lambda \otimes \mathrm{L} \to \mathrm{L}.
$$

Supposons qu'il existe un point géométrique u de U tel que la fibre  $L_{u}$  de L en u est un module libre sur la fibre  $\Lambda_{u}$  de  $\Lambda$  en u. Supposons que L est semi-simple comme système local gradué. Alors, il existe un système local gradué E sur U et un isomorphisme

$$
\mathrm{L} = \Lambda \otimes \mathrm{E}
$$

compatible avec la structure de $\Lambda$-modules.

Démonstration. — Considérons l'idéal d'augmentation de $\Lambda$

$$
\Lambda^ {+} = \bigoplus_ {i > 0} \Lambda^ {- i} [ i ].
$$

Notons E le conoyau de la flèche

$$
\Lambda^ {+} \otimes \mathrm{L} \to \mathrm{L}.
$$

Puisque L est semi-simple, l'homomorphisme surjectif L → E admet un relèvement E → L. On va montrer que la flèche induite

$$
\Lambda \otimes \mathrm{E} \to \mathrm{L}
$$

est un isomorphisme. Puisqu'il s'agit d'une flèche entre systèmes locaux, pour vérifier que c'est un isomorphisme, il suffit de vérifier que sa fibre en $u$ est un isomorphisme. Dans l'espace vectoriel $\mathrm{L}_u$, $\mathrm{E}_u$ est un sous-espace vectoriel complémentaire de $\Lambda^{+}\mathrm{L}_{u}$. La flèche

$$
\Lambda_ {u} \otimes \mathrm{E} _ {u} \to \mathrm{L} _ {u}
$$

est donc surjective d'après le lemme de Nakayama. Elle est bijective car  $L_{u}$  étant un  $\Lambda_{u}$ -module libre, on a l'égalité de dimension

$$
\dim_ {\bar {\mathbf {Q}} _ {\ell}} (\Lambda_ {u}) \times \dim_ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{E} _ {u}) = \dim_ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{L} _ {u})
$$

d'où le lemme.

7.5. Propriété de liberté dans le cas ponctuel. — Nous commençons par considérer des énoncés analogues à 7.4.10 dans le cas où la base est ponctuelle.

Proposition 7.5.1. — Soit M un schéma projectif sur un corps algébriquement clos $\overline{k}$ muni d'une action d'une $\overline{k}$-variété abélienne A avec stabilisateurs finis. Alors

$$
\bigoplus_ {n} \mathrm{H} _ {c} ^ {n} (\mathbf {M} \otimes_ {k} \bar {k}) [ - n ]
$$

est un module libre sur l'algèbre graduée $\Lambda_{\mathrm{A}} = \bigoplus_{i} \wedge^{i}\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A})[i]$.

Démonstration. — Puisque le stabilisateur dans A de tout point de M est un sous-groupe fini, le quotient N = [M/A] est champ algébrique propre sur k avec inertie finie. Puisque M est projectif, le morphisme M → N est un morphisme projectif et lisse. Le cup-produit avec la classe hyperplane induit d'après Deligne [19] un isomorphisme

$$
m _ {*} \bar {\mathbf {Q}} _ {\ell} \simeq \bigoplus_ {i} \mathrm{R} ^ {i} m _ {*} \bar {\mathbf {Q}} _ {\ell} [ - i ]
$$

où les  $\mathrm{R}^{i}(m_{*}\bar{\mathbf{Q}}_{\ell})$  sont des systèmes locaux sur N. Puisque  $M \times_{N} M = A \times M$ , l'image inverse  $m^{*}\mathrm{R}^{i}(m_{*}\bar{\mathbf{Q}}_{\ell})$  est le faisceau constant de valeur  $\mathrm{H}^{i}(\mathrm{A})$  sur M. En utilisant cf. [7, 4.2.5], on obtient un isomorphisme canonique entre  $\mathrm{R}^{i}(m_{*}\bar{\mathbf{Q}}_{\ell})$  et le faisceau constant sur N de valeur  $\mathrm{H}^{i}(\mathrm{A})$ .

La décomposition en somme directe ci-dessus implique la dégénérescence de la suite spectrale

$$
\mathrm{H} _ {c} ^ {j} (\mathrm{N}, \mathrm{R} ^ {i} m _ {*} \bar {\mathbf {Q}} _ {\ell}) \Rightarrow \mathrm{H} _ {c} ^ {i + j} (\mathrm{M}).
$$

On en déduit dans $\bigoplus_{n}\mathrm{H}_{c}^{n}(\mathbf{M})$ une filtration $\Lambda_{\mathrm{A}}$-stable dont le $j$-ième gradué est

$$
\bigoplus_ {i} \mathrm{H} _ {c} ^ {j} (\mathrm{N}, \mathrm{R} ^ {i} m _ {*} \bar {\mathbf {Q}} _ {\ell}) = \mathrm{H} _ {c} ^ {j} (\mathrm{N}) \otimes \bigoplus_ {i} \mathrm{H} ^ {i} (\mathrm{A} _ {s}).
$$

Ces gradués sont des $\Lambda_{\mathrm{A}}$-modules libres. Il en résulte que la somme directe $\bigoplus_{n} \mathrm{H}_{c}^{n}(\mathrm{M})[-n]$ est un $\Lambda_{\mathrm{A}}$-module libre.

7.5.2. — Soit P un groupe algébrique commutatif lisse et connexe sur un corps algébriquement clos  $\bar{k}$ . D'après le théorème de Chevalley cf. [66], P admet un dévissage comme une extension d'une variété abélienne par un groupe affine

$$
1 \rightarrow \mathrm{R} \rightarrow \mathrm{P} \rightarrow \mathrm{A} \rightarrow 1.
$$

Cette suite exacte existe également si P est défini sur un corps parfait, en particulier sur un corps fini.

On déduit de la suite exacte ci-dessus une suite exacte de modules de Tate

$$
0 \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{R}) \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P}) \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{A}) \to 0.
$$

On appelle relèvement homologique une application linéaire

$$
\lambda : \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{A}) \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P})
$$

qui scinde cette suite exacte. Un relèvement homologique induit un homomorphisme d'algèbres $\lambda : \Lambda_{\mathrm{A}} \to \Lambda_{\mathrm{P}}$. L'ensemble des relèvements homologiques de la partie abélienne forment un espace affine, torseur sous le $\tilde{\mathbf{Q}}_{\ell}$-espace vectoriel $\operatorname{Hom}(\mathrm{T}_{\tilde{\mathbf{Q}}_{\ell}}(\mathrm{A}), \mathrm{T}_{\tilde{\mathbf{Q}}_{\ell}}(\mathrm{R}))$.

Proposition 7.5.3. — Soit P un groupe algébrique commutatif lisse et connexe défini sur un corps fini k. Soit

$$
1 \to \mathrm{R} \to \mathrm{P} \to \mathrm{A} \to 1
$$

la suite exacte canonique qui réalise P comme une extension d'une variété abélienne A par un groupe affine R. Il existe alors un entier N > 0 et un homomorphisme a : A → P tel qu'en le composant avec P → A, on obtient la multiplication par N dans A. On dira alors que a est un quasi-relèvement.

De plus,  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(a):\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A})\to\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P})$  est l'application induite sur les modules de Tate, alors  $\mathrm{N}^{-1}\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(a)$  est l'unique relèvement homologique compatible à l'action de  $\mathrm{Gal}(\bar{k}/k)$  sur  $\mathrm{T}_{\ell}(\mathrm{P})$  et  $\mathrm{T}_{\ell}(\mathrm{A})$ . On dira que  $\mathrm{N}^{-1}\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(a)$  est le relèvement canonique.

Démonstration. — D'après [69, p. 184], le groupe des extensions d'une variété abélienne A par $\mathbf{G}_{m}$ s'identifie au groupe des $k$-points de la variété abélienne duale. Le groupe des extensions d'une variété abélienne par $\mathbf{G}_{a}$ est le $k$-espace vectoriel de dimension finie $\mathrm{H}^{1}(\mathrm{A},\mathcal{O}_{\mathrm{A}})$. Un groupe affine commutatif lisse connexe est isomorphe à un produit de $\mathbf{G}_{m}$ et de $\mathbf{G}_{a}$ après passage à une extension finie du corps de base, il s'ensuit que le groupe des extensions d'une variété abélienne A par un groupe affine commutatif lisse R défini sur un corps fini, est un groupe fini. La première assertion s'en déduit.

Le relèvement homologique  $\mathrm{N}^{-1}\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(a)$  est invariant sous l'action de  $\operatorname{Gal}(\bar{k}/k)$  puisque le relèvement a est défini sur k. L'élément de Frobenius  $\sigma\in\operatorname{Gal}(\bar{k}/k)$  agit sur  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A})$  avec des valeurs propres de valeur absolue  $|k|^{-1/2}$  et sur  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{R})$  avec des valeurs propres de valeur absolue  $|k|^{-1}$ . Ainsi,  $\mathrm{N}^{-1}\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(a)$  est l'unique relèvement homologique compatible avec l'action de  $\operatorname{Gal}(\bar{k}/k)$ .

Corollaire 7.5.4. — Soit $\bar{k}$ un corps algébriquement clos. Soit M un $\bar{k}$-schéma de type fini. Soit P un $\bar{k}$-schéma en groupes lisse commutatif et connexe agissant sur M avec stabilisateur affine. Soit A le quotient abélien maximal de P. Supposons que P est défini sur un corps fini de sorte qu'on a un quasi-relèvement $a: A \to P$. Alors le $\Lambda_{A}$-module qui se déduit du $\Lambda_{P}$-module $\bigoplus_{n} H_{c}^{n}(M)$ est un module libre.

Démonstration. — Le quasi-relèvement  $a: A \rightarrow P$  définit une action de A sur M avec stabilisateurs finis. On se ramène donc immédiatement à la proposition 7.5.1. ☐

Voici un énoncé plus général et plus satisfaisant. La démonstration qui suit est due à Deligne cf. [20]. Notons que cet énoncé ne sera pas utilisé dans la suite. En fait, le lemme 7.4.11 jouera le rôle de l'indépendance du relèvement dans la démonstration de 7.4.10.

Proposition 7.5.5. — Soit $\bar{k}$ un corps algébriquement clos. Soit M un $\bar{k}$-schéma projectif. Soit P un $\bar{k}$-groupe lisse commutatif et connexe agissant sur M avec stabilisateur affine. Soit A le quotient abélien maximal de P et soit $\lambda: T_{\tilde{\mathbf{Q}}_{\ell}}(A) \to T_{\tilde{\mathbf{Q}}_{\ell}}(P)$ n'importe quel relèvement homologique. Alors le $\Lambda_{\mathrm{A}}$-module qui se déduit du $\Lambda_{\mathrm{P}}$-module $\bigoplus_{n} H_{c}^{n}(M)$ par $\lambda$ est un module libre.

Démonstration. — Par le procédé général de passage à la limite inductive comme dans [7, 6.1.7], on se ramène au cas où M, P et l'action de P sur M sont définis sur un corps fini k. Écrivons $\bar{k}$ comme une limite inductive $(\mathrm{A}_i)_{i\in \mathrm{I}}$ des anneaux de type fini sur Z. La catégorie des $\bar{k}$-schémas de type fini est une 2-limite inductive des $\mathrm{A}_i$-schémas de type fini c'est-à-dire pour tout $\mathrm{X} / \bar{k}$, il existe $i\in \mathrm{I}$ et $\mathrm{X}_i / \mathrm{A}_i$ de type fini tel que $\mathrm{X} = \mathrm{X}_i\otimes_{\mathrm{A}_i}\bar{k}cf.$

[30, 8.9.1] et pour tous $\mathbf{X}_i$, $\mathrm{Y}_i / \mathrm{A}_i$, on a cf. [30, 8.8.2]

$$
\mathrm{Hom}_{\bar{k}}(\mathbf{X}_{i}\otimes_{\mathrm{A}_{i}}\bar{k},\mathbf{Y}_{i}\otimes_{\mathrm{A}_{i}}\bar{k}) = \lim_{\substack{\longrightarrow \\ j\geq i}}\mathrm{Hom}_{\mathrm{A}_{j}}(\mathbf{X}_{i}\otimes_{\mathrm{A}_{i}}\mathbf{A}_{j},\mathbf{Y}_{i}\otimes_{\mathrm{A}_{i}}\mathbf{A}_{j}).
$$

Le même énoncé vaut donc pour la catégorie des groupes algébriques et celle des triplets formés d'un groupe algébrique G, d'un schéma de type fini X et d'une action de G sur X. Soit  $f: X \to Y$  un morphisme dans la catégorie des  $\bar{k}$ -schémas de type fini provenant d'un morphisme  $f_i: X_i \to Y_i$  dans la catégorie des  $A_i$ -schémas. Pour que f ait l'une des propriétés suivantes : plat, lisse, affine ou projectif, il faut et il suffit que  $f_i$  acquière cette propriété après une extension de scalaires  $A_i \to A_j$  cf. [30, 11.2.6 et 8.10.5]. Il existe donc un anneau  $A_i$  de type fini sur Z contenu dans  $\bar{k}$, un  $A_i$ -schéma projectif  $M_i$, un  $A_i$ -schéma en groupes lisse  $P_i$, extension d'un schéma abélien par un schéma en groupes affine qui agit sur  $M_i$  avec stabilisateur affine tel qu'après l'extension des scalaires  $A_i \to \bar{k}$, on retrouve la situation de départ. On peut également supposer que les  $H^n(f_i! \bar{\mathbf{Q}}_\ell)$  sont des systèmes locaux. On a donc ramené l'énoncé à démontrer au cas où la base est le spectre d'un corps fini.

On peut donc supposer que M, P et l'action de P sur M sont définis sur un corps fini k. Soit A le quotient abélien de P et  $a: A \to P$  le quasi-relèvement qui définit un relèvement canonique  $\lambda_{0}: T_{\bar{\mathbf{Q}}_{\ell}}(A) \to T_{\bar{\mathbf{Q}}_{\ell}}(M)$  de modules de Tate. On sait déjà que le  $\Lambda_{A}$ -module qui se déduit du  $\Lambda_{P}$ -module  $\bigoplus_{n} H_{c}^{n}(M)$  par  $\lambda_{0}$  est un module libre d'après le corollaire précédent 7.5.4.

Démontrons maintenant le même énoncé pour un relèvement homologique arbitraire. L'espace de tous les relèvements homologiques, pointé par $\lambda_0$, s'identifie au $\bar{\mathbf{Q}}_\ell$-espace vectoriel $\mathrm{Hom}(\mathrm{T}_{\bar{\mathbf{Q}}_\ell}(\mathrm{A}_s), \mathrm{T}_{\bar{\mathbf{Q}}_\ell}(\mathrm{R}_s))$ sur lequel l'élément de Frobenius $\sigma \in \mathrm{Gal}(\bar{k}/k)$ agit avec des valeurs propres ayant pour valeur absolue $|k|^{1/2}$. Sur cet espace, l'ensemble des $\lambda$ pour lequel la structure de $\Lambda_{\mathrm{A}_s}$-module sur $\bigoplus_n \mathrm{H}_c^n(\mathrm{M})$ déduite de $\lambda$ est libre forme un ouvert Zariski de $\mathrm{Hom}(\mathrm{T}_{\bar{\mathbf{Q}}_\ell}(\mathrm{A}_s), \mathrm{T}_{\bar{\mathbf{Q}}_\ell}(\mathrm{R}_s))$. Cet ouvert est stable sous $\sigma$ et contient l'origine $\lambda_0$. Son complément est un fermé stable sous $\sigma$ qui ne contient pas $\lambda_0$. Puisque $\sigma$ agit avec des valeurs propres de valeur absolue $|k|^{1/2}$, un fermé de $\mathrm{Hom}(\mathrm{T}_{\bar{\mathbf{Q}}_\ell}(\mathrm{A}_s), \mathrm{T}_{\bar{\mathbf{Q}}_\ell}(\mathrm{R}_s))$ stable sous $\sigma$ est nécessairement stable sous l'action de $\mathbf{G}_m$. Le fait que ce fermé ne contient pas l'origine $\lambda_0$ implique qu'il est vide.

7.6. Étude sur une base hensélienne. — Dans ce paragraphe, nous allons étudier le cap-produit au-dessus d'une base hensélienne et analyser la suite spectrale aboutissant à la cohomologie de la fibre spéciale.

7.6.1. — Soit maintenant S un schéma strictement hensélien avec un morphisme  $\epsilon: S \to \operatorname{Spec}(\bar{k})$  où  $\bar{k}$  est le corps résiduel de S. Notons s le point fermé de S. La fibre  $\Lambda_{P,s}$  s'identifie alors avec  $\epsilon_{*}\Lambda_{P}$ . On en déduit par adjonction un morphisme

$$
\epsilon^ {*} \Lambda_ {\mathrm{P}, s} \rightarrow \Lambda .
$$

En restreignant le cap-produit 7.4.2 à $\epsilon^{*}\Lambda_{\mathrm{P},s}$, on obtient une flèche

$$
\Lambda_ {\mathrm{P}, s} \boxtimes f _ {!} \bar {\mathbf {Q}} _ {\ell} \rightarrow f _ {!} \bar {\mathbf {Q}} _ {\ell}
$$

qui définit une action de l'algèbre graduée $\Lambda_{\mathrm{P},s} = \bigoplus_{i}\wedge^{i}\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P}_{s})[i]$ sur le complexe $f_{i}\bar{\mathbf{Q}}_{\ell}$. En particulier, on a un morphisme

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} \left(\mathrm{P} _ {s}\right) \boxtimes f _ {!} \bar {\mathbf {Q}} _ {\ell} \rightarrow f _ {!} \bar {\mathbf {Q}} _ {\ell} [ - 1 ].
$$

On en déduit un morphisme entre les tronqués pour la t-structure perverse :

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} \left(\mathrm{P} _ {s}\right) \boxtimes^ {p} \tau^ {\leq n} \left(f _ {!} \bar {\mathbf {Q}} _ {\ell}\right)\rightarrow {} ^ {p} \tau^ {\leq n - 1} \left(f _ {!} \bar {\mathbf {Q}} _ {\ell}\right)
$$

pour tout  $n \in Z$ . Ceci induit un morphisme entre les faisceaux pervers de cohomologie en degrés n et n - 1

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} \left(\mathrm{P} _ {s}\right) \boxtimes {} ^ {p} \mathrm{H} ^ {n} \left(f _ {!} \bar {\mathbf {Q}} _ {\ell}\right)\rightarrow {} ^ {p} \mathrm{H} ^ {n - 1} \left(f _ {!} \bar {\mathbf {Q}} _ {\ell}\right)
$$

d'où une action de $\Lambda_{\mathrm{P},s}$ sur la somme directe $\bigoplus_{n}{}^{p}\mathrm{H}^{n}(f_{!}\bar{\mathbf{Q}}_{\ell})$.

7.6.2. — Cette flèche est compatible avec celle construite à la fin de 7.4.6. Par rapport à la décomposition par le support

$$
{ } ^ { p } \mathrm{H} ^ { n } ( f _ { ! } \bar { \mathbf { Q } } _ { \ell } ) = \bigoplus _ { \alpha \in \mathfrak { A } } \mathrm{K} _ { \alpha } ^ { n }
$$

elle s'exprime en termes d'une matrice ayant l'entrée indexée par un couple  $(\alpha, \alpha')$  un élément de

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P} _ {s}) ^ {*} \otimes \operatorname{Hom} \left(\mathrm{K} _ {\alpha} ^ {n}, \mathrm{K} _ {\alpha^ {\prime}} ^ {n - 1}\right).
$$

Les flèches diagonales sont compatibles avec celles de 7.4.7 alors que les flèches non diagonales sont ici clairement nulles car $\mathrm{Hom}(\mathbf{K}_{\alpha}^{n},\mathbf{K}_{\alpha^{\prime}}^{n - 1}) = 0$ si $\alpha \neq \alpha^{\prime}$.

7.6.3. — La filtration  $^{p}\tau^{\leq n}(f_{!}\bar{\mathbf{Q}}_{\ell})$  de  $f_{!}\bar{\mathbf{Q}}_{\ell}$  définit une suite spectrale

$$
\mathrm{E} _ {2} ^ {m, n} = \mathrm{H} ^ {m} (^ {p} \mathrm{H} ^ {n} (f _ {!} \bar {\mathbf {Q}} _ {\ell}) _ {s}) \Rightarrow \mathrm{H} _ {c} ^ {m + n} (\mathrm{M} _ {s})
$$

équivariante par rapport à l'action de $\Lambda_{\mathrm{P},s}$. Cette suite spectrale est convergente car le complexe $f_{!}\bar{\mathbf{Q}}_{\ell}$ est borné. On dispose donc sur la somme directe

$$
\mathrm{H} _ {c} ^ {\bullet} (\mathrm{M} _ {s}) = \bigoplus_ {r} \mathrm{H} _ {c} ^ {r} (\mathrm{M} _ {s}) [ - r ]
$$

d'une filtration décroissante  $\mathrm{F}^{m}\mathrm{H}_{c}(\mathrm{M}_{s})$  telle que

$$
\mathrm{F} ^ {m} \mathrm{H} _ {c} (\mathrm{M} _ {s}) / \mathrm{F} ^ {m + 1} \mathrm{H} _ {c} (\mathrm{M} _ {s}) = \bigoplus_ {n} \mathrm{E} _ {\infty} ^ {m, n} [ - m - n ].
$$

L'action de $\Lambda_{\mathrm{P},s}$ sur $\mathbf{H}_{c}^{\bullet}(\mathbf{M}_{s})$ respecte cette filtration. L'action induite sur les gradués associés à la filtration $\mathrm{F}^{m}\mathrm{H}_{c}(\mathrm{M}_{s})$

$$
\bigoplus_ {n} \mathrm{E} _ {\infty} ^ {m, n} [ - m - n ]
$$

se déduit de son action sur les  $E_{2}^{m,n}$  qui à son tour se déduit de l'action graduée de  $\Lambda_{P,s}$  sur  $\bigoplus_{n}{}^{p}\mathrm{H}^{n}(f_{!}\bar{\mathbf{Q}}_{\ell})[-n]$ .

7.6.4. — Mettons-nous maintenant sous les hypothèses de 7.2.2. On a en particulier $f_{!} = f_{*}$. En disposant également de la pureté, il existe un isomorphisme non-canonique sur $S \otimes_{k} \bar{k}$

$$
f _ {*} \bar {\mathbf {Q}} _ {\ell} \simeq \bigoplus_ {n \in \mathbf {Z}} ^ {p} \mathrm{H} ^ {n} (f _ {!} \bar {\mathbf {Q}} _ {\ell}) [ - n ].
$$

Cet isomorphisme subsiste quand on le restreint à l'hensélisé strict  $S_{s}$  d'un point géométrique s de S de sorte que les suites spectrales 7.6.3 dégénèrent en  $E_{2}$  c'est-à-dire  $E_{\infty}^{m,n} = E_{2}^{m,n}$ .

7.6.5. — Au niveau des faisceaux pervers de cohomologie, on dispose d'une décomposition canonique par le support

$$
{ } ^ { p } \mathrm{H} ^ { n } ( f _ { * } \bar { \mathbf { Q } } _ { \ell } ) = \bigoplus _ { \alpha \in \mathfrak { A } } \mathrm{K} _ { \alpha } ^ { n } .
$$

On a remarqué dans 7.6.2 qu'au-dessus d'une base strictement hensélienne, l'action de l'algèbre graduée $\Lambda_{\mathrm{P},s}$ sur la somme directe $\bigoplus_{n}{}^{p}\mathrm{H}^{n}(f_{*}\bar{\mathbf{Q}}_{\ell})$ respecte la décomposition selon le support. Il est bien tentant de rechercher un isomorphisme

$$
f _ {*} \bar {\mathbf {Q}} _ {\ell} \stackrel {{\sim}} {{\to}} \bigoplus_ {n} ^ {p} \mathrm{H} ^ {n} (f _ {*} \bar {\mathbf {Q}} _ {\ell})
$$

meilleur que les autres qui soit en particulier compatible à l'action de $\Lambda_{\mathrm{P},s}$ définie dans 7.6.1. On pourrait dans ce cas utiliser la liberté de l'aboutissement de la suite spectrale pour conclure la démonstration de 7.4.10. Toutefois, une décomposition en somme directe de $f_{*}\bar{\mathbf{Q}}_{\ell}$ compatible à l'action de $\Lambda_{\mathrm{P},s}$ ne semble pas exister.

On peut néanmoins démontrer 7.4.10 en se fondant sur la dégénérescence de la suite spectrale et en procédant par récurrence sur les strates. C'est ce qu'on va faire dans le paragraphe suivant.

7.7. Liberté par récurrence. — Dans ce paragraphe, on va terminer la démonstration de la propriété de liberté 7.4.10 et donc aussi celles de l’inégalité d’amplitude 7.3.2, de l’inégalité delta 7.2.2.

7.7.1. — Nous démontrons la proposition 7.4.10 par une récurrence descendante sur la dimension de  $Z_{\alpha}$ . Soit  $\alpha_{0} \in A$  l'élément maximal tel que  $Z_{\alpha_{0}}$  soit  $S \otimes_{k} \bar{k}$  tout entier. Soit  $V_{\alpha_{0}}$  un ouvert dense de  $S \otimes_{k} \bar{k}$  assez petit au sens de 7.4.8. Pour  $\alpha \neq \alpha_{0}$ , les autres strates  $Z_{\alpha}$  n'ayant pas d'intersection avec  $V_{\alpha_{0}}$ , la restriction du faisceau pervers de cohomologie  $^{p}\mathrm{H}^{n}(f_{*}\bar{\mathbf{Q}}_{\ell})$  à  $V_{\alpha_{0}}$  est un système local avec un décalage

$$
{ } ^ { p } \mathrm{H} ^ { n } ( f _ { * } \bar { \mathbf { Q } } _ { \ell } ) | _ { \mathrm{U} _ { \alpha _ { 0 } } } = \mathcal { K } _ { \alpha _ { 0 } } ^ { n } [ \dim ( S ) ] .
$$

Ici,  $K_{\alpha_{0}}^{n}$  est un système local semi-simple sur  $U_{\alpha_{0}}$  pur de poids n par hypothèse de pureté de 7.2.2.

Comme dans 7.4.8, au-dessus de l'ouvert  $V_{\alpha_{0}}$ , le faisceau des modules de Tate  $T_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P})$  se dévisse en une suite exacte

$$
0 \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{R} _ {\alpha_ {0}}) \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P} _ {\alpha_ {0}}) \to \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{A} _ {a _ {0}}) \to 0
$$

où  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{a_{0}})$  est un système local pur de poids -1 et  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{R}_{\alpha_{0}})$  est un système local pur de poids -2. Comme expliqué dans 7.4.9, l'action du module de Tate

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P} _ {\alpha_ {0}}) \otimes \mathcal {K} _ {\alpha_ {0}} ^ {n} \to \mathcal {K} _ {\alpha_ {0}} ^ {n - 1}
$$

se factorise par $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{\alpha_0})$ par la raison de poids.

La première étape de la récurrence consiste à montrer que pour tout point géométrique $u_{\alpha_0}$ de $V_{\alpha_0}$, la structure de $\Lambda_{A_{\alpha_0, u_{a_0}}}$-module qui s'en déduit sur la somme directe

$$
\mathrm{H} ^ {\bullet} (\mathrm{M} _ {u _ {\alpha_ {0}}}) := \bigoplus_ {n} \mathrm{H} ^ {n} (\mathrm{M} _ {u _ {\alpha_ {0}}}) [ - n ] = \bigoplus_ {n} \mathcal {K} _ {\alpha_ {0}, u _ {\alpha_ {0}}} ^ {n} [ - n + \dim (\mathrm{S}) ]
$$

fait de celle-ci un module libre.

D'après 7.4.11, cette assertion est indépendante du choix de $u_{\alpha_0}$. On peut en fait supposer que le point géométrique $u_{\alpha_0}$ soit défini sur un corps fini. Comme dans 7.5.3, il existe alors un quasi-relèvement $\mathrm{A}_{\alpha_0} \to \mathrm{P}_{\alpha_0}$ de sorte que l'action $\Lambda_{\mathrm{A}_{\alpha_0,u_{\alpha_0}}}$ sur $\mathrm{H}^{\bullet}(\mathrm{M}_{u_{\alpha_0}})$ provient d'une action géométrique de $\mathrm{A}_{\alpha_0,u_{\alpha_0}}$ sur $\mathrm{M}_{u_{\alpha_0}}$. On utilise maintenant l'hypothèse que la fibre $\mathrm{M}_{u_{\alpha_0}}$ est projective pour conclure que $\mathrm{H}^{\bullet}(\mathrm{M}_{u_{\alpha_0}})$ est un module libre sur $\Lambda_{\mathrm{A}_{\alpha_0,u_{\alpha_0}}}$ comme dans le lemme 7.5.1.

7.7.2. — On utilisera la propriété de liberté de la cohomologie de la fibre  $M_{u_{\alpha}}$  pour déduire la liberté du système local gradué  $K_{\alpha}$  comme  $\Lambda_{A_{\alpha}}$ -module. La difficulté est de contrôler le bruit causé par les  $K_{\alpha'}$  avec  $\alpha' \in A$  tel que  $Z_{\alpha}$  soit strictement contenu dans  $Z_{\alpha'}$ . Notons que par récurrence, on peut supposer que pour ces  $\alpha'$ ,  $K_{\alpha'}$  est un module libre sur  $\Lambda_{A_{\alpha'}}$ .

Prenons un point géométrique $u_{\alpha}$ de $V_{\alpha}$ au-dessus d'un point à valeur dans un corps fini. Soit $S_{u_{\alpha}}$ l'hensélisé strict de S en $u_{\alpha}$. La construction de 7.6.1 s'applique à $S_{u_{\alpha}}$. On dispose donc d'une action de $\Lambda_{P,u_{\alpha}}$ sur la restriction de $f_{*}\bar{\mathbf{Q}}_{\ell}$ à $S_{u_{\alpha}}$

$$
\Lambda_ {\mathrm{P}, u _ {\alpha}} \boxtimes (f _ {*} \bar {\mathbf {Q}} _ {\ell} | _ {\mathrm{S} _ {\alpha}}) \rightarrow (f _ {*} \bar {\mathbf {Q}} _ {\ell} | _ {\mathrm{S} _ {\alpha}}).\tag{7.7.3}
$$

Comme dans 7.6.1, celle-ci induit une action graduée de $\Lambda_{\mathrm{P},u_{\alpha}}$ sur la somme directe de faisceaux pervers de cohomologie dont la partie de degré $-1$ s'écrit

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} \left(\mathrm{P} _ {u _ {\alpha}}\right) \otimes {} ^ {p} \mathrm{H} ^ {n} \left(f _ {*} \bar {\mathbf {Q}} _ {\ell}\right) | _ {\mathrm{S} _ {\alpha}} \rightarrow {} ^ {p} \mathrm{H} ^ {n - 1} \left(f _ {*} \bar {\mathbf {Q}} _ {\ell}\right) | _ {\mathrm{S} _ {\alpha}}.
$$

D'après 7.6.2, cette flèche s'exprime en termes d'une matrice diagonale suivant la décomposition canonique de $^{p}\mathrm{H}^{n}(f_{*}\bar{\mathbf{Q}}_{\ell})$ et $^{p}\mathrm{H}^{n - 1}(f_{*}\bar{\mathbf{Q}}_{\ell})$ par le support

$$
{ } ^ { p } \mathrm{H} ^ { n } ( f _ { * } \bar { \mathbf { Q } } _ { \ell } ) = \bigoplus _ { \alpha \in \mathfrak { A } } \mathrm{K} _ { \alpha } ^ { n } .
$$

Autrement dit, la décomposition en somme directe

$$
\bigoplus_ {n} ^ {p} \mathrm{H} ^ {n} (f _ {*} \bar {\mathbf {Q}} _ {\ell}) = \bigoplus_ {\alpha \in \mathfrak {A}} \mathrm{K} _ {\alpha}
$$

respecte la structure de $\Lambda_{\mathrm{P},u_{\alpha}}$-modules gradués.

Le point géométrique  $u_{\alpha}$  étant défini sur un corps fini, d'après 7.5.3, il existe un quasi-relèvement  $A_{u_{\alpha}} \rightarrow P_{u_{\alpha}}$  qui induit une décomposition canonique en somme directe

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{P} _ {u _ {\alpha}}) = \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{R} _ {u _ {\alpha}}) \oplus \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{A} _ {u _ {\alpha}}).
$$

On en déduit donc une flèche

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{A} _ {u _ {\alpha}}) \otimes {} ^ {p} \mathrm{H} ^ {n} (f _ {*} \bar {\mathbf {Q}} _ {\ell}) | _ {\mathrm{S} _ {\alpha}} \rightarrow {} ^ {p} \mathrm{H} ^ {n - 1} (f _ {*} \bar {\mathbf {Q}} _ {\ell}) | _ {\mathrm{S} _ {\alpha}}
$$

laquelle se décompose d'après ce qui précède, en une somme directe des flèches

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{A} _ {u _ {\alpha}}) \otimes \mathrm{K} _ {\alpha^ {\prime}} ^ {n} | _ {\mathrm{S} _ {\alpha}} \rightarrow \mathrm{K} _ {\alpha^ {\prime}} ^ {n - 1} | _ {\mathrm{S} _ {\alpha}}
$$

sur l'ensemble des indices $\alpha' \in \mathfrak{A}$ tels que $Z_{\alpha}$ soit contenu dans $Z_{\alpha'}$.

Proposition 7.7.4. — Pour tout $\alpha' \in \mathfrak{A}$ tel que $Z_{\alpha}$ soit strictement contenu dans $Z_{\alpha'}$, pour tout entier $m$, le $\tilde{\mathbf{Q}}_{\ell}$-espace vectoriel gradué

$$
\bigoplus_ {n \in \mathbf {Z}} \mathrm{H} ^ {m} (\mathrm{K} _ {\alpha^ {\prime}, u _ {\alpha}} ^ {n}) [ - n ]
$$

est un $\Lambda_{\mathrm{A}_{u_{\alpha}}}$ -module libre.

Démonstration. — Au-dessus de  $V_{\alpha'}$ , on a une flèche canonique entre systèmes locaux gradués

$$
\Lambda_ {\mathrm{A} _ {\alpha^ {\prime}}} \otimes \mathcal {K} _ {\alpha^ {\prime}} \to \mathcal {K} _ {\alpha^ {\prime}}
$$

définie dans 7.4.9. D'après l'hypothèse de récurrence, pour tout point géométrique $u_{\alpha'}$ de $\mathrm{V}_{\alpha'}$, la fibre de $\mathcal{K}_{\alpha'}$ en $u_{\alpha'}$ est $\Lambda_{\mathrm{A}_{\alpha'}, u_{\alpha'}}$-module libre. D'après le théorème de décomposition,

$K_{\alpha'}$ est un système local gradué semi-simple. En appliquant le lemme 7.4.11, on sait qu'il existe un système local gradué $E_{\alpha'}$ sur $V_{\alpha'}$ et un isomorphisme

$$
\mathcal {K} _ {\alpha^ {\prime}} \simeq \Lambda_ {\mathrm{A} _ {\alpha^ {\prime}}} \otimes \mathrm{E} _ {\alpha^ {\prime}}
$$

en tant que $\Lambda_{\mathrm{A}_{\alpha^{\prime}}}$-modules gradués.

Cette factorisation continue à exister sur l'intersection  $V_{\alpha'} \cap S_{\alpha}$ . Notons  $y_{\alpha'}$  le point générique de  $V_{\alpha'} \cap S_{\alpha}$  et  $\bar{y}_{\alpha'}$  un point géométrique au-dessus de  $y_{\alpha'}$ . On a alors un isomorphisme de représentations de  $\text{Gal}(\bar{y}_{\alpha'} / y_{\alpha'})$

$$
\mathrm{L} _ {\alpha^ {\prime}, \bar {y} _ {\alpha^ {\prime}}} = \Lambda_ {\mathrm{A} _ {\alpha^ {\prime}, \bar {y} _ {\alpha^ {\prime}}}} \otimes \mathrm{E} _ {\alpha^ {\prime}, \bar {y} _ {\alpha^ {\prime}}}.
$$

Lemme 7.7.5. — Sous l'hypothèse que T$_{\bar{Q}_{\ell}}$(P) est polarisable comme dans 7.1.4, pour tout relèvement homologique $\beta : \text{T}_{\bar{Q}_{\ell}}(\text{A}_{u_{\alpha}}) \to \text{T}_{\bar{Q}_{\ell}}(\text{P}_{u_{\alpha}})$, l'application

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{A} _ {u _ {\alpha}}) \rightarrow \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{A} _ {\bar {y} _ {\alpha^ {\prime}}})
$$

qui s'obtient en composant $\beta$ avec la flèche de spécialisation $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P}_{u_{\alpha}})\to \mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P}_{\bar{y}_{\alpha^{\prime}}})$ suivie de la projection canonique $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P}_{\bar{y}_{\alpha^{\prime}}})\rightarrow \mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{\bar{y}_{\alpha^{\prime}}})$ est injective. De plus, il existe un complément de $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{u_{\alpha}})$ dans $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{\bar{y}_{\alpha^{\prime}}})$ qui est $\operatorname {Gal}(\bar{y}_{\alpha^{\prime}} / y_{\alpha^{\prime}})$-stable.

Démonstration. — La flèche de spécialisation  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P}_{u_{\alpha}})\to\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P}_{\bar{y}_{\alpha^{\prime}}})$  est compatible à la forme alternée de polarisation. N'importe quel relèvement homologique  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{u_{\alpha}})\to\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P}_{u_{\alpha}})$  est compatible avec la forme alternée qui est nulle sur la partie affine  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{R}_{u_{\alpha}})$  de sorte que l'application  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{u_{\alpha}})\to\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{P}_{\bar{y}_{\alpha^{\prime}}})$  qui s'en déduit l'est aussi. Il s'ensuit que  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{u_{\alpha}})\to\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{\bar{y}_{\alpha^{\prime}}})$  est injective et que l'orthogonal de  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{u_{\alpha}})$  dans  $\mathrm{T}_{\bar{\mathbf{Q}}_{\ell}}(\mathrm{A}_{\bar{y}_{\alpha^{\prime}}})$  est un complément  $\operatorname{Gal}(\bar{y}_{\alpha^{\prime}}/y_{\alpha^{\prime}})$ -stable.

Continuons la démonstration de 7.7.4. La décomposition en somme directe 7.7.5

$$
\mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{A} _ {\bar {y} _ {\alpha^ {\prime}}}) = \mathrm{T} _ {\bar {\mathbf {Q}} _ {\ell}} (\mathrm{A} _ {u _ {\alpha}}) \oplus \mathrm{U}
$$

de représentations de  $\mathrm{Gal}(\bar{y}_{\alpha^{\prime}}/y_{\alpha^{\prime}})$  induit un isomorphisme de représentations de  $\mathrm{Gal}(\bar{y}_{\alpha^{\prime}}/y_{\alpha^{\prime}})$

$$
\Lambda_ {\mathrm{A} _ {\bar {y} _ {\alpha^ {\prime}}}} = \Lambda_ {\mathrm{A} _ {u _ {\alpha}}} \otimes \Lambda (\mathrm{U})
$$

où $\Lambda(\mathrm{U}) = \bigoplus_{i} \wedge^{i}(\mathrm{U})[i]$. Ceci implique une factorisation en produit tensoriel de représentations de $\operatorname{Gal}(\bar{y}_{\alpha'} / y_{\alpha'})$

$$
\mathcal {K} _ {\alpha^ {\prime}, \bar {y} _ {\alpha^ {\prime}}} = \Lambda_ {\mathrm{A} _ {u _ {\alpha}}} \otimes \Lambda (\mathrm{U}) \otimes \mathrm{E} _ {\alpha^ {\prime}, \bar {y} _ {\alpha^ {\prime}}}.
$$

Il existe donc un isomorphisme

$$
\mathcal {K} _ {\alpha^ {\prime}} | _ {\mathrm{V} _ {\alpha^ {\prime}} \cap \mathrm{S} _ {\alpha}} = \Lambda_ {\mathrm{A} _ {u _ {\alpha}}} \boxtimes \mathrm{E} _ {\alpha^ {\prime}} ^ {\prime}
$$

où  $E_{\alpha'}'$  est un système local sur  $V_{\alpha'} \cap S_{\alpha}$ . Puisque le produit tensoriel externe avec  $\Lambda_{A_{u\alpha}}$  commute avec le prolongement intermédiaire de  $V_{\alpha'} \cap S_{\alpha}$  à  $Z_{\alpha'} \cap S_{\alpha}$  et avec le foncteur fibre en  $u_{\alpha_0}$ , la proposition 7.7.4 s'en déduit.

Considérons maintenant la suite spectrale 7.6.3

$$
\mathrm{E} _ {2} ^ {m, n} = \mathrm{H} ^ {m} (^ {p} \mathrm{H} ^ {n} (f _ {*} \bar {\mathbf {Q}} _ {\ell}) _ {u _ {\alpha}}) \Rightarrow \mathrm{H} ^ {m + n} (\mathrm{M} _ {u _ {\alpha}})
$$

qui dégénère en  $E_{2}$  d'après 7.6.4. On obtient ainsi une filtration de

$$
\mathrm{H} = \bigoplus_ {j} \mathrm{H} ^ {j} (\mathrm{M} _ {u _ {\alpha}}) [ - j ]
$$

dont le m-ième gradué est

$$
\mathrm{H} ^ {m} \left(\bigoplus_ {n} ^ {p} \mathrm{H} ^ {n} \left(f _ {*} \bar {\mathbf {Q}} _ {\ell}\right) _ {s _ {0}} [ - n ]\right) [ - m ].
$$

Cette filtration est stable sous l'action de $\Lambda_{\mathrm{A}_{u_{\alpha}}}$. Son action sur le $m$-ième gradué se déduit de l'action de $\Lambda_{\mathrm{A}_{u_{\alpha}}}$ sur la somme directe

$$
\bigoplus_ {n} ^ {p} \mathrm{H} ^ {n} (f _ {*} \bar {\mathbf {Q}} _ {\ell}) [ - n ] _ {\mathrm{S} _ {\alpha}}
$$

et donc de celle sur les  $K_{\alpha^{\prime}}|_{S_{\alpha}}$ . Ce m-ième gradué se décompose donc en une somme directe de  $\Lambda_{A_{u_{\alpha}}}$ -modules gradués

$$
\mathrm{H} ^ {m} \bigg (\bigoplus_ {\alpha^ {\prime}} \bigoplus_ {n \in \mathbf {Z}} \mathrm{K} _ {\alpha^ {\prime}, u _ {\alpha}} ^ {n} [ - n ] \bigg) [ - m ].
$$

Pour $\alpha' \neq \alpha$, on sait déjà que $\mathrm{H}^m(\bigoplus_{n \in \mathbf{Z}} \mathrm{K}_{\alpha', u_\alpha}^n [-n])$ est un $\Lambda_{\mathrm{A}_{u_\alpha}}$-module libre cf. 7.7.4. Pour $\alpha' = \alpha$, on a $\mathrm{H}^m(\mathrm{K}_{\alpha, u_\alpha}) = 0$ sauf pour $m = -\dim(\mathrm{Z}_\alpha)$. On obtient ainsi une filtration de H par des sous-$\Lambda_{\mathrm{A}_{u_\alpha}}$-modules

$$
0 \subset \mathrm{H} ^ {\prime} \subset \mathrm{H} ^ {\prime \prime} \subset \mathrm{H} = \bigoplus_ {j} \mathrm{H} ^ {j} (\mathrm{M} _ {u _ {\alpha}})
$$

tels que  $H'$  et  $H/H''$  sont des  $\Lambda_{A_{u\alpha}}$ -modules libres et tels que

$$
\mathrm{H} ^ {\prime \prime} / \mathrm{H} ^ {\prime} = \mathrm{L} _ {\alpha , u _ {\alpha}}.
$$

D'après 7.5.4, on sait que H est aussi un $\Lambda_{\mathrm{A}_{u_{\alpha}}}$-module libre. On va en déduire que $\mathrm{L}_{\alpha,u_{\alpha}}$ est aussi un $\Lambda_{\mathrm{A}_{u_{\alpha}}}$-module libre par une propriété particulière de l'anneau $\Lambda_{\mathrm{A}_{u_{\alpha}}}$.

Puisque $\Lambda_{\mathrm{A}_{u\alpha}}$ est une algèbre locale, tout $\Lambda_{\mathrm{A}_{u\alpha}}$-module projectif est libre. La suite exacte

$$
0 \to \mathrm{H} ^ {\prime \prime} \to \mathrm{H} \to \mathrm{H} / \mathrm{H} ^ {\prime \prime} \to 0
$$

avec H et H/H'' libres, implique que H'' est aussi libre.

Notons aussi que $\Lambda_{\mathrm{A}_{u\alpha}}$ est une $\bar{\mathbf{Q}}_{\ell}$-algèbre de locale dimension finie ayant un socle de dimension un. On en déduit que le dual $(\Lambda_{\mathrm{A}_{u\alpha}})^*$ de $\Lambda_{\mathrm{A}_{u\alpha}}$ en tant que $\bar{\mathbf{Q}}_{\ell}$-espaces vectoriels est un $\Lambda_{\mathrm{A}_{u\alpha}}$-module libre. Considérons la suite exacte duale

$$
0 \to (\mathrm{H} ^ {\prime \prime} / \mathrm{H} ^ {\prime}) ^ {*} \to (\mathrm{H} ^ {\prime \prime}) ^ {*} \to (\mathrm{H} ^ {\prime}) ^ {*} \to 0
$$

où  $(\mathrm{H}^{\prime\prime})^{*}$  et  $(\mathrm{H}^{\prime})^{*}$  sont des  $\Lambda_{A_{u_{\alpha}}}$ -modules libres. Il s'ensuit que  $(\mathrm{H}^{\prime\prime}/\mathrm{H}^{\prime})^{*}$  est un  $\Lambda_{A_{u_{\alpha}}}$ -module libre de sorte que  $H^{\prime\prime}/H^{\prime}$  l'est aussi.

7.8. Le cas de la fibration de Hitchin. — Appliquons le résultat de cette section au cas de la fibration de Hitchin, plus précisément au morphisme $\tilde{f}^{\mathrm{ani}}: \tilde{\mathcal{M}}^{\mathrm{ani}} \to \tilde{\mathcal{A}}^{\mathrm{ani}}$ muni de l'action de $\tilde{g}^{\mathrm{ani}}: \tilde{\mathcal{P}}^{\mathrm{ani}} \to \tilde{\mathcal{A}}^{\mathrm{ani}}$. Ici, $\tilde{\mathcal{M}}^{\mathrm{ani}}$ et $\tilde{\mathcal{P}}^{\mathrm{ani}}$ ne sont pas des schémas mais des champs de Deligne-Mumford de type fini cf. 6.1.3. On sait que $\tilde{\mathcal{P}}^{\mathrm{ani}}$ est lisse sur $\tilde{\mathcal{A}}^{\mathrm{ani}}$ d'après 4.3.5 et que $\tilde{\mathcal{M}}^{\mathrm{ani}}$ est lisse sur $k$ d'après 4.14.1. D'après 4.15.2, l'action de $\tilde{\mathcal{P}}^{\mathrm{ani}}$ sur $\tilde{\mathcal{M}}^{\mathrm{ani}}$ a des stabilisateurs affines. D'après 4.16.4, le morphisme $\tilde{f}^{\mathrm{ani}}$ est plat de dimension relative $d$ et il en est de même de $\tilde{g}^{\mathrm{ani}}$. D'après 5.5.4, le faisceau $\pi_0(\tilde{\mathcal{P}}^{\mathrm{ani}})$ est un quotient fini du faisceau constant $\mathbf{X}_*$. Le module de Tate est polarisable d'après 4.12.1. Le morphisme $\tilde{f}^{\mathrm{ani}}$ est propre sans être projectif, néanmoins $\tilde{\mathcal{M}}^{\mathrm{ani}}$ est homéomorphe à un schéma projectif $\tilde{\mathbf{M}}^{\mathrm{ani}}$ au-dessus de $\tilde{\mathcal{A}}^{\mathrm{ani}}$ d'après 6.1.3.

Il y deux façons d'appliquer de l'inégalité 7.2.3 à notre situation. La première est de remplacer $\tilde{\mathcal{M}}^{\mathrm{ani}}$ par $\tilde{\mathrm{M}}^{\mathrm{ani}}$ qui est projectif sur $\tilde{\mathcal{A}}^{\mathrm{ani}}$. Le faisceau constant $\bar{\mathbf{Q}}_{\ell}$ sur $\tilde{\mathrm{M}}^{\mathrm{ani}}$ est pur car le champ $\tilde{\mathcal{M}}^{\mathrm{ani}}$ qui lui est homéomorphe, est lisse. On peut remplacer le champ de Picard de Deligne Mumford $\tilde{\mathcal{P}}^{\mathrm{ani}}$ par le schéma en groupes $\mathcal{P}^{\infty,\mathrm{ani}}$ défini à l'aide d'un rigidificateur 4.5.6. Ici $\mathcal{P}^{\infty,\mathrm{ani}}$ est de dimension relative plus grande que $d$, mais adapter 7.2.3 à cette situation n'est qu'une question de numérologie.

En fait, il y a une façon de procéder beaucoup plus économique. Elle consiste à remarquer que l'intégralité de démonstration de 7.2.3 s'adapte telle quelle aux champs de Deligne-Mumford à l'exception du lemme 7.5.1 où on a supposé que la fibre $\mathcal{M}_a$ est projective. Mais d'après 4.15.2, on sait que $\mathcal{M}_a$ est homéomorphe à un schéma projectif de sorte que 7.2.3 s'applique. Notons aussi qu'au lieu d'utiliser 4.15.2 et 7.5.1 combinés, il sera encore plus économique d'appliquer directement la formule de produit 4.15.1 pour obtenir la conclusion de 7.5.1. Dans la situation de la fibration de Hitchin où on dispose d'une formule de produit, le paragraphe 7.5 n'est en fait pas nécessaire.

$$
\tilde {\mathcal {A}} ^ {\mathrm{ani}} = \bigsqcup_ {\delta \in \mathbf {N}} \tilde {\mathcal {A}} _ {\delta} ^ {\mathrm{ani}}
$$

## 7.8.1. — On dispose d'une stratification cf. 5.6.6

telle que pour tout  $a \in \mathcal{A}_{\delta}^{\mathrm{ani}}(\bar{k})$ , la dimension de la partie affine de  $P_{a}$  vaut  $\delta$ . Nous conjecturons que pour tout  $\delta$ , nous avons

$$
\operatorname{codim} \left(\tilde {\mathcal {A}} _ {\delta} ^ {\text { ani }}\right) \geq \delta .
$$

L'indice le plus fort en faveur de cette conjecture est le cas de caractéristique zéro dont une démonstration est esquissée dans [60, p. 4]. A défaut de disposer d'une démonstration de cette conjecture en caractéristique $p$, nous devons recourir à un stratagème :

7.8.2. — Supposons qu'il existe des entiers $\delta$ tels que $\mathrm{codim}(\tilde{\mathcal{A}}_{\delta}^{\mathrm{ani}}) < \delta$, nous noterons $\delta_{\mathrm{G}}^{\mathrm{bad}}(\mathrm{D})$ le plus petit d'entre eux. Il est important de noter la dépendance de $\delta_{\mathrm{G}}^{\mathrm{bad}}(\mathrm{D})$ s'il existe en fonction de G et du fibré inversible D. D'après 5.7.2, on sait que pour le groupe G fixé, l'entier $\delta_{\mathrm{G}}^{\mathrm{bad}}(\mathrm{D})$ tend vers l'infini avec $\deg(\mathrm{D})$. Notons

$$
\tilde {\mathcal {A}} ^ {\text { bad }} = \bigsqcup_ {\delta \geq \delta_ {\mathrm{G}} ^ {\text { bad }} (\mathrm{D})} \tilde {\mathcal {A}} _ {\delta} ^ {\text { ani }}
$$

et

$$
\tilde {\mathcal {A}} ^ {\mathrm{good}} = \tilde {\mathcal {A}} ^ {\mathrm{ani}} - \tilde {\mathcal {A}} ^ {\mathrm{bad}}.
$$

Par construction, au-dessus de $\tilde{\mathcal{A}}^{\mathrm{good}}$, $\tilde{f}^{\mathrm{ani}}$ et $\tilde{g}^{\mathrm{ani}}$ forment une fibration abélienne $\delta$-régulière.

Théorème 7.8.3. — Soit $^{p}\mathrm{H}^{n}(\tilde{f}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})_{\mathrm{st}}$ le plus grand facteur direct de $^{p}\mathrm{H}^{n}(\tilde{f}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})$ où $\mathbf{X}_{*}$ agit trivialement. Soient K un facteur pervers géométriquement irréductible de $^{p}\mathrm{H}^{n}(\tilde{f}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})_{\mathrm{st}}$ et Z le support de K. Supposons que $\mathbf{Z} \cap \tilde{\mathcal{A}}^{\mathrm{good}} \neq \emptyset$. Alors $\mathbf{Z} = \tilde{\mathcal{A}}^{\mathrm{ani}}$.

Démonstration. — Puisque $\tilde{\mathcal{P}}$ est $\delta$-régulier au-dessus de $\tilde{\mathcal{A}}^{\mathrm{good}}$, on a l'inégalité $\operatorname{codim}(Z) \geq \delta_Z$. En appliquant 7.2.3 avec le trivial kappa, on a d'une part l'égalité $\operatorname{codim}(Z) = \delta_Z$ et d'autre part l'existence d'un ouvert U de $\tilde{\mathcal{A}}^{\mathrm{ani}}$ et d'un système local L sur U $\cap$ Z tel que $i_*\mathrm{L}$, $i$ étant l'immersion fermée Z $\cap$ U $\to$ U, soit un facteur direct de H$^{2d}$($f_*\bar{\mathbf{Q}}_f$)$_{\mathrm{st}}$ |U. Or on sait d'après 6.5.1 que ce dernier est un faisceau constant sur $\tilde{\mathcal{A}}^{\mathrm{ani}}$ de sorte que U $\cap$ Z = U et donc Z = $\tilde{\mathcal{A}}^{\mathrm{ani}}$.

7.8.4. — L'application de 7.2.3 à la partie $\kappa$ est plus subtile car a priori il est possible que $\tilde{\mathcal{A}}^{\mathrm{good}} \cap \tilde{\mathcal{A}}_{\kappa} = \emptyset$. En effet, $\tilde{\mathcal{A}}_{\kappa}$ est la réunion de $\tilde{\mathcal{A}}_{\mathrm{H}}$, H étant les groupes endoscopiques associés aux données endoscopiques pointées $(\kappa, \rho_{\kappa}^{\bullet})$ et la codimension de $\tilde{\mathcal{A}}_{\mathrm{H}}$ dans $\tilde{\mathcal{A}}$ est un multiple de deg(D). Néanmoins, il n'est pas nécessaire de savoir que la fibration abélienne est $\delta$-régulière pour appliquer les inégalités 7.2.2 et 7.2.3, il suffit en fait de connaître l'inégalité $\operatorname{codim}(Z) \geq \delta_Z$ pour les supports $Z$ possibles.

En remplaçant G par un groupe endoscopique H, on a un entier  $\delta_{\mathrm{H}}^{\mathrm{bad}}(\mathrm{D})$ , un sous-schéma fermé

$$
\tilde {\mathcal {A}} _ {\mathrm{H}} ^ {\mathrm{bad}} = \bigsqcup_ {\delta_ {\mathrm{H}} \geq \delta_ {\mathrm{H}} ^ {\mathrm{bad}} (\mathrm{D})} \tilde {\mathcal {A}} _ {\delta_ {\mathrm{H}}} ^ {\mathrm{ani}}
$$

et son ouvert complémentaire $\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{good}} = \tilde{\mathcal{A}}_{\mathrm{H}} - \tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{bad}}$

Théorème 7.8.5. — Soit $^{p}\mathrm{H}^{n}(\tilde{f}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})_{\kappa}$ le plus grand facteur direct de $^{p}\mathrm{H}^{n}(\tilde{f}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})$ où $\mathbf{X}_{*}$ agit à travers le caractère $\kappa$. Soient K un facteur pervers géométriquement irréductible de $^{p}\mathrm{H}^{n}(\tilde{f}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})_{\kappa}$ et Z le support de K. Alors, il existe une donnée endoscopique pointée $(\kappa, \rho_{\kappa}^{\bullet})$ telle que Z est inclus dans $\tilde{\nu}(\tilde{\mathcal{A}}_{\mathrm{H}})$ où H est le groupe endoscopique attaché à $(\kappa, \rho_{\kappa}^{\bullet})$ et $\tilde{\nu}: \tilde{\mathcal{A}}_{\mathrm{H}} \to \tilde{\mathcal{A}}$ est l'immersion fermée qui s'en déduit.

Si on suppose de plus que  $Z \cap \tilde{\nu}(\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{good}}) \neq \emptyset$ , alors  $Z = \tilde{\nu}(\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{ani}})$ .

Démonstration. — On sait que $Z \subset \tilde{\mathcal{A}}_{\kappa}$ où cf. 6.3.3

$$
\tilde {\mathcal {A}} _ {\kappa} = \bigsqcup_ {(\kappa , \rho_ {\kappa , \xi} ^ {\bullet})} \tilde {\nu} (\tilde {\mathcal {A}} _ {\mathrm{H} _ {\xi}})
$$

de sorte que le fermé irréductible Z est contenu dans l'une des composantes irréductibles  $\tilde{\nu}(\tilde{\mathcal{A}}_{\mathrm{H}_{\xi}})$ . On va noter simplement H le groupe endoscopique attaché à la donnée endoscopique  $(\kappa, \rho_{\kappa}^{\bullet})$  tel que  $Z \subset \tilde{\nu}(\tilde{\mathcal{A}}_{\mathrm{H}})$ . Soit  $Z_{H}$  le fermé de  $\tilde{\mathcal{A}}_{H}$  tel que  $Z = \tilde{\nu}(Z_{\mathrm{H}})$ .

Supposons que $Z_{\mathrm{H}} \cap \tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{good}} \neq \emptyset$, alors on a l'inégalité

$$
\operatorname{codim} \left(\mathrm{Z} _ {\mathrm{H}}\right) \geq \delta_ {\mathrm{H}, \mathrm{Z} _ {\mathrm{H}}}
$$

où $\delta_{\mathrm{H}}$ est la fonction delta pour le champ de Picard $\tilde{\mathcal{P}}_{\mathrm{H}}$ sur $\tilde{\mathcal{A}}_{\mathrm{H}}$. D'après 4.17.3 et 4.17.1, on sait que pour tout $a_{\mathrm{H}} \in \tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{ani}}(\bar{k})$, la différence

$$
\delta (\tilde {\nu} (a _ {\mathrm{H}})) - \delta_ {\mathrm{H}} (a _ {\mathrm{H}})
$$

est indépendante de $a_{\mathrm{H}}$ et vaut exactement la codimension de $\tilde{\nu}(\tilde{\mathcal{A}}_{\mathrm{H}})$ dans $\tilde{\mathcal{A}}$. On a donc

$$
\mathrm{codim} (Z) \geq \delta_ {\mathrm{H}} (a _ {\mathrm{H}}) + \mathrm{codim} (\tilde {\nu} (\tilde {\mathcal {A}} _ {\mathrm{H}})) = \delta_ {\mathrm{Z}}.
$$

En appliquant 7.2.3, il existe un ouvert U de $\tilde{\mathcal{A}}^{\mathrm{ani}}$ et un système local non trivial sur $Z\cap U$ tel que $i_{*}L$, $i$ étant l'immersion fermée $i:Z\cap U\to U$, soit un facteur direct de $\mathrm{H}^{2d}(\tilde{f}_{*}^{\mathrm{ani}}\bar{\mathbf{Q}}_{\ell})_{\kappa}$. D'après 6.5.1, on sait alors que $Z\cap U=\tilde{\nu}(\tilde{\mathcal{A}}_{\mathrm{H}})\cap U$ de sorte que finalement $Z=\tilde{\nu}(\tilde{\mathcal{A}}_{\mathrm{H}})$.

## 8. Comptage de points

Dans ce dernier chapitre, nous complétons la démonstration du théorème de stabilisation géométrique 6.4.2 ainsi que celle des conjectures de Langlands-Shelstad 1.11.1 et de Waldspurger 1.12.7 en s'appuyant sur les théorèmes 7.8.3 et 7.8.5.

La démonstration est fondée sur le principe suivant. Soient  $K_{1}$ ,  $K_{2}$  deux complexes purs sur un k-schéma de type fini S irréductible. Supposons que tout faisceau pervers géométriquement simple présent dans  $K_{1}$  ou  $K_{2}$  a pour support S tout entier, alors pour démontrer que  $K_{1}$  et  $K_{2}$  ont la même classe dans le groupe de Grothendieck, il suffit de démontrer qu'il existe un ouvert dense U de S tel que pour toute extension finie  $k'$  de k, pour tout  $u \in \mathrm{U}(k')$ , les traces du Frobenius  $\sigma_{k'}$  de  $k'$  sur  $K_{1,u}$  et  $K_{2,u}$  sont égales. L'égalité dans le groupe de Grothendieck implique qu'on ait la même égalité mais pour tout point  $s \in \mathrm{S}(k')$ . Ce qui fait toute la force du théorème du support est que le comptage de points dans une fibre au-dessus d'un point d'un petit ouvert U devrait être beaucoup plus agréable que dans une fibre quelconque.

On va donc établir des formules générales pour le nombre  $\sharp\mathcal{M}_{a}(k)$  des k-points dans une fibre de Hitchin anisotrope. Plus précisément, on veut une formule pour la partie stable  $\sharp\mathcal{M}_{a}(k)_{\mathrm{st}}$ . La formule de produit 4.15.1 permet d'exprimer ce nombre comme un produit du nombre  $\sharp\mathcal{P}_{a}^{0}(k)$  des k-points de la composante neutre de  $P_{a}$  et des nombres de points dans des quotients de fibres de Springer affine cf. 8.4. Pour ces quotients des fibres de Springer affines, un comptage plus ou moins direct donne comme résultat une intégrale orbitale stable cf. 8.2. On a aussi la variante du comptage avec une κ-pondération qui donne lieu aux κ-intégrales orbitales. A chaque fois, il s'agit du comptage de points d'un champ d'Artin de la forme [M/P] où M est un k-schéma et où P est un k-groupe algébrique agissant sur M. Ce formalisme est rappelé dans 8.1 en même temps qu'une formule des points fixes ad hoc qui a été démontrée dans l'appendice A.3 de [54].

Pour $a \in \mathcal{A}^{\diamond}(k)$, les quotients des fibres de Springer affines sont tous triviaux de sorte que $\sharp \mathcal{M}_a(k)_{\text{st}}$ est égal au nombre $\sharp \mathcal{P}_a^0(k)$ où $\mathcal{P}_a^0$ est essentiellement une variété abélienne. Ceci permet de démontrer l'égalité des nombres $\sharp \mathcal{M}_{1,a}(k)_{\text{st}}$ et $\sharp \mathcal{M}_{2,a}(k)_{\text{st}}$ pour $a \in \mathcal{A}^{\diamond}(k)$ associés à deux groupes $G_1$ et $G_2$ ayant des données radicielles isogènes. Le théorème de support 7.8.3 permet de prolonger l'identité à $a \in (\mathcal{A}^{\text{ani}} - \mathcal{A}^{\text{bad}})(k)$. On obtient ainsi assez de points globaux pour obtenir toutes les intégrales orbitales stables locales en faisant tendre deg(D) vers l'infini. On démontre ainsi le lemme fondamental non standard conjecturé par Waldspurger cf. 8.8. En renversant l'argument global-local, on peut prolonger l'identité $\sharp \mathcal{M}_{1,a}(k)_{\text{st}} = \sharp \mathcal{M}_{2,a}(k)_{\text{st}}$ à tout $a \in \mathcal{A}^{\text{ani}}(k)$.

La démonstration de la conjecture de Langlands-Shelstad suit essentiellement la même stratégie avec un peu plus de difficultés techniques. Pour $\tilde{a}_{\mathrm{H}} \in \tilde{\mathcal{A}}_{\mathrm{H}}^{\diamond}(k)$, les intégrales orbitales stables locales de $\tilde{a}_{\mathrm{H}}$ sont triviales mais les $\kappa$-intégrales orbitales locales dans G du point $a$ correspondant ne le sont pas nécessairement. Toutefois, en rétrécissant encore plus $\tilde{\mathcal{A}}_{\mathrm{H}}^{\diamond}$, on peut supposer que ces $\kappa$-intégrales orbitales locales non triviales sont

aussi simples que possible. Le calcul de ces intégrales locales simples est bien connu et se ramène au cas SL(2) traité par Labesse et Langlands. On le reprend dans 8.3. En combinant ce calcul avec le théorème du support 7.8.5, on obtient la partie du théorème de stabilisation géométrique sur l'ouvert $\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{ani}} - \tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{bad}}$ cf. 8.5. De nouveau, en faisant tendre deg(D) vers l'infini, on obtient toutes les intégrales orbitales locales et on démontre ainsi le lemme fondamental cf. 8.6. En renversant l'argument global-local, on obtient complètement le théorème de stabilisation géométrique 6.4.2.

8.1. Remarques générales sur le comptage. — Nous allons fixer dans ce paragraphe un cadre pour les différents problèmes de comptage que nous devrons résoudre dans la suite. Nous allons aussi préciser les abus de notations que nous allons pratiquer systématiquement dans ce chapitre. Dans ce paragraphe et contrairement au reste de l'article, la lettre X ne désigne pas nécessairement une courbe.

8.1.1. — Soit M un k-schéma de type fini. D'après la formule des traces de Grothendieck-Lefschetz, le nombre de k-points de M peut être calculé comme une somme alternée de traces de l'élément de Frobenius  $\sigma \in \operatorname{Gal}(\bar{k}/k)$

$$
\sharp \mathrm{M} (k) = \sum_ {n} (- 1) ^ {n} \mathrm{tr} (\sigma , \mathrm{H} _ {c} ^ {n} (\mathrm{M}))
$$

où  $\mathrm{H}_{c}^{n}(\mathbf{M})$  désigne le n-ième groupe de cohomologie à support compact  $\mathrm{H}_{c}^{n}(\mathbf{M}\otimes_{k}\bar{k},\bar{\mathbf{Q}}_{\ell})$  de  $M\otimes_{k}\bar{k}$ .

Nous aurons besoin d'une variante de cette formule des traces dans le contexte suivant. Soit M un k-schéma de type fini ou plus généralement un champ de Deligne-Mumford de type fini, muni d'une action d'un k-groupe algébrique commutatif de type fini P. Nous voulons relier la trace de  $\sigma$  sur une partie de la cohomologie à support de M avec le nombre de points du quotient X = [M/P] et le nombre de points de la composante neutre de P. C'est le contenu de l'appendice A.3 de [54] que nous allons maintenant rappeler et généraliser légèrement.

8.1.2. — Soit donc X = [M/P] comme ci-dessus. On va écrire X pour le groupe  $\mathrm{X}(\bar{k})$ , M pour l'ensemble  $\mathrm{M}(\bar{k})$  et P pour le groupe  $\mathrm{P}(\bar{k})$ . Par définition, l'ensemble des objets de X = [M/P] est l'ensemble M. Soient  $m_{1}, m_{2} \in M$ . Alors l'ensemble des flèches  $\mathrm{Hom}_{\mathrm{X}}(m_{1}, m_{2})$  est le transporteur

$$
\operatorname{Hom} _ {\mathrm{X}} \left(m _ {1}, m _ {2}\right) = \{p \in \mathrm{P} | p m _ {1} = m _ {2} \}.
$$

La règle de composition des flèches se déduit de la multiplication dans le groupe P.

8.1.3. — L'action de l'élément de Frobenius $\sigma \in \mathrm{Gal}(\bar{k}/k)$ sur M et P induit une action sur le groupoïde X = [M/P]. Le groupoïde X(k) des points fixes sous l'action de $\sigma$ est par définition la catégorie dont

\- les objets sont les couples $(m,p)$ où $m\in \mathbf{M}$ et $p\in \mathrm{P}$ tels que $p\sigma (m) = m$

\- une flèche $h:(m,p)\to(m',p')$ dans $\mathrm{X}(k)$ est un élément $h\in\mathrm{P}$ tel que $hm=m'$ et $p'=hp\sigma(h)^{-1}$.

La catégorie  $\mathrm{X}(k)$  a un nombre fini de classes d'isomorphisme d'objets et chaque objet a un nombre fini d'automorphismes. On s'intéresse à la somme

$$
\sharp \mathrm{X} (k) = \sum_ {x \in \mathrm{X} (k) / \sim} \frac {1}{\sharp \mathrm{Aut} _ {\mathrm{X} (k)} (x)}
$$

où $x$ parcourt un ensemble de représentants des classes d'isomorphisme des objets de $\mathrm{X}(k)$.

8.1.4. — Soit X = [M/P] comme ci-dessus et soit  $x = (m, p)$  un objet de  $\mathrm{X}(k)$ . Par définition des flèches dans  $\mathrm{X}(k)$ , la classe de  $\sigma$ -conjugaison de p ne dépend que de la classe d'isomorphisme de x. Puisque P est un k-groupe de type fini, le groupe des classes de  $\sigma$ -conjugaison de P s'identifie canoniquement à  $\mathrm{H}^{1}(k, \mathrm{P})$ . Notons  $\mathrm{cl}(x) \in \mathrm{H}^{1}(k, \mathrm{P})$  la classe de  $\sigma$ -conjugaison de p qui ne dépend que de la classe d'isomorphisme de x. D'après un théorème de Lang,  $\mathrm{H}^{1}(k, \mathrm{P})$  s'identifie à  $\mathrm{H}^{1}(k, \pi_{0}(\mathrm{P}))$  où  $\pi_{0}(\mathrm{P})$  désigne le groupe des composantes connexes de  $P \otimes_{k} \bar{k}$  qui est donc un groupe fini commutatif muni d'une action de  $\sigma$ . Ainsi, pour tout caractère  $\sigma$ -invariant  $\kappa : \pi_{0}(\mathrm{P}) \to \bar{\mathbf{Q}}_{\ell}^{\times}$ , pour tout objet  $x \in \mathrm{X}(k)$ , on peut définir un accouplement

$$
\langle \mathrm{cl} (x), \kappa \rangle = \kappa (\mathrm{cl} (x)) \in \bar {\mathbf {Q}} _ {\ell} ^ {\times}
$$

qui ne dépend que de la classe d'isomorphisme de $x$. On peut donc définir le nombre de points de $\mathrm{X}(k)$ avec la $\kappa$-pondération

$$
\sharp \mathrm{X} (k) _ {\kappa} = \sum_ {x \in \mathrm{X} (k) / \sim} \frac {\langle \operatorname{cl} (x) , \kappa \rangle}{\sharp \operatorname{Aut} _ {\mathrm{X} (k)} (x)}
$$

où $x$ parcourt un ensemble de représentants des classes d'isomorphisme des objets de $\mathrm{X}(k)$.

8.1.5. — Le groupe P agit sur les groupes de cohomologie  $\mathrm{H}_{c}^{n}(\mathrm{M})$  à travers son groupe des composantes connexes  $\pi_{0}(\mathrm{P})$  d'après le lemme d'homotopie. On peut former le sous-espace propre  $\mathrm{H}_{c}^{n}(\mathrm{M})_{\kappa}$  de  $\mathrm{H}_{c}^{n}(\mathrm{M})$  de valeur propre  $\kappa$ . Puisque  $\kappa$  est  $\sigma$ -invariant,  $\sigma$  agit sur  $\mathrm{H}_{c}^{n}(\mathrm{M})_{\kappa}$ .

On a la variante suivante de la formule des traces de Grothendieck-Lefschetz démontrée dans l'appendice A.3 de [54].

Proposition 8.1.6. — Soient M un k-schéma de type fini, P un k-groupe commutatif de type fini agissant sur M et X = [M/P]. Alors la catégorie X(k) a un nombre fini de classes d'isomorphisme d'objets et chaque objet a un nombre fini d'automorphismes. Pour tout $\kappa: \pi_0(P) \to \bar{\mathbf{Q}}_\ell^\times$ un caractère $\sigma$-invariant, le nombre $\sharp X(k)_\kappa$ a l'interprétation cohomologique suivante

$$
\sharp \mathrm{P} ^ {0} (k) \sharp \mathrm{X} (k) _ {\kappa} = \sum_ {n} (- 1) ^ {n} \operatorname{tr} (\sigma , \mathrm{H} _ {c} ^ {n} (\mathrm{M}) _ {\kappa})
$$

où $\mathbf{P}^{0}$ est la composante neutre de $\mathbf{P}$.

Nous renvoyons à [54, A.3.1] pour la démonstration. On peut considérer deux exemples instructifs qui expliquent pourquoi il faut séparer le rôle de  $P^{0}$  de  $\pi_{0}(P)$ .

Exemple 8.1.7. — Supposons que M = Spec(k) et que P est un groupe fini sur lequel σ agit. Soit X = [M/P] le classifiant de P. Alors les objets de la catégorie X(k) sont les éléments  $p \in P$  alors que les flèches  $p \to p'$  sont les éléments  $h \in P$  tels que  $p' = hp\sigma(h)^{-1}$ . On a alors

$$
\sharp \mathrm{X} (k) = \frac {\sharp \mathrm{P}}{\sharp \mathrm{P}} = 1.
$$

Par ailleurs, pour tout caractère $\sigma$-invariant $\kappa: \mathrm{P} \to \bar{\mathbf{Q}}_{\ell}^{\times}$ non trivial, on a $\sharp \mathrm{X}(k)_{\kappa} = 0$.

Exemple 8.1.8. — Soient M = Spec(k) et P = G$_{m}$. Soit X = [M/P] le classifiant de G$_{m}$. Les objets de X(k) sont de nouveau les éléments p ∈ P alors que les flèches p → p' sont les éléments h ∈ P tels que p' = hpσ(h)$^{-1}$. D'après Lang, tous les éléments de k$^{\times}$ sont σ-conjugués de sorte qu'il n'y a qu'une seule classe d'isomorphisme d'objets dans X(k). Le groupe des automorphismes de chaque objet de X(k) est k$^{\times}$ et a donc q - 1 éléments. On a donc ‡X(k) = (q - 1)$^{-1}$.

Pour étudier le comptage des points dans les fibres de Springer affines, nous avons besoin d'une variante de la discussion précédente pour le cas où M et P sont localement de type fini et où [M/P] a une propriété de finitude raisonnable.

Soient M un k-schéma localement de type fini et P un k-groupe commutatif localement de type fini agissant sur M. Pour que le quotient  $[M/P]$  soit raisonnablement fini, nous faisons en plus les hypothèses suivantes.

## Hypothèse 8.1.9.

(1) Le groupe des composantes connexes $\pi_0(\mathbf{P})$ est un groupe abélien de type fini.

(2) Le stabilisateur dans P de chaque point de M est un sous-groupe de type fini.

(3) Il existe un sous-groupe discret sans torsion $\Lambda \subset \mathrm{P}$ tel que $\mathrm{P} / \Lambda$ et $\mathrm{M} / \Lambda$ sont de type fini.

La dernière hypothèse nécessite d'être commentée. Puisque le groupe $\Lambda$ est sans torsion, il agit sans points fixes sur M puisque le stabilisateur dans P de n'importe quel point de M est de type fini et en particulier a une intersection triviale avec $\Lambda$. De plus, si l'hypothèse est vérifiée, elle est vérifiée pour n'importe quel sous-groupe $\Lambda' \subset \Lambda$ d'indice fini et $\sigma$-invariant.

8.1.10. — Il faut aussi expliquer comment construire un sous-groupe discret sans torsion  $\Lambda$  de P tel que P/ $\Lambda$  soit de type fini. Le groupe P admet un dévissage canonique

$$
1 \to \mathrm{P} ^ {\mathrm{tf}} \to \mathrm{P} \to \pi_ {0} (\mathrm{P}) ^ {\mathrm{lib}} \to 0
$$

où  $\pi_{0}(P)^{\mathrm{lib}}$  est le quotient libre maximal de  $\pi_{0}(P)$  et où  $P^{tf}$  est le sous-groupe de type fini maximal de P. Puisque  $\pi_{0}(P)^{\mathrm{lib}}$  est un groupe abélien libre, il existe un relèvement

$$
\gamma : \pi_ {0} (\mathrm{P}) ^ {\mathrm{lib}} \to \mathrm{P}
$$

qui n'est pas nécessairement $\sigma$-équivariant. Puisque $\mathrm{P}^{\mathrm{tf}}$ est un $k$-groupe de type fini, la restriction de $\gamma$ à $\Lambda = \mathrm{N}\pi_0(\mathrm{P})^{\mathrm{lib}}$ pour N assez divisible est $\sigma$-équivariante. On obtient ainsi un sous-groupe discret sans torsion P. L'hypothèse (3) est équivalente à ce que le quotient de M par ce sous-groupe discret sans torsion est un $k$-schéma de type fini.

8.1.11. — Considérons le quotient X = [M/P]. Le groupoïde  $\mathrm{X}(k)$  des points fixes sous  $\sigma$  a pour objets les couples  $x = (m, p)$  avec  $m \in M$  et  $p \in P$  tels que  $p\sigma(m) = m$ . Une flèche  $h : (m, p) \to (m', p')$  est un élément  $h \in P$  tel que  $hm = m'$  et  $p' = hp\sigma(h)^{-1}$ . Soit  $P_{\sigma}$  le groupe des classes de  $\sigma$ -conjugaison dans P. La classe de  $\sigma$ -conjugaison de p définit un élément  $\mathrm{cl}(x) \in \mathrm{P}_{\sigma}$  qui ne dépend que de la classe d'isomorphisme de x. Puisque m est défini sur une extension finie de k,  $\mathrm{cl}(x)$  appartient au sous-groupe

$$
\operatorname{cl} (x) \in \mathrm{H} ^ {1} (k, \mathrm{P})
$$

qui est la partie torsion de $\mathrm{P}_{\sigma}$.

Lemme 8.1.12. — Tout caractère $\kappa: \mathrm{H}^{1}(k, \mathrm{P}) \to \bar{\mathbf{Q}}_{\ell}^{\times}$ s'étend en un caractère d'ordre fini $\tilde{\kappa}: \mathrm{P}_{\sigma} \to \bar{\mathbf{Q}}_{\ell}^{\times}$.

Démonstration. — Soit  $P^{0}$  le groupe des composantes neutres de P. D'après le théorème de Lang, tout élément de  $P^{0}$  est σ-conjugué à l'élément neutre. Il s'ensuit que l'application  $\mathrm{P}_{\sigma}\to\pi_{0}(\mathrm{P})_{\sigma}$  de  $P_{\sigma}$  sur le groupe des classes de σ-conjugaison de  $\pi_{0}(\mathrm{P})$  est un isomorphisme. Les caractères  $\tilde{\kappa}:P_{\sigma}\to\bar{\mathbf{Q}}_{\ell}^{\times}$  sont donc les  $\bar{\mathbf{Q}}_{\ell}$ -points du  $\bar{\mathbf{Q}}_{\ell}$ -groupe diagonalisable de type fini  $(\pi_{0}(\mathrm{P})_{\sigma})^{*}=\operatorname{Spec}(\bar{\mathbf{Q}}_{\ell}[\pi_{0}(\mathrm{P})_{\sigma}])$ . Les caractères  $\kappa:H^{1}(k,\mathrm{P})\to\bar{\mathbf{Q}}_{\ell}^{\times}$  forment le groupe  $\pi_{0}((\pi_{0}(\mathrm{P})_{\sigma})^{*})$  des composantes connexes de  $(\pi_{0}(\mathrm{P})_{\sigma})^{*}$ . Tout élément  $\kappa\in\pi_{0}((\pi_{0}(\mathrm{P})_{\sigma})^{*})$  peut se relever en un élément de torsion  $\tilde{\kappa}\in(\pi_{0}(\mathrm{P})_{\sigma})^{*}$ .

Le quotient X = [M/P] est clairement équivalent à  $[(M/\Lambda)/(P/\Lambda)]$  où M/ $\Lambda$  et P/ $\Lambda$  sont de type fini. En particulier, l'ensemble des classes d'isomorphisme des objets de X(k) est fini et le groupe des automorphismes de chaque objet est fini. Pour tout caractère  $\kappa: H^{1}(k, P) \to \bar{\mathbf{Q}}_{\ell}^{\times}$ , on peut donc former la somme finie

$$
\sharp \mathrm{X} (k) _ {\kappa} = \sum_ {x \in \mathrm{X} (k) / \sim} \frac {\langle \operatorname{cl} (x) , \kappa \rangle}{\sharp \operatorname{Aut} (x)}.
$$

Soit $\tilde{\kappa}:\mathrm{P}\to \bar{\mathbf{Q}}_{\ell}^{\times}$ un caractère $\sigma$-invariant d'ordre fini qui représente $\kappa$. On peut alors choisir un sous-groupe discret $\Lambda \subset \mathrm{P}$ tel que la condition (3) de 8.1.9 soit vérifiée et tel que la restriction $\kappa$ à $\Lambda$ est triviale. Notons encore par $\tilde{\kappa}$ le caractère de $\mathrm{P} / \Lambda$ qui s'en déduit. Notons $\mathrm{H}_c^n (\mathrm{M} / \Lambda)_{\tilde{\kappa}}$ le sous-espace propre de $\mathrm{H}_c^n (\mathrm{M} / \Lambda)$ de valeur propre $\tilde{\kappa}$. L'énoncé suivant est un corollaire immédiat de 8.1.6.

Proposition 8.1.13. — On a la formule

$$
\sharp \mathrm{P} ^ {0} (k) \sharp \mathrm{X} (k) _ {\kappa} = \sum_ {n} (- 1) ^ {n} \operatorname{tr} (\sigma , \mathrm{H} _ {c} ^ {n} (\mathrm{M} / \Lambda) _ {\tilde {\kappa}}).
$$

De plus, si $\Lambda' \subset \Lambda$ est un sous-groupe de rang maximal et $\sigma$-invariant alors on a un isomorphisme canonique

$$
\mathrm{H} _ {c} ^ {n} (\mathrm{M} / \Lambda^ {\prime}) _ {\tilde {\kappa}} \rightarrow \mathrm{H} _ {c} ^ {n} (\mathrm{M} / \Lambda) _ {\tilde {\kappa}}
$$

pour chaque entier n.

Démonstration. — Comme $\Lambda$ est un sous-groupe sans torsion de P, son intersection avec la composante neutre $P^{0}$ est triviale. Par conséquent, l'homomorphisme $P^{0} \to P/\Lambda$ induit un isomorphisme de $P^{0}$ sur la composante neutre de $P/\Lambda$. En comparant avec 8.1.6, on obtient la formule qu'on voulait.

En pratique, cette proposition est utile pour comparer et pour contrôler la variation de la somme  $\sharp\mathbf{X}(k')_{\kappa}$  quand on prend les points à valeurs dans une extension finie  $k'$  de k variable. Soit  $m=\deg(k'/k)$ . Pour toute classe d'isomorphisme  $x'$  de  $\mathbf{X}(k')$ , on a une classe de  $\sigma^{m}$ -conjugaison dans P. Puisque  $\kappa:P\to\bar{\mathbf{Q}}_{\ell}^{\times}$  est  $\sigma$ -invariant, il est à plus forte raison  $\sigma^{m}$ -invariant de sorte qu'on peut définir l'accouplement  $\langle\mathrm{cl}(x),\kappa\rangle\in\bar{\mathbf{Q}}_{\ell}^{\times}$ . On a alors la formule

$$
\sharp \mathrm{P} ^ {0} (k ^ {\prime}) \sharp \mathrm{X} (k ^ {\prime}) _ {\kappa} = \sum_ {n} (- 1) ^ {n} \operatorname{tr} (\sigma^ {m}, \mathrm{H} _ {c} ^ {n} (\mathrm{M} / \Lambda) _ {\tilde {\kappa}}).
$$

Corollaire 8.1.14. — Soient X = [M/P] et X' = [M'/P'] comme ci-dessus. Soient $\kappa: P \to \bar{\mathbf{Q}}_{\ell}^{\times}$ et $\kappa': P' \to \bar{\mathbf{Q}}_{\ell}^{\times}$ deux caractères $\sigma$-invariants d'ordre fini. Supposons qu'il existe un entier m tel que pour toute extension $k'/k$ de degré $m' \geq m$, on a

$$
\sharp \mathrm{P} ^ {0} (k ^ {\prime}) \sharp \mathrm{X} (k ^ {\prime}) _ {\kappa} = \sharp \mathrm{P} ^ {0} (k ^ {\prime}) \sharp \mathrm{X} ^ {\prime} (k ^ {\prime}) _ {\kappa^ {\prime}}.
$$

Alors, on a l'égalité

$$
\sharp \mathrm{P} ^ {0} (k) \sharp \mathrm{X} (k) _ {\kappa} = \sharp \mathrm{P} ^ {\prime 0} (k) \sharp \mathrm{X} ^ {\prime} (k) _ {\kappa^ {\prime}}.
$$

Nous allons maintenant étudier deux exemples jumeaux qui sont parmi les fibres de Springer affines les plus simples. Dans ces cas, on peut calculer directement les nombres  $\sharp\mathbf{X}(k)_{\kappa}$ .

Exemple 8.1.15. — Soient A un tore déployé de dimension un sur k et  $\mathbf{X}_{*}(\mathbf{A})$  son groupe des cocaractères. Considérons une extension

$$
1 \rightarrow \mathrm{A} \rightarrow \mathrm{P} \rightarrow \mathbf {X} _ {*} (\mathrm{A}) \rightarrow 1.
$$

Le faisceau $\underline{\mathrm{RHom}}(\mathbf{X}_{*}(\mathrm{A}),\mathrm{A})$ est concentré en degré 0 avec

$$
\operatorname{Hom} (\mathbf {X} _ {*} (\mathrm{A}), \mathrm{A}) = \mathbf {G} _ {m}.
$$

Puisque  $\mathrm{H}^{1}(k,\mathbf{G}_{m})=0$ , on peut scinder la suite exacte ci-dessus et en particulier, il existe un isomorphisme

$$
\mathrm{P} \simeq \mathrm{A} \times \mathbf {X} _ {*} (\mathrm{A}).
$$

Dans les deux cas, on a un isomorphisme  $P = G_{m} \times Z$  sur  $\bar{k}$ .

Considérons la chaîne infinie de $\mathbf{P}^{1}$ obtenue à partir de la réunion disjointe $\bigsqcup_{i}\mathbf{P}_{i}^{n}$ où $\mathbf{P}_{i}^{n}$ désigne la $i$-ième copie de $\mathbf{P}^{1}$, en recollant le point infini $\infty_{i}$ de $\mathbf{P}_{i}^{1}$ avec le point zéro $0_{i+1}$ de $\mathbf{P}_{i+1}^{1}$. Le groupe $\mathbf{G}_{m} \times \mathbf{Z}$ agit sur $\bigsqcup_{i}\mathbf{P}_{i}^{n}$ de façon compatible avec le recollement de sorte qu'il agit encore sur la chaîne.

Considérons un $k$-schéma M muni d'une action de P tel qu'après le changement de base à $\bar{k}$, M est isomorphe à la chaîne infinie de $\mathbf{P}^1$ munie de l'action de $\mathbf{G}_m \times \mathbf{Z}$ comme ci-dessus. On a en particulier une stratification $\mathrm{M} = \mathrm{M}_0 \sqcup \mathrm{M}_1$ où $\mathrm{M}_0$ est un torseur sous P et où $\mathrm{M}_1$ est un torseur sous le groupe discret $\mathbf{X}_*(\mathrm{A})$. Le groupoïde $\mathrm{X} = [\mathrm{M}/\mathrm{P}]$ a essentiellement deux objets $x_1$ et $x_0$ avec $\operatorname{Aut}(x_1) = \mathrm{A}$ et $\operatorname{Aut}(x_0)$ trivial. On a aussi deux classes de cohomologie

$$
\operatorname{cl} _ {1}, \operatorname{cl} _ {0} \in \mathrm{H} ^ {1} (k, \mathrm{P}) = \mathrm{H} ^ {1} (k, \mathbf {X} _ {*} (\mathrm{A})).
$$

Il y a exactement trois possibilités pour ces classes.

(1) Si A =  $\mathbf{G}_{m}$  alors  $\mathbf{X}_{*}(A) = \mathbf{Z}$ . Dans ce cas, on a l'annulation de  $\mathrm{H}^{1}(k, \mathbf{X}_{*}(A))$ . On a alors la formule

$$
\sharp \mathrm{X} (k) = 1 + \frac {1}{q - 1} = \frac {q}{q - 1}
$$

qu'il est plus agréable de retenir sous la forme

$$
\sharp \mathrm{A} (k) \sharp \mathrm{X} (k) = q.
$$

(2) Supposons que A est un tore de dimension un non déployé sur $k$. Il a donc $q + 1$ points à valeurs dans $k$. Dans ce cas $\mathbf{X}_{*}(\mathrm{A})$ est le groupe $\mathbf{Z}$ muni de l'action de $\sigma$ donnée par $m \mapsto -m$. Le groupe $\mathrm{H}^{1}(k, \mathbf{X}_{*}(\mathrm{A}))$ a deux éléments et ses éléments peuvent être décrits explicitement comme suit. Un $\mathbf{X}_{*}(\mathrm{A})$-torseur E sur $k$ est un espace principal homogène E sous $\mathbf{Z}$ muni d'une application $\sigma : \mathrm{E} \to \mathrm{E}$ compatible avec l'action de $\sigma$ sur $\mathbf{Z}$ donnée ci-dessus. Pour tout $e \in \mathrm{E}$, la différence $\sigma(e) - e$ est un entier dont la parité est indépendante du choix de $e$. Si $\sigma(e) - e$ est pair, $\operatorname{cl}(\mathrm{E})$ est l'élément trivial de $\mathrm{H}^{1}(k, \mathbf{X}_{*}(\mathrm{A}))$. Si $\sigma(e) - e$ est impair, $\operatorname{cl}(\mathrm{E})$ est l'élément non-trivial de $\mathrm{H}^{1}(k, \mathbf{X}_{*}(\mathrm{A}))$.

Supposons maintenant que  $cl_{0}=0$ . Alors, il existe exactement une copie  $P_{i}^{1}$  dans la chaîne infinie stable sous  $\sigma$ . Puisque A est le tore non-déployé,  $\sigma$  échange nécessairement  $0_{i}$  et  $\infty_{i}$ . Il s'ensuit que  $cl_{1}\neq0$ .

Si $\kappa : \mathrm{H}^1(k, \mathbf{X}_*(\mathrm{A})) \to \bar{\mathbf{Q}}_\ell^\times$ est le caractère non-trivial, on a alors la formule

$$
\sharp \mathbf {X} (k) _ {\kappa} = 1 - \frac {1}{q + 1} = \frac {q}{q + 1}
$$

qu'il est plus agréable de retenir sous la forme

$$
\sharp \mathrm{A} (k) \sharp \mathrm{X} (k) _ {\kappa} = q.
$$

(3) Supposons toujours que A est le tore non-déployé mais considérons le cas où  $cl_{0} \neq 0$ . Il existe alors deux copies  $P_{i}^{1}$  et  $P_{i+1}^{1}$  échangées par  $\sigma$  de sorte que dans la chaîne infinie M, le point commun  $\infty_{i} = 0_{i+1}$  est  $\sigma$ -invariant. Il en résulte que  $cl_{1} = 0$ . On a alors la formule

$$
\sharp \mathrm{A} (k) \sharp \mathrm{X} (k) _ {\kappa} = - q
$$

où $\kappa : \mathrm{H}^1(k, \mathbf{X}_*(\mathrm{A})) \to \bar{\mathbf{Q}}_\ell^\times$ est le caractère non-trivial.

En supposant que  $M_{0}$  a au moins un k-point, on a  $cl_{0}=0$  de sorte que la troisième possibilité est exclue. Avec cette hypothèse, on constate que la formule

$$
\sharp \mathrm{A} (k) \sharp \mathrm{X} (k) _ {\kappa} = q
$$

est valide dans tous les cas.

8.2. Comptage dans une fibre de Springer affine. — Dans ce paragraphe, nous étudions le comptage de points dans une fibre de Springer affine en suivant essentiellement [26, §15] mais en tirant profit du langage développé dans le paragraphe précédent. Comme dans le paragraphe précédent, la notation  $x \in X$  signifiera  $x \in \mathrm{X}(\bar{k})$ . Lorsqu'il s'agit de coefficients autres que  $\bar{k}$ , on le précisera.

Soit $v \in |\mathbf{X}|$ un point fermé de $\mathbf{X}$. Soient $\mathrm{F}_v$ la complétion du corps des fractions rationnelles $\mathrm{F}$ par la topologie $v$-adique et $\mathcal{O}_v$ l'anneau des entiers de $\mathrm{F}_v$, $k_v$ le corps résiduel. On note $\mathrm{X}_v = \operatorname{Spec}(\mathcal{O}_v)$ et $\mathrm{X}_v^\bullet = \operatorname{Spec}(\mathrm{F}_v)$. Soit $\bar{\mathrm{F}}_v$ la complétion $v$-adique de $\bar{\mathrm{F}} = \mathrm{F} \otimes_k \bar{k}$. Soit $\bar{\mathcal{O}}_v$ l'anneau des entiers de $\bar{\mathrm{F}}_v$.

8.2.1. — Soit  $a \in \mathfrak{c}^{\heartsuit}(\mathcal{O}_{v})$  un  $X_{v}$ -point de c dont la fibre générique est semi-simple et régulière. La fibre de Springer affine réduite  $\mathcal{M}_{v}^{\mathrm{red}}(a)$  est un k-schéma localement de type fini dont l'ensemble des  $\bar{k}$ -points est

$$
\mathcal {M} _ {v} ^ {\mathrm{red}} (a) = \{g \in \mathrm{G} (\bar {\mathrm{F}} _ {v}) / \mathrm{G} (\bar {\mathcal {O}} _ {v}) | \mathrm{ad} (g) ^ {- 1} \gamma_ {0} \in \mathfrak {g} (\bar {\mathcal {O}} _ {v}) \}
$$

où $\gamma_0 = \epsilon(a)$ est la section de Kostant au point $a$. Puisque les nilpotents ne jouent aucun rôle dans la discussion qui va suivre, on va écrire simplement $\mathcal{M}_v(a)$ à la place de $\mathcal{M}_v^{\mathrm{red}}(a)$.

8.2.2. — Soit  $J_{a} = a^{*}J$  l'image inverse du centralisateur régulier. Soit  $J_{a}^{\prime}$  un  $X_{v}$ -schéma en groupes lisse de fibres connexes muni d'un homomorphisme  $J_{a}^{\prime} \to J_{a}$  qui induit un isomorphisme sur la fibre générique. En particulier,  $J_{a}^{\prime}$  peut être le schéma en groupes  $J_{a}^{0}$  des composantes neutres de  $J_{a}$  mais il sera plus souple pour les applications de considérer  $J_{a}^{\prime}$  général.

8.2.3. — Considérons le k-schéma en groupes localement de type fini  $\mathcal{P}_{v}^{\mathrm{red}}(\mathbf{J}_{a}^{\prime})$  dont l'ensemble des  $\bar{k}$ -points est

$$
\mathcal {P} _ {v} ^ {\mathrm{red}} (\mathrm{J} _ {a} ^ {\prime}) = \mathrm{J} _ {a} (\bar {\mathrm{F}} _ {v}) / \mathrm{J} _ {a} ^ {\prime} (\bar {\mathcal {O}} _ {v}).
$$

De nouveau, on va écrire simplement  $\mathcal{P}_{v}(J_{a}^{\prime})$  pour  $\mathcal{P}_{v}^{\mathrm{red}}(J_{a}^{\prime})$  car les nilpotents ne jouent pas de rôle dans la discussion qui suit. L'homomorphisme  $J_{a}^{\prime} \to J_{a}$  induit un homomorphisme

$$
\mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) \rightarrow \mathcal {P} _ {v} (\mathrm{J} _ {a})
$$

qui induit une action de $\mathcal{P}_{v}(\mathrm{J}_{a}^{\prime})$ sur $\mathcal{M}_{v}(a)$. D'après 3.4.1, cette action vérifie l'hypothèse 8.1.9 de sorte qu'on peut envisager le nombre de $k$-points du quotient $[\mathcal{M}_{v}(a)/\mathcal{P}_{v}(\mathrm{J}_{a}^{\prime})]$ ainsi que la variante avec une $\kappa$-pondération. D'après 8.1.13, on sait que ce sont des nombres finis qui ont une interprétation cohomologique. Dans ce paragraphe, nous nous intéressons à la question d'exprimer ces nombres en termes d'intégrales orbitales stables et de $\kappa$-intégrales orbitales.

Commençons par comparer les $\kappa$ qui apparaissent dans le problème de comptage 8.1 et ceux qui apparaissent dans la définition des $\kappa$-intégrales orbitales 1.7.

Lemme 8.2.4. — Supposons que la fibre spéciale de $\mathbf{J}_{a}^{\prime}$ est connexe. Il existe un isomorphisme canonique

$$
\mathrm{H} ^ {1} \left(\mathrm{F} _ {v}, \mathrm{J} _ {a}\right) = \mathrm{H} ^ {1} \left(k, \mathcal {P} _ {v} \left(\mathrm{J} _ {a} ^ {\prime}\right)\right).
$$

Démonstration. — D'après un théorème de Steinberg,  $\mathrm{H}^{1}(\bar{\mathrm{F}}_{v},\mathrm{J}_{a})=0$ . Il s'ensuit que

$$
\mathrm{H} ^ {1} (\mathrm{F} _ {v}, \mathrm{J} _ {a}) = \mathrm{H} ^ {1} (\operatorname{Gal} (\bar {k} / k), \mathrm{J} _ {a} (\bar {\mathrm{F}} _ {v})).
$$

D'après un théorème de Lang, on a l'annulation  $\mathrm{H}^{1}(k,\mathrm{J}_{a}^{\prime}(\bar{\mathcal{O}}_{v}))=0\;\mathrm{car}\;\mathrm{J}_{a}^{\prime}$  est un schéma en groupes lisse de fibres connexes. Le lemme s'en déduit.

Proposition 8.2.5. — Supposons la fibre spéciale de $\mathbf{J}_{a}^{\prime}$ connexe. Soit $\kappa : \mathrm{H}^{1}(\mathrm{F}_{v}, \mathrm{J}_{a}) \to \bar{\mathbf{Q}}_{\ell}^{\times}$ un caractère et $\kappa : \mathrm{H}^{1}(k, \mathcal{P}_{v}(\mathbf{J}_{a}^{\prime})) \to \bar{\mathbf{Q}}_{\ell}^{\times}$ le caractère qui s'en déduit. Le nombre de $k$-points avec la $\kappa$-pondération de $[\mathcal{M}_{v}(a)/\mathcal{P}_{v}(\mathbf{J}_{a}^{\prime})]$ peut alors s'exprimer comme suit

$$
\sharp \left[ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} \left(\mathrm{J} _ {a} ^ {\prime}\right) \right] (k) _ {\kappa} = \operatorname{vol} \left(\mathrm{J} _ {a} ^ {\prime} \left(\mathcal {O} _ {v}\right), \mathrm{d} t _ {v}\right) \mathbf {O} _ {a} ^ {\kappa} \left(1 _ {\mathfrak {g} _ {v}}, \mathrm{d} t _ {v}\right)
$$

où $1_{\mathfrak{g}_v}$ est la fonction caractéristique de $\mathfrak{g}(\mathcal{O}_v)$ et où $\mathrm{dt}_v$ est n'importe quelle mesure de Haar de $\mathrm{J}_a(\mathrm{F}_v)$.

Démonstration. — Rappelons la description de la catégorie

$$
[ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k).
$$

Un objet de cette catégorie consiste en un couple $x = (m, p)$ formé d'un élément $m \in \mathcal{M}_v(a)$ et d'un élément $p \in \mathcal{P}_v(\mathrm{J}_a')$ tels qu'on ait l'égalité $p\sigma(m) = m$. Une flèche de $(m, p)$ dans $(m', p')$ dans cette catégorie consiste en un élément $h \in \mathcal{P}_v(\mathrm{J}_a')$ tel que $m' = hm$ et $p' = hp\sigma(h)^{-1}$.

Notons $\mathcal{P}_{v}(\mathrm{J}_{a}^{\prime})_{\sigma}$ le groupe des classes de $\sigma$-conjugaison de $\mathcal{P}_{v}(\mathrm{J}_{a}^{\prime})$ et $\mathrm{H}^{1}(k, \mathcal{P}_{v}(\mathrm{J}_{a}^{\prime}))$ le sous-groupe des cocycles continus. Pour chaque objet $x = (m, p)$ comme ci-dessus, on définit $\operatorname{cl}(x) \in \mathcal{P}_{v}(\mathrm{J}_{a}^{\prime})_{\sigma}$ la classe de $\sigma$-conjugaison de $p$ qui appartient en fait au sous-groupe

$$
\operatorname{cl} (x) \in \mathrm{H} ^ {1} (k, \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime})) = \mathrm{H} ^ {1} (\mathrm{F} _ {v}, \mathrm{J} _ {a}).
$$

Soit $\gamma_0$ l'image de $a$ dans $\mathfrak{g}$ par la section de Kostant. On a un isomorphisme canonique $\mathrm{J}_a = \mathrm{I}_{\gamma_0}$ cf. 1.4.3 si bien que $\operatorname{cl}(x)$ peut aussi être vu comme un élément de $\mathrm{H}^1 (\mathrm{F}_v,\mathrm{I}_{\gamma_0})$.

Lemme 8.2.6. — Pour tout objet x de  $[\mathcal{M}_{v}(a)/\mathcal{P}_{v}(\mathrm{J}_{a}^{\prime})](k)$ , la classe  $\operatorname{cl}(x)$  appartient au noyau de l'homomorphisme

$$
\mathrm{H} ^ {1} \left(\mathrm{F} _ {v}, \mathrm{I} _ {\gamma_ {0}}\right)\rightarrow \mathrm{H} ^ {1} \left(\mathrm{F} _ {v}, \mathrm{G}\right).
$$

Démonstration. — Soit  $x = (p, m)$  comme ci-dessus. Soient  $g \in \mathrm{G}(\bar{\mathrm{F}}_v)$  un représentant de  $m \in \mathrm{G}(\bar{\mathrm{F}}_v)/\mathrm{G}(\bar{\mathcal{O}}_v)$  et  $j \in \mathrm{I}_{\gamma_0}(\bar{\mathrm{F}}_v)$  un représentant de p. L'égalité  $p\sigma(m) = m$  implique que

$$
g ^ {- 1} j \sigma (g) \in \mathrm{G} (\bar {\mathcal {O}} _ {v})
$$

si bien que cet élément est $\sigma$-conjugué à l'élément neutre dans $\mathrm{G}(\bar{\mathrm{F}}_v)$. Ainsi $\operatorname{cl}(x) \in \mathrm{H}^1(\mathrm{F}_v, \mathrm{I}_{\gamma_0})$ a une image triviale dans $\mathrm{H}^1(\mathrm{F}_v, \mathrm{G})$.

Continuons la démonstration de 8.2.5. Pour tout élément $\xi$ dans le noyau de $\mathrm{H}^{1}(\mathrm{F}_{v},\mathrm{I}_{\gamma_{0}})\to \mathrm{H}^{1}(\mathrm{F}_{v},\mathrm{G})$, considérons la sous-catégorie

$$
[ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] _ {\xi} (k)
$$

des objets de $[\mathcal{M}_v(a)/\mathcal{P}_v(\mathrm{J}_a')](k)$ tels que $\operatorname{cl}(x)=\xi$. Nous nous proposons d'écrire le nombre de classes d'isomorphisme de $[\mathcal{M}_v(a)/\mathcal{P}_v(\mathrm{J}_a')]_{\xi}(k)$ comme une intégrale orbitale.

Fixons $j_{\xi} \in \mathrm{I}_{\gamma_0}(\bar{\mathrm{F}}_v)$ dans la classe de $\sigma$-conjugaison $\xi$. Soit $(m,p)$ un objet de $[\mathcal{M}_v(a)/\mathcal{P}_v(\mathrm{J}_a')]_{\xi}(k)$. Puisque $p$ est $\sigma$-conjugué à $j_{\xi}$ dans $\mathcal{P}_v(\mathrm{J}_a')$, il existe $h \in \mathcal{P}_v(\mathrm{J}_a')$ tel que $j_{\xi} = h^{-1}p\sigma(h)$. Alors $(m,p)$ est isomorphe à $(h^{-1}m,j_{\xi})$. Par conséquent, la catégorie $[\mathcal{M}_v(a)/\mathcal{P}_v(\mathrm{J}_a')]_{\xi}(k)$ est équivalente à la sous-catégorie pleine formée des objets de la forme $(m,j_{\xi})$. Une flèche $(m,j_{\xi}) \to (m',j_{\xi})$ est un élément $h \in \mathcal{P}_v(\mathrm{J}_a')(k)$ tel que $hm = m'$. Puisque $J_a'$ a des fibres connexes, on a

$$
\mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) (k) = \mathrm{J} _ {a} (\mathrm{F} _ {v}) / \mathrm{J} _ {a} ^ {\prime} (\mathcal {O} _ {v}).
$$

Soit $(m,j_{\xi})$ comme ci-dessus. Choissons un représentant $g \in \mathrm{G}(\bar{\mathrm{F}}_v)$ de $m$. On a alors $g^{-1}j_{\xi}\sigma(g) \in \mathrm{G}(\bar{\mathcal{O}}_v)$. Comme tous les éléments de $\mathrm{G}(\bar{\mathcal{O}}_v)$ sont $\sigma$-conjugués à l'élément neutre, on peut choisir $g$ avec $m = g\mathrm{G}(\bar{\mathcal{O}}_v)$ tel que

$$
g ^ {- 1} j _ {\xi} \sigma (g) = 1.
$$

Soient $g, g' \in \mathrm{G}(\bar{\mathrm{F}}_v)$ deux éléments vérifiant l'équation ci-dessus et représentant la même classe $m \in \mathrm{G}(\bar{\mathrm{F}}_v)/\mathrm{G}(\bar{\mathcal{O}}_v)$. Alors $g' = gk$ avec $k \in \mathrm{G}(\mathcal{O}_v)$ si bien que l'image de $g$ dans $\mathrm{G}(\bar{\mathrm{F}}_v)/\mathrm{G}(\mathcal{O}_v)$ est bien déterminée par $(m, j_\xi)$.

Ainsi la catégorie $[\mathcal{M}_v(a) / \mathcal{P}_v(\mathrm{J}_a')]_{\xi}(k)$ est équivalente à la catégorie $\mathrm{O}_{\xi}$ dont les objets sont les éléments $g\in \mathrm{G}(\bar{\mathrm{F}}_v) / \mathrm{G}(\mathcal{O}_v)$ vérifiant deux équations

$$
\begin{array}{l} (1) g ^ {- 1} j _ {\xi} \sigma (g) = 1 \\ (2) \operatorname{ad} (g) ^ {- 1} \gamma_ {0} \in \mathfrak {g} (\bar {\mathcal {O}} _ {v}) \end{array}
$$

et dont les flèches $g \to g_1$ sont les éléments $h \in \mathrm{J}_a(\mathrm{F}_v) / \mathrm{J}_a'(\mathcal{O}_v)$ tels que $g = hg_1$. Ici, pour faire agir $h$ à gauche, on a utilisé l'isomorphisme canonique $\mathrm{J}_a = \mathrm{I}_{\gamma_0}$.

Puisque l'image de $\xi$ dans $\mathrm{H}^1 (\mathrm{F}_v,\mathrm{G})$ est triviale, il existe $g_{\xi}\in \mathrm{G}(\bar{\mathrm{F}}_v)$ tel que $g_{\xi}^{-1}j_{\xi}\sigma (g_{\xi}) = 1$. Fixons un tel $\mathbf{G}_{\xi}$ et posons

$$
\gamma_ {\xi} = \mathrm{ad} (g _ {\xi}) ^ {- 1} \gamma_ {0}.
$$

L'équation $g_{\xi}^{-1}j_{\xi}\sigma(g_{\xi}) = 1$ implique que $\gamma_{\xi} \in \mathrm{G}(\mathrm{F}_v)$. La classe de $\mathrm{G}(\mathrm{F}_v)$-conjugaison de $\gamma_{\xi}$ ne dépend pas des choix de $j_{\xi}$ et $g_{\xi}$ mais seulement de la classe $\xi \in \mathrm{H}^1(\mathrm{F}_v, \mathrm{I}_{\gamma_0})$.

En posant $g' = g_{\xi}^{-1}g$, la catégorie $\mathrm{O}_{\xi}$ peut être décrite comme suit. Ses objets sont les éléments $g' \in \mathrm{G}(\mathrm{F}_v)/\mathrm{G}(\mathcal{O}_v)$ vérifiant

$$
\operatorname{ad} \left(g ^ {\prime}\right) ^ {- 1} \left(\gamma_ {\xi}\right) \in \mathfrak {g} \left(\mathcal {O} _ {v}\right).
$$

Ses flèches $g' \to g_1'$ sont les éléments $h \in \mathrm{J}_a(\mathrm{F}_v)/\mathrm{J}_a'(\mathcal{O}_v)$ tels que $g' = hg_1'$. Ici, pour faire agir $h$ à gauche, on a utilisé l'isomorphisme canonique $\mathrm{J}_a = \mathrm{I}_{\gamma_\xi}$ où $\mathrm{I}_{\gamma_\xi}$ est le centralisateur de $\gamma_\xi$.

L'ensemble des classes d'isomorphisme de  $O_{\xi}$  est donc l'ensemble des double-classes

$$
g ^ {\prime} \in \mathrm{I} _ {\gamma_ {\xi}} (\mathrm{F} _ {v}) \backslash \mathrm{G} (\mathrm{F} _ {v}) / \mathrm{G} (\mathcal {O} _ {v})
$$

telles que  $\mathrm{ad}(g')^{-1}\gamma_{\xi}\in\mathfrak{g}(\mathcal{O}_{v})$ . Le groupe des automorphismes de  $g'$  est le groupe

$$
(\mathrm{I} _ {\gamma_ {\xi}} (\mathrm{F} _ {v}) \cap g ^ {\prime} \mathrm{G} (\mathcal {O} _ {v}) g ^ {- 1}) / \mathrm{J} _ {a} ^ {\prime} (\mathcal {O} _ {v})
$$

dont le cardinal peut être exprimé en termes de volumes comme suit

$$
\frac {\operatorname{vol} \left(\mathrm{I} _ {\gamma_ {\xi}} \left(\mathrm{F} _ {v}\right) \cap g ^ {\prime} \mathrm{G} \left(\mathcal {O} _ {v}\right) g ^ {\prime - 1} , \mathrm{d} t _ {v}\right)}{\operatorname{vol} \left(\mathrm{J} _ {a} ^ {\prime} \left(\mathcal {O} _ {v}\right) , \mathrm{d} t _ {v}\right)}.
$$

On a donc

$$
\sharp \mathrm{O} _ {\xi} = \sum \frac {\operatorname{vol} (\mathrm{J} _ {a} ^ {\prime} (\mathcal {O} _ {v}) , \mathrm{d} t _ {v})}{\operatorname{vol} (\mathrm{J} _ {a} (\mathrm{F} _ {v}) \cap g ^ {\prime} \mathrm{G} (\mathcal {O} _ {v}) g ^ {- 1} , \mathrm{d} t _ {v})}
$$

la sommation étant étendue sur l'ensemble des double-classes

$$
g ^ {\prime} \in \mathrm{I} _ {\gamma_ {\xi}} (\mathrm{F} _ {v}) \backslash \mathrm{G} (\mathrm{F} _ {v}) / \mathrm{G} (\mathcal {O} _ {v})
$$

telles que  $\mathrm{ad}(g')^{-1}\gamma_{\xi}\in\mathfrak{g}(\mathcal{O}_{v})$ . On obtient donc la formule

$$
\sharp [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a}) ] _ {\xi} (k) = \sharp \mathrm{O} _ {\xi} = \operatorname{vol} (\mathrm{J} _ {a} ^ {\prime} (\mathcal {O} _ {v}), \mathrm{d} t) \mathbf {O} _ {\gamma_ {\xi}} (1 _ {\mathfrak {g} _ {v}}, \mathrm{d} t _ {v}).
$$

En sommant sur le noyau de $\mathrm{H}^{1}(\mathrm{F},\mathrm{I}_{\gamma_{0}})\to \mathrm{H}^{1}(\mathrm{F},\mathrm{G})$, on obtient la formule

$$
\sharp [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k) _ {\kappa} = \operatorname{vol} (\mathrm{J} _ {a} ^ {\prime} (\mathcal {O} _ {v}), \mathrm{d} t _ {v}) \mathbf {O} _ {a} ^ {\kappa} (1 _ {\mathfrak {g} _ {v}}, \mathrm{d} t _ {v})
$$

qu'on voulait.

On voudra ensuite le même type d'énoncé pour les schémas en groupes  $J_{a}^{\prime}$  n'ayant pas nécessairement une fibre spéciale connexe et en particulier pour  $J_{a}$  lui-même. Le comptage direct du nombre de k-points du quotient  $[\mathcal{M}_{v}(a)/\mathcal{P}_{v}(\mathrm{J}_{a})]$  s'avère très pénible. Il est plus économique de passer par la comparaison avec le cas connexe. Nous allons énoncer le résultat seulement dans le cas de  $J_{a}$  bien qu'il soit valide en général.

Soit $\kappa : \mathrm{H}^1(k, \mathcal{P}_v(J_a)) \to \bar{\mathbf{Q}}_\ell^\times$. En utilisant l'homomorphisme

$$
\mathrm{H} ^ {1} (k, \mathrm{P} _ {v} (\mathrm{J} _ {a} ^ {0})) \rightarrow \mathrm{H} ^ {1} (k, \mathcal {P} _ {v} (\mathrm{J} _ {a})),
$$

on obtient un caractère de  $\mathrm{H}^{1}(k,\mathcal{P}_{v}(\mathrm{J}_{a}^{0}))$  et par conséquent un caractère de  $\mathrm{H}^{1}(\mathrm{F}_{v},\mathrm{J}_{a})$  que nous allons noter  $\kappa$  également.

Proposition 8.2.7. — Considérons $\kappa$ un caractère de $\mathrm{H}^{1}(k,\mathcal{P}_{v}(\mathrm{J}_{a}))$ et notons $\kappa$: $\mathrm{H}^{1}(\mathrm{F}_{v},\mathrm{J}_{a})\to \bar{\mathbf{Q}}_{\ell}^{\times}$ le caractère de $\mathrm{H}^{1}(\mathrm{F}_{v},\mathrm{J}_{a})$ qui s'en déduit. Alors, le nombre de $k$-points avec la $\kappa$-pondération de $[\mathcal{M}_v(a)/\mathcal{P}_v(\mathrm{J}_a)]$ peut s'exprimer comme suit

$$
\sharp [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a}) ] (k) _ {\kappa} = \operatorname{vol} (\mathrm{J} _ {a} ^ {0} (\mathcal {O} _ {v}), \mathrm{d} t _ {v}) \mathbf {O} _ {a} ^ {\kappa} (1 _ {\mathfrak {g} _ {v}}, \mathrm{d} t _ {v})
$$

où  $1_{g_{v}}$  est la fonction caractéristique de  $\mathfrak{g}(\mathcal{O}_{v})$  et où  $dt_{v}$  est n'importe quelle mesure de Haar de  $\mathrm{J}_{a}(\mathrm{F}_{v})$ . De plus, si  $\kappa : H^{1}(F_{v}, J_{a}) \to \bar{\mathbf{Q}}_{\ell}^{\times}$  est un caractère qui ne provient pas d'un caractère de  $\mathrm{H}^{1}(k, \mathcal{P}_{v}(J_{a}))$  alors la  $\kappa$ -intégrale orbitale  $\mathbf{O}_{a}^{\kappa}(1_{g_{v}}, dt_{v})$  est nulle.

Démonstration. — Il s'agit d'une comparaison entre  $\mathcal{P}_{v}(J_{a})$  et le cas connu  $\mathcal{P}_{v}(J_{a}^{0})$ . Il suffit de démontrer l'égalité

$$
\sharp [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a}) ] (k) _ {\kappa} = \sharp [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0}) ] (k) _ {\kappa}
$$

dans le premier cas et l'annulation de  $[\mathcal{M}_{v}(a)/\mathcal{P}_{v}(\mathrm{J}_{a}^{0})](k)_{\kappa}$  dans le second cas. La démonstration sera fondée sur le même principe que 8.1.7 bien que les détails sont plus compliqués dans le cas présent.

On a une suite exacte

$$
1 \to \pi_ {0} (\mathrm{J} _ {a, v}) \to \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0}) \to \mathcal {P} _ {v} (\mathrm{J} _ {a}) \to 1
$$

où $\pi_0(J_{a,v})$ est le groupe des composantes connexes de la fibre de $J_a$ en $v$. On en déduit une suite exacte longue

(8.2.8)

$$
1 \to \pi_ {0} (\mathrm{J} _ {a, v}) ^ {\sigma} \to \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0}) ^ {\sigma} \to \mathcal {P} _ {v} (\mathrm{J} _ {a}) ^ {\sigma}\tag{8.2.9}
$$

$$
\rightarrow \pi_ {0} (\mathrm{J} _ {a, v}) _ {\sigma} \rightarrow \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0}) _ {\sigma} \rightarrow \mathcal {P} _ {v} (\mathrm{J} _ {a}) _ {\sigma} \rightarrow 1
$$

où l'exposant  $\sigma$  désigne le groupe des  $\sigma$ -invariants et l'indice  $\sigma$  désigne le groupe des  $\sigma$ -coinvariants.

Considérons le foncteur

$$
\pi : [ \mathcal {M} _ {v} (\mathrm{J} _ {a}) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0}) ] (k) \to [ \mathcal {M} _ {v} (\mathrm{J} _ {a}) / \mathcal {P} _ {v} (\mathrm{J} _ {a}) ] (k).
$$

Il envoie un objet $x' = (m, p')$ avec $m \in \mathcal{M}_v(a)$ et $p' \in \mathcal{P}_v(\mathrm{J}_a^0)$ tel que $p' \sigma(m) = m$ sur l'objet $x = (m, p)$ où $p$ est l'image de $p'$ dans $\mathcal{P}_v(\mathrm{J}_a)$. Choissons un ensemble de représentants $\{x_\psi \mid \psi \in \Psi\}$ des classes d'isomorphisme de $[\mathcal{M}_v(\mathrm{J}_a)/\mathcal{P}_v(\mathrm{J}_a)](k)$.

Puisque l'homomorphisme $\mathcal{P}_v(\mathrm{J}_a^0) \to \mathcal{P}_v(\mathrm{J}_a)$ est surjectif, cette sous-catégorie de $[\mathcal{M}_v(\mathrm{J}_a)/\mathcal{P}_v(\mathrm{J}_a^0)](k)$ est équivalente à $[\mathcal{M}_v(\mathrm{J}_a)/\mathcal{P}_v(\mathrm{J}_a^0)](k)$ si bien que pour calculer les nombres $\sharp [\mathcal{M}_v(\mathrm{J}_a)/\mathcal{P}_v(\mathrm{J}_a^0)](k)_\kappa$, il est loisible de se restreindre à cette sous-catégorie.

Pour tout $\psi \in \Psi$, considérons la sous-catégorie pleine

$$
[ \mathcal {M} _ {v} (\mathrm{J} _ {a}) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0}) ] (k) _ {x _ {\psi}}
$$

de $[\mathcal{M}_v(\mathrm{J}_a) / \mathcal{P}_v(\mathrm{J}_a^0)](k)$ formée des objets de la forme $x_{\psi}' = (m_{\psi}, p_{\psi}')$ avec $p_{\psi}' \mapsto p_{\psi}$. Si $\psi \neq \psi'$, deux objets $x_{\psi}' \in [\mathcal{M}_v(\mathrm{J}_a) / \mathcal{P}_v(\mathrm{J}_a^0)](k)_{x_\psi}$ et $x_{\psi'}' \in [\mathcal{M}_v(\mathrm{J}_a) / \mathcal{P}_v(\mathrm{J}_a^0)](k)_{x_{\psi'}}$ ne sont pas isomorphes. De plus pour tout $x' \in [\mathcal{M}_v(\mathrm{J}_a) / \mathcal{P}_v(\mathrm{J}_a^0)](k)$ il existe $\psi \in \Psi$ et $x_{\psi}' \in [\mathcal{M}_v(\mathrm{J}_a) / \mathcal{P}_v(\mathrm{J}_a^0)](k)_{x_\psi}$ tels que $x'$ et $x_{\psi}'$ sont isomorphes. Ainsi, la réunion disjointe des catégories

$$
\bigsqcup_ {\psi} [ \mathcal {M} _ {v} (\mathrm{J} _ {a}) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0}) ] (k) _ {x _ {\psi}}
$$

forme une sous-catégorie pleine de  $[\mathcal{M}_{v}(\mathrm{J}_{a})/\mathcal{P}_{v}(\mathrm{J}_{a}^{0})](k)$  qui lui est équivalente. Par conséquent, pour compter les objets de  $[\mathcal{M}_{v}(\mathrm{J}_{a})/\mathcal{P}_{v}(\mathrm{J}_{a}^{0})](k)$ , on peut compter dans chaque  $[\mathcal{M}_{v}(\mathrm{J}_{a})/\mathcal{P}_{v}(\mathrm{J}_{a}^{0})](k)_{x_{\psi}}$  et puis faire la somme sur les  $\psi\in\Psi$ .

Fixons un  $x_{\psi}$  et notons le simplement  $x = (m, p)$ . La catégorie

$$
[ \mathcal {M} _ {v} (\mathrm{J} _ {a}) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0}) ] (k) _ {x}
$$

n'est pas difficile à décrire. En fixant un objet $x_{1}=(m,p_{1})$ avec $p_{1}\mapsto p$, on identifie l'ensemble des objets de cette catégorie avec le groupe $\pi_{0}(J_{a,v})$ qui est le noyau de $\mathcal{P}_{v}(J_{a}^{0})\to\mathcal{P}_{v}(J_{a})$. Une flèche dans cette catégorie est donnée par un élément du groupe

$$
\mathrm{H} _ {1} = \{h _ {1} \in \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0}) \mid h m = m \text {et} h _ {1} \sigma (h _ {1}) ^ {- 1} \in \pi_ {0} (\mathrm{J} _ {a, v}) \}.
$$

La catégorie  $[\mathcal{M}_{v}(\mathrm{J}_{a})/\mathcal{P}_{v}(\mathrm{J}_{a}^{0})]_{x}$  est équivalente à la catégorie quotient de l'ensemble  $\pi_{0}(\mathrm{J}_{a,v})$  par l'action de  $H_{1}$  avec  $H_{1}$  agissant à travers l'homomorphisme  $\alpha:H_{1}\to\pi_{0}(\mathrm{J}_{a,v})$  défini par  $\alpha(h_{1})=h_{1}\sigma(h_{1})^{-1}$ . L'ensemble des classes d'isomorphisme de cette catégorie s'identifie avec le conoyau  $\operatorname{cok}(\alpha)$  de  $\alpha$  et le groupe des automorphismes de chaque objet s'identifie avec le noyau  $\ker(\alpha)$ . Ceci montre en particulier que  $H_{1}$  est un groupe fini.

Soit $\kappa$ un caractère de $\mathrm{H}^1 (k,\mathcal{P}_v(\mathrm{J}_a^0))$. Ce groupe s'identifie canoniquement à la partie de torsion de $\mathcal{P}_v(\mathrm{J}_a^0)_\sigma$. Considérons la restriction de $\kappa$ à $\pi_0(\mathrm{J}_{a,v})_\sigma$ et notons aussi $\kappa$ le caractère $\pi_0(\mathrm{J}_{a,v})\to \bar{\mathbf{Q}}_\ell^\times$ qui s'en déduit. Ce caractère est certainement trivial sur l'image de $\alpha :\mathrm{H}_1\to \pi_0(\mathrm{J}_{a,v})_\sigma$ si bien qu'il définit un caractère sur le conoyau $\kappa :\operatorname {cok}(\alpha)\to \bar{\mathbf{Q}}_\ell^\times$. La somme

$$
\sum_ {x ^ {\prime}} \frac {\langle \mathrm{cl} (x ^ {\prime}) , \kappa \rangle}{\sharp \mathrm{Aut} (x ^ {\prime})} = 0
$$

sur l'ensemble des classes d'isomorphisme de la sous-catégorie pleine $[\mathcal{M}_v(\mathrm{J}_a) / \mathcal{P}_v(\mathrm{J}_a^0)]_x$ est alors égale à

$$
\sum_ {z \in \operatorname{cok} (\alpha)} \frac {\langle z , \kappa \rangle}{\sharp \ker (\alpha)} \left\langle \operatorname{cl} (x _ {1}), \kappa \right\rangle .
$$

Si la restriction de $\kappa$ à $\pi_0(\mathbf{J}_{a,v})$ est non triviale alors cette somme est nulle ce qui entraîne l'annulation

$$
[ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0}) ] (k) _ {\kappa} = 0.
$$

Supposons maintenant que la restriction de $\kappa$ à $\pi_0(\mathrm{J}_{a,v})$ est triviale. Dans ce cas, $\kappa$ se factorise par $\mathrm{H}^1 (k,\mathcal{P}_v(\mathrm{J}_a))$ et la somme ci-dessus est égale à

$$
\frac {\sharp \operatorname{cok} (\alpha)}{\sharp \ker (\alpha)} \langle \operatorname{cl} (x), \kappa \rangle .
$$

Il reste à calculer  $\sharp\operatorname{cok}(\alpha)/\sharp\ker(\alpha)$ . La suite exacte

$$
1 \rightarrow \ker (\alpha) \rightarrow H _ {1} \rightarrow \pi_ {0} (J _ {a, v}) \rightarrow \operatorname{coker} (\alpha) \rightarrow 1
$$

implique l'égalité

$$
\frac {\sharp \operatorname{cok} (\alpha)}{\sharp \ker (\alpha)} = \frac {\sharp \pi_ {0} (J _ {a , v})}{\sharp H _ {1}}.
$$

Soient  $h_{1} \in H_{1}$  et h son image dans  $\mathcal{P}_{v}(J_{a})$ . On a alors  $h\sigma(h)^{-1} = 1$  de sorte que  $h \in \mathcal{P}_{v}(J_{a})^{\sigma}$ . Soit stab(m) le sous-groupe des éléments de  $\mathcal{P}_{v}(J_{a})$  qui stabilisent m. On a alors la suite exacte

$$
1 \to \pi_ {0} (\mathrm{J} _ {a, v}) \to \mathrm{H} _ {1} \to \mathcal {P} _ {v} (\mathrm{J} _ {a}) ^ {\sigma} \cap \operatorname{stab} (m) \to 1
$$

où $\mathcal{P}_{v}(\mathrm{J}_{a})^{\sigma}\cap\mathrm{stab}(m)$ est exactement le groupe des automorphismes de $\mathrm{Aur}(x)$ dans la catégorie $[\mathcal{M}_{v}(\mathrm{J}_{a})/\mathcal{P}_{v}(\mathrm{J}_{a})]$. On a donc l'égalité

$$
\frac {\sharp \pi_ {0} (\mathrm{J} _ {a , v})}{\sharp \mathrm{H} _ {1}} = \frac {1}{\sharp \operatorname{Aut} (x)}
$$

qui implique l'égalité

$$
\sharp [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a}) ] (k) _ {\kappa} = \sharp [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0}) ] (k) _ {\kappa}
$$

qu'on voulait.

En appliquant les résultats généraux de 8.1 à la situation présente, on obtient une interprétation cohomologique des intégrales orbitales stables et des $\kappa$-intégrales orbitales. Prenons un sous-groupe sans torsion $\sigma$-stable $\Lambda$ de $\mathcal{P}_v(J_a^0)$ comme dans 8.1.9. Ce sous-groupe existe en vertu de la discussion qui suit 8.1.9 et du résultat de Kazhdan-Lusztig cf. 3.4.1. On obtient le corollaire suivant de 8.1.13 et 8.2.5.

Corollaire 8.2.10. — Soit $\kappa$ un caractère de $\mathrm{H}^{1}(\mathrm{F}_{v},\mathrm{J}_{a})$. Soit $\mathbf{J}_{a}^{\mathrm{b},0}$ la composante neutre du modèle de Néron de $\mathbf{J}_{a}$. Pour tout $\Lambda$ comme ci-dessus, on a l'égalité

$$
\sum_ {n} (- 1) ^ {n} \operatorname{tr} (\sigma , \mathrm{H} ^ {n} ([ \mathcal {M} _ {v} (a) / \Lambda ]) _ {\kappa}) = \operatorname{vol} (\mathrm{J} _ {a} ^ {\flat , 0} (\mathcal {O} _ {v}), \mathrm{d} t _ {v}) \mathbf {O} _ {a} ^ {\kappa} (1 _ {\mathfrak {g} _ {v}}, \mathrm{d} t _ {v}).
$$

Démonstration. — En mettant ensemble 8.1.13 et 8.2.5 on obtient la formule

$$
\begin{array}{l} \sum_ {n} (- 1) ^ {n} \mathrm{tr} (\sigma , \mathrm{H} ^ {n} ([ \mathcal {M} _ {v} (a) / \Lambda ]) _ {\kappa}) \\ = (\sharp \mathcal {P} _ {v} ^ {0} (\mathrm{J} _ {a} ^ {0}) (k)) \mathrm{vol} (\mathrm{J} _ {a} ^ {0} (\mathcal {O} _ {v}), \mathrm{d} t _ {v}) \mathbf {O} _ {a} ^ {\kappa} (1 _ {\mathfrak {g} _ {v}}, \mathrm{d} t _ {v}) \end{array}
$$

où $\sharp \mathcal{P}_v^0 (\mathrm{J}_a^0)(k)$ est le nombre de $k$-points de la composante neutre de $\mathcal{P}_v(\mathrm{J}_a^0)$. Si $\mathrm{J}_a^{\flat,0}$ est la composante neutre du modèle de Néron, on a un homomorphisme $\mathrm{J}_a^0\to \mathrm{J}_a^{\flat,0}$ qui induit une suite exacte

$$
1 \to J _ {a} ^ {\flat , 0} (\bar {\mathcal {O}} _ {v}) / J _ {a} ^ {0} (\bar {\mathcal {O}} _ {v}) \to \mathcal {P} _ {v} (J _ {a} ^ {0}) \to \mathcal {P} _ {v} (J _ {a} ^ {\flat , 0}) \to 1
$$

qui permet d'identifier la composante neutre $\mathcal{P}_{v}^{0}(J_{a}^{0})$ de $\mathcal{P}_{v}(J_{a}^{0})$ avec le $k$-groupe affine connexe dont les $\bar{k}$-points sont $J_{a}^{\flat,0}(\bar{\mathcal{O}}_{v})/J_{a}^{0}(\bar{\mathcal{O}}_{v})$. Puisque $J_{a}^{0}$ et $J_{a}^{\flat,0}$ sont des schémas en groupes de fibres connexes, on en déduit une suite exacte

$$
1 \to \mathrm{J} _ {a} ^ {0} (\mathcal {O} _ {v}) \to \mathrm{J} _ {a} ^ {\flat , 0} (\mathcal {O} _ {v}) \to \mathcal {P} _ {v} ^ {0} (\mathrm{J} _ {a} ^ {0}) (k) \to 1
$$

d'où l'égalité

$$
(\sharp \mathcal {P} _ {v} ^ {0} (J _ {a} ^ {0}) (k)) \mathrm{vol} (J _ {a} ^ {0} (\mathcal {O} _ {v}), \mathrm{d} t _ {v}) = \mathrm{vol} (J _ {a} ^ {\flat , 0} (\mathcal {O} _ {v}), \mathrm{d} t _ {v})
$$

pour n'importe quelle mesure de Haar  $dt_{v}$  sur  $\mathrm{J}(\mathrm{F}_{v})$ . Le corollaire s'en déduit.

8.3. Un cas très simple. — Soit v un point fermé de X. Notons  $k_{v}$  le corps résiduel de v. Choissons un point géométrique  $\bar{v}$  au-dessus de v. Notons  $\mathrm{X}_{v} = \operatorname{Spec}(\mathcal{O}_{v})$  la complétion de X en v et  $\mathrm{X}_{v}^{\bullet} = \operatorname{Spec}(\mathrm{F}_{v})$  où  $F_{v}$  est le corps des fractions de  $O_{v}$ . Choissons un uniformisant  $\epsilon_{v}$ . Dans ce paragraphe, nous notons G la restriction de G à  $X_{v}$  et  $G^{\bullet}$  la restriction de G à  $X_{v}^{\bullet}$ .

8.3.1. — Soit  $a \in \mathfrak{c}(\mathcal{O}_{v})$  dont l'image dans  $\mathfrak{c}(\mathrm{F}_{v})$  est régulière et semi-simple. Soit  $d_{v}(a) = \deg_{v}(a^{*}\mathfrak{D}_{\mathrm{G}}) \in \mathbf{N}$ . Nous allons supposer que

$$
d _ {v} (a) = 2 \quad \mathrm{et} \quad c _ {v} (a) = 0.
$$

D'après la formule de Bezrukavnikov cf. 3.7.5, la dimension de la fibre de Springer affine $\mathcal{M}_{v}(a)$ est alors égale à un. On va montrer qu'au-dessus de $\bar{k}$, cette fibre de Springer affine est une réunion disjointe des copies de la chaîne infinie des droites projectives.

8.3.2. — Soit $\gamma_0 = \epsilon(a) \in \mathfrak{g}(F_v)$ la section de Kostant appliquée à $a$. Son centralisateur $T^\bullet = I_{\gamma_0}$ est un sous-tore maximal de $G^\bullet$. L'hypothèse $c_v(a) = 0$ implique que $T^\bullet$ est un sous-tore non ramifié c'est-à-dire qu'il s'étend en un sous-tore maximal $T$ de $G$. Soit $\Phi$ l'ensemble des racines de $\bar{T} = T \otimes_{\mathcal{O}_v} \bar{\mathcal{O}}_\bar{v}$. On a alors la fonction de valuation radicielle de Goresky, Kottwitz et MacPherson cf. [28]

$$
r _ {a}: \Phi \to \mathbf {N}
$$

définie par  $r_{a}(\alpha)=\mathrm{val}(\alpha(\gamma_{0}))$  où on a pris la valuation sur  $\bar{F}_{\bar{v}}$  qui étend la valuation sur  $F_{v}$ . On a alors

$$
d _ {v} (a) = \sum_ {\alpha \in \Phi} r _ {\alpha} (\gamma_ {0}).
$$

Il existe donc une unique paire de racines  $\pm\alpha$  telle que  $r_{\pm\alpha}(\gamma_{0})=1$  et  $r_{\alpha'}(\gamma_{0})=0$  pour toute racine  $\alpha'\notin\{\pm\alpha\}$ .

8.3.3. — Le groupe de Galois  $\operatorname{Gal}(\bar{k}/k_{v})$  agit sur  $\Phi$  en laissant invariante la fonction  $r_{a}(\alpha)$  de sorte qu'il laisse stable le couple  $\{\pm\alpha\}$ . Soit  $\bar{G}_{\pm\alpha}$  le sous-groupe de  $\bar{G}=G\otimes_{O_{v}}\bar{O}_{\bar{v}}$  engendré par  $\bar{T}$  et par les sous-groupes radiciels  $U_{\alpha}$  et  $U_{-\alpha}$ . L'action du groupe de Galois de  $\operatorname{Gal}(\bar{k}/k_{v})$  sur  $\bar{T}$  laissant stable  $\{\pm\alpha\}$  permet de descendre  $\bar{G}_{\pm\alpha}$  en un sous-schéma en groupes réductifs  $G_{\pm\alpha}$  de  $G_{O_{v}}$ . Le centre  $Z_{\pm\alpha}$  de  $G_{\pm\alpha}$  qui s'identifie au noyau de  $\alpha:T\to G_{m}$ , est aussi défini sur  $O_{v}$ . Soit  $A_{\pm\alpha}=T/Z_{\pm\alpha}$ ; c'est un tore de dimension un sur  $X_{v}$ .

Proposition 8.3.4. — On a un homomorphisme canonique $\mathbf{J}_{a} \to \mathbf{T}$ dont l'image au niveau des $\bar{\mathcal{O}}_{\bar{v}}$-points est le noyau de l'homomorphisme composé de la réduction modulo l'idéal maximal $\mathrm{T}(\bar{\mathcal{O}}_{\bar{v}}) \to \mathrm{T}(\bar{k})$ et de la racine $\alpha: \mathrm{T}(\bar{k}) \to \mathbf{G}_{m}(\bar{k})$.

On en déduit la description suivante de $\mathcal{P}_{v}(\mathrm{J}_{a})$.

Corollaire 8.3.5. — On a une suite exacte de groupes abéliens avec l'action d'endomorphisme de Frobenius σ

$$
1 \to \mathrm{A} _ {\pm \alpha} (\bar {k}) \to \mathcal {P} _ {\bar {v}} (\mathrm{J} _ {a}) (\bar {k}) \to \mathbf {X} _ {*} (\mathrm{T}) \to 1
$$

où $\mathbf{X}_{*}(\mathrm{T})$ est le groupe des cocaractères du tore T au-dessus de $\bar{\mathcal{O}}_{\bar{v}}$.

Démonstration. — On déduit de la suite exacte

$$
1 \to \mathrm{J} _ {a} (\bar {\mathcal {O}} _ {\bar {v}}) \to \mathrm{T} (\bar {\mathcal {O}} _ {\bar {v}}) \to \mathrm{A} _ {\pm \alpha} (\bar {k}) \to 1
$$

la suite exacte

$$
1 \to \mathrm{A} _ {\pm \alpha} (\bar {k}) \to \mathrm{J} _ {a} (\bar {\mathrm{F}} _ {\bar {v}}) / \mathrm{J} _ {a} (\bar {\mathcal {O}} _ {\bar {v}}) \to \mathrm{T} (\bar {\mathrm{F}} _ {v}) / \mathrm{T} (\bar {\mathcal {O}} _ {v}) \to 1.
$$

On a par ailleurs un isomorphisme

$$
\mathrm{T} (\bar {\mathrm{F}} _ {v}) / \mathrm{T} (\bar {\mathcal {O}} _ {v}) = \mathbf {X} _ {*} (\mathrm{T})
$$

qui se déduit de l'homomorphisme  $\mathbf{X}_{*}(\mathrm{T})\to\mathrm{T}(\bar{\mathrm{F}}_{v})$  défini par  $\lambda\mapsto\epsilon_{v}^{\lambda}$  d'où le corollaire.

Lemme 8.3.6. — Les $\bar{k}$-points de la fibre de Springer affine

$$
\mathcal {M} _ {\bar {v}} (a) (\bar {k}) = \{g \in \mathrm{G} (\bar {\mathrm{F}} _ {\bar {v}}) / \mathrm{G} (\bar {\mathcal {O}} _ {\bar {v}}) | \mathrm{ad} (g) ^ {- 1} (\gamma_ {0}) \in \mathfrak {g} (\bar {\mathcal {O}} _ {\bar {v}}) \}
$$

s'écrivent de façon unique sous la forme

$$
g = \epsilon_ {v} ^ {\lambda} \mathrm{U} _ {\alpha} (x \epsilon_ {v} ^ {- 1})
$$

avec $\lambda\in\mathbf{X}_{*}(\mathrm{T})$ et $x\in\bar{k}$.

Démonstration. — Avec la décomposition d'Iwasawa, pour tout élément $g \in \mathrm{G}(\bar{\mathrm{F}}_{\bar{v}})/\mathrm{G}(\bar{\mathcal{O}}_{\bar{v}})$, il existe un unique $\lambda \in \mathbf{X}_{*}(\mathrm{T})$ et un unique $u \in \mathrm{U}(\bar{\mathrm{F}}_{\bar{v}})/\mathrm{U}(\bar{\mathcal{O}}_{\bar{v}})$ tels que

$$
g = \epsilon_ {v} ^ {\lambda} u.
$$

Comme $\mathrm{T}_{\bar{v}}$ commute avec $\gamma_0$, le plongement

$$
\mathcal {M} _ {\bar {v}} (a) \to \mathcal {G} _ {\bar {v}} = \mathrm{G} (\bar {\mathrm{F}} _ {\bar {v}}) / \mathrm{G} (\bar {\mathcal {O}} _ {\bar {v}})
$$

est $\mathrm{T}_{\bar{v}}$-équivariant. L'action de $\mathrm{T}_{\bar{v}}$ sur $\mathcal{M}_v(a)$ se factorise par

$$
\mathrm{T} _ {\bar {v}} \rightarrow \mathrm{T} (\bar {\mathrm{F}} _ {\bar {v}}) \rightarrow \mathcal {P} _ {v} (\mathrm{J} _ {a}) = \mathrm{T} (\bar {\mathrm{F}} _ {\bar {v}}) / \mathrm{J} _ {a} (\bar {\mathcal {O}} _ {\bar {v}}).
$$

Elle se factorise donc par le tore de dimension un

$$
\mathrm{T} _ {\bar {v}} \rightarrow \mathrm{A} _ {\pm \alpha , \bar {v}}.
$$

Si on écrit  $g \in \mathcal{M}_{v}(a)(\bar{k})$  sous la forme  $g = \epsilon_{v}^{\lambda} u$ , u sera de la forme  $u = \mathrm{U}_{\alpha}(y)$  avec  $y \in \bar{F}_{\bar{v}} / \bar{\mathcal{O}}_{\bar{v}}$  uniquement déterminé. Un calcul dans  $SL_{2}$  cf. [26, lemme 6.2] montre alors qu'avec l'hypothèse  $r_{\pm\alpha}(a) = 1$ , y s'écrit uniquement sous la forme  $y = x \epsilon_{v}^{-1}$  avec  $x \in \bar{k}$  et inversement les éléments g de la forme  $g = \epsilon_{v}^{\lambda} \mathrm{U}_{\alpha}(x \epsilon_{v}^{-1})$  appartiennent à  $\mathcal{M}_{\bar{v}}(a)(\bar{k})$ .

Lemme 8.3.7. — Les points fixes du tore de dimension un $\mathrm{A}_{\pm \alpha, \bar{\nu}}$ dans $\mathcal{M}_{\bar{\nu}}$ sont $\epsilon_{v}^{\lambda}$. Pour $\lambda \in \mathbf{X}_{*}(\mathrm{T})$ fixé, $\mathrm{A}_{\pm \alpha, \bar{\nu}}$ agit simplement transitivement sur

$$
\mathrm{O} _ {\lambda} = \{\epsilon_ {v} ^ {\lambda} \mathrm{U} _ {\alpha} (x \epsilon_ {v} ^ {- 1}) \in \mathcal {M} _ {v} (a) (\bar {k}) | x \in \bar {k} ^ {\times} \}.
$$

De plus le bord de l'adhérence de cette orbite est constitué de  $\epsilon_{v}^{\lambda}$  et  $\epsilon_{v}^{\lambda-\alpha^{\vee}}$  où  $\alpha^{\vee}$  est la coracine associée à la racine  $\alpha$ .

Démonstration. — Un calcul direct montre que les $\epsilon_{v}^{\lambda}$ sont fixes sous l'action de $\mathrm{A}_{\pm \alpha, \bar{v}}$ et que $\mathrm{A}_{\pm \alpha, \bar{v}}$ agit simplement transitivement sur $\mathrm{O}_{\lambda}$. Ceci montre que l'ensemble des points fixes de $\mathrm{A}_{\pm \alpha, \bar{v}}$ est exactement $\{\epsilon_{v}^{\lambda} | \lambda \in \mathbf{X}_{*}(\mathrm{T})\}$. Quand $x \to 0$, $\epsilon_{v}^{\lambda} \mathrm{U}_{\alpha}(x \epsilon_{v}^{-1})$ tend vers $\epsilon_{v}^{\lambda}$ de sorte que $\epsilon_{v}^{\lambda}$ appartient à l'adhérence de $\mathrm{O}_{\lambda}$.

Il reste à démontrer que quand $x \to \infty$, $\epsilon_v^\lambda U_\alpha(x\epsilon_v^{-1})$ tend vers $\epsilon_v^{\lambda - \alpha^\vee}$. Il revient au même de démontrer que $U_\alpha(x\epsilon_v^{-1})$ tend vers $\epsilon_v^{-\alpha^\vee}$ quand $x \to \infty$. Il s'agit d'un calcul

bien connu dans la grassmannienne affine qui découle de la relation de Steinberg dans  $\mathrm{G}(\bar{\mathrm{F}}_{\bar{v}})$ cf. [76, chap. 3, lemme 19]

$$
\mathcal {Y} ^ {- \alpha^ {\vee}} w _ {\alpha} = \mathrm{U} _ {- \alpha} (\mathcal {Y}) \mathrm{U} _ {\alpha} (- \mathcal {Y} ^ {- 1}) \mathrm{U} _ {\alpha} (\mathcal {Y}).
$$

Celle-ci vaut pour tout  $y \in \bar{F}_{\bar{v}}$ , pour toute racine  $\alpha$  et pour un représentant  $w_{\alpha}$  de la réflexion  $s_{\alpha} \in W$  attachée à la racine  $\alpha$  qui appartient à  $\mathbf{G}(\bar{k})$ . En prenant  $y = -x^{-1}\epsilon_{v}$  avec  $x \in \bar{k}^{\times}$ , on obtient la relation suivante dans  $\mathbf{G}(\bar{\mathbf{F}}_{\bar{v}})/\mathbf{G}(\bar{\mathcal{O}}_{\bar{v}})$

$$
\mathrm{U} _ {\alpha} (x \epsilon_ {v} ^ {- 1}) = \epsilon_ {v} ^ {- \alpha^ {\vee}} \mathrm{U} _ {- \alpha} (- x ^ {- 1} \epsilon_ {v} ^ {- 1}).
$$

En faisant tendre $x$ vers $\infty$, on constate que $\mathrm{U}_{\alpha}(x\epsilon_{v}^{-1})$ tend vers $\epsilon_{v}^{-\alpha^{\vee}}$.

Proposition 8.3.8. — Soit $\kappa\in\hat{T}^{\sigma}$ un élément de torsion tel que

$$
\kappa (\alpha^ {\vee}) \neq 1.
$$

Alors, on a la formule

$$
[ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a}) ] (k) _ {\kappa} = \sharp \mathrm{A} _ {\pm \alpha} (k _ {v}) ^ {- 1} q ^ {\deg (v)}.
$$

Démonstration. — La fibre de Springer affine  $\mathcal{M}_{v}(a)$  s'obtient comme la restriction des scalaires  $k_{v}/k$  d'une fibre de Springer affine définie sur  $k_{v}$ . Il en est de même de  $\mathcal{P}_{v}(\mathrm{J}_{a})$  et du quotient  $[\mathcal{M}_{v}(a)/\mathcal{P}_{v}(\mathrm{J}_{a})]$ . On peut donc supposer que  $k_{v}=k$ .

Notons  $A = A_{\pm\alpha,v}$  : c'est un tore de dimension un sur k. Considérons le sous-groupe  $\sigma$ -invariant de  $\mathbf{X}_{*}(\mathrm{T})$  engendré par  $\alpha^{\vee}$  et considérons l'image réciproque de la suite exacte

$$
1 \to \mathrm{A} \to \mathcal {P} _ {v} (\mathrm{J} _ {a}) \to \mathbf {X} _ {*} (\mathrm{T}) \to 1
$$

par l'homomorphisme $\mathbf{Z}\alpha^{\vee} \to \mathbf{X}_{*}(\mathrm{T})$. C'est un groupe algébrique P défini sur $k$ muni d'une suite exacte

$$
1 \to \mathrm{A} \to \mathrm{P} \to \mathbf {Z} \alpha^ {\vee} \to 1
$$

et un homomorphisme injectif  $\mathrm{P}\to\mathcal{P}_{v}(\mathrm{J}_{a})$  qui induit l'identité sur la composante neutre A.

Dans la fibre de Springer affine $\mathcal{M}_{v}(a)$, on dispose d'un $k$-point $m$ donné par la section de Kostant. D'après la description ci-dessus de $\mathcal{M}_{v}(a) \otimes_{k} \bar{k}$, la composante connexe M de $\mathcal{M}_{v}(a) \otimes_{k} \bar{k}$ est une chaîne infinie de droites projectives munie d'une action de P $\otimes_{k} \bar{k}$ qui est simplement transitive sur la M$^{\text{reg}}$. Comme cette composante connexe contient le $k$-point $m$, elle est définie sur $k$. On retrouve $\mathcal{M}_{v}(\mathrm{J}_{a})$ à partir de M par l'induction de P à $\mathcal{P}_{v}(\mathrm{J}_{a})$

$$
\mathcal {M} _ {v} (a) = \mathrm{M} \wedge^ {\mathrm{P}} \mathcal {P} _ {v} (\mathrm{J} _ {a}).
$$

En particulier, on a une équivalence de catégories

$$
[ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a}) ] = [ \mathrm{M} / \mathrm{P} ].
$$

On se ramène donc à l'exercice de comptage de points déjà résolu dans l'exemple 8.1.15.

8.4. Comptage dans une fibre de Hitchin anisotrope. — Rappelons le comptage de points dans une fibre de Hitchin  $M_{a}$  avec  $a \in \mathcal{M}_{a}^{\mathrm{ani}}(k)$  en suivant le paragraphe 9 de [57]. Dans loc. cit., nous avons considéré le quotient de  $M_{a}$  par  $P_{a}$ . Il est en fait plus commode de considérer un quotient plus général.

8.4.1. — Soit  $J_{a}^{\prime}$  un X-schéma en groupes lisse commutatif de type fini muni d'un homomorphisme  $J_{a}^{\prime} \to J_{a}$  qui est un isomorphisme sur un ouvert non vide U de X. La donnée de  $J_{a}^{\prime}$  est équivalente à la donnée des sous-groupes ouverts compacts  $\mathrm{J}_{a}^{\prime}(\mathcal{O}_{v}) \subset \mathrm{J}_{a}(\mathcal{O}_{v})$  pour les points  $v \in |X - U|$ . Notons  $\mathcal{P}_{a}^{\prime} = \mathcal{P}(J_{a}^{\prime})$  le classifiant des  $J_{a}^{\prime}$ -torseurs sur X. On a alors un homomorphisme  $P_{a}^{\prime} \to P_{a}$  qui induit une action de  $P_{a}^{\prime}$  sur  $M_{a}$ . Pour  $J_{a}^{\prime}$  tel que le sous-groupe ouvert compact  $\mathrm{J}_{a}^{\prime}(\mathcal{O}_{v})$  soit assez petit,  $\mathrm{H}^{0}(\bar{\mathrm{X}}, J_{a}^{\prime})$  est trivial de sorte que  $P_{a}^{\prime}$  est représentable par un groupe algébrique localement de type fini sur k. Pour le comptage, il sera commode de supposer que les fibres de  $J_{a}^{\prime}$  sont toutes connexes. Considérons la catégorie quotient  $[M_{a}/P_{a}^{\prime}]$ .

Le comptage est fondé sur la formule de produit cf. 4.15.1 et [57, théorème 4.6].

Proposition 8.4.2. — Soit  $U = a^{-1}(\mathfrak{c}_{\mathrm{D}}^{\mathrm{rs}})$  l'image inverse du lieu semi-simple régulier de  $c_{D}$ . On a une équivalence de catégories

$$
[ \mathcal {M} _ {a} / \mathcal {P} _ {a} ^ {\prime} ] = \prod_ {v \in \mathrm{X-U}} [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ]
$$

compatible à l'action de $\sigma\in\mathrm{Gal}(\bar{k}/k)$. En particulier, on a une équivalence entre les catégories des $k$-points

$$
[ \mathcal {M} _ {a} / \mathcal {P} _ {a} ^ {\prime} ] (k) = \prod_ {v \in | \mathrm{X-U} |} [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k).
$$

Soit  $(\mathcal{P}_{a}^{\prime})^{0}$  la composante neutre de  $P_{a}^{\prime}$ . Puisque  $a \in \mathcal{A}^{\mathrm{ani}}(k)$ , le groupe des composantes connexes  $\pi_{0}(\mathcal{P}_{a})$  est un groupe fini muni d'une action de l'élément de Frobenius  $\sigma \in \operatorname{Gal}(\bar{k}/k)$ .

Proposition 8.4.3. — Supposons que les fibres de  $J_{a}^{\prime}$  sont connexes. Pour tout caractère  $\sigma$ -invariant de  $\pi_{0}(\mathcal{P}_{a})$

$$
\kappa : \pi_ {0} (\mathcal {P} _ {a}) _ {\sigma} \to \bar {\mathbf {Q}} _ {\ell} ^ {\times},
$$

on a

$$
\sharp [ \mathcal {M} _ {a} / \mathcal {P} _ {a} ^ {\prime} ] (k) _ {\kappa} = \prod_ {v \in | \mathrm{X-U} |} \sharp [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k) _ {\kappa}.
$$

Démonstration. — Pour tout point fermé v de X dans le complémentaire de l'ouvert  $U = a^{-a}(\mathfrak{c}_{\mathrm{D}}^{\mathrm{rs}})$ , l'homomorphisme composé

$$
\mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) \to \mathcal {P} _ {a} ^ {\prime} \to \pi_ {0} (\mathcal {P} _ {a} ^ {\prime})
$$

se factorise par $\pi_0(\mathcal{P}_v(J'_a))$. L'homomorphisme $\kappa : \pi_0(\mathcal{P}_a')_\sigma \to \bar{\mathbf{Q}}_\ell^\times$ définit donc un homomorphisme $\kappa : \pi_0(\mathcal{P}_v(J'_a))_\sigma \to \bar{\mathbf{Q}}_\ell^\times$.

Dans 8.4.2, si un point $y \in [\mathcal{M}_a / \mathcal{P}_a'](k)$ correspond à une collection de points $y_v \in [\mathcal{M}_v(a) / \mathcal{P}_v(J_a')](k)$ pour $v \in |\mathrm{X} - \mathrm{U}|$, alors on a la formule

$$
\langle \operatorname{cl} (y), \kappa \rangle = \prod_ {v \in | \mathrm{X-U} |} \langle \operatorname{cl} (y _ {v}), \kappa \rangle .
$$

Par conséquent, on a la factorisation

$$
\sharp [ \mathcal {M} _ {a} / \mathcal {P} _ {a} ^ {\prime} ] (k) _ {\kappa} = \prod_ {v \in | \mathrm{X-U} |} \sharp [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k) _ {\kappa}
$$

d'où la proposition.

La conjonction de cette proposition avec 8.1.6 implique le corollaire suivant.

Corollaire 8.4.4. — Pour tout caractère $\kappa : \pi_0(\mathcal{P}_a)_\sigma \to \bar{\mathbf{Q}}_\ell^\times$, on $a$

$$
\sum_ {n} (- 1) ^ {n} \operatorname{tr} (\sigma , \mathrm{H} ^ {n} (\mathcal {M} _ {a}) _ {\kappa}) = \sharp \left(\mathcal {P} _ {a} ^ {\prime}\right) ^ {0} (k) \prod_ {v \in [ \mathrm{X-U} ]} \sharp \left[ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} \left(\mathrm{J} _ {a} ^ {\prime}\right) \right] (k) _ {\kappa}
$$

où $\mathrm{H}^n (\mathcal{M}_a)_\kappa$ est le sous-espace propre de $\mathrm{H}^n (\mathcal{M}_a)$ où le groupe $\pi_0(\mathcal{P}_a)$ agit à travers le caractère $\kappa$.

8.4.5. — Pour exprimer les nombres $\sharp [\mathcal{M}_{v}(a)/\mathcal{P}_{v}(\mathrm{J}_{a}^{\prime})](k)_{\kappa}$ en termes d'intégrales orbitales locales, faisons les choix suivants :

\- en toute place $v \in |\mathbf{X} - \mathbf{U}|$, choisissons une trivialisation du fibré inversible $\mathrm{D}'|_{\mathrm{X}_v}$,

\- en toute place $v \in |\mathbf{X} - \mathbf{U}|$, choisissons une mesure de Haar $dt_v$ du tore $J_a(F_v)$.

Ces choix nous permettent :

\- d'identifier la restriction de $a$ à $\mathrm{X}_{v}$ avec un élément $a_{v} \in \mathfrak{c}(\mathcal{O}_{v}) \cap \mathfrak{c}^{\mathrm{rs}}(\mathrm{F}_{v})$,

\- d'identifier les schémas en groupes $J_a$ et $J_{a_v}$ ce qui munit $J_{a_v}(F_v)$ d'une mesure de Haar $dt_v$,

\- d'identifier la fibre de Springer affine $\mathcal{M}_{v}(a)$ munie de l'action de $\mathcal{P}_{v}(\mathrm{J}_{a})$ avec la fibre de Springer affine $\mathcal{M}_{v}(a_{v})$ munie de l'action de $\mathcal{P}_{v}(\mathrm{J}_{a_{v}})$.

Avec ces choix faits, on peut exprimer les nombres $\sharp[\mathcal{M}_{v}(a)/\mathcal{P}_{v}(\mathrm{J}_{a}^{\prime})](k)_{\kappa}$ en termes de $\kappa$-intégrales orbitales cf. 8.2.5

$$
\sharp [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k) _ {\kappa} = \operatorname{vol} (\mathrm{J} _ {a} ^ {\prime} (\mathcal {O} _ {v}), \mathrm{d} t _ {v}) \mathbf {O} _ {a _ {v}} ^ {\kappa} (1 _ {\mathfrak {g} _ {v}}, \mathrm{d} t _ {v}).
$$

On obtient alors la formule

$$
\sum_ {n} (- 1) ^ {n} \operatorname{tr} \left(\sigma , \mathrm{H} ^ {n} \left(\mathcal {M} _ {a}\right) _ {\kappa}\right) = \left(\mathcal {P} _ {a} ^ {\prime}\right) ^ {0} (k) \prod_ {v \in | \mathrm{X} - \mathrm{U} |} \operatorname{vol} \left(\mathrm{J} _ {a} ^ {\prime} \left(\mathcal {O} _ {v}\right), \mathrm{d} t _ {v}\right) \mathbf {O} _ {a _ {v}} ^ {\kappa} \left(1 _ {\mathfrak {g} _ {v}}, \mathrm{d} t _ {v}\right).
$$

8.5. Stabilisation sur $\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{ani}} - \tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{bad}}$. — On est en position de démontrer le théorème 6.4.2 sur l'ouvert $\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{good}} = \tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{ani}} - \tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{bad}}$. Nous nous mettons donc sous les hypothèses de 6.4.2. En particulier, on dispose d'une immersion fermée

$$
\tilde {\mathcal {A}} _ {\mathrm{H}} ^ {\mathrm{ani}} \to \tilde {\mathcal {A}} ^ {\mathrm{ani}}
$$

définie sur $k$. Comme dans 7.8.2, on a un sous-schéma fermé $\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{bad}}$ de $\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{ani}}$.

Démonstration. — D'après le théorème du support 7.8.5, sur $\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{good}}$, les faisceaux pervers purs

$$
\mathrm{K} _ {\kappa} ^ {n} = \tilde {\nu} ^ {* p} \mathrm{H} ^ {n} (\tilde {f} _ {*} ^ {\mathrm{ani}} \bar {\mathbf {Q}} _ {\ell}) _ {\kappa} \quad \text {et} \quad \mathrm{K} _ {\mathrm{H}, \mathrm{st}} ^ {n} = ^ {p} \mathrm{H} ^ {n + 2 r _ {\mathrm{H}} ^ {\mathrm{G}} (\mathrm{D})} (\tilde {f} _ {\mathrm{H}, *} ^ {\mathrm{ani}} \bar {\mathbf {Q}} _ {\ell}) _ {\mathrm{st}} (- r _ {\mathrm{H}} ^ {\mathrm{G}} (\mathrm{D}))
$$

sont le prolongement intermédiaire de leurs restrictions à n'importe quel ouvert non-vide $\tilde{\mathcal{U}}$ de $\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{good}}$. Pour démontrer que $\mathrm{K}^{n}$ et $\mathrm{K}_{\mathrm{H}}^{n}$ sont isomorphes sur $\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{good}} \otimes_{k} \bar{k}$ et sont isomorphes après semi-simplification sur $\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{good}}$, il suffit de le faire sur n'importe quel ouvert dense $\tilde{\mathcal{U}}$ de $\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{good}}$. On va construire un bon ouvert $\tilde{\mathcal{U}}$ comme suit.

Rappelons qu'on a une égalité de diviseurs cf. 1.10.3

$$
\nu^ {*} \mathfrak {D} _ {\mathrm{G,D}} = \mathfrak {D} _ {\mathrm{H,D}} + 2 \mathfrak {R} _ {\mathrm{H,D}} ^ {\mathrm{G}}
$$

sur $\mathfrak{c}_{\mathrm{H,D}}$. De plus, on sait que $\mathfrak{D}_{\mathrm{H,D}}$ et $\mathfrak{R}_{\mathrm{H,D}}^{\mathrm{G}}$ sont des diviseurs réduits de $\mathfrak{c}_{\mathrm{H,D}}$ étrangers de sorte que la réunion

$$
\mathfrak {D} _ {\mathrm{H,D}} + \mathfrak {R} _ {\mathrm{H,D}} ^ {\mathrm{G}}
$$

est aussi un diviseur réduit.

Lemme 8.5.1. — Supposons que $\deg(\mathrm{D}) > 2g$. Alors, l'ensemble des $a_{\mathrm{H}} \in \mathcal{A}_{\mathrm{H}}(\bar{k})$ tel que $a_{\mathrm{H}}(\bar{\mathbf{X}})$ coupe transversalement $\mathfrak{D}_{\mathrm{H},\mathrm{D}} + \mathfrak{R}_{\mathrm{H},\mathrm{D}}^{\mathrm{G}}$ forme un ouvert non vide $\mathcal{U}$ de $\mathcal{A}_{\mathrm{H}}$.

Démonstration. — La démonstration est identique à la démonstration de 4.7.1. □

8.5.2. — Considérons l'image réciproque  $\tilde{U}$  de U dans  $\tilde{A}$ . En rapetissant cet ouvert si nécessaire, on peut supposer que  $\tilde{U} \subset \tilde{A}^{good}$ . En le rapetissant encore si nécessaire, on peut supposer que pour tout  $n \in Z$ , les restrictions

$$
\mathrm{L} _ {\kappa} ^ {n} = \mathrm{K} _ {\kappa} ^ {n} | _ {\tilde {\mathcal {U}}} \quad \mathrm{et} \quad \mathrm{L} _ {\mathrm{H,st}} ^ {n} = \mathrm{K} _ {\mathrm{H,st}} ^ {n} | _ {\tilde {\mathcal {U}}}
$$

sont des systèmes locaux purs de poids n sur  $\tilde{U}$ .

8.5.3. — Il suffit en fait de démontrer que pour toute extension finie  $k'$  de k, pour tout  $k'$ -point  $\tilde{a}_{\mathrm{H}} \in \tilde{\mathcal{U}}(k')$  d'image  $\tilde{a} \in \tilde{\mathcal{A}}(k')$ , on a l'égalité des traces

$$
\sum_ {n} (- 1) ^ {n} \mathrm{tr} (\sigma_ {k ^ {\prime}}, (\mathrm{L} _ {\kappa} ^ {n}) _ {\tilde {a}}) = \sum_ {n} (- 1) ^ {n} \mathrm{tr} (\sigma_ {k ^ {\prime}}, (\mathrm{L} _ {\mathrm{H,st}} ^ {n}) _ {\tilde {a} _ {\mathrm{H}}}).\tag{8.5.4}
$$

En effet, on a alors l'égalité

$$
\sum_ {n} (- 1) ^ {n} \mathrm{tr} (\sigma_ {k ^ {\prime}} ^ {j}, (\mathrm{L} _ {\kappa} ^ {n}) _ {\tilde {a}}) = \sum_ {n} (- 1) ^ {n} \mathrm{tr} (\sigma_ {k ^ {\prime}} ^ {j}, (\mathrm{L} _ {\mathrm{H,st}} ^ {n}) _ {\tilde {a} _ {\mathrm{H}}})
$$

pour tout entier naturel $j$ en considérant $\tilde{a}_{\mathrm{H}}$ comme un point à valeurs dans l'extension de degré $j$ de $k'$. De plus, comme les valeurs propres de $\sigma_{k'}$ dans $(\mathrm{L}_k^n)_{\tilde{a}}$ et $(\mathrm{L}_{\mathrm{H},\mathrm{st}}^n)_{\tilde{a}_{\mathrm{H}}}$ sont toutes de valeur absolue $q^{n\deg (k'/k)/2}$, ces égalités impliquent que pour toute extension finie $k'$ de $k$, pour tout $\tilde{a}_{\mathrm{H}} \in \tilde{\mathcal{U}}(k')$ d'image $\tilde{a} \in \tilde{\mathcal{A}}$ et pour tout $n$, on a

$$
\mathrm{tr} (\sigma_ {k ^ {\prime}}, (\mathrm{L} _ {\kappa} ^ {n}) _ {\tilde {a}}) = \mathrm{tr} (\sigma_ {k ^ {\prime}}, (\mathrm{L} _ {\mathrm{H,st}} ^ {n}) _ {\tilde {a} _ {\mathrm{H}}}).
$$

D'après le théorème de Chebotarev, ceci implique que  $L_{\kappa}^{n}$  et  $L_{H,st}^{n}$  sont isomorphes après la semi-simplification.

8.5.5. — Démontrons maintenant la formule (8.5.4). Pour tout point $\tilde{a}_{\mathrm{H}} \in \tilde{\mathcal{U}}(k')$, on peut calculer directement les deux membres de cette formule et ensuite les comparer. En remplaçant $k$ par $k'$ et X par $\mathrm{X} \otimes_k k'$, on peut supposer que $\tilde{a}_{\mathrm{H}}$ est un $k$-point de $\tilde{\mathcal{U}}$.

8.5.6. — Soit  $a_{\mathrm{H}} \in \mathcal{A}_{\mathrm{H}}(k)$  l'image de  $\tilde{a}_{H}$ . Soit a l'image de  $a_{H}$  dans  $\mathcal{A}(k)$ . D'après 2.5.1, on a un homomorphisme canonique

$$
\mathrm{J} _ {a} \rightarrow \mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}}}
$$

qui est un isomorphisme au-dessus de l'ouvert  $U = a^{-1}(\mathfrak{c}_{\mathrm{D}}^{\mathrm{rs}})$ . Choisissons un schéma en groupes  $J_{a}^{\prime}$  lisse commutatif de fibres connexes muni d'un homomorphisme  $J_{a}^{\prime} \to J_{a}$  qui est génériquement un isomorphisme. Soit  $P_{a}^{\prime}$  le champ classifiant des  $J_{a}^{\prime}$ -torseurs sur X. En rapetissant  $J_{a}^{\prime}$  si nécessaire, on peut supposer  $H^{0}(\bar{X}, J_{a}^{\prime})$  trivial dans quel cas  $P_{a}^{\prime}$  est

un groupe algébrique de type fini. On a des homomorphismes naturels $\mathcal{P}_{a}^{\prime}\to\mathcal{P}_{a}$ et $\mathcal{P}_{a}^{\prime}\to\mathcal{P}_{\mathrm{H},a_{\mathrm{H}}}$ qui induisent une action de $\mathcal{P}_{a}^{\prime}$ sur $\mathcal{M}_{a}$ et $\mathcal{M}_{\mathrm{H},a_{\mathrm{H}}}$. On peut calculer les deux membres dans la formule (8.5.4) en considérant les quotients $[\mathcal{M}_{a}/\mathcal{P}_{a}^{\prime}]$ et $[\mathcal{M}_{\mathrm{H},a_{\mathrm{H}}}/\mathcal{P}_{a}^{\prime}]$. D'après 8.4.4, le membre de gauche de (8.5.4) vaut

$$
\left(\mathcal {P} _ {a} ^ {\prime}\right) ^ {0} (k) \prod_ {v \in | \mathrm{X-U} |} \sharp \left[ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) \right] (k) _ {\kappa}
$$

alors que le membre de droite vaut

$$
q _ {\mathrm{H}} ^ {\mathrm{G} (\mathrm{D})} (\mathcal {P} _ {a} ^ {\prime}) ^ {0} (k) \prod_ {v \in | \mathrm{X-U} |} \sharp [ \mathcal {M} _ {\mathrm{H}, v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k).
$$

Comme

$$
r _ {\mathrm{H}} ^ {\mathrm{G}} (\mathrm{D}) = \sum_ {v} \deg (v) r _ {\mathrm{H}, v} ^ {\mathrm{G}} (a _ {\mathrm{H}})
$$

où  $r_{\mathrm{H},v}^{\mathrm{G}}(a_{\mathrm{H}})$  est le degré du diviseur  $a_{H}^{*}\Re_{H,D}^{G}$  en v, il suffit de démontrer l'énoncé suivant qui est un cas particulièrement simple du lemme fondamental de Langlands-Shelstad 1.11.1. Notons que ce cas particulier du lemme fondamental est essentiellement contenu dans l'article [48] de Labesse et Langlands sur SL(2) et a été repris d'un point de vue plus géométrique dans [26] par Goresky, Kottwitz et MacPherson. □

Lemme 8.5.7. — Soit $\tilde{a}_{\mathrm{H}} \in \tilde{\mathcal{A}}_{\mathrm{H}}(k)$. Soit $v$ un point fermé de X au-dessus duquel $a_{\mathrm{H}}(\bar{\mathbf{X}}_v)$ ne coupe pas ou coupe transversalement le diviseur $\mathfrak{D}_{\mathrm{H},\mathrm{D}} + \mathfrak{R}_{\mathrm{H},\mathrm{D}}^{\mathrm{G}}$. On a l'égalité

$$
\sharp [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k) _ {\kappa} = q ^ {\deg (v) r _ {\mathrm{H}, v} ^ {\mathrm{G}} (a _ {\mathrm{H}})} \sharp [ \mathcal {M} _ {\mathrm{H}, v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k).
$$

De plus, c'est un nombre rationnel non nul.

Démonstration. — Soit $\bar{v}$ un point géométrique au-dessus de $v$. Comme $a_{\mathrm{H}}(\bar{\mathbf{X}}_v)$ coupe transversalement $\mathfrak{D}_{\mathrm{H},\mathrm{D}} + \mathfrak{R}_{\mathrm{H},\mathrm{D}}^{\mathrm{G}}$, il y a trois possibilités pour les entiers $d_{\mathrm{H},\bar{v}}(a_{\mathrm{H}})$, $d_{\bar{v}}(a)$ et $r_{\mathrm{H},v}^{\mathrm{G}}(a_{\mathrm{H}})$:

(1) si $a_{\mathrm{H}}(\bar{v}) \notin \mathfrak{D}_{\mathrm{H,D}} \cup \mathfrak{R}_{\mathrm{H,D}}^{\mathrm{G}}$, alors

$$
d _ {\mathrm{H}, \bar {v}} (a _ {\mathrm{H}}) = 0, \qquad d _ {\bar {v}} (a) = 0 \quad \mathrm{et} \quad r _ {\mathrm{H}, v} ^ {\mathrm{G}} (a _ {\mathrm{H}}) = 0,
$$

(2) si $a_{\mathrm{H}}(\bar{v}) \in \mathfrak{D}_{\mathrm{H,D}}$ alors $a_{\mathrm{H}}(\bar{v}) \notin \mathfrak{R}_{\mathrm{H,D}}^{\mathrm{G}}$ et on a

$$
d _ {\mathrm{H}, \bar {v}} (a _ {\mathrm{H}}) = 1, \qquad d _ {\bar {v}} (a) = 1 \quad \mathrm{et} \quad r _ {\mathrm{H}, v} ^ {\mathrm{G}} (a _ {\mathrm{H}}) = 0,
$$

(3) si $a_{\mathrm{H}}(\bar{v}) \in \mathfrak{R}_{\mathrm{H,D}}^{\mathrm{G}}$ alors $a_{\mathrm{H}}(\bar{v}) \notin \mathfrak{D}_{\mathrm{H,D}}$ et on a

$$
d _ {\mathrm{H}, \bar {v}} (a _ {\mathrm{H}}) = 0, \qquad d _ {\bar {v}} (a) = 2 \quad \mathrm{et} \quad r _ {\mathrm{H}, v} ^ {\mathrm{G}} (a _ {\mathrm{H}}) = 1.
$$

8.5.8. — Dans les deux premiers cas, la formule de Bezrukavnikov 3.7.5 montre que $\delta_{\mathrm{H},\bar{v}}(a_{\mathrm{H}})=\delta_{\bar{v}}(a)=0$ de sorte que les fibres de Springer affines $\mathcal{M}_{\mathrm{H},v}(a_{\mathrm{H}})$ et $\mathcal{M}_{v}(a)$ sont toutes les deux de dimension zéro. Il s'ensuit que $\mathcal{P}_{v}(\mathrm{J}_{a})$ agit simplement transitivement sur $\mathcal{M}_{v}(a)$ et $\mathcal{P}_{v}(\mathrm{J}_{\mathrm{H},a_{\mathrm{H}}})$ agit simplement transitivement sur $\mathcal{M}_{\mathrm{H},v}(a_{\mathrm{H}})$ cf. 3.7.2. Choissons une trivialisation de D' au-dessus de $\mathrm{X}_{v}$ comme dans 8.4.5 pour pouvoir écrire agréablement les intégrales orbitales. En particulier $a_{\mathrm{H}}$ et $a$ définissent des éléments $a_{\mathrm{H},v}\in\mathfrak{c}_{\mathrm{H}}(\mathcal{O}_{v})$ et $a_{v}\in\mathfrak{c}(\mathcal{O}_{v})$. En conjonction avec 8.2.7, on en déduit la formule

$$
1 = [ \mathcal {M} _ {\mathrm{H}, v} (a _ {\mathrm{H}}) / \mathcal {P} _ {v} (\mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}}}) ] (k) = \mathrm{vol} (\mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}}} ^ {0} (\mathcal {O} _ {v}), \mathrm{d} t _ {v}) \mathbf {S O} _ {a _ {\mathrm{H}, v}} (1 _ {\mathfrak {h} _ {v}}, \mathrm{d} t _ {v}).
$$

En comparant avec la formule 8.2.5

$$
\sharp \left[ \mathcal {M} _ {\mathrm{H}, v} (a) / \mathcal {P} _ {v} \left(\mathrm{J} _ {a} ^ {\prime}\right) \right] (k) = \operatorname{vol} \left(\mathrm{J} _ {a} ^ {\prime} \left(\mathcal {O} _ {v}\right), \mathrm{d} t _ {v}\right) \mathbf {S O} _ {a _ {\mathrm{H}, v}} \left(1 _ {\mathfrak {h} _ {v}}, \mathrm{d} t _ {v}\right)
$$

on obtient

$$
\sharp [ \mathcal {M} _ {\mathrm{H}, v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k) = \frac {\mathrm{vol} (\mathrm{J} _ {a} ^ {\prime} (\mathcal {O} _ {v}) , \mathrm{d} t _ {v})}{\mathrm{vol} (\mathrm{J} _ {\mathrm{H} , a _ {\mathrm{H}}} ^ {0} (\mathcal {O} _ {v}) , \mathrm{d} t _ {v})}.
$$

En remarquant que  $\mathcal{M}_{v}(a)$  est muni d'un k-point grâce à la section de Kostant, on a aussi

$$
\sharp [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a}) ] (k) _ {\kappa} = 1.
$$

Le même raisonnement comme ci-dessus implique alors

$$
\sharp [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k) _ {\kappa} = \frac {\operatorname{vol} (\mathrm{J} _ {a} ^ {\prime} (\mathcal {O} _ {v}) , \mathrm{d} t _ {v})}{\operatorname{vol} (\mathrm{J} _ {a} ^ {0} (\mathcal {O} _ {v}) , \mathrm{d} t _ {v})}.
$$

Il reste à remarquer que dans les deux premiers cas, l'homomorphisme  $J_{a} \rightarrow J_{H,a_{H}}$  induit un isomorphisme sur les composantes neutres  $J_{a}^{0} \rightarrow J_{H,a_{H}}^{0}$  et on obtient l'égalité

$$
\sharp [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k) _ {\kappa} = \sharp [ \mathcal {M} _ {\mathrm{H}, v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k)
$$

qu'on voulait.

8.5.9. — Considérons maintenant le troisième cas où  $a_{\mathrm{H}}(\mathrm{X}_{v})$  coupe transversalement  $R_{H,D}^{G}$  et n'intersecte pas  $D_{H,D}$ . On a dans ce cas  $d_{\mathrm{H},\bar{v}}(a_{\mathrm{H}})$  nul de sorte que

$$
\delta_ {\mathrm{H}, \bar {v}} (a _ {\mathrm{H}}) = 0 \quad \mathrm{et} \quad c _ {\mathrm{H}, \bar {v}} (a _ {\mathrm{H}}) = 0.
$$

Comme $\delta_{\mathrm{H},\bar{v}}(a_{\mathrm{H}})=0$, la fibre de Springer affine $\mathcal{M}_{\mathrm{H},v}(a_{\mathrm{H}})$ est de dimension zéro. D'après 3.7.2, $\mathcal{P}_{v}(\mathrm{J}_{\mathrm{H},a_{\mathrm{H}}})$ agit simplement transitivement sur $\mathcal{M}_{\mathrm{H},v}(a_{\mathrm{H}})$ de sorte qu'on a encore

$$
\sharp [ \mathcal {M} _ {\mathrm{H}, v} (a _ {\mathrm{H}}) / \mathcal {P} _ {v} (\mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}}}) ] (k) = 1.
$$

Le même raisonnement comme ci-dessus montre que

$$
\sharp [ \mathcal {M} _ {\mathrm{H}, v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k) = \frac {\operatorname{vol} (\mathrm{J} _ {a} ^ {\prime} (\mathcal {O} _ {v}) , \mathrm{d} t _ {v})}{\operatorname{vol} (\mathrm{J} _ {\mathrm{H} , a _ {\mathrm{H}}} ^ {0} (\mathcal {O} _ {v}) , \mathrm{d} t _ {v})}.
$$

Notons que comme $a_{\mathrm{H}}(\mathbf{X}_{v})$ n'intersecte pas $\mathfrak{c}_{\mathrm{H},\mathrm{D}},\mathrm{J}_{\mathrm{H},a_{\mathrm{H}}}$ est un tore et en particulier $\mathrm{J}_{\mathrm{H},a_{\mathrm{H}}} = \mathrm{J}_{\mathrm{H},a_{\mathrm{H}}}^{0}$.

Comme l'invariant  $c_{\bar{v}}(a)$  ne dépend que de la fibre générique de  $J_{a}|_{X_{v}}$ , on a

$$
c _ {\bar {v}} (a) = c _ {\mathrm{H}, \bar {v}} (a _ {\mathrm{H}}) = 0.
$$

Ceci implique que la fibre de Springer affine  $\mathcal{M}_{\bar{v}}(a)$  est de dimension

$$
\delta_ {\bar {v}} (a) = \frac {d _ {\bar {v}} (a) - c _ {\bar {v}} (a)}{2} = 1.
$$

On est donc exactement dans la situation de 8.3. En appliquant la formule 8.3.8 tout en notant que l'hypothèse $\kappa (\alpha^{\vee})\neq 1$ est bien vérifiée ici, on obtient la formule

$$
[ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a}) ] (k) _ {\kappa} = \sharp \mathrm{A} _ {\pm \alpha} (k _ {v}) q ^ {\deg (v)}
$$

où  $A_{\pm\alpha}$  est le tore de dimension un sur  $k_{v}$  défini par

$$
\mathrm{A} _ {\pm \alpha} (\bar {k}) = \mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}}} (\mathcal {O} _ {\bar {v}}) / \mathrm{J} _ {a} (\mathcal {O} _ {\bar {v}}).
$$

En appliquant la formule 8.2.7, on trouve

$$
\mathbf {O} _ {a} ^ {\kappa} (1 _ {\mathfrak {g} _ {v}}, \mathrm{d} t _ {v}) = \frac {q ^ {\deg (v)}}{\sharp \mathrm{A} _ {\pm \alpha} (k _ {v}) \operatorname{vol} (\mathrm{J} _ {a} ^ {0} (\mathcal {O} _ {v}) , \mathrm{d} t _ {v})}.
$$

On peut aussi vérifier la formule

$$
\sharp \mathrm{A} _ {\pm \alpha} (k _ {v}) \operatorname{vol} (\mathrm{J} _ {a} ^ {0} (\mathcal {O} _ {v}), \mathrm{d} t _ {v}) = \operatorname{vol} (\mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}}} ^ {0} (\mathcal {O} _ {v}), \mathrm{d} t _ {v})
$$

qui implique

$$
[ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k) _ {\kappa} = \frac {q ^ {\deg (v)} \operatorname{vol} (\mathrm{J} _ {a} ^ {\prime} (\mathcal {O} _ {v} , \mathrm{d} t _ {v}))}{\operatorname{vol} (\mathrm{J} _ {\mathrm{H} , a _ {\mathrm{H}}} ^ {0} (\mathcal {O} _ {v}) , \mathrm{d} t _ {v})}.
$$

On obtient donc l'égalité

$$
\sharp [ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k) _ {\kappa} = q ^ {\deg (v)} \sharp [ \mathcal {M} _ {\mathrm{H}, v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k)
$$

qu'on voulait.

Ceci termine la démonstration de 8.5.7.

8.6. Le lemme fondamental de Langlands-Shelstad. — On est maintenant en mesure de démontrer le lemme fondamental de Langlands et Shelstad 1.11.1.

Démonstration. — Soient  $X_{v} = \text{Spec}(\mathcal{O}_{v})$  avec  $\mathcal{O}_{v} = k[[\epsilon_{v}]]$  et  $X_{v}^{\bullet} = \text{Spec}(F_{v})$  avec  $F_{v} = k((\epsilon_{v}))$ . Soit  $G_{v}$  un groupe réductif sur  $X_{v}$  qui est la forme quasi-déployée de G donnée par un  $\text{Out}(\mathbf{G})$ -torseur  $\rho_{G,v}$  sur  $X_{v}$ . Soit  $(\kappa, \rho_{\kappa,v})$  une donnée endoscopique elliptique cf. 1.8. Soit  $H_{v}$  le groupe endoscopique associé. Soit  $a_{H} \in \mathfrak{c}_{H}(\mathcal{O}_{v})$  d'image  $a \in \mathfrak{c}(\mathcal{O}_{v}) \cap \mathfrak{c}^{\text{rs}}(F_{v})$ .

8.6.1. — Si le centre de  $G_{v}$  contient un tore déployé C, C est aussi contenu dans le centre de  $H_{v}$ . En remplaçant  $G_{v}$  par  $G_{v}/C$  et  $H_{v}$  par  $H_{v}/C$ , la  $\kappa$ -intégrale orbitale et l'intégrale orbitale stable envisagées ne changent pas de sorte qu'on peut supposer que le centre de  $G_{v}$  ne contient pas de tore déployé.

Si le centre de  $H_{v}$  contient un tore déployé C, C est naturellement inclus dans le tore  $I_{\gamma_{0}}$  où  $\gamma_{0} = \epsilon(a)$ . Le centralisateur  $M_{v}$  de C dans  $G_{v}$  est un sous-groupe de Levi de  $G_{v}$ . Par la formule de descente, on peut remplacer la  $\kappa$ -intégrale orbitale dans  $G_{v}$  par une  $\kappa$ -intégrale orbitale dans  $M_{v}$ . Le centre de  $M_{v}$  contient maintenant un tore déployé et on se ramène à la situation discutée ci-dessus. Après un nombre fini de ces réductions, on peut supposer que les centres de  $G_{v}$  et  $H_{v}$  ne contiennent pas de tores déployés.

8.6.2. — Soit  $\mathcal{M}_{\mathrm{H},v}(a_{\mathrm{H}})$  et  $\mathcal{M}_{v}(a)$  les fibres de Springer affines associées. D'après 3.5, il existe un entier naturel N tel que pour toute extension finie  $k'$  de k, pour tout  $a_{H}' \in \mathfrak{c}_{\mathrm{H}}(\mathcal{O}_{v} \otimes_{k} k')$  tel que

$$
a _ {\mathrm{H}} \equiv a _ {\mathrm{H}} ^ {\prime} \mod \epsilon_ {v} ^ {\mathrm{N}}
$$

alors

$$
a _ {\mathrm{H}} ^ {\prime}
$$

$$
a ^ {\prime} \in \mathfrak {c} (\mathcal {O} _ {v} \otimes_ {k} k ^ {\prime}) \cap \mathfrak {c} ^ {\mathrm{rs}} (\mathrm{F} _ {v} \otimes_ {k} k ^ {\prime})
$$

\- les fibres de Springer affines $\mathcal{M}_{\mathrm{H},v}(a_{\mathrm{H}})\otimes_{k}k^{\prime}$ et $\mathcal{M}_{\mathrm{H},v}(a_{\mathrm{H}}^{\prime})$ munies de l'action de $\mathcal{P}_v(\mathrm{J}_{\mathrm{H},a_{\mathrm{H}}})\otimes_k k'$ et $\mathcal{P}_v(\mathrm{J}_{\mathrm{H},a_{\mathrm{H}}'})$ respectivement, sont isomorphes;

\- les fibres de Springer affines $\mathcal{M}_{v}(a) \otimes_{k} k'$ et $\mathcal{M}_{v}(a')$ munies de l'action de $\mathcal{P}_{v}(\mathrm{J}_{a})$ et $\mathcal{P}_{v}(\mathrm{J}_{a'})$ respectivement, sont isomorphes.

Notons $\delta_{\mathrm{H}}(a_{\mathrm{H}})$ la dimension de la fibre de Springer affine $\mathcal{M}_{\mathrm{H},v}(a_{\mathrm{H}})$.

8.6.3. — Il existe une courbe projective lisse géométriquement connexe X sur k muni des données suivantes :

\- deux $k$-points distincts notés $\nu$ et $\infty$,

\- un isomorphisme entre la complétion de X en $v$ avec le schéma $\mathbf{X}_v$ ci-dessus,

\- un $\pi_0(\kappa)$-torseur $\rho_{\kappa}$ sur X muni d'une trivialisation $\alpha_{\infty}$ au-dessus de $\infty$ et d'un isomorphisme $\alpha_v$ avec $\rho_{\kappa,v}$ au-dessus de $\mathbf{X}_v$.

Soient G et H les X-schémas en groupes associés comme dans 1.8. Avec la donnée de $\alpha_{v}$, les restrictions de G et H à $\mathrm{X}_{v}$ sont canoniquement isomorphes à $\mathrm{G}_{v}$ et $\mathrm{H}_{v}$. Les centres de $\mathrm{G}_{v}$ et $\mathrm{H}_{v}$ ne contenant pas de tores déployés, il en est de même de G et H. Avec la donnée de $\alpha_{\infty}$, on a un homomorphisme

$$
\rho_ {\kappa} ^ {\bullet}: \pi_ {1} (\mathrm{X}, \infty) = \pi_ {1} (\overline {{\mathrm{X}}}, \infty) \rtimes \operatorname{Gal} (\bar {k} / k) \rightarrow \pi_ {0} (\kappa)
$$

trivial sur le facteur  $\operatorname{Gal}(\bar{k}/k)$ . Par conséquent, le sous-groupe  $\pi_{1}(\overline{\mathbf{X}},\infty)$  a la même image dans  $\pi_{0}(\kappa)$  que  $\pi_{1}(\mathbf{X},\infty)$ . Il s'ensuit que sur  $\overline{X}$ , les centres de G et H ne contiennent pas de tores déployés.

8.6.4. — On choisit maintenant un fibré inversible D sur X vérifiant les hypothèses suivantes

\- il existe un fibré inversible D' sur X avec D = D'⊗2,

\- une section globale de $\mathbf{D}'$ non nulle en $v$,

\- $\deg(\mathrm{D}) > r\mathrm{N} + 2g$ où $r$ est le rang de G et $g$ est le genre de X,

\- $\delta_{\mathrm{H}}(a_{\mathrm{H}})$ est plus petit que l'entier $\delta_{\mathrm{H}}^{\mathrm{bad}}(\mathrm{D})$ défini dans 7.8.2.

D'après 5.7.2, l'entier $\delta_{\mathrm{H}}^{\mathrm{bad}}$ tend vers $\infty$ lorsque $\deg(\mathrm{D}) \to \infty$ de sorte que pour $\deg(\mathrm{D})$ assez grand la dernière hypothèse est réalisée.

8.6.5. — Considérons les fibrations de Hitchin associées à la courbe X, au fibré inversible D et aux groupes G et H respectivement

$$
f \colon \mathcal {M} \to \mathcal {A} \quad \text { et } \quad f _ {\mathrm{H}} \colon \mathcal {M} _ {\mathrm{H}} \to \mathcal {A} _ {\mathrm{H}}.
$$

L'hypothèse que le centre de G et de H ne contient pas de tores déployés sur  $\overline{X}$  et l'hypothèse deg(D) > 2g assurent que les ouverts anisotropes  $A^{ani}$  et  $A_{H}^{ani}$  ne sont pas vides.

8.6.6. — Avec l'hypothèse deg(D) > rN + 2g, l'application de restriction des sections globales à Spec( $O_{v}/\epsilon_{v}^{N}$ )

$$
\mathrm{H} ^ {0} (\mathrm{X}, \mathfrak {c} _ {\mathrm{H,D}}) \rightarrow \mathfrak {c} _ {\mathrm{H}} (\mathcal {O} _ {v} / \epsilon_ {v} ^ {\mathrm{N}})
$$

est une application linéaire surjective. Soit Z le sous-espace affine de  $\mathrm{H}^{0}(\mathrm{X},\mathfrak{c}_{\mathrm{H},\mathrm{D}})$  des éléments ayant la même image dans  $\mathfrak{c}_{\mathrm{H}}(\mathcal{O}_{v}/\epsilon_{v}^{\mathrm{N}})$  que  $a_{H}$ . C'est un sous-schéma fermé de codimension rN de  $A_{H}$ . Par le même raisonnement que dans 4.7.1, on peut montrer que l'ouvert  $Z'$  de Z constitué des points  $a_{\mathrm{H}}^{\prime}\in\mathrm{Z}^{\prime}(\bar{k})$  tels que la courbe  $a_{\mathrm{H}}^{\prime}(\bar{\mathrm{X}}-\{v\})$  coupe le diviseur  $D_{H,D}+R_{H,D}^{G}$  transversalement, est un ouvert non vide. Comme le complément de  $A_{H}^{ani}$  dans  $A_{H}$  est un fermé de codimension plus grande ou égale à deg(D) cf. 6.3.5,  $Z^{\prime}\cap A_{H}^{ani}\neq\emptyset$ . En remplaçant  $Z^{\prime}$  par  $Z^{\prime}\cap A_{H}^{ani}$ , on peut supposer que  $Z^{\prime}\subset A_{H}^{ani}$ . Pour tout  $a_{\mathrm{H}}^{\prime}\in\mathrm{Z}^{\prime}(\bar{k})$ , l'invariant  $\delta_{\mathrm{H}}(a^{\prime})=\delta_{\mathrm{H}}(a_{\mathrm{H}})$  de sorte qu'on a  $Z^{\prime}\subset A_{H}^{good}$  où on dispose du théorème de stabilisation cf. 8.5.

Soit $\tilde{Z}'$ l'image réciproque de $Z'$ dans $\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{good}}$. Comme $\tilde{Z}'$ est un schéma de dimension positive, il existe un entier $m$ tel que pour toute extension $k'/k$ de degré plus grand ou égal à $m$, l'ensemble $\tilde{Z}'(k') \neq \emptyset$. Soit $\tilde{a}_{\mathrm{H}}' \in Z'(k')$ au-dessus de $a_{\mathrm{H}}' \in Z(k')$. Soient $\tilde{a}'$ l'image de $\tilde{a}_{\mathrm{H}}'$ dans $\tilde{\mathcal{A}}$ et $a'$ l'image de $a_{\mathrm{H}}'$ dans $\mathcal{A}$.

8.6.7. — La conjonction de la portion du théorème de stabilisation 6.4.2 démontrée sur l'ouvert $\tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{good}}$ et de la formule 8.4.4 nous fournit l'égalité

$$
\begin{array}{r l} & {\sharp (\mathcal {P} _ {a ^ {\prime}} ^ {\prime}) ^ {0} (k ^ {\prime}) \prod_ {v ^ {\prime} \in | (\mathrm{X-U}) \otimes_ {k} k ^ {\prime} |} \sharp [ \mathcal {M} _ {\mathrm{H}, v ^ {\prime}} (a _ {\mathrm{H}} ^ {\prime}) / \mathcal {P} _ {v ^ {\prime}} (\mathrm{J} _ {a ^ {\prime}} ^ {\prime}) ] (k ^ {\prime}) _ {\kappa}} \\ & {\qquad = q ^ {(a _ {\mathrm{H}} ^ {\prime}) \deg (k ^ {\prime} / k)} \sharp (\mathcal {P} _ {a ^ {\prime}} ^ {\prime}) ^ {0} (k ^ {\prime}) \prod_ {v ^ {\prime} \in | (\mathrm{X-U}) \otimes_ {k} k ^ {\prime} |} \sharp [ \mathcal {M} _ {v ^ {\prime}} (a _ {\mathrm{H}} ^ {\prime}) / \mathcal {P} _ {v ^ {\prime}} (\mathrm{J} _ {a ^ {\prime}} ^ {\prime}) ] (k ^ {\prime})} \end{array}
$$

avec le choix d'un schéma en groupes  $J_{a'}'$  lisse commutatif de fibre connexe muni d'un homomorphisme

$$
\mathrm{J} _ {a ^ {\prime}} ^ {\prime} \rightarrow \mathrm{J} _ {a ^ {\prime}} \rightarrow \mathrm{J} _ {\mathrm{H}, a _ {\mathrm{H}} ^ {\prime}}
$$

comme dans 8.4.1. Il sera commode de choisir $J_{a'}' = J_{a'}^0$ au-dessus de $X_v$.

8.6.8. — Puisque  $\tilde{a}_{\mathrm{H}}^{\prime}\in\tilde{\mathcal{U}}(k^{\prime})$ , on peut appliquer 8.5.7 à toutes les places  $v^{\prime}\neq v$ . En retranchant les égalités en ces places, on trouve une égalité en la place v du départ

$$
\sharp [ \mathcal {M} _ {\mathrm{H}, v} (a _ {\mathrm{H}} ^ {\prime}) / \mathcal {P} _ {v} (\mathrm{J} _ {a ^ {\prime}} ^ {0}) ] (k ^ {\prime}) _ {\kappa} = q ^ {r _ {v} (a _ {\mathrm{H}} ^ {\prime}) \deg (k ^ {\prime} / k)} \sharp [ \mathcal {M} _ {v} (a _ {\mathrm{H}} ^ {\prime}) / \mathcal {P} _ {v} (\mathrm{J} _ {a ^ {\prime}} ^ {0}) ] (k ^ {\prime}).
$$

Comme on sait que la fibre de Springer affine $\mathcal{M}_{v}(a)\otimes_{k}k^{\prime}$ munie de l'action de $\mathcal{P}_v(\mathrm{J}_a)\otimes_k k'$ est isomorphe à $\mathcal{M}_v(a')$ munie de l'action de $\mathcal{P}_v(\mathrm{J}_{a'})$ et la même chose pour le groupe H, on en déduit l'égalité

$$
\sharp [ \mathcal {M} _ {\mathrm{H}, v} (a _ {\mathrm{H}}) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0}) ] (k ^ {\prime}) _ {\kappa} = q ^ {r _ {\mathrm{H}, v} ^ {\mathrm{G}} (a _ {\mathrm{H}}) \deg (k ^ {\prime} / k)} \sharp [ \mathcal {M} _ {v} (a _ {\mathrm{H}}) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0}) ] (k ^ {\prime})
$$

pour toute extension $k'$ de $k$ de degré plus grand que $m$. En appliquant 8.1.14, on obtient l'égalité

$$
\sharp [ \mathcal {M} _ {\mathrm{H}, v} (a _ {\mathrm{H}}) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0}) ] (k) _ {\kappa} = q ^ {r _ {\mathrm{H}, v} ^ {\mathrm{G}} (a _ {\mathrm{H}})} \sharp [ \mathcal {M} _ {v} (a _ {\mathrm{H}}) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {0}) ] (k).
$$

En appliquant la formule 8.2.5, on obtient maintenant l'égalité

$$
\mathbf {O} _ {a} ^ {\kappa} (1 _ {\mathfrak {g} _ {v}}, \mathrm{d} t _ {v}) = q ^ {r _ {\mathrm{H}, v} ^ {\mathrm{G}} (a _ {\mathrm{H}})} \mathbf {S O} _ {a _ {\mathrm{H}}} (1 _ {\mathfrak {h} _ {v}}, \mathrm{d} t _ {v})
$$

qu'on voulait.

Ceci termine la démonstration de la conjecture de Langlands-Sheldstad 1.11.1. □

8.7. Stabilisation géométrique sur $\mathcal{A}^{\mathrm{ani}}$. — En renversant de nouveau le processus local-global, on peut maintenant compléter la démonstration de 6.4.2.

Démonstration. — Gardons les notations de 8.5. Comme dans 8.5, il suffit de démontrer l'égalité des traces 8.5.4

$$
\sum_ {n} (- 1) ^ {n} \mathrm{tr} (\sigma_ {k ^ {\prime}}, (\mathrm{L} _ {\kappa} ^ {n}) _ {\tilde {a}}) = \sum_ {n} (- 1) ^ {n} \mathrm{tr} (\sigma_ {k ^ {\prime}}, (\mathrm{L} _ {\mathrm{H,st}} ^ {n}) _ {\tilde {a} _ {\mathrm{H}}})\tag{8.7.1}
$$

pour tout $\tilde{a}_{\mathrm{H}} \in \tilde{\mathcal{A}}_{\mathrm{H}}^{\mathrm{ani}}(k)$ d'image $\tilde{a} \in \tilde{\mathcal{A}}^{\mathrm{ani}}(k)$. D'après 8.4.4, le membre de gauche de 8.5.4 vaut

$$
\left(\mathcal {P} _ {a} ^ {\prime}\right) ^ {0} (k) \prod_ {v \in | \mathrm{X-U} |} \sharp \left[ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) \right] (k) _ {\kappa}
$$

alors que le membre de droite vaut

$$
q ^ {r _ {\mathrm{H}} ^ {\mathrm{G} (\mathrm{D})}} (\mathcal {P} _ {a} ^ {\prime}) ^ {0} (k) \prod_ {v \in | \mathrm{X-U} |} \sharp [ \mathcal {M} _ {\mathrm{H}, v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k).
$$

En combinant 1.11.1, 8.2.5, on a l'égalité

$$
[ \mathcal {M} _ {v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k) _ {\kappa} = q ^ {r _ {\mathrm{H}, v} ^ {\mathrm{G}} (\mathrm{D})} [ \mathcal {M} _ {\mathrm{H}, v} (a) / \mathcal {P} _ {v} (\mathrm{J} _ {a} ^ {\prime}) ] (k)
$$

d'où 8.7.1.

8.8. Conjecture de Waldspurger. — Soient maintenant  $G_{1}$  et  $G_{2}$  deux X-schémas en groupes appariés au sens de 1.12.5. Supposons que les centres de  $G_{1}$  et  $G_{2}$  ne contiennent pas de tores déployés au-dessus de  $\overline{X}=X\otimes_{k}\bar{k}$ .

8.8.1. — Soient  $f_{1}: M_{1} \to A_{1}$  et  $f_{2}: M_{2} \to A_{2}$  les fibrations de Hitchin associées. Comme dans 4.18, on a

$$
\mathcal {A} = \mathcal {A} _ {1} = \mathcal {A} _ {2}.
$$

Soient $\mathcal{P}_1$ et $\mathcal{P}_2$ les $\mathcal{A}$-champs de Picard associés à $\mathrm{G}_1$ et $\mathrm{G}_2$. D'après 4.18.1, il existe un homomorphisme $\mathcal{P}_1 \to \mathcal{P}_2$ qui induit une isogénie entre leurs composantes neutres.

Théorème 8.8.2. — Il existe un isomorphisme entre les simplifications des faisceaux pervers gradués sur $\mathcal{A}^{\mathrm{ani}}$

$$
\mathrm{K} _ {1} = \bigoplus_ {n} ^ {p} \mathrm{H} ^ {n} (f _ {1, *} ^ {\text {ani}} \bar {\mathbf {Q}} _ {\ell}) _ {\text {st}} \quad \text {et} \quad \mathrm{K} _ {2} = \bigoplus_ {n} ^ {p} \mathrm{H} ^ {n} (f _ {2, *} ^ {\text {ani}} \bar {\mathbf {Q}} _ {\ell}) _ {\text {st}}.
$$

Ici l'indice st signifie la composante isotypique correspondant à l'action triviale de  $P_{i}$ .

La démonstration de ce théorème suit essentiellement les mêmes étapes que celle de 6.4.2. En particulier, on démontrera en cours de route le lemme fondamental non standard conjecturé par Waldspurger 1.12.7. Ici, on n'a pas besoin de passer au revêtement étale $\tilde{\mathcal{A}}^{\mathrm{ani}}$.

8.8.3. — On démontre d'abord qu'il existe un tel isomorphisme au-dessus de l'ouvert  $A^{\diamond}$ . Au-dessus de cet ouvert, les morphismes  $f_{1}$  et  $f_{2}$  sont propres et lisses de sorte que les restrictions de  $K_{1}$  et  $K_{2}$  à  $A^{\diamond}$  sont des systèmes locaux gradués. Pour démontrer qu'il existe un isomorphisme entre leurs simplifications, il suffit d'après le théorème de Chebotarev de démontrer l'égalité des traces

$$
\operatorname{tr} \left(\sigma_ {k ^ {\prime}}, \mathrm{K} _ {1, a}\right) = \operatorname{tr} \left(\sigma_ {k ^ {\prime}}, \mathrm{K} _ {2, a}\right)\tag{8.8.4}
$$

pour toute extension finie $k'$ de $k$ et pour tout point $a \in \mathcal{A}^{\diamond}(k')$. En remplaçant X par $\mathrm{X} \otimes_k k'$, on peut supposer que $k = k'$.

8.8.5. — Soit $a \in \mathcal{A}^{\diamond}(k)$. D'après 4.7.7, on sait :

\- $\mathcal{P}_{i,a}$ agit simplement transitivement sur $\mathcal{M}_{i,a}$

\- $\mathcal{P}_{i,a}^{0}$ est isogène à une variété abélienne $\mathrm{P}_{i,a}^{0}$.

D'après la formule des points fixes 8.1.6 et 8.1.7, on a

$$
\mathrm{tr} (\sigma , \mathrm{K} _ {i, a}) = \sharp \mathrm{P} _ {i} ^ {0} (k).
$$

Puisque  $P_{1}^{0}$  et  $P_{2}^{0}$  sont des variétés abéliennes isogènes sur k, ils ont le même nombre de k-points d'où l'égalité des traces 8.8.4. Il existe donc un isomorphisme entre les simplifications des restrictions de  $K_{1}$  et  $K_{2}$  à  $A^{\diamond}$ .

8.8.6. — D'après le théorème du support 7.8.3, il existe un isomorphisme entre les semi-simplifications des restrictions de  $K_{1}$  et  $K_{2}$  à

$$
\mathcal {A} ^ {\mathrm{good}} = \mathcal {A} ^ {\mathrm{ani}} - \mathcal {A} ^ {\mathrm{bad}}.
$$

8.8.7. — En procédant comme dans 8.6, on en déduit le lemme fondamental non standard conjecturé par Waldspurger 1.12.7.

8.8.8. — En renversant de nouveau le processus local-global comme dans 8.7, on en déduit l'égalité des traces 8.8.4 pour tout $a \in \mathcal{A}^{\mathrm{ani}}(k')$ pour toute extension finie $k'$ de $k$. On en déduit le théorème 8.8.2.

8.8.9. — Si on admet la conjecture 7.8.1, le théorème 7.2.1 implique que la partie stable des faisceaux pervers de cohomologie de la fibration de Hitchin est le prolongement intermédiaire de sa restriction à l'ouvert $\mathcal{A}^{\diamond}$ où elle consiste en des systèmes locaux.

## Remerciements

Sans l'aide et l'encouragement des mathématiciens ci-dessous nommés, ce programme n'aurait probablement pas abouti et n'aurait probablement même pas eu lieu. Je tiens à leur exprimer toute ma reconnaissance. R. Kottwitz et G. Laumon qui m'ont appris la théorie de l'endoscopie et la géométrie algébrique, n'ont jamais cessé de m'aider avec beaucoup de générosité. M. de Cataldo, P. Deligne, V. Drinfeld, G. Laumon ont relu attentivement certaines parties du manuscrit. Leurs commentaires m'ont permis de corriger quelques erreurs et améliorer certains arguments. L'argument de dualité de Poincaré et de comptage de dimension que m'a expliqué Goresky a joué un rôle catalyseur de cet article. Il est évident que la lecture de l'article de Hitchin [34] a joué un rôle dans la conception de ce programme. Il en a été de même des articles de Faltings [24], de Donagi et Gaitsgory [23] et de Rapoport [63]. Les conversations que j'ai eues avec M. Harris sur le lemme non standard ont renforcé ma conviction sur la conjecture du support. M. Raynaud a eu la gentillesse de répondre à certaines de mes questions techniques. Je voudrais remercier J. Arthur, J.-P. Labesse, L. Lafforgue, R. Langlands, C. Moeglin, H. Saito et J.-L. Waldspurger de m'avoir encouragé dans cette longue marche à la poursuite du lemme. Je dis un merci chaleureux aux mathématiciens qui ont participé activement aux séminaires sur l'endoscopie et le lemme fondamental que j'ai contribué à organiser à Paris-Nord et à Bures au printemps 2003 et à Princeton aux automnes 2006 et 2007 parmi lesquels P.-H. Chaudouard, J.-F. Dat, L. Fargues, A. Genestier, A. Ichino, V. Lafforgue, S. Morel, Nguyen Chu Gia Vuong, Ngo Dac Tuan, S.W. Shin, D. Whitehouse et Zhiwei Yun. Je remercie J. Heinloth pour d'utiles indications bibliographiques.

J'exprime ma profonde gratitude au travail méticuleux des rapporteurs anonymes et de Deligne qui ont découvert des faiblesses rédactionnelles et mathématiques dans la version antérieure de ce texte et ont ainsi beaucoup contribué à la présente. J'exprime aussi ma gratitude à Cécile Gourgue qui m'a aidé à corriger des fautes de français.

J'exprime ma gratitude à l'I.H.É.S. à Bures-sur-Yvette pour un séjour très agréable en 2003 pendant lequel ce projet a été conçu. Il a été mené à son terme durant mes séjours en automne 2006 et pendant l'année universitaire 2007–2008 à l'Institute for Advanced Study à Princeton qui m'a offert des conditions de travail idéales. Pendant mes séjours à Princeton, j'ai bénéficié des soutiens financiers de l'AMIAS en 2006, de la fondation Charles Simonyi et ainsi que de la NSF à travers le contrat DMS-0635607 en 2007–2008.

## RÉFÉRENCES

1. A. ALTMAN, A. IARROBINO, and S. KLEIMAN, Irreducibility of the compactified Jacobian, in Real and Complex Singularities (Proc. Ninth Nordic Summer School/NAVF Sympos. Math., Oslo, 1976), pp. 1–12.

2. J. ARTHUR, An introduction to the trace formula, in Harmonic Analysis, the Trace Formula, and Shimura Varieties. Clay Math. Proc., vol. 4, pp. 1–263, Am. Math. Soc., Providence, 2005.

3. M. ARTIN, Algebraic approximation of structures over complete local rings, Inst. Hautes Études Sci. Publ. Math., 36 (1969), 23–58.

4. A. BEAUVILLE and Y. LASZLO, Un lemme de descente, C. R. Acad. Sci. Paris, 320 (1995), 335–340.

5. A. BEAUVILLE, M. NARASIMHAN, and S. RAMANAN, Spectral curves and generalized theta divisor, J. Reine Angew. Math., 398 (1989), 169–179.

6. V. BEILINSON, A. DRINFELD, Opers, preprint.

7. A. BEILINSON, J. BERNSTEIN, and P. DELIGNE, Faisceaux pervers, Astérisque, 100 (1982).

8. R. BEZRUKAVNIKOV, The dimension of the fixed points set on affine flag manifolds, Math. Res. Lett., 3 (1996), 185-189.

9. I. Biswas and S. RAMANAN, Infinitesimal study of Hitchin pairs, J. Lond. Math. Soc., 49 (1994), 219-231.

10. S. Bosch, W. Lutkebohmert, and M. Raynaud, Neron Models, Ergebn. der Math., vol. 21, Springer, Berlin, 1990.

11. N. BOURBAKI, Groupes et algèbres de Lie, Masson, Paris, 1981, chapitres 4, 5 et 6.

12. R. CARTER, Finite Group of Lie Type, Wiley Classics Library.

13. C.-L. CHAI and J.-K. YU, Congruences of Néron models for tori and the Artin conductor, Ann. Math. (2), 154 (2001), 347–382.

14. L. CLOZEL, The fundamental lemma for stable base change, Duke Math. J., 61 (1990), 255-302.

15. R. CLUCKERS and F. LOESER, Fonctions constructibles exponentielles, transformation de Fourier motivique et principe de transfert, C. R. Acad. Sci. Paris, 341 (2005), 741–746.

16. J.-F. DAT, Lemme fondamental et endoscopie, une approche géométrique, Séminaire Bourbaki 940, novembre 2004.

17. O. DEBARRE, Théorèmes de connexité pour les produits d'espaces projectifs et les grassmanniennes, Am. J. Math., 118 (1996), 1347–1367.

18. P. DELIGNE, La conjecture de Weil II, Publ. Math. I.H.E.S., 52 (1980), 137-252.

19. P. DELIGNE, Décomposition dans la catégorie dérivée, in Motives, Proc. of Symp. in Pure Math., vol. 55.1, pp. 115–128, 1994.

20. P. DELIGNE, Communication privée, 2007.

21. M. DÉMAZURE and A. GROTHENDIECK, Séminaire de géométrie algébrique du Bois-Marie 3. LNM, vols. 151, 152, 153, Springer.

22. S. DIAZ and J. HARRIS, Ideals associated to Deformations of singular plane curves, Trans. Am. Math. Soc., 309 (1988), 433–468.

23. R. DONAGI and D. GAITSGORY, The gerb of Higgs bundles, Transform. Groups, 7 (2002), 109–153.

24. G. FALTINGS, Stable G-bundles and projective connections, J. Algebraic Geom., 2 (1993), 507-568.

25. B. FANTECHI, L. GÖTTSche, and D. Van STRATEN, Euler number of the compactified Jacobian and multiplicity of rational curves, J. Algebraic Geom., 8 (1999), 115–133.

26. M. GORESKY, R. KOTTWITZ, and R. MACPHERSON, Homology of affine Springer fiber in the unramified case, Duke Math. J., 121 (2004), 509–561.

27. M. GORESKY, R. KOTTWITZ, and R. MACPHERSON, Purity of equivalued affine Springer fibers, Represent. Theory, 10 (2006), 130–146.

28. M. GORESKY, R. KOTTWITZ, and R. MACPHERSON, Codimension of root valuation strata, preprint (2006).

29. A. GROTHENDIECK, Groupes de monodromie en Géométrie algébrique (SGA 7 I), LNM, vol. 288, Springer.

30. A. GROTHENDIECK and J. DIEUDONNÉ, Éléments de géométrie algébrique IV. Étude locale des schémas et de morphismes de schémas, Publ. Math. I.H.E.S. 20, 24, 28 et 32.

31. T. HALES, The fundamental lemma for Sp(4), Proc. Am. Math. Soc., 125 (1997), 301-308.

32. T. HALES, A statement of the fundamental lemma, in Harmonic Analysis, the Trace Formula, and Shimura Varieties. Clay Math. Proc., vol. 4, pp. 643–658, Am. Math. Soc., Providence, 2005.

33. J. HEINLOTH, Uniformization of $\mathcal{G}$-bundles. A paraître dans Math. Ann.

34. N. HITCHIN, Stable bundles and integrable connections, Duke Math. J., 54 (1987), 91-114.

35. D. KAZHDAN, On lifting, in Lie Group Representations, II (College Park, Md., 1982/1983). Lecture Notes in Math., vol. 1041, pp. 209–249, Springer, Berlin, 1984.

36. D. KAZHDAN and G. LUSZTIG, Fixed point varieties on affine flag manifolds, Isr. J. Math., 62 (1988), 129-168.

37. S. KLEIMAN, Algebraic cycles and Weil conjectures, in Dix exposés sur la Cohomologie des Schémas, North-Holland, Amsterdam, 1968.

38. B. KOSTANT, Lie group representations on polynomial rings, Am. J. Math., 85 (1963), 327-404.

39. R. Kottwitz, Orbital integrals on  $GL_{3}$ , Am. J. Math., 102 (1980), 327–384.

40. R. Kottwitz, Unstable orbital integrals on SL(3), Duke Math. J., 48 (1981), 649-664.

41. R. Kottwitz, Stable trace formula: cuspidal tempered terms, Duke Math. J., 51 (1984), 611-650.

42. R. KOTTWITZ, Isocristal with additional structures, Compos. Math., 56 (1985), 201-220.

43. R. Kottwitz, Base change for unit elements of Hecke algebras, Compos. Math., 60 (1986), 237-250.

44. R. KOTTWITZ, Stable trace formula: elliptic singular terms, Math. Ann., 275 (1986), 365-399.

45. R. KOTTWITZ, Shimura varieties and  $\lambda$ -adic representations, in Automorphic Forms, Shimura Varieties, and L-functions, Vol. I, Perspect. Math., vol. 10, pp. 161–209, Academic Press, Boston, 1990.

46. R. Kottwiz, Transfert factors for Lie algebra, Represent. Theory, 3 (1999), 127-138.

47. J.-P. LABESSE, Fonctions élémentaires et lemme fondamental pour le changement de base stable, Duke Math. J., 61 (1990), 519–530.

48. J.-P. LABESSE, R. LANGLANDS, L-indistinguishability for SL(2), Can. J. Math., 31 (1979), 726-785.

49. R. LANGLANDS, Base Change for GL(2), Annals of Mathematics Studies, vol. 96, Princeton University Press, Princeton, 1980.

50. R.P. LANGLANDS, Les débuts d'une formule des traces stables, in Publications Mathématiques de l'Université Paris VII, vol. 13, Université de Paris VII, U.E.R. de Mathématiques, Paris, 1983.

51. G. LAUMON, Fibres de Springer et Jacobiennes compactifiées, in Algebraic Geometry and Number Theory. Progr. Math., vol. 253, pp. 515–563, Birkhäuser Boston, Boston, 2006.

52. G. LAUMON, Sur le lemme fondamental pour les groupes unitaires, prépublication, arXiv :org/abs/math/0212245.

53. G. LAUMON and L. MORET-BAILLY, Champs algébriques, Ergebnisse der Mathematik, vol. 39, Springer, Berlin, 2000.

54. G. LAUMON and B. C. Ngô, Le lemme fondamental pour les groupes unitaires, Ann. Math., 168 (2008), 477-573.

55. P. LEVY, Involutions of reductive Lie algebras in positive characteristic, Adv. Math., 210 (2007), 505-559.

56. D. MUMFORD, Abelian Varieties. Oxford University Press.

57. B. C. Ngô, Fibration de Hitchin et endoscopie, Invent. Math, 164 (2006), 399–453.

58. B. C. Ngô, Fibration de Hitchin et structure endoscopique de la formule des traces. International Congress of Mathematicians, vol. II, pp. 1213–1225, Eur. Math. Soc., Zürich, 2006.

59. B. C. Ngô, Geometry of the Hitchin fibration. Livre en préparation.

60. B. C. Ngô, Decomposition theorem and abelian fibration. Article d'exposition pour le projet du livre disponible à l'adresse http://fa.institut.math.jussieu.fr/node/44.

61. NITSURE, Moduli space of semistable pairs on a curve, Proc. Lond. Math. Soc. (3), 62 (1991), 275-300.

62. T. ONO, On Tamagawa numbers, in Algebraic Groups and Discontinuous Subgroups, Proc. of Symp. in Pure Math, vol. 9, Am. Math. Soc., Providence, 1966.

63. M. RAPOPORT, A guide to the reduction of Shimura varieties in Automorphic forms. I, Astérisque, 298 (2005), 271–318.

64. M. RAYNAUD, Communication privée, 2004.

65. J. ROGAWSKI, Automorphic Representations of Unitary Groups in Three Variables, Annals of Math. Studies, vol. 123, pp. 1–259, Princeton University Press, Princeton, 1990

66. M. ROSENLICHT, Some basic theorems on algebraic groups, Am. J. Math., 78 (1956), 401-443.

67. H. SAITO, Automorphic Forms and Algebraic Extensions of Number Fields (Department of Mathematics, Kyoto University), Lectures in Mathematics, vol. 8, Kinokuniya Book-Store Co., Ltd., Tokyo, 1975.

68. M. SCHÖDER, Inauguraldissertation, Mannheim 1993.

69. J.-P. SERRE, Groupes algébriques et corps de classes, Publications de l'Institut de Mathématique de l'Université de Nancago, vol. VII, Hermann, Paris, 1959.

70. J.-P. SERRE, Corps locaux, Publications de l'Institut de Mathématique de l'Université de Nancago, vol. VIII, Hermann, Paris, 1962.

71. D. SHELSTAD, Orbital integrals and a family of groups attached to a real reductive group, Ann. Sci. École Norm. Supér., 12 (1979).

72. N. SPALTENSTEIN, On the fixed point set of a unipotent element on the variety of Borel subgroups, Topology, 16 (1977), 203–204.

73. T. SPRINGER, Some arithmetical results on semi-simple Lie algebras, Publ. Math. I.H.E.S., 33 (1966), 115-141.

74. T. SPRINGER, Reductive groups, in Automorphic Forms, Representations, and L-functions, Proc. Symp. in Pure Math, vol. 33-1, Am. Math. Soc., Providence, 1997.

75. T. SPRINGER and R. STEINBERG, Conjugacy classes, in Seminar on Algebraic Groups and Related Finite Groups, Lectures Notes in Math., vol. 131, Springer, Berlin, 1970.

76. R. STEINBERG, Lectures on Chevalley groups, Livre polycopié.

77. B. TEISSIER, Résolution simultanée – I. Famille de courbes, in M. Demazure, H. Pinkham, and B. Teissier (eds.), Séminaire sur les Singularités des Surfaces. LNM, vol. 777, Springer, Berlin, 1980.

78. F. VELDKAMP, The center of the universal enveloping algebra of a Lie algebra in characteristic p, Ann. Sci. École Norm. Supér. (4), 5 (1972), 217–240.

79. J.-L. WALDSPURGER, Sur les intégrales orbitales tordues pour les groupes linéaires : un lemme fondamental, Can. J. Math., 43 (1991), 852–896.

80. J.-L. WALDSPURGER, Le lemme fondamental implique le transfert, Compos. Math., 105 (1997), 153-236.

81. J.-L. WALDSPURGER, Intégrales orbitales nilpotentes et endoscopie pour les groupes classiques non ramifiés, Astérisque, 269.

82. J.-L. WALDSPURGER, Endoscopie et changement de caractéristique, Inst. Math. Jussieu 5 (2006), 423-525.

83. J.-L. WALDSPURGER, L'endoscopie tordue n'est pas si tordue, Mem. Am. Math. Soc. 194 (2008), x+261

84. R. WEISSAUER, A special case of fundamental lemma I–IV, preprint Mannheim (1993).

85. D. WHITEHOUSE, The twisted weighted fundamental lemma for the transfer of automorphic forms from GSp(4). Formes automorphes. II. Le cas du groupe GSp(4), Astérisque, 302 (2005), 291–436.

B. C. N.

Institute for Advanced Study,

Einstein Drive,

Princeton NJ 08540, USA

ngo@ias.edu

and

Département de Mathématiques,
Université Paris-Sud,
91405 Orsay, France
Bao-Chau.Ngo@math.u-psud.fr

Manuscrit reçu le 2 mai 2008
Version révisée le 4 décembre 2009
Manuscrit accepté le 4 avril 2010
publié en ligne le 23 avril 2010.