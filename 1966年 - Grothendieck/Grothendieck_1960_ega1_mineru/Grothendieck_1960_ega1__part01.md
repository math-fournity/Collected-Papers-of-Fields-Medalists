ALEXANDER GROTHENDIECK

Éléments de géométrie algébrique : I. Le langage des schémas

Publications mathématiques de l'I.H.É.S., tome 4 (1960), p. 5-228

&lt;http://www.numdam.org/item?id=PMIHES_1960_4_5_0&gt;

© Publications mathématiques de l'I.H.É.S., 1960, tous droits réservés.

L'accès aux archives de la revue « Publications mathématiques de l'I.H.É.S. » (http://www.ihes.fr/IHES/Publications/Publications.html) implique l'accord avec les conditions générales d'utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou impression systématique est constitutive d'une infraction pénale. Toute copie ou impression de ce fichier doit contenir la présente mention de copyright.

INSTITUT
DES HAUTES ÉTUDES
SCIENTIFIQUES

![](images/page_1_image_1.jpg)

# ÉLÉMENTS DE GÉOMÉTRIE ALGÉBRIQUE

par A. GROTHENDIECK
Rédigés avec la collaboration de J. DIEUDONNÉ

I
LE LANGUAGE DES SCHÉMAS

1960

PUBLICATIONS MATHÉMATIQUES, N° 4
5, ROND-POINT BUGEAUD — PARIS (XVI$^{e}$)

$^{1re}$ édition $\ldots\ldots3^{e}$ trimestre 1960
TOUS DROITS
réservés pour tous pays

## DÉPOT LÉGAL

© 1960, Institut des Hautes Études Scientifiques

# INTRODUCTION

A Oscar Zariski et André Weil.

Ce mémoire, et les nombreux autres qui doivent lui faire suite, sont destinés à former un traité sur les fondements de la Géométrie algébrique. Ils ne présupposent en principe aucune connaissance particulière de cette discipline, et il s'est même avéré qu'une telle connaissance, malgré ses avantages évidents, pouvait parfois (par l'habitude trop exclusive du point de vue birationnel qu'elle implique) être nuisible à celui qui désire se familiariser avec le point de vue et les techniques exposés ici. Par contre, nous supposerons que le lecteur a une bonne connaissance des sujets suivants :

a) L'Algèbre commutative, telle qu'elle est exposée par exemple dans les volumes en cours de préparation des Éléments de N. Bourbaki (et, en attendant la parution de ces volumes, dans Samuel-Zariski [13] et Samuel [11], [12]).

b) L'Algèbre homologique, pour laquelle nous renvoyons à Cartan-Eilenberg [2] (cité (M)) et Godement [4] (cité (G)), ainsi qu'à l'article récent de A. Grothendieck [6] (cité (T)).

c) La Théorie des faisceaux, où nos principales références seront (G) et (T) ; cette dernière théorie fournit le langage indispensable pour interpréter en termes « géométriques » les notions essentielles de l'Algèbre commutative, et pour les « globaliser ».

d) Enfin, il sera utile au lecteur d'avoir une certaine familiarité avec le langage fonctoriel, qui sera constamment employé dans ce Traité, et pour lequel le lecteur pourra consulter (M), (G) et surtout (T) ; les principes de ce langage et les principaux résultats de la théorie générale des foncteurs seront exposés plus en détail dans un ouvrage en cours de préparation par les auteurs de ce Traité.

## \* $\ast$

Ce n'est pas le lieu, dans cette Introduction, de donner une description plus ou moins sommaire du point de vue des « schémas » en Géométrie algébrique, ni la longue liste des raisons qui ont rendu nécessaire son adoption, et en particulier l'acceptation systématique d'éléments nilpotents dans les anneaux locaux des « variétés » que nous considérons (ce qui, nécessairement, relègue au second plan la notion d'application rationnelle, au profit de celle d'application régulière ou « morphisme »). Le présent Traité vise précisément à développer de façon systématique le langage des « schémas » et démontrera, nous l'espérons, sa nécessité. Encore qu'il serait facile de le faire, nous

n'essayerons pas non plus de donner ici une introduction « intuitive » aux notions développées dans le chapitre premier. Le lecteur qui désirerait avoir un aperçu préliminaire des matières de ce Traité pourra se reporter à la conférence faite par A. Grothendieck au Congrès international des Mathématiciens à Edinburgh en 1958 [7], et à l'exposé [8] du même auteur. Le travail [14] (cité (FAC)) de J.-P. Serre peut aussi être considéré comme un exposé intermédiaire entre le point de vue classique et le point de vue des schémas en Géométrie algébrique, et à ce titre, sa lecture peut constituer une excellente préparation à celle de nos Éléments.

## \* $\ast$

A titre informatif, nous donnons ci-dessous le plan général prévu pour ce Traité, d'ailleurs sujet à modifications ultérieures, surtout en ce qui concerne les derniers chapitres :

Chapitre Premier. — Le langage des schémas.

— II. — Étude globale élémentaire de quelques classes de morphismes.

— III. — Cohomologie des faisceaux algébriques cohérents. Applications.

— IV. — Étude locale des morphismes.

— V. — Procédés élémentaires de construction de schémas.

— VI. — Technique de descente. Méthode générale de construction des schémas.

— VII. — Schémas de groupes, espaces fibrés principaux.

— VIII. — Étude différentielle des espaces fibrés.

— IX. — Le groupe fondamental.

— X. — Résidus et dualité.

— XI. — Théories d'intersection, classes de Chern, théorème de Riemann-Roch.

— XII. — Schémas abéliens et schémas de Picard.

— XIII. — Cohomologie de Weil.

En principe, tous les chapitres sont considérés comme ouverts, et des paragraphes supplémentaires pourront toujours leur être ajoutés ultérieurement ; de tels paragraphes paraîtront en fascicules séparés, pour diminuer les inconvénients du mode de publication adopté. Lorsqu'un tel paragraphe est prévu ou en préparation au moment de la publication d'un chapitre, il sera mentionné dans le sommaire dudit chapitre, même si en raison de certains ordres d'urgence sa publication effective devait être nettement postérieure. Pour la commodité du lecteur, nous donnons dans un « Chapitre 0 » des compléments divers d'Algèbre commutative, d'Algèbre homologique, de Théorie des faisceaux, utilisés au cours des chapitres de ce Traité, qui sont plus ou moins bien connus, mais pour lesquels il n'a pas été possible de donner des références commodes. Il est recommandé au lecteur de ne se reporter au chapitre 0 qu'en cours de lecture du Traité proprement dit, et dans la mesure où les résultats auxquels nous référons ne lui sont pas

suffisamment familiers. Nous pensons d'ailleurs que de cette façon, la lecture de ce Traité pourra être pour le débutant une bonne méthode lui permettant de se familiariser avec l'Algèbre commutative et l'Algèbre homologique, dont l'étude, lorsqu'elle ne s'accompagne pas d'applications tangibles, est jugée fastidieuse, voire déprimante, par un assez grand nombre.

## \* $\ast$

Il est hors de notre compétence de donner dans cette Introduction un aperçu historique, même sommaire, des notions et résultats exposés. Le texte ne contiendra que des références jugées particulièrement utiles pour sa compréhension, et nous n'indiquerons l'origine que des résultats les plus importants. Formellement du moins, les sujets traités dans notre ouvrage sont assez neufs, ce qui expliquera la rareté des références faites aux Pères de la Géométrie algébrique du xix$^{e}$ siècle et du début du xx$^{e}$ siècle, dont nous ne connaissons les travaux que par oui-dire. Il convient cependant de dire quelques mots ici sur les ouvrages qui ont le plus directement influencé les auteurs et contribué au développement du point de vue des schémas. Il faut en tout premier lieu citer le travail fondamental (FAC) de J.-P. Serre, qui a servi d'introduction à la Géométrie algébrique pour plus d'un jeune adepte (dont l'un des auteurs du présent Traité), rebuté par l'aridité des classiques Foundations de A. Weil [18]. C'est là qu'il est démontré pour la première fois que la « topologie de Zariski » d'une variété algébrique « abstraite » est parfaitement appropriée pour lui appliquer certaines techniques de la Topologie algébrique et donner lieu notamment à une théorie cohomologique. De plus, la définition d'une variété algébrique qui y est donnée est celle qui se prête le plus naturellement à l'extension de cette notion que nous développons ici (1). Serre avait d'ailleurs remarqué lui-même que la théorie cohomologique des variétés algébriques affines pouvait se transcrire sans difficulté en remplaçant les algèbres affines sur un corps par des anneaux commutatifs quelconques. Les chapitres I et II de ce Traité et les deux premiers paragraphes du chapitre III peuvent donc être considérés, pour l'essentiel, comme des transpositions faciles, dans ce cadre élargi, des résultats principaux de (FAC) et d'un article ultérieur du même auteur [15]. Nous avons aussi retiré grand profit du Séminaire de Géométrie algébrique de C. Chevalley [1] ; en particulier, l'usage systématique des « ensembles constructibles » introduits par lui, s'est révélé fort utile en théorie des schémas (cf. chap. IV). Nous lui avons aussi emprunté l'étude des morphismes du point

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Ainsi que J.-P. Serre nous l'a signalé, il convient de noter que l'idée de définir la structure de variété par la donnée d'un faisceau d'anneaux est due à H. Cartan, qui a pris cette idée comme point de départ de sa théorie des espaces analytiques. Bien entendu, tout comme en Géométrie algébrique, il importerait, en « Géométrie analytique », de donner droit de cité aux éléments nilpotents dans les anneaux locaux des espaces analytiques. Cette extension de la définition de H. Cartan et J.-P. Serre a été récemment abordée par H. Grauert [5], et il y a lieu d'espérer qu'un exposé systématique de Géométrie analytique dans ce cadre général verra bientôt le jour. Il est d'ailleurs évident que les notions et techniques développées dans ce Traité gardent un sens en Géométrie analytique, bien qu'il faille s'attendre à des difficultés techniques plus considérables dans cette dernière théorie. On peut prévoir que la Géométrie algébrique, par la simplicité de ses méthodes, pourra servir comme une sorte de modèle formel pour de futurs développements dans la théorie des espaces analytiques.</span></small>

de vue de la dimension (chap. IV), qui se transcrit sans changement notable dans le cadre des schémas. Il convient de noter par ailleurs que la notion de « schémas d'anneaux locaux », introduite par Chevalley, se prête naturellement à une extension de la Géométrie algébrique (n'ayant pas cependant toute la souplesse et la généralité que nous entendons lui donner ici) ; pour les rapports entre cette notion et notre théorie, voir chapitre premier, § 8. Une telle extension a été développée par M. Nagata dans une série de mémoires [9] contenant de nombreux résultats spéciaux concernant la Géométrie algébrique sur les anneaux de Dedekind (1).

$$
\ast \ast
$$

Enfin, il va sans dire qu'un livre sur la Géométrie algébrique, et surtout un livre portant sur les fondements, est nécessairement influencé, ne serait-ce que par personnes interposées, par des mathématiciens tels que O. Zariski et A. Weil. En particulier, la Théorie des fonctions holomorphes de Zariski [20], convenablement assouplie grâce aux méthodes cohomologiques et complétée par un théorème d'existence (chap. III, §§ 4 et 5) est (avec la technique de descente exposée au chap. VI) un des principaux outils employés dans ce Traité, et nous semble un des plus puissants dont on dispose en Géométrie algébrique.

La technique générale dans laquelle elle s'insère peut être esquissée de la façon suivante (un exemple typique en sera fourni au chap. IX, dans l'étude du groupe fondamental). On a un morphisme propre (chap. II) $f: \mathbf{X} \to \mathbf{Y}$ d'une variété algébrique dans une autre (plus généralement, d'un schéma dans un autre) qu'on veut étudier au voisinage d'un point $y \in \mathbf{Y}$, en vue de résoudre un problème P relatif à un voisinage de $y$. On opère par étapes successives :

$^{1}$  On peut supposer Y affine, de sorte que X devient un schéma défini sur l'anneau affine A de Y, et on peut même remplacer A par l'anneau local de y. Cette réduction est toujours facile en pratique (chap. V) et nous ramène au cas où A est un anneau local.

2° On étudie le problème envisagé lorsque A est un anneau local artinien. Pour qu'il garde effectivement un sens lorsque A n'est pas supposé intègre, il y a lieu parfois de reformuler le problème P, et il apparaît que l'on obtient souvent ainsi une meilleure compréhension du problème, de nature « infinitésimale » à ce stade.

$3^{\circ}$ La théorie des schémas formels (chap. III, §§ 3, 4 et 5) permet de passer du cas d'un anneau artinien au cas d'un anneau local complet.

$4^{\circ}$ Enfin, si A est un anneau local quelconque, la considération de « sections multiformes » sur des schémas convenables sur X, approchant une section « formelle » donnée (chap. IV) permettra souvent de passer d'un résultat connu pour le schéma

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Parmi les travaux qui se rapprochent de notre point de vue en Géométrie algébrique, signalons l'important travail de E. Kähler [22], et une Note récente de Chow et Igusa [3], qui reprennent dans le cadre de la théorie de Nagata-Chevalley certains résultats de (FAC) et donnent aussi une formule de Künneth.</span></small>

déduit de X par extension des scalaires au complété de A, à un résultat analogue pour une extension finie assez simple (par exemple non ramifiée) de A.

Cette esquisse montre l'importance de l'étude systématique des schémas définis sur un anneau artinien A. Le point de vue de Serre dans sa formulation de la théorie du corps de classes local, et des travaux récents de Greenberg, semblent suggérer qu'une telle étude pourrait être entreprise en attachant fonctoriellement à un tel schéma X un schéma X' sur le corps résiduel k de A (supposé parfait) de dimension égale (dans les cas favorables) à n dim X, où n est la longueur de A.

Quant à l'influence de A. Weil, qu'il nous suffise de dire que c'est la nécessité de développer l'outillage nécessaire pour formuler avec toute la généralité voulue la définition de la « cohomologie de Weil » et pour aborder la démonstration (1) de toutes les propriétés formelles nécessaires pour établir ses célèbres conjectures en Géométrie diophantienne [19], qui a été une des principales motivations de la rédaction du présent Traité, au même titre que le désir de trouver le cadre naturel des notions et méthodes usuelles en Géométrie algébrique, et de donner aux auteurs l'occasion de comprendre lesdites notions et techniques.

## \* $\ast$

Pour terminer, nous croyons utile de prévenir les lecteurs que, tout comme les auteurs eux-mêmes, ils auront sans doute quelque difficulté avant de s'accoutumer au langage des schémas, et de se convaincre que les constructions habituelles que suggère l'intuition géométrique peuvent se transcrire, essentiellement d'une seule façon raisonnable, dans ce langage. Comme dans beaucoup de parties de la Mathématique moderne, l'intuition première s'éloigne de plus en plus, en apparence, du langage propre à l'exprimer avec toute la précision et la généralité voulues. En l'occurrence, la difficulté psychologique tient à la nécessité de transporter aux objets d'une catégorie déjà assez différente de la catégorie des ensembles (à savoir la catégorie des préschémas, ou la catégorie des préschémas sur un préschéma donné) des notions familières pour les ensembles : produits cartésiens, lois de groupe, d'anneau, de module, fibrés, fibrés principaux homogènes, etc. Il sera sans doute difficile au mathématicien, dans l'avenir, de se dérober à ce nouvel effort d'abstraction, peut-être assez minime, somme toute, en comparaison de celui fourni par nos pères, se familiarisant avec la Théorie des Ensembles.

## \* $\ast$

Les références seront données suivant le système décimal ; par exemple, dans III, 4.9.3, le chiffre III indique le chapitre, le chiffre 4 le paragraphe, le chiffre 9 la section du paragraphe. A l'intérieur du même chapitre, on supprimera la mention du chapitre.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Pour éviter tout malentendu, précisons que cette tâche vient à peine d'être entreprise au moment où cette Introduction est écrite, et n'a donc pas encore abouti à la démonstration des conjectures de Weil.</span></small>

The OCR result should be empty, as the image contains only a stylistic horizontal line which must be ignored according to Rule 2. No text or placeholder characters should be output.

# CHAPITRE O

## PRÉLIMINAIRES

## § 1. ANNEAUX DE FRACTIONS

## 1.0. Anneaux et algèbres.

(1.0.1) Tous les anneaux considérés dans ce Traité posséderont un élément unité ; tous les modules sur un tel anneau seront supposés unitaires ; les homomorphismes d'anneaux seront toujours supposés transformer l'élément unité en élément unité ; sauf mention expresse du contraire, un sous-anneau d'un anneau A sera supposé contenir l'élément unité de A. Nous considérerons surtout des anneaux commutatifs, et lorsque nous parlerons d'anneau sans préciser, il sera sous-entendu qu'il s'agit d'un anneau commutatif. Si A est un anneau non nécessairement commutatif, par A-module nous entendrons toujours un module à gauche, sauf mention expresse du contraire.

(1.0.2) Soient A, B deux anneaux non nécessairement commutatifs, $\varphi: A \to B$ un homomorphisme. Tout B-module à gauche (resp. à droite) M peut être muni d'une structure de A-module à gauche (resp. à droite) en posant $a.m = \varphi(a).m$ (resp. $m.a = m.\varphi(a)$); lorsqu'il sera nécessaire de distinguer sur M les structures de A-module et de B-module, nous désignerons par $\mathbf{M}_{[\varphi]}$ le A-module à gauche (resp. à droite) ainsi défini. Si L est un A-module, un homomorphisme $u: L \to M_{[\varphi]}$ est donc un homomorphisme de groupes commutatifs tel que $u(a.x) = \varphi(a).u(x)$ pour $a \in A$, $x \in L$; on dira aussi que c'est un $\varphi$-homomorphisme $L \to M$, et que le couple $(\varphi,u)$ (ou, par abus de langage, $u$) est un di-homomorphisme de (A, L) dans (B, M). Les couples (A, L) formés d'un anneau A et d'un A-module L forment donc une catégorie pour laquelle les morphismes sont les di-homomorphismes.

(1.0.3) Sous les hypothèses de (1.0.2), si J est un idéal à gauche (resp. à droite) de A, nous noterons BJ (resp. JB) l'idéal à gauche (resp. à droite) Bφ(J) (resp. φ(J)B) de B engendré par φ(J); c'est aussi l'image de l'homomorphisme canonique B⊗AJ→B (resp. J⊗A B→B) de B-modules à gauche (resp. à droite).

(1.0.4) Si A est un anneau (commutatif), B un anneau non nécessairement commutatif, la donnée d'une structure de A-algèbre sur B équivaut à la donnée d'un homomorphisme d'anneaux $\varphi: A \to B$ tel que $\varphi(A)$ soit contenu dans le centre de B. Pour tout idéal $\mathfrak{J}$ de A, $\mathfrak{J}B = B\mathfrak{J}$ est alors un idéal bilatère de B, et pour tout B-module M, $\mathfrak{J}M$ est alors un B-module égal à (B$\mathfrak{J}$)M.

(1.0.5) Nous ne reviendrons pas sur les notions de module de type fini et d'algèbre (commutative) de type fini ; dire qu'un A-module M est de type fini signifie qu'il existe

une suite exacte  $A^{p}\rightarrow M\rightarrow o$ . On dit qu'un A-module M admet une présentation finie s'il est isomorphe au conoyau d'un homomorphisme  $A^{p}\rightarrow A^{q}$ , autrement dit s'il existe une suite exacte  $A^{p}\rightarrow A^{q}\rightarrow M\rightarrow o$ . On notera que sur un anneau noethérien A, tout A-module de type fini admet une présentation finie.

Rappelons qu'une A-algèbre B est dite entière sur A si tout élément de B est racine dans B d'un polynôme unitaire à coefficients dans A ; il revient au même de dire que tout élément de B est contenu dans une sous-algèbre de B qui est un A-module de type fini. Lorsqu'il en est ainsi, et que B est commutative, la sous-algèbre de B engendrée par une partie finie de B est un A-module de type fini ; pour que l'algèbre commutative B soit entière et de type fini sur A, il faut et il suffit donc que B soit un A-module de type fini ; on dit alors aussi que B est une A-algèbre entière finie (ou simplement finie si aucune confusion n'en résulte). On observera que dans ces définitions, on ne suppose pas que l'homomorphisme A→B définissant la structure de A-algèbre soit injectif.

(1.0.6) Un anneau intègre est un anneau dans lequel le produit d'une famille finie d'éléments ≠ o est ≠ o ; il revient au même de dire que dans un tel anneau on a o ≠ i et le produit de deux éléments ≠ o est non nul. Un idéal premier d'un anneau A est un idéal p tel que A/p soit intègre ; cela entraîne donc p ≠ A. Pour qu'un anneau A ait au moins un idéal premier, il faut et il suffit que A ≠ {o}.

(1.0.7) Un anneau local est un anneau A dans lequel il existe un seul idéal maximal, qui est alors le complémentaire des éléments inversibles et contient tous les idéaux $\neq$ A. Si A et B sont deux anneaux locaux, $m$ et $n$ leurs idéaux maximaux respectifs, on dit qu'un homomorphisme $\varphi: A \to B$ est local si $\varphi(m) \subset n$ (ou, ce qui revient au même, si $\varphi^{-1}(n) = m$). Par passage aux quotients, un tel homomorphisme définit alors un monomorphisme du corps résiduel A/m dans le corps résiduel B/n. Le composé de deux homomorphismes locaux est un homomorphisme local.

## 1.1. Racine d'un idéal. Nilradical et radical d'un anneau.

(1.1.1) Soit a un idéal d'un anneau A ; la racine de a, notée r(a), est l'ensemble des  $x \in A$  tels que  $x^{n} \in a$  pour un entier n > o au moins; c'est un idéal contenant a. On a  $\mathfrak{r}(\mathfrak{r}(a)) = \mathfrak{r}(a)$ ; la relation  $a \subset b$  entraîne  $\mathfrak{r}(a) \subset \mathfrak{r}(b)$ ; la racine d'une intersection finie d'idéaux est l'intersection de leurs racines. Si  $\varphi$  est un homomorphisme d'un anneau A' dans A, on a  $\mathfrak{r}(\varphi^{-1}(a)) = \varphi^{-1}(\mathfrak{r}(a))$  pour tout idéal  $a \subset A$ . Pour qu'un idéal soit racine d'un idéal, il faut et il suffit qu'il soit intersection d'idéaux premiers. La racine d'un idéal a est l'intersection des idéaux premiers minimaux parmi ceux qui contiennent a ; si A est noethérien, ces idéaux premiers minimaux sont en nombre fini.

La racine de l'idéal (o) est encore appelée le nilradical de A ; c'est l'ensemble $\mathfrak{N}$ des éléments nilpotents de A. On dit que l'anneau A est réduit si $\mathfrak{N} = (o)$ ; pour tout anneau A, le quotient A/$\mathfrak{N}$ de A par son nilradical est un anneau réduit.

(1.1.2) Rappelons que le radical $\mathfrak{R}(A)$ d'un anneau A (non nécessairement commutatif) est l'intersection des idéaux à gauche maximaux de A (et aussi l'intersection des idéaux à droite maximaux). Le radical de A/$\mathfrak{R}(A)$ est (o).

## 1.2. Modules et anneaux de fractions.

(1.2.1) On dit qu'une partie S d'un anneau A est multiplicative si  $i \in S$  et si le produit de deux éléments de S est dans S. Les exemples qui seront les plus importants pour la suite sont :  $r^{0}$  l'ensemble  $S_{f}$  des puissances  $f^{n} (n \geqslant 0)$  d'un élément  $f \in A$ ;  $2^{0}$  le complémentaire A—p d'un idéal premier p de A.

(1.2.2) Soient S une partie multiplicative d'un anneau A, M un A-module; dans l'ensemble  $M \times S$ , la relation entre couples  $(m_{1}, s_{1}), (m_{2}, s_{2})$ :

$$
\ll \text {   il   existe   } s \in \mathbf {S} \text {   tel   que   } s (s _ {1} m _ {2} - s _ {2} m _ {1}) = 0 \gg
$$

est une relation d'équivalence. On désigne par S$^{-1}$M l'ensemble quotient de M×S par cette relation, par m/s l'image canonique dans S$^{-1}$M du couple (m, s) ; on appelle application canonique de M dans S$^{-1}$M l'application i$_{M}^{S}$: m→m/I (aussi notée i$^{S}$). Cette application n'est en général ni injective ni surjective ; son noyau est l'ensemble des m∈M tels qu'il existe un s∈S pour lequel sm=0.

Dans S $^{-1}$ M on définit une loi de groupe additif en prenant

$$
(m _ {1} / s _ {1}) + (m _ {2} / s _ {2}) = (s _ {2} m _ {1} + s _ {1} m _ {2}) / (s _ {1} s _ {2})
$$

(on vérifie que c'est bien indépendant des expressions des éléments de S$^{-1}$M considérés). Sur S$^{-1}$A on définit en outre une loi multiplicative en prenant $(a_1/s_1)(a_2/s_2)=(a_1a_2)/(s_1s_2)$, et enfin une loi externe sur S$^{-1}$M, ayant S$^{-1}$A comme ensemble d'opérateurs, en posant $(a/s)(m/s')=(am)/(ss')$. On vérifie ainsi que S$^{-1}$A est muni d'une structure d'anneau (dit anneau de fractions de A à dénominateurs dans S) et S$^{-1}$M d'une structure de S$^{-1}$A-module (dit module des fractions de M à dénominateurs dans S); pour tout $s\in$S, $s/1$ est inversible dans S$^{-1}$A, son inverse étant $1/s$. L'application canonique $i_A^S$ (resp. $i_M^S$) est un homomorphisme d'anneaux (resp. un homomorphisme de A-modules, S$^{-1}$M étant considéré comme A-module au moyen de l'homomorphisme $i_A^S: A\to S^{-1}A$).

(1.2.3) Si  $S_{f}=\{f^{n}\}_{n\geqslant0}$  pour un  $f\in A$, on écrit  $A_{f}$  et  $M_{f}$  au lieu de  $S_{f}^{-1}A$  et  $S_{f}^{-1}M$; quand  $A_{f}$  est considéré comme algèbre sur A, on peut écrire  $A_{f}=A[I/f]$.  $A_{f}$  est isomorphe à l'algèbre quotient  $A[T]/(fT-1)A[T]$. Lorsque  $f=I$,  $A_{f}$  et  $M_{f}$  s'identifient canoniquement à A et M; si f est nilpotent,  $A_{f}$  et  $M_{f}$  sont réduits à o.

Lorsque $S = A - p$, où $p$ est un idéal premier de $A$, on écrit $A_p$ et $M_p$ au lieu de $S^{-1}A$ et $S^{-1}M$; $A_p$ est un anneau local dont l'idéal maximal $q$ est engendré par $i_A^S(p)$, et on a $(i_A^S)^{-1}(q) = p$; par passage aux quotients, $i_A^S$ donne un monomorphisme de l'anneau intègre $A/p$ dans le corps $A_p/q$, qui s'identifie au corps des fractions de $A/p$.

(1.2.4) L'anneau de fractions  $S^{-1}A$  et l'homomorphisme canonique  $i_{A}^{S}$  sont solution d'un problème d'application universelle : tout homomorphisme u de A dans un anneau B tel que  $u(S)$  se compose d'éléments inversibles dans B se factorise d'une seule manière

$$
u: \mathrm{A} \rightarrow \mathrm{S} ^ {- 1} \mathrm{A} \rightarrow \mathrm{B}   i _ {\mathrm{A}} ^ {\mathrm{S}} \quad u ^ {*}
$$

où $u^*$ est un homomorphisme d'anneaux. Sous les mêmes hypothèses, soient M un A-module, N un B-module, $v: \mathbf{M} \to \mathbf{N}$ un homomorphisme de A-modules (pour la structure de B-module sur N définie par $u: \mathbf{A} \to \mathbf{B}$); alors $v$ se factorise d'une seule manière

$$
v: \begin{array}{c} \mathbf {M} \to \mathbf {S} ^ {- 1} \mathbf {M} \to \mathbf {N} \\ i _ {\mathbf {M}} ^ {\mathrm{S}} \end{array}
$$

où  $v^{*}$  est un homomorphisme de  $S^{-1}A$ -modules (pour la structure de  $S^{-1}A$ -module sur N définie par  $u^{*}$ ).

(1.2.5) On définit un isomorphisme canonique  $S^{-1}A \otimes_{A} M \xrightarrow{\sim} S^{-1}M$  de  $S^{-1}A$ -modules, en faisant correspondre à l'élément  $(a/s) \otimes m$  l'élément  $(am)/s$ , l'isomorphisme réciproque appliquant m/s sur  $(1/s) \otimes m$ .

(1.2.6) Pour tout idéal $\mathfrak{a}'$ de $S^{-1}A$, $\mathfrak{a} = (i_{\mathrm{A}}^{\mathrm{S}})^{-1}(\mathfrak{a}')$ est un idéal de A, et $\mathfrak{a}'$ est l'idéal de $S^{-1}A$ engendré par $i_{\mathrm{A}}^{\mathrm{S}}(\mathfrak{a})$, qui s'identifie à $S^{-1}\mathfrak{a}$ (1.3.2). L'application $\mathfrak{p}' \to (i_{\mathrm{A}}^{\mathrm{S}})^{-1}(\mathfrak{p}')$ est un isomorphisme, pour la structure d'ordre, de l'ensemble des idéaux premiers de $S^{-1}A$ sur l'ensemble des idéaux premiers $\mathfrak{p}$ de A tels que $\mathfrak{p} \cap S = \emptyset$. En outre, les anneaux locaux $A_{\mathfrak{p}}$ et $(S^{-1}A)_{S^{-1}\mathfrak{p}}$ sont alors canoniquement (1.5.1) isomorphes.

(1.2.7) Lorsque A est un anneau intègre, dont on désigne par K le corps des fractions, l'application canonique $i_{\mathrm{A}}^{\mathrm{S}}: \mathrm{A} \to \mathrm{S}^{-1}\mathrm{A}$ est injective pour toute partie multiplicative S ne contenant pas o, et $\mathrm{S}^{-1}\mathrm{A}$ s'identifie alors canoniquement à un sous-anneau de K contenant A. En particulier, pour tout idéal premier p de A, $\mathrm{A}_{\mathfrak{p}}$ est un anneau local contenant A, d'idéal maximal $\mathfrak{p}\mathrm{A}_{\mathfrak{p}}$, et on a $\mathfrak{p}\mathrm{A}_{\mathfrak{p}} \cap \mathrm{A} = \mathfrak{p}$.

(1.2.8) Si A est un anneau réduit (I.I.I), il en est de même de S$^{-1}$A : en effet, si $(x/s)^{n}=o$ pour $x\in A$, $s\in S$, cela signifie qu'il existe $s'\in S$ tel que $s'x^{n}=o$, d'où $(s'x)^{n}=o$, ce qui, par hypothèse, entraîne $s'x=o$, donc $x/s=o$.

## 1.3. Propriétés fonctorielles.

(1.3.1) Soient M, N deux A-modules, u un A-homomorphisme  $M \rightarrow N$ . Si S est une partie multiplicative de A, on définit un  $S^{-1}A$ -homomorphisme  $S^{-1}M \rightarrow S^{-1}N$ , noté  $S^{-1}u$ , en posant  $(S^{-1}u)(m/s) = u(m)/s$ ; si  $S^{-1}M$  et  $S^{-1}N$  sont canoniquement identifiés à  $S^{-1}A \otimes_{A} M$  et  $S^{-1}A \otimes_{A} N$  (1.2.5),  $S^{-1}u$  est identifié à  $1 \otimes u$ . Si P est un troisième A-module, v un A-homomorphisme  $N \rightarrow P$ , on a  $S^{-1}(v \circ u) = (S^{-1}v) \circ (S^{-1}u)$ ; autrement dit  $S^{-1}M$  est un foncteur covariant en M, de la catégorie des A-modules dans celle des  $S^{-1}A$ -modules (A et S étant fixés).

(1.3.2) Le foncteur  $S^{-1}M$  est exact ; autrement dit, si la suite

$$
\mathbf {M} \xrightarrow {\boldsymbol {u}} \mathbf {N} \xrightarrow {\boldsymbol {v}} \mathbf {P}
$$

est exacte, il en est de même de la suite

$$
\mathbf {S} ^ {- 1} \mathbf {M} \stackrel {\mathbf {S} ^ {- 1} u} {\rightarrow} \mathbf {S} ^ {- 1} \mathbf {N} \stackrel {\mathbf {S} ^ {- 1} v} {\rightarrow} \mathbf {S} ^ {- 1} \mathbf {P}.
$$

En particulier, si $u: \mathbf{M} \to \mathbf{N}$ est injectif (resp. surjectif), il en est de même de $S^{-1}u$;

si N et P sont deux sous-modules de M,  $S^{-1}N$  et  $S^{-1}P$  s'identifient canoniquement à des sous-modules de  $S^{-1}M$ , et l'on a

$$
\mathrm{S} ^ {- 1} (\mathrm{N} + \mathrm{P}) = \mathrm{S} ^ {- 1} \mathrm{N} + \mathrm{S} ^ {- 1} \mathrm{P} \quad \text {et} \quad \mathrm{S} ^ {- 1} (\mathrm{N} \cap \mathrm{P}) = (\mathrm{S} ^ {- 1} \mathrm{N}) \cap (\mathrm{S} ^ {- 1} \mathrm{P}).
$$

(1.3.3) Soit  $(\mathbf{M}_{\alpha}, \varphi_{\beta\alpha})$  un système inductif de A-modules; alors  $(\mathrm{S}^{-1}\mathrm{M}_{\alpha}, \mathrm{S}^{-1}\varphi_{\beta\alpha})$  est un système inductif de  $S^{-1}A$ -modules. Exprimant les  $S^{-1}M_{\alpha}$  et  $S^{-1}\varphi_{\beta\alpha}$  comme des produits tensoriels (1.2.5 et 1.3.1), il résulte de la permutabilité des opérations de produit tensoriel et de limite inductive, que l'on a un isomorphisme canonique

$$
\mathrm{S} ^ {- 1} \underset {\longrightarrow} {\lim} \mathrm{M} _ {\alpha} \underset {\rightarrow} {\sim} \underset {\longrightarrow} {\lim} \mathrm{S} ^ {- 1} \mathrm{M} _ {\alpha}
$$

ce qu'on exprime encore en disant que le foncteur  $S^{-1}M$  (en M) commute avec les limites inductives.

(1.3.4) Soient M, N deux A-modules ; il existe un isomorphisme canonique fonctoriel (en M et N)

$$
(\mathbf {S} ^ {- 1} \mathbf {M}) \otimes_ {\mathrm{S} ^ {- 1} \mathrm{A}} (\mathbf {S} ^ {- 1} \mathbf {N}) \stackrel {{\sim}} {{\to}} \mathbf {S} ^ {- 1} (\mathbf {M} \otimes_ {\mathrm{A}} \mathbf {N})
$$

qui transforme $(m / s)\otimes (n / t)$ en $(m\otimes n) / st.$

(1.3.5) On a de même un homomorphisme fonctoriel (en M et N)

$$
\mathrm{S} ^ {- 1} \operatorname{Hom} _ {\mathrm{A}} (\mathrm{M}, \mathrm{N}) \rightarrow \operatorname{Hom} _ {\mathrm{S} ^ {- 1} \mathrm{A}} (\mathrm{S} ^ {- 1} \mathrm{M}, \mathrm{S} ^ {- 1} \mathrm{N})
$$

qui, à $u/s$, fait correspondre l'homomorphisme $m/t \to u(m)/st$. Lorsque M a une présentation finie, l'homomorphisme précédent est un isomorphisme : c'est immédiat lorsque M est de la forme $A^{r}$, et on passe de là au cas général en partant de la suite exacte $A^{p} \to A^{q} \to M \to o$, et en utilisant l'exactitude du foncteur $S^{-1}M$ et l'exactitude à gauche du foncteur $\mathrm{Hom}_{\mathrm{A}}(\mathbf{M}, \mathbf{N})$ en M. On notera que ce cas se présente toujours lorsque A est noethérien et le A-module M de type fini.

## 1.4. Changement de partie multiplicative.

(1.4.1) Soient S, T deux parties multiplicatives d'un anneau A telles que $S \subset T$; il existe un homomorphisme canonique $\rho_{\mathrm{A}}^{\mathrm{T},\mathrm{S}}$ (ou simplement $\rho^{\mathrm{T},\mathrm{S}}$) de $S^{-1}\mathrm{A}$ dans $T^{-1}\mathrm{A}$, faisant correspondre à l'élément noté $a/s$ de $S^{-1}\mathrm{A}$ l'élément noté $a/s$ dans $T^{-1}\mathrm{A}$; on a $i_{\mathrm{A}}^{\mathrm{T}} = \rho_{\mathrm{A}}^{\mathrm{T},\mathrm{S}} \circ i_{\mathrm{A}}^{\mathrm{S}}$. Pour tout A-module M, il existe de même une application $S^{-1}\mathrm{A}$-linéaire de $S^{-1}\mathrm{M}$ dans $T^{-1}\mathrm{M}$ (ce dernier étant considéré comme $S^{-1}\mathrm{A}$-module grâce à l'homomorphisme $\rho_{\mathrm{A}}^{\mathrm{T},\mathrm{S}}$), qui fait correspondre à l'élément $m/s$ de $S^{-1}\mathrm{M}$ l'élément $m/s$ de $T^{-1}\mathrm{M}$; on note cette application $\rho_{\mathrm{M}}^{\mathrm{T},\mathrm{S}}$, ou simplement $\rho^{\mathrm{T},\mathrm{S}}$, et on a encore $i_{\mathrm{M}}^{\mathrm{T}} = \rho_{\mathrm{M}}^{\mathrm{T},\mathrm{S}} \circ i_{\mathrm{M}}^{\mathrm{S}}$; dans l'identification canonique (1.2.5), $\rho_{\mathrm{M}}^{\mathrm{T},\mathrm{S}}$ s'identifie à $\rho_{\mathrm{A}}^{\mathrm{T},\mathrm{S}} \otimes \mathbf{i}$. L'homomorphisme $\rho_{\mathrm{M}}^{\mathrm{T},\mathrm{S}}$ est un morphisme fonctoriel (ou transformation naturelle) du foncteur $S^{-1}\mathrm{M}$ dans le foncteur $T^{-1}\mathrm{M}$, autrement dit, le diagramme

$$
\begin{array}{c} \mathrm{S} ^ {- 1} \mathrm{M} \xrightarrow {\mathrm{S} ^ {- 1} u} \mathrm{S} ^ {- 1} \mathrm{N} \\ \rho_ {\mathrm{M}} ^ {\mathrm{T},   \mathrm{S}} \Biggl \downarrow \qquad \qquad \qquad \Biggl \downarrow \rho_ {\mathrm{N}} ^ {\mathrm{T},   \mathrm{S}} \\ \mathrm{T} ^ {- 1} \mathrm{M} \xrightarrow {\mathrm{T} ^ {- 1} u} \mathrm{T} ^ {- 1} \mathrm{N} \end{array}
$$

est commutatif, pour tout homomorphisme $u: \mathbf{M} \to \mathbf{N}$; on notera en outre que $\mathbf{T}^{-1} u$ est entièrement déterminé par $\mathbf{S}^{-1} u$, car pour $m \in \mathbf{M}$ et $t \in \mathbf{T}$, on a

$$
\left(\mathrm{T} ^ {- 1} u\right) (m / t) = (t / \mathrm{I}) ^ {- 1} \rho^ {\mathrm{T}, \mathrm{S}} \left(\left(\mathrm{S} ^ {- 1} u\right) (m / \mathrm{I})\right).
$$

(1.4.2) Avec les mêmes notations, pour deux A-modules M, N, les diagrammes (cf. (1.3.4) et (1.3.5))

$$
\begin{array}{c c} (\mathrm{S} ^ {- 1} \mathrm{M}) \otimes_ {\mathrm{S} ^ {- 1} \mathrm{A}} (\mathrm{S} ^ {- 1} \mathrm{N}) \simeq \mathrm{S} ^ {- 1} (\mathrm{M} \otimes_ {\mathrm{A}} \mathrm{N}) & \quad \mathrm{S} ^ {- 1} \mathrm{Hom} _ {\mathrm{A}} (\mathrm{M},   \mathrm{N}) \to \mathrm{Hom} _ {\mathrm{S} ^ {- 1} \mathrm{A}} (\mathrm{S} ^ {- 1} \mathrm{M},   \mathrm{S} ^ {- 1} \mathrm{N}) \\ \downarrow & \quad \downarrow \\ (\mathrm{T} ^ {- 1} \mathrm{M}) \otimes_ {\mathrm{T} ^ {- 1} \mathrm{A}} (\mathrm{T} ^ {- 1} \mathrm{N}) \simeq \mathrm{T} ^ {- 1} (\mathrm{M} \otimes_ {\mathrm{A}} \mathrm{N}) & \quad \mathrm{T} ^ {- 1} \mathrm{Hom} _ {\mathrm{A}} (\mathrm{M},   \mathrm{N}) \to \mathrm{Hom} _ {\mathrm{T} ^ {- 1} \mathrm{A}} (\mathrm{T} ^ {- 1} \mathrm{M},   \mathrm{T} ^ {- 1} \mathrm{N}) \end{array}
$$

sont commutatifs.

(1.4.3) Il y a un cas important dans lequel l'homomorphisme $\rho^{\mathrm{T},\mathrm{S}}$ est bijectif, savoir lorsque tout élément de T est diviseur d'un élément de S ; on identifie alors par $\rho^{\mathrm{T},\mathrm{S}}$ les modules $\mathrm{S}^{-1}\mathrm{M}$ et $\mathrm{T}^{-1}\mathrm{M}$. On dit que S est saturé si tout diviseur dans A d'un élément de S est dans S ; en remplaçant S par l'ensemble T de tous les diviseurs des éléments de S (ensemble qui est multiplicatif et saturé), on voit qu'on peut toujours, si l'on veut, se limiter à la considération de modules de fractions $\mathrm{S}^{-1}\mathrm{M}$, où S est saturé.

(1.4.4) Si S, T, U sont trois parties multiplicatives de A telles que $S \subset T \subset U$, on a

$$
\rho^ {\mathrm{U}, \mathrm{S}} = \rho^ {\mathrm{U}, \mathrm{T}} \circ \rho^ {\mathrm{T}, \mathrm{S}}.
$$

(1.4.5) Considérons une famille filtrante croissante  $(\mathrm{S}_{\alpha})$  de parties multiplicatives de A (on écrira  $\alpha\leqslant\beta$  pour  $S_{\alpha}\subset S_{\beta}$ ), et soit S la partie multiplicative  $\bigcup_{\alpha}S_{\alpha}$ ; posons  $\rho_{\beta\alpha}=\rho_{A}^{S_{\beta},S_{\alpha}}$  pour  $\alpha\leqslant\beta$ ; en vertu de (1.4.4), les homomorphismes  $\rho_{\beta\alpha}$  définissent un anneau A' limite inductive du système inductif d'anneaux  $(\mathrm{S}_{\alpha}^{-1}\mathrm{A},\rho_{\beta\alpha})$ . Soit  $\rho_{\alpha}$  l'application canonique  $S_{\alpha}^{-1}A\to A'$ , et posons  $\varphi_{\alpha}=\rho_{A}^{S,S_{\alpha}}$ ; comme  $\varphi_{\alpha}=\varphi_{\beta}\circ\rho_{\beta\alpha}$  pour  $\alpha\leqslant\beta$  d'après (1.4.4), on peut définir de façon unique un homomorphisme  $\varphi:A'\to S^{-1}A$  tel que le diagramme

![](images/page_14_image_9.jpg)

soit commutatif. En fait, $\varphi$ est un isomorphisme : il est en effet immédiat par construction que $\varphi$ est surjectif. D'autre part, si $\rho_{\alpha}(a/s_{\alpha})\in\mathbf{A}^{\prime}$ est tel que $\varphi(\rho_{\alpha}(a/s_{\alpha}))=0$, cela signifie que $a/s_{\alpha}=0$ dans $\mathrm{S}^{-1}\mathrm{A}$, c'est-à-dire qu'il existe $s\in\mathrm{S}$ tel que $sa=0$; mais il y a un $\beta\geqslant\alpha$ tel que $s\in\mathrm{S}_{\beta}$, et par suite, comme $\rho_{\alpha}(a/s_{\alpha})=\rho_{\beta}(sa/ss_{\alpha})=0$, on voit que $\varphi$ est injectif. On traite de même le cas d'un A-module M, et on a ainsi défini des isomorphismes canoniques

$$
\varinjlim \mathrm{S} _ {\alpha} ^ {- 1} \mathrm{A} \simeq (\varinjlim \mathrm{S} _ {\alpha}) ^ {- 1} \mathrm{A}, \quad \varinjlim \mathrm{S} _ {\alpha} ^ {- 1} \mathrm{M} \simeq (\varinjlim \mathrm{S} _ {\alpha}) ^ {- 1} \mathrm{M},
$$

le second étant fonctoriel en M.

(1.4.6) Soient  $S_{1}$ ,  $S_{2}$  deux parties multiplicatives de A; alors  $S_{1}S_{2}$  est aussi une partie multiplicative de A. Désignons par  $S_{2}^{\prime}$  l'image canonique de  $S_{2}$  dans l'anneau  $S_{1}^{-1}A$ , qui est une partie multiplicative de cet anneau. Pour tout A-module M, il existe alors un isomorphisme fonctoriel

$$
\mathrm{S} _ {2} ^ {\prime - 1} (\mathrm{S} _ {1} ^ {- 1} \mathrm{M}) \stackrel {{\sim}} {{\to}} (\mathrm{S} _ {1} \mathrm{S} _ {2}) ^ {- 1} \mathrm{M}
$$

qui fait correspondre à  $(m/s_{1})/(s_{2}/\mathrm{I})$  l'élément  $m/(s_{1}s_{2})$ .

## 1.5. Changement d'anneau.

(1.5.1) Soient A, A' deux anneaux, $\varphi$ un homomorphisme $A' \to A$, S (resp. S') une partie multiplicative de A (resp. A'), telle que $\varphi(S') \subset S$; l'homomorphisme composé $A' \xrightarrow{\varphi} A \to S^{-1}A$ se factorise en $A' \to S'^{-1}A' \xrightarrow{\varphi^{S'}} S^{-1}A$ en vertu de (1.2.4); on a $\varphi^{S'}(a'/s') = \varphi(a') / \varphi(s')$. Si $A = \varphi(A')$ et $S = \varphi(S')$, $\varphi^{S'}$ est surjective. Si $A' = A$ et si $\varphi$ est l'identité, $\varphi^{S'}$ n'est autre que l'homomorphisme $\rho_{A}^{S,S'}$ défini en (1.4.1).

(1.5.2) Sous les hypothèses de (1.5.1), soit M un A-module. Il existe un homomorphisme canonique fonctoriel

$$
\sigma : \mathrm{S} ^ {\prime - 1} (\mathbf {M} _ {[ \varphi ]}) \rightarrow (\mathrm{S} ^ {- 1} \mathbf {M}) _ {[ \varphi^ {\mathrm{s} ^ {\prime}} ]}
$$

de $\mathrm{S}^{\prime -1}\mathrm{A}^{\prime}$-modules, faisant correspondre à tout élément $m / s'$ de $\mathrm{S}^{\prime -1}(\mathbf{M}_{[\varphi]})$ l'élément $m / \varphi (s')$ de $(\mathrm{S}^{-1}\mathrm{M})_{[\varphi^{\mathrm{s}^{\prime}}]}$; on vérifie en effet immédiatement que cette définition ne dépend pas de l'expression $m / s'$ de l'élément considéré. Lorsque $\mathrm{S} = \varphi (\mathrm{S}')$, l'homomorphisme $\sigma$ est bijectif. Lorsque $\mathrm{A}' = \mathrm{A}$ et que $\varphi$ est l'identité, $\sigma$ n'est autre que l'homomorphisme $\rho_{\mathrm{M}}^{\mathrm{S},\mathrm{S}'}$ défini en (1.4.1).

Lorsqu'on prend en particulier M=A, l'homomorphisme  $\varphi$  définit sur A une structure de A'-algèbre;  $S'^{-1}(A_{[\varphi]})$  est alors muni d'une structure d'anneau, pour laquelle il s'identifie à  $(\varphi(S'))^{-1}A$ , et l'homomorphisme  $\sigma: S'^{-1}(A_{[\varphi]}) \to S^{-1}A$  est un homomorphisme de  $S'^{-1}A'$ -algèbres.

(1.5.3) Soient M et N deux A-modules ; en composant les homomorphismes définis dans (1.3.4) et (1.5.2), on obtient un homomorphisme

$$
\left(\mathrm{S} ^ {- 1} \mathrm{M} \otimes_ {\mathrm{S} ^ {- 1} \mathrm{A}} \mathrm{S} ^ {- 1} \mathrm{N}\right) _ {[ \varphi^ {\mathrm{S} ^ {\prime}} ]} \leftarrow \mathrm{S} ^ {\prime - 1} \left(\left(\mathrm{M} \otimes_ {\mathrm{A}} \mathrm{N}\right) _ {[ \varphi ]}\right)
$$

qui est un isomorphisme lorsque $\varphi(S') = S$. De même, en composant les homomorphismes (1.3.5) et (1.5.2), on obtient un homomorphisme

$$
\mathrm{S} ^ {\prime - 1} \left(\left(\operatorname{Hom} _ {\mathrm{A}} (\mathrm{M}, \mathrm{N})\right) _ {[ \varphi ]}\right)\rightarrow \left(\operatorname{Hom} _ {\mathrm{S} ^ {- 1} \mathrm{A}} \left(\mathrm{S} ^ {- 1} \mathrm{M}, \mathrm{S} ^ {- 1} \mathrm{N}\right)\right) _ {[ \varphi^ {s ^ {\prime}} ]}
$$

qui est un isomorphisme lorsque $\varphi(S') = S$ et que M admet une présentation finie.

(1.5.4) Considérons maintenant un A'-module N', et formons le produit tensoriel N'⊗A'A[φ], qui peut être considéré comme un A-module en posant a.(n'⊗b)=n'⊗(ab). Il existe un isomorphisme fonctoriel de S-1A-modules

$$
\tau : \left(\mathrm{S} ^ {\prime - 1} \mathrm{N} ^ {\prime}\right) \otimes_ {\mathrm{S} ^ {\prime - 1} \mathrm{A} ^ {\prime}} \left(\mathrm{S} ^ {- 1} \mathrm{A}\right) _ {[ \varphi^ {\mathrm{s} ^ {\prime}} ]} \simeq \mathrm{S} ^ {- 1} \left(\mathrm{N} ^ {\prime} \otimes_ {\mathrm{A} ^ {\prime}} \mathrm{A} _ {[ \varphi ]}\right)
$$

qui, à l'élément $(n'/s') \otimes (a/s)$, fait correspondre l'élément $(n' \otimes a)/( \varphi(s')s)$; on vérifie en effet séparément que lorsqu'on remplace $n'/s'$ (resp. $a/s$) par une autre expression du même élément, $(n' \otimes a)/( \varphi(s')s)$ ne change pas; d'autre part, on peut définir un homomorphisme réciproque de $\tau$ en faisant correspondre à $(n' \otimes a)/s$ l'élément $(n'/\mathbf{I}) \otimes (a/s)$: on utilise le fait que $S^{-1}(N' \otimes_{A'} A_{[\varphi]})$ est canoniquement isomorphe à $(N' \otimes_{A'} A_{[\varphi]}) \otimes_A S^{-1} A(1.2.5)$, donc aussi à $N' \otimes_{A'} (S^{-1} A)_{[\psi]}$, en désignant par $\psi$ l'homomorphisme composé $a' \to \varphi(a')/I$ de $A'$ dans $S^{-1} A$.

(1.5.5) Si M' et N' sont deux A'-modules, en composant les isomorphismes (1.3.4) et (1.5.4), on obtient un isomorphisme

$$
\mathrm{S} ^ {\prime - 1} \mathrm{M} ^ {\prime} \otimes_ {\mathrm{S} ^ {\prime - 1} \mathrm{A} ^ {\prime}} \mathrm{S} ^ {\prime - 1} \mathrm{N} ^ {\prime} \otimes_ {\mathrm{S} ^ {\prime - 1} \mathrm{A} ^ {\prime}} \mathrm{S} ^ {- 1} \mathrm{A} \stackrel {{\sim}} {{\rightarrow}} \mathrm{S} ^ {- 1} (\mathrm{M} ^ {\prime} \otimes_ {\mathrm{A} ^ {\prime}} \mathrm{N} ^ {\prime} \otimes_ {\mathrm{A} ^ {\prime}} \mathrm{A}).
$$

De même, si M' admet une présentation finie, on a en vertu de (1.3.5) et (1.5.4), un isomorphisme

$$
\operatorname{Hom} _ {\mathrm{S} ^ {\prime - 1} \mathrm{A} ^ {\prime}} \left(\mathrm{S} ^ {\prime - 1} \mathrm{M} ^ {\prime}, \mathrm{S} ^ {\prime - 1} \mathrm{N} ^ {\prime}\right) \otimes_ {\mathrm{S} ^ {\prime - 1} \mathrm{A} ^ {\prime}} \mathrm{S} ^ {- 1} \mathrm{A} \stackrel {{\sim}} {{\rightarrow}} \mathrm{S} ^ {- 1} \left(\operatorname{Hom} _ {\mathrm{A} ^ {\prime}} \left(\mathrm{M} ^ {\prime}, \mathrm{N} ^ {\prime}\right) \otimes_ {\mathrm{A} ^ {\prime}} \mathrm{A}\right).
$$

(1.5.6) Sous les hypothèses de (1.5.1), soit T (resp. T') une seconde partie multiplicative de A (resp. A') telle que S ⊂ T (resp. S' ⊂ T') et φ(T') ⊂ T. Alors le diagramme

$$
\begin{array}{c} \mathrm{S} ^ {\prime - 1} \mathrm{A} ^ {\prime} \stackrel {{\varphi^ {\mathrm{S} ^ {\prime}}}} {{\to}} \mathrm{S} ^ {- 1} \mathrm{A} \\ \rho^ {\mathrm{T} ^ {\prime}, \mathrm{s} ^ {\prime}} \Bigg | _ {\downarrow} \qquad \qquad \qquad \qquad \Bigg | _ {\downarrow} \rho^ {\mathrm{T}, \mathrm{s}} \\ \mathrm{T} ^ {\prime - 1} \mathrm{A} ^ {\prime} \stackrel {{\varphi^ {\mathrm{T} ^ {\prime}}}} {{\to}} \mathrm{T} ^ {- 1} \mathrm{A} \end{array}
$$

est commutatif. Si M est un A-module, le diagramme

$$
\begin{array}{c} \mathbf {S} ^ {\prime - 1} (\mathbf {M} _ {[ \varphi ]}) \xrightarrow {\sigma} (\mathbf {S} ^ {- 1} \mathbf {M}) _ {[ \varphi^ {s ^ {\prime}} ]} \\ \rho^ {\mathrm{T} ^ {\prime}, \mathrm{s} ^ {\prime}} \Biggl \downarrow \qquad \qquad \qquad \qquad \Biggl \downarrow_ {\rho^ {\mathrm{T}}, \mathrm{s}} \\ \mathbf {T} ^ {\prime - 1} (\mathbf {M} _ {[ \varphi ]}) \xrightarrow [ \sigma ]{} (\mathbf {T} ^ {- 1} \mathbf {M}) _ {[ \varphi^ {\mathrm{T} ^ {\prime}} ]} \end{array}
$$

est commutatif. Enfin, si N' est un A'-module, le diagramme

$$
\begin{array}{c} (\mathbf {S} ^ {\prime - 1} \mathbf {N} ^ {\prime}) \otimes_ {\mathrm{S} ^ {\prime - 1} \mathrm{A} ^ {\prime}} (\mathbf {S} ^ {- 1} \mathbf {A}) _ {[ \varphi^ {\mathrm{S} ^ {\prime}} ]} \stackrel {{\tau}} {{\to}} \mathbf {S} ^ {- 1} (\mathbf {N} ^ {\prime} \otimes_ {\mathrm{A} ^ {\prime}} \mathbf {A} _ {[ \varphi ]}) \\ \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow_ {\boldsymbol {\rho} ^ {\mathrm{T}},   \mathrm{s}} \\ (\mathbf {T} ^ {\prime - 1} \mathbf {N} ^ {\prime}) \otimes_ {\mathrm{T} ^ {\prime - 1} \mathrm{A} ^ {\prime}} (\mathbf {T} ^ {- 1} \mathbf {A}) _ {[ \varphi^ {\mathrm{T} ^ {\prime}} ]} \underset {\tau} {\overset {{\tau}} {{\to}}} \mathbf {T} ^ {- 1} (\mathbf {N} ^ {\prime} \otimes_ {\mathrm{A} ^ {\prime}} \mathbf {A} _ {[ \varphi ]}) \end{array}
$$

est commutatif, la flèche verticale de gauche étant obtenue en appliquant $\rho_{\mathrm{N}^{\prime}}^{\mathrm{T}^{\prime},\mathrm{S}^{\prime}}$ à $\mathbf{S}^{\prime -1}\mathbf{N}^{\prime}$ et $\rho_{\mathrm{A}}^{\mathrm{T},\mathrm{S}}$ à $\mathbf{S}^{-1}\mathbf{A}$.

(1.5.7) Soient A'' un troisième anneau, $\varphi': A'' \to A'$ un homomorphisme d'anneaux, S'' une partie multiplicative de A'' telle que $\varphi'(S'') \subset S'$. Posons $\varphi'' = \varphi \circ \varphi'$; alors on a

$$
\varphi^ {\prime \prime} \mathrm{S} ^ {\prime \prime} = \varphi^ {\mathrm{S} ^ {\prime}} \circ \varphi^ {\prime} \mathrm{S} ^ {\prime \prime}.
$$

Soit M un A-module ; on a évidemment  $\mathbf{M}_{[\varphi^{\prime}]} = (\mathbf{M}_{[\varphi]})_{[\varphi^{\prime}]}$ ; si  $\sigma^{\prime}$  et  $\sigma^{\prime\prime}$  sont les homomorphismes définis à partir de  $\varphi^{\prime}$  et  $\varphi^{\prime\prime}$  comme  $\sigma$  est défini dans (1.5.2) à partir de  $\varphi$ , on a la formule de transitivité

$$
\sigma^ {\prime \prime} = \sigma \circ \sigma^ {\prime}.
$$

Enfin, soit $\mathbf{N}^{\prime \prime}$ un $\mathbf{A}^{\prime \prime}$-module; le A-module $\mathbf{N}^{\prime \prime} \otimes_{\mathbf{A}''}\mathbf{A}_{[\varphi'']}$ s'identifie canoniquement à $(\mathbf{N}^{\prime \prime} \otimes_{\mathbf{A}''}\mathbf{A}'_{[\varphi']} ) \otimes_{\mathbf{A}'}\mathbf{A}_{[\varphi]}$, et de même, le $\mathbf{S}^{-1}\mathbf{A}$-module $(\mathbf{S}^{\prime \prime - 1}\mathbf{N}^{\prime \prime}) \otimes_{\mathbf{S}'' - 1}\mathbf{A}'_{[\varphi ' \mathbf{S}'']}$ s'identifie canoniquement à $((\mathbf{S}^{\prime \prime - 1}\mathbf{N}^{\prime \prime}) \otimes_{\mathbf{S}'' - 1}\mathbf{A}'_{[\varphi ' \mathbf{S}'']})(\mathbf{S}^{\prime - 1}\mathbf{A}')_{[\varphi ' \mathbf{S}'']}) \otimes_{\mathbf{S}^{\prime - 1}\mathbf{A}'}(\mathbf{S}^{-1}\mathbf{A})_{[\varphi \mathbf{S}^{\prime}]}$. Avec ces identifications, si $\tau'$ et $\tau''$ sont les isomorphismes définis à partir de $\varphi'$ et $\varphi''$ comme $\tau$ est défini dans (1.5.4) à partir de $\varphi$, on a la formule de transitivité

$$
\tau^ {\prime \prime} = \tau_ {0} (\tau^ {\prime} \otimes I).
$$

(1.5.8) Soit A un sous-anneau d'un anneau B ; pour tout idéal premier minimal p de A, il existe un idéal premier minimal q de B tel que  $p = A \cap q$ . En effet,  $A_{p}$  est un sous-anneau de  $B_{p}$  (1.3.2) et possède un seul idéal premier  $p'$  (1.2.6) ; comme  $B_{p}$  n'est pas réduit à o, il possède au moins un idéal premier  $q'$  et on a nécessairement  $q' \cap A_{p} = p'$ ; l'idéal premier  $q_{1}$  de B, image réciproque de  $q'$  est donc tel que  $q_{1} \cap A = p$ , et a fortiori on a  $q \cap A = p$  pour tout idéal premier minimal q de B contenu dans  $q_{1}$ .

## 1.6. Identification du module  $M_{i}$  à une limite inductive.

(1.6.1) Soient M un A-module, $f$ un élément de A. Considérons une suite $(\mathbf{M}_{n})$ de A-modules, tous identiques à M, et pour tout couple d'entiers $m \leqslant n$, soit $\varphi_{nm}$ l'homomorphisme $z \to f^{n-m}z$ de $\mathbf{M}_{m}$ dans $\mathbf{M}_{n}$; il est immédiat que $((\mathbf{M}_{n}), (\varphi_{nm}))$ est un système inductif de A-modules; soit $\mathbf{N} = \varinjlim \mathbf{M}_{n}$ la limite inductive de ce système. Nous allons définir un A-isomorphisme canonique fonctoriel de N sur $\mathbf{M}_{f}$. Pour cela, remarquons que, pour tout $n$, $\theta_{n}: z \to z/f^{n}$ est un A-homomorphisme de $\mathbf{M} = \mathbf{M}_{i}$ dans $\mathbf{M}_{f}$, et il résulte des définitions que l'on a $\theta_{n} \circ \varphi_{nm} = \theta_{m}$ pour $m \leqslant n$. Il existe donc un A-homomorphisme $\theta: \mathbf{N} \to \mathbf{M}_{f}$ tel que, si $\varphi_{n}$ désigne l'homomorphisme canonique $\mathbf{M}_{n} \to \mathbf{N}$, on ait $\theta_{n} = \theta \circ \varphi_{n}$ pour tout $n$. Comme par hypothèse tout élément de $\mathbf{M}_{f}$ est de la forme $z/f^{n}$ pour un $n$ au moins, il est clair que $\theta$ est surjectif. D'autre part, si $\theta(\varphi_{n}(z)) = 0$, autrement dit $z/f^{n} = 0$, il existe un entier $k > 0$ tel que $f^{k}z = 0$, donc $\varphi_{n+k,n}(z) = 0$, ce qui entraîne $\varphi_{n}(z) = 0$. On peut donc identifier $\mathbf{M}_{f}$ et $\lim_{\rightarrow} \mathbf{M}_{n}$ au moyen de $\theta$.

(1.6.2) Écrivons maintenant  $M_{l,n}$ ,  $\varphi_{nm}^{f}$  et  $\varphi_{n}^{f}$  au lieu de  $M_{n}$ ,  $\varphi_{nm}$  et  $\varphi_{n}$ . Soit g un second élément de A. Comme  $f^{n}$  divise  $f^{n}g^{n}$ , on a un homomorphisme fonctoriel

$$
\rho_ {f g, f}: \mathbf {M} _ {f} \rightarrow \mathbf {M} _ {f g} (\mathrm{I}. 4. \mathrm{I} \text {et I}. 4. 3);
$$

si on identifie $\mathbf{M}_{f}$ et $\mathbf{M}_{fg}$ à $\varinjlim\mathbf{M}_{f,n}$ et $\varinjlim\mathbf{M}_{fg,n}$ respectivement, $\rho_{fg,f}$ s'identifie à la limite inductive des applications $\rho_{fg,f}^{n}:\mathbf{M}_{f,n}\to\mathbf{M}_{fg,n}$ définies par $\rho_{fg,f}^{n}(z)=g^{n}z$. En effet, cela résulte immédiatement de la commutativité du diagramme

$$
\begin{array}{c} \mathbf {M} _ {f, n} \xrightarrow {\varphi_ {f g , f} ^ {n}} \mathbf {M} _ {f g, n} \\ \varphi_ {n} ^ {t} \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow \varphi_ {n} ^ {f g} \\ \mathbf {M} _ {f} \xrightarrow {\varphi_ {f g , f}} \mathbf {M} _ {f g} \end{array}
$$

## 1.7. Support d'un module.

(1.7.1) Étant donné un A-module M, on appelle support de M et on note Supp(M) l'ensemble des idéaux premiers p de A tels que  $M_{p} \neq 0$ . Pour que M = 0, il faut et il suffit que Supp(M) = 0, car si  $M_{p} = 0$  pour tout p, l'annulateur d'un élément  $x \in M$  ne peut être contenu dans aucun idéal premier de A, donc est A tout entier.

(1.7.2) Si $o \to N \to M \to P \to o$ est une suite exacte de A-modules, on a

$$
\operatorname{Supp} (\mathbf {M}) = \operatorname{Supp} (\mathbf {N}) \cup \operatorname{Supp} (\mathbf {P})
$$

car pour tout idéal premier p de A, la suite  $o \rightarrow N_{p} \rightarrow M_{p} \rightarrow P_{p} \rightarrow o$  est exacte (1.3.2) et pour que  $M_{p} = o$ , il faut et il suffit que  $N_{p} = P_{p} = o$ .

(1.7.3) Si M est somme d'une famille $(\mathbf{M}_{\lambda})$ de sous-modules, $\mathbf{M}_{\mathfrak{p}}$ est somme des $(\mathbf{M}_{\lambda})_{\mathfrak{p}}$ pour tout idéal premier $\mathfrak{p}$ de A (1.3.3 et 1.3.2), donc $\operatorname{Supp}(\mathbf{M}) = \bigcup_{\lambda} \operatorname{Supp}(\mathbf{M}_{\lambda})$.

(1.7.4) Si M est un A-module de type fini, Supp(M) est l'ensemble des idéaux premiers contenant l'annulateur de M. En effet, si M est monogène et engendré par $x$, dire que $M_{\mathfrak{p}} = 0$ signifie qu'il existe $s \notin \mathfrak{p}$ tel que $s.x = 0$, donc que $\mathfrak{p}$ ne contient pas l'annulateur de $x$. Si maintenant M admet un système fini $(x_i)_{1 \leqslant i \leqslant n}$ de générateurs et si $a_i$ est l'annulateur de $x_i$, il résulte de (1.7.3) que Supp(M) est l'ensemble des $\mathfrak{p}$ contenant l'un des $a_i$, ou, ce qui revient au même, l'ensemble des $\mathfrak{p}$ contenant $a = \bigcap_i x_i$ qui est l'annulateur de M.

(1.7.5) Si M et N sont deux A-modules de type fini, on a

$$
\operatorname{Supp} (\mathbf {M} \otimes_ {\mathrm{A}} \mathbf {N}) = \operatorname{Supp} (\mathbf {M}) \cap \operatorname{Supp} (\mathbf {N}).
$$

Il s'agit de voir que si p est un idéal premier de A, la condition  $M_{p} \otimes_{A_{p}} N_{p} \neq o$  est équivalente à «  $M_{p} \neq o$  et  $N_{p} \neq o$  » (compte tenu de (1.3.4)). Autrement dit, il s'agit de voir que si P, Q sont deux modules de type fini sur un anneau local B, non réduits à o, alors  $P \otimes_{B} Q \neq o$ . Soit m l'idéal maximal de B. En vertu du lemme de Nakayama, les espaces vectoriels P/mP et Q/mQ ne sont pas réduits à o, donc il en est de même de leur produit tensoriel  $(\mathrm{P}/\mathrm{mP}) \otimes_{\mathrm{B}/\mathrm{m}} (\mathrm{Q}/\mathrm{mQ}) = (\mathrm{P} \otimes_{\mathrm{B}} \mathrm{Q}) \otimes_{\mathrm{B}} (\mathrm{B}/\mathrm{m})$ , d'où la conclusion.

En particulier, si M est un A-module de type fini, a un idéal de A, Supp(M/aM) est l'ensemble des idéaux premiers contenant à la fois a et l'annulateur n de M (1.7.4), autrement dit l'ensemble des idéaux premiers contenant  $a+n$ .

## § 2. ESPACES IRRÉDUCTIBLES. ESPACES NOETHÉRIENS

## 2.1. Espaces irréductibles.

(2.1.1) On dit qu'un espace topologique X est irréductible s'il est non vide et s'il n'est pas réunion de deux sous-espaces fermés distincts de X. Il revient au même de dire que  $X \neq \emptyset$  et que l'intersection de deux ouverts (et par suite d'un nombre fini d'ouverts) non vides de X est non vide, ou que tout ouvert non vide est partout dense, ou que toute partie fermée  $\neq X$  est rare, ou enfin que tout ouvert de X est connexe.

(2.1.2) Pour qu'un sous-espace Y d'un espace topologique X soit irréductible, il faut et il suffit que son adhérence  $\overline{Y}$  soit irréductible. En particulier, tout sous-espace qui est l'adhérence  $\overline{\{x\}}$  d'un sous-espace réduit à un point est irréductible ; nous exprimerons la relation  $y \in \overline{\{x\}}$  (équivalente à  $\overline{\{y\}} \subset \overline{\{x\}}$ ) en disant que y est spécialisation de x ou que x est une générisation de y. Lorsqu'il existe dans un espace irréductible X un point x tel que  $X = \overline{\{x\}}$ , nous dirons que x est point générique de X. Tout ouvert non vide de X contient alors x et tout sous-espace contenant x admet x pour point générique.

(2.1.3) Rappelons qu'on appelle espace de Kolmogoroff un espace topologique X vérifiant l'axiome de séparation :

$(T_{0})$ Si $x \neq y$ sont deux points quelconques de X, il existe un ensemble ouvert contenant l'un des points x, y et non l'autre.

Si un espace de Kolmogoroff irréductible admet un point générique, il n'en admet qu'un seul puisqu'un ouvert non vide contient tout point générique.

Rappelons qu'un espace topologique X est dit quasi-compact si, de tout recouvrement ouvert de X, on peut extraire un recouvrement fini de X (ou, ce qui revient au même, si toute famille filtrante décroissante d'ensembles fermés non vides a une inter-section non vide). Si X est un espace quasi-compact, toute partie fermée non vide A de X contient un ensemble fermé non vide minimal M, car l'ensemble des parties fermées non vides de A est inductif pour la relation ⊃ ; si en outre X est un espace de Kolmogoroff, M est nécessairement réduite à un seul point (ou, comme on dit par abus de langage, est un point fermé).

(2.1.4) Dans un espace irréductible X, tout sous-espace ouvert non vide U est irréductible, et si X admet un point générique x, x est aussi point générique de U.

Soit  $(\mathrm{U}_{\alpha})$  un recouvrement (dont l'ensemble d'indices est non vide) d'un espace topologique X, formé d'ouverts non vides; pour que X soit irréductible, il faut et il suffit que  $U_{\alpha}$  soit irréductible pour tout  $\alpha$, et que  $U_{\alpha} \cap U_{\beta} \neq \emptyset$  quels que soient  $\alpha$,  $\beta$. La condition est évidemment nécessaire ; pour voir qu'elle est suffisante, il suffit de prouver que si V est un ouvert non vide de X,  $V \cap U_{\alpha}$  est non vide pour tout  $\alpha$, car alors  $V \cap U_{\alpha}$  est dense dans  $U_{\alpha}$  pour tout  $\alpha$, et par suite V est dense dans X. Or, il y a au moins un indice  $\gamma$  tel que  $V \cap U_{\gamma} \neq \emptyset$, donc  $V \cap U_{\gamma}$  est dense dans  $U_{\gamma}$, et comme, pour tout  $\alpha$,  $U_{\alpha} \cap U_{\gamma} \neq \emptyset$, on a aussi  $V \cap U_{\alpha} \cap U_{\gamma} \neq \emptyset$.

(2.1.5) Soient X un espace irréductible, f une application continue de X dans un espace topologique Y. Alors  $f(\mathbf{X})$  est irréductible, et si x est point générique de X,  $f(x)$  est point générique de  $f(\mathbf{X})$  et par suite aussi de  $\overline{f(\mathbf{X})}$ . En particulier, si de plus Y est irréductible et a un seul point générique y, pour que  $f(\mathbf{X})$  soit partout dense, il faut et il suffit que  $f(x)=y$ .

(2.1.6) Tout sous-espace irréductible d'un espace topologique X est contenu dans un sous-espace irréductible maximal, qui est nécessairement fermé. Les sous-espaces irréductibles maximaux de X sont appelés les composantes irréductibles de X. Si  $Z_{1}$ ,  $Z_{2}$  sont deux composantes irréductibles distinctes de l'espace X,  $Z_{1} \cap Z_{2}$  est un ensemble fermé rare dans chacun des sous-espaces  $Z_{1}$ ,  $Z_{2}$ ; en particulier, si une composante irréductible de X admet un point générique (2.1.2) un tel point ne peut appartenir à aucune autre composante irréductible. Si X n'a qu'un nombre fini de composantes irréductibles  $Z_{i}$  ( $1 \leqslant i \leqslant n$ ), et si, pour chaque i, on pose  $U_{i} = Z_{i} \cap C \left( \bigcup_{j \neq i} Z_{j} \right)$ , les  $U_{i}$  sont ouverts, irréductibles, deux à deux sans point commun et leur réunion est dense dans X.

Soit U une partie ouverte d'un espace topologique X. Si Z est une partie irréductible de X rencontrant U,  $Z \cap U$  est ouvert et dense dans Z, donc irréductible; inversement, pour toute partie fermée irréductible Y de U, l'adhérence  $\bar{Y}$  de Y dans X est irréductible et  $\bar{Y} \cap U = Y$ . On en conclut qu'il y a correspondance biunivoque entre les composantes irréductibles de U et les composantes irréductibles de X qui rencontrent U.

(2.1.7) Si un espace topologique X est réunion d'un nombre fini de sous-espaces irréductibles fermés  $Y_{i}$ , les composantes irréductibles de X sont les éléments maximaux de l'ensemble des  $Y_{i}$ , car si Z est une partie fermée irréductible de X, Z est réunion des  $Z \cap Y_{i}$ , d'où on tire aussitôt que Z doit être contenu dans un des  $Y_{i}$ . Soit Y un sous-espace d'un espace topologique X, et supposons que Y n'ait qu'un nombre fini de composantes irréductibles  $Y_{i}$  ( $i \leqslant i \leqslant n$ ); alors les adhérences  $\overline{Y}_{i}$  dans X sont les composantes irréductibles de  $\overline{Y}$ .

(2.1.8) Soit Y un espace irréductible admettant un seul point générique y. Soient X un espace topologique, f une application continue de X dans Y. Alors, pour toute composante irréductible Z de X rencontrant  $f^{-1}(y)$ ,  $f(Z)$  est dense dans Y. La réciproque n'est pas nécessairement vraie ; toutefois, si Z admet un point générique z, et si  $f(Z)$  est dense dans Y, on a nécessairement  $f(z)=y$  (2.1.5); en outre,  $Z\cap f^{-1}(y)$  est alors l'adhérence de  $\{z\}$  dans  $f^{-1}(y)$  et est donc irréductible, et comme toute partie irréductible de  $f^{-1}(y)$  contenant z est nécessairement contenue dans Z (2.1.6), z est point générique de  $Z\cap f^{-1}(y)$ . Comme toute composante irréductible de  $f^{-1}(y)$  est contenue dans une composante irréductible de X, on voit que si toute composante irréductible Z de X rencontrant  $f^{-1}(y)$  admet un point générique, alors il y a correspondance biunivoque entre l'ensemble de ces composantes et l'ensemble des composantes irréductibles  $Z\cap f^{-1}(Y)$  de  $f^{-1}(y)$ , les points génériques de Z étant identiques à ceux de  $Z\cap f^{-1}(y)$ .

## 2.2. Espaces noethériens.

(2.2.1) On dit qu'un espace topologique X est noethérien si l'ensemble des ouverts de X vérifie la condition maximale, ou, ce qui revient au même, si l'ensemble des fermés de X vérifie la condition minimale. On dit que X est localement noethérien si tout  $x \in X$  admet un voisinage qui est un sous-espace noethérien.

(2.2.2) Soit E un ensemble ordonné vérifiant la condition minimale, et soit P une propriété des éléments de E soumise à la condition suivante : si  $a \in E$  est tel que pour tout x < a,  $\mathbf{P}(x)$  soit vraie, alors  $\mathbf{P}(a)$  est vraie. Dans ces conditions,  $\mathbf{P}(x)$  est vraie pour tout  $x \in E$  (« principe de récurrence noethérienne »). En effet, soit F l'ensemble des  $x \in E$  pour lesquels  $\mathbf{P}(x)$  est fausse ; si F était non vide, il aurait un élément minimal a, et comme alors  $\mathbf{P}(x)$  est vraie pour tout x < a,  $\mathbf{P}(a)$  serait aussi vraie, ce qui est contradictoire.

Nous appliquerons en particulier ce principe lorsque E est un ensemble de parties fermées d'un espace noethérien.

(2.2.3) Tout sous-espace d'un espace noethérien est noethérien. Inversement, tout espace topologique réunion finie de sous-espaces noethériens est noethérien.

(2.2.4) Tout espace noethérien est quasi-compact ; inversement, tout espace topologique dans lequel tout ouvert est quasi-compact est noethérien.

(2.2.5) Un espace noethérien n'a qu'un nombre fini de composantes irréductibles, comme on le voit par récurrence noethérienne.

## § 3. COMPLÉMENTS SUR LES FAISCEAUX

## 3.1. Faisceaux à valeurs dans une catégorie.

(3.1.1) Soient K une catégorie,  $(\mathbf{A}_{\alpha})_{\alpha\in\mathbb{I}}, (\mathbf{A}_{\alpha\beta})_{(\alpha,\beta)\in\mathbb{I}\times\mathbb{I}}$  deux familles d'objets de K telles que  $A_{\beta\alpha}=A_{\alpha\beta}, (\rho_{\alpha\beta})_{(\alpha,\beta)\in\mathbb{I}\times\mathbb{I}}$  une famille de morphismes  $\rho_{\alpha\beta}:A_{\alpha}\to A_{\alpha\beta}$ . Nous dirons qu'un couple formé d'un objet A de K et d'une famille de morphismes  $\rho_{\alpha}:A\to A_{\alpha}$  est solution du problème universel défini par la donnée des familles  $(\mathbf{A}_{\alpha}), (\mathbf{A}_{\alpha\beta})$  et  $(\rho_{\alpha\beta})$  si, pour tout objet B de K, l'application qui, à tout  $f\in\mathrm{Hom}(\mathbf{B},\mathbf{A})$  fait correspondre la famille  $(\rho_{\alpha}\circ f)\in\Pi_{\alpha}\mathrm{Hom}(\mathbf{B},\mathbf{A}_{\alpha})$  est une bijection de  $\mathrm{Hom}(\mathbf{B},\mathbf{A})$  sur l'ensemble des  $(f_{\alpha})$  telles que  $\rho_{\alpha\beta}\circ f_{\alpha}=\rho_{\beta\alpha}\circ f_{\beta}$  pour tout couple d'indices  $(\alpha,\beta)$ . On voit aussitôt que s'il existe une telle solution, elle est unique à un isomorphisme près.

(3.1.2) Nous ne rappellerons pas la définition d'un préfaisceau U→F(U) sur un espace topologique X, à valeurs dans une catégorie K (G, I, 1.9); nous dirons qu'un tel préfaisceau est un faisceau à valeurs dans K s'il satisfait à l'axiome suivant :

(F) Pour tout recouvrement  $(\mathbf{U}_{\alpha})$  d'un ouvert U de X par des ouverts  $U_{\alpha}$  contenus dans U, si on désigne par  $\rho_{\alpha}$  (resp.  $\rho_{\alpha\beta}$ ) le morphisme de restriction

$$
\mathcal {F} (\mathrm{U}) \rightarrow \mathcal {F} (\mathrm{U} _ {\alpha}) \quad (\text { resp. } \mathcal {F} (\mathrm{U} _ {\alpha}) \rightarrow \mathcal {F} (\mathrm{U} _ {\alpha} \cap \mathrm{U} _ {\beta})),
$$

le couple formé de $\mathcal{F}(\mathbf{U})$ et de la famille $(\rho_{\alpha})$ est solution du problème universel pour $(\mathcal{F}(\mathbf{U}_{\alpha}))$, $(\mathcal{F}(\mathbf{U}_{\alpha}\cap \mathbf{U}_{\beta}))$ et $(\rho_{\alpha \beta})$ (3.1.1) (1).

Il revient au même de dire que, pour tout objet T de K, la famille U→Hom(T, F(U)) est un faisceau d'ensembles.

(3.1.3) Supposons que K soit la catégorie définie par une « espèce de structure avec morphismes » Σ, les objets de K étant donc les ensembles munis de structures d'espèce Σ et les morphismes ceux de Σ. Supposons que la catégorie K vérifie en outre la condition suivante :

(E) Si (A,  $(\rho_{\alpha})$ ) est solution d'un problème d'application universelle dans la catégorie K pour des familles ( $A_{\alpha}$ ),  $(A_{\alpha\beta})$ ,  $(\rho_{\alpha\beta})$ , alors c'est aussi une solution du problème d'application universelle pour les mêmes familles dans la catégorie des ensembles (c'est-à-dire quand on considère A, les  $A_{\alpha}$  et  $A_{\alpha\beta}$  comme des ensembles, les  $\rho_{\alpha}$  et  $\rho_{\alpha\beta}$  comme des applications) (2).

Dans ces conditions, la condition (F) entraîne que, considéré comme préfaisceau d'ensembles,  $\mathrm{U}\rightarrow\mathcal{F}(\mathrm{U})$  est un faisceau. En outre, pour qu'une application  $u:T\rightarrow\mathcal{F}(\mathrm{U})$  soit un morphisme de K, il faut et il suffit, en vertu de (F), que chaque application  $\rho_{\alpha}ou$  soit un morphisme  $\mathrm{T}\rightarrow\mathcal{F}(\mathrm{U}_{\alpha})$ , ce qui signifie que la structure d'espèce  $\Sigma$  sur  $\mathcal{F}(\mathrm{U})$  est structure initiale pour les morphismes  $\rho_{\alpha}$ . Réciproquement, supposons qu'un préfaisceau  $\mathrm{U}\rightarrow\mathcal{F}(\mathrm{U})$  sur X, à valeurs dans K, soit un faisceau d'ensembles, et vérifie la condition précédente; il est clair alors qu'il satisfait à (F), donc est un faisceau à valeurs dans K.

(3.1.4) Lorsque $\Sigma$ est l'espèce de structure de groupe ou d'anneau, le fait que le préfaisceau $U\to\mathcal{F}(U)$ à valeurs dans $K$ est un faisceau d'ensembles entraîne ipso facto que c'est un faisceau à valeurs dans $K$ (autrement dit, un faisceau de groupes ou d'anneaux au sens de (G)) (3). Mais il n'en est plus de même lorsque par exemple $K$ est la catégorie des anneaux topologiques (avec pour morphismes les représentations continues): un faisceau à valeurs dans $K$ est un faisceau d'anneaux $U\to\mathcal{F}(U)$ tel que, pour tout ouvert U et tout recouvrement de U par des ouverts $U_{\alpha}\subset U$, la topologie de l'anneau $\mathcal{F}(U)$ soit la moins fine rendant continues les représentations $\mathcal{F}(U)\to\mathcal{F}(U_{\alpha})$. On dira dans ce cas que $U\to\mathcal{F}(U)$ considéré comme faisceau d'anneaux (sans topologie) est sous-jacent au faisceau d'anneaux topologiques $U\to\mathcal{F}(U)$. Les morphismes $u_{V}:\mathcal{F}(V)\to\mathcal{G}(V)$ (V ouvert arbitraire de X) de faisceaux d'anneaux topologiques sont donc des homomorphismes des faisceaux d'anneaux sous-jacents, tels que $u_{V}$ soit continu pour tout ouvert $V\subset X$; pour les distinguer des homomorphismes quelconques des faisceaux d'anneaux sous-jacents, on les appellera homomorphismes continus de faisceaux d'anneaux topologiques. On a des définitions et conventions analogues pour les faisceaux d'espaces topologiques ou de groupes topologiques.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) C'est un cas particulier de la notion générale de limite projective (non filtrante) (voir (T, I, 1.8) et le livre en préparation annoncé dans l'Introduction).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) On peut prouver que cela signifie aussi que le foncteur canonique $\mathbf{K}\to(\text{Ens})$ permute aux limites projectives (non nécessairement filtrantes).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(3) Cela tient à ce que dans la catégorie K, tout morphisme qui est une bijection (en tant qu'application d'ensembles) est un isomorphisme. Cela n'est plus vrai lorsque K est la catégorie des espaces topologiques, par exemple.</span></small>

(3.1.5) Il est clair que pour toute catégorie K, si F est un préfaisceau (resp. un faisceau) sur X à valeurs dans K et U un ouvert de X, les  $\mathcal{F}(\mathrm{V})$  pour les ouverts  $V \subset U$  constituent un préfaisceau (resp. un faisceau) à valeurs dans K, que l'on appelle préfaisceau (resp. faisceau) induit par F sur U et que l'on note F | U.

Pour tout morphisme $u: \mathcal{F} \to \mathcal{G}$ de préfaisceaux sur X à valeurs dans $\boldsymbol{K}$, on désignera par $u|U$ le morphisme $\mathcal{F}|U \to \mathcal{G}|U$ formé des $u_{\mathrm{V}}$ pour $V \subset U$.

(3.1.6) Supposons maintenant que la catégorie K admette des limites inductives (T, 1.8); alors, pour tout préfaisceau (et en particulier tout faisceau) F sur X à valeurs dans K et tout  $x \in X$ , on peut définir la fibre  $F_x$  comme l'objet de K limite inductive des  $\mathcal{F}(U)$  selon l'ensemble filtrant (pour  $\supset$ ) des voisinages ouverts U de x dans X, et pour les morphismes  $\rho_{\mathrm{U}}^{\mathrm{V}} : \mathcal{F}(\mathrm{V}) \to \mathcal{F}(\mathrm{U})$ . Si  $u : F \to G$  est un morphisme de préfaisceaux à valeurs dans K, on définit pour tout  $x \in X$  le morphisme  $u_x : F_x \to G_x$  comme la limite inductive des  $u_{\mathrm{U}} : \mathcal{F}(\mathrm{U}) \to \mathcal{G}(\mathrm{U})$  selon l'ensemble des voisinages ouverts de x; on définit ainsi  $F_x$  comme foncteur covariant en F, à valeurs dans K, pour tout  $x \in X$ .

Lorsque K est en outre définie par une espèce de structure avec morphismes  $\Sigma$ , on appelle encore sections au-dessus de U d'un faisceau F à valeurs dans K les éléments de  $\mathcal{F}(\mathrm{U})$ , et on écrit alors  $\Gamma(\mathrm{U},\mathcal{F})$  au lieu de  $\mathcal{F}(\mathrm{U})$ ; pour  $s\in\Gamma(\mathrm{U},\mathcal{F})$ , V ouvert contenu dans U, on écrit  $s|V$  au lieu de  $\rho_{\mathrm{V}}^{\mathrm{U}}(s)$ ; pour tout  $x\in U$ , l'image canonique de s dans  $F_{x}$  est le germe de s au point x, noté  $s_{x}$  (nous n'emploierons jamais la notation  $s(x)$  dans ce sens, cette notation étant réservée pour une autre notion relative aux faisceaux particuliers qui seront considérés dans ce Traité (5.5.1)).

Si alors $u: \mathcal{F} \to \mathcal{G}$ est un morphisme de faisceaux à valeurs dans $\mathbf{K}$, on écrira $u(s)$ au lieu de $u_{\mathrm{V}}(s)$ pour tout $s \in \Gamma(\mathrm{U}, \mathcal{F})$.

Si $\mathcal{F}$ est un faisceau de groupes commutatifs, ou d'anneaux, ou de modules, on dit que l'ensemble des $x\in\mathbf{X}$ tels que $\mathcal{F}_{x}\neq\{0\}$ est le support de $\mathcal{F}$, noté $\operatorname{Supp}(\mathcal{F})$; cet ensemble n'est pas nécessairement fermé dans $\mathbf{X}$.

Lorsque K est définie par une espèce de structure avec morphismes, nous nous abstiendrons systématiquement de faire intervenir le point de vue des « espaces étalés » en ce qui concerne les faisceaux à valeurs dans K ; autrement dit, nous ne considérerons jamais un faisceau comme un espace topologique (ni même comme l'ensemble réunion de ses fibres), et nous ne considérerons pas davantage un morphisme  $u : F \to G$  de tels faisceaux sur X comme une application continue d'espaces topologiques.

## 3.2. Préfaisceaux sur une base d'ouverts.

(3.2.1) Nous nous restreindrons dans ce qui suit à des catégories K admettant des limites projectives (généralisées, c'est-à-dire correspondant à des ensembles préordonnés non nécessairement filtrants, cf. (T, 1.8)). Soient X un espace topologique, B une base d'ouverts pour la topologie de X. Nous appellerons préfaisceau sur B, à valeurs dans K, une famille d'objets  $\mathcal{F}(\mathrm{U})\in\mathbf{K}$ , attachés à chaque  $U\in\mathfrak{B}$ , et une famille de morphismes  $\rho_{\mathrm{U}}^{\mathrm{V}}:\mathcal{F}(\mathrm{V})\to\mathcal{F}(\mathrm{U})$  définis pour tout couple  $(\mathrm{U},\mathrm{V})$  d'éléments de B tels que  $U\subset V$ ,

avec les conditions $\rho_{\mathrm{U}}^{\mathrm{U}} =$ identité et $\rho_{\mathrm{U}}^{\mathrm{W}} = \rho_{\mathrm{U}}^{\mathrm{V}} \circ \rho_{\mathrm{V}}^{\mathrm{W}}$ si U, V, W dans $\mathfrak{B}$ sont tels que U⊂V⊂W. On peut lui associer un préfaisceau à valeurs dans $\kappa: \mathrm{U} \to \mathcal{F}'(\mathrm{U})$ au sens ordinaire, en prenant pour tout ouvert U, $\mathcal{F}'(\mathrm{U}) = \varprojlim \mathcal{F}(\mathrm{V})$, où V parcourt l'ensemble ordonné (pour c, non filtrant en général) des ensembles V ∈ B tels que V⊂U, car les $\mathcal{F}(\mathrm{V})$ forment un système projectif pour les $\rho_{\mathrm{V}}^{\mathrm{W}}$ (V⊂W⊂U, V ∈ B, W ∈ B). En effet, si U, U' sont deux ouverts de X tels que U⊂U', on définit $\rho_{\mathrm{U}}^{\prime \mathrm{U}'}$ comme la limite projective (pour V⊂U) des morphismes canoniques $\mathcal{F}'(\mathrm{U}') \to \mathcal{F}(\mathrm{V})$, autrement dit l'unique morphisme $\mathcal{F}'(\mathrm{U}') \to \mathcal{F}'(\mathrm{U})$, qui, composé avec les morphismes canoniques $\mathcal{F}'(\mathrm{U}) \to \mathcal{F}(\mathrm{V})$, donne les morphismes canoniques $\mathcal{F}'(\mathrm{U}') \to \mathcal{F}(\mathrm{V})$; la vérification de la transitivité des $\rho_{\mathrm{U}}^{\prime \mathrm{U}'}$ est alors immédiate. De plus, si U ∈ B, le morphisme canonique $\mathcal{F}'(\mathrm{U}) \to \mathcal{F}(\mathrm{U})$ est un isomorphisme, permettant d'identifier ces deux objets (1).

(3.2.2) Pour que le préfaisceau $\mathcal{F}'$ ainsi défini soit un faisceau, il faut et il suffit que le préfaisceau $\mathcal{F}$ sur $\mathfrak{B}$ vérifie la condition :

$(\mathbf{F}_{0})$ Pour tout recouvrement $(\mathbf{U}_{\alpha})$ de $\mathbf{U} \in \mathfrak{B}$ par des ensembles $\mathbf{U}_{\alpha} \in \mathfrak{B}$ contenus dans $\mathbf{U}$, et pour tout objet $\mathbf{T} \in \mathbf{K}$, l'application qui, à tout $f \in \text{Hom}(\mathbf{T}, \mathcal{F}(\mathbf{U}))$ fait correspondre la famille $(\rho_{\mathbf{U}_{\alpha}}^{\mathbf{U}} \circ f) \in \Pi_{\alpha} \text{Hom}(\mathbf{T}, \mathcal{F}(\mathbf{U}_{\alpha}))$ est une bijection de $\text{Hom}(\mathbf{T}, \mathcal{F}(\mathbf{U}))$ sur l'ensemble des $(f_{\alpha})$ tels que $\rho_{\mathbf{V}}^{\mathbf{U}_{\alpha}} \circ f_{\alpha} = \rho_{\mathbf{V}}^{\mathbf{U}_{\beta}} \circ f_{\beta}$ pour tout couple d'indices $(\alpha, \beta)$ et tout $\mathbf{V} \in \mathfrak{B}$ tel que $\mathbf{V} \subset \mathbf{U}_{\alpha} \cap \mathbf{U}_{\beta}$ (2).

La condition est évidemment nécessaire. Pour montrer qu'elle est suffisante, considérons d'abord une seconde base $\mathfrak{B}'$ de la topologie de X, contenue dans $\mathfrak{B}$, et montrons que si $\mathcal{F}''$ désigne le préfaisceau déduit de la sous-famille $(\mathcal{F}(V))_{V\in\mathfrak{B}'}$, $\mathcal{F}''$ est canoniquement isomorphe à $\mathcal{F}'$. En effet, tout d'abord la limite projective (pour $V\in\mathfrak{B}'$, $V\subset U$) des morphismes canoniques $\mathcal{F}'(U)\to\mathcal{F}(V)$ est un morphisme $\mathcal{F}'(U)\to\mathcal{F}''(U)$ pour tout ouvert U. Si $U\in\mathfrak{B}$, ce morphisme est un isomorphisme, car par hypothèse les morphismes canoniques $\mathcal{F}''(U)\to\mathcal{F}(V)$ pour $V\in\mathfrak{B}'$, $V\subset U$, se factorisent en $\mathcal{F}''(U)\to\mathcal{F}(U)\to\mathcal{F}(V)$, et il est immédiat de voir que les composés des morphismes $\mathcal{F}(U)\to\mathcal{F}''(U)$ et $\mathcal{F}''(U)\to\mathcal{F}(U)$ ainsi définis sont les identités. Ceci étant, pour tout ouvert U, les morphismes $\mathcal{F}''(U)\to\mathcal{F}''(W)=\mathcal{F}(W)$ pour $W\in\mathfrak{B}$ et $W\subset U$ vérifient les conditions caractérisant la limite projective des $\mathcal{F}(W)$ ($W\in\mathfrak{B}$, $W\subset U$), ce qui démontre notre assertion compte tenu de l'unicité d'une limite projective à un isomorphisme près.

Cela posé, soit U un ouvert quelconque de X,  $(\mathrm{U}_{\alpha})$  un recouvrement de U par des ouverts contenus dans U, et soit B' la sous-famille de B constituée par les ensembles

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{F}^{\prime}(\mathbf{U})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(i, j)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$(\mathbf{V}_{ijk})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">X, il ya</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(i, j, k)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$(\mathbf{V}_i)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{V}_i \cap \mathbf{V}_j$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Si X est un espace noethérien, on peut encore définir $\mathcal{F}'(\mathrm{U})$ et montrer que c'est un préfaisceau (au sens ordinaire) lorsqu'on suppose seulement que $\boldsymbol{K}$ admet des limites projectives pour les systèmes projectifs finis. En effet, si U est un ouvert quelconque de X, il y a un recouvrement fini ($V_i$) de U formé d'ensembles de $\mathfrak{B}$; pour tout couple $(i,j)$ d'indices, soit ($V_{ijk}$) un recouvrement fini de $V_i \cap V_j$ formé d'ensembles de $\mathfrak{B}$. Soit I l'ensemble formé des $i$ et des triplets $(i,j,k)$, ordonné par les seules relations $i > (i,j,k), j > (i,j,k)$; on prend alors pour $\mathcal{F}'(\mathrm{U})$ la limite projective du système des $\mathcal{F}(\mathrm{V}_i)$ et $\mathcal{F}(\mathrm{V}_{ijk})$; on vérifie aisément que cela ne dépend pas des recouvrements ($V_i$) et ($V_{ijk}$) et que $\mathrm{U} \to \mathcal{F}'(\mathrm{U})$ est un préfaisceau.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$i > (i, j, k), j > (i, j, k)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{F}(\mathbf{V}_i)$ et $\mathcal{F}(\mathbf{V}_{ijk})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{F}^{\prime}(\mathbf{U})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$(\mathbf{V}_{ijk})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$(\mathbf{V}_i)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{U}\rightarrow \mathcal{F}^{\prime}(\mathbf{U})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{F}(\mathbf{U})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\rho_{\alpha} = \rho_{\mathrm{U}_{\alpha}}^{\mathrm{U}}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(3.1.1)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathcal{F}(\mathrm{U}_{\alpha}) \to \Pi \mathcal{F}(\mathrm{V})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(2) Cela signifie encore que le couple formé par $\mathcal{F}(\mathrm{U})$ et les $\rho_{\alpha} = \rho_{\mathrm{U}_{\alpha}}^{\mathrm{U}}$ est solution du problème universel défini (3.1.1) par la donnée de $\mathrm{A}_{\alpha} = \mathcal{F}(\mathrm{U}_{\alpha})$, $\mathrm{A}_{\alpha \beta} = \Pi \mathcal{F}(\mathrm{V})$ (pour les $\mathrm{V} \in \mathfrak{B}$ tels que $\mathrm{V} \subset \mathrm{U}_{\alpha} \cap \mathrm{U}_{\beta}$) et $\rho_{\alpha \beta} = (\rho_{\mathrm{V}}^{\prime \prime}) : \mathcal{F}(\mathrm{U}_{\alpha}) \to \Pi \mathcal{F}(\mathrm{V})$ défini par la condition que pour $\mathrm{V} \in \mathfrak{B}$, $\mathrm{V}' \in \mathfrak{B}$, $\mathrm{W} \in \mathfrak{B}$, $\mathrm{V} \cup \mathrm{V}' \subset \mathrm{U}_{\alpha} \cap \mathrm{U}_{\beta}$, $\mathrm{W} \subset \mathrm{V} \cap \mathrm{V}'$, $\rho_{\mathrm{W}}^{\mathrm{V}} \circ \rho_{\mathrm{V}}^{\prime \prime} = \rho_{\mathrm{W}}^{\mathrm{V}'} \circ \rho_{\mathrm{V}'}^{\prime \prime}$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathrm{A}_{\alpha} = \mathcal{F}(\mathrm{U}_{\alpha}),\mathrm{A}_{\alpha \beta} = \Pi \mathcal{F}(\mathrm{V})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{V}\subset \mathbf{U}_{\alpha}\cap \mathbf{U}_{\beta})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\rho_{\alpha \beta} = (\rho_{V}^{\prime \prime})$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\rho_{\mathrm{W}}^{\mathrm{V}} \circ \rho_{\mathrm{V}}^{\prime \prime} = \rho_{\mathrm{W}}^{\mathrm{V}'} \circ \rho_{\mathrm{V}}^{\prime \prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\mathbf{V}\cup \mathbf{V}^{\prime}\subset \mathbf{U}_{\alpha}\cap \mathbf{U}_{\beta},\mathbf{W}\subset \mathbf{V}\cap \mathbf{V}^{\prime},$</span></small>

de B contenus dans un  $U_{\alpha}$  au moins ; il est clair que  $B'$  est encore une base de la topologie de X, donc  $\mathcal{F}'(U)$  (resp.  $\mathcal{F}'(U_{\alpha})$ ) est limite projective des  $\mathcal{F}(V)$  pour  $V \in B'$  et  $V \subset U$  (resp.  $V \subset U_{\alpha}$ ); l'axiome (F) se vérifie alors aussitôt en vertu de la définition de la limite projective.

Lorsque  $(\mathrm{F}_{0})$  est vérifié, nous dirons par abus de langage que le préfaisceau F sur la base B est un faisceau.

(3.2.3) Soient $\mathcal{F}$, $\mathcal{G}$ deux préfaisceaux sur la base $\mathfrak{B}$, à valeurs dans $K$; on définit un morphisme $u: \mathcal{F} \to \mathcal{G}$ comme une famille $(u_{\mathrm{V}})_{\mathrm{V} \in \mathfrak{B}}$ de morphismes $u_{\mathrm{V}}: \mathcal{F}(\mathrm{V}) \to \mathcal{G}(\mathrm{V})$ satisfaisant aux conditions de compatibilité usuelles avec les morphismes de restriction $\rho_{\mathrm{V}}^{\mathrm{W}}$. Avec les notations de (3.2.1), on en déduit un morphisme $u': \mathcal{F}' \to \mathcal{G}'$ des préfaisceaux (ordinaires) correspondants en prenant pour $u_{\mathrm{U}}'$ la limite projective des $u_{\mathrm{V}}$ pour $\mathrm{V} \in \mathfrak{B}$ et $\mathrm{V} \subset \mathrm{U}$; la vérification des conditions de compatibilité avec les $\rho_{\mathrm{U}}^{\prime \mathrm{U}'}$ découle du caractère fonctoriel de la limite projective.

(3.2.4) Si la catégorie K admet des limites inductives, et si F est un préfaisceau sur la base B, à valeurs dans K, pour tout  $x \in X$  les voisinages de x appartenant à B forment un ensemble cofinal (pour  $\supset$ ) dans l'ensemble des voisinages de x, donc, si  $F'$  est le préfaisceau (ordinaire) correspondant à F, la fibre  $F'_{x}$  est égale à  $\varinjlim_{\mathfrak{B}} \mathcal{F}(V)$  selon

l'ensemble des V∈B contenant x. Si u : F→G est un morphisme de préfaisceaux sur B à valeurs dans K, u' : F'→G' le morphisme correspondant de préfaisceaux ordinaires, u'\_x est de même la limite inductive des morphismes u\_V : F(V)→G(V) pour V∈B, x∈V.

(3.2.5) Revenons aux conditions générales de (3.2.1). Si $\mathcal{F}$ est un faisceau ordinaire à valeurs dans $K$, $\mathcal{F}_1$ le faisceau sur $\mathcal{B}$ obtenu par restriction de $\mathcal{F}$ à $\mathcal{B}$, le faisceau ordinaire $\mathcal{F}_1'$ obtenu à partir de $\mathcal{F}_1$ par le procédé de (3.2.1) est canoniquement isomorphe à $\mathcal{F}$, en vertu de la condition (F) et des propriétés d'unicité de la limite projective. On identifiera d'ordinaire $\mathcal{F}$ et $\mathcal{F}_1'$.

Si $\mathcal{G}$ est un second faisceau (ordinaire) sur X à valeurs dans $\kappa$, et $u: \mathcal{F} \to \mathcal{G}$ un morphisme, la remarque précédente montre que la donnée des $u_{\mathrm{V}}: \mathcal{F}(\mathrm{V}) \to \mathcal{G}(\mathrm{V})$ pour les $\mathrm{V} \in \mathfrak{B}$ seulement détermine complètement $u$; inversement, il suffit, les $u_{\mathrm{V}}$ étant donnés pour $\mathrm{V} \in \mathfrak{B}$, de vérifier le diagramme de commutativité avec les morphismes de restriction $\rho_{\mathrm{V}}^{\mathrm{W}}$ pour $\mathrm{V} \in \mathfrak{B}$, $\mathrm{W} \in \mathfrak{B}$ et $\mathrm{V} \subset \mathrm{W}$, pour qu'il existe un morphisme $u'$ et un seul de $\mathcal{F}$ dans $\mathcal{G}$ tel que $u_{\mathrm{V}}' = u_{\mathrm{V}}$ pour tout $\mathrm{V} \in \mathfrak{B}$ (3.2.3).

(3.2.6) Supposons toujours que K admette des limites projectives. Alors la catégorie des faisceaux sur X à valeurs dans K admet aussi des limites projectives ; si  $(\mathcal{F}_{\lambda})$  est un système projectif de faisceaux sur X à valeurs dans K, les  $\mathcal{F}(\mathrm{U}) = \varprojlim_{\lambda} \mathcal{F}_{\lambda}(\mathrm{U})$

définissent en effet un préfaisceau à valeurs dans K, et la vérification de l'axiome (F) résulte de la transitivité des limites projectives ; le fait que F est alors limite projective des  $F_{\lambda}$  est immédiat.

Lorsque K est la catégorie des ensembles, pour tout système projectif  $(\mathfrak{H}_{\lambda})$  tel

que $\mathfrak{H}_{\lambda}$ soit un sous-faisceau de $\mathcal{F}_{\lambda}$ pour tout $\lambda$, $\varprojlim \mathfrak{H}_{\lambda}$ s'identifie canoniquement à un sous-faisceau de $\varprojlim \mathcal{F}_{\lambda}$. Si $\kappa$ est la catégorie des groupes commutatifs, le foncteur covariant $\varprojlim \mathcal{F}_{\lambda}$ est additif et exact à gauche.

## 3.3. Recollement de faisceaux.

(3.3.1) Supposons encore que la catégorie K admette des limites projectives (généralisées). Soient X un espace topologique,  $\mathfrak{U}=(\mathrm{U}_{\lambda})_{\lambda\in\mathrm{L}}$  un recouvrement ouvert de X, et pour chaque  $\lambda\in L$, soit  $F_{\lambda}$  un faisceau sur  $U_{\lambda}$, à valeurs dans K; pour tout couple d'indices  $(\lambda,\mu)$, supposons donné un isomorphisme  $\theta_{\lambda\mu}:F_{\mu}|(\mathrm{U}_{\lambda}\cap\mathrm{U}_{\mu})\simeq F_{\lambda}|(\mathrm{U}_{\lambda}\cap\mathrm{U}_{\mu})$; en outre, supposons que pour tout triplet  $(\lambda,\mu,\nu)$, en désignant par  $\theta_{\lambda\mu}^{\prime},\theta_{\mu\nu}^{\prime},\theta_{\lambda\nu}^{\prime}$  les restrictions de  $\theta_{\lambda\mu},\theta_{\mu\nu},\theta_{\lambda\nu}$  à  $U_{\lambda}\cap U_{\mu}\cap U_{\nu}$, on ait  $\theta_{\lambda\nu}^{\prime}=\theta_{\lambda\mu}^{\prime}\circ\theta_{\mu\nu}^{\prime}$  (condition de recollement pour les  $\theta_{\lambda\mu}$). Alors, il existe un faisceau F sur X, à valeurs dans K, et pour chaque  $\lambda$  un isomorphisme  $\eta_{\lambda}:F|U_{\lambda}\simeq F_{\lambda}$  tels que, pour tout couple  $(\lambda,\mu)$, en désignant par  $\eta_{\lambda}^{\prime}$  et  $\eta_{\mu}^{\prime}$  les restrictions de  $\eta_{\lambda}$  et  $\eta_{\mu}$  à  $U_{\lambda}\cap U_{\mu}$, on ait  $\theta_{\lambda\mu}=\eta_{\lambda}^{\prime}\circ\eta_{\mu}^{\prime-1}$; en outre, F et les  $\eta_{\lambda}$  sont déterminés à un isomorphisme unique près par ces conditions. L'unicité résulte en effet aussitôt de (3.2.5). Pour établir l'existence de F, désignons par B la base d'ouverts formée des ouverts contenus dans un  $U_{\lambda}$  au moins, et pour tout  $U\in B$, choisissons (par la fonction  $\tau$  de Hilbert) un des  $\mathcal{F}_{\lambda}(U)$  pour un des  $\lambda$  tels que  $U\subset U_{\lambda}$; si on désigne cet objet par  $\mathcal{F}(U)$, les  $\rho_{U}^{V}$  pour  $U\subset V, U\in B, V\in B$  se définissent de façon évidente (au moyen des  $\theta_{\lambda\mu}$), et la condition de transitivité est conséquence de la condition de recollement; en outre, la vérification de  $(\mathrm{F}_{0})$  est immédiate, donc le préfaisceau sur B ainsi défini est bien un faisceau, et on en déduit par le procédé général (3.2.1) un faisceau (ordinaire) encore noté F et qui répond à la question. On dit que F est obtenu par recollement des  $F_{\lambda}$  au moyen des  $\theta_{\lambda\mu}$  et on identifiera d'ordinaire  $F_{\lambda}$  et F|U $_{\lambda}$  au moyen de  $\eta_{\lambda}$.

Il est clair que tout faisceau $\mathcal{F}$ sur X à valeurs dans $K$ peut être considéré comme obtenu par recollement des faisceaux $\mathcal{F}_{\lambda} = \mathcal{F}|U_{\lambda}$ (où $(U_{\lambda})$ est un recouvrement ouvert arbitraire de X), au moyen des isomorphismes $\theta_{\lambda \mu}$ réduits à l'identité.

(3.3.2) Avec les mêmes notations, soit $\mathcal{G}_{\lambda}$ un second faisceau sur $\mathrm{U}_{\lambda}$ (pour tout $\lambda \in \mathrm{L}$) à valeurs dans $\pmb{K}$, et soit donné pour tout couple ($\lambda, \mu$) un isomorphisme $\omega_{\lambda \mu}: \mathcal{G}_{\mu}|(\mathrm{U}_{\lambda} \cap \mathrm{U}_{\mu}) \simeq \mathcal{G}_{\lambda}|(\mathrm{U}_{\lambda} \cap \mathrm{U}_{\mu})$, ces isomorphismes vérifiant la condition de recollement. Supposons enfin donné pour tout $\lambda$ un morphisme $u_{\lambda}: \mathcal{F}_{\lambda} \to \mathcal{G}_{\lambda}$, et que les diagrammes

$$
\begin{array}{c} \mathcal {F} _ {\mu}   |   (\mathrm{U} _ {\lambda} \cap \mathrm{U} _ {\mu}) \stackrel {{u _ {\mu}}} {{\to}} \mathcal {G} _ {\mu}   |   (\mathrm{U} _ {\lambda} \cap \mathrm{U} _ {\mu}) \\ \downarrow \\ \mathcal {F} _ {\lambda}   |   (\mathrm{U} _ {\lambda} \cap \mathrm{U} _ {\mu}) \stackrel {{u _ {\lambda}}} {{\to}} \mathcal {G} _ {\lambda}   |   (\mathrm{U} _ {\lambda} \cap \mathrm{U} _ {\mu}) \end{array}\tag{3.3.2.1}
$$

soient commutatifs. Alors, si $\mathcal{G}$ est obtenu par recollement des $\mathcal{G}_{\lambda}$ au moyen des $\omega_{\lambda\mu}$, il existe un morphisme $u: \mathcal{F} \to \mathcal{G}$ et un seul tel que les diagrammes

$$
\begin{array}{c c c} \mathcal {F} | \mathrm{U} _ {\lambda} & \stackrel {{u | \mathrm{U} _ {\lambda}}} {{\longrightarrow}} & \mathcal {G} | \mathrm{U} _ {\lambda} \\ \downarrow & & \downarrow \\ \mathcal {F} _ {\lambda} & \stackrel {{u _ {\lambda}}} {{\longrightarrow}} & \mathcal {G} _ {\lambda} \end{array}
$$

soient commutatifs ; cela résulte aussitôt de (3.2.3). La correspondance entre la famille  $(u_{\lambda})$  et u est une bijection fonctorielle de la partie de  $\Pi\operatorname{Hom}(\mathcal{F}_{\lambda},\mathcal{G}_{\lambda})$  vérifiant les conditions (3.3.2.1) sur  $\operatorname{Hom}(\mathcal{F},\mathcal{G})$ .

(3.3.3) Avec les notations de (3.3.1), soit V un ouvert de X ; il est immédiat que les restrictions à  $V \cap U_{\lambda} \cap U_{\mu}$  des  $\theta_{\lambda\mu}$  satisfont à la condition de recollement pour les faisceaux induits  $\mathcal{F}_{\lambda}|(\mathrm{V} \cap \mathrm{U}_{\lambda})$  et que le faisceau sur V obtenu par recollement de ces derniers s'identifie canoniquement à F|V.

## 3.4. Images directes de préfaisceaux.

(3.4.1) Soient X, Y deux espaces topologiques, $\psi : X \to Y$ une application continue. Soit $\mathcal{F}$ un préfaisceau sur X à valeurs dans une catégorie $K$; pour tout ouvert U⊂Y, soit $\mathcal{G}(U) = \mathcal{F}(\psi^{-1}(U))$, et si U, V sont deux parties ouvertes de Y telles que U⊂V, soit $\rho_{U}^{V}$ le morphisme $\mathcal{F}(\psi^{-1}(V)) \to \mathcal{F}(\psi^{-1}(U))$; il est immédiat que les $\mathcal{G}(U)$ et les $\rho_{U}^{V}$ définissent un préfaisceau sur Y à valeurs dans $K$, que l'on appelle l'image directe de $\mathcal{F}$ par $\psi$ et que l'on note $\psi_{*}(\mathcal{F})$. Si $\mathcal{F}$ est un faisceau, on vérifie aussitôt l'axiome (F) pour le préfaisceau $\mathcal{G}(U)$, donc $\psi_{*}(\mathcal{F})$ est un faisceau.

(3.4.2) Soient $\mathcal{F}_1$, $\mathcal{F}_2$ deux préfaisceaux sur X à valeurs dans K, et soit $u: \mathcal{F}_1 \to \mathcal{F}_2$ un morphisme. Lorsque U parcourt l'ensemble des parties ouvertes de Y, la famille de morphismes $u_{\psi^{-1}(U)}: \mathcal{F}_1(\psi^{-1}(U)) \to \mathcal{F}_2(\psi^{-1}(U))$ satisfait aux conditions de compatibilité avec les morphismes de restriction, et définit par suite un morphisme $\psi_*(u): \psi_*(\mathcal{F}_1) \to \psi_*(\mathcal{F}_2)$. Si $v: \mathcal{F}_2 \to \mathcal{F}_3$ est un morphisme de $\mathcal{F}_2$ dans un troisième préfaisceau sur X à valeurs dans K, on a $\psi_*(v \circ u) = \psi_*(v) \circ \psi_*(u)$; autrement dit, $\psi_*(\mathcal{F})$ est un foncteur covariant en $\mathcal{F}$, de la catégorie des préfaisceaux (resp. faisceaux) sur X à valeurs dans K, dans celle des préfaisceaux (resp. faisceaux) sur Y à valeurs dans K.

(3.4.3) Soient Z un troisième espace topologique, $\psi': Y \to Z$ une application continue, et soit $\psi'' = \psi' \circ \psi$. Il est clair que l'on a $\psi'_*(\mathcal{F}) = \psi'_*(\psi_*(\mathcal{F}))$ pour tout préfaisceau $\mathcal{F}$ sur X à valeurs dans $K$; en outre, pour tout morphisme $u: \mathcal{F} \to \mathcal{G}$ de tels préfaisceaux, on a $\psi''_*(u) = \psi'_*(\psi_*(u))$. En d'autres termes, $\psi''_*$ est le composé des foncteurs $\psi'_*$ et $\psi_*$, ce qu'on peut écrire

$$
\left(\psi^ {\prime} \circ \psi\right) _ {*} = \psi_ {*} ^ {\prime} \circ \psi_ {*}.
$$

En outre, pour tout ouvert U de Y, l'image par la restriction $\psi|\psi^{-1}(\mathbf{U})$ du préfaisceau induit $\mathcal{F}|\psi^{-1}(\mathbf{U})$ n'est autre que le préfaisceau induit $\psi_{*}(\mathcal{F})|\mathbf{U}$.

(3.4.4) Supposons que la catégorie K admette des limites inductives, et soit F un préfaisceau sur X à valeurs dans K; pour tout  $x \in X$ , les morphismes  $\Gamma(\psi^{-1}(U), \mathcal{F}) \to \mathcal{F}_{x}$  (U voisinage ouvert de  $\psi(x)$  dans Y) forment un système inductif, qui donne par passage

à la limite un morphisme $\psi_x : (\psi_*(\mathcal{F}))_{\psi(x)} \to \mathcal{F}_x$ des fibres; en général, ce morphisme n'est ni injectif ni surjectif. Il est fonctoriel; en effet, si $u : \mathcal{F}_1 \to \mathcal{F}_2$ est un morphisme de préfaisceaux sur X à valeurs dans K, le diagramme

$$
\begin{array}{c}\left(\psi_ {*} (\mathcal {F} _ {1})\right) _ {\psi (x)} \stackrel {{\psi_ {x}}} {{\to}} \left(\mathcal {F} _ {1}\right) _ {x}\\\left.\begin{array}{c}\left(\psi_ {*} (u)\right) _ {\psi (x)} \Bigg \downarrow\\\left(\psi_ {*} (\mathcal {F} _ {2})\right) _ {\psi (x)} \stackrel {{\rightarrow}} {{\to}} \left(\mathcal {F} _ {2}\right) _ {x}\end{array}\right.\end{array}
$$

est commutatif. Si Z est un troisième espace topologique, $\psi':\mathrm{Y}\to\mathrm{Z}$ une application continue, et $\psi''=\psi'\circ\psi$, on a $\psi_x''=\psi_x\circ\psi_{\psi(x)}'$ pour $x\in\mathbf{X}$.

3.4.5) Sous les hypothèses de (3.4.4), supposons en outre que $\psi$ soit un homéomorphisme de X sur le sous-espace $\psi(X)$ de Y. Alors, pour tout $x\in X$, $\psi_x$ est un isomorphisme. Ceci s'applique en particulier à l'injection canonique $j$ d'une partie X de Y dans Y.

(3.4.6) Supposons que K soit la catégorie des groupes, ou des anneaux, etc. Si F est un faisceau sur X à valeurs dans K, de support S, et si  $y \notin \overline{\psi(S)}$ , il résulte de la définition de  $\psi_{*}(\mathcal{F})$  que  $(\psi_{*}(\mathcal{F}))_{y} = \{0\}$ , autrement dit le support de  $\psi_{*}(\mathcal{F})$  est contenu dans  $\overline{\psi(S)}$ ; mais il n'est pas nécessairement contenu dans  $\psi(S)$ . Sous les mêmes hypothèses, si j est l'injection canonique d'une partie X de Y dans Y, le faisceau  $j_{*}(\mathcal{F})$  induit F sur X; si de plus X est fermée dans Y,  $j_{*}(\mathcal{F})$  est le faisceau sur Y qui induit F sur X et o sur Y—X (G, II, 2.9.2), mais il est en général distinct de ce dernier lorsqu'on suppose X localement fermé mais non fermé.

## 3.5. Images réciproques de préfaisceaux.

(3.5.1) Sous les hypothèses de (3.4.1), si $\mathcal{F}$ (resp. $\mathcal{G}$) est un préfaisceau sur X (resp. Y) à valeurs dans $K$, tout morphisme $u: \mathcal{G} \to \psi_*(\mathcal{F})$ de préfaisceaux sur Y s'appelle encore un $\psi$-morphisme de $\mathcal{G}$ dans $\mathcal{F}$, et se note aussi $\mathcal{G} \to \mathcal{F}$. On désigne aussi par $\mathrm{Hom}_{\psi}(\mathcal{G}, \mathcal{F})$ l'ensemble $\mathrm{Hom}_{\mathrm{Y}}(\mathcal{G}, \psi_*(\mathcal{F}))$ des $\psi$-morphismes de $\mathcal{G}$ dans $\mathcal{F}$. Pour tout couple (U, V), où U est un ouvert de X, V un ouvert de Y tel que $\psi(U) \subset V$, on a un morphisme $u_{U,V}: \mathcal{G}(V) \to \mathcal{F}(U)$ en composant le morphisme de restriction $\mathcal{F}(\psi^{-1}(V)) \to \mathcal{F}(U)$ et le morphisme $u_V: \mathcal{G}(V) \to \psi_*(\mathcal{F})(V) = \mathcal{F}(\psi^{-1}(V))$; il est immédiat que ces morphismes rendent commutatifs les diagrammes

$$
\begin{array}{c c c} \mathcal {G} (\mathrm{V}) & \xrightarrow {u _ {\mathrm{U} , \mathrm{v}}} & \mathcal {F} (\mathrm{U}) \\ \downarrow & & \downarrow \\ \mathcal {G} (\mathrm{V} ^ {\prime}) & \xrightarrow {u _ {\mathrm{U} ^ {\prime} , \mathrm{v} ^ {\prime}}} & \mathcal {F} (\mathrm{U} ^ {\prime}) \end{array}\tag{3.5.1.1}
$$

pour  $U^{\prime} \subset U$ ,  $V^{\prime} \subset V$ ,  $\psi(U^{\prime}) \subset V^{\prime}$ . Inversement, la donnée d'une famille  $(u_{\mathrm{U},\mathrm{V}})$  de morphismes rendant commutatifs les diagrammes (3.5.1.1) définit un  $\psi$ -morphisme u, car il suffit de prendre  $u_{\mathrm{V}} = u_{\psi^{-1}(\mathrm{V}),\mathrm{V}}$ .

Si la catégorie K admet des limites projectives (généralisées), et si B, B' sont des bases des topologies de X et Y respectivement, pour définir un ψ-morphisme u de faisceaux, on peut se borner à se donner les  $u_{U,V}$  pour  $U \in B$ ,  $V \in B'$  et  $\psi(U) \subset V$ , vérifiant les conditions de compatibilité (3.5.1.1) pour U,  $U'$  dans B et V,  $V'$  dans B'; il suffit en effet de définir  $u_{W}$ , pour tout ouvert  $W \subset Y$ , comme limite projective des  $u_{U,V}$  pour  $V \in B'$  et  $V \subset W$ ,  $U \in B$  et  $\psi(U) \subset V$ .

Lorsque la catégorie K admet des limites inductives, on a, pour tout  $x \in X$ , un morphisme  $\mathcal{G}(V) \to \mathcal{F}(\psi^{-1}(V)) \to \mathcal{F}_x$  pour tout voisinage ouvert V de  $\psi(x)$  dans Y, et ces morphismes forment un système inductif qui donne par passage à la limite un morphisme  $\mathcal{G}_{\psi(x)} \to \mathcal{F}_x$ .

(3.5.2) Sous les hypothèses de (3.4.3), soient $\mathcal{F}$, $\mathcal{G}$, $\mathcal{H}$ des préfaisceaux à valeurs dans $\pmb{\kappa}$ sur X, Y, Z respectivement, et soient $u: \mathcal{G} \to \psi_*(\mathcal{F})$, $v: \mathcal{H} \to \psi_*(\mathcal{G})$ un $\psi$-morphisme et un $\psi'$-morphisme respectivement. On en déduit un $\psi''$-morphisme $w: \mathcal{H} \xrightarrow{v} \psi_*(\mathcal{G}) \xrightarrow{\psi'_*(u)} \psi_*(\psi_*(\mathcal{F})) = \psi'_*(\mathcal{F})$, que l'on appelle, par définition, le composé de $u$ et de $v$. On peut donc considérer les couples (X, $\mathcal{F}$) formés d'un espace topologique X et d'un préfaisceau $\mathcal{F}$ sur X (à valeurs dans $\pmb{k}$) comme formant une catégorie, les morphismes étant les couples ($\psi, \theta$): (X, $\mathcal{F}$)→(Y, $\mathcal{G}$) formés d'une application continue $\psi: X \to Y$ et d'un $\psi$-morphisme $\theta: \mathcal{G} \to \mathcal{F}$.

(3.5.3) Soient $\psi : X \to Y$ une application continue, $\mathcal{G}$ un préfaisceau sur $Y$ à valeurs dans $\boldsymbol{K}$. Nous appellerons image réciproque de $\mathcal{G}$ par $\psi$ un couple $(\mathcal{G}', \rho)$, où $\mathcal{G}'$ est un faisceau sur $X$ à valeurs dans $\boldsymbol{K}$, et $\rho : \mathcal{G} \to \mathcal{G}'$ un $\psi$-morphisme (autrement dit un homomorphisme $\mathcal{G} \to \psi_*(\mathcal{G}')$) tels que, pour tout faisceau $\mathcal{F}$ sur $X$ à valeurs dans $\boldsymbol{K}$, l'application

$$
\operatorname{Hom} _ {\mathrm{X}} \left(\mathcal {G} ^ {\prime}, \mathcal {F}\right)\rightarrow \operatorname{Hom} _ {\psi} (\mathcal {G}, \mathcal {F}) = \operatorname{Hom} _ {\mathrm{Y}} \left(\mathcal {G}, \psi_ {*} (\mathcal {F})\right)\tag{3.5.3.1}
$$

transformant $v$ en $\psi_{*}(v)\circ\rho$, soit une bijection ; cette application, étant fonctorielle en $\mathcal{F}$, définira alors un isomorphisme de foncteurs en $\mathcal{F}$. Le couple $(\mathcal{G}',\rho)$ étant solution d'un problème universel, on sait qu'il est déterminé à un isomorphisme unique près lorsqu'il existe. On écrira alors $\mathcal{G}'=\psi^{*}(\mathcal{G})$, $\rho=\rho_{\mathcal{G}}$, et par abus de langage, on dira que $\psi^{*}(\mathcal{G})$ est le faisceau image réciproque de $\mathcal{G}$ par $\psi$, étant entendu que $\psi^{*}(\mathcal{G})$ est considéré comme muni du $\psi$-morphisme canonique $\rho_{\mathcal{G}}:\mathcal{G}\to\psi^{*}(\mathcal{G})$, c'est-à-dire de l'homomorphisme canonique de préfaisceaux sur Y :

$$
\rho_ {\mathcal {G}}: \mathcal {G} \rightarrow \psi_ {*} (\psi^ {*} (\mathcal {G})).\tag{3.5.3.2}
$$

Pour tout homomorphisme $v: \psi^{*}(\mathcal{G}) \to \mathcal{F}$ (où $\mathcal{F}$ est un faisceau sur X à valeurs dans $\mathbf{K}$), on posera $v^{\flat} = \psi_{*}(v) \circ \rho_{\mathcal{G}}: \mathcal{G} \to \psi_{*}(\mathcal{F})$. Par définition, tout morphisme de préfaisceaux $u: \mathcal{G} \to \psi_{*}(\mathcal{F})$ est de la forme $v^{\flat}$ pour un $v$ et un seul, que l'on notera $u^{\sharp}$. En d'autres termes, tout morphisme $u: \mathcal{G} \to \psi_{*}(\mathcal{F})$ de préfaisceaux se factorise de façon unique en

$$
u: \mathcal {G} \stackrel {{\rho_ {\mathcal {G}}}} {{\rightarrow}} \psi_ {*} (\psi^ {*} (\mathcal {G})) \stackrel {{\psi_ {*} (u ^ {\#})}} {{\longrightarrow}} \psi_ {*} (\mathcal {F}).\tag{3.5.3.3}
$$

(3.5.4) Supposons maintenant que la catégorie K soit telle (1) que tout pré-faisceau G sur Y à valeurs dans K admette une image réciproque par  $\psi$ , que nous noterons  $\psi^{*}(\mathcal{G})$ .

Nous allons voir qu'on peut définir $\psi^{*}(\mathcal{G})$ comme foncteur covariant en $\mathcal{G}$, de la catégorie des préfaisceaux sur Y à valeurs dans $\boldsymbol{K}$, dans celle des faisceaux sur X à valeurs dans $\boldsymbol{K}$, de telle façon que l'isomorphisme $v\to v^{\flat}$ soit un isomorphisme de bifoncteurs

$$
\operatorname{Hom} _ {\mathrm{X}} \left(\psi^ {*} (\mathcal {G}), \mathcal {F}\right) \simeq \operatorname{Hom} _ {\mathrm{Y}} \left(\mathcal {G}, \psi_ {*} (\mathcal {F})\right)\tag{3.5.4.1}
$$

en $\mathcal{G}$ et $\mathcal{F}$.

En effet, pour tout morphisme $w: \mathcal{G}_1 \to \mathcal{G}_2$ de préfaisceaux sur Y à valeurs dans $K$, considérons le morphisme composé $\mathcal{G}_1 \xrightarrow{w} \mathcal{G}_2 \xrightarrow{\rho_{\mathcal{G}_2}} \psi_*(\psi^*(\mathcal{G}_2))$; il lui correspond un morphisme $(\rho_{\mathcal{G}_2} \circ w)^{\#}: \psi^*(\mathcal{G}_1) \to \psi^*(\mathcal{G}_2)$, que nous noterons $\psi^*(w)$. On a donc, en vertu de (3.5.3.3)

$$
\psi_ {*} (\psi^ {*} (w)) \circ \rho_ {\mathcal {G} _ {1}} = \rho_ {\mathcal {G} _ {2}} \circ w.\tag{3.5.4.2}
$$

Pour tout morphisme $u: \mathcal{G}_2 \to \psi_*(\mathcal{F})$, où $\mathcal{F}$ est un faisceau sur $X$ à valeurs dans $K$, on $a$, d'après (3.5.3.3), (3.5.4.2) et la définition de $u^\flat$

$$
(u ^ {\sharp} \circ \psi^ {*} (w)) ^ {b} = \psi_ {*} (u ^ {\sharp}) \circ \psi_ {*} (\psi^ {*} (w)) \circ \rho_ {\mathcal {G} _ {1}} = \psi_ {*} (u ^ {\sharp}) \circ \rho_ {\mathcal {G} _ {2}} \circ w = u \circ w
$$

ou encore

$$
(u \circ w) ^ {\sharp} = u ^ {\sharp} \circ \psi^ {*} (w).\tag{3.5.4.3}
$$

Si on prend en particulier pour $u$ un morphisme $\mathcal{G}_{2} \xrightarrow{w'} \mathcal{G}_{3} \xrightarrow{\rho_{\mathcal{G}_{3}}} \psi_{*}(\psi^{*}(\mathcal{G}_{3}))$, il vient $\psi^{*}(w' \circ w) = (\rho_{\mathcal{G}_{3}} \circ w' \circ w)^{\#} = (\rho_{\mathcal{G}_{3}} \circ w')^{\#} \circ \psi^{*}(w) = \psi^{*}(w') \circ \psi^{*}(w)$, d'où notre assertion.

Enfin, pour tout faisceau $\mathcal{F}$ sur X à valeurs dans $\pmb{K}$, soit $i_{\mathcal{F}}$ le morphisme identique de $\psi_{*}(\mathcal{F})$ et notons

$$
\sigma_ {\mathcal {F}}: \psi^ {*} (\psi_ {*} (\mathcal {F})) \rightarrow \mathcal {F}
$$

le morphisme $(i_{\mathcal{F}})^{\#}$; la formule (3.5.4.3) donne en particulier la factorisation

$$
u ^ {\sharp}: \psi^ {*} (\mathcal {G}) \stackrel {\psi^ {*} (u)} {\longrightarrow} \psi^ {*} (\psi_ {*} (\mathcal {F})) \stackrel {\sigma_ {\mathcal {F}}} {\rightarrow} \mathcal {F}\tag{3·5·4·4}
$$

pour tout morphisme $u: \mathcal{G} \to \psi_*(\mathcal{F})$. Nous dirons que le morphisme $\sigma_{\mathcal{F}}$ est canonique. (3.5.5) Soit $\psi': Y \to Z$ une application continue, et supposons que tout pré-faisceau $\mathcal{H}$ sur $Z$ à valeurs dans $K$ admette une image réciproque $\psi'^*(\mathcal{H})$ par $\psi'$. Alors (avec les hypothèses de (3.5.4)) tout préfaisceau $\mathcal{H}$ sur $Z$ à valeurs dans $K$ admet une image réciproque par $\psi'' = \psi' \circ \psi$ et l'on a un isomorphisme canonique fonctoriel

$$
\psi^ {\prime \prime *} (\mathcal {H}) \stackrel {{\sim}} {{\to}} \psi^ {*} (\psi^ {\prime *} (\mathcal {H}))\tag{3.5.5.1}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Dans le livre cité dans l'Introduction, nous donnerons des conditions très générales sur la catégorie K assurant l'existence des images réciproques de préfaisceaux à valeurs dans K.</span></small>

Cela résulte en effet aussitôt des définitions, tenant compte de ce que $\psi_{*}^{\prime\prime} = \psi_{*}^{\prime}\circ \psi_{*}$. En outre, si $u:\mathcal{G}\to \psi_{*}(\mathcal{F})$ est un $\psi$-morphisme, $v:\mathcal{H}\to \psi_{*}^{\prime}(\mathcal{G})$ un $\psi'$-morphisme, et $w = \psi_{*}^{\prime}(u)\circ v$ leur composé (3.5.2), on constate aussitôt que $w^{\sharp}$ est le morphisme composé

$$
w ^ {\#}: \psi^ {*} (\psi^ {\prime *} (\mathcal {H})) \xrightarrow {\psi^ {*} (v ^ {\#})} \psi^ {*} (\mathcal {G}) \xrightarrow {u ^ {\#}} \mathcal {F}.
$$

(3.5.6) Prenons en particulier pour $\psi$ l'application identique $I_X: X \to X$. Alors si l'image réciproque par $\psi$ d'un préfaisceau $\mathcal{F}$ sur $X$ à valeurs dans $K$ existe, on dit que cette image réciproque est le faisceau associé au préfaisceau $\mathcal{F}$. Tout morphisme $u: \mathcal{F} \to \mathcal{F}'$ de $\mathcal{F}$ dans un faisceau $\mathcal{F}'$ à valeurs dans $K$ se factorise donc de façon unique en $\mathcal{F} \stackrel{\circ_{\mathcal{F}}}{\to} I_X^*(\mathcal{F}) \stackrel{u^\sharp}{\to} \mathcal{F}'$.

## 3.6. Faisceaux simples et faisceaux localement simples.

(3.6.1) Nous dirons qu'un préfaisceau $\mathcal{F}$ sur X, à valeurs dans $K$, est constant si les morphismes canoniques $\mathcal{F}(\mathrm{X}) \to \mathcal{F}(\mathrm{U})$ sont des isomorphismes pour tout ouvert non vide U⊂X; on notera que $\mathcal{F}$ n'est pas nécessairement un faisceau. On dit qu'un faisceau est simple s'il est associé (3.5.6) à un préfaisceau constant. On dit qu'un faisceau $\mathcal{F}$ est localement simple si tout $x \in \mathrm{X}$ admet un voisinage ouvert U tel que $\mathcal{F}|_{\mathrm{U}}$ soit simple.

(3.6.2) Supposons que X soit irréductible (2.1.1); alors les propriétés suivantes sont équivalentes :

a) $\mathcal{F}$ est un préfaisceau constant sur X;

b) $\mathcal{F}$ est un faisceau simple sur X;

c) $\mathcal{F}$ est un faisceau localement simple sur X.

En effet, soit $\mathcal{F}$ un préfaisceau constant sur X ; si U, V sont deux ouverts non vides dans X, U∩V est non vide, donc $\mathcal{F}(\mathrm{X})\to\mathcal{F}(\mathrm{U})\to\mathcal{F}(\mathrm{U}\cap\mathrm{V})$ et $\mathcal{F}(\mathrm{X})\to\mathcal{F}(\mathrm{U})$ étant des isomorphismes, il en est de même de $\mathcal{F}(\mathrm{U})\to\mathcal{F}(\mathrm{U}\cap\mathrm{V})$ et de même $\mathcal{F}(\mathrm{V})\to\mathcal{F}(\mathrm{U}\cap\mathrm{V})$ est un isomorphisme. On en conclut aussitôt que l'axiome (F) de (3.1.2) est bien vérifié, $\mathcal{F}$ est isomorphe à son faisceau associé, et par suite $a)$ entraîne $b)$.

Soit maintenant  $(\mathrm{U}_{\alpha})$  un recouvrement ouvert de X par des ouverts non vides et un faisceau F sur X tel que  $F|U_{\alpha}$  soit simple pour tout  $\alpha$ ; comme  $U_{\alpha}$  est irréductible,  $F|U_{\alpha}$  est un préfaisceau constant en vertu de ce qui précède. Comme  $U_{\alpha}\cap U_{\beta}$  n'est pas vide,  $\mathcal{F}(U_{\alpha})\to\mathcal{F}(U_{\alpha}\cap U_{\beta})$  et  $\mathcal{F}(U_{\beta})\to\mathcal{F}(U_{\alpha}\cap U_{\beta})$  sont des isomorphismes, d'où on déduit un isomorphisme canonique  $\theta_{\alpha\beta}: \mathcal{F}(U_{\alpha})\to\mathcal{F}(U_{\beta})$  pour tout couple d'indices. Mais alors, si on applique la condition (F) pour U=X, on voit que pour tout indice  $\alpha_{0}, \mathcal{F}(U_{\alpha_{0}})$  et les  $\theta_{\alpha_{0}\alpha}$  sont solutions du problème universel, ce qui (en vertu de l'unicité) implique que  $\mathcal{F}(X)\to\mathcal{F}(U_{\alpha_{0}})$  est un isomorphisme, et démontre donc que c) entraîne a).

## 3.7. Images réciproques de préfaisceaux de groupes ou d'anneaux.

(3.7.1) Nous allons montrer que lorsqu'on prend pour K la catégorie des ensembles, l'image réciproque par  $\psi$  de tout préfaisceau G à valeurs dans K existe toujours (les notations et hypothèses sur X, Y,  $\psi$  étant celles de (3.5.3)). En effet, pour tout ouvert U ⊂ X, définissons  $\mathcal{G}'(\mathrm{U})$  comme suit : un élément  $s'$  de  $\mathcal{G}'(\mathrm{U})$  est une famille  $(s_x')_{x \in \mathrm{U}}$ , où  $s_x' \in \mathcal{G}_{\psi(x)}$  pour tout  $x \in U$ , et où, pour tout  $x \in U$ , la condition suivante est remplie : il existe un voisinage ouvert V de  $\psi(x)$  dans Y, un voisinage  $W \subset \psi^{-1}(\mathrm{V}) \cap \mathrm{U}$  de x et un élément  $s \in \mathcal{G}(\mathrm{V})$  tels que  $s_z' = s_{\psi(z)}$  pour tout  $z \in W$ . On vérifie immédiatement que  $U \to \mathcal{G}'(\mathrm{U})$  satisfait bien aux axiomes des faisceaux.

Soit maintenant $\mathcal{F}$ un faisceau d'ensembles sur X, et soient $u: \mathcal{G} \to \psi_*(\mathcal{F})$, $v: \mathcal{G}' \to \mathcal{F}$ des morphismes. On définit $u^\sharp$ et $v^\flat$ de la façon suivante : si $s'$ est une section de $\mathcal{G}'$ au-dessus d'un voisinage U de $x \in X$ et si V est un voisinage ouvert de $\psi(x)$ et $s \in \mathcal{G}(V)$ tel que l'on ait $s_z' = s_{\psi(z)}$ pour $z$ dans un voisinage de $x$ contenu dans $\psi^{-1}(V) \cap U$, on prend $u_x^\sharp(s_x') = u_{\psi(x)}(s_{\psi(x)})$. De même, si $s \in \mathcal{G}(V)$ (V ouvert dans Y), $v^\flat(s)$ est la section de $\mathcal{F}$ au-dessus de $\psi^{-1}(V)$, image par $v$ de la section $s'$ de $\mathcal{G}'$ telle que $s_x' = s_{\psi(x)}$ pour tout $x \in \psi^{-1}(V)$. En outre, l'homomorphisme canonique (3.5.3) $\rho: \mathcal{G} \to \psi_*(\psi^*(\mathcal{G}))$ se définit de la façon suivante : pour tout ouvert $V \subset Y$ et toute section $s \in \Gamma(V, \mathcal{G})$, $\rho(s)$ est la section $(s_{\psi(x)})_{x \in \psi^{-1}(V)}$ de $\psi^*(\mathcal{G})$ au-dessus de $\psi^{-1}(V)$. La vérification des relations $(u^\sharp)^{\flat} = u$, $(v^\flat)^{\sharp} = v$ et $v^\flat = \psi_*(v) \circ \rho$ est immédiate, et démontre notre assertion.

On vérifie que, si $w: \mathcal{G}_1 \to \mathcal{G}_2$ est un homomorphisme de préfaisceaux d'ensembles sur Y, $\psi^*(w)$ s'explicite de la façon suivante : si $s' = (s_x')_{x \in \mathrm{U}}$ est une section de $\psi^*(\mathcal{G}_1)$ au-dessus d'un ouvert U de X, $(\psi^*(w))(s')$ est la famille $(w_{\psi(x)}(s_x'))_{x \in \mathrm{U}}$. Enfin, il est immédiat que pour tout ouvert V de Y, l'image réciproque de $\mathcal{G}|V$ par la restriction de $\psi$ à $\psi^{-1}(V)$ est identique au faisceau induit $\psi^*(\mathcal{G})|\psi^{-1}(V)$.

Lorsque $\psi$ est l'identité $I_{X}$, on retrouve la définition d'un faisceau d'ensembles associé à un préfaisceau (G, II, 1.2). Les considérations précédentes s'appliquent sans changement lorsque $\pmb{K}$ est la catégorie des groupes ou des anneaux (non nécessairement commutatifs).

Lorsque X est une partie quelconque d'un espace topologique Y, et j l'injection canonique X→Y, pour tout faisceau G sur Y à valeurs dans une catégorie K, on appelle faisceau induit sur X par G l'image réciproque  $j^{*}(\mathcal{G})$  (lorsqu'elle existe) ; pour les faisceaux d'ensembles (ou de groupes, ou d'anneaux) on retrouve la définition usuelle (G, II, 1.5).

(3.7.2) Conservant les notations et hypothèses de (3.5.3), supposons que $\mathcal{G}$ soit un faisceau de groupes (resp. d'anneaux) sur Y. La définition des sections de $\psi^{*}(\mathcal{G})$ (3.7.1) montre (compte tenu de (3.4.4)) que l'homomorphisme de fibres $\psi_{x} \circ \rho_{\psi(x)} : \mathcal{G}_{\psi(x)} \to (\psi^{*}(\mathcal{G}))_{x}$ est un isomorphisme fonctoriel en $\mathcal{G}$, qui permet d'identifier ces deux fibres; avec cette identification, $u_{x}^{\sharp}$ est identique à l'homomorphisme défini dans (3.5.1), et en particulier, on a $\operatorname{Supp}(\psi^{*}(\mathcal{G})) = \psi^{-1}(\operatorname{Supp}(\mathcal{G}))$.

Une conséquence immédiate de ce résultat est que le foncteur $\psi^{*}(\mathcal{G})$ est exact en $\mathcal{G}$ dans la catégorie abélienne des faisceaux de groupes commutatifs.

## 3.8. Faisceaux d'espaces pseudo-discrets.

(3.8.1) Soit X un espace topologique dont la topologie admet une base B formée d'ensembles ouverts quasi-compacts. Soit F un faisceau d'ensembles sur X ; si on munit chacun des  $\mathcal{F}(\mathrm{U})$  de la topologie discrète,  $\mathrm{U}\to\mathcal{F}(\mathrm{U})$  est un préfaisceau d'espaces topologiques. Nous allons voir qu'il existe un faisceau d'espaces topologiques  $F'$  associé à F (3.5.6) tel que  $\Gamma(\mathrm{U},\mathcal{F}')$  soit l'espace discret  $\mathcal{F}(\mathrm{U})$  pour tout ouvert quasi-compact U. Il suffira pour cela de montrer que le préfaisceau  $\mathrm{U}\to\mathcal{F}(\mathrm{U})$  d'espaces topologiques discrets sur B vérifie la condition  $(\mathrm{F}_{0})$  de (3.2.2), et plus généralement que si U est un ouvert quasi-compact et si  $(\mathrm{U}_{\alpha})$  est un recouvrement de U par des ensembles de B, la topologie la moins fine T sur  $\Gamma(\mathrm{U},\mathcal{F})$  rendant continues les applications  $\Gamma(\mathrm{U},\mathcal{F})\to\Gamma(\mathrm{U}_{\alpha},\mathcal{F})$  est la topologie discrète. Or, il existe un nombre fini d'indices  $\alpha_{i}$  tels que  $U=\bigcup_{i}U_{\alpha_{i}}$ . Soit  $s\in\Gamma(\mathrm{U},\mathcal{F})$  et soit  $s_{i}$  son image dans  $\Gamma(\mathrm{U}_{\alpha_{i}},\mathcal{F})$ ; l'intersection des images réciproques des ensembles  $\{s_{i}\}$  est par définition un voisinage de s pour T ; mais puisque F est un faisceau d'ensembles et que les  $U_{\alpha_{i}}$  recouvrent U, cette intersection se réduit à s, d'où notre assertion.

On notera que si U est un ouvert non quasi-compact de X, l'espace topologique $\Gamma(U, \mathcal{F}')$ a encore $\Gamma(U, \mathcal{F})$ comme ensemble sous-jacent, mais sa topologie n'est pas discrète en général : c'est la moins fine rendant continues les applications $\Gamma(U, \mathcal{F}) \to \Gamma(V, \mathcal{F})$, pour $V \in \mathfrak{B}$ et $V \subset U$ (les $\Gamma(V, \mathcal{F})$ étant discrets).

Les considérations précédentes s'appliquent sans modification aux faisceaux de groupes ou d'anneaux (non nécessairement commutatifs), et leur associent respectivement des faisceaux de groupes topologiques ou d'anneaux topologiques. Pour abréger, nous dirons que le faisceau $\mathcal{F}'$ est le faisceau d'espaces (resp. groupes, anneaux) pseudo-discrets associé au faisceau d'ensembles (resp. groupes, anneaux) $\mathcal{F}$.

(3.8.2) Soient $\mathcal{F}$, $\mathcal{G}$ deux faisceaux d'ensembles (resp. groupes, anneaux) sur X, $u: \mathcal{F} \to \mathcal{G}$ un homomorphisme. Alors $u$ est aussi un homomorphisme continu $\mathcal{F}' \to \mathcal{G}'$, en désignant par $\mathcal{F}'$ et $\mathcal{G}'$ les faisceaux pseudo-discrets associés à $\mathcal{F}$ et $\mathcal{G}$; cela résulte en effet de (3.2.5).

(3.8.3) Soient $\mathcal{F}$ un faisceau d'ensembles, $\mathcal{H}$ un sous-faisceau de $\mathcal{F}$, $\mathcal{F}'$ et $\mathcal{H}'$ les faisceaux pseudo-discrets associés à $\mathcal{F}$ et $\mathcal{H}$ respectivement. Alors, pour tout ouvert $U\subset X$, $\Gamma(U,\mathcal{H}')$ est fermé dans $\Gamma(U,\mathcal{F}')$: en effet, c'est l'intersection des images réciproques des $\Gamma(V,\mathcal{H})$ (pour $V\in\mathfrak{B}$, $V\subset U$) par les applications continues $\Gamma(U,\mathcal{F})\to\Gamma(V,\mathcal{F})$, et $\Gamma(V,\mathcal{H})$ est fermé dans l'espace discret $\Gamma(V,\mathcal{F})$.

## § 4. ESPACES ANNELÉS

## 4.1. Espaces annelés, A-Modules, A-Algèbres.

(4.1.1) Un espace annelé (resp. topologiquement annelé) est un couple (X, A) formé d'un espace topologique X et d'un faisceau d'anneaux (non nécessairement commutatifs) (resp. d'un faisceau d'anneaux topologiques) A sur X ; on dit que X est l'espace topo-

logique sous-jacent à l'espace annelé (X, A), et A le faisceau structural. Ce dernier se note  $O_{X}$ , et sa fibre en un point  $x \in X$  se note  $O_{X,x}$  ou simplement  $O_{x}$  lorsqu'il n'en résulte pas de confusion.

On désignera par 1 ou e la section unité de $\mathcal{O}_{\mathrm{X}}$ au-dessus de X (élément unité de $\Gamma(\mathbf{X},\mathcal{O}_{\mathrm{X}})$).

Comme dans ce Traité nous aurons surtout à considérer des faisceaux d'anneaux commutatifs, il sera sous-entendu, lorsque nous parlerons d'un espace annelé (X, A) sans préciser, que A est un faisceau d'anneaux commutatifs.

Les espaces annelés à faisceau structural non nécessairement commutatif (resp. les espaces topologiquement annelés) forment une catégorie, lorsqu'on définit un morphisme  $(\mathbf{X}, \mathcal{A}) \to (\mathbf{Y}, \mathcal{B})$  comme un couple  $(\psi, \theta) = \Psi'$  formé d'une application continue  $\psi : X \to Y$  et d'un  $\psi$ -morphisme  $\theta : G \to F$  (3.5.1) de faisceaux d'anneaux (resp. de faisceaux d'anneaux topologiques); le composé d'un second morphisme  $\Psi' = (\psi', \theta') : (\mathbf{Y}, \mathcal{B}) \to (\mathbf{Z}, \mathcal{C})$  et de  $\Psi'$, noté  $\Psi'' = \Psi' \circ \Psi'$, est le morphisme  $(\psi'', \theta'')$  où  $\psi'' = \psi' \circ \psi'$, et  $\theta''$  est le composé de  $\theta$  et  $\theta'$  (égal à  $\psi'(\theta) \circ \theta'$, cf. 3.5.2). Pour les espaces annelés, rappelons que l'on a alors  $\theta''^{\#} = \theta^{\#} \circ \psi^{*}(\theta'^{\#})$  (3.5.5); donc si  $\theta'^{\#}$  et  $\theta^{\#}$  sont des homomorphismes injectifs (resp. surjectifs), il en est de même de  $\theta''^{\#}$, compte tenu du fait que  $\psi_x \circ \rho_{\psi(x)}$  est un isomorphisme pour tout  $x \in X$  (3.7.2). On vérifie aussitôt, grâce à ce qui précède, que lorsque  $\psi$  est une application continue injective et  $\theta^{\#}$  un homomorphisme surjectif de faisceaux d'anneaux, le morphisme  $(\psi, \theta)$  est un monomorphisme (T, I.I) dans la catégorie des espaces annelés.

Par abus de langage, on remplacera souvent $\psi$ par $\Psi^{\prime}$ dans les notations, par exemple en écrivant $\Psi^{-1}(\mathrm{U})$ au lieu de $\psi^{-1}(\mathrm{U})$ pour une partie U de Y, lorsque cela ne risquera pas d'entraîner confusion.

(4.1.2) Pour toute partie M de X, le couple (M, A|M) est évidemment un espace annelé, dit induit sur M par l'espace annelé (X, A) (et appelé encore la restriction de (X, A) à M). Si j est l'injection canonique M→X et ω l'application identique de A|M, (j, ωb) est un monomorphisme (M, A|M)→(X, A) d'espaces annelés, appelé l'injection canonique. Le composé d'un morphisme Ψ: (X, A)→(Y, B) et de cette injection est appelé la restriction de Ψ à M.

(4.1.3) Nous ne reviendrons pas sur la définition des A-Modules ou faisceaux algébriques sur un espace annelé (X, A) (G, II, 2.2); lorsque A est un faisceau d'anneaux non nécessairement commutatifs, par A-Module, il faudra toujours sous-entendre « A-Module à gauche » sauf mention expresse du contraire. Les sous-A-Modules de A seront qualifiés de faisceaux d'idéaux (à gauche, à droite ou bilatères) dans A ou de A-Idéaux.

Lorsque $\mathcal{A}$ est un faisceau d'anneaux commutatifs, et que, dans la définition des $\mathcal{A}$-Modules, on remplace partout la structure de module par celle d'algèbre, on obtient la définition d'une $\mathcal{A}$-Algèbre sur X. Il revient au même de dire qu'une $\mathcal{A}$-Algèbre (non nécessairement commutative) est un $\mathcal{A}$-Module $\mathcal{C}$, muni d'un homomorphisme de $\mathcal{A}$-Modules $\varphi: \mathcal{C} \otimes_{\mathcal{A}} \mathcal{C} \to \mathcal{C}$ et d'une section $e$ au-dessus de X, tels que : $1^{\circ}$ Le diagramme

![](images/page_35_image_0.jpg)

soit commutatif; $2^{0}$ pour tout ouvert $\mathbf{U} \subset \mathbf{X}$ et toute section $s \in \Gamma(\mathbf{U}, \mathcal{C})$, on ait $\varphi((e|\mathbf{U}) \otimes s) = \varphi(s \otimes (e|\mathbf{U})) = s$. Dire que $\mathcal{C}$ est une $\mathcal{A}$-Algèbre commutative revient en outre à dire que le diagramme

![](images/page_35_image_2.jpg)

est commutatif, $\sigma$ désignant la symétrie canonique du produit tensoriel $\mathcal{C} \otimes_{\mathcal{A}} \mathcal{C}$.

Les homomorphismes de $\mathcal{A}$-Algèbres se définissent aussi comme les homomorphismes de $\mathcal{A}$-Modules dans (G, II, 2.2), mais naturellement ne forment plus un groupe abélien.

Si M est un sous-A-Module d'une A-Algèbre C, la sous-A-Algèbre de C engendrée par M est la somme des images des homomorphismes  $\otimes_{M\to C}^{n}$  (pour les  $n\geqslant0$ ). C'est aussi le faisceau associé au préfaisceau U→B(U) d'algèbres, B(U) étant la sous-algèbre de Γ(U, C) engendrée par le sous-module Γ(U, M).

(4.1.4) On dit qu'un faisceau d'anneaux $\mathcal{A}$ sur un espace topologique X est réduit en un point $x$ de X si la fibre $\mathcal{A}_x$ est un anneau réduit (1.1.1); on dit que $\mathcal{A}$ est réduit s'il est réduit en tout point de X. Rappelons qu'un anneau A est dit régulier si chacun des anneaux locaux $\mathrm{A}_{\mathfrak{p}}$ (où p parcourt l'ensemble des idéaux premiers de A) est un anneau local régulier; nous dirons qu'un faisceau d'anneaux $\mathcal{A}$ sur X est régulier en un point $x$ (resp. régulier) si la fibre $\mathcal{A}_x$ est un anneau régulier (resp. si $\mathcal{A}$ est régulier en tout point). Enfin, nous dirons qu'un faisceau d'anneaux $\mathcal{A}$ sur X est normal en un point $x$ (resp. normal) si sa fibre $\mathcal{A}_x$ est un anneau intègre et intégralement clos (resp. si $\mathcal{A}$ est normal en tout point). Nous dirons qu'un espace annelé (X, $\mathcal{A}$) a l'une des propriétés précédentes si le faisceau d'anneaux $\mathcal{A}$ a cette propriété.

Un faisceau d'anneaux gradués $\mathcal{A}$ est par définition un faisceau d'anneaux qui est somme directe (G, II, 2.7) d'une famille $(\mathcal{A}_n)_{n \in \mathbb{Z}}$ de faisceaux de groupes abéliens avec les conditions $\mathcal{A}_m\mathcal{A}_n \subset \mathcal{A}_{m+n}$; un $\mathcal{A}$-Module gradué est un $\mathcal{A}$-Module $\mathcal{F}$ somme directe d'une famille $(\mathcal{F}_n)_{n \in \mathbb{Z}}$ de faisceaux de groupes abéliens, satisfaisant aux conditions $\mathcal{A}_m\mathcal{F}_n \subset \mathcal{F}_{m+n}$. Il revient d'ailleurs au même de dire que l'on a $(\mathcal{A}_m)_x(\mathcal{A}_n)_x \subset (\mathcal{A}_{m+n})_x$ (resp. $(\mathcal{A}_m)_x(\mathcal{F}_n)_x \subset (\mathcal{F}_{m+n})_x$) en tout point $x$.

(4.1.5) Étant donné un espace annelé (X, A) (non nécessairement commutatif), nous ne rappellerons pas ici les définitions des bifoncteurs  $F \otimes_{A} G$ ,  $\mathcal{H}om_{A}(F, G)$  et  $\mathrm{Hom}_{A}(F, G)$  (G, II, 2.8 et 2.2) dans les catégories des A-Modules à gauche ou à droite (selon les cas), à valeurs dans la catégorie des faisceaux de groupes abéliens (ou plus

généralement des $\mathcal{C}$-Modules, si $\mathcal{C}$ est le centre de $\mathcal{A}$). La fibre $(\mathcal{F} \otimes_{\mathcal{A}} \mathcal{G})_x$ en tout point $x \in \mathbf{X}$ s'identifie canoniquement à $\mathcal{F}_x \otimes_{\mathcal{A}_x} \mathcal{G}_x$ et on définit un homomorphisme canonique fonctoriel $(\mathcal{Hom}_{\mathcal{A}}(\mathcal{F}, \mathcal{G}))_x \to \mathrm{Hom}_{\mathcal{A}_x}(\mathcal{F}_x, \mathcal{G}_x)$ qui, en général, n'est ni injectif ni surjectif. Les bifoncteurs considérés ci-dessus sont additifs et, en particulier, commutent aux sommes directes finies; $\mathcal{F} \otimes_{\mathcal{A}} \mathcal{G}$ est exact à droite en $\mathcal{F}$ et en $\mathcal{G}$, commute aux limites inductives, et $\mathcal{A} \otimes_{\mathcal{A}} \mathcal{G}$ (resp. $\mathcal{F} \otimes_{\mathcal{A}} \mathcal{A}$) s'identifie canoniquement à $\mathcal{G}$ (resp. $\mathcal{F}$). Les foncteurs $\mathcal{Hom}_{\mathcal{A}}(\mathcal{F}, \mathcal{G})$ et $\mathrm{Hom}_{\mathcal{A}}(\mathcal{F}, \mathcal{G})$ sont exacts à gauche en $\mathcal{F}$ et $\mathcal{G}$; de façon précise, si on a une suite exacte de la forme $o \to \mathcal{G}' \to \mathcal{G} \to \mathcal{G}''$, la suite

$$
0 \rightarrow \mathcal {H} o m _ {\mathcal {A}} (\mathcal {F}, \mathcal {G} ^ {\prime}) \rightarrow \mathcal {H} o m _ {\mathcal {A}} (\mathcal {F}, \mathcal {G}) \rightarrow \mathcal {H} o m _ {\mathcal {A}} (\mathcal {F}, \mathcal {G} ^ {\prime \prime})
$$

est exacte, et si on a une suite exacte de la forme $\mathcal{F}'\to\mathcal{F}\to\mathcal{F}''\to0$, la suite

$$
0 \rightarrow \mathcal {H} o m _ {\mathcal {A}} (\mathcal {F} ^ {\prime \prime}, \mathcal {G}) \rightarrow \mathcal {H} o m _ {\mathcal {A}} (\mathcal {F}, \mathcal {G}) \rightarrow \mathcal {H} o m _ {\mathcal {A}} (\mathcal {F} ^ {\prime}, \mathcal {G})
$$

est exacte, avec des propriétés analogues pour le foncteur Hom. En outre, $\mathcal{H}om_{\mathcal{A}}(\mathcal{A},\mathcal{G})$ s'identifie canoniquement à $\mathcal{G}$ ; enfin, pour tout ouvert U$\subset$X, on a

$$
\Gamma (\mathrm{U}, \mathcal {H} o m _ {\mathcal {A}} (\mathcal {F}, \mathcal {G})) = \operatorname{Hom} _ {\mathcal {A} | \mathrm{U}} (\mathcal {F} | \mathrm{U}, \mathcal {G} | \mathrm{U}).
$$

Pour tout $\mathcal{A}$-Module à gauche $\mathcal{F}$ (resp. à droite), on appelle dual de $\mathcal{F}$ et on note $\check{\mathcal{F}}$ le $\mathcal{A}$-Module à droite (resp. à gauche) $\operatorname{Hom}_{\mathcal{A}}(\mathcal{F}, \mathcal{A})$.

Enfin, si $\mathcal{A}$ est un faisceau d'anneaux commutatifs, $\mathcal{F}$ un $\mathcal{A}$-Module, $\mathrm{U} \to \wedge^p \Gamma(\mathrm{U}, \mathcal{F})$ est un préfaisceau dont le faisceau associé est un $\mathcal{A}$-Module qui se note $\wedge^p \mathcal{F}$ et s'appelle la puissance extérieure $p$-ème de $\mathcal{F}$; on vérifie aisément que l'application canonique du préfaisceau $\mathrm{U} \to \wedge^p \Gamma(\mathrm{U}, \mathcal{F})$ dans le faisceau associé $\wedge^p \mathcal{F}$ est injective, et que pour tout $x \in \mathrm{X}$, on a $(\wedge^p \mathcal{F})_x = \wedge^p (\mathcal{F}_x)$. Il est clair que $\wedge^p \mathcal{F}$ est un foncteur covariant en $\mathcal{F}$.

(4.1.6) Supposons que $\mathcal{A}$ soit un faisceau d'anneaux non nécessairement commutatifs, $\mathcal{J}$ un faisceau d'idéaux à gauche de $\mathcal{A}$, $\mathcal{F}$ un $\mathcal{A}$-Module à gauche; on note alors $\mathcal{J}\mathcal{F}$ le sous-$\mathcal{A}$-Module de $\mathcal{F}$, image de $\mathcal{J} \otimes_{\mathbf{Z}} \mathcal{F}$ (où $\mathbf{Z}$ est le faisceau associé au préfaisceau constant $U \to \mathbf{Z}$) par l'application canonique $\mathcal{J} \otimes_{\mathbf{Z}} \mathcal{F} \to \mathcal{F}$; il est clair que pour tout $x \in X$, on a $(\mathcal{J}\mathcal{F})_x = \mathcal{J}_x\mathcal{F}_x$. Lorsque $\mathcal{A}$ est commutatif, $\mathcal{J}\mathcal{F}$ est aussi l'image canonique de $\mathcal{J} \otimes_{\mathcal{A}} \mathcal{F} \to \mathcal{F}$. Il est immédiat que $\mathcal{J}\mathcal{F}$ est aussi le $\mathcal{A}$-Module associé au préfaisceau $U \to \Gamma(U, \mathcal{J})\Gamma(U, \mathcal{F})$. Si $\mathcal{J}_1, \mathcal{J}_2$ sont deux faisceaux d'idéaux à gauche de $\mathcal{A}$, on a $\mathcal{J}_1(\mathcal{J}_2\mathcal{F}) = (\mathcal{J}_1\mathcal{J}_2)\mathcal{F}$.

(4.1.7) Soit  $(\mathbf{X}_{\lambda}, \mathcal{A}_{\lambda})_{\lambda \in \mathbb{L}}$  une famille d'espaces annelés; pour tout couple  $(\lambda, \mu)$ , supposons donnée une partie ouverte  $V_{\lambda\mu}$  de  $X_{\lambda}$ , et un isomorphisme d'espaces annelés  $\varphi_{\lambda\mu} : (\mathrm{V}_{\mu\lambda}, \mathcal{A}_{\mu} | \mathrm{V}_{\mu\lambda}) \stackrel{\sim}{\to} (\mathrm{V}_{\lambda\mu}, \mathcal{A}_{\lambda} | \mathrm{V}_{\lambda\mu})$ , avec  $V_{\lambda\lambda} = X_{\lambda}$ ,  $\varphi_{\lambda\lambda}$  étant l'identité. Supposons de plus que, pour tout triplet  $(\lambda, \mu, \nu)$ , si on désigne par  $\varphi_{\mu\lambda}'$  la restriction de  $\varphi_{\mu\lambda}$  à  $V_{\lambda\mu} \cap V_{\lambda\nu}$ ,  $\varphi_{\mu\lambda}'$  soit un isomorphisme de  $(\mathrm{V}_{\lambda\mu} \cap \mathrm{V}_{\lambda\nu}, \mathcal{A}_{\lambda} | (\mathrm{V}_{\lambda\mu} \cap \mathrm{V}_{\lambda\nu}))$  sur  $(\mathrm{V}_{\mu\nu} \cap \mathrm{V}_{\mu\lambda}, \mathcal{A}_{\mu} | (\mathrm{V}_{\mu\nu} \cap \mathrm{V}_{\mu\lambda}))$  et que l'on ait  $\varphi_{\lambda\nu}' = \varphi_{\lambda\mu}' \circ \varphi_{\mu\nu}'$  (condition de recollement pour les  $\varphi_{\lambda\mu}$ ). On peut tout d'abord considérer alors l'espace topologique obtenu par recollement (au moyen des  $\varphi_{\lambda\mu}$ ) des  $X_{\lambda}$

le long des  $V_{\lambda\mu}$ ; si on identifie  $X_{\lambda}$  à la partie ouverte  $X'_{\lambda}$  correspondante dans X, les hypothèses entraînent que les trois ensembles  $V_{\lambda\mu} \cap V_{\lambda\nu}$ ,  $V_{\mu\nu} \cap V_{\mu\lambda}$ ,  $V_{\nu\lambda} \cap V_{\nu\mu}$  s'identifient à  $X'_{\lambda} \cap X'_{\mu} \cap X'_{\nu}$ . On peut alors transporter à  $X'_{\lambda}$  la structure d'espace annelé de  $X_{\lambda}$ , et si  $A'_{\lambda}$  est le faisceau d'anneaux transporté de  $A_{\lambda}$ , les  $A'_{\lambda}$  vérifient la condition de recollement (3.3.1) et définissent donc un faisceau d'anneaux A sur X; on dit que  $(X, A)$  est l'espace annelé obtenu par recollement des  $(X_{\lambda}, A_{\lambda})$  le long des  $V_{\lambda\mu}$ , au moyen des  $\varphi_{\lambda\mu}$ .

## 4.2. Image directe d'un A-Module.

(4.2.1) Soient (X, A), (Y, B) deux espaces annelés, $\Psi = (\psi, \theta)$ un morphisme $(\mathrm{X}, \mathcal{A}) \to (\mathrm{Y}, \mathcal{B}) ; \psi_*(\mathrm{A})$ est donc un faisceau d'anneaux sur Y, et $\theta$ un homomorphisme $\mathcal{B} \to \psi_*(\mathcal{A})$ de faisceaux d'anneaux. Soit alors $\mathcal{F}$ un $\mathcal{A}$-Module; son image directe $\psi_*(\mathcal{F})$ est un faisceau de groupes abéliens sur Y. En outre, pour tout ouvert U ⊂ Y,

$$
\Gamma (\mathrm{U}, \psi_ {*} (\mathcal {F})) = \Gamma (\psi^ {- 1} (\mathrm{U}), \mathcal {F})
$$

est muni d'une structure de module par rapport à l'anneau $\Gamma(\mathrm{U},\psi_{*}(\mathcal{A}))=\Gamma(\psi^{-1}(\mathrm{U}),\mathcal{A})$; les applications bilinéaires qui définissent ces structures étant compatibles avec les opérations de restriction, définissent sur $\psi_{*}(\mathcal{F})$ une structure de $\psi_{*}(\mathcal{A})$-Module. L'homomorphisme $\theta:\mathcal{B}\to\psi_{*}(\mathcal{A})$ permet alors de définir aussi sur $\psi_{*}(\mathcal{F})$ une structure de $\mathcal{B}$-Module; nous dirons que ce $\mathcal{B}$-Module est l'image directe de $\mathcal{F}$ par le morphisme $\Psi$, et nous le noterons $\Psi_{*}(\mathcal{F})$. Si $\mathcal{F}_{1},\mathcal{F}_{2}$ sont deux $\mathcal{A}$-Modules sur X et u un $\mathcal{A}$-homomorphisme $\mathcal{F}_{1}\to\mathcal{F}_{2}$, il est immédiat (en considérant les sections au-dessus des ouverts de Y) que $\psi_{*}(u)$ est un $\psi_{*}(\mathcal{A})$-homomorphisme $\psi_{*}(\mathcal{F}_{1})\to\psi_{*}(\mathcal{F}_{2})$, et a fortiori un $\mathcal{B}$-homomorphisme $\Psi_{*}(\mathcal{F}_{1})\to\Psi_{*}(\mathcal{F}_{2})$; en tant que $\mathcal{B}$-homomorphisme, nous le noterons $\Psi_{*}^{\prime}(u)$. On voit donc que $\Psi_{*}$ est un foncteur covariant de la catégorie des $\mathcal{A}$-Modules dans celle des $\mathcal{B}$-Modules. En outre, il est immédiat que ce foncteur est exact à gauche (G, II, 2.12).

Sur $\psi_{*}(\mathcal{A})$, la structure de $\mathcal{B}$-Module et la structure de faisceaux d'anneaux définissent une structure de $\mathcal{B}$-Algèbre; on notera $\Psi_{*}(\mathcal{A})$ cette $\mathcal{B}$-Algèbre.

(4.2.2) Soient M, N deux A-Modules. Pour tout ouvert U de Y, on a une application canonique

$$
\Gamma (\psi^ {- 1} (\mathbf {U}), \mathcal {M}) \times \Gamma (\psi^ {- 1} (\mathbf {U}), \mathcal {N}) \rightarrow \Gamma (\psi^ {- 1} (\mathbf {U}), \mathcal {M} \otimes_ {\mathcal {A}} \mathcal {N})
$$

qui est bilinéaire sur l'anneau $\Gamma(\psi^{-1}(\mathbf{U}),\mathcal{A})=\Gamma(\mathbf{U},\psi_{*}(\mathcal{A}))$, et a fortiori sur $\Gamma(\mathbf{U},\mathcal{B})$; elle définit donc un homomorphisme

$$
\Gamma (\mathrm{U}, \Psi_ {*} (\mathcal {M})) \otimes_ {\Gamma (\mathrm{U}, \mathcal {B})} \Gamma (\mathrm{U}, \Psi_ {*} (\mathcal {N})) \rightarrow \Gamma (\mathrm{U}, \Psi_ {*} (\mathcal {M} \otimes_ {\mathcal {A}} \mathcal {N}))
$$

et comme on vérifie aussitôt que ces homomorphismes sont compatibles avec les opérations de restriction, ils donnent un homomorphisme canonique fonctoriel de B-Modules

$$
\Psi_ {*} (\mathcal {M}) \otimes_ {\mathcal {B}} \Psi_ {*} (\mathcal {N}) \rightarrow \Psi_ {*} (\mathcal {M} \otimes_ {\mathcal {A}} \mathcal {N})\tag{4.2.2.1}
$$

qui ne sera en général ni injectif ni surjectif. Si P est un troisième A-Module, on vérifie aussitôt que le diagramme

$$
\begin{array}{c} \Psi_ {*} (\mathcal {M}) \otimes_ {\mathcal {B}} \Psi_ {*} (\mathcal {N}) \otimes_ {\mathcal {B}} \Psi_ {*} (\mathcal {P}) \to \Psi_ {*} (\mathcal {M} \otimes_ {\mathcal {A}} \mathcal {N}) \otimes_ {\mathcal {B}} \Psi_ {*} (\mathcal {P}) \\ \downarrow \\ \Psi_ {*} (\mathcal {M}) \otimes_ {\mathcal {B}} \Psi_ {*} (\mathcal {N} \otimes_ {\mathcal {A}} \mathcal {P}) \longrightarrow \Psi_ {*} (\mathcal {M} \otimes_ {\mathcal {A}} \mathcal {N} \otimes_ {\mathcal {A}} \mathcal {P}) \end{array}\tag{4.2.2.2}
$$

est commutatif.

(4.2.3) Soient M, N deux A-Modules. Pour tout ouvert U ⊂ Y, on a par définition  $\Gamma(\psi^{-1}(U), \mathcal{H}om_{\mathcal{A}}(\mathcal{M}, \mathcal{N})) = \text{Hom}_{\mathcal{A}|V}(\mathcal{M}|V, \mathcal{N}|V)$ , où on a posé pour alléger  $V = \psi^{-1}(U)$ ; l'application  $u \to \Psi_{*}(u)$  est un homomorphisme

$$
\operatorname{Hom} _ {\mathscr {A} | \mathrm{V}} (\mathscr {M} | \mathrm{V}, \mathscr {N} | \mathrm{V}) \rightarrow \operatorname{Hom} _ {\mathscr {B} | \mathrm{U}} \left(\Psi_ {*} ^ {\prime} (\mathscr {M}) \mid \mathrm{U}, \Psi_ {*} ^ {\prime} (\mathscr {N}) \mid \mathrm{U}\right)
$$

pour les structures de $\Gamma(\mathrm{U},\mathcal{B})$-modules; ces homomorphismes étant compatibles aux opérations de restriction définissent donc un homomorphisme canonique fonctoriel de $\mathcal{B}$-Modules

$$
\Psi_ {*} (\mathcal {H} o m _ {\mathscr {A}} (\mathscr {M}, \mathscr {N})) \rightarrow \mathcal {H} o m _ {\mathscr {B}} (\Psi_ {*} (\mathscr {M}), \Psi_ {*} (\mathscr {N})).\tag{4.2.3.1}
$$

(4.2.4) Si C est une A-Algèbre, l'homomorphisme composé

$$
\Psi_ {*} (\mathcal {C}) \otimes_ {\mathcal {B}} \Psi_ {*} (\mathcal {C}) \rightarrow \Psi_ {*} (\mathcal {C} \otimes_ {\mathcal {A}} \mathcal {C}) \rightarrow \Psi_ {*} (\mathcal {C})
$$

définit sur $\Psi_{*}(\mathcal{C})$ une structure de $\mathcal{B}$-Algèbre, comme il résulte de (4.2.2.2). On voit de même que si $\mathcal{M}$ est un $\mathcal{C}$-Module, $\Psi_{*}(\mathcal{M})$ est muni canoniquement d'une structure de $\Psi_{*}(\mathcal{C})$-Module.

(4.2.5) Considérons en particulier le cas où X est un sous-espace fermé de Y et où $\psi$ est l'injection canonique $j: \mathrm{X} \to \mathrm{Y}$. Si $\mathcal{B}' = \mathcal{B} | \mathrm{X} = j^{*}(\mathcal{B})$ est la restriction du faisceau d'anneaux $\mathcal{B}$ à X, un $\mathcal{A}$-Module $\mathcal{M}$ peut être considéré comme $\mathcal{B}'$-Module au moyen de l'homomorphisme $\theta^{\sharp}: \mathcal{B}' \to \mathcal{A}$; $\Psi_{*}(\mathcal{M})$ est alors le $\mathcal{B}$-Module qui induit $\mathcal{M}$ sur X et o ailleurs. Si $\mathcal{N}$ est un second $\mathcal{A}$-Module, $\Psi_{*}(\mathcal{M}) \otimes_{\mathcal{B}} \Psi_{*}(\mathcal{N})$ s'identifie donc à $\Psi_{*}(\mathcal{M} \otimes_{\mathcal{B}'} \mathcal{N})$ et $\operatorname{Hom}_{\mathcal{B}}(\Psi_{*}(\mathcal{M}), \Psi_{*}(\mathcal{N}))$ à $\Psi_{*}(\operatorname{Hom}_{\mathcal{B}'}(\mathcal{M}, \mathcal{N}))$.

(4.2.6) Soient (Z, C) un troisième espace annelé, $\Psi' = (\psi', \theta')$ un morphisme (Y, B) → (Z, C); si $\Psi''$ est le morphisme composé $\Psi'' \circ \Psi$, il est clair que l'on a $\Psi'_* = \Psi'_* \circ \Psi_*$.

## 4.3. Image réciproque d'un B-Module.

(4.3.1) Les hypothèses et notations étant celles de (4.2.1), soient $\mathcal{G}$ un $\mathcal{B}$-Module et $\psi^{*}(\mathcal{G})$ son image réciproque (3.7.1) qui est donc un faisceau de groupes abéliens sur X. La définition des sections de $\psi^{*}(\mathcal{G})$ et de $\psi^{*}(\mathcal{B})$ (3.7.1) montre que $\psi^{*}(\mathcal{G})$ est canoniquement muni d'une structure de $\psi^{*}(\mathcal{B})$-Module. D'autre part, l'homomorphisme $\theta^{\sharp}:\psi^{*}(\mathcal{B})\to\mathcal{A}$ munit $\mathcal{A}$ d'une structure de $\psi^{*}(\mathcal{B})$-Module, que nous noterons $\mathcal{A}_{[\theta]}$ lorsqu'il y a lieu d'éviter des confusions; le produit tensoriel $\psi^{*}(\mathcal{G})\otimes_{\psi^{*}(\mathcal{B})}\mathcal{A}_{[\theta]}$ est alors muni d'une structure de $\mathcal{A}$-Module. Nous dirons que ce $\mathcal{A}$-Module est l'image réci-

proque de $\mathcal{G}$ par le morphisme $\Psi$ et nous le noterons $\Psi^{*}(\mathcal{G})$. Si $\mathcal{G}_{1}, \mathcal{G}_{2}$ sont deux $\mathcal{B}$-Modules sur Y, $v$ un $\mathcal{B}$-homomorphisme $\mathcal{G}_{1} \to \mathcal{G}_{2}, \psi^{*}(v)$, comme on le vérifie aussitôt, est un $\psi^{*}(\mathcal{B})$-homomorphisme de $\psi^{*}(\mathcal{G}_{1})$ dans $\psi^{*}(\mathcal{G}_{2})$; par suite $\psi^{*}(v) \otimes i$ est un $\mathcal{A}$-homomorphisme $\Psi^{*}(\mathcal{G}_{1}) \to \Psi^{*}(\mathcal{G}_{2})$, que nous noterons $\Psi^{*}(v)$. On a donc défini $\Psi^{*}$ comme un foncteur covariant de la catégorie des $\mathcal{B}$-Modules dans celle des $\mathcal{A}$-Modules. Ici, ce foncteur (contrairement à $\psi^{*}$) n'est plus exact en général, mais seulement exact à droite, la tensorisation par $\mathcal{A}$ étant un foncteur exact à droite dans la catégorie des $\psi^{*}(\mathcal{B})$-Modules.

Pour tout $x \in \mathbf{X}$, on a $(\Psi^{*}(\mathcal{G}))_{x} = \mathcal{G}_{\psi(x)} \otimes_{\mathcal{B}_{\psi(x)}} \mathcal{A}_{x}$, en vertu de (3.7.2). Le support de $\Psi^{*}(\mathcal{G})$ est donc contenu dans $\psi^{-1}$ (Supp $\mathcal{G}$).

(4.3.2) Soit $(\mathcal{G}_{\lambda})$ un système inductif de $\mathcal{B}$-Modules, et soit $\mathcal{G} = \lim_{\mathcal{G}_{\lambda}} \text{sa limite inductive. Les homomorphismes canoniques } \mathcal{G}_{\lambda} \to \mathcal{G}$ définissent des $\overrightarrow{\psi^{*}(\mathcal{B})}$-homomorphismes $\psi^{*}(\mathcal{G}_{\lambda}) \to \psi^{*}(\mathcal{G})$, qui donnent un homomorphisme canonique $\varinjlim \psi^{*}(\mathcal{G}_{\lambda}) \to \psi^{*}(\mathcal{G})$. Comme la fibre en un point d'une limite inductive de faisceaux est la limite inductive des fibres au même point (G, II, 1.11), l'homomorphisme canonique précédent est bijectif (3.7.2). En outre, le produit tensoriel commute aux limites inductives de faisceaux, et on a donc un isomorphisme canonique fonctoriel $\lim_{\mathcal{G}_{\lambda}} \Psi^{*}(\mathcal{G}_{\lambda}) \simeq \Psi^{*}(\lim_{\mathcal{G}_{\lambda}})$ de $\mathcal{A}$-Modules.

D'autre part, pour une somme directe finie $\bigoplus_{i} \mathcal{G}_{i}$ de $\mathcal{B}$-Modules, il est clair que $\psi^{*}(\bigoplus_{i} \mathcal{G}_{i}) = \bigoplus_{i} \psi^{*}(\mathcal{G}_{i})$, donc, par produit tensoriel avec $\mathcal{A}_{[0]}$,

$$
\Psi^ {*} (\oplus_ {i} \mathcal {G} _ {i}) = \oplus_ {i} \Psi^ {*} (\mathcal {G} _ {i}).\tag{4.3.2.1}
$$

Par passage à la limite inductive, on en déduit, en vertu de ce qui précède, que l'égalité précédente est encore vraie pour une somme directe quelconque.

(4.3.3) Soient $\mathcal{G}_1$, $\mathcal{G}_2$ deux $\mathcal{B}$-Modules; de la définition des images réciproques de faisceaux de groupes abéliens (3.7.1), on déduit aussitôt un homomorphisme canonique $\psi^*(\mathcal{G}_1)\otimes_{\psi^*(\mathcal{B})}\psi^*(\mathcal{G}_2)\to\psi^*(\mathcal{G}_1\otimes_\mathcal{B}\mathcal{G}_2)$ de $\psi^*(\mathcal{B})$-Modules, et la fibre en un point d'un produit tensoriel de faisceaux étant le produit tensoriel des fibres en ce point (G, II, 2.8), on déduit de (3.7.2) que l'homomorphisme précédent est en fait un isomorphisme. Par produit tensoriel avec $\mathcal{A}$, on en déduit un isomorphisme canonique fonctoriel

$$
\Psi^ {*} (\mathcal {G} _ {1}) \otimes_ {\mathscr {A}} \Psi^ {*} (\mathcal {G} _ {2}) \simeq \Psi^ {*} (\mathcal {G} _ {1} \otimes_ {\mathscr {B}} \mathcal {G} _ {2}).\tag{4.3.3.1}
$$

(4.3.4) Soit C une B-Algèbre ; la donnée de la structure d'Algèbre sur C revient à la donnée d'un B-homomorphisme  $C \otimes_{B} C \to C$  satisfaisant aux conditions d'associativité et de commutativité (conditions qui se vérifient sur chaque fibre) ; l'isomorphisme précédent permet de transporter cet homomorphisme en un homomorphisme de A-Modules  $\Psi^{*}(\mathcal{C}) \otimes_{\mathcal{A}} \Psi^{*}(\mathcal{C}) \to \Psi^{*}(\mathcal{C})$  satisfaisant aux mêmes conditions, donc  $\Psi^{*}(\mathcal{C})$  est ainsi muni d'une structure de A-Algèbre. En particulier, il résulte aussitôt des définitions que la A-Algèbre  $\Psi^{*}(\mathcal{B})$  est égale à A (à un isomorphisme canonique près).

De même, si M est un C-Module, la donnée de cette structure de Module revient

à celle d'un $\mathcal{B}$-homomorphisme $\mathcal{C} \otimes_{\mathcal{B}} \mathcal{M} \to \mathcal{M}$ vérifiant la condition d'associativité; d'où par transport une structure de $\Psi^{*}(\mathcal{C})$-Module sur $\Psi^{*}(\mathcal{M})$.

(4.3.5) Soit $\mathcal{J}$ un faisceau d'idéaux de $\mathcal{B}$; comme le foncteur $\psi^{*}$ est exact, le $\psi^{*}(\mathcal{B})$-Module $\psi^{*}(\mathcal{J})$ s'identifie canoniquement à un faisceau d'idéaux de $\psi^{*}(\mathcal{B})$; l'injection canonique $\psi^{*}(\mathcal{J}) \to \psi^{*}(\mathcal{B})$ donne alors un homomorphisme de $\mathcal{A}$-Modules $\Psi^{*}(\mathcal{J}) = \psi^{*}(\mathcal{J}) \otimes_{\psi^{*}(\mathcal{B})} \mathcal{A}_{[\theta]} \to \mathcal{A}$; nous noterons $\Psi^{*}(\mathcal{J})\mathcal{A}$, ou $\mathcal{J}\mathcal{A}$ si aucune confusion n'est à craindre, l'image de $\Psi^{*}(\mathcal{J})$ par cet homomorphisme. On a donc par définition $\mathcal{J}\mathcal{A} = \theta^{\sharp}(\psi^{*}(\mathcal{J}))\mathcal{A}$ et en particulier, pour tout $x \in X$, $(\mathcal{J}\mathcal{A})_x = \theta_x^{\sharp}(\mathcal{J}_{\psi(x)})\mathcal{A}_x$, en tenant compte de l'identification canonique des fibres de $\psi^{*}(\mathcal{J})$ et de celles de $\mathcal{J}$ (3.7.2). Si $\mathcal{J}_1$, $\mathcal{J}_2$ sont deux idéaux de $\mathcal{B}$, on a $(\mathcal{J}_1\mathcal{J}_2)\mathcal{A} = \mathcal{J}_1(\mathcal{J}_2\mathcal{A}) = (\mathcal{J}_1\mathcal{A})(\mathcal{J}_2\mathcal{A})$.

$$
\mathcal {J} \mathcal {F} = (\mathcal {J} \mathcal {A}) \mathcal {F}
$$

(4.3.6) Soient (Z, C) un troisième espace annelé, $\Psi' = (\psi', \theta')$ un morphisme $(\mathbf{Y}, \mathcal{B}) \to (\mathbf{Z}, \mathcal{C})$; si $\Psi''$ est le morphisme composé $\Psi'' \circ \Psi$, il résulte de la définition (4.3.1) et de (4.3.3.1) que l'on a $\Psi''* = \Psi^* \circ \Psi''*$.

## 4.4. Relations entre images directes et images réciproques.

(4.4.1) Les hypothèses et notations étant celles de (4.2.1), soit $\mathcal{G}$ un $\mathcal{B}$-Module. Par définition, un homomorphisme $u: \mathcal{G} \to \Psi_{*}(\mathcal{F})$ de $\mathcal{B}$-Modules s'appelle encore un $\Psi$-morphisme de $\mathcal{G}$ dans $\mathcal{F}$, ou simplement un homomorphisme de $\mathcal{G}$ dans $\mathcal{F}$ et on l'écrit $u: \mathcal{G} \to \mathcal{F}$ quand aucune confusion n'en résulte. Se donner un tel homomorphisme revient à se donner, pour tout couple (U, V) où U est un ouvert de X, V un ouvert de Y tels que $\psi(U) \subset V$, un homomorphisme $u_{U,V}: \Gamma(V, \mathcal{G}) \to \Gamma(U, \mathcal{F})$ de $\Gamma(V, \mathcal{B})$-modules, $\Gamma(U, \mathcal{F})$ étant considéré comme $\Gamma(V, \mathcal{B})$-module au moyen de l'homomorphisme d'anneaux $\theta_{U,V}: \Gamma(V, \mathcal{B}) \to \Gamma(U, \mathcal{A})$; les $u_{U,V}$ doivent en outre rendre commutatifs les diagrammes (3.5.1.1). Il suffit d'ailleurs pour définir $u$ de se donner les $u_{U,V}$ lorsque U (resp. V) parcourt une base $\mathfrak{B}$ (resp. $\mathfrak{B}'$) de la topologie de X (resp. Y) et de vérifier la commutativité de (3.5.1.1) pour ces restrictions.

(4.4.2) Sous les hypothèses de (4.2.1) et (4.2.6), soient H un C-Module,  $v : \mathcal{H} \to \Psi_{*}^{\prime}(\mathcal{G})$  un  $\Psi^{\prime}$ -morphisme; alors  $w : \mathcal{H} \xrightarrow{v} \Psi_{*}^{\prime}(\mathcal{G}) \xrightarrow{\Psi_{*}^{\prime}(u)} \Psi_{*}^{\prime}(\Psi_{*}(\mathcal{F}))$  est un  $\Psi^{\prime\prime}$ -morphisme que l'on appelle le composé de u et v.

(4.4.3) Nous allons maintenant voir que l'on peut définir un isomorphisme canonique de bifoncteurs en $\mathcal{F}$ et $\mathcal{G}$

$$
(\mathbf {4} \cdot \mathbf {4} \cdot \mathbf {3} \cdot \mathbf {1})
$$

$$
\operatorname{Hom} _ {\mathcal {A}} (\Psi^ {*} (\mathcal {G}), \mathcal {F}) \simeq \operatorname{Hom} _ {\mathcal {B}} (\mathcal {G}, \Psi_ {*} (\mathcal {F}))
$$

que nous désignerons par $v \to v_{0}^{b}$ (ou simplement $v \to v^{b}$ si aucune confusion n'est possible) ; nous noterons $u \to u_{0}^{\sharp}$, ou $u \to u^{\sharp}$ l'isomorphisme réciproque. Cette définition est la suivante : en composant $v: \Psi^{*}(\mathcal{G}) \to \mathcal{F}$ avec l'application canonique $\psi^{*}(\mathcal{G}) \to \Psi^{*}(\mathcal{G})$, on obtient un homomorphisme de faisceaux de groupes $v': \psi^{*}(\mathcal{G}) \to \mathcal{F}$, qui est aussi un homomorphisme de $\psi^{*}(\mathcal{B})$-modules. On en déduit (3.7.1) un homomorphisme $v'^{b}: \mathcal{G} \to \psi_{*}(\mathcal{F}) = \Psi_{*}(\mathcal{F})$, qui est aussi un homomorphisme de $\mathcal{B}$-Modules comme on

le vérifie sans peine ; on prend $v_{\theta}^{b}=v^{\prime b}$. De même, de $u: \mathcal{G}\to\Psi_{*}(\mathcal{F})$, qui est un homomorphisme de $\mathcal{B}$-Modules, on déduit (3.7.1) un homomorphisme $u^{\sharp}: \psi^{*}(\mathcal{G})\to\mathcal{F}$ de $\psi^{*}(\mathcal{B})$-Modules, d'où par tensorisation avec $\mathcal{A}$ un homomorphisme de $\mathcal{A}$-Modules $\Psi^{*}(\mathcal{G})\to\mathcal{F}$, que nous désignerons par $u_{\theta}^{\sharp}$. Il est immédiat de vérifier que $(u_{\theta}^{\sharp})_{0}^{b}=u$ et $(v_{\theta}^{b})_{0}^{\sharp}=v$, ainsi que le caractère fonctoriel en $\mathcal{F}$ de l'isomorphisme $v\to v_{\theta}^{b}$. Le caractère fonctoriel en $\mathcal{G}$ de $u\to u_{\theta}^{\sharp}$ s'en déduit alors formellement comme dans (3.5.4) (raisonnement qui démontrerait aussi le caractère fonctoriel de $\Psi^{*}$ établi dans (4.3.1) directement).

Si on prend pour $v$ l'homomorphisme identique de $\Psi^{*}(\mathcal{G})$, $v_{0}^{b}$ est un homomorphisme

$$
\rho_ {\mathcal {G}}: \mathcal {G} \rightarrow \Psi_ {*} (\Psi^ {*} (\mathcal {G}));\tag{4.4.3.2}
$$

si on prend pour $u$ l'homomorphisme identique de $\Psi_{*}(\mathcal{F}), u_{0}^{\sharp}$ est un homomorphisme

$$
\sigma_ {\mathcal {F}}: \Psi^ {*} (\Psi_ {*} (\mathcal {F})) \rightarrow \mathcal {F};\tag{4.4.3.3}
$$

ces homomorphismes seront dits canoniques. Ils ne sont en général ni injectifs ni surjectifs. On a des factorisations canoniques analogues à (3.5.3.3) et (3.5.4.4).

On notera que si $s$ est une section de $\mathcal{G}$ au-dessus d'un ouvert V de Y, $\rho_{\mathcal{G}}(s)$ est la section $s' \otimes 1$ de $\Psi^{*}(\mathcal{G})$ au-dessus de $\psi^{-1}(V)$, $s'$ étant telle que $s_x' = s_{\psi(x)}$ pour tout $x \in \psi^{-1}(V)$. Notons aussi que si $u: \mathcal{G} \to \psi_{*}(\mathcal{F})$ est un homomorphisme, il définit pour tout $x \in X$ un homomorphisme $u_x: \mathcal{G}_{\psi(x)} \to \mathcal{F}_x$ sur les fibres, obtenu en composant $(u^{\sharp})_x: (\Psi^{*}(\mathcal{G}))_x \to \mathcal{F}_x$ et l'homomorphisme canonique $s_x \to s_x \otimes 1$ de $\mathcal{G}_{\psi(x)}$ dans $(\Psi^{*}(\mathcal{G}))_x = \mathcal{G}_{\psi(x)} \otimes_{\mathcal{B}_{\psi(x)}} \mathcal{A}_x$. L'homomorphisme $u_x$ s'obtient aussi par passage à la limite inductive à partir des homomorphismes $\Gamma(V, \mathcal{G}) \overset{u}{\to} \Gamma(\psi^{-1}(V), \mathcal{F}) \to \mathcal{F}_x$, où V parcourt les voisinages de $\psi(x)$.

(4.4.4) Soient $\mathcal{F}_1, \mathcal{F}_2$ des $\mathcal{A}$-Modules, $\mathcal{G}_1, \mathcal{G}_2$ des $\mathcal{B}$-Modules, $u_i (i=1,2)$ un homomorphisme de $\mathcal{G}_i$ dans $\mathcal{F}_i$. Nous désignerons par $u_1 \otimes u_2$ l'homomorphisme $u: \mathcal{G}_1 \otimes_{\mathcal{B}} \mathcal{G}_2 \to \mathcal{F}_1 \otimes_{\mathcal{A}} \mathcal{F}_2$ tel que $u^\sharp = (u_1)^\sharp \otimes (u_2)^\sharp$ (compte tenu de (4.3.3.1)); on vérifie que $u$ est aussi le composé $\mathcal{G}_1 \otimes_{\mathcal{B}} \mathcal{G}_2 \to \Psi_*(\mathcal{F}_1) \otimes_{\mathcal{B}} \Psi_*(\mathcal{F}_2) \to \Psi_*(\mathcal{F}_1 \otimes_{\mathcal{A}} \mathcal{F}_2)$, où la première flèche est le produit tensoriel ordinaire $u_1 \otimes_{\mathcal{B}} u_2$ et la seconde l'homomorphisme canonique (4.2.2.1).

(4.4.5) Soient $(\mathcal{G}_{\lambda})_{\lambda \in L}$ un système inductif de $\mathcal{B}$-Modules, et, pour tout $\lambda \in L$, soit $u_{\lambda}$ un homomorphisme $\mathcal{G}_{\lambda} \to \Psi_{*}(\mathcal{F})$, formant un système inductif; posons $\mathcal{G} = \varinjlim \mathcal{G}_{\lambda}$ et $u = \varinjlim u_{\lambda}$; alors les $(u_{\lambda})^{\sharp}$ forment un système inductif d'homomorphismes $\Psi^{*}(\mathcal{G}_{\lambda}) \to \mathcal{F}$, et la limite inductive de ce système n'est autre que $u^{\sharp}$.

(4.4.6) Soient M, N deux B-Modules, V un ouvert de Y,  $U = \psi^{-1}(V)$ ; l'application  $v \to \Psi^{*}(v)$  est un homomorphisme

$$
\operatorname{Hom} _ {\mathscr {B} | \mathrm{V}} (\mathscr {M} | \mathrm{V}, \mathscr {N} | \mathrm{V}) \rightarrow \operatorname{Hom} _ {\mathscr {A} | \mathrm{U}} (\Psi^ {*} (\mathscr {M}) | \mathrm{U}, \Psi^ {*} (\mathscr {N}) | \mathrm{U})
$$

pour les structures de $\Gamma(\mathrm{V},\mathcal{B})$-module $(\mathrm{Hom}_{\mathcal{A}|\mathrm{U}}(\Psi^{*}(\mathcal{M})|\mathrm{U},\Psi^{*}(\mathcal{N})|\mathrm{U})$ est normalement muni d'une structure de $\Gamma(\mathrm{U},\psi^{*}(\mathcal{B}))$-module, et grâce à l'homomorphisme

canonique (3.7.2) $\Gamma(V, \mathcal{B}) \to \Gamma(U, \psi^{*}(\mathcal{B}))$, c'est donc aussi un $\Gamma(V, \mathcal{B})$-module). On voit aussitôt que ces homomorphismes sont compatibles avec les restrictions, et par suite définissent un homomorphisme canonique fonctoriel

$$
\gamma : \mathcal {H} o m _ {\mathcal {B}} (\mathcal {M}, \mathcal {N}) \rightarrow \Psi_ {*} ^ {*} (\mathcal {H} o m _ {\mathcal {A}} (\Psi^ {*} (\mathcal {M}), \Psi^ {*} (\mathcal {N}));
$$

il correspond par suite aussi à cet homomorphisme l'homomorphisme

$$
\gamma^ {\sharp}: \Psi^ {*} (\mathcal {H} o m _ {\mathcal {B}} (\mathcal {M}, \mathcal {N})) \rightarrow \mathcal {H} o m _ {\mathcal {A}} (\Psi^ {*} (\mathcal {M}), \Psi^ {*} (\mathcal {N}))
$$

et ces homomorphismes canoniques sont fonctoriels en M et N.

(4.4.7) Supposons que $\mathcal{F}$ (resp. $\mathcal{G}$) soit une $\mathcal{A}$-Algèbre (resp. une $\mathcal{B}$-Algèbre). Si $u: \mathcal{G} \to \Psi_{*}(\mathcal{F})$ est un homomorphisme de $\mathcal{B}$-Algèbres, $u^{\sharp}$ est un homomorphisme $\Psi^{*}(\mathcal{G}) \to \mathcal{F}$ de $\mathcal{A}$-Algèbres; cela résulte de la commutativité du diagramme

$$
\begin{array}{c} \mathcal {G} \otimes_ {\mathscr {B}} \mathcal {G} \longrightarrow \mathcal {G} \\ \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \downarrow^ {u} \\ \Psi_ {*} ^ {\circ} (\mathscr {F} \otimes_ {\mathscr {A}} \mathscr {F}) \to \Psi_ {*} ^ {\circ} (\mathscr {F}) \end{array}
$$

et de (4.4.4). De même, si $v: \Psi^{*}(\mathcal{G}) \to \mathcal{F}$ est un homomorphisme de $\mathcal{A}$-Algèbres, $v^{\flat}: \mathcal{G} \to \Psi_{*}(\mathcal{F})$ est un homomorphisme de $\mathcal{B}$-Algèbres.

(4.4.8) Soient (Z, C) un troisième espace annelé, $\Psi' = (\psi', \theta')$ un morphisme (Y, B)→(Z, C), et $\Psi'' : (X, A) \to (Z, C)$ le morphisme composé $\Psi''\circ\Psi$. Soit H un C-Module, $u'$ un homomorphisme de H dans G; le composé $v'' = v\circ v'$ est par définition l'homomorphisme de H dans F défini par $\mathcal{H} \xrightarrow{v'} \Psi'_*(G) \xrightarrow{\Psi'_*(v)} \Psi'_*(\Psi_*(\mathcal{F}))$; on vérifie que $v''^\#$ est l'homomorphisme

$$
\Psi^ {*} (\Psi^ {\prime *} (\mathcal {H})) \stackrel {{\Psi^ {*} (v ^ {\prime} \sharp)}} {{\longrightarrow}} \Psi^ {*} (\mathcal {G}) \stackrel {{v \sharp}} {{\rightarrow}} \mathcal {F}.
$$

## § 5. FAISCEAUX QUASI-COHÉRENTS ET FAISCEAUX COHÉRENTS

## 5.1. Faisceaux quasi-cohérents.

(5.1.1) Soient (X, $\mathcal{O}_{\mathrm{X}}$) un espace annelé, $\mathcal{F}$ un $\mathcal{O}_{\mathrm{X}}$-Module. La donnée d'un homomorphisme $u: \mathcal{O}_{\mathrm{X}} \to \mathcal{F}$ de $\mathcal{O}_{\mathrm{X}}$-Modules équivaut à celle de la section $s = u(1) \in \Gamma(\mathrm{X}, \mathcal{F})$. En effet, lorsque $s$ est donnée, pour toute section $t \in \Gamma(\mathrm{U}, \mathcal{O}_{\mathrm{X}})$, on a nécessairement $u(t) = t. (s|\mathrm{U})$; on dit que $u$ est défini par la section $s$. Si maintenant I est un ensemble d'indices quelconque, considérons le faisceau somme directe $\mathcal{O}_{\mathrm{X}}^{(\mathrm{I})}$, et pour tout $i \in \mathrm{I}$, soit $h_i$ l'injection canonique du $i$-ème facteur dans $\mathcal{O}_{\mathrm{X}}^{(\mathrm{I})}$; on sait que $u \to (u \circ h_i)$ est un isomorphisme de $\operatorname{Hom}_{\mathcal{O}_{\mathrm{X}}}(\mathcal{O}_{\mathrm{X}}^{(\mathrm{I})}, \mathcal{F})$ sur le produit $(\operatorname{Hom}_{\mathcal{O}_{\mathrm{X}}}(\mathcal{O}_{\mathrm{X}}, \mathcal{F}))^{\mathrm{I}}$. Il y a donc correspondance biunivoque canonique entre les homomorphismes $u: \mathcal{O}_{\mathrm{X}}^{(\mathrm{I})} \to \mathcal{F}$ et les familles de sections $(s_i)_{i \in \mathrm{I}}$ de $\mathcal{F}$ au-dessus de X. L'homomorphisme $u$ correspondant à $(s_i)$ applique un élément $(a_i) \in (\Gamma(\mathrm{U}, \mathcal{O}_{\mathrm{X}}))^{(\mathrm{I})}$ sur $\Sigma a_i. (s_i|\mathrm{U})$.

On dit que $\mathcal{F}$ est engendré par la famille $(s_i)$ si l'homomorphisme $\mathcal{O}_{\mathrm{X}}^{(\mathrm{I})} \to \mathcal{F}$ défini

par cette famille est surjectif (autrement dit, si, pour tout $x\in\mathbf{X}$, $\mathcal{F}_{x}$ est un $\mathcal{O}_{x}$-module engendré par les $(s_{i})_{x}$). On dit que $\mathcal{F}$ est engendré par ses sections au-dessus de $\mathbf{X}$ s'il est engendré par la famille de toutes ces sections (ou par une sous-famille), autrement dit, s'il existe un homomorphisme surjectif $\mathcal{O}_{\mathbf{X}}^{(\mathrm{I})}\to\mathcal{F}$ pour un I convenable.

On notera qu'un $\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{F}$ peut être tel qu'il existe un point $x_0 \in \mathrm{X}$ pour lequel $\mathcal{F}|\mathrm{U}$ n'est pas engendré par ses sections au-dessus de U, quel que soit le voisinage ouvert U de $x_0$: il suffit de prendre $\mathrm{X} = \mathbf{R}$, pour $\mathcal{O}_{\mathrm{X}}$ le faisceau simple $\mathbf{Z}$, pour $\mathcal{F}$ le sous-faisceau algébrique de $\mathcal{O}_{\mathrm{X}}$ tel que $\mathcal{F}_0 = \{\mathrm{o}\}$, $\mathcal{F}_x = \mathbf{Z}$ pour $x \neq 0$, et enfin $x_0 = 0$: la seule section de $\mathcal{F}|\mathrm{U}$ au-dessus de U est o pour un voisinage U de o.

(5.1.2) Soit $f: \mathbf{X} \to \mathbf{Y}$ un morphisme d'espaces annelés. Si $\mathcal{F}$ est un $\mathcal{O}_{\mathbf{X}}$-Module engendré par ses sections au-dessus de $\mathbf{X}$, alors l'homomorphisme canonique $f^{*}(f_{*}(\mathcal{F})) \to \mathcal{F}$ (4.4.3.3) est surjectif : en effet, avec les notations de (5.1.1), $s_{i} \otimes i$ est une section de $f^{*}(f_{*}(\mathcal{F}))$ au-dessus de $\mathbf{X}$, et son image dans $\mathcal{F}$ est $s_{i}$. L'exemple de (5.1.1) où $f$ est l'identité, montre que la réciproque de cette proposition est inexacte en général.

(5.1.3) On dit qu'un $\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{F}$ est quasi-cohérent si, pour tout $x \in \mathrm{X}$, il y a un voisinage ouvert U de $x$ tel que $\mathcal{F}|\mathrm{V}$ soit isomorphe au conoyau d'un homomorphisme de la forme $\mathcal{O}_{\mathrm{X}}^{(\mathrm{I})}|\mathrm{V} \to \mathcal{O}_{\mathrm{X}}^{(\mathrm{J})}|\mathrm{V}$, où I et J sont des ensembles d'indices arbitraires. Il est clair que $\mathcal{O}_{\mathrm{X}}$ lui-même est un $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent, et que toute somme directe de $\mathcal{O}_{\mathrm{X}}$-Modules quasi-cohérents est un $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent. On dit qu'une $\mathcal{O}_{\mathrm{X}}$-Algèbre $\mathcal{A}$ est quasi-cohérente si elle l'est en tant que $\mathcal{O}_{\mathrm{X}}$-Module.

(5.1.4) Soit $f: \mathbf{X} \to \mathbf{Y}$ un morphisme d'espaces annelés. Si $\mathcal{G}$ est un $\mathcal{O}_{\mathbf{Y}}$-Module quasi-cohérent, alors $f^{*}(\mathcal{G})$ est un $\mathcal{O}_{\mathbf{X}}$-Module quasi-cohérent. En effet, pour tout $x \in \mathbf{X}$, il y a un voisinage ouvert V de $f(x)$ dans Y tel que $\mathcal{G}|V$ soit le conoyau d'un homomorphisme $\mathcal{O}_{\mathbf{Y}}^{\mathrm{(I)}}|V \to \mathcal{O}_{\mathbf{Y}}^{\mathrm{(J)}}|V$. Si $U = f^{-1}(V)$, et si $f_{U}$ est la restriction de $f$ à U, on a $f^{*}(\mathcal{G})|U = f_{U}^{*}(\mathcal{G}|V)$; comme $f_{U}^{*}$ est exact à droite et commute aux sommes directes, $f_{U}^{*}(\mathcal{G}|V)$ est conoyau d'un homomorphisme $\mathcal{O}_{\mathbf{X}}^{\mathrm{(I)}}|U \to \mathcal{O}_{\mathbf{X}}^{\mathrm{(J)}}|U$.

## 5.2. Faisceaux de type fini.

(5.2.1) On dit qu'un $\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{F}$ est de type fini si, pour tout $x \in \mathrm{X}$, il existe un voisinage ouvert U de $x$ tel que $\mathcal{F}|\mathrm{U}$ soit engendré par une famille finie de sections au-dessus de U, ou encore soit isomorphe à un faisceau quotient d'un faisceau de la forme $(\mathcal{O}_{\mathrm{X}}|\mathrm{U})^p$ où $p$ est fini. Tout faisceau quotient d'un faisceau de type fini est de type fini, ainsi que toute somme directe finie et tout produit tensoriel fini de faisceaux de type fini. Un $\mathcal{O}_{\mathrm{X}}$-Module de type fini n'est pas nécessairement quasi-cohérent, comme on peut le voir pour le $\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{O}_{\mathrm{X}}/\mathcal{F}$, où $\mathcal{F}$ est l'exemple de (5.1.1). Si $\mathcal{F}$ est de type fini, $\mathcal{F}_x$ est un $\mathcal{O}_x$-module de type fini pour tout $x \in \mathrm{X}$, mais l'exemple (5.1.1) montre que cette condition nécessaire n'est pas en général suffisante.

(5.2.2) Soit $\mathcal{F}$ un $\mathcal{O}_{\mathrm{X}}$-Module de type fini. Si $s_i$ ($1 \leqslant i \leqslant n$) sont des sections de $\mathcal{F}$ au-dessus d'un voisinage ouvert U d'un point $x \in \mathrm{X}$ et si les $(s_i)_x$ engendrent $\mathcal{F}_x$, il existe un voisinage ouvert $\mathrm{V} \subset \mathrm{U}$ de $x$ tel que les $(s_i)_y$ engendrent $\mathcal{F}_y$ pour tout $y \in \mathrm{V}$ (FAC, I, 2, 12, prop. 1). On en conclut en particulier que le support de $\mathcal{F}$ est fermé.

De même, si $u: \mathcal{F} \to \mathcal{G}$ est un homomorphisme tel que $u_x = 0$, alors il existe un voisinage U de $x$ tel que $u_y = 0$ pour tout $y \in U$.

(5.2.3) Supposons X quasi-compact, et soient $\mathcal{F}$, $\mathcal{G}$ deux $\mathcal{O}_{\mathrm{X}}$-Modules tels que $\mathcal{G}$ soit de type fini, $u: \mathcal{F} \to \mathcal{G}$ un homomorphisme surjectif. Supposons de plus que $\mathcal{F}$ soit limite inductive d'un système inductif $(\mathcal{F}_{\lambda})$ de $\mathcal{O}_{\mathrm{X}}$-Modules. Alors il existe un indice $\mu$ tel que l'homomorphisme $\mathcal{F}_{\mu} \to \mathcal{G}$ soit surjectif. En effet, pour tout $x \in \mathrm{X}$, il existe un système fini de sections $s_i$ de $\mathcal{G}$ au-dessus d'un voisinage ouvert $\mathrm{U}(x)$ de $x$ tel que les $(s_i)_y$ engendrent $\mathcal{G}_y$ pour tout $y \in \mathrm{U}(x)$; il y a donc un voisinage ouvert $\mathrm{V}(x) \subset \mathrm{U}(x)$ de $x$ et $n$ sections $t_i$ de $\mathcal{F}$ au-dessus de $\mathrm{V}(x)$ telles que $s_i | \mathrm{V}(x) = u(t_i)$ pour tout $i$; on peut en outre supposer que les $t_i$ sont les images canoniques de sections d'un même faisceau $\mathcal{F}_{\lambda(x)}$ au-dessus de $\mathrm{V}(x)$. Couvrons alors X avec un nombre fini de voisinages $\mathrm{V}(x_k)$, et soit $\mu$ un indice supérieur à tous les $\lambda(x_k)$; il est clair que cet indice répond à la question.

Supposant toujours X quasi-compact, soit $\mathcal{F}$ un $\mathcal{O}_{\mathrm{X}}$-Module de type fini engendré par ses sections au-dessus de X (5.1.1); alors $\mathcal{F}$ est engendré par une sous-famille finie de ces sections : il suffit en effet de couvrir X par un nombre fini de voisinages ouverts $\mathrm{U}_{k}$ tels que, pour chaque $k$, il y ait un nombre fini de sections $s_{ik}$ de $\mathcal{F}$ au-dessus de X dont les restrictions à $\mathrm{U}_{k}$ engendrent $\mathcal{F}|\mathrm{U}_{k}$; il est clair que les $s_{ik}$ engendrent alors $\mathcal{F}$.

(5.2.4) Soit $f: \mathbf{X} \to \mathbf{Y}$ un morphisme d'espaces annelés. Si $\mathcal{G}$ est un $\mathcal{O}_{\mathrm{Y}}$-Module de type fini, alors $f^{*}(\mathcal{G})$ est un $\mathcal{O}_{\mathrm{X}}$-module de type fini. En effet, pour tout $x \in \mathbf{X}$, il y a un voisinage ouvert V de $f(x)$ dans Y et un homomorphisme surjectif $v: \mathcal{O}_{\mathrm{Y}}^{p}| \mathrm{V} \to \mathcal{G}| \mathrm{V}$. Si $\mathrm{U} = f^{-1}(\mathrm{V})$ et si $f_{\mathrm{U}}$ est la restriction de $f$ à U, on a $f^{*}(\mathcal{G})| \mathrm{U} = f_{\mathrm{U}}^{*}(\mathcal{G}| \mathrm{V})$; comme $f_{\mathrm{U}}$ est exact à droite (4.3.1) et commute aux sommes directes (4.3.2), $f_{\mathrm{U}}^{*}(v)$ est un homomorphisme surjectif $\mathcal{O}_{\mathrm{X}}^{p}| \mathrm{U} \to f^{*}(\mathcal{G})| \mathrm{U}$.

(5.2.5) On dit qu'un $\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{F}$ admet une présentation finie si, pour tout $x \in \mathrm{X}$, il existe un voisinage ouvert U de $x$ tel que $\mathcal{F}|\mathrm{U}$ soit isomorphe à un conoyau d'un $(\mathcal{O}_{\mathrm{X}}|\mathrm{U})$-homomorphisme $\mathcal{O}_{\mathrm{X}}^{p}|\mathrm{U} \to \mathcal{O}_{\mathrm{X}}^{q}|\mathrm{U}$, $p$ et $q$ étant deux entiers $>0$. Un tel $\mathcal{O}_{\mathrm{X}}$-Module est donc de type fini et quasi-cohérent. Si $f: \mathrm{X} \to \mathrm{Y}$ est un morphisme d'espaces annelés, et si $\mathcal{G}$ est un $\mathcal{O}_{\mathrm{Y}}$-Module admettant une présentation finie, $f^{*}(\mathcal{G})$ admet une présentation finie, comme le montre le raisonnement de (5.1.4).

(5.2.6) Soit $\mathcal{F}$ un $\mathcal{O}_{\mathrm{x}}$-Module admettant une présentation finie (5.2.5); alors, pour tout $\mathcal{O}_{\mathrm{x}}$-Module $\mathcal{H}$, l'homomorphisme canonique fonctoriel

$$
(\mathcal {H} o m _ {\mathcal {O} _ {\mathrm{X}}} (\mathcal {F}, \mathcal {H})) _ {x} \rightarrow \operatorname{Hom} _ {\mathcal {O} _ {x}} (\mathcal {F} _ {x}, \mathcal {H} _ {x})
$$

est bijectif (T, 4.1.1).

(5.2.7) Soient $\mathcal{F}$, $\mathcal{G}$ deux $\mathcal{O}_{\mathrm{X}}$-Modules ayant une présentation finie. Si, pour un $x \in \mathrm{X}$, $\mathcal{F}_x$ et $\mathcal{G}_x$ sont deux $\mathcal{O}_x$-modules isomorphes, alors il existe un voisinage ouvert U de $x$ tel que $\mathcal{F}|\mathrm{U}$ et $\mathcal{G}|\mathrm{U}$ soient isomorphes. En effet, si $\varphi: \mathcal{F}_x \to \mathcal{G}_x$ et $\psi: \mathcal{G}_x \to \mathcal{F}_x$ sont deux isomorphismes réciproques, il existe, d'après (5.2.6), un voisinage ouvert V de $x$ et une section $u$ (resp. $v$) de $\mathcal{Hom}_{\mathcal{O}_{\mathrm{X}}}(\mathcal{F}, \mathcal{G})$ (resp. $\mathcal{Hom}_{\mathcal{O}_{\mathrm{X}}}(\mathcal{G}, \mathcal{F})$) au-dessus de V telle

que $u_x = \varphi$ (resp. $v_x = \psi$). Comme $(u \circ v)_x$ et $(v \circ u)_x$ sont les automorphismes identiques, il existe un voisinage ouvert U ⊂ V de x tel que $(u \circ v) | U$ et $(v \circ u) | U$ soient les automorphismes identiques, d'où la proposition.

## 5.3. Faisceaux cohérents.

(5.3.1) On dit qu'un $\mathcal{O}_{\mathrm{x}}$-Module $\mathcal{F}$ est cohérent s'il vérifie les deux conditions suivantes :

a) $\mathcal{F}$ est de type fini.

b) Pour tout ouvert  $U \subset X$ , tout entier n > 0, et tout homomorphisme u :  $O_{X}^{n} | U \to F | U$ , le noyau de u est de type fini.

On notera que ces deux conditions sont de caractère local.

Pour la plupart des démonstrations des propriétés des faisceaux cohérents rappelées dans ce qui suit, cf. (FAC), I, 2.

(5.3.2) Tout $\mathcal{O}_{\mathrm{X}}$-Module cohérent admet une présentation finie (5.2.5); la réciproque n'est pas nécessairement exacte, car $\mathcal{O}_{\mathrm{X}}$ lui-même n'est pas nécessairement un $\mathcal{O}_{\mathrm{X}}$-Module cohérent.

Tout sous-$\mathcal{O}_{\mathrm{X}}$-Module de type fini d'un $\mathcal{O}_{\mathrm{X}}$-Module cohérent est cohérent ; toute somme directe finie de $\mathcal{O}_{\mathrm{X}}$-Modules cohérents est un $\mathcal{O}_{\mathrm{X}}$-Module cohérent.

(5.3.3) Si $o \to \mathcal{F} \to \mathcal{G} \to \mathcal{H} \to o$ est une suite exacte de $\mathcal{O}_x$-Modules et si deux de ces $\mathcal{O}_x$-Modules sont cohérents, il en est de même du troisième.

(5.3.4) Si $\mathcal{F}$ et $\mathcal{G}$ sont deux $\mathcal{O}_{\mathrm{X}}$-Modules cohérents, $u: \mathcal{F} \to \mathcal{G}$ un homomorphisme, $\operatorname{Im}(u)$, $\operatorname{Ker}(u)$ et $\operatorname{Coker}(u)$ sont des $\mathcal{O}_{\mathrm{X}}$-Modules cohérents. En particulier, si $\mathcal{F}$ et $\mathcal{G}$ sont des sous-$\mathcal{O}_{\mathrm{X}}$-Modules cohérents d'un $\mathcal{O}_{\mathrm{X}}$-Module cohérent, $\mathcal{F} + \mathcal{G}$ et $\mathcal{F} \cap \mathcal{G}$ sont cohérents.

(5.3.5) Si $\mathcal{F}$ et $\mathcal{G}$ sont deux $\mathcal{O}_{\mathrm{X}}$-Modules cohérents, il en est de même de $\mathcal{F} \otimes_{\mathcal{O}_{\mathrm{X}}} \mathcal{G}$ et de $\mathcal{Hom}_{\mathcal{O}_{\mathrm{X}}}(\mathcal{F}, \mathcal{G})$.

(5.3.6) Soient $\mathcal{F}$ un $\mathcal{O}_{\mathrm{X}}$-Module cohérent, $\mathcal{J}$ un faisceau cohérent d'idéaux de $\mathcal{O}_{\mathrm{X}}$. Alors le $\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{J}\mathcal{F}$ est cohérent, en tant qu'image de $\mathcal{J} \otimes_{\mathcal{O}_{\mathrm{X}}} \mathcal{F}$ par l'homomorphisme canonique $\mathcal{J} \otimes_{\mathcal{O}_{\mathrm{X}}} \mathcal{F} \to \mathcal{F}$ (5.3.4 et 5.3.5).

(5.3.7) On dit qu'une $\mathcal{O}_{\mathrm{X}}$-Algèbre $\mathcal{A}$ est cohérente si $\mathcal{A}$ est un $\mathcal{O}_{\mathrm{X}}$-Module cohérent. En particulier, $\mathcal{O}_{\mathrm{X}}$ est un faisceau cohérent d'anneaux si, et seulement si, pour tout ouvert $\mathrm{U} \subset \mathrm{X}$ et tout homomorphisme de la forme $u: \mathcal{O}_{\mathrm{X}}^{p} | \mathrm{U} \to \mathcal{O}_{\mathrm{X}} | \mathrm{U}$, le noyau de $u$ est un $(\mathcal{O}_{\mathrm{X}} | \mathrm{U})$-Module de type fini.

Si $\mathcal{O}_{\mathrm{x}}$ est un faisceau cohérent d'anneaux, tout $\mathcal{O}_{\mathrm{x}}$-Module $\mathcal{F}$ admettant une présentation finie (5.2.5) est cohérent, en vertu de (5.3.4).

L'annulateur d'un $\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{F}$ est le noyau $\mathcal{J}$ de l'homomorphisme canonique $\mathcal{O}_{\mathrm{X}} \to \mathcal{H}om_{\mathcal{O}_{\mathrm{X}}}(\mathcal{F}, \mathcal{F})$ qui, à toute section $s \in \Gamma(\mathrm{U}, \mathcal{O}_{\mathrm{X}})$ fait correspondre la multiplication par $s$ dans $\operatorname{Hom}(\mathcal{F}|\mathrm{U}, \mathcal{F}|\mathrm{U})$; si $\mathcal{O}_{\mathrm{X}}$ est cohérent et si $\mathcal{F}$ est un $\mathcal{O}_{\mathrm{X}}$-Module cohérent, $\mathcal{J}$ est cohérent (5.3.4 et 5.3.5) et pour tout $x \in \mathrm{X}$, $\mathcal{J}_x$ est l'annulateur de $\mathcal{F}_x$ (5.2.6).

(5.3.8) Supposons $\mathcal{O}_{\mathrm{X}}$ cohérent; soient $\mathcal{F}$ un $\mathcal{O}_{\mathrm{X}}$-Module cohérent, $x$ un point de X, M un sous-module de type fini de $\mathcal{F}_x$; il existe alors un voisinage ouvert U de $x$ et un sous-$(\mathcal{O}_{\mathrm{X}}|\mathrm{U})$-Module cohérent $\mathcal{G}$ de $\mathcal{F}|\mathrm{U}$ tel que $\mathcal{G}_x = \mathrm{M}$ (T, 4.1, lemme 1).

Ce résultat, joint aux propriétés des sous-$\mathcal{O}_{\mathrm{X}}$-Modules d'un $\mathcal{O}_{\mathrm{X}}$-Module cohérent, impose des conditions nécessaires aux anneaux $\mathcal{O}_{x}$ pour que $\mathcal{O}_{\mathrm{X}}$ soit cohérent. Par exemple (5·3·4), l'intersection de deux idéaux de type fini de $\mathcal{O}_{x}$ doit encore être un idéal de type fini.

(5.3.9) Supposons $\mathcal{O}_{\mathrm{X}}$ cohérent, et soit M un $\mathcal{O}_{x}$-module admettant une présentation finie, donc isomorphe à un conoyau d'un homomorphisme $\varphi: \mathcal{O}_{x}^{p} \to \mathcal{O}_{x}^{q}$; alors il existe un voisinage ouvert U de X et un $(\mathcal{O}_{\mathrm{X}}|\mathrm{U})$-Module cohérent $\mathcal{F}$ tel que $\mathcal{F}_{x}$ soit isomorphe à M. En effet, en vertu de (5.2.6), il existe une section $u$ de $\mathcal{Hom}_{\mathcal{O}_{\mathrm{X}}}(\mathcal{O}_{\mathrm{X}}^{p}, \mathcal{O}_{\mathrm{X}}^{q})$ telle que $u_{x} = \varphi$; le conoyau $\mathcal{F}$ de l'homomorphisme $u: \mathcal{O}_{\mathrm{X}}^{p}|\mathrm{U} \to \mathcal{O}_{\mathrm{X}}^{q}|\mathrm{U}$ répond à la question (5.3.4).

(5.3.10) Supposons $\mathcal{O}_{\mathrm{X}}$ cohérent, et soit $\mathcal{J}$ un faisceau cohérent d'idéaux dans $\mathcal{O}_{\mathrm{X}}$. Pour qu'un $(\mathcal{O}_{\mathrm{X}} / \mathcal{J})$-Module $\mathcal{F}$ soit cohérent, il faut et il suffit qu'il soit cohérent en tant que $\mathcal{O}_{\mathrm{X}}$-Module. En particulier $\mathcal{O}_{\mathrm{X}} / \mathcal{J}$ est un faisceau cohérent d'anneaux.

(5.3.11) Soit $f: \mathrm{X} \to \mathrm{Y}$ un morphisme d'espaces annelés, et supposons $\mathcal{O}_{\mathrm{X}}$ cohérent; alors, pour tout $\mathcal{O}_{\mathrm{Y}}$-Module cohérent $\mathcal{G}, f^{*}(\mathcal{G})$ est un $\mathcal{O}_{\mathrm{X}}$-Module cohérent. En effet, avec les notations de (5.2.4), on peut supposer que $\mathcal{G}|\mathrm{V}$ est conoyau d'un homomorphisme $v: \mathcal{O}_{\mathrm{Y}}^{q}|\mathrm{V} \to \mathcal{O}_{\mathrm{Y}}^{p}|\mathrm{V}$; comme $f_{\mathrm{U}}^{*}$ est exact à droite, $f^{*}(\mathcal{G})|\mathrm{U} = f_{\mathrm{U}}^{*}(\mathcal{G}|\mathrm{V})$ est conoyau de l'homomorphisme $f_{\mathrm{U}}^{*}(v): \mathcal{O}_{\mathrm{X}}^{q}|\mathrm{U} \to \mathcal{O}_{\mathrm{X}}^{p}|\mathrm{U}$, d'où notre assertion.

(5.3.12) Soient Y une partie fermée de X,  $j: Y \to X$  l'injection canonique,  $O_{Y}$  un faisceau d'anneaux sur Y, et posons  $\mathcal{O}_{\mathrm{X}} = j_{*}(\mathcal{O}_{\mathrm{Y}})$ . Pour qu'un  $O_{Y}$ -Module G soit de type fini (resp. quasi-cohérent, cohérent), il faut et il suffit que  $j_{*}(\mathcal{G})$  soit un  $O_{X}$ -Module de type fini (resp. quasi-cohérent, cohérent).

## 5.4. Faisceaux localement libres.

(5.4.1) Soit X un espace annelé. On dit qu'un $\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{F}$ est localement libre si, pour tout $x \in \mathrm{X}$, il existe un voisinage ouvert U de $x$ tel que $\mathcal{F}|\mathrm{U}$ soit isomorphe à un $(\mathcal{O}_{\mathrm{X}}|\mathrm{U})$-Module de la forme $\mathcal{O}_{\mathrm{X}}^{(\mathrm{I})}|\mathrm{U}$, où I peut dépendre de U. Si pour tout U, I est fini, on dit que $\mathcal{F}$ est de rang fini; si pour tout U, I a le même nombre fini d'éléments $n$, on dit que $\mathcal{F}$ est de rang $n$. Un $\mathcal{O}_{\mathrm{X}}$-Module localement libre de rang i est encore appelé inversible (cf. (5.4.3)). Si $\mathcal{F}$ est un $\mathcal{O}_{\mathrm{X}}$-Module localement libre de rang fini, pour tout $x \in \mathrm{X}$, $\mathcal{F}_x$ est un $\mathcal{O}_x$-module libre de rang fini $n(x)$, et il existe un voisinage U de $x$ tel que $\mathcal{F}|\mathrm{U}$ soit de rang $n(x)$; si X est connexe, $n(x)$ est donc constant.

Il est clair que tout faisceau localement libre est quasi-cohérent, et si  $O_{X}$  est un faisceau cohérent d'anneaux, tout  $O_{X}$ -Module localement libre de rang fini est cohérent.

Si $\mathcal{L}$ est localement libre, $\mathcal{L} \otimes_{\mathcal{O}_{\mathrm{X}}}\mathcal{F}$ est un foncteur exact en $\mathcal{F}$ dans la catégorie des $\mathcal{O}_{\mathrm{X}}$-Modules.

Nous aurons surtout à considérer des $\mathcal{O}_{\mathrm{X}}$-Modules localement libres de rang fini,

et lorsque nous parlerons de faisceaux localement libres sans préciser, il sera sous-entendu qu'ils sont de rang fini.

(5.4.2) Si $\mathcal{L}$, $\mathcal{F}$ sont deux $\mathcal{O}_{\mathrm{X}}$-Modules, on a un homomorphisme canonique fonctoriel

$$
\check {\mathcal {L}} \otimes_ {\mathcal {O} _ {\mathrm{X}}} \mathcal {F} = \mathcal {H} o m _ {\mathcal {O} _ {\mathrm{X}}} (\mathcal {L}, \mathcal {O} _ {\mathrm{X}}) \otimes_ {\mathcal {O} _ {\mathrm{X}}} \mathcal {F} \rightarrow \mathcal {H} o m _ {\mathcal {O} _ {\mathrm{X}}} (\mathcal {L}, \mathcal {F})\tag{5.4.2.1}
$$

défini de la façon suivante : pour tout ouvert U, à tout couple  $(u,t)$ , où  $u\in\Gamma(\mathrm{U},\mathcal{H}om_{\mathcal{O}_{\mathrm{X}}}(\mathcal{L},\mathcal{O}_{\mathrm{X}}))=\mathrm{Hom}(\mathcal{L}|\mathrm{U},\mathcal{O}_{\mathrm{X}}|\mathrm{U})$  et  $t\in\Gamma(\mathrm{U},\mathcal{F})$ , on fait correspondre l'élément de  $\mathrm{Hom}(\mathcal{L}|\mathrm{U},\mathcal{F}|\mathrm{U})$  qui, pour tout  $x\in U$ , fait correspondre à  $s_{x}\in\mathcal{L}_{x}$  l'élément  $u_{x}(s_{x})t_{x}$  de  $F_{x}$ . Si L est localement libre de rang fini, cet homomorphisme est bijectif; la propriété étant locale, on peut en effet se borner au cas où  $L=O_{X}^{n}$ ; comme pour tout  $O_{X}$ -Module G,  $\mathrm{Hom}_{\mathcal{O}_{\mathrm{X}}}(O_{X}^{n},G)$  est canoniquement isomorphe à  $G^{n}$ , on est ramené au cas  $L=O_{X}$ , qui est immédiat.

(5.4.3) Si $\mathcal{L}$ est inversible, il en est de même de son dual $\mathcal{L} = \mathcal{H}om_{\mathcal{O}_{\mathrm{X}}}( \mathcal{L}, \mathcal{O}_{\mathrm{X}})$, car on se ramène aussitôt (la question étant locale) au cas $\mathcal{L} = \mathcal{O}_{\mathrm{X}}$. En outre, on a un isomorphisme canonique

$$
\mathcal {H} o m _ {\mathcal {O} _ {\mathrm{X}}} (\mathcal {L}, \mathcal {O} _ {\mathrm{X}}) \otimes_ {\mathcal {O} _ {\mathrm{X}}} \mathcal {L} \xrightarrow {\sim} \mathcal {O} _ {\mathrm{X}}\tag{5.4.3.1}
$$

en effet, d'après (5.4.2), il suffit de définir un isomorphisme canonique $\mathcal{H}om_{\mathcal{O}_{\mathrm{X}}}(L, L) \xrightarrow{\sim} \mathcal{O}_{\mathrm{X}}$. Or, pour tout $\mathcal{O}_{\mathrm{X}}$-Module $F$, on a un homomorphisme canonique $\mathcal{O}_{\mathrm{X}} \xrightarrow{\sim} \mathcal{H}om_{\mathcal{O}_{\mathrm{X}}}(F, F)$ (5.3.7). Il reste à prouver que si $F = L$ est inversible, cet homomorphisme est bijectif, et comme la question est locale, on est ramené au cas $L = \mathcal{O}_{\mathrm{X}}$, qui est immédiat.

En raison de ce qui précède, on pose $\mathcal{L}^{-1} = \mathcal{H}om_{\mathcal{O}_{\mathrm{X}}}( \mathcal{L}, \mathcal{O}_{\mathrm{X}})$, et on dit que $\mathcal{L}^{-1}$ est l'inverse de $\mathcal{L}$. La terminologie de « faisceau inversible » peut se justifier de la façon suivante lorsque X est réduit à un point et $\mathcal{O}_{\mathrm{X}}$ est un anneau local A d'idéal maximal m; si M et M' sont deux A-modules (M étant de type fini) tels que $\mathbf{M} \otimes_{\mathrm{A}} \mathbf{M}'$ soit isomorphe à A, comme $(\mathrm{A} / \mathfrak{m}) \otimes_{\mathrm{A}} (\mathbf{M} \otimes_{\mathrm{A}} \mathbf{M}')$ s'identifie à $(\mathbf{M} / \mathfrak{m}\mathbf{M}) \otimes_{\mathrm{A} / \mathfrak{m}} (\mathbf{M}' / \mathfrak{m}\mathbf{M}')$, ce dernier produit tensoriel d'espaces vectoriels sur le corps A/m est isomorphe à A/m, ce qui exige que M/mM et M'/mM' soient de dimension 1. Pour tout élément $z \in \mathbf{M}$ n'appartenant pas à mM, on a donc $\mathbf{M} = \mathbf{A}z + \mathfrak{m}\mathbf{M}$, ce qui entraîne $\mathbf{M} = \mathbf{A}z$ d'après le lemme de Nakayama, M étant de type fini. D'ailleurs, comme l'annulateur de $z$ annule $\mathbf{M} \otimes_{\mathrm{A}} \mathbf{M}'$, isomorphe à A, cet annulateur est {o}, et M est par suite isomorphe à A. Dans le cas général, cela montre que si $\mathcal{L}$ est un $\mathcal{O}_{\mathrm{X}}$-Module de type fini, tel qu'il existe un $\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{F}$ pour lequel $\mathcal{L} \otimes_{\mathcal{O}_{\mathrm{X}}} \mathcal{F}$ soit isomorphe à $\mathcal{O}_{\mathrm{X}}$, et si en outre les anneaux $\mathcal{O}_{x}$ sont des anneaux locaux, alors $\mathcal{L}_{x}$ est un $\mathcal{O}_{x}$-module isomorphe à $\mathcal{O}_{x}$ pour tout $x \in \mathrm{X}$. Si $\mathcal{O}_{\mathrm{X}}$ et $\mathcal{L}$ sont supposés cohérents, on en conclut donc que $\mathcal{L}$ est inversible en vertu de (5.2.7).

(5.4.4) Si $\mathcal{L}$ et $\mathcal{L}'$ sont deux $\mathcal{O}_{\mathrm{X}}$-Modules inversibles, il en est de même de $\mathcal{L} \otimes_{\mathcal{O}_{\mathrm{X}}} \mathcal{L}'$, car la question étant locale, on peut supposer que $\mathcal{L} = \mathcal{O}_{\mathrm{X}}$, et le résultat est alors trivial. Pour tout entier $n \geqslant 1$, on désigne par $\mathcal{L}^{\otimes n}$ le produit tensoriel de $n$ faisceaux

identiques à $\mathcal{L}$; on pose par convention $\mathcal{L}^{\otimes 0} = \mathcal{O}_{\mathrm{X}}$ et pour $n \geqslant 1$, $\mathcal{L}^{\otimes (-n)} = (\mathcal{L}^{-1})^{\otimes n}$. Avec ces notations, il existe alors un isomorphisme canonique fonctoriel

$$
\mathcal {L} ^ {\otimes m} \otimes_ {\mathcal {O} _ {\mathrm{X}}} \mathcal {L} ^ {\otimes n} \stackrel {{\sim}} {{\to}} \mathcal {L} ^ {\otimes (n + m)}\tag{5.4.4.1}
$$

quels que soient les entiers rationnels $m$, $n$: en effet, en vertu des définitions, on se ramène aussitôt au cas où $m = -1$, $n = 1$, et l'isomorphisme en question a alors été défini en (5.4.3).

(5.4.5) Soit $f: \mathrm{Y} \to \mathrm{X}$ un morphisme d'espaces annelés. Si $\mathcal{L}$ est un $\mathcal{O}_{\mathrm{X}}$-Module localement libre (resp. invertible), $f^{*}(\mathcal{L})$ est un $\mathcal{O}_{\mathrm{Y}}$-Module localement libre (resp. invertible): cela résulte aussitôt de ce que les images réciproques de deux $\mathcal{O}_{\mathrm{X}}$-Modules localement isomorphes sont localement isomorphes, de ce que $f^{*}$ commute aux sommes directes finies et de ce que $f^{*}(\mathcal{O}_{\mathrm{X}}) = \mathcal{O}_{\mathrm{Y}}$ (4.3.4). En outre, on sait qu'on a un homomorphisme canonique fonctoriel $f^{*}(\check{\mathcal{L}}) \to (f^{*}(\mathcal{L}))^{\vee}$ (4.4.6), et lorsque L est localement libre, cet homomorphisme est bijectif: on est en effet encore ramené au cas où $\mathcal{L} = \mathcal{O}_{\mathrm{X}}$ qui est trivial. On en conclut que si $\mathcal{L}$ est invertible, $f^{*}(\mathcal{L}^{\otimes n})$ s'identifie canoniquement à $(f^{*}(\mathcal{L}))^{\otimes n}$ pour tout entier rationnel $n$.

(5.4.6) Soit $\mathcal{L}$ un $\mathcal{O}_{\mathrm{X}}$-Module invertible; on désigne par $\Gamma_{*}(\mathbf{X},\mathcal{L})$ ou simplement $\Gamma_{*}(\mathcal{L})$ le groupe abélien somme directe $\bigoplus_{n\in \mathbf{Z}}\Gamma (\mathbf{X},\mathcal{L}^{\otimes n})$; on le munit d'une structure d'anneau gradué, en faisant correspondre au couple $(s_n,s_m)$, où $s_n\in \Gamma (\mathbf{X},\mathcal{L}^{\otimes n})$, $s_m\in \Gamma (\mathbf{X},\mathcal{L}^{\otimes n})$, la section de $\mathcal{L}^{\otimes (n + m)}$ au-dessus de $\mathbf{X}$ qui correspond canoniquement (5.4.4.1) à la section $s_n\otimes s_m$ de $\mathcal{L}^{\otimes n}\otimes_{\mathcal{O}_\mathrm{X}}\mathcal{L}^{\otimes m}$; l'associativité de cette multiplication se vérifie de façon immédiate. Il est clair que $\Gamma_{*}(\mathbf{X},\mathcal{L})$ est un foncteur covariant en $\mathcal{L}$, à valeurs dans la catégorie des anneaux gradués.

Si maintenant F est un  $O_{X}$ -Module quelconque, on pose

$$
\Gamma_ {*} (\mathcal {L}, \mathcal {F}) = \underset {n \in \mathbf {Z}} {\oplus} \Gamma (\mathrm{X}, \mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{X}}} \mathcal {L} ^ {\otimes n}).
$$

On munit ce groupe abélien d'une structure de module gradué sur l'anneau gradué $\Gamma_{*}(\mathcal{L})$ de la façon suivante : au couple $(s_n, u_m)$, où $s_n \in \Gamma(\mathbf{X}, \mathcal{L}^{\otimes n})$ et $u_m \in \Gamma(\mathbf{X}, \mathcal{F} \otimes \mathcal{L}^{\otimes m})$, on fait correspondre la section de $\mathcal{F} \otimes \mathcal{L}^{\otimes (m+n)}$ qui correspond canoniquement (5.4.4.1) à $s_n \otimes u_m$; la vérification des axiomes des modules est immédiate. Pour X et $\mathcal{L}$ fixés, $\Gamma_{*}(\mathcal{L}, \mathcal{F})$ est un foncteur covariant en $\mathcal{F}$ à valeurs dans la catégorie des $\Gamma_{*}(\mathcal{L})$-modules gradués ; pour X et $\mathcal{F}$ fixés, c'est un foncteur covariant en $\mathcal{L}$ à valeurs dans la catégorie des groupes abéliens.

Si $f: \mathbf{Y} \to \mathbf{X}$ est un morphisme d'espaces annelés, l'homomorphisme canonique (4.4.3.2) $\rho: \mathcal{L}^{\otimes n} \to f_*(f^*(\mathcal{L}^{\otimes n}))$ définit un homomorphisme de groupes abéliens $\Gamma(\mathbf{X}, \mathcal{L}^{\otimes n}) \to \Gamma(\mathbf{Y}, f^*(\mathcal{L}^{\otimes n}))$, et comme $f^*(\mathcal{L}^{\otimes n}) = (f^*(\mathcal{L}))^{\otimes n}$, il résulte des définitions des homomorphismes canoniques (4.4.3.2) et (5.4.4.1) que les homomorphismes précédents définissent un homomorphisme fonctoriel d'anneaux gradués $\Gamma_*(\mathcal{L}) \to \Gamma_*(f^*(\mathcal{L}))$. Le même homomorphisme canonique (4.4.3) définit de même un homomorphisme de groupes abéliens $\Gamma(\mathbf{X}, \mathcal{F} \otimes \mathcal{L}^{\otimes n}) \to \Gamma(\mathbf{Y}, f^*(\mathcal{F} \otimes \mathcal{L}^{\otimes n}))$, et comme

$$
f ^ {*} (\mathcal {F} \otimes \mathcal {L} ^ {\otimes n}) = f ^ {*} (\mathcal {F}) \otimes (f ^ {*} (\mathcal {L})) ^ {\otimes n} (4. 3. 3. 1),
$$

ces homomorphismes (pour $n$ variable) définissent un di-homomorphisme de modules gradués $\Gamma_{*}(\mathcal{L},\mathcal{F})\to\Gamma_{*}(f^{*}(\mathcal{L}),f^{*}(\mathcal{F}))$.

(5.4.7) On peut montrer qu'il existe un ensemble $\mathfrak{M}$ (noté aussi $\mathfrak{M}(\mathbf{X})$) de $\mathcal{O}_{\mathbf{X}}$-Modules inversibles tel que tout $\mathcal{O}_{\mathbf{X}}$-Module inversible soit isomorphe à un élément de $\mathfrak{M}$ et un seul (1) ; on définit dans $\mathfrak{M}$ une loi de composition en faisant correspondre à deux éléments $\mathscr{L}, \mathscr{L}'$ de $\mathfrak{M}$ l'unique élément de $\mathfrak{M}$ isomorphe à $\mathscr{L} \otimes \mathscr{L}'$. Avec cette loi de composition, $\mathfrak{M}$ est un groupe isomorphe au groupe de cohomologie $\mathrm{H}^1(\mathrm{X}, \mathcal{O}_\mathrm{X}^*)$, où $\mathcal{O}_\mathrm{X}^*$ est le sous-faisceau de $\mathcal{O}_{\mathrm{X}}$ tel que $\Gamma(\mathrm{U}, \mathcal{O}_\mathrm{X}^*)$ soit le groupe des éléments inversibles de l'anneau $\Gamma(\mathrm{U}, \mathcal{O}_{\mathrm{X}})$ pour tout ouvert $\mathrm{U} \subset \mathrm{X}$ ($\mathcal{O}_\mathrm{X}^*$ est donc un faisceau de groupes abéliens multiplicatifs).

On notera pour cela que pour tout ouvert  $U \subset X$ , le groupe des sections  $\Gamma(\mathrm{U}, \mathcal{O}_{\mathrm{X}}^{*})$  s'identifie canoniquement au groupe des automorphismes du  $(\mathcal{O}_{\mathrm{X}}|\mathrm{U})$ -Module  $O_{X}|U$ , l'identification faisant correspondre à une section  $\varepsilon$  de  $O_{X}^{*}$  au-dessus de U l'automorphisme u de  $O_{X}|U$  tel que  $u_{x}(s_{x}) = \varepsilon_{x}s_{x}$  pour tout  $x \in X$  et tout  $s_{x} \in O_{x}$ . Soit alors  $\mathfrak{U} = (\mathrm{U}_{\lambda})$  un recouvrement ouvert de X; la donnée, pour tout couple d'indices  $(\lambda, \mu)$  d'un automorphisme  $\theta_{\lambda\mu}$  de  $\mathcal{O}_{\mathrm{X}}|(\mathrm{U}_{\lambda} \cap \mathrm{U}_{\mu})$  revient à se donner une i-cochaîne du recouvrement U, à valeurs dans  $O_{X}^{*}$ , et dire que les  $\theta_{\lambda\mu}$  vérifient la condition de recollement (3.3.1) signifie que la cochaîne correspondante est un cocycle. De même, la donnée, pour tout  $\lambda$ , d'un automorphisme  $\omega_{\lambda}$  de  $O_{X}|U_{\lambda}$  revient à la donnée d'une o-cochaîne du recouvrement U, à valeurs dans  $O_{X}^{*}$ , et son cobord correspond à la famille des automorphismes  $(\omega_{\lambda}|U_{\lambda} \cap U_{\mu}) \circ (\omega_{\mu}|U_{\lambda} \cap U_{\mu})^{-1}$ . On peut faire correspondre à tout i-cocycle de U à valeurs dans  $O_{X}^{*}$  l'élément de M isomorphe au  $O_{X}$ -Module inversible obtenu par recollement à partir de la famille d'automorphismes  $(\theta_{\lambda\mu})$  correspondant à ce cocycle, et à deux cocycles cohomologues correspondent deux éléments égaux de M (3.3.2); autrement dit, on a ainsi défini une application  $\varphi_{\mathfrak{U}} : H^{1}(\mathfrak{U}, \mathcal{O}_{\mathrm{X}}^{*}) \to \mathfrak{M}$ . En outre, si V est un second recouvrement ouvert de X, plus fin que U, le diagramme

$$
\begin{array}{c} \mathbf {H} ^ {1} (\mathfrak {U},   \mathcal {O} _ {\mathrm{X}} ^ {*}) \stackrel {{\varphi_ {\mathfrak {U}}}} {{\searrow}} \\ \Big \downarrow \\ \mathbf {H} ^ {1} (\mathfrak {B},   \mathcal {O} _ {\mathrm{X}} ^ {*}) \stackrel {{\nearrow}} {{\nearrow}} _ {\mathfrak {V}} \end{array} \mathfrak {M}
$$

où la flèche verticale est l'homomorphisme canonique (G, II, 5.7), est commutatif, comme il résulte de (3.3.3). Par passage à la limite inductive, on obtient donc bien une application $\mathbf{H}^1 (\mathbf{X},\mathcal{O}_{\mathrm{X}}^{*})\to \mathfrak{M}$, le groupe de cohomologie de Čech $\check{\mathbf{H}}^1 (\mathbf{X},\mathcal{O}_X^*)$ s'identifiant comme on sait au premier groupe de cohomologie $\mathbf{H}^1 (\mathbf{X},\mathcal{O}_X^*)$ (G, II, 5.9, cor. du th. 5.9.1). Cette application est surjective : en effet, par définition, pour tout $\mathcal{O}_{\mathrm{X}}$-Module invertible $\mathscr{L}$, il y a un recouvrement ouvert $(\mathrm{U}_{\lambda})$ de X tel que $\mathscr{L}$ s'obtienne par recollement des faisceaux $\mathcal{O}_{\mathrm{X}}|\mathrm{U}_{\lambda}$ (3.3.1). Elle est aussi injective, car il suffit de le prouver pour les applications $\mathbf{H}^1 (\mathfrak{U},\mathcal{O}_X)\to \mathfrak{M}$, et cela résulte alors de (3.3.2). Il reste à montrer que

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Voir le livre en préparation cité dans l'Introduction.</span></small>

la bijection ainsi définie est un homomorphisme de groupe. Or, étant donnés deux $\mathcal{O}_{\mathrm{X}}$-Modules inversibles $\mathcal{L}$, $\mathcal{L}'$, il y a un recouvrement ouvert $(\mathbf{U}_{\lambda})$ tel que $\mathcal{L}|\mathbf{U}_{\lambda}$ et $\mathcal{L}'|\mathbf{U}_{\lambda}$ soient isomorphes à $\mathcal{O}_{\mathrm{X}}|\mathbf{U}_{\lambda}$ pour tout $\lambda$; il y a donc pour chaque indice $\lambda$ un élément $a_{\lambda}$ (resp. $a_{\lambda}'$) de $\Gamma(\mathbf{U}_{\lambda},\mathcal{L})$ (resp. $\Gamma(\mathbf{U}_{\lambda},\mathcal{L}')$) tel que les éléments de $\Gamma(\mathbf{U}_{\lambda},\mathcal{L})$ (resp. $\Gamma(\mathbf{U}_{\lambda},\mathcal{L}')$) soient les $s_{\lambda}.a_{\lambda}$ (resp. $s_{\lambda}.a_{\lambda}'$), où $s_{\lambda}$ parcourt $\Gamma(\mathbf{U}_{\lambda},\mathcal{O}_{\mathrm{X}})$. Les cocycles correspondants $(\varepsilon_{\lambda \mu})$, $(\varepsilon_{\lambda \mu}')$ sont tels que $s_{\lambda}.a_{\lambda}=s_{\mu}.a_{\mu}$ (resp. $s_{\lambda}.a_{\lambda}'=s_{\mu}.a_{\mu}'$) au-dessus de $\mathbf{U}_{\lambda}\cap\mathbf{U}_{\mu}$ soit équivalent à $s_{\lambda}=\varepsilon_{\lambda \mu}s_{\mu}$ (resp. $s_{\lambda}=\varepsilon_{\lambda \mu}'s_{\mu}$) au-dessus de $\mathbf{U}_{\lambda}\cap\mathbf{U}_{\mu}$. Comme les sections de $\mathcal{L}\otimes_{\mathcal{O}_{\mathrm{X}}}\mathcal{L}'$ au-dessus de $\mathbf{U}_{\lambda}$ sont les sommes finies des $s_{\lambda}s_{\lambda}'.(a_{\lambda}\otimes a_{\lambda}')$ où $s_{\lambda}$ et $s_{\lambda}'$ parcourent $\Gamma(\mathbf{U}_{\lambda},\mathcal{O}_{\mathrm{X}})$, il est clair que le cocycle $(\varepsilon_{\lambda \mu}\varepsilon_{\lambda \mu}')$ correspond à $\mathcal{L}\otimes_{\mathcal{O}_{\mathrm{X}}}\mathcal{L}'$, ce qui achève la démonstration (1).

(5.4.8) Soit $f=(\psi,\omega)$ un morphisme Y→X d'espaces annelés. Le foncteur $f^{*}(\mathscr{L})$ dans la catégorie des $\mathcal{O}_{\mathrm{X}}$-Modules libres définit une application (encore notée $f^{*}$ par abus de langage) de l'ensemble $\mathfrak{M}(\mathrm{X})$ dans l'ensemble $\mathfrak{M}(\mathrm{Y})$. D'autre part, on a un homomorphisme canonique (T, 3.2.2)

$$
(5. 4. 8. \mathbf {r})
$$

$$
\mathrm{H} ^ {1} (\mathrm{X}, \mathcal {O} _ {\mathrm{X}} ^ {*}) \rightarrow \mathrm{H} ^ {1} (\mathrm{Y}, \mathcal {O} _ {\mathrm{Y}} ^ {*}).
$$

Lorsqu'on identifie canoniquement (5.4.7) $\mathfrak{M}(\mathbf{X})$ et $\mathrm{H}^1 (\mathbf{X},\mathcal{O}_\mathrm{X}^*)$ (resp. $\mathfrak{M}(\mathbf{Y})$ et $\mathrm{H}^1 (\mathbf{Y},\mathcal{O}_\mathrm{Y}^*)$), l'homomorphisme (5.4.8.1) s'identifie à l'application $f^{*}$. En effet, si $\mathscr{L}$ provient d'un cocycle $(\varepsilon_{\lambda \mu})$ correspondant à un recouvrement ouvert $(\mathrm{U}_{\lambda})$ de X, il suffit de montrer que $f^{*}(\mathscr{L})$ provient d'un cocycle dont la classe de cohomologie est image par (5.4.8.1) de celle de $(\varepsilon_{\lambda \mu})$. Or, si $\theta_{\lambda \mu}$ est l'automorphisme de $\mathcal{O}_{\mathrm{X}}|(\mathrm{U}_{\lambda}\cap \mathrm{U}_{\mu})$ qui correspond à $\varepsilon_{\lambda \mu}$, il est clair que $f^{*}(\mathscr{L})$ s'obtient par recollement des $\mathcal{O}_{\mathrm{Y}}|\psi^{-1}(\mathrm{U}_{\lambda})$ au moyen des automorphismes $f^{*}(\theta_{\lambda \mu})$, et il suffit donc de vérifier que ces derniers correspondent au cocycle $(\omega^{\sharp}(\varepsilon_{\lambda \mu}))$, ce qui résulte aussitôt des définitions (on a identifié $\varepsilon_{\lambda \mu}$ à son image canonique par $\rho$ (3.7.2), section de $\psi^{*}(\mathcal{O}_{\mathrm{X}}^{*})$ au-dessus de $\psi^{-1}(\mathrm{U}_{\lambda}\cap \mathrm{U}_{\mu})$).

(5.4.9) Soient $\mathcal{E}$, $\mathcal{F}$ deux $\mathcal{O}_{\mathrm{X}}$-Modules, $\mathcal{F}$ étant supposé localement libre, et soit $\mathcal{G}$ un $\mathcal{O}_{\mathrm{X}}$-Module extension de $\mathcal{F}$ par $\mathcal{E}$, autrement dit tel qu'il existe une suite exacte $0 \to \mathcal{E} \xrightarrow{i} \mathcal{G} \xrightarrow{p} \mathcal{F} \to 0$. Alors, pour tout $x \in \mathrm{X}$, il existe un voisinage ouvert U de $x$ tel que $\mathcal{G}|U$ soit isomorphe à la somme directe $\mathcal{E}|U \oplus \mathcal{F}|U$. On peut en effet se borner au cas où $\mathcal{F} = \mathcal{O}_{\mathrm{X}}^{n}$; soient $e_{i} (1 \leqslant i \leqslant n)$ les sections canoniques (5.5.5) de $\mathcal{O}_{\mathrm{X}}^{n}$; il existe alors un voisinage ouvert U de $x$ et $n$ sections $s_{i}$ de $\mathcal{G}$ au-dessus de U telles que $p(s_{i}|U) = e_{i}|U$ pour $1 \leqslant i \leqslant n$. Cela étant, soit $f$ l'homomorphisme $\mathcal{F}|U \to \mathcal{G}|U$ défini par les sections $s_{i}|U$ (5.1.1). Il est immédiat que pour tout ouvert $V \subset U$, et toute section $s \in \Gamma(V, \mathcal{G})$ on a $s - f(p(s)) \in \Gamma(V, \mathcal{E})$, d'où notre assertion.

(5.4.10) Soient $f: \mathrm{X} \to \mathrm{Y}$ un morphisme d'espaces annelés, $\mathcal{F}$ un $\mathcal{O}_{\mathrm{X}}$-Module, $\mathcal{L}$ un $\mathcal{O}_{\mathrm{Y}}$-Module localement libre de rang fini. Il existe alors un isomorphisme canonique

$$
f _ {*} (\mathcal {F}) \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {L} \xrightarrow {\sim} f _ {*} (\mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{X}}} f ^ {*} (\mathcal {L}))\tag{5.4.10.1}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">p. 51</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Pour une forme générale de ce résultat, voir le livre cité dans la note de la p. 51.</span></small>

En effet, pour tout $\mathcal{O}_{\mathrm{Y}}$-Module $\mathscr{L}$, on a un homomorphisme canonique

$$
f _ {*} (\mathcal {F}) \otimes_ {\mathcal {O} _ {\mathrm{Y}}} \mathcal {L} \xrightarrow {1 \otimes \rho} f _ {*} (\mathcal {F}) \otimes_ {\mathcal {O} _ {\mathrm{Y}}} f _ {*} (f ^ {*} (\mathcal {L})) \xrightarrow {\alpha} f _ {*} (\mathcal {F} \otimes_ {\mathcal {O} _ {\mathrm{X}}} f ^ {*} (\mathcal {L}))
$$

$\rho$ étant l'homomorphisme (4.4.3.2) et $\alpha$ l'homomorphisme (4.2.2.1). Pour montrer que lorsque $\mathcal{L}$ est localement libre, cet homomorphisme est bijectif, il suffit, la question étant locale sur Y, de considérer le cas où $\mathcal{L} = \mathcal{O}_{\mathrm{Y}}^{n}$; en outre, $f_{*}$ et $f^{*}$ commutant aux sommes directes finies, on peut supposer $n = 1$, et dans ce cas la proposition résulte aussitôt des définitions et de la relation $f^{*}(\mathcal{O}_{\mathrm{Y}}) = \mathcal{O}_{\mathrm{X}}$.

## 5.5. Faisceaux sur un espace annelé en anneaux locaux.

(5.5.1) Nous dirons qu'un espace annelé (X, $\mathcal{O}_{\mathrm{X}}$) est un espace annelé en anneaux locaux si, pour tout $x \in \mathrm{X}$, $\mathcal{O}_x$ est un anneau local; ces espaces annelés seront de loin les plus fréquents de ceux qui seront considérés dans ce travail. Nous désignerons alors par $\mathfrak{m}_x$ l'idéal maximal de $\mathcal{O}_x$, par $\boldsymbol{k}(x)$ le corps résiduel $\mathcal{O}_x / \mathfrak{m}_x$; pour tout $\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{F}$, tout ouvert U de X, tout point $x \in \mathrm{U}$ et toute section $f \in \Gamma(\mathrm{U}, \mathcal{F})$, nous désignerons par $f(x)$ la classe du germe $f_x \in \mathcal{F}_x$ mod. $\mathfrak{m}_x \mathcal{F}_x$, et nous dirons que c'est la valeur de $f$ au point $x$. La relation $f(x) = 0$ signifie donc que $f_x \in \mathfrak{m}_x \mathcal{F}_x$; lorsqu'elle est remplie, on dira (par abus de langage) que $f$ s'annule en $x$. On aura soin de ne pas confondre cette relation avec $f_x = 0$.

(5.5.2) Soient X un espace annelé en anneaux locaux, $\mathcal{L}$ un $\mathcal{O}_{\mathrm{X}}$-Module inversible, $f$ une section de $\mathcal{L}$ au-dessus de X. Il y a alors équivalence entre les trois propriétés suivantes en un point $x \in \mathbf{X}$:

a) $f_{x}$ est un générateur de $\mathcal{L}_{x}$;

b) $f_{x} \notin \mathfrak{m}_{x} \mathcal{L}_{x}$ (autrement dit, $f(x) \neq 0$);

c) Il existe une section g de $\mathcal{L}^{-1}$ au-dessus d'un voisinage ouvert V de x telle que l'image canonique de $f\otimes g$ dans $\Gamma(\mathrm{V},\mathcal{O}_{\mathrm{X}})$ (5.4.3) soit la section unité.

En effet, la question étant locale, on peut se borner au cas où $\mathcal{L}=\mathcal{O}_{\mathrm{X}}$; l'équivalence de $a)$ et $b)$ est alors évidente, et il est clair que $c)$ entraîne $b)$. D'autre part, si $f_{x}\notin\mathfrak{m}_{x}$, $f_{x}$ est inversible dans $\mathcal{O}_{x}$, soit $f_{x}g_{x}=\mathrm{I}_{x}$. Par définition des germes de sections, cela veut dire qu'il existe un voisinage V de $x$ et une section $g$ de $\mathcal{O}_{\mathrm{X}}$ au-dessus de V telle que $fg=\mathrm{I}$ dans V, d'où $c)$.

Il résulte aussitôt de la condition $c)$ que l'ensemble $\mathbf{X}_{f}$ des $x$ vérifiant les conditions équivalentes $a), b), c)$ est ouvert dans $\mathbf{X}$; suivant la terminologie introduite dans (5.5.1), c'est l'ensemble des $x$ où $f$ ne s'annule pas.

(5.5.3) Sous les hypothèses de (5.5.2), soit $\mathcal{L}'$ un second $\mathcal{O}_{\mathrm{X}}$-Module invertible; alors, si $f \in \Gamma(\mathbf{X}, \mathcal{L})$, $g \in \Gamma(\mathbf{X}, \mathcal{L}')$, on a

$$
\mathrm{X} _ {f} \cap \mathrm{X} _ {g} = \mathrm{X} _ {f \otimes g}
$$

On se ramène en effet aussitôt au cas où $\mathcal{L}=\mathcal{L}'=\mathcal{O}_{\mathrm{X}}$ (la question étant locale); comme $f\otimes g$ s'identifie alors canoniquement au produit $fg$, la proposition est évidente.

$_{p}$  (5.5.4) Soit F un  $O_{X}$ -Module localement libre de rang n ; il est immédiat que  $\wedge F$  est un  $O_{X}$ -Module localement libre de rang  $\binom{n}{p}$  si  $p \leqslant n$ , réduit à o si p > n, car la question est locale et on est ramené au cas où  $F = O_{X}^{n}$ ; en outre, pour tout  $x \in X$ ,  $(\wedge^{p}F)_{x}/\mathfrak{m}_{x}(\wedge^{p}F)_{x}$  est un espace vectoriel de dimension  $\binom{n}{p}$  sur  $k(x)$ , qui s'identifie canoniquement à  $\wedge^{p}(\mathcal{F}_{x}/\mathfrak{m}_{x}\mathcal{F}_{x})$ . Soient  $s_{1}, \ldots, s_{p}$  des sections de F au-dessus d'un ouvert U de X, et soit  $s = s_{1} \wedge \ldots \wedge s_{p}$ , qui est une section de  $\wedge^{p}F$  au-dessus de U (4.1.5) ; on a  $s(x) = s_{1}(x) \wedge \ldots \wedge s_{p}(x)$ , et par suite, dire que  $s_{1}(x), \ldots, s_{p}(x)$  sont linéairement dépendants signifie que  $s(x) = 0$ . On en conclut que l'ensemble des  $x \in X$  tels que  $s_{1}(x), \ldots, s_{p}(x)$  soient linéairement indépendants est ouvert dans X : il suffit en effet, en se ramenant au cas où  $F = O_{X}^{n}$ , d'appliquer (5.5.2) à la section image de s par une des projections de  $\wedge^{p}F = O_{X}^{(n)}_{p}$  sur les  $(n_{p})$  facteurs.

En particulier, si $s_1, \ldots, s_n$ sont $n$ sections de $\mathcal{F}$ au-dessus de U telles que $s_1(x), \ldots, s_n(x)$ soient linéairement indépendantes en tout point $x \in \mathrm{U}$, l'homomorphisme $u: \mathcal{O}_\mathrm{X}^n | \mathrm{U} \to \mathcal{F} | \mathrm{U}$ défini par les $s_i$ (5.1.1) est un isomorphisme : on peut en effet se restreindre au cas où $\mathcal{F} = \mathcal{O}_\mathrm{X}^n$ et où on identifie canoniquement $\wedge \mathcal{F}$ et $\mathcal{O}_\mathrm{X}$; $s = s_1 \wedge \ldots \wedge s_n$ est alors une section de $\mathcal{O}_\mathrm{X}$ inversible au-dessus de U, et on définit un homomorphisme réciproque de $u$ au moyen des formules de Cramer.

(5.5.5) Soient $\mathcal{E}$, $\mathcal{F}$ deux $\mathcal{O}_{\mathrm{X}}$-Modules localement libres (de rang fini), et soit $u: \mathcal{E} \to \mathcal{F}$ un homomorphisme. Pour qu'il existe un voisinage $u$ de $x \in \mathrm{X}$ tel que $u|U$ soit injectif et que $\mathcal{F}|U$ soit somme directe de $u(\mathcal{E})|U$ et d'un sous-$(\mathcal{O}_{\mathrm{X}}|U)$-Module localement libre $\mathcal{G}$, il faut et il suffit que $u_x: \mathcal{E}_x \to \mathcal{F}_x$ donne, par passage aux quotients, un homomorphisme injectif d'espaces vectoriels $\mathcal{E}_x / \mathfrak{m}_x \mathcal{E}_x \to \mathcal{F}_x / \mathfrak{m}_x \mathcal{F}_x$. La condition est en effet nécessaire, car $\mathcal{F}_x$ est alors somme directe des $\mathcal{O}_x$-modules libres $u_x(\mathcal{E}_x)$ et $\mathcal{G}_x$, donc $\mathcal{F}_x / \mathfrak{m}_x \mathcal{F}_x$ est somme directe de $u_x(\mathcal{E}_x) / \mathfrak{m}_x u_x(\mathcal{E}_x)$ et de $\mathcal{G}_x / \mathfrak{m}_x \mathcal{G}_x$. La condition est suffisante, car on peut se borner au cas où $\mathcal{E} = \mathcal{O}_{\mathrm{X}}^m$; soient $s_1, \ldots, s_m$ les images par $u$ des sections $e_i$ de $\mathcal{O}_{\mathrm{X}}^m$ telles que $(e_i)_y$ soit égal au $i$-ème élément de la base canonique de $\mathcal{O}_y^m$ pour tout $y \in X$ (sections canoniques de $\mathcal{O}_{\mathrm{X}}^m$); par hypothèse $s_1(x), \ldots, s_m(x)$ sont linéairement indépendants, donc, si $\mathcal{F}$ est de rang $n$, il existe $n-m$ sections $s_{m+1}, \ldots, s_n$ de $\mathcal{F}$ au-dessus d'un voisinage $V$ de $x$ telles que les $s_i(x)$ ($1 \leqslant i \leqslant n$) forment une base de $\mathcal{F}_x / \mathfrak{m}_x \mathcal{F}_x$. Il existe alors (5.5.4) un voisinage $U \subset V$ de $x$ tel que les $s_i(y)$ ($1 \leqslant i \leqslant n$) forment une base de $\mathcal{F}_y / \mathfrak{m}_y \mathcal{F}_y$ pour tout $y \in V$, et on en conclut (5.5.4) qu'il y a un isomorphisme de $\mathcal{F}|U$ sur $\mathcal{O}_{\mathrm{X}}^n |U$, appliquant les $s_i|U$ ($1 \leqslant i \leqslant m$) sur les $e_i|U$, ce qui achève la démonstration.

## § 6. PLATITUDE

(6.0) La notion de platitude est due à J.-P. Serre [16] ; dans ce qui suit, on omet les démonstrations des résultats qui sont exposés dans l'Algèbre commutative de N. Bourbaki, à laquelle nous renvoyons le lecteur. Nous supposons tous les anneaux commutatifs (1).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Voir l'exposé cité de N. Bourbaki pour la généralisation de la plupart des résultats au cas non commutatif.</span></small>

Si M, N sont deux A-modules,  $M'$  (resp.  $N'$ ) un sous-module de M (resp. N), nous noterons  $\operatorname{Im}(\mathbf{M}'\otimes_{\mathbf{A}}\mathbf{N}')$  le sous-module de  $M\otimes_{A}N$ , image de l'application canonique  $M'\otimes_{A}N'\to M\otimes_{A}N$ .

## 6.1. Modules plats.

(6.1.1) Soit M un A-module. Les propriétés suivantes sont équivalentes :

a) Le foncteur $\mathbf{M} \otimes_{\mathbf{A}} \mathbf{N}$ en $\mathbf{N}$ est exact dans la catégorie des A-modules;

b) $\operatorname{Tor}_i^{\mathrm{A}}(\mathbf{M},\mathbf{N}) = 0$ pour tout $i > 0$ et tout A-module N;

c) $\mathrm{Tor}_1^{\mathrm{A}}(\mathbf{M},\mathbf{N}) = 0$ pour tout A-module N.

Lorsque M vérifie ces conditions, on dit que M est un A-module plat. Il est clair que tout A-module libre est plat.

Pour que M soit un A-module plat, il suffit que pour tout idéal J de A, de type fini, l'application canonique  $M \otimes_{A} J \to M \otimes_{A} A = M$  soit injective.

(6.1.2) Toute limite inductive de A-modules plats est un A-module plat. Pour qu'une somme directe $\bigoplus_{\lambda \in L} M_{\lambda}$ de A-modules soit un A-module plat, il faut et il suffit que chacun des A-modules $M_{\lambda}$ soit plat. En particulier, tout A-module projectif est plat.

Soit $o \to M' \to M \to M'' \to o$ une suite exacte de A-modules, telle que $M''$ soit plat. Alors, pour tout A-module N, la suite

$$
\mathrm{o} \rightarrow \mathrm{M} ^ {\prime} \otimes \mathrm{N} \rightarrow \mathrm{M} \otimes \mathrm{N} \rightarrow \mathrm{M} ^ {\prime \prime} \otimes \mathrm{N} \rightarrow \mathrm{o}
$$

est exacte. En outre, pour que M soit plat, il faut et il suffit alors que  $M'$  le soit (mais il peut se faire que M et  $M'$  soient plats sans que  $M'' = M/M'$  le soit).

(6.1.3) Soient M un A-module plat, N un A-module quelconque ; pour deux sous-modules N', N'' de N, on a alors

$$
\begin{array}{l} \operatorname{Im} (\mathbf {M} \otimes (\mathbf {N} ^ {\prime} + \mathbf {N} ^ {\prime \prime})) = \operatorname{Im} (\mathbf {M} \otimes \mathbf {N} ^ {\prime}) + \operatorname{Im} (\mathbf {M} \otimes \mathbf {N} ^ {\prime \prime}) \\ \operatorname{Im} (\mathbf {M} \otimes (\mathbf {N} ^ {\prime} \cap \mathbf {N} ^ {\prime \prime})) = \operatorname{Im} (\mathbf {M} \otimes \mathbf {N} ^ {\prime}) \cap \operatorname{Im} (\mathbf {M} \otimes \mathbf {N} ^ {\prime \prime}) \end{array}
$$

(images prises dans $\mathbf{M} \otimes \mathbf{N}$).

(6.1.4) Soient M, N deux A-modules,  $M'$  (resp.  $N'$ ) un sous-module de M (resp. N), et supposons que l'un des modules  $M/M'$ ,  $N/N'$  soit plat. Alors on a  $\operatorname{Im}(M'\otimes N') = \operatorname{Im}(M'\otimes N) \cap \operatorname{Im}(M \otimes N')$  (images dans  $M \otimes N$ ). En particulier, si J est un idéal de A et si  $M/M'$  est plat, on a  $JM' = M' \cap JM$ .

## 6.2. Changement d'anneaux.

Lorsqu'un groupe additif M est muni de plusieurs structures de module par rapport à des anneaux A, B, ..., au lieu de dire que M est plat en tant que A-module, B-module, ..., nous dirons parfois aussi que M est A-plat, B-plat, ...

(6.2.1) Soient A et B deux anneaux, M un A-module, N un (A, B)-bimodule. Si M est plat et si N est B-plat, alors  $M \otimes_{A} N$  est B-plat. En particulier, si M et N sont deux A-modules plats,  $M \otimes_{A} N$  est un A-module plat. Si B est une A-algèbre et si M est

un A-module plat, le B-module  $M_{(B)} = M \otimes_{A} B$  est plat. Enfin, si B est une A-algèbre qui est plate en tant que A-module, et si N est un B-module plat, alors N est aussi A-plat.

(6.2.2) Soient A un anneau, B une A-algèbre plate en tant que A-module. Soient M, N deux A-modules, tels que M admette une présentation finie ; alors l'homomorphisme canonique

$$
\operatorname{Hom} _ {\mathrm{A}} (\mathbf {M}, \mathbf {N}) \otimes_ {\mathrm{A}} \mathbf {B} \rightarrow \operatorname{Hom} _ {\mathrm{B}} (\mathbf {M} \otimes_ {\mathrm{A}} \mathbf {B}, \mathbf {N} \otimes_ {\mathrm{A}} \mathbf {B})\tag{6.2.2.1}
$$

(transformant $u\otimes b$ en l'homomorphisme $m\otimes b'\to u(m)\otimes b'b$) est un isomorphisme.

(6.2.3) Soit  $(\mathbf{A}_{\lambda}, \varphi_{\mu\lambda})$  un système inductif filtrant d'anneaux ; soit  $A = \varinjlim A_{\lambda}$ . Soit d'autre part, pour chaque  $\lambda$ ,  $M_{\lambda}$  un  $A_{\lambda}$ -module et pour  $\lambda \leqslant \mu$  soit  $\theta_{\mu\lambda}: M_{\lambda} \to M_{\mu}$  un  $\varphi_{\mu\lambda}$ -homomorphisme, tel que  $(\mathbf{M}_{\lambda}, \theta_{\mu\lambda})$  soit un système inductif;  $M = \varinjlim M_{\lambda}$  est alors un A-module. Cela étant, si pour tout  $\lambda$ ,  $M_{\lambda}$  est un  $A_{\lambda}$ -module plat, alors M est un A-module plat. En effet, soit J un idéal de type fini de A ; par définition de la limite inductive, il existe un indice  $\lambda$  et un idéal  $J_{\lambda}$  de  $A_{\lambda}$  tels que  $J = J_{\lambda}A$ . Si on pose  $J_{\mu}' = J_{\lambda}A_{\mu}$  pour  $\mu \geqslant \lambda$ , on a aussi  $J = \varinjlim J_{\mu}'$  (où  $\mu$  parcourt les indices  $\geqslant \lambda$ ), d'où (le foncteur lim étant exact et commutant au produit tensoriel)

$$
\mathbf {M} \otimes_ {\mathrm{A}} \mathfrak {J} = \varinjlim (\mathbf {M} _ {\mu} \otimes_ {\mathrm{A} _ {\mu}} \mathfrak {J} _ {\mu} ^ {\prime}) = \varinjlim \mathfrak {J} _ {\mu} ^ {\prime} \mathbf {M} _ {\mu} = \mathfrak {J} \mathbf {M}.
$$

## 6.3. Localisation de la platitude.

(6.3.1) Si A est un anneau, S une partie multiplicative de A,  $S^{-1}A$  est un A-module plat. En effet, pour tout A-module N,  $N \otimes_{A} S^{-1}A$  s'identifie à  $S^{-1}N$  (1.2.5) et on sait (1.3.2) que  $S^{-1}N$  est un foncteur exact en N.

Si maintenant M est un A-module plat,  $S^{-1}M=M\otimes_{A}S^{-1}A$  est un  $S^{-1}A$ -module plat (6.2.1), donc est aussi A-plat en vertu de ce qui précède et de (6.2.1). En particulier, si P est un  $S^{-1}A$ -module, on peut le considérer comme un A-module isomorphe à  $S^{-1}P$ ; pour que P soit A-plat, il faut et il suffit qu'il soit  $S^{-1}A$ -plat.

(6.3.2) Soient A un anneau, B une A-algèbre, T une partie multiplicative de B. Si P est un B-module qui est A-plat,  $T^{-1}P$  est A-plat. En effet, pour tout A-module N, on a  $(\mathrm{T}^{-1}\mathrm{P})\otimes_{\mathrm{A}}\mathrm{N}=(\mathrm{T}^{-1}\mathrm{B}\otimes_{\mathrm{B}}\mathrm{P})\otimes_{\mathrm{A}}\mathrm{N}=\mathrm{T}^{-1}\mathrm{B}\otimes_{\mathrm{B}}(\mathrm{P}\otimes_{\mathrm{A}}\mathrm{N})=\mathrm{T}^{-1}(\mathrm{P}\otimes_{\mathrm{A}}\mathrm{N})$ ; or,  $\mathrm{T}^{-1}(\mathrm{P}\otimes_{\mathrm{A}}\mathrm{N})$  est un foncteur exact en N, étant composé des deux foncteurs exacts  $P\otimes_{A}N$  (en N) et  $T^{-1}Q$  (en Q). Si S est une partie multiplicative de A dont l'image dans B est contenue dans T,  $T^{-1}P$  est égal à  $\mathrm{S}^{-1}(\mathrm{T}^{-1}\mathrm{P})$ , donc est aussi  $S^{-1}A$ -plat en vertu de (6.3.1).

(6.3.3) Soient $\varphi : A \to B$ un homomorphisme d'anneaux, M un B-module. Les propriétés suivantes sont équivalentes :

a) M est un A-module plat.

b) Pour tout idéal maximal n de B,  $M_{n}$  est un A-module plat.

c) Pour tout idéal maximal n de B, en posant  $\mathfrak{m}=\varphi^{-1}(\mathfrak{n})$ ,  $M_{n}$  est un  $A_{m}$ -module plat.

En effet, comme $\mathbf{M}_{\mathfrak{n}} = (\mathbf{M}_{\mathfrak{n}})_{\mathfrak{m}}$, l'équivalence de $b$ et $c$ résulte de (6.3.1), et le fait que $a$ entraîne $b$ est un cas particulier de (6.3.2). Reste à voir que $b$ entraîne $a$),

c'est-à-dire que, pour tout homomorphisme injectif $u: \mathbf{N}' \to \mathbf{N}$ de A-modules, l'homomorphisme $v = \mathrm{i} \otimes u: \mathbf{M} \otimes_{\mathbf{A}} \mathbf{N}' \to \mathbf{M} \otimes_{\mathbf{A}} \mathbf{N}$ est injectif. Or, $v$ est aussi un homomorphisme de B-modules, et on sait que pour qu'il soit injectif, il suffit que pour tout idéal maximal $n$ de B, $v_n: (\mathbf{M} \otimes_{\mathbf{A}} \mathbf{N}')_n \to (\mathbf{M} \otimes_{\mathbf{A}} \mathbf{N})_n$ soit injectif. Mais comme

$$
(\mathbf {M} \otimes_ {\mathbf {A}} \mathbf {N}) _ {n} = \mathbf {B} _ {n} \otimes_ {\mathbf {B}} (\mathbf {M} \otimes_ {\mathbf {A}} \mathbf {N}) = \mathbf {M} _ {n} \otimes_ {\mathbf {A}} \mathbf {N},
$$

$v_{n}$ n'est autre que l'homomorphisme $\mathbf{r} \otimes u : \mathbf{M}_{\mathfrak{n}} \otimes_{\mathbf{A}} \mathbf{N}' \to \mathbf{M}_{\mathfrak{n}} \otimes_{\mathbf{A}} \mathbf{N}$, qui est injectif puisque $\mathbf{M}_{\mathfrak{n}}$ est A-plat.

En particulier (en faisant B=A), pour qu'un A-module M soit plat, il faut et il suffit que  $M_{m}$  soit  $A_{m}$ -plat pour tout idéal maximal m de A.

(6.3.4) Soit M un A-module ; si M est plat, et si  $f \in A$  n'est pas diviseur de o dans A, f n'annule aucun élément ≠o de M, car l'homomorphisme  $m \to f.m$  s'écrit  $1 \otimes u$ , où u est la multiplication  $a \to f.a$  dans A et M est identifié à  $M \otimes_{A} A$ ; si u est injective, il en est donc de même de  $1 \otimes u$  puisque M est plat. En particulier, si A est intègre, M est sans torsion.

Inversement, supposons A intègre, M sans torsion, et supposons que pour tout idéal maximal m de A,  $A_{m}$  soit un anneau de valuation discrète; alors M est A-plat. Il suffit en effet (6.3.3) de prouver que  $M_{m}$  est  $A_{m}$ -plat, et on peut donc supposer que A est déjà un anneau de valuation discrète. Mais comme M est limite inductive de ses sous-modules de type fini, et que ces derniers sont sans torsion, on peut en outre se borner au cas où M est de type fini (6.1.2). La proposition résulte dans ce cas de ce que M est un A-module libre.

En particulier, si A est un anneau intègre, $\varphi: A \to B$ un homomorphisme d'anneaux faisant de B un A-module plat et $+ \{o\}$, $\varphi$ est nécessairement injectif. Inversement, si B est intègre, A un sous-anneau de B et si pour tout idéal maximal $m$ de A, $A_m$ est un anneau de valuation discrète, B est A-plat.

## 6.4. Modules fidèlement plats.

(6.4.1) Pour un A-module M, les quatre propriétés suivantes sont équivalentes :

a) Pour qu'une suite  $N^{\prime}\rightarrow N\rightarrow N^{\prime\prime}$  de A-modules soit exacte, il faut et il suffit que la suite  $M\otimes N^{\prime}\rightarrow M\otimes N\rightarrow M\otimes N^{\prime\prime}$  soit exacte;

b) M est plat et pour tout A-module N, la relation  $M \otimes N = o$  entraîne N = o;

c) M est plat et pour tout homomorphisme $v: \mathbf{N} \to \mathbf{N}'$ de A-modules, la relation $\mathrm{I}_{\mathbf{M}} \otimes v = 0$ entraîne $v = 0$, $\mathrm{I}_{\mathbf{M}}$ étant l'automorphisme identique de M;

d) M est plat et pour tout idéal maximal m de A, mM≠M.

Lorsque M vérifie ces conditions, on dit que M est un A-module fidèlement plat ; M est alors nécessairement un module fidèle. En outre, si $u: \mathbf{N} \to \mathbf{N}'$ est un homomorphisme de A-modules, pour que $u$ soit injectif (resp. surjectif, bijectif), il faut et il suffit que $\mathbf{I} \otimes u: \mathbf{M} \otimes \mathbf{N} \to \mathbf{M} \otimes \mathbf{N}'$ le soit.

(6.4.2) Un module libre  $\neq\{o\}$  est fidèlement plat ; il en est de même de la somme directe d'un module plat et d'un module fidèlement plat. Si S est une partie multiplicative de A,  $S^{-1}A$  n'est un A-module fidèlement plat que si S est formé d'éléments inversibles (donc  $S^{-1}A=A$ ).

(6.4.3) Soit $o \to M' \to M \to M'' \to o$ une suite exacte de A-modules ; si $M'$ et $M''$ sont plats, et si l'un d'eux est fidèlement plat, alors $M$ est fidèlement plat.

(6.4.4) Soient A et B deux anneaux, M un A-module, N un (A, B)-bimodule. Si M est fidèlement plat et si N est un B-module fidèlement plat, alors  $M \otimes_{A} N$  est un B-module fidèlement plat. En particulier, si M et N sont deux A-modules fidèlement plats, il en est de même de  $M \otimes_{A} N$ . Si B est une A-algèbre et si M est un A-module fidèlement plat, le B-module  $M_{(B)}$  est fidèlement plat.

(6.4.5) Si M est un A-module fidèlement plat et si S est une partie multiplicative de A,  $S^{-1}M$  est un  $S^{-1}A$ -module fidèlement plat, puisque  $S^{-1}M = M \otimes_{A} (S^{-1}A)$  (6.4.4). Inversement, si pour tout idéal maximal m de A,  $M_{m}$  est un  $A_{m}$ -module fidèlement plat, M est un A-module fidèlement plat, car M est A-plat (6.3.3), et on a

$$
\mathrm{M} _ {\mathfrak {m}} / \mathfrak {m} \mathrm{M} _ {\mathfrak {m}} = (\mathrm{M} \otimes_ {\mathrm{A}} \mathrm{A} _ {\mathfrak {m}}) \otimes_ {\mathrm{A} _ {\mathfrak {m}}} (\mathrm{A} _ {\mathfrak {m}} / \mathfrak {m} \mathrm{A} _ {\mathfrak {m}}) = \mathrm{M} \otimes_ {\mathrm{A}} (\mathrm{A} / \mathfrak {m}) = \mathrm{M} / \mathfrak {m} \mathrm{M}
$$

donc l'hypothèse entraîne que M/mM≠o pour tout idéal maximal m de A, ce qui prouve notre assertion (6.4.1).

## 6.5. Restriction des scalaires.

(6.5.1) Soient A un anneau, $\varphi: A \to B$ un homomorphisme d'anneaux faisant de B une A-algèbre. Supposons qu'il existe un B-module N qui soit un A-module fidèlement plat. Alors, pour tout A-module M, l'homomorphisme $x \to 1 \otimes x$ de M dans $\mathbf{B} \otimes_{\mathbf{A}} \mathbf{M} = \mathbf{M}_{(\mathbf{B})}$ est injectif. En particulier, $\varphi$ est injectif; pour tout idéal a de A, on a $\varphi^{-1}(\mathfrak{aB}) = \mathfrak{a}$; pour tout idéal maximal (resp. premier) m de A, il existe un idéal maximal (resp. premier) n de B tel que $\varphi^{-1}(n) = m$.

(6.5.2) Lorsque la condition de (6.5.1) est remplie, on identifie A à un sous-anneau de B par $\varphi$ et plus généralement, pour tout A-module M, on identifie M à un sous-A-module de $\mathbf{M}_{(\mathbf{B})}$. On notera que si B est alors noethérien, il en est de même de A, car l'application $a \to aB$ est une injection croissante de l'ensemble des idéaux de A dans l'ensemble des idéaux de B ; l'existence d'une suite infinie strictement croissante d'idéaux de A entraînerait donc l'existence d'une suite analogue d'idéaux de B.

## 6.6. Anneaux fidèlement plats.

(6.6.1) Soit $\varphi: A \to B$ un homomorphisme d'anneaux faisant de B une A-algèbre. Les cinq propriétés suivantes sont équivalentes :

a) B est un A-module fidèlement plat (autrement dit,  $M_{(B)}$  est un foncteur exact et fidèle en M).

b) L'homomorphisme $\varphi$ est injectif et le A-module B/$\varphi$(A) est plat.

c) Le A-module B est plat (autrement dit, le foncteur  $M_{(B)}$  est exact), et pour tout A-module M, l'homomorphisme  $x \to 1 \otimes x$  de M dans  $M_{(B)}$  est injectif.

d) Le A-module B est plat et pour tout idéal a de A, on a $\varphi^{-1}(\mathfrak{aB}) = \mathfrak{a}$.

e) Le A-module B est plat et pour tout idéal maximal m de A, il existe un idéal maximal n de B tel que  $\varphi^{-1}(n)=m$ .

Lorsque ces conditions ont lieu, on identifie A à un sous-anneau de B.

(6.6.2) Soient A un anneau local, m son idéal maximal, B une A-algèbre telle que  $mB \neq B$  (ce qui a lieu par exemple lorsque B est un anneau local et  $A \rightarrow B$  un homomorphisme local). Si B est un A-module plat, B est un A-module fidèlement plat. En effet, comme  $mB \neq B$ , il y a un idéal maximal n de B contenant mB; comme  $\varphi^{-1}(n) \cap A$  contient m et ne contient pas i, on a  $\varphi^{-1}(n) = m$  et le critère e) de (6.6.1) s'applique. Sous les conditions indiquées, on voit donc que si B est noethérien, il en est de même de A (6.5.2).

(6.6.3) Soit B une A-algèbre qui est un A-module fidèlement plat. Pour tout A-module M et tout sous-A-module M' de M, on a (en identifiant M à un sous-A-module de  $\mathbf{M}_{(\mathrm{B})}$ )  $M' = M \cap M'_{(\mathrm{B})}$ . Pour que M soit un A-module plat (resp. fidèlement plat), il faut et il suffit que  $\mathbf{M}_{(\mathrm{B})}$  soit un B-module plat (resp. fidèlement plat).

(6.6.4) Soient B une A-algèbre, N un B-module fidèlement plat. Pour que B soit un A-module plat (resp. fidèlement plat), il faut et il suffit que N le soit.

En particulier, soit C une B-algèbre ; si l'anneau C est fidèlement plat sur B et B fidèlement plat sur A, alors C est fidèlement plat sur A ; si C est fidèlement plat sur B et sur A, alors B est fidèlement plat sur A.

## 6.7. Morphismes plats d'espaces annelés.

(6.7.1) Soit $f: \mathrm{X} \to \mathrm{Y}$ un morphisme d'espaces annelés, et soit $\mathcal{F}$ un $\mathcal{O}_{\mathrm{X}}$-Module. On dit que $\mathcal{F}$ est $f$-plat (ou Y-plat lorsque aucune confusion n'est à craindre sur $f$) en un point $x \in \mathrm{X}$ si $\mathcal{F}_x$ est un $\mathcal{O}_{f(x)}$-module plat; on dit que $\mathcal{F}$ est $f$-plat au-dessus de $y \in \mathrm{Y}$ si $\mathcal{F}$ est $f$-plat en tous les points $x \in f^{-1}(y)$; on dit que $\mathcal{F}$ est $f$-plat si $\mathcal{F}$ est $f$-plat en tous les points de X. On dit que le morphisme $f$ est plat en $x \in \mathrm{X}$ (resp. plat au-dessus de $y \in \mathrm{Y}$, resp. plat) si $\mathcal{O}_{\mathrm{X}}$ est $f$-plat en $x$ (resp. $f$-plat au-dessus de $y$, resp. $f$-plat).

(6.7.2) Avec les notations de (6.7.1), si $\mathcal{F}$ est $f$-plat en $x$, pour tout voisinage ouvert U de $y=f(x)$, le foncteur $(f^{*}(\mathcal{G})\otimes_{\mathcal{O}_{X}}\mathcal{F})_{x}$ en $\mathcal{G}$ est exact dans la catégorie des $(\mathcal{O}_{Y}|U)$-Modules; en effet, cette fibre s'identifie canoniquement à $\mathcal{G}_{y}\otimes_{\mathcal{O}_{y}}\mathcal{F}_{x}$, et notre assertion résulte de la définition. En particulier, si $f$ est un morphisme plat, le foncteur $f^{*}$ est exact dans la catégorie des $\mathcal{O}_{Y}$-Modules.

(6.7.3) Inversement, supposons le faisceau d'anneaux $\mathcal{O}_{\mathrm{Y}}$ cohérent, et supposons que pour tout voisinage ouvert U de $y$, le foncteur $(f^{*}(\mathcal{G})\otimes_{\mathcal{O}_{\mathrm{X}}}\mathcal{F})_{x}$ soit exact en $\mathcal{G}$ dans la catégorie des $(\mathcal{O}_{\mathrm{Y}}|\mathrm{U})$-Modules cohérents. Alors $\mathcal{F}$ est $f$-plat en $x$. En effet, il suffit de prouver que pour tout idéal de type fini $\mathfrak{J}$ de $\mathcal{O}_{y}$, l'homomorphisme canonique $\mathfrak{J}\otimes_{\mathcal{O}_{y}}\mathcal{F}_{x}\to\mathcal{F}_{x}$ est injectif (6.1.1). Or, on sait (5.3.8) qu'il existe alors un voisinage

ouvert U de y et un faisceau cohérent d'idéaux J de  $O_{Y}|U$  tel que  $J_{y}=J$ , d'où la conclusion.

(6.7.4) Les résultats de (6.1) sur les modules plats se transcrivent aussitôt en propositions sur les faisceaux f-plats en un point :

Si $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ est une suite exacte de $\mathcal{O}_{\mathrm{X}}$-Modules et si $\mathcal{F}''$ est $f$-plat au point $x \in \mathbf{X}$, alors, pour tout voisinage ouvert U de $y = f(x)$ et tout $(\mathcal{O}_{\mathrm{Y}}|\mathrm{U})$-Module $\mathcal{G}$, la suite

$$
0 \rightarrow (f ^ {*} (\mathcal {G}) \otimes_ {\mathcal {O} _ {\mathrm{X}}} \mathcal {F} ^ {\prime}) _ {x} \rightarrow (f ^ {*} (\mathcal {G}) \otimes_ {\mathcal {O} _ {\mathrm{X}}} \mathcal {F}) _ {x} \rightarrow (f ^ {*} (\mathcal {G}) \otimes_ {\mathcal {O} _ {\mathrm{X}}} \mathcal {F} ^ {\prime \prime}) _ {x} \rightarrow 0
$$

est exacte. Pour que $\mathcal{F}$ soit $f$-plat en $x$, il faut et il suffit alors que $\mathcal{F}'$ le soit. On a des énoncés analogues pour les notions correspondantes de $\mathcal{O}_{\mathrm{X}}$-Module $f$-plat au-dessus de $y \in \mathrm{Y}$, ou de $\mathcal{O}_{\mathrm{X}}$-Module $f$-plat.

(6.7.5) Soient $f: \mathrm{X} \to \mathrm{Y}$, $g: \mathrm{Y} \to \mathrm{Z}$ deux morphismes d'espaces annelés; soient $x \in \mathrm{X}$, $y = f(x)$, $\mathcal{F}$ un $\mathcal{O}_{\mathrm{X}}$-Module. Si $\mathcal{F}$ est $f$-plat au point $x$ et si le morphisme $g$ est plat au point $y$, alors $\mathcal{F}$ est $(g \circ f)$-plat en $x$ (6.2.1). En particulier, si $f$ et $g$ sont des morphismes plats, $g \circ f$ est plat.

(6.7.6) Soient X, Y deux espaces annelés, $f: \mathrm{X} \to \mathrm{Y}$ un morphisme plat. Alors l'homomorphisme canonique de bifoncteurs (4.4.6)

$$
f ^ {*} (\mathcal {H} o m _ {\mathcal {O} _ {\mathrm{Y}}} (\mathcal {F}, \mathcal {G})) \rightarrow \mathcal {H} o m _ {\mathcal {O} _ {\mathrm{X}}} (f ^ {*} (\mathcal {F}), f ^ {*} (\mathcal {G}))\tag{6.7.6.x}
$$

est un isomorphisme lorsque $\mathcal{F}$ admet une présentation finie (5.2.5).

En effet, la question étant locale, on peut supposer qu'il existe une suite exacte $\mathcal{O}_{\mathrm{Y}}^{m}\to\mathcal{O}_{\mathrm{Y}}^{n}\to\mathcal{F}\to0$. Or, les deux membres de (6.7.6.1) sont des foncteurs exacts à gauche en $\mathcal{F}$ en vertu de l'hypothèse sur $f$; on est alors ramené à démontrer la proposition lorsque $\mathcal{F}=\mathcal{O}_{\mathrm{Y}}$, cas où elle est triviale.

(6.7.8) On dit qu'un morphisme $f: \mathbf{X} \to \mathbf{Y}$ d'espaces annelés est fidèlement plat si $f$ est surjectif et si, pour tout $x \in \mathbf{X}$, $\mathcal{O}_x$ est un $\mathcal{O}_{f(x)}$-module fidèlement plat. Lorsque X et Y sont des espaces annelés en anneaux locaux (5.5.1), il revient au même de dire que le morphisme $f$ est surjectif et plat (6.6.2). Lorsque $f$ est fidèlement plat, $f^*$ est un foncteur exact et fidèle dans la catégorie des $\mathcal{O}_{\mathrm{Y}}$-Modules (6.6.1, a)) et pour qu'un $\mathcal{O}_{\mathrm{Y}}$-Module $\mathcal{G}$ soit Y-plat, il faut et il suffit que $f^*(\mathcal{G})$ le soit (6.6.3).

## § 7. ANNEAUX ADIQUES

## 7.1. Anneaux admissibles.

(7.1.1) Rappelons que dans un anneau topologique A (non nécessairement séparé), on dit qu'un élément $x$ est topologiquement nilpotent si o est une limite de la suite $(x^n)_{n\geqslant 0}$. On dit qu'un anneau topologique A est linéairement topologisé s'il existe un système fondamental de voisinages de o dans A formé d'idéaux (nécessairement ouverts).

Définition (7.1.2). — Dans un anneau linéairement topologisé A, on dit qu'un idéal J est un idéal de définition si J est ouvert et si, pour tout voisinage V de o, il existe un entier n > o tel

que $\mathfrak{J}^{n}\subset V$ (ce qu'on exprime, par abus de langage, en disant que la suite $(\mathfrak{J}^{n})$ tend vers o). On dit qu'un anneau linéairement topologisé A est préadmissible s'il existe dans A un idéal de définition; on dit que A est admissible s'il est préadmissible et si en outre il est séparé et complet.

Il est clair que si J est un idéal de définition, L un idéal ouvert de A, J∩L est encore un idéal de définition ; les idéaux de définition d'un anneau préadmissible A forment donc un système fondamental de voisinages de o.

Lemme (7.1.3). — Soit A un anneau linéairement topologisé.

(i) Pour que $x \in A$ soit topologiquement nilpotent, il faut et il suffit que pour tout idéal ouvert $\mathfrak{I}$ de $A$, l'image canonique de $x$ dans $A / \mathfrak{I}$ soit nilpotente. L'ensemble $\mathfrak{I}$ des éléments topologiquement nilpotents de $A$ est un idéal.

(ii) Supposons en outre que A soit préadmissible, et soit J un idéal de définition de A. Pour que  $x \in A$  soit topologiquement nilpotent, il faut et il suffit que son image canonique dans A/J soit nilpotente ; l'idéal J est l'image réciproque du nilradical de A/J et est donc ouvert.

(i) découle immédiatement des définitions. Pour prouver (ii), il suffit de remarquer que pour tout voisinage V de o dans A, il existe n>0 tel que  $J^{n}\subset V$ ; si  $x\in A$  est tel que  $x^{m}\in J$ , on a  $x^{mq}\in V$  pour  $q\geqslant n$ , donc x est topologiquement nilpotent.

Proposition (7.1.4). — Soient A un anneau préadmissible, J un idéal de définition de A.

(i) Pour qu'un idéal $\mathfrak{J}'$ de A soit contenu dans un idéal de définition, il faut et il suffit qu'il existe un entier $n > 0$ tel que $\mathfrak{J}'^n \subset \mathfrak{J}$.

(ii) Pour qu'un  $x \in A$  soit contenu dans un idéal de définition, il faut et il suffit qu'il soit topologiquement nilpotent.

(i) Si $\mathfrak{J}^{\prime n}\subset\mathfrak{J}$, pour tout voisinage ouvert V de o dans A, il existe $m$ tel que $\mathfrak{J}^{m}\subset V$, donc $\mathfrak{J}^{\prime mn}\subset V$.

(ii) La condition est évidemment nécessaire ; elle est suffisante, car si elle est remplie, il existe n tel que  $x^{n} \in J$ , donc  $J' = J + Ax$  est un idéal de définition, puisqu'il est ouvert, et que  $J'^{n} \subset J$ .

Corollaire (7.1.5). — Dans un anneau préadmissible A, un idéal premier ouvert contient tous les idéaux de définition.

Corollaire (7.1.6). — Les notations et hypothèses étant celles de (7.1.4), les propriétés suivantes d'un idéal $\mathfrak{J}_{0}$ de A sont équivalentes :

a) $\mathfrak{J}_0$ est le plus grand idéal de définition de A;

b) $\mathfrak{J}_0$ est un idéal de définition maximal;

c) $\mathfrak{J}_{0}$ est un idéal de définition tel que l'anneau A/$\mathfrak{J}_{0}$ soit réduit.

Pour qu'il existe un idéal $\mathfrak{J}_{0}$ ayant ces propriétés, il faut et il suffit que le nilradical de A/$\mathfrak{J}$ soit nilpotent ; $\mathfrak{J}_{0}$ est alors égal à l'idéal $\mathfrak{T}$ des éléments topologiquement nilpotents de A.

Il est clair que $a)$ implique $b)$, et $b)$ implique $c)$ en vertu de (7.1.4, (ii)) et (7.1.3, (ii)); pour la même raison, $c)$ entraîne $a)$. La dernière assertion résulte de (7.1.4, (i)) et (7.1.3, (ii)).

Lorsque $\mathfrak{T}/\mathfrak{J}$, nilradical de A/$\mathfrak{J}$, est nilpotent, on note A$_{\text{red}}$ l'anneau quotient (réduit) A/$\mathfrak{T}$.

Corollaire (7.1.7). — Un anneau préadmissible noethérien admet un plus grand idéal de définition.

Corollaire (7.1.8). — Si un anneau préadmissible A est tel que, pour un idéal de définition J, les puissances $\mathfrak{J}^{n}$ ($n > 0$) forment un système fondamental de voisinages de o, il en est de même des puissances $\mathfrak{J}^{\prime n}$ de tout idéal de définition J' de A.

Définition (7.1.9). — On dit qu'un anneau préadmissible A est préadique s'il existe un idéal de définition $\mathfrak{I}$ de A tel que les $\mathfrak{I}^n$ forment un système fondamental de voisinages de o dans A (ou, ce qui revient au même, tel que les $\mathfrak{I}^n$ soient ouverts). On appelle anneau adique un anneau préadique séparé et complet.

Si J est un idéal de définition d'un anneau préadique (resp. adique) A, on dit encore que A est un anneau J-préadique (resp. J-adique), et que sa topologie est la topologie J-préadique (resp. J-adique). Plus généralement, si M est un A-module, la topologie sur M ayant pour système fondamental de voisinages de o les sous-modules J$^{n}$M est dite topologie J-préadique (resp. J-adique). En vertu de (7.1.8), ces topologies sont indépendantes du choix de l'idéal de définition J.

Proposition (7.1.10). — Soient A un anneau admissible, J un idéal de définition de A. Alors J est contenu dans le radical de A.

Cet énoncé est équivalent à l'un quelconque des corollaires suivants :

Corollaire (7.1.11). — Pour tout $x \in \mathfrak{J}$, $\mathrm{i} + x$ est inversible dans A.

Corollaire (7.1.12). — Pour que $f\in\mathbf{A}$ soit inversible dans $\mathbf{A}$, il faut et il suffit que son image canonique dans $\mathbf{A}/\mathfrak{J}$ soit inversible dans $\mathbf{A}/\mathfrak{J}$.

Corollaire (7.1.13). — Pour tout A-module M de type fini, la relation  $M = J M$  (équivalente à  $M \otimes_{A} (A / J) = 0$ ) entraîne M = 0.

Corollaire (7.1.14). — Soit $u: \mathbf{M} \to \mathbf{N}$ un homomorphisme de A-modules, N étant de type fini ; pour que u soit surjectif, il faut et il suffit que $u \otimes \mathrm{I}: \mathbf{M} \otimes_{\mathrm{A}} (\mathrm{A} / \mathfrak{J}) \to \mathrm{N} \otimes_{\mathrm{A}} (\mathrm{A} / \mathfrak{J})$ le soit.

En effet, l'équivalence de (7.1.10) et (7.1.11) résulte de Bourbaki, Alg., chap. VIII, § 6, n° 3, th. 1, et celle de (7.1.10) et (7.1.13) de loc. cit., th. 2 ; le fait que (7.1.10) entraîne (7.1.14) résulte de loc. cit., cor. 4 de la prop. 6 ; d'autre part, (7.1.14) entraîne (7.1.13) en l'appliquant à l'homomorphisme nul. Enfin, (7.1.10) entraîne que si f est inversible dans A/J, f n'est contenu dans aucun idéal maximal de A, donc f est inversible dans A, autrement dit (7.1.10) entraîne (7.1.12) ; et inversement, (7.1.12) entraîne (7.1.11).

Tout revient donc à démontrer (7.1.11). Or, comme A est séparé et complet et que la suite $(\mathfrak{J}^n)$ tend vers o, il est immédiat que la série $\sum_{n=0}^{\infty} (-1)^n x^n$ est convergente dans A et que, si $y$ est sa somme, on a $y(1+x)=1$.

## 7.2. Anneaux adiques et limites projectives.

(7.2.1) Toute limite projective d'anneaux discrets est évidemment un anneau linéairement topologisé, séparé et complet. Inversement, soit A un anneau linéairement topologisé, et soit  $(\mathfrak{J}_{\lambda})$  un système fondamental de voisinages ouverts de o dans A formé

d'idéaux. Les applications canoniques $\varphi_{\lambda}: A \to A / \mathfrak{J}_{\lambda}$ forment un système projectif de représentations continues et définissent donc une représentation continue $\varphi: A \to \varprojlim A / \mathfrak{J}_{\lambda}$; si $A$ est séparé, $\varphi$ est un isomorphisme topologique de $A$ sur un sous-anneau partout dense de $\varprojlim A / \mathfrak{J}_{\lambda}$; si, en outre, $A$ est complet, $\varphi$ est un isomorphisme topologique de $A$ sur $\varprojlim A / \mathfrak{J}_{\lambda}$.

Lemme (7.2.2). — Pour qu'un anneau linéairement topologisé soit admissible, il faut et il suffit qu'il soit isomorphe à une limite projective  $A = \varprojlim A_{\lambda}$ , où  $(\mathrm{A}_{\lambda}, u_{\lambda\mu})$  est un système projectif d'anneaux discrets ayant pour ensemble d'indices un ensemble ordonné filtrant L (pour ≤) qui admet un plus petit élément noté o et satisfait aux conditions suivantes :  $1^{0}$  les  $u_{\lambda}: A \to A_{\lambda}$  sont surjectifs ;  $2^{0}$  le noyau  $J_{\lambda}$  de  $u_{0\lambda}: A_{\lambda} \to A_{0}$  est nilpotent. Lorsqu'il en est ainsi, le noyau J de  $u_{0}: A \to A_{0}$  est égal à lim  $J_{\lambda}$ .

La nécessité de la condition résulte de (7.2.1), en prenant pour $(\mathfrak{J}_{\lambda})$ un système fondamental de voisinages de o formé d'idéaux de définition contenus dans l'un d'eux $\mathfrak{J}_0$ et appliquant (7.1.4, (i)). La réciproque résulte de la définition d'une limite projective et de (7.1.2), et la dernière assertion est immédiate.

(7.2.3) Soient A un anneau topologique admissible, $\mathfrak{J}$ un idéal de A contenu dans un idéal de définition (autrement dit (7.1.4) tel que $(\mathfrak{J}^n)$ tende vers o); on peut considérer sur A la topologie d'anneau ayant pour système fondamental de voisinages de o les puissances $\mathfrak{J}^n$ ($n > 0$); nous l'appellerons encore la topologie $\mathfrak{J}$-préadique. L'hypothèse que A est admissible entraîne que $\bigcap_{n} \mathfrak{J}^n = 0$, donc la topologie $\mathfrak{J}$-préadique sur A est séparée; soit $\hat{\mathrm{A}} = \varprojlim \mathrm{A} / \mathfrak{J}^n$ le complété de A pour cette topologie (où les $\mathrm{A} / \mathfrak{J}^n$ sont munis de la topologie discrète), et désignons par $u$ l'homomorphisme d'anneaux $\mathrm{A} \to \hat{\mathrm{A}}$ (non nécessairement continu), limite projective de la suite d'homomorphismes $u_n: \mathrm{A} \to \mathrm{A} / \mathfrak{J}^n$. D'autre part, la topologie $\mathfrak{J}$-préadique sur A est plus fine que la topologie donnée $\mathcal{T}$ sur A; comme A est séparé et complet pour $\mathcal{T}$, on peut prolonger par continuité l'application identique de A (muni de la topologie $\mathfrak{J}$-préadique) dans A muni de $\mathcal{T}$; cela donne une représentation continue $v: \hat{\mathrm{A}} \to \mathrm{A}$.

Proposition (7.2.4). — Si A est un anneau admissible et J est contenu dans un idéal de définition de A, A est séparé et complet pour la topologie J-préadique.

En effet, avec les notations de (7.2.3), il est immédiat que $v\circ u$ est l'application identique de A. D'autre part, $u_{n}\circ v:\hat{\mathrm{A}}\to \mathrm{A} / \mathfrak{J}^{n}$ est le prolongement par continuité (pour la topologie $\mathfrak{J}$-préadique sur A et la topologie discrète sur $\mathrm{A} / \mathfrak{J}^n$) de l'application canonique $u_{n}$; autrement dit, c'est l'application canonique de $\hat{\mathrm{A}} = \varprojlim_{k}\mathrm{A} / \mathfrak{J}^{k}$ sur $\mathrm{A} / \mathfrak{J}^{n}$; $u\circ v$ est donc limite projective de cette suite d'applications, c'est-à-dire par définition l'application identique de $\hat{\mathrm{A}}$; ceci démontre la proposition.

Corollaire (7.2.5). — Sous les hypothèses de (7.2.3), les conditions suivantes sont équivalentes :

a) L'homomorphisme u est continu ;

b) L'homomorphisme v est bicontinu ;

c) A est un anneau ℑ-adique.

Corollaire (7.2.6). — Soient A un anneau admissible, $\mathfrak{J}$ un idéal de définition de A. Pour que A soit noethérien, il faut et il suffit que A/$\mathfrak{J}$ soit noethérien et que $\mathfrak{J}/\mathfrak{J}^2$ soit un (A/$\mathfrak{J}$)-module de type fini.

Ces conditions sont évidemment nécessaires. Inversement, supposons-les vérifiées ; comme en vertu de (7.2.4) A est complet pour la topologie $\mathfrak{J}$-préadique, pour qu'il soit noethérien, il faut et il suffit que l'anneau gradué associé grad(A) (pour la filtration des $\mathfrak{J}^n$) le soit ([1], p. 18-07, th. 4). Or, soient $a_1, \ldots, a_n$ des éléments de $\mathfrak{J}$ dont les classes mod. $\mathfrak{J}^2$ sont des générateurs de $\mathfrak{J}/\mathfrak{J}^2$ en tant que A/$\mathfrak{J}$-module. Il est immédiat par récurrence que les classes mod. $\mathfrak{J}^{m+1}$ des monômes de degré total $m$ en les $a_i$ ($i \leqslant i \leqslant n$) forment un système de générateurs du (A/$\mathfrak{J}$)-module $\mathfrak{J}^m/\mathfrak{J}^{m+1}$. On en conclut que grad(A) est un anneau isomorphe à un quotient de (A/$\mathfrak{J}$)[T$_1$, ..., T$_n$] (T$_i$ indéterminées), ce qui achève la démonstration.

Proposition (7.2.7). — Soit  $(\mathbf{A}_{i}, u_{ij})$  un système projectif  $(i \in \mathbf{N})$  d'anneaux discrets, et pour tout entier i, soit  $J_{i}$  le noyau dans  $A_{i}$  de l'homomorphisme  $u_{0i}: A_{i} \to A_{0}$ . On suppose que :

a) Pour $i \leqslant j$, $u_{ij}$ est surjectif et son noyau est $\mathfrak{J}_j^{i+1}$ (donc $\mathrm{A}_i$ est isomorphe à $\mathrm{A}_j / \mathfrak{J}_j^{i+1}$).

b) $\mathfrak{J}_1 / \mathfrak{J}_1^2 (= \mathfrak{J}_1)$ est un module de type fini sur $A_0 = A_1 / \mathfrak{J}_1$.

Soit $\mathbf{A} = \varprojlim_{i}\mathbf{A}_i$, et pour tout entier $n\geqslant 0$, soient $u_{n}$ l'homomorphisme canonique $\mathbf{A}\to \mathbf{A}_{n}$, $\mathfrak{J}^{(n + 1)}\subset \mathbf{A}$ son noyau. Dans ces conditions :

(i) A est un anneau adique, ayant pour idéal de définition $\mathfrak{J}=\mathfrak{J}^{(1)}$.

(ii) On $a$$\mathfrak{J}^{(n)} = \mathfrak{J}^n$ pour tout $n\geqslant 1$

(iii) $\mathfrak{J}/\mathfrak{J}^2$ est isomorphe à $\mathfrak{J}_1 = \mathfrak{J}_1/\mathfrak{J}_1^2$, et est par suite un module de type fini sur $A_0 = A/\mathfrak{J}$.

L'hypothèse de surjectivité des $u_{ij}$ entraîne que $u_n$ est surjectif ; en outre, l'hypothèse a) implique que $\mathfrak{J}_j^{j+1}=0$, donc A est un anneau admissible (7.2.2) ; par définition, les $\mathfrak{J}^{(n)}$ forment un système fondamental de voisinages de o dans A, donc (ii) entraîne (i). En outre, on a $\mathfrak{J}=\varprojlim_{i}\mathfrak{J}_i$ et les applications $\mathfrak{J}\to\mathfrak{J}_i$ sont surjectives, donc (ii) entraîne (iii),

et on est ramené à prouver (ii). Par définition, $\mathfrak{J}^{(n)}$ est formé des éléments $(x_{k})_{k\geqslant 0}$ de A tels que $x_{k} = 0$ pour $k < n$, donc $\mathfrak{J}^{(n)}\mathfrak{J}^{(m)}\subset \mathfrak{J}^{(n + m)}$, autrement dit les $\mathfrak{J}^{(n)}$ constituent une filtration de A. D'autre part, $\mathfrak{J}^{(n)} / \mathfrak{J}^{(n + 1)}$ est isomorphe à la projection de $\mathfrak{J}^{(n)}$ sur $\mathrm{A}_n$; comme $\mathfrak{J}^{(n)} = \lim_{\overleftarrow{i > n}}\mathfrak{J}_i^n$, cette projection n'est autre que $\mathfrak{J}_n^n$, qui est un module sur

$A_{0}=A_{n}/\mathfrak{J}_{n}$ . Soient alors  $a_{j}=(a_{jk})_{k\geqslant0}$  r éléments de  $\mathfrak{J}=\mathfrak{J}^{(1)}$  tels que  $a_{11},\ldots,a_{r1}$  forment un système de générateurs de  $J_{1}$  sur  $A_{0}$ ; nous allons voir que l'ensemble  $S_{n}$  des monômes de degré total n en les  $a_{j}$  engendre l'idéal  $\mathfrak{J}^{(n)}$  de A. Comme  $J_{i}^{i+1}=o$ , il est clair tout d'abord que  $S_{n}\subset\mathfrak{J}^{(n)}$ ; puisque A est complet pour la filtration  $(\mathfrak{J}^{(m)})$ , il suffit de prouver que l'ensemble  $\overline{S}_{n}$  des classes mod.  $\mathfrak{J}^{(n+1)}$  des éléments de  $S_{n}$  engendre le module gradué grad( $\mathfrak{J}^{(n)}$ ) sur l'anneau gradué grad(A) pour la filtration précédente ([I], p. 18-06, lemme); en vertu de la définition de la multiplication dans grad(A),

il suffira de prouver que pour tout $m$, $\overline{\mathbf{S}}_{m}$ est un système de générateurs du $\mathbf{A}_{0}$-module $\mathfrak{J}^{(m)}/\mathfrak{J}^{(m+1)}$, ou encore que $\mathfrak{J}_{m}^{m}$ est engendré par les monômes de degré $m$ en les $a_{jm}$ ($1 \leqslant j \leqslant r$). Pour cela, il reste à montrer que $\mathfrak{J}_{m}$ est (en tant que $\mathbf{A}_{m}$-module) engendré par les monômes de degré $\leqslant m$ par rapport aux $a_{jm}$; la proposition étant évidente par définition pour $m=1$, raisonnons par récurrence sur $m$, et soit $\mathfrak{J}_{m}^{\prime}$ le sous-$\mathbf{A}_{m}$-module de $\mathfrak{J}_{m}$ engendré par ces monômes. La relation $\mathfrak{J}_{m-1}=\mathfrak{J}_{m}/\mathfrak{J}_{m}^{m}$ et l'hypothèse de récurrence prouvent que $\mathfrak{J}_{m}=\mathfrak{J}_{m}^{\prime}+\mathfrak{J}_{m}^{m}$ d'où, puisque $\mathfrak{J}_{m}^{m+1}=0$, l'on tire $\mathfrak{J}_{m}^{m}=\mathfrak{J}_{m}^{\prime m}$, et finalement $\mathfrak{J}_{m}=\mathfrak{J}_{m}^{\prime}$. Corollaire (7.2.8). — Sous les conditions de (7.2.7), pour que A soit noethérien, il faut et il suffit que $\mathbf{A}_{0}$ le soit.

Cela résulte aussitôt de (7.2.6).

Proposition (7.2.9). — Supposons vérifiées les hypothèses de (7.2.7) : pour tout entier i, soit  $M_{i}$  un  $A_{i}$ -module, et, pour  $i \leqslant j$ , soit  $v_{ij}: M_{j} \to M_{i}$  un  $u_{ij}$ -homomorphisme, tels que  $(\mathbf{M}_{i}, v_{ij})$  soit un système projectif. Supposons en outre que  $M_{0}$  soit un  $A_{0}$ -module de type fini, que  $v_{ij}$  soit surjectif et que son noyau soit  $J_{j}^{i+1}M_{j}$ . Alors  $M = \varprojlim M_{i}$  est un A-module de type fini, et le noyau du  $u_{n}$ -homomorphisme surjectif  $v_{n}: M \to M_{n}$  est  $J^{n+1}M$  (de sorte que  $M_{n}$  s'identifie à  $M/J^{n+1}M = M \otimes_{A}(A/J^{n+1})$ ).

Soient $z_h = (z_{hk})_{k \geqslant 0}$ un système de $s$ éléments de M tels que les $z_{h0} (1 \leqslant h \leqslant s)$ forment un système de générateurs de $\mathbf{M}_0$; on va montrer que les $z_h$ engendrent le A-module M. Le A-module M est séparé et complet pour la filtration formée par les $\mathbf{M}^{(n)}$, où $\mathbf{M}^{(n)}$ est l'ensemble des $y = (y_k)_{k \geqslant 0}$ de M tels que $y_k = 0$ pour $k < n$; il est clair que l'on a $\mathfrak{I}^{(n)}\mathbf{M} \subset \mathbf{M}^{(n)}$ et que $\mathbf{M}^{(n)} / \mathbf{M}^{(n+1)} = \mathfrak{J}_n^n\mathbf{M}_n$. On est donc ramené à montrer que les classes des $z_h$ mod. $\mathbf{M}^{(0)}$ engendrent le module gradué grad(M) (pour la filtration précédente) sur l'anneau gradué grad(A) ([1], p. 18-06, lemme); pour cela, on constate aisément qu'il suffit encore de prouver que les $z_{hn} (1 \leqslant h \leqslant s)$ engendrent le $A_n$-module $M_n$. On raisonne de nouveau par récurrence sur $n$, la proposition étant évidente par définition pour $n = 0$; la relation $M_{n-1} = M_n / \mathfrak{J}_n^n M_n$ et l'hypothèse de récurrence montrent que si $M_n'$ est le sous-module de $M_n$ engendré par les $z_{hn}$, on a $M_n = M_n' + \mathfrak{J}_n^n M_n$, et comme $\mathfrak{J}_n$ est nilpotent, cela entraîne $M_n = M_n'$. Le même raisonnement de passage aux modules gradués associés montre que l'application canonique de $\mathfrak{J}^{(n)}\mathbf{M}$ dans $\mathbf{M}^{(n)}$ est surjective (donc bijective), autrement dit que $\mathfrak{J}^{(n)}\mathbf{M} = \mathfrak{J}^n\mathbf{M}$ est le noyau de $M \to M_n$.

Corollaire (7.2.10). — Soit  $(\mathrm{N}_{i}, w_{ij})$  un second système projectif de  $A_{i}$ -modules vérifiant les conditions de (7.2.9), et soit  $N = \varprojlim N_{i}$ . Il y a correspondance biunivoque entre les systèmes projectifs  $(h_{i})$  de  $A_{i}$ -homomorphismes  $h_{i}: M_{i} \to N_{i}$  et les homomorphismes de A-modules  $h: M \to N$  (qui sont nécessairement continus pour les topologies J-adiques).

Il est clair que si $h: \mathbf{M} \to \mathbf{N}$ est un A-homomorphisme, on a $h(\mathfrak{J}^n\mathbf{M}) \subset \mathfrak{J}^n\mathbf{N}$, d'où la continuité de $h$; par passage aux quotients, il correspond donc à $h$ un système projectif de $\mathbf{A}_i$-homomorphismes $h_i: \mathbf{M}_i \to \mathbf{N}_i$, dont $h$ est la limite projective, d'où le corollaire.

Remarque (7.2.11). — Soit A un anneau adique ayant un idéal de définition $\mathfrak{J}$ tel que $\mathfrak{J}/\mathfrak{J}^{2}$ soit un (A/$\mathfrak{J}$)-module de type fini ; il est clair que les $A_{i}=A/\mathfrak{J}^{i+1}$ vérifient

les conditions de (7.2.7) ; comme A est la limite projective des  $A_{i}$ , on voit que la prop. (7.2.7) donne la description de tous les anneaux adiques du type considéré (et en particulier de tous les anneaux adiques noethériens).

Exemple (7.2.12). — Soient B un anneau, J un idéal de B tel que $\mathfrak{J}/\mathfrak{J}^{2}$ soit un module de type fini sur B/$\mathfrak{J}$ (ou sur B, ce qui revient au même); posons $A=\varprojlim_{n}B/\mathfrak{J}^{n+1}$;

A est le séparé complété de B muni de la topologie J-préadique. Si  $A_{n}=B/J^{n+1}$ , il est immédiat que les  $A_{n}$  vérifient les conditions de (7.2.7); donc A est un anneau adique et si  $\overline{J}$  est l'adhérence dans A de l'image canonique de J,  $\overline{J}$  est un idéal de définition de A,  $\overline{J}^{n}$  est l'adhérence de l'image canonique de  $J^{n}$ ,  $A/\overline{J}^{n}$  s'identifie à  $B/J^{n}$  et  $\overline{J}/\overline{J}^{2}$  est isomorphe à  $J/J^{2}$  en tant que  $(A/\overline{J})$ -module. De même, si N est tel que N/JN soit un B-module de type fini, et si on pose  $M_{i}=N/J^{i+1}N$ ,  $M=\varprojlim M_{i}$  est un A-module de type fini, isomorphe au séparé complété de N pour la topologie J-préadique,  $\overline{J}^{n}M$  s'identifie à l'adhérence de l'image canonique de  $J^{n}N$ , et  $M/\overline{J}^{n}M$  à  $N/J^{n}N$ .

## 7.3. Anneaux préadiques noethériens.

(7.3.1) Soient A un anneau, $\mathfrak{J}$ un idéal de A, M un A-module ; nous désignerons par $\hat{\mathbf{A}} = \varprojlim_{n} \mathbf{A} / \mathfrak{J}^{n}$ (resp. $\hat{\mathbf{M}} = \varprojlim_{u} \mathbf{M} / \mathfrak{J}^{n}\mathbf{M}$) le séparé complété de A (resp. M) pour la topologie $\mathfrak{J}$-préadique. Soit $\mathbf{M}' \xrightarrow{u} \mathbf{M} \xrightarrow{v} \mathbf{M}'' \to o$ une suite exacte de A-modules; comme $\mathbf{M} / \mathfrak{J}^{n}\mathbf{M} = \mathbf{M} \otimes_{\mathbf{A}} (\mathbf{A} / \mathfrak{J}^{n})$, la suite

$$
\mathbf {M} ^ {\prime} / \Im^ {n} \mathbf {M} ^ {\prime} \stackrel {u _ {n}} {\rightarrow} \mathbf {M} / \Im^ {n} \mathbf {M} \stackrel {v _ {n}} {\rightarrow} \mathbf {M} ^ {\prime \prime} / \Im^ {n} \mathbf {M} ^ {\prime \prime} \rightarrow 0
$$

est exacte pour tout n. En outre, comme  $v(\mathfrak{J}^{n}\mathbf{M})=\mathfrak{J}^{n}v(\mathbf{M})=\mathfrak{J}^{n}\mathbf{M}^{\prime\prime},\hat{v}=\varprojlim v_{n}$  est surjective (Bourbaki, Top. gén., chap. IX, 2° éd., p. 60, cor. 2). D'autre part, si  $z=(z_{k})$  est un élément du noyau de  $\hat{v}$, pour tout entier k, il existe un  $z_{k}^{\prime}\in\mathbf{M}^{\prime}/\mathfrak{J}^{k}\mathbf{M}^{\prime}$  tel que  $u_{k}(z_{k}^{\prime})=z_{k}$; on en conclut qu'il existe  $z^{\prime}=(z_{n}^{\prime})\in\hat{\mathbf{M}}^{\prime}$  tel que les k premières composantes de  $\hat{u}(z^{\prime})$  coïncident avec celles de z; autrement dit, l'image par  $\hat{u}$  de  $\hat{M}$  est dense dans le noyau de  $\hat{v}$.

Si on suppose A noethérien, il en est de même de $\hat{\mathbf{A}}$, en vertu de (7.2.12), $\mathfrak{J}/\mathfrak{J}^{2}$ étant alors un A-module de type fini. En outre :

Théorème de Krull (7.3.2). — Soient A un anneau noethérien, J un idéal de A, M un A-module de type fini, M' un sous-module de M; alors la topologie induite sur M' par la topologie J-préadique de M est identique à la topologie J-préadique de M'.

Cela résulte aussitôt du

Lemme d'Artin-Rees (7.3.2.1). — Sous les hypothèses de (7.3.2), il existe un entier p tel que, pour  $n \geqslant p$ , on ait

$$
\mathbf {M} ^ {\prime} \cap \mathfrak {J} ^ {n} \mathbf {M} = \mathfrak {J} ^ {n - p} (\mathbf {M} ^ {\prime} \cap \mathfrak {J} ^ {p} \mathbf {M})
$$

Pour la démonstration, voir ([1], p. 2-04).

Corollaire (7.3.3). — Sous les hypothèses de (7.3.2), l'application canonique  $M \otimes_{A} \hat{A} \to \hat{M}$  est bijective, et le foncteur  $M \otimes_{A} \hat{A}$  est exact en M dans la catégorie des A-modules de type fini; par suite, le séparé complété J-adique  $\hat{A}$  est un A-module plat (6.1.1).

Notons d'abord que dans la catégorie des A-modules de type fini, $\hat{\mathbf{M}}$ est un foncteur exact en M. Soit en effet $o\to M'\xrightarrow{u}M\xrightarrow{v}M''\to o$ une suite exacte ; on sait déjà que $\hat{v}:\hat{\mathbf{M}}\to \hat{\mathbf{M}}''$ est surjectif (7.3.1) ; d'autre part, si $i$ est l'homomorphisme canonique $\mathbf{M}\to \hat{\mathbf{M}}$, il résulte du th. de Krull que l'adhérence dans $\hat{\mathbf{M}}$ de $i(u(\mathbf{M}))$ s'identifie au séparé complété de $\mathbf{M}'$ pour la topologie $\Im$-préadique ; donc $\hat{u}$ est injectif, et en vertu de (7.3.1) l'image de $\hat{u}$ est égale au noyau de $\hat{v}$.

Cela étant, l'application canonique  $M \otimes_{A} \hat{A} \to \hat{M}$  s'obtient en passant à la limite projective sur les applications  $M \otimes_{A} \hat{A} \to M \otimes_{A} (A / \mathfrak{J}^{n}) = M / \mathfrak{J}^{n} M$ . Il est clair que cette application est bijective lorsque M est de la forme  $A^{p}$ . Si M est un A-module de type fini, on a une suite exacte  $A^{p} \to A^{q} \to M \to o$ , d'où, en vertu de l'exactitude à droite des foncteurs  $M \otimes_{A} \hat{A}$  et  $\hat{M}$  (en M) dans la catégorie des A-modules de type fini, le diagramme commutatif

$$
\begin{array}{c} \mathrm{A} ^ {p} \otimes \hat {\mathrm{A}} \to \mathrm{A} ^ {q} \otimes \hat {\mathrm{A}} \to \mathrm{M} \otimes \hat {\mathrm{A}} \to 0 \\ \downarrow \qquad \qquad \qquad \downarrow \qquad \qquad \qquad \downarrow \\ \hat {\mathrm{A}} ^ {p} \longrightarrow \hat {\mathrm{A}} ^ {q} \longrightarrow \hat {\mathrm{M}} \longrightarrow 0 \end{array}
$$

où les deux lignes sont exactes et les deux premières flèches verticales des isomorphismes ; on en tire aussitôt la conclusion.

Corollaire (7.3.4). — Soient A un anneau noethérien, J un idéal de A, M, N deux A-modules de type fini; on a des isomorphismes canoniques fonctoriels

$$
(\mathbf {M} \otimes_ {\mathbf {A}} \mathbf {N}) ^ {\wedge} \stackrel {{\sim}} {{\to}} \hat {\mathbf {M}} \otimes_ {\hat {\mathbf {A}}} \hat {\mathbf {N}}, \qquad (\operatorname{Hom} _ {\mathbf {A}} (\mathbf {M}, \mathbf {N})) ^ {\wedge} \stackrel {{\sim}} {{\to}} \operatorname{Hom} _ {\hat {\mathbf {A}}} (\hat {\mathbf {M}}, \hat {\mathbf {N}})
$$

Cela résulte de (7.3.3), (6.2.1) et (6.2.2).

Corollaire (7.3.5). — Soient A un anneau noethérien, J un idéal de A. Les conditions suivantes sont équivalentes :

a) J est contenu dans le radical de A.

b) $\hat{\mathbf{A}}$ est un A-module fidèlement plat (6.4.1).

c) Tout A-module de type fini est séparé pour la topologie J-préadique.

d) Tout sous-module d'un A-module de type fini est fermé pour la topologie J-préadique.

Comme $\hat{\mathbf{A}}$ est un A-module plat, les conditions $b)$ et $c)$ sont équivalentes, car $b)$ équivaut à dire que si $\mathbf{M}$ est un A-module de type fini, l'application canonique $\mathbf{M} \to \hat{\mathbf{M}} = \mathbf{M} \otimes_{\mathbf{A}} \hat{\mathbf{A}}$ est injective (6.6.1, $c$). Il est immédiat que $c)$ entraîne $d)$, car si $\mathbf{N}$ est un sous-module d'un A-module $\mathbf{M}$ de type fini, $\mathbf{M} / \mathbf{N}$ est séparé pour la topologie $\mathfrak{J}$-préadique, donc $\mathbf{N}$ est fermé dans $\mathbf{M}$. Montrons que $d)$ implique $a)$: si $\mathfrak{m}$ est un idéal maximal de $\mathbf{A}$, $\mathfrak{m}$ est fermé dans $\mathbf{A}$ pour la topologie $\mathfrak{J}$-préadique, donc $\mathfrak{m} = \bigcap_{p \geqslant 0} (\mathfrak{m} + \mathfrak{J}^p)$, et comme $\mathfrak{m} + \mathfrak{J}^p$ est nécessairement égal à $\mathbf{A}$ ou à $\mathfrak{m}$, on a $\mathfrak{m} + \mathfrak{J}^p = \mathfrak{m}$ pour $p$ assez

grand, d'où $\mathfrak{J}^{p}\subset m$ et $\mathfrak{J}\subset m$ puisque $m$ est premier. Enfin, $a)$ entraîne $b)$ : soit en effet P l'adhérence de $\{o\}$ dans un A-module M de type fini, pour la topologie $\mathfrak{J}$-préadique ; en vertu du th. de Krull (7.3.2), la topologie induite sur P par la topologie $\mathfrak{J}$-préadique de M est la topologie $\mathfrak{J}$-préadique de P, donc $\mathfrak{JP}=P$ ; comme P est de type fini, il résulte du lemme de Nakayama que $P=o$ ($\mathfrak{J}$ étant contenu dans le radical de A).

On notera que les conditions de (7.3.5) sont remplies lorsque A est un anneau local noethérien et $\mathfrak{J}\neq\mathrm{A}$ un idéal quelconque de A.

Corollaire (7.3.6). — Si A est un anneau J-adique noethérien, tout A-module de type fini est séparé et complet pour la topologie J-préadique.

Comme on a alors $\hat{\mathbf{A}} = \mathbf{A}$, cela résulte aussitôt de (7.3.3).

On en conclut que la prop. (7.2.9) donne la description de tous les modules de type fini sur un anneau adique noethérien.

Corollaire (7.3.7). — Sous les hypothèses de (7.3.2), le noyau de l'application canonique  $M \to \hat{M} = M \otimes_{A} \hat{A}$  est l'ensemble des  $x \in M$  annulés par un élément de  $1 + J$ .

En effet, pour que $x\in\mathbf{M}$ appartienne à ce noyau, il faut et il suffit que le séparé complété du sous-module Ax se réduise à o (par (7.3.2)), autrement dit que $x\in\Im x$.

## 7.4. Modules quasi-finis sur les anneaux locaux.

Définition (7.4.1). — Étant donné un anneau local A, d'idéal maximal m, on dit qu'un A-module M est quasi-fini (sur A) si M/mM est de rang fini sur le corps résiduel k=A/m.

Lorsque A est noethérien, le séparé complété $\hat{\mathbf{M}}$ de M pour la topologie m-préadique est alors un $\hat{\mathbf{A}}$-module de type fini; en effet, comme $\mathfrak{m} / \mathfrak{m}^2$ est alors un A-module de type fini, cela résulte de (7.2.12) et de l'hypothèse sur $\mathbf{M} / \mathfrak{m}\mathbf{M}$.

En particulier, si on suppose de plus que A est complet et M séparé pour la topologie m-préadique (autrement dit,  $\bigcap_{n}m^{n}M=o$ ), M lui-même est un A-module de type fini : en effet,  $\hat{M}$  est alors un A-module de type fini, et comme M s'identifie à un sous-module de  $\hat{M}$ , M est lui aussi de type fini (et d'ailleurs identique à son complété en vertu de (7.3.6)).

Proposition (7.4.2). — Soient A, B deux anneaux locaux, m, n leurs idéaux maximaux, et supposons B noethérien. Soient φ : A→B un homomorphisme local, M un B-module de type fini. Si M est un A-module quasi-fini, les topologies m-préadique et n-préadique sur M sont identiques, donc séparées.

Remarquons que par hypothèse M/mM est de longueur finie en tant que A-module, donc aussi a fortiori en tant que B-module. On en conclut que n est le seul idéal premier de B contenant l'annulateur de M/mM : en effet, on se ramène aussitôt, en vertu de (1.7.4) et (1.7.2), au cas où M/mM est simple, donc nécessairement isomorphe à B/n, et notre assertion est évidente dans ce dernier cas. D'autre part, comme M est un B-module de type fini, les idéaux premiers qui contiennent l'annulateur de M/mM sont ceux qui contiennent mB+b, en désignant par b l'annulateur du B-module M (1.7.5). Comme B est noethérien, on en conclut ([11], p. 127, cor. 4) que mB+b est un idéal

de définition de B, autrement dit qu'il existe $k>0$ tel que $\mathfrak{n}^{k}\subset\mathfrak{m}\mathbf{B}+\mathfrak{b}\subset\mathfrak{n}$; par suite, pour tout $h>0$

$$
\mathfrak {n} ^ {h k} \mathbf {M} \subset (\mathfrak {m B} + \mathfrak {b}) ^ {h} \mathbf {M} = \mathfrak {m} ^ {h} \mathbf {M} \subset \mathfrak {n} ^ {h} \mathbf {M}
$$

ce qui prouve que les topologies m-préadique et n-préadique sur M sont les mêmes; la seconde est d'ailleurs séparée en vertu de (7.3.5).

Corollaire (7.4.3). — Sous les hypothèses de (7.4.2), si en outre A est noethérien et complet pour la topologie m-préadique, M est un A-module de type fini.

En effet, M est alors séparé pour la topologie m-préadique, et notre assertion résulte de la remarque faite dans (7.4.1).

(7.4.4) Le cas d'application de (7.4.2), qui est le plus important, est celui où B lui-même est un A-module quasi-fini, ce qui revient à dire que B/mB est une algèbre de rang fini sur k = A/m; cette condition peut d'ailleurs se décomposer en la conjonction des deux suivantes, en vertu de ce qui précède :

(i) mB est un idéal de définition de B ;

(ii) B/n est une extension de rang fini du corps A/m.

Lorsqu'il en est ainsi, tout B-module de type fini est évidemment un A-module quasi-fini.

Corollaire (7.4.5). — Sous les hypothèses de (7.4.2), si b est l'annulateur du B-module M, B/b est un A-module quasi-fini.

Supposons M≠o (sinon le corollaire est évident). On peut considérer M comme un module sur l'anneau local noethérien B/b; son annulateur étant alors réduit à o, la démonstration de (7.4.2) montre que m(B/b) est un idéal de définition de B/b. Par ailleurs, M/nM est un espace vectoriel de rang fini sur A/m, étant un quotient de M/mM, qui est par hypothèse de rang fini sur A/m; comme M≠o, on a M≠nM en vertu du lemme de Nakayama; comme M/nM est un espace vectoriel ≠o sur B/n, le fait qu'il est de rang fini sur A/m implique que B/n est aussi de rang fini sur A/m; la conclusion résulte donc de (7.4.4) appliqué à l'anneau B/b.

## 7.5. Anneaux de séries formelles restreintes.

(7.5.1) Soient A un anneau topologique, linéairement topologisé, séparé et complet; soit  $(\mathfrak{J}_{\lambda})$  un système fondamental de voisinages de o dans A formé d'idéaux (ouverts), de sorte que A s'identifie canoniquement à  $\varprojlim A/\mathfrak{J}_{\lambda}$  (7.2.1). Pour tout  $\lambda$ , soit  $B_{\lambda}=(A/\mathfrak{J}_{\lambda})[T_{1},\ldots,T_{r}]$ , où les  $T_{i}$  sont des indéterminées; il est clair que les  $B_{\lambda}$  forment un système projectif d'anneaux discrets. Nous poserons  $\varprojlim B_{\lambda}=A\{T_{1},\ldots,T_{r}\}$ , et nous allons voir que cet anneau topologique est indépendant du système fondamental d'idéaux  $(\mathfrak{J}_{\lambda})$  considéré. De façon précise, soit  $A'$  le sous-anneau de l'anneau de séries formelles  $A[[T_{1},\ldots,T_{r}]]$  formé des séries formelles  $\Sigma c_{\alpha}T^{\alpha}$  (avec  $\alpha=(\alpha_{1},\ldots,\alpha_{r})\in\mathbf{N}^{r}$ ) telles que  $\lim c_{\alpha}=0$  (suivant le filtre des complémentaires des parties finies de  $N^{r}$ ); nous dirons que ces séries sont les séries formelles restreintes en les  $T_{i}$ , à coefficients dans A.

Pour tout voisinage V de o dans A, soit V' l'ensemble des  $x = \sum_{\alpha} c_{\alpha} T^{\alpha} \in A'$  telles que  $c_{\alpha} \in V$  pour tout  $\alpha$ . On vérifie aussitôt que les V' forment un système fondamental de voisinages de o définissant sur A' une topologie d'anneau séparée ; nous allons définir canoniquement un isomorphisme topologique de l'anneau  $A\{T_{1}, \ldots, T_{r}\}$  sur  $A'$ . Pour tout  $\alpha \in N^{r}$  et tout  $\lambda$ , soit  $\varphi_{\lambda, \alpha}$  l'application de  $(A/\mathfrak{J}_{\lambda})[T_{1}, \ldots, T_{r}]$  dans  $A/\mathfrak{J}_{\lambda}$  qui, à tout polynôme du premier anneau, fait correspondre le coefficient de  $T^{\alpha}$  dans ce polynôme. Il est clair que les  $\varphi_{\lambda, \alpha}$  forment un système projectif d'homomorphismes de  $(A/\mathfrak{J}_{\lambda})$ -modules, dont la limite projective est un homomorphisme continu  $\varphi_{\alpha}: A\{T_{1}, \ldots, T_{r}\} \to A$ ; nous allons voir que, pour tout  $y \in A\{T_{1}, \ldots, T_{r}\}$ , la série formelle  $\Sigma\varphi_{\alpha}(y)T^{\alpha}$  est restreinte. En effet, si  $y_{\lambda}$  est la composante de y dans  $B_{\lambda}$ , et si on désigne par  $H_{\lambda}$  l'ensemble fini des  $\alpha \in N^{r}$  pour lesquels les coefficients du polynôme  $y_{\lambda}$  ne sont pas nuls, on a  $\varphi_{\lambda, \alpha}(y_{\mu}) \in \mathfrak{J}_{\lambda}$  pour  $J_{\mu} \subset J_{\lambda}$  et  $\alpha \notin H_{\lambda}$  et par passage à la limite,  $\varphi_{\alpha}(y) \in J_{\lambda}$  pour  $\alpha \notin H_{\lambda}$ . On définit donc un homomorphisme d'anneaux  $\varphi: A\{T_{1}, \ldots, T_{r}\} \to A'$  en posant  $\varphi(y) = \Sigma\varphi_{\alpha}(y)T^{\alpha}$ , et il est immédiat que  $\varphi$  est continu. Inversement, si  $\theta_{\lambda}$  est l'homomorphisme canonique  $A \to A/\mathfrak{J}_{\lambda}$ , pour tout élément  $z = \Sigma c_{\alpha} T^{\alpha} \in A'$  et tout  $\lambda$ , il n'y, a qu'un nombre fini d'indices  $\alpha$  tels que  $\theta_{\lambda}(c_{\alpha}) \neq 0$ , et par suite  $\psi_{\lambda}(z) = \Sigma\theta_{\lambda}(c_{\alpha}) T^{\alpha}$  appartient à  $B_{\lambda}$ ; les  $\psi_{\lambda}$  sont continus et forment un système projectif d'homomorphismes dont la limite projective est un homomorphisme continu  $\psi: A' \to A\{T_{1}, \ldots, T_{r}\}$ ; il reste enfin à vérifier que  $\varphi \circ \psi$  et  $\psi \circ \varphi$  sont les automorphismes identiques, ce qui est immédiat.

(7.5.2) Nous identifierons  $A\{T_{1}, \ldots, T_{r}\}$  à l'anneau  $A'$  des séries formelles restreintes au moyen des isomorphismes définis dans (7.5.1). Les isomorphismes canoniques

$$
((\mathrm{A} / \mathfrak {I} _ {\lambda}) [ \mathrm{T} _ {1}, \dots , \mathrm{T} _ {r} ]) [ \mathrm{T} _ {r + 1}, \dots , \mathrm{T} _ {s} ] \xrightarrow {\sim} (\mathrm{A} / \mathfrak {I} _ {\lambda}) [ \mathrm{T} _ {1}, \dots , \mathrm{T} _ {s} ]
$$

définissent, par passage à la limite projective, un isomorphisme canonique

$$
\left[\left(\mathrm{A} \left\{\mathrm{T} _ {1}, \dots , \mathrm{T} _ {r} \right\}\right)\left\{\mathrm{T} _ {r + 1}, \dots , \mathrm{T} _ {s} \right\} \widetilde {\rightarrow} \mathrm{A} \left\{\mathrm{T} _ {1}, \dots , \mathrm{T} _ {s} \right\}\right.
$$

(7.5.3) Pour tout homomorphisme continu $u: \mathrm{A} \to \mathrm{B}$ de A dans un anneau linéairement topologisé B, séparé et complet, et tout système $(b_1, \ldots, b_r)$ de $r$ éléments de B, il existe un homomorphisme continu et un seul $\overline{u}: \mathrm{A}\{\mathrm{T}_1, \ldots, \mathrm{T}_r\} \to \mathrm{B}$, tel que $\overline{u}(a) = u(a)$ pour tout $a \in \mathrm{A}$ et $\overline{u}(\mathrm{T}_j) = b_j$ pour $1 \leqslant j \leqslant r$. Il suffit en effet de prendre

$$
\overline {{{u}}} (\sum_ {\alpha} c _ {\alpha} \mathrm{T} ^ {\alpha}) = \sum_ {\alpha} u (c _ {\alpha}) b _ {1} ^ {\alpha_ {1}} \dots b _ {r} ^ {\alpha_ {r}};
$$

les vérifications du fait que la famille $(u(c_{\alpha})b_{1}^{\alpha_{1}}\ldots b_{r}^{\alpha_{r}})$ est sommable dans B et de la continuité de $\overline{u}$ sont immédiates et laissées au lecteur. On notera que cette propriété (pour B et les $b_{j}$ arbitraires) caractérise l'anneau topologique A{T$_{1}$, ..., T$_{r}$} à un isomorphisme unique près.

Proposition (7.5.4). — (i) Si A est un anneau admissible, il en est de même de $\mathbf{A}' = \mathbf{A}\{\mathrm{T}_1, \ldots, \mathrm{T}_r\}$.

(ii) Soient A un anneau adique, J un idéal de définition de A tel que $\mathfrak{J}/\mathfrak{J}^{2}$ soit de type fini

sur A/ $\mathfrak{J}$ . Si on pose  $J' = J A'$ , A'est alors un anneau  $J'$ -adique, et  $J'/J'^{2}$  est de type fini sur  $A'/J'$ . Si, en outre, A est noethérien, il en est de même de  $A'$ .

(i) Si $\mathfrak{J}$ est un idéal de A, $\mathfrak{J}'$ l'idéal de A' formé des $\sum_{\alpha} c_{\alpha} T^{\alpha}$ tels que $c_{\alpha} \in \mathfrak{J}$ pour tout $\alpha$, alors $(\mathfrak{J}')^{n} \subset (\mathfrak{J}^{n})'$; si $\mathfrak{J}$ est un idéal de définition de A, $\mathfrak{J}'$ est donc un idéal de définition de A'.

(ii) Posons  $A_{i}=A/\mathfrak{J}^{i+1}$ , et pour  $i\leqslant j$ , soit  $u_{ij}$  l'homomorphisme canonique  $A/\mathfrak{J}^{i+1}\to A/\mathfrak{J}^{i+1}$ ; posons  $A_{i}^{\prime}=A_{i}[T_{1},\ldots,T_{r}]$ , et soit  $u_{ij}^{\prime}$  l'homomorphisme  $A_{j}^{\prime}\to A_{i}^{\prime}$  ( $i\leqslant j$ ) obtenu en appliquant  $u_{ij}$  aux coefficients des polynômes de  $A_{j}^{\prime}$ . Montrons que le système projectif  $(\mathrm{A}_{i}^{\prime},u_{ij}^{\prime})$  vérifie les conditions de (7.2.7); comme  $J^{\prime}$  est le noyau de  $A^{\prime}\to A_{0}^{\prime}$ , cela démontrera la première assertion de (ii). Or, il est clair que les  $u_{ij}^{\prime}$  sont surjectifs; le noyau  $J_{i}^{\prime}$  de  $u_{0i}$  est l'ensemble des polynômes de  $A_{i}[T_{1},\ldots,T_{r}]$  dont les coefficients sont dans  $J/\mathfrak{J}^{i+1}$ ; en particulier,  $J_{1}^{\prime}$  est l'ensemble des polynômes de  $A_{1}[T_{1},\ldots,T_{r}]$  dont les coefficients sont dans  $J/\mathfrak{J}^{2}$ . Comme  $J/\mathfrak{J}^{2}$  est de type fini sur  $A_{1}=A/\mathfrak{J}^{2}$ , on voit déjà que  $J_{1}^{\prime}/J_{1}^{\prime2}$  est un module de type fini sur  $A_{1}^{\prime}$  (ou, ce qui revient au même, sur  $A_{0}^{\prime}=A_{1}^{\prime}/J_{1}^{\prime}$ ). Montrons que le noyau de  $u_{ij}$  est  $J_{j}^{\prime i+1}$ . Il est évident que  $J_{j}^{\prime i+1}$  est contenu dans ce noyau. D'autre part, soient  $a_{1},\ldots,a_{m}$  des éléments de J dont les classes mod.  $J^{2}$  engendrent  $J/\mathfrak{J}^{2}$ ; on vérifie immédiatement que les classes mod.  $J^{j+1}$  des monômes de degré  $\leqslant j$  en les  $a_{k}\left(\mathrm{i}\leqslant k\leqslant m\right)$  engendrent  $J/\mathfrak{J}^{j+1}$ , et les classes des monômes de degré >i et  $\leqslant j$  engendrent donc  $J^{i+1}/J^{j+1}$ ; un monôme en les  $T_{k}$  ayant un tel élément comme coefficient est donc produit de  $i+\mathrm{i}\acute{}$ éléments de  $J_{j}^{\prime}$ , ce qui établit notre assertion. Enfin, si A est noethérien, il en est de même de  $A^{\prime}/J^{\prime}=(A/\mathfrak{J})[T_{1},\ldots,T_{r}]$ , donc  $A^{\prime}$  est noethérien (7.2.8).

Proposition (7.5.5). — Soient A un anneau noethérien J-adique, B un anneau topologique admissible, $\varphi : \mathrm{A} \to \mathrm{B}$ un homomorphisme continu, faisant de B une A-algèbre. Les conditions suivantes sont équivalentes :

a) B est noethérien et JB-adique, et B/JB est une algèbre de type fini sur A/J.

b) B est topologiquement A-isomorphe à $\varprojlim\mathrm{B}_{n}$, où $\mathrm{B}_{n}=\mathrm{B}_{m}/\mathfrak{J}^{n+1}\mathrm{B}_{m}$ pour $m\geqslant n$, et $\mathrm{B}_{1}$ est une algèbre de type fini sur $\mathrm{A}_{1}=\mathrm{A}/\mathfrak{J}^{2}$.

c) B est topologiquement A-isomorphe à un quotient d'une algèbre de la forme A  $\{T_{1}, \ldots, T_{r}\}$  par un idéal (nécessairement fermé en vertu de (7.3.6) et (7.5.4 (ii))).

Comme A est noethérien, il en est de même de  $A' = A \{T_{1}, \ldots, T_{r}\}$  (7.5.4), donc c) implique que B est noethérien; comme  $J' = JA'$  est un voisinage ouvert de o dans  $A'$  tel que les  $J'^{n}$  forment un système fondamental de voisinages de o, les images  $J^{m}B$  des  $J'^{m}$  forment un système fondamental de voisinages de o dans B, et comme on sait que B est séparé et complet, B est un anneau JB-adique. Enfin, B/JB est une algèbre (sur A/J) quotient de  $A'/J'A' = (A/J)[T_{1}, \ldots, T_{r}]$ , donc est de type fini, ce qui achève de prouver que c) entraîne a).

Si B est JB-adique et noethérien, B est isomorphe à  $\lim_{n\to\infty}B_n$ , où  $B_n=B/\mathfrak{J}^{n+1}B(7.2.11)$ , et JB/ $J^2B$  est un module de type fini sur B/JB. Soit  $(a_j)_{1\leqslant j\leqslant s}$  un système de générateurs du (B/JB)-module JB/ $J^2B$ , et  $(c_i)_{1\leqslant i\leqslant r}$  un système d'éléments de B/ $J^2B$  dont les classes

mod. $\mathfrak{J}\mathrm{B} / \mathfrak{J}^2\mathrm{B}$ forment un système de générateurs de la (A/$\mathfrak{J}$)-algèbre B/$\mathfrak{J}\mathrm{B}$; on voit aussitôt que les $c_i a_j$ forment un système de générateurs de la (A/$\mathfrak{J}^2$)-algèbre B/$\mathfrak{J}^2\mathrm{B}$, donc $a)$ implique $b$).

Reste à prouver que $b)$ entraîne $c)$. L'hypothèse entraîne que $\mathbf{B}_1$ est un anneau noethérien, et comme $\mathbf{B}_1 = \mathbf{B}_2 / \mathfrak{J}^2\mathbf{B}_2$, on a $\mathfrak{J}^2\mathbf{B}_1 = \mathbf{o}$, donc $\mathfrak{J}\mathbf{B}_1 = \mathfrak{J}\mathbf{B}_1 / \mathfrak{J}^2\mathbf{B}_1$ est un $\mathbf{B}_0$-module de type fini. Les conditions de (7.2.7) sont donc vérifiées par le système projectif ($\mathbf{B}_n$) et B est un anneau $\mathfrak{J}\mathbf{B}$-adique. Soit $(c_i)_{1 \leqslant i \leqslant r}$ un système fini d'éléments de B dont les classes mod. $\mathfrak{J}\mathbf{B}$ engendrent la (A/$\mathfrak{J}$)-algèbre B/$\mathfrak{J}\mathbf{B}$, et dont les combinaisons linéaires à coefficients dans $\mathfrak{J}$ sont telles que leurs classes mod. $\mathfrak{J}^2\mathbf{B}$ engendrent le $\mathbf{B}_0$-module $\mathfrak{J}\mathbf{B}/\mathfrak{J}^2\mathbf{B}$. Il existe un A-homomorphisme continu $u$ de $\mathbf{A}' = \mathbf{A}\{\mathrm{T}_1, \ldots, \mathrm{T}_r\}$ dans B qui se réduit à $\varphi$ dans A et est tel que $u(\mathrm{T}_i) = c_i$ pour $1 \leqslant i \leqslant r$ (7.5.3); si nous prouvons que $u$ est surjectif, $c)$ sera établi, car de $u(\mathrm{A}') = \mathrm{B}$ on déduira $u(\mathfrak{J}^n\mathrm{A}') = \mathfrak{J}^n\mathrm{B}$, autrement dit $u$ sera un morphisme strict d'anneaux topologiques et B sera donc isomorphe à un quotient de $\mathbf{A}'$ par un idéal fermé. Or, comme B est complet pour la topologie $\mathfrak{J}\mathbf{B}$-adique, il suffit ([1], p. 18-07) de montrer que l'homomorphisme $\operatorname{grad}(\mathrm{A}') \to \operatorname{grad}(\mathrm{B})$ déduit canoniquement de $u$ pour les filtrations $\mathfrak{J}$-adiques sur $\mathbf{A}'$ et B, est surjectif. Mais par définition, les homomorphismes $\mathbf{A}' / \mathfrak{J}\mathbf{A}' \to \mathbf{B}/\mathfrak{J}\mathbf{B}$ et $\mathfrak{J}\mathbf{A}' / \mathfrak{J}^2\mathbf{A}' \to \mathfrak{J}\mathbf{B}/\mathfrak{J}^2\mathbf{B}$ déduits de $u$ sont surjectifs; par récurrence sur $n$, on en déduit aussitôt qu'il en est de même de $\mathfrak{J}\mathbf{A}' / \mathfrak{J}^n\mathbf{A}' \to \mathfrak{J}\mathbf{B}/\mathfrak{J}^n\mathbf{B}$, et a fortiori de $\mathfrak{J}^n\mathbf{A}' / \mathfrak{J}^{n+1}\mathbf{A}' \to \mathfrak{J}^n\mathbf{B}/\mathfrak{J}^{n+1}\mathbf{B}$, ce qui achève la démonstration.

## 7.6. Anneaux complets de fractions.

(7.6.1) Soient A un anneau linéairement topologisé,  $(\mathfrak{J}_{\lambda})$  un système fondamental de voisinages de o dans A formé d'idéaux, S une partie multiplicative de A. Soit  $u_{\lambda}$  l'homomorphisme canonique  $A \to A_{\lambda} = A / \mathfrak{J}_{\lambda}$ , et pour  $J_{\mu} \subset J_{\lambda}$ , soit  $u_{\lambda\mu}$  l'homomorphisme canonique  $A_{\mu} \to A_{\lambda}$ . Posons  $S_{\lambda} = u_{\lambda}(S)$ , de sorte que  $u_{\lambda\mu}(S_{\mu}) = S_{\lambda}$ . Les  $u_{\lambda\mu}$  donnent canoniquement des homomorphismes surjectifs  $S_{\mu}^{-1}A_{\mu} \to S_{\lambda}^{-1}A_{\lambda}$ , pour lesquels ces anneaux forment un système projectif ; désignons par  $A\{S^{-1}\}$  la limite projective de ce système. Cette définition ne dépend pas du système fondamental de voisinages  $(\mathfrak{J}_{\lambda})$  choisi ; en effet :

Proposition (7.6.2). — L'anneau A{S$^{-1}$} est topologiquement isomorphe au séparé complété de l'anneau S$^{-1}$A pour la topologie dont un système fondamental de voisinages de o est formé des S$^{-1}$J$_{\lambda}$.

En effet, si $v_{\lambda}$ est l'homomorphisme canonique $S^{-1}A \to S_{\lambda}^{-1}A_{\lambda}$ déduit de $u_{\lambda}$, le noyau de $v_{\lambda}$ est $S^{-1}\mathfrak{J}_{\lambda}$ et $v_{\lambda}$ est surjectif, d'où la proposition (7.2.1).

Corollaire (7.6.3). — Si S' est l'image canonique de S dans le séparé complété $\hat{\mathbf{A}}$ de A, $\mathbf{A}\{\mathbf{S}^{-1}\}$ s'identifie canoniquement à $\hat{\mathbf{A}}\{\mathbf{S}^{\prime-1}\}$.

On notera que même si A est séparé et complet, il n'en est pas de même de  $S^{-1}A$  pour la topologie définie par les  $S^{-1}J_{\lambda}$ , comme on le voit par exemple en prenant pour S l'ensemble des  $f^{n} (n \geqslant 0)$ , où f est topologiquement nilpotent et non nilpotent : en effet,  $S^{-1}A$  n'est pas réduit à o et d'autre part, pour tout  $\lambda$  il existe n tel que  $f^{n} \in J_{\lambda}$ , donc  $r = f^{n}/f^{n} \in S^{-1}J_{\lambda}$  et  $S^{-1}J_{\lambda} = S^{-1}A$ .

Corollaire (7.6.4). — Si, dans A, o n'est pas adhérent à S, l'anneau A{S$^{-1}$} n'est pas réduit à o.

En effet, o n'est pas adhérent à  $\{1\}$  dans l'anneau  $S^{-1}A$ ; sinon, on aurait  $i \in S^{-1}J_{\lambda}$  pour tout idéal ouvert  $J_{\lambda}$  de A, et il en résulterait que  $J_{\lambda} \cap S \neq \emptyset$  pour tout  $\lambda$ , contrairement à l'hypothèse.

(7.6.5) Nous dirons que  $A\{S^{-1}\}$  est l'anneau complet des fractions de A ayant leurs dénominateurs dans S. Avec les notations précédentes, il est clair que l'image réciproque de  $S^{-1}J_{\lambda}$  dans A contient  $J_{\lambda}$, donc l'application canonique  $A \to S^{-1}A$  est continue, et si on la compose avec l'application canonique  $S^{-1}A \to A\{S^{-1}\}$, on obtient un homomorphisme canonique continu  $A \to A\{S^{-1}\}$, limite projective des homomorphismes  $A \to S_{\lambda}^{-1}A_{\lambda}$.

(7.6.6) Le couple formé de $\mathbf{A}\{\mathbf{S}^{-1}\}$ et de l'application canonique $\mathbf{A}\to\mathbf{A}\{\mathbf{S}^{-1}\}$ est caractérisé par la propriété universelle suivante : tout homomorphisme continu $u$ de $\mathbf{A}$ dans un anneau linéairement topologisé $\mathbf{B}$, séparé et complet, tel que $u(\mathbf{S})$ soit formé d'éléments inversibles dans $\mathbf{B}$, se factorise d'une seule manière en $\mathbf{A}\to\mathbf{A}\{\mathbf{S}^{-1}\}\xrightarrow{u'}\mathbf{B}$, où $u'$ est continu. En effet, $u$ se factorise d'une seule manière en $\mathbf{A}\to\mathbf{S}^{-1}\mathbf{A}\xrightarrow{v'}\mathbf{B}$; comme pour tout idéal ouvert $\Re$ de $\mathbf{B}$, $u^{-1}(\Re)$ contient un $\Im_{\lambda}, v'^{-1}(\Re)$ contient nécessairement $\mathbf{S}^{-1}\Im_{\lambda}$, donc $v'$ est continu ; puisque $\mathbf{B}$ est séparé et complet, $v'$ se factorise d'une seule manière en $\mathbf{S}^{-1}\mathbf{A}\to\mathbf{A}\{\mathbf{S}^{-1}\}\xrightarrow{u'}\mathbf{B}$, où $u'$ est continu ; d'où notre assertion.

(7.6.7) Soient B un second anneau linéairement topologisé, T une partie multiplicative de B, $\varphi: A \to B$ un homomorphisme continu tel que $\varphi(S) \subset T$. D'après ce qui précède, l'homomorphisme continu $A \xrightarrow{\varphi} B \to B \{T^{-1}\}$ se factorise de façon unique en $A \to A \{S^{-1}\} \xrightarrow{\varphi'} B \{T^{-1}\}$, où $\varphi'$ est continu. En particulier, si $B = A$ et si $\varphi$ est l'identité, on voit que pour $S \subset T$ on a un homomorphisme continu $\rho^{T,S}: A \{S^{-1}\} \to A \{T^{-1}\}$ obtenu par passage au séparé complété à partir de $S^{-1}A \to T^{-1}A$; si U est une troisième partie multiplicative de A telle que $S \subset T \subset U$, on a $\rho^{U,S} = \rho^{U,T_{o}} \rho^{T,S}$.

(7.6.8) Soient  $S_{1}$ ,  $S_{2}$  deux parties multiplicatives de A, et soit  $S_{2}^{\prime}$  l'image canonique de  $S_{2}$  dans  $A\{S_{1}^{-1}\}$ ; on a alors un isomorphisme topologique canonique  $A\{(S_{1}S_{2})^{-1}\}\simeq A\{S_{1}^{-1}\}\{S_{2}^{\prime}-1\}$ , comme on le voit en partant de l'isomorphisme canonique  $(S_{1}S_{2})^{-1}A\simeq S_{2}^{\prime\prime-1}(S_{1}^{-1}A)$  (où  $S_{2}^{\prime\prime}$  est l'image canonique de  $S_{2}$  dans  $S_{1}^{-1}A$ ), qui est bicontinu.

(7.6.9) Soit a un idéal ouvert de A ; on peut supposer que $\mathfrak{J}_{\lambda} \subset \mathfrak{a}$ pour tout $\lambda$, et par suite $S^{-1}\mathfrak{J}_{\lambda} \subset S^{-1}\mathfrak{a}$ dans l'anneau $S^{-1}\mathbf{A}$, autrement dit, $S^{-1}\mathfrak{a}$ est un idéal ouvert de $S^{-1}\mathbf{A}$; nous désignerons par $\mathfrak{a}\{S^{-1}\}$ son séparé complété, égal à $\varprojlim (S^{-1}\mathfrak{a}/S^{-1}\mathfrak{J}_{\lambda})$, qui est un idéal ouvert de $A\{S^{-1}\}$, isomorphe à l'adhérence de l'image canonique de $S^{-1}\mathfrak{a}$. En outre, l'anneau discret $A\{S^{-1}\}/\mathfrak{a}\{S^{-1}\}$ est canoniquement isomorphe à $S^{-1}A/S^{-1}\mathfrak{a}=S^{-1}(A/\mathfrak{a})$. Inversement, si $\mathfrak{a}'$ est un idéal ouvert de $A\{S^{-1}\}$, $\mathfrak{a}'$ contient un idéal de la forme $\mathfrak{J}_{\lambda}\{S^{-1}\}$, donc est l'image réciproque d'un idéal de $S^{-1}A/S^{-1}\mathfrak{J}_{\lambda}$, qui est nécessairement (1.2.6) de la forme $S^{-1}\mathfrak{a}$, où $\mathfrak{a} \supset J_{\lambda}$. On en conclut que l'on a $\mathfrak{a}'=\mathfrak{a}\{S^{-1}\}$. En particulier (1.2.6):

Proposition (7.6.10). — L'application  $p \to p\{S^{-1}\}$  est une bijection croissante de l'ensemble des idéaux premiers ouverts p de A tels que  $p \cap S = \emptyset$  sur l'ensemble des idéaux premiers ouverts

de $\mathrm{A}\{\mathrm{S}^{-1}\}$; en outre, le corps des fractions de $\mathrm{A}\{\mathrm{S}^{-1}\}/\mathfrak{p}\{\mathrm{S}^{-1}\}$ est canoniquement isomorphe à celui de $\mathrm{A}/\mathfrak{p}$.

Proposition (7.6.11). — (i) Si A est un anneau admissible, il en est de même de  $A' = A\{S^{-1}\}$  et pour tout idéal de définition J de A,  $J' = J\{S^{-1}\}$  est un idéal de définition de  $A'$ .

(ii) Soient A un anneau adique, J un idéal de définition de A tel que $\mathfrak{J}/\mathfrak{J}^{2}$ soit de type fini sur A/$\mathfrak{J}$; alors A' est un anneau $\mathfrak{J}'$-adique et $\mathfrak{J}'/\mathfrak{J}'^{2}$ est de type fini sur A'/$\mathfrak{J}'$. Si en outre A est noethérien, il en est de même de A'.

(i) Si $\mathfrak{J}$ est un idéal de définition dans A, il est clair que $S^{-1}\mathfrak{J}$ est un idéal de définition dans l'anneau topologique $S^{-1}A$, car on a $(S^{-1}\mathfrak{J})^n = S^{-1}\mathfrak{J}^n$. Soit $A''$ l'anneau séparé associé à $S^{-1}A$, $\mathfrak{J}''$ l'image de $S^{-1}\mathfrak{J}$ dans $A''$; l'image de $S^{-1}\mathfrak{J}^n$ est $\mathfrak{J}''^n$, donc $\mathfrak{J}''^n$ tend vers o dans $A''$; comme $\mathfrak{J}'$ est l'adhérence de $\mathfrak{J}''$ dans $A'$, $\mathfrak{J}'^n$ est contenu dans l'adhérence de $\mathfrak{J}''^n$, donc tend vers o dans $A'$.

(ii) Posons  $A_{i}=A/J^{i+1}$ , et pour  $i\leqslant j$ , soit  $u_{ij}$  l'homomorphisme canonique  $A/J^{i+1}\to A/J^{i+1}$ ; soit  $S_{i}$  l'image canonique de S dans  $A_{i}$ , et posons  $A_{i}^{\prime}=S_{i}^{-1}A_{i}$ ; soit enfin  $u_{ij}^{\prime}:A_{j}^{\prime}\to A_{i}^{\prime}$  l'homomorphisme déduit canoniquement de  $u_{ij}$ . Montrons que le système projectif  $(A_{i}^{\prime},u_{ij}^{\prime})$  vérifie les conditions de la prop. (7.2.7): il est clair que les  $u_{ij}^{\prime}$  sont surjectifs; d'autre part, le noyau de  $u_{ij}^{\prime}$  est  $S_{j}^{-1}(J^{i+1}/J^{j+1})$  (1.3.2), égal à  $J_{j}^{\prime i+1}$ , où  $J_{j}^{\prime}=S_{j}^{-1}(J/J^{j+1})$ ; enfin,  $J_{1}^{\prime}/J_{1}^{\prime2}=S_{1}^{-1}(J/J^{2})$ , et comme  $J/J^{2}$  est de type fini sur  $A/J^{2}$ ,  $J_{1}^{\prime}/J_{1}^{\prime2}$  est de type fini sur  $A_{1}^{\prime}$ . Enfin, si A est noethérien, il en est de même de  $A_{0}^{\prime}=S_{0}^{-1}(A/J)$ , ce qui achève de démontrer la proposition (7.2.8).

Corollaire (7.6.12). — Sous les hypothèses de (7.6.11, (ii)), on a $(\Im \{S^{-1}\})^n = \Im^n \{S^{-1}\}$.

Cela résulte en effet de (7.2.7) et de la démonstration de (7.6.11).

Proposition (7.6.13). — Soient A un anneau adique noethérien, S une partie multiplicative de A ; alors A{S$^{-1}$} est un A-module plat.

En effet, si $\mathfrak{J}$ est un idéal de définition de A, $\mathrm{A}\{\mathrm{S}^{-1}\}$ est le séparé complété de l'anneau noethérien $\mathrm{S}^{-1}\mathrm{A}$ muni de la topologie $\mathrm{S}^{-1}\mathfrak{J}$-préadique; par suite (7.3.3) $\mathrm{A}\{\mathrm{S}^{-1}\}$ est un $\mathrm{S}^{-1}\mathrm{A}$-module plat; comme $\mathrm{S}^{-1}\mathrm{A}$ est un A-module plat (6.3.1), la proposition résulte de la transitivité de la platitude (6.2.1).

Corollaire (7.6.14). — Sous les hypothèses de (7.6.13), soit S'⊂S une seconde partie multiplicative de A ; alors A{S$^{-1}$} est un A{S'$^{-1}$}-module plat.

En effet (7.6.8), $\mathrm{A}\{\mathrm{S}^{-1}\}$ s'identifie canoniquement à $\mathrm{A}\{\mathrm{S}'^{-1}\}\{\mathrm{S}_0^{-1}\}$, où $\mathrm{S}_0$ est l'image canonique de S dans $\mathrm{A}\{\mathrm{S}'^{-1}\}$, et $\mathrm{A}\{\mathrm{S}'^{-1}\}$ est noethérien (7.6.11).

(7.6.15) Pour tout élément $f$ d'un anneau linéairement topologisé A, nous désignerons par $\mathbf{A}_{\{f\}}$ l'anneau complet de fractions $\mathbf{A}\{\mathrm{S}_{f}^{-1}\}$, où $\mathrm{S}_{f}$ est l'ensemble multiplicatif des $f^{n}$ ($n\geqslant0$); pour tout idéal ouvert $\mathfrak{a}$ de A, nous écrirons $\mathfrak{a}_{\{f\}}$ au lieu de $\mathfrak{a}\{\mathrm{S}_{f}^{-1}\}$. Si $g$ est un second élément de A, on a un homomorphisme canonique continu $\mathbf{A}_{\{f\}}\to\mathbf{A}_{\{fg\}}$ (7.6.7). Lorsque $f$ parcourt une partie multiplicative S de A, les $\mathbf{A}_{\{f\}}$ forment donc un système inductif filtrant d'anneaux pour les homomorphismes précédents; nous poserons $\mathbf{A}_{\{\mathrm{S}\}}=\lim_{f\in\mathbb{S}}\mathbf{A}_{\{f\}}$. Pour tout $f\in\mathrm{S}$, on a un homomorphisme $\mathbf{A}_{\{f\}}\to\mathbf{A}\{\mathrm{S}^{-1}\}$ (7.6.7), et

ces homomorphismes forment un système inductif ; par passage à la limite inductive, ils définissent donc un homomorphisme canonique  $A_{\{S\}} \rightarrow A\{S^{-1}\}$ .

Proposition (7.6.16). — Si A est un anneau noethérien,  $A\{S^{-1}\}$  est un module plat sur  $A_{\{S\}}$ . En effet (7.6.14),  $A\{S^{-1}\}$  est plat sur chacun des anneaux  $A_{\{f\}}$  pour  $f \in S$ , et la conclusion résulte de (6.2.3).

Proposition (7.6.17). — Soit p un idéal premier ouvert dans un anneau admissible A, et soit S = A — p. Alors les anneaux  $A\{S^{-1}\}$  et  $A_{\{S\}}$  sont des anneaux locaux, l'homomorphisme canonique  $A_{\{S\}} \to A\{S^{-1}\}$  est local et les corps résiduels de  $A_{\{S\}}$  et  $A\{S^{-1}\}$  sont canoniquement isomorphes au corps des fractions de A/p.

En effet, soit $\mathfrak{J} \subset \mathfrak{p}$ un idéal de définition de A; on a $S^{-1}\mathfrak{J} \subset S^{-1}\mathfrak{p} = \mathfrak{p}A_{\mathfrak{p}}$, donc $A_{\mathfrak{p}} / S^{-1}\mathfrak{J}$ est un anneau local; on conclut de (7.1.12), (7.6.9) et (7.6.11, (i)) que $A\{S^{-1}\}$ est un anneau local. Posons $\mathfrak{m} = \varinjlim_{f \in S} \mathfrak{p}_{\{f\}}$, qui est un idéal de $A_{\{S\}}$; nous allons voir

que tout élément de $\mathbf{A}_{\{\mathbb{S}\}}$ n'appartenant pas à $m$ est inversible. En effet, un tel élément est l'image dans $\mathbf{A}_{\{\mathbb{S}\}}$ d'un élément $z \in \mathbf{A}_{\{f\}}$ n'appartenant pas à $\mathfrak{p}_{\{f\}}$, pour un $f \in S$; son image canonique $z_0$ dans $\mathbf{A}_{\{f\}} / \mathfrak{J}_{\{f\}} = \mathrm{S}_f^{-1}(\mathrm{A} / \mathfrak{J})$ n'appartient donc pas à $\mathrm{S}_f^{-1}(\mathfrak{p} / \mathfrak{J})$ (7.6.9), ce qui signifie que $z_0 = \bar{x} / \bar{f}^k$, où $x \notin \mathfrak{p}$ et $\bar{x}, \bar{f}$ sont les classes de $x, f$ mod. $\mathfrak{J}$. Comme $x \in S$, on a $g = xf \in S$, et dans $\mathrm{S}_g^{-1}\mathrm{A}$, $y_0 = x^{k+1} / g^k$, image canonique de $x / f^k \in \mathrm{S}_f^{-1}\mathrm{A}$, admet un inverse $x^{k-1} f^{2k} / g^k$. Cela entraîne a fortiori que l'image de $y_0$ dans $\mathrm{S}_g^{-1}\mathrm{A} / \mathrm{S}_g^{-1}\mathfrak{J}$ est inversible, donc (7.6.9 et 7.1.12) l'image canonique $y$ de $z$ dans $\mathbf{A}_{\{g\}}$ est inversible; l'image de $z$ dans $\mathbf{A}_{\{\mathbb{S}\}}$ (égale à celle de $y$) est par suite inversible. On voit donc que $\mathbf{A}_{\{\mathbb{S}\}}$ est un anneau local d'idéal maximal $m$; en outre, l'image de $\mathfrak{p}_{\{f\}}$ dans $\mathrm{A}\{\mathrm{S}^{-1}\}$ est contenue dans l'idéal maximal $\mathfrak{p}\{\mathrm{S}^{-1}\}$ de cet anneau; a fortiori, l'image de $m$ dans $\mathrm{A}\{\mathrm{S}^{-1}\}$ est contenue dans $\mathfrak{p}\{\mathrm{S}^{-1}\}$, donc l'homomorphisme canonique $\mathbf{A}_{\{\mathbb{S}\}} \to \mathbf{A}\{\mathrm{S}^{-1}\}$ est local. Enfin, comme tout élément de $\mathrm{A}\{\mathrm{S}^{-1}\} / \mathfrak{p}\{\mathrm{S}^{-1}\}$ est image d'un élément d'un anneau $\mathrm{S}_f^{-1}\mathrm{A}$ pour un $f \in S$ convenable, l'homomorphisme $\mathbf{A}_{\{\mathbb{S}\}} \to \mathbf{A}\{\mathrm{S}^{-1}\} / \mathfrak{p}\{\mathrm{S}^{-1}\}$ est surjectif, et donne donc par passage aux quotients un isomorphisme des corps résiduels.

Corollaire (7.6.18). — Sous les hypothèses de (7.6.17), si on suppose de plus que A est un anneau adique noethérien, les anneaux locaux  $A\{S^{-1}\}$  et  $A_{\{S\}}$  sont noethériens, et  $A\{S^{-1}\}$  est un  $A_{\{S\}}$ -module fidèlement plat.

On sait déjà (7.6.11, (ii)) que  $A\{S^{-1}\}$  est noethérien et  $A_{\{S\}}$ -plat (7.6.16); comme l'homomorphisme  $A_{\{S\}} \to A\{S^{-1}\}$  est local, on en conclut que  $A\{S^{-1}\}$  est un  $A_{\{S\}}$ -module fidèlement plat (6.6.2), et par suite que  $A_{\{S\}}$  est noethérien (6.5.2).

## 7.7. Produits tensoriels complétés.

(7.7.1) Soient A un anneau linéairement topologisé, M, N, deux A-modules linéairement topologisés. Soient J, V, W des voisinages ouverts de o dans A, M, N respectivement, qui soient des A-modules, et tels que J.M⊂V, J.N⊂W, de sorte que M/V et N/W peuvent être considérés comme des (A/J)-modules. Lorsque J, V, W parcourent les systèmes de voisinages ouverts vérifiant les conditions précédentes, il est immédiat que les modules (M/V)⊗$_{A/J}$(N/W) forment un système projectif de modules

sur le système projectif d'anneaux A/ $\mathfrak{J}$ ; par passage à la limite projective, on en déduit donc un module sur le séparé complété $\hat{A}$ de A, que l'on appelle le produit tensoriel complété de M et de N et que l'on note $(M\otimes_{A}N)^{\wedge}$. Si l'on remarque que M/V est canoniquement isomorphe à $\hat{M}/\overline{V}$, où $\hat{M}$ est le séparé complété de M et $\overline{V}$ l'adhérence dans $\hat{M}$ de l'image de V, on voit que le produit tensoriel complété $(M\otimes_{A}N)^{\wedge}$ s'identifie canoniquement à $(\hat{M}\otimes_{\hat{A}}\hat{N})^{\wedge}$, que l'on note aussi $\hat{M}\hat{\otimes}_{\hat{A}}\hat{N}$.

(7.7.2) Avec les notations précédentes, les produits tensoriels  $(\mathbf{M}/\mathbf{V})\otimes_{\mathbf{A}}(\mathbf{N}/\mathbf{W})$  et  $(\mathbf{M}/\mathbf{V})\otimes_{\mathbf{A}/\mathfrak{I}}(\mathbf{N}/\mathbf{W})$  s'identifient canoniquement; ils s'identifient donc aussi à  $(\mathbf{M}\otimes_{\mathbf{A}}\mathbf{N})/(\operatorname{Im}(\mathbf{V}\otimes_{\mathbf{A}}\mathbf{N})+\operatorname{Im}(\mathbf{M}\otimes_{\mathbf{A}}\mathbf{W}))$ . On en conclut que  $(\mathbf{M}\otimes_{\mathbf{A}}\mathbf{N})^{\wedge}$  est le séparé complété du A-module  $M\otimes_{A}N$ , muni de la topologie pour laquelle les sous-modules

$$
\operatorname{Im} \left(\mathbf {V} \otimes_ {\mathbf {A}} \mathbf {N}\right) + \operatorname{Im} \left(\mathbf {M} \otimes_ {\mathbf {A}} \mathbf {W}\right)
$$

forment un système fondamental de voisinages de o (V et W parcourant l'ensemble des sous-modules ouverts de M et N respectivement) ; nous dirons pour abréger que cette topologie est le produit tensoriel des topologies données sur M et N.

(7.7.3) Soient M', N' deux A-modules linéairement topologisés, $u: \mathbf{M} \to \mathbf{M}'$, $v: \mathbf{N} \to \mathbf{N}'$ deux homomorphismes continus; il est immédiat que $u \otimes v$ est continu pour les topologies produits tensoriels sur $\mathbf{M} \otimes \mathbf{N}$ et $\mathbf{M}' \otimes \mathbf{N}'$ respectivement; par passage au séparé complété, on en déduit un homomorphisme continu $(\mathbf{M} \otimes \mathbf{N})^{\wedge} \to (\mathbf{M}' \otimes \mathbf{N}')^{\wedge}$, que nous désignerons par $u \widehat{\otimes} v$; $(\mathbf{M} \otimes_{\mathbf{A}} \mathbf{N})^{\wedge}$ est donc un bifoncteur en M et N dans la catégorie des A-modules linéairement topologisés.

(7.7.4) On définit de même le produit tensoriel complété d'un nombre fini quelconque de A-modules linéairement topologisés ; il est immédiat que ce produit possède les propriétés usuelles d'associativité et de commutativité.

(7.7.5) Si B, C sont deux A-algèbres topologiques linéairement topologisées, la topologie produit tensoriel sur  $B \otimes_{A} C$  a pour système fondamental de voisinages de o les idéaux  $\operatorname{Im}(\mathfrak{R} \otimes_{A} C) + \operatorname{Im}(B \otimes_{A} \mathfrak{L})$  de l'algèbre  $B \otimes_{A} C$,  $\mathfrak{R}$  (resp. L) parcourant l'ensemble des idéaux ouverts de B (resp. C). Par suite,  $(\mathrm{B} \otimes_{\mathrm{A}} \mathrm{C})^{\wedge}$  est muni d'une structure de  $\hat{A}$ -algèbre topologique, limite projective du système projectif de  $(\mathrm{A}/\mathfrak{J})$ -algèbres  $(\mathrm{B}/\mathfrak{R}) \otimes_{\mathrm{A}/\mathfrak{J}} (\mathrm{C}/\mathfrak{L})$  (J idéal ouvert de A tel que J.B⊂K, J.C⊂L; il en existe toujours). On dit que cette algèbre est le produit tensoriel complété des algèbres B et C.

(7.7.6) Les homomorphismes de A-algèbres $b \to b \otimes \mathrm{I}$, $c \to \mathrm{I} \otimes c$ de B et C dans $\mathrm{B} \otimes_{\mathrm{A}} \mathrm{C}$ sont continus quand on munit cette dernière algèbre de la topologie produit tensoriel ; par composition avec l'homomorphisme canonique de $\mathrm{B} \otimes_{\mathrm{A}} \mathrm{C}$ dans son séparé complété, ils donnent donc des homomorphismes canoniques $\rho : \mathrm{B} \to (\mathrm{B} \otimes_{\mathrm{A}} \mathrm{C})^{\wedge}$, $\sigma : \mathrm{C} \to (\mathrm{B} \otimes_{\mathrm{A}} \mathrm{C})^{\wedge}$. L'algèbre $(\mathrm{B} \otimes_{\mathrm{A}} \mathrm{C})^{\wedge}$ et les homomorphismes $\rho$ et $\sigma$ possèdent en outre la propriété universelle suivante ; pour toute A-algèbre linéairement topologisée, séparée et complète D, et tout couple de A-homomorphismes continus $u : \mathrm{B} \to \mathrm{D}$, $v : \mathrm{C} \to \mathrm{D}$, il existe un A-homomorphisme continu et un seul $w : (\mathrm{B} \otimes_{\mathrm{A}} \mathrm{C})^{\wedge} \to \mathrm{D}$ et un seul tel que $u = w \circ \rho$ et $v = w \circ \sigma$. En effet, il existe déjà un A-homomorphisme unique $w_0 : \mathrm{B} \otimes_{\mathrm{A}} \mathrm{C} \to \mathrm{D}$ tel que $u(b) = w_0 (b \otimes \mathrm{I})$ et $v(c) = w_0 (\mathrm{I} \otimes c)$, et tout revient à prouver que $w_0$ est continu, car il donnera alors un

homomorphisme continu $w$ par passage au séparé complété. Or, si $\mathfrak{M}$ est un idéal ouvert de D, il existe par hypothèse des idéaux ouverts $\mathfrak{R} \subset B$, $\mathfrak{L} \subset C$ tels que $u(\mathfrak{R}) \subset \mathfrak{M}$, $v(\mathfrak{L}) \subset \mathfrak{M}$; l'image par $w_0$ de $\operatorname{Im}(\mathfrak{R} \otimes \mathbf{C}) + \operatorname{Im}(\mathbf{B} \otimes \mathfrak{L})$ est encore contenue dans $\mathfrak{M}$, d'où notre assertion.

Proposition (7.7.7). — Si B et C sont deux A-algèbres préadmissibles,  $(\mathbf{B}\otimes_{\mathbf{A}}\mathbf{C})^{\wedge}$  est admissible, et si R (resp. L) est un idéal de définition de B (resp. C), l'adhérence dans  $(\mathbf{B}\otimes_{\mathbf{A}}\mathbf{C})^{\wedge}$  de l'image canonique de  $\mathfrak{H}=\operatorname{Im}(\mathfrak{R}\otimes\mathbf{C})+\operatorname{Im}(\mathbf{B}\otimes\mathfrak{L})$  est un idéal de définition.

Il suffit de montrer que $\mathfrak{H}^n$ tend vers o pour la topologie produit tensoriel, ce qui résulte immédiatement de l'inclusion

$$
\mathfrak {H} ^ {2 n} \subset \operatorname{Im} (\mathfrak {R} ^ {n} \otimes \mathrm{C}) + \operatorname{Im} (\mathrm{B} \otimes \mathfrak {L} ^ {n})
$$

Proposition (7.7.8). — Soient A un anneau préadique, J un idéal de définition de A, M un A-module de type fini, muni de la topologie J-préadique. Pour toute A-algèbre topologique adique et noethérienne B, B⊗$_{A}$M s'identifie au produit tensoriel complété (B⊗$_{A}$M)^.

Si $\mathfrak{K}$ est un idéal de définition de B, il existe par hypothèse un entier $m$ tel que $\mathfrak{J}^{m}\mathrm{B}\subset\mathfrak{K}$, donc $\operatorname{Im}(\mathrm{B}\otimes_{\mathrm{A}}\mathfrak{J}^{nm}\mathrm{M})=\operatorname{Im}(\mathfrak{J}^{nm}\mathrm{B}\otimes_{\mathrm{A}}\mathrm{M})\subset\operatorname{Im}(\mathfrak{K}^{n}\mathrm{B}\otimes_{\mathrm{A}}\mathrm{M})=\mathfrak{K}^{n}(\mathrm{B}\otimes_{\mathrm{A}}\mathrm{M})$; on en conclut que sur $\mathrm{B}\otimes_{\mathrm{A}}\mathrm{M}$, le produit tensoriel des topologies de B et de M est la topologie $\mathfrak{K}$-préadique. Comme $\mathrm{B}\otimes_{\mathrm{A}}\mathrm{M}$ est un B-module de type fini, la proposition résulte aussitôt de (7.3.6).

## 7.8. Topologies sur les modules d'homomorphismes.

(7.8.1) Soient A un anneau $\mathfrak{J}$-adique noethérien, M et N deux A-modules de type fini, munis de la topologie $\mathfrak{J}$-préadique ; on sait (7.3.6) qu'ils sont séparés et complets ; en outre, tout A-homomorphisme $\mathrm{M} \to \mathrm{N}$ est automatiquement continu, et le A-module $\mathrm{Hom}_{\mathrm{A}}(\mathrm{M}, \mathrm{N})$ est de type fini. Pour tout entier $i \geqslant 0$, posons $\mathrm{A}_i = \mathrm{A} / \mathfrak{J}^{i+1}$, $\mathrm{M}_i = \mathrm{M} / \mathfrak{J}^{i+1}\mathrm{M}$, $\mathrm{N}_i = \mathrm{N} / \mathfrak{J}^{i+1}\mathrm{N}$; pour $i \leqslant j$, tout homomorphisme $u_j: \mathrm{M}_j \to \mathrm{N}_j$ applique $\mathfrak{J}^{i+1}\mathrm{M}_j$ dans $\mathfrak{J}^{i+1}\mathrm{N}_j$, donc donne par passage aux quotients un homomorphisme $u_i: \mathrm{M}_i \to \mathrm{N}_i$, ce qui définit un homomorphisme canonique $\mathrm{Hom}_{\mathrm{A}_j}(\mathrm{M}_j, \mathrm{N}_j) \to \mathrm{Hom}_{\mathrm{A}_i}(\mathrm{M}_i, \mathrm{N}_i)$; en outre, les $\mathrm{Hom}_{\mathrm{A}_i}(\mathrm{M}_i, \mathrm{N}_i)$ constituent un système projectif pour ces homomorphismes, et il résulte de (7.2.10) qu'il y a un isomorphisme canonique $\varphi: \mathrm{Hom}_{\mathrm{A}}(\mathrm{M}, \mathrm{N}) \to \varprojlim_{i} \mathrm{Hom}_{\mathrm{A}_i}(\mathrm{M}_i, \mathrm{N}_i)$. En outre :

Proposition (7.8.2). — Si M et N sont des modules de type fini sur un anneau J-adique noethérien A, les sous-modules  $\mathrm{Hom}_{\mathrm{A}}(\mathrm{M}, \mathfrak{J}^{i+1}\mathrm{N})$  forment un système fondamental de voisinages de o dans  $\mathrm{Hom}_{\mathrm{A}}(\mathrm{M}, \mathrm{N})$  pour la topologie J-adique, et l'homomorphisme canonique  $\varphi : \mathrm{Hom}_{\mathrm{A}}(\mathrm{M}, \mathrm{N}) \to \varprojlim_{i} \mathrm{Hom}_{\mathrm{A}_i}(\mathrm{M}_i, \mathrm{N}_i)$  est un isomorphisme topologique.

On peut en effet considérer M comme quotient d'un A-module libre L de type fini, et par suite identifier  $\mathrm{Hom}_{\mathrm{A}}(\mathrm{M},\mathrm{N})$  à un sous-module de  $\mathrm{Hom}_{\mathrm{A}}(\mathrm{L},\mathrm{N})$ ; dans cette identification,  $\mathrm{Hom}_{\mathrm{A}}(\mathrm{M},\mathfrak{J}^{i+1}\mathrm{N})$  est l'intersection de  $\mathrm{Hom}_{\mathrm{A}}(\mathrm{M},\mathrm{N})$  et de  $\mathrm{Hom}_{\mathrm{A}}(\mathrm{L},\mathfrak{J}^{i+1}\mathrm{N})$ ; comme la topologie induite sur  $\mathrm{Hom}_{\mathrm{A}}(\mathrm{M},\mathrm{N})$  par la topologie J-adique de  $\mathrm{Hom}_{\mathrm{A}}(\mathrm{L},\mathrm{N})$  est la topologie J-adique (7.3.2), on est ramené à démontrer la première assertion

pour $\mathbf{M} = \mathbf{L} = \mathbf{A}^m$; mais alors $\mathrm{Hom}_{\mathrm{A}}(\mathbf{L},\mathbf{N}) = \mathbf{N}^{m}$, $\mathrm{Hom}_{\mathrm{A}}(\mathbf{L},\mathfrak{J}^{i + 1}\mathbf{N}) = (\mathfrak{J}^{i + 1}\mathbf{N})^{m} = \mathfrak{J}^{i + 1}\mathbf{N}^{m}$ et le résultat est évident. Pour établir la seconde assertion, notons que l'image de $\mathrm{Hom}_{\mathrm{A}}(\mathbf{M},\mathfrak{J}^{i + 1}\mathbf{N})$ dans $\mathrm{Hom}_{\mathrm{A}_j}(\mathbf{M}_j,\mathbf{N}_j)$ est nulle pour $j\leqslant i$, donc $\varphi$ est continu; inversement, l'image réciproque dans $\mathrm{Hom}_{\mathrm{A}}(\mathbf{M},\mathbf{N})$ du 0 de $\mathrm{Hom}_{\mathrm{A}_i}(\mathbf{M}_i,\mathbf{N}_i)$ est $\mathrm{Hom}_{\mathrm{A}}(\mathbf{M},\mathfrak{J}^{i + 1}\mathbf{N})$, donc $\varphi$ est bicontinu.

Si on suppose seulement que A est un anneau $\mathfrak{J}$-préadique noethérien, M et N deux A-modules de type fini, séparés pour la topologie $\mathfrak{J}$-préadique, la démonstration précédente montre que la première assertion de (7.8.2) reste valable, et que $\varphi$ est un isomorphisme topologique de $\mathrm{Hom}_{\mathrm{A}}(\mathrm{M}, \mathrm{N})$ sur un sous-module de $\lim \mathrm{Hom}_{\mathrm{A}_i}(\mathrm{M}_i, \mathrm{N}_i)$.

Proposition (7.8.3). — Sous les hypothèses de (7.8.2), l'ensemble des homomorphismes injectifs (resp. surjectifs, bijectifs) de M dans N est une partie ouverte de Hom$_{A}$(M, N).

En effet, en vertu de (7.3.5) et (7.1.14), pour que $u$ soit surjectif, il faut et il suffit que l'homomorphisme correspondant $u_0: \mathbf{M} / \mathfrak{J}\mathbf{M} \to \mathbf{N} / \mathfrak{J}\mathbf{N}$ le soit, et l'ensemble des homomorphismes surjectifs de $\mathbf{M}$ dans $\mathbf{N}$ est donc image réciproque par l'application continue $\mathrm{Hom}_{\mathbf{A}}(\mathbf{M}, \mathbf{N}) \to \mathrm{Hom}_{\mathbf{A}_0}(\mathbf{M}_0, \mathbf{N}_0)$ d'une partie d'un espace discret. Montrons maintenant que l'ensemble des homomorphismes injectifs est ouvert; soit $v$ un tel homomorphisme et posons $\mathbf{M}' = v(\mathbf{M})$; par le lemme d'Artin-Rees (7.3.2.1), il existe un entier $k \geqslant 0$ tel que $\mathbf{M}' \cap \mathfrak{J}^{m+k}\mathbf{N} \subset \mathfrak{J}^m\mathbf{M}'$ pour tout $m > 0$; nous allons voir que pour $w \in \mathfrak{J}^{k+1}\mathrm{Hom}_{\mathbf{A}}(\mathbf{M}, \mathbf{N}), u = v + w$ est injectif, ce qui achèvera la démonstration. En effet, soit $x \in \mathbf{M}$ tel que $u(x) = 0$; prouvons que pour tout $i \geqslant 0$ la relation $x \in \mathfrak{J}^i\mathbf{M}$ implique $x \in \mathfrak{J}^{i+1}\mathbf{M}$; il en résultera bien $x \in \bigcap_{i \geqslant 0} \mathfrak{J}^i\mathbf{M} = (\mathbf{o})$. En effet, on a alors $w(x) \in \mathfrak{J}^{i+k+1}\mathbf{N}$, et par ailleurs $w(x) = -v(x) \in \mathbf{M}'$, donc $v(x) \in \mathbf{M}' \cap \mathfrak{J}^{i+k+1}\mathbf{N} \subset \mathfrak{J}^{i+1}\mathbf{M}'$, et comme $v$ est un isomorphisme de $\mathbf{M}$ sur $\mathbf{M}'$, $x \in \mathfrak{J}^{i+1}\mathbf{M}$; c.q.f.d.

(A suivre.)

# CHAPITRE PREMIER

# LE LANGAGE DES SCHÉMAS

## Sommaire

§ 1. Schémas affines.

§ 2. Préschémas et morphismes de préschémas.

§ 3. Produits de préschémas.

§ 4. Sous-préschémas et morphismes d'immersion.

§ 5. Préschémas réduits ; condition de séparation.

§ 6. Conditions de finitude.

§ 7. Applications rationnelles.

§ 8. Les schémas de Chevalley.

§ 9. Compléments sur les faisceaux quasi-cohérents.

§ 10. Schémas formels.

Les §§ 1 à 8 ne font guère que développer un langage, celui qui sera utilisé dans toute la suite. Notons cependant que, conformément à l'esprit général de ce Traité, les §§ 7 et 8 seront moins utilisés que les autres, et de façon moins essentielle; on n'a d'ailleurs parlé des schémas de Chevalley que pour faire le lien avec le langage de Chevalley [1] et Nagata [9]. Le § 9 donne des définitions et résultats sur les faisceaux quasi-cohérents, dont certains ne se bornent plus à une traduction en langage « géométrique » de notions connues d'Algèbre commutative, mais sont déjà de nature globale ; ils seront indispensables, dès les chapitres suivants, dans l'étude globale des morphismes. Enfin, le § 10 introduit une généralisation de la notion de schéma, qui nous servira d'intermédiaire au chapitre III pour formuler et démontrer de façon commode les résultats fondamentaux de l'étude cohomologique des morphismes propres ; par ailleurs, signalons que la notion de schéma formel semble indispensable pour exprimer certains faits de la « théorie des modules » (problèmes de classification des variétés algébriques). Les résultats du § 10 ne seront pas utilisés avant le § 3 du chapitre III et il est recommandé d'en omettre la lecture jusque-là.

## § 1. SCHÉMAS AFFINES

## 1.1. Le spectre premier d'un anneau.

(1.1.1) Notations : Soient A un anneau (commutatif), M un A-module. Dans ce chapitre et les suivants, nous utiliserons constamment les notations suivantes :

$\operatorname{Spec}(\mathbf{A}) = \text{ensemble des idéaux premiers de A, appelé aussi spectre premier de A ; pour un } x \in \mathbf{X} = \operatorname{Spec}(\mathbf{A})$, il sera souvent commode d'écrire $\mathbf{j}_x$ au lieu de $x$. Pour que $\operatorname{Spec}(\mathbf{A})$ soit vide, il faut et il suffit que l'anneau A soit réduit à o.

$A_{x}=A_{j_{x}}=anneau(local)des fractions S^{-1}A, \text{ où } S=A-j_{x}.$

$m_{x}=j_{x}A_{j_{x}}=ideal maximal de A_{x}.$

$\boldsymbol{k}(x)=\mathrm{A}_{x}/\mathrm{m}_{x}=corps\ résiduel\ de\ \mathrm{A}_{x},\ isomorphe\ canoniquement\ au\ corps\ des\ fractions\ de\ l'anneau\ intègre\ \mathrm{A}/\mathrm{j}_{x},\ auquel\ on\ l'identifie.$

$f(x) = \text{classe de } f \text{ mod. } \mathrm{j}_x$, dans $\mathrm{A} / \mathrm{j}_x \subset \mathbf{k}(x)$, pour $f \in \mathrm{A}$ et $x \in \mathrm{X}$. On dit encore que $f(x)$ est la valeur de $f$ au point $x \in \operatorname{Spec}(\mathrm{A})$; les relations $f(x) = 0$ et $f \in \mathrm{j}_x$ sont équivalentes.

$M_{x}=M\otimes_{A}A_{x}=module~des~fractions~à~dénominateurs~dans~A-j_{x}.$

$\mathfrak{r}(\mathbf{E}) = racine\ de\ l'ideal\ de\ A\ engendré\ par\ une\ partie\ E\ de\ A.$

$V(E) = ensemble \ des \ x \in X \ tels \ que \ E \subset j_x \ (ou \ encore \ ensemble \ des \ x \in X \ tels \ que \ f(x) = 0 \ pour \ tout \ f \in E), \ pour \ E \subset A. \ On \ a \ donc$

$$
\mathfrak {r} (\mathrm{E}) = \bigcap_ {\boldsymbol {x} \in \mathrm{V} (\mathrm{E})} \mathrm{i} _ {\boldsymbol {x}}\tag{\( (I.I.I.I) \}
$$

$\mathrm{V}(f) = \mathrm{V}(\{f\})$ pour $f \in \mathbf{A}$.

$\mathbf{D}(f) = \mathbf{X} - \mathbf{V}(f) = ensemble des x \in \mathbf{X} \quad où f(x) \neq 0.$

Proposition (1.1.2). — On a les propriétés suivantes :

(i) $\mathbf{V}(\mathbf{o}) = \mathbf{X},\mathbf{V}(\mathbf{i}) = \emptyset .$

(ii) La relation $\mathbf{E} \subset \mathbf{E}'$ entraîne $\mathbf{V}(\mathbf{E}) \supset \mathbf{V}(\mathbf{E}')$.

(iii) Pour toute famille $(\mathrm{E}_{\lambda})$ de parties de A, $\mathrm{V}(\bigcup_{2}\mathrm{E}_{\lambda}) = \mathrm{V}(\Sigma \mathrm{E}_{\lambda}) = \bigcap_{2}\mathrm{V}(\mathrm{E}_{\lambda}).$

(iv) $\mathbf{V}(\mathbf{EE}') = \mathbf{V}(\mathbf{E}) \cup \mathbf{V}(\mathbf{E}')$.

(v)  $\mathbf{V}(\mathbf{E})=\mathbf{V}(\mathbf{r}(\mathbf{E}))$ .

Les propriétés (i), (ii), (iii) sont triviales, et (v) résulte de (ii) et de la formule (I.I.I.I). Il est évident que  $\mathrm{V}(\mathrm{EE}') \supset \mathrm{V}(\mathrm{E}) \cup \mathrm{V}(\mathrm{E}')$ ; inversement, si  $x \notin \mathrm{V}(\mathrm{E})$  et  $x \notin \mathrm{V}(\mathrm{E}')$ , il existe  $f \in E$  et  $f' \in E'$  tels que  $f(x) \neq o$  et  $f'(x) \neq o$  dans  $\boldsymbol{k}(x)$ , d'où  $f(x)f'(x) \neq o$ , autrement dit  $x \notin \mathrm{V}(\mathrm{EE}')$ , ce qui prouve (iv).

La prop. (1.1.2) montre entre autres que les ensembles de la forme V(E) (où E parcourt l'ensemble des parties de A) sont les ensembles fermés d'une topologie sur X, que nous appellerons la topologie spectrale (1); sauf mention expresse du contraire, on supposera toujours X=Spec(A) muni de la topologie spectrale.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">X.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) L'introduction de cette topologie en géométrie algébrique est due à Zariski. Aussi est-elle souvent appelée la « topologie de Zariski » de X.</span></small>

(1.1.3) Pour toute partie Y de X, nous désignerons par j(Y) l'ensemble des $f\in A$ tels que $f(y)=0$ pour tout $y\in Y$; il revient au même de dire que j(Y) est l'intersection des idéaux premiers $j_y$ pour $y\in Y$. Il est clair que la relation $Y\subset Y'$ entraîne $j(Y)\supset j(Y')$ et que l'on a

$$
\mathrm{i} (\bigcup_ {\lambda} \mathrm{Y} _ {\lambda}) = \bigcap_ {\lambda} \mathrm{i} (\mathrm{Y} _ {\lambda})\tag{Ⅰ.Ⅱ.3.Ⅱ}
$$

pour toute famille  $(Y_{\lambda})$  de parties de X. Enfin on a

$$
\mathrm{i} (\{x \}) = \mathrm{i} _ {x}.\tag{Ⅰ.Ⅰ.3.2}
$$

Proposition (1.1.4). — (i) Pour toute partie E de A, on a j(V(E)) = r(E).

(ii) Pour toute partie Y de X, V(j(Y))= $\overline{Y}$ , adhérence de Y dans X.

(i) est conséquence immédiate des définitions et de (i.i.i.i); d'autre part,  $V(j(Y))$  est fermé et contient Y; inversement, si  $Y \subset V(E)$ , on a  $f(y) = 0$  pour tout  $f \in E$  et tout  $y \in Y$ , donc  $E \subset j(Y)$ ,  $V(E) \supset V(j(Y))$ , ce qui prouve (ii).

Corollaire (1.1.5). — Les parties fermées de X=Spec(A) et les idéaux de A égaux à leurs racines (autrement dit les intersections d'idéaux premiers) se correspondent biunivoquement par les applications décroissantes Y→j(Y), a→V(a); à la réunion Y₁∪Y₂ de deux parties fermées correspond j(Y₁)∩j(Y₂), et à l'intersection d'une famille quelconque (Yλ) de parties fermées correspond la racine de la somme des j(Yλ).

Corollaire (1.1.6). — Si A est un anneau noethérien, X=Spec(A) est un espace noethérien.

On notera que la réciproque de ce corollaire est inexacte, comme le montre l'exemple d'un anneau intègre non noethérien ayant un seul idéal premier  $\neq\{0\}$ , par exemple un anneau de valuation non discrète de rang 1.

Comme exemple d'anneau A dont le spectre n'est pas un espace noethérien, on peut signaler l'anneau $\mathcal{C}(Y)$ des fonctions continues numériques sur un espace compact infini Y ; on sait qu'en tant qu'ensemble, Y s'identifie à l'ensemble des idéaux maximaux de A, et il est facile de voir que la topologie induite sur Y par celle de $X = \text{Spec}(A)$ est la topologie initiale de Y. Comme Y n'est pas un espace noethérien, il en est donc de même de X.

Corollaire (1.1.7). — Pour tout  $x \in X$ , l'adhérence de  $\{x\}$  est l'ensemble des  $y \in X$  tels que  $j_{x} \subset j_{y}$ . Pour que  $\{x\}$  soit fermé, il faut et il suffit que  $j_{x}$  soit maximal.

Corollaire (1.1.8). — L'espace X=Spec(A) est un espace de Kolmogoroff.

En effet, si $x$, $y$ sont deux points distincts de X, on a, soit $\mathbf{j}_{x} \subset \mathbf{j}_{y}$, soit $\mathbf{j}_{y} \subset \mathbf{j}_{x}$, donc l'un des points $x$, $y$ n'appartient pas à l'adhérence de l'autre.

(1.1.9) D'après la prop. (1.1.2, (iv)), pour deux éléments $f$, $g$ de A, on a

$$
\mathrm{D} (f g) = \mathrm{D} (f) \cap \mathrm{D} (g)\tag{ⅰ.ⅰ.9.ⅰ}
$$

Notons aussi que la relation  $\mathbf{D}(f)=\mathbf{D}(g)$  signifie, d'après la prop. (i.1.4, (i)) et la prop. (i.1.2, (v)) que  $\mathfrak{r}(f)=\mathfrak{r}(g)$ , ou encore que les idéaux premiers minimaux contenant (f) et (g) sont les mêmes; en particulier, il en est ainsi lorsque f=ug, où u est inversible.

Proposition (I.I.10). — (i) Lorsque f parcourt A, les ensembles D(f) forment une base de la topologie de X.

(ii) Pour tout $f \in \mathbf{A}$, $\mathrm{D}(f)$ est quasi-compact. En particulier $\mathrm{X} = \mathrm{D}(\mathrm{i})$ est quasi-compact.

(i) Soit U un ensemble ouvert dans X ; par définition, on a U=X—V(E) où E est une partie de A, et V(E)= $\bigcap_{f\in E}V(f)$ , d'où U= $\bigcup_{f\in E}D(f)$ .

(ii) D'après (i), il suffit de prouver que si $(f_{\lambda})_{\lambda \in L}$ est une famille d'éléments de A telle que $D(f)\subset \bigcup_{\lambda \in L}D(f_{\lambda})$, il existe une partie finie J de L telle que $D(f)\subset \bigcup_{\lambda \in J}D(f_{\lambda})$. Soit a l'idéal de A engendré par les $f_{\lambda}$; on a par hypothèse $V(f)\supset V(a)$, donc $\mathfrak{r}(f)\subset \mathfrak{r}(a)$; comme $f\in \mathfrak{r}(f)$, il existe un entier $n\geqslant 0$ tel que $f^n\in \mathfrak{a}$. Mais alors $f^n$ appartient à l'idéal b engendré par une sous-famille finie $(f_{\lambda})_{\lambda \in J}$, et on a $V(f) = V(f^n)\supset V(b) = \bigcap_{\lambda \in J}V(f_\lambda)$, c'est-à-dire $D(f)\subset \bigcup_{\lambda \in J}D(f_\lambda)$.

Proposition (I.I.II). — Pour tout idéal a de A, Spec(A/a) s'identifie canoniquement au sous-espace fermé V(a) de Spec(A).

On sait en effet qu'il y a correspondance biunivoque canonique, respectant la structure d'ordre de l'inclusion, entre idéaux (resp. idéaux premiers) de A/a et idéaux (resp. idéaux premiers) de A contenant a.

Rappelons que l'ensemble N des éléments nilpotents de A (ou nilradical de A) est un idéal égal à r(o), intersection de tous les idéaux premiers de A (0, i.1.1).

Corollaire (1.1.12). — Les espaces topologiques Spec(A) et Spec(A/Re) sont canoniquement isomorphes.

Proposition (1.1.13). — Pour que  $X=\text{Spec}(A)$  soit irréductible (0, 2.1.1), il faut et il suffit que l'anneau A/Re soit intègre (ou, ce qui revient au même, que l'idéal Re soit premier).

En vertu du cor. (I.I.12), on peut se borner au cas où $\mathfrak{N}=0$. Si X est réductible, il existe deux parties fermées $Y_{1}$, $Y_{2}$ distinctes de X et telles que $X=Y_{1} \cup Y_{2}$, d'où $j(X)=j(Y_{1}) \cap j(Y_{2})=0$, les idéaux $j(Y_{1})$ et $j(Y_{2})$ étant distincts de (o) (I.I.5); donc A n'est pas intègre. Inversement, si dans A il y a deux éléments $f \neq 0$, $g \neq 0$ tels que $fg=0$, on a $V(f) \neq X$, $V(g) \neq X$ (puisque l'intersection des idéaux premiers de A est (o)), et $X=V(fg)=V(f) \cup V(g)$.

Corollaire (1.1.14). — (i) Dans la correspondance biunivoque entre parties fermées de X=Spec(A) et idéaux de A égaux à leurs racines, les parties fermées irréductibles de X correspondent aux idéaux premiers de A. En particulier, les composantes irréductibles de X correspondent aux idéaux premiers minimaux de A.

(ii) L'application  $x \to \{x\}$  établit une correspondance biunivoque entre X et l'ensemble des parties fermées irréductibles de X (autrement dit toute partie fermée irréductible de X admet un point générique et un seul).

(i) résulte aussitôt de (I.I.I3) et (I.I.II); et pour démontrer (ii), on peut, en vertu de (I.I.II), se borner au cas où X est irréductible; alors, d'après la prop. (I.I.I3), il existe dans A un plus petit idéal premier N, qui correspond donc à un point générique

de X; en outre, X n'admet qu'un seul point générique puisque c'est un espace de Kolmogoroff ((1.1.8) et (0, 2.1.3)).

Proposition (1.1.15). — Si J est un idéal de A contenu dans le radical R(A), le seul voisinage de V(J) dans X = Spec(A) est l'espace X tout entier.

En effet, tout idéal maximal de A appartient par définition à V(ℑ). Comme tout idéal a de A est contenu dans un idéal maximal, on a V(a) ∩ V(ℑ) ≠ 0, d'où la proposition.

## 1.2. Propriétés fonctorielles des spectres premiers d'anneaux.

(1.2.1) Soient A, A' deux anneaux,

$$
\varphi : \mathrm{A} ^ {\prime} \rightarrow \mathrm{A}
$$

un homomorphisme d'anneaux. Pour tout idéal premier $x = \mathbf{j}_x \in \operatorname{Spec}(\mathbf{A}) = \mathbf{X}$, l'anneau $A'/\varphi^{-1}(\mathbf{j}_x)$ est canoniquement isomorphe à un sous-anneau de $A/\mathbf{j}_x$, donc est intègre, autrement dit $\varphi^{-1}(\mathbf{j}_x)$ est un idéal premier de $A'$; nous le noterons $^a\varphi(x)$, et nous avons ainsi défini une application

$$
{ } ^ { a } \varphi : X = \operatorname{Spec} (A) \rightarrow X ^ { \prime } = \operatorname{Spec} (A ^ { \prime })
$$

(aussi notée $\operatorname{Spec}(\varphi)$) que nous appellerons l'application associée à l'homomorphisme $\varphi$. Nous désignerons par $\varphi^x$ l'homomorphisme injectif de $A'/\varphi^{-1}(j_x)$ dans $A/j_x$, déduit de $\varphi$ par passage aux quotients, ainsi que son prolongement canonique en un monomorphisme de corps

$$
\varphi^ {x}: \mathbf {K} (^ {a} \varphi (x)) \rightarrow \mathbf {K} (x);
$$

pour tout $f' \in A'$, on a donc par définition

(1.2.1.1)

$$
\varphi^ {x} (f ^ {\prime} (^ {a} \varphi (x))) = (\varphi (f ^ {\prime})) (x)\tag{\( (x \in X) \) .}
$$

Proposition (1.2.2). — (i) Pour toute partie $\mathbf{E}'$ de $\mathbf{A}'$, on $a$

$$
{ } ^ { a } \varphi ^ { - 1 } ( \mathrm{V} ( \mathrm{E} ^ { \prime } ) ) = \mathrm{V} ( \varphi ( \mathrm{E} ^ { \prime } ) )\tag{1.2.2.1}
$$

et en particulier, pour tout $f' \in A'$

$$
{ } ^ { a } \varphi ^ { - 1 } ( \mathrm{D} ( f ^ { \prime } ) ) = \mathrm{D} ( \varphi ( f ^ { \prime } ) ) .\tag{1.2.2.2}
$$

(ii) Pour tout idéal a de A, on a

$$
\overline {{{^ {a} \varphi (\mathrm{V} (\mathfrak {a}))}}} = \mathrm{V} (\varphi^ {- 1} (\mathfrak {a})).\tag{1.2.2.3}
$$

En effet, la relation $^a\varphi(x) \in V(E')$ est par définition équivalente à $E' \subset \varphi^{-1}(j_x)$, donc à $\varphi(E') \subset j_x$, et finalement à $x \in V(\varphi(E'))$, d'où (i). Pour démontrer (ii), on peut supposer $a$ égal à sa racine, puisque $V(r(a)) = V(a)$ (I. I. 2 (v)) et $\varphi^{-1}(r(a)) = r(\varphi^{-1}(a))$; si on pose $Y = V(a)$, et $a' = j(^a\varphi(Y))$, on a $^a\varphi(Y) = V(a')$ (prop. (I. I. 4 (ii))); la relation $f' \in a'$ est par définition équivalente à $f'(x') = o$ pour tout $x' \in ^a\varphi(Y)$, donc, en vertu de la formule (I. 2. I. I), elle est aussi équivalente à $\varphi(f')(x) = o$ pour tout $x \in Y$, ou encore à $\varphi(f') \in j(Y) = a$, puisque $a$ est égal à sa racine ; d'où (ii).

Corollaire (1.2.3). — L'application $^{a}\varphi$ est continue.

Remarquons que si A'' est un troisième anneau, $\varphi'$ un homomorphisme A''→A', on a “(φ'∘φ)=“φ∘φ'; ce résultat et le cor. (1.2.3) signifient que Spec(A) est un foncteur contravariant en A, de la catégorie des anneaux dans celle des espaces topologiques.

Corollaire (1.2.4). — Supposons que $\varphi$ soit tel que tout $f\in A$ s'écrive $f=h\varphi(f')$, où $h$ est inversible dans A (ce qui est en particulier le cas lorsque $\varphi$ est surjectif). Alors $^a\varphi$ est un homéomorphisme de X sur $^a\varphi(X)$.

Montrons que pour toute partie $\mathbf{E} \subset \mathbf{A}$, il existe une partie $\mathbf{E}'$ de $\mathbf{A}'$ telle que $V(\mathbf{E}) = V(\varphi(\mathbf{E}'))$; en vertu de l'axiome $(T_0)$ (1.1.8) et de la formule (1.2.2.1), cela entraînera d'abord que "φ est injective, puis, toujours en vertu de (1.2.2.1), que "φ est un homéomorphisme. Or, il suffit pour chaque $f \in E$ de prendre un $f' \in A'$ tel que $h\varphi(f') = f$ avec $h$ inversible dans $A$; l'ensemble $\mathbf{E}'$ de ces éléments $f'$ répond à la question.

(1.2.5) En particulier, lorsque $\varphi$ est l'homomorphisme canonique de A sur un anneau quotient A/a, on retrouve (1.1.12), et $^a\varphi$ est l'injection canonique de V(a), identifié à $\operatorname{Spec}(A/a)$, dans X = $\operatorname{Spec}(A)$.

Un autre cas particulier de (1.2.4) donne :

Corollaire (1.2.6). — Si S est une partie multiplicative de A, le spectre $\operatorname{Spec}(\mathrm{S}^{-1}\mathrm{A})$ s'identifie canoniquement (avec sa topologie) au sous-espace de $\mathrm{X}=\operatorname{Spec}(\mathrm{A})$ formé des $x$ tels que $\mathfrak{i}_{x}\cap\mathrm{S}=\emptyset$.

On sait en effet (0, 1.2.6) que les idéaux premiers de $\mathbf{S}^{-1}\mathbf{A}$ sont les idéaux $\mathbf{S}^{-1}\mathbf{j}_x$ tels que $\mathbf{j}_x\cap \mathbf{S} = \emptyset$, et que l'on a $\mathbf{j}_x = (i_{\mathrm{A}}^{\mathrm{S}})^{-1}(\mathrm{S}^{-1}\mathbf{j}_x)$. Il suffit donc d'appliquer à $i_{\mathrm{A}}^{\mathrm{S}}$ le cor. (1.2.4).

Corollaire (1.2.7). — Pour que $^a\varphi(X)$ soit partout dense dans $X'$, il faut et il suffit que tout élément du noyau Ker $\varphi$ soit nilpotent.

En effet, appliquant la formule (1.2.2.3) à l'idéal  $\alpha=(0)$ , il vient  $\overline{\varphi(X)}=V(\operatorname{Ker}\varphi)$ , et pour que  $V(\operatorname{Ker}\varphi)=X$ , il faut et il suffit que  $\operatorname{Ker}\varphi$  soit contenu dans tous les idéaux premiers de A, c'est-à-dire dans le nilradical N de A.

## 1.3. Faisceau associé à un module.

(1.3.1) Soient A un anneau commutatif, M un A-module, f un élément de A,  $S_{f}$  l'ensemble multiplicatif des  $f^{n}$, où  $n \geqslant 0$. Rappelons que nous posons  $A_{f} = S_{f}^{-1}A$,  $M_{f} = S_{f}^{-1}M$. Si  $S_{f}'$  est la partie multiplicative saturée de A formée des  $g \in A$  qui divisent un élément de  $S_{f}$, on sait que  $A_{f}$  et  $M_{f}$  s'identifient canoniquement à  $S_{f}^{'-1}A$  et  $S_{f}^{'-1}M$  (0, 1.4.3).

Lemme (1.3.2). — Les conditions suivantes sont équivalentes :

$$
a) g \in \mathrm{S} _ {f} ^ {\prime}; b) \mathrm{S} _ {g} ^ {\prime} \subset \mathrm{S} _ {f} ^ {\prime}; c) f \in \mathfrak {r} (g); d) \mathfrak {r} (f) \subset \mathfrak {r} (g); e) \mathrm{V} (g) \subset \mathrm{V} (f); f) \mathrm{D} (f) \subset \mathrm{D} (g).
$$

Cela résulte immédiatement des définitions et de (1.1.5).

(1.3.3) Si $\mathrm{D}(f) = \mathrm{D}(g)$, le lemme (1.3.2, b)) montre que $\mathbf{M}_j = \mathbf{M}_g$. Plus généralement, si $\mathrm{D}(f) \supset \mathrm{D}(g)$, donc $\mathrm{S}_j' \subset \mathrm{S}_g'$, on sait (0, 1.4.1) qu'il existe un homomorphisme canonique fonctoriel

$$
\rho_ {g, f}: \mathrm{M} _ {f} \rightarrow \mathrm{M} _ {g},
$$

et si $\mathbf{D}(f)\supset \mathbf{D}(g)\supset \mathbf{D}(h)$, on a $(0,1.4.4)$

$$
\rho_ {h, g} \circ \rho_ {g, f} = \rho_ {h, f}.\tag{1.3.3.1}
$$

Lorsque $f$ parcourt $\mathbf{A}-\mathbf{j}_{x}$ (pour un $x$ donné dans $\mathbf{X}=\operatorname{Spec}(\mathbf{A})$), les ensembles $\mathbf{S}_{f}^{\prime}$ constituent un ensemble filtrant croissant de parties de $\mathbf{A}-\mathbf{j}_{x}$, car pour deux éléments $f,g$ de $\mathbf{A}-\mathbf{j}_{x},\mathbf{S}_{f}^{\prime}$ et $\mathbf{S}_{g}^{\prime}$ sont contenus dans $\mathbf{S}_{fg}^{\prime}$; comme la réunion des $\mathbf{S}_{f}^{\prime}$ pour $f\in\mathbf{A}-\mathbf{j}_{x}$ est $\mathbf{A}-\mathbf{j}_{x}$, on en conclut (0, 1.4.5) que le $\mathbf{A}_{x}$-module $\mathbf{M}_{x}$ s'identifie canoniquement à la limite inductive $\lim_{\longrightarrow}\mathbf{M}_{f}$, relativement à la famille d'homomorphismes ($\rho_{g,f}$). Nous désignerons par

$$
\rho_ {x} ^ {\prime}: \mathbf {M} _ {f} \rightarrow \mathbf {M} _ {x}
$$

l'homomorphisme canonique pour $f \in A - j_x$ (ou, ce qui revient au même, $x \in D(f)$). Définition (1.3.4). — On appelle faisceau structural du spectre premier $X = \text{Spec}(A)$ (resp. faisceau associé au A-module M) et on note $\widetilde{A}$ ou $O_X$ (resp. $\widetilde{M}$) le faisceau d'anneaux (resp. le $\widetilde{A}$-Module) associé au préfaisceau $D(f) \to A_f$ (resp. $D(f) \to M_f$) sur la base $\mathfrak{B}$ de X formée des $D(f)$ où $f \in A$ ((1.1.10), (0, 3.2.1 et 3.5.6)).

On a vu (0, 3.2.4) que la fibre $\widetilde{\mathrm{A}}_{x}$ (resp. $\widetilde{\mathrm{M}}_{x}$) s'identifie à l'anneau $\mathrm{A}_{x}$ (resp. au $\mathrm{A}_{x}$-module $\mathrm{M}_{x}$); nous désignerons par

$$
\begin{array}{c}\theta_ {f}: \mathrm{A} _ {f} \rightarrow \Gamma (\mathrm{D} (f), \widetilde {\mathrm{A}})\\(\mathrm{resp.} \theta_ {f}: \mathrm{M} _ {f} \rightarrow \Gamma (\mathrm{D} (f), \widetilde {\mathrm{M}})),\end{array}
$$

l'application canonique, de sorte que pour tout $x \in \mathrm{D}(f)$ et tout $\xi \in \mathbf{M}_j$, on a

$$
\left(\theta_ {f} (\xi)\right) _ {x} = \rho_ {x} ^ {f} (\xi).
$$

Proposition (1.3.5). — $\widetilde{\mathbf{M}}$ est un foncteur covariant exact en $\mathbf{M}$, de la catégorie des A-modules dans la catégorie des $\widetilde{\mathbf{A}}$-Modules.

En effet, soient M, N deux A-modules, u un homomorphisme  $M \to N$ ; pour tout  $f \in A$ , il correspond canoniquement à u un homomorphisme  $u_{f}$  du  $A_{f}$ -module  $M_{f}$  dans le  $A_{f}$ -module  $N_{f}$ , et le diagramme (pour  $D(g) \subset D(f)$ )

$$
\begin{array}{c} \mathbf {M} _ {f} \stackrel {{u _ {f}}} {{\to}} \mathbf {N} _ {f} \\ \rho_ {g, f} \Biggl \downarrow \qquad \qquad \qquad \Biggl \downarrow \rho_ {g, f} \\ \mathbf {M} _ {g} \stackrel {{\to}} {{\to}} \mathbf {N} _ {g} \end{array}
$$

est commutatif (0, 1.4.1); ces homomorphismes définissent donc un homomorphisme de $\widetilde{\mathbf{A}}$-Modules $\widetilde{u}:\widetilde{\mathbf{M}}\to\widetilde{\mathbf{N}}$ (0, 3.2.3). En outre, pour tout $x\in\mathbf{X}$, $\widetilde{u}_{x}$ est la limite inductive des $u_{f}$ pour $x\in\mathrm{D}(f)$ ($f\in\mathrm{A}$), et par suite (0, 1.4.5) si on identifie canoniquement $\widetilde{\mathbf{M}}_{x}$ et $\widetilde{\mathbf{N}}_{x}$ à $\mathbf{M}_{x}$ et $\mathbf{N}_{x}$ respectivement, $\widetilde{u}_{x}$ s'identifie à l'homomorphisme $u_{x}$ déduit canoniquement de $u$. Si P est un troisième A-module, $v$ un homomorphisme $\mathbf{N}\to\mathbf{P}$ et $w=v\circ u$, il est immédiat que $w_{x}=v_{x}\circ u_{x}$, donc $\widetilde{w}=\widetilde{v}\circ\widetilde{u}$. On a donc bien défini un foncteur covariant $\widetilde{\mathbf{M}}$ en M, de la catégorie des A-modules dans celle des $\widetilde{\mathbf{A}}$-Modules. Ce foncteur est exact, car pour tout $x\in\mathbf{X}$, $\mathbf{M}_{x}$ est un foncteur exact en M (0, 1.3.2); en outre, on a $\operatorname{Supp}(\mathbf{M})=\operatorname{Supp}(\widetilde{\mathbf{M}})$ en vertu des définitions des deux membres (0, 1.7.1 et 3.1.6).

Proposition (1.3.6). — Pour tout $f\in\mathbf{A}$, l'ensemble ouvert $\mathbf{D}(f)\subset\mathbf{X}$ s'identifie canoniquement au spectre premier $\operatorname{Spec}(\mathbf{A}_{f})$, et le faisceau $\widetilde{\mathbf{M}}_{f}$ associé au $\mathbf{A}_{f}$-module $\mathbf{M}_{f}$ s'identifie canoniquement à la restriction $\widetilde{\mathbf{M}}|\mathbf{D}(f)$.

La première assertion est un cas particulier de (1.2.6). En outre, si  $g \in A$  est tel que  $\mathrm{D}(g) \subset \mathrm{D}(f)$ ,  $M_{g}$  s'identifie canoniquement au module des fractions de  $M_{f}$  dont les dénominateurs sont les puissances de l'image canonique de g dans  $A_{f}$  (0, 1.4.6). L'identification canonique de  $\widetilde{M}_{f}$  à  $\widetilde{M}|D(f)$  résulte alors des définitions.

Théorème (1.3.7). — Pour tout A-module M et tout  $f \in A$ , l'homomorphisme

$$
\theta_ {f}: \mathbf {M} _ {f} \rightarrow \Gamma (\mathrm{D} (f), \widetilde {\mathbf {M}})
$$

est bijectif (autrement dit, le préfaisceau  $\mathrm{D}(f)\to\mathrm{M}_{f}$  est un faisceau). En particulier, M s'identifie par  $\theta_{1}$  à  $\Gamma(\mathrm{X},\widetilde{\mathrm{M}})$ .

On notera que, si $\mathbf{M} = \mathbf{A}$, $\theta_f$ est un homomorphisme de structure d'anneau ; le th. (1.3.7) entraînera donc que, si on identifie les anneaux $\mathbf{A}_f$ et $\Gamma(\mathbf{D}(f), \widetilde{\mathbf{A}})$ au moyen de $\theta_j$, l'homomorphisme $\theta_f: \mathbf{M}_f \to \Gamma(\mathbf{D}(f), \widetilde{\mathbf{M}})$ sera un isomorphisme de modules.

Montrons d'abord que $\theta_{f}$ est injectif. En effet, si $\xi\in\mathbf{M}_{f}$ est tel que $\theta_{f}(\xi)=0$, cela signifie que pour tout idéal premier p de $A_{f}$, il existe $h\notin p$ tel que $h\xi=0$; comme l'annulateur de $\xi$ n'est contenu dans aucun idéal premier de $A_{f}$, c'est $A_{f}$ tout entier, donc $\xi=0$.

Reste à montrer que $\theta_{f}$ est surjectif; on peut se ramener au cas où $f=1$, le cas général s'en déduisant en « localisant » à l'aide de (1.3.6). Soit donc s une section de $\widetilde{M}$ au-dessus de X; en vertu de (1.3.4) et de (1.1.10, (ii)), il existe un recouvrement fini $(\mathbf{D}(f_{i}))_{i\in I}$ de $\mathbf{X}$ ($f_{i}\in\mathbf{A}$) tel que, pour tout $i\in\mathbf{I}$, la restriction $s_{i}=s|\mathbf{D}(f_{i})$ soit de la forme $\theta_{f_{i}}(\xi_{i})$, où $\xi_{i}\in\mathbf{M}_{f_{i}}$. Si $i,j$ sont deux indices de I, en écrivant que les restrictions de $s_{i}$ et de $s_{j}$ à $\mathbf{D}(f_{i})\cap\mathbf{D}(f_{j})=\mathbf{D}(f_{i}f_{j})$ sont égales, il vient par définition de M

$$
\rho_ {f _ {i} f _ {j}, f _ {i}} (\xi_ {i}) = \rho_ {f _ {i} f _ {j}, f _ {j}} (\xi_ {j}).\tag{1.3.7.1}
$$

Par définition, on peut écrire, pour chaque $i\in I$, $\xi_{i}=z_{i}/f_{i}^{n_{i}}$, où $z_{i}\in M$, et comme I est fini, en multipliant chaque $z_{i}$ par une puissance de $f_{i}$, on peut supposer tous les $n_{i}$ égaux à un même $n$. Alors, par définition, (1.3.7.1) signifie qu'il existe un entier $m_{ij}\geqslant o$ tel que $(f_{i}f_{j})^{m_{ij}}(f_{j}^{n}z_{i}-f_{i}^{n}z_{j})=0$, et on peut encore supposer tous les $m_{ij}$ égaux à un même entier $m$; remplaçant alors $z_{i}$ par $f_{i}^{m}z_{i}$, on est ramené au cas où $m=o$, autrement dit au cas où l'on a

$$
f _ {j} ^ {n} z _ {i} = f _ {i} ^ {n} z _ {j}\tag{1.3.7.2}
$$

quels que soient $i, j$. Or, on a $\mathrm{D}(f_i^n) = \mathrm{D}(f_i)$, et comme les $\mathrm{D}(f_i)$ forment un recouvrement de X, l'idéal engendré par les $f_i^n$ est A; en d'autres termes, il existe des éléments $g_i \in A$ tels que $\sum_{i} g_i f_i^n = 1$. Considérons alors l'élément $z = \sum_{i} g_i z_i$ de M; d'après (1.3.7.2), on a $f_i^n z = \sum_{j} g_j f_i^n z_j = (\sum_{j} g_j f_j^n) z_i = z_i$, d'où par définition $\xi_i = z / 1$ dans $\mathbf{M}_{f_i}$. On en conclut

que $s_i$ est la restriction à $\mathbf{D}(f_i)$ de $\theta_1(z)$, ce qui prouve que $s = \theta_1(z)$ et achève la démonstration.

Corollaire (1.3.8). — Soient M, N deux A-modules ; l'homomorphisme canonique $u\to\widetilde{u}$ de $\mathrm{Hom}_{\mathrm{A}}(\mathrm{M},\mathrm{N})$ dans $\mathrm{Hom}_{\mathrm{A}}(\widetilde{\mathrm{M}},\widetilde{\mathrm{N}})$ est bijectif. En particulier, les relations $M=0$ et $\widetilde{M}=0$ sont équivalentes.

Considérons en effet l'homomorphisme canonique $v\to\Gamma(v)$ de $\mathrm{Hom}_{\widetilde{\mathbf{A}}}(\widetilde{\mathbf{M}},\widetilde{\mathbf{N}})$ dans $\mathrm{Hom}_{\Gamma(\widetilde{\mathbf{A}})}(\Gamma(\widetilde{\mathbf{M}}),\Gamma(\widetilde{\mathbf{N}}))$; ce dernier module s'identifie canoniquement à $\mathrm{Hom}_{\mathbf{A}}(\mathbf{M},\mathbf{N})$ en vertu du th. (1.3.7). Il reste à vérifier que $u\to\widetilde{u}$ et $v\to\Gamma(v)$ sont réciproques l'un de l'autre; or, il est évident que $\Gamma(\widetilde{u})=u$ par définition de $\widetilde{u}$; et d'autre part, si on pose $u=\Gamma(v)$ pour $v\in\mathrm{Hom}_{\widetilde{\mathbf{A}}}(\widetilde{\mathbf{M}},\widetilde{\mathbf{N}})$, l'application $w:\Gamma(\mathbf{D}(f),\widetilde{\mathbf{M}})\to\Gamma(\mathbf{D}(f),\widetilde{\mathbf{N}})$ déduite canoniquement de $v$ est telle que le diagramme

$$
\begin{array}{c} \mathbf {M} \xrightarrow {u} \mathbf {N} \\ \varrho_ {f, 1} \Biggl \downarrow \qquad \qquad \qquad \qquad \Biggl \downarrow \varrho_ {f, 1} \\ \mathbf {M} _ {f} \xrightarrow [ w ]{} \mathbf {N} _ {f} \end{array}
$$

soit commutatif ; on a donc nécessairement $w = u_{j}$ pour tout $f \in A$ (0, 1.2.4), ce qui montre que $(\Gamma(v))^{\sim} = v$.

Corollaire (1.3.9). — (i) Soit u un homomorphisme d'un A-module M dans un A-module N ; alors les faisceaux associés à Ker u, Im u, Coker u, sont respectivement Ker  $\widetilde{u}$ , Im  $\widetilde{u}$ , Coker  $\widetilde{u}$ . En particulier pour que  $\widetilde{u}$  soit injectif (resp. surjectif, bijectif), il faut et il suffit que u le soit.

(ii) Si M est une limite inductive (resp. somme directe) d'une famille de A-modules  $(\mathbf{M}_{\lambda})$ ,  $\widetilde{M}$  est limite inductive (resp. somme directe) de la famille  $(\widetilde{\mathbf{M}}_{\lambda})$ , à un isomorphisme canonique près.

(i) Il suffit d'appliquer le fait que $\widetilde{M}$ est un foncteur exact en $M$ (1.3.5) aux deux suites exactes de A-modules

$$
\mathrm{o} \rightarrow \operatorname{Ker} u \rightarrow \mathrm{M} \rightarrow \operatorname{Im} u \rightarrow \mathrm{o}
$$

$$
\mathrm{o} \rightarrow \operatorname{Im} u \rightarrow \mathrm{N} \rightarrow \operatorname{Coker} u \rightarrow \mathrm{o}
$$

La seconde assertion résulte alors du th. (1.3.7).

(ii) Soit $(\mathbf{M}_{\lambda}, g_{\mu \lambda})$ un système inductif de A-modules, de limite inductive M, et soit $g_{\lambda}$ l'homomorphisme canonique $\mathbf{M}_{\lambda} \to \mathbf{M}$. Comme on a $\widetilde{g}_{\nu \mu} \circ \widetilde{g}_{\mu \lambda} = \widetilde{g}_{\nu \lambda}$ et $\widetilde{g}_{\lambda} = \widetilde{g}_{\mu} \circ \widetilde{g}_{\mu \lambda}$ pour $\lambda \leqslant \mu \leqslant \nu$, $(\widetilde{\mathbf{M}}_{\lambda}, \widetilde{g}_{\mu \lambda})$ est un système inductif de faisceaux sur X, et si on désigne par $h_{\lambda}$ l'homomorphisme canonique $\widetilde{\mathbf{M}}_{\lambda} \to \varinjlim \widetilde{\mathbf{M}}_{\lambda}$, il y a un homomorphisme unique $v: \varinjlim \widetilde{\mathbf{M}}_{\lambda} \to \widetilde{\mathbf{M}}$ tel que $v \circ h_{\lambda} = \widetilde{g}_{\lambda}$. Pour voir que $v$ est bijectif, il suffit de vérifier que, pour tout $x \in X$, $v_x$ est une bijection de $(\varinjlim \widetilde{\mathbf{M}}_{\lambda})_x$ sur $\widetilde{\mathbf{M}}_x$; mais $\widetilde{\mathbf{M}}_x = \mathbf{M}_x$ et

$$
(\varinjlim \widetilde {M} _ {\lambda}) _ {x} = \varinjlim (\widetilde {M} _ {\lambda}) _ {x} = \varinjlim (M _ {\lambda}) _ {x} = M _ {x} (0, 1. 3. 3).
$$

D'autre part, il résulte des définitions que $(\widetilde{g}_{\lambda})_x$ et $(h_{\lambda})_x$ sont tous deux égaux à l'application canonique de $(\mathbf{M}_{\lambda})_x$ dans $\mathbf{M}_x$; comme $(\widetilde{g}_{\lambda})_x = v_x \circ (h_{\lambda})_x$, $v_x$ est l'identité.

Enfin, si M est somme directe de deux A-modules N, P, il est immédiat que  $\widetilde{M}=\widetilde{N}\oplus\widetilde{P}$ ; toute somme directe étant limite inductive de sommes directes finies, les assertions de (ii) sont démontrées.

On notera que (1.3.8) prouve que les faisceaux isomorphes aux faisceaux associés aux A-modules forment une catégorie abélienne (T, I, 1.4).

On notera aussi qu'il résulte de (1.3.9) que si M est un A-module de type fini, c'est-à-dire s'il existe un homomorphisme surjectif  $A^{n} \rightarrow M$ , alors il existe un homomorphisme surjectif  $\widetilde{A}^{n} \rightarrow \widetilde{M}$ , autrement dit le  $\widetilde{A}$ -Module  $\widetilde{M}$  est engendré par une famille finie de sections au-dessus de X (0, 5.1.1), et réciproquement.

(1.3.10) Si N est un sous-module d'un A-module M, l'injection canonique $j: \mathrm{N} \to \mathrm{M}$ donne par (1.3.9) un homomorphisme injectif $\widetilde{\mathrm{N}} \to \widetilde{\mathrm{M}}$, qui permet d'identifier canoniquement $\widetilde{\mathrm{N}}$ à un sous-$\widetilde{\mathrm{A}}$-Module de $\widetilde{\mathrm{M}}$; nous supposerons toujours faite cette identification. Si N et P sont deux sous-modules de M, on a alors

(1.3.10.1)

$$
(\mathbf {N} + \mathbf {P}) ^ {\sim} = \widetilde {\mathbf {N}} + \widetilde {\mathbf {P}}\tag{1.3.10.2}
$$

$$
(\mathbf {N} \cap \mathbf {P}) ^ {\sim} = \widetilde {\mathbf {N}} \cap \widetilde {\mathbf {P}}
$$

car N+P et N∩P sont respectivement l'image de l'homomorphisme canonique N⊕P→M, et le noyau de l'homomorphisme canonique M→(M/N)⊕(M/P) et il suffit d'appliquer (1.3.9).

On conclut de (1.3.10.1) et (1.3.10.2) que si $\widetilde{\mathbf{N}} = \widetilde{\mathbf{P}}$, on a $\mathbf{N} = \mathbf{P}$.

Corollaire (1.3.11). — Dans la catégorie des faisceaux isomorphes aux faisceaux associés aux A-modules, le foncteur $\Gamma$ est exact.

En effet, soit $\widetilde{\mathbf{M}}\stackrel {u}{\to}\widetilde{\mathbf{N}}\stackrel {v}{\to}\widetilde{\mathbf{P}}$ une suite exacte correspondant à deux homomorphismes $u:\mathrm{M}\rightarrow \mathrm{N},v:\mathrm{N}\rightarrow \mathrm{P}$ de A-modules. Si $\mathbf{Q} = \operatorname {Im}u$ et $\mathbb{R} = \operatorname {Ker}v,$ on a $\widetilde{\mathbf{Q}} = \operatorname {Im}\widetilde{u} = \operatorname {Ker}\widetilde{v} = \widetilde{\mathbb{R}}$ (cor. (1.3.9)), donc $\mathbf{Q} = \mathbb{R}$.

Corollaire (1.3.12). — Soient M, N deux A-modules.

(i) Le faisceau associé à $\mathbf{M} \otimes_{\mathbb{A}} \mathbf{N}$ s'identifie canoniquement à $\widetilde{\mathbf{M}} \otimes_{\widetilde{\mathbb{A}}} \widetilde{\mathbf{N}}$.

(ii) Si de plus M admet une présentation finie, le faisceau associé à $\mathrm{Hom}_{\mathbb{A}}(\mathbf{M},\mathbf{N})$ s'identifie canoniquement à $\mathcal{H}om_{\widetilde{\mathbb{A}}}(\widetilde{\mathbf{M}},\widetilde{\mathbf{N}})$.

(i) Le faisceau $\mathcal{F} = \widetilde{M}\otimes_{\tilde{\mathbf{A}}}\widetilde{N}$ est associé au préfaisceau

$$
\mathrm{U} \rightarrow \mathcal {F} (\mathrm{U}) = \Gamma (\mathrm{U}, \widetilde {\mathrm{M}}) \otimes_ {\Gamma (\mathrm{U}, \widetilde {\mathrm{A}})} \Gamma (\mathrm{U}, \widetilde {\mathrm{N}})
$$

U parcourant la base (I. I. 10, (i)) de X formée des D(f), où $f\in\mathbf{A}$. Or, $\mathcal{F}(\mathbf{D}(f))$ s'identifie canoniquement à $\mathbf{M}_{f}\otimes_{\mathbf{A}_{f}}\mathbf{N}_{f}$ en vertu de (I.3.7) et (I.3.6). On sait par ailleurs que le $\mathbf{A}_{f}$-module $\mathbf{M}_{f}\otimes_{\mathbf{A}_{f}}\mathbf{N}_{f}$ est canoniquement isomorphe à $(\mathbf{M}\otimes_{\mathbf{A}}\mathbf{N})_{f}$ (0, I.3.4), qui lui-même est canoniquement isomorphe à $\Gamma(\mathbf{D}(f), (\mathbf{M}\otimes_{\mathbf{A}}\mathbf{N})\sim)$ (I.3.7 et I.3.6). En outre, on vérifie aussitôt que les isomorphismes canoniques

$$
\mathcal {F} (\mathrm{D} (f)) \simeq \Gamma (\mathrm{D} (f), (\mathrm{M} \otimes_ {\mathrm{A}} \mathrm{N}) ^ {\sim})
$$

ainsi obtenus vérifient les conditions de compatibilité avec les opérateurs de restriction (0, 1.4.2), donc définissent un isomorphisme canonique fonctoriel

$$
\widetilde {\mathbf {M}} \otimes_ {\widetilde {\mathbf {A}}} \widetilde {\mathbf {N}} \xrightarrow {\sim} (\mathbf {M} \otimes_ {\mathbf {A}} \mathbf {N}) ^ {\sim}
$$

(ii) Le faisceau $\mathcal{G} = \mathcal{H}om_{\tilde{\mathbf{A}}}(\widetilde{\mathbf{M}},\widetilde{\mathbf{N}})$ est associé au préfaisceau

$$
\mathrm{U} \rightarrow \mathcal {G} (\mathrm{U}) = \operatorname{Hom} _ {\tilde {\mathbf {A}} | \mathrm{U}} (\widetilde {\mathbf {M}} | \mathrm{U}, \widetilde {\mathbf {N}} | \mathrm{U})
$$

U parcourant la base de X formée des D(f). Or, $\mathcal{G}(\mathrm{D}(f))$ s'identifie canoniquement à $\operatorname{Hom}_{\mathbb{A}_f}(\mathbf{M}_f, \mathbf{N}_f)$ (1.3.6 et 1.3.8), qui lui-même, en vertu de l'hypothèse sur M, s'identifie canoniquement à $(\operatorname{Hom}_{\mathbb{A}}(\mathbf{M}, \mathbf{N}))_f$ (0, 1.3.5). Finalement, $(\operatorname{Hom}_{\mathbb{A}}(\mathbf{M}, \mathbf{N}))_f$ s'identifie canoniquement à $\Gamma(\mathrm{D}(f), (\operatorname{Hom}_{\mathbb{A}}(\mathbf{M}, \mathbf{N}))^{\sim})$ (1.3.6 et 1.3.7), et les isomorphismes canoniques $\mathcal{G}(\mathrm{D}(f)) \to \Gamma(\mathrm{D}(f), (\operatorname{Hom}_{\mathbb{A}}(\mathbf{M}, \mathbf{N}))^{\sim})$ ainsi obtenus sont compatibles avec les opérateurs de restriction (0, 1.4.2); ils définissent donc un isomorphisme canonique $\mathcal{H}om_{\widetilde{\mathbb{A}}}(\widetilde{\mathbf{M}}, \widetilde{\mathbf{N}}) \simeq (\operatorname{Hom}_{\mathbb{A}}(\mathbf{M}, \mathbf{N}))^{\sim}$.

(1.3.13) Soit maintenant B une A-algèbre (commutative); cela peut s'interpréter en disant que B est un A-module et qu'on s'est donné un élément  $e \in B$  et un A-homomorphisme  $\varphi : B \otimes_{A} B \to B$ , de sorte que :  $r^{0}$  Les diagrammes

$$
\begin{array}{c c} \mathrm{B} \otimes_ {\mathrm{A}} \mathrm{B} \otimes_ {\mathrm{A}} \mathrm{B} \xrightarrow {\varphi \otimes 1} \mathrm{B} \otimes_ {\mathrm{A}} \mathrm{B} & \quad \mathrm{B} \otimes_ {\mathrm{A}} \mathrm{B} \xrightarrow {\sigma} \mathrm{B} \otimes_ {\mathrm{A}} \mathrm{B} \\ 1 \otimes \varphi \Bigg \downarrow & \quad \varphi \searrow \\ \mathrm{B} \otimes_ {\mathrm{A}} \mathrm{B} \xrightarrow [ \varphi ]{} \mathrm{B} & \quad \mathrm{B} \end{array}
$$

(σ symétrie canonique) soient commutatifs;  $2^{\circ} \varphi(e \otimes x) = \varphi(x \otimes e) = x$ . En vertu de (1.3.12), l'homomorphisme  $\widetilde{\varphi}: \widetilde{B} \otimes_{\widetilde{A}} \widetilde{B} \to \widetilde{B}$  de A-Modules vérifie les conditions analogues, donc définit sur  $\widetilde{B}$  une structure de  $\widetilde{A}$ -Algèbre. De la même manière, la donnée d'un B-module N revient à la donnée d'un A-module N et d'un A-homomorphisme  $\psi: B \otimes_{A} N \to N$  tel que le diagramme

$$
\begin{array}{c} \mathbf {B} \otimes_ {\mathbf {A}} \mathbf {B} \otimes_ {\mathbf {A}} \mathbf {N} \xrightarrow {\varphi \otimes 1} \mathbf {B} \otimes_ {\mathbf {A}} \mathbf {N} \\ \Biggl \downarrow^ {1 \otimes \psi} \\ \mathbf {B} \otimes_ {\mathbf {A}} \mathbf {N} \xrightarrow [ \psi ]{} \mathbf {N} \end{array}
$$

soit commutatif et $\psi(e\otimes n)=n$; l'homomorphisme $\widetilde{\psi}:\widetilde{B}\otimes_{\widetilde{A}}\widetilde{N}\to\widetilde{N}$ vérifiera la condition analogue, et définit donc sur $\widetilde{N}$ une structure de $\widetilde{B}$-Module.

De la même façon, on voit que si $u: \mathbf{B} \to \mathbf{B}'$ (resp. $v: \mathbf{N} \to \mathbf{N}'$) est un homomorphisme de A-algèbres (resp. de B-modules), $\widetilde{u}$ (resp. $\widetilde{v}$) est un homomorphisme de $\widetilde{\mathbf{A}}$-Algèbres (resp. de $\widetilde{\mathbf{B}}$-Modules), Ker $\widetilde{u}$ un $\widetilde{\mathbf{B}}$-Idéal (resp. Ker $\widetilde{v}$, Coker $\widetilde{v}$ et Im $\widetilde{v}$ des $\widetilde{\mathbf{B}}$-Modules). Si N est un B-module, $\widetilde{\mathbf{N}}$ est un $\widetilde{\mathbf{B}}$-Module de type fini si et seulement si N est un B-module de type fini (0, 5.2.3).

Si M, N sont deux B-modules, le $\widetilde{\mathbf{B}}$-Module $\widetilde{\mathbf{M}}\otimes_{\widetilde{\mathbf{B}}}\widetilde{\mathbf{N}}$ s'identifie canoniquement à $(\mathbf{M}\otimes_{\mathbf{B}}\mathbf{N})^{\sim}$; de même $\mathcal{H}om_{\widetilde{\mathbf{B}}}(\widetilde{\mathbf{M}},\widetilde{\mathbf{N}})$ s'identifie canoniquement à $(\mathrm{Hom}_{\mathbf{B}}(\mathbf{M},\mathbf{N}))^{\sim}$ lorsque M admet une présentation finie; les démonstrations sont les mêmes que dans (1.3.12).

Si $\mathfrak{J}$ est un idéal de B, N un B-module, on a $(\mathfrak{J}N)^{\sim} = \widetilde{\mathfrak{J}}.\widetilde{N}$.

Enfin, si B est une A-algèbre graduée par des sous-A-modules  $B_{n}$  ( $n \in Z$ ), la  $\widetilde{A}$ -Algèbre  $\widetilde{B}$ , somme directe des  $\widetilde{A}$ -Modules  $\widetilde{B}_{n}$  (1.3.9) est graduée par ces sous- $\widetilde{A}$ -Modules, l'axiome de la graduation exprimant que l'image de l'homomorphisme  $B_{m} \otimes B_{n} \to B$  est contenu dans  $B_{m+n}$ . De même, si M est un B-module gradué par des sous-modules  $M_{n}, \widetilde{M}$  est un  $\widetilde{B}$ -Module gradué par les  $\widetilde{M}_{n}$ .

(1.3.14) Si B est une A-algèbre, M un sous-module de B, la sous-Ã-Algèbre de  $\widetilde{B}$  engendrée par  $\widetilde{M}$  (0, 4.1.3) est la sous-Ã-Algèbre  $\widetilde{C}$, en désignant par C la sous-algèbre de B engendrée par M. En effet, C est la somme des sous-modules de B images des homomorphismes  $\otimes^{n}M\to B$  ( $n\geqslant0$ ), et il suffit d'appliquer (1.3.9) et (1.3.12).

## 1.4. Faisceaux quasi-cohérents sur un spectre premier.

Théorème (1.4.1). — Soient X le spectre premier d'un anneau A, V une partie ouverte quasi-compacte de X, F un  $(\mathcal{O}_{\mathrm{X}}|\mathrm{V})$ -Module. Les quatre conditions suivantes sont équivalentes :

a) Il existe un A-module M tel que $\mathcal{F}$ soit isomorphe à $\widetilde{\mathbf{M}}|\mathbf{V}$.

b) Il existe un recouvrement ouvert fini (V$_{i}$) de V par des ensembles de la forme D(f$_{i}$) (f$_{i}$ ∈ A) contenus dans V, tels que, pour tout i, F|V$_{i}$ soit isomorphe à un faisceau de la forme M$_{i}$, où M$_{i}$ est un A$_{fi}$-module.

c) Le faisceau $\mathcal{F}$ est quasi-cohérent (0, 5.1.3).

d) Les deux propriétés suivantes ont lieu :

d 1) Pour tout $f \in \mathbf{A}$ tel que $\mathbf{D}(f) \subset \mathbf{V}$ et toute section $s \in \Gamma(\mathbf{D}(f), \mathcal{F})$, il existe un entier $n \geqslant 0$ tel que $f^n s$ se prolonge en une section de $\mathcal{F}$ sur $\mathbf{V}$.

d 2) Pour tout $f \in A$ tel que $D(f) \subset V$ et toute section $t \in \Gamma(V, \mathcal{F})$ telle que la restriction de $t$ à $D(f)$ soit $o$, il existe un entier $n \geqslant o$ tel que $f^n t = o$.

(Dans l'écriture des conditions $d\mathfrak{r}$) et $d\mathfrak{z}$), on a tacitement identifié $\mathbf{A}$ et $\Gamma(\widetilde{\mathbf{A}})$ en vertu de 1.3.7.)

Le fait que $a)$ entraîne $b)$ est conséquence immédiate de (1.3.6) et du fait que les $\mathrm{D}(f_i)$ forment une base de la topologie de $\mathbf{X}$ (1.1.10). Comme tout A-module est isomorphe au conoyau d'un homomorphisme $\mathrm{A}^{(I)}\to \mathrm{A}^{(J)}$, (1.3.9) prouve que tout faisceau associé à un A-module est quasi-cohérent; donc $b)$ entraîne $c)$. Réciproquement, si $\mathcal{F}$ est quasi-cohérent, tout $x\in V$ possède un voisinage de la forme $\mathrm{D}(f)\subset V$ tel que $\mathcal{F}|\mathrm{D}(f)$ soit isomorphe au conoyau d'un homomorphisme $\widetilde{\mathrm{A}}_f^{(I)}\to \widetilde{\mathrm{A}}_f^{(J)}$, donc au faisceau associé au module $\widetilde{\mathrm{N}}$, conoyau de l'homomorphisme $\mathrm{A}_f^{(I)}\to \mathrm{A}_f^{(J)}$ correspondant (1.3.8 et 1.3.9); comme $V$ est quasi-compact, il est clair que $c)$ entraîne $b)$.

Pour prouver que $b)$ entraîne $d \, \mathrm{I}$) et $d \, 2)$, supposons d'abord que $V = D(g)$ pour un $g \in A$, et que $\mathcal{F}$ soit isomorphe à un faisceau $\widetilde{\mathbf{N}}$ associé à un $A_g$-module $N$; en remplaçant $X$ par $V$ et $A$ par $A_g$ (1.3.6), on peut se ramener au cas où $g = 1$. Alors $\Gamma(D(f), \widetilde{\mathbf{N}})$ et $N_j$ s'identifient canoniquement (1.3.6 et 1.3.7), donc une section $s \in \Gamma(D(f), \widetilde{\mathbf{N}})$ s'identifie à un élément de la forme $z/f^n$, où $z \in N$; la section $f''s$ s'identifie à l'élément $z/1$ de $N_j$ et est par suite restriction à $D(f)$ de la section de $\widetilde{\mathbf{N}}$ sur $X$ identifiée à l'élément $z \in N$; d'où $d\,1)$ dans ce cas. De même, $t \in \Gamma(X, \widetilde{\mathbf{N}})$ est identifié à un élément $z' \in N$, la restriction de $t$ à $D(f)$ est identifiée à l'image $z'/1$ de $z'$ dans $N_j$, et dire que cette image est nulle signifie qu'il existe $n \geqslant 0$ tel que $f''z' = 0$ dans $N$, ou, ce qui revient au même, $f''t = 0$.

Pour achever de prouver que $b)$ entraîne $d$ 1) et $d$ 2), il suffira d'établir le lemme suivant :

Lemme (1.4.1.1). — Supposons que V soit réunion finie d'ensembles de la forme  $\mathrm{D}(g_{i})$ , et que chacun des faisceaux  $\mathcal{F}|\mathrm{D}(g_{i}),\mathcal{F}|(\mathrm{D}(g_{i})\cap\mathrm{D}(g_{j}))=\mathcal{F}|\mathrm{D}(g_{i}g_{j})\quad\text{vérifie d i})\text{ et d 2)}$ ; alors F possède les deux propriétés suivantes :

d' 1) Pour tout $f \in A$ et toute section $s \in \Gamma(D(f) \cap V, \mathcal{F})$, il existe un entier $n \geqslant 0$ tel que $f^n s$ se prolonge en une section de $\mathcal{F}$ sur $V$.

d' 2) Pour tout $f \in A$ et toute section $t \in \Gamma(V, \mathcal{F})$ telle que la restriction de $t$ à $D(f) \cap V$ soit $o$, il existe un entier $n \geqslant 0$ tel que $f^n t = 0$.

Prouvons d'abord $d'2$): comme $\mathbf{D}(f) \cap \mathbf{D}(g_i) = \mathbf{D}(fg_i)$, il existe pour chaque $i$ un entier $n_i$ tel que la restriction de $(fg_i)^{n_i}t$ à $\mathbf{D}(g_i)$ soit nulle: comme l'image de $g_i$ dans $\mathbf{A}_{g_i}$ est inversible, la restriction de $f^{nit}$ à $\mathbf{D}(g_i)$ est aussi nulle; prenant pour $n$ le plus grand des $n_i$, on a $d'2$).

Pour démontrer $d'$ 1), appliquons $d$ 1) au faisceau $\mathcal{F}|D(g_i)$ : il existe un entier $n_i \geqslant o$ et une section $s_i'$ de $\mathcal{F}$ sur $D(g_i)$ prolongeant la restriction de $(fg_i)^{n}s$ à $D(fg_i)$; comme l'image de $g_i$ dans $\mathrm{A}_{g_i}$ est inversible, il y a une section $s_i$ de $\mathcal{F}$ sur $D(g_i)$ telle que $s_i' = g_i^{n}i s_i$, et $s_i$ prolonge la restriction de $f^{n}i s$ à $D(fg_i)$; on peut en outre supposer tous les $n_i$ égaux à un même entier $n$. Par construction, la restriction de $s_i - s_j$ à $D(f) \cap D(g_i) \cap D(g_j) = D(fg_i g_j)$ est nulle; d'après $d$ 2) appliqué au faisceau $\mathcal{F}|D(g_i g_j)$, il existe un entier $m_{ij} \geqslant o$ tel que la restriction à $D(g_i g_j)$ de $(fg_i g_j)^{m_{ij}}(s_i - s_j)$ soit nulle; comme l'image de $g_i g_j$ dans $\mathrm{A}_{g_i g_j}$ est inversible, la restriction de $f^{m_{ij}}(s_i - s_j)$ à $D(g_i g_j)$ est nulle. On peut alors supposer tous les $m_{ij}$ égaux à un même entier $m$, et il existe donc une section $s' \in \Gamma(V, \mathcal{F})$ prolongeant les $f^m s_i$; cette section prolonge par suite $f^{n+m}s$, d'où $d'$ 1).

Reste à prouver que $d\mathfrak{I}$) et $d\mathfrak{2})$ entraînent $a)$. Montrons d'abord que $d\mathfrak{I}$) et $d\mathfrak{2})$ entraînent que ces conditions sont vérifiées pour tout faisceau $\mathcal{F}|\mathrm{D}(g)$, où $g\in\mathrm{A}$ est tel que $\mathrm{D}(g)\subset\mathrm{V}$. C'est évident pour $d\mathfrak{I}$); d'autre part, si $t\in\Gamma(\mathrm{D}(g),\mathcal{F})$ est telle que sa restriction à $\mathrm{D}(f)\subset\mathrm{D}(g)$ soit nulle, il existe par $d\mathfrak{I}$) un entier $m\geqslant0$ tel que $g^{m}t$ se

prolonge en une section s de F sur V ; appliquant d 2), on voit qu'il existe un entier  $n \geqslant 0$  tel que  $f^{n}g^{m}t = 0$ , et comme l'image de g dans  $A_{g}$  est inversible,  $f^{n}t = 0$ .

Cela étant, comme V est quasi-compact, le lemme (1.4.1.1) prouve que les conditions $d'$ 1) et $d'$ 2) sont vérifiées. Considérons alors le A-module $\mathbf{M} = \Gamma(\mathbf{V},\mathcal{F})$, et définissons un homomorphisme de $\widetilde{\mathbf{A}}$-Modules $u:\widetilde{\mathbf{M}}\to j_*(\mathcal{F})$, où $j$ est l'injection canonique $\mathbf{V}\to \mathbf{X}$. Comme les $\mathbf{D}(f)$ forment une base de la topologie de X, il suffit, pour chaque $f\in \mathbf{A}$, de définir un homomorphisme $u_{i}: \mathbf{M}_{i}\to \Gamma(\mathbf{D}(f),j_{*}(\mathcal{F})) = \Gamma(\mathbf{D}(f)\cap \mathbf{V},\mathcal{F})$, avec les conditions de compatibilité usuelles (0, 3.2.5). Comme l'image canonique de $f$ dans $\mathbf{A}_{i}$ est inversible, l'homomorphisme de restriction $\mathbf{M} = \Gamma(\mathbf{V},\mathcal{F})\to \Gamma(\mathbf{D}(f)\cap \mathbf{V},\mathcal{F})$ se factorise en $\mathbf{M}\to \mathbf{M}_{i}\xrightarrow{u_{i}}\Gamma(\mathbf{D}(f)\cap \mathbf{V},\mathcal{F})$ (0, 1.2.4), et la vérification des conditions de compatibilité pour $\mathbf{D}(g)\subset \mathbf{D}(f)$ est immédiate. Cela étant, montrons que la condition $d'$ 1) (resp. $d'$ 2)) entraîne que chacun des $u_{i}$ est surjectif (resp. injectif), ce qui prouvera que $u$ est bijectif, et par suite que $\mathcal{F}$ est la restriction à V d'un $\widetilde{\mathbf{A}}$-Module isomorphe à $\widetilde{\mathbf{M}}$. Or, si $s\in \Gamma(\mathbf{D}(f)\cap \mathbf{V},\mathcal{F})$, il existe d'après $d'$ 1) un entier $n\geqslant 0$ tel que $f^n s$ se prolonge en une section $z\in \mathbf{M}$; on a alors $u_{i}(z / f^{n}) = s$, donc $u_{i}$ est surjectif. De même, si $z\in \mathbf{M}$ est tel que $u_{i}(z / \mathrm{i}) = 0$, cela signifie que la restriction à $\mathbf{D}(f)\cap \mathbf{V}$ de la section $z$ est nulle; d'après $d'$ 2), il existe un entier $n\geqslant 0$ tel que $f^n z = 0$, d'où $z / \mathrm{i} = 0$ dans $\mathbf{M}_{i}$, et $u_{i}$ est donc injectif.

C.Q.F.D.

Corollaire (1.4.2). — Tout faisceau quasi-cohérent sur un ouvert quasi-compact de X est induit par un faisceau quasi-cohérent sur X.

Corollaire (1.4.3). — Toute $\mathcal{O}_{\mathrm{X}}$-Algèbre quasi-cohérente sur $\mathrm{X} = \operatorname{Spec}(\mathrm{A})$ est isomorphe à une $\mathcal{O}_{\mathrm{X}}$-Algèbre de la forme $\widetilde{\mathrm{B}}$, où $\mathrm{B}$ est une algèbre sur $\mathrm{A}$; tout $\widetilde{\mathrm{B}}$-Module quasi-cohérent est isomorphe à un $\widetilde{\mathrm{B}}$-Module de la forme $\widetilde{\mathrm{N}}$, où $\mathrm{N}$ est un $\mathrm{B}$-module.

En effet, une $\mathcal{O}_{\mathrm{X}}$-Algèbre quasi-cohérente est un $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent, donc de la forme $\widetilde{\mathbf{B}}$, où $\mathbf{B}$ est un A-module; le fait que $\mathbf{B}$ soit une A-algèbre résulte de la caractérisation de la structure de $\mathcal{O}_{\mathrm{X}}$-Algèbre à l'aide de l'homomorphisme $\widetilde{\mathbf{B}} \otimes_{\widetilde{\mathbf{A}}} \widetilde{\mathbf{B}} \to \widetilde{\mathbf{B}}$ de $\widetilde{\mathbf{A}}$-Modules, ainsi que de (1.3.12). Si $\mathcal{G}$ est un $\widetilde{\mathbf{B}}$-Module quasi-cohérent, il suffit de montrer que $\mathcal{G}$ est aussi un $\widetilde{\mathbf{A}}$-Module quasi-cohérent pour conclure ensuite de la même façon ; comme la question est locale, on peut, en se restreignant à un ouvert de $\mathbf{X}$ de la forme $\mathrm{D}(f)$, supposer que $\mathcal{G}$ est le conoyau d'un homomorphisme $\widetilde{\mathbf{B}}^{(I)} \to \widetilde{\mathbf{B}}^{(J)}$ de $\widetilde{\mathbf{B}}$-Modules (et a fortiori de $\widetilde{\mathbf{A}}$-Modules) ; la proposition résulte alors de (1.3.8) et (1.3.9).

## 1.5. Faisceaux cohérents sur un spectre premier.

Théorème (1.5.1). — Soient A un anneau noethérien, X=Spec(A) son spectre premier, V une partie ouverte de X, F un  $(\mathcal{O}_{\mathrm{X}}|\mathrm{V})$ -Module. Les conditions suivantes sont équivalentes :

a) F est cohérent.

b) F est de type fini et quasi-cohérent.

c) Il existe un A-module M de type fini tel que F soit isomorphe au faisceau  $\widetilde{M}|V$ .

a) implique trivialement b). Pour voir que b) implique c), remarquons déjà, puisque V est quasi-compact (0, 2.2.3), que $\mathcal{F}$ est isomorphe à un faisceau $\widetilde{\mathrm{N}}|\mathrm{V}$, où N est un A-module (1.4.1). Or, on a $N = \lim M_{\lambda}$, où $M_{\lambda}$ parcourt l'ensemble des sous-A-modules de type fini de N, d'où (1.3.9) $\overrightarrow{\mathcal{F}} = \widetilde{\mathrm{N}}|\mathrm{V} = \lim \widetilde{M}_{\lambda}|\mathrm{V}$; mais comme $\mathcal{F}$ est de type fini, et V quasi-compact, il existe un indice $\lambda$ tel que $\mathcal{F} = \widetilde{M}_{\lambda}|\mathrm{V}$ (0, 5.2.3).

Montrons enfin que $c)$ entraîne $a)$. Il est clair que $\mathcal{F}$ est alors de type fini (1.3.6 et 1.3.9); en outre, la question étant locale, on peut se borner au cas où $V = D(f), f \in A$. Comme $A_{f}$ est noethérien, on voit finalement que tout revient à prouver que le noyau d'un homomorphisme $\widetilde{A}^{n} \to \widetilde{M}$, où $M$ est un A-module, est de type fini. Or, un tel homomorphisme est de la forme $\widetilde{u}$, où $u$ est un homomorphisme $A^{n} \to M$ (1.3.8), et si $P = Ker u$, on a $\widetilde{P} = Ker \widetilde{u}$ (1.3.9). Comme A est noethérien, P est de type fini, ce qui achève la démonstration.

Corollaire (1.5.2). — Sous les hypothèses de (1.5.1), le faisceau $\mathcal{O}_{\mathrm{X}}$ est un faisceau cohérent d'anneaux.

Corollaire (1.5.3). — Sous les hypothèses de (1.5.1), tout faisceau cohérent sur un ouvert de X est induit par un faisceau cohérent sur X.

Corollaire (1.5.4). — Sous les hypothèses de (1.5.1), tout $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent $\mathcal{F}$ est limite inductive des sous-$\mathcal{O}_{\mathrm{X}}$-Modules cohérents de $\mathcal{F}$.

En effet, $\mathcal{F} = \widetilde{\mathbf{M}}$ où $\mathbf{M}$ est un A-module, et $\mathbf{M}$ est limite inductive de ses sous-modules de type fini; on conclut par (1.3.9) et (1.5.1).

## 1.6. Propriétés fonctorielles des faisceaux quasi-cohérents sur un spectre premier.

(1.6.1) Soient A, A' deux anneaux,

$$
\varphi : \mathrm{A} ^ {\prime} \rightarrow \mathrm{A}.
$$

un homomorphisme,

$$
{ } ^ { a } \varphi : X = \operatorname{Spec} (A) \rightarrow X ^ { \prime } = \operatorname{Spec} (A ^ { \prime })
$$

l'application continue associée à $\varphi$ (1.2.1). Nous allons définir un homomorphisme canonique

$$
\widetilde {\varphi}: \mathcal {O} _ {\mathrm{X} ^ {\prime}} \rightarrow^ {a} \varphi_ {*} (\mathcal {O} _ {\mathrm{X}})
$$

de faisceaux d'anneaux. Pour tout $f' \in A'$, posons $f = \varphi(f')$; on a $^a\varphi^{-1}(D(f')) = D(f)$ (1.2.2.2). Les anneaux $\Gamma(D(f'), \widetilde{A}')$ et $\Gamma(D(f), \widetilde{A})$ s'identifient respectivement à $A'_f$ et $A_f$ (1.3.6 et 1.3.7). Or, l'homomorphisme $\varphi$ définit canoniquement un homomorphisme $\varphi_{f'} : A'_f \to A_f$ (0, 1.5.1), autrement dit on a un homomorphisme d'anneaux

$$
\Gamma (\mathrm{D} (f ^ {\prime}), \widetilde {\mathrm{A}} ^ {\prime}) \rightarrow \Gamma (^ {a} \varphi^ {- 1} (\mathrm{D} (f ^ {\prime})), \widetilde {\mathrm{A}}) = \Gamma (\mathrm{D} (f ^ {\prime}), ^ {a} \varphi_ {*} (\widetilde {\mathrm{A}}))
$$

En outre, ces homomorphismes satisfont aux conditions de compatibilité usuelles : pour  $\mathrm{D}(f')\supset\mathrm{D}(g')$ , le diagramme

$$
\begin{array}{c} \Gamma (\mathbf {D} (f ^ {\prime}), \widetilde {\mathbf {A}} ^ {\prime}) \to \Gamma (\mathbf {D} (f ^ {\prime}), ^ {a} \varphi_ {*} (\widetilde {\mathbf {A}})) \\ \downarrow \qquad \qquad \qquad \qquad \downarrow \\ \Gamma (\mathbf {D} (g ^ {\prime}), \widetilde {\mathbf {A}} ^ {\prime}) \to \Gamma (\mathbf {D} (g ^ {\prime}), ^ {a} \varphi_ {*} (\widetilde {\mathbf {A}})) \end{array}
$$

est commutatif (0, 1.5.1); on a donc bien défini un homomorphisme de $\mathcal{O}_{\mathrm{X}^{\prime}}$-Algèbres, les $\mathrm{D}(f^{\prime})$ formant une base de la topologie de $\mathrm{X}^{\prime}$ (0, 3.2.3). Le couple $\Phi = (^{a}\varphi, \widetilde{\varphi})$ est donc un morphisme d'espaces annelés

$$
\Phi : (\mathrm{X}, \mathcal {O} _ {\mathrm{X}}) \rightarrow (\mathrm{X} ^ {\prime}, \mathcal {O} _ {\mathrm{X} ^ {\prime}})
$$

(0, 4.1.1).

Notons en outre que, si on pose $x' = {}^a \varphi(x)$, l'homomorphisme $\widetilde{\varphi}_x^\sharp(0, 3.7.1)$ n'est autre que l'homomorphisme

$$
\varphi_ {x}: \mathrm{A} _ {x ^ {\prime}} ^ {\prime} \rightarrow \mathrm{A} _ {x}
$$

déduit canoniquement de $\varphi: A' \to A(0, 1.5.1)$. En effet, tout $z' \in A_x'$ s'écrit $g'/f'$, où $f'$, $g'$ sont dans $A'$ et $f' \notin J_x'$; $D(f')$ est donc un voisinage de $x'$ dans $X'$, et l'homomorphisme $\Gamma(D(f'), \widetilde{A}') \to \Gamma(^a \varphi^{-1}(D(f))), \widetilde{A})$ déduit de $\widetilde{\varphi}$ n'est autre que $\varphi_{j'}$; en considérant la section $s' \in \Gamma(D(f'), \widetilde{A}')$ correspondant à $g'/f' \in A_{j'}$, on obtient bien $\widetilde{\varphi}_x^\sharp(z') = \varphi(g') / \varphi(f')$ dans $A_x$.

(1.6.2) Exemple. — Soient S une partie multiplicative de A, $\varphi$ l'homomorphisme canonique $A\to S^{-1}A$; on a déjà vu (1.2.6) que $^a\varphi$ est un homéomorphisme de $Y = \operatorname{Spec}(S^{-1}A)$ sur le sous-espace de $X = \operatorname{Spec}(A)$ formé des $x$ tels que $j_x\cap S = \emptyset$. En outre, pour tout $x$ appartenant à ce sous-espace, donc de la forme $^a\varphi(y)$ avec $y\in Y$, l'homomorphisme $\widetilde{\varphi}_{y}^{\sharp}:\mathcal{O}_x\to \mathcal{O}_y$ est bijectif (0, 1.2.6); autrement dit, $\mathcal{O}_Y$ s'identifie au faisceau induit sur Y par $\mathcal{O}_X$.

Proposition (1.6.3). — Pour tout A-module M, il existe un isomorphisme canonique fonctoriel du  $O_{X^{\prime}}$ -Module  $(\mathbf{M}_{[\varphi]})\sim$  sur l'image directe  $\Phi_{*}(\widetilde{\mathbf{M}})$ .

Posons pour abréger $\mathbf{M}' = \mathbf{M}_{[\varphi]}$, et pour tout $f' \in A'$, posons encore $f = \varphi(f')$. Les modules de sections $\Gamma(\mathrm{D}(f'), \widetilde{\mathbf{M}}')$ et $\Gamma(\mathrm{D}(f), \widetilde{\mathbf{M}})$ s'identifient respectivement aux modules $\mathbf{M}_{j'}'$ et $\mathbf{M}_j$ (sur $\mathbf{A}_{j'}'$ et $\mathbf{A}_j$ respectivement); en outre, le $\mathbf{A}_{j'}'$-module $(\mathbf{M}_j)_{[\varphi_{j'}]}$ est canoniquement isomorphe à $\mathbf{M}_{j'}'$ (0, 1.5.2). On a donc un isomorphisme fonctoriel de $\Gamma(\mathrm{D}(f'), \widetilde{\mathbf{A}}')$-modules: $\Gamma(\mathrm{D}(f'), \widetilde{\mathbf{M}}') \simeq \Gamma(^a\varphi^{-1}(\mathrm{D}(f'))$, $\widetilde{\mathbf{M}})_{[\varphi_{j'}]}$ et ces isomorphismes satisfont aux conditions de compatibilité usuelles avec les restrictions (0, 1.5.6), donc définissent l'isomorphisme fonctoriel annoncé. On notera que, de façon précise, si $u: \mathbf{M}_1 \to \mathbf{M}_2$ est un homomorphisme de A-modules, il peut être considéré comme un homomorphisme $(\mathbf{M}_1)_{[\varphi]} \to (\mathbf{M}_2)_{[\varphi]}$ de A'-modules; si on note $u_{[\varphi]}$ cet homomorphisme, $\Phi_*(\widetilde{u})$ s'identifie à $(u_{[\varphi]})^\sim$.

Cette démonstration prouve aussi que pour toute A-algèbre B, l'isomorphisme

canonique fonctoriel $(\mathbf{B}_{[\varphi]})^{\sim} \to \Phi_{*}(\widetilde{\mathbf{B}})$ est un isomorphisme de $\mathcal{O}_{\mathrm{X}^{\prime}}$-Algèbres; si M est un B-module, l'isomorphisme canonique fonctoriel $(\mathbf{M}_{[\varphi]})^{\sim} \simeq \Phi_{*}(\widetilde{\mathbf{M}})$ est un isomorphisme de $\Phi_{*}(\widetilde{\mathbf{B}})$-Modules.

Corollaire (1.6.4). — Le foncteur image directe $\Phi_{*}$ est exact sur la catégorie des $\mathcal{O}_{\mathrm{X}}$-Modules quasi-cohérents.

En effet, il est clair que  $M_{[\varphi]}$  est un foncteur exact en M et  $\widetilde{M}'$  un foncteur exact en  $M'$  (1.3.5).

Proposition (1.6.5). — Soient N' un A'-module, N le A-module N' ⊗\_{A'} A\_{[φ]}; il existe un isomorphisme canonique fonctoriel du O\_X-Module Φ\*(N') sur N.

Remarquons d'abord que $j: z' \to z' \otimes \mathrm{I}$ est un A'-homomorphisme de N' dans N$_{[\varphi]}$: en effet, par définition, pour $f' \in \mathrm{A}'$, on a $(f'z') \otimes \mathrm{I} = z' \otimes \varphi(f') = \varphi(f')(z' \otimes \mathrm{I})$. On en déduit (1.3.8) un homomorphisme $\widetilde{j}: \widetilde{\mathrm{N}}' \to (\mathrm{N}_{[\varphi]})^{\sim}$ de $\mathcal{O}_{\mathrm{x}'}$-Modules, et en vertu de (1.6.3), on peut considérer que $\widetilde{j}$ applique $\widetilde{\mathrm{N}}'$ dans $\Phi_{*}(\widetilde{\mathrm{N}})$. Il correspond canoniquement à cet homomorphisme $\widetilde{j}$ un homomorphisme $h = \widetilde{j}^{\sharp}$ de $\Phi^{*}(\widetilde{\mathrm{N}}')$ dans $\widetilde{\mathrm{N}}$ (0, 4.4.3); on va voir que pour chaque fibre, $h_x$ est bijectif. Posons $x' = ^a\varphi(x)$ et soit $f' \in \mathrm{A}'$ tel que $x' \in \mathrm{D}(f')$; soit $f = \varphi(f')$. L'anneau $\Gamma(\mathrm{D}(f), \widetilde{\mathrm{A}})$ s'identifie à $A_f$, les modules $\Gamma(\mathrm{D}(f), \widetilde{\mathrm{N}})$ et $\Gamma(\mathrm{D}(f'), \widetilde{\mathrm{N}}')$ à $N_f$ et $N_{f'}'$ respectivement; soient $s' \in \Gamma(\mathrm{D}(f'), \widetilde{\mathrm{N}}')$, identifiée à $n'/f'^p(n' \in N')$, s son image par $\widetilde{j}$ dans $\Gamma(\mathrm{D}(f), \widetilde{\mathrm{N}})$; s est identifiée à $(n' \otimes \mathrm{I})/f^p$. Soit d'autre part $t \in \Gamma(\mathrm{D}(f), \widetilde{\mathrm{A}})$, identifiée à $g/f^q(g \in A)$; alors, par définition, on a $h_x(s_x'\otimes t_x) = t_x.s_x(0, 4.4.3)$. Mais on peut identifier canoniquement $N_f$ à $N_{f'}' \otimes_{A_{f'}}(A_{f})_{[\varphi_{f'}]}(0, 1.5.4)$; s correspond alors à l'élément $(n'/f'^p) \otimes \mathrm{I}$, et la section $y \to t_y.s_y$ à $(n'/f'^p)\otimes(g/f^q)$. Les diagrammes de compatibilité de (0, 1.5.6) montrent que $h_x$ n'est autre que l'isomorphisme canonique

$$
\mathrm{N} _ {x ^ {\prime}} ^ {\prime} \otimes_ {\mathrm{A} _ {x ^ {\prime}} ^ {\prime}} (\mathrm{A} _ {x}) _ {[ \varphi_ {x ^ {\prime}} ]} \stackrel {{\sim}} {{\to}} \mathrm{N} _ {x} = (\mathrm{N} ^ {\prime} \otimes_ {\mathrm{A} ^ {\prime}} \mathrm{A} _ {[ \varphi ]}) _ {x}.\tag{1.6.5.1}
$$

En outre, soit $v: \mathbf{N}_1' \to \mathbf{N}_2'$ un homomorphisme de A'-modules; comme $\widetilde{v}_{x'} = v_{x'}$ pour tout $x' \in \mathbf{X}'$, il résulte aussitôt de ce qui précède que $\Phi^*(\widetilde{v})$ s'identifie canoniquement à $(v \otimes 1)^\sim$, ce qui achève la démonstration de (1.6.5).

Si B' est une A'-algèbre, l'isomorphisme canonique de $\Phi^{*}(\widetilde{\mathbf{B}}^{\prime})$ sur $(\mathbf{B}^{\prime}\otimes_{\mathbf{A}^{\prime}}\mathbf{A}_{[\varphi]})\sim$ est un isomorphisme de $\mathcal{O}_{X}$-Algèbres; si en outre N' est un B'-module, l'isomorphisme canonique de $\Phi^{*}(\widetilde{\mathbf{N}}^{\prime})$ sur $(\mathbf{N}^{\prime}\otimes_{\mathbf{A}^{\prime}}\mathbf{A}_{[\varphi]})\sim$ est un isomorphisme de $\Phi^{*}(\widetilde{\mathbf{B}}^{\prime})$-Modules.

Corollaire (r.6.6). — Les sections de $\Phi^{*}(\widetilde{\mathbb{N}}^{\prime})$ images canoniques des sections $s^{\prime}$, où $s^{\prime}$ parcourt le A'-module $\Gamma(\widetilde{\mathbb{N}}^{\prime})$, engendrent le A-module $\Gamma(\Phi^{*}(\mathbb{N}^{\prime}))$.

En effet, ces images s'identifient aux éléments  $z'\otimes i$  de N, lorsqu'on identifie  $N'$  et N à  $\Gamma(\widetilde{N}')$  et  $\Gamma(\widetilde{N})$  respectivement (1.3.7) et que  $z'$  parcourt  $N'$ .

(1.6.7) Dans la démonstration de (1.6.5), on a prouvé en passant que l'application canonique (0, 4.4.3.2) $\rho: \widetilde{\mathrm{N}}' \to \Phi_*(\Phi^*(\widetilde{\mathrm{N}}'))$ n'est autre que l'homomorphisme $\widetilde{j}$,

où $j: \mathbf{N}' \to \mathbf{N}' \otimes_{\mathbf{A}'} \mathbf{A}_{[\varphi]}$ est l'homomorphisme $z' \to z' \otimes \mathbf{I}$. De même, l'application canonique (0, 4.4.3.3) $\sigma: \Phi^*(\Phi_*(\widetilde{\mathbf{M}})) \to \widetilde{\mathbf{M}}$ n'est autre que $\widetilde{p}$, où $p: \mathbf{M}_{[\varphi]} \otimes_{\mathbf{A}'} \mathbf{A}_{[\varphi]} \to \mathbf{M}$ est l'homomorphisme canonique qui, à tout produit tensoriel $z \otimes a$ ($z \in \mathbf{M}, a \in \mathbf{A}$) fait correspondre $a.z$; cela résulte aussitôt des définitions (0, 3.7.1, 0, 4.4.3, et I, 1.3.7).

On en conclut (0, 4.4.3 et 3.5.4.4) que si $v: \mathbf{N}' \to \mathbf{M}_{[\varphi]}$ est un A'-homomorphisme, on a $\widetilde{v}^{\#} = (v \otimes \mathrm{I})^{\sim}$.

(1.6.8) Soient  $N_{1}^{\prime}$ ,  $N_{2}^{\prime}$  deux A'-modules,  $N_{1}^{\prime}$  étant supposé avoir une présentation finie; il résulte alors de (1.6.7) et (1.3.12, (ii)) que l'homomorphisme canonique (0, 4.4.6)

$$
\Phi^ {*} (\mathcal {H} o m _ {\tilde {\mathrm{A}} ^ {\prime}} (\widetilde {\mathrm{N}} _ {1} ^ {\prime}, \widetilde {\mathrm{N}} _ {2} ^ {\prime})) \rightarrow \mathcal {H} o m _ {\tilde {\mathrm{A}}} (\Phi^ {*} (\widetilde {\mathrm{N}} _ {1} ^ {\prime}), \Phi^ {*} (\widetilde {\mathrm{N}} _ {2} ^ {\prime}))
$$

n'est autre que $\widetilde{\gamma}$, en désignant par $\gamma$ l'homomorphisme canonique de A-modules $\mathrm{Hom}_{\mathbf{A}'}(\mathbf{N}_1', \mathbf{N}_2') \otimes_{\mathbf{A}'} \mathbf{A} \to \mathrm{Hom}_{\mathbf{A}}(\mathbf{N}_1' \otimes_{\mathbf{A}'} \mathbf{A}, \mathbf{N}_2' \otimes_{\mathbf{A}'} \mathbf{A})$.

(1.6.9) Soient $\mathfrak{J}'$ un idéal de A', M un A-module; comme par définition $\widetilde{\mathfrak{J}}'\widetilde{\mathbf{M}}$ est l'image de l'homomorphisme canonique $\Phi^{*}(\widetilde{\mathfrak{J}}')\otimes_{\widetilde{\mathbf{A}}}\widetilde{\mathbf{M}}\to\widetilde{\mathbf{M}}$, il résulte de (1.6.5) et (1.3.12, (i)) que $\widetilde{\mathfrak{J}}'\widetilde{\mathbf{M}}$ s'identifie canoniquement à $(\mathfrak{J}'\mathbf{M})^{\sim}$; en particulier, $\Phi^{*}(\widetilde{\mathfrak{J}}')\widetilde{\mathbf{A}}$ s'identifie à $(\mathfrak{J}'\mathbf{A})^{\sim}$, et en tenant compte de l'exactitude à droite du foncteur $\Phi^{*}$, la $\widetilde{\mathbf{A}}$-Algèbre $\Phi^{*}((\mathbf{A}'/\mathfrak{J}')^{\sim})$ s'identifie à $(\mathbf{A}/\mathfrak{J}'\mathbf{A})^{\sim}$.

(1.6.10) Soient A'' un troisième anneau, $\varphi'$ un homomorphisme $A''\to A'$, et posons $\varphi''=\varphi\circ\varphi'$. Il résulte aussitôt des définitions que $^a\varphi''=(^a\varphi')\circ(^a\varphi)$, et $\widetilde{\varphi}''=\widetilde{\varphi}\circ\widetilde{\varphi}'$ (0, 1.5.7). On en conclut que l'on a $\Phi''=\Phi'\circ\Phi$; en d'autres termes, (SpecA, $\widetilde{A}$) est un foncteur en A de la catégorie des anneaux dans celle des espaces annelés.

## 1.7. Caractérisation des morphismes de schémas affines.

Définition (1.7.1). — On dit qu'un espace annelé (X, $\mathcal{O}_{\mathrm{X}}$) est un schéma affine s'il est isomorphe à un espace annelé de la forme (Spec(A), $\widetilde{\mathrm{A}}$), où A est un anneau; on dit alors que $\Gamma(\mathrm{X},\mathcal{O}_{\mathrm{X}})$, qui s'identifie canoniquement à l'anneau A (1.3.7) est l'anneau du schéma affine (X, $\mathcal{O}_{\mathrm{X}}$), et on le note A(X) quand aucune confusion n'en résulte.

Par abus de langage, quand nous parlerons du schéma affine $\operatorname{Spec}(A)$, il s'agira toujours de l'espace annelé $(\operatorname{Spec}(A), \widetilde{A})$.

(1.7.2) Soient A, B deux anneaux,  $(\mathbf{X}, \mathcal{O}_{\mathbf{X}})$ ,  $(\mathbf{Y}, \mathcal{O}_{\mathbf{Y}})$  les schémas affines correspondants sur les spectres premiers  $\mathbf{X} = \operatorname{Spec}(\mathbf{A})$ ,  $\mathbf{Y} = \operatorname{Spec}(\mathbf{B})$ . On a vu (1.6.1) qu'à tout homomorphisme d'anneaux  $\varphi : B \to A$  correspond un morphisme  $\Phi = (^{a}\varphi, \widetilde{\varphi}) = \operatorname{Spec}(\varphi) : (\mathbf{X}, \mathcal{O}_{\mathbf{X}}) \to (\mathbf{Y}, \mathcal{O}_{\mathbf{Y}})$ . On notera que  $\varphi$  est entièrement déterminé par  $\Phi$ , car on a par définition  $\varphi = \Gamma(\widetilde{\varphi}) : \Gamma(\widetilde{\mathbf{B}}) \to \Gamma(^{a}\varphi_{*}(\widetilde{\mathbf{A}})) = \Gamma(\widetilde{\mathbf{A}})$ .

Théorème (1.7.3). — Soient (X, $\mathcal{O}_{\mathrm{X}}$), (Y, $\mathcal{O}_{\mathrm{Y}}$) deux schémas affines. Pour qu'un morphisme d'espaces annelés ($\psi$, $\theta$): (X, $\mathcal{O}_{\mathrm{X}}$)→(Y, $\mathcal{O}_{\mathrm{Y}}$) soit de la forme ($^a\varphi$, $\widetilde{\varphi}$), où $\varphi$ est un homomorphisme d'anneaux : A(Y)→A(X), il faut et il suffit que, pour tout $x \in \mathrm{X}$, $\theta_{x}^{\sharp}$ soit un homomorphisme local : $\mathcal{O}_{\psi(x)} \to \mathcal{O}_{x^{*}}$.

Posons $\mathrm{A} = \mathrm{A}(\mathrm{X}), \mathrm{B} = \mathrm{A}(\mathrm{Y})$. La condition est nécessaire, car on a vu (1.6.1) que $\widetilde{\varphi}_{x}^{\sharp}$ est l'homomorphisme de $\mathrm{B}_{a_{\varphi(x)}}$ dans $\mathrm{A}_x$ déduit canoniquement de $\varphi$, et par définition de $^a\varphi(x) = \varphi^{-1}(\mathbf{j}_x)$, cet homomorphisme est local.

Prouvons que la condition est suffisante. Par définition, $\theta$ est un homomorphisme $\mathcal{O}_{\mathrm{Y}} \to \psi_{*}(\mathcal{O}_{\mathrm{X}})$, et on en déduit canoniquement un homomorphisme d'anneaux

$$
\varphi = \Gamma (\theta): B = \Gamma (Y, \mathcal {O} _ {Y}) \rightarrow \Gamma (Y, \psi_ {*} (\mathcal {O} _ {X})) = \Gamma (X, \mathcal {O} _ {X}) = A.
$$

L'hypothèse sur $\theta_x^\sharp$ permet de déduire de cet homomorphisme, par passage aux quotients, un monomorphisme $\theta^x$ du corps des restes $k(\psi(x))$ dans le corps des restes $k(x)$, tel que, pour toute section $f \in \Gamma(Y, \mathcal{O}_Y) = B$, on ait $\theta^x(f(\psi(x))) = \varphi(f)(x)$. La relation $f(\psi(x)) = o$ est donc équivalente à $\varphi(f)(x) = o$, ce qui signifie que $i_{\psi(x)} = j^{a_{\varphi(x)}}$, et s'écrit encore $\psi(x) = ^a\varphi(x)$ pour tout $x \in X$, ou $\psi = ^a\varphi$. On sait aussi que le diagramme

$$
\begin{array}{c} \mathrm{B} = \Gamma (\mathrm{Y}, \mathcal {O} _ {\mathrm{Y}}) \xrightarrow {\varphi} \Gamma (\mathrm{X}, \mathcal {O} _ {\mathrm{X}}) = \mathrm{A} \\ \downarrow \\ \mathrm{B} _ {\psi (x)} \xrightarrow [ \theta_ {c} ^ {\sharp} ]{\quad} \mathrm{A} _ {x} \end{array}
$$

est commutatif (0, 3.7.2), ce qui signifie que $\theta_{x}^{\sharp}$ est égal à l'homomorphisme $\varphi_{x}: B_{\psi(x)} \to A_{x}$ déduit canoniquement de $\varphi$ (0, 1.5.1). Comme la donnée des $\theta_{x}^{\sharp}$ caractérise complètement $\theta^{\sharp}$, et par suite aussi $\theta$ (0, 3.7.1), on en conclut que l'on a $\theta = \widetilde{\varphi}$, par définition de $\widetilde{\varphi}$ (1.6.1).

Nous dirons qu'un morphisme $(\psi, \theta)$ d'espaces annelés satisfaisant à la condition de (1.7.3) est un morphisme de schémas affines.

Corollaire (1.7.4). — Si (X, $\mathcal{O}_{\mathrm{X}}$), (Y, $\mathcal{O}_{\mathrm{Y}}$) sont deux schémas affines, il existe un isomorphisme canonique de l'ensemble de morphismes de schémas affines Hom((X, $\mathcal{O}_{\mathrm{X}}$), (Y, $\mathcal{O}_{\mathrm{Y}}$)) sur l'ensemble d'homomorphismes d'anneaux de B dans A, où $\mathrm{A} = \Gamma(\mathcal{O}_{\mathrm{X}})$ et $\mathrm{B} = \Gamma(\mathcal{O}_{\mathrm{Y}})$.

On peut encore dire que les foncteurs (Spec(A), $\widetilde{A}$) en A et $\Gamma(X, \mathcal{O}_{X})$ en $(X, \mathcal{O}_{X})$ définissent une équivalence de la catégorie des anneaux commutatifs et de la catégorie duale de la catégorie des schémas affines (T, I, r.2).

Corollaire (1.7.5). — Si $\varphi: B \to A$ est surjectif, le morphisme correspondant ($^{a}\varphi$, $\widetilde{\varphi}$) est un monomorphisme d'espaces annelés (cf. (4.1.7)).

On sait en effet que $^a\varphi$ est injective (1.2.5), et comme $\varphi$ est surjectif, pour tout $x \in X$, $\varphi_x^\sharp : B_{a_\varphi(x)} \to A_x$, qui se déduit de $\varphi$ par passage aux anneaux de fractions, est aussi surjectif (0, 1.5.1); d'où la conclusion (0, 4.1.1).

## § 2. PRÉSCHÉMAS ET MORPHISMES DE PRÉSCHÉMAS

## 2.1. Définition des préschémas.

(2.1.1) Étant donné un espace annelé (X, $\mathcal{O}_{\mathrm{X}}$), on dit qu'une partie ouverte V de X est un ouvert affine si l'espace annelé (V, $\mathcal{O}_{\mathrm{X}}|\mathrm{V}$) est un schéma affine (1.7.1).

Définition (2.1.2). — On appelle préschéma un espace annelé (X, $\mathcal{O}_{\mathrm{X}}$) tel que tout point de X admette un voisinage ouvert affine.

Proposition (2.1.3). — Si (X, $\mathcal{O}_{\mathrm{X}}$) est un préschéma, les ensembles ouverts affines forment une base de la topologie de X.

En effet, si V est un voisinage ouvert quelconque de $x\in\mathbf{X}$, il existe par hypothèse un voisinage ouvert W de $x$ tel que $(W,\mathcal{O}_{\mathrm{X}}|W)$ soit un schéma affine ; désignons par A son anneau. Dans l'espace W, $V\cap W$ est un voisinage ouvert de $x$; donc il existe $f\in\mathbf{A}$ tel que D(f) soit un voisinage ouvert de $x$ contenu dans $V\cap W$ (1.1.10 (i)). L'espace annelé $(D(f),\mathcal{O}_{\mathrm{X}}|D(f))$ est alors un schéma affine d'anneau isomorphe à $A_{f}$ (1.3.6), d'où la proposition.

Proposition (2.1.4). — L'espace sous-jacent d'un préschéma est un espace de Kolmogoroff.

En effet, si $x, y$ sont deux points distincts d'un préschéma X, il est évident qu'il existe un voisinage ouvert de l'un de ces points ne contenant pas l'autre si $x, y$ ne sont pas dans un même ouvert affine ; et s'ils sont dans un même ouvert affine, cela résulte de (1.1.8).

Proposition (2.1.5). — Si (X, $\mathcal{O}_{\mathrm{X}}$) est un préschéma, toute partie fermée irréductible de X admet un point générique et un seul, et l'application $x \to \overline{\{x\}}$ est donc une bijection de X sur l'ensemble de ses parties fermées irréductibles.

En effet, si Y est une partie fermée irréductible de X et  $y \in Y$ , et si U est un voisinage ouvert affine de y dans X,  $U \cap Y$  est partout dense dans Y et est irréductible (0, 2.1.1 et 2.1.4); donc (1.1.14),  $U \cap Y$  est l'adhérence dans U d'un point x, et par suite  $Y \subset \overline{U}$  est l'adhérence de x dans X. L'unicité du point générique de X résulte de (2.1.4) et de (0, 2.1.3).

(2.1.6) Si Y est une partie fermée irréductible de X, y son point générique, l'anneau local  $O_{y}$  se note aussi  $O_{X/Y}$  et s'appelle l'anneau local de X le long de Y, ou l'anneau local de Y dans X.

Si X lui-même est irréductible et si $x$ est son point générique, on dit encore que $\mathcal{O}_x$ est l'anneau des fonctions rationnelles sur X (cf. § 7).

Proposition (2.1.7). — Si (X, $\mathcal{O}_{\mathrm{X}}$) est un préschéma, pour toute partie ouverte U de X, l'espace annelé (U, $\mathcal{O}_{\mathrm{X}}|\mathrm{U}$) est un préschéma.

Cela résulte aussitôt de la déf. (2.1.2) et de la prop. (2.1.3).

On dit que  $(\mathbf{U}, \mathcal{O}_{\mathbf{X}}|\mathbf{U})$  est le préschéma induit sur U par  $(\mathbf{X}, \mathcal{O}_{\mathbf{X}})$ , ou la restriction de  $(\mathbf{X}, \mathcal{O}_{\mathbf{X}})$  à U.

(2.1.8) On dit qu'un préschéma (X, $\mathcal{O}_{\mathrm{X}}$) est irréductible (resp. connexe) si l'espace sous-jacent X est irréductible (resp. connexe). On dit qu'un préschéma est intègre s'il est irréductible et réduit (cf. (5.1.4)). On dit qu'un préschéma (X, $\mathcal{O}_{\mathrm{X}}$) est localement intègre si tout $x \in \mathrm{X}$ admet un voisinage ouvert U tel que le préschéma induit sur U par (X, $\mathcal{O}_{\mathrm{X}}$) soit intègre.

## 2.2. Morphismes de préschémas.

Définition (2.2.1). — Étant donnés deux préschémas (X, $\mathcal{O}_{\mathrm{X}}$), (Y, $\mathcal{O}_{\mathrm{Y}}$), on appelle morphisme (de préschémas) de (X, $\mathcal{O}_{\mathrm{X}}$) dans (Y, $\mathcal{O}_{\mathrm{Y}}$) tout morphisme d'espaces annelés ($\psi$, $\theta$) tel que, pour tout $x \in \mathrm{X}$, $\theta_{x}^{\sharp}$ soit un homomorphisme local: $\mathcal{O}_{\psi(x)} \to \mathcal{O}_{x}$.

Par passage aux quotients, l'application $\theta_{x}^{\sharp}:\mathcal{O}_{\psi(x)}\to\mathcal{O}_{x}$ donne donc un monomorphisme $\theta^{x}:k(\psi(x))\to k(x)$, qui permet de considérer $k(x)$ comme une extension du corps $k(\psi(x))$.

(2.2.2) Le composé  $(\psi^{\prime\prime}, \theta^{\prime\prime})$  de deux morphismes de préschémas  $(\psi, \theta)$  et  $(\psi', \theta')$  est encore un morphisme de préschémas, comme il résulte de la formule  $\theta^{\prime\prime\sharp} = \theta^{\sharp}\circ\psi^{*}(\theta^{\prime\sharp})$  (0, 3.5.5). On en conclut que les préschémas forment une catégorie ; suivant la notation générale, on écrira Hom(X, Y) l'ensemble des morphismes d'un préschéma X dans un préschéma Y.

Exemple (2.2.3). — Si U est une partie ouverte de X, l'injection canonique (0, 4.1.2) du préschéma induit (U, $\mathcal{O}_{\mathrm{X}}|\mathrm{U}$) dans (X, $\mathcal{O}_{\mathrm{X}}$) est un morphisme de préschémas; c'est d'ailleurs un monomorphisme d'espaces annelés (et a fortiori un monomorphisme de préschémas), comme il résulte aussitôt de (0, 4.1.1).

Proposition (2.2.4). — Soient (X, $\mathcal{O}_{\mathrm{X}}$) un préschéma, (S, $\mathcal{O}_{\mathrm{S}}$) un schéma affine d'anneau A. Il existe une correspondance biunivoque canonique entre les morphismes du préschéma (X, $\mathcal{O}_{\mathrm{X}}$) dans le préschéma (S, $\mathcal{O}_{\mathrm{S}}$) et les homomorphismes de A dans l'anneau $\Gamma(\mathrm{X}, \mathcal{O}_{\mathrm{X}})$.

Notons d'abord que, si  $(\mathbf{X}, \mathcal{O}_{\mathbf{X}})$  et  $(\mathbf{Y}, \mathcal{O}_{\mathbf{Y}})$  sont deux espaces annelés quelconques, un morphisme  $(\psi, \theta)$  de  $(\mathbf{X}, \mathcal{O}_{\mathbf{X}})$  dans  $(\mathbf{Y}, \mathcal{O}_{\mathbf{Y}})$  définit canoniquement un homomorphisme d'anneaux  $\Gamma(\theta): \Gamma(\mathbf{Y}, \mathcal{O}_{\mathbf{Y}}) \to \Gamma(\mathbf{Y}, \psi_{*}(\mathcal{O}_{\mathbf{X}})) = \Gamma(\mathbf{X}, \mathcal{O}_{\mathbf{X}})$ . Dans le cas considéré, tout revient à voir qu'un homomorphisme quelconque  $\varphi: A \to \Gamma(\mathbf{X}, \mathcal{O}_{\mathbf{X}})$  est de la forme  $\Gamma(\theta)$  pour un  $\theta$  et un seul. Or, il y a par hypothèse un recouvrement  $(\mathrm{V}_{\alpha})$  de X par des ouverts affines; par composition de  $\varphi$  avec l'homomorphisme de restriction  $\Gamma(\mathbf{X}, \mathcal{O}_{\mathbf{X}}) \to \Gamma(\mathrm{V}_{\alpha}, \mathcal{O}_{\mathbf{X}} | \mathrm{V}_{\alpha})$ , on obtient un homomorphisme  $\varphi_{\alpha}: A \to \Gamma(V_{\alpha}, \mathcal{O}_{\mathbf{X}} | V_{\alpha})$ , qui correspond à un morphisme unique  $(\psi_{\alpha}, \theta_{\alpha})$  du préschéma  $(\mathrm{V}_{\alpha}, \mathcal{O}_{\mathrm{X}} | V_{\alpha})$  dans  $(\mathrm{S}, \mathcal{O}_{\mathrm{S}})$ , en vertu de (1.7.3). En outre, pour tout couple d'indices  $(\alpha, \beta)$ , tout point de  $V_{\alpha} \cap V_{\beta}$  admet un voisinage ouvert affine W contenu dans  $V_{\alpha} \cap V_{\beta}$  (2.1.3); il est clair qu'en composant  $\varphi_{\alpha}$  et  $\varphi_{\beta}$  avec les homomorphismes de restriction à W, on obtient le même homomorphisme  $\Gamma(\mathrm{S}, \mathcal{O}_{\mathrm{S}}) \to \Gamma(\mathrm{W}, \mathcal{O}_{\mathrm{X}} | \mathrm{W})$ , donc, en vertu des relations  $(\theta_{\alpha}^{\sharp})_{x} = (\varphi_{\alpha})_{x}$  pour tout  $x \in V_{\alpha}$  et tout  $\alpha$  (1.6.1), les restrictions à W des morphismes  $(\psi_{\alpha}, \theta_{\alpha})$  et  $(\psi_{\beta}, \theta_{\beta})$  coïncident. On en conclut qu'il y a un morphisme d'espaces annelés  $(\psi, \theta): (\mathrm{X}, \mathcal{O}_{\mathrm{X}}) \to (\mathrm{S}, \mathcal{O}_{\mathrm{S}})$  et un seul dont la restriction à chaque  $V_{\alpha}$  est  $(\psi_{\alpha}, \theta_{\alpha})$  et il est clair que ce morphisme est un morphisme de préschémas et est tel que  $\Gamma(\theta) = \varphi$ .

Soit $u: \mathbf{A} \to \Gamma(\mathbf{X}, \mathcal{O}_{\mathbf{X}})$ un homomorphisme d'anneaux, et soit $v = (\psi, \theta)$ le morphisme $(\mathbf{X}, \mathcal{O}_{\mathbf{X}}) \to (\mathbf{S}, \mathcal{O}_{\mathbf{S}})$ correspondant. Pour tout $f \in \mathbf{A}$, on a

$$
\psi^ {- 1} (\mathrm{D} (f)) = \mathrm{X} _ {u (f)}\tag{2.2.4.1}
$$

avec les notations de (0, 5.5.2) relatives au faisceau localement libre $\mathcal{O}_{\mathrm{x}}$. Il suffit en effet de vérifier cette formule lorsque X lui-même est affine, et alors elle n'est autre que (1.2.2.2).

Proposition (2.2.5). — Sous les hypothèses de (2.2.4), soient $\varphi: A \to \Gamma(X, \mathcal{O}_X)$ un homomorphisme d'anneau, $f: (X, \mathcal{O}_X) \to (S, \mathcal{O}_S)$ le morphisme de préschémas correspondant, $\mathcal{G}$ (resp. $\mathcal{F}$) un $\mathcal{O}_X$-Module (resp. un $\mathcal{O}_S$-Module) quasi-cohérent et soit $M = \Gamma(S, \mathcal{F})$. Il existe alors une

correspondance biunivoque canonique entre les $f$-morphismes $\mathcal{F} \to \mathcal{G}$ (0, 4.4.1) et les A-homomorphismes $\mathbf{M} \to (\Gamma(\mathbf{X}, \mathcal{G}))_{[\varphi]}$.

En effet, en raisonnant comme dans (2.2.4), on est aussitôt ramené au cas où X est affine et la proposition résulte alors de (1.6.3) et (1.3.8).

(2.2.6) On dit qu'un morphisme de préschémas $(\psi, \theta): (X, \mathcal{O}_{X}) \to (Y, \mathcal{O}_{Y})$ est ouvert (resp. fermé), si pour toute partie ouverte U de X (resp. toute partie fermée F de X), $\psi(U)$ est ouvert dans Y (resp. $\psi(F)$ fermé dans Y). On dit que $(\psi, \theta)$ est dominant si $\psi(X)$ est dense dans Y, surjectif si $\psi$ est surjectif. On notera que ces conditions ne font intervenir que l'application continue $\psi$.

Proposition (2.2.7). — Soient

$$
f = (\psi , \theta): (X, \mathcal {O} _ {X}) \rightarrow (Y, \mathcal {O} _ {Y}), \quad g = (\psi^ {\prime}, \theta^ {\prime}): (Y, \mathcal {O} _ {Y}) \rightarrow (Z, \mathcal {O} _ {Z})
$$

deux morphismes de préschémas.

(i) Si f et g sont tous deux ouverts (resp. fermés, dominants, surjectifs), il en est de même de gof.

(ii) Si f est surjectif, et si gof est fermé, g est fermé.

(iii) Si gof est surjectif, g est surjectif.

Les assertions (i) et (iii) sont évidentes. Posons $g \circ f = (\psi'', \theta'')$. Si F est fermé dans Y, $\psi^{-1}(F)$ est fermé dans X, donc $\psi''(\psi^{-1}(F))$ est fermé dans Z; mais comme $\psi$ est surjectif, $\psi(\psi^{-1}(F)) = F$, donc $\psi''(\psi^{-1}(F)) = \psi'(F)$, ce qui démontre (ii).

Proposition (2.2.8). — Soient $f = (\psi, \theta)$ un morphisme $(\mathrm{X}, \mathcal{O}_{\mathrm{X}}) \to (\mathrm{Y}, \mathcal{O}_{\mathrm{Y}})$, $(\mathrm{U}_{\alpha})$ un recouvrement ouvert de Y. Pour que $f$ soit ouvert (resp. fermé, surjectif, dominant), il faut et il suffit que sa restriction à chacun des préschémas induits $(\psi^{-1}(\mathrm{U}_{\alpha}), \mathcal{O}_{\mathrm{X}}|\psi^{-1}(\mathrm{U}_{\alpha}))$, considérée comme un morphisme de ce préschéma induit dans le préschéma induit $(\mathrm{U}_{\alpha}, \mathcal{O}_{\mathrm{Y}}|\mathrm{U}_{\alpha})$, soit ouvert (resp. fermé, surjectif, dominant).

La proposition résulte aussitôt des définitions, tenant compte du fait qu'une partie F de Y est fermée (resp. ouverte, dense) dans Y si et seulement si chacun des ensembles  $F \cap U_{\alpha}$  est fermé (resp. ouvert, dense) dans  $U_{\alpha}$ .

(2.2.9) Soient (X, $\mathcal{O}_{\mathrm{X}}$), (Y, $\mathcal{O}_{\mathrm{Y}}$) deux préschémas; on suppose que X et Y ont un même nombre fini de composantes irréductibles $\mathrm{X}_{i}$ (resp. $\mathrm{Y}_{i}$) ($\mathrm{i} \leqslant i \leqslant n$); soit $\xi_{i}$ (resp. $\eta_{i}$) le point générique de $\mathrm{X}_{i}$ (resp. $\mathrm{Y}_{i}$) (2.1.5). On dit qu'un morphisme

$$
f = (\psi , \theta): (X, \mathcal {O} _ {X}) \rightarrow (Y, \mathcal {O} _ {Y})
$$

est birationnel si, pour tout $i$, $\psi^{-1}(\eta_i) = \{\xi_i\}$ et $\theta_{\xi_i}^{\sharp}: \mathcal{O}_{\eta_i} \to \mathcal{O}_{\xi_i}$ est un isomorphisme. Il est clair qu'un morphisme birationnel est dominant (0, 2.1.8), donc surjectif s'il est aussi fermé.

Convention de notations (2.2.10). — Dans toute la suite de cet ouvrage et lorsque cela ne risquera pas de créer des confusions, nous supprimerons dans la notation d'un préschéma (resp. d'un morphisme) le faisceau structural (resp. le morphisme de faisceaux structuraux). Si U est une partie ouverte de l'espace sous-jacent d'un préschéma X, lorsqu'on parlera de U comme d'un préschéma, il s'agira toujours du préschéma induit sur U.

## 2.3. Recollement de préschémas.

(2.3.1) Il résulte de la définition (2.1.2) que tout espace annelé obtenu par recollement de préschémas (0, 4.1.6) est encore un préschéma. En particulier, puisque tout préschéma admet par définition un recouvrement formé d'ensembles ouverts affines, on voit que tout préschéma peut s'obtenir par recollement de schémas affines.

Exemple (2.3.2). — Soient K un corps, B=K[s], C=K[t] deux anneaux de polynômes à une indéterminée sur K, et soient  $X_{1}=Spec(B)$ ,  $X_{2}=Spec(C)$ , qui sont deux schémas affines isomorphes. Dans  $X_{1}$  (resp.  $X_{2}$ ), soit  $U_{12}$  (resp.  $U_{21}$ ) l'ouvert affine  $D(s)$  (resp.  $D(t)$ ) dont l'anneau  $B_{s}$  (resp.  $C_{t}$ ) est formé des fractions rationnelles de la forme  $f(s)/s^{m}$  (resp.  $g(t)/t^{n}$ ) avec  $f\in B$  (resp.  $g\in C$ ). Soit  $u_{12}$  l'isomorphisme de préschémas  $U_{21}\to U_{12}$  correspondant (2.2.4) à l'isomorphisme de B sur C qui, à  $f(s)/s^{m}$  fait correspondre la fraction rationnelle  $f(\mathbf{I}/t)/(\mathbf{I}/t^{m})$ . On peut recoller  $X_{1}$  et  $X_{2}$  le long de  $U_{12}$  et  $U_{21}$  au moyen de  $u_{12}$ , car il n'y a évidemment pas de condition de recollement. Nous retrouverons plus tard le préschéma X ainsi obtenu comme cas particulier d'une méthode de construction générale (II, 2.4.3). Montrons seulement ici que X n'est pas un schéma affine; cela résultera de ce que l'anneau  $\Gamma(X, O_{X})$  est isomorphe à K, donc a un spectre réduit à un point. En effet, une section de  $O_{X}$  au-dessus de X a une restriction au-dessus de  $X_{1}$  (resp.  $X_{2}$ ), identifié à un ouvert affine de X, qui est un polynôme  $f(s)$  (resp.  $g(t)$ ), et il résulte des définitions que l'on doit avoir  $g(t)=f(\mathbf{I}/t)$ , ce qui n'est possible que si  $f=g\in K$ .

## 2.4. Schémas locaux.

(2.4.1) On appelle schéma local un schéma affine dont l'anneau A est local ; il existe alors dans X=Spec(A) un seul point fermé a, et pour tout autre point b∈X, on a  $a\in\overline{\{b\}}$  (I.I.7).

Pour tout préschéma Y et tout point $y \in \mathbf{Y}$, le schéma local $\operatorname{Spec}(\mathcal{O}_y)$ est appelé le schéma local de Y au point $y$. Soient V un ouvert affine de Y contenant $y$, B l'anneau du schéma affine V; $\mathcal{O}_y$ s'identifie canoniquement à $\mathbf{B}_y$ (1.3.4), et l'homomorphisme canonique $\mathbf{B} \to \mathbf{B}_y$ correspond par suite (1.6.1) à un morphisme de préschémas $\operatorname{Spec}(\mathcal{O}_y) \to \mathbf{V}$. Si on compose ce morphisme avec l'injection canonique $\mathbf{V} \to \mathbf{Y}$, on obtient donc un morphisme $\operatorname{Spec}(\mathcal{O}_y) \to \mathbf{Y}$, qui est indépendant de l'ouvert affine V (contenant $y$) choisi : en effet, si $\mathbf{V}'$ est un second ouvert affine contenant $y$, il existe un troisième ouvert affine W contenant $y$ et tel que $\mathbf{W} \subset \mathbf{V} \cap \mathbf{V}'$ (2.1.3); on peut donc se limiter au cas où $\mathbf{V} \subset \mathbf{V}'$, et si $\mathbf{B}'$ est l'anneau de $\mathbf{V}'$, tout revient à remarquer que le diagramme

$$
\begin{array}{c} \mathrm{B} ^ {\prime} \to \mathrm{B} \\ \searrow \swarrow \\ \mathcal {O} _ {y} \end{array}
$$

est commutatif (0, 1.5.1). Le morphisme

$$
\operatorname{Spec} \left(\mathcal {O} _ {y}\right)\rightarrow \mathrm{Y}
$$

ainsi défini est dit canonique.

Proposition (2.4.2). — Soit (Y, $\mathcal{O}_{\mathrm{Y}}$) un préschéma; pour tout $y \in \mathrm{Y}$, soit $(\psi, \theta)$ le morphisme canonique $(\operatorname{Spec}(\mathcal{O}_y), \widetilde{\mathcal{O}}_y) \to (\mathrm{Y}, \mathcal{O}_{\mathrm{Y}})$. Alors $\psi$ est un homéomorphisme de $\operatorname{Spec}(\mathcal{O}_y)$ sur le sous-espace $S_y$ de Y formé des $z$ tels que $y \in \overline{\{z\}}$ (autrement dit, des générisations de $y(0, 2.1.2)$); en outre, si $z = \psi(p)$, $\theta_z^\sharp : \mathcal{O}_z \to (\mathcal{O}_y)_p$ est un isomorphisme; $(\psi, \theta)$ est donc un monomorphisme d'espaces annelés.

Comme l'unique point fermé $a$ de $\operatorname{Spec}(\mathcal{O}_y)$ est adhérent à tout point de cet espace, et que $\psi(a)=y$, l'image de $\operatorname{Spec}(\mathcal{O}_y)$ par l'application continue $\psi$ est contenue dans $S_y$. Comme $S_y$ est contenu dans tout ouvert affine contenant $y$, on peut se ramener au cas où Y est un schéma affine ; mais dans ce cas la proposition résulte de (1.6.2).

On voit donc (2.1.5) qu'il y a correspondance biunivoque entre $\operatorname{Spec}(\mathcal{O}_{y})$ et l'ensemble des parties fermées irréductibles de Y contenant $y$.

Corollaire (2.4.3). — Pour que  $y \in Y$  soit le point générique d'une composante irréductible de Y, il faut et il suffit que le seul idéal premier de l'anneau local  $O_{y}$  soit son idéal maximal (autrement dit, que  $O_{y}$  soit de dimension zéro).

Proposition (2.4.4). — Soient (X, $\mathcal{O}_{\mathrm{X}}$) un schéma local d'anneau A, a son unique point fermé, (Y, $\mathcal{O}_{\mathrm{Y}}$) un préschéma. Tout morphisme $u = (\psi, \theta) : (\mathrm{X}, \mathcal{O}_{\mathrm{X}}) \to (\mathrm{Y}, \mathcal{O}_{\mathrm{Y}})$ se factorise de façon unique en X→Spec($\mathcal{O}_{\psi(a)}$→Y, où la seconde flèche désigne le morphisme canonique, et la première correspond à un homomorphisme local $\mathcal{O}_{\psi(a)} \to \mathrm{A}$. Cela établit une correspondance biunivoque canonique entre l'ensemble des morphismes (X, $\mathcal{O}_{\mathrm{X}}$→(Y, $\mathcal{O}_{\mathrm{Y}}$) et l'ensemble des homomorphismes locaux $\mathcal{O}_{y} \to \mathrm{A}$ ($y \in \mathrm{Y}$).

En effet, pour tout $x \in X$, on a $a \in \overline{\{x\}}$, donc $\psi(a) \in \overline{\{\psi(x)\}}$, ce qui prouve que $\psi(X)$ est contenu dans tout ouvert affine contenant $\psi(a)$. On peut donc se ramener au cas où $(Y, \mathcal{O}_Y)$ est un schéma affine d'anneau $B$, et on a alors $u = (^a\varphi, \widetilde{\varphi})$, où $\varphi \in \text{Hom}(B, A)$ (1.7.3). En outre, on a $\varphi^{-1}(j_a) = j_{\psi(a)}$, et par suite l'image par $\varphi$ de tout élément de $B - j_{\psi(a)}$ est inversible dans l'anneau local $A$; la factorisation de l'énoncé résulte donc de la propriété universelle des anneaux de fractions (0, 1.2.4). Inversement, à tout homomorphisme local $\mathcal{O}_y \to A$ correspond un morphisme unique $(\psi, \theta): X \to \text{Spec}(\mathcal{O}_y)$ tel que $\psi(a) = y$ (1.7.3), et en le composant avec le morphisme canonique $\text{Spec}(\mathcal{O}_y) \to Y$, on obtient un morphisme $X \to Y$, ce qui achève de démontrer la proposition.

(2.4.5) Les schémas affines dont l'anneau est un corps K ont un espace sous-jacent réduit à un point. Si A est un anneau local d'idéal maximal m, tout homomorphisme local A→K a un noyau égal à m, donc se factorise en A→A/m→K, où la seconde flèche est un monomorphisme. Les morphismes Spec(K)→Spec(A) correspondent donc biunivoquement aux monomorphismes de corps A/m→K.

Soit (Y, $\mathcal{O}_{\mathrm{Y}}$) un préschéma ; pour tout $y \in \mathrm{Y}$ et tout idéal $\mathfrak{a}_y$ de $\mathcal{O}_{y}$, l'homomorphisme canonique $\mathcal{O}_y \to \mathcal{O}_y / \mathfrak{a}_y$ définit un morphisme $\operatorname{Spec}(\mathcal{O}_y / \mathfrak{a}_y) \to \operatorname{Spec}(\mathcal{O}_y)$; si on le compose avec le morphisme canonique $\operatorname{Spec}(\mathcal{O}_y) \to \mathrm{Y}$, on obtient un morphisme $\operatorname{Spec}(\mathcal{O}_y / \mathfrak{a}_y) \to \mathrm{Y}$, dit encore canonique. Pour $\mathfrak{a}_y = \mathfrak{m}_y$, c'est-à-dire $\mathcal{O}_y / \mathfrak{a}_y = \kappa(y)$, la prop. (2.4.4) entraîne donc :

Corollaire (2.4.6). — Soient (X, $\mathcal{O}_{\mathrm{X}}$) un schéma local dont l'anneau est un corps K, $\xi$ l'unique point de X, (Y, $\mathcal{O}_{\mathrm{Y}}$) un préschéma. Tout morphisme $u: (\mathrm{X}, \mathcal{O}_{\mathrm{X}}) \to (\mathrm{Y}, \mathcal{O}_{\mathrm{Y}})$ se factorise de façon unique en $\mathrm{X} \to \operatorname{Spec}(\mathbb{K}(\psi(\xi))) \to \mathrm{Y}$, où la seconde flèche désigne le morphisme canonique, et la première correspond à un monomorphisme $\mathbb{K}(\psi(\xi)) \to \mathrm{K}$. Cela établit une correspondance biunivoque canonique entre l'ensemble des morphismes (X, $\mathcal{O}_{\mathrm{X}}) \to (\mathrm{Y}, \mathcal{O}_{\mathrm{Y}})$ et l'ensemble des monomorphismes $\mathbb{K}(y) \to \mathrm{K}$ ($y \in \mathrm{Y}$).

Corollaire (2.4.7). — Pour tout  $y \in Y$ , tout morphisme canonique  $\operatorname{Spec}(\mathcal{O}_{y}/\mathfrak{a}_{y}) \to Y$  est un monomorphisme d'espaces annelés.

On l'a déjà vu lorsque $a_y = 0$ (2.4.2), et il suffit d'appliquer (1.7.5).

Remarque (2.4.8). — Soient X un schéma local, $a$ son unique point fermé. Comme tout ouvert affine contenant $a$ est nécessairement X tout entier, tout $\mathcal{O}_{\mathrm{X}}$-Module $inversible$ (0, 5.4.1) est nécessairement $isomorphe$ à $\mathcal{O}_{\mathrm{X}}$ (ou, comme on dit encore, est trivial). Cette propriété n'a pas lieu en général pour un schéma affine quelconque $\operatorname{Spec}(\mathrm{A})$; on verra au chap. V que si A est un anneau normal, elle est vraie lorsque A est $factoriel$.

## 2.5. Préschémas au-dessus d'un préschéma.

Définition (2.5.1). — Étant donné un préschéma S, on dit que la donnée d'un préschéma X et d'un morphisme de préschémas $\varphi: X \to S$ définit un préschéma X au-dessus du préschéma S, ou un S-préschéma ; on dit que S est le préschéma de base du S-préschéma X. Le morphisme $\varphi$ est appelé le morphisme structural du S-préschéma X. Lorsque S est un schéma affine d'anneau A, on dit aussi que X muni de $\varphi$ est un préschéma au-dessus de l'anneau A (ou un A-préschéma).

Il résulte de (2.2.4) que la donnée d'un préschéma au-dessus d'un anneau A équivaut à la donnée d'un préschéma  $(\mathbf{X}, \mathcal{O}_{\mathbf{X}})$  dont le faisceau structural  $O_{X}$  est un faisceau de A-algèbres. Un préschéma quelconque peut donc toujours être considéré de façon unique comme un Z-préschéma.

Si $\varphi: X \to S$ est le morphisme structural d'un S-préschéma $X$, on dit qu'un point $x \in X$ est au-dessus d'un point $s \in S$ si $\varphi(x) = s$. On dit que $X$ domine $S$ si $\varphi$ est un morphisme dominant (2.2.6).

(2.5.2) Soient X, Y deux S-préschémas ; on dit qu'un morphisme de préschémas $u: \mathrm{X} \to \mathrm{Y}$ est un morphisme de préschémas au-dessus de S (ou un S-morphisme) si le diagramme

![](images/page_101_image_9.jpg)

(où les flèches obliques sont les morphismes structuraux) est commutatif : cela entraîne que pour tout $s\in S$ et tout $x\in X$ au-dessus de $s$, $u(x)$ doit aussi être au-dessus de $s$.

Cette définition montre aussitôt que le composé de deux S-morphismes est un S-morphisme ; les S-préschémas forment donc une catégorie.

On notera $\mathrm{Hom}_{\mathrm{S}}(\mathrm{X},\mathrm{Y})$ l'ensemble des S-morphismes d'un S-préschéma X dans un S-préschéma Y ; le morphisme identique d'un S-préschéma X sera désigné par $\mathbf{I}_{\mathbf{X}}$. Lorsque S est un schéma affine d'anneau A, on dira aussi A-morphisme au lieu de S-morphisme.

(2.5.3) Si X est un S-préschéma, $v: \mathrm{X}' \to \mathrm{X}$ un morphisme de préschémas, le morphisme composé $\mathrm{X}' \xrightarrow{v} \mathrm{X} \to \mathrm{S}$ définit $\mathrm{X}'$ comme S-préschéma; en particulier, tout préschéma induit sur un ouvert U de X peut être considéré comme un S-préschéma au moyen de l'injection canonique.

Si $u: \mathrm{X} \to \mathrm{Y}$ est un S-morphisme de S-préschémas, la restriction de $u$ à tout préschéma induit sur un ouvert U de X est donc un S-morphisme $\mathrm{U} \to \mathrm{Y}$. Inversement, soit $(\mathrm{U}_{\alpha})$ un recouvrement ouvert de X et pour chaque $\alpha$, soit $u_{\alpha}: \mathrm{U}_{\alpha} \to \mathrm{Y}$ un S-morphisme; si, pour tout couple d'indices $(\alpha, \beta)$, les restrictions de $u_{\alpha}$ et de $u_{\beta}$ à $\mathrm{U}_{\alpha} \cap \mathrm{U}_{\beta}$ coincident, il existe un S-morphisme $\mathrm{X} \to \mathrm{Y}$ et un seul dont la restriction à chaque $\mathrm{U}_{\alpha}$ soit $u_{\alpha}$.

Si $u: \mathrm{X} \to \mathrm{Y}$ est un S-morphisme tel que $u(\mathrm{X}) \subset \mathrm{V}$, où $\mathrm{V}$ est une partie ouverte de $\mathrm{Y}$, alors $u$, considéré comme morphisme de $\mathrm{X}$ dans $\mathrm{V}$, est encore un S-morphisme.

(2.5.4) Soit $S' \to S$ un morphisme de préschémas; pour tout $S'$-préschéma, le morphisme composé $X \to S' \to S$ définit $X$ comme $S$-préschéma. Inversement, supposons que $S'$ soit le préschéma induit sur un ouvert de $S$; soit $X$ un $S$-préschéma et supposons que le morphisme structural $f: X \to S$ soit tel que l'on ait $f(X) \subset S'$; alors on peut considérer $X$ comme un $S'$-préschéma. Dans ce dernier cas, si $Y$ est un $S$-préschéma dont le morphisme structural applique aussi l'espace sous-jacent dans $S'$, tout $S$-morphisme de $X$ dans $Y$ est aussi un $S'$-morphisme.

(2.5.5) Si X est un S-morphisme, $\varphi: X \to S$ le morphisme structural, on appelle S-section de X un S-morphisme de S dans X, c'est-à-dire un morphisme de préschémas $\psi: S \to X$ tel que $\varphi \circ \psi$ soit l'identité de S. On désigne par $\Gamma(X/S)$ l'ensemble des S-sections de X.

## § 3. PRODUIT DE PRÉSCHÉMAS

## 3.1. Somme de préschémas.

Soit  $(\mathbf{X}_{\alpha})$  une famille quelconque de préschémas; soit X un espace topologique somme des espaces sous-jacents  $X_{\alpha}$ ; X est alors réunion de sous-espaces ouverts deux à deux disjoints  $X_{\alpha}^{\prime}$ , et pour chaque  $\alpha$  il y a un homéomorphisme  $\varphi_{\alpha}$  de  $X_{\alpha}$  sur  $X_{\alpha}^{\prime}$ . Si on munit chacun des  $X_{\alpha}^{\prime}$  du faisceau  $(\varphi_{\alpha})_{*}(\mathcal{O}_{X_{\alpha}})$ , il est clair que X devient un préschéma, qu'on appelle somme de la famille de préschémas  $(\mathbf{X}_{\alpha})$  et que l'on note  $\Pi\mathbf{X}_{\alpha}$ . Si Y est un préschéma, l'application  $f\to(f\circ\varphi_{\alpha})$  est une bijection de l'ensemble Hom(X, Y) sur l'ensemble produit  $\Pi\mathrm{Hom}(X_{\alpha}, Y)$ . En particulier, si les  $X_{\alpha}$  sont des S-préschémas, de morphismes structuraux  $\psi_{\alpha}$ , X est un S-préschéma pour l'unique morphisme  $\psi:X\to S$  tel que  $\psi\circ\varphi_{\alpha}=\psi_{\alpha}$  pour tout  $\alpha$ . La somme de deux préschémas X, Y se note  $X_{II}Y$ . Il est immédiat que si  $X=\operatorname{Spec}(A)$ ,  $Y=\operatorname{Spec}(B)$ ,  $X_{II}Y$  s'identifie canoniquement à  $\operatorname{Spec}(A\times B)$ .

## 3.2. Produit de préschémas.

Définition (3.2.1). — Étant donnés deux S-préschémas X, Y, on dit qu'un triplet  $(Z, p_{1}, p_{2})$  formé d'un S-préschéma Z et de deux S-morphismes  $p_{1}: Z \to X$ ,  $p_{2}: Z \to Y$ , est un produit des

S-préschémas X et Y, si, pour tout S-préschéma T, l'application  $f \rightarrow (p_{1} \circ f, p_{2} \circ f)$  est une bijection de l'ensemble des S-morphismes de T dans Z, sur l'ensemble des couples formés d'un S-morphisme  $T \rightarrow X$  et d'un S-morphisme  $T \rightarrow Y$  (autrement dit, une bijection

$$
\operatorname{Hom} _ {\mathrm{s}} (\mathrm{T}, \mathrm{Z}) \xrightarrow {\sim} \operatorname{Hom} _ {\mathrm{s}} (\mathrm{T}, \mathrm{X}) \times \operatorname{Hom} _ {\mathrm{s}} (\mathrm{T}, \mathrm{Y}))
$$

Il s'agit donc là de la notion générale de produit de deux objets d'une catégorie, appliquée à la catégorie des S-préschémas (T, I, i.1) ; en particulier, un produit de deux S-préschémas est unique à un S-isomorphisme unique près. En raison de cette unicité, on désigne le plus souvent un produit de deux S-préschémas X, Y par la notation  $X \times_{s} Y$  (ou simplement  $X \times Y$  si aucune confusion n'est à craindre), les morphismes  $p_{1}, p_{2}$  (appelés les projections canoniques de  $X \times_{s} Y$  dans X et Y respectivement) étant supprimés de la notation. Si  $g : T \to X$ ,  $h : T \to Y$  sont deux S-morphismes, on désignera par  $(g, h)_{s}$ , ou simplement  $(g, h)$  le S-morphisme  $f : T \to X \times_{s} Y$  tel que  $p_{1} \circ f = g$ ,  $p_{2} \circ f = h$ . Si  $X', Y'$  sont deux S-préschémas,  $p_{1}', p_{2}'$  les projections canoniques de  $X' \times_{s} Y'$  (supposé exister),  $u : X' \to X$ ,  $v : Y' \to Y$  deux S-morphismes, on écrira  $u \times_{s} v$  (ou simplement  $u \times v$ ) le S-morphisme  $(u \circ p_{1}', v \circ p_{2}')_{s}$  de  $X' \times_{s} Y'$  dans  $X \times_{s} Y$ .

Lorsque S est un schéma affine d'anneau A, on remplace souvent S par A dans les notations précédentes.

Proposition (3.2.2). — Soient X, Y, S trois schémas affines, B, C, A leurs anneaux respectifs. Soient  $Z=\operatorname{Spec}(B\otimes_{A}C)$ ,  $p_{1}$ ,  $p_{2}$  les S-morphismes correspondant (2.2.4) aux A-homomorphismes canoniques  $u:b\to b\otimes I$  et  $v:c\to I\otimes c$  de B et C dans  $B\otimes_{A}C$ ; alors  $(Z,p_{1},p_{2})$  est un produit de X et Y.

En vertu de (2.2.4), tout revient à vérifier que si, à tout A-homomorphisme $f: \mathbf{B} \otimes_{\mathbf{A}} \mathbf{C} \to \mathbf{L}$ (où L est une A-algèbre), on associe le couple $(f \circ u, f \circ v)$, on définit une bijection $\operatorname{Hom}_{\mathbf{A}}(\mathbf{B} \otimes_{\mathbf{A}} \mathbf{C}, \mathbf{L}) \simeq \operatorname{Hom}_{\mathbf{A}}(\mathbf{B}, \mathbf{L}) \times \operatorname{Hom}_{\mathbf{A}}(\mathbf{C}, \mathbf{L})$ (1), ce qui résulte immédiatement des définitions et de la relation $b \otimes c = (b \otimes 1)(1 \otimes c)$.

Corollaire (3.2.3). — Soient T un schéma affine d'anneau D, $\alpha=(^{a}\rho,\widetilde{\rho})$ (resp. $\beta=(^{a}\sigma,\widetilde{\sigma})$) un S-morphisme T→X (resp. T→Y), où $\rho$ (resp. $\sigma$) est un A-homomorphisme de B (resp. C) dans D; alors $(\alpha,\beta)_{S}=(^{a}\tau,\widetilde{\tau})$, où $\tau$ est l'homomorphisme B⊗$_{A}C\to D$ tel que $\tau(b\otimes c)=\rho(b)\sigma(c)$.

Proposition (3.2.4). — Soient $f: S' \to S$ un monomorphisme de préschémas (T, I, I.I), X, Y deux S'-préschémas, qui sont considérés aussi comme S-préschémas au moyen de f. Tout produit des S-préschémas X, Y est alors un produit des S'-préschémas X, Y et réciproquement.

Soient $\varphi: X \to S'$, $\psi: Y \to S'$ les morphismes structuraux. Si T est un S-préschéma, $u: T \to X$, $v: T \to Y$ deux S-morphismes, on a par définition $f \circ \varphi \circ u = f \circ \psi \circ v = \theta$, morphisme structural de T; l'hypothèse sur $f$ entraîne $\varphi \circ u = \psi \circ v = \theta'$, et on voit qu'on peut considérer T comme S'-préschéma de morphisme structural $\theta'$, $u$ et $v$ comme des S'-morphismes. La conclusion de la proposition en résulte immédiatement, compte tenu de (3.2.1).

Corollaire (3.2.5). — Soient X, Y deux S-préschémas, $\varphi: X \to S$, $\psi: Y \to S$ leurs morphismes structuraux, $S'$ une partie ouverte de S telle que $\varphi(X) \subset S'$, $\psi(Y) \subset S'$. Tout produit des S-préschémas X, Y est aussi un produit des $S'$-préschémas X, Y, et réciproquement.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) La notation $\mathrm{Hom}_{\mathbf{A}}$ désigne ici l'ensemble des homomorphismes de A-algèbres.</span></small>

Il suffit d'appliquer (3.2.4) à l'injection canonique S'→S.

Théorème (3.2.6). — Étant donnés deux S-préschémas X, Y, il existe un produit  $X \times_{s} Y$ . Nous procéderons en plusieurs étapes.

Lemme (3.2.6.1). — Soient (Z, p, q) un produit de X et Y, U, V des parties ouvertes de X, Y respectivement. Si on pose  $W = p^{-1}(U) \cap q^{-1}(V)$ , le triplet formé de W et des restrictions de p et q à W (considérées comme des morphismes  $W \to U$ ,  $W \to V$  respectivement) est un produit de U et V.

En effet, si T est un S-préschéma, on peut identifier les S-morphismes T→W et les S-morphismes T→Z appliquant T dans W. Si alors g : T→U, h : T→V sont deux S-morphismes quelconques, on peut les considérer comme des S-morphismes de T dans X et Y respectivement, et par hypothèse il y a donc un S-morphisme et un seul f : T→Z tel que g = p∘f, h = q∘f. Comme  $p(f(T)) \subset U$ ,  $q(f(T)) \subset V$ , on a

$$
f (\mathbf {T}) \subset p ^ {- 1} (\mathbf {U}) \cap q ^ {- 1} (\mathbf {V}) = \mathbf {W}
$$

d'où notre assertion.

Lemme (3.2.6.2). — Soient Z un S-préschéma, $p: \mathrm{Z} \to \mathrm{X}$, $q: \mathrm{Z} \to \mathrm{Y}$ deux S-morphismes, $(\mathrm{U}_{\alpha})$ un recouvrement ouvert de X, $(\mathrm{V}_{\lambda})$ un recouvrement ouvert de Y. On suppose que pour tout couple $(\alpha, \lambda)$, le S-préschéma $\mathrm{W}_{\alpha\lambda} = p^{-1}(\mathrm{U}_{\alpha}) \cap q^{-1}(\mathrm{V}_{\lambda})$ et les restrictions de $p$ et $q$ à $\mathrm{W}_{\alpha\lambda}$ constituent un produit de $\mathrm{U}_{\alpha}$ et de $\mathrm{V}_{\lambda}$. Alors $(\mathrm{Z}, p, q)$ est un produit de X et Y.

Montrons d'abord que, si $f_1$, $f_2$ sont deux S-morphismes $T \to Z$, les relations $p \circ f_1 = p \circ f_2$ et $q \circ f_1 = q \circ f_2$ entraînent $f_1 = f_2$. En effet, $Z$ est réunion des $W_{\alpha\lambda}$, donc les $f_1^{-1}(W_{\alpha\lambda})$ forment un recouvrement ouvert de $T$, et il en est de même des $f_2^{-1}(W_{\alpha\lambda})$. En outre, on a

$$
f _ {1} ^ {- 1} \left(\mathrm{W} _ {\alpha \lambda}\right) = f _ {1} ^ {- 1} \left(p ^ {- 1} \left(\mathrm{U} _ {\alpha}\right)\right) \cap f _ {1} ^ {- 1} \left(q ^ {- 1} \left(\mathrm{V} _ {\lambda}\right)\right) = f _ {2} ^ {- 1} \left(p ^ {- 1} \left(\mathrm{U} _ {\alpha}\right)\right) \cap f _ {2} ^ {- 1} \left(q ^ {- 1} \left(\mathrm{V} _ {\lambda}\right)\right) = f _ {2} ^ {- 1} \left(\mathrm{W} _ {\alpha \lambda}\right)
$$

par hypothèse, et tout revient à voir que les restrictions de $f_{1}$ et $f_{2}$ à $f_{1}^{-1}(W_{\alpha\lambda})=f_{2}^{-1}(W_{\alpha\lambda})$ sont identiques pour tout couple d'indices. Mais comme ces restrictions peuvent être considérées comme des S-morphismes de $f_{1}^{-1}(W_{\alpha\lambda})$ dans $W_{\alpha\lambda}$, notre assertion résulte des hypothèses et de la déf. (3.2.1).

Supposons maintenant donnés deux S-morphismes $g: \mathrm{T} \to \mathrm{X}, h: \mathrm{T} \to \mathrm{Y}$. Posons $\mathrm{T}_{\alpha \lambda} = g^{-1}(\mathrm{U}_{\alpha}) \cap h^{-1}(\mathrm{V}_{\lambda})$; les $\mathrm{T}_{\alpha \lambda}$ forment un recouvrement ouvert de T. Par hypothèse, il existe un S-morphisme $f_{\alpha \lambda}$ tel que $p \circ f_{\alpha \lambda}$ et $q \circ f_{\alpha \lambda}$ soient les restrictions respectives de $g$ et $h$ à $\mathrm{T}_{\alpha \lambda}$. En outre, montrons que les restrictions de $f_{\alpha \lambda}$ et de $f_{\beta \mu}$ à $\mathrm{T}_{\alpha \lambda} \cap \mathrm{T}_{\beta \mu}$ coïncident, ce qui achèvera de prouver (3.2.6.2). Or, les images de $\mathrm{T}_{\alpha \lambda} \cap \mathrm{T}_{\beta \mu}$ par $f_{\alpha \lambda}$ et par $f_{\beta \mu}$ sont contenues dans $\mathrm{W}_{\alpha \lambda} \cap \mathrm{W}_{\beta \mu}$ par définition. Comme

$$
\mathrm{W} _ {\alpha \lambda} \cap \mathrm{W} _ {\beta \mu} = p ^ {- 1} (\mathrm{U} _ {\alpha} \cap \mathrm{U} _ {\beta}) \cap q ^ {- 1} (\mathrm{V} _ {\lambda} \cap \mathrm{V} _ {\mu})
$$

il résulte de (3.2.6.1) que  $W_{\alpha\lambda}\cap W_{\beta\mu}$  et les restrictions à ce préschéma de p et q constituent un produit de  $U_{\alpha}\cap U_{\beta}$  et de  $V_{\lambda}\cap V_{\mu}$ . Comme  $p\circ f_{\alpha\lambda}$  et  $p\circ f_{\beta\mu}$  coïncident dans  $T_{\alpha\lambda}\cap T_{\beta\mu}$  et qu'il en est de même de  $q\circ f_{\alpha\lambda}$  et  $q\circ f_{\beta\mu}$ , on voit que  $f_{\alpha\lambda}$  et  $f_{\beta\mu}$  coïncident dans  $T_{\alpha\lambda}\cap T_{\beta\mu}$ , c.q.f.d.

(3.2.6.3) Soient  $(\mathbf{U}_{\alpha})$  un recouvrement ouvert de X,  $(\mathbf{V}_{\lambda})$  un recouvrement ouvert de Y, et supposons que pour tout couple  $(\alpha, \lambda)$ , il existe un produit de  $U_{\alpha}$  et de  $V_{\lambda}$ ; alors il existe un produit de X et Y.

Appliquant le lemme (3.2.6.1) aux ouverts  $U_{\alpha} \cap U_{\beta}$  et  $V_{\lambda} \cap V_{\mu}$ , on voit qu'il existe un produit des S-préschémas induits respectivement par X et Y sur ces ouverts; en outre, l'unicité du produit montre que, si on pose  $i = (\alpha, \lambda)$ ,  $j = (\beta, \mu)$ , il y a un isomorphisme canonique  $h_{ij}$  (resp.  $h_{ji}$ ) de ce produit sur un S-préschéma  $W_{ij}$  (resp.  $W_{ji}$ ) induit par  $U_{\alpha} \times _{S} V_{\lambda}$  (resp.  $U_{\beta} \times _{S} V_{\mu}$ ) sur un ouvert;  $f_{ij} = h_{ij} \circ h_{ji}^{-1}$  est donc un isomorphisme de  $W_{ji}$  sur  $W_{ij}$ . En outre, pour un troisième couple  $k = (\gamma, \nu)$ , on a  $f_{ik} = f_{ij} \circ f_{jk}$  dans  $W_{ki} \cap W_{kj}$ , comme il résulte de l'application de (3.2.6.1) aux ouverts  $U_{\alpha} \cap U_{\beta} \cap U_{\gamma}$  et  $V_{\lambda} \cap V_{\mu} \cap V_{\nu}$  dans  $U_{\beta}$  et  $V_{\mu}$  respectivement. Il y a par suite un préschéma Z, un recouvrement ouvert ( $Z_i$ ) de l'espace sous-jacent à Z et pour chaque i un isomorphisme  $g_i$  du préschéma induit  $Z_i$  sur le préschéma  $U_{\alpha} \times _{S} V_{\lambda}$ , de sorte que pour tout couple  $(i, j)$ , on ait  $f_{ij} = g_i \circ g_j^{-1}$  (2.3.1); de plus, on a  $g_i(Z_i \cap Z_j) = W_{ij}$ . Si  $p_i$ ,  $q_i$ ,  $\theta_i$  sont les projections et le morphisme structural du S-préschéma  $U_{\alpha} \times _{S} V_{\lambda}$ , on constate aussitôt que  $p_i \circ g_i = p_j \circ g_j$  dans  $Z_i \cap Z_j$ , et de même pour les deux autres morphismes. On peut donc définir des morphismes de préschémas  $p : Z \to X$  (resp.  $q : Z \to Y$ ,  $\theta : Z \to S$ ) par la condition que p (resp. q,  $\theta$ ) coïncide avec  $p_i \circ g_i$  (resp.  $q_i \circ g_i$ ,  $\theta_i \circ g_i$ ) dans chacun des  $Z_i$ ; Z, muni de  $\theta$ , est alors un S-préschéma. Montrons maintenant que  $Z_i' = p^{-1}(U_\alpha) \cap q^{-1}(V_\lambda)$  est égal à  $Z_i$ . Pour tout indice j = ( $\beta, \mu$ ), on a  $Z_j \cap Z_i' = g_j^{-1}(p_j^{-1}(U_\alpha) \cap q_j^{-1}(V_\lambda))$ . Or,

$$
p _ {j} ^ {- 1} \left(\mathrm{U} _ {\alpha}\right) \cap q _ {j} ^ {- 1} \left(\mathrm{V} _ {\lambda}\right) = p _ {j} ^ {- 1} \left(\mathrm{U} _ {\alpha} \cap \mathrm{U} _ {\beta}\right) \cap q _ {j} ^ {- 1} \left(\mathrm{V} _ {\lambda} \cap \mathrm{V} _ {\mu}\right);
$$

en vertu de (3.2.6.1), les restrictions de $p_j$ et $q_j$ à $p_j^{-1}(\mathrm{U}_\alpha) \cap q_j^{-1}(\mathrm{V}_\lambda)$ définissent sur ce S-préschéma une structure de produit de $\mathrm{U}_\alpha \cap \mathrm{U}_\beta$ et $\mathrm{V}_\lambda \cap \mathrm{V}_\mu$; mais l'unicité du produit entraîne alors que $p_j^{-1}(\mathrm{U}_\alpha) \cap q_j^{-1}(\mathrm{V}_\lambda) = \mathrm{W}_{ji}$. On a par suite $Z_j \cap Z_i' = Z_j \cap Z_i$ pour tout $j$, d'où $Z_i' = Z_i$. On déduit alors de (3.2.6.2) que $(\mathbf{Z}, p, q)$ est un produit de $\mathbf{X}$ et $\mathbf{Y}$.

(3.2.6.4) Soient $\varphi : \mathrm{X} \to \mathrm{S}$, $\psi : \mathrm{Y} \to \mathrm{S}$ les morphismes structuraux de $\mathrm{X}$ et $\mathrm{Y}$, $(\mathrm{S}_i)$ un recouvrement ouvert de $\mathrm{S}$, et posons $\mathrm{X}_i = \varphi^{-1}(\mathrm{S}_i)$, $\mathrm{Y}_i = \psi^{-1}(\mathrm{S}_i)$. Si chacun des produits $\mathrm{X}_i \times {}_{\mathrm{s}} \mathrm{Y}_i$ existe, alors $\mathrm{X} \times {}_{\mathrm{s}} \mathrm{Y}$ existe.

D'après (3.2.6.3), tout revient à prouver que les produits  $X_{i} \times_{s} Y_{j}$  existent quels que soient i et j. Posons  $X_{ij} = X_{i} \cap X_{j} = \varphi^{-1}(S_{i} \cap S_{j})$ ,  $Y_{ij} = Y_{i} \cap Y_{j} = \psi^{-1}(S_{i} \cap S_{j})$ ; en vertu de (3.2.6.1), le produit  $Z_{ij} = X_{ij} \times_{s} Y_{ij}$  existe. Notons maintenant que si T est un S-préschéma et si  $g : T \to X_{i}$ ,  $h : T \to Y_{j}$  sont des S-morphismes, on a nécessairement  $\varphi(g(T)) = \psi(h(T)) \subset S_{i} \cap S_{j}$  d'après la définition d'un S-morphisme, donc  $g(T) \subset X_{ij}$  et  $h(T) \subset Y_{ij}$ ; il est alors immédiat que  $Z_{ij}$  est un produit de  $X_{i}$  et  $Y_{j}$ .

(3.2.6.5) Nous pouvons maintenant achever de démontrer le th. (3.2.6). Si S est un schéma affine, il y a des recouvrements  $(\mathrm{U}_{\alpha})$ ,  $(\mathrm{V}_{\lambda})$  de X et Y respectivement, formés d'ouverts affines; comme  $U_{\alpha} \times_{s} V_{\lambda}$  existe en vertu de (3.2.2), il en est de même de  $X \times_{s} Y$  par (3.2.6.3). Si S est un préschéma quelconque, il y a un recouvrement  $(\mathrm{S}_{i})$  de S formé d'ouverts affines. Si  $\varphi : X \to S$ ,  $\psi : Y \to S$  sont les morphismes structuraux, et si on pose  $\mathbf{X}_{i} = \varphi^{-1}(\mathbf{S}_{i})$ ,  $\mathbf{Y}_{i} = \psi^{-1}(\mathbf{S}_{i})$ , les produits  $X_{i} \times_{s_{i}} Y_{i}$  existent d'après ce qui

précède ; mais alors les produits  $X_{i} \times_{s} Y_{i}$  existent aussi (3.2.5), donc il en est de même de  $X \times_{s} Y$  par (3.2.6.4).

Corollaire (3.2.7). — Soient $Z = X \times_{S} Y$ le produit de deux S-préschémas, $p, q$ les projections de $Z$ dans $X$ et $Y$, $\varphi$ (resp. $\psi$) le morphisme structural de $X$ (resp. $Y$). Soient $S'$ une partie ouverte de $S$, $U$ (resp. $V$) une partie ouverte de $X$ (resp. $Y$) contenue dans $\varphi^{-1}(S')$ (resp. $\psi^{-1}(S')$). Alors le produit $U \times_{S'} V$ s'identifie canoniquement au préschéma induit par $Z$ sur $p^{-1}(U) \cap q^{-1}(V)$ (considéré comme $S'$-préschéma). En outre, si $f: T \to X$, $g: T \to Y$ sont des S-morphismes tels que $f(T) \subset U$, $g(T) \subset V$, le $S'$-morphisme $(f, g)_{S'}$ s'identifie à la restriction de $(f, g)_{S'}$ à $p^{-1}(U) \cap q^{-1}(V)$.

Cela résulte de (3.2.5) et (3.2.6.1).

(3.2.8) Soient  $(\mathbf{X}_{\alpha})$ ,  $(\mathbf{Y}_{\lambda})$  deux familles de S-préschémas, X (resp. Y) la somme de la famille  $(\mathbf{X}_{\alpha})$  (resp.  $(\mathbf{Y}_{\lambda})$ ) (3.1). Alors  $X \times_{s} Y$  s'identifie à la somme de la famille  $(\mathbf{X}_{\alpha} \times_{s} \mathbf{Y}_{\lambda})$ ; cela résulte aussitôt de (3.2.6.3).

## 3.3. Propriétés formelles du produit; changement de préschéma de base.

(3.3.1) Le lecteur remarquera que toutes les propriétés énoncées dans cette section, sauf (3.3.13) et (3.3.15), sont valables sans modification dans toute catégorie, chaque fois que les produits qui interviennent dans les énoncés existent (car il est clair que les notions de S-objet et de S-morphisme peuvent se définir exactement comme dans (2.5) pour tout objet S de la catégorie).

(3.3.2) En premier lieu,  $X \times_{s} Y$  est un bifoncteur covariant en X et Y dans la catégorie des S-préschémas : il suffit en effet de remarquer que le diagramme

$$
\begin{array}{c} \mathrm{X} \times \mathrm{Y} \xrightarrow {f \times 1} \mathrm{X} ^ {\prime} \times \mathrm{Y} \xrightarrow {f ^ {\prime} \times 1} \mathrm{X} ^ {\prime \prime} \times \mathrm{Y} \\ \downarrow \qquad \qquad \qquad \qquad \qquad \downarrow \qquad \qquad \qquad \qquad \downarrow \\ \mathrm{X} \xrightarrow [ f ]{} \mathrm{X} ^ {\prime} \xrightarrow [ f ^ {\prime} ]{} \mathrm{X} ^ {\prime \prime} \end{array}
$$

est commutatif.

Proposition (3.3.3). — Pour tout S-préschéma X, la première (resp. seconde) projection de  $X \times_{s} S$  (resp.  $S \times_{s} X$ ) est un isomorphisme fonctoriel de  $X \times_{s} S$  (resp.  $S \times_{s} X$ ) sur X, dont l'isomorphisme réciproque est  $(\mathrm{I}_{\mathrm{X}}, \varphi)_{\mathrm{S}}$  (resp.  $(\varphi, \mathrm{I}_{\mathrm{X}})_{\mathrm{S}}$ ), en désignant par  $\varphi$  le morphisme structural  $X \to S$ ; on peut donc écrire, à un isomorphisme canonique près

$$
\mathbf {X} \times_ {\mathrm{s}} \mathbf {S} = \mathbf {S} \times_ {\mathrm{s}} \mathbf {X} = \mathbf {X}.
$$

Il suffit de prouver que le triplet (X,  $I_{X}$ ,  $\varphi$ ) est un produit de X et S. Or, si T est un S-préschéma, le seul S-morphisme de T dans S est nécessairement le morphisme structural  $\psi: T \to S$ . Si f est un S-morphisme de T dans X, on a nécessairement  $\psi = \varphi \circ f$ , d'où notre assertion.

Corollaire (3.3.4). — Soient X, Y deux S-préschémas, $\varphi: X \to S$, $\psi: Y \to S$ leurs morphismes structuraux. Si on identifie canoniquement X à $X \times_{S} S$ et Y à $S \times_{S} Y$, les projections $X \times_{S} Y \to X$ et $X \times_{S} Y \to Y$ s'identifient respectivement à $I_X \times \psi$ et $\varphi \times I_Y$.

La vérification est immédiate et laissée au lecteur.

(3.3.5) On peut définir de la même manière que dans (3.2) le produit d'un

nombre fini quelconque n de S-préschémas, l'existence de ces produits résulte de (3.2.6) par récurrence sur n, en remarquant que  $(\mathbf{X}_{1} \times_{\mathrm{S}} \mathbf{X}_{2} \times \ldots \times_{\mathrm{S}} \mathbf{X}_{n-1}) \times_{\mathrm{S}} \mathbf{X}_{n}$  satisfait à la définition du produit. L'unicité du produit entraîne, comme dans toute catégorie, ses propriétés de commutativité et d'associativité. Si, par exemple,  $p_{1}, p_{2}, p_{3}$  désignent les projections de  $X_{1} \times X_{2} \times X_{3}$ , et si on identifie ce préschéma à  $(\mathbf{X}_{1} \times \mathbf{X}_{2}) \times \mathbf{X}_{3}$ , la projection dans  $X_{1} \times X_{2}$  est identifiée à  $(p_{1}, p_{2})_{\mathrm{S}}$ .

(3.3.6) Soient S, S' deux préschémas, $\varphi: S' \to S$ un morphisme, qui fait de S' un S-préschéma. Pour tout S-préschéma X, considérons le produit $X \times_{S} S'$, et soient $p$ et $\pi'$ ses projections dans X et S' respectivement. Muni de $\pi'$, ce produit est un S'-pré-schéma; quand on le considère comme tel, on le désigne par $X_{(S')}$ ou $X_{(\varphi)}$, et on dit que c'est le préschéma obtenu par extension du préschéma de base de S à S', au moyen du morphisme $\varphi$, ou l'image réciproque de X par $\varphi$. On notera que si $\pi$ est le morphisme structural de X, $\theta$ le morphisme structural de $X \times_{S} S'$, considéré comme S-préschéma, le diagramme

![](images/page_107_image_2.jpg)

est commutatif.

(3.3.7) Avec les notations de (3.3.6), pour tout S-morphisme $f: \mathbf{X} \to \mathbf{Y}$, on note encore $f_{(\mathrm{S}^{\prime})}$ le S'-morphisme $f \times_{\mathrm{SI}}: \mathbf{X}_{(\mathrm{S}^{\prime})} \to \mathbf{Y}_{(\mathrm{S})}$, et on dit que $f_{(\mathrm{S}^{\prime})}$ est l'image réciproque du morphisme $f$ par $\varphi$. $\mathbf{X}_{(\mathrm{S}^{\prime})}$ est donc un foncteur covariant en $\mathbf{X}$, de la catégorie des S-préschémas dans celle des S'-préschémas.

(3.3.8) Le préschéma  $X_{(S')}$  peut encore être considéré comme solution d'un problème d'application universelle : tout S'-préschéma T est aussi un S-préschéma au moyen de  $\varphi$ ; tout S-morphisme  $g: T \to X$  s'écrit alors d'une seule manière  $g = p \circ f$ , où f est un S'-morphisme  $T \to X_{(S')}$ , comme il résulte de la définition du produit appliquée aux S-morphismes f et  $\psi: T \to S'$  (morphisme structural de T).

Proposition (3.3.9) (« transitivité de l'extension des préschémas de base »). — Soient S'' un préschéma, $\varphi': S'' \to S'$ un morphisme. Pour tout S-préschéma X, il existe un isomorphisme canonique fonctoriel du S''-préschéma $(\mathbf{X}_{(\varphi)})_{(\varphi')}$ sur le S''-préschéma $\mathbf{X}_{(\varphi \circ \varphi')}$.

En effet, soient T un S''-préschéma, $\psi$ son morphisme structural, $g$ un S-morphisme de T dans X (T étant considéré comme S-préschéma de morphisme structural $\varphi\circ\varphi'\circ\psi$). Comme T est aussi un S'-préschéma de morphisme structural $\varphi'\circ\psi$, on peut écrire $g=p\circ g'$, où $g'$ est un S'-morphisme T$\rightarrow$X$_{(\varphi)}$, puis $g'=p'\circ g''$, où $g''$ est un S''-morphisme T$\rightarrow$X$_{(\varphi)}_{(\varphi')} :$

![](images/page_107_image_8.jpg)

D'où la proposition en raison de l'unicité de la solution d'un problème d'application universelle.

Ce résultat s'exprime encore en écrivant l'égalité (à un isomorphisme canonique près)  $(\mathbf{X}_{(\mathrm{S}^{\prime})})_{(\mathrm{S}^{\prime \prime})} = \mathbf{X}_{(\mathrm{S}^{\prime \prime})}$ , si aucune confusion n'est à craindre, ou encore

$$
(\mathbf {X} \times_ {\mathrm{s}} \mathbf {S} ^ {\prime}) \times_ {\mathrm{s} ^ {\prime}} \mathbf {S} ^ {\prime \prime} = \mathbf {X} \times_ {\mathrm{s}} \mathbf {S} ^ {\prime \prime};\tag{3.3.9.1}
$$

le caractère fonctoriel de l'isomorphisme défini dans (3.3.9) s'exprime de même par la formule de transitivité des images réciproques de morphismes

$$
\left(f _ {\left(\mathrm{S} ^ {\prime}\right)}\right) _ {\left(\mathrm{S} ^ {\prime \prime}\right)} = f _ {\left(\mathrm{S} ^ {\prime \prime}\right)}\tag{3.3.9.2}
$$

pour tout S-morphisme $f: \mathbf{X} \to \mathbf{Y}$.

Corollaire (3.3.10). — Si X et Y sont deux S-préschémas, il existe un isomorphisme canonique fonctoriel du S'-préschéma  $\mathbf{X}_{(\mathrm{S}^{\prime})}\times_{\mathrm{S}^{\prime}}\mathbf{Y}_{(\mathrm{S}^{\prime})}$  sur le S'-préschéma  $(\mathbf{X}\times_{\mathrm{S}}\mathbf{Y})_{(\mathrm{S}^{\prime})}$ .

En effet, on a, à des isomorphismes canoniques près

$$
(\mathbf {X} \times_ {\mathrm{s}} \mathbf {S} ^ {\prime}) \times_ {\mathrm{s} ^ {\prime}} (\mathbf {Y} \times_ {\mathrm{s}} \mathbf {S} ^ {\prime}) = \mathbf {X} \times_ {\mathrm{s}} (\mathbf {Y} \times_ {\mathrm{s}} \mathbf {S} ^ {\prime}) = (\mathbf {X} \times_ {\mathrm{s}} \mathbf {Y}) \times_ {\mathrm{s}} \mathbf {S} ^ {\prime}
$$

en vertu de (3.3.9.1) et de l'associativité des produits de S-préschémas.

Le caractère fonctoriel de l'isomorphisme défini dans (3.3.10) s'exprime par la formule

$$
\left(u _ {\left(\mathrm{S} ^ {\prime}\right)}, v _ {\left(\mathrm{S} ^ {\prime}\right)}\right) _ {\mathrm{S} ^ {\prime}} = \left(\left(u, v\right) _ {\mathrm{S}}\right) _ {\left(\mathrm{S} ^ {\prime}\right)}\tag{3.3.10.1}
$$

pour tout couple de S-morphismes $u: \mathrm{T} \to \mathrm{X}, v: \mathrm{T} \to \mathrm{Y}$.

En d'autres termes, le foncteur image réciproque  $X_{(S')}$  commute à la formation des produits; il commute aussi à la formation des sommes (3.2.8).

Corollaire (3.3.11). — Soient Y un S-préschéma, $f: \mathbf{X} \to \mathbf{Y}$ un morphisme qui fait de X un Y-préschéma (et par suite aussi un S-préschéma). Le préschéma $\mathbf{X}_{(\mathrm{S}^{\prime})}$ s'identifie alors au produit $\mathbf{X} \times_{\mathbf{Y}} \mathbf{Y}_{(\mathrm{S}^{\prime})}$, la projection $\mathbf{X} \times_{\mathbf{Y}} \mathbf{Y}_{(\mathrm{S}^{\prime})} \to \mathbf{Y}_{(\mathrm{S}^{\prime})}$ s'identifiant à $f_{(\mathrm{S}^{\prime})}$.

Soit $\psi : Y \to S$ le morphisme structural de $Y$; on a le diagramme commutatif

![](images/page_108_image_16.jpg)

Or  $Y_{(S')}$  s'identifie à  $S'_{(\psi)}$ , et  $X_{(S')}$  à  $S'_{(\psi o f)}$ ; tenant compte de (3.3.9) et de (3.3.4), on en déduit le corollaire.

(3.3.12) Soient $f: \mathbf{X} \to \mathbf{X}'$, $g: \mathbf{Y} \to \mathbf{Y}'$ deux S-morphismes qui sont des monomorphismes de préschémas (T, I, i.i); alors $f \times_{\mathrm{S}} g$ est un monomorphisme. En effet, si $p$ et $q$ sont les projections de $\mathbf{X} \times_{\mathrm{S}} \mathbf{Y}$, $p'$, $q'$ celles de $\mathbf{X}' \times_{\mathrm{S}} \mathbf{Y}'$, $u$, $v$ deux S-morphismes $\mathbf{T} \to \mathbf{X} \times_{\mathrm{S}} \mathbf{Y}$, la relation $(f \times_{\mathrm{S}} g) \circ u = (f \times_{\mathrm{S}} g) \circ v$ entraîne $p' \circ (f \times_{\mathrm{S}} g) \circ u = p' \circ (f \times_{\mathrm{S}} g) \circ v$, autrement dit $f \circ p \circ u = f \circ p \circ v$, et comme $f$ est un monomorphisme, $p \circ u = p \circ v$; utilisant le fait que $g$ est un monomorphisme, on obtient de même $q \circ u = q \circ v$, d'où $u = v$.

Il en résulte que pour toute extension  $S^{\prime}\rightarrow S$  du préschéma de base,

$$
f _ {(\mathbf {S} ^ {\prime})}: \mathbf {X} _ {(\mathbf {S} ^ {\prime})} \to \mathbf {Y} _ {(\mathbf {S} ^ {\prime})}
$$

est un monomorphisme.

(3.3.13) Soient S, S' deux schémas affines d'anneaux respectifs A, A'; un morphisme S'→S correspond donc à un homomorphisme d'anneaux A→A'. Si X est un S-préschéma, on notera alors aussi  $\mathbf{X}_{(\mathbf{A}^{\prime})}$  ou  $X\otimes_{A}A^{\prime}$  le S'-préschéma  $\mathbf{X}_{(\mathbf{S}^{\prime})}$ ; lorsque X est lui-même affine d'anneau B,  $\mathbf{X}_{(\mathbf{A}^{\prime})}$  est affine d'anneau  $\mathbf{B}_{(\mathbf{A}^{\prime})}=\mathbf{B}\otimes_{A}\mathbf{A}^{\prime}$  obtenu par extension à A' de l'anneau des scalaires de la A-algèbre B.

(3.3.14) Avec les notations de (3.3.6), pour tout S-morphisme $f: \mathrm{S}' \to \mathrm{X}, f' = (f, \mathrm{I}_{\mathrm{S}'})_\mathrm{S}$ est un S'-morphisme $\mathrm{S}' \to \mathrm{X}' = \mathrm{X}_{(\mathrm{S}')}$ tel que $p \circ f' = f, \pi' \circ f' = \mathrm{I}_{\mathrm{S}'}$, autrement dit une S'-section de $\mathbf{X}'$; et réciproquement si $f'$ est une telle S'-section, $f = p \circ f'$ est un S-morphisme $\mathrm{S}' \to \mathrm{X}$. On définit donc ainsi une correspondance biunivoque canonique

$$
\operatorname{Hom} _ {\mathrm{s}} \left(\mathrm{S} ^ {\prime}, \mathrm{X}\right) \simeq \operatorname{Hom} _ {\mathrm{s} ^ {\prime}} \left(\mathrm{S} ^ {\prime}, \mathrm{X} ^ {\prime}\right)
$$

On dit que $f'$ est le morphisme graphe de $f$, et on le désigne par $\Gamma_f$.

(3.3.15) Étant donné un préschéma X, qu'on peut toujours considérer comme un Z-préschéma, il résulte en particulier de (3.3.14) que les X-sections de  $X \otimes_{Z} Z[T]$  (où T est une indéterminée) correspondent biunivoquement aux morphismes  $Z[T] \to X$ . Montrons que ces X-sections correspondent biunivoquement aussi aux sections du faisceau structural  $O_{X}$  au-dessus de X. En effet, soit  $(\mathrm{U}_{\alpha})$  un recouvrement de X par des ouverts affines; soit  $u : X \to X \otimes_{Z} Z[T]$  un X-morphisme et soit  $u_{\alpha}$  sa restriction à  $U_{\alpha}$ ; si  $A_{\alpha}$  est l'anneau du schéma affine  $U_{\alpha}, U_{\alpha} \otimes_{Z} Z[T]$  est un schéma affine d'anneau  $A_{\alpha}[T]$  (3.2.2), et  $u_{\alpha}$  correspond canoniquement à un  $A_{\alpha}$ -homomorphisme  $A_{\alpha}[T] \to A_{\alpha}$  (1.7.3). Or, un tel homomorphisme est complètement déterminé par la donnée de l'image de T dans  $A_{\alpha}$ , soit  $s_{\alpha} \in A_{\alpha} = \Gamma(\mathrm{U}_{\alpha}, \mathcal{O}_{\mathrm{X}})$ , et si on écrit que les restrictions de  $u_{\alpha}$  et de  $u_{\beta}$  à un ouvert affine  $V \subset U_{\alpha} \cap U_{\beta}$  coïncident, on voit aussitôt que  $s_{\alpha}$  et  $s_{\beta}$  coïncident dans V; donc la famille  $(s_{\alpha})$  est formée des restrictions aux  $U_{\alpha}$  d'une section s de  $O_{X}$  au-dessus de X; et réciproquement, il est clair qu'une telle section définit une famille  $(u_{\alpha})$  de morphismes qui sont les restrictions aux  $U_{\alpha}$  d'un X-morphisme  $X \to X \otimes_{Z} Z[T]$ . Ce résultat sera généralisé dans II, I.7.12.

## 3.4. Points d'un préschéma à valeurs dans un préschéma ; points géométriques.

(3.4.1) Soit X un préschéma ; pour tout préschéma T, on note encore X(T) l'ensemble Hom(T, X) des morphismes T→X, et les éléments de cet ensemble sont aussi appelés points de X à valeurs dans T. Si on associe à tout morphisme f : T→T' l'application u'→u'∘f de X(T') dans X(T), on voit que, pour X fixé, X(T) est un foncteur contravariant en T, de la catégorie des préschémas dans celle des ensembles. En outre, tout morphisme de préschémas g : X→Y définit un homomorphisme fonctoriel X(T)→Y(T), faisant correspondre gov à v∈X(T).

(3.4.2) Étant donnés trois ensembles P, Q, R et deux applications $\varphi: P \to R$, $\psi: Q \to R$, on appelle produit fibré de P et Q au-dessus de R (relatif à $\varphi$ et $\psi$) la partie de

l'ensemble produit $\mathbf{P} \times \mathbf{Q}$ formée des couples $(p, q)$ tels que $\varphi(p) = \psi(q)$; on le note $\mathbf{P} \times_{\mathbb{R}} \mathbf{Q}$. La définition (3.2.1) du produit de S-préschémas peut encore s'interpréter, avec les notations de (3.4.1), par la formule

$$
(\mathbf {X} \times_ {\mathbf {s}} \mathbf {Y}) (\mathbf {T}) = \mathbf {X} (\mathbf {T}) \times_ {\mathbf {s} (\mathbf {T})} \mathbf {Y} (\mathbf {T})\tag{3.4.2.1}
$$

les applications  $\mathbf{X}(\mathbf{T})\to\mathbf{S}(\mathbf{T})$  et  $\mathbf{Y}(\mathbf{T})\to\mathbf{S}(\mathbf{T})$  correspondant aux morphismes structuraux  $X\to S$  et  $Y\to S$ .

(3.4.3) Si l'on se donne un préschéma S et que l'on ne considère que les S-préschémas et les S-morphismes, on notera encore  $\mathrm{X(T)_{s}}$  l'ensemble  $\mathrm{Hom_{s}(T,X)}$  des S-morphismes  $T\to X$, en se permettant de supprimer l'indice S lorsque aucune confusion n'est possible ; on dit encore que les éléments de  $\mathrm{X(T)_{s}}$  sont les points (ou S-points lorsqu'il y a à craindre des confusions) du S-préschéma X à valeurs dans le S-préschéma T. En particulier, une S-section de X n'est autre qu'un point de X à valeurs dans S. La formule (3.4.2.1) s'écrit alors aussi

$$
(\mathbf {X} \times_ {\mathrm{s}} \mathbf {Y}) (\mathbf {T}) _ {\mathrm{s}} = \mathbf {X} (\mathbf {T}) _ {\mathrm{s}} \times \mathbf {Y} (\mathbf {T}) _ {\mathrm{s}};\tag{3.4.3.1}
$$

plus généralement, si Z est un S-préschéma, X, Y, T des Z-préschémas (donc ipso facto des S-préschémas), on a

$$
(\mathbf {X} \times_ {\mathbf {Z}} \mathbf {Y}) (\mathbf {T}) _ {\mathbf {S}} = \mathbf {X} (\mathbf {T}) _ {\mathbf {S}} \times_ {\mathbf {Z} (\mathbf {T}) _ {\mathbf {S}}} \mathbf {Y} (\mathbf {T}) _ {\mathbf {S}}.\tag{3.4.3.2}
$$

On notera que pour démontrer qu'un triplet (W, r, s) formé d'un S-préschéma W et de deux S-morphismes  $r: W \to X$ ,  $s: W \to Y$  est un produit de X et Y (au-dessus de Z), il suffit par définition de vérifier que pour tout S-préschéma T, le diagramme

$$
\begin{array}{c} \mathbf {W} (\mathbf {T}) _ {\mathrm{s}} \xrightarrow {r ^ {\prime}} \mathbf {X} (\mathbf {T}) _ {\mathrm{s}} \\ \stackrel {{s ^ {\prime}}} {{\downarrow}} \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \varphi^ {\prime} \\ \mathbf {Y} (\mathbf {T}) _ {\mathrm{s}} \xrightarrow [ \psi^ {\prime} ]{} \mathbf {Z} (\mathbf {T}) _ {\mathrm{s}} \end{array}
$$

fait de  $\mathrm{W}(\mathrm{T})_{\mathrm{s}}$  le produit fibré de  $\mathrm{X}(\mathrm{T})_{\mathrm{s}}$  et  $\mathrm{Y}(\mathrm{T})_{\mathrm{s}}$  au-dessus de  $\mathrm{Z}(\mathrm{T})_{\mathrm{s}}$ ,  $r'$  et  $s'$  correspondant à r et s,  $\varphi'$  et  $\psi'$  aux morphismes structuraux  $\varphi: X \to Z$ ,  $\psi: Y \to Z$ .

(3.4.4) Lorsque dans ce qui précède, T (resp. S) est un schéma affine d'anneau B (resp. A), on remplace T (resp. S) par B (resp. A) dans les notations précédentes, et on parle alors de points de X à valeurs dans l'anneau B, ou de points du A-préschéma X à valeurs dans la A-algèbre B pour les éléments de X(B) et de X(B)$_{A}$ respectivement. On notera que X(B) et X(B)$_{A}$ sont maintenant des foncteurs covariants en B. On écrira de même X(T)$_{A}$ pour l'ensemble des points du A-préschéma X à valeurs dans le A-préschéma T.

(3.4.5) Considérons en particulier le cas où T est de la forme $\operatorname{Spec}(A)$, où A est un anneau local; les éléments de X(A) correspondent alors biunivoquement aux homomorphismes locaux $\mathcal{O}_{x} \to A$ pour $x \in X$ (2.4.4); on dit que le point $x$ de l'espace sous-jacent à X est la localité du point de X à valeurs dans A auquel il correspond.

Plus particulièrement, on appellera points géométriques d'un préschéma X les points de X à valeurs dans un corps K : la donnée d'un tel point revient donc à la donnée de sa

localité $x$ dans l'espace sous-jacent à X, et d'une extension K de $k(x)$; K sera appelé le corps des valeurs du point géométrique correspondant, et on dit encore que ce point géométrique est localisé en $x$. On définit ainsi une application $\mathbf{X}(\mathbf{K}) \to \mathbf{X}$, appliquant un point géométrique à valeurs dans K sur sa localité.

Si $S' = \text{Spec}(K)$ est un S-préschéma (autrement dit, si K est considéré comme extension d'un corps résiduel $k(s)$, où $s \in S$) et si X est un S-préschéma, un élément de $X(K)_s$, ou, comme on dit encore, un point géométrique de X au-dessus de $s$ à valeurs dans K, consiste en la donnée d'un $k(s)$-monomorphisme d'un corps résiduel $k(x)$ dans K, où $x$ est un point de X au-dessus de $s$ (donc $k(x)$ une extension de $k(s)$).

Plus particulièrement, si  $\mathrm{S}=\mathrm{Spec}(\mathrm{K})=\{\xi\}$ , les points géométriques de X à valeurs dans K s'identifient aux points  $x\in X$  tels que  $\boldsymbol{k}(x)=\mathbf{K}$ ; on dit encore que ces derniers sont les points du K-préschéma X rationnels sur K; si  $K'$  est une extension de K, les points géométriques de X à valeurs dans  $K'$  correspondent donc biunivoquement aux points de  $X'=X_{(K')}$  rationnels sur  $K'(3.3.14)$ .

Lemme (3.4.6). — Soient  $X_{i}$  ( $i \leqslant i \leqslant n$ ) des S-préschémas, s un point de S,  $x_{i}$  ( $i \leqslant i \leqslant n$ ) un point de  $X_{i}$  au-dessus de s. Il existe alors une extension K de  $\mathbf{k}(s)$  et un point géométrique du produit  $Y = X_{1} \times_{S} X_{2} \times \ldots \times_{S} X_{n}$ , à valeurs dans K, dont les projections soient localisées aux  $x_{i}$ .

En effet, il existe des $\pmb{k}(s)$-monomorphismes $\pmb{k}(x_i) \to \mathbf{K}$ dans une même extension $\mathbf{K}$ de $\pmb{k}(s)$ (Bourbaki, Alg., chap. V, § 4, prop. 2). Les composés $\pmb{k}(s) \to \pmb{k}(x_i) \to \mathbf{K}$ sont tous identiques, donc les morphismes $\operatorname{Spec}(\mathbf{K}) \to \mathbf{X}_i$ correspondant à $\pmb{k}(x_i) \to \mathbf{K}$ sont des S-morphismes, et on en conclut qu'ils définissent un morphisme unique $\operatorname{Spec}(\mathbf{K}) \to \mathbf{Y}$. Si $y$ est le point correspondant de Y, il est clair que sa projection dans chacun des $\mathbf{X}_i$ est $x_i$.

Proposition (3.4.7). — Soient  $X_{i}$  ( $i \leqslant i \leqslant n$ ) des S-préschémas, et pour chaque indice i, soit  $x_{i}$  un point de  $X_{i}$ . Pour qu'il existe un point y de  $Y = X_{1} \times_{S} X_{2} \times \ldots \times_{S} X_{n}$  dont  $x_{i}$  soit la projection d'indice i pour  $i \leqslant i \leqslant n$ , il faut et il suffit que les  $x_{i}$  soient au-dessus d'un même point s de S.

La condition est évidemment nécessaire ; le lemme (3.4.6) prouve qu'elle est suffisante.

En d'autres termes, si on désigne par (X) l'ensemble sous-jacent à X, on voit qu'on a une application surjective canonique  $(\mathbf{X} \times_{\mathrm{S}} \mathbf{Y}) \to (\mathbf{X}) \times_{(\mathrm{S})} (\mathbf{Y})$ ; il faut noter que cette application n'est pas injective en général; autrement dit, il peut exister plusieurs points z distincts dans  $X \times_{S} Y$  ayant mêmes projections  $x \in X, y \in Y$ ; c'est ce qu'on voit déjà lorsque S, X, Y sont des spectres premiers de corps k, K, K', car le produit tensoriel  $K \otimes_{k} K'$  a en général plusieurs idéaux premiers distincts (cf. 3.4.9).

Corollaire (3.4.8). — Soient $f: \mathrm{X} \to \mathrm{Y}$ un S-morphisme, $f_{(\mathrm{S}')}: \mathrm{X}_{(\mathrm{S}')} \to \mathrm{Y}_{(\mathrm{S}')}$ le $\mathrm{S}'$-morphisme déduit de $f$ par une extension $\mathrm{S}' \to \mathrm{S}$ du préschéma de base. Soit $p$ (resp. $q$) la projection $\mathrm{X}_{(\mathrm{S}')} \to \mathrm{X}$ (resp. $\mathrm{Y}_{(\mathrm{S}')} \to \mathrm{Y}$); pour toute partie M de X, on a

$$
q ^ {- 1} (f (\mathbf {M})) = f _ {(\mathrm{S} ^ {\prime})} (p ^ {- 1} (\mathbf {M}))
$$

En effet (3.3.11),  $X_{(S')}$  s'identifie au produit  $X \times_{Y} Y_{(S')}$  grâce au diagramme commutatif

![](images/page_112_image_1.jpg)

En vertu de (3.4.7), la relation $q(y') = p(x)$ pour $x \in \mathbf{M}$, $y' \in Y_{(S')}$ équivaut à l'existence d'un $x' \in X_{(S')}$ tel que $p(x') = x$ et $f_{(S')} (x') = y'$, d'où le corollaire.

Le lemme (3.4.6) se précise de la façon suivante :

Proposition (3.4.9). — Soient X, Y deux S-préschémas, x un point de X, y un point de Y, au-dessus du même point  $s \in S$ . L'ensemble des points de  $X \times_{s} Y$  ayant pour projections x et y est en correspondance biunivoque canonique avec l'ensemble des types d'extensions composées de  $\mathbf{k}(x)$  et  $\mathbf{k}(y)$  considérés comme extensions de  $\mathbf{k}(s)$  (Bourbaki, Alg., chap. VIII, § 8, prop. 2).

Soit $p$ (resp. $q$) la projection de $X \times_{s} Y$ dans $X$ (resp. $Y$) et soit $E$ le sous-espace $p^{-1}(x) \cap q^{-1}(y)$ de l'espace sous-jacent à $X \times_{s} Y$. Notons d'abord que les morphismes $\text{Spec}(\boldsymbol{k}(x)) \to S$ et $\text{Spec}(\boldsymbol{k}(y)) \to S$ se factorisent en $\text{Spec}(\boldsymbol{k}(x)) \to \text{Spec}(\boldsymbol{k}(s)) \to S$ et $\text{Spec}(\boldsymbol{k}(y)) \to \text{Spec}(\boldsymbol{k}(s)) \to S$; comme $\text{Spec}(\boldsymbol{k}(s)) \to S$ est un monomorphisme (2.4.7), il résulte de (3.2.4) que l'on a

$$
\mathrm{P} = \operatorname{Spec} (\boldsymbol {k} (x)) \times_ {\mathrm{s}} \operatorname{Spec} (\boldsymbol {k} (y)) = \operatorname{Spec} (\boldsymbol {k} (x)) \times_ {\operatorname{Spec} (\boldsymbol {k} (s))} \operatorname{Spec} (\boldsymbol {k} (y)) = \operatorname{Spec} (\boldsymbol {k} (x) \otimes_ {\boldsymbol {k} (s)} \boldsymbol {k} (y))
$$

Nous allons définir deux applications $\alpha: P_0 \to E$, $\beta: E \to P_0$ réciproques l'une de l'autre ($P_0$ désignant l'ensemble sous-jacent au préschéma $P$). Si $i: \text{Spec}(\boldsymbol{k}(x)) \to X$ et $j: \text{Spec}(\boldsymbol{k}(y)) \to Y$ sont les morphismes canoniques (2.4.5), on prendra pour $\alpha$ l'application des espaces sous-jacents correspondant au morphisme $i \times_{8} j$. D'autre part, tout $z \in E$ définit par hypothèse deux $\boldsymbol{k}(s)$-monomorphismes $\boldsymbol{k}(x) \to \boldsymbol{k}(z)$ et $\boldsymbol{k}(y) \to \boldsymbol{k}(z)$, donc un $\boldsymbol{k}(s)$-monomorphisme produit tensoriel $\boldsymbol{k}(x) \otimes_{\boldsymbol{k}(s)} \boldsymbol{k}(y) \to \boldsymbol{k}(z)$ et par suite un morphisme $\text{Spec}(\boldsymbol{k}(z)) \to P$; $\beta(z)$ sera l'image de $z$ dans $P_0$ par ce morphisme. La vérification du fait que $\alpha \circ \beta$ et $\beta \circ \alpha$ sont les applications identiques découle de (2.4.5) et de la définition du produit (3.2.1). On sait enfin que $P_0$ est en correspondance biunivoque avec l'ensemble des types d'extensions composées de $\boldsymbol{k}(x)$ et $\boldsymbol{k}(y)$ (Bourbaki, Alg., chap. VIII, § 8, prop. 1).

## 3.5. Surjections et injections.

(3.5.1) De façon générale, considérons une propriété P de morphismes de préschémas, et les deux propositions suivantes :

(i) Si $f: \mathbf{X} \to \mathbf{X}'$, $g: \mathbf{Y} \to \mathbf{Y}'$ sont deux S-morphismes possédant la propriété $\mathbf{P}$, $f \times_{\mathrm{sg}} g$ possède la propriété $\mathbf{P}$.

(ii) Si $f: \mathbf{X} \to \mathbf{Y}$ est un S-morphisme possédant la propriété $\mathbf{P}$, tout S'-morphisme $f_{(S')} : \mathbf{X}_{(S')} \to \mathbf{Y}_{(S')}$, déduit de $f$ par extension du préschéma de base, possède la propriété $\mathbf{P}$.

Comme $f_{(\mathrm{S}^{\prime})} = f \times_{\mathrm{S}} \mathrm{I}_{\mathrm{S}^{\prime}}$, on voit que si pour tout préschéma X l'identité $\mathrm{I}_{\mathrm{X}}$ possède la propriété $P$, (i) implique (ii) ; comme d'autre part, $f \times_{\mathrm{S}} g$ est le morphisme composé

$$
\mathbf {X} \times_ {\mathrm{s}} \mathbf {Y} \stackrel {f \times \mathbf {1} _ {\mathbf {Y}}} {\longrightarrow} \mathbf {X} ^ {\prime} \times_ {\mathrm{s}} \mathbf {Y} \stackrel {\mathbf {1} _ {\mathbf {X}} \times g} {\longrightarrow} \mathbf {X} ^ {\prime} \times_ {\mathrm{s}} \mathbf {Y} ^ {\prime}
$$

on voit que, si le composé de deux morphismes possédant la propriété P, possède aussi cette propriété, alors (ii) implique (i).

Une première application de cette remarque est la

Proposition (3.5.2). — (i) Si $f: \mathbf{X} \to \mathbf{X}'$, $g: \mathbf{Y} \to \mathbf{Y}'$ sont des S-morphismes surjectifs, $f \times_{\mathbb{S}} g$ est surjectif.

(ii) Si $f: \mathbf{X} \to \mathbf{Y}$ est un S-morphisme surjectif, $f_{(\mathbb{S}^{\prime})}$ est surjectif pour toute extension $\mathbf{S}'$ du préschéma de base.

Le composé de deux surjections étant une surjection, il suffit de démontrer (ii) ; mais cette proposition résulte aussitôt de (3.4.8) appliqué à M=X.

Proposition (3.5.3). — Pour qu'un morphisme $f: \mathbf{X} \to \mathbf{Y}$ soit surjectif, il faut et il suffit que pour tout corps $\mathbf{K}$ et tout morphisme $\operatorname{Spec}(\mathbf{K}) \to \mathbf{Y}$, il existe une extension $\mathbf{K}'$ de $\mathbf{K}$ et un morphisme $\operatorname{Spec}(\mathbf{K}') \to \mathbf{X}$ rendant commutatif le diagramme

$$
\begin{array}{c} \mathbf {X} \leftarrow \operatorname{Spec} (\mathbf {K} ^ {\prime}) \\ f \downarrow \qquad \qquad \qquad \downarrow \\ \mathbf {Y} \leftarrow \operatorname{Spec} (\mathbf {K}) \end{array}
$$

La condition est suffisante, car pour tout $y \in \mathbf{Y}$, il suffit de l'appliquer à un morphisme $\operatorname{Spec}(\mathbf{K}) \to \mathbf{Y}$ correspondant à un monomorphisme $\boldsymbol{k}(y) \to \mathbf{K}$, $\mathbf{K}$ étant une extension de $\boldsymbol{k}(y)$ (2.4.6). Inversement, supposons $f$ surjectif, et soit $y \in \mathbf{Y}$ l'image de l'unique point de $\operatorname{Spec}(\mathbf{K})$; il existe $x \in \mathbf{X}$ tel que $f(x) = y$; considérons le monomorphisme correspondant $\boldsymbol{k}(y) \to \boldsymbol{k}(x)$ (2.2.1); il suffit alors de prendre $\mathbf{K}'$ extension de $\boldsymbol{k}(y)$ telle qu'il existe des $\boldsymbol{k}(y)$-monomorphismes de $\boldsymbol{k}(x)$ et de $\mathbf{K}$ dans $\mathbf{K}'$ (Bourbaki, Alg., chap. V, § 4, prop. 2); le morphisme $\operatorname{Spec}(\mathbf{K}') \to \mathbf{X}$ correspondant à $\boldsymbol{k}(x) \to \mathbf{K}'$ répond à la question.

Avec le langage introduit dans (3.4.5), on peut dire encore que tout point géométrique de Y à valeurs dans K provient d'un point géométrique de X à valeurs dans une extension de K.

Définition (3.5.4). — On dit qu'un morphisme de préschémas $f: \mathbf{X} \to \mathbf{Y}$ est universellement injectif, ou un morphisme radiciel, si pour tout corps $\mathbf{K}$, l'application correspondante $\mathbf{X}(\mathbf{K}) \to \mathbf{Y}(\mathbf{K})$ est injective.

Il résulte aussitôt des définitions que tout monomorphisme de préschémas (T, i.1) est radiciel.

(3.5.5) Pour qu'un morphisme $f: \mathbf{X} \to \mathbf{Y}$ soit radiciel, il suffit que la condition de la déf. (3.5.4) soit vérifiée pour tout corps algébriquement clos. En effet, si K est un corps quelconque, $\mathbf{K}'$ une extension algébriquement close de K, le diagramme

$$
\begin{array}{c} \mathbf {X} (\mathbf {K}) \xrightarrow {\alpha} \mathbf {Y} (\mathbf {K}) \\ \varphi \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow \varphi^ {\prime} \\ \mathbf {X} (\mathbf {K} ^ {\prime}) \xrightarrow [ \alpha^ {\prime} ]{} \mathbf {Y} (\mathbf {K} ^ {\prime}) \end{array}
$$

est commutatif, $\varphi$ et $\varphi'$ provenant du morphisme $\operatorname{Spec}(\mathbf{K}')\to\operatorname{Spec}(\mathbf{K})$, $\alpha$ et $\alpha'$ correspondant à $f$. Or, $\varphi$ est injectif et il en est de même de $\alpha'$ par hypothèse ; donc $\alpha$ est nécessairement injectif.

Proposition (3.5.6). — Soient $f: \mathrm{X} \to \mathrm{Y}$, $g: \mathrm{Y} \to \mathrm{Z}$ deux morphismes de préschémas.

(i) Si f et g sont radiciels, il en est de même de gof.

(ii) Inversement, si gof est radiciel, il en est de même de f.

Compte tenu de la déf. (3.5.4), la proposition revient aux assertions correspondantes pour les applications  $\mathbf{X}(\mathbf{K})\to\mathbf{Y}(\mathbf{K})\to\mathbf{Z}(\mathbf{K})$ , qui sont évidentes.

Proposition (3.5.7). — (i) Si les S-morphismes $f: X \to X'$, $g: Y \to Y'$ sont radiciels, il en est de même de $f \times_{\mathbb{S}} g$.

(ii) Si le S-morphisme $f: \mathbf{X} \to \mathbf{Y}$ est radiciel, il en est de même de $f_{(S')} : \mathbf{X}_{(S')} \to \mathbf{Y}_{(S')}$ pour toute extension $S' \to S$ du préschéma de base.

Vu (3.5.1), il suffit de démontrer (i). On a vu (3.4.2.1) que

$$
(\mathbf {X} \times_ {\mathrm{S}} \mathbf {Y}) (\mathbf {K}) = \mathbf {X} (\mathbf {K}) \times_ {\mathrm{S} (\mathbf {K})} \mathbf {Y} (\mathbf {K}), \quad \left(\mathbf {X} ^ {\prime} \times_ {\mathrm{S}} \mathbf {Y} ^ {\prime}\right) (\mathbf {K}) = \mathbf {X} ^ {\prime} (\mathbf {K}) \times_ {\mathrm{S} (\mathbf {K})} \mathbf {Y} ^ {\prime} (\mathbf {K})
$$

l'application  $(\mathbf{X} \times_{\mathbb{S}} \mathbf{Y})(\mathbf{K}) \to (\mathbf{X}' \times_{\mathbb{S}} \mathbf{Y}')(\mathbf{K})$  correspondant à  $f \times_{sg} s'$  identifie alors à  $(u, v) \to (f \circ u, g \circ v)$  et la proposition en résulte aussitôt.

Proposition (3.5.8). — Pour qu'un morphisme $f = (\psi, \theta) : X \to Y$ soit radiciel, il faut et il suffit que $\psi$ soit injectif et que, pour tout $x \in X$, le monomorphisme $\theta^x : k(\psi(x)) \to k(x)$ fasse de $k(x)$ une extension radicielle de $k(\psi(x))$.

Supposons $f$ radiciel et montrons d'abord que la relation $\psi(x_1) = \psi(x_2) = y$ entraîne nécessairement $x_1 = x_2$. En effet, il existe un corps K, extension de $\pmb{k}(y)$, et des $\pmb{k}(y)$-monomorphismes $\pmb{k}(x_1) \to \mathbf{K}$, $\pmb{k}(x_2) \to \mathbf{K}$ (Bourbaki, Alg., chap. V, § 4, prop. 2); les morphismes correspondants $u_1: \operatorname{Spec}(\mathbf{K}) \to \mathbf{X}$, $u_2: \operatorname{Spec}(\mathbf{K}) \to \mathbf{X}$ sont donc tels que $f o u_1 = f o u_2$, donc $u_1 = u_2$ par hypothèse, et cela implique en particulier $x_1 = x_2$. Considérons maintenant $\pmb{k}(x)$ comme extension de $\pmb{k}(\psi(x))$ au moyen de $\theta^x: \text{si } \pmb{k}(x)$ n'est pas extension radicielle de $\pmb{k}(\psi(x))$, il existe deux $\pmb{k}(\psi(x))$-monomorphismes distincts de $\pmb{k}(x)$ dans une extension algébriquement close K de $\pmb{k}(\psi(x))$ et les deux morphismes correspondants $\operatorname{Spec}(\mathbf{K}) \to \mathbf{X}$ violeraient l'hypothèse. Inversement, compte tenu de (2.4.6), il est immédiat que les conditions de l'énoncé sont suffisantes pour que $f$ soit radiciel.

Corollaire (3.5.9). — Si A est un anneau, S une partie multiplicative de A, le morphisme canonique  $\operatorname{Spec}(S^{-1}A)\to\operatorname{Spec}(A)$  est radiciel.

En effet, ce morphisme est un monomorphisme (1.6.2).

Corollaire (3.5.10). — Soient $f: \mathbf{X} \to \mathbf{Y}$ un morphisme radiciel, $g: \mathbf{Y}' \to \mathbf{Y}$ un morphisme, et soit $\mathbf{X}' = \mathbf{X}_{(\mathbf{Y}')} = \mathbf{X} \times_{\mathbf{Y}} \mathbf{Y}'$. Alors le morphisme radiciel $f_{(\mathbf{Y}')}$ (3.5.7 (ii)) est une bijection de l'espace sous-jacent $\mathbf{X}'$ sur $g^{-1}(f(\mathbf{X}))$; en outre, pour tout corps $\mathbf{K}$, l'ensemble $\mathbf{X}'(\mathbf{K})$ s'identifie au sous-ensemble de $\mathbf{Y}'(\mathbf{K})$ image réciproque par l'application $\mathbf{Y}'(\mathbf{K}) \to \mathbf{Y}(\mathbf{K})$ (correspondant à $g$) du sous-ensemble $\mathbf{X}(\mathbf{K})$ de $\mathbf{Y}(\mathbf{K})$.

La première assertion résulte aussitôt de (3.5.8) et de (3.4.8) ; la seconde, de la commutativité du diagramme

$$
\begin{array}{c} \mathbf {X} ^ {\prime} (\mathbf {K}) \to \mathbf {Y} ^ {\prime} (\mathbf {K}) \\ \downarrow \qquad \qquad \qquad \downarrow \\ \mathbf {X} (\mathbf {K}) \to \mathbf {Y} (\mathbf {K}) \end{array}
$$

Remarque (3.5.11). — Nous dirons qu'un morphisme $f = (\psi, \theta)$ de préschémas est injectif si l'application $\psi$ est injective. Pour qu'un morphisme $f = (\psi, \theta) : \mathbf{X} \to \mathbf{Y}$ soit radiciel, il faut et il suffit que pour tout morphisme $\mathbf{Y}' \to \mathbf{Y}$, le morphisme $f_{(\mathbf{Y}')} : \mathbf{X}_{(\mathbf{Y}')} \to \mathbf{Y}'$ soit injectif (ce qui justifie la terminologie de morphisme universellement injectif). En effet, la condition est nécessaire en vertu de (3.5.7, (ii)) et de (3.5.8). Inversement, la condition implique d'abord que $\psi$ est injectif; si pour un $x \in \mathbf{X}$, le monomorphisme $\theta^x : \boldsymbol{k}(\psi(x)) \to \boldsymbol{k}(x)$ n'était pas radiciel, il y aurait une extension $\mathbf{K}$ de $\boldsymbol{k}(\psi(x))$ et deux morphismes distincts $\text{Spec}(\mathbf{K}) \to \mathbf{X}$ correspondant au même morphisme $\text{Spec}(\mathbf{K}) \to \mathbf{Y}$ (3.5.8). Mais alors, en posant $\mathbf{Y}' = \text{Spec}(\mathbf{K})$, il y aurait deux $\mathbf{Y}'$-sections distinctes de $\mathbf{X}_{(\mathbf{Y}')}$ (3.3.14), ce qui contredit l'hypothèse que $f_{(\mathbf{Y}')}$ est injectif.

## 3.6. Fibres.

Proposition (3.6.1). — Soient $f: \mathbf{X} \to \mathbf{Y}$ un morphisme, $y$ un point de $\mathbf{Y}$, $\mathfrak{a}_y$ un idéal de définition de $\mathcal{O}_y$ pour la topologie $\mathfrak{m}_y$-préadique. La projection $p: \mathbf{X} \times_{\mathbf{Y}} \text{Spec}(\mathcal{O}_y / \mathfrak{a}_y) \to \mathbf{X}$ est un homéomorphisme de l'espace sous-jacent au préschéma $\mathbf{X} \times_{\mathbf{Y}} \text{Spec}(\mathcal{O}_y / \mathfrak{a}_y)$ sur la fibre $f^{-1}(y)$ munie de la topologie induite par celle de l'espace sous-jacent à $\mathbf{X}$.

Comme $\operatorname{Spec}(\mathcal{O}_y / \mathfrak{a}_y) \to \mathrm{Y}$ est radiciel (3.5.4 et 2.4.7) et que $\operatorname{Spec}(\mathcal{O}_y / \mathfrak{a}_y)$ est réduit à un seul point, l'idéal $\mathfrak{m}_y / \mathfrak{a}_y$ étant nilpotent par hypothèse (1.1.12), on sait déjà (3.5.10 et 3.3.4) que $p$ identifie en tant qu'ensemble l'espace sous-jacent à $\mathrm{X} \times_{\mathrm{Y}} \operatorname{Spec}(\mathcal{O}_y / \mathfrak{a}_y)$ à $f^{-1}(y)$; tout revient à démontrer que $p$ est un homéomorphisme. En vertu de (3.2.7), la question est locale sur $\mathrm{X}$ et $\mathrm{Y}$, et on peut donc supposer que $\mathrm{X} = \operatorname{Spec}(\mathrm{B})$, $\mathrm{Y} = \operatorname{Spec}(\mathrm{A})$, B étant une A-algèbre. Le morphisme $p$ correspond alors à l'homomorphisme $\mathrm{i} \otimes \varphi : \mathrm{B} \to \mathrm{B} \otimes_{\mathrm{A}} \mathrm{A}'$, où $\mathrm{A}' = \mathrm{A}_y / \mathfrak{a}_y$ et $\varphi$ est l'application canonique de A dans $\mathrm{A}'$. Or, tout élément de $\mathrm{B} \otimes_{\mathrm{A}} \mathrm{A}'$ s'écrit $\sum_{i} b_i \otimes \varphi(a_i) / \varphi(s) = (\sum_{i} (a_i b_i \otimes \mathrm{i})) (\mathrm{i} \otimes \varphi(s))^{-1}$, où $s \notin \mathrm{j}_y$, et la prop. (1.2.4) est applicable.

(3.6.2) Dans toute la suite de ce Traité, lorsque nous considérerons une fibre  $f^{-1}(y)$  d'un morphisme comme munie d'une structure de  $\boldsymbol{k}(y)$ -préschéma, il s'agira toujours du préschéma obtenu en transportant la structure de  $\mathbf{X} \times_{\mathbf{Y}} \text{Spec}(\boldsymbol{k}(y))$  par la projection dans X. Nous écrirons aussi ce dernier produit  $\mathbf{X} \otimes_{\mathbf{Y}} \boldsymbol{k}(y)$ , ou  $\mathbf{X} \otimes_{\mathcal{O}_{\mathbf{Y}}} \boldsymbol{k}(y)$ ; plus généralement, si B est une  $O_{y}$ -algèbre, nous noterons  $X \otimes_{Y} B$  ou  $X \otimes_{O_{Y}} B$  le produit  $X \times_{Y} \text{Spec}(B)$ .

Avec la convention précédente, il résulte de (3.5.10) que les points de X à valeurs dans une extension K de  $\boldsymbol{k}(y)$  sont identifiés aux points de  $f^{-1}(y)$  à valeurs dans K.

(3.6.3) Soient $f: \mathbf{X} \to \mathbf{Y}$, $g: \mathbf{Y} \to \mathbf{Z}$ deux morphismes, $h = g \circ f$ leur composé; pour tout $z \in \mathbf{Z}$, la fibre $h^{-1}(z)$ est un préschéma isomorphe à

$$
\mathbf {X} \times_ {\mathrm{Z}} \operatorname{Spec} (\boldsymbol {k} (z)) = (\mathbf {X} \times_ {\mathrm{Y}} \mathbf {Y}) \times_ {\mathrm{Z}} \operatorname{Spec} (\boldsymbol {k} (z)) = \mathbf {X} \times_ {\mathrm{Y}} g ^ {- 1} (z)
$$

En particulier, si U est une partie ouverte de X, le préschéma induit sur  $\mathbf{U}\cap f^{-1}(y)$  par le préschéma  $f^{-1}(y)$  est isomorphe à  $f_{\mathbf{U}}^{-1}(y)$  ( $f_{U}$  étant la restriction de  $f$  à U).

Proposition (3.6.4) (« transitivité des fibres »). — Soient $f: \mathrm{X} \to \mathrm{Y}$, $g: \mathrm{Y}' \to \mathrm{Y}$ deux morphismes; posons $\mathrm{X}' = \mathrm{X} \times_{\mathrm{Y}} \mathrm{Y}' = \mathrm{X}_{(\mathrm{Y}')}$, et $f' = f_{(\mathrm{Y}')}: \mathrm{X}' \to \mathrm{Y}'$. Pour tout $y' \in \mathrm{Y}'$, si on pose $y = g(y')$, le préschéma $f'^{-1}(y')$ est isomorphe à $f^{-1}(y) \otimes_{\boldsymbol{k}(y)} \boldsymbol{k}(y')$.

En effet, cela revient à remarquer que les deux préschémas $(\mathbf{X} \otimes_{\mathbf{Y}} \boldsymbol{k}(y)) \otimes_{\boldsymbol{k}(y)} \boldsymbol{k}(y')$ et $(\mathbf{X} \times_{\mathbf{Y}} \mathbf{Y}') \otimes_{\mathbf{Y}'} \boldsymbol{k}(y')$ sont tous deux canoniquement isomorphes à $\mathbf{X} \times_{\mathbf{Y}} \operatorname{Spec}(\boldsymbol{k}(y'))$ par (3.3.9.1).

En particulier, si V est un voisinage ouvert de y dans Y, et si on désigne par  $f_{V}$  la restriction de f au préschéma induit sur  $f^{-1}(V)$ , les préschémas  $f^{-1}(y)$  et  $f_{\mathrm{V}}^{-1}(y)$  s'identifient canoniquement.

Proposition (3.6.5). — Soient $f: \mathrm{X} \to \mathrm{Y}$ un morphisme, $y$ un point de Y, Z le préschéma local $\operatorname{Spec}(\mathcal{O}_y)$, $p = (\psi, \theta)$ la projection $\mathrm{X} \times_{\mathrm{Y}} \mathrm{Z} \to \mathrm{X}$; $p$ est un homéomorphisme de l'espace sous-jacent à $\mathrm{X} \times_{\mathrm{Y}} \mathrm{Z}$ sur le sous-espace $f^{-1}(\mathrm{Z})$ de X (lorsque l'espace sous-jacent à Z est identifié à un sous-espace de Y, cf. (2.4.2)), et pour tout $t \in \mathrm{X} \times_{\mathrm{Y}} \mathrm{Z}$, si on pose $z = \psi(t)$, $\theta_l^\sharp$ est un isomorphisme de $\mathcal{O}_z$ sur $\mathcal{O}_t$.

Comme Z (identifié à un sous-espace de Y) est contenu dans tout ouvert affine contenant y (2.4.2), on peut, comme dans (3.6.1) se ramener au cas où X=Spec(A) et Y=Spec(B) sont des schémas affines, A étant une B-algèbre. Alors  $X \times_{Y} Z$  est le spectre premier de  $A \otimes_{B} B_{y}$  et cet anneau s'identifie canoniquement à  $S^{-1}A$, où S est l'image de  $B - j_{y}$  dans A (0, 1.5.2); comme p correspond alors à l'homomorphisme canonique  $A \to S^{-1}A$, la proposition résulte de (1.6.2).

## 3.7. Application : réduction d'un préschéma mod. ℑ (1).

(3.7.1) Soient A un anneau, X un A-préschéma, J un idéal de A ; alors  $\mathrm{X}_{0}=\mathrm{X}\otimes_{\mathrm{A}}(\mathrm{A}/\mathfrak{J})$  est un  $(\mathrm{A}/\mathfrak{J})$ -préschéma, dont on dit parfois qu'il est déduit de X par réduction mod. J.

(3.7.2) Cette terminologie est surtout utilisée lorsque A est un anneau local et J son idéal maximal, de sorte que  $X_{0}$  est un préschéma sur le corps résiduel  $k=A/J$  de A.

Lorsqu'en outre A est intègre, de corps des fractions K, on peut aussi considérer le K-préschéma  $X' = X \otimes_{A} K$ . Par un abus de langage dont nous ne ferons pas usage, on disait d'ordinaire jusqu'à présent que  $X_{0}$  est déduit de  $X'$  par réduction mod. J. Dans les cas où ce langage était utilisé, A était un anneau local de dimension i (le plus souvent un anneau de valuation discrète) et il était sous-entendu (de façon plus ou moins explicite) que le K-préschéma  $X'$  donné était un sous-préschéma fermé d'un K-préschéma  $P'$  (en fait, un espace projectif type  $P_{K}^{r}$ , cf. II, 4.1.1), lui-même de la forme  $P' = P \otimes_{A} K$ , où P est un A-préschéma donné (en fait, le A-schéma  $P_{A}^{r}$ , avec les notations de II, 4.1.1). Dans notre langage, la définition de  $X_{0}$  à partir de  $X'$  se formule comme suit :

On considère le schéma affine  $Y=\text{Spec}(A)$ , formé de deux points, l'unique point

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(1) Ce numéro, qui fait usage de notions et résultats de la suite du chap. Ier et du chap. II, ne sera pas utilisé par la suite, et n'est destiné qu'aux lecteurs familiers avec la Géométrie algébrique classique.</span></small>

fermé $y = \mathfrak{J}$ et le point générique (o), l'ensemble U réduit au point générique étant donc un ouvert $U = \text{Spec}(K)$ dans Y. Si X est un A-préschéma (autrement dit un Y-préschéma), $X \otimes_A K = X'$ n'est autre que le préschéma induit par X sur $\psi^{-1}(U)$, en désignant par $\psi$ le morphisme structural $X \to Y$. En particulier, si $\varphi$ est le morphisme structural $P \to Y$, un sous-préschéma fermé $X'$ de $P' = \varphi^{-1}(U)$ est donc un sous-préschéma (localement fermé) de P. Si P est noethérien (par exemple si A est noethérien et P de type fini sur A), il existe un plus petit sous-préschéma fermé $X = \overline{X}'$ de P qui majore X (9.5.10), et $X'$ est le préschéma induit par X sur l'ouvert $\varphi^{-1}(U) \cap X$, donc est isomorphe à $X \otimes_A K$ (9.5.10). L'immersion de $X'$ dans $P' = P \otimes_A K$ permet donc de façon canonique de considérer $X'$ comme étant de la forme $X' = X \otimes_A K$, où X est un A-préschéma. On peut alors considérer le préschéma réduit mod. J, $X_0 = X \otimes_A k$, qui n'est autre d'ailleurs que la fibre $\psi^{-1}(y)$ du point fermé y. Jusqu'à présent, faute d'une terminologie adéquate, on avait évité d'introduire explicitement le A-préschéma X. Il convient cependant de noter que toutes les assertions faites habituellement sur le préschéma « réduit mod. J» $X_0$ doivent être regardées comme conséquences d'assertions plus complètes concernant X lui-même, et ne peuvent être formulées et comprises de façon satisfaisante qu'en les interprétant ainsi. Il semble d'ailleurs que les hypothèses faites reviennent toujours à des hypothèses sur X lui-même (indépendamment de la donnée préalable d'une immersion de $X'$ dans un $P_K^r$), ce qui permet de donner des énoncés plus intrinsèques.

(3.7.3) Signalons enfin un fait très particulier, qui a sans doute contribué à retarder la clarification conceptuelle de la situation envisagée ici : si A est un anneau de valuation discrète et si X est propre sur A (ce qui est en fait le cas si X est un sous-préschéma fermé d'un  $P_{A}^{r}$ , cf. II, 5.5.4), les points de X à valeurs dans A et les points de  $X'$  à valeurs dans K sont en correspondance biunivoque (II, 7.3.8). C'est pourquoi on a souvent cru démontrer des résultats concernant  $X'$ , alors qu'en réalité on démontrait des énoncés concernant X, et qui restent valables (sous cette forme) lorsqu'on ne suppose plus l'anneau local de base de dimension 1.

## § 4. SOUS-PRÉSCHÉMAS ET MORPHISMES D'IMMERSION

## 4.1. Sous-préschémas.

(4.1.1) Comme la notion de faisceau quasi-cohérent (0, 5.1.3) est locale, un $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent $\mathcal{F}$ sur un préschéma X peut être défini par la condition que, pour tout ouvert affine V de X, $\mathcal{F}|\mathrm{V}$ est isomorphe à un faisceau associé à un $\Gamma(\mathrm{V},\mathcal{O}_{\mathrm{X}})$-module (1.4.1). Il est clair que, sur un préschéma X, le faisceau structural $\mathcal{O}_{\mathrm{X}}$ est quasi-cohérent et que noyaux, conoyaux, images d'homomorphismes de $\mathcal{O}_{\mathrm{X}}$-Modules quasi-cohérents, limites inductives et sommes directes de $\mathcal{O}_{\mathrm{X}}$-Modules quasi-cohérents sont quasi-cohérents (1.3.7 et 1.3.9).

Proposition (4.1.2). — Soient X un préschéma, $\mathcal{I}$ un faisceau quasi-cohérent d'idéaux dans $\mathcal{O}_{\mathrm{X}}$. Le support Y du faisceau $\mathcal{O}_{\mathrm{X}} / \mathcal{I}$ est alors fermé, et si on désigne par $\mathcal{O}_{\mathrm{Y}}$ la restriction de $\mathcal{O}_{\mathrm{X}} / \mathcal{I}$ à Y, (Y, $\mathcal{O}_{\mathrm{Y}}$) est un préschéma.

Il suffit évidemment (2.1.3) de considérer le cas où X est un schéma affine, et de montrer que dans ce cas Y est fermé dans X et est un schéma affine. En effet, si  $\mathbf{X}=\operatorname{Spec}(\mathbf{A})$ , on a  $O_{X}=\widetilde{A}$  et  $I=\widetilde{J}$ , où J est un idéal de A (1.4.1); Y est alors égal à la partie fermée  $\mathrm{V}(\mathfrak{J})$  de X et s'identifie au spectre premier de l'anneau  $\mathbf{B}=\mathbf{A}/\mathfrak{J}$  (1.1.11); de plus, si  $\varphi$  est l'homomorphisme canonique  $A\to B=A/\mathfrak{J}$ , l'image directe  $^{a}\varphi_{*}(\widetilde{\mathbf{B}})$  s'identifie canoniquement au faisceau  $\widetilde{A}/\widetilde{J}=\mathcal{O}_{X}/\mathcal{I}$  (1.6.3 et 1.3.9), ce qui achève la démonstration.

Nous dirons que  $(\mathbf{Y}, \mathcal{O}_{\mathbf{Y}})$  est le sous-préschéma de  $(\mathbf{X}, \mathcal{O}_{\mathbf{X}})$  défini par le faisceau d'idéaux I; c'est un cas particulier de la notion générale de sous-préschéma :

Définition (4.1.3). — On dit qu'un espace annelé (Y, $\mathcal{O}_{\mathrm{Y}}$) est un sous-préschéma d'un préschéma (X, $\mathcal{O}_{\mathrm{X}}$) si :

$^{10}$ Y est un sous-espace localement fermé de X ; $^{20}$ Si U désigne le plus grand ouvert de X contenant Y et tel que Y soit fermé dans U (autrement dit, le complémentaire dans X de la frontière de Y par rapport à $\overline{Y}$), (Y, $\mathcal{O}_{\mathrm{Y}}$) est un sous-préschéma de (U, $\mathcal{O}_{\mathrm{X}}$ | U) défini par un faisceau quasi-cohérent d'idéaux de $\mathcal{O}_{\mathrm{X}}$ | U. On dit que le sous-préschéma (Y, $\mathcal{O}_{\mathrm{Y}}$) de (X, $\mathcal{O}_{\mathrm{X}}$) est fermé si Y est fermé dans X (auquel cas U = X).

Il résulte aussitôt de cette définition et de (4.1.2) que les sous-préschémas fermés de X sont en correspondance biunivoque canonique avec les faisceaux d'idéaux quasicohérents J de  $O_{X}$ , car le fait que deux tels faisceaux J,  $J'$  aient même support (fermé) Y et soient tels que les restrictions de  $O_{X}/J$  et de  $O_{X}/J'$  à Y soient identiques, entraîne aussitôt que  $J'=J$ .

(4.1.4) Soient (Y, $\mathcal{O}_{\mathrm{Y}}$) un sous-préschéma de X, U le plus grand ouvert de X contenant Y et dans lequel Y soit fermé, V un ouvert de X contenu dans U ; alors $\mathrm{V} \cap \mathrm{Y}$ est fermé dans V. En outre, si Y est défini par le faisceau quasi-cohérent $\mathcal{J}$ d'idéaux de $\mathcal{O}_{\mathrm{X}}|\mathrm{U}$, $\mathcal{J}|\mathrm{V}$ est un faisceau quasi-cohérent d'idéaux de $\mathcal{O}_{\mathrm{X}}|\mathrm{V}$, et il est immédiat que le préschéma induit par Y sur $\mathrm{Y} \cap \mathrm{V}$ est le sous-préschéma fermé de V défini par le faisceau d'idéaux $\mathcal{J}|\mathrm{V}$. Inversement :

Proposition (4.1.5). — Soit (Y, $\mathcal{O}_{\mathrm{Y}}$) un espace annelé tel que Y soit un sous-espace de X et qu'il existe un recouvrement ($V_{\alpha}$) de Y par des ouverts de X tels que pour tout $\alpha$, $Y \cap V_{\alpha}$ soit fermé dans $V_{\alpha}$ et que l'espace annelé ($Y \cap V_{\alpha}$, $\mathcal{O}_{\mathrm{Y}} | (Y \cap V_{\alpha})$) soit un sous-préschéma fermé du préschéma induit sur $V_{\alpha}$ par X. Alors (Y, $\mathcal{O}_{\mathrm{Y}}$) est un sous-préschéma de X.

L'hypothèse implique que Y est localement fermé dans X et que le plus grand ouvert U contenant Y et dans lequel Y est fermé contient tous les  $V_{\alpha}$ ; on peut donc se ramener au cas où U=X et Y est fermé dans X. On définit alors un faisceau quasi-cohérent d'idéaux J de  $O_{X}$  en prenant pour  $J|V_{\alpha}$  le faisceau d'idéaux de  $O_{X}|V_{\alpha}$  qui définit le sous-préschéma fermé  $(Y\cap V_{\alpha}, O_{Y}|(Y\cap V_{\alpha}))$  et pour tout ouvert W de X ne rencontrant pas Y,  $J|W=O_{X}|W$ . On vérifie immédiatement en vertu de (4.1.3) et (4.1.4) qu'il existe un faisceau d'idéaux J et un seul satisfaisant à ces conditions et qu'il définit le sous-préschéma fermé  $(Y, O_{Y})$ .

En particulier, le préschéma induit par X sur un ouvert de X est un sous-préschéma de X.

Proposition (4.1.6). — Un sous-préschéma (resp. un sous-préschéma fermé) d'un sous-

préschéma (resp. sous-préschéma fermé) de X s'identifie canoniquement à un sous-préschéma (resp. sous-préschéma fermé) de X.

Une partie localement fermée d'un sous-espace localement fermé de X étant un sous-espace localement fermé de X, il est clair (4.1.5) que la question est locale et qu'on peut donc supposer X affine ; la proposition résulte alors de l'identification canonique de A/ $J'$ et de (A/ $J$)/($J'/J$) lorsque $J$, $J'$ sont deux idéaux d'un anneau A tels que $J \subset J'$. Nous ferons toujours par la suite l'identification précédente.

(4.1.7) Soit Y un sous-préschéma d'un préschéma X, et désignons par $\psi$ l'injection canonique Y$\rightarrow$X des espaces sous-jacents; on sait que l'image réciproque $\psi^{*}(\mathcal{O}_{\mathrm{X}})$ est la restriction $\mathcal{O}_{\mathrm{X}}|\mathrm{Y}$ (0, 3.7.1). Si, pour tout $y\in\mathrm{Y}$, on désigne par $\omega_{y}$ l'homomorphisme canonique $(\mathcal{O}_{\mathrm{X}})_{y}\to(\mathcal{O}_{\mathrm{Y}})_{y}$, ces homomorphismes sont les restrictions aux fibres d'un homomorphisme surjectif $\omega$ de faisceaux d'anneaux $\mathcal{O}_{\mathrm{X}}|\mathrm{Y}\to\mathcal{O}_{\mathrm{Y}}$: il suffit en effet de le vérifier localement sur Y, c'est-à-dire que l'on peut supposer X affine et le sous-préschéma Y fermé; si dans ce cas $\mathscr{I}$ est le faisceau d'idéaux dans $\mathcal{O}_{\mathrm{X}}$ qui définit Y, les $\omega_{y}$ ne sont autres que les restrictions aux fibres de l'homomorphisme $\mathcal{O}_{\mathrm{X}}|\mathrm{Y}\to(\mathcal{O}_{\mathrm{X}}/\mathscr{I})|\mathrm{Y}$. Nous avons donc défini un monomorphisme d'espaces annelés (0, 4.1.1) $j=(\psi,\omega^{\flat})$ qui est évidemment un morphisme Y$\rightarrow$X de préschémas (2.2.1), et que nous appellerons le morphisme d'injection canonique.

Si $f: \mathbf{X} \to \mathbf{Z}$ est un morphisme, nous dirons encore que le morphisme composé $\mathbf{Y} \xrightarrow{j} \mathbf{X} \xrightarrow{f} \mathbf{Z}$ est la restriction de $f$ au sous-préschéma $\mathbf{Y}$.

(4.1.8) Conformément aux définitions générales (T, I, 1.1), nous dirons qu'un morphisme de préschémas $f: \mathbf{Z} \to \mathbf{X}$ est majoré par le morphisme d'injection $j: \mathbf{Y} \to \mathbf{X}$ d'un sous-préschéma Y de X si $f$ se factorise en $Z \xrightarrow{g} Y \xrightarrow{j} X$, où $g$ est un morphisme de préschémas; $g$ est nécessairement unique puisque $j$ est un monomorphisme.

Proposition (4.1.9). — Pour qu'un morphisme $f: \mathbf{Z} \to \mathbf{X}$ soit majoré par un morphisme d'injection $j: \mathbf{Y} \to \mathbf{X}$, il faut et il suffit que $f(\mathbf{Z}) \subset \mathbf{Y}$ et que, pour tout $z \in \mathbf{Z}$, si on pose $y = f(z)$, l'homomorphisme $(\mathcal{O}_{\mathbf{X}})_y \to \mathcal{O}_z$ correspondant à $f$ se factorise en $(\mathcal{O}_{\mathbf{X}})_y \to (\mathcal{O}_{\mathbf{Y}})_y \to \mathcal{O}_z$ (ou, ce qui revient au même, que le noyau de $(\mathcal{O}_{\mathbf{X}})_y \to \mathcal{O}_z$ contienne celui de $(\mathcal{O}_{\mathbf{X}})_y \to (\mathcal{O}_{\mathbf{Y}})_y$).

Les conditions sont évidemment nécessaires. Pour voir qu'elles sont suffisantes, on peut se ramener au cas où Y est un sous-préschéma fermé de X, en remplaçant au besoin X par un ouvert U tel que Y soit fermé dans U (4.1.3); Y est alors défini par un faisceau quasi-cohérent $\mathcal{I}$ d'idéaux de $\mathcal{O}_{\mathrm{X}}$. Posons $f = (\psi, \theta)$, et soit $\mathcal{J}$ le faisceau d'idéaux de $\psi^{*}(\mathcal{O}_{\mathrm{X}})$, noyau de $\theta^{\sharp}: \psi^{*}(\mathcal{O}_{\mathrm{X}}) \to \mathcal{O}_{\mathrm{Z}}$; compte tenu des propriétés du foncteur $\psi^{*}(0, 3.7.2)$, l'hypothèse entraîne que pour tout $z \in \mathbb{Z}$, on a $(\psi^{*}(\mathcal{I}))_{z} \subset \mathcal{J}_{z}$, et par suite $\psi^{*}(\mathcal{I}) \subset \mathcal{J}$. Par suite, $\theta^{\sharp}$ se factorise en

$$
\psi^ {*} (\mathcal {O} _ {\mathrm{X}}) \rightarrow \psi^ {*} (\mathcal {O} _ {\mathrm{X}}) / \psi^ {*} (\mathcal {I}) = \psi^ {*} (\mathcal {O} _ {\mathrm{X}} / \mathcal {I}) \stackrel {\omega} {\rightarrow} \mathcal {O} _ {\mathrm{Z}}
$$

la première flèche étant l'homomorphisme canonique. Soit $\psi'$ l'application continue $Z\to Y$ coïncidant avec $\psi$; il est clair que l'on a $\psi'^{*}(\mathcal{O}_{Y})=\psi^{*}(\mathcal{O}_{X}/\mathcal{J})$; d'autre part, $\omega$ est évidemment un homomorphisme local, donc $g=(\psi',\omega^{\flat})$ est un morphisme $Z\to Y$

de préschémas (2.2.1), qui, en vertu de ce qui précède, est tel que $f=j\circ g$, d'où la proposition.

Corollaire (4.1.10). — Pour qu'un morphisme d'injection Z→X soit majoré par le morphisme d'injection Y→X, il faut et il suffit que Z soit un sous-préschéma de Y.

On écrit alors $Z \leqslant Y$, et cette relation est évidemment une relation d'ordre dans l'ensemble des sous-préschémas de $X$.

## 4.2. Morphismes d'immersion.

Définition (4.2.1). — On dit qu'un morphisme $f: \mathrm{Y} \to \mathrm{X}$ est une immersion (resp. une immersion fermée, une immersion ouverte) s'il se factorise en $\mathrm{Y} \xrightarrow{g} \mathrm{Z} \xrightarrow{j} \mathrm{X}$, où $g$ est un isomorphisme, $Z$ un sous-préschéma de $X$ (resp. un sous-préschéma fermé, un sous-préschéma induit sur un ouvert) et $j$ le morphisme d'injection.

Le sous-préschéma Z et l'isomorphisme g sont alors déterminés de façon unique, car si  $Z'$  est un second sous-préschéma de X,  $j'$  l'injection  $Z' \to X$  et  $g'$  un isomorphisme  $Y \to Z'$  tel que  $j \circ g = j' \circ g'$ , on en déduit  $j' = j \circ g \circ g'^{-1}$ , d'où  $Z' \leqslant Z$  (4.1.10), et on montre de même que  $Z \leqslant Z'$ , donc  $Z' = Z$ , et comme j est un monomorphisme de préschémas,  $g' = g$ .

On dit que $f = \text{jog}$ est la factorisation canonique de l'immersion $f$, et le sous-préschéma $Z$ et l'isomorphisme $g$ sont dits associés à $f$.

Il est clair qu'une immersion est un monomorphisme de préschémas (4.1.7) et a fortiori un morphisme radiciel (3.5.4).

Proposition (4.2.2). — a) Pour qu'un morphisme $f = (\psi, \theta): \mathrm{Y} \to \mathrm{X}$ soit une immersion ouverte, il faut et il suffit que $\psi$ soit un homéomorphisme de $\mathrm{Y}$ sur une partie ouverte de $\mathrm{X}$, et que pour tout $y \in \mathrm{Y}$, l'homomorphisme $\theta_y^\sharp: \mathcal{O}_{\psi(y)} \to \mathcal{O}_y$ soit bijectif.

b) Pour qu'un morphisme $f = (\psi, \theta): \mathbf{Y} \to \mathbf{X}$ soit une immersion (resp. une immersion fermée), il faut et il suffit que $\psi$ soit un homéomorphisme de $\mathbf{Y}$ sur une partie localement fermée (resp. fermée) de $\mathbf{X}$, et que pour tout $y \in \mathbf{Y}$, l'homomorphisme $\theta_y^\sharp: \mathcal{O}_{\psi(y)} \to \mathcal{O}_y$ soit surjectif.

a) Les conditions sont évidemment nécessaires. Inversement, si elles sont remplies, il est clair que $\theta^{\sharp}$ est un isomorphisme de $\mathcal{O}_{\mathrm{Y}}$ sur $\psi^{*}(\mathcal{O}_{\mathrm{X}})$, et $\psi^{*}(\mathcal{O}_{\mathrm{X}})$ est le faisceau déduit par transport de structure au moyen de $\psi^{-1}$ à partir de $\mathcal{O}_{\mathrm{X}}|\psi(\mathrm{Y})$; d'où la conclusion.

b) Les conditions étant évidemment nécessaires, prouvons qu'elles sont suffisantes. Considérons d'abord le cas particulier où l'on suppose que X est un schéma affine et que  $Z=\psi(Y)$  est fermé dans X. On sait (0, 3.4.6) que  $\psi_{*}(\mathcal{O}_{\mathrm{Y}})$  a alors pour support Z et que si l'on désigne par  $O_{Z}'$  sa restriction à Z, l'espace annelé (Z,  $O_{Z}'$ ) se déduit de (Y,  $O_{Y}$ ) par transport de structure au moyen de l'homéomorphisme  $\psi$, considéré comme application de Y sur Z. Montrons que  $f_{*}(\mathcal{O}_{\mathrm{Y}})=\psi_{*}(\mathcal{O}_{\mathrm{Y}})$  est un  $O_{X}$-Module quasi-cohérent. En effet, pour tout  $x\notin Z$,  $\psi_{*}(\mathcal{O}_{\mathrm{Y}})$, restreint à un voisinage convenable de x, est nul. Si au contraire  $x\in Z$, on a  $x=\psi(y)$  pour un  $y\in Y$  bien déterminé; soit V un voisinage ouvert affine de y dans Y;  $\psi(V)$  est alors ouvert dans Z, donc trace sur Z d'un ouvert U de X, et la restriction à U de  $\psi_{*}(\mathcal{O}_{\mathrm{Y}})$  est identique à la restriction à U de l'image

directe $(\psi_{\mathrm{V}})_{*}(\mathcal{O}_{\mathrm{Y}}|\mathrm{V})$, où $\psi_{\mathrm{V}}$ est la restriction de $\psi$ à V. Or, la restriction à $(\mathrm{V},\mathcal{O}_{\mathrm{Y}}|\mathrm{V})$ du morphisme $(\psi,\theta)$ est un morphisme de ce préschéma dans $(\mathrm{X},\mathcal{O}_{\mathrm{X}})$, et par suite est de la forme $(^a\varphi ,\widetilde{\varphi})$, où $\varphi$ est un homomorphisme de l'anneau $\mathrm{A} = \Gamma (\mathrm{X},\mathcal{O}_{\mathrm{X}})$ dans l'anneau $\Gamma (\mathrm{V},\mathcal{O}_{\mathrm{Y}})$ (1.7.3); on en conclut que $(\psi_{\mathrm{V}})_{*}(\mathcal{O}_{\mathrm{Y}}|\mathrm{V})$ est un $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent (1.6.3), ce qui prouve notre assertion, en raison du caractère local des faisceaux quasi-cohérents. En outre, l'hypothèse que $\psi$ est un homéomorphisme entraîne (0, 3.4.5) que pour tout $y\in \mathrm{Y}$, $\psi_y$ est un isomorphisme $(\psi_{*}(\mathcal{O}_{\mathrm{Y}}))_{\psi (y)}\to \mathcal{O}_y$; comme le diagramme

$$
\begin{array}{c} \mathcal {O} _ {\psi (y)} \xrightarrow {\theta_ {\psi (y)}} (\psi_ {*} (\mathcal {O} _ {\mathrm{Y}})) _ {\psi (y)} \\ \psi_ {y} \circ \alpha_ {\psi (y)} \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow \psi_ {y} \\ (\psi^ {*} (\mathcal {O} _ {\mathrm{X}})) _ {y} \xrightarrow {\theta_ {y} ^ {\#}} \mathcal {O} _ {y} \end{array}
$$

est commutatif et que les deux flèches verticales sont des isomorphismes (0, 3.7.2), l'hypothèse que $\theta_y^\sharp$ est surjectif entraîne qu'il en est de même de $\theta_{\psi(y)}$. Comme le support de $\psi_*(\mathcal{O}_Y)$ est $Z = \psi(Y)$, $\theta$ est un homomorphisme surjectif de $\mathcal{O}_X = \widetilde{\mathbf{A}}$ dans le $\mathcal{O}_X$-Module quasi cohérent $f_*(\mathcal{O}_Y)$. Par suite, il existe un isomorphisme unique $\omega$ d'un faisceau quotient $\widetilde{\mathbf{A}} / \widetilde{\mathfrak{I}}$ ($\mathfrak{I}$ idéal de A) sur $f_*(\mathcal{O}_Y)$ qui, composé avec l'homomorphisme canonique $\widetilde{\mathbf{A}} \to \widetilde{\mathbf{A}} / \widetilde{\mathfrak{I}}$, donne $\theta$ (1.3.8); si $\mathcal{O}_Z$ désigne la restriction de $\widetilde{\mathbf{A}} / \widetilde{\mathfrak{I}}$ à Z, (Z, $\mathcal{O}_Z$) est un sous-préschéma de (X, $\mathcal{O}_X$), et $f$ se factorise en l'injection canonique de ce sous-préschéma dans X, et l'isomorphisme ($\psi_0$, $\omega_0$), où $\psi_0$ est $\psi$ considéré comme application de Y sur Z, et $\omega_0$ la restriction de $\omega$ à $\mathcal{O}_Z$.

Passons au cas général. Soit U un ensemble ouvert affine dans X tel que  $\mathrm{U}\cap\psi(\mathrm{Y})$  soit fermé dans U et non vide. En restreignant f au préschéma induit par Y sur l'ouvert  $\psi^{-1}(\mathrm{U})$, et en le considérant comme un morphisme de ce préschéma dans le préschéma induit par X sur U, on est ramené au premier cas; la restriction de  $f\dot{\alpha}\psi^{-1}(\mathrm{U})$  est donc une immersion fermée  $\psi^{-1}(\mathrm{U})\to\mathrm{U}$, se factorisant canoniquement en  $j_{U}\circ g_{U}$, où  $g_{U}$  est un isomorphisme du préschéma  $\psi^{-1}(\mathrm{U})$  sur un sous-préschéma  $Z_{U}$  de U, et  $j_{U}$  l'injection canonique  $Z_{U}\to U$. Soit V un second ouvert affine de X tel que  $V\subset U$; comme la restriction  $Z_{V}'$  de  $Z_{U}$  à V est un sous-préschéma du préschéma V, la restriction de f à  $\psi^{-1}(\mathrm{V})$  se factorise en  $j_{V}'\circ g_{V}'$, où  $j_{V}'$  est l'injection canonique  $Z_{V}'\to V$  et  $g_{V}'$  un isomorphisme de  $\psi^{-1}(\mathrm{V})$  sur  $Z_{V}'$. Par l'unicité de la factorisation canonique d'une immersion (4.2.1), on a nécessairement  $Z_{V}'=Z_{V}$  et  $g_{V}'=g_{V}$. On en conclut (4.1.5) qu'il y a un sous-préschéma Z de X dont l'espace sous-jacent est  $\psi(\mathrm{Y})$  et dont la restriction à chaque  $U\cap\psi(\mathrm{Y})$  est  $Z_{U}$; les  $g_{U}$  sont alors les restrictions aux  $\psi^{-1}(\mathrm{U})$  d'un isomorphisme  $g:\mathrm{Y}\to\mathrm{Z}$  tel que f=jog, où j est l'injection canonique  $Z\to X$.

Corollaire (4.2.3). — Soit X un schéma affine. Pour qu'un morphisme $f = (\psi, \theta) : Y \to X$ soit une immersion fermée, il faut et il suffit que Y soit un schéma affine et que l'homomorphisme $\Gamma(\psi) : \Gamma(\mathcal{O}_{X}) \to \Gamma(\mathcal{O}_{Y})$ soit surjectif.

Corollaire (4.2.4). — a) Soient $f$ un morphisme $\mathbf{Y}\to\mathbf{X}$, $(\mathbf{V}_{\lambda})$ un recouvrement de $f(\mathbf{Y})$ par des ouverts de $\mathbf{X}$. Pour que $f$ soit une immersion (resp. une immersion ouverte), il faut et il suffit

que sa restriction à chacun des préschémas induits  $f^{-1}(V_{\lambda})$  soit une immersion (resp. une immersion ouverte) dans  $V_{\lambda}$ .

b) Soient $f$ un morphisme $\mathbf{Y}\to\mathbf{X}$, $(\mathbf{V}_{\lambda})$ un recouvrement ouvert de $\mathbf{X}$. Pour que $f$ soit une immersion fermée, il faut et il suffit que sa restriction à chacun des préschémas induits $f^{-1}(\mathbf{V}_{\lambda})$ soit une immersion fermée dans $\mathbf{V}_{\lambda}$.

Soit $f = (\psi, \theta)$; dans le cas $a$, $\theta_y^\#$ est surjectif (resp. bijectif) pour tout $y \in Y$, et dans le cas $b$) $\theta_y^\#$ est surjectif pour tout $y \in Y$; il suffit donc de vérifier que $\psi$, dans le cas $a$), est un homéomorphisme de $Y$ sur une partie localement fermée (resp. ouverte) de $X$, et dans le cas $b$), un homéomorphisme de $Y$ sur une partie fermée de $X$. Or, $\psi$ est évidemment injectif et transforme tout voisinage de $y$ dans $Y$ en un voisinage de $\psi(y)$ dans $\psi(Y)$ pour tout $y \in Y$, en vertu de l'hypothèse; dans le cas $a$), $\psi(Y) \cap V_\lambda$ est localement fermé (resp. ouvert) dans $V_\lambda$, donc $\psi(Y)$ est localement fermé (resp. ouvert) dans la réunion des $V_\lambda$, et a fortiori dans $X$; dans le cas $b$), $\psi(Y) \cap V_\lambda$ est fermé dans $V_\lambda$, donc $\psi(Y)$ est fermé dans $X$ puisque $X = \bigcup_{\lambda} V_\lambda$.

Proposition (4.2.5). — Le composé de deux immersions (resp. de deux immersions ouvertes, de deux immersions fermées) est une immersion (resp. une immersion ouverte, une immersion fermée).

Cela résulte trivialement de (4.1.6).

## 4.3. Produit d'immersions.

Proposition (4.3.1). — Soient $\alpha : \mathrm{X}' \to \mathrm{X}$, $\beta : \mathrm{Y}' \to \mathrm{Y}$ deux S-morphismes; si $\alpha$ et $\beta$ sont des immersions (resp. des immersions ouvertes, des immersions fermées), $\alpha \times_{\mathrm{s}} \beta$ est une immersion (resp. une immersion ouverte, une immersion fermée). En outre, si $\alpha$ (resp. $\beta$) identifie $\mathrm{X}'$ (resp. $\mathrm{Y}'$) à un sous-préschéma $\mathrm{X}''$ (resp. $\mathrm{Y}''$) de $\mathrm{X}$ (resp. $\mathrm{Y}$), $\alpha \times_{\mathrm{s}} \beta$ identifie l'espace sous-jacent à $\mathrm{X}' \times_{\mathrm{s}} \mathrm{Y}'$ au sous-espace $p^{-1}(\mathrm{X}'')\cap q^{-1}(\mathrm{Y}'')$ de l'espace sous-jacent à $\mathrm{X} \times_{\mathrm{s}} \mathrm{Y}$, en désignant par $p$ et $q$ les projections de $\mathrm{X} \times_{\mathrm{s}} \mathrm{Y}$ dans $\mathrm{X}$ et $\mathrm{Y}$ respectivement.

Compte tenu de la déf. (4.2.1), on peut se restreindre au cas où X' et Y' sont des sous-préschémas, α et β les morphismes d'injection. La proposition a déjà été établie pour les sous-préschémas induits sur les ouverts (3.2.7); comme tout sous-préschéma est un sous-préschéma fermé d'un préschéma induit sur un ouvert (4.1.3), on est ramené au cas où X' et Y' sont des sous-préschémas fermés.

Montrons d'abord qu'on peut supposer que S est affine. En effet, soit  $(\mathrm{S}_{\lambda})$  un recouvrement de S formé d'ouverts affines ; si  $\varphi$  et  $\psi$  sont les morphismes structuraux de X et Y, soit  $\mathbf{X}_{\lambda}=\varphi^{-1}(\mathbf{S}_{\lambda}),\mathbf{Y}_{\lambda}=\psi^{-1}(\mathbf{S}_{\lambda})$ . La restriction  $X_{\lambda}^{\prime}$  (resp.  $Y_{\lambda}^{\prime}$ ) de  $X^{\prime}$  (resp.  $Y^{\prime}$ ) à  $X_{\lambda}\cap X^{\prime}$  (resp.  $Y_{\lambda}\cap Y^{\prime}$ ) est un sous-préschéma fermé de  $X_{\lambda}$  (resp.  $Y_{\lambda}$ ), les préschémas  $X_{\lambda}, Y_{\lambda}, X_{\lambda}^{\prime}, Y_{\lambda}^{\prime}$  peuvent être considérés comme des  $S_{\lambda}$ -préschémas et les produits  $X_{\lambda}\times_{s}Y_{\lambda}$  et  $X_{\lambda}\times_{s}Y_{\lambda}$  (resp.  $X_{\lambda}^{\prime}\times_{s}Y_{\lambda}^{\prime}$  et  $X_{\lambda}^{\prime}\times_{s}Y_{\lambda}^{\prime}$ ) sont identiques (3.2.5). Si la proposition est vraie lorsque S est affine, la restriction de  $\alpha\times_{s}\beta$  à chacun des  $X_{\lambda}^{\prime}\times_{s}Y_{\lambda}^{\prime}$  sera donc une immersion (3.2.7). Comme le produit  $X_{\lambda}^{\prime}\times_{s}Y_{\mu}^{\prime}$  (resp.  $X_{\lambda}\times_{s}Y_{\mu}$ ) s'identifie à  $(\mathbf{X}_{\lambda}^{\prime}\cap\mathbf{X}_{\mu}^{\prime})\times_{s}(\mathbf{Y}_{\lambda}^{\prime}\cap\mathbf{Y}_{\mu}^{\prime})$  (resp.  $(\mathbf{X}_{\lambda}\cap\mathbf{X}_{\mu})\times_{s}(\mathbf{Y}_{\lambda}\cap\mathbf{Y}_{\mu})$ ) (3.2.6.4), la restriction de  $\alpha\times_{s}\beta$

à chacun des  $X_{\lambda}^{\prime}\times_{s}Y_{\mu}^{\prime}$  est encore une immersion; il en est par suite de même de  $\alpha\times_{s}\beta$  en vertu de (4.2.4).

En second lieu, prouvons qu'on peut aussi supposer que X et Y sont affines. En effet, soit  $(\mathrm{U}_{i})$  (resp.  $(\mathrm{V}_{j})$ ) un recouvrement de X (resp. Y) par des ouverts affines, et soit  $X_{i}^{\prime}$  (resp.  $Y_{j}^{\prime}$ ) la restriction de  $X^{\prime}$  (resp.  $Y^{\prime}$ ) à  $X^{\prime}\cap U_{i}$  (resp.  $Y^{\prime}\cap V_{j}$ ), qui est un sous-préschéma fermé de  $U_{i}$  (resp.  $V_{j}$ );  $U_{i}\times_{s}V_{j}$  s'identifie à la restriction de  $X\times_{s}Y$  à  $p^{-1}(U_{i})\cap q^{-1}(V_{j})$  (3.2.7); et de même, si  $p^{\prime}, q^{\prime}$  sont les projections de  $X^{\prime}\times_{s}Y^{\prime}, X_{i}^{\prime}\times_{s}Y_{j}^{\prime}$  s'identifie à la restriction de  $X^{\prime}\times_{s}Y^{\prime}$  à  $p^{\prime-1}(X_{i}^{\prime})\cap q^{\prime-1}(Y_{j}^{\prime})$ . Posons  $\gamma=\alpha\times_{s}\beta$ ; on a par définition  $p\circ\gamma=\alpha\circ p^{\prime}, q\circ\gamma=\beta\circ q^{\prime}$ ; comme  $X_{i}^{\prime}=\alpha^{-1}(U_{i}), Y_{j}^{\prime}=\beta^{-1}(V_{j})$ , on a aussi  $p^{\prime-1}(X_{i}^{\prime})=\gamma^{-1}(p^{-1}(U_{i}))$ ,  $q^{\prime-1}(Y_{j}^{\prime})=\gamma^{-1}(q^{-1}(V_{j}))$ , d'où

$$
p ^ {\prime - 1} \left(\mathrm{X} _ {i} ^ {\prime}\right) \cap q ^ {\prime - 1} \left(\mathrm{Y} _ {j} ^ {\prime}\right) = \gamma^ {- 1} \left(p ^ {- 1} \left(\mathrm{U} _ {i}\right) \cap q ^ {- 1} \left(\mathrm{V} _ {j}\right)\right) = \gamma^ {- 1} \left(\mathrm{U} _ {i} \times_ {\mathrm{s}} \mathrm{V} _ {j}\right)
$$

on conclut comme dans la première partie du raisonnement.

Supposons donc X, Y, S affines, et soient B, C, A leurs anneaux respectifs. Alors B et C sont des A-algèbres, X' et Y' des schémas affines dont les anneaux sont des algèbres quotients B', C' de B et C respectivement. En outre, on a $\alpha=(^{a}\rho,\widetilde{\rho})$, $\beta=(^{a}\sigma,\widetilde{\sigma})$, où $\rho$ et $\sigma$ sont respectivement les homomorphismes canoniques B→B', C→C' (1.7.3). Cela étant, on sait que X×sY (resp. X'×sY') est un schéma affine d'anneau B⊗A C (resp. B'⊗A C'), et $\alpha\times_{\mathrm{S}}\beta=(^{a}\tau,\widetilde{\tau})$, où $\tau$ est l'homomorphisme $\rho\otimes\sigma$ de B⊗A C dans B'⊗A C' (3.2.2 et 3.2.3); comme cet homomorphisme est surjectif, $\alpha\times_{\mathrm{S}}\beta$ est bien une immersion. En outre, si b (resp. c) est le noyau de $\rho$ (resp. $\sigma$), le noyau de $\tau$ est $u(b)+v(c)$, où u (resp. v) est l'homomorphisme $b\to b\otimes\mathrm{I}$ (resp. $c\to\mathrm{I}\otimes c$). Comme $p=(^{a}u,\widetilde{u})$ et $q=(^{a}v,\widetilde{v})$, ce noyau correspond, dans le spectre premier de B⊗A C, à l'ensemble fermé $p^{-1}(X')\cap q^{-1}(Y')$ (1.2.2.1 et 1.1.2 (iii)), ce qui achève la démonstration.

Corollaire (4.3.2). — Si f: X→Y est une immersion (resp. une immersion ouverte, une immersion fermée) et un S-morphisme, $f_{(S')}$ est une immersion (resp. une immersion ouverte, une immersion fermée) pour toute extension S'→S du préschéma de base.

## 4.4. Image réciproque d'un sous-préschéma.

Proposition (4.4.1). — Soient $f: \mathrm{X} \to \mathrm{Y}$ un morphisme, $\mathrm{Y}'$ un sous-préschéma (resp. un sous-préschéma fermé, un préschéma induit sur un ouvert) de $\mathrm{Y}$, $j: \mathrm{Y}' \to \mathrm{Y}$ le morphisme d'injection. Alors la projection $p: \mathrm{X} \times_{\mathrm{Y}} \mathrm{Y}' \to \mathrm{X}$ est une immersion (resp. une immersion fermée, une immersion ouverte); le sous-préschéma de $\mathrm{X}$ associé à $p$ a $f^{-1}(\mathrm{Y}')$ pour espace sous-jacent; en outre, si $j'$ est le morphisme d'injection de ce sous-préschéma dans $\mathrm{X}$, pour qu'un morphisme $h: \mathrm{Z} \to \mathrm{X}$ soit tel que $f \circ h: \mathrm{Z} \to \mathrm{Y}$ soit majoré par $j$, il faut et il suffit que $h$ soit majoré par $j'$.

Comme $p = \mathrm{I}_{\mathbf{X}} \times_{\mathbf{Y}} j$ (3.3.4), la première assertion résulte de (4.3.1); la seconde est un cas particulier de (3.5.10) (où il faut échanger les rôles de X et de Y'). Enfin, si on a $foh = joh'$, où $h'$ est un morphisme $Z \to Y'$, il résulte de la définition du produit que l'on a $h = pou$, où $u$ est un morphisme $Z \to X \times_{\mathbf{Y}} Y'$, d'où la dernière assertion.

Nous dirons que le sous-préschéma de X ainsi défini est l'image réciproque du sous-préschéma Y' de Y par le morphisme f, terminologie qui s'accorde avec celle introduite

de façon plus générale dans (3.3.6). Quand nous parlerons de $f^{-1}(\mathbf{Y}')$ comme d'un sous-préschéma de X, c'est toujours de ce sous-préschéma qu'il s'agira.

Lorsque les préschémas $f^{-1}(\mathbf{Y}')$ et $\mathbf{X}$ sont identiques, $j'$ est l'identité et tout morphisme $h: \mathbf{Z} \to \mathbf{X}$ est donc majoré par $j'$, donc le morphisme $f: \mathbf{X} \to \mathbf{Y}$ se factorise alors en $\mathbf{X} \xrightarrow{g} \mathbf{Y}' \xrightarrow{j} \mathbf{Y}$.

Lorsque y est un point fermé de Y et  $\mathrm{Y}^{\prime}=\operatorname{Spec}(\boldsymbol{k}(y))$  le plus petit sous-préschéma fermé de Y ayant  $\{y\}$  comme espace sous-jacent (4.1.9), le sous-préschéma fermé  $f^{-1}(\mathrm{Y}^{\prime})$  est canoniquement isomorphe à la fibre  $f^{-1}(y)$  définie en (3.6.2), à laquelle on l'identifiera.

Corollaire (4.4.2). — Soient $f: \mathrm{X} \to \mathrm{Y}$, $g: \mathrm{Y} \to \mathrm{Z}$ deux morphismes, $h = g\circ f$ leur composé. Pour tout sous-préschéma $\mathbf{Z}'$ de $\mathbf{Z}$, les sous-préschémas $f^{-1}(g^{-1}(\mathbf{Z}'))$ et $h^{-1}(\mathbf{Z}')$ de $\mathbf{X}$ sont identiques.

Cela résulte de l'existence de l'isomorphisme canonique  $\mathbf{X}\times_{\mathbf{Y}}(\mathbf{Y}\times_{\mathbf{Z}}\mathbf{Z}')\simeq\mathbf{X}\times_{\mathbf{Z}}\mathbf{Z}'$  (3.3.9.1).

Corollaire (4.4.3). — Soient X', X'' deux sous-préschémas de X, j': X'→X, j'' : X''→X les morphismes d'injection; alors, j'−1(X'') et j''−1(X') sont tous deux égaux à la borne inférieurs inf (X', X'') de X' et X'' pour la relation d'ordre entre sous-préschémas, et canoniquement isomorphee à X' × xX''.

Cela résulte aussitôt de (4.4.1) et (4.1.10).

Corollaire (4.4.4). — Soient $f: \mathbf{X} \to \mathbf{Y}$ un morphisme, $\mathbf{Y}'$, $\mathbf{Y}''$ deux sous-préschémas de $\mathbf{Y}$; on a $f^{-1}$ ($\inf (\mathbf{Y}', \mathbf{Y}'')$) = $\inf (f^{-1}(\mathbf{Y}')$, $f^{-1}(\mathbf{Y}'')$).

Cela résulte de l'existence de l'isomorphisme canonique entre  $(\mathbf{X}\times_{\mathbf{Y}}\mathbf{Y}')\times_{\mathbf{X}}(\mathbf{X}\times_{\mathbf{Y}}\mathbf{Y}''$  et  $\mathbf{X}\times_{\mathbf{Y}}(\mathbf{Y}'\times_{\mathbf{Y}}\mathbf{Y}''$  (3.3.9.1).

Proposition (4.4.5). — Soient $f: \mathrm{X} \to \mathrm{Y}$ un morphisme, $\mathrm{Y}'$ un sous-préschéma fermé de Y défini par un faisceau quasi-cohérent $\mathcal{K}$ d'idéaux de $\mathcal{O}_{\mathrm{Y}}$ (4.1.3); le sous-préschéma fermé $f^{-1}(\mathrm{Y}')$ de X est alors défini par le faisceau quasi cohérent d'idéaux $f^{*}(\mathcal{K})\mathcal{O}_{\mathrm{X}}$ de $\mathcal{O}_{\mathrm{X}}$.

La question est évidemment locale sur X et Y ; il suffit alors de remarquer que si B est une A-algèbre et R un idéal de B, on a  $\mathrm{A}\otimes_{\mathrm{B}}(\mathrm{B}/\Re)=\mathrm{A}/\Re\mathrm{A}$ , et d'appliquer (1.6.9).

Corollaire (4.4.6). — Soient X' un sous-préschéma fermé de X défini par un faisceau quasi cohérent d'idéaux J de  $O_{X}$ , i l'injection  $X'\to X$ ; pour que la restriction foi de f à  $X'$  soit majorée par l'injection j :  $Y'\to Y$  (autrement dit se factorise en jog, où g est un morphisme  $X'\to Y'$ ), il faut et il suffit que  $f^{*}(\mathcal{K})\mathcal{O}_{\mathrm{X}}\subset\mathcal{J}$ .

Il suffit d'appliquer à $i$ la prop. (4.4.1) en tenant compte de (4.4.5).

## 4.5. Immersions locales et isomorphismes locaux.

Définition (4.5.1). — Soit $f: \mathbf{X} \to \mathbf{Y}$ un morphisme de préschémas. On dit que $f$ est une immersion locale en un point $x \in \mathbf{X}$ s'il existe un voisinage ouvert $\mathbf{U}$ de $x$ dans $\mathbf{X}$ et un voisinage ouvert $\mathbf{V}$ de $f(x)$ dans $\mathbf{Y}$ tels que la restriction de $f$ au préschéma induit $\mathbf{U}$ soit une immersion fermée de $\mathbf{U}$ dans le préschéma induit $\mathbf{V}$. On dit que $f$ est une immersion locale si $f$ est une immersion locale en tout point de $\mathbf{X}$.

Définition (4.5.2). — On dit qu'un morphisme $f: \mathbf{X} \to \mathbf{Y}$ est un isomorphisme local en

un point $x \in \mathbf{X}$ s'il existe un voisinage ouvert U de $x$ dans X tel que la restriction de f au préschéma induit U soit une immersion ouverte de U dans Y. On dit que f est un isomorphisme local si f est un isomorphisme local en tout point de X.

(4.5.3) Une immersion (resp. une immersion fermée) $f: \mathbf{X} \to \mathbf{Y}$ peut donc se caractériser comme une immersion locale telle que $f$ soit un homéomorphisme de l'espace sous-jacent à $\mathbf{X}$ sur une partie (resp. une partie fermée) de $\mathbf{Y}$. Une immersion ouverte $f$ peut se caractériser comme un isomorphisme local injectif.

Proposition (4.5.4). — Soient X un préschéma irréductible, $f: \mathbf{X} \to \mathbf{Y}$ un morphisme injectif dominant. Si f est une immersion locale, f est une immersion et f(X) est ouvert dans Y.

En effet, soit $x \in \mathbf{X}$ et soient $\mathbf{U}$ un voisinage ouvert de $x$, $\mathbf{V}$ un voisinage ouvert de $f(x)$ dans $\mathbf{Y}$ tels que la restriction de $f$ à $\mathbf{U}$ soit une immersion fermée dans $\mathbf{V}$; comme $\mathbf{U}$ est dense dans $\mathbf{X}$, $f(\mathbf{U})$ est dense dans $\mathbf{Y}$ par hypothèse, donc $f(\mathbf{U}) = \mathbf{V}$ et $f$ est un homéomorphisme de $\mathbf{U}$ sur $\mathbf{V}$; l'hypothèse que $f$ est injectif entraîne que $f^{-1}(\mathbf{V}) = \mathbf{U}$, d'où aussitôt la proposition.

Proposition (4.5.5). — (i) Le composé de deux immersions locales (resp. de deux isomorphismes locaux) est une immersion locale (resp. un isomorphisme local).

(ii) Soient $f: \mathbf{X} \to \mathbf{X}'$, $g: \mathbf{Y} \to \mathbf{Y}'$ deux S-morphismes. Si f et g sont des immersions locales (resp. des isomorphismes locaux), il en est de même de $f \times_{8} g$.

(iii) Si un S-morphisme $f$ est une immersion locale (resp. un isomorphisme local), il en est de même de $f_{(S')}$ pour toute extension $S' \to S$ du préschéma de base.

D'après (3.5.1), il suffit de prouver (i) et (ii).

(i) résulte aussitôt de la transitivité des immersions fermées (resp. ouvertes) (4.2.4) et du fait que si $f$ est un homéomorphisme de $\mathbf{X}$ sur une partie fermée de $\mathbf{Y}$, pour tout ouvert $\mathbf{U} \subset \mathbf{X}$, $f(\mathbf{U})$ est ouvert dans $f(\mathbf{X})$, donc il existe une partie ouverte $\mathbf{V}$ de $\mathbf{Y}$ telle que $f(\mathbf{U}) = \mathbf{V} \cap f(\mathbf{X})$, et $f(\mathbf{U})$ est par suite fermé dans $\mathbf{V}$.

Pour démontrer (ii), soient $p, q$ les projections de $\mathbf{X} \times_{\mathbb{S}} \mathbf{Y}$, $p', q'$ celles de $\mathbf{X}' \times_{\mathbb{S}} \mathbf{Y}'$. Il existe par hypothèse des voisinages ouverts $\mathbf{U}, \mathbf{U}', \mathbf{V}, \mathbf{V}'$ de $x = p(z), x' = p'(z'), y = q(z), y' = q'(z')$ respectivement, tels que les restrictions de $f$ et $g$ à $\mathbf{U}$ et $\mathbf{V}$ respectivement soient des immersions fermées (resp. ouvertes) dans $\mathbf{U}'$ et $\mathbf{V}'$ respectivement. Comme l'espace sous-jacent de $\mathbf{U} \times_{\mathbb{S}} \mathbf{V}$ et celui de $\mathbf{U}' \times_{\mathbb{S}} \mathbf{V}'$ s'identifient aux voisinages ouverts $p^{-1}(\mathbf{U}) \cap q^{-1}(\mathbf{V})$ et $p'^{-1}(\mathbf{U}') \cap q'^{-1}(\mathbf{V}')$ de $z$ et $z'$ respectivement (3.2.7), la proposition résulte de (4.3.1).

## § 5. PRÉSCHÉMAS RÉDUITS; CONDITION DE SÉPARATION

## 5.1. Préschémas réduits.

Proposition (5.1.1). — Soient (X, $\mathcal{O}_{\mathrm{X}}$) un préschéma, $\mathcal{B}$ une $\mathcal{O}_{\mathrm{X}}$-Algèbre quasi-cohérente. Il existe un $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent et un seul $\mathcal{N}$ dont la fibre $\mathcal{N}_{x}$ en tout $x \in \mathrm{X}$ soit le nilradical de l'anneau $\mathcal{B}_{x}$. Lorsque X est affine, et par suite $\mathcal{B} = \widetilde{\mathrm{B}}$, où B est une algèbre sur A(X), on a $\mathcal{N} = \widetilde{\mathfrak{N}}$, où $\mathfrak{N}$ est le nilradical de B.

La question étant locale, on est ramené à démontrer la dernière assertion. On sait que $\widetilde{\mathfrak{N}}$ est un $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent (1.4.1) et que sa fibre au point $x \in \mathrm{X}$ est l'idéal $\mathfrak{N}_x$ de l'anneau de fractions $\mathrm{B}_x$; tout revient à prouver que le nilradical de $\mathrm{B}_x$ est contenu dans $\mathfrak{N}_x$, l'inclusion opposée étant évidente. Or, soit $z/s$ un élément du nilradical de $\mathrm{B}_x$, avec $z \in \mathrm{B}$, $s \notin \mathrm{j}_x$; par hypothèse, il existe un entier $k$ tel que $(z/s)^k = 0$, ce qui signifie qu'il existe $t \notin \mathrm{j}_x$ tel que $tz^k = 0$. On en conclut $(tz)^k = 0$, et par suite $z/s = (tz)/(ts)$ appartient à $\mathfrak{N}_x$.

Nous dirons que le $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent $\mathcal{N}$ ainsi défini est le Nilradical de la $\mathcal{O}_{\mathrm{X}}$-Algèbre $\mathcal{B}$; nous noterons en particulier $\mathcal{N}_{\mathrm{X}}$ le nilradical de $\mathcal{O}_{\mathrm{X}}$.

Corollaire (5.1.2). — Soit X un préschéma; le sous-préschéma fermé de X défini par le faisceau d'idéaux  $N_{X}$  est le seul sous-préschéma réduit (0, 4.1.4) de X ayant X pour espace sous-jacent; c'est aussi le plus petit sous-préschéma de X ayant X pour espace sous-jacent.

Comme le faisceau structural du sous-préschéma fermé défini Y par $\mathcal{N}_{\mathrm{X}}$ est $\mathcal{O}_{\mathrm{X}} / \mathcal{N}_{\mathrm{X}}$, il est immédiat que Y est réduit et a X pour espace sous-jacent, puisque $\mathcal{N}_{x} \neq \mathcal{O}_{x}$ pour tout $x \in \mathrm{X}$. Pour démontrer les autres assertions, remarquons qu'un sous-préschéma Z de X ayant X pour espace sous-jacent est défini par un faisceau d'idéaux $\mathcal{J}(4.1.3)$ tel que $\mathcal{J}_{x} \neq \mathcal{O}_{x}$ pour tout $x \in \mathrm{X}$. On peut se borner au cas où X est affine, soit $\mathrm{X} = \operatorname{Spec}(\mathrm{A})$ et $\mathcal{J} = \widetilde{\mathfrak{J}}$, où $\mathfrak{J}$ est un idéal de A; alors, pour tout $x \in \mathrm{X}$, on a $\mathfrak{J}_{x} \subset \mathrm{j}_{x}$, donc $\mathfrak{J}$ est contenu dans tous les idéaux premiers de A, c'est-à-dire dans leur intersection $\mathfrak{N}$, nilradical de A. Cela prouve que Y est le plus petit sous-préschéma de X ayant X comme espace sous-jacent (4.1.9); en outre, si Z est distinct de Y, on a nécessairement $\mathcal{J}_{x} \neq \mathcal{N}_{x}$ pour un $x \in \mathrm{X}$ au moins, et par suite (5.1.1) Z n'est pas réduit.

Définition (5.1.3). — On appelle préschéma réduit associé à un préschéma X et on note  $X_{red}$  l'unique sous-préschéma réduit de X ayant X pour espace sous-jacent.

Dire qu'un préschéma X est réduit signifie donc que  $X=X_{red}$ .

Proposition (5.1.4). — Pour que le spectre premier d'un anneau A soit un préschéma réduit (resp. intègre) (2.1.7), il faut et il suffit que A soit un anneau réduit (resp. intègre).

En effet, il résulte aussitôt de (5.1.1) que la condition $\mathcal{N}=(0)$ est nécessaire et suffisante pour que $X=\text{Spec}(A)$ soit réduit ; l'assertion relative aux anneaux intègres est alors une conséquence de (1.1.13).

Comme tout anneau de fractions $\neq\{0\}$ d'un anneau intègre est intègre, il résulte de (5.1.4) que pour tout préschéma localement intègre X, $\mathcal{O}_{x}$ est un anneau intègre pour tout $x\in\mathbf{X}$. La réciproque est vraie lorsque l'espace sous-jacent à X est localement noethérien : en effet X est alors réduit, et si U est un ouvert affine de X, qui soit un espace noethérien, U n'a qu'un nombre fini de composantes irréductibles, donc son anneau A n'a qu'un nombre fini d'idéaux premiers minimaux (1.1.14). Si deux de ces composantes $\mathbf{U}_{i}$ avaient un point commun $x$, $\mathcal{O}_{x}$ aurait au moins deux idéaux premiers minimaux distincts, donc ne serait pas intègre ; les $\mathbf{U}_{i}$ sont par suite des ouverts deux à deux disjoints, et chacun d'eux est donc intègre.

(5.1.5) Soit  $f=(\psi,\theta)$  : X→Y un morphisme de préschémas; l'homomor-

phisme $\theta_{x}^{\sharp}:\mathcal{O}_{\psi (x)}\to \mathcal{O}_{x}$ applique tout élément nilpotent de $\mathcal{O}_{\psi (x)}$ sur un élément nilpotent de $\mathcal{O}_x$ ; par passage aux quotients, on déduit donc de $\theta^{\sharp}$ un homomorphisme

$$
\omega : \psi^ {*} (\mathcal {O} _ {\mathrm{Y}} / \mathcal {N} _ {\mathrm{Y}}) \rightarrow \mathcal {O} _ {\mathrm{X}} / \mathcal {N} _ {\mathrm{X}}
$$

il est clair que pour tout $x\in\mathbf{X}$, $\omega_{x}:\mathcal{O}_{\psi(x)}/\mathcal{N}_{\psi(x)}\to\mathcal{O}_{x}/\mathcal{N}_{x}$ est un homomorphisme local, donc $(\psi,\omega^{b})$ est un morphisme de préschémas $\mathbf{X}_{\mathrm{red}}\to\mathbf{Y}_{\mathrm{red}}$, que nous noterons $f_{\mathrm{red}}$ et appellerons le morphisme réduit associé à $f$. Il est immédiat que pour deux morphismes $f:\mathbf{X}\to\mathbf{Y},g:\mathbf{Y}\to\mathbf{Z}$, on a $(g\circ f)_{\mathrm{red}}=g_{\mathrm{red}}\circ f_{\mathrm{red}}$, donc on a défini $\mathbf{X}_{\mathrm{red}}$ comme foncteur covariant en $\mathbf{X}$.

La définition précédente montre que le diagramme

$$
\begin{array}{c} \mathbf {X} _ {\mathrm{red}} \xrightarrow {t _ {\mathrm{red}}} \mathbf {Y} _ {\mathrm{red}} \\ \downarrow \qquad \qquad \qquad \downarrow \\ \mathbf {X} \xrightarrow [ t ]{} \mathbf {Y} \end{array}
$$

est commutatif, les flèches verticales étant les morphismes d'injection ; en d'autres termes,  $X_{red} \rightarrow X$  est un morphisme fonctoriel. On notera en particulier que si X est réduit, tout morphisme  $f: X \rightarrow Y$  se factorise en  $X \stackrel{f_{red}}{\rightarrow} Y_{red} \rightarrow Y$ ; en d'autres termes, f est majoré par le morphisme d'injection  $Y_{red} \rightarrow Y$ .

Proposition (5.1.6). — Soit $f: \mathrm{X} \to \mathrm{Y}$ un morphisme; si $f$ est surjectif (resp. radiciel, une immersion, une immersion fermée, une immersion ouverte, une immersion locale, un isomorphisme local), il en est de même de $f_{\text{red}}$. Inversement, si $f_{\text{red}}$ est surjectif (resp. radiciel), il en est de même de $f$.

La proposition est triviale si $f$ est surjectif; si $f$ est radiciel, elle résulte de ce que pour tout $x \in \mathbf{X}$, le corps $\boldsymbol{k}(x)$ est le même pour les préschémas $\mathbf{X}$ et $\mathbf{X}_{\mathrm{red}}$ (3.5.8). Enfin, si $f = (\psi, \theta)$ est une immersion, une immersion fermée ou une immersion locale (resp. une immersion ouverte, ou un isomorphisme local), la proposition résulte de ce que si $\theta_x^\sharp$ est surjectif (resp. bijectif), il en est de même de l'homomorphisme obtenu en passant aux quotients par les nilradicaux de $\mathcal{O}_{\psi(x)}$ et $\mathcal{O}_x$ (5.1.2 et 4.2.2) (cf. (5.5.12)).

Proposition (5.1.7). — Si X, Y sont deux S-préschémas, les préschémas  $X_{red} \times_{S_{red}} Y_{red}$  et  $X_{red} \times_{S} Y_{red}$  sont identiques, et s'identifient canoniquement à un sous-préschéma de  $X \times_{S} Y$  ayant même espace sous-jacent que ce produit.

L'identification canonique de  $X_{red} \times_{S} Y_{red}$  à un sous-préschéma de  $X \times_{S} Y$  ayant même espace sous-jacent résulte de (4.3.1). D'autre part, si  $\varphi$  et  $\psi$  sont les morphismes structuraux  $X_{red} \rightarrow S$ ,  $Y_{red} \rightarrow S$ , ils se factorisent par  $S_{red}$  (5.1.5), et comme  $S_{red} \rightarrow S$  est un monomorphisme, la première assertion résulte de (3.2.4).

Corollaire (5.1.8). — Les préschémas  $(\mathbf{X} \times_{\mathrm{S}} \mathbf{Y})_{\mathrm{red}}$  et  $(\mathbf{X}_{\mathrm{red}} \times_{\mathrm{S}_{\mathrm{red}}} \mathbf{Y}_{\mathrm{red}})_{\mathrm{red}}$  s'identifient canoniquement.

Cela résulte de (5.1.2) et (5.1.7).

On notera que si X et Y sont des préschémas réduits, il n'en est pas nécessairement de même de  $X \times_{s} Y$ , car le produit tensoriel de deux algèbres réduites peut avoir des éléments nilpotents.

Proposition (5.1.9). — Soient X un préschéma, J un faisceau quasi-cohérent d'idéaux de  $O_{X}$  tel que  $J^{n}=0$  pour un entier n>0. Soit  $X_{0}$  le sous-préschéma fermé  $(\mathbf{X},\mathcal{O}_{\mathbf{X}}/\mathcal{J})$  de X; pour que X soit un schéma affine, il faut et il suffit que  $X_{0}$  le soit.

La condition étant évidemment nécessaire, prouvons qu'elle est suffisante. Si on pose  $\mathbf{X}_{k}=(\mathbf{X},\mathcal{O}_{\mathbf{X}}/\mathcal{J}^{k+1})$ , tout revient à prouver par récurrence sur k que les  $X_{k}$  sont affines, donc on est ramené au cas où  $J^{2}=0$ . Posons

$$
\mathrm{A} = \Gamma (\mathrm{X}, \mathcal {O} _ {\mathrm{X}}), \quad \mathrm{A} _ {0} = \Gamma (\mathrm{X} _ {0}, \mathcal {O} _ {\mathrm{X} _ {0}}) = \Gamma (\mathrm{X}, \mathcal {O} _ {\mathrm{X}} / \mathcal {J})
$$

On déduit de l'homomorphisme canonique $\mathcal{O}_{\mathrm{X}}\to\mathcal{O}_{\mathrm{X}}/\mathcal{J}$ un homomorphisme d'anneaux $\varphi:\mathrm{A}\to\mathrm{A}_{0}$. Nous verrons ci-dessous que $\varphi$ est surjectif, de sorte que la suite

$$
\mathrm{o} \rightarrow \Gamma (\mathbf {X}, \mathcal {J}) \rightarrow \Gamma (\mathbf {X}, \mathcal {O} _ {\mathrm{X}}) \rightarrow \Gamma (\mathbf {X}, \mathcal {O} _ {\mathrm{X}} / \mathcal {J}) \rightarrow \mathrm{o}\tag{5.1.9.1}
$$

est exacte. Supposons ce point établi, et montrons que cela entraîne la proposition. Notons que $\Re=\Gamma(X,\mathcal{J})$ est un idéal de carré nul dans A, et est donc un module sur $A_{0}=A/\Re$. Par hypothèse, on a $X_{0}=\operatorname{Spec}(A_{0})$, et comme les espaces topologiques sous-jacents $X_{0}$ et X sont identiques, $\Re=\Gamma(X_{0},\mathcal{J})$; par ailleurs, comme $\mathcal{J}^{2}=0$, $\mathcal{J}$ est un $(\mathcal{O}_{X}/\mathcal{J})$-Module quasi-cohérent, donc on a $\mathcal{J}\cong\widetilde{\Re}$ et $\Re_{x}=\mathcal{J}_{x}$ pour tout $x\in X_{0}$ (1.4.1). Cela étant, soit $X^{\prime}=\operatorname{Spec}(A)$, et considérons le morphisme $f=(\psi,\theta):\mathbf{X}\to\mathbf{X}^{\prime}$ de préschémas correspondant à l'application identique $A\to\Gamma(X,\mathcal{O}_{X})$ (2.2.4). Pour tout ouvert affine V dans X, le diagramme

$$
\begin{array}{c} \mathrm {A\to\Gamma(V, \mathcal {O} _ {X} |V)} \\ \downarrow \qquad \qquad \qquad \downarrow \\ \mathrm {A_ {0} = A/ \mathfrak {R} \to\Gamma(V, \mathcal {O} _ {X_ {0}} |V)} \end{array}
$$

est commutatif, d'où on conclut que le diagramme

$$
\begin{array}{c} \mathbf {X} ^ {\prime} \stackrel {{f}} {{\leftarrow}} \mathbf {X} \\ j ^ {\prime} \Bigg | \quad \Bigg | _ {j} \\ \mathbf {X} _ {0} ^ {\prime} \stackrel {{f _ {0}}} {{\leftarrow}} \mathbf {X} _ {0} \end{array}
$$

est commutatif, $\mathbf{X}_0'$ étant le sous-préschéma fermé de $\mathbf{X}'$ défini par le faisceau quasi-cohérent d'idéaux $\widetilde{\mathfrak{R}}$, $j$, $j'$ les morphismes d'injection canoniques. Mais puisque $\mathbf{X}_0$ est affine, $f_0$ est un isomorphisme et comme les applications continues sous-jacentes à $j$ et $j'$ sont les applications identiques, on voit tout d'abord que $\psi : \mathbf{X} \to \mathbf{X}'$ est un homéomorphisme. En outre, la relation $\mathfrak{R}_x = \mathcal{J}_x$ montre que la restriction de $\theta^\sharp : \psi^*(\mathcal{O}_{\mathbf{X}'}) \to \mathcal{O}_\mathbf{X}$ est un isomorphisme de $\psi^*(\widetilde{\mathfrak{R}})$ sur $\mathcal{J}$; d'autre part, par passage aux quotients, $\theta^\sharp$ donne un isomorphisme $\psi^*(\mathcal{O}_{\mathbf{X}'} / \widetilde{\mathfrak{R}}) \to \mathcal{O}_\mathbf{X} / \mathcal{J}$, puisque $f_0$ est un isomorphisme; on en conclut aussitôt par le lemme des 5 (M, I, i. i) que $\theta^\sharp$ est lui-même un isomorphisme, donc que $f$ est un isomorphisme, et par suite que X est affine.

Tout revient donc à démontrer l'exactitude de (5.1.9.1), ce qui résultera de

$H^{1}(X, \mathcal{J}) = 0.$ Or, $H^{1}(X, \mathcal{J}) = H^{1}(X_{0}, \mathcal{J})$ et nous avons vu que $\mathcal{J}$ est un $O_{X_{0}}$-Module quasi-cohérent. Notre assertion résultera donc du

Lemme (5.1.9.2). — Si Y est un schéma affine et F un  $O_{Y}$ -Module quasi-cohérent, on a  $H^{1}(Y, \mathcal{F}) = 0$ .

Ce lemme sera démontré au chap. III, § 1, comme conséquence du théorème plus général que $\mathrm{H}^i (\mathrm{Y},\mathcal{F}) = 0$ pour tout $i > 0$. Pour en donner une démonstration indépendante, observons que $\mathrm{H}^1 (\mathrm{Y},\mathcal{F})$ s'identifie au module $\operatorname {Ext}_{\mathcal{O}_Y}^{1}(\mathrm{Y};\mathcal{O}_Y,\mathcal{F})$ des classes d'extensions du $\mathcal{O}_Y$-Module $\mathcal{O}_Y$ par le $\mathcal{O}_Y$-Module $\mathcal{F}$ (T, 4.2.3); tout revient donc à prouver qu'une telle extension $\mathcal{G}$ est triviale. Or, pour tout $y\in \mathrm{Y}$, il y a un voisinage V de $y$ dans Y tel que $\mathcal{G}|\mathrm{V}$ soit isomorphe à $\mathcal{F}|\mathrm{Y}\oplus \mathcal{O}_Y|\mathrm{V}$ (0, 5.4.9); on en conclut que $\mathcal{G}$ est un $\mathcal{O}_Y$-Module quasi-cohérent. Si A est l'anneau de Y, on a donc $\mathcal{F} = \widetilde{\mathbf{M}}$, $\mathcal{G} = \widetilde{\mathbf{N}}$, où M et N sont des A-modules, et par hypothèse N est une extension du A-module A par le A-module M (1.3.11). Comme cette extension est nécessairement triviale, le lemme est démontré, et par suite aussi (5.1.9).

Corollaire (5.1.10). — Soit X un préschéma tel que  $N_{X}$  soit nilpotent. Pour que X soit un schéma affine, il faut et il suffit que  $X_{red}$  le soit.

## 5.2. Existence d'un sous-préschéma d'espace sous-jacent donné.

Proposition (5.2.1). — Pour tout sous-espace localement fermé Y de l'espace sous-jacent à un préschéma X, il existe un sous-préschéma réduit et un seul de X ayant Y pour espace sous-jacent.

L'unicité résultant de (5.1.2), il reste à prouver l'existence du sous-préschéma en question.

Si X est affine d'anneau A, et Y fermé dans X, la proposition est immédiate : j(Y) est le plus grand idéal a⊂A tel que V(a)=Y, et il est égal à sa racine (1.1.4 (i)), donc A/j(Y) est un anneau réduit.

Dans le cas général, pour tout ouvert affine U ⊂ X tel que U ∩ Y soit fermé dans U, considérons le sous-préschéma fermé Y$_{U}$ de U défini par le faisceau d'idéaux associé à l'idéal j(U ∩ Y) de A(U), qui est réduit. Montrons que, si V est un ouvert affine de X contenu dans U, Y$_{V}$ est induit par Y$_{U}$ sur V ∩ Y ; or, ce préschéma induit est un sous-préschéma fermé de V qui est réduit et a V ∩ Y comme espace sous-jacent ; l'unicité de Y$_{V}$ entraîne donc notre assertion.

Proposition (5.2.2). — Soient X un préschéma réduit, $f: \mathrm{X} \to \mathrm{Y}$ un morphisme, Z un sous-préschéma fermé de Y tel que $f(\mathrm{X}) \subset \mathrm{Z}$; alors f se factorise en $\mathrm{X} \xrightarrow{g} \mathrm{Z} \xrightarrow{j} \mathrm{Y}$, où j est le morphisme d'injection.

Il résulte de l'hypothèse que le sous-préschéma fermé $f^{-1}(\mathbf{Z})$ de $\mathbf{X}$ a pour espace sous-jacent $\mathbf{X}$ tout entier (4.4.1); comme $\mathbf{X}$ est réduit, ce sous-préschéma fermé coïncide avec $\mathbf{X}$ (5.1.2), et la proposition résulte donc de (4.4.1).

Corollaire (5.2.3). — Soit X un sous-préschéma réduit d'un préschéma Y ; si Z est le sous-préschéma fermé réduit de Y ayant pour espace sous-jacent  $\overline{X}$ , X est un sous-préschéma induit sur un ouvert de Z.

Il y a en effet un ouvert U de Y tel que  $X = U \cap \bar{X}$ ; comme X est un sous-préschéma réduit de Z en vertu de (5.2.2), le sous-préschéma X est induit par Z sur le sous-espace ouvert X en vertu de l'unicité (5.2.1).

Corollaire (5.2.4). — Soient $f: \mathbf{X} \to \mathbf{Y}$ un morphisme, $\mathbf{X}'$ (resp. $\mathbf{Y}'$) un sous-préschéma fermé de $\mathbf{X}$ (resp. $\mathbf{Y}$) défini par un faisceau d'idéaux quasi-cohérent $\mathcal{J}$ (resp. $\mathcal{K}$) de $\mathcal{O}_{\mathbf{X}}$ (resp. $\mathcal{O}_{\mathbf{Y}}$). Supposons que $\mathbf{X}'$ soit réduit et que $f(\mathbf{X}') \subset \mathbf{Y}'$. Alors on a $f^{*}(\mathcal{K})\mathcal{O}_{\mathbf{X}} \subset \mathcal{J}$.

Comme la restriction de $f$ à $\mathbf{X}'$ se factorise en $\mathbf{X}'\to\mathbf{Y}'\to\mathbf{Y}$ d'après (5.2.2), il suffit d'appliquer (4.4.6).

## 5.3. Diagonale ; graphe d'un morphisme.

(5.3.1) Soit X un S-préschéma ; on appelle morphisme diagonal de X dans  $X \times_{s} X$ , et on note  $\Delta_{X|S}$ , ou  $\Delta_{X}$ , ou même  $\Delta$  si aucune confusion n'est possible, le S-morphisme  $(\mathrm{I}_{\mathrm{X}}, \mathrm{I}_{\mathrm{X}})_{\mathrm{S}}$ , autrement dit, l'unique S-morphisme  $\Delta_{X}$  tel que

$$
p _ {1} \circ \Delta_ {\mathrm{X}} = p _ {2} \circ \Delta_ {\mathrm{X}} = \mathrm{I} _ {\mathrm{X}}\tag{5.3.1.1}
$$

en désignant par $p_{1}, p_{2}$ les projections de $\mathbf{X} \times_{\mathbb{S}} \mathbf{X}$ (déf. (3.2.1)). Si $f: \mathrm{T} \to \mathrm{X}$, $g: \mathrm{T} \to \mathrm{Y}$ sont deux S-morphismes, on vérifie aussitôt que

$$
(f, g) _ {\mathrm{S}} = (f \times_ {\mathrm{S}} g) \circ \Delta_ {\mathrm{T} | \mathrm{S}}\tag{5.3.1.2}
$$

Le lecteur observera que la définition précédente et les résultats énoncés dans les  $n^{os}$  (5.3.1) à (5.3.8) sont valables dans toute catégorie, pourvu que les produits qui y figurent existent dans cette catégorie.

Proposition (5.3.2). — Soient X, Y deux S-préschémas; si on identifie canoniquement le produit  $(\mathbf{X} \times \mathbf{Y}) \times (\mathbf{X} \times \mathbf{Y})$  à  $(\mathbf{X} \times \mathbf{X}) \times (\mathbf{Y} \times \mathbf{Y})$ , le morphisme  $\Delta_{X \times Y}$  s'identifie à  $\Delta_{X} \times \Delta_{Y}$ .

En effet, si $p_1$, $q_1$ sont les premières projections $X \times X \to X$, $Y \times Y \to Y$, la première projection $(X \times Y) \times (X \times Y) \to X \times Y$ s'identifie à $p_1 \times q_1$, et l'on a

$$
(p _ {1} \times q _ {1}) ^ {\circ} (\Delta_ {\mathrm{X}} \times \Delta_ {\mathrm{Y}}) = (p _ {1} ^ {\circ} \Delta_ {\mathrm{X}}) \times (q _ {1} ^ {\circ} \Delta_ {\mathrm{Y}}) = \mathrm{I} _ {\mathrm{X} \times \mathrm{Y}}
$$

même raisonnement pour les secondes projections.

Corollaire (5.3.4). — Pour toute extension S'→S du préschéma de base, ΔX(s') s'identifie canoniquement à (ΔX)(S').

Il suffit de remarquer que $(\mathbf{X} \times_{\mathbb{S}} \mathbf{X})_{(\mathbb{S}')}$ s'identifie canoniquement à $\mathbf{X}_{(\mathbb{S}')} \times_{\mathbb{S}'} \mathbf{X}_{(\mathbb{S}')}$ (3.3.10).

Proposition (5.3.5). — Soient X, Y deux S-préschémas, $\varphi: S \to T$ un morphisme, faisant de tout S-préschéma un T-préschéma. Soient $f: X \to S$, $Y \to S$ les morphismes structuraux, $p, q$ les projections de $X \times_{S} Y$, $\pi = f \circ p = g \circ q$ le morphisme structural $X \times_{S} Y \to S$. Alors, le diagramme

$$
\begin{array}{c} \mathbf {X} \times_ {\mathrm{S}} \mathbf {Y} \xrightarrow {(p , q) _ {\mathrm{T}}} \mathbf {X} \times_ {\mathrm{T}} \mathbf {Y} \\ \pi \Biggl \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \mathbf {S} \xrightarrow [ \Delta_ {\mathrm{S} | _ {\mathrm{T}}} ]{} \mathbf {S} \times_ {\mathrm{T}} \mathbf {S} \end{array}\tag{5.3.5.1}
$$

est commutatif, et identifie  $X \times_{S} Y$  au produit des  $(S \times_{T} S)$ -préschémas S et  $X \times_{T} Y$ , les projections s'identifiant à  $\pi$  et  $(p, q)_{T}$ .

En vertu de (3.4.3), on est ramené à démontrer la proposition correspondante dans la catégorie des ensembles, en remplaçant X, Y, S par  $\mathrm{X}(\mathrm{Z})_{\mathrm{T}}$ ,  $\mathrm{Y}(\mathrm{Z})_{\mathrm{T}}$ ,  $\mathrm{S}(\mathrm{Z})_{\mathrm{T}}$ , Z étant un T-préschéma arbitraire. Mais pour la catégorie des ensembles, la vérification est immédiate et laissée au lecteur.

Corollaire (5.3.6). — Le morphisme $(p,q)_{\mathrm{T}}s^{\prime}$ identifie (en posant $\mathbf{P} = \mathbf{S}\times_{\mathrm{T}}\mathbf{S}$) à $\mathrm{I}_{\mathrm{X}\times_{\mathrm{T}}\mathrm{Y}}\times_{\mathrm{P}}\Delta_{\mathrm{S}}$

Cela résulte de (5.3.5) et (3.3.4).

Corollaire (5.3.7). — Si $f: \mathbf{X} \to \mathbf{Y}$ est un S-morphisme, le diagramme

![](images/page_131_image_5.jpg)

est commutatif, et identifie X au produit des  $(\mathbf{Y} \times_{\mathrm{s}} \mathbf{Y})$ -préschémas Y et  $X \times_{s} Y$ .

Il suffit d'appliquer (5.3.5) en remplaçant S par Y et T par S, et remarquant que  $X \times_{Y} Y = X$  (3.3.3).

Proposition (5.3.8). — Pour que $f: \mathbf{X} \to \mathbf{Y}$ soit un monomorphisme de préschémas, il faut et il suffit que $\Delta_{\mathbf{X}|\mathbf{Y}}$ soit un isomorphisme de $\mathbf{X}$ sur $\mathbf{X} \times_{\mathbf{Y}} \mathbf{X}$.

En effet, dire que $f$ est un monomorphisme signifie que pour tout Y-préschéma Z, l'application correspondante $f': \mathbf{X}(\mathbf{Z})_{\mathbf{Y}} \to \mathbf{Y}(\mathbf{Z})_{\mathbf{Y}}$ est une injection, et comme $\mathbf{Y}(\mathbf{Z})_{\mathbf{Y}}$ est réduit à un élément, cela signifie qu'il en est de même de $\mathbf{X}(\mathbf{Z})_{\mathbf{Y}}$. Mais cela s'exprime aussi en disant que $\mathbf{X}(\mathbf{Z})_{\mathbf{Y}} \times \mathbf{X}(\mathbf{Z})_{\mathbf{Y}}$ est canoniquement isomorphe à $\mathbf{X}(\mathbf{Z})_{\mathbf{Y}}$, et le premier de ces ensembles étant $(\mathbf{X} \times_{\mathbf{Y}} \mathbf{X})(\mathbf{Z})_{\mathbf{Y}}$ (3.4.3.1), cela signifie que $\Delta_{\mathbf{X}|Y}$ est un isomorphisme.

Proposition (5.3.9). — Le morphisme diagonal $\Delta_{\mathrm{X}}$ est une immersion de X dans $\mathbf{X} \times_{\mathrm{s}} \mathbf{X}$.

En effet, comme les applications continues $p_1$ et $\Delta_X$ des espaces sous-jacents sont telles que $p_1 \circ \Delta_X$ soit l'identité, $\Delta_X$ est un homéomorphisme de X sur $\Delta_X(X)$. De même, l'homomorphisme composé $\mathcal{O}_x \to \mathcal{O}_{\Delta_X(x)} \to \mathcal{O}_x$ des homomorphismes correspondant à $p_1$ et à $\Delta_X$ étant l'identité, l'homomorphisme correspondant à $\Delta_X$ est surjectif; la proposition résulte donc de (4.2.2).

On dit que le sous-préschéma de  $X \times_{s} X$  associé à l'immersion  $\Delta_{X}$  (4.2.1) est la diagonale de  $X \times_{s} X$ .

Corollaire (5.3.10). — Sous les hypothèses de (5.3.5),  $(p, q)_{\mathrm{T}}$  est une immersion.

Cela résulte de (5.3.6) et de (4.3.1).

On dit (sous les hypothèses de (5.3.5)) que $(p, q)_{\mathrm{T}}$ est l'immersion canonique de $\mathbf{X} \times_{\mathrm{s}} \mathbf{Y}$ dans $\mathbf{X} \times_{\mathrm{T}} \mathbf{Y}$.

Corollaire (5.3.11). — Soient X, Y deux S-préschémas, $f: \mathbf{X} \to \mathbf{Y}$ un S-morphisme; alors le morphisme graphe $\Gamma_f = (\mathrm{I}_{\mathrm{X}}, f)_\mathrm{S}$ de $f$ (3.3.14) est une immersion de X dans $\mathbf{X} \times_{\mathrm{S}} \mathbf{Y}$.

C'est le cas particulier du cor. (5.3.10) où l'on remplace S par Y et T par S (cf. (5.3.7)).

Le sous-préschéma de  $X \times_{s} Y$  associé à l'immersion  $\Gamma_{f}(4.2.1)$  est appelé le graphe du morphisme f; les sous-préschémas de  $X \times_{s} Y$  qui sont des graphes de morphismes  $X \to Y$  se caractérisent par le fait que la restriction à un tel sous-préschéma G de la projection  $p_{1}: X \times_{s} Y \to X$  est un isomorphisme g de G sur X: G est alors le graphe du morphisme  $p_{2} \circ g^{-1}$ , où  $p_{2}$  est la projection  $X \times_{s} Y \to Y$ .

Lorsqu'on prend en particulier X=S, les S-morphismes  $S \rightarrow Y$ , qui ne sont autres que les S-sections de Y (2.5.5) sont égaux à leurs morphismes graphes ; les sous-préschémas de Y qui sont des graphes de S-sections (autrement dit, ceux qui sont isomorphes à S par la restriction du morphisme structural  $Y \rightarrow S$ ) s'appellent encore les images de ces sections, ou, par abus de langage, les S-sections de Y.

Corollaire (5.3.12). — Les hypothèses et notations étant celles de (5.3.11), pour tout morphisme $g: S' \to S$, soit $f'$ l'image réciproque de $f$ par $g$ (3.3.7); alors $\Gamma_{f'}$ est l'image réciproque de $\Gamma_f$ par $g$.

C'est un cas particulier de la formule (3.3.10.1).

Corollaire (5.3.13). — Soient $f: \mathrm{X} \to \mathrm{Y}$, $g: \mathrm{Y} \to \mathrm{Z}$ deux morphismes; si gof est une immersion (resp. une immersion locale), il en est de même de $f$.

En effet, $f$ se factorise en $\mathbf{X} \xrightarrow{\Gamma_f} \mathbf{X} \times_{\mathbb{Z}} \mathbf{Y} \xrightarrow{p_2} \mathbf{Y}$. D'autre part, $p_2$ s'identifie à $(g \circ f) \times_{\mathbb{Z}} \mathbf{I}_{\mathbb{Y}}$ (3.3.4); si $g \circ f$ est une immersion (resp. une immersion locale), il en est de même de $p_2$ (4.3.1 et 4.5.5), et comme $\Gamma_f$ est une immersion (5.3.11), on conclut par (4.2.4) (resp. (4.5.5)).

Corollaire (5.3.14). — Soient $j: X \to Y$, $g: X \to Z$ deux S-morphismes. Si $j$ est une immersion (resp. une immersion locale), il en est de même de $(j, g)_{s}$.

En effet, si $p: \mathbf{Y} \times_{\mathbb{S}} \mathbf{Z} \to \mathbf{Y}$ est la première projection, on a $j = p_{0}(j, g)_{\mathbb{S}}$, et il suffit d'appliquer (5.3.13).

Proposition (5.3.15). — Si $f: \mathbf{X} \to \mathbf{Y}$ est un S-morphisme, le diagramme

(5.3.15.1)

$$
\begin{array}{c}\mathbf {X} \stackrel {{\Delta_ {\mathrm{x}}}} {{\to}} \mathbf {X} \times_ {\mathrm{s}} \mathbf {X}\\f \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \Bigg \downarrow f \times_ {\mathrm{s}} f\\\mathbf {Y} \stackrel {{\rightarrow}} {{\underset {\Delta_ {\mathrm{y}}} {\to}}} \mathbf {Y} \times_ {\mathrm{s}} \mathbf {Y}\end{array}
$$

est commutatif (en d'autres termes $\Delta_{\mathrm{X}}$ est un morphisme fonctoriel dans la catégorie des préschémas).

La vérification est immédiate et laissée au lecteur.

Corollaire (5.3.16). — Si X est un sous-préschéma de Y, la diagonale $\Delta_{\mathrm{X}}(\mathrm{X})$ s'identifie à un sous-préschéma de $\Delta_{\mathrm{Y}}(\mathrm{Y})$, dont l'espace sous-jacent s'identifie à

$$
\Delta_ {\mathrm{Y}} (\mathrm{Y}) \cap p _ {1} ^ {- 1} (\mathrm{X}) = \Delta_ {\mathrm{Y}} (\mathrm{Y}) \cap p _ {2} ^ {- 1} (\mathrm{X})
$$

$(p_{1}, p_{2} \text{ projections de } Y \times_{s} Y).$

Appliquons (5.3.15) au morphisme d'injection $f: \mathbf{X} \to \mathbf{Y}$; on sait alors que $f \times_{\mathbb{S}} f$ est une immersion, identifiant l'espace sous-jacent à $\mathbf{X} \times_{\mathbb{S}} \mathbf{X}$ au sous-espace $p_1^{-1}(\mathbf{X}) \cap p_2^{-1}(\mathbf{X})$ de $\mathbf{Y} \times_{\mathbb{S}} \mathbf{Y}$ (4.3.1); en outre, si $z \in \Delta_{\mathbf{Y}}(\mathbf{Y}) \cap p_1^{-1}(\mathbf{X})$, on a $z = \Delta_{\mathbf{Y}}(y)$

et $y = p_1(z) \in \mathbf{X}$, donc $y = f(y)$, et $z = \Delta_{\mathrm{Y}}(f(y))$ appartient à $\Delta_{\mathrm{X}}(\mathbf{X})$ en vertu de la commutativité du diagramme (5.3.15.1).

Corollaire (5.3.17). — Soient $f_{1}: Y \to X$, $f_{2}: Y \to X$ deux S-morphismes, y un point de Y tel que $f_{1}(y) = f_{2}(y) = x$ et que les homomorphismes $\mathbf{k}(x) \to \mathbf{k}(y)$ correspondant à $f_{1}$ et $f_{2}$ soient identiques. Alors, si $f = (f_{1}, f_{2})_{S}$, le point $f(y)$ appartient à la diagonale $\Delta_{X|S}(X)$.

Les deux homomorphismes $\boldsymbol{k}(x) \to \boldsymbol{k}(y)$ correspondant à $f_i$ ($i=1,2$) définissent deux S-morphismes $g_i: \text{Spec}(\boldsymbol{k}(y)) \to \text{Spec}(\boldsymbol{k}(x))$ tels que les diagrammes

$$
\begin{array}{c} \operatorname{Spec} (\boldsymbol {k} (y)) \xrightarrow {g _ {i}} \operatorname{Spec} (\boldsymbol {k} (x)) \\ \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \downarrow \\ \mathbf {Y} \xrightarrow [ f _ {i} ]{} \mathbf {X} \end{array}
$$

soient commutatifs. Le diagramme

$$
\begin{array}{c} \operatorname{Spec} (\boldsymbol {k} (y)) \xrightarrow {(g _ {1} , g _ {2}) _ {\mathrm{s}}} \operatorname{Spec} (\boldsymbol {k} (x)) \times_ {\mathrm{s}} \operatorname{Spec} (\boldsymbol {k} (x)) \\ \downarrow \\ \mathbf {Y} \xrightarrow {(f _ {1} , f _ {2}) _ {\mathrm{s}}} \mathbf {X} \times_ {\mathrm{s}} \mathbf {X} \end{array}
$$

est donc aussi commutatif. Or il résulte de l'égalité $g_1 = g_2$ que l'image par $(g_1, g_2)_s$ de l'unique point de $\text{Spec}(\boldsymbol{k}(y))$ appartient à la diagonale de $\text{Spec}(\boldsymbol{k}(x)) \times {}_s\text{Spec}(\boldsymbol{k}(x))$; la conclusion résulte donc de (5.3.15).

## 5.4. Morphismes et préschémas séparés.

Définition (5.4.1). — On dit qu'un morphisme de préschémas $f: \mathbf{X} \to \mathbf{Y}$ est séparé si le morphisme diagonal $\mathbf{X} \to \mathbf{X} \times_{\mathbf{Y}} \mathbf{X}$ est une immersion fermée; on dit alors aussi que $\mathbf{X}$ est un préschéma séparé au-dessus de $\mathbf{Y}$, ou un Y-schéma. On dit qu'un préschéma $\mathbf{X}$ est séparé s'il est séparé au-dessus de $\text{Spec}(\mathbf{Z})$; on dit aussi alors que $\mathbf{X}$ est un schéma (cf. (5.5.7)).

En vertu de (5.3.9), pour que X soit séparé au-dessus de Y, il faut et il suffit que  $\Delta_{\mathrm{X}}(\mathrm{X})$  soit un sous-espace fermé de l'espace sous-jacent à  $X \times_{Y} X$ .

Proposition (5.4.2). — Soit S→T un morphisme séparé. Si X et Y sont deux S-préschémas, l'immersion canonique  $X \times_{S} Y \rightarrow X \times_{T} Y$  (5.3.10) est fermée.

En effet, si on se reporte au diagramme (5.3.5.1), on voit que $(p,q)_{\mathrm{T}}$ peut être considéré comme obtenu à partir de $\Delta_{\mathrm{S|T}}$ par l'extension $f\times_{\mathrm{T}}g:\mathbf{X}\times_{\mathrm{T}}\mathbf{Y}\to \mathbf{S}\times_{\mathrm{T}}\mathbf{S}$ du préschéma de base $\mathbf{S}\times_{\mathrm{T}}\mathbf{S}$; la proposition résulte alors de (4.3.2).

Corollaire (5.4.3). — Soient Y un S-schéma, $f: \mathrm{X} \to \mathrm{Y}$ un S-morphisme. Alors le morphisme graphe $\Gamma_f: \mathrm{X} \to \mathrm{X} \times_{\mathrm{s}} \mathrm{Y}$ (5.3.11) est une immersion fermée.

C'est le cas particulier de (5.4.2) où l'on remplace S par Y et T par S.

Corollaire (5.4.4). — Soient $f: \mathrm{X} \to \mathrm{Y}$, $g: \mathrm{Y} \to \mathrm{Z}$ deux morphismes, $g$ étant séparé. Si gof est une immersion fermée, il en est de même de $f$.

La démonstration à partir de (5.4.3) est la même que celle de (5.3.13) à partir de (5.3.11).

Corollaire (5.4.5). — Soient Z un S-schéma, $j: \mathrm{X} \to \mathrm{Y}$, $g: \mathrm{X} \to \mathrm{Z}$ deux S-morphismes. Si $j$ est une immersion fermée, il en est de même de $(j, g)_{\mathrm{s}}: \mathrm{X} \to \mathrm{Y} \times_{\mathrm{s}} \mathrm{Z}$.

La démonstration à partir de (5.4.4) est la même que celle de (5.3.14) à partir de (5.3.13).

Corollaire (5.4.6). — Si X est un S-schéma, toute S-section de X (2.5.5) est une immersion fermée.

Si $\varphi : \mathbf{X} \to \mathbf{S}$ est le morphisme structural, $\psi : \mathbf{S} \to \mathbf{X}$ une S-section de X, il suffit d'appliquer (5.4.5) à $\varphi \circ \psi = I_S$.

Corollaire (5.4.7). — Soient S un préschéma intègre, s son point générique, X un S-schéma. Si deux S-sections f, g de X sont telles que  $f(s)=g(s)$ , alors f=g.

En effet, si $x=f(s)=g(s)$, les homomorphismes $\mathbf{k}(x)\to\mathbf{k}(s)$ correspondant à $f$ et $g$ sont nécessairement identiques. Si $h=(f,g)_{\mathrm{S}}$, on en déduit (5.3.17) que $h(s)$ appartient à la diagonale $\mathrm{Z}=\Delta_{\mathrm{X}}(\mathrm{X})$; mais comme $\mathrm{S}=\overline{\{s\}}$ et que $Z$ est fermée par hypothèse, on a $h(\mathrm{S})\subset\mathrm{Z}$. Il résulte alors de (5.2.2) que $h$ se factorise en $\mathrm{S}\to\mathrm{Z}\to\mathrm{X}\times_{\mathrm{s}}\mathrm{X}$, et on en conclut que $f=g$ par définition de la diagonale.

Remarque (5.4.8). — Si l'on suppose réciproquement que la conclusion de (5.4.3) est vérifiée lorsque $f = \mathrm{I}_{\mathrm{Y}}$, on en conclut que Y est séparé au-dessus de S ; de même, si on suppose que la conclusion de (5.4.5) s'applique aux deux morphismes $\mathbf{Y} \xrightarrow{\Delta_{\mathrm{Y}}} \mathbf{Y} \times_{\mathrm{Z}} \mathbf{Y} \xrightarrow{p_1} \mathbf{Y}$, on en tire que $\Delta_{\mathrm{Y}}$ est une immersion fermée, donc que Y est séparé au-dessus de Z ; enfin, la validité de la conclusion de (5.4.6) pour la Y-section $\Delta_{\mathrm{Y}}$ du Y-préschéma $\mathbf{Y} \times_{\mathrm{s}} \mathbf{Y} \to \mathbf{Y}$, implique que Y est séparé au-dessus de S.

## 5.5. Critères de séparation.

Proposition (5.5.1). — (i) Tout monomorphisme de préschémas (et en particulier toute immersion) est un morphisme séparé.

(ii) Le composé de deux morphismes séparés est séparé.

(iii) Si $f: \mathbf{X} \to \mathbf{X}'$, $g: \mathbf{Y} \to \mathbf{Y}'$ sont deux S-morphismes séparés, $f \times_{\mathrm{S}} g$ est séparé.

(iv) Si $f: \mathbf{X} \to \mathbf{Y}$ est un S-morphisme séparé, le $\mathbf{S}'$-morphisme $f_{(\mathbf{S}')}$ est séparé pour toute extension $\mathbf{S}' \to \mathbf{S}$ du préschéma de base.

(v) Si le composé gof de deux morphismes est séparé, f est séparé.

(vi) Pour qu'un morphisme $f$ soit séparé, il faut et il suffit que $f_{\text{red}}$ (5.1.5) le soit.

(i) résulte aussitôt de (5.3.8). Si $f: \mathrm{X} \to \mathrm{Y}$, $g: \mathrm{Y} \to \mathrm{Z}$ sont deux morphismes, le diagramme

$$
\begin{array}{c} \mathbf {X} \xrightarrow {\Delta_ {\mathrm{x} | \mathrm{z}}} \mathbf {X} \times_ {\mathrm{z}} \mathbf {X} \\ \Delta_ {\mathrm{x} | \mathrm{y}} \searrow \nearrow_ {j} \\ \mathbf {X} \times_ {\mathrm{y}} \mathbf {X} \end{array}\tag{5.5.1.1}
$$

où j désigne l'immersion canonique (5.3.10) est commutatif, comme on le vérifie aussitôt. Si f et g sont séparés,  $\Delta_{X|Y}$  est une immersion fermée par définition, et j est une immersion fermée en vertu de (5.4.2), donc  $\Delta_{X|Z}$  est une immersion fermée par (4.2.4), ce qui

prouve (ii). Vu (i) et (ii), (iii) et (iv) sont équivalentes (3.5.1), et il suffit de démontrer (iv). Or, $\mathbf{X}_{(\mathrm{S}^{\prime})}\times_{\mathrm{Y}_{(\mathrm{S}^{\prime})}}\mathbf{X}_{(\mathrm{S}^{\prime})}$ s'identifie canoniquement à $(\mathbf{X}\times_{\mathrm{Y}}\mathbf{X})\times_{\mathrm{Y}}\mathbf{Y}_{(\mathrm{S}^{\prime})}$ en vertu de (3.3.11) et de (3.3.9.1), et on vérifie aussitôt que le morphisme diagonal $\Delta_{\mathrm{X}_{(\mathrm{s}^{\prime})}}$ s'identifie alors à $\Delta_{\mathrm{X}}\times_{\mathrm{Y}}\mathbf{I}_{\mathrm{Y}_{(\mathrm{s}^{\prime})}}$; la proposition résulte donc de (4.3.1).

Pour établir (v), considérons, comme dans (5.3.13) la factorisation $\mathbf{X} \xrightarrow{\Gamma_f} \mathbf{X} \times_{\mathbb{Z}} \mathbf{Y} \xrightarrow{p_2} \mathbf{Y}$ de $f$, en remarquant que $p_2 = (g \circ f) \times_{\mathbb{Z}} \mathbf{I}_{\mathbb{Y}}$; l'hypothèse que $g \circ f$ est séparé entraîne que $p_2$ est séparé par (iii) et (i), et comme $\Gamma_f$ est une immersion, $\Gamma_f$ est séparé par (i), donc $f$ est séparé par (ii). Enfin, pour démontrer (vi), rappelons que les préschémas $\mathbf{X}_{\text{red}} \times_{\mathbb{Y}_{\text{red}}} \mathbf{X}_{\text{red}}$ et $\mathbf{X}_{\text{red}} \times_{\mathbb{Y}} \mathbf{X}_{\text{red}}$ s'identifient canoniquement (5.1.7); si on désigne par $j$ l'injection $\mathbf{X}_{\text{red}} \to \mathbf{X}$, le diagramme

![](images/page_135_image_2.jpg)

est commutatif (5.3.15), et la proposition résulte de ce que les flèches verticales sont des homéomorphismes des espaces sous-jacents (4.3.1).

Corollaire (5.5.2). — Si f : X→Y est séparé, la restriction de f à tout sous-préschéma de X est séparée.

Cela résulte de (5.5.1, (i) et (ii)).

Corollaire (5.5.3). — Si X, Y sont deux S-préschémas tels que Y soit séparé au-dessus de S,  $X \times_{s} Y$  est séparé au-dessus de X.

C'est un cas particulier de (5.5.1, (iv)).

Proposition (5.5.4). — Soit X un préschéma, et supposons que son espace sous-jacent soit réunion d'une famille finie de parties fermées  $X_{k}$  ( $1 \leqslant k \leqslant n$ ); on considère pour chaque k le sous-préschéma réduit de X ayant  $X_{k}$  pour espace sous-jacent (5.2.1) et on le note encore  $X_{k}$ . Soit  $f: X \to Y$  un morphisme, et pour chaque k, soit  $Y_{k}$  une partie fermée de Y telle que  $f(X_{k}) \subset Y_{k}$ ; on note encore  $Y_{k}$  le sous-préschéma réduit de Y ayant  $Y_{k}$  pour espace sous-jacent, de sorte que la restriction  $X_{k} \to Y$  de f à  $X_{k}$  se factorise en  $X_{k} \xrightarrow{f_{k}} Y_{k} \to Y$  (5.2.2). Pour que f soit séparé, il faut et il suffit que les  $f_{k}$  le soient.

La nécessité résulte de (5.5.1, (i), (ii) et (v)). Inversement, si la condition de l'énoncé est satisfaite, chacune des restrictions  $X_{k} \rightarrow Y$  de f est séparée (5.5.1, (i) et (ii)); si  $p_{1}, p_{2}$  sont les projections de  $X \times_{Y} X$ , le sous-espace  $\Delta_{X_{k}}(X_{k})$  s'identifie au sous-espace  $\Delta_{X}(X) \cap p_{1}^{-1}(X_{k})$  de l'espace sous-jacent à  $X \times_{Y} X$  (5.3.16); ces sous-espaces étant fermés dans  $X \times_{Y} X$ , il en est de même de leur réunion  $\Delta_{X}(X)$ .

Supposons en particulier que les  $X_{k}$  soient les composantes irréductibles de X ; alors on peut supposer que les  $Y_{k}$  sont des composantes irréductibles de Y (0, 2.1.5) ; la prop. (5.5.4) ramène donc dans ce cas la notion de séparation au cas des préschémas intègres (2.1.7).

Proposition (5.5.5). — Soit  $(\mathbf{Y}_{\lambda})$  un recouvrement ouvert d'un préschéma Y; pour qu'un morphisme  $f: X \to Y$  soit séparé, il faut et il suffit que chacune de ses restrictions  $f^{-1}(\mathbf{Y}_{\lambda}) \to \mathbf{Y}_{\lambda}$  soit séparée.

Si on pose  $\mathbf{X}_{\lambda}=f^{-1}(\mathbf{Y}_{\lambda})$ , tout revient, compte tenu de (4.2.4, b)) et de l'identité des produits  $X_{\lambda}\times_{Y}X_{\lambda}$  et  $X_{\lambda}\times_{Y_{\lambda}}X_{\lambda}$  (3.2.5), à prouver que les  $X_{\lambda}\times_{Y}X_{\lambda}$  forment un recouvrement de  $X\times_{Y}X$ . Or si l'on pose  $Y_{\lambda\mu}=Y_{\lambda}\cap Y_{\mu}$  et  $X_{\lambda\mu}=X_{\lambda}\cap X_{\mu}=f^{-1}(Y_{\lambda\mu})$ ,  $X_{\lambda}\times_{Y}X_{\mu}$  s'identifie au produit  $X_{\lambda\mu}\times_{Y_{\lambda\mu}}X_{\lambda\mu}$  (3.2.6.4), donc aussi à  $X_{\lambda\mu}\times_{Y}X_{\lambda\mu}$  (3.2.5), et finalement à un ouvert de  $X_{\lambda}\times_{Y}X_{\lambda}$ , ce qui établit notre assertion (3.2.7).

La prop. (5.5.4) permet, en prenant un recouvrement de Y par des ouverts affines, de ramener l'étude des morphismes séparés à celle des morphismes séparés à valeurs dans des schémas affines.

Proposition (5.5.6). — Soient Y un schéma affine, X un préschéma,  $(\mathrm{U}_{\alpha})$  un recouvrement de X par des ouverts affines. Pour qu'un morphisme  $f: X \to Y$  soit séparé, il faut et il suffit que, pour tout couple d'indices  $(\alpha, \beta)$ ,  $U_{\alpha} \cap U_{\beta}$  soit un ouvert affine, et que l'anneau  $\Gamma(\mathrm{U}_{\alpha} \cap \mathrm{U}_{\beta}, \mathcal{O}_{\mathrm{X}})$  soit engendré par la réunion des images canoniques des anneaux  $\Gamma(\mathrm{U}_{\alpha}, \mathcal{O}_{\mathrm{X}})$  et  $\Gamma(\mathrm{U}_{\beta}, \mathcal{O}_{\mathrm{X}})$ .

Les  $U_{\alpha} \times_{Y} U_{\beta}$  forment un recouvrement ouvert de  $X \times_{Y} X$  (3.2.7); en désignant par p et q les projections de  $X \times_{Y} X$ , on a

$$
\Delta_ {\mathrm{X}} ^ {- 1} \left(\mathrm{U} _ {\alpha} \times_ {\mathrm{Y}} \mathrm{U} _ {\beta}\right) = \Delta_ {\mathrm{X}} ^ {- 1} \left(p ^ {- 1} \left(\mathrm{U} _ {\alpha}\right) \cap q ^ {- 1} \left(\mathrm{U} _ {\beta}\right)\right) = \Delta_ {\mathrm{X}} ^ {- 1} \left(p ^ {- 1} \left(\mathrm{U} _ {\alpha}\right)\right) \cap \Delta_ {\mathrm{X}} ^ {- 1} \left(q ^ {- 1} \left(\mathrm{U} _ {\beta}\right)\right) = \mathrm{U} _ {\alpha} \cap \mathrm{U} _ {\beta};
$$

tout revient donc à exprimer que la restriction de $\Delta_{\mathrm{X}}$ à $\mathrm{U}_{\alpha} \cap \mathrm{U}_{\beta}$ est une immersion fermée dans $\mathrm{U}_{\alpha} \times_{\mathrm{Y}} \mathrm{U}_{\beta}$. Or, cette restriction n'est autre que $(j_{\alpha}, j_{\beta})_{\mathrm{Y}}$, en désignant par $j_{\alpha}$ (resp. $j_{\beta}$) le morphisme d'injection de $\mathrm{U}_{\alpha} \cap \mathrm{U}_{\beta}$ dans $\mathrm{U}_{\alpha}$ (resp. $\mathrm{U}_{\beta}$), ainsi qu'il résulte des définitions. Comme $\mathrm{U}_{\alpha} \times_{\mathrm{Y}} \mathrm{U}_{\beta}$ est un schéma affine dont l'anneau est canoniquement isomorphe à $\Gamma(\mathrm{U}_{\alpha}, \mathcal{O}_{\mathrm{X}}) \otimes_{\Gamma(\mathrm{Y}, \mathcal{O}_{\mathrm{Y}})} \Gamma(\mathrm{U}_{\beta}, \mathcal{O}_{\mathrm{X}})$ (3.2.2), on voit que $\mathrm{U}_{\alpha} \cap \mathrm{U}_{\beta}$ doit être un schéma affine et que l'application $h_{\alpha} \otimes h_{\beta} \to h_{\alpha} h_{\beta}$ de l'anneau $\mathrm{A}(\mathrm{U}_{\alpha} \times_{\mathrm{Y}} \mathrm{U}_{\beta})$ dans $\Gamma(\mathrm{U}_{\alpha} \cap \mathrm{U}_{\beta}, \mathcal{O}_{\mathrm{X}})$ doit être surjective (4.2.3), ce qui achève la démonstration.

Corollaire (5.5.7). — Un schéma affine est séparé (et est par suite un schéma, ce qui justifie la terminologie de (5.4.1)).

Corollaire (5.5.8). — Soit Y un schéma affine; pour que $f: \mathbf{X} \to \mathbf{Y}$ soit un morphisme séparé, il faut et il suffit que X soit séparé (autrement dit, que X soit un schéma).

On observera en effet que le critère de (5.5.6) ne dépend pas de f.

Corollaire (5.5.9). — Pour qu'un morphisme $f: X \to Y$ soit séparé, il faut que pour tout ouvert U sur lequel Y induit un préschéma séparé, le préschéma induit $f^{-1}(U)$ soit séparé, et il suffit qu'il en soit ainsi pour tout ouvert affine $U \subset Y$.

La nécessité de la condition résulte de (5.5.4) et (5.5.1, (ii)); la suffisance résulte de (5.5.4) et (5.5.8), compte tenu de l'existence de recouvrements ouverts affines de Y.

$$
\mathrm{X} \rightarrow \mathrm{Y}
$$

Proposition (5.5.10). — Soient Y un schéma, $f: \mathrm{X} \to \mathrm{Y}$ un morphisme. Pour tout ouvert affine U de X et tout ouvert affine V de Y, $\mathrm{U} \cap f^{-1}(\mathrm{V})$ est affine.

Soient $p_1, p_2$ les projections de $X \times_z Y$; le sous-espace $U \cap f^{-1}(V)$ est l'image par $p_1$ de $\Gamma_f(X) \cap p_1^{-1}(U) \cap p_2^{-1}(V)$. Or, $p_1^{-1}(U) \cap p_2^{-1}(V)$ s'identifie à l'espace sous-jacent au

préschéma  $U \times_{z} V$  (3.2.7), et est par suite un schéma affine (3.2.2); comme  $\Gamma_{f}(X)$  est fermé dans  $X \times_{z} Y$  (5.4.3),  $\Gamma_{f}(X) \cap p_{1}^{-1}(U) \cap p_{2}^{-1}(V)$  est fermé dans  $U \times_{z} V$, et par suite le préschéma induit par le sous-préschéma de  $X \times_{z} Y$  associé à  $\Gamma_{f}$  (4.2.1), sur la partie ouverte  $\Gamma_{f}(X) \cap p_{1}^{-1}(U) \cap p_{2}^{-1}(V)$  de son espace sous-jacent, est un sous-préschéma fermé d'un schéma affine, donc un schéma affine (4.2.3). La proposition résulte alors du fait que  $\Gamma_{f}$  est une immersion.

Exemples (5.5.11). — Le préschéma de l'exemple (2.3.2) (« droite projective sur un corps K ») est séparé, car pour le recouvrement  $(\mathbf{X}_{1}, \mathbf{X}_{2})$  de X par des ouverts affines,  $X_{1} \cap X_{2} = U_{12}$  est affine et  $\Gamma(\mathrm{U}_{12}, \mathcal{O}_{\mathrm{X}})$ , anneau des fractions rationnelles de la forme  $f(s)/s^{m}$  avec  $f \in K[s]$ , est engendré par K[s] et par 1/s, donc les conditions de (5.5.6) sont vérifiées.

Avec le même choix de  $X_{1}$ ,  $X_{2}$ ,  $U_{12}$  et  $U_{21}$  que dans l'exemple (2.3.2), prenons cette fois pour  $u_{12}$  l'isomorphisme qui à  $f(s)$  fait correspondre  $f(t)$ ; on obtient cette fois par recollement un préschéma intègre non séparé X, car la première condition de (5.5.6) est vérifiée, mais non la seconde. Il est immédiat ici que  $\Gamma(\mathbf{X},\mathcal{O}_{\mathbf{X}})\to\Gamma(\mathbf{X}_{1},\mathcal{O}_{\mathbf{X}})=\mathbf{K}[s]$  est un isomorphisme; l'isomorphisme réciproque définit un morphisme  $f:\mathbf{X}\to\operatorname{Spec}(\mathbf{K}[s])$  qui est surjectif, et pour tout  $y\in\operatorname{Spec}(\mathbf{K}[s])$  tel que  $\mathbf{i}_{y}\neq(\mathbf{o})$ ,  $f^{-1}(y)$  est réduit à un point, mais pour  $\mathbf{i}_{y}=(\mathbf{o})$ ,  $f^{-1}(y)$  se compose de deux points distincts (on dit que X est la « droite affine sur K, où le point o est dédouble »).

On peut aussi donner des exemples où aucune des deux conditions de (5.5.6) n'est vérifiée. Remarquons d'abord que dans le spectre premier Y de l'anneau de polynômes A=K[s, t] à deux indéterminées sur un corps K, l'ouvert U réunion de D(s) et de D(t) n'est pas un ouvert affine. En effet, si z est une section de  $O_{Y}$  au-dessus de U, il existe deux entiers  $m \geqslant 0$ ,  $n \geqslant 0$  tels que  $s^{m}z$  et  $t^{n}z$  soient les restrictions à U de polynômes en s et t (1.4.1), ce qui n'est évidemment possible que si la section z se prolonge en une section au-dessus de Y tout entier, identifiée à un polynôme en s et t. Si U était un ouvert affine, le morphisme d'injection U→Y serait donc un isomorphisme (1.7.3), ce qui est absurde puisque U≠Y.

Cela étant, prenons deux schémas affines  $Y_{1}$ ,  $Y_{2}$ , spectres premiers des anneaux  $A_{1}=K[s_{1}, t_{1}]$ ,  $A_{2}=K[s_{2}, t_{2}]$ ; prenons  $U_{12}=D(s_{1})\cup D(t_{1})$ ,  $U_{21}=D(s_{2})\cup D(t_{2})$ , et pour  $u_{12}$  la restriction à  $U_{21}$  de l'isomorphisme  $Y_{2}\to Y_{1}$  correspondant à l'isomorphisme d'anneaux qui à  $f(s_{1}, t_{1})$  fait correspondre  $f(s_{2}, t_{2})$ ; on a ainsi un exemple où aucune des conditions de (5.5.6) n'est satisfaite (le préschéma intègre ainsi obtenu est dit « plan affine sur K, où le point o est dédoublé »).

Remarque (5.5.12). — Étant donnée une propriété P de morphismes de préschémas, considérons les propositions suivantes :

(i) Toute immersion fermée possède la propriété P.

(ii) Le composé de deux morphismes possédant la propriété P possède la propriété P.

(iii) Si $f: \mathbf{X} \to \mathbf{X}'$, $g: \mathbf{Y} \to \mathbf{Y}'$ sont deux S-morphismes possédant la propriété $\mathbf{P}$, $f \times_{\mathrm{sg}} g$ possède la propriété $\mathbf{P}$.

(iv) Si $f: \mathbf{X} \to \mathbf{Y}$ est un S-morphisme possédant la propriété $\mathbf{P}$, tout $\mathbf{S}'$-morphisme $f_{(\mathbf{S}')}$ obtenu par une extension $\mathbf{S}' \to \mathbf{S}$ du préschéma de base, possède la propriété $\mathbf{P}$.

(v) Si le composé gof de deux morphismes $f: \mathbf{X} \to \mathbf{Y}, g: \mathbf{Y} \to \mathbf{Z}$ possède la propriété $\mathbf{P}$, et si g est séparé, $f$ possède la propriété $\mathbf{P}$.

(vi) Si un morphisme $f: \mathbf{X} \to \mathbf{Y}$ possède la propriété $\mathbf{P}$, il en est de même de $f_{\text{red}}$ (5.1.5).

Dans ces conditions, si on suppose (i) et (ii) vérifiées, (iii) et (iv) sont équivalentes, et (v) et (vi) sont des conséquences de (i), (ii) et (iii).

La première assertion a déjà été démontrée (3.5.1). Considérons la factorisation (5.3.13) de $f$ en $\mathbf{X} \xrightarrow{\Gamma_f} \mathbf{X} \times_{\mathbb{Z}} \mathbf{Y} \xrightarrow{p_2} \mathbf{Y}$; la relation $p_2 = (g \circ f) \times_{\mathbb{Z}} \mathbf{I}_Y$ montre que si $g \circ f$ possède la propriété $\boldsymbol{P}$, il en est de même de $p_2$ en vertu de (iii); si $g$ est séparé, $\Gamma_f$ est une immersion fermée (5.4.3), donc possède aussi la propriété $\boldsymbol{P}$ par (i); enfin, en vertu de (ii), $f$ possède la propriété $\boldsymbol{P}$.

Enfin, considérons le diagramme commutatif

$$
\begin{array}{c} \mathbf {X} _ {\text {red}} \xrightarrow {t _ {\text {red}}} \mathbf {Y} _ {\text {red}} \\ \downarrow \qquad \qquad \qquad \downarrow \\ \mathbf {X} \xrightarrow [ f ]{} \mathbf {Y} \end{array}
$$

où les flèches verticales sont des immersions fermées (5.1.5), donc possèdent la propriété P par (i). L'hypothèse que f possède la propriété P entraîne donc par (ii) que  $X_{red} \stackrel{f_{red}}{\rightarrow} Y_{red} \rightarrow Y$  possède la propriété P ; enfin, comme une immersion fermée est séparée (5.5.1, (i)),  $f_{red}$  possède la propriété P en vertu de (v).

On notera que si on considère les propositions :

(i') Toute immersion possède la propriété P.

(v') Si gof possède la propriété P, il en est de même de f;

alors le raisonnement fait ci-dessus montre que (v') est conséquence de (i'), (ii) et (iii).

(5.5.13) On notera que (v) et (vi) sont encore conséquences de (i), (iii) et

(ii') Si $j: \mathrm{X} \to \mathrm{Y}$ est une immersion fermée et $g: \mathrm{Y} \to \mathrm{Z}$ un morphisme possédant la propriété $\mathbf{P}$, alors goj possède la propriété $\mathbf{P}$.

De même,  $(v')$  est conséquence de  $(i')$ , (iii) et

(ii'') Si $j: \mathbf{X} \to \mathbf{Y}$ est une immersion et $g: \mathbf{Y} \to \mathbf{Z}$ un morphisme possédant la propriété $\mathbf{P}$, alors goj possède la propriété $\mathbf{P}$.

Cela résulte en effet aussitôt des raisonnements de (5.5.12).

## § 6. CONDITIONS DE FINITUDE

## 6.1. Préschémas noethériens et localement noethériens.

Définition (6.1.1). — On dit qu'un préschéma X est noethérien (resp. localement noethérien) s'il est réunion finie (resp. réunion) d'ouverts affines  $V_{\alpha}$  tels que l'anneau de chacun des schémas induits sur les  $V_{\alpha}$  soit noethérien.

Il résulte aussitôt de (1.5.2) que si X est localement noethérien, le faisceau structural $\mathcal{O}_{\mathrm{X}}$ est un faisceau cohérent d'anneaux, la question étant locale. Tout sous-$\mathcal{O}_{\mathrm{X}}$-

Module (resp. tout $\mathcal{O}_{\mathrm{X}}$-Module quotient) quasi-cohérent d'un $\mathcal{O}_{\mathrm{X}}$-Module cohérent $\mathcal{F}$ est alors cohérent, car la question est de nouveau locale, et il suffit d'appliquer (1.5.1), (1.4.1) et (1.3.10), joints au fait qu'un sous-module (resp. module quotient) d'un module de type fini sur un anneau noethérien est de type fini. Plus particulièrement, tout faisceau d'idéaux quasi-cohérent de $\mathcal{O}_{\mathrm{X}}$ est cohérent.

Si un préschéma X est réunion finie (resp. réunion) d'ouverts  $W_{\lambda}$  tels que les préschémas induits sur les  $W_{\lambda}$  soient noethériens (resp. localement noethériens), il est clair que X est noethérien (resp. localement noethérien).

Proposition (6.1.2). — Pour qu'un préschéma X soit noethérien, il faut et il suffit qu'il soit localement noethérien et que son espace sous-jacent soit quasi-compact. L'espace sous-jacent de X est alors noethérien.

La première assertion découle aussitôt des définitions et de (1.1.10 (ii)). La seconde résulte de (1.1.6) et du fait que tout espace réunion finie de sous-espaces noethériens est noethérien (0, 2.2.3).

Proposition (6.1.3). — Soit X un schéma affine d'anneau A. Les conditions suivantes sont équivalentes : a) X est noethérien ; b) X est localement noethérien ; c) A est noethérien.

L'équivalence de $a$) et $b$) résulte de (6.1.2) et de ce que tout schéma affine a un espace sous-jacent quasi-compact (1.1.10); il est clair en outre que $c$) entraîne $a$). Pour voir que $a$) entraîne $c$), remarquons qu'il y a un recouvrement fini ($V_i$) de X par des ouverts affines tels que l'anneau $A_i$ du préschéma induit sur $V_i$ soit noethérien. Soit alors $(a_n)$ une suite croissante d'idéaux de A; il lui correspond canoniquement de façon biunivoque (1.3.7) une suite croissante $(\widetilde{a}_n)$ de faisceaux d'idéaux dans $\widetilde{A} = \mathcal{O}_X$; pour voir que la suite $(a_n)$ est stationnaire, il suffit de prouver que la suite $(\widetilde{a}_n)$ l'est. Or, la restriction $\widetilde{a}_n|V_i$ est un faisceau quasi-cohérent d'idéaux dans $\mathcal{O}_X|V_i$, étant l'image réciproque de $\widetilde{a}_n$ par l'injection canonique $V_i \to X$ (0, 5.1.4); $\widetilde{a}_n|V_i$ est donc de la forme $\widetilde{a}_{ni}$, où $a_{ni}$ est un idéal de $A_i$ (1.3.7). Comme $A_i$ est noethérien, la suite $(a_{ni})$ est stationnaire pour tout $i$, d'où la proposition.

On notera que le raisonnement précédent prouve aussi que si X est un préschéma noethérien, toute suite croissante de faisceaux cohérents d'idéaux de $\mathcal{O}_{\mathrm{X}}$ est stationnaire.

Proposition (6.1.4). — Tout sous-préschéma d'un préschéma noethérien (resp. localement noethérien) est noethérien (resp. localement noethérien).

Il suffit de faire la démonstration pour un préschéma noethérien X; en outre, on est aussitôt ramené par la définition (6.1.1) au cas où X est un schéma affine. Comme tout sous-préschéma de X est un sous-préschéma fermé d'un préschéma induit sur un ouvert (4.1.3), on peut se borner à considérer le cas d'un sous-préschéma Y fermé ou induit sur un ouvert de X. Le cas où Y est fermé est immédiat, car si A est l'anneau de X, on sait que Y est un schéma affine d'anneau A/Im, où Im est un idéal de A (4.2.3); comme A est noethérien (6.1.3), il en est de même de A/Im.

Supposons maintenant Y ouvert dans X ; l'espace sous-jacent Y est noethérien (6.1.2), donc quasi-compact, et par suite réunion finie d'ouverts  $\mathrm{D}(f_{i})$  ( $f_{i} \in A$ );

tout revient à démontrer la proposition lorsque  $Y=D(f)$  avec  $f\in A$ . Mais alors Y est un schéma affine dont l'anneau est isomorphe à  $A_{f}$  (1.3.6); comme A est noethérien (6.1.3), il en est de même de  $A_{f}$ .

(6.1.5) On notera que le produit de deux S-préschémas noethériens n'est pas nécessairement noethérien, même si ces préschémas sont affines, car le produit tensoriel de deux algèbres noethériennes n'est pas nécessairement un anneau noethérien (cf. (6.3.8)).

Proposition (6.1.6). — Si X est un préschéma noethérien, le Nilradical $\mathcal{N}_{\mathrm{X}}$ de $\mathcal{O}_{\mathrm{X}}$ est nilpotent.

On peut en effet recouvrir X par un nombre fini d'ouverts affines  $U_{i}$  et il suffit de prouver qu'il existe des entiers  $n_{i}$  tels que  $(\mathcal{N}_{\mathrm{X}}|\mathrm{U}_{i})^{ni}=0$ ; si n est le plus grand des  $n_{i}$ , on aura alors  $N_{X}^{n}=0$ . On est donc ramené au cas où  $\mathrm{X}=\mathrm{Spec}(\mathrm{A})$  est affine, A étant un anneau noethérien; en vertu de (5.1.1) et de (1.3.13), il suffit d'observer que le nilradical de A est nilpotent ([11], p. 127, cor. 4).

Corollaire (6.1.7). — Soit X un préschéma noethérien; pour que X soit un schéma affine, il faut et il suffit que  $X_{red}$  le soit.

Cela résulte de (6.1.6) et (5.1.10).

Lemme (6.1.8). — Soient X un espace topologique, x un point de X, U un voisinage ouvert de x n'ayant qu'un nombre fini de composantes irréductibles. Alors il existe un voisinage V de x tel que tout voisinage ouvert de x contenu dans V soit connexe.

Soient  $U_{i}$  ( $i \leqslant i \leqslant m$ ) les composantes irréductibles de U ne contenant pas x ; le complémentaire dans U de la réunion des  $U_{i}$  est un voisinage ouvert V de x dans U, donc aussi dans X ; c'est d'ailleurs le complémentaire dans X de la réunion des composantes irréductibles de X qui ne contiennent pas x (0, 2.1.6). Soit alors W un voisinage ouvert de x contenu dans V. Les composantes irréductibles de W sont les traces sur W des composantes irréductibles de U qui rencontrent W (0, 2.1.6), donc ces composantes contiennent x ; comme elles sont connexes, il en est de même de W.

Corollaire (6.1.9). — Un espace topologique localement noethérien est localement connexe (ce qui entraîne entre autres que ses composantes connexes sont ouvertes).

Proposition (6.1.10). — Soit X un espace topologique localement noethérien. Les conditions suivantes sont équivalentes :

a) Les composantes irréductibles de X sont ouvertes.

b) Les composantes irréductibles de X sont identiques à ses composantes connexes.

c) Les composantes connexes de X sont irréductibles.

d) Deux composantes irréductibles distinctes de X ne se rencontrent pas.

Enfin, si X est un préschéma, ces conditions équivalent aussi à :

e) Pour tout $x \in \mathbf{X}$, $\operatorname{Spec}(\mathcal{O}_x)$ est irréductible (autrement dit le nilradical de $\mathcal{O}_x$ est premier).

Il est immédiat que $a)$ entraîne $b)$, car un espace irréductible est connexe, et $a)$ entraîne que les composantes irréductibles de X sont des ensembles à la fois ouverts et fermés. Il est trivial que $b)$ entraîne $c)$; inversement, un ensemble fermé F contenant

une composante connexe C de X et distinct de C ne peut être irréductible, car cet ensemble n'étant pas connexe est réunion de deux ensembles non vides disjoints à la fois ouverts et fermés dans F, donc fermés dans X ; par suite c) entraîne b). On en conclut aussitôt que c) entraîne d), deux composantes connexes distinctes étant sans point commun.

Nous n'avons pas utilisé jusqu'ici le fait que X est localement noethérien. Supposons maintenant cette hypothèse réalisée et montrons que d) entraîne a) : en vertu de (0, 2.1.6), on peut se borner au cas où l'espace X est noethérien, donc n'a qu'un nombre fini de composantes irréductibles. Comme celles-ci sont fermées et deux à deux disjointes, elles sont ouvertes.

Enfin l'équivalence de $d$) et $e$) est valable sans supposer que l'espace sous-jacent au préschéma X soit localement noethérien. On peut en effet se ramener au cas où $\mathbf{X}=\operatorname{Spec}(\mathbf{A})$ est affine en vertu de (0, 2.1.6) ; dire que $x$ n'est contenu que dans une seule composante irréductible de X signifie alors que $\mathbf{j}_{x}$ ne contient qu'un seul idéal minimal de A (1.1.14), ce qui équivaut à dire que $\mathbf{j}_{x}\mathcal{O}_{x}$ ne contient qu'un seul idéal minimal de $\mathcal{O}_{x}$, d'où la conclusion.

Corollaire (6.1.11). — Soit X un espace localement noethérien. Pour que X soit irréductible, il faut et il suffit que X soit connexe et non vide, et que deux composantes irréductibles distinctes de X ne se rencontrent pas. Si X est un préschéma, cette dernière condition équivaut à ce que  $\text{Spec}(\mathcal{O}_{x})$  est irréductible pour tout  $x \in X$ .

La dernière partie a été vue dans (6.1.10) ; il n'y a donc à prouver que la suffisance des conditions de la première assertion. Mais d'après (6.1.10), ces conditions entraînent que les composantes irréductibles de X sont ses composantes connexes, et comme X est connexe et non vide, il est irréductible.

Corollaire (6.1.12). — Soit X un préschéma localement noethérien. Pour que X soit intègre, il faut et il suffit que X soit connexe et que $\mathcal{O}_{x}$ soit intègre pour tout $x\in\mathbf{X}$.

Proposition (6.1.13). — Soit X un préschéma localement noethérien, et soit  $x \in X$  un point tel que le nilradical  $N_x$  de  $O_x$  soit premier (resp. que  $O_x$  soit réduit, resp. intègre); alors il existe un voisinage ouvert U de x qui est irréductible (resp. réduit, resp. intègre).

Il suffit de considérer les deux cas où $\mathcal{N}_x$ est premier et où $\mathcal{N}_x = 0$, la troisième hypothèse étant conjonction des deux premières. Si $\mathcal{N}_x$ est premier, $x$ n'appartient qu'à une seule composante irréductible Y de X (6.1.10); la réunion des composantes irréductibles de X ne contenant pas $x$ est fermée (l'ensemble de ces composantes étant localement fini), et le complémentaire U de cette réunion est donc ouvert et contenu dans Y, donc irréductible (0, 2.1.6). Si $\mathcal{N}_x = 0$, on a aussi $\mathcal{N}_y = 0$ pour tout $y$ dans un voisinage de $x$, car $\mathcal{N}$ est quasi-cohérent (5.1.1), et par suite cohérent puisque X est localement noethérien, et la conclusion résulte de (0, 5.2.2).

## 6.2. Préschémas artiniens.

Définition (6.2.1). — On dit qu'un préschéma est artinien s'il est affine et si son anneau est artinien.

Proposition (6.2.2). — Étant donné un préschéma X, les conditions suivantes sont équivalentes :

a) X est un schéma artinien ;

b) X est noethérien et son espace sous-jacent est discret ;

c) X est noethérien et les points de son espace sous-jacent sont fermés (condition $\mathbf{T}_1$).

Lorsqu'il en est ainsi, l'espace sous-jacent à X est fini, et l'anneau A de X est composé direct des anneaux locaux (artiniens) des points de X.

On sait que $a)$ entraîne la dernière assertion ([13], p. 205, th. 3), tout idéal premier de A est alors maximal et est l'image réciproque de l'idéal maximal de l'un des composants locaux de A, donc l'espace X est fini et discret ; $a)$ entraîne donc $b)$ et $b)$ entraîne évidemment $c)$. Pour voir que $c)$ entraîne $a)$, montrons d'abord que X est alors fini ; on peut en effet se ramener au cas où X est affine, et on sait qu'un anneau noethérien dont tous les idéaux premiers sont maximaux est artinien ([13], p. 203), d'où notre assertion. L'espace sous-jacent X est alors discret, somme topologique d'un nombre fini de points $x_i$, et les anneaux locaux $\mathcal{O}_{x_i} = A_i$ sont artiniens ; il est clair que X est isomorphe au schéma affine spectre premier de l'anneau A composé direct des $A_i$ (1.7.3).

## 6.3. Morphismes de type fini.

Définition (6.3.1). — On dit qu'un morphisme $f: \mathbf{X} \to \mathbf{Y}$ est de type fini si Y est réunion d'une famille $(\mathrm{V}_{\alpha})$ d'ouverts affines ayant la propriété suivante :

(P)  $f^{-1}(V_{\alpha})$  est réunion finie d'ouverts affines  $U_{\alpha i}$  tels que chacun des anneaux  $\mathrm{A}(U_{\alpha i})$  soit une algèbre de type fini sur  $\mathrm{A}(V_{\alpha})$ .

On dit alors aussi que X est un préschéma de type fini sur Y, ou un Y-préschéma de type fini.

Proposition (6.3.2). — Si $f: \mathbf{X} \to \mathbf{Y}$ est un morphisme de type fini, tout ouvert affine W de Y possède la propriété (P) de la déf. (6.3.1).

Nous démontrerons d'abord le

Lemme (6.3.2.1). — Si T⊂Y est un ouvert affine, possédant la propriété (P), alors, pour tout g∈A(T), D(g) possède la propriété (P).

En effet, par hypothèse, $f^{-1}(\mathrm{T})$ est réunion finie d'ouverts affines $\mathbf{Z}_j$ tels que $\mathrm{A}(\mathbf{Z}_j)$ soit une algèbre de type fini sur $\mathrm{A}(\mathrm{T})$; soit $\varphi_j: \mathrm{A}(\mathrm{T}) \to \mathrm{A}(\mathbf{Z}_j)$ l'homomorphisme d'anneaux correspondant à la restriction de $f$ à $\mathbf{Z}_j$ (2.2.4), et posons $g_j = \varphi_j(g)$; on a alors $f^{-1}(\mathrm{D}(g)) \cap \mathbf{Z}_j = \mathrm{D}(g_j)$ (1.2.2.2). Or, $\mathrm{A}(\mathrm{D}(g_j)) = \mathrm{A}(\mathbf{Z}_j)_{g_j} = \mathrm{A}(\mathbf{Z}_j)[\mathrm{I}/g_j]$ est de type fini sur $\mathrm{A}(\mathbf{Z}_j)$ et a fortiori sur $\mathrm{A}(\mathrm{T})$ en vertu de l'hypothèse, donc aussi sur $\mathrm{A}(\mathrm{D}(g)) = \mathrm{A}(\mathrm{T})[\mathrm{I}/g]$, ce qui démontre le lemme.

Ce lemme étant établi, comme W est quasi-compact (1.1.10), il existe un recouvrement fini de W par des ensembles de la forme  $\mathrm{D}(g_{i})$ , où chaque  $g_{i}$  appartient à un anneau  $\mathrm{A}(\mathrm{V}_{\alpha(i)})$ . Chaque  $\mathrm{D}(g_{i})$ , étant quasi-compact, est réunion finie d'ensembles  $\mathrm{D}(h_{ik})$  où  $h_{ik} \in \mathrm{A}(\mathrm{W})$ ; si  $\varphi_{i}: \mathrm{A}(\mathrm{W}) \to \mathrm{A}(\mathrm{D}(g_{i}))$  est l'application canonique, on a  $\mathrm{D}(h_{ik}) = \mathrm{D}(\varphi_{i}(h_{ik}))$  en vertu de (1.2.2.2). En vertu de (6.3.2.1), chacun des  $f^{-1}(\mathrm{D}(h_{ik}))$  admet un recouvrement fini par des ouverts affines  $U_{ijk}$  tels que  $\mathrm{A}(\mathrm{U}_{ijk})$  soit une algèbre de type fini sur  $\mathrm{A}(\mathrm{D}(h_{ik})) = \mathrm{A}(\mathrm{W})[\mathrm{I}/h_{ik}]$ , d'où la proposition.

On peut donc dire que la notion de préschéma de type fini sur Y est locale sur Y. Proposition (6.3.3). — Soient X, Y deux schémas affines; pour que X soit de type fini sur Y, il faut et il suffit que A(X) soit une algèbre de type fini sur A(Y).

La condition étant évidemment suffisante, prouvons qu'elle est nécessaire. Posons A=A(Y), B=A(X); en vertu de (6.3.2), il existe un recouvrement ouvert affine fini ( $V_i$ ) de X tel que chacun des anneaux A( $V_i$ ) soit une A-algèbre de type fini. En outre, les  $V_i$  étant quasi-compacts, on peut recouvrir chacun d'eux par un nombre fini d'ouverts de la forme D( $g_{ij}$ ) ⊂  $V_i$ , où  $g_{ij} \in B$ ; si  $\varphi_i$  est l'homomorphisme B→A( $V_i$ ) correspondant à l'injection canonique  $V_i \to X$ , on a  $\mathrm{B}_{g_{ij}} = (\mathrm{A}(\mathrm{V}_i))_{\varphi_i(g_{ij})} = \mathrm{A}(\mathrm{V}_i)[\mathrm{I}/\varphi_i(g_{ij})]$ , donc  $B_{g_{ij}}$  est une A-algèbre de type fini. On peut donc se ramener au cas où  $V_i = D(g_i)$  avec  $g_i \in B$ . Par hypothèse, il existe une partie finie  $F_i$  de B et un entier  $n_i \geqslant 0$  tels que  $B_{g_i}$  soit l'algèbre engendrée sur A par les éléments  $b_i/g_i^n$ , où  $b_i$  parcourt  $F_i$ . Comme les  $g_i$  sont en nombre fini, on peut d'ailleurs supposer tous les  $n_i$  égaux à un même entier n: En outre, comme les D( $g_i$ ) forment un recouvrement de X, l'idéal engendré dans B par les  $g_i$  est égal à B, autrement dit, il existe des  $h_i \in B$  tels que  $\sum_{i} h_i g_i = 1$ . Soit alors F la partie finie de B, réunion des  $F_i$ , de l'ensemble des  $g_i$  et de l'ensemble des  $h_i$ ; montrons que le sous-anneau  $B' = A[F]$  de B est égal à B. Par hypothèse, pour tout  $b \in B$  et tout i, l'image canonique de b dans  $B_{g_i}$  est de la forme  $b'_i / g'_i m_i$ , où  $b'_i \in B'$ ; en multipliant les  $b'_i$  par des puissances convenables des  $g_i$ , on peut encore supposer tous les  $m_i$  égaux à un même entier m. Par définition des anneaux de fractions, il y a donc un entier N (dépendant de b) tel que N≥m et  $g'_i b \in B'$  pour tout i; or, dans l'anneau  $B'$ , les  $g'_i$  engendrent l'idéal  $B'$ , puisqu'il en est ainsi des  $g_i$  (les  $h_i$  appartenant à  $B'$ ); il y a donc des  $c_i \in B'$  tels que  $\sum_{i} c_i g'_i = 1$ , d'où  $b = \sum_{i} c_i g'_i b \in B'$ , C.Q.F.D.

Proposition (6.3.4). — (i) Toute immersion fermée est de type fini.

(ii) Le composé de deux morphismes de type fini est de type fini.

(iii) Si $f: \mathbf{X} \to \mathbf{X}'$, $g: \mathbf{Y} \to \mathbf{Y}'$ sont deux S-morphismes de type fini, $f \times_{\mathrm{sg}} g$ est de type fini.

(iv) Si $f: \mathbf{X} \to \mathbf{Y}$ est un S-morphisme de type fini, $f_{(\mathbb{S}')}$ est de type fini pour toute extension $g: \mathbf{S}' \to \mathbf{S}$ du préschéma de base.

(v) Si le composé gof de deux morphismes est de type fini, et si g est séparé, f est de type fini.

(vi) Si un morphisme f est de type fini, il en est de même de  $f_{red}$ .

En vertu de (5.5.12), il suffit de démontrer (i), (ii) et (iv).

Pour établir (i), on peut se borner au cas d'une injection canonique X→Y, X étant un sous-préschéma fermé de Y ; en outre (6.3.2), on peut supposer Y affine, auquel cas X est aussi affine (4.2.3) et son anneau est isomorphe à un anneau quotient A/Im, où A est l'anneau de Y et Im un idéal de A; comme A/Im est de type fini sur A, la conclusion en résulte.

Démontrons maintenant (ii). Soient $f: \mathrm{X} \to \mathrm{Y}$, $g: \mathrm{Y} \to \mathrm{Z}$ deux morphismes de type fini, et soit U un ouvert affine de Z; $g^{-1}(\mathrm{U})$ admet un recouvrement fini par des ouverts affines $\mathrm{V}_i$ tels que $\mathrm{A}(\mathrm{V}_i)$ soit une algèbre de type fini sur $\mathrm{A}(\mathrm{U})$ (6.3.2); de même,

chacun des $f^{-1}(\mathbf{V}_i)$ admet un recouvrement fini par des ouverts affines $\mathbf{W}_{ij}$ tels que $\mathbf{A}(\mathbf{W}_{ij})$ soit une algèbre de type fini sur $\mathbf{A}(\mathbf{V}_i)$, et par suite aussi une algèbre de type fini sur $\mathbf{A}(\mathbf{U})$; d'où la conclusion.

Enfin, pour démontrer (iv), on peut se borner au cas où S=Y; en effet,  $f_{(S')}$  est aussi égal à  $f_{(\mathrm{Y}_{(\mathrm{s}')})}$ , f étant considéré comme un Y-morphisme, et l'extension de la base étant  $Y_{(S')} \to Y$  (3.3.9). Soient alors p, q les projections  $X_{(S')} \to X$  et  $X_{(S')} \to S'$ . Soit V un ouvert affine dans S;  $f^{-1}(V)$  est réunion finie d'ouverts affines  $W_i$  dont chacun est tel que  $A(W_i)$  soit une algèbre de type fini sur  $A(V)$  (6.3.2). Soit  $V'$  un ouvert affine de  $S'$  contenu dans  $g^{-1}(V)$ ; comme  $f\circ p = g\circ q$ ,  $q^{-1}(V')$  est contenu dans la réunion des  $p^{-1}(W_i)$ ; d'autre part, l'intersection  $p^{-1}(W_i)\cap q^{-1}(V')$  s'identifie au produit  $W_i\times_VV'$  (3.2.7), qui est un schéma affine d'anneau isomorphe à  $A(W_i)\otimes_{A(V)}A(V')$  (3.2.2); ce dernier étant par hypothèse une algèbre de type fini sur  $A(V')$ , la proposition est démontrée.

Corollaire (6.3.5). — Soit $f: \mathbf{X} \to \mathbf{Y}$ un morphisme d'immersion. Si l'espace sous-jacent à Y (resp. X) est localement noethérien (resp. noethérien), $f$ est de type fini.

On peut toujours supposer Y affine (6.3.2) ; si l'espace sous-jacent à Y est localement noethérien, on peut en outre le supposer noethérien et alors l'espace sous-jacent à X, qui en est un sous-espace, est noethérien. Autrement dit, on peut supposer Y affine et l'espace sous-jacent à X noethérien ; il existe alors un recouvrement de X par un nombre fini d'ouverts affines  $\mathrm{D}(g_{i})\subset\mathrm{Y}$ , où  $g_{i}\in\mathrm{A}(\mathrm{Y})$ , tels que  $\mathrm{X}\cap\mathrm{D}(g_{i})$  soit fermé dans  $\mathrm{D}(g_{i})$  (donc un schéma affine (4.2.3)), puisque X est localement fermé dans Y (4.1.3). Alors  $\mathrm{A}(\mathrm{X}\cap\mathrm{D}(g_{i}))$  est une algèbre de type fini sur  $\mathrm{A}(\mathrm{D}(g_{i}))$ , d'après (6.3.4, (i)) et (6.3.3), et  $\mathrm{A}(\mathrm{D}(g_{i}))=\mathrm{A}(\mathrm{Y})_{g_{i}}=\mathrm{A}(\mathrm{Y})[\mathrm{I}/g_{i}]$  est de type fini sur  $\mathrm{A}(\mathrm{Y})$ , ce qui achève la démonstration.

Corollaire (6.3.6). — Soient $f: \mathrm{X} \to \mathrm{Y}$, $g: \mathrm{Y} \to \mathrm{Z}$ deux morphismes. Si gof est de type fini, et si X est noethérien, ou $\mathrm{X} \times_{\mathrm{Z}} \mathrm{Y}$ localement noethérien, f est de type fini.

Cela résulte aussitôt de la démonstration de (5.5.12) et de (6.3.5) appliquée au morphisme d'immersion $\Gamma_{f}$.

Proposition (6.3.7). — Soit $f: \mathbf{X} \to \mathbf{Y}$ un morphisme de type fini; si Y est noethérien (resp. localement noethérien), X est noethérien (resp. localement noethérien).

On peut se borner à faire la démonstration lorsque Y est noethérien. Alors Y est réunion finie d'ouverts affines  $V_{i}$  tels que les  $A(V_{i})$  soient des anneaux noethériens. En vertu de (6.3.2), chacun des  $f^{-1}(V_{i})$  est réunion d'un nombre fini d'ouverts affines  $W_{ij}$  tels que les  $A(W_{ij})$  soient des algèbres de type fini sur  $A(V_{i})$, donc des anneaux noethériens ; cela prouve que X est noethérien.

Corollaire (6.3.8). — Soit X un préschéma de type fini sur S. Pour toute extension de la base S'→S telle que S' soit noethérien (resp. localement noethérien), X$_{(S')}$ est noethérien (resp. localement noethérien).

$$
(6. 3. 7), \mathrm{X} _ {\left(\mathrm{S} ^ {\prime}\right)}
$$

$$
\mathbf {S} ^ {\prime}
$$

$$
(6. 3. 4, (\mathrm{iv}))
$$

On peut encore dire que dans un produit  $X \times_{s} Y$  de S-préschémas, si l'un des

facteurs X, Y est de type fini sur S et l'autre noethérien (resp. localement noethérien), alors  $X \times_{s} Y$  est noethérien (resp. localement noethérien).

Corollaire (6.3.9). — Soit X un préschéma de type fini sur un préschéma localement noethérien S. Alors tout S-morphisme $f: \mathbf{X} \to \mathbf{Y}$ est de type fini.

En effet, on peut supposer S noethérien ; si $\varphi : \mathrm{X} \to \mathrm{S}$, $\psi : \mathrm{Y} \to \mathrm{S}$ sont les morphismes structuraux, on a $\varphi = \psi \circ f$, et X est noethérien en vertu de (6.3.7); $f$ est donc de type fini en vertu de (6.3.6).

Proposition (6.3.10). — Soit $f: \mathbf{X} \to \mathbf{Y}$ un morphisme de type fini. Pour que $f$ soit surjectif, il faut et il suffit que, pour tout corps algébriquement clos $\Omega$, l'application $\mathbf{X}(\Omega) \to \mathbf{Y}(\Omega)$ correspondant à $f(3.4.1)$ soit surjective.

La condition est suffisante, comme on le voit en considérant pour tout  $y \in Y$ , une extension algébriquement close  $\Omega$  de  $\boldsymbol{k}(y)$ , et le diagramme commutatif

![](images/page_145_image_5.jpg)

(cf. (3.5.3)). Inversement, supposons $f$ surjective, et soit $g: \{\xi\} = \operatorname{Spec}(\Omega) \to Y$ un morphisme, $\Omega$ étant un corps algébriquement clos. Si on considère le diagramme

$$
\begin{array}{c} \mathbf {X} \longleftarrow \mathbf {X} _ {(\Omega)} \\ f \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad f _ {(\Omega)} \\ \mathbf {Y} \leftarrow \operatorname{Spec} (\Omega) \end{array}
$$

il suffit donc de montrer qu'il existe dans $\mathbf{X}_{(\Omega)}$ un point rationnel sur $\Omega$ (3.3.14, 3.4.3 et 3.4.4). Comme $f$ est surjectif, $\mathbf{X}_{(\Omega)}$ n'est pas vide (3.5.10) et comme $f$ est de type fini, il en est de même de $f_{(\Omega)}$ (6.3.4, (iv)); donc $\mathbf{X}_{(\Omega)}$ contient un ouvert affine non vide Z tel que $\mathrm{A}(\mathrm{Z})$ soit une algèbre de type fini non nulle sur $\Omega$. En vertu du th. des zéros de Hilbert [21], il existe un $\Omega$-homomorphisme $\mathrm{A}(\mathrm{Z}) \to \Omega$, donc une section de $\mathbf{X}_{(\Omega)}$ au-dessus de $\operatorname{Spec}(\Omega)$, ce qui démontre la proposition.

## 6.4. Préschémas algébriques.

Définition (6.4.1). — Étant donné un corps K, on appelle K-préschéma algébrique un préschéma X de type fini sur K ; K est appelé le corps de base de X. Si en outre X est un schéma (ou, ce qui revient au même (5.5.8), si X est un K-schéma), on dit aussi que X est un K-schéma algébrique.

Tout K-préschéma algébrique est noethérien (6.3.7).

Proposition (6.4.2). — Soit X un K-préschéma algébrique. Pour qu'un point  $x \in X$  soit fermé, il faut et il suffit que  $\mathbf{k}(x)$  soit une extension algébrique de K, de degré fini.

On peut supposer X affine, l'anneau A de X étant une K-algèbre de type fini. En effet, les ouverts affines U de X tels que A(U) soit une K-algèbre de type fini forment un recouvrement de X (6.3.1). Les points fermés de X sont alors les points tels que  $j_{x}$  soit

un idéal maximal de A, autrement dit tels que  $A/j_{x}$  soit un corps (nécessairement égal à  $\boldsymbol{k}(x)$ ). Comme  $A/j_{x}$  est une K-algèbre de type fini, on voit que si x est fermé,  $\boldsymbol{k}(x)$  est un corps qui est une algèbre de type fini sur K, donc nécessairement une K-algèbre de rang fini [21]. Inversement, si  $\boldsymbol{k}(x)$  est de rang fini sur K, il en est de même de  $A/j_{x}\subset\boldsymbol{k}(x)$  et comme tout anneau intègre qui est une K-algèbre de rang fini est un corps, on a  $A/j_{x}=\boldsymbol{k}(x)$ , donc x est fermé.

Corollaire (6.4.3). — Soient K un corps algébriquement clos, X un K-préschéma algébrique ; les points fermés de X sont alors les points rationnels sur K (3.4.4) et s'identifient canoniquement aux points de X à valeurs dans K.

Proposition (6.4.4). — Soit X un préschéma algébrique sur un corps K. Les propriétés suivantes sont équivalentes:

a) X est artinien.

b) L'espace sous-jacent à X est discret.

c) L'espace sous-jacent à X n'a qu'un nombre fini de points fermés.

c') L'espace sous-jacent à X est fini.

d) Les points de X sont fermés.

e) X est isomorphe à Spec(A), où A est une K-algèbre de rang fini.

Comme X est noethérien, il résulte de (6.2.2) que les conditions $a$, $b$, $d$ sont équivalentes et entraînent $c$ et $c'$; par ailleurs, il est clair que $e$ entraîne $a$. Reste à voir que $c$ entraîne $d$ et $e$; on peut se borner au cas où X est affine. Alors A(X) est une K-algèbre de type fini (6.3.3), donc un anneau de Jacobson ([1], p. 3-11 et 3-12), dans lequel il n'y a par hypothèse qu'un nombre fini d'idéaux maximaux. Comme une intersection finie d'idéaux premiers ne peut être un idéal premier que si elle est égale à l'un d'eux, tout idéal premier de A(X) est donc maximal, d'où $d$). En outre, on sait alors (6.2.2) que A(X) est une K-algèbre artinienne de type fini, donc nécessairement de rang fini [21].

(6.4.5) Lorsque les conditions de (6.4.4) sont satisfaites, on dit que X est un schéma fini sur K (cf. (II, 6.1.1)), ou un K-schéma fini, de rang [A : K] que l'on note aussi $rg_{K}(X)$; si X, Y sont deux schémas finis sur K, on a

(6.4.5.1)

$$
r g _ {\mathrm{K}} (\mathbf {X} \amalg \mathbf {Y}) = r g _ {\mathrm{K}} (\mathbf {X}) + r g _ {\mathrm{K}} (\mathbf {Y})\tag{6.4.5.2}
$$

$$
r g _ {\mathrm{K}} (\mathbf {X} \times_ {\mathrm{K}} \mathbf {Y}) = r g _ {\mathrm{K}} (\mathbf {X}) r g _ {\mathrm{K}} (\mathbf {Y})
$$

comme il résulte de (3.2.2).

Corollaire (6.4.6). — Soit X un schéma fini sur un corps K. Pour toute extension K' de K,  $X \otimes_{K} K'$  est un schéma fini sur  $K'$ , et son rang sur  $K'$  est égal au rang de X sur K.

En effet, si $\mathbf{A} = \mathbf{A}(\mathbf{X})$, on a $[\mathbf{A}\otimes_{\mathbb{K}}\mathbf{K}':\mathbf{K}'] = [\mathbf{A}:\mathbf{K}]$.

Corollaire (6.4.7). — Soit X un schéma fini sur un corps K; on pose  $n = \sum_{x \in X} [k(x) : K]_s$

(on rappelle que si $\mathbf{K}'$ est une extension de $\mathbf{K}$, $[\mathbf{K}':\mathbf{K}]_s$ est le rang séparable de $\mathbf{K}'$ sur $\mathbf{K}$, rang de la plus grande extension algébrique séparable de $\mathbf{K}$ contenue dans $\mathbf{K}'$);

alors, pour toute extension algébriquement close $\Omega$ de K, l'espace sous-jacent à X$\otimes_{K}$$\Omega$ a exactement $n$ points, qui s'identifient aux points de X à valeurs dans $\Omega$.

On peut évidemment se borner au cas où l'anneau A = A(X) est local (6.2.2); soient m son idéal maximal, L = A/m son corps résiduel, extension algébrique de K. Les points de X à valeurs dans Ω correspondent alors biunivoquement aux Ω-sections de  $X \otimes_{K} \Omega$  (3.4.1 et 3.3.14), et aussi aux K-homomorphismes de L dans Ω (1.7.3), d'où la proposition (Bourbaki, Alg., chap. V, § 7, n° 5, prop. 8), compte tenu de (6.4.3).

(6.4.8) Le nombre $n$ défini dans (6.4.7) s'appelle le rang séparable de A (ou de X) sur K, ou aussi le nombre géométrique de points de X; il est donc égal au nombre d'éléments de $\mathbf{X}(\Omega)_{\mathbb{K}}$. Il résulte aussitôt de cette définition que, pour toute extension $\mathbf{K}'$ de K, $\mathbf{X} \otimes_{\mathbb{K}} \mathbf{K}'$ a même nombre géométrique de points que X. Si on désigne ce nombre par $n(\mathbf{X})$, il est clair que si X, Y sont deux schémas finis sur K, on a

$$
n (\mathbf {X} \amalg \mathbf {Y}) = n (\mathbf {X}) + n (\mathbf {Y}).
$$

Sous les mêmes hypothèses, on a aussi

## (6.4.8.2)

$$
n (\mathbf {X} \times_ {\mathrm{K}} \mathbf {Y}) = n (\mathbf {X}) n (\mathbf {Y})
$$

comme il résulte aussitôt de l'interprétation de $n(\mathbf{X})$ comme nombre d'éléments de $\mathbf{X}(\Omega)_{\mathrm{K}}$ et de la formule (3.4.3.1).

Proposition (6.4.9). — Soient K un corps, X, Y deux K-préschémas algébriques, $f: \mathbf{X} \to \mathbf{Y}$ un K-morphisme, $\Omega$ une extension algébriquement close de K, de degré de transcendance infini sur K. Pour que $f$ soit surjectif, il faut et il suffit que l'application $\mathbf{X}(\Omega)_{\mathbf{K}} \to \mathbf{Y}(\Omega)_{\mathbf{K}}$ correspondant à $f(3.4.1)$ soit surjective.

La nécessité résulte de (6.3.10), en remarquant que $f$ est nécessairement de type fini (6.3.9). Pour voir que la condition est suffisante, on raisonne comme dans (6.3.10), en remarquant que pour tout $y\in\mathbf{Y}$, $\boldsymbol{k}(y)$ est une extension de K de type fini, et par suite est K-isomorphe à un sous-corps de $\Omega$.

Remarque (6.4.10). — Nous verrons au chap. IV que la conclusion de (6.4.9) est encore valable sans hypothèse relative au degré de transcendance de Ω sur K.

Proposition (6.4.11). — Si $f: \mathbf{X} \to \mathbf{Y}$ est un morphisme de type fini, pour tout $y \in \mathbf{Y}$, la fibre $f^{-1}(y)$ est un préschéma algébrique sur le corps résiduel $\boldsymbol{k}(y)$ et pour tout $x \in f^{-1}(y)$, $\boldsymbol{k}(x)$ est une extension de type fini de $\boldsymbol{k}(y)$.

Comme $f^{-1}(y) = \mathbf{X} \otimes_{\mathbf{Y}} \boldsymbol{k}(y)$ (3.6.3), la proposition résulte de (6.3.4, (iv)) et de (6.3.3).

Proposition (6.4.12). — Soient $f: \mathrm{X} \to \mathrm{Y}$, $g: \mathrm{Y}' \to \mathrm{Y}$ deux morphismes; posons $\mathrm{X}' = \mathrm{X} \times_{\mathrm{Y}} \mathrm{Y}'$ et soit $f' = f_{(\mathrm{Y}')}: \mathrm{X}' \to \mathrm{Y}'$. Soit $y' \in \mathrm{Y}'$, $y = g(y')$; si la fibre $f^{-1}(y)$ est un schéma algébrique fini sur $\mathbf{k}(y)$, alors la fibre $f'^{-1}(y')$ est un schéma algébrique fini sur $\mathbf{k}(y')$, ayant même rang et même nombre géométrique de points que $f^{-1}(y)$.

Compte tenu de la transitivité des fibres (3.6.5), cela résulte aussitôt de (6.4.6) et (6.4.8).

(6.4.13) La prop. (6.4.11) montre que les morphismes de type fini correspondent intuitivement aux « familles algébriques de variétés algébriques », les points de Y jouant

le rôle de « paramètres », ce qui donne à ces morphismes une signification « géométrique ». Les morphismes qui ne sont pas de type fini interviendront surtout par la suite dans les questions de « changement du préschéma de base », par exemple par localisation ou complétion.

## 6.5. Détermination locale d'un morphisme.

Proposition (6.5.1). — Soient X, Y deux S-préschémas, Y étant de type fini sur S; soient  $x \in X$ ,  $y \in Y$  au-dessus d'un même point  $s \in S$ .

(i) Si deux S-morphismes $f = (\psi, \theta), f' = (\psi', \theta')$ de X dans Y sont tels que $\psi(x) = \psi'(x) = y$, et que les $\mathcal{O}_s$-homomorphismes (locaux) $\theta_x^\sharp$ et $\theta_x'^\sharp$ de $\mathcal{O}_y$ dans $\mathcal{O}_x$ soient identiques, $f$ et $f'$ coïncident dans un voisinage ouvert de $x$.

(ii) Supposons en outre S localement noethérien. Pour tout $\mathcal{O}_{s}$-homomorphisme local $\varphi: \mathcal{O}_{y} \to \mathcal{O}_{x}$, il existe un voisinage ouvert U de $x$ dans X et un S-morphisme $f = (\psi, \theta)$ de U dans Y tels que $\psi(x) = y$ et $\theta_{x}^{\#} = \varphi$.

(i) La question étant locale sur S, X et Y, on peut supposer S, X, Y affines d'anneaux respectifs A, B, C, $f$ et $f'$ étant de la forme $(^a\varphi, \widetilde{\varphi})$ et $(^a\varphi', \widetilde{\varphi}')$ respectivement, où $\varphi$ et $\varphi'$ sont deux A-homomorphismes de C dans B tels que $\varphi^{-1}(\mathbf{j}_x) = \varphi'^{-1}(\mathbf{j}_x) = \mathbf{j}_y$, et les homomorphismes $\varphi_x$ et $\varphi'_x$ de $C_y$ dans $B_x$, déduits de $\varphi$ et $\varphi'$, sont identiques; on peut en outre supposer que C est une A-algèbre de type fini. Soient $c_i$ ($1 \leqslant i \leqslant n$) des générateurs de la A-algèbre C, et posons $b_i = \varphi(c_i)$, $b_i' = \varphi'(c_i)$; par hypothèse, on a $b_i / 1 = b_i' / 1$ dans l'anneau de fractions $B_x$ ($1 \leqslant i \leqslant n$). Cela signifie qu'il existe des éléments $s_i \in B - j_x$ tels que $s_i(b_i - b_i') = 0$ pour $1 \leqslant i \leqslant n$, et on peut évidemment supposer tous les $s_i$ égaux à un même élément $g \in B - j_x$. On en conclut que l'on a $b_i / 1 = b_i' / 1$ pour $1 \leqslant i \leqslant n$ dans l'anneau de fractions $B_g$; si $i_g$ est l'homomorphisme canonique $B \to B_g$, on a par suite $i_g \circ \varphi = i_g \circ \varphi'$; donc les restrictions de $f$ et $f'$ à $D(g)$ sont identiques.

(ii) On peut se ramener à la même situation que dans (i), et supposer en outre que l'anneau A est noethérien. Soient $c_i$ ($i \leqslant i \leqslant n$) des générateurs de la A-algèbre C, et soit $\alpha: \mathrm{A}[\mathrm{X}_1, \ldots, \mathrm{X}_n] \to \mathrm{C}$ l'homomorphisme de l'algèbre de polynômes $\mathrm{A}[\mathrm{X}_1, \ldots, \mathrm{X}_n]$ sur C transformant $\mathrm{X}_i$ en $c_i$ pour $i \leqslant i \leqslant n$. Soit d'autre part $i_y$ l'homomorphisme canonique $\mathrm{C} \to \mathrm{C}_y$, et considérons l'homomorphisme composé

$$
\beta : \mathrm{A} [ \mathrm{X} _ {1}, \dots , \mathrm{X} _ {n} ] \xrightarrow {\alpha} \mathrm{C} \xrightarrow {i _ {y}} \mathrm{C} _ {y} \xrightarrow {\varphi} \mathrm{B} _ {x}.
$$

Désignons par $\mathfrak{a}$ le noyau de $\beta$; comme A est noethérien, il en est de même de $\mathrm{A}[\mathrm{X}_1,\ldots ,\mathrm{X}_n]$, et par suite $\mathfrak{a}$ admet un système fini de générateurs $\mathbf{Q}_j(\mathbf{X}_1,\dots ,\mathbf{X}_n)$ ($\mathfrak{i}\leqslant j\leqslant m$). D'autre part, chacun des éléments $\varphi (i_y(c_i))$ peut s'écrire $b_{i} / s_{i}$, où $b_{i}\in \mathbf{B}$ et $s_i\notin \mathfrak{j}_x$; on peut en outre supposer tous les $s_i$ égaux à un même élément $g\in \mathbf{B}-\mathfrak{j}_x$. Cela étant, on a par hypothèse $\mathbf{Q}_j(b_1 / g,\ldots ,b_n / g) = 0$ dans $\mathbf{B}_x$; posons

$$
\mathrm{Q} _ {j} \left(\mathrm{X} _ {1} / \mathrm{T}, \dots , \mathrm{X} _ {n} / \mathrm{T}\right) = \mathrm{P} _ {j} \left(\mathrm{X} _ {1}, \dots , \mathrm{X} _ {n}, \mathrm{T}\right) / \mathrm{T} ^ {k j}
$$

où  $P_{j}$  est homogène de degré  $k_{j}$ . Soit alors  $d_{j}=\mathrm{P}_{j}(b_{1},\ldots,b_{n},g)\in\mathrm{B}$ . Par hypothèse, on a  $t_{j}d_{j}=0$  pour un  $t_{j}\in\mathrm{B}-\mathrm{j}_{x}$  ( $1\leqslant j\leqslant m$ ), et on peut évidemment supposer tous les  $t_{j}$

égaux à un même élément $h \in \mathbf{B} - \mathbf{j}_x$; on en conclut que $\mathrm{P}_j(hb_1, \ldots, hb_n, hg) = 0$ pour $1 \leqslant j \leqslant m$. Cela étant, considérons l'homomorphisme $\rho$ de $\mathrm{A}[\mathrm{X}_1, \ldots, \mathrm{X}_n]$ dans l'anneau de fractions $\mathrm{B}_{hg}$ qui applique $\mathrm{X}_i$ sur $hb_i / hg (1 \leqslant i \leqslant n)$; l'image de $a$ par cet homomorphisme est $o$, et il en est a fortiori de même de l'image par $\rho$ du noyau $\alpha^{-1}(o)$. Donc $\rho$ se factorise en $\mathrm{A}[\mathrm{X}_1, \ldots, \mathrm{X}_n] \xrightarrow{\alpha} \mathrm{C} \xrightarrow{\gamma} \mathrm{B}_{hg}$, avec $\gamma(c_i) = hb_i / hg$, et il est clair que si $i_x$ est l'homomorphisme canonique $\mathrm{B}_{hg} \to \mathrm{B}_x$, le diagramme

$$
\begin{array}{c} \mathbf {C} \xrightarrow {\gamma} \mathbf {B} _ {h g} \\ i _ {y} \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \mathbf {C} _ {y} \xrightarrow [ \varphi ]{} \mathbf {B} _ {x} \end{array}\tag{6.5.1.1}
$$

est commutatif ; on a donc $\varphi = \gamma_x$, et comme $\varphi$ est un homomorphisme local, $^a\gamma(x) = y$; $f = (^a\gamma, \widetilde{\gamma})$ est donc un S-morphisme du voisinage D(hg) de $x$ dans Y qui répond à la question.

Corollaire (6.5.2). — Sous les hypothèses de (6.5.1, (ii)), si en outre X est de type fini sur S, on peut supposer le morphisme f de type fini.

Cela résulte de (6.3.6).

Corollaire (6.5.3). — Supposons vérifiées les hypothèses de (6.5.1, (ii)), et supposons en outre que Y soit intègre, et φ un homomorphisme injectif. Alors on peut supposer que  $f=(^{a}\Upsilon,\widetilde{\Upsilon})$  où γ est injectif.

En effet, on peut supposer C intègre (5.1.4), donc  $i_{y}$  injectif; il résulte alors du diagramme (6.5.1.1) que  $\gamma$  est injectif.

Proposition (6.5.4). — Soient $f = (\psi, \theta): X \to Y$ un morphisme de type fini, $x$ un point de $X$, $y = \psi(x)$.

(i) Pour que $f$ soit une immersion locale au point $x$ (4.5.1), il faut et il suffit que $\theta_x^\#: \mathcal{O}_y \to \mathcal{O}_x$ soit surjectif.

(ii) On suppose en outre Y localement noethérien. Pour que $f$ soit un isomorphisme local au point $x$ (4.5.2), il faut et il suffit que $\theta_x^\sharp$ soit un isomorphisme.

(ii) En vertu de (6.5.1), il existe alors un voisinage ouvert V de y et un morphisme  $g: V \to X$  tels que  $g \circ f$  (resp.  $f \circ g$ ) soit défini et coïncide avec l'identité dans un voisinage de x (resp. y), d'où on tire aisément que f est un isomorphisme local.

(i) La question étant locale sur X et Y, on peut supposer X et Y affines, d'anneaux respectifs A, B ; on a $f = (^{a}\varphi, \widetilde{\varphi})$, où $\varphi$ est un homomorphisme d'anneaux $\mathrm{B} \to \mathrm{A}$ qui fait de A une B-algèbre de type fini ; on a $\varphi^{-1}(\mathrm{j}_{x}) = \mathrm{j}_{y}$, et l'homomorphisme $\varphi_{x}: \mathrm{B}_{y} \to \mathrm{A}_{x}$ déduit de $\varphi$ est surjectif. Soit $(t_{i}) (\mathrm{i} \leqslant i \leqslant n)$ un système de générateurs de la B-algèbre A ; l'hypothèse sur $\varphi_{x}$ implique qu'il existe des $b_{i} \in \mathrm{B}$ et un $c \in \mathrm{B} - \mathrm{j}_{y}$ tels que, dans l'anneau de fractions $\mathrm{A}_{x}$, on ait $t_{i}/\mathrm{i} = \varphi(b_{i})/\varphi(c)$ pour $\mathrm{i} \leqslant i \leqslant n$. Par suite $(\mathrm{i}.3.3)$, il existe $a \in \mathrm{A} - \mathrm{j}_{x}$ tel que, si l'on pose $g = a\varphi(c)$, on ait aussi $t_{i}/\mathrm{i} = a\varphi(b_{i})/g$ dans l'anneau de fractions $\mathrm{A}_{g}$. Cela étant, il existe par hypothèse un polynôme $\mathbf{Q}(\mathbf{X}_{1}, \ldots, \mathbf{X}_{n})$ à coefficients dans l'anneau $\varphi(\mathbf{B})$,

tel que $a = \mathbf{Q}(t_1, \ldots, t_n)$; posons $\mathbf{Q}(\mathbf{X}_1 / \mathbf{T}, \ldots, \mathbf{X}_n / \mathbf{T}) = \mathbf{P}(\mathbf{X}_1, \ldots, \mathbf{X}_n, \mathbf{T}) / \mathbf{T}^m$, où P est homogène de degré $m$. Dans l'anneau $\mathbf{A}_g$, on a

$$
a / \mathrm{I} = a ^ {m} \mathrm{P} (\varphi (b _ {1}), \dots , \varphi (b _ {n}), \varphi (c)) / g ^ {m} = a ^ {m} \varphi (d) / g ^ {m}
$$

où $d \in \mathbf{B}$. Comme, dans $\mathbf{A}_g$, $g / \mathrm{I} = (a / \mathrm{I})(\varphi(c) / \mathrm{I})$ est inversible par définition, il en est de même de $a / \mathrm{I}$ et de $\varphi(c) / \mathrm{I}$, et on peut donc écrire $a / \mathrm{I} = (\varphi(d) / \mathrm{I})(\varphi(c) / \mathrm{I})^{-m}$. On en conclut que $\varphi(d) / \mathrm{I}$ est aussi inversible dans $\mathbf{A}_g$. Posons alors $h = cd$; comme $\varphi(h) / \mathrm{I}$ est inversible dans $\mathbf{A}_g$, l'homomorphisme composé $\mathbf{B} \xrightarrow{\varphi} \mathbf{A} \to \mathbf{A}_g$ se factorise en $\mathbf{B} \to \mathbf{B}_h \xrightarrow{\gamma} \mathbf{A}_g$ (0, 1.2.4). Montrons que $\gamma$ est surjectif; il suffit de vérifier que l'image de $\mathbf{B}_h$ dans $\mathbf{A}_g$ contient les $t_i / \mathrm{I}$ et $(g / \mathrm{I})^{-1}$. Or, on a $(g / \mathrm{I})^{-1} = (\varphi(c) / \mathrm{I})^{m-1}(\varphi(d) / \mathrm{I})^{-1} = \gamma(c^m / h)$, et $a / \mathrm{I} = \gamma(d^{m+1} / h^m)$, donc $(a\varphi(b_i)) / \mathrm{I} = \gamma(b_i d^{m+1} / h^m)$, et comme $t_i / \mathrm{I} = (a\varphi(b_i) / \mathrm{I})(g / \mathrm{I})^{-1}$, notre assertion est démontrée. Le choix de $h$ implique que $\psi(\mathbf{D}(g)) \subset \mathbf{D}(h)$, et la restriction de $f$ à $\mathbf{D}(g)$ est égale à $(^a\gamma, \widetilde{\gamma})$; comme $\gamma$ est surjectif, cette restriction est une immersion fermée de $\mathbf{D}(g)$ dans $\mathbf{D}(h)$ (4.2.3).

Corollaire (6.5.5). — Soit $f = (\psi, \theta) : X \to Y$ un morphisme de type fini. On suppose X irréductible, on désigne par $x$ son point générique, et on pose $y = \psi(x)$.

(i) Pour que $f$ soit une immersion locale en un point de $\mathbf{X}$, il faut et il suffit que $\theta_x^\sharp : \mathcal{O}_y \to \mathcal{O}_x$ soit surjectif.

(ii) On suppose de plus Y irréductible et localement noethérien. Pour que $f$ soit un isomorphisme local en un point de X, il faut et il suffit que $y$ soit le point générique de Y (ou, ce qui revient au même (0, 2.1.4) que $f$ soit un morphisme dominant) et que $\theta_{x}^{\sharp}$ soit un isomorphisme (autrement dit, que $f$ soit birationnel (2.2.9)).

Il est clair que (i) résulte de (6.5.4, (i)) compte tenu de ce que tout ouvert non vide de X contient x ; de même (ii) résulte de (6.5.4, (ii)).

## 6.6. Morphismes quasi-compacts et morphismes localement de type fini.

Définition (6.6.1). — On dit qu'un morphisme $f: \mathbf{X} \to \mathbf{Y}$ est quasi-compact si l'image réciproque par $f$ de tout ouvert quasi-compact de $\mathbf{Y}$ est quasi-compacte.

Soit B une base de la topologie de Y formée d'ouverts quasi-compacts (par exemple d'ouverts affines) ; pour que f soit quasi-compact, il faut et il suffit que l'image réciproque par f de tout ensemble de B soit quasi-compacte (ou, ce qui revient au même, réunion finie d'ouverts affines), car tout ouvert quasi-compact de Y est réunion finie d'ensembles de B. Par exemple, si X est quasi-compact et Y affine, alors tout morphisme  $f: X \to Y$  est quasi-compact : en effet, X est réunion finie d'ensembles ouverts affines  $U_i$ , et pour tout ouvert affine V de Y,  $U_i \cap f^{-1}(V)$  est affine (5.5.10), donc quasi-compact.

Si $f: \mathbf{X} \to \mathbf{Y}$ est un morphisme quasi-compact, il est clair que pour tout ouvert V de Y, la restriction de $f$ à $f^{-1}(\mathbf{V})$ est un morphisme quasi-compact $f^{-1}(\mathbf{V}) \to \mathbf{V}$. Inversement, si $(\mathbf{U}_{\alpha})$ est un recouvrement ouvert de Y et $f: \mathbf{X} \to \mathbf{Y}$ un morphisme tel que les restrictions $f^{-1}(\mathbf{U}_{\alpha}) \to \mathbf{U}_{\alpha}$ soient quasi-compactes, alors $f$ est quasi-compact.

Définition (6.6.2). — On dit qu'un morphisme $f: \mathbf{X} \to \mathbf{Y}$ est localement de type fini si, pour tout $x \in \mathbf{X}$, il existe un voisinage ouvert $\mathbf{U}$ de $x$ et un voisinage ouvert $\mathbf{V} \supset f(\mathbf{U})$ de $y$ tels que la

restriction de f à U soit un morphisme de type fini de U dans V. On dit alors aussi que X est un préschéma localement de type fini sur Y, ou un Y-préschéma localement de type fini.

Il résulte aussitôt de (6.3.2) que si $f$ est localement de type fini, alors, pour tout ouvert $W$ de $Y$, la restriction de $f \dot{a} f^{-1}(W)$ est un morphisme $f^{-1}(W) \to W$ qui est localement de type fini.

Si Y est localement noethérien et si X est localement de type fini sur Y, X est localement noethérien en vertu de (6.3.7).

Proposition (6.6.3). — Pour qu'un morphisme $f: \mathbf{X} \to \mathbf{Y}$ soit de type fini, il faut et il suffit qu'il soit quasi-compact et localement de type fini.

La nécessité des conditions est immédiate, vu (6.3.1) et la remarque suivant (6.6.1). Inversement, supposons ces conditions satisfaites et soit U un ouvert affine de Y, d'anneau A; pour tout $x \in f^{-1}(U)$, il y a par hypothèse un voisinage $V(x) \subset f^{-1}(U)$ de $x$ et un voisinage $W(x) \subset U$ de $y = f(x)$, contenant $f(V(x))$ et tel que la restriction de $f$ à $V(x)$ soit un morphisme $V(x) \to W(x)$ qui est de type fini. En remplaçant $W(x)$ par un voisinage $W_1(x) \subset W(x)$ de $x$ de la forme $D(g)$ (avec $g \in A$), et $V(x)$ par $V(x) \cap f^{-1}(W_1(x))$, on peut supposer que $W(x)$ est de la forme $D(g)$, donc de type fini sur U (puisque son anneau s'écrit $A[1/g]$); par suite $V(x)$ est de type fini sur U. En outre $f^{-1}(U)$ est quasi-compact par hypothèse, donc réunion d'un nombre fini d'ouverts $V(x_i)$, ce qui achève la démonstration.

Proposition (6.6.4). — (i) Une immersion X→Y est quasi-compacte si elle est fermée, ou si l'espace sous-jacent à Y est localement noethérien ou si l'espace sous-jacent à X est noethérien.

(ii) Le composé de deux morphismes quasi-compacts est quasi-compact.

(iii) Si $f: \mathbf{X} \to \mathbf{Y}$ est un S-morphisme quasi-compact, il en est de même de $f_{(\mathbb{S}')}: \mathbf{X}_{(\mathbb{S}')} \to \mathbf{Y}_{(\mathbb{S}')}$ pour toute extension $g: \mathbf{S}' \to \mathbf{S}$ du préschéma de base.

(iv) Si $f: \mathbf{X} \to \mathbf{X}'$ et $g: \mathbf{Y} \to \mathbf{Y}'$ sont deux S-morphismes quasi-compacts, $f \times_{\mathbb{S}} g$ est quasi-compact.

(v) Si le composé de deux morphismes $f: \mathrm{X} \to \mathrm{Y}$, $g: \mathrm{Y} \to \mathrm{Z}$ est quasi-compact et si g est séparé, ou l'espace sous-jacent à X localement noethérien, f est quasi-compact.

(vi) Pour qu'un morphisme $f$ soit quasi-compact, il faut et il suffit que $f_{\text{red}}$ le soit.

On notera que (vi) est évident puisque la propriété d'être quasi-compact pour un morphisme ne dépend que de l'application continue correspondante des espaces sous-jacents. Démontrons de même la partie de (v) correspondant au cas où l'espace sous-jacent X est supposé localement noethérien. Posons $h = g \circ f$, et soit U un ouvert quasi-compact dans Y; $g(U)$ est quasi-compact (non nécessairement ouvert) dans Z, donc contenu dans une réunion finie d'ouverts quasi-compacts $V_j$ (2.1.3), et $f^{-1}(U)$ est par suite contenu dans la réunion des $h^{-1}(V_j)$, qui sont des sous-espaces quasi-compacts de X, donc des sous-espaces noethériens. On en conclut (0, 2.2.3) que $f^{-1}(U)$ est un espace noethérien, et a fortiori quasi-compact.

Pour prouver les autres assertions, il suffit de démontrer (i), (ii) et (iii) (5.5.12). Or, (ii) est évidente, et (i) résulte de (6.3.5) lorsque l'espace Y est localement noethérien ou l'espace X noethérien et est évidente pour une immersion fermée. Pour établir (iii),

153

on peut se borner au cas où $S = Y$ (3.3.11); posons $f' = f_{(S')}$, et soit $U'$ un ouvert quasi-compact dans $S'$. Pour tout $s' \in U'$, soit $T$ un voisinage ouvert affine de $g(s')$ dans $S$, et soit $W$ un voisinage ouvert affine de $s'$ contenu dans $U' \cap g^{-1}(T)$; il suffira de montrer que $f'^{-1}(W)$ est quasi-compact; autrement dit, on peut se ramener à prouver que lorsque $S$ et $S'$ sont affines, l'espace sous-jacent à $X \times_s S'$ est quasi-compact. Mais comme $X$ est alors par hypothèse réunion finie d'ouverts affines $V_j$, $X \times_s S'$ est réunion des espaces sous-jacents aux schémas affines $V_j \times_s S'$ (3.2.2 et 3.2.7), ce qui achève de prouver la proposition.

On notera aussi que si  $X=X^{\prime}$$\Pi X^{\prime\prime}$  est somme de deux préschémas, un morphisme  $f:X\to Y$  est quasi-compact si et seulement si ses restrictions à  $X^{\prime}$  et  $X^{\prime\prime}$  le sont.

Proposition (6.6.5). — Soit $f: \mathbf{X} \to \mathbf{Y}$ un morphisme quasi-compact. Pour que $f$ soit dominant, il faut et il suffit que pour tout point générique $y$ d'une composante irréductible de $\mathbf{Y}$, $f^{-1}(y)$ contienne le point générique d'une composante irréductible de $\mathbf{X}$.

Il est immédiat que la condition est suffisante (sans supposer $f$ quasi-compact). Pour voir qu'elle est nécessaire, considérons un voisinage ouvert affine U de $y$; $f^{-1}(U)$ est quasi-compact, donc réunion finie d'ouverts affines $V_i$, et l'hypothèse que $f$ est dominant implique que $y$ appartient à l'adhérence dans U d'un des $f(V_i)$. On peut évidemment supposer X et Y réduits ; comme l'adhérence dans X d'une composante irréductible de $V_i$ est une composante irréductible de X (0, 2.1.6), on peut remplacer X par $V_i$, Y par le sous-préschéma fermé réduit de U ayant $\overline{f(V_i)} \cap U$ pour espace sous-jacent (5.2.1), et on est ainsi ramené à démontrer la proposition lorsque $X = \text{Spec}(A)$ et $Y = \text{Spec}(B)$ sont affines et réduits. Comme $f$ est dominant, B est alors un sous-anneau de A (1.2.7), et la proposition résulte alors du fait que tout idéal premier minimal de B est l'intersection de B et d'un idéal premier minimal de A (0, 1.5.8).

Proposition (6.6.6). — (i) Toute immersion locale est localement de type fini.

(ii) Si deux morphismes $f: \mathbf{X} \to \mathbf{Y}, g: \mathbf{Y} \to \mathbf{Z}$ sont localement de type fini, il en est de même de gof.

(iii) Si $f: \mathbf{X} \to \mathbf{Y}$ est un S-morphisme localement de type fini, $f_{(\mathbf{S}')}: \mathbf{X}_{(\mathbf{S}')} \to \mathbf{Y}_{(\mathbf{S}')}$ est localement de type fini pour toute extension $\mathbf{S}' \to \mathbf{S}$ du préschéma de base.

(iv) Si $f: \mathbf{X} \to \mathbf{X}'$ et $g: \mathbf{Y} \to \mathbf{Y}'$ sont deux S-morphismes localement de type fini, $f \times_{\mathrm{sg}}$ est localement de type fini.

(v) Si le composé gof de deux morphismes est localement de type fini, f est localement de type fini.

(vi) Si un morphisme $f$ est localement de type fini, il en est de même de $f_{\mathrm{red}}$.

En vertu de (5.5.12), il suffit de démontrer (i), (ii) et (iii). Si $j: \mathbf{X} \to \mathbf{Y}$ est une immersion locale, pour tout $x \in \mathbf{X}$, il y a un voisinage ouvert $V$ de $j(x)$ dans $Y$ et un voisinage ouvert $U$ de $x$ dans $X$ tels que la restriction de $j$ à $U$ soit une immersion fermée $U \to V$ (4.5.1), donc cette restriction est de type fini. Pour établir (ii), considérons un point $x \in X$; il y a par hypothèse un voisinage ouvert $W$ de $g(f(x))$ et un voisinage ouvert $V$ de $f(x)$ tels que $g(V) \subset W$ et que $V$ soit de type fini sur $W$; en outre $f^{-1}(V)$ est localement de type fini sur $V$ (6.6.2), donc il y a un voisinage ouvert $U$ de $x$ qui

est contenu dans $f^{-1}(\mathbf{V})$ et de type fini sur $\mathbf{V}$; par suite on a $g(f(\mathbf{U})) \subset \mathbf{W}$ et $\mathbf{U}$ est de type fini sur $\mathbf{W}$ (6.3.4, (ii)). Enfin, pour démontrer (iii), on peut se borner au cas où $\mathbf{Y} = \mathbf{S}$ (3.3.11); pour tout $x' \in \mathbf{X}' = \mathbf{X}_{(\mathbf{S}')}$, soient $x$ l'image de $x'$ dans $\mathbf{X}$, $s$ l'image de $x$ dans $\mathbf{S}$, $\mathbf{T}$ un voisinage ouvert de $s$, $\mathbf{T}'$ son image réciproque dans $\mathbf{S}'$, $\mathbf{U}$ un voisinage ouvert de $x$ dont l'image est contenue dans $\mathbf{T}$ et qui est de type fini sur $\mathbf{T}$; alors $\mathbf{U} \times_{\mathbb{S}} \mathbf{T}' = \mathbf{U} \times_{\mathbb{T}} \mathbf{T}'$ est un voisinage ouvert de $x'$ (3.2.7) qui est de type fini sur $\mathbf{T}'$ (6.3.4, (iv)).

Corollaire (6.6.7). — Soient X, Y deux S-préschémas qui sont localement de type fini sur S. Si S est localement noethérien,  $X \times_{s} Y$  est localement noethérien.

En effet, X étant localement de type fini sur S, est localement noethérien, et  $X \times_{s} Y$  est localement de type fini sur X, donc est aussi localement noethérien.

Remarque (6.6.8). — La proposition (6.3.10) et sa démonstration s'étendent aussitôt au cas où l'on suppose seulement que le morphisme $f$ est localement de type fini. De même, les propositions (6.4.2) et (6.4.9) restent valables lorsqu'on suppose que les préschémas X, Y qui figurent dans leur énoncé sont seulement localement de type fini sur le corps K.

## § 7. APPLICATIONS RATIONNELLES

## 7.1. Applications rationnelles et fonctions rationnelles.

(7.1.1) Soient X, Y deux préschémas, U, V, deux ouverts denses dans X, f (resp. g) un morphisme de U (resp. V) dans Y ; nous dirons que f et g sont équivalents s'ils coïncident dans un ouvert dense dans U∩V. Comme une intersection finie d'ouverts denses dans X est un ouvert dense dans X, il est clair que cette relation est une relation d'équivalence.

Définition (7.1.2). — Étant donnés deux préschémas X, Y, on appelle application rationnelle de X dans Y une classe d'équivalence de morphismes de parties ouvertes denses de X dans Y, pour la relation définie dans (7.1.1). Si X et Y sont des S-préschémas, on dit qu'une telle classe est une S-application rationnelle s'il existe un représentant de cette classe qui est un S-morphisme. On appelle S-section rationnelle de X toute S-application rationnelle de S dans X. On appelle fonction rationnelle sur un préschéma X toute X-section rationnelle du X-préschéma  $X \otimes_{Z} Z[T]$  (où T est une indéterminée).

Par abus de langage, lorsqu'il ne sera question que de S-préschémas, on dira « application rationnelle » au lieu de « S-application rationnelle » si aucune confusion ne peut en résulter.

Soient $f$ une application rationnelle de $\mathbf{X}$ dans $\mathbf{Y}$, $\mathbf{U}$ un ouvert de $\mathbf{X}$; si $f_{1}, f_{2}$ sont des morphismes appartenant à la classe $f$, définis respectivement dans des ouverts denses $\mathbf{V}$, $\mathbf{W}$ de $\mathbf{X}$, les restrictions $f_{1}|(\mathbf{U} \cap \mathbf{V}), f_{2}|(\mathbf{U} \cap \mathbf{W})$ coïncident dans $\mathbf{U} \cap \mathbf{V} \cap \mathbf{W}$ qui est dense dans $\mathbf{U}$; la classe de morphismes $f$ définit donc une application rationnelle de $\mathbf{U}$ dans $\mathbf{Y}$, appelée restriction de $f$ à $\mathbf{U}$ et notée $f|\mathbf{U}$.

Si, à tout S-morphisme $f: \mathbf{X} \to \mathbf{Y}$, on fait correspondre la S-application rationnelle

à laquelle appartient $f$, on définit une application canonique de $\mathrm{Hom}_{\mathrm{s}}(\mathrm{X},\mathrm{Y})$ dans l'ensemble des S-applications rationnelles de $\mathbf{X}$ dans $\mathbf{Y}$. On désigne par $\Gamma_{\mathrm{rat}}(\mathbf{X}/\mathbf{Y})$ l'ensemble des Y-sections rationnelles de $\mathbf{X}$, et on a donc une application canonique $\Gamma(\mathbf{X}/\mathbf{Y})\to\Gamma_{\mathrm{rat}}(\mathbf{X}/\mathbf{Y})$. Il est clair en outre que si $\mathbf{X}$ et $\mathbf{Y}$ sont deux S-préschémas, l'ensemble des S-applications rationnelles de $\mathbf{X}$ dans $\mathbf{Y}$ s'identifie canoniquement à $\Gamma_{\mathrm{rat}}((\mathbf{X}\times_{\mathrm{s}}\mathbf{Y})/\mathbf{X})$ (3.3.14).

(7.1.3) Il résulte aussitôt de (7.1.2) et de (3.3.14) que les fonctions rationnelles sur X s'identifient canoniquement aux classes d'équivalence des sections du faisceau structural $\mathcal{O}_{\mathrm{X}}$ au-dessus d'ouverts partout denses de X, deux telles sections étant équivalentes si elles coïncident dans un ouvert partout dense contenu dans l'intersection de leurs ensembles de définition. Il en résulte en particulier que les fonctions rationnelles sur X forment un anneau R(X).

(7.1.4) Lorsque X est un préschéma irréductible, tout ouvert non vide est dense dans X ; on peut encore dire que les ouverts non vides de X sont les voisinages ouverts du point générique x de X. Dire que deux morphismes de parties ouvertes non vides de X dans Y sont équivalents signifie donc dans ce cas qu'ils ont même germe au point x. Autrement dit, les applications rationnelles (resp. S-applications rationnelles) X→Y s'identifient aux germes de morphismes (resp. de S-morphismes) de parties ouvertes non vides de X dans Y au point générique x de X. En particulier :

Proposition (7.1.5). — Si X est un préschéma irréductible, l'anneau R(X) des fonctions rationnelles sur X s'identifie canoniquement à l'anneau local $\mathcal{O}_{x}$ du point générique $x$ de X. C'est un anneau local de dimension o, et par suite un anneau local artinien lorsque X est noethérien; c'est un corps lorsque X est intègre, et il s'identifie au corps des fractions de A(X) lorsqu'en outre X est un schéma affine.

Vu ce qui précède et l'identification des fonctions rationnelles aux sections de $\mathcal{O}_{\mathrm{X}}$ au-dessus d'un ouvert partout dense, la première assertion n'est autre que la définition de la fibre d'un faisceau en un point. Pour les autres assertions, on peut se borner au cas où X est affine d'anneau A; alors $\mathbf{j}_x$ est le nilradical de A, et $\mathcal{O}_x$ est donc de dimension o; si A est intègre, $\mathbf{j}_x = (0)$, et $\mathcal{O}_x$ est donc le corps des fractions de A. Enfin, si A est noethérien, on sait ([11], p. 127, cor. 4) que $\mathbf{j}_x$ est nilpotent et $\mathcal{O}_x = \mathrm{A}_x$ artinien.

Si X est intègre, l'anneau $\mathcal{O}_{z}$ est intègre pour tout $z\in\mathbf{X}$; tout ouvert affine U contenant $z$ contient aussi $x$, et R(U), égal au corps des fractions de A(U), s'identifie donc à R(X); on en conclut que R(X) s'identifie aussi au corps des fractions de $\mathcal{O}_{z}$: l'identification canonique de $\mathcal{O}_{z}$ à un sous-anneau de R(X) consiste à faire correspondre à tout germe de section $s\in\mathcal{O}_{z}$ l'unique fonction rationnelle sur X, classe d'une section de $\mathcal{O}_{X}$ (nécessairement définie sur un ouvert partout dense) ayant pour germe $s$ au point $z$.

(7.1.6) Supposons maintenant que X ait un nombre fini de composantes irréductibles  $X_{i}$  ( $i \leqslant i \leqslant n$ ) (ce qui est le cas lorsque l'espace sous-jacent à X est noethérien); soit  $X_{i}'$  l'ouvert de X, complémentaire par rapport à  $X_{i}$  de la réunion des  $X_{j} \cap X_{i}$  pour  $j \neq i$ ;  $X_{i}'$  est irréductible, son point générique  $x_{i}$  est le point générique de  $X_{i}$, et les  $X_{i}'$  sont deux à deux disjoints, leur réunion étant dense dans X (0, 2.1.6). Pour

tout ouvert partout dense U de X,  $U_{i}=U\cap X_{i}^{\prime}$  est un ouvert non vide dense dans  $X_{i}^{\prime}$ , les  $U_{i}$  étant deux à deux sans point commun, donc  $U^{\prime}=\bigcup_{i}U_{i}^{\prime}$  est dense dans X. Se donner un morphisme de  $U^{\prime}$  dans Y revient à se donner (arbitrairement) un morphisme de chacun des  $U_{i}$  dans Y. Donc :

Proposition (7.1.7). — Soient X, Y deux préschémas (resp. S-préschémas) tels que X ait un nombre fini de composantes irréductibles  $X_{i}$ , de points génériques  $x_{i}$  ( $i \leqslant i \leqslant n$ ). Si  $R_{i}$  est l'ensemble des germes de morphismes (resp. S-morphismes) de parties ouvertes de X dans Y au point  $x_{i}$ , l'ensemble des applications rationnelles (resp. S-applications rationnelles) de X dans Y s'identifie au produit des  $R_{i}$  ( $i \leqslant i \leqslant n$ ).

Corollaire (7.1.8). — Soit X un préschéma noethérien. L'anneau des fonctions rationnelles sur X est un anneau artinien, dont les composants locaux sont les anneaux $\mathcal{O}_{xi}$ des points génériques $x_{i}$ des composantes irréductibles de X.

Corollaire (7.1.9). — Soient A un anneau noethérien, et soit X=Spec(A). Si Q est le complémentaire de la réunion des idéaux premiers minimaux de A, l'anneau des fonctions rationnelles sur X s'identifie canoniquement à l'anneau de fractions Q $^{-1}$ A.

Cela résultera du lemme suivant :

Lemme (7.1.9.1). — Pour qu'un élément $f\in\mathbf{A}$ soit tel que $\mathbf{D}(f)$ soit partout dense dans $\mathbf{X}$, il faut et il suffit que $f\in\mathbf{Q}$; tout ouvert dense dans $\mathbf{X}$ contient un ouvert de la forme $\mathbf{D}(f)$, où $f\in\mathbf{Q}$.

En effet, supposons ce lemme démontré; l'anneau des sections $\Gamma(\mathrm{D}(f),\mathcal{O}_{\mathrm{X}})$ s'identifiant à $A_{f}$ (1.3.6 et 1.3.7), il résulte du fait que les $\mathrm{D}(f)$ avec $f\in\mathbf{Q}$ forment un ensemble cofinal dans l'ensemble ordonné (pour $\supset$) des ouverts denses dans X, et de la déf. (7.1.1) que l'anneau des fonctions rationnelles sur X s'identifie à la limite inductive des $A_{f}$ pour $f\in\mathbf{Q}$ (pour la relation de préordre « g est multiple de f »), c'est-à-dire à $\mathbf{Q}^{-1}\mathbf{A}$ (0, 1.4.5).

Pour démontrer (7.1.9.1), désignons encore par  $X_{i}$  les composantes irréductibles de  $X(1 \leqslant i \leqslant n)$ ; si  $D(f)$  est dense dans  $X$ ,  $D(f) \cap X_{i} \neq \emptyset$  pour  $1 \leqslant i \leqslant n$  et réciproquement; mais cela signifie que  $f \notin p_{i}$  pour  $1 \leqslant i \leqslant n$ , en posant  $p_{i} = j(X_{i})$ , et comme les  $p_{i}$  sont les idéaux premiers minimaux de A (1.1.14), les relations  $f \notin p_{i}(1 \leqslant i \leqslant n)$  équivalent à  $f \in Q$ , d'où la première assertion du lemme. D'autre part, si U est un ouvert dense dans X, le complémentaire de U est un ensemble de la forme V(a), où a est un idéal qui n'est contenu dans aucun des  $p_{i}$ ; il n'est donc pas contenu dans leur réunion ([10], p. 13), et il existe donc un  $f \in a$  appartenant à Q; d'où  $D(f) \subset U$ , ce qui achève la démonstration.

(7.1.10) Supposons de nouveau X irréductible, de point générique $x$. Comme tout ouvert non vide U de X contient $x$, et par suite contient aussi tout $z \in \mathbf{X}$ tel que $x \in \overline{\{z\}}$, tout morphisme $\mathrm{U} \to \mathrm{Y}$ peut se composer avec le morphisme canonique $\operatorname{Spec}(\mathcal{O}_x) \to \mathbf{X}$ (2.4.1); et deux morphismes dans Y de deux parties ouvertes non vides de X, qui coïncident dans une partie ouverte non vide de X donnent par composition le même morphisme $\operatorname{Spec}(\mathcal{O}_x) \to \mathrm{Y}$. Autrement dit, à toute application rationnelle de X dans Y correspond ainsi un morphisme $\operatorname{Spec}(\mathcal{O}_x) \to \mathrm{Y}$ bien déterminé.

Proposition (7.1.11). — Soient X, Y deux S-préschémas; on suppose X irréductible, de point générique x, et Y de type fini sur S. Deux S-applications rationnelles de X dans Y, auxquelles correspond le même S-morphisme  $\operatorname{Spec}(\mathcal{O}_{x})\to\mathbf{Y}$  sont identiques. Si on suppose de plus S localement noethérien, tout S-morphisme de  $\operatorname{Spec}(\mathcal{O}_{x})$  dans Y correspond à une S-application rationnelle (et une seule) de X dans Y.

Compte tenu de ce que tout ouvert non vide de X est partout dense, cela résulte aussitôt de (6.5.1).

Corollaire (7.1.12). — On suppose S localement noethérien, et les autres hypothèses de (7.1.11) satisfaites. Les S-applications rationnelles de X dans Y s'identifient alors aux points du S-préschéma Y, à valeurs dans le S-préschéma $\operatorname{Spec}(\mathcal{O}_{x})$.

Cela n'est autre que (7.1.11), avec la terminologie introduite dans (3.4.1).

Corollaire (7.1.13). — On suppose remplies les conditions de (7.1.12). Soit s l'image de x dans S. La donnée d'une S-application rationnelle de X dans Y équivaut à la donnée d'un point y de Y au-dessus de s, et d'un $\mathcal{O}_s$-homomorphisme local $\mathcal{O}_y \to \mathcal{O}_x = \mathrm{R}(\mathrm{X})$.

Cela résulte de (7.1.11) et de (2.4.4).

En particulier :

Corollaire (7.1.14). — Sous les conditions de (7.1.12), les S-applications rationnelles de X dans Y ne dépendent (pour Y donné) que du S-préschéma $\operatorname{Spec}(\mathcal{O}_{x})$ et en particulier restent les mêmes lorsqu'on remplace X par $\operatorname{Spec}(\mathcal{O}_{z})$, pour tout $z \in \mathbf{X}$.

En effet, comme $z \in \overline{\{x\}}$, $x$ est le point générique de $Z = \text{Spec}(\mathcal{O}_z)$, et $\mathcal{O}_{X,x} = \mathcal{O}_{Z,x}$. Lorsque $X$ est intègre, $R(X) = \mathcal{O}_x = k(x)$ est un corps (7.1.5); les corollaires précédents se spécialisent alors en :

Corollaire (7.1.15). — On suppose vérifiées les conditions de (7.1.12) et en outre que X est intègre. Soit s l'image de x dans S. Alors les S-applications rationnelles de X dans Y s'identifient aux points géométriques de  $\mathrm{Y}\otimes_{\mathrm{S}}\mathbf{k}(s)$  à valeurs dans l'extension  $\mathrm{R}(\mathrm{X})$  de  $\mathbf{k}(s)$ , autrement dit chacune d'elles équivaut à la donnée d'un point  $y\in Y$  au-dessus de s et d'un  $\mathbf{k}(s)$ -monomorphisme de  $\mathbf{k}(y)$  dans  $\mathbf{k}(x)=\mathrm{R}(\mathrm{X})$ .

Les points de Y au-dessus de s s'identifient en effet à ceux de  $\mathbf{Y}\otimes_{\mathbb{S}}\boldsymbol{k}(s)$  (3.6.3) et les  $O_{s}$ -homomorphismes locaux  $\mathcal{O}_{y}\to\mathrm{R}(\mathbf{X})$  aux  $\boldsymbol{k}(s)$ -monomorphismes  $\boldsymbol{k}(y)\to\mathrm{R}(\mathbf{X})$ . Plus particulièrement :

Corollaire (7.1.16). — Soient k un corps, X, Y deux préschémas algébriques (6.4.1) sur k; on suppose en outre X intègre. Alors les k-applications rationnelles de X dans Y s'identifient aux points géométriques de Y à valeurs dans l'extension R(X) de k (3.4.4).

## 7.2. Domaine de définition d'une application rationnelle.

(7.2.1) Soient X, Y deux préschémas, $f$ une application rationnelle de X dans Y. On dit que $f$ est définie en un point $x \in X$ s'il existe un ensemble ouvert partout dense U contenant $x$ et un morphisme U$\rightarrow$Y appartenant à la classe d'équivalence $f$. L'ensemble des points $x \in X$ où $f$ est définie est appelé le domaine de définition de $f$; il est clair que c'est un ouvert partout dense dans X.

Proposition (7.2.2). — Soient X, Y deux S-préschémas, tels que X soit réduit et Y séparé sur S. Soit f une S-application rationnelle de X dans Y,  $U_{0}$  son domaine de définition. Il existe alors un S-morphisme et un seul  $U_{0} \rightarrow Y$  appartenant à la classe f.

Comme pour tout morphisme  $U \rightarrow Y$  appartenant à la classe f, on a nécessairement  $U \subset U_{0}$ , il est clair que la proposition sera conséquence du

Lemme (7.2.2.1). — Sous les hypothèses de (7.2.2), soient  $U_{1}$ ,  $U_{2}$  deux ouverts partout denses de X,  $f_{i}: U_{i} \to Y (i=1,2)$  deux S-morphismes tels qu'il existe un ouvert  $V \subset U_{1} \cap U_{2}$  dense dans X et dans lequel  $f_{1}$  et  $f_{2}$  coïncident. Alors  $f_{1}$  et  $f_{2}$  coïncident dans  $U_{1} \cap U_{2}$ .

On peut évidemment se borner au cas où  $X = U_{1} = U_{2}$ . Comme X (donc V) est réduit, X est le plus petit sous-préschéma fermé de X majorant V (5.2.2). Soit  $g = (f_{1}, f_{2})_{\mathrm{S}} : \mathrm{X} \to \mathrm{Y} \times_{\mathrm{S}} \mathrm{Y}$ ; comme par hypothèse la diagonale  $T = \Delta_{\mathrm{Y}}(\mathrm{Y})$  est un sous-préschéma fermé de  $Y \times_{\mathrm{S}} Y$ ,  $Z = g^{-1}(T)$  est un sous-préschéma fermé de X (4.4.1). Si  $h : V \to Y$  est la restriction commune de  $f_{1}$  et  $f_{2}$  à V, la restriction de g à V est  $g' = (h, h)_{\mathrm{S}}$ , qui se factorise en  $g' = \Delta_{\mathrm{Y}}^{-1}(T) = Y$ , on a  $g'^{-1}(T) = V$ , et par suite Z est un sous-préschéma fermé de X induisant V, donc majorant V, ce qui entraîne Z = X. De la relation  $g^{-1}(T) = X$ , on déduit (4.4.1) que g se factorise en  $\Delta_{Y} \circ f$ , où f est un morphisme  $X \to Y$ , ce qui entraîne par définition du morphisme diagonal que  $f_{1} = f_{2} = f$ .

Il est clair que le morphisme  $U_{0}\rightarrow Y$  défini dans (7.2.2) est l'unique morphisme de la classe f qui ne puisse être prolongé à un morphisme d'une partie ouverte de X contenant strictement  $U_{0}$ . Sous les hypothèses de (7.2.2), on peut donc identifier les applications rationnelles de X dans Y aux morphismes non prolongables (à des ouverts strictement plus grands) d'ouverts partout denses de X dans Y. Avec cette identification, la prop. (7.2.2) entraîne :

Corollaire (7.2.3). — Les hypothèses sur X et Y étant celles de (7.2.2), soit U un ouvert partout dense de X. Il existe une correspondance biunivoque canonique entre les S-morphismes de U dans Y et les S-applications rationnelles de X dans Y définies en tous les points de U.

En vertu de (7.2.2), pour tout S-morphisme $f$ de U dans Y, il existe en effet une S-application rationnelle et une seule $\overline{f}$ de X dans Y qui prolonge $f$.

Corollaire (7.2.4). — Soient S un schéma, X un S-préschéma réduit, Y un S-schéma, $f: U \to Y$ un S-morphisme d'un ouvert dense U de X dans Y. Si $\overline{f}$ est la Z-application rationnelle de X dans Y qui prolonge $f$, $\overline{f}$ est un S-morphisme (et est par suite la S-application rationnelle de X dans Y prolongeant $f$).

En effet, si $\varphi: \mathbf{X} \to \mathbf{S}$, $\psi: \mathbf{Y} \to \mathbf{S}$ sont les morphismes structuraux, $\mathbf{U}_0$ le domaine de définition de $\overline{f}, j$ l'injection $\mathbf{U}_0 \to \mathbf{X}$, il suffit de prouver que $\psi \circ \overline{f} = \varphi \circ j$, ce qui résulte aussitôt de (7.2.2.1), puisque $f$ est un S-morphisme.

Corollaire (7.2.5). — Soient X, Y deux S-préschémas; on suppose X réduit, X et Y séparés sur S. Soient $p: \mathrm{Y} \to \mathrm{X}$ un S-morphisme (faisant de Y un X-préschéma), U un ouvert partout dense de X, f une U-section de Y; alors l'application rationnelle $\overline{f}$ de X dans Y prolongeant f est une X-section rationnelle de Y.

Il faut prouver que $p_{0}\overline{f}$ est l'identité dans le domaine de définition de $\overline{f}$; puisque X est séparé sur S, cela résulte encore de (7.2.2.1).

Corollaire (7.2.6). — Soient X un préschéma réduit, U un ouvert partout dense de X. Il y a correspondance biunivoque canonique entre les sections de $\mathcal{O}_{\mathrm{X}}$ au-dessus de U et les fonctions rationnelles $f$ sur X définies en tout point de U.

Compte tenu de (7.2.3), (7.1.2) et (7.1.3), il suffit de remarquer que le X-pré-schéma  $X \otimes_{Z} Z[T]$  est séparé au-dessus de X (5.5.1, (iv)).

Corollaire (7.2.7). — Soient Y un préschéma réduit,  $f: X \to Y$  un morphisme séparé, U un ouvert partout dense de Y,  $g: U \to f^{-1}(U)$  une U-section de  $f^{-1}(U)$, Z le sous-préschéma réduit de X ayant  $g(U)$  pour espace sous-jacent (5.2.1). Pour que g soit restriction d'une Y-section de X (autrement dit (7.2.5) pour que l'application rationnelle de Y dans X prolongeant g soit partout définie), il faut et il suffit que la restriction de f à Z soit un isomorphisme de Z sur Y.

La restriction de $f$ à $f^{-1}(\mathrm{U})$ est un morphisme séparé (5.5.1, (i)), donc $g$ est une immersion fermée (5.4.6), et par suite $g(\mathrm{U}) = \mathrm{Z} \cap f^{-1}(\mathrm{U})$ et le sous-préschéma induit par $Z$ sur l'ouvert $g(\mathrm{U})$ de $Z$ est identique au sous-préschéma fermé de $f^{-1}(\mathrm{U})$ associé à $g$ (5.2.1). Il est clair alors que la condition de l'énoncé est suffisante, car si elle est remplie et si $f_{\mathbb{Z}}: \mathbb{Z} \to \mathbb{Y}$ est la restriction de $f$ à $Z$ et $\overline{g}: \mathbb{Y} \to \mathbb{Z}$ l'isomorphisme réciproque, $\overline{g}$ prolonge $g$. Inversement, si $g$ est restriction à $U$ d'une Y-section $h$ de $X$, $h$ est une immersion fermée (5.4.6), donc $h(\mathbb{Y})$ est fermé, et comme il est contenu dans $Z$, il est égal à $Z$, et il résulte de (5.2.1) que $h$ est nécessairement un isomorphisme de $Y$ sur le sous-préschéma fermé $Z$ de $X$.

(7.2.8) Soient X, Y deux S-préschémas, X étant supposé réduit et Y séparé sur S. Soit f une S-application rationnelle de X dans Y, et soit x un point de X ; on peut composer f avec le S-morphisme canonique  $\operatorname{Spec}(\mathcal{O}_{x})\to\mathbf{X}$  (2.4.1) pourvu que la trace sur  $\operatorname{Spec}(\mathcal{O}_{x})$  du domaine de définition de f soit dense dans  $\operatorname{Spec}(\mathcal{O}_{x})$  (identifié à l'ensemble des  $z\in X$  tels que  $x\in\overline{\{z\}}$  (2.4.2)). Ceci aura lieu dans les cas suivants :

$\mathbf{1}^{\circ}\mathbf{X}$ est irréductible (donc intègre), car alors le point générique $\xi$ de X est le point générique de $\operatorname{Spec}(\mathcal{O}_{x})$; comme le domaine de définition U de f contient $\xi$, $\mathrm{U} \cap \operatorname{Spec}(\mathcal{O}_{x})$ contient $\xi$, donc est dense dans $\operatorname{Spec}(\mathcal{O}_{x})$.

$2^{0}$ X est localement noethérien ; notre assertion résulte en effet alors du

Lemme (7.2.8.1). — Soient X un préschéma dont l'espace sous-jacent est localement noethérien, x un point de X. Les composantes irréductibles de  $\operatorname{Spec}(\mathcal{O}_{x})$  sont les traces sur  $\operatorname{Spec}(\mathcal{O}_{x})$  des composantes irréductibles de X contenant x. Pour qu'un ouvert U ⊂ X soit tel que U ∩  $\operatorname{Spec}(\mathcal{O}_{x})$  soit dense dans  $\operatorname{Spec}(\mathcal{O}_{x})$ , il faut et il suffit qu'il rencontre les composantes irréductibles de X contenant x (ce qui a lieu en particulier si U est dense dans X).

La seconde assertion résulte évidemment de la première, et il suffit donc de démontrer celle-ci. Comme $\operatorname{Spec}(\mathcal{O}_x)$ est contenu dans tout ouvert affine U contenant $x$, et que les composantes irréductibles de U contenant $x$ sont les traces sur U des composantes irréductibles de X contenant $x$ (0, 2.1.6), on peut supposer X affine d'anneau A. Comme les idéaux premiers de $\mathbf{A}_x$ correspondent biunivoquement aux idéaux premiers

de A contenus dans  $j_{x}$  (0, 1.2.6), les idéaux premiers minimaux de  $A_{x}$  correspondent aux idéaux premiers minimaux de A contenus dans  $j_{x}$ , d'où le lemme (1.1.14).

Cela étant, supposons que l'on soit dans l'un des deux cas précités. Si U est le domaine de définition de la S-application rationnelle $f$, désignons par $f'$ l'application rationnelle de $\operatorname{Spec}(\mathcal{O}_x)$ dans Y qui coïncide (compte tenu de (2.4.2)) avec $f$ dans $\mathrm{U} \cap \operatorname{Spec}(\mathcal{O}_x)$; nous dirons que cette application rationnelle est induite par $f$.

Proposition (7.2.9). — Soient S un préschéma localement noethérien, X un S-préschéma réduit, Y un S-schéma de type fini. On suppose en outre X irréductible ou localement noethérien. Soient alors f une S-application rationnelle de X dans Y, x un point de X. Pour que f soit définie au point x, il faut et il suffit que l'application rationnelle $f'$ de $\text{Spec}(\mathcal{O}_x)$ dans Y, induite par f (7.2.8), soit un morphisme.

La condition étant évidemment nécessaire (puisque $\operatorname{Spec}(\mathcal{O}_x)$ est contenu dans tout ouvert contenant $x$), prouvons qu'elle est suffisante. En vertu de (6.5.1), il existe un voisinage ouvert U de $x$ dans X et un S-morphisme $g$ de U dans Y, induisant $f'$ sur $\operatorname{Spec}(\mathcal{O}_x)$. Si X est irréductible, U est dense dans X, et en vertu de (7.2.3) on peut supposer que $g$ est une S-application rationnelle. En outre, le point générique de X appartient à $\operatorname{Spec}(\mathcal{O}_x)$ et au domaine de définition de $f$, donc $f$ et $g$ coïncident en ce point, et par suite dans un ensemble ouvert non vide de X (6.5.1). Mais comme $f$ et $g$ sont des S-applications rationnelles, elles sont identiques (7.2.3), donc $f$ est définie en $x$.

Si maintenant on suppose X localement noethérien, on peut supposer U noethérien ; il n'y a alors qu'un nombre fini de composantes irréductibles  $X_{i}$  de X contenant x (7.2.8.1), et on peut supposer que ce sont les seules rencontrant U, en remplaçant au besoin U par un ouvert plus petit (puisqu'il n'y a qu'un nombre fini de composantes irréductibles de X rencontrant U, U étant noethérien). On voit alors comme ci-dessus que f et g coïncident dans un ouvert non vide de chacun des  $X_{i}$ . Tenant compte du fait que chacun des  $X_{i}$  est contenu dans  $\overline{U}$ , considérons alors le morphisme  $f_{1}$ , défini dans un ouvert dense de  $\mathrm{U}\cup(\mathrm{X}-\overline{\mathrm{U}})$ , égal à g dans U et à f dans l'intersection de  $X-\overline{U}$  et du domaine de définition de f. Comme  $\mathrm{U}\cup(\mathrm{X}-\overline{\mathrm{U}})$  est dense dans  $X,f_{1}$  et f coïncident dans un ouvert dense de X, et comme f est une application rationnelle, f est une extension de  $f_{1}$  (7.2.3), donc est définie au point x.

## 7.3. Faisceau des fonctions rationnelles.

(7.3.1) Soit X un préschéma. Pour tout ouvert U⊂X, désignons par R(U) l'anneau des fonctions rationnelles sur U (7.1.3); c'est une Γ(U, Ox)-algèbre. En outre, si V⊂U est un second ouvert de X, toute section de Ox au-dessus d'une partie ouverte partout dense de U donne par restriction à V une section au-dessus d'une partie ouverte partout dense de V, et si deux sections coïncident au-dessus d'une partie ouverte partout dense de U, leurs restrictions à V coïncident au-dessus d'une partie ouverte partout dense de V. On définit donc ainsi un di-homomorphisme d'algèbres ρV,U : R(U) → R(V), et il est clair que si U⊃V⊃W sont trois ouverts de X, on a ρW,U = ρW,V∘ρV,U; les R(U) définissent donc un préfaisceau d'algèbres sur X.

Définition (7.3.2). — On appelle faisceau des fonctions rationnelles sur un préschéma X et on désigne par $\mathcal{R}(\mathbf{X})$ la $\mathcal{O}_{\mathbf{X}}$-Algèbre associée au préfaisceau formé des $\mathbf{R}(\mathbf{U})$.

Pour tout préschéma X et tout ouvert U⊂X, il est clair que le faisceau induit $\mathcal{R}(\mathbf{X})|U$ n'est autre que $\mathcal{R}(\mathbf{U})$.

Proposition (7.3.3). — Soit X un préschéma tel que la famille  $(\mathbf{X}_{\lambda})$  de ses composantes irréductibles soit localement finie (ce qui est en particulier le cas lorsque l'espace sous-jacent à X est localement noethérien). Alors le  $\mathcal{O}_{\mathrm{X}}$ -Module  $\mathcal{R}(\mathrm{X})$  est quasi-cohérent, et pour tout ouvert U de X ne rencontrant qu'un nombre fini de composantes  $X_{\lambda}$ ,  $\mathrm{R}(\mathrm{U})$  est égal à  $\Gamma(\mathrm{U}, \mathcal{R}(\mathrm{X}))$  et s'identifie canoniquement au composé direct des anneaux locaux des points génériques des  $X_{\lambda}$  telles que  $U \cap X_{\lambda} \neq \emptyset$ .

On peut évidemment se limiter au cas où X n'a qu'un nombre fini de composantes irréductibles  $X_{i}$ , de points génériques  $x_{i}$  ( $i \leqslant i \leqslant n$ ). Le fait que R(U) est canoniquement identifié au composé direct des  $\mathcal{O}_{x_{i}} = \mathrm{R}(\mathrm{X}_{i})$  tels que  $\mathrm{U} \cap \mathrm{X}_{i} \neq \emptyset$  résulte alors de (7.1.7). Montrons en outre que le préfaisceau U→R(U) vérifie les axiomes des faisceaux, ce qui prouvera que  $\mathrm{R}(\mathrm{U}) = \Gamma(\mathrm{U}, \mathcal{R}(\mathrm{X}))$ . En effet, il vérifie (F 1) d'après ce qui précède. Pour voir qu'il satisfait à (F 2), considérons un recouvrement d'un ouvert U de X par des ouverts  $V_{\alpha} \subset U$ ; si les  $s_{\alpha} \in \mathrm{R}(V_{\alpha})$  sont telles que les restrictions de  $s_{\alpha}$  et  $s_{\beta}$  à  $V_{\alpha} \cap V_{\beta}$  coïncident pour tout couple d'indices, on en conclut que pour tout indice i tel que  $\mathrm{U} \cap X_{i} \neq \emptyset$ , les composantes dans  $\mathrm{R}(X_{i})$  de toutes les  $s_{\alpha}$  telles que  $V_{\alpha} \cap X_{i} \neq \emptyset$  sont les mêmes; désignant par  $t_{i}$  cette composante, il est clair que l'élément de R(U) ayant les  $t_{i}$  pour composantes a pour restriction  $s_{\alpha}$  à chaque  $V_{\alpha}$ . Enfin, pour voir que  $\mathcal{R}(X)$  est quasi-cohérent, on peut se limiter au cas où X=Spec(A) est affine; en prenant pour U les ouverts affines de la forme D(f), où  $f \in A$ , il résulte de ce qui précède et de la définition (1.3.4) que l'on a  $\mathcal{R}(X) = \widetilde{\mathbf{M}}$ , où M est somme directe des A-modules  $A_{x_{i}}$ .

Corollaire (7.3.4). — Soit X un préschéma réduit n'ayant qu'un nombre fini de composantes irréductibles, et soient  $X_{i}$  ( $i \leqslant i \leqslant n$ ) les sous-préschémas fermés réduits de X ayant pour espaces sous-jacents les composantes irréductibles de X (5.2.1). Si  $h_{i}$  est l'injection canonique  $X_{i} \to X$ ,  $\mathcal{R}(X)$  est alors composée directe des  $\mathcal{O}_{X}$ -Algèbres  $(h_{i})_{*}(\mathcal{R}(X_{i}))$ .

Corollaire (7.3.5). — Si X est irréductible, tout $\mathcal{R}(\mathbf{X})$-Module quasi-cohérent $\mathcal{F}$ est un faisceau simple.

Il suffit de montrer que tout $x \in \mathbf{X}$ admet un voisinage $\mathbf{U}$ tel que $\mathcal{F} | \mathbf{U}$ soit un faisceau simple (0, 3.6.2), autrement dit on est ramené au cas où $\mathbf{X}$ est affine ; on peut en outre supposer que $\mathcal{F}$ est le conoyau d'un homomorphisme $(\mathcal{R}(\mathbf{X}))^{(I)} \to (\mathcal{R}(\mathbf{X}))^{(J)}$ (0, 5.1.3), et tout revient à voir que $\mathcal{R}(\mathbf{X})$ est un faisceau simple ; mais cela est évident puisque $\Gamma(\mathbf{U}, \mathcal{R}(\mathbf{X})) = \mathbf{R}(\mathbf{X})$ pour tout ouvert non vide $\mathbf{U}$, $\mathbf{U}$ contenant le point générique de $\mathbf{X}$.

Corollaire (7.3.6). — Si X est irréductible, pour tout $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent $\mathcal{F}$, $\mathcal{F} \otimes_{\mathcal{O}_{\mathrm{X}}} \mathcal{R}(\mathrm{X})$ est un faisceau simple; si en outre X est réduit (donc intègre), $\mathcal{F} \otimes_{\mathcal{O}_{\mathrm{X}}} \mathcal{R}(\mathrm{X})$ est isomorphe à un faisceau de la forme $(\mathcal{R}(\mathrm{X}))^{(1)}$.

La seconde assertion résulte de ce que R(X) est alors un corps.

Proposition (7.3.7). — Supposons que le préschéma X soit localement intègre ou localement

noethérien. Alors $\mathcal{R}(\mathbf{X})$ est une $\mathcal{O}_{\mathrm{X}}$-Algèbre quasi-cohérente; si en outre $\mathbf{X}$ est réduit (ce qui est le cas lorsque $\mathbf{X}$ est localement intègre), l'homomorphisme canonique $\mathcal{O}_{\mathrm{X}} \to \mathcal{R}(\mathbf{X})$ est injectif.

La question étant locale, la première assertion résulte de (7.3.3); la seconde résulte aussitôt de (7.2.3).

(7.3.8) Soient X, Y deux préschémas ayant chacun un nombre fini de composantes irréductibles, et soit $f: \mathrm{X} \to \mathrm{Y}$ un morphisme dont la restriction à l'ensemble des points génériques des composantes irréductibles de X est une surjection sur l'ensemble des points génériques des composantes irréductibles de Y. Alors on a

$$
f ^ {*} (\mathcal {R} (\mathrm{Y})) = \mathcal {R} (\mathrm{X}).\tag{7.3.8.1}
$$

En effet, on est ramené (en vertu de (7.3.3)) au cas où X et Y sont irréductibles, de points génériques $x$, $y$, avec $f(x)=y$; donc $(f^{*}(\mathcal{R}(\mathbf{Y})))_{x}=\mathcal{O}_{y}\otimes_{\mathcal{O}_{y}}\mathcal{O}_{x}=\mathcal{O}_{x}$ (0, 4.3.1), ce qui démontre (7.3.8.1) en vertu de (7.3.5).

## 7.4. Faisceaux de torsion et faisceaux sans torsion.

(7.4.1) Soit X un préschéma intègre. Pour tout $\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{F}$, l'homomorphisme canonique $\mathcal{O}_{\mathrm{X}} \to \mathcal{R}(\mathrm{X})$ définit par tensorisation un homomorphisme (dit encore canonique) $\mathcal{F} \to \mathcal{F} \otimes_{\mathcal{O}_{\mathrm{X}}} \mathcal{R}(\mathrm{X})$ qui, sur chaque fibre, n'est autre que l'homomorphisme $z \to z \otimes 1$ de $\mathcal{F}_x$ dans $\mathcal{F}_x \otimes_{\mathcal{O}_{\mathrm{X}}} \mathrm{R}(\mathrm{X})$. Le noyau $\mathcal{T}$ de cet homomorphisme est un sous-$\mathcal{O}_{\mathrm{X}}$-Module de $\mathcal{F}$, appelé faisceau de torsion de $\mathcal{F}$; il est quasi-cohérent si $\mathcal{F}$ est quasi-cohérent (4.1.1 et 7.3.6). On dit que $\mathcal{F}$ est sans torsion si $\mathcal{T} = 0$ et que $\mathcal{F}$ est un faisceau de torsion si $\mathcal{T} = \mathcal{F}$. Pour tout $\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{F}$, $\mathcal{F}/\mathcal{T}$ est sans torsion. On déduit de (7.3.5) que :

Proposition (7.4.2). — Si X est un préschéma intègre, tout $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent sans torsion $\mathcal{F}$ est isomorphe à un sous-faisceau $\mathcal{G}$ d'un faisceau simple de la forme $(\mathcal{R}(\mathbf{X}))^{(I)}$, engendré (en tant que $\mathcal{R}(\mathbf{X})$-Module) par $\mathcal{G}$.

Le cardinal de I est appelé le rang de F ; pour tout ouvert affine non vide U de X, le rang de F est égal au rang de  $\Gamma(\mathrm{U},\mathcal{F})$  en tant que  $\Gamma(\mathrm{U},\mathcal{O}_{\mathrm{X}})$ -module, comme on le voit aussitôt en considérant le point générique de X, contenu dans U. En particulier :

Corollaire (7.4.3). — Sur un préschéma intègre X, tout $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent sans torsion et de rang i (en particulier tout $\mathcal{O}_{\mathrm{X}}$-Module inversible) est isomorphe à un sous-$\mathcal{O}_{\mathrm{X}}$-Module de $\mathcal{R}(\mathbf{X})$, et réciproquement.

Corollaire (7.4.4). — Soient X un préschéma intègre, $\mathcal{L}$, $\mathcal{L}'$ deux $\mathcal{O}_{\mathrm{X}}$-Modules sans torsion, $f$ (resp. $f'$) une section de $\mathcal{L}$ (resp. $\mathcal{L}'$) au-dessus de X. Pour que $f \otimes f' = 0$, il faut et il suffit que l'une des sections $f$, $f'$ soit nulle.

Soit $x$ le point générique de $\mathbf{X}$; on a par hypothèse $(f \otimes f')_x = f_x \otimes f'_x = 0$. Comme $\mathcal{L}_x$ et $\mathcal{L}'_x$ s'identifient à des sous-$\mathcal{O}_x$-Modules du corps $\mathcal{O}_x$, la relation précédente entraîne $f_x = 0$ ou $f'_x = 0$, et par suite $f = 0$ ou $f' = 0$ puisque $\mathcal{L}$ et $\mathcal{L}'$ sont sans torsion (7.3.5).

Proposition (7.4.5). — Soient X, Y deux préschémas intègres,  $f: X \to Y$  un morphisme dominant. Pour tout  $O_{X}$ -Module quasi-cohérent sans torsion F,  $f_{*}(\mathcal{F})$  est un  $O_{Y}$ -Module sans torsion.

Comme $f_*$ est exact à gauche (0, 4.2.1), il suffit, en vertu de (7.4.2), de prouver la proposition lorsque $\mathcal{F} = (\mathcal{R}(\mathbf{X}))^{(I)}$. Or, tout ouvert non vide U de Y contient le point générique de Y, donc $f^{-1}(\mathrm{U})$ contient le point générique de X (0, 2.1.5), donc on a alors $\Gamma(\mathrm{U}, f_*(\mathcal{F})) = \Gamma(f^{-1}(\mathrm{U}), \mathcal{F}) = (\mathrm{R}(\mathbf{X}))^{(I)}$; autrement dit, $f_*(\mathcal{F})$ est le faisceau simple de fibre $(\mathrm{R}(\mathbf{X}))^{(I)}$, considéré comme $\mathcal{R}(\mathbf{Y})$-Module, et il est évidemment sans torsion.

Proposition (7.4.6). — Soient X un préschéma intègre, x son point générique. Pour tout  $O_{X}$ -Module quasi-cohérent de type fini F, les conditions suivantes sont équivalentes : a) F est un faisceau de torsion ; b)  $F_{x}=0$ ; c) Supp(F)≠X.

En vertu de (7.3.5) et de (7.4.1), les relations $\mathcal{F}_x = 0$ et $\mathcal{F} \otimes_{\mathcal{O}_X} \mathcal{R}(X) = 0$ sont équivalentes, donc $a)$ et $b)$ sont équivalentes; d'autre part, $\operatorname{Supp}(\mathcal{F})$ est fermé dans X (0, 5.2.2), et comme tout ouvert non vide de X contient $x, b)$ et $c)$ sont équivalentes.

(7.4.7) On étend (par abus de langage) les définitions de (7.4.1) au cas où X est un préschéma réduit n'ayant qu'un nombre fini de composantes irréductibles ; il résulte alors de (7.3.4) que l'équivalence de a) et c) dans (7.4.6) est encore valable pour un tel préschéma.

## § 8. LES SCHÉMAS DE CHEVALLEY

## 8.1. Anneaux locaux apparentés.

Pour tout anneau local A, nous noterons m(A) l'idéal maximal de A.

Lemme (8.1.1). — Soient A, B deux anneaux locaux tels que A⊂B ; les conditions suivantes sont équivalentes : (i) m(B)∩A=m(A); (ii) m(A)⊂m(B); (iii) i n'appartient pas à l'idéal de B engendré par m(A).

Il est évident que (i) entraîne (ii) et (ii) entraîne (iii) ; enfin, si (iii) est vérifiéé, $m(B) \cap A$ contient $m(A)$ et ne contient pas 1, donc est égal à $m(A)$.

Lorsque les conditions équivalentes de (8.1.1) sont remplies, on dit que B domine A ; il revient au même de dire que l'injection A→B est un homomorphisme local. Il est clair que, dans l'ensemble des sous-anneaux locaux d'un anneau R, la relation de domination est une relation d'ordre.

(8.1.2) Considérons maintenant un corps R. Pour tout sous-anneau A de R, nous désignerons par L(A) l'ensemble des anneaux locaux  $A_{p}$ , où p parcourt le spectre premier de A ; ils sont identifiés à des sous-anneaux de R contenant A. Comme  $\mathfrak{p} = (\mathfrak{p}A_{\mathfrak{p}}) \cap A$ , l'application  $p \to A_{p}$  de Spec(A) dans L(A) est bijective.

Lemme (8.1.3). — Soient R un corps, A un sous-anneau de R. Pour qu'un sous-anneau local M de R domine un anneau  $\mathrm{A}_{\mathfrak{p}} \in \mathrm{L}(\mathrm{A})$ , il faut et il suffit que  $A \subset M$ ; l'anneau local  $A_{p}$  dominé par M est alors unique et correspond à  $\mathfrak{p} = \mathfrak{m}(\mathbf{M}) \cap \mathbf{A}$ .

En effet, si M domine  $A_{p}$ , on a  $m(M) \cap A_{p} = pA_{p}$  d'après (8.1.1), d'où l'unicité de p; d'autre part, si  $A \subset M$ ,  $m(M) \cap A = p$  est premier dans A, et comme  $A - p \subset M$ , on a  $A_{p} \subset M$  et  $pA_{p} \subset m(M)$ , donc M domine  $A_{p}$ .

Lemme (8.1.4). — Soient R un corps, M, N deux sous-anneaux locaux de R, P le sous-anneau de R engendré par M ∪ N. Les conditions suivantes sont équivalentes :

(i) Il existe un idéal premier p de P tel que $\mathfrak{m}(\mathbf{M}) = \mathfrak{p} \cap \mathbf{M}$, $\mathfrak{m}(\mathbf{N}) = \mathfrak{p} \cap \mathbf{N}$.

(ii) L'idéal a engendré dans P par m(M) ∪ m(N) est distinct de P.

(iii) Il existe un sous-anneau local Q de R dominant à la fois M et N.

Il est clair que (i) implique (ii) ; inversement, si $a \neq P$, $a$ est contenu dans un idéal maximal $n$ de $P$ et comme $1 \notin n$, $n \cap M$ contient $m(M)$ et est distinct de $M$, donc $n \cap M = m(M)$ et de même $n \cap N = m(N)$. Il est clair que si $Q$ domine $M$ et $N$, on a $P \subset Q$ et $m(M) = m(Q) \cap M = (m(Q) \cap P) \cap M$, $m(N) = (m(Q) \cap P) \cap N$, donc (iii) entraîne (i); la réciproque est évidente en prenant $Q = P_p$.

Lorsque les conditions de (8.1.4) sont satisfaites, on dit, avec C. Chevalley, que les anneaux locaux M et N sont apparentés.

Proposition (8.1.5). — Soient A, B deux sous-anneaux d'un corps R, C le sous-anneau de R engendré par A∪B. Les conditions suivantes sont équivalentes :

(i) Pour tout anneau local Q contenant A et B, on a  $A_{p}=B_{q}$ , en posant  $p=m(Q)\cap A$ ,  $q=m(Q)\cap B$ .

(ii) Pour tout idéal premier r de C, on a  $A_{p}=B_{q}$ , en posant  $p=r\cap A$ ,  $q=r\cap B$ .

(iii) Si  $\mathbf{M}\in\mathbf{L}(\mathbf{A})$  et  $\mathbf{N}\in\mathbf{L}(\mathbf{B})$  sont apparentés, ils sont identiques.

(iv) On a $\mathbf{L}(\mathbf{A})\cap \mathbf{L}(\mathbf{B}) = \mathbf{L}(\mathbf{C})$

Les lemmes (8.1.3) et (8.1.4) prouvent que (i) et (iii) sont équivalentes ; il est clair que (i) entraîne (ii) en l'appliquant à $\mathbf{Q} = \mathbf{C}_{\mathbf{r}}$; inversement, (ii) entraîne (i), car si $\mathbf{Q}$ contient $\mathbf{A} \cup \mathbf{B}$, il contient $\mathbf{C}$, et si $\mathfrak{r} = \mathfrak{m}(\mathbf{Q}) \cap \mathbf{C}$, on a $\mathfrak{p} = \mathfrak{r} \cap \mathbf{A}$ et $\mathfrak{q} = \mathfrak{r} \cap \mathbf{B}$ d'après (8.1.3). Il est immédiat que (iv) implique (i), car si $\mathbf{Q}$ contient $\mathbf{A} \cup \mathbf{B}$, il domine un anneau local $\mathbf{C}_{\mathbf{r}} \in \mathbf{L}(\mathbf{C})$ par (8.1.3); on a par hypothèse $\mathbf{C}_{\mathbf{r}} \in \mathbf{L}(\mathbf{A}) \cap \mathbf{L}(\mathbf{B})$, et (8.1.1) et (8.1.3) prouvent que $\mathbf{C}_{\mathbf{r}} = \mathbf{A}_{\mathfrak{p}} = \mathbf{B}_{\mathfrak{q}}$. Prouvons enfin que (iii) entraîne (iv). Soit $\mathbf{Q} \in \mathbf{L}(\mathbf{C})$; $\mathbf{Q}$ domine un $\mathbf{M} \in \mathbf{L}(\mathbf{A})$ et un $\mathbf{N} \in \mathbf{L}(\mathbf{B})$ (8.1.3), donc $\mathbf{M}$ et $\mathbf{N}$, étant apparentés, sont identiques par hypothèse. Comme on a alors $\mathbf{C} \subset \mathbf{M}$, $\mathbf{M}$ domine un $\mathbf{Q}' \in \mathbf{L}(\mathbf{C})$ (8.1.3), donc $\mathbf{Q}$ domine $\mathbf{Q}'$, ce qui (8.1.3) entraîne nécessairement $\mathbf{Q} = \mathbf{Q}' = \mathbf{M}$, donc $\mathbf{Q} \in \mathbf{L}(\mathbf{A}) \cap \mathbf{L}(\mathbf{B})$. Inversement, si $\mathbf{Q} \in \mathbf{L}(\mathbf{A}) \cap \mathbf{L}(\mathbf{B})$, on a $\mathbf{C} \subset \mathbf{Q}$, donc (8.1.3) $\mathbf{Q}$ domine un $Q'' \in L(\mathbf{C}) \subset L(\mathbf{A}) \cap L(\mathbf{B})$; $\mathbf{Q}$ et $Q''$ étant apparentés sont identiques, donc $Q'' = Q \in L(\mathbf{C})$, ce qui achève la démonstration.

## 8.2. Anneaux locaux d'un schéma intègre.

(8.2.1) Soient X un préschéma intègre, R son corps des fonctions rationnelles, identique à l'anneau local du point générique $a$ de X; pour tout $x \in \mathbf{X}$, on sait que $\mathcal{O}_x$ s'identifie canoniquement à un sous-anneau de R (7.1.5), et pour toute fonction rationnelle $f \in \mathbb{R}$, le domaine de définition $\delta(f)$ de $f$ est l'ensemble ouvert des $x \in \mathbf{X}$ tels que $f \in \mathcal{O}_x$. Il en résulte (7.2.6) que pour tout ouvert U⊂X, on a

$$
\Gamma (\mathrm{U}, \mathcal {O} _ {\mathrm{X}}) = \bigcap_ {\boldsymbol {x} \in \mathrm{U}} \mathcal {O} _ {\boldsymbol {x}}\tag{8.2.1.1}
$$

Proposition (8.2.2). — Soient X un préschéma intègre, R son corps des fonctions rationnelles. Pour que X soit un schéma, il faut et il suffit que la relation « O\_x et O\_y sont apparentés » (8.1.4) entre points x, y de X implique x=y.

Supposons cette condition vérifiée, et montrons que X est séparé. Soient U et V deux ouverts affines distincts de X, A et B leurs anneaux, identifiés à des sous-anneaux de R ; U (resp. V) s'identifie donc (8.1.2) à L(A) (resp. L(B)), et l'hypothèse entraîne (8.1.5) que si C est le sous-anneau de R engendré par AuB, W = U ∩ V s'identifie à L(A) ∩ L(B) = L(C). En outre, on sait ([1], p. 5-03, prop. 4 bis) que tout sous-anneau E de R est égal à l'intersection des anneaux locaux appartenant à L(E) ; C s'identifie donc à l'intersection des anneaux $\mathcal{O}_{z}$ pour $z \in W$, autrement dit (8.2.1.1) à $\Gamma(W, \mathcal{O}_{X})$. Considérons alors le sous-préschéma induit par X sur W ; à l'homomorphisme identique $\varphi: C \to \Gamma(W, \mathcal{O}_{X})$ correspond (2.2.4) un morphisme $\Phi = (\psi, \theta): W \to \text{Spec}(C)$; nous allons voir que $\Phi$ est un isomorphisme de préschémas, d'où résultera que W est un ouvert affine. L'identification de W à L(C) = Spec(C) montre que $\psi$ est bijective. D'autre part, pour tout $x \in W$, $\theta_{x}^{\sharp}$ est l'injection $C_{r} \to \mathcal{O}_{x}$, si $r = m_{x} \cap C$, et par définition $C_{r}$ est identifié à $\mathcal{O}_{x}$, donc $\theta_{x}^{\sharp}$ est bijective. Il reste donc à voir que $\psi$ est un homéomorphisme, autrement dit que pour toute partie fermée F ⊂ W, $\psi(F)$ est fermé dans Spec(C). Or, F est la trace sur W d'une partie fermée de U, de la forme V(a), où a est un idéal de A ; montrons que $\psi(F) = V(aC)$, ce qui prouvera notre assertion. En effet, les idéaux premiers de C contenant aC sont les idéaux premiers de C contenant a, donc les idéaux de la forme $\psi(x) = m_{x} \cap C$ où a ⊂ m$_{x}$ et $x \in W$; comme a ⊂ m$_{x}$ équivaut à $x \in V(a) = W \cap F$ pour $x \in U$, on a bien $\psi(F) = V(aC)$.

Il s'ensuit que X est séparé, car U∩V est affine et son anneau C est engendré par la réunion A∪B des anneaux de U et V (5.5.6).

Inversement, supposons X séparé, et soient $x, y$ deux points de X tels que $\mathcal{O}_x$ et $\mathcal{O}_y$ soient apparentés. Soit U (resp. V) un ouvert affine contenant $x$ (resp. $y$), d'anneau A (resp. B); on sait alors que U∩V est affine et que son anneau C est engendré par A∪B (5.5.6). Si $\mathfrak{p} = \mathfrak{m}_x \cap \mathrm{A}$, $\mathfrak{q} = \mathfrak{m}_y \cap \mathrm{B}$, on a $\mathrm{A}_{\mathfrak{p}} = \mathcal{O}_x$, $\mathrm{B}_{\mathfrak{q}} = \mathcal{O}_y$, et comme $\mathrm{A}_{\mathfrak{p}}$ et $\mathrm{B}_{\mathfrak{q}}$ sont apparentés, il existe un idéal premier r de C tel que $\mathfrak{p} = \mathfrak{r} \cap \mathrm{A}$, $\mathfrak{q} = \mathfrak{r} \cap \mathrm{B}$ (8.1.4). Mais alors il existe un point $z \in \mathrm{U} \cap \mathrm{V}$ tel que $\mathfrak{r} = \mathfrak{m}_z \cap \mathrm{C}$ puisque U∩V est affine, et on a évidemment $x = z$ et $y = z$, d'où $x = y$.

Corollaire (8.2.3). — Soient X un schéma intègre, x, y deux points de X. Pour que  $x \in \{y\}$ , il faut et il suffit que  $O_{x} \subset O_{y}$ , autrement dit que toute fonction rationnelle définie en x soit définie en y.

La condition est évidemment nécessaire puisque le domaine de définition $\delta(f)$ d'une fonction rationnelle $f\in\mathbb{R}$ est ouvert; montrons qu'elle est suffisante. Si $\mathcal{O}_{x}\subset\mathcal{O}_{y}$, il existe un idéal premier $\mathfrak{p}$ de $\mathcal{O}_{x}$ tel que $\mathcal{O}_{y}$ domine $(\mathcal{O}_{x})_{\mathfrak{p}}$ (8.1.3); or (2.4.2) il existe $z\in\mathbf{X}$ tel que $x\in\overline{\{z\}}$ et que $\mathcal{O}_{z}=(\mathcal{O}_{x})_{\mathfrak{p}}$; comme $\mathcal{O}_{z}$ et $\mathcal{O}_{y}$ sont apparentés, on a $z=y$ par (8.2.2), d'où le corollaire.

Corollaire (8.2.4). — Si X est un schéma intègre, l'application  $x \to O_{x}$  est injective ; autrement dit, si x, y sont deux points distincts de X, il existe une fonction rationnelle définie en l'un de ces points et non en l'autre.

Cela résulte de (8.2.3) et de l'axiome $(\mathbf{T}_0)$ (2.1.4).

Corollaire (8.2.5). — Soit X un schéma intègre dont l'espace sous-jacent est noethérien; lorsque f parcourt le corps R des fonctions rationnelles sur X, les ensembles δ(f) engendrent la topologie de X.

En effet, toute partie fermée de X est alors réunion finie d'ensembles fermés irréductibles, c'est-à-dire de la forme  $\overline{\{y\}}$  (2.1.5). Or, si  $x \notin \overline{\{y\}}$ , il existe une fonction rationnelle f définie en x et non en y (8.2.3), autrement dit, on a  $x \in \delta(f)$  et  $\delta(f)$  ne rencontre pas  $\overline{\{y\}}$ . Le complémentaire de  $\overline{\{y\}}$  est par suite réunion d'ensembles de la forme  $\delta(f)$ , et en vertu de la première remarque, tout ouvert de X est réunion d'intersections finies d'ouverts de la forme  $\delta(f)$ .

(8.2.6) Le cor. (8.2.5) montre que la topologie de X est entièrement caractérisée par la donnée de la famille d'anneaux locaux  $(\mathcal{O}_{x})_{x\in\mathrm{X}}$  ayant R pour corps des fractions. Il revient au même d'ailleurs de dire que les parties fermées de X sont définies de la façon suivante : étant donnée une partie finie  $\{x_{1},\ldots,x_{n}\}$  de X, on considère l'ensemble des  $y\in X$  tels que  $O_{y}\subset O_{x_{i}}$  pour un indice i au moins, et ces ensembles (pour tous les choix de  $\{x_{1},\ldots,x_{n}\}$ ) sont les ensembles fermés de X. En outre, une fois connue la topologie de X, le faisceau structural  $O_{X}$  est aussi bien déterminé par la famille des  $O_{x}$, puisque  $\Gamma(\mathrm{U},\mathcal{O}_{\mathrm{X}})=\bigcap_{x\in\mathrm{U}}\mathcal{O}_{x}$  par (8.2.1.1). La famille  $(\mathcal{O}_{x})_{x\in\mathrm{X}}$  détermine donc complètement le préschéma X lorsque X est un schéma intègre dont l'espace sous-jacent est noethérien.

Proposition (8.2.7). — Soient X, Y deux schémas intègres, $f: \mathbf{X} \to \mathbf{Y}$ un morphisme dominant (2.2.6), K (resp. L) le corps des fonctions rationnelles sur X (resp. Y). Alors L s'identifie à un sous-corps de K, et pour tout $x \in \mathbf{X}$, $\mathcal{O}_{f(x)}$ est l'unique anneau local de Y dominé par $\mathcal{O}_x$.

En effet, si $f = (\psi, \theta)$ et si $a$ est le point générique de X, $\psi(a)$ est le point générique de Y (0, 2.1.5); $\theta_a^\sharp$ est par suite un monomorphisme du corps $L = \mathcal{O}_{\psi(a)}$ dans le corps $K = \mathcal{O}_a$. Comme tout ouvert affine non vide U de Y contient $\psi(a)$, il résulte de (2.2.4) que l'homomorphisme $\Gamma(U, \mathcal{O}_Y) \to \Gamma(\psi^{-1}(U), \mathcal{O}_X)$ correspondant à $f$ est la restriction de $\theta_a^\sharp$ à $\Gamma(U, \mathcal{O}_Y)$. Donc, pour tout $x \in X$, $\theta_x^\sharp$ est la restriction à $\mathcal{O}_{\psi(x)}$ de $\theta_a^\sharp$, et est par suite un monomorphisme. On sait en outre que $\theta_x^\sharp$ est un homomorphisme local, donc, si on identifie L à un sous-corps de K par $\theta_a^\sharp$, $\mathcal{O}_{\psi(x)}$ est dominé par $\mathcal{O}_x$ (8.1.1); c'est d'ailleurs le seul anneau local de Y dominé par $\mathcal{O}_x$, puisque deux anneaux locaux de Y qui sont apparentés sont identiques (8.2.2).

Proposition (8.2.8). — Soient X un préschéma irréductible, $f: \mathbf{X} \to \mathbf{Y}$ une immersion locale (resp. un isomorphisme local); on suppose en outre le morphisme $f$ séparé. Alors $f$ est une immersion (resp. une immersion ouverte).

Soit $f = (\psi, \theta)$; il suffit, dans les deux cas, de prouver que $\psi$ est un homéomorphisme de X sur $\psi(X)$ (4.5.3). Remplaçant $f$ par $f_{\text{red}}$ (5.1.6 et 5.5.1, (vi)), on peut supposer X et Y réduits. Si $Y'$ est le sous-préschéma fermé réduit de Y ayant pour espace sous-jacent $\overline{\psi(X)}$, $f$ se factorise en $X \xrightarrow{f'} Y' \xrightarrow{j} Y$, où $j$ est l'injection canonique (5.2.2). Il résulte de (5.5.1, (v)) que $f'$ est encore un morphisme séparé; en outre, $f'$ est encore

une immersion locale (resp. un isomorphisme local), car la question étant locale sur X et Y, on peut se borner pour le démontrer au cas où f est une immersion fermée (resp. une immersion ouverte) et notre assertion découle alors aussitôt de (4.2.2).

On peut donc supposer que $f$ est un morphisme dominant, ce qui entraîne que Y est, lui aussi, irréductible (0, 2.1.5), donc que X et Y sont tous deux intègres. En outre, la question étant locale sur Y, on peut supposer que Y est un schéma affine; comme $f$ est séparé, X est un schéma (5.5.1, (ii)), et on est finalement dans les hypothèses de (8.2.7). Alors, pour tout $x \in \mathbf{X}$, $\theta_{x}^{\#}$ est injectif; mais l'hypothèse que $f$ est une immersion locale implique que $\theta_{x}^{\#}$ est surjectif (4.2.2), donc $\theta_{x}^{\#}$ est bijectif, autrement dit (avec l'identification de (8.2.7)) on a $\mathcal{O}_{\psi(x)} = \mathcal{O}_{x}$. Cela implique par (8.2.4) que $\psi$ est une application injective, ce qui démontre déjà la proposition lorsque $f$ est un isomorphisme local (4.5.3). Lorsqu'on suppose seulement que $f$ est une immersion locale, pour tout $x \in \mathbf{X}$ il existe un voisinage ouvert U de $x$ dans X et un voisinage ouvert V de $\psi(x)$ dans Y tels que la restriction de $\psi$ à U soit un homéomorphisme de U sur une partie fermée de V. Or, U est dense dans X, donc $\psi(\mathbf{U})$ est dense dans Y et a fortiori dans V, ce qui prouve que $\psi(\mathbf{U}) = \mathbf{V}$; comme $\psi$ est injective, $\psi^{-1}(\mathbf{V}) = \mathbf{U}$ et ceci achève de montrer que $\psi$ est un homéomorphisme de X sur $\psi(\mathbf{X})$.

## 8. 3. Les schémas de Chevalley.

(8.3.1) Soient X un schéma intègre noethérien, R son corps des fonctions rationnelles ; désignons par X' l'ensemble des sous-anneaux locaux $\mathcal{O}_{x} \subset \mathbb{R}$, où $x$ parcourt X. L'ensemble X' vérifie les trois conditions suivantes :

(Sch. 1) Pour tout $\mathbf{M} \in \mathbf{X}'$, R est le corps des fractions de $\mathbf{M}$.

(Sch. 2) Il existe un ensemble fini de sous-anneaux noethériens $\mathbf{A}_i$ de $\mathbf{R}$ tels que $\mathbf{X}' = \bigcup_{i} \mathbf{L}(\mathbf{A}_i)$ et que, pour tout couple d'indices $i, j$, le sous-anneau $\mathbf{A}_{ij}$ de $\mathbf{R}$ engendré par $\mathbf{A}_i \cup \mathbf{A}_j$ soit une algèbre de type fini sur $\mathbf{A}_i$.

(Sch. 3) Deux éléments M, N de X' qui sont apparentés sont identiques.

On a en effet vu dans (8.2.1) que (Sch. 1) est satisfaite, et (Sch. 3) résulte de (8.2.2). Pour démontrer (Sch. 2), il suffit de recouvrir X par un nombre fini d'ouverts affines  $U_{i}$ , d'anneaux noethériens, et de prendre  $\mathbf{A}_{i}=\Gamma(\mathbf{U}_{i},\mathcal{O}_{\mathbf{X}})$ ; l'hypothèse que X est un schéma entraîne que  $U_{i}\cap U_{j}$  est affine et que  $\Gamma(\mathbf{U}_{i}\cap\mathbf{U}_{j},\mathcal{O}_{\mathbf{X}})=\mathbf{A}_{ij}$  (5.5.6); en outre, comme l'espace  $U_{i}$  est noethérien, l'immersion  $U_{i}\cap U_{j}\to U_{i}$  est de type fini (6.3.5), donc  $A_{ij}$  est une  $A_{i}$ -algèbre de type fini (6.3.3).

(8.3.2) Les structures dont les axiomes sont (Sch. 1), (Sch. 2) et (Sch. 3) généralisent les « schémas » au sens de C. Chevalley, qui suppose en outre que R est une extension de type fini d'un corps K et que les A$_{i}$ sont des K-algèbres de type fini (ce qui rend inutile une partie de (Sch. 2)) [1]. Inversement, si on a une telle structure sur un ensemble X', on peut lui associer un schéma intègre X en utilisant les remarques de (8.2.6) : l'espace sous-jacent de X est égal à X' muni de la topologie définie dans (8.2.6), et du faisceau O$_{X}$

tel que $\Gamma(\mathrm{U},\mathcal{O}_{\mathrm{X}})=\bigcap_{x\in\mathrm{U}}\mathcal{O}_{x}$ pour tout ouvert $\mathrm{U}\subset\mathrm{X}$, avec une définition évidente des homomorphismes de restriction. Nous laissons au lecteur le soin de vérifier qu'on obtient bien ainsi un schéma intègre, dont les anneaux locaux sont les éléments de $\mathrm{X}'$; nous n'utiliserons pas ce résultat par la suite.

## § 9. COMPLÉMENTS SUR LES FAISCEAUX QUASI-COHÉRENTS

## 9. 1. Produit tensoriel de faisceaux quasi-cohérents.

Proposition (9.1.1). — Soit X un préschéma (resp. un préschéma localement noethérien). Soient F et G deux  $O_{X}$ -Modules quasi-cohérents (resp. cohérents); alors  $F \otimes_{O_{X}} G$  est quasi-cohérent (resp. cohérent) et de type fini si F et G sont de type fini. Si F admet une présentation finie et si G est quasi-cohérent (resp. cohérent), alors  $\mathcal{H}om_{\mathcal{O}_{X}}(\mathcal{F}, \mathcal{G})$  est quasi-cohérent (resp. cohérent).

La question étant locale, on peut supposer X affine (resp. affine noethérien) ; en outre, si $\mathcal{F}$ est cohérent, on peut supposer qu'il est le conoyau d'un homomorphisme $\mathcal{O}_{\mathrm{X}}^{m} \to \mathcal{O}_{\mathrm{X}}^{n}$. Les assertions relatives aux faisceaux quasi-cohérents résultent alors de (1.3.12) et (1.3.9) ; les assertions relatives aux faisceaux cohérents résultent de (1.5.1) et du fait que, si M et N sont des modules de type fini sur un anneau noethérien A, $\mathbf{M} \otimes_{\mathbf{A}} \mathbf{N}$ et $\operatorname{Hom}_{\mathbf{A}}(\mathbf{M}, \mathbf{N})$ sont des A-modules de type fini.

Définition (9.1.2). — Soient X, Y deux S-préschémas, p, q les projections de  $X \times_{s} Y$ , F (resp. G) un  $O_{X}$ -Module (resp. un  $O_{Y}$ -Module) quasi-cohérent. On appelle produit tensoriel de F et G sur  $O_{S}$  (ou sur S) et on note  $F \otimes_{O_{S}} G$  (ou  $F \otimes_{S} G$ ) le produit tensoriel  $p^{*}(\mathcal{F}) \otimes_{\mathcal{O}_{X \times_{S}} Y} q^{*}(\mathcal{G})$  sur le préschéma  $X \times_{s} Y$ .

Si  $X_{i}$  ( $i \leqslant i \leqslant n$ ) sont des S-préschémas,  $F_{i}$  un  $O_{X_{i}}$ -Module quasi-cohérent ( $i \leqslant i \leqslant n$ ), on définit de la même manière le produit tensoriel  $F_{1} \otimes_{S} F_{2} \otimes_{S} \ldots \otimes_{S} F_{n}$  sur le préschéma  $Z = X_{1} \times_{S} X_{2} \ldots \times_{S} X_{n}$ ; c'est un  $O_{Z}$ -module quasi-cohérent en vertu de (9.1.1) et de (0, 5.1.4); il est cohérent si les  $F_{i}$  le sont et si Z est localement noethérien en vertu de (9.1.1), (0, 5.3.11) et (6.1.1).

On notera que si on prend X=Y=S, la définition (9.1.2) redonne le produit tensoriel de  $O_{s}$ -Modules. En outre, comme  $q^{*}(\mathcal{O}_{\mathrm{Y}})=\mathcal{O}_{\mathrm{X}\times_{\mathrm{S}}\mathrm{Y}}(0,4.3.4)$ , le produit  $F\otimes_{s}O_{Y}$  s'identifie canoniquement à  $p^{*}(\mathcal{F})$ , et de même  $O_{X}\otimes_{s}G$  s'identifie canoniquement à  $q^{*}(\mathcal{G})$ . Plus particulièrement, si on prend Y=S et qu'on désigne par f le morphisme structural  $X\to Y$ , on a  $O_{X}\otimes_{Y}G=f^{*}(\mathcal{G})$ : le produit tensoriel ordinaire et l'image réciproque apparaissent donc comme des cas particuliers du produit tensoriel général.

La déf. (9.1.2) entraîne immédiatement que, pour X et Y fixés, $\mathcal{F} \otimes_{\mathrm{s}} \mathcal{G}$ est un bifoncteur covariant additif et exact à droite en $\mathcal{F}$ et $\mathcal{G}$.

Proposition (9.1.3). — Soient S, X, Y trois schémas affines d'anneaux respectifs, A, B, C, B et C étant des A-algèbres. Soit M (resp. N) un B-module (resp. C-module), $\mathcal{F}=\widetilde{\mathbf{M}}$ (resp. $\mathcal{G}=\widetilde{\mathbf{N}}$) le faisceau quasi-cohérent associé; alors $\mathcal{F}\otimes_{\mathrm{S}}\mathcal{G}$ est canoniquement isomorphe au faisceau associé au $(\mathrm{B}\otimes_{\mathrm{A}}\mathrm{C})$-module $\mathrm{M}\otimes_{\mathrm{A}}\mathrm{N}$.

En effet, en vertu de (1.6.5), $\mathcal{F} \otimes_{\mathrm{S}} \mathcal{G}$ est canoniquement isomorphe au faisceau associé au $(\mathrm{B} \otimes_{\mathrm{A}} \mathrm{C})$-module

$$
(\mathbf {M} \otimes_ {\mathbf {B}} (\mathbf {B} \otimes_ {\mathbf {A}} \mathbf {C})) \otimes_ {\mathbf {B} \otimes_ {\mathbf {A}} \mathbf {C}} ((\mathbf {B} \otimes_ {\mathbf {A}} \mathbf {C}) \otimes_ {\mathbf {c}} \mathbf {N})
$$

et en raison des isomorphismes canoniques entre produits tensoriels, ce dernier est isomorphe à  $\mathbf{M}\otimes_{\mathbf{B}}(\mathbf{B}\otimes_{\mathbf{A}}\mathbf{C})\otimes_{\mathbf{C}}\mathbf{N}=(\mathbf{M}\otimes_{\mathbf{B}}\mathbf{B})\otimes_{\mathbf{A}}(\mathbf{C}\otimes_{\mathbf{C}}\mathbf{N})=\mathbf{M}\otimes_{\mathbf{A}}\mathbf{N}$ .

Proposition (9.1.4). — Soient $f: \mathrm{T} \to \mathrm{X}$, $g: \mathrm{T} \to \mathrm{Y}$ deux S-morphismes, $\mathcal{F}$ (resp. $\mathcal{G}$) un $\mathcal{O}_{\mathrm{X}}$-Module (resp. $\mathcal{O}_{\mathrm{Y}}$-Module) quasi-cohérent. On a alors $(f, g)_{\mathrm{S}}^{*}(\mathcal{F} \otimes_{\mathrm{S}} \mathcal{G}) = f^{*}(\mathcal{F}) \otimes_{\mathcal{O}_{\mathrm{T}}} g^{*}(\mathcal{G})$.

Si $p, q$ sont les projections de $X \times_{\mathbb{S}} Y$, la formule résulte en effet des relations $(f, g)_{\mathbb{S}}^{*} \circ p^{*} = f^{*}$ et $(f, g)_{\mathbb{S}}^{*} \circ q^{*} = g^{*}$ (0, 3.5.5), et du fait qu'une image réciproque d'un produit tensoriel de faisceaux algébriques est le produit tensoriel de leurs images réciproques (0, 4.3.3).

Corollaire (9.1.5). — Soient $f: \mathrm{X} \to \mathrm{X}'$, $g: \mathrm{Y} \to \mathrm{Y}'$ deux S-morphismes, $\mathcal{F}'$ (resp. $\mathcal{G}'$) un $\mathcal{O}_{\mathrm{X}'}$-Module (resp. $\mathcal{O}_{\mathrm{Y}'}$-Module) quasi-cohérent. On a alors

$$
(f \times_ {\mathrm{s}} g) ^ {*} (\mathcal {F} ^ {\prime} \otimes_ {\mathrm{s}} \mathcal {G} ^ {\prime}) = f ^ {*} (\mathcal {F} ^ {\prime}) \otimes_ {\mathrm{s}} g ^ {*} (\mathcal {G} ^ {\prime}).
$$

Cela résulte de (9.1.4) et du fait que $f \times_{\mathbb{S}} g = (f \circ p, g \circ q)_{\mathbb{S}}$, $p$ et $q$ étant les projections de $\mathbf{X} \times_{\mathbb{S}} \mathbf{Y}$.

Corollaire (9.1.6). — Soient X, Y, Z trois S-préschémas, $\mathcal{F}$ (resp. $\mathcal{G},\mathcal{H}$) un $\mathcal{O}_{\mathrm{X}}$-Module (resp. $\mathcal{O}_{\mathrm{Y}}$-Module, $\mathcal{O}_{\mathrm{Z}}$-Module) quasi-cohérent; le faisceau $\mathcal{F} \otimes_{\mathrm{S}} \mathcal{G} \otimes_{\mathrm{S}} \mathcal{H}$ est l'image réciproque de $(\mathcal{F} \otimes_{\mathrm{S}} \mathcal{G}) \otimes_{\mathrm{S}} \mathcal{H}$ par l'isomorphisme canonique de $\mathrm{X} \times_{\mathrm{S}} \mathrm{Y} \times_{\mathrm{S}} \mathrm{Z}$ sur $(\mathrm{X} \times_{\mathrm{S}} \mathrm{Y}) \times_{\mathrm{S}} \mathrm{Z}$.

En effet, cet isomorphisme s'écrit  $(p_{1}, p_{2})_{\mathrm{S}} \times_{\mathrm{S}} p_{3}$ , en désignant par  $p_{1}, p_{2}, p_{3}$  les projections de  $X \times_{S} Y \times_{S} Z$ .

De même, l'image réciproque de $\mathcal{G}\otimes_{\mathbb{S}}\mathcal{F}$ par l'isomorphisme canonique de $\mathbf{X}\times_{\mathbb{S}}\mathbf{Y}$ sur $\mathbf{Y}\times_{\mathbb{S}}\mathbf{X}$ est $\mathcal{F}\otimes_{\mathbb{S}}\mathcal{G}$.

Corollaire (9.1.7). — Si X est un S-préschéma, tout $\mathcal{O}_{\mathrm{x}}$-Module quasi-cohérent $\mathcal{F}$ est l'image réciproque de $\mathcal{F} \otimes_{\mathrm{s}} \mathcal{O}_{\mathrm{s}}$ par l'isomorphisme canonique de X sur $\mathrm{X} \times_{\mathrm{s}} \mathrm{S}$ (3.3.3).

En effet, cet isomorphisme est  $(\mathrm{I}_{\mathrm{X}}, \varphi)_{\mathrm{S}}$ , où  $\varphi$  est le morphisme structural  $X \to S$ , et le corollaire résulte de (9.1.4) et du fait que  $\varphi^{*}(\mathcal{O}_{\mathrm{S}}) = \mathcal{O}_{\mathrm{X}}$ .

(9.1.8) Soient X un S-préschéma, $\mathcal{F}$ un $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent, $\varphi: \mathrm{S}' \to \mathrm{S}$ un morphisme; on désigne par $\mathcal{F}_{(\varphi)}$ ou $\mathcal{F}_{(\mathrm{S}')}$ le faisceau quasi-cohérent $\mathcal{F} \otimes_{\mathrm{S}} \mathcal{O}_{\mathrm{S}'}$ sur $\mathrm{X} \times_{\mathrm{S}} \mathrm{S}' = \mathrm{X}_{(\varphi)} = \mathrm{X}_{(\mathrm{S}')}$; donc $\mathcal{F}_{(\mathrm{S}')} = p^*(\mathcal{F})$, où $p$ est la projection $\mathrm{X}_{(\mathrm{S}')} \to \mathrm{X}$.

Proposition (9.1.9). — Soit $\varphi': S'' \to S'$ un morphisme. Pour tout $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent $\mathcal{F}$ sur le S-préschéma $\mathbf{X}$, $(\mathcal{F}_{(\varphi)})_{(\varphi')}$ est l'image réciproque de $\mathcal{F}_{(\varphi \circ \varphi')}$ par l'isomorphisme canonique $(\mathbf{X}_{(\varphi)})_{(\varphi')} \simeq \mathbf{X}_{(\varphi \circ \varphi')}$ (3.3.9).

Cela résulte aussitôt des définitions et de (3.3.9), et s'écrit encore

$$
(\mathcal {F} \otimes_ {\mathrm{s}} \mathcal {O} _ {\mathrm{s} ^ {\prime}}) \otimes_ {\mathrm{s} ^ {\prime}} \mathcal {O} _ {\mathrm{s} ^ {\prime \prime}} = \mathcal {F} \otimes_ {\mathrm{s}} \mathcal {O} _ {\mathrm{s} ^ {\prime \prime}}.\tag{9.1.9.1}
$$

Proposition (9.1.10). — Soient Y un S-préschéma, $f: X \to Y$ un S-morphisme. Pour tout $\mathcal{O}_{Y}$-Module quasi-cohérent $\mathcal{G}$ et tout morphisme $S' \to S$, on a $(f_{(S')})^*(\mathcal{G}_{(S')}) = (f^*(\mathcal{G}))_{(S')}.$

Cela résulte aussitôt de la commutativité du diagramme

$$
\begin{array}{c} \mathbf {X} _ {(\mathrm{S} ^ {\prime})} \xrightarrow {f _ {(\mathrm{S} ^ {\prime})}} \mathbf {Y} _ {(\mathrm{S} ^ {\prime})} \\ \downarrow \qquad \qquad \qquad \qquad \qquad \downarrow \\ \mathbf {X} \xrightarrow [ f ]{} \mathbf {Y} \end{array}
$$

Corollaire (9.1.11). — Soient X, Y deux S-préschémas, $\mathcal{F}$ (resp. $\mathcal{G}$) un $\mathcal{O}_{\mathrm{X}}$-Module (resp. $\mathcal{O}_{\mathrm{Y}}$-Module) quasi-cohérent. L'image réciproque du faisceau $(\mathcal{F}_{(\mathrm{S}^{\prime})}) \otimes_{\mathrm{S}^{\prime}} (\mathcal{G}_{(\mathrm{S}^{\prime})})$ par l'isomorphisme canonique $(\mathrm{X} \times_{\mathrm{S}} \mathrm{Y})_{(\mathrm{S}^{\prime})} \simeq (\mathrm{X}_{(\mathrm{S}^{\prime})}) \times_{\mathrm{S}^{\prime}} (\mathrm{Y}_{(\mathrm{S}^{\prime})})$ (3.3.10) est égale à. $(\mathcal{F} \otimes_{\mathrm{S}} \mathcal{G})_{(\mathrm{S}^{\prime})}$.

Si $p$, $q$ sont les projections de $\mathbf{X} \times_{\mathrm{s}} \mathbf{Y}$, l'isomorphisme en question n'est autre que $(p_{(\mathrm{S}^{\prime})}, q_{(\mathrm{S}^{\prime})})_{\mathrm{S}^{\prime}}$; le corollaire résulte des prop. (9.1.4) et (9.1.10).

Proposition (9.1.12). — Avec les notations de (9.1.2) soient z un point de  $X \times_{S} Y$ ,  $x = p(z)$ ,  $y = q(z)$ ; la fibre  $(\mathcal{F} \otimes_{\mathbb{S}} \mathcal{G})_{z}$  est isomorphe à  $(\mathcal{F}_{x} \otimes_{\mathcal{O}_{x}} \mathcal{O}_{z}) \otimes_{\mathcal{O}_{z}} (\mathcal{G}_{y} \otimes_{\mathcal{O}_{y}} \mathcal{O}_{z}) = \mathcal{F}_{x} \otimes_{\mathcal{O}_{x}} \mathcal{O}_{z} \otimes_{\mathcal{O}_{y}} \otimes \mathcal{G}_{y}$ . Comme on peut se ramener au cas affine, la proposition résulte de la formule (1.6.5.1).

Corollaire (9.1.13). — Si F et G sont de type fini, on a

$$
\operatorname{Supp} (\mathcal {F} \otimes_ {\mathrm{s}} \mathcal {G}) = p ^ {- 1} (\operatorname{Supp} (\mathcal {F})) \cap q ^ {- 1} (\operatorname{Supp} (\mathcal {G})).
$$

Comme $p^{*}(\mathcal{F})$ et $q^{*}(\mathcal{G})$ sont de type fini sur $\mathcal{O}_{\mathrm{X}\times_{\mathrm{S}}\mathrm{Y}}$, on est ramené, par (9.1.12) et (0, 1.7.5), au cas particulier où $\mathcal{G} = \mathcal{O}_{\mathrm{Y}}$, c'est-à-dire à démontrer la formule (9.1.13.1) Supp$(p^{-1}(\mathcal{F})) = p^{-1}(\text{Supp}(\mathcal{F}))$.

Le même raisonnement que dans (0, 1.7.5) ramène à vérifier que l'on a, pour tout $z\in\mathbf{X}\times_{\mathbb{S}}\mathbf{Y}$, $\mathcal{O}_{z}/\mathfrak{m}_{x}\mathcal{O}_{z}\neq\mathrm{o}$ (avec $x=p(z)$), ce qui découle du fait que l'homomorphisme $\mathcal{O}_{x}\to\mathcal{O}_{z}$ est local par hypothèse.

Nous laissons au lecteur le soin d'étendre à un produit d'un nombre quelconque de facteurs les résultats démontrés dans ce numéro pour deux facteurs.

## 9.2. Image directe d'un faisceau quasi-cohérent.

Proposition (9.2.1). — Soit $f: \mathrm{X} \to \mathrm{Y}$ un morphisme de préschémas. On suppose qu'il existe un recouvrement $(\mathrm{Y}_{\alpha})$ de $\mathrm{Y}$ par des ouverts affines ayant la propriété suivante : chacun des $f^{-1}(\mathrm{Y}_{\alpha})$ admet un recouvrement fini $(\mathrm{X}_{\alpha i})$ par des ouverts affines contenus dans $f^{-1}(\mathrm{Y}_{\alpha})$, tel que chacune des intersections $\mathrm{X}_{\alpha i} \cap \mathrm{X}_{\alpha j}$ soit elle-même réunion finie d'ouverts affines. Dans ces conditions, pour tout $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent $\mathcal{F}, f_{*}(\mathcal{F})$ est un $\mathcal{O}_{\mathrm{Y}}$-Module quasi-cohérent.

La question étant locale sur Y, on peut supposer Y égal à l'un des  $Y_{\alpha}$ , donc supprimer les indices  $\alpha$ .

a) Supposons d'abord que les  $X_{i} \cap X_{j}$  soient eux-mêmes des ouverts affines. Posons  $F_{i} = F | X_{i}, F_{ij} = F | (X_{i} \cap X_{j})$ , et soient  $F_{i}'$  et  $F_{ij}'$  les images de  $F_{i}$  et  $F_{ij}$  respectivement par les restrictions de f à  $X_{i}$  et  $X_{i} \cap X_{j}$ ; on sait que les  $F_{i}'$  et  $F_{ij}'$  sont quasi-cohérents (1.6.3). Posons  $G = \bigoplus_{i} F_{i}'$ ,  $H = \bigoplus_{i,j} F_{ij}'$ ; G et H sont des  $O_{Y}$-Modules quasi-cohérents; nous allons définir un homomorphisme u :  $G \to H$  tel que  $f_{*}(F)$  soit le noyau de u; il en résultera que  $f_{*}(F)$  est quasi-cohérent (1.3.9). Il suffit de définir u

comme homomorphisme de préfaisceaux ; tenant compte des définitions de $\mathcal{G}$ et $\mathcal{H}$, il suffit donc, pour tout ensemble ouvert $W\subset Y$, de définir un homomorphisme

$$
u _ {\mathrm{W}}: \bigoplus_ {i} \Gamma (f ^ {- 1} (\mathrm{W}) \cap \mathrm{X} _ {i}, \mathscr {F}) \rightarrow \bigoplus_ {i, j} \Gamma (f ^ {- 1} (\mathrm{W}) \cap \mathrm{X} _ {i} \cap \mathrm{X} _ {j}, \mathscr {F})
$$

de façon à satisfaire aux conditions de compatibilité usuelles lorsque W varie. Si, pour toute section $s_i \in \Gamma(f^{-1}(W) \cap X_i, \mathcal{F})$, on désigne par $s_{i|j}$ sa restriction à $f^{-1}(W) \cap X_i \cap X_j$, on posera

$$
u _ {\mathrm{W}} ((s _ {i})) = (s _ {i | j} - s _ {j | i})
$$

et les conditions de compatibilité sont remplies de façon évidente. Pour prouver que le noyau $\mathcal{R}$ de $u$ est $f_{*}(\mathcal{F})$, définissons un homomorphisme de $f_{*}(\mathcal{F})$ dans $\mathcal{R}$ en faisant correspondre à toute section $s \in \Gamma(f^{-1}(\mathbf{W}), \mathcal{F})$ la famille $(s_i)$, où $s_i$ est la restriction de $s$ à $f^{-1}(\mathbf{W}) \cap \mathbf{X}_i$; les axiomes (F1) et (F2) des faisceaux (G, II, 1.1) entraînent que cet homomorphisme est $bijectif$, ce qui termine la démonstration dans ce cas.

b) Dans le cas général, le même raisonnement s'applique une fois que l'on a établi que les $\mathcal{F}_{ij}^{\prime}$ sont quasi-cohérents. Or, par hypothèse, $\mathbf{X}_i\cap \mathbf{X}_j$ est réunion finie d'ouverts affines $\mathbf{X}_{ijk}$; et comme les $\mathbf{X}_{ijk}$ sont des ouverts affines dans un schéma, l'intersection de deux quelconques d'entre eux est encore un ouvert affine (5.5.6). On est donc ramené au premier cas, et (9.2.1) est donc démontrée.

Corollaire (9.2.2). — La conclusion de (9.2.1) est valable dans chacun des cas suivants :

a) f est séparé et quasi-compact.

b) f est séparé et de type fini.

c) f est quasi-compact et l'espace sous-jacent à X est localement noethérien.

Dans le cas $a$), les $\mathbf{X}_{\alpha i} \cap \mathbf{X}_{\alpha j}$ sont affines (5.5.6). Le cas $b$) est un cas particulier de $a$) (6.6.3). Enfin, dans le cas $c$), on peut se ramener au cas où Y est affine et l'espace sous-jacent à X noethérien; alors X admet un recouvrement ouvert affine fini ($\mathbf{X}_i$), et les $\mathbf{X}_i \cap \mathbf{X}_j$, étant quasi-compacts, sont réunions finies d'ouverts affines (2.1.3).

## 9.3. Prolongement des sections de faisceaux quasi-cohérents.

Théorème (9.3.1). — Soit X un préschéma dont l'espace sous-jacent est noethérien, ou un schéma dont l'espace sous-jacent est quasi-compact. Soient $\mathcal{L}$ un $\mathcal{O}_{\mathrm{X}}$-Module inversible (0, 5.4.1), $f$ une section de $\mathcal{L}$ au-dessus de X, $\mathbf{X}_f$ l'ensemble ouvert des $x \in \mathbf{X}$ où $f(x) \neq 0$ (0, 5.5.1), $\mathcal{F}$ un $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent.

(i) $Si s \in \Gamma(\mathbf{X}, \mathcal{F})$ est telle que $s | \mathbf{X}_j = 0$, il existe un entier $n > 0$ tel que $s \otimes f^{\otimes n} = 0$.

(ii) Pour toute section $s \in \Gamma(\mathbf{X}_j, \mathcal{F})$, il existe un entier $n > 0$ tel que $s \otimes f^{\otimes n}$ se prolonge en une section de $\mathcal{F} \otimes \mathcal{L}^{\otimes n}$ au-dessus de $\mathbf{X}$.

(i) Comme l'espace sous-jacent à X est quasi-compact, donc réunion finie d'ouverts affines  $U_{i}$  tels que  $L|U_{i}$  soit isomorphe à  $O_{X}|U_{i}$ , on est ramené au cas où X est affine et  $L=O_{X}$ . Dans ce cas, f's identifie à un élément de A(X) et on a  $\mathbf{X}_{f}=\mathbf{D}(f)$ ; s's identifie à un élément d'un A(X)-module M et  $s|X_{f}$  à l'élément correspondant de  $M_{f}$ , et le résultat est trivial, compte tenu de la définition d'un module de fractions.

(ii) De nouveau X est réunion finie d'ouverts affines  $U_{i}$  ( $i \leqslant i \leqslant r$ ) tels que  $L |U_{i} \cong O_{X}|U_{i}$ , et pour chaque i,  $(s \otimes f^{\otimes n}) |(U_{i} \cap X_{j})$  s'identifie par l'isomorphisme précédent à  $(f |(U_{i} \cap X_{j}))^{n}(s |(U_{i} \cap X_{j}))$ . On sait alors (1.4.1) qu'il existe un entier n>0 tel que pour chaque i,  $(s \otimes f^{\otimes n}) |(U_{i} \cap X_{j})$  se prolonge en une section  $s_{i}$  de  $F \otimes L^{\otimes n}$  au-dessus de  $U_{i}$ . Soit  $s_{i|j}$  la restriction de  $s_{i}$  à  $U_{i} \cap U_{j}$ ; on a par définition  $s_{i|j} - s_{j|i} = o$  dans  $X_{j} \cap U_{i} \cap U_{j}$ . Or, si X est un espace noethérien,  $U_{i} \cap U_{j}$  est quasi-compact; si X est un schéma,  $U_{i} \cap U_{j}$  est un ouvert affine (5.5.6), donc encore quasi-compact. En vertu de (i), il existe donc un entier m (indépendant de i et j) tel que  $(s_{i|j} - s_{j|i}) \otimes f^{\otimes m} = o$ . On conclut aussitôt qu'il existe une section  $s'$  de  $F \otimes L^{\otimes (n+m)}$  au-dessus de X, induisant  $s_{i} \otimes f^{\otimes m}$  au-dessus de chaque  $U_{i}$ , et induisant par suite  $s \otimes f^{\otimes (n+m)}$  au-dessus de  $X_{j}$ .

Les corollaires qui suivent donnent une interprétation du th. (9.3.1) en un langage plus algébrique :

Corollaire (9.3.2). — Les hypothèses étant celles de (9.3.1), considérons l'anneau gradué  $\mathrm{A}_{*}=\Gamma_{*}(\mathcal{L})$  et le  $A_{*}$ -module gradué  $\mathrm{M}_{*}=\Gamma_{*}(\mathcal{L},\mathcal{F})$  (0, 5.4.6). Si  $f\in A_{n}$ , où  $n\in Z$ , alors on a un isomorphisme canonique  $\Gamma(\mathrm{X}_{f},\mathcal{F})\widetilde{\to}((\mathrm{M}_{*})_{f})_{0}$  (sous-groupe du module de fractions  $(\mathrm{M}_{*})_{f}$  formé des éléments de degré o).

Corollaire (9.3.3). — On suppose vérifiées les hypothèses de (9.3.1), et on suppose en outre que $\mathcal{L}=\mathcal{O}_{\mathrm{X}}$. Alors si on pose $\mathrm{A}=\Gamma(\mathrm{X},\mathcal{O}_{\mathrm{X}})$, $\mathrm{M}=\Gamma(\mathrm{X},\mathcal{F})$, le $\mathrm{A}_{f}$-module $\Gamma(\mathrm{X}_{f},\mathcal{F})$ est canoniquement isomorphe à $\mathrm{M}_{f}$.

Proposition (9.3.4). — Soient X un préschéma noethérien, $\mathcal{F}$ un $\mathcal{O}_{\mathrm{X}}$-Module cohérent, $\mathcal{J}$ un faisceau cohérent d'idéaux dans $\mathcal{O}_{\mathrm{X}}$, tels que le support de $\mathcal{F}$ soit contenu dans celui de $\mathcal{O}_{\mathrm{X}}|\mathcal{J}$. Alors il existe un entier $n > 0$ tel que $\mathcal{J}^{n}\mathcal{F} = 0$.

Comme X est réunion finie d'ouverts affines dont les anneaux sont noethériens, on peut supposer X affine d'anneau A noethérien ; alors $\mathcal{F}=\widetilde{\mathrm{M}}$, où $\mathrm{M}=\Gamma(\mathrm{X},\mathcal{F})$ est un A-module de type fini, et $\mathcal{J}=\widetilde{\mathfrak{I}}$, où $\mathfrak{I}=\Gamma(\mathrm{X},\mathcal{J})$ est un idéal de A (1.4.1 et 1.5.1). Comme A est noethérien, $\mathfrak{I}$ admet un système fini de générateurs $f_{i}$ ($1\leqslant i\leqslant m$). Par hypothèse, toute section de $\mathcal{F}$ au-dessus de X est nulle dans chacun des $\mathrm{D}(f_{i})$; si $s_{j}$ ($1\leqslant j\leqslant q$) sont des sections de $\mathcal{F}$ engendrant M, il existe donc un entier $h$ indépendant de $i$ et $j$, tel que $f_{i}^{h}s_{j}=0$ (1.4.1), donc $f_{i}^{h}s=0$ pour tout $s\in\mathrm{M}$. On en conclut que si $n=mh$, on a $\mathfrak{I}^{n}\mathrm{M}=0$, et par suite le $\mathcal{O}_{\mathrm{X}}$-Module correspondant $\mathcal{J}^{n}\mathcal{F}=(\mathfrak{I}^{n}\mathrm{M})^{\sim}$ (1.3.13) est nul.

Corollaire (9.3.5). — Sous les hypothèses de (9.3.4), il existe un sous-préschéma fermé Y de X, dont l'espace sous-jacent est le support de $\mathcal{O}_{\mathrm{X}}/\mathcal{J}$, et tel que, si $j: \mathrm{Y} \to \mathrm{X}$ est l'injection canonique, on ait $\mathcal{F} = j_{*}(j^{*}(\mathcal{F}))$.

Notons d'abord que les supports de $\mathcal{O}_{\mathrm{X}}/\mathcal{J}$ et de $\mathcal{O}_{\mathrm{X}}/\mathcal{J}^{n}$ sont les mêmes car si $\mathcal{J}_{x}=\mathcal{O}_{x}$, on a aussi $\mathcal{J}_{x}^{n}=\mathcal{O}_{x}$, et on a d'autre part $\mathcal{J}_{x}^{n}\subset\mathcal{J}_{x}$ pour tout $x\in\mathrm{X}$. On peut donc en vertu de (9.3.4) supposer que $\mathcal{J}\mathcal{F}=0$; on prend alors pour Y le sous-préschéma fermé de X défini par $\mathcal{J}$, et comme $\mathcal{F}$ est alors un $(\mathcal{O}_{\mathrm{X}}/\mathcal{J})$-Module, la conclusion est immédiate.

## 9.4. Prolongement des faisceaux quasi-cohérents.

(9.4.1) Soient X un espace topologique, $\mathcal{F}$ un faisceau d'ensembles (resp. de groupes, d'anneaux) sur X, U une partie ouverte de X, $\psi: \mathrm{U} \to \mathrm{X}$ l'injection canonique, $\mathcal{G}$ un sous-faisceau de $\mathcal{F} | \mathrm{U} = \psi^*(\mathcal{F})$. Comme $\psi_*$ est exact à gauche, $\psi_*(\mathcal{G})$ est un sous-faisceau de $\psi_*(\psi^*(\mathcal{F}))$; si on considère l'homomorphisme canonique $\rho: \mathcal{F} \to \psi_*(\psi^*(\mathcal{F}))$ (0, 3.5.3), nous désignerons par $\overline{\mathcal{G}}$ le sous-faisceau $\rho^{-1}(\psi_*(\mathcal{G}))$ de $\mathcal{F}$. Il résulte immédiatement des définitions que pour tout ouvert V de X, $\Gamma(V, \overline{\mathcal{G}})$ est formé des sections $s \in \Gamma(V, \mathcal{F})$ dont la restriction à $V \cap U$ soit une section de $\mathcal{G}$ au-dessus de $V \cap U$. On a donc $\overline{\mathcal{G}} | U = \psi^*(\overline{\mathcal{G}}) = \mathcal{G}$, et $\overline{\mathcal{G}}$ est le plus grand sous-faisceau de $\mathcal{F}$ induisant $\mathcal{G}$ sur U; nous dirons que $\overline{\mathcal{G}}$ est le prolongement canonique du sous-faisceau $\mathcal{G}$ de $\mathcal{F} | U$ en un sous-faisceau de $\mathcal{F}$.

Proposition (9.4.2). — Soient X un préschéma, U une partie ouverte de X telle que l'injection canonique j : U→X soit un morphisme quasi-compact (ce qui sera vérifié pour tout U si l'espace sous-jacent X est localement noethérien (6.6.4, (i))). Alors :

(i) Pour tout $(\mathcal{O}_{\mathrm{X}}|\mathrm{U})$-Module quasi-cohérent $\mathcal{G}$, $j_{*}(\mathcal{G})$ est un $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent et on a $j_{*}(\mathcal{G})|\mathrm{U}=j^{*}(j_{*}(\mathcal{G}))=\mathcal{G}$.

(ii) Pour tout $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent $\mathcal{F}$ et tout sous-$(\mathcal{O}_{\mathrm{X}}|\mathrm{U})$-Module quasi-cohérent $\mathcal{G}$, le prolongement canonique $\overline{\mathcal{G}}$ de $\mathcal{G}$ (9.4.1) est un sous-$\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent de $\mathcal{F}$.

Si $j = (\psi, \theta)$ ($\psi$ étant l'injection U→X des espaces sous-jacents), on a par définition $j_*(\mathcal{G}) = \psi_*(\mathcal{G})$ pour tout $(\mathcal{O}_X | U)$-Module $\mathcal{G}$, et en outre $j^*(\mathcal{H}) = \psi^*(\mathcal{H}) = \mathcal{H} | U$ pour tout $\mathcal{O}_X$-Module $\mathcal{H}$ en raison de la définition d'un préschéma induit sur un ouvert. (i) est donc un cas particulier de (9.2.2, a)); pour la même raison, $j_*(j^*(\mathcal{F}))$ est quasi-cohérent, et comme $\overline{\mathcal{G}}$ est l'image réciproque de $j_*(\mathcal{G})$ par l'homomorphisme $\rho : \mathcal{F} \to j_*(j^*(\mathcal{F}))$, (ii) résulte de (4.1.1).

On notera que l'hypothèse que le morphisme $j: \mathrm{U} \to \mathrm{X}$ est quasi-compact est aussi vérifiée lorsque l'ouvert U est quasi-compact et X un schéma : en effet, U est alors réunion finie d'ouverts affines $\mathrm{U}_{i}$, et pour tout ouvert affine V de X, $\mathrm{V} \cap \mathrm{U}_{i}$ est un ouvert affine (5.5.6), donc quasi-compact.

Corollaire (9.4.3). — Soient X un préschéma, U un ouvert quasi-compact de X tel que le morphisme d'injection  $j: U \to X$  soit quasi-compact. Supposons en outre que tout  $O_{X}$ -Module quasi-cohérent soit limite inductive de ses sous- $O_{X}$ -Modules quasi-cohérents de type fini (ce qui a lieu lorsque X est un schéma affine). Soient alors F un  $O_{X}$ -Module quasi-cohérent, G un sous- $(\mathcal{O}_{\mathrm{X}}|U)$ -Module quasi-cohérent de type fini de F|U. Il existe alors un sous- $O_{X}$ -Module quasi-cohérent de type fini  $G'$  de F tel que  $G'|U = G$ .

En effet, on a $\mathcal{G} = \overline{\mathcal{G}}|\mathrm{U}$, et $\overline{\mathcal{G}}$ est quasi-cohérent d'après (9.4.2), donc limite inductive de ses sous-$\mathcal{O}_{\mathbf{x}}$-Modules quasi-cohérents de type fini $\mathcal{H}_{\lambda}$. Par suite $\mathcal{G}$ est limite inductive des $\mathcal{H}_{\lambda}|\mathrm{U}$, donc égal à un des $\mathcal{H}_{\lambda}|\mathrm{U}$ puisqu'il est de type fini (0, 5.2.3).

Remarque (9.4.4). — Supposons que pour tout ouvert affine U ⊂ X le morphisme d'injection U → X soit quasi-compact. Alors si la conclusion de (9.4.3) a lieu pour tout ouvert affine U et tout sous-(Oₓ|U)-Module quasi-cohérent de type fini G de F|U,

il en résulte que $\mathcal{F}$ est limite inductive de ses sous-$\mathcal{O}_{\mathrm{X}}$-Modules quasi-cohérents de type fini. En effet, pour tout ouvert affine $U \subset X$, on a $\mathcal{F}|U = \widetilde{M}$, où $M$ est un A(U)-module, et comme ce dernier est limite inductive de ses sous-modules de type fini, $\mathcal{F}|U$ est limite inductive de ses sous-$(\mathcal{O}_{\mathrm{X}}|U)$-Modules quasi-cohérents de type fini (1.3.9). Or, par hypothèse, chacun de ces sous-Modules est induit sur $U$ par un sous-$\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent de type fini $\mathcal{G}_{\lambda,U}$ de $\mathcal{F}$. Les sommes finies des $\mathcal{G}_{\lambda,U}$ sont encore des $\mathcal{O}_{\mathrm{X}}$-Modules quasi-cohérents de type fini, car la question est locale et le cas où $X$ est affine a été traité dans (1.3.10); il est clair alors que $\mathcal{F}$ est limite inductive de ces sommes finies, d'où notre assertion.

Corollaire (9.4.5). — Sous les hypothèses de (9.4.3), pour tout  $(\mathcal{O}_{\mathrm{X}}|\mathrm{U})$ -Module quasi-cohérent de type fini G, il existe un  $O_{X}$ -Module quasi-cohérent de type fini  $G'$  tel que  $G' | U = G$ .

Comme $\mathcal{F}=j_{*}(\mathcal{G})$ est quasi-cohérent (9.4.2) et $\mathcal{F}|U=\mathcal{G}$, il suffit d'appliquer (9.4.3) à $\mathcal{F}$.

Lemme (9.4.6). — Soient X un préschéma, L un ensemble bien ordonné,  $(\mathrm{V}_{\lambda})_{\lambda\in\mathrm{L}}$  un recouvrement de X par des ouverts affines, U un ouvert de X; pour tout  $\lambda\in L$ , on pose  $W_{\lambda}=\bigcup_{\mu<\lambda}V_{\mu}$ .

On suppose que :  $1^{0}$  Pour tout  $\lambda\in L$ ,  $V_{\lambda}\cap W_{\lambda}$  soit quasi-compact :  $2^{0}$  Le morphisme d'immersion  $U\to X$  est quasi-compact. Alors, pour tout  $O_{X}$ -Module quasi-cohérent F et tout sous- $(\mathcal{O}_{X}|U)$ -Module quasi-cohérent de type fini G de F|U, il existe un sous- $O_{X}$ -Module quasi-cohérent de type fini  $G'$  de F tel que  $G'|U=G$ .

Posons  $U_{\lambda}=U\cup W_{\lambda}$ ; on va définir par récurrence transfinie une famille  $(\mathcal{G}_{\lambda}^{\prime})$ , où  $G_{\lambda}^{\prime}$  est un sous- $(\mathcal{O}_{X}|U_{\lambda})$ -Module quasi-cohérent de type fini de  $F|U_{\lambda}$ , tel que  $G_{\lambda}^{\prime}|U_{\mu}=G_{\mu}^{\prime}$  pour  $\mu<\lambda$  et  $G_{\lambda}^{\prime}|U=G$ . L'unique sous- $O_{X}$ -Module  $G^{\prime}$  de F tel que  $G^{\prime}|U_{\lambda}=G^{\prime}$  pour tout  $\lambda\in L(0,3.3.1)$  répondra à la question. Supposons donc les  $G_{\mu}^{\prime}$  définis et ayant les propriétés précédentes pour  $\mu<\lambda$ ; si  $\lambda$  n'a pas de prédécesseur on prendra pour  $G_{\lambda}^{\prime}$  l'unique sous- $(\mathcal{O}_{X}|U_{\lambda})$ -Module de  $F|U_{\lambda}$  tel que  $G_{\lambda}^{\prime}|U_{\mu}=G_{\mu}^{\prime}$  pour tout  $\mu<\lambda$ , ce qui est licite puisque les  $U_{\mu}$  avec  $\mu<\lambda$  forment alors un recouvrement de  $U_{\lambda}$ . Si au contraire  $\lambda=\mu+1$ , on a  $U_{\lambda}=U_{\mu}\cup V_{\mu}$ , et il suffira de définir un sous- $(\mathcal{O}_{X}|V_{\mu})$ -Module quasi-cohérent de type fini  $G_{\mu}^{\prime\prime}$  de F  $|V_{\mu}$  tel que

$$
\mathcal {G} _ {\mu} ^ {\prime \prime} \left| \left(\mathrm{U} _ {\mu} \cap \mathrm{V} _ {\mu}\right) = \mathcal {G} _ {\mu} ^ {\prime} \right| \left(\mathrm{U} _ {\mu} \cap \mathrm{V} _ {\mu}\right);
$$

on prendra ensuite pour $\mathcal{G}_{\lambda}^{\prime}$ le sous-$(\mathcal{O}_{\mathrm{X}}|\mathrm{U}_{\lambda})$-Module de $\mathcal{F}|\mathrm{U}_{\lambda}$ tel que $\mathcal{G}_{\lambda}^{\prime}|\mathrm{U}_{\mu}=\mathcal{G}_{\mu}^{\prime}$ et $\mathcal{G}_{\lambda}^{\prime}|\mathrm{V}_{\mu}=\mathcal{G}_{\mu}^{\prime\prime}$ (0, 3.3.1). Or, comme $\mathrm{V}_{\mu}$ est affine, l'existence de $\mathcal{G}_{\mu}^{\prime\prime}$ est assurée par (9.4.3) dès que l'on a démontré que $\mathrm{U}_{\mu}\cap\mathrm{V}_{\mu}$ est quasi-compact; mais $\mathrm{U}_{\mu}\cap\mathrm{V}_{\mu}$ est réunion de $\mathrm{U}\cap\mathrm{V}_{\mu}$ et de $\mathrm{W}_{\mu}\cap\mathrm{V}_{\mu}$, qui sont tous deux quasi-compacts en vertu de l'hypothèse.

Théorème (9.4.7). — Soient X un préschéma, U un ouvert de X. On suppose vérifiée l'une des conditions suivantes :

a) L'espace sous-jacent à X est localement noethérien.

b) X est un schéma quasi-compact et U un ouvert quasi-compact.

Pour tout $\mathcal{O}_{\mathrm{x}}$-Module quasi-cohérent $\mathcal{F}$ et tout sous-$(\mathcal{O}_{\mathrm{x}}|\mathrm{U})$-Module quasi-cohérent de type fini $\mathcal{G}$ de $\mathcal{F}|\mathrm{U}$, il existe alors un sous-$\mathcal{O}_{\mathrm{x}}$-Module quasi-cohérent de type fini $\mathcal{G}'$ de $\mathcal{F}$ tel que $\mathcal{G}'|\mathrm{U}=\mathcal{G}$.

Soit  $(\mathrm{V}_{\lambda})_{\lambda\in\mathrm{L}}$  un recouvrement de X par des ouverts affines, L étant supposé fini dans le cas b); L étant muni d'une structure d'ensemble bien ordonné, il suffit de vérifier que les conditions du lemme (9.4.6) sont satisfaites. C'est évident dans l'hypothèse a), les espaces  $V_{\lambda}$  étant noethériens. Dans l'hypothèse b), les  $V_{\lambda}\cap V_{\mu}$  sont affines (5.5.6), donc quasi-compacts, et comme L est fini,  $V_{\lambda}\cap W_{\lambda}$  est quasi-compact. D'où le théorème.

Corollaire (9.4.8). — Sous les hypothèses de (9.4.7), pour tout  $(\mathcal{O}_{\mathrm{X}}|\mathrm{U})$ -Module quasi-cohérent de type fini G, il existe un  $O_{X}$ -Module quasi-cohérent de type fini  $G'$  tel que  $G' | U = G$ .

$$
(9. 4. 7) \text {   à   } \mathcal {F} = j _ {*} (\mathcal {G})
$$

$$
(9. 4. 2)
$$

$$
\mathcal {F} \mid \mathrm{U} = \mathcal {G}
$$

Corollaire (9.4.9). — Soit X un préschéma dont l'espace sous-jacent est localement noethérien, ou un schéma quasi-compact. Alors tout $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent est limite inductive de ses sous-$\mathcal{O}_{\mathrm{X}}$-Modules quasi-cohérents de type fini.

Cela résulte de (9.4.7) et de la remarque (9.4.4).

Corollaire (9.4.10). — Sous les hypothèses de (9.4.9), si un $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent $\mathcal{F}$ est tel que tout sous-$\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent de type fini de $\mathcal{F}$ soit engendré par ses sections au-dessus de X, alors $\mathcal{F}$ est engendré par ses sections au-dessus de X.

En effet, soient U un voisinage ouvert affine d'un point $x \in \mathbf{X}$, et soit $s$ une section de $\mathcal{F}$ au-dessus de U; le sous-$\mathcal{O}_{\mathrm{X}}$-Module $\mathcal{G}$ de $\mathcal{F}|\mathrm{U}$ engendré par $s$ est quasi-cohérent et de type fini, donc il existe un sous-$\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent de type fini $\mathcal{G}'$ de $\mathcal{F}$ tel que $\mathcal{G}'|\mathrm{U} = \mathcal{G}$ (9.4.7). Par hypothèse, il y a donc un nombre fini de sections $t_i$ de $\mathcal{G}'$ au-dessus de X et des sections $a_i$ de $\mathcal{O}_{\mathrm{X}}$ au-dessus d'un voisinage $\mathrm{V} \subset \mathrm{U}$ de $x$ telles que $s|\mathrm{V} = \Sigma a_i \cdot (t_i|\mathrm{V})$, ce qui démontre le corollaire.

## 9.5. Image fermée d'un préschéma. Adhérence d'un sous-préschéma.

Proposition (9.5.1). — Soit $f: \mathbf{X} \to \mathbf{Y}$ un morphisme de préschémas tel que $f_{*}(\mathcal{O}_{\mathbf{X}})$ soit un $\mathcal{O}_{\mathbf{Y}}$-Module quasi-cohérent (ce qui a lieu si $f$ est quasi-compact et si de plus $f$ est séparé ou $\mathbf{X}$ localement noethérien (9.2.2)). Alors il existe un plus petit sous-préschéma $\mathbf{Y}'$ de $\mathbf{Y}$ tel que l'injection canonique $j: \mathbf{Y}' \to \mathbf{Y}$ majore $f$ (ou, ce qui revient au même (4.4.1), tel que le sous-préschéma $f^{-1}(\mathbf{Y}')$ de $\mathbf{X}$ soit identique à $\mathbf{X}$).

De façon plus précise :

Corollaire (9.5.2). — Sous les conditions de (9.5.1), soit $f = (\psi, \theta)$ et soit $\mathcal{J}$ le noyau (quasi-cohérent) de l'homomorphisme $\theta : \mathcal{O}_{\mathrm{Y}} \to f_{*}(\mathcal{O}_{\mathrm{X}})$. Alors le sous-préschéma fermé $\mathrm{Y}'$ de $\mathrm{Y}$ défini par $\mathcal{J}$ vérifie les conditions de (9.5.1).

Comme le foncteur $\psi^{*}$ est exact, la factorisation canonique $\theta : \mathcal{O}_{\mathrm{Y}} \to \mathcal{O}_{\mathrm{Y}} / \mathcal{J} \xrightarrow{\theta'} \psi_{*}(\mathcal{O}_{\mathrm{X}})$ donne (0, 3.5.4.3) une factorisation $\theta^{\#} : \psi^{*}(\mathcal{O}_{\mathrm{Y}}) \to \psi^{*}(\mathcal{O}_{\mathrm{Y}}) / \psi^{*}(\mathcal{J}) \xrightarrow{\theta'^\#} \mathcal{O}_{\mathrm{X}}$; comme pour tout $x \in \mathbf{X}$, $\theta_{x}^{\#}$ est un homomorphisme local, il en est de même de $\theta_{x}^{\prime \#}$; si on désigne par $\psi_{0}$ l'application continue $\psi$ considérée comme application de X dans $\mathbf{X}'$, par $\theta_{0}$ la restriction $\theta' | \mathbf{X}' : (\mathcal{O}_{\mathrm{Y}} / \mathcal{J}) | \mathbf{X}' \to \psi_{*}(\mathcal{O}_{\mathrm{X}}) | \mathbf{X}' = (\psi_{0})_{*}(\mathcal{O}_{\mathrm{X}})$, on voit donc que $f_{0} = (\psi_{0}, \theta_{0})$ est un morphisme de préschémas $\mathbf{X} \to \mathbf{X}'$ (2.2.1) tel que $f = j_0 f_0$. Si maintenant $\mathbf{X}''$

est un second sous-préschéma fermé de Y, défini par un faisceau quasi-cohérent d'idéaux $\mathcal{J}'$ de $\mathcal{O}_{\mathrm{Y}}$, et tel que l'injection $j': \mathrm{X}'' \to \mathrm{Y}$ majore $f$, on doit tout d'abord avoir $\mathrm{X}'' \supset \psi(\mathrm{X})$, donc $\mathrm{X}' \subset \mathrm{X}''$ puisque $\mathrm{X}''$ est fermé. En outre, pour tout $y \in \mathrm{X}''$, $\theta$ doit se factoriser en $\mathcal{O}_y \to \mathcal{O}_y / \mathcal{J}_y' \to (\psi_*(\mathcal{O}_{\mathrm{X}}))_y$, ce qui par définition entraîne $\mathcal{J}_y' \subset \mathcal{J}_y$, et par suite $\mathrm{X}'$ est un sous-préschéma fermé de $\mathrm{X}''$ (4.1.10).

Définition (9.5.3). — Lorsqu'il existe un plus petit sous-préschéma fermé Y' de Y tel que l'injection canonique $j: \mathrm{Y}' \to \mathrm{Y}$ majore $f$, on dit que Y' est le préschéma image fermée de X par le morphisme $f$.

Proposition (9.5.4). — Si $f_{*}(\mathcal{O}_{\mathrm{X}})$ est un $\mathcal{O}_{\mathrm{Y}}$-Module quasi-cohérent, l'espace sous-jacent de l'image fermée de X par f est l'adhérence $\overline{f(\mathbf{X})}$ dans Y.

Comme le support de $f_{*}(\mathcal{O}_{\mathrm{X}})$ est contenu dans $f(\overline{\mathbf{X}})$, on a (avec les notations de (9.5.2)) $\mathcal{J}_y = \mathcal{O}_y$ pour $y \notin f(\overline{\mathbf{X}})$, donc le support de $\mathcal{O}_{\mathrm{Y}} / \mathcal{J}$ est contenu dans $f(\overline{\mathbf{X}})$. En outre, ce support est fermé et contient $f(\mathbf{X})$: en effet, si $y \in f(\mathbf{X})$, l'élément unité de l'anneau $(\psi_{*}(\mathcal{O}_{\mathrm{X}}))_y$ n'est pas nul, étant le germe en $y$ de la section

$$
\mathrm{I} \in \Gamma (\mathrm{X}, \mathcal {O} _ {\mathrm{X}}) = \Gamma (\mathrm{Y}, \psi_ {*} (\mathcal {O} _ {\mathrm{X}}));
$$

comme il est l'image par $\theta$ de l'élément unité de $\mathcal{O}_{y}$, ce dernier n'appartient pas à $\mathcal{J}_{y}$, donc $\mathcal{O}_{y}/\mathcal{J}_{y} \neq 0$; ceci achève la démonstration.

Proposition (9.5.5) (transitivité des images fermées). — Soient $f: \mathbf{X} \to \mathbf{Y}$ et $g: \mathbf{Y} \to \mathbf{Z}$ deux morphismes de préschémas ; on suppose que l'image fermée $\mathbf{Y}'$ de $\mathbf{X}$ par $f$ existe, et que, si $g'$ est la restriction de $g$ à $\mathbf{Y}'$, l'image fermée $\mathbf{Z}'$ de $\mathbf{Y}'$ par $g'$ existe. Alors l'image fermée de $\mathbf{X}$ par go$f$ existe et est égale à $\mathbf{Z}'$.

Il suffit (9.5.1) de montrer que $Z'$ est le plus petit sous-préschéma fermé $Z_1$ de $Z$ tel que le sous-préschéma fermé $(g\circ f)^{-1}(Z_1)$ de $X$ (égal à $f^{-1}(g^{-1}(Z_1))$ par (4.4.2)) soit égal à $X$; il revient au même de dire que $Z'$ est le plus petit sous-préschéma fermé de $Z$ tel que $f$ soit majoré par l'injection $g^{-1}(Z_1)\to Y$ (4.4.1). Or, en vertu de l'existence de l'image fermée $Y'$, tout $Z_1$ ayant cette propriété est tel que $g^{-1}(Z_1)$ majore $Y'$, ce qui équivaut à dire que $j^{-1}(g^{-1}(Z_1)) = g'^{-1}(Z_1) = Y'$ en désignant par $j$ l'injection $Y'\to Y$. Par définition de $Z'$, on en conclut bien que $Z'$ est le plus petit sous-préschéma fermé de $Z$ vérifiant la condition précédente.

Corollaire (9.5.6). — Soit $f: \mathbf{X} \to \mathbf{Y}$ un S-morphisme tel que Y soit l'image fermée de X par $f$. Soit Z un S-schéma; si deux S-morphismes $g_{1}, g_{2}$ de Y dans Z sont tels que $g_{1} \circ f = g_{2} \circ f$, alors $g_{1} = g_{2}$.

Soit $h = (g_1, g_2)_\mathrm{s} : \mathrm{Y} \to \mathrm{Z} \times_{\mathrm{s}} \mathrm{Z}$; comme la diagonale $\mathrm{T} = \Delta_{\mathrm{Z}}(\mathrm{Z})$ est un sous-préschéma fermé de $\mathrm{Z} \times_{\mathrm{s}} \mathrm{Z}$, $\mathrm{Y}' = h^{-1}(\mathrm{T})$ est un sous-préschéma fermé de $\mathrm{Y}$ (4.4.1). Posons $u = g_1 \circ f = g_2 \circ f$; on a alors par définition du produit $h' = h \circ f = (u, u)_\mathrm{s}$, donc $h \circ f = \Delta_{\mathrm{Z}} \circ u$; comme $\Delta_{\mathrm{Z}}^{-1}(\mathrm{T}) = \mathrm{Z}$, on a $h'^{-1}(\mathrm{T}) = u^{-1}(\mathrm{Z}) = \mathrm{X}$, donc $f^{-1}(\mathrm{Y}') = \mathrm{X}$. On en conclut (4.4.1) que l'injection canonique $\mathrm{Y}' \to \mathrm{Y}$ majore $f$, donc $\mathrm{Y}' = \mathrm{Y}$ par hypothèse; par suite (4.4.1), $h$ se factorise en $\Delta_{\mathrm{Z}} \circ v$, où $v$ est un morphisme $\mathrm{Y} \to \mathrm{Z}$, ce qui entraîne $g_1 = g_2 = v$.

Remarque (9.5.7). — Si X et Y sont des S-schémas, la prop. (9.5.6) signifie que

lorsque Y est l'image fermée de X par f, f est un épimorphisme dans la catégorie des S-schémas (T, 1.1). Nous démontrerons au chap. V que, réciproquement, si l'image fermée Y' de X par f existe et si f est un épimorphisme de S-schémas, alors on a nécessairement Y' = Y.

Proposition (9.5.8). — Supposons vérifiées les hypothèses de (9.5.1), et soit Y' l'image fermée de X par f. Pour tout ouvert V de Y, soit  $f_{\mathrm{V}}:f^{-1}(\mathrm{V})\to\mathrm{V}$  la restriction de f; alors l'image fermée de  $f^{-1}(\mathrm{V})$  par  $f_{V}$  dans V existe et est égale au préschéma induit par Y' sur l'ouvert  $V\cap Y'$  de Y' (autrement dit, au sous-préschéma inf(V, Y') de Y (4.4.3)).

Posons  $X' = f^{-1}(V)$ ; comme l'image directe de  $O_{X'}$  par  $f_{V}$  n'est autre que la restriction de  $f_{*}(\mathcal{O}_{\mathrm{X}})$  à V, il est clair que le noyau  $J'$  de l'homomorphisme  $\mathcal{O}_{\mathrm{V}} \to (f_{\mathrm{V}})_{*}(\mathcal{O}_{\mathrm{X'}})$  est la restriction de J à V, d'où aussitôt la proposition.

On notera que ce résultat s'interprète en disant que la formation de l'image fermée commute à une extension  $Y_{1} \rightarrow Y$  du préschéma de base, qui est une immersion ouverte. Nous verrons au chap. IV qu'il en est de même pour une extension  $Y_{1} \rightarrow Y$  qui est un morphisme plat, pourvu que f soit séparé et quasi-compact.

Proposition (9.5.9). — Soit $f: \mathbf{X} \to \mathbf{Y}$ un morphisme tel que l'image fermée $\mathbf{Y}'$ de $\mathbf{X}$ par $f$ existe.

(i) Si X est réduit, il en est de même de Y'.

(ii) Si on suppose vérifiées les hypothèses de (9.5.1) et si X est irréductible (resp. intègre), il en est de même de Y'.

Par hypothèse, le morphisme $f$ se factorise en $\mathbf{X} \xrightarrow{g} \mathbf{Y}' \xrightarrow{1} \mathbf{Y}$, où $j$ est l'injection canonique. Comme $\mathbf{X}$ est réduit, $g$ se factorise en $\mathbf{X} \xrightarrow{h} \mathbf{Y}'_{\text{red}} \xrightarrow{j'} \mathbf{Y}'$ où $j'$ est l'injection canonique (5.2.2), et il résulte alors de la définition de $\mathbf{Y}'$ que $\mathbf{Y}'_{\text{red}} = \mathbf{Y}'$. Si de plus les conditions de (9.5.1) sont remplies, il résulte de (9.5.4) que $f(\mathbf{X})$ est dense dans $\mathbf{Y}'$; si $\mathbf{X}$ est irréductible, il en est donc de même de $\mathbf{Y}'$ (0, 2.1.5). L'assertion relative aux préschémas intègres résulte de la conjonction des deux autres.

Proposition (9.5.10). — Soit Y un sous-préschéma d'un préschéma X, tel que l'injection canonique i : Y→X soit un morphisme quasi-compact. Il existe alors un plus petit sous-préschéma fermé  $\overline{Y}$  de X majorant Y ; son espace sous-jacent est l'adhérence de celui de Y ; ce dernier est ouvert dans son adhérence, et le préschéma Y est induit sur cet ouvert par  $\overline{Y}$ .

Il suffit d'appliquer (9.5.1) à l'injection $j$, qui est séparée (5.5.1) et quasi-compacte par hypothèse ; (9.5.1) prouve donc l'existence de $\overline{\mathbf{Y}}$ et (9.5.4) montre que son espace sous-jacent est l'adhérence de Y dans X ; comme Y est localement fermé dans X, il est ouvert dans $\overline{\mathbf{Y}}$, et la dernière assertion provient de (9.5.8) appliqué à un ouvert V de X tel que Y soit fermé dans V.

Avec ces notations, si l'injection  $V \rightarrow X$  est quasi-compacte, et si J est le faisceau quasi-cohérent d'idéaux de  $O_{X}|V$  définissant le sous-préschéma fermé Y de V, il résulte de (9.5.1) que le faisceau quasi-cohérent d'idéaux de  $O_{X}$  définissant  $\overline{Y}$  est le prolongement canonique (9.4.1)  $\overline{J}$  de J, car c'est évidemment le plus grand sous-faisceau d'idéaux quasi-cohérent de  $O_{X}$  induisant J sur V.

Corollaire (9.5.11). — Sous les hypothèses de (9.5.10), toute section de $\mathcal{O}_{\overline{\mathrm{Y}}}$ au-dessus d'un ouvert V de $\overline{\mathrm{Y}}$ qui est nulle dans $\mathrm{V} \cap \mathrm{Y}$ est nulle.

En vertu de (9.5.8), on peut se ramener au cas où  $V = \overline{Y}$ . Si l'on tient compte de ce que les sections de  $O_{\overline{Y}}$  au-dessus de  $\overline{Y}$  correspondent canoniquement aux  $\overline{Y}$ -sections de  $\overline{Y} \otimes_{z} Z[T]$  (3.3.15) et de ce que ce dernier est séparé sur  $\overline{Y}$ , le corollaire apparaît comme un cas particulier de (9.5.6).

Lorsqu'il existe un plus petit sous-préschéma fermé Y de X majorant un sous-préschéma Y de X, on dit que Y' est l'adhérence de Y dans X, lorsqu'il n'en résulte pas de confusion.

## 9. 6. Faisceaux quasi-cohérents d'algèbres ; changement du faisceau structural.

Proposition (9.6.1). — Soient X un préschéma, B une  $O_{X}$ -Algèbre quasi-cohérente (0, 5.1.3). Pour qu'un B-Module F soit quasi-cohérent (sur l'espace annelé (X, B)), il faut et il suffit que F soit un  $O_{X}$ -Module quasi-cohérent.

Comme la question est locale, on peut supposer X affine d'anneau A, et alors $\mathcal{B} = \widetilde{\mathbf{B}}$, où B est une A-algèbre (1.4.3). Si $\mathcal{F}$ est quasi-cohérent sur l'espace annelé (X, $\mathcal{B}$), on peut aussi supposer que $\mathcal{F}$ est le conoyau d'un $\mathcal{B}$-homomorphisme $\mathcal{B}^{(I)} \to \mathcal{B}^{(J)}$; comme cet homomorphisme est aussi un $\mathcal{O}_{\mathrm{X}}$-homomorphisme de $\mathcal{O}_{\mathrm{X}}$-Modules, et que $\mathcal{B}^{(I)}$ et $\mathcal{B}^{(J)}$ sont des $\mathcal{O}_{\mathrm{X}}$-Modules quasi-cohérents (1.3.9, (ii)), $\mathcal{F}$ est aussi un $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent (1.3.9, (i)).

Inversement, si $\mathcal{F}$ est un $\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent, on a $\mathcal{F} = \widetilde{\mathbf{M}}$, où $\mathbf{M}$ est un B-module (1.4.3); $\mathbf{M}$ est isomorphe à un conoyau de B-homomorphisme $\mathbf{B}^{(I)} \to \mathbf{B}^{(J)}$, donc $\mathcal{F}$ est un $\mathcal{B}$-Module isomorphe au conoyau de l'homomorphisme correspondant $\mathcal{B}^{(I)} \to \mathcal{B}^{(J)}$ (1.3.13), ce qui achève la démonstration.

En particulier, si $\mathcal{F}$ et $\mathcal{G}$ sont deux $\mathcal{B}$-Modules quasi-cohérents, $\mathcal{F} \otimes_{\mathcal{B}} \mathcal{G}$ est un $\mathcal{B}$-Module quasi-cohérent; il en est de même de $\mathcal{Hom}_{\mathcal{B}}(\mathcal{F}, \mathcal{G})$ lorsqu'on suppose en outre que $\mathcal{F}$ admet une présentation finie (1.3.13).

(9.6.2) Étant donné un préschéma X, nous dirons qu'une $\mathcal{O}_{\mathrm{X}}$-Algèbre quasi-cohérente $\mathcal{B}$ est de type fini si pour tout $x \in \mathrm{X}$, il existe un voisinage ouvert affine U de $x$ tel que $\Gamma(\mathrm{U}, \mathcal{B}) = \mathrm{B}$ soit une algèbre de type fini sur $\Gamma(\mathrm{U}, \mathcal{O}_{\mathrm{X}}) = \mathrm{A}$. On a alors $\mathcal{B} | \mathrm{U} = \widetilde{\mathrm{B}}$ et pour tout $f \in \mathrm{A}$, la $(\mathcal{O}_{\mathrm{X}} | \mathrm{D}(f))$-Algèbre induite $\mathcal{B} | \mathrm{D}(f)$ est de type fini, car elle est isomorphe à $(\mathrm{B}_f)^\sim$, et $\mathrm{B}_f = \mathrm{B} \otimes_{\mathrm{A}} \mathrm{A}_f$ est évidemment une algèbre de type fini sur $\mathrm{A}_f$. Comme les $\mathrm{D}(f)$ forment une base de la topologie de U, on en conclut que si $\mathcal{B}$ est une $\mathcal{O}_{\mathrm{X}}$-Algèbre quasi-cohérente de type fini, pour tout ouvert V de X, $\mathcal{B} | \mathrm{V}$ est une $(\mathcal{O}_{\mathrm{X}} | \mathrm{V})$-Algèbre quasi-cohérente de type fini.

Proposition (9.6.3). — Soit X un préschéma localement noethérien. Toute $\mathcal{O}_{\mathrm{X}}$-Algèbre quasi-cohérente de type fini $\mathcal{B}$ est alors un faisceau cohérent d'anneaux (0, 5.3.7).

On peut de nouveau se limiter au cas où X est un schéma affine d'anneau noethérien A, et où $\mathcal{B}=\widetilde{\mathrm{B}}$, B étant une A-algèbre de type fini; B est donc un anneau noethérien. Cela étant, il faut prouver que le noyau $\mathcal{N}$ d'un $\mathcal{B}$-homomorphisme $\mathcal{B}^{m}\to\mathcal{B}$ est un $\mathcal{B}$-

Module de type fini ; or, il est isomorphe (en tant que $\mathcal{B}$-Module) à $\widetilde{\mathbf{N}}$, où $\mathbf{N}$ est le noyau de l'homomorphisme correspondant de B-modules $\mathbf{B}^{m} \to \mathbf{B}$ (1.3.13). Comme B est noethérien, le sous-module N de $\mathbf{B}^{m}$ est un B-module de type fini, donc il existe un homomorphisme $\mathbf{B}^{p} \to \mathbf{B}^{m}$ d'image N ; la suite $\mathbf{B}^{p} \to \mathbf{B}^{m} \to \mathbf{B}$ étant exacte, il en est de même de la suite $\mathcal{B}^{p} \to \mathcal{B}^{m} \to \mathcal{B}$ correspondante (1.3.5) et comme $\mathcal{N}$ est l'image de $\mathcal{B}^{p} \to \mathcal{B}^{m}$ (1.3.9, (i)), la proposition est démontrée.

Corollaire (9.6.4). — Sous les hypothèses de (9.6.3), pour qu'un B-Module F soit cohérent, il faut et il suffit qu'il soit un  $O_{X}$ -Module quasi-cohérent et un B-Module de type fini. S'il en est ainsi, et si G est un sous-B-Module ou un B-Module quotient de F, pour que G soit un B-Module cohérent, il faut et il suffit que G soit un  $O_{X}$ -Module quasi-cohérent.

Compte tenu de (9.6.1), les conditions sur $\mathcal{F}$ sont évidemment nécessaires; montrons qu'elles sont suffisantes. On peut se limiter au cas où X est affine d'anneau noethérien A, $\mathcal{B} = \widetilde{\mathbf{B}}$, où B est une A-algèbre de type fini, $\mathcal{F} = \widetilde{\mathbf{M}}$, où M est un B-module, et où il existe un $\mathcal{B}$-homomorphisme surjectif $\mathcal{B}^m \to \mathcal{F} \to 0$. On a alors une suite exacte correspondante $B^m \to M \to 0$, donc M est un B-module de type fini; en outre, le noyau P de l'homomorphisme $B^m \to M$ est alors un B-module de type fini, puisque B est noethérien. On en conclut (1.3.13) que $\mathcal{F}$ est le conoyau d'un $\mathcal{B}$-homomorphisme $\mathcal{B}^m \to \mathcal{B}^n$, et est donc cohérent puisque $\mathcal{B}$ est un faisceau cohérent d'anneaux (0, 5.3.4). Le même raisonnement montre qu'un sous-$\mathcal{B}$-Module (resp. un $\mathcal{B}$-Module quotient) quasi-cohérent de $\mathcal{F}$ est de type fini, d'où la seconde partie du corollaire.

Proposition (9.6.5). — Soit X un schéma quasi-compact ou un préschéma dont l'espace sous-jacent est noethérien. Pour toute $\mathcal{O}_{\mathrm{X}}$-Algèbre quasi-cohérente de type fini $\mathcal{B}$, il existe un sous-$\mathcal{O}_{\mathrm{X}}$-Module quasi-cohérent de type fini $\mathcal{E}$ de $\mathcal{B}$ tel que $\mathcal{E}$ engendre (0, 4.1.4) la $\mathcal{O}_{\mathrm{X}}$-Algèbre $\mathcal{B}$.

En effet, il existe par hypothèse un recouvrement fini  $(\mathbf{U}_{i})$  de X formé d'ouverts affines tels que  $\Gamma(\mathbf{U}_{i},\mathcal{B})=\mathbf{B}_{i}$  soit une algèbre de type fini sur  $\Gamma(\mathbf{U}_{i},\mathcal{O}_{\mathbf{X}})=\mathbf{A}_{i}$ ; soit  $E_{i}$  un sous- $A_{i}$ -module de type fini de  $B_{i}$  engendrant la  $A_{i}$ -algèbre  $B_{i}$ ; en vertu de (9.4.7), il existe un sous- $O_{X}$ -Module  $E_{i}$  de B, quasi-cohérent et de type fini, tel que  $E_{i}|U_{i}=\widetilde{E}_{i}$ . Il est clair que la somme E des  $E_{i}$  répond à la question.

Proposition (9.6.6). — Soit X un préschéma dont l'espace sous-jacent est localement noethérien, ou un schéma quasi-compact. Alors toute $\mathcal{O}_{\mathrm{X}}$-Algèbre quasi-cohérente $\mathcal{B}$ est limite inductive de ses sous-$\mathcal{O}_{\mathrm{X}}$-Algèbres quasi-cohérentes de type fini.

En effet, il résulte de (9.4.9) que $\mathcal{B}$ est limite inductive (en tant que $\mathcal{O}_{\mathrm{x}}$-Module) de ses sous-$\mathcal{O}_{\mathrm{x}}$-Modules quasi-cohérents de type fini; ces derniers engendrent des sous-$\mathcal{O}_{\mathrm{x}}$-Algèbres quasi-cohérentes de type fini de $\mathcal{B}$ (1.3.14), dont $\mathcal{B}$ est a fortiori limite inductive.

## § 10. SCHÉMAS FORMELS

## 10.1. Schémas formels affines.

(10.1.1) Soit A un anneau topologique admissible (0, 7.1.2); pour tout idéal de définition J de A, Spec(A/J) s'identifie au sous-espace fermé V(J) de Spec(A) (1.1.11), ensemble des idéaux premiers ouverts de A; cet espace topologique ne dépend pas de

l'idéal de définition $\mathfrak{J}$ considéré ; notons-le $\mathfrak{X}$. Soit $(\mathfrak{J}_{\lambda})$ un système fondamental de voisinages de o dans A, formé d'idéaux de définition, et pour tout $\lambda$, soit $\mathcal{O}_{\lambda}$ le faisceau structural de $\operatorname{Spec}(\mathrm{A}/\mathfrak{J}_{\lambda})$; ce faisceau est induit sur $\mathfrak{X}$ par $\widetilde{\mathrm{A}}/\widetilde{\mathfrak{J}}_{\lambda}$ (lequel est nul hors de $\mathfrak{X}$). Pour $\mathfrak{J}_{\mu} \subset \mathfrak{J}_{\lambda}$, l'homomorphisme canonique $\mathrm{A}/\mathfrak{J}_{\mu} \to \mathrm{A}/\mathfrak{J}_{\lambda}$ définit donc un homomorphisme $u_{\lambda\mu}: \mathcal{O}_{\mu} \to \mathcal{O}_{\lambda}$ de faisceaux d'anneaux (1.6.1), et $(\mathcal{O}_{\lambda})$ est un système projectif de faisceaux d'anneaux pour ces homomorphismes. Comme la topologie de $\mathfrak{X}$ admet une base formée d'ouverts quasi-compacts, on peut associer à tout $\mathcal{O}_{\lambda}$ un faisceau d'anneaux topologiques pseudo-discrets (0, 3.8.1) qui a $\mathcal{O}_{\lambda}$ comme faisceau d'anneaux (sans topologie) sous-jacent, et que nous noterons encore $\mathcal{O}_{\lambda}$; et les $\mathcal{O}_{\lambda}$ forment encore un système projectif de faisceaux d'anneaux topologiques (0, 3.8.2). Nous désignerons par $\mathcal{O}_{\mathfrak{X}}$ le faisceau d'anneaux topologiques sur $\mathfrak{X}$, limite projective du système $(\mathcal{O}_{\lambda})$; pour tout ouvert quasi-compact U de $\mathfrak{X}$, $\Gamma(\mathrm{U}, \mathcal{O}_{\mathfrak{X}})$ est donc l'anneau topologique limite projective du système d'anneaux discrets $\Gamma(\mathrm{U}, \mathcal{O}_{\lambda})$ (0, 3.2.6).

Définition (10.1.2). — Étant donné un anneau topologique admissible A, on appelle spectre formel de A et on note Spf(A) le sous-espace fermé $\mathfrak{X}$ de Spec(A) formé des idéaux premiers ouverts de A. On dit qu'un espace topologiquement annelé est un schéma formel affine s'il est isomorphe à un spectre formel Spf(A) = $\mathfrak{X}$ muni du faisceau d'anneaux topologiques $\mathcal{O}_{\mathfrak{X}}$ limite projective des faisceaux d'anneaux pseudo-discrets $(\widetilde{\mathrm{A}} / \widetilde{\mathfrak{J}}_{\lambda}) \mid \mathfrak{X}$, où $\mathfrak{J}_{\lambda}$ parcourt l'ensemble filtrant des idéaux de définition de A.

Quand nous parlerons d'un spectre formel $\mathfrak{X}=\mathrm{Spf}(\mathrm{A})$ comme d'un schéma formel affine, il s'agira toujours de l'espace topologiquement annelé $(\mathfrak{X},\mathcal{O}_{\mathfrak{X}})$ où $\mathcal{O}_{\mathfrak{X}}$ est défini comme ci-dessus.

On notera que tout schéma affine  $\mathbf{X}=\operatorname{Spec}(\mathbf{A})$  peut être considéré comme un schéma formel affine d'une seule manière, en considérant A comme un anneau topologique discret : les anneaux topologiques  $\Gamma(\mathbf{U},\mathcal{O}_{\mathbf{X}})$  sont alors discrets lorsque U est quasi-compact (mais non en général lorsque U est un ouvert quelconque de X).

Proposition (10.1.3). — Si $\mathfrak{X} = \operatorname{Spf}(A)$, où $A$ est un anneau admissible, $\Gamma(\mathfrak{X},\mathcal{O}_{\mathfrak{X}})$ est topologiquement isomorphe à $A$.

En effet, comme $\mathfrak{X}$ est fermé dans $\operatorname{Spec}(\mathbf{A})$, il est quasi-compact, et par suite $\Gamma(\mathfrak{X}, \mathcal{O}_{\mathfrak{X}})$ est topologiquement isomorphe à la limite projective des anneaux discrets $\Gamma(\mathfrak{X}, \mathcal{O}_{\lambda})$; mais $\Gamma(\mathfrak{X}, \mathcal{O}_{\lambda})$ est isomorphe à $\mathbf{A}/\mathfrak{J}_{\lambda}$ (1.3.7); comme A est séparé et complet, il est topologiquement isomorphe à $\lim_{\mathbf{A}} \mathbf{A}/\mathfrak{J}_{\lambda}$ (0, 7.2.1), d'où la proposition.

Proposition (10.1.4). — Soient A un anneau admissible, $\mathfrak{X}=\mathrm{Spf}(A)$, et pour tout $f\in\mathbf{A}$, soit $\mathfrak{D}(f)=\mathbf{D}(f)\cap\mathfrak{X}$; l'espace topologiquement annelé $(\mathfrak{D}(f),\mathcal{O}_{\mathfrak{X}}|\mathfrak{D}(f))$ est isomorphe au spectre formel affine $\mathrm{Spf}(\mathrm{A}_{\{f\}})$ (0, 7.6.15).

Pour tout idéal de définition $\mathfrak{J}$ de A, l'anneau discret $S_{f}^{-1}A/S_{f}^{-1}\mathfrak{J}$ s'identifie canoniquement à $A_{\{f\}}/\mathfrak{J}_{\{f\}}$ (0, 7.6.9), donc (1.2.5 et 1.2.6), l'espace topologique $\operatorname{Spf}(A_{\{f\}})$ s'identifie canoniquement à $\mathfrak{D}(f)$. En outre, pour tout ouvert quasi-compact U de $\mathfrak{X}$ contenu dans $\mathfrak{D}(f)$, $\Gamma(U, \mathcal{O}_{\lambda})$ s'identifie au module des sections du faisceau structural de $\operatorname{Spec}(S_{f}^{-1}A/S_{f}^{-1}\mathfrak{J}_{\lambda})$ au-dessus de U (1.3.6), donc, si on pose $\mathfrak{Y}=\operatorname{Spf}(A_{\{f\}})$, $\Gamma(U, \mathcal{O}_{\mathfrak{X}})$ s'identifie au module des sections $\Gamma(U, \mathcal{O}_{\mathfrak{Y}})$, ce qui démontre la proposition.