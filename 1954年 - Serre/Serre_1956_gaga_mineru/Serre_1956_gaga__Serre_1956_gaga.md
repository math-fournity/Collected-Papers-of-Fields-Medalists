JEAN-PIERRE SERRE
Géométrie algébrique et géométrie analytique

Annales de l'institut Fourier, tome 6 (1956), p. 1-42 &lt;http://www.numdam.org/item?id=AIF_1956__6__1_0&gt;

© Annales de l’institut Fourier, 1956, tous droits réservés.

L'accès aux archives de la revue « Annales de l'institut Fourier » (http://annalif.ujf-grenoble.fr/) implique l'accord avec les conditions générales d'utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou impression systématique est constitutive d'une infraction pénale. Toute copie ou impression de ce fichier doit contenir la présente mention de copyright.

NUMDAM
Article numérisé dans le cadre du programme
Numérisation de documents anciens mathématiques
http://www.numdam.org/

# GEOMÉTRIE ALGÉBRIQUE ET GÉOMÉTRIE ANALYTIQUE

par Jean-Pierre SERRE.

## INTRODUCTION

Soit X une variété algébrique projective, définie sur le corps des nombres complexes. L'étude de X peut être entreprise de deux points de vue : le point de vue algébrique, dans lequel on s'intéresse aux anneaux locaux des points de X, aux applications rationnelles, ou régulières, de X dans d'autres variétés, et le point de vue analytique (parfois appelé « transcendant ») dans lequel c'est la notion de fonction holomorphe sur X qui joue le principal rôle. On sait que ce second point de vue s'est révélé particulièrement fécond lorsque X est non singulière, cette hypothèse permettant de lui appliquer toutes les ressources de la théorie des variétés kählériennes (formes harmoniques, courants, cobordisme, etc.)

Dans de nombreuses questions, les deux points de vue conduisent à des résultats essentiellement équivalents, bien que par des méthodes très différentes. Par exemple, on sait que les formes différentielles holomorphes en tout point de X ne sont pas autre chose que les formes différentielles rationnelles qui sont partout « de première espèce » (la variété X étant encore supposée non singulière); le théorème de CNow, d'après lequel tout sous-espace analytique fermé de X est une variété algébrique, est un autre exemple du même type.

Le but principal du présent mémoire est d'étendre cette équivalence aux faisceaux cohérents; de façon précise, nous

montrons que faisceaux algébriques cohérents et faisceaux analytiques cohérents se correspondent biunivoquement, et que la correspondance entre ces deux catégories de faisceaux laisse invariants les groupes de cohomologie (voir n° 12 pour les énoncés); nous indiquons diverses applications de ces résultats, notamment à la comparaison entre espaces fibrés algébriques et espaces fibrés analytiques.

Les deux premiers paragraphes sont préliminaires. Au § 1 nous rappelons la définition et les principales propriétés des « espaces analytiques ». La définition que nous avons adoptée est celle proposée par H. CARTAN dans [3], à cela près que H. CARTAN se bornait aux variétés normales, restriction inutile pour notre objet; une définition très voisine a été utilisée par W-L. Chow dans ses travaux, encore inédits, sur ce sujet. Dans le § 2, nous montrons comment l'on peut munir toute variété algébrique X d'une structure d'espace analytique, et nous en donnons diverses propriétés élémentaires. La plus importante est sans doute le fait que, si $\mathcal{O}_x$ (resp. $\mathcal{H}_x$) désigne l'anneau local (resp. l'anneau des germes de fonctions holomorphes) de X au point $x$, les anneaux $\mathcal{O}_x$ et $\mathcal{H}_x$ ont même complété, et, de ce fait, forment un « couple plat », au sens de l'Annexe, déf. 4.

Le § 3 contient les démonstrations des théorèmes sur les faisceaux cohérents auxquels nous avons fait allusion plus haut. Ces démonstrations reposent principalement, d'une part sur la théorie des faisceaux algébriques cohérents développée dans [18], et d'autre part sur les théorèmes A et B de [3], exp. XVIII-XIX; pour être complets, nous avons reproduit les démonstrations de ces théorèmes.

Le § 4 est consacré aux applications (1): invariance des nombres de Betti par automorphisme du corps des complexes, théorème de Chow, comparaison des espaces fibrés algébriques et analytiques de groupe structural un groupe algébrique donné. Nos résultats sur cette dernière question sont d'ailleurs fort incomplets: de tous les groupes semi-simples, nous ne savons traiter que le groupe linéaire unimodulaire, et le groupe symplectique.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Nous avons laissé de côté les applications aux fonctions automorphes, pour lesquelles nous renvoyons à [3], exp. XX.</span></small>

Enfin, nous avons eu besoin d'un certain nombre de résultats sur les anneaux locaux qui ne se trouvent pas explicitement dans la littérature; nous les avons groupés dans une Annexe.

## § 1. — Espaces analytiques.

## 1. Sous-ensembles analytiques de l'espace affine.

Soit $n$ un entier $\geqslant 0$, et soit $\mathbb{C}^{n}$ l'espace numérique complexe de dimension $n$, muni de la topologie usuelle. Si U est un sous-ensemble de $\mathbb{C}^{n}$, on dit que U est analytique si, pour tout $x \in \mathrm{U}$, il existe des fonctions $f_{1}, \ldots, f_{k}$, holomorphes dans un voisinage W de $x$, et telles que U $\cap$ W soit identique à l'ensemble des points $z \in \mathrm{W}$ vérifiant les équations $f_{i}(z) = 0$, $i = 1, \ldots, k$. Le sous-ensemble U est alors localement fermé dans $\mathbb{C}^{n}$ (c'est-à-dire intersection d'un ouvert et d'un fermé), donc localement compact lorsqu'on le munit de la topologie induite par celle de $\mathbb{C}^{n}$.

Nous allons maintenant munir l'espace topologique U d'un faisceau. Si X est un espace quelconque, nous noterons $\mathcal{C}(\mathbf{X})$ le faisceau des germes de fonctions sur X, à valeurs dans $\mathbb{C}$ (cf. [18], n° 3). Si $\mathcal{H}$ désigne le faisceau des germes de fonctions holomorphes sur $\mathbb{C}^n$, le faisceau $\mathcal{H}$ est un sous-faisceau de $\mathcal{C}(\mathbb{C}^n)$. Soit alors $x$ un point de U; on a un homomorphisme de restriction

$$
\varepsilon_ {x}: \quad \mathcal {C} (\mathbf {C} ^ {n}) _ {x} \rightarrow \mathcal {C} (\mathrm{U}) _ {x}.
$$

L'image de $\mathcal{H}_x$ par $\varepsilon_x$ est un sous-anneau $\mathcal{H}_{x,\mathrm{U}}$ de $\mathcal{C}(\mathrm{U})_x$; les $\mathcal{H}_{x,\mathrm{U}}$ forment un sous-faisceau $\mathcal{H}_{\mathrm{U}}$ de $\mathcal{C}(\mathrm{U})$, que nous appellerons le faisceau des germes de fonctions holomorphes sur U; c'est un faisceau d'anneaux. Nous noterons $\mathcal{A}_x(\mathrm{U})$ le noyau de $\varepsilon_x\colon \mathcal{H}_x\to \mathcal{H}_{x,\mathrm{U}}$; vu la définition de $\mathcal{H}_{x,\mathrm{U}}$, c'est l'ensemble des $f\in \mathcal{H}_x$ dont la restriction à U est nulle dans un voisinage de $x$; nous identifierons fréquemment $\mathcal{H}_{x,\mathrm{U}}$ à l'anneau quotient $\mathcal{H}_x / \mathcal{A}_x(\mathrm{U})$.

Puisque nous avons une topologie et un faisceau de fonctions sur U, nous pouvons définir la notion d'application holomorphe (cf. [3], exp. VI ainsi que [18], n° 32):

Soient U et V deux sous-ensembles analytiques de $\mathbb{C}^r$ et de $\mathbb{C}^s$, respectivement. Une application $\varphi: \mathrm{U} \to \mathrm{V}$ sera dite holomorphe si elle est continue, et si $f \in \mathcal{H}_{\varphi(x),\mathrm{V}}$ entraîne $f \circ \varphi \in \mathcal{H}_{x,\mathrm{U}}$.

Il revient au même de dire que les $s$ coordonnées de $\varphi(x)$, $x\in\mathbf{U}$, sont des fonctions holomorphes de $x$, autrement dit des sections de $\mathcal{H}_{\mathbf{U}}$.

La composée de deux applications holomorphes est holomorphe. Une bijection $\varphi: U \to V$ est appelée un isomorphisme analytique (ou simplement un isomorphisme) si $\varphi$ et $\varphi^{-1}$ sont holomorphes; cela équivaut à dire que $\varphi$ est un homéomorphisme de U sur V qui transforme le faisceau $\mathcal{H}_{U}$ en le faisceau $\mathcal{H}_{\backslash}$.

Si U et U' sont deux sous-ensembles analytiques de C$^{r}$ et de C$^{r'}$, le produit U × U' est un sous-ensemble analytique de C$^{r+r'}$. Les propriétés énoncées dans [18], n° 33 sont valables, en remplaçant partout sous-ensemble localement fermé par sous-ensemble analytique, et application régulière par application holomorphe; en particulier, si φ : U → V et φ' : U' → V' sont des isomorphismes analytiques, il en est de même de

$$
\varphi \times \varphi^ {\prime}: \mathrm{U} \times \mathrm{U} ^ {\prime} \rightarrow \mathrm{V} \times \mathrm{V} ^ {\prime}.
$$

Toutefois, à la différence du cas algébrique, la topologie de U × U' est identique à la topologie produit des topologies de U et de U'.

## 2. La notion d'espace analytique.

DÉFINITION 1. — On appelle espace analytique un ensemble X muni d'une topologie et d'un sous-faisceau $\mathcal{H}_{\mathrm{x}}$ du faisceau $\mathcal{C}(\mathrm{X})$, ces données étant assujetties à vérifier les axiomes suivants:

$(\mathrm{H}_{1})$. Il existe un recouvrement ouvert $\{V_{i}\}$ de l'espace X, tel que chaque $V_{i}$, muni de la topologie et du faisceau induits par ceux de X, soit isomorphe à un sous-ensemble analytique $U_{i}$ d'un espace affine, muni de la topologie et du faisceau définis au n° 1.

$(\mathrm{H}_{\mathrm{II}})$ . La topologie de X est séparée.

Les définitions du n° 1, étant de caractère local, se transportent aux espaces analytiques. Ainsi, si X est un espace analytique, le faisceau $\mathcal{H}_{\mathrm{x}}$ sera appelé le faisceau des germes de fonctions holomorphes sur X; si X et Y sont deux espaces analytiques, une application $\varphi: \mathrm{X} \to \mathrm{Y}$ sera dite holomorphe si elle continue, et si $f \in \mathcal{H}_{\varphi(x),\mathrm{Y}}$ entraîne $f \circ \varphi \in \mathcal{H}_{x,\mathrm{X}}$; ces applications forment une famille de morphismes (au sens de N. BOURBAKI) pour la structure d'espace analytique.

Si V est un sous-ensemble ouvert d'un espace analytique X, nous appellerons carte de V tout isomorphisme analytique de V sur un sous-ensemble analytique U d'un espace affine. L'axiome (H$_{II}$) signifie qu'il est possible de recouvrir X par des ouverts possédant des cartes. Si Y est un sous-ensemble de X, nous dirons que Y est analytique si, pour toute carte $\varphi: V \to U$, l'image $\varphi(Y \cap V)$ est un sous-ensemble analytique de U. S'il en est ainsi, Y est localement fermé dans X, et peut être muni de façon naturelle d'une structure d'espace analytique, dite induite par celle de X (cf. [18], n° 35 pour le cas algébrique). De même, soient X et X' deux espaces analytiques; il existe alors sur X × X' une structure d'espace analytique et une seule telle que, si $\varphi: V \to U$ et $\varphi': V' \to U'$ sont des cartes, $\varphi \times \varphi': V \times V' \to U \times U'$ soit une carte de V × V'; muni de cette structure, X × X' est appelé le produit des espaces analytiques X et X'; on observera que la topologie de X × X' coïncide avec la topologie produit des topologies de X et de X'.

Nous laissons au lecteur le soin de transposer aux espaces analytiques les autres résultats de [18], nos 34-35.

## 3. Faisceaux analytiques.

La définition des faisceaux analytiques donnée dans [2], exp. XV s'étend d'elle-même au cas d'un espace analytique X : un faisceau analytique $\mathcal{F}$ est simplement un faisceau de modules sur le faisceau d'anneaux $\mathcal{H}_{\mathrm{X}}$, autrement dit, un faisceau de $\mathcal{H}_{\mathrm{X}}$-modules (cf. [18], n° 6).

Soit Y un sous-ensemble analytique fermé de X; pour tout  $x \in X$ , soit  $\mathcal{A}_{x}(Y)$  l'ensemble des  $f \in H_{x,Y}$  dont la restriction à Y est nulle au voisinage de x. Les  $\mathcal{A}_{x}(Y)$  forment un faisceau d'idéaux  $\mathcal{A}(Y)$  du faisceau  $H_{X}$ ; le faisceau  $\mathcal{A}(Y)$  est donc un faisceau analytique. Le faisceau quotient  $\mathcal{H}_{X}/\mathcal{A}(Y)$  est nul en dehors de Y, et sa restriction à Y n'est autre que  $H_{Y}$ , par définition même de la structure induite; on pourra donc l'identifier à  $H_{Y}$ , cf. [18], n° 5.

PROPOSITION 1. — a) Le faisceau $\mathcal{H}_{\mathrm{X}}$ est un faisceau cohérent d'anneaux ([18], n° 15).

b) Si Y est un sous-espace analytique fermé de X, le faisceau $\mathcal{A}(\mathrm{Y})$ est un faisceau analytique cohérent (c'est-à-dire un faisceau cohérent de $\mathcal{H}_{\mathrm{X}}$-modules, au sens de [18], n° 12).

Dans le cas où X est un ouvert de $\mathbb{C}^{n}$, ces résultats sont dus à K. OKA et H. CARTAN cf. [1], ths. 1 et 2 ainsi que [2], exp. XV-XVI. Le cas général se ramène immédiatement à celui-là; en effet, la question étant locale, on peut supposer que X est un sous-ensemble analytique fermé d'un ouvert U de $\mathbb{C}^{n}$; on a $\mathcal{H}_{\mathrm{X}} = \mathcal{H}_{\mathrm{U}} / \mathcal{A}(\mathrm{X})$, et, d'après ce qui précède, $\mathcal{H}_{\mathrm{U}}$ est un faisceau cohérent d'anneaux, et $\mathcal{A}(\mathrm{X})$ est un faisceau cohérent d'idéaux de $\mathcal{H}_{\mathrm{U}}$; il en résulte bien que $\mathcal{H}_{\mathrm{U}}$ est cohérent, cf. [18], n° 16. L'assertion $b$) se démontre de la même manière.

Comme autres exemples de faisceaux analytiques cohérents, signalons les faisceaux de germes de sections d'espaces fibrés à fibre vectorielle (cf. n° 20), et les faisceaux de germes de fonctions automorphes ([3], exp. XX).

## 4. Voisinage d'un point dans un espace analytique.

Soient X un espace analytique, x un point de X, et  $H_{x}$  l'anneau des germes de fonctions holomorphes sur X au point x; cet anneau est une algèbre sur C, admettant pour unique idéal maximal l'idéal m formé des fonctions f nulles en x, et le corps  $H_{x}/m$  n'est autre que C; autrement dit,  $H_{x}$  est une algèbre locale sur C. Lorsque  $X = C^{n}$ , l'algèbre  $H_{x}$  n'est autre que l'algèbre  $C\{z_{i}, \ldots, z_{n}\}$  des séries convergentes à n variables; dans le cas général,  $H_{x}$  est isomorphe à une algèbre quotient  $C\{z_{i}, \ldots, z_{n}\}/a$ , puisque X est localement isomorphe à un sous-espace analytique de  $C^{n}$ ; il en résulte que  $H_{x}$  est un anneau noethérien; c'est de plus un anneau analytique, au sens de H. CARTAN ([3], exp. VII).

On voit facilement que la connaissance de $\mathcal{H}_{x}$ détermine X au voisinage de $x$ ([3], loc. cit.). En particulier, pour que X soit isomorphe à $\mathbb{C}^{n}$ au voisinage de $x$, il faut et il suffit que l'algèbre $\mathcal{H}_{x}$ soit isomorphe à $\mathbb{C}\{z_{1},\ldots,z_{n}\}$; on voit aisément que cette condition équivaut à dire que $\mathcal{H}_{x}$ est un anneau local régulier de dimension $n$ (pour tout ce qui concerne les anneaux locaux, cf. [16]). Le point $x$ est alors appelé un point simple de dimension $n$ sur X; si tous les points de X sont simples, X est appelé une variété analytique.

Revenons au cas général; l'anneau $\mathcal{H}_{x}$ n'ayant pas d'autre élément nilpotent que 0, il en résulte (cf. [15], chap. iv, § 2) que l'on a :

$$
0 = \cap \mathfrak {p} _ {i},
$$

les $\mathfrak{p}_i$ désignant les idéaux premiers minimaux de $\mathcal{H}_x$. Si l'on note $X_i$ les composantes irréductibles de X en $x$, on a $\mathfrak{p}_i = \mathcal{A}_x(X_i)$ et $\mathcal{H}_x / \mathfrak{p}_i = \mathcal{H}_{x,\mathrm{X}_i}$. Ceci ramène essentiellement l'étude locale de X à celle des $X_i$; par exemple, la dimension (analytique — c'est-à-dire la moitié de la dimension topologique) de X en $x$ est la borne supérieure des dimensions des $X_i$. On observera que cette dimension coïncide avec la dimension (au sens de Krull) de l'anneau local $\mathcal{H}_x$; en effet, il suffit de le vérifier lorsque X est irréductible en $x$, c'est-à-dire lorsque $\mathcal{H}_x$ est un anneau d'intégrité; dans ce cas, si l'on note $r$ la dimension analytique de X en $x$, on sait (cf. [14], § 4 ainsi que [3], exp. VIII) que $\mathcal{H}_x$ est une extension finie de $\mathbb{C}\{z_i,\dots,z_r\}$; comme $\mathbb{C}\{z_1,\dots,z_r\}$ a pour complété l'algèbre de séries formelles $\mathbb{C}[[z_1,\dots,z_r]]$, sa dimension est $r$, et il en est alors de même de $\mathcal{H}_x$, d'après [16], p. 18, ce qui démontre notre assertion.

## § 2. — Espace analytique associé à une variété algébrique.

Dans ce qui suit, nous aurons à considérer des variétés algébriques sur le corps C. Une telle variété sera munie de deux topologies : la topologie « usuelle », et la topologie « de Zariski ». Pour éviter les confusions, nous ferons précéder de la lettre Z les notions relatives à cette dernière topologie; par exemple, « Z-ouvert » signifiera « ouvert pour la topologie de Zariski ».

5. Définition de l'espace analytique associé à une variété algébrique.

La possibilité de munir toute variété algébrique d'une structure d'espace analytique résulte du lemme suivant :

LEMME 1. — a) La Z-topologie de $\mathbb{C}^{n}$ est moins fine que la topologie usuelle.

b) Tout sous-ensemble Z-localement fermé de $\mathbf{C}^n$ est analytique.

c) Si U et U' sont deux sous-ensembles Z-localement fermés de $\mathbf{C}^n$ et de $\mathbf{C}^{n'}$, et si $f: \mathrm{U} \to \mathrm{U}'$ est une application régulière, alors $f$ est holomorphe.

d) Dans les hypothèses de c), si l'on suppose en outre que f est un isomorphisme birégulier, c'est aussi un isomorphisme analytique.

Par définition, un sous-ensemble Z-fermé de $\mathbb{C}^n$ est défini par l'annulation d'un certain nombre de polynômes; comme un polynôme est continu pour la topologie usuelle (resp. holomorphe), on en déduit bien $a$) (resp. $b$). Pour démontrer $c$), on peut supposer que $\mathrm{U}' = \mathbb{C}$; on doit alors montrer que toute fonction régulière sur U est holomorphe, ce qui résulte encore du fait qu'un polynôme est une fonction holomorphe. Enfin, $d$) est conséquence immédiate de $c$) appliqué à $f^{-1}$.

Soit maintenant X une variété algébrique sur le corps C (au sens de [18], n° 34, donc non nécessairement irréductible). Soit V un sous-ensemble Z-ouvert de X, possédant une carte (algébrique)

$$
\varphi : \quad \mathrm{V} \rightarrow \mathrm{U},
$$

sur un sous-ensemble Z-localement fermé U d'un espace affine. D'après le lemme 1, b), U peut être muni d'une structure d'espace analytique.

PROPOSITION 2. — Il existe sur X une structure d'espace analytique et une seule telle que, pour toute carte $\varphi: V \to U$, l'ensemble Z-ouvert V soit ouvert, et $\varphi$ soit un isomorphisme analytique de V (muni de la structure analytique induite par celle de X) sur U (muni de la structure analytique définie au n° 1).

(Plus brièvement : toute carte algébrique doit être une carte analytique).

L'unicité est évidente, puisque l'on peut recouvrir X par des ensembles Z-ouverts V possédant des cartes. Pour prouver l'existence, soit $\varphi: V \to U$ une carte, et transportons à V la structure analytique de U au moyen de $\varphi^{-1}$. Si $\varphi': V': \to U'$ est une autre carte, les structures analytiques induites sur $V \cap V'$ par V et par $V'$ sont les mêmes, en vertu du lemme 1, $d$); de plus $V \cap V'$ est ouvert à la fois dans V et dans $V'$, en vertu du lemme 1, $a$). Par recollement, on obtient ainsi sur X une topologie et un faisceau $\mathcal{H}_X$ qui vérifient visiblement l'axiome ($H_I$). Pour vérifier ($H_{II}$) nous utiliserons l'axiome ($VA_{II}'$) de [18], n° 34; avec les notations de cet axiome, les graphes $T_{ij}$ des relations d'identification entre deux $U_i$ et $U_j$ sont Z-fermés dans $U_i \times U_j$, donc a fortiori fermés, ce qui signifie bien que X est séparé.

Remarque. — On peut donner une définition directe de la structure analytique de X, sans passer par les cartes $\varphi: V \to U$.

On définit la topologie comme la moins fine rendant continues les fonctions régulières sur les sous-ensembles Z-ouverts de X, et l'on définit $\mathcal{H}_{x,\mathrm{x}}$ comme le sous-anneau analytique de $\mathcal{C}(\mathrm{X})_x$ engendré par $\mathcal{O}_{x,\mathrm{x}}$ (au sens de [3], exp. VIII). Nous laissons au lecteur le soin de vérifier l'équivalence des deux définitions.

Dans la suite, nous noterons  $X^{h}$  l'ensemble X muni de la structure d'espace analytique qui vient d'être définie. La topologie de  $X^{h}$  est plus fine que la topologie de X; comme  $X^{h}$  peut être recouvert par un nombre fini d'ouverts possédant des cartes,  $X^{h}$  est un espace localement compact dénombrable à l'infini.

Les propriétés suivantes résultent immédiatement de la définition de  $X^{h}$ :

Si X et Y sont deux variétés algébriques, on a  $(\mathbf{X} \times \mathbf{Y})^{h} = \mathbf{X}^{h} \times \mathbf{Y}^{h}$ . Si Y est un sous-ensemble Z-localement fermé dans X, alors  $Y^{h}$  est un sous-ensemble analytique de  $X^{h}$ ; de plus, la structure analytique de  $Y^{h}$  coïncide avec la structure analytique induite sur Y par  $X^{h}$ . Enfin, si  $f: X \to Y$  est une application régulière d'une variété algébrique X dans une variété algébrique Y, f est aussi une application holomorphe de  $X^{h}$  dans  $Y^{h}$ .

6. Relations entre l'anneau local d'un point et l'anneau des fonctions holomorphes en ce point.

Soit X une variété algébrique, et soit x un point de X. Nous nous proposons de comparer l'anneau local  $O_{x}$  des fonctions régulières sur X au point x avec l'anneau local  $H_{x}$  des fonctions holomorphes sur  $X^{h}$  au voisinage de x.

Comme toute fonction régulière est holomorphe, toute fonction $f\in\mathcal{O}_{x}$ définit un germe de fonction holomorphe en $x$, que nous désignerons par $\theta(f)$. L'application $\theta:\mathcal{O}_{x}\to\mathcal{H}_{x}$ est un homomorphisme, et applique l'idéal maximal de $\mathcal{O}_{x}$ dans celui de $\mathcal{H}_{x}$; elle se prolonge donc par continuité en un homomorphisme $\hat{\theta}:\hat{\mathcal{O}}_{x}\to\hat{\mathcal{H}}_{x}$ du complété de $\mathcal{O}_{x}$ dans celui de $\mathcal{H}_{x}$ (cf. Annexe, n° 24).

PROPOSITION 3. — L'homomorphisme $\hat{0}:\hat{\mathcal{O}}_{x}\to\hat{\mathcal{H}}_{x}$ est bijectif.
Nous démontrerons la proposition précédente en même temps qu'un autre résultat :

Soit Y un sous-ensemble Z-localement fermé de X, et soit $\mathfrak{J}_{x}(\mathrm{Y})$ (ou $\mathfrak{J}_{x}(\mathrm{Y},\mathrm{X})$ lorsque l'on veut préciser X) l'idéal de $\mathcal{O}_{x}$

formé des fonctions $f$ dont la restriction à $\mathbf{Y}$ est nulle, dans un Z-voisinage de $x$ (cf. [18], n° 39). L'image de $\mathfrak{I}_{x}(\mathbf{Y})$ par $\theta$ est évidemment contenue dans l'idéal $\mathcal{A}_{x}(\mathbf{Y})$ de $\mathcal{H}_{x}$ défini au n° 3.

PROPOSITION 4. — L'idéal $\mathcal{A}_{x}(\mathbf{Y})$ est engendré par $0(\mathfrak{J}_{x}(\mathbf{Y}))$. Nous démontrerons d'abord les propositions 3 et 4 dans le cas particulier où X est l'espace affine $\mathbb{C}^{n}$. La proposition 3 est alors triviale, car $\hat{\mathcal{O}}_{x}$ et $\hat{\mathcal{H}}_{x}$ ne sont autres que l'algèbre $\mathbb{C}[z_{1},\ldots,z_{n}]$ des séries formelles en $n$ indéterminées. Passons à la proposition 4; soit a l'idéal de $\mathcal{H}_{x}$ engendré par $\mathfrak{J}_{x}(\mathbf{Y})$ (l'anneau $\mathcal{O}_{x}$ étant identifié à un sous-anneau de $\mathcal{H}_{x}$ au moyen de 0). Tout idéal de $\mathcal{H}_{x}$ définit un germe de sous-ensemble analytique de X en $x$, cf. [1], n° 3 ou [3], exp. VI, p. 6; il est clair que le germe défini par a n'est autre que Y. Soit alors $f$ un élément de $\mathcal{A}_{x}(\mathbf{Y})$; en vertu du « théorème des zéros » (qui est valable pour les idéaux de $\mathcal{H}_{x}$, cf. [14], p. 278, ainsi que [2], exp. XIV, p. 3 et [3], exp. VIII, p. 9) il existe un entier $r\geqslant0$ tel que $f^{\prime}\in\mathfrak{a}$. A fortiori, on aura

$$
f ^ {r} \in \mathfrak {a}. \hat {\mathcal {H}} _ {x} = \mathfrak {I} _ {x} (\mathrm{Y}). \hat {\mathcal {H}} _ {x} = \mathfrak {I} _ {x} (\mathrm{Y}). \hat {\mathcal {O}} _ {x}.
$$

Mais l'idéal $\mathfrak{J}_x(\mathbf{Y})$ est intersection d'idéaux premiers, qui correspondent aux composantes irréductibles de Y passant par $x$. D'après un théorème de CHEVALLEY (cf. [16], p. 40 ainsi que [17], p. 67), il en est donc de même de l'idéal $\mathfrak{J}_x(\mathbf{Y})$. $\hat{\mathcal{O}}_x$, et la relation $f^r \in \mathfrak{J}_x(\mathbf{Y})$. $\hat{\mathcal{O}}_x$ entraîne donc $f \in \mathfrak{J}_x(\mathbf{Y})$. $\hat{\mathcal{O}}_x$. Puisque $\mathcal{H}_x$ est un anneau local noethérien, on a $\mathfrak{a}$. $\hat{\mathcal{H}}_x \cap \mathcal{H}_x = \mathfrak{a}$ (cf. [15], Chap. IV, ou Annexe, prop. 27); on a donc $f \in \mathfrak{a}$, ce qui démontre la proposition 4 dans le cas considéré.

Passons au cas général. La question étant locale, on peut supposer que X est une sous-variété d'un espace affine que nous désignerons par U. Par définition, on a :

$$
\mathcal {O} _ {x} = \mathcal {O} _ {x, \mathrm{U}} / \mathfrak {I} _ {x} (\mathrm{X}, \mathrm{U}) \quad \text { et } \quad \mathcal {H} _ {x} = \mathcal {H} _ {x, \mathrm{U}} / \mathfrak {I} _ {x} (\mathrm{X}, \mathrm{U}).
$$

L'application $\theta: \mathcal{O}_x \to \mathcal{H}_x$ est obtenue par passage au quotient à partir de l'application $\theta: \mathcal{O}_{x,\mathrm{U}} \to \mathcal{H}_{x,\mathrm{U}}$, et, d'après ce qui précède, nous savons que $\hat{\theta}: \hat{\mathcal{O}}_{x,\mathrm{U}} \to \hat{\mathcal{H}}_{x,\mathrm{U}}$ est bijectif, et que $\mathcal{A}_x(\mathrm{X}, \mathrm{U}) = \theta (\mathfrak{I}_x(\mathrm{X}, \mathrm{U}))$. $\mathcal{H}_{x,\mathrm{U}}$. La proposition 3 en résulte immédiatement, en appliquant la proposition 29 de l'Annexe. Quant à la proposition 4, elle résulte de ce que $\mathcal{A}_x(\mathrm{Y})$ est l'image

canonique de l'idéal $\mathcal{A}_{x}(\mathbf{Y},\mathbf{U})$, lequel est engendré par $\theta(\mathfrak{I}_{x}(\mathbf{Y},\mathbf{U}))$, d'après ce qui précède.

La proposition 3 montre en particulier que $\theta: \mathcal{O}_x \to \mathcal{H}_x$ est injectif ce qui nous permettra d'identifier $\mathcal{O}_x$ au sous-anneau $\theta(\mathcal{O}_x)$ de $\mathcal{H}_x$. Compte tenu de cette identification, on a :

COROLLAIRE 1. — Le couple d'anneaux ($\mathcal{O}_{x}$, $\mathcal{H}_{x}$) est un couple plat (au sens de l'Annexe, déf. 4).

C'est une conséquence immédiate de la proposition 3 et de la proposition 28 de l'Annexe.

COROLLAIRE 2. — Les anneaux $\mathcal{O}_{x}$ et $\mathcal{H}_{x}$ ont même dimension. En effet, on sait que la dimension d'un anneau local noethérien est égale à celle de son complété (cf. [16], p. 26).

Compte tenu des résultats énoncés au n° 4, on obtient le résultat suivant (où nous supposons X irréductible pour simplifier l'énoncé):

COROLLAIRE 3. — Si X est une variété algébrique irréductible de dimension r, l'espace analytique  $X^{h}$  est de dimension analytique r en chacun de ses points.

7. Relations entre la topologie usuelle et la topologie de Zariski d'une variété algébrique.

PROPOSITION 5. — Soient X une variété algébrique, et U une partie de X. Si U est Z-ouverte et Z-dense dans X, alors U est dense dans X.

Soit Y le complémentaire de U dans X; c'est une partie Z-fermée de X. Soit x un point de X; si x n'était pas adhérent à U, on aurait Y = X au voisinage de x, d'où  $\mathcal{A}_{x}(\mathbf{Y}) = 0$ , avec les notations du n° 6. Comme  $\mathcal{A}_{x}(\mathbf{Y})$  contient  $\theta(\mathfrak{J}_{x}(\mathbf{Y}))$ , et que  $\theta$  est injectif (prop. 3), on aurait alors  $\mathfrak{J}_{x}(\mathbf{Y}) = 0$ , ce qui signifierait que Y = X dans un Z-voisinage de X, contrairement à l'hypothèse que U est Z-dense dans X, cqfd.

Remarque. — On voit facilement que la proposition 5 équivaut au fait que $\theta : \mathcal{O}_x \to \mathcal{H}_x$ est injectif, fait beaucoup plus élémentaire que la proposition 3, et que l'on peut, par exemple, démontrer par réduction au cas d'une courbe.

Nous allons maintenant donner deux applications simples de la proposition 5.

PROPOSITION 6. — Pour qu'une variété algébrique X soit complète, il faut et il suffit qu'elle soit compacte.

Rappelons d'abord un résultat de Chow (cf. [7], ainsi que [19], n° 4): pour toute variété algébrique X, il existe une variété projective Y, une partie U de Y, Z-ouverte et Z-dense dans Y, et une application régulière surjective f: U → X dont le graphe T soit Z-fermé dans X × Y. On a U = Y si et seulement si X est complète.

Ceci étant, supposons d'abord X complète; on a alors  $X = f(Y)$ , et, comme toute variété projective est compacte pour la topologie usuelle, on en conclut bien que X est compacte. Réciproquement, supposons X compacte; il en est alors de même de T qui est fermé dans  $X \times Y$ , donc de U puisque c'est la projection de T dans Y; ainsi, U est fermé dans Y, et la proposition 5 montre que U = Y, ce qui achève la démonstration.

Le lemme suivant est essentiellement dû à CHEVALLEY :

LEMME 2. — Soit $f\colon X\to Y$ une application régulière d'une variété algébrique X dans une variété algébrique Y, et supposons que $f(X)$ soit Z-dense dans Y. Il existe alors une partie $U\subset f(X)$ qui est Z-ouverte et Z-dense dans Y.

Lorsque X et Y sont irréductibles, ce résultat est bien connu, cf. [4], exp. 3 ou [17], p. 15, par exemple. Nous allons ramener le cas général à celui-là: soient $\mathbf{X}_i$, $i \in \mathbf{I}$, les composantes irréductibles de X, et soit $\mathbf{Y}_i$ la Z-adhérence de $f(\mathbf{X}_i)$ dans Y; les $\mathbf{Y}_i$ sont irréductibles, et l'on a $\mathbf{Y} = \cup \mathbf{Y}_i$; il existe donc $\mathbf{J} \subset \mathbf{I}$ tel que les $\mathbf{Y}_j$, $j \in \mathbf{J}$, soient les composantes irréductibles de Y. D'après le résultat rappelé au début, pour tout $j \in \mathbf{J}$, il existe une partie $\mathbf{U}_j \subset f(\mathbf{X}_j)$ qui est Z-ouverte et Z-dense dans $\mathbf{Y}_j$; quitte à restreindre $\mathbf{U}_j$, on peut en outre supposer que $\mathbf{U}_j$ ne rencontre aucun des $\mathbf{Y}_k$, $k \in \mathbf{J}$, $k \neq j$. En posant alors $\mathbf{U} = \bigcup_{j \in \mathbf{J}} \mathbf{U}_j$, on obtient un sous-ensemble de Y qui jouit de toutes les propriétés requises.

PROPOSITION 7. — Si $f\colon X \to Y$ est une application régulière d'une variété algébrique $X$ dans une variété algébrique $Y$, l'adhérence et la Z-adhérence de $f(X)$ dans $Y$ coïncident.

Soit T la Z-adhérence de $f(X)$ dans Y. En appliquant le lemme 2 à $f\colon X\to T$, on voit qu'il existe une partie $U\subset f(X)$

qui est Z-ouverte et Z-dense dans T. D'après la proposition 5, U est donc dense dans T, et il en est a fortiori de même de $f(X)$; ceci montre que T est contenu dans l'adhérence de $f(X)$; comme l'inclusion opposée est évidente, ceci achève la démonstration.

## 8. Un critère analytique de régularité.

On sait que toute application régulière est holomorphe. La proposition suivante (que nous complèterons d'ailleurs au n° 19) indique dans quel cas la réciproque est vraie.

PROPOSITION 8. — Soient X et Y deux variétés algébriques, et soit f: X → Y une application holomorphe de X dans Y. Si le graphe T de f est un sous-ensemble Z-localement fermé (i.e. une sous-variété algébrique) de X × Y, l'application f est régulière.

Soit $p = pr_{\mathrm{X}}$ la projection canonique de T sur le premier facteur X de $\mathrm{X} \times \mathrm{Y}$; l'application $p$ est régulière, bijective, et son application inverse est l'application $x \to (x, f(x))$ qui est holomorphe par hypothèse; donc $p$ est un isomorphisme analytique, et tout revient à montrer que $p$ est un isomorphisme birégulier (puisque l'on a $f = pr_{\mathrm{Y}} \circ p^{-1}$). C'est ce qui résulte de la proposition suivante:

PROPOSITION 9. — Soient T et X deux variétés algébriques, et soit $p: \mathrm{T} \to \mathrm{X}$ une application régulière bijective. Si $p$ est un isomorphisme analytique de T sur X, c'est aussi un isomorphisme birégulier.

Montrons d'abord que $p$ est un homéomorphisme pour les topologies de Zariski de T et de X. Soit F un sous-ensemble Z-fermé de T; puisque $p$ est un isomorphisme analytique, c'est a fortiori un homéomorphisme, et $p(\mathrm{F})$ est fermé dans X. En appliquant la proposition 7 à $p: \mathrm{F} \to \mathrm{X}$, on en conclut que $p(\mathrm{F})$ est Z-fermé dans X, ce qui démontre notre assertion.

Il nous reste maintenant à montrer que p transforme le faisceau  $O_{x}$  des anneaux locaux de X en le faisceau  $O_{T}$  des anneaux locaux de T. De façon plus précise, si t est un point de T, et si  $x = p(t)$ , l'application p définit un homomorphisme

$$
p ^ {*}: \quad \mathcal {O} _ {x, \mathrm{x}} \rightarrow \mathcal {O} _ {t, \mathrm{T}},
$$

et il nous faut prouver que $p^*$ est bijectif $(^2)$.

(2) La démonstration qui suit m'a été communiquée par P. SAMUEL.

Du fait que $p$ est un Z-homéomorphisme, $p^*$ est injectif, ce qui permet d'identifier $\mathcal{O}_{x,\mathbf{x}}$ à un sous-anneau de $\mathcal{O}_{t,\mathrm{T}}$. Pour simplifier l'écriture, nous poserons $A = \mathcal{O}_{x,\mathbf{x}}$, $A' = \mathcal{O}_{t,\mathrm{T}}$, de sorte que l'on a $A \subset A'$. De même, nous noterons $B$ (resp. $B'$) l'anneau $\mathcal{H}_{x,\mathbf{x}}$ (resp. $\mathcal{H}_{t,\mathrm{T}}$), et nous considérerons $A$ et $A'$ comme plongés respectivement dans $B$ et $B'$ (ce qui est licite, en vertu de la proposition 3). L'hypothèse que $p$ est un isomorphisme analytique signifie que $B = B'$.

Soient  $X_{i}$  les composantes irréductibles de X passant par x; chaque  $X_{i}$  détermine un idéal premier  $\mathfrak{p}_{i} = \mathfrak{I}_{x}(X_{i})$  de l'anneau A, et l'anneau local quotient  $A_{i} = A/\mathfrak{p}_{i}$  n'est autre que l'anneau local de x sur  $X_{i}$ ; le corps des quotients de  $A_{i}$, soit  $K_{i}$, n'est donc pas autre chose que le corps des fonctions rationnelles sur la variété irréductible  $X_{i}$. Les idéaux  $p_{i}$  sont évidemment les idéaux premiers minimaux de l'anneau A, et l'on a  $0 = \cap p_{i}$. L'ensemble S des éléments de A qui n'appartiennent à aucun des  $p_{i}$  est multiplicativement stable (il est facile de voir que c'est l'ensemble des éléments réguliers de A). L'anneau total de fractions  $A_{s}$  est égal au composé direct des corps  $K_{i}$  (cf. lemme 3 ci-après).

Soit  $T_{i}=p^{-1}(X_{i})$ ; puisque p est un Z-homéomorphisme, les  $T_{i}$  sont les composantes irréductibles de T passant par t, et définissent des idéaux premiers  $p_{i}^{\prime}$  de  $A^{\prime}$ ; on posera encore  $A_{i}^{\prime}=A^{\prime}/p_{i}^{\prime}$ , et l'on désignera par  $K_{i}^{\prime}$  le corps des fractions de  $A_{i}^{\prime}$ ; l'anneau total de fractions  $A_{s}^{\prime}$  est égal au composé direct des  $K^{\prime}$ . Notons que  $p_{i}^{\prime}\cap A=p_{i}$ , d'où  $A_{i}\subset A_{i}^{\prime}$ ,  $K_{i}\subset K_{i}^{\prime}$  et  $A_{s}\subset A_{s}^{\prime}$ .

Nous allons d'abord montrer que  $K_{i} = K_{i}'$ , autrement dit que p définit une correspondance « birationnelle » entre  $T_{i}$  et  $X_{i}$ ; puisque  $p: T_{i} \to X_{i}$  est un Z-homéomorphisme,  $T_{i}$  et  $X_{i}$  ont même dimension, et les corps  $K_{i}$  et  $K_{i}'$  ont même degré de transcendance sur C. Si l'on pose alors  $n_{i} = [K_{i}' : K_{i}]$ , on sait (3) qu'il existe un sous-ensemble Z-ouvert et non vide  $U_{i}$  de  $X_{i}$  tel que l'image réciproque de tout point de  $U_{i}$  se compose d'exactement  $n_{i}$  points de  $T_{i}$ . Comme p est bijectif, ceci montre que  $n_{i} = 1$ , et l'on a bien  $K_{i} = K_{i}'$ .

Puisque $\mathbf{A}_{\mathrm{s}}$ (resp. $\mathbf{A}_{\mathrm{s}^{\prime}}^{\prime}$) est composé direct des $\mathbf{K}_{i}$ (resp.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(3) C'est un résultat classique, et facile à démontrer, sur les correspondances. On trouvera dans [17], p. 16 un résultat un peu plus faible, mais suffisant pour l'application que nous en faisons.</span></small>

des K$_{i}^{\prime}$), il s'ensuit que A$_{s}$ = A$_{s}^{\prime}$. Soit alors f'∈A'; vu ce qui précède, on a f'∈A$_{s}$, autrement dit il existe g∈A et s∈S tels que g = sf'. On a donc g∈sA', d'où g∈sB', c'est-à-dire g∈sB. Mais, d'après le cor. 1 à la prop. 3, le couple (A, B) est un couple plat, et l'on a donc sB ∩ A = sA, cf. Annexe, n° 22. On en tire g∈sA, autrement dit, il existe f∈A tel que g = sf, ou encore s(f - f') = 0, et, comme s est non diviseur de zéro dans A', ceci entraîne f = f', c'est-à-dire A = A', cqfd.

Nous avons utilisé en cours de démonstration le résultat suivant, que nous allons maintenant démontrer:

LEMME 3. — Soit A un anneau commutatif, dans lequel l'idéal 0 soit intersection d'un nombre fini d'idéaux premiers minimaux distincts $\mathfrak{p}_i$; soit $\mathrm{K}_i$ le corps des fractions de $\mathrm{A} / \mathfrak{p}_i$, et soit S l'ensemble des éléments de A qui n'appartiennent à aucun des $\mathfrak{p}_i$. L'anneau de fractions $\mathrm{A}_{\mathrm{s}}$ est alors isomorphe au composé direct des $\mathrm{K}_i$.

On sait que les idéaux premiers de  $A_{s}$  correspondent biunivoquement à ceux des idéaux premiers de A qui ne rencontrent pas S (cf. [15], chap. IV, § 3, auquel nous renvoyons pour tout ce qui concerne les anneaux de fractions). Il s'ensuit que, si l'on pose  $m_{i} = p_{i}A_{s}$ , les  $m_{i}$  sont les seuls idéaux premiers de  $A_{s}$ ; en particulier, ce sont des idéaux maximaux, évidemment distincts, puisque  $m_{i} \cap A = p_{i}$  ([15], loc. cit.). De plus, le corps  $A_{s}/m_{i}$  est engendré par  $A/p_{i}$ , donc coïncide avec  $K_{i}$ . Il reste à montrer que l'homomorphisme canonique

$$
\varphi : \mathrm{A} _ {\mathrm{s}} \rightarrow \prod \mathrm{A} _ {\mathrm{s}} / \mathfrak {m} _ {i} = \prod \mathrm{K} _ {i}
$$

est bijectif.

Tout d'abord, la relation $\cap \mathfrak{p}_i = 0$ entraîne $\cap \mathfrak{m}_i = 0$, ce qui montre que $\varphi$ est injectif. Désignons alors par $\mathfrak{b}_i$ le produit (dans l'anneau $\mathrm{A_s}$) des idéaux $\mathfrak{m}_j$, $j \neq i$, et posons $\mathfrak{b} = \sum \mathfrak{b}_i$. L'idéal $\mathfrak{b}$ n'est contenu dans aucun des $\mathfrak{m}_i$, donc est identique à $\mathrm{A_s}$, et il existe des éléments $x_i \in \mathfrak{b}_i$ tels que $\sum x_i = 1$. On a:

$$
x _ {i} \equiv 1 \pmod {\mathfrak {m} _ {i}} \quad \text { et } \quad x _ {i} \equiv 0 \pmod {\mathfrak {m} _ {j}}, \quad j \neq i,
$$

ce qui montre que $\varphi(\mathrm{A}_{\mathrm{s}})$ contient les éléments $(1,0,\ldots,0),\ldots,(0,\ldots,0,1)$ de $\prod\mathrm{K}_{i}$. Comme ces éléments engendrent le $\mathrm{A}_{\mathrm{s}}$-module $\prod\mathrm{K}_{i}$, cela montre bien que $\varphi$ est bijectif, et achève la démonstration.

## § 3. — Correspondance entre faisceaux algébriques et faisceaux analytiques cohérents.

## 9. Faisceau analytique associé à un faisceau algébrique.

Soit X une variété algébrique, et soit  $X^{h}$  l'espace analytique qui lui est associé par le procédé du n° 5. Si F est un faisceau quelconque sur X, nous munirons l'ensemble F d'une nouvelle topologie, qui en fait un faisceau sur  $X^{h}$ ; cette topologie est définie de la manière suivante : si  $\pi: F \to X$  désigne la projection de F sur X, on plonge F dans  $X^{h} \times F$  par l'application  $f \to (\pi(f), f)$ , et la topologie en question est celle induite sur F par celle de  $X^{h} \times F$ . On vérifie tout de suite que l'on a ainsi muni l'ensemble F d'une structure de faisceau sur  $X^{h}$ , faisceau que nous désignerons par F'. Pour tout  $x \in X$ , on a donc  $F_{x}' = F_{x}$ ; les faisceaux F et F' ne diffèrent que par leur topologie (F' n'est pas autre chose que l'image réciproque de F par l'application continue  $X^{h} \to X$ ).

Ce qui précède s'applique notamment au faisceau O des anneaux locaux de X; la prop. 3 du n° 6 nous permet d'identifier le faisceau O ainsi obtenu à un sous-faisceau du faisceau H des germes de fonctions holomorphes sur X$^{h}$.

DÉFINITION 2. — Soit F un faisceau algébrique sur X. On appelle faisceau analytique associé à F, le faisceau $\mathcal{F}^{h}$ sur $X^{h}$ défini par la formule:

$$
\mathcal {F} ^ {h} = \mathcal {F} ^ {\prime} \otimes \mathcal {H},
$$

le produit tensoriel étant pris sur le faisceau d'anneaux O'.
(Autrement dit, $\mathcal{F}^h$ se déduit de $\mathcal{F}'$ par extension de l'anneau d'opérateurs à $\mathcal{H}$).

Le faisceau $\mathcal{F}^{h}$ est un faisceau de $\mathcal{H}$-modules, c'est-à-dire un faisceau analytique; l'injection $\mathcal{O}' \to \mathcal{H}$ définit un homomorphisme canonique $\alpha: \mathcal{F}' \to \mathcal{F}^{h}$.

Tout homomorphisme algébrique (c'est-à-dire O-linéaire)

$$
\varphi : \quad \mathcal {F} \rightarrow \mathcal {G}
$$

définit, par extension de l'anneau d'opérateurs, un homomorphisme analytique

$$
\varphi^ {h}: \quad \mathcal {F} ^ {h} \rightarrow \mathcal {G} ^ {h}.
$$

Ainsi $\mathcal{F}^h$ est un foncteur covariant de $\mathcal{F}$.

PROPOSITION 10. — a) Le foncteur $\mathcal{F}^{h}$ est un foncteur exact.

b) Pour tout faisceau algébrique $\mathcal{F}$, l'homomorphisme $\alpha: \mathcal{F}' \to \mathcal{F}^h$ est injectif.

c) Si F est un faisceau algébrique cohérent,  $F^{h}$  est un faisceau analytique cohérent.

Si $\mathcal{F}_{1}\to\mathcal{F}_{2}\to\mathcal{F}_{3}$ est une suite exacte de faisceaux algébriques, il en est évidemment de même de la suite $\mathcal{F}_{1}^{\prime}\to\mathcal{F}_{2}^{\prime}\to\mathcal{F}_{3}$, donc aussi de la suite

$$
\mathcal {F} _ {1} ^ {\prime} \otimes \mathcal {H} \rightarrow \mathcal {F} _ {2} ^ {\prime} \otimes \mathcal {H} \rightarrow \mathcal {F} _ {3} ^ {\prime} \otimes \mathcal {H},
$$

d'après le cor. 1 à la prop. 3, ce qui démontre a). L'assertion b) résulte également du même corollaire.

Pour démontrer c) remarquons d'abord que l'on a  $O^{h} = H$ ; si alors F est algébrique cohérent, et si x est un point de X, on peut trouver une suite exacte :

$$
\mathcal {O} ^ {q} \rightarrow \mathcal {O} ^ {p} \rightarrow \mathscr {F} \rightarrow 0,
$$

valable dans un Z-voisinage U de x. D'après a), on en déduit une suite exacte :

$$
\mathcal {H} ^ {q} \rightarrow \mathcal {H} ^ {p} \rightarrow \mathcal {F} ^ {h} \rightarrow 0,
$$

valable sur U. Comme U est un voisinage de x, et que le faisceau d'anneaux H est cohérent (prop. 1, n° 3), ceci montre bien que $\mathcal{F}^{h}$ est cohérent ([18], n° 15).

La proposition précédente montre en particulier que, si $\mathfrak{J}$ est un faisceau d'idéaux de $\mathcal{O}$, le faisceau $\mathfrak{J}^h$ n'est autre que le faisceau d'idéaux de $\mathcal{H}$ engendré par les éléments de $\mathfrak{J}$.

## 10. Prolongement d'un faisceau.

Soit Y une sous-variété Z-fermée de la variété algébrique X, et soit F un faisceau algébrique cohérent sur Y. Si l'on note  $F^{X}$  le faisceau obtenu en prolongeant F par 0 sur X — Y (cf. [18], n° 5), on sait que  $F^{X}$  est un faisceau algébrique cohérent sur X, et le faisceau  $(\mathcal{F}^{\mathrm{X}})^{h}$  est bien défini; c'est un faisceau analytique cohérent sur  $X^{h}$ . Mais, d'autre part, le faisceau  $F^{h}$  est un faisceau analytique cohérent sur  $Y^{h}$ , que l'on peut prolonger par 0 sur  $X^{h}$ —  $Y^{h}$ , obtenant ainsi un nouveau faisceau  $(\mathcal{F}^{h})^{\mathrm{X}}$ . On a :

PROPOSITION 11. — Les faisceaux $(\mathcal{F}^h)^X$ et $(\mathcal{F}^X)^h$ sont canoniquement isomorphes.

Les deux faisceaux en question sont nuls en dehors de  $Y^{h}$ ; il nous suffira donc de montrer que leurs restrictions à  $Y^{h}$  sont isomorphes.

Soit $x$ un point de Y. Posons, pour simplifier les notations :

$$
\mathrm{A} = \mathcal {O} _ {x, \mathrm{x}}, \quad \mathrm{A} ^ {\prime} = \mathcal {O} _ {x, \mathrm{y}}, \quad \mathrm{B} = \mathcal {H} _ {x, \mathrm{x}}, \quad \mathrm{B} ^ {\prime} = \mathcal {H} _ {x, \mathrm{y}}, \quad \mathrm{E} = \mathcal {F} _ {x}.
$$

On a alors :

$$
(\mathcal {F} ^ {h}) _ {x} ^ {\mathrm{X}} = \mathrm{E} \otimes_ {\mathrm{A}} \mathrm{B} ^ {\prime} \quad \text { et } \quad (\mathcal {F} ^ {\mathrm{X}}) _ {x} ^ {h} = \mathrm{E} \otimes_ {\mathrm{A}} \mathrm{B}.
$$

L'anneau A' est le quotient de A par un idéal a, et, d'après la prop. 4 du n° 6, on a B' = B/àB = B⊗A'. En vertu de l'associativité du produit tensoriel, on obtient alors un isomorphisme :

$$
\theta_ {x}: \mathrm{E} \otimes_ {\mathbf {A} ^ {\prime}} \mathrm{B} ^ {\prime} = \mathrm{E} \otimes_ {\mathbf {A} ^ {\prime}} \mathrm{A} ^ {\prime} \otimes_ {\mathbf {A}} \mathrm{B} \rightarrow \mathrm{E} \otimes_ {\mathbf {A}} \mathrm{B},
$$

qui varie continûment avec $x$, comme on le voit aisément; la proposition en résulte.

On peut exprimer la proposition 11 en disant que le foncteur $\mathcal{F}^{h}$ est compatible avec l'identification usuelle de $\mathcal{F}$ avec $\mathcal{F}^{\mathrm{X}}$.

## 11. Homomorphismes induits sur la cohomologie.

Les notations étant les mêmes qu'au n° 9, soient X une variété algébrique, F un faisceau algébrique sur X, et $\mathcal{F}^h$ le faisceau analytique associé à $\mathcal{F}$. Si U est un sous-ensemble Z-ouvert de X, et si s est une section de $\mathcal{F}$ au-dessus de U, on peut considérer s comme une section $s'$ de $\mathcal{F}'$ au-dessus de l'ouvert $\mathrm{U}^h$ de $\mathrm{X}^h$, et $\alpha(s') = s' \otimes 1$ est une section de $\mathcal{F}^h = \mathcal{F}' \otimes \mathcal{H}$ au-dessus de $\mathrm{U}^h$. L'application $s \to \alpha(s')$ est un homomorphisme

$$
\varepsilon : \Gamma (\mathrm{U}, \mathcal {F}) \rightarrow \Gamma (\mathrm{U} ^ {h}, \mathcal {F} ^ {h}).
$$

Soit maintenant $\mathfrak{U}=\{\mathrm{U}_{i}\}$ un recouvrement Z-ouvert fini de X; les $\mathrm{U}_{i}^{h}$ forment un recouvrement ouvert fini de $X^{h}$, que nous noterons $\mathfrak{U}^{h}$. Pour tout système d'indices $i_{0},\ldots,i_{q}$, on a, d'après ce qui précède, un homomorphisme canonique

$$
\varepsilon : \Gamma (\mathrm{U} _ {i _ {0}} \cap \dots \cap \mathrm{U} _ {i _ {q}}, \mathcal {F}) \rightarrow \Gamma (\mathrm{U} _ {i _ {0}} ^ {h} \cap \dots \cap \mathrm{U} _ {i _ {q}} ^ {h}, \mathcal {F} ^ {h}),
$$

d'où un homomorphisme

$$
\varepsilon : \mathrm{C} (\mathfrak {U}, \mathscr {F}) \rightarrow \mathrm{C} (\mathfrak {U} ^ {h}, \mathscr {F} ^ {h}),
$$

avec les notations de [18], n° 18.

Cet homomorphisme commute avec le cobord d, donc définit, par passage à la cohomologie, de nouveaux homomorphismes :

$$
\varepsilon : \mathrm{H} ^ {q} (\mathfrak {U}, \mathscr {F}) \rightarrow \mathrm{H} ^ {q} (\mathfrak {U} ^ {h}, \mathscr {F} ^ {h}).
$$

Enfin, par passage à la limite inductive sur $\mathfrak{U}$, on obtient les homomorphismes induits sur les groupes de cohomologie

$$
\varepsilon : \mathrm{H} ^ {q} (\mathrm{X}, \mathcal {F}) \rightarrow \mathrm{H} ^ {q} (\mathrm{X} ^ {h}, \mathcal {F} ^ {h}).
$$

Ces homomorphismes jouissent des propriétés fonctorielles usuelles; ils commutent avec les homomorphismes $\varphi: \mathcal{F} \to \mathcal{G}$; si l'on a une suite exacte de faisceaux algébriques :

$$
0 \rightarrow \mathcal {A} \rightarrow \mathcal {B} \rightarrow \mathcal {C} \rightarrow 0,
$$

où le faisceau à est cohérent, le diagramme :

$$
\begin{array}{c} \mathrm{H} ^ {q} (\mathrm{X}, \mathcal {C}) \xrightarrow {\delta} \mathrm{H} ^ {q + 1} (\mathrm{X}, \mathcal {A}) \\ \varepsilon \downarrow \qquad \qquad \qquad \qquad \qquad \varepsilon \downarrow \\ \mathrm{H} ^ {q} (\mathrm{X} ^ {h}, \mathcal {C} ^ {h}) \xrightarrow {\delta} \mathrm{H} ^ {q + 1} (\mathrm{X} ^ {h}, \mathcal {A} ^ {h}) \end{array}
$$

est commutatif : cela se voit, par exemple, en prenant pour recouvrements $\mathfrak{U}$ des recouvrements par des ouverts affines (cf. [18]).

## 12. Variétés projectives. Énoncé des théorèmes.

Supposons que X soit une variété projective, c'est-à-dire une sous-variété Z-fermée d'un espace projectif  $\mathbf{P}_{r}(\mathbb{C})$ . On a alors les théorèmes suivants, que nous démontrerons dans la suite de ce paragraphe :

THÉORÈME 1. — Pour tout faisceau algébrique cohérent F sur X, et pour tout entier $q \geqslant 0$, l'homomorphisme

$$
\varepsilon : \quad \mathrm{H} ^ {q} (\mathrm{X}, \mathcal {F}) \rightarrow \mathrm{H} ^ {q} (\mathrm{X} ^ {h}, \mathcal {F} ^ {h}),
$$

défini au n° 11, est bijectif.

Pour $q=0$ on obtient en particulier un isomorphisme de $\Gamma(X, \mathcal{F})$ sur $\Gamma(X^{h}, \mathcal{F}^{h})$.

THÉORÈME 2. — Si F et G sont deux faisceaux algébriques cohérents sur X, tout homomorphisme analytique de F$^{h}$ dans G$^{h}$ provient d'un homomorphisme algébrique de F dans G, et d'un seul.

THÉORÈME 3. — Pour tout faisceau analytique cohérent $\mathfrak{M}$ sur $X^{h}$, il existe un faisceau algébrique cohérent $\mathcal{F}$ sur X tel que $\mathcal{F}^{h}$ soit isomorphe à $\mathfrak{M}$. De plus, cette propriété détermine $\mathcal{F}$ de façon unique, à un isomorphisme près.

REMARQUES — 1. Ces trois théorèmes signifient que la théorie des faisceaux analytiques cohérents sur $X^h$ coïncide essentiellement avec celle des faisceaux algébriques cohérents sur $X$. Bien entendu, ils tiennent à ce que $X$ est une variété projective, et sont inexacts même pour une variété affine.

2. On peut factoriser ε en :

$$
\mathrm{H} ^ {q} (\mathrm{X}, \mathcal {F}) \rightarrow \mathrm{H} ^ {q} (\mathrm{X} ^ {h}, \mathcal {F} ^ {\prime}) \rightarrow \mathrm{H} ^ {q} (\mathrm{X} ^ {h}, \mathcal {F} ^ {h}).
$$

Le théorème 1 conduit à se demander si $\mathrm{H}^q (\mathbf{X},\mathcal{F})\to \mathrm{H}^q (\mathbf{X}^h,\mathcal{F}')$ est bijectif. La réponse est négative; en effet, si cet homomorphisme était bijectif pour tout faisceau algébrique cohérent $\mathcal{F}$, il le serait aussi pour le faisceau constant $\mathrm{K} = \mathbb{C}(\mathrm{X})$ des fonctions rationnelles sur X (supposé irréductible), puisque ce faisceau est réunion de faisceaux cohérents (comparer avec [19], §2); or, on a $\mathrm{H}^q (\mathrm{X},\mathrm{K}) = 0$ pour $q > 0$, alors que $\mathrm{H}^q (\mathrm{X}^h,\mathrm{K})$ est un K-espace vectoriel de dimension égale au $q$-ème nombre de Betti de $\mathbf{X}^h$.

## 13. Démonstration du théorème 1.

Supposons X plongé dans l'espace projectif  $\mathbf{P}_{r}(\mathbb{C})$ ; si nous identifions F avec le faisceau obtenu en le prolongeant par 0 en dehors de X, on sait ([18], n° 26) que l'on a :

$$
\mathrm{H} ^ {q} (\mathrm{X}, \mathscr {F}) = \mathrm{H} ^ {q} \left(\mathrm{P} _ {r} (\mathrm{C}), \mathscr {F}\right) \quad \text { et } \quad \mathrm{H} ^ {q} \left(\mathrm{X} ^ {h}, \mathscr {F} ^ {h}\right) = \mathrm{H} ^ {q} \left(\mathrm{P} _ {r} (\mathrm{C}) ^ {h}, \mathscr {F} ^ {h}\right),
$$

la notation $\mathcal{F}^h$ étant justifiée par la proposition 11. On voit donc qu'il suffit de prouver que

$$
\varepsilon : \quad \mathrm{H} ^ {q} (\mathbf {P} _ {r} (\mathbf {C}), \mathcal {F}) \rightarrow \mathrm{H} ^ {q} (\mathbf {P} _ {r} (\mathbf {C}) ^ {h}, \mathcal {F} ^ {h})
$$

est bijectif, autrement dit, on est ramené au cas où  $X = \mathbf{P}_{r}(\mathbb{C})$ . Nous établirons tout d'abord deux lemmes :

LEMME 4. — Le théorème 1 est vrai pour le faisceau O.

Pour $q=0$, $\mathrm{H}^{0}(\mathrm{X},\mathcal{O})$ et $\mathrm{H}^{0}(\mathrm{X}^{h},\mathcal{O}^{h})$ sont tous deux réduits aux constantes. Pour $q>0$, on sait que $\mathrm{H}^{q}(\mathrm{X},\mathcal{O})=0$, cf. [18], n° 65, proposition 8; d'autre part, d'après le théorème de Dolbeault (cf. [8]), $\mathrm{H}^{q}(\mathrm{X}^{h},\mathcal{O}^{h})$ est isomorphe à la coho-

mologie de type  $(0, q)$  de l'espace projectif X, donc est réduit à 0, c.q.f.d. (4).

LEMME 5. — Le théorème 1 est vrai pour le faisceau $\mathcal{O}(n)$. (Pour la définition de $\mathcal{O}(n)$, cf. [18], n° 54, ainsi que le n° 16 ci-après).

Nous raisonnerons par récurrence sur $r = \dim X$, le cas $r = 0$ étant trivial. Soit $t$ une forme linéaire non identiquement nulle en les coordonnées homogènes $t_0, \ldots, t_r$, et soit E l'hyperplan défini par l'équation $t = 0$. On a une suite exacte :

$$
0 \rightarrow \mathcal {O} (- 1) \rightarrow \mathcal {O} \rightarrow \mathcal {O} _ {\mathrm{E}} \rightarrow 0,
$$

où $\mathcal{O} \to \mathcal{O}_{\mathrm{E}}$ est l'homomorphisme de restriction, alors que $\mathcal{O}(-1) \to \mathcal{O}$ est la multiplication par $t$ (cf. [18], n° 81). De là, on déduit une suite exacte, valable pour tout $n \in \mathbb{Z}$:

$$
0 \rightarrow \mathcal {O} (n - 1) \rightarrow \mathcal {O} (n) \rightarrow \mathcal {O} _ {\mathrm{E}} (n) \rightarrow 0.
$$

D'après le n° 11, on a un diagramme commutatif :

$$
\begin{array}{c} \dots \to \mathrm{H} ^ {q} (\mathrm{X}, \mathcal {O} (n - 1)) \to \mathrm{H} ^ {q} (\mathrm{X}, \mathcal {O} (n)) \to \mathrm{H} ^ {q} (\mathrm{E}, \mathcal {O} _ {\mathbf {E}} (n)) \to \mathrm{H} ^ {q + 1} (\mathrm{X}, \mathcal {O} (n - 1)) \to \dots \\ \varepsilon \downarrow \quad \varepsilon \downarrow \quad \varepsilon \downarrow \quad \varepsilon \downarrow \\ \dots \to \mathrm{H} ^ {q} (\mathrm{X} ^ {h}, \mathcal {O} (n - 1) ^ {h}) \to \mathrm{H} ^ {q} (\mathrm{X} ^ {h}, \mathcal {O} (n) ^ {h}) \to \mathrm{H} ^ {q} (\mathrm{E} ^ {h}, \mathcal {O} _ {\mathbf {E}} (n) ^ {h}) \to \mathrm{H} ^ {q + 1} (\mathrm{X} ^ {h}, \mathcal {O} (n - 1) ^ {h}) \to \dots \end{array}
$$

Vu l'hypothèse de récurrence, l'homomorphisme

$$
\varepsilon : \mathrm{H} ^ {q} (\mathrm{E}, \mathcal {O} _ {\mathrm{E}} (n)) \rightarrow \mathrm{H} ^ {q} (\mathrm{E} ^ {h}, \mathcal {O} _ {\mathrm{E}} (n) ^ {h})
$$

est bijectif pour tout $q \geqslant 0$ et tout $n \in \mathbb{Z}$. En appliquant le lemme des cinq, on voit alors que, si le théorème 1 est vrai pour $\mathcal{O}(n)$, il est vrai pour $\mathcal{O}(n - 1)$, et réciproquement. Comme il est vrai pour $n = 0$ d'après le lemme 4, il est donc vrai pour tout $n$.

Nous pouvons maintenant passer à la démonstration du théorème 1. Nous raisonnerons par récurrence descendante sur $q$, le théorème étant trivial pour $q > 2r$, puisque $\mathrm{H}^{q}(\mathrm{X},\mathcal{F})$ et $\mathrm{H}^{q}(\mathrm{X}^{h},\mathcal{F}^{h})$ sont alors nuls tous les deux. D'après [18], n° 55, cor. au th. 1, il existe une suite exacte de faisceaux algébriques cohérents :

$$
0 \rightarrow \mathcal {R} \rightarrow \mathscr {L} \rightarrow \mathscr {F} \rightarrow 0,
$$

(4) On peut aussi calculer directement Hq(X, O) en utilisant le recouvrement ouvert de X défini au n° 16, ainsi que des développements en séries de LAURENT (J. FRENKEL, non publié). On évite ainsi tout recours à la théorie des variétés kählériennes.

où ℒ est somme directe de faisceaux isomorphes à ℒ(n); vu le lemme 5, le théorème 1 est vrai pour le faisceau ℒ.

On a un diagramme commutatif :

$$
\begin{array}{c c c c c c}\mathrm{H} ^ {q} (\mathrm{X}, \mathcal {R})&\rightarrow&\mathrm{H} ^ {q} (\mathrm{X}, \mathcal {L})&\rightarrow&\mathrm{H} ^ {q} (\mathrm{X}, \mathcal {F})&\rightarrow&\mathrm{H} ^ {q + 1} (\mathrm{X}, \mathcal {R})\\\varepsilon_ {1} \downarrow&&\varepsilon_ {2} \downarrow&&\varepsilon_ {3} \downarrow&&\varepsilon_ {4} \downarrow\\\mathrm{H} ^ {q} (\mathrm{X} ^ {h}, \mathcal {R} ^ {h})&\rightarrow&\mathrm{H} ^ {q} (\mathrm{X} ^ {h}, \mathcal {L} ^ {h})&\rightarrow&\mathrm{H} ^ {q} (\mathrm{X} ^ {h}, \mathcal {F} ^ {h})&\rightarrow&\mathrm{H} ^ {q + 1} (\mathrm{X} ^ {h}, \mathcal {R} ^ {h})\\\end{array}
$$

Dans ce diagramme, les homomorphismes $\varepsilon_{4}$ et $\varepsilon_{5}$ sont bijectifs, d'après l'hypothèse de récurrence; d'après ce que l'on vient de dire, il en est de même de $\varepsilon_{2}$. Le lemme des cinq montre donc que $\varepsilon_{3}$ est surjectif. Ce résultat, étant valable pour tout faisceau algébrique cohérent $\mathcal{F}$ s'applique en particulier à $\mathcal{R}$, ce qui montre que $\varepsilon_{1}$ est surjectif. Une nouvelle application du lemme des cinq montre alors que $\varepsilon_{3}$ est bijectif, ce qui achève la démonstration.

## 14. Démonstration du théorème 2.

Soit $\mathcal{A} = \operatorname{Hom}(\mathcal{F}, \mathcal{G})$ le faisceau des germes d'homomorphismes de $\mathcal{F}$ dans $\mathcal{G}$ (cf. [18], n$^{\text{os}}$ 11 et 14). Un élément $f \in \mathcal{A}_x$ est un germe d'homomorphisme de $\mathcal{F}$ dans $\mathcal{G}$, au voisinage de $x$, donc définit un germe d'homomorphisme $f^h$ du faisceau analytique $\mathcal{F}^h$ dans le faisceau $\mathcal{G}^h$; l'application $f \to f^h$ est un homomorphisme $\mathcal{O}'$-linéaire du faisceau $\mathcal{A}'$ défini par $\mathcal{A}$ (cf. n$^0$ 9) dans le faisceau $\mathcal{B} = \operatorname{Hom}(\mathcal{F}^h, \mathcal{G}^h)$; cet homomorphisme se prolonge par linéarité en un homomorphisme

$$
i: \quad \mathcal {A} ^ {h} \rightarrow \mathcal {B}.
$$

LEMME 6. — L'homomorphisme $\iota: \mathcal{A}^h \to \mathcal{B}$ est bijectif.
Soit $x \in X$. Puisque $\mathscr{F}$ est cohérent, on a, d'après [18], n° 14 :

$$
\mathscr {A} _ {x} = \operatorname{Hom} \left(\mathscr {F} _ {x}, \mathscr {G} _ {x}\right) \quad \text { d'où } \quad \mathscr {A} _ {x} ^ {h} = \operatorname{Hom} \left(\mathscr {F} _ {x}, \mathscr {G} _ {x}\right) \otimes \mathscr {H} _ {x},
$$

les foncteurs $\otimes$ et Hom étant pris sur l'anneau $\mathcal{O}_{x}$.

Puisque $\mathfrak{F}^{h}$ est cohérent, on a de même :

$$
\mathcal {B} _ {x} = \operatorname{Hom} \left(\mathscr {F} _ {x} \otimes \mathscr {H} _ {x}, \mathscr {G} _ {x} \otimes \mathscr {H} _ {x}\right),
$$

le foncteur $\otimes$ étant pris sur $\mathcal{O}_{x}$, et le foncteur Hom sur $\mathcal{H}_{x}$. Tout revient donc à voir que l'homomorphisme

$$
\iota_ {x}: \quad \operatorname{Hom} \left(\mathcal {F} _ {x}, \mathcal {G} _ {x}\right) \otimes \mathcal {H} _ {x} \rightarrow \operatorname{Hom} \left(\mathcal {F} _ {x} \otimes \mathcal {H} _ {x}, \mathcal {G} _ {x} \otimes \mathcal {H} _ {x}\right)
$$

est bijectif, ce qui résulte du fait que le couple  $(\mathcal{O}_{x}, \mathcal{H}_{x})$  est plat et de la prop. 21 de l'Annexe.

Démontrons maintenant le théorème 2. Considérons les homomorphismes

$$
\mathrm{H} ^ {0} (\mathrm{X}, \mathscr {A}) \xrightarrow {\varepsilon} \mathrm{H} ^ {0} (\mathrm{X} ^ {h}, \mathscr {A} ^ {h}) \xrightarrow {\iota} \mathrm{H} ^ {0} (\mathrm{X} ^ {h}, \mathscr {B}).
$$

Un élément de $\mathrm{H}^0 (\mathbf{X}^h,\mathcal{A})$ (resp. de $\mathrm{H}^0 (\mathbf{X}^h,\mathcal{B}))$ n'est pas autre chose qu'un homomorphisme de $\mathcal{F}$ dans $\mathcal{G}$ (resp. de $\mathcal{F}^h$ dans $\mathcal{G}^h$). De plus, si $f\in \mathrm{H}^0 (\mathbf{X},\mathcal{A})$, on a $\iota \circ \varepsilon (f) = f^h$, par définition même de $\iota$. Le théorème 2 revient donc à affirmer que $\iota \circ \varepsilon$ est bijectif. Or $\varepsilon$ est bijectif d'après le théorème 1 (qui est applicable parce que $\mathcal{A}$ est cohérent, d'après [18], no 14), et $\iota$ est bijectif d'après le lemme 6, c.q.f.d.

## 15. Démonstration du théorème 3. Préliminaires.

L'unicité du faisceau $\mathcal{F}$ résulte du théorème 2. En effet, si $\mathcal{F}$ et $\mathcal{G}$ sont deux faisceaux algébriques cohérents sur X répondant à la question, il existe par hypothèse un isomorphisme $g: \mathcal{F}^h \to \mathcal{G}^h$. D'après le théorème 2, il existe donc un homomorphisme $f: \mathcal{F} \to \mathcal{G}$ tel que $g = f^h$. Si l'on désigne par $\mathcal{A}$ et $\mathcal{B}$ le noyau et le conoyau de $f$, on a une suite exacte :

$$
0 \rightarrow \mathcal {A} \rightarrow \mathcal {F} \xrightarrow {f} \mathcal {G} \rightarrow \mathcal {B} \rightarrow 0,
$$

d'où, d'après la prop. 10 a), une suite exacte :

$$
0 \rightarrow \mathcal {A} ^ {h} \rightarrow \mathcal {F} ^ {h} \xrightarrow {g} \mathcal {G} ^ {h} \rightarrow \mathcal {B} ^ {h} \rightarrow 0.
$$

Puisque $g$ est bijectif, ceci entraîne $\mathcal{A}^h = \mathcal{B}^h = 0$, d'où, d'après la prop. 10 b), $\mathcal{A} = \mathcal{B} = 0$, ce qui montre bien que $f$ est bijectif.

Reste à démontrer l'existence de $\mathcal{F}$. Je dis que l'on peut se borner au cas où X est un espace projectif $\mathbf{P}_{r}(\mathbb{C})$. En effet, soit Y une sous-variété algébrique de $X = \mathbf{P}_{r}(\mathbb{C})$, et soit $\mathcal{M}$ un faisceau analytique cohérent sur $Y^{h}$. Le faisceau $\mathcal{M}^{x}$ obtenu en prolongeant $\mathcal{M}$ par 0 en dehors de $Y^{h}$ est un faisceau analytique cohérent sur $X^{h}$. Si l'on suppose le théorème 3 démontré pour l'espace X, il existe donc un faisceau algébrique cohérent $\mathcal{G}$ sur X tel que $\mathcal{G}^{h}$ soit isomorphe à $\mathcal{M}^{x}$. Soit $\mathcal{I} = \mathcal{I}(Y)$ le faisceau cohérent d'idéaux défini par la sous-variété Y. Si $f \in \mathcal{J}_{x}$, la multiplication par $f$ est un endomorphisme $\varphi$ de $\mathcal{G}_{f x}$; l'endomorphisme $\varphi^{h}$ de $\mathcal{G}_{f x}^{h} = \mathcal{M}_{x}^{x}$ est réduit à 0, puisque $\mathcal{M}$ est un faisceau

analytique cohérent sur  $Y^{h}$ ; il en est donc de même de  $\varphi$ , d'après la prop. 10 b). Ainsi, l'on a J. G = 0, ce qui signifie qu'il existe un faisceau algébrique cohérent F sur Y, tel que  $G = F^{X}$  ([18], n° 39, prop. 3). D'après la prop. 11,  $(\mathcal{F}^{h})^{X}$  est isomorphe à  $(\mathcal{F}^{X})^{h} = \mathcal{G}^{h}$ , lequel est isomorphe à  $M_{b}^{X}$ . Par restriction à Y, on voit que  $F^{h}$  est isomorphe à M, ce qui démontre notre assertion.

## 16. Démonstration du théorème 3. Les faisceaux $\mathfrak{M}(n)$.

Vu le n° précédent, nous supposerons que  $X = \mathbf{P}_{r}(\mathbb{C})$ , et nous raisonnerons par récurrence sur r, le cas r = 0 étant trivial.

Pour tout $n\in\mathbb{Z}$, nous définirons d'abord un nouveau faisceau analytique, le faisceau $\mathcal{M}(n)$:

Soient $t_0, \ldots, t_r$ un système de coordonnées homogènes dans X, et soit $U_i$ l'ensemble ouvert formé des points où $t_i \neq 0$; nous noterons $\mathfrak{M}_i$ la restriction du faisceau $\mathfrak{M}$ à $U_i$; la multiplication par $t_j^n / t_i^n$ est un isomorphisme de $\mathfrak{M}_j$ sur $\mathfrak{M}_i$, défini au-dessus de $U_i \cap U_j$. Le faisceau $\mathfrak{M}(n)$ est alors défini par recollement des faisceaux $\mathfrak{M}_i$ au moyen des isomorphismes précédents (cf. [18], n° 54, où la même construction est appliquée aux faisceaux algébriques). Le faisceau $\mathfrak{M}(n)$ est localement isomorphe à $\mathfrak{M}$, donc cohérent puisque $\mathfrak{M}$ l'est; on a un isomorphisme canonique $\mathfrak{M}(n) = \mathfrak{M} \otimes \mathcal{H}(n)$, le produit tensoriel étant pris sur $\mathcal{H}$. Si $\mathcal{F}$ est un faisceau algébrique, on a $\mathcal{F}^h(n) = \mathcal{F}(n)^h$.

LEMME 7. — Soit E un hyperplan de $\mathbf{P}_{r}(\mathbb{C})$, et soit $\mathcal{A}$ un faisceau analytique cohérent sur E. On a $\mathrm{H}^{q}(\mathrm{E}^{h},\mathcal{A}(n))=0$ pour $q>0$ et $n$ assez grand.

(C'est le « théorème B » de [3], exp. XVIII).

En vertu de l'hypothèse de récurrence, il existe un faisceau algébrique cohérent $\mathcal{F}$ sur E tel que $\mathcal{A} = \mathcal{F}^{h}$, d'où $\mathcal{A}(n) = \mathcal{F}(n)^{h}$; d'après le théorème 1, $\mathrm{H}^{q}(\mathrm{E}^{h},\mathcal{A}(n))$ est isomorphe à $\mathrm{H}^{q}(\mathrm{E},\mathcal{F}(n))$, et le lemme 7 résulte alors de la prop. 7 de [8], n° 65.

LEMME 8. — Soit $\mathfrak{M}$ un faisceau analytique cohérent sur $X = P_r(\mathbb{C})$. Il existe un entier $n(\mathfrak{M})$ tel que, pour tout $n \geqslant n(\mathfrak{M})$, et pour tout $x \in X$, le $\mathcal{H}_x$-module $\mathfrak{M}(n)_x$ soit engendré par les éléments de $H^0(X^h, \mathfrak{M}(n))$.

(C'est le « théorème A » de [3], exp. XVIII).

Remarquons d'abord que, si  $\mathrm{H}^{0}(\mathrm{X}^{h},\mathfrak{M}(n))$  engendre  $\mathfrak{M}(n)_{x}$ , la même propriété vaut pour tout  $m\geqslant n$ . En effet, soit k un indice tel que  $x\in U_{k}$ ; pour tout i, soit  $\theta_{i}$  l'homothétie de rapport  $(t_{k}/t_{i})^{m-n}$  dans  $M_{i}$ ; les  $\theta_{i}$  commutent aux identifications qui définissent respectivement  $\mathfrak{M}(n)$  et  $\mathfrak{M}(m)$ , donc donnent naissance à un homomorphisme  $\theta:\mathfrak{M}(n)\to\mathfrak{M}(m)$ ; comme  $\theta$  est un isomorphisme au-dessus de  $U_{k}$ , notre assertion en résulte.

Remarquons également que, si  $\mathrm{H}^{0}(\mathrm{X}^{h},\mathfrak{M}(n))$  engendre  $\mathfrak{M}(n)_{x}$ , il engendre aussi  $\mathfrak{M}(n)_{y}$  pour y assez voisin de x, d'après [18], n° 12.

Ces deux remarques, jointes à la compacité de  $X^{h}$ , nous ramènent à démontrer l'énoncé suivant :

Pour tout $x\in X$, il existe un entier $n$, dépendant de $x$ et de $\mathfrak{M}$, tel que $\mathrm{H}^{0}(X^{h},\mathfrak{M}(n))$ engendre $\mathfrak{M}(n)_{x}$.

Choisissons un hyperplan E passant par $x$, d'équation homogène $t=0$. Si $\mathfrak{b}(E)$ désigne le faisceau d'idéaux défini par E (cf. n° 3), on a une suite exacte:

$$
0 \rightarrow \mathcal {A} (\mathrm{E}) \rightarrow \mathcal {H} \rightarrow \mathcal {H} _ {\mathrm{E}} \rightarrow 0.
$$

De plus, le faisceau $\mathcal{A}(\mathrm{E})$ est isomorphe à $\mathcal{H}(-1)$, l'isomorphisme $\mathcal{H}(-1) \to \mathcal{A}(\mathrm{E})$ étant défini par la multiplication par $t$ (cf. démonstration du lemme 5).

Par produit tensoriel avec $\mathfrak{M}$, on obtient une suite exacte :

$$
\mathcal {A} \otimes \mathcal {A} (\mathrm{E}) \rightarrow \mathcal {A} \rightarrow \mathcal {A} \otimes \mathcal {H} _ {\mathrm{E}} \rightarrow 0.
$$

Nous noterons $\mathcal{B}$ le faisceau $\mathcal{A}\otimes\mathcal{H}_{\mathrm{E}}$, et nous désignerons par $\mathcal{C}$ le noyau de l'homomorphisme $\mathcal{A}\otimes\mathcal{A}(\mathrm{E})\to\mathcal{A}$ (on a $\mathcal{C}=\operatorname{Tor}_{1}(\mathcal{A},\mathcal{H}_{\mathrm{E}})$); du fait que $\mathcal{A}(\mathrm{E})$ est isomorphe à $\mathcal{H}(-1)$, le faisceau $\mathcal{A}\otimes\mathcal{A}(\mathrm{E})$ est isomorphe à $\mathcal{A}(-1)$, et l'on obtient donc une suite exacte:

$$
0 \rightarrow \mathcal {C} \rightarrow \mathfrak {M} (- 1) \rightarrow \mathfrak {M} \rightarrow \mathcal {B} \rightarrow 0.\tag{1}
$$

En appliquant le foncteur $\mathfrak{M}(n)$ à la suite exacte (1), on obtient une nouvelle suite exacte:

$$
0 \rightarrow \mathcal {C} (n) \rightarrow \mathbb {1} _ {0} (n - 1) \rightarrow \mathbb {1} _ {0} (n) \rightarrow \mathcal {B} (n) \rightarrow 0.\tag{2}
$$

Soit $\mathfrak{L}_n$ le noyau de l'homomorphisme $\mathfrak{M}(n) \to \mathfrak{B}(n)$; la suite (2) se décompose en les deux suites exactes:

(3)

$$
0 \rightarrow \mathcal {C} (n) \rightarrow \mathbb {1 b} (n - 1) \rightarrow \mathfrak {L} _ {n} \rightarrow 0,\tag{4}
$$

$$
0 \rightarrow \mathfrak {L} _ {n} \rightarrow \mathfrak {M} (n) \rightarrow \mathfrak {B} (n) \rightarrow 0,
$$

qui, à leur tour, donnent naissance aux suites exactes de cohomologie :

$$
\begin{array}{l}\text {(5)} \quad \mathrm{H} ^ {1} (\mathrm{X} ^ {h}, \mathfrak {N} (n - 1)) \rightarrow \mathrm{H} ^ {1} (\mathrm{X} ^ {h}, \mathscr {X} _ {n}) \rightarrow \mathrm{H} ^ {2} (\mathrm{X} ^ {h}, \mathscr {C} (n))\\\text {et}\end{array}
$$

$$
\mathrm{H} ^ {1} \left(\mathrm{X} ^ {h}, \mathfrak {L} _ {n}\right)\rightarrow \mathrm{H} ^ {1} \left(\mathrm{X} ^ {h}, \mathfrak {M} (n)\right)\rightarrow \mathrm{H} ^ {1} \left(\mathrm{X} ^ {h}, \mathfrak {B} (n)\right). \tag {6}
$$

D'après la définition de $\mathcal{B}$ et de $\mathcal{C}$, on a $\mathcal{A}(\mathrm{E})$. $\mathcal{B}=0$ et $\mathcal{A}(\mathrm{E})$. $\mathcal{C}=0$, ce qui signifie que $\mathcal{B}$ et $\mathcal{C}$ sont des faisceaux analytiques cohérents sur l'hyperplan E. Appliquant alors le lemme 7, on voit qu'il existe un entier $n_{0}$ tel que l'on ait, pour tout $n\geqslant n_{0}$, $\mathrm{H}^{1}(\mathrm{X}^{h},\mathcal{B}(n))=0$ et $\mathrm{H}^{2}(\mathrm{X}^{h},\mathcal{C}(n))=0$. Les suites exactes (5) et (6) donnent alors les inégalités:

$$
\begin{array}{r l} \dim . \mathrm{H} ^ {1} (\mathrm{X} ^ {h}, \mathfrak {M} (n - 1)) & \geqslant \dim . \mathrm{H} ^ {1} (\mathrm{X} ^ {h}, \mathscr {P} _ {n}) \\ & \geqslant \dim . \mathrm{H} ^ {1} (\mathrm{X} ^ {h}, \mathfrak {M} (n)). \end{array} \tag {7}
$$

Ces dimensions sont finies, d'après [5] (voir aussi [3], exp. XVII). Il en résulte que dim. H$^{1}$(X$^{h}$, ℓ(n)) est une fonction décroissante de n, pour n ≥ n₀; il existe donc un entier n₁ ≥ n₀ tel que la fonction dim. H$^{1}$(X$^{h}$, ℓ(n)) soit constante pour n ≥ n₁. On a alors :

$$
\begin{array}{r l} \dim . \mathrm{H} ^ {\prime} (\mathrm{X} ^ {h}, \mathfrak {M} (n)) & = \dim . \mathrm{H} ^ {\prime} (\mathrm{X} ^ {h}, \mathfrak {L} _ {n}) \\ & = \dim . \mathrm{H} ^ {\prime} (\mathrm{X} ^ {h}, \mathfrak {M} (n)) \quad \text { si } \quad n > n _ {1}. \end{array} \tag {8}
$$

Puisque $n_{1} \geqslant n_{0}$, on a $\mathrm{H}^{1}(X^{h}, \mathcal{B}(n)) = 0$, et la suite exacte (6) montre que $\mathrm{H}^{1}(X^{h}, \mathcal{P}_{n}) \to \mathrm{H}^{1}(X^{h}, \mathcal{M}(n))$ est surjectif; mais, d'après (8), ces deux espaces vectoriels ont même dimension; l'homomorphisme en question est donc injectif, et la suite exacte de cohomologie associée à la suite exacte (4) montre que $\langle^{5}\rangle$:

(9) $\mathrm{H}^0 (\mathbf{X}^h,\mathcal{M}(n))\to \mathrm{H}^0 (\mathbf{X}^h,\mathcal{B}(n))$ est surjectif pour $n > n_{1}$.

Nous choisirons maintenant un entier $n > n_{1}$ tel que $\mathrm{H}^{0}(\mathrm{X}^{h},\mathcal{B}(n))$ engendre $\mathcal{B}(n)_{x}$; c'est possible, car, $\mathcal{B}$ étant un faisceau analytique cohérent sur E, est de la forme $\mathcal{G}^{h}$, d'où $\mathrm{H}^{0}(\mathrm{X}^{h},\mathcal{B}(n)) = \mathrm{H}^{0}(\mathrm{X},\mathcal{G}(n))$, d'après le théorème 1, et l'on sait que $\mathrm{H}^{0}(\mathrm{X},\mathcal{G}(n))$ engendre $\mathcal{G}(n)_{x}$ pour $n$ assez grand, cf. [18], n° 55, th. 1.

Ceci étant, je dis qu'un tel entier n répond à la question.

(5) On reconnaît le procédé utilisé par KODAIRA-SPENCER pour démontrer le théorème de LEFSCHETZ (cf. [12]).

En effet, posons, pour simplifier l'écriture, $\mathbf{A} = \mathcal{H}_x$, $\mathbf{M} = \mathcal{M}(n)_x$, $\mathfrak{p} = \mathcal{A}_x(\mathbf{E})$, et soit N le sous-A-module de M engendré par $\mathrm{H}^0 (\mathrm{X}^h,\mathcal{M}(n))$. On a $\mathcal{B}(n)_x = \mathcal{M}(n)_x\otimes \mathcal{H}_{x,\mathbf{E}} = \mathbf{M}\otimes_{\mathbf{A}}\mathbf{A} / \mathfrak{p} = \mathbf{M} / \mathfrak{p}\mathbf{M}$; d'autre part, il résulte de ce qui précède que l'image canonique de N dans M/pM engendre M/pM. Ceci s'écrit $\mathbf{M} = \mathbf{N} + \mathfrak{p}\mathbf{M}$, d'où, a fortiori, $\mathbf{M} = \mathbf{N} + \mathfrak{m}\mathbf{M}$ (m désignant l'idéal maximal de l'anneau local A), ce qui entraîne bien $\mathbf{M} = \mathbf{N}$ (Annexe, prop. 24, cor.), et achève la démonstration du lemme 8.

## 17. Fin de la démonstration du théorème 3.

Soit toujours $\mathcal{M}$ un faisceau analytique cohérent sur $X = P_r(C)$. En vertu du lemme 8, il existe un entier $n$ tel que $\mathcal{M}(n)$ soit isomorphe à un faisceau quotient d'un faisceau $\mathcal{H}^p$, et $\mathcal{M}$ est donc isomorphe à un quotient de $\mathcal{H}(-n)^p$. Si nous désignons par $\mathfrak{L}_0$ le faisceau algébrique cohérent $\mathcal{O}(-n)^p$, on voit donc que l'on a une suite exacte :

$$
0 \rightarrow \mathcal {R} \rightarrow \mathfrak {L} _ {0} ^ {h} \rightarrow \mathfrak {A b} \rightarrow 0,
$$

où R est un faisceau analytique cohérent.

Appliquant le même raisonnement au faisceau R, on construit un faisceau algébrique cohérent  $L_{i}$  et un homomorphisme analytique surjectif  $L_{i}^{h} \rightarrow R$ . D'où une suite exacte :

$$
\mathfrak {L} _ {1} ^ {h} \xrightarrow {g} \mathfrak {L} _ {0} ^ {h} \to \mathfrak {M} \to 0.
$$

D'après le théorème 2, il existe un homomorphisme $f: \mathfrak{L}_1 \to \mathfrak{L}_0$ tel que $g = f^h$. Si l'on désigne par $\mathcal{F}$ le conoyau de $f$, on a une suite exacte:

$$
\mathfrak {L} _ {1} \xrightarrow {f} \mathfrak {L} _ {0} \to \mathcal {F} \to 0,
$$

d'où (prop. 10), une nouvelle suite exacte :

$$
\mathfrak {L} _ {1} ^ {h} \xrightarrow {g} \mathfrak {L} _ {0} ^ {h} \to \mathcal {F} ^ {h} \to 0,
$$

qui montre bien que $\mathcal{A}$b est isomorphe à $\mathcal{F}^{h}$, ce qui achève la démonstration du théorème 3.

## § 4. Applications.

## 18. Caractère algébrique des nombres de Betti.

Soit $\sigma$ un automorphisme du corps $\mathbb{C}$; si $x$ est un point de $\mathbf{P}_{r}(\mathbb{C})$, de coordonnées homogènes $t_{0}, \ldots, t_{r}$, nous noterons $x^{\sigma}$

le point de coordonnées homogènes $t_{0}^{\sigma},\ldots,t_{r}^{\sigma}$; ainsi, $\sigma$ définit une permutation de $\mathbf{P}_{r}(\mathbf{C})$.

Si X est une sous-variété algébrique Z-fermée de  $\mathbf{P}_{r}(\mathbb{C})$ , sa transformée  $X^{\circ}$  par  $\sigma$  est encore une sous-variété algébrique Z-fermée de  $\mathbf{P}_{r}(\mathbb{C})$ ; si X est non-singulière, il en est de même de  $X^{\circ}$  (à cause du critère jacobien, par exemple).

PROPOSITION 12. — Si X est non singulière, les nombres de Betti de X et de X$^{\sigma}$ sont les mêmes.

Soit $b_n(X)$ le $n^{\text{ième}}$ nombre de Betti de X, et soit $\Omega^p(X)^h$ le faisceau des germes de formes différentielles holomorphes de degré $p$ sur X. Posons :

$$
h ^ {p, q} (\mathrm{X}) = \dim . \mathrm{H} ^ {q} \left(\mathrm{X} ^ {h}, \Omega^ {p} (\mathrm{X}) ^ {h}\right).
$$

D'après le théorème de DolBEAULT (cf. [8]), on a :

$$
b _ {n} (\mathrm{X}) = \sum_ {p + q = n} h ^ {p, q} (\mathrm{X}),
$$

et de même :

$$
b _ {n} \left(\mathrm{X} ^ {\sigma}\right) = \sum_ {p + q = n} h ^ {p, q} \left(\mathrm{X} ^ {\sigma}\right).
$$

Mais, d'après le théorème 1, on a $h^{p,q}(X) = \dim. H^q(X, \Omega^p(X))$, en désignant cette fois par $\Omega^p(X)$ le faisceau algébrique cohérent des germes de formes différentielles régulières de degré $p$ sur $X$, et de même $h^{p,q}(X^\sigma) = \dim. H^q(X^\sigma, \Omega^p(X^\sigma))$. De plus, si $\omega$ est une forme différentielle régulière sur un sous-ensemble Z-ouvert U de $X$, la forme $\omega^\sigma$ est régulière sur le sous-ensemble Z-ouvert $U^\sigma$ de $X^\sigma$; on en conclut que pour tout recouvrement Z-ouvert $\mathfrak{U}$ de $X$, $\sigma$ définit un isomorphisme semi-linéaire de $C(\mathfrak{U}, \Omega^p(X))$ sur $C(\mathfrak{U}^\sigma, \Omega^p(X^\sigma))$, donc de $H^q(\mathfrak{U}, \Omega^p(X^\sigma))$ sur $H^q(\mathfrak{U}^\sigma, \Omega^p(X^\sigma))$, donc aussi de $H^q(X, \Omega^p(X))$ sur $H^q(X^\sigma, \Omega^p(X^\sigma))$, et l'on a bien $h^{p,q}(X) = h^{p,q}(X^\sigma)$, ce qui démontre la proposition.

La proposition 12 entraîne le résultat suivant, conjecturé par A. WEIL :

COROLLAIRE. — Soit V une variété projective, non singulière, définie sur un corps de nombres algébriques K. Les variétés complexes X obtenues à partir de V en plongeant K dans C ont des nombres de Betti indépendants du plongement choisi.

En effet, on sait que deux plongements de K dans C ne diffèrent que par un automorphisme de C.

Remarque. — J'ignore si les variétés X et X$^{\sigma}$ sont toujours homéomorphes; en tout cas, l'exemple d'une courbe de genre 1 montre déjà qu'elles ne sont pas toujours analytiquement isomorphes.

## 19. Le théorème de Chow.

C'est le résultat suivant (cf. [6]):

PROPOSITION 13. — Tout sous-ense.nble analytique fermé de l'espace projectif est algébrique.

Montrons comment cette proposition résulte du théorème 3. Soit X un espace projectif et soit Y un sous-ensemble analytique fermé de $\mathbf{X}^h$. D'après un théorème de H. CARTAN cité plus haut (n° 3, prop. 1), le faisceau $\mathcal{H}_{\mathrm{Y}} = \mathcal{H}_{\mathrm{X}} / \mathcal{A}(\mathrm{Y})$ est un faisceau analytique cohérent sur $\mathbf{X}^h$; il existe donc (th. 3) un faisceau algébrique cohérent $\mathcal{F}$ sur X tel que $\mathcal{H}_{\mathrm{Y}} = \mathcal{F}^h$. D'après la prop. 10, b), le support de $\mathcal{F}^h$ est égal à celui de $\mathcal{F}$ (rappelons, cf. [18], n° 81, que le support de $\mathcal{F}$ est l'ensemble des $x \in \mathbf{X}$ tels que $\mathcal{F}_x \neq 0$), donc est Z-fermé, puisque $\mathcal{F}$ est cohérent. Comme $\mathcal{F}^h = \mathcal{H}_{\mathrm{Y}}$, ceci signifie que Y est Z-fermé, c.q.f.d.

Indiquons maintenant quelques applications simples du théorème de Chow :

PROPOSITION 14. — Si X est une variété algébrique, tout sous-ensemble analytique compact X' de X est algébrique.

Reprenons les notations de la démonstration de la proposition 6: soient Y une variété projective, U une partie de Y, Z-ouverte et Z-dense dans Y, et $f\colon U\to X$ une application régulière surjective dont le graphe T soit Z-fermé dans X × Y. Soit $\mathrm{T}^{\prime} = \mathrm{T}\cap (\mathrm{X}^{\prime}\times \mathrm{Y})$; puisque $\mathrm{X}^{\prime}$ et Y sont compacts, et que T est fermé, $\mathrm{T}^{\prime}$ est compact; il en est donc de même de la projection $\mathrm{Y}^{\prime}$ de $\mathrm{T}^{\prime}$ sur le facteur Y. D'autre part, $\mathrm{Y}^{\prime} = f^{-1}(\mathrm{X}^{\prime})$, ce qui montre que $\mathrm{Y}^{\prime}$ est un sous-ensemble analytique de U, donc de Y; le théorème de Chow montre alors que $\mathrm{Y}^{\prime}$ est un sous-ensemble Z-fermé de Y. En appliquant la proposition 7 à $f\colon \mathrm{Y}^{\prime}\to \mathrm{X}$, on en conclut que $\mathrm{X}^{\prime} = f(\mathrm{Y}^{\prime})$ est Z-fermé dans X, c.q.f.d.

PROPOSITION 15. — Toute application holomorphe f d'une variété algébrique compacte X dans une variété algébrique Y est régulière.

Soit T le graphe de f dans X × Y. Puisque f est holomorphe, T est un sous-ensemble analytique compact de X × Y; la proposition 14 montre alors que T est algébrique, d'où le fait que f est régulière, d'après la proposition 8.

COROLLAIRE. — Tout espace analytique compact possède au plus une structure de variété algébrique.

20. Espaces fibrés algébriques et espaces fibrés analytiques.

Soient G un groupe algébrique et X une variété algébrique. Les germes d'applications régulières de X dans G forment un faisceau de groupes, en général non abéliens, que nous désignerons par $\mathcal{G}$.

On sait que, si $\mathcal{A}$ est un faisceau de groupes, on peut définir le groupe $H^{6}(X, \mathcal{A})$ et l'ensemble $H^{1}(X, \mathcal{A})$: cf. [9] ainsi que [10], chap. v, par exemple. En particulier, $H^{1}(X, \mathcal{G})$ est défini; les éléments de cet ensemble ne sont autres que les classes d'espaces fibrés algébriques principaux, de base X, et de groupe structural G (au sens défini par A. WEIL, cf. [20]). Par exemple, les éléments de $H^{1}(X, \mathcal{O}_{X})$ sont les classes d'espaces fibrés de groupe le groupe additif C.

De même, si $\mathcal{G}^{h}$ désigne le faisceau des germes d'applications holomorphes de X dans G, les éléments de H$^{1}$(X$^{h}$, $\mathcal{G}^{h}$) ne sont autres que les classes d'espaces fibrés analytiques de base X et de groupe G. Tout espace fibré algébrique E définit un espace fibré analytique E$^{h}$, d'où une application

$$
\varepsilon : \mathrm{H} ^ {1} (\mathrm{X}, \mathcal {G}) \rightarrow \mathrm{H} ^ {1} (\mathrm{X} ^ {h}, \mathcal {G} ^ {h}),
$$

analogue à celle du n° 11.

PROPOSITION 16. — Si X est compacte, l'application $\varepsilon$ est injective.

Soient E et E' deux espaces fibrés algébriques principaux, de base X, et de groupe structural G. La proposition 16 signifie que, si E et E' sont analytiquement isomorphes, ils le sont aussi algébriquement. En fait, nous allons démontrer un résultat un peu plus précis, à savoir que tout isomorphisme analytique $\varphi: E \to E'$ est un isomorphisme algébrique (c'est-à-dire régulier).

L'espace E × E' est un espace fibré algébrique principal,

de base X × X, et de groupe structural G × G; nous désigne-rons par (E, E') son image réciproque par l'application diagonale X → X × X: c'est le « produit fibré » de E et de E'. Faisons opérer G × G sur G par la formule :

$$
(g, g ^ {\prime}). h = g h g ^ {- 1}.
$$

Soit T l'espace fibré associé à l'espace fibré principal (E, E') et admettant pour fibre type le groupe G, muni des opérations précédentes. On voit tout de suite que les sections de T correspondent biunivoquement aux isomorphismes de E sur E'; en particulier, l'isomorphisme $\varphi$ correspond à une section analytique s de T. En appliquant à $s: X \to T$ la proposition 15, on voit que s est régulière, ce qui signifie que $\varphi$ est régulier, et démontre la proposition.

Supposons maintenant que X soit une variété projective. On peut se demander si $\varepsilon: H'(X, \mathcal{G}) \to H'(X^h, \mathcal{G}^h)$ est bijective, autrement dit (compte tenu de la prop. 16), si tout espace fibré analytique est algébrique. C'est évidemment inexact si l'on n'impose aucune condition à G, comme le montre le cas où G est une variété abélienne (ou un groupe fini); dans les propositions suivantes, nous allons indiquer un certain nombre de groupes G pour lesquels c'est exact.

PROPOSITION 17. — Si G est le groupe additif C, l'application est bijective.

En effet, on a alors $\mathcal{G} = \mathcal{O}$ et $\mathcal{G}^h = \mathcal{O}^h$, et la proposition est un cas particulier du théorème 1.

PROPOSITION 18. — Si G est le groupe linéaire général GL$_{n}$(C), l'application $\varepsilon$ est bijective.

A tout espace fibré principal de groupe structural  $\mathrm{GL}_{n}(\mathbb{C})$  est associé un espace fibré à fibre vectorielle, de fibre type  $C^{n}$ , qui le caractérise. Compte tenu de la correspondance entre espaces fibrés à fibres vectorielles et faisceaux localement libres (cf. [18], n° 41, par exemple), on est donc ramené à démontrer l'énoncé suivant :

Si $\mathfrak{M}$ est un faisceau analytique cohérent sur $X^{h}$, qui est localement isomorphe à $\mathcal{H}^{n}$, il existe un faisceau algébrique cohérent $\mathcal{F}$ sur X, qui est localement isomorphe à $\mathcal{O}^{n}$, et tel que $\mathcal{F}^{h}$ soit isomorphe à $\mathfrak{A}$.

D'après le théorème 3 il existe un faisceau algébrique cohérent $\mathcal{F}$ sur X vérifiant la seconde condition. Pour tout $x\in X$, le $\mathcal{H}_x$-module $\mathcal{F}_x^h = \mathcal{F}_x\otimes \mathcal{H}_x$ est donc isomorphe à $\mathcal{H}_x^n$; en appliquant la proposition 30 de l'Annexe aux anneaux $A = \mathcal{O}_x$, $A' = \mathcal{H}_x$ et au module $E = \mathcal{F}_x$, on en conclut que $\mathcal{F}_x$ est isomorphe à $\mathcal{O}_x^n$; puisque $\mathcal{F}$ est cohérent, ceci entraîne que $\mathcal{F}$ est localement isomorphe à $\mathcal{O}^n$, et achève la démonstration.

Remarques 1. — Pour $n=1$, $\mathrm{GL}_{n}(\mathbb{C})$ coïncide avec le groupe multiplicatif $\mathbb{C}^{*}$; si l'on suppose que X est une variété normale, le groupe $\mathrm{H}^{\prime}(\mathrm{X},\mathcal{G})$ coïncide avec le groupe des classes de diviseurs localement linéairement équivalents à zéro (cf. [20], § 3) et la proposition 18 signifie que tout espace fibré analytique de base X et de groupe structural $\mathbb{C}^{*}$ provient d'un tel diviseur. Lorsque X est non singulière, ce résultat avait été obtenu par KODAIRA-SPENCER [12]; dans ce cas, il est d'ailleurs essentiellement équivalent au théorème de LEFSCHETZ sur l'existence de diviseurs de classe d'homologie donnée.

2. La proposition 18 permet d'étendre d'autres résultats de KODAIRA aux variétés projectives arbitraires (pouvant avoir des singularités); il en est notamment ainsi des théorèmes 7 et 8 de [11]. Nous n'insisterons pas là-dessus.

Soient maintenant G un groupe algébrique, et H un sous-groupe algébrique de G; on sait (cf. [13], par exemple) que l'espace homogène G/H peut être muni d'une structure de variété algébrique, quotient de celle de G. Le groupe H opère sur G par translations à droite; nous supposerons que ces opérations définissent sur G une structure d'espace fibré algébrique principal, de base G/H, et de groupe structural H, ou, ce qui revient au même, nous supposerons qu'il existe une section rationnelle G/H → G (ce qui n'est pas toujours le cas, comme nous le verrons plus loin). Sous cette hypothèse, on a le résultat suivant, qui m'a été communiqué, ainsi que sa démonstration, par A. GROTHENDIECK :

PROPOSITION 19. — Soit X une variété algébrique compacte, et soit P un espace fibré principal analytique, de groupe structural H, et de base X. Pour que P soit algébrique, il faut et il suffit qu'il en soit ainsi de l'espace fibré P ×$_{H}$ G déduit de P en étendant le groupe structural de H à G.

La nécessité est évidente. Pour démontrer la suffisance, supposons que  $P \times_{H} G$  soit algébrique. Cela signifie qu'il existe un espace fibré algébrique principal  $P_{0}$  de groupe structural G, et un isomorphisme analytique  $h: P_{0} \rightarrow P \times_{H} G$ . Considérons l'espace fibré E (resp.  $E_{0}$ ) associé à  $P \times_{H} G$ . (resp. à  $P_{0}$ ) et de fibre type G/H sur lequel G opère par translations. On a :

$$
\mathrm{E} _ {0} = \mathrm{P} _ {0} \times_ {\mathrm{G}} \mathrm{G} / \mathrm{H} \quad \text {et} \quad \mathrm{E} = (\mathrm{P} \times_ {\mathrm{H}} \mathrm{G}) \times_ {\mathrm{G}} \mathrm{G} / \mathrm{H} = \mathrm{P} \times_ {\mathrm{H}} \mathrm{G} / \mathrm{H}.
$$

L'isomorphisme analytique $h$ définit un isomorphisme analytique $f: \mathrm{E}_{0} \to \mathrm{E}$. Mais l'espace fibré $\mathrm{E} = \mathrm{P} \times_{\mathrm{H}} \mathrm{G}/\mathrm{H}$ possède une section canonique $s$, puisque le groupe H laisse invariant le point de $\mathrm{G}/\mathrm{H}$ correspondant à l'élément neutre de G. L'isomorphisme $f$ transforme $s$ en une section $s_{0} = f^{-1} \circ s$ de $\mathrm{E}_{0}$; la section $s_{0}$ est holomorphe, donc régulière, d'après la proposition 15.

D'autre part, puisque G opère sur  $P_{0}$ , il en est de même de H, et  $P_{0}/H$  n'est autre que  $E_{0}$ ; plus précisément,  $P_{0}$  est un espace fibré algébrique principal, de groupe structural H, et de base  $E_{0}$ : cela se vérifie facilement, par un raisonnement local, en utilisant l'hypothèse que G est un espace fibré algébrique principal de groupe structural H et de base G/H. Soit alors  $\mathrm{P}_{1}=s_{0}^{-1}(\mathrm{P}_{0})$  l'image réciproque de  $P_{0}$  par l'application  $s_{0}:X\to E_{0}$ ; l'espace fibré  $P_{1}$  est un espace fibré algébrique principal, de base X, et de groupe structural H. Nous allons montrer que  $P_{1}$  est analytiquement isomorphe à P, ce qui démontrera la proposition.

La relation $s_0 = f^{-1} \circ s$, jointe au fait que $f$ est un isomorphisme analytique, montre que $P_1 = s_0^{-1}(P_0)$ est analytiquement isomorphe à l'image réciproque de $P \times_H G$ (considéré comme espace fibré principal de groupe structural H) par l'application $s: X \to E$. Mais cette dernière image réciproque n'est autre que P, comme le montre le diagramme commutatif :

$$
\begin{array}{l}\mathrm{P} \longrightarrow \mathrm{P} \times_ {\mathrm{H}} \mathrm{G}\\\downarrow \qquad \qquad \qquad \downarrow\\\mathrm{X} \stackrel {{s}} {{\rightarrow}} \mathrm{E} = \mathrm{P} \times_ {\mathrm{H}} \mathrm{G} / \mathrm{H}.\end{array}
$$

Ceci achève la démonstration.

En combinant les propositions 18 et 19, on obtient :

PROPOSITION 20. — Soit G un sous-groupe algébrique du groupe $\mathrm{GL}_{n}(\mathbb{C})$ vérifiant la condition suivante:

(R) — Il existe une section rationnelle  $\mathrm{GL}_{n}(\mathbb{C})/\mathrm{G}\rightarrow\mathrm{GL}_{n}(\mathbb{C})$ .

Alors, pour toute variété projective X, l'application :

$$
\varepsilon : \mathrm{H} ^ {1} (\mathrm{X}, \mathcal {G}) \rightarrow \mathrm{H} ^ {1} (\mathrm{X} ^ {h}, \mathcal {G} ^ {h})
$$

est bijective.

Exemples. — La condition (R) est vérifiée dans les cas suivants :

a) lorsque G est résoluble, en vertu d'un théorème de Rosenlicht, [13];

b) lorsque  $\mathrm{G} = \mathrm{SL}_{n}(\mathbb{C})$ , la section rationnelle étant alors évidente;

c) lorsque  $\mathrm{G} = \mathrm{Sp}_{n}(\mathbb{C})$ , n = 2m; dans ce cas, l'espace homogène  $\mathrm{GL}_{n}(\mathbb{C}) / \mathrm{G}$  est l'espace des formes alternées non dégénérées  $\sum_{i < j} a_{ij} x_{i} \wedge x_{j}$ , et la condition (R) résulte du fait que la forme générique  $\sum_{i < j} u_{ij} x_{i} \wedge x_{j}$  peut être ramenée à la forme canonique  $\sum_{i=1}^{m} x_{2i-1} \wedge x_{2i}$  par un changement linéaire de variables à coefficients dans le corps  $\mathbb{C}(u_{ij})$ .

Ces deux derniers exemples conduisent à conjecturer que la condition (R) est vérifiée chaque fois que G est un groupe semi-simple simplement connexe.

Par contre, on peut montrer que le groupe orthogonal unimodulaire  $G = O_{n}^{+}(\mathbb{C})$  ne vérifie pas la condition (R) lorsque  $n \geqslant 3$ . J'ignore si, dans ce cas, l'application  $\varepsilon : H^{1}(X, \mathcal{G}) \to H^{1}(X^{h}, \mathcal{G}^{h})$  est bijective.

## ANNEXE

Tous les anneaux considérés ci-dessous sont supposés commutatifs et à élément unité; tous les modules sur ces anneaux sont supposés unitaires.

## 21. Modules plats.

DÉFINITION 3. — Soit B un A-module. On dit que B est A-plat (ou plat) si, pour toute suite exacte de A-modules:

$$
\mathrm{E} \rightarrow \mathrm{F} \rightarrow \mathrm{G},
$$

la suite

$$
\mathrm{E} \otimes_ {\mathrm{A}} \mathrm{B} \rightarrow \mathrm{F} \otimes_ {\mathrm{A}} \mathrm{B} \rightarrow \mathrm{G} \otimes_ {\mathrm{A}} \mathrm{B}
$$

est exacte.

Vu la définition des foncteurs Tor, la condition précédente équivaut à dire que $\mathrm{Tor}_{\mathfrak{i}}^{\mathsf{A}}(\mathbf{B},\mathbf{Q}) = 0$ pour tout A-module Q; comme Tor commute avec les limites inductives, on peut se borner aux modules Q de type fini, et même (grâce à la suite exacte des Tor) aux modules Q monogènes; ainsi, pour que B soit A-plat, il faut et il suffit que $\mathrm{Tor}_{\mathfrak{i}}^{\mathsf{A}}(\mathbf{B},\mathbf{A} / \mathfrak{a}) = 0$ pour tout idéal $\mathfrak{a}$ de A, autrement dit que l'homomorphisme canonique $\mathfrak{a}\otimes_{\mathbf{A}}\mathbf{B}\to \mathbf{B}$ soit injectif.

Exemples. — 1. Si A est un anneau principal, il résulte de ce qui précède que « B est A-plat » équivaut à « B est sans torsion ».

2. Si S est une partie multiplicativement stable d'un anneau A, l'anneau de fractions  $A_{s}$  est A-plat, d'après [18], n° 48, lemme 1.

Soient A et B deux anneaux, et soit  $\theta: A \rightarrow B$  un homomorphisme de A dans B; cet homomorphisme munit B d'une structure de A-module. Si E et F sont deux A-modules,  $E \otimes_{A} B$  et  $F \otimes_{A} B$  sont munis de structures de B-modules; de plus, si  $f: E \rightarrow F$  est un homomorphisme,  $f \otimes 1$  est un B-homomorphisme de  $E \otimes_{A} B$  dans  $F \otimes_{A} B$ ; on obtient ainsi une application A-linéaire canonique:

$$
\operatorname{Hom} _ {\mathbf {A}} (\mathrm{E}, \mathrm{F}) \rightarrow \operatorname{Hom} _ {\mathbf {B}} (\mathrm{E} \otimes_ {\mathbf {A}} \mathrm{B}, \mathrm{F} \otimes_ {\mathbf {A}} \mathrm{B}),
$$

qui se prolonge par linéarité en une application B-linéaire :

$$
\iota : \quad \operatorname{Hom} _ {\mathbf {A}} (\mathrm{E}, \mathrm{F}) \otimes_ {\mathbf {A}} \mathrm{B} \rightarrow \operatorname{Hom} _ {\mathbf {B}} (\mathrm{E} \otimes_ {\mathbf {A}} \mathrm{B}, \mathrm{F} \otimes_ {\mathbf {A}} \mathrm{B}).
$$

PROPOSITION 21. — L'homomorphisme : défini ci-dessus est bijectif lorsque A est un anneau noethérien, E est un A-module de type fini, et B est A-plat.

Pour un module F fixé, posons :

$\mathrm{T(E)} = \mathrm{Hom}_{\mathrm{A}}(\mathrm{E},\mathrm{F})\otimes_{\mathrm{A}}\mathrm{B}\quad \text{et}\quad \mathrm{T}'(\mathrm{E}) = \mathrm{Hom}_{\mathrm{B}}(\mathrm{E}\otimes_{\mathrm{A}}\mathrm{B},\mathrm{F}\otimes_{\mathrm{A}}\mathrm{B}),$ de sorte que $\iota$ est un homomorphisme du foncteur $\mathrm{T(E)}$ dans le foncteur $\mathrm{T}'(\mathrm{E})$.

Pour $E = A$, on a $T(E) = T'(E) = F \otimes_A B$, et $\iota$ est bijectif; il en est de même lorsque $E$ est un module libre de type fini.

Mais l'anneau A est noethérien, et E est de type fini; il existe donc une suite exacte :

$$
\mathrm{L} _ {1} \rightarrow \mathrm{L} _ {0} \rightarrow \mathrm{E} \rightarrow 0,
$$

où  $L_{0}$  et  $L_{1}$  sont des modules libres de type fini. Considérons le

diagramme commutatif :

$$
\begin{array}{c} 0 \to \mathrm{T} (\mathrm{E}) \to \mathrm{T} (\mathrm{L} _ {0}) \to \mathrm{T} (\mathrm{L} _ {1} \\ \iota_ {1} \downarrow \quad \iota_ {0} \downarrow \quad \iota_ {1} \downarrow \\ 0 \to \mathrm{T} ^ {\prime} (\mathrm{E}) \to \mathrm{T} ^ {\prime} (\mathrm{L} _ {0}) \to \mathrm{T} ^ {\prime} (\mathrm{L} _ {1 /}. \end{array}
$$

La première ligne de ce diagramme est exacte du fait que B est A-plat; la seconde l'est aussi d'après les propriétés générales des foncteurs $\otimes$ et Hom. Comme nous savons que $\iota_0$ et $\iota_1$ sont bijectifs, il en résulte bien que $\iota$ est bijectif, c.q.f.d.

## 22. Couples plats.

DÉFINITION 4. — Soit A un anneau, et soit B un anneau contenant A. On dit que le couple (A, B) est plat si le A-module B/A est A-plat.

On a:

PROPOSITION 22. — Pour qu'un couple (A, B) soit plat, il faut et il suffit que B soit A-plat, et que l'une des propriétés suivantes soit vérifiée :

a) (resp. a') Pour tout A-module (resp. pour tout A-module de type fini) E, l'homomorphisme  $E \rightarrow E \otimes_{A} B$  est injectif.

$a^{\prime \prime})$ Pour tout idéal $\mathfrak{a}$ de A, on a $\mathfrak{aB} \cap \mathbf{A} = \mathfrak{a}$.

Si E est un A-module quelconque, la suite exacte :

$$
0 \rightarrow \mathrm{A} \rightarrow \mathrm{B} \rightarrow \mathrm{B} / \mathrm{A} \rightarrow 0,
$$

donne naissance à la suite exacte :

$$
\operatorname{Tor} _ {1} ^ {\mathrm{A}} (\mathrm{A}, \mathrm{E}) \rightarrow \operatorname{Tor} _ {1} ^ {\mathrm{A}} (\mathrm{B}, \mathrm{E}) \rightarrow \operatorname{Tor} _ {1} ^ {\mathrm{A}} (\mathrm{B} / \mathrm{A}, \mathrm{E}) \rightarrow \mathrm{A} \otimes_ {\mathrm{A}} \mathrm{E} \rightarrow \mathrm{B} \otimes_ {\mathrm{A}} \mathrm{E}.
$$

Compte tenu de ce que  $A \otimes_{A} E = E$  et  $\operatorname{Tor}_{1}^{A}(A, E) = 0$ , on obtient la nouvelle suite exacte:

$$
0 \rightarrow \operatorname{Tor} _ {1} ^ {\mathrm{A}} (\mathrm{B}, \mathrm{E}) \rightarrow \operatorname{Tor} _ {1} ^ {\mathrm{A}} (\mathrm{B} / \mathrm{A}, \mathrm{E}) \rightarrow \mathrm{E} \rightarrow \mathrm{E} \otimes_ {\mathrm{A}} \mathrm{B}.
$$

On voit donc que, pour que $\mathrm{Tor}_{1}^{\mathrm{A}}(\mathrm{B}/\mathrm{A},\mathrm{E})$ soit réduit à 0, il faut et il suffit qu'il en soit de même pour $\mathrm{Tor}_{1}^{\mathrm{A}}(\mathrm{B},\mathrm{E})$ et que l'homomorphisme $\mathrm{E}\rightarrow\mathrm{E}\otimes_{\mathrm{A}}\mathrm{B}^{*}$ soit injectif; la proposition résulte immédiatement de là (noter que la propriété $a''$) revient à dire que l'homomorphisme $\mathrm{A}/\mathfrak{a}\rightarrow\mathrm{A}/\mathfrak{a}\otimes_{\mathrm{A}}\mathrm{B}$ est injectif).

PROPOSITION 23. — Soient A ⊂ B ⊂ C trois anneaux. Si les couples (A, C) et (B, C) sont plats, il en est de même du couple (A, B).

Montrons d'abord que B est A-plat, autrement dit que, si l'on a une suite exacte de A-modules:

$$
0 \rightarrow \mathrm{E} \rightarrow \mathrm{F},
$$

la suite: $0 \to E \otimes_{A} B \to F \otimes_{A} B$ est encore exacte.

Soit N le noyau de l'homomorphisme  $E \otimes_{A} B \rightarrow F \otimes_{A} B$ ; puisque C est B-plat, on a une suite exacte:

$$
0 \rightarrow \mathrm{N} \otimes_ {\mathrm{B}} \mathrm{C} \rightarrow (\mathrm{E} \otimes_ {\mathrm{A}} \mathrm{B}) \otimes_ {\mathrm{B}} \mathrm{C} \rightarrow (\mathrm{F} \otimes_ {\mathrm{A}} \mathrm{B}) \otimes_ {\mathrm{B}} \mathrm{C}.
$$

Mais, d'après l'associativité du produit tensoriel,  $(\mathrm{E}\otimes_{\mathrm{A}}\mathrm{B})\otimes_{\mathrm{B}}\mathrm{C}$  s'identifie à  $E\otimes_{A}C$, et de même  $(\mathrm{F}\otimes_{\mathrm{A}}\mathrm{B})\otimes_{\mathrm{B}}\mathrm{C}$  s'identifie à  $F\otimes_{A}C$. De plus, C étant A-plat, l'homomorphisme  $E\otimes_{A}C\to F\otimes_{A}C$  est injectif. Il s'ensuit que  $N\otimes_{B}C=0$, et, en appliquant la proposition 22 au couple (B, C), on voit que N=0, ce qui achève de démontrer que B est A-plat.

D'autre part, si E est un A-module quelconque, l'homomorphisme composé:  $E \rightarrow E \otimes_{A} B \rightarrow E \otimes_{A} C$  est injectif (puisque le couple (A, C) est plat), et il en est a fortiori de même de  $E \rightarrow E \otimes_{A} B$ ; ceci montre que le couple (A, B) vérifie toutes les hypothèses de la proposition 22, c.q.f.d.

Remarque. — Un raisonnement analogue montre que si (A, B) et (B, C) sont plats, il en est de même de (A, C). Par contre, il peut se faire que (A, B) et (A, C) soient plats, sans que (B, C) le soit.

## 23. Modules sur un anneau local.

Dans ce numéro, nous désignerons par A un anneau local noethérien (6), d'idéal maximal M.

PROPOSITION 24. — Si un A-module de type fini E vérifie la relation E = mE, on a E = 0.

(Cf. [15], p. 138 ou [4], exp. I, par exemple.)

Supposons E ≠ 0, et soit $e_{1}, \ldots, e_{n}$ un système de générateurs

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(6) En fait, tous les résultats démontrés dans ces deux derniers numéros sont valables sans changement pour un anneau de Zariski (cf. [15], p. 157).</span></small>

de E ayant le plus petit nombre possible d'éléments. Puisque  $e_{n} \in mE$ , on a  $e_{n} = x_{1}e_{1} + \cdots + x_{n}e_{n}$ , avec  $x_{i} \in m$ , d'où

$$
(1 - x _ {n}) e _ {n} = x _ {1} e _ {1} + \dots + x _ {n - 1} e _ {n - 1};
$$

comme 1 — $x_{n}$ est inversible dans A, ceci montre que les $e_{1}, \ldots, e_{n-1}$ engendrent E, ce qui est en contradiction avec l'hypothèse faite sur n.

COROLLAIRE. — Soit E un A-module de type fini. Si un sous-module F de E vérifie la relation  $E = F + mE$ , on a E = F. En effet, cette relation signifie que  $E/F = m(E/F)$ .

Nous munirons tout A-module E de la topologie m-adique dans laquelle les sous-modules m°E forment une base de voisinages de 0 (cf. [15], p. 153).

PROPOSITION 25. — Soit E un A-module de type fini. Alors : a) La topologie induite sur un sous-module F de E par la topologie m-adique de E coïncide avec la topologie m-adique de F.

b) Tout sous-module de E est fermé pour la topologie m-adique de E (et, en particulier, E est séparé).

(Cf. [15], loc. cit., ainsi que [3], exp. VIII bis).

Rappelons brièvement la démonstration de cette proposition. On commence par démontrer $a$), ce qui peut se faire, soit en utilisant la théorie de la décomposition primaire (Krull, cf. [15]), soit en établissant l'existence d'un entier $r$ tel que l'on ait

$$
\mathrm{F} \cap \mathfrak {m} ^ {n} \mathrm{E} = \mathfrak {m} ^ {n - r} (\mathrm{F} \cap \mathfrak {m} ^ {r} \mathrm{E}) \text {   pour   } n \geqslant r (\text { Artin }, \text { Rees }, \text { cf. } [ 4 ], \exp . 2).
$$

On montre ensuite que E est séparé : en appliquant a) au sous-module F adhérence de 0 dans E, on voit que F = mF, d'où F = 0, d'après la proposition 24. En appliquant ce résultat aux modules quotients de E, on en déduit b).

Soit encore E un A-module de type fini, et soient $\hat{E}$ et $\hat{A}$ les complétés de E et de A pour la topologie m-adique. L'application bilinéaire $A \times E \to E$ se prolonge par continuité en une application $\hat{A} \times \hat{E} \to \hat{E}$ qui fait de $\hat{E}$ un $\hat{A}$-module. L'injection canonique de E dans $\hat{E}$ se prolonge donc par linéarité en un homomorphisme.

$$
\varepsilon : \quad \mathrm{E} \otimes_ {\mathrm{A}} \hat {\mathrm{A}} \rightarrow \hat {\mathrm{E}}.
$$

PROPOSITION 26. — Pour tout A-module de type fini E, l'homomorphisme ε défini ci-dessus est bijectif.

Soit $0 \to R \to L \to E \to 0$ une suite exacte de A-modules, L étant un module libre de type fini. Du fait que A est noethérien, R est de type fini; d'autre part, la proposition 25 montre que la topologie m-adique de R est induite par celle de L, et il est clair que celle de E est quotient de celle de L; comme ces topologies sont métrisables, on en déduit une suite exacte :

$$
0 \rightarrow \hat {\mathrm{R}} \rightarrow \hat {\mathrm{L}} \rightarrow \hat {\mathrm{E}} \rightarrow 0.
$$

Considérons alors le diagramme commutatif :

$$
\begin{array}{c c c c c} \mathrm{R} \otimes_ {\Lambda} \hat {\mathrm{A}} \to \mathrm{L} \otimes_ {\Lambda} \hat {\mathrm{A}} \to \mathrm{E} \otimes_ {\Lambda} \hat {\mathrm{A}} \to 0 \\ \varepsilon^ {\prime \prime} \downarrow & & \varepsilon^ {\prime} \downarrow & & \varepsilon \downarrow \\ \hat {\mathrm{R}} & \to & \hat {\mathrm{L}} & \to & \hat {\mathrm{E}} \end{array}
$$

Les deux lignes de ce diagramme sont exactes, et, d'autre part, il est clair que $\varepsilon'$ est bijectif. On en déduit que $\varepsilon$ est surjectif (autrement dit, on a $\hat{\mathbf{E}} = \hat{\mathbf{A}}.\mathbf{E}$, cf. [15], p. 153, lemme 1). Ce résultat, étant démontré pour tout A-module de type fini, s'applique en particulier à R, ce qui montre que $\varepsilon''$ est surjectif, et, en appliquant le lemme des cinq, on en conclut que $\varepsilon$ est bijectif, c.q.f.d.

## 24. Propriétés de platitude des anneaux locaux.

Tous les anneaux locaux considérés ci-dessous sont supposés noethériens.

PROPOSITION 27. — Soit A un anneau local, et soit $\hat{\mathbf{A}}$ son complété. Le couple (A, $\hat{\mathbf{A}}$) est plat.

Tout d'abord, $\hat{\mathbf{A}}$ est A-plat. En effet, il suffit de montrer que, si $\mathbf{E} \to \mathbf{F}$ est injectif, il en est de même de $\mathbf{E} \otimes_{\mathbf{A}} \hat{\mathbf{A}} \to \mathbf{F} \otimes_{\mathbf{A}} \hat{\mathbf{A}}$, et l'on peut même supposer E et F de type fini. Dans ce cas, la proposition 26 montre que $\mathbf{E} \otimes_{\mathbf{A}} \hat{\mathbf{A}}$ s'identifie à $\hat{\mathbf{E}}$, et de même $\mathbf{F} \otimes_{\mathbf{A}} \hat{\mathbf{A}}$ s'identifie à $\hat{\mathbf{F}}$, et notre assertion résulte alors du fait évident que $\hat{\mathbf{E}}$ se plonge dans $\hat{\mathbf{F}}$.

De même, le fait que E → Ê soit injectif si E est de type fini montre que le couple (A, Â) vérifie la propriété  $a'$  de la proposition 22, donc est bien un couple plat.

Soient maintenant A et B deux anneaux locaux, et soit 0 un homomorphisme de A dans B. Supposons que 0 applique l'idéal

maximal de A dans l'idéal maximal de B. Alors $\theta$ est continu, et se prolonge par continuité en un homomorphisme $\hat{\theta}:\hat{A}\to\hat{B}$.

PROPOSITION 28. — Supposons que $\hat{\theta}\colon\hat{A}\to\hat{B}$ soit bijectif, et identifions A à un sous-anneau de B au moyen de $\theta$. Le couple (A, B) est alors un couple plat.

On a  $A \subset B \subset \hat{B} = \hat{A}$ , et les couples (A,  $\hat{A}$ ) et (B,  $\hat{B}$ ) sont plats, d'après la proposition précédente. La proposition 23 montre que (A, B) est un couple plat.

PROPOSITION 29. — Soient A et B deux anneaux locaux, soit a un idéal de A, et soit 0 un homomorphisme de A dans B. Si 0 vérifie l'hypothèse de la proposition 28, il en est de même de l'homomorphisme de A/a dans B/θ(a)B défini par 0 (ce qui montre que le couple (A/a, B/θ(a)B) est un couple plat).

D'après la proposition 26, le complété de A/a est $\hat{A}/a\hat{A}$, et, de même, celui de B/$\theta(a)$B est $\hat{B}/\theta(a)\hat{B}$, d'où le résultat.

PROPOSITION 30. — Soient A et A' deux anneaux locaux, soit 0 un homomorphisme de A dans A' vérifiant l'hypothèse de la proposition 28, et soit E un A-module de type fini. Si le A'-module E' = E ⊗A'A'est isomorphe à A'n, alors E est isomorphe à A^n.

Nous identifierons A à un sous-anneau de A' au moyen de 0. Si m et m' désignent les idéaux maximaux de A et A', on a donc m < m'; d'autre part, puisque m' est un voisinage de 0 dans A', et que A est dense dans A', on a A' = m' + A, ce qui montre que A/m = A'/m', d'où E/mE = E'/m'E'. Puisque le A'-module E' est un module libre de rang n, il en est de même du A'/m'-module E'/m'E'. On en conclut qu'il est possible de choisir n éléments  $e_{1}, \ldots, e_{n}$  dans E dont les images dans E/mE forment une base de E/mE, considéré comme espace vectoriel sur A/m. Les éléments  $e_{i}$  définissent un homomorphisme f: A^n → E qui est surjectif en vertu du corollaire à la proposition 24. Nous allons montrer que f est injectif, ce qui démontrera la proposition.

Soit N le noyau de f. Du fait que le couple (A, A') est plat (prop. 28), la suite exacte :

$$
0 \rightarrow \mathrm{N} \rightarrow \mathrm{A} ^ {n} \xrightarrow {f} \mathrm{E} \rightarrow 0,
$$

donne naissance à la suite exacte :

$$
0 \rightarrow \mathrm{N} ^ {\prime} \rightarrow \mathrm{A} ^ {\prime n} \xrightarrow {f ^ {\prime}} \mathrm{E} ^ {\prime} \rightarrow 0.
$$

Comme le module E' est libre, N' est facteur direct dans A'n, et l'on a une suite exacte:

$$
0 \rightarrow \mathrm{N} ^ {\prime} / \mathfrak {m} ^ {\prime} \mathrm{N} ^ {\prime} \rightarrow \mathrm{A} ^ {\prime n} / \mathfrak {m} ^ {\prime} \mathrm{A} ^ {\prime n} \rightarrow \mathrm{E} ^ {\prime} / \mathfrak {m} ^ {\prime} \mathrm{E} ^ {\prime} \rightarrow 0.
$$

Mais, par construction même, $f'$ définit une bijection de $A'^n / m'A'^n$ sur $E'/m'E'$. Il s'ensuit que $N'/m'N' = 0$, d'où $N' = 0$ (proposition 24), d'où $N = 0$ puisque le couple $(A, A')$ est plat, c.q.f.d.

## BIBLIOGRAPHIE

[1] H. CARTAN. Idéaux et modules de fonctions analytiques de variables complexes. Bull. Soc. Math. France, 78, 1950, pp. 29-64.

[2] H. CARTAN. Séminaire E. N. S., 1951-1952.

[3] H. CARTAN. Séminaire E. N. S., 1953-1954.

[4] H. CARTAN et C. CHEVALLEY. Séminaire E. N. S., 1955-1956.

[5] H. CARTAN et J.-P. SERRE. Un théorème de finitude concernant les variétés analytiques compactes. C. R., 237, 1953, pp. 128-130.

[6] W-L. Chow. On compact complex analytic varieties. Amer. J. of Maths., 71, 1949, pp. 893-914.

[7] W-L. Chow. On the projective embedding of homogeneous varieties. Lefschetz's volume, Princeton, 1956.

[8] P. DOLBEAULT. Sur la cohomologie des variétés analytiques complexes. C. R., 236, 1953, pp. 175-177.

[9] J. FRENKEL. Cohomologie à valeurs dans un faisceau non abélien.
C. R., 240, 1955, pp. 2368-2370.

[10] A. GROTHENDIECK. A general theory of fibre spaces with structure sheaf. Kansas Univ., 1955.

[11] K. KODAIRA. On Kähler varieties of restricted type (an intrinsic characterization of algebraic varieties). Ann. of Maths., 60, 1954, pp. 28-48.

[12] K. KODAIRA and D. C. SPENCER. Divisor class groups on algebraic varieties. Proc. Nat. Acad. Sci. U. S. A., 39, 1953, pp. 872-877.

[13] M. ROSENLICHT. Some basic theorems on algebraic groups. Amer J. of Maths., 78, 1956, pp. 401-443.

[14] W. RÜCKERT. Zum Eliminationsproblem der Potenzreihendeale. Math. Ann., 107, 1933, pp. 259-281.

[15] P. SAMUEL. Commutative Algebra (Notes by D. Herzig). Cornell Univ., 1953.

[16] P. SAMUEL. Algèbre locale. Mém. Sci. Math., 123, Paris, 1953.

[17] P. SAMUEL. Méthodes d'algèbre abstraite en géométrie algébrique. Ergebn. der Math., Springer, 1955.

[18] J.-P. SERRE. Faisceaux algébriques cohérents. Ann. of Maths., 61, 1955, pp. 197-278.

[19] J.-P. SERRE. Sur la cohomologie des variétés algébriques. J. de Maths. Pures et Appl., 35, 1956.

[20] A. WEIL. Fibre-spaces in algebraic geometry (Notes by A. Wallace). Chicago Univ., 1952.