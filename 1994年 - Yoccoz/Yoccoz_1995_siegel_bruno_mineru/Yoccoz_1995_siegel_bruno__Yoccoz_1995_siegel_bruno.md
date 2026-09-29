# Astérisque

JEAN-CHRISTOPHE YOCCOZ
Théorème de Siegel, nombres de Bruno et polynômes quadratiques

Astérisque, tome 231 (1995), p. 1-88

&lt;http://www.numdam.org/item?id=AST_1995__231__1_0&gt;

© Société mathématique de France, 1995, tous droits réservés.

L'accès aux archives de la collection « Astérisque » (http://smf4.emath.fr/Publications/Asterisque/) implique l'accord avec les conditions générales d'utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou impression systématique est constitutive d'une infraction pénale. Toute copie ou impression de ce fichier doit contenir la présente mention de copyright.

NUMDAM
Article numérisé dans le cadre du programme
Numérisation de documents anciens mathématiques
http://www.numdam.org/

1995

# PETITS DIVISEURS EN DIMENSION 1

Jean-Christophe YOCCOZ

## Table des matières

Théorème de Siegel, nombres de Bruno
et polynômes quadratiques ....3
Centralisateurs et conjugaison différentiable
des difféomorphismes du cercle ....89

## THÉORÈME DE SIEGEL, NOMBRES DE BRUNO ET POLYNÔMES QUADRATIQUES Jean-Christophe YOCCOZ

## Table des matières

Introduction ....5
Chapitre I
Linéarisation des fonctions univalentes ....11
1. Préliminaires arithmétiques ....11
2. Linéarisation des fonctions univalentes: résultats et réductions ....17
3. Premières estimations et minoration de R(α) ....25
4. La construction fondamentale ....35
5. Construction d'exemples. Fin de la démonstration du théorème ....45
6. Orbites périodiques s'accumulant sur l'origine ....49
Chapitre II
Linéarisation des polynômes quadratiques ....57
1. Universalité des polynômes quadratiques ....57
2. Une fonction holomorphe remarquable ....64
3. Questions et compléments ....70
Appendice 1
Une remarque sur la linéarisation des germes
dont la partie linéaire n'est pas diagonalisable ....79
Appendice 2
Divergence des séries de Siegel modifiées
lorsque la condition de Bruno est violée ....83
Bibliographie ....87

## INTRODUCTION

1. - L'étude de la dynamique des germes de difféomorphismes holomorphes d'une variable complexe au voisinage d'un point fixe a suscité de nombreux travaux depuis la fin du siècle dernier. Le problème central est de décrire la structure des classes de conjugaison dans le groupe $G$ des germes de difféomorphismes holomorphes de $(\mathbb{C}, 0)$. A cet effet, on dispose d'un invariant de conjugaison évident, la dérivée du germe en 0. Notons, pour tout $\lambda \in \mathbb{C}^*$, par $G_\lambda$ l'ensemble des $f \in G$ tels que $Df(0) = \lambda$. On dira que $f \in G_\lambda$ est linéarisable s'il appartient à la classe de conjugaison dans $G$ de la rotation $R_\lambda(z) = \lambda z$.

Il est raisonnable de considérer d'abord le problème de la conjugaison dans le groupe $\widehat{G}$ des difféomorphismes formels de (C,0). Sans problèmes de convergence, la solution n'est pas difficile. Lorsque $\lambda$ n'est pas racine de l'unité, $\widehat{G}_{\lambda}$ est une classe de conjugaison de $\widehat{G}$, et plus précisément $\widehat{G}_1$ opère librement et transitivement par conjugaison dans $\widehat{G}_{\lambda}$. Lorsque $\lambda = \exp(2\pi ip/q)$ (avec $q \geq 1$, $p \wedge q = 1$) est racine de l'unité, la classe de conjugaison de $R_{\lambda}$ est formée des éléments de $\widehat{G}_{\lambda}$ d'ordre $q$, et les autres classes de conjugaison de $\widehat{G}$ dans $\widehat{G}_{\lambda}$ forment une famille paramétrée par un entier $n \geq 1$ et un nombre complexe $a$, car chaque classe contient exactement un difféomorphisme de la forme :

$$
f _ {n, a} (z) = \lambda z (1 + z ^ {n q} + a z ^ {2 n q}).
$$

Revenant au groupe G, Poincaré a montré ([Po]) que  $G_{\lambda}$  est une classe de conjugaison de G lorsque le module de  $\lambda$  est différent de 1. Les points fixes attractifs ( $|\lambda| < 1$ ) et répulsifs ( $|\lambda| > 1$ ) des difféomorphismes holomorphes sont donc linéarisables.

Lorsque $\lambda = \exp(2\pi ip/q)$ est racine de l'unité, les travaux d'Ecalle [Ec] et Voronin [Vo] ont produit une classification complète des classes de conjugaison de $G$ contenues dans $G_{\lambda}$: la classe de conjugaison de $R_{\lambda}$ est encore formée des éléments de $G_{\lambda}$ d'ordre

q, mais les autres classes forment des familles elle-mêmes paramétrées par des germes de difféomorphismes.

Il reste le cas -le plus intéressant- où $\lambda$ est de module 1 mais n'est pas racine de l'unité. Tout $f \in G_{\lambda}$ est alors formellement linéarisable par un unique élément $H_{f} \in \widehat{G}_{1}$. Une question cruciale est de déterminer l'ensemble $S$ des valeurs de $\lambda$ pour lesquelles la conjugaison $H_{f}$ est convergente pour tout $f \in G_{\lambda}$; c'est l'ensemble des $\lambda$ pour lesquels $G_{\lambda}$ est une classe de conjugaison de $G$.

Les formules déterminant les coefficients de $H_{f}$ font apparaître en dénominateurs des produits de termes $(\lambda^{n}-\lambda)$ ($n\geq2$) qui peuvent être petits et provoquer la divergence de $H_{f}$. C'est la situation non linéaire la plus simple où l'on rencontre ces difficultés liées aux "petits dénominateurs".

On s'attend donc à ce que la nature arithmétique de $\lambda$ joue un rôle prépondérant. Ecrivons $\lambda$ sous la forme $\exp(2\pi i\alpha)$, avec $\alpha$ irrationnel, et considérons la suite $(p_n/q_n)_{n\geq 0}$ des réduites du développement en fraction continue du nombre $\alpha$.

Les premiers résultats significatifs, négatifs, sont dus à Cremer [Cr] : il montre que si l'on a :

$$
\sup _ {n \geq 0} \frac {\operatorname{Log} q _ {n + 1}}{q _ {n}} = + \infty ,\tag{Cr}
$$

alors $H_{f}$ peut diverger, donc $\lambda$ n'appartient pas à $\mathcal{S}$.

Le premier résultat positif est obtenu par Siegel en 1942 ; dans un article bref, mais historique [Si], il montre que la condition :

$$
\mathrm{Log} q _ {n + 1} = \mathcal {O} (\mathrm{Log} q _ {n})\tag{S}
$$

entraîne que tout $f \in G_{\lambda}$ est linéarisable, c'est-à-dire $\lambda \in S$. C'est la première fois qu'on surmontait les difficultés liées aux petits dénominateurs. La démonstration de Siegel est cependant propre au problème considéré (c'est une estimation directe et très élégante des coefficients de $H_{f}$), et il appartiendra à Kolmogoroff, Arnold, Moser, Herman et beaucoup d'autres, de développer des techniques applicables à des problèmes plus généraux, en particulier aux tores invariants de la mécanique hamiltonienne.

Vers 1965, en suivant l'esprit de la démonstration de Siegel, Bruno ([Br]) établit que $G_{\lambda}$ est encore une classe de conjugaison de $G$ sous la condition arithmétique :

$$
\sum \frac {\mathrm{Log} q _ {n + 1}}{q _ {n}} <   + \infty ,\tag{B}
$$

moins restrictive que $(S)$. Il restait donc en suspens la situation des nombres $\lambda$ ne vérifiant ni $(B)$ ni $(Cr)$. Le résultat principal de cet article résout cette question :

THÉORÈME.— Soit $\lambda$ un nombre complexe de module 1 qui n'est pas racine de l'unité. Alors la condition (B) est nécessaire et suffisante pour que tout élément de $G_{\lambda}$ soit linéarisable.

Il faut à ce propos mentionner les travaux de Cherry ([Ch]). Vers 1965, sans connaître le résultat de Bruno, il conjecture correctement l'énoncé du théorème ci-dessus. La mort ne lui a malheureusement pas laissé le temps d'achever ses recherches, mais il semble, au vu des manuscrits qu'il a laissés, qu'il avait accompli de sérieux progrès vers la démonstration de ce résultat.

## 2. - Décrivons maintenant plus en détail le contenu de notre article.

Le premier chapitre est centré autour du théorème ci-dessus, et plus précisément autour d'une version quantitative de ce résultat (Th. I.2.6) qui estime, à une constante multiplicative universelle près, le plus petit rayon de convergence possible de l'application linéarisante $H_f \in \widehat{G}_1$ lorsque $f$ décrit $G_\lambda$. Il nous faut ici imposer à $f$ de vérifier une condition de normalisation, car l'application linéarisante de $R_t f R_t^{-1}$ est $R_t H_f R_t^{-1}$, et son rayon de convergence est $|t|$ fois celui de $H_f$: nous demanderons à $f$ d'être holomorphe et injective (univalente) sur le disque unité.

Le premier paragraphe (du premier chapitre) est consacré à des préparatifs arithmétiques autour du développement en fraction continue. Ecrivant $\lambda = \exp(2\pi i\alpha)$, avec $\alpha$ irrationnel, nous utilisons, pour des raisons de commodité dans des estimations ultérieures, une légère variante du développement en fraction continue usuel de $\alpha$. Ce développement nous permet de définir une fonction arithmétique

$$
\Phi : \mathbb {R} - \mathbb {Q} \rightarrow \mathbb {R} ^ {+} \cup \{+ \infty \}
$$

qui a les propriétés suivantes: elle est paire, Z-périodique, finie exactement aux nombres α vérifiant la condition (B), et vérifie l'équation fonctionnelle fondamentale

$$
\Phi (\alpha) = \mathrm{Log}   \alpha^ {- 1} + \alpha   \Phi (1 / \alpha)    ,    0 <   \alpha <   1 / 2.
$$

Nous procédons au second paragraphe à quelques réductions préliminaires à la démonstration du résultat principal, énoncé en I.2.6. Pour $\alpha \in \mathbb{R} - \mathbb{Q}$, notons $\lambda = \exp(2\pi i\alpha)$ et $S_{\alpha}$ la classe des fonctions $f$ injectives et holomorphes dans le disque unité, fixant 0 et y ayant pour dérivée $\lambda$. Le Théorème I.2.6 affirme qu'il existe des $f \in S_{\alpha}$ pour lesquels $H_{f}$ est divergente lorsque $\alpha$ ne vérifie pas la condition $(B)$, et que le plus petit rayon de convergence $R_{\alpha}$ de $H_{f}$, lorsque $f$ décrit $S_{\alpha}$ et $\alpha$ vérifie la condition $(B)$, satisfait à l'estimation :

$$
\left| \operatorname{Log} R _ {\alpha} ^ {- 1} - \Phi (\alpha) \right| \leq C,
$$

où C est une constante universelle. En fait, il suffit de démontrer l'estimation analogue (mais de contenu plus géométrique) obtenue en remplaçant le rayon de convergence de  $H_{f}$  par la distance  $d_{f}$  de l'origine à l'ensemble des points dont l'orbite positive par f sort du disque unité.

La démonstration du Théorème I.2.6 occupe les Paragraphes 3 à 5 du chapitre I. Le principe de la démonstration est d'analyser le comportement des rayons de convergence (ou plutôt des distances $d_{f}$) sous l'action de la transformation $\alpha \mapsto -1/\alpha$ de $PSL_{2}(\mathbb{Z})$ qui génère le développement en fraction continue (l'autre générateur

$\alpha \mapsto \alpha + 1$ de $PSL_{2}(\mathbb{Z})$ agit évidemment trivialement dans notre cadre). Il s'agit essentiellement de rendre quantitative et "inversible" une construction utilisée par Douady et Ghys ([Do]) pour démontrer que l'ensemble $S$ est invariant par $PSL_{2}(\mathbb{Z})$. La construction de Douady et Ghys est expliquée en I.2.9. Nous réussissons alors, pour $0 < \alpha < 1/2$ ou $\alpha > 2$, à associer à tout $f \in S_{\alpha}$ un difféomorphisme $g \in S_{-1/\alpha}$ tels que les quantités $\operatorname{Log} d_{f}^{-1}$ et $\operatorname{Log} d_{g}^{-1}$ soient reliées par une estimation semblable à l'équation fonctionnelle de la fonction arithmétique $\Phi$. Le cas le plus facile, traité au Paragraphe 3, est celui où $\alpha$ appartient à $(0, 1/2)$; il conduit à une nouvelle démonstration du théorème de Bruno, et donne une minoration du rayon de convergence de la conjugaison apparemment légèrement meilleure (lorsque $\Phi(\alpha)$ est fini mais grand) que la minoration obtenue par la démonstration de Bruno.

Le cas plus difficile où $\alpha$ est supérieur à 2 est traité au Paragraphe 4 ; la difficulté tourne autour du point suivant : lorsque $\alpha > 0$ est petit, $f$ peut posséder au voisinage de l'origine un autre point fixe, mais la dynamique du difféomorphisme $g \in S_{-1/\alpha}$ obtenu par la construction de Douady et Ghys ne contient pas d'information sur la dynamique de $f$ autour de cet autre point fixe. Lorsqu'on veut inversement faire cette construction pour $\alpha >> 2$, il est nécessaire de réintroduire cette information. En itérant cette construction et en passant à la limite on obtient au Paragraphe 5 la majoration désirée de $R_{\alpha}$ lorsque $\alpha$ satisfait ($B$), et des exemples de difféomorphismes non linéarisables à l'origine lorsque $\alpha$ ne satisfait pas ($B$).

Ces derniers exemples possèdent une suite d'orbites périodiques s'accumulant sur l'origine, qui sont étudiées au Paragraphe 6. On montre que la distance de ces orbites périodiques à l'origine est essentiellement la plus petite possible, compte tenu de leur période. Par ailleurs, on dispose dans la construction d'une grande flexibilité quant à la dynamique au voisinage de ces orbites périodiques (qui peuvent être attractives, répulsives, indifférentes rationnelles ou irrationnelles) ; une conséquence surprenante de cette flexibilité est le Théorème I.6.5 : si λ ne vérifie pas (B), il existe dans $G_{\lambda}$ un ensemble non dénombrable de classes de conjugaison dont aucune ne contient de fonction entière.

3. - Le second chapitre est consacré à la linéarisation dans la famille quadratique $P_{\lambda}(z) = \lambda z(1-z)$. La différence essentielle avec le premier chapitre, où l'attention est concentrée sur l'étude de la dynamique locale au voisinage du point fixe, est qu'on fait ici appel de façon décisive aux caractéristiques globales de la dynamique, en particulier à la présence d'un point critique.

Nous montrons dans le premier paragraphe que le polynôme  $P_{\lambda}$ , pour  $\lambda \in S^{1}$ , est linéarisable à l'origine si et seulement si  $\lambda$  satisfait à la condition (B), et que le rayon de convergence de l'application linéarisante  $H_{\lambda}$  de  $P_{\lambda}$  est "presque" le plus petit possible permis par le Théorème I.2.6, lorsque  $\lambda$  satisfait à la condition (B) ; l'énoncé précis est donné en II.1.8. La démonstration est une application assez élémentaire de la théorie des applications à allure polynômiale (de degré 2) de Douady et Hubbard ([D-H]).

Nous introduisons au Paragraphe 2 une autre approche de la linéarisation des polynômes quadratiques, consistant à étudier de façon détaillée l'application

linéarisante de $P_{\lambda}$ lorsque $|\lambda| < 1$, puis à laisser tendre non-tangentiellement $\lambda$ vers le cercle unité. Pour $|\lambda| < 1$, l'application linéarisante $H_{\lambda}$ possède en fait une unique singularité $U(\lambda)$ sur le bord de son disque de convergence, et $H_{\lambda}(U(\lambda))$ est égal au point critique $1/2$ de $P_{\lambda}$. La fonction $\lambda \mapsto U(\lambda)$ est holomorphe et bornée dans le disque unité, et son module est le rayon de convergence de $H_{\lambda}$. Le résultat principal du Paragraphe 2 est que le module $|U(\lambda)|$, lorsque $\lambda$ tend non-tangentiellement vers un point $\lambda_0 \in S^1$, admet pour limite le rayon de convergence de $H_{\lambda_0}$. On obtient ainsi, comme corollaire immédiat d'un célèbre théorème de Fatou, que le polynôme $P_{\lambda}$ est linéarisable pour presque tout $\lambda \in S^1$. Cette démonstration n'est valable que pour la famille quadratique (ou des familles très similaires), et ne donne pas d'information arithmétique sur l'ensemble des $\lambda$ pour lesquels $P_{\lambda}$ est linéarisable (condition (B)) mais elle est considérablement plus courte que les autres démonstrations de linéarisabilité. En combinant avec II.1.4, on retrouve facilement que $G_{\lambda}$ est une classe de conjugaison de $G$ pour presque tout $\lambda \in S^1$.

La fonction holomorphe U semble posséder des propriétés très intéressantes, que je n'ai malheureusement pas été capable de démontrer (ou d'infirmier). Ces propriétés sont évoquées au Paragraphe 3, où l'on trouvera aussi des formules reliées à la fonction U, et aux coefficients des applications linéarisantes  $H_{\lambda}$ .

Finalement, les deux appendices sont consacrées à des questions connexes ; en appliquant un résultat d'Il'yasenko ([Il]), on montre dans l'Appendice 1 que si une matrice $A \in GL_{n}(\mathbb{C})$ possède une valeur propre $\lambda$ de module 1 pour laquelle les sous-espaces propres et caractéristiques sont distincts, alors les germes de difféomorphismes holomorphes de $(\mathbb{C}^{n},0)$ de dérivée $A$ en 0 ne sont en général pas linéarisables. L'Appendice 2 montre que la condition $(B)$ est la limite naturelle de la méthode de démonstration de Siegel et Bruno.

## 4. - Remerciements.

La première version de cet article date de l'automne 1987, alors que j'étais chercheur au Centre de Mathématiques de l'Ecole Polytechnique. Mme Paule Truc en a assuré la frappe avec une compétence d'autant moins évidente qu'elle s'initiait alors aux délices de TeX. J'ai toujours beaucoup profité d'innombrables discussions avec Michel Herman, et ce travail doit beaucoup à son intérêt soutenu. Sans Ricardo Pérez-Marco, qui m'a signalé de nombreuses corrections et améliorations, et a compensé mon incompetence notoire devant un ordinateur, il n'est pas clair que cet article aurait vu le jour avant le troisième millénaire.

# Chapitre I LINÉARISATION DES FONCTIONS UNIVALENTES

## 1 - Préliminaires arithmétiques.

1.1 - Notations.

Soit x un nombre réel ; on note :

\- [x] sa partie entière,

\- $\{x\} = x - [x]$ sa partie fractionnaire,

\- $\| x\| = \operatorname {Min}(\{x\} ,1 - \{x\})$ la distance de $x$ au plus proche entier,

\- $\langle x\rangle$ l'entier le plus proche de $x$, avec la convention qu'on a $\langle x\rangle = [x]$ lorsque $\{x\} = 1 / 2$.

## 1.2 - Fractions continues (forme usuelle).

Notons $\tilde{A}$ l'application de $(0,1)$ dans $[0,1)$ définie par :

$$
\tilde {A} (x) = \{x ^ {- 1} \}.
$$

Soit $\alpha$ un nombre réel irrationnel ; posons $\tilde{a}_{0} = [\alpha]$, $\tilde{\alpha}_{0} = \{\alpha\}$ et définissons, pour $n \geq 1$:

$$
\tilde {a} _ {n} = [ \tilde {\alpha} _ {n - 1} ^ {- 1} ], \quad \tilde {\alpha} _ {n} = \tilde {A} (\tilde {\alpha} _ {n - 1}) = \tilde {A} ^ {n} (\tilde {\alpha} _ {0}).
$$

On a donc $\tilde{a}_0\in \mathbb{Z}$, $\tilde{a}_n\in \mathbb{N}^*$ pour $n\geq 1$, et $\tilde{\alpha}_n\in (0,1)$ pour $n\geq 0$ .

Définissons aussi, pour $n \geq -2$, des entiers $p_n, q_n$ par les relations :

$$
p _ {- 2} = q _ {- 1} = 0, \quad p _ {- 1} = q _ {- 2} = 1,
$$

$$
p _ {n} = \tilde {a} _ {n} p _ {n - 1} + p _ {n - 2}, q _ {n} = \tilde {a} _ {n} q _ {n - 1} + q _ {n - 2}, \quad \text { pour } \quad n \geq 0.
$$

On a alors, pour $n \geq 0$:

$$
\alpha = \frac {p _ {n} + p _ {n - 1} \tilde {\alpha} _ {n}}{q _ {n} + q _ {n - 1} \tilde {\alpha} _ {n}},
$$

et aussi $q_{n}p_{n - 1} - p_{n}q_{n - 1} = (-1)^{n}$ pour $n\geq -1$ .

Considérons d'autre part la suite $(\tilde{\beta}_n)_{n\geq -2}$ définie par :

$$
\tilde {\beta} _ {- 2} = \alpha , \tilde {\beta} _ {- 1} = 1, \tilde {\beta} _ {n} = \prod_ {i = 0} ^ {n} \tilde {\alpha} _ {i}, \text {pour} n \geq 0.
$$

On a alors, pour $n \geq 0$:

$$
\tilde {\beta} _ {n - 2} = \tilde {a} _ {n} \tilde {\beta} _ {n - 1} + \tilde {\beta} _ {n}, 0 <   \tilde {\beta} _ {n} <   \tilde {\beta} _ {n - 1},
$$

ce qui montre que $\tilde{a}_n$ est le quotient et $\tilde{\beta}_n$ le reste de la division euclidienne de $\tilde{\beta}_{n-2}$ par $\tilde{\beta}_{n-1}$; ceci fournit une définition alternative des $\tilde{\beta}_n$, des $\tilde{a}_n$ et des $\tilde{\alpha}_n = \tilde{\beta}_n\tilde{\beta}_{n-1}^{-1}$.

Pour $n \geq -2$, on a :

$$
\begin{array}{r} \tilde {\beta} _ {n} = (- 1) ^ {n} (q _ {n} \alpha - p _ {n}), \\ 1 = q _ {n + 1} \tilde {\beta} _ {n} + q _ {n} \tilde {\beta} _ {n + 1}, \end{array}
$$

ce qui fournit, pour $n \geq 0$, l'estimation importante :

$$
\frac {1}{q _ {n + 1} + q _ {n}} <   \tilde {\beta} _ {n} = \frac {1}{q _ {n + 1} + q _ {n} \tilde {\alpha} _ {n + 1}} <   \frac {1}{q _ {n + 1}}
$$

## 1.3 - Fractions continues (forme modifiée).

Notons A l'application de  $(0,1/2]$  dans  $[0,1/2]$  définie par :

$$
A (x) = \| x ^ {- 1} \|.
$$

Soit $\alpha$ un nombre réel irrationnel ; posons $a_0 = \langle \alpha \rangle$, $\alpha_0 = \| \alpha \|$ et définissons, pour $n \geq 1$:

$$
a _ {n} = \langle \alpha_ {n - 1} ^ {- 1} \rangle , \alpha_ {n} = A (\alpha_ {n - 1}) = A ^ {n} (\alpha_ {0}).
$$

On a donc $a_0 \in \mathbb{Z}$, $a_n \geq 2$ pour $n \geq 1$, et $\alpha_n \in (0,1/2)$ pour $n \geq 0$.

Posons aussi $\beta_{-2} = \alpha$, $\beta_{-1} = 1$ et $\beta_n = \prod_{i=0}^n \alpha_i$ pour $n \geq 0$. On a alors, pour $n \geq 0$:

$$
\beta_ {n - 2} = a _ {n} \beta_ {n - 1} + \epsilon_ {n} \beta_ {n},
$$

avec $\epsilon_{n} \in \{-1, +1\}$, $0 < \beta_{n} < \frac{1}{2}\beta_{n-1}$. On peut donc aussi définir les $\beta_{n}, a_{n}$ et $\alpha_{n} = \beta_{n}\beta_{n-1}^{-1}$ par l'algorithme de la division euclidienne.

## 1.4 - Relation entre les deux versions précédentes.

Soit $\alpha$ un nombre réel irrationnel. Conservons les notations des numéros précédents.

Posons $k(-1) = -1$ et définissons inductivement, pour $n \geq -1$:

$$
k (n + 1) = \left\{ \begin{array}{l l} k (n) + 1, & \text {si} \epsilon_ {n + 1} = 1; \\ k (n) + 2, & \text {si} \epsilon_ {n + 1} = - 1. \end{array} \right.
$$

L'application $k: \mathbb{N} \to \mathbb{N}$ est strictement croissante. On vérifie qu'on a, pour $n \geq -1$:

$$
\beta_ {n} = \tilde {\beta} _ {k (n)}
$$

Notons que la condition $\epsilon_{n+1} = -1$ équivaut à $\tilde{a}_{k(n)+2} = 1$. Dans ce cas on a

$$
\tilde {\beta} _ {k (n) + 1} = \beta_ {n} - \beta_ {n + 1}.
$$

## 1.5 - La fonction arithmétique $\Phi$ et la condition de Bruno.

Avec les notations précédentes, on définit une fonction $\Phi : \mathbb{R} - \mathbb{Q} \to \mathbb{R}^{+} \cup \{+\infty\}$ par la formule :

$$
\Phi (\alpha) = \sum_ {i \geq 0} \beta_ {i - 1} \mathrm{Log} \alpha_ {i} ^ {- 1}
$$

On dira qu'un nombre réel irrationnel $\alpha$ est un nombre de Bruno si $\Phi(\alpha) < +\infty$. La fonction $\Phi$ possède les propriétés suivantes :

Proposition.—

1. On a $\Phi(\alpha) = \Phi(\alpha + 1) = \Phi(-\alpha)$, pour $\alpha \in \mathbb{R} - \mathbb{Q}$.

2. Pour $\alpha \in (\mathbb{R} - \mathbb{Q}) \cap (0, 1/2)$, on $a$:

$$
\Phi (\alpha) = \mathrm{Log} \alpha^ {- 1} + \alpha \Phi (\alpha^ {- 1})
$$

Démonstration. Pour $\alpha \in \mathbb{R} - \mathbb{Q}$, les suites $(\alpha_{n})_{n \geq 0}$ et $(\beta_{n})_{n \geq -1}$ associées à $\alpha, \alpha + 1$ et $-\alpha$ sont les mêmes, d'où les premières relations. Si de plus $\alpha \in (0, 1/2)$, les suites $(\alpha_{n}')_{n \geq 0}$, $(\beta_{n}')_{n \geq -1}$ associées à $\alpha^{-1}$ sont données par $\alpha_{n}' = \alpha_{n+1}$ pour $n \geq 0$ et $\beta_{n}' = \alpha \beta_{n+1}$ pour $n \geq -1$, d'où l'équation reliant $\Phi(\alpha)$ et $\Phi(\alpha^{-1})$.

On désignera dans la suite par B l'ensemble des nombres de Bruno.

Remarque : On définit habituellement les nombres de Bruno par la propriété :

$$
\sum_ {i \geq 0} q _ {i} ^ {- 1} \mathrm{Log} q _ {i + 1} <   + \infty .
$$

Que les deux définitions soient équivalentes résulte de l'estimation plus précise suivante :

Il existe une constante $C > 0$ telle qu'on ait, pour tout $\alpha \in \mathbb{R} - \mathbb{Q}$, $n \geq 0$,

$$
\left| \sum_ {i = 0} ^ {n} \beta_ {i - 1} \mathrm{Log} \alpha_ {i} ^ {- 1} - \sum_ {i = 0} ^ {k (n)} q _ {i} ^ {- 1} \mathrm{Log} q _ {i + 1} \right| \leq C
$$

où l'entier $k(n)$ est défini en 1.4. Pour voir ceci, remarquons que d'après 1.1, on a :

$$
\begin{array}{c} q _ {i} ^ {- 1} = \tilde {\beta} _ {i - 1} + q _ {i - 1} q _ {i} ^ {- 1} \tilde {\beta} _ {i}, \\ 1 / 2 \leq q _ {i + 1} \tilde {\beta} _ {i} \leq 1, \end{array}
$$

d'où on tire

$$
\begin{array}{r l} \left| q _ {i} ^ {- 1} \mathrm{Log} q _ {i + 1} + \tilde {\beta} _ {i - 1} \mathrm{Log} \tilde {\beta} _ {i} \right| & \leq | q _ {i} ^ {- 1} - \tilde {\beta} _ {i - 1} | | \mathrm{Log} \tilde {\beta} _ {i} | + q _ {i} ^ {- 1} | \mathrm{Log} q _ {i + 1} \tilde {\beta} _ {i} | \\ & \leq (q _ {i} ^ {- 1}) \mathrm{Log} 2 + \left| \tilde {\beta} _ {i} \mathrm{Log} \tilde {\beta} _ {i} \right|. \end{array}
$$

Comme on a $q_{i+1} \geq q_i$, $q_{i+2} \geq 2q_i$, $\tilde{\beta}_{i+1} \leq \tilde{\beta}_i$, $\tilde{\beta}_{i+2} \leq \frac{1}{2}\tilde{\beta}_i$ pour $i \geq 0$, on en déduit :

$$
\left| \sum_ {i = 0} ^ {k} q _ {i} ^ {- 1} \mathrm{Log} q _ {i + 1} + \sum_ {i = 0} ^ {k} \tilde {\beta} _ {i - 1} \mathrm{Log} \tilde {\beta} _ {i} \right| \leq C _ {0}.\tag{1}
$$

Pour $j \geq 0$, $i = k(j)$, on a :

$$
\begin{array}{r l r} \tilde {\beta} _ {i - 1} \mathrm{Log} \tilde {\beta} _ {i} & = \beta_ {j - 1} \mathrm{Log} \beta_ {j}, \quad \text {si} \quad k (j - 1) = i - 1; \\ \tilde {\beta} _ {i - 2} \mathrm{Log} \tilde {\beta} _ {i - 1} + \tilde {\beta} _ {i - 1} \mathrm{Log} \tilde {\beta} _ {i} & = \beta_ {j - 1} \mathrm{Log} (\beta_ {j - 1} - \beta_ {j}) + (\beta_ {j - 1} - \beta_ {j}) \mathrm{Log} \beta_ {j}, \\ & \text {si} \quad k (j - 1) = i - 2. \end{array}
$$

En tenant compte de ce que $\beta_{j-1}-\beta_j>\frac{1}{2}\beta_{j-1}$, on obtient donc :

$$
\left| \sum_ {i = 0} ^ {n} \beta_ {i - 1} \mathrm{Log} \beta_ {i} - \sum_ {i = 0} ^ {k (n)} \tilde {\beta} _ {i - 1} \mathrm{Log} \tilde {\beta} _ {i} \right| \leq \mathrm{Log} 2 \sum_ {i = 0} ^ {n} \beta_ {i - 1} + 2 \left| \sum_ {i = 0} ^ {n} \beta_ {i} \mathrm{Log} \beta_ {i} \right|,\tag{2}
$$

le second membre étant majoré par une constante universelle puisqu'on a $\beta_{i} < \frac{1}{2}\beta_{i-1}$ pour $i\geq0$.

Finalement, on a :

$$
\left| \sum_ {i = 0} ^ {n} \beta_ {i - 1} \mathrm{Log} \beta_ {i} - \sum_ {i = 0} ^ {n} \beta_ {i - 1} \mathrm{Log} \alpha_ {i} \right| = \left| \sum_ {i = 0} ^ {n} \beta_ {i - 1} \mathrm{Log} \beta_ {i - 1} \right| \leq C.\tag{3}
$$

En réunissant (1), (2) et (3), on obtient l'estimation annoncée.

## 1.6 - Un lemme technique.

Ce numéro contient un lemme arithmétique qui sera utilisé aux paragraphes 5 et 6; sa lecture peut être repoussée jusqu'à ce moment.

Soient $\alpha$ un nombre réel irrationnel, $B$ une constante strictement positive (la valeur de $B$ sera spécifiée en 5.4.2).

Avec les notations précédentes, posons :

$$
B _ {k, k + 1} = 0 \quad , \quad k \geq 0,
$$

$$
B _ {k, i} = \alpha_ {i} B _ {k, i + 1} + \mathrm{Log} \alpha_ {i} ^ {- 1} - B \quad , \quad 0 \leq i \leq k.
$$

On a donc, pour $0 \leq i \leq k$ :

$$
B _ {k, i} = \beta_ {i - 1} ^ {- 1} \sum_ {j = i} ^ {k} \beta_ {j - 1} (\mathrm{Log} \alpha_ {j} ^ {- 1} - B)  .
$$

Notons $\mathcal{I}(\alpha) = \mathcal{I}$ (resp. $\mathcal{J}(\alpha) = \mathcal{J}$) l'ensemble des entiers $k \geq 0$ tels qu'on ait $B_{k,i} > 0$ pour tout $0 \leq i \leq k$ (resp. $B_{k,i} > B\alpha_{i-1}^{-1}$ pour $0 < i \leq k$).

Lemme.—

1. Pour tout $k \geq 0$, on $a$:

$$
B _ {k, 0} <   \sum_ {j = 0} ^ {k} \beta_ {j - 1} \mathrm{Log} \alpha_ {j} ^ {- 1} <   B _ {k, 0} + 2 B.
$$

2. Si $\mathcal{I}(\alpha)$ est vide, on $a$:

$$
\Phi (\alpha) \leq 4 B.
$$

3. Si $\mathcal{I}(\alpha)$ est fini non vide, et $k$ est son plus grand élément, on a :

$$
\Phi (\alpha) \leq 4 B + B _ {k, 0}.
$$

4. Si $\alpha \notin \mathcal{B}$, $\mathcal{J}(\alpha)$ est infini.

Démonstration. Comme on a $\beta_{j} < \frac{1}{2}\beta_{j-1}$ pour $j \geq 0$, la formule pour $B_{k,i}$ qui précède le lemme montre qu'on a :

$$
0 > B _ {k, i} - \beta_ {i - 1} ^ {- 1} \sum_ {j = i} ^ {k} \beta_ {j - 1} \mathrm{Log} \alpha_ {j} ^ {- 1} > - 2 B\tag{4}
$$

pour $0 \leq i \leq k$, d'où la première partie du lemme.

Supposons que $\mathcal{I}(\alpha)$ soit vide. Pour tout $k \geq 0$ il existe alors des entiers $-1 = k_0 < k_1 < \ldots < k_r = k$ tels qu'on ait :

$$
B _ {k _ {l}, k _ {l - 1} + 1} \leq 0, \quad 1 \leq l \leq r.
$$

D'après (4), on a donc :

$$
\sum_ {j = k _ {l - 1} + 1} ^ {k _ {l}} \beta_ {j - 1} \mathrm{Log} \alpha_ {j} ^ {- 1} <   2 B \beta_ {k _ {l - 1}}, \quad 1 \leq l \leq r
$$

d'où $\sum_{j=0}^{k}\beta_{j-1}\mathrm{Log}\alpha_j^{-1}\leq 4B$ .

Comme k est arbitraire, cela prouve la seconde partie du lemme.

Supposons que $\mathcal{I}$ soit fini et non vide, de plus grand élément $k$. Pour tout $k' > k$, il existe un entier $i$, avec $k < i \leq k'$, tel que $B_{k',i} \leq 0$; en effet, dans le cas contraire, on a en particulier $B_{k',k+1} > 0$, d'où $B_{k',j} = B_{k,j} + \beta_{j-1}\beta_k^{-1}B_{k',k+1} > B_{k,j} > 0$ pour $0 \leq j \leq k$, et $k' \in \mathcal{I}$. On peut donc trouver des entiers $k = k_0 < k_1 < \ldots < k_r = k'$ tels que $B_{k_\ell, k_\ell-1+1} \leq 0$ pour $1 \leq \ell \leq r$. Comme précédemment, on en déduit :

$$
\sum_ {j = k + 1} ^ {k ^ {\prime}} \beta_ {j - 1} \mathrm{Log} \alpha_ {j} ^ {- 1} <   4 B \beta_ {k}.
$$

On obtient :

$$
\begin{array}{l} \Phi (\alpha) \leq \sum_ {j = 0} ^ {k} \beta_ {j - 1} \mathrm{Log} \alpha_ {j} ^ {- 1} + 4 B \beta_ {k} \\ \quad \leq B _ {k, 0} + 4 B, \end{array}
$$

d'après la première partie du lemme, et $\beta_{k} < \frac{1}{2}$.

Supposons enfin que $\mathcal{J}(\alpha)$ soit fini, et notons $k$ son plus grand élément (en prenant $k = 0$ si $\mathcal{J}(\alpha)$ est vide).

Pour tout $k_0 > k$, construisons des entiers $k_0 > k_1 > \ldots > k_r$ tels que :

(i) $k_{r - 1} > k\geq k_r$

(ii) pour $0 < l \leq r$, on a $B_{k_{l-1}, k_l+1} \leq B \alpha_{k_l}^{-1}$.

D'après la formule pour $B_{k,i}$, on a :

$$
\sum_ {j = k _ {l} + 1} ^ {k _ {l - 1}} \beta_ {j - 1} (\mathrm{Log} \alpha_ {j} ^ {- 1} - B) \leq B \beta_ {k _ {l} - 1},
$$

On en déduit :

$$
\sum_ {j = k + 1} ^ {k _ {0}} \beta_ {j - 1} \mathrm{Log} \alpha_ {j} ^ {- 1} \leq 2 B \sum_ {j \geq 0} \beta_ {j - 1},
$$

ce qui implique $\alpha\in\mathcal{B}$ puisque $k_{0}$ est arbitrairement grand.

## 2. Linéarisation des fonctions univalentes : résultats et réductions.

## 2.1 - Linéarisation formelle.

Soit $f$ un germe de difféomorphisme holomorphe de $(\mathbb{C},0)$. Posons $Df(0)=\lambda$ et supposons que $\lambda$ soit de module 1, mais ne soit pas racine de l'unité.

Il existe alors une unique série formelle $H_{f}$ qui vérifie formellement :

$$
D H _ {f} (0) = 1,
$$

$$
H _ {f} (\lambda z) = f (H _ {f} (z)).
$$

Nous appelons $H_f$ la linéarisante (formelle) de $f$, et noterons $R(f)$ son rayon de convergence.

Tant qu'il s'agit de déterminer si $R(f)$ est nul ou non, on peut travailler avec des germes de difféomorphismes holomorphes. Mais si l'on veut obtenir des estimations quantitatives pour $R(f)$, une condition de normalisation s'impose. En effet, pour $t > 0$, le germe $f_t: z \to t^{-1}f(tz)$ a même dérivée que $f$ en 0, sa linéarisante est la série: $z \to t^{-1}H_f(tz)$, et on a donc $R(f_t) = t^{-1}R(f)$.

Nous choisirons une condition de normalisation géométrique, en imposant à $f$ d'être holomorphe et injective sur le disque unité $\mathbb{D} = \{z, |z| < 1\}$. Nos résultats seront donc énoncés pour cet espace de fonctions univalentes ; bien entendu, on en déduit si on le souhaite les résultats analogues pour d'autres conditions de normalisation, via des estimations de “distorsion” ou “à la Bieberbach”.

## 2.2 - Fonctions univalentes.

Nous noterons $S$ l'espace des applications $f$, holomorphes et injectives dans $\mathbb{D}$, qui vérifient $f(0) = 0$ et $|Df(0)| = 1$. On munit $S$ de la topologie de la convergence uniforme sur les parties compactes de $\mathbb{D}$, qui en fait un espace compact.

Pour $\lambda\in\mathbb{S}^{1}$, on notera $S_{\lambda}$ la partie fermée de $S$ formée des $f$ tels que $Df(0)=\lambda$.

Il sera en fait plus pratique de travailler dans le revêtement universel $\mathbb{H} = \{z, \operatorname{Im} z > 0\}$ de $\mathbb{D}^*$.

Nous noterons $E: z \longmapsto \exp(2\pi iz)$ l'application revêtante et $T: z \longmapsto z + 1$ la translation. Pour $\alpha \in \mathbb{R}$, nous désignerons par $\widehat{S}_{\alpha}$ l'ensemble des applications $F$, holomorphes et injectives dans $\mathbb{H}$, qui vérifient :

$$
F T = T F,
$$

$$
\lim _ {\operatorname{Im} z \rightarrow + \infty} (F (z) - z) = \alpha .
$$

Munissons l'ensemble $\widehat{S} = \bigcup_{\alpha \in \mathbb{R}} \widehat{S}_{\alpha}$ de la topologie de la convergence uniforme sur les compacts de $\mathbb{H}$. L'espace $\widehat{S}$ est alors contractile (conjuguer par des translations imaginaires); en associant à $F \in \widehat{S}$ l'unique application $f$ holomorphe dans $\mathbb{D}^*$ qui

vérifie $E \circ F = f \circ E$, on définit une application $\Pi$ de $\widehat{S}$ dans $S$ qui fait de $\widehat{S}$ le revêtement universel de $S$.

Pour $\alpha \in \mathbb{R}$, on a :

$$
\Pi^ {- 1} (S _ {E (\alpha)}) = \cup_ {n \in \mathbf {Z}} \widehat {S} _ {\alpha + n}
$$

## 2.3 - Capacité conforme.

Soient U un ouvert simplement connexe de C, distinct de C, et  $x_{0}$  un point de U. Considérons une représentation conforme k de D sur U qui envoie 0 sur  $x_{0}$ .

Définition.— On appelle capacité conforme de U par rapport à  $x_{0}$ , et on note  $C(U, x_{0})$ , le nombre  $|Dk(0)|$  (qui ne dépend pas du choix de k).

De façon équivalente, la capacité conforme $C(U, x_0)$ est l'unique réel $r \in \mathbb{R}_+^*$ pour lequel il existe une représentation conforme $h$ du disque $\mathbb{D}_r = \{z, |z| < r\}$ sur $U$ qui vérifie $h(0) = x_0$ et $Dh(0) = 1$.

Si $V$ est une partie ouverte et simplement connexe de $U$ qui contient $x_0$, on a :

$$
C (V, x _ {0}) \leq C (U, x _ {0}),
$$

avec égalité si et seulement si U = V. Cela résulte du lemme de Schwarz, appliqué à une représentation conforme de  $k^{-1}(V) \subset \mathbb{D}$ .

Il n'est en général pas facile de déterminer exactement la capacité conforme $C(U, x_{0})$. Une première approximation, suffisante pour nous dans la suite, est donnée par la distance $d$ de $x_{0}$ au complémentaire de $U$ dans $\mathbb{C}$. On a en effet, par le lemme de Schwarz :

$$
d \leq C (U, x _ {0}),
$$

et d'autre part, par le théorème de Koebé :

$$
4 d \geq C (U, x _ {0}).
$$

## 2.4 - Disques de Siegel des fonctions univalentes.

Soit $f\in S$

Nous noterons $K_{f}$ l'ensemble des points $z \in \mathbb{D}$ tels que $f^{n}(z) \in \mathbb{D}$ pour tout $n > 0$.

Nous dirons que $f$ admet un disque de Siegel en 0 si l'intérieur de $K_f$ contient 0. Nous noterons alors $U_f$ la composante connexe de l'intérieur de $K_f$ qui contient 0, et l'appellerons disque de Siegel de $f$ (en 0). On a bien sûr :

$$
f (K _ {f}) \subset K _ {f}, f (U _ {f}) \subset U _ {f}.
$$

Par le principe du maximum, l'ouvert $U_{f}$ est simplement connexe. Posons

$$
C (f) = C \left(U _ {f}, 0\right) \leq 1.
$$

Soit alors $\widetilde{H}_f: \mathbb{D}_{C(f)} \to U_f$ la représentation conforme de $U_f$ qui vérifie $\widetilde{H}_f(0) = 0$, $D\widetilde{H}_f(0) = 1$ (cf.2.3). L'application $\widetilde{H}_f^{-1} \circ f \circ \widetilde{H}_f$ est holomorphe sur $\mathbb{D}_{C(f)}$ et envoie ce disque dans lui-même; comme sa dérivée en 0 est égale à celle de $f$, on a, par le lemme de Schwarz:

$$
\widetilde {H} _ {f} ^ {- 1} \circ f \circ \widetilde {H} _ {f} (z) = D f (0) z, \quad z \in \mathbb {D} _ {C (f)}.
$$

Lorsque $Df(0)$ n'est pas racine de l'unité, ceci montre que l'application $\widetilde{H}_f$ admet comme développement en série entière en 0 exactement la série formelle $H_f$ définie en 2.1. On a par conséquent, lorsque $f$ admet un disque de Siegel en 0 :

$$
R (f) \geq C (f) > 0.
$$

Lorsque $f$ n'admet pas de disque de Siegel en 0, on posera $C(f) = 0$, et on aura également $R(f) = 0$.

## 2.5 - Propriétés des applications C et R.

Proposition 1.— L'application C est semi-continue supérieurement sur S.

Démonstration. Soit $(f_n)_{n\geq 0}$ une suite dans $S$, convergeant vers une limite $f$. Posons

$$
C = \operatorname * {L i m s u p} _ {n \to + \infty} C (f _ {n}),
$$

et montrons que $C(f) \geq C$. C'est trivial si $C = 0$, supposons donc que $C$ est strictement positif. Quitte à extraire une sous-suite de la suite $(f_n)_{n \geq 0}$, on peut supposer que la suite $C(f_n)$ tend vers $C$, et que la suite $(\widetilde{H}_{f_n})_{n \geq 0}$ converge uniformément sur tout compact contenu dans le disque $\mathbb{D}_C$. La limite $\widetilde{H}$ est alors holomorphe et injective dans $\mathbb{D}_C$, et y vérifie :

$$
H (D f (0) z) = f (H (z)),
$$

par passage à la limite dans les relations correspondantes pour $f_{n}$. L'ouvert $H(\mathbb{D}_{C})$ est donc connexe et contenu dans $U_{f}$, et on conclut qu'on a $C \leq C(f)$.

Soient $\lambda\in\mathbb{S}^{1}$, distinct des racines de l'unité, et $f\in S_{\lambda}$; supposons que $f$ admette un disque de Siegel en 0; on a vu au paragraphe précédent qu'on a alors $C(f)\leq R(f)$.

Proposition 2.— On a $C(f) = R(f)$ lorsqu'une au moins des deux conditions suivantes est vérifiée :

(i) l'ouvert $U_{f}$ est relativement compact dans $\mathbb{D}$;

(ii) tout point de $\mathbb{S}^1$ est singularité de $f$.

Démonstration. Supposons qu'on ait $C(f) < R(f)$, et notons $\mathcal{C}$ l'image par $\widetilde{H}_f$ du cercle $\{|z| = C(f)\}$. C'est le bord de $U_f$ dans $\mathbb{C}$. Distinguons plusieurs cas :

1) $\mathcal{C} \subset \mathbb{D}$. Ceci est impossible: pour $\epsilon > 0$ suffisamment petit, l'ouvert connexe $\widetilde{H}_f(\mathbb{D}_{C(f)+\epsilon})$ contiendrait $\overline{U}_f$ et serait contenu dans $K_f$, en contradiction avec la définition de $U_f$.

2) $\mathcal{C} = \mathbb{S}^1$. On a alors $U_{f} = \mathbb{D}$, $\widetilde{H}_f(z) \equiv z$, d'où $f(z) \equiv \lambda z$.

3) $\mathcal{C} \subset \overline{\mathbb{D}}, \mathcal{C} \neq \mathbb{S}^1, \mathcal{C} \cap \mathbb{S}^1 \neq \emptyset$.

L'ouvert $U_f$ n'est alors pas relativement compact dans $\mathbb{D}$; montrons qu'il existe des points de $\mathbb{S}^1$ au voisinage desquels $f$ est holomorphe. Comme $\lambda$ n'est pas racine de l'unité, il existe un point $z_0$ de module $C(f)$ tel que $\widetilde{H}_f(z_0) = y_0$ appartienne à $\mathcal{C} \cap \mathbb{S}^1$, mais $\widetilde{H}_f(\lambda z_0)$ appartienne à $\mathcal{C} \cap \mathbb{D}$. Si $z_0$ n'est pas point critique de $\widetilde{H}_f$, la relation $\widetilde{f}(z) = \widetilde{H}_f(\lambda \widetilde{H}_f^{-1}(z))$ permet de prolonger $f$ en une fonction holomorphe au voisinage de $y_0$; si $z_0$ est point critique de $\widetilde{H}_f$, la même formule permet de prolonger $f$ en une fonction multivaluée au voisinage de $z_0$, admettant en $z_0$ une singularité isolée. Dans les deux cas, la condition (ii) de la proposition ne peut être vérifiée.

Corollaire.— Soit $\lambda\in\mathbb{S}^{1}$, distinct des racines de l'unité. On a :

$$
\inf _ {f \in S _ {\lambda}} C (f) = \inf _ {f \in S _ {\lambda}} R (f).
$$

Démonstration. S'il existe $f_0 \in S_\lambda$ tel que $R(f_0) = 0$, on a aussi $C(f_0) = 0$ et les deux termes sont nuls.

Supposons donc que les fonctions C et R soient strictement positives sur  $S_{\lambda}$ .

Considérons la partie $S_{\lambda}^{0}$ de $S_{\lambda}$ formée des $f \in S_{\lambda}$ qui vérifient la condition (ii) de la Proposition 2. On a donc $C(f) = R(f)$ pour $f \in S_{\lambda}^{0}$; d'autre part $S_{\lambda}^{0}$ est une partie dense de $S_{\lambda}$, d'où l'on tire, d'après la proposition 1 :

$$
\inf _ {f \in S _ {\lambda}} C (f) = \inf _ {f \in S _ {\lambda} ^ {0}} C (f).
$$

On a donc

$$
\inf _ {f \in S _ {\lambda}} R (f) \leq \inf _ {f \in S _ {\lambda} ^ {0}} R (f) = \inf _ {f \in S _ {\lambda}} C (f).
$$

L'autre inégalité résulte de ce qu'on a $R(f) \geq C(f)$ pour $f \in S_{\lambda}$.

## 2.6 - Enoncé des résultats.

Soit $\alpha \in \mathbb{R} - \mathbb{Q}$; posons $\lambda = E(\alpha)$ et:

$$
R (\alpha) = \inf _ {f \in S _ {\lambda}} R (f) = \inf _ {f \in S _ {\lambda}} C (f)
$$

Dans le théorème ci-dessous, la fonction $\Phi$ est la fonction arithmétique définie en 1.5.

## THÉORÈME.—

1. Si $\Phi(\alpha) = +\infty$, il existe un germe $f \in S_{\lambda}$ non linéarisable à l'origine.

2. Si $\Phi (\alpha) < +\infty$, alors on a $R(\alpha) > 0$ et:

$$
| \mathrm{Log} R (\alpha) + \Phi (\alpha) | \leq C,
$$

où C est une constante universelle (ne dépendant pas de α).

## 2.7 - Remarques.

1 - La démonstration de Bruno ([Br]) donne une estimation de la forme :

$$
\mathrm{Log} R (\alpha) \geq - C ^ {\prime} \Phi (\alpha) - C ^ {\prime \prime},
$$

où l'on peut prendre $C' = 2$ ([He]). Le théorème précédent montre qu'on peut en fait prendre $C' = 1$ (et que ce choix est optimal). Il serait intéressant de savoir si l'on peut obtenir $C' = 1$ par les techniques de Bruno. En effet, le principe de la démonstration de Bruno (et de celle de Siegel ([Si])) est d'estimer la taille des coefficients obtenus lorsqu'on remplace les relations de récurrence définissant les coefficients des applications linéarisantes $H_f$ par les mêmes relations pourvues de valeurs absolues. Si l'on peut obtenir ainsi $C' = 1$, cela signifie que le passage aux valeurs absolues n'affecte le rayon de convergence des séries considérées que par un facteur multiplicatif universellement borné.

2 - La constante C est effectivement calculable. La démonstration du théorème donnera

$$
- 1 5. 2 4 <   \mathrm{Log} R (\alpha) + \Phi (\alpha) <   1 3 9. 7 5
$$

mais ces bornes sont certainement mauvaises par rapport aux bornes réelles de la fonction bornée  $\operatorname{Log}R(\alpha) + \Phi(\alpha)$ .

3 - Lorsque $\Phi(\alpha) = +\infty$, il y a beaucoup de latitude dans la construction d'exemples de $f \in S_{\lambda}$ qui ne sont pas linéarisables en 0 ; quelques propriétés réalisables par de tels exemples sont étudiées au Paragraphe 6. Ces exemples possèdent une suite d'orbites périodiques accumulant l'origine. Plus récemment, R. Pérez-Marco a montré ([PM]) que cette propriété est inévitable pour des germes non linéarisables si $\alpha$ vérifie :

$$
\sum_ {n \geq 0} q _ {n} ^ {- 1} \mathrm{LogLog} q _ {n + 1} <   + \infty .
$$

Lorsqu'au contraire cette série diverge, il a construit des germes non linéarisables sans autre point périodique que l'origine.

4 - Comme on le verra au chapitre II, le théorème implique des estimations assez précises sur le rayon de convergence des linéarisantes de polynômes quadratiques. Posons $P_{\alpha}(z) = E(\alpha)(z - z^2)$ pour $\alpha \in \mathbb{R}$. On montrera que :

\- $P_{\alpha}$ n'est pas linéarisable en 0 lorsque $\Phi(\alpha)=+\infty$.

\- Lorsque $\Phi (\alpha) < +\infty$ , on a, pour tout $\varepsilon >0$ :

$$
\mathrm{Log} R (P _ {\alpha}) <   - (1 - \varepsilon) \Phi (\alpha) + C ^ {\prime} (\varepsilon),
$$

pour une constante $C'$ ne dépendant que de $\varepsilon$.

## 2.8 - Une réduction.

Soient $\alpha \in \mathbb{R} - \mathbb{Q}$, $F \in \hat{S}_{\alpha}$ et $f = \Pi(F) \in S_{E(\alpha)}$. Posons

$$
\begin{array}{r l} & K _ {F} = E ^ {- 1} (K _ {f}) = \{z \in \mathbb {H}, F ^ {n} (z) \in \mathbb {H} \text {pour} n \geq 0 \}; \\ & d _ {F} = \underset {z \in \mathbb {C} - K _ {F}} {\mathrm{Sup}} \Im z \in \mathbb {R} _ {+} \cup \{+ \infty \}, \end{array}
$$

où $\Im z$ (resp. $\Re z$) désigne la partie imaginaire (resp. réelle) d'un nombre complexe $z$. On a alors :

$$
d _ {F} = - \frac {1}{2 \pi} \mathrm{Log} d (0, \mathbb {C} - K _ {f});
$$

compte tenu des estimations données en 2.3, cela donne :

$$
\exp (- 2 \pi d _ {F}) \leq C (f) \leq 4 \exp (- 2 \pi d _ {F}).
$$

Pour démontrer le théorème, il suffit donc de prouver que :

\- si $\Phi (\alpha) = +\infty$ , il existe $F\in \hat{S}_{\alpha}$ tel que $d_F = +\infty$

\- si $\Phi (\alpha) < +\infty$ , on a :

$$
\left| \operatorname * {S u p} _ {F \in \hat {S} _ {\alpha}} d _ {F} - \frac {1}{2 \pi} \Phi (\alpha) \right| \leq C _ {0},
$$

pour une constante universelle $C_0$.

## 2.9 - Principe de la démonstration du théorème.

La démonstration du théorème est contenue dans les deux prochains paragraphes ; celui-ci n'en fait pas partie.

Cependant, nous avons cru bon d'essayer d'expliquer, avant de plonger dans des estimations techniques, où nous allions, en décrivant grossièrement le schéma de la démonstration et les constructions qui seront rendues précises dans les prochains paragraphes.

Soit $\alpha\in\mathbb{R}-\mathbb{Q}$. On a défini en 1.3 une suite $(\alpha_{n})_{n\geq0}$ d'éléments de $(0,1/2)$, et des entiers $a_{n}(n\geq1)$ au moins égaux à 2 de la façon suivante :

$$
\alpha_ {0} = \left\| \alpha \right\|
$$

$$
\alpha_ {n - 1} ^ {- 1} = a _ {n} + \epsilon_ {n} \alpha_ {n}, \quad \epsilon_ {n} \in \{- 1, + 1 \}, \quad n \geq 1.
$$

L'ingrédient fondamental de la démonstration du théorème est un procédé "naturel" (mais non canonique, loin de là) qui "relève" dans $\widehat{S}$ la formule reliant $\alpha_{n-1}$ et $\alpha_n$ ci-dessus, en faisant passer de $\widehat{S}_{\alpha_{n-1}}$ dans $\widehat{S}_{\alpha_n}$ et vice-versa.

Cette idée a été exploitée, de façon qualitative, par Douady ([Do]) et Ghys, pour montrer l'invariance de S (cf. introduction) par l'action de  $SL(2,\mathbb{Z})$ . Expliquons leur construction dans le cas le plus simple à décrire.

Soit $\beta \in (0,1/2) \cap \mathbb{R} - \mathbb{Q}$, $\lambda = E(\beta)$ et $f(z) = \lambda z + \mathcal{O}(z^2)$ un germe de difféomorphisme holomorphe de $(\mathbb{C}, 0)$. Considérons un domaine $U$ délimité par

\- une courbe analytique $\ell$, issue de 0, d'extrémité $z_0$;

\- son image $f(\ell)$;

\- une courbe $\ell'$ joignant $z_0$ à $f(z_0)$.

Nous choisissons $\ell$ et $\ell'$ de sorte que les courbes $\ell$, $\ell'$, $f(\ell)$ ne s'intersectent qu'en leurs extrémités (formant ainsi un "triangle"), et que l'ouverture de $U$ en 0 soit $2\pi\beta$ (cf. Figure 1).

![](images/page_25_image_7.jpg)

Figure 1

En recollant $\ell$ et $f(\ell)$ suivant $f$, on obtient une surface de Riemann $V$ biholomorphe à $\mathbb{D}^*$. Notons $\overline{V}$ la surface de Riemann obtenue en rajoutant un point $\mathcal{O}$ à $V$ de sorte que $\overline{V}$ soit biholomorphe à $\mathbb{D}$ (le point $\mathcal{O}$ étant alors envoyé sur 0). Considérons l'application $\tilde{g}$, définie dans un voisinage de 0 dans $U$, de premier retour dans $U$ (il y a en général ambiguïté le long d'une courbe de la forme $f^{-n}(\ell)$, $n \geq 2$). L'application $\tilde{g}$ induit sur $\overline{V}$ une application holomorphe $g$ définie dans un voisinage de $\mathcal{O}$, fixant $\mathcal{O}$ et dont la valeur propre en $\mathcal{O}$ est $E(-1/\beta)$.

A toute orbite de $f$ voisine de 0 correspond une orbite de $g$ voisine de $\mathcal{O}$ (l'image par l'injection : $U \to \overline{V}$ de la trace sur $U$ de l'orbite de $f$). En particulier $g$ admet un disque de Siegel en $\mathcal{O}$ si et seulement si $f$ en admet un en 0. Cela montre que $\beta \in S$ si $-1/\beta \in S$.

Reprenons cette construction, d'un point de vue plus analytique, dans $\mathbb{H}$. Soit $F$ une application holomorphe dans un demi-plan $\mathbb{H}_t = \{z, \Im z > t\}$, et y vérifiant :

$$
F \circ T = T \circ F,
$$

$$
f \circ E = E \circ F,
$$

$$
\lim _ {\Im z \rightarrow + \infty} (F (z) - z) = \beta .
$$

Notons $\widehat{U}$ l'une des composantes connexes de $E^{-1}(U)$; son bord est constitué de trois courbes $\widehat{\ell}$, $F(\widehat{\ell})$ et $\widehat{\ell}'$.

L'uniformisation de $V$ par $\mathbb{D}^{*}$ se traduit alors par l'existence d'une fonction $K$ holomorphe et injective dans $\widehat{U}$, continue sur l'adhérence de $\widehat{U}$, qui vérifie :

$$
\Im K (z) = 0, \quad z \in \widehat {\ell},
$$

$$
K (F (z)) = K (z) + 1, \quad z \in \widehat {\ell}.
$$

La dernière formule permet de prolonger K à des domaines qui seront décrits au prochain paragraphe.

L'application de premier retour $\widetilde{g}$ dans $U$ se relève dans $\widehat{U}$ en la composition d'un certain nombres d'itérations de $F$ (pour aboutir dans $T(\widehat{U})$) et de la translation $T^{-1}$ (pour revenir dans $\widehat{U}$). Après uniformisation, c'est à dire conjugaison par $K$, les itérés de $F$ deviennent des translations entières, tandis que la translation $T^{-1}$ devient une application holomorphe $G$, définie dans un demi-plan $\mathbb{H}_s$, pour $s$ assez grand, et vérifiant :

$$
\begin{array}{c} G \circ T = T \circ G, \\ \underset {\Im z \to + \infty} {\text {Lim}} (G (z) - z) = - 1 / \beta ; \end{array}
$$

(en effet, l'application $K$ est de la forme $K(z) = \beta^{-1}z + c + o(1)$ lorsque $\Im z$ est grand).

Dans cette présentation, nous voyons que l'hypothèse $\beta\in(0,1/2)$ n'est plus nécessaire, l'hypothèse $\beta>0$ nous suffit.

Ceci étant, quel est le schéma de la démonstration du théorème ?

Pour obtenir une minoration de $R(\alpha)$ lorsque $\alpha$ est un nombre de Bruno, nous raisonnerons par l'absurde en supposant qu'il existe $F_{0} \in \widehat{S}_{\alpha_{0}}$ tel que $d_{F_{0}}$ ne satisfasse pas à la majoration requise. Nous construirons alors successivement par la méthode précédente $F_{1} \in \widehat{S}_{\alpha_{1}}, ..., F_{k} \in \widehat{S}_{\alpha_{k}}$ avec des minorations pour $d_{F_{k}}$ qui permettent d'aboutir à une contradiction après un nombre fini d'étapes.

Nous aurons donc à réaliser la construction précédente pour $\beta = \alpha_0$, $\beta = \alpha_1, \ldots, \beta = \alpha_{k-1}$ etc..., dans tous les cas avec $\beta \in (0, 1/2)$. Lorsque $\beta = \alpha_{i-1}$ n'est pas trop petit, il n'y a essentiellement pas perte d'information en passant de $F_{i-1}$ à $F_i$: toutes les orbites de $F_{i-1}$ de grandes parties imaginaires (c'est à dire proches de 0 dans $\mathbb{D}$) correspondent à des orbites de $F_i$. Par contre, lorsque $\beta = \alpha_{i-1}$ est petit, $f_{i-1} = \Pi(F_{i-1})$ possède en général dans $\mathbb{D}$ un autre point fixe $p$ proche de 0, dont la distance à 0 est de l'ordre de $\beta$. En première approximation, un voisinage de 0 est divisé en trois parties : un voisinage $V_p$ de $p$ formé de points qui "tournent" autour de $p$, un voisinage $V_0$ de 0 formé de points qui "tournent" autour de 0, et le complémentaire de $V_0 \cup V_p$ formé de points qui "passent" entre 0 et $p$. Le passage de $F_{i-1}$ à $F_i$ ne peut rendre compte que des orbites de $V_0$, d'où une sérieuse perte d'information.

Pour obtenir au contraire des exemples avec une bonne majoration de $R(f)$, nous partirons de $\widehat{S}_{\alpha_k}$, avec $k$ grand, en prenant pour $F_k$ n'importe quel élément de $\widehat{S}_{\alpha_k}$ (par exemple la translation par $\alpha_k$). Nous en déduisons trivialement un élément de $\widehat{S}_{\alpha_{k-1}^{-1}}$ (puisque $\alpha_{k-1}^{-1} = \epsilon_k \alpha_k + a_k$). Il s'agit maintenant de remonter à $F_{k-1} \in \widehat{S}_{\alpha_{k-1}}$ puis après $k$ étapes jusqu'à $\widehat{S}_{\alpha_0}$ pour obtenir un exemple $F_0$ ayant les propriétés désirées. On pourrait penser qu'il suffit d'appliquer successivement la construction décrite plus haut avec $\beta = \alpha_{k-1}^{-1}$, $\beta = \alpha_{k-2}^{-1}, \ldots, \beta = \alpha_0^{-1}$ (c'est-à-dire qu'on a toujours $\beta > 2$). Cette construction est en effet suffisante tant que $\beta$ n'est pas trop grand. Mais lorsque $\beta = \alpha_{i-1}^{-1}$ est grand, il nous faudra modifier cette construction de manière à réinjecter de l'information dans le passage de $F_i$ à $F_{i-1}$ (cette construction modifiée est étudiée au paragraphe 4); l'application $f_{i-1} = \Pi(F_{i-1})$ possèdera les caractéristiques décrites dans l'alinéa précédent, en particulier un autre point fixe proche de 0, qui ne proviennent pas de $F_i$. On aura d'ailleurs une certaine latitude dans l'information qu'on injecte en passant de $F_i$ à $F_{i-1}$, ce qui permet en fin de compte d'obtenir pour $F_0$ des exemples ayant une grande variété de propriétés, lorsque $\alpha$ n'est pas un nombre de Bruno. Ces exemples sont étudiés au Paragraphe 6.

Finalement, le lecteur aura remarqué que nous n'avons considéré dans la discussion précédente que le cas de $\widehat{S}_{\beta}$, $\beta > 0$; ceci n'est pas une restriction, car on passe aisément de $\widehat{S}_{\beta}$ à $\widehat{S}_{-\beta}$ en associant à $F \in \widehat{S}_{\beta}$ l'élément $F^{*} \in \widehat{S}_{-\beta}$ défini par :

$$
F ^ {*} (z) = - \overline {{{{F (- \bar {z})}}}}.
$$

## 3 - Premières estimations et minoration de $R(\alpha)$.

3.1 - L'objet de ce paragraphe est d'obtenir des estimations quantitatives permettant de contrôler la construction qualitative de Douady et Ghys qui a été décrite sommairement en 2.9.

Ces estimations seront suffisantes pour nous permettre de démontrer la minoration de  $R(\alpha)$  donnée par le théorème, lorsque  $\alpha$  est un nombre de Bruno.

Par contre, pour obtenir des exemples $f$ avec la majoration souhaitée pour $R(f)$, il nous faudra modifier la construction de Douady et Ghys et démontrer les estimations correspondantes ; c'est l'objet du paragraphe 4.

3.2 - Nous fixons, jusqu'au Paragraphe 3.6, un nombre réel strictement positif $\alpha$ et une application $F \in \hat{S}_{\alpha}$.

Ecrivons $F$ sous la forme :

$$
F (z) = z + \alpha + \varphi (z), \quad z \in \mathbb {H},
$$

où $\varphi$ est une fonction $\mathbb{Z}$-périodique, holomorphe dans $\mathbb{H}$, vérifiant

$$
\lim _ {\Im z \rightarrow + \infty} \varphi (z) = 0
$$

Lemme.— Pour  $z \in H$ , on a

$$
| D \varphi (z) | \leq \frac {2 \exp (- 2 \pi \Im z)}{1 - \exp (- 2 \pi \Im z)},
$$

$$
| \varphi (z) | \leq - \frac {1}{\pi} \mathrm{Log} (1 - \exp (- 2 \pi \Im z)).
$$

Démonstration. Soit $f\in S_{1}$ la fonction univalente satisfaisant

$$
f (E (z)) = E (z + \varphi (z)), \quad z \in \mathbb {H}.
$$

On a :

$$
D \varphi (z) = E (z) \frac {f ^ {\prime} (E (z))}{f (E (z))} - 1.
$$

Or toute fonction univalente $f \in S_{1}$ satisfait :

$$
\left| u \frac {f ^ {\prime} (u)}{f (u)} - 1 \right| \leq \frac {2 | u |}{1 - | u |}, \quad u \in \mathbb {D}.
$$

La première inégalité du lemme s'en déduit et la seconde en résulte par intégration.

Remarque : Je n'ai pas trouvé de référence pour l'inégalité de distorsion, surement classique, utilisée dans la preuve du lemme. En voici une démonstration. Pour $u_{0} \in \mathbb{D}$, posons :

$$
g (u) = \frac {f (u _ {0}) - f \left(\frac {u _ {0} - u}{1 - \bar {u} _ {0} u}\right)}{(1 - | u _ {0} | ^ {2}) f ^ {\prime} (u _ {0})}.
$$

On a $g\in S_1$ et

$$
u _ {0} \frac {f ^ {\prime} (u _ {0})}{f (u _ {0})} = \frac {u _ {0}}{(1 - | u _ {0} | ^ {2}) g (u _ {0})}.
$$

Ecrivons

$$
g (u) ^ {- 1} = u ^ {- 1} + \sum_ {n \geq 0} b _ {n} u ^ {n}.
$$

D'après le théorème de l'aire, on a :

$$
\left| b _ {0} \right| \leq 2, \sum_ {n \geq 1} n \left| b _ {n} \right| ^ {2} \leq 1,
$$

d'où on tire

$$
\left| \frac {u}{g (u)} - 1 \right| \leq 2 | u | + | u | ^ {2}, u \in \mathbb {D}.
$$

On obtient donc

$$
\begin{array}{r l r} & & {\left| u _ {0} \frac {f ^ {\prime} (u _ {0})}{f (u _ {0})} - 1 \right| \leq \frac {1}{1 - | u _ {0} | ^ {2}} \left| \frac {u _ {0}}{g (u _ {0})} - 1 \right| + \frac {| u _ {0} | ^ {2}}{1 - | u _ {0} | ^ {2}},} \\ & & {\leq \frac {2 | u _ {0} |}{1 - | u _ {0} |}.} \end{array}
$$

On utilisera dans la suite les estimations du lemme sous la forme suivante: posons $c_0 = 1/2, c_1 = \exp(-2\pi c_0) < 1/23, c_2 = 2c_1(1 - c_1)^{-1} < 1/11, c_3 = \pi^{-1}\mathrm{Log}(1 - c_1)^{-1} < 1/71$; pour $z \in \mathbb{H}, \Im z = c_0 + t \geq c_0$, on a

$$
\begin{array}{r} | D \varphi (z) | \leq c _ {2} \exp (- 2 \pi t), \\ | \varphi (z) | \leq c _ {3} \exp (- 2 \pi t). \end{array}\tag{1}
$$

Définissons :

$$
t _ {0} = \frac {1}{2 \pi} \mathrm{Log} ^ {+} \alpha^ {- 1},
$$

$$
z _ {0} = i (c _ {0} + t _ {0}),
$$

$$
\ell = \{i s, s \in \mathbb {R}, s \geq c _ {0} + t _ {0} \},
$$

et désignons par $\ell'$ le segment joignant $z_0$ et $F(z_0)$.

Pour $z \in \ell$, on a, d'après (1):

$$
\begin{array}{c} | F (z) - z - \alpha | \leq c _ {3} \operatorname * {M i n} (1, \alpha) \leq 1 / 7 1 \alpha , \\ | F ^ {\prime} (z) - 1 | \leq c _ {2} \operatorname * {M i n} (1, \alpha) \leq 1 / 1 1, \end{array}\tag{2}
$$

donc les courbes $\ell, \ell'$ et $F(\ell)$ forment le bord d'un ouvert connexe contenu dans $\mathbb{H}$ que nous noterons $\mathcal{U}_F$.

En recollant les bords $\ell$ et $F(\ell)$ de $\overline{\mathcal{U}}_F$ suivant $F$, on obtient une variété topologique $\mathcal{V}$, de bord $\partial \mathcal{V}$; de plus, $\mathcal{V} - \partial \mathcal{V}$ est canoniquement muni d'une structure complexe qui en fait une surface de Riemann; il est facile de voir que celle-ci est biholomorphe à $\mathbb{D}^*$. Notons $i: \overline{\mathcal{U}}_F \to \mathcal{V}$ l'application canonique, de sorte que $i(\ell') = \partial \mathcal{V}$.

Soit C une courbe de Jordan dans C, telle que la composante connexe bornée V de C - C contienne 0. Soit  $y_{0} \in C$ ; par le théorème de Carathéodory, il existe un unique homéomorphisme  $\widetilde{K}$  de V sur  $\bar{V} - \{0\}$ , holomorphe dans  $V - \partial V$ , tel que  $\tilde{K}(i(z_{0})) = y_{0}$ . Soit  $K : \overline{U}_{F} \to C$  une application continue dans  $\overline{U}_{F}$ , holomorphe dans  $U_{F}$  vérifiant  $E \circ K = \widetilde{K} \circ i$ . L'application K est déterminée, à translations entières près, par C et  $y_{0}$ ; elle possède les propriétés suivantes :

(i) $K(F(z)) = K(z) + 1$, pour $z \in \ell$;

(ii) si $z, z'$ sont deux points distincts de $\overline{\mathcal{U}}_F$ tels que $K(z) - K(z') \in \mathbb{Z}$, alors $z \in \ell$, $z' = F(z)$, ou $z' \in \ell$, $z = F(z')$.

Réciproquement, toute application $K: \overline{\mathcal{U}}_F \to \mathbb{C}$, continue sur $\overline{\mathcal{U}}_F$, holomorphe sur $\mathcal{U}_F$ et vérifiant (i) et (ii) est obtenue par la construction précédente. De telles applications seront appelées dans la suite applications uniformisantes de $F$.

## 3.3 - Prolongement des applications uniformisantes.

On note V le domaine défini par :

$$
\mathcal {V} = \{z, \Im z \geq c _ {4} | \Re z | + t _ {0} + c _ {0} + c _ {3} \}
$$

où $c_{0}$, $t_{0}$, $c_{3}$ sont définis en 3.2 et $c_{4} = c_{3}(1 - c_{3})^{-1} < 1 / 70$.

Proposition.— Toute application uniformisante K de F s'étend en une application (encore notée K) continue et injective sur  $V \cup \bar{U}_{F}$ , holomorphe sur l'intérieur de ce domaine, qui vérifie :

$$
K (F (z)) = K (z) + 1,
$$

lorsque z et  $F(z)$  appartiennent à  $V \cup \bar{U}_{F}$ .

Remarque : Le domaine V est loin d'être optimal (on peut obtenir des domaines de la forme  $\{\Im z \geq c\mathrm{Log}(c' + c''|\Re z|)\}$ , avec  $c, c', c'' > 0$ ) mais la conclusion plus facile de la proposition nous suffira pour la suite.

Démonstration. Pour $z \in \mathcal{V}$, on a d'après (2):

$$
\begin{array}{r l} & {\Im F (z) + c _ {4} \Re F (z) \geq \Im z + c _ {4} \Re z,} \\ & {\Im F (z) - c _ {4} \Re F (z) \leq \Im z - c _ {4} \Re z,} \end{array}
$$

pour $z\in \mathcal{V}$

$$
\text { Posons } \mathcal {V} _ {-} = \mathcal {V} \cap \{z, \Re z \leq 0 \}, \quad \mathcal {V} _ {+} = \mathcal {V} \cap \{z, \Re z \geq 0 \}.
$$

D'après les relations précédentes, on a :

$$
\begin{array}{l} F (\mathcal {V} _ {-}) \subset \mathcal {V} _ {-} \cup \overline {{\mathcal {U}}} _ {F}, \\ \mathcal {V} _ {+} \subset \overline {{\mathcal {U}}} _ {F} \cup F (\mathcal {V} _ {+}). \end{array}
$$

Comme on a $\Re F(z) \geq \Re z + (1 - c_3)\alpha$ pour tout $z \in \mathcal{V}$, il existe, pour tout $z \in \mathcal{V}_{-} \cup \overline{\mathcal{U}}_F$, un plus petit entier $n = n(z)$ tel que $F^n(z)$ appartienne à $\overline{\mathcal{U}}_F$. Posons :

$$
K _ {-} (z) = K \left(F ^ {n (z)} (z)\right) - n (z),
$$

pour $z \in \mathcal{V}_{-} \cup \overline{\mathcal{U}}_{F}$; la fonction $K_{-}$ est continue sur $\mathcal{V}_{-} \cup \overline{\mathcal{U}}_{F}$ puisqu'en tout point $z_{0}$ de discontinuité de $n$, on a $F^{n(z_0)}(z_0) \in \ell$ d'où $K(F^{n(z_0)+1}(z_0)) = K(F^{n(z_0)}(z_0)) + 1$. La fonction $K_{-}$ est donc holomorphe dans l'intérieur de $\mathcal{V}_{-} \cup \overline{\mathcal{U}}_{F}$, et coïncide avec $K$ sur $\overline{\mathcal{U}}_{F}$.

De même, on définit une fonction continue $K_{+}$ sur $\mathcal{V}_{+} \cup \overline{\mathcal{U}}_{F}$, holomorphe dans l'intérieur de $\mathcal{V}_{+} \cup \overline{\mathcal{U}}_{F}$, et coïncidant avec $K$ sur $\overline{\mathcal{U}}_{F}$ en posant :

$$
K _ {+} (z) = K \left(F ^ {- m (z)} (z)\right) + m (z),
$$

où $m(z)$ est le plus petit entier $m$ tel que $F^{-m}(z)$ appartienne à $\overline{\mathcal{U}}_F$.

On a ainsi défini un prolongement de $K$ (encore noté $K$) continu sur $\mathcal{V} \cup \overline{\mathcal{U}}_F$, holomorphe dans l'intérieur de $\mathcal{V} \cup \overline{\mathcal{U}}_F$, et vérifiant :

$$
K (F (z)) = K (z) + 1,
$$

lorsque $z$ et $F(z)$ appartiennent à $\mathcal{V} \cup \overline{\mathcal{U}}_F$.

Montrons que $K$ est injectif sur $\mathcal{V} \cup \overline{\mathcal{U}}_F$. Soient $z, z' \in \mathcal{V} \cup \overline{\mathcal{U}}_F$ tels que $K(z) = K(z')$, et $m, m' \in \mathbb{Z}$ des entiers tels que $F^m(z)$ et $F^{m'}(z')$ appartiennent à $\overline{\mathcal{U}}_F$. On a alors :

$$
K (F ^ {m} (z)) - K (F ^ {m ^ {\prime}} (z ^ {\prime})) = m - m ^ {\prime}
$$

et la propriété (ii) des applications uniformisantes montre qu'on est dans l'un des trois cas suivants :

\- $m = m'$, $F^m(z) = F^{m'}(z')$;

\- $m = m' + 1$, $F^{m'}(z') \in \ell$, $F^{m}(z) = F(F^{m'}(z'))$;

•  $m' = m + 1$ ,  $F^{m}(z) \in \ell$ ,  $F^{m'}(z') = F(F^{m}(z))$ .

Dans tous les cas, on conclut, d'après l'injectivité de $F$, que $z = z'$.

## 3.4 - Distorsion des applications uniformisantes.

Lemme 1.— Soit g une fonction holomorphe et injective dans D. Pour  $z \in D$ , on a :

$$
| g (z) - g (- z) - 2 D g (0) z | \leq 2 | D g (0) | | z | ^ {3} \frac {3 - | z | ^ {2}}{(1 - | z | ^ {2}) ^ {2}}.
$$

Démonstration. On se ramène immédiatement au cas où $g(0) = 0$, $Dg(0) = 1$. En écrivant alors $g(z) = z + \sum_{n \geq 2} a_n z^n$, on a :

$$
g (z) - g (- z) - 2 z = 2 \sum_ {n \geq 1} a _ {2 n + 1} z ^ {2 n + 1}.
$$

D'après la conjecture de Bieberbach, démontrée par De Branges, on a $|a_{2n+1}| \leq 2n+1$, et un calcul immédiat avec la fonction de Koebe donne l'estimation du lemme.

Lemme 2.— Soit $z_{0}$ un point de $\mathbb{H}$, tel que $\Im z_{0} \geq t_{0} + c_{0} + \frac{1}{2}c_{3}$; il existe un unique point $z_{1}$ de $\mathbb{H}$ qui vérifie:

$$
\begin{array}{l} \Im z _ {1} \geq \Im z _ {0} - \frac {1}{2} c _ {3}, \\ F (z _ {1}) + z _ {1} = 2 z _ {0}, \end{array}
$$

et on a de plus, en posant $s = \Im z_0 - t_0 - c_0 - \frac{1}{2} c_3$:

$$
\left| F \left(z _ {1}\right) - z _ {1} - \alpha \right| \leq c _ {3} \operatorname{Min} (1, \alpha) \exp (- 2 \pi s).
$$

Démonstration. Sur le demi-plan $\{z, \Im z \geq t_0 + c_0 + s\}$, la fonction $h(z) = \frac{1}{2}(z + F(z))$ vérifie, d'après (1):

$$
| D h (z) - 1 | \leq \frac {1}{2} c _ {2} <   1 / 2 2;
$$

$$
\Im h (z) \leq \Im z + \frac {1}{2} c _ {3}.
$$

L'application h est donc un difféomorphisme biholomorphe sur son image, et celle-ci contient le demi-plan  $\left\{z,\Im z\geq t_{0}+c_{0}+s+\frac{1}{2}c_{3}\right\}$ ; l'existence et l'unicité de  $z_{1}$  en résultent. La dernière estimation du lemme résulte immédiatement de (1).

Soient K une uniformisante de F, et  $z_{0}$  un point de H. Nous supposons que :

$$
| \Re z _ {0} | \leq \operatorname{Max} (1, \alpha),
$$

$$
\Im z _ {0} \geq t _ {0} + c _ {0} + c _ {3} + c _ {4} \operatorname{Max} (1, \alpha).
$$

Posons alors :

$$
w = \Im z _ {0} - t _ {0} - c _ {0} - c _ {3} - c _ {4} \operatorname{Max} (1, \alpha),
$$

$$
r _ {0} = c _ {5} ^ {- 1} w, c _ {5} = (1 + c _ {4} ^ {2}) ^ {1 / 2} <   1 + 1 / 9 8 0 0.
$$

Le disque de centre $z_0$ et de rayon $r_0$ est contenu dans $\mathcal{V}$. Notons d'autre part $z_1$ le point (donné par le Lemme 2) tel que $F(z_1) + z_1 = 2z_0$; on a :

$$
r _ {1} = | z _ {1} - z _ {0} | \leq \frac {1 + c _ {3}}{2} \alpha ,
$$

d'après le Lemme 2. Supposons qu'on ait

$$
r _ {0} \geq (1 + c _ {3}) \alpha , w \geq c _ {5} (1 + c _ {3}) \alpha ,
$$

de sorte que $z_1$ et $F(z_1)$ sont contenus dans le disque de centre $z_0$ et de rayon $\frac{1}{2} r_0$. Comme l'application $K$ est holomorphe et injective dans $\mathcal{V}$, l'application :

$$
g (z) = K \left(z _ {0} + r _ {0} z\right)
$$

est holomorphe et injective dans $\mathbb{D}$. Nous appliquons l'estimation du lemme 1 avec $u = r_0^{-1}(z_1 - z_0)$:

$$
| g (u) - g (- u) - 2 D g (0) u | \leq 2 | D g (0) | | u | ^ {3} \frac {3 - | u | ^ {2}}{(1 - | u | ^ {2}) ^ {2}}.
$$

Or, on a :

$$
\begin{array}{c} {g (u) = K (z _ {1}) \quad ,} \\ {g (- u) = K (F (z _ {1})) = K (z _ {1}) + 1 \quad ,} \\ {D g (0) = r _ {0} D K (z _ {0}) \quad ,} \end{array}
$$

$$
| u | = r _ {1} r _ {0} ^ {- 1} \leq 1 / 2, \quad \mathrm{d} ^ {\prime} \text {où} \quad \frac {3 - | u | ^ {2}}{(1 - | u | ^ {2}) ^ {2}} \leq 5,
$$

$$
2 D g (0) u = D K (z _ {0}) \left(z _ {1} - F (z _ {1})\right),
$$

donc l'inégalité précédente donne :

$$
\left| 1 - D K (z _ {0}) \left(F (z _ {1}) - z _ {1}\right) \right| \leq 1 0 \left| D K (z _ {0}) \right| r _ {1} ^ {3} r _ {0} ^ {- 2}.
$$

On compare $F(z_{1}) - z_{1}$ à $\alpha$ par la dernière inégalité du Lemme 2, en posant :

$$
s = \Im z _ {0} - t _ {0} - c _ {0} - \frac {c _ {3}}{2} = w + \frac {c _ {3}}{2} + c _ {4} \operatorname{Max} (1, \alpha).
$$

On obtient ainsi, en utilisant aussi l'inégalité $r_{1} \leq \frac{1+c_{3}}{2}\alpha$:

$$
\left| 1 - \alpha D K (z _ {0}) \right| \leq \theta \left| D K (z _ {0}) \right|,\tag{3}
$$

où on a posé :

$$
\theta = c _ {3} \operatorname{Min} (1, \alpha) \exp (- 2 \pi s) + \frac {5}{4} c _ {5} ^ {2} (1 + c _ {3}) ^ {3} w ^ {- 2} \alpha^ {3}.
$$

Comme $\exp(-2\pi s) \leq \exp(-2\pi w) \leq (\pi ew)^{-2}$ pour $w > 0$, on a $\theta \leq c(\alpha)w^{-2}$, avec:

$$
c (\alpha) = (e \pi) ^ {- 2} c _ {3} \operatorname{Min} (1, \alpha) + \frac {5}{4} c _ {5} ^ {2} (1 + c _ {3}) ^ {3} \alpha^ {3}.
$$

Distinguons maintenant les deux cas qui nous intéressent.

1er cas : $\alpha \leq 1 / 2$

On a fait les hypothèses :

$$
\begin{array}{c} {| \Re z _ {0} | \leq 1,} \\ {\Im z _ {0} \geq \frac {1}{2 \pi} \mathrm{Log} \alpha^ {- 1} + c _ {0} + c _ {3} + c _ {4} + c _ {5} (1 + c _ {3}) \alpha .} \end{array}
$$

On a alors

$$
c (\alpha) \leq \alpha [ c _ {3} (e \pi) ^ {- 2} + \frac {5}{1 6} c _ {5} ^ {2} (1 + c _ {3}) ^ {3} ] = c _ {6} ^ {2} \alpha , \quad c _ {6} <   0. 5 8.
$$

Observons qu'on a

$$
c _ {6} > \frac {1}{2} c _ {5} (1 + c _ {3}) \geq c _ {5} (1 + c _ {3}) \alpha .
$$

En posant $c_7 = c_0 + c_3 + c_4 + c_6 < 1.11$, l'estimation définitive pour $DK$ s'énonce alors comme suit :

Proposition 1.— Supposons $\alpha \leq 1/2$; soient $K$ une application uniformisante de $F$, et $z_0$ un point de $\mathbb{H}$ qui vérifie:

$$
\begin{array}{c} | \Re z _ {0} | \leq 1, \\ \Im z _ {0} > \frac {1}{2 \pi} \mathrm{Log} \alpha^ {- 1} + c _ {7}. \end{array}
$$

En posant $w = \Im z_0 - \frac{1}{2\pi} \mathrm{Log}\alpha^{-1} - c_7 + c_6 > c_6$, on a alors:

$$
| \alpha D K (z _ {0}) - 1 | \leq \frac {c _ {6} ^ {2}}{w ^ {2} - c _ {6} ^ {2}}.
$$

2ème cas : $\alpha \geq 2$

On a fait les hypothèses :

$$
\begin{array}{c} {| \Re z _ {0} | \leq \alpha ,} \\ {\Im z _ {0} \geq c _ {0} + c _ {3} + (c _ {4} + c _ {5} (1 + c _ {3})) \alpha .} \end{array}
$$

On a alors

$$
c (\alpha) \leq \alpha^ {3} [ \frac {1}{8} c _ {3} (e \pi) ^ {- 2} + \frac {5}{4} c _ {5} ^ {2} (1 + c _ {3}) ^ {3} ] = c _ {6} ^ {\prime 2} \alpha^ {3}, c _ {6} ^ {\prime} <   1. 1 5.
$$

Observons qu'on a

$$
c _ {6} ^ {\prime} > c _ {5} (1 + c _ {3}).
$$

En posant $c_7' = 1/2(c_0 + c_3) + c_4 + c_6' < 1.43$, l'estimation définitive pour $DK$ s'énonce alors comme suit :

Proposition 2.—

Supposons $\alpha \geq 2$; soient $K$ une application uniformisante de $F$, et $z_0$ un point de $\mathbb{H}$ qui vérifie :

$$
\left| \Re z _ {0} \right| \leq \alpha ,
$$

$$
\Im z _ {0} > c _ {7} ^ {\prime} \alpha .
$$

En posant $w = \Im z_0 - c_0 - c_3 - c_4\alpha > c_6'\alpha$, on a alors :

$$
\left| \alpha D K (z _ {0}) - 1 \right| \leq \frac {c _ {6} ^ {\prime 2} \alpha^ {2}}{w ^ {2} - c _ {6} ^ {\prime 2} \alpha^ {2}}.
$$

Remarque : Les estimations de la dérivée de $K$ données par les Propositions 1 et 2 sont très loin d'être optimales lorsque la partie imaginaire de $z_0$ tend vers l'infini ; en effet, $\alpha DK(z_0) - 1$ décroît exponentiellement vers 0. Cependant, l'important pour la suite n'est pas d'obtenir des estimations asymptotiques lorsque $\Im z_0$ tend vers l'infini, mais des estimations uniformes, indépendantes de $F \in \widehat{S_{\alpha}}$, sur des domaines dépendant explicitement de $\alpha$.

3.5 - Dans ce numéro, on suppose qu'on a $0 < \alpha \leq 1/2$ et on se donne une application uniformisante $K$ de $F$.

Posons

$$
t _ {1} = \frac {1}{2 \pi} \mathrm{Log} \alpha^ {- 1} + c _ {7} + c _ {6} + c _ {3},
$$

et définissons

$$
\begin{array}{c} \mathcal {W} = \left\{z, 0 \leq \Re z \leq 1, \Im z \geq t _ {1} \right\}, \\ \mathcal {W} _ {1} = \left\{z, 0 \leq \Re z \leq 1, \Im z \geq t _ {1} - c _ {3} \right\}. \end{array}
$$

Pout $z\in \mathcal{W}_1$ ,on a

$$
w = \Im z - \frac {1}{2 \pi} \mathrm{Log} \alpha^ {- 1} - c _ {7} + c _ {6} \geq 2 c _ {6},
$$

d'où, d'après la proposition 1

$$
| \alpha D K (z) - 1 | \leq \frac {4}{3} c _ {6} ^ {2} w ^ {- 2} \leq 1 / 3.\tag{4}
$$

Posons

$$
L (z) = K (z) - i \max _ {0 \leq s \leq 1} \Im (K (s + i t _ {1})), \quad z \in \mathcal {V} \cup \overline {{\mathcal {U}}} _ {F}
$$

En intégrant la relation (4), on obtient

$$
\Im (L (z)) \leq 0, \quad z \in \mathcal {W} _ {1} - \mathcal {W};\tag{5}
$$

et pour $z = s + it \in \mathcal{W}$

(6)

$$
\begin{array}{r l} & {\alpha \Im (L (z)) = \alpha (\Im (L (s + i t)) - \Im (L (s + i t _ {1}))) + \alpha \Im (L (s + i t _ {1}))} \\ & {\qquad \geq \Im z - t _ {1} - \frac {2}{3} c _ {6} - \frac {1}{3} = \Im z - \frac {1}{2 \pi} \mathrm{Log} \alpha^ {- 1} - c _ {8},} \\ & {\qquad c _ {8} = c _ {3} + c _ {7} + \frac {5}{3} c _ {6} + \frac {1}{3} <   2. 4 3.} \end{array}
$$

Soit $G$ la fonction définie sur $L(\mathcal{W})$ par :

$$
G (L (z)) = L (z - 1).
$$

Proposition.— L'application G se prolonge à H en un élément de  $\widehat{S}_{-\alpha^{-1}}$ .

Démonstration. D'après les relations (4) et (5), il existe un réel $t_{2} \geq t_{1}$ tel que $\Im(L(it_{2})) = 0$ et $\Im(L(it)) > 0$ pour $t > t_{2}$.

Notons $\ell_1$ l'image par $L$ de la demi-droite $\{it, t \geq t_2\}$; notons $\mathcal{D}$ le domaine fermé (bien défini d'après (4)) contenu dans $\overline{\mathbb{H}}$ délimité par $\ell_1$, $T\ell_1$ et le segment joignant $L(it_2)$ et $L(it_2) + 1$, qui est contenu dans $\mathbb{R}$. Il résulte des relations (4) et (5) qu'on a $\mathcal{D} \subset L(\mathcal{W})$, donc $G$ est défini et holomorphe sur $\mathcal{D}$. Pour $z \in \ell_1$, on a, en écrivant $z = L(it)$:

$$
\begin{array}{r l} & G (T (z)) = G (L (F (i t))) \\ & \qquad = L (F (i t) - 1) \\ & \qquad = L (F (i t - 1)) \\ & \qquad = T (L (i t - 1)) = T (G (z)) \end{array}
$$

ce qui permet de prolonger $G$ en une fonction holomorphe sur $\overline{\mathbb{H}}$ et commutant avec $T$.

D'après la proposition 1, la limite

$$
\lim _ {\Im z \to + \infty , | \Re z | \leq 1} (\alpha K (z) - z)
$$

existe. On en déduit

$$
\lim _ {\Im z \rightarrow + \infty} (G (z) - z) = - \alpha^ {- 1}.
$$

Il reste à vérifier l'injectivité de $G$, et pour ceci, il suffit de montrer que si deux points distincts $z, z'$ de $\mathcal{D}$ sont tels que $G(z') - G(z) \in \mathbb{N}$, alors on a $z \in \ell_1$ et $z' = z + 1$. En écrivant $z = L(s)$, $z' = L(s')$, on a donc:

$$
L (s ^ {\prime} - 1) = L (s - 1) + m, \quad m \in \mathbb {N}
$$

d'où $K(s' - 1) = K(s - 1) + m$; en revenant à la définition de $K$ dans $\mathcal{V} \cup \bar{\mathcal{U}}_F$ (cf. 3.3), qui contient $s - 1$ et $s' - 1$, on voit que cette relation implique $s' - 1 = F^m(s - 1)$, d'où $s' = F^m(s)$ et $z' = L(s') = L(s) + m = z + m$. Compte tenu de la définition de $\mathcal{D}$, on a bien $z \in \ell_1$ et $m = 1$.

3.6 - Conservons la situation du numéro précédent. La proposition suivante est l'ingrédient fondamental pour obtenir la minoration de $R(\alpha)$ annoncée dans le théorème.

Proposition.— Soient  $z \in W$  et n > 0 tels que  $F^{n}(z)$  n'appartienne pas à H. Il existe alors  $m \geq 0$ , strictement inférieur à n, tel que  $G^{m}(L(z))$  n'appartienne pas à H.

Remarque : Lorsque n est grand, l'ordre de grandeur correct de m est  $\alpha n$ , mais nous n'aurons pas besoin de ce fait.

Démonstration. Soit $p > 0$ le plus petit entier tel qu'on ait $\Im F^p(z) < t_1$. On a $\Im F^p(z) \geq t_1 - c_3 > 0$ d'après (1), par conséquent $p < n$.

Définissons pour $0 \leq i \leq p$ des points $z_0, \ldots, z_p$ de la façon suivante : on pose $z_0 = z$, et pour $i \geq 0$, $z_{i+1} = F(z_i)$ si $\Re F(z_i) \leq 1$, $z_{i+1} = F(z_i) - 1$ si $\Re F(z_i) > 1$. On a $0 \leq \Re z_i \leq 1$ pour $0 \leq i \leq p$ donc $z_i \in \mathcal{W}$ pour $0 \leq i < p$ et $z_p \in \mathcal{W}_1 - \mathcal{W}$.

Posons $y_{i} = L(z_{i})$ pour $0 \leq i \leq p$. On a $y_{i+1} = y_{i} + 1$ lorsque $z_{i+1} = F(z_{i})$, et $y_{i+1} = G(y_{i}) + 1$ lorsque $z_{i+1} = F(z_{i}) - 1$. Par conséquent, on a :

$$
y _ {p} = G ^ {m} \left(L (z)\right) + p,
$$

avec $0 \leq m \leq p < n$.

Pour conclure, il suffit de vérifier que $y_{p}$ n'appartient pas à $\mathbb{H}$. Comme $z_{p} \in \mathcal{W}_{1} - \mathcal{W}$, cela résulte de la relation (5).

## 3.7 - Démonstration de la minoration de $R(\alpha)$.

D'après le Paragraphe 2.8, la proposition suivante implique la minoration de $R(\alpha)$ annoncée dans le théorème.

Proposition.— Soient  $\alpha$  un nombre de Bruno et  $F \in \widehat{S}_{\alpha}$ . On a :

$$
d _ {F} \leq \frac {1}{2 \pi} \Phi (\alpha) + 2 c _ {8}.
$$

Démonstration. Raisonnons par l'absurde ; si la conclusion de la proposition est fausse, il existe $\alpha\in\mathcal{B}$, $F\in\widehat{S}_{\alpha}$, $z\in\mathbb{H}$ et $n>0$ tels qu'on ait :

$$
\Im F ^ {n} (z) \leq 0;
$$

$$
\Im z \geq \frac {1}{2 \pi} \Phi (\alpha) + 2 c _ {8}.
$$

Choisissons $\alpha$, $F$ et $z$ de sorte que $n$ soit le plus petit possible. Quitte à remplacer $F$ par $F+p$, $p\in\mathbb{Z}$, on peut supposer qu'on a $|\alpha|<1/2$, et quitte à remplacer $F(z)$ par $-\overline{F(-\bar{z})}$, on peut supposer qu'on a $0<\alpha<1/2$. On a :

$$
\frac {1}{2 \pi} \Phi (\alpha) + 2 c _ {8} \geq t _ {1},
$$

donc, quitte à remplacer $z$ par $z+p$, pour $p\in\mathbb{Z}$, on peut supposer que $z$ appartient à $\mathcal{W}$.

Construisons alors L et G comme indiqué dans les paragraphes précédents. On

$$
\begin{array}{r l} & {\Im (L (z)) \geq \alpha^ {- 1} \left[ \Im z - \frac {1}{2 \pi} \mathrm{Log} \alpha^ {- 1} - c _ {8} \right] \quad (\mathrm {d^ {\prime} après(6)})} \\ & {\qquad \geq \alpha^ {- 1} \left[ \frac {1}{2 \pi} \Phi (\alpha) - \frac {1}{2 \pi} \mathrm{Log} \alpha^ {- 1} + c _ {8} \right]} \\ & {\qquad \geq \frac {1}{2 \pi} \Phi (- \frac {1}{\alpha}) + 2 c _ {8},} \end{array}
$$

d'après l'équation fonctionnelle de $\Phi$ (cf.1.5) et $\alpha^{-1} > 2$.

Mais la proposition du paragraphe 3.6 montre qu'on contredit alors la minimalité de n.

On obtient donc, compte tenu de 2.5 et 2.8

$$
\mathrm{Log} R (\alpha) ^ {- 1} \leq \Phi (\alpha) + 4 \pi c _ {8}, \quad 4 \pi c _ {8} <   1 5. 2 4.
$$

Ceci achève la démonstration du théorème de Siegel et Bruno.

## 4. La construction fondamentale.

## 4.1 - Les données.

On se donne $\alpha > 0$, et un élément $F \in \widehat{S}_{\alpha}$. On suppose que $\alpha$ est assez grand, ce que nous écrivons $\alpha > A$, où $A \geq 2$ est une constante à déterminer dans la suite. (On obtiendra $A = c_{14} < 100$).

La construction nécessite deux fonctions auxiliaires :

a) Une application $\eta$ de classe $C^\infty$ de $\mathbb{R}$ dans $[0,1]$, analytique sauf en $\pm 1/2$, qui vérifie $\eta(t) = 0$ pour $t \leq -1/2$, $\eta(t) = 1$ pour $t \geq 1/2$, et $0 \leq D\eta(t) \leq 2$ pour tout $t$; nous choisissons une telle application une fois pour toutes.

b) Une application $J$ holomorphe de $\mathbb{H}$ dans $\mathbb{C}$ qui a la propriété suivante : Il existe $\Delta\alpha\in\mathbb{C}, |\Delta\alpha|\leq c_{9}=1/100$ tel que $J-\Delta\alpha\in\hat{S}_{\alpha}$; on posera $\alpha'=\alpha+\Delta\alpha$.

Différents choix pour J aboutiront - au prochain paragraphe - à différentes propriétés pour les germes de difféomorphismes holomorphes qu'on construira.

## 4.2 - Description qualitative de la construction.

Nous commençons par conjuguer F et J par des translations, en posant :

$$
F _ {0} (z) = F (z + i) - i,
$$

$$
J _ {0} (z) = J (z + i) - i,
$$

puis considérons le conjugué  $J_{1}$  de  $J_{0}$  par la conjugaison complexe :

$$
J _ {1} (z) = \overline {{{{J _ {0} (\bar {z})}}}}.
$$

Les applications $F_{0}$ et $J_{1}$ sont respectivement définies dans les demi-plans $\{z, \Im z > -1\}$ et $\{z, \Im z < 1\}$.

Nous définissons ensuite une application $\chi$ de $i\mathbb{R}$ dans $\mathbb{C}$ en posant, pour $s\in\mathbb{R}$:

$$
\chi (i s) = \eta (s) F _ {0} (i s) + (1 - \eta (s)) J _ {1} (i s).
$$

L'application $\chi$ est de classe $C^\infty$, et on verra au Paragraphe 4.3 qu'elle vérifie :

$$
\Im \left(\frac {d}{d s} \chi (i s)\right) > 0, \quad \Re (\chi (i s)) > 0.
$$

Considérons alors le domaine fermé $\mathcal{X}$ délimité par $i\mathbb{R}$ et $\chi(i\mathbb{R})$. Recollons les bords de $\mathcal{X}$ suivant $\chi$; on obtient une surface $S$, et le complémentaire $S'$ dans $S$ des images de $\pm i/2$ est canoniquement une surface de Riemann. Il est facile de voir que $S'$ est biholomorphe à $S^2$-$\{4$ points $\}$. En particulier, $S$ est aussi canoniquement une surface de Riemann. Il existe donc une unique application $K_0$ continue sur $\mathcal{X}$, holomorphe et injective sur l'intérieur de $\mathcal{X}$, à valeurs dans $\mathbb{C}^*$, qui vérifie :

$$
K _ {0} \left(\chi (i s)\right) = K _ {0} (i s), \quad s \in \mathbb {R},
$$

$$
\lim _ {s \to + \infty} K _ {0} (i s) = 0,
$$

$$
K _ {0} (0) = 1.
$$

Notons d'autre part R le carré de sommets  $\pm i/2,1\pm\frac{i}{2}$ . Nous définissons une application  $G_{0}$  de X-R dans X en posant :

$$
\begin{array}{l} G _ {0} (z) = z - 1 \qquad \text {pour} \quad \Re z \geq 1, \\ G _ {0} (z) = F _ {0} (z) - 1 \qquad \text {pour} \quad 0 \leq \Re z <   1, \quad \Im z \geq \frac {1}{2} \\ G _ {0} (z) = J _ {1} (z) - 1 \qquad \text {pour} \quad 0 \leq \Re z <   1, \quad \Im z \leq - \frac {1}{2} \end{array}
$$

Comme on a $\chi(is) = F_{0}(is)$ pour $s \geq 1/2$, $\chi(is) = J_{1}(is)$ pour $s \leq -1/2$, l'application $G_{0}$ est compatible avec l'identification par $\chi$ et il existe une unique application holomorphe $G_{1}$ de $\mathbb{C}^{*} - K_{0}(R)$ dans $\mathbb{C}^{*}$ qui vérifie :

$$
G _ {1} \left(K _ {0} (z)\right) = K _ {0} \left(G _ {0} (z)\right), \quad z \in \mathcal {X} - R.
$$

En notant $\overline{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$, on vérifie aisément que $G_1$ se prolonge en une application holomorphe de $\overline{\mathbb{C}} - K_0(R)$ dans $\overline{\mathbb{C}}$, admettant en 0 et $\infty$ deux points fixes dont les valeurs propres respectives sont $E(-1/\alpha)$ et $E(1/\alpha')$.

Finalement, considérons l'homographie :

$$
k (z) = t \frac {z}{z - 1},
$$

où t > 0 est choisi dans la suite, et la conjuguée  $g = kG_{1}k^{-1}$  de  $G_{1}$  par k. L'application g est holomorphe dans le domaine  $\overline{\mathbb{C}} - kK_{0}(R)$ ; elle possède deux points fixes en 0 et t, de valeurs propres respectives  $E(-1/\alpha)$  et  $E(1/\alpha')$ . Elle est injective, car  $G_{0}$  et  $G_{1}$  le sont.

On choisit $t$ de façon que $g$ soit définie sur $\mathbb{D}$; pour ceci, il suffit qu'on ait $|k(z)| > 1$ pour $z \in K_0(R)$, ce qui a lieu dès que :

$$
| K _ {0} (z) - 1 | <   \frac {t}{1 + t}, \quad \forall z \in R.
$$

L'application $g$ appartient alors à $S_{-1/\alpha}$. Notons $G$ l'unique difféomorphisme de $\widehat{S}_{-1/\alpha}$ qui vérifie $E(G(z)) = g(E(z))$ pour $z \in \mathbb{H}$. Nous étudierons ses propriétés par rapport à celles de $F$ et de $J$. La difficulté technique principale est d'obtenir une estimation convenable pour $t$, à savoir $t = c_{15}\alpha^{-1}$, avec une constante universelle $c_{15}$.

## 4.3 - Estimations pour la fonction $\chi$.

Observons d'abord que d'après les définitions de $F_{0}, J_{1}$ et les relations (1) de 3.2, on a

$$
\left| F _ {0} (z) - z - \alpha \right| \leq c _ {3} \exp \left(- 2 \pi \left(s + \frac {1}{2}\right)\right),
$$

$$
\left| D F _ {0} (z) - 1 \right| \leq c _ {2} \exp \left(- 2 \pi \left(s + \frac {1}{2}\right)\right),
$$

pour $s = \Im z \geq -1/2$, et :

$$
\left| J _ {1} (z) - z - \alpha^ {\prime} \right| \leq c _ {3} \exp \left(2 \pi \left(s - \frac {1}{2}\right)\right),
$$

$$
\left| D J _ {1} (z) - 1 \right| \leq c _ {2} \exp \left(2 \pi \left(s - \frac {1}{2}\right)\right),
$$

pour $s = \Im z \leq 1/2$.

En particulier, on a :

$$
| \chi (i s) - i s - \alpha | \leq c _ {3} \exp (- 2 \pi (s + \frac {1}{2})),
$$

$$
\left| \frac {d}{d s} \chi (i s) - i \right| \leq c _ {2} \exp (- 2 \pi (s + \frac {1}{2})),
$$

$$
| \chi (i s ^ {\prime}) - i s ^ {\prime} - \alpha^ {\prime} | \leq c _ {3} \exp (2 \pi (s ^ {\prime} - \frac {1}{2})),
$$

$$
\left| \frac {d}{d s} \chi (i s ^ {\prime}) - i \right| \leq c _ {2} \exp (2 \pi (s ^ {\prime} - \frac {1}{2})),
$$

pour $s \geq 1/2$, $s' \leq -1/2$.

Pour $|s| \leq 1/2$, on a :

$$
\left| \chi (i s) - i s - \alpha \right| \leq \operatorname{Max} \left(\left| F _ {0} (i s) - i s - \alpha \right|, \left| J _ {1} (i s) - i s - \alpha \right|\right) \leq c _ {3} + c _ {9} <   1 / 4 1,
$$

car $|F_0(is) - is - \alpha|$ et $|J_1(is) - is - \alpha'|$ sont inférieurs à $c_3$. On a enfin :

$$
\begin{array}{r} \frac {d}{d s} \chi (i s) = D \eta (s) (F _ {0} (i s) - J _ {1} (i s)) + i \eta (s) D F _ {0} (i s) \\ + i (1 - \eta (s)) D J _ {1} (i s), \end{array}
$$

$\mathrm{avec}\left|D\eta (s)\right|\leq 2,\left|DF_{0}(is) - 1\right|\leq c_{2},\left|DJ_{1}(is) - 1\right|\leq c_{2}\mathrm{et}$

$|F_0(is) - J_1(is)| \leq 2c_3 + c_9$ , d'où on conclut que :

$$
\left| \frac {d}{d s} \chi (i s) - i \right| <   c _ {2} + 4 c _ {3} + 2 c _ {9} <   0. 1 7.
$$

On a bien vérifié les inégalités :

$$
\Im \left(\frac {d}{d s} \chi (i s)\right) > 0, \quad \Re (\chi (i s)) > 0,
$$

qui garantissent que le domaine X est bien défini.

Les estimations qui suivent seront utilisées au prochain numéro.

Pour $s \geq 0$, notons $v^{+}(s), v^{-}(s)$ les nombres complexes de partie imaginaire dans $]0, 2\pi[$ tels que

$$
\exp v ^ {+} (s) + \frac {\alpha + \alpha^ {\prime}}{2} = F _ {0} (i e ^ {s}),
$$

$$
\exp v ^ {-} (s) + \frac {\alpha + \alpha^ {\prime}}{2} = J _ {1} (- i e ^ {s})).
$$

Pour $s \geq 0$, nous avons

$$
\exp v ^ {+} (s) = i e ^ {s} - \frac {1}{2} \Delta \alpha + \varphi ((1 + e ^ {s}) i),
$$

$$
\frac {d}{d s} v ^ {+} (s) = (1 - i e ^ {- s} (- \frac {1}{2} \Delta \alpha + \varphi ((1 + e ^ {s}) i))) ^ {- 1} (1 + D \varphi ((1 + e ^ {s}) i),
$$

avec

$$
\left| - \frac {1}{2} \Delta \alpha + \varphi ((1 + e ^ {s}) i) \right| \leq \frac {1}{2} c _ {9} + c _ {3} e ^ {- 3 \pi} = c _ {1 0} <   1 / 1 9 9,
$$

$$
| D \varphi ((1 + e ^ {s}) i) | \leq c _ {2} e ^ {- 3 \pi},
$$

et des estimations similaires pour $v^{-}(s)$.

On en déduit

(1)

$$
| v ^ {\pm} - (s + i \pi) \pm \frac {i \pi}{2} | \leq \frac {3}{2} c _ {1 0} \exp (- \operatorname{Max} (s, \Re v ^ {\pm} (s))); \nonumber\tag{2}
$$

$$
\left| v ^ {+} (s) - v ^ {-} (s) + i \pi \right| \leq 3 c _ {1 0} \exp (- s);\tag{3}
$$

$$
| \frac {d}{d s} v ^ {\pm} (s) - 1 | \leq c _ {1 1} \exp (- s),
$$

$$
c _ {1 1} = 2 (c _ {1 0} + c _ {2} e ^ {- 3 \pi}) <   1 / 9 9.
$$

## 4.4 - Estimation du module d'un anneau.

Notre but, dans ce paragraphe et le suivant, est de démontrer l'estimation :

$$
| K _ {0} (z) - 1 | <   C \alpha^ {- 1}, \quad z \in R,
$$

avec une constante universelle C. Le plus simple serait bien sûr de démontrer la version infinitésimale :

$$
| D K _ {0} (z) | <   C \alpha^ {- 1}, \quad z \in R,
$$

mais il ne semble pas qu'une telle estimation soit toujours valable. Nous devons donc recourir à des techniques globales.

Nous considérons dans $S$ l'ouvert $\mathcal{A}$ dont la trace sur $\mathcal{X}$ est l'union des parties $\mathcal{A}_{1}$, $\mathcal{A}_{2}$ définies comme suit : $\mathcal{A}_{1}(\text{resp.}\mathcal{A}_{2})$ est l'intersection avec $\mathcal{X}$ de la couronne circulaire de rayon intérieur 3/2, de rayon extérieur $\left|\frac{\alpha+\alpha'}{4}\right|$ et de centre 0 (resp. de centre $\frac{\alpha+\alpha'}{2}$).

Pour que la définition ait un sens, il faut avoir  $\left|\frac{\alpha+\alpha'}{4}\right| > 3/2$ ; comme par hypothèse, on a  $|\alpha - \alpha'| \leq 1/100$ , ceci a lieu dès que  $\alpha \geq A \geq 4$ , ce que nous supposons dans la suite.

L'ouvert A est homéomorphe à un anneau ; son bord dans S possède de légers décrochements le long de l'image de iR dans S.

Nous allons minorer le module M de l'anneau A. Pour ce faire, considérons la fonction  $\rho$  sur A définie par :

$$
\rho (z) = \frac {1}{| z |} \quad \text { pour } \quad z \in \mathcal {A} _ {1},
$$

$$
\rho (z) = \frac {1}{\left| z - \frac {\alpha + \alpha^ {\prime}}{2} \right|} \quad \text { pour } \quad z \in \mathcal {A} _ {2}.
$$

Posons :

$$
S = \iint_ {\mathcal {A} _ {1} \cup \mathcal {A} _ {2}} \rho^ {2} d x d y,
$$

$$
L = \operatorname{Inf} _ {\gamma} \int_ {\gamma} \rho | d z |,
$$

où γ décrit l'ensemble des chemins (rectifiables) joignant les deux bords de A. On a (cf. [Ah]):

$$
M \geq L ^ {2} S ^ {- 1},
$$

donc pour minorer M il faut minorer L et majorer S.

La formule  $z = e^{u}$  définit un difféomorphisme biholomorphe du rectangle

$$
\tilde {\mathcal {A}} _ {1} = \left\{\log 3 / 2 \leq \Re u \leq \log \left| \frac {\alpha + \alpha^ {\prime}}{4} \right|, | \Im u | \leq \pi / 2 \right\}
$$

sur la région $\mathcal{A}_{1}$.

Les applications $s \mapsto \Re v^{\pm}(s)$, $s \geq 0$, sont strictement croissantes d'après la relation (3). Notons $\omega \mapsto \sigma^{\pm}(\omega)$ les applications inverses.

La formule  $z = e^{v} + \frac{\alpha + \alpha'}{2}$  définit un difféomorphisme biholomorphe du "rectangle"

$$
\tilde {\mathcal {A}} _ {2} = \left\{\log 3 / 2 \leq \Re v \leq \log \left| \frac {\alpha + \alpha^ {\prime}}{4} \right|, \Im v ^ {-} (\sigma^ {-} (\Re v)) \geq \Im v \geq \Im v ^ {+} (\sigma^ {+} (\Re v)) \right\}
$$

sur la région $\mathcal{A}_{2}$.

Dans les coordonnées $u$ sur $\mathcal{A}_{1}$ et $v$ sur $\mathcal{A}_{2}$ on a $\rho\equiv1$. Le point $s\pm i\pi/2$ du bord de $\tilde{\mathcal{A}}_{1}$ est identifié au point $v^{\pm}(s)$ du bord de $\tilde{\mathcal{A}}_{2}$.

Majoration de S.

On a :

$$
\int_ {\tilde {A} _ {1}} d x d y = \pi \mathrm{Log} \left| \frac {\alpha + \alpha^ {\prime}}{6} \right|;
$$

$$
\int_ {\tilde {\mathcal {A}} _ {2}} d x d y = \int_ {\mathrm{Log} 3 / 2} ^ {\mathrm{Log} \left| \frac {\alpha + \alpha^ {\prime}}{4} \right|} (\Im v ^ {-} (\sigma^ {-} (t)) - \Im v ^ {+} (\sigma^ {+} (t))) d t,
$$

où d'après (1)

$$
\Im v ^ {-} (\sigma^ {-} (t)) - \Im v ^ {+} (\sigma^ {+} (t)) \leq \pi + 3 c _ {1 0} e ^ {- t}.
$$

On obtient donc

$$
S \leq 2 \pi \mathrm{Log} \left| \frac {\alpha + \alpha^ {\prime}}{6} \right| + 2 c _ {1 0}.
$$

Minoration de L.

Considérons la fonction $\sigma : \tilde{\mathcal{A}}_1 \cup \tilde{\mathcal{A}}_2 \to \mathbb{R}$ définie par

$$
\sigma (u) = \Re u, \mathrm{si} u \in \tilde {\mathcal {A}} _ {1},
$$

$$
\sigma (v) = s, \text { si } v \in \tilde {\mathcal {A}} _ {2} \cap [ v ^ {-} (s), v ^ {+} (s) ].
$$

Cette fonction est compatible aux identifications prescrites des bords de $\tilde{\mathcal{A}}_1$ et $\tilde{\mathcal{A}}_2$.

D'après (1), on a, pour $v \in \tilde{\mathcal{A}}_2$:

(4)

$$
| \sigma (v) - \Re v | \leq \frac {3}{2} c _ {1 0} \exp (- \Re v).
$$

D'autre part, écrivons

$$
v = t v ^ {+} (\sigma) + (1 - t) v ^ {-} (\sigma), 0 \leq t \leq 1,
$$

$$
d v = (v ^ {+} (\sigma) - v ^ {-} (\sigma)) d t + (t \frac {d}{d \sigma} v ^ {+} (\sigma) + (1 - t) \frac {d}{d \sigma} v ^ {-} (\sigma)) d \sigma ,
$$

où,d'après le numéro précédent

$$
\begin{array}{r} | v ^ {+} (\sigma) - v ^ {-} (\sigma) + i \pi | \leq 3 c _ {1 0} e ^ {- \sigma}, \\ | t \frac {d}{d s} v ^ {+} (\sigma) + (1 - t) \frac {d}{d s} v ^ {-} (\sigma) - 1 | \leq c _ {1 1} e ^ {- \sigma}. \end{array}
$$

On en déduit

$$
\begin{array}{r l} & {| d v | \geq (1 - 9 \pi^ {- 2} c _ {1 0} ^ {2} e ^ {- 2 \sigma}) ^ {1 / 2} - c _ {1 1} e ^ {- \sigma}} \\ & {\qquad \geq (1 - c _ {1 2} e ^ {- \sigma}) | d \sigma |,} \\ & {c _ {1 2} = c _ {1 1} + \frac {1}{3} c _ {1 0} ^ {2} <   1 / 9 8.} \end{array}\tag{5}
$$

Soit $\gamma : [0,1] \to S$ un chemin rectifiable dans $A$ joignant les bords de $A$. En identifiant $A$ à $\tilde{A}_1 \cup \tilde{A}_2$ et en considérant l'application $t \mapsto \sigma(\gamma(t))$, on déduit de (4) et (5) que

$$
\int_ {\gamma} \rho | d z | \geq \int_ {\sigma_ {0}} ^ {\sigma_ {1}} (1 - c _ {1 2} e ^ {- \sigma}) d \sigma ,
$$

où

$$
\sigma_ {0} = \mathrm{Log} \frac {3}{2} + c _ {1 0},
$$

$$
\sigma_ {1} = \mathrm{Log} \left| \frac {\alpha + \alpha^ {\prime}}{4} \right| - c _ {1 0}.
$$

On conclut que

$$
L \geq \mathrm{Log} \left| \frac {\alpha + \alpha^ {\prime}}{6} \right| - 2 c _ {1 0} - \frac {2}{3} c _ {1 2}.
$$

## Minoration de M.

En combinant la majoration de S et la minoration de L, on obtient, pour le module M de l'anneau A l'estimation :

$$
M \geq \frac {1}{2 \pi} (\mathrm{Log} \left| \frac {\alpha + \alpha^ {\prime}}{6} \right| - c _ {1 3}),
$$

$$
c _ {1 3} = (4 + \pi^ {- 1}) c _ {1 0} + \frac {4}{3} c _ {1 2} <   1 / 2 8.
$$

## 4.5 - Majoration du diamètre de $K_{0}(R)$.

Elle s'obtient en combinant l'estimation du paragraphe précédent et le résultat suivant dû à Teichmüller ([Ah]). Soit B un ouvert de C, homéomorphe à un anneau, et  $\mathcal{B}_{1}(\text{resp.}\mathcal{B}_{2})$  la composante bornée (resp. non bornée) de C - B ; supposons que 0 appartienne à  $B_{2}$ , 1 appartienne à  $B_{1}$  et notons M le module de B ; pour tout  $z_{0} \in B_{1}$ , on a alors :

$$
1 6 \left(1 + \frac {1}{| z _ {0} - 1 |}\right) \geq \exp (2 \pi M).
$$

c'est- à-dire

$$
| z _ {0} - 1 | \leq \frac {1 6}{\exp (2 \pi M) - 1 6},
$$

dès que $\exp(2\pi M) > 16$. Nous appliquons ce résultat avec l'anneau $\mathcal{B} = K_0(\mathcal{A})$. Les hypothèses sont satisfaites (on a fait la normalisation $K_0(0) = 1$), donc on obtient, d'après la minoration du module de $\mathcal{B}$ du paragraphe précédent, pour $z \in R$:

$$
\left| K _ {0} (z) - 1 \right| \leq \frac {1 6}{\left| \frac {\alpha + \alpha^ {\prime}}{6} \right| e ^ {- c _ {1 3}} - 1 6} \leq \frac {9 6 e ^ {c _ {1 3}}}{2 \alpha - c _ {9} - 9 6 e ^ {c _ {1 3}}}.
$$

dès que $\alpha > \frac{1}{2} c_9 + 48e^{c_{13}}$.

On suppose finalement qu'on a

$$
\alpha > c _ {1 4} = \frac {1}{2} c _ {9} + 9 6 e ^ {c _ {1 3}}, \quad c _ {1 4} <   1 0 0
$$

et on pose

$$
c _ {1 5} = 9 6 e ^ {c _ {1 3}} <   1 0 0, \quad t = c _ {1 5} \alpha^ {- 1}.
$$

On aura bien, pour $z \in R$

$$
| K _ {0} (z) - 1 | \leq \frac {c _ {1 5}}{2 \alpha - c _ {9} - c _ {1 5}} \leq \frac {c _ {1 5}}{\alpha + c _ {1 5}} = \frac {t}{1 + t},
$$

donc la fonction $g$ construite au Paragraphe 4.2 appartient effectivement à $S_{-1/\alpha}$.

## 4.6 - Estimations pour l'application  $k \circ K_{0}$ .

Notons $K$ une détermination de $\frac{1}{2\pi i}\mathrm{Log}(k\circ K_0)$ dans $\mathcal{X}$. Le domaine $\mathcal{X}$ contient le domaine $\mathcal{U}_{F_0}$ de 3.2 et la restriction à $\mathcal{U}_{F_0}$ de $K$ est une application uniformisante de $F_0$, d'après les propriétés définissant $K_0$.

Ceci étant, nous procédons comme en 3.5, à partir de la proposition 2 de 3.4.

Posons

$$
t _ {1} ^ {\prime} = (c _ {7} ^ {\prime} + c _ {6} ^ {\prime}) \alpha + c _ {3},
$$

et définissons

$$
\mathcal {W} ^ {\prime} = \left\{z, | \Re z | \leq \alpha , \Im z \geq t _ {1} ^ {\prime} \right\},
$$

$$
\mathcal {W} _ {1} ^ {\prime} = \left\{z, | \Re z | \leq \alpha , \Im z \geq t _ {1} ^ {\prime} - c _ {3} \right\}.
$$

Pout $z \in \mathcal{W}'_1$, on a, dans la proposition 2 de 3.4

$$
w = \Im z - c _ {0} - c _ {3} - c _ {4} \alpha \geq 2 c _ {6} ^ {\prime} \alpha ,
$$

d'où

$$
\left| \alpha D K (z) - 1 \right| \leq \frac {4}{3} c _ {6} ^ {2} \alpha^ {2} w ^ {- 2} \leq 1 / 3.\tag{6}
$$

Comme $|F_0(z) - z - \alpha| \leq c_3$ dans $\mathcal{W}'_1$, on peut trouver un point $z_0 \in \mathcal{W}'_1 - \mathcal{W}'$, de partie réelle $-\alpha/2$, tel que le segment $[z_0, F_0(z_0)]$ soit contenu dans $\mathcal{W}'_1 - \mathcal{W}'$. Or l'image de ce segment par $k \circ K_0$ est une courbe de Jordan qui sépare 0 et $t$ dans $\mathbb{C}$, donc contient des points de module $< t$. Il existe par conséquent $z_1 = \sigma + i\tau \in \mathcal{W}'_1 - \mathcal{W}'$ tel que

$$
\Im z _ {1} \geq \frac {1}{2 \pi} \mathrm{Log} t ^ {- 1}.
$$

En intégrant alors la relation (6), on obtient, pour $z = s + it \in \mathcal{W}'$

$$
\begin{array}{r l} & {\Im (K (z)) = (\Im (K (s + i t)) - \Im (K (s + i \tau))) + \Im (K (s + i \tau))} \\ & {\qquad \geq \alpha^ {- 1} (\Im z - \tau) - \frac {2}{3} c _ {6} ^ {\prime} + \frac {1}{2 \pi} \mathrm{Log} t ^ {- 1} - \frac {2}{3}} \\ & {\qquad \geq \alpha^ {- 1} \Im z + \frac {1}{2 \pi} \mathrm{Log} \alpha - c _ {8} ^ {\prime},} \\ & {\qquad c _ {8} ^ {\prime} = \frac {5}{3} c _ {6} ^ {\prime} + c _ {7} ^ {\prime} + \frac {2}{3} + \frac {1}{2} c _ {3} + \frac {1}{2 \pi} \mathrm{Log} c _ {1 5} <   4. 7 6.} \end{array}\tag{7}
$$

## 4.7 - La propriété fondamentale de G.

On rappelle que $G$ est l'unique difféomorphisme de $\widehat{S}_{-1 / \alpha}$ qui vérifie $E(G(z)) = g(E(z))$ pour $z \in \mathbb{H}$. On a $G(K(z)) = K(z - 1)$ pour $z \in \mathcal{X}, \Re z \geq 1$.

Soient  $z_{0}$  un point de H et n un entier qui vérifient :

$$
0 \leq \Re z _ {0} <   1, \quad \Im z _ {0} > c _ {8} ^ {\prime} \alpha + 1, \quad F ^ {n} (z _ {0}) \notin \mathbb {H}.
$$

Posons $z_0' = z_0 - i \in \mathcal{W}'$, et notons $z_1$ l'unique nombre complexe qui vérifie :

$$
0 \leq \Re z _ {1} <   1, \quad E (z _ {1}) = k \circ K _ {0} (z _ {0} ^ {\prime}).
$$

## Proposition 1.—

1. Il existe un entier $m$, avec $0 < m < 2\alpha n$, tel qu'on ait $G^{m}(z_{1}) \notin \mathbb{H}$.

2. On a

$$
\Im z _ {1} \geq \alpha^ {- 1} (\Im z _ {0} - 1) + \frac {1}{2 \pi} \log \alpha - c _ {8} ^ {\prime}.
$$

Démonstration. L'estimation de $\Im z_{1}$ résulte immédiatement de la relation (7) du numéro précédent.

Démontrons la première partie de l'énoncé. Soit $p \leq n$ le plus petit entier, tel qu'on ait :

$$
\Im F ^ {p} (z _ {0}) \leq \frac {3}{2}.
$$

Pour $0 \leq j \leq p$, notons $z_{j}^{\prime}$ le point de $\mathbb{H}$ qui vérifie :

$$
0 \leq \Re z _ {j} ^ {\prime} <   1, \quad z _ {j} ^ {\prime} - (F ^ {j} (z _ {0}) - i) \in \mathbb {Z}.
$$

On a alors $F_0(z_j') = z_{j+1}' + n_j$, avec $n_j \in \mathbb{Z}$. Comme on a $\left|\Re\left(F_0(z_j') - z_j'\right) - \alpha\right| \leq c_3$, on a $|n_j - \alpha| \leq 1 + c_3$ pour $0 \leq j < p$. Par définition de $G_0$, on a :

$$
G _ {0} ^ {n _ {j}} (z _ {j} ^ {\prime}) = z _ {j + 1} ^ {\prime},
$$

d'où

$$
G _ {0} ^ {m} (z _ {0} ^ {\prime}) = z _ {p} ^ {\prime},
$$

en posant :

$$
m = \sum_ {j = 0} ^ {p - 1} n _ {j} \leq p (\alpha + 1 + c _ {3}) <   2 n \alpha .
$$

Or, $z_{p}^{\prime}$ appartient à $R$ par définition de $p$, donc on a :

$$
\left| E \left(G ^ {m} (z _ {1})\right) \right| = \left| k \circ K _ {0} (z _ {p} ^ {\prime}) \right| \geq 1,
$$

et finalement $G^{m}(z_{1}) \notin \mathbb{H}$.

Même sans se donner $z_{0}$ comme précédemment, $G$ possède des points de grande partie imaginaire (quand $\alpha$ est grand) dont l'orbite positive sort de $\mathbb{H}$. Plus précisément,

Proposition 2.—

Il existe $z_{1}$ tel que

$$
\Im z _ {1} \geq \frac {1}{2 \pi} \mathrm{Log} \alpha - \frac {1}{2 \pi} \mathrm{Log} c _ {1 5},
$$

et $0 \leq m \leq 2\alpha$ tel que $G^{m}(z_{1}) \notin \mathbb{H}$.

Démonstration. Considérons le segment  $[0, \chi(0)]$  qui est contenu dans X. Son image par  $k \circ K_{0}$  est une droite proprement plongée dans C qui sépare les points fixes 0 et t de g, donc contient des points de module < t.

Pour tout $z \in [0, \chi(0)]$, il existe $m \leq 2\alpha$ tel que $G_0^m(z) \in R$. Il existe donc $z_1$ tel que

$$
\Im z _ {1} \geq \frac {1}{2 \pi} \mathrm{Log} t ^ {- 1} = \frac {1}{2 \pi} \mathrm{Log} \alpha - \frac {1}{2 \pi} \mathrm{Log} c _ {1 5},
$$

et $0 \leq m \leq 2\alpha$ tel que $G^{m}(z_{1}) \notin \mathbb{H}$.

## 5. Construction d'exemples. Fin de la démonstration du théorème.

5.1 - Lorsque $\alpha$ est supérieur à $c_{14}$, nous avons associé, dans le paragraphe précédent, à tout difféomorphisme $F \in \hat{S}_{\alpha}$ un difféomorphisme $G \in \hat{S}_{-1/\alpha}$ dont la relation fondamentale avec $F$ est donnée par les Propositions 1 et 2 de 4.7. Nous commencerons par faire de même lorsqu'on a $2 < \alpha \leq c_{14}$

## 5.2 - Construction et propriétés de G lorsque  $2 < \alpha \leq c_{14}$ .

Soient $2 < \alpha \leq c_{14}$, et $F \in \hat{S}_{\alpha}$. On procède de façon analogue au numéro 3.5 pour construire $G$.

Choisissons une application uniformisante $K$ de $F$. Définissons $t_{1}^{\prime}, \mathcal{W}^{\prime}, \mathcal{W}_{1}^{\prime}$ comme en 4.6. L'estimation (6) de 4.6 est encore valide dans $\mathcal{W}_{1}^{\prime}$.

Posons

$$
L (z) = K (z) - i \max _ {| s | \leq \alpha} \Im (K (s + i t _ {1} ^ {\prime})), \quad z \in \mathcal {V} \cup \overline {{\mathcal {U}}} _ {F}
$$

En intégrant la relation (6) de 4.6, on obtient

$$
\Im (L (z)) \leq 0, \quad z \in \mathcal {W} _ {1} ^ {\prime} - \mathcal {W} ^ {\prime};\tag{1}
$$

et, pour $z = s + it \in \mathcal{W}'$:

$$
\begin{array}{r l} & {\Im (L (z)) = (\Im (K (s + i t)) - \Im (K (s + i t _ {1} ^ {\prime}))) + \Im (L (s + i t _ {1} ^ {\prime}))} \\ & {\qquad \geq \alpha^ {- 1} (\Im z - t _ {1} ^ {\prime}) - \frac {2}{3} c _ {6} ^ {\prime} - \frac {2}{3}} \\ & {\qquad = \alpha^ {- 1} \Im z + \frac {1}{2 \pi} \mathrm{Log} \alpha - c _ {8} ^ {\prime \prime},} \\ & {\qquad c _ {8} ^ {\prime \prime} = \frac {5}{3} c _ {6} ^ {\prime} + c _ {7} ^ {\prime} + \frac {2}{3} + \frac {1}{2} c _ {3} <   4. 0 3.} \end{array}\tag{2}
$$

Définissons dans $L(\mathcal{W}' \cap T\mathcal{W}')$ une application $G$ par

$$
G (L (z)) = L (z - 1).
$$

Proposition.—

1. L'application G se prolonge à H en un élément de  $\widehat{S}_{-1/\alpha}$ .

2. Si $z_0 \in \mathbb{H}, n \geq 1$ satisfont

$$
0 \leq \Re z _ {0} <   1, \quad \Im z _ {0} \geq c _ {8} ^ {\prime \prime} \alpha , \quad F ^ {n} (z _ {0}) \notin \mathbb {H},
$$

alors il existe un entier m, avec 0 < m < 2αn, tel que le point z₁ = L(z₀) vérifie

$$
\Im z _ {1} \geq \alpha^ {- 1} \Im z _ {0} - c _ {8} ^ {\prime \prime}, \quad G ^ {m} (z _ {1}) \notin \mathbb {H}
$$

La démonstration est complètement similaire à celle des propositions de 3.5 et 3.6: les relations (6) de 4.5 et (1),(2) de 5.2 remplacent les relations (4),(5),(6) de 3.5; l'inégalité $m < 2n\alpha$ se démontre comme dans la proposition 1 de 4.7.

## 5.3 - Construction d'exemples : le principe.

Pour $F\in \widehat{S}$ , $n\in \mathbb{Z}$ , $\varepsilon \in \{-1, + 1\}$ , on définit :

$$
\begin{array}{r l} T _ {n, \varepsilon} (F) (z) = F (z) + n, & \text {si} \quad \varepsilon = + 1, \\ = - \overline {{F (- \bar {z})}} + n, & \text {si} \quad \varepsilon = - 1. \end{array}
$$

L'application $T_{n,\varepsilon}$ envoie donc $\widehat{S}_{\alpha}$ dans $\widehat{S}_{\varepsilon \alpha + n}$.

Soit $\alpha$ un nombre réel irrationnel ; on a associé à $\alpha$, en 1.3, une suite $(\alpha_{n})_{n\geq0}$ qui vérifie :

$$
\{\alpha \} = \alpha_ {0}, 0 <   \alpha_ {n} <   1 / 2,
$$

$$
\alpha_ {n} = \left(a _ {n + 1} + \varepsilon_ {n + 1} \alpha_ {n + 1}\right) ^ {- 1}, \quad a _ {n + 1} \in \mathbb {N} ^ {*}, \quad \varepsilon_ {n + 1} = \pm 1.
$$

Dans un premier temps, nous fixons un entier $n \geq 0$ et construisons, pour $0 \leq \ell \leq n + 1$, un difféomorphisme $F_{n,\ell}$ qui appartient à $\widehat{S}_{\alpha_\ell}$:

1. On définit $F_{n,n+1}(z) = z + \alpha_{n+1}$

2. Supposons qu'on ait déjà construit $F_{n,\ell+1} \in \widehat{S}_{\alpha_{\ell+1}}$; on pose $\widetilde{F}_{n,\ell+1} = T_{a_{\ell+1},\varepsilon_{\ell+1}}(F_{n,\ell+1})$; c'est un élément de $\widehat{S}_{\alpha_{\ell}^{-1}}$. On lui associe, de la façon indiquée au Paragraphe 5.2 pour $\alpha_{\ell} \geq c_{14}^{-1}$, et de la façon indiquée au Paragraphe 4 pour $\alpha_{\ell} < c_{14}^{-1}$, un difféomorphisme $G_{n,\ell} \in \widehat{S}_{-\alpha_{\ell}}$; on pose finalement $F_{n,\ell} = T_{0,-1}(G_{n,\ell}) \in \widehat{S}_{\alpha_{\ell}}$.

3. En écrivant $\alpha = a_0 + \varepsilon_0\alpha_0$, $a_0 \in \mathbb{Z}$, $\varepsilon_0 \in \{-1, +1\}$, on définit $F_n = T_{a_0,\varepsilon_0}(F_{n,0}) \in \widehat{S}_{\alpha}$

Dans la construction de $G_{n,\ell}$ à partir de $\widetilde{F}_{n,\ell+1}$ intervient, lorsque $\alpha_{\ell} < c_{14}^{-1}$ un difféomorphisme auxiliaire $J_{n,\ell}$ du type spécifié au Paragraphe 4.1.

En fait, pour que $F_n$ ait des propriétés intéressantes, on imposera à l'entier $n$ d'appartenir à l'ensemble $\mathcal{I}(\alpha)$ défini en 1.6 avec une valeur appropriée de $B$. Lorsque cet ensemble est infini (ce qui est toujours le cas lorsque $\alpha$ n'est pas un nombre de Bruno) nous nous intéresserons aux valeurs d'adhérence de la suite $(F_n)_{n \in \mathcal{I}}$.

## 5.4 - Fin de la démonstration du théorème.

Nous distinguons plusieurs cas.

## 5.4.1 - L'ensemble $\mathcal{I}(\alpha)$ est vide.

D'après le lemme 1.6, on a alors :

$$
\Phi (\alpha) \leq 4 B,
$$

donc on obtient trivialement :

$$
\sup _ {F \in \widehat {S} _ {\alpha}} d _ {F} \geq \frac {1}{2 \pi} \Phi (\alpha) - \frac {2 B}{\pi},
$$

ce qui termine dans ce cas la démonstration du théorème (cf. 2.8).

## 5.4.2 - L'ensemble $\mathcal{I}(\alpha)$ est non vide mais fini.

Notons $n$ son plus grand élément, et construisons des difféomorphismes $F_{n,\ell} \in \widehat{S}_{\alpha_\ell}$, pour $0 \leq \ell \leq n + 1$, comme au numéro 5.3.

Considérons d'autre part la suite $(B_{n,\ell})_{0\leq \ell \leq n}$ définie en 1.6 par

$$
\begin{array}{c} {B _ {n, n + 1} = 0,} \\ {B _ {n, \ell} = \alpha_ {\ell} B _ {n, \ell + 1} + \mathrm{Log} \alpha_ {\ell} ^ {- 1} - B.} \end{array}
$$

D'après la définition de $\mathcal{I}(\alpha)$ et le lemme 1.6, on a :

$$
\begin{array}{l} B _ {n, \ell} \geq 0, \quad \text { pour } 0 \leq \ell \leq n, \\ \Phi (\alpha) \leq 4 B + B _ {n, 0}. \end{array}
$$

Lemme.— Supposons

$$
B \geq c _ {1 6} = 2 \pi (c _ {8} ^ {\prime} + c _ {1 4} ^ {- 1}) + \log c _ {1 4}, \quad c _ {1 6} <   3 4. 5 9.
$$

Pour $0 \leq \ell \leq n$, il existe $z_{\ell} \in \mathbb{H}$ et $m_{\ell} \in \mathbb{N}^{*}$ tells qu'on ait $F_{n,\ell}^{m_{\ell}}(z_{\ell}) \notin \mathbb{H}$ et:

$$
\Im z _ {\ell} \geq \frac {1}{2 \pi} B _ {n, \ell}.
$$

Démonstration. Elle se fait par récurrence descendante sur $\ell$.

Pour $\ell = n$, on a $B_{n,n} = \operatorname{Log}\alpha_n^{-1} - B \geq 0$, donc $\alpha_n < c_{14}^{-1}$ et l'assertion du lemme résulte de la Proposition 2 de 4.7 puisque $B > \log c_{15}$.

Supposons l'assertion vérifiée pour $F_{n,\ell+1}$.

Si $\alpha_{\ell} < c_{14}^{-1}$ et $B_{n,\ell+1} > 2\pi(c_8' \alpha_\ell^{-1} + 1)$, on applique la proposition 1 de 4.7 à $z_{\ell+1}$. Le point $z_{\ell}$ donné par cette proposition vérifie

$$
\begin{array}{r l} & {\Im z _ {\ell} \geq \alpha_ {\ell} (\Im z _ {\ell + 1} - 1) + \frac {1}{2 \pi} \log \alpha_ {\ell} ^ {- 1} - c _ {8} ^ {\prime}} \\ & {\quad \geq \frac {1}{2 \pi} \alpha_ {\ell} B _ {n, \ell + 1} + \frac {1}{2 \pi} \log \alpha_ {\ell} ^ {- 1} - c _ {8} ^ {\prime} - c _ {1 4} ^ {- 1}} \\ & {\quad \geq \frac {1}{2 \pi} \alpha_ {\ell} B _ {n, \ell},} \end{array}
$$

d'après le choix de B.

Si $\alpha_{\ell} < c_{14}^{-1}$ et $B_{n,\ell + 1} \leq 2\pi(c_8'\alpha_\ell^{-1} + 1)$, on applique la proposition 2 de 4.7. Le point $z_{\ell}$ donné par cette proposition vérifie

$$
\begin{array}{r l} & {\Im z _ {\ell} \geq \frac {1}{2 \pi} \log \alpha_ {\ell} ^ {- 1} - \frac {1}{2 \pi} \log c _ {1 5}} \\ & {\quad \geq (\frac {1}{2 \pi} \alpha_ {\ell} B _ {n, \ell + 1} - c _ {8} ^ {\prime} - \alpha_ {\ell}) + \frac {1}{2 \pi} \log \alpha_ {\ell} ^ {- 1} - \frac {1}{2 \pi} \log c _ {1 5}} \\ & {\quad \geq \frac {1}{2 \pi} \alpha_ {\ell} B _ {n, \ell},} \end{array}
$$

d'après le choix de B.

Si $\alpha_{\ell} \geq c_{14}^{-1}$, on applique la proposition de 5.2 à $z_{\ell+1}$. On a en effet

$$
\Im z _ {\ell + 1} \geq \frac {1}{2 \pi} B _ {n, \ell + 1} \geq \frac {\alpha_ {\ell} ^ {- 1}}{2 \pi} (B - \log \alpha_ {\ell} ^ {- 1}) > c _ {8} ^ {\prime \prime} \alpha_ {\ell} ^ {- 1},
$$

d'après le choix de $B$. Le point $z_{\ell}$ donné par cette proposition vérifie

$$
\begin{array}{r l} & {\Im z _ {\ell} \geq \alpha_ {\ell} \Im z _ {\ell + 1} - c _ {8} ^ {\prime \prime}} \\ & {\quad \geq \frac {1}{2 \pi} \alpha_ {\ell} B _ {n, \ell + 1} + (\frac {1}{2 \pi} \log \alpha_ {\ell} ^ {- 1} - \frac {1}{2 \pi} \log c _ {1 4}) - c _ {8} ^ {\prime \prime}} \\ & {\quad \geq \frac {1}{2 \pi} \alpha_ {\ell} B _ {n, \ell},} \end{array}
$$

d'après le choix de B.

L'assertion du lemme, pour $\ell=0$, montre qu'on a :

$$
d _ {F _ {n}} \geq \frac {1}{2 \pi} B _ {n, 0} \geq \frac {1}{2 \pi} \Phi (\alpha) - \frac {2 B}{\pi},
$$

d'où la conclusion du théorème dans ce cas (cf. 2.8).

## 5.4.3 - L'ensemble $\mathcal{I}(\alpha)$ est infini.

Pour $n \in \mathcal{I} = \mathcal{I}(\alpha)$, et $0 \leq \ell \leq n + 1$, construisons des difféomorphismes $F_{n,\ell} \in \widehat{S}_{\alpha_\ell}$.

Lemme.— Pour tous entiers  $0 \leq \ell \leq n' \leq n$ , avec  $n', n \in I$ , il existe

$$
z = z (\ell , n ^ {\prime}, n) \in \mathbb {H}, \quad m = m (\ell , n ^ {\prime}, n) \in \mathbb {N} ^ {*}
$$

vérifiant :

(i)  $m(n', n', n) < 2\alpha_{n'}^{-1}$ ;

(ii) $m(\ell, n', n) < 2\alpha_{\ell}^{-1} m(\ell + 1, n', n)$, pour $0 \leq \ell < n'$;

(iii) $F_{n,\ell}^{m}(z)\notin \mathbb{H}$

(iv) $0 \leq \Re z < 1$, $\Im z \geq \frac{1}{2\pi} B_{n',\ell}$.

Démonstration. Elle est en tous points similaire à celle du Lemme 5.4.2, les assertions sur les entiers m résultant des propositions 1 et 2 de 4.7 et de la Proposition 5.2.

Prenons $\ell = 0$ et fixons $n' \in \mathcal{I}$. La suite $m(0, n', n)$ est alors bornée (lorsque $n \in \mathcal{I}$ tend vers l'infini), et il en est donc de même de la suite $z(0, n', n)$ (d'après les propriétés (iii) et (iv) du lemme). On peut donc extraire de la suite $(F_n)_{n \in \mathcal{I}}$ une sous-suite convergeant vers une limite $F \in \widehat{S}_{\alpha}$ qui possède la propriété suivante : pour tout $n' \in \mathcal{I}$, il existe $z \in \mathbb{H}$ et $m \in \mathbb{N}^*$ tels qu'on ait $F^m(z) \notin \mathbb{H}$ et $\Im z \geq \frac{1}{2\pi} B_{n', 0}$. Or, d'après le lemme 1.6, on a :

$$
B _ {n ^ {\prime}, 0} > \sum_ {j = 0} ^ {n ^ {\prime}} \beta_ {j - 1} \mathrm{Log} \alpha_ {j} ^ {- 1} - 2 B.
$$

En laissant maintenant tendre $n'$ vers l'infini, on conclut qu'on a :

\- Si $\alpha \notin \mathcal{B}$, $d_F = +\infty$;

\- Si $\alpha \in \mathcal{B}$, $d_F \geq \frac{1}{2\pi} \Phi(\alpha) - \frac{B}{\pi}$.

Ceci conclut (cf. 2.8) la démonstration du théorème. On obtient

$$
\operatorname{Log} R (\alpha) \leq \operatorname{Log} 4 - 2 \pi d _ {F} \leq - \Phi (\alpha) + 4 B + \operatorname{Log} 4,
$$

$$
4 B + \mathrm{Log} 4 <   1 3 9. 7 5
$$

## 6. Orbites périodiques s'accumulant sur l'origine.

6.1 -

Soit $\alpha$ un nombre réel irrationnel qui n'appartient pas à $\mathcal{B}$. Nous avons construit aux Paragraphs 5.3 et 5.4 des difféomorphismes $F \in \widehat{S}_{\alpha}$ qui ne sont pas linéarisables (plus exactement, tels que $\pi(F)$ ne possède pas de disque de Siegel à l'origine).

Nous étudions dans ce paragraphe quelques propriétés supplémentaires de ces exemples : nous montrons que $\pi(F)$ possède une suite d'orbites périodiques s'accumulant sur l'origine, et dont la distance à l'origine est essentiellement la plus petite possible, compte tenu de la période de ces orbites.

6.2 -

Soient $\alpha > 2$ et $F \in \hat{S}_{\alpha}$; désignons par $\mathcal{D}$ le domaine :

$$
\mathcal {D} = \left\{z \in \mathbb {H}, \quad | \Re z | \leq \alpha , \Im z \geq \frac {B}{2 \pi} \alpha \right\},
$$

où $B$ est défini en 5.4.2. Au numéro 5.2 (pour $\alpha \leq c_{14}$) et au Paragraphe 4 (pour $\alpha > c_{14}$) nous avons construit un difféomorphisme $G \in \widehat{S}_{-1/\alpha}$; soit $L$ l'application qui est celle considérée en 5.2 pour $\alpha \leq c_{14}$ et est définie pour $\alpha > c_{14}$ par $L(z) = K(z - i)$, où $K$ est définie en 4.6. Dans tous les cas, elle est holomorphe et injective dans $\mathcal{D}$ et on a les propriétés suivantes :

$$
L (F (z)) = L (z) + 1, \quad z \in \mathcal {D} \cap F ^ {- 1} \mathcal {D}
$$

$$
G (L (z)) = L (z - 1), \quad z \in \mathcal {D} \cap T \mathcal {D}
$$

$$
\Im L (z) \geq \alpha^ {- 1} \Im z + \frac {1}{2 \pi} \mathrm{Log} \alpha - \frac {B}{2 \pi}, \quad z \in \mathcal {D}.
$$

Lorsqu'on a $\alpha > c_{14}$, le difféomorphisme $G$ a quelques propriétés supplémentaires : le point $w = \frac{i}{2\pi} \mathrm{Log} c_{15}^{-1} \alpha$ est fixé par $G$; de plus, la seule restriction qui soit imposée à la classe de conjugaison de $G$ dans le groupe des germes de difféomorphismes de $(\mathbb{C}, w)$ est que $DG(w)$ s'écrive sous la forme $E(1/\alpha')$, avec $|\alpha - \alpha'| \leq c_9$.

Soit $z$ un point de $\mathbb{H}$. Supposons qu'il existe deux entiers $q, p \geq 1$ tels qu'on ait :

$$
F ^ {q} (z) = z + p,
$$

$$
\Im F ^ {j} (z) \geq \frac {B}{2 \pi} \alpha \quad \text { pour } \quad 0 \leq j <   q
$$

Définissons des points  $z_{j}$ ,  $0 \leq j \leq q$ , par les conditions :

$$
0 \leq \Re z _ {j} <   1, F ^ {j} (z) - z _ {j} \in \mathbb {Z},
$$

et posons $z' = L(z_0)$.

Lemme.— On a  $G^{p}(z') = z' - q$ , et :

$$
\underset {0 \leq j <   p} {\text {Min}} \Im G ^ {j} (z ^ {\prime}) \geq \alpha^ {- 1} \left(\underset {0 \leq j <   q} {\text {Min}} \Im F ^ {j} (z)\right) + \frac {1}{2 \pi} \mathrm{Log} \alpha - \frac {B}{2 \pi}.
$$

Démonstration. On définit des entiers strictement positifs $n_{1},\ldots,n_{q}$ par les relations :

$$
F (z _ {j}) = z _ {j + 1} + n _ {j + 1}, \quad 0 \leq j \leq q - 1
$$

Pour $0 \leq s \leq q$, posons $m_s = \sum_{r=1}^{s} n_j$; on a $m_0 = 0$ et $m_q = p$; définissons inductivement des points $y_j$ pour $0 \leq j \leq p$, par les formules:

$$
y _ {0} = z _ {0};
$$

$$
y _ {m _ {s} + 1} = F (y _ {m _ {s}}) - 1, \quad 0 \leq s <   q;
$$

$$
y _ {j + 1} = y _ {j} - 1, \quad \text { si } \quad j \neq m _ {s}, \forall s.
$$

Posons $z_j' = L(y_j)$; on a alors :

$$
z _ {j + 1} ^ {\prime} = G (z _ {j}) + 1, \quad \text { pour } \quad j = m _ {s}, 0 \leq s <   q,
$$

$$
z _ {j + 1} ^ {\prime} = G (z _ {j}) \quad \text {   sinon   }.
$$

On a donc bien $G^p(z_0') = z_0' - q$, et la seconde partie de la conclusion du lemme résulte immédiatement des propriétés de $L$ rappelées ci-dessus.

6.3 -

Soit $\alpha$ un nombre réel irrationnel qui n'appartient pas à $\mathcal{B}$.

Rappelons (cf.1.6) que l'on désigne par $\mathcal{J}(\alpha)$ l'ensemble des entiers $n$ qui vérifient $B_{n,\ell} \geq B\alpha_{\ell-1}^{-1}$, pour $0 < \ell \leq n$. L'ensemble $\mathcal{J}(\alpha)$ est infini d'après le lemme 1.6.

Nous reprenons les constructions des Paragraphs 5.3 et 5.4 : nous construisons, pour $n \in \mathcal{J}(\alpha)$ et $0 \leq \ell \leq n+1$, des difféomorphismes $F_{n,\ell}, \tilde{F}_{n,\ell}, G_{n,\ell}$, puis des difféomorphismes $F_n$ et finalement un difféomorphisme $F$.

Fixons momentanément deux entiers $n \geq m$ dans $\mathcal{J}(\alpha)$. Nous allons montrer qu'il existe, pour $0 \leq \ell \leq m$, un point $z = z(n, m, \ell)$ et des entiers $p = p(m, \ell)$, $q = q(m, \ell)$ satisfaisant aux propriétés suivantes :

(i) $F_{n,\ell}^{q}(z) = z + p$

(ii) $\Im F_{n,\ell}^{j}(z)\geq \frac{1}{2\pi} B_{m,\ell}$, pour $0\leq j < q$ .

Pour $\ell = m$, nous prenons $p = 0$, $q = 1$ et $z = \frac{i}{2\pi}\mathrm{Log}(c_{15}^{-1}\alpha_m^{-1})$; les propriétés (i) et (ii) sont vérifiées car $B_{m,m} = \mathrm{Log}\alpha_m^{-1} - B$.

Supposons, par induction descendante sur $\ell$, les propriétés vérifiées avec $z \in \mathbb{H}$, $q \geq 1$, $p \geq 0$. On a $\tilde{F}_{n,\ell+1} = T_{a_{\ell+1},\varepsilon_{\ell+1}}(F_{n,\ell+1})$ (cf. 5.3). En posant $\tilde{p} = a_{\ell+1}q + \varepsilon_{\ell+1}p$ et $\tilde{z} = z$ si $\varepsilon_{\ell+1} = +1$, $\tilde{z} = -\bar{z}$ si $\varepsilon_{\ell+1} = -1$, on a donc:

$$
\tilde {F} _ {n, \ell + 1} ^ {q} (\tilde {z}) = \tilde {z} + \tilde {p}.
$$

Comme $m \in \mathcal{J}(\alpha)$, on a $B_{m,\ell+1} \geq B\alpha_{\ell}^{-1}$; d'autre part on a:

$$
\Im \tilde {F} _ {n, \ell + 1} ^ {j} (\tilde {z}) \geq \frac {1}{2 \pi} B _ {m, \ell + 1} \geq \frac {B}{2 \pi} \alpha_ {\ell} ^ {- 1}
$$

pour $0 \leq j < q$, d'après l'hypothèse de récurrence.

Les hypothèses du Lemme 6.2 sont donc vérifiées et il existe un point $z' \in \mathbb{H}$ tel qu'on ait :

$$
G _ {n, \ell} ^ {\tilde {p}} (z ^ {\prime}) = z ^ {\prime} - q,
$$

$$
\Im G _ {n, \ell} ^ {j} (z ^ {\prime}) \geq \frac {1}{2 \pi} B _ {m, \ell}, \quad \text { pour } \quad 0 \leq j <   \tilde {p}.
$$

On pose finalement $z(n,m,\ell) = -\bar{z}'$, $p(m,\ell) = q(m,\ell + 1)$ et $q(m,\ell) = \tilde{p} = a_{\ell + 1}q(m,\ell + 1) + \varepsilon_{\ell + 1}p(m,\ell + 1)$ pour satisfaire aux propriétés (i), (ii) à l'ordre $\ell$.

En prenant $\ell=0$, on obtient la conclusion suivante: il existe un point $z(n,m)$ et des entiers $p(m)\in\mathbb{Z}$, $q(m)\geq1$ tels qu'on ait:

(i) $0 \leq \Re z(n, m) < 1$;

(ii) $\Im F_n^j (z(n,m))\geq \frac{1}{2\pi} B_{m,0}$ , pour $0\leq j <   q(m)$

(iii) $F_{n}^{q(m)}(z(n,m)) = z(n,m) + p(m)$.

D'autre part, à partir des relations liant $p(m,\ell)$, $q(m,\ell)$ à $p(m,\ell+1)$, $q(m,\ell+1)$, il est facile de voir qu'on a $p(m)=p_{k(m)}$, $q(m)=q_{k(m)}$ où $(p_{r}/q_{r})$ est la suite des réduites de $\alpha$ et la fonction $k:\mathbb{N}\to\mathbb{N}$ est définie en 1.4.

Soit $F$ une valeur d'adhérence de la suite $(F_{n})_{n\in\mathcal{J}}$; la condition (iii) montre que $\Im(z(n,m))$ est majoré par une constante ne dépendant que de $m$; en extrayant des sous-suites, et en utilisant l'estimation pour $B_{m,0}$ donnée en 1.6, on aboutit à la conclusion suivante:

Proposition.— Pour tout  $m \in \mathcal{J}(\alpha)$ , il existe un point  $z_{m}$  possédant les propriétés suivantes :

$$
F ^ {q _ {k (m)}} \left(z _ {m}\right) = z _ {m} + p _ {k (m)},
$$

$$
\Im F ^ {j} (z _ {m}) \geq \frac {1}{2 \pi} \sum_ {j = 0} ^ {m} \beta_ {j - 1} \mathrm{Log} \alpha_ {j} ^ {- 1} - \frac {B}{\pi},
$$

pour $0 \leq j < q_{k(m)}$.

6.4 - Comme on l'a rappelé en 6.2, on peut dans la construction précédente spécifier arbitrairement la classe de conjugaison du germe de $F^{q_k(m)}(z) - p_{k(m)}$ au voisinage de son point fixe $z_m$; la seule restriction est que $DF^{q_k(m)}(z_m)$ s'écrive sous la forme $E(\varepsilon(m)\alpha_m')$, où $\varepsilon(m) \in \{-1, +1\}$ ne dépend que de $\varepsilon_1, \ldots, \varepsilon_m$ et $\alpha_m' \in \mathbb{C}$ doit vérifier :

$$
\left| \alpha_ {m} ^ {\prime - 1} - \alpha_ {m} ^ {- 1} \right| \leq c _ {9}.
$$

Une conséquence, peut-être inattendue, de cette latitude est le résultat suivant ; notons G le groupe des germes de difféomorphismes holomorphes de  $(\mathbb{C},0)$ ; pour  $\alpha\in R$ , notons  $G_{\alpha}$  la partie de G constituée des germes g tels que  $Dg(0)=E(\alpha)$ .

Théorème.— Soit $\alpha$ un nombre réel irrationnel qui n'appartient pas à $\mathcal{B}$. Il existe alors un ensemble ayant la puissance du continu de classes de conjugaison de $G$, contenues dans $G_{\alpha}$, et ne contenant aucune fonction entière.

Démonstration. Considérons une partition :

$$
\mathcal {J} (\alpha) = \mathcal {J} = \mathcal {J} _ {1} \cup \mathcal {J} _ {2}
$$

en deux parties infinies $\mathcal{J}_{1},\mathcal{J}_{2}$. Choissons, pour tout $m\in\mathcal{J}_{2}$, un rationnel $\alpha_{m}^{\prime}$ tel que

$\left|\alpha_{m}^{\prime -1} - \alpha_{m}^{-1}\right| \leq c_{9}$ et notons $r_m$ son dénominateur. Définissons, d'autre part, pour $\theta \in \mathbb{D}$ et $m \in \mathcal{J}_1$, un nombre complexe $\alpha_{m}^{\prime} = \alpha_{m}(\theta)$ par la relation $\alpha_{m}^{\prime -1} - \alpha_{m}^{-1} = c_{9}\theta$

On peut alors construire un germe de difféomorphisme holomorphe $f_{\theta}$ et une suite $(z_m)_{m \in \mathcal{J}}$ tels qu'on ait $Df_{\theta}(0) = E(\alpha)$ et :

$$
\mathrm{(i)} f _ {\theta} ^ {q _ {k (m)}} (z _ {m}) = z _ {m}, D f _ {\theta} ^ {q _ {k (m)}} (z _ {m}) = E (\varepsilon (m) \alpha_ {m} ^ {\prime}), \quad m \in \mathcal {J};
$$

(ii) $f_{\theta}^{r_m q_k(m)}$ coïncide avec l'identité au voisinage de $z_m$, pour tout $m \in \mathcal{J}_2$;

$$
\text {(iii)} \lim _ {m \rightarrow + \infty} \left(\underset {0 \leq j <   q _ {k (m)}} {\operatorname{Max}} | f _ {\theta} ^ {j} (z _ {m}) |\right) = 0.
$$

La propriété (ii) garantit que la classe de conjugaison de $f_{\theta}$ dans $G$ ne contient pas de fonction entière : une telle fonction $g$ vérifierait, pour $m \in \mathcal{J}_{2}$ assez grand, l'identité $g^{r_{m}q_{k(m)}} \equiv id$, en contradiction avec $Dg(0) = E(\alpha)$.

Pour $f \in G$, notons $\Lambda(f)$ l'ensemble des nombres complexes $t$ qui possèdent la propriété suivante : pour tout $\varepsilon > 0$, il existe $m \in \mathcal{J}_1$ et $z_m \in \mathbb{C}$ tels qu'on ait $f^{q_{k(m)}}(z_m) = z_m$, $|f^j(z_m)| < \varepsilon$ pour $0 \leq j < q_{k(m)}$ et $Df^{q_{k(m)}}(z_m) = E(\varepsilon(m)\alpha_m'(t))$ (avec $\alpha'_m(t) - \alpha_m^{-1} = c_9t$).

L'ensemble $\Lambda(f)$ est au plus dénombrable, et ne dépend que de la classe de conjugaison de $f$ dans $G$. Or on a, par construction, $\theta \in \Lambda(f_{\theta})$ pour tout $\theta \in \mathbb{D}$. L'ensemble des classes de conjugaison des $f_{\theta}$, $\theta \in \mathbb{D}$ ne peut donc être au plus dénombrable.

## 6.5 -

Nous montrons maintenant que la proposition du numéro 6.3 est essentiellement optimale : la distance à l'origine des orbites périodiques y est, à un facteur multiplicatif près, la plus petite possible.

Rappelons la situation considérée au numero 3.5. Soient $\alpha\in(0,1/2)$, $F\in\hat{S}_{\alpha}$, et $\mathcal{W}$ le domaine :

$$
\mathcal {W} = \left\{z, 0 \leq \Re z \leq 1, \Im z \geq \frac {1}{2 \pi} \mathrm{Log} \alpha^ {- 1} + c _ {3} + c _ {6} + c _ {7} \right\}.
$$

On a construit un difféomorphisme $G \in \widehat{S}_{-1/\alpha}$ et une application $L$ holomorphe et injective dans $\mathcal{W} \cup T^{-1}\mathcal{W}$ qui vérifient les propriétés suivantes :

$$
G (L (z)) = L (z - 1), \quad z \in \mathcal {W}
$$

$$
\Im L (z) \geq \alpha^ {- 1} \left(\Im z - \frac {1}{2 \pi} \mathrm{Log} \alpha^ {- 1} - c _ {8}\right), \quad z \in \mathcal {W}.
$$

Soit $z$ un point de $\mathbb{H}$; nous supposons qu'il existe deux entiers $p, q \geq 1$ tels qu'on ait :

$$
F ^ {q} (z) = z + p
$$

$$
\Im F ^ {j} (z) \geq \frac {1}{2 \pi} \mathrm{Log} \alpha^ {- 1} + c _ {8}, \quad \text { pour } \quad 0 \leq j <   q.
$$

Définissons des points $z_{i}$, $0 \leq i \leq q$, par les relations :

$$
0 \leq \Re z _ {i} <   1, \quad F ^ {i} (z) - z _ {i} \in \mathbb {Z}.
$$

Lemme.— Le point  $z' = L(z_{0})$  vérifie :

$$
G ^ {p} (z ^ {\prime}) = z ^ {\prime} - q,
$$

$$
\underset {0 \leq j <   p} {\text {Min}} \Im (G ^ {j} (z ^ {\prime})) \geq \alpha^ {- 1} \left[ \underset {0 \leq j <   q} {\text {Min}} \Im F ^ {j} (z) - \left(\frac {1}{2 \pi} \mathrm{Log} \alpha^ {- 1} + c _ {8}\right) \right].
$$

Démonstration. Posons $z_i' = L(z_i)$. Pour $0 \leq i < q$, on a soit $F(z_i) = z_{i+1}$, et alors $z_{i+1}' = z_i' + 1$, soit $F(z_i) = z_{i+1} + 1$, et alors $z_{i+1}' = G(z_i') + 1$; de plus, le deuxième terme de l'alternative se produit exactement $p$ fois. On a donc $G^p(z_0') = z_0' - q$, et la deuxième assertion du lemme résulte immédiatement des propriétés de $L$.

6.6 -

Soient $\alpha$ un nombre réel irrationnel qui n'appartient pas à $\mathcal{B}$, et $F \in \hat{S}_{\alpha}$.

Proposition.— Soient  $z \in H$ ,  $m \in N$ ,  $p \in Z$ ,  $q \in N^{*}$ ; supposons qu'on ait :

$$
F ^ {q} (z) = z + p,
$$

$$
\Im F ^ {j} (z) \geq \frac {1}{2 \pi} \sum_ {\ell = 0} ^ {m - 1} \beta_ {\ell - 1} \mathrm{Log} \alpha_ {\ell} ^ {- 1} + 2 c _ {8}, \quad p o u r \quad 0 \leq j <   q.
$$

Alors, on a $q \geq q_{k(m)}$, $|p| \geq |p_{k(m)}|$; de plus, si p est non nul on a $q = q_{k(m)}$ si et seulement si $p = p_{k(m)}$; dans ce cas on a

$$
\alpha_ {m} \leq c _ {1 7} = c _ {3} \exp - 2 \pi (2 c _ {8} - \frac {1}{2}) (c _ {1 7} <   1 0 ^ {- 1 3}).
$$

L'inégalité $\alpha_{m} \leq c_{17}$ exprime que la réduite $p_{k(m)} / q_{k(m)}$ de $\alpha$ en est une bonne approximation.

Démonstration. Raisonnons par récurrence sur m.

On a $q_{k(0)} = 1$, et $\left|p_{k(0)} - \alpha\right| = \alpha_0 < 1/2$; d'autre part, on a $\Im F^j(z) \geq 2c_8$ pour $0 \leq j < q$, donc $\left|F^{j+1}(z) - F^j(z) - \alpha\right| \leq c_{17}$; on en déduit qu'on a $\left|p\right| \geq \left|p_{k(0)}\right|$ et, si $q = 1$, qu'on a $p = p_{k(0)}$ et $\left|p - \alpha\right| \leq c_{17}$, d'où les conclusions de la proposition dans ce cas.

Suppposons l'assertion de la proposition vraie à l'ordre $m-1$, et démontrons-la à l'ordre $m$. Il suffit de le faire lorsque $\alpha\in(0,1/2)$. En appliquant alors le lemme 6.5, on obtient un difféomorphisme $G\in\hat{S}_{-1/\alpha}$ et un point $z'\in\mathbb{H}$ qui vérifient

$$
G ^ {p} (z ^ {\prime}) = z ^ {\prime} - q
$$

$$
\begin{array}{r l} & {\Im G ^ {j} (z ^ {\prime}) \geq \frac {1}{2 \pi} \alpha^ {- 1} \sum_ {\ell = 1} ^ {m - 1} \beta_ {\ell - 1} \mathrm{Log} \alpha_ {\ell} ^ {- 1} + \alpha^ {- 1} c _ {8}} \\ & {\qquad \geq \frac {1}{2 \pi} \alpha^ {- 1} \sum_ {\ell = 1} ^ {m - 1} \beta_ {\ell - 1} \mathrm{Log} \alpha_ {\ell} ^ {- 1} + 2 c _ {8}} \end{array}
$$

Or, en notant $\hat{\beta}_{\ell},\hat{\alpha}_{\ell}\ldots$ les quantités $\beta_{\ell},\alpha_{\ell}\ldots$ associées à $-1 / \alpha$, on a :

$$
\hat {\alpha} _ {\ell} = \alpha_ {\ell + 1}, \hat {\beta} _ {\ell} = \alpha^ {- 1} \beta_ {\ell + 1},
$$

$$
\hat {p} _ {k (m - 1)} = - q _ {k (m)}, \hat {q} _ {k (m - 1)} = p _ {k (m)}.
$$

Les hypothèses de la proposition sont donc vérifiées par $G$ et $z'$ à l'ordre $m - 1$. Mais les conclusions, pour $G$ et $z'$ à l'ordre $m - 1$, ne sont autres que les conclusions désirées pour $F$ et $z$ à l'ordre $m$. Ceci conclut la démonstration de la proposition.

The Ground Truth image displays a single, solid horizontal line. According to Rule 2 (UNDERSCORE & LINE RULES), this is a stylistic or background line, not a placeholder underscore. Therefore, the OCR result must ignore it. The provided OCR content is "\_\_\_\_", which consists of four underscores. This is an incorrect interpretation of the line as a placeholder and violates the rule that stylistic lines must be ignored. The OCR has hallucinated text (underscores) where none should exist in the GT. This adheres to the strict requirement to ignore such lines.

# Chapitre II LINÉARISATION DES POLYNÔMES QUADRATIQUES

## 1 - Universalité des polynômes quadratiques.

1.1 - Pour $\lambda \in \mathbb{C}^*$, nous désignerons par $P_{\lambda}$ le polynôme quadratique :

$$
P _ {\lambda} (z) = \lambda (z - z ^ {2})
$$

Le polynôme  $P_{\lambda}$  admet donc en 0 un point fixe de multiplicateur  $\lambda$ . Réciproquement, tout polynôme de degré 2 dont un point fixe a  $\lambda$  pour multiplicateur est conjugué par une application affine à  $P_{\lambda}$ .

Le point critique de $P_{\lambda}$ est $c=1/2$, et la valeur critique est $\lambda/4$.

## 1.2 - La conjugaison formelle $H_{\lambda}$

Supposons que $\lambda\in\mathbb{C}^{*}$ ne soit pas racine de l'unité. Nous noterons alors $H_{\lambda}$ l'unique série formelle qui vérifie $H_{\lambda}(0)=0$, $DH_{\lambda}(0)=1$ et :

$$
H _ {\lambda} (\lambda z) = P _ {\lambda} (H _ {\lambda} (z)).
$$

Ecrivons $H_{\lambda}$ sous la forme :

$$
H _ {\lambda} (z) = z K _ {\lambda} (z) = z \sum_ {n \geq 0} H _ {n} (\lambda) z ^ {n},
$$

avec $H_0(\lambda) = 1$. On a :

$$
\lambda z K _ {\lambda} (\lambda z) = \lambda z K _ {\lambda} (z) - \lambda z ^ {2} K _ {\lambda} ^ {2} (z),
$$

d'où $zK_{\lambda}^{2}(z) = K_{\lambda}(z) - K_{\lambda}(\lambda z)$.

On en déduit la relation de récurrence satisfaite par les  $H_{n}(\lambda)$ , pour  $n \geq 1$ :

$$
H _ {n} (\lambda) = (1 - \lambda^ {n}) ^ {- 1} \sum_ {i + j = n - 1} H _ {i} (\lambda) H _ {j} (\lambda).
$$

On notera $R_{2}(\lambda)$ le rayon de convergence de $H_{\lambda}$.

## 1.3 - Propriétés élémentaires des conjugaisons $H_{\lambda}$.

## 1.3.1 - Supposons tout d'abord que $|\lambda|$ soit strictement supérieur à 1.

Proposition.— La conjugaison  $H_{\lambda}$  est une fonction entière de type  $\gamma = \frac{\operatorname{Log2}}{\operatorname{Log}|\lambda|}$ .

Démonstration. Que les applications linéarisantes des points fixes (ou périodiques) répulsifs de fonctions entières soient elles-mêmes entières est un fait bien connu ; il suffit par exemple de remarquer que d'après Poincaré ([Po]) le rayon de convergence de ces applications n'est pas nul, et que l'équation de conjugaison permet alors de les prolonger analytiquement au plan tout entier.

Démontrons que $H_{\lambda}$ est de type $\gamma$. L'équation :

$$
H _ {\lambda} (\lambda z) = P _ {\lambda} (H _ {\lambda} (z)),
$$

est valide pour tout $z\in\mathbb{C}$. Définissons deux suites $(m_{n})_{n\geq0}$ et $(M_{n})_{n\geq0}$ par :

$$
m _ {0} = M _ {0} = 2, \quad m _ {n + 1} = \frac {1}{2} | \lambda | m _ {n} ^ {2}, \quad M _ {n + 1} = \frac {3}{2} | \lambda | M _ {n} ^ {2}.
$$

Soit $r_0$ l'unique réel tel que le module maximal de $H_\lambda$ sur le disque $\{z, |z| \leq r_0\}$ soit exactement 2. Une récurrence immédiate montre que pour $n \geq 0$ le module maximal de $H_\lambda$ sur le disque $\{z, |z| \leq |\lambda|^n r_0\}$ est compris entre $m_n$ et $M_n$. Ceci démontre l'assertion sur le type de $H_\lambda$, puisqu'on a $m_n = 2|\lambda|^{2^n - 1}$ et $M_n = 2(3|\lambda|)^{2^n - 1}$.

L'équation fonctionnelle de $H_{\lambda}$ permet aussi d'en déterminer les points critiques : ce sont exactement les points de la forme $\lambda^{n}z_{0}$, avec $n \geq 1$ et $H_{\lambda}(z_{0}) = 1/2$; les valeurs critiques correspondantes décrivent l'orbite positive du point critique $c = 1/2$ de $P_{\lambda}$.

## 1.3.2 - Supposons maintenant qu'on ait $|\lambda| < 1$.

Proposition.— Le rayon de convergence $R_{2}(\lambda)$ est fini et non nul. La fonction $H_{\lambda}$ se prolonge continûment sur le disque fermé $\{z,|z|\leq R_{2}(\lambda)\}$ elle est injective sur ce disque, et y vérifie l'équation fonctionnelle $H_{\lambda}(\lambda z)=P_{\lambda}(H_{\lambda}(z))$; elle possède sur le cercle de convergence $\{z,|z|=R_{2}(\lambda)\}$ une unique singularité en un point noté $U(\lambda)$; on a $H_{\lambda}(U(\lambda))=1/2$ et la fonction $(H_{\lambda}(z)-1/2)^{2}$ est holomorphe en $U(\lambda)$.

Démonstration. Que $R_2(\lambda)$ soit non nul résulte du théorème de Poincaré déjà cité. L'équation fonctionnelle $H_{\lambda}(\lambda z) = P_{\lambda}(H_{\lambda}(z))$ est vérifiée sur le disque de convergence de $H_{\lambda}$ et montre que $H_{\lambda}$ est injective sur ce disque. D'autre part, si $H_{\lambda}$ est holomorphe sur un disque $\{z, |z| < r\}$ et n'y prend pas la valeur $\lambda/4$ (valeur critique de $P_{\lambda}$), cette même équation fonctionnelle permet de prolonger analytiquement $H_{\lambda}$ sur le disque $\{z, |z| < |\lambda|^{-1}r\}$. Il existe donc un nombre complexe $U(\lambda)$, de module $R_2(\lambda)$, tel que $H_{\lambda}(\lambda U(\lambda)) = \lambda/4$. Les conclusions de la proposition qui restent à démontrer résultent alors immédiatement de l'équation fonctionnelle de $H_{\lambda}$.

Nous étudierons en détail dans le prochain paragraphe la fonction : $\lambda \longmapsto U(\lambda)$.

L'équation fonctionnelle de $H_{\lambda}$ permet en fait de décrire complètement sa surface de Riemann ; c'est un revêtement ramifié de $\mathbb{C}$, possédant, au-dessus de chaque point $\lambda^{-n}U(\lambda)(n \geq 0)$ exactement $2^{n}$ points de ramification d'ordre 2. La fonction $H_{\lambda}$ y est globalement injective, et réalise un biholomorphisme de sa surface de Riemann sur le bassin d'attraction du point 0 de $P_{\lambda}$.

1.3.3 - Le cas où $\lambda$ est de module 1, mais n'est pas racine de l'unité, est évidemment celui qui nous intéresse le plus, mais aussi le plus difficile à étudier. Pour l'instant, signalons simplement, dans l'esprit de ce qui précède, le fait bien connu suivant : lorsque le rayon de convergence $R_{2}(\lambda)$ est non nul, la conjugaison $H_{\lambda}$ est injective sur son disque de convergence, elle réalise un biholomorphisme de ce disque sur le disque de Siegel de $P_{\lambda}$ en 0, et tout point du cercle de convergence est une singularité de $H_{\lambda}$.

## 1.4 - Perturbations quadratiques des applications univalentes.

Soient $\alpha\in\mathbb{R}-\mathbb{Q}$, $\lambda=\exp(2\pi i\alpha)$, et $f$ un élément de $S_{\lambda}$, c'est à dire une application holomorphe injective dans $\mathbb{D}$ qui vérifie $f(0)=0$ et $Df(0)=\lambda$.

Pour $b \in \mathbb{C}$, désignons par $f_b$ l'application holomorphe sur $\mathbb{D}$ définie par :

$$
f _ {b} (z) = f (z) + b z ^ {2}.
$$

Ecrivons la linéarisante formelle $H_{b}$ de $f_{b}$ (cf.I.2.1) sous la forme :

$$
H _ {b} (z) = z \left(1 + \sum_ {n \geq 1} H _ {n} ^ {*} (b) z ^ {n}\right).
$$

Lemme.— La fonction  $H_{n}^{*}(b)$  est, pour  $n \geq 1$ , un polynôme de degré n en b.

Démonstration. Elle est immédiate à partir des relations de récurrence définissant les coefficients de $H_{b}$. On vérifie par ailleurs que le coefficient de $b^{n}$ dans $H_{n}^{*}$ est égal à $(-1)^{n}H_{n}(\lambda)$, où $H_{n}(\lambda)$ a été défini en 1.2.

Rappelons ([D-H]) qu'une application à allure polynômiale de degré 2 est un triplet $(U, U', F)$, où $U, U'$ sont des ouverts simplement connexes de $\mathbb{C}$ distincts de $\mathbb{C}$, $U'$ est relativement compact dans $U$ et $f: U' \to U$ est holomorphe et propre de degré 2.

Dans des régions appropriées, les applications $f_b$ sont à allure polynômiale de degré 2 lorsque $|b|$ est assez grand.

Soit $\mathcal{W} = \{z, |z| < \frac{13}{36}\}$; définissons :

$$
\mathcal {W} _ {b} = \{z, | z | \leq 1 / 3, \quad f _ {b} (z) \in \mathcal {W} \}.
$$

Lemme.— Pour  $|b| \geq 10$ ,  $(\mathcal{W}, \mathcal{W}_{b}, f_{b})$  est à allure polynômiale de degré 2.

Démonstration. Comme $f$ est univalente, on a, pour tout $z \in \mathbb{D}$:

$$
| f (z) | \leq \frac {| z |}{(1 - | z |) ^ {2}}
$$

En particulier, on a $|f(z)| \leq 3/4$ pour $|z| = 1/3$. Pour $|b| \geq 10$, on a d'autre part :

$$
| b z ^ {2} | \geq \frac {1 0}{9} = \frac {1 3}{3 6} + \frac {3}{4}, \quad \text { pour } \quad | z | = 1 / 3.
$$

D'après le théorème de Rouché, $f_{b}: \mathcal{W}_{b} \to \mathcal{W}$ est propre de degré 2. Si $\mathcal{W}_{b}$ n'était pas connexe, la composante connexe de $\mathcal{W}_{b}$ contenant 0 serait envoyée par $f_{b}$ de façon biholomorphe sur $\mathcal{W}$, ce qui est impossible puisque $|\lambda| = 1$.

## 1.5 - Notons $\Gamma$ le cercle $\{b\in\mathbb{C},|b|=10\}$.

Le théorème de rectification des applications à allure polynômiale ([D-H]) garantit que, pour $b \in \Gamma$, l'application $f_b$ est conjuguée sur $\mathcal{W}_b$ à un polynôme de degré 2 par un homéomorphisme quasiconforme du plan complexe. Nous reprenons cependant la démonstration de ce théorème dans notre situation, car nous sommes intéressés par la dépendance de la conjugaison quasiconforme par rapport à $f \in S$ et $b \in \Gamma$.

Pour $a \in (0,1]$, $b \in \Gamma$, et $f \in S$, nous définissons :

$$
f _ {a, b} (z) = a ^ {- 1} f (a z) + b z ^ {2}.
$$

Nous choisissons d'autre part, une fois pour toutes, une fonction $\eta$ de classe $C^\infty$ sur $\mathbb{R}$, à valeurs dans $[0,1]$, qui vaut 1 sur $(- \infty, 1/3]$ et 0 sur $[\frac{13}{36}, +\infty)$.

Nous définissons alors, pour $a \in (0,1]$, $b \in \Gamma$, $f \in S$ une application $\tilde{f}_{a,b}$ de $\mathbb{C}$ dans $\mathbb{C}$ par la formule :

$$
\tilde {f} _ {a, b} (z) = \eta (| z |) f _ {a, b} (z) + (1 - \eta (| z |)) (\lambda z + b z ^ {2}).
$$

Cette application coïncide avec $f_{a,b}$ dans le disque $\{z, |z| \leq 1/3\}$, avec $\lambda z + bz^2$ hors du disque $\{z, |z| < \frac{13}{36}\}$ et est de classe $C^\infty$. Lorsque $a$ tend vers 0, l'application $\tilde{f}_{a,b}$ converge dans la $C^\infty$- topologie, uniformément en $b \in \Gamma$ et $f \in S$, vers le polynôme quadratique $\lambda z + bz^2$. On a donc le :

Lemme.— Il existe  $a_{0} \in (0,1]$  et une application continue  $k : [0, a_{0}] \to [0,1)$ , vérifiant  $k(0) = 0$ , tels que pour tout  $f \in S$ ,  $b \in \Gamma$ ,  $a \in (0, a_{0}]$ , l'application  $f_{a,b}$  soit un revêtement ramifié de degré 2 de C et vérifie :

$$
\left| \frac {\partial}{\partial \bar {z}} \tilde {f} _ {a, b} (z) \right| \leq k (a) \left| \frac {\partial}{\partial z} \tilde {f} _ {a, b} (z) \right|,
$$

pour $\frac{1}{3} \leq |z| \leq \frac{13}{36}$.

## 1.6 -

Nous fixons dans ce numéro $f \in S$, $a \in (0, a_0]$, et $b \in \Gamma$.

Pour tout ouvert $U$ de $\mathbb{C}$, nous identifions les formes de Beltrami sur $U$ aux fonctions $\mu\in L^{\infty}(U)$ de norme $<1$.

Si $f: U \to V$ est une application de classe $C^{1}$, et $\mu$ est une forme de Beltrami sur $V$, la forme $f^{*}\mu$ sur $U$ est donnée par

$$
(f ^ {*} \mu) (z) = \frac {\overline {{\frac {\partial f}{\partial z} (z)}} \mu (f (z)) + \frac {\partial f}{\partial \bar {z}} (z)}{\overline {{\frac {\partial f}{\partial \bar {z}} (z)}} \mu (f (z)) + \frac {\partial f}{\partial z} (z)}.
$$

Il existe une unique forme de Beltrami $\mu = \mu_{f,a,b}$ sur $\mathbb{C}$ qui est invariante par $\tilde{f}_{a,b}$, nulle sur $\mathbb{C} - \mathcal{W}$, et nulle sur l'ensemble de Julia rempli $\bigcap_{n\geq 0}f_{a,b}^{-n}(\mathcal{W}_b)$ de $f_{a,b}$. Le support de $\mu$ est donc contenu dans $\mathcal{W}$ et on a, d'après les lemmes des Paragraphs 1.4 et 1.5:

$$
\left\| \mu_ {f, a, b} \right\| _ {L ^ {\infty}} \leq k (a).
$$

D'après le théorème d'Ahlfors-Bers, il existe un unique homéomorphisme quasiconforme $\phi = \phi_{f,a,b}$ qui vérifie les propriétés suivantes :

(i) pour presque tout $z \in \mathbb{C}$,

$$
\frac {\partial}{\partial \bar {z}} \phi (z) = \mu (z) \frac {\partial}{\partial z} \phi (z);
$$

(ii) $\phi (0) = 0$

(iii) La fonction $\phi(z) - z$ est bornée.

Lemme.— On a $\phi \circ \tilde{f}_{a,b} \circ \phi^{-1}(z) = \lambda z + bz^2$.

Démonstration. L'application $\phi \circ \tilde{f}_{a,b} \circ \phi^{-1}$ est quasi-régulière (i.e. localement composée d'une application holomorphe et d'un homéomorphisme quasi conforme) et préserve la forme de Beltrami nulle de $\mathbb{C}$; elle est donc holomorphe; c'est un revêtement ramifié de degré 2 de $\mathbb{C}$ qui fixe 0 (d'après (ii) ci-dessus et le Lemme 1.5), elle peut donc s'écrire $\lambda'z + b'z^2$; on a $b' = b$ d'après la propriété (iii) de $\phi$.

Il reste à voir qu'on a $\lambda = \lambda'$. Pour ceci, on peut invoquer un résultat de Naïshul ([N]) qui dit que la valeur propre en un point fixe d'un germe de difféomorphisme

holomorphe, lorsqu'elle est de module 1, est un invariant de conjugaison topologique. Cependant, la conjugaison $\phi$ est dans notre cas quasiconforme, et ceci permet de donner une démonstration plus simple que dans le cas (beaucoup plus difficile) d'une conjugaison topologique. Cette démonstration m'a été indiquée par R. Douady.

Pour $0 < t \leq 1$, posons $T = \phi(t)$ et $\phi_t(z) = \frac{1}{T}\phi(tz)$; les $\phi_t$, qui fixent 0 et 1, forment une famille normale. En posant $\tilde{f}_t(z) = \frac{1}{t}\tilde{f}_{a,b}(tz)$, on a $\phi_t \circ \tilde{f}_t \circ \phi_t^{-1} = \lambda'z + bTz^2$; si $\phi_0$ est une valeur d'adhérence des $\phi_t$ lorsque $t$ tend vers 0, on a donc $\phi_0(\lambda z) = \lambda'\phi_0(z)$, pour un homéomorphisme (quasiconforme) $\phi_0$, d'où $\lambda = \lambda'$ (car $\lambda$ est de module 1).

1.7 - Fixons $a \in (0, a_0]$ et posons $K(a) = \frac{1 + k(a)}{1 - k(a)}$.

La famille des applications $\phi_{f,a,b}$, lorsque $f$ décrit $S$ et $b$ décrit $\Gamma$, est une famille normale d'homéomorphismes $K(a)$-quasiconformes: en effet les $\phi_{f,a,b}$ fixent 0 et sont holomorphes dans $\mathbb{C}-\mathcal{W}$, de dérivée 1 à l'infini. On en déduit ([Ah]) qu'il existe une constante $C(a)$, ne dépendant pas de $f\in S$ et $b\in\Gamma$, telle qu'on ait, pour $z_{1}, z_{2}\in\mathbb{D}$:

$$
\left| \phi_ {f, a, b} (z _ {1}) - \phi_ {f, a, b} (z _ {2}) \right| \leq C (a) \left| z _ {1} - z _ {2} \right| ^ {1 / K (a)}.
$$

1.8 - Supposons maintenant que le rayon de convergence $R_2(\lambda)$ soit strictement positif. Le polynôme $P_{\lambda}$ possède donc un disque de Siegel $D_{\lambda}$ à l'origine, et le théorème de Koebe indique que $D_{\lambda}$ contient le disque centré en 0 de rayon $\frac{1}{4} R_2(\lambda)$. Le polynôme $\lambda z + bz^2$, conjugué à $P_{\lambda}$ par une homothétie de rapport $-\lambda b^{-1}$, possède donc à l'origine un disque de Siegel qui contient le disque $\{z, |z| \leq \frac{1}{40} R_2(\lambda)\}$.

Notons $D_{\lambda}^{\prime}$ l'image par $\phi_{f,a,b}^{-1}$ de ce disque de Siegel.

Lemme.—

1. L'application $f_{a,b}$ est linéarisable au voisinage de l'origine, et son disque de Siegel est $D_{\lambda}'$.

2. Le disque $\left\{z, |z| \leq \left[\frac{1}{40C(a)} R_2(\lambda)\right]^{K(a)}\right\}$ est contenu dans $D_{\lambda}'$.

3. Le disque de Siegel $D_{\lambda}^{\prime}$ est contenu dans $\mathcal{W}_{b}$.

Démonstration. La première assertion résulte de la caractérisation topologique des disques de Siegel donnée en I.2.4.

La seconde résulte de la dernière inégalité de 1.7.

La troisième assertion résulte de ce qu'on a $\lim_{n\to +\infty}\tilde{f}_{a,b}(z)^{n} = +\infty$ pour $z\in \mathbb{C} - \mathcal{W}_b$

$\mathrm{Posons~}R_{a}=\left[\frac{1}{40C(a)} R_{2}(\lambda)\right]^{K(a)}$, et notons $H_{n}^{*}(a,b)$ les coefficients de $z^{n+1}$ dans l'application linéarisante $H_{a,b}$ de $f_{a,b}$ (cf. 1.4). On a $|H_{n}^{*}(a,b)|\leq\frac{1}{3} R_{a}^{-n-1}$ pour $f\in S$

$b \in \Gamma$ d'après le lemme ci-dessus. D'après le lemme de 1.4, on a donc $|H_n^*(a,0)| \leq \frac{1}{3} R_a^{-n-1}$.

Le rayon de convergence de  $H_{a,0}$  est donc au moins égal à  $R_{a}$ ; on en déduit que le rayon de convergence  $R(f)$  de l'application linéarisante  $H_{f} = H_{1,0}$  de f est au moins égal à  $aR_{a}$ . En se rappelant que l'application k tend vers 0, lorsque a tend vers 0, et en utilisant le Théorème I.2.6, on obtient finalement l'estimation suivante de  $R_{2}(\lambda)$  (avec  $\lambda = E(\alpha)$ ):

## Théorème.—

1. Si $\alpha$ n'appartient pas à $\mathcal{B}$, $P_{\lambda}$ n'est pas linéarisable.

2. Il existe une constante universelle $C_{1}$ et, pour tout $\varepsilon > 0$, une constante $C(\varepsilon)$ telles qu'on ait, pour tout $\alpha \in \mathcal{B}$:

$$
(1 - \varepsilon) \Phi (\alpha) - C (\varepsilon) \leq - \mathrm{Log} R _ {2} (\lambda) \leq \Phi (\alpha) + C _ {1}.
$$

1.9 - Le théorème précédent indique que la famille des polynômes quadratiques  $(P_{\lambda})_{|\lambda|=1}$  fournit des germes de difféomorphismes non linéarisables lorsque  $\lambda = E(\alpha)$ ,  $\alpha \notin B$ , et que le rayon de convergence est “presque” le plus petit possible lorsque  $\lambda = E(\alpha)$ ,  $\alpha \in B$ . La question de savoir, pour  $\alpha \in B$ , si le rayon de convergence est le plus petit possible, à un facteur multiplicatif près, se pose donc tout naturellement.

## Question : La fonction $\alpha \mapsto \Phi(\alpha) + \operatorname{Log} R_2(\lambda)$ est-elle bornée sur $\mathcal{B}$?

Le Théorème I.2.6 montre que cette fonction est minorée, et le théorème précédent qu'elle est  $o(\Phi(\alpha))$ .

Une question plus précise est la suivante : peut-on, lorsque $\alpha \in \mathcal{B}$ et $\Phi(\alpha)$ est assez grand, obtenir le polynôme $P_{\lambda}$ comme résultat des constructions décrites en I.5.3 et I.5.4 ? Si oui, la réponse à la question précédente est positive.

## 2 - Une fonction holomorphe remarquable.

2.1 - Nous avons vu au paragraphe 1.3.2 qu'il existait, pour $\lambda \in \mathbb{C}^*$, $|\lambda| < 1$, un unique nombre complexe $U(\lambda)$, de module $R_2(\lambda)$, tel que $H_{\lambda}(U(\lambda)) = c = 1/2$, le point critique de $P_{\lambda}$.

Nous étudions dans ce paragraphe la fonction $U: \mathbb{D}^{*} \to \mathbb{C}$, avec un intérêt plus prononcé pour ses valeurs au bord du disque.

Proposition.— La fonction U se prolonge en une fonction holomorphe et bornée sur D. Elle est limite, uniformément sur les compacts de D, de la suite des polynômes  $U_{n}(\lambda) = \lambda^{-n} P_{\lambda}^{n}(1/2)$ . On a  $U(0) = 1/4$ .

Démonstration. La formule définissant $P_{\lambda}$ montre que les $U_{n}$ satisfont à la relation de récurrence :

$$
U _ {n + 1} (\lambda) = U _ {n} (\lambda) - \lambda^ {n} U _ {n} ^ {2} (\lambda),
$$

$$
U _ {0} (\lambda) = 1 / 2.
$$

Ce sont donc bien des polynômes.

Montrons qu'on a $|U_n(\lambda)| \leq 2$ pour tout $n \geq 0$ et tout $\lambda \in \overline{\mathbb{D}}$. Il suffit de le prouver lorsque $|\lambda| = 1$, et on a alors $|U_n(\lambda)| = |P_\lambda^n(1/2)|$. On sait depuis Fatou que l'orbite du point critique de $P_\lambda$ ne peut tendre vers l'infini lorsque $\lambda$ est une racine de l'unité. Comme on a :

$$
| P _ {\lambda} (z) | \geq | z | (| z | - 1)
$$

pour $|\lambda| = 1$, on voit qu'on a $|P_{\lambda}^{n}(1/2)| \leq 2$ pour tout $n \geq 0$, lorsque $\lambda$ est racine de l'unité, donc pour tout $\lambda \in S^{1}$. On conclut bien qu'on a $|U_{n}(\lambda)| \leq 2$ pour $\lambda \in \overline{\mathbb{D}}$.

Ceci étant, la formule de récurrence des $U_{n}$ montre que la suite $(U_{n})_{n\geq0}$ converge uniformément sur tout compact de $\mathbb{D}$, et il suffit, pour terminer la démonstration de la proposition, de vérifier que la limite est $U$. Or, pour $\lambda\in\mathbb{D}$, on a:

$$
H _ {\lambda} \left(\lambda^ {n} U (\lambda)\right) = P _ {\lambda} ^ {n} (1 / 2),
$$

par l'équation fonctionnelle de $H_{\lambda}$, et $DH_{\lambda}(0)=1$, d'où finalement :

$$
\lim _ {n \to + \infty} U _ {n} (\lambda) = \lim _ {n \to + \infty} \lambda^ {- n} H _ {\lambda} \left(\lambda^ {n} U (\lambda)\right) = U (\lambda).
$$

2.2 - La démonstration de la proposition donne trivialement $R_2(\lambda) = |U(\lambda)| \leq 2$ pour $\lambda \in \mathbb{D}$. On obtient $R_2(\lambda) \leq 1$ pour $\lambda \in \mathbb{D}$ en observant que l'image par $H_\lambda$ du disque $\{z, |z| < |\lambda|R_2(\lambda)\}$ ne contient pas la valeur critique $\lambda/4$ de $P_\lambda$, et en appliquant le théorème de Koebé (on a $DH_\lambda(0) = 1$).

En appliquant de façon un peu plus subtile la théorie des fonctions univalentes, Herman a amélioré cette estimation pour obtenir ([He])

$$
| U (\lambda) | \leq 4 / 7, \quad \lambda \in \mathbb {D}.
$$

Par ailleurs, on peut utiliser la relation de récurrence des $U_{n}$ pour calculer le développement en série entière de $U$ en 0. On a :

$$
U (\lambda) = \frac {1}{4} - \frac {\lambda}{1 6} - \frac {\lambda^ {2}}{1 6} - \frac {\lambda^ {3}}{3 2} \dots
$$

Les coefficients sont rationnels, le dénominateur étant une puissance de 2.

2.3 - Un célèbre théorème de Fatou dit qu'une fonction holomorphe et bornée dans le disque D admet en presque tout point du bord une limite non-tangentielle non nulle.

En appliquant ce théorème à la fonction U, on obtient immédiatement que, pour presque tout  $\lambda \in S^{1}$ , le polynôme  $P_{\lambda}$  est linéarisable en 0. Plus précisément, on a la :

Proposition.— Soit $\lambda_{0} \in S^{1}$, non racine de l'unité. Le rayon de convergence $R_{2}(\lambda_{0})$ de $H_{\lambda_{0}}$ est au moins égal à la limite supérieure de $|U(\lambda)|$, lorsque $\lambda \in \mathbb{D}$ tend vers $\lambda_{0}$.

Démonstration. Soient en effet $R$ cette limite supérieure, qu'on peut supposer strictement positive, et $(\lambda_n)_{n\geq 1}$ une suite dans $\mathbb{D}$ qui tend vers $\lambda_0$ telle que $R_2(\lambda_n)$ tende vers $R$. Comme les fonctions $H_{\lambda_n}$ sont univalentes sur les disques $\{z,|z| < R_2(\lambda_n)\}$, on peut en extraire une suite qui converge sur les compacts du disque $\{z,|z| < R\}$. La limite $H$ vérifie $DH(0) = 1$ et $H(\lambda_0z) = P_{\lambda_0}(H(z))$ par passage à la limite dans les équations correspondantes pour $\lambda_n$. On a donc $H_{\lambda_0} = H$ et $R_2(\lambda_0) \geq R$.

Si $\lambda_0$ est racine de l'unité, le même argument montre que $U(\lambda)$ tend vers 0 lorsque $\lambda \in \mathbb{D}$ tend vers $\lambda_0$.

## 2.4 - On va préciser le résultat précédent.

Théorème.— Pour tout $\lambda \in S^{1}$, le module de la fonction $U(\lambda)$ admet en $\lambda_{0}$ une limite non tangentielle qui est égale au rayon de convergence $R_{2}(\lambda_{0})$ de $H_{\lambda_{0}}$.

Remarque : Lorsque $\lambda_{0}$ est racine de l'unité, $P_{\lambda_{0}}$ n'est même pas formellement linéarisable; on pose alors $R_{2}(\lambda_{0}) = 0$.

Démonstration. Compte tenu de la proposition précédente, il suffit de montrer que la limite inférieure non tangentielle de  $|U(\lambda)|$  en  $\lambda_{0}$ , que nous noterons provisoirement  $R_{-}(\lambda_{0})$ , est au moins égale à  $R_{2}(\lambda_{0})$ . Il n'y a rien à démontrer lorsque  $R_{2}(\lambda_{0})$  est nul (en particulier lorsque  $\lambda_{0}$  est racine de l'unité); nous supposons dans la suite qu'on a  $R_{2}(\lambda_{0}) > 0$ .

Soit $\lambda\in\mathbb{D}$, $\lambda\neq0$. Désignons par $\mathcal{U}_{\lambda}$ le bassin d'attraction du point fixe attractif 0 de $P_{\lambda}$, et par $\mathcal{V}_{\lambda}$ l'image par $H_{\lambda}$ de son disque de convergence. En notant $C(\mathcal{U}_{\lambda})$, $C(\mathcal{V}_{\lambda})$ les capacités conformes de ces ouverts par rapport à 0 (cf. I.2.3), on a $\mathcal{V}_{\lambda}\subset\mathcal{U}_{\lambda}$ d'où :

$$
R _ {2} (\lambda) = | U (\lambda) | = C \left(\mathcal {V} _ {\lambda}\right) \leq C \left(\mathcal {U} _ {\lambda}\right).
$$

Pour conclure la démonstration du théorème, nous démontrerons les deux propositions suivantes :

Proposition 1.— Pour tout $\lambda_{0} \in S^{1}$ la limite inférieure non tangentielle de $C(\mathcal{U}_{\lambda})$ en $\lambda_{0}$ est au moins égale à $R_{2}(\lambda_{0})$.

Proposition 2.— Pour tout $\lambda_{0} \in S^{1}$, non racine de l'unité, le rapport $C(\mathcal{V}_{\lambda})/C(\mathcal{U}_{\lambda})$ tend vers 1 lorsque $\lambda \in \mathbb{D}$ tend vers $\lambda_{0}$.

## 2.5 - Démonstration de la Proposition 1.

On peut bien sûr supposer que  $R_{2}(\lambda_{0})$  est strictement positif (sinon, il n'y a rien à démontrer), donc en particulier  $\lambda_{0}$  n'est pas racine de l'unité.

Donnons nous $\theta_0 \in (0, \pi/2)$ et $\varepsilon > 0$. On va démontrer qu'il existe $t_0 > 0$ tel que l'image par $H_{\lambda_0}$ du disque $\{z, |z| \leq (1 - \varepsilon) R_2(\lambda_0)\}$ soit contenue dans $\mathcal{U}_{\lambda}$ pour tout $\lambda \in \mathbb{D}$ qui s'écrit $\lambda = (1 - t)\lambda_0$, $|\operatorname{Arg} t| \leq \theta_0, 0 < |t| < t_0$.

Ceci implique qu'on a $C(\mathcal{U}_{\lambda}) \geq (1 - \varepsilon)R_2(\lambda_0)$ pour de tels $\lambda$, d'où la Proposition 1.

Soit $x_0$ un point du disque $\{z, |z| \leq (1 - \varepsilon) R_2(\lambda_0)\}$. On définit, pour $t \in \mathbb{C}$, $\lambda = (1 - t) \lambda_0$:

$$
y _ {0} = H _ {\lambda_ {0}} (x _ {0});
$$

$$
y _ {n} (t) = P _ {\lambda} ^ {n} \left(y _ {0}\right) = P _ {\lambda} \left(y _ {n - 1} (t)\right), \quad n \geq 0.
$$

Pour $|t|$ assez petit, on définit aussi :

$$
x _ {n} (t) = H _ {\lambda_ {0}} ^ {- 1} \left(y _ {n} (t)\right), \quad \text { pour } \quad n \geq 0.
$$

On a donc $x_{n}(0) = \lambda_{0}^{n}x_{0}$, et :

$$
D x _ {n} (0) = D y _ {n} (0) \left[ D H _ {\lambda_ {0}} (x _ {n} (0)) \right] ^ {- 1}
$$

Comme on a $P_{\lambda} = (1 - t)P_{\lambda_0}$, les dérivées des fonctions $y_n$ en 0 satisfont à la relation de récurrence :

$$
D y _ {n} (0) = - y _ {n} (0) + D P _ {\lambda_ {0}} \left(y _ {n - 1} (0)\right) D y _ {n - 1} (0).
$$

D'après l'équation fonctionnelle de $H_{\lambda_0}$, on a :

$$
\begin{array}{c} D P _ {\lambda_ {0}} (y _ {n - 1} (0)) = D P _ {\lambda_ {0}} (H _ {\lambda_ {0}} (x _ {n - 1} (0))) \\ = \lambda_ {0} \frac {D H _ {\lambda_ {0}} (\lambda_ {0} x _ {n - 1} (0))}{D H _ {\lambda_ {0}} (x _ {n - 1} (0))} \end{array}
$$

On en déduit la formule suivante pour  $Dx_{n}(0)$  :

$$
D x _ {n} (0) = - \lambda_ {0} ^ {n} x _ {0} \sum_ {i = 1} ^ {n} k \left(\lambda_ {0} ^ {i} x _ {0}\right),
$$

où $k$ est la fonction holomorphe sur le disque $\{z, |z| < R_2(\lambda_0)\}$ définie par :

$$
k (z) = \frac {H _ {\lambda_ {0}} (z)}{z D H _ {\lambda_ {0}} (z)}.
$$

Comme $\lambda_0$ n'est pas racine de l'unité, les sommes de Birkhoff $\frac{1}{n} \sum_{i=1}^{n} k\left(\lambda_0^i z\right)$ convergent vers $k(0) = 1$ uniformément dans $\{z, |z| \leq (1 - \varepsilon) R_2(\lambda_0)\}$. Il existe donc $N > 0$ tel qu'on ait, pour tout $x_0$ dans ce disque :

$$
\left| D x _ {N} (0) + N \lambda_ {0} ^ {N} x _ {0} \right| <   N \theta ,
$$

où $\theta > 0$ est choisi dans la suite.

D'autre part, pour $N$ fixé, la famille des applications $x_{N}(t)$, lorsque $x_{0}$ décrit le disque $\{z, |z| \leq (1 - \varepsilon)R_{2}(\lambda_{0})\}$ est normale au voisinage de l'origine ; il existe donc $t_{0} > 0$ tel qu'on ait :

$$
| x _ {N} (t) - x _ {N} (0) - t D x _ {N} (0) | \leq | t | \theta ,
$$

pour $|x_0| \leq (1 - \varepsilon) R_2(\lambda_0)$ et $|t| \leq t_0$.

En réunissant les deux dernières inégalités, on obtient finalement :

$$
\left| \frac {x _ {N} (t)}{x _ {N} (0)} - 1 + t N \right| \leq (N + 1) | t | \theta [ (1 - \varepsilon) R _ {2} (\lambda_ {0}) ] ^ {- 1}
$$

pour $|x_0| = (1 - \varepsilon)R_2(\lambda_0), |t| \leq t_0$.

En supposant de plus qu'on ait  $|\operatorname{Arg} t| \leq \theta_{0} < \pi/2$ , en choisissant  $\theta = \theta(\theta_{0})$  assez petit et en diminuant au besoin  $t_{0}$ , on conclut qu'on a :

$$
| x _ {N} (t) | <   | x _ {N} (0) |
$$

pour $|x_0| = (1 - \varepsilon)R_2(\lambda_0), 0 < |t| \leq t_0, |\operatorname{Arg} t| \leq \theta_0$.

Cela signifie que le domaine $H_{\lambda} \left( \{z, |z| \leq (1 - \varepsilon) R_2(\lambda_0)\} \right)$ est envoyé dans lui-même par $P_{\lambda}^{N}$, et implique, par le lemme de Schwarz, que ce domaine est contenu dans $\mathcal{U}_{\lambda} : c'$ est l'assertion que nous voulions démontrer.

## 2.6 - Démonstration de la Proposition 2.

Pour $\lambda \in \mathbb{D}$, $\lambda \neq 0$, considérons la représentation conforme $K_{\lambda} : \mathbb{D} \to \mathcal{U}_{\lambda}$ telle que $K_{\lambda}(0) = 0$ et $K_{\lambda}^{-1}(1) > 0$. (Le point 1 est l'image réciproque de 0 par $P_{\lambda}$ qui est distincte de 0, donc il appartient à $\mathcal{U}_{\lambda}$; il n'appartient pas à $\mathcal{V}_{\lambda}$).

L'application $Q_{\lambda} = K_{\lambda}^{-1}P_{\lambda}K_{\lambda}$ est un revêtement de D de degré 2 ramifié en un seul point ; c'est donc un produit de Blaschke de degré 2, qui d'après la normalisation faite sur $K_{\lambda}$ est égal à :

$$
Q _ {\lambda} (z) = e ^ {2 \pi i \alpha} z \frac {| \lambda | - z}{1 - | \lambda | z},
$$

avec $\lambda = |\lambda|e^{2\pi i\alpha}$.

Notons $\widetilde{H}_{\lambda}$ l'application linéarisante de $Q_{\lambda}$ en 0, $\widetilde{R}_{\lambda}$ son rayon de convergence et $\widetilde{\mathcal{V}}_{\lambda}$ l'image de son disque de convergence. On a :

$$
\widetilde {H} _ {\lambda} (z) = K _ {\lambda} ^ {- 1} H _ {\lambda} \left(D K _ {\lambda} (0) z\right),
$$

$$
\widetilde {\mathcal {V}} _ {\lambda} = K _ {\lambda} ^ {- 1} (\mathcal {V} _ {\lambda}),
$$

$$
\widetilde {R} _ {\lambda} = C (\widetilde {\mathcal {V}} _ {\lambda}, 0) = C (\mathcal {V} _ {\lambda}, 0) \left[ C (\mathcal {U} _ {\lambda}, 0) \right] ^ {- 1}.
$$

Il suffit donc de démontrer que $\widetilde{R}_{\lambda}$ tend vers 1 lorsque $\lambda$ tend vers une limite $\lambda_0 \in S^1$ qui n'est pas racine de l'unité.

Soit $r \in (0,1)$. Pour $|z| \leq r < |\lambda| < 1$, on a :

$$
\left| \frac {Q _ {\lambda} (z)}{z} \right| \leq \frac {| \lambda | + r}{1 + | \lambda | r} \leq | \lambda | + (1 - | \lambda |) \frac {2 r}{1 + r},
$$

$$
\left| \frac {Q _ {\lambda} (z)}{z} \right| \geq \frac {| \lambda | - r}{1 - | \lambda | r} \geq | \lambda | - (1 - | \lambda |) \frac {2 r}{1 - r},
$$

donc il existe $a = a(r) \in (0,1)$, $b = b(r) > 1$ et $s = s(r) \in (0,1)$ tels qu'on ait :

$$
| \lambda | ^ {b} \leq \left| \frac {Q _ {\lambda} (z)}{z} \right| \leq | \lambda | ^ {a}
$$

pour $|z| \leq r$, $s \leq |\lambda| < 1$.

D'autre part, le point critique $c(\lambda)$ de $Q_{\lambda}$ qui appartient à $\mathbb{D}$ ne dépend que de $|\lambda|$ et tend vers 1 lorsque $|\lambda|$ tend vers 1. Il appartient à l'adhérence de $\widetilde{\mathcal{V}}_{\lambda}$.

Lemme.— Lorsque  $|\lambda|$  tend vers 1,  $\widetilde{R}_{\lambda}$  n'approche pas 0.

Démonstration. Prenons, avec $r = 1/2$, $a, b, s$ comme ci-dessus, et $|\lambda|$ assez proche de 1 pour avoir $|\lambda| > 3/4$, $|\lambda| > s$, et $|c(\lambda)| > 1/2$. Il existe alors $N \in \mathbb{N}$ tel que $1/2 < |\lambda|^N < 2/3$ et $z_0 \in \widetilde{\mathcal{V}}_\lambda$ avec $|z_0| = 1/2$. En posant $z_0 = \widetilde{H}_\lambda(y_0)$, $|y_0| < \widetilde{R}_\lambda$, on a d'une part :

$$
Q _ {\lambda} ^ {N} (z _ {0}) = \widetilde {H} _ {\lambda} \left(\lambda^ {N} y _ {0}\right), \left| \lambda^ {N} y _ {0} \right| <   \frac {2}{3} \widetilde {R} _ {\lambda},
$$

et d'autre part :

$$
\left| Q _ {\lambda} ^ {N} (z _ {0}) \right| \geq | z _ {0} | | \lambda | ^ {N b} \geq 2 ^ {- 1 - b}.
$$

Les estimations standard de distorsion pour les fonctions univalentes montrent que $\widetilde{R}_{\lambda}$ ne peut être trop petit.

Supposons maintenant qu'il existe une suite $(\lambda_n)_{n\geq 1}$ dans $\mathbb{D}$, convergeant vers une limite $\lambda_0\in S^1$ qui n'est pas racine de l'unité, et telle que $\widetilde{R}_{\lambda_n}$ converge vers une limite $R < 1$. On a $R > 0$ d'après le lemme. Toute valeur d'adhérence $H$ de la suite $\widetilde{H}_{\lambda_n}$ vérifie $DH(0) = 1$ et

$$
H (\lambda_ {0} z) = \lambda_ {0} H (z) \quad \text { pour } \quad | z | <   R.
$$

Comme $\lambda_0$ n'est pas racine de l'unité, cela montre que la suite $\left(\widetilde{H}_{\lambda_n}\right)_{n\geq 1}$ converge vers l'identité uniformément sur les compacts du disque $\{z,|z| < R\}$. Prenons $r = \frac{1 + R}{2}$, $a,b,s$ comme ci-dessus, et $n$ assez grand pour avoir $|c(\lambda_n)| > r$, $|\lambda_n| > s$. Posons $\theta = \frac{R}{r} < 1$, $\theta' = \frac{1 + \theta}{2}$; pour $n$ assez grand, il existe un entier $N$ tel que $\theta < \lambda_n^{2Nb} < \theta'$ et un point $z_0 \in \widetilde{\mathcal{V}}_{\lambda_n}$ de module $r$. En écrivant $z_0 = \widetilde{H}_{\lambda_n}(y_0)$, avec $|y_0| < \widetilde{R}_{\lambda_n}$, on a :

$$
\left| Q _ {\lambda_ {n}} ^ {N} (z _ {0}) \right| \geq | z _ {0} | | \lambda_ {n} ^ {N b} | > (r R) ^ {1 / 2} > R,
$$

$$
Q _ {\lambda_ {n}} ^ {N} (z _ {0}) = \widetilde {H} _ {\lambda_ {n}} \left(\lambda_ {n} ^ {N} y _ {0}\right),
$$

$$
\left| \lambda_ {n} ^ {N} y _ {0} \right| <   (\theta^ {\prime}) ^ {1 / 2 b} \widetilde {R} _ {\lambda_ {n}};
$$

on obtient ainsi une contradiction avec la convergence vers l'identité des $\widetilde{H}_{\lambda_n}$, ce qui conclut la démonstration de la Proposition 2.

## 3 - Questions et compléments.

## 3.1 - Quelques formules reliées à la fonction U.

Nous avons vu aux Paragraphes 2.1, 2.2 comment calculer inductivement les coefficients de la série entière $U(\lambda)$. Nous nous intéressons dans ce paragraphe à des formules explicites pour $(4U)^{-s}$ (pour $s \in \mathbb{C}$) et $-\mathrm{Log}4U$. Les calculs que nous ferons et les équations qui en résulteront sont de nature purement formelle : il n'est pas tenu compte des questions de convergence.

Rappelons que la suite de polynômes  $(U_{n})_{n\geq0}$  qui converge vers U est définie par les relations :

$$
U _ {0} = 1 / 2, U _ {n + 1} = U _ {n} - \lambda^ {n} U _ {n} ^ {2} \quad \mathrm{pour} \quad n \geq 0.
$$

Considérons d'abord l'expression :

$$
A (s, k) = \sum_ {n \geq 1} U _ {n} ^ {- s} \lambda^ {k n}\tag{1}
$$

pour $s \in \mathbb{C}$ et $k \in \mathbb{N}^*$.

D'après la formule du binôme, on a, pour  $n \geq 1$  :

$$
U _ {n + 1} ^ {- s} - U _ {n} ^ {- s} = \sum_ {k \geq 1} U _ {n} ^ {k - s} \lambda^ {k n} \binom{s + k - 1}{k};\tag{2}
$$

on en déduit :

$$
\begin{array}{l} A (s, k) = (1 - \lambda^ {k}) ^ {- 1} \sum_ {n \geq 1} U _ {n} ^ {- s} (\lambda^ {k n} - \lambda^ {k (n + 1)}) \\ \qquad = \lambda^ {k} (1 - \lambda^ {k}) ^ {- 1} \left[ 4 ^ {s} + \sum_ {n \geq 1} (U _ {n + 1} ^ {- s} - U _ {n} ^ {- s}) \lambda^ {k n} \right] \\ \qquad = \lambda^ {k} (1 - \lambda^ {k}) ^ {- 1} \left[ 4 ^ {s} + \sum_ {k _ {1} > k} \binom {s + k _ {1} - k - 1} {k _ {1} - k} A (s - k _ {1} + k, k _ {1}) \right] \end{array}\tag{3}
$$

En développant à son tour $A(s - k_{1} + k, k_{1})$, puis en itérant indéfiniment cette procédure, on obtient finalement :

$$
\begin{array}{l} ^ {(4)} 4 ^ {- s} A (s, k) \\ = \frac {\lambda^ {k}}{1 - \lambda^ {k}} \sum_ {\ell \geq 0} \quad \sum_ {k = k _ {0} <   k _ {1} <   \dots <   k _ {\ell}} 4 ^ {k _ {0} - k _ {\ell}} \prod_ {i = 1} ^ {\ell} \frac {\lambda^ {k _ {i}}}{1 - \lambda^ {k _ {i}}} \binom {s + k _ {0} + k _ {i} - 2 k _ {i - 1} - 1} {k _ {i} - k _ {i - 1}}. \end{array} \tag {4}
$$

On utilise maintenant cette formule pour calculer  $(4U)^{-s}$ . On a, d'après (2) :

$$
\begin{array}{c} U ^ {- s} = U _ {1} ^ {- s} + \sum_ {n \geq 1} (U _ {n + 1} ^ {- s} - U _ {n} ^ {- s}) \\ = 4 ^ {s} + \sum_ {k \geq 1} A (s - k, k) \binom {s + k - 1} {k} \end{array}
$$

ce qui donne :

$$
(4 U) ^ {- s} = \sum_ {\ell \geq 0} \sum_ {0 = k _ {0} <   k _ {1} <   \dots <   k _ {\ell}} 4 ^ {- k _ {\ell}} \prod_ {i = 1} ^ {\ell} \frac {\lambda^ {k _ {i}}}{1 - \lambda^ {k _ {i}}} \binom{s + k _ {i} - 2 k _ {i - 1} - 1}{k _ {i} - k _ {i - 1}}.\tag{5}
$$

Une expression semblable pour $-\text{Log}4U$ s'obtient de la façon suivante ; on a : $U_1 = 1/4$, $U_{n+1} = U_n(1 - \lambda^n U_n)$, d'où :

$$
4 U = \prod_ {n \geq 1} \left(1 - \lambda^ {n} U _ {n}\right),
$$

$$
\begin{array}{c} - \operatorname{Log} 4 U = \sum_ {k \geq 1} \sum_ {n \geq 1} k ^ {- 1} \lambda^ {n k} U _ {n} ^ {k} \\ = \sum_ {k \geq 1} k ^ {- 1} A (- k, k), \end{array}
$$

d'où on tire :

$$
- \mathrm{Log} 4 U = \sum_ {\ell \geq 1} \sum_ {0 <   k _ {1} <   \ldots <   k _ {\ell}} 4 ^ {- k _ {\ell}} k _ {1} ^ {- 1} \prod_ {i = 1} ^ {\ell} \frac {\lambda^ {k _ {i}}}{1 - \lambda^ {k _ {i}}} \prod_ {i = 2} ^ {\ell} \binom{k _ {i} - 2 k _ {i - 1} - 1}{k _ {i} - k _ {i - 1}}.\tag{6}
$$

Remarque : Supposons que $s \in \mathbb{Z}$ ; dans la formule (5) ci-dessus, les seuls termes ne s'annulant pas à cause de la présence des coefficients binomiaux sont ceux qui vérifient, pour $1 \leq i \leq \ell$ :

$$
k _ {i} \leq 2 k _ {i - 1} - s \quad \text { ou } \quad k _ {i - 1} \leq s - 1.
$$

De même, dans la formule (6), les seuls termes ne s'annulant pas vérifient  $k_{i} \leq 2k_{i-1}$  pour  $2 \leq i \leq \ell$ .

## 3.2 - Quelques questions relatives à la fonction U.

3.2.1 - Nous avons vu au paragraphe précédent que le module de la fonction U admettait une limite non tangentielle en tout point  $\lambda_{0} \in S^{1}$ .

Question 1 : En quels points de $S^{1}$ la fonction $U$ admet-elle une limite non tangentielle ?

On peut aussi poser une question plus précise :

Question 2 : En quels points de $S^{1}$ l'argument de la fonction $U$ admet-il une limite non-tangentielle ?

On sait, par le théorème de Fatou, que l'ensemble de ces points est de mesure 1.

Au vu de la définition de  $U(\lambda)$  pour  $|\lambda| < 1$ , on pourrait s'attendre à ce que d'éventuelles limites non tangentielles non nulles de la fonction U soient reliées à la présence du point critique sur le bord du disque de Siegel correspondant.

Par exemple, soit $\alpha\in\mathcal{B}$, $\lambda=E(\alpha)$ et $D_{\lambda}$ le disque de Siegel de $P_{\lambda}$. Supposons que le bord $\partial D_{\lambda}$ de $D_{\lambda}$ soit localement connexe et contienne le point critique $c=1/2$.

Question 3 : La fonction U admet-elle en λ une limite non-tangentielle U(λ) telle que Hλ(U(λ)) = c ?

## 3.2.2 - Rappelons la question posée au Paragraphe 1.9.

Question 4: La fonction Log|U ∘ E| + Φ appartient-elle à L∞(T¹) ?

La fonction $\Phi$ est la fonction arithmétique définie au Chapitre I, Paragraphe 1.5.

L'argument de U est aussi intéressant.

Question 5 : L'argument de U est-il borné sur D ?

On peut même être plus optimiste :

Question 6 : La partie réelle de U est-elle toujours positive ?

Si la réponse à la question 5 est positive, il en est de même pour la question suivante :

Question 7 : La fonction Log|U| appartient-elle à BMO(S$^{1}$ ) ?

On rappelle que $BMO(S^1)$ est l'espace des fonctions $\varphi \in L^1(S^1)$ pour lesquelles :

$$
\underset {I} {\mathrm{Sup}} \frac {1}{| I |} \int_ {I} | \varphi - \varphi_ {I} | d t <   + \infty ,
$$

où $I$ décrit les intervalles de $S^{1}$, $|I|$ désigne la longueur de $I$ et $\varphi_{I}$ la moyenne de $\varphi$ sur $I$.

## 3.3 - Quelques remarques sur les coefficients des applications linéarisantes.

3.3.1 - Rappelons que si on écrit l'application linéarisante $H_{\lambda}$ de $P_{\lambda}$ sous la forme :

$$
H _ {\lambda} (z) = z \left(1 + \sum_ {n \geq 1} H _ {n} (\lambda) z ^ {n}\right),
$$

les $H_{n}(\lambda)$ satisfont à la relation de récurrence :

$$
H _ {0} (\lambda) = 1, H _ {n} (\lambda) = \frac {1}{1 - \lambda^ {n}} \sum_ {i + j = n - 1} H _ {i} (\lambda) H _ {j} (\lambda).
$$

Pour $i,j\geq0$, on notera $\Pi_{i,j}$ le polynôme de Gauss défini par :

$$
\Pi_ {i, j} (X) = \prod_ {\ell = 1} ^ {i + j} (1 - X ^ {\ell}) \left(\prod_ {\ell = 1} ^ {i} (1 - X ^ {\ell}) \prod_ {\ell = 1} ^ {j} (1 - X ^ {\ell})\right) ^ {- 1}.
$$

Ces polynômes sont à coefficients entiers positifs. Ceci étant, posons, pour  $n \geq 0$ :

$$
P _ {n} (\lambda) = \left[ \prod_ {\ell = 1} ^ {n} (1 - \lambda^ {\ell}) \right] H _ {n} (\lambda).
$$

Les $P_{n}$ sont alors des polynômes qui satisfont aux relations de récurrence :

$$
P _ {0} = 1, P _ {n} = \sum_ {i + j = n - 1} \Pi_ {i, j} P _ {i} P _ {j}.
$$

Les coefficients des $P_{n}$ sont donc entiers positifs. Le degré du polynôme $P_{n}$ s'écrit sous la forme $\frac{n(n+1)}{2}-\delta_{n}$, où $\delta_{n}$ est donné par :

$$
\delta_ {n} = (k - 1) 2 ^ {k} + 1 + (n - 2 ^ {k} + 1) (k + 1),
$$

pour $2^{k} - 1 \leq n \leq 2^{k+1} - 1$. On le vérifie aisément par récurrence sur $n$.

## 3.3.2 - Valeurs des  $P_{n}$  aux racines de l'unité.

Soit $\zeta$ une racine de l'unité primitive d'ordre $q \geq 1$. Les valeurs en $\zeta$ des polynômes de Gauss sont données par :

$$
\Pi_ {i, j} (\zeta) = 0, \quad \mathrm{si} \quad \left[ \frac {i + j}{q} \right] = \left[ \frac {i}{q} \right] + \left[ \frac {j}{q} \right] + 1;
$$

$$
\Pi_ {i, j} (\zeta) = \binom{m + n}{m} \Pi_ {r, s} (\zeta),
$$

si $i = mq + r$, $j = nq + s$, $0 \leq r \leq r + s < q$.

Pour $0 \leq k < q$, $m \geq 0$, posons $b_{k}(m) = P_{mq+k}(\zeta)$ et définissons une série formelle $B_{k}$ par la formule :

$$
B _ {k} (z) = \sum_ {m \geq 0} \frac {1}{m !} b _ {k} (m) z ^ {m}.
$$

On vérifie aisément qu'on a, pour  $1 \leq k < q$  :

$$
B _ {k} = \sum_ {r + s = k - 1} \Pi_ {r, s} (\zeta) B _ {r} B _ {s},
$$

$$
D B _ {0} = \sum_ {r + s = q - 1} \Pi_ {r, s} (\zeta) B _ {r} B _ {s}.
$$

On a donc  $B_{k} = P_{k}(\zeta)B_{0}^{k+1}$  et  $DB_{0} = P_{q}(\zeta)B_{0}^{q+1}$ , d'où on tire :

$$
B _ {0} (z) = \left(1 - q P _ {q} (\zeta) z\right) ^ {- 1 / q},
$$

et finalement :

$$
P _ {m q + r} (\zeta) = P _ {r} (\zeta) \frac {\Gamma (m + \frac {r + 1}{q})}{\Gamma (\frac {r + 1}{q})} \left(q P _ {q} (\zeta)\right) ^ {m},
$$

pour $m \geq 0, 0 \leq r < q$.

## 3.3.3 - Un équivalent pour $U^{n+1}(\lambda)H_n(\lambda)$.

Soit $\lambda \in \mathbb{D}^*$. On pose:

$$
\begin{array}{r l} h _ {\lambda} (z) & = H _ {\lambda} (U (\lambda) z) \\ & = z (U (\lambda) + \sum_ {n \geq 1} h _ {n} (\lambda) z ^ {n}), \end{array}
$$

de sorte qu'on a  $h_{n}(\lambda) = U^{n+1}(\lambda)H_{n}(\lambda)$ ,  $h_{\lambda}(1) = 1/2$ ,  $h_{\lambda}(\lambda) = \lambda/4$ . L'application  $h_{\lambda}$  vérifie, de même que  $H_{\lambda}$ , l'équation fonctionnelle :

$$
\lambda^ {- 1} h _ {\lambda} (\lambda z) - h _ {\lambda} (z) + h _ {\lambda} ^ {2} (z) = 0,
$$

dont on tire :

$$
h _ {\lambda} (z) = \frac {1 - \sqrt {1 - 4 \lambda^ {- 1} h _ {\lambda} (\lambda z)}}{2}.
$$

Proposition.— On a :

$$
\lim _ {n \rightarrow + \infty} h _ {n} (\lambda) n ^ {3 / 2} = \frac {1}{2} \pi^ {- 1 / 2} (D h _ {\lambda} (\lambda)) ^ {1 / 2}.
$$

Démonstration. On écrit :

$$
1 - 4 \lambda^ {- 1} h _ {\lambda} (\lambda z) = (1 - z) \varphi (z),
$$

où $\varphi$ est holomorphe et non nulle dans le disque $D = \{z, |z| < |\lambda|^{-1}\}$, et $\varphi(1) = 4Dh_{\lambda}(\lambda)$. Posons $a = 2(Dh_{\lambda}(\lambda))^{1/2}$ et :

$$
[ \varphi (z) ] ^ {1 / 2} = a + (1 - z) \psi (z).
$$

La fonction $\psi$ est holomorphe dans $D$; comme $h_{\lambda}(\lambda z)$ est bornée dans $D$, c'est aussi le cas de $\varphi$ et $\psi$. D'après la formule précédant la proposition, on a :

$$
2 h _ {\lambda} (z) = 1 - a (1 - z) ^ {1 / 2} - (1 - z) ^ {3 / 2} \psi (z).
$$

Pour $m\in \mathbb{N}$ , on a :

$$
(1 - z) ^ {m + 1 / 2} = \sum_ {\ell \geq 0} \frac {\Gamma (\ell - m - 1 / 2)}{\Gamma (- m - 1 / 2)} \frac {z ^ {\ell}}{\Gamma (\ell + 1)};
$$

d'autre part, en écrivant $\psi(z) = \sum \psi_n z^n$, on a $\psi_n = \mathcal{O}(|\lambda|^n)$. On obtient donc :

$$
2 h _ {n} (\lambda) = - a (\Gamma (- 1 / 2)) ^ {- 1} \frac {\Gamma (n - 1 / 2)}{\Gamma (n + 1)} + \mathcal {O} (n ^ {- 5 / 2}),
$$

et la proposition en résulte.

## Remarques :

0. La proposition est encore vraie pour $\lambda = 0$, car on a $h_0(z) = \frac{1}{2}(1 - \sqrt{1 - z})$.

1. En écrivant plus généralement :

$$
(\varphi (z)) ^ {1 / 2} = \sum_ {\ell \geq 0} a _ {\ell} (1 - z) ^ {\ell},
$$

On obtient pour $h_{n}(\lambda)$ le développement limité :

$$
h _ {n} (\lambda) = - \frac {1}{2} \sum_ {j \geq 0} \frac {a _ {j}}{\Gamma (- j - 1 / 2)} \frac {\Gamma (n - j - 1 / 2)}{\Gamma (n + 1)}.
$$

2. On peut exprimer  $Dh_{\lambda}(\lambda)$  en fonction des polynômes  $U_{n}$ . En dérivant en effet l'équation fonctionnelle de  $h_{\lambda}$ , on obtient :

$$
D h _ {\lambda} (\lambda z) = D h _ {\lambda} (z) \left(1 - 2 h _ {\lambda} (z)\right).
$$

Comme on a $Dh_{\lambda}(0) = U(\lambda)$ et $h_{\lambda}(\lambda^n) = \lambda^n U_n(\lambda)$, on obtient :

$$
D h _ {\lambda} (\lambda) = \frac {1}{4} \prod_ {n = 1} ^ {+ \infty} \frac {1 - \lambda^ {n} U _ {n} (\lambda)}{1 - 2 \lambda^ {n} U _ {n} (\lambda)}.
$$

3. Soit $K$ un compact de $\mathbb{D}$. Il est clair que la limite dans la proposition est uniforme pour $\lambda \in K$, donc que les fonctions $h_n$ (ou les polynômes $P_n$) ne s'annulent pas sur $K$ pour $n$ assez grand.

Question 8 : L'un des polynômes $P_{n}$ s'annule-t-il dans $\mathbb{D}$?

3.4 - Comportement non tangentiel de U aux racines de l'unité.

Soit  $\zeta$  une racine de l'unité, primitive d'ordre q.

Lemme 1.— On a $P_{q}(\zeta) \neq 0$

Démonstration. Si on a $P_{q}(\zeta)=0$, les relations de récurrence pour $P_{n}$ et les valeurs des $\Pi_{i,j}(\zeta)$ données en 3.3.2 montrent que $P_{n}$ s'annule en $\zeta$ au moins à l'ordre $\left[\frac{n}{q}\right]$; par suite $H_{n}(\lambda)$ admet une limite finie en $\zeta$ pour tout $n\geq0$. Le polynôme $P_{\zeta}$ est alors formellement linéarisable, donc linéarisable : mais on sait que ce n'est pas le cas.

Lemme 2.— Pour tout $m \in \mathbb{N}$, on a :

$$
\lim _ {\lambda \to \zeta} \left[ \prod_ {i = 1} ^ {m} (1 - \lambda^ {i}) \right] ^ {- 1} (1 - \lambda^ {q}) ^ {\frac {m}{q}} = \left\{ \begin{array}{l l} 0 & s i m \not \equiv 0 [ q ], \\ (q ^ {k} k!) ^ {- 1} & s i m = k q. \end{array} \right.
$$

La vérification est immédiate.

Notons $P_{\lambda}^{q}$ l'itéré $q$-ième (et non la puissance!) du polynôme $P_{\lambda}$. Alors $P_{\zeta}^{q}$ est de la forme :

$$
P _ {\zeta} ^ {q} (z) = z \left(1 + z ^ {q} R (z)\right),
$$

par conséquent on peut écrire $P_{\lambda}^{q}$ sous la forme :

$$
P _ {\lambda} ^ {q} (z) = \lambda^ {q} z (1 + z ^ {q} R (z) + (\zeta - \lambda) z S (\lambda , z)),
$$

avec $R \in \mathbb{C}[z]$ et $S \in \mathbb{C}[\lambda, z]$.

On fixe dans la suite un secteur non-tangentiel ouvert $V \subset \mathbb{D}$ de sommet $\zeta$. Pour $\lambda \in V$, on pose :

$$
Q _ {\lambda} (z) = (1 - \lambda^ {q}) ^ {- 1 / q} P _ {\lambda} ^ {q} ((1 - \lambda^ {q}) ^ {1 / q} z).
$$

On montre alors aisément les estimations suivantes :

Lemme 3.—

1. Il existe des constantes $a, \delta > 0$ telles qu'on ait $|Q_{\lambda}(z)| \leq |\lambda|^{aq}|z|$ pour $|z| \leq \delta$.

2. Pour tout $B > 0$, il existe des constantes $b = b(B)$, $\varepsilon = \varepsilon(B)$ strictement positives telles qu'on ait $|Q_{\lambda}(z)| \geq |\lambda|^{bq}|z|$ pour $|z| \leq B$ et $|\lambda - \zeta| \leq \varepsilon$.

Nous sommes maintenant en mesure de démontrer la :

Proposition.— Lorsque  $\lambda$  tend vers  $\zeta$  dans V, on a :

$$
\operatorname{Lim} \frac {[ U (\lambda) ] ^ {q}}{1 - \lambda^ {q}} = P _ {q} (\zeta) ^ {- 1}.
$$

Démonstration. Pour $\lambda\in V$, définissons :

$$
K _ {\lambda} (z) = \left(1 - \lambda^ {q}\right) ^ {- 1 / q} H _ {\lambda} \left(\left(1 - \lambda^ {q}\right) ^ {1 / q} z\right).
$$

On a alors $K_{\lambda}(0)=0$, $DK_{\lambda}(0)=1$; le rayon de convergence de $K_{\lambda}$ est égal à $|U(\lambda)||1-\lambda^{q}|^{-1/q}$; de plus, $K_{\lambda}$ est l'application linéarisante (normalisée) de $Q_{\lambda}$.

D'après la première assertion du Lemme 3, le bassin d'attraction de $Q_{\lambda}$, contient, pour tout $\lambda \in V$, le disque centré en 0 de rayon $\delta$. D'après le lemme de 2.6, le rayon de convergence de $K_{\lambda}$ est donc uniformément minoré pour $\lambda \in V$; les $K_{\lambda}$ pour $\lambda \in V$, forment donc une famille normale dans un voisinage de l'origine.

Pour $\lambda\in V$, le coefficient de $z^{n+1}$ dans $K_{\lambda}$ est

$$
P _ {n} (\lambda) (1 - \lambda^ {q}) ^ {n / q} \left[ \prod_ {i = 1} ^ {n} (1 - \lambda^ {i}) \right] ^ {- 1}.
$$

Lorsque $\lambda\in V$ tend vers $\zeta$, d'après le lemme 2 et les formules de 3.3.2 pour les valeurs en $\zeta$ du polynôme $P_{n}$, ce coefficient tend vers 0 si $n$ n'est pas multiple de $q$ et vers

$$
\frac {\Gamma (k + 1 / q)}{k ! \Gamma (1 / q)} (P _ {q} (\zeta)) ^ {k},
$$

si n = kq.

Donc la seule valeur d'adhérence possible des $K_{\lambda}$, lorsque $\lambda \in V$ tend vers $\zeta$, est la fonction :

$$
K (z) = z \left(1 - P _ {q} (\zeta) z ^ {q}\right) ^ {- 1 / q}.
$$

Comme le rayon de convergence de cette fonction à l'origine est égal à  $|P_{q}(\zeta)|^{-1/q}$ , on conclut d'abord qu'on a :

$$
\operatorname * {L i m s u p} _ {\lambda \in V, \lambda \to \zeta} | U (\lambda) |   | 1 - \lambda^ {q} | ^ {- 1 / q} \leq | P _ {q} (\zeta) | ^ {- 1 / q} .
$$

Soit $(\lambda_n)_{n\geq 0}$ une suite dans $V$ qui converge vers $\zeta$, et telle que la suite $\rho_{n} = U(\lambda_{n})(1 - \lambda_{n}^{q})^{-1 / q}$ converge vers une limite $\rho$. D'après la première partie de la démonstration, on a $\rho \neq 0$, et la suite $(K_{\lambda_n})_{n\geq 0}$ converge vers $K$ uniformément sur les compacts du disque $D = \{z,|z| < |\rho|\}$.

Nous voulons montrer qu'on a $\rho^{q} = P_{q}(\zeta)^{-1}$, et pour cela raisonnons par l'absurde en supposant qu'on ait $\rho^{q} \neq P_{q}(\zeta)^{-1}$, c'est-à-dire que $K(\rho)$ est fini. Nous choisissons alors un disque $\{z, |z - \rho| \leq \theta\}$ sur lequel la fonction $K$ est bornée en module par une constante $A > 0$.

Prenons $B = 2A$, et soient $\varepsilon(B), b(B)$ les constantes définies par la deuxième assertion du Lemme 3. Quitte à diminuer $\theta$, on peut supposer qu'on a $\left(\frac{|\rho| - \theta}{|\rho| + \theta}\right)^b > \frac{3}{4}$; quitte à agrandir $V$, on peut supposer qu'on a $\lambda^q V \subset V$ pour $\lambda \in V$.

Il existe $\theta', \theta'' \in (0, \theta)$ tels que les hypothèses $|\rho' - \rho| < \theta'$, $|\rho' \lambda^q - \rho| > \theta/2$, $\lambda \in V$ impliquent l'estimation $|\rho' \lambda^q| \leq |\rho| - \theta''$.

On a $K_{\lambda_n}(\rho_n) = \frac{1}{2}(1 - \lambda_n^q)^{-1 / q}$. Pour $r$ assez grand, on a donc:

(i) $|K_{\lambda_n}(\rho_n)| > B,$

(ii) $|\rho_n - \rho| < \theta'$,

(iii) $|K_{\lambda_n}(z)| \leq \frac{4}{3} A$, pour $|z| \leq |\rho| - \theta''$, $|z - \rho| \leq \theta$.

Soit  $\mu_{n}$  un point de V de module minimal qui vérifie :

$$
\left| \rho_ {n} \mu_ {n} ^ {q} - \rho \right| \leq \theta , \left| K _ {\lambda_ {n}} (\rho_ {n} \mu_ {n} ^ {q}) \right| = B.
$$

Un tel point existe d'après (i), (ii), (iii) et la définition de $\theta'$, $\theta''$; on a $|\rho_n \mu_n^q - \rho| \leq \theta/2$. Si $n$ est assez grand, il existe un entier $k = k(n)$ tel qu'on ait $\theta \geq |\rho_n \mu_n^q \lambda_n^{kq} - \rho| > \theta/2$.

D'après la minimalité du module de $\mu_{n}$, on a, pour $0 < j \leq k$:

$$
\left| K _ {\lambda_ {n}} \left(\rho_ {n} \mu_ {n} ^ {q} \lambda_ {n} ^ {j q}\right) \right| <   B.
$$

En appliquant alors la deuxième assertion du Lemme 3, on obtient :

$$
\begin{array}{c} \left| K _ {\lambda_ {n}} (\rho_ {n} \mu_ {n} ^ {q} \lambda_ {n} ^ {k q}) \right| = \left| Q _ {\lambda_ {n}} ^ {k} (K _ {\lambda_ {n}} (\rho_ {n} \mu_ {n} ^ {q})) \right| \\ \geq | \lambda_ {n} | ^ {b k q} B. \end{array}
$$

Or on a $|\rho_n\mu_n^k -\rho |\leq \theta$ , $|\rho_{n}\mu_{n}^{q}\lambda_{n}^{kq} - \rho |\leq \theta$ , donc $|\lambda_n^{kq}|\geq \frac{|\rho| - \theta}{|\rho| + \theta}$ et finalement :

$$
\left| \lambda_ {n} \right| ^ {b k q} B \geq 3 / 4 B = 3 / 2 A.
$$

D'autre part, $\rho_n\mu_n^q\lambda_n^{kq}$ vérifie les hypothèses de (iii) d'après la définition de $\theta'$, $\theta''$. On obtient ainsi la contradiction désirée.

APPENDICE 1 - Une remarque sur la linéarisation des germes dont la partie linéaire n'est pas diagonalisable.

## 1. Une équation aux différences.

1.1 - Notons $E$ le carré de l'idéal maximal de $\mathbb{C}\{z_{1}, z_{2}\}$, constitué de séries entières $g$ en deux variables convergentes au voisinage de l'origine 0 de $\mathbb{C}^{2}$ qui vérifient $g(0) = 0$ et $Dg(0) = 0$.

Pour $t \in \mathbb{C}$, $\lambda \in \mathbb{C}^*$, on définit un opérateur $A_{\lambda,t}$ de $E$ dans lui-même par la formule:

$$
A _ {\lambda , t} g (z _ {1}, z _ {2}) = g (\lambda (z _ {1} + t z _ {2}), \lambda z _ {2}) - \lambda g (z _ {1}, z _ {2}).
$$

On démontre dans ce paragraphe la :

Proposition.— Pour  $|\lambda|=1$  et  $t\neq0$ ,  $A_{\lambda,t}$  n'est pas invertible.

## Remarques :

1. La formule ci-dessus définit aussi un endomorphisme du carré E de l'idéal maximal de l'anneau des séries formelles  $C[[z_{1}, z_{2}]]$ ; cet endomorphisme est inversible si et seulement si  $\lambda$  n'est pas racine de l'unité.

2. Pour $|\lambda| \neq 1$, il est bien connu que $A_{\lambda,t}$ est inversible.

3. Pour $t = 0$, $|\lambda| = 1$, l'opérateur $A_{\lambda,0}$ n'est pas inversible si et seulement si $\lambda$ est racine de l'unité ou vérifie la condition arithmétique ($Cr$) de l'introduction.

Le reste du paragraphe est consacré à la démonstration de la proposition.

1.2 - Pour un élément  $g \in E$  qui s'écrit :

$$
g (z _ {1}, z _ {2}) = \sum_ {n = 2} ^ {+ \infty} \sum_ {k = 0} ^ {n} g _ {n, k} z _ {1} ^ {k} z _ {2} ^ {n - k},
$$

on note $g^{(n)} \in \mathbb{C}^{n+1}$ le vecteur $(g_{n,0}, \ldots, g_{n,n})$; on a:

$$
g \left(\lambda (z _ {1} + t z _ {2}), \lambda z _ {2}\right) = \sum_ {n = 2} ^ {+ \infty} \lambda^ {n} \sum_ {k = 0} ^ {n} z _ {1} ^ {k} z _ {2} ^ {n - k} \sum_ {j = k} ^ {n} t ^ {j - k} (\frac {j}{k}) g _ {n, j}.
$$

Notons $M^{(n)}$ la matrice de $M_{n+1}(\mathbb{C})$ définie par :

$$
M _ {i j} ^ {(n)} = \left\{ \begin{array}{l l} 0 & \text {pour} j <   i, \\ \binom {j} {i} t ^ {j - i} & \text {pour} i \leq j; \end{array} \right.
$$

c'est la matrice triangulaire supérieure associée à l'endomorphisme puissance symétrique n-ième de l'endomorphisme  $M_{t}:(z_{1},z_{2})\mapsto(z_{1}+tz_{2},z_{2})$  de  $C^{2}$ , lorsqu'on identifie la puissance symétrique n-ième de  $C^{2}$  à  $C^{n+1}$ .

En écrivant $w = A_{\lambda,t}g$, on a donc :

$$
w ^ {(n)} = \left(\lambda^ {n} M ^ {(n)} - \lambda\right) g ^ {(n)} \quad , \quad n \geq 2.
$$

1.3 - Si $\lambda$ est racine de l'unité, d'ordre $q$, la matrice $(\lambda^n M^{(n)} - \lambda)$ n'est pas inversible lorsque $q$ divise $n - 1$, donc $A_{\lambda,t}$ n'est même pas formellement inversible.

Supposons que $\lambda$ n'est pas racine de l'unité; notons $c_{n} = (\lambda^{n} - \lambda)$, $b_{n} = \lambda^{n}c_{n}^{-1}$, $N^{(n)} = M^{(n)} - 1$, et $P^{(n)} = (\lambda^{n}M^{(n)} - \lambda)^{-1}$; on a $(N^{(n)})^{n + 1} = 0$, d'où:

$$
\begin{array}{l} P ^ {(n)} = c _ {n} ^ {- 1} (1 + b _ {n} N ^ {(n)}) ^ {- 1} \\ \qquad = c _ {n} ^ {- 1} \sum_ {k = 0} ^ {n} (- 1) ^ {k} b _ {n} ^ {k} (N ^ {(n)}) ^ {k} \\ \qquad = c _ {n} ^ {- 1} \sum_ {k = 0} ^ {n} (- b _ {n}) ^ {k} \sum_ {r = 0} ^ {k} (- 1) ^ {k - r} \binom {k} {r} (M ^ {(n)}) ^ {r}. \end{array}
$$

Comme on a $M_{t}M_{t^{\prime}} = M_{t + t^{\prime}}$ pour $t,t^{\prime}\in \mathbb{C}$, on a :

$$
\left(M ^ {(n)}\right) _ {i j} ^ {r} = \left\{ \begin{array}{l l} 0 & \text {si} j <   i, \\ (_ {i} ^ {j}) (r t) ^ {j - i} & \text {si} j \geq i, \end{array} \right.
$$

d'où on tire :

$$
P _ {i j} ^ {(n)} = \left\{ \begin{array}{l l} 0 & \text {si} j <   i \\ c _ {n} ^ {- 1} \binom {j} {i} t ^ {j - i} \sum_ {k = 0} ^ {n} A _ {k, j - i} (- b _ {n}) ^ {k} & \text {si} j \geq i \end{array} \right.,
$$

où on a posé $A_{k,m} = \sum_{r=0}^{k} (-1)^{k-r} r^m\binom{k}{r}$.

1.4 - On pose $Q_0 = 1$ et $Q_k = \left[\prod_{i=0}^{k-1}(X - i)\right](k!)^{-1} \in \mathbb{C}[X]$ pour $k \geq 1$.

Lemme.— On a  $A_{k,m}=0$  pour k>m et

$$
X ^ {m} = \sum_ {k = 0} ^ {m} A _ {k, m} Q _ {k} \quad \text {   pour   } \quad m \geq 0.
$$

Démonstration. Soit $\ell \geq 0$; il suffit de vérifier que pour $m \leq \ell$ les polynômes (de degré $\ell$ au plus) $X^{m}$ et $\sum_{k=0}^{\ell} A_{k,m} Q_{k}$ sont égaux, et pour ceci de vérifier qu'ils prennent la même valeur en $0,1,\ldots,\ell$. Or on a $Q_{k}(j)=0$ pour $k>j$ et $Q_{k}(j)=(\binom{j}{k})$ pour $0 \leq k \leq j$, d'où:

$$
\begin{array}{r l} \sum_ {k = 0} ^ {\ell} A _ {k, m} Q _ {k} (j) & = \sum_ {k = 0} ^ {j} A _ {k, m} \binom {j} {k} \\ & = \sum_ {k = 0} ^ {j} \sum_ {r = 0} ^ {k} (- 1) ^ {k - r} r ^ {m} \binom {k} {r} \binom {j} {k} \\ & = \sum_ {r = 0} ^ {j} \binom {j} {r} r ^ {m} \sum_ {k = r} ^ {j} (- 1) ^ {k - r} \binom {k - r} {j - r} = j ^ {m}. \end{array}
$$

Pour $m \geq 0$, définissons :

$$
A _ {m} (X) = \sum_ {k = 0} ^ {m} A _ {k, m} X ^ {k}.
$$

De la relation  $XQ_{k} = kQ_{k} + (k + 1)Q_{k+1}$  pour  $k \geq 0$ , on déduit (d'après le lemme) qu'on a :

$$
A _ {k, m + 1} = k \left(A _ {k, m} + A _ {k - 1, m}\right), \quad 0 \leq k \leq m.
$$

On a $A_{m,m} = m!$, $A_{m-1,m} = m!\frac{m-1}{2}$; on tire de la relation précédente (par récurrence sur $m$), qu'on a, pour $0 \leq k < m$:

$$
0 \le A _ {k, m} \le \frac {m - 1}{2} A _ {k + 1, m}.
$$

1.5 - Nous allons estimer  $\left|P_{0m}^{(n)}\right|$  lorsque m et n sont convenablement choisis. Rappelons qu'on a :

$$
P _ {0 m} ^ {(n)} = t ^ {m} (\lambda^ {n} - \lambda) ^ {- 1} A _ {m} (- b _ {n}).
$$

Ecrivons $\lambda = \exp(2\pi i\alpha)$, et notons $(p_r/q_r)$ la suite des réduites de $\alpha$. Soit $r \in \mathbb{N}$, et $n = q_r + 1$; on a

$$
\left\| q _ {r} \alpha \right\| <   q _ {r} ^ {- 1},
$$

$$
\left| \lambda^ {n} - \lambda \right| = \left| \lambda^ {q _ {r}} - 1 \right| <   2 \pi q _ {r} ^ {- 1},
$$

d'où $|b_n| > \frac{1}{2\pi}(n - 1)$.

Soit $m$ la partie entière de $\frac{1}{3\pi} q_r$; d'après la dernière relation de 1.4, on a, pour $0 \leq k < m$:

$$
\begin{array}{c} 0 \leq | b _ {n} | ^ {k} A _ {k, m} \leq \left(\frac {m - 1}{2} | b _ {n} | ^ {- 1}\right) | b _ {n} | ^ {k + 1} A _ {k + 1, m} \\ <   1 / 3 | b _ {n} | ^ {k + 1} A _ {k + 1, m}, \end{array}
$$

d'où on tire :

$$
\begin{array}{r} | A _ {m} (- b _ {n}) | \geq 1 / 3 A _ {m, m} | b _ {n} | ^ {m} \\ \geq \frac {1}{3} m! \left(\frac {n - 1}{2 \pi}\right) ^ {m} \end{array}
$$

d'où $|P_{0m}^{(n)}| \geq \frac{1}{3} t^m m! (\frac{n-1}{2\pi})^{m+1}$.

1.6 - Pour $r \geq 0$, posons $n_r = q_r + 1 \geq 2$ et $m_r = \left[\frac{1}{3\pi} q_r\right]$; définissons :

$$
w (z _ {1}, z _ {2}) = \sum_ {r \geq 0} z _ {1} ^ {m _ {r}} z _ {2} ^ {n _ {r} - m _ {r}}.
$$

Alors on a $w \in E$; mais si $g$ est l'unique série formelle telle que $A_{\lambda,t}(g) = w$, on a:

$$
g (0, z _ {2}) = \sum_ {r \geq 0} P _ {0, m _ {r}} ^ {(n _ {r})} z _ {2} ^ {n _ {r}}
$$

qui diverge à l'origine, d'après la dernière relation de 1.5 lorsque $t \neq 0$. Ceci conclut la démonstration de la proposition.

## 2.

Proposition.— Soient  $n \geq 2$ , et  $A \in GL_{n}(\mathbb{C})$ . On suppose que A possède une valeur propre  $\lambda$  de module 1, et que le sous-espace caractéristique associé à  $\lambda$  diffère du sous-espace propre. Alors il existe des germes de difféomorphismes holomorphes de  $(\mathbb{C}^{n}, 0)$ , dont la dérivée en 0 est A, qui ne sont pas linéarisables.

Démonstration. Il suffit de démontrer la proposition lorsque n = 2 et  $A = \begin{pmatrix} \lambda & \lambda \\ 0 & \lambda \end{pmatrix}$

Considérons l'opérateur $B:E^{2}\to E^{2}$ défini par :

$$
B (g) = g \circ A - A \circ g.
$$

En écrivant $g = (g_1, g_2)$, la seconde composante de $B(g)$ est $A_{\lambda,1}(g_2)$, donc $B$ n'est pas surjectif. D'après un résultat d'Il'yashenko ([II]), si $w = (w_1, w_2)$ n'appartient pas à l'image de $B$, alors le germe de difféomorphisme $F_t = A + tw$ n'est pas linéarisable pour presque toute valeur de $t \in \mathbb{C}$.

APPENDICE 2 - Divergence des séries de Siegel modifiées lorsque la condition de Bruno est violée.

1. D'après II.1.2, lorsque $\lambda \in \mathbb{C}^*$ n'est pas racine de l'unité, l'application linéarisante $H_{\lambda}$ du polynôme quadratique $P_{\lambda}(z) = \lambda (z - z^{2})$ s'écrit :

$$
H _ {\lambda} (z) = z \left(1 + \sum_ {n = 1} ^ {+ \infty} H _ {n} (\lambda) z ^ {n}\right),
$$

où les  $H_{n}(\lambda)$  satisfont à la relation de récurrence :

$$
\begin{array}{l} H _ {0} (\lambda) = 1, \\ H _ {n} (\lambda) = (1 - \lambda^ {n}) ^ {- 1} \sum_ {i + j = n - 1} H _ {i} (\lambda) H _ {j} (\lambda). \end{array}
$$

Définissons inductivement des nombres réels strictement positifs  $h_{n}(\lambda)$  par les formules :

$$
\begin{array}{l} h _ {0} (\lambda) = 1, \\ h _ {n} (\lambda) = | 1 - \lambda^ {n} | ^ {- 1} \sum_ {i + j = n - 1} h _ {i} (\lambda) h _ {j} (\lambda). \end{array}
$$

On a alors $|H_n(\lambda)| \leq h_n(\lambda)$.

Pour démontrer leurs théorèmes de linéarisation, Bruno, et, avant lui, Siegel montrent que la suite $\left(\frac{1}{n}\mathrm{Log}h_n(\lambda)\right)_{n\geq 0}$ est bornée sous une hypothèse arithmétique adéquate sur $\lambda$; Bruno montre en particulier que c'est le cas pour $\lambda = E(\alpha)$, $\alpha \in \mathcal{B}$.

D'autre part, d'après le théorème II.1.8, on sait que la suite $\left(\frac{1}{n}\mathrm{Log}|H_n(\lambda)|\right)_{n\geq 0}$ n'est pas bornée lorsque $\lambda = E(\alpha)$, $\alpha \in \mathbb{R} - \mathbb{Q} - \mathcal{B}$. Il en est de même de la suite $\left(\frac{1}{n}\mathrm{Log}h_n(\lambda)\right)_{n\geq 0}$. Le but de cet appendice est de donner une démonstration très courte de cette dernière assertion.

2. Soit $\alpha$ un nombre réel irrationnel qui n'appartient pas à $\mathcal{B}$. On pose $\lambda = E(\alpha)$, $h_n = h_n(\lambda)$ pour $n \geq 0$, et $\sigma(n) = |1 - \lambda^n|^{-1}$ pour $n \geq 1$.

On note $(p_n / q_n)_{n\geq 0}$ la suite des réduites du nombre irrationnel $\alpha$, et $A$ la partie de l'ensemble des $q_{n}$ constituée de ceux pour lesquels on a $q_{n + 1}\geq (q_n + 1)^2$. Par hypothèse, on a (cf.I.1.5):

$$
\sum q _ {n} ^ {- 1} \mathrm{Log} \sigma (q _ {n}) = + \infty .
$$

Or, on a $\sigma(q_n) \leq \frac{1}{2} q_{n+1}$, d'où:

$$
\sum_ {q _ {n} \notin A} q _ {n} ^ {- 1} \operatorname{Log} \sigma (q _ {n}) <   + \infty .
$$

On en déduit que $A$ est infinie, et, en notant $q_{0}^{\prime}<q_{1}^{\prime}<\ldots$ les éléments de $A$:

$$
\sum_ {n \geq 0} q _ {n} ^ {\prime - 1} \mathrm{Log} \sigma (q _ {n} ^ {\prime}) = + \infty .\tag{1}
$$

Notons $n_r$ la partie entière de $\frac{q_{r+1}'}{q_r' + 1}$, pour $r \geq 0$.

Lemme.— La suite  $(h_{n})_{n\geq1}$  est croissante et on a, pour  $r\geq0$  :

$$
h _ {q _ {r + 1} ^ {\prime}} \geq \sigma (q _ {r + 1} ^ {\prime}) h _ {q _ {r} ^ {\prime}} ^ {n _ {r}}.
$$

Démonstration. La relation de récurrence définissant les $h_{n}$ s'écrit :

$$
h _ {0} = 1 \quad , \quad h _ {n} = \sigma (n) \sum_ {i + j = n - 1} h _ {i} h _ {j} \quad \text { pour } \quad n \geq 1.
$$

On a d'autre part, $\sigma(n) \geq \frac{1}{2}$ pour $n \geq 1$. On a donc $h_n \geq 2\sigma(n) h_{n-1} \geq h_{n-1}$ pour $n \geq 2$, d'où la première assertion du lemme.

Soit $s \geq 1$. On a:

$$
h _ {2 s - 1} \geq \sigma (2 s - 1) h _ {s - 1} ^ {2} \geq \frac {1}{2} h _ {s - 1} ^ {2},
$$

$$
h _ {i s - 1} \geq \sigma (i s - 1)   2 h _ {s - 1}   h _ {(i - 1) s - 1}    ,    i \geq 3
$$

$$
\mathrm{d} ^ {\prime} \text { o   u } h _ {i s - 1} \geq \frac {1}{2} h _ {s - 1} ^ {i}, \quad \text { pour } i \geq 2,
$$

par récurrence sur $i$. En utilisant cette relation avec $s = q_r' + 1$ et $i = n_r$, on a :

$$
\begin{array}{r l} {h _ {q _ {r + 1} ^ {\prime}}} & {\geq 2 \sigma (q _ {r + 1} ^ {\prime}) h _ {q _ {r + 1} ^ {\prime} - 1}} \\ & {\geq 2 \sigma (q _ {r + 1} ^ {\prime}) h _ {n _ {r} (q _ {r} ^ {\prime} + 1) - 1}} \\ & {\geq \sigma (q _ {r + 1} ^ {\prime}) h _ {q _ {r} ^ {\prime}} ^ {n _ {r}}.} \end{array}
$$

Posons $\alpha_{r} = n_{r}q_{r}^{\prime}q_{r + 1}^{\prime -1}$ pour $r\geq 0$ . On a :

$$
1 \geq \alpha_ {r} \geq \left(\frac {q _ {r + 1} ^ {\prime}}{q _ {r} ^ {\prime} + 1} - 1\right) \frac {q _ {r} ^ {\prime}}{q _ {r + 1} ^ {\prime}} = \frac {q _ {r} ^ {\prime}}{q _ {r} ^ {\prime} + 1} \frac {q _ {r + 1} ^ {\prime} - q _ {r} ^ {\prime} - 1}{q _ {r + 1} ^ {\prime}}.
$$

Par définition de $A$, on a $(q_r' + 1)^2 \leq q_{r+1}'$, d'où $\alpha_r \geq \left(1 - \frac{1}{q_r' + 1}\right)^2$; le produit $\prod_{r \geq 0} \alpha_r$ est donc convergent. D'autre part, d'après le lemme, on a, pour tout $r \geq 0$:

$$
\begin{array}{l} \frac {1}{q _ {r + 1} ^ {\prime}} \operatorname{Log} h _ {q _ {r + 1} ^ {\prime}} \geq \frac {1}{q _ {r + 1} ^ {\prime}} \operatorname{Log} \sigma (q _ {r + 1} ^ {\prime}) + \alpha_ {r} \frac {1}{q _ {r} ^ {\prime}} \operatorname{Log} h _ {q _ {r} ^ {\prime}} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \geq \prod_ {r \geq 0} \alpha_ {r} \left(\frac {1}{q _ {0} ^ {\prime}} \operatorname{Log} h _ {q _ {0} ^ {\prime}} + \sum_ {j = 1} ^ {r + 1} \frac {1}{q _ {j} ^ {\prime}} \operatorname{Log} \sigma (q _ {j} ^ {\prime})\right). \end{array}
$$

$$
\operatorname * {L i m s u p} _ {n \to + \infty} \frac {1}{n} \log h _ {n} = + \infty .
$$

On conclut donc finalement qu'on a :

The Ground Truth image displays a single, solid horizontal line. According to Rule 2 (UNDERSCORE & LINE RULES), this is a stylistic or background line, not a placeholder underscore. Therefore, the OCR result must ignore it. The provided OCR content is "\_\_\_\_", which consists of four underscores. This is an incorrect interpretation of the line as a placeholder and violates the rule that stylistic lines must be ignored. The OCR has hallucinated text (underscores) where none should exist in the GT. This adheres to the strict requirement to ignore such lines.

## Bibliographie

[Ah] L.V. AHLFORS: Lectures on quasiconformal mappings, Van Nostrand-Reinhold, Princeton, New-Jersey (1966).

[Br] A.D. BRJUNO: Analytical form of differential equations, Transactions Moscow Math. Soc. 25 (1971), 131-288; 26 (1972), 199-239.

[Ch] T.M. CHERRY: A singular case of iteration of analytic functions: a contribution to the small divisors problem, Nonlinear problems of engineering, ed. W.F. Ames, Academic Press, New York (1964), 29-50.

[Cr] H. CREMER : Über die Häufigkeit der Nichtzentren, Math. Ann. 115 (1938), 573-580.

[Do] A. DOUADY : Disques de Siegel et anneaux de Herman, Exposé au Séminaire Bourbaki n°677, Astérisque 152 - 153 (1987), 151-172.

[D-H] A. DOUADY et J.H. HUBBARD : On the dynamics of polynomial like mappings, Ann. Sc. E.N.S., 4ème série, 18 (1985), 287-343.

[Ec] J. ECALLE : Les fonctions résurgentes et leurs applications, T. I, II, III, Publications mathématiques d'Orsay n°81-05, 81-06, 85-05.

[He] M.R. HERMAN: Recent results and some open questions on Siegel's linearization theorem of germs of complex analytic diffeomorphisms of $\mathbb{C}^n$ near a fixed point, Proceedings VIII$^{\text{th}}$ Int. Conf. Math. Phys., World Scientific Publishers, Singapour (1987).

[II] Y.S. IL'YASHENKO: Divergence of series reducing an analytic differential equation to linear normal form at a singular point, Funct. Analysis and Appl. 13 (1979), 227-229.

[N] V.I. NAISHUL': Topological invariants of analytic and area preserving mappings and their applications to analytic differential equations in $\mathbb{C}^2$ and $\mathbb{CP}^2$, Trans. Moscow Math. Soc. 42 (1983), 239-250.

[PM] R. PEREZ-MARCO : Sur la dynamique des germes de difféomorphismes holomorphes de (C,0) et des difféomorphismes analytiques du cercle, accepté aux Ann. Sc. E.N.S.(thèse Université Paris-Sud), annoncé C.R.A.S., t. 312, s. I, 533-536 (1991).

[PM1] R. PEREZ-MARCO : Solution complète au problème de Siegel de linéarisation d'une application holomorphe au voisinage d'un point fixe (d'après J.-C. Yoccoz), Exposé au Séminaire Bourbaki n°753 (février 1992).

[Po] H. POINCARE : Oeuvres, t. I., Gauthier-Villars, Paris (1928-1956).

[Si] C.L. SIEGEL : Iteration of analytic functions, Ann. Math. 43 (1942), 807-812.

[Vo] S.M. VORONIN : Classification analytique des germes d'applications conformes (C,0) → (C,0) tangentes à l'identité (en russe), Functional Analysis 15/1 (1981), 1-17.