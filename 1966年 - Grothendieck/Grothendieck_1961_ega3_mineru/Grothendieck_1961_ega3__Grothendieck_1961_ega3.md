ALEXANDER GROTHENDIECK

Éléments de géométrie algébrique : III. Étude cohomologique des faisceaux cohérents, Seconde partie

Publications mathématiques de l'I.H.É.S., tome 17 (1963), p. 5-91

&lt;http://www.numdam.org/item?id=PMIHES_1963_17_5_0&gt;

© Publications mathématiques de l'I.H.É.S., 1963, tous droits réservés.

L'accès aux archives de la revue « Publications mathématiques de l'I.H.É.S. » (http://www.ihes.fr/IHES/Publications/Publications.html) implique l'accord avec les conditions générales d'utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou impression systématique est constitutive d'une infraction pénale. Toute copie ou impression de ce fichier doit contenir la présente mention de copyright.

INSTITUT
DES HAUTES ÉTUDES
SCIENTIFIQUES

![](images/page_1_image_1.jpg)

# ÉLÉMENTS DE GÉOMÉTRIE ALGÉBRIQUE

par A. GROTHENDIECK
Rédigés avec la collaboration de J. DIEUDONNÉ

III
ÉTUDE COHOMOLOGIQUE
DES FAISCEAUX COHÉRENTS
(Seconde Partie)

1963
PUBLICATIONS MATHÉMATIQUES, N° 17
LE BOIS-MARIE — BURES-SUR-YVETTE (S.-et-O.)

DÉPOT LÉGAL

$^{1re}$ édition .. .. .. $4^{e}$ trimestre 1963

TOUS DROITS

réservés pour tous pays

© 1963, Institut des Hautes Études Scientifiques

## ÉTUDE COHOMOLOGIQUE DES FAISCEAUX COHÉRENTS

## § 6. FONCTEURS « TOR » LOCAUX ET GLOBAUX; FORMULE DE KÜNNETH

## 6.1. Introduction.

(6.1.1) Soient $f: \mathbf{X} \to \mathbf{Y}$ un morphisme de préschémas, $\mathcal{F}$ un $\mathcal{O}_{\mathbf{X}}$-Module quasi-cohérent. Dans l'étude des « images directes supérieures » $\mathrm{R}^{n}f_{*}(\mathcal{F})$, on est amené à considérer le problème général suivant : étant donné un morphisme « changement de base » $g: \mathbf{Y}' \to \mathbf{Y}$, on pose $\mathbf{X}' = \mathbf{X}_{(\mathbf{Y}')} = \mathbf{X} \times_{\mathbf{Y}} \mathbf{Y}'$, $\mathcal{F}' = \mathcal{F} \otimes_{\mathbf{Y}} \mathcal{O}_{\mathbf{Y}'}$, $f' = f_{(\mathbf{Y}')}: \mathbf{X}' \to \mathbf{Y}'$, et l'on se propose d'avoir des renseignements sur les images directes supérieures $\mathrm{R}^{n}f_{*}'(\mathcal{F}')$ (en supposant connus les $\mathrm{R}^{n}f_{*}(\mathcal{F})$). On voit aisément (cf. par exemple (7.7.2)) que l'on est ramené à étudier les variations de $\mathrm{R}^{n}f_{*}(\mathcal{F} \otimes_{\mathcal{O}_{\mathbf{Y}}} \mathcal{G})$ pour un $\mathcal{O}_{\mathbf{Y}}$-Module quasi-cohérent variable $\mathcal{G}$, autrement dit le foncteur $\mathcal{G} \rightsquigarrow \mathrm{R}^{n}f_{*}(\mathcal{F} \otimes_{\mathcal{O}_{\mathbf{Y}}} \mathcal{G})$. Si $\mathcal{F}$ est plat sur Y, le foncteur $\mathcal{G} \rightsquigarrow \mathcal{F} \otimes_{\mathcal{O}_{\mathbf{Y}}} \mathcal{G}$ est exact ($\mathbf{0}_{\mathrm{I}}, 6.7.4$) et par suite le foncteur composé $\mathcal{G} \rightsquigarrow \mathrm{R}^{n}f_{*}(\mathcal{F} \otimes_{\mathcal{O}_{\mathbf{Y}}} \mathcal{G})$ est encore un foncteur cohomologique. Mais il n'en est plus de même dans le cas général; pour pouvoir appliquer les méthodes cohomologiques, on est conduit à substituer à $\mathcal{G} \rightsquigarrow \mathrm{R}^{n}f_{*}(\mathcal{F} \otimes_{\mathcal{O}_{\mathbf{Y}}} \mathcal{G})$ d'autres foncteurs, qui cette fois sont toujours des foncteurs cohomologiques. Ces foncteurs, qui généralisent les foncteurs « Tor » de la théorie des modules, sont définis aux n°8 6.3 à 6.7; il y a d'ailleurs deux telles généralisations, l'une « locale » et l'autre « globale », reliées par des suites spectrales qui seront discutées au n° 6.7; comme application de ces suites spectrales, on obtient en particulier, sous certaines conditions, une « formule de Künneth » exprimant $\mathrm{R}^{n}(f_{1} \times f_{2})_{*}(\mathcal{F}_{1} \otimes_{\mathbf{Y}} \mathcal{F}_{2})$ à l'aide des images directes supérieures $\mathrm{R}^{p}f_{1*}(\mathcal{F}_{1})$ et $\mathrm{R}^{q}f_{2*}(\mathcal{F}_{2})$. D'autres suites spectrales (6.8) généralisent les suites spectrales d'associativité du foncteur « Tor » de modules; enfin, le problème du changement de base conduit lui aussi à des suites spectrales (6.9).

(6.1.2) En outre, on constate (6.10) que les foncteurs cohomologiques $\mathcal{G} \rightsquigarrow \mathcal{T}_{\bullet}(\mathcal{G})$ ainsi définis sont localement (sur Y) du type $\mathcal{G} \rightsquigarrow \mathcal{H}_{\bullet}(\mathcal{L}_{\bullet} \otimes_{Y} \mathcal{G})$, où $\mathcal{L}_{\bullet}$ est un complexe de $\mathcal{O}_{Y}$-Modules localement libres (défini à une homotopie près) et $\mathcal{H}_{\bullet}$ l'homologie. Il y a alors intérêt à oublier la situation particulière qui a donné naissance à $\mathcal{T}_{\bullet}$, et à étudier de

façon générale les foncteurs de la forme précédente $\mathcal{G} \rightsquigarrow \mathcal{H}_{\bullet}(\mathcal{L}_{\bullet} \otimes_{\mathrm{Y}} \mathcal{G})$ (où l'on fait en outre le cas échéant des hypothèses de finitude appropriées sur les $\mathcal{L}_i$ ou les $\mathcal{H}_i(\mathcal{L}_i)$): c'est ce qui est l'objet du § 7, dont la lecture, pour l'essentiel, est indépendante du § 6. Les propriétés les plus importantes de ces foncteurs concernent les propriétés d'exactitude d'une composante $\mathcal{T}_i$ de $\mathcal{T}_i$; on donnera divers critères permettant d'établir de telles propriétés; comme application, on obtiendra des conditions permettant d'affirmer (avec les notations de (6.1.1)) que le foncteur $\mathcal{G} \rightsquigarrow \mathbf{R}^n f_*(\mathcal{F} \otimes_{\mathcal{O}_\mathrm{Y}} \mathcal{G})$ est exact (ce qu'on exprimera en disant que $\mathcal{F}$ est cohomologiquement plat sur Y en dimension $n$). Une autre propriété importante pour les composantes $\mathcal{T}_i$ de $\mathcal{T}_{\bullet}(\mathcal{G}) = \mathcal{H}_{\bullet}(\mathcal{L}_{\bullet} \otimes_{\mathrm{Y}} \mathcal{G})$ est une propriété de semi-continuité de la fonction $y \rightsquigarrow \dim_{\mathbf{k}(y)} (\mathrm{T}_i(\mathbf{k}(y)))$; lorsque $\mathcal{T}_i$ est exact, cette propriété est remplacée par une propriété de continuité, la réciproque étant d'ailleurs vraie d'après Grauert lorsque Y est réduit (7.8.4).

(6.1.3) Dans les §§ 6 et 7, nous avons systématiquement fait usage de l'hypercohomologie, en prenant partout comme arguments des complexes de faisceaux au lieu de faisceaux, bien que la nécessité de ce point de vue n'apparaîtra que dans des chapitres ultérieurs. Le formalisme cohomologique développé à cette occasion deviendra d'ailleurs plus transparent dans le chapitre de ce Traité qui sera consacré à la mise au point d'une algèbre des foncteurs cohomologiques de faisceaux cohérents, incluant le formalisme de la dualité. Mais cela demandera des développements qui sortent du cadre du présent chapitre.

(6.1.4) Pour abréger, étant donnés deux complexes  $K^{\bullet}$ ,  $K^{\prime\prime}$  dans une catégorie abélienne C, nous dirons qu'un morphisme de complexes  $f: K^{\bullet} \to K^{\prime\prime}$  est un homotopisme s'il existe un morphisme  $g: K^{\prime\prime} \to K^{\bullet}$  tel que les morphismes composés fog et gof soient tous deux homotopes à l'identité (par abus de langage, lorsqu'il existe un tel homotopisme, on dira aussi que  $K^{\bullet}$  et  $K^{\prime\prime}$  sont homotopes). Lorsqu'on peut définir l'hypercohomologie d'un foncteur covariant additif T de C dans une catégorie abélienne  $C'$ , par rapport à un complexe de C (0, 11.4.3), il est immédiat qu'un homotopisme  $K^{\bullet} \to K^{\prime\prime}$  de complexes de C définit canoniquement un isomorphisme  $\mathbf{R}^{\bullet}\mathbf{T}(\mathbf{K}^{\bullet}) \to \mathbf{R}^{\bullet}\mathbf{T}(\mathbf{K}^{\prime\bullet})$  pour l'hypercohomologie (loc. cit.).

## 6.2. Hypercohomologie des complexes de modules sur un préschéma.

(6.2.1) Soient X un préschéma, $\mathcal{K}^{\bullet} = (\mathcal{K}^{i})_{i\in \mathbf{Z}}$ un complexe de $\mathcal{O}_{\mathrm{X}}$-Modules dont l'opérateur de dérivation est de degré $+1$. Rappelons que pour tout morphisme $f:\mathbf{X}\to \mathbf{Y}$ de préschémas, on a défini (0, 12.4.1) les $\mathcal{O}_{\mathrm{Y}}$-Modules d'hypercohomologie $\mathcal{H}^n (f,\mathcal{H}^\bullet)$ (aussi notés $\mathcal{H}_j^n (\mathcal{H}^\bullet)$ ou $\mathbf{R}^nf_*(\mathcal{H}^\bullet)$) pour tout $n\in \mathbf{Z}$; l'hypercohomologie $\mathcal{H}^{\bullet}(f,\mathcal{H}^{\bullet})$ est l'aboutissement des deux foncteurs spectraux ' $\mathcal{E}(f,\mathcal{H}^{\bullet})$ et '' $\mathcal{E}(f,\mathcal{H}^{\bullet})$, dont les termes $\mathcal{E}_2$ sont donnés par

(6.2.1.1)

$$
^ \prime \mathcal {E} _ {2} ^ {p q} = \mathcal {H} ^ {p} (\mathcal {H} ^ {q} (f, \mathcal {K} ^ {\bullet}))\tag{6.2.1.2}
$$

$$
^ {\prime \prime} \mathcal {E} _ {2} ^ {p q} = \mathcal {H} ^ {p} (f, \mathcal {H} ^ {q} (\mathcal {K} ^ {\bullet})) = R ^ {p} f _ {*} (\mathcal {H} ^ {q} (\mathcal {K} ^ {\bullet}))
$$

138

où $\mathcal{H}^{q}(f, \mathcal{K}^{\bullet})$ est le complexe dont le composant de degré $i$ est $\mathcal{H}^{q}(f, \mathcal{K}^{i}) = \mathrm{R}^{q} f_{*}(\mathcal{K}^{i})$ (loc. cit.). Rappelons aussi que lorsque Y est réduit à un point, on note l'hypercohomologie correspondante $\mathbf{H}^{\bullet}(\mathbf{X}, \mathcal{K}^{\bullet})$ (qui est formée de modules sur $\Gamma(\mathbf{X}, \mathcal{O}_{\mathbf{X}})$ indépendants du préschéma ponctuel Y considéré); lorsque Y = X et $f = \mathrm{I}_{\mathbf{X}}$, on a $\mathcal{H}^{n}(f, \mathcal{K}^{\bullet}) = \mathcal{H}^{n}(\mathcal{K}^{\bullet})$ (cohomologie du complexe $\mathcal{K}^{\bullet}$); lorsque $\mathcal{K}^{i} = 0$, sauf pour $i = i_{0}$, on a

$$
\mathcal {H} ^ {n} (f, \mathcal {K} ^ {\bullet}) = \mathrm{R} ^ {n - i _ {0}} f _ {*} (\mathcal {K} ^ {i _ {0}}).
$$

La suite spectrale $\mathcal{E}(f, \mathcal{K}^{\bullet})$ est toujours régulière; les deux suites spectrales sont birégulières lorsque $K^{\bullet}$ est limité inférieurement (0, 12.4.1).

Tout homotopisme $h: \mathcal{H}^{\bullet} \to \mathcal{H}''$ de complexes de $\mathcal{O}_{\mathrm{X}}$-Modules (6.1.4) donne un isomorphisme $\mathcal{H}^{\bullet}(f, \mathcal{H}^{\bullet}) \simeq \mathcal{H}^{\bullet}(f, \mathcal{H}''')$ pour l'hypercohomologie. Il en est de même lorsqu'on suppose seulement que $\mathcal{H}^{\bullet}(h): \mathcal{H}^{\bullet}(\mathcal{H}^{\bullet}) \to \mathcal{H}^{\bullet}(\mathcal{H}''')$ est un isomorphisme et que $\mathcal{H}^{\bullet}$ et $\mathcal{H}''$ sont limités inférieurement, comme il résulte aussitôt de (0, 11.1.5) appliqué à la suite spectrale (6.2.1.2) et à l'analogue pour $\mathcal{H}''$. Enfin, pour tout recouvrement ouvert $\mathfrak{U} = (\mathrm{U}_{\alpha})$ de X, on a aussi défini (0, 12.4.5) l'hypercohomologie $\mathbf{H}^{\bullet}(\mathfrak{U}, \mathcal{H}^{\bullet})$ comme la cohomologie du bicomplexe $\mathbf{C}^{\bullet}(\mathfrak{U}, \mathcal{H}^{\bullet})$ (dont le composant d'indices (i, j) est par définition $\mathbf{C}^{i}(\mathfrak{U}, \mathcal{H}^{j})$); les $\mathbf{H}^{n}(\mathfrak{U}, \mathcal{H}^{\bullet})$ sont encore des modules sur $\Gamma(\mathrm{X}, \mathcal{O}_{\mathrm{X}})$.

Proposition (6.2.2). — Soient X un schéma,  $\mathfrak{U}=(\mathrm{U}_{\alpha})$  un recouvrement de X par des ouverts affines. Pour tout complexe  $K^{\bullet}$  de  $O_{X}$ -Modules quasi-cohérents, les modules d'hypercohomologie  $\mathbf{H}^{\bullet}(\mathbf{X},\mathcal{K}^{\bullet})$  et  $\mathbf{H}^{\bullet}(\mathfrak{U},\mathcal{K}^{\bullet})$  sont canoniquement isomorphes.

En effet, toute intersection finie V d'ouverts du recouvrement U est affine (I, 5.5.6), donc  $\mathrm{H}^{q}(\mathrm{V},\mathcal{K}^{i})=\mathrm{o}$  pour tout i et tout q>0 (1.3.1); la proposition est donc un cas particulier de (0, 12.4.7).

Proposition (6.2.3). — Soit $f: \mathbf{X} \to \mathbf{Y}$ un morphisme quasi-compact et séparé de préschémas. Pour tout complexe $\mathcal{K}^{\bullet}$ de $\mathcal{O}_{\mathbf{X}}$-Modules quasi-cohérents, les $\mathcal{O}_{\mathbf{Y}}$-Modules $\mathcal{H}^{n}(f, \mathcal{K}^{\bullet})$ sont quasi-cohérents.

Comme les $\mathcal{H}^{q}(f,\mathcal{K}^{i})=\mathrm{R}^{q}f_{*}(\mathcal{K}_{i})$ sont des $\mathcal{O}_{\mathrm{Y}}$-Modules quasi-cohérents (1.4.10), il en est de même de $^{\prime}\mathcal{E}_{2}^{pq}$, qui, d'après (6.2.1.1), est quotient d'un noyau d'homomorphisme de Modules quasi-cohérents par une image d'un tel homomorphisme (I, 4.1.1). Pour la même raison, tous les $\mathcal{O}_{\mathrm{Y}}$-Modules $^{\prime}\mathcal{E}_{r}^{pq},\mathrm{B}_{k}(^{\prime}\mathcal{E}_{r}^{pq}),\mathrm{Z}_{k}(^{\prime}\mathcal{E}_{r}^{pq})$ de la première suite spectrale sont quasi-cohérents. La régularité de la suite spectrale $^{\prime}\mathcal{E}(f,\mathcal{K}^{\bullet})$ entraîne que $\mathrm{Z}_{\infty}(^{\prime}\mathcal{E}_{2}^{pq})$ est égal à un des $\mathrm{Z}_{k}(^{\prime}\mathcal{E}_{2}^{pq})$, donc est quasi-cohérent, et il en est de même de $\mathrm{B}_{\infty}(^{\prime}\mathcal{E}_{2}^{pq})=\lim_{k}\mathrm{B}_{k}(^{\prime}\mathcal{E}_{2}^{pq})$ (0, 11.2.4 et I, 4.1.1); les $^{\prime}\mathcal{E}_{\infty}^{pq}$ sont donc aussi quasi-cohérents.

La suite spectrale précédente étant régulière, la filtration des  $\mathrm{F}^{p}(\mathcal{H}^{n}(f,\mathcal{K}^{\bullet}))$  est discrète et exhaustive; autrement dit, le  $O_{Y}$ -Module  $\mathcal{E}^{n}(f,\mathcal{K}^{\bullet})$  est réunion d'une suite croissante  $(\mathcal{G}_{k})_{k\geqslant0}$  de  $O_{Y}$ -Modules telle que  $G_{0}=o$  et que chaque  $G_{k}/G_{k-1}$  soit égal à un des  $O_{Y}$ -Modules ' $E_{\infty}^{pq}$ , donc soit quasi-cohérent. Par récurrence sur k, on en déduit que les  $G_{k}$  sont quasi-cohérents (I.4.17), et comme  $\mathcal{H}^{n}(f,\mathcal{K}^{\bullet})=\varinjlim\mathcal{G}_{k}$ , la proposition est démontrée (I, 4.1.1).

Corollaire (6.2.4). — Sous les hypothèses de (6.2.3), pour tout ouvert affine V de Y, l'homomorphisme canonique

$$
(6. 2. 4. 1)
$$

$$
\mathbf {H} ^ {n} (f ^ {- 1} (\mathrm{V}), \mathscr {K} ^ {\bullet}) \rightarrow \Gamma (\mathrm{V}, \mathscr {K} ^ {n} (f, \mathscr {K} ^ {\bullet}))
$$

est bijectif pour tout  $n \in Z$ .

La démonstration est la même que celle de (1.4.11), en utilisant (6.2.2), remplaçant $\mathcal{F}$ par $\mathcal{K}^{\bullet},\mathcal{K}^{\bullet}$ par $f_{*}(\mathcal{C}^{\bullet}(\mathfrak{U},\mathcal{K}^{\bullet}))$, $\mathcal{H}^{\bullet}(\mathcal{K}^{\bullet})$ par $\mathcal{H}^{\bullet}(f,\mathcal{K}^{\bullet})$, et notant que ce dernier est un $\mathcal{O}_{\mathrm{Y}}$-Module quasi-cohérent par (6.2.3).

Proposition (6.2.5). — Soient Y un préschéma localement noethérien, $f: X \to Y$ un morphisme propre, $\mathcal{K}^{\bullet}$ un complexe de $\mathcal{O}_{X}$-Modules tel que les $\mathcal{O}_{X}$-Modules $\mathcal{H}^{q}(\mathcal{H}^{\bullet})$ soient cohérents. Alors les $\mathcal{O}_{Y}$-Modules $\mathcal{H}^{n}(f, \mathcal{H}^{\bullet})$ sont cohérents.

La question étant locale sur Y, on peut se borner au cas où Y est noethérien et affine, et il s'agit donc, en vertu de (6.2.4), de prouver que les $\mathbf{H}^{n}(\mathbf{X},\mathcal{K}^{\bullet})$ sont des $\Gamma (\mathrm{Y},\mathcal{O}_{\mathrm{Y}})$-modules de type fini. On a alors $\mathbf{H}^{\bullet}(\mathbf{X},\mathcal{K}^{\bullet}) = \mathbf{H}^{\bullet}(\mathfrak{U},\mathcal{K}^{\bullet})$ (6.2.2), où l'on peut supposer que $\mathfrak{U}$ est fini, puisque X est quasi-compact. Les cochaînes de chaque complexe $\mathbf{C}^{\bullet}(\mathfrak{U},\mathcal{K}^{j})$ étant alternées par définition, il y a un entier $r > 0$ tel que $\mathbf{C}^{i}(\mathfrak{U},\mathcal{K}^{j}) = 0$ pour $i < 0$ et $i > r$; on en conclut (0, 11.3.3) que les deux suites spectrales du bicomplexe $\mathbf{C}^{\bullet}(\mathfrak{U},\mathcal{K}^{\bullet})$ sont birégulières. Comme les intersections des ensembles de $\mathfrak{U}$ sont des ouverts affines (I, 5.5.6), chaque foncteur $\mathcal{F}\to \mathbf{C}^{i}(\mathfrak{U},\mathcal{F})$ est exact dans la catégorie des $\mathcal{O}_{\mathrm{X}}$-Modules quasi-cohérents; donc $\mathrm{H}_{1}^{q}(\mathrm{C}^{i}(\mathfrak{U},\mathcal{K}^{\bullet})) = \mathrm{C}^{i}(\mathfrak{U},\mathcal{H}^{q}(\mathcal{K}^{\bullet}))$, et les termes $\mathrm{E}_2$ de la seconde suite spectrale de $\mathbf{C}^{\bullet}(\mathfrak{U},\mathcal{K}^{\bullet})$ sont donnés (0, 11.3.2) par

$$
^ {\prime \prime} \mathrm{E} _ {2} ^ {p q} = \mathrm{H} ^ {p} (\mathrm{C} ^ {\bullet} (\mathfrak {U}, \mathscr {H} ^ {q} (\mathscr {K} ^ {\bullet}))) = \mathrm{H} ^ {p} (\mathfrak {U}, \mathscr {H} ^ {q} (\mathscr {K} ^ {\bullet})) = \mathrm{H} ^ {p} (\mathrm{X}, \mathscr {H} ^ {q} (\mathscr {K} ^ {\bullet}))
$$

en vertu de (1.4.1); puisque $f$ est propre, ce sont des $\Gamma(\mathbf{Y},\mathcal{O}_{\mathbf{Y}})$-modules de type fini (3.2.1). La suite spectrale ${}^{\prime\prime}\mathrm{E}(\mathrm{C}^{*}(\mathfrak{U},\mathcal{K}^{*}))$ étant birégulière, on en déduit bien que les $\mathbf{H}^{n}(\mathbf{X},\mathcal{K}^{*})$ sont des $\Gamma(\mathbf{Y},\mathcal{O}_{\mathbf{Y}})$-modules de type fini (0, 11.1.8).

A fortiori, si $\mathcal{H}^{\bullet}$ est un complexe de $\mathcal{O}_{\mathrm{X}}$-Modules cohérents, les $\mathcal{O}_{\mathrm{Y}}$-Modules $\mathcal{H}^{n}(f,\mathcal{K}^{\bullet})$ sont cohérents sous les hypothèses de (6.2.5) relatives à Y et $f(\mathbf{0}_{\mathrm{I}},5.3.4)$.

(6.2.6) L'hypercohomologie $\mathcal{H}^{\bullet}(f, \mathcal{K}^{\bullet})$ est un foncteur cohomologique dans la catégorie des complexes de $\mathcal{O}_{\mathrm{X}}$-Modules limités inférieurement (0, 12.4.4). C'est un foncteur cohomologique dans la catégorie de tous les complexes de $\mathcal{O}_{\mathrm{X}}$-Modules lorsque le morphisme $f$ est quasi-compact et l'espace sous-jacent à X localement noethérien : en effet, il résulte alors de (G, II, 3.10.1) que $f_{*}$ permute aux limites inductives (la question étant locale sur Y), et l'on peut appliquer (0, 11.5.2).

Enfin, si $f$ est séparé, $\mathcal{H}^{\bullet}(f,\mathcal{H}^{\bullet})$ est un foncteur cohomologique dans la catégorie des complexes de $\mathcal{O}_{\mathrm{X}}$-Modules quasi-cohérents. C'est immédiat lorsque Y est affine, car alors X est un schéma, donc, en vertu de l'isomorphisme canonique (6.2.2), on est ramené à voir que $\mathcal{H}^{\bullet}\to\mathbf{H}^{\bullet}(\mathfrak{U},\mathcal{H}^{\bullet})$ est un foncteur cohomologique dans la catégorie des complexes de $\mathcal{O}_{\mathrm{X}}$-Modules quasi-cohérents, ce qui est immédiat puisque le foncteur $\mathcal{H}^{\bullet}\to\mathbf{C}^{\bullet}(\mathfrak{U},\mathcal{H}^{\bullet})$ est exact dans cette catégorie (I, 1.3.7). Dans le cas général, pour tout ouvert affine V

de Y,  $f^{-1}(Y)$  est un schéma, et pour appliquer ce qui précède, il suffit de vérifier que pour une suite exacte  $o \to H'' \to H' \to H''' \to o$  de complexes de  $O_{X}$ -Modules quasi-cohérents, l'homomorphisme  $\partial : \mathcal{H}^{n}(f, \mathcal{H}''')|V \to \mathcal{H}^{n+1}(f, \mathcal{H}')|V$  ne dépend pas du recouvrement ouvert affine U de  $f^{-1}(V)$  utilisé pour le définir. Mais cela résulte de ce que, si  $U'$  est un recouvrement ouvert affine plus fin que U, le diagramme

![](images/page_7_image_1.jpg)

d'isomorphismes canoniques est commutatif, ainsi que le diagramme

$$
\begin{array}{c c c} \mathbf {H} ^ {n} (\mathfrak {U}, \mathscr {K} ^ {\prime \prime \bullet}) & \stackrel {{\partial}} {{\to}} & \mathbf {H} ^ {n + 1} (\mathfrak {U}, \mathscr {K} ^ {\prime \bullet}) \\ \Bigg | _ {\downarrow} & & \Bigg | _ {\downarrow} \\ \mathbf {H} ^ {n} (\mathfrak {U} ^ {\prime}, \mathscr {K} ^ {\prime \prime \bullet}) & \stackrel {{\partial}} {{\to}} & \mathbf {H} ^ {n + 1} (\mathfrak {U} ^ {\prime}, \mathscr {K} ^ {\prime \bullet}) \end{array}
$$

Lorsque l'une des conditions précédentes est remplie et que $\mathcal{K}^{\bullet}\to\mathcal{K}^{\prime\bullet}$ est un homotopisme (6.1.4), l'isomorphisme correspondant $\mathcal{H}^{\bullet}(f,\mathcal{K}^{\bullet})\simeq\mathcal{H}^{\bullet}(f,\mathcal{K}^{\prime\bullet})$ est alors un isomorphisme de $\partial$-foncteurs (0, 11.4.4).

(6.2.7) Tout ce qui précède s'applique naturellement sans changement (sinon de notations) à un complexe $\mathcal{K}$. de $\mathcal{O}_{\mathrm{X}}$-Modules quasi-cohérents dont l'opérateur de dérivation est de degré — 1; il suffit de considérer le complexe $\mathcal{K}^{\bullet} = (\mathcal{K}^{i})$ où $\mathcal{K}^{i} = \mathcal{K}_{-}$; pour tout $i \in \mathbf{Z}$.

## 6.3. Hypertor de deux complexes de modules.

(6.3.1) Soient A un anneau commutatif, P., Q. deux complexes de A-modules dont les opérateurs de dérivation sont de degré —1; soit L.. (resp. M..) une résolution projective de Cartan-Eilenberg de P. (resp. Q.) (0, 11.6.1); L..⊗A M.. est alors (pour la somme des premiers degrés et la somme des seconds degrés) un bicomplexe (à opérateurs de dérivation de degré —1), dont l'homologie H.(L..⊗A M..) ne dépend pas des résolutions de Cartan-Eilenberg L., M.. choisies, et est par définition l'hyperhomologie du bifoncteur P.⊗A Q. en P. et Q. (0, 11.6.5). Nous poserons par définition

(6.3.1.1)

$$
\mathbf {T o r} _ {n} ^ {\mathrm{A}} \left(\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet}\right) = \mathrm{H} _ {n} \left(\mathrm{L} _ {\bullet \bullet} \otimes_ {\mathrm{A}} \mathrm{M} _ {\bullet \bullet}\right)\tag{141}
$$

et nous dirons que cet A-module est l'hypertor d'indice n des deux complexes P., Q.. On sait que dans la catégorie des complexes de A-modules limités inférieurement, les  $\mathbf{Tor}_{n}^{\mathrm{A}}(\mathrm{P.},\mathrm{Q.})$  forment un bifoncteur homologique en P., Q. (0, 11.6.5). En outre :

Proposition (6.3.2). — Le bifoncteur  $\mathbf{Tor}_{\bullet}^{\mathrm{A}}(\mathbf{P}_{\bullet},\mathbf{Q}_{\bullet})$ . est l'aboutissement commun de deux bifoncteurs spectraux 'E(P., Q.), ''E(P., Q.), dont les termes  $E_{2}$  sont

(6.3.2.1)

$$
^ \prime \mathrm{E} _ {p q} ^ {2} = \mathrm{H} _ {p} (\mathrm{Tor} _ {q} ^ {\mathrm{A}} (\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet}))\tag{6.3.2.2}
$$

$$
^ {\prime \prime} \mathrm{E} _ {p q} ^ {2} = \underset {q ^ {\prime} + q ^ {\prime \prime} = q} {\oplus} \mathrm{Tor} _ {p} ^ {\mathrm{A}} (\mathbf {H} _ {q ^ {\prime}} (\mathbf {P _ {\bullet}}), \mathbf {H} _ {q ^ {\prime \prime}} (\mathbf {Q _ {\bullet}}))
$$

où, dans (6.3.2.1),  $\operatorname{Tor}_{q}^{\mathrm{A}}(\mathbf{P}_{\bullet},\mathbf{Q}_{\bullet})$  désigne le bicomplexe formé des A-modules  $\operatorname{Tor}_{q}^{\mathrm{A}}(\mathbf{P}_{i},\mathbf{Q}_{j})$ . La suite spectrale (6.3.2.2) est toujours régulière; si P. et Q. sont limités inférieurement, ou si A est de dimension cohomologique finie, les deux suites spectrales (6.3.2.1) et (6.3.2.2) sont birégulières.

Cela résulte de (0, 11.6.5), car lorsque A est de dimension cohomologique finie n, tout A-module admet une résolution projective de longueur n (M, VI, 2.1).

Corollaire (6.3.3). — Soient P', Q'. deux complexes de A-modules,  $u: P_{\bullet} \to P'$ ,  $v: Q_{\bullet} \to Q'$ . deux homomorphismes de complexes. Si les homomorphismes H.(u): H.(P.) → H.(P'), H.(v): H.(Q.) → H.(Q') déduits respectivement de u et v sont bijectifs, alors l'homomorphisme  $\mathbf{Tor}_{\bullet}^{\mathrm{A}}(\mathrm{P}_{\bullet}, \mathrm{Q}_{\bullet}) \to \mathbf{Tor}_{\bullet}^{\mathrm{A}}(\mathrm{P}'_{\bullet}, \mathrm{Q}'_{\bullet})$  déduit de u et v est bijectif.

En effet, l'homomorphisme de suites spectrales $\mathbf{''E}(\mathbf{P}_{\bullet},\mathbf{Q}_{\bullet})\to \mathbf{''E}(\mathbf{P}_{\bullet}',\mathbf{Q}_{\bullet}')$ déduit de $u$ et $v$ est alors un isomorphisme pour les termes $\mathrm{E}_2$ et la conclusion résulte de ce que ces suites sont régulières en vertu de (6.3.2) (0, 11.1.5).

Proposition (6.3.4). — Soient P., Q. deux complexes de A-modules, limités inférieurement. Soit L.. (resp. M..) un bicomplexe formé de A-modules plats, tel que pour tout i, L$_{i}$, (resp. M$_{i}$,.) soit une résolution de P$_{i}$ (resp. Q$_{i}$). On a alors des isomorphismes canoniques.

$$
\mathbf {T o r} _ {\bullet} ^ {\mathrm{A}} \left(\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet}\right) \simeq \mathrm{H} _ {\bullet} \left(\mathrm{L} _ {\bullet \bullet} \otimes_ {\mathrm{A}} \mathrm{Q} _ {\bullet}\right) \simeq \mathrm{H} _ {\bullet} \left(\mathrm{P} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{M} _ {\bullet \bullet}\right) \simeq \mathrm{H} _ {\bullet} \left(\mathrm{L} _ {\bullet \bullet} \otimes_ {\mathrm{A}} \mathrm{M} _ {\bullet \bullet}\right) \tag {6.3.4.1}
$$

Cela résulte de (0, 11.6.5, (ii) et (iii)) et de la définition des A-modules plats. Remarques (6.3.5). — (i) Avec les notations de (6.3.1), les bicomplexes $L_{..} \otimes_{A} M_{..}$ et $M_{..} \otimes_{A} L_{..}$ sont canoniquement isomorphes, d'où un isomorphisme canonique $\mathbf{Tor}_{\cdot}^{A}(P_{\cdot}, Q_{\cdot}) \simeq \mathbf{Tor}_{\cdot}^{A}(Q_{\cdot}, P_{\cdot})$.

(ii) Si F et G sont deux A-modules, P. et Q. les complexes de A-modules réduits à F et G respectivement en degré o et nuls dans les autres degrés, alors deux résolutions projectives L., M. de F et G respectivement peuvent être considérées comme des résolutions de Cartan-Eilenberg de P. et Q. en les complétant par des zéros. On a par suite dans ce cas  $\mathbf{Tor}_{\bullet}^{\mathrm{A}}(\mathbf{P}_{\bullet}, \mathbf{Q}_{\bullet}) = \mathbf{Tor}_{\bullet}^{\mathrm{A}}(\mathbf{F}, \mathbf{G})$ .

Proposition (6.3.6). — Soient  $(\mathbf{P}_{\bullet}^{\lambda})$ ,  $(\mathbf{Q}_{\bullet}^{\mu})$  deux systèmes inductifs filtrants de complexes de A-modules ; on a un isomorphisme canonique

$$
\varinjlim_ {\lambda , \mu} \mathbf {T o r} _ {\bullet} ^ {A} (P _ {\bullet} ^ {\lambda}, Q _ {\bullet} ^ {\mu}) \xrightarrow {} \mathbf {T o r} _ {\bullet} ^ {A} (\varinjlim_ {\lambda} P _ {\bullet} ^ {\lambda}, \varinjlim_ {\mu} Q _ {\bullet} ^ {\mu})\tag{6.3.6.1}
$$

Posons  $P_{\bullet}=\varinjlim P^{\lambda}, Q_{\bullet}=\varinjlim Q^{\mu};$  par fonctorialité, il est clair que les  $\mathbf{Tor}_{\bullet}^{A}(P^{\lambda}, Q^{\mu})$  forment un système inductif et que les applications  $\mathbf{Tor}_{\bullet}^{A}(P^{\lambda}, Q^{\mu})\to\mathbf{Tor}_{\bullet}^{A}(P_{\bullet}, Q_{\bullet})$  déduites

des applications canoniques  $P^{\lambda} \rightarrow P_{\bullet}$ ,  $Q^{\mu} \rightarrow Q_{\bullet}$ , forment un système inductif d'homomorphismes, d'où un homomorphisme canonique (6.3.6.1), et plus généralement un homomorphisme canonique  $\lim_{\longrightarrow}''E(P^{\lambda}, Q^{\mu}) \rightarrow''E(P_{\bullet}, Q_{\bullet})$  dont (6.3.6.1) est l'homomorphisme des aboutissements. En outre, la suite spectrale  $''E(P_{\bullet}, Q_{\bullet})$  est régulière (6.3.2), et il en est de même de la suite spectrale  $\lim_{\longrightarrow}''E(P^{\lambda}, Q^{\mu})$ , comme il résulte des définitions (0, 11.1.7) et de la démonstration de (0, 11.3.3); pour démontrer que (6.3.6.1) est bijectif, il suffit donc (0, 11.1.5) de prouver que l'homomorphisme

$$
\lim _ {\rightarrow} ^ {\prime \prime} \mathrm{E} (\mathrm{P} _ {\bullet} ^ {\lambda}, \mathrm{Q} _ {\bullet} ^ {\mu}) \rightarrow^ {\prime \prime} \mathrm{E} (\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet})\tag{6.3.6.2}
$$

est bijectif pour les termes  $E^{2}$ . Comme le foncteur H. commute à la limite inductive des complexes de modules, on est finalement ramené à prouver que pour deux systèmes inductifs filtrants  $(\mathbf{F}^{\lambda})$ ,  $(\mathbf{G}^{\mu})$  de A-modules, l'homomorphisme canonique

$$
\varinjlim_ {\lambda , \mu} (\operatorname{Tor} _ {\bullet} ^ {A} (F ^ {\lambda}, G ^ {\mu})) \rightarrow \operatorname{Tor} _ {\bullet} ^ {A} (\varinjlim_ {\lambda} F ^ {\lambda}, \varinjlim_ {\mu} G ^ {\mu})
$$

est bijectif. Pour cela, considérons pour chaque  $F^{\lambda}$  la résolution libre canonique

$$
\mathrm{L} _ {\bullet} ^ {\lambda}: \dots \rightarrow \mathrm{L} _ {i + 1} ^ {\lambda} \rightarrow \mathrm{L} _ {i} ^ {\lambda} \rightarrow \dots \rightarrow \mathrm{L} _ {1} ^ {\lambda} \rightarrow \mathrm{L} _ {0} ^ {\lambda} \rightarrow 0
$$

où  $L_{0}^{\lambda}$  est le A-module des combinaisons linéaires formelles d'éléments de  $F^{\lambda}$  et  $L_{i+1}^{\lambda}$  le A-module des combinaisons linéaires formelles d'éléments de Ker  $(\mathbf{L}_{i}^{\lambda}\to\mathbf{L}_{i-1}^{\lambda})$ ; on vérifie immédiatement que les  $L_{\bullet}^{\lambda}$  forment un système inductif de complexes, et si l'on pose  $F=\varinjlim_{\lambda}F^{\lambda}, L_{i}=\varinjlim_{\lambda}L_{i}^{\lambda}$ , les  $L_{i}$  forment une résolution  $L_{\bullet}$  de F, le foncteur  $\varinjlim$  étant exact; en outre, les  $L_{i}$ , limites inductives de A-modules libres, sont plats  $(0_{I},6.1.2)$ . On considère de même pour chaque  $\mu$  la résolution libre canonique  $M_{\bullet}^{\mu}$  de  $G^{\mu}$ , et  $M_{\bullet}=\varinjlim M_{\bullet}^{\mu}$  est une résolution plate de  $G=\varinjlim G^{\mu}$ . On a alors  $\operatorname{Tor}_{\bullet}^{A}(\varinjlim F^{\lambda},\varinjlim G^{\mu})=H_{\bullet}(L_{\bullet}\otimes_{A}M_{\bullet})$  en vertu de (6.3.5) et (6.3.4); mais  $H_{\bullet}(L_{\bullet}\otimes_{A}M_{\bullet})=\varinjlim_{\lambda,\mu}H_{\bullet}(L_{\bullet}^{\lambda}\otimes_{A}M_{\bullet}^{\mu})$  puisque  $H_{\bullet}$  commute aux limites inductives de complexes de modules; comme  $H_{\bullet}(L_{\bullet}^{\lambda}\otimes_{A}M_{\bullet}^{\mu})=\operatorname{Tor}_{\bullet}^{A}(F^{\lambda},G^{\mu})$ , cela termine la démonstration.

Lorsqu'on suppose qu'il existe $i_{0}$ tel que $\mathrm{P}_{i}^{\lambda}=\mathrm{Q}_{i}^{\mu}=0$ pour $i<i_{0}$ quels que soient $\lambda$ et $\mu$, on démontre de la même manière que l'homomorphisme canonique

$$
\lim _ {\rightarrow} ^ {\prime} \mathrm{E} (\mathrm{P} _ {\bullet} ^ {\lambda}, \mathrm{Q} _ {\bullet} ^ {\mu}) \rightarrow^ {\prime} \mathrm{E} (\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet})\tag{6.3.6.3}
$$

est bijectif.

Proposition (6.3.7). — Supposons P. et Q. limités inférieurement. Si le complexe P. est formé de A-modules plats, on a un A-isomorphisme canonique de  $\partial$ -foncteurs en Q.

$$
\mathbf {T o r} _ {\bullet} ^ {\mathrm{A}} \left(\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet}\right) \simeq \mathrm{H} _ {\bullet} \left(\mathrm{P} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{Q} _ {\bullet}\right).\tag{6.3.7.1}
$$

En effet, la suite spectrale (6.3.2.1) est birégulière et dégénérée, et l'existence de l'isomorphisme (6.3.7.1) résulte de (0, 11.1.6). En outre, en calculant l'hypertor à partir d'une résolution projective de Cartan-Eilenberg de P. (6.3.4), on voit aussitôt que l'isomorphisme ainsi défini est un isomorphisme de $\partial$-foncteurs en Q.

143

(6.3.8) Soit $\rho: A \to A'$ un homomorphisme d'anneaux. Nous nous proposons de définir un A-homomorphisme fonctoriel de degré o canoniquement associé à $\rho$:

$$
\rho_ {\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet}}: \mathbf {T o r} _ {\bullet} ^ {\mathrm{A}} (\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet}) \rightarrow \mathbf {T o r} _ {\bullet} ^ {\mathrm{A} ^ {\prime}} (\mathrm{P} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime}, \mathrm{Q} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime}).\tag{6.3.8.1}
$$

Pour cela, considérons une résolution de Cartan-Eilenberg projective L. de P.; considérons d'autre part une résolution de Cartan-Eilenberg projective L'. de P.⊗A' Nous allons voir qu'on peut définir un A'-homomorphisme de complexes L.⊗A'→L', déterminé à homotopie près. En effet, la construction de L.. est entièrement déterminée lorsqu'on se donne (arbitrairement) pour chaque i, une résolution projective (X$_{ij}^{B}$)j≥0 de B$_{i}$(P.) et une résolution projective (X$_{ij}^{H}$)j≥0 de H$_{i}$(P.), qui sont respectivement égales à B$_{i}^{I}$(L..) et H$_{i}^{I}$(L..)); on en déduit successivement Z$_{i}^{I}$(L..)=H$_{i}^{I}$(L..)+B$_{i}^{I}$(L..), puis L$_{i,\cdot}$=Z$_{i}^{I}$(L..)+B$_{i-1}^{I}$(L..). Cela étant, X$_{i,\cdot}^{B}$⊗A' n'est plus en général une résolution de P.⊗A' , mais est encore un complexe formé de A'-modules projectifs, et il y a donc un A'-homomorphisme X$_{i,\cdot}^{B}$⊗A'→B$_{i}^{I}$(L'. ) compatible avec les augmentations, et déterminé à homotopie près (M, V, I.I). On a de même un A'-homomorphisme X$_{i,\cdot}^{H}$⊗A'→H$_{i}^{I}$(L'. ) déterminé à homotopie près, d'où l'on déduit, par la construction rappelée plus haut, un A'-homomorphisme L$_{i,\cdot}$⊗A'→L'. pour tout i; ces homomorphismes (pour i∈Z) sont compatibles avec les opérateurs de dérivation L$_{i,\cdot}$→L$_{i-1,\cdot}$ et les analogues pour L', en vertu de la même construction, et ils constituent donc le A'-homomorphisme L.⊗A'→L'. cherché.

Pour définir (6.3.8.1), il suffit alors de considérer de même une résolution de Cartan-Eilenberg projective  $M_{\bullet\bullet}$  (resp.  $M_{\bullet\bullet}^{\prime}$ ) de  $Q_{\bullet}$  (resp.  $Q_{\bullet}\otimes_{A}A^{\prime}$ ), et un A'-homomorphisme  $M_{\bullet\bullet}\otimes_{A}A^{\prime}\to M_{\bullet\bullet}^{\prime}$ . On déduit de ces homomorphismes un A'-homomorphisme  $(\mathbf{L}_{\bullet\bullet}\otimes_{A}A^{\prime})\otimes_{A^{\prime}}(\mathbf{M}_{\bullet\bullet}\otimes_{A}A^{\prime})\to L_{\bullet\bullet}^{\prime}\otimes_{A^{\prime}}M_{\bullet\bullet}^{\prime}$ , puis par composition un A-homomorphisme de bicomplexes  $L_{\bullet\bullet}\otimes_{A}M_{\bullet\bullet}\to L_{\bullet\bullet}^{\prime}\otimes_{A^{\prime}}M_{\bullet\bullet}^{\prime}$ , et en passant à l'homologie on obtient (6.3.8.1), qui est bien défini puisqu'il provient d'un morphisme de complexes défini à homotopie près.

Si $\rho': A' \to A''$ est un second homomorphisme d'anneaux, et $\rho'': A \to A''$ l'homomorphisme composé $\rho' \circ \rho$, il est clair que $\rho_{P_*, Q_*}'' = \rho_{P_*, Q_*'}^{\prime} \circ \rho_{P_*, Q_*}$, où

$$
\mathrm{P} _ {\bullet} ^ {\prime} = \mathrm{P} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime}, \quad \mathrm{Q} _ {\bullet} ^ {\prime} = \mathrm{Q} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime}.
$$

Notons encore que le morphisme de bicomplexes  $L_{\bullet\bullet}\otimes_{A}M_{\bullet\bullet}\rightarrow L^{\prime}_{\bullet\bullet}\otimes_{A^{\prime}}M^{\prime}_{\bullet\bullet}$  considéré ci-dessus définit des morphismes fonctoriels (en P. et Q.) de suites spectrales

$$
{ } ^ { \prime } \mathrm{E} _ { p q } ^ { r } ( \mathrm{P} _ { \bullet } , \mathrm{Q} _ { \bullet } ) \rightarrow { } ^ { \prime } \mathrm{E} _ { p q } ^ { r } ( \mathrm{P} _ { \bullet } \otimes _ { \mathrm{A} } \mathrm{A} ^ { \prime } , \mathrm{Q} _ { \bullet } \otimes _ { \mathrm{A} } \mathrm{A} ^ { \prime } ) \text {~ e~ t~ ~ } { } ^ { \prime \prime } \mathrm{E} _ { p q } ^ { r } ( \mathrm{P} _ { \bullet } , \mathrm{Q} _ { \bullet } ) \rightarrow { } ^ { \prime \prime } \mathrm{E} _ { p q } ^ { r } ( \mathrm{P} _ { \bullet } \otimes _ { \mathrm{A} } \mathrm{A} ^ { \prime } , \mathrm{Q} _ { \bullet } \otimes _ { \mathrm{A} } \mathrm{A} ^ { \prime } ) ,
$$

indépendants des résolutions de Cartan-Eilenberg considérées, et ayant aussi la propriété de transitivité précédente.

Proposition (6.3.9). — Soit $\rho: A \to A'$ un homomorphisme d'anneaux tel que $A'$ soit un A-module plat. On a alors des isomorphismes canoniques fonctoriels

$$
\mathbf {T o r} _ {\bullet} ^ {\mathrm{A} ^ {\prime}} \left(\mathrm{P} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime}, \mathrm{Q} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime}\right) \stackrel {{\sim}} {{\rightarrow}} \mathbf {T o r} _ {\bullet} ^ {\mathrm{A}} \left(\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet}\right) \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime}\tag{6.3.9.1}
$$

$$
\left. ^ {\prime} \mathrm{E} (\mathrm{P} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime}, \mathrm{Q} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime}) \right. \stackrel {{\sim}} {{\rightarrow}} ^ {\prime} \mathrm{E} (\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet}) \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime}\tag{6.3.9.2}
$$

$$
\left. ^ {\prime \prime} \mathrm{E} \left(\mathrm{P} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime}, \mathrm{Q} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime}\right) \stackrel {{\sim}} {{\rightarrow}} ^ {\prime \prime} \mathrm{E} \left(\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet}\right) \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime}. \right.
$$

144

145

En effet, vu l'exactitude du foncteur  $M\otimes_{A}A'$  en M,  $L_{..}\otimes_{A}A'$  et  $M_{..}\otimes_{A}A'$  sont alors des résolutions projectives de Cartan-Eilenberg de  $P_{.}\otimes_{A}A'$  et  $Q_{.}\otimes_{A}A'$  respectivement, d'où la conclusion.

(6.3.10) Soit $\rho: A \to A'$ un homomorphisme d'anneaux; pour tout complexe $P'$ de $A'$-modules, $P_{\bullet[\rho]}'$ est un complexe de A-modules; en outre, l'application identique $P_{\bullet[\rho]}' \to P'$ peut être considérée comme composée des applications canoniques

$$
\mathrm{P} _ {\bullet [ \rho ]} ^ {\prime} \rightarrow \mathrm{P} _ {\bullet [ \rho ]} ^ {\prime} \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime} \stackrel {{\mu}} {{\rightarrow}} \mathrm{P} _ {\bullet} ^ {\prime},
$$

où $\mu$ est le A'-homomorphisme $\mu(x\otimes a')=a'x$. Si Q' est un second complexe de A'-modules, on a donc des homomorphismes canoniques fonctoriels de degré o

$$
\mathbf {T o r} _ {\bullet} ^ {A} \left(P _ {[ p ]} ^ {\prime}, Q _ {[ c ]} ^ {\prime}\right)\rightarrow \mathbf {T o r} _ {\bullet} ^ {A ^ {\prime}} \left(P _ {[ p ]} ^ {\prime} \otimes_ {A} A ^ {\prime}, Q _ {[ p ]} ^ {\prime} \otimes_ {A} A ^ {\prime}\right)\rightarrow \mathbf {T o r} _ {\bullet} ^ {A ^ {\prime}} \left(P _ {,} ^ {\prime}, Q _ {,} ^ {\prime}\right) \tag {6.3.10.1}
$$

où la première flèche est le A-homomorphisme défini dans (6.3.8) et la seconde se déduit des A'-homomorphismes  $P_{\bullet[\rho]}\otimes_{A}A'\to P_{\bullet}'$  et  $Q_{\bullet[\rho]}\otimes_{A}A'\to Q_{\bullet}'$  par fonctorialité. On a des homomorphismes analogues pour les suites spectrales de (6.3.2), et des propriétés évidentes de transitivité, que nous laissons au lecteur le soin d'énoncer.

Proposition (6.3.11). — Soit $\rho: A \to A'$ un homomorphisme d'anneaux faisant de $A'$ un A-module plat. Pour tout complexe $P'$ de $A'$-modules et tout complexe $Q$, de A-modules limités inférieurement, on a un isomorphisme canonique fonctoriel

$$
\mathbf {T o r} _ {\bullet} ^ {\mathrm{A}} \left(\mathrm{P} _ {\bullet [ \rho ]} ^ {\prime}, \mathrm{Q} _ {\bullet}\right) \simeq \mathbf {T o r} _ {\bullet} ^ {\mathrm{A} ^ {\prime}} \left(\mathrm{P} _ {\bullet} ^ {\prime}, \mathrm{Q} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime}\right).\tag{6.3.II.I}
$$

En effet, si  $M_{\bullet}$  est une résolution projective de Cartan-Eilenberg de  $Q_{\bullet}$,  $M_{\bullet}\otimes_{A}A'$  est une résolution projective de Cartan-Eilenberg de  $Q_{\bullet}\otimes_{A}A'$, et l'on a, à un isomorphisme canonique près,  $P'_{[\sigma]}\otimes_{A}M_{\bullet}=P'\otimes_{A'}(M_{\bullet}\otimes_{A}A')$; la conclusion résulte de (6.3.4).

Remarque (6.3.12). — Soit (A$^{\lambda}$) un système inductif filtrant d'anneaux, et soient (P$^{\lambda}$), (Q$^{\lambda}$) deux systèmes inductifs de complexes de (A$^{\lambda}$)-modules; on a alors un isomorphisme canonique généralisant (6.3.6.1)

$$
\lim _ {\rightarrow} \mathbf {T o r} _ {\bullet} ^ {A ^ {\lambda}} (P _ {\bullet} ^ {\lambda}, Q _ {\bullet} ^ {\lambda}) \simeq \mathbf {T o r} _ {\bullet} ^ {A} (P _ {\bullet}, Q _ {\bullet})\tag{6.3.12.1}
$$

$\mathrm{ou}\quad \mathrm{A} = \varinjlim \mathrm{A}^{\lambda},\quad \mathrm{P}_{\bullet} = \varinjlim \mathrm{P}_{\bullet}^{\lambda},\quad \mathrm{Q}_{\bullet} = \varinjlim \mathrm{Q}_{\bullet}^{\lambda}. \quad \text{Une fois définis les homomorphismes}$

$$
\mathbf {T o r} _ {\bullet} ^ {\mathrm{A} ^ {\lambda}} (\mathrm{P} _ {\bullet} ^ {\lambda}, \mathrm{Q} _ {\bullet} ^ {\lambda}) \rightarrow \mathbf {T o r} _ {\bullet} ^ {\mathrm{A} ^ {\mu}} (\mathrm{P} _ {\bullet} ^ {\mu}, \mathrm{Q} _ {\bullet} ^ {\mu})
$$

pour $\lambda \leqslant \mu$, à l'aide de (6.3.10), la démonstration est celle de (6.3.6).

Proposition (6.3.13). — Soient S une partie multiplicative de A, P. et Q. deux complexes de A-modules, dans lesquels les homothéties définies par les éléments de S soient bijectives, de sorte que, si  $A' = S^{-1}A$ , P. et Q. sont formés de A'-modules. Alors on a un isomorphisme canonique  $\mathbf{Tor}_{\bullet}^{A}(P_{\bullet}, Q_{\bullet}) \stackrel{\sim}{\to} \mathbf{Tor}_{\bullet}^{A'}(P_{\bullet}, Q_{\bullet})$ .

En effet, l'hypothèse entraîne que les homomorphismes canoniques  $P_{\bullet}\rightarrow P_{\bullet}\otimes_{A}A'$ ,  $Q_{\bullet}\rightarrow Q_{\bullet}\otimes_{A}A'$  sont bijectifs. D'autre part, la fonctorialité de l'hypertor montre que tout  $s\in S$  définit une homothétie bijective dans  $\operatorname{Tor}_{\bullet}^{A}(P_{\bullet},Q_{\bullet})$ , et par suite

$$
\mathbf {T o r} _ {\bullet} ^ {\mathrm{A}} \left(\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet}\right)\rightarrow \mathbf {T o r} _ {\bullet} ^ {\mathrm{A}} \left(\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet}\right) \otimes_ {\mathrm{A}} \mathrm{A} ^ {\prime}
$$

est aussi un homomorphisme bijectif. Comme A' est un A-module plat, la conclusion résulte de (6.3.9), et on a de même des isomorphismes canoniques pour les suites spectrales.

## 6.4. Foncteurs hypertor locaux de complexes de Modules quasi-cohérents : cas des schémas affines.

(6.4.1) Soient S un schéma affine d'anneau A, X, Y deux S-schémas affines d'anneaux B, C respectivement, de sorte que B et C sont des algèbres sur A. Tout complexe $\mathcal{P}_{\bullet}$ (resp. $\mathcal{Q}_{\bullet}$) de $\mathcal{O}_{X}$-Modules (resp. $\mathcal{O}_{Y}$-Modules) quasi-cohérents est de la forme $\widetilde{\mathrm{P}}_{\bullet}$ (resp. $\widetilde{\mathrm{Q}}_{\bullet}$), où P. (resp. Q.) est un complexe de B-modules (resp. C-modules) (I, 1.3.7 et 1.3.8). On peut évidemment considérer P. et Q. comme des complexes de A-modules et former les $\mathbf{Tor}_{n}^{\mathrm{A}}(\mathrm{P}_{\bullet}, \mathrm{Q}_{\bullet})$; en outre, en vertu du caractère bifonctoriel de $\mathbf{Tor}_{n}^{\mathrm{A}}(\mathrm{P}_{\bullet}, \mathrm{Q}_{\bullet})$, les A-algèbres B et C opèrent dans ce A-module, et ces opérations en font un (B, C)-bimodule, ou, ce qui revient au même, un module sur $\mathrm{B} \otimes_{\mathrm{A}} \mathrm{C} = \mathrm{A}(\mathrm{X} \times_{\mathrm{S}} \mathrm{Y})$. On a donc défini de la sorte un $\mathcal{O}_{\mathrm{X} \times_{\mathrm{S}} \mathrm{Y}}$-Module quasi-cohérent

$$
\mathfrak {T o r} _ {n} ^ {\mathcal {O} _ {\mathrm{S}}} (\mathscr {P} _ {\bullet}, \mathscr {Q} _ {\bullet}) = (\mathbf {T o r} _ {n} ^ {\mathrm{A}} (\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet})) ^ {\sim}\tag{6.4.1.1}
$$

que l'on appelle l'hypertor local d'indice n des complexes $\mathcal{P}_{\bullet}$ et $\mathcal{Q}_{\bullet}$ et que l'on note aussi $\mathfrak{Vor}_{n}^{\mathrm{S}}(\mathcal{P}_{\bullet},\mathcal{Q}_{\bullet})$.

Lemme (6.4.2). — Avec les notations de (6.4.1), supposons que l'anneau A soit de la forme  $R^{-1}A'$ , où  $A'$  est un anneau et R une partie multiplicative de  $A'$ . Soit  $S' = Spec(A')$ , de sorte que X et Y peuvent être considérés comme des  $S'$ -préschémas et que l'on a  $X \times_{S'} Y = X \times_{S} Y(I, I.6.2 \text{ et } 3.2.4)$ . On a alors  $\mathcal{Gor}_{\bullet}^{S'}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet}) = \mathcal{Gor}_{\bullet}^{S}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$ .

Cela résulte de la formule (6.4.1.1) et de (6.3.13).

(6.4.3) Avec les notations et hypothèses de (6.4.1), soient $\mathcal{F} = \widetilde{\mathrm{F}}$ un $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent, $\mathcal{G} = \widetilde{\mathrm{G}}$ un $\mathcal{O}_{\mathrm{Y}}$-Module quasi-cohérent; considérant $\mathcal{F}$ et $\mathcal{G}$ comme des complexes de Modules, on notera $\mathcal{T}or_{n}^{\mathrm{C}}_{\mathrm{s}}(\mathcal{F},\mathcal{G})$ ou $\mathcal{T}or_{n}^{\mathrm{S}}(\mathcal{F},\mathcal{G})$ leur hypertor d'indice $n$; il résulte de (6.3.5 (ii)) que l'on a

$$
\mathcal {T} o r _ {n} ^ {\mathfrak {C} _ {\mathrm{s}}} (\mathcal {F}, \mathcal {G}) = (\operatorname{Tor} _ {n} ^ {\mathrm{A}} (\mathrm{F}, \mathrm{G})) ^ {\sim}.\tag{6.4.3.1}
$$

Revenons alors au cas général de deux complexes de Modules quasi-cohérents $\mathcal{P}_{\bullet}$, $\mathcal{Q}_{\bullet}$. Les formules (6.4.1.1) et (6.4.3.1) montrent, compte tenu de la prop. (6.3.2), que $\mathfrak{Gor}_{\bullet}^{\mathrm{S}}(\mathcal{P}_{\bullet},\mathcal{Q}_{\bullet})$ est l'aboutissement de deux suites spectrales ' $\mathcal{E}(\mathcal{P}_{\bullet},\mathcal{Q}_{\bullet})$," $\mathcal{E}(\mathcal{P}_{\bullet},\mathcal{Q}_{\bullet})$, dont les termes $\mathrm{E}_2$ sont donnés par

(6.4.3.2)

$$
\begin{array}{r l} & {^ {\prime} \mathcal {E} _ {p q} ^ {2} = \mathcal {H} _ {p} (\mathcal {T o r} _ {q} ^ {\mathrm{S}} (\mathcal {P} _ {\bullet}, \mathcal {Q} _ {\bullet}))} \\ & {^ {\prime \prime} \mathcal {E} _ {p q} ^ {2} = \underset {q ^ {\prime} + q ^ {\prime \prime} = q} {\bigoplus} \mathcal {T o r} _ {p} ^ {\mathrm{S}} (\mathcal {H} _ {q ^ {\prime}} (\mathcal {P} _ {\bullet}), \mathcal {H} _ {q ^ {\prime \prime}} (\mathcal {Q} _ {\bullet}))} \end{array}\tag{6.4.3.3}
$$

où  $\mathcal{Tor}_{q}^{\mathrm{S}}(\mathcal{P}_{\bullet},\mathcal{Q}_{\bullet})$  est le bicomplexe de  $O_{X\times_{s}Y}$ -Modules quasi-cohérents  $\mathcal{Tor}_{q}^{\mathrm{S}}(\mathcal{P}_{i},\mathcal{Q}_{j})$ .
(6.4.4) Considérons maintenant deux autres schémas affines  $\mathbf{X}^{(1)}=\operatorname{Spec}(\mathbf{B}^{(1)})$ ,  $\mathbf{Y}^{(1)}=\operatorname{Spec}(\mathbf{C}^{(1)})$ , où  $B^{(1)}$  et  $C^{(1)}$  sont des A-algèbres, et supposons donnés deux

S-morphismes $u: \mathbf{X}^{(1)} \to \mathbf{X}, v: \mathbf{Y}^{(1)} \to \mathbf{Y}$, correspondant à des A-homomorphismes $\varphi: \mathbf{B} \to \mathbf{B}^{(1)}, \psi: \mathbf{C} \to \mathbf{C}^{(1)}$. Considérons les complexes $u^*(\mathcal{P}_.) = (\mathcal{P}_. \otimes_{\mathbf{B}} \mathbf{B}^{(1)})^\sim$ de $\mathcal{O}_{\mathbf{X}^{(1)}}$-Modules, $v^*(\mathcal{Q}_.) = (\mathbf{Q}_. \otimes_{\mathbf{C}} \mathbf{C}^{(1)})^\sim$ de $\mathcal{O}_{\mathbf{Y}^{(1)}}$-Modules. Les A-homomorphismes canoniques

$$
\mathbf {P} _ {\bullet} \rightarrow \mathbf {P} _ {\bullet} \otimes_ {\mathrm{B}} \mathbf {B} ^ {(1)}, \quad \mathbf {Q} _ {\bullet} \rightarrow \mathbf {Q} _ {\bullet} \otimes_ {\mathrm{C}} \mathbf {C} ^ {(1)}
$$

donnent par fonctorialité un A-homomorphisme

$$
\mathbf {T o r} _ {\bullet} ^ {\mathrm{A}} \left(\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet}\right)\rightarrow \mathbf {T o r} _ {\bullet} ^ {\mathrm{A}} \left(\mathrm{P} _ {\bullet} \otimes_ {\mathrm{B}} \mathrm{B} ^ {(1)}, \mathrm{Q} _ {\bullet} \otimes_ {\mathrm{C}} \mathrm{C} ^ {(1)}\right);
$$

en outre, toujours par fonctorialité, cet homomorphisme est en fait un homomorphisme de  $(\mathrm{B}\otimes_{\mathrm{A}}\mathrm{C})$ -modules. D'où l'on conclut que l'on a défini ainsi un  $(u\times_{\mathrm{s}}v)$ -morphisme

$$
\theta : \mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} (\mathscr {P} _ {\bullet}, \mathscr {Q} _ {\bullet}) \rightarrow \mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} (u ^ {*} (\mathscr {P} _ {\bullet}), v ^ {*} (\mathscr {Q} _ {\bullet}))\tag{6.4.4.1}
$$

et par suite, un homomorphisme de $\mathcal{O}_{\mathrm{X}^{(1)}\times_{\mathrm{s}}\mathrm{Y}^{(1)}}$-Modules

$$
\theta^ {\sharp}: (u \times_ {S} v) ^ {*} (\mathfrak {C o r} _ {\bullet} ^ {S} (\mathscr {P} _ {\bullet}, \mathscr {Q} _ {\bullet})) \rightarrow \mathfrak {C o r} _ {\bullet} ^ {S} (u ^ {*} (\mathscr {P} _ {\bullet}), v ^ {*} (\mathscr {Q} _ {\bullet}))\tag{6.4.4.2}
$$

qui est évidemment un morphisme de bi-∂-foncteurs dans les catégories de Modules quasi-cohérents limités inférieurement.

L'homomorphisme (6.4.4.2) n'est pas nécessairement bijectif; toutefois :

Lemme (6.4.5). — Avec les notations de (6.4.4), supposons que u et v soient des immersions ouvertes ; alors l'homomorphisme (6.4.4.2) est bijectif.

Identifions $\mathbf{X}^{(1)}$ (resp. $\mathbf{Y}^{(1)}$) à un ouvert de $\mathbf{X}$ (resp. $\mathbf{Y}$); $\mathbf{X}^{(1)}$ (resp. $\mathbf{Y}^{(1)}$) est alors réunion d'ouverts de la forme $\mathbf{D}(f)$ (resp. $\mathbf{D}(g)$), où $f \in \mathbf{B}$ (resp. $g \in \mathbf{C}$), et les préschémas induits $\mathbf{D}(\varphi(f))$ et $\mathbf{D}(f)$ (resp. $\mathbf{D}(\psi(g))$ et $\mathbf{D}(g)$) sont isomorphes. Il suffira de prouver le lemme lorsque $\mathbf{X}^{(1)}$ (resp. $\mathbf{Y}^{(1)}$) est de la forme $\mathbf{D}(f)$ (resp. $\mathbf{D}(g)$); en effet, si ce point est établi, et si l'on revient au cas général, il suffira de prouver que la restriction de $\theta^{\#}$ à chaque ouvert $\mathbf{D}(f) \times_{\mathbb{S}} \mathbf{D}(g)$ est un isomorphisme; or, si $u_1: \mathbf{D}(f) \to \mathbf{X}^{(1)}$, $v_1: \mathbf{D}(g) \to \mathbf{Y}^{(1)}$ sont les injections canoniques, la restriction précédente n'est autre que $(u_1 \times_{\mathbb{S}} v_1)^*(\theta^{\#})$; mais il est immédiat, en vertu des définitions (6.4.4) et de $(\mathbf{0}_1, 4.4.8)$, qu'en la composant avec l'homomorphisme canonique

$$
(u _ {1} \times_ {\mathrm{S}} v _ {1}) ^ {*} (\mathcal {C o r} _ {\bullet} ^ {\mathrm{S}} (u ^ {*} (\mathcal {P} _ {\bullet}), v ^ {*} (\mathcal {Q} _ {\bullet})) \to \mathcal {C o r} _ {\bullet} ^ {\mathrm{S}} (u ^ {\prime *} (\mathcal {P} _ {\bullet}), v ^ {\prime *} (\mathcal {Q} _ {\bullet}))\tag{6.4.5.1}
$$

où $u' = u \circ u_1$ et $v' = v \circ v_1$, on obtient l'homomorphisme canonique

$$
(u ^ {\prime} \times_ {S} v ^ {\prime}) ^ {*} (\mathcal {C o r} _ {\bullet} ^ {S} (\mathcal {P} _ {\bullet}, \mathcal {Q} _ {\bullet})) \rightarrow \mathcal {C o r} _ {\bullet} ^ {S} (u ^ {\prime *} (\mathcal {P} _ {\bullet}), v ^ {\prime *} (\mathcal {Q} _ {\bullet}))\tag{6.4.5.2}
$$

et si l'on sait que (6.4.5.1) et (6.4.5.2) sont des isomorphismes, il en résultera qu'il en est de même de $(u_{1} \times_{\mathrm{S}} v_{1})^{*}(\theta^{\#})$.

Supposons donc que $\mathbf{X}^{(1)} = \mathbf{D}(f)$ et $\mathbf{Y}^{(1)} = \mathbf{D}(g)$, de sorte que $\mathbf{B}^{(1)} = \mathbf{B}_f$ et $\mathbf{C}^{(1)} = \mathbf{C}_g$; $u^*(\mathcal{P}_{\bullet})$ (resp. $v^*(2_{\bullet})$) s'identifie alors à $(\mathbf{P}_{\bullet})_{f}^{\sim}$ (resp. $(\mathbf{Q}_{\bullet})_{g}^{\sim}$); d'autre part, $\mathbf{X}^{(1)} \times {}_{\mathrm{S}} \mathbf{Y}^{(1)}$ s'identifie au sous-schéma ouvert $\mathbf{D}(f \otimes g)$ de $\mathbf{X} \times {}_{\mathrm{S}} \mathbf{Y} = \operatorname{Spec}(\mathbf{B} \otimes_{\mathrm{A}} \mathbf{C})$ (II, 4.3.2.4); il s'agit de prouver que l'homomorphisme

(6.4.5.3)

$$
\left(\mathbf {T o r} _ {\bullet} ^ {\mathrm{A}} \left(\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet}\right)\right) _ {f \otimes g} \rightarrow \mathbf {T o r} _ {\bullet} ^ {\mathrm{A}} \left(\left(\mathrm{P} _ {\bullet}\right) _ {f}, \left(\mathrm{Q} _ {\bullet}\right) _ {g}\right)\tag{147}
$$

déduit par fonctorialité des homomorphismes canoniques  $\mathrm{P}_{\bullet}\to(\mathrm{P}_{\bullet})_{f},\mathrm{Q}_{\bullet}\to(\mathrm{Q}_{\bullet})_{g}$ , est bijectif. Or  $(\mathbf{0}_{\mathrm{I}},\mathrm{I}.6.\mathrm{I})$ , on peut écrire  $(\mathrm{P}_{\bullet})_{f}=\lim_{\longrightarrow}\mathrm{P}_{\bullet}^{(n)}$ , où les  $\mathrm{P}_{\bullet}^{(n)}$  sont tous des complexes de B-modules identiques à  $P_{\bullet}$ , l'application  $\mathrm{P}_{\bullet}^{(m)}\to\mathrm{P}_{\bullet}^{(n)}$  pour  $m\leqslant n$  étant la multiplication par  $f^{n-m}$ ; on a un résultat analogue pour  $Q_{\bullet}$  en remplaçant f par g; d'autre part, il est clair que l'homomorphisme

$$
\mathbf {T o r} _ {\bullet} ^ {\mathrm{A}} \left(\mathrm{P} _ {\bullet} ^ {(m)}, \mathrm{Q} _ {\bullet} ^ {(m)}\right)\rightarrow \mathbf {T o r} _ {\bullet} ^ {\mathrm{A}} \left(\mathrm{P} _ {\bullet} ^ {(n)}, \mathrm{Q} _ {\bullet} ^ {(n)}\right)
$$

correspondant aux homomorphismes $\mathbf{P}_{\bullet}^{(m)}\to\mathbf{P}_{\bullet}^{(n)}$ et $\mathbf{Q}_{\bullet}^{(m)}\to\mathbf{Q}_{\bullet}^{(n)}$ est par définition la multiplication par $(f\otimes g)^{n-m}$. La conclusion résulte alors de $(\mathbf{0}_{\mathrm{I}},\mathrm{I}.6.\mathrm{I})$ appliqué au premier membre de (6.4.5.3) et de (6.3.6).

(6.4.6) Avec les notations de (6.4.4), on définit de même des homomorphismes canoniques de foncteurs spectraux

$$
\left\{\begin{array}{l}(u \times_ {\mathrm{S}} v) ^ {*} (^ {\prime} \mathcal {E} (\mathcal {P} _ {\bullet}, \mathcal {Q} _ {\bullet})) \rightarrow {} ^ {\prime} \mathcal {E} (u ^ {*} (\mathcal {P} _ {\bullet}), v ^ {*} (\mathcal {Q} _ {\bullet}))\\(u \times_ {\mathrm{S}} v) ^ {*} (^ {\prime \prime} \mathcal {E} (\mathcal {P} _ {\bullet}, \mathcal {Q} _ {\bullet})) \rightarrow {} ^ {\prime \prime} \mathcal {E} (u ^ {*} (\mathcal {P} _ {\bullet}), v ^ {*} (\mathcal {Q} _ {\bullet}))\end{array}\right.\tag{6.4.6.1}
$$

et le raisonnement de (6.4.5) montre que lorsque $u$ et $v$ sont des immersions ouvertes, les homomorphismes (6.4.6.1) sont $\text{bijectifs}$: en effet, compte tenu de (6.3.6.2) et (6.3.6.3), il prouve que c'est un isomorphisme pour les termes $E^2$, et (6.4.5) montre que c'est un isomorphisme pour les aboutissements; on conclut donc à l'aide de (0, 11.1.2) et (0, 11.2.4).

## 6.5. Foncteurs hypertor locaux de complexes de Modules quasi-cohérents : cas général.

(6.5.1) Considérons maintenant un préschéma S quelconque et deux S-préschémas quelconques X, Y; soit $\mathcal{P}_{\bullet}$ (resp. 2.) un complexe de $\mathcal{O}_{\mathrm{X}}$-Modules (resp. $\mathcal{O}_{\mathrm{Y}}$-Modules) quasi-cohérents. Posons $Z = X \times_{S} Y$; nous allons définir des $\mathcal{O}_{\mathrm{Z}}$-Modules quasi-cohérents $\mathfrak{Gor}_{n}^{\mathrm{S}}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$ dits hypertor locaux de $\mathcal{P}_{\bullet}$ et 2. qui se réduiront à ceux déjà définis dans (6.4) lorsque S, X et Y sont affines.

Lorsque $\mathcal{P}_{\bullet}$ et $\mathcal{Q}_{\bullet}$ se réduisent respectivement à leurs termes de degré o, $\mathcal{F}$ et $\mathcal{G}$, (les autres étant nuls), on écrira $\mathcal{Tor}_{n}^{\mathrm{S}}(\mathcal{F},\mathcal{G})$ au lieu de $\mathcal{Cor}_{n}^{\mathrm{S}}(\mathcal{P}_{\bullet},\mathcal{Q}_{\bullet})$.

(6.5.2) Supposons d'abord S affine, et soient  $(\mathbf{X}_{\lambda})$ ,  $(\mathbf{Y}_{\mu})$  des recouvrements de X et Y respectivement par des ouverts affines; alors les  $Z_{\lambda\mu} = X_{\lambda} \times_{S} Y_{\mu}$  forment un recouvrement ouvert affine de Z. Posons  $P_{\lambda\bullet} = P_{\bullet} | X_{\lambda}, Q_{\mu\bullet} = Q_{\bullet} | Y_{\mu}$ ; nous avons donc pour tout couple  $(\lambda, \mu)$  un  $O_{Z_{\lambda\mu}}$ -Module quasi-cohérent  $\mathcal{F}_{\lambda\mu} = \mathcal{C}or_{n}^{\mathrm{S}}(\mathcal{P}_{\lambda\bullet}, Q_{\mu\bullet})$ , et il faut montrer que les  $F_{\lambda\mu}$  vérifient la condition de recollement  $(\mathbf{0}_{\mathrm{I}}, 3.3.1)$ . Pour cela, il suffit de vérifier que pour tout ouvert affine  $U \subset X_{\lambda} \cap X_{\lambda'}$  (resp.  $V \subset Y_{\mu} \cap Y_{\mu'}$ ), les restrictions de  $F_{\lambda\mu}$  et de  $F_{\lambda'\mu'}$  à  $U \times_{S} V$  sont canoniquement isomorphes; mais cela découle aussitôt de l'existence d'isomorphismes canoniques de ces restrictions sur  $\mathcal{C}or_{n}^{\mathrm{S}}(\mathcal{P}_{\bullet} | U, Q_{\bullet} | V)$  (6.4.5). En outre, il résulte aussitôt de cette définition et de (6.4.5) que le  $O_{Z}$ -Module ainsi défini ne dépend pas (à un isomorphisme près) des recouvrements ouverts  $(\mathbf{X}_{\lambda})$ ,  $(\mathbf{Y}_{\mu})$  consi-

dérés; nous le noterons donc $\mathcal{C}or_{n}^{\mathrm{S}}(\mathcal{P}_{\bullet},\mathcal{Q}_{\bullet})$; il résulte enfin de (6.4.5) que pour toute partie ouverte U (resp. V) de X (resp. Y), la restriction de $\mathcal{C}or_{n}^{\mathrm{S}}(\mathcal{P}_{\bullet},\mathcal{Q}_{\bullet})$ à $U\times_{\mathrm{s}}V$ est canoniquement isomorphe à $\mathcal{C}or_{n}^{\mathrm{S}}(\mathcal{P}_{\bullet}|U,\mathcal{Q}_{\bullet}|V)$.

(6.5.3) Passons maintenant au cas général où S est quelconque, et soit  $(\mathbf{S}_{\alpha})$  un recouvrement de S formé d'ouverts affines; désignons par  $X_{\alpha}$  (resp.  $Y_{\alpha}$ ) l'image réciproque de  $S_{\alpha}$  dans X (resp. Y); il faut encore prouver que les faisceaux  $\mathcal{G}or_{n}^{\mathrm{S}_{\alpha}}(\mathcal{P}_{\cdot}|X_{\alpha},2_{\cdot}|Y_{\alpha})=\mathcal{G}_{\alpha}$  vérifient la condition de recollement. Il suffit de définir, pour tout ouvert affine T contenu dans  $S_{\alpha}\cap S_{\beta}$, des isomorphismes canoniques des restrictions de  $G_{\alpha}$  et  $G_{\beta}$  à  $U\times_{s}V$  (en désignant par U et V les images réciproques de T dans X et Y respectivement) sur  $\mathcal{G}or_{n}^{\mathrm{T}}(\mathcal{P}_{\cdot}|U,2_{\cdot}|V)$; on peut, en outre, se borner au cas où T s'écrit à la fois  $D(f_{\alpha})$  et  $D(f_{\beta})$,  $f_{\alpha}$  (resp.  $f_{\beta}$) étant une section de  $O_{s}$  au-dessus de  $S_{\alpha}$  (resp.  $S_{\beta}$); mais alors  $\mathcal{G}or_{n}^{\mathrm{T}}(\mathcal{P}_{\cdot}|U,2_{\cdot}|V)$  est canoniquement isomorphe à  $\mathcal{G}or_{n}^{\mathrm{S}_{\alpha}}(\mathcal{P}_{\cdot}|U,2_{\cdot}|V)$  d'une part, à  $\mathcal{G}or_{n}^{\mathrm{S}_{\beta}}(\mathcal{P}_{\cdot}|U,2_{\cdot}|V)$  d'autre part, en vertu de (6.4.2); comme on vient de définir des isomorphismes canoniques de  $G_{\alpha}$  sur  $\mathcal{G}or_{n}^{\mathrm{S}_{\alpha}}(\mathcal{P}_{\cdot}|U,2_{\cdot}|V)$  et de  $G_{\beta}$  sur  $\mathcal{G}or_{n}^{\mathrm{S}_{\beta}}(\mathcal{P}_{\cdot}|U,2_{\cdot}|V)$  (6.5.2), cela achève de définir le  $O_{Z}$-Module  $\mathcal{G}or_{n}^{\mathrm{S}}(\mathcal{P}_{\cdot},2_{\cdot})$. En outre, pour toute partie ouverte U (resp. V) de X (resp. Y),  $\mathcal{G}or_{n}^{\mathrm{S}}(\mathcal{P}_{\cdot}|U,2_{\cdot}|V)$  est canoniquement isomorphe à la restriction de  $\mathcal{G}or_{n}^{\mathrm{S}}(\mathcal{P}_{\cdot},2_{\cdot})$  à  $U\times_{s}V$.

Il est immédiat que l'on a ainsi défini (dans les catégories de complexes de Modules quasi-cohérents limités inférieurement) un bi-∂-foncteur  $\mathcal{Tor}_{\bullet}^{\mathrm{S}}(\mathcal{P}_{\bullet},\mathcal{Q}_{\bullet})$  à valeurs dans la catégorie des  $O_{Z}$ -Modules, car il est clair que la question est locale sur X, Y et S, en vertu de (6.4.5) et de la remarque que (6.4.4.2) est un morphisme de bi-∂-foncteurs. On notera que si  $P_{\bullet}$  et 2. sont réduits respectivement à leurs termes de degré o, F et G,  $\mathcal{Tor}_{0}^{\mathrm{S}}(\mathcal{F},\mathcal{G})$  n'est autre, en vertu de (6.4.1.1), que le produit tensoriel externe  $F\otimes_{S}G$  défini dans (I, 9.1.2); cela résulte en effet de (I, 9.1.3).

(6.5.4) Il résulte de la construction précédente et des remarques faites dans (6.4.6) que $\mathfrak{Gor}^{\mathrm{S}}(\mathcal{P}_{\bullet},\mathcal{Q}_{\bullet})$ est l'aboutissement de deux foncteurs spectraux, $^\prime \mathcal{E}(\mathcal{P}_{\bullet},\mathcal{Q}_{\bullet})$, $\mathcal{E}(\mathcal{P}_{\bullet},\mathcal{Q}_{\bullet})$, de termes $\mathrm{E}_2$ égaux à

(6.5.4.1)

$$
\begin{array}{r l} & {\mathcal {E} _ {p q} ^ {2} = \mathcal {H} _ {p} (\mathcal {T o r} _ {q} ^ {\mathrm{S}} (\mathcal {P} _ {\bullet}, \mathcal {Q} _ {\bullet})} \\ & {\mathcal {E} _ {p q} ^ {2} = \bigoplus_ {q ^ {\prime} + q ^ {\prime \prime} = q} \mathcal {T o r} _ {p} ^ {\mathrm{S}} (\mathcal {H} _ {q ^ {\prime}} (\mathcal {P} _ {\bullet}), \mathcal {H} _ {q ^ {\prime \prime}} (\mathcal {Q} _ {\bullet}))} \end{array}\tag{6.5.4.2}
$$

La suite spectrale (6.5.4.2) est toujours régulière; les deux suites spectrales sont birégulières si $\mathcal{P}$, et $\mathcal{Q}$, sont limités inférieurement. Un autre cas où les deux suites précédentes sont birégulières est le suivant :

(6.5.5) Nous dirons que sur un espace topologique T un faisceau d'anneaux A est de dimension cohomologique  $\leqslant n$  si, pour tout  $t\in T$  l'anneau  $A_{t}$  est de dimension cohomologique  $\leqslant n$ ; on dira alors aussi que l'espace annelé (T, A) est de dimension cohomologique  $\leqslant n$ . On dira qu'un faisceau d'anneaux (resp. un espace annelé) est de dimension cohomologique finie s'il existe un entier n tel qu'il soit de dimension cohomologique  $\leqslant n$ . On notera que si les  $A_{t}$  sont des anneaux locaux (commutatifs) noethériens,

dire qu'ils sont de dimension cohomologique $\leqslant n$ signifie qu'ils sont réguliers et de dimension (de Krull) $\leqslant n$ ($\mathbf{0}_{\mathrm{IV}}$, 17.3.1). Avec la terminologie de la théorie de la dimension que nous introduirons au chap. IV, il revient au même de dire qu'un préschéma localement noethérien T est de dimension cohomologique $\leqslant n$, ou de dire qu'il est régulier ($\mathbf{0}_{\mathrm{I}}$, 4.1.4) et de dimension $\leqslant n$; cela signifie que pour tout ouvert affine U de T, l'anneau $\Gamma(\mathrm{U}, \mathcal{O}_{\mathrm{T}})$ est de dimension cohomologique $\leqslant n$ ($\mathbf{0}_{\mathrm{IV}}$, 17.2.6). Cela étant, cette dernière remarque, jointe à (6.3.2), prouve que si S est localement noethérien et de dimension cohomologique finie, les suites spectrales ' $\mathcal{E}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$ et '' $\mathcal{E}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$ sont birégulières.

Il est clair que $\mathfrak{Tor}_{\bullet}^{\mathrm{S}}(\mathcal{P}_{\bullet},\mathcal{Q}_{\bullet})$ se transforme en $\mathfrak{Tor}_{\bullet}^{\mathrm{S}}(\mathcal{Q}_{\bullet},\mathcal{P}_{\bullet})$ (à un isomorphisme près) par l'isomorphisme canonique de $\mathbf{X}\times_{\mathrm{S}}\mathbf{Y}$ sur $\mathbf{Y}\times_{\mathrm{S}}\mathbf{X}$.

Proposition (6.5.6). — Soit  $(\mathcal{P}_{\alpha_{\bullet}})$  un système inductif filtrant de complexes de  $O_{X}$ -Modules quasi-cohérents ; il existe alors un isomorphisme canonique

$$
\varinjlim (\mathcal {C o r} _ {\bullet} ^ {\mathrm{S}} (\mathcal {P} _ {\alpha_ {\bullet}}, \mathcal {2} _ {\bullet})) \stackrel {{\sim}} {{\to}} \mathcal {C o r} _ {\bullet} ^ {\mathrm{S}} (\varinjlim \mathcal {P} _ {\alpha_ {\bullet}}, \mathcal {2} _ {\bullet}).\tag{6.5.6.1}
$$

La question étant locale sur S, X et Y, on peut supposer S, X, Y affines et la proposition se réduit alors à (6.3.6).

Remarques (6.5.7). — (i) Considérons en particulier le cas où S=X=Y, P. et 2. étant donc deux complexes de $\mathcal{O}_{\mathrm{S}}$-Modules quasi-cohérents; alors les $\mathfrak{Tor}_{n}^{\mathrm{S}}(\mathcal{P}_{\cdot},\mathcal{Q}_{\cdot})$ sont des $\mathcal{O}_{\mathrm{S}}$-Modules quasi-cohérents; en outre, pour tout point $z\in\mathrm{S}$, il résulte de (6.5.6) que l'on a un isomorphisme canonique

$$
(\mathfrak {C o r} _ {n} ^ {\mathrm{S}} (\mathcal {P} _ {\bullet}, \mathcal {Q} _ {\bullet})) _ {z} \stackrel {{\sim}} {{\to}} \mathbf {T o r} _ {n} ^ {\mathcal {O} _ {z}} ((\mathcal {P} _ {\bullet}) _ {z}, (\mathcal {Q} _ {\bullet}) _ {z})\tag{6.5.7.1}
$$

car la question est locale et on est ramené au cas des modules, en vertu de (6.4.1.1).
(ii) On peut généraliser la définition des hypertor au cas de deux complexes de $\mathcal{O}_{\mathrm{X}}$-Modules $\mathcal{P}_{\bullet}$, $\mathcal{Q}_{\bullet}$ sur un même espace annelé ($\mathrm{X}$, $\mathcal{O}_{\mathrm{X}}$); pour tout ouvert U de X, posons en effet $\mathrm{A}(\mathrm{U}) = \Gamma(\mathrm{U}, \mathcal{O}_{\mathrm{X}})$, $\mathrm{P}_{\bullet}(\mathrm{U}) = \Gamma(\mathrm{U}, \mathcal{P}_{\bullet})$, $\mathrm{Q}_{\bullet}(\mathrm{U}) = \Gamma(\mathrm{U}, \mathcal{Q}_{\bullet})$; les $\mathrm{A}(\mathrm{U})$-modules $\mathbf{T}\mathbf{o}\mathbf{r}_{n}^{\mathrm{A}(\mathrm{U})}(\mathrm{P}_{\bullet}(\mathrm{U}), \mathrm{Q}_{\bullet}(\mathrm{U}))$ forment alors un préfaisceau sur X, et l'on désigne par $\mathcal{C}\mathbf{o}\mathbf{r}_{n}^{\mathrm{X}}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$ le $\mathcal{O}_{\mathrm{X}}$-Module associé à ce préfaisceau. Lorsque X est un préschéma, il résulte de (6.3.12) que ce $\mathcal{O}_{\mathrm{X}}$-Module est canoniquement isomorphe à l'hypertor défini ci-dessus. Nous ne développerons pas davantage cette généralisation.

Proposition (6.5.8). — Soient X, Y deux S-préschémas, $\mathcal{F}$ (resp. $\mathcal{G}$) un $\mathcal{O}_{\mathrm{X}}$-Module (resp. un $\mathcal{O}_{\mathrm{Y}}$-Module) quasi-cohérent. Si $\mathcal{F}$ ou $\mathcal{G}$ est S-plat, on a $\operatorname{Tor}_{n}^{\mathrm{S}}(\mathcal{F},\mathcal{G}) = 0$ pour $n\neq 0$.

La question étant locale sur X et Y, on peut supposer X, Y et S affines, d'anneaux respectifs B, C, A, et $\mathcal{F}=\widetilde{\mathrm{M}}$, $\mathcal{G}=\widetilde{\mathrm{N}}$, M (resp. N) étant un B-module (resp. un C-module). Supposons par exemple que $\mathcal{F}$ soit S-plat, ce qui signifie que pour tout $s\in\mathrm{S}$, $\mathrm{M}_{s}$ est un $\mathrm{A}_{s}$-module plat ($\mathbf{0}_{\mathrm{I}}$, 6.7.1); par suite M est un A-module plat ($\mathbf{0}_{\mathrm{I}}$, 6.3.3), et l'on sait que $\operatorname{Tor}_{n}^{\mathrm{A}}(\mathrm{M},\mathrm{N})=\mathrm{o}$ pour $n>0$ et pour tout C-module N ($\mathbf{0}_{\mathrm{I}}$, 6.1.1), d'où la conclusion par (6.4.1.1).

Corollaire (6.5.9). — Soient X, Y deux S-préschémas, P. (resp. 2.) un complexe de

$\mathcal{O}_{\mathrm{X}}$-Modules (resp. de $\mathcal{O}_{\mathrm{Y}}$-Modules) quasi-cohérents limité inférieurement. Supposons que tous les $\mathcal{P}_{i}$ soient S-plats. Alors il existe un isomorphisme canonique de $\partial$-foncteurs en $\mathcal{Q}$.

$$
\mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} (\mathcal {P} _ {\bullet}, \mathcal {Q} _ {\bullet}) \stackrel {{\sim}} {{\to}} \mathcal {H} _ {\bullet} (\mathcal {P} _ {\bullet} \otimes_ {\mathrm{S}} \mathcal {Q} _ {\bullet}).\tag{6.5.9.1}
$$

Ce n'est autre que (6.3.7) lorsque S, X, Y sont affines; on passe de là au cas général par les raisonnements de (6.5.2) et (6.5.3).

Corollaire (6.5.10). — Supposons que X soit plat sur S (0$_{I}$, 6.7.1), que P$_{\bullet}$ et 2$_{\bullet}$ soient limités inférieurement et que tous les P$_{i}$ soient des O$_{X}$-Modules localement libres (non nécessairement de type fini). Alors l'homomorphisme (6.5.9.1) est bijectif.

En effet, l'hypothèse de (6.5.9) est remplie, la platitude étant une propriété ponctuelle sur X par définition et toute somme directe de modules plats étant un module plat  $(\mathbf{0}_{\mathrm{I}}, 6.1.2)$ .

Proposition (6.5.11). — Soient X', Y' deux S-préschémas, $f: \mathbf{X} \to \mathbf{X}'$, $g: \mathbf{Y} \to \mathbf{Y}'$ deux S-morphismes affines. Soit $\mathcal{P}_{\bullet}$ (resp. 2.) un complexe de $\mathcal{O}_{\mathbf{X}}$-Modules (resp. de $\mathcal{O}_{\mathbf{Y}}$-Modules) quasi-cohérents; on a alors un isomorphisme canonique fonctoriel

$$
(f \times_ {\mathrm{S}} g) _ {*} (\mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} (\mathscr {P} _ {\bullet}, \mathscr {Q} _ {\bullet})) \stackrel {{\sim}} {{\to}} \mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} (f _ {*} (\mathscr {P} _ {\bullet}), g _ {*} (\mathscr {Q} _ {\bullet})).\tag{6.5.11.1}
$$

Comme $f$ et $g$ sont affines, $f_{*}(\mathcal{P}_{\bullet})$ et $g_{*}(\mathcal{Q}_{\bullet})$ sont des complexes de Modules quasi-cohérents (II, 1.2.6), et si l'on pose $Z' = X' \times_{S} Y'$, les deux membres de (6.5.11.1) sont des $\mathcal{O}_{Z'}$-Modules quasi-cohérents (6.5.1); on se ramène aisément au cas où S, $X'$ et $Y'$ sont affines; mais alors il en est de même par hypothèse de X et Y et la vérification résulte aussitôt de (6.4.1.1) et (I, 1.6.3).

Remarque (6.5.12). — Soient X', Y' deux S-préschémas et supposons que X' soit S-plat; soient X un sous-préschéma fermé de X', i : X → X' l'injection canonique, P. (resp. 2.) un complexe de Ox-Modules (resp. de Oy'-Modules) quasi-cohérents, limité inférieurement. Soit enfin L'. une résolution de i\*(P.) formé de Ox'-Modules localement libres, telle que tout point de X' ait un voisinage ouvert affine U pour lequel L'j., |U soit une résolution libre de i\*(Pj)| U pour tout j. On a alors un isomorphisme canonique

$$
(i \times_ {\mathrm{SI}}) _ {*} (\mathfrak {C o r} _ {\bullet} ^ {\mathbb {S}} (\mathcal {P} _ {\bullet}, \mathcal {Q} _ {\bullet})) \simeq \mathscr {H} _ {\bullet} (\mathscr {L} _ {\bullet \bullet} ^ {\prime} \otimes_ {\mathrm{S}} \mathcal {Q} _ {\bullet}).\tag{6.5.12.1}
$$

Si S, X', Y' sont affines et si $\mathcal{L}_{j,\cdot}^{\prime}$ est une résolution libre de $i_{*}(\mathcal{P}_{j})$ pour tout $j$, on est ramené, en vertu de (6.5.11), au cas où $\mathbf{X}' = \mathbf{X}$ est S-plat, et il suffit d'appliquer (6.3.4). Dans le cas général, on définit localement l'isomorphisme (6.5.12.1), et il s'agit de vérifier que cette définition donne bien un isomorphisme global. Pour cela, il faut se reporter à la définition du premier isomorphisme (6.3.4.1) qui provient d'un isomorphisme de suites spectrales (0, 11.6.5 et 11.5.3), obtenu lui-même à partir d'un morphisme de bicomplexes $\mathrm{L}_{\cdot \cdot} \to \mathrm{L}_{\cdot \cdot}^{\prime \prime}$, où $\mathrm{L}_{\cdot \cdot}$ est la résolution donnée de P., $\mathrm{L}_{\cdot \cdot}^{\prime \prime}$ une résolution projective de P. dans la catégorie des complexes de A-modules limités

inférieurement (cf. (0, 11.5.2.2)); notre assertion résulte de ce que l'isomorphisme (6.3.4.1) ne dépend pas de la résolution projective L'' choisie, en vertu de l'existence d'un homotopisme entre deux telles résolutions (M, V, 1.2).

Proposition (6.5.13). — Soient X, Y deux S-préschémas, et supposons vérifiée l'une des conditions suivantes :

(i) X et  $Z = X \times_{S} Y$  sont localement noethériens et X est plat sur S.

(ii) S et X sont localement noethériens et Y est de type fini sur S.

Soit $\mathcal{P}_{\bullet}$ (resp. $\mathcal{Q}_{\bullet}$) un complexe de $\mathcal{O}_{\mathrm{X}}$-Modules (resp. de $\mathcal{O}_{\mathrm{Y}}$-Modules) quasi-cohérents, limité inférieurement. On suppose en outre que, pour tout $n$, $\mathcal{H}_{n}(\mathcal{P}_{\bullet})$ (resp. $\mathcal{H}_{n}(\mathcal{Q}_{\bullet})$) est un $\mathcal{O}_{\mathrm{X}}$-Module (resp. un $\mathcal{O}_{\mathrm{Y}}$-Module) de type fini. Alors les $\operatorname{Cor}_{n}^{\mathrm{S}}(\mathcal{P}_{\bullet}, \mathcal{Q}_{\bullet})$ sont des $\mathcal{O}_{\mathrm{Z}}$-Modules cohérents.

Comme $\mathcal{P}_{\bullet}$ et $\mathcal{Q}_{\bullet}$ sont limités inférieurement, la suite spectrale ${}^{\prime \prime}\mathcal{E}(\mathcal{P}_{\bullet},\mathcal{Q}_{\bullet})$ est birégulière (6.5.4), et en vertu de (0, 11.1.8), il suffit (puisque dans les deux cas (i), (ii), Z est localement noethérien) de prouver que les termes ${}^{\prime \prime}\mathcal{E}_{pq}^{2}$ sont cohérents. L'hypothèse sur les $\mathcal{H}_{n}(\mathcal{P}_{\bullet})$ et $\mathcal{H}_{n}(\mathcal{Q}_{\bullet})$ et l'expression (6.5.4.2) des ${}^{\prime \prime}\mathcal{E}_{pq}^{2}$ montrent donc que la proposition est équivalente à son cas particulier correspondant à $\mathcal{P}_{\bullet}$ et $\mathcal{Q}_{\bullet}$ réduits à leurs termes de degré o, autrement dit à son

Corollaire (6.5.14). — Supposons vérifiée l'une des conditions (i), (ii) de (6.5.13), et soit $\mathcal{F}$ (resp. $\mathcal{G}$) un $\mathcal{O}_{\mathrm{X}}$-Module (resp. un $\mathcal{O}_{\mathrm{Y}}$-Module) quasi-cohérent de type fini; alors les $\mathcal{Tor}_{n}^{\mathrm{S}}(\mathcal{F},\mathcal{G})$ sont des $\mathcal{O}_{\mathrm{Z}}$-Modules cohérents.

La question étant locale sur X et Y, on peut supposer S, X, Y affines.

(i) Sous les hypothèses de (i), S, X et Z sont noethériens. Il existe donc une résolution localement libre $\mathcal{L}$. de $\mathcal{F}$ formée de $\mathcal{O}_{\mathrm{X}}$-Modules de type fini (I, 1.3.7); comme X est plat sur S, il résulte de (6.3.4) que l'on a $\operatorname{Tor}_{n}^{\mathrm{S}}(\mathcal{F}, \mathcal{G}) = \mathcal{H}_{n}(\mathcal{L}_{\bullet} \otimes_{\mathrm{S}} \mathcal{G})$; or, les $\mathcal{L}_{i} \otimes_{\mathrm{S}} \mathcal{G}$ sont des $\mathcal{O}_{\mathrm{Z}}$-Modules quasi-cohérents de type fini (I, 9.1.1), donc cohérents. On en conclut que $\mathcal{H}_{n}(\mathcal{L}_{\bullet} \otimes_{\mathrm{S}} \mathcal{G})$ est cohérent ($0_{\mathrm{I}}, 5.3.4$).

(ii) Supposons maintenant vérifiées les conditions (ii). Comme l'anneau A(Y) est quotient d'une A(S)-algèbre de polynômes à un nombre fini d'indéterminées (I, 6.3.3), Y est un sous-S-préschéma fermé d'un S-préschéma affine Y', plat et de type fini sur S; Y' étant noethérien (I, 6.3.7), il existe une résolution localement libre M. de j\*(G) par des OY'-Modules de type fini (j: Y→Y' étant l'injection canonique); en vertu de (6.5.12), Torn(S(F, G) est l'image réciproque par 1×j du OZ'-Module Hn(F⊗sM.) (où Z'=X×sY'); on voit comme dans (i) que les F⊗sMi sont des OZ-Modules cohérents, et l'on en tire encore la conclusion par (01, 5.3.4).

(6.5.15) La théorie développée ci-dessus pour deux complexes $\mathcal{P}_{\bullet}$, $\mathcal{Q}_{\bullet}$ de faisceaux quasi-cohérents sur deux S-préschémas X, Y se généralise sans peine au cas où l'on considère un nombre fini quelconque de S-préschémas $\mathbf{X}^{(i)}$ ($1 \leqslant i \leqslant m$) et sur chaque $\mathbf{X}^{(i)}$ un complexe $\mathcal{P}_{\bullet}^{(i)}$ de $\mathcal{O}_{\mathrm{X}^{(i)}}$-Modules quasi-cohérents; si $Z = X^{(1)} \times_{S} X^{(2)} \times_{S} \ldots \times_{S} X^{(m)}$, on définit ainsi un $\mathcal{O}_{Z}$-Module quasi-cohérent $\mathcal{Cor}_{q}^{\mathrm{S}}(\mathcal{P}_{\bullet}^{(1)}, \mathcal{P}_{\bullet}^{(2)}, \ldots, \mathcal{P}_{\bullet}^{(m)})$. Nous laissons au lecteur le soin de développer la théorie dans ce cas général et nous nous bornerons à écrire, pour référence ultérieure, le terme $E_{2}$ de la seconde suite spectrale (régulière) dont l'aboutissement est $\mathcal{Cor}_{\bullet}^{\mathrm{S}}(\mathcal{P}_{\bullet}^{(1)}, \mathcal{P}_{\bullet}^{(2)}, \ldots, \mathcal{P}_{\bullet}^{(m)})$:

153

$$
{ } ^ { \prime \prime } \mathcal { E } _ { p q } ^ { 2 } = \bigoplus _ { q _ { 1 } + q _ { 2 } + \dots + q _ { m } = q } \mathcal { T o r } _ { p } ^ { S } ( \mathcal { H } _ { q _ { 1 } } ( \mathcal { P } _ { \bullet } ^ { ( 1 ) } ) , \dots , \mathcal { H } _ { q _ { m } } ( \mathcal { P } _ { \bullet } ^ { ( m ) } ) ) .\tag{6.5.15.1}
$$

Nous étudierons dans (6.8) les suites spectrales d'associativité auxquelles donnent lieu ces foncteurs hypertor d'un nombre quelconque de complexes.

## 6.6. Foncteurs hypertor globaux de complexes de Modules quasi-cohérents et suites spectrales de Künneth : cas de la base affine.

(6.6.1) Considérons un schéma affine $S = \text{Spec}(A)$ et deux S-schémas quasi-compacts $X^{(i)}$ ($i = 1, 2$); soit $\mathcal{P}_{\bullet}^{(i)}$ un complexe de $\mathcal{O}_{X^{(i)}}$-Modules quasi-cohérents, limité inférieurement, dont l'opérateur de dérivation est de degré —$I$ ($i = 1, 2$). Considérons d'autre part un recouvrement fini $\mathfrak{U}^{(i)} = (U_{\alpha}^{(i)})$ de $X^{(i)}$ par des ouverts affines; soit $X = X^{(1)} \times _S X^{(2)}$, qui est un S-schéma quasi-compact ($I$, 5.5.1 et 6.6.4), et soit $\mathfrak{U} = \mathfrak{U}^{(1)} \times _S \mathfrak{U}^{(2)}$ le recouvrement de $X$ formé des ouverts affines $U_{\alpha}^{(1)} \times _S U_{\beta}^{(2)}$. Pour tout couple d'entiers $p \leqslant 0$, $q \in Z$, le groupe des $(-p)$-cochaînes alternées $C^{-p}(\mathfrak{U}^{(i)}, \mathcal{P}_{q}^{(i)})$ du recouvrement $\mathfrak{U}^{(i)}$ à coefficients dans le faisceau $\mathcal{P}_{q}^{(i)}$ (G, II, 5.1) est un A-module; pour $p > 0$, on posera $C^p(\mathfrak{U}^{(i)}, \mathcal{P}_{q}^{(i)}) = 0$; on a ainsi défini un bicomplexe $C^\bullet(\mathfrak{U}^{(i)}, \mathcal{P}_{\bullet}^{(i)})$ de A-modules, dont les deux opérateurs de dérivation sont de degré —$I$. Il résulte des définitions ($0, 12.1.2$) que le A-module d'homologie $H_n(C^\bullet(\mathfrak{U}^{(i)}, \mathcal{P}_{\bullet}^{(i)}))$ de ce bicomplexe (considéré à l'ordinaire comme un complexe simple pour le degré total) n'est autre que le A-module d'hypercohomologie $H^{-n}(\mathfrak{U}^{(i)}, \mathcal{P}^{(i)\bullet})$ où $\mathcal{P}^{(i)\bullet}$ est le complexe à opérateur de dérivation de degré +$I$ obtenu en prenant $\mathcal{P}_{-q}^{(i)}$ pour composante de degré $q$; par abus de notation, nous l'écrirons $H^{-n}(\mathfrak{U}^{(i)}, \mathcal{P}_{\bullet}^{(i)})$. Il résulte alors de (6.2.2) que ce A-module est canoniquement isomorphe au A-module d'hypercohomologie $H^{-n}(X^{(i)}, \mathcal{P}^{(i)\bullet})$, que nous écrirons de même $H^{-n}(X^{(i)}, \mathcal{P}_{\bullet}^{(i)})$; il ne dépend donc pas du recouvrement fini $\mathfrak{U}^{(i)}$ choisi.

(6.6.2) Nous allons appliquer aux deux bicomplexes de A-modules

$$
\mathrm{L} _ {\bullet \bullet} ^ {(i)} = \mathrm{C} ^ {\bullet} (\mathfrak {U} ^ {(i)}, \mathscr {P} _ {\bullet} ^ {(i)})\tag{\((i = \mathrm{I},2)\}
$$

et au bifoncteur covariant $\mathbf{L}_{\bullet \bullet}^{(1)}\otimes_{\mathrm{A}}\mathbf{L}_{\bullet \bullet}^{(2)}$ en ces deux bicomplexes, la théorie générale de l'hyperhomologie des foncteurs par rapport aux bicomplexes (0, 11.7.4). Comme les cochaînes considérées sont alternées et les recouvrements $\mathfrak{U}^{(i)}$ finis, on notera que les modules $\mathbf{C}^{-p}(\mathfrak{U}^{(i)},\mathcal{P}_{q}^{(i)})$ ne sont $\neq 0$ que pour un nombre fini (indépendant de $q$) de valeurs de $p$, et en particulier les deux degrés de chacun des $\mathbf{L}_{\bullet \bullet}^{(i)}$ sont limités inférieurement. Nous désignerons par $\mathbf{Tor}_{n}^{\mathrm{A}}(\mathbf{L}_{\bullet \bullet}^{(1)},\mathbf{L}_{\bullet \bullet}^{(2)})$ ou $\mathbf{Tor}_{n}^{\mathrm{S}}(\mathfrak{U}^{(1)},\mathfrak{U}^{(2)};\mathcal{P}_{\bullet}^{(1)},\mathcal{P}_{\bullet}^{(2)})$ le $n$-ème module d'hyperhomologie de $\mathbf{L}_{\bullet \bullet}^{(1)}\otimes_{\mathrm{A}}\mathbf{L}_{\bullet \bullet}^{(2)}$, que nous appellerons l'hypertor d'indice $n$ de $\mathcal{P}_{\bullet}^{(1)}$ et $\mathcal{P}_{\bullet}^{(2)}$, relatif aux recouvrements $\mathfrak{U}^{(1)}$ et $\mathfrak{U}^{(2)}$. Lorsque $\mathcal{P}_{\bullet}^{(1)}$ et $\mathcal{P}_{\bullet}^{(2)}$ sont réduits à leurs termes de degré $o$, $\mathcal{F}^{(1)}$ et $\mathcal{F}^{(2)}$, on écrit $\mathcal{Tor}_{n}^{\mathrm{S}}(\mathfrak{U}^{(1)},\mathfrak{U}^{(2)};\mathcal{F}^{(1)},\mathcal{F}^{(2)})$ leur hypertor. On désignera par $\mathcal{Tor}_{n}^{\mathrm{S}}(\mathfrak{U}^{(1)},\mathfrak{U}^{(2)};\mathcal{P}_{\bullet}^{(1)},\mathcal{P}_{\bullet}^{(2)})$, suivant les conventions générales, le bicomplexe dont le composant d'indices ($j,k$) est $\mathcal{Tor}_{n}^{\mathrm{S}}(\mathfrak{U}^{(1)},\mathfrak{U}^{(2)};\mathcal{P}_{j}^{(1)},\mathcal{P}_{k}^{(2)})$.

Comme  $L_{\bullet\bullet}^{(i)}$  est un foncteur exact en  $\mathcal{P}_{\bullet}^{(i)}$ , puisque les intersections des ensembles

de $\mathfrak{U}^{(i)}$ sont affines (I, 5.5.6 et 1.3.11), $\mathbf{Tor}_{\bullet}^{\mathrm{S}}(\mathfrak{U}^{(1)},\mathfrak{U}^{(2)};\mathcal{P}_{\bullet}^{(1)},\mathcal{P}_{\bullet}^{(2)})$ est un bi-$\partial$-foncteur covariant en $\mathcal{P}_{\bullet}^{(1)},\mathcal{P}_{\bullet}^{(2)}$, à valeurs dans la catégorie des A-modules (0, 11.7.3). En outre, on sait (0, 11.7.2) que ce bifoncteur est l'aboutissement commun de six foncteurs spectraux biréguliers, que nous désignerons par la notation ${}^{(t)}\mathrm{E}^{\mathrm{S}}(\mathfrak{U}^{(1)},\mathfrak{U}^{(2)};\mathcal{P}_{\bullet}^{(1)},\mathcal{P}_{\bullet}^{(2)})$ ou ${}^{(t)}\mathrm{E}(\mathfrak{U}^{(1)},\mathfrak{U}^{(2)};\mathcal{P}_{\bullet}^{(1)},\mathcal{P}_{\bullet}^{(2)})$, où $t$ doit être remplacé par une des lettres $a,b,a',b',c,d$, et dont les termes $\mathrm{E}_2$ sont les suivants :

$$
{ } ^ { ( a ) } \mathrm{E} _ { p q } ^ { 2 } = \bigoplus _ { q _ { 1 } + q _ { 2 } = q } \operatorname{Tor} _ { p } ^ { \mathrm{A} } ( \mathrm{H} _ { q _ { 1 } } ( \mathrm{L} _ { \bullet \bullet } ^ { ( 1 ) } ) , \mathrm{H} _ { q _ { 2 } } ( \mathrm{L} _ { \bullet \bullet } ^ { ( 2 ) } ) )
$$

$$
{ } ^ { ( b ) } \mathrm{E} _ { p q } ^ { 2 } = \mathrm{H} _ { p } ( \mathbf { T o r } _ { q } ^ { \mathrm{A,II} } ( \mathbf { L } _ { \bullet \bullet } ^ { ( 1 ) } , \mathbf { L } _ { \bullet \bullet } ^ { ( 2 ) } ) )
$$

$$
{ } ^ { ( a ^ { \prime } ) } \mathrm{E} _ { p q } ^ { 2 } = \bigoplus _ { q _ { 1 } + q _ { 2 } = q } \mathbf { T o r } _ { p } ^ { \mathrm{A} } ( \mathrm{H} _ { q _ { 1 } } ^ { \mathrm{I} } ( \mathrm{L} _ { \bullet \bullet } ^ { ( 1 ) } ) , \mathrm{H} _ { q _ { 2 } } ^ { \mathrm{I} } ( \mathrm{L} _ { \bullet \bullet } ^ { ( 2 ) } ) )
$$

$$
{ } ^ { ( b ^ { \prime } ) } \mathrm{E} _ { p q } ^ { 2 } = \mathrm{H} _ { p } ( \mathrm{Tor} _ { q } ^ { \mathrm{A} } ( \mathrm{L} _ { \bullet \bullet } ^ { ( 1 ) } , \mathrm{L} _ { \bullet \bullet } ^ { ( 2 ) } ) )
$$

$$
{ } ^ { ( c ) } \mathrm{E} _ { p q } ^ { 2 } = \bigoplus _ { q _ { 1 } + q _ { 2 } = q } \mathbf { T o r } _ { p } ^ { \mathrm{A} } ( \mathrm{H} _ { q _ { 1 } } ^ { \mathrm{II} } ( \mathrm{L} _ { \bullet \bullet } ^ { ( 1 ) } ) , \mathrm{H} _ { q _ { 2 } } ^ { \mathrm{II} } ( \mathrm{L} _ { \bullet \bullet } ^ { ( 2 ) } ) )
$$

$$
{ } ^ { ( d ) } \mathrm{E} _ { p q } ^ { 2 } = \mathrm{H} _ { p } ( \mathbf { T o r } _ { q } ^ { \mathrm{A} , \mathrm{I} } ( \mathrm{L} _ { \bullet \bullet } ^ { ( 1 ) } , \mathrm{L} _ { \bullet \bullet } ^ { ( 2 ) } ) ) ,
$$

où les notations sont conformes à celles de la théorie générale de l'hyperhomologie. Nous allons dans ce qui suit expliciter davantage ces termes initiaux.

(6.6.3) Suites spectrales (a) et (a'). Nous avons vu en (6.6.1) que le module d'homologie  $\mathbf{H}_{n}(\mathbf{L}_{\bullet\bullet}^{(i)})$  du bicomplexe  $\mathbf{L}_{\bullet\bullet}^{(i)}$  était égal à  $\mathbf{H}^{-n}(\mathbf{X}^{(i)},\mathcal{P}_{\bullet}^{(i)})$ ; donc

$$
{ } ^ { ( a ) } \mathrm{E} _ { p q } ^ { 2 } = \bigoplus _ { q _ { 1 } + q _ { 2 } = q } \operatorname{Tor} _ { p } ^ { A } ( \mathbf { H } ^ { - q _ { 1 } } ( \mathbf { X } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 1 ) } ) , \mathbf { H } ^ { - q _ { 2 } } ( \mathbf { X } ^ { ( 2 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) ) .
$$

Par définition, le complexe $\mathbf{H}_{n}^{\mathrm{I}}(\mathbf{L}_{\bullet \bullet}^{(i)})$ a pour terme de degré $k$ le module d'homologie $\mathbf{H}_{n}(\mathbf{C}^{\bullet}(\mathfrak{U}^{(i)},\mathcal{P}_{k}^{(i)}))$, c'est-à-dire, par définition, le module de cohomologie $\mathbf{H}^{-n}(\mathfrak{U}^{(i)},\mathcal{P}_{k}^{(i)})$; on sait (1.4.1) que ce module est canoniquement isomorphe à $\mathbf{H}^{-n}(\mathbf{X}^{(i)},\mathcal{P}_{k}^{(i)})$; donc

$$
{ } ^ { ( a ^ { \prime } ) } \mathrm{E} _ { p q } ^ { 2 } = \bigoplus _ { q _ { 1 } + q _ { 2 } = q } \mathbf { T o r } _ { p } ^ { \mathrm{A} } ( \mathrm{H} ^ { - q _ { 1 } } ( \mathrm{X} ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 1 ) } ) , \mathrm{H} ^ { - q _ { 2 } } ( \mathrm{X} ^ { ( 2 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) ) .
$$

(6.6.4) Suites spectrales (b) et (b'). Par définition,  $\mathbf{Tor}_{q}^{\mathrm{A},\mathrm{II}}(\mathrm{L}_{\bullet\bullet}^{(1)},\mathrm{L}_{\bullet\bullet}^{(2)})$  est un bicomplexe dont le terme de degré (h, k) est le A-module

$$
\mathbf {T o r} _ {q} ^ {\mathrm{A}} \left(\mathrm{C} ^ {- h} \left(\mathfrak {U} ^ {(1)}, \mathscr {P} _ {\bullet} ^ {(1)}\right), \mathrm{C} ^ {- k} \left(\mathfrak {U} ^ {(2)}, \mathscr {P} _ {\bullet} ^ {(2)}\right)\right).
$$

Soit $\Phi^{(i)}$ l'ensemble d'indices de $\mathfrak{U}^{(i)}$; par définition, le complexe de modules $\mathbf{C}^r (\mathfrak{U}^{(i)},\mathcal{P}_{\bullet}^{(i)})$ ($r\geqslant 0$) est somme directe des complexes $\Gamma (\mathrm{U}_{\rho}^{(i)},\mathcal{P}_{\bullet}^{(i)})$, où $\mathrm{U}_{\rho}^{(i)}$ est l'intersection des $\mathrm{U}_{\xi}^{(i)}$ pour $\xi \in \rho$, et $\rho$ parcourt $\mathfrak{P}(\Phi^{(i)})$; donc le A-module

$$
\mathbf {T o r} _ {q} ^ {\mathrm{A}} \left(\mathrm{C} ^ {- h} \left(\mathfrak {U} ^ {(1)}, \mathscr {P} _ {\bullet} ^ {(1)}\right), \mathrm{C} ^ {- k} \left(\mathfrak {U} ^ {(2)}, \mathscr {P} _ {\bullet} ^ {(2)}\right)\right)
$$

est somme directe des A-modules $\mathbf{Tor}_{q}^{A}(\Gamma(\mathrm{U}_{\sigma}^{(1)},\mathcal{P}_{\bullet}^{(1)}),\Gamma(\mathrm{U}_{\tau}^{(2)},\mathcal{P}_{\bullet}^{(2)}))$, où $\sigma$ (resp. $\tau$) parcourt les éléments de $\mathfrak{P}(\Phi^{(1)})$ (resp. $\mathfrak{P}(\Phi^{(2)})$) tels que $\operatorname{Card}(\sigma) = -(h + 1)$ (resp. $\operatorname{Card}(\tau) = -(k + 1)$). Comme $\mathbf{X}^{(1)}$ et $\mathbf{X}^{(2)}$ sont des schémas, les $\mathrm{U}_{\rho}^{(i)}$ sont affines, donc on a (6.4.1.1)

$$
\mathbf {T o r} _ {q} ^ {\mathrm{A}} \left(\Gamma \left(\mathrm{U} _ {\sigma} ^ {(1)}, \mathcal {P} _ {\bullet} ^ {(1)}\right), \Gamma \left(\mathrm{U} _ {\tau} ^ {(2)}, \mathcal {P} _ {\bullet} ^ {(2)}\right)\right) = \Gamma \left(\mathrm{U} _ {\sigma} ^ {(1)} \times_ {\mathrm{S}} \mathrm{U} _ {\tau} ^ {(2)}, \mathfrak {C o r} _ {q} ^ {\mathrm{S}} \left(\mathcal {P} _ {\bullet} ^ {(1)}, \mathcal {P} _ {\bullet} ^ {(2)}\right)\right).
$$

154

155

On voit donc que  ${}^{(b)}E_{pq}^{2}$  est le  $(-p)$ -ème module de cohomologie du complexe  $\mathbf{L}^{\bullet}(\Phi^{(1)},\Phi^{(2)};\mathcal{S})$  des cochaînes bi-alternées sur  $\Phi^{(1)}$  et  $\Phi^{(2)}$  à valeurs dans le système de coefficients

$$
\mathscr {S}: (\sigma , \tau) \rightsquigarrow \Gamma \left(\mathrm{U} _ {\sigma} ^ {(1)} \times_ {\mathrm{S}} \mathrm{U} _ {\tau} ^ {(2)}, \mathfrak {C o r} _ {q} ^ {\mathrm{S}} \left(\mathscr {P} _ {\bullet} ^ {(1)}, \mathscr {P} _ {\bullet} ^ {(2)}\right)\right)
$$

(0, 11.8.4). On sait alors (0, 11.8.5 et 11.8.6) que la cohomologie de ce complexe est la même que celle du complexe $\mathbf{C}^{\bullet}(\Phi^{(1)},\Phi^{(2)};\mathcal{S})$ de toutes les cochaînes sur $\Phi^{(1)}$ et $\Phi^{(2)}$ à valeurs dans $\mathcal{S}$, et aussi que celle du complexe $\mathbf{P}^{\bullet}(\Phi^{(1)},\Phi^{(2)};\mathcal{S})$, dont les éléments sont les combinaisons linéaires des

$$
\lambda (\sigma , \tau) \in \Gamma \left(\mathrm{U} _ {\sigma} ^ {(1)} \times_ {\mathrm{S}} \mathrm{U} _ {\tau} ^ {(2)}, \mathfrak {C o r} _ {q} ^ {\mathrm{S}} \left(\mathscr {P} _ {\bullet} ^ {(1)}, \mathscr {P} _ {\bullet} ^ {(2)}\right)\right)
$$

où $\sigma = (\alpha_0, \ldots, \alpha_h)$ et $\tau = (\beta_0, \ldots, \beta_h)$ sont des suites ayant même nombre d'éléments. Mais on a alors $U_{\sigma}^{(1)} \times_S U_{\tau}^{(2)} = (U_{\alpha_0}^{(1)} \times_S U_{\beta_0}^{(2)}) \cap \ldots \cap (U_{\alpha_h}^{(1)} \times_S U_{\beta_h}^{(2)})$ (I, 3.2.7). Si l'on désigne par \$\mathfrak{U}\$ le recouvrement de $Z = X^{(1)} \times_S X^{(2)}$ par les ouverts affines $U_{\alpha}^{(1)} \times_S U_{\beta}^{(2)}$, on voit finalement, compte tenu de ce que $X^{(1)} \times_S X^{(2)}$ est un schéma, que l'on a, en vertu de (I.3.I),

$$
{ } ^ { ( b ) } \mathrm{E} _ { p q } ^ { 2 } = \mathrm{H} ^ { - p } ( \mathrm{X} ^ { ( 1 ) } \times _ { \mathrm{S} } \mathrm{X} ^ { ( 2 ) } , \mathfrak { C o r } _ { q } ^ { \mathrm{S} } ( \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) .
$$

En second lieu, $\operatorname{Tor}_{q}^{\mathbf{A}}(\mathbf{L}_{\bullet \bullet}^{(1)}, \mathbf{L}_{\bullet \bullet}^{(2)})$ est un bicomplexe dont le terme de degré $(h, k)$ est la somme directe des A-modules

$$
\operatorname{Tor} _ {q} ^ {\mathrm{A}} \left(\mathrm{C} ^ {- h _ {1}} \left(\mathfrak {U} ^ {(1)}, \mathscr {P} _ {k _ {1}} ^ {(1)}\right), \mathrm{C} ^ {- h _ {2}} \left(\mathfrak {U} ^ {(2)}, \mathscr {P} _ {k _ {2}} ^ {(2)}\right)\right)
$$

tels que $h_1 + h_2 = h$ et $k_1 + k_2 = k$; explicitant les modules $\mathbf{C}^r(\mathfrak{U}^{(i)}, \mathcal{P}_s^{(i)})$ comme ci-dessus, on voit encore que ce terme est somme directe des A-modules

$$
\Gamma (\mathrm{U} _ {\sigma} ^ {(1)} \times_ {\mathrm{S}} \mathrm{U} _ {\tau} ^ {(2)}, \mathcal {T o r} _ {q} ^ {\mathrm{S}} (\mathcal {P} _ {k _ {1}} ^ {(1)}, \mathcal {P} _ {k _ {2}} ^ {(2)}))
$$

où $k_1 + k_2 = k$, et $\sigma$ (resp. $\tau$) parcourt les éléments de $\mathfrak{P}(\Phi^{(1)})$ (resp. $\mathfrak{P}(\Phi^{(2)})$) tels que $\text{Card}(\sigma) + \text{Card}(\tau) = -h - 2$. Le terme $^{(b')} \mathrm{E}_{pq}^2$ que nous calculons est le $(-p)$-ème module de cohomologie d'un bicomplexe $\mathrm{N}^{\bullet \bullet} = (\mathrm{N}^{hk})$, où le complexe simple $\mathrm{N}^{\bullet k}$ est le complexe de cochaînes bi-alternées sur $\Phi^{(1)}$ et $\Phi^{(2)}$, à valeurs dans le système de coefficients

$$
\mathcal {S} _ {k}: (\sigma , \tau) \rightsquigarrow \Gamma \left(\mathrm{U} _ {\sigma} ^ {(1)} \times \mathrm{U} _ {\tau} ^ {(2)}, \bigoplus_ {k _ {1} + k _ {2} = k} \mathcal {T o r} _ {q} ^ {\mathrm{S}} \left(\mathcal {P} _ {- k _ {1}} ^ {(1)}, \mathcal {P} _ {- k _ {2}} ^ {(2)}\right)\right)
$$

ces systèmes de coefficients formant un complexe $\mathcal{S}^{\bullet}$ où la différentielle provient de celle du complexe simple associée au bicomplexe $\mathcal{Tor}_{q}^{\mathrm{S}}(\mathcal{P}^{(1)\bullet},\mathcal{P}^{(2)\bullet})$. On sait que la cohomologie de $\mathbf{N}^{\bullet \bullet}$ est la même que celle du bicomplexe $\mathbf{C}^{\bullet}(\Phi^{(1)},\Phi^{(2)};\mathcal{S}^{\bullet})$ (0, 11.8.9), et aussi la même que celle du bicomplexe $\mathbf{P}^{\bullet}(\Phi^{(1)},\Phi^{(2)};\mathcal{S}^{\bullet})$, où les éléments de degrés $(h,k)$ sont les combinaisons linéaires des

$$
\lambda (\sigma , \tau) \in \Gamma \left(\mathrm{U} _ {\sigma} ^ {(1)} \times_ {\mathrm{S}} \mathrm{U} _ {\tau} ^ {(2)}, \bigoplus_ {k _ {1} + k _ {2} = k} \mathcal {T o r} _ {q} ^ {\mathrm{S}} \left(\mathcal {P} _ {- k _ {1}} ^ {(1)}, \mathcal {P} _ {- k _ {2}} ^ {(2)}\right)\right)
$$

$\sigma = (\alpha_0, \ldots, \alpha_h), \tau = (\beta_0, \ldots, \beta_h)$ étant des suites ayant même nombre d'éléments (0, 11.8.10). On voit alors comme ci-dessus que $^{(b')}\mathrm{E}_{pq}^2$ est le $(-p)$-ème module de cohomologie du bicomplexe $\mathbf{C}^\bullet(\mathfrak{U}, \mathcal{D})$, où $\mathcal{D}^\bullet$ est le complexe simple associé au bicomplexe $\mathcal{T}or_q^{\mathrm{S}}(\mathcal{P}^{(1)}\cdot, \mathcal{P}^{(2)}\cdot)$ de $\mathcal{O}_{\mathbb{Z}}$-Modules. Avec les conventions faites dans (6.6.1), on a donc

$$
{ } ^ { ( b ^ { \prime } ) } \mathrm{E} _ { p q } ^ { 2 } = \mathbf { H } ^ { - p } ( \mathbf { X } ^ { ( 1 ) } \times _ { \mathrm{S} } \mathbf { X } ^ { ( 2 ) } , \mathcal { T o r } _ { q } ^ { \mathrm{S} } ( \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) ) .
$$

(6.6.5) Suites spectrales (c) et (d). Par définition, le complexe  $\mathrm{H}_{n}^{\mathrm{II}}(\mathrm{L}_{\bullet\bullet}^{(i)})$  a pour terme de degré h le A-module  $\mathrm{C}^{-h}(\mathfrak{U}^{(i)},\mathcal{H}_{n}(\mathcal{P}_{\bullet}^{(i)}))$ , en vertu de l'exactitude du foncteur  $C^{-h}$ . On a donc, par définition de l'hypertor de deux Modules relatif à deux recouvrements (6.6.2)

$$
{ } ^ { ( c ) } \mathrm{E} _ { p q } ^ { 2 } = \bigoplus _ { q _ { 1 } + q _ { 2 } = q } \operatorname{Tor} _ { p } ^ { \mathrm{S} } ( \mathfrak { U } ^ { ( 1 ) } , \mathfrak { U } ^ { ( 2 ) } ; \mathscr { H } _ { q _ { 1 } } ( \mathscr { P } _ { \bullet } ^ { ( 1 ) } ) , \mathscr { H } _ { q _ { 2 } } ( \mathscr { P } _ { \bullet } ^ { ( 2 ) } ) ) .
$$

Enfin, par définition, $\mathbf{Tor}_{q}^{\mathrm{A},\mathrm{I}}(\mathrm{L}_{\bullet \bullet}^{(1)},\mathrm{L}_{\bullet \bullet}^{(2)})$ est un bicomplexe dont le terme de degré $(h,k)$ est le A-module $\operatorname {Tor}_q^S (\mathfrak{U}^{(1)},\mathfrak{U}^{(2)};\mathcal{P}_h^{(1)},\mathcal{P}_k^{(2)})$. On a donc

$$
{ } ^ { ( d ) } \mathrm{E} _ { p q } ^ { 2 } = \mathrm{H} _ { p } ( \mathrm{Tor} _ { q } ^ { \mathrm{S} } ( \mathfrak { U } ^ { ( 1 ) } , \mathfrak { U } ^ { ( 2 ) } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) ) .
$$

(6.6.6) La théorie de l'hyperhomologie des foncteurs de bicomplexes (0, 11.7.3) montre, comme dans (6.3.4), que, pour toute résolution plate de Cartan-Eilenberg $\mathbf{M}_{\bullet \bullet}^{(i)}$ de $\mathbf{L}_{\bullet \bullet}^{(i)}$ (dans la catégorie des complexes de modules limités inférieurement) $(i = 1,2)$, on a des isomorphismes canoniques de bi-$\partial$-foncteurs

$$
\mathbf {T o r} _ {\bullet} ^ {\mathrm{S}} (\mathfrak {U} ^ {(1)}, \mathfrak {U} ^ {(2)}; \mathscr {P} _ {\bullet} ^ {(1)}, \mathscr {P} _ {\bullet} ^ {(2)}) \xrightarrow {\sim} \mathrm{H} _ {\bullet} (\mathrm{M} _ {\dots} ^ {(1)} \otimes_ {\mathrm{A}} \mathrm{M} _ {\dots} ^ {(2)}) \xrightarrow {\sim} \mathrm{H} _ {\bullet} (\mathrm{M} _ {\dots} ^ {(1)} \otimes_ {\mathrm{A}} \mathrm{L} _ {\dots} ^ {(2)}) \xrightarrow {\sim} \mathrm{H} _ {\bullet} (\mathrm{L} _ {\dots} ^ {(1)} \otimes_ {\mathrm{A}} \mathrm{M} _ {\dots} ^ {(2)}).\tag{6.6.6.1}
$$

(6.6.7) Nous allons maintenant montrer que l'hypertor global défini dans (6.6.2), et les six suites spectrales correspondantes, ne dépendent pas des recouvrements ouverts affines finis $\mathfrak{U}^{(i)}$ qui ont servi à les définir (à des isomorphismes canoniques près). Il suffira pour cela de montrer que si $\mathfrak{B}^{(i)}$ sont deux autres recouvrements de même nature, tels que $\mathfrak{B}^{(i)}$ soit plus fin que $\mathfrak{U}^{(i)}$ pour $i=1,2$, alors on a des isomorphismes canoniques de foncteurs spectraux

$$
{ } ^ { ( t ) } \mathrm{E} \left( \mathfrak { U } ^ { ( 1 ) } , \mathfrak { U } ^ { ( 2 ) } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } \right) \simeq { } ^ { ( t ) } \mathrm{E} \left( \mathfrak { V } ^ { ( 1 ) } , \mathfrak { V } ^ { ( 2 ) } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } \right)\tag{6.6.7, t)}
$$

où t est remplacé par a, b,  $a'$ ,  $b'$ , c ou d.

Or, on a pour $i=1,2$ des homomorphismes de bicomplexes

$$
\mathbf {C} ^ {\bullet} \left(\mathfrak {U} ^ {(i)}, \mathcal {P} _ {\bullet} ^ {(i)}\right)\rightarrow \mathbf {C} ^ {\bullet} \left(\mathfrak {V} ^ {(i)}, \mathcal {P} _ {\bullet} ^ {(i)}\right)
$$

bien définis à homotopies près (G, II, 5.7.1); il en résulte déjà des homomorphismes (6.6.7, t)) canoniquement définis et compatibles avec les opérateurs bords dans les aboutissements (0, 11.3.2). En outre, le calcul des termes  $E_{2}$  des suites spectrales (a), (b), (a'), (b'), montre que pour ces suites spectrales l'homomorphisme (6.6.7, t)) est un isomorphisme sur les termes  $E_{2}$ ; comme ces suites spectrales sont birégulières, on voit que (6.6.7, t)) est un isomorphisme pour ces trois foncteurs spectraux, donc un isomorphisme de bi- $\partial$ -foncteurs pour leur aboutissement commun (0, 11.1.5).

En particulier, pour des $\mathcal{O}_{\mathrm{X}^{(i)}}$-Modules quasi-cohérents $\mathcal{F}^{(i)}(i=1,2)$, l'homomorphisme canonique

$$
\mathrm{Tor} _ {\bullet} ^ {\mathrm{S}} (\mathfrak {U} ^ {(1)}, \mathfrak {U} ^ {(2)}; \mathcal {F} ^ {(1)}, \mathcal {F} ^ {(2)}) \to \mathrm{Tor} _ {\bullet} ^ {\mathrm{S}} (\mathfrak {V} ^ {(1)}, \mathfrak {V} ^ {(2)}; \mathcal {F} ^ {(1)}, \mathcal {F} ^ {(2)})
$$

est bijectif; vu le calcul de (6.6.5), on voit que (6.6.7, t)) est aussi un isomorphisme des termes  $E_{2}$  pour t=c et t=d. On conclut comme ci-dessus que (6.6.7, t)) est aussi un isomorphisme de suites spectrales pour t=c et t=d.

On peut considérer que les isomorphismes (6.6.7, t)) définissent des systèmes inductifs de foncteurs spectraux sur l'ensemble filtrant des couples  $(\mathfrak{U}^{(1)}, \mathfrak{U}^{(2)})$  de recouvrements ouverts affines finis de  $\mathbf{X}^{(1)}$  et  $\mathbf{X}^{(2)}$ . Nous désignerons par

$$
{ } ^ { ( t ) } \mathrm{E} ( \mathbf { X } ^ { ( 1 ) } , \mathbf { X } ^ { ( 2 ) } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) \quad \text {   o   u   } { } ^ { ( t ) } \mathrm{E} ^ { \mathrm{S} } ( \mathbf { X } ^ { ( 1 ) } , \mathbf { X } ^ { ( 2 ) } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } )
$$

la limite inductive de ce système, par $\mathbf{Tor}_{\bullet}^{S}(\mathbf{X}^{(1)},\mathbf{X}^{(2)};\mathcal{P}_{\bullet}^{(1)},\mathcal{P}_{\bullet}^{(2)})$ l'aboutissement de ce foncteur spectral, que nous appellerons l'hypertor global des deux complexes $\mathcal{P}_{\bullet}^{(1)}$ et $\mathcal{P}_{\bullet}^{(2)}$; si $\mathcal{P}_{\bullet}^{(1)}$ et $\mathcal{P}_{\bullet}^{(2)}$ sont réduits à leurs termes de degré o, $\mathcal{F}^{(1)}$ et $\mathcal{F}^{(2)}$, nous écrirons

$$
\mathrm{Tor} _ {\bullet} ^ {\mathrm{S}} (\mathbf {X} ^ {(1)}, \mathbf {X} ^ {(2)}; \mathcal {F} ^ {(1)}, \mathcal {F} ^ {(2)}),
$$

et conformément aux conventions générales, $\operatorname{Tor}_{q}^{\mathrm{S}}(\mathbf{X}^{(1)},\mathbf{X}^{(2)};\mathcal{P}_{\bullet}^{(1)},\mathcal{P}_{\bullet}^{(2)})$ sera donc le bicomplexe des $\operatorname{Tor}_{q}^{\mathrm{S}}(\mathbf{X}^{(1)},\mathbf{X}^{(2)};\mathcal{P}_{h}^{(1)},\mathcal{P}_{k}^{(2)})$.

(6.6.8) Les hypothèses étant celles de (6.6.1), considérons maintenant deux S-morphismes $f_i: \mathbf{X}^{(i)} \to \mathbf{Y}^{(i)}$, où $\mathbf{Y}^{(i)} = \text{Spec}(\mathbf{B}_i)$ est un S-schéma affine, $\mathbf{B}_i$ étant donc une A-algèbre ($i = 1, 2$); cela définit donc un A-homomorphisme $\mathbf{B}_i \to \Gamma(\mathbf{X}^{(i)}, \mathcal{O}_{\mathbf{X}^{(i)}})(\mathbf{I}, 2.2.4)$, et par suite chacun des $\mathbf{L}_{\bullet \bullet}^{(i)}$ définis dans (6.6.2) est un bicomplexe de $\mathbf{B}_i$-modules; on en conclut que $\mathbf{L}_{\bullet \bullet}^{(1)} \otimes_{\mathbf{A}} \mathbf{L}_{\bullet \bullet}^{(2)}$ est un quadricomplexe de $(\mathbf{B}_1 \otimes_{\mathbf{A}} \mathbf{B}_2)$-modules, et ses six foncteurs spectraux d'hyperhomologie peuvent donc être considérés comme prenant leurs valeurs dans la catégorie des suites spectrales de $(\mathbf{B}_1 \otimes_{\mathbf{A}} \mathbf{B}_2)$-modules. Si l'on pose $\mathbf{Y} = \mathbf{Y}^{(1)} \times_{\mathbf{S}} \mathbf{Y}^{(2)} = \text{Spec}(\mathbf{B}_1 \otimes_{\mathbf{A}} \mathbf{B}_2)$, on peut considérer les $\mathcal{O}_{\mathbf{Y}}$-Modules quasi-cohérents associés à ces modules ($\mathbf{I}, 1.3.4$); nous noterons $^{(t)}\mathcal{E}(f_1, f_2; \mathcal{P}_{\bullet}^{(1)}, \mathcal{P}_{\bullet}^{(2)})$ (pour $t = a, b, a', b', c$ ou $d$) les six suites spectrales $(^{(t)}\text{E}(\mathbf{X}^{(1)}, \mathbf{X}^{(2)}; \mathcal{P}_{\bullet}^{(1)}, \mathcal{P}_{\bullet}^{(2)}))^{\sim}$ de $\mathcal{O}_{\mathbf{Y}}$-Modules, et $\mathcal{Gor}_{\bullet}^{\text{S}}(f_1, f_2; \mathcal{P}_{\bullet}^{(1)}, \mathcal{P}_{\bullet}^{(2)})$ leur aboutissement commun $(\text{Tor}_{\bullet}^{\text{S}}(\mathbf{X}_{\bullet}^{(1)}, \mathbf{X}^{(2)}; \mathcal{P}_{\bullet}^{(1)}, \mathcal{P}_{\bullet}^{(2)}))^{\sim}$. On le notera $\text{Tor}_{\bullet}^{\text{S}}(f_1, f_2; \mathcal{F}^{(1)}, \mathcal{F}^{(2)})$ lorsque $\mathcal{P}_{\bullet}^{(i)}$ est réduit à son terme de degré $o, \mathcal{F}^{(i)} (i = 1, 2)$.

## 6.7. Foncteurs hypertor globaux de complexes de Modules quasi-cohérents et suites spectrales de Künneth : cas général.

(6.7.1) Nous allons maintenant généraliser les définitions de (6.6.8) au cas où S est un préschéma quelconque,  $\mathbf{X}^{(i)}$ ,  $\mathbf{Y}^{(i)}$  des S-préschémas et  $f_{i}: \mathbf{X}^{(i)} \to \mathbf{Y}^{(i)}$  des morphismes séparés et quasi-compacts. Il s'agit alors, pour tout couple de complexes  $\mathcal{P}_{\bullet}^{(i)}$  de  $\mathcal{O}_{\mathrm{X}}^{(i)}$ -Modules quasi-cohérents, limités inférieurement,  $(i = 1, 2)$ , de définir pour tout n un  $O_{Y}$ -Module quasi-cohérent  $\mathfrak{Gor}_{n}^{\mathrm{S}}(f_{1}, f_{2}; \mathcal{P}_{\bullet}^{(1)}, \mathcal{P}_{\bullet}^{(2)})$  ainsi que 6 foncteurs spectraux, se réduisant aux définitions de (6.6.8) lorsque S,  $\mathbf{Y}^{(1)}$  et  $\mathbf{Y}^{(2)}$  sont affines (on pose  $\mathbf{Y} = \mathbf{Y}^{(1)} \times_{\mathrm{s}} \mathbf{Y}^{(2)}$ ). Supposons d'abord S = Spec(A) affine, mais  $\mathbf{Y}^{(1)}$  et  $\mathbf{Y}^{(2)}$  quelconques; soit  $\mathbf{W}^{(i)}$  un ouvert affine de  $\mathbf{Y}^{(i)}$ ;  $f_{i}^{-1}(\mathbf{W}^{(i)})$  est alors un S-schéma quasi-compact,  $W = W^{(1)} \times_{s} W^{(2)}$  un ouvert affine de Y; soit  $f_{i}' : f_{i}^{-1}(W^{(i)}) \to W^{(i)}$  la restriction de  $f_{i}$ , et  $\mathcal{P}_{\bullet}^{(i)}$  la restriction  $\mathcal{P}_{\bullet}^{(i)} | f_{i}^{-1}(W^{(i)}) (i = 1, 2)$ . On a alors d'après (6.6.8) les suites spectrales  $^{(l)}\mathcal{E}(f_{1}', f_{2}', \mathcal{P}_{\bullet}^{(1)}, \mathcal{P}_{\bullet}^{(2)})$  de  $(\mathcal{O}_{\mathrm{Y}}|W)$ -Modules quasi-cohérents, et il s'agit de vérifier qu'elles satisfont aux conditions de recollement  $(\mathbf{0}_{\mathrm{I}}, 3.3.1)$ . On est aussitôt ramené au cas où  $\mathbf{Y}^{(i)} = \operatorname{Spec}(\mathbf{B}_{i})$  est affine et où  $\mathbf{W}^{(i)} = \mathbf{D}(g_{i})$ , où  $g_{i} \in B_{i}$ , de sorte que  $W = D(g_{1} \otimes g_{2})$

dans  $\mathrm{Y}=\mathrm{Spec}(\mathrm{B}_{1}\otimes_{\mathrm{A}}\mathrm{B}_{2})$  (II, 4.3.2.1); si  $\mathbf{X}^{\prime(i)}=f_{i}^{-1}(\mathbf{W}^{(i)})$ , il s'agit d'établir un isomorphisme canonique de foncteurs spectraux

$$
{ } ^ { ( t ) } \mathrm{E} ( \mathbf { X } ^ { \prime ( 1 ) } , \mathbf { X } ^ { \prime ( 2 ) } ; \mathcal { P } _ { \bullet } ^ { \prime ( 1 ) } , \mathcal { P } _ { \bullet } ^ { \prime ( 2 ) } ) \simeq { } ^ { ( t ) } \mathrm{E} ( \mathbf { X } ^ { ( 1 ) } , \mathbf { X } ^ { ( 2 ) } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) \otimes _ { \mathrm{B} } \mathbf { B } _ { g }\tag{6.7.1.1}
$$

où l'on a posé  $B=B_{1}\otimes_{A}B_{2}$  et  $g=g_{1}\otimes g_{2}$ . Pour cela, partons de recouvrements ouverts affines finis  $\mathfrak{U}^{(i)}$  de  $\mathbf{X}^{(i)}$  (i=1,2), et soit  $\mathfrak{U}^{\prime(i)}$  la trace de  $\mathfrak{U}^{(i)}$  sur  $\mathbf{X}^{\prime(i)}$ , qui est encore formé d'ouverts affines (I, 5.5.10); de façon précise, on a

$$
\mathrm{C} ^ {\bullet} \left(\mathfrak {U} ^ {\prime (i)}, \mathscr {P} _ {\bullet} ^ {\prime (i)}\right) = \mathrm{C} ^ {\bullet} \left(\mathfrak {U} ^ {(i)}, \mathscr {P} _ {\bullet} ^ {(i)}\right) \otimes_ {\mathrm{B} _ {i}} \left(\mathrm{B} _ {i}\right) _ {g _ {i}}.
$$

Si on pose  $L_{\bullet\bullet}^{\prime(i)} = C^{\bullet}(\mathfrak{U}^{\prime(i)}, \mathcal{P}_{\bullet}^{\prime(i)})$ , on a donc  $L_{\bullet\bullet}^{\prime(1)} \otimes_{A} L_{\bullet\bullet}^{\prime(2)} = (L_{\bullet\bullet}^{(1)} \otimes_{B_1}(B_1)_{g_1}) \otimes_{A} (L_{\bullet\bullet}^{(2)} \otimes_{B_2}(B_2)_{g_2})$ ; comme on a  $B_g = (B_1)_{g_1} \otimes_A (B_2)_{g_2}$  à un isomorphisme canonique près, on a, à un isomorphisme canonique près,  $L_{\bullet\bullet}^{\prime(1)} \otimes_{A} L_{\bullet\bullet}^{\prime(2)} = (L_{\bullet\bullet}^{(1)} \otimes_{A} L_{\bullet\bullet}^{(2)}) \otimes_{B} B_g$ . Si  $M_{\bullet\bullet}^{(i)}$  est une résolution projective de Cartan-Eilenberg de  $L_{\bullet\bullet}^{(i)}$ , qu'on peut supposer formée de  $B_i$ -modules, il résulte du fait que  $(B_i)_{g_i}$  est plat sur  $B_i$  que  $M_{\bullet\bullet}^{\prime(i)} = M_{\bullet\bullet}^{(i)} \otimes_{B_i}(B_i)_{g_i}$  est une résolution projective de Cartan-Eilenberg du bicomplexe  $L_{\bullet\bullet}^{\prime(i)}$ ; en outre, on a

$$
\mathbf {M} _ {\bullet \bullet \bullet} ^ {\prime (1)} \otimes_ {\mathrm{A}} \mathbf {M} _ {\bullet \bullet \bullet} ^ {\prime (2)} = (\mathbf {M} _ {\bullet \bullet \bullet} ^ {(1)} \otimes_ {\mathrm{A}} \mathbf {M} _ {\bullet \bullet \bullet} ^ {(2)}) \otimes_ {\mathrm{B}} \mathbf {B} _ {g}.
$$

L'isomorphisme cherché (6.7.1.1) résulte alors aussitôt des définitions de l'hyperhomologie d'un bicomplexe, et de l'exactitude du foncteur  $G \otimes_{B} B_{g}$  en le B-module G.

(6.7.2) Supposons maintenant S quelconque, et soient $u_i: \mathrm{Y}^{(i)} \to \mathrm{S}$ les morphismes structuraux ($i = 1, 2$). Soit $(\mathrm{S}_{\alpha})$ un recouvrement ouvert affine de S, posons $\mathrm{Y}_{\alpha}^{(i)} = u_i^{-1}(\mathrm{S}_{\alpha})$, $\mathrm{X}_{\alpha}^{(i)} = f_i^{-1}(\mathrm{Y}_{\alpha}^{(i)})$, et soit $f_{i\alpha}: \mathrm{X}_{\alpha}^{(i)} \to \mathrm{Y}_{\alpha}^{(i)}$ la restriction de $f_i$, qui est un morphisme séparé et quasi-compact. Les $\mathrm{Y}_{\alpha} = \mathrm{Y}_{\alpha}^{(1)} \times_{\mathrm{S}_{\alpha}} \mathrm{Y}_{\alpha}^{(2)}$ forment un recouvrement ouvert de Y, et sur chaque $\mathrm{Y}_{\alpha}$ sont définis par (6.7.1) des foncteurs spectraux

$$
{ } ^ { ( t ) } \mathcal { E } ^ { \mathrm{S} _ { \alpha } } ( f _ { 1 \alpha } , f _ { 2 \alpha } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } | \mathbf { X } _ { \alpha } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } | \mathbf { X } _ { \alpha } ^ { ( 2 ) } ) ;
$$

il s'agit encore de montrer que ces foncteurs vérifient les conditions de recollement. On se ramène aussitôt à la situation suivante : $S = \text{Spec}(A)$ est affine, $S' = D(h)$, où $h \in A$, et $u_i(Y^{(i)}) \subset S'$; on peut en outre supposer $Y^{(i)} = \text{Spec}(B_i)$ affine; il s'agit de définir des isomorphismes canoniques

$$
{ } ^ { ( t ) } \mathrm{E} ^ { \mathrm{S} } ( \mathbf { X } ^ { ( 1 ) } , \mathbf { X } ^ { ( 2 ) } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) \stackrel { \sim } { \rightarrow } { } ^ { ( t ) } \mathrm{E} ^ { \mathrm{S} ^ { \prime } } ( \mathbf { X } ^ { ( 1 ) } , \mathbf { X } ^ { ( 2 ) } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) .\tag{6.7.2.1}
$$

Or, avec les notations de (6.6.2), les  $L_{\bullet\bullet}^{(i)}$  sont formés de  $A_{h}$ -modules, et l'on a donc  $\mathbf{L}_{\bullet\bullet}^{(1)}\otimes_{A_{h}}\mathbf{L}_{\bullet\bullet}^{(2)}=\mathbf{L}_{\bullet\bullet}^{(1)}\otimes_{A}\mathbf{L}_{\bullet\bullet}^{(2)}$  à un isomorphisme canonique près; comme on peut prendre une résolution projective de Cartan-Eilenberg  $\mathbf{M}_{\bullet\bullet}^{(i)}$  de  $L_{\bullet\bullet}^{(i)}$  formée de  $A_{h}$ -modules, cela donne aussitôt l'isomorphisme canonique cherché.

Nous avons en résumé démontré le

Théorème (6.7.3). — Soient S un préschéma, $f_i: \mathbf{X}_i \to \mathbf{Y}_i$ un S-morphisme séparé et quasi-compact de S-préschémas, $\mathcal{P}_{\bullet}^{(i)}$ un complexe de $\mathcal{O}_{\mathrm{X}}^{(i)}$-Modules quasi-cohérents limité inférieurement ($i = 1, 2$); on pose $\mathbf{Y} = \mathbf{Y}^{(1)} \times_{\mathrm{S}} \mathbf{Y}^{(2)}$. Il existe un bi-$\partial$-foncteur $\mathcal{G}or_{\bullet}^{\mathrm{S}}(f_1, f_2; \mathcal{P}_{\bullet}^{(1)}, \mathcal{P}_{\bullet}^{(2)})$

à valeurs dans la catégorie des $\mathcal{O}_{\mathrm{Y}}$-Modules quasi-cohérents, tel que si $\mathrm{V}^{(i)}$ est un ouvert affine de $\mathrm{Y}^{(i)}$ ($i = 1, 2$) et $\mathrm{V} = \mathrm{V}^{(1)} \times_{\mathrm{S}} \mathrm{V}^{(2)}$, on ait

$$
\mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} (f _ {1}, f _ {2}; \mathcal {P} _ {\bullet} ^ {(1)}, \mathcal {P} _ {\bullet} ^ {(2)}) | \mathrm{V} = (\mathbf {T o r} _ {\bullet} ^ {\mathrm{S}} (f _ {1} ^ {- 1} (\mathrm{V} ^ {(1)}), f _ {2} ^ {- 1} (\mathrm{V} ^ {(2)}); \mathcal {P} _ {\bullet} ^ {(1)} | f _ {1} ^ {- 1} (\mathrm{V} ^ {(1)}), \mathcal {P} _ {\bullet} ^ {(2)} | f _ {2} ^ {- 1} (\mathrm{V} ^ {(2)}))) \sim .
$$

Ce bifoncteur est l'aboutissement de six foncteurs spectraux biréguliers

$$
{ } ^ { ( t ) } \mathcal { E } ( f _ { 1 } , f _ { 2 } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) \quad ( t = a , b , a ^ { \prime } , b ^ { \prime } , c , d )
$$

dont les termes  $E_{2}$  sont donnés par

$$
{ } ^ { ( a ) } \mathcal { E } _ { p q } ^ { 2 } = \bigoplus _ { q _ { 1 } + q _ { 2 } = q } \mathcal { T o r } _ { p } ^ { S } ( \mathcal { H } ^ { - q _ { 1 } } ( f _ { 1 } , \mathcal { P } _ { \bullet } ^ { ( 1 ) } ) , \mathcal { H } ^ { - q _ { 2 } } ( f _ { 2 } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) )
$$

$$
{ } ^ { ( b ) } \mathcal { E } _ { p q } ^ { 2 } = \mathcal { H } ^ { - p } ( f _ { 1 } \times _ { \mathrm{S} } f _ { 2 } , \mathfrak { C o r } _ { q } ^ { \mathrm{S} } ( \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) )
$$

$$
{ } ^ { ( a ^ { \prime } ) } \mathcal { E } _ { p q } ^ { 2 } = \bigoplus _ { q _ { 1 } + q _ { 2 } = q } \mathfrak { C o r } _ { p } ^ { \mathrm{S} } ( \mathscr { H } ^ { - q _ { 1 } } ( f _ { 1 } , \mathscr { P } _ { \bullet } ^ { ( 1 ) } ) , \mathscr { H } ^ { - q _ { 2 } } ( f _ { 2 } , \mathscr { P } _ { \bullet } ^ { ( 2 ) } ) )
$$

$$
{ } ^ { ( b ^ { \prime } ) } \mathcal { E } _ { p q } ^ { 2 } = \mathcal { H } ^ { - p } ( f _ { 1 } \times _ { \mathrm{S} } f _ { 2 } , \mathcal { T o r } _ { q } ^ { \mathrm{S} } ( \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) )
$$

$$
{ } ^ { ( c ) } \mathcal { E } _ { p q } ^ { 2 } = \bigoplus _ { q _ { 1 } + q _ { 2 } = q } \mathcal { T o r } _ { p } ^ { S } ( f _ { 1 } , f _ { 2 } ; \mathcal { H } _ { q _ { 1 } } ( \mathcal { P } _ { \bullet } ^ { ( 1 ) } ) , \mathcal { H } _ { q _ { 2 } } ( \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) )
$$

$$
{ } ^ { ( d ) } \mathcal { E } _ { p q } ^ { 2 } = \mathcal { H } _ { p } ( \mathcal { T o r } _ { q } ^ { \mathrm{S} } ( f _ { 1 } , f _ { 2 } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) )
$$

On dit que les suites spectrales (a) et (b) sont les suites spectrales de Künneth.

On notera que les suites spectrales (a) et (a') (resp. (b) et (b')) sont identiques lorsque $\mathcal{P}_{\bullet}^{(1)}$ et $\mathcal{P}_{\bullet}^{(2)}$ se réduisent à leurs termes de degré o; dans ce cas, les suites (c) et (d) sont dégénérées et sont donc sans intérêt.

Remarque (6.7.4). Les hypertor globaux que nous avons définis ci-dessus comprennent comme cas particuliers, à la fois les Modules d'hypercohomologie définis dans (6.2.1) et les hypertor locaux définis dans (6.5.3). Montrons que l'on a, pour tout morphisme $f: \mathbf{X} \to \mathbf{Y}$ quasi-compact et séparé et tout complexe $\mathcal{P}$. de $\mathcal{O}_{\mathbf{X}}$-Modules quasi-cohérents, limité inférieurement, un isomorphisme canonique de $\partial$-foncteurs en $\mathcal{P}$.

(6.7.4.1)

$$
\mathfrak {C o r} _ {n} ^ {\mathrm{Y}} (f, \mathrm{I} _ {\mathrm{Y}}; \mathcal {P} _ {\bullet}, \mathcal {O} _ {\mathrm{Y}}) \simeq \mathcal {H} ^ {- n} (f, \mathcal {P} _ {\bullet})\tag{pour tout \(n\in \mathbf{Z}\)).}
$$

En effet, les méthodes de recollement de (6.7.2) ramènent aussitôt au cas où Y est affine; on peut alors, en vertu de (6.2.2), calculer les deux membres de (6.7.4.1) à l'aide d'un même recouvrement fini U de Y par des ouverts affines, et (pour le premier membre) du recouvrement de Y formé de Y lui-même; avec les notations de (6.6.2), le bicomplexe  $L_{\bullet\bullet}^{(2)}$  est alors réduit à son terme de degrés (o, o), égal à A, et la conclusion résulte de (0, 11.7.5). Pour une généralisation de ce résultat, voir (6.7.7); mais on notera que lorsque dans le premier membre de (6.7.4.1), on remplace  $O_{Y}$  par un  $O_{Y}$ -Module quasi-cohérent quelconque F, on n'a plus en général un isomorphisme avec  $\mathcal{H}^{-n}(f,\mathcal{P}_{\bullet}\otimes_{\mathcal{O}_{Y}}\mathcal{F})$ , bien que, dans le calcul précédent, le bicomplexe  $L_{\bullet\bullet}^{(1)}\otimes_{A}L_{\bullet\bullet}^{(2)}$  s'identifie encore au bicomplexe  $C^{\bullet}(\mathfrak{U},\mathcal{P}_{\bullet}\otimes_{\mathbb{Y}}\mathcal{F})$ .

D'autre part, on a un isomorphisme canonique de bi-∂-foncteurs

$$
\mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} \left(\mathrm{I} _ {\mathrm{X} ^ {(1)}}, \mathrm{I} _ {\mathrm{X} ^ {(2)}}; \mathcal {P} _ {\bullet} ^ {(1)}, \mathcal {P} _ {\bullet} ^ {(2)}\right) \stackrel {{\sim}} {{\to}} \mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} \left(\mathcal {P} _ {\bullet} ^ {(1)}, \mathcal {P} _ {\bullet} ^ {(2)}\right).\tag{6.7.4.2}
$$

En effet, on se ramène encore, par (6.7.1) et (6.7.2), au cas où S et les  $\mathbf{X}^{(i)}$  sont affines; dans le calcul du premier membre de (6.7.4.2), on peut alors prendre pour

recouvrement $\mathfrak{U}^{(i)}$ la famille réduite au seul élément $\mathrm{X}^{(i)}$, de sorte qu'avec les notations de (6.6.2), $\mathrm{L}_{\bullet \bullet}^{(i)}$ se réduit à $\Gamma (\mathbf{X}^{(i)},\mathcal{P}_{\bullet}^{(i)})$ (considéré comme bicomplexe dont les termes de premier degré $\neq 0$ sont nuls), et l'égalité des deux membres de (6.7.4.2) résulte de (6.4.1.1) et (6.3.1).

Proposition (6.7.5). — Soit $u: \mathcal{P}_{\bullet}^{(1)} \to \mathcal{Q}_{\bullet}^{(1)}$ un homomorphisme de complexes de $\mathcal{O}_{\mathrm{X}}^{(1)}$-Modules quasi-cohérents, limités inférieurement, tel que l'homomorphisme

$$
\mathcal {H} _ {\bullet} (u): \mathcal {H} _ {\bullet} (\mathcal {P} _ {\bullet} ^ {(1)}) \rightarrow \mathcal {H} _ {\bullet} (\mathcal {Q} _ {\bullet} ^ {(1)})
$$

déduit de u soit un isomorphisme. Alors les homomorphismes

$$
{ } ^ { ( t ) } \mathcal { E } ( f _ { 1 } , f _ { 2 } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) \to { } ^ { ( t ) } \mathcal { E } ( f _ { 1 } , f _ { 2 } ; \mathcal { Q } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } )
$$

déduits de u sont des isomorphismes pour t=a, t=b et t=c.

L'assertion relative à la suite spectrale (c) résulte de ce que cette suite est birégulière et de ce que l'homomorphisme considéré est un isomorphisme pour les termes  $E_{2}$  par hypothèse (0, 11.1.5). Ceci montre déjà que  $\mathcal{G}or_{\bullet}^{\mathrm{S}}(f_{1}, f_{2}; \mathcal{P}_{\bullet}^{(1)}, \mathcal{P}_{\bullet}^{(2)}) \to \mathcal{G}or_{\bullet}^{\mathrm{S}}(f_{1}, f_{2}; \mathcal{Q}_{\bullet}^{(1)}, \mathcal{P}_{\bullet}^{(2)})$  est un isomorphisme. Appliquant les relations (6.7.4.1) et (6.7.4.2) on voit d'abord que les homomorphismes  $\mathcal{H}^{-n}(f_{1}, \mathcal{P}_{\bullet}^{(1)}) \to \mathcal{H}^{-n}(f_{1}, \mathcal{Q}_{\bullet}^{(1)})$  et  $\mathcal{G}or_{n}^{\mathrm{S}}(\mathcal{P}_{\bullet}^{(1)}, \mathcal{P}_{\bullet}^{(2)}) \to \mathcal{G}or_{n}^{\mathrm{S}}(\mathcal{Q}_{\bullet}^{(1)}, \mathcal{P}_{\bullet}^{(2)})$  déduits de u sont des isomorphismes. L'assertion relative aux suites (a) et (b) résulte alors de ce que ces suites sont birégulières (6.7.3) et que les homomorphismes considérés sont bijectifs pour les termes  $E_{2}$  (0, 11.1.5).

Notons d'autre part que, si $u: \mathcal{P}_{\bullet}^{(1)} \to \mathcal{Q}_{\bullet}^{(1)}$ est un homotopisme, on en déduit des isomorphismes canoniques $^{(t)} \mathcal{E}(f_1, f_2; \mathcal{P}_{\bullet}^{(1)}, \mathcal{P}_{\bullet}^{(2)}) \to ^{(t)} \mathcal{E}(f_1, f_2; \mathcal{Q}_{\bullet}^{(1)}, \mathcal{P}_{\bullet}^{(2)})$ pour les six suites spectrales. En effet, si S et les $Y^{(i)}$ sont affines, on déduit de $u$ un homotopisme de bicomplexes $C^{\bullet}(\mathfrak{U}^{(1)}, \mathcal{P}_{\bullet}^{(1)}) \to C^{\bullet}(\mathfrak{U}^{(1)}, \mathcal{Q}_{\bullet}^{(1)})$, et la proposition résulte de la théorie générale de l'hyperhomologie (0, 11.3.2); le passage au cas général se fait par recollement, en utilisant le fait que, d'un homotopisme de complexes, on déduit un homotopisme de résolutions projectives de Cartan-Eilenberg de ces complexes (M, XVII, 1.2).

Proposition (6.7.6). — Supposons que le complexe $\mathcal{P}_{\bullet}^{(1)}$ ou le complexe $\mathcal{P}_{\bullet}^{(2)}$ soit formé de Modules S-plats (les deux complexes étant limités inférieurement). On a alors un isomorphisme canonique de bi-$\partial$-foncteurs

$$
\mathfrak {C o r} _ {n} ^ {\mathrm{S}} \left(f _ {1}, f _ {2}; \mathcal {P} _ {\bullet} ^ {(1)}, \mathcal {P} _ {\bullet} ^ {(2)}\right) \stackrel {{\sim}} {{\rightarrow}} \mathcal {H} ^ {- n} \left(f _ {1} \times_ {\mathrm{S}} f _ {2}, \mathcal {P} _ {\bullet} ^ {(1)} \otimes_ {\mathrm{S}} \mathcal {P} _ {\bullet} ^ {(2)}\right).\tag{6.7.6.x}
$$

Supposons d'abord S,  $\mathbf{Y}^{(1)}$  et  $\mathbf{Y}^{(2)}$  affines, de sorte qu'on est dans la situation de (6.6.2), dont nous conservons les notations. Supposons par exemple que  $\mathcal{P}_{\bullet}^{(1)}$  soit formé de Modules S-plats, et calculons l'hypertor en utilisant la remarque (6.6.6) : c'est donc l'homologie de  $\mathrm{L}_{\bullet\bullet}^{(1)}\otimes_{\mathrm{A}}\mathrm{M}_{\bullet\bullet}^{(2)}$ , où  $M_{\bullet\bullet}^{(2)}$  est une résolution projective de Cartan-Eilenberg de  $\mathrm{L}_{\bullet\bullet}^{(2)}$ , au sens de (0, 11.7.1). D'autre part, les modules  $\mathrm{L}_{ij}^{(1)}$  sont plats sur A en vertu de l'hypothèse (1.4.15.1); on déduit alors de (0, 11.7.5) un isomorphisme canonique

$$
\mathbf {T o r} _ {\bullet} ^ {\mathrm{S}} (\mathfrak {U} ^ {(1)}, \mathfrak {U} ^ {(2)}; \mathcal {P} _ {\bullet} ^ {(1)}, \mathcal {P} _ {\bullet} ^ {(2)}) \xrightarrow {\sim} \mathcal {H} _ {\bullet} (\mathrm{L} _ {\bullet \bullet} ^ {(1)} \otimes_ {\mathrm{A}} \mathrm{L} _ {\bullet \bullet} ^ {(2)}).\tag{6.7.6.2}
$$

On a d'autre part un homomorphisme naturel de bicomplexes de $\mathbf{L}_{\bullet \bullet}^{(1)}\otimes_{\Lambda}\mathbf{L}_{\bullet \bullet}^{(2)}$ dans $\mathbf{C}^{\bullet}(\mathfrak{U},\mathcal{Q}_{\bullet})$, où $\mathfrak{U}$ est le recouvrement de $Z = X^{(1)}\times_{S}X^{(2)}$ par les ouverts affines

$U_{\alpha}^{(1)} \times _{S} U_{\beta}^{(2)}$ et $2_{\bullet} = \mathcal{P}_{\bullet}^{(1)} \otimes _{S} \mathcal{P}_{\bullet}^{(2)}$ (considéré comme complexe simple pour le degré total); en effet, la définition de cet homomorphisme a en substance été donnée au cours du calcul de la suite $(b')$ dans (6.6.4), pour $q = 0$; il suffit simplement (en gardant les notations de (6.6.4)) de tenir compte de ce qu'il y a d'une part un homomorphisme naturel du complexe $N^{\bullet k}$ dans le complexe $C^{\bullet}(\Phi^{(1)}, \Phi^{(2)}; \mathcal{S}_k)$ (0, 11.8.5), d'autre part un homomorphisme naturel de ce dernier complexe dans le complexe $P^{\bullet}(\Phi^{(1)}, \Phi^{(2)}; \mathcal{S}_k)$ (0, 11.8.6), et enfin un homomorphisme naturel de ce dernier complexe de cochaînes dans le sous-complexe des cochaînes alternées (0, 11.8.7). Par ailleurs, l'homomorphisme de bicomplexes ainsi défini donne un isomorphisme en homologie, comme on l'a vu en (6.6.4); on a donc, en composant avec (6.7.6.2), obtenu un isomorphisme

$$
\mathbf {T o r} _ {n} ^ {\mathrm{S}} (\mathfrak {U} ^ {(1)}, \mathfrak {U} ^ {(2)}; \mathcal {P} _ {\bullet} ^ {(1)}, \mathcal {P} _ {\bullet} ^ {(2)}) \simeq \mathbf {H} ^ {- n} (\mathfrak {U}, \mathcal {P} _ {\bullet} ^ {(1)} \otimes_ {\mathrm{S}} \mathcal {P} _ {\bullet} ^ {(2)}).\tag{6.7.6.3}
$$

Il faut ensuite prouver que l'isomorphisme ainsi défini ne dépend pas des recouvrements ouverts choisis (le second membre de (6.7.6.3) étant canoniquement isomorphe à $\mathbf{H}^{-n}(\mathbf{X}^{(1)}\times_{\mathrm{S}}\mathbf{X}^{(2)},\mathcal{P}_{\bullet}^{(1)}\otimes_{\mathrm{S}}\mathcal{P}_{\bullet}^{(2)})$ par (6.2.2)); cela se fait à l'aide de (6.6.7) en remarquant (avec les notations de (6.6.7)) que l'on a un diagramme commutatif à homotopismes près

$$
\begin{array}{c c c} \mathrm{C} ^ {\bullet} (\mathfrak {U} ^ {(1)}, \mathcal {P} _ {\bullet} ^ {(1)}) \otimes_ {\mathrm{A}} \mathrm{C} ^ {\bullet} (\mathfrak {U} ^ {(2)}, \mathcal {P} _ {\bullet} ^ {(2)}) & \to & \mathrm{C} ^ {\bullet} (\mathfrak {U}, \mathcal {Q} _ {\bullet}) \\ \Bigg \downarrow & & \Bigg \downarrow \\ \mathrm{C} ^ {\bullet} (\mathfrak {V} ^ {(1)}, \mathcal {P} _ {\bullet} ^ {(1)}) \otimes_ {\mathrm{A}} \mathrm{C} ^ {\bullet} (\mathfrak {V} ^ {(2)}, \mathcal {P} _ {\bullet} ^ {(2)}) & \to & \mathrm{C} ^ {\bullet} (\mathfrak {V}, \mathcal {Q} _ {\bullet}) \end{array}
$$

où les flèches horizontales sont les homomorphismes définis ci-dessus. Enfin, il faut passer au cas général par recollement, ce qui se fait sans difficulté comme dans (6.7.1) et (6.7.2); nous laissons les détails au lecteur.

Proposition (6.7.7). — Supposons que $\mathcal{P}_{\bullet}^{(1)}$ et $\mathcal{P}_{\bullet}^{(2)}$ soient limités inférieurement, et que tous les Modules $\mathcal{H}^{-n}(f_{1},\mathcal{P}_{\bullet}^{(1)})$ ou tous les Modules $\mathcal{H}^{-n}(f_{2},\mathcal{P}_{\bullet}^{(2)})$ soient S-plats. On a alors un isomorphisme canonique de bi-$\partial$-foncteurs ($n$ parcourant $\mathbf{Z}$)

$$
\mathcal {C} o r _ {n} ^ {\mathrm{S}} (f _ {1}, f _ {2}; \mathcal {P} _ {\bullet} ^ {(1)}, \mathcal {P} _ {\bullet} ^ {(2)}) \underset {\rightarrow} {\sim} \bigoplus_ {q _ {1} + q _ {2} = n} \partial \mathcal {H} ^ {- q _ {1}} (f _ {1}, \mathcal {P} _ {\bullet} ^ {(1)}) \otimes_ {\mathrm{S}} \partial \mathcal {H} ^ {- q _ {2}} (f _ {2}, \mathcal {P} _ {\bullet} ^ {(2)}). \tag {6.7.7.I}
$$

En effet, vu (6.5.8), la suite spectrale (a) de (6.7.3) est dégénérée, et la proposition résulte aussitôt de (0, 11.1.6), cette suite étant birégulière (6.7.3).

Théorème (6.7.8). — Supposons que : 1$^{0}$ les complexes $\mathcal{P}_{\bullet}^{(1)}$ et $\mathcal{P}_{\bullet}^{(2)}$ soient limités inférieurement ; 2$^{0}$ le complexe $\mathcal{P}_{\bullet}^{(1)}$ ou le complexe $\mathcal{P}_{\bullet}^{(2)}$ soit formé de Modules S-plats ; 3$^{0}$ tous les

Modules $\mathcal{H}^{-n}(f_{1},\mathcal{P}_{\bullet}^{(1)})$ ou tous les Modules $\mathcal{H}^{-n}(f_{2},\mathcal{P}_{\bullet}^{(2)})$ soient S-plats. On a alors un isomorphisme canonique de bi-$\partial$-foncteurs ($n$ parcourant $\mathbf{Z}$)

$$
\mathcal {H} ^ {n} (f _ {1} \times_ {\mathrm{S}} f _ {2}, \mathcal {P} _ {\bullet} ^ {(1)} \otimes_ {\mathrm{S}} \mathcal {P} _ {\bullet} ^ {(2)}) \underset {\rightarrow} {\sim} \bigoplus_ {n _ {1} + n _ {2} = n} \mathcal {H} ^ {n _ {1}} (f _ {1}, \mathcal {P} _ {\bullet} ^ {(1)}) \otimes_ {\mathrm{S}} \mathcal {H} ^ {n _ {2}} (f _ {2}, \mathcal {P} _ {\bullet} ^ {(2)}) \tag {6.7.8.i}
$$

(« formule de Künneth »).

Cela résulte de (6.7.6) et (6.7.7).

Lorsque S,  $Y^{(1)}$  et  $Y^{(2)}$  sont affines, l'isomorphisme réciproque de (6.7.8.1) se déduit (avec les notations de (6.7.6)) de l'homomorphisme de bicomplexes

$$
\mathrm{C} ^ {\bullet} \left(\mathfrak {U} ^ {(1)}, \mathscr {P} _ {\bullet} ^ {(1)}\right) \otimes_ {\mathrm{A}} \mathrm{C} ^ {\bullet} \left(\mathfrak {U} ^ {(2)}, \mathscr {P} _ {\bullet} ^ {(2)}\right)\rightarrow \mathrm{C} ^ {\bullet} (\mathfrak {U}, \mathscr {Q} _ {\bullet})
$$

par le procédé défini dans (G, I, 2.7), comme il résulte de (G, I, 5.5).

Proposition (6.7.9). — Supposons vérifiées les trois conditions suivantes :

$^{10}$  S,  $\mathbf{Y}^{(1)}$  et  $\mathbf{Y}^{(2)}$  sont localement noethériens,  $f_{1}$  et  $f_{2}$  sont propres,  $\mathbf{Y}^{(1)}$  ou  $\mathbf{Y}^{(2)}$  de type fini sur S.

$2^{0} \mathcal{P}_{\bullet}^{(1)} \text{ et } \mathcal{P}_{\bullet}^{(2)} \text{ sont limités inférieurement.}$

$3^{0}$ Pour tout $n\in\mathbf{Z}$, $\mathcal{H}_{n}(\mathcal{P}_{\bullet}^{(i)})$ est un Module cohérent $(i=1,2)$.

Dans ces conditions, $\mathcal{C}\text{or}_n^{\mathrm{S}}(f_1,f_2;\mathcal{P}_{\bullet}^{(1)},\mathcal{P}_{\bullet}^{(2)})$ est un $\mathcal{O}_{\mathrm{Y}}$-Module cohérent (avec $\mathbf{Y} = \mathbf{Y}^{(1)}\times_{\mathrm{S}}\mathbf{Y}^{(2)}$).

Il résulte de (6.5.13) que les hypertor locaux $\mathcal{E}or_{n}^{\mathrm{S}}(\mathcal{P}_{\bullet}^{(1)},\mathcal{P}_{\bullet}^{(2)})$ sont des $\mathcal{O}_{\mathrm{X}}$-Modules cohérents $(\mathbf{X} = \mathbf{X}^{(1)}\times_{\mathrm{S}}\mathbf{X}^{(2)}$ étant localement noethérien, car un des $\mathbf{X}^{(i)}$ est par hypothèse de type fini sur S (I, 6.3.4 et 6.3.8)). Comme Y est localement noethérien et $f_{1}\times_{\mathrm{S}}f_{2}$ propre (II, 5.4.2), il résulte de (6.2.5) que les termes ${}^{(b)}\mathcal{E}_{pq}^{2}$ de (6.7.3) sont des $\mathcal{O}_{\mathrm{Y}}$-Modules cohérents. Comme toutes les suites spectrales de (6.7.3) sont birégulières en vertu de l'hypothèse $2^{0}$, on conclut par (0, 11.1.8).

(6.7.10) Soient maintenant  $Y^{\prime(i)}$  deux S-préschémas,  $v_{i}:Y^{\prime(i)}\to Y^{(i)}$  deux S-morphismes  $(i=1,2)$,  $v:v_{1}\times_{S}v_{2}$  leur produit, qui est un S-morphisme  $Y^{\prime}\to Y$, où l'on pose  $Y^{\prime}=Y^{\prime(1)}\times_{S}Y^{\prime(2)}$. Considérons d'autre part, pour i=1,2, un S-préschéma  $X^{\prime(i)}$, et deux S-morphismes  $u_{i}:X^{\prime(i)}\to X^{(i)},f_{i}^{\prime}:X^{\prime(i)}\to Y^{\prime(i)}$, de sorte que les diagrammes

$$
\begin{array}{c c c} \mathbf {X} ^ {\prime (i)} & \xrightarrow {u _ {i}} & \mathbf {X} ^ {(i)} \\ f _ {i} ^ {\prime} \Big \downarrow & & \Big \downarrow f _ {i} \\ \mathbf {Y} ^ {\prime (i)} & \xrightarrow [ v _ {i} ] & \mathbf {Y} ^ {(i)} \end{array}\tag{6.7.10.1}
$$

soient commutatifs, les morphismes $f_{i}^{\prime}$ étant séparés et quasi-compacts. On a alors des $\mathcal{O}_{\mathrm{Y}^{\prime}}$-homomorphismes canoniques de foncteurs spectraux

$$
v ^ {*} (^ {(t)} \mathcal {E} (f _ {1}, f _ {2}; \mathcal {P} _ {\bullet} ^ {(1)}, \mathcal {P} _ {\bullet} ^ {(2)})) \rightarrow^ {(t)} \mathcal {E} (f _ {1} ^ {\prime}, f _ {2} ^ {\prime}; u _ {1} ^ {*} (\mathcal {P} _ {\bullet} ^ {(1)}), u _ {2} ^ {*} (\mathcal {P} _ {\bullet} ^ {(2)}))\tag{6.7.10.2}
$$

pour $t=a$, $a'$, $b$, $b'$, $c$, $d$. Pour les définir, supposons d'abord $\mathrm{S}=\mathrm{Spec}(\mathrm{A})$, $\mathrm{Y}^{(i)}=\mathrm{Spec}(\mathrm{B}_{i})$, $\mathrm{Y}'^{(i)}=\mathrm{Spec}(\mathrm{B}_{i}')$ affines; les $\mathbf{X}^{(i)}$ et $\mathbf{X}'^{(i)}$ sont alors des schémas quasi-compacts. Pour calculer les suites spectrales ${ }^{(i)}\mathcal{E}(f_{1},f_{2};\mathcal{P}_{\bullet}^{(1)},\mathcal{P}_{\bullet}^{(2)})$, nous considérerons comme dans (6.6.1) des recouvrements finis $\mathfrak{U}^{(i)}$ par des ouverts affines de $\mathbf{X}^{(i)}$ ($i=1,2$); pour calculer ${ }^{(i)}\mathcal{E}(f_{1}',f_{2}';u_{1}^{*}(\mathcal{P}_{\bullet}^{(1)}),u_{2}^{*}(\mathcal{P}_{\bullet}^{(2)}))$, nous considérerons des recouvrements finis $\mathfrak{U}'^{(i)}$

de $\mathbf{X}^{\prime(i)}$ par des ouverts affines, plus fins respectivement que les recouvrements $u_i^{-1}(\mathfrak{U}^{(i)})$ ($i=1,2$). Il est clair que le bicomplexe $\mathbf{C}^{\bullet}(\mathfrak{U}^{(i)},\mathcal{P}_{\bullet}^{(i)})=\mathbf{L}_{\bullet\bullet}^{(i)}$ peut être considéré canoniquement comme un sous-bicomplexe de $\mathbf{C}^{\bullet}(u_{i}^{-1}(\mathfrak{U}^{(i)}),u_{i}^{*}(\mathcal{P}_{\bullet}^{(i)}))$ ($\mathbf{0}_{\mathrm{I}},4.4.3.2$); en outre, en choisissant une application simpliciale (G, II, 5.7) de $\mathfrak{U}^{\prime(i)}$ dans $u_{i}^{-1}(\mathfrak{U}^{(i)})$, on définit un homomorphisme de bicomplexes $\mathbf{C}^{\bullet}(u_{i}^{-1}(\mathfrak{U}^{(i)}),u_{i}^{*}(\mathcal{P}_{\bullet}^{(i)}))\to\mathbf{C}^{\bullet}(\mathfrak{U}^{\prime(i)},u_{i}^{*}(\mathcal{P}_{\bullet}^{(i)}))$ d'où, par composition, un homomorphisme de bicomplexes $\mathbf{L}_{\bullet\bullet}^{(i)}\to\mathbf{L}_{\bullet\bullet}^{\prime(i)}=\mathbf{C}^{\bullet}(\mathfrak{U}^{\prime(i)},u_{i}^{*}(\mathcal{P}_{\bullet}^{(i)}))$. En outre, cet homomorphisme est remplacé par un homomorphisme homotope quand on change d'application simpliciale (G, II, 5.7.1); on a ainsi un homomorphisme bien défini de foncteurs spectraux :

$$
{ } ^ { ( t ) } \mathcal { E } ( \mathfrak { U } ^ { ( 1 ) } , \mathfrak { U } ^ { ( 2 ) } ; \mathscr { P } _ { \bullet } ^ { ( 1 ) } , \mathscr { P } _ { \bullet } ^ { ( 2 ) } ) \to { } ^ { ( t ) } \mathcal { E } ( \mathfrak { U } ^ { \prime ( 1 ) } , \mathfrak { U } ^ { \prime ( 2 ) } ; u _ { 1 } ^ { * } ( \mathscr { P } _ { \bullet } ^ { ( 1 ) } ) , u _ { 2 } ^ { * } ( \mathscr { P } _ { \bullet } ^ { ( 2 ) } ) ) .\tag{6.7.10.3}
$$

On vérifie aussitôt que si $\mathfrak{B}^{(i)}$ est un recouvrement affine fini de $\mathbf{X}^{(i)}$ plus fin que $\mathfrak{U}^{(i)},\mathfrak{B}'^{(i)}$ un recouvrement affine fini de $\mathbf{X}'^{(i)}$, plus fin que $u_i^{-1}(\mathfrak{U}'^{(i)})$ et que $\mathfrak{B}^{(i)}$, le diagramme

$$
\begin{array}{c c c} \mathrm{C} ^ {\bullet} (\mathfrak {U} ^ {(i)}, \mathcal {P} _ {\bullet} ^ {(i)}) & \to & \mathrm{C} ^ {\bullet} (\mathfrak {V} ^ {(i)}, \mathcal {P} _ {\bullet} ^ {(i)}) \\ \Bigg \downarrow & & \Bigg \downarrow \\ \mathrm{C} ^ {\bullet} (\mathfrak {U} ^ {\prime (i)}, u _ {i} ^ {*} (\mathcal {P} _ {\bullet} ^ {(i)})) & \to & \mathrm{C} ^ {\bullet} (\mathfrak {V} ^ {\prime (i)}, u _ {i} ^ {*} (\mathcal {P} _ {\bullet} ^ {(i)})) \end{array}
$$

est commutatif, ce qui implique que l'homomorphisme (6.7.10.3) ne dépend pas essentiellement des recouvrements $\mathfrak{U}^{(i)}$ et $\mathfrak{U}'^{(i)}$ considérés. On a donc en fait défini un homomorphisme de A-modules

$$
{ } ^ { ( t ) } \mathrm{E} ( \mathbf { X } ^ { ( 1 ) } , \mathbf { X } ^ { ( 2 ) } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) \to { } ^ { ( t ) } \mathrm{E} ( \mathbf { X } ^ { \prime ( 1 ) } , \mathbf { X } ^ { \prime ( 2 ) } ; u _ { 1 } ^ { * } ( \mathcal { P } _ { \bullet } ^ { ( 1 ) } ) , u _ { 2 } ^ { * } ( \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) )\tag{6.7.10.4}
$$

mais il est clair par définition des $u_i^*(\mathcal{P}_i^{(i)})$ et en vertu de la commutativité de (6.7.10.1) que cet homomorphisme est aussi un homomorphisme de $(\mathrm{B}_1 \otimes_A \mathrm{B}_2)$-modules; comme le second membre de (6.7.10.4) est formé de $(\mathrm{B}_1' \otimes_A \mathrm{B}_2')$-modules, on déduit canoniquement de (6.7.10.4) un homomorphisme de $(\mathrm{B}_1' \otimes_A \mathrm{B}_2')$-modules

$$
{ } ^ { ( t ) } \mathrm{E} ( \mathbf { X } ^ { ( 1 ) } , \mathbf { X } ^ { ( 2 ) } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) \otimes _ { \mathrm{B} _ { 1 } \otimes _ { A } \mathrm{B} _ { 2 } } ( \mathrm{B} _ { 1 } ^ { \prime } \otimes _ { A } \mathrm{B} _ { 2 } ^ { \prime } ) \to { } ^ { ( t ) } \mathrm{E} ( \mathbf { X } ^ { \prime ( 1 ) } , \mathbf { X } ^ { \prime ( 2 ) } ; u _ { 1 } ^ { * } ( \mathcal { P } _ { \bullet } ^ { ( 1 ) } ) , u _ { 2 } ^ { * } ( \mathcal { P } _ { \bullet } ^ { ( 2 ) } ) )
$$

ce qui, compte tenu de (I, 1.6.5) n'est autre que l'homomorphisme cherché (6.7.10.2) dans le cas particulier considéré.

Il reste à passer au cas général en suivant les recollements de (6.7.1) et (6.7.2); le second passage est immédiat; en ce qui concerne le premier, on considère comme dans (6.7.1) des éléments $g_i \in \mathbf{B}_i$, et leurs images $g_i' \in \mathbf{B}_i'$, le produit tensoriel $g = g_1 \otimes g_2$ dans $\mathbf{B} = \mathbf{B}_1 \otimes_{\mathbf{A}} \mathbf{B}_2$ et son image $g' = g_1' \otimes g_2'$ dans $\mathbf{B}' = \mathbf{B}_1' \otimes_{\mathbf{A}} \mathbf{B}_2'$, et tout revient à utiliser

l'isomorphisme canonique  $(\mathbf{M}\otimes_{\mathrm{B}}\mathbf{B}^{\prime})_{g^{\prime}}\simeq\mathbf{M}_{g}\otimes_{\mathrm{B}_{g}}\mathbf{B}^{\prime}_{g^{\prime}}$  (0, i.5.4); nous laissons les détails au lecteur.

(6.7.11) La théorie des hypertor globaux, développée ci-dessus pour deux S-morphismes  $\mathbf{X}^{(i)}\to\mathbf{Y}^{(i)}$  et deux complexes  $\mathcal{P}_{\bullet}^{(i)}$  de Modules quasi-cohérents limités inférieurement, s'étend aussitôt au cas général suivant : on a un préschéma S, une famille finie de S-préschémas  $\mathbf{Y}^{(i)}$  ( $i\in I$ ), une famille finie de S-morphismes séparés et quasi-compacts  $f_{i}:\mathbf{X}^{(i)}\to\mathbf{Y}^{(i)}$, et pour chaque i un complexe de  $\mathcal{O}_{\mathbf{X}^{(i)}}$-Modules quasi-cohérents  $\mathcal{P}_{\bullet}^{(i)}$  limités inférieurement. Si Y est le produit des S-préschémas  $\mathbf{Y}^{(i)}$, on définit alors pour chaque entier  $n\in\mathbf{Z}$, un  $O_{Y}$-Module quasi-cohérent  $\mathcal{C}\sigma r_{n}^{\mathrm{S}}((f_{i})_{i\in\mathrm{I}};(\mathcal{P}_{\bullet}^{(i)})_{i\in\mathrm{I}})$, ces Modules formant un  $\partial$-foncteur covariant en chacun des complexes  $\mathcal{P}_{\bullet}^{(i)}$; en outre, ce foncteur est l'aboutissement commun de six foncteurs spectraux  ${}^{(t)}\mathcal{E}((f_{i})_{i\in\mathrm{I}};(\mathcal{P}_{\bullet}^{(i)})_{i\in\mathrm{I}})$. Nous laissons au lecteur le soin de répéter pour ce cas général les définitions et les raisonnements faits ci-dessus pour  $I=\{1,2\}$. Notons simplement que lorsque I se réduit à un seul élément, on retrouve l'hypercohomologie  $\mathcal{H}^{\bullet}(f,\mathcal{P}_{\bullet})$  définie dans (6.2.7) (comme on l'a déjà observé dans (6.7.4)). Lorsque I est l'intervalle  $1\leqslant i\leqslant m$  de N, nous écrirons

$$
\mathfrak {C o r} _ {n} ^ {\mathrm{S}} \left(f _ {1}, \dots , f _ {m}; \mathcal {P} _ {\bullet} ^ {(1)}, \dots , \mathcal {P} _ {\bullet} ^ {(m)}\right) \quad \text {pour} \quad \mathfrak {C o r} _ {n} ^ {\mathrm{S}} \left(\left(f _ {i}\right) _ {i \in \mathrm{I}}; \mathcal {P} _ {\bullet} ^ {(i)}\right) _ {i \in \mathrm{I}}.
$$

Proposition (6.7.12). — Les notations étant celles de (6.7.11), soit J une partie de I telle que, pour  $i \in I - J$ , on ait  $\mathbf{X}^{(i)} = \mathbf{Y}^{(i)} = \mathbf{S}$ ,  $f_i$  étant réduit à l'identité, et  $\mathcal{P}_{\bullet}^{(i)}$  égal au complexe réduit au terme de degré o égal à  $O_S$ . Il y a alors un isomorphisme canonique de  $\partial$ -foncteurs

$$
\mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} ((f _ {i}) _ {i \in \mathrm{I}}; (\mathscr {P} _ {\bullet} ^ {(i)}) _ {i \in \mathrm{I}}) \xrightarrow {\sim} \mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} ((f _ {i}) _ {i \in \mathrm{J}}; (\mathscr {P} _ {\bullet} ^ {(i)}) _ {i \in \mathrm{J}}).\tag{6.7.12.1}
$$

On peut se borner à définir cet isomorphisme lorsque S et les  $Y^{(i)}$  sont affines, le recollement se faisant comme d'ordinaire. Pour  $i \in I - J$ , on peut prendre le recouvrement  $\mathfrak{U}^{(i)}$  formé du seul ensemble S, et alors  $\mathrm{L}_{\bullet\bullet}^{(i)} = \mathrm{C}^{\bullet}(\mathfrak{U}^{(i)}, \mathcal{P}_{\bullet}^{(i)})$  est réduit à son seul terme de degrés (o, o), égal à  $\Gamma(\mathrm{S}, \mathcal{O}_{\mathrm{S}}) = \mathrm{A}(\mathrm{S})$ ; l'isomorphisme (6.7.12.1) est alors évident.

Remarque (6.7.13). — Les notations étant celles de (6.7.3), considérons le S-isomorphisme canonique  $\mathbf{Y}^{(1)}\times_{\mathbb{S}}\mathbf{Y}^{(2)}\to\mathbf{Y}^{(2)}\times_{\mathbb{S}}\mathbf{Y}^{(1)}$  (I, 3.3.5); alors l'image par cet isomorphisme de  $\mathcal{E}\mathsf{or}_{\bullet}^{\mathrm{S}}(f_{1},f_{2};\mathcal{P}_{\bullet}^{(1)},\mathcal{P}_{\bullet}^{(2)})$  est  $\mathcal{E}\mathsf{or}_{\bullet}^{\mathrm{S}}(f_{2},f_{1}:\mathcal{P}_{\bullet}^{(2)},\mathcal{P}_{\bullet}^{(1)})$ ; la question étant locale, on est ramené au cas envisagé dans (6.6.2), et si on désigne par  $M_{\bullet\bullet}^{(i)}$  une résolution projective de Cartan-Eilenberg de  $L_{\bullet\bullet}^{(i)}$  (i=1,2), l'isomorphisme considéré transforme  $M_{\bullet\bullet}^{(1)}\otimes_{A}M_{\bullet\bullet}^{(2)}$  en  $M_{\bullet\bullet}^{(2)}\otimes_{A}M_{\bullet\bullet}^{(1)}$ , d'où notre assertion en considérant l'homologie des complexes simples associés à ces tricomplexes.

## 6.8. Les suites spectrales d'associativité des hypertor globaux.

(6.8.1) Les hypothèses et notations étant celles de (6.7.11) (et en particulier les $\mathcal{P}_{\bullet}^{(i)}$ étant supposés limités inférieurement, supposons donnée une partition $(\mathrm{I}_j)_{j\in \mathrm{J}}$ de l'ensemble d'indices I; nous nous proposons de donner une relation d'« associativité » entre les hypertor $\mathcal{Cor}_n^{\mathrm{S}}((f_i)_{i\in \mathrm{I}};(\mathcal{P}_{\bullet}^{(i)})_{i\in \mathrm{I}})$ et chacun des hypertor « partiels »

$$
\mathcal {T} _ {\bullet j} = \mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} ((f _ {i}) _ {i \in \mathrm{I} _ {j}}; (\mathcal {P} _ {\bullet} ^ {(i)}) _ {i \in \mathrm{I} _ {j}}).
$$

164

Pour simplifier l'écriture, nous nous bornerons au cas où I est l'intervalle $1 \leqslant i \leqslant m$, et où la partition $(I_j)$ se compose des deux intervalles $\{1, 2, \ldots, r\}$ et $\{r + 1, \ldots, m\}$. Proposition (6.8.2). — Il existe un foncteur spectral canonique birégulier (dit « foncteur spectral d'associativité ») noté

$$
{ } ^ { ( e ) } \mathcal { E } ^ { \mathrm{S} } ( f _ { 1 } , \dots , f _ { m } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \dots , \mathcal { P } _ { \bullet } ^ { ( m ) } ) \quad ( \text {   o   u   s   i   m   p   l   e   m   e   n   t   } \quad { } ^ { ( e ) } \mathcal { E } ( f _ { 1 } , \dots , f _ { m } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \dots , \mathcal { P } _ { \bullet } ^ { ( m ) } ) )
$$

dont l'aboutissement est $\mathfrak{Gor}_{\bullet}^{\mathrm{S}}(f_1,\ldots ,f_m;\mathcal{P}_{\bullet}^{(1)},\ldots ,\mathcal{P}_{\bullet}^{(m)})$ , et dont le terme $\mathrm{E}_2$ est donné par (e) $\mathcal{E}_{pq}^2 = \bigoplus_{q_1 + q_2 = q}\mathcal{T}or_q^{\mathrm{S}}(\mathfrak{Gor}_{q_1}^{\mathrm{S}}(f_1,\ldots ,f_r;\mathcal{P}_{\bullet}^{(1)},\ldots ,\mathcal{P}_{\bullet}^{(r)}),\mathfrak{Gor}_{q_2}^{\mathrm{S}}(f_{r + 1},\ldots ,f_m;\mathcal{P}_{\bullet}^{(r + 1)},\ldots ,\mathcal{P}_{\bullet}^{(m)})).$

Dans cet énoncé, on a identifié canoniquement Y au produit  $Z^{(1)} \times_{\mathrm{S}} Z^{(2)}$ , où  $Z^{(1)} = Y^{(1)} \times_{\mathrm{S}} Y^{(2)} \times \ldots \times_{\mathrm{S}} Y^{(r)}$ , et  $Z^{(2)} = Y^{(r+1)} \times_{\mathrm{S}} \ldots \times_{\mathrm{S}} Y^{(m)}$ . Nous nous bornerons au cas où S et les  $Y^{(i)}$  sont affines; on passe de ce cas particulier au cas général par les méthodes développées dans (6.7.1) et (6.7.2), et nous laissons les détails du raisonnement (sans difficulté) au lecteur. Nous démontrerons donc le

Corollaire (6.8.3). — Soient A un anneau, $S = \text{Spec}(A)$, $X^{(i)}$ ($i \leqslant i \leqslant m$) des S-schémas quasi-compacts et, pour chaque $i$, soit $\mathcal{P}_{\bullet}^{(i)}$ un complexe de $\mathcal{O}_{X^{(i)}}$-Modules quasi-cohérents limité inférieurement. Il existe un foncteur spectral canonique birégulier ayant pour aboutissement

$$
\mathbf {T o r} _ {\bullet} ^ {\mathrm{S}} \left(\mathrm{X} ^ {(1)}, \dots , \mathrm{X} ^ {(m)}; \mathscr {P} _ {\bullet} ^ {(1)}, \dots , \mathscr {P} _ {\bullet} ^ {(m)}\right)
$$

et dont le terme  $E_{2}$  est donné par

$$
\begin{array}{c} ^ {(e)} \mathrm{E} _ {p q} ^ {2} = \underset {q _ {1} + q _ {2} = q} {\oplus} \operatorname{Tor} _ {p} ^ {\mathrm{A}} (\mathbf {T o r} _ {q _ {1}} ^ {\mathrm{S}} (\mathrm{X} ^ {(1)}, \dots , \mathrm{X} ^ {(r)}; \mathcal {P} _ {\bullet} ^ {(1)}, \dots , \mathcal {P} _ {\bullet} ^ {(r)}), \\ \mathbf {T o r} _ {q _ {2}} ^ {\mathrm{S}} (\mathrm{X} ^ {(r + 1)}, \dots , \mathrm{X} ^ {(m)}; \mathcal {P} _ {\bullet} ^ {(r + 1)}, \dots , \mathcal {P} _ {\bullet} ^ {(m)}) \end{array}
$$

Suivant la définition donnée en (6.6.2), le calcul de l'hypertor considéré se fait en prenant pour chaque $i$ un recouvrement ouvert affine fini $\mathfrak{U}^{(i)}$ de $\mathbf{X}^{(i)}$, en considérant les bicomplexes $\mathbf{L}_{\bullet \bullet}^{(i)} = \mathbf{C}^{\bullet}(\mathfrak{U}^{(i)},\mathcal{P}_{\bullet}^{(i)})$, une résolution projective $\mathbf{M}_{\bullet \bullet}^{(i)}$ de Cartan-Eilenberg de chacun de ces bicomplexes (au sens de (0, 11.7.1)), le produit tensoriel $\mathbf{M}_{\bullet \bullet} = \bigotimes_{i=1}^{m}\mathbf{M}_{\bullet \bullet}^{(i)}$ de ces tricomplexes, et en prenant l'homologie de $\mathbf{M}_{\bullet \bullet}$. Considérons $\mathbf{M}_{\bullet \bullet}$ comme un complexe simple $\mathbf{N}_{\bullet}$, produit tensoriel des deux complexes simples

$$
\mathrm{N} _ {\bullet} ^ {\prime} = \bigotimes_ {i = 1} ^ {r} \mathrm{M} _ {\bullet \bullet \bullet} ^ {(i)}, \quad \mathrm{N} _ {\bullet} ^ {\prime \prime} = \bigotimes_ {i = r + 1} ^ {m} \mathrm{M} _ {\bullet \bullet \bullet} ^ {(i)},
$$

où N' et N'' sont gradués par la somme des degrés totaux des M$^{(i)}$ . En outre, les A-modules des complexes N' et N'' sont projectifs, donc il résulte de (6.5.9) que l'on a H.(M...) = Tor$^{A}$(N', N''); la suite spectrale cherchée n'est autre alors que la suite (6.3.2.2) appliquée aux complexes N' et N'', compte tenu de l'interprétation des modules d'homologie de ces complexes qui résulte de ce qui précède (quand on applique les remarques du début à chacun des produits partiels X$^{(1)}$ × s × ... ×s X$^{(r)}$ et X$^{(r+1)}$ × s × ... ×s X$^{(m)}$). Enfin, les propriétés de régularité résultent de (6.3.2) et du fait que, les $\mathcal{P}^{(i)}$ étant limités inférieurement, il en est de même des M$^{(i)}$; par suite, N' et N'' sont limités inférieurement.

## 6.9. Les suites spectrales de changement de base dans les hypertor globaux.

(6.9.1) Les hypothèses et notations étant toujours celles de (6.7.11) (et en particulier les $\mathcal{P}_{\bullet}^{(i)}$ étant supposés limités inférieurement), considérons un morphisme $g: S' \to S$ de préschémas, et posons $Y'^{(i)} = Y_{(S')}^{(i)}, X'^{(i)} = X_{(S')}^{(i)}$ et $\mathcal{P}_{\bullet}^{'(i)} = \mathcal{P}_{\bullet}^{(i)} \otimes_{\mathcal{O}_S} \mathcal{O}_{S'}$, $\mathcal{P}_{\bullet}^{'(i)}$ étant donc un complexe de $\mathcal{O}_{X'(i)}$-Modules quasi-cohérents; soit $f_i' = (f_i)_{(S')} : X'^{(i)} \to Y'^{(i)}$, qui est un morphisme séparé et quasi-compact (I, 5.5.1 et 6.6.4). Nous nous proposons d'étudier les relations entre les $\mathcal{O}_{Y'}$-Modules quasi-cohérents $\mathcal{Cor}_n^{S'}((f_i')_{i \in I}; (\mathcal{P}_{\bullet}^{(i)})_{i \in I})$ et $\mathcal{Cor}_n^{S}((f_i)_{i \in I}; (\mathcal{P}_{\bullet}^{(i)})_{i \in I}) \otimes_{\mathcal{O}_S} \mathcal{O}_{S'}$, où $Y' = Y \times_S S' = Y_{(S')}.$ Un cas particulièrement simple est le suivant, qui se réduit à (1.4.15) lorsque I se réduit à un seul élément et $\mathcal{P}$ à un seul module :

Proposition (6.9.2). — Si le morphisme $g: S' \to S$ est plat, on a un isomorphisme canonique de $\partial$-foncteurs (en les $\mathcal{P}_{\bullet}^{(i)}$):

$$
\mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} ((f _ {i}) _ {i \in \mathrm{I}}; (\mathcal {P} _ {\bullet} ^ {(i)}) _ {i \in \mathrm{I}}) \otimes_ {\mathcal {O} _ {\mathrm{s}}} \mathcal {O} _ {\mathrm{S} ^ {\prime}} \stackrel {{\sim}} {{\to}} \mathfrak {C o r} _ {\bullet} ^ {\mathrm{S} ^ {\prime}} ((f _ {i} ^ {\prime}) _ {i \in \mathrm{I}}; (\mathcal {P} _ {\bullet} ^ {(i)}) _ {i \in \mathrm{I}}).\tag{6.9.2.1}
$$

On peut encore se borner au cas où S, S' et les Y$^{(i)}$ sont affines, le recollement se faisant suivant les méthodes de (6.7.1) et (6.7.2). Soient S=Spec(A), S'=Spec(A'), et prenons pour chaque i un recouvrement ouvert affine U$^{(i)}$ de X$^{(i)}$; si $u_i: X'^{(i)} \to X^{(i)}$ est la projection canonique, $u_i^{-1}(\mathfrak{U}^{(i)})$ est un recouvrement ouvert affine de X'$^{(i)}$ (II, 1.5.5), que nous noterons U'$^{(i)}$; il est clair alors que C$^{\bullet}$(U'$^{(i)}$, P'$^{(i)}$) = C$^{\bullet}$(U$^{(i)}$, P'$^{(i)}$)⊗A A', et l'existence de l'isomorphisme (6.9.2.1) est immédiate, car si M$_{\bullet\bullet}^{(i)}$ est une résolution projective de Cartan-Eilenberg de L$^{(i)}$=C$^{\bullet}$(U$^{(i)}$, P'$^{(i)}$) au sens de (0, 11.7.1), formée de A-modules, M$_{\bullet\bullet}^{(i)}$⊗A A' est une résolution projective de Cartan-Eilenberg (au même sens) de L$^{(i)}$⊗A A' formée de A'-modules, en vertu de l'hypothèse que A' est un A-module plat; cette même hypothèse montre en outre que H.$_{i=1}^{m}$(M$_{\bullet\bullet}^{(i)}$⊗A A')=H.$_{i=1}^{m}$(M$_{\bullet\bullet}^{(i)}$)⊗A A'.

On notera que lorsque I est réduit au seul élément I, la formule (6.9.2.1) se déduit directement de (6.7.7), appliqué en prenant  $Y_{2}=X_{2}=S'$ ,  $f_{2}=I_{S'}$ , et le complexe  $\mathcal{P}^{(2)}$  réduit à son terme de degré o, égal à  $O_{S'}$ ; on sait alors que l'hypercohomologie  $\mathcal{H}^{n}(I_{S'},\mathcal{O}_{S'})$  est nulle pour tout  $n\neq0$  et se réduit à  $O_{S'}$  pour n=o (6.2.1).

Dans le cas général, nous allons introduire à la place de $\mathcal{O}_{\mathrm{S}'}$ un complexe $2'$ de $\mathcal{O}_{\mathrm{S}'}$-Modules quasi-cohérents limités inférieurement, de sorte que si, pour simplifier, on prend $\mathbf{I} = \{1, 2, \ldots, m\}$, on peut considérer le $\partial$-foncteur

$$
\mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} \left(f _ {1}, \dots , f _ {m}, \mathrm{I} _ {\mathrm{S} ^ {\prime}}; \mathscr {P} _ {\bullet} ^ {(1)}, \dots , \mathscr {P} _ {\bullet} ^ {(m)}, \mathscr {Q} _ {\bullet} ^ {\prime}\right).
$$

Proposition (6.9.3). — Il existe trois foncteurs spectraux canoniques biréguliers notés  $^{(t)}\mathcal{E}(f_{1},\ldots,f_{m};\mathcal{P}_{\bullet}^{(1)},\ldots,\mathcal{P}_{\bullet}^{(m)},2^{\prime})$  (avec t=e, f ou  $f^{\prime}$ ) ayant pour aboutissement commun  $\mathcal{Gor}_{\bullet}^{\mathrm{S}}(f_{1},\ldots,f_{m},\mathrm{I}_{\mathrm{S}^{\prime}};\mathcal{P}_{\bullet}^{(1)},\ldots,\mathcal{P}_{\bullet}^{(m)},2^{\prime})$  et dont les termes  $E_{2}$  sont respectivement

$$
{ } ^ { ( e ) } \mathcal { E } _ { p q } ^ { 2 } = \bigoplus _ { q ^ { \prime } + q ^ { \prime \prime } = q } \mathcal { T o r } _ { p } ^ { \mathrm{S} } ( \mathfrak { C o r } _ { q ^ { \prime } } ^ { \mathrm{S} } ( f _ { 1 } , \dots , f _ { m } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \dots , \mathcal { P } _ { \bullet } ^ { ( m ) } ) , \mathcal { H } _ { q ^ { \prime \prime } } ( \mathcal { Z } _ { \bullet } ^ { \prime } ) )
$$

$$
{ } ^ { ( f ) } \mathcal { E } _ { p q } ^ { 2 } = _ { q _ { 1 } + q _ { 2 } + \dots + q _ { m + 1 } = q } \bigoplus \mathcal { T o r } _ { p } ^ { S ^ { \prime } } ( \mathfrak { C o r } _ { q _ { 1 } } ^ { S } ( f _ { 1 } , \mathrm{I} _ { S ^ { \prime } } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { O } _ { S ^ { \prime } } ) , \dots ,\tag{\((\mathcal{L}^{\prime})\}
$$

$$
{ } ^ { ( \prime ) } \mathcal { E } _ { p q } ^ { 2 } = \bigoplus _ { q _ { 1 } + \dots + q _ { m } = q } \mathfrak { C o r } _ { p } ^ { S ^ { \prime } } ( f _ { 1 } ^ { \prime } , \dots , f _ { m } ^ { \prime } , \mathrm{I} _ { S ^ { \prime } } ; \mathcal { T o r } _ { q _ { 1 } } ^ { S } ( \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { O } _ { S ^ { \prime } } ) , \dots , \mathcal { T o r } _ { q _ { m } } ^ { S } ( \mathcal { P } _ { \bullet } ^ { ( m ) } , \mathcal { O } _ { S ^ { \prime } } ) , \mathcal { Z } _ { \bullet } ^ { \prime } )
$$

La suite (e) n'est autre que la suite d'associativité de (6.8.2) pour r=m. Pour définir les deux autres suites spectrales, on va encore se limiter au cas où S, S' et les  $Y^{(i)}$  sont affines, le passage au cas général se faisant par les méthodes de (6.7.1) et (6.7.2) et étant laissé au lecteur. Nous démontrerons donc le

Corollaire (6.9.4). — Soient A un anneau, A' une A-algèbre, S = Spec(A), S' = Spec(A'), X$^{(i)}$ (I ≤ i ≤ m) des S-schémas quasi-compacts et pour chaque i, soit X$^{(i)}$ = X$_{(S')}$, qui est un S'-schéma quasi-compact. Pour chaque i, soit P$_{i}$ un complexe de O$_{X^{(i)}}$-Modules quasi-cohérents; soit enfin Q'. un complexe de A'-modules, ces complexes étant limités inférieurement. Il existe trois foncteurs spectraux biréguliers en les P$_{i}$ et en Q', ayant pour aboutissement commun

$$
\mathbf {T o r} _ {\bullet} ^ {\mathrm{S}} \left(\mathrm{X} ^ {(1)}, \dots , \mathrm{X} ^ {(m)}, \mathrm{S} ^ {\prime}; \mathscr {P} _ {\bullet} ^ {(1)}, \dots , \mathscr {P} _ {\bullet} ^ {(m)}, \widetilde {\mathrm{Q}} _ {\bullet} ^ {\prime}\right)
$$

et dont les termes  $E_{2}$  sont respectivement

$$
{ } ^ { ( e ) } \mathrm{E} _ { p q } ^ { 2 } = \bigoplus _ { q ^ { \prime } + q ^ { \prime \prime } = q } \operatorname{Tor} _ { p } ^ { \mathrm{A} } ( \mathbf { T o r } _ { q ^ { \prime } } ^ { \mathrm{S} } ( \mathrm{X} ^ { ( 1 ) } , \dots , \mathrm{X} ^ { ( m ) } ; \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \dots , \mathcal { P } _ { \bullet } ^ { ( m ) } ) , \mathrm{H} _ { q ^ { \prime \prime } } ( \mathrm{Q} _ { \bullet } ^ { \prime } ) )
$$

$$
\begin{array}{c} ^ {(f)} \mathrm{E} _ {p q} ^ {2} = _ {q _ {1} + q _ {2} + \dots + q _ {m + 1} = q} \oplus \operatorname{Tor} _ {p} ^ {\mathrm{A} ^ {\prime}} (\mathbf {T o r} _ {q _ {1}} ^ {\mathrm{S}} (\mathrm{X} ^ {(1)}, \mathrm{S} ^ {\prime}; \mathcal {P} _ {\bullet} ^ {(1)}, \mathcal {O} _ {\mathrm{S} ^ {\prime}}), \dots , \\ \dots , \mathbf {T o r} _ {q _ {m}} ^ {\mathrm{S}} (\mathrm{X} ^ {(m)}, \mathrm{S} ^ {\prime}; \mathcal {P} _ {\bullet} ^ {(m)}, \mathcal {O} _ {\mathrm{S} ^ {\prime}}), \mathrm{H} _ {q _ {m + 1}} (\mathrm{Q} _ {\bullet} ^ {\prime})) \end{array}
$$

$$
{ } ^ { ( f ^ { \prime } ) } \mathrm{E} _ { p q } ^ { 2 } = \bigoplus _ { q _ { 1 } + \dots q _ { m } = q } \mathbf { T o r } _ { p } ^ { \mathrm{S} ^ { \prime } } ( \mathrm{X} ^ { \prime ( 1 ) } , \dots , \mathrm{X} ^ { \prime ( m ) } , \mathrm{S} ^ { \prime } ; \mathcal { T o r } _ { q _ { 1 } } ^ { \mathrm{S} } ( \mathcal { P } _ { \bullet } ^ { ( 1 ) } , \mathcal { O } _ { \mathrm{S} ^ { \prime } } ) , \dots , \mathcal { T o r } _ { q _ { m } } ^ { \mathrm{S} } ( \mathcal { P } _ { \bullet } ^ { ( m ) } , \mathcal { O } _ { \mathrm{S} ^ { \prime } } ) , \widetilde { \mathrm{Q} } _ { \bullet } ^ { \prime } ) .
$$

Nous ne reviendrons pas sur le premier de ces foncteurs spectraux, qui a été traité dans (6.8.3) et n'est inclus ici que pour mémoire. Pour définir les autres, considérons pour chaque $i$ un recouvrement ouvert affine fini $\mathfrak{U}^{(i)}$ de $\mathbf{X}^{(i)}$, et, si $u_i: \mathbf{X}'^{(i)} \to \mathbf{X}^{(i)}$ est la projection canonique, le recouvrement ouvert affine fini correspondant $\mathfrak{U}'^{(i)} = u_i^{-1}(\mathfrak{U}^{(i)})$. En vertu de (6.6.6), $\mathcal{Gor}_{\bullet}^{\mathrm{S}}(\mathbf{X}^{(1)}, \ldots, \mathbf{X}^{(m)}, \mathbf{S}', \mathcal{P}_{\bullet}^{(1)}, \ldots, \mathcal{P}_{\bullet}^{(m)}, \widetilde{\mathbf{Q}}_{\bullet}')$ s'obtient en prenant pour $1 \leqslant i \leqslant m$ une résolution projective de Cartan-Eilenberg $\mathbf{M}_{\bullet\bullet}^{(i)}$ de $\mathbf{L}_{\bullet\bullet}^{(i)} = \mathbf{C}^*(\mathfrak{U}^{(i)}, \mathcal{P}_{\bullet}^{(i)})$ (au sens de (0, 11.7.1)), considérant le tricomplexe $\mathbf{M}_{\bullet\bullet} = \mathbf{M}_{\bullet\bullet}^{(1)} \otimes_{\mathrm{A}} \mathbf{M}_{\bullet\bullet}^{(2)} \otimes \ldots \otimes_{\mathrm{A}} \mathbf{M}_{\bullet\bullet}^{(m)} \otimes_{\mathrm{A}} \mathbf{Q}_{\bullet}'$ (où $\mathbf{Q}_{\bullet}'$ est considéré comme un tricomplexe dont les deux derniers degrés se réduisent à o), et en en prenant l'homologie. Si l'on pose $\mathbf{M}_{\bullet\bullet}^{\prime(i)} = \mathbf{M}_{\bullet\bullet}^{(i)} \otimes_{\mathrm{A}} \mathbf{A}'$, on a (en se rappelant que $\mathbf{Q}_{\bullet}'$ est un complexe de A'-modules) $\mathbf{M}_{\bullet\bullet} = \mathbf{M}_{\bullet\bullet}^{\prime(1)} \otimes_{\mathrm{A}'} \mathbf{M}_{\bullet\bullet}^{\prime(2)} \otimes \ldots \otimes_{\mathrm{A}'} \mathbf{M}_{\bullet\bullet}^{\prime(m)} \otimes_{\mathrm{A}'} \mathbf{Q}_{\bullet}'$. Or, considérons chacun des complexes $\mathbf{M}_{\bullet\bullet}^{\prime(i)}$ comme un complexe simple (pour son degré total) et notons que ce complexe est formé de A'-modules projectifs; il résulte de (6.3.7) (étendu à un nombre quelconque de complexes) que $\mathbf{H}_{\bullet}(\mathbf{M}_{\bullet\bullet})$ est aussi égal à $\mathbf{Tor}_{\bullet}^{\mathrm{A}'}(\mathbf{M}_{\bullet\bullet}^{\prime(1)}, \ldots, \mathbf{M}_{\bullet\bullet}^{\prime(m)}, \mathbf{Q}_{\bullet}')$; c'est donc (6.5.15) l'aboutissement d'une suite spectrale ayant les propriétés de régularité voulues (les trois degrés de $\mathbf{M}_{\bullet\bullet}^{(i)}$ étant limités inférieurement lorsque $\mathcal{P}_{\bullet}^{(i)}$ est limité inférieurement) et dont le terme $\mathbf{E}_2$ est donné par

$$
\mathrm{E} _ {p q} ^ {2} = \underset {q _ {1} + \dots + q _ {m + 1} = q} {\oplus} \operatorname{Tor} _ {p} ^ {A ^ {\prime}} \left(\mathrm{H} _ {q _ {1}} \left(\mathrm{M} _ {\bullet \bullet} ^ {(1)}\right), \dots , \mathrm{H} _ {q _ {m}} \left(\mathrm{M} _ {\bullet \bullet} ^ {\prime (m)}\right), \mathrm{H} _ {q _ {m + 1}} \left(\mathrm{Q} _ {\bullet} ^ {\prime}\right)\right).
$$

On a d'ailleurs  $\mathrm{H}_{q_{i}}(\mathrm{M}^{\prime(i)})=\mathrm{H}_{q_{i}}(\mathrm{M}^{\prime(i)}\otimes_{\mathrm{A}}\mathrm{A}^{\prime})=\mathbf{T}\mathbf{o}\mathbf{r}_{q_{i}}^{\mathrm{S}}(\mathrm{X}^{(i)},\mathrm{S}^{\prime};\mathcal{P}^{(i)},\mathcal{O}_{\mathrm{S}^{\prime}})$  en vertu de la définition des hypertor globaux, ce qui donne la suite (f) cherchée. On peut d'autre part considérer  $\mathrm{M}^{\prime(i)}$  comme un bicomplexe dans lequel le premier degré est la somme du premier et du second degré du tricomplexe  $\mathrm{M}^{\prime(i)}$, le second degré étant le troisième degré de ce tricomplexe; comme les modules formant les  $\mathrm{M}^{\prime(i)}$  sont des A'-modules projectifs, la théorie générale de l'hyperhomologie montre que l'homologie du bicomplexe  $\mathrm{M}^{\prime(1)}\otimes_{\mathrm{A}^{\prime}}\mathrm{M}^{\prime(2)}\otimes\ldots\otimes_{\mathrm{A}^{\prime}}\mathrm{M}^{\prime(m)}\otimes_{\mathrm{A}^{\prime}}\mathrm{Q}^{\prime}$  est canoniquement isomorphe à son hyperhomologie (0, 11.6.5); c'est donc l'aboutissement d'une suite spectrale de terme  $E_{2}$  égal à

$$
\mathrm{E} _ {p q} ^ {2} = \underset {q _ {1} + \dots + q _ {m + 1} = q} {\oplus} \mathbf {T o r} _ {p} ^ {\mathrm{A} ^ {\prime}} \left(\mathrm{H} _ {q _ {1}} ^ {\mathrm{II}} \left(\mathrm{M} _ {\dots} ^ {\prime (1)}\right), \dots , \mathrm{H} _ {q _ {m}} ^ {\mathrm{II}} \left(\mathrm{M} _ {\dots} ^ {\prime (m)}\right), \mathrm{H} _ {q _ {m + 1}} ^ {\mathrm{II}} \left(\mathrm{Q} _ {\cdot}\right)\right).
$$

Or, comme le second degré de  $Q'$ . se réduit à o, on a  $H_{n}^{\mathrm{II}}(Q') = o$  pour  $n \neq o$  et  $H_{0}^{\mathrm{II}}(Q') = Q'$ ; la formule précédente s'écrit aussi

$$
\mathrm{E} _ {p q} ^ {2} = \bigoplus_ {q _ {1} + \dots + q _ {m} = q} \mathbf {T o r} _ {p} ^ {\mathrm{A} ^ {\prime}} (\mathrm{H} _ {q _ {1}} ^ {\mathrm{II}} (\mathrm{M} _ {\bullet \bullet} ^ {\prime (1)}), \dots , \mathrm{H} _ {q _ {m}} ^ {\mathrm{II}} (\mathrm{M} _ {\bullet \bullet} ^ {\prime (m)}), \mathrm{Q} _ {\bullet} ^ {\prime}).
$$

En outre, on a  $\mathrm{H}_{q_{i}}^{\mathrm{II}}(\mathbf{M}_{\bullet\bullet}^{\prime(i)})=\mathrm{H}_{q_{i}}^{\mathrm{II}}(\mathbf{M}_{\bullet\bullet}^{(i)}\otimes_{\mathrm{A}}\mathrm{A}^{\prime})=\mathrm{Tor}_{q_{i}}^{\mathrm{A}}(\mathbf{L}_{\bullet\bullet}^{(i)},\mathrm{A}^{\prime})$  en vertu de (6.3.4); mais  $\mathrm{L}_{-j,k}^{(i)}=\mathrm{C}^{j}(\mathfrak{U}^{(i)},\mathcal{P}_{k}^{(i)})$ , somme directe des  $\Gamma(\mathrm{V},\mathcal{P}_{k}^{(i)})$ , où V parcourt les intersections (affines) de  $j+\mathrm{i}$  ensembles du recouvrement  $\mathfrak{U}^{(i)}$ ; si  $V'=u_{i}^{-1}(\mathrm{V})$ ,  $V'$  est affine dans  $\mathbf{X}^{\prime(i)}$ , et il résulte de (6.4.1.1) que l'on a

$$
\Gamma (\mathrm{V} ^ {\prime}, \mathcal {T o r} _ {q _ {i}} ^ {\mathrm{S}} (\mathcal {P} _ {k} ^ {(i)}, \mathcal {O} _ {\mathrm{S} ^ {\prime}})) = \operatorname{Tor} _ {q _ {i}} ^ {\mathrm{A}} (\Gamma (\mathrm{V}, \mathcal {P} _ {k} ^ {(i)}), \mathrm{A} ^ {\prime})
$$

d'où pour le bicomplexeH  $_{q_{i}}^{\mathrm{II}}(\mathbf{M}^{\prime(i)})$  l'expression

$$
\mathbf {C} ^ {\bullet} \left(\mathfrak {U} ^ {\prime (i)}, \mathcal {T o r} _ {q _ {i}} ^ {\mathrm{S}} \left(\mathcal {P} _ {\bullet} ^ {(i)}, \mathcal {O} _ {\mathrm{S} ^ {\prime}}\right)\right)
$$

ce qui donne finalement l'expression cherchée pour le terme  $E_{2}$  de la suite  $(f')$ . Le fait que cette suite soit birégulière sous les conditions indiquées se vérifie comme d'ordinaire, tenant compte de ce que, si  $\mathcal{P}_{\bullet}^{(i)}$  est limité inférieurement, tous les degrés de  $M_{\bullet\bullet}^{(i)}$  sont limités inférieurement.

Remarque (6.9.5). — On voit comme dans (6.7.6) que le remplacement des $\mathcal{P}_{\bullet}^{(i)}$ et de $\mathcal{Q}'$ par des complexes qui leur sont respectivement homotopes ne change pas les suites $(e)$, $(f)$ et $(f')$ à un isomorphisme canonique près. En outre, pour la suite $(f)$, des homomorphismes $\mathcal{P}_{\bullet}^{(i)} \to \mathcal{R}_{\bullet}^{(i)}, \mathcal{Q}' \to \mathcal{T}'$ de complexes qui donnent des isomorphismes en homologie $\mathcal{H}_{\bullet}(\mathcal{P}_{\bullet}^{(i)}) \simeq \mathcal{H}_{\bullet}(\mathcal{R}_{\bullet}^{(i)}), \mathcal{H}_{\bullet}(\mathcal{Q}') \simeq \mathcal{H}_{\bullet}(\mathcal{T}')$ fournissent un isomorphisme de suites spectrales ${}^{(f)}\mathcal{E}(f_1, \ldots, f_m; \mathcal{P}_{\bullet}^{(1)}, \ldots, \mathcal{P}_{\bullet}^{(m)}, \mathcal{Q}') \simeq {}^{(f)}\mathcal{E}(f_1, \ldots, f_m: \mathcal{R}_{\bullet}^{(1)}, \ldots, \mathcal{R}_{\bullet}^{(m)}, \mathcal{T}')$; la démonstration est la même que pour (6.7.6) en tenant compte du résultat de (6.7.6) et de la régularité de la suite $(f)$.

Corollaire (6.9.6). — Sous les conditions de (6.9.1), supposons que :

$^{10}$ Les complexes $\mathcal{P}_{\bullet}^{(i)}$ sont formés de Modules plats sur S, et les $\mathcal{O}_{Y}$-Modules

$$
\mathcal {C o r} _ {n} ^ {\mathrm{S}} (f _ {1}, \dots , f _ {m}; \mathcal {P} _ {\bullet} ^ {(1)}, \dots , \mathcal {P} _ {\bullet} ^ {(m)})
$$

sont plats sur S.

$2^{0}$ Les $\mathcal{P}_{\bullet}^{(i)}$ et $2'$ sont limités inférieurement.

169

On a alors, en posant $\mathcal{P}^{\prime(i)} = \mathcal{P}^{\prime(i)}\otimes_{\mathcal{O}_{\mathfrak{s}}}\mathcal{O}_{\mathrm{S}^{\prime}}$ , des isomorphismes canoniques fonctoriels

$$
\begin{array}{c} \mathfrak {C o r} _ {n} ^ {\mathrm{S} ^ {\prime}} (f _ {1} ^ {\prime}, \ldots , f _ {m} ^ {\prime}, \mathrm{I} _ {\mathrm{S} ^ {\prime}}; \mathcal {P} _ {\bullet} ^ {(1)}, \ldots , \mathcal {P} _ {\bullet} ^ {(m)}, \mathcal {Q} _ {\bullet} ^ {\prime}) \stackrel {{\sim}} {{\to}} \\ \stackrel {{\sim}} {{\to}} \bigoplus_ {n ^ {\prime} + n ^ {\prime \prime} = n} \mathfrak {C o r} _ {n ^ {\prime}} ^ {\mathrm{S}} (f _ {1}, \ldots , f _ {m}; \mathcal {P} _ {\bullet} ^ {(1)}, \ldots , \mathcal {P} _ {\bullet} ^ {(m)}) \otimes_ {\mathrm{S}} \mathcal {H} _ {n ^ {\prime \prime}} (\mathcal {Q} _ {\bullet} ^ {\prime}). \end{array}\tag{6.9.6.1}
$$

En particulier, pour 2' réduit à un seul terme $\mathcal{F}'$ de degré o, on a des isomorphismes canoniques fonctoriels

$$
\mathfrak {C o r} _ {n} ^ {\mathrm{S} ^ {\prime}} (f _ {1} ^ {\prime}, \dots , f _ {m} ^ {\prime}, \mathrm{I} _ {\mathrm{S} ^ {\prime}}; \mathcal {P} _ {\bullet} ^ {(1)}, \dots , \mathcal {P} _ {\bullet} ^ {(m)}, \mathcal {F} ^ {\prime}) \stackrel {{\sim}} {{\to}} \mathfrak {C o r} _ {n} ^ {\mathrm{S}} (f _ {1}, \dots , f _ {m}; \mathcal {P} _ {\bullet} ^ {(1)}, \dots , \mathcal {P} _ {\bullet} ^ {(m)}) \otimes_ {\mathcal {O} _ {\mathrm{S}}} \mathcal {F} ^ {\prime}\tag{6.9.6.2}
$$

et plus particulièrement, pour $\mathcal{F}' = \mathcal{O}_{\mathrm{S}'}$,

$$
\mathfrak {G o r} _ {n} ^ {\mathrm{S} ^ {\prime}} \left(f _ {1} ^ {\prime}, \dots , f _ {m} ^ {\prime}; \mathcal {P} _ {\bullet} ^ {\prime (1)}, \dots , \mathcal {P} _ {\bullet} ^ {\prime (m)}\right) \xrightarrow {} \mathfrak {G o r} _ {n} ^ {\mathrm{S}} \left(f _ {1}, \dots , f _ {m}; \mathcal {P} _ {\bullet} ^ {(1)}, \dots , \mathcal {P} _ {\bullet} ^ {(m)}\right) \otimes_ {\mathcal {O} _ {\mathrm{S}}} \mathcal {O} _ {\mathrm{S} ^ {\prime}}.\tag{6.9.6.3}
$$

L'hypothèse de platitude sur les Modules composant les $\mathcal{P}_{\bullet}^{(i)}$ entraîne que les complexes $\mathcal{T}or_{q_i}^{\mathrm{S}}(\mathcal{P}_{\bullet}^{(i)},\mathcal{O}_{\mathrm{S}^{\prime}})$ sont nuls pour $q\neq 0$ (6.5.8). La suite $(f^{\prime})$ est donc dégénérée; l'hypothèse $2^{\circ}$ entraîne d'ailleurs qu'elle est birégulière (6.9.3), donc le edge-homomorphisme

$$
\begin{array}{r l} \mathfrak {C o r} _ {n} ^ {\mathrm{S}} (f _ {1}, \dots , f _ {m}, \mathrm{I} _ {\mathrm{S} ^ {\prime}}; \mathcal {P} _ {\bullet} ^ {(1)}, \dots , \mathcal {P} _ {\bullet} ^ {(m)}, \mathcal {Q} _ {\bullet} ^ {\prime}) & \to {} ^ {(f ^ {\prime})} \mathcal {E} _ {n 0} ^ {2} = \\ & = \mathfrak {C o r} _ {n} ^ {\mathrm{S} ^ {\prime}} (f _ {1} ^ {\prime}, \dots , f _ {m} ^ {\prime}, \mathrm{I} _ {\mathrm{S} ^ {\prime}}; \mathcal {P} _ {\bullet} ^ {(1)}, \dots , \mathcal {P} _ {\bullet} ^ {(m)}, \mathcal {Q} _ {\bullet} ^ {\prime}) \end{array}\tag{6.9.6.4}
$$

est bijectif (0, 11.1.6). L'hypothèse de platitude sur les Modules

$$
\mathcal {C o r} _ {n} ^ {\mathrm{S}} (f _ {1}, \dots , f _ {m}; \mathcal {P} _ {\bullet} ^ {(1)}, \dots , \mathcal {P} _ {\bullet} ^ {(m)})
$$

entraîne que $^{(e)} \mathcal{E}_{pq}^{2} = 0$ pour $p \neq 0$ (6.5.8). La suite $(e)$ est donc aussi dégénérée, et comme elle est birégulière, le edge-homomorphisme

$$
\begin{array}{r l} \mathfrak {C o r} _ {n} ^ {\mathrm{S}} (f _ {1}, \dots , f _ {m}, \mathrm{I} _ {\mathrm{S} ^ {\prime}}; \mathcal {P} _ {\bullet} ^ {(1)}, \dots , \mathcal {P} _ {\bullet} ^ {(m)}, \mathcal {Q} _ {\bullet} ^ {\prime}) & \to^ {(e)} \mathcal {E} _ {0 n} ^ {2} = \\ & = \bigoplus_ {n ^ {\prime} + n ^ {\prime \prime} = n} \mathfrak {C o r} _ {n ^ {\prime}} ^ {\mathrm{S}} (f _ {1}, \dots , f _ {m}; \mathcal {P} _ {\bullet} ^ {(1)}, \dots , \mathcal {P} _ {\bullet} ^ {(m)}) \otimes_ {\mathcal {O} _ {\mathrm{S}}} \mathcal {H} _ {n ^ {\prime \prime}} (\mathcal {Q} _ {\bullet} ^ {\prime}) \end{array}\tag{6.9.6.5}
$$

est bijectif (0, 11.1.6); d'où, en combinant les deux isomorphismes précédents, l'isomorphisme (6.9.6.1). L'isomorphisme (6.9.6.2) s'en déduit trivialement, puisque l'on a alors $\mathcal{H}_{q}(2') = o$ si $q \neq o$ et $\mathcal{H}_{0}(2') = \mathcal{F}'$. Enfin, le cas $\mathcal{F}' = \mathcal{O}_{\mathrm{S}}$, dans (6.9.6.2) donne l'isomorphisme (6.9.6.3), compte tenu de (6.7.12).

Corollaire (6.9.7). — Sous les conditions de (6.9.1), supposons S et S' affines, et supposons donné pour chaque i un entier  $d_{i}$  ( $1 \leqslant i \leqslant m$ ). Il existe alors un entier N ne dépendant que de S, des  $\mathbf{X}^{(i)}$  et des  $d_{i}$ , ayant la propriété suivante : pour tout entier  $n_{0}$ , on a des isomorphismes canoniques (6.9.6.3) pour  $n \leqslant n_{0}$  et pour tout système de complexes  $\mathcal{P}_{\bullet}^{(i)}$  vérifiant les conditions suivantes :  $1^{0} \mathcal{P}_{k}^{(i)} = 0$  pour  $k < d_{i}$ ;  $2^{0} \mathcal{P}_{k}^{(i)}$  est plat sur S pour  $k < n_{0} + N$ ;  $3^{0} \mathcal{Gor}_{q}^{\mathrm{S}}(f_{1}, \ldots, f_{m}; \mathcal{P}_{\bullet}^{(1)}, \ldots, \mathcal{P}_{\bullet}^{(m)})$  est plat sur S pour  $q < n_{0} + N$ .

Supposons $\mathcal{P}_k^{(i)}$ plat sur S pour $k < r$; alors $\mathcal{Tor}_{q_i}^{\mathrm{S}}(\mathcal{P}_k^{(i)},\mathcal{O}_{\mathrm{S}'}) = 0$ pour $k < r$ et $q_{i}\neq 0$; calculons

$$
\mathcal {C o r} _ {p} ^ {\mathrm{S} ^ {\prime}} (f _ {1} ^ {\prime}, \dots , f _ {m} ^ {\prime}; \mathcal {T o r} _ {q _ {1}} ^ {\mathrm{S}} (\mathcal {P} _ {\bullet} ^ {(1)}, \mathcal {O} _ {\mathrm{S} ^ {\prime}}), \dots , \mathcal {T o r} _ {q _ {m}} ^ {\mathrm{S}} (\mathcal {P} _ {\bullet} ^ {(m)}, \mathcal {O} _ {\mathrm{S} ^ {\prime}}))\tag{6.9.7.1}
$$

par la méthode de (6.6.2), à l'aide de l'image réciproque d'un recouvrement affine fixe $\mathfrak{U}^{(i)}$ de $\mathbf{X}^{(i)}$ ($1 \leqslant i \leqslant m$) (indépendant de S' et des $\mathcal{P}_{\bullet}^{(i)}$); les termes $\mathrm{L}_{jk}^{(i)}$ sont nuls pour $j < -\mathrm{N}_i$ (ne dépendant que de $\mathfrak{U}^{(i)}$); si l'un des $q_i$ n'est pas nul, le complexe simple dont l'homologie de degré $p$ est (6.9.7.1) a ses termes nuls pour tous les degrés $< r + \sum_{j \neq i} d_j - \sum_{i=1}^{m} \mathrm{N}_i$, donc (6.9.7.1) est nul pour $p < r - \mathrm{N}$, en désignant par N le plus grand des nombres $\sum_{i=1}^{m} \mathrm{N}_i - \sum_{j \neq i} d_j$. On en conclut que l'on a ${}^{(l')}\mathcal{E}_{pq}^2 = 0$ pour $q \neq 0$ et $p < r - \mathrm{N}$; comme d'autre part ${}^{(l')}\mathcal{E}_{pq}^2 = 0$ pour $q < 0$, on voit que le edge-homomorphisme (6.9.6.4) est bijectif pour $n < r - \mathrm{N}$ (M, XV, 5.6) (pour $\mathcal{Q}' = \mathcal{O}_{\mathrm{S}'}$). En second lieu, si $\mathcal{Gor}_q^{\mathrm{S}}(f_1, \ldots, f_m; \mathcal{P}_{\bullet}^{(1)}, \ldots, \mathcal{P}_{\bullet}^{(m)})$ est plat sur S pour $q < r$, on a ${}^{(e)}\mathcal{E}_{pq}^2 = 0$ pour $p \neq 0$ et $q < r$; par ailleurs ${}^{(e)}\mathcal{E}_{pq}^2 = 0$ pour $p < 0$, donc le edge-homomorphisme (6.9.6.5) est bijectif pour $n < r$, ce qui achève la démonstration.

Le cas le plus important de (6.9.3) dans les applications est celui où $m = 1$, $\mathcal{Q}'$ étant réduit à un seul terme $\mathcal{F}'$ de degré o; nous l'énoncerons à nouveau dans ce cas en vue de références ultérieures (1):

Proposition (6.9.8). — Soient S un préschéma, $g: \mathrm{S}' \to \mathrm{S}$ un morphisme, $f: \mathrm{X} \to \mathrm{Y}$ un S-morphisme séparé et quasi-compact de S-préschémas, $\mathcal{P}_{\bullet}$ un complexe de $\mathcal{O}_{\mathrm{X}}$-Modules quasi-cohérents limité inférieurement, $\mathcal{F}'$ un $\mathcal{O}_{\mathrm{S}'}$-Module quasi-cohérent. Il existe deux foncteurs spectraux biréguliers en $\mathcal{P}_{\bullet}$ et $\mathcal{F}'$, à valeurs dans la catégorie des $\mathcal{O}_{\mathrm{Y}_{(\mathrm{S}')}}$-Modules quasi-cohérents, ayant même aboutissement $\mathfrak{Cor}_{\bullet}^{\mathrm{S}}(f, \mathrm{I}_{\mathrm{S}'}; \mathcal{P}_{\bullet}, \mathcal{F}')$, et dont les termes $\mathrm{E}_2$ sont

(6.9.8.1)

$$
\begin{array}{r l} & {^ {\prime} \mathcal {E} _ {p q} ^ {2} = \mathcal {T o r} _ {p} ^ {\mathrm{S}} (\mathcal {H} ^ {- q} (f, \mathcal {P} _ {\bullet}), \mathcal {F} ^ {\prime})} \\ & {^ {\prime \prime} \mathcal {E} _ {p q} ^ {2} = \mathcal {H} ^ {- p} (f ^ {\prime}, \mathcal {T o r} _ {q} ^ {\mathrm{S}} (\mathcal {P} _ {\bullet}, \mathcal {F} ^ {\prime})),} \end{array}\tag{6.9.8.2}
$$

$où f' = f_{(S')} : X_{(S')} \to Y_{(S')}$.

Les suites en question peuvent aussi s'obtenir, non en partant de (6.9.3), mais des suites (a) et (b') de (6.7.3) pour  $\mathbf{X}^{(1)}=\mathbf{X},\;\mathbf{Y}^{(1)}=\mathbf{Y},\;\mathbf{X}^{(2)}=\mathbf{Y}^{(2)}=\mathbf{S}'$ ,  $f_{1}=f$ ,  $f_{2}=I_{S'}$ . Lorsque  $S=S'=Y$ , Y étant affine, on obtient deux suites spectrales de termes  $E_{2}$  égaux à

(6.9.8.3)

$$
^ \prime \mathcal {E} _ {p q} ^ {2} = \mathcal {T o r} _ {p} ^ {\mathrm{Y}} (\mathcal {H} ^ {- q} (f, \mathcal {P} _ {\bullet}), \mathcal {F})\tag{6.9.8.4}
$$

$$
^ {\prime \prime} \mathcal {E} _ {p q} ^ {2} = \mathcal {H} ^ {- p} (f, \mathcal {T o r} _ {q} ^ {\mathrm{Y}} (\mathcal {P} _ {\bullet}, \mathcal {F}))
$$

aboutissant (en vertu de (6.7.6)) à l'hypercohomologie $\mathcal{H}^{\bullet}(f, \mathcal{P}_{\bullet} \otimes_{\mathrm{Y}} \mathcal{F})$ du foncteur $f_{*}$ par rapport au complexe $\mathcal{P}_{\bullet} \otimes_{\mathrm{Y}} \mathcal{F}$ de $\mathcal{O}_{\mathrm{X}}$-Modules, pour tout $\mathcal{O}_{\mathrm{Y}}$-Module quasi-cohérent et Y-plat $\mathcal{F}$ (ou pour tout $\mathcal{O}_{\mathrm{Y}}$-Module quasi-cohérent $\mathcal{F}$ lorsque $\mathcal{P}_{\bullet}$ est formé de $\mathcal{O}_{\mathrm{X}}$-Modules Y-plats), qui sont distinctes de celles de (6.2.1).

Corollaire (6.9.9). — Sous les conditions de (6.9.8), supposons que le complexe $\mathcal{P}_{\bullet}$ soit limité inférieurement, formé de Modules plats sur S, et que les $\mathcal{O}_{\mathrm{Y}}$-Modules $\mathcal{H}^{n}(f,\mathcal{P}_{\bullet})$ soient plats sur S.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(6.9.8),</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Le cas traité dans (6.9.8), et en particulier les suites spectrales (6.9.8.3) et (6.9.8.4), nous avaient été signalés en 1957 par J.-P. Serre.</span></small>

On a alors des isomorphismes canoniques fonctoriels

$$
\mathfrak {C o r} _ {n} ^ {\mathrm{S} ^ {\prime}} \left(f ^ {\prime}, \mathrm{I} _ {\mathrm{S} ^ {\prime}}; \mathcal {P} _ {\bullet} ^ {\prime}, \mathcal {F} ^ {\prime}\right) \simeq \mathscr {H} ^ {- n} (f, \mathcal {P} _ {\bullet}) \otimes_ {\mathcal {O} _ {\mathrm{s}}} \mathcal {F} ^ {\prime}\tag{6.9.9.1}
$$

$\text{ou } \mathcal{P}^{\prime} = \mathcal{P}_{\bullet} \otimes_{\mathcal{O}_{\mathrm{S}}}\mathcal{O}_{\mathrm{S}^{\prime}}; \text{ en particulier, pour } \mathcal{F}^{\prime} = \mathcal{O}_{\mathrm{S}^{\prime}}, \text{ on a des isomorphismes canoniques fonctoriels}$

$$
\mathcal {H} ^ {n} (f ^ {\prime}, \mathcal {P} _ {\bullet} ^ {\prime}) \xrightarrow {\sim} \mathcal {H} ^ {n} (f, \mathcal {P} _ {\bullet}) \otimes_ {\mathcal {O} _ {\mathrm{s}}} \mathcal {O} _ {\mathrm{S} ^ {\prime}}.\tag{6.9.9.2}
$$

C'est le cas particulier $m=\mathrm{i}$ de (6.9.6). Plus particulièrement :

Corollaire (6.9.10). — Soient S un préschéma, $f: \mathbf{X} \to \mathbf{Y}$ un S-morphisme séparé et quasi-compact de S-préschémas, $\mathcal{P}_{\bullet}$ un complexe limité inférieurement, formé de $\mathcal{O}_{\mathbf{X}}$-Modules quasicohérents, plats sur S. On suppose en outre que les $\mathcal{O}_{\mathbf{Y}}$-Modules $\mathcal{H}^{n}(f, \mathcal{P}_{\bullet})$ soient plats sur S. Pour tout $s \in \mathbb{S}$, notons $\mathbf{X}_{s}$ et $\mathbf{Y}_{s}$ les fibres $\mathbf{X} \otimes_{\mathbb{S}} \boldsymbol{k}(s)$, $\mathbf{Y} \otimes_{\mathbb{S}} \boldsymbol{k}(s)$, $f_{s}: \mathbf{X}_{s} \to \mathbf{Y}_{s}$ le morphisme $f \times_{\mathbb{S}} \mathbf{I}$, $\mathcal{P}_{\bullet}^{s}$ le complexe $\mathcal{P}_{\bullet} \otimes_{\mathcal{O}_{\mathbb{S}}} \boldsymbol{k}(s)$ de $\mathcal{O}_{\mathbf{X}_{s}}$-Modules. On a alors des isomorphismes canoniques fonctoriels

$$
\mathcal {H} ^ {n} (f _ {s}, \mathcal {P} _ {\bullet} ^ {s}) \simeq \mathcal {H} ^ {n} (f, \mathcal {P} _ {\bullet}) \otimes_ {\mathcal {O} _ {s}} \boldsymbol {k} (s).\tag{6.9.10.1}
$$

On a donc, moyennant des hypothèses de platitude convenables, un cas où la formation des foncteurs dérivés  $\mathrm{R}^{n}f_{*}(\mathcal{F})$  « commute au passage aux fibres », que nous retrouverons par une autre méthode au § 7.

## 6.10. Structure locale de certains foncteurs cohomologiques.

Proposition (6.10.1). — Soient S = Spec(A) un schéma affine,  $\mathrm{Y}^{(i)}(\mathrm{i}\leqslant i\leqslant n)$  une famille finie de S-schémas affines, plats sur S; pour chaque i, soit  $f_{i}:X^{(i)}\to Y^{(i)}$  un S-morphisme séparé et quasi-compact, et soit  $\mathcal{P}_{\bullet}^{(i)}$  un complexe de  $\mathcal{O}_{\mathrm{X}}^{(i)}$ -Modules quasi-cohérents limité inférieurement. Soit Y le produit des S-schémas  $Y^{(i)}$ . Il existe un complexe R. de  $O_{Y}$ -Modules quasi-cohérents et plats sur S, ayant la propriété suivante : pour tout S-schéma affine  $S'$  et tout complexe de  $O_{S'}$ -Modules quasi-cohérents  $Q'$ . limité inférieurement, il y a un isomorphisme

$$
\mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} \left(f _ {1}, \dots , f _ {n}, \mathrm{I} _ {\mathrm{S} ^ {\prime}}; \mathcal {P} _ {\bullet} ^ {(1)}, \dots , \mathcal {P} _ {\bullet} ^ {(n)}, 2 _ {\bullet} ^ {\prime}\right) \stackrel {{\sim}} {{\rightarrow}} \mathscr {H} _ {\bullet} \left(\mathscr {R} _ {\bullet} \otimes_ {\mathscr {O} _ {\mathrm{S}}} 2 _ {\bullet} ^ {\prime}\right)\tag{6.10.1.1}
$$

qui est un isomorphisme de $\partial$-foncteurs en $2'$. En outre, pour tout S-morphisme $u: S'' \to S'$ de S-schémas affines, le diagramme

$$
\begin{array}{c c c} \mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} (f _ {1},   \ldots , f _ {n},   \mathrm{I} _ {\mathrm{S} ^ {\prime}};   \mathcal {P} _ {\bullet} ^ {(1)},   \ldots , \mathcal {P} _ {\bullet} ^ {(n)}, \mathcal {Q} _ {\bullet} ^ {\prime}) & \simeq & \mathcal {H} _ {\bullet} (\mathcal {R} _ {\bullet} \otimes_ {\mathcal {O} _ {\mathrm{S}}} \mathcal {Q} _ {\bullet} ^ {\prime}) \\ \Bigg \downarrow & & \Bigg \downarrow \\ \mathfrak {C o r} _ {\bullet} ^ {\mathrm{S}} (f _ {1},   \ldots , f _ {n},   \mathrm{I} _ {\mathrm{S} ^ {\prime \prime}};   \mathcal {P} _ {\bullet} ^ {(1)},   \ldots , \mathcal {P} _ {\bullet} ^ {(n)}, u ^ {*} (\mathcal {Q} _ {\bullet} ^ {\prime})) & \simeq & \mathcal {H} _ {\bullet} (\mathcal {R} _ {\bullet} \otimes_ {\mathcal {O} _ {\mathrm{S}}} u ^ {*} (\mathcal {Q} _ {\bullet} ^ {\prime})) \end{array}\tag{6.10.1.2}
$$

(où les flèches verticales sont les  $(\mathbf{I}_{\mathrm{Y}} \times_{\mathrm{S}} u)$ -morphismes canoniques définis dans (6.7.10)) est commutatif.

Calculons les hypertor par la méthode de (6.6.2), en tenant compte de la remarque (6.6.6); avec les notations de (6.6.2), chaque  $L_{\cdot\cdot}^{(i)}$  est un bicomplexe de  $A_{i}$ -modules, en désignant par  $A_{i}$  l'anneau de  $Y^{(i)}$ ; il admet donc une résolution de Cartan-Eilenberg projective  $M_{\cdot\cdot}^{(i)}$  (au sens de (0, 11.7.1)) formée de  $A_{i}$ -modules, et en vertu de (6.6.6), le premier membre de (6.10.1.1) est canoniquement isomorphe à  $H_{\cdot}(M_{\cdot\cdot}\otimes_{A}Q')$ , où  $M_{\cdot\cdot}=M_{\cdot\cdot}^{(1)}\otimes_{A}M_{\cdot\cdot}^{(2)}\otimes\ldots\otimes_{A}M_{\cdot\cdot}^{(n)}$  et  $2^{\prime}=\widetilde{Q}^{\prime}$ . Comme, par hypothèse, les anneaux  $A_{i}$  sont des A-modules plats, les  $M_{\cdot\cdot}^{(i)}$  sont des tricomplexes de A-modules plats ( $0_{I}, 6.2.1$ ), et il en est de même de  $M_{\cdot\cdot}$ ; en outre, si B est l'anneau de Y, produit tensoriel des  $A_{i}$ ,  $M_{\cdot\cdot}$  est un tricomplexe de B-modules; le complexe  $\mathcal{R}_{\cdot}=(M_{\cdot\cdot})^{\sim}$  de  $O_{Y}$ -Modules (où  $M_{\cdot\cdot}$  est considéré comme complexe simple) répond donc à la question, comme il résulte aisément de (6.7.10).

Corollaire (6.10.2). — Dans l'énoncé de (6.10.1), on peut supposer R. limité inférieurement. Lorsque les  $\mathcal{P}^{(i)}$  sont limités supérieurement et les  $Y^{(i)}$  de dimension cohomologique finie, on peut supposer R. limité supérieurement.

La première assertion résulte de ce que les trois degrés de chacun des  $M_{\cdots}^{(i)}$  sont limités inférieurement; d'autre part, si les anneaux  $A_{i}$  sont de dimension cohomologique finie, le troisième degré de chacun des  $M_{\cdots}^{(i)}$  ne prend qu'un nombre fini de valeurs, et il en est de même par construction de son premier degré (6.6.2); comme son second degré est limité supérieurement s'il en est ainsi du degré de  $\mathcal{P}_{\bullet}^{(i)}$  (6.6.2), la seconde assertion en résulte aussitôt.

Remarques (6.10.3). — (i) Avec les notations de (6.10.1), $\mathcal{H}_{\bullet}(\mathcal{R}_{\bullet}\otimes_{\mathrm{s}}2^{\prime})$ est isomorphe à $\mathcal{E}or_{\bullet}(\mathcal{R}_{\bullet},2^{\prime})$ puisque $\mathcal{R}_{\bullet}$ est formé de $\mathcal{O}_{\mathrm{Y}}$-Modules S-plats (6.5.9); il est donc (6.5.4) l'aboutissement d'une suite spectrale régulière de terme $\mathrm{E}_2$ donné par

$$
\mathcal {E} _ {p q} ^ {2} = \bigoplus_ {q ^ {\prime} + q ^ {\prime \prime} = q} \mathcal {T o r} _ {p} ^ {\mathrm{S}} (\mathcal {H} _ {q ^ {\prime}} (\mathcal {R} _ {\bullet}), \mathcal {H} _ {q ^ {\prime \prime}} (2 _ {\bullet} ^ {\prime}))\tag{6.10.3.1}
$$

qui n'est autre que la suite spectrale (e) du changement de base (6.9.3).

(ii) Soit $\mathcal{R}'$. un second complexe de $\mathcal{O}_{\mathrm{Y}}$-Modules quasi-cohérents, plat sur S, et soit $g: \mathcal{R}' \to \mathcal{R}$. un homomorphisme de complexes tel que $\mathcal{H}_{\bullet}(g): \mathcal{H}_{\bullet}(\mathcal{R}') \to \mathcal{H}_{\bullet}(\mathcal{R})$ soit un isomorphisme. Alors, en vertu de (6.3.3) et (6.5.9), on déduit de $g$ un isomorphisme de $\partial$-foncteurs en $\mathcal{Q}': \mathcal{H}_{\bullet}(\mathcal{R}' \otimes_{\mathrm{S}} \mathcal{Q}') \simeq \mathcal{H}_{\bullet}(\mathcal{R}' \otimes_{\mathrm{S}} \mathcal{Q}')$ tel que le diagramme

$$
\begin{array}{c c c} \mathcal {H} _ {\bullet} (\mathcal {R} _ {\bullet} ^ {\prime} \otimes_ {\mathrm{s}} \mathcal {Q} _ {\bullet} ^ {\prime}) & \stackrel {{\sim}} {{\to}} & \mathcal {H} _ {\bullet} (\mathcal {R} _ {\bullet} \otimes_ {\mathrm{s}} \mathcal {Q} _ {\bullet} ^ {\prime}) \\ \Bigg \downarrow & & \Bigg \downarrow \\ \mathcal {H} _ {\bullet} (\mathcal {R} _ {\bullet} ^ {\prime} \otimes_ {\mathrm{s}} u ^ {*} (\mathcal {Q} _ {\bullet} ^ {\prime})) & \stackrel {{\sim}} {{\to}} & \mathcal {H} _ {\bullet} (\mathcal {R} _ {\bullet} \otimes_ {\mathrm{s}} u ^ {*} (\mathcal {Q} _ {\bullet} ^ {\prime})) \end{array}
$$

172

soit commutatif. Cela prouve donc que le complexe R, n'est pas entièrement déterminé par les propriétés de (6.10.1).

(iii) Dans la démonstration de (6.10.1), on peut supposer les  $M_{\cdots}^{(i)}$  formés de  $A_{i}$ -modules libres (comme il résulte aisément de la démonstration de (0, 11.5.2.1) « dualisée »); les  $M_{\cdots}^{(i)} \otimes_{A_{i}} B$  sont alors formés de B-modules libres, et comme  $M_{\cdots}$  est égal à leur produit tensoriel sur B, on voit qu'on peut supposer en outre dans (6.10.1) que R. est associé à un complexe de B-modules libres. En outre, en vertu de (M, XVII, 1.2), le tricomplexe  $M_{\cdots}$  dépend fonctoriellement de chacun des bicomplexes  $L_{\cdots}^{(i)}$  (donc de chacun des  $P_{\cdot}^{(i)}$ , lorsqu'on fixe un recouvrement fini de chacun des  $X^{(i)}$ ), les « morphismes » de tricomplexes devant être ici entendus comme les classes d'homomorphismes pour la relation d'homotopie; d'ailleurs, le remplacement d'un recouvrement de  $X^{(i)}$  par un recouvrement plus fin donnant lieu pour les  $L_{\cdots}^{(i)}$  à des homomorphismes définis précisément à homotopie près (6.6.8), on voit finalement qu'avec la convention précédente pour les morphismes, le tricomplexe  $M_{\cdots}$  est un foncteur en chacun des  $P_{\cdot}^{(i)}$ . Nous préciserons cette dépendance fonctorielle, et notamment le comportement de R. relativement à des suites exactes  $o \to P_{\cdot}^{(i)} \to P_{\cdot}^{(i)} \to P_{\cdot}^{\prime\prime(i)} \to o$  de complexes, dans le chapitre consacré à une algèbre générale de foncteurs cohomologiques, mentionné dans (6.1.3).

Scholie (6.10.4). — Le fait que $\mathcal{R}_{\bullet}$ est formé de $\mathcal{O}_{\mathrm{Y}}$-Modules S-plats entraîne aisément que $\mathcal{H}_{\bullet}(\mathcal{R}_{\bullet}\otimes_{\mathrm{S}}\mathcal{Q}_{\bullet}^{\prime})$ est un foncteur homologique en $\mathcal{Z}_{\bullet}^{\prime}$ (voir le raisonnement de (7.7.1)). C'est cette propriété qui, ainsi qu'on l'a mentionné en (6.1.1), est la motivation de l'introduction de l'hypertor. Posons en effet

$$
\begin{array}{c} \mathbf {X} = \mathbf {X} _ {1} \times_ {\mathrm{s}} \mathbf {X} _ {2} \times \ldots \times_ {\mathrm{s}} \mathbf {X} _ {n}, \qquad f = f _ {1} \times_ {\mathrm{s}} f _ {2} \times_ {\mathrm{s}} \ldots \times_ {\mathrm{s}} f _ {n}, \qquad \mathcal {P} _ {\bullet} = \mathcal {P} _ {\bullet} ^ {(1)} \otimes_ {\mathrm{s}} \mathcal {P} _ {\bullet} ^ {(2)} \otimes \ldots \otimes_ {\mathrm{s}} \mathcal {P} _ {\bullet} ^ {(n)}, \\ \mathbf {X} ^ {\prime} = \mathbf {X} \times_ {\mathrm{s}} \mathbf {S} ^ {\prime}, \quad \mathbf {Y} ^ {\prime} = \mathbf {Y} \times_ {\mathrm{s}} \mathbf {S} ^ {\prime}, \quad f ^ {\prime} = f \times_ {\mathrm{s}} \mathbf {I} _ {\mathrm{s} ^ {\prime}}; \end{array}
$$

les problèmes de changement de base amènent à étudier l'hypercohomologie $\mathcal{H}_{j'}^{\bullet}(\mathcal{P}_{\bullet}\otimes_{\mathrm{s}}\mathcal{N}')$ en tant que foncteur par rapport au $\mathcal{O}_{\mathrm{s}'}$-Module quasi-cohérent $\mathcal{N}'$, ou encore l'hypercohomologie $\mathcal{H}_{j'}^{\bullet}(\mathcal{P}_{\bullet}\otimes_{\mathrm{s}}\mathcal{N})$ comme foncteur en le $\mathcal{O}_{\mathrm{s}}$-Module quasi-cohérent $\mathcal{N}$. Lorsque les $\mathcal{P}_{\bullet}^{(i)}$ (donc aussi $\mathcal{P}_{\bullet}$) sont S-plats, il résulte de ce qui précède et de (6.7.6) que ce foncteur est bien un foncteur cohomologique en $\mathcal{N}$; mais il n'en est plus de même lorsqu'on ne fait plus l'hypothèse de platitude sur les $\mathcal{P}_{\bullet}^{(i)}$, et l'on ne peut plus alors aborder l'étude de $\mathcal{H}_{j'}^{\bullet}(\mathcal{P}_{\bullet}\otimes_{\mathrm{s}}\mathcal{N})$ par les méthodes usuelles de l'Algèbre homologique.

Nous aurons toutefois surtout à utiliser le cas où $n=1$, Y=S et où $\mathcal{P}$. est formé de $\mathcal{O}_{X}$-Modules Y-plats. On a dans ce cas le

Théorème (6.10.5). — Soient Y = Spec(A) un schéma affine noethérien,  $f : X \to Y$  un morphisme propre, P. un complexe de  $O_{X}$ -Modules cohérents, plats sur Y, limité inférieurement. Il existe alors un complexe L. de  $O_{Y}$ -Modules, limité inférieurement, dont les termes  $L_{i}$  sont des  $O_{Y}$ -Modules de la forme  $O_{Y}^{mi}$ , et un isomorphisme

$$
\mathcal {H} ^ {\bullet} (f, \mathscr {P} _ {\bullet} \otimes_ {\mathrm{Y}} \mathscr {2} _ {\bullet}) \stackrel {{\sim}} {{\to}} \mathcal {H} _ {\bullet} (\mathscr {L} _ {\bullet} \otimes_ {\mathrm{Y}} \mathscr {2} _ {\bullet})\tag{6.10.5.1}
$$

de $\partial$-foncteurs en le complexe $\mathcal{Q}$. de $\mathcal{O}_{\mathrm{Y}}$-Modules quasi-cohérents, limité inférieurement. En outre, pour tout morphisme $u: \mathrm{Y}' \to \mathrm{Y}$, on $a$, en posant

$$
\mathbf {X} ^ {\prime} = \mathbf {X} _ {(\mathrm{Y} ^ {\prime})}, \quad f ^ {\prime} = f _ {(\mathrm{Y} ^ {\prime})}, \quad \mathcal {P} _ {\bullet} ^ {\prime} = \mathcal {P} _ {\bullet} \otimes_ {\mathrm{Y}} \mathcal {O} _ {\mathrm{Y} ^ {\prime}}, \quad \mathcal {L} _ {\bullet} ^ {\prime} = u ^ {*} (\mathcal {L} _ {\bullet})\tag{173}
$$

( qui est un complexe de $\mathcal{O}_{\mathrm{Y}^{\prime}}$-modules localement libres de type fini), un isomorphisme

$$
\mathcal {H} ^ {\bullet} (f ^ {\prime}, \mathcal {P} _ {\bullet} ^ {\prime} \otimes_ {\mathrm{Y} ^ {\prime}} \mathcal {Q} _ {\bullet} ^ {\prime}) \xrightarrow {\sim} \mathcal {H} _ {\bullet} (\mathcal {L} _ {\bullet} ^ {\prime} \otimes_ {\mathrm{Y} ^ {\prime}} \mathcal {Q} _ {\bullet} ^ {\prime})\tag{6.10.5.2}
$$

de $\partial$-foncteurs en le complexe $\mathcal{Q}'_{\bullet}$ de $\mathcal{O}_{\mathrm{Y}'}$-Modules quasi-cohérents, limité inférieurement, de sorte que le diagramme

$$
\begin{array}{c c c} \mathcal {H} ^ {\bullet} (f, \mathcal {P} _ {\bullet} \otimes_ {\mathrm{Y}} \mathcal {Q} _ {\bullet}) & \stackrel {{\sim}} {{\to}} & \mathcal {H} _ {\bullet} (\mathcal {L} _ {\bullet} \otimes_ {\mathrm{Y}} \mathcal {Q} _ {\bullet}) \\ \Bigg \downarrow & & \Bigg \downarrow \\ \mathcal {H} ^ {\bullet} (f ^ {\prime}, \mathcal {P} _ {\bullet} ^ {\prime} \otimes_ {\mathrm{Y} ^ {\prime}} u ^ {*} (\mathcal {Q} _ {\bullet})) & \stackrel {{\sim}} {{\to}} & \mathcal {H} _ {\bullet} (\mathcal {L} _ {\bullet} ^ {\prime} \otimes_ {\mathrm{Y} ^ {\prime}} u ^ {*} (\mathcal {Q} _ {\bullet})) \end{array}\tag{6.10.5.3}
$$

soit commutatif.

L'application de (6.10.1) donne d'abord un complexe limité inférieurement (6.10.2) $\mathcal{R}_{\bullet}$ de $\mathcal{O}_{\mathrm{Y}}$-Modules quasi-cohérents et Y-libres (6.10.3, (ii)) et un isomorphisme

$$
\mathcal {H} ^ {\bullet} (f, \mathcal {P} _ {\bullet} \otimes_ {\mathrm{Y}} 2 _ {\bullet}) \xrightarrow {\sim} \mathcal {H} _ {\bullet} (\mathcal {R} _ {\bullet} \otimes_ {\mathrm{Y}} 2 _ {\bullet})\tag{6.10.5.4}
$$

de $\partial$-foncteurs en $\mathcal{Q}_{\bullet}$, mais a priori les termes de $\mathcal{R}_{\bullet}$ ne sont pas nécessairement des $\mathcal{O}_{\mathrm{Y}}$-Modules de type fini. Mais si l'on applique (6.10.5.4) au cas où $\mathcal{Q}_{\bullet}$ est un complexe réduit à un seul terme $\mathcal{O}_{\mathrm{Y}}$, on voit que $\mathcal{H}_{\bullet}(\mathcal{R}_{\bullet})$ est isomorphe à $\mathcal{H}^{\bullet}(f,\mathcal{P}_{\bullet})$, et est par suite formé de $\mathcal{O}_{\mathrm{Y}}$-Modules cohérents (6.2.5). On sait alors (0, 11.9.2) qu'il existe un complexe $\mathcal{L}_{\bullet}$ limité inférieurement, formé de $\mathcal{O}_{\mathrm{Y}}$-Modules associés à des A-modules libres de type fini, et un homomorphisme $\mathcal{L}_{\bullet}\to\mathcal{R}_{\bullet}$, tels que l'homomorphisme correspondant pour l'homologie, $\mathcal{H}_{\bullet}(\mathcal{L}_{\bullet})\to\mathcal{H}_{\bullet}(\mathcal{R}_{\bullet})$ soit bijectif; d'où l'isomorphisme (6.10.5.1), en vertu de (6.10.3, (ii)). Les autres assertions de (6.10.5) résultent de (6.10.1) et (6.10.3, (ii)) lorsque Y' est affine; dans le cas général, il suffit de vérifier que lorsqu'on considère un recouvrement ($V_{\alpha}$) de Y' par des ouverts affines, et l'isomorphisme correspondant (6.10.5.2) relatif à chacun des $V_{\alpha}$, les restrictions à un ouvert affine $W\subset V_{\alpha}\cap V_{\beta}$ des isomorphismes correspondant à $V_{\alpha}$ et à $V_{\beta}$ coïncident avec l'isomorphisme correspondant à W, ce qui résulte de la commutativité du diagramme (6.10.1.2) appliqué aux injections canoniques $W\to V_{\alpha}$ et $W\to V_{\beta}$.

Remarque (6.10.6). — Dans les chapitres suivants, nous appliquerons surtout (6.10.5) au cas où $\mathcal{P}_{\bullet}$ est réduit à un seul $\mathcal{O}_{\mathrm{X}}$-Module cohérent $\mathcal{F}$, plat sur Y. Comme on a alors $\mathcal{H}_{n}(\mathcal{L}_{\bullet}) = \mathcal{H}^{-n}(f, \mathcal{F}) = \mathrm{R}^{-n} f_{*}(\mathcal{F})$ (6.2.1), on voit que les $\mathcal{H}_{n}(\mathcal{L}_{\bullet})$ sont nuls pour $n > 0$; nous verrons plus loin (7.7.12, (i)) qu'on peut alors supposer que $\mathcal{L}_{\bullet}$ n'a que des termes de degrés $\leqslant 0$ (donc en nombre fini), à condition de remplacer l'hypothèse que les $\mathcal{L}_{i}$ sont associés à des A-modules libres de type fini par celle que les $\mathcal{L}_{i}$ sont localement libres de type fini.

Le complexe $\mathcal{L}$, correspondant à un tel $\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{F}$ ne paraît posséder aucune

propriété particulière, en dehors de la restriction précédente sur les degrés. On peut alors se demander si inversement, étant donné un complexe $\mathcal{L}$. formé de $\mathcal{O}_{\mathrm{Y}}$-Modules associés à des A-modules projectifs de type fini, limité inférieurement et dont les termes de degré $>0$ sont nuls, il existe un Y-schéma X, projectif et plat sur Y et un $\mathcal{O}_{\mathrm{X}}$-Module localement libre $\mathcal{F}$, tels qu'il y ait un isomorphisme $\mathcal{H}^{\bullet}(f, \mathcal{F} \otimes_{\mathrm{Y}} 2.) \simeq \mathcal{H}_{\bullet}(\mathcal{L}_{\bullet} \otimes_{\mathrm{Y}} 2.)$ fonctoriel en $\mathcal{Q}$. L'intérêt d'un tel résultat serait de réduire complètement la théorie cohomologique des Modules cohérents et Y-plats sur des Y-schémas propres, à la théorie « à homotopie près » des complexes de A-modules projectifs de type fini sur un anneau noethérien A.

## § 7. ÉTUDE DU CHANGEMENT DE BASE DANS LES FONCTEURS HOMOLOGIQUES COVARIANTS DE MODULES

## 7.1. Foncteurs de A-modules.

(7.1.1) Étant donné un anneau A (non nécessairement commutatif), nous noterons $\mathbf{Ab}_{\mathrm{A}}$ la catégorie des A-modules à gauche, et nous noterons simplement $\mathbf{Ab}$ la catégorie des Z-modules, identiques aux groupes commutatifs. Soit $\mathrm{T}: \mathbf{Ab}_{\mathrm{A}} \to \mathbf{Ab}$ un foncteur covariant additif, et soit M un (A, A)-bimodule; T(M) est alors muni de façon naturelle d'une structure de A-module à droite. En effet, pour tout $a \in \mathrm{A}$, notons $h_{a,\mathrm{M}}$ (ou simplement $h_a$) l'endomorphisme $x \to xa$ du A-module à gauche M. Par hypothèse, T($h_a$) est un endomorphisme du Z-module T(M); en outre, comme T est un foncteur covariant additif, on a, pour $a \in \mathrm{A}$, $b \in \mathrm{A}$,

$$
\mathrm{T} \left(h _ {a b}\right) = \mathrm{T} \left(h _ {b} \circ h _ {a}\right) = \mathrm{T} \left(h _ {b}\right) \circ \mathrm{T} \left(h _ {a}\right) \quad \text {et} \quad \mathrm{T} \left(h _ {a + b}\right) = \mathrm{T} \left(h _ {a} + h _ {b}\right) = \mathrm{T} \left(h _ {a}\right) + \mathrm{T} \left(h _ {b}\right);
$$

cela prouve que l'application  $(a,y)\to\mathrm{T}(h_{a})(y)$  est une loi externe de A-module à droite sur T(M). En particulier,  $\mathrm{T}(\mathrm{A}_{s})$  est un A-module à droite.

(7.1.2) Lorsque A est un anneau commutatif, il résulte de (7.1.1) que pour tout A-module M, T(M) est naturellement muni d'une structure de A-module; en outre, si $u: \mathbf{M} \to \mathbf{N}$ est un homomorphisme de A-modules, on a, pour tout $a \in \mathbf{A}$, $u \circ h_{a,\mathbf{M}} = h_{a,\mathbf{N}} \circ u$, d'où $\mathrm{T}(u) \circ \mathrm{T}(h_{a,\mathbf{M}}) = \mathrm{T}(h_{a,\mathbf{N}}) \circ \mathrm{T}(u)$, ce qui prouve que $\mathrm{T}(u): \mathrm{T}(\mathrm{M}) \to \mathrm{T}(\mathrm{N})$ est un homomorphisme de A-modules; on voit donc que T peut être considéré comme un foncteur covariant additif de la catégorie $Ab_A$ dans elle-même. De façon précise, on a ainsi défini une équivalence canonique entre la catégorie des foncteurs covariants additifs $Ab_A \to Ab$ et la catégorie des foncteurs covariants A-linéaires $\mathrm{T}: Ab_A \to Ab_A$, c'est-à-dire tels que $\mathrm{T}(h_{a,\mathbf{M}}) = h_{a,\mathrm{T}(\mathbf{M})}$ pour tout $a \in \mathbf{A}$. Comme le foncteur d'inclusion I: $Ab_A \to Ab$, faisant correspondre à tout A-module le Z-module sous-jacent, est exact et fidèle, les propriétés d'exactitude des deux foncteurs associés par l'équivalence précédente sont les mêmes.

(7.1.3) L'anneau A étant toujours supposé commutatif, soit B une A-algèbre (non nécessairement commutative), et soit $\rho: \mathrm{A} \to \mathrm{B}$ l'homomorphisme d'anneaux correspondant à cette structure d'algèbre; cet homomorphisme définit un foncteur covariant

additif $\rho_{*}: \mathbf{M} \rightsquigarrow \mathbf{M}_{[\rho]}$ de la catégorie $Ab_{\mathrm{B}}$ des B-modules à gauche dans la catégorie $Ab_{\mathrm{A}}$ des A-modules. Par composition, on en déduit un foncteur $\mathrm{T}_{(\mathrm{B})}: Ab_{\mathrm{B}} \xrightarrow{\rho_{*}} Ab_{\mathrm{A}} \xrightarrow{\mathrm{T}} Ab$, évidemment covariant et additif, que nous noterons aussi $\mathrm{T}^{(\mathrm{B})}$ (pour des raisons typographiques) ou $\mathrm{T} \otimes_{\mathrm{A}} \mathrm{B}$, et que nous dirons obtenu à partir de T par extension des scalaires de A à B. Bien entendu, si B est commutative, on peut considérer $\mathrm{T}_{(\mathrm{B})}$ comme un foncteur de $Ab_{\mathrm{B}}$ dans elle-même (7.1.2). Lorsque B est commutative, et C une B-algèbre, on voit aussitôt que $\mathrm{T}_{(\mathrm{C})} = (\mathrm{T}_{(\mathrm{B})})_{(\mathrm{C})}$; il est immédiat que l'extension des scalaires est fonctorielle et additive en T; en outre, lorsque T commute aux limites inductives ou aux sommes directes (resp. est exact à gauche, exact à droite, exact), il en est de même de $\mathrm{T}_{(\mathrm{B})}$: en effet, $\rho_{*}$ est exact et commute aux limites inductives et aux sommes directes.

(7.1.4) Supposons toujours A commutatif, et soit T un foncteur covariant additif A-linéaire  $Ab_{A} \rightarrow Ab_{A}$ , commutant aux limites inductives. Alors, pour toute partie multiplicative S de A et tout A-module M, on a un isomorphisme canonique fonctoriel de A-modules

$$
\mathbf {T} (\mathbf {S} ^ {- 1} \mathbf {M}) \simeq \mathbf {S} ^ {- 1} \mathbf {T} (\mathbf {M}).\tag{7.1.4.1}
$$

Supposons en effet d'abord que S soit l'ensemble des puissances $f^n$ ($n \geqslant 0$) d'un élément $f \in \mathbf{A}$. On sait alors que $\mathbf{M}_f = \varinjlim \mathbf{M}_n$, où $(\mathbf{M}_n, \varphi_{nm})$ est le système inductif des A-modules $\mathbf{M}_n = \mathbf{M}$, avec $\varphi_{nm}: z \to f^{n - m}z$ ($\mathbf{0}_{\mathrm{I}}$, i.6.i); d'où dans ce cas l'isomorphisme (7.i.4.i) en vertu de l'hypothèse sur T; si ensuite S est quelconque, $S^{-1}M$ est limite inductive des $\mathbf{M}_f$, pour $f \in S$ ($\mathbf{0}_{\mathrm{I}}$, i.4.5) et l'on conclut de la même façon. En outre, la fonctorialité de l'isomorphisme (7.i.4.i) montre que c'est un isomorphisme de $S^{-1}A-modules$, et qu'on peut donc écrire, à un isomorphisme canonique près

$$
\mathrm{T} _ {(\mathrm{S} ^ {- 1} \mathrm{A})} (\mathrm{S} ^ {- 1} \mathrm{M}) = \mathrm{S} ^ {- 1} \mathrm{T} (\mathrm{M}) = \mathrm{T} (\mathrm{S} ^ {- 1} \mathrm{M}).\tag{7.1.4.2}
$$

Lorsque $S = A - p$ est le complémentaire d'un idéal premier $p$ de $A$, on écrit $T_p$ au lieu de $T_{(A_p)}$.

Proposition (7.1.5). — Sous les hypothèses de (7.1.4), si  $T_{m}$  est exact à gauche (resp. exact à droite, exact) pour tout idéal maximal m de A, T est exact à gauche (resp. exact à droite, exact).

On sait en effet que lorsque deux sous-modules N, P d'un A-module M sont tels que  $N_{m}=P_{m}$  pour tout idéal maximal m de A, on a N=P (Bourbaki, Alg. comm., chap. II, § 3, n° 3, th. 1).

## 7.2. Caractérisations du foncteur produit tensoriel.

(7.2.1) Soient A un anneau (non nécessairement commutatif), M (resp. N) un A-module à gauche (resp. à droite), P un Z-module. Rappelons que la donnée d'un Z-homomorphisme  $v: N \otimes_{A} M \to P$  équivaut à la donnée d'une application Z-bilinéaire  $u: N \times M \to P$  telle que  $u(ta, x) = u(t, ax)$  pour  $a \in A$ ,  $t \in N$ ,  $x \in M$ , les deux applications étant reliées par  $v(t \otimes x) = u(t, x)$ . D'autre part, la donnée de u équivaut à celle d'un

Z-homomorphisme  $x \to f_{x}$  de M dans  $\operatorname{Hom}_{\mathbf{Z}}(\mathbf{N}, \mathbf{P})$  tel que  $f_{ax}(t) = f_{x}(ta)$  pour  $a \in A, t \in N, x \in M$ , les deux applications étant reliées par  $u(t, x) = f_{x}(t)$ .

(7.2.2) Soit  $T: Ab_{A} \rightarrow Ab$  un foncteur covariant additif. Nous allons définir pour tout A-module à gauche M, un homomorphisme canonique fonctoriel en M, de Z-modules

$$
t _ {\mathbf {M}}: \mathrm{T} (\mathrm{A} _ {s}) \otimes_ {\mathrm{A}} \mathrm{M} \rightarrow \mathrm{T} (\mathrm{M}).\tag{7.2.2.1}
$$

Il suffira pour cela, en vertu de (7.2.1), de définir un Z-homomorphisme $x \to t_{\mathrm{M}}'(x)$ de M dans $\operatorname{Hom}_{\mathbf{Z}}(\mathrm{T}(\mathrm{A}_s), \mathrm{T}(\mathrm{M}))$, tel que l'on ait $t_{\mathrm{M}}'(ax)(y) = t_{\mathrm{M}}'(x)(ya)$ pour $a \in \mathrm{A}$, $x \in \mathrm{M}$ et $y \in \mathrm{T}(\mathrm{A}_s)$. Notons pour cela que $\operatorname{Hom}_{\mathbf{Z}}(\mathrm{T}(\mathrm{A}_s), \mathrm{T}(\mathrm{M}))$ est canoniquement muni d'une structure de A-module à gauche provenant de la structure de A-module à droite de $\mathrm{T}(\mathrm{A}_s)$, la loi externe étant telle que si $a \in \mathrm{A}$, $v \in \operatorname{Hom}_{\mathbf{Z}}(\mathrm{T}(\mathrm{A}_s), \mathrm{T}(\mathrm{M}))$, $(a.v)(y) = v(ya)$ pour $y \in \mathrm{T}(\mathrm{A}_s)$. Cela étant, nous définirons $t_{\mathrm{M}}'$ comme composé des deux homomorphismes canoniques

$$
\mathbf {M} \stackrel {{\sim}} {{\to}} \operatorname{Hom} _ {\mathrm{A}} (\mathrm{A} _ {s}, \mathbf {M}) \stackrel {{\mathrm{T}}} {{\rightarrow}} \operatorname{Hom} _ {\mathbf {z}} (\mathrm{T} (\mathrm{A} _ {s}), \mathrm{T} (\mathbf {M}))
$$

la seconde flèche étant l'application $u \to \mathrm{T}(u)$, la première l'isomorphisme canonique de A-modules $x \mapsto \theta_x$ tel que $\theta_x(\xi) = \xi x$ pour $\xi \in \mathbf{A}$, $x \in \mathbf{M}$. On a $\theta_{ax} = \theta_x \circ h_a$, donc $\mathrm{T}(\theta_{ax}) = \mathrm{T}(\theta_x \circ h_a) = \mathrm{T}(\theta_x) \circ \mathrm{T}(h_a)$ et par suite, pour $y \in \mathrm{T}(\mathbf{A}_s)$,

$$
\mathrm{T} (\theta_ {a x}) (y) = \mathrm{T} (\theta_ {x}) (\mathrm{T} (h _ {a}) (y)) = \mathrm{T} (\theta_ {x}) (y a)
$$

par définition de la loi externe sur $\mathrm{T}(\mathbf{A}_{s})$, ce qui prouve l'existence de $t_{\mathbb{M}}$; il est immédiat de vérifier que cet homomorphisme est fonctoriel en $\mathbf{M}$, c'est-à-dire que pour tout homomorphisme $w: \mathbf{M} \to \mathbf{M}'$ de A-modules à gauche, le diagramme

$$
\begin{array}{c c c} \mathrm{T} (\mathrm{A} _ {s}) \otimes_ {\mathrm{A}} \mathrm{M} & \xrightarrow {t _ {\mathrm{M}}} & \mathrm{T} (\mathrm{M}) \\ \Bigg \downarrow_ {1 \otimes w} & & \Bigg \downarrow_ {\mathrm{T} (w)} \\ \mathrm{T} (\mathrm{A} _ {s}) \otimes_ {\mathrm{A}} \mathrm{M} ^ {\prime} & \xrightarrow {t _ {\mathrm{M} ^ {\prime}}} & \mathrm{T} (\mathrm{M} ^ {\prime}) \end{array}\tag{7.2.2.2}
$$

est commutatif.

La fonctorialité de l'homomorphisme (7.2.2.1) montre que lorsque A est commutatif, c'est un homomorphisme de A-modules (cf. (7.1.2)).

(7.2.3) Lorsque A est commutatif, on peut plus généralement définir un homomorphisme canonique de A-modules

$$
\mathbf {T} (\mathbf {N}) \otimes_ {\mathbf {A}} \mathbf {M} \rightarrow \mathbf {T} (\mathbf {N} \otimes_ {\mathbf {A}} \mathbf {M})\tag{7.2.3.1}
$$

pour tout A-module N; il suffit dans la construction de (7.2.2) de remplacer l'homomorphisme $\theta_{x}$ par l'homomorphisme de A-modules $\mathrm{N} \to \mathrm{N} \otimes_{\mathrm{A}} \mathrm{M}$ qui à tout $y \in \mathbb{N}$ fait correspondre $y \otimes x$. Il est immédiat que cet homomorphisme est fonctoriel en M et N.

En particulier, si B est une A-algèbre (non nécessairement commutative), on a un homomorphisme fonctoriel en M

$$
(\mathbf {T} (\mathbf {M})) _ {(\mathrm{B})} = \mathbf {T} (\mathbf {M}) \otimes_ {\mathrm{A}} \mathbf {B} \rightarrow \mathbf {T} (\mathbf {M} \otimes_ {\mathrm{A}} \mathbf {B}) = \mathbf {T} _ {(\mathrm{B})} (\mathbf {M} _ {(\mathrm{B})})\tag{7.2.3.2}
$$

qui, en vertu de la fonctorialité de (7.2.3.1) en M, est un homomorphisme de B-modules.

On a en outre le diagramme commutatif

(7.2.3.3)

![](images/page_44_image_5.jpg)

où la flèche verticale de droite est l'homomorphisme composé

$$
\mathrm{T} (\mathbf {M}) \rightarrow \mathrm{T} (\mathbf {M}) \otimes_ {\mathrm{A}} \mathrm{B} \rightarrow \mathrm{T} (\mathbf {M} \otimes_ {\mathrm{A}} \mathrm{B}) = \mathrm{T} _ {(\mathrm{B})} (\mathbf {M} _ {(\mathrm{B})})
$$

de (7.2.3.2) et de l'homomorphisme canonique; quant à la flèche verticale de gauche de (7.2.3.3), c'est l'homomorphisme  $\mathrm{T}(\mathrm{A})\otimes_{\mathrm{A}}\mathrm{M}\to\mathrm{T}_{(\mathrm{B})}(\mathrm{B}_{s})\otimes_{\mathrm{B}}(\mathrm{B}\otimes_{\mathrm{A}}\mathrm{M})=\mathrm{T}_{(\mathrm{B})}(\mathrm{B}_{s})\otimes_{\mathrm{A}}\mathrm{M}$  où  $\mathrm{T}(\mathrm{A})\to\mathrm{T}_{(\mathrm{B})}(\mathrm{B}_{s})=\mathrm{T}(\mathrm{B})$  est  $\mathrm{T}(\rho)$ ,  $\rho$  étant considéré comme homomorphisme de A-modules  $A\to B_{[\rho]}$ .

Lemme (7.2.4). — Si T est un foncteur covariant additif de  $Ab_{A}$  dans Ab, commutant avec les sommes directes, l'homomorphisme canonique  $t_{L}$  (7.2.2.1) est un isomorphisme pour tout A-module libre L.

En effet, on a  $L=\bigoplus_{\alpha\in I}L_{\alpha}$  où  $L_{\alpha}$  est isomorphe à  $A_{s}$  pour tout  $\alpha\in I$ ; la définition de  $t_{M}$  donnée dans (7.2.2) montre que  $t_{L}=\bigoplus_{\alpha\in I}t_{L_{\alpha}}$ , puisque

$$
\mathrm{T}: \operatorname{Hom} _ {\mathrm{A}} (\mathrm{A} _ {s}, \mathrm{L}) \rightarrow \operatorname{Hom} _ {\mathbf {z}} (\mathrm{T} (\mathrm{A} _ {s}), \mathrm{T} (\mathrm{L}))
$$

est somme directe des applications Z-linéaires  $T_{\alpha}: \mathrm{Hom}_{\mathrm{A}}(\mathrm{A}_{s}, \mathrm{L}_{\alpha}) \to \mathrm{Hom}_{\mathbf{Z}}(\mathrm{T}(\mathrm{A}_{s}), \mathrm{T}(\mathrm{L}_{\alpha}))$  en vertu de l'hypothèse sur T. On est donc ramené à prouver le lemme pour  $L = A_{s}$ ; mais  $t_{L}$  n'est autre alors que l'isomorphisme canonique  $\mathrm{T}(\mathrm{A}_{s}) \otimes_{\mathrm{A}} \mathrm{A}_{s} \xrightarrow{\sim} \mathrm{T}(\mathrm{A}_{s})$  valable pour tout A-module à droite.

Proposition (7.2.5). — Soit T un foncteur covariant additif de  $Ab_{A}$  dans Ab, commutant aux sommes directes. Les conditions suivantes sont équivalentes :

a) T est exact à droite.

b) L'homomorphisme canonique  $t_{M}$  (7.2.2.1) est un isomorphisme pour tout A-module à gauche M.

$b^{\prime})$ T est semi-exact et l'homomorphisme $t_{\mathbb{M}}$ est surjectif pour tout A-module à gauche M.

c) T est isomorphe à un foncteur en M de la forme $\mathbf{N} \otimes_{\mathbf{A}} \mathbf{M}$, où N est un A-module à droite.

Il est clair que $b)$ implique $c)$ et que $c)$ implique $a)$; montrons que $a)$ implique $b)$.

Posons  $\mathrm{T}^{\prime}(\mathrm{M})=\mathrm{T}(\mathrm{A}_{\mathrm{s}})\otimes_{\mathrm{A}}\mathrm{M}$  pour tout A-module à gauche M. Il existe une suite exacte  $L^{\prime}\rightarrow L\rightarrow M\rightarrow0$ , où L et  $L^{\prime}$  sont deux A-modules à gauche libres; comme T et  $T^{\prime}$  sont exacts à droite, on a donc le diagramme commutatif

$$
\begin{array}{c c c c} \mathrm{T} ^ {\prime} (\mathrm{L} ^ {\prime}) & \to \mathrm{T} ^ {\prime} (\mathrm{L}) & \to \mathrm{T} ^ {\prime} (\mathrm{M}) & \to 0 \\ t _ {\mathrm{L} ^ {\prime}} \Bigg \downarrow & t _ {\mathrm{L}} \Bigg \downarrow & t _ {\mathrm{M}} \Bigg \downarrow \\ \mathrm{T} (\mathrm{L} ^ {\prime}) & \to \mathrm{T} (\mathrm{L}) & \to \mathrm{T} (\mathrm{M}) & \to 0 \end{array}
$$

où les deux lignes sont exactes; comme $t_{\mathrm{L}}$ et $t_{\mathrm{L}'}$ sont des isomorphismes en vertu de (7.2.4), il en est de même de $t_{\mathbb{M}}$ par le lemme des cinq. Enfin, il est clair que $b)$ entraîne $b')$. Pour montrer que $b')$ entraîne $a)$, il suffit de prouver le

Lemme (7.2.5.1). — Soient K,  $K'$  deux catégories abéliennes, F, G deux foncteurs covariants additifs de K dans  $K'$ ,  $f: F \to G$  un morphisme fonctoriel (T, I, 1.2) tel que, pour tout objet E de la catégorie K,  $f_{\mathrm{E}}: \mathrm{F}(\mathrm{E}) \to \mathrm{G}(\mathrm{E})$  soit un épimorphisme. Alors, si F est exact à droite et G semi-exact, G est exact à droite.

Tout revient en effet à démontrer que pour tout épimorphisme $v: \mathrm{E}' \to \mathrm{E}$ dans $\mathbf{K}$, $\mathrm{G}(v): \mathrm{G}(\mathrm{E}') \to \mathrm{G}(\mathrm{E})$ est un épimorphisme; or, on a le diagramme commutatif

$$
\begin{array}{c c c} \mathrm{F} (\mathrm{E} ^ {\prime}) & \xrightarrow {\mathrm{F} (v)} & \mathrm{F} (\mathrm{E}) \\ \Bigg \downarrow f _ {\mathrm{E} ^ {\prime}} & & \Bigg \downarrow f _ {\mathrm{E}} \\ \mathrm{G} (\mathrm{E} ^ {\prime}) & \xrightarrow {\mathrm{G} (v)} & \mathrm{G} (\mathrm{E}) \end{array}
$$

dans lequel $\mathbf{F}(v), f_{\mathrm{E}'}$ et $f_{\mathrm{E}}$ sont des épimorphismes; il en est donc de même de $\mathbf{G}(v)$.

Remarque (7.2.6). — Pour tout A-module à droite N, posons  $\mathrm{T}_{\mathrm{N}}(\mathrm{M})=\mathrm{N}\otimes_{\mathrm{A}}\mathrm{M}$  pour tout A-module à gauche M, de sorte que  $T_{N}$  est un foncteur covariant additif de  $Ab_{A}$  dans Ab, exact à droite et commutant aux sommes directes. Si on identifie canoniquement  $\mathrm{T}_{\mathrm{N}}(\mathrm{A}_{s})$  à N, on vérifie aussitôt que l'homomorphisme correspondant (7.2.2.1) devient l'identité. On en conclut que le A-module à droite N de l'énoncé de (7.2.5, c)) est déterminé à un isomorphisme unique près et est canoniquement isomorphe à  $\mathrm{T}(\mathrm{A}_{s})$ . On peut encore dire que les morphismes fonctoriels  $\mathrm{T}\leadsto\mathrm{T}(\mathrm{A}_{s})$  et  $N\leadsto T_{N}$  constituent une équivalence (T, I, 1.2) de la catégorie des A-modules à droite et de la catégorie des foncteurs covariants additifs  $Ab_{A}\rightarrow Ab$  qui sont exacts à droite et commutent aux sommes directes.

Proposition (7.2.7). — Soient A un anneau artinien à gauche, dont le quotient par son radical m est un corps k. Soit T un foncteur covariant additif de  $Ab_{A}$  dans Ab, commutant aux sommes directes. Les conditions de (7.2.5) sont alors aussi équivalentes à

d) T est semi-exact et l'homomorphisme  $\mathbf{T}(\varepsilon):\mathbf{T}(\mathbf{A}_{s})\to\mathbf{T}(k)$  déduit de l'homomorphisme canonique  $\varepsilon:\mathbf{A}_{s}\to k$  est surjectif.

Il est clair que la condition $b'$ de (7.2.5) entraîne $d$; prouvons que $d$ entraîne $b'$. Il existe un entier $n$ tel que $m^n = 0$; posons, pour tout A-module M, $M_h = m^h M$; nous prouverons par récurrence descendante sur $h$ que $t_{M_h}$ est surjectif. La proposition est évidente pour $h = n$; pour $h < n$, on a une suite exacte

$$
\mathrm{o} \rightarrow \mathbf {M} _ {h + 1} \rightarrow \mathbf {M} _ {h} \rightarrow \mathbf {M} _ {h} / \mathbf {M} _ {h + 1} \rightarrow \mathrm{o}
$$

et l'hypothèse de récurrence entraîne que $t_{\mathrm{M}_{h+1}}$ est surjectif. D'autre part, $\mathbf{M}_h / \mathbf{M}_{h+1}$ est annulé par $m$ et est donc un $(A/m)$-module, autrement dit est somme directe de A-modules isomorphes à $k$. Pour prouver que $t_{\mathrm{M}_h / \mathrm{M}_{h+1}}$ est surjectif, il suffit donc de prouver que $t_k$ l'est, puisque T commute aux sommes directes. Or, en vertu de la commutativité du diagramme

$$
\begin{array}{c} \mathrm{T} (\mathrm{A} _ {s}) \otimes_ {\mathrm{A}} \mathrm{A} _ {s} \xrightarrow {t _ {\mathrm{A} _ {s}}} \mathrm{T} (\mathrm{A} _ {s}) \\ \Bigg \downarrow^ {1 \otimes \varepsilon} \\ \mathrm{T} (\mathrm{A} _ {s}) \otimes_ {\mathrm{A}} k \xrightarrow {t _ {k}} \mathrm{T} (k) \end{array}
$$

et de (7.2.4), l'hypothèse $d$) entraîne que $t_{k}$ est bien surjectif. Pour terminer la démonstration, il suffira de prouver que si l'on a une suite exacte $o \to M' \to M \xrightarrow{v} M'' \to o$ de A-modules, telle que $t_{M'}$ et $t_{M''}$ sont surjectifs, alors $t_{M}$ est surjectif. Or, on a un diagramme commutatif

$$
\begin{array}{c} \mathrm{T} ^ {\prime} (\mathrm{M} ^ {\prime}) \longrightarrow \mathrm{T} ^ {\prime} (\mathrm{M}) \longrightarrow \mathrm{T} ^ {\prime} (\mathrm{M} ^ {\prime \prime}) \longrightarrow \mathrm{o} \\ t _ {\mathrm{M} ^ {\prime}} \Bigg | _ {\downarrow} \qquad \qquad t _ {\mathrm{M}} \Bigg | _ {\downarrow} \qquad \qquad t _ {\mathrm{M} ^ {\prime \prime}} \Bigg | _ {\downarrow} \\ \mathrm{T} (\mathrm{M} ^ {\prime}) \longrightarrow \mathrm{T} (\mathrm{M}) \xrightarrow [ \mathrm{T} (v) ]{} \mathrm{T} (\mathrm{M} ^ {\prime \prime}) \longrightarrow \operatorname{Coker} (\mathrm{T} (v)) \end{array}
$$

dans lequel les deux lignes sont exactes, en vertu de l'hypothèse que T est semi-exact. Comme par l'hypothèse de récurrence $t_{\mathbb{M}}$, et $t_{\mathbb{M}''}$ sont des épimorphismes et que la dernière flèche verticale est un monomorphisme, le lemme des cinq (M, I, 1.1) montre que $t_{\mathbb{M}}$ est un épimorphisme.

## 7.3. Critères d'exactitude des foncteurs homologiques de modules.

Proposition (7.3.1). — Soient A un anneau (non nécessairement commutatif), T. un foncteur homologique covariant (T, II, 2.1) de la catégorie  $Ab_{A}$  dans la catégorie Ab, commutant aux sommes directes. Soit p un entier tel que  $T_{p}$  et  $T_{p-1}$  soient définis. Les conditions suivantes sont équivalentes :

a) $\mathbf{T}_p$ est exact à droite.

b) $\mathrm{T}_{p - 1}$ est exact à gauche.

180

c) Pour tout A-module à gauche M, l'homomorphisme fonctoriel canonique (7.2.2.1)

$$
\mathbf {T} _ {p} (\mathbf {A} _ {s}) \otimes_ {\mathbf {A}} \mathbf {M} \rightarrow \mathbf {T} _ {p} (\mathbf {M})\tag{7.3.1.1}
$$

est un isomorphisme.

d) Pour tout A-module à gauche M, l'homomorphisme (7.3.1.1) est un épimorphisme.

e)  $T_{p}$  est isomorphe à un foncteur  $M \leadsto N \otimes_{A} M$ , où N est un A-module à droite.

Si en outre les conditions de (7.2.7) sur A et m sont vérifiées, les conditions précédentes sont aussi équivalentes à

f) L'homomorphisme canonique  $\mathrm{T}_{p}(\varepsilon):\mathrm{T}_{p}(\mathrm{A}_{s})\to\mathrm{T}_{p}(k)$  est un épimorphisme.

Comme par définition d'un foncteur homologique,  $T_{i}$  est semi-exact pour tous les i tels que  $T_{i}$  soit défini, et que, pour toute suite exacte  $o \to M' \stackrel{u}{\to} M \stackrel{v}{\to} M'' \to 0$ , on a  $\operatorname{Ker}(T_{i-1}(u)) = \operatorname{Coker}(T_{i}(v))$ , il est clair que a) et b) sont équivalentes et les autres assertions résultent trivialement de (7.2.5) et (7.2.7).

Corollaire (7.3.2). — Soit A un anneau commutatif. Avec les notations de (7.3.1), supposons  $T_{p}$  exact à droite. Si  $f \in A$  n'appartient à l'annulateur d'aucun élément  $\neq o$  d'un A-module M, alors f n'appartient à l'annulateur d'aucun élément  $\neq o$  de  $T_{p-1}(M)$ . En particulier, si A est intègre, le A-module  $T_{p-1}(A)$  est sans torsion.

En effet, si $h_f$ désigne l'homothétie $x \to fx$ de M, l'hypothèse signifie que $h_f$ est injectif; il en est donc de même de $T_{p-1}(h_f)$ par la condition $b)$ de (7.3.1).

Proposition (7.3.3). — Soient A un anneau, T. un foncteur homologique covariant de  $Ab_{A}$  dans Ab, commutant aux sommes directes. Soit p un entier tel que  $T_{p-1}$ ,  $T_{p}$  et  $T_{p+1}$  soient définis. Les conditions suivantes sont équivalentes :

a) $\mathbf{T}_p$ est exact.

b) $\mathrm{T}_{p + 1}$ et $\mathrm{T}_p$ sont exacts à droite.

c) $\mathbf{T}_p$ et $\mathbf{T}_{p - 1}$ sont exacts à gauche.

d) $\mathbf{T}_{p + 1}$ est exact à droite et $\mathbf{T}_{p - 1}$ est exact à gauche.

e) Pour tout A-module M, les homomorphismes canoniques

$$
(7 \cdot 3 \cdot 3 \cdot \mathbf {1})
$$

$$
\mathbf {T} _ {i} (\mathbf {A} _ {s}) \otimes_ {\mathbf {A}} \mathbf {M} \rightarrow \mathbf {T} _ {i} (\mathbf {M})
$$

sont des isomorphismes pour $i=p$ et $i=p+1$.

$e^{\prime})$ Pour tout A-module M, les homomorphismes canoniques (7.3.3.1) sont des épimorphismes pour $i=p$ et $i=p+1$.

f) Pour tout A-module M, l'homomorphisme (7.3.3.1) est un isomorphisme pour i=p et  $\mathrm{T}_{p}(\mathrm{A}_{s})$  est un A-module à droite plat.

$f^{\prime})$ Pour tout A-module M, l'homomorphisme (7.3.3.1) est un épimorphisme pour $i=p$ et $\mathbf{T}_{p}(\mathbf{A}_{s})$ est un A-module à droite plat.

L'équivalence des conditions $a$, $b$, $c$, $d$ ) résulte de l'équivalence des conditions $a$ ) et $b$ ) de (7.3.1). L'équivalence de $b$, $e$ ) et $e'$ ) résulte de l'équivalence de $a$, $c$ ) et $d$ ) dans (7.3.1). Enfin, dire que $\mathrm{T}_{p}(\mathrm{A}_{s})$ est plat signifie que le foncteur $\mathbf{M}\rightsquigarrow \mathrm{T}_{p}(\mathrm{A}_{s})\otimes_{\mathrm{A}}\mathbf{M}$ est exact à gauche; l'équivalence de $a$, $f$ ) et $f'$ ) résulte encore de l'équivalence de $a$, $c$), $d$ ) dans (7.3.1).

Corollaire (7.3.4). — Supposons A commutatif,  $T_{p}$  exact et supposons en outre que  $\mathrm{T}_{p}(\mathrm{A})$  soit un A-module de présentation finie. Alors la fonction  $x \to \operatorname{rang}_{\mathbf{k}(x)}(\mathrm{T}_{p}(\mathbf{k}(x)))$  est localement constante dans  $\mathbf{X} = \operatorname{Spec}(\mathbf{A})$ , donc constante si  $\operatorname{Spec}(\mathbf{A})$  est connexe.

En effet, comme  $\mathrm{T}_{p}(\mathrm{A})$  est un A-module plat en vertu de  $(7.3.3,f)$ , il est projectif de type fini, et  $(\mathrm{T}_{p}(\mathrm{A}))^{\sim}$  est donc un  $O_{X}$ -Module localement libre (Bourbaki, Alg. comm., chap. II, § 5, n° 2, th. 1); on a en outre  $\mathrm{T}_{p}(\boldsymbol{k}(x))=\mathrm{T}_{p}(\mathrm{A})\otimes_{\mathrm{A}}\boldsymbol{k}(x)$  (7.3.3, e)) et l'on sait que le rang au point x du A-module  $\mathrm{T}_{p}(\mathrm{A})$  est localement constant (loc. cit.), d'où le corollaire.

Proposition (7.3.5). — Supposons que A soit un anneau artinien à gauche dont le quotient par son radical m est un corps k. Alors les conditions de (7.3.3) sont encore équivalentes à chacune des suivantes :

g) L'homomorphisme canonique  $\mathrm{T}_{i}(\varepsilon):\mathrm{T}_{i}(\mathrm{A}_{s})\rightarrow\mathrm{T}_{i}(k)$  est un épimorphisme pour i=p et  $i=p+1$ .

h)  $\mathrm{T}_{p}(\varepsilon)$  est un épimorphisme et  $\mathrm{T}_{p}(\mathrm{A}_{s})$  est un A-module à droite plat (ou, ce qui revient au même (Bourbaki, Alg. comm., chap. II, § 3, n° 2, cor. 2 de la prop. 5) un A-module libre).

Supposons en outre que A soit commutatif et le A-module  $\mathrm{T}_{p}(k)$  de longueur finie d. Alors les conditions précédentes équivalent aussi à chacune des suivantes :

i) Pour tout A-module M de longueur finie, on a

$$
\operatorname{long} \left(\mathrm{T} _ {p} (\mathbf {M})\right) = d. \operatorname{long} (\mathbf {M}).\tag{7.3.5.1}
$$

j) On a

$$
(7 \cdot 3 \cdot 5 \cdot 2)
$$

$$
\operatorname{long} \left(\mathrm{T} _ {p} (\mathrm{A})\right) = d. \operatorname{long} (\mathrm{A}).
$$

L'équivalence de $g$ ) et $h$ ) avec les conditions de (7.3.3) découle aussitôt de (7.2.7). Pour démontrer les autres assertions, nous utiliserons le lemme suivant :

Lemme (7.3.5.3). — Soient K,  $K'$  deux catégories abéliennes,  $F:K\to K'$  un foncteur covariant additif; on suppose que F soit semi-exact, et que, pour tout objet simple S de K,  $\mathrm{F}(\mathrm{S})$  soit un objet de longueur finie dans  $K'$ . Alors, pour tout objet E de longueur finie dans K,  $\mathrm{F}(\mathrm{E})$  est de longueur finie dans  $K'$ . Pour toute suite exacte  $o\to E'\xrightarrow{u}E\xrightarrow{v}E''\to o$  d'objets de longueur finie dans K, on a

$$
\operatorname{long} \mathrm{F} (\mathrm{E}) \leqslant \operatorname{long} \mathrm{F} \left(\mathrm{E} ^ {\prime}\right) + \operatorname{long} \mathrm{F} \left(\mathrm{E} ^ {\prime \prime}\right)\tag{7·3·5·4}
$$

et pour que les deux membres de (7.3.5.4) soient égaux, il faut et il suffit que la suite

$$
\mathrm{o} \rightarrow \mathrm{F} (\mathrm{E} ^ {\prime}) \rightarrow \mathrm{F} (\mathrm{E}) \rightarrow \mathrm{F} (\mathrm{E} ^ {\prime \prime}) \rightarrow \mathrm{o}
$$

soit exacte.

En effet, la suite  $\mathrm{F}(\mathrm{E}^{\prime})\xrightarrow{\mathrm{F}(u)}\mathrm{F}(\mathrm{E})\xrightarrow{\mathrm{F}(v)}\mathrm{F}(\mathrm{E}^{\prime\prime})$  est exacte par hypothèse; si l'on suppose  $\mathrm{F}(\mathrm{E}^{\prime})$  et  $\mathrm{F}(\mathrm{E}^{\prime\prime})$  de longueur finie, il en est de même de  $\mathrm{Im}(\mathrm{F}(u))$  et de  $\mathrm{Im}(\mathrm{F}(v))$  et comme  $\mathrm{Ker}(\mathrm{F}(v))=\mathrm{Im}(\mathrm{F}(u))$ ,  $\mathrm{F}(\mathrm{E})$  est de longueur finie et l'on a

$$
\text { long   } \mathrm{F} (\mathrm{E}) = \text { long   } \mathrm{Im} (\mathrm{F} (u)) + \text { long   } \mathrm{Im} (\mathrm{F} (v)) \leqslant \text { long   } \mathrm{F} (\mathrm{E} ^ {\prime}) + \text { long   } \mathrm{F} (\mathrm{E} ^ {\prime \prime}). \tag {7.3.5.5}
$$

182

Par récurrence sur la longueur de E, cela prouve déjà la première assertion; en outre, les deux membres de (7.3.5.5) ne peuvent être égaux que si long $\operatorname{Im}(\mathbf{F}(u)) = \operatorname{long}\mathbf{F}(\mathbf{E}')$ (ce qui équivaut à long $\operatorname{Ker}(\mathbf{F}(u)) = 0$, ou $\operatorname{Ker}(\mathbf{F}(u)) = 0$) et long $\operatorname{Im}(\mathbf{F}(v)) = \operatorname{long}\mathbf{F}(\mathbf{E}'')$ (ce qui équivaut à long $\operatorname{Coker}(\mathbf{F}(v)) = 0$, ou $\operatorname{Coker}(\mathbf{F}(v)) = 0$).

Notons maintenant que si M est un A-module de longueur finie (A étant commutatif), les quotients d'une suite de Jordan-Hölder de M sont nécessairement isomorphes au A-module k, donc on déduit de  $(7.3.5.4)$ , par récurrence sur la longueur de M

$$
\operatorname{long} \mathrm{T} _ {p} (\mathbf {M}) \leqslant d. \operatorname{long} (\mathbf {M}).\tag{7.3.5.6}
$$

En outre, il résulte de (7.3.5.3) que si  $T_{p}$  est exact, on a l'égalité (7.3.5.1); donc la condition a) de (7.3.3) entraîne i); il est clair que i) entraîne j), et il reste à prouver le

Lemme (7.3.5.7). — La relation long  $\mathrm{T}_{p}(\mathrm{A})=d$ . long A entraîne que  $\mathrm{T}_{p}(\varepsilon)$  est un épimorphisme et que  $\mathrm{T}_{p}(\mathrm{A})$  est un A-module plat.

En effet, partant de la suite exacte $\mathrm{o} \to \mathfrak{m} \to \mathrm{A} \to k \to \mathrm{o}$, il résulte de (7.3.5.4) et (7.3.5.6) que l'on a

$$
\operatorname{long} \mathrm{T} _ {p} (\mathrm{A}) \leqslant \operatorname{long} \mathrm{T} _ {p} (\mathfrak {m}) + \operatorname{long} \mathrm{T} _ {p} (k) \leqslant d (\operatorname{long} \mathfrak {m} + \operatorname{long} k) = d. \text { long } \mathrm{A}
$$

et que l'égalité ne peut avoir lieu (7.3.5.3) que si la suite

$$
\mathrm{o} \rightarrow \mathrm{T} _ {p} (\mathfrak {m}) \rightarrow \mathrm{T} _ {p} (\mathrm{A}) \rightarrow \mathrm{T} _ {p} (k) \rightarrow \mathrm{o}\tag{7.3.5.8}
$$

est exacte. En vertu de (7.2.7) et (7.2.5),  $T_{p}$  est isomorphe à un foncteur  $M \leadsto N \otimes_{A} M$ , et l'exactitude de la suite (7.3.5.8) montre, en vertu de la suite exacte des Tor, que l'on a  $\operatorname{Tor}_{1}^{A}(N, k) = o$ . On en conclut que  $N = T_{p}(A)$  est un A-module plat (0, 10.1.3).

Lemme (7.3.6). — Soient A un anneau, T. un foncteur homologique covariant de  $Ab_{A}$  dans Ab, commutant aux sommes directes. Supposons  $T_{p}$  et  $T_{p+1}$  définis, et  $T_{p}$  exact à gauche. Pour que  $T_{p+1}$  soit exact, il faut et il suffit que  $\mathrm{T}_{p+1}(\mathrm{A}_{s})$  soit un A-module à droite plat.

En effet, on sait d'après (7.3.1) que l'homomorphisme canonique

$$
\mathbf {T} _ {p + 1} (\mathbf {A} _ {s}) \otimes_ {\mathbf {A}} \mathbf {M} \rightarrow \mathbf {T} _ {p + 1} (\mathbf {M})
$$

est un isomorphisme de foncteurs; il suffit d'appliquer la définition d'un A-module plat. Proposition (7.3.7). — Soient A un anneau, T. un foncteur homologique covariant de  $Ab_{A}$  dans Ab, commutant aux sommes directes. On suppose qu'il existe  $i_{0}$  tel que  $T_{i}$  soit exact pour  $i \leqslant i_{0}$ . Alors, pour tout entier  $p > i_{0}$ , les conditions suivantes sont équivalentes :

a) $\mathbf{T}_q$ est exact pour $q \leqslant p$;

b) $\mathbf{T}_q(\mathbf{A}_s)$ est un A-module à droite plat pour $q \leqslant p$.

c) Pour tout A-module M, l'homomorphisme canonique  $\mathrm{T}_{q}(\mathrm{A}_{s})\otimes_{\mathrm{A}}\mathrm{M}\to\mathrm{T}_{q}(\mathrm{M})$  est surjectif pour  $q\leqslant p+1$ .

L'équivalence de $a$ et $b$ ) résulte de (7.3.6) par récurrence sur $q$, puisque $\mathrm{T}_{i_0}$ est exact par hypothèse; l'équivalence de $a$ ) et $c$ ) résulte de l'équivalence des conditions $a$ ) et $e'$ ) dans (7.3.3).

(7.3.8) Si A est un anneau commutatif, B une A-algèbre (non nécessairement commutative), T. un foncteur homologique covariant de  $Ab_{A}$  dans Ab, il résulte des définitions (7.1.3) que le foncteur de  $Ab_{B}$  dans Ab obtenu par extension des scalaires de A à B, et que nous noterons  $\mathrm{T}_{\bullet}^{(\mathrm{B})} = (\mathrm{T}_{i}^{(\mathrm{B})})$ , est encore un foncteur homologique.

Corollaire (7.3.9). — Supposons que T. vérifie les conditions générales de (7.3.7) et commute aux limites inductives, et en outre que A soit un anneau intègre et tous les  $\mathrm{T}_{n}(\mathrm{A})$  des A-modules de présentation finie. Alors, pour tout entier N, il existe un  $f \in A - \{0\}$  tel que le foncteur  $\mathrm{T}_{p}^{(\mathrm{A}_{f})}: \mathbf{A}\mathbf{b}_{\mathbf{A}_{f}} \to \mathbf{A}\mathbf{b}$  soit exact pour  $p \leqslant N$ .

Par hypothèse,  $T_{i}$  est exact pour  $i \leqslant i_{0}$ , donc  $\mathrm{T}_{i}(\mathrm{A})$  est plat pour ces valeurs de i. En vertu de (7.3.7, b)), il suffit de prendre f tel que  $\mathrm{T}_{p}^{(\mathrm{A})f}(\mathrm{A}_{f}) = \mathrm{T}_{p}(\mathrm{A}_{f})$  soit un  $A_{f}$ -module libre pour  $i_{0} < p \leqslant N$ . Or, on a  $\mathrm{T}_{p}(\mathrm{A}_{f}) = (\mathrm{T}_{p}(\mathrm{A}))_{f}$  puisque  $T_{p}$  commute aux limites inductives (7.1.4). Si x est le point générique de Spec(A),  $(\mathrm{T}_{p}(\mathrm{A}))_{x}$  est un espace vectoriel de dimension finie sur le corps des fractions de A. Comme chaque  $T_{p}(\mathrm{A})$  est de présentation finie, il existe bien un f ayant la propriété voulue (Bourbaki, Alg. comm., chap. II, § 5, n° 1, cor. de la prop. 2).

On notera que s'il n'y a qu'un nombre fini d'indices i tels que  $T_{i} \neq o$ , il existe  $f \in A - \{o\}$  tel que tous les  $\mathrm{T}_{p}^{(\Lambda_{f})}$  soient exacts.

Corollaire (7.3.10). — Supposons que T. vérifie les conditions générales de (7.3.7) et commute aux limites inductives, que A soit commutatif et noethérien et les  $\mathrm{T}_{n}(\mathrm{A})$  des A-modules de type fini. Alors, pour tout entier N, il existe un ouvert dense U de Spec(A) tel que, pour tout  $p \leqslant N$ , la fonction  $x \to \operatorname{rang}_{\mathbf{k}(x)}(\mathbf{T}_{p}(\mathbf{k}(x)))$  soit constante dans U.

Soit p un idéal premier minimal de A; par hypothèse, l'anneau B = A/p est intègre et Spec(B) s'identifie à une composante irréductible de l'espace topologique Spec(A). Nous allons montrer par récurrence sur  $p \leqslant N$  qu'il existe  $f_{p} \in B - \{o\}$  tel que si on pose  $B' = B_{f_{p}}$ ,  $T_{i}^{(B')}$  soit exact et les  $T_{i}(B')$  des B'-modules de type fini pour  $i \leqslant p$ . La proposition est vraie pour  $p \leqslant i_{0}$  en vertu de l'hypothèse, en prenant  $f_{p} = I$  (donc  $B' = B = A/p$ ) car  $T_{p}$  étant alors exact,  $T_{p}(B)$  est isomorphe à  $T_{p}(A)/T_{p}(p)$ , donc est un A-module (et a fortiori un B-module) de type fini. Raisonnons par récurrence sur p;  $f_{p}$  est l'image canonique dans B d'un élément  $g_{p} \in A$ , et si l'on pose  $A' = A_{g_{p}}$ , on a  $B' = A'/p'$  où  $p'$  est un idéal premier minimal de  $A'$ , égal à  $p_{g_{p}}$ . Comme on a  $T_{i}(A_{g_{p}}) = (T_{i}(A))_{g_{p}}$ , les  $T_{i}(A')$  sont des A'-modules de type fini, donc le foncteur  $T_{i}^{(A')}$  vérifie les mêmes hypothèses que  $T_{*}$ , mais en remplaçant  $i_{0}$  par p. On peut donc se borner au cas où  $A' = A$ , et où  $T_{p}$  est exact; la suite exacte  $o \to p \to A \to A/p \to o$  donne alors la suite exacte  $T_{p+1}(A) \to T_{p+1}(A/p) \xrightarrow{\partial} T_{p}(p) \to T_{p}(A)$ , et comme  $T_{p}$  est exact, la dernière flèche de droite est injective, donc  $T_{p+1}(A/p)$  est un quotient de  $T_{p+1}(A)$  et est par suite de type fini. Notons maintenant que le raisonnement de (7.3.9) n'a utilisé le fait que les  $T_{p}(A)$  sont de type fini que pour  $p \leqslant N$ ; on peut donc l'appliquer à l'anneau intègre B, au foncteur  $T_{i}^{(B)}$  et à  $N = p + I$ , ce qui achève le raisonnement par récurrence. Cela étant, il y a un  $f_{N} \in B - \{o\}$  tel que Spec( $B_{f_{N}}$ ) soit un ouvert V partout dense dans Spec(B) ne rencontrant aucune autre composante irréductible de Spec(A). Si la proposition est

démontrée pour  $B_{f_{N}}$ , on aura un ouvert W partout dense dans V dans lequel les fonctions de l'énoncé seront constantes, puisque  $\mathbf{A}_{x}=(\mathbf{B}_{f_{N}})_{x}$  pour tout  $x\in W$ . En faisant le même raisonnement pour toute composante irréductible de Spec(A), le corollaire sera démontré. On peut donc se borner au cas où A est intègre; le raisonnement de (7.3.9) prouve alors l'existence d'un  $f\in A-\{0\}$  tel que les  $\mathrm{T}_{p}(\mathrm{A}_{f})$  soient des  $A_{f}$ -modules libres de type fini pour  $p\leqslant N$ , ce qui entraîne la conclusion de (7.3.10) en vertu de (7.3.4).

Proposition (7.3.11). — Soient A un anneau commutatif local, k son corps résiduel, T. un foncteur homologique covariant de  $Ab_{A}$  dans Ab, commutant aux sommes directes. On suppose qu'il existe  $i_{0}$  tel que  $T_{i}$  soit exact pour  $i \leqslant i_{0}$ , et que tous les  $T_{n}(A)$  soient des A-modules de présentation finie. Alors les conditions équivalentes a), b), c) de (7.3.7) impliquent les deux suivantes, et leur sont équivalentes lorsque l'anneau est en outre réduit :

d) Pour tout $x \in \operatorname{Spec}(\mathbf{A})$, on a $\operatorname{rang}_{\mathbf{k}(x)} \mathrm{T}_q(\boldsymbol{k}(x)) = \operatorname{rang}_k \mathrm{T}_q(k)$ pour $q \leqslant p$.

$d^{\prime})$ Pour tout point générique $x_{j}$ d'une composante irréductible de $\operatorname{Spec}(\mathbf{A})$, on a

$$
\operatorname{rang} _ {\mathbf {k} \left(x _ {j}\right)} \mathrm{T} _ {q} (\boldsymbol {k} \left(x _ {j}\right)) = \operatorname{rang} _ {k} \mathrm{T} _ {q} (k) \text {   pour   } q \leqslant p.
$$

Comme $\mathbf{T}_q(\mathbf{A})$ est un A-module de présentation finie, la condition $b)$ de (7.3.7) équivaut à dire que $\mathbf{T}_q(\mathbf{A})$ est un A-module libre pour $q \leqslant p$ (Bourbaki, Alg. comm., chap. II, § 3, n° 2, cor. 2 de la prop. 5); la condition $c)$ implique que $\mathbf{T}_q(\boldsymbol{k}(x)) = \mathbf{T}_q(\mathbf{A}) \otimes_{\mathbf{A}} \boldsymbol{k}(x)$ pour $q \leqslant p$, donc les conditions équivalentes de (7.3.7) impliquent $d)$, et il est trivial que $d)$ entraîne $d'$). Reste à prouver que $d'$) implique $a)$ lorsque A est réduit. Raisonnons par récurrence sur $q \leqslant p$, puisque $\mathbf{T}_q$ est exact pour $q \leqslant i_0$. Supposons donc $\mathbf{T}_k$ exact pour $k \leqslant q < p$ et montrons que $\mathbf{T}_{q+1}(\mathbf{A})$ est un A-module libre. En vertu de l'hypothèse de récurrence, $\mathbf{T}_{q+1}(\mathbf{A}) \otimes_{\mathbf{A}} \mathbf{M}$ est isomorphe à $\mathbf{T}_{q+1}(\mathbf{M})$ pour tout A-module $\mathbf{M}$, par la condition $c)$ de (7.3.7) et (7.3.3); appliquant cette propriété à $\mathbf{M} = \boldsymbol{k}(x_j)$ et $\mathbf{M} = k$, on trouve, en vertu de l'hypothèse $d'$), que

$$
\operatorname{rang} _ {\mathbf {k} (x _ {j})} \left(\mathrm{T} _ {q + 1} (\mathrm{A}) \otimes_ {\mathrm{A}} \boldsymbol {k} (x _ {j})\right) = \operatorname{rang} _ {k} \mathrm{T} _ {q + 1} (k)
$$

pour tout $i$; mais cela implique que $\mathbf{T}_{q+1}(\mathbf{A})$ est libre (Bourbaki, Alg. comm., chap. II, § 3, n° 2, prop. 7), ce qui achève la démonstration.

Les résultats précédents seront considérablement améliorés pour les foncteurs homologiques de type particulier que nous allons étudier dans (7.4); on obtiendra en effet des critères d'exactitude ne faisant intervenir qu'un seul des  $T_{p}$ .

## 7.4. Critères d'exactitude pour les foncteurs H.(P.⊗A M).

(7.4.1) Soient A un anneau (non nécessairement commutatif), P. un complexe de A-modules à droite plats. Comme le foncteur  $M \rightarrow P_{k} \otimes_{A} M$  est alors exact dans  $Ab_{A}$  pour tout k, le  $\partial$ -foncteur

(7.4.I.I)

$$
\mathrm{T} _ {\bullet} (\mathrm{M}) = \mathrm{H} _ {\bullet} (\mathrm{P} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{M})\tag{185}
$$

est un foncteur homologique de  $Ab_{A}$  dans Ab, évidemment A-linéaire lorsque A est commutatif (7.1.2), et commutant aux limites inductives.

Si A est commutatif, alors, pour toute A-algèbre B, le foncteur homologique  $T_{\bullet}^{(B)}$  (7.3.8) est donné par définition par

$$
\mathrm{T} _ {\bullet} ^ {(\mathrm{B})} (\mathrm{N}) = \mathrm{H} _ {\bullet} \left(\mathrm{P} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{N} _ {[ \rho ]}\right)\tag{7.4.1.2}
$$

où $\rho : \mathbf{A} \to \mathbf{B}$ est l'homomorphisme définissant la structure d'algèbre de B; comme on peut aussi écrire $\mathbf{P}_{\bullet} \otimes_{\mathbf{A}} \mathbf{N}_{[\rho]} = \mathbf{P}_{\bullet} \otimes_{\mathbf{A}} (\mathbf{B} \otimes_{\mathbf{B}} \mathbf{N})_{[\rho]} = (\mathbf{P}_{\bullet} \otimes_{\mathbf{A}} \mathbf{B}) \otimes_{\mathbf{B}} \mathbf{N}$, on voit que l'on a

$$
\mathbf {T} _ {\bullet} ^ {(B)} (\mathbf {N}) = \mathbf {H} _ {\bullet} (\mathbf {P} _ {\bullet} ^ {\prime} \otimes_ {B} \mathbf {N})\tag{7.4.1.3}
$$

pour tout B-module N, P' étant le complexe P$_{\bullet}$⊗A B de B-modules plats (0$_{I}$, 6.2.1). Proposition (7.4.2). — Sous les conditions générales de (7.4.1), et pour un entier p∈Z donné, les propriétés suivantes sont équivalentes :

a)  $T_{p}$  est exact à gauche (ou, ce qui revient au même,  $T_{p+1}$  est exact à droite).

b)  $\mathrm{Z}_{p}^{\prime}(\mathbf{P}_{\bullet})=\mathrm{Coker}(\mathbf{P}_{p+1}\rightarrow\mathbf{P}_{p})$  est un A-module à droite plat.

c) Il existe un complexe $\mathbf{P}'$. de A-modules à droite plats tel que la différentielle

$$
d _ {p + 1}: \mathbf {P} _ {p + 1} ^ {\prime} \rightarrow \mathbf {P} _ {p} ^ {\prime}
$$

soit nulle, et un isomorphisme de foncteurs homologiques de $\mathbf{H}_{\bullet}(\mathbf{P}_{\bullet}\otimes_{\mathrm{A}}\mathbf{M})$ sur $\mathbf{H}_{\bullet}(\mathbf{P}_{\bullet}^{\prime}\otimes_{\mathrm{A}}\mathbf{M})$.

Par définition, on a une suite exacte fonctorielle en M

$$
\mathrm{o} \rightarrow \mathrm{T} _ {p} (\mathbf {M}) \rightarrow \mathrm{Z} _ {p} ^ {\prime} (\mathrm{P} _ {\bullet} \otimes \mathbf {M}) \rightarrow \mathrm{P} _ {p - 1} \otimes \mathbf {M}
$$

où  $Z_{p}^{\prime}(\mathbf{P}_{\bullet}\otimes\mathbf{M})=\operatorname{Coker}(\mathbf{P}_{p+1}\otimes\mathbf{M}\to\mathbf{P}_{p}\otimes\mathbf{M})=Z_{p}^{\prime}(\mathbf{P}_{\bullet})\otimes\mathbf{M}$  en vertu de l'exactitude à droite du produit tensoriel. Pour tout homomorphisme  $f:\mathbf{M}\to\mathbf{N}$ , on a donc un diagramme commutatif

$$
\begin{array}{c c c} \mathrm{o} \to \mathrm{T} _ {p} (\mathrm{M}) & \longrightarrow & Z _ {p} ^ {\prime} (\mathrm{P} _ {\bullet}) \otimes \mathrm{M} \to \mathrm{P} _ {p - 1} \otimes \mathrm{M} \\ \Bigg \downarrow_ {u} & & \Bigg \downarrow_ {v} \\ \mathrm{o} \to \mathrm{T} _ {p} (\mathrm{N}) & \longrightarrow & Z _ {p} ^ {\prime} (\mathrm{P} _ {\bullet}) \otimes \mathrm{N} \to \mathrm{P} _ {p - 1} \otimes \mathrm{N} \end{array}\tag{7.4.2.1}
$$

dont les lignes sont exactes. Si $f$ est un monomorphisme, il en est de même de $w$ puisque $\mathbf{P}_{p-1}$ est plat; si $\mathrm{T}_{p}$ est exact à gauche, $u$ est lui aussi un monomorphisme; on en conclut que $v$ est un monomorphisme, ce qui entraîne que $\mathrm{Z}_{p}^{\prime}(\mathbf{P}_{\bullet})$ est plat. Inversement, s'il en est ainsi, $v$ est un monomorphisme pour tout monomorphisme $f: \mathbf{M} \to \mathbf{N}$, donc le diagramme (7.4.2.1) montre que $u$ est un monomorphisme, et par suite $\mathrm{T}_{p}$ (qui est déjà semi-exact) est exact à gauche. Ainsi $a)$ et $b)$ sont équivalentes. Il est immédiat que $c)$ entraîne $a)$, car si $d_{p+1}: \mathbf{P}_{p+1} \to \mathbf{P}_{p}$ est nulle, et $o \to \mathbf{M}' \to \mathbf{M} \to \mathbf{M}'' \to o$ est une suite exacte de A-modules, l'opérateur bord dans la suite exacte

$$
\mathbf {H} _ {p + 1} (\mathbf {P _ {\bullet}} \otimes \mathbf {M ^ {\prime \prime}}) \xrightarrow {\partial} \mathbf {H} _ {p} (\mathbf {P _ {\bullet}} \otimes \mathbf {M ^ {\prime}}) \to \mathbf {H} _ {p} (\mathbf {P _ {\bullet}} \otimes \mathbf {M})
$$

186

est nul par définition (M, IV, 1), donc $\mathbf{T}_p$ est exact à gauche. Montrons inversement que $b)$ implique $c)$. Si $\mathrm{Z}_{p+1}(\mathrm{P}_{\bullet}) = \mathrm{Ker}(\mathrm{P}_{p+1} \to \mathrm{P}_{p})$, on a une suite exacte

$$
\mathrm{o} \rightarrow \mathrm{Z} _ {p + 1} (\mathrm{P} _ {\bullet}) \rightarrow \mathrm{P} _ {p + 1} \rightarrow \mathrm{Z} _ {p} ^ {\prime} (\mathrm{P} _ {\bullet}) \rightarrow \mathrm{o}
$$

dans laquelle $\mathbf{P}_{p+1}$ et $Z_p'(\mathbf{P}_{\bullet})$ sont plats, donc $Z_{p+1}(\mathbf{P}_{\bullet})$ est plat $(\mathbf{0}_{\mathrm{I}}, 6.1.2)$. On va prendre

$$
\mathrm{P} _ {i} ^ {\prime} = \mathrm{P} _ {i} \quad \text {pour} \quad i \neq p \quad \text {et} \quad i \neq p + 1, \quad \mathrm{P} _ {p} ^ {\prime} = Z _ {p} ^ {\prime} (\mathrm{P} _ {\bullet}) \quad \text {et} \quad \mathrm{P} _ {p + 1} ^ {\prime} = Z _ {p + 1} (\mathrm{P} _ {\bullet});
$$

pour différentielle $d_i': \mathrm{P}_i' \to \mathrm{P}_{i-1}'$, on prendra celle du complexe $\mathbf{P}_\bullet$ pour $i \neq p$ et $i \neq p + 1$, o pour $i = p + 1$ et pour $i = p$ l'homomorphisme $Z_p'(P_\bullet) \to P_{p-1}$ déduit de $d_p$ par passage au quotient. Comme les $\mathbf{P}_i$ sont plats, on a

$$
\mathrm{Z} _ {i} ^ {\prime} (\mathrm{P} _ {\bullet} \otimes \mathrm{M}) = \mathrm{Z} _ {i} ^ {\prime} (\mathrm{P} _ {\bullet}) \otimes \mathrm{M}, \quad \mathrm{Z} _ {i} (\mathrm{P} _ {\bullet} \otimes \mathrm{M}) = \mathrm{Z} _ {i} (\mathrm{P} _ {\bullet}) \otimes \mathrm{M} \quad \text { et } \quad \mathrm{B} _ {i} (\mathrm{P} _ {\bullet} \otimes \mathrm{M}) = \mathrm{B} _ {i} (\mathrm{P} _ {\bullet}) \otimes \mathrm{M}
$$

(en posant  $\mathrm{B}_{i}(\mathrm{P}_{\bullet})=\mathrm{Im}(\mathrm{P}_{i+1}\rightarrow\mathrm{P}_{i})$ ); on en conclut aussitôt pour tout M des isomorphismes fonctoriels  $\mathrm{H}_{i}(\mathrm{P}_{\bullet}\otimes\mathrm{M})\stackrel{\sim}{\to}\mathrm{H}_{i}(\mathrm{P}^{\prime}\otimes\mathrm{M})$  pour tout i, et la vérification du fait qu'il s'agit d'un isomorphisme de  $\partial$ -foncteurs découle sans peine de la définition de  $\partial$  (M, IV, r).

On remarquera que les conditions de (7.4.2) impliquent aussi que  $\mathrm{B}_{p}(\mathrm{P}_{\bullet})$  est plat, car on a une suite exacte  $\mathrm{o}\rightarrow\mathrm{B}_{p}(\mathrm{P}_{\bullet})\rightarrow\mathrm{P}_{p}\rightarrow\mathrm{Z}_{p}^{\prime}(\mathrm{P}_{\bullet})\rightarrow\mathrm{o}$ , dans laquelle  $P_{p}$  et  $Z_{p}^{\prime}(\mathrm{P}_{\bullet})$  sont plats  $(\mathbf{0}_{\mathrm{I}},6.\mathrm{I}.2)$ .

Corollaire (7.4.3). — Supposons que A soit un anneau noethérien régulier de dimension 1 (autrement dit un produit d'anneaux de Dedekind (0$_{IV}$, 17.1.3 et 17.3.7), par exemple un anneau principal). Alors, pour que T$_{p}$ soit exact à gauche, il faut et il suffit que T$_{p}$(A) soit un A-module plat. Pour que T$_{p}$ soit exact, il faut et il suffit que T$_{p}$(A) et T$_{p-1}$(A) soient des A-modules plats.

Rappelons que pour un module M sur un anneau de Dedekind, il revient au même de dire que M est plat ou qu'il est sans torsion (0$_{1}$, 6.3.3 et 6.3.4); sous les hypothèses de (7.4.3), tout sous-module d'un A-module plat est donc plat.

La seconde assertion de (7.4.3) résulte de la première, puisque dire que  $T_{p}$  est exact signifie que  $T_{p}$  et  $T_{p-1}$  sont exacts à gauche. Pour démontrer la première assertion, notons que l'on a une suite exacte

$$
\mathrm{o} \rightarrow \mathrm{H} _ {p} (\mathrm{P} _ {\bullet}) \rightarrow \mathrm{Z} _ {p} ^ {\prime} (\mathrm{P} _ {\bullet}) \rightarrow \mathrm{B} _ {p - 1} (\mathrm{P} _ {\bullet}) \rightarrow \mathrm{o}
$$

dans laquelle  $\mathbf{B}_{p-1}(\mathbf{P}_{\bullet})$  est un A-module plat, en tant que sous-module du A-module plat  $P_{p-1}$ . Il est donc équivalent de dire que  $\mathbf{H}_{p}(\mathbf{P}_{\bullet})$  est plat ou que  $\mathbf{Z}_{p}^{\prime}(\mathbf{P}_{\bullet})$  est plat  $(\mathbf{0}_{\mathrm{I}},6,\mathrm{I},2)$ .

Les applications les plus importantes de (7.4.2) sont les suivantes :

Proposition (7.4.4). — Soient A un anneau noethérien, P. un complexe de A-modules plats : on suppose, soit que les  $P_{i}$  sont de type fini, soit que les  $\mathrm{H}_{i}(\mathrm{P}_{\bullet})$  sont des A-modules de type fini et qu'il existe  $i_{0}$  tel que  $\mathrm{H}_{i}(\mathrm{P}_{\bullet})=\mathrm{o}$  pour  $i<i_{0}$ . Soit T le foncteur homologique défini par (7.4.1.1). Alors l'ensemble U des  $y\in\operatorname{Spec}(\mathbf{A})$  tels que  $(\mathrm{T}_{p})_{y}$  (7.1.4) soit exact à droite (resp. exact à gauche, exact) est ouvert dans  $\operatorname{Spec}(\mathbf{A})$ .

Dans la seconde hypothèse sur P., on peut remplacer P. par un complexe P' de

A-modules libres de type fini pour lequel le foncteur  $\mathrm{H}_{\bullet}(\mathrm{P}_{\bullet}^{\prime}\otimes_{\mathrm{A}}\mathrm{M})$  est isomorphe (en tant que  $\partial$ -foncteur) à  $\mathrm{T}_{\bullet}(\mathrm{M})$  (0, 11.9.3). On peut donc toujours se ramener à la première hypothèse et dans ce cas les  $\mathrm{Z}_{i}^{\prime}(\mathrm{P}_{\bullet})$  sont de type fini; en outre, on peut se borner à démontrer les assertions relatives à l'exactitude à gauche (cf. (7.4.2, a))). Cela étant, soit  $x\in U$ ; comme le foncteur  $M\leadsto M_{x}$  est exact, on a  $(\mathrm{Z}_{p}^{\prime}(\mathrm{P}_{\bullet}))_{x}=\mathrm{Z}_{p}^{\prime}((\mathrm{P}_{\bullet})_{x})$ , et (en tenant compte de (7.4.1.3)) l'hypothèse entraîne, en vertu de (7.4.2, b)) que  $(\mathrm{Z}_{p}^{\prime}(\mathrm{P}_{\bullet}))_{x}$  est un  $A_{x}$ -module plat, donc libre puisqu'il est de type fini et que  $A_{x}$  est un anneau local noethérien (Bourbaki, Alg. comm., chap. II, § 3, n° 2, cor. 2 de la prop. 5). On en conclut qu'il y a un  $f\in A$  tel que  $(\mathrm{Z}_{p}^{\prime}(\mathrm{P}_{\bullet}))_{f}$  soit libre sur  $A_{f}$  (Bourbaki, Alg. comm., chap. II, § 5, n° 1, cor. de la prop. 2), et a fortiori  $(\mathrm{Z}_{p}^{\prime}(\mathrm{P}_{\bullet}))_{y}$  est libre sur  $A_{y}$  pour tout  $y\in D(f)$ , ce qui achève la démonstration en vertu de (7.4.2, b)).

Corollaire (7.4.5). — Sous les hypothèses de (7.4.4), supposons en outre que A soit intègre. Alors l'ensemble U des  $x \in \text{Spec}(A)$  tels que  $(\mathbf{T}_{p})_{x}$  soit exact est ouvert non vide.

Il suffit en effet de prouver que  $(\mathbf{T}_{p})_{x}$  est exact pour le point générique x de Spec(A), ce qui est immédiat puisque  $A_{x}$  est un corps, donc tout foncteur additif sur  $Ab_{A_{x}}$  est exact.

Proposition (7.4.6). — Sous les hypothèses générales de (7.4.4), les conditions a), b) et c) de (7.4.2) sont aussi équivalentes à :

d) Il existe un A-module Q et un isomorphisme fonctoriel

$$
\mathrm{T} _ {p} (\mathrm{M}) \stackrel {{\sim}} {{\to}} \operatorname{Hom} _ {\mathrm{A}} (\mathrm{Q}, \mathrm{M}).\tag{7.4.6.1}
$$

En outre, le A-module Q est déterminé à isomorphisme unique près par cette propriété, et il est de type fini.

L'unicité de Q est un cas particulier de l'unicité d'un objet représentatif d'un foncteur représentable (0, 8.1.5). Il est clair que le second membre de (7.4.6.1) est exact à gauche. Inversement, pour démontrer l'existence de Q, lorsque $T_p$ est exact à gauche, on peut d'abord, comme dans (7.4.4), se ramener au cas où les $P_i$ sont plats et de type fini, donc (puisque A est noethérien) projectifs de type fini (Bourbaki, Alg. comm., chap. II, § 5, n° 2, cor. du th. 1). Le dual $\check{P}_i$ de $P_i$ est alors aussi un A-module projectif de type fini, $P_i$ est canoniquement isomorphe au dual de $\check{P}_i$, et l'homomorphisme canonique $P_i \otimes_A M \to \text{Hom}_A(\check{P}_i, M)$ est bijectif (Bourbaki, Alg., chap. II, 3° éd., § 4, n° 2, prop. 2). On sait d'autre part (7.4.2, c)) qu'on peut supposer que $d_{p+1}: P_{p+1} \to P_p$ est nulle, donc que l'on a une suite exacte

$$
\mathrm{o} \rightarrow \mathrm{T} _ {p} (\mathbf {M}) \stackrel {{u}} {{\rightarrow}} \mathrm{P} _ {p} \otimes \mathrm{M} \stackrel {{v}} {{\rightarrow}} \mathrm{P} _ {p - 1} \otimes \mathrm{M}
$$

où  $v=d_{p}\otimes\mathtt{I}$ . Posons alors  $\mathbf{Q}^{\prime}=\mathrm{Ker}(d_{p})$ , de sorte qu'on a la suite exacte  $o\to Q^{\prime}\stackrel{w}{\to}P_{p}\stackrel{dp}{\to}P_{p-1}$ , d'où, par transposition, la suite exacte  $\check{P}_{p-1}\stackrel{t_{d_{p}}}{\longrightarrow}\check{P}_{p}\stackrel{t_{w}}{\to}\check{Q}^{\prime}\to\mathtt{o}$ . Nous allons voir que  $\mathbf{Q}=\check{\mathbf{Q}}^{\prime}=\mathrm{Coker}(^{t}d_{p})$  répond à la question. En effet, on a la suite exacte

$$
\mathrm{o} \rightarrow \operatorname{Hom} (\mathrm{Q}, \mathrm{M}) \rightarrow \operatorname{Hom} \left(\check {\mathrm{P}} _ {p}, \mathrm{M}\right) \xrightarrow {v ^ {\prime}} \operatorname{Hom} \left(\check {\mathrm{P}} _ {p - 1}, \mathrm{M}\right)
$$

où $v' = \text{Hom}(^{t} d_{p}, \mathfrak{i})$; lorsqu'on identifie canoniquement $\mathbf{P}_{i} \otimes \mathbf{M}$ à $\text{Hom}(\check{\mathbf{P}}_{i}, \mathbf{M})$, $v'$ s'identifie donc à $v = d_{p} \otimes \mathfrak{i}$, et l'on a par suite l'isomorphisme fonctoriel $\mathbf{T}_{p}(\mathbf{M}) \xrightarrow{\sim} \text{Hom}_{\mathbb{A}}(\mathbf{Q}, \mathbf{M})$ cherché. En outre, $\mathbf{Q}$, étant un quotient de $\check{\mathbf{P}}_{p}$, est de type fini.

Proposition (7.4.7). — Supposons vérifiées les conditions générales de (7.4.4). Alors, pour tout A-module M de type fini :

(i) Les  $\mathrm{T}_{i}(\mathbf{M})$  sont des A-modules de type fini.

(ii) Pour tout idéal m de A, l'homomorphisme canonique

$$
(\mathbf {T} _ {i} (\mathbf {M})) ^ {\wedge} \rightarrow \varprojlim_ {n} \mathbf {T} _ {i} (\mathbf {M} \otimes_ {\mathrm{A}} (\mathbf {A} / \mathfrak {m} ^ {n + 1}))\tag{7.4.7.1}
$$

(où le premier membre est le séparé complété de  $\mathrm{T}_{i}(\mathbf{M})$  pour la topologie m-préadique) est bijectif. Comme dans (7.4.4), on se ramène d'abord au cas où les  $P_{i}$  sont de type fini; A étant noethérien, les sous-modules des  $P_{i} \otimes_{A} M$  sont de type fini, d'où trivialement l'assertion (i). Quant à l'assertion (ii), elle résulte plus généralement du lemme suivant :

Lemme (7.4.7.2). — Soient A un anneau noethérien,  $u: E \rightarrow F$  un homomorphisme de A-modules de type fini. Pour tout A-module de type fini, posons  $\mathbf{K}(\mathbf{M}) = \operatorname{Ker}(u \otimes \mathrm{I}_{\mathrm{M}})$ ,  $\mathbf{C}(\mathbf{M}) = \operatorname{Coker}(u \otimes \mathrm{I}_{\mathrm{M}})$ ; alors les homomorphismes canoniques

$$
(\mathbf {K} (\mathbf {M})) ^ {\wedge} \rightarrow \varprojlim_ {n} \mathbf {K} (\mathbf {M} _ {n}), \quad (\mathbf {C} (\mathbf {M})) ^ {\wedge} \rightarrow \varprojlim_ {n} \mathbf {C} (\mathbf {M} _ {n})\tag{7.4.7.3}
$$

(où l'on a posé $\mathbf{M}_n = \mathbf{M} \otimes_{\mathrm{A}} (\mathbf{A} / \mathfrak{m}^{n+1}) = \mathbf{M} / \mathfrak{m}^{n+1} \mathbf{M}$) sont bijectifs pour tout idéal m de A.

Comme $\mathbf{E} \otimes \mathbf{M}$ et $\mathbf{F} \otimes \mathbf{M}$ sont de type fini, et que le foncteur $\mathbf{M} \leadsto \hat{\mathbf{M}}$ est exact dans la catégorie des A-modules de type fini ($\mathbf{0}_{\mathrm{I}}, 7.3.3$), $(\mathbf{K}(\mathbf{M}))^{\wedge}$ et $(\mathbf{C}(\mathbf{M}))^{\wedge}$ sont respectivement le noyau et le conoyau de $(u \otimes \mathrm{I})^{\wedge}: (\mathrm{E} \otimes \mathbf{M})^{\wedge} \to (\mathrm{F} \otimes \mathbf{M})^{\wedge}$. L'exactitude à gauche du foncteur $\varprojlim$ montre donc que $(\mathbf{K}(\mathbf{M}))^{\wedge} = \varprojlim \mathbf{K}(\mathbf{M}_n)$; d'autre part, l'exactitude à droite du produit tensoriel prouve que $\mathbf{C}(\mathbf{M}_n) = \mathbf{C}(\mathbf{M}) \otimes_{\mathrm{A}} (\mathrm{A}/\mathrm{m}^{n+1})$, donc $(\mathbf{C}(\mathbf{M}))^{\wedge} = \varprojlim \mathbf{C}(\mathbf{M}_n)$ par définition.

Remarque (7.4.8). — Compte tenu de (6.10.5) et (6.10.6), on voit que, moyennant une hypothèse de platitude supplémentaire, (7.4.7) redonne le fait que (4.1.7.1) est un isomorphisme, c'est-à-dire l'essentiel du « premier théorème de comparaison » pour les morphismes propres; en outre, l'énoncé s'applique non plus seulement à un $\mathcal{O}_{\mathrm{X}}$-Module cohérent, mais à un complexe de tels Modules. Il serait intéressant d'obtenir un énoncé comprenant à la fois (7.4.7) et (4.1.7.1) comme cas particuliers. On notera que lorsque les $\mathbf{P}_i$ sont de type fini, la démonstration de (7.4.7) n'utilise pas le fait que ce sont des modules plats; il y aurait lieu d'examiner si la conclusion de (7.4.7) est encore valable lorsque les $\mathbf{P}_i$ ne sont pas supposés plats ni de type fini, mais que les $\mathrm{H}_i(\mathbf{P}_.)$ sont supposés de type fini pour tout $i$ et nuls pour $i<i_0$. Est-il alors possible de remplacer $\mathbf{P}_.$ par un complexe $\mathbf{P}'$ de A-modules de type fini tel que les foncteurs $\mathrm{H}_.(P_\bullet\otimes M)$ et $\mathrm{H}_.(P'_\otimes M)$ (qui ne sont plus homologiques) soient encore isomorphes?

189

## 7.5. Cas des anneaux locaux noethériens.

(7.5.1) Soient A un anneau local noethérien, m son idéal maximal, et pour tout A-module M, désignons par  $\hat{M}$  son séparé complété pour la topologie m-préadique, isomorphe à  $\varprojlim(\mathbf{M}\otimes_{\mathbb{A}}(\mathbf{A}/\mathfrak{m}^{n+1}))=\varprojlim(\mathbf{M}/\mathfrak{m}^{n+1}\mathbf{M})$ . Soit T un foncteur covariant additif de  $Ab_{A}$  dans Ab; les homomorphismes canoniques (7.2.3.1)

$$
\mathbf {T} (\mathbf {M}) \otimes_ {\mathbf {A}} (\mathbf {A} / \mathfrak {m} ^ {n + 1}) \to \mathbf {T} (\mathbf {M} \otimes_ {\mathbf {A}} (\mathbf {A} / \mathfrak {m} ^ {n + 1}))
$$

forment évidemment un système projectif de A-homomorphismes, qui donnent donc à la limite un Â-homomorphisme fonctoriel en M

$$
(\mathbf {T} (\mathbf {M})) ^ {\wedge} \to \varprojlim_ {n} \mathbf {T} (\mathbf {M} _ {n})\tag{7.5.1.1}
$$

où l'on a posé $\mathbf{M}_n = \mathbf{M} \otimes_{\mathbf{A}} (\mathbf{A} / \mathfrak{m}^{n+1})$, $\mathbf{A}_n = \mathbf{A} / \mathfrak{m}^{n+1}$.

Proposition (7.5.2). — Soient A un anneau local noethérien d'idéal maximal m, k = A/m son corps résiduel, T un foncteur covariant additif de  $Ab_{A}$  dans Ab, semi-exact et commutant aux limites inductives. On suppose en outre que pour tout A-module de type fini M, T(M) est un A-module de type fini et que l'homomorphisme canonique (7.5.1.1) est un isomorphisme. Sous ces conditions, les propriétés suivantes sont équivalentes :

a) T est exact à droite.

b) Pour tout n, le foncteur  $\mathbf{N}\leadsto\mathbf{T}(\mathbf{N})$  est exact à droite dans la catégorie des  $A_{n}$ -modules de type fini (ce qui revient à dire que T est exact à droite dans la catégorie des A-modules de longueur finie).

c) L'homomorphisme canonique T(ε) : T(A) → T(k) est surjectif.

d) Pour tout n assez grand, l'homomorphisme canonique $\mathbf{T}(\mathbf{A}_n)\to\mathbf{T}(k)$ est surjectif.

Il est clair que $a)$ entraîne $b)$. Montrons que $b)$ entraîne $a)$, c'est-à-dire que si $u: \mathbf{M} \to \mathbf{N}$ est un épimorphisme de A-modules, $\mathrm{T}(u)$ est un épimorphisme. Comme T commute aux limites inductives et que le foncteur $\varinjlim$ est exact dans la catégorie des modules (pour des ensembles d'indices filtrants), on peut se borner au cas où M et N sont de type fini. Comme $\mathrm{T(M)}$ et $\mathrm{T(N)}$ sont alors de type fini, et que A est un anneau local noethérien, il suffit de montrer que $(\mathrm{T}(u))^{\wedge}: (\mathrm{T(M)})^{\wedge} \to (\mathrm{T(N)})^{\wedge}$ est surjectif $(\mathbf{0}_{\mathrm{I}}, 7.3.5$ et $\mathbf{0}_{\mathrm{I}}, 6.4.1)$. Par hypothèse, $(\mathrm{T(M)})^{\wedge}$ et $(\mathrm{T(N)})^{\wedge}$ sont respectivement $\varprojlim \mathrm{T(M}_{n})$ et $\varprojlim \mathrm{T(N}_{n})$, donc $(\mathrm{T}(u))^{\wedge}$ est limite du système projectif d'homomorphismes $\overleftarrow{\mathrm{T}}(u \otimes \mathrm{I}_{\mathrm{A}_{n}}): \mathrm{T(M}_{n}) \to \mathrm{T(N}_{n})$. Or, $b)$ signifie que ces homomorphismes sont surjectifs; en outre, $\mathrm{T(M}_{n)}$ est un $\mathrm{A}_{n}$-module de type fini, et $\mathrm{A}_{n}$ est un anneau artinien par hypothèse; on en conclut que $(\mathrm{T}(u))^{\wedge}$ est surjectif $(\mathbf{0}, 13.1.2$ et $13.2.2)$. Il est clair que $a)$ entraîne $c)$, et comme $\mathrm{T}(\varepsilon)$ se factorise en $\mathrm{T(A)} \to \mathrm{T(A}_{n}) \to \mathrm{T}(k)$, $c)$ implique $d)$; enfin, il résulte de (7.2.7) que $b)$ et $d)$ sont équivalentes puisque T est semi-exact dans $Ab_{A_{n}}$, ce qui achève la démonstration.

Corollaire (7.5.3). — Sous les hypothèses générales de (7.5.2), si  $\mathrm{T}(k)=\mathrm{o}$ , alors  $\mathrm{T}(\mathrm{M})=\mathrm{o}$  pour tout A-module M.

Comme $k$ est le seul A-module simple, on déduit de (7.3.5.4) que $\mathrm{T}(\mathrm{E}) = 0$ pour tout A-module de longueur finie E. Si maintenant M est de type fini, $(\mathrm{T}(\mathbf{M}))^{\wedge}$ est isomorphe à $\varprojlim \mathrm{T}(\mathbf{M}_n)$, et comme les $\mathbf{M}_n$ sont de longueur finie, on a $(\mathrm{T}(\mathbf{M}))^{\wedge} = 0$; comme $\mathrm{T}(\mathbf{M})$ est de type fini par hypothèse, il est isomorphe à un sous-module de $(\mathrm{T}(\mathbf{M}))^{\wedge}(\mathbf{0}_1, 7.3.5)$, donc on a $\mathrm{T}(\mathbf{M}) = 0$. Enfin, pour un A-module M quelconque, $\mathrm{T}(\mathbf{M})$ est limite inductive des $\mathrm{T}(\mathrm{N}_{\alpha})$ pour les sous-modules de type fini $\mathbf{N}_{\alpha}$ de M, ce qui achève la démonstration.

Proposition (7.5.4). — Soient A un anneau local noethérien d'idéal maximal m, k = A/m son corps résiduel, T. un foncteur homologique de  $Ab_{A}$  dans Ab, commutant aux limites inductives. On suppose en outre que pour tout i et tout A-module M de type fini,  $T_{i}(M)$  est de type fini et l'homomorphisme canonique  $(\mathrm{T}_{i}(\mathbf{M}))^{\wedge} \to \varprojlim \mathrm{T}_{i}(\mathbf{M}_{n})$  est bijectif. Pour un entier p donné, les conditions suivantes sont alors équivalentes :

a) $\mathbf{T}_p$ est exact.

b) $\mathbf{T}_p$ est exact à droite, et $\mathbf{T}_p(\mathbf{A})$ est un A-module libre.

c) Les homomorphismes canoniques $\mathbf{T}_{p+1}(\mathbf{A})\to\mathbf{T}_{p+1}(k)$ et $\mathbf{T}_{p}(\mathbf{A})\to\mathbf{T}_{p}(k)$ sont surjectifs.
d) Pour tout $n$, les homomorphismes canoniques $\mathbf{T}_{p+1}(\mathbf{A}_{n})\to\mathbf{T}_{p+1}(k)$ et $\mathbf{T}_{p}(\mathbf{A}_{n})\to\mathbf{T}_{p}(k)$ sont surjectifs.

e) Pour tout n, le foncteur  $\mathbf{N}\leadsto\mathbf{T}_{p}(\mathbf{N})$  est exact dans la catégorie des  $A_{n}$ -modules de type fini.

On sait (7.3.3) que $a)$ équivaut à dire que $\mathbf{T}_{p+1}$ et $\mathbf{T}_p$ sont exacts à droite; comme $\mathbf{T}_\cdot$ est un foncteur homologique dans la catégorie $\boldsymbol{Ab}_{\mathrm{A}_n}$, le même raisonnement que dans (7.3.1) montre que $e)$ équivaut à dire que $\mathbf{T}_p$ et $\mathbf{T}_{p+1}$ sont exacts à droite dans la catégorie des $\mathrm{A}_n$-modules de type fini. On déduit donc de (7.5.2) que $a)$ et $e)$ sont équivalentes; l'équivalence de $a)$, $c)$ et $d)$ résulte aussi de (7.5.2). Enfin, on sait que tout A-module plat de type fini est libre (Bourbaki, Alg. comm., chap. II, § 3, n° 2, cor. 2 de la prop. 5); l'équivalence de $a)$ et $b)$ résulte alors de (7.3.1) et (7.3.3).

Corollaire (7.5.5). — Supposons vérifiées les conditions générales de (7.5.4).

(i) Si  $\mathrm{T}_{p}(k)=\mathrm{o}$ , on a  $T_{p}=0$ ,  $T_{p+1}$  est exact à droite et  $T_{p-1}$  est exact à gauche.

(ii) $Si\quad \mathrm{T}_{p - 1}(k) = \mathrm{T}_{p + 1}(k) = \mathrm{o},\quad \mathrm{T}_p$ est exact, l'homomorphisme canonique

$$
\mathbf {T} _ {p} (\mathbf {A}) \otimes_ {\mathbf {A}} \mathbf {M} \rightarrow \mathbf {T} _ {p} (\mathbf {M})
$$

est bijectif et $\mathbf{T}_p(\mathbf{A})$ est un A-module libre.

(i) découle aussitôt de (7.5.3) puisque  $T_{p}$  est semi-exact, la dernière assertion résultant de la définition d'un foncteur homologique. On conclut aussitôt de (i) les deux premières assertions de (ii), compte tenu de (7.3.3); le fait que  $\mathrm{T}_{p}(\mathrm{A})$  soit libre résulte de (7.5.4).

Corollaire (7.5.6). — Supposons vérifiées les hypothèses générales de (7.5.4), et supposons de plus que A soit un anneau de valuation discrète.

(i) Pour que $\mathbf{T}_p$ soit exact à droite, il faut et il suffit que $\mathbf{T}_{p-1}(\mathbf{A})$ soit un A-module libre.

(ii) Pour que $\mathbf{T}_p$ soit exact, il faut et il suffit que $\mathbf{T}_p(\mathbf{A})$ et $\mathbf{T}_{p-1}(\mathbf{A})$ soient des A-modules libres.

Il est clair que (i) implique (ii) (cf. (7.3.3)). Pour prouver (i), remarquons que si $f$ est un générateur de l'idéal maximal de A (« uniformisante » de A), pour qu'un A-module de type fini M soit libre (ou plat, ce qui revient au même), il faut et il suffit que l'homothétie $h_f: x \to fx$ de M soit injective, car cela équivaut ici à dire que M est sans torsion ($\mathbf{0}_1$, 6.3.4). Considérons alors la suite exacte $o \to A \xrightarrow{h_f} A \to k \to o$, qui fournit la suite exacte d'homologie

$$
\mathbf {T} _ {p} (\mathbf {A}) \rightarrow \mathbf {T} _ {p} (k) \rightarrow \mathbf {T} _ {p - 1} (\mathbf {A}) \xrightarrow {h _ {f}} \mathbf {T} _ {p - 1} (\mathbf {A})
$$

On voit que  $\mathbf{T}_{p-1}(\mathbf{A})$  est libre si et seulement si  $\mathbf{T}_{p}(\mathbf{A})\to\mathbf{T}_{p}(k)$  est surjectif; la conclusion résulte alors de (7.5.2).

Remarque (7.5.7). — On notera que, en vertu de (7.4.7), les hypothèses générales de (7.4.4) entraînent que le foncteur homologique T. défini par (7.4.1.1) satisfait aux hypothèses générales de (7.5.4). Dans ce cas, (7.5.6) est donc contenu dans (7.4.3).

## 7.6. Descente des propriétés d'exactitude. Théorème de semi-continuité et critère d'exactitude de Grauert.

Proposition (7.6.1). — Sous les conditions de (7.4.1), soit B une A-algèbre commutative. Si  $T_{p}$  est exact à droite (resp. exact à gauche, exact) il en est de même de  $\mathrm{T}_{p}^{\mathrm{(B)}}$ ; la réciproque est vraie lorsque B est un A-module fidèlement plat.

La première assertion est un cas particulier d'une assertion triviale de (7.1.3). Inversement, supposons d'abord que B soit un A-module plat. On a alors, pour tout A-module M,  $\mathrm{H}_{\bullet}(\mathrm{P}_{\bullet}\otimes_{\mathrm{A}}(\mathrm{M}\otimes_{\mathrm{A}}\mathrm{B}))=(\mathrm{H}_{\bullet}(\mathrm{P}_{\bullet}\otimes_{\mathrm{A}}\mathrm{M}))\otimes_{\mathrm{A}}\mathrm{B}$ , ce qui s'écrit aussi, pour tout p,

$$
\mathbf {T} _ {p} (\mathbf {M}) \otimes_ {\mathrm{A}} \mathbf {B} = \mathbf {T} _ {p} ^ {(\mathrm{B})} (\mathbf {M} _ {(\mathrm{B})})\tag{7.6.x.x}
$$

à un isomorphisme canonique près. Supposons  $\mathbf{T}_{p}^{(\mathrm{B})}$  exact à droite (resp. exact à gauche, exact); comme  $\mathbf{M}\leadsto\mathbf{M}_{(\mathrm{B})}$  est un foncteur exact, le premier membre de (7.6.1.1) est un foncteur exact à droite (resp. exact à gauche, exact) en M; si maintenant B est fidèlement plat sur A, on en déduit que  $T_{p}$  a la même propriété d'exactitude ( $0_{I}$ , 6.4.1).

Proposition (7.6.2). — Sous les conditions de (7.4.1), on suppose en outre que A soit un anneau noethérien réduit et que les  $P_{i}$  soient des A-modules de type fini. Pour que  $T_{p}$  soit exact à droite (resp. exact à gauche, exact), il faut et il suffit que, pour toute A-algèbre B qui est un anneau de valuation discrète,  $T_{p}^{(B)}$  le soit.

En vertu de (7.3.1) et (7.3.3), on peut se borner à considérer l'exactitude à droite, et il n'y a naturellement qu'à prouver la suffisance de la condition (7.6.1). En vertu de (7.4.2), il suffit de montrer que  $Z_{p-1}^{\prime}(\mathbf{P}_{\bullet})$  est un A-module plat; comme  $P_{p-1}$  est de type fini,  $Z_{p-1}^{\prime}(\mathbf{P}_{\bullet})$  est aussi de type fini; le critère (0, 10.2.8) montre qu'il suffit alors que  $Z_{p-1}^{\prime}(\mathbf{P}_{\bullet}) \otimes_{\mathrm{A}} \mathbf{B}$  soit un B-module plat pour toute A-algèbre B qui est un anneau de valuation discrète. Or, comme P. est un complexe de A-modules plats, on a

$$
\mathrm{Z} _ {p - 1} ^ {\prime} (\mathbf {P} _ {\bullet}) \otimes_ {\mathrm{A}} \mathrm{B} = \mathrm{Z} _ {p - 1} ^ {\prime} (\mathbf {P} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{B});
$$

$P_{\bullet}\otimes_{A}B$ est un complexe de B-modules plats $(\mathbf{0}_{I},6.2.I)$, et pour tout B-module N, on a $H_{\bullet}(P_{\bullet}\otimes_{A}N)=H_{\bullet}((P_{\bullet}\otimes_{A}B)\otimes_{B}N)$, donc $T_{p}^{(B)}(N)=H_{p}((P_{\bullet}\otimes_{A}B)\otimes_{B}N)$; appliquant (7.4.2) à $T_{p}^{(B)}$, on voit que l'hypothèse que $T_{p}^{(B)}$ est exact à droite est équivalente au fait que $Z_{p-1}'(P_{\bullet}\otimes_{A}B)$ est un B-module plat.

Le critère précédent amène à étudier de plus près le cas des anneaux de valuation discrète :

Proposition (7.6.3). — Sous les conditions de (7.4.1), supposons que A soit un anneau noethérien régulier de dimension 1 (autrement dit, que A est noethérien et que, pour tout $x \in \text{Spec}(A)$, $A_x$ est un corps ou un anneau de valuation discrète). Alors, pour tout entier $p$ et tout A-module M, on a une suite exacte canonique fonctorielle en M

$$
\mathbf {o} \to \mathbf {T} _ {p} (\mathbf {A}) \otimes_ {\mathbf {A}} \mathbf {M} \xrightarrow {t _ {\mathrm{M}}} \mathbf {T} _ {p} (\mathbf {M}) \to \mathbf {T o r} _ {1} ^ {\mathbf {A}} (\mathbf {T} _ {p - 1} (\mathbf {A}), \mathbf {M}) \to \mathbf {o}.\tag{7.6.3.1}
$$

Dans ce qui suit, nous supprimerons pour simplifier la mention du complexe P. dans les notations homologiques usuelles  $\mathrm{H}_{p}(\mathrm{P}_{\bullet})$ ,  $\mathrm{B}_{p}(\mathrm{P}_{\bullet})$ ,  $\mathrm{Z}_{p}(\mathrm{P}_{\bullet})$  et  $\mathrm{Z}_{p}^{\prime}(\mathrm{P}_{\bullet})$ . On a les trois suites exactes

$$
\begin{array}{r l}&{\mathrm{o} \rightarrow \mathrm{H} _ {p} \rightarrow \mathrm{Z} _ {p} ^ {\prime} \rightarrow \mathrm{B} _ {p - 1} \rightarrow \mathrm{o}}\\&{\mathrm{o} \rightarrow \mathrm{B} _ {p - 1} \rightarrow \mathrm{Z} _ {p - 1} \rightarrow \mathrm{H} _ {p - 1} \rightarrow \mathrm{o}}\\&{\mathrm{o} \rightarrow \mathrm{Z} _ {p - 1} \rightarrow \mathrm{P} _ {p - 1} \rightarrow \mathrm{B} _ {p - 2} \rightarrow \mathrm{o}}\end{array}
$$

Comme  $P_{p-1}$  et  $P_{p-2}$  sont plats, il en est de même de leurs sous-modules respectifs  $B_{p-1}$,  $Z_{p-1}$  et  $B_{p-2}$  puisqu'il y a identité entre  $A_{x}$-modules plats et  $A_{x}$-modules sans torsion (pour tout  $x \in \text{Spec}(A)$); par tensorisation avec M, on a donc les suites exactes

(7.6.3.2)

$$
\mathrm{o} = \operatorname{Tor} _ {1} ^ {\mathrm{A}} (\mathrm{B} _ {p - 1}, \mathrm{M}) \rightarrow \mathrm{H} _ {p} \otimes \mathrm{M} \rightarrow \mathrm{Z} _ {p} ^ {\prime} \otimes \mathrm{M} \stackrel {u} {\rightarrow} \mathrm{B} _ {p - 1} \otimes \mathrm{M} \rightarrow \mathrm{o}\tag{7.6.3.3}
$$

$$
\mathrm{o} = \operatorname{Tor} _ {1} ^ {\mathrm{A}} (\mathrm{Z} _ {p - 1}, \mathrm{M}) \rightarrow \operatorname{Tor} _ {1} ^ {\mathrm{A}} (\mathrm{H} _ {p - 1}, \mathrm{M}) \rightarrow \mathrm{B} _ {p - 1} \otimes \mathrm{M} \stackrel {v} {\rightarrow} \mathrm{Z} _ {p - 1} \otimes \mathrm{M}\tag{7.6.3.4}
$$

$$
\mathrm{o} = \operatorname{Tor} _ {1} ^ {\mathrm{A}} (\mathrm{B} _ {p - 2}, \mathrm{M}) \rightarrow \mathrm{Z} _ {p - 1} \otimes \mathrm{M} \stackrel {{w}} {{\rightarrow}} \mathrm{P} _ {p - 1} \otimes \mathrm{M}.
$$

Par définition,  $\mathrm{T}_{p}(\mathbf{M})=\mathrm{Ker}(d_{p}\otimes\mathbf{i})/\mathrm{Im}(d_{p+1}\otimes\mathbf{i})$ ; c'est donc le noyau de l'homomorphisme  $(\mathrm{P}_{p}\otimes\mathrm{M})/\mathrm{Im}(d_{p+1}\otimes\mathbf{i})\to\mathrm{P}_{p-1}\otimes\mathrm{M}$  obtenu à partir de  $d_{p}\otimes\mathbf{i}$  par passage au quotient, homomorphisme qui s'écrit aussi  $Z_{p}^{\prime}\otimes M\to P_{p-1}\otimes M$  par définition de  $Z_{p}^{\prime}=P_{p}/B_{p}$ ; or, cet homomorphisme peut être considéré comme le composé

$$
\mathrm{Z} _ {p} ^ {\prime} \otimes \mathrm{M} \xrightarrow {u} \mathrm{B} _ {p - 1} \otimes \mathrm{M} \xrightarrow {v} \mathrm{Z} _ {p - 1} \otimes \mathrm{M} \xrightarrow {w} \mathrm{P} _ {p - 1} \otimes \mathrm{M}.
$$

Comme w est injectif d'après (7.6.3.4), on a une suite exacte

$$
\mathrm{o} \rightarrow \operatorname{Ker} u \rightarrow \mathrm{T} _ {p} (\mathbf {M}) \rightarrow \operatorname{Ker} v \rightarrow \mathrm{o},
$$

qui n'est autre que (7.6.3.1), compte tenu de (7.6.3.2) et (7.6.3.3) et de ce que $\mathbf{H}_p = \mathbf{T}_p(\mathbf{A})$ par définition.

Remarques (7.6.4). — (i)  $\mathrm{H}_{\bullet}(\mathrm{P}_{\bullet}\otimes_{\mathrm{A}}\mathrm{M})$  est l'homologie du bicomplexe  $P_{\bullet}\otimes_{A}M$ , où M est considéré comme un complexe réduit à son terme de degré o; elle est par suite (6.3.6 et 6.3.2) l'aboutissement de la suite spectrale régulière dont le terme  $E_{2}$  est

$$
\mathrm{E} _ {p q} ^ {2} = \operatorname{Tor} _ {q} ^ {\mathrm{A}} (\mathrm{H} _ {q} (\mathrm{P} _ {\bullet}), \mathrm{M}) = \operatorname{Tor} _ {p} ^ {\mathrm{A}} (\mathrm{T} _ {q} (\mathrm{A}), \mathrm{M}).\tag{193}
$$

Or, l'hypothèse sur l'anneau A entraîne que $\operatorname{Tor}_{p}^{\mathrm{A}}(\mathrm{E},\mathrm{F}) = 0$ pour $p \geqslant 2$ et pour des A-modules quelconques $(\mathbf{0}_{\mathrm{IV}},17.2.2)$; on sait (M, XV) que cela entraîne l'exactitude de la suite

$$
\mathrm{o} \rightarrow \mathrm{E} _ {0, q} ^ {2} \rightarrow \mathrm{H} _ {q} (\mathrm{P} _ {\bullet} \otimes_ {\mathrm{A}} \mathrm{M}) \rightarrow \mathrm{E} _ {1, q - 1} ^ {2} \rightarrow \mathrm{o}
$$

qui n'est autre que (7.6.3.1).

(ii) Compte tenu de (7.3.1), la suite exacte (7.6.3.1) redonne comme cas particulier le résultat de (7.4.3).

Corollaire (7.6.5). — Sous les conditions de (7.4.1), supposons que A soit un anneau de valuation discrète, de corps des fractions K, de corps résiduel k, et que les  $T_{i}(A)$  soient des A-modules de type fini. On a alors

$$
\operatorname{rang} _ {k} \mathrm{T} _ {p} (k) \geqslant \operatorname{rang} _ {k} (\mathrm{T} _ {p} (\mathrm{A}) \otimes_ {\mathrm{A}} k) \geqslant \operatorname{rang} _ {\mathrm{A}} \mathrm{T} _ {p} (\mathrm{A}) = \operatorname{rang} _ {\mathrm{K}} \mathrm{T} _ {p} (\mathrm{K}). \tag {7.6.5.i}
$$

En outre, pour que les termes extrêmes de cette inégalité soient égaux, il faut et il suffit que  $T_{p}$  soit exact, ou encore que  $\mathrm{T}_{p}(\mathrm{A})$  et  $\mathrm{T}_{p-1}(\mathrm{A})$  soient des A-modules libres.

Faisons en effet M=k dans la suite exacte (7.6.3.1); il vient, puisqu'il s'agit d'espaces vectoriels sur k

$$
\operatorname{rang} _ {k} \mathrm{T} _ {p} (k) = \operatorname{rang} _ {k} (\mathrm{T} _ {p} (\mathrm{A}) \otimes_ {\mathrm{A}} k) + \operatorname{rang} _ {k} (\operatorname{Tor} _ {1} ^ {\mathrm{A}} (\mathrm{T} _ {p - 1} (\mathrm{A}), k)).
$$

D'autre part, comme  $T_{p}(A)$  est un module de type fini sur l'anneau local intègre A, on a (Bourbaki, Alg. comm., chap. II, § 3, n° 2, cor. 1 de la prop. 4)

$$
\operatorname{rang} _ {k} \left(\mathrm{T} _ {p} (\mathrm{A}) \otimes_ {\mathrm{A}} k\right) \geqslant \operatorname{rang} _ {\mathrm{A}} \mathrm{T} _ {p} (\mathrm{A}) = \operatorname{rang} _ {\mathrm{K}} \left(\mathrm{T} _ {p} (\mathrm{A}) \otimes_ {\mathrm{A}} \mathrm{K}\right)\tag{7.6.5.2}
$$

et en outre les deux membres de (7.6.5.2) sont égaux si et seulement si  $\mathrm{T}_{p}(\mathrm{A})$  est un A-module libre (loc. cit., prop. 7). On notera d'ailleurs que puisque K est un A-module plat, on a par définition  $\mathrm{T}_{p}(\mathrm{A})\otimes_{\mathrm{A}}\mathrm{K}=\mathrm{H}_{p}(\mathrm{P}_{\bullet})\otimes_{\mathrm{A}}\mathrm{K}=\mathrm{H}_{p}(\mathrm{P}_{\bullet}\otimes_{\mathrm{A}}\mathrm{K})=\mathrm{T}_{p}(\mathrm{K})$ . On a donc bien l'inégalité (7.6.5.1) et on voit en outre que l'égalité n'est possible que si:  $1^{0}\mathrm{T}_{p}(\mathrm{A})$  est libre;  $2^{0}\mathrm{Tor}_{1}^{\mathrm{A}}(\mathrm{T}_{p-1}(\mathrm{A}), k)=0$ , condition qui équivaut, comme on sait (0, 10.1.3), au fait que  $\mathrm{T}_{p-1}(\mathrm{A})$  est un A-module libre. Enfin, comme les  $\mathrm{T}_{i}(\mathrm{A})$  sont des A-modules de type fini, il revient au même de dire qu'ils sont plats ou libres (Bourbaki, Alg. comm., chap. II, § 3, n° 2, cor. 2 de la prop. 5), et on conclut par (7.4.3).

(7.6.6) Les hypothèses étant toujours celles de (7.4.1), nous poserons, pour tout  $x \in \text{Spec}(A)$

$$
d _ {p} (x) = d _ {p} ^ {\mathrm{T}} (x) = \operatorname{rang} _ {\mathbf {k} (x)} \mathrm{T} _ {p} (\boldsymbol {k} (x)).\tag{7.6.6.1}
$$

Lemme (7.6.7). — Soit $\varphi : A \to A'$ un homomorphisme d'anneaux, et soit

$$
f = ^ {a} \varphi : \operatorname{Spec} (\mathrm{A} ^ {\prime}) \rightarrow \operatorname{Spec} (\mathrm{A})
$$

l'application correspondante (I, 1.2.1). Si l'on pose $\mathrm{T}_{\bullet}^{\prime} = \mathrm{T}_{\bullet}^{(\mathrm{A}^{\prime})}$ (7.1.3), on a

(7.6.7.1)

194

$$
d _ {p} ^ {\mathrm{T} ^ {\prime}} = d _ {p} ^ {\mathrm{T}} \circ f.
$$

(7.6.10.2)

En effet, pour tout $x' \in \operatorname{Spec}(\mathbf{A}')$, on $a$, en posant $x = f(x')$,

$$
\mathrm{H} _ {\bullet} \left(\mathrm{P} _ {\bullet} \otimes_ {\mathrm{A}} \boldsymbol {k} \left(x ^ {\prime}\right)\right) = \mathrm{H} _ {\bullet} \left(\left(\mathrm{P} _ {\bullet} \otimes_ {\mathrm{A}} \boldsymbol {k} (x)\right) \otimes_ {\mathbf {k} (x)} \boldsymbol {k} \left(x ^ {\prime}\right)\right) = \mathrm{H} _ {\bullet} \left(\mathrm{P} _ {\bullet} \otimes_ {\mathrm{A}} \boldsymbol {k} (x)\right) \otimes_ {\mathbf {k} (x)} \boldsymbol {k} \left(x ^ {\prime}\right),
$$

puisque  $\boldsymbol{k}(x')$  est plat sur  $\boldsymbol{k}(x)$ , d'où la relation (7.6.7.1).

Lemme (7.6.8). — Si l'anneau A est noethérien et le complexe P. formé de A-modules de type fini, la fonction  $x \mapsto d_{p}^{\mathrm{T}}(x)$  sur Spec(A) est constructible.

Il faut prouver que pour toute partie fermée irréductible Y de X=Spec(A), il existe un ouvert non vide U de Y dans lequel  $d_{p}$  est constante (0, 9.2.2); comme Y=Spec(A/a), où a est un idéal de A tel que A/a soit réduit, on peut, en vertu de (7.6.7), se borner au cas où Y=X et où A est un anneau noethérien intègre; mais alors l'assertion résulte de (7.4.5).

Théorème (7.6.9). — Soient A un anneau noethérien, P. un complexe de A-modules plats de type fini, T.(M)=H.(P.⊗A M) le foncteur homologique défini par P.; pour tout x∈Spec(A), soit $d_{p}(x)=\text{rang}_{\mathbf{k}(x)}\text{T}_{p}(\boldsymbol{k}(x))$. Alors :

(i) La fonction $d_p$ est constructible et semi-continue supérieurement dans $\operatorname{Spec}(A)$.

(ii) Si  $T_{p}$  est exact,  $d_{p}$  est continue (donc localement constante) dans Spec(A); la réciproque est vraie lorsque l'anneau A est réduit.

(i) La première assertion a été démontrée dans (7.6.8). Pour prouver la seconde, il suffit donc (0, 9.2.4) de montrer que si $x' \neq x$ est une générisation de $x$ dans $\operatorname{Spec}(A)$, on a $d_p(x') \leqslant d_p(x)$. Or, il existe alors un anneau de valuation discrète B et un morphisme $f: \operatorname{Spec}(B) \to \operatorname{Spec}(A)$ tels que, si $a$ désigne le point fermé de $\operatorname{Spec}(B)$ et $b$ son point générique, on ait $f(a) = x$ et $f(b) = y$ (II, 7.1.9). En vertu de la formule (7.6.7.1), on voit qu'on est ramené à démontrer l'inégalité $d_p(a) \geqslant d_p(b)$ dans $\operatorname{Spec}(B)$; mais cela n'est autre que l'inégalité (7.6.5.1) (1).

(ii) La première assertion a déjà été démontrée (7.3.4). Pour démontrer la réciproque, utilisons le critère valuatif (7.6.2); compte tenu de la formule (7.6.7.1), on est donc ramené au cas où A est un anneau de valuation discrète; mais comme Spec(A) ne comporte alors que deux points, l'hypothèse que $d_p$ est constante implique bien que $T_p$ est exact, en vertu de (7.6.5).

Corollaire (7.6.10). — Soient A un anneau noethérien,  $p_{i}$  ( $i \leqslant i \leqslant r$ ) ses idéaux premiers minimaux,  $k_{i}$  le corps résiduel de  $A_{p_{i}}$  ( $i \leqslant i \leqslant r$ ).

(i) Pour tout $x \in \operatorname{Spec}(\mathbf{A})$, il existe un indice $i$ tel que

$$
d _ {p} (x) \geqslant \operatorname{rang} _ {k _ {i}} \mathrm{T} _ {p} (k _ {i}).\tag{7.6.10.1}
$$

En particulier, si A est intègre et si K est son corps des fractions, on a

$$
d _ {p} (x) \geqslant \operatorname{rang} _ {\mathrm{K}} \mathrm{T} _ {p} (\mathrm{K})
$$

pour tout  $x \in \text{Spec}(A)$ .

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Le principe de démonstration de (i) par réduction au cas d'un anneau de valuation discrète nous a été communiqué oralement par Hironaka.</span></small>

(ii) Supposons en outre que A soit local et réduit, et soit k son corps résiduel. Alors, pour que  $T_{p}$  soit exact, il faut et il suffit que l'on ait

$$
\operatorname{rang} _ {k} \mathrm{T} _ {p} (k) = \operatorname{rang} _ {k _ {i}} \mathrm{T} _ {p} (k _ {i})\tag{7.6.10.3}
$$

$$
\text { pour } \quad \mathrm{I} \leqslant i \leqslant r.
$$

(i) est immédiat puisque tout voisinage de $x$ contient un des $p_i$, et il suffit d'appliquer la définition de la semi-continuité. D'autre part, si A est local, le seul voisinage dans $\text{Spec(A)}$ de l'idéal maximal $m$ est $\text{Spec(A)}$ tout entier, donc on a $d_p(x) \leqslant \text{rang}_k T_p(k)$ pour tout $x \in \text{Spec(A)}$; cette relation, jointe à (i), montre que la condition (7.6.10.3) entraîne que $d_p(x)$ est constante dans $\text{Spec(A)}$, et par suite que $T_p$ est exact en vertu de (7.6.9, (ii)); la réciproque est évidente en vertu de (7.6.9, (ii)).

Remarque (7.6.11). — On peut se demander si l'assertion de (7.6.9, (i)) ne peut être renforcée par l'inégalité

$$
\operatorname{rang} _ {\mathbf {k} (x)} \mathrm{T} _ {p} (\boldsymbol {k} (x)) \geqslant \operatorname{rang} _ {\mathbf {k} (x)} \left(\mathrm{T} _ {p} (\mathrm{A}) \otimes_ {\mathrm{A}} \boldsymbol {k} (x)\right)\tag{7.6.11.1}
$$

pour tout $x \in \text{Spec}(A)$, qui a lieu effectivement lorsque A est un anneau de valuation discrète et $x$ son idéal maximal (7.6.5). Bornons-nous au cas où A est un anneau local noethérien, d'idéal maximal m et de corps résiduel k. Alors, les conditions suivantes sont équivalentes :

a) Pour tout complexe P. de A-modules plats de type fini, on a

$$
\operatorname{rang} _ {k} \left(\mathrm{T} _ {p} (k)\right) \geqslant \operatorname{rang} _ {k} \left(\mathrm{T} _ {p} (\mathrm{A}) \otimes_ {\mathrm{A}} k\right)\tag{7.6.11.2}
$$

pour tout entier p.

b) Pour tout A-module M de type fini, on a

$$
\operatorname{rang} _ {k} (\mathbf {M} \otimes_ {\mathrm{A}} k) \geqslant \operatorname{rang} _ {k} (\check {\mathbf {M}} \otimes_ {\mathrm{A}} k).\tag{7.6.11.3}
$$

c) Pour tout A-module N de type fini, on a

$$
\operatorname{rang} _ {k} \left(\operatorname{Tor} _ {1} ^ {\mathrm{A}} (\mathrm{N}, k)\right) \geqslant \operatorname{rang} _ {k} \left(\operatorname{Tor} _ {2} ^ {\mathrm{A}} (\mathrm{N}, k)\right).\tag{7.6.11.4}
$$

On notera qu'il revient au même, par décalage (M, V, 7.2), de dire que l'on a, pour tout $i \geqslant 1$

$$
\operatorname{rang} _ {k} \left(\operatorname{Tor} _ {i} ^ {\mathrm{A}} (\mathrm{N}, k)\right) \geqslant \operatorname{rang} _ {k} \left(\operatorname{Tor} _ {i + 1} ^ {\mathrm{A}} (\mathrm{N}, k)\right).\tag{7.6.11.5}
$$

Donnons rapidement quelques indications sur la démonstration. Pour voir que $a)$ entraîne $b)$, on considère une suite exacte $\mathbf{L}_1 \xrightarrow{d} \mathbf{L}_0 \to \mathbf{M} \to 0$ où $\mathbf{L}_0$ et $\mathbf{L}_1$ sont libres de type fini, et on applique $a)$ au complexe $\mathbf{P}_1 \xrightarrow{t_d} \mathbf{P}_0$ avec $\mathbf{P}_0 = \check{\mathbf{L}}_1$, $\mathbf{P}_1 = \check{\mathbf{L}}_0$, les autres termes étant nuls; on a alors $\mathrm{T}_1(\mathrm{A}) = \check{\mathrm{M}}$ et $\mathrm{T}_1(k) = \mathrm{Hom}_{\mathrm{A}}(\mathrm{M}, k) = \mathrm{Hom}_k(\mathrm{M}/\mathrm{mM}, k)$, autrement dit $\mathrm{T}_1(k)$ est le dual de l'espace vectoriel $\mathbf{M} \otimes_{\mathrm{A}} k$, et a donc même rang que ce dernier. Pour prouver que $b)$ entraîne $c)$, nous établirons d'abord le lemme suivant :

Lemme (7.6.11.6). — Étant donné un complexe  $\ldots\to0\to P_{1}\stackrel{d}{\to}P_{0}\to0\to\ldots$  de A-modules plats, on a une suite exacte

$$
\mathrm{o} \rightarrow \operatorname{Tor} _ {2} ^ {\mathrm{A}} \left(\mathrm{Z} _ {0} ^ {\prime}, k\right)\rightarrow \mathrm{T} _ {1} (\mathrm{A}) \otimes_ {\mathrm{A}} k \rightarrow \mathrm{T} _ {1} (k) \rightarrow \operatorname{Tor} _ {1} ^ {\mathrm{A}} \left(\mathrm{Z} _ {0} ^ {\prime}, k\right)\rightarrow \mathrm{o}. \tag {7.6.11.7}
$$

196

En effet, partant de la suite exacte $\mathrm{o} \to \mathrm{Z}_1 \to \mathrm{P}_1 \to \mathrm{B}_0 \to \mathrm{o}$, on en tire la suite exacte $\mathrm{o} \to \operatorname{Tor}_1^{\mathrm{A}}(\mathrm{B}_0, k) \to \mathrm{Z}_1 \otimes k \to \mathrm{P}_1 \otimes k \xrightarrow{u} \mathrm{B}_0 \otimes k \to \mathrm{o}$. De la suite exacte $\mathrm{o} \to \mathrm{B}_0 \to \mathrm{Z}_0 \to \mathrm{Z}_0' \to \mathrm{o}$, on tire, puisque $Z_0 = P_0$ est plat, $\operatorname{Tor}_1^{\mathrm{A}}(B_0, k) = \operatorname{Tor}_2^{\mathrm{A}}(Z_0', k)$; par définition, on a $Z_1 = T_1(A)$; enfin, on a $T_1(k) = \operatorname{Ker}(d \otimes 1)$, et $d \otimes 1$ se factorise en $P_1 \otimes k \xrightarrow{u} B_0 \otimes k \xrightarrow{v} Z_0 \otimes k = P_0 \otimes k$; on a $T_1(k) = u^{-1}(R)$, où $R = Ker v$, et comme $u$ est surjectif, $R = u(T_1(k))$; enfin, $R = \operatorname{Tor}_1^{\mathrm{A}}(Z_0', k)$ par définition de $v$, ce qui achève d'établir la suite exacte (7.6.11.7).

Pour déduire alors $c)$ de $b)$, on considère une suite exacte $\mathbf{L}_{1} \xrightarrow{d} \mathbf{L}_{0} \to \mathbf{N} \to \mathbf{o}$, où $\mathbf{L}_{0}$ et $\mathbf{L}_{1}$ sont des modules libres de type fini; considérons le foncteur T associé au complexe formé de $\mathbf{L}_{1}$ et $\mathbf{L}_{0}$; comme $\mathbf{L}_{0}$ et $\mathbf{L}_{1}$ sont libres, ils s'identifient à leurs biduals; donc si $\mathbf{M} = \operatorname{Coker}(^{t} d)$, $\mathbf{T}_{1}(\mathbf{A}) = \operatorname{Ker}(d) = \check{\mathbf{M}}$; par ailleurs, $\mathbf{M} \otimes_{\mathbf{A}} k = \operatorname{Coker}(^{t} d \otimes \mathbf{I}_{k})$ a même rang sur $k$ que $\operatorname{Ker}(d \otimes \mathbf{I}_{k})$. L'hypothèse $b)$ entraîne par suite que

$$
\operatorname{rang} _ {k} \left(\mathrm{T} _ {1} (\mathrm{A}) \otimes_ {\mathrm{A}} k\right) \leqslant \operatorname{rang} _ {k} \left(\mathrm{T} _ {1} (k)\right);
$$

comme $Z_0' = N$, l'inégalité (7.6.11.4) résulte donc de la suite exacte (7.6.11.7). Enfin, pour prouver que $c)$ entraîne $a)$, appliquons (7.6.11.6) en remplaçant $P_0$ et $P_1$ par $P_p$ et $P_{p-1}$; l'hypothèse $c)$ appliquée au module $Z_p'$ donne rang$_kR \geqslant$rang$_kS$, où $R = \text{Ker}(P_p \otimes k \to P_{p-1} \otimes k)$ et $S = Z_p \otimes k$. Or, si l'on factorise $d_{p+1}: P_{p+1} \to P_p$ en $P_{p+1} \xrightarrow{v} Z_p \xrightarrow{j} P_p$ on a $\text{Im}(d_{p+1} \otimes I) = (j \otimes I)(\text{Im}(v \otimes I))$. Comme

$$
\mathrm{T} _ {p} (\mathrm{A}) \otimes_ {\mathrm{A}} k = \left(\mathrm{Z} _ {p} / \mathrm{B} _ {p}\right) \otimes_ {\mathrm{A}} k = \left(\mathrm{Z} _ {p} \otimes k\right) / \operatorname{Im} (v \otimes \mathrm{I}),
$$

et $\mathrm{T}_{p}(k) = \mathrm{R} / \mathrm{Im}(d_{p + 1}\otimes \mathrm{I})$, on en conclut bien l'inégalité (7.6.II.2).

Cela étant, supposons que l'anneau local A soit régulier de dimension n; on sait alors

[17] que le A-module $\operatorname{Tor}_{i}^{\mathrm{A}}(k,k)$ est isomorphe à la puissance extérieure $\wedge (\mathfrak{m} / \mathfrak{m}^{2})$; on voit donc que la condition (7.6.11.4) n'est pas vérifiée pour $N = k$, dès que $n \geqslant 4$. Par contre, si l'anneau local intègre A est tel que tout A-module réflexif de type fini soit libre (ce qui est le cas lorsque A est un anneau régulier de dimension 2), la condition (7.6.11.3) est vérifiée : en effet, on sait que le dual $\check{\mathbf{M}}$ d'un A-module M de type fini M est réflexif, donc libre, et par suite $\operatorname{rang}_{k}(\check{\mathbf{M}} \otimes_{\mathrm{A}} k) = \operatorname{rang}_{\mathrm{K}}(\check{\mathbf{M}}) = \operatorname{rang}_{\mathrm{K}}(\mathbf{M})$ (K corps des fractions de A); par ailleurs, on sait que toute base sur $k$ de $\mathbf{M} \otimes_{\mathrm{A}} k$ est formée d'images d'un système de générateurs de M (Bourbaki, Alg. comm., chap. II, § 3, no 2, cor. 2 de la prop. 4), donc $\operatorname{rang}_{\mathrm{K}}(\mathbf{M}) \leqslant \operatorname{rang}_{k}(\mathbf{M} \otimes_{\mathrm{A}} k)$, ce qui prouve notre assertion.

## 7.7. Application aux morphismes propres : I. La propriété d'échange.

Les trois numéros qui suivent sont, pour l'essentiel, des traductions, dans le langage des morphismes de préschémas, des résultats des numéros précédents.

(7.7.1) Soit $f: \mathbf{X} \to \mathbf{Y}$ un morphisme quasi-compact et séparé de préschémas, et soit $\mathcal{P}_{\bullet}$ un complexe de $\mathcal{O}_{\mathbf{X}}$-Modules quasi-cohérents, dont l'opérateur de dérivation est de degré — 1; supposons en outre que les $\mathcal{O}_{\mathbf{X}}$-Modules $\mathcal{P}_{i}$ sont Y-plats ($\mathbf{0}_{\mathrm{I}}$, 6.7.1).

Nous allons considérer le $\partial$-foncteur $\mathcal{M} \leadsto \mathcal{T}_{\bullet}(\mathcal{M})$ (aussi noté $\mathcal{T}_{\bullet}(\mathcal{P}_{\bullet}, \mathcal{M})$) dans la catégorie des $\mathcal{O}_{\mathrm{Y}}$-Modules quasi-cohérents, à valeurs dans la catégorie des $\mathcal{O}_{\mathrm{Y}}$-Modules quasi-cohérents (en vertu de (6.2.3)), défini par

$$
\mathcal {T} _ {n} (\mathcal {P} _ {\bullet}, \mathcal {M}) = \mathcal {T} _ {n} (\mathcal {M}) = \mathcal {H} ^ {- n} (f, \mathcal {P} ^ {\bullet} \otimes_ {\mathcal {O} _ {\mathbf {Y}}} \mathcal {M})\tag{7.7.1.1}
$$

$$
\mathbf {z},\tag{pour  \( n \in Z, \}
$$

où $\mathcal{P}^{\bullet}$ est le complexe dont le terme de degré $j$ est $\mathrm{P}_{-j}$, l'opérateur de dérivation étant donc alors de degré $+1$. Le foncteur $\mathcal{T}_{\bullet}$ ainsi défini est un foncteur homologique en $\mathcal{M}$ (6.2.6).

(7.7.2) Soit $g: \mathrm{Y}' \to \mathrm{Y}$ un morphisme, et posons $\mathbf{X}' = \mathbf{X}_{(\mathrm{Y}')} = \mathbf{X} \times_{\mathrm{Y}} \mathbf{Y}'$ et $f' = f_{(\mathrm{Y}')}: \mathbf{X}' \to \mathbf{Y}'$, qui est un morphisme quasi-compact et séparé; soit d'autre part $\mathcal{P}' = \mathcal{P}_* \otimes_{\mathcal{O}_\mathrm{Y}} \mathcal{O}_{\mathrm{Y}'}$; c'est un complexe de $\mathcal{O}_{\mathrm{X}'}$-Modules quasi-cohérents qui sont $\mathrm{Y}'$-plats en vertu de (I, 9.1.12) et ($\mathbf{0}_I$, 6.2.1). Nous poserons (avec les mêmes conventions sur les degrés)

$$
\mathcal {T} _ {\bullet} ^ {\mathrm{Y} ^ {\prime}} (\mathcal {M} ^ {\prime}) = \mathcal {H} ^ {\bullet} (f ^ {\prime}, \mathcal {P} ^ {\bullet} \otimes_ {\mathcal {O} _ {\mathrm{Y} ^ {\prime}}} \mathcal {M} ^ {\prime}) = \mathcal {H} ^ {\bullet} (f ^ {\prime}, \mathcal {P} ^ {\bullet} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M} ^ {\prime})\tag{7.7.2.1}
$$

qui est un foncteur homologique en le $\mathcal{O}_{\mathrm{Y}^{\prime}}$-Module quasi-cohérent $\mathcal{M}^{\prime}$. Lorsque $\mathrm{Y}^{\prime}$ est un schéma affine d'anneau $\mathrm{A}^{\prime}$, on écrira $\mathcal{T}_{\bullet}^{\mathrm{A}^{\prime}}$ au lieu de $\mathcal{T}_{\bullet}^{\mathrm{Y}^{\prime}}$; pour tout $\mathrm{A}^{\prime}$-module $\mathrm{M}^{\prime}$, on a alors $\mathcal{T}_{\bullet}^{\mathrm{A}^{\prime}}(\widetilde{\mathrm{M}}^{\prime}) = (\Gamma(\mathrm{Y}^{\prime},\mathcal{T}_{\bullet}^{\mathrm{Y}^{\prime}}(\widetilde{\mathrm{M}}^{\prime})))^{\sim}$; on posera $\mathrm{T}_{\bullet}^{\mathrm{A}^{\prime}}(\mathrm{M}^{\prime}) = \Gamma(\mathrm{Y}^{\prime},\mathcal{T}_{\bullet}^{\mathrm{Y}^{\prime}}(\widetilde{\mathrm{M}}^{\prime}))$, qui est un foncteur homologique de $\mathrm{A}^{\prime}$-modules, à valeurs dans la catégorie des $\mathrm{A}^{\prime}$-modules. On observera que si $\mathrm{Y} = \operatorname{Spec}(\mathrm{A})$ est aussi affine, le foncteur de $\mathrm{A}^{\prime}$-modules $\mathrm{T}_{\bullet}^{\mathrm{A}^{\prime}}$ coincide avec le foncteur obtenu par extension des scalaires de $\mathrm{A}$ à $\mathrm{A}^{\prime}$ à partir du foncteur homologique de $\mathrm{A}$-modules $\mathrm{T}_{\bullet}^{\mathrm{A}}(7.1.3)$: en effet, soit $g: \mathrm{Y}^{\prime} \to \mathrm{Y}$ le morphisme correspondant à l'homomorphisme d'anneaux $\mathrm{A} \to \mathrm{A}^{\prime}$, et soit $g': \mathrm{X}^{\prime} \to \mathrm{X}$ le morphisme correspondant qui est affine (II, 1.6.2); si $\mathfrak{U}$ est un recouvrement ouvert affine de $\mathbf{X}$, $\mathfrak{U}' = g'^{-1}(\mathfrak{U})$ est un recouvrement ouvert affine de $\mathbf{X}^{\prime}$; en vertu de (6.2.2), tout revient à voir que $\mathrm{C}^{\bullet}(\mathfrak{U},\mathcal{P}_{\bullet}\otimes_{\mathcal{O}_{\mathrm{Y}}}g_{*}(\mathcal{M}^{\prime})) = \mathrm{C}^{\bullet}(\mathfrak{U}',\mathcal{P}_{\bullet}\otimes_{\mathcal{O}_{\mathrm{Y}}} \mathcal{M}')$, et finalement, que pour tout ouvert affine U de X, en posant $\mathrm{U}' = g'^{-1}(\mathrm{U})$, on a $\Gamma(\mathrm{U},\mathcal{P}_{\bullet}\otimes_{\mathcal{O}_{\mathrm{Y}}}g_{*}(\mathcal{M}^{\prime})) = \Gamma(\mathrm{U}',\mathcal{P}_{\bullet}\otimes_{\mathcal{O}_{\mathrm{Y}}} \mathcal{M}')$, ce qui est trivial (I, 1.3 et 3.2).

En particulier, si U est un ouvert de Y, on a, pour tout $\mathcal{O}_{\mathrm{Y}}$-Module quasi-cohérent $\mathcal{M}$

$$
\mathcal {T} _ {\bullet} ^ {\mathrm{U}} (\mathcal {M} \mid \mathrm{U}) = (\mathcal {T} _ {\bullet} (\mathcal {M})) \mid \mathrm{U}.\tag{7.7.2.2}
$$

(7.7.3) Pour tout $\mathcal{O}_{\mathrm{Y}}$-Module quasi-cohérent $\mathcal{M}$, on a un homomorphisme canonique, fonctoriel en $\mathcal{M}$:

$$
\mathcal {T} _ {p} (\mathcal {O} _ {\mathrm{Y}}) \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M} \to \mathcal {T} _ {p} (\mathcal {M}).\tag{7.7.3.1}
$$

En effet, si Y est affine, cet homomorphisme a été défini en (7.2.2); cette définition s'étend sans peine au cas général, en remarquant que si U, V sont deux ouverts affines de Y tels que  $V \subset U$ , le diagramme

$$
\begin{array}{c} (\mathcal {T} _ {p} (\mathcal {O} _ {\mathrm{Y}}) \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M})   |   \mathrm{U} = \mathcal {T} _ {p} ^ {\mathrm{U}} (\mathcal {O} _ {\mathrm{Y}} |   \mathrm{U}) \otimes_ {\mathcal {O} _ {\mathrm{Y}} | \mathrm{U}} (\mathcal {M}   |   \mathrm{U})   \to   \mathcal {T} _ {p} ^ {\mathrm{U}} (\mathcal {M}   |   \mathrm{U}) = (\mathcal {T} _ {p} (\mathcal {M}))   |   \mathrm{U} \\ \Bigg \downarrow \\ (\mathcal {T} _ {p} (\mathcal {O} _ {\mathrm{Y}}) \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M})   |   \mathrm{V} = \mathcal {T} _ {p} ^ {\mathrm{V}} (\mathcal {O} _ {\mathrm{Y}} |   \mathrm{V}) \otimes_ {\mathcal {O} _ {\mathrm{Y}} | \mathrm{V}} (\mathcal {M}   |   \mathrm{V})   \to   \mathcal {T} _ {p} ^ {\mathrm{V}} (\mathcal {M}   |   \mathrm{V}) = (\mathcal {T} _ {p} (\mathcal {M}))   |   \mathrm{V} \end{array}
$$

est commutatif par (7.2.3.3).

Pour tout morphisme  $g: Y' \to Y$  on a un homomorphisme canonique

$$
\mathcal {T} _ {p} (\mathcal {O} _ {\mathrm{Y}}) \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {O} _ {\mathrm{Y} ^ {\prime}} \rightarrow \mathcal {T} _ {p} ^ {\mathrm{Y} ^ {\prime}} (\mathcal {O} _ {\mathrm{Y} ^ {\prime}})\tag{7.7.3.2}
$$

qui n'est autre que le cas particulier de (6.7.11.2) (pour les aboutissements) dans le cas où $S = Y$, $v_1 = f$, $v_2 = I_Y$, $\mathcal{P}_{\bullet}^{(2)}$ réduit au seul terme $M$ de degré o.

Lorsque  $Y = \text{Spec}(A)$ ,  $Y' = \text{Spec}(A')$  sont affines, (7.7.3.2) n'est autre que l'homomorphisme de faisceaux correspondant à l'homomorphisme canonique de A'-modules défini dans (7.2.2)

$$
\mathbf {T} _ {p} ^ {\mathrm{A}} (\mathbf {A}) \otimes_ {\mathbf {A}} \mathbf {A} ^ {\prime} \rightarrow \mathbf {T} _ {p} ^ {\mathrm{A} ^ {\prime}} (\mathbf {A} ^ {\prime}) = \mathbf {T} _ {p} ^ {\mathrm{A}} (\mathbf {A} ^ {\prime})
$$

comme il résulte aisément de (6.7.11) (car dans le cas envisagé, on peut prendre $\mathfrak{U}^{\prime(i)} = u_i^{-1}(\mathfrak{U}^{(i)})$ dans (6.7.11)).

(7.7.4) Lorsque $f$ est un morphisme propre, $\mathrm{Y}=\mathrm{Spec}(\mathrm{A})$ un schéma affine noethérien et $\mathcal{P}$. un complexe de $\mathcal{O}_{\mathrm{X}}$-Modules cohérents et Y-plats limité inférieurement, on a vu (6.10.5) que l'on peut écrire à un isomorphisme près, $\mathcal{T}_{p}(\mathcal{M})=\mathcal{H}_{p}(\mathcal{L}_{\bullet}\otimes_{\mathcal{O}_{\mathrm{Y}}}\mathcal{M})$, avec $\mathcal{L}_{\bullet}=\widetilde{\mathrm{L}}_{\bullet}$, où $\mathrm{L}_{\bullet}$ est un complexe de A-modules libres de type fini limité inférieurement; le foncteur $\mathcal{T}_{\bullet}$ est donc du type qui a été étudié en détail dans (7.4) et (7.6). Nous allons traduire les résultats de cette étude :

Théorème (7.7.5). — Soient Y un préschéma localement noethérien,  $(\mathrm{U}_{\alpha})$  un recouvrement de Y formé d'ouverts affines,  $f: X \to Y$  un morphisme propre, P. un complexe de  $O_{X}$ -Modules cohérents et Y-plats limité inférieurement. Le foncteur homologique  $\mathcal{T}(\mathcal{M})$  défini par (7.7.1.1) possède alors les propriétés suivantes :

I) (La propriété de semi-continuité) (1). La fonction

$$
y \rightsquigarrow d _ {p} (y) = \operatorname{rang} _ {\mathbf {k} (y)} \mathrm{T} _ {p} ^ {\mathbf {k} (y)} (\boldsymbol {k} (y))\tag{7.7.5.1}
$$

est semi-continue supérieurement.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Un cas particulier de ce théorème se trouve déjà dans la note [3] de Chow-Igusa. La propriété de semi-continuité a été découverte, dans le cadre des espaces analytiques (et sous des hypothèses assez particulières), par Kodaira-Spencer (On the variations of almost-complex structures, Algebraic Geometry and Topology, A Symposium in honor of S. Lefschetz, Princeton Series n° 12, p. 139-150, Princeton, 1957) et la version générale démontrée par Grauert [5].</span></small>

II) (La propriété d'échange). Pour un entier p donné, les conditions suivantes sont équivalentes :

a) $\mathcal{T}_p$ est exact à droite.

a') $\mathcal{T}_{p}(\mathcal{M})$ est isomorphe à un foncteur de la forme $\mathcal{N}\otimes_{\mathcal{O}_{\mathrm{Y}}}\mathcal{M}$ ($\mathcal{N}$ étant nécessairement isomorphe à $\mathcal{T}_{p}(\mathcal{O}_{\mathrm{Y}})=\mathcal{H}^{-p}(f,\mathcal{P}^{\bullet}))$.

a'') L'homomorphisme canonique fonctoriel (7.7.3.1) est un isomorphisme.

b) $\mathcal{T}_{p-1}$ est exact à gauche.

b') Il existe un $\mathcal{O}_{\mathrm{Y}}$-Module 2 (nécessairement cohérent, et déterminé à un isomorphisme unique près) et un isomorphisme de foncteurs

$$
\mathcal {T} _ {p - 1} (\mathcal {M}) \xrightarrow {\sim} \mathcal {H} o m _ {\mathcal {O} _ {\mathbf {Y}}} (2, \mathcal {M}).\tag{7.7.5.2}
$$

c) En désignant par $\mathbf{A}_{\alpha}$ l'anneau de l'ouvert affine $\mathbf{U}_{\alpha}$, pour tout indice $\alpha$ le foncteur de $\mathbf{A}_{\alpha}$-modules $\mathbf{T}_{p}^{\mathbf{A}_{\alpha}}$ est exact à droite.

d) Pour tout morphisme  $g: Y' \to Y$ , l'homomorphisme canonique

$$
(7 \cdot 7 \cdot 5 \cdot 3)
$$

$$
\mathcal {T} _ {p} (\mathcal {O} _ {\mathrm{Y}}) \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {O} _ {\mathrm{Y} ^ {\prime}} \rightarrow \mathcal {T} _ {p} ^ {\mathrm{Y} ^ {\prime}} (\mathcal {O} _ {\mathrm{Y} ^ {\prime}})
$$

est un isomorphisme.

La propriété de semi-continuité est locale sur Y et résulte donc de la remarque (7.7.4) et de (7.6.9). Il est clair que $a'')$ entraîne $a')$ et que $a')$ entraîne $a)$. L'équivalence de $a$, $a''), b) et b')$ a été démontrée dans (7.3.1) et (7.4.6), compte tenu de la remarque (7.7.4), lorsque Y est affine. Pour passer au cas général, prouvons d'abord que $a$ est équivalent à $c$), ce qui prouvera le caractère local sur Y de la propriété $a)$; la démonstration s'appliquera également pour prouver le caractère local de $a'')$ et $b)$. Comme il est clair que $c$ entraîne $a)$, tout revient à prouver la réciproque. Il suffit évidemment de montrer que pour tout ouvert affine U de Y et toute suite exacte $o \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to o$ de $(\mathcal{O}_{Y}|U)$-Modules quasi-cohérents, il existe une suite exacte $o \to \mathcal{G}' \to \mathcal{G} \to \mathcal{G}'' \to o$ de $\mathcal{O}_{Y}$-Modules quasi-cohérents telle que $\mathcal{F}' = \mathcal{G}'|U, \mathcal{F} = \mathcal{G}|U, \mathcal{F}'' = \mathcal{G}''|U$; or, cela résulte aussitôt de l'hypothèse que Y est localement noethérien, et de (I, 9.4.2): on prolonge en effet $\mathcal{F}$ en un $\mathcal{O}_{X}$-Module quasi-cohérent $\mathcal{G}, \mathcal{F}'$ en un sous-$\mathcal{O}_{X}$-Module $\mathcal{G}'$ de $\mathcal{G}$, et il suffit de prendre $\mathcal{G}'' = \mathcal{G}/\mathcal{G}'$.

Pour démontrer l'équivalence de $b$) et $b'$) dans le cas général, remarquons que lorsque Y est affine, on sait que $\mathcal{Q}$ est déterminé à un isomorphisme unique près; si alors U est un ouvert affine du schéma affine Y, on en déduit qu'il existe un isomorphisme fonctoriel $\mathcal{T}_{p-1}^{\mathrm{U}}(\mathcal{M}|\mathrm{U})\xrightarrow{\sim}\mathcal{H}om_{\mathcal{O}_{\mathrm{Y}}|\mathrm{U}}(\mathcal{Q}|\mathrm{U},\mathcal{M}|\mathrm{U})$. Dans le cas général, pour tout ouvert affine U de Y, il y a un $(\mathcal{O}_{\mathrm{Y}}|\mathrm{U})$-Module cohérent $\mathcal{Q}_{\mathrm{U}}$ et un isomorphisme fonctoriel $\mathcal{T}_{p-1}^{\mathrm{U}}(\mathcal{M}|\mathrm{U})\to\mathcal{H}om_{\mathcal{O}_{\mathrm{Y}}|\mathrm{U}}(\mathcal{Q}_{\mathrm{U}},\mathcal{M}|\mathrm{U})$; la remarque précédente montre que si V est un ouvert affine contenu dans U, on a $\mathcal{Q}_{\mathrm{U}}|\mathrm{V}=\mathcal{Q}_{\mathrm{V}}$; d'où l'existence et l'unicité du $\mathcal{O}_{\mathrm{Y}}$-Module $\mathcal{Q}$ vérifiant (7.7.5.2).

Reste enfin à montrer l'équivalence de $a$) et $d$); il est clair que $d$) est de caractère local sur Y, et l'on a vu ci-dessus qu'il en est de même de $a$); en outre, $d$) est aussi local sur Y'. Or, lorsque $\mathrm{Y}=\mathrm{Spec}(\mathrm{A})$, $\mathrm{Y}'=\mathrm{Spec}(\mathrm{A}')$, on a vu que $\mathrm{T}_{\bullet}^{\mathrm{A}}$ est le foncteur obtenu

à partir de $\mathbf{T}_{\bullet}^{\mathrm{A}}$ par extension des scalaires à $\mathbf{A}'$, et il est clair alors que $a')$ entraîne que (7.7.5.3) est un isomorphisme. Inversement, supposons toujours $\mathbf{Y} = \operatorname{Spec}(\mathbf{A})$ affine et soit $\mathbf{A}'$ la A-algèbre $\mathbf{A} \oplus \mathbf{M}$, où $\mathbf{M}$ est un A-module quelconque, la multiplication dans $\mathbf{A}'$ étant donnée par $(a_{1}, m_{1})(a_{2}, m_{2}) = (a_{1}a_{2}, a_{1}m_{2} + a_{2}m_{1})$; alors

$$
\mathrm{T} _ {p} ^ {\mathrm{A} ^ {\prime}} (\mathrm{A} ^ {\prime}) = \mathrm{T} _ {p} (\mathrm{A} \oplus \mathrm{M}) = \mathrm{T} _ {p} (\mathrm{A}) \oplus \mathrm{T} _ {p} (\mathrm{M}),
$$

et l'hypothèse que (7.7.5.3) soit bijectif entraîne qu'il en est de même de l'application canonique  $\mathbf{T}_{p}(\mathbf{A})\otimes_{\mathbf{A}}\mathbf{M}\to\mathbf{T}_{p}(\mathbf{M})$ , autrement dit d) entraîne  $a''$ ), ce qui achève la démonstration.

Théorème (7.7.6). — Soient Y un préschéma localement noethérien, $f: \mathbf{X} \to \mathbf{Y}$ un morphisme propre, $\mathcal{F}$ un $\mathcal{O}_{\mathbf{X}}$-Module cohérent et Y-plat. Il existe alors un $\mathcal{O}_{\mathbf{Y}}$-Module cohérent 2 (déterminé à isomorphisme unique près) et un isomorphisme de foncteurs en le $\mathcal{O}_{\mathbf{Y}}$-Module quasi-cohérent $\mathcal{M}$:

$$
f _ {*} (\mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M}) \simeq \mathcal {H} o m _ {\mathcal {O} _ {\mathrm{Y}}} (2, \mathcal {M})\tag{7.7.6.1}
$$

(d'où un isomorphisme de foncteurs

$$
\Gamma (\mathbf {X}, \mathcal {F} \otimes_ {\mathcal {O} _ {\mathbf {Y}}} \mathcal {M}) \simeq \operatorname{Hom} _ {\mathcal {O} _ {\mathbf {Y}}} (\mathcal {2}, \mathcal {M}).)\tag{7.7.6.2}
$$

En effet, comme $\mathcal{M} \rightsquigarrow \mathcal{F} \otimes_{\mathcal{O}_{\mathrm{Y}}} \mathcal{M}$ est exact (0$_{\mathrm{I}}$, 6.7.4) et $f_*$ exact à gauche, le foncteur $\mathcal{M} \rightsquigarrow f_*(\mathcal{F} \otimes_{\mathcal{O}_{\mathrm{Y}}} \mathcal{M})$ est exact à gauche. Il suffit alors d'appliquer l'équivalence de (7.7.5, b)) et (7.7.5, b')) pour $p = \mathrm{i}$.

Corollaire (7.7.7). — Soient Y un préschéma localement noethérien, $f: X \to Y$ un morphisme propre, $\mathcal{F}$, $\mathcal{F}'$ deux $\mathcal{O}_{X}$-Modules cohérents et Y-plats, $u: \mathcal{F} \to \mathcal{F}'$ un homomorphisme. Considérons les deux foncteurs en le $\mathcal{O}_{Y}$-Module quasi-cohérent $\mathcal{M}$ :

$$
\begin{array}{c} \mathcal {T} (\mathcal {M}) = \mathrm{Ker} (f _ {*} (\mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M}) \to f _ {*} (\mathcal {F} ^ {\prime} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M})) \\ \mathrm{T} (\mathcal {M}) = \Gamma (\mathrm{Y}, \mathcal {T} (\mathcal {M})) = \mathrm{Ker} (\Gamma (\mathrm{X}, \mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M}) \to \Gamma (\mathrm{X}, \mathcal {F} ^ {\prime} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M})). \end{array}
$$

Alors il existe un $\mathcal{O}_{\mathrm{Y}}$-Module cohérent $\mathcal{R}$ (déterminé à isomorphisme unique près) et des isomorphismes de foncteurs

$$
(7. 7. 7. \mathbf {I})\tag{7.7.7.2}
$$

$$
\begin{array}{l} \mathcal {T} (\mathcal {M}) \xrightarrow {\sim} \mathcal {H} o m _ {\mathcal {O} _ {\mathbf {Y}}} (\mathcal {R}, \mathcal {M}) \\ \mathrm{T} (\mathcal {M}) \xrightarrow {\sim} \mathrm{Hom} _ {\mathcal {O} _ {\mathbf {Y}}} (\mathcal {R}, \mathcal {M}). \end{array}
$$

On peut se borner à démontrer (7.7.7.2); cela prouvera en effet (7.7.7.1) dans le cas où Y est affine, et on passera de là au cas général en raisonnant comme dans la démonstration de l'équivalence de (7.7.5, b) et $b'$), grâce à l'unicité à isomorphisme unique près d'un représentant d'un foncteur représentable (0, 8.1.8). Il résulte de (7.7.6) qu'il existe deux $\mathcal{O}_{\mathrm{Y}}$-Modules cohérents 2, 2' définissant des isomorphismes fonctoriels

$$
\Gamma (\mathrm{X}, \mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M}) \stackrel {{\sim}} {{\to}} \operatorname{Hom} _ {\mathcal {O} _ {\mathrm{Y}}} (2, \mathcal {M}), \quad \Gamma (\mathrm{X}, \mathcal {F} ^ {\prime} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M}) \stackrel {{\sim}} {{\to}} \operatorname{Hom} _ {\mathcal {O} _ {\mathrm{Y}}} (2 ^ {\prime}, \mathcal {M}).
$$

Or, $u: \mathcal{F} \to \mathcal{F}'$ définit canoniquement un morphisme de foncteurs

$$
\Gamma (\mathrm{X}, \mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M}) \rightarrow \Gamma (\mathrm{X}, \mathcal {F} ^ {\prime} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M});\tag{201}
$$

il correspond à ce dernier un homomorphisme unique $v:2'\to2$ de $\mathcal{O}_{\mathrm{Y}}$-Modules tel que le diagramme

![](images/page_68_image_1.jpg)

soit commutatif (0, 8.1.4). Comme le foncteur contravariant $\mathcal{N} \leadsto \mathrm{Hom}_{\mathcal{O}_{\mathbb{Y}}}(N, \mathcal{M})$ est exact à gauche dans la catégorie des $\mathcal{O}_{\mathbb{Y}}$-Modules, il suffit de prendre $\mathcal{R} = \mathrm{Coker}(v)$ pour obtenir l'isomorphisme (7.7.7.2) cherché.

Corollaire (7.7.8). — Sous les hypothèses de (7.7.6) relatives à X, Y et f, soient F, G deux  $O_{X}$ -Modules cohérents vérifiant les conditions suivantes : (i) F est Y-plat : (ii) G est isomorphe au conoyau d'un homomorphisme de  $O_{X}$ -Modules localement libres de type fini  $E_{1} \rightarrow E_{0}$ . Considérons les deux foncteurs en le  $O_{Y}$ -Module quasi-cohérent M :

$$
\begin{array}{c} \mathcal {T} (\mathcal {M}) = f _ {*} (\mathcal {H} o m _ {\mathcal {O} _ {\mathrm{Y}}} (\mathcal {G}, \mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M})) \\ \mathrm{T} (\mathcal {M}) = \Gamma (\mathrm{Y}, \mathcal {T} (\mathcal {M})) = \mathrm{Hom} _ {\mathcal {O} _ {\mathrm{x}}} (\mathcal {G}, \mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M}). \end{array}
$$

Alors il existe un $\mathcal{O}_{\mathbf{y}}$-Module cohérent $\mathcal{N}$ (déterminé à isomorphisme unique près) et des isomorphismes de foncteurs

(7.7.8.1)

$$
\begin{array}{l} \mathcal {T} (\mathcal {M}) \simeq \mathcal {H} o m _ {\mathcal {O} _ {\mathrm{Y}}} (\mathcal {N}, \mathcal {M}) \\ \mathrm{T} (\mathcal {M}) \simeq \mathrm{Hom} _ {\mathcal {O} _ {\mathrm{Y}}} (\mathcal {N}, \mathcal {M}). \end{array}\tag{7.7.8.2}
$$

En vertu de l'isomorphisme fonctoriel (0$_{I}$, 5.4.2.1), on a des isomorphismes fonctoriels en $\mathcal{M}$

$$
\mathcal {H} o m _ {\mathcal {O} _ {\mathrm{X}}} (\mathcal {E} _ {i}, \mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M}) \stackrel {{\sim}} {{\to}} \check {\mathcal {E}} _ {i} \otimes_ {\mathcal {O} _ {\mathrm{X}}} (\mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M}) \stackrel {{\sim}} {{\to}} (\check {\mathcal {E}} _ {i} \otimes_ {\mathcal {O} _ {\mathrm{X}}} \mathcal {F}) \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M} \stackrel {{\sim}} {{\to}} \mathcal {H} o m _ {\mathcal {O} _ {\mathrm{X}}} (\mathcal {E} _ {i}, \mathcal {F}) \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M}
$$

pour $i=0,1$. Posons $\mathcal{F}_{i}=\mathcal{H}om_{\mathcal{O}_{X}}(\mathcal{E}_{i},\mathcal{F})$ pour $i=0,1$; ce sont des $\mathcal{O}_{X}$-Modules cohérents $(\mathbf{0}_{I},5.3.5)$ et Y-plats $(\mathbf{0}_{I},5.4.2)$; soit $u=\mathcal{H}om(v,\mathrm{I}_{\mathcal{F}}):\mathcal{F}_{0}\to\mathcal{F}_{1}$. En vertu de l'exactitude à gauche du foncteur $\mathcal{H}\rightsquigarrow\mathcal{H}om_{\mathcal{O}_{X}}(\mathcal{H},\mathcal{F}\otimes_{\mathcal{O}_{Y}}\mathcal{M})$, on a des isomorphismes fonctoriels en $\mathcal{M}$

$$
\begin{array}{r l} \mathcal {H} o m _ {\mathcal {O} _ {\mathrm{x}}} (\mathcal {G}, \mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{y}}} \mathcal {M}) & \simeq \operatorname{Ker} (\mathcal {H} o m _ {\mathcal {O} _ {\mathrm{x}}} (\mathcal {E} _ {0}, \mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{y}}} \mathcal {M}) \to \mathcal {H} o m _ {\mathcal {O} _ {\mathrm{x}}} (\mathcal {E} _ {1}, \mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{y}}} \mathcal {M})) \simeq \\ & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \operatorname{Ker} (\mathcal {F} _ {0} \otimes_ {\mathcal {O} _ {\mathrm{y}}} \mathcal {M} \to \mathcal {F} _ {1} \otimes_ {\mathcal {O} _ {\mathrm{y}}} \mathcal {M}) \end{array}
$$

Puisque $f_{*}$ est exact à gauche, on en déduit un isomorphisme fonctoriel

$$
f _ {*} (\mathcal {H} o m _ {\mathcal {O} _ {\mathrm{X}}} (\mathcal {G}, \mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M})) \xrightarrow {\sim} \operatorname{Ker} (f _ {*} (\mathcal {F} _ {0} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M}) \to f _ {*} (\mathcal {F} _ {1} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M}))
$$

et il suffit alors d'appliquer (7.7.7).

Remarques (7.7.9). — (i) Dans (7.7.6), (7.7.7), (7.7.8), la formation des $\mathcal{O}_{\mathrm{Y}}$-Modules 2, $\mathcal{R}$, $\mathcal{N}$ permute aux changements de base. Par exemple (gardant les notations de (7.7.2)), dans le cas (7.7.6), on a, pour tout $\mathcal{O}_{\mathrm{Y}}$-Module quasi-cohérent $\mathcal{M}'$, l'isomorphisme

$$
f _ {*} ^ {\prime} (\mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {M} ^ {\prime}) \stackrel {{\sim}} {{\to}} \mathcal {H} o m _ {\mathcal {O} _ {\mathrm{Y} ^ {\prime}}} (g ^ {*} (\mathcal {Q}), \mathcal {M} ^ {\prime})
$$

car en vertu de la remarque faite dans (7.7.2), tout revient à voir que l'on a

$$
\operatorname{Hom} _ {\mathcal {O} _ {\mathrm{Y}}} (\mathcal {2}, g _ {*} (\mathcal {M} ^ {\prime})) = \operatorname{Hom} _ {\mathcal {O} _ {\mathrm{Y} ^ {\prime}}} (g ^ {*} (\mathcal {2}), \mathcal {M} ^ {\prime})
$$

ce qui n'est autre que $(\mathbf{0}_{\mathrm{I}}, 4.4.3.\mathrm{I})$. De même, quand dans (7.7.7) on remplace Y, $f, \mathcal{M}, \mathcal{F}, \mathcal{F}'$ par Y', $f', \mathcal{M}'$, $\mathcal{F} \otimes_{\mathcal{O}_{\mathrm{X}}}\mathcal{O}_{\mathrm{X}'}$, $\mathcal{F}' \otimes_{\mathcal{O}_{\mathrm{X}}}\mathcal{O}_{\mathrm{X}'}$, il faut remplacer $\mathcal{R}$ par $g^{*}(\mathcal{R})$. Enfin, dans (7.7.8), lorsqu'on remplace X, Y, $f, \mathcal{M}, \mathcal{F}$ par X', Y', $f', \mathcal{M}'$, $\mathcal{F} \otimes_{\mathcal{O}_{\mathrm{X}}}\mathcal{O}_{\mathrm{X}'}$, et $\mathcal{G}$ par $\mathcal{G}' = \mathcal{G} \otimes_{\mathcal{O}_{\mathrm{Y}}}\mathcal{O}_{\mathrm{X}'}$, il faut remplacer $\mathcal{N}$ par $g^{*}(\mathcal{N})$: cela résulte de ce que l'on a encore une suite exacte $\mathcal{E}_1' \to \mathcal{E}_0' \to \mathcal{G}' \to 0$ avec $\mathcal{E}_i' = \mathcal{E}_i \otimes_{\mathcal{O}_{\mathrm{Y}}}\mathcal{O}_{\mathrm{X}'}$ et de ce que $\check{\mathcal{E}}_i' \otimes_{\mathcal{O}_{\mathrm{X}'}}(\mathcal{F} \otimes_{\mathcal{O}_{\mathrm{Y}}}\mathcal{M}') = \check{\mathcal{E}}_i \otimes_{\mathcal{O}_{\mathrm{X}}}(\mathcal{F} \otimes_{\mathcal{O}_{\mathrm{Y}}}\mathcal{M})$ ($i = 0, 1$).

(ii) La condition (ii) de l'énoncé de (7.7.8) relative à $\mathcal{G}$ est toujours satisfaite pour un $\mathcal{O}_{\mathrm{X}}$-Module cohérent $\mathcal{G}$ quelconque lorsqu'il existe un $\mathcal{O}_{\mathrm{X}}$-Module inversible Y-ample, par exemple lorsque Y est affine et $f: \mathrm{X} \to \mathrm{Y}$ est un morphisme projectif. Il suffit alors de noter (compte tenu de (II, 5.5.1)) qu'il existe un $\mathcal{O}_{\mathrm{X}}$-Module localement libre de type fini $\mathcal{E}_0$ tel que $\mathcal{G}$ soit isomorphe à un quotient de $\mathcal{E}_0$ (II, 2.7.10); comme $\mathcal{E}_0$ et $\mathcal{G}$ sont cohérents, il en est de même du noyau $\mathcal{G}_1$ de $\mathcal{E}_0 \to \mathcal{G}$, et en appliquant le même résultat à $\mathcal{G}_1$, on obtient bien une suite exacte $\mathcal{E}_1 \to \mathcal{E}_0 \to \mathcal{G} \to 0$ où $\mathcal{E}_0$ et $\mathcal{E}_1$ sont localement libres de type fini.

(iii) Nous prouverons au chap. V que, dans (7.7.8), l'hypothèse restrictive (ii) est surabondante.

Proposition (7.7.10) (critères locaux pour la propriété d'échange). — Sous les conditions générales de (7.7.5), soient y un point de Y, p un entier. Les propriétés suivantes sont équivalentes :

a) Le foncteur $\mathbf{T}_{p}^{\mathcal{O}y}$ est exact à droite.

b) $L^{\prime}$ homomorphisme canonique $\mathbf{T}_{p}^{\mathcal{O}y}(\mathcal{O}_{y})\to \mathbf{T}_{p}^{\mathcal{O}y}(\boldsymbol {k}(y))$ est surjectif.

c) Pour tout entier $n$, l'homomorphisme canonique $\mathbf{T}_{p}^{\mathcal{O}y}(\mathcal{O}_{y}/\mathfrak{m}_{y}^{n+1}) \to \mathbf{T}_{p}^{\mathcal{O}y}(\boldsymbol{k}(y))$ est surjectif.

De plus, l'ensemble des $y \in \mathbf{Y}$ vérifiant ces conditions est le plus grand ensemble ouvert $\mathbf{U}$ de $\mathbf{Y}$ tel que $\mathcal{T}_p^{\mathrm{U}}$ soit exact à droite.

Compte tenu de (7.7.4), l'équivalence de $a$), $b$) et $c$) résulte de (7.4.7) et (7.5.2). Le fait que l'ensemble U où $\mathrm{T}_{p}^{\mathcal{O}y}$ est exact à droite soit ouvert est aussi conséquence de (7.4.4), et inversement si $\mathcal{T}_{p}^{\mathrm{V}}$ est exact à droite, il en est de même de $\mathrm{T}_{p}^{\mathcal{O}y}$ pour tout $y\in\mathrm{V}$, par la condition $c$) de (7.7.5) et (7.6.1).

Corollaire (7.7.11). — Si $\mathcal{T}_{p}$ est exact à droite (resp. à gauche), alors, pour tout morphisme $g: Y' \to Y$, $\mathcal{T}_{p}^{Y'}$ est exact à droite (resp. à gauche). La réciproque est vraie lorsque le morphisme $g$ est fidèlement plat.

La première assertion est conséquence immédiate de (7.6.1) et du fait que la question est locale sur Y et Y', d'après (7.7.5, c) et b)). Pour démontrer la seconde assertion, il suffit de voir que pour tout  $y \in Y$ ,  $T_{p}^{c_{y}}$  est exact à droite (resp. à gauche), en vertu de (7.7.10). Mais par hypothèse, il existe  $y' \in Y'$  tel que  $g(y') = y$ , et  $O_{y'}$  est un  $O_{y}$ -module fidèlement plat; la conclusion résulte alors de l'hypothèse et de (7.6.1).

Remarques (7.7.12). — (i) Sous les hypothèses de (7.7.4), supposons en outre que $\mathcal{P}$. soit un complexe fini; alors il résulte de (7.7.1) (puisqu'on peut prendre pour $\mathfrak{U}$ un recouvrement ouvert affine fini de X) que le bicomplexe $\mathbf{C}^{\bullet}(\mathfrak{U},\mathcal{P}^{\bullet}\otimes_{\mathcal{O}_{\mathbb{Y}}}\mathcal{M})$ est aussi fini, et de façon précise qu'il existe un ensemble fini E de couples, indépendant de $\mathcal{M}$, tel que $\mathbf{C}^{h}(\mathfrak{U},\mathcal{P}^{k}\otimes_{\mathcal{O}_{\mathbb{Y}}}\mathcal{M}) = 0$ pour tous les couples $(h,k)\notin \mathbf{E}$. On en conclut qu'il existe $i_{1}$ tel que, pour $i\geqslant i_{1}$, on ait $\mathcal{T}_{i}(\mathcal{M}) = 0$ pour tout $\mathcal{O}_{\mathbb{Y}}$-Module quasi-cohérent $\mathcal{M}$. En particulier, $\mathcal{T}_{i}$ est trivialement un foncteur exact en $\mathcal{M}$ pour ces valeurs de $i$, et par suite (7.4.1), $\mathrm{Z}_{i}^{\prime}(\mathrm{L}_{\bullet})$ est un A-module plat de type fini (donc projectif de type fini, puisque A est noethérien) pour ces valeurs de $i$. Considérons alors le complexe ($\mathrm{L}_{\bullet}^{\prime}$) de A-modules tel que $\mathrm{L}_{i}^{\prime} = \mathrm{L}_{i}$ pour $i < i_{1}$, $\mathrm{L}_{i_{1}}^{\prime} = \mathrm{Z}_{i_{1}}^{\prime}(\mathrm{L}_{\bullet})$ et $\mathrm{L}_{i}^{\prime} = 0$ pour $i > i_{1}$ et soit $\mathcal{L}_{\bullet}^{\prime} = \widetilde{\mathrm{L}}_{\bullet}^{\prime}$. Il est clair que $\mathcal{H}_{i}(\mathcal{L}_{\bullet}^{\prime}\otimes_{\mathcal{O}_{\mathbb{Y}}}\mathcal{M}) = \mathcal{H}_{i}(\mathcal{L}_{\bullet}^{\prime}\otimes_{\mathcal{O}_{\mathbb{Y}}}\mathcal{M})$ pour $i < i_{1}-1$ et aussi pour $i\geqslant i_{1}$ (les deux membres étant alors nuls); enfin, comme $\operatorname{Im}(Z_{i_1}'\otimes_A M) = \operatorname{Im}(L_{i_1}\otimes_A M)$ par définition, on a aussi $\mathcal{H}_{i}(\mathcal{L}_{\bullet}^{\prime}\otimes_{\mathcal{O}_{\mathbb{Y}}}\mathcal{M}) = \mathcal{H}_{i}(\mathcal{L}_{\bullet}\otimes_{\mathcal{O}_{\mathbb{Y}}}\mathcal{M})$ pour $i = i_{1}-1$. On voit donc qu'on peut supposer dans (7.7.4) que $\mathcal{L}_{\bullet}$ est aussi un complexe fini, à condition d'exiger seulement que les $\mathcal{L}_{i}$ soient des $\mathcal{O}_{\mathbb{Y}}$-Modules localement libres (associés à des A-modules projectifs de type fini).

Ce raisonnement s'applique en particulier au cas où $\mathcal{P}$ est réduit à un seul terme $\mathcal{F} \neq 0$, de degré o (auquel cas $\mathcal{T}_{n}(\mathcal{M}) = \mathrm{R}^{-n} f_{*}(\mathcal{F} \otimes_{\mathcal{O}_{\mathrm{Y}}}\mathcal{M}))$; on peut alors supposer que les $\mathcal{L}_{i}$ sont nuls pour $i > 0$; on utilisera de préférence dans ce cas les notations cohomologiques, écrivant donc $\mathcal{T}^{-p}$ au lieu de $\mathcal{T}_{p}$.

(ii) Lorsque dans l'énoncé de (7.7.5), on ne suppose plus que les  $P_{i}$  sont Y-plats, les conclusions restent valables à condition de poser cette fois

$$
\mathcal {T} _ {p} (\mathcal {M}) = \mathfrak {C o r} _ {p} ^ {\mathrm{Y}} (f, \mathrm{I} _ {\mathrm{Y}}; \mathscr {P} _ {\bullet}, \mathcal {M}).\tag{7.7.12.1}
$$

En effet, $\mathfrak{Cor}_{n}^{\mathrm{Y}}(f,\mathrm{I}_{\mathrm{Y}};\mathcal{P}_{\bullet},\mathcal{O}_{\mathrm{Y}})$ est alors un $\mathcal{O}_{\mathrm{Y}}$-Module cohérent en vertu de (6.7.9). La démonstration de (6.10.5) s'applique sans changement, compte tenu de (6.10.1) et montre encore que lorsque $\mathrm{Y} = \operatorname {Spec}(\mathrm{A})$ est affine, l'on a $\mathcal{T}_p(\mathcal{M}) = \mathcal{H}_p(\mathcal{L}_\otimes_{\mathcal{O}_\mathrm{Y}}\mathcal{M})$, avec $\mathcal{L}_{\bullet} = \widetilde{\mathrm{L}}_{\bullet}$, où $\mathrm{L}_{\bullet}$ est un complexe de A-modules libres de type fini; cela prouve notre assertion.

## 7.8. Application aux morphismes propres : II. Critères de platitude cohomologique.

Définition (7.8.1). — Soient X, Y deux préschémas, $f: \mathbf{X} \to \mathbf{Y}$ un morphisme quasi-compact et séparé, $\mathcal{P}_{\bullet}$ un complexe de $\mathcal{O}_{\mathrm{X}}$-Modules quasi-cohérents et Y-plats, $\mathcal{T}_{\bullet}$ le foncteur homologique de $\mathcal{O}_{\mathrm{Y}}$-Modules quasi-cohérents défini par (7.7.1.1), y un point de Y. On dit que $\mathcal{P}_{\bullet}$ est

homologiquement plat sur Y au point y, en dimension p (ou cohomologiquement plat sur Y au point y, en dimension —p) s'il existe un voisinage ouvert U de y dans Y tel que  $T_{p}^{U}=T_{U}^{-p}$  soit exact. On dit que P, est homologiquement plat en dimension p sur Y (ou cohomologiquement plat en dimension —p sur Y) s'il est homologiquement plat sur Y en tout point  $y\in Y$, en dimension p.

Lorsque $\mathcal{P}$. est homologiquement plat sur Y (resp. sur Y au point $y$) pour toute dimension $p$, on dit simplement que $\mathcal{P}$. est homologiquement plat sur Y (resp. sur Y au point $y$) ou cohomologiquement plat sur Y (resp. sur Y au point $y$).

(7.8.2) Par définition, la notion de platitude homologique sur Y est locale sur Y. Si Y est localement noethérien, ou un schéma, pour que P. soit homologiquement plat sur Y en dimension p, il faut et il suffit que le foncteur  $T_{p}$  soit exact : la démonstration a été faite dans le cas où Y est localement noethérien au cours de la démonstration de (7.7.5); le raisonnement est le même (basé sur (I, 9.4.2) appliqué à un ouvert affine dans un schéma quasi-compact) lorsque Y est un schéma.

Proposition (7.8.3). — Les notations et hypothèses étant celles de (7.8.1), les conditions suivantes sont équivalentes :

a) $\mathcal{P}$. est homologiquement plat sur Y au point y en dimension $p$.

b) Il existe un voisinage ouvert U de y dans Y tel que $\mathcal{T}_{p}^{\mathrm{U}}$ et $\mathcal{T}_{p+1}^{\mathrm{U}}$ soient exacts à droite.

c) Il existe un voisinage ouvert U de y dans Y tel que $\mathcal{T}_{p}^{\mathrm{U}}$ et $\mathcal{T}_{p-1}^{\mathrm{U}}$ soient exacts à gauche.

d) Il existe un voisinage ouvert U de y dans Y tel que $\mathcal{T}_{p+1}^{\mathrm{U}}$ est exact à droite et $\mathcal{T}_{p-1}^{\mathrm{U}}$ exact à gauche.

Compte tenu de l'interprétation de $\mathcal{T}_{p}$ lorsque Y est affine, cela n'est qu'une traduction d'une partie de (7.3.3).

Proposition (7.8.4). — Soient Y un préschéma localement noethérien, $f: X \to Y$ un morphisme propre, $\mathcal{P}$, un complexe de $\mathcal{O}_{X}$-Modules cohérents et Y-plats limité inférieurement, $\mathcal{T}$, le foncteur défini par (7.7.1.1). Pour tout $y \in Y$, les conditions suivantes sont équivalentes :

a) $\mathcal{P}$. est homologiquement plat sur Y en y en dimension $p$.

b) Le foncteur $\mathbf{T}_p^{\mathcal{O}y}$ est exact.

c) Il existe un entier $n_{0}$ tel que pour $n \geqslant n_{0}$, on ait

(7.8.4.1) long $\mathrm{T}_p^{\mathcal{O}_y}(\mathcal{O}_y / \mathfrak{m}_y^{n + 1}) = \mathrm{long}\mathrm{T}_p^{\mathcal{O}_y}(\boldsymbol {k}(\boldsymbol {y}))$ .long $\mathcal{O}_y / \mathfrak{m}_y^{n + 1}$

(où il s'agit de longueurs de $\mathcal{O}_y$-modules).

d) Il y a un voisinage ouvert U de y tel que  $(\mathcal{H}^{-p}(f,\mathcal{P}^{\bullet}))|U$  soit isomorphe à un  $(\mathcal{O}_{\mathrm{Y}}|\mathrm{U})$ -Module de la forme  $(\mathcal{O}_{\mathrm{Y}}|\mathrm{U})^{m}$  et que, pour tout  $(\mathcal{O}_{\mathrm{Y}}|\mathrm{U})$ -Module quasi-cohérent M, l'homomorphisme canonique

$$
(7. 8. 4. 2)
$$

$$
\left(\mathcal {K} ^ {- p} (f, \mathcal {P} ^ {\bullet})\right) | U) \otimes_ {\mathcal {O} _ {Y} | U} \mathcal {M} \rightarrow \mathcal {K} ^ {- p} (f, (\mathcal {P} ^ {\bullet} | U) \otimes_ {\mathcal {O} _ {Y} | U} \mathcal {M})
$$

soit bijectif.

Lorsque ces conditions sont vérifiées, on a en outre la propriété suivante :

e) Il existe un voisinage de y dans lequel la fonction  $z \leadsto d_{p}(z)$  (définie dans (7.7.5.1)) est constante.

De plus, si Y est réduit au point y (0$_{I}$, 4.1.4), e) est équivalente aux autres conditions.

En effet, la condition $b)$ équivaut à dire que $\mathrm{T}_{p}^{\mathcal{O}_{y}}$ et $\mathrm{T}_{p+1}^{\mathcal{O}_{y}}$ sont exacts à droite (7.3.3). L'équivalence de $a)$ et $b)$ résulte alors de (7.7.10) et (7.8.3). Comme $\mathcal{O}_{y}/\mathfrak{m}_{y}^{n+1}$ est artinien, et que $\mathrm{T}_{p}^{\mathcal{O}_{y}}(\mathcal{O}_{y}/\mathfrak{m}_{y}^{n+1})$ et $\mathrm{T}_{p}^{\mathcal{O}_{y}}(\boldsymbol{k}(y))$ sont des $(\mathcal{O}_{y}/\mathfrak{m}_{y}^{n+1})$-modules de type fini (7.7.4), donc de longueur finie, l'équivalence de $b)$ et $c)$ résulte encore de (7.7.10) et de (7.3.5.7). Le fait que $a)$ entraîne $e)$, et lui est équivalente lorsque $\mathcal{O}_{y}$ est réduit, est conséquence de (7.6.9). Enfin, $a)$ entraîne que (7.8.4.2) est bijectif en vertu de la définition (7.8.1) et de (7.7.5); d'autre part, $a)$ entraîne que $(\mathcal{H}^{-p}(f,\mathcal{P}^{\bullet}))_{y}$ est un $\mathcal{O}_{y}$-module plat (7.3.3,f)), donc libre ($\mathbf{0}$, 10.1.3), puisqu'il s'agit d'un $\mathcal{O}_{y}$-module de type fini en vertu de (7.7.4); puisque $\mathcal{H}^{-p}(f,\mathcal{P}^{\bullet})$ est un $\mathcal{O}_{Y}$-Module cohérent (7.7.4), il est localement libre dans un voisinage de $y$ ($\mathbf{0}_{I}$, 5.2.7). Inversement, il est clair que $d)$ entraîne $a)$ par définition du foncteur $\mathcal{T}_{p}^{\mathrm{U}}$ (7.7.2.2).

Proposition (7.8.5). — Sous les hypothèses de (7.8.4), les conditions suivantes sont équivalentes :

a) $\mathcal{P}_{\bullet}$ est homologiquement plat sur Y en toute dimension $i \leqslant p$.

b) Pour $i \leqslant p + 1$ les foncteurs $\mathcal{T}_i$ sont exacts à droite.

c) Pour $i \geqslant -p$, les $\mathcal{O}_{\mathrm{Y}}$-Modules $\mathcal{H}^i(f, \mathcal{P}^\bullet)$ sont localement libres.

L'équivalence de $a$) et $b$) est triviale (7.8.3) et $a$) entraîne $c$) en vertu de (7.8.4). Inversement, supposons $c$) vérifiée; notons d'autre part qu'on a $\mathcal{L}_{i}=0$ pour $i\leqslant i_{0}$ (7.7.4), donc aussi $\mathcal{T}_{i}=0$ pour $i\leqslant i_{0}$. Tout point $y\in Y$ a donc un voisinage affine $U=Spec(A)$ tel que $\mathrm{T}_{i}^{\mathrm{A}}(A)$ soit un A-module libre pour $i\leqslant p$; en vertu de (7.3.7), on en conclut que $\mathcal{T}_{i}^{\mathrm{U}}=\mathrm{T}_{i}^{\mathrm{A}}$ est exact pour $i\leqslant p$.

Nous allons surtout appliquer les critères de platitude cohomologique au cas où le complexe $\mathcal{P}_{\bullet}$ est réduit à un seul $\mathcal{O}_{\mathrm{X}}$-Module cohérent F plat sur Y, pris égal à $\mathcal{P}_{0}$; rappelons que l'on a alors $\mathcal{T}_{p}(\mathcal{M}) = \mathrm{R}^{-p}f_{*}(\mathcal{F}\otimes_{\mathcal{O}_{\mathrm{Y}}}\mathcal{M})$.

Proposition (7.8.6). — Soient Y un préschéma localement noethérien, $f: X \to Y$ un morphisme propre et plat, y un point de Y; désignons par $X_y$ la fibre $f^{-1}(y) = X \otimes_Y k(y)$. Supposons que $\Gamma(X_y, \mathcal{O}_{X_y}) = R$ soit une $k(y)$-algèbre séparable (Bourbaki, Alg., chap. VIII, § 7, n° 5) autrement dit composée d'un nombre fini d'extensions séparables de degré fini de $k(y)$. Alors $\mathcal{O}_X$ est cohomologiquement plat sur Y au point y en dimension o.

En vertu de (7.8.4), on peut se borner au cas où Y est le spectre de l'anneau local  $A = O_{y}$ ; l'hypothèse que f est plat entraîne  $T_{-1} = o$ , donc on voit déjà que  $T_{0}^{A}$  est exact à gauche et tout revient à voir qu'il est exact à droite; en vertu de (7.7.10 c)), on est même ramené au cas où  $A = O_{y}$  est artinien. Soit  $k'$  une extension finie de  $\boldsymbol{k}(y)$  qui soit un corps neutralisant de R, de sorte que  $\mathbf{R} \otimes_{\boldsymbol{k}(y)} k'$  est composée directe d'un nombre fini de corps isomorphes à  $k'$ . On sait qu'il existe un homomorphisme local de A dans un anneau local  $A'$ , faisant de  $A'$  une A-algèbre libre finie sur A, et tel que le corps résiduel de  $A'$  soit isomorphe à  $k'$  (0, 10.3.2). En vertu de (7.6.1), on est ramené à prouver que  $T_{0}^{A'}$  est exact à droite, autrement dit on peut supposer que R est composé direct de m corps isomorphes à  $\boldsymbol{k}(y)$ . Notons maintenant le lemme élémentaire suivant :

Lemme (7.8.6.1). — Soit Z un espace annelé en anneaux locaux ; pour que Z soit connexe,

il faut et il suffit que l'anneau $\Gamma(Z, \mathcal{O}_{Z})$ ne soit pas un produit de deux anneaux non réduits à o.

Il est clair en effet que si Z est réunion de deux ouverts non vides disjoints, $\Gamma(Z, \mathcal{O}_{\mathbb{Z}})$ est isomorphe au produit des deux anneaux $\Gamma(Z_1, \mathcal{O}_{\mathbb{Z}})$ et $\Gamma(Z_2, \mathcal{O}_{\mathbb{Z}})$ non réduits à o. Inversement, dire que $\Gamma(Z, \mathcal{O}_{\mathbb{Z}})$ est un tel produit équivaut à dire qu'il y a dans $\Gamma(Z, \mathcal{O}_{\mathbb{Z}})$ un idempotent $s$ distinct de o et de i; pour tout $z \in \mathbb{Z}$, $s_z$ est alors un idempotent dans $\mathcal{O}_z$, donc égal à o ou i. Mais il est clair que l'ensemble des $z$ tels que $s_z = o$ est ouvert; d'autre part, si $s_z = 1$, on a par définition $s(z) \neq 0$, donc l'ensemble des $z$ où $s_z = 1$ est aussi ouvert ($0_1, 5.5.2$); d'où la conclusion.

Il résulte de ce lemme que  $X_{y}$  a exactement m composantes connexes  $X_{i}^{\prime}$  et que  $\Gamma(\mathbf{X}_{i}^{\prime},\mathcal{O}_{\mathbf{X}_{i}^{\prime}})=\boldsymbol{k}(y)$  pour tout i. Comme A a été supposé local et artinien, son spectre est réduit à un point, donc X et  $X_{y}$  ont même espace sous-jacent; X a donc m composantes connexes  $X_{i}$  telles que  $\mathbf{X}_{i}^{\prime}=\mathbf{X}_{i}\otimes_{\mathbf{Y}}\boldsymbol{k}(y)$ . On est ainsi finalement ramené au cas où  $\mathbf{R}=\boldsymbol{k}(y)$ ; en vertu de (7.7.10, b)), on est ramené à prouver que l'homomorphisme canonique  $\Gamma(\mathbf{X},\mathcal{O}_{\mathbf{X}})\to\Gamma(\mathbf{X}_{y},\mathcal{O}_{\mathbf{X}_{y}})$  est surjectif; mais cela est trivial, car le composé

$$
\Gamma (\mathrm{Y}, \mathcal {O} _ {\mathrm{Y}}) = \mathrm{A} \rightarrow \Gamma (\mathrm{X}, \mathcal {O} _ {\mathrm{X}}) \rightarrow \Gamma (\mathrm{X} _ {y}, \mathcal {O} _ {\mathrm{X} _ {y}}) = \boldsymbol {k} (y)
$$

est déjà surjectif.

Corollaire (7.8.7). — Sous les hypothèses de (7.8.6), il existe un voisinage ouvert U de y tel que :

(i) $f_{*}(\mathcal{O}_{\mathrm{X}})|\mathrm{U}$ soit isomorphe à un $(\mathcal{O}_{\mathrm{Y}}|\mathrm{U})$-Module de la forme $(\mathcal{O}_{\mathrm{Y}}|\mathrm{U})^{m}$.

(ii) Pour tout $z\in\mathbf{U}$, l'homomorphisme canonique

$$
\left(f _ {*} (\mathcal {O} _ {\mathrm{X}})\right) _ {z} \otimes_ {\mathcal {O} _ {z}} \boldsymbol {k} (z) \rightarrow \Gamma (\mathrm{X} _ {z}, \mathcal {O} _ {\mathrm{X} _ {z}})
$$

est bijectif.

(i) résulte de (7.8.6) et (7.8.4).

(ii) résulte de ce que $\mathcal{T}_0^{\mathrm{U}}$ est exact (pour U convenablement choisi), et de (7.7.5.3).

Corollaire (7.8.8). — Supposons vérifiées les conditions de (7.8.6) et en outre que $\Gamma(\mathbf{X}_{y},\mathcal{O}_{\mathbf{X}_{y}})=\boldsymbol{k}(\mathcal{y})$. Alors il existe un voisinage ouvert U de y tel que l'homomorphisme canonique $\mathcal{O}_{\mathrm{Y}}|\mathrm{U}\to f_{*}(\mathcal{O}_{\mathrm{X}})|\mathrm{U}$ soit bijectif.

En effet, il résulte de (7.8.7, (ii)) que l'entier $m$ figurant dans (7.8.7, (i)) est nécessairement égal à 1.

Corollaire (7.8.9). — Sous les hypothèses de (7.8.6), il existe un voisinage ouvert U de y, un $\mathcal{O}_{\mathrm{U}}$-Module cohérent 2 (déterminé à isomorphisme unique près) et un isomorphisme de foncteurs en le $\mathcal{O}_{\mathrm{U}}$-Module quasi-cohérent M :

$$
\mathrm{R} ^ {1} f _ {*} (f ^ {*} (\mathcal {M})) \stackrel {{\sim}} {{\to}} \mathcal {H} o m _ {\mathcal {O} _ {\mathrm{U}}} (2, \mathcal {M}).\tag{7.8.9.1}
$$

En effet, l'hypothèse entraîne que $\mathcal{T}_{0}^{\mathrm{U}}$ est exact pour un U convenable; il suffit donc d'appliquer l'équivalence de $(7.7.5, a))$ et $(7.7.5, b')$ au cas $p = 0$ et en prenant pour $\mathcal{P}$. le complexe réduit à son terme de degré o égal à $\mathcal{O}_{\mathrm{x}}$.

Remarques (7.8.10). — (i) Sous les conditions de (7.8.6), considérons la factorisation de Stein de $f$ (4.3.3)

$$
\mathbf {X} \xrightarrow {f ^ {\prime}} \mathbf {Y} ^ {\prime} \xrightarrow {g} \mathbf {Y}
$$

avec  $Y' = \text{Spec}(f_{*}(\mathcal{O}_{X}))$ ; le morphisme fini g est alors tel que  $g_{*}(\mathcal{O}_{Y'}) = f_{*}(\mathcal{O}_{X})$  soit localement libre au voisinage de y, et sa fibre en y est le spectre d'une algèbre séparable sur  $\boldsymbol{k}(y)$  (II, I.5.I). Nous en déduirons au chap. IV qu'il y a un voisinage ouvert U de y dans Y tel que pour la restriction  $g^{-1}(U) \to U$  de g, toute fibre  $g^{-1}(z)$  (où  $z \in U$ ) soit spectre d'une algèbre séparable sur  $\boldsymbol{k}(z)$  (c'est ce que nous appellerons un revêtement étale de U); il résultera alors de (7.8.7, (ii)) que l'hypothèse faite sur le point y dans (7.8.6) est vérifiée aussi en tous les points d'un voisinage de y.

(ii) Nous verrons au chap. V que, même si X est projectif sur Y (et même s'il est en outre « simple » sur Y, propriété qui sera définie au chap. IV), le $\mathcal{O}_{\mathrm{U}}$-Module 2 de (7.8.9) n'est pas nécessairement localement libre; en d'autres termes, $\mathcal{O}_{\mathrm{X}}$ (sous ces conditions) n'est pas nécessairement cohomologiquement plat en dimension 1 sur Y au point y. Au chap. V, nous interpréterons 2 comme le faisceau des 1-différentielles du schéma de Picard de X par rapport à Y le long de la section unité.

## 7.9. Application aux morphismes propres : III. Invariance de la caractéristique d'Euler-Poincaré et du polynôme de Hilbert.

(7.9.1) Soient A un anneau, M un A-module projectif de type fini; rappelons (Bourbaki, Alg. comm., chap. II, § 5, n° 2) qu'il revient au même de dire que le $\mathcal{O}_{\mathrm{X}}$-Module associé $\widetilde{\mathbf{M}}$ sur $\mathbf{X} = \operatorname{Spec}(\mathbf{A})$ est localement libre de type fini. Pour tout $\mathfrak{p} \in \operatorname{Spec}(\mathbf{A})$ on appelle rang de M en $\mathfrak{p}$ et on note $\operatorname{rang}_{\mathfrak{p}}(\mathbf{M})$ le rang du $\mathbf{A}_{\mathfrak{p}}$-module libre $\mathbf{M}_{\mathfrak{p}}$ (ou encore le rang en $\mathfrak{p}$ du $\mathcal{O}_{\mathrm{X}}$-Module localement libre $\widetilde{\mathbf{M}}$). On a donc

$$
\operatorname{rang} _ {\mathfrak {p}} \mathrm{M} = \operatorname{rang} _ {\mathfrak {p}} (\mathrm{M} _ {\mathfrak {p}}) = \operatorname{rang} _ {\mathbf {k} (\mathfrak {p})} (\mathrm{M} \otimes_ {\mathrm{A}} \boldsymbol {k} (\mathfrak {p})).\tag{7.9.1.1}
$$

Proposition (7.9.2). — Soit P. un complexe fini de A-modules projectifs de type fini, et pour tout A-module M, soit T.(M) = H.(P.⊗A M). Alors, pour tout p∈Spec(A), on a

$$
\sum_ {i} (- \mathrm{I}) ^ {i} \operatorname{rang} _ {\mathbf {k} (\mathfrak {p})} \mathrm{T} _ {i} (\boldsymbol {k} (\mathfrak {p})) = \sum_ {i} (- \mathrm{I}) ^ {i} \operatorname{rang} _ {\mathfrak {p}} (\mathrm{P} _ {i}).\tag{7.9.2.1}
$$

En effet, on a par définition  $\mathrm{T}_{i}(\boldsymbol{k}(\mathfrak{p}))=\mathrm{H}_{i}(\mathrm{P}_{\bullet}\otimes_{\mathrm{A}}\boldsymbol{k}(\mathfrak{p}))$  et, compte tenu de (7.9.1.1), la formule (7.9.1.2) n'est autre que l'invariance de la caractéristique d'Euler-Poincaré d'un complexe fini d'espaces vectoriels de dimension finie par passage à l'homologie (0, II.10.2).

Corollaire (7.9.3). — La fonction

$$
\mathfrak {p} \sim \sum_ {i} (- \mathrm{r}) ^ {i} \operatorname{rang} _ {\mathbf {k} (\mathfrak {p})} \mathrm{T} _ {i} (\boldsymbol {k} (\mathfrak {p}))
$$

est localement constante dans $\operatorname{Spec}(\mathbf{A})$.

Théorème (7.9.4). — Soient Y un préschéma localement noethérien, $f: \mathbf{X} \to \mathbf{Y}$ un morphisme propre, $\mathcal{P}_{\bullet}$ un complexe fini de $\mathcal{O}_{\mathbf{X}}$-Modules cohérents et Y-plats. Si l'on pose $\mathcal{T}_{\bullet}(\mathcal{M}) = \mathcal{H}^{\bullet}(f, \mathcal{P}^{\bullet} \otimes_{\mathcal{O}_{\mathbf{X}}}\mathcal{M})$ (cf. (7.7.1.1)) la fonction

$$
(7. 9. 4. \mathbf {I})
$$

$$
y \sim \sum_ {i} (- 1) ^ {i} \operatorname{rang} _ {\mathbf {k} (y)} \mathrm{T} _ {i} (\boldsymbol {k} (y))
$$

est localement constante dans Y.

On peut se borner au cas où $Y = \text{Spec}(A)$ est affine d'anneau A noethérien. Comme le complexe $\mathcal{P}_{\bullet}$ est fini, on sait (7.7.12, (i)) qu'on a $\mathcal{T}_p(\mathcal{M}) = \mathcal{H}_p(\mathcal{L}_{\bullet} \otimes_{\mathcal{O}_Y} \mathcal{M})$, où $\mathcal{L}_{\bullet} = \widetilde{\mathrm{L}}_{\bullet}$, $L_{\bullet}$ étant un complexe fini de A-modules projectifs de type fini. Le théorème résulte alors de (7.9.3).

(7.9.5) Sous les conditions de (7.9.4), la fonction (7.9.4.1) est constante lorsque Y est connexe. Lorsque Y est connexe et non vide, on désigne la valeur unique (entière) de (7.9.4.1) par EP(f, P.) ou EP(Y, P.), ou simplement EP(P.) s'il ne peut en résulter de confusion, et l'on dit que cet entier est la caractéristique d'Euler-Poincaré de P. relativement à f (ou à Y). Dans le cas général, on notera aussi EP(f, P.; y) ou EP(Y, P.; y) ou EP(P.; y) le second membre de (7.9.4.1).

(7.9.6) Sous les hypothèses de (7.9.4) relativement à X, Y et f, soit

$$
0 \to \mathcal {P} _ {\bullet} ^ {\prime} \stackrel {u} {\to} \mathcal {P} _ {\bullet} \stackrel {v} {\to} \mathcal {P} _ {\bullet} ^ {\prime \prime} \to 0
$$

une suite exacte de complexes finis de $\mathcal{O}_{\mathrm{X}}$-Modules cohérents et Y-plats, les homomorphismes $u$ et $v$ étant de degrés pairs $2d$, $2d'$ respectivement. Comme $\mathcal{T}$. est un foncteur homologique (7.7.1), on a une suite exacte d'homologie

$$
\rightarrow \mathcal {T} _ {i} (\mathcal {P} _ {\bullet} ^ {\prime}, \boldsymbol {k} (y)) \rightarrow \mathcal {T} _ {i + 2 d} (\mathcal {P} _ {\bullet}, \boldsymbol {k} (y)) \rightarrow \mathcal {T} _ {i + 2 d + 2 d ^ {\prime}} (\mathcal {P} _ {\bullet} ^ {\prime \prime}, \boldsymbol {k} (y)) \rightarrow \mathcal {T} _ {i - 1} (\mathcal {P} _ {\bullet} ^ {\prime}, \boldsymbol {k} (y)) \rightarrow \dots
$$

n'ayant d'ailleurs qu'un nombre fini de termes. En écrivant que la caractéristique d'Euler-Poincaré de ce complexe est nulle (0, 11.10.1), il vient aussitôt

$$
\mathrm{EP} (\mathcal {P} _ {\bullet}; y) = \mathrm{EP} (\mathcal {P} _ {\bullet} ^ {\prime}; y) + \mathrm{EP} (\mathcal {P} _ {\bullet} ^ {\prime \prime}; y)\tag{7.9.6.r}
$$

pour tout $y\in Y$. Or, si par exemple $\mathcal{P}_{\bullet}=(\mathcal{P}_{i})$ avec $\mathcal{P}_{i}=0$ pour $i<0$, on a la suite exacte de complexes

$$
\begin{array}{c} \dots \to 0 \to 0 \longrightarrow 0 \longrightarrow 0 \longrightarrow \dots \\ \downarrow \quad \downarrow \quad \downarrow \quad \downarrow \\ \dots \to 0 \to 0 \longrightarrow \mathcal {P} _ {1} \to \mathcal {P} _ {2} \to \dots \\ \downarrow \quad \downarrow \quad \downarrow \quad \downarrow \\ \dots \to 0 \to \mathcal {P} _ {0} \to \mathcal {P} _ {1} \to \mathcal {P} _ {2} \to \dots \\ \downarrow \quad \downarrow \quad \downarrow \quad \downarrow \\ \dots \to 0 \to \mathcal {P} _ {0} \to 0 \longrightarrow 0 \longrightarrow \dots \\ \downarrow \quad \downarrow \quad \downarrow \quad \downarrow \\ \dots \to 0 \to 0 \longrightarrow 0 \longrightarrow 0 \longrightarrow \dots \end{array}\tag{7.9.6.2}
$$

les flèches verticales non nulles étant les automorphismes identiques; on peut appliquer (7.9.6.1) à cette suite exacte, d'où, par récurrence sur la longueur de $\mathcal{P}_{\bullet}$, la formule

$$
\mathrm{EP} (\mathcal {P} _ {\bullet}; y) = \Sigma (- \mathrm{i}) ^ {i} \mathrm{EP} (\mathcal {P} _ {i}; y)\tag{209}
$$

où, pour tout $\mathcal{O}_{\mathrm{X}}$-Module cohérent $\mathcal{F}$, plat sur Y, on désigne par $\mathrm{EP}(\mathcal{F};y)$ (ou $\mathrm{EP}(f,\mathcal{F};y)$ ou $\mathrm{EP}(\mathrm{Y},\mathcal{F};y)$) la fonction $\mathrm{EP}(\mathcal{Q};y)$ correspondant au complexe $\mathcal{Q}$. dont le seul terme $\neq$ o est de degré o et égal à $\mathcal{F}$. On voit donc qu'on peut se ramener à étudier les caractéristiques d'Euler-Poincaré de complexes réduits à un seul terme.

Proposition (7.9.7). — Sous les hypothèses de (7.9.4), soient Y' un préschéma localement noethérien,  $g: Y' \to Y$  un morphisme,  $X' = X \times_{Y} Y'$ ,  $f' = f_{(Y')} : X' \to Y'$ ,  $P'$  le complexe fini  $P_{\bullet} \otimes_{O_{Y}} O_{Y'}$  de  $O_{X'}$ -Modules;  $P'$  est formé de  $O_{X'}$ -Modules cohérents et Y'-plats, et pour tout  $y' \in Y'$ , on a

$$
\operatorname{EP} \left(\mathscr {P} _ {\bullet} ^ {\prime}; y ^ {\prime}\right) = \operatorname{EP} \left(\mathscr {P} _ {\bullet}; g \left(y ^ {\prime}\right)\right).\tag{7.9.7.1}
$$

Les $\mathcal{O}_{\mathrm{X}^{\prime}}$-Modules $\mathcal{P}_i^{\prime}$ étant images réciproques des $\mathcal{P}_i$ par la projection $\mathbf{X}^{\prime} \to \mathbf{X}$ sont cohérents, ils sont $\mathbf{Y}^{\prime}$-plats en vertu de $(\mathbf{0}_1, 6.2.1)$ et (1.4.14.5), la question étant locale sur $\mathbf{X}, \mathbf{Y}$ et $\mathbf{Y}^{\prime}$; enfin, on sait que $f^{\prime}$ est propre (II, 5.4.2), donc le premier membre de (7.9.7.1) est défini. La formule (7.9.7.1) résulte alors de (6.10.4.2), (7.7.2) et du lemme (7.6.7), en se ramenant, comme on peut toujours le faire, au cas où $\mathbf{Y}$ et $\mathbf{Y}^{\prime}$ sont affines.

Proposition (7.9.8). — Supposons vérifiées les hypothèses de (7.9.4) et en outre qu'il existe un entier $i_{0}$ tel que $\mathrm{T}_{i}(\boldsymbol{k}(y)) = 0$ pour $i \neq i_{0}$ et tout $y \in \mathbf{Y}$. Alors $\mathcal{T}_{i_{0}}(\mathcal{O}_{\mathbf{Y}}) = \mathcal{H}^{-i_{0}}(f, \mathcal{P}_{\bullet})$ est un $\mathcal{O}_{\mathbf{Y}}$-Module localement libre, dont le rang en $y \in \mathbf{Y}$ est égal à $(-1)^{i_{0}}\mathrm{EP}(f, \mathcal{P}_{\bullet}; y)$.

Remarquons d'abord que les hypothèses de (7.4.4) sont vérifiées par les  $T_{j}^{\mathcal{O}y}$ , donc (7.4.7) leur est applicable, et l'hypothèse entraîne que  $T_{i}^{\mathcal{O}y}$  est nul pour  $i \neq i_{0}$  en vertu de (7.5.3); en raison de (7.3.3),  $T_{i_{0}}$  est donc aussi exact, et par suite (7.8.4),  $\mathcal{H}^{-i_{0}}(f, \mathcal{P}_{\bullet})$  est localement libre et son rang en un point  $y \in Y$  est

$$
\operatorname{rang} _ {\mathbf {k} (y)} \mathrm{T} _ {i _ {0}} (\boldsymbol {k} (y)) = \mathrm{EP} (f, \mathscr {P} _ {\bullet}; y)
$$

par définition, puisque $\mathbf{T}_i(\pmb{k}(\mathcal{Y})) = 0$ pour $i \neq i_0$.

Corollaire (7.9.9). — Soient Y un préschéma localement noethérien, $f: \mathbf{X} \to \mathbf{Y}$ un morphisme propre, $\mathcal{F}$ un $\mathcal{O}_{\mathrm{X}}$-Module cohérent et Y-plat; on suppose qu'il existe un entier $i_0$ tel que $\mathbf{H}^i(f^{-1}(y), \mathcal{F} \otimes_{\mathcal{O}_\mathbf{Y}} \mathbf{k}(y)) = 0$ pour tout $i \neq i_0$ et tout $y \in \mathbf{Y}$. Alors $\mathbf{R}^{i_0} f_*(\mathcal{F})$ est un $\mathcal{O}_{\mathrm{Y}}$-Module localement libre, dont le rang en $y$ est égal à $(-1)^{i_0} \mathrm{EP}(f, \mathcal{F}; y)$.

En particulier :

Corollaire (7.9.10). — Sous les conditions préliminaires de (7.9.9) pour X, Y et F, supposons que l'on ait  $\mathrm{R}^{i}f_{*}(\mathcal{F})=\mathrm{o}$  pour tout i>0. Alors  $f_{*}(\mathcal{F})$  est un  $O_{Y}$ -Module localement libre, dont le rang en y est égal à  $\mathrm{EP}(f,\mathcal{F};y)$ .

Il suffira, en vertu de (7.9.9) de prouver le lemme suivant :

Lemme (7.9.10.1). — Sous les hypothèses de (7.9.10), on a  $\mathrm{H}^{i}(f^{-1}(y), \mathcal{F} \otimes_{\mathcal{O}_{\mathbf{Y}}} \boldsymbol{k}(y)) = 0$  pour tout i > 0 et tout  $y \in Y$ .

En effet, on peut se borner au cas où  $Y = \text{Spec}(A)$  est affine. Avec les notations de (7.9.4), et P. étant réduit à son terme de degré o égal à F, on a en effet  $\mathcal{T}_{p}(\mathcal{O}_{Y}) = 0$  pour p < 0 par hypothèse; on conclut de (7.3.7) que  $T_{p}$  est exact pour p < 0, et le lemme résulte alors de l'équivalence de (7.7.5, a)) et (7.7.5, d)).

211

Proposition (7.9.11). — Les hypothèses étant celles de (7.9.4), soit $\mathcal{L}$ un $\mathcal{O}_{\mathrm{X}}$-Module inversible très ample pour Y, et posons $\mathcal{P}_{\bullet}(n)=\mathcal{P}_{\bullet}\otimes_{\mathcal{O}_{\mathrm{X}}}\mathcal{L}^{\otimes n}$ pour tout $n\in\mathbf{Z}$. Alors, pour tout $y\in\mathbf{Y}$, la fonction

$$
n \rightsquigarrow \mathrm{EP} (f, \mathscr {P} _ {\bullet} (n); y)\tag{7.9.II.I}
$$

est un polynôme à coefficients dans Q, qui est le même pour tous les points d'une même composante connexe de Y.

Il est clair que $\mathcal{P}_{\bullet}(n)$ est un complexe de $\mathcal{O}_{\mathrm{X}}$-Modules Y-plats. En vertu de (7.9.6.2), on peut se borner au cas où $\mathcal{P}_{\bullet}$ est réduit à un seul terme $\mathcal{F} \neq 0$ de degré o; en outre, comme il s'agit de questions locales sur Y, on peut supposer Y affine et $f$ projectif (II, 5.5.3); posons $\mathbf{X}_y = f^{-1}(y)$, et soit $\mathcal{L}_y = \mathcal{L} \otimes_{\mathcal{O}_Y} \boldsymbol{k}(y)$, qui est un $\mathcal{O}_{\mathrm{X}_y}$-Module très ample (II, 4.4.10); en vertu de (7.7.2), on a, pour le foncteur $\mathcal{T}_{\bullet}$ relatif au complexe $\mathcal{P}_{\bullet}(n)$, $\mathrm{T}_i(\boldsymbol{k}(y)) = \mathrm{H}^{-i}(\mathrm{X}_y, \mathcal{F}_y \otimes \mathcal{L}_y^{\otimes n})$ (où $\mathcal{F}_y = \mathcal{F} \otimes_{\mathcal{O}_Y} \boldsymbol{k}(y)$); d'où résulte que $\mathrm{EP}(f, \mathcal{F}(n); y)$ n'est autre que la caractéristique d'Euler-Poincaré $\chi_{\boldsymbol{k}(y)}(\mathcal{F}_y(n))$ définie dans (2.5.1); le fait que (7.9.11.1) soit un polynôme résulte alors de (2.5.3); en outre, pour chaque $n$, sa valeur est constante dans une composante connexe de Y (7.9.4), ce qui achève la démonstration.

Nous désignerons par $\mathrm{PH}(f, \mathcal{P}_{\bullet}; y)$ ou $\mathrm{PH}(\mathcal{P}_{\bullet}; y)$ le polynôme (7.9.11.1), à coefficients rationnels, et nous dirons que c'est le polynôme de Hilbert en $y$ relatif à $\mathcal{P}_{\bullet}$, $f$ et $\mathcal{L}$ (ou simplement le polynôme de Hilbert en $y$ de $\mathcal{P}_{\bullet}$, ou de $f$, s'il n'en résulte pas de confusion); lorsque Y est connexe non vide, on supprime la mention de $y$ dans la notation et la terminologie. L'invariant ainsi obtenu jouera un rôle essentiel au chap. V, dans la théorie des « modules » des faisceaux cohérents quotients d'un faisceau cohérent donné.

(7.9.12) Avec les notations de (7.9.6) et (7.9.11), on a

$$
\mathrm{PH} \left(\mathscr {P} _ {\bullet}; y\right) = \mathrm{PH} \left(\mathscr {P} _ {\bullet} ^ {\prime}; y\right) + \mathrm{PH} \left(\mathscr {P} _ {\bullet} ^ {\prime \prime}; y\right)\tag{7.9.12.1}
$$

et en particulier

$$
\mathrm{PH} (\mathcal {P} _ {\bullet}; y) = \sum_ {i} (- 1) ^ {i} \mathrm{PH} (\mathcal {P} _ {i}; y);\tag{7.9.12.2}
$$

cela résulte trivialement de (7.9.6.1) et (7.9.6.2). De même, avec les notations et hypothèses de (7.9.7), on a

$$
\mathrm{PH} \left(\mathcal {P} _ {\bullet} ^ {\prime}; y ^ {\prime}\right) = \mathrm{PH} \left(\mathcal {P} _ {\bullet}; g \left(y ^ {\prime}\right)\right).\tag{7.9.12.3}
$$

La formule (7.9.12.2) ramène l'étude des polynômes de Hilbert d'un complexe à celle des polynômes de Hilbert d'un seul $\mathcal{O}_{\mathrm{x}}$-Module Y-plat. Ces derniers admettent une interprétation remarquable indépendante de considérations homologiques :

Corollaire (7.9.13). — Soient Y un préschéma noethérien, $f: \mathbf{X} \to \mathbf{Y}$ un morphisme propre, $\mathcal{L}$ un $\mathcal{O}_{\mathrm{X}}$-Module inversible très ample pour Y, $\mathcal{F}$ un $\mathcal{O}_{\mathrm{X}}$-Module cohérent et Y-plat. Il existe un entier $n_0$ tel que pour $n \geqslant n_0$, $f_*(\mathcal{F}(n))$ soit un $\mathcal{O}_{\mathrm{Y}}$-Module localement libre, de rang en $y \in \mathbf{Y}$ égal à $\mathrm{PH}(f, \mathcal{F}; y)(n)$.

Comme le morphisme $f$ est projectif (II, 5.5.3), il existe $n_{0}$ tel que pour $n \geqslant n_{0}$

on ait  $\mathrm{R}^{if}_{*}(\mathcal{F}(n))=0$  pour tout i>0 (2.2.1); la conclusion résulte donc de (7.9.10). Le critère de platitude suivant sera important dans la théorie des « modules » des faisceaux cohérents du chap. V :

Proposition (7.9.14). — Soient Y un préschéma noethérien, $f: \mathbf{X} \to \mathbf{Y}$ un morphisme projectif, $\mathcal{L}$ un $\mathcal{O}_{\mathrm{X}}$-Module inversible ample pour $f$, et posons $\mathcal{F}(n) = \mathcal{F} \otimes \mathcal{L}^{\otimes n}$ pour tout $\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{F}$ et tout $n \in \mathbf{Z}$. Pour qu'un $\mathcal{O}_{\mathrm{X}}$-Module cohérent $\mathcal{F}$ soit Y-plat, il faut et il suffit qu'il existe un entier $n_0$ tel que, pour tout $n \geqslant n_0$, $f_*(\mathcal{F}(n))$ soit un $\mathcal{O}_{\mathrm{Y}}$-Module localement libre.

La nécessité de la condition se démontre comme dans (7.9.13) (le résultat de (2.2.1) s'appliquant à un faisceau ample $\mathcal{L}$, puisque $f$ est projectif). Pour démontrer la réciproque, on peut se borner au cas où Y est affine d'anneau A; en vertu de l'hypothèse et de (2.2.2, (i)), les A-modules $\Gamma(\mathbf{X},\mathcal{F}(n))$ sont de type fini et projectifs (Bourbaki, Alg. comm., chap. II, § 5, n° 2, th. 1). Soit S l'anneau gradué $\bigoplus_{n\geqslant0}\Gamma(\mathbf{X},\mathcal{L}^{\otimes n})$; on sait que X s'identifie canoniquement à Proj(S) (II, 4.5.2, (b) et 5.4.4). Soit $\mathbf{M}=\bigoplus_{n\geqslant n_0}\Gamma(\mathbf{X},\mathcal{F}(n))$; remplaçant au besoin $\mathcal{L}$ par une puissance $\mathcal{L}^{\otimes d}$, on peut supposer que S est engendré par un nombre fini d'éléments de degré I (2.3.5.1), et il résulte alors de (II, 2.7.5 et 2.7.2) que $\mathcal{F}$ s'identifie à Proj$_0(\mathbf{M})$. Pour tout élément homogène $g\in\mathbf{S}$ de degré >0, on a donc $\Gamma(\mathbf{X}_g,\mathcal{F})=\mathbf{M}_{(g)}$; or, M, somme directe de A-modules projectifs, est un A-module plat, donc il en est de même de $\mathbf{M}_g$ ($\mathbf{0}_I$, 6.3.2), et par suite aussi de $\mathbf{M}_{(g)}$, qui est un facteur direct de $\mathbf{M}_g$ ($\mathbf{0}_I$, 6.1.2). On en conclut (1.4.14.5) que $\mathcal{F}$ est Y-plat en tout point de $\mathbf{X}_g$, et comme les $\mathbf{X}_g$ recouvrent X, la proposition est démontrée.

(A suivre.)

$$
\mathbf {T o r} _ {n} ^ {\mathrm{A}} \left(\mathrm{P} _ {\bullet}, \mathrm{Q} _ {\bullet}\right) ^ {\prime}: 6. 3. 1.
$$

$$
\mathcal {C o r} _ {n} ^ {\mathcal {O} _ {\mathrm{S}}} (\mathcal {P} _ {\bullet}, \mathfrak {Z} _ {\bullet}), \mathcal {C o r} _ {n} ^ {\mathrm{S}} (\mathcal {P} _ {\bullet}, \mathfrak {Z} _ {\bullet}): 6. 4. \mathrm{I} \text {   et   } 6. 5. \mathrm{I}.
$$

$$
\mathcal {T} o r _ {n} ^ {\mathrm{S}} (\mathcal {F}, \mathcal {G}): 6. 5. \mathrm{I}.
$$

$$
\mathfrak {C o r} _ {q} ^ {\mathrm{S}} (\mathcal {P} _ {\bullet} ^ {(1)}, \mathcal {P} _ {\bullet} ^ {(2)}, \dots , \mathcal {P} _ {\bullet} ^ {(m)}): 6. 5. 1 5.
$$

$$
\mathbf {H} ^ {- n} \left(\mathfrak {U} ^ {(i)}, \mathscr {P} _ {\bullet} ^ {(i)}\right), \mathbf {H} ^ {- n} \left(\mathrm{X} ^ {(i)}, \mathscr {P} _ {\bullet} ^ {(i)}\right): 6. 6. 1.
$$

$$
\mathbf {T o r} _ {n} ^ {\mathrm{A}} (\mathrm{L} _ {\bullet \bullet} ^ {(1)}, \mathrm{L} _ {\bullet \bullet} ^ {(2)}), \mathbf {T o r} _ {n} ^ {\mathrm{S}} (\mathfrak {U} ^ {(1)}, \mathfrak {U} ^ {(2)}; \mathcal {P} _ {\bullet} ^ {(1)}, \mathcal {P} _ {\bullet} ^ {(2)}): 6. 6. 2.
$$

$$
\mathcal {T o r} _ {n} ^ {\mathrm{S}} (\mathfrak {U} ^ {(1)}, \mathfrak {U} ^ {(2)}; \mathcal {F} ^ {(1)}, \mathcal {F} ^ {(2)}), \mathcal {T o r} _ {n} ^ {\mathrm{S}} (\mathfrak {U} ^ {(1)}, \mathfrak {U} ^ {(2)}; \mathcal {P} _ {\bullet} ^ {(1)}, \mathcal {P} _ {\bullet} ^ {(2)}): 6. 6. 2.
$$

$$
\mathfrak {C o r} _ {n} ^ {\mathrm{S}} (f _ {1}, f _ {2}; \mathscr {P} _ {\bullet} ^ {(1)}, \mathscr {P} _ {\bullet} ^ {(2)}): 6. 6. 8, 6. 7. \text {   i   et   } 6. 7. 3.
$$

$$
\mathfrak {E} o r _ {n} ^ {\mathrm{S}} ((f _ {i}) _ {i \in \mathrm{I}}; (\mathscr {P} _ {\bullet} ^ {(i)}) _ {i \in \mathrm{I}}), \mathfrak {E} o r _ {n} ^ {\mathrm{S}} (f _ {1}, \dots , f _ {m}; \mathscr {P} _ {\bullet} ^ {(1)}, \dots , \mathscr {P} _ {\bullet} ^ {(m)}): 6. 7. 1 1.
$$

$$
\boldsymbol {A} \boldsymbol {b}, \boldsymbol {A} \boldsymbol {b} _ {\mathrm{A}}: 7. \mathrm{I}. \mathrm{I}.
$$

$$
\mathrm{T} _ {(\mathrm{B})}, \mathrm{T} ^ {(\mathrm{B})}, \mathrm{T} \otimes_ {\mathrm{A}} \mathrm{B} (\mathrm{T} \text { foncteur   de } A b _ {\mathrm{A}} \text { dans } A b): 7. 1. 3.
$$

$$
t _ {\mathbf {M}}: 7. 2. 2.
$$

$$
\mathrm{T} _ {\mathfrak {p}}: 7. \mathrm{I}. 4.
$$

$$
\mathcal {T} _ {\bullet} ^ {\mathrm{Y} ^ {\prime}} (\mathcal {M} ^ {\prime}), \mathcal {T} _ {\bullet} ^ {\mathrm{U}} (\mathcal {M} | \mathrm{U}): 7. 7. 2.
$$

$$
\operatorname{EP} (f, \mathscr {P} _ {\bullet}; y), \operatorname{EP} (\mathrm{Y}, \mathscr {P} _ {\bullet}; y), \operatorname{EP} (\mathscr {P} _ {\bullet}; y): 7. 9. 5.
$$

$$
\mathrm{PH} (f, \mathscr {P} _ {\bullet}; y), \mathrm{PH} (\mathscr {P} _ {\bullet}; y): 7. 9. 1 2.
$$

# INDEX TERMINOLOGIQUE

Caractéristique d'Euler-Poincaré d'un complexe de Modules : 7.9.5.

Cohomologiquement plat en un point $y \in \mathbf{Y}$ en dimension $p$, cohomologiquement plat sur $\mathbf{Y}$ en dimension $p$, cohomologiquement plat sur $\mathbf{Y}$ au point $y$, cohomologiquement plat sur $\mathbf{Y}$ (complexe de $c_{\mathbf{X}}$-Modules Y-plats): 7.8.1.

Complexes homotopes : 6.1.4.

Espace annelé de dimension cohomologique $\leqslant n:6.5.5$.

Extension des scalaires dans un foncteur covariant additif : 7.1.3.

Faisceau d'anneaux de dimension cohomologique $\leqslant n:6.5.5$.

Formule de Künneth : 6.7.8.

Homologiquement plat en un point $y \in \mathbf{Y}$ en dimension $p$, homologiquement plat sur $\mathbf{Y}$ en dimension $p$, homologiquement plat sur $\mathbf{Y}$ au point $y$, homologiquement plat sur $\mathbf{Y}$ (complexe de $\mathfrak{O}_{\mathbf{X}}$-Modules Y-plats): 7.8.1. Homotopisme : 6.1.4.

Hypertor de deux complexes de A-modules : 6.3.1.

Hypertor local de deux complexes de Modules : 6.4.1.

Hypertor global de deux complexes de Modules : 6.6.2, 6.6.8 et 6.7.3.

Polynôme de Hilbert relatif à un complexe de Modules : 7.9.12.

Suites spectrales de Künneh : 6.7.3.

## TABLE DES MATIÈRES

CHAPITRE III. — Étude cohomologique des faisceaux cohérents (suite) 5
§ 6. Foncteurs Tor locaux et globaux; formule de Künneith .....
6.1. Introduction .....
6.2. Hypercohomologie des complexes de Modules sur un préschéma.
6.3. Hypertor de deux complexes de modules.....
6.4. Foncteurs hypertor locaux de complexes de Modules quasi-cohérents; cas des schémas affines.....
6.5. Foncteurs hypertor locaux de complexes de Modules quasi-cohérents : cas général.....
6.6. Foncteurs hypertor globaux de complexes de Modules quasi-cohérents et suites spectrales de Künneith : cas de la base affine..
6.7. Foncteurs hypertor globaux de complexes de Modules quasi-cohérents et suites spectrales de Künneith : cas général.....
6.8. Les suites spectrales d'associativité des hypertor globaux.....
6.9. Les suites spectrales de changement de base dans les hypertor globaux.....
6.10. Structure locale de certains foncteurs cohomologiques.....
§ 7. Étude du changement de base dans les foncteurs homologiques covariants de Modules.....
7.1. Foncteurs de A-modules.....
7.2. Caractérisation du foncteur produit tensoriel.....
7.3. Critères d'exactitude des foncteurs homologiques de modules.
7.4. Critères d'exactitude pour les foncteurs H.(P.⊗A M).....
7.5. Cas des anneaux locaux noethériens.....
7.6. Descente des propriétés d'exactitude. Théorème de semi-continuité et critère d'exactitude de Grauert.....
7.7. Application aux morphismes propres : I. La propriété d'échange.
7.8. Application aux morphismes propres : II. Critères de platitude cohomologique.....
7.9. Application aux morphismes propres : III. Invariance de la caractéristique d'Euler-Poincaré et du polynôme de Hilbert..
5
14
16
21
25
32
34
39
43
43
44
48
53
58
60
65
72
76

The Ground Truth image displays a single, solid horizontal line. According to Rule 2 (UNDERSCORE & LINE RULES), this is a stylistic or background line, not a placeholder underscore. Therefore, the OCR result must ignore it. The provided OCR content is "\_\_\_\_", which consists of four underscores. This is an incorrect interpretation of the line as a placeholder, violating the rule that stylistic lines must be ignored. The OCR has hallucinated text (underscores) where none should exist in the GT. This adheres to the strict requirement to ignore stylistic lines and not output any underscores. Hence, the OCR result is inconsistent with the Ground Truth.

## ERRATA ET ADDENDA

## (Liste 2)

## A) Erreurs typographiques

$(0_{1}, 3.2.1)$ Ligne 2 de la p. 27, remplacer X par U.

$(0_{I}, 3.2.6)$ Ligne $i$ du bas de la p. 27 et ligne $i$ de la p. 28, remplacer (3 fois) $\mathfrak{H}_{\lambda}$ par $\mathcal{H}_{\lambda}$.

$(0_{1}, 3.4.5)$ Ajouter une parenthèse devant $3.4.5$.

$(0_{I}, 4.2.1)$ Ligne 10 de la p. 39, remplacer $\psi_{*}(A)$ par $\psi_{*}(\mathcal{A})$.

$(0_{I}, 5.1.3)$ Ligne 16 de la p. 45, remplacer $\mathcal{F} | V$ par $\mathcal{F} | U$.

(0$_{1}$, 5.3.9) Ligne 12 de la p. 48, avant « telle que », ajouter : au-dessus d'un voisinage ouvert U de x.

(0, 7.6.9) Ligne 3 du bas de la p. 73, remplacer Jλ par ℑλ.

(I, i.i.15) Ligne 3 de la p. 83, remplacer a par a≠A.

(I, I.4.I) Ligne 2 du bas de la p. 90, remplacer $\widetilde{\mathbf{N}}$ par N.

(I, 2.3.1) Ligne 3 de la p. 101, remplacer (0, 4.1.6) par (0, 4.1.7).

(I, 2.3.2) Ligne II de la p. 101, remplacer B par  $B_{s}$  et C par  $C_{t}$ .

(I, 2.5.5) Ligne 19 de la p. 104, remplacer S-morphisme par S-préschéma.

(I, 3.3.7) Ligne 17 de la p. 109, remplacer  $Y_{(S)}$  par  $Y_{(S')}$ .

(I, 3.4.5) Ligne 9 de la p. 113, remplacer s par s.

(I, 3.4.8) Ligne 4 de la p. 114, remplacer $p(x)$ par $f(x)$.

(I, 3.5.1) Ligne 3 de la p. 115, remplacer $\mathrm{I_X}\times g$ par $\mathrm{I_{X'}}\times g$.

(I, 3.7.2) Ligne 8 de la p. 119, remplacer le premier X par X'.

(I, 4.2.2) Ligne 8 de la p. 123, dans la flèche verticale de gauche du diagramme, remplacer $\alpha_{\psi(y)}$ par $\rho_{\psi(y)}$.

(I, 4.4.3) Ligne 16 de la p. 126, remplacer isomorphee par isomorphes.

(I, 4.5.5) Ligne 17 du bas de la p. 127, remplacer (4.2.4) par (4.2.5).

(I, 5.1.4) Ligne 14 du bas de la p. 128, remplacer (2.1.7) par (2.1.8).

(I, 5.3.13) Ligne 20 de la p. 134, remplacer (4.2.4) par (4.2.5).

(I, 6.4.2) Ligne i du bas de la p. 147, remplacer recouvrement par recouvrement fini.

(I, 9.1.13) Ligne 15 de la p. 171, remplacer $p^{-1}(\mathcal{F})$ par $p^{*}(\mathcal{F})$.

(I, 9.5.11) Ligne 7 de la p. 179, remplacer Y par Y'.

(I, 9.6.5) Ligne 17 du bas de la p. 180, remplacer (0, 4.1.4) par (0, 4.1.3).

(I, 10.12.2) Ligne 14 du bas de la p. 206, remplacer $(\mathbf{X}_n)_{(\mathbb{S}_n)}$ par $(\mathbf{X}_n)_{(\mathbb{S}_m)}$.

(I), Index terminologique : Ligne 6 du bas de la p. 219, remplacer 0, 4.1.4 par 0, 4.1.5. Lignes 16, 17, 18 du bas de la p. 222, remplacer I, 2.1.7 par I, 2.1.8 ; ligne 19 du bas de la p. 222, remplacer I, 2.1.8 par I, 2.1.7.

(II, 1.5.2) Ligne 17 de la p. 12, insérer un f à côté de la flèche verticale de gauche du diagramme.

(II, 4.2.7) Ligne 16 du bas de la p. 75, remplacer (III, 2.1.14) par (III, 2.1.13).

(II, 5.2.1) Ligne 16 du bas de la p. 97, remplacer X—U par U. Ligne 8 du bas de la p. 97, remplacer  $X^{f}$  par  $X_{f}$ .

(II, 5.3.6) Ligne 16 de la p. 100, remplacer (4.6.18) par (4.6.17).

(II, 6.2.7) Ligne 9 du bas de la p. 116, remplacer chap. V par chap. IV.

(II, 6.6.5) Ligne 15 du bas de la p. 132, remplacer chap. V par chap. IV.

(II, 7.4.12) Ligne i de la p. 151, remplacer chap. V par chap. III.

(II, 8.1.4) Ligne 15 de la p. 154, remplacer (III, 2.3.8) par (III, 2.3.7).

(II, 8.10.5) Ligne 17 du bas de la p. 187, remplacer $g_{(j)x}$ par $g_{j(x)}$.

$(0_{\mathrm{III}}, 10.2.7)$ Ligne 1 de la p. 20, remplacer u-adique par n-adique. Ligne 13 du bas de la p. 20, remplacer k par $k_i$.

$(0_{\mathrm{III}}, \mathbf{II}.\mathbf{I}.\mathbf{I})$ Ligne 18 de la p. 23, remplacer $\operatorname{Im}(d_r^{p + r,q - r + 1})$ par $\operatorname{Im}(d_r^{p - r,q + r - 1})$.

(0III, 11.8.6) Ligne 14 du bas de la p. 45, remplacer les flèches → par ↗ (4 fois).

$(0_{\mathrm{III}}, 12.3.4)$ Ligne 4 de la p. 61, remplacer $\stackrel{\sim}{\rightarrow}$ par $\rightarrow$.

$(0_{\mathrm{III}}, 13.2.4)$ Ligne 2 du bas de la p. 67, remplacer lim par lim (2 fois).

(III, 1.1.7) Ligne 15 de la p. 85, remplacer $\mathbf{A}^r$ par $\wedge (\mathring{\mathbf{A}}^r)$ (2 fois).

(III, 1.2.4) Ligne 7 de la p. 87, remplacer $\Gamma(\mathbf{U},\mathcal{F})$ par $\Gamma(\mathbf{U},\mathcal{O}_{\mathrm{X}})$ et remplacer $\mathcal{G}$ par $\mathcal{F}$. Ligne 8 de la p. 87, remplacer $\mathbf{H}^{p}(\mathfrak{U},\mathcal{G})$ par $\mathbf{H}^{p}(\mathfrak{U},\mathcal{F})$.

(III, 2.5.3.1) Ligne 3 de la p. III, remplacer n>0 par  $n \geqslant 0$ . Ligne 8 de la p. III, remplacer  $-r \leqslant n \leqslant 0$  par  $-r \leqslant n < 0$ .

(III, 3.1.2) Ligne 13 de la p. 116, remplacer $\mathcal{G}$ par $\mathcal{G} \in K'$.

(III, 4.3.6) Ligne 7 de la p. 133, remplacer $\mathbf{K}' = \mathbf{K} \otimes_{\mathbf{A}} \hat{\mathbf{A}}$ par $\mathbf{K}' \supset \mathbf{K} \otimes_{\mathbf{A}} \hat{\mathbf{A}}$. Ligne 16 de la p. 133, remplacer $\mathbf{R}(\mathbf{X})$ par $\mathbf{R}(\mathbf{Y})$.

(III, 4.4.12) Ligne 10 de la p. 138, remplacer chap. V par chap. IV.

(III, 4.6.6) Ligne 19 de la p. 142, remplacer « chap. V » par « dans un paragraphe ultérieur ».

## B) Modifications de texte (1)

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{i})$ Dans $(\mathbf{0}_{1}, 5.1.3)$, ligne 18 de la p. 45, remplacer « somme directe » par « somme directe finie ».

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{2})$ Dans $(\mathbf{0}_{\mathrm{I}}, 5.4.3)$, lignes 8 à 4 du bas de la p. 49, remplacer depuis « Dans le cas général... » par le texte suivant :

Dans le cas général où X est un espace annelé tel que $\mathcal{O}_{x}$ soit un anneau local pour

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Err $_{N}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Pour faciliter la recherche des références, les modifications appartenant à la liste d'errata insérée dans le chapitre N seront désormais désignées par $\mathbf{Err}_{\mathrm{N}}$ suivi d'un numéro.</span></small>

tout $x \in \mathbf{X}$, si $\mathcal{L}$ est un $\mathcal{O}_{\mathrm{X}}$-Module de type fini tel qu'il existe un $\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{F}$ pour lequel $\mathcal{L} \otimes_{\mathcal{O}_{\mathrm{X}}} \mathcal{F}$ soit isomorphe à $\mathcal{O}_{\mathrm{X}}$, le raisonnement précédent montre que pour tout $x \in \mathbf{X}$, $\mathcal{L}_{x}$ est isomorphe à $\mathcal{O}_{x}$. On en déduit que $\mathcal{L}$ est alors inversible. En effet, pour tout $x \in \mathbf{X}$, soient U un voisinage ouvert de $x$ tel que $\mathcal{L}|\mathrm{U}$ soit engendré par $n$ sections $s_{i}(1 \leqslant i \leqslant n)$ au-dessus de U (5.2.1). On peut supposer par exemple que $s = s_{1}$ est telle que $s_{x} \neq 0$, et comme $\mathcal{L}_{x}$ est isomorphe à $\mathcal{O}_{x}$, il existe pour chaque $i$ une section $t_{i}$ de $\mathcal{O}_{\mathrm{X}}$ au-dessus d'un voisinage ouvert $\mathrm{V}_{i} \subset \mathrm{U}$ de $x$ telle que $(t_{i})_{x}s_{x} = (s_{i})_{x}$. Il y a par suite un voisinage ouvert $\mathrm{V} \subset \bigcap_{i=1}^{n} \mathrm{V}_{i}$ de $x$ tel que $t_{i}s = s_{i}$ dans V, autrement dit $\mathcal{L}|\mathrm{V}$ est engendré par l'unique section $s|\mathrm{V}$. En outre, si $z$ est une section au-dessus d'un ouvert $\mathrm{W} \subset \mathrm{V}$ du noyau de l'homomorphisme $\mathcal{O}_{\mathrm{X}}|\mathrm{V} \to \mathcal{L}|\mathrm{V}$ defini par $s(5.1.1)$, $z_{y}$ annule $\mathcal{L}_{y}$ pour tout $y \in \mathrm{W}$, donc $z_{y} = 0$ par hypothèse et par suite $z = 0$, ce qui achève de prouver notre assertion. De plus, la considération du produit tensoriel $\mathcal{L}^{-1} \otimes \mathcal{L} \otimes \mathcal{F}$ montre aussitôt que $\mathcal{F}$ est isomorphe à $\mathcal{L}^{-1}$.

$(\mathbf{Err}_{\mathrm{III}}, 3)$ Dans $(\mathbf{0}_{\mathrm{I}}, 7.2.4)$, il faut imposer la condition que les puissances $\mathfrak{J}^{n}$ sont des idéaux fermés dans l'anneau admissible A pour que la proposition soit exacte. La démonstration donnée est incorrecte, et l'énoncé rectifié résulte de Bourbaki, Top. gén., chap. III, $3^{\circ}$ éd., § 3, n° 5, cor. I de la prop. 9. Il faut de même supposer les $\mathfrak{J}^{n}$ fermés dans A dans les énoncés $(\mathbf{0}_{\mathrm{I}}, 7.2.5)$ et $(\mathbf{0}_{\mathrm{I}}, 7.2.6)$.

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{4})$ Après la proposition $(\mathbf{I}, 2.2.5)$, ajouter : avec les notations de $(\mathbf{I}, 2.2.5)$, si $\mathfrak{J}$ est un idéal de A, on note $\mathfrak{J}\mathcal{F}$ le sous-$\mathcal{O}_{\mathrm{x}}$-Module $\widetilde{\mathfrak{J}}\mathcal{F}$ défini dans $(\mathbf{0}, 4.3.5)$.

$(Err_{III}, 5)$ Dans $(I, 3.4.5)$, ligne $i$ du bas de la p. 112, remplacer « un corps K » par « un corps algébriquement clos K ». Ligne $i$ de la p. 113, remplacer « extension » par « extension algébriquement close ». Lignes $i$ à 4 de la p. 113, remplacer depuis « K sera appelé... » par le texte suivant :

Pour tout point de X à valeurs dans un corps K, K sera appelé le corps des valeurs du point correspondant, et si x est la localité de ce point on dit encore que ce dernier est localisé en x. On définit ainsi une application  $\mathbf{X}(\mathbf{K})\to\mathbf{X}$ , faisant correspondre à un point à valeurs dans K sa localité.

Lignes 7 et 16 de la p. 113, supprimer « géométrique »; lignes 10 et 13 de la p. 113, supprimer « géométriques ». Lignes 10 et 11 du bas de la p. 115, supprimer « géométrique ».

$(\mathbf{Err}_{\mathrm{III}}, 6)$ A la fin de la démonstration de (I, 3.6.1), ligne 12 du bas de la p. 117, ajouter: Si l'on pose $\mathbf{X}' = \mathbf{X} \times_{\mathbf{Y}} \operatorname{Spec}(\mathcal{O}_y / \mathfrak{a}_y)$, alors, pour tout point $x \in \mathbf{X}'$, identifié par $p$ à un point de $\mathbf{X}$, on a $\mathcal{O}_{\mathbf{X}', x} = \mathcal{O}_{\mathbf{X}, x} / \mathfrak{a}_y \mathcal{O}_{\mathbf{X}, x}$. La question étant en effet locale sur $\mathbf{X}$ et $\mathbf{Y}$, on peut supposer que $\mathbf{X} = \operatorname{Spec}(\mathbf{B})$, $\mathbf{Y} = \operatorname{Spec}(\mathbf{A})$, et l'on a $(\mathbf{B} / \mathfrak{a}_y \mathbf{B})_x = \mathbf{B}_x / \mathfrak{a}_y \mathbf{B}_x$ par platitude (0, 1.3.2).

$(\mathbf{Err}_{\mathrm{III}}, 7)$ Dans $(\mathbf{I}, 5.1.1)$, ligne 3 du bas de la p. 127, remplacer « $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent » par « Idéal quasi-cohérent de $\mathcal{B}$ ».

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{8})$ Après (I, 5.1.10), ligne 16 de la p. 131, ajouter :

Remarque (5.1.11). — Une légère adaptation du raisonnement fait dans (5.1.9) montre que la conclusion reste valable sans supposer a priori que X soit un préschéma, mais

en supposant seulement que  $(\mathbf{X}, \mathcal{O}_{\mathrm{X}})$  soit un espace annelé en anneaux locaux, J un Idéal de  $O_{X}$  tel que  $J^{n}=0$ , que l'espace annelé  $\mathbf{X}_{0}=(\mathbf{X}, \mathcal{O}_{\mathrm{X}}/\mathcal{J})$  soit un schéma affine et enfin que les Idéaux  $J^{k}/J^{k+1}$  soient des  $O_{X_{0}}$ -Modules quasi-cohérents. Il suffit en effet d'utiliser (1.8.1) (cf.  $(\mathbf{Err}_{\mathrm{II}})$ ) au lieu de (2.2.4) dans le raisonnement.

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{9})$ Dans $(\mathbf{I}, 5.3.1)$, ligne 11 de la p. 132, insérer, après « ou $\Delta_{X}$», « ou $\Delta_{\varphi}$ si $\varphi : X \to S$ est le morphisme structural ».

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{10})$ Dans (I, 5.3.9), la démonstration est insuffisante, car elle ne prouve pas que $\Delta_{\mathrm{X}}(\mathbf{X})$ soit localement fermé dans $\mathbf{X} \times_{\mathrm{S}} \mathbf{X}$. Pour avoir une démonstration correcte, il suffit d'utiliser (4.2.4, a): pour tout $x \in \mathbf{X}$ et tout voisinage affine U de $x$ dans $\mathbf{X}$, $\mathbf{U} \times_{\mathrm{S}} \mathbf{U}$ est un voisinage affine de $\Delta_{\mathrm{X}}(x)$; compte tenu de (5.3.16) (dont la démonstration n'utilise que la définition (5.3.1.1)), on est ramené à démontrer (5.3.9) lorsque $\mathrm{S} = \operatorname{Spec}(\mathrm{B})$ et $\mathrm{X} = \operatorname{Spec}(\mathrm{A})$ sont des schémas affines; il est clair alors en vertu de (5.3.1.1) que $\Delta_{\mathrm{X}}$ correspond à l'homomorphisme canonique $\mathrm{A} \otimes_{\mathrm{B}} \mathrm{A} \to \mathrm{A}$ qui transforme $x \otimes y$ en $xy$; cet homomorphisme étant surjectif, $\Delta_{\mathrm{X}}$ est dans ce cas une immersion fermée (4.2.3), ce qui achève la démonstration.

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{II})$ Dans $(\mathbf{I}, 7.1.15)$ et $(\mathbf{I}, 7.1.16)$, lignes 7 et 15 du bas de la p. 158, supprimer « géométriques ».

$(Err_{III}, 12)$ Remplacer (I, 7.4.7) par : On étend (par abus de langage) les définitions de (7.4.1) au cas où X est un préschéma réduit dont tout point admet un voisinage ouvert n'ayant qu'un nombre fini de composantes irréductibles; il résulte alors de (7.3.4) et (7.4.6) que, pour un $\mathcal{O}_{X}$-Module quasi-cohérent de type fini $\mathcal{F}$, dire que F est un faisceau de torsion équivaut à dire que $\mathrm{Supp}(\mathcal{F})$ ne contient aucune composante irréductible de X.

$(Err_{III}, 13)$ Dans (I, 10.11.7), lignes 17 à 23 de la p. 205, la fin de la démonstration depuis « Reste à prouver... » est inutile en vertu de (10.11.6), les faisceaux considérés étant cohérents par (0, 5.3.5).

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{14})$ Dans $(\mathbf{II}, \mathbf{I}.7.8)$, après la ligne 10 du bas de la p. 16, ajouter : lorsque $\mathcal{E} = \mathcal{O}_{\mathrm{S}}^{n}$, on écrit aussi $\mathbf{V}_{\mathrm{S}}^{n}$ au lieu de $\mathbf{V}(\mathcal{E})$; si en outre $\mathrm{S} = \operatorname{Spec}(\mathrm{A})$ est affine, on écrit $\mathbf{V}_{\mathrm{A}}^{n}$ au lieu de $\mathbf{V}_{\mathrm{S}}^{n}$; on a $\mathbf{V}_{\mathrm{A}}^{n} = \operatorname{Spec}(\mathrm{A}[\mathrm{T}_{1}, \ldots, \mathrm{T}_{n}])$ où les $\mathrm{T}_{i}$ sont des indéterminées.

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{15})$ Dans $(\mathbf{II}, \mathbf{1.7.10})$, ligne 10 de la p. 17, supprimer « géométriques »; lignes 12 et 16-17 de la p. 17, supprimer « géométrique ».

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{16})$ Dans $(\mathbf{II}, \mathbf{1.7.12})$, ajouter : On pose de même :

$$
\mathbf {V} (\mathcal {O} _ {\mathrm{S}} ^ {n}) = \mathbf {V} _ {\mathrm{S}} ^ {n} = \mathrm{S} [ \mathrm{T} _ {1}, \dots , \mathrm{T} _ {n} ].
$$

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{17})$ Dans (II, 4.2.6), ligne 7 de la p. 75, supprimer « géométriques »; ligne 8 de la p. 75, supprimer « géométrique ».

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{18})$ Dans (II, 4.6.13), ligne 7 de la p. 92, le raisonnement doit être précisé, car avec les notations de (4.4.10), il faut ici prouver que l'immersion $\Gamma_f$ est quasi-compacte, afin d'appliquer (i bis). En vertu de (4.6.4), pour prouver que $\mathcal{L}$ est ample relativement à $f$, on peut se borner au cas où Y est affine. Notons d'autre part que dans chacune des hypothèses de (v), $f$ est quasi-compact (I, 6.6.4). D'autre part, si $g$ est

séparé, $\Gamma_{f}$ est une immersion fermée (I, 5.4.3) donc quasi-compacte (I, 6.6.4). Si au contraire X est localement noethérien, comme Y est affine et $f$ quasi-compact, l'espace sous-jacent à X est quasi-compact, donc noethérien, et on peut de nouveau appliquer (I, 6.6.4) pour prouver que $\Gamma_{f}$ est quasi-compacte.

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{19})$ L'énoncé de (II, 5.2.2) est incorrect, les conditions $b), c)$ et $c')$ n'étant pas locales sur Y lorsqu'on ne sait pas si pour un ouvert U de Y, un $(\mathcal{O}_{\mathrm{X}}|f^{-1}(\mathrm{U}))$-Module quasi-cohérent est restriction à $f^{-1}(\mathrm{U})$ d'un $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent. Il faut donc remplacer dans la ligne 16 de la p. 98 « Soit $f: \mathrm{X} \to \mathrm{Y}$ un morphisme séparé quasi-compact » par : « Soient X, Y deux préschémas tels que X soit un schéma ou que l'espace sous-jacent à X soit localement noethérien, et soit $f: \mathrm{X} \to \mathrm{Y}$ un morphisme quasi-compact. » Dans la démonstration, on observera que les hypothèses entraînent que $f$ est séparé lorsqu'on suppose que X est un schéma, en vertu de (I, 5.5.5 et 5.5.8); on peut donc appliquer (I, 9.2.2) dans les deux cas.

$(Err_{III}, 20)$ Dans $(II, 6.2.3)$, ajouter, après la ligne 18 du bas de la p. 115 : On dit qu'un morphisme $f: X \to Y$ est quasi-fini en un point $x \in X$ s'il existe un voisinage ouvert affine $V$ de $y = f(x)$ et un voisinage ouvert affine $U$ de $x$ tels que $f(U) \subset V$ et que le morphisme $U \to V$ restriction de $f$ soit quasi-fini. On dit qu'un morphisme $f: X \to Y$ est localement quasi-fini s'il est quasi-fini en tout point de $X$.

$(Err_{III}, 21)$ Dans $(II, 6.4.3)$, la démonstration est incorrecte, les éléments d'un sous-A-module de type fini de K n'étant pas nécessairement entiers sur A. Remplacer les 9 dernières lignes de la p. 121 par le texte suivant : Comme on peut supposer que E est sans torsion, donc fidèle, E est aussi un A[u]-module fidèle (A étant plongé dans l'anneau des endomorphismes de E). Comme E est un A-module de type fini, il en résulte que u est entier sur A (Bourbaki, Alg. comm., chap. V, § 1, n° 1, lemme 1). On en conclut immédiatement que les valeurs propres de $u \otimes 1$ (dans une clôture algébrique de K) sont des éléments entiers sur A, et il en est donc de même des $\sigma_i(u)$.

$(Err_{III}, 22)$ Dans $(0_{III}, 9.1.1)$, ligne 18 du bas de la p. 12, supprimer « ouverte ». $(Err_{III}, 23)$ Dans $(0_{III}, 11.7.3)$, ligne 10 de la p. 43, après $C''$, ajouter : tel que pour tout objet projectif P de $C$ (resp. tout objet projectif P' de $C'$) le foncteur A'→T(P, A')(resp. A→T(A, P')) soit exact dans $C'$ (resp. C).

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{24})$ L'énoncé de $(\mathbf{0}_{\mathrm{III}}, 13.7.7)$ est inexact, et doit être modifié comme suit : ligne 6 de la p. 78, supprimer « et $(\mathrm{R}^{n+1}\mathrm{T}(\mathrm{A}_k))_{k \in \mathbf{Z}}$ »; ligne 7 de la p. 78, remplacer « $\mathrm{R}^{\prime n}\mathrm{T}(\mathbf{A})$ est un S-module de type fini» par « $\mathrm{R}^{\prime n}\mathrm{T}(\mathbf{A})$ et $\mathrm{R}^{\prime n+1}\mathrm{T}(\mathbf{A})$ sont des S-modules de type fini»; lignes 12-13 de la p. 78, supprimer « et $p + q = n + 1$ ». Dans la démonstration, ligne 23 de la p. 78, supprimer « et pour $n + 1$ ».

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{25})$ Dans (III, 1.4.15), ligne 6 du bas de la p. 92, remplacer « de type fini » par « quasi-compact ».

$(Err_{III}, 26)$ Dans $(III, 2.2.4)$, ligne $1$ de la p. 102, remplacer « que les supports de $\mathcal{F}$ et de $\mathcal{H}$ soient propres sur Y » par « que le support de $\operatorname{Im}(\mathcal{F} \to \mathcal{G})$ soit propre sur Y ». Dans la démonstration, remplacer le texte des lignes 10 à 16, depuis « Cela étant... », par :

Posons $\mathcal{G}_1 = \operatorname{Im}(\mathcal{F} \to \mathcal{G}) = \operatorname{Ker}(\mathcal{G} \to \mathcal{H})$, qui est cohérent. Comme on a la suite exacte $0 \to \mathcal{G}_1(n) \to \mathcal{G}(n) \to \mathcal{H}(n)$ et que le foncteur $f_*$ est exact à gauche, la suite $0 \to f_*(\mathcal{G}_1(n)) \to f_*(\mathcal{G}(n)) \to f_*(\mathcal{H}(n))$ est exacte pour tout $n$, et il suffit donc de montrer que, pour $n$ assez grand, la suite $f_*(\mathcal{F}(n)) \to f_*(\mathcal{G}_1(n)) \to 0$ est exacte. Autrement dit, on peut se borner au cas où $\mathcal{H} = 0$ et où le support de $\mathcal{G}$ est propre sur Y, donc fermé dans Z (II, 5.4.10); $\mathcal{G}' = i_*(\mathcal{G})$ est par suite un $\mathcal{O}_Z$-Module cohérent tel que $\mathcal{G}' | X = \mathcal{G}$. On sait (I, 9.4.3) qu'il existe un $\mathcal{O}_Z$-Module cohérent $\mathcal{F}'$ tel que $\mathcal{F}' | X = \mathcal{F}$. En outre, comme X est ouvert dans Z et $\operatorname{Supp}(\mathcal{G}) \subset X$ fermé dans Z, il est immédiat que l'on définit un homomorphisme surjectif $u': \mathcal{F}' \to \mathcal{G}'$ de faisceaux tel que $u'|X$ soit l'homomorphisme surjectif donné $u: \mathcal{F} \to \mathcal{G}$, en prenant $u'|U = 0$ pour tout ouvert U de Z ne rencontrant pas $\operatorname{Supp}(\mathcal{G})$ et $u'|U = u|U$ pour tout ouvert U ⊂ X. Cela étant, on voit comme au début de la démonstration de (2.2.2) que l'on peut se borner au cas où Y est affine, et il s'agit donc de montrer que, pour $n$ assez grand, l'homomorphisme $\Gamma(u): \Gamma(X, \mathcal{F}(n)) \to \Gamma(X, \mathcal{G}(n))$ est surjectif. Or, on a le diagramme commutatif

$$
\begin{array}{c c c} \Gamma (Z, \mathcal {F} ^ {\prime} (n)) & \xrightarrow {\Gamma (u ^ {\prime})} & \Gamma (Z, \mathcal {G} ^ {\prime} (n)) \\ \Bigg \downarrow_ {v} & & \Bigg \downarrow_ {w} \\ \Gamma (\mathbf {X}, \mathcal {F} (n)) & \xrightarrow [ \Gamma (u) ]{} & \Gamma (\mathbf {X}, \mathcal {G} (n)) \end{array}
$$

où $v$ et $w$ sont les homomorphismes de restriction. La définition de $\mathcal{G}'$ montre en outre que $w$ est $\text{bijectif}$; par ailleurs, en vertu de (2.2.3), $\Gamma(u')$ est surjectif pour $n$ assez grand, donc il en est de même de $\Gamma(u)$.

$(\mathbf{Err}_{\mathrm{III}}, \mathbf{27})$ Dans $(\mathbf{III}, 2.2.5)$, après la ligne 7 du bas de la p. 102, ajouter :

(iii) Sous les hypothèses de (2.2.4) concernant X, Y, f et L, il est immédiat que si H est un  $O_{X}$ -Module cohérent dont le support est propre sur Y, un raisonnement analogue à celui de (2.2.4) montre qu'il existe un entier N tel que pour  $n \geqslant N$ , on ait  $\mathrm{R}^{if}_{*}(\mathcal{H}(n)) = 0$  pour tout i > 0. On en conclut, par la suite exacte de cohomologie, que si  $u : F \to G$  est un homomorphisme de  $O_{X}$ -Modules cohérents tel que  $\operatorname{Ker}(u)$  et  $\operatorname{Coker}(u)$  aient leurs supports propres sur Y, alors il existe N tel que pour  $n \geqslant N$ , l'homomorphisme correspondant  $\mathrm{R}^{if}_{*}(\mathcal{F}(n)) \to \mathrm{R}^{if}_{*}(\mathcal{G}(n))$  soit bijectif pour tout i > 0.

$(Err_{III}, 28)$ Dans $(III, 4.4.9)$, ligne 17 du bas de la p. 137, remplacer « Soient Y un préschéma intègre localement noethérien » par « Soient X et Y deux préschémas intègres localement noethériens »; ligne 16 du bas de la p. 137, remplacer « de type fini » par « localement de type fini ». La démonstration est essentiellement inchangée, $f^{-1}(y)$ étant localement de type fini sur $k(y)$, donc encore discret.

$(\mathbf{Err}_{\mathrm{III}}, 29)$ dans (I, 9.3.4), ligne 19 du bas de la p. 173, remplacer « noethérien » par « quasi-compact »; lignes 18 et 19 du bas de la p. 173, remplacer « cohérent » par « quasi-

cohérent de type fini ». Dans la démonstration, on se ramène au cas où X = Spec(A), F = M, où M est un A-module de type fini, J = J, où J est un idéal de type fini de A ; le reste du raisonnement est alors inchangé.

$(\mathbf{Err}_{\mathrm{III}}, 30)$ Dans $(\mathbf{I}, 9.3.5)$, remplacer les lignes 1 à 7 du bas de la p. 173 par le texte suivant :

Proposition (9.3.5). — Soient X un préschéma, F un  $O_{X}$ -Module quasi-cohérent de type fini. Alors il existe un sous-préschéma fermé Y de X, dont l'espace sous-jacent est égal à Supp(F), et un  $O_{Y}$ -Module quasi-cohérent de type fini G tels que, si  $j: Y \to X$  est l'injection canonique, F soit isomorphe à  $j_{*}(G)$ .

Il suffira de montrer que l'Idéal J de  $O_{X}$ , annulateur de F, est quasi-cohérent; on prendra alors pour Y le sous-préschéma fermé de X défini par J (I, 4.1.2), et comme JF = 0, F est un  $(\mathcal{O}_{\mathrm{X}}/\mathcal{J})$ -Module et on répondra à la question en prenant  $\mathcal{G}=j^{*}(\mathcal{F})$ . Pour voir que J est quasi-cohérent, on peut (la question étant locale) se borner au cas où  $\mathrm{X}=\operatorname{Spec}(\mathrm{A})$ ,  $F=\widetilde{M}$ , où M est un A-module engendré par un nombre fini d'éléments  $x_{i}$  ( $i\leqslant i\leqslant r$ ); l'Idéal J est alors l'intersection des annulateurs des  $x_{i}$ . Mais l'annulateur de  $x_{i}$  est le noyau de l'homomorphisme  $O_{X}\to F$  correspondant à l'homomorphisme  $s\to sx_{i}$  de A dans M; c'est donc bien un Idéal quasi-cohérent (I, 4.1.1) et toute intersection finie de tels Idéaux est aussi un Idéal quasi-cohérent (I, 1.3.10).