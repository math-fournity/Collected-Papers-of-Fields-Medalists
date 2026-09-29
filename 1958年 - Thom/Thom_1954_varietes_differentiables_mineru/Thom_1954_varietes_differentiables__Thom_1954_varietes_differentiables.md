# Quelques propriétés globales des variétés différentiables

Par RENÉ THOM, Strasbourg

## Introduction

Le présent article donne la démonstration des résultats que j'ai annoncés dans quatre Notes aux Comptes-Rendus [28]¹). Il est divisé en quatre chapitres. Le premier chapitre élabore une technique d'approximation des applications différentiables; les théorèmes démontrés sont en quelque sorte une formulation différentiable du théorème d'approximation simpliciale de la Topologie; grâce à eux, toute la théorie pourra être établie sans faire appel au théorème de triangulation des variétés différentiables. Le chapitre II est consacré au problème de la réalisation des classes d'homologie d'une variété par des sous-variétés; on y obtient les résultats essentiels: En homologie mod 2, toutes les classes dont la dimension est inférieure à la moitié de la dimension de la variété sont réalisables par des sous-variétés. En homologie entière, pour toute classe d'homologie z de la variété orientable V, il existe un entier non nul N tel que la classe multiple N·z soit réalisable par une sous-variété. Le chapitre III applique les résultats précédents au problème de Steenrod: Toute classe d'homologie d'un polyèdre fini est-elle l'image de la classe fondamentale d'une variété? On y montre que, si le problème admet une réponse affirmative en homologie mod 2, il existe au contraire, pour toute dimension ≥7, des classes d'homologie entière qui ne sont l'image d'aucune variété différentiable compacte. Le chapitre IV, enfin, est consacré à l'étude des conditions pour qu'une variété soit une variété-bord, et à la classification des variétés cobordantes. Ici encore, on obtient des résultats assez complets pour les classes «mod 2», sans condition d'orientabilité. Par contre, je n'ai pu donner que des résultats fragmentaires pour les groupes Ωk qui s'introduisent dans la classification des variétés orientées, à cause de difficultés algébriques liées en particulier au comportement des puissances de Steenrod dans la suite spec

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1) Les numéros placés entre crochets renvoient à la bibliographie placée à la fin de l'ouvrage.</span></small>

trale d'une fibration. De plus, cette théorie appellerait d'autres recherches sur la signification topologique des nombres caractéristiques de Pon-trjagin.

La présente étude est fondée presque entièrement sur la considération de complexes auxiliaires, que j'ai notés $M(SO(k))$ et $M(O(k))$. La détermination des propriétés homotopiques de ces complexes n'aurait pu être entreprise sans l'emploi des méthodes inaugurées en homotopie par H. Cartan et J. P. Serre. Leurs résultats sur la cohomologie des complexes d'Eilenberg-Mac Lane, notamment, se sont révélés un instrument essentiel, et je leur dois tous mes remerciements pour m'avoir communiqué, avant publication, les résultats de leurs recherches. Je tiens à adresser en particulier mes remerciements à J. P. Serre pour l'aide précieuse qu'il m'a apportée dans la rédaction du manuscrit, et la mise au point de nombreuses démonstrations.

## CHAPITRE I

## Propriétés des applications différentiables

La notation  $V^{n}$  désigne, dans toute la suite, une variété paracompacte $^{2}$ ), différentiable de classe  $C^{\infty}$ , de dimension n.

1. Définitions. Soit $f$ une application de classe $C^m$, $m \geqslant 1$, de la variété $V^n$ dans la variété $M^p$. On appelle critique tout point $x$ de $V^n$ où le rang de l'application $f$ est strictement inférieur à la dimension $p$ de la variété $M^p$; l'ensemble $\Sigma$ des points $x$, ou ensemble critique de $f$, est un ensemble fermé de $V^n$. Tout point $y$ de l'ensemble image $f(\Sigma)$ dans $M^p$ sera dit valeur critique de l'application $f$. Au contraire, tout point $y$ de $M^p$ n'appartenant pas à l'ensemble image $f(\Sigma)$ sera dit valeur régulière de l'application $f^3$).

2. Image réciproque d'une valeur régulière. L'image réciproque $f^{-1}(y)$ d'une valeur régulière $y \in M^{p}$ peut être vide; c'est notamment toujours le cas si la dimension $n$ de $V^{n}$ est strictement inférieure à la

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2) Rappelons qu'une variété paracompacte connexe peut être définie comme variété réunion dénombrable de compacts.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$f(V)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$f^{-1}(x)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">3) On observera que cette définition des valeurs critiques diffère sensiblement de la définition usuelle: lorsque la dimension $n$ de $V$ est inférieure à la dimension $p$ de $M$, tout point de l'image $f(V)$ est une valeur critique, même si l'application $f$ est de rang maximum en tout point de $f^{-1}(x)$. Au contraire tout point n'appartenant pas à l'image $f(V)$ est une valeur régulière.</span></small>

dimension $p$ de $M^{p}$; supposons qu'il n'en soit pas ainsi, et soit $x$ un point de $f^{-1}(y)$; désignons par $y_{1}, y_{2} \ldots y_{p}$ un système de $p$ fonctions coordonnées pour un voisinage de $y$ dans $M^{p}$. Dire que $f$ est de rang $p$ en $x$, c'est dire qu'on peut former, pour un voisinage $U_{x}$ de $x$ assez petit dans $V^{n}$, un système de $n$ fonctions coordonnées, formé des $p$ fonctions $(y_{1}, y_{2} \ldots y_{p})$, et de $(n - p)$ autres fonctions $x_{p+1} \ldots x_{n}$. L'image réciproque $f^{-1}(y)$ est alors définie dans $U_{x}$ par les équations: $y_{1} = y_{2} = \cdots = y_{p} = 0$. Donc $x$ admet dans $f^{-1}(y)$ un voisinage homéomorphe à l'espace euclidien $R^{n-p}$; comme ceci est vrai de tout point $x \in f^{-1}(y)$, l'image réciproque $f^{-1}(y)$ est une sous-variété différentiablement plongée de classe $C^{m}$ de la variété $V^{n}$, soit $W^{n-p}$.

Désignons par $V_x$ l'espace des vecteurs tangents en $x$ à $V^n$, par $W_x$ le sous-espace de $V_x$ formé des vecteurs tangents en $x$ à la sous-variété $W^{n-p}$. Soit de même $M_y$ l'espace des vecteurs tangents en $y$ à la variété $M^p$. Dire que $f$ est de rang $p$ en $x$, c'est dire que l'application $\overline{f}$, prolongée de $f$ aux espaces de vecteurs tangents, définit un isomorphisme du quotient $V_x / W_x$ sur $M_y$. On appellera — par abus de langage — le quotient $V_x / W_x$, l'espace des vecteurs transverses en $x$ à la sous-variété $W^{n-p}$; supposons la variété ambiante $V^n$ munie d'une métrique riemannienne; on peut alors définir en $x$ l'espace $H_x$ des vecteurs normaux à la sous-variété $W^{n-p}$. Il est clair qu'alors les deux espaces $V_x / W_x$ et $H_x$ sont isomorphes, et cet isomorphisme peut être défini globalement, sur toute la sous-variété $W^{n-p}$. Aussi parlera-t-on indifféremment de la structure fibrée des vecteurs transverses ou de celle des vecteurs normaux à une sous-variété.

Nous obtenons finalement: L'image réciproque d'une valeur régulière y de f est une sous-variété  $f^{-1}(y)=W^{n-p}$ , et l'application prolongée  $\overline{f}$  induit un isomorphisme canonique de l'espace fibré des vecteurs normaux à  $W^{n-p}$  sur le produit  $W^{n-p}\times M_{y}$ , ou  $M_{y}\approx R^{p}$  est l'espace des vecteurs tangents en y à la variété  $M^{p}$ .

Remarque. Ceci vaut même si $y$ est adhérent à l'ensemble des valeurs critiques. On observera que, si l'application $f$ est une application propre (en particulier, si $V^n$ est compacte), l'ensemble $f(\Sigma)$ des valeurs critiques est fermé dans $M^p$. En ce cas, toute valeur régulière $y$ admet un voisinage $U_y$ sur lequel l'application $f$ est localement fibrée. Ceci est la forme locale d'un théorème de C. Ehresmann [10].

3. Propriétés de l'ensemble $f(\Sigma)$ des valeurs critiques. Il peut arriver que l'intérieur de l'ensemble $f(\Sigma)$ ne soit pas vide. Par exemple, H. Whitney a construit dans [30] une fonction numérique de classe $C^{1}$

sur le carré, pour laquelle toute valeur est une valeur critique. Mais ce phénomène ne se présente que pour des applications f de classe  $C^{m}$  pour lesquelles l'entier m est strictement inférieur à la dimension n de la variété appliquée. En effet, A. P. Morse a démontré le théorème [16]:

Théorème I. 1. L'ensemble des valeurs critiques d'une fonction numérique de classe $C^m$ sur $R^n$, ou $m \geqslant n$, est de mesure nulle.

(Ce théorème cesse d'être exact pour les fonctions de classe $C^r$, où $r < n$).

Toute variété paracompacte  $V^{n}$  peut être recouverte d'une infinité dénombrable de cartes homéomorphes à  $R^{n}$ ; comme une réunion dénombrable d'ensembles de mesure nulle est encore de mesure nulle, le théorème précédent se généralise en:

Théorème I. 2. L'ensemble des valeurs critiques d'une fonction numérique de classe $C^m$, ou $m \geqslant n$, sur une variété $V^n$, est de mesure nulle. Une nouvelle généralisation de ce théorème donnera$^{4}$):

Théorème I. 3. Si f est une application de classe $C^m$ de $V^n$ dans $M^p$ avec $m \geqslant n$, alors f admet sur tout ouvert de $M^p$ des valeurs régulières.

Ou encore: L'ensemble $f(\Sigma)$ des valeurs critiques de $f$ n'a pas de point intérieur.

Comme le théorème affirme une propriété locale dans la variété image $M^{p}$, on peut supposer que $M^{p}$ n'est autre que l'espace euclidien $R^{p}$; la propriété se démontre alors par récurrence sur l'entier $p$; pour $p = 1$, c'est une conséquence immédiate du théorème I.2. Supposons donc le théorème vrai jusqu'à la dimension $p - 1$ incluse, et soit $f$ une application de classe $C^{n}$ de $V^{n}$ dans $R^{p}$. Désignons par $y_{1}, y_{2} \ldots y_{p}$ un système de coordonnées pour $R^{p}$, et soit $U$ un ouvert de $R^{p}$; soit $[a, b[$ un intervalle ouvert de valeurs prises par la fonction $y_{p}$ sur l'ouvert $U; y_{p}$ est une fonction de classe $C^{n}$ sur $V^{n}$, donc, d'après le théorème I.2, $y_{p}$ admet dans $[a, b[$ une valeur régulière $c; W^{n-1} = y^{-1}(c)$ est une sous-variété de dimension $n - 1$ de $V^{n}$, qu'on supposera non vide (sinon la propriété serait trivialement vérifiée); soit $x$ un point de $W^{n-1}$; pour un voisinage $V_{x}$ assez petit de $x$ dans $V^{n}$, on peut faire choix d'un système de fonctions coordonnées de la forme $(x_{1}, x_{2} \ldots x_{n-1}, y_{p})$ qui contient la fonction $y_{p}$. Soit $U_{c}$ la coupe de l'ouvert $U$ par l'hyperplan $y_{p} = c$. La restriction $f_{c}$ de l'application $f$ à la sous-variété $W^{n-1}$ est de classe $C^{n}$; donc, par hypothèse,

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">4) Comme me l'a signalé M. G. de Rham, ce résultat est une conséquence d'un théorème de A. Sard: The measure of the critical values of differentiable maps, Bull. Amer. Math. Soc., 48, 1942, p. 883–90.</span></small>

$f_{c}: W^{n-1} \to R^{p-1}$, où $R^{p-1}$ désigne l'hyperplan d'équation $y_{p}=c$, admet sur l'ouvert $U_{c}$ une valeur régulière, soit $a$; soit $x \in V^{n}$ un point de l'image réciproque $f_{c}^{-1}(a)=f^{-1}(a,c)$, supposée non vide. Puisque $a$ est valeur régulière pour $f_{c}$, l'application $f_{c}$, définie sur un système de coordonnées locales d'un voisinage $V_{x}$ de $x$ dans $V$, est de la forme: $f(x_{1}, x_{2} \ldots, x_{n-1}, c)=(y_{1}, y_{2}, \ldots y_{p-1})$ et est alors de rang $(p-1)$; donc l'un des mineurs $\left|\frac{\partial y_{i}}{\partial x_{j}}\right|$ n'est pas nul pour $y_{p}=c$, et, par continuité, pour des valeurs de $y_{p}$ assez voisines de $c$; il en résulte qu'on peut prendre dans un voisinage $V_{x}^{\prime} \subset V_{x}$ un système de fonctions coordonnées de la forme: $(x_{1}, x_{2} \ldots x_{n-p}, y_{1}, y_{2} \ldots y_{p})$; c'est dire que $f$ est de rang maximum en $x$; comme ceci est vrai pour tout point $x$ de $f^{-1}(a,c)$, le point $(a,c) \in U$ est une valeur régulière pour $f$. Le théorème I.3 est ainsi démontré.

Si l'application $f$ est propre (en particulier, si $V^n$ est compacte), l'ensemble $f(\Sigma)$ des valeurs critiques de $f$ est un fermé sans point intérieur, c'est un ensemble rare de $M^p$ dans la terminologie de Bourbaki [6]. Dans le cas général, soit $V^n = \cup_j K_j$ un recouvrement dénombrable de $V^n$ par des compacts $K_j$; chacun des ensembles intersections $\Sigma_j = K_j \cap \Sigma$ est compact, et $f(\Sigma_j)$ est un compact rare de $M^p$; donc, $f(\Sigma) = \cup_j f(\Sigma_j)$ est une réunion dénombrable d'ensembles fermés rares, c'est, dans la terminologie de [6], un sous-ensemble maigre de $M^p$.

## 3. L'image réciproque d'une sous-variété.

Définition: voisinage tubulaire d'une sous-variété. Soit $N^{p-q}$ une sous-variété compacte, différentiablement plongée de classe $C^\infty$, de la variété $M^p$. Supposons $M^p$ munie d'une métrique riemannienne de classe $C^\infty$. Soit $T$ l'ensemble des points de $M^p$ situés à une distance $\leqslant \varepsilon$ de la sous-variété $N^{p-q}$. Si $\varepsilon$ a été pris assez petit, par tout point $x \in T$ il ne passe qu'une géodésique normale à $N^{p-q}$, aboutissant sur $N^{p-q}$ en un point $y = p(x)$. L'application $p: T \to N^{p-q}$ est une fibration, la fibre $p^{-1}(y)$ est une $q$-boule géodésique normale. Le bord $F$ de $T$ est une variété de dimension $p - 1$, fibrée par $p$ sur $N^{p-q}$ en $(q - 1)$-sphères. Un tel voisinage $T$ de $N^{p-q}$ sera appelé, par toute la suite, un voisinage tubulaire normal de la sous-variété $N^{p-q}$. Il est clair que la fibration $p$ admet pour groupe de structure un sous-groupe du groupe orthogonal $O(q)$ et la structure fibrée de $T$ est canoniquement isomorphe à celle de l'espace fibré des vecteurs normaux (donc transverses) à la sous-variété $N^{p-q}$ dans $M^p$.

Rappel sur les homéomorphismes différentiables d'une boule.

Soit $B^q$ la $q$-boule fermée de centre $O$; soit $A$ un homéomorphisme de $B^q$ de classe $C^\infty$ sur elle-même; si on suppose de plus que l'homéomorphisme inverse $A^{-1}$ est différentiable, alors l'application de $B^q$ sur elle-même est en tout point de rang $q$. On considérera le groupe de ces homéomorphismes qui se réduisent à l'identité sur le bord $S^{q-1}$ de $B^q$, soit $G$.

Etant donné un point $c$ intérieur à $B^{q}$, on peut définir, de bien des façons, un homéomorphisme $A$ de $G$, tel que $A(c) = O$; on peut de plus montrer qu'un tel homéomorphisme $A$ est homotope à l'identité dans $G$, muni de la topologie ainsi définie: topologie de la convergence uniforme pour l'application $A: B^{q} \to B^{q}$, ainsi que pour l'application inverse $A^{-1}$, et pour les dérivées partielles de $A$ et $A^{-1}$ jusqu'à l'ordre $n$ inclus. On peut définir dans $G$ un homéomorphisme dépendant continuement du paramètre $t(0 \leqslant t \leqslant 1)$, $A_{t}$, tel que $A_{0} = A$ et $A_{1} =$ identité.

Le groupe des homéomorphismes H d'un voisinage tubulaire normal.

Soit $T$ un voisinage tubulaire normal de la sous-variété $N^{p-q}$ dans $M^{p}$; on lui associe le groupe $H$ des homéomorphismes de classe $C^{n}$ de $T$ ainsi définis:

i) Tout élément  $A \in H$  applique globalement toute fibre  $p^{-1}(y)$  sur elle-même.

ii) Tout élément de H se réduit à l'identité sur le bord F de T. Le groupe H est muni de la topologie ainsi définie: topologie de la convergence uniforme pour les applications A et  $A^{-1}$ , ainsi que leurs dérivées partielles jusqu'à l'ordre n. (Pour définir les dérivées partielles d'une application  $A : T \to T$ , on peut plonger T dans un espace euclidien  $R^{k}$ ; la topologie définie à l'aide des coordonnées dans  $R^{k}$  est indépendante de l'immersion). Avec la topologie ainsi définie, H est un espace de Baire. En effet, H est un espace métrique complet: il suffit de montrer que tout filtre de Cauchy  $(A_{t})$  dans H converge dans H; en effet, pour tout point  $x \in T$ , les points  $A_{t}(x)$  forment un filtre de Cauchy dans T, qui définit un point  $J(x) \in T$ , et l'application limite J est de classe  $C^{n}$ ; de même, le filtre de Cauchy des  $A_{t}^{-1}(x)$  est convergent, et définit une application de classe  $C^{n}, J^{-1}$  qui est inverse de J.

Définition: Application t-régulière sur une sous-variété. Soit f une application différentiable de  $V^{n}$  dans  $M^{p}$ , et soit y un point de la sous-variété  $N^{p-q}$  de  $M^{p}$ . Soit  $M_{y}$  l'espace des vecteurs tangents en y à  $M^{p}$ ,  $N_{y}$  le sous-espace des vecteurs tangents à la sous-variété  $N^{p-q}$ . Soit x un point quelconque de l'image réciproque  $f^{-1}(y)$ ,  $V_{x}$  l'espace des

vecteurs tangents en $x$ à $V^{n}$. On dira que $y$ est une valeur $t$-régulière, si, en tout point $x \in f^{-1}(y)$, l'application prolongée $\overline{f}: V_{x} \to M_{y} \to M_{y}/N_{y}$ est de rang $q$, et applique $V_{x}$ sur l'espace des vecteurs transverses à $N^{p-q}$ à $M^{p5}$).

4. Image réciproque d'une sous-variété par une application t-régulière. On dira que l'application $f: V^{n} \to M^{p}$ est t-régulière sur la sous-variété $N^{p-q} \subset M^{p}$, si tout point $y$ de $N^{p-q}$ est une valeur t-régulière de $f$. Désignons, dans une carte locale autour de $y$, par $y_{1}, y_{2} \ldots y_{q}$ un système de $q$ fonctions coordonnées telles que les équations $y_{1} = y_{2} = \cdots = y_{q} = 0$ définissent localement la sous-variété $N^{p-q}$. Soit $x$ un point de l'image réciproque $f^{-1}(y)$, supposée non vide; si $y$ est une valeur t-régulière, on peut trouver un voisinage $U_{x}$ de $x$ dans $V^{n}$ dans lequel existe un système de $n$ fonctions coordonnées de la forme: $(x_{1}, x_{2}, \ldots x_{n-q}, y_{1}, y_{2} \ldots y_{q})$; l'image réciproque $f^{-1}(N^{p-q})$ est définie dans $U_{x}$ par les équations: $y_{1} = y_{2} = \ldots = y_{q} = 0$; $x$ admet donc dans $f^{-1}(y)$ un voisinage homéomorphe à $R^{n-q}$. C'est dire que l'image réciproque $f^{-1}(N^{p-q})$ est une sous-variété $W^{n-q}$ différentiablement plongée de classe $C^{n}$.

Soit $V_x$ l'espace des vecteurs tangents en $x$ à $V^n$, $W_x$ l'espace des vecteurs tangents en $x$ à $W^{n-q}$. Si $y = f(x)$ est une valeur t-régulière, cela veut dire que l'application prolongée $\overline{f}$ induit un isomorphisme de l'espace des vecteurs transverses $V_x / W_x$ sur l'espace des vecteurs transverses en $y$ à $N^{p-q} : M_y / N_y$. Globalement, la structure fibrée des vecteurs transverses (ou normaux) à $W^{n-q}$ dans $V^n$ est canoniquement isomorphe à la structure induite de celle des vecteurs transverses à $N^{p-q}$ dans $M^p$ par l'application $f$.

Soit y un point de  $N^{p-q}$ ; désignons par X la boule ouverte de centre y de rayon géodésique r, dans la sous-variété  $N^{p-q}$ , par  $X'$  la boule concentrique de rayon 2r; on suppose r assez petit pour que  $X'$  soit effectivement une boule. Dans ces conditions, les sous-ensembles du voisinage tubulaire T définis par:

$D = p^{-1}(X)$; $D' = p^{-1}(X')$ sont resp. homéomorphes aux produits: $X \times B^q$; $X' \times B^q$ puisque toute fibration est triviale sur une boule. Soit $k : D'$ (ou $D$) → $B^q$ l'application définie par cet homéomorphisme. Nous allons démontrer le:

Lemme I. 4. L'ensemble des homéomorphismes $A \in H$ du voisinage

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$f^{-1}(y)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$y\in Np - q$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">5) L'image réciproque $f^{-1}(y)$ d'une valeur $t$-régulière $y \in N^{p - q}$ peut être vide; on dira en ce cas que c'est une valeur $t$-régulière triviale.</span></small>

tubulaire T tels que l'application composée  $A \circ f$ , où  $f : V^{n} \to M^{p}$  est de classe  $C^{n}$ , n'est pas t-régulière sur X, est un sous-ensemble maigre de l'espace de Baire H.

Dire qu'une application $g: V^n \to M^p$ n'est pas t-régulière sur $X$, c'est dire que l'application composée $k \circ g$, définie sur $g^{-1}(D)$, admet le centre $O$ de la fibre $B^q$ pour valeur critique (en effet, par définition, l'application prolongée $\overline{k}$ induit, en un point $y \in M^p$, le quotient de l'espace des vecteurs tangents $M_y$ par le sous-espace des vecteurs tangents $N_y$ à la sous-variété $N^{p-q}$).

Désignons par $K_i$ un compact de $V^n$; on dira qu'un homéomorphisme $A \in H$ est $i$-critique, si l'application composée $k \circ A \circ f$, définie sur $f^{-1}(D)$, admet dans $K_i$ au moins un point critique $x$ tel que $f(x) \in X$. Soit $\sigma_i$ l'ensemble des $A \in H$ qui sont $i$-critiques. On va montrer que $\sigma_i$ est un fermé de $H$ sans point intérieur.

i) $\sigma_{i}$ est fermé. Soit $A$ un élément de $H$ qui n'appartient pas à $\sigma_{i}$; c'est dire que l'application composée $k \circ A \circ f$ admet $O$ comme valeur régulière, lorsqu'elle est restreinte à $K_{i} \cap f^{-1}(D)$. Soient $y_{1}, y_{2} \ldots y_{q}$ un système de fonctions coordonnées pour la $q$-boule $B^{q}$; par hypothèse, sur l'intersection $K_{i} \cap f^{-1} \circ A^{-1}(N^{p-q})$, les jacobiens d'ordre $q \left| \frac{\partial y_{i}}{\partial x_{k}} \right|$ ont en valeur absolue une borne inférieure strictement positive, soit $3B$, où $B > 0$. Il existe par suite un voisinage fermé — donc compact — $J$ de $K_{i} \cap f^{-1} \circ A^{-1}(N^{p-q})$ dans $K_{i}$ dans lequel ces jacobiens $\left| \frac{\partial y_{j}}{\partial x_{k}} \right|$ sont en valeur absolue $> 2B$.

Considérons maintenant l'ensemble des homéomorphismes $A'$ de $\pmb{H}$ assez voisins de $A$ dans $\pmb{H}$ pour que:

1. La nouvelle intersection $K_{i} \cap f^{-1} A'^{-1}(N^{p - q})$ soit tout entière contenue dans $J$: ceci peut être obtenu en majorant convenablement la distance (dans $M^{p}$) de $A$ à $A'$: il suffit de prendre $||A'(y) - A(y)||$ plus petit que la distance de $O$ à la frontière de l'ensemble image $k \circ A f(J)$.

2. Les jacobiens  $\left|\frac{\partial y_{j}}{\partial x_{k}}\right|$  associés à l'application  $k \circ A' \circ f$  soient, dans J, supérieurs en valeur absolue à B > 0; ceci sera obtenu par une approximation convenable sur les dérivées partielles du premier ordre de l'application  $A'$  par rapport à celles de l'application A: en effet, les jacobiens  $\left|\frac{\partial y_{j}}{\partial x_{k}}\right|$  sont des fonctions continues des dérivées partielles du premier ordre de l'application A.

Pour tout $A'$ assez voisin de $A$ qui satisfait à ces deux conditions, les jacobiens $\left|\frac{\partial y_j}{\partial x_k}\right|$ ne s'annulent pas sur $K_i \cap f^{-1} A'^{-1}(N^{p-q})$, et par suite $A' \circ f$ est $t$-régulière sur la boule $X$.

ii) $\sigma_{i}$ n'a pas de point intérieur. Soit $A$ un élément de $\sigma_{i}$; l'application composée $k \circ A \circ f$ admet $O$ pour valeur critique; mais, comme l'application est de classe $C^{n}$, elle admet, d'après le théorème I.3, une valeur régulière $c$ aussi voisine qu'on voudra de $O$; soit $E$ l'homéomorphisme de $D' = p^{-1}(X')$ défini comme suit: soit $G$ un homéomorphisme de la $q$-boule $B^{q}$ qui applique $c$ sur $O$, et se réduit à l'identité sur le bord $S^{q-1}$ de $B^{q}$, et $G_{t}$ un homéomorphisme dépendant continuement du paramètre $t \in I$, tel que $G_{0} = G$ et $G_{1} =$ identité. Soit $d$ une fonction de classe $C^{\infty}$, égale à 0 sur $\overline{X}$, égale à l'unité à la frontière de $X'$, et croissant de 0 à 1 lorsque la distance géodésique au centre $y$ de $X$ croît de $r$ à $2r$; usant de l'homéomorphisme: $D' \approx X' \times B^{q}$, $E$ peut être défini par la formule:

$$
E \left(y _ {1}, z\right) = \left(y _ {1}, G _ {d (y)} (z)\right) \quad y _ {1} \in X ^ {\prime}, z \in B ^ {q}.
$$

L'homéomorphisme $E$ conserve globalement les fibres $p^{-1}(y)$, et se réduit à l'identité sur la frontière de $D'$; $E$ peut par suite être prolongé en un homéomorphisme du voisinage tubulaire $T$ sur lui-même; il suffit de prendre la transformation identique à l'extérieur de $D'$. L'élément $E$ ainsi défini appartient alors au groupe $H$.

Par ailleurs, l'application $E \circ A \circ f$ est t-régulière sur $X$, car, par construction même, l'application composée $k \circ E \circ A \circ f$ admet $O$ pour valeur régulière. Si donc on pose $A' = E \circ A$, l'application $A' \circ f$ est t-régulière sur $X$ et peut-être rendue arbitrairement voisine de $A \circ f$: en effet, l'homéomorphisme $E$ peut-être pris aussi voisin qu'on voudra de l'identité: il suffit pour cela de prendre la valeur régulière $c$ assez voisine de $O$.

(On remarquera que dans cette seconde partie du raisonnement le compact $K_{i}$ n'intervient pas: on montre ainsi que l'ensemble des $A$ tels que $A \circ f$ n'est pas $t$-régulière sur $X$ est sans point intérieur dans $H$).

Comme la variété  $V^{n}$  est réunion dénombrable des compacts  $K_{j}$ , l'ensemble  $\sigma$  des A tels que  $A \circ f$  n'est pas t-régulière sur X est la réunion dénombrable des ensembles rares  $\sigma_{i}$ , c'est donc un ensemble maigre de H, et le Lemme I.4 est démontré.

La sous-variété $N^{p-q}$ étant supposée paracompacte, on peut la recouvrir par une infinité dénombrable de boules ouvertes telles que $X$. (No-tons en passant, qu'on peut définir un voisinage tubulaire normal pour

une sous-variété paracompacte: le seul changement par rapport au cas compact est que le «rayon» du voisinage tubulaire doit être pris variable.) Dès lors, l'ensemble des $A$ tels que $A \circ f$ n'est pas $t$-régulière sur $N^{p-q}$ est une réunion dénombrable d'ensembles maigres de $H$, donc aussi un ensemble maigre, sans point intérieur. Ceci nous permet d'énoncer le théorème:

Théorème I. 5. Soit $f$ une application de classe $C^n$ de la variété $V^n$ dans la variété $M^p$, et soit $N^{p-q}$ une sous-variété paracompacte de $M^p$, et $T$ un voisinage tubulaire normal de $N^{p-q}$ dans $M^p$. Il est possible de trouver un homéomorphisme $A$ de $T$ sur lui-même, arbitrairement voisin de l'identité dans $H$, tel que, si $f' = A \circ f$:

i) L'image réciproque $f'^{-1}(N^{p - q})$ de $N^{p - q}$ soit une sous-variété de $V^n$, de dimension $n - q: W^{n - q}$ différentiablement plongée de classe $C^n$.

ii) L'espace fibré des vecteurs normaux à  $W^{n-q}$  dans  $V^{n}$  soit canoniquement isomorphe à l'espace induit de la structure fibrée des vecteurs normaux à  $N^{p-q}$  dans  $M^{p}$ .

5. Le théorème d'isotopie. La propriété énoncée ci-dessous ne nous servira que dans la partie IV, et dans le cas $V^n$ compacte seulement ; aussi ne l'établirons-nous que sous cette hypothèse.

Soit $f$ une application de classe $C^{n}$ de la variété $V^{n}$ dans $M^{p}$, $t$-régulière sur la sous-variété compacte $N^{p-q}$. Supposons qu'on ait défini en chaque point $y$ de $N^{p-q}$ un système de $q$-fonctions coordonnées normales $y_{1}, y_{2} \ldots y_{q}$, tel que dans un voisinage de $y$, $N^{p-q}$ soit définie par les équations $y_{1} = y_{2} = \cdots = y_{q} = 0$. $N^{p-q}$ étant supposée compacte, on pourra définir $N^{p-q}$ avec un nombre fini de systèmes $(y_{j})$. A l'aide d'une métrique riemannienne dans $V^{n}$, on définira un voisinage tubulaire $Q$ de la sous-variété $W^{n-q} = f^{-1}(N^{p-q})$, et dont le rayon $\varepsilon$ sera pris assez petit pour satisfaire à la condition suivante:

Soit $x$ un point de $W^{n-q}$, $B_x$ la $q$-boule géodésique normale en $x$ à $W^{n-q}$: les fonctions $(y_j)$ associées à $y = f(x)$, sont, pour tout $x$, un système de fonctions coordonnées pour la $q$-boule $B_x$. Il est évidemment possible de satisfaire à cette condition, puisque $f$ est supposée $t$-régulière, et que $W^{n-q}$ est compacte.

Soit $A$ un élément du groupe $\boldsymbol{H}$, voisin de l'identité. On se propose d'étudier l'image réciproque $g^{-1}(N^{p-q})$, où $g = A \circ f$. Il est clair, tout d'abord, que si $A$ est assez voisin de l'identité, l'application $g$ est elle aussi $t$-régulière sur $N^{p-q}$; en effet, si on prend $A$ assez voisin de l'identité pour que $||A(y) - y||$ dans $M^p$ soit strictement inférieure

à la distance de $N^{p-q}$ à la frontière de $f(Q)$, l'image réciproque $g^{-1}(N^{p-q})$ sera tout entière contenue dans $Q$.

On peut de plus supposer $A$ assez voisin de l'identité — au point de vue de l'écart sur les dérivées partielles du premier ordre — pour que l'application $g$, soit, comme $f$, de rang $q$ sur toute $q$-boule $B_x$. Dans ces conditions, l'application $g$ est $t$-régulière. On va montrer que, moyennant éventuellement une approximation un peu plus serrée, les deux sous-variétés $W^{n-q} = f^{-1}(N^{p-q})$ et $W' = g^{-1}(N^{p-q})$ sont isotopes dans $V^n$. La démonstration ne fait que suivre un schéma donné par Seifert dans [21].

Désignant par $(y_{j})$ un système de $q$ fonctions coordonnées transverses au voisinage du point $y = f(x)$ de $N^{p - q}$, à tout point $z \in B_x$, associons le point de $R^q$ dont les coordonnées sont $y_{j}(g(z))$; on définit ainsi une application $L: B_x \to R^q$ qui, si $g = f$, donne l'homéomorphisme identique; l'image réciproque $L^{-1}(O)$ est l'intersection de $B_x$ avec la variété $W' = g^{-1}(N^{p - q})$.

$\varepsilon$ désignant toujours le rayon de $B_x$, on peut prendre $A$ assez voisin de 1, donc $g$ assez voisin de $f$, pour que, $\|L(z)-z\|\leq\varepsilon$, uniformément en $x$, et pour tout système $(y_f)$ associé à $y=f(x)$. Ceci implique que la sphère $L(S^{q-1})$ image du bord $S^{q-1}$ de $B_x$ est homotope à $S^{q-1}$ dans l'espace $R^q-O$, privé de l'origine $O$. Il en résulte que le degré de l'application $L$, est, sur le point $O$, égal à celui de l'application identique, et est donc égal à $+1$. Par ailleurs, l'application $L$ est de rang maximum en tout point de $B_x$: au voisinage de tout point $z$ de $B_x$, $L$ est un homéomorphisme local, et par suite, l'image réciproque $L^{-1}(O)$ ne peut contenir que des points isolés; comme tout point de $B_x$ est appliqué sur $R^q$ avec le degré $+1$ (signe du jacobien de l'application $L$), l'image réciproque $L^{-1}(O)$ est formée d'un point $x'$ unique. Ainsi $W'$ ne rencontre chaque boule $B_x$ qu'en un point unique $x'$; la correspondance $x\to x'$ est un homéomorphisme de $W^{n-q}$ sur $W'^{n-q}$. De plus, comme $x'$ peut être joint à $x$ par un arc géodésique $s(x,x')$ dans $B_x$, on peut définir évidemment une isotopie qui déforme $W^{n-q}$ sur $W'^{n-q}$. On obtient ainsi:

Théorème I. 6. Soit f une application de classe $C^n$ de la variété compacte $V^n$ dans $M^p$, t-régulière sur la sous-variété compacte $N^{p-q}$. Alors, pour tout homéomorphisme A de H du voisinage tubulaire de $N^{p-q}$, assez voisin de l'identité dans H, l'application $g = A \circ f$ est t-régulière sur $N^{p-q}$, et les deux sous-variétés $W^{n-q} = f^{-1}(N^{p-q})$; $W'^{n-q} = g^{-1}(N^{p-q})$ sont isotopes dans $V^n$.

## CHAPITRE II

## Sous-variétés et classes d'homologie d'une variété

1. Généralités. Soit $V^n$ une variété orientable ; orienter $V^n$, c'est faire choix, dans le groupe d'homologie entière $H_n(V^n; Z)$ d'une classe privilégiée, qu'on appellera classe fondamentale de la variété $V^n$ ainsi orientée. Dans $V^n$ orientée, la dualité de Poincaré s'exprime par un isomorphisme canonique entre le groupe d'homologie $H_{n-k}(V^n; Z)$ et le groupe de cohomologie $H^k(V^n; Z)$. On appellera classes correspondantes deux classes images l'une de l'autre pour cet isomorphisme. Si le groupe des coefficients est le groupe $Z_2$ des entiers mod 2, la classe fondamentale de $H_n(V^n; Z_2)$ est définie de façon unique, même si $V^n$ n'est pas orientable, et l'isomorphisme, dit de Poincaré-Veblen, entre $H_{n-k}(V^n; Z_2)$ et $H^k(V^n; Z_2)$ est canoniquement défini. Ici, et dans tout ce qui suit, nous supposons la variété $V^n$ compacte ; nous ne ferons qu'indiquer brièvement la généralisation possible des résultats aux variétés paracompactes non compactes.

Soit $W^p$ une sous-variété de dimension $p$. L'application identique $i: W^p \to V^n$ induit un homomorphisme $i_*$ de l'homologie $H_p(W^p)$ dans l'homologie $H_p(V^n)$; soit $z \in H_p(V^n)$ la classe image par $i_*$ de la classe fondamentale de la variété $W^p$. On dit alors que la classe $z$ est réalisée par la sous-variété $W^p$. La question envisagée ici est la suivante: une classe d'homologie donnée $z$ d'une variété $V^n$ est-elle réalisable par une sous-variété? Le problème, on le verra, reçoit des réponses très différentes suivant que le groupe des coefficients est le groupe $Z$ des entiers ou le groupe $Z_2$ à deux éléments. Dans le premier cas, on supposera toujours, même si on ne le rappelle pas explicitement, que la variété $V^n$ considérée est orientable, et munie d'une orientation fixée, bien qu'arbitrairement choisie.

2. Complexe associé à un sous-groupe fermé du groupe orthogonal. Soit $G$ un sous-groupe fermé du groupe orthogonal à $k$ variables $O(k)$. On sait que tout espace fibré en sphères $S^{k-1}$ dont $G$ est groupe de structure est induit d'un espace fibré universel $E_G$, dont la base $B_G$ est une variété compacte; (on se restreint ici, évidemment, aux espaces fibrés dont la base est de dimension finie $\leqslant N$). Désignons par $A_G$ le «mapping cylinder» de l'application fibrée $E_G \to B_G$, espace fibré en $k$-boules sur $B_G$; c'est une variété à bord de bord $E_G$; on désignera par $A_G'$ le complémentaire $A_G - E_G$, espace fibré en $k$-boules ouvertes associé à $E_G$ (Cf. [27]).

Définition. On appellera complexe associé au sous-groupe $G$ de $O(k)$, l'espace dénoté $M(G)$ obtenu à partir de $A_{G}$ par identification en un point $a$ de son bord $E_{G}$; $M(G)$ est, si l'on veut, la compactification d'Alexandroff de l'espace fibré en boules ouvertes $A_{G}^{\prime}$.

Cohomologie de $M(G)$. La cohomologie $H^{r}(M(G))$ s'identifie, pour tout $r > 0$, à la cohomologie à supports compacts $H_{K}^{r}(M(G))$, ou encore, à la cohomologie relative $H^{r}(A_{G}, E_{G})$. Or, on a l'isomorphisme classique de la théorie des espaces fibrés en boules ouvertes (Cf. [26]):

$$
\varphi_ {G} ^ {*}: H ^ {r - k} (B _ {G}) \to H _ {K} ^ {r} (A _ {G} ^ {\prime}) \approx H ^ {r} (M (G))
$$

les coefficients étant pris dans le groupe $Z_2$ en général, dans $Z$ si l'espace fibré $E_G$ est orientable ($G$ connexe). La cohomologie $H^*(M(G))$ s'obtient donc, pour les dimensions $r > 0$, en majorant de $k$ unités la graduation de la cohomologie $H^*(B_G)$ de l'espace classifiant $B_G$. En particulier, le premier groupe $H^r(M(G))$ non nul, pour $r > 0$, est $H^k(M(G))$; il est engendré par la classe $U \in H^k(M(G))$ définie par:

$$
U = \varphi_ {G} ^ {*} (\omega_ {G})
$$

où $\omega_{G}$ désigne la classe-unité de $H^{o}(B_{G})$. La classe $U$ sera appelée classe fondamentale du complexe $M(G)$. Rappelons que $U$ est une classe à coefficients entiers si $E_{G}$ est orientable ($G$ connexe); c'est une classe mod 2, si $E_{G}$ n'est pas orientable ($G$ non connexe).

3. Le théorème fondamental. Définition. On dira qu'une classe de cohomologie $u \in H^{k}(A)$ d'un espace $A$ est réalisable pour le groupe $G \subset O(k)$, ou encore: admet une $G$-réalisation, s'il existe une application $f: A \to M(G)$ telle que $u$ soit l'image, pour l'homomorphisme $f^{*}$ induit par $f$, de la classe fondamentale $U$ du complexe $M(G)$.

Nous avons alors le théorème:

Théorème II. 1. Pour qu'une classe d'homologie $z \in H_{n-k}(V^n)$, $k > 0$, puisse être réalisée par une sous-variété $W^{n-k}$ dont l'espace fibré des vecteurs normaux admet $G$ pour groupe de structure, il faut et il suffit que la classe de cohomologie $u \in H^k(V^n)$ correspondante à $z$ soit réalisable pour le groupe $G$.

i) La condition est nécessaire. Supposons qu'il existe dans $V^n$ une sous-variété $W^{n-k}$ dont la classe fondamentale appartient à $z$; soit $N$ un voisinage tubulaire normal de $W^{n-k}$, de bord $T$. La fibration géodésique normale $p: N \to W^{n-k}$ admet, par hypothèse, $G$ pour groupe de structure. $N$ est induit de l'espace universel $A_G$ par une application

$g: W^{n-k} \to B_G$ ; il existe donc une application  $F: N \to A_G$  (qui applique fibre sur fibre), telle que le diagramme:

$$
\begin{array}{c} N \xrightarrow {F} A _ {G} \\ p \Big \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Big \downarrow p _ {G} \\ W ^ {n - k} \xrightarrow {g} B _ {G} \end{array}
$$

soit commutatif.

La restriction de $F$ au bord $T$ de $N$ applique $T$ dans le bord $E_{G}$ de $A_{G}$. Si l'on désigne par $\varphi^{*}$, resp. $\varphi_{G}^{*}$, les isomorphismes des espaces fibrés en $k$-boules $N$, resp. $A_{G}$, le diagramme:

$$
\begin{array}{c} H ^ {k} (N, T) \xrightarrow {F} H ^ {k} (A _ {G}, E _ {G}) \\ \varphi^ {*} \uparrow \\ H ^ {o} (W ^ {n - k}) \xrightarrow {g} H ^ {o} (B _ {G}) \end{array}\tag{1}
$$

est également commutatif.

Par ailleurs, soit $j_{*}: H^{k}(N, T) \to H^{k}(V^{n})$ l'homomorphisme canonique défini par l'injection; on sait que dans la variété ouverte $N' = N - T$, la classe $\varphi^{*}(\omega)$ correspond — par la dualité de Poincaré — à la classe d'homologie fondamentale de la base $W^{n-k}$ (Cf. [27] Th. I. 8). Par suite, la classe $j_{*} \varphi^{*}(\omega) \in H^{k}(V^{n})$ n'est autre que la classe $u$ correspondant à $z$.

Désignons par $h: A_G \to M(G)$ l'application obtenue en identifiant en un point $a$ le bord $E_G$ de $A_G$; l'application composée $h \circ g$ applique le bord $T$ de $N$ sur le point $a$; par suite, l'application $h \circ g$ peut être étendue à toute la variété $V^n$: il suffit d'appliquer le complémentaire $V^n - N$ sur le point $a$; on définit ainsi une application $f$ de $V^n$ dans $M(G)$, pour laquelle on a bien:

$f^{*}(U) = f\varphi_{G}^{*}(\omega_{G}) = j_{*}\varphi^{*}(\omega) = u,\quad \mathrm{d}^{\prime}\mathrm{après}\quad \mathrm{le}\quad \mathrm{diagramme}\quad \mathrm{commutatif (1).}$

ii) La condition est suffisante. Supposons qu'il existe une application $f$ de $V^{n}$ dans $M(G)$, telle que $f^{*}(U)=u$; l'espace $M(G)$, privé du point exceptionnel $a$, est une variété différentiable; on pourra régulariser la restriction de $f$ au complémentaire $V^{n}-f^{-1}(a)$, de façon à obtenir une nouvelle application $f_{1}$, voisine de $f$, qui soit différentiable de classe $C^{n}$ sur $V^{n}-f^{-1}(a)$; on appliquera alors à l'application $f_{1}$ le théorème I.5. On pourra ainsi définir une application $F$, arbitrairement voisine de $f$, telle que l'image réciproque $F^{-1}(B_{G})$ soit une sous-variété $W^{n-k}$;

l'espace des vecteurs normaux à $W^{n-k}$, induit de l'espace $A_G$, admet $G$ pour groupe de structure. Désignant alors par $\varphi^*$ l'isomorphisme $\varphi^*$ associé à un voisinage tubulaire normal de $W^{n-k}$ dans $V^n$, la classe $u = f^*(U) = F^*(U)$ n'est autre que $j_* \varphi^*(\omega)$, $\omega$ classe-unité de $W^{n-k}$; comme on l'a vu en i), ceci exprime que $u$ correspond par la dualité de Poincaré à la classe du cycle fondamental porté par la sous-variété $W^{n-k}$.

Extension du théorème II.1 aux variétés paracompactes non compactes.
Rappelons que dans une variété paracompacte non compacte, il existe autant de théorèmes de dualité que de familles ( $\Phi$ ) de sous-ensembles fermés utilisés pour définir homologie et cohomologie (Cf. [26], Th. 0.3). On peut se poser, dans ces conditions, la question suivante: une classe d'homologie à supports dans ( $\Phi$ ),  $z \in H_{n-k}^{\Phi}(V^{n})$  peut-elle être réalisée par une sous-variété  $W^{n-k}$ ? Peu de modifications doivent être apportées à la démonstration précédente pour y répondre: on observera d'abord que le voisinage tubulaire normal d'une sous-variété paracompacte peut toujours être défini, à condition de prendre son rayon éventuellement variable. Disons de plus qu'une application  $f: V \to M$  est  $\Phi$ -propre, si l'image réciproque  $f^{-1}(K)$  de tout compact K de M appartient à ( $\Phi$ ) (si  $\Phi$  est la famille K des compacts de V, on retrouve la définition classique des applications propres). On aura alors le théorème:

Théorème II.1'. Pour qu'une classe $z \in H_{n-k}^{\Phi}(V^n)$ soit réalisable par une sous-variété dont l'espace fibré des vecteurs normaux admette $G$ pour groupe de structure, il faut et il suffit qu'il existe une application $f: V^n \to M(G)$, $\Phi$-propre sur $M(G) - a$, telle que la classe image $f^*(U) \in H_\Phi^k(V^n)$ corresponde à $z$ par la dualité de Poincaré.

4. Cas où $G$ se réduit à l'élément unité $e \in O(k)$. L'espace classifiant $B_G$ se réduit alors à un point, $A_G$ est une $k$-boule fermée et le complexe $M(e)$ n'est autre que la sphère $S^k$. Disons qu'une classe de cohomologie entière $u$ d'un espace $A$ est sphérique, s'il existe une application $f: A \to S^k$, telle que $u = f^*(s^k)$, $s^k$ désignant la classe fondamentale de $H^k(S^k; Z)$. Le théorème I.1 nous donnera alors:

Théorème II. 2. Pour qu'une classe d'homologie $z \in H_{n-k}(V^n; Z)$ de la variété orientable $V^n$ puisse être réalisée par une sous-variété dont l'espace fibré des vecteurs normaux est trivial, il faut et il suffit que la classe de cohomologie $u \in H^k(V^n; Z)$ correspondant à $z$ soit sphérique.

On ne connaît pas, en Topologie Algébrique, de condition nécessaire et suffisante pour qu'une classe de cohomologie donnée soit sphérique ;

le seul résultat de nature générale a été obtenu par J. P. Serre [22]; le voici:

Théorème II. 3. Pour toute classe $x \in H^{k}(A;Z)$ d'un espace $A$ de dimension finie $n$, avec $k$ impair, ou $n < 2k$, il existe un entier non nul $N$, ne dépendant que de $k$ et de $n$, tel que la classe multiple $N \cdot x$ soit une classe sphérique. De là, on déduit:

Théorème II. 4. Soit $z \in H_{n-k}(V^n; Z)$ une classe d'homologie entière de la variété orientable $V^n$, avec $k$ impair, ou $n < 2k$. Il existe alors un entier non nul $N$, ne dépendant que de $k$ et de $n$, tel que la classe multiple $N \cdot z$ puisse être réalisée par une sous-variété $W^{n-k}$ dont l'espace fibré des vecteurs normaux est trivial.

5. Description des complexes $M(O(k))$ et $M(SO(k))$. Il résulte immédiatement du théorème II.1 qu'on a les théorèmes suivants, qui montrent l'importance des complexes $M(O(k))$ et $M(SO(k))$:

Théorème II.5. Pour qu'une classe d'homologie $z \in H_{n-k}(V^n; Z)$ de la variété orientable $V^n$ soit réalisable par une sous-variété, il faut et il suffit que la classe de cohomologie u correspondant à $z$ soit réalisable pour le groupe des rotations.

Théorème II.5'. Pour qu'une classe d'homologie mod 2 $z \in H_{n-k}(V^n; Z_2)$ de la variété $V^n$ soit réalisable par une sous-variété, il faut et il suffit que la classe de cohomologie u correspondant à $z$ admette une réalisation orthogonale.

On désignera par $G_{k}$ la grassmannienne des $k$-plans non-orientés dans un espace euclidien $R^{m}$, où $m$ est très grand. $G_{k}$ est, c'est bien connu, l'espace classifiant $B_{O(k)}$ associé au groupe orthogonal $O(k)$. On désignera par $\widehat{G}_{k}$ la grassmannienne des $k$-plans orientés dans $R^{m}$; c'est le classifiant $B_{SO(k)}$ associé au groupe des rotations $SO(k) \cdot \widehat{G}_{k}$ est un revêtement à deux feuilllets de $G_{k}$.

L'espace fibré universel $E_{SO(k)}$ s'obtient en associant à tout $k$-plan de $\widehat{G}_k$ son intersection $S^{k-1}$ avec la sphère de rayon 1 dans $R^m$; $E_{SO(k)}$ peut donc être considéré comme l'espace des couples formés d'un $k$-plan orienté et d'un vecteur unitaire contenu dedans; associons à ce couple le $(k-1)$-plan orthogonal au vecteur dans le $k$-plan; on définit ainsi une fibration de $E_{SO(k)}$ sur la grassmannienne $\widehat{G}_{k-1}$, la fibre étant une sphère $S^{m-k}$, de grande dimension. Par suite, pour les dimensions inférieures à la dimension classifiante $m - k$, $E_{SO(k)}$ a même type d'homo-

topie que la grassmannienne $\widehat{G}_{k-1}$; et l'injection $E_{SO(k)} \to A_{SO(k)}$ s'identifie — au point de vue de l'homotopie — à l'application canonique $\widehat{G}_{k-1} \to \widehat{G}_k$ déduite de l'injection du sous-groupe $SO(k-1)$ dans $SO(k)$.

Cohomologie de $M(SO(k))$. Pour les dimensions $r > 0$, la cohomologie $H^{*}(M(SO(k)))$ s'identifie à la cohomologie relative $H(\widehat{G}_{k}, \widehat{G}_{k-1})$; on la déterminera grâce à la suite exacte:

$$
\rightarrow H ^ {r} \left(\widehat {G} _ {k}\right) \stackrel {{i ^ {*}}} {{\longrightarrow}} H ^ {r} \left(\widehat {G} _ {k - 1}\right) \stackrel {{\delta^ {*}}} {{\longrightarrow}} H ^ {r + 1} \left(\widehat {G} _ {k}, \widehat {G} _ {k - 1}\right) \longrightarrow H ^ {r + 1} \left(\widehat {G} _ {k}\right) \longrightarrow\tag{2}
$$

où l'homomorphisme $i^{*}$ est bien connu.

Cohomologie mod 2. On sait (cf. [3]) que la cohomologie $H^{*}(\widehat{G}_{k};Z_{2})$ est une algèbre de polynômes engendrée par ($k-1$) générateurs: $W_{2},W_{3},\ldots ,W_{k}$, où $W_{i}$, de degré $i$, est la $i^{\text{ème}}$ classe de Stiefel-Whitney. Il est bien connu que les classes $W_{j}$ s'appliquent l'une sur l'autre par l'homomorphisme $i^{*}$; par suite, la cohomologie relative $H^{*}(\widehat{G}_{k},\widehat{G}_{k-1})$ s'identifie à l'idéal engendré par la classe $W_{k}$ dans l'algèbre de polynômes $H^{*}(\widehat{G}_{k};Z_{2})$. On retrouvera directement ce résultat en considérant, comme au n° 2, l'isomorphisme $\varphi^{*}$.

Cohomologie mod $p, p$ premier $> 2$. Distinguons deux cas:

i) k impair,  $k = 2m + 1$ .  $H^{*}(\widehat{G}_{k}; Z_{p})$  est une algèbre de polynômes engendrée par des générateurs  $P^{4i}$  de dimension divisible par 4 (classes de Pontrjagin, réduites mod p):
 $P^{4}, P^{8}, \ldots, P^{4m}$ .

ii) $k$ pair, $k = 2m'$. $H^{*}(G_{k};Z_{p})$ est une algèbre de polynômes engendrée par les classes de Pontrjagin, réduites mod $p$: $P^{4}, P^{8}, \ldots P^{4m'-4}$ et la «classe fondamentale» $X^{2m'}$.

Dans l'application canonique $\widehat{G}_{k} \to \widehat{G}_{k+1}$, les classes de Pontrjagin $P^{4i}$ s'appliquent l'une sur l'autre, sauf, si $k$ est pair, la classe de dimension maximum de $H^{4m}(\widehat{G}_{k+1})$, $P^{4m}$, qui se trouve appliquée par $i^{*}$ sur le cup-carré $(X^{2m})^{2}$ de la classe fondamentale $X^{2m} \in H^{k}(\widehat{G}_{k})$ (cf. [5]). Il en résulte: si $k$ est pair, $H^{*}(\widehat{G}_{k}, \widehat{G}_{k-1})$ s'identifie à l'idéal engendré par la classe $X^{2m}$ dans $H^{*}(\widehat{G}_{k})$; si $k$ est impair, $H^{*}(M(SO(k))$ s'identifie à une algèbre extérieure de générateur $\delta^{*}(X^{2m'})$.

Cohomologie de $M(O(k))$.

On utilise la même suite exacte que (2), où les $G_{k}$ remplacent les $\widehat{G}_{k}$

Cohomologie mod 2. La cohomologie $H^{*}(G_{k};Z_{2})$ est une algèbre de polynômes, engendrée par $k$ générateurs $W_{1},W_{2},W_{3},\ldots W_{k}$. Comme précédemment, on trouve que $H^{*}(G_{k},G_{k-1};Z_{2})$ s'identifie à l'idéal $\mathfrak{f}$ engendré par la classe $W_{k}$ dans $H^{*}(G_{k};Z_{2})$.

Cohomologie mod $p, p$ premier $> 2$. Soit $g$ le groupe d'automorphismes du revêtement à deux feuilllets $\widehat{G}_k \to G_k$. On vérifie aisément les propriétés suivantes: les classes de Pontrjagin $P^{4i}$ sont invariantes par $g$; par contre, $g$ transforme, si $k$ est pair, la classe fondamentale $X_k$ en son opposée $-X_k$. D'après un résultat classique de la théorie des revêtements (B. Eckmann [9]), il en résulte que: pour $k$ impair, $H^*(G_k; Z_p)$ est isomorphe à $H^*(\widehat{G}_k; Z_p)$; pour $k$ pair $= 2m$, $H^*(G_k; Z_p)$ est une algèbre de polynômes engendrée par les classes de Pontrjagin: $P^4, P^8 \ldots P^{4m-4}$ et le cup-carré $(X_k)^2$ de la classe fondamentale $X_k$; (en effet, si $X_k$ n'est pas invariant par $g$, par contre $(X_k)^2$ l'est).

Usant toujours de la suite exacte analogue à (2), on en déduit:

i) $k$ impair = 2m + 1. Comme $H^{*}(G_{k};Z_{p})$ et $H^{*}(G_{2m};Z_{p})$ sont des algèbres de polynômes isomorphes, et que cet isomorphisme est induit par $i^{*}$ (rappelons que $i^{*}(P^{4m})=(X_{2m})^{2}$), on obtient:

$$
H ^ {r} (G _ {k}, G _ {k - 1}; Z _ {p}) = 0 \text {   pour   tout   } r > 0
$$

ii) $k$ pair = 2m. On trouve immédiatement que $H^{*}(G_{k}; G_{k-1})$ s'identifie à l'idéal engendré par la classe $(X_{2m})^{2}$ dans l'algèbre de polynômes $H^{*}(G_{k}; Z_{p})$.

Groupe fondamental. De façon générale, le groupe fondamental du complexe $M(G)$ s'obtient à partir du groupe fondamental de $A_G$ (ou $B_G$) en annulant ceux des éléments qui sont images par l'injection $E_G \to A_G$ d'éléments de $\pi_1(E_G)$. Ceci nous donnera:

a) comme $\pi_1(\widehat{G}_k) = 0$, on a $\pi_1(M(SO(k))) = 0$.

b) l'homomorphisme $i_*$ applique $\pi_1(G_{k-1}) \simeq Z_2$ sur $\pi_1(G_k) \simeq Z_2$; donc $\pi_1(M(O(k))) = 0$ pour $k \geqslant 1$.

Les complexes $M(O(k))$ et $M(SO(k))$ sont simplement connexes; comme leur premier groupe de cohomologie, de dimension $>0$, est $H^k$, on en déduit que ces espaces sont asphériques jusqu'en dimension $k-1$, incluse. Le premier groupe d'homotopie non nul est $\pi_k(M(O(k))) = Z_2$ et $\pi_k(M(SO(k))) = Z$.

Nous allons maintenant énoncer un théorème de topologie, qui permet de ramener la détermination de l'homotopie d'un espace à des propriétés de cohomologie ; le principe en est dû à J. H. C. Whitehead [29].

Théorème II.6. Soient $X, Y$ deux complexes simplement connexes, et $f$ une application de $X$ dans $Y$, telle que $f$ induit un isomorphisme de $H^{r}(Y)$ sur $H^{r}(X)$ pour $r < k$, et que $f^{*}: H^{k}(Y) \to H^{k}(X)$ est biunivoque, et ceci pour tout corps $Z_{p}$ de coefficients. Dans ces conditions, il existe une application $g$ du $k$-squelette de $Y$ dans $X$, telle que $f \circ g$ et $g \circ f$ (restreintes aux $(k - 1)$-squelettes) sont homotopes à l'identité.

Il en résulte, en particulier, que X et Y ont même k-type : leurs groupes d'homotopie sont isomorphes pour toute dimension  $\leqslant k - 1$ .

On substitue au complexe $Y$ le mapping cylinder $Y'$ de l'application $f$: $Y$ est rétracte par déformation de $Y'$, et lui est homotopiquement équivalent; écrivons la suite exacte:

$$
H ^ {r} (Y ^ {\prime}) \stackrel {f} {\rightarrow} H ^ {r} (X) \rightarrow H ^ {r + 1} (Y ^ {\prime}, X) \rightarrow H ^ {r + 1} (X) \rightarrow H ^ {r + 1} (Y ^ {\prime}).
$$

Les hypothèses faites sur $f$ expriment précisément que $H^{r}(Y', X; Z_{p}) = 0$ pour tout premier $p$ et $r \leqslant k$; par dualité sur le corps $Z_{p}$ des coefficients, on en déduit: $H_{r}(Y', X; Z_{p}) = 0$$r \leqslant k$, et, de là, par la formule des coefficients universels: $H_{r}(Y', X; Z) = 0$, $r \leqslant k$. Puisque $X$ et $Y$ sont simplement connexes, on peut invoquer le théorème d'Hurewicz relatif [15], et en déduire: $\pi_{r}(Y', X) = 0$ pour $r \leqslant k$. On pourra par suite définir une application $g: Y' \to X$, inverse de l'injection $f$, sur le $k$-squelette de $Y'$ telle que $g \circ f \simeq$ identité mod $X^{(k-1)}$ et $f \circ g \simeq$ identité sur $Y'^{k}$, où $X^{(k-1)}$ désigne le $(k - 1)$-squelette de $X$. On a vu plus haut que les groupes de cohomologie $H^{k+i}(M(O(k)))$, resp. $M(SO(k))$, sont indépendants de $k$, tant que $i < k$. Nous allons ici démontrer que la même propriété vaut pour l'homotopie.

Théorème II.7. Les groupes d'homotopie $\pi_{k+i}\left(M(O(k))\right)$ (resp. $M(SO(k))$) sont, pour $i<k$, indépendants de $k$.

Ceci constitue un théorème de suspension, tout-à-fait analogue à celui des sphères.

Soit $A_{O(k-1)}'$ l'espace fibré en $(k-1)$-boules ouvertes sur la grassmannienne $G_{k-1}$; désignons par $A' \otimes I$, le «joint» (au sens de Whitney) de l'espace fibré $A_{O(k-1)}'$ par une structure triviale de dimension 1 (en segments ouverts); il existe une application canonique $i: G_{k-1} \to G_k$, qui induit cet espace fibré $A' \otimes I$ en $k$-boules ouvertes: c'est évidemment l'application $i$ précédemment considérée, déduite de l'injection $O(k-1) \subset O(k)$. Cette application $i$ se relève en une application $f$ de $A' \otimes I$ dans $|A_{O(k)}'$; compactifions $A' \otimes I$ par l'adjonction d'un point «à l'infini» $x$ et soit $X$ l'espace ainsi obtenu. $f$ se prolonge en une application $F: X \to M(O(k))$ et l'homomorphisme $F^*$ induit par $F$

est un isomorphisme de $H^{k+i}(M(O(k)))$ sur $H^{k+i}(X)$ pour tout $i < k - 1$; pour $i = k - 1, F^*$ est biunivoque. Par ailleurs $X$ et $M(O(k))$ sont simplement connexes. On peut donc appliquer le théorème II.6, ce qui montre que les groupes d'homotopie $\pi_{k+i}$ de $X$ et de $M(O(k))$ sont isomorphes pour $i < k - 1$.

Désignons par $T(k - 1)$ le complexe suspension de $M(O(k - 1))$, et soient $p$ et $p'$ les deux pôles de la suspension; désignant toujours par $a$ le point «à l'infini» de $M(O(k))$, soit $g$ l'application qui identifie tout le segment $[pa p']$ en un seul point $x$; le complexe ainsi obtenu n'est autre que $X$; ici encore, $g$ satisfait aux conditions du théorème II.6 (on peut même montrer que $g$ est une homotopie-équivalence); par suite, les groupes d'homotopie de $T(k - 1)$ et de $X$ sont isomorphes.

Or, on a le théorème suivant: soit $K$ un complexe asphérique jusqu'en dimension $n-1$ incluse, $T(K)$ la suspension de $K$; désignons par $E:\pi_{j}(K)\to\pi_{j+1}(T(K))$ l'homomorphisme de Freudenthal; $E$ est un isomorphisme sur pour $j<2n$. (Cf. Blakers-Massey [2]).

La suite des isomorphismes:

$$
\begin{array}{l}\pi_ {k - 1 + i} (M (O (k - 1))) \stackrel {{E}} {{\rightarrow}} \pi_ {k + i} (T (k - 1)) \rightarrow \pi_ {k + i} (X) \simeq \pi_ {k + i} (M (O (k))\\i <   k - 1\end{array}
$$

achève la démonstration du théorème. La démonstration serait tout-à fait analogue pour $M(SO(k))$.

6. Etude du type d'homotopie de $M(O(k))$. Avant d'aborder la détermination des groupes d'homotopie de $M(O(k))$, il est nécessaire de rappeler quelques résultats généraux sur les complexes d'Eilenberg-Mac Lane d'une part, et sur la grassmannienne d'autre part.

Rappel sur les complexes d'Eilenberg-Mac Lane.

Si $\pi$ désigne un groupe abélien, on appelle complexe d'Eilenberg-Mac Lane $K(\pi,n)$ tout espace connexe dont tous les groupes d'homotopie de dimension $>0$ sont nuls, à l'exception de $\pi_n(K(\pi,n)) = \pi$; tous ces espaces ont même type d'homotopie, et il en existe un qui est un complexe simplicial. Si de plus le groupe $\pi$ est de type fini, il existe un complexe $K(\pi,n)$ qui est un complexe simplicial dont le $q$-squelette est un complexe fini. Comme cette propriété n'est pas absolument classique, indiquons en brièvement la démonstration, qui se fait par induction sur l'entier $q$; pour $q = k$, le $k$-squelette de $K(\pi,n)$ se compose d'un nombre fini de sphères $S^k$; soit $K^q$ le $q$-squelette, supposé fini par induction; en vertu des théorèmes de Serre [24], le groupe d'homotopie $\pi_q(K^q)$ est de type fini; on peut l'annuler en adjoignant à $K^q$ un nombre

fini de  $(q+1)$ -cellules, dont les q-sphères bords sont appliquées dans  $K^{q}$  par des applications qu'on peut supposer simpliciales; on obtient ainsi un complexe fini  $K^{q+1}$ , dont tous les groupes  $\pi_{i}(K^{q+1})$  avec  $k<i\leqslant q$ , sont nuls. C'est le  $(q+1)$ -squelette cherché.

On désignera les groupes de cohomologie de $K(\pi, n)$ à coefficients dans $G$ par la notation abrégée $H^{r}(\pi, n; G)$; rappelons que le groupe $H^{n}(G, n; G)$ possède une «classe fondamentale» qu'on notera $\iota$. Pour toute classe de cohomologie $u \in H^{n}(A; G)$ d'un espace $A$, il existe une application $f: A \to K(G, n)$ telle que $u = f^{*}(\iota)$.

La cohomologie des complexes $K(Z, n; Z_p)$ et $K(Z_p, n; Z_p)$ a été déterminée par J. P. Serre et H. Cartan. Rappelons-ici certains de leurs résultats.

Cohomologie de $K(Z_{2}, n)$. (Cf. l'article de J. P. Serre [23].)

La cohomologie $H^{*}(Z_{2}, k; Z_{2})$ est engendrée par des carrés de Steenrod$^{6)}$ de la classe fondamentale $\iota \in H^{k}(Z_{2}, k; Z_{2})$ et par leurs cup-produits; pour $h < k$ (partie stable de $H^{*}(Z_{2}, k; Z_{2})$, le groupe $H^{k+h}(Z_{2}, k; Z_{2})$ est engendré par les carrés itérés $Sq^{i_1} Sq^{i_2} \ldots Sq^{ir}(\iota)$, où $\Sigma_m i_m = h$; une base de ce groupe est donnée par les suites de carrés itérés: $Sq^{i_1} Sq^{i_2} \ldots Sq^{ir}$ avec $i_1 \geqslant 2i_2; i_2 \geqslant 2i_3; i_3 \geqslant 2i_4 \ldots i_{r-1} \geqslant 2i_r$. Une telle suite de $Sq^i$ sera appelée, comme dans [23], suite admissible, et symbolisée par la notation $Sq^I$. Le rang du groupe $H^{k+h}(Z_2, k; Z_2)$, soit $c(h)$, est égal au nombre des partitions de l'entier $h$ (sans considération de l'ordre des termes) en entiers de la forme $2^m - 1$.

On a des résultats sensiblement analogues pour $H(Z, k; Z_2)$.

Cohomologie de $K(Z, k)$ à valeurs dans $Z_p, p > 2$.

Nous utiliserons seulement le résultat suivant de H. Cartan [7]: L'algèbre $H^{*}(Z, k; Z_{p})$ est engendrée par des puissances de Steenrod$^{6)}$ itérées de la classe fondamentale $\iota$.

Rappel sur la grassmannienne $G_{k}$.

On a vu que $H^{*}(G_{k};Z_{2})$ est une algèbre de polynômes engendrée par les $k$ générateurs $W_{i},1\leqslant i\leqslant k$, classes de Stiefel-Whitney. Il est souvent utile de considérer les $W_{i}$ comme fonctions symétriques élémentaires de $k$ variables $t_1,t_2\dots t_k$ de degré 1. Ces variables $t_r$, introduites formellement par Wu Wen-Tsün, ont reçu une interprétation topologique dans la théorie de Borel-Serre [4-5]. L'introduction des variables $t_r$ conduit aux formules de Wu [34], qui donnent les carrés de Steenrod des $W_{i}$:

$$
S q ^ {r} W _ {i} = \Sigma_ {t} \left\{ \begin{array}{c} r - i + t - 1 \\ t \end{array} \right\} W _ {r - t} \cdot W _ {i + t}\tag{3}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{6}$  Pour la définition et les propriétés des carrés et puissances de Steenrod, voir N. E. Steenrod [25].</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">N.</span></small>

Le Lemme suivant, dont je dois la démonstration à J. P. Serre, montre qu'on peut, dans une certaine mesure, substituer la grassmannienne $G_{k}$ au complexe d'Eilenberg-Mac Lane $K(Z_{2}, k)$.

Lemme II.8. Toute combinaison linéaire de $Sq^i$ itérés, de degré total $h \leqslant k$, qui est nulle sur la classe $W_k \in H^k(W_k; Z_2)$, est identiquement nulle.

Observons d'abord que toute classe de la forme $Sq^I(W_k)$ — où la suite $I$ n'est pas nécessairement admissible — est de la forme $W_k \cdot Q_I$, où $Q_I$ est une classe de $H^h(G_k)$, polynôme de poids total $h$ par rapport aux $W_i$. Tout se passe donc dans l'idéal $\mathcal{J}$ engendré par $W_k$ dans $H^*(G_k)$.

Introduisons entre les monômes en $W_{i}$ une relation d'ordre (R) ainsi définie: ordre lexicographique obtenu en posant $W_{m} < W_{n}$ si $m < n$. Par exemple: $W_{4} < W_{4} \cdot (W_{1})^{2} < W_{4} \cdot W_{2} \cdot W_{1} < W_{4} \cdot W_{3}$.

Soit $Sq^I = Sq^{i_1} Sq^{i_2} \ldots Sq^{i_r}$, où les $i_m$ forment une suite admissible ($i_{m-1} \geqslant 2i_m$); formons $Sq^I W_k = W_k \cdot Q_I$. Je dis que $Q_I = W_{i_1} W_{i_2} \ldots W_{i_r} +$ des monômes tous strictement inférieurs pour (R) à $\dot{W}_{i_1} \cdot W_{i_2} \cdot W_{i_3} \ldots W_{i_r}$. Ceci se démontre par récurrence sur l'entier $r$; si $r = 1$, la formule (3) donne, en ce cas: $Sq^i W_k = W_k \cdot W_i$ et $Q_i = W_i$ et rien d'autre. Supposons la propriété établie pour $r - 1$, et considérons:

$Sq^{I} W_{k} = Sq^{i_{1}}(Sq^{i_{2}} \ldots Sq^{ir} W_{k}) = Sq^{i_{1}}(W_{k} \cdot P), \quad \text{ou, par hypothèse, le polynôme } P \text{ est de la forme } W_{i_{2}} \cdot W_{i_{3}} \ldots W_{i_{r}} + \text{des monômes strictement inférieurs. Développons ce produit:}$

$$
S q ^ {i} \left(W _ {k} \cdot P\right) = \sum_ {0 \leqslant m \leqslant i _ {1}} S q ^ {m} (P) \cdot S q ^ {i - m} W _ {k} = \sum_ {0 \leqslant m \leqslant i _ {1}} S q ^ {m} (P) \cdot W _ {i - m} \cdot W _ {k}
$$

Si donc on a posé  $Sq^{I} W_{k} = W_{k} \cdot Q_{I}$ , on obtient:

$$
Q _ {I} = \Sigma_ {0 \leqslant m \leqslant i _ {1}} S q ^ {m} (P) \cdot W _ {i _ {1} - m}
$$

Dans cette somme, $m = 0$ donne $P \cdot W_{i_1} = W_{i_1} \cdot W_{i_2} \ldots W_{i_r} +$ des monômes strictement inférieurs pour (R). Par ailleurs, aucun des termes du développement de $Sq^m(P), m > 0$, ne peut contenir un $W_i$ supérieur ou égal à $W_{i_1}$ pour (R). En effet, d'après la formule (3), $Sq^m W_s$ ne contient que des $W_i$ d'indice $i < 2s$. Il s'ensuit que $Sq^m(P), m > 0$, ne contient que des $W_i$ dont l'indice $i$ vérifie: $i < 2i_2 \leqslant i_1$. C'est dire que tous ces termes sont strictement inférieurs pour (R) à $W_{i_1} \cdot W_{i_2} \ldots W_{i_r}$.

De là on déduit que toutes les classes $Sq^I(W_k)$, lorsque $I$ parcourt l'ensemble des $c(h)$ suites admissibles, de degré total $h$, sont linéaire-

ment indépendantes dans $H^{k+h}(G_k)$; si, en effet, il existait entre ces classes une relation linéaire non triviale, on prendrait, dans cette relation, le terme supérieur pour (R); on en déduirait que ce terme peut s'exprimer linéairement en fonction de termes strictement inférieurs pour (R), ce qui est impossible.

Si l'on revient maintenant à l'interprétation des $W_{i}$ comme fonctions symétriques de $k$ variables $t_{m}$ de degré 1, le lemme précédent prend la forme:

Lemme II.8.' Les classes $Sq^I(t_1 t_2 \ldots t_k)$, où $I$ parcourt l'ensemble des suites admissibles de degré total $h \leqslant k$, sont des fonctions symétriques des $t_i$ linéairement indépendantes.

On a vu que la cohomologie $H^{*}(M(O(k)) ; Z_{2})$ s'identifie à l'idéal $\mathcal{F}$ engendré par la classe $W_{k}$ dans $H^{*}(G_{k} ; Z_{2})$; or, par l'introduction des $k$ variables $t_{i}$, on obtient une base du groupe $H^{h}(G_{k})$ en formant tous les monômes symétrisés:

$$
\Sigma (t _ {1}) ^ {a _ {1}} (t _ {2}) ^ {a _ {2}} \dots (t _ {r}) ^ {a _ {r}}\tag{4}
$$

où les entiers $a_{i}$ constituent une partition de l'entier $h$, et où on fait pour la symétrisation $\Sigma$ la convention classique: on ne prend du groupe symétrique total à $k$ variables que les permutations «essentielles» pour le monôme (4), c'est-à-dire un système de représentants des classes du groupe symétrique modulo le sous-groupe qui laisse invariant le monôme (4); par exemple:

$$
\Sigma (t _ {1}) (t _ {2}) \dots (t _ {k}) = t _ {1} \cdot t _ {2} \cdot \dots t _ {k}.
$$

Si $h = \Sigma_i a_i$ est une partition $(\omega)$ de $h$, et (4) le monôme associé, on désignera par $\mathfrak{S}_{\omega}$ un système de permutations essentielles pour (4); toutes les fois que le signe $\Sigma$ apparait, dans les calculs, devant un monôme tel que (4), la sommation doit s'effectuer suivant un système de permutations essentielles, sauf convention contraire explicitement énoncée.

On obtiendra une base pour la dimension  $(k + h)$  de l'idéal J en multipliant par  $W_{k} = t_{1} \cdot t_{2} \cdot \ldots \cdot t_{k}$  les éléments de la base (4); on obtient ainsi tous les monômes symétrisés:

$$
\Sigma (t _ {1}) ^ {a _ {1} + 1} (t _ {2}) ^ {a _ {2} + 1} \dots (t _ {r}) ^ {a _ {r} + 1} t _ {r + 1} \dots t _ {k}.\tag{5}
$$

En effet, toute permutation essentielle pour le monôme (4) est essentielle pour le monôme (5), et réciproquement.

Définition. Soit $P$ un polynôme par rapport aux variables $t_{i}$; on dira que la variable $t_{n}$ est une variable dyadique du polynôme $P$, si

$t_{n}$ figure dans tous les monômes de P sous un exposant nul ou de la forme $2^{m}$.

Lemme II.9. Si $t_n$ est une variable dyadique du polynome $P$, $t_n$ est également variable dyadique du polynome $Sq^i P$.

On sait, en effet, que $S q^{a}(t_{n})^{m} = \begin{bmatrix} m \\ a \end{bmatrix} (t_{n})^{m + a}$.

Or, si $m$ est non nul, et est une puissance de 2, le coefficient binomial $\begin{bmatrix} m \\ a \end{bmatrix}$ est nul, sauf pour $a = 0$ ou $a = m$; (en effet, $\begin{bmatrix} p \\ q \end{bmatrix} = 1 \mod 2$, si et seulement si le développement dyadique de $p$ contient celui de $q$, cf. Whitehead-Steenrod [26]). Dans ces conditions, le nouvel exposant $m + a$ est encore une puissance de 2.

Définition. Dans un monôme $(t_1)^{a_1}(t_2)^{a_2} \ldots (t_r)^{a_r}$, appelons facteur non dyadique, le sous-monôme constitué de toutes les variables qui ne sont pas dyadiques; on désignera par $u$ le nombre de ces variables, par $v$ leur degré total. On introduit entre monômes en $(t_i)$ une relation de préordre $(Q)$ ainsi définie: le monôme $X$ est dit supérieur au monôme $Y$ pour $(Q)$, si $u(X) > u(Y)$, et, si pour $u(X) = u(Y)$, on a $v(X) < v(Y)$. Cela étant, pour tout $h \leqslant k$, formons les classes:

$$
X _ {\omega} ^ {h} = \sum (t _ {1}) ^ {a _ {1} + 1} (t _ {2}) ^ {a _ {2} + 1} \dots (t _ {r}) ^ {a _ {r} + 1} \cdot t _ {r + 1} \dots t _ {k}\tag{6}
$$

où $\omega = \{a_{1}a_{2}\ldots a_{r}\}$ parcourt l'ensemble des partitions de l'entier $h$ en entiers dont aucun n'est de la forme $2^{m} - 1$ (partitions non dyadiques de $h$); on désignera par $d(h)$ le nombre de ces partitions.

Pour toute dimension $m \leqslant h$, formons les classes:

$$
X _ {\omega} ^ {m}, S q ^ {1} X _ {\omega} ^ {m - 1}, S q ^ {2} X _ {\omega} ^ {m - 2}, \dots , S q ^ {I h} X _ {\omega h} ^ {h} \dots S q ^ {I} W _ {k}\tag{7}
$$

où les $Sq^{Ih}$ parcourent toutes les suites admissibles de carrés itérés de degré total $(m - h)$, et où $\omega_h$ parcourt l'ensemble des $d(h)$ partitions non-dyadiques de $h$, définies en (6).

Je dis que toutes les classes du tableau (7) sont linéairement indépendantes.

En effet, prenons dans chacun des développements de $Sq^I X_\omega^h$, ceux des monômes qui sont supérieurs pour (Q) ; je dis qu'ils forment le développement de:

$$
\sum_ {\mathfrak {S} _ {\omega}} \left(t _ {1}\right) ^ {a _ {1} + 1} \left(t _ {2}\right) ^ {a _ {2} + 1} \dots \left(t _ {r}\right) ^ {a _ {r} + 1} \cdot S q ^ {I} \left(t _ {r + 1} \dots t _ {k}\right)\tag{8}
$$

où la sommation $\Sigma$ a lieu suivant le système $\mathfrak{S}_{\omega}$ des permutations essen-

tielles pour le monôme (6) associé à la partition $\omega$. En effet, tout monôme du développement de:

$$
S q ^ {I} (t _ {1}) ^ {a _ {1} + 1} (t _ {2}) ^ {a _ {2} + 1} \dots (t _ {r}) ^ {a _ {r} + 1} \cdot t _ {r + 1} \dots t _ {k}
$$

est nécessairement d'indice $u \leqslant r$, car, d'après le Lemme II.9, les variables $(t_{r+1}, \ldots, t_k)$ sont des variables dyadiques; si l'on a $u = r$, deux cas sont possibles: ou le monôme provient du développement de:

$$
\left(t _ {1}\right) ^ {a _ {1} + 1} \left(t _ {2}\right) ^ {a _ {2} + 1} \dots \left(t _ {r}\right) ^ {a _ {r} + 1} \cdot S q ^ {I} \left(t _ {r + 1} \dots t _ {k}\right)\tag{9}
$$

et alors $v = u + h$, ou il appartient à un terme provenant par carrés successifs du facteur non dyadique $(t_1)^{a_1+1}(t_2)^{a_2+1} \ldots (t_r)^{a_r+1}$, et, en ce cas, l'indice $v$ est nécessairement strictement plus grand que $r + h$; c'est dire que les termes de (9) sont tous supérieurs pour $(Q)$ à tout autre terme du développement de $Sq^I X_\omega^h$. D'autre part, le terme (9) ne peut disparaître du fait de la symétrisation effectuée en (8). En effet, toute permutation des $t_i$ essentielle pour le monôme (6) est essentielle pour son facteur non-dyadique $(t_1)^{a_1+1}(t_2)^{a_2+1} \ldots (t_r)^{a_r+1}$, qui est aussi le facteur non-dyadique du terme (9); donc, les transformés de (9) par des permutations de $\mathfrak{S}_\omega$ contiennent des facteurs non-dyadiques tous différents, et leur somme ne peut être nulle, si (9) n'est pas nulle.

Comme un terme ne peut s'exprimer en fonction linéaire de termes qui lui sont strictement inférieurs pour la relation  $(Q)$ , il en résulte que les seules combinaisons linéaires non triviales entre classes de (7) ne peuvent contenir que des classes  $Sq^{I}X_{\omega}^{h}$ , dont les termes supérieurs pour  $(Q)$  ont même indice u = r, et même indice  $v = r + h$ , donc même valeur pour h; de plus les partitions  $\omega$  de h figurant dans les  $X_{\omega}^{h}$  de cette relation ne peuvent être différentes, car alors les termes supérieurs pour  $(Q)$  des développements des  $Sq^{I}X_{\omega}^{h}$  ont des facteurs non-dyadiques tous différents, et leur somme ne peut être nulle. Reste donc comme seule possibilité une relation linéaire de la forme  $\Sigma_{\lambda}c_{\lambda}Sq^{I\lambda}X_{\omega}^{h}=0$ , relative à une seule classe  $X_{\omega}^{h}$ .

Ecrivons les termes supérieurs pour  $(Q)$  de cette relation:

$$
\sum_ {\lambda} c _ {\lambda} \left(t _ {1}\right) ^ {a _ {1} + 1} \left(t _ {2}\right) ^ {a _ {2} + 1} \dots \left(t _ {r}\right) ^ {a _ {r} + 1} S q ^ {I _ {\lambda}} \left(t _ {r + 1} \dots t _ {k}\right) = 0.
$$

Extrayons de cette somme tous les termes contenant le monôme $(t_1)^{a_1 + 1}(t_2)^{a_2 + 1}\ldots (t_r)^{a_r + 1}$ en facteur ; si l'on fixe ce facteur non-dyadique, $\mathfrak{S}_{\omega}$ se réduit à l'identité, et il reste :

$$
\left(t _ {1}\right) ^ {a _ {1} + 1} \cdot \left(t _ {2}\right) ^ {a _ {2} + 1} \dots \left(t _ {r}\right) ^ {a _ {r} + 1} \sum_ {\lambda} c _ {\lambda} S q ^ {I \lambda} \left(t _ {r + 1} \dots t _ {k}\right) = 0.
$$

Mais on a vu, d'après le Lemme II. 8', que toutes les classes

$Sq^{I}(t_{r+1} \ldots t_{k})$ sont linéairement indépendantes, pourvu que $m - h$, degré de $I, \leqslant k - r$. Mais on a évidemment $h \geqslant 2r$, de sorte que cette inégalité est satisfaite pour tout $m \leqslant k$. Donc les constantes $c_{\lambda}$ sont nulles, et il n'existe entre les classes du tableau (7) aucune relation linéaire non triviale.

Le rang de $H^{k+m}(M(O(k)))$, ou rang de l'idéal $\mathcal{J}$, est égal à $p(m)$, nombre total de partitions de l'entier $m$. Or les classes du tableau (7) sont en nombre égal à $\Sigma_{h\leqslant m}c(m-h)d(h)$.

Il est aisé de vérifier l'égalité:

$$
p (m) = \Sigma_ {h \leqslant m} c (m - h) d (h).
$$

En effet, à toute partition de $m$, on peut associer un couple de deux partitions: l'une de $(m - h)$, constituée uniquement des entiers de la forme $2^{n} - 1$; l'autre de $h$, formée des autres entiers. Il en résulte que les classes du tableau (7) constituent une base de $H^{k+m}(M(O(k)))$.

Associons à chaque classe  $X_{\omega}^{h}$  une application

$$
F _ {\omega}: M (O (k)) \rightarrow K (Z _ {2}, k + h),
$$

telle que, si $F_{\omega}^{*}$ désigne l'homomorphisme induit, on ait: $F_{\omega}^{*}(\iota) = X_{\omega}^{h}$; l'ensemble des $F_{\omega}$ définit une application $F$ de $M(O(k))$ dans le produit:

$$
\begin{array}{l} Y = K (Z _ {2}, k) \times K (Z _ {2}, k + 2) \times \dots (K (Z _ {2}, k + h)) ^ {d (h)} \\ + \dots (K (Z _ {2}, 2 k)) ^ {d (k)} \end{array}\tag{10}
$$

Dire que les classes de (7) forment une base de $H^{k+h}(M(O(k)))$, c'est dire que l'homomorphisme $F^*$ induit par $F$ est un isomorphisme de $H^{k+m}(Y;Z_2)$ sur $H^{k+m}(M(O(k)))$ pour tout $m \leqslant k$. En coefficients mod $p, p > 2$, la cohomologie de $Y$ est nulle, celle de $M(O(k))$ est nulle pour toute dimension $< 2k$; $F^*$ est donc ici encore un isomorphisme sur pour toute dimension $< 2k$, et est biunivoque pour la dimension $2k$. On pourra donc appliquer aux espaces $M(O(k))$ et $Y$ le théorème II.6. Cela nous donnera:

Il existe une application inverse g du 2k-squelette de Y dans  $M(O(k))$  telle que  $g \circ F = identité sur le (2k - 1)$ -squelette de  $M(O(k))$ . Donc:

Théorème II.10. L'espace $M(O(k))$ a même 2k-type d'homotopie que le produit Y de complexes d'Eilenberg-Mac Lane défini en (10).

Corollaire II.11. Le groupe d'homotopie stable $\pi_{k+h}\left(M(O(k))\right)$, $h < k$ est isomorphe à la somme directe de $d(h)$ groupes $Z_2$.

En prenant la restriction de l'application inverse g au premier facteur de Y, on obtient:

Corollaire II.12. Il existe une application g du 2k-squelette de  $K(Z_{2}, k)$  dans  $M(O(k))$ , telle que  $g^{*}(U) = \iota$ , classe fondamentale de  $K(Z_{2}, k)$ .

Comme toute classe $u \in H^{k}(A;Z_{2})$ d'un espace $A$ est l'image de la classe fondamentale $\iota$ dans une application $f: A \to K(Z_{2}, k)$, on obtient:

Corollaire II.13. Toute classe de cohomologie mod 2 de dimension k d'un espace de dimension $\leqslant 2k$, admet une réalisation orthogonale.

## 7. Etude de  $M(O(k))$  pour les petites valeurs de k.

k = 1. L'espace des 1-vecteurs non orientés n'est autre que l'espace projectif réel de très grande dimension  $PR(N)$ ; l'espace fibré universel associé  $A_{O(1)}$  n'est autre que le «mapping cylinder» du revêtement à deux feuilllets  $S^{N} \to PR(N)$ ; si, dans ce complexe  $A_{O(1)}$ , on identifie en un point la sphère-bord  $S^{N}$ , on obtient pour complexe  $M(O(1))$  l'espace projectif réel  $PR(N + 1)$ ; ici, les complexes  $K(Z_{2}, 1)$  et  $M(O(1))$  sont tous deux réalisés par l'espace projectif réel de grande dimension  $PR(\infty)$ , et toute classe de cohomologie mod 2, de dimension 1, admet une réalisation orthogonale.

$k = 2$. La cohomologie de $MO(2)$ admet la description suivante:

En dimensions 2, la classe fondamentale U, définie mod 2.

En dimension 3, la classe entière $Sq^{1}U = U\cdot W_{1}$.

En dimension 4, une classe entière X — cup-carré de la classe fondamen-

tale de  $M(SO(2))$  — dont la réduction mod 2 est  $U^{2}$ .

et une classe mod 2, définie par $U \cdot (W_1)^2$.

En dimension 5, une classe entière d'ordre 2, $Sq^{1}(U \cdot (W_{1})^{2})$

$$
= U \cdot (W _ {1}) ^ {3}
$$

et une classe mod 2 $U^{2} \cdot W_{1}$.

Dans l'application canonique $F: M(O(2)) \to K(Z_{2}, 2)$, on a, en coefficients mod 2:

$$
\begin{array}{c} F ^ {*} (\iota) = U; F ^ {*} (S q ^ {1} \iota) = U \cdot W _ {1}; F ^ {*} (S q ^ {2} \iota) = U ^ {2}; F ^ {*} (S q ^ {2} S q ^ {1} \iota) \\ = S q ^ {2} (U \cdot W _ {1}) = U ^ {2} \cdot W _ {1} + U \cdot (W _ {1}) ^ {3}; F ^ {*} (\iota \cdot S q ^ {1} \iota) = U ^ {2} \cdot W _ {1}. \end{array}
$$

On considère, comme pour le théorème II.6, le «mapping cylinder» de l'application F, qu'on notera encore K; K contient  $M(O(2))$  -noté M

pour simplifier — comme sous-ensemble fermé. La suite exacte associée à l'injection  $F: M \to K$ , donne alors:

$H^{r}(K,M;Z_{p}) = 0;r <   5;H^{5}(K,M;Z_{p}) = Z_{p}$ pour tout premier $p$

On en déduit, par dualité:

$H_{r}(K,M;Z_{p}) = 0,r <   5;H_{5}(K,M;Z_{p}) = Z_{p}$ pour tout premier $p$

La formule des coefficients universels donne alors :

$$
H _ {r} (K, M; Z) = 0, r <   5; H _ {5} (K, M; Z) = Z.
$$

Par application du théorème d'Hurewicz relatif, on obtient: $\pi_{4}K, M) = 0$;

$$
\pi_ {5} (K, M) = Z, \quad \mathrm{d} ^ {\prime} \text { o   u } \quad \pi_ {3} (M) = 0, \pi_ {4} (M) = Z.
$$

Si l'on cherche à former une application $G$ inverse de $F$ au point de vue de l'homotopie, on pourra définir $G$ sur le 4-squelette de $K$; mais le prolongement de $G$ au 5-squelette de $K(Z_{2}, 2)$ est interdit par une obstruction, à valeurs dans $\pi_{4}(M) = Z$. Conformément à la théorie générale de la seconde obstruction [14], cette classe-obstruction de $H^{5}(Z_{2}, 2; Z)$ n'est autre que l'invariant d'Eilenberg-Mac Lane associé au second groupe d'homotopie non nul $\pi_{4}(M)$; elle engendre le noyau de l'homomorphisme $F^{*}: H^{5}(Z_{2}, 2; Z) \to H^{5}(M; Z)$.

Déterminons cet homomorphisme: le groupe $H^5(Z_2, 2; Z)$ est cyclique d'ordre 4 ; il est engendré par l'élément $(\frac{1}{4}) \delta p(\iota)$, image par l'homomorphisme de Bockstein $\frac{1}{4} \cdot \delta$ du carré de Pontrjagin $p(\iota)$ de la classe fondamentale $\iota$. Le groupe $H^5(M; Z)$ est cyclique d'ordre 2, et il est engendré par la classe $Sq^1(U \cdot (W_1)^2)$, dont la réduction mod 2 est $U \cdot (W_1)^3$. Par l'homomorphisme $F^*$, le générateur du premier groupe est appliqué sur le générateur du second. Il suffit évidemment de le vérifier sur leurs réductions mod 2. Calculons $(\frac{1}{4}) \delta p(\iota)$, réduit mod 2 ; soit $u$ un cocycle de la classe $\iota, v = (\frac{1}{2}) \delta(u)$ un cocycle de la classe $Sq^1\iota$. L'expression du carré de Pontrjagin est: $p(u) = u \cup u + u \cup_1 \delta u$, d'où, par application de la formule du cobord:

$$
\delta \boldsymbol {p} (u) = \delta u \cup u + u \cup \delta u + \delta u \cup_ {1} \delta u + u \cup \delta u - \delta u \cup^ {*} u
$$

d'où, après division par 4:

$$
\begin{array}{r l} \frac {1}{4} \cdot \delta p (u) & = u \cup v + v \cup_ {1} v; \quad \text { réduisons   mod } 2 \\ & = \iota \cdot S q ^ {1} \iota + S q ^ {2} S q ^ {1} \iota . \end{array}
$$

44

L'image par $F^{*}$ de la classe précédente est:

$$
U ^ {2} \cdot W _ {1} + U ^ {2} \cdot W _ {1} + U \cdot (W _ {1}) ^ {3} = U \cdot (W _ {1}) ^ {3}
$$

qui est bien le générateur de  $H^{5}(M;Z)$ , réduit mod 2.

Comme cette classe est d'ordre 2, la classe $(\frac{1}{2})\delta p(t)$ est appliquée par $F^{*}$ sur 0; c'est l'obstruction cherchée. (On observera que cette classe est d'ordre 2, mais sa réduction mod 2 est nulle, ce qui explique qu'on ne puisse l'exprimer à l'aide de $Sq^{i}$.) On obtient ainsi:

Théorème II.14. Pour qu'une classe $x \in H^2(A; Z_2)$ d'un espace $A$ de dimension 5 admette une réalisation orthogonale, il faut et il suffit que la classe $(\frac{1}{2}) \cdot \delta p(x)$ soit nulle, ou $p(x)$ désigne le carré de Pontrjagin de la classe $x$.

Une condition nécessaire pour qu'il en soit ainsi est qu'il existe une classe  $X \in H^{4}(A; Z_{2})$ , telle que  $Sq^{2}Sq^{1}x + x \cdot Sq^{1}x = Sq^{1}X$ .

k = 3. On compare  $M(O(3))$  au produit Y de complexes d'Eilenberg-Mac Lane défini au théorème général II.10. On constate que  $F^{*}$  est un isomorphisme pour les cohomologies, non seulement jusqu'en dimension 6, mais encore en dimension 7; par contre, l'isomorphisme est rompu en dimension 8. Voici le détail des calculs:

En dimension 3: $F^{*}(\iota) = U$.

En dimension 4: $F^{*}(Sq^{1}\iota) = U\cdot W_{1}$.

En dimension 5: $F^{*}(Sq^{2}\iota) = U\cdot W_{2}$ et $F^{*}(X^{2}) = U\cdot (W_{1})^{2}$ (nouveau générateur).

En dimension 6: $F^{*}(Sq^{3}\iota) = U^{2};F^{*}(Sq^{2}Sq^{1}\iota) = U\cdot (W_{2}W_{1} + (W_{1})^{3});$

$$
F ^ {*} (S q ^ {1} X ^ {2}) = U \cdot (W _ {1}) ^ {3}.
$$

En dimension 7: $F^{*}(\iota \cdot Sq^{1}\iota) = U^{2} \cdot W_{1}$;

$$
F ^ {*} (S q ^ {2} X ^ {2}) = U \cdot (W _ {2} \cdot (W _ {1}) ^ {2} + (W _ {1}) ^ {4}).
$$

On a en dimension 7 deux nouveaux générateurs $F^{*}(X^{4}) = U \cdot (W_{1})^{4}$ et $F^{*}(X^{22}) = U \cdot (W_{2})^{2}$; en dimension 8, l'isomorphisme n'a plus lieu à cause de la relation: $F^{*}(Sq^{3}X^{2} + (Sq^{1}\iota)^{2} + Sq^{1}X^{4}) = 0$. Nous pouvons donc affirmer (Th. II. 6):

Théorème II.15. Toute classe de cohomologie de dimension 3, à coefficients dans $Z_2$, d'un espace de dimension $< 8$ admet une réalisation orthogonale.

Remarque. J'ignore quelle est l'obstruction en dimension 8, qui est d'ailleurs peut-être nulle.

Terminons par une remarque générale : une application

$$
g: K (Z _ {2}, k) \rightarrow M (O (k))
$$

homotopiquement inverse de $F: M(O(k)) \to K(Z_2, k)$ ne peut exister, pour $k > 1$; en effet, comme me l'a fait remarquer J. P. Serre, la cohomologie de $K(Z_2, k)$ est, pour $k > 1$, une algèbre de polynômes à une infinité de générateurs; au contraire, la cohomologie de $M(O(k))$, est — à un décalage dans la graduation près — isomorphe à celle de la grassmannienne $G_k$, donc de type fini. Pour une dimension assez élevée, le rang de $H^*(Z_2, k)$ finit par excéder celui de $H^*(M(O(k)))$, et le noyau de $F^*$ n'est pas nul, ce qui montre l'inexistence de l'application $g$. Donc, pour toute dimension $k > 1$, il existe des classes de cohomologie mod 2 qui, dans des espaces de dimension assez élevée $> 2k$, n'admettent pas de réalisation orthogonale.

8. Etude de $M(SO(k))$; cas stable. Nous avons pu, au n° 6, donner une description explicite du type d'homotopie «stable» de $M(O(k))$; nous ne pourrons en faire autant pour $M(SO(k))$; en effet, le type d'homotopie de ce dernier complexe est beaucoup plus compliqué, en raison notamment du fait suivant: pour $M(O(k))$, le complexe Y équivalent était un produit topologique de complexes $K(Z_2, k)$; au contraire, pour $M(SO(k))$, le complexe équivalent n'est plus un produit, mais un espace fibré multiple, dont les fibres successives sont des $K(Z_2, r)$ ou des $K(Z, m)$ (peut-être même des $K(Z_p, n)!$), et où les fibrations successives sont en général non triviales. Aussi nous bornerons nous à ne donner la description du complexe équivalent que pour les dimensions $k + i$, où $i \leqslant 7$.

Définition du complexe «de Zilber» K. On sait que le complexe  $K(Z, k + 4)$  est fibre d'un espace asphérique A, dont la base est le complexe  $K(Z, k + 5)$  (cf. J. P. Serre [24]). Soit u la classe fondamentale du complexe base  $K(Z, k + 5)$ ; il existe une application f du complexe  $K(Z, k)$  dans  $K(Z, k + 5)$ , telle que  $f^{*}(u) = St_{3}^{5}(\iota)$ , où  $St_{3}^{5}$  désigne le «cube de Steenrod» de dimension 5, qui définit une classe entière d'ordre 3. On désignera par K l'espace induit de l'espace fibré A par l'application f; K est ainsi fibré sur  $K(Z, k)$ , de fibre  $K(Z, k + 4)$ ; les seuls groupes d'homotopie non nuls de K sont  $\pi_{k}$  et  $\pi_{k+4}$ , tous deux isomorphes à Z; l'invariant d'Eilenberg-Mac Lane  $k \in H^{k+5}(Z, k; Z)$  associé n'est autre que  $St_{3}^{5}(\iota)$ ; pour qu'une application F d'un espace M dans K, définie sur le  $(k + 4)$ -squelette de M, puisse être prolongée à tout M, il faut et il suffit que le cube  $St_{3}^{5}$  de la classe x image par  $F^{*}$  de la classe  $\iota$  soit nul.

Cohomologie du complexe K.

1. Cohomologie mod 2. Désignons par $F^3$ l'application de $K(Z, k)$ dans lui-même, telle que $(F^3)^*(\iota) = 3\iota$. L'espace fibré induit de $K$ par cette application n'est autre que le produit $K(Z, k) \times K(Z, k + 4)$, car son invariant d'Eilenberg-Mac Lane n'est autre que $(F^3)^*(St_3^5(\iota)) = St_3^5(F^3(\iota)) = St_3^5(3\iota) = 0$. Il existe donc une application $G$ du produit $K(Z, k) \times K(Z, k + 4)$ dans $K$, compatible avec la fibration en complexes $K(Z, k + 4)$, et qui se projette sur les bases $K(Z, k)$ suivant l'application $F^3$.

G induit un homomorphisme de la suite spectrale de cohomologie relative à la fibration de K dans celle — triviale — relative au produit  $K(Z, k) \times K(Z, k + 4)^{7}$ .

$G^{*}$ est un isomorphisme pour les termes $E^{2}$ de ces suite spectrales; si l'on remarque que $(F^{3})^{*}$ est un isomorphisme pour $H^{*}(Z, k; Z_{2})$, on en déduit que la différentielle de Leray $d_{2}$ du terme $E^{2}$ de la fibration de $K$ est nulle, car elle est nulle dans le produit; de même pour toutes les $d_{i}$ successives, et ceci démontre: la cohomologie $H^{*}(K; Z_{2})$ est isomorphe à celle du produit $K(Z, k) \times K(Z, k + 4)$.

2. Cohomologie mod $p, p$ premier $\geqslant 5$. Le même raisonnement que plus haut conduit à la même conclusion: $H^{*}(K; Z_{p})$ est isomorphe à la cohomologie du produit $K(Z, k) \times K(Z, k + 4)$.

3. Cohomologie mod 3. Il est ici nécessaire d'expliciter un fragment de la suite spectrale relative à la fibration de $K$ sur $K(Z, k)$; désignons par $v$ la classe fondamentale du complexe fibre $K(Z, k + 4)$. Par construction même de $K$, $v$ s'envoie par transgression (ici par la différentielle $d_5$) sur la classe $St_3^5(\iota)$; comme les puissances de Steenrod commutent à la transgression, la classe fibre $St_3^4 v$ s'envoie sur $St_3^4 \circ St_3^5(\iota) = St^9(\iota)$ (à un coefficient non nul près). Il en résulte que la cohomologie $H^*(K; Z_3)$ admet les générateurs suivants: en dimension $k$, un générateur, qui provient de $\iota$ (et qu'on désignera encore, bien qu'indûement, par $\iota$); en dimension $k + 4$, la classe $St_3^4(\iota)$; en dimension $k + 8$, la classe $St_3^8(\iota)$; en dimension $k + 9$, on aura un élément provenant de $St_3^5 v$, qui se trouve appliqué par transgression sur $St_3^5 \circ St_3^5(\iota) = 0$. Mais nous ne nous en préoccuperons pas.

Le complexe équivalent à $M(SO(k))$. Ce sera le produit $Y$ du com-

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">7) Pour la définition et les propriétés de la suite spectrale associée à une fibration, on se reportera aux articles de J. Leray (J. Math. pures et appl., 29, 1950; pp. 1—139 et 169—213) ainsi qu'à J. P. Serre [24].</span></small>

plexe $K$ défini plus haut par un complexe d'Eilenberg-Mac Lane $K(Z_{2}, k + 5)$. Définissons maintenant l'application $F: M(SO(k)) \to Y$. Il existe une application $f$ du $(k + 4)$-squelette de $M(SO(k))$ dans $K$, telle que $f^{*}(\iota) = U$; comme $St_{3}^{5}U = 0$ (parce que $M(SO(k))$, comme $\widehat{G}_{k}$, n'a pas de co-torsion d'ordre 3), l'application

$$
f: M (S O (k)) \rightarrow K
$$

se prolonge à tout le complexe $M(SO(k))$; par ailleurs, il existe une application $g: M(SO(k)) \to K(Z_2, k + 5)$, telle que si $\iota'$ désigne la classe fondamentale de ce complexe, on ait: $g^*(\iota') = U \cdot W_2 W_3$. L'ensemble des applications $f$ et $g$ définit l'application $F: M(SO(k)) \to Y$ cherchée.

Calculons l'homomorphisme $F^{*}$ induit par $F$, suivant les coefficients:

Calcul mod 2. On considère les dimensions $k + i$, où $0 \leqslant i \leqslant 8$.

On désigne ici encore par v le générateur du facteur  $K(Z, k + 4)$  dans K, définie dans l'isomorphisme

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$H^{*}(K;Z_{2})\approx H^{*}(Z,k;Z)\otimes H^{*}(Z,k + 4;Z_{2}).$ $i = 0;F^{*}(\iota) = U.$ $i = 1;F^{*}(0) = 0.$ $i = 2;F^{*}(Sq^{2}\iota) = U\cdot W_{2}.$ $i = 3;F^{*}(Sq^{3}\iota) = U\cdot W_{3}.$ $i = 4;F^{*}(Sq^{4}\iota) = U\cdot W_{4}.$ $F^{*}(v) = U\cdot (W_{2})^{2}.$ $i = 5;F^{*}(Sq^{5}\iota) = U\cdot W_{5}.$ $F^{*}(\iota^{\prime}) = U\cdot W_{2}W_{3}.$ $i = 6;F^{*}(Sq^{6}\iota) = U\cdot W_{6};$ $F^{*}(Sq^{4}Sq^{2}\iota) = U\cdot (W_{2}W_{4} + (W_{3})^{2} + (W_{2})^{3}).$ $F^{*}(Sq^{2}v) = U\cdot ((W_{2})^{3} + (W_{3})^{2}).$ $F^{*}(Sq^{1}\iota^{\prime}) = U\cdot (W_{3})^{2}.$ $i = 7;F^{*}(Sq^{7}\iota) = U\cdot W_{7};$ $F^{*}(Sq^{5}Sq^{2}\iota) = U\cdot (W_{5}W_{2} + W_{4}W_{3} + W_{3}(W_{2})^{2}).$ $F^{*}(Sq^{3}v) = U\cdot W_{3}(W_{2})^{2}.$ $F^{*}(Sq^{2}\iota^{\prime}) = U\cdot W_{2}(W_{5} + W_{3}W_{2}).$ $i = 8;F^{*}(Sq^{8}\iota) = U\cdot W_{8};$ $F^{*}(Sq^{6}Sq^{2}\iota) = U\cdot (W_{6}W_{2} + W_{5}W_{3} + W_{4}\cdot (W_{2})^{2}).$ $F^{*}(Sq^{4}v) = U\cdot (W_{4}(W_{2})^{2} + W_{2}(W_{3})^{2} + (W_{2})^{4}).$ $F^{*}(Sq^{3}\iota^{\prime}) = U\cdot W_{5}W_{3};F^{*}(Sq^{2}Sq^{1}\iota^{\prime}) = U\cdot W_{2}(W_{3})^{2}.$
</div>

On vérifie que, pour tout $i \leqslant 8$, les classes de $H^{*}(M(SO(k);Z_{2}))$ figurant dans ce tableau sont linéairement indépendantes; de plus, pour $i \leqslant 7$, les classes écrites forment une base pour $H^{k+i}(M(SO(k);Z_{2}))$; donc, $F^{*}$ est un isomorphisme de $H^{k+i}(Y)$ sur $H^{k+i}(M(SO(k)))$ pour $i \leqslant 7$, et est biunivoque pour $i = 8$.

Remarque. On a utilisé dans ce calcul la forme canonique des générateurs de $H^{*}(Z, k; Z_{2})$ donnée par J. P. Serre [23]; il est clair qu'on pourrait continuer le calcul plus loin, en introduisant deux générateurs nouveaux en dim 8 correspondant aux classes («de Pontrjagin») $(W_{2})^{4}$ et $(W_{4})^{2}$.

Calcul mod 3. Le facteur $K(Z_2, k + 5)$ ne donne rien ; on a seulement :

$$
i = 0; F ^ {*} (\iota) = U; i = 4, F ^ {*} (S t ^ {4} \iota) = U \cdot P _ {4}; i = 8; F ^ {*} (S t _ {3} ^ {8} \iota)
$$

$$
= U \cdot ((P _ {4}) ^ {2} + 2 P _ {8}).
$$

Calcul mod $p; p = 5$

$$
i = 0; F ^ {*} (\iota) = U; F ^ {*} (v) = U \cdot P _ {4}; F ^ {*} \left(S t _ {5} ^ {8} \iota\right) = U \cdot \left(\left(P _ {4}\right) ^ {2} - 2 P _ {8}\right) ^ {8})
$$

Calcul mod $p; p > 5$.

$$
i = 0; F ^ {*} (t) = U; i = 4, F ^ {*} (v) = U \cdot P _ {4}; i = 8, F ^ {*} (0) = 0.
$$

Il en résulte que pour tout corps de coefficients, $F^*$ est un isomorphisme de $H^{k+i}(Y)$ sur $H^{k+i}(M(SO(k)))$ pour $i \leqslant 7$, et $F^*$ est biunivoque pour $i = 8$. Comme $Y$ et $M(SO(k))$ sont simplement connexes, on peut appliquer le théorème II.6, ce qui montre que $M(SO(k))$ a même $(k + 8)$-type que $Y$. Donc:

Théorème II.16. Les groupes d'homotopie stables $\pi_{k+i}(M(SO(k)))$ sont pour $i \leqslant 7$; $\pi_{k+1} = \pi_{k+2} = \pi_{k+3} = 0$; $\pi_{k+4} = Z$; $\pi_{k+5} = Z_2$; $\pi_{k+6} = \pi_{k+7} = 0$.

Théorème II.17. La condition nécessaire et suffisante pour qu'une classe de cohomologie entière $x$ de dimension $k$, dans un espace de dimension $k + 8$ où $k > 8$, soit réalisable pour le groupe des rotations, est que la classe entière $St_3^5(x)$ soit nulle.

9. Etude de $M(SO(k))$ pour les petites valeurs de $k$. On se bornera dans ce paragraphe à la détermination de la première obstruction pour une application $g: K(Z, k) \to M(SO(k))$ pour les valeurs de $k < 5$. Il apparaîtra que cette obstruction est donnée, comme dans le cas stable, par le cube de Steenrod $St_3^5(t)$ de la classe fondamentale.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{8)}$  Pour le calcul des puissances de Steenrod  $St_{p}^{i} U$  de la classe fondamentale U, voir l'article de Borel-Serre [5] ainsi que Wu [35].</span></small>

i) $k=1$. $M(SO(1))$ s'identifie au produit $S^{\infty}\times S^{1}$, dans lequel une sphère de la forme $S\times t$, est identifiée en un point. Ce complexe a même homotopie que le cercle $S^{1}$; or $S^{1}$ est aussi une réalisation du complexe $K(Z,1)$; donc, toute classe de cohomologie entière de dimension 1 est réalisable pour le groupe des rotations (qui est d'ailleurs, en ce cas, réduit à l'unité).

ii) $k=2$. La grassmannienne $\hat{G}_{2}$ des 2-plans orientés est un espace classifiant pour $SO(2)=SU(1)=S^{1}$; elle s'identifie par suite à l'espace projectif complexe de «grande dimension» $PC(N)$; la structure universelle sur $\hat{G}_{2}$, soit $A_{SO(2)}$, s'identifie à un voisinage tubulaire normal de $PC(N)$ regardé comme hyperplan projectif de $PC(N+1)$; par suite, l'espace $M(SO(2))$ s'identifie à $PC(N+1)$ lui-même: $M(SO(2))$, tout comme $K(Z,2)$, est réalisé par l'espace projectif complexe de «grande dimension». Il en résulte: Toute classe de cohomologie entière de dimension 2 est réalisable pour le groupe des rotations.

iii) $k = 3$. $\iota$ désignant toujours la classe fondamentale de $K(Z, 3)$; on sait que la classe $St_3^5(\iota)$ n'est pas nulle, et, on peut définir le complexe «de Zilber» $K$, fibré sur $K(Z, 3)$, de fibre $K(Z, 7)$, dont l'invariant d'Eilenberg-Mac Lane $k$ est $St_3^5(\iota)$. Comme précédemment, pour tout premier $p \neq 3$, la cohomologie $H^*(K; Z_p)$ est isomorphe à celle du produit $K(Z, 3) \times K(Z, 7)$. On désignera par $v$ la classe fondamentale de ce dernier complexe; en cohomologie mod 3, $H^3(K; Z_3)$ est engendré par une classe, image de $\iota$ dans la fibration $K \to K(Z, 3)$, et qu'on notera encore $\iota$; $H^4 = H^5 = H^6 = 0$; $H^7$ est engendré par $St_3^4(\iota)$; $H^8$ est nul.

Puisque $St_3^5(U) = 0$, il existe une application $F: M(SO(3)) \to K$, et l'on a, pour l'homomorphisme $F^*$:

Mod 2. $F^{*}(\iota) = U; F^{*}(Sq^{2}\iota) = U \cdot W_{2}; F^{*}(Sq^{3}\iota) = U \cdot W_{3}$

$$
= U ^ {2}; F ^ {*} (v) = U \cdot \left(W _ {2}\right) ^ {2}; F ^ {*} (\iota \cdot S q ^ {2} \iota) = U ^ {2} \cdot W _ {2}.
$$

Mod 3. $F^{*}(\iota) = U; F^{*}(St_{3}^{4}\iota) = U \cdot P_{4}$ et rien avant la dimension 11. Mod $p; p \geq 5$. $F^{*}(\iota) = U; F^{*}(v) = U \cdot P_{4}$ et rien avant la dimension 11.

Il en résulte que $F^{*}$ est un isomorphisme de $H^{*}(K)$ sur $H^{*}(M(SO(3)))$ pour les dimensions $\leqslant 7$, et est biunivoque pour la dimension 8, pour tout corps de coefficients. Le théorème II. 6 montre que $K$ et $M(SO(3))$ ont même 8-type, et l'on en déduit:

Théorème II.18. La condition nécessaire et suffisante pour qu'une classe de cohomologie entière x, de dimension 3, dans un espace de dimension

$\leqslant 8$ soit réalisable pour le groupe des rotations est que la classe entière $St_{3}^{5}(x)$ soit nulle.

iii) $k = 4$. On construit ici encore le complexe de Zilber $K$, qu'on compare à $M(SO(4)$; l'application $F: M(SO(4)) \to K$ donne lieu à l'homomorphisme: $F^{*}$, défini, avec les mêmes notations que plus haut, par:

Mod 2. $F^{*}(\iota) = U; F^{*}(Sq^{2}\iota) = U \cdot W_{2}; F^{*}(Sq^{3}\iota)$$= U \cdot W_{3}; F^{*}(Sq^{4}\iota) = U^{2}$. $F^{*}(v) = U \cdot (W_{2})^{2}$ et rien en dimension 9.

Mod 3. $F^{*}(\iota) = U; F^{*}(St^{4}\iota) = U \cdot P_{4}; F^{*}(\iota^{2}) = U^{2}$ et rien avant la dimension 12.

Mod $p; p \geqslant 5$. $F^{*}(\iota) = U; F^{*}(\iota^{2}) = U^{2}; F^{*}(v) = U \cdot P_{4}$ et rien avant la dimension 12.

Ici encore $F^*$ est un isomorphisme pour les dimensions $\leqslant 8$, et est biunivoque pour la dimension 9. Donc $M(SO(4))$ et $K$ ont même 9-type, ce qui donne:

Théorème II.19. Pour qu'une classe de cohomologie entière $x$, de dimension 4, d'un espace de dimension $\leqslant 9$, soit réalisable pour le groupe des rotations, il faut et il suffit que $St_3^5(x) = 0$ en coefficients entiers.

## 10. Le théorème multiplicatif.

On donne dans ce paragraphe quelques théorèmes généraux sur les classes réalisables pour le groupe des rotations. D'abord une condition nécessaire:

Théorème II.20. Pour qu'une classe de cohomologie entière $x$ soit réalisable pour le groupe des rotations, il faut que toutes les puissances de Steenrod $St_{p}^{2m(p-1)+1}x$, $p$ premier impair, soient nulles.

En effet, toutes les puissances de Steenrod $St_{p}^{2m(p-1)+1}U$ de la classe fondamentale $U$ de $M(SO(k))$ sont nulles, si $p$ est un premier impair, car la grassmannienne $\widehat{G}_{k}$ n'a pas de $p$-torsion pour $p > 2$ (cf. [3]). La démonstration du théorème suivant exigera plusieurs Lemmes, sur les complexes d'Eilenberg-Mac Lane $K(Z,n)$. D'abord une définition:

Notation: On désigne par $F_{N}$ l'application — définie à une homotopie près — de $K(Z,n)$ dans lui-même, telle que $F_{N}^{*}(\iota)=N\cdot\iota$.

Lemme II.21. Soit $0 \to G' \to G \to G'' \to 0$ une suite exacte de groupes abéliens; supposons que les homomorphismes: $(F_{N'})^*: H^*(Z, k; G')$ et $(F_{N'})^*: H^*(Z, k; G'')$ soient nuls. Alors l'homomorphisme $(F_N)^*$, où $N = N' \cdot N''$, annule $H^*(Z, k; G)$.

Ecrivons en effet la suite exacte de cohomologie induite:

$$
\rightarrow H ^ {r} (Z, k; G ^ {\prime}) \stackrel {{f}} {{\rightarrow}} H ^ {r} (Z, k; G) \stackrel {{g}} {{\rightarrow}} H ^ {r} (Z, k; G ^ {\prime \prime}) \rightarrow
$$

Les homomorphismes $f$ et $g$ de cette suite commutent avec $(F_{m})^{*}$, pour tout entier $m$. Soit $x$ une classe de $H^{r}(Z, k; G)$; formons $F_{N''}^{*}(x)$; on a: $g(F_{N''}^{*}(x)) = F_{N''}^{*}(g(x)) = 0$, par hypothèse.

Donc $F_{N''}^{*}(x) = f(y)$, où $y$ est une classe de $H^{r}(Z, k; G')$. On forme alors

$$
F _ {N} ^ {*} (x) = F _ {N ^ {\prime}} ^ {*} \circ F _ {N ^ {\prime \prime}} ^ {*} (x) = F _ {N ^ {\prime}} ^ {*} (f (y)) = f \left(F _ {N ^ {\prime}} ^ {*} (y)\right) = f (0) = 0.
$$

De là on tire le

Lemme II.22. Si $G$ est un groupe abélien fini d'ordre $N$, l'homomorphisme $(F_{N})^{*}$ annule $H^{*}(Z, k; G)$.

Par décomposition de $G$ en ses composantes $p$-primaires, il suffit, grâce au Lemme précédent, de démontrer que $(F_{p})^{*}$ annule $H^{*}(Z,k;Z_{p})$ pour tout premier $p$. Or ceci résulte immédiatement du fait, énoncé au $\mathbf{n}^{\mathbf{o}}6\colon H^{*}(Z,k;Z_{p})$ est engendrée par des $p$-puissances $St_{p}^{i}$ itérées de la classe fondamentale $(\iota)$.

Lemme II.23. Si $G$ est un groupe abélien de type fini, et si tout élément de $H^{r}(Z,k;G)$ est d'ordre fini $N$, il existe un entier non nul $m$, tel que $(F_{m})^{*}$ annule $H^{r}(Z,k;G)$.

On décompose $G$ en sa composante libre $F$ et sa composante de torsion $T$; on a alors: $H^{r}(Z, k; G) \approx H^{r}(Z, k; F) \oplus H^{r}(Z, k; T)$.

Tout élément de $H^{r}(Z, k; F)$ est d'ordre $N$; il est clair qu'il suffit de démontrer le lemme pour $H^{r}(Z, k; F)$, car $H^{r}(Z, k; T)$ est justiciable du lemme II.22, puisque $T$ est un groupe fini.

Formons alors la suite exacte:

$$
0 \to F \underset {(N)} {\overset {\rightarrow} {\to}} F \to F ^ {\prime} \to 0
$$

où l'homomorphisme $(N)$ est la multiplication par l'entier non nul $N$. Puisque $F$ est de type fini, $F'$ est un groupe fini, d'ordre $N'$. Soit $x$ une classe de $H^{r}(Z, k; F)$, et soit $g$ l'homomorphisme de la suite exacte induite:

$$
\rightarrow H ^ {r} (Z, k; F) \stackrel {(N)} {\rightarrow} H ^ {r} (Z, k; F) \stackrel {g} {\rightarrow} H ^ {r} (Z, k; F ^ {\prime}) \rightarrow
$$

On aura: $g \circ F_{N'}^*(x) = F_{N'}^*(g(x)) = 0$ d'après le lemme II.22.

Donc $F_{N'}^{*}(x)$ est de la forme $N \cdot y, y \in H^{r}(Z, k; F)$, et est par suite nul. Nous sommes maintenant en mesure de démontrer le lemme:

Lemme II.24. Soit Y un espace, dont le  $k^{ième}$  groupe d'homotopie  $\pi_{k}(Y)$  a une composante libre isomorphe à Z, de générateur t. On suppose de plus que tous les groupes d'homotopie  $\pi_{q}(Y)$, où  $q \geqslant k$, sont de type fini, et tels que les groupes de cohomologie  $H^{q+1}(Z, k; \pi_{q}(Y))$  soient finis. Il existe alors une application  $G_{n}$  du n-squelette  $K^{n}$  de  $K(Z, k)$  dans Y, qui applique le générateur de  $\pi_{k}(K(Z, k)) \approx Z$  sur  $N(q, k) \cdot t$, où l'en-tier non nul  $N(q, k)$  ne dépend que de k, q et Y.

Le $k$-squelette de $K(Z, k)$ peut être réalisé par une sphère $S^k$; l'application $G_k: S^k \to Y$ est celle définie par l'élément $t$ de $\pi_k(Y)$; supposons $G_q$ définie sur le $q$-squelette $K^q$ de $K(Z, k)$; le prolongement de $G_q$ au $(q + 1)$-squelette de $K(Z, k)$ est en général interdit par une obstruction, cocycle $w'$ dont la classe appartient au groupe — fini par hypothèse — $H^{q+1}(Z, k; \pi_q(Y))$. Formons alors l'application $F_m: K(Z, k) \to K(Z, k)$ associée par le lemme II.23 au groupe fini $H^{q+1}(Z, k; \pi_q(Y))$, et composons la avec $G_q$:

$$
K (Z, k) \stackrel {F _ {m}} {\rightarrow} K (Z, k) \stackrel {G _ {q}} {\rightarrow} Y
$$

L'application composée $G_q \circ F_m$ est définie sur le $q$-squelette de $K(Z, k)$; elle définit sur le $(q + 1)$-squelette, un cocycle obstruction $w$, dont la classe est donnée par la relation: $w = (F_m)^*(w')$.

D'après le lemme II.23, cette classe est nulle ; c'est dire qu'on pourra, après une éventuelle déformation, prolonger l'application $G_q \circ F_m$ au $(q + 1)$-squelette de $K(Z, k)$, et définir ainsi $G_{q+1}$; et l'on aura: $N(q + 1, k) = m \cdot N(q, k)$, ce qui définit bien un entier non nul. Le Lemme II.24 est ainsi entièrement démontré.

On appliquera le lemme II.24 à la grassmannienne $\widehat{G}_{k}$ des $k$-plans orientés pour $k$ pair, ou, plus exactement, à l'espace universel $A_{SO(k)}$ qui lui est homotopiquement équivalent. Rappelons que la cohomologie $H^{*}(\widehat{G}_{k})$, à coefficients réels, est une algèbre de polynômes, dont les générateurs sont les classes de Pontrjagin $P^{4i}$, $i < [k/2]$, et la classe fondamentale $X_{k}$ de dimension $k$. Il résulte alors de la $\mathcal{C}$-théorie de J. P. Serre [22], qu'il existe un $\mathcal{C}$-isomorphisme entre la cohomologie de $\widehat{G}_{k}$ et celle d'un produit de complexes d'Eilenberg-Mac Lane de la forme:

$$
K (Z, 4) \times K (Z, 8) \times \dots \times K (Z, k).
$$

C désignant la famille des groupes finis. Par suite, les seuls groupes d'homotopie non finis de $\widehat{G}_{k}$ apparaissent pour les dimensions des générateurs, soit 4i et k; on prendra pour élément $t\in\pi_{k}(\widehat{G}_{k})$ le générateur de la composante Z associée — non canoniquement, mais c'est sans importance — au générateur de dimension k lié à la classe $X_{k}$; c'est dire que, dans l'application $t:S^{k}\to\widehat{G}_{k}$, on aura $t^{*}(X_{k})=N^{0}\cdot s^{k}$, où $N^{0}$ est un entier non nul.

Les hypothèses du Lemme II.24 sont alors vérifiées; en effet, le groupe de cohomologie $H^{q+1}(Z, k; \pi_q(\widehat{G}_k))$ est de type fini, parce que le groupe $\pi_q(\widehat{G}_k)$ est lui-même de type fini; et tout élément y est d'ordre fini: en effet, ou bien le groupe des coefficients $\pi_q(\widehat{G}_k)$ est lui-même fini, ou, s'il est infini — ce qui arrive pour $q \equiv 0 \mod 4$, le groupe $H^{q+1}(Z, k; \pi_q(\widehat{G}_k))$ n'a que des éléments d'ordre fini, parce que tout élément du groupe $H^{q+1}(Z, k; Z)$ est alors d'ordre fini.

On pourra ainsi définir, pour tout entier $q > k$, une application $G_{q}$ du $q$-squelette de $K(Z, k)$ dans $A_{SO(k)}$, donc dans $M(SO(k))$; formons l'application composée:

$$
K ^ {q} \stackrel {G} {\rightarrow} \widehat {G} _ {k} \stackrel {h} {\rightarrow} M (S O (k)).
$$

$U$ désignant toujours la classe fondamentale de $M(SO(k))$, on a, si $k$ est pair: $h^{*}(U) = X_{k}$, et par suite: $G^{*} \circ h^{*}(U) = N \cdot \iota$ où l'entier $N$, non nul, ne dépend que de $q$ et $k$. Donc:

Théorème II.25. Pour toute classe de cohomologie entière $x$, de dimension $k$, d'un espace de dimension finie $q$, il existe un entier non nul $N$, ne dépendant que de $k$ et $q$, tel que la classe multiple $N \cdot x$ soit réalisable pour le groupe des rotations.

Remarque. Ce raisonnement s'appliquerait également en substituant à la grassmannienne réelle $\widehat{G}_{k}$, la grassmannienne complexe, et, éventuellement, pour $k \equiv 0 \mod 4$, le classifiant du groupe symplectique. On obtiendra donc le même théorème, en substituant au groupe $SO(k)$ le groupe unitaire (resp. le groupe symplectique), mais les coefficients $N$ seront alors plus élevés.

11. Enoncé des résultats. Nous sommes maintenant en mesure d'énoncer les résultats acquis pour notre problème initial: réaliser une classe d'homologie donnée d'une variété par une sous-variété; grâce aux théorèmes II.5 et 5', on est ramené à chercher si la classe de cohomologie corres-

pondante admet une réalisation orthogonale, problémé sur lequel les théorèmes des n° 7—8—9—10 fournissent autant de réponses partielles.

i) Classes mod 2. Les théorèmes II.13—5 donnent:

Théorème II.26. Dans une variété différentiable $V^n$ les classes des groupes d'homologie mod 2 suivants sont réalisables par des sous-variétés: $H_{n-1}(V^n)$ pour tout $n; H_{n-2}(V^n)$ pour $n < 6; H_{n-3}(V^n)$ pour $n < 8; H_i(V^n)$ pour $i \leqslant (n/2)$, et pour tout $n$.

On observera, dans le cas de $H_{n-2}(V^n)$, que l'obstruction $(1/2) \cdot \delta p(u)$ du théorème II.14, est nécessairement nulle sur la classe fondamentale d'une variété $V^5$ de dimension 5: c'est trivial si $V^5$ est orientable; si $V^5$ n'est pas orientable, la classe fondamentale de $H^5(V^5; Z)$ est un $Sq^1$, par suite, sa réduction mod 2 n'est pas nulle. Par contre, on ne peut rien dire des classes du groupe $H_4(V^6)$: c'est là l'exemple le plus simple de groupe d'homologie pour laquelle la question de la réalisation par des sous-variétés ne peut être résolue par les résultats ici énoncés.

ii) Classes d'homologie entières.

Les théorèmes II.17—8—9 nous donnent:

Théorème II.27. Sont réalisables dans $V^n$ orientable par des sous-variétés orientables, les classes des groupes suivants: $H_{n-1}(V^n); H_{n-2}(V^n)$ pour tout $n; H_i(V^n)$ pour $i \leqslant 5$, et tout $n$.

En effet, dans le cas limite  $H_{5}(V^{8};Z)$ , l'obstruction correspondante, donnée par le cube de Steenrod  $St_{3}^{5}(u)$ , est une classe d'ordre 3, et est donc nulle sur la classe fondamentale. De là on tire:

Corollaire II.28. Toutes les classes d'homologie entière des variétés orientables de dimension  $\leqslant8$  sont réalisables par des sous-variétés. Ici encore, le cas le plus simple non décidé est donné par les classes du groupe  $H_{6}(V^{9};Z)$ . (Cf. la note  $^{9}$ ), qui suit.)

On notera encore, en conséquence du théorème II.17: Pour qu'une classe d'homologie de dimension 8 dans une variété de dimension $\geqslant 17$ soit réalisable par une sous-variété, il faut et il suffit que le cube $St_{3}^{5}$ de la classe de cohomologie duale soit nul.

Enfin, les théorèmes «multiplicatifs» II.4 et II.25 donnent:

Théorème II.29. Pour toute classe d'homologie entière z d'une variété orientable  $V^{n}$ , il existe un entier non nul N tel que la classe multiple  $N \cdot z$  soit réalisable par une sous-variété.

Ce théorème admet un corollaire intéressant en cohomologie réelle ou rationnelle:

Corollaire II.30. Les groupes d'homologie à coefficients réels ou rationnels d'une variété orientable  $V^{n}$  admettent pour bases des systèmes d'éléments représentés par des sous-variétés.

Remarques. Il ne faudrait pas croire que toute classe d'homologie entière d'une variété peut être réalisée par une sous-variété ; nous verrons au Chap. III l'exemple d'une classe de dimension 7 (dans une variété de dimension 14) qui n'est pas réalisable ; on montrera, que, pour toute dimension $\geqslant 7$, il existe des classes entières non réalisables dans des variétés de dimension arbitrairement grande. J'ignore s'il existe des classes de dimension 6 non réalisables.$^{9)}$

Si deux classes $z$ et $z'$ sont réalisables, il ne s'ensuit pas que la classe $z + z'$ est réalisable; cette propriété n'est exacte — en général — que si la dimension des classes $z$ et $z'$ est inférieure strictement à la moitié de la dimension de la variété. Par contre, l'intersection de deux classes réalisables est réalisable. C'est là une conséquence presque immédiate du théorème I.5.

Nécessité des hypothèses de différentiabilité. Toute la théorie ici présentée repose de façon essentielle sur la structure différentiable de la variété ambiante et des sous-variétés plongées ; on peut montrer cependant que, dans le cas du problème de la réalisation des classes mod 2 certaines conditions tirées du théorème II.1 ont une signification topologique intrinsèque. Par exemple: Soit $F: M(O(k)) \to K(Z_2, k)$ l'application canonique, telle que $F^*(\iota) = U$; soit $c = T(\iota)$ une classe de $H^*(Z_2, k; Z_2)$ qui appartient au noyau de $F$ ($T$ désigne ici une somme de cup-produits de $Sq^i$ itérés); il est clair que, pour qu'une classe de cohomologie $x \in H^k(V^n)$ corresponde à la classe d'une sous-variété différentiablement plongée, il faut que $T(x) = 0$. Or on peut montrer que si $T(x)$ n'est pas nul, mod 2, la classe correspondante à $x$ ne peut être réalisée, même par une sous-variété topologiquement plongée. J'ai montré en effet dans [27] qu'à toute sous-variété topologiquement plongée, on peut associer des classes caractéristiques normales généralisées $W^i$; ces classes ont les mêmes propriétés formelles que les classes de Stiefel-

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$St_{3}^{5}; H^{n-6} (V^{n}; Z) \rightarrow H^{n-1} (V^{n}; Z)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">9) Par un calcul plus poussé, j'ai pu montrer que toute classe d'homologie entière de dimension 6 est réalisable; l'obstruction correspondante, définie par l'homomorphisme $St_{3}^{5}$; $H^{n-6}(V^{n};Z)\to H^{n-1}(V^{n};Z)$ est identiquement nulle. De même les résultats des théorèmes II. 18 et 19 peuvent être améliorés; dans le corollaire II. 28 la limite 8 peut être remplacée par 9. Le premier cas à décider est celui du groupe $H_{7}(V^{10};Z)$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$H_{7}(V^{10};Z)$</span></small>

Whitney de la structure des vecteurs normaux à une sous-variété différentiablement plongée, et satisfont notamment aux formules (3) de Wu (qui se démontrent alors à l'aide des relations d'Adem [1] entre $Sq^i$ itérés). A toute opération telle que $T$, augmentant la dimension de $i$ unités, on peut associer un polynome en $W_j$, de poids total $i$. Si la classe $T(\iota)$ appartient au noyau de $F$, ce polynome est identiquement nul; il en résulte que $T(x)$ doit être nul, d'où une contradiction. On pourra conduire explicitement les calculs sur l'exemple suivant, qui m'a été indiqué par J. P. Serre: Si $\iota$ est la classe fondamentale de $K(Z_2, 2)$, prendre $T(\iota) = (Sq^2 Sq^1 \iota) \cdot \iota^2 + (Sq^1 \iota)^3 + Sq^1 \iota \cdot \iota^3$.

## CHAPITRE III

## Sur un problème de Steenrod

1. Enoncé du problème. N. Steenrod a, dans [12], posé le problème suivant: étant donnée une classe d'homologie $z \in H_r(K)$ d'un polyèdre fini $K$, existe-t-il une variété $M^r$ compacte, et une application $f: M^r \to K$, telle que $z$ soit l'image par $f_*$ de la classe fondamentale de la variété $M^r$? Nous supposerons ici encore que la variété $M^r$ considérée est différentiable. Comme on le verra, la réponse est très différente, suivant le groupe de coefficients ($Z$ ou $Z_2$), qui sert à définir la classe d'homologie donnée $z$. Ce problème est en rapport étroit avec le problème du Chapitre II sur la réalisation des classes d'homologie de variétés par des sous-variétés. Nous allons préciser ce rapport.

2. Définition: Variétés associées à un polyèdre fini $K$. Soit $K$ un polyèdre fini, de dimension $n$; $K$ peut toujours être plongé rectilinéairement dans un espace euclidien $R^n$, où $n \geqslant 2m + 1$; on peut alors définir — par exemple, comme solution d'un problème de Dirichlet — une fonction numérique nulle sur $K$, strictement positive et de classe $C^\infty$ sur le complémentaire $R^n - K$. Puisque $K$ est un rétracte absolu de voisinage, il existe un voisinage ouvert $U$ de $K$, et une rétraction $r: U \to K$. Soit $c$ une valeur régulière de la fonction $f$, assez petite pour que l'image réciproque $f^{-1}(0, c)$ soit tout entière contenue dans $U$ (il en existe, d'après le Théorème I.1). Dans ces conditions, l'image réciproque $f^{-1}(0, c)$ est une variété à bord $M^n$, dont le bord régulier différentiable $T^{n-1}$ est l'image réciproque $f^{-1}(c)$. $K$ est rétracte, par la restriction de la rétraction $r$, de la variété à bord $M^n$.

Remarque. S'il n'existait dans l'intervalle [0, c] aucune valeur critique de la fonction f, on pourrait affirmer, de façon plus précise, que K est un rétracte par déformation de la variété à bord  $M^{n}$ : la déformation  $M^{n} \to K$  serait alors définie grâce aux trajectoires intégrales du champ de vecteurs défini par le gradient de f; mais je ne sais si on peut exclure pour la fonction f la possibilité d'admettre des valeurs critiques arbitrairement petites.

Etant donnée la variété à bord $M^n$, on peut en déduire, par la construction classique du «dédoublement» (Verdoppelung) une variété compacte $V^n$: on prend deux exemplaires isomorphes de $M^n$ qu'on identifie le long de leur bord commun $T^{n-1}$; on désignera par $g =: M^n \to V^n$ l'injection, et par $h: V^n \to M^n$ l'application définie par le passage au quotient quand on identifie les deux composantes $M_1^n$ et $M_2^n$. Une variété telle que $V^n$ sera appelée variété associée au polyèdre fini $K$. Il est clair que $K$ est un rétracte de toute variété associée, et par suite l'application $r \circ h: V^n \to K$ induit, pour tout groupe de coefficients, un homomorphisme $h^* \circ r^*: H^r(K) \to H^r(V^n)$ qui est biunivoque. En effet, si on désigne par $i$ l'application identique de $K$ dans $M^m$, l'application $r \circ h$ est inverse de l'application $g \circ i$. Un voisinage à bord différentiable régulier tel que $M^n$ sera appelé voisinage associé à $K$. Nous avons alors le théorème, qui donne le rapport entre les questions des Chapitres II et III:

Théorème III.1. Pour qu'une classe d'homologie $z \in H_r(K)$ soit l'image d'une variété différentiable compacte, il faut et il suffit que la classe $z$ puisse être réalisée par une sous-variété dans un voisinage associé à $K$, de dimension assez grande.

Il est immédiat que la condition est suffisante: si, en effet, la classe z est réalisée dans le voisinage  $M^{n}$  par une sous-variété compacte  $W^{r}$ , z est l'image de la classe fondamentale de  $W^{r}$  par l'homomorphisme  $r_{*}$  induit par la rétraction  $r: M^{n} \to K$ .

La condition est nécessaire. Supposons que z soit l'image, par une application f de la classe fondamentale d'une variété différentiable compacte  $W^{r}$ . Donnons-nous alors:

a) un plongement régulier différentiable de $W^r$ dans un $R^n$, soit $g$.  
b) un plongement rectilinéaire de $K$ dans un $R^m$, soit $i$.

Désignons par Y le «mapping cylinder» de l'application donnée f; soit  $(x, t)$  le point de Y qui, pour tout point x de  $W^{r}$ , divise le segment  $[f(x), x]$  pris dans cet ordre dans le rapport  $t(0 \leqslant t \leqslant 1)$ .

Soit enfin $a$ un paramètre réel $\geqslant 0$. On définit un plongement $F_{a}$ de $Y$ dans l'espace euclidien $R^{n+m+1} \approx R^{n} \times R^{m} \times R$ par la formule:

$$
F _ {a} (x, t) = (a t g (x), (1 - t) i \circ f (x), a t)
$$

et pour tout point y de K

$$
F _ {a} (y) = (0, i (y), a t).
$$

Soit $M$ un voisinage associé au plongement de $K$ dans $R^{n+m+1}$ défini par $F_0(K)$. Par raison de compacité, il existe une valeur $c$ du paramètre $a$ assez petite pour que, si $a < c$, l'espace image $F_a(Y)$ soit tout entier contenu dans $M$. Dans ces conditions, l'image $F_a(W^r, 1)$ est une sous-variété de $M$, et sa classe fondamentale appartient à la classe $k(z)$, image de $z$ par l'injection $k: K \to M$ définie par $F_a$. Le théorème III.1 est ainsi entièrement démontré.

3. Application: Cas des coefficients mod 2. Toutes les fois qu'on pourra réaliser la classe $k(z)$ par une sous-variété dans la variété associée $V^n$, on pourra résoudre affirmativement le problème de Steenrod. C'est précisément le cas lorsque les coefficients sont les entiers mod 2. En effet, la dimension $n$ de la variété associée peut toujours être prise plus grand que $2r$, de sorte qu'on peut appliquer le théorème II.26. Ceci nous donne:

Théorème III.2. Toute classe d'homologie mod 2 d'un polyèdre fini est l'image de la classe fondamentale d'une variété différentiable compacte.

En coefficients entiers, le théorème II.27 donne:

Théorème III.3. Toute classe d'homologie entière de dimension $\leqslant 5$ d'un polyèdre fini est l'image de la classe fondamentale d'une variété orientable compacte.

Le théorème II.29 nous donne le théorème «multiplicatif»:

Théorèmes III.4. Pour toute classe z de dimension p d'homologie entière d'un polyèdre fini K, il existe un entier non nul N, ne dépendant que de p, tel que la classe multiple Nz soit l'image de la classe fondamentale d'une variété différentiable compacte.

Pour obtenir des résultats plus précis dans le cas des coefficients entiers, on va introduire dans l'homologie de K de nouveaux opérateurs.

4. Les opérateurs $\vartheta_{i}^{p}$. Soit toujours $K$ un polyèdre fini, plongé (topologiquement) dans $R^{m}$; formons la limite projective des cohomologies à supports compacts des voisinages ouverts de $K$ dans $R^{m}$, soit $H^{*}(U)$.

La dualité de Poincaré donne alors (cf. [27] Théorème III.4) un isomorphisme $\chi$ de $H_{r}(K)$ sur $H_{K}^{m-r}(U)$, pour tout groupe de coefficients.

A toute puissance de Steenrod d'indice $i$ pair $St_{p}^{i}$ 10), on associe l'homomorphisme $\vartheta_{i}^{p}:H_{r}(K;Z_{p})\to H_{r-i}(K;Z)$, défini par la relation:

$$
\vartheta_ {i} ^ {p} = \chi^ {- 1} S t _ {p} ^ {i} \chi .
$$

On définira les opérateurs $\vartheta_{p}^{i}$ correspondant aux $St_{p}^{i}$ d'indice $i$ impair directement par la formule:

$$
\vartheta_ {2 r + 1} ^ {p} = \vartheta_ {1} ^ {p} \circ \vartheta_ {2 r} ^ {p}
$$

où $\vartheta_{1}^{p}$ désigne l'homomorphisme de Bockstein $1/p\cdot\delta$ (ceci afin d'éviter des complications de signe, dues au fait que l'opérateur $St_{p}^{1}$ ne commute pas à la suspension).

Ces opérateurs $\vartheta_{i}^{p}$ ont les propriétés suivantes, démontrées dans [27] pour le cas $p = 2$, mais qui s'étendent sans difficultés au cas $p > 2$:

i) Ce sont des invariants topologiques, indépendants de l'immersion de K dans l'espace euclidien.

ii) Dans toute application $f: K \to K'$, $\vartheta_{i}^{p}$ commute avec l'homomorphisme $f_{*}$ induit par $f$.

iii) Sur le corps $Z_p$, les opérateurs $\vartheta_i^p$ peuvent être déterminés en fonction des $St_p^i$; si $\vartheta_i^p$ applique $H_r(K)$ dans $H_{r-i}(K)$, désignons par $Q_p^i$ l'homomorphisme dual, qui applique $H^{r-i}(K;Z_p)$ dans $H^r (K;Z_p)$. Alors les $Q_p^i$ d'indice pair s'expriment en fonction des $St_p^i$ par les formules:

$$
\Sigma_ {i} Q _ {p} ^ {m - i} S t _ {p} ^ {i} = 0 m, i \equiv 0 \bmod 2 (p - 1), Q ^ {\circ} = \text { identité }.
$$

La démonstration de cette formule est en tout point analogue à celle de la formule (60) Th. III. 23 de [27]. Les $Q^i$ d'indice impair s'obtiennent à partir des $Q^i$ pairs par la relation, transposée des $\vartheta_i^p$:

$Q_{p}^{2r+1}=Q_{p}^{2r}\circ Q_{p}^{1}\quad\text{ou}\quad Q_{p}^{1}\quad\text{désigne l'homomorphisme de Bockstein 1/p}\cdot\delta,\quad\text{suivi de la réduction mod }p.$

Par exemple, on aura:

$$
Q _ {3} ^ {4} = - S t _ {3} ^ {4}; Q _ {3} ^ {5} = - S t _ {3} ^ {4} \circ Q _ {3} ^ {1} = S t _ {3} ^ {4} S t _ {3} ^ {1}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$St_{p}^{2k(p - 1)}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{10)}$ On suppose ici les puissances de Steenrod $St_{p}^{2k(p-1)}$ munies du coefficient normalisateur introduit par J. P. Serre dans [5], où $St_{p}^{2k(p-1)}$ est notée $P_{p}^{k}$. Les puissances d'indice impair se déduisent des puissances d'indice pair $P_{p}^{k}$ par l'homomorphisme de Bockstein $1/p\cdot\delta$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$P_{p}^{k}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$P_{p}^{k}$</span></small>

Revenons maintenant au polyèdre $K$, plongé dans une variété associée $V^{m}$; si $z$ est une classe de $H_{r}(K;Z)$, la classe $\chi(z) \in H^{m-r}(U;Z)$ a dans $H^{m-r}(V^{m})$ une image canonique $u$ qu'on dénotera encore $\chi(z)$; $u$ n'est autre que la classe de cohomologie qui correspond à la classe d'homologie $i_{*}(z) \in H_{r}(V^{m})$ par la dualité de Poincaré; comme $i_{*}:H_{r}(K) \to H_{r}(V^{m})$ est biunivoque, $\chi:H_{r}(K) \to H^{m-r}(V^{m})$ l'est aussi. Et l'on a par définition:

$$
S t _ {p} ^ {i} \chi (z) = \pm \chi (\vartheta_ {i} ^ {p} (z)).
$$

On sait que, pour que la classe d'homologie $i_{*}(z)$ soit réalisable dans $V^{m}$ par une sous-variété, il faut que toutes les puissances $St_{p}^{i}(i, p \text{ impairs})$ de la classe de cohomologie correspondante $\chi(z)$ soient nulles (Th. II. 20). Ceci nous donne:

Théorème III.5. Pour qu'une classe d'homologie entière z d'un polyèdre fini soit l'image de la classe fondamentale d'une variété différentiable compacte, il faut que toutes les classes entières $\vartheta_{i}^{p}(z)$, $p$, i impairs, soient nulles.

Cette condition est suffisante pour les classes de dimension $\leqslant 8$; en effet, le théorème II.17 donne:

Théorème III.6. Pour qu'une classe d'homologie entière z de dimension  $\leqslant8$  d'un polyèdre fini soit l'image de la classe fondamentale d'une variété orientable différentiable compacte, il faut et il suffit que la classe entière  $\vartheta_{5}^{3}(z)$  soit nulle.

Pour $r \leqslant 5$, on retrouve le résultat du théorème III.3. Considérons le cas $r = 6$; la classe $\vartheta_5^3(z)$ est une classe de $H_1(K;Z)$, d'ordre 3. Si elle n'est pas nulle, il existe un entier $m$ (multiple de 3), et une classe de cohomologie $u \in H^1(K;Z_m)$ dont le produit scalaire avec $\vartheta_5^3(z)$ n'est pas nul.

Soit $f$ l'application canonique de $K$ dans $K(Z_{m}, 1)$, telle que $f^{*}(\iota) = u, \iota$ désignant toujours la classe fondamentale de $K(Z_{m}, 1)$. Ecrivons alors le diagramme commutatif:

$$
\begin{array}{c} H _ {6} (K; Z) \longrightarrow H _ {6} (Z _ {m}, 1; Z) \\ \vartheta_ {5} ^ {3} \Bigg \downarrow \qquad \qquad \qquad \qquad \vartheta_ {5} ^ {3} \Bigg \downarrow \\ H _ {1} (K; Z) \xrightarrow {f _ {*}} H _ {1} (Z _ {m}, 1; Z) \end{array}
$$

Or, le groupe $H_6(Z_m, 1; Z)$ est nul, comme il ressort de la détermination connue [11] de l'homologie des groupes cycliques ; donc $f_*(\vartheta_5^3(z)) = 0$, et le produit scalaire $\vartheta_5^3(z), u$ est nul. Comme ceci est vrai pour tout entier $m$, on en déduit que la classe entière $\vartheta_5^3(z)$ est nulle. Donc:

Corollaire III.7. Toute classe d'homologie entière de dimension 6 d'un polyèdre fini, est l'image de la classe fondamentale d'une variété différentiable compacte.

Nous allons montrer que ce résultat ne peut être amélioré ; dans ce but, énonçons d'abord un lemme sur les complexes d'Eilenberg-Mac Lane:

Lemme III.8. La classe $St_3^5 St_3^1(\iota)$ du complexe $K(Z_3, r)$ n'est pas nulle dès que $r \geqslant 2$.

Observons d'abord que, si la classe $St_3^5 St_3^1(\iota)$ n'est pas nulle pour la valeur $r = n$, elle n'est pas nulle dans tous les complexes $K(Z_3, m)$ où $m > n$, à cause de la suspension; il suffit par suite de montrer que $St_3^5 St_3^1(\iota)$ n'est pas nulle dans $K(Z_3, 2)$; il en est effectivement ainsi; mais, comme il est assez délicat de le voir directement, il est plus commode de substituer au complexe $K(Z_3, 2)$ un produit de deux complexes $K(Z_3, 1)$. Désignons par $v_1$, resp. $v_2$ leurs classes fondamentales, par $u_1 = St_3^1 v_1$, resp. $u_2 = St_3^1 v_2$ les générateurs de $H^2(Z_3, 1; Z_3)$ dans les deux complexes. On a alors:

$$
\begin{array}{r l} S t _ {3} ^ {5} S t _ {3} ^ {1} (v _ {1} \cdot v _ {2}) & = S t _ {3} ^ {1} S t _ {3} ^ {4} (u _ {1} \cdot v _ {2} - v _ {1} \cdot u _ {2}) = S t _ {3} ^ {1} ((u _ {1}) ^ {3} \cdot v _ {2} - (u _ {2}) ^ {3} \cdot v _ {1}) \\ & = (u _ {1}) ^ {3} \cdot u _ {2} - u _ {1} \cdot (u _ {2}) ^ {3} \neq 0. \end{array}
$$

Le lemme est ainsi démontré. Puisque la classe entière

$$
S t _ {3} ^ {5} S t _ {3} ^ {1} (\iota) \in H ^ {r + 6} (Z _ {3}, r; Z), r \geqslant 2,
$$

n'est pas nulle, on en déduit, par dualité, qu'il existe une classe $z \in H_{r+5}(Z_3, r; Z)$ dont le produit scalaire avec la classe $St_3^4 St_3^1(\iota)$ n'est pas nul (mod 3). C'est dire que $\langle z, Q_3^5(\iota) \rangle \neq 0$ donc $\langle \vartheta_5^3(z), \iota \rangle \neq 0$ et $\vartheta_5^3(z) \neq 0$. Nous avons ainsi démontré:

Théorème III.9. Pour toute dimension $r \geqslant 7$, il existe des classes d'homologie entière de polyèdres finis qui ne sont l'image d'aucune variété orientable différentiable compacte.

Un exemple. On réalise les complexes $K(Z_{3}, 1)$ par des espaces lenticulaires ; il suffit ici de prendre des espaces $L^{7}$ de dimension 7, quotients de la sphère $S^{7}$ par le groupe $Z_{3}$ qui y opère sans point fixe. On désigne ici encore par $v_{1}$, resp. $v_{2}$ les générateurs de $H^{1}(L_{1}; Z_{3})$ resp. $H^{1}(L_{2}; Z_{3})$, par $u_{1} = St_{3}^{1} v_{1}$, resp. $u_{2} = St_{3}^{1} v_{2}$, ceux de $H^{2}(L_{1}; Z_{3})$ resp. $H^{2}(L_{2}; Z_{3})$

pour deux exemplaires  $L_{1}$  et  $L_{2}$  de L, et on forme la variété  $V^{14}$  produit de  $L_{1}$  par  $L_{2}$ . Considérons alors la classe:

$$
X = u _ {1} \cdot v _ {2} (u _ {2}) ^ {2} - v _ {1} \cdot (u _ {2}) ^ {3}.
$$

C'est une classe entière, car $X = St_{3}^{1}(v_{1} \cdot v_{2}(u_{2})^{2})$.

Désignons par $z \in H_7(V^{14}; Z)$ la classe qui lui correspond par la dualité de Poincaré. Je dis que la classe $\vartheta_5^3(z)$ n'est pas nulle mod 3 ; formons en effet le produit scalaire:

$$
\langle \vartheta_ {5} ^ {3} (z), v _ {1} \cdot v _ {2} \rangle = \langle z, Q _ {3} ^ {5} (v _ {1} \cdot v _ {2}) \rangle = \langle z, S t _ {3} ^ {4} S t _ {3} ^ {1} (v _ {1} \cdot v _ {2}) \rangle \mod 3
$$

Ce produit scalaire peut être remplacé par le cup-produit:

$$
X \cdot S t _ {3} ^ {4} S t _ {3} ^ {1} (v _ {1} \cdot v _ {2}) = X \cdot ((u _ {1}) ^ {3} \cdot v _ {2} - v _ {1} \cdot (u _ {2}) ^ {3}) = v _ {1} \cdot v _ {2} (u _ {1} \cdot u _ {2}) ^ {3} \neq 0.
$$

$\vartheta_{5}^{3}(z)$ n'est donc pas nulle, et la classe z n'est l'image d'aucune variété différentiable compacte. A fortiori, z ne peut être réalisée dans $V^{14}$ par aucune sous-variété, ce qu'on vérifie en formant:

$$
S t _ {3} ^ {5} X = S t _ {3} ^ {1} \left(\left(u _ {1}\right) ^ {3} \cdot v _ {2} \left(u _ {2}\right) ^ {2}\right) = \left(u _ {1} \cdot u _ {2}\right) ^ {3} \neq 0.
$$

On pourrait donner de même des exemples de classes de dimension 7 non réalisables par des sous-variétés dans des variétés de dimension arbitrairement grande.

5. Les puissances de Steenrod dans la cohomologie d'une variété différentiable. Soit $V^n$ une variété différentiable compacte, et $(V^n)$ sa classe fondamentale; d'après le théorème III.5 dont c'est un cas particulier, toutes les classes entières $\vartheta_i^p(V^n), p$ premier impair, $i \equiv 1 \mod 2(p - 1)$ sont nulles. On en déduit par dualité:

Théorème III.10. Dans toute variété orientable différentiable compacte  $V^{n}$ , les homomorphismes  $Q_{p}^{i}: H^{n-i}(V^{n}; Z_{p}) \to H^{n}(V^{n}; Z_{p})$  sont nuls  $(p, i \text{ impaires})$ .

Par example: $Q_3^5 = St_3^4 St_3^1: H^{n-5}(V^n) \to H^n(V^n; Z_3)$ est nul.

On retrouvera ces relations en exprimant que dans le produit  $V^{n} \times V^{n}$ , la classe diagonale est réalisable par une sous-variété à l'aide du théorème II.20. On remarquera que ces relations sont vérifiées non seulement dans toute variété différentiable, mais encore, dans toute variété image par une application de degré 1 d'une variété différentiable. Elles ne semblent point provenir, cependant, de la dualité de Poincaré. D'où la question ouverte: Ces relations peuvent-elles être établies pour une variété topologique, sans hypothèse de différentiabilité?

## CHAPITRE IV

## Variétés différentiables cobordantes

Soit $V^n$ une variété compacte orientable; on dit que $M^{n+1}$ est une variété à bord de bord $V^n$, si les conditions suivantes sont remplies:

a) Le complémentaire $M^{n+1} - V^n$ est une variété (ouverte) de dimension $n + 1$.

b) En tout point $x$ de $V^n$ il existe une carte locale, compatible avec les structures différentiables données sur $V$ et $M$, dans laquelle l'image de $M^{n+1}$ est un demi-espace $R^{n+1}$ limité par un espace $R^n$ image de $V^n$.

Si la variété $M^{n+1} - V^n$ est orientable, alors le bord $V^n$ est également orientable, et toute orientation de $M^{n+1}$ induit canoniquement une orientation de $V^n$; il suffit pour cela d'introduire l'opérateur bord défini par: $\delta : H_{n+1}(M^{n+1}, V^n) \to H_n(V^n)$.

On dira qu'une variété compacte orientée $V^n$ est une variété-bord s'il existe une variété à bord orientable compacte $M^{n+1}$ de bord $V^n$, et si on peut munir $M^{n+1}$ d'une orientation qui induise l'orientation donnée de $V^n$. Le présent Chapitre est consacré à la question suivante, également soulevée par N. Steenrod dans [12]: Donner des conditions nécessaires et suffisantes pour qu'une variété $V^n$ donnée soit une variété-bord. J'ai donné dans [27] un certain nombre de conditions nécessaires pour qu'une variété soit un bord, ou un bord mod 2 (sans condition d'orientabilité); par une généralisation convenable du problème, il nous sera possible d'aborder la question des conditions suffisantes.

## Définition. Variétés cobordantes.

Deux variétés compactes $V, V'$ de même dimension $k$, orientées, seront dites cobordantes (notation $V \simeq V'$), si la variété $V' - V$, réunion de la variété $V'$ et de la variété $V$ dont on a renversé l'orientation, est une variété-bord.

Si $V$ et $V'$ sont cobordantes à une même variété $V''$, alors $V$ et $V'$ sont cobordantes entre elles, comme le montre une construction géométrique très simple (identifier le long de $V''$ les deux variétés à bord qui définissent $V \simeq V''$ et $V' \simeq V''$). L'ensemble des variétés de dimension $k$, compactes et orientées, se trouve ainsi partagé en classes d'équivalence; on notera $[V]$ la classe de la variété $V$.

On peut définir entre ces classes une loi d'addition commutative, en

posant $[V] + [V'] = [V \cup V']$; $-V$ désignant la variété $V$ dont on a renversé l'orientation, on aura $[V] + [-V] = 0$, où la classe 0 est la classe des variétés-bords; en effet, $V \cup (-V)$ est le bord du produit $V \times I$. L'ensemble des classes $[V]$ des variétés de dimension $k$ forme ainsi un groupe abélien qu'on dénotera $\Omega^k$ (groupe de cobordisme de dimension $k$).

Si $V$ est cobordante à $V'$, on vérifie immédiatement que, pour toute variété compacte orientée $W$, le produit $V \times W$ est cobordant à $V' \times W$; il en résulte qu'on peut définir sur les classes $[V]$ une structure multiplicative, anticommutative et distributive par rapport à l'addition. On désigne par $\Omega$ l'anneau qu'elle définit sur la somme directe des $\Omega^k$.

Si dans ces définitions, on abandonne toutes les conditions d'orientabilité, on définit: les variétés cobordantes mod 2, la classe d'équivalence mod 2, notée $[V]_2$, le groupe de cobordisme mod 2 de dimension $k$, noté $\mathfrak{N}^k$, et l'anneau $\mathfrak{N}$ des classes de cobordisme mod 2. Il est clair que dans l'anneau $\mathfrak{N}$ tout élément est d'ordre 2.

2. Les invariants des classes de cobordisme. Tous les critères connus pour qu'une variété soit une variété-bord donnent évidemment des critères pour que deux variétés soient cobordantes. Ainsi, le théorème V.11 de [27]: Si une variété  $V^{4k}$  orientée est une variété-bord, l'index  $\tau$  de la forme quadratique définie par le cup-produit sur  $H^{2k}(V^{4k})$  est nul, va donner:

Théorème IV.1. Si deux variétés $V, V'$, orientées, de dimension 4k, sont cobordantes, les formes quadratiques définies par le cup-produit sur $H^{2k}(V)$ resp. $H^{2k}(V')$ ont même index $\tau$.

(Rappelons que l'index d'une forme quadratique est ici l'excès du nombre des carrés positifs sur celui des carrés négatifs — en coefficients réels ou rationnels.)

Il est aisé de voir que cet invariant $\tau$ des classes de cobordisme de dimension $\equiv 0 \mod 4$ se comporte additivement, et multiplicativement, et définit ainsi un homomorphisme de l'anneau $\Omega$ dans $Z$.

Enfin un théorème de Pontrjagin [18], cité en [27], sur la nullité des nombres caractéristiques d'une variété-bord, donnera:

Théorème IV.2. Si deux variétés $V, V'$ orientées, de dimension $4k$, sont cobordantes, leurs nombres caractéristiques de Pontrjagin $\Pi(P^{4i})$ sont égaux.

Ces invariants se comportent additivement dans l'addition des classes; seul le nombre caractéristique associé à la classe de dimension maximum $P^{4k}$ se comporte multiplicativement. (Ceci résulte de la loi tensorielle

qui définit les classes de Pontrjagin de la structure fibrée sphérique joint de deux structures données).

Pour les classes de Stiefel-Whitney, on aura:

Théorème IV.3. Si deux variétés $V$, $V'$ de même dimension $k$ sont cobordantes mod 2, leurs nombres caractéristiques de Stiefel-Whitney sont égaux. Ici encore, seul le nombre associé à la classe de dimension maximum se comporte multiplicativement, alors que tous se comportent additivement. L'invariant associé n'est autre, comme il est connu, que la caractéristique d'Euler-Poincaré, réduite mod 2.

3. Applications différentiables d'une variété à bord. Définition. Soit $X^{n+1}$ une variété à bord compacte, de bord $V^n$, et $f$ une application différentiable de $X^{n+1}$ dans une variété $M^p$, contenant une sous-variété compacte $N^{p-q}$. On dira que l'application $f$ est $t$-régulière sur la sous-variété $N^{p-q}$, si les restrictions de $f$, d'une part à l'intérieur $X^{n+1} - V^n$, d'autre part, au bord $V^n$, sont séparément $t$-régulières (au sens de I. 3) sur $N^{p-q}$.

Image réciproque d'une application t-régulière. En vertu des propriétés générales des applications t-régulières énoncées en I.4, l'intersection par  $V^{n}$  de l'image réciproque  $A^{n+1-q}=F^{-1}(N^{p-q})$  est une sous-variété  $C^{n-q}$  de  $V^{n}$ ; de même, l'intersection de  $A^{n+1-q}$  par l'intérieur  $(X^{n+1}-V^{n})$  est une sous-variété  $A^{n+1-q}-C^{n}$  de dimension  $n+1-q$ . Nous allons montrer que  $A^{n+1-q}$  est une variété à bord, de bord  $C^{n}$ ; soit x un point de  $C^{n}, y=f(x)$  le point image de  $N^{p-q}, y_{1}, y_{2}, \ldots, y_{q}$  un système de q-fonctions coordonnées pour la q-boule géodésique normale en y à  $N^{p-q}$ . Soit  $(x_{1}, x_{2} \ldots x_{n}, t)$  un système de fonctions coordonnées d'une carte locale autour de x, où la dernière coordonnée t ne prend que des valeurs positives, t=0 étant l'équation du bord  $V^{n}$ . Dire que la restriction de f à  $V^{n}$  est t-régulière, c'est dire que l'application  $f(x_{1}, x_{2} \ldots x_{n}, 0) \to (y_{1}, y_{2}, \ldots y_{q})$  est de rang q au point x; il existe par suite un jacobien d'ordre  $q\left|\frac{\partial y_{r}}{\partial x_{i}}\right|$  non nul, pour  $x_{i}=0$, et pour t=0; par continuité, ce jacobien sera également non nul pour des valeurs assez petites des  $x_{i}$  et de t. C'est dire qu'on pourra trouver un voisinage de x admettant un système de coordonnées de la forme

$$
\left(y _ {1}, y _ {2} \dots y _ {q}, x _ {q + 1}, \dots , x _ {n}, t\right).
$$

Dans ce voisinage $A^{n+1-q}$ est défini par les équations linéaires: $y_{1}=y_{2}=y_{q}=0$, et $C^{n}$ en y ajoutant la relation $t=0$; c'est dire que $x$

admet dans $A^{n+1-q}$ un voisinage homéomorphe au demi-espace $R^{n+1-q}$ (de coordonnées $x_{q+1}, \ldots, x_n; t$) limité par un espace $R^{n-q}$ (de coordonnées $x_{q+1} \ldots x_n$) image de $C^n \cdot C.Q.F.D$.

Définition. Orientation induite sur une sous-variété.

Soit $f$ une application de la variété orientée $V^{n}$ dans $M^{p}$, $t$-régulière sur la sous-variété $N^{p-q}$, et soit $C^{n-q}$ la variété image réciproque de $N^{p-q}$. Supposons que le voisinage fibré normal à $N^{p-q}$ dans $M^{p}$ soit orientable; on peut alors définir dans un voisinage tubulaire normal de $N$ une classe «fondamentale» $U = \varphi^{*}(\omega) \in H^{q}(T;Z)$; le voisinage tubulaire de $C^{n-q}$ est également orientable, et on peut $y$ définir une classe $U$ image par $f^{*}$ de la classe $U$ de $H^{q}(T)$; on dira que la variété $C^{n-q}$ est munie de l'orientation induite de $V^{n}$ si son cycle fondamental ($C^{n-q}$) est donné, dans un voisinage tubulaire normal de $C^{n-q}$, par le cap-produit

$$
(C ^ {n - q}) = (V ^ {n}) \cap U
$$

$(V^{n})$ désignant la classe fondamentale de l'homologie (à supports fermés) de dimension $n$ du voisinage tubulaire ouvert de $C^{n}$, qui induit l'orientation donnée de $V^{n}$.

Supposons qu'on ait, comme précédemment, une application de la variété à bord $X^{n+1}$, orientée, compacte, de bord $V^n$, dans $M^p$, t-réguilière sur la sous-variété $N^{p-q}$. On suppose de plus la structure fibrée normale à $N^{p-q}$ orientable. Dans ces conditions, les images réciproques $A^{n+1-q} = f^{-1}(N^{p-q})$, et $C^n = A^{n+1-q} \cap V^n$ sont également orientables. On peut s'en assurer, par exemple, grâce au théorème de dualité de Whitney [32]; $V^n$ est supposée munie de l'orientation induite de l'orientation de $X^{n+1}: (V^n) = \partial(X^{n+1}, V^n)$, $\partial$ désignant l'opérateur de bord. Dans ces conditions, l'orientation induite sur $C^{n-q}$ par son immersion dans $V^n$ est l'orientation induite quand on considère $C^{n-q}$ comme bord de $A^{n+1-q}$, une fois qu'on a muni $A^{n+1-q}$ de l'orientation induite de $X^{n+1}$. Il suffit d'écrire: $V^n \cap U = \partial(X^{n+1}) \cap U = \partial(X^{n+1} \cap U)$. Nous allons maintenant démontrer le

Théorème IV.4. Soient $f, g$ deux applications de classe $C^{m}, m \geqslant n$, de la variété compacte orientée $V^{n}$ dans la variété $M^{p}$, $t$-régulières sur une sous-variété $N^{p-q}$ de $M^{p}$, compacte, à voisinage normal orientable; soient $W^{n-q} = f^{-1}(N^{p-q})$, $W' = g^{-1}(N^{p-q})$ les images réciproques de $N^{p-q}$, sous-variétés orientables qu'on munira de l'orientation induite de $V^{n}$. Si les applications $f$ et $g$ sont homotopes, alors les variétés $W^{n-q}$ et $W'^{n-q}$ sont cobordantes.

Il est clair qu'en abandonnant dans cet énoncé toutes les conditions d'orientation, on obtiendra: les images réciproques $f^{-1}(N^{p - q})$, $g^{-1}(N^{p - q})$ sont des variétés cobordantes mod 2.

Nous allons démontrer d'abord le lemme suivant, dont le principe m'a été suggéré par H. Whitney:

Lemme IV.5. Si deux applications f et g de classe  $C^{m}$  de la variété  $V^{n}$  dans  $M^{p}$  sont homotopes par une déformation continue, elles sont également homotopes par une déformation de classe  $C^{m}$ .

Soit $F: V \times I \to M^p$ l'application donnée, de classe $C^0$; on lui substitue une application $G: V \times I \to M^p$ ainsi définie: pour $t \in I$, on pose $G(V, t) = f = F(V, 0)$ pour $0 \leqslant t \leqslant \frac{1}{4}$; $G(V, t) = F\left(V, \frac{4t - 1}{2}\right)$ pour $\frac{1}{4} \leqslant t \leqslant \frac{3}{4}$; $G(V, t) = g$ pour $\frac{3}{4} \leqslant t \leqslant 1$. Munissons le produit $V \times I$ de la métrique riemannienne produit d'une métrique sur $V^n$ et de la métrique euclidienne de $I$. On régularise alors l'application $G$ par le procédé classique, en substituant à l'application $G$ sa moyenne sur des boules géodésiques de rayon $r$. Le rayon $r$ sera pris constant et $< \frac{1}{8}$ pour $\frac{1}{8} \leqslant t \leqslant \frac{7}{8}$; dans les tranches terminales $t < \frac{1}{8}$, resp. $\frac{7}{8} < t$, on prend $r$ variable décroissant avec $t$ (resp. $(1 - t)$), de classe $C^\infty$, et égal à 0 pour $t = 0$ et $t = 1$. Ainsi, la régularisation augmente de 1 la classe de différentiabilité de $G$ sur la tranche $\frac{1}{8} \leqslant t \leqslant \frac{7}{8}$, et elle ne la diminue pas sur $0 \leqslant t \leqslant \frac{1}{8}$ et $\frac{7}{8} \leqslant t \leqslant 1$; et les applications $f$ et $g$, restrictions de $G$ à $(V, 0)$ et $(V, 1)$ sont inchangées. En itérant le procédé, on obtiendra une application de $V \times I$ dans $M^p$ de classe $C^m$.

L'application obtenue $F: V \times I \to M^p$ de classe $C^m$ n'est peut-être pas $t$-régulière sur la sous-variété $N^{p-q}$; mais l'ensemble $H_0$ des homéomorphismes $h \in H$ du voisinage tubulaire $T$ de $N^{p-q}$, tels que $h \circ F$, restreint à l'intérieur de $V \times I$ ne soit pas $t$-régulière sur $N^{p-q}$ est maigre dans $H$; de même pour ceux des $h$ tels que la restriction de $h \circ F$ à $(V, 0) \cup (V, 1)$ ne soit pas $t$-régulière sur $N^{p-q}$; par suite, le théorème I.5 peut se généraliser aux applications de variétés à bord; et l'homéomorphisme $h$ peut être pris assez voisin de l'identité, pour que le théorème I.6 puisse s'appliquer aux restrictions $f$ et $g$ de $F$ à $(V, 0)$, resp. (V, 1). Posons $F' = h \circ F$, et soient $f'$ et $g'$ les restrictions de $F'$ à $(V, 0)$ et $(V, 1)$. A cause du théorème I.6, les variétés images réciproques $C^{n-q} = f'^{-1}(N^{p-q})$, $C'^{n-q} = g'^{-1}(N^{p-q})$ sont isotopes aux variétés $W^{n-q} = f^{-1}(N^{p-q})$, resp. $W'^{n-q} = g^{-1}(N^{p-q})$; cette isotopie conserve l'orientation induite, de sorte que $C^{n-q}$ et $C'^{n-q}$ forment le bord de la variété à bord $A = F'^{-1}(N^{p-q})$, munie de l'orientation induite. Par

suite, les variétés $C^{n-q}$, $C'^{n-q}$, donc $W^{n-q}$ et $W'^{n-q}$ sont cobordantes, et le théorème IV.4 est entièrement démontré.

4. Sous-variétés L-équivalentes. Au chapitre II.2, on a associé à toute sous-variété  $W^{n-k}$ , orientée, dans la variété orientable  $V^{n}$ , une application  $f: V^{n} \to M(SO(k))$ . Nous allons ici préciser cette définition.

Supposons la variété $V^n$ plongée dans un espace euclidien $R^{n+m}$; soit, en tout point $x$ de $W^{n-k}$, $H(x)$ le $k$-plan tangent en $x$ à $V^n$, et normal à $W^{n-k}$ (pour une métrique riemannienne arbitraire). Menons par l'origine $O$ de $R^{n+m}$ un $k$-plan parallèle à $H(x)$. On définit ainsi une application

$$
g: W ^ {n - k} \to \widehat {G} _ {k},
$$

$\widehat{G}_{k}$ désignant, comme précédemment, la grassmannienne des $k$-plans orientés. Soit $N$ un voisinage tubulaire de $W^{n-k}$ dans $V^n$. En associant à toute géodésique normale issue de $x \in W^{n-k}$, son vecteur tangent en $x$, on définit par parallélisme une application

$$
F: N \to A _ {S O (k)}
$$

telle que le diagramme:

$$
\begin{array}{c} N \xrightarrow {F} A _ {S O (k)} \\ p \Big \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ W ^ {n - k} \xrightarrow {g} \widehat {G} _ {k} \end{array}
$$

soit commutatif ($p$ et $p'$ désignant les fibrations canoniques en $k$-boules). Comme en II.2, l'application $F$ s'étend en une application

$$
f: V ^ {n} \rightarrow M (S O (k)).
$$

Si on remplace le plongement initial de $V^n$ dans $R^{n+m}$ par un autre plongement, ou la métrique par une autre métrique, l'application $f$ est remplacée par une application homotope. En effet, deux métriques riemanniennes sur une variété $V^n$ peuvent toujours être déformées continûment l'une sur l'autre ; il en résulte une isotopie entre les voisinages tubulaires $N$ et $N'$ associés à ces deux métriques, et par suite une homotopie entre les applications $F: N \to A_{SO(k)}$, donc entre les applications

$$
f: V ^ {n} \rightarrow M (S O (k)).
$$

Reste à montrer que la classe d'homotopie ne dépend pas du plongement initial de  $V^{n}$  dans  $R^{n+m}$ ; nous aurons besoin dans ce but du lemme suivant que nous rencontrerons encore par la suite:

Soit $Q^{n+1}$ une variété à bord, de bord $V^n$; soit $X^{k+1}$ une sous-variété à bord, plongée dans $Q^{n+1}$, dont le bord, plongé dans $V^n$, est une sous-variété $W^k$ de $V^n$; on suppose de plus qu'en tout point $x$ de $W^k$, le demi-espace $R^{k+1}$ des vecteurs tangents à $X^{k+1}$ est transverse au bord $V^n$, en ce sens que l'intersection de ce demi-espace $R^{k+1}$ par l'espace des vecteurs tangents à $V^n$ se réduit à l'espace des vecteurs tangents à $W^k$. Supposons donnée sur $Q^{n+1}$ une métrique riemannienne; elle permet de définir un voisinage normal de $V^n$ dans $Q^{n+1}$, de la forme $V^n \times I$, où les semi-droites de la forme $(x, t), t \in I$, sont des géodésiques normales à $V^n$. On peut alors montrer:

Lemme IV.5'. Après un homéomorphisme $\Phi$ de $Q^{n+1}$ sur lui-même, on peut toujours supposer que $X^{k+1}$ rencontre orthogonalement le bord $V^n$.

Cet homéomorphisme $\Phi$ de $Q^{n+1}$ est ainsi défini: il se réduit à l'identité à l'extérieur de $V^n \times I$; sur $V^n \times I$, il est l'image réciproque de l'homéomorphisme de $I$ sur lui-même défini par une fonction $t' = \varphi(t)$, telle que: $0 = \varphi(0)$; $1 = \varphi(1)$; $dt'/dt = +\infty$ pour $t = 0$, et $dt'/dt = 1$ pour $t = 1$.

On vérifie alors directement que tout vecteur tangent en $x$ à $\Phi(X^{k+1})$ est tangent au cylindre orthogonal à $V^n$, $W^k \times t'$, où $t'$ varie dans $I$.

Revenons maintenant à la variété $V^n$, plongée dans $R^{n+m}$ suivant deux plongements différents $i_0$ et $i_1$; si $m > n + 2$, on peut supposer les images $i_0(V^n), i_1(V^n)$ disjointes — au besoin après une translation convenable de $i_1$; on peut alors trouver, d'après un théorème de H. Whitney un plongement $i$ du produit $V^n \times I$ dans $R^{n+m}$, dont la restriction à $(V, 0)$, resp. $(V, 1)$, est précisément $i_0$, resp. $i_1$. La variété à bord plongée $i(V^n \times I)$ contient une sous-variété plongée de la forme $W^{n-k} \times I$, qui rencontre le bord de $V^n \times I$ transversalement. Supposons donnée sur $V^n \times I$ une métrique riemannienne; d'après le lemme, on peut supposer que $W^{n-k} \times I$ rencontre les bords $(V^n, 0)$ et $(V^n, 1)$ de $V^n \times I$ orthogonalement. Formons alors un voisinage tubulaire normal de $W^{n-k} \times I$ dans $V^n \times I$, soit $N$. Les intersections $N_0 = N \cap i_0(V^n), N_1 = N \cap i_1(V^n)$ ne sont autres que les voisinages tubulaires normaux associés à $i_0(W^{n-k})$, resp. $i_1(W^{n-k})$ plongées dans $i_0(V^n)$, resp. $i_1(V^n)$. Formons l'application canonique — par parallèlement.

$$
\boldsymbol {F}: N \rightarrow A _ {S O (k)}.
$$

Par extension, on obtient une application:

$$
\boldsymbol {F}: V ^ {n} \times \boldsymbol {I} \rightarrow M (S O (k))
$$

telle que les restrictions de $F$ à $(V^{n},0)$, resp. $(V^{n},1)$ sont précisément les applications canoniques $f_{0}$, resp. $f_{1}$ définies grâce aux plongements $i_{0}$, resp. $i_{1}$ de $V^{n}$. $F$ définit bien l'homotopie annoncée entre $f_{0}$ et $f_{1}$.

Définition. Sous-variétés L-équivalentes. Soient $W_0^{n-k}$, $W_1^{n-k}$ deux sous-variétés orientées de même dimension $n-k$ plongées dans la variété orientable $V^n$. On dira que $W_0^{n-k}$, $W_1^{n-k}$ sont L-équivalentes, s'il existe une variété à bord orientable $X^{n-k+1}$, de bord $W_0^{n-k} \cup W_1^{n-k}$, plongée dans le produit $V^n \times I$, de façon que:

$$
X ^ {n - k + 1} \cap (V ^ {n}, 0) = W _ {0} ^ {n - k}
$$

$$
X ^ {n - k + 1} \cap (V ^ {n}, 1) = W _ {1} ^ {n - k}
$$

et si $X^{n - k + 1}$ peut être munie d'une orientation telle que $\partial X^{n - k + 1} = W_1^{n - k} - W_0^{n - k}$.

Il résulte immédiatement de cette définition et du lemme IV.5' que deux sous-variétés $L$-équivalentes à une même troisième sont $L$-équivalentes entre elles. L'ensemble des sous-variétés de dimension $n - k$, orientées, de la variété $V^n$ se trouve ainsi partagé en classes de $L$-équivalence; on désignera par $L_{n-k}(V^n)$ l'ensemble de ces classes.

Si, dans les définitions précédentes, on abandonne toutes les conditions d'orientabilité, on définit les sous-variétés $L$-équivalentes mod 2, et les ensembles $L_{n-k}(V^n;Z_2)$ des classes de $L$-équivalence mod 2.

Il est clair que deux sous-variétés $L$-équivalentes sont à la fois homologues et cobordantes; si deux sous-variétés $W_0, W_1$ constituent dans $V^n$ le bord d'une même sous-variété à bord $X$, alors $W_0$ et $W_1$ sont $L$-équivalentes.

Il existe une application évidente de l'ensemble $L_{n-k}(V^n)$ dans le groupe $H_{n-k}(V^n; Z)$; les classes images sont les classes réalisables par des sous-variétés ; le «noyau» de cette application est en général non nul, comme nous en verrons des exemples. Il est naturel de se demander si l'on peut munir $L_{n-k}(V^n)$ d'une structure de groupe, compatible avec l'application précédente. Il en est ainsi dans un cas au moins, lorsque $n - k < n/2 - 1$. En effet, en ce cas, on peut définir entre classes de $L$-équivalence une loi d'addition, par simple réunion de sous-variétés représentant les classes ; en effet, ces représentants peuvent toujours, si $n - k < n/2$, être supposés disjoints et, pour $n - k < n/2 - 1$, la $L$-classe ainsi définie ne dépend pas du plongement choisi des deux sous-variétés. Par ailleurs, la somme $[W] + [-W]$ donne bien la classe nulle, car on peut toujours — localement — plonger le produit $W \times I$ dans un voisinage tubulaire normal de $W$.

A toute sous-variété $W^{n-k}$ de $V^n$ correspond une classe d'applications de $V^n$ dans $M(SO(k))$; on démontre sans difficulté que si $W$ et $W'$ sont $L$-équivalentes, les applications associées $f: V^n \to M(SO(k))$ sont homotopes.

Si, en effet, $W_0$ et $W_1$ sont $L$-équivalentes, il existe une sous-variété à bord $X$ plongée dans $V^n \times I$, dont le bord se compose de $W_0$ plongée dans $(V^n, 0)$ et $W_1$ plongée dans $(V^n, 1)$. On peut toujours supposer, à cause du lemme IV 5', que $X$ rencontre orthogonalement les variétés bords $(V^n, 0)$ et $(V^n, 1)$. On forme alors un voisinage tubulaire normal $Q$ de $X$ dans $V^n \times I$, et l'application $F$ associée $F: Q \to A_{SO(k)}$. Par extension on obtient une application $F_1: V^n \times I \to M(SO(k))$, qui définit précisément l'homotopie annoncée entre les applications canoniques:

$$
\boldsymbol {F} \mid (V ^ {n}, 0) = f _ {0}, \quad \boldsymbol {F} \mid (V ^ {n}, 1) = f _ {1} \quad \text { associées   resp.   à } W _ {0} \text { et } W _ {1}.
$$

Ceci définit une application $J$ de l'ensemble $L_{n-k}(V^n)$ des classes de $L$-équivalence dans l'ensemble $C^k(V)$ des classes d'homotopie d'applications $f: V^n \to M(SO(k))$. L'application $J$ est biunivoque: si, en effet, deux sous-variétés $W_0, W_1$ donnent lieu à des applications

$$
f _ {0}, f _ {1}: V ^ {n} \rightarrow M (S O (k))
$$

homotopes, le théorème IV.4 montre qu'on peut régulariser l'application d'homotopie $F: V^n \times I \to M(SO(k))$, de telle façon que les images réciproques $f_0^{-1}(\widehat{G}_k) = W_0$ et $f_1^{-1}(\widehat{G}_k) = W_1$ forment — après éventuellement une isotopie qui est une L-équivalence — le bord d'une variété à bord $A = F^{-1}(\widehat{G}_k)$.

On peut remarquer que $J$ applique la classe des variétés $L$-équivalentes à 0 sur la classe nulle des applications $f: V^n \to M(SO(k))$ inessentielles. Si $k > (n/2) + 1$, l'ensemble $C^k(V)$ des applications de $V$ dans $M(SO(k))$, espace asphérique jusqu'en dimension $k$, peut être muni d'une structure de groupe abélien, conformément à la théorie générale de la cohomotopie$^{11}$). Il est d'une vérification presque immédiate que l'application $J$ est alors un homomorphisme; il suffit d'expliciter la loi de groupe dans $C^k(V)$: on vérifiera que l'image réciproque $(f + g)^{-1}(\widehat{G}_k)$ par l'application somme

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{11}$  Les groupes de cohomotopie ont été étudiés par E. Spanier (Ann. of Math., 50, 1949, pp. 203—45) dans le cas des sphères; leur généralisation aux espaces asphériques, ici mentionnée, doit faire l'objet d'un travail de E. Spanier, N. E. Steenrod et J. H. C. Whitehead, à paraître ultérieurement. La démonstration esquissée plus bas est aisée à expliciter dans le cas typique de la sphère; et la généralisation n'introduit aucun élément nouveau de difficulté.</span></small>

est à une L-équivalence près la réunion des images réciproques  $f^{-1}(\widehat{G}_{k})$  et  $g^{-1}(\widehat{G}_{k})$ .

Nous allons maintenant montrer que l'application $J$ applique $L_{n - k}(V^n)$ sur $C^k (V^n)$.

Soit $c$ une classe de $C^{k}(V)$, et $h$ une application de la classe $c$; d'après le théorème I.5, on peut supposer l'application $h$ t-régulière sur la grassmannienne $\widehat{G}_{k}$ plongée dans $M(SO(k))$. Soit $W^{n-k}=h^{-1}(\widehat{G}_{k})$ l'image réciproque de $\widehat{G}_{k}$, et $N$ un voisinage tubulaire normal de $W^{n-k}$ dans $V^{n}$; on peut de plus supposer $h$ normalisée, de façon que $h$ applique l'intérieur de $N$ sur $M(SO(k))-a$, $k$-boule ouverte sur $k$-boule ouverte, et que, de plus, $h$ applique le complémentaire $Q=V^{n}-N$ sur le point $a$. Désignons alors par $i:V^{n}\to R^{p}$ un plongement arbitraire de $V^{n}$ dans $R^{p}$, par: $g:W^{n-k}\to\widehat{G}_{k}$, $F:N\to A_{SO(k)}$, $f:V^{n}\to M(SO(k))$, les applications qui lui sont canoniquement associées par parallélisme. Or, les applications:

$$
h: W ^ {n - k} \rightarrow \widehat {G} _ {k} (\text {restriction   de } h) \text { et } g: W ^ {n - k} \rightarrow \widehat {G} _ {k}
$$

induisent toutes deux l'espace fibré des vecteurs normaux à $W^{n-k}$ dans $V^n$; en raison du théorème de classification des espaces fibrés, ces deux applications sont homotopes. Or, si nous écrivons à nouveau le diagramme commutatif:

$$
\begin{array}{c} N \xrightarrow {h} A _ {S O (k)} \\ \Big \downarrow \\ W ^ {n - k} \xrightarrow {h} \widehat {G} _ {\kappa} \end{array}
$$

nous en déduisons, par relèvement de l'homotopie  $h \simeq g$ , qu'il existe une application  $h_{1}$ , homotope à h, telle que:

$$
\begin{array}{c} N \xrightarrow {h _ {1}} A _ {S O (k)} \\ \Big \downarrow \\ W ^ {n - k} \xrightarrow {g} \widehat {G} _ {k} \end{array}
$$

C'est dire que la nouvelle application $h_1$ ne diffère de l'application $F$ que par un isomorphisme $\alpha$ du voisinage tubulaire $N$ sur lui-même. On aura: $h_1 = F \circ \alpha$ (restreint à $N$).

Or, je dis qu'il est possible de définir (au besoin en augmentant la dimension de l'espace euclidien ambiant) un nouveau plongement $i'$ de $V^n$, tel que, pour la restriction à $N$, on ait:

$$
i ^ {\prime} = \alpha \circ i.
$$

En effet, on peut démontrer le lemme:

Lemme. Soit $Q$ une variété à bord, de bord $T$; supposons donné un plongement i d'un voisinage de $T$ (de la forme $T \times I$) dans un espace $R^{p}$; il est possible de prolonger ce plongement à toute la variété $Q$ dans un espace $R^{p+q}$, où l'entier $q$ est assez grand.

En effet, soient $y_1, y_2 \ldots y_p$ les $p$ fonctions coordonnées de $R^p$; dans un voisinage $U$ de $T \times I$, les fonctions $y_i$, arbitrairement prolongées à tout $Q$, séparent les points; prenons ensuite un nombre suffisant de fonctions $(x_1, x_2 \ldots x_q)$, nulles sur $T \times I$, pour séparer tous les points de $Q - U$ (il suffit d'en prendre au plus $2n + 1$, $n$ dimension de $Q$). L'ensemble des fonctions $y_i, x_j$ définit alors le plongement cherché de $Q$ dans $R^{p+q}$.

On appliquera ce lemme au complémentaire $Q = V^{n} - N$; le plongement donné sur le bord $T$ de $N$ et un voisinage de $T$ de la forme $T \times I$ sera donné par: $i' = \alpha \circ i$.

Dans ces conditions, on vérifie immédiatement que l'application $F'$ canoniquement attachée à l'immersion $i': F': N \to A_{SO(k)}$ s'identifie à l'application $h_1$; par extension, on en déduit que l'application

$$
f _ {1}: V ^ {n} \rightarrow M (S O (k))
$$

déduite de $h_1$ s'identifie à l'application canonique associée à l'immersion $i'$. Or, comme $h_1: N \to A(SO(k))$ était homotope à la restriction de $h$ à $N$, l'application «étendue» $f_1$ est homotope à $h$. (Car on a supposé $h$ «normalisée» de telle façon que $h(Q)$ soit le point $a$ compactifiant de $M(SO(k))$.) Nous avons ainsi démontré:

Théorème IV.6. L'ensemble $L_{n-k}(V^n)$ des classes de L-équivalence d'une variété $V^n$ s'identifie à l'ensemble $C^k(V)$ des classes d'applications de $V^n$ dans $M(SO(k))$; si $k > (n/2) + 1$, cette identification est compatible avec la structure de groupe abélien donnée sur $L_{n-k}$ et $C^k(V)$. On a un théorème analogue pour $L_{n-k}(V^n; Z_2)$, le complexe $M(O(k))$ remplaçant $M(SO(k))$.

Applications. Le nombre maximum de $L$-classes contenues dans une classe d'homologie $z$ correspondant à la classe $u \in H^{k}(V^{n}; Z)$ est donné par le nombre des classes d'applications du complexe d'Eilenberg-Mac Lane $K(Z, k)$ dans $M(SO(k))$, telles que $f^{*}(U) = \iota$. Comme $M(SO(1))$ et $M(SO(2))$ s'identifient à $K(Z, 1)$ et $K(Z, 2)$, on obtient:

Deux sous-variétés, orientées, de dimension n - 1 ou n - 2, de la variété orientable  $V^{n}$  sont L-équivalentes dès qu'elles sont homologues.

Corollaire: Toute sous-variété de dimension n - 2 homologue à 0 est une variété-bord. (Résultat trivial pour n - 1.)

On a un résultat semblable pour les sous-variétés de dimension $n - 1$ en homologie mod 2.

Enfin, on a vu, au chap. II. (Th. II. 16), que le second groupe d'homotopie non nul de $M(SO(k))$ apparaît en dimension $k + 4$; on en déduit que deux applications de $V^n$ dans $M(SO(k))$ qui sont homotopes sur le $k$-squelette de $V^n$ le sont également sur le $(k + 3^{\text{ième}})$. Donc: Deux sous-variétés orientées de dimension $\leqslant 3$, homologues, sont $L$-équivalentes.

5. Un théorème fondamental. Nous allons appliquer le théorème précédent au cas où la variété  $V^{n}$  est la sphère  $S^{n}$ . Enonçons le

Lemme IV.7. Le groupe $L_k(S^n)$ des classes de $L$-équivalence pour la sphère $S^n$ s'identifie, pour $n > 2k + 2$, au groupe $\Omega^k$ des classes de cobordisme.

Il existe une application canonique de $L_k(S^n)$ dans $\Omega^k$, obtenue en assignant à tout représentant d'une $L$-classe sa classe de cobordisme; cette application est évidemment un homomorphisme pour la structure de groupe, car, dans les deux groupes, l'addition est définie par la réunion des représentants. Cet homomorphisme applique $L_k(S^n)$ sur $\Omega^k$; soit $c$ une classe de $\Omega^k$, $W^k$ une variété de la classe $c$. $W^k$ peut être plongée dans $R^n$ pour $n \geqslant 2k + 2$, donc dans $S^n$, et par suite $c$ est l'image d'une $L$-classe de $S^n$. Reste à montrer que le noyau de cet homomorphisme est nul; c'est-à-dire: si deux variétés $W^k$, $W'^k$ plongées dans $S^n$ sont cobordantes, alors elles y sont $L$-équivalentes. Soit $X^{k+1}$ une variété à bord, telle que $\partial X^{k+1} = W'^k - W^k$. On peut toujours plonger $X^{k+1}$ dans $R^n$, si $n > 2k + 2$. Définissons sur $X^{k+1}$ une fonction (de classe $C^\infty$) $t$, comprise entre 0 et 1, telle que les équations $t = 0$, resp. $t = 1$, définissent $W^k$, resp. $W'^k$. Par compactification des $(R^n, t)$ en $(S^n, t)$, on obtient bien le plongement de $X$ dans $S^n \times I$ qui définit la $L$-équivalence. Si l'on remarque en plus que deux plongements arbitraires de $W^k$ dans $S^n$, sont toujours, pour $n \geqslant 2k + 2$, $L$-équivalents, on a bien démontré que la correspondance entre $L_k(V^n)$ et $\Omega^k$ est un isomorphisme.

Nous pouvons maintenant énoncer le théorème essentiel de ce chapitre:

Théorème IV.8. Les groupes de cobordisme $\Omega^{k}$ et de cobordisme mod $2\mathfrak{N}^{k}$ sont resp. isomorphes aux groupes d'homotopie stables $\pi_{n+k}(M(SO(n)))$, resp. $\pi_{n+k}(M(O(n)))$.

Il suffit d'appliquer le théorème IV.6 au cas où  $V^{n}$  est la sphère  $S^{n}$ , en tenant compte de l'isomorphisme  $L_{k}(S^{n}) \simeq \Omega^{k}$  du lemme IV.7. On doit simplement remarquer, ce qui est un résultat classique en théorie de la cohomotopie, que l'ensemble des classes d'applications

$$
f: S ^ {n + k} \rightarrow M (S O (n)),
$$

muni de sa structure de groupe de cohomotopie est isomorphe au groupe d'homotopie $\pi_{n+k}(M(SO(n)))$.

6. Les groupes $\mathfrak{N}^k$ des classes mod 2. Au chapitre II, on a déterminé les groupes d'homotopie stables $\pi_{n+k}(M(O(n)))$; on a vu (théorème II.10) que l'espace $M(O(n))$ a dans les dimensions $< 2n$, même type d'homotopie qu'un produit $Y$ de complexes d'Eilenberg-Mac Lane:

$$
Y = K \left(Z _ {2}, n\right) \times K \left(Z _ {2}, n + 2\right) \times \dots \left(K \left(Z _ {2}, n + h\right)\right) ^ {d (h)} \times \dots h \leqslant n.
$$

où $d(h)$ est le nombre des partitions non-dyadiques de $h$, c'est-à-dire des partitions qui ne contiennent aucun entier de la forme $2^{m} - 1$. Donc:

Théorème IV.9. Pour toute dimension $k$, le groupe $\mathfrak{N}^k$ est isomorphe à la somme directe de $d(k)$ groupes isomorphes à $Z_2$, ou $d(k)$ désigne le nombre des partitions non-dyadiques de l'entier $k$.

Ceci détermine la structure additive des $\mathfrak{N}^{k}$.

Il résulte du théorème II.10 que toute application de $S^{n+k}, n > k$, dans $M(O(n))$, qui est homologiquement nulle (mod 2), est homotopiquement nulle. Ce résultat peut être précisé comme suit: pour toute partition non-dyadique $\omega$ de $k$, on a défini une application

$$
F _ {\omega}: M (O (n)) \rightarrow K (Z _ {2}, k + n),
$$

telle que  $F_{\omega}^{*}(\iota)=X_{\omega}$ , où  $X_{\omega}$  désigne la classe de  $H^{k+n}(M(O(n)))$  définie par la fonction symétrique:

$$
\Sigma (t _ {1}) ^ {a _ {1} + 1} (t _ {2}) ^ {a _ {2} + 1} \dots (t _ {r}) ^ {a _ {r} + 1} t _ {r + 1} \dots t _ {n}
$$

où les entiers  $(a_{i})$  constituent la partition non-dyadique  $\omega$  de k. Po- sons, dans la cohomologie  $H^{k}(G_{k};Z_{2})$ :

$$
Y _ {\omega} = \Sigma (t _ {1}) ^ {a _ {1}} (t _ {2}) ^ {a _ {2}} \dots (t _ {r}) ^ {a _ {r}}.
$$

On a alors, avec les notations de II.2:

$$
X _ {\omega} = \varphi_ {G} ^ {*} (Y _ {\omega}).
$$

Désignons par $f_{\omega^1}$ une base de $\pi_{n+k}(M(O(n)))$, telle que, par dualité avec les $F_{\omega}$, on ait:

$f_{\omega^{1}}^{*}F_{\omega}(\iota)=\delta_{\omega^{1}}^{\omega}(s), s$ classe fondamentale de $H^{k+n}(S^{k+n};Z_{2})$ (1) et où $\delta_{\omega^{1}}^{\omega}$ est le symbole de Kronecker avec sa signification classique, les partitions $\omega$ remplaçant les entiers pour indices.

Les applications $f_{\omega^1}$ peuvent être supposées $t$-régulières sur la grassmannienne $G_n$ contenue dans $M(O(n))$; soit $V_{\omega^1}$ une image réciproque de $G_n$ pour $f_{\omega^1}$; formons alors un voisinage tubulaire normal de $V$ dans $S^{n+k}$, et soit $\varphi^*$ l'isomorphisme ($\varphi^*$) associé; désignons par $Y_\omega'$ l'image de la classe $Y_\omega$ dans la cohomologie de $V$ par l'application $f_{\omega^1}$, restreinte à $V_{\omega^1}$; la classe $Y_\omega'$ s'exprime alors en fonction des classes $\overline{W}_i$, classes caractéristiques de Stiefel-Whitney de la structure fibrée normale à $V$ dans $S^{n+k}$. D'après le diagramme commutatif (1) de II.2, on aura:

$$
\varphi^ {*} (Y _ {\omega} ^ {\prime}) = \varphi^ {*} f _ {\omega^ {1}} ^ {*} (Y _ {\omega}) = f _ {\omega^ {1}} ^ {*} \varphi_ {G} ^ {*} (Y _ {\omega}) = f _ {\omega^ {1}} ^ {*} (X _ {\omega}) = \delta_ {\omega^ {1}} ^ {\omega} (s) \text {   d'après   (1)   }\tag{2}
$$

Appelons nombres caractéristiques normaux les valeurs prises par tout polynôme en $\overline{W}_{i}$, de poids total $k$, sur la classe fondamentale de $V$. La relation (2) exprime que si une application $f: S^{n+k} \to M(O(n))$ n'est pas homotopiquement nulle, il existe une combinaison linéaire non triviale des $X_{\omega}$ dont l'image par $f^{*}$ n'est pas nulle dans $H^{*}(S^{n+k})$; par suite, un au moins des nombres caractéristiques normaux de $V$ n'est pas nul. Ceci nous permet d'énoncer la réciproque du théorème de Pontrjagin:

Théorème IV.10. Si une variété  $V^{k}$  a tous ses nombres caractéristiques de Stiefel-Whitney nuls, c'est une variété-bord (mod 2).

En effet, si tous les nombres caractéristiques définis à partir des classes $W_{i}$ de la structure tangente sont nuls, il en va de même des nombres caractéristiques normaux définis à partir des classes $\overline{W}_{r}$; en effet, d'après les relations de Whitney

$$
\Sigma_ {i} W _ {i} \cdot \overline {{{W}}} _ {r - i} = 0
$$

les $\overline{W}_{r}$ sont des polynômes par rapport aux $W_{i}$.

Corollaire IV.11. Si les nombres caractéristiques de Stiefel-Whitney de deux variétés $V$, $V'$ sont égaux, $V$ et $V'$ sont cobordantes mod 2.

Remarque. Ce résultat implique que, dans le groupe — isomorphe à $H^{k}(G_{n})$ — des nombres caractéristiques (tangents) d'une variété $V^{k}$ de dimension $k$, il y en a exactement $d(k)$ qui sont linéairement indépendants; on peut vérifier ce résultat pour les petites dimensions ($k \leqslant 6$), en tenant compte des relations de Wu Wen-Tsün [33] qui lient

les classes $W_{i}$ de la structure tangente d'une variété. La question se trouve ainsi posée de savoir si les relations de Wu donnent toutes les relations liant les $W_{i}$ de la structure des vecteurs tangents à une variété.

7. Structure multiplicative des groupes $\mathfrak{N}^k$. Posons $k = r + s$; soit $\omega_1$ une partition non-dyadique de $r$, $\omega_2$ une partition non-dyadique de $s$; la réunion $(\omega_1, \omega_2)$ est une partition non-dyadique de $k$.

On a défini plus haut la variété $V_{\omega}^{k}$; rappelons que tous les nombres caractéristiques normaux $Y_{\omega_1}$, de $V_{\omega}^{k}$ sont nuls, à l'exception du nombre $Y_{\omega}$. On va montrer que la variété $V^{k}$ est cobordante mod 2 au produit des variétés: $V_{\omega_1}^r \times V_{\omega_2}^s$. Il suffira pour cela de montrer, d'après le corollaire IV.11, que tous leurs nombres caractéristiques de Stiefel-Whitney sont égaux.

Or cela résulte immédiatement de la formule suivante, que nous allons établir:
$X_{\text{max}} = \sum_{n=1}^{N} (X_{n}) / (X_{n-1})$

$$
Y _ {\omega} = \sum_ {(\omega_ {1}, \omega_ {2})} (Y _ {\omega_ {1}}) (Y _ {\omega_ {2}})\tag{3}
$$

où $(\omega_{1},\omega_{2})$ parcourt toutes les décompositions possibles de la partition $\omega$ de $k$ en une partition $\omega_{1}$ de $r$ et une partition $\omega_{2}$ de $s$. Il résulte en effet, de (3), que tous les nombres $Y_{\omega}$, du produit $V_{\omega_1} \times V_{\omega_2}$ sont nuls, à l'exception de $Y_{\omega}$, où $\omega = (\omega_{1},\omega_{2})$.

Rappelons que la structure fibrée normale du produit $V_{\omega_1}^r \times V_{\omega_2}^s$ est le joint des structures fibrées normales de $V_{\omega_1}^r$, et de $V_{\omega_2}^s$. Désignons par $\overline{W}_i$ les classes normales de la variété-produit, par $U_i$ celles du facteur $V_1^r$, par $V_i$ celles du facteur $V_2^s$. Le théorème de «dualité» de Whitney s'exprime par la formule symbolique:

$$
\Sigma_ {i} \overline {{{W}}} _ {i} t ^ {i} = \Sigma_ {i} U _ {i} t ^ {i} \times \Sigma_ {j} V _ {j} t ^ {j}.
$$

Désignons par $u_i$, resp. $v_j$ les $r$ racines symboliques du premier (resp. les $s$ racines du second) facteur. Si dans l'expression

$$
Y _ {\omega} = \sum (t _ {1}) ^ {a _ {1}} (t _ {2}) ^ {a _ {2}} \dots (t _ {q}) ^ {a _ {q}}
$$

on substitue aux racines $t_i$ l'ensemble des $k$ racines $u_i$ et $v_j$, on doit tout d'abord annuler tous les termes pour lesquels le degré total en $(u_i)$ est $\neq r$, et le degré total en $(v_j)$ est $\neq s$, ceci pour des raisons de degré; les termes restants peuvent se grouper sous la forme:

$$
Y _ {\omega} = \sum_ {(\omega_ {1}, \omega_ {2})} \sum (u _ {1}) ^ {a _ {1}} (u _ {2}) ^ {a _ {2}}.. (u _ {m}) ^ {a _ {m}}. \sum (v _ {1}) ^ {b _ {1}} (v _ {2}) ^ {b _ {2}} (v _ {n}) ^ {b _ {n}}\tag{4}
$$

où $\omega_{1}$ désigne la partition $a_{1}, a_{2} \ldots a_{q}$ de $r$, extraite de $\omega$, et $\omega_{2}$ désigne la partition $(b_{1}, b_{2}, b_{n})$ de $s$, formée des entiers restants. Le premier $\Sigma$ s'effectue suivant toutes les décompositions possibles de la par-

tition $\omega$ en une partition $\omega_{1}$ de $r$ et une partition $\omega_{2}$ de $s$; les deux autres $\Sigma$ sont des $\Sigma$ de symétrisation, avec la convention classique en pareil cas. Par ailleurs, si $\omega$ se décompose en $(\omega_{1},\omega_{2})$, je dis que cette décomposition ne figure qu'une seule fois dans l'expression (4), même si cette décomposition peut être obtenue de plusieurs manières différentes à partir de $\omega$. Supposons en effet que la décomposition $(\omega_{1},\omega_{2})$ puisse s'obtenir de deux manières différentes à partir de $\omega$, c'est-à-dire qu'il existe une permutation $P$ des $k$ variables $(t_{i})$, qui, dans le monôme typique

$$
(t _ {1}) ^ {a _ {1}} (t _ {2}) ^ {a _ {2}} \dots (t _ {m}) ^ {a _ {m}} (t _ {m + 1}) ^ {b _ {1}} \dots (t _ {k}) ^ {b _ {n}}
$$

transforme la décomposition  $(\omega_{1}, \omega_{2})$  en une décomposition isomorphe. Alors la permutation P transforme le monôme typique en lui-même, et par suite, la permutation P, inessentielle, n'intervient pas dans la symétrisation. La formule (4) s'identifie donc bien à la formule (3) à démontrer. Par suite, si la partition non-dyadique  $\omega$  de k se décompose en une partition  $\omega_{1}$  de r, et une partition  $\omega_{2}$  de s, on a, pour les classes des variétés  $V_{\omega}^{k}$  correspondantes:

$$
[ V _ {\omega} ^ {k} ] = [ V _ {\omega_ {1}} ^ {r} ] \times [ V _ {\omega_ {2}} ^ {s} ]\tag{5}
$$

Les seules classes $[V_{\omega}^{k}]$ non décomposables sont par suite les classes $[V_{(k)}^{k}]$, où $(k)$ est la partition de $k$ constituée de l'entier $k$ lui-même ($k$ non de la forme $2^{m}-1$). Toute autre classe se met — univoquement — sous forme d'une somme de produits de ces classes indécomposables. Ceci nous permet d'énoncer:

Théorème IV.12. L'anneau N des groupes  $N^{k}$  est isomorphe à une algèbre de polynômes sur le corps  $Z_{2}$ , admettant un générateur  $[V_{(k)}^{k}]$  pour toute dimension k qui n'est pas de la forme  $2^{m}-1$ .

Corollaire: Si V et V' ne sont pas des bords (mod 2), la variété produit V × V' n'est pas un bord (mod 2).

Les générateurs pour les petites dimensions.

Le premier générateur apparaît pour $k=2$; le nombre caractéristique correspondant est $\Sigma(t^{2})=(\Sigma t)^{2}=(\overline{W}_{1})^{2}=(W_{1})^{2}$; un représentant de la classe $[V_{(2)}^{2}]$ est donné par le plan projectif réel $PR(2)$.

$$
k = 3, \mathfrak {N} ^ {3} = 0
$$

Pour $k = 4$, on a un nouveau générateur, de nombre caractéristique normal $(t)^{4} = (\overline{W}_{1})^{4} = (W_{1})^{4}$; il est représenté par la somme $PR(4) + (PR(2))^{2}$; le groupe $\mathfrak{N}^{4}$ est isomorphe à $Z_{2} + Z_{2}$; on notera que le plan projectif

complexe $PC(2)$ est cobordant mod 2 au carré du plan projectif réel $PR(2)$.

Pour $k = 5, \mathfrak{N}^5$, isomorphe à $Z_2$, est engendré par le générateur $[V_{(5)}]$. Le nombre caractéristique tangent correspondant est $W_2 \cdot W_3$; la classe est représentée par une variété fibrée sur $S^1$, de fibre $PC(2)$, qui a été construite par Wu Wen-Tsün [33].

Pour $k = 6$, $\mathfrak{N}^6$ est isomorphe à $(Z_2)^3$; deux classes décomposables: $(PR(2))^3$ et $PR(4) \times PR(2)$; la classe primitive $[V_{(6)}]$ admet pour nombre caractéristique normal

$$
\Sigma (t ^ {6}) = (\Sigma (t) ^ {3}) ^ {2} = (\overline {{W}} _ {3}) ^ {2} + (\overline {{W}} _ {2} \cdot \overline {{W}} _ {1}) ^ {2} + (\overline {{W}} _ {1}) ^ {6}.
$$

On vérifie aisément qu'un représentant de cette classe est donné par l'espace projectif $PR(6)$.

Pour $k = 7$, comme $k = 2^3 - 1$, toute classe est décomposable
$\mathfrak{N}^7 = Z_2$, de générateur $[V_{(5)}] \times [V_{(2)}]$.

Pour $k = 8$. on a une classe primitive, dont le nombre caractéristique associé est $(W_1)^8$; tout élément de cette classe $[V_{(8)}]$ est cobordant mod 2 à l'espace projectif $PR(8)$, modulo des éléments décomposables qu'on pourrait expliciter sans difficulté.

De façon plus générale, on peut montrer:

Pour toute dimension paire $n=2r$, la classe primitive $[V_{(n)}^{n}]$ s'obtient en ajoutant à la classe $[PR(n)]$ de l'espace projectif réel certaines classes décomposables convenablement choisies.

Il suffit de démontrer que le nombre caractéristique normal $\Sigma(\overline{t_{i}})^{n}$ n'est pas nul pour $PR(n)$ (on désigne ici par $\overline{t_{i}}$ les variables $\overline{t_{i}}$ associées symboliquement aux classes normales $\overline{W_{i}}$); si, en effet, outre $\Sigma(\overline{t_{i}})^{n}$, d'autres nombres caractéristiques normaux tels que

$$
\Sigma (\bar {t} _ {1}) ^ {a _ {1}} (\bar {t} _ {2}) ^ {a _ {2}} \dots (\bar {t} _ {m}) ^ {a _ {m}},
$$

où les $a_{i}$ forment une partition non dyadique $\omega$ de $n$, ne sont pas nuls pour $PR(n)$, on formera la somme $PR(n)+\bigcup_{i}V_{c_{i}}^{n}$; pour cette variété, tous les nombres caractéristiques normaux définis par des partitions non-dyadiques de $n$ sont nuls, à la seule exception de $\Sigma(t)^{n}$; cette variété est donc un représentant de la classe primitive $[V_{(n)}^{n}]$.

Et, d'après la formule (5), toutes les classes  $[V_{\omega_{i}}^{n}]$ ,  $\omega_{i} \neq (n)$ , sont décomposables.

Or, pour toute variété $V^n$, le nombre caractéristique normal $\Sigma(t)^n$ est égal au nombre caractéristique tangent $\Sigma(t^n)$. En effet, d'après la formule de dualité de Whitney [32], les variables $t$ de la structure tangente, et les $\overline{t}_i$ de la structure normale sont liées par la relation:

$$
\Sigma W _ {i} t ^ {i} \times \Sigma \overline {{{W}}} _ {j} \overline {{{t}}} ^ {j} = 1
$$

ce qui signifie que toute fonction symétrique de l'ensemble des $t_i$ et des $\bar{t}_j$, non constante, est nulle. Par suite $\Sigma(t_i)^n + \Sigma(\bar{t}_j)^n = 0$.

Or, si l'on désigne par $d$ le générateur de $H^{1}\big(PR(n);Z_{2}\big)$, le polynôme de Stiefel-Whitney de $PR(n)$ s'écrit:

$$
1 + \left\{ \begin{array}{c} n + 1 \\ 1 \end{array} \right\} d \cdot t + \left\{ \begin{array}{c} n + 1 \\ 2 \end{array} \right\} d ^ {2}, t ^ {2} +.. + \left\{ \begin{array}{c} n + 1 \\ p \end{array} \right\} d ^ {p}, t ^ {p} +.. + \left\{ \begin{array}{c} n + 1 \\ n \end{array} \right\} d ^ {n} \cdot t ^ {n}
$$

Ceci peut s'écrire, symboliquement: (comme $d^{n+1} = 0$) $(1 + d \cdot t)^{n+1}$.

On peut donc considérer que ce polynôme admet  $n + 1$  racines toutes égales à t = -1/d; comme n est pair, la somme  $\Sigma(t_{i})^{n}$  est égale à  $1/(d)^{n}$  et le nombre caractéristique associé est égal à 1.

J'ignore par contre s'il existe une généralisation convenable de la construction de Wu qui fournisse les générateurs de dimension impaire.

8. Les groupes $\Omega^{k}$. Les groupes d'homotopie stables

$$
\pi_ {n + k} (M (S O (n))
$$

ne sont pas connus en général ; pour les petites valeurs de k, on a seulement le résultat du théorème II.16, qui donne:

Théorème IV.13. Pour les valeurs de $k<8$, les groupes $\Omega^{k}$ sont:

$$
\Omega^ {0} = Z; \Omega^ {1} = \Omega^ {2} = \Omega^ {3} = 0; \Omega^ {4} = Z; \Omega^ {5} = Z _ {2}; \Omega^ {6} = \Omega^ {7} = 0.
$$

Résultat trivial pour $k \leqslant 2$; les résultats concernant $\Omega^{3}$ et $\Omega^{4}$ ont été annoncés par Rokhlin [19–20]. Le générateur de $\Omega^{4}$ est représenté par le plan projectif complexe $PC(2)$; ceci entraîne en particulier:

Corollaire IV.14. Le nombre caractéristique  $P^{4}$  de Pontrjagin d'une variété orientée de dimension 4 est égal à  $3\tau$ , ou  $\tau$  désigne l'index de la forme quadratique définie par le cup-produit sur  $H^{2}(V^{4}, R)$ .

Cela résulte immédiatement des théorèmes IV.1 et 2, associés au fait que $\Omega^{4}=Z$; le coefficient 3 s'obtient en calculant la valeur de $P^{4}$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">6 Commentarii Mathematici Helvetici</span></small>

pour $PC(2)$, pour lequel $\tau = 1$. Ce résultat avait été conjecturé par Wu Wen-Tsün, qui avait démontré que le nombre $P^4$ est divisible par 3 [35]. Il a été également obtenu par Rokhlin [20] et par moi-même, par une voie différente$^{12}$).

On remarquera que ce résultat entraîne l'invariance topologique de la classe  $P^{4}$  dans une  $V^{4}$ ; il n'en serait pas moins très souhaitable d'avoir une démonstration plus directe de la relation  $P^{4} = 3\tau$ . En particulier, la classe de cobordisme d'une  $V^{4}$  est indépendante de sa structure différentiable.

On a vu au chap. II.5 que la cohomologie $H^{*}(M(SO(n)))$ est, à coefficients rationnels, isomorphe à celle d'un produit $Y$ de complexes d'Eilenberg-Mac Lane:

$$
Y = K (Z, k) \times K (Z, k + 4) \times (K (Z, k + 8)) ^ {2} \dots (K (Z, k + 4 m)) ^ {c (m)} \dots , m \leqslant k,
$$

où $c(m)$ est le rang de $H^{4m}(\hat{G}_{k};R)$, et il existe une application $F:M(SO(k))\to Y$ qui induit un tel isomorphisme. On en déduit, par application de la $\mathcal{C}$-théorie de J. P. Serre, $\mathcal{C}$ désignant ici la famille des groupes finis (cf. [22]).

Théorème IV.15. Tous les groupes $\Omega^{i}$ sont finis, si $i \not\equiv 0 \mod 4$; la composante libre du groupe $\Omega^{4m}$ est de rang $c(m)$, nombre de Betti de dimension $4m$ de la grassmannienne $\hat{G}_{k}$.

Corollaire IV.16. Si tous les nombres caractéristiques de Pontrjagin d'une variété orientée  $V^{k}$ , sont nuls, il existe un entier non nul N tel que la variété  $N \cdot V$  soit une variété-bord.

On remarquera que le générateur de $\Omega^{5} \simeq Z_{2}$ est la variété de Wu définie en [33].

La structure multiplicative des $\Omega^{k}$.

Désignons par $\Omega^{T}$ l'ensemble des éléments d'ordre fini de $\Omega\cdot\Omega^{T}$ est un idéal de $\Omega$, et l'on peut définir l'anneau quotient $\Omega/\Omega^{T}$. On a vu (Th. IV.15) que la composante de cet anneau pour la dimension $4m$, est la somme directe de $c(m)$ groupes isomorphes à $Z$; désignons par $Q$ le corps des rationnels; nous trouvons ainsi que

$$
\Omega^ {4 m} \otimes Q \simeq \pi_ {k + 4 m} (M (S O (k))) \otimes Q
$$

est en dualité (sur le corps Q) avec le groupe de cohomologie

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$N^{4}=Z_{2}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{12}$ Voir mon exposé au Colloque de Topologie de Strasbourg (Juin 1952). La Note [20] de Rokhlin contient également des résultats sur les groupes N, dont le résultat erroné  $N^{4}=Z_{2}$  (au lieu de  $Z_{2}+Z_{2}$ ).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$Z_{2} + Z_{2})$</span></small>

$$
H ^ {k + 4 m} (M (S O (k)); Q) \simeq H ^ {4 m} (\widehat {G} _ {k}; Q);
$$

ainsi, tout élément de $\Omega/\Omega^{T}$ pour la dimension $4m$ est entièrement caractérisé par les valeurs des nombres caractéristiques normaux

$$
\langle \Pi (P ^ {4 r}), V ^ {4 m} \rangle ,
$$

définis dans l'immersion d'une variété  $V^{4m}$  de la classe dans l'espace euclidien. Il importe toutefois de préciser le point suivant: si l'on se donne «a priori» un système de  $c(m)$  valeurs entières  $n_{i}$, il n'est nulle-ment certain qu'il existe une variété admettant pour ensemble de ses nombres caractéristiques normaux (ou tangents) le système des  $n_{i}$; mais on peut affirmer l'existence d'un entier non nul N tel que le système des produits  $N \cdot n_{i}$  constitue l'ensemble des nombres caractéristiques normaux (ou tangents) d'une variété  $V^{4m}$.

Cela étant, on peut refaire pour le produit tensoriel $\Omega\otimes Q$ la théorie faite pour l'anneau $\mathfrak{N}$. Rappelons que dans la théorie de Borel-Serre, les classes de Pontrjagin sont associées aux fonctions symétriques élémentaires des carrés $(x_{i})^{2}$ de variables $x_{i}$ de dimension 2 (s'il existe une structure unitaire subordonnée à la structure orthogonale donnée, les fonctions symétriques des $x_{i}$ donnent les classes de Chern de cette structure). On obtient ainsi une base du groupe $H^{4m}(\widehat{G}_{k})$ en formant tous les monômes symétrisés:

$$
P _ {\omega} = \sum (x _ {1} ^ {2}) ^ {a _ {1}} (x _ {2} ^ {2}) ^ {a _ {2}} \dots (x _ {r} ^ {2}) ^ {a _ {r}}
$$

où les entiers $a_{1}, a_{2} \ldots a_{r}$ constituent toutes les partitions $(\omega)$ possibles de l'entier $m$.

Si $X^{p}$ et $Y^{q}$ sont deux variétés orientées, les nombres caractéristiques normaux de la variété-produit $X^{p} \times Y^{q}$ sont donnés en fonction de ceux des facteurs $X^{p}$ et $Y^{q}$ par la formule:

$$
P _ {\omega} (X ^ {p} \times Y ^ {q}) = \Sigma_ {\omega_ {1}, \omega_ {2}} P _ {\omega_ {1}} (X ^ {p}) \cdot P _ {\omega_ {2}} (Y ^ {q})\tag{3'}
$$

où $\omega_{1},\omega_{2}$ parcourent l'ensemble des partitions complémentaires de telles que $\deg \omega_{1} = p,\deg \omega_{2} = q$

Or, d'après la remarque plus haut, il existe pour toute dimension $4m$, des variétés $V^{4m}$ dont tous les nombres caractéristiques normaux sont nuls, à la seule exception du nombre $\langle \Sigma(x_i)^{2m}, V^{4m} \rangle$; soit $Y_{[4m]}$ la classe correspondante de $\Omega^{4m} \otimes Q$. Il résulte alors de la formule (3') et du corollaire IV.16, que les classes $Y_{[4m]}$ sont indécomposables, et que toute autre classe de $\Omega \otimes Q$ s'exprime de façon univoque comme somme de produits de classes $Y_{[4m]}$. D'où le:

Théorème IV.17. L'algèbre $\Omega \otimes Q$ est une algèbre de polynômes admettant un générateur $Y_{[4m]}$ pour toute dimension divisible par 4. Nous allons maintenant montrer que la classe $Y_{4m}$ est, à un facteur non nul près, la somme de la classe de l'espace projectif complexe $PC(2m)$ et d'éléments décomposables; on pourra ainsi faire choix, comme nouveau générateur $Y_{[4m]}'$, de la classe de $PC(2m)$. Il suffit, ici encore, de vérifier que le nombre caractéristique normal de $PC(2m)$, associé à la classe $\Sigma(x_i)^{2m}$ n'est pas nul. Or, en vertu des formules de dualité entre classes normales et classes tangentes, le nombre caractéristique normal associé à $\Sigma(x_i)^{2m}$ est l'opposé du nombre caractéristique tangent associé à la même classe. Or on sait que le polynôme de Chern de l'espace projectif complexe $PC(2m)$ s'écrit (en désignant par $d$ la classe de la droite projective):

$$
C (x) = 1 + \left\{ \begin{array}{c} 2 m + 1 \\ 1 \end{array} \right\} d x + \dots + \left\{ \begin{array}{c} 2 m + 1 \\ i \end{array} \right\} d ^ {i} \cdot x ^ {i} + \dots + \left\{ \begin{array}{c} 2 m + 1 \\ 2 m \end{array} \right\} d ^ {2 m} \cdot x ^ {2 m}
$$

soit, symboliquement:

$$
C (x) = (1 + d x) ^ {2 m + 1}.
$$

On peut donc considérer que les racines de ce polynôme sont en nombre  $2m + 1$ , et toutes égales à  $x_{i} = -1/d$ .

Dans ces conditions, le nombre caractéristique $\langle \Sigma(x_i)^{2m}, PC(2m) \rangle$ est égal à $\Sigma\langle(-1/d)^{2m}, d^{2m}\rangle = 2m + 1$.

Le nombre caractéristique normal de  $PC(2m)$  associé à la classe  $(x_{i})^{2m}$  est donc égal à  $-(2m+1)\neq0$  et la propriété est prouvée. On en tire:

Corollaire IV.18. Pour toute variété orientée  $V^{n}$ , il existe un entier non nul N tel que la variété multiple  $N \cdot V^{n}$  soit cobordante à une combinaison linéaire à coefficients entiers  $m_{i}$  de produits d'espaces projectifs complexes de dimension complexe paire. Les entiers  $m_{i}$  sont des fonctions linéaires homogènes des nombres caractéristiques de Pontrjagin de  $N \cdot V^{n}$ .

Remarque. On peut se demander si les produits d'espaces $PC(2j)$ ne constituent pas une base du $Z$-module $\Omega/\Omega^{T}$. Il en est effectivement ainsi pour la dimension 4, car la classe $PC(4)$ engendre $\Omega_{4}$. On peut montrer qu'il en est de même en dimension 8; en effet, pour cette dimension les nombres caractéristiques $P^{8}$ et $(P^{4})^{2}$ sont liés par les relations suivantes:

$$
(P ^ {4}) ^ {2} - 2 \cdot P ^ {8} \equiv 0 \mod 5
$$

$$
7 P ^ {8} - (P ^ {4}) ^ {2} = 4 5 \tau .
$$

La première relation provient de la relation $St_{5}^{8}\Delta = 0$, dans la variétéproduit (cf. Wu [35]); la seconde s'obtient en écrivant $\tau$ comme fonction linéaire homogène de $P^8$ et $(P^4)^2$, et en déterminant les coefficients par les exemples-types $PC(4)$ et $(PC(2))^2$. Soit $V^8$ une variété, $\tau$ la signature de la forme quadratique du cup-carré sur $H^4(V^8,R)$. Si on pose $(P^4)^2 - 2P^8 = 5q$, alors on vérifie que $V^8$ et la variété

$$
q \cdot P C (4) + (\tau - q) \cdot (P C (2)) ^ {2}
$$

ont mêmes nombres de Pontrjagin et sont cobordantes (mod $\Omega^{T}$). La généralisation de ce résultat exigerait des connaissances plus précises sur les propriétés arithmétiques et topologiques des nombres de Pontrjagin$^{13}$.

## BIBLIOGRAPHIE

[1] J. Adem. The iteration of the Steenrod squares in Algebraic Topology. Proc. Nat. Acad. Sci. U.S.A., 38, 8, p. 720—6.

[2] A. L. Blakers. — W. S. Massey. The homotopy groups of a triad. Ann. of Math. 53, 1, 1951, p. 161—204.

[3] A. Borel. Sur la cohomologie des espaces fibrés principaux et des espaces homogènes de groupes de Lie compacts. Ann. of Math., 57, 1953, p. 115—207.

[4] A. Borel. La cohomologie modulo 2 de certains espaces homogènes. Comment. Math. Helv. 27, 3, 1953, pp. 165—97.

[5] A. Borel. — J. P. Serre. Groupes de Lie et puissances réduites de Steenrod. Amer. J. of Math. 75, 3 1953, pp. 409—48.

[6] N. Bourbaki. Topologie Générale. Chap. IX. p. 75. Act. Sci. Ind. Paris.

[7] H. Cartan. Sur les groupes d'Eilenberg-MacLane (à paraître ultérieurement).

[8] S. Chern. On the multiplication of the characteristic ring of a sphere-bundle. Ann. of Math., 49, 1948, p. 2.

[9] B. Eckmann. Coverings and Betti numbers. Bull. Amer. Math. Soc., 55, 1949, p. 95—101.

[10] C. Ehresmann. Sur les espaces fibrés différentiables. C. R. Acad. Sci. Paris, 224, 1947, pp. 1611—12.

[11] S. Eilenberg. Topological Methods in abstract algebra; cohomology theory of groups. Bull. Amer. Math. Soc., 55, 1949, pp. 3—27.

[12] S. Eilenberg. Problems in Topology. Ann. of Math., 50, 1949, pp. 246—60.

[13] S. Eilenberg. — S. M. Mac Lane. Cohomology Theory of abelian groups and homotopy groups (I). Proc. Nat. Acad. Sci. U.S.A., 36, 1950, p. 443—7.

[14] S. Eilenberg. — S. Mac Lane. (IV). Proc. Nat. Acad. Sci. U.S.A., 38, 1952, pp. 1340—2.

[15] W. Hurewicz. Beiträge zur Topologie der Deformationen. Nederl, Akad. Wetensch. Proc. Ser. A, 1935—6.

$^{13}$  Voir à ce sujet les travaux récents de F. Hirzebruch (Notes miméographiées de l'Université de Princeton, Juillet-Août 1953).

[16] A. P. Morse. The behavior of a function on its critical set. Ann. of Math., 40, 1939, 1, pp. 62–70.

[17] L. Pontrjagin. Doklady Akad. Nauk S.S.S.R., 34, 1942, pp. 35—7.

[18] L. Pontrjagin. Characteristic cycles of differentiable Manifolds. Mat. Sbornik, 21 (63), 1947, pp. 233–84.

[19] B. A. Rokhlin. Une variété de dimension 3 est le bord d'une variété de dimension 4 (Russe). Doklady Akad. Nauk S.S.S.R., 81, 1951, p. 355.

[20] B.A. Rokhlin. Nouveaux résultats en théorie des variétés de dimension 4 (Russe). Doklady Akad. Nauk. S.S.S.R., 84, n° 2, 1952, pp. 221—4.

[21] H. Seifert. Algebraische Approximation von Mannigfaltigkeiten. Math. Z., 41, 1936, pp. 1—17.

[22] J. P. Serre. Groupes d'homotopie et classes de groupes abéliens. Ann. of Math. 58, 2, 1953, pp. 258—294.

[23] J. P. Serre. Cohomologie modulo 2 des complexes d'Eilenberg-Mac Lane. Comment. Math. Helv. 27, 3, 1953, pp. 198—231.

[24] J. P. Serre. Homologie singulière des espaces fibrés. Ann. of Math., 54, 3, pp. 425–505.

[25] N. E. Steenrod. Cyclic reduced Powers of cohomology classes. Proc. Nat. Acad. Sci. U.S.A. 39, 3, 1953, pp. 213—223.

[26] N. E. Steenrod. — J. H. C. Whitehead. Vector fields on the n-sphere. Proc. Nat. Acad. Sci. U.S.A., 37, 1, p. 58—63, 1951.

[27] R. Thom. Espaces fibrés en sphères et carrés de Steenrod. Ann. Sci. Ecole Norm. Sup., 69 (3), 1952, pp. 109—81.

[28] R. Thom. Sous-variétés et classes d'homologie des variétés différentiables. C. R. Acad. Sci. Paris, 236, pp. 453—4 et 573—5. Sur un problème de Steenrod. Ibid. 236, p. 1128—30. Variétés différentiables cobordantes. Ibid. 236, pp. 1733—5.

[29] J. H. C. Whitehead. Combinatorial Homotopy. Bull. Amer. Math. Soc. 55, p. 213–45 et p. 453–96.

[30] H. Whitney. A function not constant on a connected set of critical points. Duke Math. J. I. n° 4, 1935, p. 514—17.

[31] H. Whitney. Analytic extensions of differentiable functions defined in closed sets. Trans. Amer. Math. Soc. 36, n° 1, 1934, p. 63–89.

[32] H. Whitney. Topology of differentiable Manifolds. Michigan Lectures, p. 101–41.

[33] Wu W. T. Classes caractéristiques et i-carrés d'une variété. C.R. Acad. Sci. Paris, 230, 1950, p. 508—9.

[34] Wu W. T. Les i-carrés dans une variété grassmannienne. C. R. Acad. Sci., Paris, 230, 1950, p. 918.

[35] Wu W. T. Sur les puissances de Steenrod. Colloque de Topologie de Strasbourg, Juillet 1951. (Miméographié).