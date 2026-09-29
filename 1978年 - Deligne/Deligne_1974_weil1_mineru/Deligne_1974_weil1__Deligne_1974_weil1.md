PIERRE DELIGNE

La conjecture de Weil : I

Publications mathématiques de l'I.H.É.S., tome 43 (1974), p. 273-307

&lt;http://www.numdam.org/item?id=PMIHES_1974__43__273_0&gt;

© Publications mathématiques de l'I.H.É.S., 1974, tous droits réservés.

L'accès aux archives de la revue « Publications mathématiques de l'I.H.É.S. » (http://www.ihes.fr/IHES/Publications/Publications.html) implique l'accord avec les conditions générales d'utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou impression systématique est constitutive d'une infraction pénale. Toute copie ou impression de ce fichier doit contenir la présente mention de copyright.

# LA CONJECTURE DE WEIL. I par PIERRE DELIGNE

## SOMMAIRE

1. La théorie de Grothendieck : interprétation cohomologique de fonctions L .... 273
2. La théorie de Grothendieck : dualité de Poincaré.... 280
3. La majoration fondamentale .... 283
4. La théorie de Lefschetz : théorie locale .... 287
5. La théorie de Lefschetz : théorie globale.... 289
6. Un théorème de rationalité .... 294
7. Fin de la démonstration de (1.7) .... 298
8. Premières applications .... 301

Dans cet article, je démontre la conjecture de Weil sur les valeurs propres des endomorphismes de Frobenius. Un énoncé précis est donné en (1.6). J'ai tenté de présenter la démonstration sous une forme aussi géométrique et élémentaire que possible et j'ai inclus force rappels : seuls sont originaux les résultats des §§ 3, 6, 7 et 8.

Dans un article faisant suite à celui-ci, je donnerai divers raffinements des résultats intermédiaires, et des applications, parmi lesquelles le théorème de Lefschetz « difficile » (sur les cup-produits itérés par la classe de cohomologie d'une section hyperplane).

Le texte suit fidèlement celui de six conférences données à Cambridge en juillet 1973. Je remercie N. Katz de m'avoir permis d'utiliser ses notes.

## 1. La théorie de Grothendieck : interprétation cohomologique de fonctions L.

(1.1) Soient X un schéma de type fini sur Z, |X| l'ensemble des points fermés de X et, pour  $x \in |X|$ , soit  $N(x)$  le nombre d'éléments du corps résiduel  $k(x)$  de X en x. La fonction zêta de Hasse-Weil de X est

$$
(\mathbf {I}. \mathbf {I}. \mathbf {I})
$$

$$
\zeta_ {\mathrm{X}} (s) = \prod_ {x \in | \mathrm{X} |} (\mathrm{I} - \mathrm{N} (x) ^ {- s}) ^ {- 1}
$$

(ce produit converge absolument pour $\mathcal{R}(s)$ assez grand). Pour $\mathbf{X} = \operatorname{Spec}(\mathbf{Z})$, $\zeta_{\mathbf{X}}(s)$ est la fonction zêta de Riemann.

Nous considérerons exclusivement le cas où X est un schéma sur un corps fini  $F_{q}$ .

Pour $x \in |X|$, nous écrirons $q_x$ plutôt que $N(x)$. Posant $\deg(x) = [k(x) : \mathbf{F}_q]$, on a $q_x = q^{\deg(x)}$. Il y a intérêt à introduire la variable $t = q^{-s}$. Posons

$$
Z (X; t) = \prod_ {x \in | X |} (I - t ^ {\deg (x)}) ^ {- 1};\tag{\( (1.1.2) \}
$$

ce produit infini converge pour  $|t|$  assez petit, et on a

$$
\zeta_ {\mathrm{X}} (s) = \mathrm{Z} (\mathrm{X}; q ^ {- s}).\tag{\((\mathbf{I}.\mathbf{I}.\mathbf{3})\}
$$

(1.2) Dwork (On the rationality of the zeta function of an algebraic variety, Amer. J. Math., 82, 1960, p. 631-648) et Grothendieck ([1] et SGA 5) ont démontré que $\mathbf{Z}(\mathbf{X}, t)$ est une fonction rationnelle de $t$.

Pour Grothendieck, c'est là un corollaire de résultats généraux en cohomologie $\ell$-adique ($\ell$ désigne un nombre premier différent de la caractéristique $p$ de $\mathbf{F}_q$). Ceux-ci fournissent une interprétation cohomologique des zéros et des pôles de $\mathbf{Z}(\mathbf{X}; t)$, et une équation fonctionnelle lorsque $\mathbf{X}$ est propre et lisse. Les méthodes de Dwork sont $p$-adiques. Pour $\mathbf{X}$ une hypersurface non singulière dans l'espace projectif, elles lui fournissaient également une interprétation cohomologique des zéros et des pôles, et l'équation fonctionnelle. Elles ont inspiré la théorie cristalline de Grothendieck et Berthelot, qui pour $\mathbf{X}$ propre et lisse fournit une interprétation cohomologique $p$-adique des zéros et pôles, et l'équation fonctionnelle. Se basant sur des idées de Washnitzer, Lubkin a créé une variante de cette théorie, valable seulement pour $\mathbf{X}$ propre, lisse et relevable en caractéristique zéro (A $p$-adic proof of Weil's conjectures, Ann. of Math., 87, 1968, p. 105-255).

Nous ferons un usage essentiel des résultats de Grothendieck, et les rappelons ci-dessous.

(1.3) Soit X une variété algébrique sur un corps algébriquement clos $k$ de caractéristique $p$, i.e. un schéma séparé de type fini sur $k$. On n'exclut pas le cas $p=0$. Pour tout nombre premier $\ell\neq p$, Grothendieck a défini des groupes de cohomologie $\ell$-adiques $\mathrm{H}^{i}(\mathrm{X},\mathbf{Q}_{\ell})$. Il a aussi défini des groupes de cohomologie à support propre $\mathrm{H}_{c}^{i}(\mathrm{X},\mathbf{Q}_{\ell})$. Pour X propre, les deux coïncident. Les $\mathrm{H}_{c}^{i}(\mathrm{X},\mathbf{Q}_{\ell})$ sont des espaces vectoriels de dimension finie sur $\mathbf{Q}_{\ell}$, nuls pour $i>2\dim(\mathrm{X})$.

(1.4) Soient  $X_{0}$  une variété algébrique sur  $F_{q}$,  $\overline{F}_{q}$  une clôture algébrique de  $F_{q}$  et X la variété algébrique sur  $\overline{F}_{q}$  déduite de  $X_{0}$  par extension des scalaires de  $F_{q}$  à  $\overline{F}_{q}$. Dans le langage de Weil ou Shimura, on exprimerait cette situation par : « Soit X une variété algébrique définie sur  $F_{q}$ ». Soit  $F : X \to X$  le morphisme de Frobenius; il envoie le point de coordonnées x vers le point de coordonnées  $x^{q}$; en d'autres termes, pour  $U_{0}$  un ouvert de Zariski de  $X_{0}$, définissant un ouvert U de X, on a  $F^{-1}(U) = U$; pour  $x \in H^{0}(U_{0}, \mathcal{O})$, on a  $F^{*}x = x^{q}$. Identifons l'ensemble |X| des points fermés de X à  $X_{0}(\overline{\mathbf{F}}_{q})$  (l'ensemble  $\operatorname{Hom}_{\mathbf{F}_{q}}(\operatorname{Spec}(\overline{\mathbf{F}}_{q}), X_{0})$  des points de  $X_{0}$  à coefficients dans  $\overline{F}_{q}$), et soit

$\varphi \in \operatorname{Gal}(\overline{\mathbf{F}}_q / \mathbf{F}_q)$ la substitution de Frobenius: $\varphi(x) = x^q$. L'action de F sur $|\mathbf{X}|$ s'identifie à l'action de $\varphi$ sur $\mathbf{X}_0(\overline{\mathbf{F}}_q)$. Dès lors:

a) L'ensemble $\mathbf{X}^{\mathrm{F}}$ des points fermés de X fixes sous F s'identifie à l'ensemble $\mathbf{X}_0(\mathbf{F}_q)\subset \mathbf{X}_0(\overline{\mathbf{F}}_q)$ des points de X définis sur $\mathbf{F}_q$. Ceci exprime simplement que, pour $x\in \overline{\mathbf{F}}_q$, on a $x\in \mathbf{F}_q\Leftrightarrow x^q = x$.

b) De même, l'ensemble  $X^{F^{n}}$  des points fermés de X fixes sous le  $n^{ième}$  itéré de F s'identifie à  $\mathbf{X}_{0}(\mathbf{F}_{\sigma^{n}})$ .

c) L'ensemble $|\mathbf{X}_0|$ des points fermés de $\mathbf{X}_0$ s'identifie à l'ensemble $|\mathbf{X}|_{\mathrm{F}}$ des orbites de F (ou de $\varphi$) dans $|\mathbf{X}|$. Le degré $\deg(x)$ de $x \in |\mathbf{X}_0|$ est le nombre d'éléments de l'orbite correspondante.

d) De b) et c) résulte la formule

$$
\# \mathbf {X} ^ {\mathrm{F} ^ {n}} = \# \mathbf {X} _ {0} (\mathbf {F} _ {q ^ {n}}) = \sum_ {\deg (x) | n} \deg x\tag{1.4.1}
$$

(pour $x \in |\mathbf{X}_0|$ et $\deg(x)|n$, $x$ définit $\deg(x)$ points à coordonnées dans $\mathbf{F}_{q^n}$, tous conjugués sur $\mathbf{F}_q$).

(1.5) Le morphisme F est fini, en particulier propre. Il induit donc des applications

$$
\mathbf {F} ^ {*}: \mathrm{H} _ {c} ^ {i} (\mathrm{X}, \mathbf {Q} _ {\ell}) \rightarrow \mathrm{H} _ {c} ^ {i} (\mathrm{X}, \mathbf {Q} _ {\ell}).
$$

Grothendieck a prouvé la formule de Lefschetz

$$
\# \mathbf {X} ^ {\mathrm{F}} = \sum_ {i} (- \mathrm{i}) ^ {i} \operatorname{Tr} (\mathrm{F} ^ {*}, \mathrm{H} _ {c} ^ {i} (\mathrm{X}, \mathbf {Q} _ {\ell}));
$$

le membre de droite, a priori un nombre ℓ-adique, est entier, et égal au membre de gauche. On notera qu'une telle formule n'est raisonnable que parce que dF=o, même à l'infini (X n'est pas supposé propre); la relation dF=o implique que les points fixes de F sont de multiplicité un.

Une formule analogue vaut pour les itérés de F :

$$
\# \mathbf {X} ^ {\mathrm{F} ^ {n}} = \# \mathbf {X} _ {0} (\mathbf {F} _ {q ^ {n}}) = \sum_ {i} (- \mathrm{i}) ^ {i} \operatorname{Tr} (\mathrm{F} ^ {* n}, \mathrm{H} _ {c} ^ {i} (\mathrm{X}, \mathbf {Q} _ {\ell})).\tag{1.5.1}
$$

Prenons la dérivée logarithmique de (1.1.2) :

$$
\begin{array}{r l} t \frac {d}{d t} \log Z (X _ {0}, t) & = \frac {t \frac {d}{d t} Z (X _ {0} , t)}{Z (X _ {0} , t)} = \sum_ {x \in | X _ {0} |} - \frac {- \deg (x) t ^ {\deg (x)}}{I - t ^ {\deg (x)}} \\ & = \sum_ {x \in | X _ {0} |} \sum_ {n > 0} \deg (x) t ^ {n. \deg (x)} = \sum_ {(1. 4. 1) n} \# X _ {0} (\mathbf {F} _ {q ^ {n}}). t ^ {n}. \end{array}\tag{1.5.2}
$$

Pour F un endomorphisme d'un espace vectoriel V, on a une identité de séries formelles

(1.5.3)

$$
t \frac {d}{d t} \log (\det (\mathrm{I} - \mathrm{F} t, \mathrm{V}) ^ {- 1}) = \sum_ {n > 0} \operatorname{Tr} (\mathrm{F} ^ {n}, \mathrm{V}) t ^ {n}\tag{275}
$$

(le vérifier pour  $\dim(V)=1$ , et observer que les deux membres sont additifs en V dans une suite exacte courte). Substituant (1.5.1) dans (1.5.2) et appliquant (1.5.3), on trouve

$$
t \frac {d}{d t} \log Z (X _ {0}, t) = \sum_ {i} (- 1) ^ {i} t \frac {d}{d t} \log \det (1 - F ^ {*} t, H _ {c} ^ {i} (X, Q _ {\ell})) ^ {- 1},
$$

soit

$$
Z (X _ {0}, t) = \prod_ {i} \det (I - F ^ {*} t, H _ {c} ^ {i} (X, Q _ {\ell})) ^ {(- 1) ^ {i + 1}}.\tag{1.5.4}
$$

Le membre de droite est un élément de $\mathbf{Q}_{\ell}(t)$. La formule affirme que son développement de Taylor en $t=0$, a priori une série formelle dans $\mathbf{Q}_{\ell}[[t]]$ de terme constant un, est dans $\mathbf{Z}[[t]]$, et est égal au membre de gauche, lui aussi considéré comme une série formelle en $t$. Cette formule est l'interprétation cohomologique de Grothendieck de la fonction $\mathbf{Z}$.

Notre résultat principal est le suivant.

Théorème (1.6). — Soit  $X_{0}$  une variété projective non singulière (=lisse) sur  $F_{q}$ . Pour chaque i, le polynôme caractéristique det(t.i—F\*, H^{i}(X, Q\_{\ell})) est à coefficients entiers indépendants de  $\ell (\ell \neq p)$ . Les racines complexes  $\alpha$  de ce polynôme (les conjugués complexes des valeurs propres de F\*) sont de valeur absolue  $|\alpha| = q^{i/2}$ .

Montrons déjà que (1.6) résulte du résultat apparemment plus faible suivant.

Lemme (1.7). — Pour chaque i, et chaque  $\ell\neq p$ , les valeurs propres de l'endomorphisme  $F^{*}$  de  $\mathrm{H}^{i}(\mathbf{X},\mathbf{Q}_{\ell})$  sont des nombres algébriques dont tous les conjugués complexes  $\alpha$  sont de valeur absolue  $|\alpha|=q^{i/2}$ .

Preuve de (1.7)⇒(1.6). — Regardons  $Z(X_{0},t)$  comme une série formelle de terme constant 1, élément de  $Z[[t]]:Z(X_{0},t)=\sum_{n}a_{n}t^{n}$ . D'après (1.5.3), l'image de  $Z(X_{0},t)$  dans  $Q_{\ell}[[t]]$  est le développement de Taylor d'une fraction rationnelle. Ceci signifie que pour N et M assez grands (≥ les degrés des numérateurs et dénominateurs) les déterminants de Hankel

$$
\mathrm{H} _ {k} = \det ((a _ {i + j + k}) _ {0 \leq i, j \leq \mathbb {M}}) \quad (k > \mathbf {N})
$$

sont nuls. Cette nullité est vraie dans $\mathbf{Q}_{\ell}$ si et seulement si elle l'est dans $\mathbf{Q}$; $Z(X_{0}, t)$ est donc le développement en série de Taylor d'un élément de $\mathbf{Q}(t)$. En d'autres termes,

$$
\mathbf {Z} (\mathbf {X} _ {0}, t) \in \mathbf {Z} [ [ t ] ] \cap \mathbf {Q} _ {\ell} (t) \subset \mathbf {Q} (t).
$$

Écrivons $Z(X_0, t) = P/Q$, avec $P, Q \in \mathbf{Z}[t]$, premiers entre eux, et de terme constant positif. D'après un lemme de Fatou, que $Z(X_0, t)$ soit dans $\mathbf{Z}[[t]]$ et de terme constant un implique que les termes constants de $P$ et $Q$ sont 1. Posons

$$
\mathrm{P} _ {i} (t) = \det (\mathrm{i} - \mathrm{F} ^ {*} t, \mathrm{H} ^ {i} (\mathrm{X}, \mathbf {Q} _ {\ell})).
$$

277

D'après l'hypothèse (1.7), les  $P_{i}$  sont premiers entre eux. Le membre de droite de (1.5.4) est donc sous forme irréductible, et

$$
\mathrm{P} (t) = \prod_ {i \text {   impair }} \mathrm{P} _ {i} (t)
$$

$$
\mathrm{Q} (t) = \prod_ {i \text {   pair }} \mathrm{P} _ {i} (t).
$$

Soit K le sous-corps d'une clôture algébrique $\overline{\mathbf{Q}}_{\ell}$ de $\mathbf{Q}_{\ell}$ engendré sur $\mathbf{Q}$ par les racines de $\mathrm{R}(t)=\mathrm{P}(t)\mathrm{Q}(t)$. Les racines de $\mathrm{P}_{i}(t)$ sont celles des racines de $\mathrm{R}(t)$ ayant la propriété que tous leurs conjugués complexes sont de valeur absolue $q^{-i/2}$. Cet ensemble est stable sous $\operatorname{Gal}(\mathrm{K}/\mathbf{Q})$. Le polynôme $\mathrm{P}_{i}(t)$ est donc à coefficients rationnels. D'après le lemme de Gauss (ou parce que les racines de $\mathrm{P}_{i}$, étant racines de $\mathrm{R}(t)$, sont des inverses d'entiers algébriques), il est même à coefficients entiers. La description ci-dessus des racines de $\mathrm{P}_{i}(t)$ est indépendante de $\ell$; le polynôme $\mathrm{P}_{i}(t)$ lui-même est donc indépendant de $\ell$.

La suite de cet article est consacrée à la démonstration de (1.7).

(1.8) La théorie de Grothendieck fournit une interprétation cohomologique non seulement de fonctions zêta, mais encore de fonctions L. Les résultats sont les suivants.

(1.9) Soit X une variété algébrique sur un corps k. Pour la définition d'un  $Q_{t}$ -faisceau constructible sur X, je renvoie à SGA 5 VI. Qu'il suffise de dire que:

a) Si $\mathcal{F}$ est un $\mathbf{Q}_{\ell}$-faisceau constructible sur $\mathbf{X}$, il existe une partition finie de $\mathbf{X}$ en parties localement fermées $\mathbf{X}_{i}$ telles que $\mathcal{F}|\mathbf{X}_{i}$ soit constant tordu.

b) Supposons X connexe et soit  $\bar{x}$  un point géométrique de X. Pour F constant tordu,  $\pi_{1}(X,\bar{x})$  agit sur la fibre  $F_{\bar{x}}$ ; le foncteur fibre en  $\bar{x}$  est une équivalence de catégorie ( $Q_{t}$ -faisceaux constructibles constants tordus sur X)→

$\mapsto$ (représentations continues de $\pi_1(\mathbf{X},\bar{x})$ sur un $\mathbf{Q}_{\ell}$-espace vectoriel de dimension finie).

Une telle représentation ne se factorise pas, en général, à travers un quotient fini de  $\pi_{1}(\mathbf{X},\bar{x})$ .

c) Si $k = \mathbf{C}$, les $\mathbf{Q}_t$-faisceaux constructibles sur $X$ s'identifient aux faisceaux de $\mathbf{Q}_t$-espaces vectoriels $\mathcal{F}$ sur $X^{\text{an}}$, tels qu'il existe une partition finie de $X$ en parties Zariski-localement fermées $X_i$, et pour chaque $i$ un système local de $Z_t$-Modules libres de type fini $\mathcal{F}_i$ sur $X_i$, avec

$$
\mathcal {F} \mid \mathrm{X} _ {i} = \mathcal {F} _ {i} \otimes_ {\mathbf {Z} _ {\ell}} \mathbf {Q} _ {\ell}.
$$

Nous ne considérerons que des  $Q_{t}$ -faisceaux constructibles, et les appellerons simplement  $Q_{t}$ -faisceaux.

(1.10) Supposons $k$ algébriquement clos, et soit $\mathcal{F}$ un $\mathbf{Q}_{\ell}$-faisceau sur X. Grothendieck a défini des groupes de cohomologie $\ell$-adique $\mathrm{H}^{\mathrm{i}}(\mathrm{X},\mathcal{F})$ et $\mathrm{H}_{c}^{\mathrm{i}}(\mathrm{X},\mathcal{F})$. Les $\mathrm{H}_{c}^{\mathrm{i}}(\mathrm{X},\mathcal{F})$ sont des espaces vectoriels de dimension finie sur $\mathbf{Q}_{\ell}$, nuls pour $i > 2$ dim(X).

Pour $k = \mathbf{C}$, les $\mathrm{H}^i(\mathbf{X}, \mathcal{F})$ et $\mathrm{H}_c^i(\mathbf{X}, \mathcal{F})$ sont les groupes de cohomologie usuels (resp. à support propre) de $\mathbf{X}^{\text{an}}$, à coefficients dans $\mathcal{F}$.

(1.11) Soient  $X_{0}$  une variété algébrique sur  $F_{q}$, X la variété sur  $\overline{F}_{q}$  correspondante, et  $F_{0}$  un faisceau d'ensembles sur  $X_{0}$  (pour la topologie étale). On note F son image réciproque sur X. Outre le morphisme de Frobenius  $F: X \to X$, on dispose alors d'un isomorphisme canonique  $F^{*}: F^{*}F \cong F$. En voici une description. On regarde  $F_{0}$  comme un espace étalé sur  $X_{0}$, i.e. on identifie  $F_{0}$  à l'espace algébrique  $[F_{0}]$, muni d'un morphisme étale  $f: [F_{0}] \to X_{0}$, tel que  $F_{0}$  soit le faisceau des sections locales de  $[F_{0}]$. L'espace analogue  $[F]$, étalé sur X, se déduit de  $[F_{0}]$  par extension des scalaires. On dispose donc d'un diagramme commutatif

![](images/page_6_image_2.jpg)

d'où un morphisme $[\mathcal{F}] \to \mathbf{X} \times_{(\mathbb{F},\mathbf{X},f)}[\mathcal{F}] = [\mathbf{F}^*\mathcal{F}]$, qui est un isomorphisme car $f$ est étale. Son inverse définit l'isomorphisme $\mathbf{F}^*\mathcal{F} \xrightarrow{\sim} \mathcal{F}$ cherché.

Cette construction se généralise aux $\mathbf{Q}_{\ell}$-faisceaux.

(1.12) Soient  $X_{0}$  une variété algébrique sur  $F_{q}, F_{0}$  un  $Q_{\ell}$ -faisceau sur  $X_{0}$ , (X, F) déduit de  $(\mathbf{X}_{0}, \mathcal{F}_{0})$  par extension des scalaires de  $F_{q}$  à  $\overline{F}_{q}$ , F : X → X et  $F^{*}: F^{*}F \to F$ . Le morphisme fini F et  $F^{*}$  définissent un endomorphisme

$$
\mathrm{F} ^ {*}: \mathrm{H} _ {c} ^ {i} (\mathrm{X}, \mathcal {F}) \rightarrow \mathrm{H} _ {c} ^ {i} (\mathrm{X}, \mathrm{F} ^ {*} \mathcal {F}) \rightarrow \mathrm{H} _ {c} ^ {i} (\mathrm{X}, \mathcal {F}).
$$

Pour $x\in|\mathrm{X}|$, $\mathbf{F}^{*}$ définit un morphisme $\mathbf{F}_{x}^{*}:\mathcal{F}_{\mathrm{F}(x)}\to\mathcal{F}_{x}$. Pour $x\in\mathrm{X}^{\mathrm{F}}$, c'est un endomorphisme de $\mathcal{F}_{x}$. Grothendieck a démontré la formule de Lefschetz

$$
\sum_ {x \in \mathrm{X} ^ {\mathrm{F}}} \operatorname{Tr} (\mathrm{F} _ {x} ^ {*}, \mathcal {F} _ {x}) = \sum_ {i} (- \mathrm{i}) ^ {i} \operatorname{Tr} (\mathrm{F} ^ {*}, \mathrm{H} _ {c} ^ {i} (\mathrm{X}, \mathcal {F})).
$$

Une formule analogue vaut pour les itérés de F : le  $n^{ième}$  itéré de  $F^{*}$  définit des morphismes  $\mathrm{F}_{x}^{*n} : \mathcal{F}_{\mathrm{F}_{1}(x)} \to \mathcal{F}_{x}$ ; pour x fixe sous  $F^{n}$ ,  $F_{x}^{*n}$  est un endomorphisme, et

$$
\sum_ {x \in \mathrm{X} ^ {\mathrm{F} ^ {n}}} \operatorname{Tr} (\mathrm{F} _ {x} ^ {* n}, \mathcal {F} _ {x}) = \sum_ {i} (- \mathrm{i}) ^ {i} \operatorname{Tr} (\mathrm{F} ^ {* n}, \mathrm{H} _ {c} ^ {i} (\mathrm{X}, \mathcal {F})).\tag{1.12.1}
$$

(1.13) Soient $x_{0}\in|\mathbf{X}_{0}|$, Z l'orbite correspondante de F dans $|\mathbf{X}|$ et $x\in\mathbf{Z}$. L'orbite Z a $\deg(x_{0})$ éléments (1.4). On note $\mathrm{F}_{x_{0}}^{*}$ l'endomorphisme $\mathrm{F}_{x}^{*\deg(x_{0})}$ de $\mathcal{F}_{x}$, et on pose

$$
\det (\mathrm{I} - \mathrm{F} _ {x _ {0}} ^ {*} t, \mathcal {F} _ {0}) = \det (\mathrm{I} - \mathrm{F} _ {x _ {0}} ^ {*} t, \mathcal {F} _ {x}).
$$

A isomorphisme près, $(\mathcal{F}_x,\mathrm{F}_{x_0}^*)$ ne dépend pas du choix de $x$. Ceci justifie d'omettre $x$ de la notation. On utilisera une notation analogue pour d'autres fonctions de $(\mathcal{F}_x,\mathrm{F}_{x_0}^*)$.

(1.14) Définissons  $Z(X_{0},\mathcal{F}_{0},t)\in\mathbf{Q}_{\ell}[[t]]$  par le produit

$$
\mathrm{Z} (\mathrm{X} _ {0}, \mathcal {F} _ {0}, t) = \prod_ {x \in | \mathrm{X} _ {0} |} \det (\mathrm{I} - \mathrm{F} _ {x} ^ {*} t ^ {\deg (x)}, \mathcal {F} _ {0}) ^ {- 1}.\tag{\((\mathbf{I}.\mathbf{I}_4.\mathbf{I})\}
$$

Pour $\mathcal{F}$ le faisceau constant $\mathbf{Q}_{\ell}$, on retrouve (1.1.2). D'après (1.5.3), la dérivée logarithique de $Z$ est

$$
t \frac {d}{d t} \log Z (X _ {0}, \mathcal {F} _ {0}, t) = \frac {t \frac {d}{d t} Z (X _ {0} , \mathcal {F} _ {0} , t)}{\mathrm{dfn}} = \frac {1}{Z (X _ {0} , \mathcal {F} _ {0} , t)} = \sum_ {n} \sum_ {x \in X ^ {\mathrm{f} n} = X _ {0} (\mathbf {F} _ {q ^ {n}})} \operatorname{Tr} (F _ {x} ^ {* n}, \mathcal {F} _ {0}) t ^ {n}.\tag{1.14.2}
$$

Substituant (1.12.1) dans (1.14.2), on trouve par le même calcul qu'en (1.5) la généralisation suivante de (1.5.4)

$$
\mathrm{Z} (\mathrm{X} _ {0}, \mathcal {F} _ {0}, t) = \prod_ {i} \det (\mathrm{I} - \mathrm{F} ^ {*} t, \mathrm{H} _ {c} ^ {i} (\mathrm{X}, \mathcal {F})) ^ {(- 1) ^ {i + 1}}.\tag{1.14.3}
$$

Cette formule est une identité dans $\mathbf{Q}_{\ell}[[t]]$.

(1.15) Il est parfois commode d'utiliser un langage galoisien plutôt que géométrique. Voici le dictionnaire.

Si $\overline{\mathbf{F}}_{q}^{1}$ et $\overline{\mathbf{F}}_{q}^{2}$ sont deux clôtures algébriques de $\mathbf{F}_{q}$, $(\mathbf{X}_{0},\mathcal{F}_{0})$ sur $\mathbf{F}_{q}$ définit par extension des scalaires $(\mathbf{X}_{1},\mathcal{F}_{1})$ sur $\overline{\mathbf{F}}_{q}^{1}$ et $(\mathbf{X}_{2},\mathcal{F}_{2})$ sur $\overline{\mathbf{F}}_{q}^{2}$. Tout $\mathbf{F}_{q}$-isomorphisme $\sigma : \overline{\mathbf{F}}_{q}^{1} \xrightarrow{\sim} \overline{\mathbf{F}}_{q}^{2}$ induit un isomorphisme

$$
\mathrm{H} _ {c} ^ {*} (\mathrm{X} _ {1}, \mathcal {F} _ {1}) \stackrel {{\sim}} {{\to}} \mathrm{H} _ {c} ^ {*} (\mathrm{X} _ {2}, \mathcal {F} _ {2}).
$$

En particulier, pour $\overline{\mathbf{F}}_{q}^{1}=\overline{\mathbf{F}}_{q}^{2}$ (noté $\overline{\mathbf{F}}_{q}$), on trouve que $\operatorname{Gal}(\overline{\mathbf{F}}_{q}/\mathbf{F}_{q})$ agit sur $\mathrm{H}_{c}^{*}(\mathrm{X},\mathcal{F})$ (action par transport de structure). Soit $\varphi\in\operatorname{Gal}(\overline{\mathbf{F}}_{q}/\mathbf{F}_{q})$ la substitution de Frobenius. On vérifie que

$$
\mathrm{F} ^ {*} = \varphi^ {- 1} \quad (\text { dans   } \operatorname{End} (\mathrm{H} _ {c} ^ {*} (\mathrm{X}, \mathcal {F}))).
$$

Ceci amène à définir le Frobenius géométrique  $F \in \text{Gal}(\overline{\mathbf{F}}_{q}/\mathbf{F}_{q})$  comme étant  $\varphi^{-1}$ . On a (I. I5. I)  $F^{*} = F$ .

Soit $x$ un point géométrique de $\mathbf{X}_{0}$, localisé en $x_{0} \in |\mathbf{X}_{0}|$. Par transport de structure, le groupe $\operatorname{Gal}(k(x)/k(x_{0}))$ agit sur la fibre $(\mathcal{F}_{0})_{x}$ de $\mathcal{F}_{0}$ en $x$; en particulier, le Frobenius géométrique relatif à $k(x_{0}): \mathrm{F}_{x_{0}} \in \operatorname{Gal}(k(x)/k(x_{0}))$, agit. Pour $x$ défini par un point fermé, encore noté $x$, de $\mathbf{X}$, on a $\mathcal{F}_{x} = (\mathcal{F}_{0})_{x}$, et

$$
\mathrm{F} _ {x _ {0}} ^ {*} = \mathrm{F} _ {x} ^ {* \deg (x _ {0})} = \mathrm{F} _ {x _ {0}} \quad (\text { dans } \quad \operatorname{End} (\mathcal {F} _ {x})).\tag{1.15.2}
$$

En notations galoisiennes, (1.14.3) s'écrit

$$
\prod_ {x \in | X _ {0} |} \det (I - F _ {x} t ^ {\deg (x)}, \mathcal {F} _ {0}) ^ {- 1} = \prod_ {i} \det (I - F t, H _ {c} ^ {i} (X, \mathcal {F})) ^ {(- 1) ^ {i + 1}}.\tag{279}
$$

## 2. La théorie de Grothendieck : dualité de Poincaré.

(2.1) Pour expliquer la relation entre racines de l'unité et orientations, je vais au préalable redire dans un langage farfelu deux cas classiques.

a) Variétés différentiables. — Soit X une variété différentiable purement de dimension n. Le faisceau d'orientation  $Z'$  sur X est le faisceau localement isomorphe au faisceau constant Z, dont les sections inversibles sur un ouvert U de X correspondent aux orientations de U. Une orientation de X est un isomorphisme de  $Z'$  sur le faisceau constant Z. La classe fondamentale de X est un morphisme  $\mathrm{Tr}: \mathrm{H}_{c}^{n}(\mathrm{X}, \mathbf{Z}') \to \mathbf{Z}$ ; si X est orientée, il s'identifie à un morphisme  $\mathrm{Tr}: \mathrm{H}_{c}^{n}(\mathrm{X}, \mathbf{Z}) \to \mathbf{Z}$ . La dualité de Poincaré s'exprime à l'aide de la classe fondamentale.

b) Variétés complexes. — Soit C une clôture algébrique de R. Une variété algébrique complexe lisse, ou plutôt la variété différentiable sous-jacente, est toujours orientable. Pour l'orienter, il suffit d'orienter C lui-même. Ceci revient au choix :

a) à choisir l'une des deux racines de l'équation  $X^{2} = -1$ ; on l'appelle +i;

b) à choisir un isomorphisme de R/Z avec  $U^{1}=\{z\in C||z|=1\}$ ; +i est l'image de r/4;

c) à choisir l'un des deux isomorphismes  $x \mapsto \exp(\pm 2\pi ix)$  de Q/Z sur le groupe des racines de l'unité de C, qui se prolonge par continuité en un isomorphisme de R/Z sur U¹.

On note $\mathbf{Z}(\mathrm{I})$ un $\mathbf{Z}$-module libre de rang un dont l'ensemble à deux éléments des générateurs soit en correspondance canonique avec l'un des ensembles à deux éléments $a), b), c)$. Le plus simple est de prendre $\mathbf{Z}(\mathrm{I}) = \operatorname{Ker}(\exp : \mathbf{C} \to \mathbf{C}^*)$. Au générateur $y = \pm 2\pi i$ correspond l'isomorphisme $c) : x \mapsto \exp(xy)$.

Soit  $\mathbf{Z}(r)$  la puissance tensorielle  $r^{ième}$  de  $\mathbf{Z}(1)$ . Si X est une variété algébrique complexe lisse purement de dimension complexe r, le faisceau d'orientation de X est le faisceau constant de valeur  $\mathbf{Z}(r)$ .

(2.2) Pour « orienter » les variétés algébriques sur k algébriquement clos de caractéristique o, il faut choisir un isomorphisme de Q/Z sur le groupe des racines de l'unité de k. L'ensemble de ces isomorphismes est un espace principal homogène sous  $\hat{Z}^{*}$  (non plus sous  $Z^{*}$ ). Lorsqu'on s'intéresse seulement à la cohomologie  $\ell$ -adique, il suffit de considérer les racines de l'unité d'ordre une puissance de  $\ell$, et de supposer la caractéristique p de k différente de  $\ell$. On note  $\mathbf{Z}/\ell^{n}(\mathbf{1})$  le groupe des racines de l'unité de k d'ordre divisant  $\ell^{n}$. Pour n variable, les  $\mathbf{Z}/\ell^{n}(\mathbf{1})$  forment un système projectif, d'applications de transition les

$$
\sigma_ {m, n}: \mathbf {Z} / \ell^ {m} (\mathrm{I}) \rightarrow \mathbf {Z} / \ell^ {n} (\mathrm{I}): x \mapsto x ^ {\ell^ {m - n}}.
$$

On pose $\mathbf{Z}_{\ell}(\mathrm{I}) = \lim \operatorname{proj}\mathbf{Z} / \ell^{n}(\mathrm{I})$ et $\mathbf{Q}_{\ell}(\mathrm{I}) = \mathbf{Z}_{\ell}(\mathrm{I})\otimes_{\mathbf{Z}_{\ell}}\mathbf{Q}_{\ell}$. On note $\mathbf{Q}_{\ell}(r)$ la puissance tensorielle $r^{\text{ième}}$ de $\mathbf{Q}_{\ell}(\mathrm{I})$; pour $r\in \mathbf{Z}$, $r$ négatif, on pose encore $\mathbf{Q}_{\ell}(r) = \mathbf{Q}_{\ell}(-r)^{\vee}$.

En tant qu'espace vectoriel sur $\mathbf{Q}_{\ell}$, $\mathbf{Q}_{\ell}(\mathrm{I})$ est isomorphe à $\mathbf{Q}_{\ell}$. Toutefois le groupe des automorphismes de $k$ agit non trivialement sur $\mathbf{Q}_{\ell}(\mathrm{I})$: il agit via le caractère à valeurs dans $\mathbf{Z}_{\ell}^{*}$ qui donne son action sur les racines de l'unité. En particulier, si $k = \overline{\mathbf{F}}_{q}$, la substitution de Frobenius $\varphi : x \mapsto x^{q}$ agit par multiplication par $q$.

Soit X une variété algébrique lisse purement de dimension n sur k. Le faisceau d'orientation de X en cohomologie  $\ell$ -adique est le  $\mathbf{Q}_{\ell}$ -faisceau constant  $\mathbf{Q}_{\ell}(n)$ . La classe fondamentale est un morphisme

$$
\operatorname{Tr}: \mathrm{H} _ {c} ^ {2 n} (\mathrm{X}, \mathbf {Q} _ {\ell} (n)) \rightarrow \mathbf {Q} _ {\ell},
$$

soit encore

$$
\operatorname{Tr}: \mathrm{H} _ {c} ^ {2 n} (\mathrm{X}, \mathbf {Q} _ {\ell}) \rightarrow \mathbf {Q} _ {\ell} (- n).
$$

Théorème (2.3) (dualité de Poincaré). — Pour X propre et lisse purement de dimension n, la forme bilinéaire

$$
\operatorname{Tr} (x \cup y): \mathrm{H} ^ {i} (\mathrm{X}, \mathbf {Q} _ {\ell}) \otimes \mathrm{H} ^ {2 n - i} (\mathrm{X}, \mathbf {Q} _ {\ell}) \rightarrow \mathbf {Q} _ {\ell} (- n)
$$

est une dualité parfaite (elle identifie $\mathrm{H}^i (\mathbf{X},\mathbf{Q}_\ell)$ au dual de $\mathrm{H}^{2n - i}(\mathbf{X},\mathbf{Q}_{\ell}(n)))$

(2.4) Soient  $X_{0}$  une variété algébrique propre et lisse sur  $F_{q}$ , purement de dimension n, et X sur  $\overline{F}_{q}$  déduit de  $X_{0}$  par extension des scalaires. Le morphisme (2.3) est compatible à l'action de  $\operatorname{Gal}(\overline{\mathbf{F}}_{q}/\mathbf{F}_{q})$ . Si les  $(\alpha_{j})$  sont les valeurs propres du Frobenius géométrique F agissant sur  $\mathrm{H}^{i}(\mathrm{X},\mathbf{Q}_{\ell})$ , les valeurs propres de F agissant sur  $\mathrm{H}^{2n-i}(\mathrm{X},\mathbf{Q}_{\ell})$  sont donc les  $(q^{n}\alpha_{j}^{-1})$ .

(2.5) Supposons pour simplifier X connexe. La démonstration (2.4) se transpose comme suit dans un langage géométrique, plutôt que galoisien (cf. (1.15)).

a) Le cup-produit met  $\mathrm{H}^{i}(\mathrm{X},\mathbf{Q}_{\ell})$  et  $\mathrm{H}^{2n-i}(\mathrm{X},\mathbf{Q}_{\ell})$  en dualité parfaite à valeur dans  $\mathrm{H}^{2n}(\mathrm{X},\mathbf{Q}_{\ell})$ , qui est de dimension un.

b) Le cup-produit commute à l'image réciproque F\* par le morphisme de Frobenius F : X → X.

c) Le morphisme F est fini et de degré  $q^{n}$ : sur  $\mathrm{H}^{2n}(\mathrm{X}, \mathbf{Q}_{\ell})$ ,  $F^{*}$  est la multiplication par  $q^{n}$ .

d) Les valeurs propres de $\mathbf{F}^*$ ont donc la propriété (2.4).

(2.6) On pose $\chi(\mathbf{X}) = \sum_{i} (-\mathrm{i})^{i} \dim \mathrm{H}^{i}(\mathbf{X}, \mathbf{Q}_{\ell})$. Si $n$ est impair, la forme $\operatorname{Tr}(x \cup y)$ sur $\mathrm{H}^{n}(\mathbf{X}, \mathbf{Q}_{\ell})$ est alternée; l'entier $n\chi(\mathbf{X})$ est donc toujours pair. On déduit facilement de (1.5.4) et de (2.3), (2.4) que

$$
Z (X _ {0}, t) = \varepsilon . q ^ {\frac {- n \chi (X)}{2}}. t ^ {- \chi (X)}. Z (X _ {0}, q ^ {- n} t ^ {- 1})
$$

où $\varepsilon = \pm 1$. Si $n$ est pair, notons N la multiplicité de la valeur propre $q^{n/2}$ de F\* agissant sur H$^{n}$(X, Q$_{t}$) (i.e. la dimension du sous-espace propre généralisé correspondant). On a

$$
\varepsilon = \left\{ \begin{array}{l l} \mathrm{I} & \text { si   } n \text {   est   impair } \\ (- \mathrm{I}) ^ {\mathrm{N}} & \text { si   } n \text {   est   pair. } \end{array} \right.
$$

C'est là la formulation de Grothendieck de l'équation fonctionnelle des fonctions Z.

(2.7) Nous aurons besoin d'autres formes du théorème de dualité. Le cas des courbes nous suffirait dans celles-ci. Si $\mathcal{F}$ est un $\mathbf{Q}_{\ell}$-faisceau sur une variété algébrique X sur $k$ algébriquement clos, nous noterons $\mathcal{F}(r)$ le faisceau $\mathcal{F} \otimes \mathbf{Q}_{\ell}(r)$. Ce faisceau est (non canoniquement) isomorphe à $\mathcal{F}$.

Théorème (2.8). — Supposons X lisse purement de dimension n et F constant tordu. Soit  $F^{\sim}$  le dual de F. La forme bilinéaire

$$
\operatorname{Tr} (x \cup y): \mathrm{H} ^ {i} (\mathrm{X}, \mathcal {F}) \otimes \mathrm{H} _ {c} ^ {2 n - i} (\mathrm{X}, \mathcal {F} ^ {\vee} (n)) \rightarrow \mathrm{H} _ {c} ^ {2 n} (\mathrm{X}, \mathcal {F} \otimes \mathcal {F} ^ {\vee} (n)) \rightarrow \mathrm{H} _ {c} ^ {2 n} (\mathrm{X}, \mathbf {Q} _ {\ell} (n)) \rightarrow \mathbf {Q} _ {\ell}
$$

est une dualité parfaite.

(2.9) Supposons X connexe et soit x un point fermé de X. Le foncteur  $F \mapsto F_{x}$  est une équivalence de la catégorie des  $Q_{\ell}$ -faisceaux constants tordus avec celle des représentations  $\ell$ -adiques de  $\pi_{1}(X, x)$ . Via cette équivalence,  $H^{0}(X, \mathcal{F})$  s'identifie aux invariants de  $\pi_{1}(X, x)$  agissant dans  $F_{x}$ :

$$
\mathrm{H} ^ {0} (\mathrm{X}, \mathcal {F}) \xrightarrow {\sim} \mathcal {F} _ {x} ^ {\pi_ {1} (\mathrm{X}, x)}.\tag{2.9.1}
$$

D'après (2.8), pour X lisse et connexe de dimension n, on a donc

$$
\mathrm{H} _ {c} ^ {2 n} (\mathrm{X}, \mathcal {F}) = \mathrm{H} ^ {0} (\mathrm{X}, \mathcal {F} ^ {\vee} (n)) ^ {\vee} = ((\mathcal {F} _ {x} ^ {\vee} (n)) ^ {\pi_ {1} (\mathrm{X}, x)}) ^ {\vee}.
$$

La dualité échange invariants (plus grand sous-espace invariant) et coinvariants (plus grand quotient invariant). Cette formule se récrit donc

$$
\mathrm{H} _ {c} ^ {2 n} (\mathrm{X}, \mathcal {F}) = (\mathcal {F} _ {x}) _ {\pi_ {1} (\mathrm{X}, x)} (- n).
$$

Nous ne l'utiliserons que pour $n=1$.

Scholie (2.10). — Soient X une courbe lisse et connexe sur k algébriquement clos, x un point fermé de X et F un Q\_faisceau constant tordu. On a

(i) $\mathrm{H}_c^0 (\mathbf{X},\mathcal{F}) = 0$ si X est affine.

(ii) $\mathrm{H}_c^2 (\mathbf{X},\mathcal{F}) = (\mathcal{F}_x)_{\pi_1(\mathbf{X},x)}(-\mathrm{I}).$

L'assertion (i) signifie simplement que $\mathcal{F}$ n'a pas de section à support fini.

(2.11) Soient X une courbe projective, lisse et connexe sur k algébriquement clos, U un ouvert de X, complément d'un ensemble fini S de points fermés de X, j l'inclusion  $U \hookrightarrow X$  et F un  $Q_{t}$ -faisceau constant tordu sur U. Soit  $j_{*}F$  le  $Q_{t}$ -faisceau constructible image directe de F. Sa fibre en  $x \in S$  est de rang inférieur ou égal au rang

de sa fibre en un point général; c'est un espace d'invariants sous un groupe de monodromie locale.

Théorème (2.12). — La forme bilinéaire

$$
\begin{array}{r l} \mathrm{Tr} (x \cup y): & \mathrm{H} ^ {i} (\mathrm{X}, j _ {*} \mathcal {F}) \otimes \mathrm{H} ^ {2 - i} (\mathrm{X}, j _ {*} \mathcal {F} ^ {\smile} (\mathrm{I})) \to \mathrm{H} ^ {2} (\mathrm{X}, j _ {*} \mathcal {F} \otimes j _ {*} \mathcal {F} ^ {\smile} (\mathrm{I})) \\ & \to \mathrm{H} ^ {2} (\mathrm{X}, j _ {*} (\mathcal {F} \otimes \mathcal {F} ^ {\smile}) (\mathrm{I})) \to \mathrm{H} ^ {2} (\mathrm{X}, j _ {*} \mathbf {Q} _ {\ell} (\mathrm{I})) = \mathrm{H} ^ {2} (\mathrm{X}, \mathbf {Q} _ {\ell} (\mathrm{I})) \to \mathbf {Q} _ {\ell} \end{array}
$$

est une dualité parfaite.

(2.13) Il nous sera commode de disposer des  $Q_{\ell}$ -faisceaux  $\mathbf{Q}_{\ell}(r)$  sur un quelconque schéma X où  $\ell$  est inversible. Le tout est de définir les  $\mathbf{Z}/\ell^{n}(\mathbf{i})$ . Par définition,  $\mathbf{Z}/\ell^{n}(\mathbf{i})$  est le faisceau étale des racines  $(\ell^{n})^{\mathrm{i}\mathrm{e}\mathrm{m}\mathrm{e}}$  de l'unité.

## (2.14) Indications bibliographiques sur les §§ 1 et 2.

A) Tous les résultats importants en cohomologie étale se démontrent d'abord pour des faisceaux de torsion. L'extension aux  $Q_{t}$ -faisceaux se fait par des passages à la limite formels. Dans ce qui suit, pour chaque théorème cité, je renverrai non point à une référence où il est démontré, mais à une référence où son analogue pour les faisceaux de torsion l'est.

B) A l'exception de la formule de Lefschetz et de (2.12), les résultats de cohomologie étale utilisés dans cet article sont tous démontrés dans SGA 4. Pour ceux déjà énoncés, les références sont : définition des H$^{i}$ : VII; définition des H$_{e}^{i}$ : XVII 5.1; théorème de finitude : XIV 1, complété en XVII 5.3; dimension cohomologique : X; dualité de Poincaré : XVIII.

C) La relation entre les divers Frobenius ((1.4), (1.11), (1.15)) est expliquée en détail dans SGA 5, XV, §§1, 2.

D) L'interprétation cohomologique des fonctions Z (1.14.3) est clairement exposée dans [1]; toutefois, la formule de Lefschetz (1.12), pour X une courbe projective et lisse, y est utilisée, mais non démontrée. Pour la démonstration, il faut, hélas, renvoyer à SGA 5.

E) La forme (2.12) du théorème de dualité de Poincaré résulte du résultat général SGA 4, XVIII (3.2.5) (pour $\mathbf{S} = \operatorname{Spec}(k)$, $\mathbf{X} = \mathbf{X}$, $\mathbf{K} = j_{*}\mathcal{F}$, $\mathbf{L} = \mathbf{Q}_{\ell}$) par un calcul local qui n'est pas difficile. L'énoncé figurera explicitement dans la version définitive de SGA 5. Dans le cas où nous l'utiliserons (ramification de $\mathcal{F}$ modérée), on pourrait l'obtenir par voie transcendante, en relevant $\mathbf{X}$ et $\mathcal{F}$ en caractéristique o.

## 3. La majoration fondamentale.

Le résultat de ce paragraphe a été catalysé par la lecture de Rankin [3].

(3.1) Soient  $U_{0}$  une courbe sur  $F_{q}$ , complément dans  $P^{1}$  d'un ensemble fini de points fermés, U la courbe sur  $\overline{F}_{q}$  qui s'en déduit, u un point fermé de U,  $F_{0}$  un  $Q_{\ell}$ -faisceau constant tordu sur  $U_{0}$  et F son image réciproque sur U.

Soit $\beta\in\mathbf{Q}$. Nous dirons que $\mathcal{F}_{0}$ est de $poids$$\beta$ si pour tout $x\in|\mathrm{U}_{0}|$, les valeurs propres de $\mathrm{F}_{x}$ agissant sur $\mathcal{F}_{0}$ (1.13) sont des nombres algébriques dont tous les conjugués complexes sont de valeur absolue $q_{x}^{\beta/2}$. Par exemple, $\mathbf{Q}_{t}(r)$ est de poids $-2r$.

Théorème (3.2). — Faisons les hypothèses suivantes :

(i)  $F_{0}$  est muni d'une forme bilinéaire alternée non dégénérée

$$
\psi : \mathcal {F} _ {0} \otimes \mathcal {F} _ {0} \rightarrow \mathbf {Q} _ {\ell} (- \beta) \quad (\beta \in \mathbf {Z}).
$$

(ii) L'image de $\pi_1(\mathbf{U}, u)$ dans $\mathrm{GL}(\mathcal{F}_u)$ est un sous-groupe ouvert du groupe symplectique $\mathrm{Sp}(\mathcal{F}_u, \psi_u)$.

(iii) Pour tout $x \in |\mathbf{U}_0|$, le polynôme $\det(\mathrm{i} - \mathrm{F}_x t, \mathcal{F}_0)$ est à coefficients rationnels.

Alors, F est de poids β.

On peut supposer, et nous supposerons, que U est affine et que $\mathcal{F} \neq 0$.

Lemme (3.3). — Soit 2k un entier pair et notons $\otimes\mathcal{F}_{0}$ la puissance tensorielle $(2k)^{\mathrm{ieme}}$ de $\mathcal{F}_{0}$. Pour $x\in|U_{0}|$, la dérivée logarithmique

$$
t \frac {d}{d t} \log (\det (\mathrm{i} - \mathrm{F} _ {x} t ^ {\deg (x)}, \overset {2 k} {\otimes} \mathcal {F} _ {0}) ^ {- 1})
$$

est une série formelle à coefficients rationnels positifs.

L'hypothèse (iii) assure que, pour tout $n$, $\operatorname{Tr}(\mathbf{F}_x^n, \mathcal{F}_0) \in \mathbf{Q}$. Le nombre

$$
\operatorname{Tr} \left(\mathrm{F} _ {x} ^ {n}, \stackrel {{2 k}} {\otimes} \mathcal {F} _ {0}\right) = \operatorname{Tr} \left(\mathrm{F} _ {x} ^ {n}, \mathcal {F} _ {0}\right) ^ {2 k}
$$

est donc rationnel positif, et on applique (1.5.3).

Lemme (3.4). — Les facteurs locaux  $\det(\mathrm{I}-\mathrm{F}_{x}t^{\deg(x)},\bigotimes_{2^{n}}\mathcal{F}_{0})^{-1}$  sont des séries formelles à coefficients rationnels positifs.

La série formelle  $\log\det(\mathrm{I}-\mathrm{F}_{x}t^{\deg(x)},\bigotimes\mathcal{F}_{0})^{-1}$  est sans terme constant; d'après (3.3), ses coefficients sont  $\geq0$ ; les coefficients de son exponentielle sont donc également positifs.

Lemme (3.5). — Soit $f_i = \sum_{n} a_{i,n} t^n$ une suite de séries formelles de terme constant un, et à coefficients réels positifs. On suppose que l'ordre de $f_i - 1$ tend vers l'infini avec $i$, et on pose $f = \prod_{i} f_i$. Alors, le rayon de convergence absolue de $f_i$ est au moins égal à celui de $f$.

Si $f = \sum_{n} a_{n} t^{n}$, on a en effet $a_{i,n} \leq a_{n}$.

Lemme (3.6). — Sous les hypothèses de (3.5), si f et les $f_{i}$ sont les développements en série de Taylor de fonctions méromorphes, alors

$$
\inf \{| z | | f (z) = \infty \} \leq \inf \{| z | | f _ {i} (z) = \infty \}.
$$

Ces nombres sont en effet les rayons de convergence absolue.

284

(3.7) Pour chaque partition P de  $[1, 2k]$  en parties à deux éléments  $\{i_{\alpha}, j_{\alpha}\} (i_{\alpha} < j_{\alpha})$ , on définit

$$
\psi_ {\mathrm{P}}: \stackrel {2 k} {\otimes} \mathcal {F} _ {0} \rightarrow \mathbf {Q} _ {\ell} (- k \beta): x _ {1} \otimes \dots \otimes x _ {2 k} \mapsto \prod_ {\alpha} \psi (x _ {i _ {\alpha}}, x _ {j _ {\alpha}}).
$$

Soit $x$ un point fermé de $\mathbf{X}$. L'hypothèse (ii) assure que les coinvariants de $\pi_1(\mathbf{U}, u)$ dans $\bigotimes_{2k} \mathcal{F}_u$ sont les coinvariants dans $\bigotimes_{2k} \mathcal{F}_u$ du groupe symplectique tout entier ($\pi_1$ est Zariski-dense dans Sp). Soit $\mathcal{P}$ l'ensemble des partitions P. D'après H. Weyl (The classical groups, Princeton University Press, chap. VI, § 1), pour $\mathcal{P}' \subset \mathcal{P}$ convenable, dépendant de $\dim(\mathcal{F}_u)$, les $\psi_P$ pour $\mathrm{P} \in \mathcal{P}'$ définissent un isomorphisme

$$
(\overset {2 k} {\otimes} \mathcal {F} _ {u}) _ {\pi_ {1}} = (\overset {2 k} {\otimes} \mathcal {F} _ {u}) _ {\mathrm{Sp}} \stackrel {{\sim}} {{\to}} \mathbf {Q} _ {\ell} (- k \beta) ^ {\mathcal {P} ^ {\prime}}.
$$

Soit N le nombre d'éléments de $\mathcal{P}'$. D'après (2.10), la formule ci-dessus donne

$$
\mathrm{H} _ {c} ^ {2} (\mathbf {U}, \stackrel {{2 k}} {\otimes} \mathcal {F}) \simeq \mathbf {Q} _ {\ell} (- k \beta - \mathrm{i}) ^ {\mathrm{N}}.
$$

Puisque $\mathrm{H}_c^0 (\mathbf{U},\bigotimes^{\mathcal{A}\mathfrak{n}}\mathcal{F}) = 0$ , la formule (1.14.3) se réduit à

$$
Z (U _ {0}, \overset {2 k} {\otimes} \mathcal {F} _ {0}, t) = \frac {\det (\mathrm{I} - F ^ {*} t , H ^ {1} (U , \overset {2 k} {\otimes} \mathcal {F}))}{(\mathrm{I} - q ^ {k \beta + 1} t) ^ {N}}.
$$

Cette fonction $Z$ est donc le développement en série de Taylor d'une fonction rationnelle n'ayant de pôle qu'en $t = \mathrm{i} / q^{k\beta + 1}$. Nous utiliserons seulement le fait que les pôles sont de valeur absolue $\mathrm{i} / q^{k\beta + 1}$ dans $\mathbf{C}$. Cela pourrait se déduire d'arguments généraux sur les groupes réductifs. Si $\alpha$ est une valeur propre de $F_x$ sur $\mathcal{F}_0$, alors $\alpha^{2k}$ est une valeur propre de $F_x$ sur $\bigotimes_{2k} \mathcal{F}_0$. Notons encore $\alpha$ un quelconque conjugué complexe de $\alpha$. La puissance inverse $\mathrm{i} / \alpha^{2k/\deg(x)}$ est un pôle de $\det(\mathrm{i} - \mathrm{F}_x t^{\deg(x)}, \bigotimes_{2k} \mathcal{F})^{-1}$. D'après (3.4) et (3.6), on a donc

$$
\left| \mathrm{I} / q ^ {k \beta + 1} \right| \leq \left| \mathrm{I} / \alpha^ {2 k / \deg (x)} \right|,
$$

soit

$$
| \alpha | \leq q _ {x} ^ {\frac {\beta}{2} + \frac {1}{2 k}}.
$$

Faisant tendre k vers l'infini, on trouve que

$$
| \alpha | \leq q _ {x} ^ {\beta / 2}.
$$

Par ailleurs, l'existence de $\psi$ assure que $q_x^\beta \alpha^{-1}$ est également valeur propre, d'où l'inégalité

$$
\mid q _ {x} ^ {\beta} \alpha^ {- 1} \mid \leq q _ {x} ^ {\beta / 2}
$$

soit

$$
q _ {x} ^ {\beta / 2} \leq | \alpha |.
$$

Ceci achève la démonstration.

Corollaire (3.8). — Soit $\alpha$ une valeur propre de $\mathbf{F}^*$ agissant sur $\mathrm{H}_c^1 (\mathbf{U},\mathcal{F})$. Alors, $\alpha$ est un nombre algébrique, dont tous les conjugués complexes vérifient

$$
| \alpha | \leq q ^ {\frac {\beta + 1}{2} + \frac {1}{2}}.
$$

La formule (1.14.3) pour $\mathcal{F}_{0}$ se réduit à

$$
\mathbf {Z} (\mathrm{U} _ {0}, \mathcal {F} _ {0}, t) = \det (\mathrm{i} - \mathrm{F} ^ {*} t, \mathrm{H} _ {c} ^ {1} (\mathrm{U}, \mathcal {F})).
$$

Le premier membre est une série formelle à coefficients rationnels, vu son développement en produit et l'hypothèse (iii). Le second membre est donc un polynôme à coefficients rationnels;  $1/\alpha$  en est racine. Ceci prouve déjà que  $\alpha$  est algébrique. Pour achever la démonstration, il suffit de vérifier que le produit infini qui définit  $Z(U_{0},\mathcal{F}_{0},t)$  converge

absolument (donc est non nul) pour $|t| < q^{\frac{-\beta}{2} - 1}$.

Soit N le rang de F, et posons

$$
\det (\mathrm{I} - \mathrm{F} _ {x} t, \mathcal {F}) = \prod_ {i = 1} ^ {\mathrm{N}} (\mathrm{I} - \alpha_ {i, x} t).
$$

D'après (3.2), $|\alpha_{i,x}| = q_x^{\beta/2}$. La convergence du produit infini Z résulte de celle de la série

$$
\sum_ {i, x} \left| \alpha_ {i, x} t ^ {\deg (x)} \right|.
$$

Pour $|t| = q^{\frac{-\beta}{2} - 1 - \varepsilon}$ ($\varepsilon > 0$), on a

$$
\sum_ {i, x} \left| \alpha_ {i, x} t ^ {\deg (x)} \right| = N \sum_ {x} q _ {x} ^ {- 1 - \varepsilon}.
$$

Sur la droite affine, il y a  $q^{n}$  points à valeurs dans  $F_{q^{n}}$ , donc au plus  $q^{n}$  points fermés de degré n. On a donc

$$
\sum_ {x} q _ {x} ^ {- 1 - \varepsilon} \leq \sum_ {n} q ^ {n}. q ^ {n (- 1 - \varepsilon)} = \sum_ {n} q ^ {- n \varepsilon} <   \infty ,
$$

ce qui achève la démonstration.

Corollaire (3.9) — Soient $j_{0}$ l'inclusion de $\mathbf{U}_{0}$ dans $\mathbf{P}_{\mathbf{F}_{q}}^{1}$, $j$ celle de $\mathbf{U}$ dans $\mathbf{P}^{1}$, et $\alpha$ une valeur propre de $\mathbf{F}^{*}$ agissant sur $\mathrm{H}^{1}(\mathbf{P}^{1}, j_{*}\mathcal{F})$. Alors $\alpha$ est un nombre algébrique, dont tous les conjugués complexes vérifient

$$
q ^ {\frac {\beta + 1}{2} - \frac {1}{2}} \leq | \alpha | \leq q ^ {\frac {\beta + 1}{2} + \frac {1}{2}}.
$$

Un segment de la suite longue de cohomologie définie par la suite exacte courte

$$
0 \rightarrow j _ {!} \mathcal {F} \rightarrow j _ {*} \mathcal {F} \rightarrow j _ {*} \mathcal {F} / j _ {!} \mathcal {F} \rightarrow 0
$$

$(j_{!}=\text{prolongement par o}) \text{s'écrit}$

$$
\mathrm{H} _ {c} ^ {1} (\mathrm{U}, \mathcal {F}) \rightarrow \mathrm{H} ^ {1} (\mathbf {P} ^ {1}, j _ {*} \mathcal {F}) \rightarrow 0.
$$

La valeur propre $\alpha$ apparaît donc déjà dans $\mathrm{H}_{c}^{1}(\mathrm{U},\mathcal{F})$, et est justiciable de (3.8) :

$$
| \alpha | \leq q ^ {\frac {\beta + 1}{2} + \frac {1}{2}}.
$$

La dualité de Poincaré (2.12) assure que $q^{\beta + 1}\alpha^{-1}$ est également valeur propre, d'où l'inégalité

$$
\left| q ^ {\beta + 1} \alpha^ {- 1} \right| \leq q ^ {\frac {\beta + 1}{2} + \frac {1}{2}}
$$

et le corollaire.

## 4. La théorie de Lefschetz : théorie locale.

(4.1) Sur C, les résultats locaux de Lefschetz sont les suivants.

Soient  $D=\{z||z|<1\}$  le disque unité,  $D^{*}=D-\{0\}$ , et  $f:X\to D$  un morphisme d'espaces analytiques. On suppose que

a) X est non singulier, et purement de dimension  $n+1$ ;

b) $f$ est propre;

c) $f$ est lisse en dehors d'un point $x$ de la fibre spéciale $\mathbf{X}_{0}=f^{-1}(0)$;

d) en x, f présente un point quadratique non dégénéré.

Soient $t \neq 0$ dans D et $X_t = f^{-1}(t)$ « la » fibre générale. Aux données précédentes, on associe :

α) des morphismes de spécialisation  $sp: H^{i}(X_{0}, \mathbf{Z}) \to H^{i}(X_{t}, \mathbf{Z})$  :  $X_{0}$  est un rétracte par déformation de X, et sp est la flèche composée

$$
\mathrm{H} ^ {i} (\mathrm{X} _ {0}, \mathbf {Z}) \stackrel {{\sim}} {{\leftarrow}} \mathrm{H} ^ {i} (\mathrm{X}, \mathbf {Z}) \rightarrow \mathrm{H} ^ {i} (\mathrm{X} _ {t}, \mathbf {Z});
$$

β) des transformations de monodromie T: H$^{i}$(X$_{t}$, Z) → H$^{i}$(X$_{t}$, Z), qui décrivent l'effet sur les cycles singuliers de X$_{t}$ de « faire tourner t autour de o ». C'est encore l'action sur H$^{i}$(X$_{t}$, Z), fibre en t du système local R$^{i}$f$_{*}$Z|D\*, du générateur positif de $\pi_{1}$(D\*, t).

La théorie de Lefschetz décrit $\alpha$ et $\beta$ en terme du cycle évanescent $\delta\in\mathrm{H}^{n}(\mathbf{X}_{t},\mathbf{Z})$. Ce cycle est bien défini au signe près. Pour $i\neq n$, $n+1$, on a

$$
\mathrm{H} ^ {i} \left(\mathrm{X} _ {0}, \mathbf {Z}\right) \stackrel {{\sim}} {{\rightarrow}} \mathrm{H} ^ {i} \left(\mathrm{X} _ {t}, \mathbf {Z}\right) \quad (i \neq n, n + 1).
$$

Pour $i = n, n + 1$, on a une suite exacte

$$
0 \rightarrow H ^ {n} (X _ {0}, \mathbf {Z}) \rightarrow H ^ {n} (X _ {t}, \mathbf {Z}) \xrightarrow {x \mapsto (x , \delta)} \mathbf {Z} \rightarrow H ^ {n + 1} (X _ {0}, \mathbf {Z}) \rightarrow H ^ {n + 1} (X _ {t}, \mathbf {Z}) \rightarrow 0.
$$

Pour $i \neq n$, la monodromie T est l'identité. Pour $i = n$, on a

$$
\mathrm{T} x = x \pm (x, \delta) \delta .
$$

Les valeurs de ce ±, de Tδ, et de (δ, δ) sont les suivantes :

$$
\begin{array}{l l l l l} n \bmod 4 & \text {0} & \text {I} & 2 & 3 \\ \mathrm{T} x = x \pm (x, \delta) \delta & - & - & + & + \\ (\delta , \delta) & 2 & 0 & - 2 & 0 \\ \mathrm{T} \delta & - \delta & \delta & - \delta & \delta \end{array}
$$

La transformation de monodromie T respecte la forme d'intersection  $\mathrm{Tr}(x\cup y)$  sur  $\mathrm{H}^{n}(\mathbf{X}_{t},\mathbf{Z})$ . Pour n impair, c'est une transvection symplectique. Pour n pair, c'est une symétrie orthogonale.

(4.2) Voici l'analogue de (4.1) en géométrie algébrique abstraite. Le disque D est remplacé par le spectre d'un anneau de valuation discrète hensélien A à corps résiduel algébriquement clos. Soient S ce spectre, η son point générique (spectre du corps des fractions de A), s son point fermé (spectre du corps résiduel). Le rôle de t est joué par un point générique géométrique  $\overline{\eta}$  (spectre d'une clôture algébrique du corps des fractions de A).

Soit $f: \mathbf{X} \to \mathbf{S}$ un morphisme propre, avec $\mathbf{X}$ régulier purement de dimension $n+1$. On suppose $f$ lisse, sauf pour un point quadratique ordinaire $x$ dans la fibre spéciale $\mathbf{X}_s$. Soit $\ell$ un nombre premier différent de la caractéristique résiduelle $p$ de S. Notant $\mathbf{X}_{\overline{\eta}}$ la fibre générique géométrique, on dispose encore d'un morphisme de spécialisation

$$
s p: \mathrm{H} ^ {i} (\mathrm{X} _ {s}, \mathbf {Q} _ {\ell}) \precsim \mathrm{H} ^ {i} (\mathrm{X}, \mathbf {Q} _ {\ell}) \rightarrow \mathrm{H} ^ {i} (\mathrm{X} _ {\overline {{\eta}}}, \mathbf {Q} _ {\ell}).\tag{4.2.1}
$$

Le rôle de T est joué par l'action du groupe d'inertie  $\mathbf{I}=\mathbf{Gal}(\overline{\eta}/\eta)$ , agissant sur  $\mathbf{H}^{i}(\mathbf{X}_{\overline{\eta}},\mathbf{Q}_{\ell})$  par transport de structure (cf. (1.15)):

$$
\mathbf {I} = \operatorname{Gal} (\overline {{{\eta}}} / \eta) \rightarrow \operatorname{GL} \left(\mathrm{H} ^ {i} \left(\mathrm{X} _ {\overline {{{\eta}}}}, \mathbf {Q} _ {\ell}\right)\right).\tag{4.2.2}
$$

Les données (4.2.1), (4.2.2) décrivent entièrement les faisceaux  $R^{i}f_{*}Q_{\ell}$  sur S.

(4.3) Posons $n = 2m$ pour $n$ pair, et $n = 2m + 1$ pour $n$ impair. (4.2.1) et (4.2.2) se décrivent encore en terme d'un cycle évanescent

$$
\delta \in \mathrm{H} ^ {n} (\mathrm{X} _ {\overline {{\eta}}}, \mathbf {Q} _ {\ell}) (m).\tag{4.3.1}
$$

Ce cycle est bien défini au signe près.

Pour $i \neq n, n + 1$, on a

$$
\mathrm{H} ^ {i} (\mathrm{X} _ {s}, \mathbf {Q} _ {\ell}) \stackrel {{\sim}} {{\to}} \mathrm{H} ^ {i} (\mathrm{X} _ {\overline {{{{\eta}}}}}, \mathbf {Q} _ {\ell}) \quad (i \neq n, n + 1).\tag{4.3.2}
$$

Pour $i = n, n + 1$, on a une suite exacte

$$
0 \rightarrow H ^ {n} (X _ {s}, \mathbf {Q} _ {\ell}) \rightarrow H ^ {n} (X _ {\bar {\eta}}, \mathbf {Q} _ {\ell}) \xrightarrow {x \mapsto \operatorname{Tr} (x \cup \delta)} \mathbf {Q} _ {\ell} (m - n) \rightarrow H ^ {n + 1} (X _ {s}, \mathbf {Q} _ {\ell}) \rightarrow H ^ {n + 1} (X _ {\bar {\eta}}, \mathbf {Q} _ {\ell}) \rightarrow 0.\tag{4.3.3}
$$

L'action (4.2.2) de I (la monodromie locale) est triviale si $i \neq n$. Pour $i = n$, elle se décrit comme suit.

A) n impair. — On dispose d'un homomorphisme canonique

$$
t _ {\ell}: \mathbf {I} \rightarrow \mathbf {Z} _ {\ell} (\mathrm{I}),
$$

et l'action de $\sigma\in\mathbf{I}$ est

288

$$
x \mapsto x \pm t _ {\ell} (\sigma) (x, \delta) \delta .
$$

B) n pair. — Ce cas ne nous servira pas. Disons seulement que, si  $p \neq 2$ , il existe un unique caractère d'ordre deux

$$
\varepsilon : \mathrm{I} \rightarrow \{\pm \mathrm{I} \},
$$

et qu'on a

$$
\begin{array}{l l l} \sigma x = x & \text { si } & \varepsilon (\sigma) = \mathrm{I} \\ \sigma x = x \pm (x, \delta) \delta & \text { si } & \varepsilon (\sigma) = - \mathrm{I}. \end{array}
$$

Les signes ± dans A) et B) sont les mêmes qu'en (4.1).

(4.4) Ces résultats apportent les informations suivantes sur les  $R^{i}f_{*}Q_{\ell}$ .

a) $Si \delta \neq 0$ :

1) Pour $i \neq n$, le faisceau $\mathbf{R}^i f_* \mathbf{Q}_\ell$ est constant.

2) Soit j l'inclusion de η dans S. On a

$$
\mathbf {R} ^ {n} f _ {*} \mathbf {Q} _ {\ell} = j _ {*} j ^ {*} \mathbf {R} ^ {n} f _ {*} \mathbf {Q} _ {\ell}.
$$

b) Si $\delta = 0$: (C'est là un cas exceptionnel. Puisque $(\delta, \delta) = \pm 2$ pour $n$ pair, il ne peut se produire que pour $n$ impair.)

1) Pour $i \neq n + 1$, le faisceau $\mathbf{R}^i f_* \mathbf{Q}_\ell$ est constant.

2) Soit $\mathbf{Q}_{\ell}(m-n)_s$ le faisceau $\mathbf{Q}_{\ell}(m-n)$ sur $\{s\}$, prolongé par zéro sur S. On a une suite exacte

$$
0 \rightarrow \mathbf {Q} _ {\ell} (m - n) _ {s} \rightarrow \mathrm{R} ^ {n + 1} f _ {*} \mathbf {Q} _ {\ell} \rightarrow j _ {*} j ^ {*} \mathrm{R} ^ {n + 1} f _ {*} \mathbf {Q} _ {\ell} \rightarrow 0,
$$

$\mathrm{ou} j_{*}j^{*}\mathbf{R}^{n + 1}f_{*}\mathbf{Q}_{\ell}$ est un faisceau constant.

## 5. La théorie de Lefschetz : théorie globale.

(5.1) Sur C, les résultats de Lefschetz sont les suivants. Soient P un espace projectif de dimension  $\geq1$ , et  $\check{P}$  l'espace projectif dual; ses points paramétrisent les hyperplans de P, et on note  $H_{t}$  l'hyperplan défini par  $t\in\check{P}$ . Si A est un sous-espace linéaire de codimension 2 de P, les hyperplans contenant A sont paramétrés par les points d'une droite  $D\subset\check{P}$ , la duale de A. Ces hyperplans  $(\mathrm{H}_{t})_{t\in\mathbb{D}}$  forment le pinceau d'axe A.

Soit $X \subset P$ une variété projective non singulière connexe et de dimension $n + 1$. Soit $\widetilde{X} \subset X \times D$ l'ensemble des couples $(x, t)$ tels que $x \in H_t$. Les applications première et seconde coordonnée forment un diagramme

$$
\begin{array}{c} \text {X} \xleftarrow {\pi} \widetilde {\text {X}} \\ \Big \downarrow_ {f} \\ \text {D} \end{array}\tag{5.1.1}
$$

La fibre de $f$ en $t\in\mathbf{D}$ est la section hyperplane $\mathbf{X}_{t}=\mathbf{X}\cap\mathbf{H}_{t}$ de $\mathbf{X}$.

289

Fixons X, et prenons A assez général. Alors :

A) A est transverse à X, et  $\tilde{X}$  se déduit de X par éclatement de  $A \cap X$ . En particulier,  $\tilde{X}$  est non singulier.

B) Il existe une partie finie S de D et pour chaque $s\in\mathbf{S}$ un point $x_{s}\in\mathbf{X}_{s}$, tels que $f$ soit lisse en dehors des $x_{s}$.

C) Les  $x_{s}$  sont des points critiques non dégénérés de f.

Pour chaque $s\in\mathbf{S}$, la théorie de Lefschetz locale (4.1) s'applique donc à un petit disque $\mathbf{D}_{s}$ autour de $s$ et à $f^{-1}(\mathbf{D}_{s})$.

(5.2) On pose U=D-S. Soit  $u \in U$ , et choisissons des lacets disjoints  $(\gamma_{s})_{s \in S}$  partant de u, avec  $\gamma_{s}$  tournant une fois autour de s :

![](images/page_18_image_6.jpg)

Ces lacets engendrent le groupe fondamental $\pi_{1}(\mathbf{U},u)$. Ce groupe agit sur $\mathrm{H}^{i}(\mathbf{X}_{u},\mathbf{Z})$, fibre en $u$ du système local $\mathbb{R}^{i}f_{*}\mathbf{Z}|\mathbf{U}$. D'après la théorie locale (4.1), à chaque $s\in S$ correspond un cycle évanescent $\delta_{s}\in\mathrm{H}^{n}(\mathbf{X}_{u},\mathbf{Z})$; ces cycles dépendent du choix des $\gamma_{s}$. Pour $i\neq n$, l'action de $\pi_{1}(\mathbf{U},u)$ sur $\mathrm{H}^{i}(\mathbf{X}_{u},\mathbf{Z})$ est triviale. Pour $i=n$, on a

$$
\gamma_ {s} x = x \pm (x, \delta_ {s}) \delta_ {s}.\tag{5.2.1}
$$

Soit E le sous-espace de  $\mathrm{H}^{n}(\mathbf{X}_{u},\mathbf{Q})$  engendré par les  $\delta_{s}$  (partie évanescente de la cohomologie).

Proposition (5.3). — E est stable sous l'action du groupe de monodromie $\pi_{1}(U, u)$. L'orthogonal $E^{\perp}$ de E (pour la forme d'intersection $\operatorname{Tr}(x \cup y)$) est le sous-espace des invariants de la monodromie dans $H^{n}(X_{u}, Q)$.

Les $\gamma_{s}$ engendrant le groupe de monodromie, c'est clair sur (5.2.1).

Théorème (5.4). — Les cycles évanescents ±δs (pris au signe près) sont conjugués sous l'action de π₁(U, u).

Soit $\check{\mathbf{X}}\subset\check{\mathbf{P}}$ la variété duale de $\mathbf{X}$: c'est l'ensemble des $t\in\check{\mathbf{P}}$ tels que $\mathbf{H}_{t}$ soit tangent à $\mathbf{X}$, i.e. tels que $\mathbf{X}_{t}$ soit singulier, ou que $\mathbf{X}\subset\mathbf{H}_{t}$. La variété $\check{\mathbf{X}}$ est irré-

ductible. Soit  $Y \subset X \times P$  l'espace des couples  $(x, t)$  tels que  $x \in H_{t}$ . On dispose d'un diagramme

$$
\begin{array}{c} \text {X} \leftarrow \text {Y} \\ \Big \downarrow_ {g} \\ \check {\mathbf {P}} \end{array}
$$

La fibre de $g$ en $t\in\breve{\mathbf{P}}$ est la section hyperplane $\mathbf{X}_{t}=\mathbf{X}\cap\mathbf{H}_{t}$ de $\mathbf{X}$, et $g$ est lisse en dehors de l'image réciproque de $\breve{\mathbf{X}}$.

On retrouve la situation de (5.1) en remplaçant  $\check{P}$  par une droite  $D\subset\check{P}$  et Y par  $g^{-1}(D)$ . On a  $S=D\cap\check{X}$ . D'après un théorème de Lefschetz, pour D assez générale, l'application

$$
\pi_ {1} (\mathbf {D} - \mathbf {S}, u) \rightarrow \pi_ {1} (\check {\mathbf {P}} - \check {\mathbf {X}}, u)
$$

est surjective. Il suffit donc de montrer que les  $\pm\delta_{s}$  sont conjugués sous  $\pi_{1}(\breve{\mathbf{P}}-\breve{\mathbf{X}})$ .

Pour $x$ dans le lieu lisse de codimension 1 de $\check{\mathbf{X}}$, soient $ch$ un chemin de $t$ à $x$ dans $\check{\mathbf{P}} - \check{\mathbf{X}}$, et $\gamma_x$ le lacet qui suit $ch$ jusqu'au voisinage de $\check{\mathbf{X}}$, tourne une fois autour de $\check{\mathbf{X}}$, puis revient à $t$ par $ch$. Les lacets $\gamma_x$ (pour $ch$ variable) sont conjugués entre eux. Puisque $\check{\mathbf{X}}$ est irréductible, deux points du lieu lisse de $\check{\mathbf{X}}$ peuvent toujours, dans $\check{\mathbf{X}}$, être joints par un chemin qui ne quitte pas le lieu lisse. Il en résulte que la classe de conjugaison de $\gamma_x$ ne dépend pas de $x$. En particulier, les $\gamma_s$ sont conjugués entre eux. On lit sur (5.2.1) que ceci implique la conjugaison des $\pm \delta_s$.

Corollaire (5.5). — L'action de $\pi_1(\mathrm{U}, u)$ sur $\mathrm{E}/(\mathrm{E} \cap \mathrm{E}^\perp)$ est absolument irréductible.

Soit $\mathbf{F} \subset \mathbf{E} \otimes \mathbf{C}$ un sous-espace stable sous la monodromie. Si $\mathbf{F} \nsubseteq (\mathbf{E} \cap \mathbf{E}^{\perp}) \otimes \mathbf{C}$, il existe $x \in \mathbf{F}$ et $s \in \mathbf{S}$ tels que $(x, \delta_s) \neq 0$. On a alors

$$
\gamma_ {s} x - x = \pm (x, \delta_ {s}) \delta_ {s} \in \mathbf {F},
$$

et $\delta_s \in \mathbf{F}$. D'après (5.4), tous les $\delta_s$ sont alors dans $\mathbf{F}$, et $\mathbf{F} = \mathbf{E}$. Ceci prouve (5.5).

(5.6) Ces résultats se transposent comme suit en géométrie algébrique abstraite.

Soient $\mathbf{P}$ un espace projectif de dimension $>1$ sur $k$ algébriquement clos de caractéristique $p$ et $\mathbf{X} \subset \mathbf{P}$ une variété projective non singulière connexe et de dimension $n+1$. Pour A un sous-espace linéaire de $\mathbf{P}$ de codimension 2, on définit comme en (5.1) D et le pinceau $(\mathbf{H}_t)_{t \in \mathbb{D}}$, les $\mathbf{X}_t$, $\widetilde{\mathbf{X}}$ et le diagramme (5.1.1). On dit que les $(\mathbf{X}_t)_{t \in \mathbb{D}}$ forment un pinceau de Lefschetz de sections hyperplanes si les conditions suivantes sont vérifiées :

A) L'axe A est transverse à X. L'espace  $\tilde{X}$  se déduit alors de X par éclatement de  $A \cap X$ , et est lisse.

B) Il existe une partie finie S de D et pour chaque  $s \in S$  un point  $x_{s} \in X_{s}$ , tels que f soit lisse en dehors des  $x_{s}$ .

C) $x_{s}$ est un point singulier quadratique ordinaire de $\mathbf{X}_s$.

Pour chaque $s\in\mathbf{S}$, la théorie de Lefschetz locale du § 4 s'applique au spectre $\mathbf{D}_{s}$ de l'hensélisé de l'anneau local de D en $s$, et à $\widetilde{\mathbf{X}}_{\mathbf{D}_{s}}=\widetilde{\mathbf{X}}\times_{\mathbf{D}}\mathbf{D}_{s}$.

(5.7) Soient N la dimension de P, r un entier  $\geq1$ , et  $\iota_{(r)}$  le plongement de P dans l'espace projectif de dimension  $\binom{N+r}{N}-1$ , de coordonnées homogènes les monômes de degré r en les coordonnées homogènes de P. Les sections hyperplanes de  $\iota_{(r)}(\mathbf{P})$  sont les hypersurfaces de degré r de P.

Si $p \neq 0$, il se peut qu'aucun pinceau de sections hyperplanes de X ne soit de Lefschetz. Toutefois, si $r \geq 2$ et qu'on remplace le plongement projectif donné $\iota_1: X \hookrightarrow P$ par $\iota_r = \iota_{(r)} \circ \iota_1$, alors, dans ce nouveau plongement, tout pinceau assez général est de Lefschetz. En d'autres termes, si $r \geq 2$, un pinceau assez général de sections hypersurfaces de degré $r$ de X est toujours de Lefschetz.

(5.8) Dans la suite de cette discussion, nous étudions un pinceau de Lefschetz de sections hyperplanes de X, en excluant le cas $p=2$, n pair. Le cas où n est impair nous suffirait pour la suite. On pose U=D-S. Soient $u\in U$ et $\ell$ un nombre premier $\neq p$. Les résultats locaux du § 4 montrent que R$^{n}$f$_{*}$Q$_{\ell}$ est modérément ramifié en chaque $s\in S$. Le groupe fondamental modéré de U est un quotient du complété profini du groupe fondamental transcendant analogue (relèvement en caractéristique o des revêtements modérés, et théorème d'existence de Riemann). La situation algébrique est dès lors toute pareille à la situation transcendante, et la transposition de résultats de Lefschetz se fait par des arguments standards. Dans la démonstration de (5.4), le théorème de Lefschetz sur les $\pi_{1}$ devient le théorème de Bertini, et on doit invoquer le lemme d'Abhyankar pour contrôler la ramification de R$^{•}$g$_{*}$Q$_{\ell}$ le long du lieu lisse de codimension un de $\check{X}$.

Les résultats sont les suivants.

a) Si les cycles évanescents sont non nuls :

1) Pour $i \neq n$, le faisceau $\mathbf{R}^i f_* \mathbf{Q}_\ell$ sur D est constant.

2) Soit j l'inclusion de U dans D. On a

$$
\mathrm{R} ^ {n} f _ {*} \mathbf {Q} _ {\ell} = j _ {*} j ^ {*} \mathrm{R} ^ {n} f _ {*} \mathbf {Q} _ {\ell}.
$$

3) Soit $\mathbf{E} \subset \mathbf{H}^n(\mathbf{X}_u, \mathbf{Q}_t)$ le sous-espace de la cohomologie engendré par les cycles évanescents. Ce sous-espace est stable sous $\pi_1(\mathbf{U}, u)$, et

$$
\mathbf {E} ^ {\perp} = \mathrm{H} ^ {n} (\mathrm{X} _ {u}, \mathbf {Q} _ {\ell}) ^ {\pi_ {1} (\mathrm{U}, u)}.
$$

La représentation de $\pi_{1}(\mathbf{U}, u)$ sur $\mathbf{E}/(\mathbf{E} \cap \mathbf{E}^{\perp})$ est absolument irréductible, et l'image de $\pi_{1}$ dans $\mathbf{GL}(\mathbf{E}/(\mathbf{E} \cap \mathbf{E}^{\perp}))$ est engendrée (topologiquement) par les $x \to x \pm (x, \delta_{s})\delta_{s}$ ($s \in \mathbf{S}$) (le signe $\pm$ étant déterminé comme en (4.1)).

b) Si les cycles évanescents sont nuls : (C'est là un cas exceptionnel. Puisque $(\delta, \delta) = \pm 2$ pour $n$ pair, il ne peut se produire que pour $n$ impair : $n = 2m + 1$. On notera que si un cycle évanescent est nul, ils le sont tous, car conjugués.)

1) Pour $i \neq n + 1$, le faisceau $\mathbf{R}^i f_* \mathbf{Q}_\ell$ est constant.

2) On a une suite exacte

$$
0 \rightarrow \bigoplus_ {s \in S} \mathbf {Q} _ {\ell} (m - n) _ {s} \rightarrow R ^ {n + 1} f _ {*} \mathbf {Q} _ {\ell} \rightarrow \mathcal {F} \rightarrow 0
$$

avec $\mathcal{F}$ constant.

3) $\mathbf{E} = \mathbf{0}$.

(5.9) Le sous-espace  $E \cap E^{\perp}$  de E est le noyau de la restriction à E de la forme d'intersection  $\operatorname{Tr}(x \cup y)$ . Cette forme induit donc une forme bilinéaire non dégénérée

$$
\psi : \mathrm{E} / (\mathrm{E} \cap \mathrm{E} ^ {\perp}) \otimes \mathrm{E} / (\mathrm{E} \cap \mathrm{E} ^ {\perp}) \rightarrow \mathbf {Q} _ {\ell} (- n),
$$

alternée pour n impair, et symétrique pour n pair. Cette forme est respectée par la monodromie; pour n impair, la représentation de monodromie induit donc

$$
\rho : \pi_ {1} (\mathrm{U}, u) \rightarrow \operatorname{Sp} (\mathrm{E} / (\mathrm{E} \cap \mathrm{E} ^ {\perp}), \psi).
$$

Théorème (5.10) (Kajdan-Margulis). — L'image de ρ est ouverte.

L'image de $\rho$ est un sous-groupe compact, donc analytique $\ell$-adique, de $\mathrm{Sp}(\mathrm{E}/(\mathrm{E}\cap\mathrm{E}^{\perp}),\psi)$. Il suffit de montrer que son algèbre de Lie $\mathfrak{L}$ est égale à $\mathfrak{sp}(\mathrm{E}/(\mathrm{E}\cap\mathrm{E}^{\perp}),\psi)$. L'analogue transcendant de cette algèbre de Lie est l'algèbre de Lie de l'adhérence de Zariski du groupe de monodromie.

On déduit de (5.8) que $\mathfrak{L}$ est engendrée par les transformations de carré nul

$$
\mathbf {N} _ {s}: x \mapsto (x, \delta_ {s}) \delta_ {s} \quad (s \in \mathbf {S})
$$

et que  $\mathbf{E}/(\mathbf{E}\cap\mathbf{E}^{\perp})$  est une représentation absolument irréductible de L. Le théorème résulte du lemme suivant.

Lemme (5.11). — Soient V un espace vectoriel de dimension finie sur un corps k de caractéristique o, $\psi$ une forme alternée non dégénérée et $\mathfrak{L}$ une sous-algèbre de Lie de $\mathfrak{sp}(V,\psi)$. On suppose que :

(i) V est une représentation simple de L.

(ii) $\mathfrak{L}$ est engendrée par une famille d'endomorphismes de V de la forme $x\mapsto\psi(x,\delta)\delta$. Alors, $\mathfrak{L}=\mathfrak{sp}(V,\psi)$.

On peut supposer et on supposera que V, donc $\mathfrak{L}$, est non nul. Soit $W\subset V$ l'ensemble des $\delta\in V$ tels que $N(\delta):x\mapsto\psi(x,\delta)\delta$ soit dans $\mathfrak{L}$.

a) W est stable par homothétie (car $\mathfrak{L}$ est un sous-espace vectoriel de $\mathfrak{gl}(\mathbf{V})$).

b) Si $\delta\in W$, $\exp(\lambda N(\delta))$ est un automorphisme de $(V,\psi,\mathfrak{L})$, donc transforme $W$ en lui-même. Si $\delta'$, $\delta''\in W$, on a donc $\exp(\lambda N(\delta'))$. $\delta''=\delta''+\lambda\psi(\delta'',\delta')\delta'\in W$; si $\psi(\delta',\delta'')\neq0$, le sous-espace vectoriel tendu par $\delta'$ et $\delta''$ est dans $W$.

c) Il en résulte que W est réunion de ses sous-espaces linéaires maximaux  $W_{\alpha}$ , et que ceux-ci sont deux à deux orthogonaux. Chaque  $W_{\alpha}$  est dès lors stable sous les  $N(\delta)$  ( $\delta \in W$ ), donc stable sous L. Vu l'hypothèse (i),  $W_{\alpha} = V$  et L contient tous les  $N(\delta)$  pour  $\delta \in V$ . On conclut en notant que l'algèbre de Lie  $\mathfrak{sp}(V, \psi)$  est engendrée par les  $N(\delta)$  ( $\delta \in V$ ).

Remarque (5.12) (inutile pour la suite). — Il est maintenant facile de prouver (1.6) pour une hypersurface de dimension impaire n dans  $P_{F_{q}}^{n+1}$ .

Soient  $X_{0}$  une telle hypersurface, et  $\overline{X}_{0}$  l'hypersurface sur  $\overline{F}_{q}$  qui s'en déduit par extension des scalaires. On a

$$
\mathrm{H} ^ {2 i} (\overline {{{\mathrm{X}}}} _ {0}, \mathbf {Q} _ {\ell}) = \mathbf {Q} _ {\ell} (- i) \quad (0 \leq i \leq n);
$$

$H^{2i}(\bar{X}_{0},\mathbf{Q}_{\ell}(i))$ est engendré par la $i^{\text{ème}}$ cup-puissance de $\eta$, la classe de cohomologie $c_{1}(\mathcal{O}(1))$ d'une section hyperplane. On a donc

$$
\mathrm{Z} \left(\mathrm{X} _ {0}, t\right) = \det \left(\mathrm{I} - \mathrm{F} ^ {*} t, \mathrm{H} ^ {n} \left(\overline {{\mathrm{X}}} _ {0}, \mathbf {Q} _ {\ell}\right)\right) / \prod_ {i = 0} ^ {n} (\mathrm{I} - q ^ {i} t)
$$

et  $\det(\mathrm{I}-\mathrm{F}^{*}t,\mathrm{H}^{n}(\overline{\mathbf{X}}_{0},\mathbf{Q}_{\ell}))$  est un polynôme à coefficients entiers indépendants de  $\ell$ .

Faisons varier  $X_{0}$  dans un pinceau de Lefschetz d'hypersurfaces, qui soit défini sur  $F_{q}$  (cf. (5.7) pour  $X=P^{n+1}$ ; l'existence d'un tel pinceau n'est pas claire; si on voulait compléter l'argument esquissé ici, il faudrait recourir aux arguments qui seront donnés en (7.1)). On vérifie que E coïncide ici avec le  $H^{n}$  tout entier, et (3.2) fournit la conjecture de Weil pour toutes les hypersurfaces du pinceau, en particulier pour  $X_{0}$ .

(5.13) Indications bibliographiques sur les §§ 4 et 5.

A) Les résultats de Lefschetz (4.1) et (5.1) à (5.5) sont contenus dans son livre [2]. Pour la théorie locale (4.1), il peut être plus commode de consulter SGA 7, XIV (3.2).

B) Les résultats du § 4 sont démontrés dans les exposés XIII, XIV et XV de SGA 7.

C) (5.7) est démontré dans SGA 7, XVII.

D) (5.8) est démontré dans SGA 7, XVIII. Le théorème d'irréductibilité y est démontré pour E, mais seulement sous l'hypothèse que $\mathbf{E} \cap \mathbf{E}^{\perp} = \{\mathbf{o}\}$. La démonstration dans le cas général (pour $\mathbf{E}/(\mathbf{E} \cap \mathbf{E}^{\perp})$) est pareille.

## 6. Un théorème de rationalité.

(6.1) Soient  $P_{0}$  un espace projectif de dimension  $\geq r$  sur  $F_{q}$ ,  $X_{0} \subset P_{0}$  une variété projective non singulière,  $A_{0} \subset P_{0}$  un sous-espace linéaire de codimension deux,  $D_{0} \subset \check{P}_{0}$  la droite duale,  $\overline{F}_{q}$  une clôture algébrique de  $F_{q}$  et P, X, A, D sur  $\overline{F}_{q}$  déduits de  $P_{0}$ ,  $X_{0}$ ,

295

$A_{0}$ ,  $D_{0}$  par extension des scalaires. Le diagramme (5.1.1) de (5.6) provient d'un diagramme analogue sur  $F_{q}$ :

$$
\begin{array}{c} \mathrm{X} _ {0} \xleftarrow {\pi_ {0}} \widetilde {\mathrm{X}} _ {0} \\ \Big \downarrow f _ {0} \\ \mathrm{D} _ {0} \end{array}\tag{6.1.1}
$$

On suppose que X est connexe de dimension paire  $n+1=2m+2$ , et que le pinceau  $(\mathbf{X}_{t})_{t\in\mathbb{D}}$  de sections hyperplanes de X défini par D est un pinceau de Lefschetz. L'ensemble S des  $t\in D$  tels que  $X_{t}$  soit singulier est défini sur  $F_{q}$ , i.e. provient de  $S_{0}\subset D_{0}$ . On pose  $U_{0}=D_{0}-S_{0}$  et U=D-S.

Soit $u\in\mathbf{U}$. La partie évanescente de la cohomologie $\mathbf{E}\subset\mathbf{H}^{n}(\mathbf{X}_{u},\mathbf{Q}_{t})$ est stable sous $\pi_{1}(\mathbf{U},u)$, donc définit sur U un sous-système local $\mathcal{E}$ de $\mathbf{R}^{n}f_{*}\mathbf{Q}_{t}$. Ce dernier est défini sur $\mathbf{F}_{q}:\mathbf{R}^{i}f_{*}\mathbf{Q}_{t}$ est l'image réciproque du $\mathbf{Q}_{t}$-faisceau $\mathbf{R}^{i}f_{0*}\mathbf{Q}_{t}$ sur $\mathbf{D}_{0}$, et, sur U, $\mathcal{E}$ est l'image réciproque d'un sous-système local

$$
\mathcal {E} _ {0} \subset \mathrm{R} ^ {n} f _ {0 *} \mathbf {Q} _ {\ell}.
$$

Le cup-produit est une forme alternée

$$
\psi : \mathrm{R} ^ {n} f _ {0 *} \mathbf {Q} _ {\ell} \otimes \mathrm{R} ^ {n} f _ {0 *} \mathbf {Q} _ {\ell} \rightarrow \mathbf {Q} _ {\ell} (- n).
$$

Notant $\mathcal{E}_{0}^{\perp}$ l'orthogonal de $\mathcal{E}_{0}$ relativement à $\psi$, dans $\mathrm{R}^{n}f_{0*}\mathbf{Q}_{\ell}|\mathrm{U}_{0}$ on voit que $\psi$ induit une dualité parfaite

$$
\psi : \mathcal {E} _ {0} / (\mathcal {E} _ {0} \cap \mathcal {E} _ {0} ^ {\perp}) \otimes \mathcal {E} _ {0} / (\mathcal {E} _ {0} \cap \mathcal {E} _ {0} ^ {\perp}) \rightarrow \mathbf {Q} _ {\ell} (- n).
$$

Théorème (6.2). — Pour tout  $x \in |U_{0}|$ , le polynôme  $\det(\mathrm{I}-\mathrm{F}_{x}^{*}t, \mathcal{E}_{0}/(\mathcal{E}_{0} \cap \mathcal{E}_{0}^{\perp}))$  est à coefficients rationnels.

Corollaire (6.3). — Soiert $j_{0}$ l'inclusion de $\mathbf{U}_{0}$ dans $\mathbf{D}_{0}$, et $j$ celle de $\mathbf{U}$ dans $\mathbf{D}$. Les valeurs propres de $\mathbf{F}^{*}$ agissant sur $\mathrm{H}^{1}(\mathrm{D}, j_{*}\mathcal{E}/(\mathcal{E} \cap \mathcal{E}^{\perp}))$ sont des nombres algébriques dont tous les conjugués complexes $\alpha$ vérifient

$$
q ^ {\frac {n + 1}{2} - \frac {1}{2}} \leq | \alpha | \leq q ^ {\frac {n + 1}{2} + \frac {1}{2}}.
$$

D'après (5.10) et (6.2), les hypothèses de (3.2) sont en effet vérifiées par $(\mathbf{U}_0, \mathcal{E}_0 / (\mathcal{E}_0 \cap \mathcal{E}_0^\perp), \psi)$, pour $\beta = n$, et on applique (3.9).

Lemme (6.4). — Soit $\mathcal{G}_{0}$ un $\mathbf{Q}_{\ell}$-faisceau constant tordu sur $\mathbf{U}_{0}$, tel que son image réciproque $\mathcal{G}$ sur U soit un faisceau constant. Il existe alors dans $\overline{\mathbf{Q}}_{\ell}$ des unités $\alpha_{i}$ telles que, pour tout $x\in|\mathbf{U}_{0}|$, on ait

$$
\det (\mathrm{I} - \mathrm{F} _ {x} ^ {*} t, \mathcal {G} _ {0}) = \prod_ {i} (\mathrm{I} - \alpha_ {i} ^ {\deg (x)} t).
$$

Ce lemme exprime que $\mathcal{G}_{0}$ est l'image réciproque d'un faisceau sur $\operatorname{Spec}(\mathbf{F}_{q})$, à savoir son image directe sur $\operatorname{Spec}(\mathbf{F}_{q})$. Ce dernier s'identifie à une représentation $\ell$-adique $\mathbf{G}_{0}$ de $\operatorname{Gal}(\overline{\mathbf{F}}_{q}/\mathbf{F}_{q})$, et on prend

$$
\det (\mathrm{I} - \mathrm{F} t, \mathrm{G} _ {0}) = \prod_ {i} (\mathrm{I} - \alpha_ {i} t).
$$

Le lemme (6.4) s'applique aux $\mathbf{R}^i f_{0*}\mathbf{Q}_\ell$ ($i\neq n$), à $\mathbf{R}^n f_{0*}\mathbf{Q}_\ell/\mathcal{E}_0$ et à $\mathcal{E}_0\cap\mathcal{E}_0^\perp$.

Pour $x \in |U_0|$ la fibre $X_x = f_0^{-1}(x)$ est une variété sur le corps fini $k(x)$. Si $\bar{x}$ est un point de U au-dessus de $x$, $X_{\bar{x}}$ se déduit de $X_x$ par extension des scalaires de $k(x)$ à sa clôture algébrique $k(\bar{x}) = \overline{\mathbf{F}}_q$, et $H^i(X_{\bar{x}}, Q_\ell)$ est la fibre de $R^i f_*Q_\ell$ en $\bar{x}$. La formule (1.5.4) pour la variété $X_x$ sur $k(x)$ s'écrit donc

$$
Z \left(\mathrm{X} _ {x}, t\right) = \prod_ {i} \det \left(\mathrm{I} - \mathrm{F} _ {x} ^ {*} t, \mathrm{R} ^ {i} f _ {0 *} \mathbf {Q} _ {\ell}\right) ^ {(- 1) ^ {i + 1}}
$$

et $\mathbf{Z}(\mathbf{X}_x,t)$ est le produit de

$$
\mathbf {Z} ^ {f} = \det (\mathrm{I} - \mathrm{F} _ {x} ^ {*} t, \mathrm{R} ^ {n} f _ {0 *} \mathbf {Q} _ {\ell} / \mathcal {E} _ {0}). \det (\mathrm{I} - \mathrm{F} _ {x} ^ {*} t, \mathcal {E} _ {0} \cap \mathcal {E} _ {0} ^ {\perp}). \prod_ {i \neq n} \det (\mathrm{I} - \mathrm{F} _ {x} ^ {*} t, \mathrm{R} ^ {i} f _ {0 *} \mathbf {Q} _ {\ell}) ^ {(- 1) ^ {i + 1}}
$$

par

$$
Z ^ {m} = \det (\mathrm{I} - \mathrm{F} _ {x} ^ {*} t, \mathcal {E} _ {0} / (\mathcal {E} _ {0} \cap \mathcal {E} _ {0} ^ {\perp})).
$$

Posons $\mathcal{F}_{0}=\mathcal{E}_{0}/(\mathcal{E}_{0}\cap\mathcal{E}_{0}^{\perp})$, $\mathcal{F}=\mathcal{E}/(\mathcal{E}\cap\mathcal{E}^{\perp})$ et appliquons (6.4) aux facteurs de $Z^{f}$. On trouve qu'il existe des unités $\ell$-adiques $\alpha_{i}$ ($1\leq i\leq N$) et $\beta_{j}$ ($1\leq j\leq M$) dans $\overline{\mathbf{Q}}_{t}$ tels que pour tout $x\in|U_{0}|$

$$
\mathrm{Z} (\mathrm{X} _ {x}, t) = \frac {\prod_ {i} \left(\mathrm{I} - \alpha_ {i} ^ {\deg x} t\right)}{\prod_ {j} \left(\mathrm{I} - \beta_ {j} ^ {\deg x} t\right)}. \det (\mathrm{I} - \mathrm{F} _ {x} ^ {*} t, \mathcal {F} _ {0})
$$

et qu'en particulier le second membre est dans $\mathbf{Q}(t)$. Si un $\alpha_{i}$ coïncide avec un $\beta_{j}$, il est loisible de supprimer simultanément cet $\alpha_{i}$ de la liste des $\alpha$ et ce $\beta_{j}$ de la liste des $\beta$. On peut donc supposer, et nous supposerons, que $\alpha_{i} \neq \beta_{j}$ pour tout $i$ et tout $j$.

(6.5) Il suffit de prouver que les polynômes $\prod_{i} (1 - \alpha_{i} t)$ et $\prod_{j} (1 - \beta_{j} t)$ sont à coefficients rationnels, i.e. que la famille des $\alpha_{i}$ (resp. la famille des $\beta_{j}$) est définie sur $\mathbf{Q}$. Nous le déduirons des propositions suivantes.

Proposition (6.6). — Soient $(\gamma_i)$ ($1 \leq i \leq P$) et $(\delta_j)$ ($1 \leq j \leq Q$) deux familles d'unités $l$-adiques dans $\overline{\mathbf{Q}}_l$. On suppose que $\gamma_i \neq \delta_j$. Si K est un ensemble fini assez grand d'entiers $\neq 1$, et L une partie de densité o assez grande de $|U_0|$, alors, si $x \in |U_0|$ vérifie $k \nmid \deg(x)$ (pour tout $k \in K$) et $x \notin L$, le dénominateur de

$$
\det (\mathrm{I} - \mathrm{F} _ {x} ^ {*} t, \mathcal {F} _ {0}) \prod_ {i} (\mathrm{I} - \gamma_ {i} ^ {\deg (x)} t) / \prod_ {j} (\mathrm{I} - \delta_ {j} ^ {\deg (x)} t),\tag{6.6.1}
$$

écrit sous forme irréductible, est $\prod_{j} (\mathrm{I} - \delta_{j}^{\deg(x)} t)$.

La démonstration sera donnée en (6.10-13). D'après (6.7) ci-dessous, (6.6) fournit 296

297

une description intrinsèque de la famille des $\delta_{j}$ en terme de la famille des fractions rationnelles (6.6.1) pour $x\in|U_{0}|$.

Lemme (6.7). — Soient K un ensemble fini d'entiers ≠ 1 et (δj) (1 ≤ j ≤ Q) et (εj) (1 ≤ j ≤ Q) deux familles d'éléments d'un corps. Si, pour tout n assez grand, non divisible par aucun des k ∈ K, la famille des δj^n coïncide avec celle des εj^n (à l'ordre près), alors la famille des δj coïncide avec celle des εj (à l'ordre près).

On procède par récurrence sur Q. L'ensemble des entiers n tels que  $\delta_{Q}^{n}=\varepsilon_{j}^{n}$  est un idéal  $(n_{j})$ . Prouvons qu'il existe  $j_{0}$  tel que  $\delta_{Q}=\varepsilon_{j_{0}}$ . Sinon les  $n_{j}$  seraient distincts de 1, et il existerait des entiers arbitrairement grands n, non divisibles par aucun des  $n_{j}$ , ni par aucun des  $k\in K$ . On aurait  $\delta_{Q}^{n}\neq\varepsilon_{j}^{n}$ , et ceci contredirait l'hypothèse. Il existe donc  $j_{0}$  tel que  $\delta_{Q}=\varepsilon_{j_{0}}$ . On conclut en appliquant l'hypothèse de récurrence aux familles  $(\delta_{j})(j\neq Q)$  et  $(\varepsilon_{j})(j\neq j_{0})$ .

Proposition (6.8). — Soient  $(\gamma_{i})$  (I ≤ i ≤ P) et  $(\delta_{j})$  (I ≤ j ≤ Q) deux familles d'unités p-adiques dans  $\overline{Q}_{\ell}$ ,  $\mathrm{R}(t)=\prod_{i}(\mathrm{I}-\gamma_{i}t)$  et  $\mathrm{S}(t)=\prod_{j}(\mathrm{I}-\delta_{j}t)$ . Supposons que pour tout  $x\in|U_{0}|$ ,  $\prod_{i}(\mathrm{I}-\delta_{i}^{\deg(x)}t)$  divise

$$
\prod_ {i} \left(\mathrm{I} - \gamma_ {i} ^ {\deg (x)} t\right). \det (\mathrm{I} - \mathrm{F} _ {x} ^ {*} t, \mathcal {F} _ {0}).
$$

Alors $\mathbf{S}(t)$ divise $\mathbf{R}(t)$.

Supprimons des familles  $(\gamma_{i})$  et  $(\delta_{j})$  des paires d'éléments communs jusqu'à vérifier l'hypothèse de (6.6). Appliquons (6.6). Par hypothèse, les fractions rationnelles (6.6.1) sont des polynômes. Aucun δ n'a donc subsisté, ce qui signifie que  $\mathbf{S}(t)$  divise  $\mathbf{R}(t)$ .

Cette proposition fournit une caractérisation intrinsèque de R(t) en terme de la famille de polynômes

$$
\prod_ {i} \left(\mathrm{I} - \gamma_ {i} ^ {\deg (x)} t\right). \det (\mathrm{I} - \mathrm{F} _ {x} ^ {*} t, \mathcal {F} _ {0}).
$$

C'est le ppcm des polynômes $S(t) = \prod_{j} (1 - \delta_j t)$ vérifiant l'hypothèse de (6.8).

(6.9) Prouvons (6.5) et donc (6.2) (modulo (6.6)). Faisons dans (6.6) $(\gamma_i) = (\alpha_i)$ et $(\delta_j) = (\beta_j)$. On trouve une caractérisation intrinsèque de la famille des $\beta_j$ en terme de la famille de fractions rationnelles $Z(X_x, t) (x \in |U_0|)$. Celles-ci étant dans $\mathbf{Q}(t)$, la famille des $\beta_j$ est définie sur $\mathbf{Q}$.

Les polynômes $\prod_{i} (\mathrm{I} - \alpha_{i}^{\deg(x)} t) \cdot \det(\mathrm{I} - \mathrm{F}_{x}^{*} t, \mathcal{F}_{0})$ sont donc dans $\mathbf{Q}[t]$. La proposition (6.8) fournit une description intrinsèque de la famille des $\alpha_{i}$ en terme de cette famille de polynômes. La famille des $\alpha_{i}$ est donc définie sur $\mathbf{Q}$.

(6.10) Préliminaires. — Soient  $u \in U$  et  $F_{u}$  la fibre de F en u. Le groupe fondamental arithmétique  $\pi_{1}(U_{0}, u)$ , extension de  $\hat{\mathbf{Z}} = \operatorname{Gal}(\overline{\mathbf{F}}_{q}/\mathbf{F}_{q})$  (générateur :  $\varphi$ ) par le groupe fondamental géométrique  $\pi_{1}(U, u)$ , agit sur  $F_{u}$  par similitudes symplectiques :

$$
\rho : \pi_ {1} (\mathrm{U} _ {0}, u) \rightarrow \operatorname{CSp} \left(\mathscr {F} _ {u}, \psi\right).
$$

Nous notons $\mu(g)$ le multiplicateur d'une similitude symplectique $g$. Soit

$$
\mathbf {H} \subset \hat {\mathbf {Z}} \times \operatorname{CSp} \left(\mathscr {F} _ {u}, \psi\right)
$$

le sous-groupe défini par l'équation

$$
q ^ {- n} = \mu (g)
$$

(q étant une unité $\ell$-adique, $q^n \in \mathbf{Q}_\ell^*$ est défini pour tout $n \in \hat{\mathbf{Z}}$). Le fait que $\psi$ soit à valeurs dans $\mathbf{Q}_\ell(-n)$ s'exprime en disant que l'application de $\pi_1$ dans $\hat{\mathbf{Z}} \times \mathrm{CSp}$, de coordonnées la projection canonique sur $\hat{\mathbf{Z}}$ et $\rho$, se factorise par

$$
\rho_ {1}: \pi_ {1} (\mathrm{U} _ {0}, u) \rightarrow \mathrm{H}.
$$

Lemme (6.11). — L'image H$_{1}$ de ρ$_{1}$ est ouverte dans H.

En effet, $\pi_1(\mathbf{U}_0,u)$ se projette sur $\hat{\mathbf{Z}}$, et l'image de $\pi_1(\mathbf{U},u) = \mathrm{Ker}(\pi_1(\mathbf{U}_0,u)\to \hat{\mathbf{Z}})$ dans $\mathrm{Sp}(\mathcal{F}_u,\psi) = \mathrm{Ker}(\mathrm{H}\rightarrow \hat{\mathbf{Z}})$ est ouverte (5.10).

Lemme (6.12). — Pour $\delta\in\overline{\mathbf{Q}}_{\ell}$ une unité $\ell$-adique, l'ensemble Z des $(n,g)\in\mathrm{H}_{1}$ tels que $\delta^{n}$ soit valeur propre de $g$ est un fermé de mesure nulle.

Il est clair que Z est fermé. Pour chaque  $n \in \hat{Z}$ , soit  $CSp_{n}$  l'ensemble des  $g \in \mathrm{CSp}(\mathcal{F}_{u}, \psi)$  tels que  $\mu(g) = q^{-n}$ , et soit  $Z_{n}$  l'ensemble des  $g \in CSp_{n}$  tels que  $\delta^{n}$  soit valeur propre de g. Alors,  $CSp_{n}$  est un espace homogène sous Sp, et on vérifie que  $Z_{n}$  en est un sous-espace algébrique propre, donc de mesure o. D'après (6.11),  $H_{1} \cap (\{n\} \times Z_{n})$  est donc de mesure o dans l'image inverse dans  $H_{1}$  de n, et on applique Fubini à la projection  $H_{1} \to \hat{Z}$ .

(6.13) Prouvons (6.6). Pour chaque $i$ et $j$, l'ensemble des entiers $n$ tels que $\gamma_{i}^{n} = \delta_{j}^{n}$ est l'ensemble des multiples d'un entier fixe $n_{ij}$ (on n'exclut pas $n_{ij} = 0$). Par hypothèse, $n_{ij} \neq 1$.

D'après (6.12) et le théorème de densité de Čebotarev, l'ensemble des $x\in|U_{0}|$ tels qu'un $\beta_{j}^{\mathrm{deg}(x)}$ soit valeur propre de $\mathbf{F}_{x}^{*}$ agissant sur $\mathcal{F}_{0}$ est de densité o. On prend pour K l'ensemble des $n_{ij}$ et pour L l'ensemble des $x$ ci-dessus.

## 7. Fin de la démonstration de 1.7.

Lemme (7.1). — Soit  $X_{0}$  une variété projective non singulière absolument irréductible de dimension paire d sur  $F_{q}$ . Soient X sur  $\overline{F}_{q}$  déduit de  $X_{0}$  par extension des scalaires et  $\alpha$  une valeur propre de  $F^{*}$  agissant sur  $\mathrm{H}^{d}(\mathrm{X},\mathbf{Q}_{\ell})$ . Alors,  $\alpha$  est un nombre algébrique dont tous les conjugués complexes, encore notés  $\alpha$ , vérifient

$$
(7. \mathbf {I}. \mathbf {I})
$$

$$
q ^ {\frac {d}{2} - \frac {1}{2}} \leq | \alpha | \leq q ^ {\frac {d}{2} + \frac {1}{2}}.
$$

On procède par récurrence sur $d$ (toujours supposé pair). Le cas $d=0$ est trivial, même sans supposer $\mathbf{X}_{0}$ absolument irréductible; on suppose dorénavant $d\geq2$. On pose $d=n+1=2m+2$.

298

Si $\mathbf{F}_{q^{r}}$ est une extension de degré $r$ de $\mathbf{F}_{q}$ et que $\mathrm{X}_{0}^{\prime}/\mathbf{F}_{q^{r}}$ se déduit de $\mathrm{X}_{0}/\mathbf{F}_{q}$ par extension des scalaires, l'assertion (7.1) pour $\mathrm{X}_{0}/\mathbf{F}_{q}$ équivaut à (7.1) pour $\mathrm{X}_{0}^{\prime}/\mathbf{F}_{q^{r}}$: de même que $q$ est remplacé par $q^{r}$, les valeurs propres de $\mathbf{F}^{*}$ sont remplacées par leurs puissances $r^{\text{ièmes}}$.

D'après (5.7), dans un plongement projectif convenable $i: \mathbf{X} \to \mathbf{P}$, $\mathbf{X}$ admet un pinceau de Lefschetz de sections hyperplanes. La remarque précédente nous permet de supposer $i$ et ce pinceau définis sur $\mathbf{F}_q$ (quitte à remplacer $\mathbf{F}_q$ par une extension finie).

Supposons donc qu'il existe sur $\mathbf{F}_{q}$ un plongement projectif $\mathbf{X}_{0} \to \mathbf{P}_{0}$ et un sous-espace de codimension deux $\mathbf{A}_{0}$ de $\mathbf{P}_{0}$ qui définisse un pinceau de Lefschetz. On reprend les notations de (6.1) et (6.3). Une nouvelle extension des scalaires nous ramène à supposer que :

a) Les points de S sont définis sur  $F_{q}$ .

b) Les cycles évanescents en $x_{s}$ ($s\in\mathbf{S}$) sont définis sur $\mathbf{F}_{q}$ (puisque seul $\pm\delta$ est intrinsèque, ils pourraient n'être définis que sur une extension quadratique).

c) Il existe un point rationnel $u_0 \in U_0$. On prend le point correspondant $u$ de $U$ comme point base.

$d)\ \mathbf{X}_{u_{0}} = f_{0}^{-1}(u_{0})$ admet une section hyperplane lisse $\mathbf{Y}_{0}$, définie sur $\mathbf{F}_{q}$. On pose $\mathbf{Y} = \mathbf{Y}_{0} \otimes_{\mathbf{F}_{q}} \overline{\mathbf{F}}_{q}$.

Puisque $\tilde{\mathbf{X}}$ se déduit de $\mathbf{X}$ par éclatement de la sous-variété lisse de codimension deux $\mathbf{A} \cap \mathbf{X}$, on a

$$
\mathrm{H} ^ {i} (\mathrm{X}, \mathbf {Q} _ {\ell}) \hookrightarrow \mathrm{H} ^ {i} (\widetilde {\mathrm{X}}, \mathbf {Q} _ {\ell})
$$

(en fait, $\mathrm{H}^i (\widetilde{\mathbf{X}},\mathbf{Q}_t) = \mathrm{H}^i (\mathrm{X},\mathbf{Q}_t)\oplus \mathrm{H}^{i - 2}(\mathrm{A}\cap \mathrm{X},\mathbf{Q}_t)(-\mathrm{i}))$ . Il suffit donc de prouver (7.1.1) pour les valeurs propres $\alpha$ de $\mathbf{F}^*$ agissant sur $\mathrm{H}^d (\widetilde{\mathbf{X}},\mathbf{Q}_t)$

La suite spectrale de Leray pour f s'écrit

$$
\mathrm{E} _ {2} ^ {p q} = \mathrm{H} ^ {p} (\mathrm{D}, \mathrm{R} ^ {q} f _ {*} \mathbf {Q} _ {\ell}) \Rightarrow \mathrm{H} ^ {p + q} (\widetilde {\mathrm{X}}, \mathbf {Q} _ {\ell}).
$$

Il suffit de prouver (7.1.1) pour les valeurs propres $\alpha$ de $\mathbf{F}^*$ agissant sur les $\mathbf{E}_2^{pq}$ pour $p + q = d = n + 1$. Ce sont :

A)  $E_{2}^{2,n-1}$ . D'après (5.8),  $R^{n-1}f_{*}Q_{\ell}$  est constant. D'après (2.10), on a donc

$$
\mathrm{E} _ {2} ^ {2, n - 1} = \mathrm{H} ^ {n - 1} (\mathbf {X} _ {u}, \mathbf {Q} _ {\ell}) (- \mathrm{I}).
$$

D'après le théorème de Lefschetz faible (corollaire de SGA 4, XIV (3.2), et de la dualité de Poincaré, SGA 4, XVIII), on a

$$
\mathrm{H} ^ {n - 1} \left(\mathrm{X} _ {u}, \mathbf {Q} _ {\ell}\right) (- \mathrm{I}) \hookrightarrow \mathrm{H} ^ {n - 1} (\mathrm{Y}, \mathbf {Q} _ {\ell}) (- \mathrm{I}),
$$

et on applique l'hypothèse de récurrence à  $Y_{0}$ .

$$
\mathrm{E} _ {2} ^ {0, n + 1} = \mathrm{H} ^ {n + 1} (\mathrm{X} _ {u}, \mathbf {Q} _ {\ell}).
$$

B)  $E_{2}^{0,n+1}$ . Si les cycles évanescents sont non nuls,  $R^{n+1}f_{*}Q_{\ell}$  est constant et

299

Le morphisme de Gysin

$$
\mathrm{H} ^ {n - 1} (\mathrm{Y}, \mathbf {Q} _ {\ell}) (- \mathrm{i}) \rightarrow \mathrm{H} ^ {n + 1} (\mathrm{X} _ {u}, \mathbf {Q} _ {\ell})
$$

est surjectif (cet argument est dual de A)), et on applique l'hypothèse de récurrence à  $Y_{0}$ .

Si les cycles évanescents sont nuls, la suite exacte de (5.8) b) fournit une suite exacte

$$
\bigoplus_ {s \in \mathrm{S}} \mathbf {Q} _ {\ell} (m - n) \rightarrow \mathrm{E} _ {2} ^ {0, n + 1} \rightarrow \mathrm{H} ^ {n + 1} (\mathrm{X} _ {u}, \mathbf {Q} _ {\ell}).
$$

La valeur propre de F agissant sur  $\mathbf{Q}_{\ell}(m-n)$  est  $q^{d/2}$ , et  $H^{n+1}$  se traite comme plus haut.
C)  $E_{2}^{1,n}$ . Si on disposait du théorème de Lefschetz « difficile », on saurait que  $E \cap E^{\perp}$  est nul, et que  $R^{n}f_{*}Q_{\ell}$  est somme directe de  $j_{*}E$  et d'un faisceau constant. Le  $H^{1}$  d'un faisceau constant sur  $P^{1}$  est nul, et il suffirait d'appliquer (6.3).

Faute d'avoir déjà démontré Lefschetz « difficile », il nous va falloir dévisser. Si les cycles évanescents sont nuls,  $R^{n}f_{*}Q_{\ell}$  est constant ((5.8) b)) et  $E_{2}^{1,n}=0$ . On peut donc supposer, et on supposera, les cycles évanescents non nuls. Filtrons  $R^{n}f_{*}Q_{\ell}=j_{*}j^{*}R^{n}f_{*}Q_{\ell}$  (5.8) par les sous-faisceaux  $j_{*}\mathcal{E}$  et  $j_{*}(\mathcal{E}\cap\mathcal{E}^{\perp})$ . Si les cycles évanescents δ ne sont pas dans  $\mathcal{E}\cap\mathcal{E}^{\perp}$ , on dispose de suites exactes :

$$
\mathrm{o} \rightarrow j _ {*} \mathcal {E} \rightarrow \mathrm{R} ^ {n} f _ {*} \mathbf {Q} _ {\ell} \rightarrow \text { faisceau   constant } \rightarrow \mathrm{o}.\tag{7.1.2}
$$

(7.1.3) o→faisceau constant  $j_{*}(\mathcal{E}\cap\mathcal{E}^{\perp})\rightarrow j_{*}\mathcal{E}\rightarrow j_{*}(\mathcal{E}/(\mathcal{E}\cap\mathcal{E}^{\perp}))\rightarrow0.$

Si, à Dieu ne plaise, les δ sont dans $\mathcal{E} \cap \mathcal{E}^{\perp}$, on a $\mathcal{E} \subset \mathcal{E}^{\perp}$, et des suites exactes :

(7.1.4) o→le faisceau constant  $j_{*}E^{\perp}\rightarrow R^{n}f_{*}Q_{\ell}\rightarrow$  un faisceau  $F\rightarrow o$

(7.1.5) $\mathrm{o}\rightarrow \mathcal{F}\rightarrow \mathrm{le}$ faisceau constant $j_{*}j^{*}\mathcal{F}\rightarrow \bigoplus_{s\in S}\mathbf{Q}_{\ell}(n - m)_{s}\rightarrow 0.$

Dans le premier cas, les suites exactes longues de cohomologie fournissent

(7.1.2')

$$
\mathrm{H} ^ {1} (\mathrm{D}, j _ {*} \mathcal {E}) \rightarrow \mathrm{H} ^ {1} (\mathrm{R} ^ {n} f _ {*} \mathbf {Q} _ {\ell}) \rightarrow 0,\tag{7.1.3'}
$$

$$
\mathrm{o} \rightarrow \mathrm{H} ^ {1} (\mathrm{D}, j _ {*} \mathcal {E}) \rightarrow \mathrm{H} ^ {1} (\mathrm{D}, j _ {*} (\mathcal {E} / (\mathcal {E} \cap \mathcal {E} ^ {\perp})))
$$

et on applique (6.3).

Dans le second cas, elles fournissent

$$
(7. \mathbf {I}. 4 ^ {\prime})
$$

$$
\mathrm{o} \rightarrow \mathrm{H} ^ {1} (\mathrm{D}, \mathrm{R} ^ {n} f _ {*} \mathbf {Q} _ {\ell}) \rightarrow \mathrm{H} ^ {1} (\mathrm{D}, \mathscr {F}),\tag{7.1.5'}
$$

$$
\bigoplus_ {s \in \mathbb {S}} \mathbf {Q} _ {\ell} (n - m) \rightarrow \mathrm{H} ^ {1} (\mathrm{D}, \mathcal {F}) \rightarrow 0
$$

et on remarque que F agit sur $\mathbf{Q}_{\ell}(n - m)$ par multiplication par $q^{d / 2}$.

Lemme (7.2). — Soit  $X_{0}$  une variété projective non singulière absolument irréductible de dimension d sur  $F_{q}$ . Soient X sur  $\overline{F}_{q}$  déduit de  $X_{0}$  par extension des scalaires et  $\alpha$  une valeur propre de  $F^{*}$  agissant sur  $H^{d}(X, Q_{\ell})$ . Alors,  $\alpha$  est un nombre algébrique dont tous les conjugués complexes, encore notés  $\alpha$ , vérifient

$$
| \alpha | = q ^ {d / 2}.
$$

Prouvons déjà que  $(7.2)\Rightarrow(1.7)$ . Pour  $X_{0}$  projective non singulière sur  $F_{q}$  et i un entier, il faut prouver l'assertion suivante :

$W(X_{0,i})$ . Soit X déduit de  $X_{0}$  par extension des scalaires de  $F_{q}$  à  $\overline{F}_{q}$ . Si  $\alpha$  est une valeur propre de  $F^{*}$  agissant sur  $H^{i}(X, Q_{t})$ , alors  $\alpha$  est un nombre algébrique dont tous les conjugués complexes, encore notés  $\alpha$ , vérifient  $|\alpha| = q^{i/2}$ .

a) Si $\mathbf{F}_{q^{n}}$ est une extension de degré $n$ de $\mathbf{F}_{q}$, et que $\mathrm{X}_{0}^{\prime}/\mathbf{F}_{q^{n}}$ se déduit de $\mathrm{X}_{0}/\mathbf{F}_{q}$ par extension des scalaires, alors $\mathrm{W}(\mathrm{X}_{0},i)$ équivaut à $\mathrm{W}(\mathrm{X}_{0}^{\prime},i)$: étendre les scalaires revient à remplacer $\alpha$ par $\alpha^{n}$ et $q$ par $q^{n}$.

b) Si  $X_{0}$  est purement de dimension n,  $W(X_{0}, i)$  équivaut à  $W(X_{0}, 2n-i)$  : ceci résulte de la dualité de Poincaré.

c) Si $\mathbf{X}_0$ est somme de variétés $\mathbf{X}_0^\alpha$, $\mathrm{W}(\mathbf{X}_0, i)$ équivaut à la conjonction des $\mathrm{W}(\mathbf{X}_0^\alpha, i)$.

d) Si  $X_{0}$  est purement de dimension n,  $Y_{0}$  une section hyperplane lisse de  $X_{0}$, et que i < n, alors  $W(Y_{0}, i) \Rightarrow W(X_{0}, i)$ : ceci résulte du théorème de Lefschetz faible.

Pour prouver les assertions $W(X_0, i)$, on se ramène successivement :

— par c), à supposer  $X_{0}$  purement d'une dimension n;

— par b), à supposer de plus  $o \leq i \leq n$ ;

— par a) et d), à supposer de plus i=n;

— par $a)$ et $c)$, à supposer de plus $\mathbf{X}_{0}$ absolument irréductible.

Ce cas est justiciable de (7.2).

(7.3) Prouvons (7.2). Pour tout entier $k$, $\alpha^{k}$ est valeur propre de $\mathbf{F}^{*}$ agissant sur $\mathrm{H}^{kd}(\mathbf{X}^{k}, \mathbf{Q}_{\ell})$ (formule de Künneth). Pour $k$ pair, $\mathbf{X}^{k}$ est justiciable de (7.1), d'où

$$
q ^ {\frac {k d}{2} - \frac {1}{2}} \le | \alpha^ {k} | \le q ^ {\frac {k d}{2} - \frac {1}{2}}
$$

et

$$
q ^ {\frac {d}{2} - \frac {1}{2 k}} \leq | \alpha | \leq q ^ {\frac {d}{2} + \frac {1}{2 k}}.
$$

Faisant tendre $k$ vers l'infini, on trouve (7.2).

## 8. Premières applications.

Théorème (8.1). — Soit  $X_{0} \subset P_{0}^{n+r}$  une intersection complète non singulière sur  $F_{q}$ , de dimension n et de multidegré  $(d_{1}, \ldots, d_{r})$ . Soit  $b'$  le  $n^{ième}$  nombre de Betti des intersections complètes non singulières complexes, de mêmes dimension et multidegré. Posons  $b = b'$  pour n impair, et  $b = b' - 1$  pour n pair. Alors

$$
\mid \# \mathbf {X} _ {0} (\mathbf {F} _ {q}) - \# \mathbf {P} ^ {n} (\mathbf {F} _ {q}) \mid \leq b. q ^ {n / 2}.
$$

Soient $\mathbf{X} / \overline{\mathbf{F}}_q$ déduit de $\mathbf{X}_0$, et $\mathbf{Q}_{\ell}.\eta^i$ la droite dans $\mathrm{H}^{2i}(\mathbf{X},\mathbf{Q}_{\ell})$ engendrée par la $i^{\text{ème}}$ cup-puissance de la classe de cohomologie d'une section hyperplane. Sur cette droite, $\mathbf{F}^*$ agit par multiplication par $q^i$. La cohomologie de $\mathbf{X}$ est somme des $\mathbf{Q}_{\ell}.\eta^i$

$(0 \leq i \leq n)$ et de la partie primitive de $\mathbf{H}^n(\mathbf{X}, \mathbf{Q}_\ell)$, de dimension $b$. D'après (1.5), il existe donc $b$ nombres algébriques $\alpha_j$, les valeurs propres de $\mathbf{F}^*$ agissant sur cette cohomologie primitive, tels que

$$
\# \mathbf {X} _ {0} (\mathbf {F} _ {q}) = \sum_ {i = 0} ^ {n} q ^ {i} + (- \mathrm{I}) ^ {n} \sum_ {j} \alpha_ {j}.
$$

D'après (1.7), $|\alpha_j| = q^{n/2}$ et

$$
\left| \# \mathbf {X} _ {0} (\mathbf {F} _ {q}) - \# \mathbf {P} (\mathbf {F} _ {q}) \right| = \left| \# \mathbf {X} _ {0} (\mathbf {F} _ {q}) - \sum_ {i = 0} ^ {n} q ^ {i} \right| = \left| \sum_ {j} \alpha_ {j} \right| \leq \sum_ {j} \left| \alpha_ {j} \right| = b. q ^ {n / 2}.
$$

Théorème (8.2). — Soient N un entier ≥1, ε : (Z/N)\* → C\* un caractère, k un entier ≥2 et f une forme modulaire holomorphe sur Γ₀(N), de poids k et de caractère ε : f est une fonction holomorphe sur le demi-plan de Poincaré X, telle que pour  $\begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \text{SL}(2, Z)$ , avec  $c \equiv o(N)$ , on ait

$$
f \left(\frac {a z + b}{c z + d}\right) = \varepsilon (a) ^ {- 1} (c z + d) ^ {k} f (z).
$$

On suppose $f$ cuspidale et primitive (« new » au sens d'Atkin-Lehner et de Miyake), en particulier vecteur propre des opérateurs de Hecke $T_p$ ($p \nmid N$). Posons $f = \sum_{n=1}^{\infty} a_n q^n$, avec $q = e^{2\pi iz}$ (et $a_1 = 1$). Alors, pour $p$ premier ne divisant pas $N$

$$
\left| a _ {p} \right| \leq 2. p ^ {\frac {k - 1}{2}}.
$$

En d'autres termes, les racines de l'équation

$$
\mathbf {T} ^ {2} - a _ {p} \mathbf {T} + \varepsilon (p) \cdot p ^ {k - 1}
$$

sont de valeur absolue $p^{\frac{k-1}{2}}$.

Ces racines sont en effet des valeurs propres de Frobenius agissant sur le  $H^{k-1}$  d'une variété projective non singulière de dimension k—i définie sur  $F_{p}$ .

Sous des hypothèses restrictives, ce fait est démontré dans mon exposé Bourbaki (Formes modulaires et représentations ℓ-adiques, exposé 355, février 1969, dans : Lecture Notes in Mathematics, 179). Le cas général n'est pas beaucoup plus difficile.

Remarque (8.3). — J. P. Serre et moi-même avons récemment démontré que (8.2) reste vrai pour $k=1$. La démonstration est toute différente.

L'application suivante m'a été suggérée par E. Bombieri.

Théorème (8.4). — Soient Q un polynôme à n variables et de degré d sur  $F_{q}$ ,  $Q_{d}$  la partie homogène de degré d de Q et  $\psi: F_{q} \to C^{*}$  un caractère additif non trivial sur  $F_{q}$ . On suppose que :

(i) d est premier à p;

(ii) l'hypersurface  $H_{0}$  dans  $P_{F_{q}}^{n-1}$  définie par  $Q_{d}$  est lisse.

302

Alors

$$
\left| \sum_ {x _ {1}, \dots , x _ {n} \in \mathbb {F} _ {q}} \psi (\mathrm{Q} (x _ {1}, \dots , x _ {n})) \right| \leq (d - 1) ^ {n} q ^ {n / 2}.
$$

Quitte à remplacer Q par un multiple scalaire, on peut supposer (et on supposera) que

$$
\psi (x) = \exp (2 \pi i \operatorname{Tr} _ {\mathbf {F} _ {q} / \mathbf {F} _ {p}} (x) / p).\tag{8.4.x}
$$

Soit  $X_{0}$  le revêtement étale de l'espace affine  $A_{0}$  de dimension n sur  $F_{q}$  d'équation  $T^{p}-T=Q$ , et soit  $\sigma$  la projection de  $X_{0}$  sur  $A_{0}$ :

$$
\sigma : \mathrm{X} _ {0} \rightarrow \mathrm{A} _ {0}
$$

$$
\mathbf {X} _ {0} = \operatorname{Spec} \left(\mathbf {F} _ {q} \left[ x _ {1}, \dots , x _ {n}, \mathrm{T} \right] / \left(\mathrm{T} ^ {p} - \mathrm{T} - \mathrm{Q}\right)\right).
$$

Le revêtement  $X_{0}$  est galoisien, de groupe de Galois Z/p;  $i \in Z/p = F_{p}$  agit par  $T \mapsto T + i$ .

Soit $x \in \mathrm{A}_0(\mathbf{F}_q)$ et calculons l'endomorphisme de Frobenius de la fibre de $\mathrm{X}_0 / \mathrm{A}_0$ en $x$. Posons $q = p^f$ et soit $\overline{\mathbf{F}}_q$ une clôture algébrique de $\mathbf{F}_q$. Pour $(x, \mathrm{T}) \in \mathrm{X}_0(\overline{\mathbf{F}}_q)$ au-dessus de $x$, on a $\mathrm{F}((x, \mathrm{T})) = (x, \mathrm{T}^q)$, et

$$
\mathrm{T} ^ {q} = \mathrm{T} + \sum_ {i = 1} ^ {f} (\mathrm{T} ^ {p ^ {i}} - \mathrm{T} ^ {p ^ {i - 1}}) = \mathrm{T} + \sum_ {i} \mathrm{Q} (x) ^ {p ^ {i - 1}} = \mathrm{T} + \mathrm{Tr} _ {\mathbf {F} _ {q} / \mathbf {F} _ {p}} (\mathrm{Q} (x)).
$$

C'est l'action de l'élément $\mathrm{Tr}_{\mathbf{F}_q / \mathbf{F}_p}(\mathbb{Q}(x))$ du groupe de Galois.

Soient E le corps des racines $p^{\text{ièmes}}$ de l'unité et $\lambda$ une place finie de E première à $p$. Nous travaillerons en cohomologie $\lambda$-adique. Pour $j \in \mathbf{Z} / p$, soit $\mathcal{F}_{j,0}$ le $E_{\lambda}$-système local de rang un sur $A_0$ défini par $X_0$ et $\psi(-jx): Z / p \to E^* \to E_\lambda^*$: on dispose de $\iota: X_0 \to \mathcal{F}_{j,0}$ et $\iota(i*x) = \psi(-ji)\iota(x)$. Notons sans $_0$ les objets déduits de $A_0$, $X_0$, $\mathcal{F}_{j,0}$ par extension des scalaires à $\overline{\mathbf{F}}_q$. La formule des traces (1.12.1) pour $\mathcal{F}_{j,0}$ s'écrit

$$
\sum_ {x _ {1}, \dots , x _ {n} \in \mathbb {F} _ {q}} \psi (Q (x _ {1}, \dots , x _ {n})) = \sum_ {i} (- 1) ^ {i} \operatorname{Tr} (F ^ {*}, H _ {c} ^ {i} (A, \mathcal {F} _ {1})).\tag{8.4.2}
$$

On a $\sigma_{*}\mathrm{E}_{\lambda} = \bigoplus_{j}\mathcal{F}_{j}$, et donc

$$
\mathrm{H} _ {c} ^ {*} (\mathrm{X}, \mathbf {Q} _ {\ell}) \otimes_ {\mathbf {q} _ {\ell}} \mathrm{E} _ {\lambda} = \bigoplus_ {j} \mathrm{H} _ {c} ^ {*} (\mathrm{A}, \mathcal {F} _ {j}).\tag{8.4.3}
$$

Pour $j=0$, $\mathcal{F}_{j}$ est le faisceau constant $\mathrm{E}_{\lambda}$; ce facteur correspond à l'inclusion, par image réciproque, de la cohomologie de A dans celle de X.

Lemme (8.5). — (i) Pour $j \neq 0$, $\mathrm{H}_c^i(\mathrm{A}, \mathcal{F}_j)$ est nul pour $i \neq n$; pour $i = n$, cet espace de cohomologie est de dimension $(d - 1)^n$.

(ii) Pour $j \neq 0$, le cup-produit

$$
\mathrm{H} _ {c} ^ {n} (\mathrm{A}, \mathcal {F} _ {j}) \otimes \mathrm{H} _ {c} ^ {n} (\mathrm{A}, \mathcal {F} _ {- j}) \rightarrow \mathrm{H} _ {c} ^ {2 n} (\mathrm{A}, \mathrm{E} _ {\lambda}) \stackrel {\mathrm{Tr}} {\rightarrow} \mathrm{E} _ {\lambda} (- n)
$$

est une dualité parfaite.

(iii)  $X_{0}$  est un ouvert d'une variété projective non singulière  $Z_{0}$ .

Déduisons (8.4) de (8.5). Soient $j_0: \mathbf{X}_0 \hookrightarrow \mathbf{Z}_0$ et $j: \mathbf{X} \hookrightarrow \mathbf{Z}$ déduit par extension des scalaires à $\overline{\mathbf{F}}_q$. D'après (8.4.2), (i), et (1.7) pour $\mathbf{Z}_0$, il suffit de prouver l'injectivité de

$$
\mathrm{H} _ {c} ^ {n} (\mathrm{A}, \mathcal {F} _ {1}) \stackrel {\sigma^ {*}} {\rightarrow} \mathrm{H} _ {c} ^ {n} (\mathrm{X}, \mathcal {F} _ {1}) = \mathrm{H} _ {c} ^ {n} (\mathrm{X}, \mathrm{E} _ {\lambda}) \stackrel {\jmath_ {!}} {\rightarrow} \mathrm{H} ^ {n} (\mathrm{Z}, \mathrm{E} _ {\lambda}).
$$

On a $\operatorname{Tr}(a \cup b) = \frac{\mathrm{I}}{p} \operatorname{Tr}(j_1 \sigma^* a \cup j_1 \sigma^* b)$, donc cette injectivité résulte de (ii).

(8.6) Prouvons (8.5) (iii). Soient  $P_{0}$  l'espace projectif sur  $F_{q}$  complété de  $A_{0}$  par adjonction d'un hyperplan à l'infini  $P_{0}^{\infty}$ ,  $H_{0} \subset P_{0}^{\infty}$  d'équation  $Q_{d}=0$  et  $Y_{0}$  le revêtement de  $P_{0}$  normalisé de  $P_{0}$  dans  $X_{0}$ .

$$
\begin{array}{c c c c c c} \mathrm{X} _ {0} & \hookrightarrow & \mathrm{Y} _ {0} \\ \sigma \Big \downarrow & & \Big \downarrow \\ \mathrm{A} _ {0} & \hookrightarrow & \mathrm{P} _ {0} & \longleftarrow & \mathrm{P} _ {0} ^ {\infty} & \longleftarrow & \mathrm{H} _ {0} \end{array}\tag{8.6.1}
$$

Étudions  $Y_{0}/P_{0}$  près de l'infini, localement pour la topologie étale.

Lemme (8.7). — Y$_{0}$ est lisse en dehors de l'image réciproque de H$_{0}$.

Le diviseur de la fonction rationnelle Q sur  $P_{0}$  est somme de sa partie finie  $\text{div}(Q)_{f}$  et de  $(-d)$  fois l'hyperplan à l'infini. On a :

$$
\begin{array}{c} \operatorname{div} (\mathbf {Q}) = \operatorname{div} (\mathbf {Q}) _ {f} - d \mathrm{P} _ {0} ^ {\infty} \\ \operatorname{div} (\mathbf {Q}) _ {f} \cap \mathrm{P} _ {0} ^ {\infty} = \mathrm{H} _ {0}. \end{array}\tag{8.7.1}
$$

A distance finie,  $Y_{0}=X_{0}$  est étale sur  $A_{0}$ , donc lisse. A l'infini, mais en dehors de l'image réciproque de  $H_{0}$ , il existe des coordonnées locales  $(z_{1},\ldots,z_{n})$  telles que  $Q=z_{1}^{-d}$  (ceci utilise que  $(d,p)=1$ ). Dans ces coordonnées,  $Y_{0}$  apparaît comme produit d'une courbe et d'un espace lisse (correspondant aux coordonnées  $z_{2},\ldots,z_{n}$ ). Par normalité, il est lisse.

Lemme (8.8). — Au voisinage étale d'un point au-dessus de  $H_{0}$ ,  $Y_{0}$  est lisse sur une surface singulière normale, toujours la même.

On peut cette fois trouver des coordonnées locales telles que  $Q=z_{1}^{-d}z_{2}$ . En effet, puisque  $H_{0}$  est lisse,  $\text{div}(Q)_{f}$  est lisse au voisinage de l'infini et coupe  $P_{0}^{\infty}$  transversalement. Cette forme est indépendante du point choisi, et n'utilise que deux coordonnées, d'où l'assertion.

(8.9) On sait que le procédé suivant (dû à Zariski) permet de résoudre les singularités de surfaces : alternativement, on normalise et on éclate le lieu singulier (réduit). Les opérateurs en jeu commutent à la localisation étale et au produit par un espace lisse. Le procédé de Zariski permet donc encore de résoudre les singularités d'un espace qui, comme  $Y_{0}$ , est, localement pour la topologie étale, lisse sur une surface. La résolution obtenue de  $Y_{0}$  est le  $Z_{0}$  cherché.

Si T est une courbe sur une surface S, contenant le lieu singulier, et que T' est l'image réciproque de T dans la résolution de Zariski S' de S, on sait que si on éclate de façon itérée dans S' le lieu singulier (réduit) de  $(\mathrm{T}^{\prime})_{\mathrm{red}}$ , on obtient une surface S'' telle que l'image réciproque réduite  $(\mathrm{T}^{\prime\prime})_{\mathrm{red}}$  de T dans S'' soit un diviseur à croisements normaux. A nouveau, les opérations en jeu commutent à la localisation étale et au produit par un espace lisse. Raisonnant comme plus haut, et observant que  $(\mathrm{Y}_{0}, \mathrm{l}^{\prime}\mathrm{infini})$  est localement lisse sur un  $(\mathrm{S}, \mathrm{T})$ , on peut même trouver  $Z_{0}$  tel que  $Z_{0}-X_{0}$  soit un diviseur à croisements normaux.

(8.10) Prouvons (8.5) (i), (ii). Ce sont des assertions géométriques; ceci nous permet de travailler dorénavant sur $\overline{\mathbf{F}}_q$. Soit S' l'espace affine sur $\overline{\mathbf{F}}_q$ qui paramétrise les polynômes à $n$ variables de degré $\leq d$, et soit S l'ouvert de S' correspondant aux polynômes dont la partie homogène de degré $d$ est de discriminant non nul. On note $\mathrm{Q}_{\mathrm{s}} \in \mathrm{H}^{0}(\mathrm{S}, \mathcal{O}_{\mathrm{s}}[x_{1}, \ldots, x_{n}])$ le polynôme universel sur S, et $\mathrm{X}_{\mathrm{s}}$ le revêtement galoisien étale de $\mathrm{A}_{\mathrm{s}} = \mathrm{A}^{n} \times \mathrm{S}$ d'équation $\mathrm{T}^{p} - \mathrm{T} = \mathrm{Q}_{\mathrm{s}}$, de groupe de Galois $\mathbf{Z}/p$. Soient $\mathrm{P}_{\mathrm{s}} = \mathrm{P}^{n} \times \mathrm{S}$ l'espace projectif sur S complété de $\mathrm{A}_{\mathrm{s}}$ et $\mathrm{Y}_{\mathrm{s}}$ le normalisé de $\mathrm{P}_{\mathrm{s}}$ dans $\mathrm{X}_{\mathrm{s}}$. On dispose, sur S, d'un diagramme analogue à (8.6.1).

Les expressions de Q en coordonnées locales données en (8.7) et (8.8) restent valables dans la situation présente, avec paramètres, de sorte que, localement pour la topologie étale sur  $Y_{S}$ ,  $Y_{S}/S$  est isomorphe au produit de S (qui est lisse) avec une fibre. La méthode canonique de résolution utilisée en (8.9) nous fournit une compactification relative  $Z_{S}/S$  de  $X_{S}/S$ , avec  $Z_{S}-X_{S}$  un diviseur à croisements normaux relatifs sur S

$$
\begin{array}{c c c} \mathrm {X_ {S}} & \stackrel {{u}} {{\hookrightarrow}} & \mathrm {Z_ {S}} \\ \Big \downarrow^ {\sigma} & & \Big \downarrow^ {f} \\ \mathrm {A_ {S}} & \stackrel {{a}} {{\longrightarrow}} & \mathrm{S} \end{array}
$$

(f propre et lisse, u plongement ouvert,  $Z_{s}-X_{s}$  diviseur à croisements normaux relatifs).
Soit  $F_{j,s}$  le  $E_{\lambda}$ -faisceau sur  $A_{s}$  déduit comme en (8.4) de  $X_{s}/A_{s}$ . On a  $\sigma_{*}E_{\lambda}=\bigoplus F_{j,s}$ , donc

$$
\mathrm{R} ^ {*} (f u) _ {1} (\mathrm{E} _ {\lambda}) = \bigoplus_ {j} \mathrm{R} ^ {*} a _ {1} \mathcal {F} _ {j, \mathrm{s}}.
$$

Les propriétés de $Z_S$ assurent que les $R^i(fu)_1 E_\lambda = R^i f_*(u_1 E_\lambda)$ sont des faisceaux localement constants sur S. Dès lors, les $R^i a_1 \mathcal{F}_{j,s}$ également sont localement constants. Puisque S est connexe, il suffit de prouver (8.5) (i), (ii) pour un polynôme Q particulier. On prendra $Q = \sum_{i} x_i^d$. Ce polynôme vérifie la condition de non-singularité car $(d, p) = 1$. Pour ce polynôme, les variables se séparent dans la somme exponentielle de (8.4). Ceci correspond au fait que $\mathcal{F}_j$ est le produit tensoriel des images réciproques de

faisceaux analogues $\mathcal{F}_{j}^{1}$ sur les facteurs de dimension un $A^{1}$ de $A = A^{n}$. Par la formule de Künneth

$$
\mathrm{H} ^ {*} (\mathrm{A}, \mathcal {F} _ {j}) = \bigotimes \mathrm{H} ^ {*} (\mathrm{A} ^ {1}, \mathcal {F} _ {j} ^ {1}).
$$

Ceci ramène la preuve de (8.5) (i), (ii) au cas où $n=\mathrm{i}$ et où $\mathbf{Q}$ est $x^{d}$.

(8.11) Traitons ce cas particulier. Le revêtement X de A est irréductible, de sorte que pour i=0,2

$$
\mathrm{H} _ {c} ^ {i} (\mathrm{A}, \mathrm{E} _ {\lambda}) \stackrel {{\sim}} {{\to}} \mathrm{H} _ {c} ^ {i} (\mathrm{X}, \mathrm{E} _ {\lambda}).
$$

Pour $i \neq 1$ et $j \neq 0$, on a donc

$$
\mathrm{H} _ {c} ^ {i} (\mathrm{A}, \mathcal {F} _ {j}) = 0.
$$

L'assertion (ii) résulte de (2.8) ou (2.12) et de ce que $u_{i}\mathcal{F}_{j} = u_{*}\mathcal{F}_{j}$. Pour prouver (i), il reste à vérifier que

$$
\chi_ {c} (\mathrm{A}, \mathcal {F} _ {j}) = \mathrm{i} - d.
$$

D'après la formule d'Euler-Poincaré (voir l'exposé Bourbaki 286 de février 1965, par M. Raynaud), ceci équivaut au lemme suivant.

Lemme (8.12). — Le conducteur de Swan de $\mathcal{F}_{j}$ à l'infini est égal à $d$.

Cet énoncé équivaut au suivant.

Lemme (8.13). — Soient $k$ un corps fini de caractéristique $p$, $y \in k[[x]]$ un élément de valuation $d$ première à $p$, L l'extension de $\mathbf{K} = k((x))$ engendré par les racines de $\mathrm{T}^p - \mathrm{T} = y^{-1}$ et $\chi$ le caractère suivant de $\operatorname{Gal}(\mathrm{L}/\mathrm{K})$ à valeurs dans $\mathbf{Z}/p$:

$$
\chi (\sigma) = \sigma \mathrm{T} - \mathrm{T}.
$$

Alors, $\chi$ est de conducteur $d + 1$.

Par extension du corps résiduel, on se ramène à supposer $k$ algébriquement clos plutôt que fini, et on applique : J. P. Serre, Sur les corps locaux à corps résiduel algébriquement clos, Bull. Soc. Math. France, 89 (1961), p. 105-154, n° 4.4.

## BIBLIOGRAPHIE

[1] A. GROTHENDIECK, Formule de Lefschetz et rationalité des fonctions L, Séminaire Bourbaki, 279, décembre 1964 (Benjamin).

[2] S. LEFSCHETZ, L'analysis situs et la géométrie algébrique (Gauthier-Villars), 1924. Reproduit dans : Selected papers (Chelsea Publ. Co.).

[3] R. A. RANKIN, Contributions to the theory of Ramanujan's function $\tau(n)$ and similar arithmetical functions. II, Proc. Camb. Phil. Soc., 35 (1939), 351-372.

[4] A. Weil, Numbers of solutions of equations in finite fields, Bull. Am. Math. Soc., 55 (1949), p. 497-508.

SGA, Séminaire de Géométrie Algébrique du Bois-Marie (IHES) :

SGA 4, Théorie des topos et cohomologie étale des schémas (dirigé par M. ARTIN, A. GROTHENDIECK et J.-L. VERDIER), Lecture Notes in Math., 269, 270, 305.

SGA 5, Cohomologie l-adique et fonctions L, diffusé par l'IHES.

SGA 7, Groupes de monodromie en géométrie algébrique.

$^{1re}$ partie : dirigé par A. GROTHENDIECK, Lecture Notes in Math., 288.

$2^{e}$ partie : par P. DELIGNE et N. KATZ, Lecture Notes in Math., 340.

Manuscrit reçu le 20 septembre 1973.