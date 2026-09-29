# Chtoucas de Drinfeld et correspondance de Langlands

Laurent Lafforgue

Universite de Paris-Sud, UMR 8628 du CNRS, Math´ ematique, bât. 425,´ 91405 Orsay Cedex, France

Institut des Hautes Etudes Scientifiques, Le Bois-Marie, 35, route de Chartres,<sup>´</sup> 91440 Bures-Sur-Yvette, France

Oblatum 13-X-2000 & 7-VI-2001

Published online: 12 October 2001 –  Springer-Verlag 2001

Resum´ e.´ On demontre la correspondance de Langlands pour´$\mathrm { G L } _ { r }$sur les corps de fonctions. La preuve gen´ eralise celle de Drinfeld en rang 2 : elle´ consiste à realiser la correspondance en rang´ r dans la cohomologie -adique des variet´ es modulaires de chtoucas de Drinfeld de rang´ r.

Abstract. One proves Langlands’ correspondence for$\mathrm { G L } _ { r }$over function fields. This is a generalization of Drinfeld’s proof in the case of rank 2 : Langlands’ correspondence is realized in -adic cohomology spaces of the modular varieties classifying rank r Drinfeld shtukas.

## Introduction

L’objet de ce travail est de demontrer la correspondance de Langlands pour´ les groupes lineaires´$\mathrm { G L } _ { r }$sur les corps de fonctions. La preuve gen´ eralise´ celle de Drinfeld en rang 2 : elle consiste à realiser la correspondance en´ rang r arbitraire dans la cohomologie -adique des variet´ es (ou plutôt des´ champs) de chtoucas de Drinfeld de rang r. On s’appuie sur differents´ travaux preparatoires effectu´ es pr´ ec´ edemment par l’auteur : le calcul au´ moyen de la formule des traces d’Arthur-Selberg des nombres de points fixes dans les variet´ es de chtoucas convenablement tronqu´ ees, dans le livre´ [Lafforgue,$1 9 9 7 ]$, et la compactification dans l’article [Lafforgue, 1998] des variet´ es de chtoucas sans structures de niveau en vari´ et´ es de “chtoucas´ iter´ es”.´

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Code matière AMS (2000) : 11F, 11F52, 11F60, 11F66, 11F70, 11F72, 11F80, 11R39, 14G35, 14H60, 22E55.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Mots cles :´ Chtoucas – Variet´ es modulaires de Drinfeld – Modules des fibr´ es sur les courbes´ – Correspondance de Langlands – Corps de fonctions – Representations galoisiennes –´ Representations automorphes – Fonctions L – Cohomologie´ -adique – Correspondances de Hecke – Formule des traces d’Arthur-Selberg – Formule des points fixes de Grothendieck-Lefschetz</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Key words : Shtukas – Drinfeld modular varieties – Moduli of vector bundles over curves – Langlands’ correspondence – Function fields – Galois representations – Automorphic representations – L-functions – -adic cohomology – Hecke correspondences – Arthur-Selberg trace formula – Grothendieck-Lefschetz fixed points formula</span></small>

On considère donc une courbe X projective, lisse et geom´ etriquement´ connexe sur un corps fini$\mathbb { F } _ { q }$à$q$el´ ements et´ F le corps des fonctions rationnelles sur la courbe X. On note${ \bf G } _ { F }$le groupe de Galois de$F , \ | X |$ l’ensemble des points fermes de´ X identifies aux places de´ F,$\mathbb { A } = \prod _ { x \in | X | } F _ { x }$

l’anneau des adèles de F et$O _ { \mathbb { A } } = \prod _ { x \in | X | } O _ { x }$son sous-anneau des entiers.

On fixe un nombre premier  qui ne divise pas$q .$. Pour tout entier $r \geq 1$, on designe par´$\bar { \mathcal { A } } ^ { \bar { r } } ( F )$l’ensemble des representations automorphes´ cuspidales irreductibles´$\pi$de$\mathrm { G L } _ { r } ( \mathbb { A } )$(ou de son algèbre de convolution${ \mathcal { H } } ^ { r }$ appelee algèbre de Hecke) dont le caractère central´$\chi _ { \pi }$est d’ordre fini et par$\mathcal { G } _ { \ell } ^ { r } ( F )$l’ensemble des representations ´ -adiques de${ \bf G } _ { F }$qui sont presque partout non ramifiees et irr´ eductibles de dimension´ r et dont le determinant´ est d’ordre fini.

La correspondance de Langlands sur le corps de fonctions F s’enonce :´

Theor´ eme.\` – Pour tout entier$r \geq 1$, on a :

(i) A toute representation automorphe cuspidale´$\pi \in { \mathcal { A } } ^ { r } ( F )$, on peut associer une unique representation galoisienne´$\sigma _ { \pi } \in \mathcal { G } _ { \ell } ^ { r } ( F )$qui est non ramifiee en toute place´$x \in | X |$où π est non ramifiee et a pour valeurs´ propres de Frobenius les valeurs propres de Hecke$z _ { 1 } ( \pi _ { x } ) , \ldots , z _ { r } ( \pi _ { x } )$ de π.

(ii) Reciproquement, à toute repr´ esentation galoisienne´$\sigma \in { \mathcal { G } } _ { \ell } ^ { r } ( F )$, on peut associer une unique representation automorphe´$\pi _ { \sigma } ~ \in ~ \mathcal { A } ^ { r } ( F )$ dont les valeurspropres de Hecke sont les valeurspropres de Frobenius de σ.

L’unicite dans les assertions (i) de ce th´ eorème r´ esulte du th´ eorème de´ densite de Chebotarev et l’unicit´ e dans les assertions (ii) du “th´ eorème de´ multiplicite un fort” de Piatetski-Shapiro.´

Les assertions (i) et (ii) en rang$r = 1$equivalent à la loi de r´ eciprocit´ e´ dans la theorie du corps de classes sur´ F.

Raisonnant par recurrence, on fixe un entier´$r \geq 2$et on suppose les assertions (i) dejà connues en rangs´ < r. En combinant les equations fonc-´ tionnelles de fonctions L de Grothendieck, la formule du produit de Laumon et les “theorèmes r´ eciproques” de Hecke, Weil et Piatetski-Shapiro, on en´ deduit (c’est le “principe de r´ ecurrence” de Deligne) que les assertions (ii)´ sont aussi connues en rangs$\leq r$

Ainsi, on est reduit à construire l’application´$\mathcal { A } ^ { r } ( F ) \to \mathcal { G } _ { \ell } ^ { r } ( F ) : \pi \mapsto \sigma _ { \pi }$ En fait, notant$q ^ { \prime }$et$q ^ { \prime \prime }$les deux projections de la surface$X \times X$sur la courbe X, on va identifier dans la cohomologie -adique au-dessus du point gen´ erique de´$X \times X$des variet´ es de chtoucas de rang´ r (munies de l’action de${ \mathcal { H } } ^ { r }$par correspondances de Hecke) un morceau de la forme

$$
\bigoplus_ {\pi \in \mathcal {A} ^ {r} (F)} \pi \otimes q ^ {\prime *} \sigma_ {\pi} \otimes q ^ {\prime \prime *} \check {\sigma} _ {\pi} (1 - r).
$$

Rappelons en effet que pour tout niveau N c’est-à-dire tout sous-schema´ ferme fini´$N = \mathsf { S p e c } \mathcal { O } _ { N } ^ { \phantom { \dagger } }$de X, on dispose du champ (algebrique au sens de´ Deligne-Mumford)$\mathrm { C h t } _ { N } ^ { r }$classifiant les chtoucas de Drinfeld de rang r avec structures de niveau N ; il est muni naturellement$\mathrm { d } ^ { \prime }$un morphisme lisse de dimension$2 r - 2$sur$( X - N ) \times ( X - N )$, de deux endomorphismes dits “de Frobenius partiels” Frob et Frob dont le compose est Frob et´ d’une action par correspondances de la sous-algèbre$\mathcal { H } _ { N } ^ { r }$de${ \mathcal { H } } ^ { r }$constituee´ des fonctions bi-invariantes par$K _ { N } = \mathrm { K e r } [ K = \mathrm { G L } _ { r } ( \ddot { O } _ { \mathbb { A } } ) \to \mathrm { G L } _ { r } ( \mathcal { O } _ { N } ) ]$ Dans$\mathrm { C h t } _ { N } ^ { r } , \mathrm { i l ~ y }$a une infinite de composantes connexes ; afin de´$\mathrm { n ^ { \prime } }$en plus avoir qu’un nombre fini, on peut considerer le classifiant´$\mathbf { C h t } _ { N } ^ { r , d } \subset \mathbf { C h t } _ { N } ^ { r }$des chtoucas de degre´ d fixe ou bien le quotient´$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb { Z } } \cong \coprod _ { 1 \leq d \leq r } \mathrm { C h t } _ { N } ^ { r , d }$par un idèle$a \in \mathbb { A } ^ { \times }$de degre 1. Un tel quotient reste muni d’une action de´$\mathrm { F r o b } _ { \infty }$ et Frob et de$\mathcal { H } _ { N } ^ { r }$

La principale difficulte dans l’´ etude des chtoucas r´ eside en ceci que les´ composantes connexes de$\mathrm { C h t } _ { N } ^ { r }$ne sont pas de type fini. Leur cohomologie -adique est de dimension infinie et si on cherche à compter leurs nombres de points fixes par les correspondances de Hecke, on trouve$\mathrm { \ q u ^ { \prime } i l }$y en a une infinite. De plus, il n’existe pas dans´$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb Z }$d’ouvert de type fini qui soit stable par l’action de Frob , Frob ou$\dot { \mathcal { H } } _ { N } ^ { r }$

Dans le livre [Lafforgue, 1997], on a neanmoins d´ efini des ouverts de´ type fini$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } \cong \amalg \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p }$dans$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb Z }$en bornant par un 1≤d≤r

polygone de troncature$p : [ 0 , r ] \to \mathbb { R } _ { + }$le polygone canonique de Harder-Narasimhan$\overline { { p } }$des chtoucas. En combinant la formule des traces d’Arthur-Selberg et la description adelique des chtoucas par Drinfeld, on a calcul´ e´ les nombres de points fixes par les composes de puissances de Frob et de´ correspondances de Hecke$f \in \mathcal { H } _ { N } ^ { r }$qui sont dans la fibre de$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$ au-dessus d’un point x de$X \times X$qui s’envoie sur deux places distinctes ∞, $0 \in | X - N |$. En simplifiant, on a pour ces nombres de points fixes des expression de la forme

$$
\operatorname{Lef}_{x}\left(\operatorname{Frob}^{s}\times f,\operatorname{Cht}_{N}^{r,\overline{p}\leq p} / a^{\mathbb{Z}}\right)\\ = q^{(r - 1)s}\sum_{\substack{\pi \in \mathcal{A}^{r}(F)\\ \chi \pi (a) = 1}}\operatorname{Tr}_{\pi}(f)\big(z_{1}(\pi_{\infty})^{-s / \deg (\infty)} + \dots +z_{r}(\pi_{\infty})^{-s / \deg (\infty)}\big)\\ \big(z_{1}(\pi_{0})^{s / \deg (0)} + \dots +z_{r}(\pi_{0})^{s / \deg (0)}\big)
$$

$+ \mathrm { d } ^ { , }$autres termes où apparaissent les valeurs propres de Hecke des represen-´ tations automorphes cuspidales des sous-groupes de Levi stricts de´$\mathrm { G L } _ { r }$

Il faut remarquer tout de suite que, si Frob designe l’´ el´ ement de Frobe-´ nius en le point ferme´ x de la surface$X \times X$, le terme principal dans la formule de comptage ci-dessus a la forme qu’on attend pour une trace de Frob${ \phantom { - } } _ { x } ^ { - s / \deg ( x ) } \times f$sur la representation´$\bigoplus \ \pi \otimes q ^ { \prime * } \sigma _ { \pi } \otimes q ^ { \prime \prime * } { \check { \sigma } } _ { \pi } ( 1 - r ) \operatorname { q u " i l }$ π∈A<sup>r</sup>(F) s’agit de construire.χ<sub>π</sub> (a)=1

Quand f est l’unite´ 11$N$de l’algèbre$\mathcal { H } _ { N } ^ { r }$, la correspondance de Hecke associee est l’identit´ e de´$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$et d’après la formule des points fixes de Grothendieck-Lefschetz, Lef (Frob<sup>s</sup>, Ch$\stackrel { r , \overline { { p } } \leq p } { N } / a ^ { \mathbb { Z } } )$s’interprète comme la trace de Frob${ \underset { x } { - s / \deg ( x ) } }$sur la cohomologie -adique à supports compacts $H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$de$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$au-dessus du point gen´ erique de´$X \times X$ Mais en gen´ eral´ f ne stabilise pas l’ouvert tronque´$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$et le nombre $\mathrm { L e f } _ { x } ( \mathrm { F r o b } ^ { s } , \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z } )$est a priori depourvu de sens cohomologique.´

Afin de retrouver l’action des correspondances de Hecke qu’on a perdue en tronquant, on considère les compactifications$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$des ouverts $\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$. Pour$N = \emptyset$, elles ont et´ e construites dans l’article [Lafforgue,´ 1998]. Ce sont des champs algebriques au sens d’Artin dont les groupes´ d’automorphismes sont finis (mais ont une partie ramifiee), ils sont propres´ et lisses au-dessus de$X \times X$et leurs bords sont des diviseurs à croisements normaux relatifs. Les strates de bord sont munies non seulement de ces deux morphismes sur X “pôle” et “zero” mais aussi de morphismes sur´ X supplementaires appel´ es “d´ eg´ en´ erateurs”. Chaque´ el´ ement´$f \in \mathcal { H } _ { \varnothing } ^ { r }$definit´ une correspondance dans$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$par simple normalisation de la trace dans l’ouvert$\mathrm { C h t } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$de la correspondance de Hecke associee à´ f dans $\mathrm { C h t } ^ { r } / a ^ { \mathbb { Z } }$; une telle correspondance induit un endomorphisme de la cohomologie$H _ { c } ^ { * } ( \overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb Z } )$auquel on peut esperer appliquer une formule des´ points fixes de Grothendieck.

Pour$N \neq \emptyset$, on definit les champs´$\overline { { { \mathrm { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$comme les normalises´ des$\mathrm { C h t } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } \times _ { X \times X } ( X - N ) \times ( X - N )$dans les$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z }$. Ils sont propres sur$( X - N ) \times ( X - N )$mais ils ne sont pas lisses et a priori les correspondances de Hecke$f \in \mathcal { H } _ { N } ^ { r }$etendues par normalisation n’induisent´ pas d’endomorphismes en cohomologie. Si toutefois$\overline { { { \mathrm { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$admet une resolution des singularit´ es´$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z }$propre et lisse sur$( X - N ) \times ( X - N )$ et dont le bord$\mathrm { { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } - { \mathrm { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$est un diviseur à croisements normaux relatif, les correspondances normalisees induisent des endomor-´ phismes de$H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$

On considère d’autre part l’ouvert$\overline { { { \mathrm { C h t } _ { N } ^ { r , \overline { { { p } } } \leq p } } } } / a ^ { \mathbb { Z } } \mathrm { d e } \overline { { { \mathrm { C h t } _ { N } ^ { r , \overline { { { p } } } \leq p } } } } / a ^ { \mathbb { Z } }$defini en´ demandant que non seulement le pôle et le zero mais aussi les “d´ eg´ en´ era-´ teurs” evitent´ N. Il est lisse sur$( X - N ) \times ( X - N )$et son bord$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } } } } / a ^ { \mathbb Z } -$ $\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$est un diviseur à croisements normaux relatif. On montre que, de façon remarquable, les correspondances de Hecke normalisees sta-´ bilisent$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } } } } / a ^ { \mathbb Z }$et donc elles induisent des endomorphismes de sa cohomologie.

Il faut noter que tous ces endomorphismes induits dans les $H _ { c } ^ { * } ( \overline { { \mathbf { C } \mathbf { h } \mathbf { t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } } )$et les$H _ { c } ^ { * } ( \overline { { \mathbf { C } \mathbf { h } \mathbf { t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } } } } / a ^ { \mathbb { Z } } )$(ou eventuellement les´ $H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } ) )$ne definissent pas d’action des´$\mathcal { H } _ { \varnothing } ^ { r }$et$\mathcal { H } _ { N } ^ { r }$car la formation des correspondances de Hecke normalisees ne commute pas avec la´ multiplication.

En resum´ e, on dispose de trois objets g´ eom´ etriques distincts sur lesquels´ on dispose de trois informations differentes qui suffiraient à conclure si on´ pouvait les rapporter à un unique objet : sur$\mathrm { \dot { C } h t } _ { N } ^ { r } / a ^ { \mathbb { Z } }$, on a une action par correspondances de l’algèbre de Hecke$\mathcal { H } _ { N } ^ { r }$(et aussi de$\mathrm { F r o b } _ { \infty }$et$\operatorname { F r o b } _ { 0 } )$ sur les$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$, on a des formules de comptage des points fixes ; enfin, sur les ouverts$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { ' } } / a ^ { \mathbb Z }$des$\overline { { { \bf { C } } \mathrm { { h t } } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$(ou eventuellement sur´ les$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z } )$, on a la formule des traces de Grothendieck-Lefschetz-Verdier. Le principe de la demonstration va consister à s´ eparer dans les´ trois representations galoisiennes´$H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r } / a ^ { \mathbb { Z } } )$$H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$et $H _ { c } ^ { * } ( { \bf C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { ' } } / a ^ { \mathbb { Z } } )$(ou eventuellement´$H _ { c } ^ { * } ( { \bf C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } ) )$un morceau “essentiel” de tout le reste$\mathrm { \ q u } ^ { \prime }$on qualifiera de “negligeable”. Cette cohomologie´ essentielle sera la même pour les trois objets et il s’agira d’extraire dans les trois informations de depart ce qui la concerne et qui va permettre de la´ calculer.

La definition de ce qui est n´ egligeable et de ce qui est essentiel est´ dictee par la formule de comptage rappel´ ee plus haut. En effet, les termes´ complementaires dans cette formule, ceux´$\mathrm { \ q u } ^ { \prime }$on voudrait supprimer, ne font apparaître que les valeurs propres de Hecke de representations automorphes´ cuspidales de sous-groupes de Levi stricts de´$\mathrm { G L } _ { r }$lesquelles s’interprètent d’après l’hypothèse de recurrence comme valeurs propres de Frobenius de´ representations galoisiennes irr´ eductibles de dimension´$< r$. Au contraire, on${ \bf s } '$attend à ce que les valeurs propres de Hecke qui apparaissent dans le terme principal s’interprètent comme valeurs propres de Frobenius de representations galoisiennes toutes irr´ eductibles de dimension´ r. Ainsi eston amene à poser :´

Definition.´ – Unfaisceau -adique lisse irreductible sur un ouvert de´$X \times X$ sera dit r-negligeable s’il estfacteur direct d’un faisceau de laforme´

$$
q ^ {\prime *} \sigma^ {\prime} \otimes q ^ {\prime \prime *} \sigma^ {\prime \prime},
$$

avec$\sigma ^ { \prime }$et$\sigma ^ { \prime \prime }$deux faisceaux -adiques lisses et irreductibles de rangs´$\cdot < r$ sur des ouverts de la courbe X.

Il sera dit essentiel sinon.

Les representations virtuelles´$H _ { c } ^ { * } ( \mathbf { C } \mathrm { h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$nous sont connues par les traces des puissances$\mathrm { F r o b } _ { x } ^ { - s / \mathrm { d e g } ( x ) }$des el´ ements de Frobenius´$\operatorname { F r o b } _ { x }$en les points fermes´ x de$( X - { \overset { \cdot } { N } } ) \times ( X - N )$. L’hypothèse de recurrence´ jointe à ce qu’on sait de la localisation des pôles et zeros des fonctions´ L de paires (tant automorphes que galoisiennes) permet de separer dans´ $H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$la partie essentielle$H _ { c } ^ { * } ( \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z } ) _ { \mathrm { e s s } }$de la partie ne-´ gligeable et en les points x dont les deux projections ∞ et 0 sur X sont distinctes, on obtient la formule des traces suivante

$$
\begin{array}{c}\operatorname{Tr}\left(\operatorname{Frob}_{x}^{-s / \deg (x)},H_{c}^{*}\bigl (\operatorname{Cht}_{N}^{r,\overline{p}\leq p} / a^{\mathbb{Z}}\bigr)_{\text{ess}}\right) = \\ q^{(r - 1)s}\sum_{\substack{\pi \in \mathcal{A}^{r}(F)\\ \chi_{\pi}(a) = 1}}\operatorname{Tr}_{\pi}(\mathbb{1}_{N})\bigl (z_{1}(\pi_{\infty})^{-s / \deg (\infty)} + \dots +z_{r}(\pi_{\infty})^{-s / \deg (\infty)}\bigr)\\ \bigl (z_{1}(\pi_{0})^{s / \deg (0)} + \dots +z_{r}(\pi_{0})^{s / \deg (0)}\bigr). \end{array}
$$

On remarque que cette formule ne depend pas du polygone de troncature´ p et ceci permettra d’identifier les$H _ { c } ^ { * } ( \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z } ) _ { \mathrm { e s s } }$entre eux et avec la partie essentielle de$H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r } / a ^ { \mathbb { Z } } ) = \varinjlim _ { p } H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$

Mais il faut d’abord montrer que$H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$et$H _ { c } ^ { * } ( \overline { { \mathbf { C } \mathbf { h } \mathbf { t } _ { N } ^ { r , \overline { { p } } \leq p } } } ^ { \prime } / a ^ { \mathbb { Z } } )$ ou eventuellement´$H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$ont même partie essentielle et pour cela que la cohomologie des strates de bord de$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } } } } / a ^ { \mathbb Z } \mathrm { o u } \mathrm { C h t } _ { N } ^ { \overline { { p } } \leq p } / a ^ { \mathbb Z }$ est r-negligeable.´

Quand le niveau N est vide, les strates de bord des$\overline { { \mathrm { C h t } ^ { r , d , \overline { { { p } } } \leq p } } }$sont indexees par les partitions non triviales´$r = r _ { 1 } + \cdots + r _ { k }$de l’entier r et elles sont essentiellement de la forme$\mathrm { C h t } ^ { r _ { 1 } , d _ { 1 } , \overline { { p } } \leq p _ { 1 } } \times _ { X } \cdot \cdot \cdot \times _ { X } \mathbf { C h t } ^ { r _ { k } , d _ { k } , \overline { { p } } \leq p _ { k } }$ Il resulte de l’hypothèse de r´ ecurrence que la cohomologie sur´$X \times X$de chaque$\mathrm { C h t } ^ { r _ { i } , d _ { i } , \dot { \overline { { p } } } \hat { \le } p _ { i } }$est$( r _ { i } + 1 ) { \tt - n e g l i }$geable et a fortiori r-negligeable et´ on en deduit que la cohomologie sur´$X \times X$de la strate consider´ ee est´ r-negligeable.´

Quand le niveau N n’est pas vide, un argument du même type s’applique à tout champ X qui$\mathrm {  ~ s ~ } ^ { \prime }$ecrit comme produit fibr´ e dans un carr´ e cart´ esien´

![](images/page_5_image_6.jpg)

dont la base est le morphisme lisse$\mathbf { \nabla } \cdot \otimes _ { \mathcal { O } _ { X } } \mathcal { O } _ { N }$de “restriction des chtoucas iter´ es de´$X \grave { \mathbf { a } } N ^ { \prime \prime }$(voir le paragraphe III.2a pour une definition pr´ ecise) et où´ C est un champ representable quasi-projectif sur´$\mathcal { C } ^ { r , N }$qui prolonge le revêtement de Lang qui definit´$\mathrm { C h t } _ { N } ^ { \bar { r } , d , \overline { { p } } \leq \bar { p } }$. Ici encore, on utilise l’hypothèse de recurrence et le calcul des nombres de points fixes par les puis´ sances de Frob dans les fibres des$\mathrm { C h t } _ { N } ^ { r ^ { \prime } , \overline { { p } } \leq p } / a ^ { \mathbb Z } , r ^ { \prime } < r$, au-dessus de$( X - N ) \times ( X - N )$ Quand les “deg´ en´ erateurs” (qui sont les z´ eros et pôles des chtoucas de rangs´ $r _ { 1 } , \ldots , r _ { k } < r$que classifient les strates de bord des$\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } } } )$n’evitent´ pas N, on a besoin d’un calcul de points fixes supplementaire dans les´ champs de chtoucas de rangs$< r$avec structures de niveau N comprenant le zero ou le pôle.´

On applique ces arguments d’une part aux ouverts$\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } } }$des $\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \le p } } }$(lesquels ont la forme ci-dessus en prenant pour C un certain ouvert lisse$\mathcal { C } _ { n } ^ { \bar { \prime } r }$de la normalisation$\mathcal { C } _ { N } ^ { r }$de$\hat { \mathcal { C } } ^ { \hat { r } , N }$dans le revêtement de Lang, voir les paragraphes III.3a et III.3b) et d’autre part à la cohomologie d’intersection des normalisations$\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \le p } } }$(en utilisant le fait qu’elles sont deduites de´$\mathcal { C } _ { N } ^ { r }$par changement de base et que leur complexe d’intersection est l’image reciproque de celui de´$\mathcal { C } _ { N } ^ { r } )$. Dans tous les cas, le plus important est de ne considerer que des objets d´ efinis comme des produits´ fibres au-dessus du morphisme de restriction de´ X à N.

Si on veut construire des resolutions des singularit´ es´$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p }$des $\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$qui verifient toutes les propri´ et´ es dont nous avons besoin, on est´ ramene au problème de r´ esoudre les singularit´ es de la normalisation´$\mathcal { C } _ { N } ^ { r }$ Ce problème est etroitement li´ e à celui de construire des compactifications´ equivariantes et lisses de tous les quotients´$\mathrm { P G L } _ { r } ^ { n + 1 } / \mathrm { P G L } _ { r }$. L’auteur avait cru le resoudre dans l’article [Lafforgue, 1999] mais en pr´ eparant un cours´ à l’Institut Henri Poincare il´$\mathrm {  ~ s ~ } ^ { \prime }$est aperçu dans les premiers jours de juin 2000 que le principal enonc´ e de lissit´ e de cet article (le th´ eorème 6 du´ paragraphe 1c) est faux quand$n \geq 3$(l’erreur est dans le lemme 3 du paragraphe 3b). Le cas$n = 1$(celui des homomorphismes complets, cas particulier des compactifications “mirifiques” de De Concini et Procesi) et le cas$n = 2$sont vrais et cela suffit pour resoudre les singularit´ es de´ $\mathcal { C } _ { N } ^ { r }$quand N n’a pas de multiplicites mais´${ \mathrm { c } } ^ { \prime }$est insuffisant sinon. C’est la necessit´ e de corriger les cons´ equences de cette faute qui a amen´ e l’auteur´ à s’apercevoir fin juin 2000 de la propriet´ e de stabilit´ e des ouverts lisses´ $\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p ^ { \prime } } } } / a ^ { \mathbb Z }$par les correspondances de Hecke.

Une fois qu’on a montre que la partie essentielle des´$H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$ des$H _ { c } ^ { * } ( \overline { { \mathbf { C } \mathbf { h } \mathbf { t } _ { N } ^ { r , \overline { { p } } \leq p ^ { ' } } } } / a ^ { \mathbb { Z } } )$ou$H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$et de$H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r } / a ^ { \mathbb { Z } } )$est la même (et qu’elle est concentree en degr´ e´$2 r - 2 )$ce qui utilise aussi la purete de la´ cohomologie d’intersection de$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$ou de$H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$, on peut commencer à faire entrer en jeu l’action de$\mathcal { H } _ { N } ^ { r }$et de$\mathrm { F r o b } _ { \infty }$et Frob . Sur $H _ { c } ^ { 2 r - 2 } ( { \mathrm { C h t } } _ { N } ^ { r } / a ^ { \mathbb { Z } } ) = \varinjlim _ { p } H _ { c } ^ { 2 r - 2 } ( { \mathrm { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$, on construit une filtration finie stable par ces actions et dont chaque sous-quotient est ou bien r-negligeable´ ou bien essentiel. Ainsi la partie essentielle$H _ { N , \mathrm { { e s s } } }$de$H _ { c } ^ { 2 r - 2 } ( \mathbf { C h t } _ { N } ^ { r } / \bar { a } ^ { \mathbb { Z } } )$se retrouve-t-elle munie d’une action de$\mathcal { H } _ { N } ^ { r }$et de$\mathrm { F r o b } _ { \infty }$et Frob . Afin de determiner l’action de´$\mathcal { H } _ { N } ^ { r }$sur la representation galoisienne´$H _ { N , { \mathrm { e s s } } } .$, il suffit de calculer la trace des composes de toute correspondance de Hecke fix´ ee´ $f \in \mathcal { H } _ { N } ^ { r }$avec les puissances$\mathbf { \tilde { F } r o b } _ { r } ^ { - s / \deg ( x ) }$des el´ ements de Frobenius en les´ points fermes´ x de$( X - N ) \times ( \dot { X ^ { } } - N )$

L’action de f sur$H _ { N , \mathrm { { e s s } } }$est identique à celle de la correspondance induite par$f$sur la cohomologie essentielle des ouverts$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } } } } / a ^ { \mathbb Z }$ou des compactifies´$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$quand ils existent. On doit relier les traces de celle-ci aux nombres de points fixes dans les ouverts$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$

Notons$S \ = \ ( X - N ) \times ( X - N ) , \mathfrak { X } \ = \ \mathbf { C } \mathbf { h } t ^ { r , \overline { { p } } \le p } / a ^ { \mathbb { Z } } \ ( \mathrm { s i } \ N \ = \ \varnothing )$ $\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb Z }$ou$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z } \ \mathrm { e t } \ \overline { { \mathfrak { X } } } _ { 1 } , \dots , \overline { { \mathfrak { X } } } _ { m }$les strates fermees du bord de´ X qui sont de codimension 1. Les autres strates fermees de bord sont les´ $\overline { { \mathfrak { X } } } _ { I } = \bigcap _ { i \in I } \overline { { \mathfrak { X } } } _ { i } , I \subseteq \{ 1 , \dots , m \} , I \ne \emptyset$. Comme dans l’article [Pink], on introduit l’eclat´ e´$\widetilde { Z }$de$Z = { \mathfrak { X } } \times _ { S } { \mathfrak { X } }$le long des$\overline { { \mathfrak { X } } } _ { 1 } \times _ { S } \overline { { \mathfrak { X } } } _ { 1 } , \ldots , \overline { { \mathfrak { X } } } _ { m } \times _ { S } \overline { { \mathfrak { X } } } _ { m }$ il est muni de diviseurs exceptionnels$E _ { 1 } , \ldots , E _ { m }$qui sont à croisements normaux et pour$I \subseteq \{ 1 , \dots , m \} , I \neq \emptyset$, on peut considerer´$E _ { I } = \bigcap _ { i \in I } E _ { i }$

Expliquons le cas où X est propre sur S.

La correspondance f dans X est un cycle dans Z dont on note$\widetilde { f }$le transforme strict dans´$\widetilde { Z }$; soient cl$( f )$et cl$\widetilde { ( f ) }$leurs classes de cohomologie. Pour toute$I \subseteq \{ 1 , \dots , m \}$, on note cl$( \widetilde f ) _ { I }$l’image directe dans$\overline { { \mathfrak { X } } } _ { I } \times _ { S } \overline { { \mathfrak { X } } } _ { I }$ de l’image reciproque dans´$E _ { I }$de$\operatorname { c l } ( \widetilde { f } ) : \operatorname { c } ^ { \prime }$est une correspondance cohomologique dans$\overline { { \mathfrak { X } } } _ { I }$

Soient encore cl$( \delta _ { x } ^ { s } )$et cl$( \delta _ { x , I } ^ { s } )$les classes de cohomologie des graphes de Frob<sup>s</sup> dans les fibres de X et des$\overline { { \mathfrak { X } } } _ { I }$au-dessus des points fermes´ x de $S = ( X - N ) \times ( X - N )$. Soit cl$( \widetilde { \delta } _ { x } ^ { s } )$la classe du transforme strict du graphe´ $\delta _ { x } ^ { s }$de Frob<sup>s</sup> dans$\widetilde { Z } \times _ { S } \boldsymbol { x }$

Un calcul d’adjonction donne pour les nombres d’intersection la formule suivante

$$
\operatorname{cl} \left(\widetilde {\delta} _ {x} ^ {s}\right) \cdot x ^ {*} (\operatorname{cl} (\widetilde {f})) = \operatorname{cl} \left(\delta_ {x} ^ {s}\right) \cdot x ^ {*} (\operatorname{cl} (f)) + \sum_ {I \neq \emptyset} (- 1) ^ {| I |} \operatorname{cl} \left(\delta_ {x, I} ^ {s}\right) \cdot x ^ {*} (\operatorname{cl} (\widetilde {f}) _ {I}).
$$

Notons$\mathfrak { X } _ { \varnothing } \ = \ \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \le p } / a ^ { \mathbb { Z } }$l’ouvert de X complementaire du bord´ $\overline { { \mathfrak { X } } } _ { 1 } \cup \ldots \cup \overline { { \mathfrak { X } } } _ { m }$. Pink a montre que pour une correspondance´ f gen´ erale´ qui stabilise l’ouvert$\mathfrak { X } _ { \varnothing }$(et quitte à remplacer$\hat { \boldsymbol f }$par sa transformee´ par une puissance assez grande de$\mathrm { I d } \times \mathrm { F r o b } )$, les nombres d’intersection c$( \widetilde { \delta } _ { x } ^ { s } ) \cdot x ^ { * } ( \mathrm { c l } ( \widetilde { f } ) )$des transformes stricts dans´$\widetilde { Z }$sont concentres dans´ l’ouvert${ \mathfrak { X } } _ { \varnothing } \times _ { S } { \mathfrak { X } } _ { \varnothing }$

Dans notre situation, la correspondance de Hecke$f$ne stabilise pas$\mathfrak { X } _ { \varnothing }$ Mais on remarque que l’argument geom´ etrique de Pink reste valable si l’on´ suppose seulement que f “stabilise$\mathfrak { X } _ { \varnothing }$au voisinage de ses points fixes”

au sens qu’il existe un ouvert U de${ \mathfrak { X } } \times _ { S } { \mathfrak { X } } = Z$, contenant toutes les intersections de f avec les graphes des puissances de Frob et tel que, si$p _ { f } ^ { \prime }$ et$p _ { f } ^ { \prime \prime }$designent les deux projections sur´ X de la correspondance$f ,$, on ait

$$
U \cap p _ {f} ^ {\prime - 1} (\mathfrak {X} _ {\emptyset}) \subseteq U \cap p _ {f} ^ {\prime \prime - 1} (\mathfrak {X} _ {\emptyset}).
$$

Or on demontre que les correspondances de Hecke´$f$dans$\mathfrak { X } = \overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \le p } } } / a ^ { \mathbb { Z } }$ verifient cette propri´ et´ e de stabilisation locale de´$\mathfrak { X } _ { \varnothing }$. L’argument pour cela est une gen´ eralisation en rang´ r arbitraire de la proposition 7.2 de l’article [Drinfeld, 1989]. Il est fonde sur l’existence des “d´ eg´ en´ erateurs” dans les´ strates de bord de$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb Z }$

En resum´ e, on a montr´ e que pour´$f \in \mathcal { H } _ { N } ^ { r }$fixee, il existe des correspon-´ dances cohomologiques$u _ { I }$dans les strates de bord${ \overline { { \mathfrak { X } } } } _ { I } , I \subseteq \{ 1 , \dots , m \}$ $I \neq \emptyset$, telles que pour tout point ferme´ x de$( X - N ) \times ( X - N )$et tout multiple s assez grand de deg(x), on ait

$$
\begin{array}{l} \operatorname{Tr} _ {H _ {c} ^ {*} (\mathfrak {X})} \left(f \times \operatorname{Frob} _ {x} ^ {- s / \deg (x)}\right) + \sum_ {I \neq \emptyset} (- 1) ^ {| I |} \operatorname{Tr} _ {H _ {c} ^ {*} (\overline {{\mathfrak {X}}} _ {I})} \left(u _ {I} \times \operatorname{Frob} _ {x} ^ {- s / \deg (x)}\right) \\ = \operatorname{Lef} _ {x} \left(\operatorname{Frob} ^ {s} \times f, \operatorname{Cht} _ {N} ^ {r, \overline {{p}} \leq p} / a ^ {\mathbb {Z}}\right). \end{array}
$$

On a le même resultat quand´ X n’est pas propre sur S. En plus des arguments prec´ edents, il faut raisonner cette fois en termes de correspond´ ances cohomologiques au sens de Grothendieck-Verdier sur l’espace de modules grossier de$\hat { \mathfrak X }$et appliquer la formule gen´ erale des traces de Grothendieck-´ Lefschetz-Verdier et le theorème de Fujiwara sur la conjecture de Deligne´ pour faire disparaître les termes à l’infini. La demonstration de Fujiwara´ utilise la cohomologie analytique rigide qui est developp´ ee seulement pour´ les schemas et non pour les espaces alg´ ebriques. Pour cette raison, on est´ aussi amene à montrer que les espaces alg´ ebriques grossiers associ´ es aux´ $\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z }$deviennent des schemas au moins après extension finie du corps´ de base$\mathbb { F } _ { q }$

Quand les deux projections ∞ et 0 de x sur X sont distinctes, on a calcule le nombre de Lefschetz´$\mathrm { L e f } _ { x } ( \mathrm { F r o b } ^ { s } \times f , \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$en termes automorphes. En utilisant encore une fois l’hypothèse de recurrence et des´ arguments de fonctions L de paires, on separe dans la formule ci-dessus la´ partie essentielle de la partie negligeable et on obtient´

$$
\begin{array}{c}\operatorname{Tr}\left(f\times \operatorname{Frob}_{x}^{-s / \deg (x)},H_{N,\text{ess}}\right) = q^{(r - 1)s}\sum_{\substack{\pi \in \mathcal{A}^{r}(F)\\ \chi_{\pi}(a) = 1}}\operatorname{Tr}_{\pi}(f)\\ \big(z_{1}(\pi_{\infty})^{-s / \deg (\infty)} + \dots +z_{r}(\pi_{\infty})^{-s / \deg (\infty)}\big)\\ \big(z_{1}(\pi_{0})^{s / \deg (0)} + \dots +z_{r}(\pi_{0})^{s / \deg (0)}\big). \end{array}
$$

Cela suffit pour conclure.

Pour la commodite du lecteur, on peut pr´ eciser quelles sont les res-´ semblances et les differences entre la pr´ esente d´ emonstration et celle de´ Drinfeld en rang$r = 2$

Dans les espaces$\mathrm { C h t } ^ { 2 } / a ^ { \mathbb Z }$ou$\mathrm { C h t } _ { N } ^ { 2 } / a ^ { \mathbb Z }$de chtoucas de rang 2, Drinfeld a d’abord defini des ouverts de type fini´$\mathrm { C h t } ^ { 2 , m } / a ^ { \mathbb { Z } }$ou$\mathrm { C h t } _ { N } ^ { 2 , m } / a ^ { \mathbb { Z } }$indexes´ par les entiers$m \in \mathbb { N }$et que nos ouverts tronques´$\mathrm { C h t } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$gen´ eralisent´ (les entiers m sont les valeurs des polygones convexes$p : [ 0 , 2 ]  \mathbb { R } _ { + }$en $s = 1 )$. Puis il a construit des compactifications${ \overline { { \mathrm { C h t } ^ { 2 , m } } } } / a ^ { \mathbb { Z } }$des$\mathrm { C h t } ^ { 2 , m } / a ^ { \mathbb { Z } }$ que nos compactifications sans niveau$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$gen´ eralisent encore : leur´ bord comprend une unique strate qui correspond à la partition$2 = 1 + 1$

Dans le cas avec niveau, les normalisations$\overline { { \mathrm { C h t } _ { N } ^ { 2 , m } } } / a ^ { \mathbb Z }$des$\overline { { \mathrm { C h t } ^ { 2 , m } } } / a ^ { \mathbb { Z } }$ dans les$\mathrm { C h t } _ { N } ^ { 2 , m } / a ^ { \mathbb { Z } }$ne sont pas lisses mais Drinfeld a montre qu’elles sont´ “cohomologiquement lisses” au sens que le faisceau constant$\mathbb { Q } _ { \ell } { \mathrm { ~ y ~ } }$est auto-dual (l’auteur ignore ce qu’il en est en rang$r \geq 3 )$si bien que leur cohomologie -adique$H _ { c } ^ { * } ( \mathbf { C } \mathbf { h } \mathrm { t } _ { N } ^ { 2 , m } / a ^ { \mathbb { Z } } )$verifie la dualit´ e de Poincar´ e.´

Drinfeld a prouve encore que les immersions ouvertes´$\mathrm { C h t } _ { N } ^ { 2 , m } / a ^ { \mathbb { Z } } \hookrightarrow$ $\mathrm { C h t } _ { N } ^ { 2 , m + 1 } / a ^ { \mathbb Z }$induisent des morphismes birationnels partout bien definis´ dans l’autre sens$\overline { { { \mathrm { C h t } _ { N } ^ { 2 , m + 1 } } } } / a ^ { \mathbb { Z } } \to \overline { { { \mathrm { C h t } _ { N } ^ { 2 , m } } } } / a ^ { \mathbb { Z } }$(ce qui n’est plus vrai dès le rang$r = 3 )$et à partir de là toute son etude se concentre sur la tour des´ $\mathrm { C h t } _ { N } ^ { 2 , m } / a ^ { \mathbb Z }$et la limite inductive de dimension infinie$H _ { c } ^ { * } ( \overline { { \mathrm { C h t } _ { N } ^ { 2 , * } } } / a ^ { \mathbb { Z } } ) = \underline { { \mathrm { l i m } } }$ m $H _ { c } ^ { * } ( \overline { { \mathrm { C h t } _ { N } ^ { 2 , m } } } / a ^ { \mathbb Z } )$munie du produit scalaire fourni par la dualite de Poincar´ e.´ Les correspondances de Hecke$f \in \mathcal { H } _ { N } ^ { 2 }$et les endomorphismes de Frobenius partiels Frob$\mathrm { \infty , F r o b _ { 0 } }$etendus par normalisation induisent des endomor-´ phismes de chaque$H _ { c } ^ { * } ( \overline { { \mathrm { C h t } _ { N } ^ { 2 , m } } } / a ^ { \mathbb Z } )$et Drinfeld prouve qu’ils definissent de´ nouveau une veritable action de´$\mathcal { H } _ { N } ^ { 2 } \times \mathbb { Z }$sur la limite inductive$H _ { c } ^ { * } ( \overline { { \mathbf { C h t } _ { N } ^ { 2 , * } } } / a ^ { \mathbb { Z } } )$ (dans chaque$H _ { c } ^ { * } ( \mathbf { C } \mathbf { h } \mathrm { t } _ { N } ^ { 2 , m } / a ^ { \mathbb { Z } } )$l’endomorphisme induit par une correspondance$f \in \mathcal { H } _ { N } ^ { 2 }$est le compose de celui dans´$H _ { c } ^ { * } ( \overline { { \mathbf { C } \mathbf { h } \mathbf { t } _ { N } ^ { 2 , * } } } / a ^ { \mathbb { Z } } )$et de la projection orthogonale sur le sous-espace de dimension finie$H _ { c } ^ { * } ( \mathbf { C } \mathbf { h } \mathrm { t } _ { N } ^ { 2 , m } / a ^ { \mathbb { Z } } )$ce qui explique pourquoi, dès le rang$r = 2 , \mathcal { H } _ { N } ^ { 2 }$n’agit pas sur$H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { 2 , m } / a ^ { \mathbb { Z } } ) )$.

Enfin, Drinfeld calcule complètement$H _ { c } ^ { * } ( \mathbf { C } \mathbf { h t } _ { N } ^ { 2 , * } / a ^ { \mathbb { Z } } )$muni de la triple action du groupe de Galois$G _ { F ^ { 2 } }$, de$\mathcal { H } _ { N } ^ { 2 }$et de$\mathrm { F r o b } _ { \infty }$, Frob . Il commence par etudier dans les´$\overline { { \mathrm { C h t } _ { N } ^ { 2 , m } } } / a ^ { \mathbb { Z } }$une certaine famille infinie de cycles algebriques, les “horocycles”, avec leurs nombres d’intersec´ tion mutuels et l’action sur eux de$\dot { \mathcal { H } } _ { N } ^ { 2 }$et$\mathrm { F r o b } _ { \infty }$, Frob ; les classes de cohomologie de ces cycles engendrent une sous-representation de´$H _ { c } ^ { * } ( \overline { { \mathbf { C h t } _ { N } ^ { 2 , * } } } / a ^ { \mathbb { Z } } )$dont la structure est complètement explicite et qui est de codimension finie. La representation quotient est la partie la plus int´ eressante´$( \mathrm { c } ^ { \prime }$est elle qui contient la “cohomologie essentielle” en notre sens et donc realise la correspon-´ dance de Langlands en rang 2) ; Drinfeld la calcule grâce à la formule des points fixes de Grothendieck-Lefschetz dans les$H _ { c } ^ { * } ( \overline { { \mathrm { C h t } _ { N } ^ { 2 , m } } } / a ^ { \mathbb Z } )$en obtenant une formule de comptage des points fixes non seulement dans les ouverts tronques´$\mathrm { C h t } _ { N } ^ { 2 , m } / a ^ { \mathbb Z }$mais même dans leurs compactifications$\overline { { \mathrm { C h t } _ { N } ^ { 2 , m } } } / a ^ { \mathbb Z }$ Cela utilise bien sûr la formule des traces de Selberg pour$\mathrm { G L } _ { 2 }$et aussi (pour le comptage des points fixes au bord) un calcul explicite et une interpretation g´ eom´ etrique de tous ses termes spectraux non cuspidaux (que´ l’auteur ne saurait gen´ eraliser en rang´$r \geq 3$que dans le cas sans niveau c’est-à-dire sans operateurs d’entrelacement locaux).´

Donnons quelques indications sur le plan du present travail.´

La partie finale de la demonstration, celle où tous les acteurs entrent en´ scène, est donnee dans le chapitre VI, particulièrement aux paragraphes 2´ et 3. Les cinq chapitres prec´ edents et les deux appendices sont de nature´ preparatoire et rassemblent les diff´ erents types d’informations dont on a´ besoin.

Le chapitre I rappelle les formules de comptage des points fixes dans les ouverts tronques des champs de chtoucas et les met sous la forme qui´ servira. Le chapitre II complète ce calcul quand le niveau comprend le zero (ou le pôle) : on en aura besoin pour montrer que les strate´ s de bord sont negligeables. Le chapitre III rappelle la forme des compacti´ fications sans niveau et les munit de structures de niveau. Il montre que les ouverts $\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } } } }$sont lisses. L’appendice A donne les propriet´ es de base de la´ cohomologie -adique du type de champs (algebriques au sens d’Artin´ avec groupes d’automorphismes finis) auquel appartiennent les champs de chtoucas et leurs compactifications. Le chapitre IV etablit une formule´ gen´ erale des points fixes d’une correspondance dans un ouvert qu´ ’elle ne stabilise pas globalement mais “localement au voisinage de ses points fixes”, d’abord dans le cas propre puis dans le cas non propre. Le chapitre V montre que les correspondances de Hecke verifient cette hypothèse de stabilit´ e´ locale et qu’elles stabilisent globalement les ouverts$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb Z }$. Il montre aussi que les espaces algebriques grossiers des´$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p }$deviennent sur$\overline { { \mathbb { F } } } _ { q }$ des schemas. L’appendice B rappelle les propri´ et´ es dont on a besoin des´ fonctions L de paires automorphes ainsi que le “theorème r´ eciproque” de´ Piatetski-Shapiro.

Enfin, le chapitre VII est consacre à des applications : compatiblit´ e entre´ correspondances de Langlands locales et globale, consequences pour les´ faisceaux -adiques, plus quelques mots sur la correspondance de Langlands geom´ etrique.´

En terminant ce travail, je tiens à exprimer encore une fois ma profonde reconnaissance envers Gerard Laumon qui m’a initi´ e aux chtoucas´ de Drinfeld et à la formule des traces d’Arthur-Selberg. Il n’a jamais cesse´ de m’encourager dans la voie de la correspondance de Langlands et je peux dire qu’au fil des ans il m’a consacre des centaines d’heures, soit pour me´ communiquer un peu de ses connaissances, soit pour m’ecouter quand je´ faisais des progrès, soit pour me soutenir dans les periodes difficiles.´

Je remercie aussi les nombreux mathematiciens avec qui j’ai eu l’occa-´ sion de parler, Laurent Clozel, Alain Genestier, Guy Henniart, Luc Illusie, Serge Lysenko, Ngo Bao Chau, Michel Raynaud et Jean-Loup Waldspurger ainsi que Christophe Soule pour sa relecture attentive du manuscrit et ses´ nombreuses remarques et corrections.

J’ai et´ e particulièrement sensible aux manifestations de soutien´ et d’amitie qui m’ont´ et´ e t´ emoign´ ees dans la p´ eriode très difficile pour moi de´ juin et juillet 2000. C’est pourquoi je veux renouveler mes remerciments les plus profonds, encore et toujours à Gerard Laumon, mais aussi à Michel´ Raynaud, Alain Genestier, Ngo Bao Chau, Luc Illusie et Laurent Clozel.

Je remercie aussi beaucoup Gerd Faltings, le rapporteur automorphe anonyme, Pierre Deligne, Vladimir Drinfeld et l’ensemble des rapporteurs pour leur travail de relecture critique des differentes parties. Ils m’ont´ permis de corriger quelques (petites) erreurs qui subsistaient et, je l’espère, d’ameliorer la r´ edaction.´

Enfin, j’adresse mes plus chaleureux remerciements à${ \bf M } ^ { \mathrm { m e } }$Bonnardel qui a assure la frappe entière de la première mouture de ce texte comme´ de mes prec´ edents articles et à´${ \bf M } ^ { \mathrm { m e } }$Gourgues de l’I.H.E.S qui a realis´ e la´ frappe des nouveaux paragraphes necessit´ es par la correction de mon erreur´ avec une rapidite et un soin extraordinaires.´

## Sommaire

Chapitre I : Rappels sur les chtoucas et leur comptage ..... 17
1) Les champs de chtoucas de Drinfeld ..... 17
a) Définition. Morphisme de structure ..... 17
b) Endomorphismes de Frobenius partiels ..... 18
c) Correspondances de Hecke ..... 19
d) Troncatures ..... 20
e) Nombres de Lefschetz ..... 22
2) Comptage des points fixes et expression spectrale ..... 23
a) Variantes des traces tronquées d'Arthur ..... 23
b) Egalité en moyenne sur les $\alpha \in \mathbb{R}$ ..... 25
c) Egalité en moyenne sur les $\overline{\infty}$ ou les $\overline{0}$ ..... 25
d) Valeurs propres de Hecke ..... 27
e) La formule des traces d'Arthur-Selberg ..... 28
f) Forme des résidus ..... 29
g) Allure des nombres de Lefschetz ..... 30
Chapitre II : Compléments quand le niveau comprend le zéro ..... 33
1) Chtoucas avec structures de niveau en le zéro ..... 33
a) Restriction des chtoucas à un niveau ..... 33
b) Choix d'un modèle ..... 36
c) Structures de niveau naïves en le zéro ..... 37
d) Expression intégrale des nombres de Lefschetz ..... 39
2) Calcul des nombres de Lefschetz et expression spectrale ..... 42
a) Fonctions de Kottwitz ..... 42
b) Amplification à partir d'un sous-groupe de Lévi ..... 44
c) Transfert ..... 46
d) Forme de l'action des fonctions $f_{h_0,m_0}^s$ ..... 47
e) Allure des nombres de Lefschetz ..... 58
Chapitre III : Compactifications des champs de chtoucas ..... 59
1) Les compactifications sans niveau ..... 60
a) Le schéma des homomorphismes complets ..... 60
b) Le champ des chtoucas itérés ..... 61
c) Description des strates de bord ..... 63
2) Le morphisme de restriction associé à un niveau ..... 66
a) Définition et propriétés ..... 66
b) Vérification de ce que le morphisme de restriction est lisse ..... 67
3) Compactifications avec niveau ..... 72
a) Structures de niveau définies par normalisation ..... 72
b) Un ouvert naturel de lissité ..... 75
c) Résolution des singularités pour les niveaux sans multiplicités ..... 80

Chapitre IV : Formule des points fixes dans un ouvert instable ..... 87
1) Eclatement et stabilité au voisinage des points fixes ..... 88
a) La situation géométrique ..... 88
b) Un éclatement ..... 89
c) Graphes des morphismes de Frobenius ..... 89
d) Correspondances et stabilité au voisinage des points fixes ..... 91
e) L'argument géométrique de Pink ..... 92
2) Formule des points fixes de Grothendieck-Lefschetz dans le cas propre ..... 93
a) Formule d'adjonction ..... 94
b) Une formule des points fixes sur l'ouvert $\mathfrak{X}_{\emptyset}$ ..... 96
3) Généralisation au cas non propre ..... 99
a) Espaces de modules grossiers ..... 99
b) Correspondances cohomologiques ..... 100
c) Nombres d'intersections ..... 103
d) Formule des points fixes ..... 107
Chapitre V : Stabilisation des correspondances de Hecke ..... 113
1) Propriétés des espaces classifiants de chtoucas itérés ..... 114
a) Vérification de ce que les champs de chtoucas itérés sont sereins ..... 114
b) Schématisation des espaces de modules grossiers ..... 115
c) Recours à la théorie de stabilité de Mumford et Seshadri ..... 117
d) Le critère numérique de stabilité de Mumford ..... 120
e) Une condition ouverte suffisante pour vérifier la stabilité ..... 122
f) Vérification du critère de stabilité par les chtoucas itérés ..... 128
2) Stabilisation des correspondances de Hecke dans un ouvert lisse ..... 132
a) Prolongement des correspondances de Hecke par normalisation ..... 132
b) Dégénérateurs des chtoucas dégénérés ..... 134
c) Effet des transformations de φ-réseaux itérés sur les dégénérateurs ..... 137
d) Effet des correspondances de Hecke sur les dégénérateurs ..... 140
3) Stabilité des chtoucas au voisinage des points fixes ..... 142
a) La propriété de stabilité locale ..... 142
b) Un point double à valeurs dans un trait ..... 143
c) Filtration des points génériques ..... 144
d) Filtration des points spéciaux ..... 146
e) Fin de la démonstration ..... 149
Chapitre VI : Cohomologie des chtoucas et correspondance globale ..... 151
1) Enoncé de la correspondance de Langlands et réductions ..... 152
a) Fonctions L des systèmes locaux ℓ-adiques ..... 152
b) Facteurs L locaux en les places ramifiées et équation fonctionnelle ..... 154
c) Facteurs ε locaux et formule du produit de Laumon ..... 156
d) La correspondance de Langlands globale ..... 157
e) Hypothèse de récurrence et réductions ..... 159
2) Cohomologie essentielle des champs de chtoucas ..... 164
a) Cohomologie ℓ-adique des chtoucas et de leurs compactifications ..... 164
b) Faisceaux ou représentations ℓ-adiques r-négligeables ..... 166
c) Vérification de ce que le bord est r-négligeable ..... 168
d) Séparation de la cohomologie essentielle ..... 175
e) Effet r-négligeable des troncatures ..... 180
3) Scindage au moyen des correspondances de Hecke ..... 181
a) Action de l'algèbre de Hecke $\mathcal{H}_N^r$ et de $Frob_{\infty}$ et $Frob_0$ ..... 181
b) Lien avec les correspondances tronquées et stabilisées ..... 183
c) Calcul des traces des correspondances de Hecke ..... 185
d) Conclusion du raisonnement ..... 189

Chapitre VII : Conséquences de la correspondance globale ..... 193
1) Conséquences sur les représentations de groupes ..... 193
a) Quelques fonctorialités de Langlands ..... 193
b) La correspondance de Langlands locale ..... 194
c) Compatibilité entre correspondances locales et globale ..... 196
2) Conséquences sur les faisceaux ℓ-adiques ..... 198
a) Le cas des courbes lisses ..... 198
b) Le cas général ..... 200
3) Remarque sur le programme de Langlands géométrique ..... 202

Appendice A : Cohomologie ℓ-adique des champs ..... 203
1) Définition et premières propriétés ..... 203
a) Une classe de champs algébriques ..... 203
b) Cohomologie ℓ-adique des champs sereins ..... 205
c) Correspondances cohomologiques ..... 209
d) Dualité de Poincaré et pureté ..... 211
2) Classes des cycles et formules des traces ..... 214
a) Classe de cohomologie associée à un cycle ..... 214
b) La formule des traces de Grothendieck ..... 215
c) Formule des points fixes pour l’endomorphisme de Frobenius ..... 217

Appendice B : Fonctions L de paires automorphes et théorème réciproque ..... 219
1) Fonctions L de paires de représentations adéliques ..... 220
a) Facteurs L et ε locaux ..... 220
b) Classification de Bernstein et Zelevinski et facteurs L locaux ..... 222
c) Les équations fonctionnelles locales ..... 224
d) Propriétés globales des fonctions L de paires automorphes ..... 226
e) Unicité du prolongement aux places ramifiées ..... 227
2) Un théorème réciproque de Piatetski-Shapiro ..... 229
a) L’énoncé ..... 229
b) Modèles de Whittaker globaux ..... 230
c) Construction opposée et lemme principal ..... 233
d) Egalité des produits scalaires ..... 234
e) Conclusion du raisonnement ..... 236

Bibliographie ..... 239

## Chapitre I

## Rappels sur les chtoucas et leur comptage

Ce chapitre rassemble un certain nombre de resultats ant´ erieurs dont on´ aura besoin dans la suite. On renvoie à l’article [Drinfeld, 1987] pour la definition des chtoucas et l’´ etude de leurs propri´ et´ es g´ eom´ etriques et au´ livre [Lafforgue, 1997] pour les troncatures et les formules de comptage.

Tous les schemas (et champs) consid´ er´ es seront sur un même corps de´ base$\mathbb { F } _ { q }$fini à$q$el´ ements. On a fix´ e une fois pour toutes une courbe´ X projective, lisse et geom´ etriquement connexe sur´$\mathbb { F } _ { q }$. L’ensemble des points fermes de´ X est note´$| X |$; il s’identifie à celui des places du corps F des fonctions rationnelles sur X.

## 1) Les champs de chtoucas de Drinfeld

## a) Definition. Morphisme de structure´

Pour tout schema (ou champ)´ S sur$\mathbb { F } _ { q }$, on notera$\mathrm { F r o b } _ { S }$l’endomorphisme de S d’el´ evation à la puissance´$q$

Definition I.1 (Drinfeld).´ – Un chtouca (à droite) [resp. à gauche] de rang $r \geq 1$sur un schema´$S \left( s u r \mathbb { F } _ { q } \right)$consiste en

• unfibre´ E de rang r sur$X \times S ,$, autrement dit un${ \mathcal { O } } _ { X \times S }$-Module localement libre de rang r,

• une modification (à droite) [resp. à gauche] de E c’est-à-dire un diagramme

$$
\mathcal {E} \stackrel {{j}} {{\hookrightarrow}} \mathcal {E} ^ {\prime} \stackrel {{t}} {{\hookleftarrow}} \mathcal {E} ^ {\prime \prime} [ r e s p. \mathcal {E} \stackrel {{t}} {{\hookleftarrow}} \mathcal {E} ^ {\prime} \stackrel {{j}} {{\hookrightarrow}} \mathcal {E} ^ {\prime \prime} ]
$$

où$\mathcal { E } ^ { \prime } , \mathcal { E } ^ { \prime \prime }$sont deux fibres de rang r sur´$X \times S$et j, t sont deux homomorphismes injectifs dont les conoyaux sont supportes par les graphes´ de deux morphismes ∞,$0 : S  X$appeles “pôle” et´$\ " { z e r o } ^ { \prime \prime }$et sont inversibles sur${ \mathcal { O } } _ { S } ,$

• un isomorphisme$\begin{array} { r } { \tau \pounds = ( \mathrm { I d } _ { X } \times \mathrm { F r o b } _ { S } ) ^ { * } \pounds \stackrel { \sim } { \to } \mathcal { E } ^ { \prime \prime } . } \end{array}$

Pour$r \geq 1$un entier, Cht<sup>r</sup> [resp. <sup>r</sup> Cht] designe le champ classifiant les´ chtoucas (à droite) [resp. à gauche] de rang r. Il est algebrique au sens de´ Deligne-Mumford.$\mathbf { D } '$associer aux chtoucas leur pôle et leur zero d´ efinit un´ morphisme

$$
(\infty , 0): \operatorname{Cht} ^ {r} \rightarrow X \times X [ \text { resp. } (\infty , 0): ^ {r} \operatorname{Cht} \rightarrow X \times X ]
$$

qui est lisse de dimension relative$2 r - 2$

Definition I.2 (Drinfeld).´ – Soit$N = \operatorname { S p e c } ( { \mathcal { O } } _ { N } ) \hookrightarrow X$un niveau$\vec { c ^ { \prime } e s t { – } a { \cdot } }$ dire un sous-schema ferm´ e fini de X.´

Une structure de niveau N sur un chtouca$( \mathcal { E } \hookrightarrow \mathcal { E } ^ { \prime } \longleftrightarrow \mathcal { E } ^ { \prime \prime } \tilde {  } { \tau } \mathcal { E } )$ de rang r sur un schema S dont le pôle et le z´ ero´ evitent N consiste en un´ isomorphisme

$$
\mathcal {E} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N} = \mathcal {E} \otimes_ {\mathcal {O} _ {X \times S}} \mathcal {O} _ {N \times S} \stackrel {{u}} {{\to}} \mathcal {O} _ {N \times S} ^ {r}
$$

faisant commuter le diagramme :

$$
\begin{array}{c} \mathcal {E} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N} \xrightarrow {\sim} \mathcal {E} ^ {\prime} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N} \xleftarrow {\sim} \mathcal {E} ^ {\prime \prime} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N} \xleftarrow {\sim} ^ {\tau} \mathcal {E} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N} \\ \Biggl \downarrow^ {\sim} u \Biggl \downarrow^ {\sim} \mathcal {O} _ {N \times S} ^ {r} \xleftarrow {\sim_ {\tau_ {u}}} \end{array}
$$

On note$\mathrm { C h t } _ { N } ^ { r }$le champ des chtoucas de rang r avec structures de niveau N. Il est muni d’un morphisme d’oubli des structures de niveau

$$
\operatorname{Cht} _ {N} ^ {r} \rightarrow \operatorname{Cht} ^ {r} \times_ {X \times X} (X - N) \times (X - N)
$$

qui est representable fini´ etale galoisien de groupe de Galois´${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N } )$ Ainsi le morphisme de structure

$$
(\infty , 0): \operatorname{Cht} _ {N} ^ {r} \rightarrow (X - N) \times (X - N)
$$

est-il egalement lisse de dimension relative´$2 r - 2$

## b) Endomorphismes de Frobenius partiels

Sur la surface$X \times X$, on dispose des deux endomorphismes Frob$\boldsymbol { x } \times \operatorname { I d } _ { X }$et $\operatorname { I d } _ { X } \times \operatorname { F r o b } _ { X }$. Le schema intersection de tous les ouverts compl´ ementaires´ des images reciproques de la diagonale par ces endomorphismes et leurs´ puissances est note´ Λ.

Au-dessus de Λ, les champs$\operatorname { C h t } ^ { r }$et$\mathrm { C h t } _ { N } ^ { r }$sont egalement munis chacun´ de deux endomorphismes dits “de Frobenius partiels”$\mathrm { F r o b } _ { \infty }$et$\mathrm { F r o b } _ { 0 }$tels que

$$
\mathrm{Frob} _ {\infty} \circ \mathrm{Frob} _ {0} = \mathrm{Frob} _ {0} \circ \mathrm{Frob} _ {\infty} = \mathrm{Frob}
$$

et qui rendent commutatifs les diagrammes :

$$
\begin{array}{c c c} \Lambda \times_ {X \times X} \operatorname{Cht} _ {N} ^ {r} & \xrightarrow {\operatorname{Frob} _ {\infty} , \operatorname{Frob} _ {0}} & \operatorname{Cht} _ {N} ^ {r} \times_ {X \times X} \Lambda \\ \Big \downarrow & & \Big \downarrow \\ \Lambda \times_ {X \times X} \operatorname{Cht} ^ {r} & \xrightarrow {\operatorname{Frob} _ {\infty} , \operatorname{Frob} _ {0}} & \operatorname{Cht} ^ {r} \times_ {X \times X} \Lambda \\ \Big \downarrow & & \Big \downarrow \\ \Lambda & \xrightarrow {\operatorname{Frob} _ {X} \times \operatorname{Id} _ {X} , \operatorname{Id} _ {X} \times \operatorname{Frob} _ {X}} & \Lambda \end{array}
$$

On renvoie par exemple au paragraphe I.1d de [Lafforgue, 1997] pour une definition des endomorphismes´$\mathrm { F r o b } _ { \infty }$et$\mathrm { F r o b } _ { 0 }$. Precisons toutefois´ que dans toute la suite de cet article on ne se servira que de l’existence de telles paires d’endomorphismes verifiant les propri´ et´ es ci-dessus (plus´ le fait qu’ils ne modifient pas les fibres gen´ eriques des chtoucas pour la´ demonstration des th´ eorèmes de stabilit´ e globale V.14(ii) et de stabilit´ e´ locale V.18).

## c) Correspondances de Hecke

On note$\mathbb { A } = \prod _ { x \in | X | } F _ { x }$l’anneau des adèles du corps F des fonctions ration-

nelles sur la courbe X et$O _ { \mathbb { A } } = \prod O _ { x }$son sous-anneau des entiers. x∈|X|

Tout el´ ement´ g d’un des$\mathrm { G L } _ { r } ( \mathbb { A } )$induit un fibre´$\mathcal { E } ^ { g }$de rang r sur X avec structures de niveaux arbitraires, et ce de manière compatible avec le produit tensoriel. Cela induit en particulier une action du groupe des idèles $\bar { \mathbb { A } } ^ { \times } = { \bf G } { \bf L } _ { 1 } ( \mathbb { A } )$

$$
(g, \widetilde {\mathcal {E}} = (\mathcal {E} \hookrightarrow \mathcal {E} ^ {\prime} \leftarrow {} ^ {\tau} \mathcal {E})) \mapsto \mathcal {E} ^ {g} \otimes \widetilde {\mathcal {E}} = (\mathcal {E} ^ {g} \otimes \mathcal {E} \hookrightarrow \mathcal {E} ^ {g} \otimes \mathcal {E} ^ {\prime} \leftarrow \mathcal {E} ^ {g} \otimes {} ^ {\tau} \mathcal {E})
$$

sur le système projectif constitue de Cht´ <sup>r</sup> et des$\mathrm { C h t } _ { N } ^ { r }$

D’autre part, le groupe$\mathrm { G L } _ { r } ( { \cal O } _ { \mathbb { A } } ) = \varprojlim _ { N } \mathrm { G L } _ { r } ( \mathcal { O } _ { N } )$agit egalement sur les´

$$
\mathrm{Cht} _ {N} ^ {r}.
$$

Ces deux actions se prolongent par celle des “correspondances de Hecke”.

On note${ \mathcal { H } } ^ { r }$l’algèbre de Hecke des fonctions localement constantes à support compact sur$\mathrm { G L } _ { r } ( \mathbb { A } )$munies du produit de convolution pour la mesure de Haar dg qui attribue le volume 1 au sous-groupe ouvert compact maximal$K = \mathrm { G L } _ { r } ( { \cal O } _ { \mathbb { A } } )$. Pour tout niveau$N = \mathrm { S p e c } ( \bar { \mathcal { O } _ { N } } ) \hookrightarrow X$, on note $\mathcal { H } _ { N } ^ { r }$la sous-algèbre unitaire de${ \mathcal { H } } ^ { r }$constituee des fonctions invariantes à´ gauche et à droite par le sous-groupe de congruence$K _ { N } = \mathop { \mathrm { K e r } } [ K \to \mathop {  }$ ${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N } ) ]$

Soit donc f une fonction dans$\mathcal { H } _ { N } ^ { r }$. Il existe un plus petit sous-ensemble fini$T _ { f }$de$| X |$contenant les points de N et tel que, pour toute place$x \notin T _ { f }$ $f$contienne en facteur la fonction caracteristique´ 11$\mathrm { { G L } } _ { r } ( O _ { x } ) = f _ { x } ^ { 0 }$de${ \mathrm { G L } } _ { r } ( O _ { x } )$ dans${ \mathrm { G L } } _ { r } ( F _ { x } )$

La fonction f s’ecrit comme une combinaison lin´ eaire finie´

$$
f = \sum_ {i} \lambda_ {i} \cdot \mathbb {1} _ {K _ {N} g _ {i} K _ {N}}
$$

de fonctions caracteristiques´ 11$. K _ { N } g _ { i } K _ { N }$de doubles classes$K _ { N } g _ { i } K _ { N }$de $K _ { N } \backslash \mathrm { G L } _ { r } ( \mathbb { A } ) / K _ { N }$. Les$g _ { i }$qui apparaissent ici sont dans$\prod \mathrm { G L } _ { r } ( O _ { x } ) \ \times$

$$
x \notin T _ {f}
$$

$\prod { \mathrm { G L } _ { r } ( F _ { x } ) }$donc, d’après la proposition 3 du paragraphe I.4c de [Laf-$\boldsymbol { x } { \in } T _ { f }$

forgue, 1997], ils definissent des champs´$\Gamma _ { N } ^ { r } ( g _ { i } )$representables finis sur´ $\mathbf { C h f } _ { N } ^ { r } \times \mathbf { C h t } _ { N } ^ { r } \times _ { ( X \times X ) \times ( X \times X ) } ( X - T _ { f } ) \times ( \bar { X } - \dot { T _ { f } } )$(mais qui en gen´ eral ne sont´ pas des sous-champs) dont les deux projections sur${ \mathrm { C h t } } _ { N } ^ { r } \times _ { X \times X } ( X - T _ { f } ) \times$ $( X - T _ { f } )$sont representables,´ etales et finies. Ainsi, chaque´$\Gamma _ { N } ^ { r } ( g _ { i } )$est une correspondance etale relative dans´$\mathrm { C h t } _ { N } ^ { r }$au-dessus de$( X - T _ { f } ) \times ( X - T _ { f } )$

On associe alors à la fonction f la somme formelle

$$
\sum_ {i} d g (K _ {N}) \lambda_ {i} \cdot \left[ \Gamma_ {N} ^ {r} (g _ {i}) \right]
$$

dans l’algèbre des classes de correspondances etales (au sens du paragraphe´ I.4c de [Lafforgue, 1997]) dans$\mathrm { C h } \bar { \mathrm { t } } _ { N } ^ { r }$au-dessus de$( X - T _ { f } ) \times \mathsf { \bar { ( } } X - T _ { f } )$

D’après le theorème 5 du paragraphe I.4c de [Lafforgue, 1997], ceci´ definit un homomorphisme de l’algèbre unitaire´$\mathcal { H } _ { N } ^ { r }$dans l’algèbre des classes de correspondances etales dans la fibre de´$\mathrm { C h } \dot { \mathrm { t } } _ { N } ^ { r }$au-dessus du point gen´ erique de´$X \bar { \times } X$. Cette action de$\mathcal { H } _ { N } ^ { r }$commute avec celle des endomorphismes de Frobenius partiels$\mathrm { F r o b } _ { \infty }$et Frob .

Dans toute la suite de cet article, la definition pr´ ecise des correspon-´ dances de Hecke que rappellent par exemple les paragraphes I.1e et I.4c de [Lafforgue, 1997] n’interviendra$\mathrm { \ q u } ^ { \prime }$au travers des propriet´ es que nous´ venons de rappeler, du fait que les correspondances de Hecke ne modifient pas les fibres gen´ eriques des chtoucas et bien sûr des formules de comptage´ des points fixes rassemblees dans les th´ eorèmes I.5 et I.7 ci-dessous.´

## d) Troncatures

Soit α un el´ ement de´ R.

On considère$\widetilde { \mathcal { E } } = ( \mathcal { E } \overset { j } { \hookrightarrow } \mathcal { E } ^ { \prime } \overset { t } { \longleftrightarrow } \tau _ { \mathcal { E } } )$un point du champ Cht<sup>r</sup> à valeurs dans le spectre S d’un corps algebriquement clos (contenant´$\mathbb { F } _ { q } )$. Si α$\notin$ [0, 1], on suppose que le pôle$\eqslantdot$et le zero´$\overline { { 0 } }$de$\widetilde { \mathcal E }$dans$X ( S )$ne sont images l’un de l’autre par aucune puissance de Frob c’est-à-dire que$( \overline { { \infty } } , \overline { { 0 } } ) \in \Lambda ( S )$

On appelle sous-objet$\widetilde { \mathcal F }$de$\widetilde { \mathcal E }$la donnee de deux sous-fibr´ es´${ \mathcal { F } } , { \mathcal { F } } ^ { \prime }$de $\mathcal { E } , \mathcal { E } ^ { \prime }$ de même rang et maximaux (au sens que$\mathcal { E } / \mathcal { F }$et$\mathcal { E } ^ { \prime } / \mathcal { F } ^ { \prime }$sont sans torsion) et tels que$j$et t envoient$\mathcal { F }$et$\boldsymbol { \tau } _ { \mathcal { F } } \stackrel { } { = } ( \mathrm { I d } _ { X } \times \mathrm { F r o b } _ { S } ) ^ { * } \boldsymbol { \mathcal { F } }$dans${ \mathcal { F } } ^ { \prime }$ A un tel sous-objet, on peut associer son rang

$$
\mathrm{rg} \widetilde {\mathcal {F}} = \mathrm{rg} \mathcal {F} = \mathrm{rg} \mathcal {F} ^ {\prime}
$$

et aussi son degre d’indice´ α

$$
\deg_ {\alpha} \widetilde {\mathcal {F}} = (1 - \alpha) \deg \mathcal {F} + \alpha \deg \mathcal {F} ^ {\prime}.
$$

(Remarque : Par rapport à [Lafforgue, 1997], on change ici α en$1 - \alpha . )$

Si maintenant$0 = \widetilde { \mathcal { F } } _ { 0 } \subset \widetilde { \mathcal { F } } _ { 1 } \subsetneq \cdots \subsetneq \widetilde { \mathcal { F } } _ { k } = \widetilde { \mathcal { E } }$est une filtration croissante de$\widetilde { \mathcal E }$    par des sous-objets, on peut lui associer son polygone qui est la fonction affine par morceaux

$$
p: [ 0, r ] \to \mathbb {R}, \text {   avec   } p (0) = p (r) = 0,
$$

dont les seules ruptures de pente sont en les entiers rg$\widetilde { \mathcal F } _ { e }$et qui en ces entiers-là vaut

$$
p (\mathrm{rg} \widetilde {\mathcal {F}} _ {e}) = \mathrm{deg} _ {\alpha} \widetilde {\mathcal {F}} _ {e} - \frac {\mathrm{rg} \widetilde {\mathcal {F}} _ {e}}{r} \mathrm{deg} _ {\alpha} \widetilde {\mathcal {E}}, 0 \leq e \leq k.
$$

On prouve que parmi tous les polygones attaches aux filtrations de´$\widetilde { \mathcal E }$il en est un plus grand que tous les autres.$\mathrm { C } '$est le polygone canonique de Harder-Narasimhan$\overline { { p } } _ { \alpha } ^ { \widetilde { \varepsilon } }$de$\widetilde { \mathcal { E } } .$. La filtration la moins fine qui le definit est´ appelee la filtration canonique de Harder-Narasimhan (d’indice´$\alpha )$de$\widetilde { \mathcal { E } } .$.

Nous rappelons (voir le theorème 8 du paragraphe II.2b de [Lafforgue,´ 1997]) :

Proposition I.3. – Etant donne´ α un reel´ [resp. un reel dans´ [0, 1]] et $p : [ 0 , r ] \to \mathbb { R } _ { + }$un polygone convexe de troncature, il existe dans le champ Cht<sup>r</sup>$\times _ { X \times X } \Lambda$[resp. Cht<sup>r</sup>] un unique ouvert$\mathrm { C h t } ^ { r , \overline { { p } } _ { \alpha } \leq p }$tel qu’un point geom´ etrique´$\widetilde { \mathcal E }$de ce champ est dans l’ouvert$\mathrm { C h t } ^ { r , \overline { { p } } _ { \alpha } \leq p }$si et seulement si son polygone canonique$\overline { { p } } _ { \alpha } ^ { \widetilde { \varepsilon } }$est majore par p.´!"

Le champ$\operatorname { C h t } ^ { r }$s’ecrit comme une somme disjointe´

$$
\mathrm{Cht} ^ {r} = \coprod_ {d \in \mathbb {Z}} \mathrm{Cht} ^ {r, d}
$$

où les$\mathrm { C h t } ^ { r , d }$classifient les chtoucas$\widetilde { \mathcal { E } } \ = \ ( \mathcal { E } \ \hookrightarrow \ \mathcal { E } ^ { \prime } \  \ \tau \mathcal { E } )$de degre´ deg$\varepsilon = d$

Chaque$\mathrm { C h t } ^ { r , d }$n’a qu’un nombre fini de composantes connexes et est localement de type fini puisque lisse sur$X \times X$mais il n’est pas de type fini si$r \geq 2$. En revanche, les ouverts${ \mathrm { C h t } } ^ { r , d , \overline { { p } } _ { \alpha } \leq p } = { \mathrm { C h t } } ^ { r , d } \cap { \mathrm { C h t } } ^ { r , \overline { { p } } _ { \alpha } \leq p }$sont de type fini.

Le groupe$\mathbb { A } ^ { \times }$agissant sur$\operatorname { C h t } ^ { r }$stabilise chaque ouvert$\mathrm { C h t } ^ { r , \overline { { p } } _ { \alpha } \leq p }$. Choisissant un idèle$a \in \mathbb { A } ^ { \times }$de degre non nul, on peut consid´ erer le quotient´

$$
\operatorname{Cht} ^ {r} / a ^ {\mathbb {Z}} \cong \coprod_ {0 \leq d <   r | \deg (a) |} \operatorname{Cht} ^ {r, d}
$$

qui donc est reunion filtrante des ouverts de type fini´

$$
\operatorname{Cht} ^ {r, \overline {{p}} _ {\alpha} \leq p} / a ^ {\mathbb {Z}} \cong \coprod_ {0 \leq d <   r | \deg (a) |} \operatorname{Cht} ^ {r, d, \overline {{p}} _ {\alpha} \leq p}.
$$

Pour$N = \operatorname { S p e c } ( { \mathcal { O } } _ { N } ) \hookrightarrow X$un niveau, on notera$\mathbf { C h t } _ { N } ^ { r } , \mathbf { C h t } _ { N } ^ { r , \overline { { p } } _ { \alpha } \leq p }$et $\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } _ { \alpha } \leq p }$les images reciproques par le morphisme d’oubli des structures´ de niveau$\mathrm { C h t } _ { N } ^ { r } \to \mathrm { C h t } ^ { r }$des ouverts$\mathrm { C h t } ^ { r , d } , \mathrm { C h t } ^ { r , \overline { { p } } _ { \alpha } \leq p } \mathrm { e t } \mathrm { C h t } ^ { r , d , \overline { { p } } _ { \alpha } \leq p }$

Sur Cht<sup>r</sup>$/ a ^ { \mathbb { Z } }$et les$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb Z }$, il y a bien sûr une action de$\mathbb { A } ^ { \times } / a ^ { \mathbb { Z } }$, de $\mathrm { G L } _ { r } ( O _ { \mathbb { A } } )$et des endomorphismes de Frobenius partiels$\mathrm { F r o b } _ { \infty }$et Frob .

Et pour$N \hookrightarrow X$un niveau, il y a une action par correspondances etales´ dans la fibre de$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb Z }$au-dessus du point gen´ erique de´$\bar { X } \times X$de l’algèbre $\mathcal { H } _ { N } ^ { r } / a ^ { \mathbb { Z } }$quotient de$\mathcal { H } _ { N } ^ { r }$par$a ^ { \mathbb { Z } }$(laquelle s’identifie à l’algèbre des fonctions à support compact sur${ \mathrm { G L } } _ { r } ( \mathbb { A } ) / a ^ { \mathbb { Z } }$invariantes des deux côtes par´$K _ { N } )$

Cependant, les ouverts de type fini$\mathrm { C h t } ^ { r , \overline { { p } } _ { \alpha } \leq p } / a ^ { \mathbb { Z } }$ne sont pas stabilises´ par$\mathrm { F r o b } _ { \infty }$ou$\mathrm { F r o b } _ { 0 }$et un$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } _ { \alpha } \overset { - } { \leq } p } / a ^ { \mathbb { Z } }$n’est stabilise par la correspondance´ de Hecke associee à une fonction´$f \in \mathcal { H } _ { N } ^ { r } / a ^ { \mathbb { Z } }$que si celle-ci est supportee´ par$\mathbb { A } ^ { \times } \cdot K$

## e) Nombres de Lefschetz

Considerons´ f une fonction dans$\mathcal { H } _ { N } ^ { r }$, ∞ et 0 deux places distinctes en dehors de$T _ { f } , \overline { { \infty } }$et$\overline { { 0 } }$deux points geom´ etriques dans´$X ( \overline { { \mathbb { F } } } _ { q } )$au-dessus de ∞ et 0, et$s ^ { \prime } , u ^ { \prime } \geq 1$deux entiers. On ecrit à nouveau´

$$
f = \sum_ {i} \lambda_ {i} \cdot \mathbb {1} _ {K _ {N} g _ {i} K _ {N}}.
$$

Les puissances$\mathrm { F r o b } _ { \infty } ^ { \mathrm { d e g ( \infty ) } s ^ { \prime } } \mathrm { e t F r o b } _ { 0 } ^ { \mathrm { d e g ( 0 ) } u ^ { \prime } }$stabilisent la fibre de$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb Z }$ au-dessus de$( \overline { { \infty } } , \overline { { 0 } } )$et on peut considerer dans cette fibre les correspon-´ dances composees´

$$
\Gamma_ {N} ^ {r} (g _ {i}) \times \operatorname{Frob} _ {\infty} ^ {\deg (\infty) s ^ {\prime}} \times \operatorname{Frob} _ {0} ^ {\deg (0) u ^ {\prime}}.
$$

Elles coupent transversalement la diagonale, c’est-à-dire que leurs produits fibres avec celle-ci sont´ etales sur´$\overline { { \mathbb { F } } } _ { q }$et finis sur$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb { Z } } \times _ { X \times X } ( \overline { { \infty } } , \overline { { 0 } } )$ Ils deviennent finis absolument si on les restreint aux ouverts de type fini

$$
\mathrm{Cht} _ {N} ^ {r, \overline {{p}} _ {\alpha} \leq p} / a ^ {\mathbb {Z}}
$$

et, comptant chaque point fixe avec sa multiplicite´ egale à l’inverse du´ nombre fini de ses automorphismes, on peut alors introduire leurs cardinaux notes´

$$
\operatorname{Lef} _ {\overline {{\infty}}, \overline {{0}}} ^ {r, \overline {{p}} _ {\alpha} \leq p} \left(g _ {i} \times \operatorname{Frob} _ {\infty} ^ {\deg (\infty) s ^ {\prime}} \times \operatorname{Frob} _ {0} ^ {\deg (0) u ^ {\prime}}\right).
$$

Puis on pose

$$
\begin{array}{l} \operatorname{Lef} _ {\overline {{\infty}}, \overline {{0}}} ^ {r, \overline {{p}} _ {\alpha} \leq p} \left(f \times \operatorname{Frob} _ {\infty} ^ {\deg (\infty) s ^ {\prime}} \times \operatorname{Frob} _ {0} ^ {\deg (0) u ^ {\prime}}\right) \\ = \sum_ {i} d g (K _ {N}) \lambda_ {i} \cdot \operatorname{Lef} _ {\overline {{\infty}}, \overline {{0}}} ^ {r, \overline {{p}} _ {\alpha} \leq p} \left(g _ {i} \times \operatorname{Frob} _ {\infty} ^ {\deg (\infty) s ^ {\prime}} \times \operatorname{Frob} _ {0} ^ {\deg (0) u ^ {\prime}}\right). \end{array}
$$

## 2) Comptage des points fixes et expression spectrale

a) Variantes des traces tronquees d’Arthur´

On fixe un niveau N.

On considère f une fonction dans$\mathcal { H } _ { N } ^ { r } / a ^ { \mathbb { Z } }$et$\infty$, 0 deux places distinctes dans$| X | - T _ { f }$. Par definition de´$T _ { f }$, la fonction$f$se factorise en$f =$ $f ^ { \infty , 0 } \otimes f _ { \infty } ^ { 0 } \otimes { f _ { 0 } ^ { 0 } }$où$f _ { \infty } ^ { 0 }$et$f _ { 0 } ^ { 0 }$designent les fonctions caract´ eristiques de´ ${ \mathrm { G L } } _ { r } ( O _ { \infty } )$et${ \mathrm { G L } } _ { r } ( O _ { 0 } )$dans$\begin{array} { r } { \dot { \bf G L } _ { r } ( F _ { \infty } ) } \end{array}$et${ \mathrm { G L } } _ { r } ( F _ { 0 } )$

Etant donnes encore´$s ^ { \prime } , u ^ { \prime } \geq 1$deux entiers, on introduit la fonction $f _ { s ^ { \prime } , u ^ { \prime } } = f ^ { \infty , 0 } \otimes f _ { \infty } ^ { - s ^ { \prime } } \otimes f _ { 0 } ^ { u ^ { \prime } }$où$f _ { \infty } ^ { - s ^ { \prime } }$et$f _ { 0 } ^ { u ^ { \prime } }$sont les fonctions spheriques de´ Drinfeld de niveaux$- s ^ { \prime }$et$u ^ { \prime }$en ∞ et 0 (voir par exemple la definition´$^ { 7 }$ du paragraphe III.6c de [Lafforgue, 1997] ou bien le corollaire I.8 du paragraphe 2d ci-dessous qui peut être consider´ e comme une d´ efinition´ equivalente).´

On dispose des traces tronquees d’Arthur´

$$
\operatorname{Tr} ^ {\leq p} (f _ {s ^ {\prime}, u ^ {\prime}}) = \operatorname{Tr} ^ {\leq p} \left(f ^ {\infty , 0} \otimes f _ {\infty} ^ {- s ^ {\prime}} \otimes f _ {0} ^ {u ^ {\prime}}\right)
$$

pour$p : [ 0 , r ] \to \mathbb { R } _ { + }$un polygone convexe de troncature.

Nous allons rappeler comment elles sont definies. On note´$\mathcal { P } _ { 0 }$l’ensemble des sous-groupes paraboliques standards de${ \mathrm { G L } } _ { r } = G$et, pour$P \in \mathcal { P } _ { 0 }$, on note$N _ { P }$son radical unipotent,$M _ { P }$son sous-groupe de$\operatorname { L e v i } , | P |$le nombre de facteurs de$M _ { P }$et$d n _ { P }$la mesure de Haar sur$N _ { P } ( \mathbb { A } )$qui attribue le volume 1 à$N _ { P } ( O _ { \mathbb { A } } )$

Pour tout$P \in \mathcal { P } _ { 0 }$, on considère l’operateur de convolution à droite par´ $f _ { s ^ { \prime } , u ^ { \prime } }$dans l’espace des fonctions localement integrables sur´$M _ { P } ( F ) N _ { P } ( \mathbb { A } ) \backslash$ $\overset { \cdot } { G } ( \mathbb { A } ) / a ^ { \mathbb { Z } }$. Cet operateur admet le noyau´

$$
K _ {f _ {s ^ {\prime}, u ^ {\prime}}, P}: (g, g ^ {\prime}) \mapsto \sum_ {\gamma \in M _ {P} (F)} \int_ {N _ {P} (\mathbb {A})} d n _ {P} \cdot f _ {s ^ {\prime}, u ^ {\prime}} (g ^ {\prime - 1} \gamma n _ {P} g).
$$

D’autre part, on a une application naturelle

$$
\mathrm{GL} _ {r} (\mathbb {A}) \to N _ {P} (\mathbb {A}) \backslash \mathrm{GL} _ {r} (\mathbb {A}) / \mathrm{GL} _ {r} (O _ {\mathbb {A}}) \stackrel {{\sim}} {{\to}} M _ {P} (\mathbb {A}) / M _ {P} (O _ {\mathbb {A}}) \stackrel {{\deg}} {{\longrightarrow}} \mathbb {Z} ^ {| P |}
$$

et on note$g \mapsto \mathbb { I } ( p _ { P } ^ { g } > _ { P } p )$la fonction caracteristique du sous-ensemble´ des$g \in { \mathrm { G L } } _ { r } ( { \mathbb { A } } ) = G ( { \mathbb { A } } )$dont l’image$( d _ { 1 } , \ldots , d _ { | P | } )$dans$\mathbb { Z } ^ { | P | }$verifie´

$$
d _ {1} + \dots + d _ {j} - \frac {r _ {1} + \cdots + r _ {j}}{r} (d _ {1} + \dots + d _ {| P |}) > p (r _ {1} + \dots + r _ {j}), 1 \leq j <   | P |
$$

(si$r _ { 1 } , \ldots , r _ { | P | }$designent les rangs des facteurs de´$M _ { P } )$

Les traces tronquees d’Arthur sont les int´ egrales convergentes´

$$
\begin{array}{l} \operatorname{Tr} ^ {\leq p} (f _ {s ^ {\prime}, u ^ {\prime}}) = \int_ {G (F) \backslash G (\mathbb {A}) / a ^ {\mathbb {Z}}} d g \\ \sum_ {P \in \mathcal {P} _ {0}} (- 1) ^ {| P | - 1} \sum_ {\delta \in P (F) \backslash G (F)} \mathbb {1} \left(p _ {P} ^ {\delta g} > _ {P} p\right) K _ {f _ {s ^ {\prime}, u ^ {\prime}}, P} (\delta g, \delta g). \end{array}
$$

Or notre fonction$f _ { s ^ { \prime } , u ^ { \prime } }$contient en facteur la fonction spherique de´ Drinfeld$f _ { \infty } ^ { - s ^ { \prime } }$(ainsi que$f _ { 0 } ^ { u ^ { \prime } } )$. Ceci va nous permettre de definir des variantes´ $\mathrm { T r } _ { \alpha } ^ { \le p } ( f _ { s ^ { \prime } , u ^ { \prime } } )$de$\mathrm { T r } ^ { \le p } ( f _ { s ^ { \prime } , u ^ { \prime } } )$indexees par les´$\alpha \in \mathbb { R }$

Tout d’abord, en toute place$x \in | X |$, les fonctions spheriques de Drinfeld´ $f _ { x } ^ { t } ~ ( t \in \mathbb { Z } - \{ 0 \} )$et les fonctions caracteristiques´$\mathbf { \hat { \mathcal { f } } } _ { x } ^ { 0 }$de${ \mathrm { G L } } _ { r } ( O _ { x } )$dans $\mathrm { { \dot { G L } } } _ { r } ( F _ { x } )$en les differents rangs´ r sont reliees de la façon suivante :´

Proposition I.4. – Etant donnes´$P \in \mathcal { P } _ { 0 }$un sous-groupe parabolique standard de${ \mathrm { G L } } _ { r } = G$et$x \ \in \ | X |$une place de F, munissons$N _ { P } ( F _ { x } )$de la mesure de Haar$d n _ { x }$qui attribue le volume 1 à$N _ { P } ( O _ { x } )$et notons$\rho _ { P }$la racine carree du caractère modulaire de´$N _ { P } ( F _ { x } )$

Alors pour tout$t ~ \in ~ \mathbb { Z } \mathrm { ~ - ~ } \{ 0 \}$et tout$( m ^ { 1 } , \ldots , m ^ { | P | } ) \ \in \ M _ { P } ( \mathbb { A } ) \ =$ $\mathrm { G L } _ { r _ { 1 } } ( \mathbb { A } ) \times \cdot \cdot \cdot \times \mathrm { G L } _ { r _ { | P | } } ( \mathbb { A } )$, on a

$$
\begin{array}{l} \rho_ {P} (m ^ {1}, \ldots , m ^ {| P |}) \int_ {N _ {P} (F _ {x})} f _ {x} ^ {t} \big ((m ^ {1}, \ldots , m ^ {| P |}) n _ {x} \big) \cdot d n _ {x} \\ = \sum_ {1 \leq i \leq | P |} q ^ {\deg (x) \frac {r - r _ {i}}{2} | t |} f _ {x} ^ {t} (m ^ {i}) \prod_ {j \neq i} f _ {x} ^ {0} (m ^ {j}). \end{array}
$$

Demonstration :´ Voir [Laumon, 1996] volume I, proposition 4.2.5. !"

En appliquant cette proposition au facteur$f _ { \infty } ^ { - s ^ { \prime } }$de$f _ { s ^ { \prime } , u ^ { \prime } }$, on determine´ pour tout$P \in \mathcal { P } _ { 0 }$une decomposition du noyau´$K _ { f _ { s ^ { \prime } , u ^ { \prime } } , P }$en une somme

$$
K _ {f _ {s ^ {\prime}, u ^ {\prime}}, P} = \sum_ {1 \leq i \leq | P |} K _ {f _ {s ^ {\prime}, u ^ {\prime}}, P} ^ {i}.
$$

D’autre part, si$P ~ \in ~ \mathcal { P } _ { 0 }$est un sous-groupe parabolique standard de $\operatorname { G L } _ { r } = G \operatorname { e t } { \underline { { r } } } = ( r _ { 1 } , \ldots , r _ { k } ) , r _ { 1 } + \cdot \cdot \cdot + r _ { k } = r _ { : }$, est la suite des rangs des facteurs de$M _ { P }$, on introduit pour tout indice i,$1 \leq i \leq k$, le polygone$p _ { P } ^ { i } =$ $p _ { \underline { { r } } } ^ { i } : [ 0 , r ]$R qui est affine sur chaque intervalle$[ r _ { 1 } + \cdot \cdot \cdot + r _ { j - 1 } , r _ { 1 } + \cdot \cdot \cdot$ $+ r _ { j } ]$et verifie´

$$
p _ {P} ^ {i} (r _ {1} + \dots + r _ {j}) = \left\{ \begin{array}{l l} - \frac {r _ {1} + \cdots + r _ {j}}{r} & \text { si } 0 \leq j <   i , \\ 1 - \frac {r _ {1} + \cdots + r _ {j}}{r} & \text { si } i \leq j \leq k . \end{array} \right.
$$

Ceci etant pos´ e, on d´ efinit pour tout´$\alpha \in \mathbb { R }$les variantes suivantes des traces tronquees d’Arthur´

$$
\begin{array}{c} \operatorname{Tr} _ {\alpha} ^ {\leq p} (f _ {s ^ {\prime}, u ^ {\prime}}) = \int_ {G (F) \backslash G (\mathbb {A}) / a ^ {\mathbb {Z}}} d g \cdot \sum_ {P \in \mathcal {P} _ {0}} (- 1) ^ {| P | - 1} \sum_ {1 \leq i \leq | P |} \sum_ {\delta \in P (F) \backslash G (F)} \\ \mathbb {1} \left(p _ {P} ^ {\delta g} > _ {P} p - \alpha p _ {P} ^ {i}\right) K _ {f _ {s ^ {\prime}, u ^ {\prime}}, P} ^ {i} (\delta g, \delta g). \end{array}
$$

(Remarque : Par rapport à [Lafforgue, 1997], on a change ici´$p _ { P } ^ { i }$en${ \textstyle \frac { 1 } { r } } p _ { P } ^ { i }$ou, ce qui revient au même, α en$\textstyle { \frac { \alpha } { r } } . )$

Il est evident sur la d´ efinition que´$\mathrm { T r } _ { 0 } ^ { \le p } ( f _ { s ^ { \prime } , u ^ { \prime } } ) = \mathrm { T r } ^ { \le p } ( f _ { s ^ { \prime } , u ^ { \prime } } )$et d’après [Lafforgue, 1997, paragraphe VI.2f, theorème 11], on sait que la fonction´ $\alpha \mapsto \mathrm { T r } _ { \alpha } ^ { \le p } ( f _ { s ^ { \prime } , u ^ { \prime } } )$est en escalier et periodique de p´ eriode´ r!r (et même en fait r!).

## b) Egalite en moyenne sur les´$\alpha \in \mathbb { R }$

On rappelle que, parlant d’un polygone$p : [ 0 , r ] \to \mathbb { R }$, l’expression “si p est assez convexe” signifie “si toutes les differences de pentes´$[ p ( { \boldsymbol { r } } ^ { \prime } ) -  \} ]  \}$ $p ( r ^ { \prime } - 1 ) ] - [ p ( r ^ { \prime } + 1 ) - p ( r ^ { \prime } ) ] , 1 \le r ^ { \prime } < r .$, sont superieures à un nombre´ reel assez grand”.´

Nous pouvons maintenant reproduire le resultat central de [Laffor-´ gue, 1997] (c’est le theorème 1 du paragraphe V.2a) :´

Theor´ eme I.5.\` – Soient$N \hookrightarrow X$un niveau,$f \in \mathcal { H } _ { N } ^ { r } / a ^ { \mathbb { Z } }$une fonction, ∞ et 0 deux places distinctes dans$| X | - T _ { f }$avec donc$\ddot { f } = f ^ { \infty , 0 } \otimes f _ { \infty } ^ { 0 } \otimes f _ { 0 } ^ { 0 }$ et$u ^ { \prime } , s ^ { \prime } \geq 1$deux entiers.

On suppose que deg(0) et deg(∞) sont assez grands en fonction du support de f et de$t = \deg ( 0 ) u ^ { \prime } - \deg ( \infty ) s ^ { \prime }$(cette condition etant vide si´ f est supportee par´$\mathbb { A } ^ { \times } \cdot \mathrm { G L } _ { r } ( O _ { \mathbb { A } } )$et si$t = 0 )$.

Enfin, soit$p : [ 0 , r ] \to \mathbb { R } _ { + }$un polygone de troncature assez convexe en fonction de N et du support de f .

Alors,pour ∞ et 0 deuxpoints de$X ( \overline { { \mathbb { F } } } _ { q } )$au-dessus de ∞ et 0, lafonction sur R

$$
\alpha \mapsto \operatorname{Lef} _ {\overline {{\infty}}, \overline {{0}}} ^ {r, \overline {{p}} _ {\alpha} \leq p} \left(f \times \operatorname{Frob} _ {\infty} ^ {\deg (\infty) s ^ {\prime}} \times \operatorname{Frob} _ {0} ^ {\deg (0) u ^ {\prime}}\right)
$$

est en escalier et periodique (de p´ eriode le p.g.c.d de´ deg(∞) et deg(0)) et sa moyenne est egale à celle de la fonction´ egalement en escalier et´ periodique´

$$
\alpha \mapsto \operatorname{Tr} _ {\alpha} ^ {\leq p} \left(f ^ {\infty , 0} \otimes f _ {\infty} ^ {- s ^ {\prime}} \otimes f _ {0} ^ {u ^ {\prime}}\right).
$$

## c) Egalite en moyenne sur les´$\eqslantgtr$ou les$\overline { { 0 } }$

On s’aperçoit qu’on peut remplacer la moyenne sur les$\alpha \in \mathbb { R }$par une moyenne sur les$\eqslantdot$(ou les$\overline { { 0 } } )$au-dessus de la place ∞ (ou 0) fixee. Nous´ aurons besoin dans la suite de cette adaptation.

On commence par :

Lemme I.6. – Soient un niveau$N \hookrightarrow X$, une fonction$f \in \mathcal { H } _ { N } ^ { r } / a ^ { \mathbb { Z } }$, deux points ∞,${ \overline { { 0 } } } \in X ( { \overline { { \mathbb { F } } } } _ { q } )$au-dessus de deux places distinctes$\infty , 0 \in | X | - T _ { f }$ et deux entiers$s ^ { \prime } , u ^ { \prime } \geq 1$

Alors pour tout polygone de troncature$p : [ 0 , r ] \to \mathbb { R } _ { + }$et tout$\alpha \in \mathbb { R }$ les suites

$$
\begin{array}{l} \mathbb {Z} \ni n \mapsto \operatorname{Lef} _ {\operatorname{Frob} ^ {n} (\overline {{\infty}}), \overline {{0}}} ^ {r, \overline {{p}} _ {\alpha} \leq p} \left(f \times \operatorname{Frob} _ {\infty} ^ {\deg (\infty) s ^ {\prime}} \times \operatorname{Frob} _ {0} ^ {\deg (0) s ^ {\prime}}\right) \\ \mathbb {Z} \ni n \mapsto \operatorname{Lef} _ {\overline {{\infty}}, \operatorname{Frob} ^ {n} (\overline {{0}})} ^ {r, \overline {{p}} _ {\alpha} \leq p} \left(f \times \operatorname{Frob} _ {\infty} ^ {\deg (\infty) s ^ {\prime}} \times \operatorname{Frob} _ {0} ^ {\deg (0) s ^ {\prime}}\right) \end{array}
$$

sont periodiques de p´ eriode le p.g.c.d de´ deg(∞), deg(0) et r!.

Demonstration :´ Ces deux suites se deduisent l’une de l’autre par le change-´ ment de variables n$\mapsto - n$. La première est periodique de p´ eriode deg´ (∞) et la seconde de periode deg´ (0) car$\mathrm { F r o b } ^ { \mathrm { d e g ( \infty ) } } ( \overline { { \infty } } ) = \overline { { \infty } } \mathrm { e t } \mathrm { \bar { F } r o b } ^ { \mathrm { d e g ( 0 ) } } ( \overline { { 0 } } ) = \overline { { 0 } } .$ Il reste seulement à prouver que r! est aussi une periode.´

On se reporte pour cela à la formule integrale pour le nombre des´ points fixes qui est enonc´ ee dans la proposition 2 du paragraphe III.6b´ de [Lafforgue, 1997]. Bien sûr, les domaines d’integration sont limit´ es´ aux$( m _ { \tilde { \infty } } , g _ { \infty } ^ { \tilde { \infty } } , g ^ { \infty , 0 } , g _ { 0 } ^ { \tilde { 0 } } , m _ { \tilde { 0 } } )$dont le polygone α-canonique est majore par´ p. Le sens de ces conditions est explicite dans le lemme´$1 ( \mathrm { v i } ) ( \mathrm { v i i } )$du même paragraphe III.6b. On voit d’après cela qu’il suffit de montrer que r! appartient à l’image de l’homomorphisme de degre´

$$
\operatorname{End} (E ^ {\prime}) _ {\gamma^ {\prime}} ^ {\times} (\mathbb {A} ^ {\infty , 0}) \xrightarrow {\deg} \mathbb {Z}
$$

pour tout el´ ement´$( u ^ { \prime } \deg ( 0 ) , s ^ { \prime } \deg ( \infty ) )$-admissible$\gamma = ( \gamma ^ { \prime } , \gamma ^ { \prime \prime } )$dans $\mathrm { G L } _ { r } ( F )$. Or, etant donn´ e un tel´ el´ ement´$\gamma = ( \gamma ^ { \prime } , \gamma ^ { \prime \prime } ) , F ^ { \prime } = F [ \gamma ^ { \prime } ]$est un corps extension de F de$\mathrm { d e g r e } \le r$, le corps des constantes de$F ^ { \prime }$est une extension de$\mathbb { F } _ { q }$de degre´$h \leq r$et l’image de l’homomorphisme deg ci-dessus est$h \mathbb { Z } . \mathbf { D } ^ { \ast }$où la conclusion.!"

On a la variante suivante du theorème I.5 :´

Theor´ eme I.7.\` – Soient un niveau$N \hookrightarrow X ,$, unefonction$f \in \mathcal { H } _ { N } ^ { r } / a ^ { \mathbb { Z } }$, deux points$\overline { { \infty } } , \overline { { 0 } } \in X ( \overline { { \mathbb { F } } } _ { q } )$au-dessus de deux places distinctes$\infty , 0 \in | X | - T _ { f }$ et deux entiers$s ^ { \prime } , u ^ { \prime } \geq 1$

On suppose que deg(0) et deg(∞) sont assez grands en fonction du support de f et de$t = \deg ( 0 ) u ^ { \prime } - \deg ( \infty ) s ^ { \prime }$(cette condition etant vide si´ f est supportee par´$\mathbb { A } ^ { \times } \cdot \mathrm { G L } _ { r } ( O _ { \mathbb { A } } )$et si$t = 0 )$

Enfin, soient$p : [ 0 , r ] \to \mathbb { R } _ { + }$un polygone de troncature assez convexe enfonction de N et du support de f et α un nombre reel.´

Alors les deux suites periodiques´

$$
\begin{array}{l} n \mapsto \operatorname{Lef} _ {\operatorname{Frob} ^ {n} (\overline {{\infty}}), \overline {{0}}} ^ {r, \overline {{p}} _ {\alpha} \leq p} \left(f \times \operatorname{Frob} _ {\infty} ^ {\deg (\infty) s ^ {\prime}} \times \operatorname{Frob} _ {0} ^ {\deg (0) u ^ {\prime}}\right) \\ n \mapsto \operatorname{Lef} _ {\overline {{\infty}}, \operatorname{Frob} ^ {n} (\overline {{0}})} ^ {r, \overline {{p}} _ {\alpha} \leq p} \left(f \times \operatorname{Frob} _ {\infty} ^ {\deg (\infty) s ^ {\prime}} \times \operatorname{Frob} _ {0} ^ {\deg (0) u ^ {\prime}}\right) \end{array}
$$

ont la même moyenne que la suite egalement p´ eriodique´

$$
n \mapsto \operatorname{Tr} _ {\alpha + n} ^ {\leq p} \left(f ^ {\infty , 0} \otimes f _ {\infty} ^ {- s ^ {\prime}} \otimes f _ {0} ^ {u ^ {\prime}}\right).
$$

Demonstration :´ Il faut reprendre la demonstration du th´ eorème I.5 telle´ qu’elle est exposee dans [Lafforgue, 1997]. Il´$\boldsymbol { \mathrm { n ^ { \prime } y } }$a à changer$\mathrm { \ q u } ^ { \mathrm { ; } }$’une partie du paragraphe V.2d, pages 243 à 247. L’argument est essentiellement le même :

On voit apparaître des expressions de la forme

$$
\sum_ {n \in \mathbb {Z} \cap I} \int_ {H (\mathbb {A})} d h \cdot \varphi (h) \mathbb {1} (\deg (h) = n)
$$

avec H un sous-groupe de${ \mathrm { G L } } _ { r } , \varphi$une fonction sur$H ( \mathbb { A } )$muni$\mathrm { d } ^ { \prime }$une mesure de Haar dh,$h \mapsto \mathbb { 1 } ( \deg ( h ) = n )$les fonctions caracteristiques des´ ensembles d’el´ ements de´$H ( \mathbb { A } )$de degre´$n \in \mathbb { Z }$et I un intervalle borne de´ R.

Or, de la suite

$$
n \mapsto \int_ {H (\mathbb {A})} d h \cdot \varphi (h) \mathbb {1} (\deg (h) = n)
$$

qui est periodique de p´ eriode´$r ! . .$, on ne connaît que la valeur moyenne.

Cependant, de remplacer$\overline { { \infty } }$par Frob$( \overline { { \infty } } )$ou$\overline { { 0 } }$par Frob(0) ou encore α par$\alpha + 1$a toujours pour effet de translater I par 1 ou −1. Cela permet de terminer le calcul de la même façon,$\mathrm { \ q u } ^ { \prime }$on fasse une moyenne sur les$\overline { { \infty } } .$ sur les$\overline { { 0 } }$ou sur les$\alpha .$!"

## d) Valeurs propres de Hecke

Etant donnee´$x \in | X |$une place de$F _ { ; }$, on note$\mathcal { H } _ { x } ^ { r }$l’algèbre de convolution des fonctions localement constantes à support compact sur${ \mathrm { G L } } _ { r } ( F _ { x } ) =$ $G ( F _ { x } )$pour la mesure de Haar$d g _ { x }$qui attribue le volume 1 au sous-groupe ouvert compact maximal${ \mathrm { G L } } _ { r } ( O _ { x } ) = K _ { x }$

D’après Satake et notant toujours$f _ { x } ^ { 0 }$la fonction caracteristique de´$K _ { x }$ dans${ \mathrm { G L } } _ { r } ( F _ { x } )$, la sous-algèbre$f _ { x } ^ { 0 } \mathcal { H } _ { x } ^ { r } \ddot { f } _ { x } ^ { 0 }$de$\mathcal { H } _ { x } ^ { r }$constituee des fonctions´ invariantes à gauche et à droite par$K _ { x }$est commutative et elle est canoniquement isomorphe à l’algèbre de polynômes symetriques´

$$
\mathbb {C} \left[ Z _ {1}, Z _ {1} ^ {- 1}, \dots , Z _ {r}, Z _ {r} ^ {- 1} \right] ^ {\mathfrak {G} _ {r}}.
$$

On a comme consequence de la proposition I.4 :´

Corollaire I.8. – Pour tout$t \in \mathbb { Z } - \{ 0 \}$, la fonction spherique de Drinfeld´ $\begin{array} { r } { f _ { x } ^ { t } \in f _ { x } ^ { 0 } \mathcal { H } _ { x } ^ { r } f _ { x } ^ { 0 } } \end{array}$de niveau t correspond, via l’isomorphisme de Satake, au polynôme symetrique´

$$
q ^ {\deg (x) \frac {r - 1}{2} | t |} \left(Z _ {1} ^ {t} + \dots + Z _ {r} ^ {t}\right).
$$

Demonstration :´ Voir [Laumon, 1996] volume I, corollaire 4.2.6.

Si$\pi _ { x }$est une representation admissible irr´ eductible de´$\mathcal { H } _ { x } ^ { r }$qui est non ramifiee c’est-à-dire telle que´$\pi _ { x } \cdot f _ { x } ^ { 0 } \neq 0 .$, alors le module$\pi _ { x } \cdot f _ { x } ^ { 0 }$sur l’algèbre commutative$f _ { x } ^ { 0 } \mathcal { H } _ { x } ^ { r } f _ { x } ^ { 0 }$est lui-même irreductible donc de dimen-´ sion 1 et il existe r nombres complexes$z _ { 1 } ( \pi _ { x } ) , \ldots , z _ { r } ( \pi _ { x } )$, bien determin´ es´ à permutation près, tels que, pour tout$t \in \mathbb { Z } - \{ 0 \}$, l’action de$f _ { x } ^ { t }$sur$\pi _ { x }$ soit egale à la multiplication par´$q ^ { \deg ( x ) { \frac { r - 1 } { 2 } } | t | } ( z _ { 1 } ( \pi _ { x } ) ^ { t } + \cdot \cdot \cdot + z _ { r } ( \pi _ { x } ) ^ { t } )$. Ces nombres sont appeles les “valeurs propres de Hecke” de la repr´ esentation´ non ramifiee´$\pi _ { x }$

Bien sûr, si$\pi _ { x }$est ramifiee c’est-à-dire si´$\pi _ { x } \cdot f _ { x } ^ { 0 } = 0 .$, les actions sur$\pi _ { x }$ des fonctions spheriques et en particulier des´$f _ { x } ^ { t }$sont nulles.

## e) Laformule des traces d’Arthur-Selberg

En combinant la proposition I.4 et le corollaire I.8 ci-dessus avec le theorème´ $_ { 1 2 } ,$du paragraphe VI.2f de [Lafforgue, 1997], on obtient :

Theor´ eme I.9.\` – Etant donnes une fonction´$f \in { \mathcal { H } } ^ { r } / a ^ { \mathbb { Z } }$, deux places distinctes$\infty , 0 \in | X | - T _ { f }$et deux entiers$s ^ { \prime } , u ^ { \prime } \geq 1$, on a pour tout polygone de troncature$p : [ 0 , r ] \to \mathbb { R }$et tout reel´ α

$$
\begin{array}{l} \operatorname{Tr} _ {\alpha} ^ {\leq p} \left(f ^ {\infty , 0} \otimes f _ {\infty} ^ {- s ^ {\prime}} \otimes f _ {0} ^ {u ^ {\prime}}\right) = \sum_ {(P, \pi , \sigma , \lambda_ {\pi})} \frac {1}{| \operatorname{Fixe} (P , \pi , \sigma , \lambda_ {\pi}) |} \frac {1}{| \sigma |} \\ q ^ {\deg (0) \frac {r - 1}{2} u ^ {\prime}} q ^ {\deg (\infty) \frac {r - 1}{2} s ^ {\prime}} \sum_ {1 \leq i, j \leq | P |} \left(z _ {1} \left(\pi_ {\infty} ^ {i}\right) ^ {- s ^ {\prime}} + \dots + z _ {r} \left(\pi_ {\infty} ^ {i}\right) ^ {- s ^ {\prime}}\right) \\ \left(z _ {1} \left(\pi_ {0} ^ {j}\right) ^ {u ^ {\prime}} + \dots + z _ {r} \left(\pi_ {0} ^ {j}\right) ^ {u ^ {\prime}}\right) \operatorname{tr} _ {\alpha} ^ {\leq p} \left(f _ {s ^ {\prime}, u ^ {\prime}} ^ {i, j}\right) _ {P, \pi , \sigma , \lambda_ {\pi}} \end{array}
$$

où

$$
\begin{array}{l}\operatorname{tr}_{\alpha}^{\leq p}\left(f_{s^{\prime},u^{\prime}}^{i,j}\right)_{P,\pi ,\sigma ,\lambda_{\pi}} = \int_{\operatorname{Im}\Lambda_{P_{\sigma}}}d\lambda_{\sigma}\cdot \sum_{\lambda_{\pi}^{\sigma}}\frac{\left(\left(\lambda_{\pi}^{\sigma}\right)^{j}\left(\lambda_{\sigma}\right)^{j_{\sigma}}\right)^{\deg(0)u^{\prime}}}{\left(\left(\lambda_{\pi}^{\sigma}\right)^{i}\left(\lambda_{\sigma}\right)^{i_{\sigma}}\right)^{\deg(\infty)s^{\prime}}}\\ \\ \lim_{\substack{\mu_{\sigma}\mapsto 1\\ \mu_{\sigma}\in \Lambda_{P_{\sigma}}}}\sum_{\tau \in \mathfrak{G}_{|P_{\sigma}|}}\widehat{\mathbb{1}}_{P_{\sigma},\tau}^{p - \alpha p_{\tau (P_{\sigma})}^{\tau (i_{\sigma})}}\big(\mu_{\sigma}\sigma \big(\lambda_{\pi}^{\sigma}\big) / \lambda_{\pi}^{\sigma}\sigma (\lambda_{\pi})\big)\\ \\ \operatorname{Tr}_{L^{2}(M_{P}(F)N_{P}(\mathbb{A})\backslash G(\mathbb{A}) / a^{\mathbb{Z}},\pi)}\left[\left(M_{P,\tau \sigma}^{\tau (P)}(\cdot ,\lambda_{\pi}^{\sigma}\lambda_{\sigma})\tau \sigma (\lambda_{\pi})\right)^{-1}\right.\\ \left. \circ M_{P,\tau}^{\tau (P)}(\cdot ,\lambda_{\pi}^{\sigma}\lambda_{\sigma} / \mu_{\sigma})\circ f(\cdot ,\lambda_{\pi}^{\sigma}\lambda_{\sigma} / \mu_{\sigma})\right]. \end{array}
$$

Commentaire : Les notations sont les mêmes que dans [Lafforgue, 1997]. En particulier, les$( P , \pi , \sigma , \lambda _ { \pi } )$sont des bons “quadruplets discrets” constitues de´

• une “paire discrète” (P, π) c’est-à-dire un sous-groupe parabolique standard P de${ \mathrm { G L } } _ { r }$et une representation automorphe discrète´$\pi =$ $( \pi ^ { 1 } , \ldots , \pi ^ { | P | } )$de$M _ { P } ( \mathbb { A } ) = \operatorname { G } \bar { \operatorname { L } } _ { r _ { 1 } } ( \mathbb { A } ) \times \cdot \cdot \cdot \times \operatorname { G } \operatorname { L } _ { r _ { | P | } } ( \mathbb { A } )$

• un fixateur$( \sigma , \lambda _ { \pi } )$de$( P , \pi ) \mathrm { ~ c ~ } ^ { \prime }$’est-à-dire une permutation$\sigma \in { \mathfrak { G } } _ { | P | }$de $\{ 1 , 2 , \dots , | P | \}$et un caractère$\lambda _ { P } \in \Lambda _ { P }$verifiant´$\sigma ( \pi \otimes \lambda _ { P } ) = \pi$

N’apparaissent que les$( P , \pi )$dont les facteurs$\pi ^ { 1 } , \ldots , \pi ^ { | P | }$sont non ramifies en dehors de´$T _ { f }$, si bien que les valeurs propres de Hecke$z _ { 1 } ( \pi _ { \infty } ^ { i } )$ $\dots , z _ { r _ { i } } ( \pi _ { \infty } ^ { i } ) \operatorname { e t } z _ { 1 } ( \pi _ { 0 } ^ { j } ) , \dots , z _ { r _ { j } } ( \pi _ { 0 } ^ { j } )$des composantes$\pi _ { \infty } ^ { i }$et$\pi _ { 0 } ^ { j }$des facteurs $\pi ^ { i }$et$\pi ^ { j }$en ∞ et 0 sont bien definies.´

Enfin, il a fallu rajouter dans la formule un facteur$\frac { 1 } { | \sigma | }$(où$| \sigma |$designe le´ produit des cardinaux des orbites de la permutation$\sigma )$qui manquait dans les enonc´ es des th´ eorèmes 11, 12 et´$_ { 1 2 } ,$du paragraphe VI.2f de [Lafforgue, 1997] : la faute se situe dans la demonstration du th´ eorème 11 à partir du´ lemme 9 du paragraphe VI.2e où on procède$\grave { \mathbf { a } }$un changement de variables d’integration qui induit en v´ erit´ e ce facteur´$\frac { 1 } { | \sigma | }$. (Mais cela$\mathrm { n } \ ' \mathrm { a }$pas d’importance pour la suite du livre).!"

## f) Forme des residus´

Nous allons preciser la forme des termes´$\mathrm { t r } _ { \alpha } ^ { \le p } ( f _ { s ^ { \prime } , u ^ { \prime } } ^ { i , j } ) _ { P , \pi , \sigma , \lambda _ { \pi } }$qui apparaissent dans l’expression du theorème I.9.´

Proposition I.10. – Fixons une fonction$f \in { \mathcal { H } } ^ { r } / a ^ { \mathbb { Z } }$, un entier$t \in \mathbb { Z } ,$un polygone$p : [ 0 , r ]  \mathbb { R }$, un reel´ α, un bon quadruplet discret$( P , \pi , \sigma , \lambda _ { \pi } )$ et deux indices$i , j \in \{ 1 , 2 , \dots , | P | \}$

Alors il existe un ensemble fini de constantes$c _ { \iota } ^ { \phantom { \dagger } }$, d’entiers$m _ { \iota } \geq 0$et de scalaires$\lambda _ { \iota }$tels que pour toutes places distinctes ∞,$0 \in | X | - T _ { f }$et tous entiers$s ^ { \prime } , u ^ { \prime } \geq 1$verifiant´ deg$( 0 ) \bar { u ^ { \prime } } - \deg ( \infty ) s ^ { \prime } = t ,$, on ait

$$
\operatorname{tr} _ {\alpha} ^ {\leq p} \left(f _ {s ^ {\prime}, u ^ {\prime}} ^ {i, j}\right) _ {P, \pi , \sigma , \lambda_ {\pi}} = \sum_ {\iota} c _ {\iota} (\deg (\infty) s ^ {\prime}) ^ {m _ {\iota}} \lambda_ {\iota} ^ {\deg (\infty) s ^ {\prime}}
$$

dès lors que$\mathrm { d e g } ( \infty ) s ^ { \prime }$ou$\mathrm { d e g } ( 0 ) u ^ { \prime }$est assez grand en fonction de t et du support de$f .$

Demonstration :´ Si$i _ { \sigma } = j _ { \sigma } , \mathrm { c } ^ { \prime }$est immediat. Dans le cas contraire, nous al-´ lons deplacer le contour d’int´ egration Im´$\Lambda _ { P _ { \sigma } }$dans l’operateur´$\int _ { \mathrm { I m } \Lambda _ { P \sigma } } d \lambda _ { \sigma } .$ de façon à faire tendre le quotient$( \lambda _ { \sigma } ) ^ { j _ { \sigma } } / ( \lambda _ { \sigma } ) ^ { i _ { \sigma } }$vers 0.

On sait que la fonction sur$\Lambda _ { P _ { \sigma } }$

$$
\begin{array}{l}\lambda_{\sigma}\mapsto R(\lambda_{\sigma}) = \lim_{\substack{\mu_{\sigma}\mapsto 1\\ \mu_{\sigma}\in \Lambda_{P_{\sigma}}}}\sum_{\tau \in \mathfrak{G}_{|P_{\sigma}|}}\widehat{\mathbb{1}}_{P_{\sigma},\tau}^{p - \alpha p^{\tau (i_{\sigma})}}\big(\mu_{\sigma}\sigma \big(\lambda_{\pi}^{\sigma}\big) / \lambda_{\pi}^{\sigma}\sigma \big(\lambda_{\pi}\big)\big)\\ \\ \mathrm{Tr}_{L^{2}(M_{P}(F)N_{P}(\mathbb{A})\setminus G(\mathbb{A}) / a^{\mathbb{Z}},\pi)}\left[ \left(M_{P,\tau \sigma}^{\tau (P)}\big(\cdot ,\lambda_{\pi}^{\sigma}\lambda_{\sigma}\right)\tau \sigma (\lambda_{\pi})\right)^{-1}\circ M_{P,\tau}^{\tau (P)}\big(\cdot ,\lambda_{\pi}^{\sigma}\lambda_{\sigma} / \mu_{\sigma}\big)\\ \circ f\big(\cdot ,\lambda_{\pi}^{\sigma}\lambda_{\sigma} / \mu_{\sigma}\big)\big] \end{array}
$$

est une fraction rationnelle dont les pôles sont supportes par des hyperplans´ de la forme

$$
\lambda_ {\sigma} ^ {k} / \lambda_ {\sigma} ^ {\ell} = \lambda \text {   avec   } k, \ell \in \{1, \dots , | P _ {\sigma} | \} \text {   et   } \lambda \in \mathbb {C} ^ {\times}.
$$

Si$\mathrm { d e g } ( \infty ) s ^ { \prime }$ou$\mathrm { d e g } ( 0 ) u ^ { \prime }$est assez grand, les residus à l’infini s’annulent´ et il ne reste plus que les residus à distance finie lesquels sont de la forme´

$$
\underset { \begin{array}{c} (\lambda_ {\sigma}) ^ {k | P _ {\sigma} | - 1} \\ (\lambda_ {\sigma}) ^ {\ell | P _ {\sigma} | - 1} \end{array} = \lambda_ {k | P _ {\sigma} | - 1}} {\text {Res}} \dots \underset { \begin{array}{c} (\lambda_ {\sigma}) ^ {k _ {1}} \\ (\lambda_ {\sigma}) ^ {\ell_ {1}} \end{array} = \lambda_ {1}} {\text {Res}} \left[ \frac {\left(\left(\lambda_ {\pi} ^ {\sigma}\right) ^ {j} (\lambda_ {\sigma}) ^ {j _ {\sigma}}\right) ^ {\deg (0) u ^ {\prime}}}{\left(\left(\lambda_ {\pi} ^ {\sigma}\right) ^ {i} (\lambda_ {\sigma}) ^ {i _ {\sigma}}\right) ^ {\deg (\infty) s ^ {\prime}}} R (\lambda_ {\sigma}) \right]
$$

où les notations$\mathrm { \Delta ^ { 6 6 } }$designent les op´ erateurs de r´ esidus le long d’hyper-´ plans$\begin{array} { r } { \frac { ( \lambda _ { \sigma } ) ^ { k _ { e } } } { ( \lambda _ { \sigma } ) ^ { \ell _ { e } } } = \lambda _ { e } , 1 \leq e < | P _ { \sigma } | } \end{array}$, qui se coupent proprement dans$\Lambda _ { P _ { \sigma } }$ (autrement dit, tels que les couples$( k _ { e } , \ell _ { e } ) , 1 \ \leq \ e \ < \ | P _ { \sigma } |$, fassent de l’ensemble d’indices$\{ 1 , 2 , \dots , | P _ { \sigma } | \}$un arbre connexe).

La proposition resulte alors du lemme suivant appliqu´ e´$| P _ { \sigma } | - 1$fois :

Lemme I.11. – Soient K un corps,$R ( z )$une fraction rationnelle à coefficients dans K et$z _ { 0 } \in K ^ { \times }$un pôle non nul d’ordre$m _ { 0 } \geq 1$de R. Alors la suite

$$
m _ {0} \leq n \mapsto \underset {z = z _ {0}} {\operatorname{Res}} R (z) z ^ {n} d z
$$

est une combinaison lineaire des suites´

$$
m _ {0} \leq n \mapsto n ^ {m} z _ {0} ^ {n}, 0 \leq m <   m _ {0}.
$$

Demonstration :´ Il suffit d’ecrire´$z ^ { n } = \sum _ { k = 0 } ^ { n } C _ { n } ^ { k } ( z - z _ { 0 } ) ^ { k } z _ { 0 } ^ { n - k }$et de remarquer que la forme$R ( z ) ( z - z _ { 0 } ) ^ { k } d z$n’a pas de pôle en$z _ { 0 }$et donc pas de residu si´ $k \geq m _ { 0 }$!"

## g) Allure des nombres de Lefschetz

On rappelle le resultat suivant :´

Theor´ eme I.12.\` – Pour toute representation automorphe discrète´ π d’un groupe lineaire ad´ elique´$\mathrm { G L } _ { n } ( \mathbb { A } ) , n \geq 1$, il existe des representations auto-´ morphes cuspidales$\hat { \pi ^ { 1 } } , \ldots , \pi ^ { k }$de groupes lineaires´$\mathbf { G L } _ { n _ { 1 } } ( \mathbb { A } ) , \dots , \mathbf { G L } _ { n _ { k } } ( \mathbb { A } )$ avec$n _ { 1 } + \cdots + n _ { k } = n$telles que, en toute place$x \in \left| X \right|$où π est non ramifiee, les´$\pi ^ { 1 } , \ldots , \pi ^ { k }$sont elles-mêmes non ramifiees et la famille des´ valeurs propres de Hecke

$$
z _ {1} (\pi_ {x}), \ldots , z _ {n} (\pi_ {x})
$$

est la reunion disjointe sur les´$i , 1 \le i \le k$, desfamilles de valeurs propres de Hecke

$$
z _ {1} \left(\pi_ {x} ^ {i}\right), \dots , z _ {n _ {i}} \left(\pi_ {x} ^ {i}\right).
$$

Demonstration´$\therefore { \bf { C } } ^ { \bf { \Theta } }$est une forme faible de la construction gen´ erale due´ à Langlands des spectres discrets par residus. On renvoie par exemple au´ theorème VI.2.2 de [Moeglin et Waldspurger, 1994].´

Dans leur article aux Annales de l’E.N.S., Moeglin et Waldspurger ont complètement determin´ e le spectre discret des groupes´$\mathrm { G L } _ { n }$, mais le resultat´ moins precis ci-dessus nous suffira.´!"

En combinant ce theorème avec le th´ eorème I.7, le th´ eorème I.9 et la´ proposition I.10, on obtient :

Theor´ eme I.13.\` – Fixons un niveau$N \hookrightarrow X ,$, une fonction$f \in \mathcal { H } _ { N } ^ { r } / a ^ { \mathbb { Z } }$et un entier$t \in \mathbb { Z }$

Notons {π}<sup>r</sup> l’ensemblefini des representations automorphes cuspidales´ de$\mathrm { G L } _ { r } ( \mathbb { A } ) = \mathbf { \mathcal { \ddot { G } } } ( \mathbb { A } )$qui apparaissent dans la decomposition spectrale de´ $L ^ { 2 } ( G ( F ) \backslash G ( \mathbb { A } ) / K _ { N } \cdot a ^ { \mathbb { Z } } )$

Soit$p : [ 0 , r ] \to \mathbb { R } _ { + }$un polygone de troncature assez convexe en fonction de N et du support de f et soit α un nombre reel.´

Alors il existe un ensemble fini de constantes$c _ { \iota } ,$, d’entiers$m _ { \iota } \ \geq \ 0 ,$ de scalaires$\lambda _ { \iota }$et de representations automorphes cuspidales´$\pi ^ { \iota } \ e t \ \pi ^ { \prime \iota }$de groupes lineaires ad´ eliques´$\mathrm { G L } _ { r _ { \iota } } ( \mathbb { A } )$et$\mathrm { G L } _ { r _ { i } ^ { \prime } } ( \mathbb { A } )$de rangs$r _ { \iota } , r _ { \iota } ^ { \prime } \ < \ r$tels qu’on ait laformule suivante :

Pour tous points$\overline { { \infty } } , \overline { { 0 } } \in X ( \overline { { \mathbb { F } } } _ { q } )$au-dessus de deux places distinctes $\infty , 0 \ \in \ | X | - T _ { f }$et pour tous entiers$s ^ { \prime } , u ^ { \prime } \geq 1$verifiant´$\deg ( 0 ) u ^ { \prime } -$ $\deg ( \infty ) s ^ { \prime } = t ,$, la moyenne de chacune des deux suites periodiques´

$$
n \mapsto \operatorname{Lef} _ {\operatorname{Frob} ^ {n} (\overline {{\infty}}), \overline {{0}}} ^ {r, \overline {{p}} _ {\alpha} \leq p} \left(f \times \operatorname{Frob} _ {\infty} ^ {\deg (\infty) s ^ {\prime}} \times \operatorname{Frob} _ {0} ^ {\deg (0) u ^ {\prime}}\right)
$$

$$
n \mapsto \operatorname{Lef} _ {\overline {{\infty}}, \operatorname{Frob} ^ {n} (\overline {{0}})} ^ {r, \overline {{p}} _ {\alpha} \leq p} \left(f \times \operatorname{Frob} _ {\infty} ^ {\deg (\infty) s ^ {\prime}} \times \operatorname{Frob} _ {0} ^ {\deg (0) u ^ {\prime}}\right)
$$

est egale à´

$$
\sum_ {\pi \in \{\pi \} _ {N} ^ {r}} \operatorname{Tr} _ {\pi} (f) q ^ {\deg (0) \frac {r - 1}{2} u ^ {\prime}} q ^ {\deg (\infty) \frac {r - 1}{2} s ^ {\prime}} \left(z _ {1} \left(\pi_ {\infty}\right) ^ {- s ^ {\prime}} + \dots + z _ {r} \left(\pi_ {\infty}\right) ^ {- s ^ {\prime}}\right)
$$

$$
\begin{array}{c} \left(z _ {1} (\pi_ {0}) ^ {u ^ {\prime}} + \dots + z _ {r} (\pi_ {0}) ^ {u ^ {\prime}}\right) \\ + \sum_ {\iota} c _ {\iota} (\deg (\infty) s ^ {\prime}) ^ {m _ {\iota}} \lambda_ {\iota} ^ {\deg (\infty) s ^ {\prime}} \big (z _ {1} \big (\pi_ {\infty} ^ {\prime \iota} \big) ^ {- s ^ {\prime}} + \dots + z _ {r _ {\iota} ^ {\prime}} \big (\pi_ {\infty} ^ {\prime \iota} \big) ^ {- s ^ {\prime}} \big) \end{array}
$$

$$
\left(z _ {1} \left(\pi_ {0} ^ {\iota}\right) ^ {u ^ {\prime}} + \dots + z _ {r _ {\iota}} \left(\pi_ {0} ^ {\iota}\right) ^ {u ^ {\prime}}\right)
$$

dès lors que deg(∞) et deg(0) sont assez grands (condition qui est vide si f est supportee par´$\mathbb { A } ^ { \times } \cdot \mathrm { G L } _ { r } ( O _ { \mathbb { A } } )$et si$t = 0 )$et que$\mathrm { d e g } ( \infty ) \bar { s ^ { \prime } }$ou$\mathrm { d e g } ( 0 ) u ^ { \prime }$ est assez grand enfonction du support de f et de t.

Remarque : La demonstration de la proposition I.10 un peu plus haut est´ semblable à celle du lemme 11 du paragraphe VI.3f de [Lafforgue, 1997]. Cela signifie en particulier que dans l’enonc´ e dudit lemme 11 on a oubli´ e´ d’eventuelles puissances de´$u = \deg ( \infty ) s ^ { \prime }$apparaissant en facteurs des exponentielles$\lambda ^ { u }$. Mais la suite du livre reste valable car, quand on fait la somme sur tous les bons quadruplets discrets à la page 325 (ou comme dans le theorème I.13 ci-dessus) et´$\mathrm { \ q u ^ { \prime } }$on identifie le resultat obtenu à´ une trace en cohomologie, on voit que necessairement tous les termes où´ apparaissent des puissances positives de deg$( \infty ) s ^ { \prime }$se simplifient les uns les autres. D’ailleurs, nous nous servirons plus loin de cet argument.

Notons aussi que lorsque$N = \emptyset { \mathrm { c } } ^ { \prime } { \mathrm { e s t - a - d i r e ~ q u ~ \ ' i l ~ n ~ ' y } }$a pas de niveau, on peut montrer que dans l’enonc´ e de la proposition I.10 et donc du th´ eorème´ I.13 tous les entiers$m _ { \iota }$valent 0 : on se sert de ce que les operateurs´ d’entrelacement de Langlands attaches à des repr´ esentations partout non´ ramifiees sont scalaires si bien´$\mathrm { \ q u ^ { \prime } }$on peut leur appliquer la “combinatoire des (G, M)-familles” d’Arthur.

Signalons d’autre part que dans la suite nous n’utiliserons le theorème´ I.13 ci-dessus qu’avec$t = 0 \operatorname { e t } \alpha = 0$(avec la notation$\overline { { p } } = \overline { { p } } _ { 0 } )$!"

## Chapitre II

## Complements quand le niveau comprend le z´ ero´

Dans le livre [Lafforgue, 1997] et comme rappele au chapitre I, nous avons´ compte les chtoucas munis d’une structure de niveau´ N en dehors de leur pôle et de leur zero. Mais nous verrons au chapitre III que lorsqu’on com-´ pactifie les champs$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p }$au-dessus de$( X - N ) \times ( X - N )$, on fait apparaître au bord des strates qui classifient des familles de chtoucas de rangs$< r .$, munis de structures de niveau N et dont les pôles et zeros peu-´ vent rencontrer N. Afin d’etudier la cohomologie de ces strates on est donc´ amene à compter aussi les chtoucas munis d’une structure de nivea´ u N et dont le zero (ou le pôle) est contenu dans´ N. C’est ce que nous allons faire dans ce chapitre, après avoir defini une première notion de structure de´ niveau (naïve) en le zero (ou le pôle) d’un chtouca.´

## 1) Chtoucas avec structures de niveau en le zero´

## a) Restriction des chtoucas à un niveau

On fixe toujours une courbe X projective, lisse et geom´ etriquement connexe´ sur un corps fini de base$\mathbb { F } _ { q }$et$r \geq 1$un entier.

On fixe aussi un niveau c’est-à-dire un sous-schema ferm´ e fini´$N =$ Spec$( { \mathcal { O } } _ { N } ) \hookrightarrow X$de la courbe X.

On note$\overline { { \mathcal { C } } } _ { \varnothing } ^ { r , N }$[resp.$r \overline { { \mathcal { C } } } _ { \varnothing } ^ { N } ]$le champ algebrique (au sens d’Artin) qui´ associe à tout schema´ S sur$\mathbb { F } _ { q }$le groupoïde des diagrammes

$$
\mathcal {F} \stackrel {j} {\rightarrow} \mathcal {F} ^ {\prime} \stackrel {t} {\leftarrow} ^ {\tau} \mathcal {F}
$$

$$
\left[ \text {resp.} \quad \mathcal {F} \stackrel {{t}} {{\leftarrow}} \mathcal {F} ^ {\prime} \stackrel {{j}} {{\rightarrow}} ^ {\tau} \mathcal {F} \right]
$$

où$\mathcal { F }$et${ \mathcal { F } } ^ { \prime }$sont deux$\mathcal { O } _ { N \times S ^ { - } } \mathrm { M o d u l e s }$localement libres de rang r, $\tau _ { \mathcal { F } }$designe´$( \mathrm { I d } _ { N } \times \mathrm { F r o b } _ { S } ) ^ { * } { \mathcal { F } }$et j, t sont deux homomorphismes dont les conoyaux admettent localement sur S un gen´ erateur comme´$\mathcal { O } _ { S ^ { - } } \mathbf { M }$odules.

En associant à tout chtouca à droite$( \mathcal { E } \hookrightarrow \mathcal { E } ^ { \prime } \smile \tau _ { \mathcal { E } } )$[resp. à gauche $( \mathcal { E } \longleftrightarrow \mathcal { E } ^ { \prime } \hookrightarrow \tau _ { \mathcal { E } ) } ]$de rang r sur un schema´ S le diagramme

$$
\mathcal {E} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N} \to \mathcal {E} ^ {\prime} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N} \leftarrow {} ^ {\tau} \mathcal {E} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N}
$$

$$
\left[ \text { resp. } \quad \mathcal {E} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N} \leftarrow \mathcal {E} ^ {\prime} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N} \rightarrow {} ^ {\tau} \mathcal {E} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N} \right],
$$

on definit un morphisme de champs alg´ ebriques´

$$
\begin{array}{c} \operatorname{Cht} ^ {r} \xrightarrow {\cdot \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N}} \overline {{\mathcal {C}}} _ {\emptyset} ^ {r, N} \\ \left[ \text {resp.} \quad {} ^ {r} \operatorname{Cht} \xrightarrow {\cdot \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N}} r \overline {{\mathcal {C}}} _ {\emptyset} ^ {N} \right] \end{array}
$$

qu’on appellera le morphisme de restriction des chtoucas de X à N.

On note$\mathbb { G } _ { m } ^ { N }$et$\mathbb { A } ^ { N }$les schemas d´ eduits du groupe multiplicatif´$\mathbb { G } _ { m }$et de la droite affine$\mathbb { A } ^ { 1 }$par restriction des scalaires à la Weil de$\mathcal { O } _ { N }$à$\mathbb { F } _ { q }$. Le champ quotient$\mathbb { G } _ { m } ^ { N } \backslash \mathbb { A } ^ { N }$associe à tout schema´ S (sur$\mathbb { F } _ { q } )$le groupoïde des $\mathcal { O } _ { N \times S ^ { - } } \mathrm { M o d u l e s }$inversibles sur$N \times S$qui sont munis d’une section globale.

En associant à tout diagramme$\mathcal { F } \stackrel { j } { \to } \mathcal { F } ^ { \prime } \stackrel { t } {  } \tau \mathcal { F } [ \mathrm { r e s p . } \mathcal { F } \stackrel { t } {  } \mathcal { F } ^ { \prime } \stackrel { j } { \to } \tau \mathcal { F } ]$ les determinants de´ j et t, on definit un morphisme de´$\bar { \mathcal { C } } _ { \varnothing } ^ { r , N } [ \mathrm { r e s p . } ^ { r \overline { { \mathcal { C } } } _ { \varnothing } ^ { N } ] }$dans $( \mathbb { G } _ { m } ^ { N } \backslash \mathbb { A } ^ { N } ) \times ( \mathbb { G } _ { m } ^ { N } \backslash \mathbb { A } ^ { N } )$

Par ailleurs, N plonge diagonalement dans´$X \times N$est un diviseur de Cartier et donc induit un morphisme

$$
X \to \mathbb {G} _ {m} ^ {N} \backslash \mathbb {A} ^ {N}
$$

qui est lisse de dimension relative 1.

Il est clair que les carres´

$$
\begin{array}{c c c} \operatorname{Cht} ^ {r} & \xrightarrow {\cdot \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N}} & \overline {{\mathcal {C}}} _ {\emptyset} ^ {r, N} \\ \Big \downarrow & & \Big \downarrow \\ X \times X & \longrightarrow & (\mathbb {G} _ {m} ^ {N} \backslash \mathbb {A} ^ {N}) \times (\mathbb {G} _ {m} ^ {N} \backslash \mathbb {A} ^ {N}) \\ ^ r \operatorname{Cht} & \xrightarrow {\cdot \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N}} & ^ r \overline {{\mathcal {C}}} _ {\emptyset} ^ {N} \\ \Big \downarrow & & \Big \downarrow \\ X \times X & \longrightarrow & (\mathbb {G} _ {m} ^ {N} \backslash \mathbb {A} ^ {N}) \times (\mathbb {G} _ {m} ^ {N} \backslash \mathbb {A} ^ {N}) \end{array}
$$

sont commutatifs.

Lemme II.1. – Pour tout entier$r \geq 1$, les morphismes

$$
\begin{array}{l} \text {Cht} ^ {r} \to \overline {{\mathcal {C}}} _ {\emptyset} ^ {r, N} \times_ {\left(\mathbb {G} _ {m} ^ {N} \backslash \mathbb {A} ^ {N}\right) \times \left(\mathbb {G} _ {m} ^ {N} \backslash \mathbb {A} ^ {N}\right)} (X \times X) \\ ^ {r} \text {Cht} \to {} ^ {r} \overline {{\mathcal {C}}} _ {\emptyset} ^ {N} \times_ {\left(\mathbb {G} _ {m} ^ {N} \backslash \mathbb {A} ^ {N}\right) \times \left(\mathbb {G} _ {m} ^ {N} \backslash \mathbb {A} ^ {N}\right)} (X \times X) \end{array}
$$

sont lisses de dimension relative$2 r - 2 .$

Demonstration :´ Comme les isomorphismes de passage aux duaux echan-´ gent$\mathbf { C h t } ^ { r } \to \overline { { \mathcal { C } } } _ { \varnothing } ^ { r , N }$et$\mathrm { T C h t } \to r \overline { { \mathcal { C } } } _ { \varnothing } ^ { N }$et preservent pôles et z´ eros des chtoucas,´ on peut se limiter au champ Cht<sup>r</sup> des chtoucas à droite.

Soit$\mathrm { H e } _ { N } ^ { r }$[resp.$\mathrm { H e } ^ { r } ]$le champ qui à tout schema ´ S sur$\mathbb { F } _ { q }$associe le groupoïde des diagrammes

$$
\mathcal {E} \stackrel {j} {\to} \mathcal {E} ^ {\prime} \stackrel {t} {\leftarrow} \widetilde {\mathcal {E}}
$$

où$\mathcal { E } , \mathcal { E } ^ { \prime } , \widetilde { \mathcal { E } }$sont trois${ \mathcal { O } } _ { N \times S ^ { - } } \mathbf { N }$odules [resp.${ \mathcal { O } } _ { X \times S ^ { - } } \mathbf { M o d u l e s } ]$localement libres de rang r sur$N \times S$[resp.$X \times S ]$et j, t sont deux homomorphismes dont les conoyaux admettent localement sur S un gen´ erateur comme´$\mathcal { O } _ { S ^ { - } }$ Modules [resp. deux plongements dont les conoyaux sont supportes par les´ graphes de deux morphismes$\infty , 0 \colon S \to X$et sont inversibles sur$\mathcal { O } _ { S } ]$

On remarque qu’ici encore on a un morphisme

$$
\mathrm{He} _ {N} ^ {r} \rightarrow \left(\mathbb {G} _ {m} ^ {N} \backslash \mathbb {A} ^ {N}\right) \times \left(\mathbb {G} _ {m} ^ {N} \backslash \mathbb {A} ^ {N}\right)
$$

defini par ´

$$
(\mathcal {E} \stackrel {{j}} {{\to}} \mathcal {E} ^ {\prime} \stackrel {{t}} {{\leftarrow}} \widetilde {\mathcal {E}}) \mapsto (\det j, \det t).
$$

Soit aussi$\mathrm { V e c } _ { N } ^ { r } \left[ \mathrm { r e s p . ~ V e c } _ { X } ^ { r } \right]$le champ qui à tout schema´ S sur$\mathbb { F } _ { q }$associe le groupoïde des$\mathcal { O } _ { N \times S ^ { - } } { \bf M }$odules [resp.$\mathcal { O } _ { X \times S ^ { - } } \mathbf { M o d u l e s } ]$localement libres de rang r sur$N \times S$[resp.$X \times S ]$

On a deux carres cart´ esiens :´

$$
\begin{array}{c c c} \operatorname{Cht} ^ {r} \longrightarrow & \operatorname{Vec} _ {X} ^ {r} & \overline {{\mathcal {C}}} _ {\emptyset} ^ {r, N} \longrightarrow \operatorname{Vec} _ {N} ^ {r} \\ \Big \downarrow & \Big \downarrow^ {(\text {Id,Frob})} & \Big \downarrow \qquad \Big \downarrow^ {(\text {Id,Frob})} \\ \operatorname{He} ^ {r} \longrightarrow & \operatorname{Vec} _ {X} ^ {r} \times \operatorname{Vec} _ {X} ^ {r} & \operatorname{He} _ {N} ^ {r} \longrightarrow \operatorname{Vec} _ {N} ^ {r} \times \operatorname{Vec} _ {N} ^ {r} \end{array}
$$

D’après la proposition 1 du paragraphe I.2 de [Lafforgue, 1997], il suffit de prouver :

Lemme II.2. – Pour tout entier$r \geq 1$, le morphisme representable´

$$
\mathrm{He} ^ {r} \rightarrow \left(\mathrm{He} _ {N} ^ {r} \times_ {\operatorname{Vec} _ {N} ^ {r}} \operatorname{Vec} _ {X} ^ {r}\right) \times_ {\left(\mathbb {G} _ {m} ^ {N} \backslash \mathbb {A} ^ {N}\right) \times \left(\mathbb {G} _ {m} ^ {N} \backslash \mathbb {A} ^ {N}\right)} (X \times X)
$$

est lisse de dimension relative$2 r - 2$

Demonstration :´ Les deux côtes´ etant lisses, il suffit de prouver que toutes´ les fibres geom´ etriques de ce morphisme sont non vides et lisses de dimen-´ sion$2 r - 2$

Soit donc (B$\stackrel { j } { \to } \mathcal { B } ^ { \prime } \stackrel { t } {  } \widetilde { \mathcal { B } } , \widetilde { \mathcal { E } } , \infty , 0 )$un point du champ

$$
\left(\operatorname{He} _ {N} ^ {r} \times_ {\operatorname{Vec} _ {N} ^ {r}} \operatorname{Vec} _ {X} ^ {r}\right) \times_ {\left(\mathbb {G} _ {m} ^ {N} \backslash \mathbb {A} ^ {N}\right) \times \left(\mathbb {G} _ {m} ^ {N} \backslash \mathbb {A} ^ {N}\right)} (X \times X)
$$

à valeurs dans un corps.

Si ∞ et 0 sont dans$X - N .$, on sait d’après le lemme 8 du paragraphe I.2 de [Lafforgue, 1997] que la fibre au-dessus de ce point est projective lisse de dimension$2 r - 2$

Si ∞ est dans$X - N$et 0 figure dans N avec une multiplicite´ egale à´ 1 [resp. plus grande que 1], cette fibre est representable par le produit de´ l’espace projectif$\mathbb { P } ( \mathcal { \tilde { E } } _ { \infty } )$de dimension$r { - } 1$(associe à la fibre´$\widetilde { \mathcal { E } } _ { \infty }$de$\widetilde { \mathcal E }$en ∞) et du groupe des automorphismes de$\mathcal { B } ^ { \prime }$ qui induisent l’identite sur Im´ t et dont le determinant est 1, lequel groupe est isomorphe à´$\mathrm { K e r } [ \mathbb { A } ^ { r - 1 } \rtimes \mathbb { G } _ { m } \to$ $\mathbb { G } _ { m } ] \cong \mathbb { A } ^ { r - 1 }$[resp. à Ker$\bar { \mathbb { A } } ^ { r } \xrightarrow { } \bar { \mathbb { A } } ^ { 1 } ] \cong \mathbb { A } ^ { r - 1 } ]$

De même, si 0 est dans$X - N$et ∞ figure dans N, cette fibre est representable par le produit de l’espace projectif´$\mathbb { P } ( \mathcal { \widetilde { E } } _ { 0 } ^ { \vee } )$de dimension$r - 1$ (associe au dual de la fibre´$\widetilde { \mathcal { E } } _ { 0 }$de$\widetilde { \mathcal E }$en 0) et du groupe des automorphismes  de B qui induisent l’identite sur Ker´ j et ont 1 pour determinant, lequel´ groupe est isomorphe à$\mathbb { A } ^ { r - 1 }$dans tous les cas.

Enfin, si$\infty$et 0 figurent tous deux dans N, cette fibre est representable´ par le produit de deux groupes isomorphes à$\mathbb { A } ^ { r - 1 }$

Ceci termine la demonstration du lemme II.2 et donc aussi du lemme II.1.´

## b) Choix d’un modèle

Fixons un point ferme 0 de la courbe´ X qui est supporte par le niveau´ $N = \mathrm { S p e c } ( { \bar { \mathcal { O } } } _ { N } ) \hookrightarrow X$

Le corps residuel´$\kappa ( 0 )$de 0 est une extension finie de$\mathbb { F } _ { q }$de dimension deg(0). Choisissant une uniformisante$\varpi _ { 0 }$en 0, l’anneau local complet´ e´$O _ { 0 }$ de X en 0 et son corps des fractions$F _ { 0 }$(qui est le complet´ e du corps des´ fonctions F de X en la place 0) sont isomorphes à$\kappa ( 0 ) [ [ \overline { { \varpi } } _ { 0 } ] ]$et$\kappa ( 0 ) ( ( \varpi _ { 0 } ) )$ respectivement. Si m designe la multiplicit´ e du point 0 dans le niveau´ N, celui-ci s’ecrit´$N = N ^ { \prime }$'$\bar { \mathrm { S p e c } } ( O _ { 0 } / \varpi _ { 0 } ^ { \hat { m } _ { 0 } } )$où$N ^ { \prime } \overset { \cdot } { = } \mathrm { S p e c } ( \mathcal { O } _ { N ^ { \prime } } )$est la partie de N supportee par le compl´ ementaire de 0.´

Considerons´$\widetilde { \mathcal F }$un point du champ$\overline { { \mathcal { C } } } _ { \varnothing } ^ { r , N }$à valeurs dans$\kappa ( 0 )$qui n’a pas de pôle mais a un zero en´$0 . \mathrm { { C } ^ { \prime } }$est un diagramme de$\mathcal { O } _ { N \otimes \kappa ( 0 ) }$-Modules libres de rang r

$$
\mathcal {F} \stackrel {\sim} {\to} \mathcal {F} ^ {\prime} \leftarrow^ {\tau} \mathcal {F},
$$

où$\tau _ { \mathcal { F } }$designe toujours´$( \mathrm { I d } _ { N } \times \mathrm { F r o b } _ { \kappa ( 0 ) } ) ^ { * } \mathcal { F } , \mathcal { F } \stackrel { \sim } {  } \mathcal { F } ^ { \prime }$est un isomorphisme et$\tau _ { \mathcal { F } }  \bar { \mathcal { F } } ^ { \prime }$un homomorphisme dont le conoyau est supporte par 0 et de´ dimension 1 sur$\kappa ( 0 )$

La partie$\widetilde { \mathcal { F } } ^ { \prime } = \widetilde { \mathcal { F } } \otimes _ { \mathcal { O } _ { N } } \mathcal { O } _ { N ^ { \prime } }$de$\widetilde { \mathcal F }$en dehors de 0 peut être identifiee au´ fibre trivial´$\mathcal { O } _ { N ^ { \prime } \otimes \kappa ( 0 ) } ^ { r }$ . Et il existe un entier$h _ { 0 } , 1 \leq h _ { 0 } \leq r$, tel que la partie $\widetilde { \mathcal { F } } _ { 0 } = \widetilde { \mathcal { F } } \otimes _ { \mathcal { O } _ { N } } O _ { 0 } / \varpi _ { 0 } ^ { m _ { 0 } }$concentree en 0 se d´ ecompose en une somme directe´

$$
\widetilde {\mathcal {F}} _ {0} = \widetilde {\mathcal {F}} _ {0} ^ {\mathrm{ét}} \oplus \widetilde {\mathcal {F}} _ {0} ^ {c},
$$

où$\mathcal { \widetilde { F } } _ { 0 } ^ { \mathrm { e t } }$s’identifie à$( O _ { 0 } / \varpi _ { 0 } ^ { m _ { 0 } } \otimes _ { \mathbb { F } _ { q } } \kappa ( 0 ) ) ^ { r - h _ { 0 } }$et$\widetilde { \mathcal { F } } _ { 0 } ^ { c } = ( ^ { \tau } \mathcal { F } _ { 0 } ^ { c }  \mathcal { F } _ { 0 } ^ { c } )$admet une base$n _ { 1 } , n _ { 2 } , \ldots , n _ { h _ { 0 } }$sur laquelle$\tau ^ { \mathrm { d e g ( 0 ) } }$agit par

$$
n _ {2} \mapsto n _ {1}, n _ {3} \mapsto n _ {2}, \dots , n _ {h _ {0}} \mapsto n _ {h _ {0} - 1}, n _ {1} \mapsto \varpi_ {0} n _ {h _ {0}}.
$$

Le schema en groupes Aut´$\widetilde { \mathcal F }$des automorphismes de$\widetilde { \mathcal F }$se decompose´ naturellement en produit

$$
\operatorname{Aut} \widetilde {\mathcal {F}} = \operatorname{Aut} \widetilde {\mathcal {F}} ^ {\prime} \times \operatorname{Aut} \widetilde {\mathcal {F}} _ {0} ^ {\text { ét }} \times \operatorname{Aut} \widetilde {\mathcal {F}} _ {0} ^ {c}
$$

avec Aut${ \widetilde { \mathcal { F } } } ^ { \prime }$et Aut$\mathcal { \widetilde { F } } _ { 0 } ^ { \mathrm { e t } }$des groupes discrets respectivement isomorphes à ${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N ^ { \prime } } )$et$\mathrm { G L } _ { r - h _ { 0 } } ( O _ { 0 } / \varpi _ { 0 } ^ { m _ { 0 } } )$. Le troisième facteur Aut$\mathcal { \widetilde { F } } _ { 0 } ^ { c }$a une composante neutre (Aut$\mathcal { \widetilde { F } } _ { 0 } ^ { c } ) ^ { \mathrm { c o n t } }$qui est une extension de$h _ { 0 }$groupes$\mathbb { A } _ { 1 }$(sauf un $\mathbb { G } _ { m }$si$m _ { 0 } = 1 )$.

Afin de decrire la partie discrète´$( \mathrm { A u t } \widetilde { \mathcal { F } } _ { 0 } ^ { c } ) ^ { \mathrm { d i s c } } = \mathrm { A u t } \widetilde { \mathcal { F } } _ { 0 } ^ { c } / ( \mathrm { A u t } \widetilde { \mathcal { F } } _ { 0 } ^ { c } )$cont de Aut$\mathcal { \widetilde { F } } _ { 0 } ^ { c }$, introduisons le$F _ { 0 }$-module de Dieudonne´$N _ { h _ { 0 } , 1 } = ( F _ { 0 } \widehat { \otimes } _ { \mathbb { F } _ { q } } \overline { { \mathbb { F } } } _ { q } ) ^ { h _ { 0 } }$ muni de la base canonique$n _ { 1 } , n _ { 2 } , \ldots , n _ { h _ { 0 } }$sur laquelle on fait agir$\dot { \tau } ^ { \mathrm { d e g ( 0 ) } }$ par

$$
n _ {2} \mapsto n _ {1}, n _ {3} \mapsto n _ {2}, \dots , n _ {h _ {0}} \mapsto n _ {h _ {0} - 1}, n _ {1} \mapsto \varpi_ {0} n _ {h _ {0}}.
$$

D’après Drinfeld (voir le theorème 6 du paragraphe III.1 de [Lafforgue,´ 1997]), il est irreductible de rang´$h _ { 0 }$et son algèbre des endomorphismes est une algèbre à division centrale simple$D _ { 0 }$de dimension$h _ { 0 } ^ { 2 }$sur$F _ { 0 }$et d’invariant$- \frac { 1 } { h _ { 0 } } \in \mathbb { Q } / \mathbb { Z }$

La valuation 0 sur le corps local complet$F _ { 0 }$se prolonge de manière unique à$D _ { 0 }$où elle definit un homomorphisme de groupes´

$$
0: D _ {0} - \{0 \} = D _ {0} ^ {\times} \to \frac {1}{h _ {0}} \mathbb {Z}
$$

dont le noyau$\mathcal { D } _ { 0 } ^ { \times }$est compact.

Pour tout$\begin{array} { r } { m \in \frac { 1 } { h _ { 0 } } \mathbb { Z } , m > 0 } \end{array}$, on peut definir le sous-groupe de´$\mathcal { D } _ { 0 } ^ { \times } = \mathcal { D } _ { 0 } ^ { \times 0 }$ d’indice fini

$$
\mathcal {D} _ {0} ^ {\times m} = \{\delta \in D _ {0} \mid 0 (1 - \delta) \geq m \}.
$$

On a :

Lemme II.3. – La partie discrète$( \mathrm { A u t } \widetilde { \mathcal { F } } _ { 0 } ^ { c } ) ^ { \mathrm { d i s c } } = \mathrm { A u t } \widetilde { \mathcal { F } } _ { 0 } ^ { c } / ( \mathrm { A u t } \widetilde { \mathcal { F } } _ { 0 } ^ { c } ) ^ { \mathrm { c o n t } } d i$u groupe Aut$\mathcal { \widetilde { F } } _ { 0 } ^ { c }$des automorphismes de$\mathcal { \widetilde { F } } _ { 0 } ^ { c }$ s’identifie au quotient $\mathcal { D } _ { 0 } ^ { \times } / \mathcal { D } _ { 0 } ^ { \times ( m _ { 0 } - 1 ) }$!"

## c) Structures de niveau naïves en le zero´

Sont toujours fixes un point 0 support´ e par le niveau´ N et un “modèle” c’est-à-dire un point$\widetilde { \mathcal { F } } = ( \mathcal { F } \widetilde { \right. } \mathcal { F } ^ { \prime } \left. { } ^ { \tau } \mathcal { F } )$du champ$\overline { { \mathcal { C } } } _ { \varnothing } ^ { r , N }$à valeurs dans $\kappa ( 0 )$qui n’a pas de pôle mais a un zero en 0.´

On rappelle que pour tout degre´$d \in \mathbb { Z }$et tout polygone convexe de troncature$\bar { p } : [ 0 , \bar { r } ] \overset { \cdot } {  } \mathbb { R } _ { + } , { \bf C h t } ^ { r , d , \overline { { p } } \leq p }$designe le champ alg´ ebrique au sens´ de Deligne-Mumford qui classifie les chtoucas de rang$r ,$de degre´$d$et dont le polygone canonique de Harder-Narasimhan$\overline { { p } }$est majore par´$p .$

Nous nous interessons au produit fibr ´ e :´

$$
\mathrm{Cht} ^ {r, d, \overline {{p}} \leq p} \times_ {\overline {{\mathcal {C}}} _ {\emptyset} ^ {r, N}} \widetilde {\mathcal {F}}.
$$

$\mathbf { C } '$est un champ algebrique au sens de Deligne-Mumford et de type fini ; il´ classifie les chtoucas$\widetilde { \mathcal E }$dans$\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p }$munis d’un isomorphisme${ \dot { \mathcal { E } } } \otimes \mathcal { O } _ { X } { \mathcal { O } } _ { N }$ $\cong \tilde { \mathcal { F } }$. De tels chtoucas$\widetilde { \mathcal E }$ont leur zero en 0 et leur pôle dans´$X - N$et, d’après le lemme II.1,$\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } \times _ { \overline { { \mathcal { C } } } _ { \varnothing } ^ { r , N } } \widetilde { \mathcal { F } }$est lisse sur$( X - N ) \otimes _ { \mathbb { F } _ { q } } \kappa ( 0 )$ De plus, ce champ est muni d’une action du groupe algebrique Aut´$\widetilde { \mathcal F }$des automorphismes de$\widetilde { \mathcal F }$

Au paragraphe prec´ edent on a introduit la composante neutre´ (Aut$\widetilde { \mathcal { F } } _ { 0 } )$cont du groupe algebrique Aut´$\widetilde { \mathcal F }$et on peut former le champ quotient

$$
\operatorname{Cht} _ {N, \widetilde {\mathcal {F}}} ^ {r, d, \overline {{p}} \leq p} = \big (\operatorname{Cht} ^ {r, d, \overline {{p}} \leq p} \times_ {\overline {{\mathcal {C}}} _ {\emptyset} ^ {r, N}} \widetilde {\mathcal {F}} \big) / (\operatorname{Aut} \widetilde {\mathcal {F}} _ {0}) ^ {\text { cont }}.
$$

Proposition II.4. – Le champ$\mathrm { C h t } _ { N , \widetilde { \mathcal { F } } } ^ { r , d , \overline { { p } } \le p }$est algebrique au sens de Deligne-´ Mumford, de type fini et lisse sur$( \ddot { X } - N ) \otimes _ { \mathbb { F } _ { q } } \kappa ( 0 )$

Il est muni d’une action du groupefini (Aut$\overset { \vartriangle } { \mathcal { F } } ) ^ { \mathrm { d i s c } } = \mathrm { A u t } \widetilde { \mathcal { F } } ^ { \prime } \times \mathrm { A u t } \widetilde { \mathcal { F } } _ { 0 } ^ { \acute { e } t } \times$ $\begin{array} { r } { \mathrm { ( A u t ~ \widetilde { \mathcal { F } } ^ { c } _ { 0 } ) ^ { d i s c } } = \mathrm { G L } _ { r } ( \mathcal { O } _ { N ^ { \prime } } ) \times \mathrm { G L } _ { r - h _ { 0 } } ( O _ { 0 } / \varpi _ { 0 } ^ { m _ { 0 } } ) \times ( \mathcal { D } _ { 0 } ^ { \times } / \mathcal { D } _ { 0 } ^ { \times ( m _ { 0 } - 1 ) } ) } \end{array}$

Enfin, le produit fibre´$\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } \times _ { \overline { { \mathfrak { C } } } _ { \varnothing } ^ { r , N } } \widetilde { \mathcal { F } }$est un torseur sous le groupe algebrique´ (Aut$\widetilde { \mathcal { F } } _ { 0 } ^ { c } ) ^ { \mathrm { c o n t } }$au-dessus de$\mathrm { C h t } _ { N , \widetilde { \mathcal { F } } } ^ { r , d , \overline { { p } } \leq p }$qui est localement trivial pour la topologie de Zariski.

Demonstration :´ Le groupe (Aut$\widetilde { \mathcal { F } } _ { 0 } ^ { c } ) ^ { \mathrm { c o n t } }$est une extension de groupes isomorphes à$\mathbb { A } ^ { 1 }$(ou eventuellement à´$\mathbb { G } _ { m }$si$m _ { 0 } = 1 )$donc tout torseur sous (Aut$\mathcal { \widetilde { F } } _ { 0 } ^ { c } ) ^ { \mathrm { c o n t } }$est localement trivial pour la topologie de Zariski.!"

Les champs$\mathrm { C h t } _ { N , \widetilde { \mathcal { F } } } ^ { r , d , \overline { { p } } \leq p }$peuvent être appeles champs de chtoucas avec´ structures de niveau naïves comprenant le zero. On qualifie ces structures´ de niveau de naïves car elles sont definies en fixant un “modèle” c’est-à-dire´ un point$\widetilde { \mathcal F }$de$\mathcal { C } _ { \varnothing } ^ { r , N }$alors que le champ$\overline { { \mathcal { C } } } _ { \varnothing } ^ { r , N }$, tout en etant connexe, compte´ plusieurs points sans pôle et avec un zero en 0.´

On note$\mathrm { C h t } _ { N , \widetilde { \mathcal { F } } } ^ { r , \overline { { p } } \leq p } = \coprod _ { d \in \mathbb { Z } } \mathrm { C h t } _ { N , \widetilde { \mathcal { F } } } ^ { r , d , \overline { { p } } \leq p }$. Il est muni d’une action de$\mathbb { A } ^ { \times } / F ^ { \times }$ et fixant comme au chapitre I un el´ ement´$a \in \mathbb { A } ^ { \times }$de degre non nul, on peut´ considerer le champ de type fini´

$$
\operatorname{Cht} _ {N, \widetilde {\mathcal {F}}} ^ {r, \overline {{p}} \leq p} / a ^ {\mathbb {Z}} \cong \coprod_ {1 \leq d \leq r | \deg (a) |} \operatorname{Cht} _ {N, \widetilde {\mathcal {F}}} ^ {r, d, \overline {{p}} \leq p}.
$$

Dans la suite, nous aurons besoin de contrôler la cohomologie -adique de la fibre des$\mathrm { C h t } _ { N , \widetilde { \mathcal { F } } } ^ { r , d , \overline { { p } } \leq p }$au-dessus du point gen´ erique de´$X - N$. Dans ce but, nous allons compter les points dans les fibres des$\mathbf { C h t } _ { N , \widetilde { \mathcal { F } } } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$au-dessus des points geom´ etriques de´$X - N$

Pour$\overline { { \infty } } \in ( X - N ) ( \overline { { \mathbb { F } } } _ { q } )$un point geom´ etrique de´$X - N$supporte par´ un point ferme´$\infty \in | X - \bar { N } | \operatorname { e t } s \geq 1$un multiple de deg(∞), considerons´ donc

$$
\operatorname{Lef} _ {N, \widetilde {\mathcal {F}}, \overline {{\infty}}} ^ {r, \overline {{p}} \leq p} (\text { Frob } ^ {s})
$$

le nombre de points fixes (comptes avec multiplicit´ es) de´$\mathrm { F r o b } ^ { s }$agissant sur la fibre$( \mathrm { C h t } _ { N , \mathcal { \widetilde { F } } } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } ) \times _ { ( X - N ) } \overline { { \infty } } .$

Il nous suffira de calculer ce nombre lorsque s est un multiple non seulement de deg(∞) mais aussi de$\mathrm { d e g } ( 0 ) h _ { 0 }$

## d) Expression integrale des nombres de Lefschetz´

On conserve toutes les notations des paragraphes prec´ edents et en particulier´ $m _ { 0 }$la multiplicite du z´ ero 0 dans le niveau´ N, l’entier$h _ { 0 } \in \{ 1 , \ldots , r \}$ determin´ e par le choix du modèle´$\widetilde { \mathcal F }$, le point ferme´$\infty \in | X - N |$supportant $\overline { { \infty } } \in ( X - N ) ( \overline { { \mathbb { F } } } _ { q } )$et$s \geq 1$un entier divisible à la fois par deg(∞) et $\mathrm { d e g } ( 0 ) h _ { 0 }$

On choisit${ \overline { { 0 } } } \in X ( { \overline { { \mathbb { F } } } } _ { q } )$un point geom´ etrique de´ X qui$\mathrm {  ~ s ~ } ^ { \prime }$envoie sur 0 ; ainsi les points geom´ etriques de´$( X - N ) \otimes _ { \mathbb { F } _ { q } } \kappa ( 0 )$au-dessus de$\overline { { \infty } } \in ( X - N ) ( \overline { { \mathbb { F } } } _ { q } )$ sont-ils les$( \overline { { \infty } } , \mathrm { F r o b } ^ { n } ( \overline { { 0 } } ) ) , 0 \leq n < \mathrm { d e g } ( 0 )$

La description adelique des chtoucas de z´ ero 0 et de pôle´ ∞ qui est faite dans le chapitre III de [Lafforgue, 1997] permet de donner pour$\mathrm { L e f } _ { N , \mathcal { \widetilde { F } } , \overline { { \infty } } } ^ { r , \overline { { p } } \leq p }$ une expression integrale semblable à celle de la proposition 2 du paragraphe´ III.6b de [Lafforgue, 1997].

L’expression de cette proposition doit être modifiee essentiellement en´ la place 0. Il faut restreindre la sommation sur les$\gamma$aux representants des´ classes de conjugaison d’el´ ements´ (s, s)-admissibles de${ \bar { \mathrm { G L } } } _ { r } ( F )$tels que $G _ { 0 } ^ { \tilde { 0 } } = \mathrm { G L } _ { r - h _ { 0 } } ( F _ { 0 } )$. L’integrale orbitale de la fonction´$f _ { 0 } ^ { \tilde { 0 } } = \mathbb { 1 } _ { \mathrm { G L } _ { r - h _ { 0 } } ( O _ { 0 } ) }$doit être remplacee par celle de la fonction caract´ eristique du sous-groupe de´ congruence$\mathrm { K e r } [ \mathrm { G L } _ { r - h _ { 0 } } ( O _ { 0 } )  \mathrm { G L } _ { r - h _ { 0 } } ( O _ { 0 } / \varpi _ { 0 } ^ { m _ { 0 } } ) ]$. Et la sommation sur les$\deg ( 0 ) m _ { \tilde { \sigma } } \ \in \ \deg ( 0 ) \mathbb { Z } \ \subset \ \mathbb { Z } \ = \ D _ { 0 } ^ { \times } / \mathcal { D } _ { 0 } ^ { \times }$doit être remplacee par une´ integrale orbitale sur les´$g _ { \tilde { 0 } } ^ { - 1 } \gamma g _ { \tilde { 0 } } , g _ { \tilde { 0 } } \in D _ { 0 } ^ { \times }$, de la fonction caracteristique´ du sous-groupe d’indice fini$\mathcal { D } _ { 0 } ^ { \times ( m _ { 0 } - 1 ) }$de$\mathcal { D } _ { 0 } ^ { \times }$decal´ e par multiplication par´ $\varpi _ { 0 } ^ { s / \deg ( 0 ) { \overline { { h } } _ { 0 } } }$

Dans la fonction de troncature qu’on a ecrite´

$$
\mathbb {1} \left(\overline {{p}} _ {\gamma , \alpha} ^ {(m _ {\tilde {\infty}}, g _ {\infty} ^ {\tilde {\infty}}, g ^ {\infty , 0}, g _ {0} ^ {\tilde {0}}, m _ {\tilde {0}})} \leq p\right)
$$

il faut alors remplacer la variable$m _ { \tilde { 0 } } \in \mathbb { Z } \mathrm { p a r } \frac { \deg ( g _ { \tilde { 0 } } ) } { \deg ( 0 ) } \in \frac { 1 } { \deg ( 0 ) } \mathbb { Z }$et poser $\alpha = 1$. On peut garder γ en indice car la filtration canonique de Harder-Narasimhan de tout chtouca fixe par Frob´ <sup>s</sup> est automatiquement respectee´ par le fixateur$\gamma$.

Enfin, il faut prendre pour$f ^ { \infty , 0 }$la fonction caracteristique du sous-´ groupe de congruence$\mathrm { K e r } [ \mathrm { G L } _ { r } ( O _ { \mathbb { A } ^ { \infty , 0 } } ) \to \mathrm { G L } _ { r } ( \mathcal { O } _ { N ^ { \prime } } ) ]$

Comme ici on n’a pas normalise les´$\mathrm { L e f } _ { N , \mathcal { F } , \overline { { \infty } } } ^ { r , \overline { { p } } \preceq p } ( \mathrm { F r o b } ^ { s } )$en les multipliant par les mesures de Haar des sous-groupes de congruence consider´ es, on´ obtient :

Proposition II.5. – Pour tout polygone convexe de troncature$p : [ 0 , r ]$ $\mathbb { R } _ { + }$, tout point geom´ etrique´$\vec { \infty } \in \dot { ( X - N ) } ( \overline { { \mathbb { F } } } _ { q } )$au-dessus d’un pointferme´ $\infty \in | X - N |$et tout multiple$s \geq 1$de deg(∞) et deg(0)h , on a

$$
\begin{array}{c} d g ^ {\infty , 0} \big (K _ {N ^ {\prime}} ^ {\infty , 0} \big) d g _ {0} ^ {\tilde {0}} \big (K _ {0, m _ {0}} ^ {\tilde {0}} \big) d g _ {\tilde {0}} \big (\mathcal {D} _ {0} ^ {\times (m _ {0} - 1)} \big) \operatorname{Lef} _ {N, \widetilde {\mathcal {F}}, \overline {{\infty}}} ^ {r, \overline {{p}} \leq p} (\text {Frob} ^ {s}) \\ = \sum_ {\gamma} \int_ {\Delta_ {\gamma} ^ {\times} a ^ {\mathbb {Z}} \backslash \left[ \mathbb {Z} \times G _ {\infty} ^ {\tilde {\infty}} \times G ^ {\infty , 0} \times G _ {0} ^ {\tilde {0}} \times D _ {0} ^ {\times} \right]} d m _ {\tilde {\infty}} \cdot d g _ {\infty} ^ {\tilde {\infty}} \cdot d g ^ {\infty , 0} \cdot d g _ {0} ^ {\tilde {0}} \cdot d g _ {\tilde {0}}. \\ \mathbb {1} _ {K _ {\infty} ^ {\tilde {\infty}}} \big ((g _ {\infty} ^ {\tilde {\infty}}) ^ {- 1} \gamma g _ {\infty} ^ {\tilde {\infty}} \big)   \mathbb {1} _ {K _ {N ^ {\prime}} ^ {\infty , 0}} \big ((g ^ {\infty , 0}) ^ {- 1} \gamma g ^ {\infty , 0} \big)   \mathbb {1} _ {K _ {0, m _ {0}} ^ {\tilde {0}}} \big ((g _ {0} ^ {\tilde {0}}) ^ {- 1} \gamma g _ {0} ^ {\tilde {0}} \big) \\ \mathbb {1} _ {\mathcal {D} _ {0} ^ {\times (m _ {0} - 1)}} \big (g _ {\tilde {0}} ^ {- 1} \gamma g _ {\tilde {0}} \varpi_ {0} ^ {- s / \deg (0) h _ {0}} \big)   \mathbb {1} \left(\overline {{p}} _ {\gamma} ^ {(m _ {\tilde {\infty}}, g _ {\infty} ^ {\tilde {\infty}}, g ^ {\infty , 0}, g _ {0} ^ {\tilde {0}}, \deg (g _ {\tilde {0}}))} \leq p\right) \end{array}
$$

où :

• γ decrit un ensemble de repr´ esentants des classes de conjugaison´ d’el´ ements´ (s, s)-admissibles (comme dans le theorème´ 5 duparagraphe III.4 de [[Lafforgue, 1997]) de$\mathrm { G L } _ { r } ( F )$dont le polynôme caracteristique´ $\chi _ { \gamma } a r - h _ { 0 }$racines de valuation 0 en 0 et$h _ { 0 }$racines de même valuation > 0 en 0 ;

$d m _ { \tilde { \infty } }$est la mesure de comptage sur$\mathbb { Z }$et$d g _ { \infty } ^ { \tilde { \infty } } , \ d g ^ { \infty , 0 } , \ d g _ { 0 } ^ { \tilde { 0 } } , \ d g _ { \tilde { 0 } }$sont les mesures de Haar sur$G _ { \infty } ^ { \tilde { \infty } } = \mathrm { G L } _ { r - h _ { \infty } } ( F _ { \infty } ) , G ^ { \infty , 0 } = \bar { \mathrm { G L } } _ { r } ( \mathbb { A } ^ { \infty , 0 } )$ $G _ { 0 } ^ { \tilde { 0 } } = \mathrm { G L } _ { r - h _ { 0 } } ( F _ { 0 } )$et$D _ { 0 } ^ { \times }$qui attribuent le volume 1 aux sous-groupes $K _ { \infty } ^ { \tilde { \infty } } = \mathrm { { G L } } _ { r - h _ { \infty } } ( O _ { \infty } ) , K ^ { \infty , 0 } = \mathrm { { G L } } _ { r } ( O _ { \mathbb { A } ^ { \infty , 0 } } ) , K _ { 0 } ^ { \tilde { 0 } } = \mathrm { { G L } } _ { r - h _ { 0 } } ( O _ { 0 } ) e t \mathcal { D } _ { 0 } ^ { \times } \ ,$ $\mathbb { 1 } _ { K _ { \infty } ^ { \tilde { \infty } , } } \mathbb { 1 } _ { K _ { N ^ { \prime } } ^ { \infty , 0 , 0 } } , \mathbb { 1 } _ { K _ { 0 , m _ { 0 } } ^ { \tilde { 0 } } } e t \mathbb { 1 } _ { \mathcal { D } _ { 0 } ^ { \times ( m _ { 0 } - 1 ) } }$designent les fonctions caract´ eristiques´ des sous-groupes$K _ { \infty } ^ { \tilde { \infty } , ~ K _ { N ^ { \prime } } ^ { \infty , 0 } } = \mathrm { K e r } [ K ^ { \infty , 0 } \to \mathrm { G L } _ { r } ( { \mathcal O } _ { N ^ { \prime } } ) ] , ~ K _ { 0 , m _ { 0 } } ^ { \tilde { 0 } } =$ $\mathrm { K e r } [ K _ { 0 } ^ { \tilde { 0 } } \to \mathbf { G } \mathbf { L } _ { r - h _ { 0 } } ( O _ { 0 } / \varpi _ { 0 } ^ { m _ { 0 } } ) ]$et$\mathcal { D } _ { 0 } ^ { \times ( m _ { 0 } - 1 ) }$

• la fonction de troncature 11$( \overline { { { p } } } _ { \gamma } ^ { ( m _ { \tilde { \infty } } , g _ { \infty } ^ { \tilde { \infty } } , g ^ { \infty , 0 } , g _ { 0 } ^ { 0 } , \deg ( g _ { \tilde { 0 } } ) ) } \ \leq \ p )$est egale à la´ fonction de troncature 11$( \overline { { p } } _ { \gamma , 1 } ^ { ( m _ { \tilde { \infty } } , g _ { \infty } ^ { \tilde { \infty } } , g ^ { \infty , 0 } , g _ { 0 } ^ { \tilde { 0 } } , \frac { \mathrm { d e g } ( g _ { \tilde { 0 } } ) } { \mathrm { d e g } ( 0 ) } ) } \le p )$explicitee dans´$l e$ paragraphe III.6a de [Lafforgue, 1997].!"

On rappelle qu’à tout el´ ement´$\gamma \in \operatorname { G L } _ { r } ( F )$qui est$( s , s )$)-admissible est associee une´ F-algèbre$\Delta = \Delta ^ { \prime } \times \Delta ^ { \prime \prime }$. On note$\Delta _ { \gamma }$la sous-algèbre des commutateurs de$\gamma$et$\Delta _ { \gamma } ^ { \times }$son groupe des el´ ements inversibles.´

La composante$\gamma ^ { \prime }$de$\gamma$dans$\Delta ^ { \prime }$est elliptique au sens que$F ^ { \prime } = F [ \gamma ^ { \prime } ]$ est un corps. Dans l’extension finie$F ^ { \prime }$de$F$il existe au-dessus des places $\infty$et 0 deux places uniques$\infty ^ { \prime }$et$0 ^ { \prime }$telles que$\infty ^ { \prime } ( \gamma ^ { \prime } ) \neq 0 , 0 ^ { \prime } ( \gamma ^ { \prime } ) \neq 0 ,$

Comme dans le paragraphe III.6 de [Lafforgue,$1 9 9 7 ]$, on a pu choisir chaque representant´$\gamma$de façon que les complet´ es´$F _ { \infty ^ { \prime } } ^ { \prime } \mathrm { e t } F _ { 0 ^ { \prime } } ^ { \prime }$soient plonges´ dans$M _ { h _ { \infty } } ( F _ { \infty } )$et$M _ { h _ { 0 } } ( F _ { 0 } )$; les images de$\gamma ^ { \prime }$dans$\check { \mathrm { G L } } _ { h _ { \infty } } ( \check { F } _ { \infty } )$et${ \mathrm { G L } } _ { h _ { 0 } } ( F _ { 0 } )$ sont notees´$\gamma _ { \infty ^ { \prime } } ^ { \prime }$et$\gamma _ { 0 ^ { \prime } } ^ { \prime }$

Proposition II.6. – Dans la situation de la proposition II.4, chacune des integrales´

$$
\int_ {\Delta_ {\gamma} ^ {\times} a ^ {\mathbb {Z}} \setminus \left[ \mathbb {Z} \times G _ {\infty} ^ {\tilde {\infty}} \times G ^ {\infty , 0} \times G _ {0} ^ {\tilde {0}} \times D _ {0} ^ {\times} \right]} d m _ {\tilde {\infty}} \cdot d g _ {\infty} ^ {\tilde {\infty}} \cdot d g ^ {\infty , 0} \cdot d g _ {0} ^ {\tilde {0}} \cdot d g _ {\tilde {0}} \cdot
$$

$$
\mathbb {1} _ {K _ {\infty} ^ {\tilde {\infty}}} \big (\big (g _ {\infty} ^ {\tilde {\infty}} \big) \gamma g _ {\infty} ^ {\tilde {\infty}} \big)   \mathbb {1} _ {K _ {N ^ {\prime}} ^ {\infty , 0}} \big (\big (g ^ {\infty , 0} \big) ^ {- 1} \gamma g ^ {\infty , 0} \big)   \mathbb {1} _ {K _ {0, m _ {0}} ^ {\tilde {0}}} \big (\big (g _ {0} ^ {\tilde {0}} \big) ^ {- 1} \gamma g _ {0} ^ {\tilde {0}} \big)
$$

$$
\mathbb {1} _ {\mathcal {D} _ {0} ^ {\times (m _ {0} - 1)}} \left(g _ {\tilde {0}} ^ {- 1} \gamma g _ {\tilde {0}} \varpi_ {0} ^ {- s / \deg (0) h _ {0}}\right) \mathbb {1} \left(\overline {{p}} _ {\gamma} ^ {(m _ {\tilde {\infty}}, g _ {\tilde {\infty}} ^ {\tilde {\infty}}, g ^ {\infty , 0}, g _ {0} ^ {\tilde {0}}, \deg (g _ {\tilde {0}}))} \leq p\right)
$$

ne peut être non nulle que si$0 ( \gamma _ { 0 } ^ { \prime } , \varpi _ { 0 } ^ { - s / \deg ( 0 ) h _ { 0 } } - 1 ) \geq m _ { 0 } - 1$quand$m _ { 0 } > 1$ [resp.$0 ( \gamma _ { 0 } ^ { \prime } , \varpi _ { 0 } ^ { - s / \deg ( 0 ) h _ { 0 } } ) = 0$quand$m _ { 0 } = 1 ]$

Et dans ce cas elle vaut

$$
\sum_ {1 \leq m _ {\infty^ {\prime}} \leq \frac {\deg (\infty^ {\prime})}{\deg (\infty)}} \mu_ {\infty} \mu_ {0} \int_ {\mathrm{GL} _ {r} (F) _ {\gamma} a ^ {\mathbb {Z}} \backslash \left[ G _ {\gamma \infty^ {\prime}} \times G _ {\infty} ^ {\infty^ {\prime}} \times G ^ {\infty , 0} \times G _ {0} ^ {0 ^ {\prime}} \times G _ {\gamma 0 ^ {\prime}} \right]} d g _ {\gamma \infty^ {\prime}} \cdot d g _ {\infty} ^ {\infty^ {\prime}} \cdot d g ^ {\infty , 0}.
$$

$$
1 \leq m _ {0 ^ {\prime}} \leq \frac {\deg (0 ^ {\prime})}{\deg (0)}
$$

$$
d g _ {0} ^ {0 ^ {\prime}} \cdot d g _ {\gamma 0 ^ {\prime}} \cdot \mathbb {1} _ {K _ {\infty} ^ {\infty^ {\prime}}} \big (\big (g _ {\infty} ^ {\infty^ {\prime}} \big) ^ {- 1} \gamma g _ {\infty} ^ {\infty^ {\prime}} \big) \mathbb {1} _ {K _ {N ^ {\prime}} ^ {\infty , 0}} \big (\big (g ^ {\infty , 0} \big) ^ {- 1} \gamma g ^ {\infty , 0} \big) \mathbb {1} _ {K _ {0, m _ {0}} ^ {\prime}} \big (\big (g _ {0} ^ {0 ^ {\prime}} \big) ^ {- 1} \gamma g _ {0} ^ {0 ^ {\prime}} \big)
$$

$$
\mathbb {1} \left(\overline {{p}} _ {\gamma} ^ {(m _ {\infty^ {\prime}} - \frac {\deg (\infty^ {\prime})}{\deg (\infty)} \infty^ {\prime} (\det g _ {\gamma \infty^ {\prime}}), g _ {\infty} ^ {\infty^ {\prime}}, g ^ {\infty , 0}, g _ {0} ^ {0 ^ {\prime}}, m _ {0 ^ {\prime}} + \frac {\deg (0 ^ {\prime})}{\deg (0)} 0 ^ {\prime} (\det g _ {\gamma 0 ^ {\prime}}))} \leq p\right)
$$

où :

$d g _ { \infty } ^ { \infty } , d g ^ { \infty , 0 } e t d g _ { 0 } ^ { 0 ^ { \prime } }$sont les mesures de Haar sur$G _ { \infty } ^ { \infty ^ { \prime } } = \mathrm { G L } _ { r - h _ { \infty } } ( F _ { \infty } )$ $G ^ { \infty , 0 } = \mathrm { G L } _ { r } ( \mathbb { A } ^ { \infty , 0 } )$et$G _ { 0 } ^ { 0 ^ { \prime } } = \mathrm { G L } _ { r - h _ { 0 } } ( F _ { 0 } )$qui attribuent le volume 1 aux sous-groupes ouverts compacts maximaux$K _ { \infty } ^ { \infty ^ { \prime } } = \mathrm { G L } _ { r - h _ { \infty } } ( O _ { \infty } )$ $K ^ { \infty , 0 } = \mathrm { G L } _ { r } ( O _ { \mathbb { A } ^ { \infty , 0 } } )$et$K _ { 0 } ^ { 0 ^ { \prime } } = \mathrm { G L } _ { r - h _ { 0 } } ( O _ { 0 } )$

$d g _ { \gamma \infty ^ { \prime } } e t d g _ { \gamma 0 ^ { \prime } }$sont les mesures de Haar sur les sous-groupes de commutateurs$\dot { G } _ { \gamma \infty ^ { \prime } } = \mathrm { G L } _ { h _ { \infty } } ( F _ { \infty } ) _ { \gamma _ { \infty ^ { \prime } } ^ { \prime } }$et$G _ { \gamma 0 ^ { \prime } } = \mathrm { G L } _ { h _ { 0 } } ( F _ { 0 } ) _ { \gamma _ { 0 ^ { \prime } } ^ { \prime } }$des el´ ements´ elliptiques$\gamma _ { \infty ^ { \prime } } ^ { \prime } e t \gamma _ { 0 ^ { \prime } } ^ { \prime }$qui attribuent le volume 1 aux sous-groupes ouverts compacts maximaux ;

${ \mathrm { G L } } _ { r } ( F ) _ { \gamma }$designe le sous-groupe de´$\mathrm { G L } _ { r } ( F )$des commutateurs de$l ^ { \prime } \acute { e } l \acute { e } { - }$ ment γ ;

$\mathbb { 1 } _ { K _ { \infty } ^ { \infty ^ { \prime } } } , \ \mathbb { 1 } _ { K _ { N ^ { \prime } } ^ { \infty , 0 } } \ e t \ \mathbb { 1 } _ { K _ { 0 , m _ { 0 } } ^ { 0 ^ { \prime } } }$sont les fonctions caracteristiques des sous-´ groupes$K _ { \infty } ^ { \infty ^ { \prime } } , K _ { N ^ { \prime } } ^ { \infty , 0 } = \mathrm { K e r } [ K ^ { \infty , 0 } \to \mathrm { G L } _ { r } ( { \mathcal O } _ { N ^ { \prime } } ) ] e t K _ { 0 , m _ { 0 } } ^ { 0 ^ { \prime } } = \mathrm { K e r } [ K _ { 0 } ^ { 0 ^ { \prime } } \to$ $\mathrm { G L } _ { r - h _ { 0 } } ( O _ { 0 } / \varpi _ { 0 } ^ { m _ { 0 } } ) ]$

• on a pose´

$$
\begin{array}{l} \mu_ {\infty} = (q ^ {\deg (\infty^ {\prime})} - 1) (q ^ {2 \deg (\infty^ {\prime})} - 1) \dots \big (q ^ {\left(\frac {h _ {\infty}}{[ F _ {\infty} ^ {\prime} : F _ {\infty} ]} - 1\right) \deg (\infty^ {\prime})} - 1 \big), \\ \mu_ {0} = (q ^ {\deg (0 ^ {\prime})} - 1) (q ^ {2 \deg (0 ^ {\prime})} - 1) \dots \big (q ^ {\left(\frac {h _ {0}}{[ F _ {0 ^ {\prime}} ^ {\prime} : F _ {0} ]} - 1\right) \deg (0 ^ {\prime})} - 1 \big). \end{array}
$$

Demonstration :´ Cela se prouve de la même façon que la proposition$^ 6$du paragraphe III.6b de [Lafforgue, 1997] une fois qu’on a remarque que´

$$
\mathbb {1} _ {\mathcal {D} _ {0} ^ {\times (m _ {0} - 1)}} \left(g _ {\tilde {0}} ^ {- 1} \gamma g _ {\tilde {0}} \varpi_ {0} ^ {- s / \deg (0) h _ {0}}\right) = 1
$$

si et seulement si

[resp.

$$
\begin{array}{l l} 0 \big (\gamma_ {0 ^ {\prime}} ^ {\prime} \varpi_ {0} ^ {- s / \deg (0) h _ {0}} - 1 \big) \geq m _ {0} - 1 & \text { quand } m _ {0} > 1 \\ 0 \big (\gamma_ {0 ^ {\prime}} ^ {\prime} \varpi_ {0} ^ {- s / \deg (0) h _ {0}} \big) = 0 & \text { quand } m _ {0} = 1 ] \end{array}
$$

comme il resulte de la caract´ erisation´

$$
\mathcal {D} _ {0} ^ {\times m} = \{\delta \in D _ {0} \mid 0 (1 - \delta) \geq m \} \text {   pour   } m > 0 \text {   et   }
$$

$$
\mathcal {D} _ {0} ^ {\times 0} = \mathcal {D} _ {0} ^ {\times} = \{\delta \in D _ {0} | 0 (\delta) = 0 \}.
$$

## 2) Calcul des nombres de Lefschetz et expression spectrale

## a) Fonctions de Kottwitz

Nous allons nous servir des resultats du chapitre 5 de [Laumon, 1996,´ volume I]. Dans le paragraphe 5.1 de ce chapitre est definie une “fonction´ d’Euler-Poincare”´

$$
\mathrm{GL} _ {h _ {0}} (F _ {0}) \to \mathbb {Q}
$$

qui est localement constante, invariante par$F _ { 0 } ^ { \times }$et à support compact modulo$F _ { 0 } ^ { \times }$. Ses principales propriet´ es sont donn´ ees dans le th´ eorème 5.1.3 (dû´ à Kottwitz pour les parties (i) et (iii) sur les integrales orbitales et à Laumon´ aide de Waldspurger pour la partie (ii) sur les termes constants´ ) que nous recopions en utilisant les notations propres à notre situation :

Theor´ eme II.7.\` – Il existe une fonction (dite d’Euler-Poincare ou de Kott-´ witz)

$$
f _ {0 ^ {\prime}}: \mathrm{GL} _ {h _ {0}} (F _ {0}) \to \mathbb {Q}
$$

localement constante, invariante par$F _ { 0 } ^ { \times }$et à support compact modulo$F _ { 0 } ^ { \times }$ et qui verifie les propri´ et´ es suivantes :´

(i) Pour tout el´ ement´$\gamma _ { 0 ^ { \prime } } ^ { \prime } \in \mathrm { G L } _ { h _ { 0 } } ( F _ { 0 } )$qui est elliptique c’est-à-dire tel que $F _ { 0 ^ { \prime } } ^ { \prime } = F _ { 0 } [ \gamma _ { 0 ^ { \prime } } ^ { \prime } ]$soit un corps (local complet, extension finie de$F _ { 0 } )$, on a

$$
\begin{array}{l} \int_ {G _ {\gamma 0 ^ {\prime} \setminus G _ {0 ^ {\prime}}}} \frac {d g _ {0 ^ {\prime}}}{d g _ {\gamma 0 ^ {\prime}}} \cdot f _ {0 ^ {\prime}} \big (g _ {0 ^ {\prime}} ^ {- 1} \gamma_ {0 ^ {\prime}} ^ {\prime} g _ {0 ^ {\prime}} \big) = \frac {\deg (0 ^ {\prime})}{h _ {0} \deg (0)} (- 1) ^ {\frac {h _ {0}}{\left[ F _ {0 ^ {\prime}} ^ {\prime} : F _ {0} \right]} - 1} \mu_ {0} \\ = \frac {1}{h _ {0}} (1 - q ^ {\deg (0 ^ {\prime})}) (1 - q ^ {2 \deg (0 ^ {\prime})}) \dots \big (1 - q ^ {\left(\frac {h _ {0}}{\left[ F _ {0 ^ {\prime}} ^ {\prime} : F _ {0} \right]} - 1\right) \deg (0 ^ {\prime})} \big) \frac {\deg (0 ^ {\prime})}{\deg (0)} \end{array}
$$

en notant dg 	 et$d g _ { \gamma 0 ^ { \prime } }$les mesures de Haar sur$\mathrm { { G L } } _ { h _ { 0 } } ( F _ { 0 } ) = G _ { 0 ^ { \prime } }$ et le sous-groupe$\mathrm { { G L } } _ { h _ { 0 } } ( F _ { 0 } ) _ { \gamma _ { 0 ^ { \prime } } ^ { \prime } } = G _ { \gamma 0 ^ { \prime } }$des commutateurs de$\gamma _ { 0 ^ { \prime } } ^ { \prime }$qui attribuent le volume 1 aux sous-groupes ouverts compacts maximaux.

(ii) Pour tout sous-groupe parabolique standard$P \subsetneq { \mathrm { G L } } _ { h _ { 0 } }$de sous-groupe de Levi´$M _ { P }$et de radical unipotent$N _ { P }$, on a

$$
\int_ {N _ {P} (F _ {0})} d n _ {0 ^ {\prime}} \cdot \int_ {K _ {0 ^ {\prime}}} d k _ {0 ^ {\prime}} \cdot f _ {0 ^ {\prime}} \left(k _ {0 ^ {\prime}} ^ {- 1} m _ {0 ^ {\prime}} n _ {0 ^ {\prime}} k _ {0 ^ {\prime}}\right) = 0, \forall m _ {0 ^ {\prime}} \in M _ {P} (F _ {0}),
$$

en notant dn 	 une mesure de Haar sur$N _ { P } ( F _ { 0 } )$et$d k _ { 0 ^ { \prime } }$la restriction à $K _ { 0 ^ { \prime } } = \mathrm { G L } _ { h _ { 0 } } ( O _ { 0 } )$de la mesure de Haar dg 	 sur$G _ { 0 ^ { \prime } } = \mathrm { G L } _ { h _ { 0 } } ( F _ { 0 } )$

(iii) Pour tout el´ ement´$\gamma _ { 0 ^ { \prime } } ^ { \prime } \in \mathrm { G L } _ { h _ { 0 } } ( F _ { 0 } )$qui n’est pas elliptique et si$d g _ { \gamma 0 ^ { \prime } }$ designe une mesure de Haar sur le groupe´$G _ { \gamma 0 ^ { \prime } } = \mathrm { G L } _ { h _ { 0 } } ( F _ { 0 } ) _ { \gamma _ { 0 ^ { \prime } } ^ { \prime } }$des commutateurs de$\gamma _ { 0 ^ { \prime } } ^ { \prime }$, on a

$$
\int_ {G _ {\gamma 0 ^ {\prime}} \backslash G _ {0 ^ {\prime}}} \frac {d g _ {0 ^ {\prime}}}{d g _ {\gamma 0 ^ {\prime}}} \cdot f _ {0 ^ {\prime}} \big (g _ {0 ^ {\prime}} ^ {- 1} \gamma_ {0 ^ {\prime}} ^ {\prime} g _ {0 ^ {\prime}} \big) = 0.
$$

Soit donc$f _ { 0 ^ { \prime } }$une telle fonction de Kottwitz. Quitte à la remplacer par la fonction

$$
\mathrm{GL} _ {h _ {0}} (F _ {0}) \ni g _ {0 ^ {\prime}} \mapsto \int_ {K _ {0 ^ {\prime}}} d k _ {0 ^ {\prime}} \cdot f _ {0 ^ {\prime}} \left(k _ {0 ^ {\prime}} ^ {- 1} g _ {0 ^ {\prime}} k _ {0 ^ {\prime}}\right),
$$

on peut la supposer invariante par conjugaison par$K _ { 0 ^ { \prime } } = \mathrm { G L } _ { h _ { 0 } } ( O _ { 0 } )$

Notant toujours$m _ { 0 } \geq 1$la multiplicite du point 0 dans le niveau´ N, on introduit la fonction produit

$$
\mathrm{GL} _ {h _ {0}} (F _ {0}) \ni g _ {0 ^ {\prime}} \mapsto f _ {0 ^ {\prime}, m _ {0}} (g _ {0 ^ {\prime}}) = f _ {0 ^ {\prime}} (g _ {0 ^ {\prime}}) \mathbb {1} _ {m _ {0}} (g _ {0 ^ {\prime}})
$$

où${ \mathbb l } _ { m _ { 0 } }$designe la fonction caract´ eristique du sous-ensemble des´ el´ ements´ de${ \mathrm { G L } } _ { h _ { 0 } } ( F _ { 0 } )$dont le polynôme caracteristique´$\chi _ { 0 ^ { \prime } }$verifie l’une des deux´ propriet´ es´ equivalentes suivantes :´

• toutes les racines$\gamma _ { 0 ^ { \prime } } ^ { \prime }$de$\chi _ { 0 ^ { \prime } }$satisfont

$$
0 (\gamma_ {0 ^ {\prime}} ^ {\prime} - 1) \geq m _ {0} - 1 \quad \text { quand } m _ {0} > 1
$$

$$
[ \text { resp. } \quad 0 (\gamma_ {0 ^ {\prime}} ^ {\prime}) = 0 \quad \text { quand } m _ {0} = 1 ],
$$

$$
\bullet \text {   on   a   } \chi_ {0 ^ {\prime}} (1 + T) = T ^ {h _ {0}} + \sum_ {0 \leq i <   h _ {0}} b _ {i} T ^ {i}
$$

$$
\operatorname{avec} 0 \left(b _ {i}\right) \geq \left(h _ {0} - i\right) \left(m _ {0} - 1\right), 0 \leq i <   h _ {0} \text {   quand   } m _ {0} > 1
$$

$$
[ \text { resp.   on   a } \chi_ {0 ^ {\prime}} (T) = T ^ {h _ {0}} + \sum_ {0 \leq i <   h _ {0}} a _ {i} T ^ {i}
$$

$$
\text { avec } 0 (a _ {i}) \geq 0, 0 <   i <   h _ {0}, e t 0 (a _ {0}) = 0 \text { quand } m _ {0} = 1 ].
$$

Du theorème II.7, on d´ eduit aussitôt :´

Corollaire II.8. – Lafonction$f _ { 0 ^ { \prime } , m _ { 0 } }$su$r \mathbf { G L } _ { h _ { 0 } } ( F _ { 0 } )$est localement constante, à support compact et invariante par conjugaison par$K _ { 0 ^ { \prime } } = \mathrm { G L } _ { h _ { 0 } } ( O _ { 0 } )$

Elle verifie les propri´ et´ es´ (ii) et (iii) du theorème´ II.7.

Enfin, pour$\gamma _ { 0 ^ { \prime } } ^ { \prime }$un el´ ement elliptique de´${ \mathrm { G L } } _ { h _ { 0 } } ( F _ { 0 } )$, l’integrale orbitale´ de$f _ { 0 ^ { \prime } , m _ { 0 } }$en$\gamma _ { 0 ^ { \prime } } ^ { \prime }$a la même valeur que dans le theorème´ II.7(i) si le polynôme caracteristique´$\chi _ { 0 ^ { \prime } }$de$\gamma _ { 0 ^ { \prime } } ^ { \prime }$verifie les conditions ci-dessus et elle est nulle´ sinon.!"

## b) Amplification à partir d’un sous-groupe de Levi´

On conserve toutes les notations du prec´ edent paragraphe.´

Procedant comme dans le paragraphe 10 de [Harris, Taylor], on d´ efinit´ pour tout multiple$s \geq 1$de$\mathrm { d e g } ( 0 ) h _ { 0 }$une fonction localement constante à support compact

$$
f _ {h _ {0}, m _ {0}} ^ {s}: \mathrm{GL} _ {r} (F _ {0}) \to \mathbb {Q}
$$

en specifiant de la manière suivante la valeur des´ el´ ements´$\gamma _ { 0 } \in \mathrm { G L } _ { r } ( F _ { 0 } )$

$\mathrm { S i l }$existe

$$
\begin{array}{l} k _ {0} \in K _ {0} = \mathrm{GL} _ {r} (O _ {0}), \\ \gamma_ {0} ^ {0 ^ {\prime}} \in K _ {0, m _ {0}} ^ {0 ^ {\prime}} = \mathrm{Ker} \big [ \mathrm{GL} _ {r - h _ {0}} (O _ {0}) \to \mathrm{GL} _ {r - h _ {0}} \left(O _ {0} / \varpi_ {0} ^ {m _ {0}}\right) \big ], \\ \gamma_ {0 ^ {\prime}} ^ {\prime} \in \mathrm{GL} _ {h _ {0}} (F _ {0}) \end{array}
$$

tels que$k _ { 0 } ^ { - 1 } \gamma _ { 0 } k _ { 0 } = ( \gamma _ { 0 } ^ { 0 ^ { \prime } } , \gamma _ { 0 ^ { \prime } } ^ { \prime } )$et$f _ { 0 ^ { \prime } , m _ { 0 } } ( \gamma _ { 0 ^ { \prime } } ^ { \prime } \varpi _ { 0 } ^ { - s / \deg ( 0 ) h _ { 0 } } ) \neq 0 .$, on pose

$$
f _ {h _ {0}, m _ {0}} ^ {s} (\gamma_ {0}) = f _ {0 ^ {\prime}, m _ {0}} \bigl (\gamma_ {0 ^ {\prime}} ^ {\prime} \varpi_ {0} ^ {- s / \deg (0) h _ {0}} \bigr)
$$

(definition qui ne d´ epend pas du choix de´$k _ { 0 } \in K _ { 0 } )$

• Dans tous les autres cas, on pose

$$
f _ {h _ {0}, m _ {0}} ^ {s} (\gamma_ {0}) = 0.
$$

Lemme II.9. – Il existe un sous-groupe ouvert (d’indice fini) de$K _ { 0 } \ =$ ${ \mathrm { G L } } _ { r } ( O _ { 0 } ) \subset { \mathrm { G L } } _ { r } ( F _ { 0 } )$, ne dependant que de la multiplicit´ e´$m _ { 0 } ,$, par lequel soient invariantes à droite et à gauche toutes les fonctions

$$
f _ {h _ {0}, m _ {0}} ^ {s}: \mathrm{GL} _ {r} (F _ {0}) \to \mathbb {Q}
$$

associees aux multiples´$s \geq 1$de$\mathrm { d e g } ( 0 ) h _ { 0 }$

Demonstration :´ Soit$\gamma _ { 0 }$un el´ ement du support d’une des fonctions´$f _ { h _ { 0 } , m _ { 0 } } ^ { s } .$ Il${ \bf s } '$agit de prouver que si$v , v ^ { \prime }$sont deux el´ ements d’un sous-groupe ouvert´ $V$de$K _ { 0 }$assez petit (independamment de´ s), alors$v \gamma _ { 0 } v ^ { \prime }$est encore dans le support de$f _ { h _ { 0 } , m _ { 0 } } ^ { s }$et même$f _ { h _ { 0 } , m _ { 0 } } ^ { s } ( v \gamma _ { 0 } v ^ { \prime } ) = f _ { h _ { 0 } , m _ { 0 } } ^ { s } ( \gamma _ { 0 } )$

Par definition des´$f _ { h _ { 0 } , m _ { 0 } } ^ { s }$, il existe$k _ { 0 } \in \mathrm { \Delta } K _ { 0 } = \mathrm { G L } _ { r } ( O _ { 0 } ) , \gamma _ { 0 } ^ { 0 ^ { \prime } } \in \mathrm { \Delta } K _ { 0 , m _ { 0 } } ^ { 0 ^ { \prime } } \ \subset$ $K _ { 0 } ^ { 0 ^ { \prime } } = \mathrm { G L } _ { r - h _ { 0 } } ( O _ { 0 } )$et un el´ ement´$\gamma _ { 0 ^ { \prime } } ^ { \prime }$du support compact de$f _ { 0 ^ { \prime } , m _ { 0 } }$dans ${ \mathrm { G L } } _ { h _ { 0 } } ( F _ { 0 } )$tels que$\gamma _ { 0 } = k _ { 0 } ( \gamma _ { 0 } ^ { 0 ^ { \prime } } , \varpi _ { 0 } ^ { s / \deg ( 0 ) h _ { 0 } } \gamma _ { 0 ^ { \prime } } ^ { \prime } ) k _ { 0 } ^ { - 1 }$

Le polynôme caracteristique´$\chi _ { 0 }$de γ s’ecrit´

$$
\chi_ {0} (T) = \chi_ {0} ^ {0 ^ {\prime}} (T) \varpi_ {0} ^ {s / \deg (0)} \chi_ {0 ^ {\prime}} \left(\varpi_ {0} ^ {- s / \deg (0) h _ {0}} T\right)
$$

avec$\chi _ { 0 } ^ { 0 ^ { \prime } }$et$\chi _ { 0 ^ { \prime } }$deux polynômes unitaires de degres´$r - h _ { 0 }$et$h _ { 0 }$dont les racines sont de valuation 0 (ou, ce qui est equivalent, dont les coefficients´ sont entiers et le coefficient constant entier inversible).

On voit d’autre part que les coefficients des matrices$\gamma _ { 0 }$et$\varpi _ { 0 } ^ { s / \deg ( 0 ) h _ { 0 } } \gamma _ { 0 } ^ { - 1 }$ restent dans un compact de$F _ { 0 }$independant de´ s. Il en est de même des coefficients de$v \gamma _ { 0 } v ^ { \prime }$et$\varpi _ { 0 } ^ { s / \deg ( 0 ) h _ { 0 } } ( v \gamma _ { 0 } v ^ { \prime } ) ^ { - 1 }$et pour V assez petit (independamment´ de s) ils sont arbitrairement proches de ceux de$\gamma _ { 0 }$et$\varpi _ { 0 } ^ { s / \deg ( 0 ) h _ { 0 } } \gamma _ { 0 } ^ { - 1 }$

Par consequent, le polynôme caract´ eristique´$\widetilde { \chi } _ { 0 }$de$v \gamma _ { 0 } v ^ { \prime } \ s ^ { \prime }$’ecrit lui aussi´ sous la forme

$$
\widetilde {\chi} _ {0} (T) = \widetilde {\chi} _ {0} ^ {0 ^ {\prime}} (T) \varpi_ {0} ^ {s / \deg (0)} \widetilde {\chi} _ {0 ^ {\prime}} \left(\varpi_ {0} ^ {- s / \deg (0) h _ {0}} T\right)
$$

avec$\widetilde { \chi } _ { 0 } ^ { 0 ^ { \prime } }$et$\widetilde \chi _ { 0 ^ { \prime } }$deux polynômes unitaires de degres´$r \mathrm { ~ - ~ } h _ { 0 }$et$h _ { 0 }$dont les  coefficients sont arbitrairement proches de ceux de$\chi _ { 0 } ^ { 0 ^ { \prime } }$et$\chi _ { 0 ^ { \prime } }$.

La matrice

$$
\varpi_ {0} ^ {s / \deg (0)} \widetilde {\chi} _ {0 ^ {\prime}} \left(\varpi_ {0} ^ {- s / \deg (0) h _ {0}} \left(v \gamma_ {0} v ^ {\prime}\right)\right)
$$

a des coefficients arbitrairement proches de ceux de

$$
\varpi_ {0} ^ {s / \deg (0)} \chi_ {0 ^ {\prime}} \left(\varpi_ {0} ^ {- s / \deg (0) h _ {0}} \gamma_ {0}\right)
$$

et elle a le même rang$r - h _ { 0 }$. Son noyau et son image sont arbitrairement proches de ceux de la seconde matrice.

Pour V assez petit (independamment de´ s), il existe donc un el´ ement´ $\widetilde { k } _ { 0 } \in { \cal K } _ { 0 } = \mathrm { G L } _ { r } ( { \cal O } _ { 0 } )$arbitrairement proche de$k _ { 0 }$et des el´ ements´$\widetilde { \gamma } _ { 0 } ^ { 0 ^ { \prime } } \in$ ${ \mathrm { G L } } _ { r - h _ { 0 } } ( F _ { 0 } )$et$\widetilde { \gamma } _ { 0 ^ { \prime } } ^ { \prime } \in \mathrm { G L } _ { h _ { 0 } } ( F _ { 0 } )$de polynômes caracteristiques´$\widetilde { \chi } _ { 0 ^ { \prime } } ^ { 0 }$et$\widetilde \chi _ { 0 ^ { \prime } }$tels que

$$
v \gamma_ {0} v ^ {\prime} = \widetilde {k} _ {0} \left(\widetilde {\gamma} _ {0} ^ {0 ^ {\prime}}, \varpi_ {0} ^ {s / \deg (0) h _ {0}} \widetilde {\gamma} _ {0 ^ {\prime}} ^ {\prime}\right) \widetilde {k} _ {0} ^ {- 1}.
$$

De plus,$\widetilde { \gamma } _ { 0 } ^ { 0 ^ { \prime } }$et$\widetilde { \gamma } _ { 0 ^ { \prime } } ^ { \prime }$   sont arbitrairement proches de$\gamma _ { 0 } ^ { 0 ^ { \prime } }$et$\gamma _ { 0 ^ { \prime } } ^ { \prime }$.

## c) Transfert

Comme dans les paragraphes prec´ edents, on a fix´ e le niveau´$N = \operatorname { S p e c } ( { \mathcal { O } } _ { N } )$ $\hookrightarrow X$et le point 0 de N de multiplicite´$m _ { 0 }$et on a note´$N ^ { \prime } = \mathrm { S p e c } ( \mathcal { O } _ { N ^ { \prime } } )$la partie de N en dehors de 0.

On considère un point ferme´$\infty \in | X - N |$en dehors du niveau N. Pour tout multiple$s \geq 1$de deg(∞) et$\mathrm { d e g } ( 0 ) h _ { 0 }$, on dispose de la fonction spherique de Drinfeld´

$$
f _ {\infty} ^ {- s ^ {\prime}}: \mathrm{GL} _ {r} (F _ {\infty}) \to \mathbb {Q}
$$

de niveau$\begin{array} { r } { - s ^ { \prime } = - \frac { s } { \deg ( \infty ) } } \end{array}$sur$\mathrm { G L } _ { r } ( F _ { \infty } )$(voir la definition 7 du paragraphe´ III.6c de [Lafforgue, 1997]). Elle est invariante des deux côtes par le sous-´ groupe ouvert compact maximal$K _ { \infty } = \mathrm { G L } _ { r } ( O _ { \infty } )$

Sur$\mathrm { G L } _ { r } ( \mathbb { A } ) = \mathrm { G L } _ { r } ( F _ { \infty } ) \times \mathrm { G L } _ { r } ( \mathbb { A } ^ { \infty , 0 } ) \times \mathrm { G L } _ { r } ( F _ { 0 } )$, on peut former la fonction localement constante à support compact

$$
f _ {\infty} ^ {- s ^ {\prime}} \otimes \mathbb {1} _ {K _ {N ^ {\prime}} ^ {\infty , 0}} \otimes f _ {h _ {0}, m _ {0}} ^ {s}: \mathrm{GL} _ {r} (\mathbb {A}) \to \mathbb {Q}  ,
$$

où$f _ { h _ { 0 } , m _ { 0 } } ^ { s } : \mathbf { G L } _ { r } ( F _ { 0 } ) \to \mathbb { Q }$est la fonction construite au paragraphe prec´ edent´ et$\mathbb { 1 } _ { K _ { N ^ { \prime } } ^ { \infty , 0 } }$designe la fonction caract´ eristique du sous-groupe de congruence´ $K _ { N ^ { \prime } } ^ { \infty , 0 } = \operatorname { K e r } [ K ^ { \infty , 0 } = \operatorname { G L } _ { r } ( O _ { \mathbb { A } ^ { \infty , 0 } } ) \to \operatorname { G L } _ { r } ( \mathscr { O } _ { N ^ { \prime } } ) ] \operatorname { d e } \operatorname { G L } _ { r } ( \mathbb { A } ^ { \infty , 0 } ) .$

D’après le lemme II.9, la fonction$f _ { \infty } ^ { - s ^ { \prime } } \otimes \mathbb { 1 } _ { K _ { N ^ { \prime } } ^ { \infty , 0 } } \otimes f _ { h _ { 0 } , m _ { 0 } } ^ { s }$est invariante à gauche et à droite par un sous-groupe ouvert (d’indice fini) de$K = \mathrm { G L } _ { r } ( O _ { \mathbb { A } } )$ qui ne depend pas de´ s mais seulement du niveau N.

Pour tout polygone convexe de troncature$p : [ 0 , r ] \to \mathbb { R } _ { + }$, on dispose alors de la trace tronquee d’Arthur´

$$
\operatorname{Tr} ^ {\leq p} \left(f _ {\infty} ^ {- s ^ {\prime}} \otimes 1 1 _ {K _ {N ^ {\prime}} ^ {\infty , 0}} \otimes f _ {h _ {0}, m _ {0}} ^ {s}\right).
$$

Comme les fonctions$f _ { \infty } ^ { - s ^ { \prime } } \otimes \mathbb { 1 } _ { K _ { N ^ { \prime } } ^ { \infty , 0 } } \otimes f _ { h _ { 0 } , m _ { 0 } } ^ { s }$contiennent en facteurs en la place$\infty$les fonctions spheriques de Drinfeld´$f _ { \infty } ^ { - s ^ { \prime } }$, on peut aussi definir à´ la façon du paragraphe I.2a des variantes des traces tronquees d’Arthur´

$$
\operatorname{Tr} _ {\alpha} ^ {\leq p} \left(f _ {\infty} ^ {- s ^ {\prime}} \otimes \mathbb {1} _ {K _ {N ^ {\prime}} ^ {\infty , 0}} \otimes f _ {h _ {0}, m _ {0}} ^ {s}\right)
$$

indexees par les´$\alpha \in \mathbb { R }$. Les fonctions sur R

$$
\alpha \mapsto \operatorname{Tr} _ {\alpha} ^ {\leq p} \left(f _ {\infty} ^ {- s ^ {\prime}} \otimes \mathbb {1} _ {K _ {N ^ {\prime}} ^ {\infty , 0}} \otimes f _ {h _ {0}, m _ {0}} ^ {s}\right)
$$

sont en escalier et periodiques de p´ eriode´ r!

Rappelant que$\widetilde { \mathcal F }$designe un “modèle” dans´$\overline { { \mathcal { C } } } _ { \varnothing } ^ { r , N }$sans pôle et avec zero´ en 0 et que$h _ { 0 }$est le rang de la partie non triviale$\mathcal { \widetilde { F } } _ { 0 } ^ { c }$de$\widetilde { \mathcal F }$en 0, nous pouvons maintenant enoncer :´

Theor´ eme II.10.\` – Pour toutpolygone de troncature$p : [ 0 , r ] \to \mathbb { R } _ { + }$assez convexe enfonction du niveau N, toutpoint geom´ etrique´$\overline { { \infty } } \in ( X - \dot { N } ) ( \overline { { \mathbb { F } } } _ { q } )$ au-dessus d’un pointferme´$\infty \in | X - N |$et tout multiple$s = \deg ( \infty ) s ^ { \prime }$de deg(∞) et deg(0)h , le nombre de Lefschetz

$$
\operatorname{Lef} _ {N, \mathcal {F}, \overline {{\infty}}} ^ {r, \overline {{p}} \leq p} (\text { Frob } ^ {s})
$$

multiplie par la constante´

$$
d g ^ {\infty , 0} \left(K _ {N ^ {\prime}} ^ {\infty , 0}\right) d g _ {0} ^ {\tilde {0}} \left(K _ {0, m _ {0}} ^ {\tilde {0}}\right) d g _ {\tilde {0}} \left(\mathcal {D} _ {0} ^ {\times (m _ {0} - 1)}\right) / h _ {0} \deg (0)
$$

est egal à la moyenne de la suite p´ eriodique´

$$
\mathbb {Z} \ni n \mapsto \operatorname{Tr} _ {n} ^ {\leq p} \left(f _ {\infty} ^ {- s ^ {\prime}} \otimes \mathbb {1} _ {K _ {N ^ {\prime}} ^ {\infty , 0}} \otimes f _ {h _ {0}, m _ {0}} ^ {s}\right).
$$

Demonstration :´ Ce theorème se prouve à partir des propositions II.5 et II.6´ exactement de la même façon que dans [Lafforgue, 1997] le theorème 1 du´ paragraphe V.2a à partir des propositions 2 et 6 du paragraphe III.6b.

On a besoin de deux types d’informations en chacune des places ∞ et 0 : d’une part des propriet´ es d’annulation de termes constants de façon´ à pouvoir appliquer le theorème 10 du paragraphe V.2d de [Lafforgue,´ 1997], et d’autre part des formules pour les integrales orbitales d’´ el´ ements´ elliptiques.

En la place ∞ rien n’est change et les propri´ et´ es voulues des fonctions´ spheriques de Drinfeld´$f _ { \infty } ^ { - s ^ { \prime } }$ont et´ e prouv´ ees dans [Lafforgue, 1997] à´ partir des lemmes 8 et 9 du paragraphe III.6c. En la place 0 les propriet´ es´ voulues des fonctions$f _ { h _ { 0 } , m _ { 0 } } ^ { s } : \mathrm { G L } _ { r } ( F _ { 0 } ) \to \mathbb { Q }$resultent du corollaire II.8´ <sup>0 0</sup>etant donn´ ee la manière dont elles ont´ et´ e construites au paragraphe II.2b´ ci-dessus à partir de la fonction$f _ { 0 ^ { \prime } , m _ { 0 } } : \mathbf { G L } _ { h _ { 0 } } ( F _ { 0 } ) \to \mathbb { Q }$

Dans l’enonc´ e du th´ eorème, on n’a besoin de prendre´ p assez convexe qu’en fonction de N seulement car toutes les$f _ { \infty } ^ { - s ^ { \prime } } \otimes \mathbb { 1 } _ { K _ { N ^ { \prime } } ^ { \infty , 0 } } \otimes f _ { h _ { 0 } , m _ { 0 } } ^ { s }$sont invariantes des deux côtes par un sous-groupe ouvert qui ne d´ epend que de´ N et pas de s.!"

## d) Forme de l’action des fonctions$f _ { h _ { 0 } , m _ { 0 } } ^ { s }$

Si P est un sous-groupe parabolique semi-standard de${ \mathrm { G L } } _ { r } .$on note$N _ { P }$son radical unipotent et$M _ { P } = M _ { P } ^ { 1 } \times \dots \times M _ { P } ^ { | P | } = \mathrm { G L } _ { r _ { 1 } } \times \dots \times \mathrm { G L } _ { r _ { | P | } }$son sous-groupe de Levi. On d´ esigne par´$\Lambda _ { P ( F _ { 0 } ) }$le tore complexe des caractères $M _ { P } ( F _ { 0 } ) \to \mathbb { C }$qui se factorisent à travers deg :$M _ { P } ( F _ { 0 } ) = M _ { P } ^ { 1 } ( F _ { 0 } ) \times \cdot \cdot \cdot \times$ $M _ { P } ^ { | P | } ( F _ { 0 } ) \to ( \deg ( 0 ) \mathbb { Z } ) ^ { | P | }$

Nous allons demontrer :´

Proposition II.11. – Soient P un sous-groupe parabolique semi-standard de$\bar { G } = \mathrm { G L } _ { r } e t \pi _ { 0 } = \pi _ { 0 } ^ { 1 } \times \cdot \cdot \cdot \times \pi _ { 0 } ^ { | P | }$une representation lisse admissible´ irreductible unitaire de´$\mathsf { \check { M } } _ { P } ( F _ { 0 } ) = \check { \mathrm { G L } } _ { r _ { 1 } } ( F _ { 0 } ) \times \cdots \times \mathrm { G L } _ { r _ { | P | } } ( F _ { 0 } )$

Alors l’action des fonctions$f _ { h _ { 0 } , m _ { 0 } } ^ { s } ~ ( p o u r s \ge 1$multiple assez grand de $\deg ( 0 ) h _ { 0 } )$sur les induites normalisees´

$$
\operatorname{Ind} _ {P (F _ {0})} ^ {G (F _ {0})} (\pi_ {0} \otimes \lambda_ {0}), \lambda_ {0} \in \Lambda_ {P (F _ {0})},
$$

est de laforme

$$
\sum_ {\iota = 1} ^ {\iota_ {0}} s ^ {m _ {\iota}} \chi_ {\iota} (\lambda_ {0}) ^ {s} R _ {\iota} (\lambda_ {0}) u _ {\iota}
$$

où les$u _ { \iota }$sont des operateurs de rangfini dans´ Ind$\begin{array} { c } { { G ( F _ { 0 } ) } } \\ { { P ( F _ { 0 } ) } } \end{array} ( \pi _ { 0 } )$, les$R _ { \iota } : \Lambda _ { { P ( F _ { 0 } ) } }$ $\begin{array} { r l } {  } & { { } \mathbb { C } } \end{array}$sont des fonctions rationnelles, les$\chi _ { \iota } : \Lambda _ { P ( F _ { 0 } ) } \to \mathbb { C } ^ { \times }$sont des fonctions monomiales et les$m _ { \iota }$sont des entiers ≥ 0.

Demonstration :´ Il existe un sous-groupe parabolique semi-standard$Q \subseteq P$ (avec donc$M _ { \mathcal { O } } \subseteq M _ { P } )$et une representation lisse admissible supercuspidale´ $\pi _ { 0 } ^ { \prime }$de$M _ { Q } ( F _ { 0 } )$tels que$\pi _ { 0 }$soit un sous-quotient de l’induite normalisee´ $\mathrm { I n d } _ { ( M _ { P } \cap \mathcal { Q } ) ( F _ { 0 } ) } ^ { M _ { P } ( F _ { 0 } ) } ( \pi _ { 0 } ^ { \prime } )$. Comme la forme donnee dans l’´ enonc´ e de la proposition´ est automatiquement preserv´ ee par passage à n’importe quel sous-quotient,´ on voit qu’on peut supposer$\pi _ { 0 } \stackrel { \cdot } { = } \bar { \pi _ { 0 } ^ { 1 } } \times \cdot \cdot \cdot \times \pi _ { 0 } ^ { | P | }$supercuspidale.

Afin de calculer l’action des fonctions$f _ { h _ { 0 } , m _ { 0 } } ^ { s }$sur les induites $\mathrm { I n d } _ { P ( F _ { 0 } ) } ^ { G ( F _ { 0 } ) } ( \pi _ { 0 } \otimes \lambda _ { 0 } )$, on procède comme dans la demonstration du lemme´ 7.5.7 de [Laumon, 1996, volume I].

On note W l’espace de la representation´$\pi _ { 0 }$et$\rho$l’action sur W qui definit´ π ; pour tout$\lambda _ { 0 } \in \Lambda _ { P ( F _ { 0 } ) }$, l’espace de la representation´$\pi _ { 0 } \otimes \lambda _ { 0 } \ : \mathrm { s } ^ { , }$identifie à W et l’action qui la definit est´$\lambda _ { 0 } \rho$

Soit alors V l’espace vectoriel des fonctions localement constantes

$$
v: K _ {0} = \mathrm{GL} _ {r} (O _ {0}) \to W
$$

telles que

$$
v \left(g _ {0} n _ {0} k _ {0}\right) = \rho \left(g _ {0}\right) \left(v \left(k _ {0}\right)\right), \forall g _ {0} \in M _ {P} \left(O _ {0}\right), \forall n _ {0} \in N _ {P} \left(O _ {0}\right), \forall k _ {0} \in K _ {0}.
$$

Pour tout$\lambda _ { 0 } \in \Lambda _ { P ( F _ { 0 } ) }$, l’espace de la representation´$\mathrm { I n d } _ { P ( F _ { 0 } ) } ^ { G ( F _ { 0 } ) } ( \pi _ { 0 } \otimes \lambda _ { 0 } )$ s’identifie à V et l’action des fonctions$f _ { h _ { 0 } , m _ { 0 } } ^ { s }$est donnee par´

$$
v \mapsto \left(K _ {0} \ni k _ {0} \mapsto \int_ {K _ {0}} (\lambda_ {0} \rho) \bigl (\psi_ {k _ {0}, k _ {0} ^ {\prime}} ^ {s} \bigr) \bigl (v \bigl (k _ {0} ^ {\prime} \bigr) \bigr) \cdot d k _ {0} ^ {\prime}\right)
$$

où les$\psi _ { k _ { 0 } , k _ { 0 } ^ { \prime } } ^ { s }$sont les fonctions sur$M _ { P } ( F _ { 0 } )$definies par´

$$
\psi_ {k _ {0}, k _ {0} ^ {\prime}} ^ {s} (g _ {0}) = \rho_ {P (F _ {0})} (g _ {0}) \int_ {N _ {P} (F _ {0})} d n _ {0} \cdot f _ {h _ {0}, m _ {0}} ^ {s} \bigl (k _ {0} ^ {- 1} g _ {0} n _ {0} k _ {0} ^ {\prime} \bigr);
$$

ici,$d k _ { 0 } ^ { \prime }$est la mesure de Haar de volume 1 sur$K _ { 0 } = \mathrm { G L } _ { r } ( O _ { 0 } )$, dn est la mesure de Haar sur$N _ { P } ( F _ { 0 } )$qui attribue le volume 1 à$N _ { P } ( O _ { 0 } )$et$\rho _ { P ( F _ { 0 } ) }$ designe la racine carr´ ee du caractère modulaire de´$P ( F _ { 0 } )$

D’après le lemme II.9, il existe un entier$m _ { 0 } ^ { \prime } \geq 1$ne dependant que de´ la multiplicite´$m _ { 0 }$de 0 dans N tel que toutes les fonctions$f _ { h _ { 0 } , m _ { 0 } } ^ { s }$soient invariantes à gauche et à droite par le sous-groupe de congruence${ \breve { K } } _ { 0 , m _ { 0 } ^ { \prime } } =$ Ker[$K _ { 0 } = \mathrm { G L } _ { r } ( O _ { 0 } )  \mathrm { G L } _ { r } ( O _ { 0 } / \varpi _ { 0 } ^ { m _ { 0 } ^ { \prime } } ) ]$. Comme$K _ { 0 , m _ { 0 } ^ { \prime } }$est distingue dans´ $K _ { 0 }$, toutes les fonctions

$$
M _ {P} (F _ {0}) \ni g _ {0} \mapsto \psi_ {k _ {0}, k _ {0} ^ {\prime}} ^ {s} (g _ {0})
$$

sont invariantes à gauche et à droite par$K _ { 0 , m _ { 0 } ^ { \prime } } \cap M _ { P } ( O _ { 0 } )$

Or on sait que les pseudo-coefficients des representations supercuspi-´ dales des groupes${ \mathrm { G L } } _ { r ^ { \prime } } ^ { - } ( F _ { 0 } )$sont à support compact modulo le centre$\bar { F } _ { 0 } ^ { \times }$ $\mathbf { C } '$est en particulier le cas pour les facteurs$\pi _ { 0 } ^ { 1 } , \ldots , \pi _ { 0 } ^ { | P | }$de la representation´ $\pi _ { 0 }$de$\bar { M _ { P } } ( F _ { 0 } ) = \mathrm { G L } _ { r _ { 1 } } ( F _ { 0 } ) \times \cdot \cdot \cdot \times \mathrm { G L } _ { r _ { | P | } } ( \check { F } _ { 0 } )$

Par consequent, il existe des parties compactes´$S _ { 1 } , \ldots , S _ { | P | } \operatorname* { d e } \operatorname { G L } _ { r _ { 1 } } ( F _ { 0 } )$ $\dots , \mathrm { G L } _ { r _ { | P | } } ( F _ { 0 } )$, stables à gauche et à droite par$\mathrm { G L } _ { r _ { 1 } } ( O _ { 0 } ) , \dots , \bar { \mathrm { G L } } _ { r _ { | P | } } ( O _ { 0 } )$ telles que si$\mathbb { 1 } _ { \mathcal { W } _ { 0 } ^ { \mathbb { Z } } S _ { 1 } \times \cdots \times \mathcal { W } _ { 0 } ^ { \mathbb { Z } } S _ { | P | } }$designe la fonction caract´ eristique de´$\varpi _ { 0 } ^ { \mathbb { Z } } S _ { 1 } \times$ $\cdots \times \varpi _ { 0 } ^ { \mathbb { Z } } S _ { | P | }$dans$\mathrm { G L } _ { r _ { 1 } } ( F _ { 0 } ) \times \cdot \cdot \cdot \times \mathrm { G L } _ { r _ { | P | } } ( F _ { 0 } )$, on ait les egalit´ es´

$$
(\lambda_ {0} \rho) \big (\psi_ {k _ {0}, k _ {0} ^ {\prime}} ^ {s} \big) = (\lambda_ {0} \rho) \big (\psi_ {k _ {0}, k _ {0} ^ {\prime}} ^ {s} \mathbb {1} _ {\varpi_ {0} ^ {\mathbb {Z}} S _ {1} \times \dots \times \varpi_ {0} ^ {\mathbb {Z}} S _ {| P |}} \big)
$$

entre operateurs de l’espace´ W des representations´$\pi _ { 0 } \otimes \lambda _ { 0 } , \lambda _ { 0 } \in \Lambda _ { P ( F _ { 0 } ) }$. On peut supposer que tous les el´ ements´$g _ { 1 } , \ldots , g _ { | P | } \mathrm { d e } S _ { 1 } { \subset } \mathrm { G L } _ { r _ { 1 } } ( F _ { 0 } ) , \ldots , S _ { | P | }$ $\subset \mathrm { ~ G L } _ { r _ { | P | } } ( F _ { 0 } )$sont à coefficients entiers et que leurs valuations$0 ( g _ { 1 } )$ $\ldots , 0 ( \dot { g _ { | P | } } ) \ ( \mathrm { c " e s t - a - d i r e }$les plus petites valuations de leurs coefficients dans$O _ { 0 } )$valent 0.

La proposition II.11 resulte du lemme suivant :´

Lemme II.12. – Soient$g _ { 1 } ^ { 0 } , \ldots , g _ { | P | } ^ { 0 }$des el´ ements de´$S _ { 1 } , \ldots , S _ { | P | }$et$k _ { 0 } , k _ { 0 } ^ { \prime }$ deux el´ ements de´$K _ { 0 } = \mathrm { G L } _ { r } ( O _ { 0 } )$

On considère l’expression

$$
\psi_ {k _ {0}, k _ {0} ^ {\prime}} ^ {s} \left(\varpi_ {0} ^ {d _ {1}} g _ {1} ^ {0}, \dots , \varpi_ {0} ^ {d _ {| P |}} g _ {| P |} ^ {0}\right)
$$

comme fonction du multiple$s ~ = ~ \deg ( 0 ) h _ { 0 } s ^ { \prime }$de$\mathrm { d e g } ( 0 ) h _ { 0 }$et d’entiers $d _ { 1 } , \dotsc , d _ { | P | } \in \mathbb { Z }$

Alors il existe un ensemble fini d’inegalit´ es de laforme´

$$
c _ {1} d _ {1} + c _ {2} d _ {2} + \dots + c _ {| P |} d _ {| P |} + c ^ {\prime} s ^ {\prime} + c \geq 0
$$

(où$c _ { 1 } , c _ { 2 } , \ldots , c _ { | P | } , c , c ^ { \prime }$sont des entiers fixes´ ) telles que dans chacune des parties du reseau des´$( d _ { 1 } , \ldots , d _ { | P | } , s ^ { \prime } )$definies en demandant que chacune´ de ces inegalit´ es soit v´ erifi´ ee ou ne le soit pas, l’expression´

$$
\psi_ {k _ {0}, k _ {0} ^ {\prime}} ^ {s} \big (\varpi_ {0} ^ {d _ {1}} g _ {1} ^ {0}, \dots , \varpi_ {0} ^ {d _ {| P |}} g _ {| P |} ^ {0} \big)
$$

s’ecrive´

$$
\sum_ {\iota} c _ {\iota} d _ {1} ^ {m _ {1, \iota}} \dots d _ {| P |} ^ {m _ {| P |, \iota}} s ^ {\prime m _ {\iota}} q _ {1, \iota} ^ {d _ {1}} \dots q _ {| P |, \iota} ^ {d _ {| P |}} q _ {\iota} ^ {s ^ {\prime}}
$$

où les$m _ { 1 , \iota } , \ldots , m _ { | P | , \iota } , m _ { \iota }$sont des entiers fixes et les´$c _ { \iota } , q _ { 1 , \iota } , \dots , q _ { | P | , \iota } , q _ { \iota }$ sont des constantes.

En particulier, pour que$\psi _ { k _ { 0 } , k _ { 0 } ^ { \prime } } ^ { s } ( \varpi _ { 0 } ^ { d _ { 1 } } g _ { 1 } ^ { 0 } , \ldots , \varpi _ { 0 } ^ { d _ { | P | } } g _ { | P | } ^ { 0 } ) \neq 0 ,$, il faut

$$
0 \leq d _ {1} \leq s ^ {\prime}, \dots , 0 \leq d _ {| P |} \leq s ^ {\prime}.
$$

Demonstration du lemme II.12 :´ Il s’agit de comprendre la dependance des´ integrales´

$$
\int_ {N _ {P} (F _ {0})} d n _ {0} \cdot f _ {h _ {0}, m _ {0}} ^ {s} \left(k _ {0} ^ {- 1} \left(\varpi_ {0} ^ {d _ {1}} g _ {1} ^ {0}, \dots , \varpi_ {0} ^ {d _ {| P |}} g _ {| P |} ^ {0}\right) n _ {0} k _ {0} ^ {\prime}\right)
$$

en$s = \deg ( 0 ) h _ { 0 } s ^ { \prime }$et$d _ { 1 } , \dotsc , d _ { | P | }$

Il existe un entier$m \geq 1$tel que si$g _ { 1 } \in M _ { r _ { 1 } } ( O _ { 0 } ) , \ldots , g _ { | P | } \in M _ { r _ { | P | } } ( O _ { 0 } )$ verifient´

$$
g _ {1} \equiv g _ {1} ^ {0}, \dots , g _ {| P |} \equiv g _ {| P |} ^ {0} \mod \text { modulo } \varpi_ {0} ^ {m},
$$

alors$g _ { 1 } , \ldots , g _ { | P | }$sont dans$S _ { 1 } , \ldots , S _ { | P | }$et on a toujours

$$
\begin{array}{l} \int_ {N _ {P} (F _ {0})} f _ {h _ {0}, m _ {0}} ^ {s} \big (k _ {0} ^ {- 1} \big (\varpi_ {0} ^ {d _ {1}} g _ {1}, \ldots , \varpi_ {0} ^ {d _ {| P |}} g _ {| P |} \big) n _ {0} k _ {0} ^ {\prime} \big) \cdot d n _ {0} \\ = \int_ {N _ {P} (F _ {0})} f _ {h _ {0}, m _ {0}} ^ {s} \big (k _ {0} ^ {- 1} \big (\varpi_ {0} ^ {d _ {1}} g _ {1} ^ {0}, \ldots , \varpi_ {0} ^ {d _ {| P |}} g _ {| P |} ^ {0} \big) n _ {0} k _ {0} ^ {\prime} \big) \cdot d n _ {0}. \end{array}
$$

On est ramene à comprendre le comportement des int ´ egrales´

$$
\int f _ {h _ {0}, m _ {0}} ^ {s} \left(k _ {0} ^ {- 1} \left(\varpi_ {0} ^ {d _ {1}} g _ {1}, \dots , \varpi_ {0} ^ {d _ {| P |}} g _ {| P |}\right) n _ {0} k _ {0} ^ {\prime}\right) \cdot d n _ {0} d g _ {1} \dots d g _ {| P |}
$$

où$g _ { 1 } , \ldots , g _ { | P | }$decrivent maintenant des classes de congruence modulo´$\varpi _ { 0 } ^ { m }$

On a besoin de savoir determiner les valeurs´$f _ { h _ { 0 } , m _ { 0 } } ^ { s } ( g )$des fonctions $f _ { h _ { 0 } , m _ { 0 } } ^ { s }$en les el´ ements´$g \in \mathrm { G L } _ { r } ( F _ { 0 } )$

Lemme II.13. – Soit$s = \deg ( 0 ) h _ { 0 } s ^ { \prime } , s ^ { \prime } \geq 1$, un multiple de deg(0)h et g un el´ ement de´${ \mathrm { G L } } _ { r } ( F _ { 0 } )$

(i) Pour que$f _ { h _ { 0 } , m _ { 0 } } ^ { s } ( g ) \neq 0$, ilfaut que g verifie les conditions suivantes :´ • 0(det$g ) = h _ { 0 } s ^ { \prime }$

• g est à coefficients entiers,

• l’image et le noyau de la reduction modulo´$\varpi _ { 0 } ^ { s ^ { \prime } }$de g sont libres de rangs$r - h _ { 0 }$et h<sub>0</sub> sur${ \cal O } _ { 0 } / \varpi _ { 0 } ^ { s ^ { \prime } }$

• l’image et le noyau de la reduction modulo´$\varpi _ { 0 }$de g sont en somme directe.

(ii) Si les conditions de (i) sont verifi´ ees, on a´

$\varpi _ { 0 } ^ { s ^ { \prime } } g ^ { - 1 }$est à coefficients entiers,

• la matrice$\varpi _ { 0 } ^ { - s ^ { \prime } } \cdot \Lambda ^ { r - h _ { 0 } + 1 } g$est à coefficients entiers et l’image de sa reduction modulo´$\varpi _ { 0 } ^ { s ^ { \prime } }$est libre de rang h sur${ { O } _ { 0 } } / { { \varpi } _ { 0 } }$

(iii) Si l’entier m a et´ e choisi assez grand, si´$s ^ { \prime } > m$et si g verifie les´ conditions de (i) et donc aussi de (ii), la valeur$f _ { h _ { 0 } , m _ { 0 } } ^ { s } ( g )$ne depend´ que des reductions modulo´$\varpi _ { 0 } ^ { m }$des matrices g et$\varpi _ { 0 } ^ { - s ^ { \prime } } \cdot \Lambda ^ { r - h _ { 0 } + 1 } g .$

Demonstration du lemme II.13 :´ Rappelons comment la fonction$f _ { h _ { 0 } , m _ { 0 } } ^ { s }$ a et´ e d´ efinie. Il existe une fonction localement constante et invar´ iante par conjugaison

$$
f _ {0 ^ {\prime}, m _ {0}}: \mathrm{GL} _ {h _ {0}} (O _ {0}) \to \mathbb {Q}
$$

telle que, pour tout$g \in \mathrm { G L } _ { r } ( F _ { 0 } )$, on a

$$
f _ {h _ {0}, m _ {0}} ^ {s} (g) = f _ {0 ^ {\prime}, m _ {0}} (g ^ {\prime \prime})
$$

s’il existe$k \in \mathrm { G L } _ { r } ( O _ { 0 } )$verifiant´

$$
k ^ {- 1} g k = \left(g ^ {\prime}, \varpi_ {0} ^ {s ^ {\prime}} g ^ {\prime \prime}\right) \quad \text { avec } \quad g ^ {\prime} \in \mathrm{GL} _ {r - h _ {0}} (O _ {0}),   g ^ {\prime \prime} \in \mathrm{GL} _ {h _ {0}} (O _ {0})\tag{*}
$$

et sinon

$$
f _ {h _ {0}, m _ {0}} ^ {s} (g) = 0.
$$

Pour$g$donne, l’existence d’un´$k \in \mathrm { G L } _ { r } ( O _ { 0 } )$verifiant´ (∗) est equivalente´ aux conditions de (i) et elle implique les conditions de (ii).

Il reste à prouver (iii).

On peut supposer que l’entier$m \geq 1$a et´ e choisi assez grand pour que´ la fonction$\bar { \mathrm { \bf G L } _ { h _ { 0 } } } \bar { ( O _ { 0 } ) \mathrm { \bf ~ \ni ~ } } g ^ { \prime \prime } \mapsto f _ { 0 ^ { \prime } , m _ { 0 } } ( g ^ { \prime \prime } )$ne depende que des classes de´ congruence modulo$\varpi _ { 0 } ^ { m }$des el´ ements´$g ^ { \prime \prime }$

Considerons donc un´ el´ ement´ g qui verifie les conditions de´$\mathrm { ( i ) } \mathrm { c } ^ { \mathrm { , } } \mathrm { e s t - } \mathrm { a - }$ dire s’ecrit´$g = k ( g ^ { \prime } , \varpi _ { 0 } ^ { s ^ { \prime } } g ^ { \prime \prime } ) k ^ { - 1 }$. La reduction modulo´$\varpi _ { 0 } ^ { m }$de$\varpi _ { 0 } ^ { - s ^ { \prime } } \cdot \Lambda ^ { r - h _ { 0 } + 1 } g$ se factorise en

$$
\begin{array}{c} \Lambda^ {r - h _ {0} + 1} (O _ {0} / \varpi_ {0} ^ {m}) ^ {r} \longrightarrow \Lambda^ {r - h _ {0} + 1} (O _ {0} / \varpi_ {0} ^ {m}) ^ {r} \\ \Biggl \downarrow \\ \det ((O _ {0} / \varpi_ {0} ^ {m}) ^ {r} / \operatorname{Ker} _ {m} (g)) \xrightarrow {\sim} \det (\operatorname{Im} _ {m} (g)) \\ \otimes \operatorname{Ker} _ {m} (g) \end{array}
$$

(où$\mathrm { K e r } _ { m } ( g )$et${ \mathrm { I m } } _ { m } ( g )$designent le noyau et l’image de´$g$reduit modulo´ $\varpi _ { 0 } ^ { m } )$.

Si on tensorise avec l’inverse de l’isomorphisme

$$
\det \left(\left(O _ {0} / \varpi_ {0} ^ {m}\right) ^ {r} / \operatorname{Ker} _ {m} (g)\right) \stackrel {{\sim}} {{\longrightarrow}} \det (\operatorname{Im} _ {m} (g))
$$

deduit de´ g par reduction modulo´$\varpi _ { 0 } ^ { m }$, on obtient un isomorphisme

$$
\mathrm{Ker} _ {m} (g) \stackrel {\sim} {\longrightarrow} \left(O _ {0} / \varpi_ {0} ^ {m}\right) ^ {r} / \mathrm{Im} _ {m} (g)
$$

qu’on peut toujours composer avec l’inverse de la projection

$$
\operatorname{Ker} _ {m} (g) \hookrightarrow \left(O _ {0} / \varpi_ {0} ^ {m}\right) ^ {r} \longrightarrow \left(O _ {0} / \varpi_ {0} ^ {m}\right) ^ {r} / \operatorname{Im} _ {m} (g)
$$

pour obtenir un automorphisme

$$
\operatorname{Ker} _ {m} (g) \stackrel {{\sim}} {{\longrightarrow}} \operatorname{Ker} _ {m} (g).
$$

Celui-ci est conjugue à´$g ^ { \prime \prime }$et donc il determine la valeur´$f _ { h _ { 0 } , m _ { 0 } } ^ { s } ( g )$!"

Suite de la demonstration du lemme II.12 :´ Pour alleger, notons d´ esormais´ $k = | \boldsymbol { P } |$et revenons aux integrales´

$$
\int f _ {h _ {0}, m _ {0}} ^ {s} \left(k _ {0} ^ {- 1} \left(\varpi_ {0} ^ {d _ {1}} g _ {1}, \dots , \varpi_ {0} ^ {d _ {k}} g _ {k}\right) n _ {0} k _ {0} ^ {\prime}\right) \cdot d n _ {0} d g _ {1} \dots d g _ {k}.
$$

On voit dejà que pour avoir´

$$
f _ {h _ {0}, m _ {0}} ^ {s} \big (k _ {0} ^ {- 1} \big (\varpi_ {0} ^ {d _ {1}} g _ {1}, \ldots , \varpi_ {0} ^ {d _ {k}} g _ {k} \big) n _ {0} k _ {0} ^ {\prime} \big) \neq 0,
$$

il faut

$$
0 \leq d _ {1} \leq s ^ {\prime}, \dots , 0 \leq d _ {k} \leq s ^ {\prime}
$$

et

$$
r _ {1} d _ {1} + \dots + r _ {k} d _ {k} + (v _ {1} + \dots + v _ {k}) = h _ {0} s ^ {\prime}
$$

où$v _ { 1 } , \ldots , v _ { k }$designent les valuations des d´ eterminants de´$g _ { 1 } , \ldots , g _ { k }$(elles sont fixees car ne d´ ependent que des classes de congruence modulo´$\varpi _ { 0 } ^ { m }$de ceux-ci). Dorenavant, on supposera ces conditions v´ erifi´ ees.´

Recrivons les´ el´ ements´$( \varpi _ { 0 } ^ { d _ { 1 } } g _ { 1 } , \ldots , \varpi _ { 0 } ^ { d _ { k } } g _ { k } ) n _ { 0 } = g$sous la forme :

$$
g = \left( \begin{array}{c c c c} \varpi_ {0} ^ {d _ {1}} g _ {1} & n _ {1, 2} & \ldots & n _ {1, k} \\ 0 & \varpi_ {0} ^ {d _ {2}} g _ {2} & n _ {2, 3} & \vdots \\ \vdots & \ddots & \ddots & \ddots \\ \vdots & \ddots & & n _ {k - 1, k} \\ 0 & \ldots & 0 & \varpi_ {0} ^ {d _ {k}} g _ {k} \end{array} \right)
$$

D’après le lemme II.13, on est ramene au problème de calculer en´ fonction de$s ^ { \prime }$et$d _ { 1 } , d _ { 2 } , \ldots , d _ { k }$le volume de l’ouvert des$g _ { 1 } , \ldots , g _ { k } \operatorname { e t } n _ { i , j }$ $0 < i < j \leq k$, qui verifient les conditions suivantes :´

(1) Les$g _ { 1 } , \ldots , g _ { k }$sont dans des classes de congruence fixees modulo´$\varpi _ { 0 } ^ { m }$ (2) Tous les$n _ { i , j }$sont à coefficients entiers et ils sont dans des classes de congruence fixees modulo´$\varpi _ { 0 } ^ { m }$

(3) Modulo$\varpi _ { 0 } ^ { s ^ { \prime } }$, la matrice g a un noyau libre de rang$h _ { 0 }$sur${ \cal O } _ { 0 } / \varpi _ { 0 } ^ { s ^ { \prime } }$

(4) La matrice$\varpi _ { 0 } ^ { - s ^ { \prime } } \cdot \Lambda ^ { r - h _ { 0 } + 1 } g$(qui est automatiquement à coefficients entiers) est dans une classe de congruence fixee modulo´$\varpi _ { 0 } ^ { m }$

Comme la matrice g a une image libre de rang$r - h _ { 0 }$modulo$\varpi _ { 0 } ^ { s ^ { \prime } }$, on peut choisir une famille de$r - h _ { 0 }$vecteurs colonnes de g qui forment une base de l’image. L’ensemble$\mathcal { B } \subseteq \{ 1 , 2 , \ldots , r \}$de leurs indices peut être choisi independamment de´ g car g est dans une classe de congruence fixee´ modulo$\varpi _ { 0 } ^ { m }$(on decide que chaque´$d _ { i }$et$s ^ { \prime } - d _ { i }$ou bien est fixe à une valeur´ $< m$ou bien est variable$\geq m )$

Ces$r \mathrm { ~ - ~ } h _ { 0 }$vecteurs colonnes forment une matrice à r vecteurs lignes dont on note$\ell _ { 1 } , \ldots , \ell _ { r }$les reductions dans´$( O _ { 0 } / \varpi _ { 0 } ^ { s ^ { \prime } + m } ) ^ { r - h _ { 0 } }$et$\overline { { \ell } } _ { 1 } , \ldots , \overline { { \ell } } _ { r }$ celles dans$( O _ { 0 } / \varpi _ { 0 } ^ { s ^ { \prime } } ) ^ { r - h _ { 0 } }$

On note$E _ { r - 1 } , E _ { r - 2 } , \ldots , E _ { 0 }$les sous-modules de$( O _ { 0 } / \varpi _ { 0 } ^ { s ^ { \prime } + m } ) ^ { r - h _ { 0 } }$engendres par ´$\ell _ { r } , ( \ell _ { r } , \ell _ { r - 1 } ) , \ldots , ( \ell _ { r } , \ell _ { r - 1 } , \ldots , \ell _ { 1 } )$et$\bar { E } _ { r - 1 } , \bar { E } _ { r - 2 } , \ldots , \bar { E } _ { 0 }$ leurs images dans$( O _ { 0 } / \varpi _ { 0 } ^ { s ^ { \prime } } ) ^ { r - h _ { 0 } }$. On a

$$
0 = E _ {r} \subseteq E _ {r - 1} \subseteq E _ {r - 2} \subseteq \dots \subseteq E _ {0} = \left(O _ {0} / \varpi_ {0} ^ {s ^ {\prime} + m}\right) ^ {r - h _ {0}}
$$

et on peut choisir un ensemble d’indices (ici encore independant de´ g) $\mathcal { A } \subseteq \{ 1 , \ldots , r \}$de cardinal$r - h _ { 0 }$tel que les$\ell _ { \alpha } , \alpha \in \mathcal { A }$, forment une base de$( O _ { 0 } / \varpi _ { 0 } ^ { s ^ { \prime } + m } ) ^ { r - h _ { 0 } } = E _ { 0 }$

Pour tout α,$0 \leq \alpha \leq r - 1$, il existe des entiers$v _ { \alpha , d } , 1 \le d \le r - \alpha ,$ $0 \leq v _ { \alpha , d } \leq s ^ { \prime } + m$, tels que pour tout entier v,$0 \leq v < s ^ { \prime } + m$, on a l’equivalence´

$$
\left. \dim \left(E _ {\alpha} \cap \left(\varpi_ {0} ^ {v} \cdot O _ {0}\right) ^ {r - h _ {0}}\right) / \left(E _ {\alpha} \cap \left(\varpi_ {0} ^ {v + 1} \cdot O _ {0}\right) ^ {r - h _ {0}}\right) \geq d \right.
$$

$$
\Longleftrightarrow v \geq v _ {\alpha , d}.
$$

Les entiers$\bar { v } _ { \alpha , d } = \operatorname* { m i n } \{ v _ { \alpha , d } , s ^ { \prime } \}$sont tels que pour tout entier$v \leq s ^ { \prime }$, on a

$$
\left. \dim \left(\bar {E} _ {\alpha} \cap \left(\varpi_ {0} ^ {v} \cdot O _ {0}\right) ^ {r - h _ {0}}\right) / \left(\bar {E} _ {\alpha} \cap \left(\varpi_ {0} ^ {v + 1} \cdot O _ {0}\right) ^ {r - h _ {0}}\right) \geq d \right.
$$

$$
\Longleftrightarrow v \geq \bar {v} _ {\alpha , d}.
$$

Ceux des entiers$v _ { \alpha , d }$qui sont$< ~ m$sont fixes puisque´ g et donc les $\ell _ { 1 } , \ldots , \ell _ { r }$sont dans une classe de congruence modulo$\varpi _ { 0 } ^ { m }$fixee. On d´ ecide´ de fixer aussi ceux des entiers$s ^ { \prime } + m - v _ { \alpha , d }$qui sont$< m$

Considerons maintenant un vecteur colonne arbitraire´$c _ { \beta } , 1 \leq \beta \leq r .$ dans la matrice g. Soit$i , 1 \le i \le k$, l’unique entier tel que

$$
\beta^ {-} = r _ {1} + \dots + r _ {i - 1} <   \beta \leq r _ {1} + \dots + r _ {i} = \beta^ {+}.
$$

Ce vecteur doit verifier les conditions suivantes :´

• d’une part, (3) signifie que, modulo$\varpi _ { 0 } ^ { s ^ { \prime } }$, il est lie aux´$r - h _ { 0 }$vecteurs colonnes$c _ { \beta ^ { \prime } } , \beta ^ { \prime } \in \mathcal { B }$;

• d’autre part, si on note$( x _ { 1 } , \ldots , x _ { r } )$ses coordonnees, on a´

$$
x _ {\alpha} = 0, \forall \alpha > \beta^ {+}.
$$

(On oublie provisoirement la condition (4).)

On considère la matrice formee des´$r \mathrm { ~ - ~ } h _ { 0 }$colonnes$c _ { \beta ^ { \prime } } , \beta ^ { \prime } \in \mathcal { B }$, et de la colonne$c _ { \beta }$. La première condition se represente en disant que pour´ tout α,$1 \leq \alpha \leq r , \alpha \notin { \mathcal { A } }$, la matrice carree´$M _ { \alpha , \beta }$d’ordre$r - h _ { 0 } + 1$formee´ des vecteurs lignes indexes par les´$\alpha ^ { \prime } \in \mathcal { A }$et par α a un determinant qui´ $\mathrm {  ~ s ~ } ^ { \prime }$annule à l’ordre$\varpi _ { 0 } ^ { s ^ { \prime } }$

Notons$\bar { \ell } _ { \mathcal { A } }$la matrice carree form´ ee par les vecteurs lignes´$\bar { \ell } _ { \alpha ^ { \prime } } , \alpha ^ { \prime } \in \mathcal { A }$ et pour tous indices α$\notin \mathcal { A } , \alpha ^ { \prime } \in \mathcal { A }$, notons$\mathcal { \overline { {ell } } } _ { \alpha , \mathcal { A } } ^ { \alpha ^ { \prime } }$la matrice deduite de´$\bar { \ell } _ { \mathcal { A } }$ en enlevant la ligne d’indice$\alpha ^ { \prime }$et en la remplaçant par le vecteur ligne$\overline { { \ell } } _ { \alpha }$

On obtient les equations´

$$
(\det \bar {\ell} _ {\mathcal {A}}) x _ {\alpha} - \sum_ {\alpha^ {\prime} \in \mathcal {A}} \big (\det \bar {\ell} _ {\alpha , \mathcal {A}} ^ {\alpha^ {\prime}} \big) x _ {\alpha^ {\prime}} \equiv 0 \quad \left[ \varpi_ {0} ^ {s ^ {\prime}} \right].
$$

Il resulte de la d´ efinition de´$\mathcal { A }$que det$\bar { \ell } _ { \mathcal { A } }$est inversible. Pour tout$\alpha ,$, le vecteur à$r - h _ { 0 }$coordonnees´

$$
\left(\frac {\det \bar {\ell} _ {\alpha , \mathcal {A}} ^ {\alpha^ {\prime}}}{\det \bar {\ell} _ {\mathcal {A}}}\right) _ {\alpha^ {\prime} \in \mathcal {A}}
$$

n’est autre que le vecteur des coordonnees de´$\bar { \ell } _ { \alpha }$dans la base de$( O _ { 0 } / \varpi _ { 0 } ^ { s ^ { \prime } } ) ^ { r - h _ { 0 } }$ constituée des$\bar { \ell } _ { \alpha ^ { \prime } } , \alpha ^ { \prime } \in \mathcal { A }$

Le fait que$x _ { \alpha } = 0 , \forall \alpha > \beta ^ { + }$, signifie exactement que le vecteur des $( x _ { \alpha ^ { \prime } } ) _ { \alpha ^ { \prime } \in \mathcal { A } }$doit être dans l’orthogonal du sous-module$\bar { E } _ { \beta ^ { + } }$de$( O _ { 0 } / \varpi _ { 0 } ^ { s ^ { \prime } } ) ^ { r - h _ { 0 } }$ Autrement dit, le vecteur$( x _ { \alpha ^ { \prime } } ) _ { \alpha ^ { \prime } \in \mathcal { A } }$est astreint à decrire le sous-espace des´ applications lineaires´

$$
\left(O _ {0} / \varpi_ {0} ^ {s ^ {\prime}}\right) ^ {r - h _ {0}} \longrightarrow O _ {0} / \varpi_ {0} ^ {s ^ {\prime}}
$$

qui$\mathrm {  ~ s ~ } ^ { \prime }$annulent sur le sous-module$\bar { E } _ { \beta ^ { + } }$. Quant aux autres coordonnees´$x _ { \alpha }$ $\alpha \notin \mathcal A$, elles sont complètement determin´ ees (à l’ordre´$\varpi _ { 0 } ^ { s ^ { \prime } } )$par celles-là.

Pour un i donne,´$1 \leq i \leq k .$, regardons maintenant simultanement tous´ les$\beta$tels que$r _ { 1 } + \cdot \cdot \cdot + r _ { i - 1 } < \beta \leq r _ { 1 } + \cdot \cdot \cdot + r _ { i } \mathrm { c } ^ { \prime } \mathrm { e s t } { \tt - } \hat { \bf a } \mathrm { - } \mathrm { d i r e } \beta ^ { + } = r _ { 1 } + \cdot \cdot \cdot + r _ { i }$ L’ensemble des vecteurs colonnes$c _ { \beta }$definit une application lin´ eaire´

$$
\left(O _ {0} / \varpi_ {0} ^ {s ^ {\prime}}\right) ^ {r - h _ {0}} \longrightarrow \left(O _ {0} / \varpi_ {0} ^ {s ^ {\prime}}\right) ^ {r _ {i}}
$$

qui${ \mathrm { s } } ^ { \prime }$annule sur le sous-module$\bar { E } _ { r _ { 1 } + \cdots + r _ { i } }$. Les coordonnees des´$c _ { \beta }$dont l’indice α verifie´$r _ { 1 } + \cdot \cdot \cdot + r _ { i - 1 } < \alpha \leq r _ { 1 } + \cdot \cdot \cdot + r _ { i }$, soit$\alpha ^ { + } = r _ { 1 } + \cdot \cdot \cdot + r _ { i }$ definissent une application lin´ eaire´

$$
\bar {E} _ {r _ {1} + \dots + r _ {i - 1}} / \bar {E} _ {r _ {1} + \dots + r _ {i}} \longrightarrow \left(O _ {0} / \varpi_ {0} ^ {s ^ {\prime}}\right) ^ {r _ {i}}
$$

qui donc s’identifie à la reduction modulo´$\varpi _ { 0 } ^ { s ^ { \prime } }$de$\boldsymbol { \varpi } _ { 0 } ^ { d _ { i } } \boldsymbol { g } _ { i }$

La longueur de$\bar { E } _ { r _ { 1 } + \cdots + r _ { i - 1 } } / \bar { E } _ { r _ { 1 } + \cdots + r _ { i } }$est egale à ´

$$
\left(\sum_ {d \leq r _ {i + 1} + \dots + r _ {k}} \bar {v} _ {r _ {1} + \dots + r _ {i}, d}\right) - \left(\sum_ {d \leq r _ {i} + \dots + r _ {k}} \bar {v} _ {r _ {1} + \dots + r _ {i - 1}, d}\right)
$$

et elle majore la longueur de son image qui est

$$
r _ {i} (s ^ {\prime} - d _ {i}) - v _ {i}.
$$

En faisant la somme sur tous les$i , 1 \leq i \leq k$, on obtient

$$
(r - h _ {0}) s ^ {\prime} \geq (r _ {1} + \dots + r _ {k}) s ^ {\prime} - (r _ {1} d _ {1} + \dots + r _ {k} d _ {k}) - (v _ {1} + \dots + v _ {k})
$$

qui se recrit´

$$
(r _ {1} d _ {1} + \dots + r _ {k} d _ {k}) + (v _ {1} + \dots + v _ {k}) \geq h _ {0} s ^ {\prime}.
$$

Or au debut de la discussion on a impos´ e´

$$
(r _ {1} d _ {1} + \dots + r _ {k} d _ {k}) + (v _ {1} + \dots + v _ {k}) = h _ {0} s ^ {\prime}.
$$

Toutes les inegalit´ es ci-dessus doivent donc être des´ egalit´ es et´

$$
\bar {E} _ {r _ {1} + \dots + r _ {i - 1}} / \bar {E} _ {r _ {1} + \dots + r _ {i}} \hookrightarrow \left(O _ {0} / \varpi_ {0} ^ {s ^ {\prime}}\right) ^ {r _ {i}}
$$

doit être un plongement.

Pour tout indice α,$r _ { 1 } + \cdot \cdot \cdot + r _ { i - 1 } < \alpha \leq r _ { 1 } + \cdot \cdot \cdot + r _ { i }$, notons$m _ { \alpha } .$ $0 < m _ { \alpha } \le m$, la longueur du quotient dans$( O _ { 0 } / \varpi _ { 0 } ^ { m } ) ^ { r _ { i } }$du sous-module engendre par les vecteurs lignes de´$g _ { i }$d’indices$\geq \alpha$par le sous-module engendre par ceux d’indices´$> \alpha . \mathbf { C } ^ { \prime }$est un entier fixe. Alors on a pour tout´ α

$$
\left(\sum_ {d \leq r - \alpha} \bar {v} _ {\alpha , d}\right) - \left(\sum_ {d \leq r - \alpha + 1} \bar {v} _ {\alpha - 1, d}\right) = (s ^ {\prime} - d _ {i}) + m _ {\alpha} - m.
$$

Nous decidons maintenant de fixer pour tout´ α,$1 \leq \alpha \leq r .$, la filtration croissante de$( O _ { 0 } / \varpi _ { 0 } ^ { m } ) ^ { r - h _ { 0 } }$constituee par les images des´$( E _ { \alpha } \cap \varpi _ { 0 } ^ { v }$ $O _ { 0 } ^ { r - h _ { 0 } } ) / ( E _ { \alpha } \cap \varpi _ { 0 } ^ { v + m } \cdot O _ { 0 } ^ { r - h _ { 0 } } ) , 0 \le v \le s ^ { \prime }$

En particulier, les modules$\bar { E } _ { \alpha }$sont entièrement determin´ es modulo´$\varpi _ { 0 } ^ { m }$ et il en est de même de leurs quotients

$$
(\bar {E} _ {r _ {1} + \dots + r _ {i - 1}} / \bar {E} _ {r _ {1} + \dots + r _ {i}}) \otimes \left(O _ {0} / \varpi_ {0} ^ {m}\right).
$$

Alors, pour tout$\beta \notin \mathcal { B }$, l’existence d’un vecteur colonne$c _ { \beta } = ( x _ { 1 } , \ldots , x _ { r } )$ ${ \mathrm { c } } ^ { \prime }$est-à-dire d’une application lineaire´

$$
\left(O _ {0} / \varpi_ {0} ^ {s ^ {\prime}}\right) ^ {r - h _ {0}} / \bar {E} _ {\beta^ {+}} \longrightarrow \left(O _ {0} / \varpi_ {0} ^ {s ^ {\prime}}\right)
$$

compatible à la fois avec les conditions de congruence imposees aux´

$$
\varpi_ {0} ^ {- d _ {i}} (x _ {\beta^ {-} + 1}, \dots , x _ {\beta^ {+}})
$$

et aux

$$
(x _ {1}, x _ {2}, \dots , x _ {\beta})
$$

modulo$\varpi _ { 0 } ^ { m }$, ne depend que de toutes les classes de congruence modulo´$\varpi _ { 0 } ^ { m }$ que nous avons fixees.´

S’il y a compatibilite, le volume de l’ouvert des vecteurs colonnes´

$$
c _ {\beta}, \beta \notin \mathcal {B},
$$

qui verifient les conditions (1), (2) et (3) est´ egal à une constante multiplica-´ tive près à

$$
\begin{array}{l} V = \prod_ {1 \leq \beta \leq r} q ^ {- \lg (\bar {E} _ {\beta^ {+}})} q ^ {- n _ {\beta} s ^ {\prime}} \\ = \prod_ {1 \leq i \leq k} q ^ {- r _ {i} \cdot \sum_ {d \leq r _ {i + 1} + \dots + r _ {k}} \bar {v} _ {r _ {1} + \dots + r _ {i}, d}} \cdot \left(\prod_ {1 \leq \beta \leq r} q ^ {- n _ {\beta}}\right) ^ {s ^ {\prime}} \end{array}
$$

où$\mathrm { l g } \left( \cdot \right)$designe la longueur´$\mathrm { d } '$un module et, pour tout indice β,$1 \leq \beta \leq r$ $n _ { \beta }$est le cardinal de l’ensemble

$$
\{\alpha \mid 1 \leq \alpha \leq \beta^ {+}, \alpha \notin \mathcal {A} \}.
$$

Il reste à imposer en plus la condition (4). Connaître l’homomorphisme $\varpi _ { 0 } ^ { - s ^ { \prime } } \cdot \Lambda ^ { r - h _ { 0 } + 1 } g$modulo$\varpi _ { 0 } ^ { m }$est equivalent à connaître modulo´$\varpi _ { 0 } ^ { s ^ { \prime } + m }$la famille des determinants´

$$
\det M _ {\alpha , \beta}, \alpha \notin \mathcal {A}, \beta \notin \mathcal {B},
$$

qui$\mathrm { s } '$annulent modulo$\varpi _ { 0 } ^ { s ^ { \prime } }$.

Pour tout indice$\beta$avec$\beta ^ { - } = r _ { 1 } + \cdot \cdot \cdot + r _ { i - 1 } < \beta \leq r _ { 1 } + \cdot \cdot \cdot + r _ { i } = \beta ^ { + }$ et si$c _ { \beta } = ( x _ { 1 } , \ldots , x _ { r } )$est le vecteur colonne associe, on a pour tout indice´ α$\notin \mathcal { A }$

$$
\det M _ {\alpha , \beta} \equiv (\det \ell_ {\mathcal {A}}) x _ {\alpha} - \sum_ {\alpha^ {\prime} \in \mathcal {A}} \bigl (\det \ell_ {\alpha , \mathcal {A}} ^ {\alpha^ {\prime}} \bigr) x _ {\alpha} \qquad \left[ \varpi_ {0} ^ {s ^ {\prime} + m} \right]
$$

où$\ell _ { \mathcal { A } }$designe la matrice carr´ ee form´ ee par les vecteurs lignes´$\ell _ { \alpha ^ { \prime } } , \alpha ^ { \prime } \in \mathcal { A }$ et les$\ell _ { \alpha , \mathcal { A } } ^ { \alpha ^ { \prime } }$sont deduites de´$\ell _ { \mathcal { A } }$en remplaçant la ligne$\ell _ { \alpha ^ { \prime } } \operatorname { p a r } \ell _ { \alpha }$

En les indices$\alpha \leq \beta ^ { - }$, les det$M _ { \alpha , \beta }$peuvent prendre des valeurs arbitraires dans$\varpi _ { 0 } ^ { s ^ { \prime } } \cdot O _ { 0 } / \varpi _ { 0 } ^ { s ^ { \prime } + m } \cdot O _ { 0 } \cong O _ { 0 } / \varpi _ { 0 } ^ { m }$et independantes des autres´ choix. Il en est de même en les indices α dans$] \beta ^ { - } , \beta ^ { + } ] \sin s ^ { \prime } - d _ { i } \geq m$

Se donner la famille des (det$M _ { \alpha , \beta } ) _ { \alpha > \beta ^ { + } }$modulo$\varpi _ { 0 } ^ { s ^ { \prime } + m }$est equivalent´ à se donner une application lineaire sur le module´$E _ { \beta ^ { + } } \cap \varpi _ { 0 } ^ { s ^ { \prime } } \cdot O _ { 0 } ^ { r - h _ { 0 } }$. Or celui-ci est complètement determin´ e puisqu’on a fix´ e la filtration croissante´ de$( O _ { 0 } / \varpi _ { 0 } ^ { m } ) ^ { r - h _ { 0 } }$par les images des$( \bar { E } _ { \alpha ^ { \prime } } \cap \bar { \varpi } _ { 0 } ^ { v } \cdot O _ { 0 } ^ { r - h _ { 0 } } ) / ( E _ { \alpha ^ { \prime } } \cap \varpi _ { 0 } ^ { v + m } \cdot O _ { 0 } ^ { r - h _ { 0 } } )$ et ceux des entiers$s ^ { \prime } + m - v _ { \alpha ^ { \prime } , d }$qui sont$< m$

De même, si$s ^ { \prime } - d _ { i } < m$, il est fixe et la famille des´ (det$M _ { \alpha , \beta } ) _ { \alpha > \beta ^ { - } }$ peut prendre dans$( \varpi _ { 0 } ^ { s ^ { \prime } } \cdot O _ { 0 } / \varpi _ { 0 } ^ { s ^ { \prime } + m } \cdot O _ { 0 } ) ^ { r - \beta ^ { - } } \cong ( O _ { 0 } / \varpi _ { 0 } ^ { m } ) ^ { r - \beta ^ { - } }$des valeurs independantes des autres choix dans un ensemble de possibilit´ es d´ etermin´ e´ seulement par la classe de congruence modulo$\varpi _ { 0 } ^ { m }$de$g _ { i }$et le module fixe´ $E _ { \beta } \cap \varpi _ { 0 } ^ { s ^ { \prime } } \cdot O _ { 0 } ^ { r - h _ { 0 } }$

En definitive, le volume´$V ^ { \prime }$de l’ouvert des vecteurs colonnes$c _ { \beta } , \beta \notin { \mathcal { B } }$ qui verifient les conditions (1), (2), (3) et (4) (les autres vecte´ urs colonnes $c _ { \beta } , \beta \in { \mathcal { B } }$, etant donn´ es) ne diffère du volume´ V de l’ouvert defini par les´ seules conditions (1), (2) et (3) que par une constante multiplicative, et la demonstration du lemme II.12 est ramen´ ee au lemme facile suivant :´

Lemme II.14. – Les entiers r,$h _ { 0 }$et m$\geq$1 etantfix´ es, on considère un entier´ variable$s ^ { \prime } \geq$m ainsi qu’une famille d’entiers variables$v _ { \alpha , d } , 0 \le \alpha < r$ $1 \leq d \leq r - \alpha$, verifiant´$0 \leq v _ { \alpha , d } \leq s ^ { \prime } + m$

On considère le volume V de l’ouvert desfamilles de vecteurs$\ell _ { 1 } , \ldots , \ell _ { r }$ dans des sous-espaces fixes (d´ efinis par l’annulation de certaines coor-´ donnees) de´$O _ { 0 } ^ { r - h _ { 0 } }$tels que, si$E _ { r - 1 } , \ldots , E _ { 0 }$designent les sous-modules de´ $( O _ { 0 } / \varpi _ { 0 } ^ { s ^ { \prime } + m } ) ^ { r - h _ { 0 } }$engendres par´$\ell _ { r } , ( \ell _ { r } , \ell _ { r - 1 } ) , \ldots , ( \ell _ { r } , \ldots , \ell _ { 1 } )$, on ait :

• les classes de congruence modulo$\varpi _ { 0 } ^ { m }$de$\ell _ { 1 } , \ldots , \ell _ { r }$sont fixees,´

• pour tout α,$1 \leq \alpha \leq r ,$, et si la valuation$0 ( \ell _ { \alpha } )$de$\ell _ { \alpha } e s t \le s ^ { \prime }$, la classe de congruence modulo$\varpi _ { 0 } ^ { m }$de$\varpi _ { 0 } ^ { - 0 ( \ell _ { \alpha } ) } \ell _ { \alpha }$estfixee,´

• pour tout α, la filtration croissante de$( O _ { 0 } / \varpi _ { 0 } ^ { m } ) ^ { r - h _ { 0 } }$definie par les´ images des$( E _ { \alpha } \cap \varpi _ { 0 } ^ { v } \cdot O _ { 0 } ^ { r - h _ { 0 } } ) / ( E _ { \alpha } \cap \varpi _ { 0 } ^ { v + m } \cdot O _ { 0 } ^ { r - h _ { 0 } } ) , 0 \le v \le s ^ { \prime }$, est fixee,´

• pour tout α,$0 \leq \alpha < r$, tout d,$1 \leq d \leq r - \alpha$et tout v,$0 \leq v < s ^ { \prime } + m$ l’inegalit´ e´$v \leq v _ { \alpha , d }$est verifi´ ee si et seulement si´

$$
\dim \left(E _ {\alpha} \cap \varpi_ {0} ^ {v} \cdot O _ {0} ^ {r - h _ {0}} / E _ {\alpha} \cap \varpi_ {0} ^ {v + 1} \cdot O _ {0} ^ {r - h _ {0}}\right) \geq d.
$$

Alors il existe un ensemble fini d’inegalit´ es de laforme´

$$
v _ {\alpha , d} - v _ {\alpha^ {\prime}, d ^ {\prime}} \geq c,
$$

$$
v _ {\alpha , d} \geq c, s ^ {\prime} - v _ {\alpha , d} \geq c
$$

(où les c sont des entiersfixes´ ) tels que dans chacune des parties du reseau´ des$( s ^ { \prime } : v _ { \alpha , d } )$definies en demandant que chacune de ces in´ egalit´ es soient´ verifi´ ees ou ne le soit pas, le volume V s’´ ecrive´

$$
\sum_ {\iota} c _ {\iota} q ^ {- \left(\sum_ {\alpha , d} m _ {\alpha , d, \iota} v _ {\alpha , d} + m _ {\iota} s ^ {\prime}\right)}
$$

où les$m _ { \alpha , d , \iota }$et$m _ { \iota }$sont des entiers fixes et les´$c _ { \iota }$sont des constantes.

## e) Allure des nombres de Lefschetz

Sont toujours fixes le niveau´$N \hookrightarrow X$, le point 0 de N de multiplicite´$m _ { 0 }$et un “modèle”$\widetilde { \mathcal F }$, autrement dit un point de$\overline { { \mathcal { C } } } _ { \varnothing } ^ { r , N }$, qui n’a pas de pôle mais a un zero en 0. Nous pouvons maintenant d´ emontrer :´

Theor´ eme II.15.\` – Pour toutpolygone de troncature$p : [ 0 , r ] \to \mathbb { R } _ { + }$assez convexe enfonction du niveau N, il existe un ensemblefini de constantes$c _ { \iota } ,$ d’entiers$m _ { \iota } \geq 0 ,$, de scalaires$\lambda _ { \iota }$et de representations automorphes cuspi-´ dales$\pi ^ { \iota }$de rangs$r _ { \iota } \leq r$non ramifiees sur´$X - N$telles qu’on ait laformule suivante :

Pour tout point geom´ etrique´$\overline { { \infty } } \in ( X - N ) ( \overline { { \mathbb { F } } } _ { q } )$au-dessus d’une place $\infty \in | X - N |$et pour tout multiple assez grand$s ^ { \mathbf { \lambda } } = \mathrm { d e g } ( \infty ) s ^ { \prime }$de deg(∞) et deg(0)h , le nombre de Lefschetz

$$
\operatorname{Lef} _ {N, \widetilde {\mathcal {F}}, \overline {{\infty}}} ^ {r, \overline {{p}} \leq p} (\text { Frob } ^ {s})
$$

est egal à ´

$$
\sum_ {\iota} c _ {\iota} s ^ {m _ {\iota}} \lambda_ {\iota} ^ {s} \left(z _ {1} \left(\pi_ {\infty} ^ {\iota}\right) ^ {- s ^ {\prime}} + \dots + z _ {r _ {\iota}} \left(\pi_ {\infty} ^ {\iota}\right) ^ {- s ^ {\prime}}\right).
$$

Demonstration :´ Elle est semblable à celle du theorème I.13.´

On part de l’enonc´ e du th´ eorème II.10.´

Puis on ecrit la moyenne de la suite p´ eriodique´

$$
\mathbb {Z} \ni n \mapsto \operatorname{Tr} _ {n} ^ {\leq p} \left(f _ {\infty} ^ {- s ^ {\prime}} \otimes \mathbb {1} _ {K _ {N ^ {\prime}} ^ {\infty , 0}} \otimes f _ {h _ {0}, m _ {0}} ^ {s}\right)
$$

sous forme spectrale, en appliquant la formule des traces d’Arthur-Selberg (theorème´${ 1 2 } ^ { \circ }$du paragraphe VI.2f de [Lafforgue, 1997]).

Dans l’expression spectrale obtenue, la dependance des termes de traces´ en la place ∞ et$s ^ { \prime }$est donnee par la proposition I.4 et le corollaire I.8,´ exactement comme pour le theorème I.9.´

D’autre part, la dependance en ´ s à la place 0 est precis ´ ee par la proposition´ II.11 ci-dessus.

Il reste à deplacer les contours d’int´ egration et à calculer les r´ esidus qui´ apparaissent, ce qui se fait grâce au lemme I.11.!"

## Chapitre III

## Compactifications des champs de chtoucas

Dans l’article [Lafforgue, 1998], on a construit des compactifications des champs de chtoucas de rang r sans structures de niveau qui gen´ eralisent´ celles de Drinfeld en rang$r = 2$. Ce sont les champs de chtoucas iter´ es´ $\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \le p } } }$. Ils sont propres et lisses sur$X \times X$et leurs bords sont des diviseurs à croisements normaux relatifs dont les strates classifient des familles de chtoucas de rangs strictement plus petits que r. Cette dernière propriet´ e est´ essentielle dans la demonstration par r´ ecurrence de la correspondance de´ Langlands que nous allons exposer.

Pour$N = \today$un niveau,$\mathrm { c } ^ { \mathrm {  ' } } \mathrm { e s t - a - d i r e }$un sous-schema ferm´ e fini´ de la courbe X, on peut definir des compactifications´$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$des champs $\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p }$de chtoucas avec structures de niveau N par normalisation audessus de$\operatorname { C h t } ^ { r , d , \overline { { p } } \leq p } \times _ { X \times X } ( X - N ) \times ( X - N )$. Elles apparaissent aussi comme produits fibres dans des carr´ es cart´ esiens´

![](images/page_58_image_4.jpg)

où$\mathbf { \nabla } \cdot \otimes _ { \mathcal { O } _ { X } } \mathcal { O } _ { N }$designe le morphisme lisse de “restriction” des chtoucas it´ er´ es´ de X à N et$\mathcal { C } _ { N } ^ { r }$est le prolongement par normalisation au-dessus de$\mathcal { C } ^ { r , N }$du revêtement de Lang.

Chaque$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$est lisse sur${ \mathfrak { C } } _ { N } ^ { r } \times ( X - N ) \times ( X - N )$mais$\mathcal { C } _ { N } ^ { r }$n’est pas lisse. On exhibe toutefois un ouvert naturel$\mathcal { C } ^ { \prime r , N }$dans$\mathcal { C } ^ { r , N }$tel que les ouverts images reciproques´$\mathcal { C } _ { N } ^ { \prime r }$dans$\mathcal { C } _ { N } ^ { r }$et$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p ^ { \prime } } } }$dans$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$sont lisses. Ces derniers sont très importants et on verifiera au chapitre´$\mathrm { ~ V ~ q u ' ~ }$ils sont stabilises par les correspondances de Hecke.´

Dans le dernier paragraphe et bien qu’en definitive cela ne soit pas´ necessaire pour la suite, on construit des r´ esolutions des singularit´ es´$\widetilde { \mathcal { C } } _ { N } ^ { r }$ des champs$\mathcal { C } _ { N } ^ { r }$dans le cas de niveaux N sans multiplicites. Par un simple´ changement de base, cela induit des resolutions des singularit´ es´$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p }$ des$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$qui donc sont propres et lisses sur$( X - N ) \times ( X - N )$et dont les bords sont des diviseurs à croisements normaux relatifs.

## 1) Les compactifications sans niveau

On rappelle dans ce paragraphe le proced´ e de construction et les principales´ propriet´ es des compactifications´$\overline { { \mathrm { C h t } ^ { r , d , \overline { { { p } } } \leq p } } }$des champs de chtoucas sans structures de niveau, tels qu’exposes dans l’article [Lafforgue, 1998]. On´ part du schema des “homomorphismes complets” vu comme prolongement´ du schema en groupes´${ \mathrm { G L } } _ { r }$

## a) Le schema des homomorphismes complets´

Pour$r \geq 2$un entier, on considère la suite exacte de tores

$$
1 \to \mathbb {G} _ {m} ^ {2} \to \mathbb {G} _ {m} ^ {r + 1} \to \mathbb {G} _ {m} ^ {r - 1} \to 1
$$

où$\mathbb { G } _ { m } ^ { 2 } \to \mathbb { G } _ { m } ^ { r + 1 }$est$( \lambda _ { 0 } , \lambda _ { 1 } ) \mapsto ( \lambda _ { 0 } \lambda _ { 1 } ^ { i } ) _ { 0 \leq i \leq r } \operatorname { e t } \mathbb { G } _ { m } ^ { r + 1 } \to \mathbb { G } _ { m } ^ { r - 1 }$est$( \lambda _ { i } ) _ { 0 \leq i \leq n } \mapsto$ $( \lambda _ { i - 1 } \lambda _ { i } ^ { - 2 } \lambda _ { i + 1 } ) _ { 1 \leq i < r }$. Elle permet d’identifier le quotient$\mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m } ^ { 2 }$au tore $\mathcal { A } _ { \varnothing } ^ { r , 1 } = \mathbb { G } _ { m } ^ { r - 1 }$de la variet´ e torique´$\mathcal { A } ^ { r , 1 } = \mathbb { A } ^ { r - 1 }$

Dans$\mathcal { A } ^ { r , 1 } = \mathbb { A } ^ { r - 1 }$, les orbites de$\mathcal { A } _ { \varnothing } ^ { r , 1 }$sont naturellement indexees par les´ partitions$\boldsymbol { r } = ( r _ { 1 } , \ldots , r _ { k } ) , r _ { 1 } + \cdot \cdot \cdot + r _ { k } = \boldsymbol { r }$, de l’entier r. Ce sont les sousschemas localement ferm´ es´$\mathcal { A } _ { r } ^ { r , 1 }$constitues des points dont les coordonn´ ees´ d’indices$r _ { 1 } + \cdot \cdot \cdot + r _ { e } , 1 \leq e ^ { } < k$, sont nulles et les autres sont inversibles ; chacune contient un unique point$\alpha _ { \underline { { r } } }$dont toutes les coordonnees valent 0´ ou 1.

On note encore$\mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m }$le quotient de$\mathbb { G } _ { m } ^ { r + 1 }$par$\mathbb { G } _ { m }$plonge diagonale-´ ment ; il agit sur$\mathcal { A } ^ { r , 1 }$via son quotient$\mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m } ^ { 2 } \cong \mathcal { A } _ { \varnothing } ^ { r , 1 }$

Proposition III.1. – Pour tout entier$r \ \geq \ 2 ,$, notons$\boldsymbol { \Omega } ^ { r , 1 }$l’adherence´ schematique dans´ (End$( \Lambda ^ { s } \mathbb { A } ^ { r } ) \textrm { - } \{ 0 \} )$de$\mathbf { G L } _ { r } \times \mathbb { G } _ { m } ^ { r - 1 }$plonge par´ 1≤s≤r

$( u , ( \ell _ { t } ) _ { 1 \leq t < r } ) \mapsto \left( \left( \prod _ { t < s } \ \ell _ { t } ^ { ( s - t ) } \right) \cdot \Lambda ^ { s } u \right) _ { 1 \leq s < r }$. Le schema´$\boldsymbol { \Omega } ^ { r , 1 }$verifie les pro-´ priet´ es suivantes :´

(i)$\boldsymbol { \Omega } ^ { r , 1 }$est muni de deux actions à gauche et à droite de$\mathrm { G L } _ { r }$et d’une action du tore$\mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m }$qui commutent entre elles.

(ii)$\boldsymbol { \Omega } ^ { r , 1 }$est muni d’un morphisme equivariant´ (relativement à ces actions et à l’action triviale de$\mathrm { G L } _ { r }$sur$\mathbf { \mathcal { A } } ^ { r , 1 } )$0

$$
\Omega^ {r, 1} \to \mathcal {A} ^ {r, 1}
$$

qui est lisse de dimension relative$r ^ { 2 }$

(iii)$L a f l b r e \mathrm { G r } _ { \varnothing } ^ { r , 1 }$de$\boldsymbol { \Omega } ^ { r , 1 }$au-dessus dupoint unite´ α du tore$\mathcal { A } _ { \varnothing } ^ { r , 1 }$s’identifie à${ \mathrm { G L } } _ { r }$

Et plus gen´ eralement, si´$\underline { { r } } = ( r _ { 1 } , \ldots , r _ { k } ) , r _ { 1 } + \cdot \cdot \cdot + r _ { k } = r ,$, est une partition de l’entier r, la fibre$\mathrm { G r } _ { \underline { { r } } } ^ { r , 1 }$de$\boldsymbol { \Omega } ^ { r , 1 }$au-dessus du point marque´$\alpha _ { \underline { { r } } }$ de l’orbite$\mathcal { A } _ { \underline { { r } } } ^ { r , 1 }$classifie naturellement les familles constituees de´

• une filtration decroissante´$\mathbb { A } ^ { r } = \overline { { F } } _ { 0 } \supset \overline { { F } } _ { 1 } \supset \cdots \supset \overline { { F } } _ { k } = 0$de l’espace vectoriel$\mathbb { A } ^ { r }$de dimension r dont les sous-quotients sont de dimensions $r _ { 1 } , r _ { 2 } , \ldots , r _ { k }$

• une filtration croissante$0 = F _ { 0 } \subsetneq F _ { 1 } \subsetneq \cdots \subsetneq F _ { k } = \mathbb { A } ^ { r }$de$\mathbb { A } ^ { r }$dont les sous-quotients sont de dimensions$r _ { 1 } , r _ { 2 } , \ldots , r _ { k }$

• des isomorphismes$\overline { { F } } _ { e - 1 } / \overline { { F } } _ { e } \stackrel { \sim } {  } F _ { e } / F _ { e - 1 } , 1 \leq e \leq k .$

L’action du tore$\mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m }$sur$\boldsymbol { \Omega } ^ { r , 1 }$est libre. Le schema quotient´$\overline { { \Omega } } ^ { r , 1 }$ est muni de deux actions à droite et à gauche de$\mathrm { P G L } _ { r }$et d’un morphisme lisse de dimension$r ^ { 2 } - 1$sur le “champ torique”$\mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$quotient de la variet´ e torique´$\mathcal { A } ^ { r , 1 } = \mathbb { A } ^ { r - 1 }$par son tore$\mathcal { A } _ { \varnothing } ^ { r , 1 } = \mathbb { G } _ { m } ^ { r - 1 }$. L’ouvert dense de $\overline { { \Omega } } ^ { r , 1 }$image reciproque du point ouvert dense´$\mathcal { A } _ { \varnothing } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$s’identifie à$\mathrm { P G L } _ { r }$ et on montre que$\overline { { \Omega } } ^ { r , 1 }$est projectif.$\mathbf { C } '$est la compactification de De Concini et Procesi de$\bar { \mathrm { P G L } } _ { r } \cong ( \mathrm { P G L } _ { r } \times \mathrm { P G L } _ { r } ) / \mathrm { P G L } _ { r }$

Scindons la suite exacte de tores$1 ~ \to ~ \mathbb { G } _ { m } ^ { 2 } / \mathbb { G } _ { m } ~ \to ~ \mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m } ~ \to ~$ $\mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m } ^ { 2 } \to 1$au moyen de$\mathbb { G } _ { m } ^ { r + 1 } \ \to \ \mathbb { G } _ { m } ^ { 2 } \ : \ ( \lambda _ { i } ) _ { 0 \le i \le r } \ \mapsto \ ( \lambda _ { 0 } , \lambda _ { 1 } \lambda _ { 0 } ^ { - 1 } )$ Cela definit une section´$\mathcal { A } _ { \varnothing } ^ { r , 1 } = \mathbb { G } _ { m } ^ { r - 1 } \cong \mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m } ^ { 2 } \to \mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m }$et donc une action de$\mathcal { A } _ { \varnothing } ^ { r , 1 }$sur$\boldsymbol { \Omega } ^ { r , 1 }$qui est libre et relève celle sur$\mathcal { A } _ { \varnothing } ^ { r , 1 }$. Le schema quo-´ tient$\Omega ^ { r } = \Omega ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$est muni de deux actions à droite et à gauche de${ \mathrm { G L } } _ { r }$ et$\mathrm { d } ^ { \circ } \mathrm { u n }$morphisme lisse de dimension$r ^ { 2 }$sur le champ torique$\mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$et il contient${ \mathrm { G L } } _ { r }$comme ouvert dense.$\mathbf { C } '$est ce$\mathrm { \ q u } ^ { \prime }$on appelle le schema des´ homomorphismes complets.

## b) Le champ des chtoucas iter´ es´

Le schema´$\Omega ^ { r }$des homomorphismes complets de rang r est muni de deux actions à droite et$\grave { \mathbf { a } }$gauche de$\mathrm { G L } _ { r }$commutant entre elles. Cela permet de parler aussi d’homomorphismes complets entre deux fibres localement´ libres de rang r sur un schema. Comme ces deux actions de´${ \mathrm { G L } } _ { r }$respectent le morphisme$\Omega ^ { r } \to \mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \mathcal { A } } ^ { r , 1 }$, tout homomorphisme complet entre fibres´ de rang r sur un schema induit un point du champ torique´$\mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 } =$ $\mathbb { A } ^ { r - 1 } / \mathbb { G } _ { m } ^ { r - 1 } = ( \mathbb { A } ^ { 1 } / \mathbb { G } _ { m } ) ^ { r - 1 }$à valeurs dans ce schema.´

On peut rappeler que le champ quotient$\mathbb { A } ^ { 1 } / \mathbb { G } _ { m }$est le classifiant des fibres´ inversibles munis d’une section globale (pas necessairement inversible).´

Un homomorphisme complet entre deux fibres´$\mathcal { E }$et$\mathcal { F }$localement libres de rang r au-dessus de la donnee de´$r - 1$fibres inversibles´$\mathscr { L } _ { 1 } , \ldots , \mathscr { L } _ { r - 1 }$ munis de sections globales$\ell _ { 1 } , \ldots , \ell _ { r - 1 }$consiste en une famille d’homo-

morphismes partout non nuls

$$
u _ {s}: \Lambda^ {s} \mathcal {E} \otimes \bigotimes_ {t <   s} \mathcal {L} _ {t} ^ {\otimes (s - t)} \longrightarrow \Lambda^ {s} \mathcal {F}, 1 \leq s \leq r,
$$

qui verifient en particulier les relations´

$$
\Lambda^ {s} u _ {1} = \bigg (\prod_ {t <   s} \ell_ {t} ^ {(s - t)} \bigg) u _ {s}, 1 \leq s \leq r.
$$

On notera$\mathcal { E } \Rightarrow \mathcal { F }$les homomorphismes complets entre$\mathcal { E }$et$\mathcal { F }$.

A partir de maintenant, on se refère à nouveau à la courbe´ X projective, lisse et geom´ etriquement connexe sur le corps de base fini à´$q$el´ ements´$\mathbb { F } _ { q }$

Un chtouca iter´ e de rang´ r sur un schema´ S (sur$\mathbb { F } _ { q } )$consiste en

• un fibre´ E localement libre de rang r sur$X \times S$

• une modification (à droite) de$\varepsilon _ { \mathrm { ~ C ~ } } ,$est-à-dire un diagramme

$$
\mathcal {E} \stackrel {j} {\hookrightarrow} \mathcal {E} ^ {\prime} \stackrel {t} {\hookleftarrow} \mathcal {E} ^ {\prime \prime}
$$

où$\mathcal { E } ^ { \prime } , \mathcal { E } ^ { \prime \prime }$sont deux autres fibres de rang´ r sur$X \times S$et$j , t$sont des homomorphismes injectifs dont les conoyaux sont supportes par les´ graphes de deux morphismes “pôle” et${ } ^ { \mathfrak { a } } \mathrm { z e r o } ^ { , \mathfrak { o } } \infty , 0 : \bar { S }  X$et sont inversibles sur$\mathcal { O } _ { S }$

• des fibres inversibles´$\mathscr { L } _ { 1 } , \ldots , \mathscr { L } _ { r - 1 }$sur S munis de sections globales $\ell _ { 1 } , \ldots , \ell _ { r - 1 }$

• un homomorphisme complet

$$
{ } ^ { \tau } \mathcal { E } = ( \mathrm{Id} _ { X } \times \mathrm{Frob} _ { S } ) ^ { * } \mathcal { E } \Longrightarrow \mathcal { E } ^ { \prime \prime }
$$

dont l’image dans$( \mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \mathcal { A } } ^ { r , 1 } ) ( X \times S )$provient via la projection$X \times S$ $S$du point$( ( \mathcal { L } _ { 1 } ^ { q - 1 } , \ell _ { 1 } ^ { q - \widetilde { 1 } } ) , \dots , ( \mathcal { L } _ { r - 1 } ^ { q - 1 } , \ell _ { r - 1 } ^ { q - 1 } ) )$de$( \mathbb { A } ^ { 1 } / \mathbb { G } _ { m } ) ^ { r - 1 } ( S ) =$ $( \mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 } ) ( S )$

Dans la definition, on impose à ces donn´ ees un certain nombre de con-´ ditions ouvertes (voir la definition 3 et le lemme´$^ 6$du paragraphe 1 de [Lafforgue, 1998]) que nous ne recopions pas ici.

On note$\overline { { \mathrm { C h t } ^ { r } } }$le champ classifiant les chtoucas iter´ es de rang´ r. Il est algebrique au sens d’Artin et localement de type fini. Ses groupe´ s$\mathrm { d } ^ { \prime }$automorphismes en tous points sont finis mais attention ! certains ont une partie ramifiee si bien que´$\overline { { \mathrm { C h t } ^ { r } } }$n’est pas algebrique au sens de Deligne-Mumford´ (contrairement à ce qui est dit dans l’introduction de [Lafforgue, 1998]).

A tout chtouca iter´ e´$( \boldsymbol { \mathcal { E } } ; \boldsymbol { \mathcal { E } } \hookrightarrow \boldsymbol { \mathcal { E } } ^ { \prime } \longleftrightarrow \boldsymbol { \mathcal { E } } ^ { \prime \prime } ; \boldsymbol { \mathcal { L } } _ { 1 } , \ldots , \boldsymbol { \mathcal { L } } _ { r - 1 } ; \boldsymbol { \ell } _ { 1 } , \ldots , \boldsymbol { \ell } _ { r - 1 } ;$ $^ { \tau } \mathcal { E } \Longrightarrow \mathcal { E } ^ { \prime \prime } )$, on peut associer d’une part le pôle et le zero de la modification´ $\mathcal { E } \hookrightarrow \mathcal { E } ^ { \prime } \hookrightarrow \mathcal { E } ^ { \prime \prime }$et d’autre part la famille des fibres inversibles munis de´ sections$( { \mathcal { L } } _ { 1 } , \ell _ { 1 } ) , \ldots , ( { \mathcal { L } } _ { r - 1 } , \ell _ { r - 1 } )$. Cela definit deux morphismes´

$$
\begin{array}{c} (\infty , 0): \overline {{\mathrm{Cht} ^ {r}}} \to X \times X \\ \text { et } \qquad \overline {{\mathrm{Cht} ^ {r}}} \to \mathcal {A} ^ {r, 1} / \mathcal {A} _ {\emptyset} ^ {r, 1}. \end{array}
$$

L’image reciproque du point ouvert dense´$\mathcal { A } _ { \varnothing } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$de$\mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$est le champ Cht<sup>r</sup> des chtoucas de rang r.

Le champ$\overline { { \mathrm { C h t } ^ { r } } }$n’est pas separ´ e. Cela rend possible l’´ enonc´ e suivant qui´ est le resultat principal de l’article [Lafforgue, 1998] :´

Theor´ eme III.2.\` – Pour tout entier$d \in \mathbb { Z }$et tout polygone de troncature $p : [ 0 , r ] \to \mathbb { R } _ { + }$assez convexe (en fonction de la courbe X), il existe dans le champ$\overline { { \mathrm { C h t } ^ { r } } }$des chtoucas iter´ es de rang r un ouvert´$\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \le p } } }$tel que

(i) le morphisme${ \overline { { \operatorname { C h t } ^ { r , d , \overline { { p } } } \leq p } } } \to X \times X$est propre (en particulier separ´ e et´ de type fini),

(ii) le morphisme$\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } } } \to X \times X \times \mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$est lisse de dimension relative$2 r - 2 ,$

(iii) l’intersection$\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } \cap \mathrm { C h t } ^ { r }$est le champ$\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p }$des chtoucas de rang r, de degre d et dont le polygone canonique ´$\overline { { p } }$est majore par p.´!"

Le champ$\overline { { \mathrm { C h t } ^ { r } } }$est muni d’une action par produit tensoriel du groupe de Picard de X identifie à´$F ^ { \times } \backslash \mathbb { A } ^ { \times } / O _ { \mathbb { A } } ^ { \times }$qui stabilise les ouverts${ \overline { { \mathrm { C h t } ^ { r , { \overline { { p } } } } } } } \leq p  =$ $\prod \overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } } }$ d∈Z

Pour$a \in \mathbb { A } ^ { \times }$un idèle de degre non nul, on dispose donc de´

$$
\overline {{\mathrm{Cht} ^ {r , \overline {{p}} \leq p}}} / a ^ {\mathbb {Z}} \cong \coprod_ {1 \leq d \leq r | \deg (a) |} \overline {{\mathrm{Cht} ^ {r , d , \overline {{p}} \leq p}}}
$$

qui est une compactification de$\mathrm { C h t } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$lisse sur$X \times X \times \mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \mathcal { A } } ^ { r , 1 }$

## c) Description des strates de bord

Pour$d \in \mathbb { Z }$un degre et´$p : [ 0 , r ] \to \mathbb { R } _ { + }$un polygone de troncature (assez convexe en fonction de X), nous rappelons comment decrire les strates de´ bord de la compactification$\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p }$de$\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p }$

Dans la variet´ e torique´$\mathcal { A } ^ { r , 1 } = \mathbb { A } ^ { r , 1 }$, les orbites du tore$\mathcal { A } _ { \varnothing } ^ { r , 1 } = \mathbb { G } _ { m } ^ { r - 1 }$sont indexees par les partitions´$\underline { { r } } = ( r _ { 1 } , \ldots , r _ { k } )$de l’entier r et sont notees´$\mathcal { A } _ { \underline { { r } } } ^ { r , 1 }$ l’adherence´$\overline { { \mathcal { A } _ { \underline { { r } } } ^ { r , 1 } } }$de chaque$\mathcal { A } _ { \underline { { r } } } ^ { r , 1 }$est la reunion disjointe des´$\mathcal { A } _ { \underline { { r } } ^ { \prime } } ^ { r , 1 }$quand$\underline { { r } } ^ { \prime }$ decrit l’ensemble des partitions de´ r qui raffinent$\underline { { r } } .$

Comme$\overline { { \mathrm { C h t } ^ { r , d , \overline { { { p } } } \le p } } }$est lisse sur$X \times X \times { \mathcal { A } } ^ { r , 1 } / { \mathcal { A } } _ { \mathcal { Y } } ^ { r , 1 }$, on voit que pour toute partition$\underline { { r } } = ( r _ { 1 } , \ldots , r _ { k } )$de r, l’image reciproque´$\mathrm { C h t } _ { \underline { { r } } } ^ { r , d , \overline { { p } } \leq p }$de$\mathcal { A } _ { \underline { { r } } } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$ dans$\overline { { \mathrm { C h t } ^ { r , d , \overline { { { p } } } \leq p } } }$est lisse sur$X \times X$de dimension$2 r - k - 1 ; { \mathrm { i l } }$en est de même de son adherence´$\mathrm { C h t } _ { \underline { { r } } } ^ { r , d , \overline { { p } } \leq p }$qui est l’image reciproque de´$\overline { { \mathcal { A } _ { \underline { { r } } } ^ { r , 1 } } } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$ et aussi la reunion disjointe des´$\mathrm { C h t } _ { \underline { { r } } ^ { \prime } } ^ { r , d , \overline { { p } } \leq p }$quand$\underline { { r } } ^ { \prime }$decrit l’ensemble des´ partitions de r qui raffinent$\underline { { r } } .$

Modifiant legèrement les notations de [Lafforgue, 1998], on d´ esigne par´ $\mathrm { C h t } ^ { r }$le produit fibre´

$$
\mathrm{Cht} ^ {r} = \mathrm{Cht} ^ {r _ {1}} \times_ {X} ^ {r _ {2}} \mathrm{Cht} \times \dots \times_ {X} ^ {r _ {k}} \mathrm{Cht};
$$

il classifie les familles constituees d’un chtouca à droite de rang´$r _ { 1 }$et de $k - 1$chtoucas à gauche de rangs$r _ { 2 } , \ldots , r _ { k }$tels que le zero de chacun se´ confonde avec le pôle du suivant.

On note encore$\underline { { r } } ^ { - } = \{ 0 , r _ { 1 } , \dots , r _ { 1 } + \dots + r _ { k - 1 } \} \mathrm { ~ e t } \underline { { r } } ^ { + } = \{ r _ { 1 } , r _ { 1 } + r _ { 2 }$ $\dots , r _ { 1 } + \dots + r _ { k } = r \}$. Tout élément s de$\underline { { r } } ^ { - } \mathrm { ~ a ~ }$un successeur$s ^ { + } \in \underline { { r } } ^ { + }$et tout el´ ement´ s de$\underline { { r } } ^ { + }$a un pred´ ecesseur´$s ^ { - } \in \underline { { r } } ^ { - }$

On designe par´$\widetilde { \mathrm { C h t } } ^ { \underline { { { r } } } }$le champ qui à tout schema´ S sur$\mathbb { F } _ { q }$associe le "groupoïde des familles$( ( \widetilde { \mathscr { E } } _ { s } ) _ { s \in \underline { { r } } ^ { + } } , ( \mathscr { L } _ { s } ) _ { s \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + } } )$où :

$\widetilde { \pmb { \mathscr { E } } } _ { r _ { 1 } } = ( \pmb { \mathscr { E } } _ { r _ { 1 } } \hookrightarrow \pmb { \mathscr { E } } _ { r _ { 1 } } ^ { \prime } \smile \tau \pmb { \mathscr { E } } _ { r _ { 1 } } )$est un chtouca à droite de rang$r _ { 1 }$,

• pour$s > r _ { 1 } , \tilde { \mathcal { E } } _ { s } = ( \mathcal { E } _ { s } \longleftrightarrow \mathcal { E } _ { s } ^ { \prime } \hookrightarrow { } ^ { \tau } \mathcal { E } _ { s } )$est un chtouca à gauche de rang $s - s ^ { - }$

• les$\mathcal { L } _ { s }$sont des fibres inversibles sur´ S munis d’isomorphismes sur$X \times S$

$$
{ } ^ { \tau } \mathcal { E } _ { s ^ { + } } / \mathcal { E } _ { s ^ { + } } ^ { \prime } \cong \left\{ \begin{array} { l l } \left( \mathcal { E } _ { r _ { 1 } } ^ { \prime } / { } ^ { \tau } \mathcal { E } _ { r _ { 1 } } \right) \otimes { } ^ { \tau } \mathcal { L } _ { r _ { 1 } } & \text {~ si~ } s = r _ { 1} , \\ \left( \mathcal { E } _ { s } / \mathcal { E } _ { s } ^ { \prime } \right) \otimes { } ^ { \tau } \mathcal { L } _ { s } & \text {~ si~ } s > r _ { 1} . \end{array} \right.
$$

Si$\mathbf { B } \mathbb { G } _ { m }$designe le champ classifiant du tore´$\mathbb { G } _ { m }$, le champ$\widetilde { \mathrm { C h t } } ^ { \underline { { r } } }$s’inscrit dans un carre cart´ esien´

![](images/page_63_image_11.jpg)

où la flèche verticale de droite associe à toute famille de chtoucas$( \widetilde { \mathcal { E } } _ { s } ) _ { s \in \underline { { r } } ^ { + } }$ comme ci-dessus la famille de fibres inversibles sur´ S

$$
\left\{ \begin{array}{l} \left(^ {\tau} \mathcal {E} _ {r _ {1} ^ {+}} / \mathcal {E} _ {r _ {1} ^ {+}} ^ {\prime}\right) \otimes \left(\mathcal {E} _ {r _ {1}} ^ {\prime} / ^ {\tau} \mathcal {E} _ {r _ {1}}\right) ^ {- 1} \\ \left(^ {\tau} \mathcal {E} _ {s ^ {+}} / \mathcal {E} _ {s ^ {+}} ^ {\prime}\right) \otimes \left(\mathcal {E} _ {s} / \mathcal {E} _ {s} ^ {\prime}\right) ^ {- 1}, s \in \underline {{r}} ^ {-}, s > r _ {1}. \end{array} \right.
$$

Le morphisme$\widetilde { \mathrm { C h t } } ^ { \underline { { { r } } } } \to \mathrm { C h t } ^ { \underline { { { r } } } } .$, qui se deduit de´$\mathbf { B } { \mathbb { G } _ { m } ^ { k - 1 } } \xrightarrow { \mathrm { F r o b } } \mathbf { B } { \mathbb { G } _ { m } ^ { k - 1 } }$par "changement de base, est un morphisme de gerbe dont le groupe de structure est le noyau$\mathbb { G } _ { m } ^ { k - 1 } [ \tau ]$de$\mathbb { G } _ { m } ^ { k - 1 } \xrightarrow [ m ] { \mathrm { F r o b } } \mathbb { G } _ { m } ^ { k - 1 }$lequel est fini et radiciel.

D’après les propositions 7 et 9 du paragraphe 1 de [Lafforgue, 1998], on a :

Proposition III.3. – Etant donnes d un entier et´$p : [ 0 , r ] \to \mathbb { R } _ { + }$un polygone assez convexe (en fonction de X), associons à tout entier$r ^ { \prime } ,$ $0 \leq r ^ { \prime } \leq r$, l’unique entier$d ( \boldsymbol { r } ^ { \prime } )$tel que

$$
d (r ^ {\prime}) - \frac {r ^ {\prime}}{r} d \in ] p (r ^ {\prime}) - 1,   p (r ^ {\prime}) ].
$$

Alors, pour toute partition$\underline { { r } } = ( r _ { 1 } , \ldots , r _ { k } )$de r, la strate$\mathrm { C h t } _ { \underline { { r } } } ^ { r , d , \overline { { p } } \leq p }$ s’ecrit naturellement comme une gerbe dont le groupe de struct´ ure est plat, fini et radiciel sur l’ouvert$\widetilde { \mathrm { C h t } } ^ { { \underline { { r } } } , d , \overline { { p } } \leq p } d e \widetilde { \mathrm { C h t } } ^ { \underline { { r } } }$image reciproque de l’ouvert´ $\mathbf { \mathop { C h t } } ^ { r , d , \overline { { p } } \leq p }$" "de Chtr classifiant les familles de chtoucas$\widetilde { \mathcal { E } } _ { 1 } , \ldots , \widetilde { \mathcal { E } } _ { k }$de rangs $r _ { 1 } , r _ { 2 } , \ldots , r _ { k }$qui verifient :´

• Le chtouca à droite$\widetilde { \mathcal { E } } _ { 1 } \ = \ ( \mathcal { E } _ { 1 } \ \hookrightarrow \ \mathcal { E } _ { 1 } ^ { \prime } \ \longleftrightarrow \ ^ { \tau } \mathcal { E } _ { 1 } )$est de degre´$d _ { 1 } \ =$ $d ( r _ { 1 } )$et ses sous-objets$( \mathcal { F } \hookrightarrow \mathcal { F } ^ { \prime } \hookrightarrow \mathit { \bar { \tau } } _ { \mathcal { F } } )$sont de degres´ deg$( \mathcal { F } ) \leq$ $\begin{array} { r } { p ( \mathbf { r g } \mathcal { F } ) + \frac { \mathbf { r g } \mathcal { F } } { r } d } \end{array}$; autrement dit, son polygone canonique est majore par´ $\begin{array} { r } { r ^ { \prime } \mapsto p _ { 1 } ( r ^ { \prime } ) = d ( r ^ { \prime } ) - \frac { r ^ { \prime } } { r _ { 1 } } d ( r _ { 1 } ) , 0 \leq r ^ { \prime } \leq r _ { 1 } . } \end{array}$

• Pour$\begin{array} { r } { 1 \ < \ e \ \le \ k , } \end{array}$, le chtouca à gauche$\widetilde { \mathcal { E } } _ { e } \ = \ ( \mathcal { E } _ { e } \ \longleftrightarrow \ \mathcal { E } _ { e } ^ { \prime } \ \hookrightarrow \ ^ { \tau } \mathcal { E } _ { e } )$ est de degre´$d ( r _ { 1 } + \cdot \cdot \cdot + r _ { e } ) - d ( r _ { 1 } + \cdot \cdot \cdot + r _ { e - 1 } )$et ses sous-objets $( \mathcal { F } \hookrightarrow \mathcal { F } ^ { \prime } \hookrightarrow \tau _ { \mathcal { F } ) }$sont de degres´ deg$( { \mathcal { F } } ) \leq p ( r _ { 1 } + \cdot \cdot \cdot + r _ { e - 1 } + \arg { \mathcal { F } } ) +$ $\textstyle { \frac { r _ { 1 } + \dots + r _ { e - 1 } + \arg { \mathcal { F } } } { r } } d - d ( r _ { 1 } + \cdot \cdot \cdot + r _ { e - 1 } ) - 1$quand deg$( \mathcal { F } ) = \deg ( \mathcal { F } ^ { \prime } )$et de degres´ deg$\begin{array} { r } { ( \mathcal { F } ) \leq p ( r _ { 1 } + \cdot \cdot \cdot + r _ { e - 1 } + \mathrm { r g } \mathcal { F } ) + \frac { r _ { 1 } + \cdots + r _ { e - 1 } + \mathrm { r g } \mathcal { F } } { r } d - d ( r _ { 1 } + } \end{array}$ $\cdots + r _ { e - 1 } )$quand deg$( \mathcal { F } ) = \deg ( \mathcal { F } ^ { \prime } ) + 1$. Autrement dit, le chtouca à droite associe´$( \mathcal { E } _ { e } ^ { \prime } \hookrightarrow \tau \mathcal { E } _ { e } \smile \tau \bar { \mathcal { E } } _ { e } ^ { \prime } )$est de degre´$d _ { e } = d ( r _ { 1 } + \cdot \cdot \cdot + r _ { e } )$ $- d ( r _ { 1 } + \cdot \cdot \cdot + r _ { e - 1 } ) - 1$et son polygone canonique est majore par´ $r ^ { \prime } \mapsto p _ { e } ( r ^ { \prime } ) = d ( r _ { 1 } + \cdot \cdot \cdot + r _ { e - 1 } + r ^ { \prime } ) - d ( r _ { 1 } + \cdot \cdot \cdot + r _ { e - 1 } ) - 1 -$ $\begin{array} { r } { \frac { r ^ { \prime } } { r _ { e } } ( d ( r _ { 1 } + \cdot \cdot \cdot + r _ { e } ) - d ( r _ { 1 } + \cdot \cdot \cdot + r _ { e - 1 } ) - 1 ) , 1 \le r ^ { \prime } \le r _ { e } . } \end{array}$!"

Pour tout entier$r ^ { \prime } \geq 1$, le morphisme

$$
{ } ^ { r ^ { \prime } } \mathrm{Cht} \rightarrow \mathrm{Cht} ^ { r ^ { \prime } } : ( \mathcal { E } \hookleftarrow \mathcal { E } ^ { \prime } \hookrightarrow { } ^ { \tau } \mathcal { E } ) \mapsto ( \mathcal { E } ^ { \prime } \hookrightarrow { } ^ { \tau } \mathcal { E } \hookleftarrow { } ^ { \tau } \mathcal { E } ^ { \prime } )
$$

est representable, fini, surjectif et radiciel et il s’inscrit dans u´ n carre com-´ mutatif :

$$
\begin{array}{c c c} ^ {r ^ {\prime}} \text {Cht} & \longrightarrow & \text {Cht} ^ {r ^ {\prime}} \\ (\infty , 0) \Big \downarrow & & \Big \downarrow (\infty , 0) \\ X \times X & \xrightarrow {\operatorname{Id} _ {X} \times \operatorname{Frob} _ {X}} & X \times X \end{array}
$$

On obtient donc :

Corollaire III.4. – Dans la situation et avec les notations de la proposition III.3, on a pour toute partition non triviale$\underline { { r } } = ( r _ { 1 } , \ldots , r _ { k } )$de l’entier r un morphisme naturel

$$
\operatorname{Cht} _ {r} ^ {r, d, \overline {{p}} \leq p} \rightarrow \operatorname{Cht} ^ {r _ {1}, d _ {1}, \overline {{p}} \leq p _ {1}} \times_ {X} \operatorname{Cht} ^ {r _ {2}, d _ {2}, \overline {{p}} \leq p _ {2}} \times_ {X, \text { Frob }} \dots \times_ {X, \text { Frob }} \operatorname{Cht} ^ {r _ {k}, d _ {k}, \overline {{p}} \leq p _ {k}}
$$

au-dessus de l’endomorphisme Id × Frob de$X \times X \ ; c ^ { \prime } e s t$le compose´ d’un morphisme de gerbe dont le groupe de structure est plat,fini et radiciel et d’un morphisme representable, fini, surjectif et radiciel.´!"

## 2) Le morphisme de restriction associe à un niveau´

A partir de maintenant, on fixe un niveau c’est-à-dire un sous-schema ferm´ e´ fini$N = \operatorname { S p e c } { \mathcal { O } } _ { N }$de la courbe X.

## a) Definition et propri´ et´ es´

Soit$\overline { { \mathcal { C } } } ^ { r , N }$le champ qui associe à tout schema´$S \ ( \operatorname { s u r } \mathbb { F } _ { q } )$le groupoïde des familles constituees de´

• trois$\mathcal { O } _ { N \times S } – \mathbf { M o d u l }$les$\mathcal { F } , \mathcal { F } ^ { \prime }$et$\mathcal { F } ^ { \prime \prime }$localement libres de rang r sur$N \times S$

• deux homomorphismes de$\mathcal { O } _ { N \times S ^ { - } } \mathrm { M o d u l e s }$s$\mathcal { F } \ \stackrel { j } { \to } \ \mathcal { F } ^ { \prime }$et$\mathcal { F } ^ { \prime \prime } \stackrel { t } { \to } \mathcal { F } ^ { \prime }$ dont les conoyaux admettent localement sur S un gen´ erateur comme´ ${ \mathcal { O } } _ { S ^ { - } } \mathbf { M o d u l e } { \mathrm { : } }$s,

• des fibres inversibles´$\mathscr { L } _ { 1 } , \ldots , \mathscr { L } _ { r - 1 }$sur S munis de sections globales $\ell _ { 1 } , \ldots , \ell _ { r - 1 }$

• un homomorphisme complet

$$
{ } ^ { \tau } \mathcal { F } = ( \mathrm{Id} _ { N } \times \mathrm{Frob} _ { S } ) ^ { * } \mathcal { F } \Longrightarrow \mathcal { F } ^ { \prime \prime }
$$

dont l’image dans$( \mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \mathcal { A } } ^ { r , 1 } ) ( X \times S )$provient via la projection$N \times S$ $S$du point$( ( \mathcal { L } _ { 1 } ^ { q - 1 } , \ell _ { 1 } ^ { q - 1 } ) , \dots , ( \mathcal { L } _ { r - 1 } ^ { q - 1 } , \ell _ { r - 1 } ^ { q - 1 } ) )$de$( \mathbb { A } ^ { 1 } / \mathbb { G } _ { m } ) ^ { r - 1 } ( S ) =$ $( \mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 } ) ( S )$

Le champ$\overline { { \mathcal { C } } } ^ { r , N }$est algebrique au sens d’Artin. Il est muni´$\mathrm { d } ^ { \prime }$un morphisme sur$\mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$qui est lisse puisque le schema´$\Omega ^ { r }$des homomorphismes complets est lisse sur$\mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \mathcal { A } } ^ { r , 1 } = \mathbb { A } ^ { r - 1 } / \mathbb { G } _ { m } ^ { r - 1 }$. On peut remarquer que l’image reciproque par ce morphisme de structure du point ouvert dens ´ e $\mathcal { A } _ { \varnothing } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$n’est autre que le champ$\overline { { \mathcal { C } } } _ { \varnothing } ^ { r , N }$introduit dans le paragraphe 1a du chapitre II.

Les foncteurs

$$
(\mathcal {E} \hookrightarrow \mathcal {E} ^ {\prime} \leftarrow \mathcal {E} ^ {\prime \prime}, ^ {\tau} \mathcal {E} \Longrightarrow \mathcal {E} ^ {\prime \prime}) \mapsto
$$

$$
\left(\mathcal {E} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N} \rightarrow \mathcal {E} ^ {\prime} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N} \leftarrow \mathcal {E} ^ {\prime \prime} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N}, ^ {\tau} \mathcal {E} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N} \Longrightarrow \mathcal {E} ^ {\prime \prime} \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N}\right)
$$

induisent des morphismes

$$
\begin{array}{c} \overline {{\mathrm{Cht} ^ {r}}} \longrightarrow \overline {{\mathcal {C}}} ^ {r, N} \\ \overline {{\mathrm{Cht} ^ {r , d , \overline {{p}} \leq p}}} \longrightarrow \overline {{\mathcal {C}}} ^ {r, N} \end{array}
$$

qui commutent avec les morphismes de structure sur$\mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$. On les appellera morphismes de restriction des chtoucas iter´ es à´ N.

En associant à tout point$( \mathcal { F } \stackrel { j } { \longrightarrow } \mathcal { F } ^ { \prime } \stackrel { \iota } { \longleftarrow } \mathcal { F } ^ { \prime \prime } ; \mathcal { L } _ { 1 } , \ldots , \mathcal { L } _ { r - 1 } ; \ell _ { 1 } , \ldots ,$ $\ell _ { r - 1 } ; \tau \mathcal { F } \Longrightarrow \mathcal { F } ^ { \prime \prime } )$les determinants de´ j et t, on definit un morphisme´

$$
\overline {{\mathcal {C}}} ^ {r, N} \to \left(\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}\right) ^ {2}
$$

où$\mathbb { A } ^ { N }$et$\mathbb { G } _ { m } ^ { N }$designent les sch´ emas d´ eduits de´$\mathbb { A } ^ { 1 }$et$\mathbb { G } _ { m }$par restriction des scalaires à la Weil de$\mathcal { O } _ { N } \hat { \textmd a } \mathbb { F } _ { q }$

Par ailleurs, on rappelle que N plonge diagonalement dans´$X \times N$et vu comme diviseur de Cartier definit un morphisme´

$$
X \to \mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}
$$

qui est lisse de dimension relative 1.

Il est clair que les carres´

$$
\begin{array}{c c c} \overline {{\mathbf {C h t} ^ {r , d , \overline {{p}} \leq p}}} & \stackrel {{\cdot \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N}}} {{\longrightarrow}} & \overline {{\mathfrak {C}}} ^ {r, N} \\ (\infty , 0) \Big \downarrow & & \Big \downarrow \\ X \times X & \longrightarrow & \left(\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}\right) ^ {2} \end{array}
$$

sont commutatifs.

Nous allons prouver :

Proposition III.5. – Si le polygone de troncature p est assez convexe en fonction (de$X e t )$de N, le morphisme

$$
\overline {{\mathrm{Cht} ^ {r , d , \overline {{p}} \leq p}}} \rightarrow \overline {{\mathcal {C}}} ^ {r, N} \times_ {\left(\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}\right) ^ {2}} (X \times X)
$$

est lisse de dimension relative$2 r - 2$

Demonstration :´ Nous savons dejà d’après le lemme II.1 que pour tout´ entier$r ^ { \prime } \leq r$les morphismes de restriction à N

$$
\begin{array}{l} \operatorname{Cht} ^ {r ^ {\prime}} \longrightarrow \overline {{\mathcal {C}}} _ {\emptyset} ^ {r ^ {\prime}, N} \times_ {\left(\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}\right) ^ {2}} (X \times X) \\ ^ {r ^ {\prime}} \operatorname{Cht} \longrightarrow^ {r ^ {\prime}} \overline {{\mathcal {C}}} _ {\emptyset} ^ {N} \times_ {\left(\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}\right) ^ {2}} (X \times X) \end{array}
$$

sont lisses de dimension relative$2 r ^ { \prime } - 2$

En utilisant la proposition III.3, nous allons voir au paragraphe suivant que cela implique le resultat annonc´ e.´!"

## b) Verification de ce que le morphisme de restriction est lisse´

Demontrons la proposition III.5.´

Les champs$\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } } } \operatorname { e t } \overline { { \mathfrak { C } } } ^ { r , N }$sont lisses sur$\mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$et$X \times X$est lisse sur$( \mathbb { A } ^ { N } / ( \mathbb { G } _ { m } ^ { N } ) ^ { 2 }$. En notant$\overline { { \mathcal { C } } } _ { \underline { { r } } } ^ { r , N }$les fibres de$\overline { { \mathcal { C } } } ^ { r , N }$au-dessus des strates $\mathcal { A } _ { r } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$de$\mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$, il suffit donc de prouver que pour toute partition$\underline { r }$ de l’entier$r ,$, le morphisme

$$
\mathrm{Cht} _ {\underline {{r}}} ^ {r, d, \overline {{p}} \leq p} \rightarrow \overline {{\mathcal {C}}} _ {\underline {{r}}} ^ {r, N} \times_ {\left(\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}\right) ^ {2}} (X \times X)
$$

est lisse de dimension relative$2 r - 2 .$

Fixons une telle partition$\underline { { r } } ~ = ~ ( r _ { 1 } , \ldots , r _ { k } )$et considerons les points´ $( \mathcal { F } \to \mathcal { F } ^ { \prime }  \mathcal { F } ^ { \prime \prime } ; \mathcal { L } _ { 1 } , \dotsc , \mathcal { L } _ { r - 1 } ; \ell _ { 1 } , \dotsc , \ell _ { r - 1 } ; ^ { \tau } \mathcal { F } \Longrightarrow \mathcal { F } ^ { \prime \prime } )$du champ $\overline { { \mathcal { C } } } _ { r } ^ { r , N }$à valeurs dans les schemas´ S sur$\mathbb { F } _ { q } .$. Pour tout$s \notin \underline { { r } } ^ { + }$, on peut identifier$\mathcal { L } _ { s }$muni de la section inversible$\ell _ { s }$au fibre canonique´$\mathcal { O } _ { S }$muni de la section 1. Et l’homomorphisme complet$\tau _ { \mathcal { F } } \Longrightarrow \mathcal { F } ^ { \prime \prime }$consiste en la donnee de´

• une filtration croissante$0 = { \mathcal { F } } _ { 0 } ^ { \prime \prime } \subsetneq \cdots \subsetneq { \mathcal { F } } _ { s } ^ { \prime \prime } \subsetneq \cdots \subsetneq { \mathcal { F } } _ { r } ^ { \prime \prime } = { \mathcal { F } } ^ { \prime \prime }$de$\mathcal { F } ^ { \prime \prime }$ par des$\mathcal { O } _ { N \times S ^ { - } } \mathbf { M }$odules$\mathcal { F } _ { s } ^ { \prime \prime }$localement libres de rangs s,$s \in \underline { { r } } ^ { - } \cup \underline { { r } } ^ { + }$ tels que les quotients$\mathcal { F } ^ { \prime \prime } / \mathcal { F } _ { s } ^ { \prime \prime }$soient aussi localement libres,

• une filtration decroissante´$\boldsymbol { \tau } _ { \mathcal { F } } = \overline { { \mathcal { F } } } _ { 0 } \nsupseteq \cdots \supset \overline { { \mathcal { F } } } _ { s } \supset \cdots \supset \overline { { \mathcal { F } } } _ { r } = 0$de $\tau _ { \mathcal { F } }$par des O -Modules$\mathcal { F } _ { s }$localement libres,$s \in \underline { { r } } ^ { - } \cup \underline { { r } } ^ { + }$, tels que les quotients$\overline { { \mathcal { F } } } / \overline { { \mathcal { F } } } _ { s }$soient localement libres de rangs s,

• une famille d’isomorphismes

$$
\overline{\mathcal{F}}_{s^{-}} / \overline{\mathcal{F}}_{s}\otimes^{\tau}\Bigl (\bigotimes_{\substack{t\in \underline{r}^{+}\\ t <   s}}\mathcal{L}_{t}\Bigr)\xrightarrow{\sim}\mathcal{F}_{s} / \mathcal{F}_{s^{-}}\otimes \Bigl (\bigotimes_{\substack{t\in \underline{r}^{+}\\ t <   s}}\mathcal{L}_{t}\Bigr),s\in \underline{r}^{+}  .
$$

On note$\widetilde { \mathcal { C } } _ { \underline { { r } } } ^ { r , N }$le sous-champ ouvert de$\overline { { \mathcal { C } } } _ { \underline { { r } } } ^ { r , N }$qui est defini par les trois´ conditions suivantes :

(i) Chaque$\mathcal { F } _ { s } ^ { \prime } = \mathcal { F } _ { s } ^ { \prime \prime } , s \in \underline { { r } } ^ { - }$, est plonge dans´${ \mathcal { F } } ^ { \prime }$via$\mathcal { F } ^ { \prime \prime }  \mathcal { F } ^ { \prime }$et les quotients$\bar { \mathcal { F } } ^ { \prime } / \mathcal { F } _ { s } ^ { \prime }$sont localement libres de rangs$r \mathrm { ~ - ~ } s$

(ii) Notant aussi$\mathcal { F } _ { r } ^ { \prime } = \mathcal { F } ^ { \prime }$, chaque$\mathcal { F } _ { s } ^ { \prime } , s \in \underline { { r } } ^ { + } , \mathrm { s } ^ { \ast } \mathrm { e n v o i e }$surjectivement sur$\operatorname { C o k e r } ( \mathcal { F } \stackrel { \cdot } {  } \mathcal { F } ^ { \prime } )$si bien que les images reciproques´$\mathcal { F } _ { s }$des$\mathcal { F } _ { s } ^ { \prime }$ via$\mathcal { F }  \mathcal { F } ^ { \prime }$(et aussi$\mathcal { F } _ { 0 } = 0 )$sont localement libres ainsi que les quotients$\mathcal { F } / \mathcal { F } _ { s }$

(iii) Pour tout$s \in \underline { { r } } ^ { + }$, on a

$$
\overline {{\mathcal {F}}} _ {s ^ {-}} + ^ {\tau} \mathcal {F} _ {s} = ^ {\tau} \mathcal {F}
$$

et$\tau _ { \mathcal { F } / ( \overline { { \mathcal { F } } } _ { s } + } \tau _ { \mathcal { F } _ { s } } )$admet un gen´ erateur comme´${ \mathcal { O } } _ { S ^ { - } } \mathbf { M o d u l e }$localement sur S.

Ces conditions ouvertes sont le reflet dans N de celles introduites dans le lemme 6 du paragraphe 1c de [Lafforgue, 1998] pour definir les chtoucas´ iter´ es. Cela signifie que le morphisme de restriction à´ N

$$
\mathrm{Cht} _ {\underline {{r}}} ^ {r, d, \overline {{p}} \leq p} \to \overline {{\mathcal {C}}} _ {\underline {{r}}} ^ {r, N}
$$

se factorise à travers l’ouvert$\widetilde { \mathcal { C } } _ { \underline { { r } } } ^ { r , N }$

Continuons notre description des points de$\widetilde { \mathcal { C } } _ { \underline { { r } } } ^ { r , N }$

On note$\mathcal { A } _ { r _ { 1 } } = \mathcal { F } _ { r _ { 1 } }$et$\mathcal { A } _ { r _ { 1 } } ^ { \prime } = \mathcal { F } _ { r _ { 1 } } ^ { \prime } = \mathcal { F } _ { r _ { 1 } } ^ { \prime \prime }$. Ils sont munis des homomorphismes$\mathcal { A } _ { r _ { 1 } } \to \mathcal { A } _ { r _ { 1 } } ^ { \prime } \mathrm { ~ e t ~ } ^ { \tau } \mathcal { A } _ { r _ { 1 } } \to { } ^ { \tau } \mathcal { F } / \overline { { \mathcal { F } } } _ { r _ { 1 } } \overset { \sim } { \to } \mathcal { F } _ { r _ { 1 } } ^ { \prime \prime } = \mathcal { A } _ { r _ { 1 } } ^ { \prime } .$

Et pour$s \in \underline { { r } } ^ { + } , s \textgreater r _ { 1 } = 0 ^ { + }$, on note$\mathcal { A } _ { s } = \mathcal { F } _ { s } / \mathcal { F } _ { s ^ { - } } = \mathcal { F } _ { s } ^ { \prime } / \mathcal { F } _ { s ^ { - } } ^ { \prime }$ et${ \mathcal A } _ { s } ^ { \prime } = \overline { { \mathcal F } } _ { s ^ { - } } \cap { } ^ { \tau } \mathcal F _ { s } = \mathrm { K e r } [ \overline { { \mathcal F } } _ { s ^ { - } } \oplus { } ^ { \tau } \mathcal F _ { s } \to { } ^ { \tau } \mathcal F ] .$. Ce sont des${ \mathcal { O } } _ { N \times S ^ { - } }$ Modules localement libres de rangs$s - s ^ { - }$et ils sont munis d’homomorphismes$\mathcal { A } _ { s } ^ { \prime } = \overline { { \mathcal { F } } } _ { s ^ { - } } \cap \{ \mathcal { F } _ { s } \  \ ^ { \tau } \mathcal { F } _ { s } / ^ { \tau } \mathcal { F } _ { s ^ { - } } = ^ { \tau } \mathcal { A } _ { s }$et$\mathcal { A } _ { s } ^ { \prime } \otimes \tau \big ( \bigotimes \mathcal { L } _ { t } \big )$

$$
\overline{\mathcal{F}}_{s^{-}} / \overline{\mathcal{F}}_{s}\otimes {}^{\tau}\bigg(\bigotimes_{\substack{t\in \underline{r}^{+}\\ t <   s}}\mathcal{L}_{t}\bigg)\xrightarrow{\sim}\mathcal{F}_{s}^{\prime \prime} / \mathcal{F}_{s^{-}}^{\prime \prime}\otimes \bigg(\bigotimes_{\substack{t\in \underline{r}^{+}\\ t <   s}}\mathcal{L}_{t}\bigg)\to \mathcal{A}_{s}\otimes \bigg(\bigotimes_{\substack{t\in \underline{r}^{+}\\ t <   s}}\mathcal{L}_{t}\bigg).
$$

De plus, pour$s \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + }$, on a des isomorphismes canoniques

et

$$
\begin{array}{l}\det \left(\overline {{\mathcal {F}}} _ {s} \oplus {} ^ {\tau} \mathcal {F} _ {s} \rightarrow {} ^ {\tau} \mathcal {F}\right)\\\cong \det \left(\left(\overline {{\mathcal {F}}} _ {s} \oplus {} ^ {\tau} \mathcal {F} _ {s}\right) \oplus \left(\overline {{\mathcal {F}}} _ {s} \cap {} ^ {\tau} \mathcal {F} _ {s ^ {+}}\right)\rightarrow \left(\overline {{\mathcal {F}}} _ {s} \oplus {} ^ {\tau} \mathcal {F} _ {s ^ {+}}\right)\right)\\\cong \det \left(\overline {{\mathcal {F}}} _ {s} \cap {} ^ {\tau} \mathcal {F} _ {s ^ {+}} \rightarrow {} ^ {\tau} \mathcal {F} _ {s ^ {+}} / {} ^ {\tau} \mathcal {F} _ {s}\right)\\\cong \det \left(\mathcal {A} _ {s ^ {+}} ^ {\prime} \rightarrow {} ^ {\tau} \mathcal {A} _ {s ^ {+}}\right)\\\det \left(\overline {{\mathcal {F}}} _ {s} \oplus {} ^ {\tau} \mathcal {F} _ {s} \rightarrow {} ^ {\tau} \mathcal {F}\right)\\\cong \det \left(\left(\overline {{\mathcal {F}}} _ {s} \oplus {} ^ {\tau} \mathcal {F} _ {s}\right) \oplus \big (\overline {{\mathcal {F}}} _ {s ^ {-}} \cap {} ^ {\tau} \mathcal {F} _ {s} \big) \rightarrow \big (\overline {{\mathcal {F}}} _ {s ^ {-}} \oplus {} ^ {\tau} \mathcal {F} _ {s} \big)\right)\\\cong \det \left(\overline {{\mathcal {F}}} _ {s ^ {-}} \cap {} ^ {\tau} \mathcal {F} _ {s} \rightarrow \overline {{\mathcal {F}}} _ {s ^ {-}} / \overline {{\mathcal {F}}} _ {s}\right)\\= \left\{\begin{array}{l l}\det \left(^ {\tau} \mathcal {A} _ {r _ {1}} \rightarrow \mathcal {A} _ {r _ {1}} ^ {\prime}\right)&\text { si } s = r _ {1},\\\det \left( \right.\mathcal {A} _ {s} ^ {\prime} \rightarrow \mathcal {A} _ {s} \otimes^ {1 - \tau} \left( \right.\bigotimes_ {\substack {t \in r _ {-} ^ {+}\\t <   s}} \mathcal {L} _ {t}\left. \right)\left. \right)&\text { si } s > r _ {1}.\end{array}\right.\end{array}
$$

Si on pose$\mathcal { B } _ { s } = \mathcal { A } _ { s } \otimes \Big ( \bigotimes _ { { t \in \underline { { r } } ^ { + } } \atop { t < s } } \mathcal { L } _ { t } \Big )$et$\mathcal { B } _ { s } ^ { \prime } = \mathcal { A } _ { s } ^ { \prime } \otimes \tau \Big ( \bigotimes _ { t \in \underline { { r } } ^ { + } } \mathcal { L } _ { t } \Big )$pour tout $s \in \underline { { r } } ^ { + }$, on definit alors un morphisme de´$\widetilde { \mathcal { C } } _ { r } ^ { r , N }$vers le champ algebrique´ $\overline { { \mathfrak { C } } } ^ { r , N } = \overline { { \mathfrak { C } } } _ { \varnothing } ^ { r _ { 1 } , N } \times _ { \mathbb { A } ^ { N } / \mathbb { G } _ { m } ^ { N } } r _ { 2 } \overline { { \mathfrak { C } } } _ { \varnothing } ^ { N } \times \cdot \cdot \cdot \times _ { \mathbb { A } ^ { N } / \mathbb { G } _ { m } ^ { N } } r _ { k } \overline { { \mathfrak { C } } } _ { \varnothing } ^ { \overline { { N } } }$qui à tout schema´ S associe le groupoïde des familles ainsi constituees :´

• des$\mathcal { O } _ { N \times S } – \mathbf { M o d u l e s } \ \mathcal { B } _ { s }$et$\mathcal { B } _ { s } ^ { \prime } , s \in \underline { { r } } ^ { + }$, localement libres de rangs$s - s ^ { - }$ • des homomorphismes$\begin{array} { r } { \mathcal { B } _ { r _ { 1 } } \tilde { \mathbf { \Sigma } }  \mathcal { B } _ { r _ { 1 } } ^ { \prime } , \tau \mathcal { B } _ { r _ { 1 } }  \mathcal { B } _ { r _ { 1 } } ^ { \prime } } \end{array}$et$\mathcal { B } _ { s } ^ { \prime } \ \to \ \mathcal { B } _ { s } ,$ $\mathcal { B } _ { s } ^ { \prime } \ \to \ ^ { \tau } \mathcal { B } _ { s }$pour$s ~ > ~ r _ { 1 } ~ = ~ 0 ^ { + }$, dont les conoyaux admettent un gen´ erateur comme´${ \mathcal { O } } _ { S ^ { - } } \mathbf { M o d u l e s }$localement sur S, et tels que pour tout $\bar { s } \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + }$le determinant de´$\mathcal { B } _ { s ^ { + } } ^ { \prime } \to \mathrm { ~ } ^ { \tau } \mathcal { B } _ { s ^ { + } }$est muni d’un isomorphisme avec celui de$\mathcal { B } _ { s } ^ { \prime } \to \mathcal { B } _ { s }$si$s > r _ { 1 }$[resp. de$\tau _ { \mathcal { B } _ { r _ { 1 } } } \to \mathcal { B } _ { r _ { 1 } } ^ { \prime }$si$s = r _ { 1 } ]$

On a un carre commutatif´

$$
\begin{array}{c c c} \operatorname{Cht} _ {\underline {{r}}} ^ {r, d, \overline {{p}} \leq p} & \longrightarrow & \widetilde {\mathcal {C}} _ {\underline {{r}}} ^ {r, N} \times_ {\left(\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}\right) ^ {2}} (X \times X) \\ \Big \downarrow & & \Big \downarrow \\ \operatorname{Cht} ^ {r \cdot d, \overline {{p}} \leq p} & \longrightarrow & \overline {{\mathcal {C}}} ^ {r, N} \times_ {\left(\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}\right) ^ {2}} (X \times X) \end{array}
$$

où on rappelle que$\mathrm { C h t } ^ { { \underline { { r } } } , d , { \overline { { p } } } \leq p }$est un ouvert de$\mathbf { C h t } \sp { \underline { { r } } } = \mathbf { C h t } \sp { r _ { 1 } } \times { } _ { X } \sp { r _ { 2 } }$Cht$\times _ { X } \cdot \cdot \cdot$ $\times _ { X } r _ { k }$Cht et que$\overline { { \mathfrak { C } } } ^ { { \cal P } , { \cal N } } \times _ { ( \mathbb { A } ^ { N } / \mathbb { G } _ { \mathfrak { m } } ^ { N } ) ^ { 2 } } ( { \boldsymbol X } \times { \boldsymbol X } ) = { \boldsymbol X } \times _ { \mathbb { A } ^ { N } / \mathbb { G } _ { \mathfrak { m } } ^ { N } } \overline { { \mathfrak { C } } } _ { \sharp } ^ { r _ { 1 } , N } \times _ { \mathbb { A } ^ { N } / \mathbb { G } _ { \mathfrak { m } } ^ { N } } { \overline { { \mathfrak { C } } } } _ { \sharp } ^ { N } \times$ $\dots \times _ { \mathbb { A } ^ { N } / \mathbb { G } _ { m } ^ { N } } r _ { k } \overline { { \mathfrak { C } } } _ { \varnothing } ^ { N } \times _ { \mathbb { A } ^ { N } / \mathbb { G } _ { m } ^ { N } }$X. D’après le lemme II.1, la seconde flèche horizontale$\mathrm { C h t } ^ { \underline { { r } } , d , \overline { { p } } \leq p } \to \overline { { \mathfrak { C } } } ^ { \underline { { r } } , N } \times _ { ( \mathbb { A } ^ { N } / \mathbb { G } _ { \mathfrak { m } ^ { N } } ^ { N } ) ^ { 2 } } ( X \times X )$est lisse de dimension relative $( 2 r _ { 1 } - 2 ) + \cdot \cdot \cdot + ( 2 r _ { k } - 2 ) + ( k ^ { \frac { m } { - } } 1 ) = 2 r - k - 1$

D’autre part, on a le lemme suivant :

Lemme III.6. – Le groupe G des automorphismes d’un point geom´ etrique´ $\widetilde { \mathcal { F } } = ( \mathcal { F } \right. \mathcal { F } ^ { \prime } \left. \mathcal { F } ^ { \prime \prime } ; ( \mathcal { L } _ { s } ) _ { s \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + } } , { } ^ { \tau } \mathcal { F } \Longrightarrow \mathcal { F } ^ { \prime \prime } )$de$\widetilde { \mathcal { C } } _ { \underline { { r } } } ^ { r , N }$au-dessus de son image dans$\overline { { \mathcal { C } } } ^ { \underline { { r } } , N }$s’inscrit dans une suite exacte naturelle

$$
1 \to \mathbb {G} _ {m} ^ {k - 1} [ \tau ] \times U [ \tau ] \to G \to G ^ {\prime} \to 1
$$

où$\mathbb { G } _ { m } ^ { k - 1 } [ \tau ]$et$U [ \tau ]$designent les noyaux de´ Frob dans$\mathbb { G } _ { m } ^ { k - 1 }$et le groupe unipotent U associe´$\grave { a } \mathcal { F }$muni de lafiltration$( \mathcal { F } _ { s } )$et où$G ^ { \dot { \prime } }$est compose de´ $k - 1$facteurs egaux à´$\mathbb { G } _ { m }$ou$\mathbb { A } ^ { 1 }$

Demonstration :´ Le groupe$G$est le groupe des automorphismes de$\widetilde { \mathcal F }$qui induisent l’identite du point image dans´$\widetilde { \mathcal { C } } _ { \underline { { r } } } ^ { r , N }$. Celui-ci consiste en des$\mathcal { B } _ { s }$ et$\mathcal { B } _ { s } ^ { \prime } , s \in \underline { { r } } ^ { + }$, relies par diff´ erents homomorphismes. De plus, le point´$\widetilde { \mathcal F }$ definit des isomorphismes entre les d´ eterminants´

$$
\det \left(\mathcal {B} _ {s ^ {+}} ^ {\prime} \to {} ^ {\tau} \mathcal {B} _ {s ^ {+}}\right) \cong \left\{ \begin{array}{l l} \det \left(^ {\tau} \mathcal {B} _ {r _ {1}} \otimes {} ^ {\tau} \mathcal {L} _ {r _ {1}} \to \mathcal {B} _ {r _ {1}} ^ {\prime} \otimes {} ^ {\tau} \mathcal {L} _ {r _ {1}}\right) & \text { si } s = r _ {1}, \\ \det \left(\mathcal {B} _ {s} ^ {\prime} \otimes {} ^ {\tau} \mathcal {L} _ {s} \to \mathcal {B} _ {s} \otimes {} ^ {\tau} \mathcal {L} _ {s}\right) & \text { si } s > r _ {1} \end{array} \right.
$$

indexes par l’ensemble´$\{ s \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + } \}$de cardinal$k - 1$. Notons I [resp. J] le sous-ensemble des s tels que les deux determinants ci-dessus soient nuls´ [resp. non nuls].

Le facteur$\mathbb { G } _ { m } ^ { k - 1 } [ \tau ]$est le groupe des automorphismes des$\mathcal { L } _ { s }$, $s \in \underline { r } ^ { - } \cap \underline { r } ^ { + }$, qui induisent l’identite sur les´$\tau _ { \mathcal { L } _ { s } }$

Le quotient de G par$\mathbb { G } _ { m } ^ { k - 1 } [ \tau ] \times U [ \tau ]$contient un facteur$\mathbb { G } _ { m }$indexe´ par chaque el´ ement´$s \in I \mathrm { { \Omega } } ( \mathrm { c } ^ { \prime }$est le groupe des automorphismes de$\boldsymbol { \tau } _ { \mathcal { L } _ { s } }$qui respectent l’isomorphisme entre determinants nuls ci-dessus). Et il contient´ comme unique autre facteur le groupe$\operatorname { A u t } ( ^ { \tau } { \mathcal { F } } )$des automorphismes de$\tau _ { \mathcal { F } }$ qui respectent les deux filtrations$( \tau _ { \mathcal { F } _ { s } } )$et$( \overline { \mathcal { F } } _ { s } )$et induisent l’identite sur les´ $\hat { \tau _ { \mathcal { F } _ { s } } } / \tau \hat { \mathcal { F } } _ { s ^ { - } } , \overline { { \mathcal { F } } } _ { s ^ { - } } / \overline { { \mathcal { F } } } _ { s }$et$\overline { { \mathcal { F } } } _ { s ^ { - } } \cap \tau \mathcal { F } _ { s }$puisque ceux-ci peuvent être reconstitues´ par la donnee des´$\mathcal { B } _ { s } , \mathcal { B } _ { s } ^ { \prime }$et$\mathcal { L } _ { t }$. On est ramene à montrer que´$\operatorname { A u t } ( ^ { \tau } { \mathcal { F } } )$est compose de´$| J |$facteurs egaux à´$\mathbb { A } ^ { 1 }$

Pour tout$s \in I , \tau _ { \mathcal { F } }$se decompose en somme directe´${ } ^ { \tau } \mathcal { F } = { } ^ { \tau } \mathcal { F } _ { s } \oplus \overline { { \mathcal { F } } } _ { s }$ si bien qu’il suffit de traiter le cas où$I = \emptyset$et$J = \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + }$. Considerant´ $r ^ { - } = r _ { 1 } + \cdots + r _ { k - 1 }$et$\operatorname { A u t } ( { } ^ { \tau } \mathcal { F } _ { r ^ { - } } )$le groupe associe´$\hat { \textbf { a } } ^ { \tau } \mathcal { F } _ { r ^ { - } }$muni des deux filtrations par les$\tau _ { \mathcal { F } _ { s } }$et les$\tau _ { \mathcal { F } _ { r } - } \cap \overline { { \mathcal { F } } } _ { s } , s < r ^ { - }$, (avec la remarque que $\begin{array} { r } { \tau _ { \mathcal { F } _ { r } - \big / } \tau _ { \mathcal { F } _ { r } - \bigcap } \overline { { \mathscr { F } } } _ { s } \cong \tau _ { \mathcal { F } } / \overline { { \mathscr { F } } } _ { s } \operatorname { e t } ^ { \tau } \mathcal { F } _ { r ^ { - } } \cap \overline { { \mathscr { F } } } _ { s ^ { - } } / { } ^ { \tau } \mathcal { F } _ { r ^ { - } } \cap \overline { { \mathscr { F } } } _ { s } \cong \overline { { \mathscr { F } } } _ { s ^ { - } } / \overline { { \mathscr { F } } } _ { s } ) } \end{array}$on a un homomorphisme surjectif de restriction de$\tau _ { \mathcal { F } \mathrm { ~ a ~ } ^ { \tau } \mathcal { F } _ { r ^ { - } } }$

$$
\operatorname{Aut} \left(^ {\tau} \mathcal {F}\right)\rightarrow \operatorname{Aut} \left(^ {\tau} \mathcal {F} _ {r ^ {-}}\right).
$$

Son noyau est constitue des´ el´ ements de la forme´

$$
\mathrm{Id} + u,
$$

où u est un endomorphisme de$\tau _ { \mathcal { F } }$verifiant´

$$
\begin{array}{l} u (\tau \mathcal {F} _ {r ^ {-}}) = 0 \qquad \text { et } \qquad u (\overline {{\mathcal {F}}} _ {r ^ {-}}) = 0  , \\ u (\tau \mathcal {F}) \subseteq {} ^ {\tau} \mathcal {F} _ {r ^ {-}}  , \\ u (\tau \mathcal {F}) \subseteq \overline {{\mathcal {F}}} _ {r ^ {-}} \qquad \left(\text { puisque }   ^ {\tau} \mathcal {F} = ^ {\tau} \mathcal {F} _ {r ^ {-}} + \overline {{\mathcal {F}}} _ {(r ^ {-}) ^ {-}}\right). \end{array}
$$

Comme$\begin{array} { r } { { ^ { \tau } \mathcal { F } } / ( { ^ { \tau } \mathcal { F } _ { r ^ { - } } } + { \overline { { \mathcal { F } } } _ { r ^ { - } } } ) \operatorname { e t } { ^ { \tau } \mathcal { F } _ { r ^ { - } } } \cap \overline { { \mathcal { F } } } _ { r ^ { - } } } \end{array}$sont de dimension 1, ce noyau est isomorphe à$\mathbb { A } ^ { 1 }$. On conclut par recurrence sur le nombre´$k - 1$d’el´ ements´ de$\underline { { r } } ^ { - } \cap \underline { { r } } ^ { + }$!"

On peut maintenant donner :

Fin de la demonstration de la proposition III.5 :´ Comme$\mathrm { C h t } _ { \underline { { r } } } ^ { r , d , \overline { { p } } \leq p }$et ${ \widetilde { \mathfrak { C } } } _ { \underline { { r } } } ^ { r , N } \times _ { ( { \mathbb { A } } ^ { N } / { \mathbb { G } } _ { m } ^ { N } ) ^ { 2 } } \ : ( X \times X )$sont lisses, il suffit de prouver que les fibres geom´ etriques non vides de´

$$
\operatorname{Cht} _ {\underline {{r}}} ^ {r, d, \overline {{p}} \leq p} \to \widetilde {\mathcal {C}} _ {\underline {{r}}} ^ {r, N} \times_ {\left(\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}\right) ^ {2}} (X \times X)
$$

sont lisses de dimension$2 r - 2$. On sait dejà qu’elles sont de dimension´ $\geq 2 r - 2$car celles dans la strate gen´ erique index´ ee par la partition triviale´ $\varnothing$sont lisses de dimension$2 r - 2$

Le morphisme$\mathrm { C h t } _ { \underline { { r } } } ^ { r , d , \overline { { p } } \leq p } \to \mathrm { C h t } ^ { \underline { { r } } , d , \overline { { p } } \leq p }$est le compose´$\mathrm { d } ^ { \prime }$un morphisme de gerbe deduit par changement de base de´$\mathbf { B } \mathbb { G } _ { m } ^ { k - 1 } \xrightarrow [ m ] { \mathrm { F r o b } } \mathbf { B } \mathbb { G } _ { m } ^ { k - 1 }$et d’un autre morphisme de gerbe dont le groupe de structure$\mathcal { U } [ \tau ]$est plat, fini et radiciel. En un point$\widetilde { \mathcal { E } } = ( \mathcal { E } \hookrightarrow \mathcal { E } ^ { \prime }  \mathcal { E } ^ { \prime \prime } ; ( \mathcal { L } _ { s } ) _ { s \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + } } , { } ^ { \tau } \mathcal { E } \longrightarrow \mathcal { E } ^ { \prime \prime } )$ de$\begin{array} { r } { \mathrm { C h t } _ { r } ^ { r , d , \overline { { p } } \leq p } , \ \mathcal { U } [ \tau ] } \end{array}$est le noyau de Frob dans le groupe unipotent U des automorphismes de E muni de sa filtration canonique$( \mathcal E _ { s } ) _ { s \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + } }$

Il resulte des conditions de troncature qui d´ efinissent le champ´$\mathbf { C } \mathrm { h t } _ { r } ^ { r , d , \overline { { p } } \leq p }$ à partir du polygone$p$(voir la proposition 9 et le lemme 10 de [Lafforgue, 1998] paragraphe 1d) que si$p$est assez convexe, les$\mathcal { E } _ { s }$figurent dans la filtration canonique de Harder-Narasimhan de$\mathcal { E }$et que les ruptures de pentes $\mu ^ { - } ( \mathcal { E } _ { s } ) - \mu ^ { + } ( \mathcal { E } / \mathcal { E } _ { s } )$de son polygone canonique en les entiers$s \in \underline { r } ^ { - } \cap \underline { r } ^ { + }$ sont arbitrairement grandes. On en deduit que si le polygone´$p$est assez convexe en fonction de (X et) N, l’homomorphisme de restriction de X à N

$$
\mathcal {U} \to U
$$

est surjectif et il en est de même de$\mathcal { U } [ \tau ]  \ \boldsymbol { U } [ \tau ]$

Comme les fibres geom´ etriques de´

$$
\mathrm{Cht} ^ {\underline {{r}} \cdot d, \overline {{p}} \leq p} \rightarrow \overline {{\mathcal {C}}} _ {\underline {{r}}} ^ {r, N} \times_ {\left(\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}\right) ^ {2}} (X \times X)
$$

sont lisses de dimension$2 r - k - 1 = ( 2 r - 2 ) - ( k - 1 )$et d’après le lemme III.6, les fibres geom´ etriques de´

$$
\mathrm{Cht} _ {\underline {{r}}} ^ {r, d, \overline {{p}} \leq p} \rightarrow \widetilde {\mathcal {C}} _ {\underline {{r}}} ^ {r, N} \times_ {\left(\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}\right) ^ {2}} (X \times X)
$$

sont des fermes dans des champs lisses de dimension´$( 2 r - 2 ) - ( k - 1 ) +$ $( k - 1 ) = ( 2 r - 2 )$. Sachant que leur dimension est$\geq 2 r - 2 .$, on conclut que ce sont des reunions de composantes connexes, lisses de dimension´ $2 r - 2$!"

## 3) Compactifications avec niveau

Dans ce paragraphe, on met des structures de niveau$N = \operatorname { S p e c } { \mathcal { O } } _ { N }$sur les chtoucas iter´ es au moyen de carr´ es cart´ esiens dont la base est le morphisme´ de restriction au niveau N.

## a) Structures de niveau definies par normalisation´

Il existe un unique sous-champ ouvert$\widetilde { \mathcal { C } } ^ { r , N }$de$\overline { { \mathcal { C } } } ^ { r , N }$dont la trace dans chaque strate$\overline { { \mathcal { C } } } _ { r } ^ { r , \overline { { N } } }$soit egale à´$\widetilde { \mathcal { C } } _ { r } ^ { r , N }$

Pour d un degre et´$p : [ 0 , \overline { { r } } ] \to \mathbb { R } _ { + }$un polygone de troncature, le morphisme de restriction à N

$$
\overline {{\mathrm{Cht} ^ {r , d , \overline {{p}} \leq p}}} \to \overline {{\mathcal {C}}} ^ {r, N}
$$

se factorise à travers cet ouvert$\widetilde { \mathcal { C } } ^ { r , N }$

On notera$\mathcal { C } ^ { r , N }$l’ouvert de$\widetilde { \mathcal { C } } ^ { r , N }$constitue des´ el´ ements qui n’ont ni´ pôle ni zero dans´ N c’est-à-dire l’image reciproque du point g´ en´ erique´ $( \mathbb { G } _ { m } ^ { N } / \mathbb { G } _ { m } ^ { N } ) ^ { 2 }$de$( \mathbb { A } ^ { N } / ( \mathbb { G } _ { m } ^ { N } ) ^ { 2 }$. Son image reciproque dans´$\overline { { \mathrm { C h t } ^ { r , d , \overline { { { p } } } \leq p } } }$est $\operatorname { C h t } ^ { r , d , \overline { { p } } \leq p } \times _ { X \times X } \left( X - N \right) \times \left( X - N \right)$et d’après la proposition III.5, le morphisme

$$
\overline {{\operatorname{Cht} ^ {r , d , \overline {{p}} \leq p}}} \times_ {X \times X} (X - N) \times (X - N) \rightarrow \mathcal {C} ^ {r, N} \times (X - N) \times (X - N)
$$

est lisse de dimension relative$2 r - 2$si$p$est assez convexe en fonction de (X et) N.

Le champ$\mathcal { C } ^ { r , N }$est muni d’un morphisme lisse sur le champ torique $\mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \mathcal { A } } ^ { r , 1 } = ( \mathbb { A } ^ { 1 } / \mathbb { G } _ { m } ) ^ { r - 1 }$. L’image reciproque du point g´ en´ erique´$\bar { \mathcal { A } } _ { \varnothing } ^ { r , 1 } / \bar { \mathcal { A } } _ { \varnothing } ^ { r , 1 }$ est la strate ouverte dense$\mathcal { C } _ { \varnothing } ^ { r , N }$de$\mathcal { C } ^ { r , N }$qui associe à tout schema´$S \left( \operatorname { s u r } \mathbb { F } _ { q } \right)$ le groupoïde des$\mathcal { O } _ { N \times S ^ { - } } \mathbf { M }$odules$\mathcal { F }$localement libres de rang r munis d’un isomorphisme

$$
{ } ^ { \tau } \mathcal { F } = ( \mathrm{Id} _ { N } \times \mathrm{Frob} _ { S } ) ^ { * } \mathcal { F } \stackrel { \sim } { \to } \mathcal { F } .
$$

Il s’identifie au champ$\mathrm { G L } _ { r } ^ { N } / \tau / \mathrm { G L } _ { r } ^ { N }$quotient de$\mathrm { G L } _ { r } ^ { N }$(le groupe deduit de´ $\mathrm { G L } _ { r }$par restriction des scalaires à la Weil de$\mathcal { O } _ { N } \dot { \textmd { a } } \dot { \mathbb { F } _ { q } } )$par l’action à droite de$\mathrm { G L } _ { r } ^ { N }$par conjugaison tordue

$$
(u, g) \mapsto u ^ {g} = \tau (g) ^ {- 1} \circ u \circ g.
$$

En associant à tout schema´ S le fibre trivial´$\mathcal { O } _ { N \times S } ^ { r }$on definit un point´ Spec$\mathbb { F } _ { q } \to \mathcal { C } _ { \varnothing } ^ { r , N }$et d’après le theorème 2(ii) du paragraphe I.3 de [Laf-´ forgue,$1 9 9 7 ] , \mathcal { C } _ { \varnothing } ^ { r , N }$est aussi le classifiant$\mathrm { B G L } _ { r } ( \mathcal { O } _ { N } ) = \mathrm { S p e c } \mathbb { F } _ { q } / \mathrm { G L } _ { r } ( \mathcal { O } _ { N } )$ du groupe fini$\mathrm { G L } _ { r } ^ { N } ( \mathbb { F } _ { q } ) = \mathrm { G L } _ { r } ( \mathcal { O } _ { N } )$

On peut reformuler la definition I.2 en disant que le revêtement´$\mathrm { C h t } _ { N } ^ { r }$de $\mathrm { C h t } ^ { r } \times _ { X \times X } \left( X - N \right) \times \left( X - N \right)$est defini comme produit fibr´ e dans le carr´ e´ cartesien´

$$
\begin{array}{c c c} \operatorname{Cht} _ {N} ^ {r} & \longrightarrow & \mathcal {C} _ {N, \emptyset} ^ {r} = \operatorname{Spec} \mathbb {F} _ {q} = \operatorname{GL} _ {r} ^ {N} / \operatorname{GL} _ {r} ^ {N} \\ \Big \downarrow & & \Big \downarrow \\ \operatorname{Cht} ^ {r} \times_ {X \times X} (X - N) \times (X - N) & \longrightarrow & \mathcal {C} _ {\emptyset} ^ {r, N} = \operatorname{Spec} \mathbb {F} _ {q} / \operatorname{GL} _ {r} (\mathcal {O} _ {N}) \\ & & = \operatorname{GL} _ {r} ^ {N} / ^ {\tau} / \operatorname{GL} _ {r} ^ {N} \end{array}
$$

où$\mathrm { G L } _ { r } ^ { N } / \mathrm { G L } _ { r } ^ { N } \to \mathrm { G L } _ { r } ^ { N } / \tau / \mathrm { G L } _ { r } ^ { N }$est le quotient par$\mathbf { G L } _ { r } ^ { N }$de l’isogenie de´ Lang

$$
\mathrm{GL} _ {r} ^ {N} \to \mathrm{GL} _ {r} ^ {N}: g \mapsto \tau (g) ^ {- 1} \circ g.
$$

Ceci amène à definir des structures de niveau´ N sur les chtoucas iter´ es´ en prolongeant l’isogenie de Lang au-dessus de´$\mathcal { C } ^ { r , N }$

Proposition III.7. – Soit$\mathcal { C }  \mathcal { C } ^ { r , N }$un champ algebrique repr´ esentable´ quasi-projectif sur$\mathcal { C } ^ { r , N }$dont la restriction au-dessus de l’ouvert dense$\mathcal { C } _ { \varnothing } ^ { r , N }$ s’identifie au revêtement de Lang$\mathcal { C } _ { N , \emptyset } ^ { r } \to \mathcal { C } _ { \varnothing } ^ { r , N }$

Alors pour tout degre d et tout polygone de troncature p assez convexe´ enfonction de (X et) N, le champ algebrique´ X defini comme produitfibr´ e´ dans le carre cart´ esien´

![](images/page_72_image_12.jpg)

verifie les propri´ et´ es suivantes :´

(i) Il est representable quasi-projectif sur´${ \mathrm { C h t } } ^ { r , d , \overline { { p } } \leq p } \times _ { X \times X } ( X - N ) \times$ $( X - N )$et sa restriction au-dessus de l’ouvert$\operatorname { C h t } ^ { r , d , \overline { { p } } \leq p } \times _ { X \times X } ( X - N )$ $\times \ ( X - N )$s’identifie au revêtement etale galoisien´$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p }$. Si $\mathrm { ~ \mathcal { C } ~ } \to ~ \mathcal { C } ^ { r , N }$est projectif [resp. fini], il est projectif [resp. fini] sur $\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } \times _ { X \times X } ( X - N ) \times ( X - N )$et doncpropre sur$( X { - } N ) \times ( X { - } N )$

(ii) Il est lisse sur${ \mathfrak { C } } \times ( X - N ) \times ( X - N )$. Si C est lui-même lisse sur le champ torique$\mathcal { A } / \mathcal { A } _ { \mathcal { Y } }$quotient d’une variet´ e torique lisse´ A par son tore$\mathcal { A } _ { \emptyset }$(de tellefaçon que$\mathcal { C } _ { N , \emptyset } ^ { r }$soit l’image reciproque de´$\mathcal { A } _ { \emptyset } / \mathcal { A } _ { \emptyset } )$, il est lisse sur$\mathcal { A } / \mathcal { A } _ { \emptyset } \times ( \bar { X } - \ddot { N } ) ^ { \prime \prime } \times ( X - N )$; autrement dit, il est lisse sur$( X - N ) \times ( X - N )$et son bord$\mathfrak { X } - \mathbf { C } \mathbf { h } \mathfrak { t } _ { N } ^ { r , d , \overline { { p } } \leq p }$est un diviseur à croisements normaux relatifs.!"

Un choix naturel consiste à prolonger par normalisation de$\mathcal { C } _ { \varnothing } ^ { r , N }$à$\mathcal { C } ^ { r , N }$ le revêtement$\mathcal { C } _ { N , \emptyset } ^ { r }$. On pose :

Definition III.8.´ – Soit$\mathcal { C } _ { N } ^ { r }$le champ algebrique normal repr´ esentable fini´ sur$\mathcal { C } ^ { r , N }$(avec action de${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N } ) )$qui est la normalisation de$\mathcal { C } ^ { r , N }$dans $\mathcal { C } _ { N , \emptyset } ^ { r } .$

On notera$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$et on appellera champs de chtoucas iter´ es avec´ structures de niveau N les champs algebriques d´ efinis comme produits´ fibres dans les carr´ es cart´ esiens :´

![](images/page_73_image_5.jpg)

Ils sont representables finis sur´$\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } } } \times _ { X \times X } ( X - N ) \times ( X - N )$ et donc propres sur$( X - N ) \times ( X - N )$et ils sont munis d’une action de ${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N } )$

D’autre part, ils sont lisses sur${ \mathfrak { C } } _ { N } ^ { r } \times ( X - N ) \times ( X - N )$(si p est assez convexe enfonction de X et N) et en particulier normaux.

Bien sûr, on notera aussi$\overline { { { \bf C h t } _ { N } ^ { r , \overline { { { p } } } \leq p } } } = \coprod _ { d \in \mathbb { Z } } \overline { { { \bf C h t } _ { N } ^ { r , d , \overline { { { p } } } \leq p } } } \mathrm { e t } \overline { { { \bf C h t } _ { N } ^ { r , \overline { { { p } } } \leq p } } } / a ^ { \mathbb { Z } } \cong$ $\prod _ { 1 \le d \le r | \deg ( a ) | } \overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \le p } } }$. Tous sont lisses sur${ \mathfrak { C } } _ { N } ^ { r } \times ( X - N ) \times ( X - N )$mais ils ne sont pas lisses sur$( X - N ) \times ( X - N )$car$\mathcal { C } _ { N } ^ { r }$est singulier.

Dans le cas où N n’a pas de multiplicites, on construira au paragraphe c´ une resolution des singularit´ es de´$\mathcal { C } _ { N } ^ { r }$mais dans le cas gen´ eral nous allons´ nous contenter d’expliciter dans le paragraphe b ci-dessous un ouvert de lissite dans´$\mathcal { C } _ { N } ^ { r }$plus gros que$\mathcal { C } _ { N , \emptyset } ^ { r }$

## b) Un ouvert naturel de lissite´

Le champ$\mathcal { C } ^ { r , N }$associe à tout schema´ S sur$\mathbb { F } _ { q }$le groupoïde des familles constituees de´

• un$\mathcal { O } _ { N \times S ^ { - } } \mathbf { M }$odule$\mathcal { F }$localement libre de rang r sur$N \times S$

• des fibres inversibles´$\mathscr { L } _ { 1 } , \ldots , \mathscr { L } _ { r - 1 }$sur S munis de sections globales $\ell _ { 1 } , \ldots , \ell _ { r - 1 }$

• un homomorphisme complet$\begin{array} { r } { ^ { \tau } \mathcal { F } = ( \mathrm { I d } _ { N } \times \mathrm { F r o b } _ { S } ) ^ { * } \mathcal { F } \Rightarrow \mathcal { F } } \end{array}$dont l’image dans$( \mathbb { A } ^ { 1 } / \mathbb { G } _ { m } ) ^ { r - 1 } ( N \times S )$est$( ( \mathcal { L } _ { 1 } ^ { \otimes ( q - 1 ) } , \ell _ { 1 } ^ { q - 1 } ) , \dots , ( \mathcal { L } _ { r - 1 } ^ { \otimes ( q - 1 ) } , \ell _ { r - 1 } ^ { q - 1 } ) )$

Un tel homomorphisme complet peut s’ecrire comme une famille ´ d’homomorphismes lineaires entre fibr´ es´

$$
u _ {s}: ^ {\tau} \left(\Lambda^ {s} \mathcal {F} \otimes \bigotimes_ {t <   s} \mathcal {L} _ {t} ^ {\otimes (s - t)}\right)\rightarrow \Lambda^ {s} \mathcal {F} \otimes \bigotimes_ {t <   s} \mathcal {L} _ {t} ^ {\otimes (s - t)}, \quad 1 \leq s \leq r,
$$

qui sont non nuls en tout point geom´ etrique de´$N \times S$

On definit un ouvert´$\mathfrak { C } ^ { \prime r , N } \mathrm { ~ d e ~ } \mathcal { C } ^ { r , N }$en demandant qu’en tout point geom´ etrique de´$N \times S$aucun des$u _ { s } , 1 \le s \le r$, ne soit τ-nilpotent (ou, ce qui revient au même, que pour tout s, Ker$u _ { s }$et <sup>τ</sup> Im$u _ { s }$soient en somme directe).

D’autre part, on definit un champ´$\mathcal { C } _ { N } ^ { \prime r }$representable sur´$\mathcal { C } ^ { r , N }$en classifiant les façons de completer les donn´ ees ci-dessus´$( { \mathcal { F } } ~ ; ( { \mathcal { L } } _ { 1 } , { \ell } _ { 1 } ) , \ldots ,$ $( \mathscr { L } _ { r - 1 } , \ell _ { r - 1 } ) ; \tau \mathscr { F } \Rightarrow \mathscr { F } )$par un homomorphisme complet

$$
\mathcal {F} \Rightarrow \mathcal {O} _ {N \times S} ^ {r}
$$

dont l’image dans$( \mathbb { A } ^ { 1 } / \mathbb { G } _ { m } ) ^ { r - 1 } ( N \times S )$est$( ( \mathcal { L } _ { 1 } , \ell _ { 1 } ) , \dots , ( \mathcal { L } _ { r - 1 } , \ell _ { r - 1 } ) )$et qui, si on l’ecrit sous la forme d’une famille d’homomorphismes lin´ eaires´

$$
v _ {s}: \Lambda^ {s} \mathcal {F} \otimes \bigotimes_ {t <   s} \mathcal {L} _ {t} ^ {\otimes (s - t)} \to \Lambda^ {s} \left(\mathcal {O} _ {N \times S} ^ {r}\right), \quad 1 \leq s \leq r,
$$

verifie les relations´$\tau ( v _ { s } ) = v _ { s } \circ u _ { s } , 1 \leq s \leq r$

La restriction de$\mathcal { C } _ { N } ^ { \prime r } \to \mathcal { C } ^ { r , N }$au-dessus de l’ouvert dense$\mathcal { C } _ { \varnothing } ^ { r , N } \subset \mathcal { C } ^ { r , N }$ s’identifie à l’isogenie de Lang´$\mathcal { C } _ { N , \emptyset } ^ { r } \to \mathcal { C } _ { \varnothing } ^ { r , N }$puisqu’elle est definie par la´ condition que les sections$\ell _ { 1 } , \ldots , \ell _ { r - 1 }$soient inversibles ou, ce qui revient au même, que$u _ { 1 } \mathrm { e t } v _ { 1 }$soient des isomorphismes. On a le lemme evident :´

Lemme III.9. – Le morphisme$\mathcal { C } _ { N } ^ { \prime r } \to \mathcal { C } ^ { r , N }$se factorise à travers l’ouvert $\mathcal { C } ^ { \prime r , N } d e \mathcal { C } ^ { r , N }$

Demonstration :´ La relation$\tau ( v _ { s } ) = v _ { s } \circ u _ { s }$entraîne, pour tout entier n, $\tau ^ { n } ( \upsilon _ { s } ) = \upsilon _ { s } \circ u _ { s } \circ \tau ( u _ { s } ) \circ \cdot \cdot \cdot \circ \tau ^ { n - 1 } ( u _ { s } )$si bien que si$v _ { s }$ne$\mathrm {  ~ s ~ } ^ { \prime }$annule jamais, $u _ { s } \mathrm { ~ n ~ } ^ { \prime }$est jamais τ-nilpotent.!"

On a un diagramme commutatif :

![](images/page_75_image_1.jpg)

Dans$\mathbf { \mathcal { A } } ^ { r , 1 } = \mathbb { A } ^ { r - 1 }$, les orbites$\mathcal { A } _ { \underline { { r } } } ^ { r , 1 }$de$\mathcal { A } _ { \varnothing } ^ { r , 1 } = \mathbb { G } _ { m } ^ { r - 1 }$sont indexees par les´ partitions$\boldsymbol { r } = ( r = r _ { 1 } + \cdot \cdot \cdot + r _ { k } )$de l’entier r et chacune a un point distingue´$\alpha _ { \underline { { r } } } .$. On note$\mathcal { C } _ { N , \underline { { r } } } ^ { \prime r }$et$\mathcal { C } _ { r } ^ { \prime r , N }$les strates dans$\mathcal { C } _ { N } ^ { \prime r }$et$\mathcal { C } ^ { \prime r , N }$images reciproques des points´$\mathcal { A } _ { \underline { { r } } } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 }$. En un point$( ^ { \tau } { \mathcal { F } } \Rightarrow { \mathcal { F } } )$de$\mathcal { C } _ { \underline { { r } } } ^ { r , N }$, les conditions de transversalite Ker´$u _ { s } \cap ^ { \tau } \mathrm { K e r } u _ { s } = 0 , 1 \leq s \leq r ,$, qui definissent´ l’ouvert$\mathcal { C } _ { r } ^ { \prime r , N }$sont verifi´ ees si et seulement si elles le sont en les indices´ $s \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + } = \{ r _ { 1 } , r _ { 1 } + r _ { 2 } , \dots , r _ { 1 } + \cdot \cdot \cdot + r _ { k - 1 } \}$. Elles signifient que la filtration des noyaux dans$\tau _ { \mathcal { F } }$et la transformee par´ τ de la filtration des images dans$\mathcal { F }$sont transverses. Strate par strate, on a :

Lemme III.10. – Pour toute partition$\underline { { r } } = ( r = r _ { 1 } + \cdot \cdot \cdot + r _ { k } )$, la strate $\mathcal { C } _ { N , \underline { { r } } } ^ { \prime r }$est lisse de même dimension que$\mathcal { C } _ { \underline { { r } } } ^ { \prime r , N }$

Le morphisme

$$
\mathcal {C} _ {N, \underline {{r}}} ^ {\prime r} \to \mathcal {C} _ {\underline {{r}}} ^ {\prime r, N}
$$

est fini et plat, de rang egal au cardinal de´${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N } )$(donc independant´ de$\underline { { r } } )$, compose d’un morphisme´ etale et d’un morphisme radiciel surjectif ;´ sesfibres sont homogènes sous l’action du groupe fini${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N } )$

Demonstration :´ La fibre$\mathcal { C } _ { N } ^ { \prime r } \times _ { \left( \mathbb { A } ^ { 1 } / \mathbb { G } _ { m } \right) ^ { r - 1 } } \alpha _ { \underline { { r } } }$classifie les familles constituees´ $\mathrm { d } ^ { \circ } \mathrm { u n }$fibre´$\mathcal { F }$sur$N \times S$muni de

• une filtration croissante$0 = \mathcal { F } _ { 0 } \subset \mathcal { F } _ { 1 } \subsetneq \dots \subset \mathcal { F } _ { k } = \mathcal { F }$de$\mathcal { F }$dont les gradues sont localement libres de rangs´$r _ { 1 } , \ldots , r _ { k }$

• une filtration decroissante´$\mathcal { F } = \mathcal { F } ^ { 0 ^ { \circ } } \supset \mathcal { F } ^ { 1 } \supset \ldots \supset \mathcal { F } ^ { k } = 0$de$\mathcal { F }$ dont les gradues sont localement libres de rangs´$r _ { 1 } , \ldots , r _ { k }$et qui verifie´ $\mathcal { F } = \mathcal { F } _ { i } \bar { \oplus } \mathcal { F } ^ { i } , 0 \leq i \leq k$

• une filtration croissante$0 = E _ { 0 } \subset E _ { 1 } \subsetneq \cdots \subsetneq E _ { k } = E$de$E = \mathcal { O } _ { N \times S } ^ { r }$ qui est fixee par´ τ (car pour tous i et s avec$r _ { 1 } + \cdot \cdot \cdot + r _ { i } = s$, det$E _ { i } = \Lambda ^ { s } \tilde { E } _ { i }$ est l’image de l’homomorphisme$v _ { s }$lequel verifie´$\tau ( v _ { s } ) = v _ { s } \circ u _ { s } )$et dont les gradues sont libres de rangs´$r _ { 1 } , \ldots , r _ { k }$

• des isomorphismes

$$
\overline {{v}} _ {i}: \mathcal {F} ^ {i - 1} / \mathcal {F} ^ {i} \stackrel {\sim} {\to} E _ {i} / E _ {i - 1}, 1 \leq i \leq k.
$$

Le morphisme sur$\mathfrak { C } ^ { \prime r , N } \times _ { ( \mathbb { A } ^ { 1 } / \mathbb { G } _ { m } ) ^ { r - 1 } } \alpha _ { \underline { { r } } }$consiste à associer à ces donnees´ celles constituees de´

• le fibre´$\mathcal { F }$,

• la filtration croissante$( \mathcal { F } _ { i } )$de$\mathcal { F }$,

• la filtration decroissante´$( \overline { { \mathcal { F } } } _ { i } = { } ^ { \tau } \mathcal { F } ^ { i } )$de$\tau _ { \mathcal { F } }$,

• les isomorphismes

$$
\overline {{u}} _ {i} = \overline {{v}} _ {i} ^ {- 1} \circ \tau (\overline {{v}} _ {i}): \overline {{\mathcal {F}}} _ {i - 1} / \overline {{\mathcal {F}}} _ {i} \stackrel {{\sim}} {{\to}} \mathcal {F} ^ {i - 1} / \mathcal {F} ^ {i} \cong \mathcal {F} _ {i} / \mathcal {F} _ {i - 1}.
$$

On voit que$\mathcal { C } _ { N } ^ { \prime r } \times _ { \left( \mathbb { A } ^ { 1 } / \mathbb { G } _ { m } \right) ^ { r - 1 } } \alpha _ { \underline { { r } } }$est lisse et que le morphisme

$$
\mathcal {C} _ {N} ^ {\prime r} \times_ {\left(\mathbb {A} ^ {1} / \mathbb {G} _ {m}\right) ^ {r - 1}} \alpha_ {\underline {{r}}} \rightarrow \mathcal {C} ^ {\prime r, N} \times_ {\left(\mathbb {A} ^ {1} / \mathbb {G} _ {m}\right) ^ {r - 1}} \alpha_ {\underline {{r}}}
$$

est fini et plat, compose d’un morphisme´ etale et d’un morphisme radiciel´ surjectif ; ses fibres sont homogènes sous l’action du groupe fini${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N } )$

Si$U _ { \underline { { r } } }$designe le radical unipotent du sous-groupe parabolique sta´ ndard $P _ { \underline { { r } } }$de$\mathrm { G } \overline { { \mathrm { L } } } _ { r }$associe à la partition´$\underline { { r } } ,$le rang de ce morphisme fini plat est egal´ au produit du cardinal du quotient

$$
\mathrm{GL} _ {r} (\mathcal {O} _ {N}) / U _ {\underline {{r}}} (\mathcal {O} _ {N}) = \mathrm{GL} _ {r} ^ {N} (\mathbb {F} _ {q}) / U _ {\underline {{r}}} ^ {N} (\mathbb {F} _ {q})
$$

et de la puissance de$q$

$$
q ^ {\dim (\mathrm{GL} _ {r} ^ {N} / P _ {\underline {{r}}} ^ {N})}.
$$

Or dim$( \mathrm { G L } _ { r } ^ { N } / P _ { \underline { { r } } } ^ { N } ) =$dim$U _ { \underline { { r } } } ^ { N }$et #$U _ { \underline { { r } } } ^ { N } ( \mathbb { F } _ { q } ) = q ^ { \dim U _ { \underline { { r } } } ^ { N } }$donc ce produit est toujours egal à #´$\mathrm { G L } _ { r } ^ { N } ( \mathbb { F } _ { q } )$

Toutes ces propriet´ es se transportent à la strate´$\mathcal { C } _ { N , \underline { { r } } } ^ { \prime r }$et au morphisme $\mathcal { C } _ { N , \underline { { r } } } ^ { \prime r } \to \mathcal { C } _ { \underline { { r } } } ^ { \prime r , N }$!"

Nous pouvons maintenant prouver :

Proposition III.11. – Le champ$\mathcal { C } _ { N } ^ { \prime r }$est lisse sur$( \mathbb { A } ^ { 1 } / \mathbb { G } _ { m } ) ^ { r - 1 }$, donc lisse absolument.

Le morphisme representable´$\mathcal { C } _ { N } ^ { \prime r }  \mathcal { C } ^ { \prime r , N }$est fini plat et le groupe ${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N } )$agit transitivement sur ses fibres.

L’image reciproque de´$\mathcal { C } ^ { \prime r , N }$dans la normalisation$\mathcal { C } _ { N } ^ { r }$de$\mathcal { C } ^ { r , N }$dans $\mathcal { C } _ { N , \emptyset } ^ { r }$s’identifie à$\mathcal { C } _ { N } ^ { \prime \bar { r } }$

Remarque : Comme le morphisme representable fini plat´$\mathcal { C } _ { N } ^ { \prime r }  \mathcal { C } ^ { \prime r , N }$ n’est etale que g´ en´ eriquement et ramifi´ e au bord, on voit en revenant à´ la demonstration du lemme 16(ii) du paragraphe 2d de [Lafforgue´ , 1998] que dans l’enonc´ e de ce lemme il faut´$\mathrm { s } ^ { \mathrm { , } }$autoriser à remplacer l’anneau de valuation discrète A par une extension finie eventuellement ramifi´ ee´ (contrairement à ce qui est dit) qui ne depend que de la famille´$( \widehat { W } _ { w } )$et du niveau I consider´ e. Par cons´ equent, dans la proposition 15 qui pr´ ecède´ dans [loc. cit.], il faut${ \mathrm { s } } ^ { \prime }$autoriser à remplacer A par une extension finie eventuellement ramifi´ ee qui ne d´ epend que de´$( \widehat { W } _ { w } )$et de la constante$\mu \geq 0$ $\mathbf { C } '$est suffisant pour la demonstration des corollaires 17, 18 et 19 qui suivent´ (quitte encore une fois à remplacer A par une extension finie eventuellement´ ramifiee) car les polygones canoniques de Harder-Narasimhan des s´ uites de chtoucas deg´ en´ er´ es qui apparaissent dans la preuve des corollaires 18 et 19´ restent bornes et la constante´$\mu \geq 0$peut être choisie une fois pour toutes.

Demonstration :´ Il suffit de montrer que tout point de$\mathcal { C } ^ { \prime r , N }$à valeurs dans un trait et dont la gen´ erisation est dans´$\mathcal { C } _ { \varnothing } ^ { r , N }$et se relève en un point de$\mathcal { C } _ { N , \emptyset } ^ { r }$ se relève lui-même en un point de$\mathcal { C } _ { N } ^ { \prime r }$qui prolonge le prec´ edent.´

En effet, comme${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N } )$agit transitivement sur les fibres de$\mathcal { C } _ { N } ^ { \prime r }$ $\mathcal { C } ^ { \prime r , N }$et$\mathcal { C } _ { \varnothing } ^ { r , N }$est dense dans$\mathcal { C } ^ { \prime r , N }$, cela prouvera d’abord que$\mathcal { C } _ { N , \emptyset } ^ { r }$est dense dans$\mathcal { C } _ { N } ^ { \prime r }$puis que$\mathcal { C } _ { N } ^ { \prime r }$est propre donc fini sur$\mathcal { C } ^ { \prime r , N }$. Cela implique que $\mathcal { C } _ { N } ^ { \prime r } \to \mathrm { \bar { C } } ^ { \prime r , N }$est plat puisque d’après le lemme III.10 son rang est constant et que$\mathcal { C } ^ { \prime r , N }$est lisse. Il en resulte que le compos´ e´$\mathfrak { C } _ { N } ^ { \prime r } \to \bar { \mathfrak { C } } ^ { \prime r , N } \overset { \cdot } { \to } ( \mathbb { A } ^ { 1 } / \mathbb { G } _ { m } ) ^ { r - 1 }$ est plat, donc lisse puisque ses fibres sont lisses.

Considerons donc un anneau de valuation discrète´ A de corps des fractions K et un point de$\mathcal { C } ^ { \prime r , N }$à valeurs dans$S = \operatorname { S p e c } A$consistant en les donnees suivantes :´

• un fibre´$\mathcal { F }$de rang r sur$N \times S .$

• des$( { \mathcal { L } } _ { 1 } , \ell _ { 1 } ) , \ldots , ( { \mathcal { L } } _ { r - 1 } , \ell _ { r - 1 } )$sur S,

• un homomorphisme complet$\begin{array} { l } { \displaystyle \tau _ { \mathcal { F } } \Rightarrow \mathcal { F } } \end{array}$qui s’ecrit sous la forme´ d’homomorphismes lineaires partout non nuls´

$$
u _ {s}: ^ {\tau} \left(\Lambda^ {s} \mathcal {F} \otimes \bigotimes_ {t <   s} \mathcal {L} _ {t} ^ {\otimes (s - t)}\right)\rightarrow \Lambda^ {s} \mathcal {F} \otimes \bigotimes_ {t <   s} \mathcal {L} _ {t} ^ {\otimes (s - t)}, 1 \leq s \leq r,
$$

tels que Ker$u _ { s }$et <sup>τ</sup> Im$u _ { s }$soient partout en somme directe.

On suppose que la gen´ erisation de ce point est dans´$\mathcal { C } _ { \varnothing } ^ { r , N }$, ce qui signifie que sur$N \times S$pec K les$u _ { s }$sont partout des isomorphismes, et qu’elle se relève dans$\mathcal { C } _ { N , \emptyset } ^ { r }$. Ce relèvement consiste en des isomorphismes

$$
v _ {s}: \Lambda^ {s} \mathcal {F} \otimes \bigotimes_ {t <   s} \mathcal {L} _ {t} ^ {\otimes (s - t)} \to \Lambda^ {s} \left(\mathcal {O} _ {N \times S} ^ {r}\right), \quad 1 \leq s \leq r,
$$

bien definis sur´ N × Spec K et qui verifient´

$$
\tau (v _ {s}) = v _ {s} \circ u _ {s}, \quad 1 \leq s \leq r.
$$

Il s’agit de prouver que les$v _ { s }$sont bien definis en tant qu’homomorphismes´ sur N × Spec A et que leurs specialisations sont non nulles en tout point´ de N.

Pour tout s,$1 \leq s \leq r$, notons$\varphi _ { s }$l’isomorphisme τ-lineaire de l’espace´ $[ \Lambda ^ { s } \mathcal { F } \otimes \bigotimes _ { t < s } \mathcal { L } _ { t } ^ { \otimes ( s - t ) } ] \otimes _ { A } K$qui est induit par l’isomorphisme$u _ { s }$. Sur cet espace, il existe une unique valuation$\deg _ { \varphi _ { s } }$telle que

$$
\deg_ {\varphi_ {s}} \left(\varphi_ {s} (e)\right) = q \deg_ {\varphi_ {s}} (e), \quad \forall e \in \left[ \Lambda^ {s} \mathcal {F} \otimes \bigotimes_ {t <   s} \mathcal {L} _ {t} ^ {\otimes (s - t)} \right] \otimes_ {A} K
$$

(voir la demonstration du lemme 3 du paragraphe 2a de [Lafforgue, 1998´ ]). Comme$u _ { s }$stabilise le reseau´$\Lambda ^ { s } \mathcal { F } \otimes \bigotimes _ { t < s } \mathcal { L } _ { t } ^ { \otimes ( s - t ) }$, on a

$$
\deg_ {\varphi_ {s}} (e) \geq 0, \quad \forall e \in \Lambda^ {s} \mathcal {F} \otimes \bigotimes_ {t <   s} \mathcal {L} _ {t} ^ {\otimes (s - t)},
$$

et comme Ker$u _ { s }$et <sup>τ</sup> Im$u _ { s }$sont en somme directe partout, on peut trouver pour tout point ferme de´$N \times S$un el´ ement´$e$du facteur associe de´$\Lambda ^ { s } { \mathcal { F } } \otimes$ $\bigotimes \mathcal { L } _ { t } ^ { \otimes ( s - t ) }$qui verifie´$\deg _ { \varphi _ { s } } ( e ) = 0$

L’isomorphisme$v _ { s }$transforme necessairement la valuation´$\deg _ { \varphi _ { s } }$de $[ \Lambda ^ { s } { \mathcal { F } } \otimes \bigotimes _ { t < s } { \mathcal { L } } _ { t } ^ { \otimes ( s - t ) } ] \otimes _ { A } K$en la valuation canonique de$\Lambda ^ { s } ( { \mathcal { O } } _ { N } ^ { r } \otimes K )$ Donc il envoie le reseau´$\Lambda ^ { s } \mathcal { F } \otimes \bigotimes _ { t < s } \mathcal { L } _ { t } ^ { \otimes ( s - t ) }$dans le reseau´$\Lambda ^ { s } ( \mathcal { O } _ { N } ^ { r } \otimes A )$et en tout point ferme de´$N \times S$sa reduction n’est pas nulle. C’est ce´$\mathrm { \ q u ^ { \prime } }$on voulait.!"

Il est facile de completer la proposition ci-dessus par :´

Corollaire III.12. – Pour tout niveau$N ^ { \prime } = \sec { \mathcal { O } _ { N ^ { \prime } } } \hookrightarrow X$qui contient N comme sous-schema ferm´ e et a même support, on a un diagramme´ commutatif:

![](images/page_78_image_6.jpg)

Le morphisme induit

$$
\mathcal {C} _ {N ^ {\prime}} ^ {\prime r} \to \mathcal {C} ^ {\prime r, N ^ {\prime}} \times_ {\mathcal {C} ^ {\prime r, N}} \mathcal {C} _ {N} ^ {\prime r}
$$

est representable, fini et plat et il est muni d’une action du groupe fin´ i Ker$[ \mathrm { G L } _ { r } ( \mathcal { O } _ { N ^ { \prime } } )  \mathrm { G L } _ { r } ( \mathcal { O } _ { N } ) ]$qui est transitive sur ses fibres.!"

D’autre part, on a le lemme important :

Lemme III.13. – Pour d un entier et p un polygone de troncature, notons $\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } } }$l’ouvert de$\operatorname { C h t } ^ { r , d , \overline { { p } } \leq p } \times _ { X \times X } ( X - N ) \times ( X - N )$defini comme´ image reciproque de´$\mathcal { C } ^ { \prime r , N }$via le morphisme de restriction

$$
\overline {{\operatorname{Cht} ^ {r , d , \overline {{p}} \leq p}}} \times_ {X \times X} (X - N) \times (X - N) \rightarrow \mathcal {C} ^ {r, N}.
$$

Alors, pour toute partition$\underline { { r } } = ( r = r _ { 1 } + \cdot \cdot \cdot + r _ { k } )$, la trace de$\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } } }$ dans la strate$\mathrm { C h t } _ { \underline { { r } } } ^ { r , d , \bar { \overline { { p } } } \leq p }$est l’image reciproque de´$( X - N ) \times ( X - N ) ^ { k - 1 } \times$ $( X - N )$via

$$
\operatorname{Cht} _ {\underline {{r}}} ^ {r, d, \overline {{p}} \leq p} \rightarrow X \times X ^ {k - 1} \times X;
$$

autrement dit, elle est definie en demandant que pôle, z´ ero et d´ eg´ en´ erateurs´ evitent le niveau N.´

Demonstration :´ Soit$\widetilde { \mathcal { E } } \ = \ ( \mathcal { E } \ \hookrightarrow \ \mathcal { E } ^ { \prime } \  \ \mathcal { E } ^ { \prime \prime } \ \Leftarrow \ \ ^ { \tau } \mathcal { E } )$un point de $\mathrm { C h t } _ { r } ^ { r , d , \overline { { p } } \leq p } \times _ { X \times X } ( X - N ) \times ( X - N ) \mathrm { ~ e t ~ } \widetilde { \mathcal { F } } = ( \mathcal { F }  \tau _ { \mathcal { F } } )$son image dans$\mathcal { C } _ { \underline { { r } } } ^ { r , N }$. Les fibres´ E et$\tau _ { \mathcal { E } }$sont munis des filtrations canoniques$( \mathcal { E } _ { s } )$et $( \overline { { \mathcal { E } } } _ { s } )$tandis que leurs restrictions$\mathcal F = \mathcal E \otimes _ { \mathcal O _ { \boldsymbol X } } \mathcal O _ { \boldsymbol N }$et$\tau _ { \mathcal { F } }$sont munies des filtrations induites$( \mathcal { F } _ { s } = \mathcal { E } _ { s } \otimes _ { \mathcal { O } _ { X } } \mathcal { O } _ { N } )$et$( \overline { { \mathcal { F } } } _ { s } = \overline { { \mathcal { E } } } _ { s } \otimes _ { \mathcal { O } _ { X } } \mathcal { O } _ { N } )$. Pour tout $s \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + }$, les sous-fibres´$\tau _ { \mathcal { E } _ { s } }$et$\overline { { \mathcal { E } } } _ { s }$de$\tau _ { \mathcal { E } }$sont gen´ eriquement en somme´ directe et le quotient${ } ^ { \tau } \mathcal { E } / ( ^ { \tau } \mathcal { E } _ { s } \oplus \overline { { \mathcal { E } } } _ { s } )$est supporte par un point exactement´ qui est le deg´ en´ erateur en rang´ s. Demander que ce deg´ en´ erateur´ evite´ N est donc equivalent à demander que´${ } ^ { \tau } \mathcal { F } = { } ^ { \tau } \mathcal { F } _ { s } \oplus \overline { { \mathcal { F } } } _ { s }$!"

Sur les champs de chtoucas iter´ es avec structures de niveau´ N, on sait maintenant :

Corollaire III.14. – Avec les notations de la definition´ III.8, soit$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p ^ { \prime } } } }$ l’ouvert de$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p }$image reciproque de l’ouvert´$\mathcal { C } _ { N } ^ { \prime r }$de$\mathcal { C } _ { N } ^ { r }$.

Alors$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p ^ { \prime } } } }$est representable, fini et plat au-dessus de l’ouvert´ $\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } } }$de$\overline { { \mathrm { C h t } ^ { r , d , \overline { { { p } } } \leq p } } }$et le groupe fini${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N } )$agit transitivement sur ses fibres.

Si le polygone de troncature p est assez convexe enfonction de$( X e t ) \ N$ $\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$est lisse sur$( X - N ) \times ( X - N ) \times ( \mathbb { A } ^ { 1 } / \mathbb { G } _ { m } ) ^ { k - 1 }$!"

Bien sûr, on notera aussi${ \overline { { \mathrm { C h t } _ { N } ^ { r , { \overline { { p } } } \leq p ^ { \prime } } } } } = \coprod _ { d \in \mathbb { Z } } { \overline { { \mathrm { C h t } _ { N } ^ { r , d , { \overline { { p } } } \leq p ^ { \prime } } } } }$

## c) Resolution des singularit´ es pour les niveaux sans multiplicit´ es´

Dans le cas d’un niveau$N = \operatorname { S p e c } { \mathcal { O } } _ { N } \hookrightarrow X$sans multiplicites c’est-à-dire´ reduit, nous allons construire ici une r´ esolution des singularit´ es du champ´ $\mathcal { C } _ { N } ^ { r }$qui prolonge le revêtement de Lang de$\mathcal { C } _ { \varnothing } ^ { r , N }$au-dessus de$\mathcal { C } ^ { r , N }$

On commence par un resultat pr´ eparatoire qui vaut pour un niveau´ N arbitraire. On note$( \Omega ^ { r , 1 } ) ^ { N }$et$( \mathcal { A } ^ { r , 1 } ) ^ { N } = ( \mathbb { A } ^ { r - 1 } ) ^ { N } = ( \mathbb { A } ^ { N } ) ^ { r - 1 }$les schemas d´ eduits´ de$\boldsymbol { \Omega } ^ { r , 1 }$et$\begin{array} { r } { \mathcal { A } ^ { r , 1 } = \mathbb { A } ^ { r - 1 } } \end{array}$par restriction des scalaires à la Weil de$\mathcal { O } _ { N } \hat { \mathrm { ~ a ~ } } \mathbb { F } _ { q }$. Ils sont munis d’actions des groupes$\mathbf { G } \mathbf { L } _ { r } ^ { N } \times \mathbf { G } \mathbf { L } _ { r } ^ { N } \times ( \mathbb { G } _ { m } ^ { N } ) ^ { r + 1 } / \mathbb { G } _ { m } ^ { N } \operatorname { e t } { ( \mathcal { A } _ { \varnothing } ^ { r , 1 } ) ^ { \setminus } } =$ $( \mathbb { G } _ { m } ^ { N } ) ^ { r - 1 } \cong ( \mathbb { G } _ { m } ^ { N } ) ^ { r + 1 } / ( \mathbb { G } _ { m } ^ { N } ) ^ { 2 }$et ils sont relies par un morphisme´ equivariant´

$$
(\Omega^ {r, 1}) ^ {N} \to (\mathcal {A} ^ {r, 1}) ^ {N}
$$

qui est lisse de dimension relative$r ^ { 2 } \dim ( { \mathcal { O } } _ { N } )$

On note aussi$a ~ : \mathcal { A } ^ { r , 1 } \to ( \mathcal { A } ^ { r , 1 } ) ^ { N }$le “plongement diagonal” induit par le morphisme N → Spec$\mathbb { F } _ { q } \det a ^ { q - 1 } : \mathring { \pmb { \mathscr { A } } } ^ { r , 1 } \to ( \pmb { \mathscr { A } } ^ { r , 1 } ) ^ { N }$son compose´ avec$\mathcal { A } ^ { r , 1 } = \mathbb { A } ^ { r - 1 } \to \mathbb { A } ^ { r - 1 } = \mathcal { A } ^ { r , 1 } : ( \lambda _ { 1 } , \dotsc , \lambda _ { r - 1 } ) \mapsto ( \lambda _ { 1 } ^ { q - 1 } , \dotsc , \lambda _ { r - 1 } ^ { q - 1 } )$

Le produit fibre´$( \Omega ^ { r , 1 } ) ^ { N } \times _ { ( \mathcal { A } ^ { r , 1 } ) ^ { N } , a ^ { q - 1 } } \mathcal { A } ^ { r , 1 }$est muni d’une action du groupe $\mathbf { G L } _ { r } ^ { N } \times \mathbf { G L } _ { r } ^ { N } \times \mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m }$. Si on compose cette action avec l’homomorphisme

$$
\mathrm{GL} _ {r} ^ {N} \rightarrow \mathrm{GL} _ {r} ^ {N} \times \mathrm{GL} _ {r} ^ {N}
$$

$$
g \mapsto (\tau (g), g)  ,
$$

on obtient une action de G$\boldsymbol { \mathsf { \Pi } } _ { r } ^ { N } \times \mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m }$dont le noyau est$\mathbb { G } _ { m } \cong \mathbb { G } _ { m } ^ { 2 } / \mathbb { G } _ { m }$ plonge par´$\lambda \mapsto ( \lambda , \lambda )$

Lemme III.15. – Le champ$\mathcal { C } ^ { r , N }$s’identifie à un ouvert du champ quotient du schema´

$$
(\Omega^ {r, 1}) ^ {N} \times_ {(\mathcal {A} ^ {r, 1}) ^ {N}, a ^ {q - 1}} \mathcal {A} ^ {r, 1}
$$

par l’action du groupe

$$
\left(\mathrm{GL} _ {r} ^ {N} \times \mathbb {G} _ {m} ^ {r + 1} / \mathbb {G} _ {m}\right) / \left(\mathbb {G} _ {m} \cong \mathbb {G} _ {m} ^ {2} / \mathbb {G} _ {m}\right).
$$

Demonstration :´ En effet, comme le schema´$\Omega ^ { r }$des homomorphismes complets est un quotient de$\boldsymbol { \Omega } ^ { r , 1 }$par$\mathcal { A } _ { \varnothing } ^ { r , 1 } = \mathbb { G } _ { m } ^ { r - 1 } \cong \mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m } ^ { 2 }$, on voit$\mathrm { \ q u ` u n }$ point du champ quotient ci-dessus à valeurs dans un schema´ S consiste en un fibre´$\mathcal { F }$de rang r sur$N \times S$muni d’un homomorphisme complet $\tau _ { \mathcal { F } } = ( \mathrm { I d } _ { N } \times \mathrm { F r o b } _ { S } ) ^ { * } \mathcal { F } \Rightarrow \mathcal { F }$dont l’image dans$( \mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 } ) ( N \times S ) =$ $( \mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \mathcal { G } } ^ { r , 1 } ) ^ { N } ( S )$provient via$a ^ { q - 1 }$d’un point de$( \mathcal { A } ^ { r , 1 } / \mathcal { A } _ { \varnothing } ^ { r , 1 } ) ( S )$

On remarque que l’exposant$q - 1$qui apparaît dans la definition de´ $\mathcal { C } ^ { r , N }$permet ici de se debarasser du choix de la section de´$\mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m } \to$ $\mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m } ^ { 2 } \cong \mathcal { A } _ { \varnothing } ^ { r , 1 }$qui est necessaire pour d´ efinir´$\Omega ^ { r }$!"

Le problème est donc de prolonger l’isogenie de Lang au-dessus de´ $( \Omega ^ { r , 1 } ) ^ { \hat { N } } \times _ { ( \mathcal { A } ^ { r , 1 } ) ^ { N } , a ^ { q - 1 } } \mathcal { A } ^ { r , 1 }$en un morphisme equivariant et projectif dont´ la source est lisse absolument. Ce problème a et´ e r´ esolu dans le dernier´ paragraphe 4d de l’article [Lafforgue, 1999] en ce qui concerne$\boldsymbol { \Omega } ^ { r , 1 }$. Cela utilise l’existence et les propriet´ es des compactifications´$\overline { { \Omega } } ^ { r , n }$des quotients PG$\boldsymbol { \mathsf { \Pi } } _ { r } ^ { n + 1 } / \mathrm { P G L } _ { r }$introduites dans cet article dans les cas$n = 1$et$n = 2$ qui sont entièrement corrects. On renvoie par exemple à la prepublication´ [Lafforgue, mars 2001] pour une demonstration complète des r´ esultats de´ lissite dont nous allons nous servir ici.´

Rappelons que pour$n = 1$ou 2, nous avons construit une compactification projective equivariante´$\overline { { \Omega } } ^ { r , n }$de$\overline { { \Omega } } _ { \varnothing } ^ { r , n } = ( \mathrm { P G L } _ { r } ) ^ { n + 1 } / \mathrm { P G L } _ { r }$muni de l’action à gauche de$\mathrm { P G L } _ { r } ^ { n + 1 }$

Au-dessus de$\overline { { \Omega } } ^ { r , n }$, il y a un torseur$\Omega ^ { r , n }$sous un tore$\mathcal { T } ^ { r , n } = \mathbb { G } _ { m } ^ { S ^ { r , n } } / \mathbb { G } _ { m }$ qui est muni$\mathrm { d } ^ { \prime }$une action compatible de G$\boldsymbol { \mathsf { \Pi } } _ { r } ^ { n + 1 }$ainsi que d’un morphisme lisse et equivariant sur une vari´ et´ e torique´$\mathbf { \mathcal { A } } ^ { r , n }$dont le tore$\mathcal { A } _ { \varnothing } ^ { r , n }$est un quotient de$\mathcal { T } ^ { r , n }$par un sous-tore$\mathcal { T } _ { \varnothing } ^ { r , n } \cong \mathbb { G } _ { m } ^ { n + 1 } / \mathbb { G } _ { m }$. La fibre de$\Omega ^ { r , n }$audessus de l’unite de ce tore´$\mathcal { A } _ { \varnothing } ^ { r , n }$s’identifie naturellement$\dot { \mathrm { ~ a ~ } } \mathrm { G L } _ { r } ^ { n + 1 } / \mathrm { G L } _ { r }$

Pour$n ^ { \prime }$un second entier$\leq 2$et$\iota ~ : \{ 0 , \dots , n ^ { \prime } \} \to \{ 0 , \dots , n \}$une application, on a des morphismes induits

$$
\mathcal {T} ^ {r, n} \to \mathcal {T} ^ {r, n ^ {\prime}}, \mathcal {A} ^ {r, n} \to \mathcal {A} ^ {r, n ^ {\prime}}, \Omega^ {r, n} \to \Omega^ {r, n ^ {\prime}}, \overline {{\Omega}} ^ {r, n} \to \overline {{\Omega}} ^ {r, n ^ {\prime}},
$$

tous compatibles entre eux et avec les morphismes

$$
\mathrm{GL} _ {r} ^ {n + 1} \rightarrow \mathrm{GL} _ {r} ^ {n ^ {\prime} + 1}, \mathrm{PGL} _ {r} ^ {n + 1} \rightarrow \mathrm{PGL} _ {r} ^ {n ^ {\prime} + 1}.
$$

Dans le cas$\mathrm { d } ^ { \prime }$un application injective$\iota : \{ 0 , 1 \}  \{ 0 , 1 , 2 \}$, le morphisme induit

$$
\Omega^ {r, 2} \to \Omega^ {r, 1} \times_ {\mathcal {A} ^ {r, 1}} \mathcal {A} ^ {r, 2}
$$

est lisse de dimension relative$r ^ { 2 }$

Considerons maintenant un niveau´$N = \mathrm { S p e c } \mathcal { O } _ { N } \hookrightarrow X { \mathrm { q u } } ^ { \prime }$on suppose reduit et donc´ etale sur Spec´$\mathbb { F } _ { q }$. Pour$n = 1$ou 2, on note$\overline { { \Omega } } ^ { r , N , n } , \Omega ^ { r , N , n }$，$\mathcal { T } ^ { r , N , n } , \mathcal { A } ^ { r , N , n } , \ldots$. les schemas d´ eduits de´$\overline { { \Omega } } ^ { r , n } , \Omega ^ { r , n } , \mathcal { T } ^ { r , n } , \mathcal { A } ^ { r , n }$par restriction des scalaires à la Weil de$\mathcal { O } _ { N }$à$\mathbb { F } _ { q }$. Il resulte de l’hypothèse que´$N$est reduit que´$\overline { { \Omega } } ^ { r , N , 1 } \mathrm { e t } \overline { { \Omega } } ^ { r , N , 2 }$sont projectifs tout comme$\overline { { \Omega } } ^ { r , 1 } \mathrm { e t } \overline { { \Omega } } ^ { r , 2 }$

Si$\iota _ { \alpha , \beta } ~ : ~ \{ 0 , 1 \} ~  ~ \{ 0 , 1 , 2 \} , ~ 0 ~ \mapsto ~ \alpha , ~ 1 ~ \mapsto ~ \beta _ { 1 }$est une application injective, on designera par´$p _ { \alpha , \beta }$n’importe lequel des morphismes induits $\bar { \Omega ^ { r , N , 2 } } \to \Omega ^ { r , N , 1 } , \bar { \mathcal { A } ^ { r , N , 2 } } \to \bar { \mathcal { A } ^ { r , N , 1 } }$, etc.

Soient$\mathcal { T } ^ { r , N , \tau } , \mathcal { T } _ { \varnothing } ^ { r , N , \tau } \operatorname { e t } \mathcal { A } _ { \varnothing } ^ { r , N , \tau }$les plus grands sous-tores de$\mathcal { T } ^ { r , N , 2 } , \mathcal { T } _ { \varnothing } ^ { r , N , 2 }$ et$\mathcal { A } _ { \varnothing } ^ { r , N , 2 }$qui verifient l’´ equation´

$$
p _ {0, 2} = \operatorname{Frob} \circ p _ {0, 1}
$$

dans$\mathcal { T } ^ { r , N , 1 } , \mathcal { T } _ { \varnothing } ^ { r , N , 1 }$et$\mathbf { \mathcal { A } } _ { \boldsymbol { \varnothing } } ^ { r , N , 1 }$. Alors$\mathcal { T } _ { \varnothing } ^ { r , N , \tau }$est isomorphe à$( \mathbb { G } _ { m } ^ { N } ) ^ { 2 } / \mathbb { G } _ { m } ^ { N } , \mathrm { c } ^ { \mathrm { \large ~ , ~ } }$est un sous-tore de${ \mathcal { T } } ^ { r , N , \tau }$et leur quotient${ \bf s } '$identifie à$\mathbf { \mathcal { A } } _ { \boldsymbol { \mathcal { A } } } ^ { r , N , \tau }$

Soit$\mathcal { A } ^ { r , N , \tau }$la variet´ e torique de tore´$\mathcal { A } _ { \varnothing } ^ { r , N , \tau }$qui est la normalisation de l’adherence sch´ ematique de celui-ci dans´$\mathcal { A } ^ { r , N , 2 }$. Ainsi$\mathcal { A } ^ { r , N , \tau }$est-elle le noyau du diagramme

$$
\mathcal {A} ^ {r, N, 2} \xrightarrow [ \text {Frob} \circ p _ {0 , 1} ]{p _ {0 , 2}} \mathcal {A} ^ {r, N, 1}
$$

dans la categorie des vari´ et´ es toriques normales.´

Nous pouvons enoncer :´

Proposition III.16. – Etant donne N un niveau r´ eduit, soit´$\Omega ^ { r , N , \tau }$le sousschemaferm´ e de´$\Omega ^ { r , N , 2 } \times _ { \mathcal { A } ^ { r , N , 2 } } \mathcal { A } ^ { r , N , \tau }$defini par l’´ equation´

$$
p _ {0, 2} = \operatorname{Frob} \circ p _ {0, 1}
$$

dans$\Omega ^ { r , N , 1 }$

Il est muni d’actions du groupe algebrique´$\mathrm { G L } _ { r } ^ { N }$, du groupefini${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N } )$ et du tore${ \mathcal { T } } ^ { r , N , \tau }$commutant entre elles et d’un morphisme equivariant´

$$
\Omega^ {r, N, \tau} \to \mathcal {A} ^ {r, N, \tau}
$$

qui est lisse et dont lafibre au-dessus de l’unite du tore´$\mathcal { A } _ { \varnothing } ^ { r , N , \tau }$s’identifie à

$$
\operatorname{Ker} \left[ \left(\mathrm{GL} _ {r} ^ {N}\right) ^ {3} / \mathrm{GL} _ {r} ^ {N} \xrightarrow [ \text {Frob} \circ p _ {0 , 1} ]{p _ {0 , 2}} \left(\mathrm{GL} _ {r} ^ {N}\right) ^ {2} / \mathrm{GL} _ {r} ^ {N} \right].
$$

Enfin, le quotient$\overline { { \Omega } } ^ { r , N , \tau }$de$\Omega ^ { r , N , \tau }$par l’action libre du tore${ \mathcal { T } } ^ { r , N , \tau }$est projectif.

Demonstration :´ Le schema´$\Omega ^ { r , N , \tau }$est muni d’une action du groupe

$$
\operatorname{Ker} \left[ \left(\mathrm{GL} _ {r} ^ {N}\right) ^ {3} \xrightarrow [ \text {Frob} \circ p _ {0 , 1} ]{p _ {0 , 2}} \left(\mathrm{GL} _ {r} ^ {N}\right) ^ {2} \right]
$$

qui, via la projection de$( \mathbf { G L } _ { r } ^ { N } ) ^ { 3 }$sur ses deux premiers facteurs, est isomorphe à$\mathrm { \bf G L } _ { r } ^ { N } ( \mathbb { F } _ { q } ) \times \mathrm { \bf G L } _ { r } ^ { N } = \mathrm { \bf G L } _ { r } ( \mathcal { O } _ { N } ) \times \mathrm { \bf G L } _ { r } ^ { N }$

Il est lisse sur$\mathcal { A } ^ { r , N , \tau }$puisque$\Omega ^ { r , N , 2 } \ \to \ { \mathcal A } ^ { r , N , 2 }$et$p _ { 0 , 2 } : \Omega ^ { r , N , 2 } \ \to$ $\Omega ^ { r , N , 1 } \times _ { \mathcal { A } ^ { r , N , 1 } } \mathcal { A } ^ { r , N , 2 }$sont lisses et par transversalite des morphismes de´ Frobenius et des morphismes lisses.

Enfin,$\overline { { \Omega } } ^ { r , N , \tau }$est projectif car${ \mathrm { c } } '$est un schema fini sur´$\overline { { \Omega } } ^ { r , N , 2 }$

On peut considerer les deux morphismes´

$$
\Omega^ {r, N, \tau} \underset {p _ {0, 2} = \text {Frob} \circ p _ {0, 1}} {\overset {p _ {2, 1}} {\longrightarrow}} \Omega^ {r, N, 1} .
$$

Au-dessus des el´ ements unit´ es de´$\mathbf { \mathcal { A } } _ { \boldsymbol { \varnothing } } ^ { r , N , \tau }$et$\begin{array} { r } { \mathcal { A } _ { \varnothing } ^ { r , N , 1 } , p _ { 0 , 2 } = \operatorname { F r o b } \circ p _ { 0 , } } \end{array}$est un isomorphisme sur$( \mathbf { G L } _ { r } ^ { N } ) ^ { 2 } / \mathbf { G L } _ { r } ^ { N } \cong \mathbf { G L } _ { r } ^ { N }$tandis que$p _ { 2 , 1 }$s’identifie à l’isogenie de Lang´

$$
\mathrm{GL} _ {r} ^ {N} \to \mathrm{GL} _ {r} ^ {N}: g \mapsto \tau (g) ^ {- 1} \circ g.
$$

On deduit de la proposition ci-dessus :´

Theor´ eme III.17.\` – Soit$N = { \sf S }$pec$\mathcal { O } _ { N }$un niveau reduit.´

Alors il existe un champ algebrique´$\widetilde { \mathcal { C } } _ { N } ^ { r }$au-dessus de$\mathcal { C } ^ { r , N }$tel que :

$\widetilde { \mathcal { C } } _ { N } ^ { r }$est representable et projectif sur´$\mathcal { C } ^ { r , N }$

• sa restriction au-dessus de l’ouvert dense$\mathcal { C } _ { \varnothing } ^ { r , N }$de$\mathcal { C } ^ { r , N }$s’identifie au revêtement de Lang$\mathcal { C } _ { N , \emptyset } ^ { r } ,$

$\widetilde { \mathcal { C } } _ { N } ^ { r }$est muni d’un morphisme lisse sur le champ torique$\widetilde { \mathcal { A } } ^ { r , N } / \mathcal { A } _ { \varnothing } ^ { r , N }$ quotient d’une variet´ e torique lisse´$\displaystyle \widetilde { \mathcal { A } } ^ { r , N }$par son tore$\mathbf { \mathcal { A } } _ { \boldsymbol { \mathcal { G } } } ^ { r , N }$(avec la propriet´ e que´$\mathcal { C } _ { N , \emptyset } ^ { r }$soit l’image reciproque de´$\mathcal { A } _ { \varnothing } ^ { r , N } / \mathcal { A } _ { \varnothing } ^ { r , N } )$

Demonstration :´ D’après le lemme III.15, on est ramene au problème de´ compactifier l’isogenie de Lang au-dessus de´$\Omega ^ { r , N , 1 } \times { _ { \mathcal { A } ^ { r , N , 1 } , a ^ { q - 1 } } } \mathbf { \hat { \mathcal { A } } } ^ { r , 1 }$. Dans la proposition III.16, une telle compactification$\Omega ^ { r , N , \tau }$est construite au-dessus de$\dot { \boldsymbol \Omega } ^ { r , N , 1 }$; on doit donc modifier la base$\mathcal { A } ^ { r , N , \tau }$de$\Omega ^ { r , N , \tau }$

Soient$\mathcal { T } ^ { r , N } , \mathcal { T } _ { \varnothing } ^ { r , N }$et$\mathcal { A } _ { \varnothing } ^ { r , N }$les composantes neutres des produits fibres´ $\begin{array} { r } { \mathcal { T } ^ { r , N , \tau } \ \times _ { p _ { 2 , 1 } , \mathcal { T } ^ { r , N , 1 } , a ^ { q - 1 } } \ \mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } , \mathcal { T } _ { \varnothing } ^ { r , N , \tau } \ \times _ { p _ { 2 , 1 } , \mathcal { T } _ { \varnothing } ^ { r , N , 1 } , a ^ { q - 1 } } \ \mathbb { G } _ { m } ^ { 2 } / \mathbb { G } _ { m } } \end{array}$et$\mathbf { \mathcal { A } } _ { \boldsymbol { \mathcal { A } } } ^ { r , N , \tau }$ $\times _ { p _ { 2 , 1 } , \mathcal { A } _ { \mathcal { A } } ^ { r , N , 1 } , a ^ { q - 1 } } \mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m } ^ { 2 }$. Ce sont trois tores,$\mathcal { T } _ { \varnothing } ^ { r , N }$est un sous-tore de$\mathcal { T } ^ { r , N }$ isomorphe à$\mathbb { G } _ { m } ^ { 2 } / \mathbb { G } _ { m }$$\mathbf { \mathcal { A } } _ { \boldsymbol { \emptyset } } ^ { r , N }$s’identifie au quotient$\mathcal { T } ^ { r , N } / \mathcal { T } _ { \varnothing } ^ { r , N }$

Soit alors$\mathcal { A } ^ { r , N }$la variet´ e torique qui est la normalisation de l’adh´ erence´ schematique de´$\mathbf { \mathcal { A } } _ { \boldsymbol { \mathcal { G } } } ^ { r , N }$dans le produit fibre´

$$
\mathcal {A} ^ {r, N, \tau} \times_ {p _ {2, 1}, \mathcal {A} ^ {r, N, 1}, a ^ {q - 1}} \mathcal {A} ^ {r, 1}.
$$

Autrement dit, on a dans la categorie des vari´ et´ es toriques normales un carr´ e´ cartesien :´

$$
\begin{array}{c} \mathcal {A} ^ {r, N} \xrightarrow {} \mathcal {A} ^ {r, 1} \\ \Biggl \downarrow \qquad \qquad \square \qquad \Biggl \downarrow a ^ {q - 1} \\ \mathcal {A} ^ {r, N, \tau} \xrightarrow [ p _ {2 , 1} ]{} \mathcal {A} ^ {r, N, 1} \end{array}
$$

Le produit fibre´$\Omega ^ { r , N , \tau } \times _ { \mathcal { A } ^ { r , N , \tau } } \mathcal { A } ^ { r , N }$est muni d’une action de GL$\begin{array} { r } { \mathbf { \mathcal { \mathbf { \Phi } } } _ { \prime r } ^ { N } \times \mathcal { T } ^ { r , N } \times \mathbf { \Psi } } \end{array}$ ${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N } )$dont le noyau est isomorphe à$\mathbb { G } _ { m } \cong \mathcal { T } _ { \varnothing } ^ { r , N }$et d’un morphisme equivariant lisse sur la vari´ et´ e torique´$\mathcal { A } ^ { r , N }$de tore$\bar { \mathcal { A } } _ { \varnothing } ^ { r , N } \cong \mathcal { T } ^ { r , N } / \mathcal { T } _ { \varnothing } ^ { r , N }$

Par construction, on a un homomorphisme

$$
\mathcal {T} ^ {r, N} \to \mathbb {G} _ {m} ^ {r + 1} / \mathbb {G} _ {m},
$$

un morphisme equivariant de vari´ et´ es toriques´

$$
\mathcal {A} ^ {r, N} \to \mathcal {A} ^ {r, 1} = \mathbb {A} ^ {r - 1}
$$

et, au-dessus de celui-ci, un morphisme

$$
p _ {2, 1}: \Omega^ {r, N, \tau} \times_ {\mathcal {A} ^ {r, N, \tau}} \mathcal {A} ^ {r, N} \to \Omega^ {r, N, 1} \times_ {\mathcal {A} ^ {r, N, 1}, a ^ {q - 1}} \mathcal {A} ^ {r, 1}
$$

qui est equivariant relativement aux actions de´$\mathbf { G L } _ { r } ^ { N } \times \mathcal { T } ^ { r , N } \times \mathbf { G L } _ { r } ( \mathcal { O } _ { N } )$et de$\mathbf { G L } _ { r } ^ { N } \times \mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m }$via l’homomorphisme$\mathcal { T } ^ { r , N } \to \mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m }$

Le champ quotient de$\Omega ^ { r , N , \tau } \times _ { \mathcal { A } ^ { r , N , \tau } } \mathcal { A } ^ { r , N }$par l’action de$( \mathbf { G L } _ { r } ^ { N } \times \mathcal { T } ^ { r , N } ) /$ $( \mathbb { G } _ { m } \cong \mathcal { T } _ { \varnothing } ^ { r , N } )$verifie les propri´ et´ es suivantes :´

• il est muni d’un morphisme representable projectif sur le champ quotient´ de$\Omega ^ { r , N , 1 } \times \mathcal { A } ^ { r , N , 1 } , a ^ { q - 1 } \mathcal { A } ^ { r , 1 }$par l’action de$( \mathbf { G L } _ { r } ^ { N } \times \mathbb { G } _ { m } ^ { r + 1 } / \mathbb { G } _ { m } ) / ( \mathbb { G } _ { m } \cong$ $\mathbb { G } _ { m } ^ { 2 } / \mathbb { G } _ { m } )$(lequel contient$\mathcal { C } ^ { r , N }$comme sous-champ ouvert d’après le lemme III.15),

• sa restriction au-dessus de l’ouvert dense$\mathfrak { C } _ { \varnothing } ^ { r , N } \cong \mathrm { G L } _ { r } ^ { N } / \tau / \mathrm { G L } _ { r } ^ { N }$s’identifie au revêtement de Lang$\mathcal { C } _ { N , \emptyset } ^ { r } \cong \mathbf { G } \mathbf { L } _ { r } ^ { N } / \tilde { \mathbf { G } } \mathbf { L } _ { r } ^ { N }$

• il est lisse sur le champ torique$\mathcal { A } ^ { r , N } / \mathcal { A } _ { \varnothing } ^ { r , N }$

Pour conclure, il suffit$\mathrm { d } ^ { \prime }$une part de se restreindre au-dessus de l’ouvert$\mathcal { C } ^ { r , N }$et d’autre part de proceder au changement de base consistant à´ remplacer la variet´ e torique´$\mathbf { \mathcal { A } } ^ { r , N }$par une resolution des singularit´ es´$\displaystyle \widetilde { \mathcal { A } } ^ { r , N }$ comme suit :

Lemme III.18. – Etant donnee une vari´ et´ e torique´$\mathcal { A }$de tore$\mathcal { A } _ { \emptyset }$definie´ sur un corps F, il existe une variet´ e torique´$\mathcal { \widetilde A }$de même tore$\mathcal { A } _ { \emptyset }$qui est lisse et telle que l’identite de´$\mathcal { A } _ { \emptyset }$se prolonge en un morphisme equivariant et´ projectif$\mathcal { A }  \mathcal { A }$

Demonstration :´ Si le tore$\mathcal { A } _ { \emptyset }$est deploy´ e,´${ \mathrm { c } } ^ { \prime }$est le contenu du theorème 11´ de [Saint-Donat]. La demonstration consiste à consid´ erer l’´ eventail associ´ e´ à A (c’est une decomposition en cellules qui sont des cônes convexes´ polyedraux rationnels´$\bar { \mathrm { d } ^ { \flat } }$un certain cône polyedral dans un espace vectoriel´ de dimension finie sur R muni$\mathrm { d } '$une structure entière) et à montrer qu’il est toujours possible de subdiviser un tel eventail en un autre plus fin dont les´ cellules munies de leurs structures entières sont toutes des simplexes.

Si le tore$\mathcal { A } _ { \emptyset }$n’est pas deploy´ e, choisissons une extension finie´ galoisienne$\mathbb { F } ^ { \prime }$de F telle que$\mathcal { A } _ { \varnothing } \ \otimes _ { \mathbb { F } } \ \mathbb { F } ^ { \prime }$soit deploy´ e. A la vari´ et´ e torique´ $\mathcal { A } \otimes _ { \mathbb { F } } \mathbb { F } ^ { \prime }$correspond un eventail´ X muni d’une action du groupe de Galois fini$G$de$\mathbb { F } ^ { \prime }$sur F. Il s’agit de prouver qu’il est possible de subdiviser$\mathfrak { X }$en un autre eventail´$\widetilde { \mathfrak { X } }$dont les cellules munies de leurs structures entières sont des simplexes et qui de plus est respecte par l’action de´$G$

Tout d’abord, on peut subdiviser$\mathfrak { X }$en un eventail´$\mathcal { X } ^ { \prime }$egalement respect´ e´ par$G$et tel que pour toute cellule$\sigma$et tout el´ ement´$g$de$G$qui stabilise $\sigma$l’action de g sur$\sigma$est triviale. On remarque que toute subdivision de$\mathcal { X } ^ { \prime }$ respectee par´$G$verifiera la même propri´ et´ e.´

On construit alors$\widetilde { \mathfrak { X } }$à partir de$\mathcal { X } ^ { \prime }$en recopiant la demonstration qui est´ donnee dans [Saint-Donat] : la seule diff´ erence est´$\mathrm { \ q u ^ { \prime } }$on complète chaque nouvelle subdivision en la combinant avec toutes les subdivisions images sous l’action de$G$!"

Bien sûr, rien n’empêche de poser :

Conjecture III.19. – Pour$N \sb { \textnormal { \textsf { C l e c } } } { \mathcal { O } } _ { N } \hookrightarrow X$un niveau arbitraire, il existe un champ algebrique´$\bar { \mathcal { C } } _ { N } ^ { r }$au-dessus de$\mathcal { C } ^ { r , N }$qui verifie les propri´ et´ es´ du theorème III.17.´

Remarque : Tout comme$\mathcal { C } ^ { r , N }$, la normalisation$\mathcal { C } _ { N } ^ { r }$de$\mathcal { C } ^ { r , N }$dans$\mathcal { C } _ { N , \emptyset } ^ { r }$ $\mathrm {  ~ s ~ } ^ { \prime }$ecrit comme le champ quotient par´$\mathbf { G L } _ { r } ^ { N } \times \mathbb { G } _ { m } ^ { r - 1 }$d’un schema quasi-´ projectif. Afin de resoudre la conjecture, il suffirait donc de savoir construir´ e une resolution des singularit´ es´ equivariante´$\mathrm { d } ^ { \prime }$un tel schema.´

C’est le cas quand$r = 2$car alors toutes les orbites sont de codimension 2 au plus et on peut appliquer le proced´ e connu de r´ esolution des singularit´ es´ des surfaces lequel est canonique et donc respecte les actions de groupes.

Quand N a des multiplicites, ce problème est li´ e à celui de construire des´ compactifications lisses des$\mathrm { P G L } _ { r } ^ { n + 1 } / \mathrm { P G L } _ { r }$pour tous les entiers n. L’auteur avait cru resoudre ce problème dans l’article [Lafforgue, 1999] mais i´ l s’est aperçu que l’enonc´ e de lissit´ e contenu dans cet article (le th´ eorème 6 du´ paragraphe 1c) est faux pour$n \geq 3$!"

Lorsqu’il existe un champ algebrique´$\widetilde { \mathcal { C } } _ { N } ^ { r }$verifiant les propri´ et´ es du´ theorème III.17 (par exemple si ´ N est reduit ou si ´$r \ = \ 2 )$, on definit´ des champs algebriques´$\mathrm { C h t } _ { N } ^ { r , \bar { d } , \overline { { p } } \leq p }$comme produits fibres dans des carr´ es´ cartesiens :´

$$
\begin{array}{c c c} \widetilde {\mathrm{Cht} _ {N} ^ {r , d , \overline {{p}} \leq p}} & \longrightarrow & \widetilde {\mathcal {C}} _ {N} ^ {r} \\ \Big \downarrow & & \Big \downarrow \\ \mathrm{Cht} ^ {r, d, \overline {{p}} \leq p} \times_ {X \times X} (X - N) \times (X - N) & \longrightarrow & \mathcal {C} ^ {r, N} \end{array}
$$

Chacun contient$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p }$comme ouvert dense. Il est representable pro-´ jectif sur$\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } \times _ { X \times X } ( X - N ) \times ( X - N )$et donc propre sur$( X - N ) \times$ $( X - N )$. Enfin, il est lisse sur$\mathfrak { F } ^ { r , N } / \mathcal { A } _ { \varnothing } ^ { r , N } \times ( X - N ) \times ( X - N )$; autrement dit, il est lisse sur$( X - N ) \times ( X - N )$et son bord$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } - \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p }$ est un diviseur à croisements normaux relatif.

Encore une fois, on pourra noter

$$
\widetilde {\mathrm{Cht} _ {N} ^ {r , \overline {{p}} \leq p}} = \coprod_ {d \in \mathbb {Z}} \widetilde {\mathrm{Cht} _ {N} ^ {r , d , \overline {{p}} \leq p}}.
$$

## Chapitre IV

## Formule des points fixes dans un ouvert instable

Le theorème des points fixes de Grothendieck-Lefschetz permet de´ donner un sens cohomologique au nombre des points fixes comptes avec multi-´ plicites d’une correspondance dans une vari´ et´ e projective et lisse : il identifie´ ce nombre à la somme alternee des traces des endomorphismes induits par´ la correspondance dans les espaces de cohomologie -adique de la variet´ e.´

Dans le cas d’une correspondance dans une variet´ e ouverte´$\mathfrak { X } _ { \varnothing }$lisse sur un corps de base fini, Deligne a conjecture que si on compose cette´ correspondance avec une puissance assez grande de l’endomorphisme de Frobenius, le nombre des points fixes est encore egal à la trace de l’action´ induite sur la somme alternee des espaces de cohomologie´ -adique à supports compacts. Pink a donne une d´ emonstration de cette conjecture quand´ $\mathfrak { X } _ { \varnothing }$admet une compactification X dont le bord est un diviseur à croisements normaux.

Si on reste sur une variet´ e ouverte´$\mathfrak { X } _ { \varnothing }$admettant une telle compactification X mais qu’on considère maintenant une correspondance Γ dans X qui ne stabilise pas l’ouvert$\mathfrak { X } _ { \varnothing }$, l’enonc´ e pr´ ec´ edent n’a même plus de sens´ car il$\boldsymbol { \mathrm { n ^ { \prime } y } }$a pas d’action induite sur la cohomologie de$\mathfrak { X } _ { \varnothing }$. Nous allons montrer toutefois que le nombre des points fixes dans$\mathfrak { X } _ { \varnothing }$de Γ (composee´ avec une puissance assez grande de Frob) s’interprète en fonction de l’action de Γ sur la cohomologie de X et de celle de correspondances induites sur la cohomologie des strates du bord. Pour la demonstration, on remarque que´ le principal argument geom´ etrique de Pink est local (il consiste à regarder´ comment des equations locales sont transform´ ees par les puissances de´ Frob) si bien$\mathrm { \ q u ^ { \mathrm { , } } i l }$reste valide si on suppose seulement que Γ stabilise$\mathfrak { X } _ { \varnothing }$ non plus globalement mais localement au voisinage de ses points fixes.

Dans un second temps, nous gen´ eralisons ce r´ esultat au cas où´ X lisse contient toujours$\mathfrak { X } _ { \varnothing }$comme ouvert dense et a pour bord${ \mathfrak { X } } - { \mathfrak { X } } _ { \varnothing }$un diviseur à croisements normaux mais n’est plus necessairement propre. Pour´ cela, on combine l’argument geom´ etrique tir´ e de [Pink] avec la conjec-´ ture de Deligne demontr´ ee par Fujiwara sans hypothèse de r´ esolution des´ singularites.´

Ceci s’appliquera aux champs de chtoucas. En effet, les ouverts $\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$où on sait calculer les nombres de points fixes ne sont pas stabilises globalement par les correspondances de Hecke mais on v´ erifiera´ qu’ils le sont “localement au voisinage des points fixes”. Et ils se plongent comme ouverts denses dans des$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } } } } / a ^ { \mathbb Z }$qui ne sont propres que si $N = \emptyset$mais sont lisses, ont pour bords des diviseurs à croisements normaux et sont stabilises par les correspondances de Hecke. (On sait aussi qu’ils´ admettent des compactifications lisses quand N n’a pas de multiplicites ou´ $r = 2 . )$

## 1) Eclatement et stabilite au voisinage des points fixes´

## a) La situation geom´ etrique´

Dans tout ce qui suit, on se place sur le corps de base$\mathbb { F } _ { q }$à q el´ ements.´

Nous appelons champ torique tout champ quotient$\mathcal { A } / \mathcal { A } _ { \mathcal { V } }$d’une variet´ e´ torique A par son tore$\mathcal { A } _ { \emptyset }$. Il est lisse si et seulement si la variet´ e torique´ A est lisse.

Dans une variet´ e torique il n’y a qu’un nombre fini d’orbites et leurs´ adherences sch´ ematiques sont des r´ eunions d’orbites donc dans un champ´ torique il$\boldsymbol { \mathrm { n ^ { \prime } y } }$a$\mathrm { \ q u } ^ { \prime }$un nombre fini de points et ils sont localement fermes.´

Pour tout schema ou tout champ alg´ ebrique´ X muni d’un morphisme vers un champ torique$\mathcal { A } / \mathcal { A } _ { \varnothing }$, on appelle strate ouverte [resp. fermee] de´ X les sous-schemas ou sous-champs localement ferm´ es [resp. ferm´ es] obtenus´ comme images reciproques des points [resp. des adh´ erences des points] du´ champ torique$\mathcal { A } / \mathcal { A } _ { \mathcal { V } }$

Considerons donc´ S un schema quasi-projectif et lisse sur´$\mathbb { F } _ { q }$et$\mathfrak { X }$un champ algebrique de type fini (mais pas n´ ecessairement propre) et lisse´ de dimension relative d sur le schema de base´ S. On fait les hypothèses suivantes :

• Le morphisme de structure$p : { \mathfrak { X } } \to S$se relève en un morphisme lisse

$$
\mathfrak {X} \to S \times \mathcal {A} / \mathcal {A} _ {\emptyset}
$$

pour$\mathcal { A } / \mathcal { A } _ { \mathcal { V } }$un champ torique lisse. Cela signifie que le bord de X (le complementaire´${ \mathfrak { X } } - { \mathfrak { X } } _ { \varnothing }$de l’ouvert$\mathfrak { X } _ { \varnothing }$image reciproque du point´ $\mathcal { A } _ { \emptyset } / \mathcal { A } _ { \emptyset } )$est un diviseur à croisements normaux relatif sur S sans autointersections des composantes.

• Le champ X est serein et compactifiable sur S au sens de l’appendice A (definition A.1).´

Cette dernière hypothèse implique que tout champ representable quasi-´ projectif sur X et en particulier toute strate ouverte ou fermee est aussi un´ champ serein compactifiable sur S.

On note$\mathfrak { X } _ { 1 } , \mathfrak { X } _ { 2 } , \ldots , \mathfrak { X } _ { m }$les strates ouvertes de X qui sont de codimension 1. Pour toute partie I de l’ensemble$\{ 1 , 2 , \dots , m \}$, on pose

$$
\begin{array}{l} \overline {{\mathfrak {X}}} _ {I} = \bigcap_ {i \in I} \overline {{\mathfrak {X}}} _ {i} \\ \text { et } \quad \mathfrak {X} _ {I} = \overline {{\mathfrak {X}}} _ {I} - \bigcup_ {J \supseteq I} \overline {{\mathfrak {X}}} _ {J}. \end{array}
$$

Celles des$\mathfrak { X } _ { I }$qui ne sont pas vides sont les strates ouvertes de$\mathfrak { X }$et les $\overline { { \mathfrak { X } } } _ { I }$sont les strates fermees, adh´ erences des´$\mathfrak { X } _ { I }$. Leur codimension est le cardinal |I| de I.

## b) Un eclatement´

On considère encore un endomorphisme$\varphi : S  S$du schema de base´ S. On note$Z = \mathfrak { X } \times _ { \varphi \circ p , S , p } \mathfrak { X } = \mathfrak { X } \times _ { \varphi , S } \mathfrak { X }$

Comme dans l’article [Pink], on introduit l’eclat´ e´$\widetilde { Z }$de Z le long du ferme r´ eunion des´$\overline { { \mathfrak { X } } } _ { i } \ \times _ { \varphi , S } \overline { { \mathfrak { X } } } _ { i }$. Si l’on prefère,´$\widetilde { Z }$est le produit fibre sur´ $Z$des eclat´ es´$\widetilde { Z } _ { i }$de Z le long des$\overline { { \mathfrak { X } } } _ { i } \times _ { \varphi , S } \overline { { \mathfrak { X } } } _ { i } , 1 \le i \le m$. On note$\pi$la projection$\widetilde { Z } \to Z :$; elle est representable, projective et birationnelle. On´ remarque que Z et$\widetilde { Z }$sont aussi des champs sereins, compactifiables et lisses sur S, de même dimension relative$2 d .$

Un modèle de l’eclatement´$\pi : \widetilde { Z } \to Z$est fourni par le lemme suivant :

Lemme IV.1. – Localementpour la topologie lisse, le champ$Z = { \mathfrak { X } } \times _ { \varphi , S } { \mathfrak { X } }$ muni de lafamille depaires de diviseurs$\overline { { \mathfrak { X } } } _ { i } \times _ { \varphi , S } \mathfrak { X }$et$\mathfrak { X } \times _ { \varphi , S } \overline { { \mathfrak { X } } } _ { i } , 1 \le i \le m$, et du morphisme representableprojectifbirationnel´$\pi : \widetilde { Z } \to Z$est isomorphe auproduit d’un certain nombre defacteurs$\mathbb { A } ^ { 1 } \times \mathbb { A } ^ { 1 }$munis des deux diviseurs $\{ 0 \} \times \mathbb { A } ^ { 1 }$et$\mathbb { A } ^ { 1 } \times \{ 0 \}$et de l’eclat´ e´$\mathbb { A } ^ { 1 } \times \mathbb { A } ^ { 1 }$de$\mathbb { A } ^ { 1 } \times \mathbb { A } ^ { 1 }$le long du point (0, 0).

Demonstration :´ Le champ Z est muni d’un morphisme lisse

$$
Z \to \mathcal {A} / \mathcal {A} _ {\emptyset} \times \mathcal {A} / \mathcal {A} _ {\emptyset} = (\mathcal {A} \times \mathcal {A}) / (\mathcal {A} _ {\emptyset} \times \mathcal {A} _ {\emptyset})
$$

et ses diviseurs sont les images reciproques de ceux de´$( \mathcal { A } \times \mathcal { A } ) / ( \mathcal { A } _ { \emptyset } \times \mathcal { A } _ { \emptyset } )$ Et comme la variet´ e torique´ A est lisse,${ \mathrm { c } } '$est une reunion d’ouverts qui sont´ des espaces affines$\mathbb { A } ^ { 1 } \times \dot { \ } \cdot \cdot \cdot \times \mathbb { A } ^ { 1 }$munis de leurs diviseurs naturels definis´ par l’annulation des differentes coordonn´ ees.´!"

L’eclat´ e´$\widetilde { Z }$est muni de diviseurs à croisements normaux$E _ { i } , 1 \le i \le m$ qui sont les images reciproques des diviseurs exceptionnels dans les´ eclat´ es´$\widetilde { Z } _ { i }$

Pour toute partie non vide I de$\{ 1 , \ldots , m \}$, on a$\bigcap { \overline { { \mathfrak { X } } } } _ { i } \times _ { \varphi , S } { \overline { { \mathfrak { X } } } } _ { i } =$ i∈I

$\overline { { \mathfrak { X } } } _ { I } \times _ { \varphi , S } \overline { { \mathfrak { X } } } _ { I }$et$E _ { I } = \bigcap _ { i \in I } E _ { i }$est contenu dans$\pi ^ { - 1 } ( \overline { { \mathfrak { X } } } _ { I } \times _ { \varphi , S } \overline { { \mathfrak { X } } } _ { I } )$. D’après le

lemme IV.1,$E _ { I }$est le produit fibre sur´ Z des diviseurs exceptionnels des $\widetilde { Z } _ { i }$tels que$i \in I$avec les$\widetilde { Z } _ { i }$tels que$i \notin I$et sa restriction au-dessus de l’ouvert$\mathfrak { X } _ { I } \times _ { \varphi , S } \mathfrak { X } _ { I }$de$\overline { { \mathfrak { X } } } _ { I } \times _ { \varphi , S } \overline { { \mathfrak { X } } } _ { I }$est un fibre projectif de rang´ |I|.

## c) Graphes des morphismes de Frobenius

Soit$s = \mathrm { S p e c } \kappa _ { s }$le spectre d’un corps$\kappa _ { s }$extension finie du corps de base $\mathbb { F } _ { q }$et$x : s \hookrightarrow S$un point ferme du sch´ ema de base´ S de corps residuel´$\kappa _ { s }$

Posant$y = \varphi \circ x$, on note$\mathfrak { X } ^ { x }$et$\mathfrak { X } ^ { y }$les fibres${ \mathfrak { X } } \times _ { S , x } s$et$\boldsymbol { \mathfrak { X } } \times _ { S , y }$s de X au-dessus de x et y. Ce sont des champs sereins, propres et lisses de dimension d sur s dont les strates ouvertes sont les$\mathfrak { X } _ { I } ^ { x } = \mathfrak { X } _ { I } \times _ { S , x } s$et les $\mathfrak { X } _ { I } ^ { y } = \mathfrak { X } _ { I } \times _ { S , x } s .$

Le produit$\mathfrak { X } ^ { x } \times _ { s } \mathfrak { X } ^ { y }$s’identifie à la fibre$Z ^ { x } = Z \times _ { S , x } s$de Z au-dessus de x et son eclat´ e le long des´$\overline { { \mathfrak { X } } } _ { i } ^ { x } \times _ { s } \overline { { \mathfrak { X } } } _ { i } ^ { y } , 1 \le i \le m , \mathrm { s } ^ { \mathrm { { \scriptscriptstyle T } } }$identifie à$\widetilde { Z } ^ { x } = \widetilde { Z } \times _ { S , x } s .$  Cet eclat´ e est donc muni de la famille de diviseurs à croisements norma´ ux $E _ { i } ^ { x } = E _ { i } \times _ { S , x } s , 1 \le i \le m$, dont les intersections mutuelles sont les $\bigcap E _ { i } ^ { x } = E _ { I } ^ { x } = E _ { I } \times _ { S , x } s .$ i∈I

L’ensemble des entiers$n \in \mathbb { N }$tels que les morphismes$y \circ \operatorname { F r o b } ^ { n } =$ Frob<sup>n</sup> ◦ y et$x : s \hookrightarrow S$se confondent est, s’il n’est pas vide, une classe de congruence modulo deg$\mathbf { \sigma } ( s ) = [ \boldsymbol { \kappa } _ { s } : \mathbb { F } _ { q } ]$. Soit n un entier dans cette classe.

Le carre commutatif´

$$
\begin{array}{c c c} \mathfrak {X} & \xrightarrow {\text {(Frob} ^ {n} , \mathrm{Id})} & \mathfrak {X} \times \mathfrak {X} \\ \Big \downarrow & & \Big \downarrow \\ S & \xrightarrow {\text {(Frob} ^ {n} , \mathrm{Id})} & S \times S \end{array}
$$

induit un morphisme

$$
\mathfrak {X} \rightarrow S \times_ {\left(\operatorname{Frob} ^ {n}, \operatorname{Id}\right), S \times S} \mathfrak {X} \times \mathfrak {X}
$$

dont la fibre au-dessus de$y : s  S \mathrm {  ~ s ~ } ^ { \prime }$ecrit´

$$
\mathfrak {X} ^ {y} \rightarrow s \times_ {\left(\operatorname{Frob} ^ {n} \circ y, y\right), S \times S} \mathfrak {X} \times \mathfrak {X}
$$

c’est-à-dire, puisque Frob${ } ^ { n } \circ y = x$par hypothèse,

$$
\mathfrak {X} ^ {y} \rightarrow \mathfrak {X} ^ {x} \times_ {s} \mathfrak {X} ^ {y} = Z ^ {x}.
$$

On notera$\delta ^ { n }$ce morphisme. C’est une section de${ \mathfrak { X } } ^ { x } \times _ { s } { \mathfrak { X } } ^ { y } \to { \mathfrak { X } } ^ { y }$donc il est representable fini.´

Via$\delta ^ { n }$, les fermes´$\overline { { \mathfrak { X } } } _ { i } ^ { x } \times _ { s } \overline { { \mathfrak { X } } } _ { i } ^ { y } , 1 \le i \le m$, de$\mathfrak { X } ^ { s } \times _ { s } \mathfrak { X } ^ { y }$ont pour images reciproques les diviseurs´$\overline { { \mathfrak { X } } } _ { i } ^ { y }$donc le morphisme$\delta ^ { n } : \mathfrak { X } ^ { y } \to Z ^ { x }$se relève dans l’eclat´ e´$\widetilde { Z } ^ { x }$en un morphisme

$$
\widetilde {\delta} ^ {n}: \mathfrak {X} ^ {y} \to \widetilde {Z} ^ {x}
$$

qui lui aussi est representable fini.´

De même, pour I une partie non vide de$\{ 1 , \ldots , m \}$, on dispose de la restriction

$$
\delta_ {I} ^ {n}: \overline {{\mathfrak {X}}} _ {I} ^ {y} \to \overline {{\mathfrak {X}}} _ {I} ^ {x} \times_ {s} \overline {{\mathfrak {X}}} _ {I} ^ {y}
$$

du morphisme$\delta ^ { n } : \mathfrak { X } ^ { y } \to \mathfrak { X } ^ { x } \times \mathfrak { X } ^ { y } \overset { } { \underset { } { \mathrm { \mathfrak { a } } } } \overline { \mathfrak { X } } _ { I } ^ { y }$; c’est une section de$\overline { { \mathfrak { X } } } _ { I } ^ { x } \times _ { s } \overline { { \mathfrak { X } } } _ { I } ^ { y } \to \overline { { \mathfrak { X } } } _ { I } ^ { y }$ et elle est representable finie.´

Pour tout$i \in \{ 1 , \ldots , m \} - I$, l’image reciproque via´

$$
\delta_ {I} ^ {n}: \overline {{\mathfrak {X}}} _ {I} ^ {y} \rightarrow \overline {{\mathfrak {X}}} _ {I} ^ {x} \times_ {s} \overline {{\mathfrak {X}}} _ {I} ^ {y} \hookrightarrow Z ^ {x}
$$

de$\overline { { \mathfrak { X } } } _ { i } ^ { x } \times _ { s } \overline { { \mathfrak { X } } } _ { i } ^ { y }$est le diviseur$\overline { { \mathfrak { X } } } _ { I \cup \{ i \} } ^ { y }$donc$\delta _ { I } ^ { n }$se relève en un morphisme de$\overline { { \mathfrak { X } } } _ { I } ^ { y }$ dans le produit fibre sur´$Z ^ { x }$des$\widetilde { Z } _ { i } ^ { x } , i \in \{ 1 , \ldots , m \} - I$

Son image reciproque dans´$\widetilde { Z } ^ { { \boldsymbol { x } } }$(qui est le produit fibre sur´$Z ^ { x }$de tous les $\widetilde { Z } _ { i } ^ { x } , i \in \{ 1 , \ldots , m \} )$est un morphisme representable fini´

$$
\widetilde {\delta} _ {I} ^ {n}: \widetilde {\mathfrak {X}} _ {I} ^ {y} \to \widetilde {Z} ^ {x}
$$

où$\widetilde { \mathfrak { X } } _ { I } ^ { y }$est une fibration projective sur$\overline { { \mathfrak { X } } } _ { I } ^ { y }$isomorphe à$\overline { { \mathcal { X } } } _ { I } ^ { y } \times ( \mathbb { P } ^ { 1 } ) ^ { | I | }$(et dont la restriction au-dessus de$\boldsymbol { \mathfrak { X } } _ { I } ^ { y }$s’identifie à l’image reciproque de´$E _ { I } ^ { x }$via $\delta _ { I } ^ { n } : \overline { { \mathfrak { X } } } _ { I } ^ { y } \to \overline { { \mathfrak { X } } } _ { I } ^ { x } \times _ { s } \overline { { \mathfrak { X } } } _ { I } ^ { y } )$

On a :

Lemme IV.2. – Avec ces notations, le produitfibre´$\mathfrak { X } ^ { y } \times _ { \delta ^ { n } , Z ^ { x } } \widetilde Z ^ { x }$au-dessus $d e \widetilde { Z } ^ { x }$est la reunion sch´ ematique de´${ \mathfrak { X } } ^ { y } { \xrightarrow { { \widetilde { \delta } } ^ { n } } } { \widetilde { Z } } ^ { x }$et des$\widetilde { \mathfrak { X } } _ { J } ^ { y }$lesquels sont tous   lisses de même dimension et ont des intersections mutuelles de dimensions plus petites.

Etpour I unepartie non vide de$\{ 1 , \ldots , m \}$, leproduitfibre´$\overline { { \mathcal { X } } } _ { I } ^ { y } \times _ { \delta _ { I } ^ { n } , Z ^ { x } } \widetilde Z ^ { x }$ $\mathbf { \Phi } = { \mathfrak { X } } ^ { y } \times \delta ^ { n } , Z ^ { x } \ E _ { I }$est la reunion sch´ ematique des´$\widetilde { \mathfrak { X } } _ { J } ^ { y } , J \supseteq I .$

Demonstration :´ Cela resulte du lemme IV.1 puisque dans l’´ eclat´ e´$\mathbb { A } ^ { 1 } \times \mathbb { A } ^ { 1 }$ d’un$\mathbb { A } ^ { 1 } \times \mathbb { A } ^ { 1 }$le long de$\{ 0 \} \times \{ 0 \}$, l’image reciproque du graphe de´$\mathrm { F r o b } ^ { n }$ $\mathbb { A } ^ { 1 } \to \mathbb { A } ^ { 1 }$a deux composantes : le transforme strict de ce graphe et le´ diviseur exceptionnel.!"

## d) Correspondances et stabilite au voisinage des points fixes´

Nous allons maintenant introduire une correspondance dans$\mathfrak { X }$au-dessus de l’endomorphisme$\varphi$de$\begin{array} { r } { S \mathrm { \ c ^ { \prime } e s t { - } \hat { a } - d i r e } } \end{array}$un cycle de codimension d dans ${ \mathfrak { X } } \times _ { \varphi , S } { \mathfrak { X } } = { \bar { Z } }$et son transforme strict dans l’´ eclat´ e´$\widetilde { Z }$de$Z$qui va nous permettre de definir des correspondances (cohomologiques) induites dans´ les strates de bord$\overline { { \mathfrak { X } } } _ { I }$de$\mathfrak { X }$.

On part$\mathrm { d } ^ { \prime }$un champ normal$\Gamma _ { \emptyset }$representable fini sur l’ouvert ´$\mathfrak { X } _ { \varnothing } \times _ { \varphi , S } \mathfrak { X } _ { \varnothing }$ et dont le support de l’image$| \Gamma _ { \emptyset } |$est de codimension$d .$

Par normalisation, il induit deux champs normaux$\Gamma$et$\widetilde \Gamma$representables´ finis sur$Z = { \mathfrak { X } } \times _ { \varphi , S } { \mathfrak { X } }$et$\widetilde { Z }$et qui contiennent$\Gamma _ { \emptyset }$comme ouvert dense. Ils sont relies par un morphisme repr´ esentable projectif birationnel´$\widetilde \Gamma \to \Gamma$qui fait commuter le diagramme :

![](images/page_90_image_14.jpg)

On note$p _ { \Gamma } ^ { \prime } , ~ p _ { \Gamma } ^ { \prime \prime }$et$p _ { \widetilde { \Gamma } } ^ { \prime } , ~ p _ { \widetilde { \Gamma } } ^ { \prime \prime }$les deux projections de Γ et$\widetilde \Gamma$sur${ \mathfrak { X } } .$On   dit que Γ (ou Γ) definit une correspondance g´ eom´ etrique dans´ X au-dessus de l’endomorphisme$\varphi$de S si la seconde projection$p _ { \Gamma } ^ { \prime \prime } : \Gamma \to \mathfrak { X }$(ou $p _ { \widetilde { \Gamma } } ^ { \prime \prime } : \widetilde { \Gamma }  \mathfrak { X } )$est propre. (Cette condition est automatiquement verifi´ ee si´  X est propre sur S.)

Bien sûr, on dit qu’une telle correspondance Γ stabilise (à droite) l’ouvert $\mathfrak { X } _ { \varnothing }$quand on a l’inclusion$p _ { \Gamma } ^ { \prime \prime - 1 } ( \mathfrak { X } _ { \varnothing } ) \overset { \cdot } { \subseteq } p _ { \Gamma } ^ { \prime - 1 } ( \mathfrak { X } _ { \varnothing } )$

Posons la definition suivante :´

Definition IV.3.´ – Soit Γ une correspondance dans X au-dessus de$\varphi .$

On dira que Γ stabilise$\mathfrak { X } _ { \varnothing }$au voisinage de ses pointsfixes$s { \ ' } i l$existe un ouvert U dans${ \mathfrak { X } } \times { \mathfrak { X } } .$, contenant toutes les intersections du support |Γ| de $\Gamma$avec les images des morphismes${ \mathfrak { X } } { \xrightarrow { \ ( \operatorname { F r o b } ^ { n } , \operatorname { I d } ) } } { \mathfrak { X } } \times { \mathfrak { X } } , n \in \mathbb { N }$, et tel que

$$
p _ {\Gamma} ^ {\prime \prime - 1} (\mathfrak {X} _ {\emptyset}) \cap U \subseteq p _ {\Gamma} ^ {\prime - 1} (\mathfrak {X} _ {\emptyset}) \cap U.
$$

Pour verifier qu’une correspondance´ Γ stabilise$\mathfrak { X } _ { \varnothing }$au voisinage de ses points fixes, on dispose du critère valuatif suivant :

Lemme IV.4. – Pour qu’une correspondance Γ dans X au-dessus de ϕ stabilise$\mathfrak { X } _ { \varnothing }$au voisinage de ses points fixes, il suffit qu’elle satisfasse la condition suivante :

(SV) Pour tout point α de Γ à valeurs dans un anneau de valuation discrète et dont la gen´ erisation est support´ ee par´${ p _ { \Gamma } ^ { \prime } } ^ { - 1 } ( \mathfrak { X } - \mathfrak { X } _ { \varnothing } ) \cap p _ { \Gamma } ^ { \prime \prime } { } ^ { - 1 } ( \mathfrak { X } _ { \varnothing } )$, la specialisation de´ α n’est supportee par l’image d’aucun des morphismes´ ${ \mathfrak { X } } { \xrightarrow { ( \operatorname { F r o b } ^ { n } , \operatorname { I d } ) } } { \mathfrak { X } } \times { \mathfrak { X } } , n \in \mathbb { N } .$

Demonstration :´ Dans le support de Γ qui est un ferme de´$\mathfrak { X } \times _ { \varphi , S } \mathfrak { X }$et donc de${ \mathfrak { X } } \times { \mathfrak { X } }$, l’intersection$p _ { \Gamma } ^ { \prime \top } ( \mathfrak { X } - \mathfrak { X } _ { \varnothing } ) \cap p _ { \Gamma } ^ { \prime \prime - 1 } ( \mathfrak { X } _ { \varnothing } )$est un sous-ensemble constructible. Pour que l’ouvert U complementaire de son adh´ erence dans´ ${ \mathfrak { X } } \times { \mathfrak { X } }$contienne l’intersection de |Γ| avec les images de tous les morphismes ${ \mathfrak { X } } { \xrightarrow { \ { \mathrm { ( F r o b } } ^ { n } , { \mathrm { I d } } { \mathrm { ) } } } } { \mathfrak { X } } \times { \mathfrak { X } }$, il suffit par consequent que soit v´ erifi´ ee la condition´ (SV).!"

## e) L’argument geom´ etrique de Pink´

Pour toute correspondance Γ dans X au-dessus de$\varphi ,$on note$\Gamma _ { \emptyset }$sa restriction au-dessus de l’ouvert${ \mathfrak { X } } _ { \varnothing } \times _ { \varphi , S } { \mathfrak { X } } _ { \varnothing }$de${ \mathfrak { X } } \times _ { \varphi , S } { \mathfrak { X } } = Z$. On dit que$\Gamma$est engendree par´$\Gamma _ { \emptyset }$si cet ouvert$\Gamma _ { \emptyset }$est dense dans Γ. La normalisation$\widetilde \Gamma$de $\Gamma _ { \emptyset }$au-dessus de l’eclat´ e´$\widetilde { Z }$est alors appelee le transform´ e strict de´ Γ dans$\widetilde { Z } .$

On a le resultat suivant qui g ´ en´ eralise la proposition 7.3.1 de [Pink] :´

Proposition IV.5. – Soit Γ une correspondance dans$\mathfrak { X }$au-dessus de ϕ qui est engendree par´$\Gamma _ { \emptyset }$et qui stabilise$\dot { \mathfrak { X } } _ { \varnothing }$au voisinage de ses points fixes.

Alors, quitte à remplacer ϕ par$\varphi \circ { \mathrm { F r o b } } ^ { n _ { 0 } } = { \mathrm { F r o b } } ^ { n _ { 0 } } \circ \varphi$et Γ par la normalisation$\Gamma ^ { ( n _ { 0 } ) }$de$( { \mathfrak { X } } \times { \mathfrak { X } } ) \times _ { ( \mathrm { F r o b } ^ { n _ { 0 } } , \mathrm { I d } ) , { \mathfrak { X } } \times { \mathfrak { X } } } \Gamma$pour$n _ { 0 } \geq 0$un entier assez grand, le transforme strict´$\widetilde \Gamma$de Γ dans$\tilde { Z }$v erifie :´

Pour tout pointferme´$x : s \hookrightarrow S$avec$y _ { \sim } = \varphi \circ x$et tout entier n ≥ 1 tel que$y \circ \mathrm { F r o b } ^ { n } = \mathrm { F r o b } ^ { n } \circ y = x , l ^ { \prime }$image de$\widetilde { \delta } ^ { n } : \mathcal { X } ^ { y }  \widetilde { Z } ^ { x } = \widetilde { Z } \times _ { S , x } s \hookrightarrow \widetilde { Z }$ ne rencontre pas le support de$\widetilde \Gamma$en dehors de${ \mathfrak { X } } _ { \varnothing } \times { \mathfrak { X } } _ { \varnothing }$

Demonstration :´ Soit U un ouvert de${ \mathfrak { X } } \times { \mathfrak { X } }$qui verifie la propri´ et´ e de la´ definition IV.3 relativement à´ Γ. Les images des$\widetilde { \delta } ^ { n }$et le support de$\widetilde \Gamma$ne peuvent se rencontrer ailleurs qu’au-dessus de$U$.

Localement sur${ \mathfrak { X } } .$considerons des´ equations´$\ell _ { 1 } , \ell _ { 2 } , \dots , \ell _ { m }$de definition´ des diviseurs$\mathfrak { X } _ { 1 } , \ldots , \mathfrak { X } _ { m }$et$\ell = \ell _ { 1 } \ell _ { 2 } \cdot \cdot \cdot \ell _ { m }$leur produit. Notons$\ell _ { 1 } ^ { \prime } , \ell _ { 2 } ^ { \prime }$ $\cdots , \ell _ { m } ^ { \prime }$et 	 d’une part,$\ell _ { 1 } ^ { \prime \prime } , \ell _ { 2 } ^ { \prime \prime } , \ldots , \ell _ { m } ^ { \prime \prime }$et$\ell ^ { \prime \prime }$d’autre part leurs images reciproques par les deux projections´${ \mathfrak { X } } \times { \mathfrak { X } } { \longrightarrow } { \mathfrak { X } }$

Comme$p _ { \Gamma } ^ { \prime \prime } { } ^ { - 1 } ( \mathfrak { X } _ { \varnothing } ) \cap U \subseteq p _ { \Gamma } ^ { \prime } { } ^ { - 1 } ( \mathfrak { X } _ { \varnothing } ) \cap U$ou encore$p _ { \Gamma } ^ { \prime } { } ^ { - 1 } ( \mathfrak { X } - \mathfrak { X } _ { \varnothing } ) \cap U \subseteq$ $p _ { \Gamma } ^ { \prime \prime } { } ^ { - 1 } ( \mathfrak { X } - \mathfrak { X } _ { \varnothing } ) \cap U$, il existe un entier$e \geq 1$et une fonction a partout definie´ sur$\Gamma \cap U$tels que sur$\Gamma \cap U$l’equation suivante soit v´ erifi´ ee´

$$
\ell^ {\prime \prime e} = a \ell^ {\prime}.
$$

Choisissant un entier$n _ { 0 } \geq 0$tel que$q ^ { n _ { 0 } } \geq e$et remplaçant Γ et U ainsi que la fonction a par leurs images reciproques via´$\mathfrak { X } \times \mathfrak { X } \xrightarrow { \ ( \mathrm { F r o b } ^ { n _ { 0 } } , \mathrm { I d } ) } \mathfrak { X } \times \mathfrak { X }$ cette equation devient´

$$
\ell^ {\prime \prime e} = a \ell^ {\prime q ^ {n _ {0}}}
$$

ce qu’on recrit´

$$
(\ell^ {\prime \prime} / \ell^ {\prime}) ^ {e} = a \ell^ {\prime q ^ {n _ {0}} - e}.
$$

Mais par ailleurs, pour tout point ferme´$x : s \hookrightarrow S$avec$y = \varphi \circ x$et tout entier$n \geq 1$tel que y ◦ Fro$\bar { \boldsymbol { \jmath } ^ { n } } = \mathrm { F r o b } ^ { n } \circ \boldsymbol { y } = \boldsymbol { x }$, on voit que sur l’image du transforme strict´${ \tilde { \mathfrak { J } } } ^ { n } : { \mathfrak { X } } ^ { y } \to { \widetilde { Z } } ^ { x } \hookrightarrow { \widetilde { Z } }$sont satisfaites les equations´

$$
\ell_ {1} ^ {\prime} = \ell_ {1} ^ {\prime \prime q ^ {n}}, \ell_ {2} ^ {\prime} = \ell_ {2} ^ {\prime \prime q ^ {n}}, \ldots , \ell_ {m} ^ {\prime} = \ell_ {m} ^ {\prime \prime q ^ {n}}
$$

qu’on recrit´

$$
\ell_ {1} ^ {\prime} / \ell_ {1} ^ {\prime \prime} = \ell_ {1} ^ {\prime \prime q ^ {n - 1}}, \ldots , \ell_ {m} ^ {\prime} / \ell_ {m} ^ {\prime \prime} = \ell_ {m} ^ {\prime \prime q ^ {n - 1}}.
$$

Cela montre que l’image de$\widetilde { \delta } ^ { n }$ne rencontre pas le support de$\widetilde { Z }$en dehors de$\mathfrak { X } _ { \varnothing } \times \mathfrak { X } _ { \varnothing }$!"

## 2) Formule des points fixes de Grothendieck-Lefschetz dans le cas propre

Dans tout le present paragraphe 2, on fait l’hypothèse suppl´ ementaire que´ X est propre sur S.

## a) Formule d’adjonction

Comme X est propre sur$S ,$il en est de même de$Z \times _ { \varphi , S } { \mathfrak { X } }$et de son eclat´ e´$\widetilde { Z } .$

On considère une correspondance$\Gamma$dans$\mathfrak { X }$au-dessus de$\varphi$qui est engendree par sa trace´$\Gamma _ { \emptyset }$au-dessus de l’ouvert${ \mathfrak { X } } _ { \varnothing } \times _ { \varphi , S } { \mathfrak { X } } _ { \varnothing }$de$Z .$. On note toujours$\widetilde \Gamma$le transforme strict de´$\Gamma$dans$\widetilde { Z } .$

Le paragraphe$2 \mathrm { a }$de l’appendice A nous permet alors de definir les´ classes de cohomologie de$\Gamma$et$\widetilde \Gamma$,

$$
\operatorname{cl} (\Gamma) \quad \text { et } \quad \operatorname{cl} (\widetilde {\Gamma}),
$$

comme sections sur S des faisceaux -adiques lisses

$$
R ^ {2 d} (p _ {Z}) _ {*} \mathbb {Q} _ {\ell} (d) \quad \text { et } \quad R ^ {2 d} (p _ {\widetilde {Z}}) _ {*} \mathbb {Q} _ {\ell} (d)
$$

où$p _ { Z }$et$p _ { \widetilde Z }$designent les morphismes de structure de´$Z$et$\widetilde { Z }$sur$S .$.

Puis, pour toute partie$I \neq \emptyset$de$\{ 1 , \ldots , m \}$telle que$\mathfrak { X } _ { I }$ne soit pas vide, on note cl$( \widetilde { \Gamma } ) _ { I }$l’image de la section cl$( \widetilde { \Gamma } )$par l’homomorphisme compose´

$$
R ^ {2 d} (p _ {\widetilde {Z}}) _ {*} \mathbb {Q} _ {\ell} (d) \to R ^ {2 d} (p _ {E _ {I}}) _ {*} \mathbb {Q} _ {\ell} (d) \to R ^ {2 (d - | I |)} (p _ {\overline {{\mathfrak {X}}} _ {I \times_ {\varphi , S}} \overline {{\mathfrak {X}}} _ {I})} _ {*} \mathbb {Q} _ {\ell} (d - | I |)
$$

où la première flèche provient de l’inclusion$E _ { I } \hookrightarrow \widetilde { Z }$et la seconde est duale (pour la dualite de Poincar´ e) de la flèche´

$$
R ^ {2 (d - | I |)} \left(p _ {\overline {{\mathfrak {X}}} _ {I} \times_ {\varphi , S} \overline {{\mathfrak {X}}} _ {I}}\right) _ {*} \mathbb {Q} _ {\ell} (d - | I |) \rightarrow R ^ {2 (d - | I |)} \left(p _ {E _ {I}}\right) _ {*} \mathbb {Q} _ {\ell} (d - | I |)
$$

induite par le morphisme$E _ { I } \to \overline { { \mathfrak { X } } } _ { I } \times _ { \varphi , S } \overline { { \mathfrak { X } } } _ { I }$

Soient$x : s \hookrightarrow S$un point ferme de´$S , y = \varphi \circ x \operatorname* { e t } n \in \mathbb { N }$un entier tel que$y \circ \mathrm { F r o b } ^ { n } = \mathrm { F r o b } ^ { n } \circ y = x$. On a introduit au paragraphe 1c ci-dessus les morphismes representables finis´

$$
\delta^ {n}: \mathfrak {X} ^ {y} \longrightarrow \mathfrak {X} ^ {x} \times_ {s} \mathfrak {X} ^ {y} = Z ^ {x},
$$

$$
\widetilde {\delta} ^ {n}: \mathfrak {X} ^ {y} \longrightarrow \widetilde {Z} ^ {x},
$$

$$
\delta_ {I} ^ {n}: \overline {{\mathfrak {X}}} _ {I} ^ {y} \longrightarrow \overline {{\mathfrak {X}}} _ {I} ^ {x} \times_ {s} \overline {{\mathfrak {X}}} _ {I} ^ {y}
$$

auxquels on peut associer des classes de cohomologie

$$
\operatorname{cl} \left(\delta^ {n}\right) \in H ^ {2 d} \left(Z ^ {x}, \mathbb {Q} _ {\ell} (d)\right),
$$

$$
\operatorname{cl} \left(\widetilde {\delta} ^ {n}\right) \in H ^ {2 d} \left(\widetilde {Z} ^ {x}, \mathbb {Q} _ {\ell} (d)\right),
$$

$$
\operatorname{cl} \left(\delta_ {I} ^ {n}\right) \in H ^ {2 (d - | I |)} \left(\overline {{\mathfrak {X}}} _ {I} ^ {x} \times_ {s} \overline {{\mathfrak {X}}} _ {I} ^ {y}, \mathbb {Q} _ {\ell} (d - | I |)\right).
$$

$\mathbf { D } '$autre part, on dispose des fibres

$$
x ^ {*} (\operatorname{cl} (\Gamma)) \in H ^ {2 d} \left(Z ^ {x}, \mathbb {Q} _ {\ell} (d)\right),
$$

$$
x ^ {*} (\operatorname{cl} (\widetilde {\Gamma})) \in H ^ {2 d} \bigl (\widetilde {Z} ^ {x}, \mathbb {Q} _ {\ell} (d) \bigr),
$$

$$
x ^ {*} (\operatorname{cl} (\widetilde {\Gamma}) _ {I}) \in H ^ {2 (d - | I |)} \left(\overline {{\mathfrak {X}}} _ {I} ^ {x} \times_ {s} \overline {{\mathfrak {X}}} _ {I} ^ {y}, \mathbb {Q} _ {\ell} (d - | I |)\right)
$$

des sections cl(Γ), cl$( \widetilde { \Gamma } )$et$\mathrm { c l } ( \widetilde { \Gamma } ) _ { I }$des faisceaux$R ^ { 2 d } ( p _ { Z } ) _ { * } \mathbb { Q } _ { \ell } ( d )$

$R ^ { 2 d } ( p _ { \widetilde { Z } } ) _ { * } \mathbb { Q } _ { \ell } ( d ) \operatorname { e t } R ^ { 2 ( d - | I | ) } { ( p _ { \overline { { \mathfrak { X } } } _ { I } ^ { x } \times _ { s } \overline { { \mathfrak { X } } } _ { I } ^ { y } } ) _ { * } \mathbb { Q } _ { \ell } ( d - | I | ) }$puisque, d’après le corol- laire A.4, la formation de ces faisceaux commute aux changements de la base S.

En combinant le produit “cup” et les homomorphismes de traces, on peut former les produits scalaires des unes et des autres. Ils sont relies par´ la formule suivante :

Proposition IV.6. – Etant donnes´$x : s \hookrightarrow S$unpointferme de S,´$y = f$◦x et$n \in \mathbb { N }$un entier tel que$y \circ \mathrm { F r o b } ^ { n } = \mathrm { F r o b } ^ { n } \circ y = x$, on a la relation entre produits scalaires

$$
\begin{array}{l} \operatorname{cl} (\widetilde {\delta} ^ {n}) \cdot x ^ {*} (\operatorname{cl} (\widetilde {\Gamma})) = \operatorname{cl} (\delta^ {n}) \cdot x ^ {*} (\operatorname{cl} (\Gamma)) \\ \qquad + \sum_ {I \neq \emptyset} (- 1) ^ {| I |} \operatorname{cl} \left(\delta_ {I} ^ {n}\right) \cdot x ^ {*} (\operatorname{cl} (\widetilde {\Gamma}) _ {I}). \end{array}
$$

Demonstration :´ Le morphisme representable projectif´$\widetilde \Gamma  \Gamma$est compatible avec$\pi : \widetilde { Z } \to Z$et il est birationnel. D’après la proposition A.11, on en deduit que cl´ (Γ) est l’image de cl(Γ) par l’homomorphisme

$$
R ^ {2 d} (p _ {\widetilde {Z}}) _ {*} \mathbb {Q} _ {\ell} (d) \xrightarrow {\pi_ {*}} R ^ {2 d} (p _ {Z}) _ {*} \mathbb {Q} _ {\ell} (d)
$$

dual de

$$
R ^ {2 d} (p _ {Z}) _ {*} \mathbb {Q} _ {\ell} (d) \xrightarrow {\pi^ {*}} R ^ {2 d} (p _ {\widetilde {Z}}) _ {*} \mathbb {Q} _ {\ell} (d).
$$

Posant$u = x ^ { * } ( \mathrm { c l } ( \widetilde { \Gamma } ) )$, on a aussi par compatibilite aux changements de´ la base S

$$
x ^ {*} (\operatorname{cl} (\Gamma)) = \pi_ {*} (u).
$$

Et pour toute$I , x ^ { * } ( \mathrm { c l } ( \widetilde { \Gamma } ) _ { I } )$est image de u par l’homomorphisme compose´

$$
H ^ {2 d} \left(\widetilde {Z} ^ {x}, \mathbb {Q} _ {\ell} (d)\right)\rightarrow H ^ {2 d} \left(E _ {I} ^ {x}, \mathbb {Q} _ {\ell} (d)\right)\rightarrow H ^ {2 (d - | I |)} \left(\overline {{\mathfrak {X}}} _ {I} ^ {x} \times_ {s} \overline {{\mathfrak {X}}} _ {I} ^ {y}, \mathbb {Q} _ {\ell} (d - | I |)\right)
$$

où la première flèche provient de l’inclusion$\iota _ { E _ { I } ^ { x } } : E _ { I } ^ { x } \hookrightarrow \widetilde { Z } ^ { x }$et la seconde est duale de la flèche

$$
H ^ {2 (d - | I |)} \left(\overline {{\mathfrak {X}}} _ {I} ^ {x} \times_ {s} \overline {{\mathfrak {X}}} _ {I} ^ {y}, \mathbb {Q} _ {\ell} (d - | I |)\right)\rightarrow H ^ {2 (d - | I |)} \left(E _ {I} ^ {x}, \mathbb {Q} _ {\ell} (d - | I |)\right)
$$

induite par le morphisme$\pi _ { I } : E _ { I } ^ { x } \to \overline { { { \mathfrak { X } } } } _ { I } ^ { x } \times _ { s } \overline { { { \mathfrak { X } } } } _ { I } ^ { y }$. On note$x ^ { * } ( \mathrm { c l } ( \widetilde { \Gamma } ) _ { I } ) =$ $\pi _ { I * } \iota _ { E _ { I } ^ { x } } ^ { * } ( u )$

Ainsi la formule à demontrer se r´ ecrit-elle´

$$
\operatorname{cl} \left(\widetilde {\delta} ^ {n}\right) \cdot u = \operatorname{cl} \left(\delta^ {n}\right) \cdot \pi_ {*} (u) + \sum_ {I \neq \emptyset} (- 1) ^ {| I |} \operatorname{cl} \left(\delta_ {I} ^ {n}\right) \cdot \pi_ {I *} \iota_ {E _ {I} ^ {x}} ^ {*} (u)
$$

soit

$$
\operatorname{cl} \left(\widetilde {\delta} ^ {n}\right) \cdot u = \pi^ {*} \left(\operatorname{cl} \left(\delta^ {n}\right)\right) \cdot u + \sum_ {I \neq \emptyset} (- 1) ^ {| I |} \pi_ {I} ^ {*} \left(\operatorname{cl} \left(\delta_ {I} ^ {n}\right)\right) \cdot \iota_ {E _ {I} ^ {x}} ^ {*} (u).
$$

Or, d’après la proposition A.11,$\pi ^ { * } ( \mathrm { c l } ( \delta ^ { n } ) )$est aussi la classe de cohomologie du produit fibre´$\mathfrak { X } ^ { y } \ \times _ { \delta ^ { n } , Z ^ { x } } \widetilde Z ^ { x }$dans$\widetilde { Z } ^ { x }$. D’après le lemme IV.2, on a

$$
\pi^ {*} (\operatorname{cl} \left(\delta^ {n}\right)) = \operatorname{cl} \left(\widetilde {\delta} ^ {n}\right) + \sum_ {J \neq \emptyset} \operatorname{cl} \left(\widetilde {\mathfrak {X}} _ {J} ^ {y}\right)
$$

et donc

$$
\pi^ {*} (\operatorname{cl} \left(\delta^ {n}\right)) \cdot u = \operatorname{cl} \left(\widetilde {\delta} ^ {n}\right) \cdot u + \sum_ {J \neq \emptyset} \operatorname{cl} \left(\widetilde {\mathfrak {X}} _ {J} ^ {y}\right) \cdot u.
$$

Pour toute partie$I \neq \emptyset$, on a de la même façon

$$
\pi_ {I} ^ {*} \big (\operatorname{cl} \left(\delta_ {I} ^ {n}\right) \big) \cdot \iota_ {E _ {I} ^ {x}} ^ {*} (u) = \sum_ {J \supseteq I} \operatorname{cl} \left(\widetilde {\mathfrak {X}} _ {J} ^ {y}\right) \cdot u.
$$

La conclusion${ \bf s } '$en deduit aussitôt puisque pour toute partie´$J \neq \emptyset$, on a $\sum _ { J \supseteq I } ( - 1 ) ^ { | I | } = 0 .$!"

## b) Une formule des points fixes sur l’ouvert$\mathfrak { X } _ { \varnothing }$

On suppose dans ce dernier paragraphe que la strate ouverte dense$\mathfrak { X } _ { \varnothing }$de $\mathfrak { X }$est un champ algebrique au sens de Deligne-Mumford´${ \mathrm { c } } ^ { \prime }$est-à-dire qu’au voisinage de tout point de$\mathfrak { X } _ { \varnothing }$il existe un revêtement etale par un sch´ ema.´

On considère une correspondance Γ dans X au-dessus de l’endomorphisme$\varphi$de la base$S$qui est engendree par´$\Gamma _ { \emptyset }$et telle que la restriction $\bar { p } _ { \Gamma } ^ { \prime } : \Gamma _ { \varnothing } \to \mathfrak { X } _ { \varnothing }$de la première projection à$\Gamma _ { \emptyset }$est etale.´

Si$x : s \hookrightarrow S$est un point ferme de´$S , y = \varphi \circ x$et$n \geq 1$est un entier tel que$y \circ \mathrm { F r o b } ^ { n } = \mathrm { F r o b } ^ { n } \circ y = x$, la fibre$\Gamma _ { \varnothing } ^ { x } = \Gamma _ { \varnothing } \times _ { S , x } s$de$\Gamma _ { \emptyset }$en x coupe transversalement dans$\mathfrak { X } _ { \varnothing } ^ { x } \times _ { s } \mathfrak { X } _ { \varnothing } ^ { y }$le graphe$\delta ^ { n } : \mathfrak { X } _ { \varnothing } ^ { y } \to \mathfrak { X } _ { \varnothing } ^ { x } \times _ { s } \mathfrak { X } _ { \varnothing } ^ { y }$de Frob<sup>n</sup>$: { \mathfrak { X } } _ { \varnothing } ^ { y } \to { \mathfrak { X } } _ { \varnothing } ^ { x }$

On note Le$⨏ _ { x } ( \Gamma _ { \varnothing } \times \mathrm { F r o b } ^ { n } )$le nombre des points de l’intersection $\mathfrak { X } _ { \varnothing } ^ { y } \ \times _ { \delta ^ { n } , \mathfrak { X } _ { \varnothing } ^ { x } \times _ { s } \mathfrak { X } _ { \varnothing } ^ { y } } \ \Gamma _ { \varnothing } ^ { x }$de$\Gamma _ { \varnothing } ^ { x } \cot \delta ^ { n }$, chacun etant compt´ e avec sa multiplicit´ e´ egale à l’inverse du cardinal du groupe fini de ses automorphi´ smes.

D’autre part, on dispose de la classe de cohomologie cl(Γ) de Γ qui est une section du faisceau -adique lisse$R ^ { 2 d } ( p _ { Z } ) _ { * } \mathbb { Q } _ { \ell } ( d )$puis, pour x et $n \geq 1$comme ci-dessus, de sa fibre$x ^ { * } ( \mathrm { c l } ( \Gamma ) )$en x qui induit une famille d’homomorphismes

$$
R ^ {i} (p _ {\mathfrak {X} ^ {y}}) _ {*} \mathbb {Q} _ {\ell} \rightarrow R ^ {i} (p _ {\mathfrak {X} ^ {x}}) _ {*} \mathbb {Q} _ {\ell}, 0 \leq i \leq 2 d,
$$

tandis que Frob${ \bf \Phi } ^ { n } : \mathfrak { X } ^ { y }  \mathfrak { X } ^ { x }$induit des homomorphismes en sens inverse

$$
R ^ {i} (p _ {\mathfrak {X} ^ {x}}) _ {*} \mathbb {Q} _ {\ell} \rightarrow R ^ {i} (p _ {\mathfrak {X} ^ {y}}) _ {*} \mathbb {Q} _ {\ell}, 0 \leq i \leq 2 d.
$$

On notera

$$
\begin{array}{l} \operatorname{Tr} _ {R ^ {*} (p _ {\mathfrak {X} ^ {x}}) _ {*} \mathbb {Q} _ {\ell}} (x ^ {*} (\operatorname{cl} (\Gamma)) \times \operatorname{Frob} ^ {n}) \\ = \sum_ {i = 0} ^ {2 d} (- 1) ^ {i} \operatorname{Tr} _ {R ^ {i} (p _ {\mathfrak {X} ^ {x}}) _ {*} \mathbb {Q} _ {\ell}} (x ^ {*} (\operatorname{cl} (\Gamma)) \circ \operatorname{Frob} ^ {n}) \\ = \sum_ {i = 0} ^ {2 d} (- 1) ^ {i} \operatorname{Tr} _ {R ^ {i} (p _ {\mathfrak {X} ^ {y}}) _ {*} \mathbb {Q} _ {\ell}} (\operatorname{Frob} ^ {n} \circ x ^ {*} (\operatorname{cl} (\Gamma))). \end{array}
$$

De même, si$I \neq \emptyset$est une partie de$\{ 1 , \ldots , m \}$telle que$\mathfrak { X } _ { I }$ne soit pas vide et$u _ { I }$est une section du faisceau -adique lisse sur$S$

$$
R ^ {2 (d - | I |)} \left(p _ {\overline {{\mathfrak {X}}} _ {I \times_ {\varphi , S}} \overline {{\mathfrak {X}}} _ {I}}\right) _ {*} \mathbb {Q} _ {\ell} (d - | I |),
$$

on peut introduire pour tout x et tout$n \geq 1$comme ci-dessus

$$
\begin{array}{l} \operatorname{Tr} _ {R ^ {*} (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {x}}) _ {*} \mathbb {Q} _ {\ell}} \left(x ^ {*} (u _ {I}) \times \operatorname{Frob} ^ {n}\right) \\ = \sum_ {i = 0} ^ {2 (d - | I |)} (- 1) ^ {i} \operatorname{Tr} _ {R ^ {i} (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {x}}) _ {*} \mathbb {Q} _ {\ell}} \left(x ^ {*} (u _ {I}) \circ \operatorname{Frob} ^ {n}\right) \\ = \sum_ {i = 0} ^ {2 (d - | I |)} (- 1) ^ {i} \operatorname{Tr} _ {R ^ {i} (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {y}}) _ {*} \mathbb {Q} _ {\ell}} \left(\operatorname{Frob} ^ {n} \circ x ^ {*} (u _ {I})\right). \end{array}
$$

Theor´ eme IV.7 (Formule des points fixes sur un ouvert instable).\` – Supposons que$\mathfrak { X }$est propre sur S et que la strate ouverte dense$\mathfrak { X } _ { \varnothing }$de$\mathfrak { X }$ est algebrique au sens de Deligne-Mumford.´

Soit Γ une correspondance dans X au-dessus d’un endomorphisme ϕ du schema de base S qui est engendr´ ee par´$\Gamma _ { \emptyset }$et telle que la restriction $p _ { \Gamma } ^ { \prime } : \Gamma _ { \emptyset } \to \mathfrak { X } _ { \emptyset }$de la première projection à$\Gamma _ { \emptyset }$est etale.´

Et supposons que Γ stabilise l’ouvert$\mathfrak { X } _ { \varnothing }$de X au voisinage de ses points fixes, au sens de la definition´ IV.3.

Alors il existe un entier$n _ { 0 } \geq 0$et des sections$u _ { I }$sur S des faisceaux -adiques lisses

$$
R ^ {2 (d - | I |)} \left(p _ {\overline {{\mathfrak {X}}} _ {I \times_ {\varphi , S}} \overline {{\mathfrak {X}}} _ {I}}\right) * \mathbb {Q} _ {\ell} (d - | I |), I \neq \emptyset ,
$$

tels que pour tout point ferme´$x : s \hookrightarrow s$avec$y = \varphi \circ x$et tout entier $n > n _ { 0 }$tel que$y \circ \mathrm { F r o b } ^ { n } = \mathrm { F r o b } ^ { n } \circ y = x ,$, on ait

$$
\begin{array}{l} \operatorname{Lef} _ {x} \left(\Gamma_ {\emptyset} \times \operatorname{Frob} ^ {n}\right) = \operatorname{Tr} _ {R ^ {*} (p _ {\mathfrak {X} ^ {x}}) _ {*} \mathbb {Q} _ {\ell}} (x ^ {*} (\operatorname{cl} (\Gamma)) \times \operatorname{Frob} ^ {n}) \\ \qquad + \sum_ {I \neq \emptyset} (- 1) ^ {| I |} \operatorname{Tr} _ {R ^ {*} (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {x}}) _ {*} \mathbb {Q} _ {\ell}} \left(x ^ {*} (u _ {I}) \times \operatorname{Frob} ^ {n}\right). \end{array}
$$

Demonstration :´ Soit$n _ { 0 } \geq 0$un entier tel que la normalisation$\widetilde { \Gamma } ^ { \prime }$sur$\widetilde { Z }$de $\Gamma _ { \mathcal { Y } } ^ { \prime } = ( \mathfrak { X } _ { \mathcal { Y } } \times \mathfrak { X } _ { \mathcal { Y } } ) \times _ { ( \mathrm { F r o b } ^ { n _ { 0 } } , \mathrm { I d } ) , \mathfrak { X } _ { \mathcal { Y } } \times \mathfrak { X } _ { \mathcal { Y } } } \Gamma _ { \mathcal { Y } }$ verifie la conclusion de la proposition´ $\mathrm { I } \tilde { \mathrm { V } } . \boldsymbol { 5 }$

Pour tout point ferme´$x : s \hookrightarrow S$avec$y = \varphi \circ x$et tout entier$n > n _ { 0 }$tel que$y \circ \mathrm { F r o b } ^ { n } = \mathrm { F r o b } ^ { n } \circ y = x$, on a evidemment´

$$
\operatorname{Lef} _ {x} \left(\Gamma_ {\emptyset} \times \operatorname{Frob} ^ {n}\right) = \operatorname{Lef} _ {x} \left(\Gamma_ {\emptyset} ^ {\prime} \times \operatorname{Frob} ^ {n - n _ {0}}\right).
$$

On pretend que ´

$$
\operatorname{Lef} _ {x} \left(\Gamma_ {\emptyset} ^ {\prime} \times \operatorname{Frob} ^ {n - n _ {0}}\right) = \operatorname{cl} (\widetilde {\delta} ^ {n - n _ {0}}) \cdot x ^ {*} (\operatorname{cl} (\widetilde {\Gamma} ^ {\prime})).
$$

En effet, les classes de cohomologie cl$( \widetilde { \delta } ^ { n - n _ { 0 } } )$et cl$( \widetilde { \Gamma } ^ { \prime } )$proviennent de sec- tions de faisceaux de cohomologie à supports dans les images de$\widetilde { \delta } ^ { n - n _ { 0 } }$et $\widetilde \Gamma ^ { \prime } : \mathrm { c } ^ { \prime }$est la façon même dont les classes de cohomologie sont definies dans´ le paragraphe$2 \mathrm { a }$de l’appendice A. Et l’intersection c$( \widetilde { \delta } ^ { n - n _ { 0 } } ) \cdot x ^ { * } ( \mathrm { c l } ( \widetilde { \Gamma } ^ { \prime } ) )$  provient de la section obtenue par produit “cup” dans un faisceau de cohomologie à supports dans l’intersection des images de$\widetilde { \delta } ^ { n - n _ { 0 } }$et$\widetilde { \Gamma } ^ { \prime }$. Or, puisque $\widetilde { \Gamma } ^ { \prime }$verifie la conclusion de la proposition IV.5, les images de´$\widetilde { \delta } ^ { n - n _ { 0 } }$et$\widetilde { \Gamma } ^ { \prime }$ne se rencontrent pas en dehors de$\mathfrak { X } _ { \varnothing } \times \mathfrak { X } _ { \varnothing }$. De plus,$\mathfrak { X } _ { \varnothing }$ est algebrique au´ sens de Deligne-Mumford et$\widetilde { \delta } ^ { n - n _ { 0 } }$et$\widetilde { \Gamma } _ { \varnothing } ^ { \prime }$se coupent transversalement sur $\mathfrak { X } _ { \varnothing } \times \mathfrak { X } _ { \varnothing }$. Le calcul de l’intersection cl$( \widetilde { \delta } ^ { n - n _ { 0 } } ) \cdot x ^ { * } ( \mathrm { c l } ( \widetilde { \Gamma } ^ { \prime } ) )$se fait localement  (pour la topologie etale) au voisinage de chacun des points d’intersection´ dans le champ$\mathfrak { X } _ { \varnothing }$. On est ramene au cas d’une intersection transversale´ dans un schema lisse. D’où la formule.´

D’après cette formule et la proposition IV.6, il existe des sections$u _ { I } ^ { \prime }$sur S des faisceaux -adiques

$$
R ^ {2 (d - | I |)} (p _ {\overline {{\mathfrak {X}}} _ {I \times_ {\varphi \circ \mathrm{Frob} ^ {n _ {0}}, S}} \overline {{\mathfrak {X}}} _ {I}}) _ {*} \mathbb {Q} _ {\ell} (d - | I |), I \neq \emptyset ,
$$

telles que pour tout point x et tout entier$n > n _ { 0 }$comme ci-dessus, on ait

$$
\begin{array}{l} \operatorname{Lef} _ {x} \left(\Gamma_ {\emptyset} \times \operatorname{Frob} ^ {n}\right) = \operatorname{cl} (\delta^ {n - n _ {0}}) \cdot x ^ {*} (\operatorname{cl} (\Gamma^ {\prime})) \\ \qquad + \sum_ {I \neq \emptyset} (- 1) ^ {| I |} \operatorname{cl} \left(\delta_ {I} ^ {n - n _ {0}}\right) \cdot x ^ {*} (u _ {I} ^ {\prime}). \end{array}
$$

Ici,$\Gamma ^ { \prime }$est la normalisation sur Z de$\Gamma _ { \mathcal { Y } } ^ { \prime } = ( \mathfrak { X } _ { \mathcal { Y } } \times \mathfrak { X } _ { \mathcal { Y } } ) \times _ { ( \mathrm { F r o b } ^ { n _ { 0 } } , \mathrm { I d } ) , \mathfrak { X } _ { \mathcal { Y } } \times \mathfrak { X } _ { \mathcal { Y } } } \Gamma _ { \mathcal { Y } }$et donc

$$
\operatorname{cl} \left(\delta^ {n - n _ {0}}\right) \cdot x ^ {*} \left(\operatorname{cl} \left(\Gamma^ {\prime}\right)\right) = \operatorname{cl} \left(\delta^ {n}\right) \cdot x ^ {*} \left(\operatorname{cl} (\Gamma)\right).
$$

Pour toute$I \neq \emptyset$telle que$\mathfrak { X } _ { I }$ne soit pas vide, notons$u _ { I }$l’image de$u _ { I } ^ { \prime }$ par l’homomorphisme d’image directe

$$
\begin{array}{c} (\operatorname{Frob} ^ {n _ {0}}, \operatorname{Id}) _ {*}: R ^ {2 (d - | I |)} (p _ \overline {{\mathfrak {X}}} _ {I \times_ {\varphi \circ \operatorname{Frob} ^ {n _ {0}, s}} \overline {{\mathfrak {X}}} _ {I}}) _ {*} \mathbb {Q} _ {\ell} (d - | I |) \\ \longrightarrow R ^ {2 (d - | I |)} (p _ {\overline {{\mathfrak {X}}} _ {I \times_ {\varphi , s}} \overline {{\mathfrak {X}}} _ {I}}) _ {*} \mathbb {Q} _ {\ell} (d - | I |). \end{array}
$$

Alors on a pour tout point x et tout entier$n > n _ { 0 }$comme ci-dessus

$$
\operatorname{Lef} _ {x} \left(\Gamma_ {\emptyset} \times \operatorname{Frob} ^ {n}\right) = \operatorname{cl} \left(\delta^ {n}\right) \cdot x ^ {*} (\operatorname{cl} (\Gamma)) + \sum_ {I \neq \emptyset} (- 1) ^ {| I |} \operatorname{cl} \left(\delta_ {I} ^ {n}\right) \cdot x ^ {*} \left(u _ {I}\right).
$$

On conclut d’après le theorème A.13.´

## 3) Gen´ eralisation au cas non propre´

Dans ce dernier paragraphe, on ne suppose plus que$\mathfrak { X }$est propre sur S.

On considère toujours une correspondance geom´ etrique sur´ X qui stabilise$\mathfrak { X } _ { \varnothing }$au voisinage de ses points fixes et on cherche à interpreter les´ nombres de points fixes dans$\mathfrak { X } _ { \varnothing }$en termes cohomologiques à la façon du theorème IV.7. On y parvient en recourant au th´ eorème de Fujiwara sur´ la conjecture de Deligne. Cela amène à raisonner en termes de correspondances cohomologiques sur les espaces de modules grossiers.

## a) Espaces de modules grossiers

On note${ \mathfrak { X } } ^ { \mathrm { g r } }$l’espace algebrique grossier associ´ e au champ serein com-´ pactifiable X sur S et$p _ { \mathfrak { X } } ^ { \mathrm { g r } } : \mathfrak { X } ^ { \mathrm { g r } } \to S$sa projection canonique. Comme$\mathfrak { X }$ est lisse de dimension d sur S, il resulte de la proposition A.5 que´${ \mathfrak { X } } ^ { \mathrm { g r } }$est cohomologiquement lisse de dimension d sur S au sens$\mathrm { \ q u ^ { \prime } i l }$est muni d’un isomorphisme naturel induit par X

$$
R \left(p _ {\mathfrak {X}} ^ {\mathrm{gr}}\right) ^ {!} \mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\to}} \mathbb {Q} _ {\ell} (d) [ 2 d ].
$$

Pour toute partie I de$\{ 1 , \ldots , m \}$, on note$\overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } }$l’image schematique de´ $\overline { { \mathfrak { X } } } _ { I }$dans$\mathcal { X } ^ { \mathrm { g r } } . \mathrm { C }$’est un ferme et d’après le th´ eorème A.2, l’espace de modules´ grossier de$\overline { { \mathfrak { X } } } _ { I }$lui est relie par un morphisme fini, surjectif et radiciel. On ´ en deduit que´$p _ { \overline { { \mathfrak { X } } } _ { I } } ^ { \mathrm { g r } } : \overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } } \to \overline { { S } }$est cohomologiquement lisse de dimension $d - | I |$au sens qu’on a un isomorphisme induit par$\overline { { \mathfrak { X } } } _ { I }$

$$
R \left(p _ {\overline {{\mathfrak {X}}} _ {I}} ^ {\mathrm{gr}}\right) ^ {!} \mathbb {Q} _ {\ell} \rightarrow \mathbb {Q} _ {\ell} (d - | I |) [ 2 d - 2 | I | ].
$$

On note encore$Z ^ { \mathrm { g r } } = { \mathfrak { X } } ^ { \mathrm { g r } } \times _ { \varphi , S } { \mathfrak { X } } ^ { \mathrm { g r } }$et$\widetilde { Z } ^ { \mathrm { g r } }$l’espace algebrique grossier´ associe à l’´ eclat´ e´$\widetilde { Z }$de$Z = { \mathfrak { X } } \times _ { \varphi , S } { \mathfrak { X } }$. Tous deux sont cohomologiquement lisses de dimension 2d sur S et ils sont relies par un morphisme propre et´ birationnel$\pi : { \widetilde { Z } } ^ { \mathrm { g r } }  Z ^ { \mathrm { g r } }$

Pour toute I, on designe par´$E _ { I } ^ { \mathrm { g r } }$le ferme de´$\widetilde { Z } ^ { \mathrm { g r } }$qui est l’image schematique de ´$E _ { I }$. Il est cohomologiquement lisse de dimension$2 d - | \bar { I } |$ sur S. L’image du morphisme compose´$E _ { I } ^ { \mathrm { g r } } \hookrightarrow \widetilde { Z } ^ { \mathrm { g r } } \longrightarrow Z ^ { \mathrm { g r } }$est le carre´ $\overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } } \times _ { \varphi , S } \overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } }$

On peut considerer aussi un point ferm´ e´$x : s \hookrightarrow S$du schema de base´ S et un entier$n \in \mathbb N$tel que$y = \varphi \circ x$verifie´$y \circ \mathrm { F r o b } ^ { n } = \mathrm { F r o b } ^ { n } \circ y = x$ On designe par´$\mathfrak { X } ^ { \mathrm { g r } , x } , \mathfrak { X } ^ { \mathrm { g r } , y } , \overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } , x } , \overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } , y } , Z ^ { \mathrm { g r } , x } , \widetilde { Z } ^ { \mathrm { g r } , x }$, et$E _ { I } ^ { \mathrm { g r } , x }$les fibres de $\mathfrak { X } ^ { \mathrm { g r } } , \overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } } , Z ^ { \mathrm { g r } } , \widetilde { Z } ^ { \mathrm { g r } }$et$E _ { I } ^ { \mathrm { g r } }$au-dessus de x (ou y) et par$p _ { \mathfrak { X } ^ { x } } ^ { \mathrm { g r } } , p _ { \mathfrak { X } ^ { y } } ^ { \mathrm { g r } } , p _ { \overline { { \mathfrak { X } } } _ { I } ^ { x } } ^ { \mathrm { g r } } , p _ { \overline { { \mathfrak { X } } } _ { I } ^ { y } } ^ { \mathrm { g r } } ,$ $p _ { Z ^ { x } } ^ { \mathrm { g r } } , p _ { \widetilde { Z } ^ { x } } ^ { \mathrm { g r } } , p _ { E _ { I } ^ { x } } ^ { \mathrm { g r } }$leurs projections naturelles sur s. D’après le theorème A.2(ii)´ et la proposition A.5, toutes sont cohomologiquement lisses et on a des isomorphismes canoniques

$$
x ^ {*} R \big (p _ {\mathfrak {X}} ^ {\mathrm{gr}} \big) ^ {!} \mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\to}} R \big (p _ {\mathfrak {X} ^ {x}} ^ {\mathrm{gr}} \big) ^ {!} \mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\to}} \mathbb {Q} _ {\ell} (d) [ 2 d ] ,
$$

$$
x ^ {*} R \left(p _ {\overline {{\mathfrak {X}}} _ {I}} ^ {\mathrm{gr}}\right) ^ {!} \mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\to}} R \left(p _ {\overline {{\mathfrak {X}}} _ {I} ^ {x}} ^ {\mathrm{gr}}\right) ^ {!} \mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\to}} \mathbb {Q} _ {\ell} (d - | I |) [ 2 d - 2 | I | ],
$$

$$
x ^ {*} R \left(p _ {Z} ^ {\mathrm{gr}}\right) ^ {!} \mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\to}} R \left(p _ {Z ^ {x}} ^ {\mathrm{gr}}\right) ^ {!} \mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\to}} \mathbb {Q} _ {\ell} (2 d) [ 4 d ],
$$

$$
x ^ {*} R \big (p _ {\widetilde {Z}} ^ {\mathrm{gr}} \big) ^ {!} \mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\to}} R \big (p _ {\widetilde {Z} ^ {x}} ^ {\mathrm{gr}} \big) ^ {!} \mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\to}} \mathbb {Q} _ {\ell} (2 d) [ 4 d ] ,
$$

$$
x ^ {*} R \left(p _ {E _ {I}} ^ {\mathrm{gr}}\right) ^ {!} \mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\to}} R \left(p _ {E _ {I} ^ {x}} ^ {\mathrm{gr}}\right) ^ {!} \mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\to}} \mathbb {Q} _ {\ell} (2 d - | I |) [ 4 d - 2 | I | ].
$$

On notera encore$\delta ^ { n } : { \mathfrak { X } } ^ { \operatorname { g r } , y } \to { \mathfrak { X } } ^ { \operatorname { g r } , x } \times _ { s } { \mathfrak { X } } ^ { \operatorname { g r } , y } = Z ^ { \operatorname { g r } , x }$et$\delta _ { I } ^ { n } : \overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } , y }$ $\overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } , x } \times _ { s } \overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } , y }$les graphes de Frob<sup>n</sup> ; ce sont des immersions fermees.´

Le morphisme$\widetilde { \delta } ^ { n } : \mathfrak { X } ^ { y } \to \widetilde { Z } ^ { x }$en induit un autre$\widetilde { \delta } ^ { n } : \mathfrak { X } ^ { \mathrm { g r } , y } \to \widetilde { Z } ^ { \mathrm { g r } , x }$qui relève$\delta ^ { n }$et donc est une immersion fermee.´

Enfin, pour toute partie non vide I de$\{ 1 , \ldots , m \}$, l’image schematique´ de

$$
\widetilde {\mathfrak {X}} _ {I} ^ {y} \xrightarrow {\widetilde {\delta} _ {I} ^ {n}} \widetilde {Z} ^ {x} \longrightarrow \widetilde {Z} ^ {\mathrm{gr}, x}
$$

est un ferme´${ \widetilde { \mathfrak { X } } } _ { I } ^ { y , \mathrm { g r } } \xrightarrow { \widetilde { \delta } _ { I } ^ { n } } { \widetilde { Z } } ^ { \mathrm { g r } , x }$qui est cohomologiquement lisse de dimension d sur s.

D’après le lemme IV.2, le produit fibre´${ \mathfrak { X } } ^ { \operatorname { g r } , y } \times _ { \delta ^ { n } , Z ^ { \operatorname { g r } , x } } { \widetilde { Z } } ^ { \operatorname { g r } , x }$est, comme ferme de´$\widetilde { Z } ^ { \mathrm { g r } , x }$, la reunion sch´ ematique de´${ \mathfrak { X } } ^ { \operatorname { g r } , y } \hookrightarrow { \widetilde { \underline { { \delta } } } } ^ { n } \widetilde { Z } ^ { \operatorname { g r } , x }$et des$\widetilde { \mathfrak { X } } _ { I } ^ { y , \mathrm { g r } } \hookrightarrow \hookrightarrow$ $\widetilde { Z } ^ { \mathrm { g r } , x }$ dont les intersections mutuelles sont de dimensions$< d$

## b) Correspondances cohomologiques

On suppose dorenavant que l’endomorphisme´ ϕ de S est propre.

On considère une correspondance geom´ etrique dans´ X au-dessus de$\varphi .$ $\mathbf { C } '$est un champ normal Γ representable fini sur´${ \mathfrak { X } } \times _ { \varphi , S } { \mathfrak { X } } = Z$, dont le support de$\mathrm { | \bar { m a g e } | \Gamma | }$est de codimension d et dont la seconde projection $p _ { \Gamma } ^ { \prime \prime } \colon \Gamma \to \mathfrak { X }$est propre. On suppose que$\Gamma$est engendre par sa trace´$\Gamma _ { \emptyset }$ au-dessus de l’ouvert$\bar { \boldsymbol { x } _ { \beta } } \times _ { \varphi , s } \bar { \boldsymbol { x _ { \beta } } } \mathrm { c } ^ { \circ }$est-à-dire que$\Gamma _ { \emptyset }$est dense dans Γ. On dispose alors du transforme strict´$\widetilde \Gamma$de Γ dans$\widetilde { Z }$qui est la normalisation de$\Gamma _ { \emptyset }$dans$\widetilde { Z }$. Le morphisme$\pi : \widetilde { \Gamma }  \Gamma$est representable, projectif et´ birationnel.

Notant$\Gamma ^ { \mathrm { g r } }$et$\widetilde { \Gamma } ^ { \mathrm { g r } }$les espaces algebriques grossiers associ´ es à´ Γ et$\widetilde \Gamma$ et$p _ { \Gamma ^ { \mathrm { g r } } } ^ { \prime } , p _ { \Gamma ^ { \mathrm { g r } } } ^ { \prime \prime } : \Gamma ^ { \mathrm { g r } } \overrightarrow { \longrightarrow } \mathfrak { X } ^ { \mathrm { g r } }$et$p _ { \widetilde { \Gamma } ^ { \mathrm { g r } } } ^ { \prime } , p _ { \widetilde { \Gamma } ^ { \mathrm { g r } } } ^ { \prime \prime } : \widetilde { \Gamma } ^ { \mathrm { g r } } \implies \mathfrak { X } ^ { \mathrm { g r } }$les deux couples   de projections, on sait d’après la proposition A.6 que les correspondances geom´ etriques´$\Gamma$et$\widetilde \Gamma$se relèvent en des correspondances cohomologiques

$$
p _ {\Gamma^ {\mathrm{gr}}} ^ {\prime \prime *} \mathbb {Q} _ {\ell} \longrightarrow p _ {\Gamma^ {\mathrm{gr}}} ^ {\prime !} \mathbb {Q} _ {\ell}
$$

$$
p _ {\widetilde {\Gamma} ^ {\mathrm{gr}}} ^ {\prime \prime *} \mathbb {Q} _ {\ell} \longrightarrow p _ {\widetilde {\Gamma} ^ {\mathrm{gr}}} ^ {\prime !} \mathbb {Q} _ {\ell}
$$

et que celles-ci induisent des endomorphismes en cohomologie -adique à supports compacts

$$
\varphi^ {*} R (p _ {\mathfrak {X}})! \mathbb {Q} _ {\ell} \longrightarrow R (p _ {\mathfrak {X}})! \mathbb {Q} _ {\ell}.
$$

On a :

Lemme IV.8. – Les deux endomorphismes en cohomologie

$$
\varphi^ {*} R (p _ {\mathfrak {X}})! \mathbb {Q} _ {\ell} \implies R (p _ {\mathfrak {X}})! \mathbb {Q} _ {\ell}
$$

induits par la correspondance Γ et sa transformee stricte´$\widetilde \Gamma$coïncident.

Demonstration :´ Afin de montrer que les deux endomorphismes induits sont identiques, il suffit de verifier que,´ π designant le morphisme propre et´ birationnel$\widetilde \Gamma  \Gamma$, le compose´

$$
\begin{array}{r c l} p _ {\Gamma^ {\mathrm{gr}}} ^ {\prime \prime *} \mathbb {Q} _ {\ell} & \longrightarrow & \pi_ {*} \pi^ {*} p _ {\Gamma^ {\mathrm{gr}}} ^ {\prime \prime *} \mathbb {Q} _ {\ell} = \pi_ {!} p _ {\widetilde {\Gamma} ^ {\mathrm{gr}}} ^ {\prime \prime *} \mathbb {Q} _ {\ell} \\ & \longrightarrow & \pi_ {!} p _ {\widetilde {\Gamma} ^ {\mathrm{gr}}} ^ {\prime !} \mathbb {Q} _ {\ell} = \pi_ {!} \pi^ {!} p _ {\Gamma^ {\mathrm{gr}}} ^ {\prime !} \mathbb {Q} _ {\ell} \\ & \longrightarrow & p _ {\Gamma^ {\mathrm{gr}}} ^ {\prime !} \mathbb {Q} _ {\ell} \end{array}
$$

se confond avec le morphisme

$$
p _ {\Gamma^ {\mathrm{gr}}} ^ {\prime \prime *} \mathbb {Q} _ {\ell} \longrightarrow p _ {\Gamma^ {\mathrm{gr}}} ^ {\prime !} \mathbb {Q} _ {\ell} .
$$

Ces deux flèches coïncident sur un ouvert dense de$\Gamma ^ { \mathrm { g r } }$, donc partout puisque ce sont les adjoints de morphismes

$$
\left(p _ {S} p _ {\mathfrak {X}} ^ {\mathrm{gr}} p _ {\Gamma^ {\mathrm{gr}}} ^ {\prime}\right) _ {!} \mathbb {Q} _ {\ell} (d + d _ {S}) [ 2 d + 2 d _ {S} ] \longrightarrow \mathbb {Q} _ {\ell}
$$

(en notant$d _ { S }$la dimension du morphisme lisse$p _ { S } ~ : { \cal S }  \mathrm { S p e c } \mathbb { F } _ { q } )$bien determin´ es par leurs restrictions à la cohomologie d’un ouvert dense´ . !"

Pour toute partie non vide I de$\{ 1 , \ldots , m \}$, on notera$\widetilde { \Gamma } _ { I } ^ { \mathrm { g r } }$le produit fibre´$E _ { I } ^ { \mathrm { g r } } \times _ { \widetilde { Z } ^ { \mathrm { g r } } } \widetilde { \Gamma } ^ { \mathrm { g r } }$intersection de$E _ { I } ^ { \mathrm { g r } }$et$\widetilde { \Gamma } ^ { \mathrm { g r } }$dans$\widetilde { Z } ^ { \mathrm { g r } }$. Il est muni de deux projections$\overline { { p _ { \widetilde { \Gamma } _ { I } ^ { \mathrm { g r } } } ^ { \prime } } } , p _ { \widetilde { \Gamma } _ { I } ^ { \mathrm { g r } } } ^ { \prime \prime } : \widetilde { \Gamma } _ { I } ^ { \mathrm { g r } }  \overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } }$ dont la seconde est propre et qui verifient´ $\varphi \circ p _ { \mathfrak { X } _ { I } } ^ { \mathrm { g r } } \circ p _ { \widetilde { \Gamma } _ { I } ^ { \mathrm { g r } } } ^ { \prime } \dot { = } p _ { \mathfrak { X } _ { I } } ^ { \mathrm { g r } } \circ p _ { \widetilde { \Gamma } _ { I } ^ { \mathrm { g r } } } ^ { \prime \prime }$

 Si Y est l’un des espaces algebriques que nous consid´ erons, par exemple´ ${ \mathfrak { X } } ^ { \mathrm { g r } } , Z ^ { \mathrm { g r } } = { \mathfrak { X } } ^ { \mathrm { g r } } \times _ { \varphi , S } { \bar { \mathfrak { X } } } ^ { \mathrm { g r } }$ou$\widetilde { Z } ^ { \mathrm { g r } }$, et$\mathcal { Y } ^ { \prime }$est l’un de ses fermes, par exemple´ $\overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } } , \overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } } \times _ { \varphi , S } \overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } }$ou$E _ { I } ^ { \mathrm { g r } }$, on designera par´$i _ { \mathcal { Y } ^ { \prime } } ^ { \mathcal { Y } }$le morphisme d’immersion fermee´$\mathcal { Y } ^ { \prime } \hookrightarrow \mathcal { Y }$. On notera aussi$i _ { \Gamma ^ { \mathrm { g r } } } ^ { Z ^ { \mathrm { g r } } } , \ : i _ { \widetilde { \Gamma } ^ { \mathrm { g r } } } ^ { \widetilde { Z } ^ { \mathrm { g r } } }$et$i _ { \widetilde { \Gamma } _ { I } ^ { \mathrm { g r } } } ^ { \widetilde { Z } ^ { \mathrm { g r } } }$les morphismes finis $\Gamma ^ { \mathrm { g r } }  Z ^ { \mathrm { g r } } , \widetilde \Gamma ^ { \mathrm { g r } }  \widetilde Z ^ { \mathrm { g r } } \mathrm { e t } \widetilde \Gamma _ { \scriptscriptstyle I } ^ { \mathrm { g r } }  \widetilde Z ^ { \mathrm { g r } }$

Comme${ \mathfrak { X } } ^ { \mathrm { g r } } , { \widetilde Z } ^ { \mathrm { g r } }$et les$\overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } } , E _ { I } ^ { \mathrm { g r } }$sont cohomologiquement lisses de dimensions d, 2d et$d - | I | , 2 d - | I |$sur S, on a des isomorphismes canoniques

$$
\left(i \frac {\mathfrak {X} ^ {\mathrm{gr}}}{\mathfrak {X} _ {I} ^ {\mathrm{gr}}}\right) ^ {!} \mathbb {Q} _ {\ell} (| I |) [ 2 | I | ] \stackrel {{\sim}} {{\to}} \mathbb {Q} _ {\ell},
$$

$$
\big (i _ {E _ {I} ^ {\mathrm{gr}}} ^ {\widetilde {Z} ^ {\mathrm{gr}}} \big) ^ {!} \mathbb {Q} _ {\ell} (| I |) [ 2 | I | ] \stackrel {{\sim}} {{\to}} \mathbb {Q} _ {\ell} .
$$

Maintenant, on peut relever les$\widetilde { \Gamma } _ { I } ^ { \mathrm { g r } }$en des correspondances cohomologiques sur les$\overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } }$:

Proposition IV.9. – Pour toute partie non vide I de$\{ 1 , \ldots , m \}$, le produit “cup” dans$\widetilde { Z } ^ { \mathrm { g r } }$avec l’isomorphisme

$$
\mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\longrightarrow}} \left(i _ {E _ {I} ^ {\mathrm{gr}}} ^ {\widetilde {Z} ^ {\mathrm{gr}}}\right) ^ {!} \mathbb {Q} _ {\ell} (| I |) [ 2 | I | ]
$$

definit à partir de la correspondance cohomologique´

$$
p _ {\widetilde {\Gamma} ^ {\mathrm{gr}}} ^ {\prime \prime *} \mathbb {Q} _ {\ell} \longrightarrow p _ {\widetilde {\Gamma} ^ {\mathrm{gr}}} ^ {\prime !} \mathbb {Q} _ {\ell}
$$

une correspondance cohomologique induite

$$
p _ {\widetilde {\Gamma} _ {I} ^ {\mathrm{gr}}} ^ {\prime \prime *} \mathbb {Q} _ {\ell} \longrightarrow p _ {\widetilde {\Gamma} _ {I} ^ {\mathrm{gr}}} ^ {\prime !} \mathbb {Q} _ {\ell}
$$

sur lefaisceau constant$\mathbb { Q } _ { \ell }$de$\overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } }$

Celle-ci induit un endomorphisme en cohomologie -adique à supports compacts

$$
\varphi^ {*} R (p _ {\overline {{\mathfrak {X}}} _ {I}})! \mathbb {Q} _ {\ell} \longrightarrow R (p _ {\overline {{\mathfrak {X}}} _ {I}})! \mathbb {Q} _ {\ell}.
$$

Demonstration :´ Comme$\widetilde { Z } ^ { \mathrm { g r } }$est cohomologiquement lisse, on a un isomorphisme canonique

$$
p _ {\widetilde {\Gamma} ^ {\mathrm{gr}}} ^ {\prime !} \mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\longrightarrow}} \left(i _ {\widetilde {\Gamma} ^ {\mathrm{gr}}} ^ {\widetilde {Z} ^ {\mathrm{gr}}}\right) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ]
$$

et la correspondance cohomologique

$$
p _ {\widetilde {\Gamma} ^ {\mathrm{gr}}} ^ {\prime \prime *} \mathbb {Q} _ {\ell} \longrightarrow p _ {\widetilde {\Gamma} ^ {\mathrm{gr}}} ^ {\prime !} \mathbb {Q} _ {\ell}
$$

peut s’ecrire´

$$
\mathbb {Q} _ {\ell} \longrightarrow \left(i _ {\widetilde {\Gamma} ^ {\mathrm{gr}}} ^ {\widetilde {Z} ^ {\mathrm{gr}}}\right) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ].
$$

Son produit “cup” avec

$$
\mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\longrightarrow}} \left(i _ {E _ {I} ^ {\mathrm{gr}}} ^ {\widetilde {Z} ^ {\mathrm{gr}}}\right) ^ {!} \mathbb {Q} _ {\ell} (| I |) [ 2 | I | ]
$$

est un morphisme

$$
\mathbb {Q} _ {\ell} \longrightarrow \left(i _ {\widetilde {\Gamma} _ {I} ^ {\mathrm{gr}}} ^ {\widetilde {Z} ^ {\mathrm{gr}}}\right) ^ {!} \mathbb {Q} _ {\ell} (d + | I |) [ 2 d + 2 | I | ]
$$

puisque$\widetilde { \Gamma } _ { I } ^ { \mathrm { g r } } = \widetilde { \Gamma } ^ { \mathrm { g r } } \times _ { \widetilde { Z } ^ { \mathrm { g r } } } E _ { I } ^ { \mathrm { g r } }$

  Cette dernière flèche se recrit´

$$
p _ {\widetilde {\Gamma} _ {I} ^ {\mathrm{gr}}} ^ {\prime \prime *} \mathbb {Q} _ {\ell} \longrightarrow p _ {\widetilde {\Gamma} _ {I} ^ {\mathrm{gr}}} ^ {\prime !} \mathbb {Q} _ {\ell}
$$

car$\widetilde { Z } ^ { \mathrm { g r } }$et$\overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } }$sont cohomologiquement lisses de dimensions$2 d$et$d - | I |$ sur S.

La dernière assertion resulte de la proposition A.6(ii).´

## c) Nombres d’intersections

Etant donnes un point ferm´ e´$x : s \hookrightarrow S$et un entier$n \in \mathbb { N }$tels que$y = \varphi \circ x$ verifie Fro´$\mathsf { \Omega } ^ { n } \circ y = y \circ \mathrm { F r o b } ^ { n } = x$, les endomorphismes en cohomologie -adique à supports compacts induits par$\Gamma$ou$\widetilde \Gamma$et les$\Gamma _ { I }$

$$
\begin{array}{l} \varphi^ {*} (p _ {\mathfrak {X}})! \mathbb {Q} _ {\ell} \xrightarrow {\Gamma_ {*} = \widetilde {\Gamma} _ {*}} (p _ {\mathfrak {X}})! \mathbb {Q} _ {\ell} \\ \varphi^ {*} (p _ {\overline {{\mathfrak {X}}} _ {I}})! \mathbb {Q} _ {\ell} \xrightarrow {(\widetilde {\Gamma} _ {I}) _ {*}} (p _ {\overline {{\mathfrak {X}}} _ {I}})! \mathbb {Q} _ {\ell} \end{array}
$$

se specialisent en´

$$
\begin{array}{l} (p _ {\mathfrak {X} ^ {y}})! \mathbb {Q} _ {\ell} \xrightarrow {\Gamma_ {*} ^ {x} = \widetilde {\Gamma} _ {*} ^ {x}} (p _ {\mathfrak {X} ^ {x}})! \mathbb {Q} _ {\ell}, \\ (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {y}})! \mathbb {Q} _ {\ell} \xrightarrow {(\widetilde {\Gamma} _ {I}) _ {*} ^ {x}} (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {x}})! \mathbb {Q} _ {\ell}. \end{array}
$$

D’autre part, les morphismes propres Frob<sup>n</sup> :$\mathfrak { X } ^ { y } \to \mathfrak { X } ^ { x }$et$\mathrm { F r o b } ^ { n } : \overline { { \mathfrak { X } } } _ { I } ^ { y }$ $\to \overline { { \mathfrak { X } } } _ { I } ^ { x }$induisent des homomorphismes en sens inverse

$$
\begin{array}{l} (p _ {\mathfrak {X} ^ {x}})! \mathbb {Q} _ {\ell} \xrightarrow {\text {   Frob   } ^ {n}} (p _ {\mathfrak {X} ^ {y}})! \mathbb {Q} _ {\ell}, \\ (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {x}})! \mathbb {Q} _ {\ell} \xrightarrow {\text {   Frob   } ^ {n}} (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {y}})! \mathbb {Q} _ {\ell}. \end{array}
$$

Notre but est de calculer sous certaines conditions la somme alternee´ des traces

$$
\operatorname{Tr} \left(\Gamma_ {*} ^ {x} \times \operatorname{Frob} ^ {n}, (p _ {\mathfrak {X} ^ {x}})! \mathbb {Q} _ {\ell}\right) = \operatorname{Tr} \left(\operatorname{Frob} ^ {n} \times \Gamma_ {*} ^ {x}, (p _ {\mathfrak {X} ^ {y}})! \mathbb {Q} _ {\ell}\right)
$$

et

$$
\operatorname{Tr} \left((\widetilde {\Gamma} _ {I}) _ {*} ^ {x} \times \operatorname{Frob} ^ {n}, (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {x}}) _ {!} \mathbb {Q} _ {\ell}\right) = \operatorname{Tr} \left(\operatorname{Frob} ^ {n} \times (\widetilde {\Gamma} _ {I}) _ {*} ^ {x}, (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {y}}) _ {!} \mathbb {Q} _ {\ell}\right)
$$

en reliant celles-ci à des nombres d’intersection. Il faut d’abord definir ces´ nombres.

Comme par hypothèse$\mathfrak { X }$est un champ serein compactifiable sur$S _ { : }$ ${ \mathfrak { X } } ^ { \mathrm { g r } }$peut être plonge comme ouvert dense dans un espace alg´ ebrique´$\overline { { \mathfrak { X } } } ^ { \mathrm { g r } }$ propre sur S. Quitte à eclater, on peut supposer que le ferm´ e compl´ ementaire´ ${ \overline { { \boldsymbol { \mathfrak { X } } } } } ^ { \mathrm { g r } } - { \mathfrak { X } } ^ { \mathrm { g r } }$est un diviseur de Cartier$D ^ { \mathrm { g r } }$. On note$\overline { { \boldsymbol { Z } } } ^ { \mathrm { g r } } = \overline { { \boldsymbol { \mathfrak { X } } } } ^ { \mathrm { g r } } \times _ { \varphi , S } \overline { { \boldsymbol { \mathfrak { X } } } } ^ { \mathrm { g r } }$et$\widetilde { \overline { { Z } } } ^ { \mathrm { g r } }$ l’eclat´ e de´${ \overline { { Z } } } ^ { \mathrm { g r } }$le long du ferme´$D ^ { \mathrm { g r } } \times _ { \varphi , S } D ^ { \mathrm { g r } }$; il est muni d’un diviseur exceptionnel$E ^ { \mathrm { g r } }$

La correspondance$\Gamma ^ { \mathrm { g r } }$sur$Z ^ { \mathrm { g r } } \mathrm { s } '$tend par normalisation en des espaces algebriques´$\overline { { \Gamma } } ^ { \mathrm { g r } }$et$\widetilde { \overline { { \Gamma } } } ^ { \mathrm { g r } }$sur${ \overline { { Z } } } ^ { \mathrm { g r } }$et$\widetilde { \overline { { Z } } } ^ { \mathrm { g r } }$dont on note$p _ { \overline { { \Gamma } } ^ { \mathrm { g r } } } ^ { \prime } , ~ p _ { \overline { { \Gamma } } ^ { \mathrm { g r } } } ^ { \prime \prime }$et$p _ { \widetilde { \Gamma } } ^ { \prime } { \mathrm { g r } } , \ p _ { \widetilde { \Gamma } } ^ { \prime \prime } { \mathrm { g r } }$ les projections sur$\overline { { \mathfrak { X } } } ^ { \mathrm { g r } }$. De plus, l’espace algebrique compactifiable´$\widetilde { \Gamma } ^ { \mathrm { g r } }$se plonge comme ouvert dense dans un espace algebrique ´$\bf \tilde { \Gamma }$propre sur S et on peut supposer que le morphisme$\widetilde \Gamma ^ { \mathrm { g r } }  \Gamma ^ { \mathrm { g r } }  Z ^ { \mathrm { g r } }$se prolonge en $\overline { { \widetilde { \Gamma } } } ^ { \mathrm { g r } }  \overline { { \widetilde { \Gamma } } } ^ { \mathrm { g r } }  \widetilde { \overline { { Z } } } ^ { \mathrm { g r } }$

 Pour tout point ferme´$x : s \hookrightarrow S$, tous ces objets ont des fibres audessus de$x \ \mathrm { { q u } ^ { \prime } \mathrm { { o n } } }$note en ajoutant x en exposant. La fibre${ \mathfrak { X } } ^ { \mathrm { g r } , x }$est un ouvert de l’espace algebrique´$\overline { { \boldsymbol { \mathfrak { X } } } } ^ { \mathrm { g r } , \boldsymbol { x } }$propre sur s et son complementaire est´ le diviseur de Cartier$D ^ { \mathrm { g r } , x }$; le morphisme$\widetilde { \overline { { Z } } } ^ { \mathrm { g r } , x }  \overline { { Z } } ^ { \mathrm { g r } , x }$est projectif,${ \mathrm { c } } ^ { \prime }$est un isomorphisme en dehors de$D ^ { \mathrm { g r } , x } \times _ { s } D ^ { \mathrm { g r } , y }$(pour$y = \varphi \circ x )$et l’image reciproque de´$D ^ { \mathrm { g r } , x } \times _ { s } D ^ { \mathrm { g r } , y }$est le diviseur de Cartier$E ^ { \mathrm { g r } , x }$

Lemme IV.10. – Quitte à changer ϕ en$\varphi \circ { \mathrm { F r o b } } ^ { n _ { 0 } }$(pour$n _ { 0 } \geq 0$un entier assez grand) et$\Gamma ^ { \mathrm { g r } } , \ \widetilde { \Gamma } ^ { \mathrm { g r } } , \ \overline { { { \Gamma } } } ^ { \mathrm { g r } } , \ \widetilde { \overline { { { \Gamma } } } } ^ { \mathrm { g r } } , \ \widetilde { \overline { { { \Gamma } } } } ^ { \mathrm { g r } } , \ \overline { { { \widetilde { \Gamma } } } } ^ { \mathrm { g r } }$en les normalisees de leurs images´ reciproques par´$( \mathrm { F r o b } ^ { n _ { 0 } } , \mathrm { I d } )$$\overline { { \mathfrak { X } } } ^ { \mathrm { g r } } \times \overline { { \mathfrak { X } } } ^ { \mathrm { g r } } \to \overline { { \mathfrak { X } } } ^ { \mathrm { g r } } \times \overline { { \mathfrak { X } } } ^ { \mathrm { g r } }$, on a en tout point ferme´$x : s \hookrightarrow$S et pour tout entier$n \geq 0$avec$y = \varphi \circ x$et$y \circ \operatorname { F r o b } ^ { n } =$ $\operatorname { F r o b } ^ { n } \circ y = x$les deux propriet´ es suivantes :´

(i) Le produit fibre sur´$Z ^ { \mathrm { g r } , x } = \mathfrak { X } ^ { \mathrm { g r } , x } \times _ { s } \mathfrak { X } ^ { \mathrm { g r } , y }$de$\widetilde { \Gamma } ^ { \mathrm { g r } , x }$et de$\delta ^ { n } : \mathfrak { X } ^ { \mathrm { g r } , \mathfrak { y } } \to$ $Z ^ { \mathrm { g r } , x }$est propre sur s. Il en est a fortiori de même du produit fibre sur´ chaque$\dot { \overline { { \mathcal { X } } } } _ { I } ^ { \mathrm { g r } , \dot { x } } \times _ { s } \overline { { \mathcal { X } } } _ { I } ^ { \mathrm { g r } , y }$de$\widetilde { \Gamma } _ { I } ^ { \mathrm { g r } , x }$et de δ<sup>n</sup> :$\overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } , y } \to \overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } , x ^ { \cdot } } \times _ { s } \overline { { \mathfrak { X } } } _ { I } ^ { \mathrm { g r } , \tilde { y } }$

(ii) Les correspondances$\Gamma ^ { \mathrm { g r } , x }$et$\widetilde { \Gamma } ^ { \mathrm { g r } , x }$composees avec´ Frob<sup>n</sup> ont un ordre d’annulation > 1 le long de$D ^ { \mathrm { g r } , x } \times _ { s } D ^ { \mathrm { g r } , y }$au sens de la definition´ 5.3.3 de [Fujiwara]. Il en est afortiori de même des correspondances induites $\widetilde { \Gamma } _ { I } ^ { \mathrm { g r } , x }$

Demonstration :´ On utilise toujours le même argument geom´ etrique tir´ e de´ [Pink] :

Localement sur$\overline { { \Gamma } } ^ { \mathrm { g r } }$, considerons les images r´ eciproques´$\ell ^ { \prime } , \ell ^ { \prime \prime }$par les projections$p _ { \overline { { \Gamma } } ^ { \mathrm { g r } } } ^ { \prime } , p _ { \overline { { \Gamma } } ^ { \mathrm { g r } } } ^ { \prime \prime }$de deux equations qui d´ efinissent le diviseur de Cartier´

$D ^ { \mathrm { g r } }$dans$\overline { { \mathfrak { X } } } ^ { \mathrm { g r } }$. Comme$p _ { \overline { { \Gamma } } ^ { \mathrm { g r } } } ^ { \prime \prime - 1 } ( \mathfrak { X } ^ { \mathrm { g r } } ) \subseteq p _ { \overline { { \Gamma } } ^ { \mathrm { g r } } } ^ { \prime - 1 } ( \mathfrak { X } ^ { \mathrm { g r } } )$ou encore$p _ { \overline { { \Gamma ^ { \mathrm { g r } } } } } ^ { \prime - 1 } ( \overline { { \mathfrak { X } } } ^ { \mathrm { g r } } - \mathfrak { X } ^ { \mathrm { g r } } ) \subseteq$ $p _ { \overline { { \Gamma } } ^ { \mathrm { g r } } } ^ { \prime \prime - 1 } ( \overline { { \mathfrak { X } } } ^ { \mathrm { g r } } - \mathfrak { X } ^ { \mathrm { g r } } )$, il existe un entier$e \geq 1$et une fonction a bien definie sur´ l’ouvert consider´ e de´$\overline { { \Gamma } } ^ { \mathrm { g r } }$tels que

$$
\ell^ {\prime \prime e} = a \ell^ {\prime}.
$$

Choisissons$n _ { 0 }$de façon que$q ^ { n _ { 0 } } \geq 2 e$. Si l’on remplace$\overline { { \Gamma } } ^ { \mathrm { g r } }$et a par leurs images reciproques via´ (Frob<sup>n0</sup>, Id) :$\overline { { \mathfrak { X } } } ^ { \mathrm { g r } } \times \overline { { \mathfrak { X } } } ^ { \mathrm { g r } } \to \overline { { \mathfrak { X } } } ^ { \mathrm { g r } } \times \overline { { \mathfrak { X } } } ^ { \mathrm { g r } }$, cette equation´ devient

$$
\ell^ {\prime \prime e} = a \ell^ {\prime q ^ {n _ {0}}}.
$$

Elle reste verifi´ ee si on sp´ ecialise au-dessus d’un point´$x : s \hookrightarrow S$

(i) Dans le produit fibre sur´$\overline { { \mathfrak { X } } } ^ { \mathrm { g r } , x } \times _ { s } \overline { { \mathfrak { X } } } ^ { \mathrm { g r } , y }$de$\overline { { \Gamma } } _ { x } ^ { \mathrm { g r } }$et$( \mathrm { F r o b } ^ { n } , \mathrm { I d } ) : \overline { { \mathfrak { X } } } ^ { \mathrm { g r } , y } \to$ $\overline { { \mathfrak { X } } } ^ { \mathrm { g r } , x } \times _ { s } \overline { { \mathfrak { X } } } ^ { \mathrm { g r } , y }$sont verifi´ ees les deux´ equations´

$$
\left\{ \begin{array}{l} \ell^ {\prime \prime e} = a   \ell^ {\prime q ^ {n _ {0}}} \\ \ell^ {\prime} = \ell^ {\prime \prime q ^ {n}} \end{array} \right.
$$

d’où$\ell ^ { \prime \prime e } ( 1 { - } a \ell ^ { \prime \prime ( q ^ { n _ { 0 } + n } - e ) } ) = 0$. Dans ce produit fibre, l’image r´ eciproque´ de l’ouvert${ \mathfrak { X } } ^ { \mathrm { g r } , x } \times _ { s } { \mathfrak { X } } ^ { \mathrm { g r } , y }$est donc definie par l’´ equation´

$$
1 - a \ell^ {\prime \prime (q ^ {n _ {0} + n} - e)} = 0;
$$

elle est fermee c’est-à-dire propre et il en est de même de son image´ reciproque dans´$\widetilde { \Gamma } ^ { \mathrm { g r } , x }$ou les$\widetilde { \Gamma } _ { I } ^ { \mathrm { g r } , x }$

 (ii) Par composition avec un Frobn, l’equation´$\ell ^ { \prime \prime e } = a \ell ^ { \prime q ^ { n _ { 0 } } }$verifi´ ee sur´ l’ouvert consider´ e de´$\overline { { \Gamma } } ^ { \mathrm { g r } , x }$devient

$$
\ell^ {\prime \prime e} = a \ell^ {\prime q ^ {n _ {0} + n}}
$$

qu’on peut recrire´

$$
(\ell^ {\prime \prime} / \ell^ {\prime}) ^ {e} = a \ell^ {\prime (q ^ {n _ {0} + n} - e)}.
$$

Elle signifie que sur le transforme strict´$\widetilde { \overline { { \Gamma } } } ^ { \mathrm { g r } , x }$compose avec Frob´ <sup>n</sup>,$\ell ^ { \prime \prime } / \ell ^ { \prime }$ s’annule partout où$\ell ^ { \prime } \mathbf { s } ^ { \prime }$annule ;${ \mathrm { c } } '$est la propriet´ e d’annulation à l’ordre´ $> 1$demandee par Fujiwara. Elle est v´ erifi´ ee a fortiori par´$\widetilde { \Gamma } ^ { \mathrm { g r } , x }$puisque le morphisme$\begin{array} { r } { \overline { { \widetilde { \Gamma } } } ^ { \mathrm { g r } , x } \to \widetilde { \overline { { Z } } } ^ { \mathrm { g r } , x } } \end{array}$se factorise à travers$\widetilde { \overline { { \Gamma } } } ^ { \mathrm { g r } , \dot { x } }$!"

Supposons maintenant que la correspondance$\widetilde { \Gamma } ^ { \mathrm { g r } }$verifie la propri´ et´ e de´ conclusion (i) du lemme IV.10. Et considerons comme toujours un point´ ferme´$x : s \hookrightarrow S$et un entier$n \in \mathbb { N }$avec$y = \varphi \circ x$, Frob<sup>n</sup> ◦ y = x.

Cela permet de definir des nombres d’intersection de la correspondance´ cohomologique$\widetilde { \Gamma } _ { \ast }$en x avec$\delta ^ { n } : \mathfrak { X } ^ { y } \to Z ^ { x }$et aussi avec les composantes $\widetilde { \delta } _ { I } ^ { n } : \widetilde { \mathfrak { X } } _ { I } ^ { y } \to \widetilde { Z } ^ { x }$et$\widetilde { \delta } ^ { n } : \mathfrak { X } ^ { y } \to \widetilde { Z } ^ { x }$de$\mathfrak { X } ^ { y } \times _ { \delta ^ { n } , Z ^ { x } } \widetilde { Z } ^ { x }$

On part de la correspondance cohomologique sur$\widetilde { \Gamma } ^ { \mathrm { g r } }$

$$
\mathbb {Q} _ {\ell} = p _ {\widetilde {\Gamma} ^ {\mathrm{gr}}} ^ {\prime \prime *} \mathbb {Q} _ {\ell} \xrightarrow {\widetilde {\Gamma} _ {*}} p _ {\widetilde {\Gamma} ^ {\mathrm{gr}}} ^ {\prime !} \mathbb {Q} _ {\ell}.
$$

En le point x, elle se specialise en´

$$
\mathbb {Q} _ {\ell} = x ^ {*} \mathbb {Q} _ {\ell} \longrightarrow x ^ {*} p _ {\widetilde {\Gamma} ^ {\mathrm{gr}}} ^ {\prime !} \mathbb {Q} _ {\ell} \longrightarrow p _ {\widetilde {\Gamma} ^ {\mathrm{gr}, x}} ^ {\prime !} \mathbb {Q} _ {\ell}
$$

qu’on peut ecrire´

$$
\mathbb {Q} _ {\ell} \longrightarrow \left(i _ {\widetilde {\Gamma} ^ {\mathrm{gr}, x}} ^ {Z ^ {\mathrm{gr}, x}}\right) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ]
$$

ou

$$
\mathbb {Q} _ {\ell} \longrightarrow \left(i _ {\widetilde {\Gamma} ^ {\mathrm{gr}, x}} ^ {\widetilde {Z} ^ {\mathrm{gr}, x}}\right) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ].
$$

$\mathbf { D } '$autre part, on a des isomorphismes

$$
\begin{array}{r c l} \mathbb {Q} _ {\ell} & \stackrel {{\sim}} {{\longrightarrow}} & (\delta^ {n}) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ]  , \\ \mathbb {Q} _ {\ell} & \stackrel {{\sim}} {{\longrightarrow}} & (\widetilde {\delta} ^ {n}) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ]  , \\ \mathbb {Q} _ {\ell} & \stackrel {{\sim}} {{\longrightarrow}} & \big (\widetilde {\delta} _ {I} ^ {n} \big) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ] \end{array}
$$

obtenus en composant$( p _ { \mathfrak { X } ^ { y } } ^ { \operatorname { g r } } ) ^ { ! } \mathbb { Q } _ { \ell } \cong \mathbb { Q } _ { \ell } ( d ) [ 2 d ]$et les$( p _ { \widetilde { \mathfrak { X } } _ { \mathfrak { r } } ^ { y , \mathrm { g r } } } ) ^ { ! } \mathbb { Q } _ { \ell } \cong \mathbb { Q } _ { \ell } ( d ) [ 2 d ]$ avec$( p _ { Z ^ { x } } ^ { \mathrm { g r } } ) ^ { ! } \mathbb { Q } _ { \ell } \cong \mathbb { Q } _ { \ell } ( 2 d ) [ 4 d ]$et$( p _ { \widetilde { \gamma } x } ^ { \mathrm { g r } } ) ^ { ! } \mathbb { Q } _ { \ell } \cong \mathbb { Q } _ { \ell } ( 2 d ) [ 4 d ]$transformes par´ $\delta ^ { n } : \mathfrak { X } ^ { \mathrm { g r } , y }  Z ^ { \mathrm { g r } , x } , \widetilde { \delta } ^ { n } : \mathfrak { X } ^ { \mathrm { g r } , y }  \widetilde { Z } ^ { \mathrm { g r } , x } , \widetilde { \delta } _ { I } ^ { n } : \widetilde { \mathfrak { X } } _ { I } ^ { \mathrm { y , g r } }  \widetilde { Z } ^ { \mathrm { g r } , x }$

    En formant les produits “cup”, on en deduit des morphismes´

$$
\begin{array}{l} \mathbb {Q} _ {\ell} \longrightarrow \left(i \frac {Z ^ {\mathrm{gr} , x}}{\widetilde {\Gamma} ^ {\mathrm{gr} , x} \times \delta^ {n}}\right) ^ {!} \mathbb {Q} _ {\ell} (2 d) [ 4 d ]  , \\ \mathbb {Q} _ {\ell} \longrightarrow \left(i \frac {\widetilde {Z} ^ {\mathrm{gr} , x}}{\widetilde {\Gamma} ^ {\mathrm{gr} , x} \times \widetilde {\delta} ^ {n}}\right) ^ {!} \mathbb {Q} _ {\ell} (2 d) [ 4 d ]  , \\ \mathbb {Q} _ {\ell} \longrightarrow \left(i \frac {\widetilde {Z} ^ {\mathrm{gr} , x}}{\widetilde {\Gamma} ^ {\mathrm{gr} , x} \times \widetilde {\delta} _ {I} ^ {n}}\right) ^ {!} \mathbb {Q} _ {\ell} (2 d) [ 4 d ]  . \end{array}
$$

Puis en prenant l’image directe sur x (qui est propre puisque la conclusion du lemme IV.10(i) est verifi´ ee) et en composant avec les homomorphismes´ de traces sur$Z ^ { \mathrm { g r } , x }$et$\widetilde { Z } ^ { \mathrm { g r } , x }$induits par$Z$et${ \widetilde { Z } } ,$, on en deduit des flèches´

$$
\begin{array}{l} \mathbb {Q} _ {\ell} \to \big (p _ {Z ^ {x}} ^ {\mathrm{gr}} \big) _ {!} \big (i _ {\widetilde {\Gamma} ^ {\mathrm{gr}, x} \times \delta^ {n}} ^ {Z ^ {\mathrm{gr}, x}} \big) _ {!} \big (i _ {\widetilde {\Gamma} ^ {\mathrm{gr}, x} \times \delta^ {n}} ^ {Z ^ {\mathrm{gr}, x}} \big) ^ {!} \mathbb {Q} _ {\ell} (2 d) [ 4 d ] \to \big (p _ {Z ^ {x}} ^ {\mathrm{gr}} \big) _ {!} \mathbb {Q} _ {\ell} (2 d) [ 4 d ] \to \mathbb {Q} _ {\ell}  , \\ \mathbb {Q} _ {\ell} \to \big (p _ {\widetilde {Z} ^ {x}} ^ {\mathrm{gr}} \big) _ {!} \big (i _ {\widetilde {\Gamma} ^ {\mathrm{gr}, x} \times \widetilde {\delta} ^ {n}} ^ {Z ^ {\mathrm{gr}, x}} \big) _ {!} \big (i _ {\widetilde {\Gamma} ^ {\mathrm{gr}, x} \times \widetilde {\delta} ^ {n}} ^ {Z ^ {\mathrm{gr}, x}} \big) ^ {!} \mathbb {Q} _ {\ell} (2 d) [ 4 d ] \to \big (p _ {\widetilde {Z} ^ {x}} ^ {\mathrm{gr}} \big) _ {!} \mathbb {Q} _ {\ell} (2 d) [ 4 d ] \to \mathbb {Q} _ {\ell}  , \\ \mathbb {Q} _ {\ell} \to \big (p _ {\widetilde {Z} ^ {x}} ^ {\mathrm{gr}} \big) _ {!} \big (i _ {\widetilde {T r g r}, x \times \widetilde {\delta} _ {I} ^ {n}} ^ {Z ^ {\mathrm{gr}, x}} \big) _ {!} \big (i _ {\widetilde {\Gamma} ^ {\mathrm{gr}, x} \times \widetilde {\delta} _ {I} ^ {n}} ^ {Z ^ {\mathrm{gr}, x}} \big) ^ {!} \mathbb {Q} _ {\ell} (2 d) [ 4 d ] \to \big (p _ {\widetilde {Z} ^ {x}} ^ {\mathrm{gr}} \big) _ {!} \mathbb {Q} _ {\ell} (2 d) [ 4 d ] \to \mathbb {Q} _ {{\ell}}  . \end{array}
$$

Les images de 1 sont des scalaires$\mathrm { \ q u } ^ { \prime }$on notera

$$
\mathrm{Lef} _ {x} (\widetilde {\Gamma} \times \delta^ {n}),
$$

$$
\mathrm{Lef} _ {x} (\widetilde {\Gamma} \times \widetilde {\delta} ^ {n}),
$$

$$
\operatorname{Lef} _ {x} \left(\widetilde {\Gamma} \times \widetilde {\delta} _ {I} ^ {n}\right).
$$

De la même façon, on peut definir le nombre d’intersection en´ x

$$
\operatorname{Lef} _ {x} \left(\widetilde {\Gamma} _ {I} \times \delta_ {I} ^ {n}\right)
$$

de la correspondance cohomologique

$$
p _ {\widetilde {\Gamma} _ {I} ^ {\mathrm{gr}}} ^ {\prime *} \mathbb {Q} _ {\ell} \xrightarrow {(\widetilde {\Gamma} _ {I}) _ {*}} p _ {\widetilde {\Gamma} _ {I} ^ {\mathrm{gr}}} ^ {\prime \prime !} \mathbb {Q} _ {\ell}
$$

avec

$$
\delta_ {I} ^ {n}: \overline {{\mathfrak {X}}} _ {I} ^ {y} \longrightarrow \overline {{\mathfrak {X}}} _ {I} ^ {x} \times_ {s} \overline {{\mathfrak {X}}} _ {I} ^ {y}.
$$

d) Formule des points fixes

Nous allons prouver :

Theor´ eme IV.11.\` –

(i) Supposons que${ \mathfrak { X } } ^ { \mathrm { g r } }$se plonge comme ouvert dense dans un espace algebrique´$\stackrel { \mathrm { \scriptsize ~ * ~ } } { \mathrm { \textstyle ~ \mathfrak { X } } } ^ { \mathrm { \scriptsize { g r } } }$propre sur S qui devient un schema au moins après ex-´ tensionfinie du corps de base$\mathbb { F } _ { q } .$. Et supposons que les correspondances $\Gamma$et$\widetilde \Gamma$satisfont les conclusions du lemme IV.10.

Alors pour tout point ferme´$x : s \hookrightarrow s$et tout entier$n \in \mathbb { N }$avec $y = \varphi \circ x , { \mathrm { F r o b } } ^ { n } \circ y = x ,$, on a

$$
\begin{array}{l} \operatorname{Tr} \left(\Gamma_ {*} ^ {x} \times \operatorname{Frob} ^ {n}, (p _ {\mathfrak {X} ^ {x}}) _ {!} \mathbb {Q} _ {\ell}\right) + \sum_ {I \neq \emptyset} (- 1) ^ {| I |} \operatorname{Tr} \left((\widetilde {\Gamma} _ {I}) _ {*} ^ {x} \times \operatorname{Frob} ^ {n}, (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {x}}) _ {!} \mathbb {Q} _ {\ell}\right) \\ = \operatorname{Lef} _ {x} (\widetilde {\Gamma} \times \widetilde {\delta} ^ {n}). \end{array}
$$

(ii) Supposons deplus qu’au-dessus d’un ouvert$S ^ { \prime }$de$S ,$la correspondance $\widetilde { \Gamma }$satisfait la conclusion de la proposition IV.5, que le champ$\mathfrak { X } _ { \varnothing }$est algebrique au sens de Deligne-Mumford et que la première projec´ tion $p _ { \Gamma _ { \emptyset } } ^ { \prime }$de la trace$\Gamma _ { \emptyset }$de Γ au-dessus de${ \mathfrak { X } } _ { \varnothing } \times _ { \varphi , S } { \mathfrak { X } } _ { \varnothing }$est etale.´

Si, pour$x : s \hookrightarrow S ^ { \prime }$, on note$\operatorname { L e f } _ { x } ( \Gamma _ { \varnothing } \times \operatorname { F r o b } ^ { n } )$le nombre des points d’intersection comptes avec multiplicit´ es de´$\Gamma _ { \emptyset }$et du graphe de Frob<sup>n</sup> dans $\mathfrak { X } ^ { x } \times _ { s } \mathfrak { X } ^ { y }$, on a alors

$$
\operatorname{Lef} _ {x} \left(\widetilde {\Gamma} \times \widetilde {\delta} ^ {n}\right) = \operatorname{Lef} _ {x} \left(\Gamma_ {\emptyset} \times \operatorname{Frob} ^ {n}\right).
$$

Demonstration :´ (i) D’après le lemme IV.8, les correspondances cohomologiques sur$\Gamma ^ { \mathrm { g r } }$et$\widetilde { \Gamma } ^ { \mathrm { g r } }$associees aux correspondances g´ eom´ etriques´$\Gamma$et$\widetilde \Gamma$ induisent le même homomorphisme$\varphi ^ { * } ( p \mathfrak { x } ) ! \mathbb { Q } _ { \ell } \to ( p \mathfrak { x } ) ! \mathbb { Q } _ { \ell }$et donc on a

$$
\operatorname{Tr} \left(\Gamma_ {*} ^ {x} \times \operatorname{Frob} ^ {n}, (p _ {\mathfrak {X} ^ {x}})! \mathbb {Q} _ {\ell}\right) = \operatorname{Tr} \left(\widetilde {\Gamma} _ {*} ^ {x} \times \operatorname{Frob} ^ {n}, (p _ {\mathfrak {X} ^ {x}})! \mathbb {Q} _ {\ell}\right).
$$

La correspondance cohomologique$p _ { \widetilde { \Gamma } ^ { \mathrm { g r } } } ^ { \prime * } \mathbb { Q } _ { \ell } \  \ p _ { \widetilde { \Gamma } ^ { \mathrm { g r } } } ^ { \prime \prime } \mathbb { Q } _ { \ell }$supportee par´ $\widetilde { \Gamma } ^ { \mathrm { g r } }$et relative au faisceau constant$\mathbb { Q } _ { \ell }$sur${ \mathfrak { X } } ^ { \mathrm { g r } }$peut être vue comme une correspondance cohomologique supportee par´$\hat { \widetilde { \Gamma } } ^ { \mathrm { g r } }$et relative au faisceau sur$\overline { { \mathfrak { X } } } ^ { \mathrm { g r } }$qui est le prolongement par 0 de$\mathbb { Q } _ { \ell }$de${ \mathfrak { X } } ^ { \mathrm { g r } }$à$\overline { { \mathfrak { X } } } ^ { \mathrm { g r } }$. Comme$\overline { { \mathfrak { X } } } ^ { \mathrm { g r } }$est un espace algebrique propre sur´ S, le theorème g´ en´ eral des points fixes´ de Grothendieck-Lefschetz-Verdier s’applique. La conclusion du lemme IV.10(i) etant v´ erifi´ ee par hypothèse, il fait apparaître des termes à distance´ finie dont la somme$\mathrm { n ^ { \prime } }$est autre que Lef$( \widetilde { \Gamma } ^ { \bullet } \widetilde { \times } \delta ^ { n } )$et des termes à l’infini. Or on a aussi suppose que la conclusion du lemme IV.10(ii) est v´ erifi´ ee´ et que$\overline { { \mathfrak { X } } } ^ { \mathrm { g r } }$devient un schema (propre sur´ S) après extension des scalaires de$\mathbb { F } _ { q }$à sa clôture algebrique´$\overline { { \mathbb { F } } } _ { q }$. Cela permet d’appliquer la proposition 5.3.4 de [Fujiwara], la somme des termes à l’infini s’annule et on obtient en definitive´

$$
\operatorname{Tr} \left(\widetilde {\Gamma} ^ {x} \times \operatorname{Frob} ^ {n}, (p _ {\mathfrak {X} ^ {x}})! \mathbb {Q} _ {\ell}\right) = \operatorname{Lef} _ {x} (\widetilde {\Gamma} \times \delta^ {n}).
$$

De la même façon, on a pour toute partie I non vide de$\{ 1 , \ldots , m \}$

$$
\operatorname{Tr} \left((\widetilde {\Gamma} _ {I}) _ {*} ^ {x} \times \operatorname{Frob} ^ {n}, (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {x}})! \mathbb {Q} _ {\ell}\right) = \operatorname{Lef} _ {x} \left(\widetilde {\Gamma} _ {I} \times \delta_ {I} ^ {n}\right).
$$

Il s’agit donc de prouver la formule :

$$
\operatorname{Lef} _ {x} \left(\widetilde {\Gamma} \times \delta^ {n}\right) + \sum_ {I \neq \emptyset} (- 1) ^ {| I |} \operatorname{Lef} _ {x} \left(\widetilde {\Gamma} _ {I} \times \delta_ {I} ^ {n}\right) = \operatorname{Lef} _ {x} \left(\widetilde {\Gamma} \times \widetilde {\delta} ^ {n}\right)\tag{1}
$$

Le produit “cup” de la correspondance cohomologique

$$
\mathbb {Q} _ {\ell} \longrightarrow \left(i _ {\widetilde {\Gamma} ^ {\mathrm{gr}, x}} ^ {Z ^ {\mathrm{gr}, x}}\right) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ]
$$

avec

$$
\mathbb {Q} _ {\ell} \longrightarrow (\delta^ {n}) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ]
$$

est egal à celui de la même correspondance cohomologique r´ ecrite´

$$
\mathbb {Q} _ {\ell} \longrightarrow \left(i _ {\widetilde {\Gamma} ^ {\mathrm{gr}, x}} ^ {\widetilde {Z} ^ {\mathrm{gr}, x}}\right) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ]
$$

avec l’homomorphisme image reciproque via´$\delta ^ { n } \times _ { Z ^ { \mathrm { g r } , x } } \widetilde { Z } ^ { \mathrm { g r } , x } \xrightarrow [ ] { \pi } \delta ^ { n }$

$$
\mathbb {Q} _ {\ell} \longrightarrow \pi^ {*} (\delta^ {n}) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ] \longrightarrow \left(i _ {\delta^ {n} \times_ {Z ^ {\mathrm{gr}, x}} \widetilde {Z} ^ {\mathrm{gr}, x}} ^ {\widetilde {Z} ^ {\mathrm{gr}, x}}\right) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ]\tag{2}
$$

On a vu que$\delta ^ { n } \times _ { Z ^ { \mathrm { g r } , x } } \widetilde { Z } ^ { \mathrm { g r } , x }$est la reunion sch´ ematique de´${ \widetilde { \delta } } ^ { n } : { \mathfrak { X } } ^ { \mathrm { g r } , y } \to { \widetilde { Z } } ^ { \mathrm { g r } , x }$ et des$\widetilde { \delta } _ { J } ^ { n } : \widetilde { \mathfrak { X } } _ { J } ^ { y , \mathrm { g r } } \to \widetilde { Z } ^ { \mathrm { g r } , x }$ . Sur chacune de celles-ci, on a un isomorphisme

$$
\mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\longrightarrow}} (\widetilde {\delta} ^ {n}) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ]
$$

ou

$$
\mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\longrightarrow}} \left(\widetilde {\delta} _ {J} ^ {n}\right) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ]
$$

dont l’image directe via l’immersion fermee´${ \widetilde { \delta } } ^ { n } \hookrightarrow \delta ^ { n } \times _ { Z ^ { \mathrm { g r } , x } } { \widetilde { Z } } ^ { \mathrm { g r } , x }$ou$\widetilde { \delta } _ { J } ^ { n } \hookrightarrow$ $\delta ^ { n } \times _ { Z ^ { \mathrm { g r } , x } } \widetilde { Z } ^ { \mathrm { g r } , x }$est un homomorphisme :

$$
\mathbb {Q} _ {\ell} \longrightarrow \left(i _ {\delta^ {n} \times_ {Z ^ {\mathrm{gr}, x}} \widetilde {Z} ^ {\mathrm{gr}, x}} ^ {\widetilde {Z} ^ {\mathrm{gr}, x}}\right) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ]\tag{3) \( \varnothing \)  ou (3) \( _{J} \}
$$

On pretend que la somme (3) des homomorphismes´$( 3 ) _ { \varnothing }$et$( 3 ) _ { J }$est egale à´ l’homomorphisme (2). En effet, il resulte du lemme IV.2 qu’ils coïncident´ sur un ouvert dense donc qu’ils coïncident partout puisqu’on peut les ecrire´ comme des homomorphismes

$$
\mathbb {Q} _ {\ell} \longrightarrow (p _ {\delta^ {n} \times_ {Z _ {x} ^ {\mathrm{gr}}} \widetilde {Z} _ {x} ^ {\mathrm{gr}}}) ^ {!} \mathbb {Q} _ {\ell} (- d) [ - 2 d ]
$$

adjoints d’homomorphismes

$$
(p _ {\delta^ {n} \times_ {Z _ {x} ^ {\mathrm{gr}}} \widetilde {Z} _ {x} ^ {\mathrm{gr}}})! \mathbb {Q} _ {\ell} \longrightarrow \mathbb {Q} _ {\ell} (- d) [ - 2 d ]
$$

complètement determin ´ es par leurs restrictions à la cohomologie d’un ouvert ´ dense.

De ce que (2) est la somme de$( 3 ) _ { \varnothing }$et des$( 3 ) _ { J }$, on deduit :´

$$
\operatorname{Lef} _ {x} \left(\widetilde {\Gamma} \times \delta^ {n}\right) = \operatorname{Lef} _ {x} \left(\widetilde {\Gamma} \times \widetilde {\delta} ^ {n}\right) + \sum_ {J \neq \emptyset} \operatorname{Lef} _ {x} \left(\widetilde {\Gamma} \times \widetilde {\delta} _ {J} ^ {n}\right).\tag{4}
$$

De la même façon, pour toute partie non vide I de$\{ 1 , \ldots , m \}$, on a l’egalit´ e :´

$$
\operatorname{Lef} _ {x} \left(\widetilde {\Gamma} _ {I} \times \delta_ {I} ^ {n}\right) = \sum_ {J \supseteq I} \operatorname{Lef} _ {x} \left(\widetilde {\Gamma} \times \widetilde {\delta} _ {J} ^ {n}\right).\tag{5) \( _{I} \}
$$

Etant donnee la manière dont chaque correspondance cohomologique´$\widetilde \Gamma _ { I }$a et´ e d´ efinie dans la proposition IV.9 à partir de´$\widetilde \Gamma .$, cela resulte des deux faits´ suivants :

• D’après le lemme IV.2, l’image reciproque de´$\delta _ { I } ^ { n } : \overline { { \mathfrak { X } } } _ { I } ^ { y } \to \overline { { \mathfrak { X } } } _ { I } ^ { x } \times _ { s } \overline { { \mathfrak { X } } } _ { I } ^ { y } \hookrightarrow Z ^ { x }$ via$\widetilde { Z } ^ { x } \longrightarrow Z ^ { x }$ou$E _ { I } ^ { x } \longrightarrow \overline { { \mathfrak { X } } } _ { I } ^ { x } \times _ { s } \overline { { \mathfrak { X } } } _ { I } ^ { y }$est la reunion sch´ ematique des´ $\widetilde { \delta } _ { J } ^ { n }$avec$J \supseteq I$

• Pour toute partie$J \supseteq I$, le plongement$\widetilde { \delta } _ { J } ^ { n } : \widetilde { \mathfrak { X } } _ { J } ^ { y , \mathrm { g r } } \hookrightarrow \widetilde { Z } ^ { \mathrm { g r } , x }$se factorise en${ \widetilde { \mathfrak { X } } _ { J } ^ { y , \mathrm { g r } } } \hookrightarrow E _ { J } ^ { \mathrm { g r } , x } \to \widetilde { Z } ^ { \mathrm { g r } , x }$ et l’isomorphisme sur$\widetilde { \mathfrak { X } } _ { J } ^ { y , \mathrm { g r } }$

$$
\mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\longrightarrow}} \left(\widetilde {\delta} _ {J} ^ {n}\right) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ]
$$

est le compose de l’isomorphisme´

$$
\mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\longrightarrow}} \left(i _ {\widetilde {\mathfrak {X}} _ {J} ^ {y, \mathrm{gr}}}\right) ^ {!} \mathbb {Q} _ {\ell} (d - | J |) [ 2 d - 2 | J | ]
$$

et du transforme par´$( i _ { \widetilde { \mathfrak { X } } _ { J } ^ { y , \mathrm { g r } } } ^ { E _ { J } ^ { \mathrm { g r } , x } } ) ^ { ! }$de l’isomorphisme sur$E _ { J } ^ { \mathrm { g r } , x }$

$$
\mathbb {Q} _ {\ell} (d - | J |) [ 2 d - 2 | J | ] \stackrel {{\sim}} {{\longrightarrow}} \left(i \frac {\widetilde {Z} ^ {\mathrm{gr} , x}}{E _ {J} ^ {\mathrm{gr} , x}}\right) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ].
$$

En formant la somme alternee de (4) et des´ egalit´ es´$( 5 ) _ { I }$, on obtient l’identite (1) cherch´ ee.´

(ii) La conclusion de la proposition IV.5 etant v´ erifi´ ee par hypothèse, la´ correspondance$\widetilde { \Gamma } ^ { \mathrm { g r } }$et le graphe${ \widetilde { \delta } } ^ { n } : { \mathfrak { X } } ^ { \mathrm { g r } , y } \to { \widetilde { Z } } ^ { \mathrm { g r } , x }$ne se rencontrent pas en dehors de l’ouvert$\mathfrak { X } _ { \varnothing } ^ { \mathrm { g r } } \times \mathbf { \check { x } } _ { \varnothing } ^ { \mathrm { g r } }$

Dans l’ouvert$\mathfrak { X } _ { \varnothing } \times _ { \varphi , S } \mathfrak { X } _ { \varnothing } = Z _ { \varnothing }$, la trace$\Gamma _ { \emptyset }$de la correspondance Γ est etale sur´$\mathfrak { X } _ { \varnothing }$via la première projection$p _ { \Gamma _ { \emptyset } } ^ { \prime }$donc elle est lisse sur S.

La correspondance cohomologique

$$
\mathbb {Q} _ {\ell} = p _ {\Gamma_ {\emptyset} ^ {\mathrm{gr}}} ^ {\prime \prime *} \mathbb {Q} _ {\ell} \longrightarrow p _ {\Gamma_ {\emptyset} ^ {\mathrm{gr}}} ^ {\prime !} \mathbb {Q} _ {\ell} \cong \left(i _ {\Gamma_ {\emptyset} ^ {\mathrm{gr}}} ^ {Z _ {\emptyset} ^ {\mathrm{gr}}}\right) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ]
$$

ainsi que l’isomorphisme

$$
\mathbb {Q} _ {\ell} \stackrel {{\sim}} {{\longrightarrow}} (\delta^ {n}) ^ {!} \mathbb {Q} _ {\ell} \cong \big (i _ {\mathfrak {X} _ {\emptyset} ^ {\mathrm{gr}, y}} ^ {Z _ {\emptyset} ^ {\mathrm{gr}, x}} \big) ^ {!} \mathbb {Q} _ {\ell} (d) [ 2 d ]
$$

correspondent aux sections cl$( \Gamma _ { \emptyset } )$et cl$( \delta ^ { n } )$des faisceaux de cohomologie à supports$\mathcal { H } _ { | \Gamma _ { \varnothing } | } ^ { 2 d } \mathbb { Q } _ { \ell } ( d )$et$\mathcal { H } _ { | \mathfrak { X } ^ { \mathrm { g r } , \mathfrak { y } } | } ^ { 2 d } \mathbb { Q } _ { \ell } ( d )$qui sont associees à´$\Gamma _ { \emptyset } \to \mathfrak { X } _ { \emptyset } \times _ { \varphi , S } \mathfrak { X } _ { \emptyset }$ $\mathit { \Theta } = \mathit { Z } _ { \varnothing }$et à$\delta ^ { n } : \mathfrak { X } _ { \varnothing } ^ { y } \to \mathfrak { X } _ { \varnothing } ^ { x } \times _ { s } \mathfrak { X } _ { \varnothing } ^ { y } = Z _ { \varnothing } ^ { x }$d’après le paragraphe 2a de l’appendice A.

Le nombre d’intersection$\mathrm { L e f } _ { x } ( \widetilde { \Gamma } \times \widetilde { \delta } ^ { n } )$est defini en composant leur´  produit “cup” avec l’homomorphisme de trace sur$Z _ { \varnothing } ^ { \mathrm { g r } , x }$induit par$Z _ { \varnothing }$. Par consequent, on a´

$$
\operatorname{Lef} _ {x} (\widetilde {\Gamma} \times \widetilde {\delta} ^ {n}) = x ^ {*} (\operatorname{cl} (\Gamma_ {\emptyset})) \cdot \operatorname{cl} (\delta^ {n}).
$$

Enfin, le calcul de l’intersection$x ^ { * } ( \operatorname { c l } ( \Gamma _ { \varnothing } ) ) \cdot \operatorname { c l } ( \delta ^ { n } )$s’effectue localement (pour la topologie etale) au voisinage de chacun des points d’intersection´ dans le champ$Z _ { \varnothing } = { \mathfrak { X } } _ { \varnothing } \times _ { \varphi , S } { \mathfrak { X } } _ { \varnothing }$. Comme$\mathfrak { X } _ { \varnothing }$est algebrique au sens de´ Deligne-Mumford et lisse, on est ramene au cas classique d’une intersection´ transversale dans un schema lisse et on conclut´

$$
\operatorname{Lef} _ {x} \left(\widetilde {\Gamma} \times \widetilde {\delta} ^ {n}\right) = x ^ {*} \left(\operatorname{cl} \left(\Gamma_ {\emptyset}\right)\right) \cdot \operatorname{cl} \left(\delta^ {n}\right) = \operatorname{Lef} _ {x} \left(\Gamma_ {\emptyset} \times \operatorname{Frob} ^ {n}\right).
$$

Nous pouvons maintenant gen´ eraliser le r´ esultat du th´ eorème IV.7 au´ cas où le champ serein X n’est pas necessairement propre sur´$S$:

Theor´ eme IV.12.\` – Soit Γ une correspondance geom´ etrique dans le champ´ lisse (mais non necessairement propre´ ) X au-dessus de l’endomorphisme ϕ de S (suppose propre´ ). Ainsi la seconde projection$p _ { \Gamma } ^ { \prime \prime } : \Gamma \to \mathfrak { X }$est-elle propre. On suppose de plus que :

• l’espace de modules grossier${ \mathfrak { X } } ^ { \mathrm { g r } }$de X se plonge comme ouvert dense dans un espace algebrique´$\overline { { { \mathfrak { X } } } } ^ { \mathrm { g r } }$propre sur S qui devient en schema au´ moins après extension finie du corps de base$\mathbb { F } _ { q }$;

• l’ouvert$\mathfrak { X } _ { \varnothing }$de X est un champ algebrique au sens de Deligne-Mumford ;´ • au-dessus d’un ouvert$S ^ { \prime }$de S, la correspondance Γ stabilise l’ouvert $\mathfrak { X } _ { \varnothing }$de X “au voisinage de ses points fixes” et la première projection

$$
p _ {\Gamma_ {\emptyset}} ^ {\prime}: \Gamma_ {\emptyset} \to \mathfrak {X} _ {\emptyset}
$$

de sa trace$\Gamma _ { \emptyset }$sur$\mathfrak { X } _ { \varnothing } \times _ { \varphi , S } \mathfrak { X } _ { \varnothing } y$est etale.´

Alors, considerant l’homomorphisme induit par la correspondance´ Γ

$$
\varphi^ {*} (p _ {\mathfrak {X}})! \mathbb {Q} _ {\ell} \xrightarrow {\Gamma_ {*}} (p _ {\mathfrak {X}})! \mathbb {Q} _ {\ell},
$$

il existe des homomorphismes en cohomologie

$$
\varphi^ {*} (p _ {\overline {{\mathfrak {X}}} _ {I}})! \mathbb {Q} _ {\ell} \xrightarrow {(\Gamma_ {I}) _ {*}} (p _ {\overline {{\mathfrak {X}}} _ {I}})! \mathbb {Q} _ {\ell}, \quad I \neq \emptyset ,
$$

et un entier$n _ { 0 } > 0$tels que pour tout pointferme´$x : s \hookrightarrow S ^ { \prime }$et tout entier $n \geq n _ { 0 }$avec$y = \varphi$◦ x et$\operatorname { F r o b } ^ { n } \circ y = x ,$, on ait

$$
\begin{array}{l} \operatorname{Lef} _ {x} \left(\Gamma_ {\emptyset} \times \operatorname{Frob} ^ {n}\right) = \operatorname{Tr} \left(\Gamma_ {*} ^ {x} \times \operatorname{Frob} ^ {n}, (p _ {\mathfrak {X} ^ {x}}) _ {!} \mathbb {Q} _ {\ell}\right) \\ \qquad + \sum_ {I \neq \emptyset} (- 1) ^ {| I |} \operatorname{Tr} \left((\Gamma_ {I}) _ {*} ^ {x} \times \operatorname{Frob} ^ {n}, (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {x}}) _ {!} \mathbb {Q} _ {\ell}\right). \end{array}
$$

Demonstration :´ Il existe un entier$n _ { 0 } > 0$tel que la correspondance$\Gamma ^ { \prime }$sur $\varphi ^ { \prime } = \varphi \circ { \mathrm { F r o b } } ^ { n _ { 0 } }$transformee de´ Γ par Fro$\mathsf { \Omega } \mathsf { J } ^ { n _ { 0 } } \times \hat { \mathrm { I d } } : \mathfrak { X } \times \mathfrak { X } \overset { \cdot } {  } \mathfrak { X } \times \mathfrak { X }$verifie´ les conclusions du lemme IV.10 et de la proposition IV.5.

D’après le theorème IV.11, les homomorphismes en cohomologie´

$$
\varphi^ {\prime *} (p _ {\overline {{\mathfrak {X}}} _ {I}})! \mathbb {Q} _ {\ell} \xrightarrow {(\widetilde {\Gamma} _ {I} ^ {\prime}) _ {*}} (p _ {\overline {{\mathfrak {X}}} _ {I}})! \mathbb {Q} _ {\ell}, \quad I \neq \emptyset ,
$$

verifient pour tout´ x et$n \geq n _ { 0 }$comme dans l’enonc´ e´

$$
\begin{array}{l} \operatorname{Lef} _ {x} \left(\Gamma_ {\emptyset} ^ {\prime} \times \operatorname{Frob} ^ {n - n _ {0}}\right) = \operatorname{Tr} \left(\Gamma_ {*} ^ {\prime x} \times \operatorname{Frob} ^ {n - n _ {0}}, (p _ {\mathfrak {X} ^ {x}}) _ {!} \mathbb {Q} _ {\ell}\right) \\ \qquad + \sum_ {I \neq \emptyset} (- 1) ^ {| I |} \operatorname{Tr} \left(\left(\widetilde {\Gamma} _ {I} ^ {\prime}\right) _ {*} ^ {x} \times \operatorname{Frob} ^ {n - n _ {0}}, \left(p _ {\overline {{\mathfrak {X}}} _ {I} ^ {x}}\right) _ {!} \mathbb {Q} _ {\ell}\right). \end{array}
$$

Or on a evidemment´

$$
\operatorname{Lef} _ {x} \left(\Gamma_ {\emptyset} ^ {\prime} \times \operatorname{Frob} ^ {n - n _ {0}}\right) = \operatorname{Lef} _ {x} \left(\Gamma_ {\emptyset} \times \operatorname{Frob} ^ {n}\right)
$$

et

$$
\operatorname{Tr} \left(\Gamma_ {*} ^ {\prime x} \times \operatorname{Frob} ^ {n - n _ {0}}, (p _ {\mathfrak {X} ^ {x}})! \mathbb {Q} _ {\ell}\right) = \operatorname{Tr} \left(\Gamma_ {*} ^ {x} \times \operatorname{Frob} ^ {n}, (p _ {\mathfrak {X} ^ {x}})! \mathbb {Q} _ {\ell}\right).
$$

Les homomorphismes$( \Gamma _ { I } ) _ { * }$definis comme compos´ es des´

$$
(\mathrm{Frob} ^ {n _ {0}}) ^ {*} \varphi^ {*} (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {x}})! \mathbb {Q} _ {\ell} \xrightarrow {(\widetilde {\Gamma} _ {I} ^ {\prime}) _ {*}} (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {x}})! \mathbb {Q} _ {\ell}
$$

et des isomorphismes reciproques des´

$$
(\operatorname{Frob} ^ {n _ {0}}) ^ {*} \varphi^ {*} (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {x}})! \mathbb {Q} _ {\ell} \xrightarrow {\underset {\sim} {\operatorname{Frob} ^ {n _ {0}}}} \varphi^ {*} (p _ {\overline {{\mathfrak {X}}} _ {I} ^ {x}})! \mathbb {Q} _ {\ell}
$$

repondent à la question pos´ ee.´

## Chapitre V

## Stabilisation des correspondances de Hecke

On a rappele au chapitre I que pour tout niveau´ N le champ$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb Z }$audessus de$( X - N ) \times ( X - N )$est muni d’une action par correspondances de l’algèbre de Hecke$\mathcal { H } _ { N } ^ { r }$de niveau N (et aussi des deux endomorphismes de Frobenius partiels$\mathrm { F r o b } _ { \infty }$et Frob au-dessus de$\Lambda _ { X - N } ~ = ~ \Lambda ~ \times _ { X \times X }$ $( X - N ) \times ( \bar { X ^ { } } - N )$. Mais comme$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb Z }$n’est pas de type fini et que ses espaces de cohomologie sont de dimension infinie, on a et´ e amen´ e à´ definir dans´$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb Z }$des ouverts de type fini$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$. Ce faisant, on a perdu l’action des correspondances de Hecke (et des endomorphismes de Frobenius partiels) : elles sont bien definies g´ en´ eriquement dans les´ $\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$mais elle ne les stabilisent pas et les nombres de points fixes $\mathrm { L e f } _ { \overline { { \infty } } , \overline { { 0 } } } ^ { r , \overline { { p } } \leq p } ( f \times \mathrm { F r o b } _ { \infty } ^ { \deg ( \infty ) s ^ { \prime } } \times \mathrm { F r o b } _ { 0 } ^ { \deg ( 0 ) u ^ { \prime } } )$qu’on a calcules dans ces ouverts´ sont a priori depourvus de sens cohomologique.´

La stabilisation des correspondances de Hecke se fait en deux temps.

Le premier consiste à retrouver des correspondances geom´ etriques qui´ agissent sur la cohomologie -adique à supports compacts de champs sereins plus gros que les$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$. Quand il$\boldsymbol { \mathrm { n ^ { \prime } y } }$a pas de niveau, il suffit d’etendre les correspondances de Hecke par normalisation au-´ dessus des carres´$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } } \times \overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$car les$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$sont à la fois propres et lisses sur$X \times X$. On procède de même dans les$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z }$dans le cas de niveaux N tels que$\mathcal { C } _ { N } ^ { r }$admette une resolution des singularit´ es´$\widetilde { \mathcal { C } } _ { N } ^ { r }$ (par exemple si$\ l { N } \mathrm { ~ n ~ a ~ }$pas de multiplicites ou si´$r = 2 )$. Pour un niveau$\ddot { N }$ arbitraire, on verifie dans ce chapitre que les correspondances g´ eom´ etriques´ definies par normalisation dans les´$\overline { { { \mathrm { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$stabilisent les ouverts lisses $\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } } / a ^ { \mathbb Z }$ce qui implique qu’elles induisent des endomorphismes de leur cohomologie.

Le second temps consiste à verifier que ces nouvelles correspondances´ dans les${ \mathrm { C h t } } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } , { \mathrm { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$ou$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } } } } / a ^ { \mathbb Z }$stabilisent les ouverts $\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z }$au voisinage de leurs points fixes, de façon à pouvoir appliquer les resultats du chapitre IV et à donner un sens cohomologique aux´ nombres de points fixes dans ces ouverts.

On montre aussi que les espaces algebriques grossiers associ´ es aux´ champs sereins$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb Z }$deviennent des schemas au moins après exten-´ sion finie du corps de base$\mathbb { F } _ { q }$. Cela permet d’appliquer aux$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } } } } / a ^ { \mathbb { Z } }$le theorème de Fujiwara sur la conjecture de Deligne qui est l’un d´ es principaux ingredients de la formule du chapitre IV dans le cas non propre.´

Dans tout ce chapitre, on fixe encore une fois la courbe X projective, lisse et geom´ etriquement connexe sur le corps fini de base´$\mathbb { F } _ { q }$à$q$el´ ements.´

## 1) Propriet´ es des espaces classifiants de chtoucas it´ er´ es´

## a) Verification de ce que les champs de chtoucas it´ er´ es sont sereins´

Pour tout niveau$N = \operatorname { S p e c } { \mathcal { O } } _ { N } \hookrightarrow X$, tout degre´$d \in \mathbb { Z }$et tout polygone de troncature$p : [ 0 , r ] \to \mathbb { R } _ { + }$assez convexe en fonction de X et N, on a construit au chapitre III des compactifications$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p }$. Ce sont des champs algebriques au sens d’Artin, de type fini, contenant´$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p }$ comme ouvert dense et munis d’un morphisme

$$
\overline {{\mathrm{Cht} _ {N} ^ {r , d , \overline {{p}} \leq p}}} \to (X - N) \times (X - N)
$$

qui est propre au sens qu’il verifie le critère valuatif de propret ´ e. Si ´$N = \emptyset$ [resp.$\bar { N } \neq \varnothing ]$, ce morphisme se relève en un morphisme lisse

$$
\overline {{\operatorname{Cht} ^ {r , d , \overline {{p}} \leq p}}} \rightarrow X \times X \times \left(\mathbb {A} ^ {1} / \mathbb {G} _ {m}\right) ^ {r - 1}
$$

[resp.

$$
\overline {{\operatorname{Cht} _ {N} ^ {r , d , \overline {{p}} \leq p}}} \rightarrow (X - N) \times (X - N) \times \mathcal {C} _ {N} ^ {r} ]
$$

où$\mathcal { C } _ { N } ^ { r }$est le champ algebrique au sens d’Artin qui est la normalisation de´ $\mathcal { C } ^ { r , N }$dans le revêtement etale´$\mathcal { C } _ { N , \emptyset } ^ { r }$de$\mathcal { C } _ { \varnothing } ^ { r , N }$. Quand$\mathcal { C } _ { N } ^ { r }$admet une resolution´ des singularites´$\widetilde { \mathcal { C } } _ { N } ^ { r }$(par exemple quand N n’a pas de multiplicites ou quand´ $r = 2 ) , \mathrm { C h t } _ { N } ^ { r , \overline { { d } } , \overline { { p } } \leq p } = \overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } } \times _ { \mathcal { C } _ { N } ^ { r } } \widetilde { \mathcal { C } } _ { N } ^ { r }$est une resolution des singularit´ es´ de$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$qui se trouve munie d’un morphisme lisse

$$
\widetilde {\operatorname{Cht} _ {N} ^ {r , d , \overline {{p}} \leq p}} \to (X - N) \times (X - N) \times \widetilde {\mathcal {A}} ^ {r, N} / \mathcal {A} _ {\emptyset} ^ {r, N}
$$

avec$\widetilde { \mathcal { A } } ^ { r , N } / \mathcal { A } _ { \varnothing } ^ { r , N }$le champ torique quotient d’une variet´ e torique lisse´$\displaystyle \widetilde { \mathcal { A } } ^ { r , N }$ par son tore$\mathcal { A } _ { \varnothing } ^ { r , N }$

Afin de pouvoir appliquer les resultats du chapitre IV à des correspon-´ dances dans les$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$(ou les$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z }$quand ils existent) audessus de$( X - N ) \stackrel { \vartriangle } { \times } ( X - N )$, il nous faut d’abord verifier :´

Proposition V.1. – Pour tout niveau$N \hookrightarrow X$, tout degre d´$\in \ \mathbb { Z }$et tout polygone de troncature$p : [ 0 , r ] \to \mathbb { R } _ { + }$assez convexe en fonction de X et N, le champ algebrique´$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } } ( o u \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } )$au-dessus de$( X - N )$ $\times \left( X - N \right)$est serein au sens de la definition´ A.1.

Demonstration :´ Par construction, chaque$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$(ou$\mathbf { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } )$est representable projectif au-dessus de´$\mathsf { C h t } ^ { r , d , \overline { { p } } \leq p } \times _ { X \times X } ( X - N ) \times ( X - N )$ Il suffit donc de verifier que les champs de chtoucas it´ er´ es´$\overline { { \mathrm { C h t } ^ { r , d , \overline { { { p } } } \leq p } } }$sur $X \times X$sont sereins. On sait dejà qu’ils sont de type fini et s´ epar´ es puisque´ propres. Reste à verifier la propri´ et´ e (S3) pour un´$\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } } } = \mathfrak { X }$fixe.´

Si$N = \operatorname { S p e c } { \mathcal { O } } _ { N } \hookrightarrow X$est un niveau non vide, notons ici$\mathfrak { X } ^ { N }$l’ouvert de${ \mathfrak { X } } = \mathrm { C h t } ^ { r , d , { \overline { { p } } } \leq p }$defini en demandant que pôle, z´ ero et d´ eg´ en´ erateurs´ evitent ´ N. D’après le lemme III.13,$\mathfrak { X } ^ { N }$est l’image reciproque par le mor-´ phisme de restriction des chtoucas iter´ es de´ X à N

$$
\overline {{\mathrm{Cht} ^ {r , d , \overline {{p}} \leq p}}} \times_ {X \times X} (X - N) \times (X - N) \xrightarrow {\cdot \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N}} \mathcal {C} ^ {r, N}
$$

de l’ouvert$\mathcal { C } ^ { \prime r , N }$de$\mathcal { C } ^ { r , N }$. Et d’après la proposition III.11, l’ouvert$\mathcal { C } _ { N } ^ { \prime r }$de $\mathcal { C } _ { N } ^ { r }$est un revêtement fini plat de$\mathcal { C } ^ { \prime r , N }$sur les fibres duquel le groupe fini ${ \dot { \mathrm { { G L } } } } _ { r } ( { \mathcal { O } } _ { N } )$agit transitivement.

Par consequent,´$\mathfrak { X } _ { N } \ = \ \mathfrak { X } ^ { N } \times _ { \mathcal { C } ^ { \prime r , N } } \ \mathfrak { C } _ { N } ^ { \prime r } \ = \ \overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \le p ^ { \prime } } } }$est un champ algebrique repr´ esentable, fini et plat sur´$\mathfrak { X } ^ { N }$et il est muni d’une action du groupe fini${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N } )$qui est transitive sur ses fibres. Si le degre de´ N est assez grand en fonction du polygone de troncature$p ,$, le champ$\mathfrak { X } _ { N }$n’a pas d’automorphismes et d’après le corollaire 8.1.1 de [Laumon, Moret-Bailly] ${ \mathrm { c } } ^ { \prime }$est un espace algebrique.´

Quand on fait varier le support de N, les ouverts$\mathfrak { X } ^ { N }$recouvrent${ \mathfrak { X } } =$ $\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \le p } } }$et ceci achève de prouver que le champ algebrique´$\overline { { \mathrm { C h t } ^ { r , d , \overline { { { p } } } \leq p } } }$est serein.!"

Si${ \textit { a } } \in  { \mathbb { A } } ^ { \times }$est un idèle de degre non nul, les´$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb Z } \cong$ $\begin{array} { r l } { \mathrm { ~ U ~ } } & { { } \overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } } } \end{array}$(ou les$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \le p } / a ^ { \mathbb Z } \cong \qquad \big [ \big [ \mathrm { ~ \quad ~ C h t } _ { N } ^ { r , d , \overline { { p } } \le p } \big )$sont $1 { \leq } d { \leq } r | \deg ( a ) |$$1 { \leq } d { \leq } r | \deg ( a ) |$ egalement des champs sereins.´

## b) Schematisation des espaces de modules grossiers´

La suite du present paragraphe 1 est consacr´ ee à la d´ emonstration du´ theorème suivant qui permet d’appliquer aux espaces de module´ s grossiers des$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$la conjecture de Deligne demontr´ ee par Fujiwara pour les´ schemas :´

Theor´ eme V.2.\` – Pour tout polygone de troncature p (assez convexe en fonction de X), tout degre d´$\in \mathbb { Z }$et tout niveau$N \hookrightarrow X$, l’espace algebrique´ grossier associe au champ serein´$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$devient un schema au moins´ après changement du corps de base$\mathbb { F } _ { q }$en une extension finie.!"

Procedons à une première r´ eduction :´

Lemme V.3. –Afin deprouver le theorème´ V.2 ci-dessus, il suffit de montrer qu’etant donn ´ e un polygone de troncature p ´ (assez convexe en fonction de X), alorspour tout entier d assez grand et tout niveau$N = \operatorname { S p e c } \mathcal { O } _ { N } \hookrightarrow X$ de degre assez grand et sans multiplicit´ es, l’espace alg´ ebrique´

$$
\overline {{\operatorname{Cht} _ {N} ^ {r , d , \overline {{p}} \leq p}}} ^ {\prime} \times_ {\left(\mathbb {A} ^ {r - 1} / \mathbb {G} _ {m} ^ {r - 1}\right)} \mathbb {A} ^ {r - 1}
$$

est un schema quasi-projectif où l’action de´$\mathbb { G } _ { m } ^ { r - 1 }$se relève à unfibre ample.´

Demonstration :´ Les morphismes d’oubli du niveau

$$
\overline {{\operatorname{Cht} _ {N} ^ {r , d , \overline {{p}} \leq p}}} \rightarrow \overline {{\operatorname{Cht} ^ {r , d , \overline {{p}} \leq p}}} \times_ {X \times X} (X - N) \times (X - N)
$$

sont representables finis ; d’après le th´ eorème A.2 de [Laumon, Moret-´ Bailly], il suffit donc de prouver que les espaces de modules grossiers ${ \mathfrak { X } } ^ { \mathrm { g r } }$associes aux champs´${ \mathfrak { X } } = { \overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } } } } } \leq p$deviennent des schemas après´ extension finie du corps de base. Comme on peut faire agir$a ^ { \mathbb { Z } }$, il suffit de le faire quand d est assez grand.

La propriet´ e d’être un sch´ ema est locale et on peut remplacer´ X par les ouverts$\mathfrak { X } ^ { \hat { N } }$definis en demandant que pôle, z´ ero et d´ eg´ en´ erateurs´ evitent´ N, pour$N = \operatorname { S p e c } { \mathcal { O } } _ { N } \hookrightarrow X$des niveaux reduits de degr´ es assez grands.´

On a un triangle commutatif

![](images/page_115_image_9.jpg)

où la flèche horizontale est representable, finie et plate et munie de l’action´ transitive sur les fibres du groupe fini${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N } )$

Supposons que l’on sache que

$$
\overline {{\operatorname{Cht} _ {N} ^ {r , d , \overline {{p}} \leq p}}} ^ {\prime} \times_ {\left(\mathbb {A} ^ {r - 1} / \mathbb {G} _ {m} ^ {r - 1}\right)} \mathbb {A} ^ {r - 1}
$$

est un schema quasi-projectif où l’action de´$\mathbb { G } _ { m } ^ { r - 1 }$se relève à un fibre ample.´ Alors il en est de même de son quotient$\widetilde { \mathfrak { X } } ^ { N , \mathrm { g r } }$par l’action du groupe fini ${ \mathrm { G L } } _ { r } ( { \mathcal { O } } _ { N } )$

Le quotient de$\widetilde { \mathfrak { X } } ^ { N , \mathrm { g r } }$par l’action de$\mathbb { G } _ { m } ^ { r - 1 }$s’identifie à l’espace algebrique´ grossier$\mathfrak { X } ^ { N , \mathrm { g r } }$associe au champ serein´$\dot { \mathfrak { X } } ^ { N }$. D’après le theorème 1.1 de´ [Mumford, Fogarty], on est reduit à montrer qu’au moins après extension´ finie du corps de base tout point de$\widetilde { \mathfrak { X } } ^ { N , \mathrm { g r } }$admet un voisinage affine stabilise´ par$\mathbb { G } _ { m } ^ { r - 1 }$et ceci resulte du lemme g´ en´ eral suivant :´

Lemme V.4. – Soit U un schema quasi-projectif sur un corps´$\mathbb { F }$et muni de l’action d’un tore T qui se relève à un fibre ample.´

Alors, quitte à remplacer le corps de base F par une extensionfinie, tout point de U admet un voisinage ouvert affine stabilise par T.´

Demonstration :´ On peut supposer que U est plonge comme sous-sch´ ema´ localement ferme dans un espace projectif´ P sur lequel T agit. On note$\overline { U }$ l’adherence de´ U dans$\mathbb { P }$et$\partial U = \overline { { U } } - U$son bord.

Pour tout point u de U, il existe un polynôme homogène P qui est nul sur ∂U mais ne${ \mathrm { s } } ^ { \prime }$annule pas en u. Quitte à remplacer$\mathbb { F }$par une extension finie, on peut ecrire´

$$
P = P _ {1} + \dots + P _ {k}
$$

où$P _ { 1 } , \ldots , P _ { k }$sont des polynômes homogènes sur lesquels T agit par des caractères deux à deux distincts. Comme ces caractères sont lineairement´ independants, que´$P$est nul sur ∂U et que ∂U est stabilise par´$T$, tous les $P _ { 1 } , \ldots , P _ { k }$sont nuls sur ∂U. Mais l’un des$P _ { i }$au moins ne${ \mathrm { s } } ^ { \prime }$annule pas au point u et alors

$$
U \cap \{P _ {i} \neq 0 \} = \overline {{U}} \cap \{P _ {i} \neq 0 \}
$$

est un voisinage ouvert affine de u dans U qui est stabilise par´$T .$!"

## c) Recours à la theorie de stabilit´ e de Mumford et Seshadri´

A partir de maintenant, on fixe un polygone de troncature$p : [ 0 , r ] \to \mathbb { R } _ { + }$ (assez convexe en fonction de X), un niveau$N = \operatorname { S p e c } { \mathcal { O } } _ { N } \hookrightarrow X$reduit et´ de degre assez grand en fonction de´ p et un degre´ d assez grand en fonction de X, p et N. On doit montrer la propriet´ e du lemme V.3.´

Cherchant à se rapprocher des fibres, on note´$\overline { { \mathrm { V e c } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$le champ algebrique au sens d’Artin qui à tout sch´ ema´ S sur$\mathbb { F } _ { q }$associe le groupoïde des familles constituees de´

• un fibre´ E localement libre de rang r sur$X \times S$dont la restriction audessus de tout point geom´ etrique de´ S est de degre´ d et de polygone canonique$\le p$

• des fonctions$\ell _ { 1 } , \ldots , \ell _ { r - 1 }$partout definies sur´ S,

• un homomorphisme complet

$$
\mathcal {E} \otimes_ {\mathcal {O} _ {X \times S}} \mathcal {O} _ {N \times S} = \mathcal {E} _ {N} \Rightarrow \mathcal {O} _ {N \times S} ^ {r}
$$

dont l’image dans$( \mathbb { A } ^ { 1 } / ( \mathbb { G } _ { m } ) ^ { r - 1 } ( N \times S ) \exp { ( ( \mathscr { O } _ { N \times S } , \ell _ { 1 } ) , \dots , ( \mathscr { O } _ { N \times S } , \ell _ { r - 1 } ) ) } )$

On rappelle qu’un tel homomorphisme complet consiste en une famille d’homomorphismes lineaires partout non nuls´

$$
v _ {s}: \Lambda^ {s} \mathfrak {E} _ {N} \to \Lambda^ {s} \left(\mathcal {O} _ {N \times S} ^ {r}\right), \quad 1 \leq s \leq r,
$$

qui verifient en particulier les relations´

$$
v _ {s} = \left(\prod_ {t <   s} \ell_ {t} ^ {s - t}\right) \cdot \Lambda^ {s} v _ {1}, \quad 1 \leq s \leq r.
$$

Le champ algebrique´$\overline { { \mathrm { V e c } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$est muni d’un morphisme sur$\mathbb { A } ^ { r - 1 }$et il est de type fini.

Comme le polygone de troncature p a et´ e choisi assez convexe en fonc-´ tion de X, le polygone canonique de Harder-Narasimhan du fibre sous-jacent´ E à tout point$\widetilde { \mathcal { E } } = ( \mathcal { E } \hookrightarrow \mathcal { E } ^ { \prime } \hookleftarrow \mathcal { E } ^ { \prime \prime } \Leftarrow \ ^ { \tau } \mathcal { E } )$de$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } }$est majore par´$p .$ On a un diagramme commutatif

![](images/page_117_image_3.jpg)

où la flèche horizontale est un morphisme representable et quasi-projectif.´

On est donc reduit à :´

Lemme V.5. – Afin de montrer la propriet´ e du lemme´ V.3 et donc le theorème´ V.2, il suffit de prouver que dans les conditions ci-dessus, le morphisme

$$
\overline {{\operatorname{Cht} _ {N} ^ {r , d , \overline {{p}} \leq p}}} ^ {\prime} \times_ {\left(\mathbb {A} ^ {r - 1} / \mathbb {G} _ {m} ^ {r - 1}\right)} \mathbb {A} ^ {r - 1} \to \overline {{\operatorname{Vec} _ {N} ^ {r , d , \overline {{p}} \leq p}}}
$$

se factorise à travers un ouvert de$\mathrm { V e c } _ { N } ^ { r , d , \overline { { p } } \leq p }$qui est representable par un´ schema quasi-projectif.´!"

On va construire un tel ouvert quasi-projectif dans$\overline { { \mathrm { V e c } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$en recourant à la theorie des invariants g´ eom´ etriques de Mumford, à la manière´ de Seshadri pour les espaces de modules de fibres stables.´

On note$\overline { { X } }$la courbe deduite de´ X par changement du corps de base$\mathbb { F } _ { q }$ en une clôture algebrique´$\overline { { \mathbb { F } } } _ { q }$. On commence par :

Lemme V.6. – Fixons un polygone de troncature p et un entier$k _ { 0 }$. Il existe un entier$d _ { 0 }$tel que toutfibre´ E de rang r sur${ \overline { { X } } } ,$, de degre´ deg$( \mathcal { E } ) = d \geq d _ { 0 }$ et de polygone canonique$\le p$verifie :´

(i) On a$H ^ { 1 } ( \overline { { X } } , \mathcal { E } ) = 0 e t$E est engendre par ses sections globales.´

(ii) Pour tout sous-fibre non nul´ F de E de rang$s \leq r$et dont le degre´ verifie ´

$$
\deg (\mathcal {F}) \geq k _ {0} + \frac {s}{r} d,
$$

le polygone canonique de$\mathcal { F }$et deg$\textstyle ( { \mathcal { F } } ) - { \frac { s } { r } } d$sont bornes par des´ constantes qui ne dependent que de p et k´

(iii) Sous les hypothèses de (ii), on a$H ^ { 1 } ( { \overline { { X } } } , { \mathcal { F } } ) = 0$et F est engendre par´ ses sections globales.

Demonstration :´ (i) Par dualite de Serre,´$H ^ { 1 } ( { \overline { { X } } } , \mathcal { E } )$est nul si et seulement si il$\boldsymbol { \mathrm { n ^ { \prime } y } }$a pas d’homomorphisme non nul

$$
\mathcal {E} \longrightarrow \Omega_ {\overline {{X}}}.
$$

C’est automatique si le polygone canonique de$\mathcal { E }$est borne et son degr´ e´ est assez grand (en fonction du genre de$X )$

La seconde assertion provient de ce qu’on peut aussi imposer que pour tout point x de$\overline { { X } }$$H ^ { 1 } ( \overline { { X } } , \mathcal { E } ( - x ) ) = 0 .$

(ii) est evident sur les d´ efinitions.´

(iii) resulte de (i) et (ii).´

Le degre´ d ayant et´ e choisi très grand, il r´ esulte du lemme V.6(i) que si´ E est le fibre sous-jacent à un point de´$\mathrm { V e c } _ { N } ^ { r , d , \overline { { p } } \leq p }$, il est engendre par l’espace´ $H ^ { 0 } ( { \overline { { X } } } , \mathcal { E } )$de ses sections globales, lequel est de dimension$h = d + ( 1 - g ) r$ (où g designe le genre de la courbe´$X )$

Notant simplement$\mathcal { V } = \mathrm { V e c } _ { N } ^ { r , d , \overline { { p } } \leq p }$, soit$\widetilde { \mathcal { V } }$le champ sur V qui represente´ le choix (modulo l’action de$\mathbb { G } _ { m } )$d’un homomorphisme surjectif

$$
\mathcal {O} _ {X \times S} ^ {h} \longrightarrow \mathcal {E}
$$

qui, en la fibre au-dessus de chaque point geom´ etrique de ´ S, induit un isomorphisme

$$
H ^ {0} \big (\overline {{X}}, \mathcal {O} _ {\overline {{X}}} ^ {h} \big) \stackrel {{\sim}} {{\longrightarrow}} H ^ {0} (\overline {{X}}, \mathcal {E}).
$$

Le champ$\widetilde { \mathcal { V } }$est un torseur au-dessus de V sous le groupe$\mathrm { P G L } _ { h }$et il resulte de la construction par Grothendieck des “sch´ emas de Hilbert” que´ $\widetilde { \mathcal { V } }$est un schema quasi-projectif.´

Bien sûr, nous allons rechercher un ouvert de V dont l’image reciproque´ dans$\widetilde { \mathcal { V } }$soit constituee de points stables (au sens de Mumford) pour´$\mathrm { \Delta } \hat { \Gamma }$action de$\mathrm { P G L } _ { h }$

On choisit un autre sous-schema ferm´ e r´ eduit´$M \hookrightarrow X$qui evite´ N et dont le degre est très grand. On notera habituellement´ m et n les points geom´ etriques de´ M et N ; ils sont en nombres egaux aux degr´ es´$| M | , | N |$ de M et N.

Pour m$\in M , n \in N$, on note$E _ { m } , E _ { n }$les espaces vectoriels canoniques de dimension h sur les corps residuels de´ m, n. On note$\mathrm { G r } _ { m }$la grassmannienne des quotients de dimension r de$E _ { m }$

On a un morphisme canonique

$$
\widetilde {\mathcal {V}} \longrightarrow \prod_ {m \in M} \operatorname{Gr} _ {m} \hookrightarrow \prod_ {m \in M} \mathbb {P} \left(\Lambda^ {r} E _ {m} ^ {\vee}\right)
$$

et aussi

$$
\widetilde {\mathcal {V}} \longrightarrow \mathbb {P} \left(\bigoplus_ {1 \leq s \leq r} \bigoplus_ {n \in N} \operatorname{Hom} \left(\Lambda^ {s} E _ {n}, \Lambda^ {s} E _ {n} ^ {\prime}\right) ^ {\otimes (r! / s)}\right)
$$

si, pour$n \in N , E _ { n } ^ { \prime }$designe l’espace vectoriel canonique de dimension´ r sur le corps residuel de´$n .$.

On munira les$\mathbb { P } ( \Lambda ^ { r } E _ { m } ^ { \vee } )$d’une polarisation$\epsilon _ { M } \geq 1$et

$$
\mathbb{P}\left(\bigoplus_{\substack{1\leq s\leq r\\ n\in N}}\operatorname{Hom}\left(\Lambda^{s}E_{n},  \Lambda^{s}E^{\prime}_{n}\right)^{\otimes (r! / s)}\right)
$$

d’une polarisation$\epsilon _ { N } \geq 1$

d)$L e$critère numerique de stabilit´ e de Mumford´

Considerons un point g´ eom´ etrique´ V de$\widetilde { \mathcal { V } }$.

Il induit des points des$\mathrm { G r } _ { m } \hookrightarrow \mathbb { P } ( \Lambda ^ { r } E _ { m } ^ { \vee } )$qui sont des espaces quotients $E _ { m } \xrightarrow { \pi _ { m } } V _ { m }$de dimension r.

D’autre part, il induit un point de l’espace projectif

$$
\mathbb{P}\left(\bigoplus_{\substack{1\leq s\leq r\\ n\in N}}\operatorname{Hom}\left(\Lambda^{s}E_{n},  \Lambda^{s}E^{\prime}_{n}\right)^{\otimes (r! / s)}\right)
$$

qui est represent´ e par une famille d’homomorphismes non nuls´

$$
v = \left(v _ {n} ^ {s}: \Lambda^ {s} E _ {n} \to \Lambda^ {s} E _ {n} ^ {\prime}\right) _ {\stackrel {1 \leq s \leq r} {n \in N}}.
$$

On cherche des conditions sur V qui impliquent que pour tout sousgroupe à un paramètre

$$
c: \mathbb {G} _ {m} \to \mathrm{SL} _ {h},
$$

on ait avec les notations du paragraphe 2.1 de [Mumford, Fogarty]

$$
\mu (V, c) > 0.
$$

Pour un tel c, on a evidemment´

$$
\mu (V, c) = \epsilon_ {M} \sum_ {m \in M} \mu (V _ {m}, c) + \epsilon_ {N} \mu (v, c).
$$

L’espace canonique de dimension h admet une base$e _ { 1 } , \ldots , e _ { h }$dans laquelle$_ { c \mathrm { ~ s ~ } }$ecrit´

$$
c (t) e _ {j} = t ^ {n _ {j}} e _ {j}, \quad 1 \leq j \leq h,
$$

où les$n _ { j }$sont des entiers non tous nuls qui verifient´

$$
n _ {1} \geq \dots \geq n _ {h} \quad \text { et } \quad \sum_ {1 \leq j \leq h} n _ {j} = 0  .
$$

Si J est une partie de$\{ 1 , \ldots , h \}$, on note$e _ { J }$le produit exterieur (dans´ l’ordre) des$e _ { j } , j \in J$, et$n _ { J } = \sum _ { j \in J } n _ { j }$

On voit sur les definitions qu’on a pour tout´$m \in M$

$$
\mu (V _ {m}, c) = \max \left\{n _ {J} \mid J \subseteq \{1, \dots , h \}, | J | = r, \Lambda^ {r} \pi_ {m} (e _ {J}) \neq 0 \right\}
$$

et de même

$$
\mu (v,c) = r!\max_{\substack{1\leq s\leq r\\ n\in N}}\left\{\mu \big(v_{n}^{s},c\big)\right\}
$$

où, pour$1 \leq s \leq r \mathrm { e t } n \in N .$

$$
\mu (v _ {n} ^ {s}, c) = \max \left\{\frac {n _ {J}}{s} \mid J \subseteq \{1, \dots , h \}, | J | = s, v _ {n} ^ {s} (e _ {J}) \neq 0 \right\}.
$$

Dans le cône$n _ { 1 } \ge \cdots \ge n _ { h } , \sum _ { j } n _ { j } = 0$, chaque expression$\mu ( V _ { m } , c )$est lineaire en les coefficients´$n _ { 1 } , \dots , n _ { h }$(voir le paragraphe 4.4 de [Mumford, Fogarty]) et il en est de même de chacune des expressions$\mu ( v _ { n } ^ { s } , c )$pour n et s fixes. D’autre part, une famille de coefficients´$( n _ { 1 } , \ldots , n _ { h } )$dans ce cône s’ecrit comme un barycentre à pond´ erations´$\alpha _ { 1 } , \ldots , \alpha _ { h - 1 } \geq 0$(de somme 1 $\sum _ { f = 1 } ^ { n - 1 } \alpha _ { f } = 1 )$des familles$\underline { n } _ { f }$de la forme :

$$
\left. \begin{array}{l} n _ {1} = \dots = n _ {f} = h - f \\ n _ {f + 1} = \dots = n _ {h} = - f \end{array} \right\}
$$

Or, pour ces familles, les$\mu ( V _ { m } , c )$et les$\mu ( v _ { n } ^ { s } , c )$ont une expression simple :

Pour$m \in M$, notons$F _ { m }$l’image dans$V _ { m }$du sous-espace vectoriel F de base$e _ { 1 } , \ldots , e _ { f }$. Alors on a pour la famille$\underline { n } _ { f }$

$$
\mu (V _ {m}, c) = h \dim (F _ {m}) - f r.
$$

De même, pour$n \in N$, notons$F _ { n }$l’image de F dans le quotient$V _ { n }$de $E _ { n }$induit par V.

Soit$\underline { { r } } = ( r = r _ { 1 } + \cdot \cdot \cdot + r _ { k } )$la partition de l’entier r qui correspond à la strate de$\mathbb { A } ^ { r - 1 }$qui contient l’image de V. On note comme toujours $\underline { { r } } ^ { - } = \{ 0 , r _ { 1 } , \ldots .$$r _ { 1 } + \cdots + r _ { k - 1 } \}$et$\underline { { r } } ^ { + } = \{ r _ { 1 } , \dots , r _ { 1 } + \dots + r _ { k } \}$. Et pour $s \in \{ 1 , \ldots , r \}$, on note ici$s ^ { - }$le plus grand entier dans$\underline { r } ^ { - }$tel que$s ^ { - } < s$et $s ^ { + }$le plus petit entier dans$\underline { { r } } ^ { + }$tel que$s \leq s ^ { + }$

Chacun des espaces$V _ { n } , n \in N$, est muni d’une filtration decroissante´

$$
V _ {n} = V _ {n} ^ {0} \supsetneqq V _ {n} ^ {r _ {1}} \supsetneqq \dots \supsetneqq V _ {n} ^ {r} = 0
$$

par des sous-espaces$V _ { n } ^ { s } , s \in \underline { { r } } ^ { - } \cup \underline { { r } } ^ { + }$, de codimension s.

Avec toutes ces notations, on a alors pour la famille$\underline { n } _ { f }$et pour n et s fixes´

$$
\mu \left(v _ {n} ^ {s}, c\right) = \frac {h}{s} \min \left\{\dim \left(F _ {n} / F _ {n} \cap V _ {n} ^ {s ^ {+}}\right), \dim \left(F _ {n} / F _ {n} \cap V _ {n} ^ {s ^ {-}}\right) + (s - s ^ {-}) \right\} - f.
$$

En resum´ e, on a prouv´ e :´

Proposition V.7. – Pour que l’image d’un point geom´ etrique´$V \in \widetilde { \mathcal { V } }$de type r dans l’espace projectif

$$
\prod_{m\in M}\mathbb{P}\big(\Lambda^{r}E_{m}^{\vee}\big)\times \mathbb{P}\left(\bigoplus_{\substack{1\leq s\leq r\\ n\in N}}\operatorname{Hom}\left(\Lambda^{s}E_{n},\Lambda^{s}E_{n}^{\prime}\right)^{\otimes (r! / s)}\right)
$$

soit stable, ilfaut et il suffit que pour toute filtration de l’espace canonique de dimension h par des sous-espaces non triviaux F et pour toute famille de ponderations´$\alpha _ { F } > 0$de somme 1, on ait

$$
\begin{array}{l} r \epsilon_ {M} \sum_ {m \in M} \sum_ {F} \alpha_ {F} \left[ h \frac {\dim (F _ {m})}{r} - \dim (F) \right] \\ + r! \epsilon_ {N} \max_ {\substack {1 \leq s \leq r \\ n \in N}} \sum_ {F} \alpha_ {F} \left[ \frac {h}{s} \min \left\{\dim \left(F _ {n} / F _ {n} \cap V _ {n} ^ {s ^ {+}}\right), \right. \right. \\ \left. \dim \left(F _ {n} / F _ {n} \cap V _ {n} ^ {s ^ {-}}\right) + (s - s ^ {-}) \right\} - \dim (F _ {f}) ] > 0. \end{array}
$$

## e) Une condition ouverte suffisante pour verifier la stabilit´ e´

Si E est le fibre sous-jacent à un point de´ V de type r, les fibres$\mathcal { E } _ { n }$de$\mathcal { E }$en les points$n \in N$sont munies de filtrations decroissantes par des sous-espaces´ $\overline { { \mathcal { E } _ { n } ^ { s } } } , s \in \underline { { r } } ^ { - } \cup \underline { { r } } ^ { + }$, de codimension s qui sont induites par la structure de niveau$\mathcal { E } _ { N } \Rightarrow \mathcal { O } _ { N } ^ { r }$

Si$\mathcal { F }$est un sous-fibre d’un tel´ E, on notera$\mathcal { F } _ { n }$la fibre de$\mathcal { F }$en tout point$n \in N$et$\mathcal { F } _ { n } ^ { s }$les images reciproques des´$\mathcal { E } _ { n } ^ { s }$par l’homomorphisme $\mathcal { F } _ { n } \to \mathcal { E } _ { n }$

On a :

Lemme V.8. – Considerons la condition suivante portant sur les points´ geom´ etriques de´$\mathcal { V }$:

(S) Pour toute filtration par des sous-fibres non-triviaux´ F du fibre´ E sous-jacent à un point donne de type r´ de V et pour toute famille de ponderations´$\alpha _ { \mathcal { F } } > 0$de somme 1, on a l’inegalit´ e´

$$
\begin{array}{l} \sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \deg (\mathcal {F}) <   \frac {\sum \alpha_ {\mathcal {F}} \operatorname{rg} (\mathcal {F})}{r} d + \sum_ {n \in N} \max _ {1 \leq s \leq r} \sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \\ \left[ \frac {\min \left\{\dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s ^ {+}}\right) , \dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s ^ {-}}\right) + (s - s ^ {-}) \right\}}{s} - \frac {\operatorname{rg} (\mathcal {F})}{r} \right]. \end{array}
$$

Alors :

(i) Pour que cette inegalit´ e soit v´ erifi´ ee par toutes les filtrations par des´ sous-fibres´$\mathcal { F }$de E, il suffit qu’elle le soit par lesfiltrations non triviales par des sous-fibres maximaux.´

(ii) La condition (S) definit un ouvert´$\mathcal { V } ^ { \prime }$de$\mathcal { V } .$.

Demonstration :´ (i) Si$\mathcal { F }$et${ \mathcal { F } } ^ { \prime }$sont deux sous-fibres de´$\mathcal { E }$avec$\mathcal { F } \hookrightarrow \mathcal { F } ^ { \prime }$ $\arg \mathcal { F } = \arg \mathcal { F } ^ { \prime }$et deg$\mathcal { F } ^ { \prime } = \deg \mathcal { F } + 1 , \mathcal { F } _ { n } \to \mathcal { F } _ { n } ^ { \prime }$est un isomorphisme en tous les points$n \in N$sauf un au plus. En ce point-là chaque difference´

$$
\begin{array}{l} \frac {1}{s} \min \left\{\dim \left(\mathcal {F} _ {n} ^ {\prime} / \mathcal {F} _ {n} ^ {\prime s ^ {+}}\right), \dim \left(\mathcal {F} _ {n} ^ {\prime} / \mathcal {F} _ {n} ^ {\prime s ^ {-}}\right) + (s - s ^ {-}) \right\} \\ - \frac {1}{s} \min \left\{\dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s ^ {+}}\right), \dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s ^ {-}}\right) + (s - s ^ {-}) \right\} \end{array}
$$

est bornee par 1 car les deux expressions sont toujours comprises ent´ re 0 et 1. Elle est$< 1$si$\mathcal { F } ^ { \prime } = \mathcal { E }$et$s = r$. Si donc$\{ \mathcal { \bar { F } } \} ^ { \prime }$est une filtration qui comprend${ \mathcal { F } } ^ { \prime }$et verifie´$( S )$et si$\{ \mathcal { F } \}$est une filtration deduite de´$\{ \mathcal { F } \} ^ { \prime }$en remplaçant${ \mathcal { F } } ^ { \prime }$par$\mathcal { F }$, alors$\{ \mathcal { F } \}$verifie aussi l’in´ egalit´ e´ (S).$\mathbf { D } '$autre part, la filtration constituee de´$\mathcal { E }$seul verifie l’´ egalit´ e.´

(ii) La condition (S) est constructible.

Elle est stable par gen´ erisation car si´ V est un point de V specialisation´ d’un point$V ^ { \prime }$, on a :

• Le type$\underline { r }$de V est un raffinement du type$\underline { { r } } ^ { \prime }$de$V ^ { \prime }$.

• Le fibre´$\mathcal { E }$sous-jacent à V est une specialisation du fibr´ e´$\mathcal { E } ^ { \prime }$sous-jacent à$V ^ { \prime }$, les${ \mathcal { E } } _ { n } , n \in N$, sont des specialisations des´$\mathcal { E } _ { n } ^ { \prime }$et pour$s \in \underline { r } ^ { \prime - } \cup \underline { r } ^ { \prime + }$ les$\mathcal { E } _ { n } ^ { \prime s }$se specialisent en les´$\mathcal { E } _ { n } ^ { s }$

• Tout sous-fibre´${ \mathcal { F } } ^ { \prime }$de$\mathcal { E } ^ { \prime }$se specialise en un sous-fibr ´ e´$\mathcal { F }$de$\mathcal { E }$de même rang et même degre et pour tout´$s \in \underline { { r } } ^ { \prime - } \cup \underline { { r } } ^ { \prime + }$, on a

$$
\dim \left(\mathcal {F} _ {n} ^ {\prime} / \mathcal {F} _ {n} ^ {\prime s}\right) \geq \dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s}\right).
$$

Cela suffit pour conclure car, notant pour tout$s \in \{ 1 , \ldots , r \}$

$$
s ^ {-} = \max \{t \in \underline {{r}} ^ {-}, t <   s \}, s ^ {+} = \min \{t \in \underline {{r}} ^ {+}, t \geq s \},
$$

$$
s ^ {\prime -} = \max \{t \in \underline {{r}} ^ {\prime -}, t <   s \}, s ^ {\prime +} = \min \{t \in \underline {{r}} ^ {\prime +}, t \geq s \},
$$

avec donc$s ^ { \prime - } \leq s ^ { - } < s \leq s ^ { + } \leq s ^ { \prime + }$, on a

$$
\dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s ^ {+}}\right) \leq \dim \left(\mathcal {F} _ {n} ^ {\prime} / \mathcal {F} _ {n} ^ {\prime s ^ {+}}\right) \leq \dim \left(\mathcal {F} _ {n} ^ {\prime} / \mathcal {F} _ {n} ^ {\prime s ^ {\prime +}}\right),
$$

$$
\begin{array}{r l} \dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s ^ {-}}\right) + (s - s ^ {-}) & \leq \dim \left(\mathcal {F} _ {n} ^ {\prime} / \mathcal {F} _ {n} ^ {\prime s ^ {-}}\right) + (s - s ^ {-}) \\ & \leq \dim \left(\mathcal {F} _ {n} ^ {\prime} / \mathcal {F} _ {n} ^ {\prime s ^ {\prime -}}\right) + (s - s ^ {\prime -}) \end{array}
$$

d’où

$$
\begin{array}{l} \frac {1}{s} \min \left\{\dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s ^ {+}}\right), \dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s ^ {-}}\right) + (s - s ^ {-}) \right\} \\ \leq \frac {1}{s} \min \left\{\dim \left(\mathcal {F} _ {n} ^ {\prime} / \mathcal {F} _ {n} ^ {\prime s ^ {\prime +}}\right), \dim \left(\mathcal {F} _ {n} ^ {\prime} / \mathcal {F} _ {n} ^ {\prime s ^ {\prime -}}\right) + (s - s ^ {\prime -}) \right\}. \end{array}
$$

On notera${ \widetilde { \mathcal { V } } } ^ { \prime }$l’ouvert de$\widetilde { \mathcal { V } }$image reciproque de l’ouvert´$\mathcal { V } ^ { \prime }$de$\mathcal { V }$.  Sur l’espace projectif produit

$$
\prod_{m\in M}\mathbb{P}\big(\Lambda^{r}E_{m}^{\vee}\big)\times \mathbb{P}\left(\bigoplus_{\substack{1\leq s\leq r\\ n\in N}}\operatorname{Hom}\left(\Lambda^{s}E_{n},\Lambda^{s}E_{n}^{\prime}\right)^{\otimes (r! / s)}\right)  ,
$$

on met une polarisation$( \epsilon _ { M } , \dots , \epsilon _ { M } ; \epsilon _ { N } )$telle que

$$
\epsilon_ {M} | M | \frac {r | N |}{h - | N |} = r! \epsilon_ {N}.
$$

Avec ce choix, nous allons prouver :

Theor´ eme V.9.\` – On suppose que le degre d est assez grand en fonction´ de X, r, du polygone de troncature p et du niveau N et que le degre´$\lvert M \rvert$de M est assez grand enfonction de X, r, p, N et d. Alors le morphisme

$$
\widetilde{\mathcal{V}}^{\prime}\to \prod_{m\in M}\mathbb{P}(\Lambda^{r}E_{m}^{\vee})\times \mathbb{P}\left(\bigoplus_{\substack{1\leq s\leq r\\ n\in N}}\operatorname{Hom}\left(\Lambda^{s}E_{n},\Lambda^{s}E_{n}^{\prime}\right)^{\otimes (r! / s)}\right)
$$

verifie les deux propri´ et´ es suivantes :´

(i) Il envoie V	 dans l’ouvert des points stables.${ \widetilde { \mathcal { V } } } ^ { \prime }$

(ii) Deuxpoints de${ \widetilde { \mathcal { V } } } ^ { \prime }$ont même image si et seulement si ils sont transformes´ l’un de l’autre par$\mathbb { G } _ { m }$

Demonstration´$\therefore \mathit { \Omega } ( \mathrm { i } )$Considerons donc un point´$V$de${ \widetilde { \mathcal { V } } } ^ { \prime }$dont on note$\mathcal { E }$le fibre sous-jacent et´$\underline { r }$le type.

Etant donne´$F$un sous-espace propre de l’espace canonique de dimension$h .$, on peut considerer le sous-fibr´ e´$\mathcal { F }$de E$\mathrm { \ q u ^ { \prime } i l }$engendre. Comme prec´ edemment, les fibres de´$\mathcal { F }$en les$n \in N$sont notees´${ \mathcal { F } } _ { n } ~ ;$elles sont munies de filtrations$( \mathcal { F } _ { n } ^ { s } ) _ { s \in \underline { { r } } ^ { - } \cup \underline { { r } } ^ { + } }$. On designe par´$\mathcal { F } _ { m }$les fibres de$\mathcal { F }$en les $m \in M$et par$\mathcal { F } _ { m } ^ { r }$les noyaux des homomorphismes$\mathcal { F } _ { m } \to \mathcal { E } _ { m }$

En notant$h ^ { 0 } ( { \mathcal { F } } )$et$h ^ { 1 } ( \mathcal { F } )$les dimensions de$H ^ { 0 } ( { \overline { { X } } } , { \mathcal { F } } )$et$H ^ { 1 } ( { \overline { { X } } } , { \mathcal { F } } )$ on a bien sûr

$$
\dim (F) \leq h ^ {0} (\mathcal {F})
$$

et l’inegalit´ e est stricte si´$\mathcal { F } = \mathcal { E }$

Il suffit donc de prouver que si$\{ \mathcal { F } \}$est une filtration non triviale de$\mathcal { E }$et les$\alpha _ { \mathcal { F } }$sont des ponderations´$> 0$de somme 1, on a

$$
\begin{array}{l}\frac{1}{|M|}\sum_{m\in M}\sum_{\mathcal{F}}\alpha_{\mathcal{F}}\left[h\frac{\dim\left(\mathcal{F}_{m} / \mathcal{F}_{m}^{r}\right)}{r} -h^{0}(\mathcal{F})\right]\\ +\frac{|N|}{h - |N|}\max_{\substack{1\leq s\leq r\\ n\in N}}\sum_{\mathcal{F}}\alpha_{\mathcal{F}}\Bigg[\frac{h}{s}\min \big\{\dim \left(\mathcal{F}_{n} / \mathcal{F}_{n}^{s^{+}}\right),\\ \dim \left(\mathcal{F}_{n} / \mathcal{F}_{n}^{s^{-}}\right) + (s - s^{-})\big\} -h^{0}(\mathcal{F})\Bigg] > 0 \end{array}
$$

(en effet, cette expression vaut 0 si tous les$\mathcal { F }$sont egaux à´ E). Cela se recrit´

$$
\begin{array}{l}\sum_{\mathcal{F}}\alpha_{\mathcal{F}}h^{0}(\mathcal{F}) + \frac{h - |N|}{r}\frac{1}{|M|}\sum_{m\in M}\sum_{\mathcal{F}}\alpha_{\mathcal{F}}\dim (\mathcal{F}^{r})\\ <   \frac{h - |N|}{r}\sum_{\mathcal{F}}\alpha_{\mathcal{F}}\operatorname{rg}(\mathcal{F})\\ +|N|\max_{\substack{1\leq s\leq r\\ n\in N}}\sum_{\mathcal{F}}\alpha_{\mathcal{F}}\frac{\min \left\{\dim\left(\mathcal{F}_{n} / \mathcal{F}_{n}^{s^{+}}\right), \dim\left(\mathcal{F}_{n} / \mathcal{F}_{n}^{s^{-}}\right) + (s - s^{-})\right\}}{s}. \end{array}
$$

On a besoin du lemme suivant :

Lemme V.10. – Soient F et${ \mathcal { F } } ^ { \prime }$deuxfibres de même rang sur´${ \overline { { X } } } ,$, relies par´ un homomorphisme injectif$\mathcal { F } \hookrightarrow \mathcal { F } ^ { \prime }$et tels que$\mathcal { F }$soit engendre par ses´ sections globales.

Alors on a :

(i)$\deg ( \mathcal { F } ^ { \prime } / \mathcal { F } ) \leq \deg ( \mathcal { F } ^ { \prime } )$

(ii)$h ^ { 0 } ( \mathcal { F } ^ { \prime } ) \leq \mathrm { r g } ( \mathcal { F } ^ { \prime } ) + \mathrm { d e g } ( \mathcal { F } ^ { \prime } )$

Demonstration´$\therefore \mathit { \Omega } ( \mathrm { i } )$Le fibre´$\mathcal { F }$contient un sous-fibre de la forme´$\mathcal { O } _ { \overline { { X } } } ^ { \mathrm { r g \mathcal { F } } }$

Le quotient$\mathcal { F } / \mathcal { O } _ { \overline { { X } } } ^ { \mathrm { r g \mathcal { F } } }$est de torsion donc

$$
\deg (\mathcal {F} ^ {\prime} / \mathcal {F}) \leq \deg \left(\mathcal {F} ^ {\prime} / \mathcal {O} _ {\overline {{X}}} ^ {\mathrm{rg} \mathcal {F}}\right) = \deg (\mathcal {F} ^ {\prime}).
$$

(ii) On a la suite exacte

$$
0 \to \mathcal {F} \to \mathcal {F} ^ {\prime} \to \mathcal {F} ^ {\prime} / \mathcal {F} \to 0
$$

où${ \mathcal { F } } ^ { \prime } / { \mathcal { F } }$est de torsion et où on peut supposer que$\mathcal { F }$est de la forme $\mathcal { O } _ { \overline { { X } } } ^ { \mathrm { r g \mathcal { F } } }$. Mais dans ce cas

$$
h ^ {0} \left(\mathcal {F} ^ {\prime}\right) \leq h ^ {0} (\mathcal {F}) + h ^ {0} \left(\mathcal {F} ^ {\prime} / \mathcal {F}\right) = \operatorname{rg} \left(\mathcal {F} ^ {\prime}\right) + \deg \left(\mathcal {F} ^ {\prime}\right).
$$

Suite de la demonstration du th´ eorème V.9 :´ Comme le polygone canonique du fibre´ E est majore par´$p ,$, il resulte du lemme´$\mathrm { V . \bar { 1 0 ( i ) } }$que pour tout sous-fibre´$\mathcal { F }$de$\mathcal { E }$, on a

$$
\sum_ {m \in M} \dim \left(\mathcal {F} _ {m} ^ {r}\right) \leq \frac {\operatorname{rg} \mathcal {F}}{r} d + p (\operatorname{rg} \mathcal {F}).
$$

Considerons´$\mathrm { d } ^ { \prime }$abord les sous-fibres´$\mathcal { F }$dans la filtration qui verifient´ $h ^ { 1 } ( \mathcal { F } ) \neq 0$. On pretend qu’ils satisfont l’in´ egalit´ e´

$$
h ^ {0} (\mathcal {F}) + \frac {1}{| M |} \frac {h - | N |}{r} \left(\frac {\operatorname{rg} \mathcal {F}}{r} d + p (\operatorname{rg} \mathcal {F})\right) <   \frac {h - | N |}{r} \operatorname{rg} (\mathcal {F}).
$$

En effet, ayant fixe un entier´$k _ { 0 }$et ayant pris d assez grand en fonction de$k _ { 0 }$et du polygone$p ,$, on voit d’après le lemme V.6(iii) que

$$
\deg (\mathcal {F}) <   k _ {0} + \frac {\operatorname{rg} \mathcal {F}}{r} d
$$

si bien que d’après le lemme V.10(ii) ci-dessus on a

$$
h ^ {0} (\mathcal {F}) <   k _ {0} + \frac {\mathrm{rg} \mathcal {F}}{r} d + \mathrm{rg} \mathcal {F}.
$$

Comme$h = d + ( 1 - g ) r$, on est reduit à prouver´

$$
k _ {0} + \frac {\operatorname{rg} \mathcal {F}}{r} d + \operatorname{rg} \mathcal {F} + \frac {1}{| M |} \frac {(h - | N |)}{r} \left(\frac {\operatorname{rg} \mathcal {F}}{r} d + p (\operatorname{rg} \mathcal {F})\right)
$$

$$
\leq \frac {\mathrm{rg} \mathcal {F}}{r} d + (1 - g) \mathrm{rg} \mathcal {F} - \frac {| N |}{r} \mathrm{rg} \mathcal {F}.
$$

$\mathbf { C } '$est verifi´ e si´$k _ { 0 }$est pris suffisamment negatif en fonction de´$r , \mid N \mid$et$g$ puis |M| suffisamment grand en fonction de$r , | N | , g , p$et$d .$

Ceci nous ramène au cas où tous les el´ ements´$\mathcal { F }$de la filtration verifient´ $h ^ { 1 } ( \mathcal { F } ) = 0$, soit

$$
h ^ {0} (\mathcal {F}) = \deg \mathcal {F} + (1 - g) \operatorname{rg} \mathcal {F}.
$$

Comme le point V verifie la condition (S) du lemme V.8 qui d´ efinit les´ ouverts$\mathcal { V } ^ { \prime }$et${ \widetilde { \mathcal { V } } } ^ { \prime }$, la difference´

$$
\begin{array}{l} \varepsilon = | N | \max_ {\substack {1 \leq s \leq r \\ n \in N}} \sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \frac {\min \left\{\dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s ^ {+}}\right) , \dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s ^ {-}}\right) + (s - s ^ {-}) \right\}}{s} \\ - \sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \left[ \deg \mathcal {F} - \frac {\operatorname{rg} \mathcal {F}}{r} d + | N | \frac {\operatorname{rg} \mathcal {F}}{r} \right] \end{array}
$$

est > 0. Il s’agit de prouver

$$
\begin{array}{l} \sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} [ \deg \mathcal {F} + (1 - g) \operatorname{rg} \mathcal {F} ] \\ \qquad \qquad \qquad + \frac {1}{| M |} \frac {h - | N |}{r} \sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \left[ \frac {\operatorname{rg} \mathcal {F}}{r} d + p (\operatorname{rg} \mathcal {F}) \right] \\ <   \varepsilon + \sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \left[ \deg \mathcal {F} - \frac {\operatorname{rg} \mathcal {F}}{r} d + | N | \frac {\operatorname{rg} \mathcal {F}}{r} + \frac {h - | N |}{r} \operatorname{rg} \mathcal {F} \right] \end{array}
$$

qui$\mathrm {  ~ s ~ } ^ { \prime }$ecrit encore´

$$
\frac {1}{| M |} \frac {h - | N |}{r} \sum \alpha_ {\mathcal {F}} \left[ \frac {\mathrm{rg} \mathcal {F}}{r} d + p (\mathrm{rg} \mathcal {F}) \right] <   \varepsilon .
$$

Dans le simplexe des familles de ponderations´$\alpha _ { \mathcal { F } } \geq 0$de somme 1, il existe une decomposition en polyèdres convexes où´ ε est une fonction lineaire et´ dont les sommets ont des coordonnees´$\alpha _ { \mathcal { F } }$rationnelles ne dependant que´ de r. Il suffit de traiter le cas de ces sommets$( \alpha _ { \mathcal { F } } )$mais alors$\varepsilon > 0$est minoree par une constante positive qui ne d´ epend que de´$r$et l’inegalit´ e ci-´ dessus est automatiquement verifi´ ee si´$\lvert M \rvert$est pris assez grand en fonction de$g , r , p , | N |$et$d .$

(ii) Considerons deux points´ V et$V ^ { \prime }$de${ \widetilde { \mathcal { V } } } ^ { \prime }$qui ont la même image dans

$$
\prod_{m\in M}\mathbb{P}\big(\Lambda^{r}E_{m}^{\vee}\big)\times \mathbb{P}\left(\bigoplus_{\substack{1\leq s\leq r\\ n\in N}}\operatorname{Hom}\left(\Lambda^{s}E_{n},\Lambda^{s}E_{n}^{\prime}\right)^{\otimes (r! / s)}\right)  .
$$

Soient$\mathcal { E }$et$\mathcal { E } ^ { \prime }$leurs fibres sous-jacents. Ils´$\mathrm {  ~ s ~ } ^ { \prime }$ecrivent comme les quo-´ tients de$\mathcal { O } _ { \overline { { X } } } ^ { h }$par des sous-fibres maximaux´$\mathcal { H }$et${ \mathcal { H } } ^ { \prime }$

Il$\mathrm {  ~ s ~ } ^ { \prime }$agit de montrer que$\mathcal { H } = \mathcal { H } ^ { \prime } \mathrm { c } ^ { \prime } \mathrm { e s t - a - d i r e }$que$\mathcal { H } \to \mathcal { E } ^ { \prime }$et$\mathcal { H } ^ { \prime } \to \mathcal { E }$ sont nuls.

Supposons par exemple que$\mathcal { H } ^ { \prime } \to \mathcal { E }$n’est pas nul et notons$\mathcal { F }$son image,$\bar { \mathcal { K } } ^ { \prime }$son noyau.

Comme la restriction à M de$\mathcal { H } ^ { \prime } \to \mathcal { E }$est nulle,$\mathcal { F }$est contenu dans $\mathcal { E } ( - M )$et on peut majorer

$$
\deg \mathcal {F} \leq \frac {\operatorname{rg} \mathcal {F}}{r} d + p (\operatorname{rg} \mathcal {F}) - | M | \operatorname{rg} \mathcal {F}.
$$

D’autre part, on a

$$
\deg \mathcal {H} ^ {\prime} = \deg \mathcal {O} _ {\overline {{X}}} ^ {h} - \deg \mathcal {E} ^ {\prime} = - d
$$

et deg$\mathcal { K } ^ { \prime } \leq 0$puisque$\mathcal { K } ^ { \prime }$est plonge dans´${ \mathcal { O } } { \frac { h } { X } } .$

On en deduit deg´$\mathcal { F } = \mathrm { d e g } \mathcal { H } ^ { \prime } - \mathrm { d e g } \mathcal { K } ^ { \prime } \overset {  } { \geq } - d .$

Il y a contradiction si$\lvert M \rvert$est assez grand en fonction de r, p et$d .$. !"

On deduit du th´ eorème V.9 :´

Corollaire V.11. –

(i) Le schema´${ \widetilde { \mathcal { V } } } ^ { \prime }$est quasi-affine au-dessus de

$$
\prod_{m\in M}\mathbb{P}\big(\Lambda^{r}E_{m}^{\vee}\big)\times \mathbb{P}\left(\bigoplus_{\substack{1\leq s\leq r\\ n\in N}}\operatorname{Hom}\left(\Lambda^{s}E_{n},\Lambda^{s}E_{n}^{\prime}\right)^{\otimes (r! / s)}\right)  .
$$

Le fibre ample image r´ eciproque est naturellement muni d’une action´ du groupe$\mathrm { P G L } _ { { h } }$(et aussi du tore$\mathbb { G } _ { m } ^ { r - 1 } )$

(ii) Relativement à cette action de$\mathrm { P G L } _ { h }$sur sonfibre ample, tous lespoints´ de${ \widetilde { \mathcal { V } } } ^ { \prime }$sont stables.

(iii) L’ouvert V	 de V est un schema quasi-projectif´ (dont le fibre ample´ naturel est muni d’une action de$\bar { \mathbb { G } } _ { m } ^ { r - 1 } )$).

Demonstration :´ (i) D’après le theorème V.9(ii), la projection sur cet es-´ pace projectif produit du quotient$\widetilde { \mathcal { V } } ^ { \prime } / \mathbb { G } _ { m }$de${ \widetilde { \mathcal { V } } } ^ { \prime }$par l’action libre de $\mathbb { G } _ { m }$ est un monomorphisme. D’après le corollaire A.2.2 de [Laumon, Moret-Bailly],${ \mathrm { c } } ^ { \prime }$est un morphisme quasi-affine et il en est de même de la projection de${ \widetilde { \mathcal { V } } } ^ { \prime }$

(Remarque : En fait, on peut montrer que la projection de$\widetilde { \mathcal { V } } ^ { \prime } / \mathbb { G } _ { m }$est une immersion localement fermee.)´

(ii) resulte de (i) et du th´ eorème V.9(i) d’après la proposition 1.18 de´ [Mumford, Fogarty] chapitre 1, paragraphe 5.

(iii) resulte de (ii) d’après le th´ eorème 1.10 de [Mumford, Fogarty] cha-´ pitre 1, paragraphe 4.!"

## f) Verification du critère de stabilit´ e par les chtoucas it´ er´ es´

Nous allons montrer maintenant :

Proposition V.12. – Si le degre´ |N| du niveau reduit´$N = \operatorname { S p e c } { \mathcal { O } } _ { N } \hookrightarrow X$ est assez grand en fonction de X, de r et du polygone de troncature$p ,$le morphisme

$$
\overline {{\operatorname{Cht} _ {N} ^ {r , d , \overline {{p}} \leq p}}} ^ {\prime} \times_ {\left(\mathbb {A} ^ {r - 1} / \mathbb {G} _ {m} ^ {r - 1}\right)} \mathbb {A} ^ {r - 1} \to \overline {{\operatorname{Vec} _ {N} ^ {r , d , \overline {{p}} \leq p}}} = \mathcal {V}
$$

sefactorise$\grave { a }$travers l’ouvert$\mathcal { V } ^ { \prime }$de V.

Demonstration :´ Considerons donc un point g´ eom´ etrique´${ \widetilde { \mathcal { E } } = ( \mathcal { E } \hookrightarrow \mathcal { E } ^ { \prime } }$ $\begin{array} { r } { \longleftrightarrow \mathcal { E } ^ { \prime \prime } ; \ell _ { 1 } , . . . , \ell _ { r - 1 } ; { \mathrm { \Delta } } ^ { \tau } \mathcal { E } \Rightarrow \mathcal { E } ^ { \prime \prime } ; \mathcal { E } _ { N } \Rightarrow \mathcal { O } _ { \overline { N } } ^ { r } ) \mathrm { ~ d e ~ C h t } _ { N } ^ { r , d , \overline { { p } } \leq p ^ { \prime } } \times { _ { ( \mathbb { A } ^ { r - 1 } / \mathbb { C } _ { m } ^ { r - 1 } ) } \mathbb { A } ^ { r - 1 } } } \end{array}$ Soit r son type.

On sait que$\mathcal { E } , \mathcal { E } ^ { \prime } , \mathcal { E } ^ { \prime \prime }$sont munis de filtrations croissantes canoniques $( \mathcal { E } _ { s } ) , ( \mathcal { E } _ { s } ^ { \prime } ) , ( \mathcal { E } _ { s } ^ { \prime \prime } )$par des sous-fibres maximaux de rangs´$s \in \underline { { r } } ^ { - } \cup \underline { { r } } ^ { + }$. Le fibre´ E est de degre´$d ,$, sa filtration canonique de Harder-Narasimhan est un raffinement de$( \mathcal { E } _ { s } )$, son polygone canonique est majore par´ p et on a

$$
\deg \left(\mathcal {E} _ {s}\right) - \frac {s}{r} d \in ] p (s) - 1, p (s) ], \forall s \in \underline {{{r}}} ^ {-} \cup \underline {{{r}}} ^ {+}.
$$

$\mathbf { D } '$autre part,$\tau _ { \mathcal { E } }$est muni d’une filtration decroissante´$( \overline { { \mathcal { E } } } ^ { s } )$par des sousfibres maximaux de corangs´$s \in \underline { { r } } ^ { - } \cup \underline { { r } } ^ { + }$et on a des isomorphismes

$$
\overline {{{\mathcal {E}}}} ^ {s ^ {-}} / \overline {{{\mathcal {E}}}} ^ {s} \cong \mathcal {E} _ {s} ^ {\prime \prime} / \mathcal {E} _ {s ^ {-}} ^ {\prime \prime}.
$$

Pour$0 < s ^ { - } < s < r$[resp.$0 = s ^ { - } < s < r , 0 < s ^ { - } < s = r ,$ $0 = s ^ { - } < s = r ]$on a un isomorphisme$\mathcal { E } _ { s } ^ { \prime \prime } / \mathcal { E } _ { s ^ { - } } ^ { \prime \prime } \ \cong \ \mathcal { E } _ { s } / \mathcal { E } _ { s ^ { - } } \ [ \mathrm { r e s p }$. un plongement de degre 1´$\mathbf { \mathcal { E } } _ { s } ^ { \prime \prime } / \mathbf { \mathcal { E } } _ { s ^ { - } } ^ { \prime \prime } \longleftrightarrow \mathbf { \mathcal { E } } _ { s } / \mathbf { \mathcal { E } } _ { s ^ { - } } , \mathbf { \mathcal { E } } _ { s } ^ { \prime \prime } / \mathbf { \dot { \mathcal { E } } } _ { s ^ { - } } ^ { \prime \prime } \mathbf { \overset { \circ } { \hookrightarrow } } \mathbf { \mathcal { E } } _ { s } / \mathbf { \dot { \mathcal { E } } } _ { s ^ { - } } , \mathbf { \mathcal { E } } _ { s } ^ { \prime \prime } / \mathbf { \mathcal { E } } _ { s ^ { - } } ^ { \prime \prime } \mathbf { \hookrightarrow } \quad$ $\bar { \mathcal { E } } _ { s } ^ { \prime } / \mathcal { E } _ { s ^ { - } } ^ { \prime } \longleftrightarrow \mathcal { E } _ { s } / \mathcal { E } _ { s ^ { - } } ]$

Comme$p$a et´ e pris assez convexe, la filtration canonique de Harder-´ Narasimhan du fibre´

$$
\bigoplus_ {s \in \underline {{r}} ^ {+}} \overline {{\mathcal {E}}} ^ {s ^ {-}} / \overline {{\mathcal {E}}} ^ {s}
$$

est un raffinement de la filtration par les

$$
\bigoplus_{\substack{s\in \underline{r}^{+}\\ s\leq t}}\overline{\mathcal{E}}^{s^{-}} / \overline{\mathcal{E}}^{s},\quad t\in \underline{r}^{-}\cup \underline{r}^{+}  .
$$

On notera$\overline { { p } }$le polygone canonique de ce fibre.´$\mathrm { C } '$est un polygone convexe $\overline { { p } } : [ 0 , r ]  \mathbb { R } _ { + }$, s’annulant aux points extremaux 0 et´$r$et qui admet des ruptures de pentes en les entiers$s \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + }$

On sait d’autre part qu’en tout point$n \in N$, le transforme par´ τ de la filtration decroissante´$( \mathcal { E } _ { n } ^ { s } )$de la fibre$\mathcal { E } _ { n }$de E en n qui est induite par la structure de niveau$\mathcal { E } _ { N } \overset { \cdot } { \Rightarrow } \mathcal { O } _ { N } ^ { r }$coïncide avec la filtration induite par celle $( \overline { { \mathcal { E } } } ^ { s } )$de$\tau _ { \mathcal { E } }$par des sous-fibres.´

Selon le lemme V.8(i), on doit montrer que si$\{ \mathcal { F } \}$est une filtration non-triviale de$\mathcal { E }$par des sous-fibres maximaux et les´$\alpha _ { \mathcal { F } }$sont des ponderations´ $> 0$de somme 1, on a

$$
\begin{array}{l} \sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \deg (\mathcal {F}) <   \sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \frac {\operatorname{rg} \mathcal {F}}{r} d + \sum_ {n \in N} \max _ {1 \leq s \leq r} \\ \sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \left[ \frac {\min \left\{\dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s ^ {+}}\right) , \dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s ^ {-}}\right) + (s - s ^ {-}) \right\}}{s} - \frac {\operatorname{rg} \mathcal {F}}{r} \right] \end{array}
$$

(pourvu que$| N |$soit assez grand en fonction de$p )$. Ici encore on peut supposer que les$\alpha _ { \mathcal { F } }$sont des rationnels el´ ements d’un ensemble fini qui ne´ depend que de´ r. Les expressions

$$
\max _ {1 \leq s \leq r} \sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \left[ \frac {\min \left\{\dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s ^ {+}}\right) , \dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s ^ {-}}\right) + (s - s ^ {-}) \right\}}{s} - \frac {\operatorname{rg} \mathcal {F}}{r} \right]
$$

sont toutes$\geq 0$et quand elles ne sont pas nulles elles sont minorees par une´ constante$> 0$qui ne depend que de´ r.

Pour tout el´ ement´$\mathcal { F }$de la filtration$\{ \mathcal { F } \}$, notons$\mathrm { d } ^ { \prime }$autre part$( \overline { \mathcal { F } } ^ { s } ) =$ $( ^ { \tau } \mathcal { F } \cap \overline { { \mathcal { E } } } ^ { s } ) _ { s \in \underline { { r } } ^ { - } \cup \underline { { r } } ^ { + } }$la filtration de$\tau _ { \mathcal { F } } = \overline { { \mathcal { F } } }$induite par la filtration decroissante´ $( \overline { { \mathcal { E } } } ^ { s } )$de$\tau _ { \mathcal { E } }$

On a la majoration

$$
\begin{array}{l} \deg (\mathcal {F}) = \deg (\overline {{\mathcal {F}}}) \\ = \sum_ {s \in \underline {{r}} ^ {+}} \deg (\overline {{\mathcal {F}}} ^ {s ^ {-}} / \overline {{\mathcal {F}}} ^ {s}) \\ \leq \frac {\operatorname{rg} \mathcal {F}}{r} d - | N _ {\mathcal {F}} | + \sum_ {s \in \underline {{r}} ^ {+}} [ \overline {{p}} (s ^ {-} + \operatorname{rg} (\overline {{\mathcal {F}}} ^ {s ^ {-}} / \overline {{\mathcal {F}}} ^ {s})) - \overline {{p}} (s ^ {-}) ] \end{array}
$$

où$| N _ { \mathcal { F } } |$designe le cardinal du sous-ensemble´$N _ { \mathcal { F } }$de N des el´ ements´ n pour lesquels il existe$s \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + }$verifiant´

$$
\dim \left(\mathcal {F} _ {n} / \mathcal {F} _ {n} ^ {s}\right) \neq \operatorname{rg} (\overline {{\mathcal {F}}} / \overline {{\mathcal {F}}} ^ {s}) = d _ {\mathcal {F}} ^ {s}.
$$

Comme par hypothèse le cardinal$| N |$est très grand en fonction du polygone$p ,$on est ramene à montrer que si la filtration´$\{ \mathcal { F } \}$verifie´

$$
\sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \left[ \frac {\min \left\{d _ {\mathcal {F}} ^ {s ^ {+}} , d _ {\mathcal {F}} ^ {s ^ {-}} + (s - s ^ {-}) \right\}}{s} - \frac {\operatorname{rg} \mathcal {F}}{r} \right] \leq 0
$$

pour tout s,$1 \leq s \leq r$, alors

$$
\sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \sum_ {s \in \underline {{{{r}}}} ^ {+}} \left[ \overline {{{{p}}}} \big (s ^ {-} + d _ {\mathcal {F}} ^ {s} - d _ {\mathcal {F}} ^ {s ^ {-}} \big) - \overline {{{{p}}}} (s ^ {-}) \right] <   0.
$$

Le polygone$\overline { { p } } : [ 0 , r ]  \mathbb { R } _ { + }$est convexe et il a des ruptures de pentes en les entiers$t \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + }$. Il${ \bf s } '$ecrit comme une somme´

$$
\overline {{p}} = \sum_ {1 \leq t <   r} \overline {{p}} _ {t}
$$

où chaque$\overline { { p } } _ { t }$est un polygone convexe qui est affine sur$[ 0 , t ]$et$[ t , r ]$et même a une rupture de pente en t si$t \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + }$

$$
1 \leq t <   r.
$$

$$
\sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \sum_ {s \in \underline {{r}} ^ {+}} \left[ \overline {{p}} _ {t} \big (s ^ {-} + d _ {\mathcal {F}} ^ {s} - d _ {\mathcal {F}} ^ {s ^ {-}} \big) - \overline {{p}} _ {t} (s ^ {-}) \right] \leq 0
$$

est exactement equivalente (si´$\overline { { p } } _ { t } \neq 0 )$à l’inegalit´ e´

$$
\sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \left[ \frac {\min \left\{d _ {\mathcal {F}} ^ {t ^ {+}} , d _ {\mathcal {F}} ^ {t ^ {-}} + (t - t ^ {-}) \right\}}{t} - \frac {\mathrm{rg} \mathcal {F}}{r} \right] \leq 0
$$

laquelle est verifi´ ee par hypothèse.´

De plus, on a pour tout$\mathcal { F }$

$$
\frac {\min \left\{d _ {\mathcal {F}} ^ {r} , d _ {\mathcal {F}} ^ {r ^ {-}} + (r - r ^ {-}) \right\}}{r} - \frac {\operatorname{rg} \mathcal {F}}{r} \geq 0
$$

et il y a egalit´ e si et seulement si´$d _ { \mathcal { F } } ^ { r ^ { - } } = \mathrm { r g } \mathcal { F } - ( r - r ^ { - } )$puisque$d _ { \mathcal { F } } ^ { r } = \mathrm { r g } \mathcal { F }$ et$d _ { \mathcal { F } } ^ { r } - d _ { \mathcal { F } } ^ { r ^ { - } } \leq ( r - r ^ { - } )$

L’inegalit ´ e´

$$
\sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \left[ \frac {\min \left\{d _ {\mathcal {F}} ^ {r} , d _ {\mathcal {F}} ^ {r ^ {-}} + (r - r ^ {-}) \right\}}{r} - \frac {\operatorname{rg} \mathcal {F}}{r} \right] \leq 0
$$

impose donc que pour tout$\mathcal { F }$, on ait

$$
d _ {\mathcal {F}} ^ {r ^ {-}} = \mathrm{rg}   \mathcal {F} - (r - r ^ {-})  .
$$

Comme la filtration$\{ \mathcal { F } \}$est non triviale, cela impose$r ^ { - } > 0$et on obtient une inegalit´ e stricte´

$$
\sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \left[ \frac {d _ {\mathcal {F}} ^ {r ^ {-}}}{r ^ {-}} - \frac {\mathrm{rg} \mathcal {F}}{r} \right] <   0
$$

qui implique

$$
\sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \sum_ {s \in \underline {{r}} ^ {+}} \left[ \overline {{p}} _ {r ^ {-}} \left(s ^ {-} + d _ {\mathcal {F}} ^ {s} - d _ {\mathcal {F}} ^ {s ^ {-}}\right) - \overline {{p}} _ {r ^ {-}} (s ^ {-}) \right] <   0
$$

(puisque$\overline { { p } } _ { r ^ { - } } \neq 0 )$et donc

$$
\sum_ {\mathcal {F}} \alpha_ {\mathcal {F}} \sum_ {s \in \underline {{r}} ^ {+}} \left[ \overline {{p}} \big (s ^ {-} + d _ {\mathcal {F}} ^ {s} - d _ {\mathcal {F}} ^ {s ^ {-}} \big) - \overline {{p}} (s ^ {-}) \right] <   0.
$$

## 2) Stabilisation des correspondances de Hecke dans un ouvert lisse

## a) Prolongement des correspondances de Hecke par normalisation

Pour tout niveau$N \hookrightarrow X$et comme rappele dans le paragraphe 1c du´ chapitre I, à toute fonction$f \in \mathcal { H } _ { N } ^ { r }$est associee une correspondance finie´ etale, encore not´ ee´$f _ { \ast }$dans$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb Z } \times _ { X \times X } ( X - T _ { f } ) \times ( X - T _ { f } )$au-dessus de l’identite de´$( X - T _ { f } ) \times ( \dot { X ^ { - } } - T _ { f } )$, pour$T _ { f }$un ensemble fini de points fermes de´ X contenant N qui depend de´$f . { \mathrm { C } }$est une combinaison lineaire´ finie de champs$\Gamma _ { N } ^ { r } ( g )$munis de morphismes representables finis´

$$
\Gamma_ {N} ^ {r} (g) \to \mathrm{Cht} _ {N} ^ {r} / a ^ {\mathbb {Z}} \times_ {X \times X} \mathrm{Cht} _ {N} ^ {r} / a ^ {\mathbb {Z}} \times_ {X \times X} (X - T _ {f}) \times (X - T _ {f})
$$

dont les composes avec les deux projections sur´${ \mathrm { C h t } } _ { N } ^ { r } \times _ { X \times X } ( X - T _ { f } ) \ \times$ $( X - T _ { f } )$sont representables finis´ etales.´

D’autre part, Λ designant le sch´ ema compl´ ementaire dans´$X \times X$ de la diagonale et de ses images reciproques successives par les endo-´ morphismes Frob$\boldsymbol { x } \times \operatorname { I d } _ { X }$et$\operatorname { I d } _ { X } \times \operatorname { F r o b } _ { X }$, on dispose des deux endomorphismes de Frobenius partiels$\mathrm { F r o b } _ { \infty }$et Frob dans$\operatorname { C h t } _ { N } ^ { r } / a ^ { \mathbb { Z } } \times _ { X \times X }$Λ audessus des endomorphismes$\operatorname { F r o b } _ { X } \times \operatorname { I d } _ { X }$et$\operatorname { I d } _ { X } \times \operatorname { F r o b } _ { X }$de Λ ; ils verifient´ $\mathrm { F r o b } _ { \infty } \circ \mathrm { F r o b } _ { 0 } = \mathrm { F r o b } _ { 0 } \circ \mathrm { F r o b } _ { \infty } = \mathrm { F r o b } .$

Notant$\Lambda _ { f } ~ = ~ \Lambda \times _ { X \times X } ( X - T _ { f } ) \times ( X - T _ { f } )$, on peut considerer´ pour tous entiers s,$u \in \mathbb { N }$la correspondance$f ^ { ^ { \prime } } \times \mathrm { F r o b } _ { \infty } ^ { \hat { s } } \times \mathrm { F r o b } _ { 0 } ^ { u }$dans $\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb { Z } } \times _ { X \times X } \Lambda _ { f }$au-dessus de$\mathrm { F r o b } _ { X } ^ { s } \times \mathrm { F r o b } _ { X } ^ { u }$obtenue en composant la correspondance f et les endomorphismes$\mathrm { F r o b } _ { \infty } ^ { s }$et$\mathrm { F r o b } _ { 0 } ^ { u } . \mathrm { C }$est une combinaison lineaire finie de champs munis de morphismes repr´ esentables finis´ sur$( \mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb { Z } } \times _ { X \times X } \Lambda _ { f } ) \times _ { \mathrm { F r o b } _ { X } ^ { s } \times \mathrm { F r o b } _ { X } ^ { u } , \Lambda _ { f } } ( \mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb { Z } } \times _ { X \times X } \Lambda _ { f } )$dont les composes avec la première projection sur´$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb { Z } } \times _ { X \times X } \Lambda _ { f }$sont representables´ finis etales.´

On remarque que les transformes par une telle correspondance des´ points gen´ eriques de´$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb Z }$consistent encore en des familles de points gen´ eriques de´$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb Z }$; tous sont dans l’ouvert$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$pour n’importe quel polygone de troncature$p : [ 0 , r ] \to \mathbb { R } _ { + }$. Cela signifie que chaque correspondance$f \times { \mathrm { F r o b } } _ { \infty } ^ { s } \times { \mathrm { F r o b } } _ { 0 } ^ { u }$est engendree par sa trace dans l’ouvert´

$$
\left(\operatorname{Cht} _ {N} ^ {r, \overline {{p}} \leq p} / a ^ {\mathbb {Z}} \times_ {X \times X} \Lambda_ {f}\right) \times_ {\operatorname{Frob} _ {X} ^ {s} \times \operatorname{Frob} _ {X} ^ {u}, \Lambda_ {f}} \left(\operatorname{Cht} _ {N} ^ {r, \overline {{p}} \leq p} / a ^ {\mathbb {Z}} \times_ {X \times X} \Lambda_ {f}\right)
$$

et on est autorise à noter encore´$f \times { \mathrm { F r o b } } _ { \infty } ^ { s } \times { \mathrm { F r o b } } _ { 0 } ^ { u }$la normalisation de celle-ci au-dessus de la compactification

$$
\overline {{\mathrm{Cht} _ {N} ^ {r , \overline {{p}} \leq p}}} / a ^ {\mathbb {Z}} \times_ {\operatorname{Frob} _ {X} ^ {s} \times \operatorname{Frob} _ {X} ^ {u}, (X - N) \times (X - N)} \overline {{\mathrm{Cht} _ {N} ^ {r , \overline {{p}} \leq p}}} / a ^ {\mathbb {Z}}
$$

ou bien au-dessus de

$$
\widetilde {\operatorname{Cht} _ {N} ^ {r , \overline {{p}} \leq p}} / a ^ {\mathbb {Z}} \times_ {\operatorname{Frob} _ {X} ^ {s} \times \operatorname{Frob} _ {X} ^ {u}, (X - N) \times (X - N)} \widetilde {\operatorname{Cht} _ {N} ^ {r , \overline {{p}} \leq p}} / a ^ {\mathbb {Z}}
$$

quand on sait que$\mathcal { C } _ { N } ^ { r }$admet une resolution des singularit´ es´$\widetilde { \mathcal { C } } _ { N } ^ { r }$(par exemple quand N est simple ou quand$r = 2 )$.

Resumons :´

Lemme V.13. – Pour tout niveau$N \hookrightarrow X$, tout polygone de troncature $p : [ 0 , r ] \to \mathbb { R } _ { + }$assez convexe en fonction de X et de N, toute fonction $f \in \mathcal { H } _ { N } ^ { r }$et tous entiers s,$u \in \mathbb { N }$, l’ecriture compos´ ee´

$$
f \times \operatorname{Frob} _ {\infty} ^ {s} \times \operatorname{Frob} _ {0} ^ {u}
$$

definit une correspondance dans´$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$(ou dans$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z }$quand il existe) au-dessus de l’endomorphisme Frob$\mathbf { \Pi } _ { X } ^ { s } \times \operatorname { F r o b } _ { X } ^ { u }$de$( { \ddot { X } } - N ) \times ( X - N )$.

Elle est engendree par sa trace dans l’ouvert´

$$
\operatorname{Cht} _ {N} ^ {r, \overline {{p}} \leq p} / a ^ {\mathbb {Z}} \times \operatorname{Cht} _ {N} ^ {r, \overline {{p}} \leq p} / a ^ {\mathbb {Z}}.
$$

Enfin, la première projection de cette trace sur$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$est represen-´ table etale au-dessus d’un ouvert de´$( X - T _ { f } ) \times ( \ddot { X } - T _ { f } )$qui contient $\Lambda _ { f } = \Lambda \times _ { X \times X } ( X - T _ { f } ) \times ( X - T _ { f } )$et ne depend que de´$t = u - s .$!"

De la même façon, si$p \leq q$sont deux polygones de troncature assez convexes en fonction de X et N et$d \in \mathbb { Z }$est un degre, on peut consid´ erer la´ correspondance dans$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } \times _ { ( X - N ) \times ( X - N ) } \overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq q } } }$(ou eventuellement´ $\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } \times _ { ( X - N ) \times ( X - N ) } \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq q } )$qui normalise le graphe de l’inclusion $\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } \hookrightarrow \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq q }$

Dans chaque$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } } , \overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$designe l’ouvert d´ efini en demandant´ que non seulement le pôle et le zero mais aussi les d´ eg´ en´ erateurs de chtoucas´ iter´ es´ evitent le niveau´ N. Rappelons que d’après le corollaire III.14, le morphisme

$$
\overline {{\mathrm{Cht} _ {N} ^ {r , d , \overline {{p}} \leq p}}} ^ {\prime} \rightarrow (X - N) \times (X - N) \times \mathbb {A} ^ {r - 1} / \mathbb {G} _ {m} ^ {r - 1}
$$

est lisse dès que p est assez convexe en fonction de X et N.

La suite du present paragraphe 2 est consacr´ ee à la d´ emonstration du´ theorème suivant :´

Theor´ eme V.14.\` – Soit$p : [ 0 , r ] \to \mathbb { R } _ { + }$un polygone de troncature assez convexe enfonction de X et N. Alors :

(i) Pour tout autre tel polygone$q \geq p$et tout degre´$d \in \mathbb { Z }$, la correspondance dans$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } \times _ { ( X - N ) \times ( X - N ) } \overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq q } } }$qui normalise le graphe de l’inclusion$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } \hookrightarrow \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq q }$envoie$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p ^ { \prime } } } }$dans $\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq q } } }$et inversement.

(ii) Pour tous entiers$s , u \in \mathbb { N }$et toute fonction$f \in \mathcal { H } _ { N } ^ { r } / a ^ { \mathbb { Z } }$, la correspondance normalisee´$f \times { \mathrm { F r o b } } _ { \infty } ^ { s } \times { \mathrm { F r o b } } _ { 0 } ^ { u }$dans$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z }$stabilise dans les deux sens l’ouvert$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } } } } / a ^ { \mathbb Z }$!"

## b) Deg´ en´ erateurs des chtoucas d´ eg´ en´ er´ es´

Afin de demontrer le th´ eorème V.14, il nous faut´ etudier concrètement la´ façon dont les chtoucas deg´ enèrent, comme dans le paragraphe 2 de l’article´ [Lafforgue, 1998].

Considerons donc un chtouca´$\widetilde { \mathcal { E } } = ( \mathcal { E } \hookrightarrow \mathcal { E } ^ { \prime } \iff \mathcal { E } ^ { \prime \prime } \widetilde {  } \mathit { \tau } ^ { \tau } \mathcal { E } )$de rang r sur le corps des fractions$K _ { A }$d’un anneau de valuation discrète A. On note $\pi _ { A }$une uniformisante de A et$\kappa _ { A } = A / \pi _ { A } A$son corps residuel. L’anneau´ local$A _ { X }$du point gen´ erique de la courbe´$X \otimes \kappa _ { A }$dans la surface$X \otimes A$ est aussi un anneau de valuation discrète qui admet$\pi _ { A }$pour uniformisante ; son corps des fractions$K _ { A _ { X } }$est le corps des fonctions de$X \otimes A$et son corps residuel´$\kappa _ { A _ { X } }$est le corps des fonctions de$X \otimes \kappa _ { A }$

La fibre gen´ erique´ V de$\widetilde { \mathcal E }$est un ϕ-espace de dimension r sur$K _ { A _ { X } }$au sens de Drinfeld (voir le paragraphe 2a de [loc. cit.]).

Soit M un$\varphi \mathrm { - r e s e a u }$iter´ e dans´ V (au sens de [loc. cit.], paragraphe 2a, definition 1). Il lui est associ´ e en particulier une partition´$\underline { { r } } = ( r = r _ { 1 } +$ $\cdots + r _ { k } )$de l’entier r.

Le reseau´ M de V permet de prolonger$\mathcal { E } \hookrightarrow \mathcal { E } ^ { \prime } \hookrightarrow \mathcal { E } ^ { \prime \prime }$en

$$
\mathcal {E} (M) \hookrightarrow \mathcal {E} ^ {\prime} (M) \leftarrow \mathcal {E} ^ {\prime \prime} (M)
$$

où$\mathcal { E } ( M ) , \mathcal { E } ^ { \prime } ( M ) , \mathcal { E } ^ { \prime \prime } ( M )$sont trois fibres localement libres de rang´ r sur $X \otimes A$et$\mathcal { E } ( M ) \hookrightarrow \mathcal { E } ^ { \prime } ( M ) , \mathcal { E } ^ { \prime \prime } ( M ) \hookrightarrow \mathcal { E } ^ { \prime } ( M )$sont deux plongements dont les conoyaux sont supportes par les graphes de deux morphismes´$\infty , 0 :$ Spec$A  X$et sont libres de rang 1 sur A. On note$\mathcal { E } ^ { M } \hookrightarrow \mathcal { E } ^ { \prime M } \longleftrightarrow \mathcal { E } ^ { \prime \prime M }$ la restriction à$X \otimes \kappa _ { A }$de ce diagramme.

Tout el´ ement´$s \in \underline { { r } } ^ { + } = \{ r _ { 1 } , r _ { 1 } + r _ { 2 } , \ldots , r \}$a un pred´ ecesseur´$s ^ { - } \in \underline { { r } } ^ { - } =$ $\{ 0 , r _ { 1 } , \ldots , r _ { 1 } + \cdot \cdot \cdot + r _ { k - 1 } \}$et tout el´ ement´$s \in \underline { r } ^ { - }$a un successeur$s ^ { + } \in \underline { { r } } ^ { + }$ L’espace$V ^ { M } = M / \pi _ { A } M$de dimension r sur$\kappa _ { A _ { X } }$est muni de

$$
(V _ {s} ^ {M}) _ {s \in \underline {{r}} ^ {-} \cup \underline {{r}} ^ {+}}
$$

$$
V ^ {M}
$$

$$
V _ {s} ^ {M}
$$

• une filtration decroissante´$( \overline { { V } } _ { s } ^ { M } ) _ { s \in \underline { { r } } ^ { - } \cup \underline { { r } } ^ { + } } \mathrm { d e } ^ { \tau } V ^ { M }$qui verifie´$\boldsymbol { \tau } { \boldsymbol { V } } _ { s } ^ { M } = { \overline { { { \boldsymbol { V } } } } _ { s } ^ { M } }$⊕ τ${ V _ { s } ^ { M } } , \forall s$

• des isomorphismes

$$
\overline {{{V}}} _ {s ^ {-}} ^ {M} / \overline {{{V}}} _ {s} ^ {M} \stackrel {{\sim}} {{\longrightarrow}} V _ {s} ^ {M} / V _ {s ^ {-}} ^ {M}, \quad s \in \underline {{{r}}} ^ {+}.
$$

Comme$V ^ { M }$s’identifie à la fibre gen´ erique de´$\mathcal { E } ^ { M } , \mathcal { E } ^ { \prime M }$et$\mathcal { E } ^ { \prime \prime M }$, on a des filtrations induites par des sous-fibres maximaux´

$( \mathcal { E } _ { s } ^ { M } )$de E<sup>M</sup>, (E	<sup>M</sup>) de E	<sup>M</sup>, (E		<sup>M</sup>) de$\mathcal { E } ^ { \prime \prime M }$,

$( \overline { { \mathcal { E } } } _ { s } ^ { M } )$de$\tau _ { \mathcal { E } } M$avec

$$
\forall s, \quad {} ^ {\tau} \mathcal {E} ^ {M} = \overline {{\mathcal {E}}} _ {s} ^ {M} \oplus {} ^ {\tau} \mathcal {E} _ {s} ^ {M} \text {   génériquement },
$$

• plus des isomorphismes bien definis g´ en´ eriquement´

$$
\overline {{\mathcal {E}}} _ {s ^ {-}} ^ {M} / \overline {{\mathcal {E}}} _ {s} ^ {M} \stackrel {{\sim}} {{\longrightarrow}} \mathcal {E} _ {s} ^ {\prime \prime M} / \mathcal {E} _ {s ^ {-}} ^ {\prime \prime M}.
$$

On rappelle enfin qu’un sous-espace W de$V ^ { M }$est dit bon s’il existe $s \in \underline { { r } } ^ { + }$tel que$V _ { s ^ { - } } ^ { M } \subsetneq W \subsetneq V _ { s } ^ { M }$et que l’isomorphisme$\overline { { V } } _ { s ^ { - } } ^ { M } / \overline { { V } } _ { s } ^ { M } \stackrel { \sim } { \to } V _ { s } ^ { M } / V _ { s ^ { - } } ^ { M }$ se restreigne en$\overline { { { V } } } _ { s ^ { - } } ^ { M } \cap \ ^ { \tau } W \ { \overset { \sim } { \to } } \ W / V _ { s ^ { - } } ^ { M }$. Il induit des sous-fibrés maximaux $\mathcal { E } _ { w } ^ { M } , \mathcal { E } _ { w } ^ { \prime M } , \mathcal { E } _ { w } ^ { \prime \prime M }$de rang w = dim W dans$\mathcal { E } ^ { M } , \mathcal { E } ^ { \prime M } , \mathcal { E } ^ { \prime \prime M }$

Le diagramme$\mathcal { E } ^ { M } \hookrightarrow \mathcal { E } ^ { \prime M } \iff \mathcal { E } ^ { \prime \prime M }$muni des structures induites par $\widetilde { \mathcal E }$via le ϕ-reseau it´ er´ e´ M est appele un chtouca d´ eg´ en´ er´ e ; ce n’est pas´ necessairement un chtouca it´ er´ e. Mais même si l’on ne s’int´ eresse qu’aux´ chtoucas iter´ es, pour aller de l’un à l’autre par une suite de transformati´ ons el´ ementaires du´ ϕ-reseau it´ er´ e´ M, on n’evite pas en g´ en´ eral de passer par´ des chtoucas deg´ en´ er´ es qui ne sont pas des chtoucas it´ er´ es. Afin de suivre´ les deg´ en´ erateurs le long de telles transformations, on doit donc g´ en´ eraliser´ leur definition aux chtoucas d´ eg´ en´ er´ es :´

Lemme V.15. – Considerons le chtouca d´ eg´ en´ er´ e´$\widetilde { \mathcal { E } } ^ { M } = ( \mathcal { E } ^ { M } \hookrightarrow \mathcal { E } ^ { \prime M } \longleftrightarrow$ $\mathcal { E } ^ { \prime \prime M } , \ldots )$induit par un ϕ-reseau it´ er´ e M de V comme plus haut. Alors :´

(i) Pour tout$s \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + }$, l’isomorphisme bien defini g´ en´ eriquement´

$$
\det \left(^ {\tau} \mathcal {E} _ {s} ^ {M}\right) \xrightarrow {\sim} \det \left(\mathcal {E} _ {s} ^ {M}\right)
$$

s’etend en un isomorphisme partout bien d´ efini´

$$
\det \left(^ {\tau} \mathcal {E} _ {s} ^ {M}\right) \stackrel {{\sim}} {{\longrightarrow}} \det \left(\mathcal {E} _ {s} ^ {M}\right) \left(\infty (\widetilde {\mathcal {E}} ^ {M}) - x \left(\mathcal {E} _ {s} ^ {M}\right)\right)
$$

où$\infty ( \widetilde { \mathcal { E } } ^ { M } ) \in X ( \kappa _ { A } )$est le pôle de$\widetilde { \mathcal { E } } ^ { M }$et$x ( \mathcal { E } _ { s } ^ { M } ) \in X ( \kappa _ { A } )$est un point  uniquement determin´ e, appel´ e le d´ eg´ en´ erateur en rang s.´ Cette definition g´ en´ eralise celle pour les chtoucas it´ er´ es.´

(ii) Plus gen´ eralement, si W est un bon sous-espace de´$V ^ { M }$avec$V _ { s ^ { - } } ^ { M } \subsetneq$ $W \subseteq V _ { s } ^ { M }$et$\mathcal { E } _ { w } ^ { M }$est le sous-fibre maximal de´$\mathcal { E } ^ { M }$associe, on a un´ isomorphisme canonique

$$
\det \left(^ {\tau} \mathcal {E} _ {w} ^ {M}\right) \stackrel {{\sim}} {{\longrightarrow}} \det \left(\mathcal {E} _ {w} ^ {M}\right) \left(\infty (\widetilde {\mathcal {E}} ^ {M}) - x \left(\mathcal {E} _ {w} ^ {M}\right)\right)
$$

avec suivant les cas

$$
x \big (\mathcal {E} _ {w} ^ {M} \big) = x \big (\mathcal {E} _ {s} ^ {M} \big) o u x \big (\mathcal {E} _ {w} ^ {M} \big) = x \big (\mathcal {E} _ {s ^ {-}} ^ {M} \big).
$$

Demonstration :´ (i) La flèche det$( ^ { \tau } \mathcal { E } ^ { M } / \overline { { \mathcal { E } } } _ { s } ^ { M } ) \hookrightarrow \operatorname* { d e t } ( \mathcal { E } _ { s } ^ { \prime \prime M } )$est partout bien definie car il en est ainsi de´$\Lambda ^ { s } ( { } ^ { \tau } \mathcal { E } ( M ) ) \to \Lambda ^ { s } \mathcal { E } ^ { \prime \prime } ( M )$et donc de sa restriction$\Lambda ^ { s } ( ^ { \tau } \mathcal { E } ^ { M } ) \to \Lambda ^ { s } \mathcal { E } ^ { \prime \prime M }$qui se factorise à travers le quotient det$( { } ^ { \tau } \mathcal { E } ^ { M } / \overline { { \mathcal { E } } } _ { s } ^ { M } )$ de$\Lambda ^ { s } ( ^ { \tau } \mathcal { E } ^ { M } )$et le sous-fibre maximal det´$( \mathcal { E } _ { s } ^ { \prime \prime M } )$de$\Lambda ^ { s } \mathcal { E } ^ { \prime \prime M }$. Ainsi a-t-on une suite de plongements partout bien definis´

$$
\det \left(^ {\tau} \mathcal {E} _ {s} ^ {M}\right) \hookrightarrow \det \left(^ {\tau} \mathcal {E} ^ {M} / \overline {{\mathcal {E}}} _ {s} ^ {M}\right) \hookrightarrow \det \left(\mathcal {E} _ {s} ^ {\prime \prime M}\right) \hookrightarrow \det \left(\mathcal {E} _ {s} ^ {\prime M}\right) \hookleftarrow \det \left(\mathcal {E} _ {s} ^ {M}\right).
$$

De plus, le conoyau du plongement det$( \mathcal { E } _ { s } ^ { M } ) \hookrightarrow \operatorname* { d e t } ( \mathcal { E } _ { s } ^ { \prime M } )$est de dimension$\leq 1$et supporte par´$\infty ( \widetilde { \mathcal { E } } ^ { M } )$puisque$\mathcal { E } ^ { \prime M } / \mathcal { E } ^ { M }$est de dimension 1 et supporte par ´$\infty ( \widetilde { \mathcal { E } } ^ { M } )$. D’où l’assertion concernant$\mathcal { E } _ { s } ^ { M }$

Si$\widetilde { \mathcal { E } } ^ { M }$est un chtouca iter´ e, notons´$\infty = x _ { 0 }$son pôle,$0 = x _ { r }$son zero´ et$x _ { s } , s \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + }$, ses deg´ en´ erateurs. Ceux-ci sont d´ efinis en disant que´ pour tout$s ^ { - } \in \underline { { r } } ^ { + } , \mathcal { E } _ { s } ^ { M } / \mathcal { E } _ { s ^ { - } } ^ { M }$est muni d’une structure de chtouca (à droite si $s = 0 ^ { + } = r _ { 1 }$, à gauche sinon) de pôle$x _ { s ^ { - } }$et de zero´$x _ { s }$. Les determinants´ sont des chtoucas de rang 1 munis d’isomorphismes

$$
{ } ^ { \tau } \operatorname* { d e t } \left( \mathcal { E } _ { s } ^ { M } / \mathcal { E } _ { s ^ { - } } ^ { M } \right) \xrightarrow { \sim } \operatorname* { d e t } \left( \mathcal { E } _ { s } ^ { M } / \mathcal { E } _ { s ^ { - } } ^ { M } \right) ( x _ { s ^ { - } } - x _ { s})
$$

dont les produits tensoriels s’ecrivent´

$$
\det \left(^ {\tau} \mathcal {E} _ {s} ^ {M}\right) \stackrel {{\sim}} {{\longrightarrow}} \det \left(\mathcal {E} _ {s} ^ {M}\right) (\infty - x _ {s}).
$$

(ii) Si W est un bon sous-espace de$V ^ { M }$de rang w avec$V _ { s ^ { - } } ^ { M } \subsetneq W \subsetneq V _ { s } ^ { M }$et $\mathcal { E } _ { w } ^ { M } , \mathcal { E } _ { w } ^ { \prime M } , \mathcal { E } _ { w } ^ { \prime \prime M }$sont les sous-fibres maximaux de´$\mathcal { E } ^ { M } , \mathcal { E } ^ { \prime M } , \mathcal { E } ^ { \prime \prime M }$dont la fibre gen´ erique est´ W, considerons le diagramme commutatif suivant :´

![](images/page_135_image_6.jpg)

On sait dejà que (4) et (7) sont bien d´ efinies g´ en´ eriquement et que´ les autres flèches sont bien definies partout. Comme (2) est une flèche de´ quotient par un sous-fibre maximal et (3) est le plongement´$\mathrm { d } '$un sous-fibre´ maximal, la flèche (4) est bien definie partout. Puis, (5)´ etant le plongement´ $\mathrm { d } '$un sous-fibre et (6) le plongement´$\mathrm { d } ^ { \circ } \mathrm { u n }$sous-fibre maximal, (7) est bien´ definie partout.´

Ainsi a-t-on une suite de plongements partout bien definis´

$$
\det \left(^ {\tau} \mathcal {E} _ {w} ^ {M}\right) \hookrightarrow \det \left(\mathcal {E} _ {w} ^ {\prime \prime M}\right) \hookrightarrow \det \left(\mathcal {E} _ {w} ^ {\prime M}\right) \hookleftarrow \det \left(\mathcal {E} _ {w} ^ {M}\right)
$$

et il existe un unique point$x ( \mathcal { E } _ { w } ^ { M } ) \in X ( \kappa _ { A } )$tel que

$$
\det \left(^ {\tau} \mathfrak {E} _ {w} ^ {M}\right) \stackrel {{\sim}} {{\longrightarrow}} \det \left(\mathfrak {E} _ {w} ^ {M}\right) \left(\infty (\widetilde {\mathfrak {E}} ^ {M}) - x \left(\mathfrak {E} _ {w} ^ {M}\right)\right).
$$

Il reste à voir que$x ( \mathcal { E } _ { w } ^ { M } ) = x ( \mathcal { E } _ { s } ^ { M } )$ou$x ( \mathcal { E } _ { s ^ { - } } ^ { M } )$c’est-à-dire qu’en dehors des points$x ( \mathcal { E } _ { s } ^ { M } )$et$x ( \mathcal { E } _ { s ^ { - } } ^ { M } )$le plongement det$( ^ { \tau } \mathcal { E } _ { w } ^ { M } ) \hookrightarrow \operatorname* { d e t } ( \mathcal { E } _ { w } ^ { \prime M } )$est un isomorphisme. En dehors de ces deux points, les six flèches

$$
{ } ^ { \tau } \mathcal { E } _ { s ^ { - } } ^ { M } \hookrightarrow { } ^ { \tau } \mathcal { E } ^ { M } / \overline { { \mathcal { E } } } _ { s ^ { - } } ^ { M } , \operatorname * { d e t } \left( { } ^ { \tau } \mathcal { E } ^ { M } / \overline { { \mathcal { E } } } _ { s ^ { - } } ^ { M } \right) \hookrightarrow \operatorname * { d e t } \left( \mathcal { E } _ { s ^ { - } } ^ { \prime \prime M } \right) , \mathcal { E } _ { s ^ { - } } ^ { \prime \prime M } \hookrightarrow \mathcal { E } _ { s ^ { - } } ^ { \prime M } ,
$$

$$
{ } ^ { \tau } \mathcal { E } _ { s } ^ { M } \hookrightarrow { } ^ { \tau } \mathcal { E } ^ { M } / \overline { { \mathcal { E } } } _ { s } ^ { M } , \operatorname * { d e t } \left( { } ^ { \tau } \mathcal { E } ^ { M } / \overline { { \mathcal { E } } } _ { s } ^ { M } \right) \hookrightarrow \operatorname * { d e t } \left( \mathcal { E } _ { s } ^ { \prime \prime M } \right) , \mathcal { E } _ { s } ^ { \prime \prime M } \hookrightarrow \mathcal { E } _ { s } ^ { \prime M }
$$

sont des isomorphismes. Il en est alors de même de$\mathcal { E } _ { w } ^ { \prime \prime M } \hookrightarrow \mathcal { E } _ { w } ^ { \prime M }$et de $\begin{array} { r } { \boldsymbol { \tau } \boldsymbol { \mathcal { E } } _ { w } ^ { M } / \boldsymbol { \tau } \boldsymbol { \mathcal { E } } _ { w } ^ { M } \cap \overline { { \boldsymbol { \mathcal { E } } } } _ { s ^ { - } } ^ { M } \hookrightarrow \boldsymbol { \tau } \boldsymbol { \mathcal { E } } ^ { M } / \overline { { \boldsymbol { \mathcal { E } } } } _ { s ^ { - } } ^ { M } } \end{array}$puisque$\mathcal { E } _ { w } ^ { M } \supset \mathcal { E } _ { s ^ { - } } ^ { M }$

Comme dans cet ouvert det$( ^ { \tau } \mathcal { E } ^ { M } / \overline { { \mathcal { E } } } _ { s ^ { - } } ^ { M } ) \hookrightarrow \operatorname* { d e t } ( \mathcal { E } _ { s ^ { - } } ^ { \prime \prime M } )$est un isomorphisme, le plongement$\overline { { \mathcal { E } } } _ { s ^ { - } } ^ { M } / \overline { { \mathcal { E } } } _ { s } ^ { M } \hookrightarrow \mathcal { E } _ { s } ^ { \prime \prime M } / \mathcal { E } _ { s ^ { - } } ^ { \prime \prime M }$est partout bien defini et´${ \mathrm { c } } ^ { \prime }$est un isomorphisme puisque det$( ^ { \tau } \mathcal { E } ^ { M } / \overline { { \mathcal { E } } } _ { s } ^ { M } ) \hookrightarrow \operatorname* { d e t } ( \mathcal { E } _ { s } ^ { \prime \prime M } )$est aussi un isomorphisme. Donc le plongement entre sous-fibres maximaux´$\tau _ { \mathcal { E } _ { w } ^ { M } \cap \overline { { \mathcal { E } } } _ { s ^ { - } } } \hookrightarrow$ $\hat { \mathcal { E } } _ { w } ^ { \prime \prime M } / \mathcal { E } _ { s ^ { - } } ^ { \prime \prime M }$est lui-même un isomorphisme.

Finalement, on a en dehors de$x ( \mathcal { E } _ { s } ^ { M } ) \operatorname { e t } x ( \mathcal { E } _ { s ^ { - } } ^ { M } )$

$$
\begin{array}{l} \det \left(^ {\tau} \mathcal {E} _ {w} ^ {M}\right) = \det \left(^ {\tau} \mathcal {E} _ {w} ^ {M} / ^ {\tau} \mathcal {E} _ {w} ^ {M} \cap \overline {{\mathcal {E}}} _ {s ^ {-}} ^ {M}\right) \otimes \det \left(^ {\tau} \mathcal {E} _ {w} ^ {M} \cap \overline {{\mathcal {E}}} _ {s ^ {-}} ^ {M}\right) \\ \qquad \cong \det \left(^ {\tau} \mathcal {E} ^ {M} / \overline {{\mathcal {E}}} _ {s ^ {-}} ^ {M}\right) \otimes \det \left(^ {\tau} \mathcal {E} _ {w} ^ {M} \cap \overline {{\mathcal {E}}} _ {s ^ {-}} ^ {M}\right) \\ \qquad \cong \det \left(\mathcal {E} _ {s ^ {-}} ^ {\prime \prime M}\right) \otimes \det \left(\mathcal {E} _ {w} ^ {\prime \prime M} / \mathcal {E} _ {s ^ {-}} ^ {\prime \prime M}\right) = \det \left(\mathcal {E} _ {w} ^ {\prime \prime M}\right) \\ \qquad \cong \det \left(\mathcal {E} _ {w} ^ {\prime M}\right). \end{array}
$$

$\mathbf { C } '$est ce qu’on voulait.

## c) Effet des transformations de ϕ-reseaux it´ er´ es sur les d´ eg´ en´ erateurs´

Considerons toujours un´ ϕ-reseau it´ er´ e´ M dans V de partition associee´$\underline { r }$et W un bon sous-espace de$V ^ { M }$de dimension w.

D’après la proposition 6 du paragraphe 2a de [loc. cit.],$M ^ { \prime } = \mathrm { K e r } [ M \to$ $M / \pi _ { A } \hat { M } = V ^ { \hat { M } } \hat {  } V ^ { M } / W ]$est aussi un ϕ-reseau it´ er´ e dans´ V. La partition $\underline { { r } } ^ { \prime }$de r associee à´ M	 est le raffinement de r defini par´$\underline { { r } } ^ { \prime + } = \underline { { r } } ^ { + } \cup \bar { \{ w \} }$

D’après le lemme 10 et la proposition 11(i) du paragraphe 2c de [loc. cit.], on a deux plongements

$$
\mathcal {E} _ {w} ^ {M ^ {\prime}} \hookrightarrow \mathcal {E} _ {w} ^ {M}, \mathcal {E} ^ {M} / \mathcal {E} _ {w} ^ {M} \longrightarrow \mathcal {E} ^ {M ^ {\prime}} / \mathcal {E} _ {w} ^ {M ^ {\prime}}
$$

dont les conoyaux sont de même dimension 0 ou 1 sur$\kappa _ { A }$et deux suites exactes canoniques

$$
0 \longrightarrow \overline {{\mathcal {E}}} _ {w} ^ {M ^ {\prime}} \longrightarrow {} ^ {\tau} \mathcal {E} ^ {M ^ {\prime}} \longrightarrow {} ^ {\tau} \mathcal {E} _ {w} ^ {M} \longrightarrow 0,
$$

$$
0 \longrightarrow {} ^ {\tau} \mathcal {E} _ {w} ^ {M} \longrightarrow {} ^ {\tau} \mathcal {E} ^ {M} \longrightarrow \overline {{\mathcal {E}}} _ {w} ^ {M ^ {\prime}} \longrightarrow 0.
$$

On voit en particulier que pour tout$s \in \underline { { r } } ^ { \prime + }$

$$
\deg \mathcal {E} _ {s} ^ {M} - \deg \mathcal {E} _ {s} ^ {M ^ {\prime}}
$$

est egal à 0 ou 1.´

Lemme V.16. – Soit M	 le transforme de M par un bon sous-espace W de´ $V ^ { M }$comme ci-dessus. Alors pour tout$s \in \underline { { r } } ^ { \prime + }$, on a

$$
x \left(\mathcal {E} _ {s} ^ {M ^ {\prime}}\right) = x \left(\mathcal {E} _ {s} ^ {M}\right) \quad s i \quad \deg \mathcal {E} _ {s} ^ {M} = \deg \mathcal {E} _ {s} ^ {M ^ {\prime}}
$$

et

$$
x \left(\mathcal {E} _ {s} ^ {M ^ {\prime}}\right) = \operatorname{Frob} \left(x \left(\mathcal {E} _ {s} ^ {M}\right)\right) s i \deg \mathcal {E} _ {s} ^ {M} = \deg \mathcal {E} _ {s} ^ {M ^ {\prime}} + 1.
$$

Remarque : Dans la demonstration du lemme 16(i) du paragraphe 2d de´ [loc. cit.] on a dejà invoqu´ e la propri´ et´ e plus faible que si´$N \hookrightarrow X$est un niveau qui evite les sp´ ecialisations du pôle et du z´ ero et si´$M ^ { \prime }$est le transforme de´ M par un bon sous-espace W de$V ^ { M }$, alors aucun des homomorphismes induits

$$
u _ {s}: ^ {\tau} \Lambda^ {s} (\mathcal {E} (M) \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N}) \to \Lambda^ {s} (\mathcal {E} (M) \otimes_ {\mathcal {O} _ {X}} \mathcal {O} _ {N}), 1 \leq s \leq r,
$$

n’est nilpotent, même après reduction modulo´$\pi _ { A }$(ce qui equivaut à dire que´ tous les deg´ en´ erateurs de´ M evitent´$N )$si et seulement si${ \mathrm { c } } '$est vrai pour$M ^ { \prime }$ Cela resulte simplement de ce que, d’après le lemme 10 du paragraph´ e 2c de [loc. cit.], les transformations$\mathbf { \ddot { a } }$la Langton” des fibres´ E(M) commutent avec le foncteur ·$\bigotimes _ { \mathcal { O } _ { X } } \mathcal { O } _ { N }$de restriction des fibres de´ X à N.

Demonstration :´ Soit donc$s \in \underline { r } ^ { \prime + }$. Notons$\infty = \infty ( \widetilde { \mathcal { E } } ^ { M } ) = \infty ( \widetilde { \mathcal { E } } ^ { M ^ { \prime } } )$ $0 = 0 ( \widetilde { \mathcal { E } } ^ { M } ) = 0 ( \widetilde { \mathcal { E } } ^ { M ^ { \prime } } ) , x = x ( \mathcal { E } _ { s } ^ { M } ) \mathrm { ~ e t ~ } x ^ { \prime } = x ( \mathcal { E } _ { s } ^ { M ^ { \prime } } ) |$

 Par definition de´ x et$x ^ { \prime }$, on a

$$
\det \left(^ {\tau} \mathcal {E} _ {s} ^ {M}\right) \cong \det \left(\mathcal {E} _ {s} ^ {M}\right) (\infty - x),
$$

$$
\det \left(^ {\tau} \mathcal {E} _ {s} ^ {M ^ {\prime}}\right) \cong \det \left(\mathcal {E} _ {s} ^ {M ^ {\prime}}\right) (\infty - x ^ {\prime})
$$

et aussi$\operatorname * { d e t } ( { } ^ { \tau } \mathcal { E } ^ { M } ) \otimes \operatorname * { d e t } ( \mathcal { E } ^ { M } ) ^ { - 1 } \cong \mathcal { O } ( \infty - 0 ) \cong \operatorname * { d e t } ( { } ^ { \tau } \mathcal { E } ^ { M ^ { \prime } } ) \otimes \operatorname * { d e t } ( \mathcal { E } ^ { M ^ { \prime } } ) ^ { - 1 }$

Si deg$\mathcal { E } _ { s } ^ { M } = \deg \mathcal { E } _ { s } ^ { M ^ { \prime } }$, on a$\mathcal { E } _ { s } ^ { M ^ { \prime } } \cong \mathcal { E } _ { s } ^ { M }$si$s ~ \leq ~ w$[resp.$\mathcal { E } ^ { M } / \mathcal { E } _ { s } ^ { M } \ \cong$ $\mathcal { E } ^ { M ^ { \prime } } / \mathcal { E } _ { s } ^ { M ^ { \prime } }$si$s \geq w ]$et donc$x ^ { \prime } = x$

Si au contraire deg$\mathcal { E } _ { s } ^ { M } = \mathrm { d e g } \mathcal { E } _ { s } ^ { M ^ { \prime } } + 1$, il existe un point$y \in X ( \kappa _ { A } )$tel que det$( \mathcal { E } _ { s } ^ { M } ) \cong \operatorname* { d e t } ( \mathcal { E } _ { s } ^ { M ^ { \prime } } ) ( y )$[resp. det$( \mathcal { E } ^ { M ^ { \prime } } / \mathcal { E } _ { s } ^ { M ^ { \prime } } ) \cong \operatorname* { d e t } ( \mathcal { E } ^ { M } / \mathcal { E } _ { s } ^ { M } ) ( y ) ]$et il s’agit de prouver que$y = x \mathrm { \ o u }$, ce qui revient au même,$\tau ( y ) = x ^ { \prime }$

Mais d’après la suite exacte

$$
0 \longrightarrow \overline {{\mathcal {E}}} _ {w} ^ {M ^ {\prime}} \longrightarrow {} ^ {\tau} \mathcal {E} ^ {M ^ {\prime}} \longrightarrow {} ^ {\tau} \mathcal {E} _ {w} ^ {M} \longrightarrow 0
$$

[resp.

$$
0 \longrightarrow {} ^ {\tau} \mathcal {E} _ {w} ^ {M} \longrightarrow {} ^ {\tau} \mathcal {E} ^ {M} \longrightarrow \overline {{\mathcal {E}}} _ {w} ^ {M ^ {\prime}} \longrightarrow 0 ],
$$

on a un plongement

$$
{ } ^ { \tau } \mathcal { E } _ { s } ^ { M } \hookrightarrow { } ^ { \tau } \mathcal { E } ^ { M ^ { \prime } } / \overline { { \mathcal { E } } } _ { s } ^ { M ^ { \prime } }
$$

puis

$$
{ } ^ { \tau } \mathcal { E } _ { s } ^ { M } / { } ^ { \tau } \mathcal { E } _ { s } ^ { M ^ { \prime } } \hookrightarrow { } ^ { \tau } \mathcal { E } ^ { M ^ { \prime } } / \left( { } ^ { \tau } \mathcal { E } _ { s } ^ { M ^ { \prime } } \oplus \overline { { \mathcal { E } } } _ { s } ^ { M ^ { \prime } } \right)
$$

resp. un epimorphisme´

$$
{ } ^ { \tau } \mathcal { E } ^ { M ^ { \prime } } / \left( { } ^ { \tau } \mathcal { E } _ { s } ^ { M ^ { \prime } } \oplus \overline { { \mathcal { E } } } _ { s } ^ { M ^ { \prime } } \right) \longrightarrow { } ^ { \tau } \left( \mathcal { E } ^ { M ^ { \prime } } / \mathcal { E } _ { s } ^ { M ^ { \prime } } \right) / { } ^ { \tau } \left( \mathcal { E } ^ { M } / \mathcal { E } _ { s } ^ { M } \right) ]
$$

et comme$\tau  \& ^ { M ^ { \prime } } / ( ^ { \tau } \mathcal { E } _ { s } ^ { M ^ { \prime } } \oplus \overline { { \mathcal { E } } } _ { s } ^ { M ^ { \prime } } )$est supporte par´$x ^ { \prime } .$, on conclut$\tau ( y ) = x ^ { \prime }$. !"

Si M est un ϕ-reseau it´ er´ e dans la fibre g´ en´ erique´ V du chtouca$\widetilde { \varepsilon } =$ $( \mathcal { E } \ \hookrightarrow \ \mathcal { E } ^ { \prime } \  \ \mathcal { E } ^ { \prime \prime } \ \tilde {  } \ \tau \mathcal { E } )$sur$K _ { A }$, on notera$\underline { { x } } ( M )$ou$\underline { { x } } ( \widetilde { \mathcal { E } } ^ { M } )$le sousensemble fini de$X ( \kappa _ { A } )$constitue du pôle´${ \infty } ( \widetilde { \mathcal { E } } ^ { \overline { { M } } } )$, du zero´$0 ( \widetilde { \mathcal { E } } ^ { M } )$et des deg´ en´ erateurs´$x ( \mathcal { E } _ { s } ^ { M } )$

Nous allons deduire des lemmes V.15 et V.16 :´

Proposition V.17. – Soient M et$M ^ { \prime }$deux ϕ-reseaux it´ er´ es dans la fibre´ gen´ erique V d’un chtouca´$\widetilde { \mathcal { E } } = ( \mathcal { E } \hookrightarrow \mathcal { E } ^ { \prime } \hookleftarrow \mathcal { E } ^ { \prime \prime } \widetilde {  } \ ^ { \tau } \mathcal { E } )$sur$K _ { A }$

Alors pour tout$x \in \underline { { x } } ( M )$, il existe$x ^ { \prime } \in \underline { { x } } ( M ^ { \prime } )$et deux entiers n,$n ^ { \prime } \in \mathbb { N }$ tels que

$$
\operatorname{Frob} ^ {n} (x) = \operatorname{Frob} ^ {n ^ {\prime}} \left(x ^ {\prime}\right).
$$

Demonstration :´ On sait d’après le lemme V.16 et le lemme V.15(ii) que cet enonc´ e est vrai quand´$M ^ { \prime }$est le transforme de´ M par un bon sous-espace W de$M / \pi _ { A } M = \hat { V } ^ { M }$ou l’inverse (auquel cas on dit que$M ^ { \prime }$est un transforme´ reciproque de´ M). Il est vrai aussi quand M et M	 peuvent être relies l’un´ à l’autre par une chaîne de telles transformations el´ ementaires directes ou´ reciproques.´

Pour conclure, il suffit de montrer que deux ϕ-reseaux it´ er´ es arbitraires´ M et$M ^ { \prime }$peuvent toujours être relies par une telle chaîne.´

Choisissons un polygone de troncature p (assez convexe en fonction de X) tel que le chtouca$\widetilde { \mathcal { E } }$soit dans l’ouvert$\mathrm { \overline { { C } h t } } ^ { r , \overline { { p } } \leq p }$de$\operatorname { C h t } ^ { r }$

Et soit M un ϕ-reseau arbitraire dans´ V.

Quitte à remplacer A par une extension finie et M par un ϕ-reseau it´ er´ e´ qui lui est relie, on peut supposer que le type´$\underline { { r } } = ( r = r _ { 1 } + \cdot \cdot \cdot + r _ { k } )$de M est maximal pour l’ordre lexicographique parmi les types des ϕ-reseaux´ iter´ es reli´ es à´ M. Cela signifie que pour toute extension finie$A ^ { \prime }$de A et pour tout ϕ-reseau it´ er´ e´$\bar { M } ^ { \prime }$de$V \otimes _ { K _ { A _ { X } } } K _ { A _ { X } ^ { \prime } }$relie à´$M \otimes _ { A _ { X } } A _ { X } ^ { \prime }$, le type $\underline { { r } } ^ { \prime } = ( r = r _ { 1 } ^ { \prime } + \cdot \cdot \cdot + r _ { k ^ { \prime } } ^ { \prime } )$de$M ^ { \prime }$verifie´

$$
r _ {1} ^ {\prime} \leq r _ {1}
$$

$$
r _ {1} ^ {\prime} + r _ {2} ^ {\prime} \leq r _ {1} + r _ {2} \quad \text { si } \quad r _ {1} ^ {\prime} = r _ {1}
$$

$$
r _ {1} ^ {\prime} + r _ {2} ^ {\prime} + r _ {3} ^ {\prime} \leq r _ {1} + r _ {2} + r _ {3} \mathrm{si} r _ {1} ^ {\prime} = r _ {1}, r _ {2} ^ {\prime} = r _ {2},
$$

etc.

$\mathrm { \AA }$partir d’un tel M, la demonstration du th´ eorème 20(i) du paragraphe 2e´ de [loc. cit.] permet de construire un ϕ-reseau it´ er´ e´ N relie à´ M et qui definit´ un point de$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } ( A )$. En effet, le proced´ e de construction de´ N à partir de M utilise uniquement des transformations el´ ementaires dans un sens ou´ dans l’autre et l’hypothèse qui etait faite dans [loc. cit.] que le type du´ ϕ-reseau it ´ er´ e de d ´ epart soit maximal peut être remplac ´ ee sans rien changer´ dans la demonstration par celle que son type soit maximal parmi ceux d´ es ϕ-reseaux it´ er´ es reli´ es à lui.´

D’après le theorème 20(ii) de [loc. cit.] paragraphe 2e, deux´ ϕ-reseaux´ iter´ es qui d´ efinissent des points de´$\overline { { \operatorname { C h t } ^ { r , \overline { { p } } \leq p } } } ( A )$sont necessairement´ egaux´ et cela montre que tous les ϕ-reseaux it´ er´ es sont reli´ es par des chaînes de´ transformations el´ ementaires.´!"

## d) Effet des correspondances de Hecke sur les deg´ en´ erateurs´

Si$\widetilde { \mathcal E }$est un chtouca iter´ e de type ´$\underline { r }$à valeurs dans un corps, on note$\underline { { x } } ( \widetilde { \mathcal { E } } )$ l’ensemble constitue du pôle´$\infty ( \widetilde { \mathcal { E } } )$, du zero´$0 ( \widetilde { \mathcal { E } } )$et des deg´ en´ erateurs´$x ( \mathcal { E } _ { s } )$, $s \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + }$

Comme consequence de la proposition V.17, on a :´

Corollaire V.18. – Soit$( \widetilde { \mathcal { E } } , \widetilde { \mathcal { F } } )$un couple de chtoucas iter´ es´ (pas neces-´  sairement de même type) à valeurs dans un corps et qui verifie l’une des´ deux hypothèses suivantes :

(1) Il existe deuxpolygones de troncature$q \geq p$(assez convexes enfonction de X) et un entier d$\in \mathbb { Z }$tel que$( \widetilde { \mathcal { E } } , \widetilde { \mathcal { F } } )$soit un point de$\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } } } \times$ $\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \leq q } } }$ adherent au graphe de l’inclusion´$\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } \hookrightarrow \mathrm { C h t } ^ { r , d , \overline { { p } } \leq q }$

(2) Il existe un polygone$p : [ 0 , r ] \to \mathbb { R } _ { + }$(assez convexe enfonction de X), une fonction$\dot { f } \in \mathcal { H } _ { \varnothing } ^ { r } / a ^ { \mathbb { Z } }$et deux entiers$s , u \in \mathbb { N }$tels que$( \widetilde { \mathcal { E } } , \widetilde { \mathcal { F } } )$soit un point de$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } } \times \overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$ supporte par la correspondance´ $f \stackrel { \cdot } { \times } \mathrm { F r o b } _ { \infty } ^ { s } \times \mathrm { F r o b } _ { 0 } ^ { u } .$

Alors pour tout point x de$\underline { { x } } ( \widetilde { \mathcal { E } } )$[resp.$\underline { { x } } ( \widetilde { \mathcal { F } } ) ]$, il existe un point$x ^ { \prime }$de $\underline { { x } } ( \widetilde { \mathcal { F } } ) [ r e s p . \underline { { x } } ( \widetilde { \mathcal { E } } ) ]$et deux entiers n,$n ^ { \prime } \in \mathbb { N }$tels que

$$
\operatorname{Frob} ^ {n} (x) = \operatorname{Frob} ^ {n ^ {\prime}} \left(x ^ {\prime}\right).
$$

Demonstration :´ Dans le cas (1) [resp. (2)], le couple$( \widetilde { \mathcal { E } } , \widetilde { \mathcal { F } } )$peut${ \bf s } '$ecrire´ comme la specialisation d’un point´$( \widetilde { E } _ { K } , \widetilde { F } _ { K } )$de$\mathbf { C h t } ^ { r , \overline { { p } } \leq p } \times \mathbf { C h t } ^ { r , \overline { { p } } \leq p }$defini´  sur le corps des fractions K d’un anneau de valuation discrète A et qui est supporte par le graphe de l’identit´ e [resp. par la correspondance´$f \times$ Frob$\mathbf { \omega } _ { \infty } ^ { s } \times \mathrm { F r o } \bar { \mathbf { b } } _ { 0 } ^ { u }$au-dessus de$( X - T _ { f } ) \times ( \bar { X _ { } } - \bar { T _ { f } } ) \times _ { X \times X } \bar { \Lambda _ { } } ]$

Dans le cas (1), on a donc$\widetilde { \cal E } _ { K } = \widetilde { \cal F } _ { K }$et$\widetilde { \mathcal E }$et$\widetilde { \mathcal F }$sont les specialisations´    associees à deux´ ϕ-reseaux it´ er´ es de la fibre g´ en´ erique de´$\tilde { E } _ { K } = \widetilde { F } _ { K }$. On conclut d’après la proposition V.17.

Dans le cas (2), les chtoucas$\widetilde { E } _ { K }$et$\widetilde { F } _ { K }$qui sont des diagrammes de fibres sur´$X \otimes K$ coïncident en dehors de$T _ { f }$et d’un ensemble fini de transformes du pôle et du z´ ero par des puissances de Frob. En particulier,´ ils ont même fibre gen´ erique´ V et les specialisations´$\widetilde { \mathcal E }$et$\widetilde { \mathcal F }$sont induites par deux ϕ-reseaux it´ er´ es´ M et N dans$\bar { V }$

Notons$\widetilde { \mathcal { G } }$le chtouca deg´ en´ er´ e obtenu par sp´ ecialisation de´$\widetilde { F } _ { K }$le long de M (au lieu de N). Le chtouca iter´ e´$\widetilde { \mathcal { E } } = ( \mathcal { E } \overset { \cdot } { \hookrightarrow } \mathcal { E } ^ { \prime } \overset { \cdot } { \longrightarrow } \mathcal { E } ^ { \prime \prime } )$et le chtouca deg´ en´ er´ e´$\widetilde { \mathcal { g } } = ( \mathcal { g } \hookrightarrow \mathcal { g } ^ { \prime } \hookrightarrow \mathcal { g } ^ { \prime \prime } )$ont même type$\underline { { r } } = ( r = r _ { 1 } + \cdot \cdot \cdot + r _ { k } )$ les diagrammes qui les definissent´$\mathrm {  ~ s ~ } ^ { \prime }$identifient sur un ouvert de la courbe, leurs pôles d’une part et leurs zeros d’autre part diffèrent d’une puissance de´ Frob et d’après la proposition V.17 on a seulement à montrer qu’il en est de même de leurs deg´ en´ erateurs´$x _ { s } = x ( \mathcal { E } _ { s } )$et$x _ { s } ^ { \prime } = x ( \mathcal { G } _ { s } ) , s \in \underline { { r } } ^ { - } \cap \underline { { r } } ^ { + }$. Notant ∞ et$\infty ^ { \prime }$les pôles, on a par definition des isomorphismes canoniques´

$$
\begin{array}{l} ^ {\tau} \det (\mathcal {E} _ {s}) \cong \det (\mathcal {E} _ {s}) (\infty - x _ {s})  , \\ ^ {\tau} \det (\mathcal {G} _ {s}) \cong \det (\mathcal {G} _ {s}) (\infty^ {\prime} - x _ {s} ^ {\prime})  . \end{array}
$$

Comme det$( \mathcal { E } _ { s } )$et det$( \mathcal { G } _ { s } )$s’identifient sur un ouvert, il existe un ensemble fini de points$x _ { \iota }$et de multiplicites´$m _ { \iota } \in \mathbb { Z }$tels que

$$
\det (\mathcal {G} _ {s}) \cong \det (\mathcal {E} _ {s}) \left(\sum_ {\iota} m _ {\iota} \cdot x _ {\iota}\right)
$$

d’où on deduit l’´ egalit´ e entre diviseurs´

$$
\sum_ {\iota} m _ {\iota} \cdot (x _ {\iota} - \tau (x _ {\iota})) = (\infty - \infty^ {\prime}) + (x _ {s} ^ {\prime} - x _ {s}).
$$

Disons que deux points sont equivalents s’ils sont images l’un de l’autre´ par une puissance de Frob. Pour tout indice$\iota , x _ { \iota }$et$\tau ( x _ { \iota } )$sont equivalents,´ de même que ∞ et$\infty ^ { \prime }$. Donc$x _ { s } ^ { \prime }$et$x _ { s }$sont equivalents.´!"

Nous pouvons donner maintenant :

Demonstration du th´ eorème V.14 :´ On considère donc un niveau$N =$ Spec${ \mathcal { O } } _ { N } \hookrightarrow X$

Pour tous polygones de troncatures$q \ \geq \ p ,$la correspondance dans $\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } } \times \overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq q } } }$qui prolonge l’identite de´$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p }$est au-dessus de la correspondance dans$\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } } } \times \overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \leq q } } }$qui prolonge l’identite de´ $\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p }$

De même, si$s , u \in \mathbb { N }$sont deux entiers et$f \in \mathcal { H } _ { N } ^ { r }$une fonction dans l’algèbre de Hecke de niveau N, il existe une fonction$| f | _ { K } \in \mathcal { H } _ { \varnothing } ^ { r }$(par exemple celle deduite de´ |f| par convolution à droite et à gauche avec la fonction caracteristique de´$\bar { K ^ { } } = \mathrm { G L } _ { r } ( O _ { \mathbb { A } } ) )$telle que la correspondance $f \times { \mathrm { F r o b } } _ { \infty } ^ { s } \times { \mathrm { F r o b } } _ { 0 } ^ { u }$dans$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } \times { \bf C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$soit au-dessus de la correspondance$| f | _ { K } \times \mathrm { F r o b } _ { \infty } ^ { s } \times \mathrm { F r o b } _ { 0 } ^ { u }$dans$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } } \times \overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$

Comme l’ouvert$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } }$dans chaque$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } } }$est l’image reciproque´ de l’ouvert$\overline { { { \mathrm { C h t } } ^ { r , \overline { { p } } \leq p } } } ^ { \prime }$de$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } }$defini en demandant que pôle, z´ ero et´ deg´ en´ erateurs´ evitent´ N, on conclut d’après le corollaire V.18.!"

## 3) Stabilite des chtoucas au voisinage des points fixes´

## a) La propriet´ e de stabilit´ e locale´

Dans le but d’appliquer les theorèmes IV.7 et IV.12 (formule des points´ fixes dans un ouvert instable) aux correspondances$f \times \mathrm { F r o b } _ { \infty } ^ { s } \times \mathrm { \hat { F } r o b } _ { 0 } ^ { u }$ dans les$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$et les$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } } } } / a ^ { \mathbb { Z } }$ou les$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$s’ils existent et de retrouver une interpretation cohomologique pour les nombres de points´ fixes par ces correspondances dans les fibres des ouverts´$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / \bar { a } ^ { \mathbb { Z } }$audessus de$( X - N ) \ \times ( X - N )$, on doit montrer qu’elles stabilisent ces ouverts “au voisinage de leurs points fixes” au sens de la definition IV.3.´ Sous une forme un peu differente ce r´ esultat dont on a besoin avait d´ ejà´ et´ e´ demontr´ e par Drinfeld dans le cas du rang´$r = 2$(voir la proposition 7.2 de l’article [Drinfeld, 1989]). De façon gen´ erale, on a :´

Theor´ eme V.19.\` – Considerons un niveau´$N \hookrightarrow X$, unefonction$f \in \mathcal { H } _ { N } ^ { r }$ et deux entiers$s , u \in \mathbb { N } .$

Alors, pour tout polygone de troncature$p : [ 0 , r ] \to \mathbb { R } _ { + }$assez convexe et tout ouvert$X ^ { \prime } \subseteq \bar { X } - T _ { f }$assez petit enfonction de N, du support de f et de$t = u - s _ { \mathrm { { \scriptscriptstyle i } } }$, la correspondance$f \times { \mathrm { F r o b } } _ { \infty } ^ { s } \times { \mathrm { F r o b } } _ { 0 } ^ { u }$dans$\overline { { { \mathrm { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb Z }$(ou $\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$s’il existe) stabilise l’ouvert$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$au voisinage de ses pointsfixes au-dessus d’un ouvert de$X ^ { \prime } \times X ^ { \prime }$qui contient$\Lambda \times _ { X \times X } X ^ { \prime } \times X ^ { \prime }$ et ne depend que du support de f et de t.´

Demonstration :´ Par construction,$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } } }$(ou$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } )$est muni d’un morphisme d’oubli des structures de niveau sur$\mathrm { C h t } ^ { r , \overline { { p } } \leq p }$tel que l’image reciproque de l’ouvert des chtoucas´$\mathrm { C h t } ^ { r , \overline { { p } } \leq p }$soit$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p }$. Cela fait qu’il suffit de demontrer le th´ eorème pour les correspondances dans´${ \overline { { \mathrm { C h t } ^ { r , \overline { { p } } } \leq p } } } / a ^ { \mathbb { Z } }$

Associons en effet à la fonction$f \in \mathcal { H } _ { N } ^ { r }$la fonction$| f | _ { K } = \mathbb { 1 } _ { K } \cdot | f | \cdot \mathbb { 1 } _ { K }$ deduite de´$\vert f \vert$par convolution à droite et à gauche par la fonction caracte-´ ristique 11$K$de$K = \mathrm { G L } _ { r } ( O _ { \mathbb { A } } )$. Le support$\Gamma _ { N } \subset \overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } } \times \overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$ de la correspondance$f \times { \mathrm { F r o b } } _ { \infty } ^ { s } \times { \mathrm { \bar { F } r o b } } _ { 0 } ^ { u }$est contenu dans l’image reci-´ proque du support$\Gamma \subset \overline { { \mathrm { { \bf { C h t } } } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } } \times \overline { { \mathrm { { \bf { C h t } } } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$de la correspondance $\hat { | } f | _ { K } { \times } \mathrm { F r o b } _ { \infty } ^ { s } { \times } \mathrm { F r o b } _ { 0 } ^ { u }$. En particulier, les “points fixes” de$f { \times } \mathrm { F r o b } _ { \infty } ^ { s } { \times } \mathrm { F r o b } _ { 0 } ^ { u }$ c’est-à-dire les points d’intersection de$\Gamma _ { N }$avec les images des morphismes (Frob<sup>n</sup>, Id),$n \in \mathbb { N } .$, dans$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$sont au-dessus des points fixes de $| f | _ { K } \times \mathrm { F r o b } _ { \infty } ^ { s } \times \mathrm { F r o b } _ { 0 } ^ { u }$. Et si$p _ { \Gamma _ { N } } ^ { \prime } , p _ { \Gamma _ { N } } ^ { \prime \prime }$et$p _ { \Gamma } ^ { \prime } , p _ { \Gamma } ^ { \prime \prime }$sont les deux projections de$\Gamma _ { N }$<sup>N N</sup>et Γ, on a un diagramme commutatif :

$$
\begin{array}{c c c c c} \overline {{\mathrm{Cht} _ {N} ^ {r , \overline {{p}} \leq p}}} / a ^ {\mathbb {Z}} & \xleftarrow {p _ {\Gamma_ {N}} ^ {\prime}} & \Gamma_ {N} & \xrightarrow {p _ {\Gamma_ {N}} ^ {\prime \prime}} & \overline {{\mathrm{Cht} _ {N} ^ {r , \overline {{p}} \leq p}}} / a ^ {\mathbb {Z}} \\ \Big \downarrow & & \Big \downarrow & & \Big \downarrow \\ \overline {{\mathrm{Cht} ^ {r , \overline {{p}} \leq p}}} / a ^ {\mathbb {Z}} & \xleftarrow {p _ {\Gamma} ^ {\prime}} & \Gamma & \xrightarrow {p _ {\Gamma} ^ {\prime \prime}} & \overline {{\mathrm{Cht} ^ {r , \overline {{p}} \leq p}}} / a ^ {\mathbb {Z}} \end{array}
$$

Si U est un ouvert dans$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } } \times \overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$tel que$p _ { \Gamma } ^ { \prime \prime - 1 } ( \mathbf { C } \mathrm { h t } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$ $\cap U \subseteq p _ { \Gamma } ^ { \prime } { } ^ { - 1 } ( \mathbf { C h t } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } ) \cap U$, son image reciproque´$U _ { N }$dans$\overline { { { \mathrm { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$ $\times \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$verifie´$p _ { \Gamma _ { N } } ^ { \prime \prime - 1 } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } ) \cap U _ { N } \subseteq p _ { \Gamma _ { N } } ^ { \prime - 1 } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } ) \cap U _ { N }$ C’est ce qu’on voulait.

On raisonne de même pour les$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z }$

Afin de prouver le theorème pour les correspondances dans´$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$ il suffit de verifier le critère valuatif (SV) du lemme IV.4. C’est l’objet´ des sous-paragraphes qui suivent.!"

## b) Un point double à valeurs dans un trait

Soient donc une fonction$f \in \mathcal { H } _ { \varnothing } ^ { r }$et deux entiers$u , s \in \mathbb { N } .$. On doit montrer que pour$p : [ 0 , r ] \to \mathbb { R } _ { + }$un polygone de troncature assez convexe et quitte à eviter dans´$( X - T _ { f } ) \times ( \bar { X } - \bar { T } _ { f } )$un ensemble fini de points fermes de´ $X - T _ { f }$et de transformees de la diagonale par des puissances de Frob´$\boldsymbol { x } \times \operatorname { I d } _ { X }$ ou$\operatorname { I d } _ { X } \times \operatorname { F r o b } _ { X }$(tout cela ne dependant que du support de´ f et de$t = u - s )$, la correspondance$f \times { \mathrm { F r o b } } _ { \infty } ^ { s } \times { \mathrm { F r o b } } _ { 0 } ^ { u }$dans$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$verifie le critère´ valuatif (SV) du lemme IV.4 relativement à l’ouvert$\mathrm { C h t } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$

Considerons un point´ α de l’une des composantes de la correspondance $f \times { \mathrm { F r o b } } _ { \infty } ^ { s } \times { \mathrm { F r o b } } _ { 0 } ^ { \hat { u } }$à valeurs dans un anneau de valuation discrète A de corps des fractions K et de corps residuel´ κ. Le point α a deux projections $\widetilde { \mathcal E }$et$\widetilde { \mathcal F }$dans$\overline { { \operatorname { C h t } ^ { r , \overline { { p } } \leq p } } } ( A )$et on suppose que, au-dessus de Spec K, le point gen´ erique´$\widetilde { \mathcal { E } } _ { K }$de$\widetilde { \mathcal E }$est dans$\mathrm { C h t } ^ { r , \overline { { p } } \leq p } ( K )$tandis que le point gen´ erique´$\smash { \widetilde { \mathcal { F } } _ { K } }$ de$\widetilde { \mathcal F }$  est dans une strate de bord$\mathrm { C h t } _ { r } ^ { r , \overline { { p } } \leq p } ( K )$indexee par une partition non´ triviale$\boldsymbol { r } = ( r _ { 1 } , \ldots , r _ { k } ) , r _ { 1 } + \cdot \cdot \cdot \dot { + } \boldsymbol { r } _ { k } = r , k \ge 2$, de l’entier r. Il s’agit de montrer que sous toutes nos hypothèses le point special´$\alpha _ { \kappa } = ( \widetilde { \mathcal { E } } _ { \kappa } , \widetilde { \mathcal { F } } _ { \kappa } )$ n’est supporte par l’image d’aucun des morphismes´

$$
\overline {{\mathrm{Cht} ^ {r , \overline {{p}} \leq p}}} / a ^ {\mathbb {Z}} \xrightarrow {(\text { Frob } ^ {n} , \text { Id })} \overline {{\mathrm{Cht} ^ {r , \overline {{p}} \leq p}}} / a ^ {\mathbb {Z}} \times \overline {{\mathrm{Cht} ^ {r , \overline {{p}} \leq p}}} / a ^ {\mathbb {Z}}, n \in \mathbb {N}.
$$

Nous devons d’abord traduire le fait que le point$\alpha = ( \widetilde { \mathcal { E } } , \widetilde { \mathcal { F } } )$est supporte par l’une des composantes´ Γ de$f \times { \mathrm { F r o b } } _ { \infty } ^ { s } \times { \mathrm { F r o b } } _ { 0 } ^ { u }$ . Cela signifie exactement qu’il existe un point$\beta = ( \widetilde { E } , \widetilde { F } )$de Γ à valeurs dans un anneau  de valuation discrète B dont le corps residuel est´ K et dont on note K le corps des fractions, tel que le point special´$\beta _ { K } = ( \widetilde { E } _ { K } , \widetilde { F } _ { K } )$de$\beta$se confonde avec le point gen´ erique´$\alpha _ { K } \stackrel { - } { = } ( \stackrel { \sim } { \mathcal { E } } _ { K } , \stackrel { \sim } { \mathcal { F } } _ { K } )$ de α et que son point gen´ erique´ $\beta _ { \mathbb { K } } = ( \tilde { E } _ { \mathbb { K } } , \widetilde { F } _ { \mathbb { K } } )$ s’envoie sur le point gen´ erique de´ Γ. Ainsi,$\widetilde { E }$est un point de$\mathrm { C h t } ^ { r , \overline { { p } } \leq p } ( B )$et$\widetilde { E } _ { \mathbb { K } }$et$\widetilde { F } _ { \mathbb { K } }$sont des points de$( \mathbf { C h t } ^ { r , \overline { { p } } \leq p } \times _ { X \times X } \pmb { \Lambda } _ { f } ) ( \mathbb { K } )$ Comme$f \times { \mathrm { F r o b } } _ { \infty } ^ { s } \times { \mathrm { F r o b } } _ { 0 } ^ { u }$est bien definie en tant que correspondance´ dans Cht<sup>r</sup>$\times _ { X \times X } \Lambda _ { f ; }$, il existe un (unique) point$\widetilde { G }$dans Cht<sup>r</sup>(B) dont la gen´ erisation´$\widetilde { G } _ { \mathbb { K } }$soit egale à´$\widetilde { F } _ { \mathbb { K } }$; mais puisque$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } }$est separ´ e, la´ specialisation´$\bar { G } _ { K }$de$\widetilde { G }$ est necessairement en dehors de l’ouvert´${ \dot { \mathrm { C h t } } } ^ { r , { \overline { { p } } } \leq p }$ de$\operatorname { C h t } ^ { r }$

## c) Filtration des points gen´ eriques´

A partir de maintenant, nous allons constamment recourir aux resultats, au´ vocabulaire et aux notations de l’article [Lafforgue, 1998].

On note V la fibre gen´ erique du chtouca´$\widetilde { F } _ { \mathbb { K } } ~ = ~ \widetilde { G } _ { \mathbb { K } }$qui est aussi celle du chtouca$\widetilde { E } _ { \mathbb { K } }$puisque la correspondance$f \times { \mathrm { F r o b } } _ { \infty } ^ { s } \times { \mathrm { F r o b } } _ { 0 } ^ { u }$dans $\mathrm { C h t } ^ { r } \times _ { X \times X } \Lambda _ { f }$preserve les fibres g´ en´ eriques. Ce´ V est un ϕ-espace au sens du paragraphe 2a de [loc. cit.]. Les chtoucas$\widetilde { G }$et$\widetilde { E }$sur B sont definis´ par l’unique ϕ-reseau´ M de V et le chtouca iter´ e´$\widetilde { F }$ est defini par un´$\varphi -$ reseau it´ er´ e´$\dot { M ^ { \prime } }$de type r dans V. Et d’après [loc. cit.] on sait associer à$M ^ { \prime }$ une filtration du complet´ e´$\widehat { V }$de V par des sous-espaces$\widehat { V } _ { v }$de dimensions $v \in \{ r _ { 1 } , r _ { 1 } + r _ { 2 } , \ldots , r _ { 1 } + \cdots + r _ { k - 1 } \}$

Bien sûr, la filtration$( \widehat { V } _ { v } )$de$\widehat { V }$induit la filtration croissante canonique $( 0 = { \mathcal { F } } _ { K } ^ { 0 } \subset \cdots \subset { \mathcal { F } } _ { K } ^ { v } \subset \cdots \subset { \mathcal { F } } _ { K } ^ { r } = { \mathcal { F } } _ { K } )$du chtouca iter´ e´$\widetilde { F } _ { K } = \widetilde { \mathcal { F } } _ { K } =$ $( { \mathcal { F } } _ { K } \hookrightarrow { \mathcal { F } } _ { K } ^ { \prime } \longleftrightarrow { \mathcal { F } } _ { K } ^ { \prime \prime } \longleftrightarrow \tau { \mathcal { F } } _ { K } )$ de type r mais elle induit aussi des filtrations croissantes par des sous-objets maximaux$( \widetilde E _ { K } ^ { v } = \widetilde { \mathcal { E } } _ { K } ^ { v } ) \operatorname { e t } { ( \widetilde { G } _ { K } ^ { v } ) }$des chtoucas $\widetilde { \boldsymbol { E } } _ { K } = \widetilde { \boldsymbol { \mathcal { E } } } _ { K }$et$\widetilde { G } _ { K }$

Lemme V.20. – Dans la situation ci-dessus, on a pour tout rang$v \in$ $\{ r _ { 1 } , r _ { 1 } + r _ { 2 } , \ldots , r _ { 1 } + \cdot \cdot \cdot + r _ { k - 1 } \}$

(i) La difference´ deg$\widetilde { G } _ { K } ^ { v } - \mathrm { d e g } \widetilde { E } _ { K } ^ { v }$est bornee par une constante qui ne´ depend que de´$t = u - s$et du support de f, tout comme deg$\widetilde { G } _ { K } -$ deg$\widetilde { E } _ { K }$

(ii) deg$\begin{array} { r } { \widetilde { E } _ { K } ^ { v } - \frac { v } { r } \deg { \widetilde { E } _ { K } } \leq \deg { \mathcal { F } _ { K } ^ { v } } - \frac { v } { r } \deg { \mathcal { F } _ { K } } . } \end{array}$

(iii) deg$\widetilde { G } _ { K } ^ { v } > \deg \mathcal { F } _ { K } ^ { v }$tandis que deg$\widetilde { G } _ { K } = \deg \mathcal { F } _ { K }$

(iv) Le zero de´$\mathcal { F } _ { K } ^ { v } c ^ { \prime } e s t  – \dot { a } – d i r e$le deg´ en´ erateur en rang´ v du chtouca iter´ e´ $\widetilde { F } _ { K } = \widetilde { \mathcal { F } } _ { K }$est

$$
x \left(\mathcal {F} _ {K} ^ {v}\right) = \operatorname{Frob} ^ {\deg \widetilde {G} _ {K} ^ {v} - \deg \mathcal {F} _ {K} ^ {v}} (\infty (\widetilde {\mathcal {F}} _ {K}))
$$

si$\widetilde { G } _ { K } ^ { v }$est un sous-objet trivial de$\smash { \widetilde { G } } _ { K }$, et

$$
x \left(\mathcal {F} _ {K} ^ {v}\right) = \operatorname{Frob} ^ {\deg \widetilde {G} _ {K} ^ {v} - \deg \mathcal {F} _ {K} ^ {v}} \left(0 \left(\widetilde {\mathcal {F}} _ {K}\right)\right)
$$

si au contraire$\widetilde { G } _ { K } / \widetilde { G } _ { K } ^ { v }$est un quotient trivial de$\widetilde { G } _ { K }$

Demonstration :´ (i) resulte de ce que le point double´$( \widetilde E , \widetilde G )$est supporte´ par la correspondance$f \times \mathrm { F r o b } _ { \infty } ^ { s } \times \mathrm { F r o b } _ { 0 } ^ { \bar { u } }$dans$\operatorname { C h t } ^ { r } \times _ { X \times X } \Lambda _ { f }$

(ii) resulte simplement de ce que ´$\widetilde { E } _ { K }$est un point de l’ouvert tronque´ $\mathrm { C h t } ^ { r , \overline { { p } } \leq p }$tandis que$\widetilde { F } _ { K } = \widetilde { \mathcal { F } } _ { K }$est un point de la strate de bord$\mathbf { C h t } _ { \underline { { r } } } ^ { r , \widehat { p } \leq p }$  indexee par la partition´ r et qui est definie par les conditions de la proposi-´ tion 9 de [loc. cit., paragraphe 1d].

(iii) Comme le chtouca$\widetilde { G } _ { K }$et le chtouca iter´ e´$\smash { \widetilde { \mathcal { F } } _ { K } }$sont deux specialisa-´ tions du même chtouca gen´ erique´$\widetilde { G } _ { \mathbb { K } } = \widetilde { F } _ { \mathbb { K } }$, on a deg${ \widetilde { \cal G } } _ { K } = \mathrm { d e g } { \widetilde { \cal G } } _ { \mathbb { K } } =$ deg$\widetilde { F } _ { \mathbb { K } } = \deg \mathcal { \widetilde { F } } _ { K }$

 Au-dessus de l’anneau de valuation discrète B, le chtouca iter´ e´$\widetilde { F }$est construit à partir du chtouca$\widetilde { G }$en transformant le ϕ-reseau´ M de V en le$\varphi -$ reseau it´ er´ e´$M ^ { \prime }$suivant les proced´ es de [loc. cit., paragraphe 2] qui sont mis´ en œuvre particulièrement à la fin de la demonstration du th´ eorème 20(i),´ page 1034. Du fait que le point de depart´$M = M ^ { 0 }$est non pas seulement un ϕ-reseau it´ er´ e mais un v´ eritable´ ϕ-reseau de´ V, cette demonstration est ici´ notablement simplifiee. Elle consiste à construire une suite finie´$( M ^ { n } ) _ { 0 \leq n \leq m }$ de ϕ-reseau it´ er´ es de´ V allant de$M ^ { 0 } = M \mathrm {  ~ \widehat { a } ~ } M ^ { m } = M ^ { \prime }$et qui verifie :´

• si$( \widehat { W } _ { w } ^ { n } ) _ { w \in { \underline { { w } } } ^ { n } }$designe la filtration de´$\widehat { V }$associee à chaque´$M ^ { n }$, la suite des rangs minimaux$w ^ { n } = \operatorname* { m i n } ( \underline { { w } } ^ { n } )$des$\widehat { W } _ { w } ^ { n } , w \in \underline { { w } } ^ { n }$, est strictement decroissante,´

• pour chaque n,$0 ~ \leq ~ n ~ < ~ m , ~ \widehat { W } _ { w ^ { n + 1 } } ^ { n + 1 }$est contenu dans tous les$\widehat { W } _ { w } ^ { n }$ $w \in { \underline { { w } } } ^ { n }$, et$M ^ { m + 1 }$se deduit de´$M ^ { n }$comme transforme strict (au sens de´ la proposition 12 de [loc. cit., paragraphe 2c]) une ou plusieurs fois par la filtration reunion de´$\widehat { W } _ { w ^ { n + 1 } } ^ { n + 1 }$et des$\widehat { W } _ { w } ^ { n } , w \in \underline { { w } } ^ { n }$,

 • le chtouca deg´ en´ er´ e induit par chaque´$M ^ { n }$est un chtouca iter´ e dont´ on peut noter${ \widetilde { \mathcal { F } } } ^ { M ^ { n } } = ( { \mathcal { F } } ^ { { \dot { M } } ^ { n } } \hookrightarrow { \mathrm { ~ } } ^ { * } { \mathcal { F } } ^ { \prime M ^ { n } } \iff { \mathcal { F } } ^ { \prime \prime M ^ { n } } \iff { \overset { \triangledown } { \boldsymbol { \tau } } } { \mathcal { F } } ^ { M ^ { n } } )$la specialisation.´

Ainsi, on a$\widetilde { \mathcal { F } } ^ { M ^ { 0 } } = \widetilde { G } _ { K } , \widetilde { \mathcal { F } } ^ { M ^ { m } } = \widetilde { \mathcal { F } } _ { K }$et la filtration finale$( \widehat { W } _ { w } ^ { m } ) _ { w \in { \underline { { w } } } ^ { m } }$de V n’est autre que9$( \widehat { V } _ { v } )$

Pour tout$v \in \{ r _ { 1 } , r _ { 1 } + r _ { 2 } , \ldots , r _ { 1 } + \cdots + r _ { k - 1 } \}$, le sous-espace$\widehat { V } _ { v }$de$\widehat { V }$ induit un sous-fibre maximal´$\mathcal { F } _ { v } ^ { M ^ { n } }$dans chaque$\scriptstyle { \mathcal { F } } ^ { M ^ { n } }$ . D’après la proposition 12 de [loc. cit], la suite des deg$( \mathcal { F } _ { v } ^ { M ^ { n } } ) , 0 \leq n \leq m$, est decroissante et´ elle n’est pas constante. Cela prouve

$$
\deg \widetilde {G} _ {K} ^ {v} = \deg \mathcal {F} _ {v} ^ {M ^ {0}} > \deg \mathcal {F} _ {v} ^ {M ^ {m}} = \deg \mathcal {F} _ {K} ^ {v}.
$$

(iv) Nous allons suivre encore le chemin de$M ^ { 0 } = M \mathrm { ~ \widehat { a } ~ } M ^ { m } = M ^ { \prime }$ à travers les$M ^ { n }$que nous venons de rappeler dans la demonstration de´ (iii) ci-dessus. Pour tout$v \in \{ r _ { 1 } , r _ { 1 } + r _ { 2 } , \ldots , r _ { 1 } + \cdots + r _ { k - 1 } \}$, notons $\infty ( \mathcal { F } _ { v } ^ { M ^ { 0 } } ) = \infty ( \widetilde { G } _ { K } ) = \infty ( \widetilde { \mathcal { F } } _ { K } )$et

$x \big ( \mathcal { F } _ { v } ^ { M ^ { 0 } } \big ) = \left\{ \begin{array} { l l } { \infty ( \widetilde { G } _ { K } ) = \infty ( \widetilde { \mathcal { F } } _ { K } ) } \\ { 0 ( \widetilde { G } _ { K } ) = 0 ( \widetilde { \mathcal { F } } _ { K } ) } \end{array} \right.$si$\widetilde { G } _ { K } ^ { v }$est un sous-objet trivial de$\widetilde { G } _ { K }$ sinon.

Dans tous les cas, le determinant det´$( \mathcal { F } _ { v } ^ { M ^ { 0 } } )$du fibre´$\mathcal { F } _ { v } ^ { M ^ { 0 } }$est muni d’un isomorphisme canonique

$$
{ } ^ { \tau } \operatorname* { d e t } \left( \mathcal { F } _ { v } ^ { M ^ { 0 } } \right) \cong \operatorname* { d e t } \left( \mathcal { F } _ { v } ^ { M ^ { 0 } } \right) \bigl ( \infty \bigl ( \mathcal { F } _ { v } ^ { M ^ { 0 } } \bigr ) - x \bigl ( \mathcal { F } _ { v } ^ { M ^ { 0 } } \bigr ) \bigr ) .
$$

Pour tout$n , 0 \leq n \leq m$, det$( \mathcal { F } _ { v } ^ { M ^ { n } } )$a même fibre gen´ erique que det´$( \mathcal { F } _ { v } ^ { M ^ { 0 } } )$ Procedant par r´ ecurrence sur´ n, on deduit alors du lemme V.16 que l’iso-´ morphisme ci-dessus devient

$$
{ } ^ { \tau } \operatorname* { d e t } \left( \mathcal { F } _ { v } ^ { M ^ { n } } \right) \cong \operatorname* { d e t } \left( \mathcal { F } _ { v } ^ { M ^ { n } } \right) \left( \infty \left( \mathcal { F } _ { v } ^ { M ^ { 0 } } \right) - \operatorname{Frob} ^ { \deg \left( \mathcal { F } _ { v } ^ { M ^ { 0 } } \right) - \deg \left( \mathcal { F } _ { v } ^ { M ^ { n } } \right) } \left( x \left( \mathcal { F } _ { v } ^ { M ^ { 0 } } \right) \right) \right)
$$

C’est ce qu’on voulait.

## d) Filtration des points speciaux´

Nous voulons maintenant etudier le point´$\alpha = ( \widetilde { \mathcal { E } } , \widetilde { \mathcal { F } } )$à valeurs dans l’anneau de valuation discrète A.

Le point gen´ erique´$\smash { \widetilde { \mathcal { F } } _ { K } }$est un chtouca iter´ e de type´ r donc sa specialisation´ $\widetilde { \mathcal { F } } _ { \kappa }$est un chtouca iter´ e de type ´$\underline { { r } } ^ { \prime }$raffinant r.

L’autre point gen´ erique´$\widetilde { \mathcal { E } } _ { K }$est dans l’ouvert tronque´$\mathrm { C h t } ^ { r , \overline { { p } } \leq p }$de Cht<sup>r</sup>. Il est muni d’une filtration$( \widetilde { \mathcal { E } } _ { K } ^ { v } )$) par des sous-objets maximaux$\widetilde { \mathcal { E } } _ { K } ^ { v }$de rangs $v \in \{ r _ { 1 } , r _ { 1 } + r _ { 2 } , \ldots , r _ { 1 } + \cdots + r _ { k - 1 } \}$. D’après le lemme V.20(i)(ii)(iii), les differences entre les valeurs prises en les entiers´ v par le polygone de cette filtration et le polygone de troncature p sont bornees par une constante qui´ ne depend que de´ t et du support de f. Si$p$est assez convexe en fonction de t et du support de$f _ { : }$, cela implique en particulier que les$\widetilde { \mathcal { E } } _ { K } ^ { v }$figurent dans la filtration canonique de Harder-Narasimhan de$\widetilde { \mathcal { E } } _ { K }$

Si le chtouca iter´ e´$\widetilde { \mathcal E } _ { \kappa } .$, specialisation de´$\widetilde { \mathcal { E } } , \boldsymbol { \mathrm { n } } ^ { \prime } \boldsymbol { \mathrm { : } }$pas le même type$\underline { { r } } ^ { \prime }$que $\widetilde { \mathcal { F } } _ { \kappa }$, le point special´$\alpha _ { \kappa } = ( \widetilde { \mathcal { E } } _ { \kappa } , \widetilde { \mathcal { F } } _ { \kappa } )$n’est evidemment support´ e par l’image´   d’aucun des morphismes (Frobn, Id),$n \in \mathbb { N }$

Supposons donc que$\widetilde { \mathscr { E } } _ { \kappa } = ( \mathscr { E } _ { \kappa } \hookrightarrow \mathscr { E } _ { \kappa } ^ { \prime } \hookrightarrow \mathscr { E } _ { \kappa } ^ { \prime \prime } \Longleftarrow { } ^ { \tau } \mathscr { E } _ { \kappa } )$a le même type $\underline { { r } } ^ { \prime }$raffinant$\underline { r }$que$\widetilde { \mathcal { F } } _ { \kappa }$. Dans la filtration croissante canonique de$\mathcal { E } _ { \kappa }$, il y a alors des sous-fibres maximaux´$\mathcal { E } _ { \kappa } ^ { v }$de rangs les$v \in \{ r _ { 1 } , r _ { 1 } + r _ { 2 } , \ldots , r _ { 1 } +$ $\cdots + r _ { k - 1 } \}$

Lemme V.21. – Dans la situation ci-dessus et si le polygone p est assez convexe enfonction de t et du support de f, on a pour tout$\upsilon \in \{ r _ { 1 } , r _ { 1 } + r _ { 2 }$ $\dots , r _ { 1 } + \dots + r _ { k - 1 } \}$

(i) deg$\mathcal { E } _ { \kappa } ^ { v } \geq \deg \widetilde { \mathcal { E } } _ { K } ^ { v }$, avec deg$\mathcal { E } _ { \kappa } = \mathrm { d e g } \widetilde { \mathcal { E } } _ { K }$

(ii) deg$\mathcal { E } _ { \kappa } ^ { v } - \mathrm { d e g } \widetilde { \mathcal { E } } _ { K } ^ { v }$est majore par une constante qui ne d´ epend que de t´ et du support de f.

(iii) Notant$\overline { { \infty } } e t \overline { { 0 } }$les pôle et zero de´$\widetilde { \mathcal { E } } _ { \kappa } e t \overline { { x } } _ { v }$son deg´ en´ erateur en rang´ v, on a

$$
\overline {{\infty}} = \operatorname{Frob} ^ {\deg \mathcal {E} _ {\kappa} ^ {v} - \deg \widetilde {\mathcal {E}} _ {K} ^ {v}} (\overline {{x}} _ {v})
$$

si$\widetilde { \mathcal { E } } _ { K } ^ { v }$est un sous-objet trivial de$\widetilde { \mathcal { E } } _ { K }$, et

$$
\overline {{0}} = \operatorname{Frob} ^ {\deg \mathcal {E} _ {K} ^ {v} - \deg \widetilde {\mathcal {E}} _ {K} ^ {v}} (\overline {{x}} _ {v})
$$

si au contraire$\widetilde { \mathcal { E } } _ { K } / \widetilde { \mathcal { E } } _ { K } ^ { v }$est un quotient trivial de$\widetilde { \mathcal { E } } _ { K }$.

Demonstration :´ (i) resulte simplement de ce que´$\widetilde { \mathcal { E } } _ { K }$est un point de l’ouvert tronque´$\mathrm { C h t } ^ { r , \overline { { p } } \leq p }$tandis que sa specialisation´$\widetilde { \mathcal { E } } _ { \kappa }$, qui a automatiquement même degre, est un point de la strate de bord´$\mathrm { C h t } _ { \underline { { r } } ^ { \prime } } ^ { r , \overline { { p } } \leq p }$indexee par la´ partition$\underline { { r } } ^ { \prime }$raffinant r.

(ii) En les entiers v, le polygone de la filtration$( \mathcal { E } _ { \kappa } ^ { v } )$est compris entre $p - 1$et p tandis que, comme on a dit, la difference entre le polygone de la´ filtration$( \widetilde { \mathcal { E } } _ { K } ^ { v } )$et$p$est bornee par une constante qui ne d´ epend que de´ t et du support de$f .$.

(iii) Soit W la fibre gen´ erique du chtouca´$\widetilde { \mathcal { E } } _ { K } : \mathrm { c } ^ { \prime }$est un ϕ-espace. Le chtouca iter´ e´ E sur A qui prolonge$\widetilde { \mathcal { E } } _ { K }$est defini par un´ ϕ-reseau it´ er´ e´ N de W de type$\underline { { r } } ^ { \prime } = ( r _ { 1 } ^ { \prime } , r _ { 2 } ^ { \prime } , \ldots , \hat { r } _ { k ^ { \prime } } ^ { \prime } )$. Il lui est associe une filtration du compl´ et´ e´ W de W par des sous-espaces$\hat { W } _ { w }$de rangs$w \in \{ r _ { 1 } ^ { \prime } , r _ { 1 } ^ { \prime } + r _ { 2 } ^ { \prime } , \ldots , r _ { 1 } ^ { \prime } + \cdot \cdot \cdot + r _ { k ^ { \prime } - 1 } ^ { \prime } \}$ Et comme la partition$\underline { { r } } ^ { \prime }$de r raffine$\underline { { r } } ,$la filtration$( \widehat { W } _ { w } )$comprend en particulier des sous-espaces$\widehat { W } _ { v }$de rangs les$v \in \{ r _ { 1 } , r _ { 1 } + r _ { 2 } , \ldots , r _ { 1 } + \cdot \cdot \cdot +$ $r _ { k - 1 } \}$

Fixant un tel$v ,$nous allons envisager un certain nombre de ϕ-reseaux´ iter´ es´ M de W dont la filtration de$\widehat { W }$associee est contenue dans´$( \widehat { W } _ { w } )$et comprend$\widehat { W } _ { v }$. Comme dans [loc. cit., paragraphe 2], on notera$\widetilde { \mathcal { E } } ( M )$le chtouca deg´ en´ er´ e prolongement de´$\widetilde { \mathcal { E } } _ { K }$sur A associe à un tel´ M,$\widetilde { \mathcal { E } } ^ { M } =$ $( \mathcal { E } ^ { M } \hookrightarrow \mathcal { E } ^ { \prime \breve { M } } \longleftrightarrow \bar { \mathcal { E } } ^ { \prime \prime M } \longleftrightarrow \bar { \tau } \mathcal { E } ^ { M } )$sa specialisation au-dessus de´ κ et$\mathcal { E } _ { v } ^ { M } \mathrm { l e }$ sous-fibre maximal de rang´ v dans$\mathcal { E } ^ { M }$induit par$\widehat { W } _ { v }$. Ainsi a-t-on$\widetilde { \mathcal { E } } ( N ) = \widetilde { \mathcal { E } }$ $\widetilde { \mathcal { E } } ^ { N } = \widetilde { \mathcal { E } } _ { \kappa } , \mathcal { E } ^ { N } = \mathcal { E } _ { \kappa }$et$\mathcal { E } _ { v } ^ { N } = \mathcal { E } _ { \kappa } ^ { v }$

Notons$n _ { v } = \deg \mathcal { E } _ { \kappa } ^ { v } - \deg \widetilde { \mathcal { E } } _ { K } ^ { v } \geq 0 .$On sait que$\widetilde { \mathcal { E } } _ { K } ^ { v }$figure dans la filtration canonique de Harder-Narasimhan de$\widetilde { \mathcal { E } } _ { K } . \ \mathrm { { D } } ^ { \prime }$après le corollaire 18 de [loc. cit., paragraphe 2d], il existe une suite$N = N ^ { \hat { 0 } } , N ^ { 1 } , \dots , N ^ { n _ { v } }$de ϕ-reseaux´ iter´ es de´ W dont chacun est le transforme strict du pr´ ec´ edent par les´$\widehat { W } _ { w } ,$ $w \geq v$(quitte à remplacer A par une extension finie), avec en particulier $\deg ( \mathcal { E } _ { v } ^ { N ^ { n } } ) = \deg ( \mathcal { E } _ { v } ^ { N ^ { n - 1 } } ) - 1 , 0 < n \leq n _ { v }$. Comme$\eqslantgtr$designe le pôle de´ $\widetilde { \mathcal { E } } _ { \kappa } = \widetilde { \mathcal { E } } ^ { N } = \widetilde { \mathcal { E } } ^ { N ^ { 0 } }$et$\overline { { x } } _ { v }$designe son d´ eg´ en´ erateur en rang´$v ,$le determinant´  du fibre´$\mathcal { E } _ { v } ^ { N ^ { 0 } }$est muni d’un isomorphisme canonique

$$
{ } ^ { \tau } \operatorname* { d e t } \left( \mathcal { E } _ { v } ^ { N ^ { 0 } } \right) \cong \operatorname* { d e t } \left( \mathcal { E } _ { v } ^ { N ^ { 0 } } \right) ( \overline { { \infty } } - \overline { { x } } _ { v } ) .
$$

Pour tout$n , 0 < n \leq n _ { v } , \operatorname* { d e t } ( \mathcal { E } _ { v } ^ { N ^ { n } } )$a même fibre gen´ erique que det´$( \mathcal { E } _ { v } ^ { N ^ { 0 } } )$ Procedant par r´ ecurrence sur´ n, on deduit du lemme V.16 que l’isomor-´ phisme ci-dessus devient

$$
{ } ^ { \tau } \operatorname* { d e t } \left( \mathcal { E } _ { v } ^ { N ^ { n } } \right) \cong \operatorname* { d e t } \left( \mathcal { E } _ { v } ^ { N ^ { n } } \right) ( \overline { { \infty } } - \operatorname{Frob} ^ { n } ( \overline { { x } } _ { v } ) ) .
$$

En particulier, on a un isomorphisme canonique

$$
{ } ^ { \tau } \operatorname* { d e t } \left( \mathcal { E } _ { v } ^ { N ^ { n _ { v } } } \right) \cong \operatorname* { d e t } \left( \mathcal { E } _ { v } ^ { N ^ { n _ { v } } } \right) ( \overline { { \infty } } - \operatorname{Frob} ^ { n _ { v } } ( \overline { { x } } _ { v } ) ) .
$$

Montrons maintenant que$N ^ { n _ { v } }$n’admet pas de transforme strict par´$\widehat { W } _ { v }$ En effet,$\mathrm { s } ^ { \prime } \mathrm { i l }$en admettait un note´$N ^ { \prime }$, on aurait d’une part

$$
\deg \mathcal {E} _ {v} ^ {N ^ {\prime}} = \deg \mathcal {E} _ {v} ^ {N ^ {n v}} - 1 = \deg \widetilde {\mathcal {E}} _ {K} ^ {v} - 1.
$$

D’autre part, le polygone canonique de$\widetilde { \mathcal { E } } _ { \kappa }$et celui de$\widetilde { \mathcal { E } } ^ { N ^ { \prime } }$ne differeraient´ en tous les points que d’au plus$n _ { v } + 1 . \mathrm { D } ^ { \mathrm { } }$ ’après (ii), on en deduirait que si´ p a et´ e choisi assez convexe en fonction de´ t et du support de$f ,$le sous-fibre´ de$\mathcal { E } ^ { N ^ { \prime } }$induit par le sous-objet$\widetilde { \mathcal { E } } _ { K } ^ { v }$de$\widetilde { \mathcal { E } } _ { K }$et qui a pour rang$v = \arg \mathcal { E } _ { v } ^ { N ^ { \prime } }$ et pour degre deg´$\widetilde { \mathcal { E } } _ { K } ^ { v } = \mathrm { d e g } \widetilde { \mathcal { E } } _ { v } ^ { N ^ { \prime } } + 1$, serait contenu dans$\mathcal { E } _ { v } ^ { N ^ { \prime } }$. Il y aurait contradiction.

On peut donc construire à partir de$N ^ { n _ { v } }$une suite infinie$( N ^ { n } ) _ { n \geq n _ { v } }$de transformes successifs de´$N ^ { n _ { v } }$par$\widehat { W } _ { v }$avec

$$
\mathcal {E} _ {v} ^ {N ^ {n}} = \mathcal {E} _ {v} ^ {N ^ {n - 1}}, \forall n > n _ {v},
$$

comme dans la demonstration de la proposition 14 de [loc. cit., para-´ graphe 2d]. La limite projective

$$
\varprojlim_ {n \geq n _ {v}} \widetilde {\mathcal {E}} (N ^ {n _ {v}}) / \widetilde {\mathcal {E}} (N ^ {n})
$$

est un quotient localement libre de l’image reciproque de´$\widetilde { \mathcal { E } } _ { K }$sur le complet´ e´ formel de$X \otimes A$le long de$X \otimes \kappa$. Elle provient du quotient localement libre de$\bar { \mathcal { E } } _ { K }$par un sous-objet de rang v et de degre deg´$\mathbf { \widetilde { \mathcal { E } } } _ { v } ^ { N ^ { n _ { v } } } = \mathrm { d e g } \widetilde { \mathcal { E } } _ { K } ^ { v }$qui est necessairement´$\widetilde { \mathcal { E } } _ { K } ^ { v }$puisque celui-ci figure dans la filtration canonique de Harder-Narasimhan de$\widetilde { \mathcal { E } } _ { K }$

On en deduit un isomorphisme canonique´

$$
{ } ^ { \tau } \operatorname* { d e t } \left( \mathcal { E } _ { v } ^ { N ^ { n _ { v } } } \right) \cong \operatorname* { d e t } \left( \mathcal { E } _ { v } ^ { N ^ { n _ { v } } } \right) \cong \operatorname* { d e t } \left( \mathcal { E } _ { v } ^ { N ^ { n _ { v } } } \right) ( \overline { { { \infty } } } - \overline { { { \infty } } } )
$$

si$\widetilde { \mathcal { E } } _ { K } ^ { v }$est un sous-objet trivial de$\widetilde { \mathcal { E } } _ { K }$, ou bien

$$
{ } ^ { \tau } \operatorname* { d e t } \left( \mathcal { E } _ { v } ^ { N ^ { n _ { v } } } \right) \cong \operatorname* { d e t } \left( \mathcal { E } _ { v } ^ { N ^ { n _ { v } } } \right) ( \overline { { { \infty } } } - \overline { { { 0 } } } )
$$

si au contraire$\widetilde { \mathcal { E } } _ { K } / \widetilde { \mathcal { E } } _ { K } ^ { v }$est un quotient trivial de$\widetilde { \mathcal { E } } _ { K }$

 D’où la conclusion.

## e) Fin de la demonstration´

Nous pouvons maintenant achever la verification du critère valuatif (SV) de´ stabilite au voisinage des points fixes et donc du th´ eorème V.19.´

Rappelons que nous avons note´$\overline { { \infty } } , \overline { { 0 } }$et$\overline { { x } } _ { v } , v \in \{ r _ { 1 } , r _ { 1 } + r _ { 2 } , \ldots , r _ { 1 } +$ $\cdots + r _ { k - 1 } \}$les pôle, zero et d´ eg´ en´ erateurs en les rangs´ v de$\widetilde { \mathcal { E } } _ { \kappa }$. Dans le lemme V.21, nous avons prouve que si le polygone de troncature´$p$est assez convexe en fonction de t et du support de$f ,$, il existe des entiers$n _ { v } \geq 0 .$ $v \in \{ r _ { 1 } , r _ { 1 } + r _ { 2 } , \ldots , r _ { 1 } + \cdots + r _ { k - 1 } \}$, majores par une constante qui ne´ depend que de´ t et du support de$f _ { \cdot }$, tels que pour tout v

$$
\operatorname{Frob} ^ {n _ {v}} \left(\overline {{x}} _ {v}\right) = \overline {{\infty}} \text {   ou   } \overline {{0}}.
$$

De même, notons$\overline { { \infty } } ^ { \prime } , \overline { { 0 } } ^ { \prime }$et$\overline { { x } } _ { v } ^ { \prime } , v \in \{ r _ { 1 } , r _ { 1 } + r _ { 2 } , \ldots , r _ { 1 } + \cdot \cdot \cdot + r _ { k - 1 } \}$, les pôle, zero et d´ eg´ en´ erateurs en les rangs´ v de$\widetilde { \mathcal { F } } _ { \kappa }$. Par specialisation du lemme´ V.20, on voit qu’il existe des entiers$n _ { v } ^ { \prime } > 0$, majores par une constante qui´ ne depend que de´ t et du support de$f _ { : }$, tels que pour tout v

$$
\overline {{x}} _ {v} ^ {\prime} = \operatorname{Frob} ^ {n _ {v} ^ {\prime}} (\overline {{\infty}} ^ {\prime}) \text {   ou   } \operatorname{Frob} ^ {n _ {v} ^ {\prime}} (\overline {{0}} ^ {\prime}).
$$

Or, si$n \in \mathbb N$est un entier tel que le point double special´$( \widetilde { \mathcal { E } } _ { \kappa } , \widetilde { \mathcal { F } } _ { \kappa } )$est supporte par l’image de´$( \mathrm { F r o b } ^ { n } , \mathrm { I d } )$, on a automatiquement

$$
\begin{array}{l} \overline {{\infty}} = \operatorname{Frob} ^ {n} (\overline {{\infty}} ^ {\prime})  ,   \overline {{0}} = \operatorname{Frob} ^ {n} (\overline {{0}} ^ {\prime})    \text { et } \\ \overline {{x}} _ {v} = \operatorname{Frob} ^ {n} (\overline {{x}} _ {v} ^ {\prime})  ,   \forall v  . \end{array}
$$

Pour tout v, l’entier$n _ { v } + n _ { v } ^ { \prime } \ge 1$qui est majore par une constante qui ne´ depend que de´ t et du support de$f$, doit donc verifier l’une au moins des´ quatre equations´

$$
\overline {{\infty}} = \mathrm{Frob} ^ {n _ {v} + n _ {v} ^ {\prime}} (\overline {{\infty}}),
$$

$$
\text { ou } \overline {{0}} = \operatorname{Frob} ^ {n _ {v} + n _ {v} ^ {\prime}} (\overline {{0}}),
$$

$$
\text { ou } \overline {{\infty}} = \operatorname{Frob} ^ {n _ {v} + n _ {v} ^ {\prime}} (\overline {{0}}),
$$

$$
\mathrm{ou} \overline {{0}} = \mathrm{Frob} ^ {n _ {v} + n _ {v} ^ {\prime}} (\overline {{\infty}}).
$$

Cela entraîne que ou bien$\eqslantgtr$ou$\overline { { 0 } }$est supporte par un ensemble fini de´ points fermes de´$X - T _ { f }$qui ne depend que de´ t et du support de$f _ { : }$, ou bien $( \overline { { \infty } } , \overline { { 0 } } )$est supporte par une r´ eunion finie de transform´ ees de la diagonale´ de$X \times X$par des puissances de Frob$\boldsymbol { x } \times \operatorname { I d } _ { X }$ou$\operatorname { I d } _ { X } \times \operatorname { F r o b } _ { X }$qui ne depend´ elle aussi que de t et du support de f.

L’ouvert de$( X - T _ { f } ) \times ( X - T _ { f } )$qui est defini en enlevant ces deux´ familles finies de fermes r´ epond à la question pos´ ee.´!"

Remarque : A la fin de la demonstration ci-dessus on doit´ ecarter de´$\vert X - T _ { f } \vert$ l’ensemble fini des points$\infty$ou 0 dont le degre divise une constante non´ nulle qui ne depend que de´ t et du support de$f .$Cette condition etait d´ ejà´ apparue dans la formule de comptage du theorème 1 du paragraphe V.2a´ de [Lafforgue, 1997] via le lemme 11 du paragraphe V.2d de ce livre, et on l’avait reproduite dans l’enonc´ e des th´ eorèmes I.5, I.7 et I.13 du pr´ esent´ travail.

## Chapitre VI

## Cohomologie des chtoucas et correspondance globale

Dans ce chapitre, nous realisons la correspondance de Langlands globale´ pour les groupes$\mathrm { G L } _ { r }$sur le corps des fonctions d’une courbe X dans la cohomologie -adique au-dessus du point gen´ erique de´$X \times X$des champs de chtoucas de rang r, gen´ eralisant le th´ eorème en rang´$r \ = \ 2$obtenu par Drinfeld. On met en œuvre pour cela les differents types de r´ esultat´ rassembles dans les chapitres pr´ ec´ edents et dans les deux appendices.´

On commence par rappeler les propriet´ es g´ en´ erales des fonctions L´ de systèmes locaux -adiques sur les variet´ es d´ efinies sur le corps fini de´ base$\mathbb { F } _ { q } . \mathbf { D } ^ { \ast }$après Grothendieck, elles ont une interpretation cohomologique ´ qui entraîne en particulier que ce sont des fractions rationnelles et on peut situer leurs zeros et pôles grâce au th´ eorème de puret´ e de Deligne, ce qui´ est essentiel pour la suite.${ \bf \vec { S } } ^ { \prime }$agissant$\mathrm { d } ^ { \prime }$un système local -adique sur un ouvert de la courbe X, on peut lui associer des facteurs L et ε locaux en tous les points fermes de´ X. Comme consequence de la dualit´ e de Grothendieck,´ la fonction L globale definie comme produit de tous les facteurs L locaux´ verifie une´ equation fonctionnelle ; et d’après un th´ eorème de Laumon´ essentiel ici, on sait que la constante dans cette equation fonctionnelle est´ le produit de tous les facteurs ε locaux.

On enonce alors la correspondance de Langlands globale pour le´ corps des fonctions de la courbe X. Toutes les informations que nous avons rassemblees à propos des fonctions L, tant de systèmes locaux´ -adiques que de paires automorphes, permettent de proceder à beaucoup de r´ eductions´ et finalement on se ramène à demontrer l’´ enonc´ e suivant : Pour tout entier´ $r \geq 2$et supposant la correspondance de Langlands dejà connue en rangs´ $< r$, on peut associer à toute representation automorphe cuspidale´ π de $\mathrm { G L } _ { r }$un système local -adique$\sigma _ { \pi }$sur un ouvert de X qui a les mêmes facteurs L locaux en toutes les places non ramifiees. On r´ ealise ce´$\sigma _ { \pi }$dans la cohomologie -adique d’un champ de chtoucas$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$au-dessus du point gen´ erique de´$X \times X$

Tout d’abord, on definit dans la cohomologie de Ch´$\begin{array} { r } { { \cdot \sqrt { p } } { \leq } p } \\ { { N } } \end{array} / a ^ { \mathbb { Z } } , \overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$ (ou eventuellement´$\dot { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } } / a ^ { \mathbb Z } )$et$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb Z }$une partie negligeable (celle´ qui provient des rangs inferieurs) et une partie essentielle (le reste). La´ separation des deux est rendue possible par l’hypothèse de r´ ecurrence et par´ la connaissance$\mathrm { \ q u } ^ { \prime }$on a des zeros et pôles des fonctions L. On montre que´ $\mathrm { { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } , \overline { { \mathrm { { C h t } } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } } } } / a ^ { \mathbb { Z } }$(ou eventuellement´$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$et$\mathrm { C h t } _ { N } ^ { r } / a ^ { \mathbb Z }$ont même cohomologie essentielle. Et bien sûr,${ \mathrm { c } } ^ { \prime }$est là qu’on doit${ \bf s } '$attendre à trouver un morceau egal à´$\sigma _ { \pi }$

Pour isoler un tel morceau et achever ainsi la demonstration, on scinde´ la cohomologie essentielle en faisant agir les correspondances de Hecke.

## 1) Enonce de la correspondance de Langlands et r´ eductions´

## a) Fonctions L des systèmes locaux -adiques

On fixe un nombre premier  qui ne divise pas le cardinal$q$du corps fini de base$\mathbb { F } _ { q }$

Pour tout schema´ V de type fini sur$\mathbb { F } _ { q } .$, on note$\mathcal { G } _ { \ell } ( V )$l’ensemble des classes d’isomorphie de faisceaux -adiques lisses sur V. Si V est connexe et$\overline { { x } }$est un point geom´ etrique de´$V , \mathcal { G } _ { \ell } ( V )$s’identifie à l’ensemble des representations du groupe fondamental de Grothendieck´$\pi _ { 1 } ( V , { \overline { { x } } } )$qui sont continues et de dimension finie sur la clôture algebrique´$\overline { { \mathbb { Q } } } _ { \ell }$de$\mathbb { Q } _ { \ell }$et qui sont definies sur une extension finie de´$\mathbb { Q } _ { \ell }$. Tout faisceau -adique lisse sur V est alors de rang constant egal à la dimension de la repr´ esentation´ associee de´$\pi _ { 1 } ( V , { \overline { { x } } } )$. Le groupe de Galois de$\mathbb { F } _ { q }$est engendre par Frob et il´ s’identifie au complet´ e´$\widehat { \mathbb { Z } }$de$\mathbb { Z }$. Par consequent, chaque´$\pi _ { 1 } ( V , { \overline { { x } } } )$est muni d’un homomorphisme canonique continu et surjectif$\pi _ { 1 } ( V , { \overline { { x } } } ) \to { \widehat { \mathbb { Z } } }$. Le groupe de Weil$\operatorname { \dot { W } } ( V , { \overline { { x } } } ) = \operatorname { K e r } [ \pi _ { 1 } ( V , { \overline { { x } } } ) \to { \widehat { \mathbb { Z } } } / \mathbb { Z } ]$est un sous-groupe dense de$\pi _ { 1 } ( V , { \overline { { x } } } )$et toute representation´ -adique de$\pi _ { 1 } ( V , { \overline { { x } } } )$est uniquement determin´ ee par sa restriction à´$W ( V , { \overline { { x } } } )$

On note |V| l’ensemble des points fermes de´ V. Pour tout faisceau$\ell -$ adique lisse$\sigma \in \mathcal { G } _ { \ell } ( V )$de rang r et tout point ferme´$x \in | V |$, la fibre$\sigma _ { x }$de $\sigma$en x peut être vue comme un espace vectoriel de dimension r muni d’une action par automorphisme de l’el´ ement de Frobenius´$\mathrm { F r o b } _ { x } = \mathrm { F r o b } ^ { \mathrm { d e g } ( x ) }$ on note$z _ { 1 } ( \sigma _ { x } ) , \dots , z _ { r } ( \sigma _ { x } )$les valeurs propres de cet automorphisme.

On definit le facteur L local de´ σ en x comme

$$
\mathrm{L} _ {x} \left(\sigma_ {x}, Z\right) = \frac {1}{\det _ {\sigma_ {x}} \left(\operatorname{Id} - \operatorname{Frob} _ {x} ^ {- 1} \cdot Z ^ {\deg (x)}\right)} = \prod_ {1 \leq i \leq r} \frac {1}{1 - z _ {i} \left(\sigma_ {x}\right) ^ {- 1} Z ^ {\deg (x)}}
$$

puis la fonction L globale de$\sigma$comme le produit

$$
\mathrm{L} _ {V} (\sigma , Z) = \prod_ {x \in | V |} \mathrm{L} _ {x} (\sigma_ {x}, Z).
$$

Elle est bien definie en tant que s´ erie formelle en l’ind´ etermin´ ee´$Z .$, de même que sa deriv´ ee logarithmique´

$$
\frac {\mathrm{L} _ {V} ^ {\prime} (\sigma , Z)}{\mathrm{L} _ {V} (\sigma , Z)} = \sum_ {x \in | V |} \deg (x) \sum_ {k \geq 1} (z _ {1} (\sigma_ {x}) ^ {- k} + \dots + z _ {r} (\sigma_ {x}) ^ {- k}) Z ^ {k \deg (x) - 1}.
$$

Plus gen´ eralement, si´$\sigma$est un faisceau -adique constructible sur$V _ { ; }$, sa fibre$\sigma _ { x }$en tout point ferme´$x \in | V |$est un espace vectoriel de dimension finie muni d’une action par automorphisme de$\operatorname { F r o b } _ { x }$et on peut poser

$$
\mathrm{L} _ {x} (\sigma , Z) = \frac {1}{\det _ {\sigma_ {x}} \left(\operatorname{Id} - \operatorname{Frob} _ {x} ^ {- 1} \cdot Z ^ {\deg (x)}\right)}
$$

puis$\operatorname { L } _ { V } ( \sigma , Z ) = \prod _ { x \in \vert V \vert } \operatorname { L } _ { x } ( \sigma , Z )$

On a le theorème fondamental suivant de Grothendieck :´

Theor´ eme VI.1.\` – Etant donne´$\sigma \in \mathcal { G } _ { \ell } ( V )$un faisceau -adique lisse (ou plus gen´ eralement´ σ un faisceau -adique constructible) sur un schema´ V de type fini sur$\mathbb { F } _ { q } ,$, soient$H _ { c } ^ { \nu } ( \sigma ) , ~ 0 ~ \leq ~ \nu ~ \leq ~ 2$dim V, les groupes de cohomologie etale à supports compacts de´ σ au-dessus du point Spec$\mathbb { F } _ { q }$

Alors la serie formelle´$\operatorname { L } _ { V } ( \sigma , Z )$est egale à la fraction rationnelle en´ l’indetermin´ ee Z´

$$
\prod_ {\nu} \left[ \det _ {H _ {c} ^ {\nu} (\sigma)} (\mathrm{Id} - \operatorname{Frob} ^ {- 1} \cdot Z) \right] ^ {(- 1) ^ {\nu + 1}}.
$$

A partir de maintenant, on fixe un isomorphisme entre la clôture alge-´ brique$\overline { { \mathbb { Q } } } _ { \ell }$de$\mathbb { Q } _ { \ell }$et C.

On dit que$\sigma \in \mathcal { G } _ { \ell } ( V )$est pur de poids$n \in \mathbb { Z }$si pour tout$x \in | V |$les valeurs propres de$\mathrm { F r o b } _ { x } ^ { - 1 }$dans la fibre$\sigma _ { x }$sont de module$q ^ { \frac { n } { 2 } \deg ( x ) }$

On dit que$\sigma$est mixte de poids$\leq n \in \mathbb { Z }$si elle admet une filtration dont tous les quotients successifs sont purs de poids$\leq n$

On a l’autre theorème fondamental suivant dû à Deligne :´

Theor´ eme VI.2.\` – Si σ est mixte de poids$\leq n$, chaque$H _ { c } ^ { \nu } ( \sigma ) , \nu \in \mathbb { N } ,$, est mixte de poids$\leq n + \nu$

Si V est propre et lisse sur$\mathbb { F } _ { q }$et si σ est pur de poids n, chaque$H _ { c } ^ { \nu } ( \sigma )$ $\nu \in \mathbb { N } ,$, est pur de poids$n + \nu$

Si$s \in \mathbb { C }$est tel que$q ^ { s } \in \mathbb { C } \cong \overline { { \mathbb { Q } } } _ { \ell }$soit une unite´ -adique, il definit´ un faisceau -adique lisse$\mathbb { Q } _ { \ell } ( s )$de rang 1 sur Spec$\mathbb { F } _ { q }$et donc, par image reciproque, sur tout sch´ ema´ V de type fini sur$\mathbb { F } _ { q }$. Pour tout$\sigma \in \mathcal { G } _ { \ell } ( V )$, on note alors$\sigma ( s )$le produit tensoriel$\sigma \otimes \mathbb { Q } _ { \ell } ( s )$

On remarque que si s est un nombre complexe arbitraire,$\sigma ( s )$a au moins un sens en tant que faisceau -adique lisse sur$V \otimes _ { \mathbb { F } _ { q } } \overline { { \mathbb { F } } } _ { q }$muni d’une action de Frob ou, si l’on prefère, en tant que repr´ esentation du groupe de Weil´ $W ( V , { \overline { { x } } } )$en n’importe quel point geom´ etrique´$\overline { { x } }$de V.

Des theorèmes VI.1 et VI.2, on d´ eduit le r´ esultat suivant qui permet´ d’extraire les sous-faisceaux irreductibles d’un faisceau´ -adique lisse :

Corollaire VI.3. – Soit V un schema de type fini et g´ eom´ etriquement con-´ nexe sur$\mathbb { F } _ { q } .$

Soient$\sigma \in \mathcal { G } _ { \ell } ( V )$unfaisceau -adique mixte depoids ≤ n et$\sigma ^ { \prime } \in \mathcal { G } _ { \ell } ( V )$ unfaisceau -adique irreductible et pur de poids m.´

Alors dans la zone

$$
| Z | <   q ^ {\frac {m - n}{2} - \dim V + \frac {1}{2}}
$$

la fraction rationnelle$\operatorname { L } _ { V } ( \sigma \otimes { \check { \sigma } } ^ { \prime } , Z )$n’a pas de zero. Elle y a des pôles´ exactement en les points de la forme$\operatorname { \dot { } q } ^ { - \dim ^ { \cdot } V - s }$tels que$\begin{array} { r } { \operatorname { R e s } = \frac { n - m } { 2 } } \end{array}$et que $\sigma ^ { \prime } ( - s )$soit un sous-faisceau de$\sigma _ { i }$, et l’ordre d’un tel pôle est egal à la´ multiplicite de´$\sigma ^ { \prime } ( - s )$dans$\sigma$.

Demonstration :´ Compte tenu des theorèmes VI.1 et VI.2, cela r´ esulte´ de ce que chaque espace$H _ { c } ^ { 2 \dim V } ( \sigma \otimes \check { \sigma } ^ { \prime } \otimes \mathbb { Q } _ { \ell } ( \dim V + s ) )$est dual de Hom$( \sigma ^ { \prime } ( - s ) , \sigma )$!"

## b) Facteurs L locaux en les places ramifiees et´ equation fonctionnelle´

A partir de maintenant, on considère à nouveau la courbe projective, lisse et geom´ etriquement connexe´$X$sur le corps de base$\mathbb { F } _ { q }$. On rappelle que $F$designe son corps des fonctions,´$F _ { x }$le complet´ e de´$\bar { F }$en n’importe quel point ferme´$x \in | X |$et$O _ { x }$le sous-anneau des entiers de$F _ { x }$

Considerons´$\sigma _ { x }$un faisceau -adique lisse sur Spec$F _ { x }$(qu’on peut voir aussi comme une representation´ -adique du groupe de Galois de$F _ { x } )$. Son image directe par l’immersion ouverte Spec$F _ { x } \hookrightarrow \sec O _ { x }$est un faisceau -adique constructible dont on note${ \overline { { \sigma } } } _ { x }$la fibre au point ferme´ x ; celle-ci peut être vue comme un espace vectoriel muni$\mathrm { d } ^ { \prime }$une action par automorphisme de l’el´ ement de Frobenius´$\mathrm { F r o b } _ { x } = \mathrm { F r o b } ^ { \mathrm { d e g } ( x ) }$

Le facteur L de la representation locale´$\sigma _ { x }$est defini comme la fraction´ rationnelle

$$
\mathrm{L} _ {x} (\sigma_ {x}, Z) = \frac {1}{\det _ {\overline {{\sigma}} _ {x}} \left(\mathrm{Id} - \operatorname{Frob} _ {x} ^ {- 1} \cdot Z ^ {\deg (x)}\right)}.
$$

De cette definition, on d´ eduit facilement :´

Lemme VI.4. – Soient$\sigma _ { x }$un faisceau -adique lisse sur Spec$F _ { x }$et$\chi _ { x }$ un faisceau -adique inversible sur Spec$F _ { x } ~ ( c ^ { \prime } e s t - \dot { a } - d i r e$un caractère du groupe de Galois de$F _ { x } )$. Alors :

(i) Si$\sigma _ { x }$et$\chi _ { x }$sont non ramifies´ (c’est-à-dire s’etendent en des faisceaux´ -adiques lisses sur Spec$O _ { x } )$, on a

$$
\mathrm{L} _ {x} \left(\chi_ {x} \otimes \sigma_ {x}, Z\right) = \frac {1}{\det _ {\chi_ {x} \otimes \sigma_ {x}} \left(\operatorname{Id} - \operatorname{Frob} _ {x} ^ {- 1} \cdot Z ^ {\deg (x)}\right)}.
$$

(ii) Si$\sigma _ { x }$est non ramifie mais´$\chi _ { x }$est ramifie, on a´

$$
\mathrm{L} _ {x} (\chi_ {x} \otimes \sigma_ {x}, Z) = 1.
$$

(iii)$S i \chi _ { x }$est suffisamment ramifie enfonction de´$\sigma _ { x . }$, on a

$$
\mathrm{L} _ {x} (\chi_ {x} \otimes \sigma_ {x}, Z) = 1.
$$

On note$\mathcal { G } _ { \ell } ( F )$l’ensemble des faisceaux -adiques lisses sur Spec F qui $\mathrm {  ~ s ~ } ^ { \prime }$etendent en un faisceau lisse sur un ouvert de la courbe´ X. Si l’on prefère,´ ${ \mathrm { c } } ^ { \prime }$est l’ensemble des faisceaux -adiques lisses$\sigma$sur Spec$F$dont l’image directe par le morphisme Spec$F \hookrightarrow X$, notee encore´$\sigma$, est un faisceau constructible sur$X$qui est lisse sur un ouvert non vide.

Chaque tel$\sigma$induit des faisceaux -adiques lisses$\sigma _ { x }$sur les Spec$F _ { x }$et les fibres du faisceau constructible$\sigma$en les points fermes´$x \in | X |$sont egales´ aux$\overline { { \sigma } } _ { x }$. Les fractions rationnelles$\mathrm { L } _ { x } ( \sigma _ { x } , Z )$sont les facteurs L locaux de$\sigma$ en toutes les places$x \in | X |$

On a le resultat suivant de Deligne :´

Proposition VI.5. – Soit$\sigma \in { \mathcal { G } } _ { \ell } ( F )$un faisceau -adique qui est lisse et pur de poids$n \in \mathbb { Z }$sur un ouvert non vide de la courbe X.

Alors, en tout$x \in | X |$, chaque pôle de lafraction rationnelle

$$
\mathrm{L} _ {x} (\sigma_ {x}, Z)
$$

a un module de laforme

$$
q ^ {\frac {- n + m}{2}}
$$

pour un certain entier$m \geq 0 .$

Demonstration :´ Voir le theorème 1.8.4 de [Deligne].´

A tout el´ ement´$\sigma \in \mathcal { G } _ { \ell } ( F )$, on peut maintenant associer une fonction L globale sur la courbe X toute entière

$$
\mathrm{L} (\sigma , Z) = \prod_ {x \in | X |} \mathrm{L} _ {x} (\sigma_ {x}, Z)
$$

qui est certainement bien definie en tant que s´ erie formelle en l’ind´ eter-´ minee´ Z. D’après le theorème VI.1,´${ \mathrm { c } } '$est une fraction rationnelle.

Tout faisceau -adique$\sigma \in \mathcal { G } _ { \ell } ( F )$a un dual$\check { \sigma } \in \mathcal { G } _ { \ell } ( F )$. Leurs fonctions L globales sont reliees par l’´ equation fonctionnelle de Grothendieck :´

Theor´ eme VI.6.\` – Pour tout faisceau -adique$\sigma \in \mathcal { G } _ { \ell } ( F )$, les fractions rationnelles$\mathrm { L } ( \sigma , Z )$et$\mathrm { L } ( \check { \sigma } , Z )$verifient l’´ equation fonctionnelle´

$$
\mathrm{L} (\sigma , Z) = \varepsilon (\sigma , Z) \mathrm{L} \left(\check {\sigma}, \frac {1}{q Z}\right)
$$

où

$$
\varepsilon (\sigma , Z) = \prod_ {\nu = 0} ^ {2} \left[ \det _ {H _ {c} ^ {\nu} (\sigma)} (- \operatorname{Frob} ^ {- 1} \cdot Z) \right] ^ {(- 1) ^ {\nu + 1}}
$$

est le produit d’une constante non nulle et d’une puissance de$Z .$

Demonstration :´ On note encore$\sigma$et$\check { \sigma }$les faisceaux -adiques constructibles obtenus par prolongement sur la courbe X tout entière. Leurs groupes de cohomologie sont notes´$H _ { c } ^ { \nu } ( \sigma )$et$H _ { c } ^ { \nu } ( \check { \sigma } ) , 0 \leq \nu \leq 2$

D’après le theorème VI.1 de Grothendieck, on a les interpr ´ etations co-´ homologiques

$$
\mathrm{L} (\sigma , Z) = \prod_ {\nu} \left[ \det _ {H _ {c} ^ {\nu} (\sigma)} (\mathrm{Id} - \operatorname{Frob} ^ {- 1} \cdot Z) \right] ^ {(- 1) ^ {\nu + 1}},
$$

$$
\mathrm{L} (\check {\sigma}, Z) = \prod_ {\nu} \left[ \det _ {H _ {c} ^ {\nu} (\check {\sigma})} (\mathrm{Id} - \operatorname{Frob} ^ {- 1} \cdot Z) \right] ^ {(- 1) ^ {\nu + 1}}.
$$

D’autre part, le complexe -adique dualisant sur la courbe lisse X est $\mathbb { Q } _ { \ell } ( 1 ) [ 2 ]$et on a un quasi-isomorphisme

$$
R \mathcal {H} o m (\sigma , \mathbb {Q} _ {\ell} (1) [ 2 ]) \xrightarrow {\sim} \check {\sigma} (1) [ 2 ].
$$

Il resulte alors de la dualit´ e de Grothendieck que pour tout´ ν,$H _ { c } ^ { \nu } ( \sigma )$est dual de$H _ { c } ^ { 2 - \nu } ( \check { \sigma } ) ( 1 )$. L’equation fonctionnelle´$\mathrm {  ~ s ~ } ^ { \prime }$en deduit.´!"

## c) Facteurs ε locaux etformule du produit de Laumon

Notant comme toujours A l’anneau des adèles du corps des fonctions F de X, on fixe un caractère additif non trivial$\psi$de$\mathbb { A } / F$. Ses composantes $\psi _ { x }$en les places$x \in \left| X \right|$sont des caractères additifs non triviaux des$F _ { x }$ On sait que le choix de ψ est equivalent à celui d’une forme diff´ erentielle´ meromorphe non triviale sur la courbe´ X.

En toute place$x \in \left| X \right|$, on sait associer aux faisceaux -adiques lisses $\sigma _ { x }$sur Spec$F _ { x }$des facteurs ε locaux

$$
\varepsilon_ {x} (\sigma_ {x}, Z, \psi_ {x})
$$

qui sont le produit d’une constante non nulle et d’une puissance positive ou negative de l’ind´ etermin´ ee´ Z (voir le paragraphe 3.1.5 de [Laumon, 1987]).

On sait les calculer en particulier dans les cas simples suivants :

Lemme VI.7. – En une place$x \in | X |$, soient$\sigma _ { x }$unfaisceau -adique lisse de rang r et$\chi _ { x }$unfaisceau -adique inversible sur Spec$F _ { x }$. Alors :

(i) Si$\sigma _ { x }$est non ramifie, on a´

$$
\varepsilon_ {x} \left(\chi_ {x} \otimes \sigma_ {x}, Z, \psi_ {x}\right) = \varepsilon_ {x} \left(\chi_ {x}, Z, \psi_ {x}\right) ^ {r - 1} \varepsilon_ {x} \left(\chi_ {x} \otimes \det (\sigma_ {x}), Z, \psi_ {x}\right)
$$

lequel vaut 1 si$\chi _ { x }$et$\psi _ { x }$sont egalement non ramifi´ es.´ (ii) (Deligne, Henniart) Si$\chi _ { x }$est suffisamment ramifie en fonction de´$\sigma _ { x }$, on a aussi

$$
\varepsilon_ {x} \left(\chi_ {x} \otimes \sigma_ {x}, Z, \psi_ {x}\right) = \varepsilon_ {x} \left(\chi_ {x}, Z, \psi_ {x}\right) ^ {r - 1} \varepsilon_ {x} \left(\chi_ {x} \otimes \det \left(\sigma_ {x}\right), Z, \psi_ {x}\right).
$$

On rappelle que les el´ ements´$\sigma ~ \in ~ \mathcal { G } _ { \ell } ( F )$induisent des faisceaux - adiques lisses$\sigma _ { x }$sur le complet´ e´$F _ { x }$en toute place x. Et d’après l’assertion (i) du lemme ci-dessus, les facteurs ε locaux

$$
\varepsilon_ {x} (\sigma_ {x}, Z, \psi_ {x})
$$

valent 1 en toutes les places x sauf un nombre fini. Leur produit est bien defini et il v´ erifie la formule fondamentale suivante d´ emontr´ ee par Laumon :´

Theor´ eme VI.8.\` – Pour tout faisceau -adique$\sigma ~ \in ~ \mathcal { G } _ { \ell } ( F )$, le facteur $\varepsilon ( \sigma , Z )$de l’equation fonctionnelle du th´ eorème´ VI.6 se decompose en´

$$
\varepsilon (\sigma , Z) = \prod_ {x \in | X |} \varepsilon_ {x} (\sigma_ {x}, Z, \psi_ {x}).
$$

## d) La correspondance de Langlands globale

Commençons par rappeler la definition des repr´ esentations automorphes´ cuspidales de$\mathrm { G L } _ { r } ( \mathbb { A } )$dont le caractère central est d’ordre fini.

Tout d’abord, une forme automorphe cuspidale en rang r est une fonction

$$
\varphi : \mathrm{GL} _ {r} (\mathbb {A}) \to \mathbb {C}
$$

qui verifie les propri´ et´ es suivantes :´

• Elle est invariante à gauche par le sous-groupe discret$\mathrm { G L } _ { r } ( F )$de $\mathrm { G L } _ { r } ( \mathbb { A } )$

• Elle est invariante à droite par un sous-groupe ouvert de${ \mathrm { G L } } _ { r } ( \mathbb { A } )$

• Il existe un el´ ement´$a \in \mathbb { A } ^ { \times }$de degre non nul tel que´

$$
\varphi (a g) = \varphi (g), \forall g \in \mathrm{GL} _ {r} (\mathbb {A}).
$$

• Pour tout sous-groupe parabolique standard$P \subsetneq { \mathrm { G L } } _ { r }$de radical unipotent$N _ { P }$et si$d n _ { P }$designe une mesure de Haar sur´$N _ { P } ( \mathbb { A } )$, on a

$$
\int_ {N _ {P} (F) \backslash N _ {P} (\mathbb {A})} d n _ {P} \cdot \varphi (n _ {P} g) = 0, \forall g \in \mathrm{GL} _ {r} (\mathbb {A}).
$$

On note Aut<sup>r</sup> l’espace de ces formes automorphes cuspidales. Il est muni d’une action à droite du groupe$\mathrm { G L } _ { r } ( \mathbb { A } )$par translation ou, si l’on prefère,´ de l’algèbre de Hecke$\mathcal { H } ^ { r } = C _ { c } ^ { \infty } ( \mathbf { G } \mathrm { L } _ { r } ( \mathbb { A } ) )$par convolution. Comme tel, il est somme directe de representations admissibles irr´ eductibles de´$\mathrm { G L } _ { r } ( \mathbb { A } )$ ou${ \mathcal { H } } ^ { r }$; ce sont les representations automorphes cuspidales de´$\mathrm { G L } _ { r } ( \mathbb { A } )$dont le caractère central est d’ordre fini. On note$\mathcal { A } ^ { r } ( F )$leur ensemble.

D’autre part, on note$\mathcal { J } _ { \ell } ^ { r } ( F )$l’ensemble des faisceaux -adiques$\sigma \in$ $\mathcal { G } _ { \ell } ( F )$qui sont irreductibles de rang ´ r et dont le determinant est d’ordre fini ´ au sens que

$$
(\det \sigma) ^ {\otimes n} \cong \mathbb {Q} _ {\ell} \quad \text { pour   un   entier } n \neq 0  .
$$

On dit qu’une representation automorphe cuspidale´$\pi$de$\mathrm { G L } _ { r } ( \mathbb { A } )$et un faisceau -adique$\sigma \in { \mathcal { G } } _ { \ell } ( F )$irreductible de rang´ r se correspondent au sens de Langlands si en toute place$x \in | X |$où π et σ sont non ramifiees, la´ famille des valeurs propres de Hecke

$$
z _ {1} (\pi_ {x}), \dots , z _ {r} (\pi_ {x})
$$

et la famille des valeurs propres de Frobenius

$$
z _ {1} (\sigma_ {x}), \ldots , z _ {r} (\sigma_ {x})
$$

se confondent à l’ordre près, ce qui s’ecrit encore´

$$
\mathrm{L} _ {x} (\pi_ {x}, Z) = \mathrm{L} _ {x} (\sigma_ {x}, Z).
$$

L’objet du present travail est de d ´ emontrer l’ ´ enonc ´ e suivant propos ´ e par´ Langlands :

## Theor´ eme VI.9.\` –

(i) Pour tout entier$r \geq 1$, la correspondance de Langlands definit une´ bijection

$$
\pi \mapsto \sigma_ {\pi}
$$

de l’ensemble$\mathcal { A } ^ { r } ( F )$sur l’ensemble$\mathcal { J } _ { \ell } ^ { r } ( F )$

De plus, une representation automorphe cuspidale´$\pi \in { \mathcal { A } } ^ { r } ( F )$et le faisceau -adique$\sigma \in \mathcal { G } _ { \ell } ^ { r } ( F )$qui lui correspond sont ramifies exacte-´ ment en les mêmes places.

(ii) Pour toutepaire de representations automorphes cuspidales´ π$\in { \mathcal { A } } ^ { r } ( F )$ $\pi ^ { \prime } \in \mathcal { A } ^ { r ^ { \prime } } ( F )$de rangs r,$r ^ { \prime } \geq 1$et si$\sigma \in \mathcal { G } _ { \ell } ^ { r } ( F ) , \sigma ^ { \prime } \in \mathcal { G } _ { \ell } ^ { r ^ { \prime } } ( F )$sont les faisceaux -adiques qui leur correspondent, on a en toute place$x \in | X |$ les identites´

$$
\mathrm{L} _ {x} \left(\pi_ {x} \times \pi_ {x} ^ {\prime}, Z\right) = \mathrm{L} _ {x} \left(\sigma_ {x} \otimes \sigma_ {x} ^ {\prime}, Z\right),
$$

$$
\varepsilon_ {x} \big (\pi_ {x} \times \pi_ {x} ^ {\prime}, Z, \psi_ {x} \big) = \varepsilon_ {x} \big (\sigma_ {x} \otimes \sigma_ {x} ^ {\prime}, Z, \psi_ {x} \big).
$$

Remarque : Le cas particulier du rang 1 dans cet enonc´ e est la th´ eorie du´ corps de classes sur le corps de fonctions F. La première demonstration´ geom´ etrique en fut donn´ ee par Lang et Rosenlicht (voir le livre [Serre]).´

Notre demonstration va se faire en partant de ce cas d´ ejà connu, par´ recurrence sur le rang´ r et en gen´ eralisant la d´ emonstration de Drinfeld du´ cas$r = 2$!"

En même temps, nous allons prouver :

## Theor´ eme VI.10.\` –

(i) (Conjecture de Ramanujan-Petersson) Pour tout entier$r \geq 1$et toute representation automorphe cuspidale´$\pi \in { \mathcal { A } } ^ { r } ( F )$, les facteurs locaux $\pi _ { x }$de π en toutes les places$x \in | X |$sont temper´ es.´

En particulier, en les places$x \in | X |$où$\pi _ { x }$est non ramifie, ses valeurs´ propres de Hecke verifient´

$$
\left| z _ {i} \left(\pi_ {x}\right) \right| = 1, 1 \leq i \leq r.
$$

(ii) (Hypothèse de Riemann gen´ eralis´ ee´ ) Pour toute paire de representa-´ tions automorphes cuspidales$\pi \in \mathcal { A } ^ { r } ( F ) , \pi ^ { \prime } \in \mathcal { A } ^ { r ^ { \prime } } ( F )$de rangs r, $r ^ { \prime } \geq 1$, tous les zeros de lafonction´ L globale

$$
\mathrm{L} (\pi \times \pi^ {\prime}, Z)
$$

sont sur le cercle

$$
| Z | = q ^ {- 1 / 2}.
$$

Remarque : On a dejà vu dans le livre [Lafforgue, 1997] que (i) implique´ (ii). Bien sûr, (ii) est aussi une consequence imm´ ediate de (i) et du th´ eorème´ VI.9 d’après le theorème VI.1 (interpr´ etation cohomologique des fonc-´ tions L) de Grothendieck et le theorème VI.2 (puret´ e) de Deligne.´!"

## e) Hypothèse de recurrence et r´ eductions´

A partir de maintenant, on fixe un entier$r \geq 2$

On commence par remarquer qu’à toute$\pi \in { \mathcal { A } } ^ { r } ( F )$il ne peut correspondre au sens de Langlands qu’au plus une$\sigma \in \mathcal { G } _ { \ell } ^ { r } ( F )$, comme il resulte du´ theorème de densit´ e de Chebotarev. Et r´ eciproquement, à toute´$\sigma \in \mathcal { G } _ { \ell } ^ { r } ( F )$ ne peut correspondre qu’au plus une$\pi \in { \mathcal { A } } ^ { r } ( F )$d’après le “theorème de´ multiplicite un fort” de Piatetski-Shapiro.´

Precisons le pas de r´ ecurrence :´

Proposition VI.11. – Supposons les theorèmes´ VI.9 et VI.10(i) dejà connus´ en tous les rangs < r. Alors :

(i) Pour toutfaisceau -adique$\sigma \in \mathcal { G } _ { \ell } ^ { r } ( F )$, on peut construire une repre-´ sentation automorphe cuspidale$\pi \in { \mathcal { A } } ^ { r } ( F )$non ramifiee partout où´ σ est non ramifie et qui lui corresponde au sens de Langlands.´

(ii) Si de plus on sait associer à toute$\pi \in { \mathcal { A } } ^ { r } ( F )$un faisceau -adique $\sigma _ { \pi } \in \mathcal { G } _ { \ell } ^ { r } ( F )$non ramifie partout où´ π est non ramifiee, pur de poids´ 0 et qui lui corresponde au sens de Langlands, on peut conclure que les theorèmes´ VI.9 et VI.10(i) sont connus en tous les$r a n g s \le r$

Demonstration :´ Le theorème VI.9 est d´ ejà connu en rang 1. Cela signifie´ qu’on peut identifier les caractères d’ordre fini de$F ^ { \times } \backslash \mathbb { A } ^ { \times }$aux faisceaux -adiques de rang 1 et d’ordre fini$\chi \in \mathcal { G } _ { \ell } ^ { 1 } ( F )$. Cette identification respecte les facteurs L et ε locaux en toutes les places.

(i) Considerons donc un faisceau´ -adique irreductible´$\sigma ~ \in ~ \mathcal { G } _ { \ell } ^ { r } ( F )$et notons S l’ensemble fini des places$x \in | X |$où$\sigma$est ramifie.´

En toute place x$\notin \ S .$, on note$\pi _ { x }$la representation irr´ eductible non´ ramifiee de´$\bar { \mathrm { G L } } _ { r } ( F _ { x } )$dont les valeurs propres de Hecke sont les$z _ { 1 } ( \sigma _ { x } )$ $\dots , z _ { r } ( \sigma _ { x } )$. En les places$x \in S$, on peut certainement choisir une representation´$\pi _ { x }$de$\mathrm { G L } _ { r } ( F _ { x } )$qui est irreductible et induite de type de´ Whittaker et dont le caractère central$\chi _ { \pi _ { \lambda } }$correspond à det$( \sigma _ { x } )$. Ainsi, $\pi = \otimes \pi _ { x }$est une representation lisse admissible irr´ eductible de´${ \mathrm { G L } } _ { r } ( \mathbb { A } )$ x∈|X|

dont le caractère central$\chi _ { \pi } = \bigotimes \chi _ { \pi } ,$correspond à det$\sigma$.

Soit$\chi = \bigotimes _ { x \in | X | } \chi _ { x }$un caractère d’ordre fini de$F ^ { \times } \backslash \mathbb { A } ^ { \times }$qui est très ramifie´

en les places$x \in S$. On veut montrer que si$\pi ^ { \prime } = \bigotimes \pi _ { x } ^ { \prime } \in \mathcal { A } ^ { r ^ { \prime } } ( F )$est une x∈|X|

representation automorphe cuspidale en rang´$r ^ { \prime } < r$qui est non ramifiee en´ les places$x \in S$, les deux series formelles´

$$
\mathrm{L} (\chi \pi \times \pi^ {\prime}, Z) \quad \text {et} \quad \mathrm{L} (\chi^ {- 1} \check {\pi} \times \check {\pi} ^ {\prime}, Z)
$$

sont des polynômes et satisfont l’equation fonctionnelle´

$$
\mathrm{L} \left(\chi \pi \times \pi^ {\prime}, Z\right) = \varepsilon \left(\chi \pi \times \pi^ {\prime}, Z\right) \mathrm{L} \left(\chi^ {- 1} \check {\pi} \times \check {\pi} ^ {\prime}, \frac {1}{q Z}\right),
$$

ce qui permettra d’appliquer le theorème B.13.´

Or d’après l’hypothèse de recurrence´$\pi ^ { \prime }$correspond au sens de Langlands à un faisceau -adique$\sigma ^ { \prime } \in \mathcal { G } _ { \ell } ^ { r ^ { \prime } } ( F )$si bien que$\chi \pi ^ { \prime }$et$\chi \otimes \sigma ^ { \prime }$se correspondent et ont les mêmes facteurs L et ε locaux en toutes les places.

En les places x$\notin S .$, le facteur$\pi _ { x }$est non ramifie et on a automatiquement´

$$
\mathrm{L} _ {x} \left(\chi_ {x} \pi_ {x} \times \pi_ {x} ^ {\prime}, Z\right) = \mathrm{L} _ {x} \left(\sigma_ {x} \otimes \chi_ {x} \otimes \sigma_ {x} ^ {\prime}, Z\right),
$$

$$
\mathrm{L} _ {x} \big (\chi_ {x} ^ {- 1} \check {\pi} _ {x} \times \check {\pi} _ {x} ^ {\prime}, Z \big) = \mathrm{L} _ {x} \big (\check {\sigma} _ {x} \otimes \chi_ {x} ^ {- 1} \otimes \check {\sigma} _ {x} ^ {\prime}, Z \big),
$$

$$
\varepsilon_ {x} \left(\chi_ {x} \pi_ {x} \times \pi_ {x} ^ {\prime}, Z, \psi_ {x}\right) = \varepsilon_ {x} \left(\sigma_ {x} \otimes \chi_ {x} \otimes \sigma_ {x} ^ {\prime}, Z, \psi_ {x}\right).
$$

D’autre part, en les places$x \in S$, le facteur$\pi _ { x } ^ { \prime }$est non ramifie si bien´ que si$\chi _ { x }$a et´ e choisi suffisamment ramifi´ e en fonction de´$\pi _ { x }$et$\sigma _ { x }$, on a d’après le lemme B.3, le lemme VI.4(iii) et le lemme VI.7(ii)

$$
\mathrm{L} _ {x} \left(\chi_ {x} \pi_ {x} \times \pi_ {x} ^ {\prime}, Z\right) = 1 = \mathrm{L} _ {x} \left(\sigma_ {x} \otimes \chi_ {x} \otimes \sigma_ {x} ^ {\prime}, Z\right),
$$

$$
\mathrm{L} _ {x} \left(\chi_ {x} ^ {- 1} \check {\pi} _ {x} \times \check {\pi} _ {x} ^ {\prime}, Z\right) = 1 = \mathrm{L} _ {x} \left(\check {\sigma} _ {x} \otimes \chi_ {x} ^ {- 1} \otimes \check {\sigma} _ {x} ^ {\prime}, Z\right)
$$

et

$$
\begin{array}{r l} & {\varepsilon_ {x} \big (\chi_ {x} \pi_ {x} \times \pi_ {x} ^ {\prime}, Z, \psi_ {x} \big) = \varepsilon_ {x} \big (\chi_ {x}, Z, \psi_ {x} \big) ^ {r r ^ {\prime} - 1} \varepsilon_ {x} \big (\chi_ {x} \chi_ {\pi_ {x}} ^ {r ^ {\prime}} \chi_ {\pi_ {x} ^ {\prime}} ^ {r}, Z, \psi_ {x} \big)} \\ & {\qquad = \varepsilon_ {x} \big (\chi_ {x}, Z, \psi_ {x} \big) ^ {r r ^ {\prime} - 1} \varepsilon_ {x} \big (\det (\sigma_ {x}) ^ {r ^ {\prime}} \chi_ {x} \det \big (\sigma_ {x} ^ {\prime} \big) ^ {r}, Z, \psi_ {x} \big)} \\ & {\qquad = \varepsilon_ {x} \big (\sigma_ {x} \otimes \chi_ {x} \otimes \sigma_ {x} ^ {\prime}, Z, \psi_ {x} \big).} \end{array}
$$

On en deduit´

$$
\mathrm{L} (\chi \pi \times \pi^ {\prime}, Z) = \mathrm{L} (\sigma \otimes \chi \otimes \sigma^ {\prime}, Z),
$$

$$
\mathrm{L} \left(\chi^ {- 1} \check {\pi} \times \check {\pi} ^ {\prime}, Z\right) = \mathrm{L} \left(\check {\sigma} \otimes \chi^ {- 1} \otimes \check {\sigma} ^ {\prime}, Z\right)
$$

et d’après la formule du produit de Laumon

$$
\varepsilon (\chi \pi \times \pi^ {\prime}, Z) = \varepsilon (\sigma \otimes \chi \otimes \sigma^ {\prime}, Z).
$$

On voit dejà que´$\mathrm { L } ( \chi \pi \times \pi ^ { \prime } , Z )$et$\operatorname { L } ( \chi ^ { - 1 } \check { \pi } \times \check { \pi } ^ { \prime } , Z )$sont des fractions rationnelles qui verifient´

$$
\mathrm{L} \left(\chi \pi \times \pi^ {\prime}, Z\right) = \varepsilon \left(\chi \pi \times \pi^ {\prime}, Z\right) \mathrm{L} \left(\chi^ {- 1} \check {\pi} \times \check {\pi} ^ {\prime}, \frac {1}{q Z}\right).
$$

Il reste à voir que ce sont des polynômes. Mais ceci resulte de l’interpr´ etation´ cohomologique de Grothendieck

$$
\mathrm{L} (\sigma \otimes \chi \otimes \sigma^ {\prime}, Z) = \prod_ {\nu = 0} ^ {2} \left[ \det _ {H _ {c} ^ {\nu} (\sigma \otimes \chi \otimes \sigma^ {\prime})} (\mathrm{Id} - \operatorname{Frob} ^ {- 1} \cdot Z) \right] ^ {(- 1) ^ {\nu + 1}}
$$

$$
\mathrm{L} (\check {\sigma} \otimes \chi \otimes \check {\sigma} ^ {\prime}, Z) = \prod_ {\nu = 0} ^ {2} \left[ \det _ {H _ {c} ^ {\nu} (\check {\sigma} \otimes \chi^ {- 1} \otimes \check {\sigma} ^ {\prime})} (\mathrm{Id} - \operatorname{Frob} ^ {- 1} \cdot Z) \right] ^ {(- 1) ^ {\nu + 1}}
$$

puisque, comme$\sigma$et$\sigma ^ { \prime }$sont irreductibles de rangs´ r et$r ^ { \prime }$differents, les´ $\quad \overline { { { H _ { c } ^ { \nu } ( \sigma \otimes \chi \otimes \sigma ^ { \prime } ) } } }$et$H _ { c } ^ { \nu } ( \check { \sigma } \otimes \chi \otimes \check { \sigma } ^ { \prime } )$sont nuls pour$\nu = 0$ou 2.

D’après le theorème B.13, on peut maintenant affirmer que quitte à´ changer les facteurs irreductibles´$\pi _ { x }$de$\pi$en les places$x \in S$, la representation´ $\chi \pi$est automorphe$( \mathrm { c } ^ { \prime } \mathrm { e s t - \dot { a } - d i r e }$se represente comme sous-quotient de´ l’espace des formes automorphes sur$\bar { \mathbf { G L } } _ { r } ( F ) \backslash \mathbf { G L } _ { r } ( \mathbb { A } ) )$et donc aussi$\pi =$ $\bigotimes \pi _ { x }$

x∈|X|

Si$S = \emptyset$, on sait même que$\chi \pi$et π sont automorphes cuspidales et on a termine.´

Si$S \neq \emptyset .$, il reste encore à prouver que π est cuspidale. Raisonnant par l’absurde, supposons que ce n’est pas le cas. D’après Langlands, il existe une partition non triviale$r = r _ { 1 } + \cdots + r _ { k }$de l’entier r et des representations´ automorphes cuspidales$\pi ^ { 1 } , \ldots , \pi ^ { k }$de$\mathrm { G L } _ { r _ { 1 } } ( \mathbb { A } ) , \dots , \mathrm { G L } _ { r _ { k } } ( \bar { \mathbb { A } } )$non ramifiees en dehors de´ S telles que pour tout x ∈/ S l’ensemble des valeurs propres de Hecke

$$
z _ {1} (\pi_ {x}), \ldots , z _ {r} (\pi_ {x})
$$

soit la reunion disjointe sur les´$i , 1 \leq i \leq k$, des familles

$$
z _ {1} \left(\pi_ {x} ^ {i}\right), \dots , z _ {r _ {i}} \left(\pi_ {x} ^ {i}\right).
$$

Par hypothèse de recurrence, les´$\pi ^ { 1 } , \ldots , \pi ^ { k }$correspondent au sens de Langlands à des faisceaux -adiques$\sigma ^ { 1 } , \dots , \sigma ^ { k } \in \mathcal { G } _ { \ell } ( \mathbf { \hat { F } } )$irreductibles de rangs´ $r _ { 1 } , \ldots , r _ { k }$. Le faisceau irreductible´$\sigma$et le faisceau semi-simple$\sigma ^ { 1 } \oplus \cdots \oplus \sigma ^ { k }$ ont les mêmes valeurs propres de Frobenius en tous les points x$\notin S . D ^ { \prime }$après le theorème de densit´ e de Chebotarev´${ \mathrm { c } } ^ { \prime }$est impossible.

Pour demontrer la partie (ii) de la proposition, on a besoin du lemm´ e suivant :

Lemme VI.12. – En une place$x _ { 0 } \in | X |$, soit$\pi _ { x _ { 0 } }$une representation ad-´ missible irreductible supercuspidale de´${ \mathrm { G L } } _ { r } ( F _ { x _ { 0 } } )$dont le caractère central $\chi _ { \pi _ { x _ { 0 } } }$est d’ordre fini.

Alors il existe une representation automorphe cuspidale´$\pi \in { \mathcal A } ^ { r } ( F )$ dont le facteur en$x _ { 0 }$est$\pi _ { x _ { 0 } }$

Demonstration du lemme :´ On reprend celle du lemme 15.10 de [Laumon, Rapoport, Stuhler] mais sans demander autant de conditions.

Soit a un el´ ement de degr´ e non nul dans´$F _ { x _ { 0 } } ^ { \times }$pour lequel$\chi _ { \pi _ { x _ { 0 } } } ( a ) = 1$ D’après le theorème 2.42 de [Bernstein, Zelevinski], il existe une fonct´ ion $h _ { x _ { 0 } } \mathsf { \tilde { e } } C _ { c } ^ { \infty } ( \mathrm { G L } _ { r } ( F _ { x _ { 0 } } ) / a ^ { \mathbb { Z } } )$telle que

$$
\mathrm{Tr} _ {\pi_ {x _ {0}}} (h _ {x _ {0}}) \neq 0
$$

mais que pour toute autre representation admissible irr´ eductible´$\pi _ { x _ { 0 } } ^ { \prime }$de ${ \mathrm { G L } } _ { r } ( { \bar { F } } _ { x _ { 0 } } )$verifiant´$\chi _ { \pi _ { x _ { 0 } } ^ { \prime } } ( a ) = 1$, on ait

$$
\mathrm{Tr} _ {\pi_ {x _ {0}} ^ {\prime}} (h _ {x _ {0}}) = 0.
$$

En deux autres places$x _ { 1 }$et$x _ { 2 }$, on choisit deux fonctions supercuspidales $h _ { x _ { 1 } } \in C _ { c } ^ { \infty } ( \mathbf { G } \mathbf { L } _ { r } ( F _ { x _ { 1 } } ^ { \mathbf { \tilde { \alpha } } } ) )$et$h _ { x _ { 2 } } \in C _ { c } ^ { \infty } ( \mathrm { G L } _ { r } ( F _ { x _ { 2 } } ) )$qui ont au moins une integrale´ orbitale non nulle.

Pour toute fonction$h ^ { x _ { 0 } , x _ { 1 } , x _ { 2 } } \in C _ { c } ^ { \infty } ( \mathrm { G L } _ { r } ( \mathbb { A } ^ { x _ { 0 } , x _ { 1 } , x _ { 2 } } ) )$, on peut former le produit$h = h _ { x _ { 0 } } \otimes h _ { x _ { 1 } } \otimes h _ { x _ { 2 } } \otimes h ^ { x _ { 0 } , x _ { 1 } , x _ { 2 } }$dans$C _ { c } ^ { \infty } ( \mathrm { G L } _ { r } ( \mathbb { A } ) / a ^ { \mathbb { Z } } )$

La trace tronquee d’Arthur´$\mathrm { T r } ^ { \le p } ( h )$d’une telle fonction h ne depend pas´ du polygone de troncature$p$et d’après le theorème 10 du paragraphe V.2d´ de [Lafforgue, 1997], elle s’ecrit´

$$
\mathrm{Tr} (h) = \sum_ {\gamma} \int_ {\mathrm{GL} _ {r} (F) _ {\gamma} \setminus \mathrm{GL} _ {r} (\mathbb {A}) / a ^ {\mathbb {Z}}} d g \cdot h (g ^ {- 1} \gamma g)
$$

où$\gamma$decrit un ensemble de repr´ esentants des classes de conjugaison´ d’el´ ements elliptiques de´${ \mathrm { G L } } _ { r } ( F )$et${ \mathrm { G L } } _ { r } ( F ) _ { \gamma }$designe leurs sous-groupes´ de commutateurs.

Les fonctions$h _ { x _ { 0 } } , h _ { x _ { 1 } } , h _ { x _ { 2 } }$etant d´ ejà fix´ ees, on peut choisir´$h ^ { x _ { 0 } , x _ { 1 } , x _ { 2 } }$de façon que

$$
\operatorname{Tr} (h) \neq 0.
$$

D’autre part, la formule des traces d’Arthur-Selberg (voir le theorème´ 12 du paragraphe VI.2f de [Lafforgue, 1997])$\mathrm {  ~ s ~ } ^ { \prime }$ecrit ici simplement´

$$
\operatorname{Tr}(h) = \sum_{\substack{\pi \in \mathcal{A}^{r}(F)\\ \chi_{\pi}(a) = 1}}\operatorname{Tr}_{\pi}(h).
$$

Il y a donc un$\pi \in { \mathcal { A } } ^ { r } ( F )$tel que$\mathrm { T r } _ { \pi } ( h ) \neq 0$. Comme h comprend$h ^ { x _ { 0 } }$ en facteur, la composante de$\pi$en x ne peut être que$\pi _ { x _ { 0 } }$!"

Demonstration de la proposition VI.11(ii) :´ Soit$\pi \in { \mathcal { A } } ^ { r } ( F )$. On sait dejà´ qu’il lui correspond un faisceau -adique$\sigma \in { \mathcal { G } } _ { \ell } ^ { r } ( F )$qui est non ramifie´ exactement là où$\pi$est non ramifie et qui est pur de poids 0.´

De même, soient$r ^ { \prime } \leq r$un entier,$\pi ^ { \prime } \in { \mathcal { A } } ^ { r ^ { \prime } } ( F )$et$\sigma ^ { \prime }$le faisceau -adique pur de poids 0 qui correspond à$\pi ^ { \prime }$dans$\mathcal { G } _ { \ell } ^ { r ^ { \prime } } ( F )$

Notons S l’ensemble fini des places$x \in \left| X \right|$où$\pi _ { x }$ou$\pi _ { x } ^ { \prime }$est ramifie.´ Il resulte du lemme B.1 et des lemmes VI.4(i)(ii) et VI.7(i) que p´ our tous caractères d’ordre fini$\chi , \chi ^ { \prime } \in \mathcal { A } ^ { 1 } ( F ) = \mathcal { G } _ { \ell } ^ { 1 } ( F )$, on a en toute place$x \notin S$

$$
\mathrm{L} _ {x} \big (\chi_ {x} \pi_ {x} \times \chi_ {x} ^ {\prime} \pi_ {x} ^ {\prime}, Z \big) = \mathrm{L} _ {x} \big (\chi_ {x} \chi_ {x} ^ {\prime} \otimes \sigma_ {x} \otimes \sigma_ {x} ^ {\prime}, Z \big),
$$

$$
\mathrm{L} _ {x} \left(\chi_ {x} ^ {- 1} \check {\pi} _ {x} \times \chi_ {x} ^ {\prime - 1} \check {\pi} _ {x} ^ {\prime}, Z\right) = \mathrm{L} _ {x} \left(\chi_ {x} ^ {- 1} \chi_ {x} ^ {\prime - 1} \otimes \check {\sigma} _ {x} \otimes \check {\sigma} _ {x} ^ {\prime}, Z\right),
$$

$$
\varepsilon_ {x} \big (\chi_ {x} \pi_ {x} \times \chi_ {x} ^ {\prime} \pi_ {x} ^ {\prime}, Z, \psi_ {x} \big) = \varepsilon_ {x} \big (\chi_ {x} \chi_ {x} ^ {\prime} \otimes \sigma_ {x} \otimes \sigma_ {x} ^ {\prime}, Z, \psi_ {x} \big).
$$

D’après le lemme B.3 et les lemmes VI.4(iii) et VI.7(ii), ces egalit´ es sont´ egalement v´ erifi´ ees en n’importe quelle place´$x \in S$dès que$\chi _ { x } \chi _ { x } ^ { \prime }$est suffisamment ramifie.´

Comme les produits de ces facteurs L et$\varepsilon$locaux verifient les´ equations´ fonctionnelles

$$
\mathrm{L} (\chi \pi \times \chi^ {\prime} \pi^ {\prime}, Z) = \varepsilon (\chi \pi \times \chi^ {\prime} \pi^ {\prime}, Z) \mathrm{L} \left(\chi^ {- 1} \check {\pi} \times \chi^ {\prime - 1} \check {\pi} ^ {\prime}, \frac {1}{q Z}\right),
$$

$$
\mathrm{L} \left(\chi \chi^ {\prime} \otimes \sigma \otimes \sigma^ {\prime}, Z\right) = \varepsilon \left(\chi \chi^ {\prime} \otimes \sigma \otimes \sigma^ {\prime}, Z\right) \mathrm{L} \left(\chi^ {- 1} \chi^ {\prime - 1} \otimes \check {\sigma} \otimes \check {\sigma} ^ {\prime}, \frac {1}{q Z}\right),
$$

on deduit de la proposition B.11 qu’en toute place´ x

$$
\frac {\mathrm{L} _ {x} \left(\pi_ {x} \times \pi_ {x} ^ {\prime} , Z\right)}{\varepsilon_ {x} \left(\pi_ {x} \times \pi_ {x} ^ {\prime} , Z , \psi_ {x}\right) \mathrm{L} _ {x} \left(\check {\pi} _ {x} \times \check {\pi} _ {x} ^ {\prime} , \frac {1}{q Z}\right)} = \frac {\mathrm{L} _ {x} \left(\sigma_ {x} \otimes \sigma_ {x} ^ {\prime} , Z\right)}{\varepsilon_ {x} \left(\sigma_ {x} \otimes \sigma_ {x} ^ {\prime} , Z , \psi_ {x}\right) \mathrm{L} _ {x} \left(\check {\sigma} _ {x} \otimes \check {\sigma} _ {x} ^ {\prime} , \frac {1}{q Z}\right)}.
$$

D’après la proposition VI.5, on sait aussi que les pôles de$\operatorname { L } _ { x } ( \sigma _ { x } \otimes \sigma _ { x } ^ { \prime } , Z )$ et$\mathrm { L } _ { x } ( \check { \sigma } _ { x } \otimes \check { \sigma } _ { x } ^ { \prime } , \frac { 1 } { q Z } )$ne se rencontrent pas et que leurs modules sont des puissances de$q ^ { \frac { 1 } { 2 } }$.

En une place$x \ \in \ | X |$où$\pi _ { x }$est ramifie, soit´$\rho$une representation´ supercuspidale irreductible de caractère central d’ordre fini qui apparaît à´ torsion près dans l’ecriture de Bernstein et Zelevinski de´$\pi _ { x } . \mathrm { ~ D ~ } ^ { \prime }$’après le lemme VI.12 ci-dessus, on a pu choisir$\pi ^ { \prime }$de façon que$\pi _ { x } ^ { \prime } = \check { \rho }$. Comme $\pi _ { x }$est unitaire et admet un modèle de Whittaker et que$\pi _ { x } ^ { \prime }$est temper´ ee, le´ corollaire B.7 dit que$\mathrm { L } _ { x } ( \pi _ { x } \times \pi _ { x } ^ { \prime } , Z )$et$\begin{array} { r } { \mathrm { L } _ { x } ( \check { \pi } _ { x } \times \check { \pi } _ { x } ^ { \prime } , \frac { 1 } { q Z } ) } \end{array}$n’ont pas de pôle commun. Donc

$$
\mathrm{L} _ {x} \left(\pi_ {x} \times \pi_ {x} ^ {\prime}, Z\right) = \mathrm{L} _ {x} \left(\sigma_ {x} \otimes \sigma_ {x} ^ {\prime}, Z\right)
$$

et les pôles de$\operatorname { L } _ { x } ( \pi _ { x } \times \pi _ { x } ^ { \prime } , Z ) = \operatorname { L } _ { x } ( \pi _ { x } \times { \check { \rho } } , Z )$ont pour modules des puissances de$q ^ { \frac { 1 } { 2 } }$. D’après le theorème B.5 et la proposition B.6, cela implique´ que$\pi _ { x }$est temper´ ee.´

On revient maintenant à un$\pi ^ { \prime }$gen´ eral de rang´$r ^ { \prime } \leq r$, tout en sachant desormais que les´$\pi _ { x }$et$\pi _ { x } ^ { \prime }$sont temper´ es. D’après le corollaire B.7,´ $\mathrm { L } _ { x } ( \pi _ { x } \times \pi _ { x } ^ { \prime } , Z )$et$\begin{array} { r } { \mathrm { L } _ { x } ( \check { \pi } _ { x } \times \check { \pi } _ { x } ^ { \prime } , \frac { 1 } { q Z } ) } \end{array}$n’ont jamais de pôle commun et on peut conclure qu’en toute place$x \in | X |$

$$
\mathrm{L} _ {x} (\pi_ {x} \times \pi_ {x} ^ {\prime}, Z) = \mathrm{L} _ {x} (\sigma_ {x} \otimes \sigma_ {x} ^ {\prime}, Z)
$$

et

$$
\varepsilon_ {x} \left(\pi_ {x} \times \pi_ {x} ^ {\prime}, Z, \psi_ {x}\right) = \varepsilon_ {x} \left(\sigma_ {x} \otimes \sigma_ {x} ^ {\prime}, Z, \psi_ {x}\right).
$$

On a demontr´ e tout ce´$\mathrm { \ q u ^ { \prime } }$on voulait.

## 2) Cohomologie essentielle des champs de chtoucas

## a) Cohomologie -adique des chtoucas et de leurs compactifications

On fixe donc un entier$r \geq 2$et on fait l’hypothèse de recurrence que le´ theorème VI.9 et le th´ eorème VI.10(i) sont d´ ejà connus en tous les rangs´ $< r . { \mathrm { D } } ^ { \prime } { \mathrm { a p r e s } }$la proposition VI.11, on sait aussi associer à tout faisceau -adique$\sigma \in \mathcal { G } _ { \ell } ^ { r } ( F )$une representation automorphe cuspidale´$\pi \in { \mathcal { A } } _ { \ell } ^ { r } ( F )$ qui est non ramifiee partout où´ σ est non ramifie et lui correspond au sens´ de Langlands.

Pour terminer la recurrence, il suffit de construire pour toute´$\pi \in { \mathcal { A } } _ { \ell } ^ { r } ( F )$ un faisceau$\sigma _ { \pi } \in \mathcal { G } _ { \ell } ^ { r } ( F )$qui est non ramifie partout où´ π est non ramifiee,´ est pur de poids 0 et correspond à$\pi$.

Il suffit même de traiter le cas où le caractère central$\chi _ { \pi }$de$\pi$verifie´ $\chi _ { \pi } ( a ) = 1$pour un certain idèle$a \in \mathbb { A } ^ { \times }$de degre deg´ (a) = 1 que l’on fixe. Etant donne un niveau arbitraire´$N = \sec { \mathcal { O } _ { N } } \hookrightarrow X$, on rappelle que$\mathcal { H } _ { N } ^ { r }$designe la sous-algèbre de l’algèbre de Hecke´${ \mathcal { H } } ^ { r }$de${ \mathrm { G L } } _ { r } ( \mathbb { A } )$ constituee des fonctions invariantes à droite et à gauche par´$K _ { N } = \mathrm { K e r } [ K =$ $\operatorname { G L } _ { r } ( O _ { \mathbb { A } } ) \to \operatorname { G L } _ { r } ( { \mathcal { O } } _ { N } ) ]$; elle admet un el´ ement unit´ e´ 11$N$qui est le quotient de la fonction caracteristique de ´$K _ { N }$par son volume. Il s’agit d’associer à toute representation automorphe cuspidale´

$$
\pi \in \{\pi \} _ {N} ^ {r} = \left\{\pi \in \mathcal {A} ^ {r} (F) \mid \chi_ {\pi} (a) = 1 \wedge \pi \cdot \mathbb {1} _ {N} \neq 0 \right\}
$$

un faisceau -adique$\sigma _ { \pi } \in \mathcal { G } _ { \ell } ^ { r } ( F )$non ramifie sur´$X - N$, pur de poids 0 et qui correspond à π au sens de Langlands.

Notant$F ^ { 2 } = \operatorname { F r a c } ( F \otimes _ { \mathbb { F } _ { q } } F )$le corps des fonctions de la surface$X \times X$ et$q ^ { \prime } , q ^ { \prime \prime } : X \times X \implies X$les deux projections de celle-ci sur la courbe X, nous allons construire les$\sigma _ { \pi }$en identifiant dans la cohomologie -adique à supports compacts des$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$au-dessus de Spec$F ^ { 2 }$des morceaux de la forme$q ^ { \prime * } \sigma _ { \pi } \otimes q ^ { \prime \prime * } \check { \sigma } _ { \pi } ( 1 \overset { \cdot } { - } r )$

On rappelle que si$p : [ 0 , r ] \to \mathbb { R } _ { + }$est un polygone de troncature assez convexe en fonction de X, on a construit des compactifications$\overline { { \mathrm { C h t } ^ { r , d , \overline { { { p } } } \leq p } } }$ des$\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p }$qui sont propres sur$X \times X$et lisses sur$\mathbb { A } ^ { r - 1 } / \mathbb { G } _ { m } ^ { r - 1 }$. Pour $N \hookrightarrow X$un niveau non vide et si p est assez convexe en fonction de X et N, les normalisations$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$des$\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } \times _ { X \times X } ( X - N ) \times ( X - N )$ dans les$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p }$sont propres sur$( X - N ) \times ( X - N )$et lisses sur $( X - N ) \times ( X - N ) \times { \mathcal { C } } _ { N } ^ { r }$. L’ouvert$\mathcal { C } _ { N } ^ { \prime r }$de$\mathcal { C } _ { N } ^ { r }$est lisse sur$\mathbb { A } ^ { r - 1 } / \mathbb { G } _ { m } ^ { r - 1 }$si bien que les ouverts images reciproques´$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$dans les$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } }$sont lisses sur$( X - N ) \times ( X - N ) \times \mathbb { A } ^ { r - 1 } / \mathbb { G } _ { m } ^ { r - 1 }$. Quand$\mathcal { C } _ { N } ^ { r }$admet une resolution´ des singularites´$\widetilde { \mathcal { C } } _ { N } ^ { r }$lisse sur le champ torique$\widetilde { \mathcal { A } } ^ { r , N } / \mathcal { A } _ { \varnothing } ^ { r , N }$quotient d’une variet´ e torique lisse´$\displaystyle \widetilde { \mathcal { A } } ^ { r , N }$par son tore$\mathcal { A } _ { \varnothing } ^ { r , N }$(par exemple si N n’a pas de multiplicites ou si´$r = 2 )$, les$\mathrm { C h t } _ { N } ^ { r , \overline { { d , p } } \leq p } = \overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } } \times _ { \mathcal { C } _ { N } ^ { r } } \widetilde { \mathcal { C } } _ { N } ^ { r }$sont propres sur$( X - N ) \times ( X - N )$et lisses sur$( \boldsymbol { X } - \boldsymbol { N } ) \times ( \boldsymbol { X } - \boldsymbol { N } ) \times \widetilde { \mathcal { A } } ^ { r , N } / \mathcal { A } _ { \mathcal { Q } } ^ { r , N }$. Les bords des$\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p }$, des$\overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p ^ { \prime } } } }$ou eventuellement des´$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p }$sont des diviseurs à croisements normaux relatifs ; ils se decomposent en strates´ ouvertes et en strates fermees qui sont les images r´ eciproques des points de´ $\mathbb { A } ^ { r - 1 } / \mathbb { G } _ { m } ^ { r - 1 } ( \mathrm { o u } \mathcal { \widetilde { A } } ^ { r , N } / \mathcal { A } _ { \varnothing } ^ { r , N } )$et de leurs adherences sch´ ematiques.´

D’après la proposition V.1, tous ces champs sur$X { \times } X$ou$( X { - } N ) { \times } ( X { - } N )$ sont sereins et de même les$\mathrm { C h t } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } , \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$ou$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$

Si X est un ouvert$\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p } , \mathrm { C h t } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$, un compactifie´$\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \le p } } }$ $\mathrm { C h t } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$ou une strate de bord ouverte ou fermee de celui-ci, on notera´ $H _ { c } ^ { \nu } ( { \mathfrak { X } } )$les faisceaux de cohomologie -adique à supports compacts de$\mathfrak { X }$ au-dessus de$X \times X$. D’après le theorème´$\mathsf { A } . 9 ( \mathrm { i } )$, ce sont des faisceaux -adiques lisses sur$X \times X$

Pour N un niveau non vide, C un champ algebrique repr´ esentable quasi-´ projectif sur$\begin{array} { r } { \mathfrak { C } _ { N } ^ { r } , \mathfrak { X } = \mathbf { C } \mathrm { h t } _ { N } ^ { r , d , \overline { { p } } \leq p } \times _ { \mathfrak { C } _ { N } ^ { r } } \mathfrak { C } } \end{array}$ou$\mathfrak { X } = \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } \times _ { \mathfrak { C } _ { N } ^ { r } } \mathfrak { C }$et$\mathcal { F }$un complexe de faisceaux -adiques sur C, on notera$H _ { c } ^ { \nu } ( { \mathfrak { X } } , { \mathcal { F } } )$les faisceaux de cohomologie -adique à supports compacts au-dessus de$( X - N ) \times ( X - N )$ du complexe sur X deduit de´$\mathcal { F }$via le morphisme lisse de restriction de X $\grave { \textrm { a } } N$

$$
\operatorname{Res}: \overline {{\operatorname{Cht} _ {N} ^ {r , d , \overline {{p}} \leq p}}}, \overline {{\operatorname{Cht} _ {N} ^ {r , \overline {{p}} \leq p}}} / a ^ {\mathbb {Z}} \longrightarrow \mathcal {C} _ {N} ^ {r}.
$$

Ici encore, il resulte du th´ eorème A.9(i) que les´$H _ { c } ^ { \nu } ( { \mathfrak { X } } , { \mathcal { F } } )$sont des faisceaux -adiques lisses sur$( X - N ) \times ( X - N )$. Quand$\mathcal { F }$est le faisceau constant $\mathbb { Q } _ { \ell }$[resp. le complexe d’intersection], on notera simplement$H _ { c } ^ { \nu } ( { \mathfrak { X } } , { \mathcal { F } } ) =$ $H _ { c } ^ { \nu } ( { \mathfrak { X } } )$[resp.$H _ { c } ^ { \nu } ( { \mathfrak { X } } , { \mathcal { F } } ) = I H _ { c } ^ { \nu } ( { \mathfrak { X } } ) ]$

Si X est egal à´${ \overline { { \mathrm { { C h t } } ^ { r , d , \overline { { p } } \leq p } } } } , { \overline { { \mathrm { { C h t } } ^ { r , \overline { { p } } \leq p } } } } / a ^ { \mathbb { Z } }$(ou eventuellement´$\mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p }$ $\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z } )$ou à une de leurs strates fermees, les faisceaux´ -adiques lisses $H _ { c } ^ { \nu } ( { \vec { x } } )$sur$X \times X \mathrm { ( o u } ( X - N ) \times ( X - N ) )$sont purs de poids ν. De même, si$\mathcal { C }$est un champ representable projectif sur´$\mathcal { C } _ { N } ^ { r }$et$\begin{array} { r } { \mathfrak { X } = \overline { { \mathrm { C h t } _ { N } ^ { r , d , \overline { { p } } \leq p } } } \times _ { \mathcal { C } _ { N } ^ { r } } \mathfrak { C } } \end{array}$ ou$\mathfrak { X } = \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z } \times _ { \mathfrak { C } _ { N } ^ { r } } \mathfrak { C }$, les faisceaux -adiques lisses$I H _ { c } ^ { \nu } ( { \mathfrak { X } } )$sur $( X - N ) \times ( \ddot { X } - N )$sont purs de poids$\nu .$

Dans tous les cas, on notera$H _ { c } ^ { \nu } ( { \mathfrak { X } } ) ^ { s s } , I H _ { c } ^ { \nu } ( { \mathfrak { X } } ) ^ { s s } , H _ { c } ^ { \nu } ( { \mathfrak { X } } , { \mathcal { F } } ) ^ { s s }$les semi-simplifies des ´ H<sup>ν</sup>(X), IH<sup>ν</sup>(X),$H _ { c } ^ { \nu } ( { \mathfrak { X } } , { \mathcal { F } } )$et$H _ { c } ^ { * } ( { \mathfrak { X } } ) , \ { \overline { { I } } } H _ { c } ^ { * } ( { \mathfrak { X } } ) , \ H _ { c } ^ { * } ( { \mathfrak { X } } , { \mathcal { F } } )$ les faisceaux -adiques virtuels

$$
H _ {c} ^ {*} (\mathfrak {X}) = \sum_ {\nu} (- 1) ^ {\nu} H _ {c} ^ {\nu} (\mathfrak {X}) ^ {s s},
$$

$$
I H _ {c} ^ {*} (\mathfrak {X}) = \sum_ {\nu} (- 1) ^ {\nu} I H _ {c} ^ {\nu} (\mathfrak {X}) ^ {s s},
$$

$$
H _ {c} ^ {*} (\mathfrak {X}, \mathcal {F}) = \sum_ {\nu} (- 1) ^ {\nu} H _ {c} ^ {\nu} (\mathfrak {X}, \mathcal {F}) ^ {s s}.
$$

## b) Faisceaux ou representations´ -adiques r-negligeables´

On rappelle que$q ^ { \prime }$et$q ^ { \prime \prime }$designent les deux projections´$X \times X \Longrightarrow X$

On choisit un point geom´ etrique´$\eta$de$X \times X$supporte par le point´ gen´ erique Spec´$F ^ { 2 }$et on note$\eta ^ { \prime } , \eta ^ { \prime \prime }$ses images par$q ^ { \prime }$et$q ^ { \prime \prime }$.

Pour tous ouverts$X ^ { \prime }$et$X ^ { \prime \prime }$de$X$, on a des homomorphismes induits entre groupes fondamentaux

$$
\pi_ {1} (X ^ {\prime} \times X ^ {\prime \prime}, \eta) \rightarrow \pi_ {1} (X ^ {\prime}, \eta^ {\prime}), \pi_ {1} (X ^ {\prime} \times X ^ {\prime \prime}, \eta) \rightarrow \pi_ {1} (X ^ {\prime \prime}, \eta^ {\prime \prime})
$$

au-dessus de${ \widehat { \mathbb { Z } } } .$, et entre groupes de Weil

$$
W (X ^ {\prime} \times X ^ {\prime \prime}, \eta) \rightarrow W (X ^ {\prime}, \eta^ {\prime}), W (X ^ {\prime} \times X ^ {\prime \prime}, \eta) \rightarrow W (X ^ {\prime \prime}, \eta^ {\prime \prime})
$$

au-dessus de$\mathbb { Z } .$. L’endomorphisme de Frobenius partiel$\mathrm { F r o b } _ { X } \times \mathrm { I d } _ { X }$ne fixe pas$\eta$mais il definit certainement un homomorphisme de´ Z dans le groupe des automorphismes exterieurs de´$W ( X ^ { \prime } \times X ^ { \prime \prime } , \bar { \eta } )$et donc un groupe $\bar { \mathbb { Z } } W ( \mathbf { \hat { X } ^ { \prime } } \times X ^ { \prime \prime } , \boldsymbol { \eta } )$s’inscrivant dans une suite exacte

$$
1 \to W (X ^ {\prime} \times X ^ {\prime \prime}, \eta) \to \mathbb {Z} W (X ^ {\prime} \times X ^ {\prime \prime}, \eta) \to \mathbb {Z} \to 0.
$$

On dispose aussi des groupes de Galois$G _ { F ^ { 2 } } ^ { \eta } = \pi _ { 1 } ( \mathrm { S p e c } F ^ { 2 } , \eta ) , G _ { F } ^ { \eta ^ { \prime } } =$ $\pi _ { 1 } ( { \mathrm { S p e c } } F , \eta ^ { \prime } ) , G _ { F } ^ { \eta ^ { \prime \prime } } = \pi _ { 1 } ( { \mathrm { S p e c } } F , \eta ^ { \prime \prime } )$et des groupes de Weil$W _ { F ^ { 2 } } ^ { \eta } =$ $G _ { F ^ { 2 } } ^ { \eta } \times _ { \widehat { \mathbb { Z } } } \mathbb { Z } , W _ { F } ^ { \eta ^ { \prime } } = G _ { F } ^ { \eta ^ { \prime } } \times _ { \widehat { \mathbb { Z } } } \mathbb { Z } , W _ { F } ^ { \eta ^ { \prime \prime } } = G _ { F } ^ { \eta ^ { \prime \prime } } \times _ { \widehat { \mathbb { Z } } } \mathbb { Z }$que relient les homomor-<sub>phismes</sub>$q ^ { \prime } : W _ { F ^ { 2 } } ^ { \eta }  W _ { F } ^ { \eta ^ { \prime } } , q ^ { \prime \prime } : W _ { F ^ { 2 } } ^ { \eta }  W _ { F } ^ { \eta ^ { \prime \prime } }$<sub>au-dessus de</sub>$\mathbb { Z }$et$\mathrm { F r o b } _ { X } \times \mathrm { I d } _ { X }$ definit une extension´$\mathbb { Z } W _ { F ^ { 2 } } ^ { \eta }$de$\mathbb { Z }$par$W _ { F ^ { 2 } } ^ { \eta }$. On a :

## Lemme VI.13. –

(i) Pour tous ouverts$X ^ { \prime }$et$X ^ { \prime \prime }$de X, le groupe$\mathbb { Z } W ( X ^ { \prime } \times X ^ { \prime \prime } , \eta )$est naturellement muni d’un homomorphisme continu et surjectif

$$
\mathbb {Z} W (X ^ {\prime} \times X ^ {\prime \prime}, \eta) \rightarrow W (X ^ {\prime}, \eta^ {\prime}) \times W (X ^ {\prime \prime}, \eta^ {\prime \prime})
$$

qui prolonge$W ( X ^ { \prime } \times X ^ { \prime \prime } , \eta )  [ W ( X ^ { \prime } , \eta ^ { \prime } ) \times W ( X ^ { \prime \prime } , \eta ^ { \prime \prime } ) ] \times _ { \mathbb { Z } \times \mathbb { Z } } \mathbb { Z } .$

(ii) De même,$\mathbb { Z } W _ { F ^ { 2 } } ^ { \eta }$est naturellement muni d’un homomorphisme continu et surjectif

$$
\mathbb {Z} W _ {F ^ {2}} ^ {\eta} \to W _ {F} ^ {\eta^ {\prime}} \times W _ {F} ^ {\eta^ {\prime \prime}}
$$

qui prolonge$( q ^ { \prime } , q ^ { \prime \prime } ) : W _ { F ^ { 2 } } ^ { \eta } \to [ W _ { F } ^ { \eta ^ { \prime } } \times W _ { F } ^ { \eta ^ { \prime \prime } } ] \times _ { \mathbb { Z } \times \mathbb { Z } } \mathbb { Z } .$

Demonstration´$\therefore \mathit { \Omega } ( \mathrm { i } )$resulte de ce que, d’après Drinfeld, la cat´ egorie des´ paires de revêtements finis etales de´${ \hat { X ^ { \prime } } }$et$X ^ { \prime \prime }$est equivalente à celle´ des revêtements finis etales de´$X ^ { \prime } \times X ^ { \prime \prime }$munis d’un relèvement de $\mathrm { F r o b } _ { X } \times \mathrm { I d } _ { X }$

(ii) est une consequence´ evidente de (i).´

On pose la definition suivante qui nous permettra d’enlever de la coho-´ mologie des Ch$\stackrel { r , \overline { { p } } \leq p } { \mathbb { I } _ { N } } / a ^ { \mathbb { Z } }$ou de leurs compactifications tout ce qui n’est pas interessant pour nous :´

Definition VI.14.´ – Un faisceau -adique [resp. virtuel] dans$\mathcal { G } _ { \ell } ( F ^ { 2 } )$ou plus gen´ eralement une repr´ esentation de´$\boldsymbol { W } _ { F ^ { 2 } } ^ { \eta }$sera dit r-negligeable si tous´ ses sous-quotients irreductibles´ [resp. ses composantes] sont des facteurs directs defaisceaux ou de representations de laforme´

$$
q ^ {\prime *} \sigma^ {\prime} \otimes q ^ {\prime \prime *} \sigma^ {\prime \prime},
$$

avec$\sigma ^ { \prime } , \sigma ^ { \prime \prime }$deux faisceaux -adiques dans$\mathcal { G } _ { \ell } ( F )$ou deux representations´ $W _ { F } ^ { \eta ^ { \prime } }$$W _ { F } ^ { \eta ^ { \prime \prime } }$irreductibles de rangs´$< r$

Il sera dit essentiel si aucun de ses sous-quotients irreductibles´ [resp. aucune de ses composantes]$n '$est r-negligeable.´

Remarque : Attention !

Même si$\sigma ^ { \prime }$et$\sigma ^ { \prime \prime }$sont irreductibles,´$q ^ { \prime * } \sigma ^ { \prime } \otimes q ^ { \prime \prime * } \sigma ^ { \prime \prime }$ne l’est pas necessaire-´ ment. Mais d’après le lemme VI.13(ii), elle est toujours semi-simple, ses facteurs apparaissent avec la même multiplicite et ils sont images les uns´ des autres par les puissances de Frob$\boldsymbol { x } \times \operatorname { I d } _ { X }$. Leur nombre est egal à celui´ des caractères non ramifies´$\chi$tels que$\sigma ^ { \prime } \otimes \chi ^ { - 1 } \cong \sigma ^ { \prime }$et$\sigma ^ { \prime \prime } \otimes \chi \cong \sigma ^ { \prime \prime }$et il divise les rangs$r ^ { \prime }$et$r ^ { \prime \prime }$de$\sigma ^ { \prime }$et$\sigma ^ { \prime \prime }$

On dira qu’un faisceau semi-simple [resp. virtuel] dans$\mathcal { G } _ { \ell } ( F ^ { 2 } )$ou plus gen´ eralement une telle repr´ esentation de´$W _ { F ^ { 2 } } ^ { \bar { \eta } }$est r-negligeable complet´$\mathrm { s } \mathrm { \ddot { 1 } l }$ est somme d’objets de la forme$q ^ { \prime * } \sigma ^ { \prime } \otimes q ^ { \prime \prime ^ { * } } \sigma ^ { \prime \prime }$avec$\sigma ^ { \prime } , \sigma ^ { \prime \prime }$irreductibles de´ rangs$< r$. Pour qu’un tel σ r-negligeable soit complet, il faut et il suffit qu’il´ soit invariant par Frob$\boldsymbol { x } \times \operatorname { I d } _ { X }$et même s’il ne l’est pas,$\bigoplus _ { n = 1 } ^ { r ! } ( \mathrm { F r o b } _ { X } ^ { n } \times \mathrm { I d } _ { X } ) ^ { * } \sigma$ $\operatorname { o u } \sum _ { n = 1 } ^ { r ! } ( \operatorname { F r o b } _ { X } ^ { n } \times \operatorname { I d } _ { X } ) ^ { * } \sigma ^ { \downarrow } { \operatorname { e s t . } }$!"

En même temps que les theorèmes VI.9 et VI.10(i) en rang ´ r, nous allons prouver :

Proposition VI.15. – Pour tout polygone de troncature$p : [ 0 , r ] \to \mathbb { R } _ { + }$ (assez convexe enfonction de X et N), on a :

(i) Tous les faisceaux de cohomologie -adique à supports compacts $H _ { c } ^ { \nu } ( { \mathfrak { X } } )$du bord${ \mathfrak { X } } = { \mathrm { C h t } } ^ { r , { \overline { { p } } } \leq p } / a ^ { \mathbb { Z } } - { \mathrm { C h t } } ^ { r , { \overline { { p } } } \leq p } / a ^ { \mathbb { Z } } { \mathrm { ~ } } ( s i \mathrm { ~ } N \ = \ \varnothing )$ou eventuellement´$\mathfrak { X } = \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } - \mathrm { C h t } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$(si$N \neq \emptyset$et$\mathcal { C } _ { N } ^ { r }$ admet une resolution des singularit´ es´$\widetilde { \mathcal { C } } _ { N } ^ { r } )$sont r-negligeables.´

De même, si$N \neq \varnothing , \mathfrak { X } = \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \le p } / a ^ { \mathbb { Z } }$et$\mathcal { F }$est la restriction au bord$\mathcal { C } _ { N } ^ { r } - \mathcal { C } _ { N , \emptyset } ^ { r }$du complexe d’intersection sur$\mathcal { C } _ { N } ^ { r }$, tous lesfaisceaux -adiques lisses$H _ { c } ^ { \nu } ( { \mathfrak { X } } , { \mathcal { F } } )$sont r-negligeables.´

(ii) Les faisceaux de cohomologie$H _ { c } ^ { \nu } ( { \mathfrak { X } } )$de toute strate de bord ouverte ou fermee´ X de$\mathrm { C h t } ^ { r , \overline { { { p } } } \leq p } / a ^ { \mathbb { Z } } ( s i N = \varnothing ) , \mathrm { C h t } _ { N } ^ { r , \overline { { { p } } } \leq p ^ { \prime } } / a ^ { \mathbb { Z } } ( s i N \neq \varnothing )$ou eventuellement´$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$sont r-negligeables.´

(iii) Les$H _ { c } ^ { \nu } ( { \bf C h t } _ { N } ^ { r , \overline { { { p } } } \leq p } / a ^ { \mathbb { Z } } ) s o n t ( r + 1 ) \overline { { - n \not e g l i g e a b l e s . } }$

Remarque : Pour$r = 1$, il n’y a pas de troncature ni de bord et (iii) se prouve facilement sans calcul.

En effet,$\mathrm { C h t } _ { N } ^ { 1 } / a ^ { \mathbb Z }$est un revêtement fini etale de´$( X - N ) \times ( X - N )$ Comme il provient par changement de base du revêtement de la variet´ e´ de Picard de X par l’isogenie de Lang, c’est un revêtement ab´ elien et les´ sous-quotients irreductibles des´$H ^ { \nu } ( { \bf C } { \bf \breve { h } t } _ { N } ^ { 1 } / a ^ { \mathbb { Z } } )$sont des caractères. Ils sont necessairement de la forme´$q ^ { \prime * } \chi ^ { \prime } \otimes q ^ { \prime \prime * } \chi ^ { \prime \prime }$car$\mathrm { C h t } _ { N } ^ { 1 } / a ^ { \mathbb Z }$est muni de l’action des endomorphismes de Frobenius partiels$\mathrm { F r o b } _ { \infty }$et$\mathrm { F r o b } _ { 0 }$!"

On fait aussi l’hypothèse de recurrence que la proposition VI.15 est d ´ ejà´ connue en les rangs$< r$

## c) Verification de ce que le bord est r-n´ egligeable´

Ce paragraphe est consacre à la d ´ emonstration de la proposition VI.15 (i)´ et (ii).

Commençons par le cas facile où$N = \emptyset$

## Le cas sans niveau :

Il est equivalent de montrer les propri´ et´ es requises pour´$\overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } }$ou pour les$\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \le p } } }$

Comme le bord de chaque$\overline { { \mathrm { C h t } ^ { r , d , \overline { { p } } \le p } } }$et ses strates fermees sont r´ eunions´ disjointes des strates ouvertes$\mathrm { { q u } ^ { \prime } i }$ls contiennent, il suffit d’après le lemme de devissage A.15 de v´ erifier que les faisceaux de cohomologie´ -adique à supports compacts sur$X \times X$des strates ouvertes de bord de$\overline { { \mathrm { C h t } ^ { r , d , \overline { { { p } } } \leq p } } }$sont r-negligeables.´

Les strates ouvertes du bord de$\mathrm { C h t } ^ { r , d , \overline { { p } } \leq p }$sont indexees par les partitions´ non triviales$\underline { { r } } = ( r _ { 1 } , \ldots , r _ { k } )$de l’entier r ; on les a notees´$\mathrm { C h t } _ { r } ^ { r , d , \mathbf { \tilde { p } } \leq p }$

D’après le corollaire III.4, chacune est munie d’un morphisme

$$
\operatorname{Cht} _ {r} ^ {r, d, \overline {{p}} \leq p} \rightarrow \operatorname{Cht} ^ {r _ {1}, d _ {1}, \overline {{p}} \leq p _ {1}} \times \operatorname{Cht} ^ {r _ {2}, d _ {2}, \overline {{p}} \leq p _ {2}} \times_ {X, \text { Frob }} \dots \times_ {X, \text { Frob }} \operatorname{Cht} ^ {r _ {k}, d _ {k}, \overline {{p}} \leq p _ {k}}
$$

au-dessus de l’endomorphisme$\operatorname { I d } _ { X } \times \operatorname { F r o b } _ { X }$de$X \times X$lequel preserve les´ representations´$r { \mathrm { - n e g l i g e a b l e s } }$. De plus, ce morphisme induit des isomorphismes en cohomologie car${ \mathrm { c } } ^ { \prime }$est le compose´$\bar { \mathrm { d } ^ { \circ } } \mathrm { u n }$morphisme de gerbe et d’un morphisme representable, fini, surjectif et radiciel.´

On est reduit à montrer que la cohomologie à supports compacts de´

$$
\mathcal {C} = \operatorname{Cht} ^ {r _ {1}, d _ {1}, \overline {{p}} \leq p _ {1}} \times_ {X} \operatorname{Cht} ^ {r _ {2}, d _ {2}, \overline {{p}} \leq p _ {2}} \times_ {X, \text { Frob }} \dots \times_ {X, \text { Frob }} \operatorname{Cht} ^ {r _ {k}, d _ {k}, \overline {{p}} \leq p _ {k}}
$$

au-dessus de$X \times X$est r-negligeable. Consid´ erons la factorisation du´ morphisme de structure sur$X \times X$à travers$X \times X ^ { k - 1 } \times X$et notons $q _ { 0 } , q _ { 1 } , \ldots , q _ { k }$les$k + 1$projections de$X \times X ^ { k - 1 } \times X$sur X. D’après les hypothèses de recurrence, la cohomologie à supports compacts de´$\mathcal { C }$audessus de$X \times X ^ { k - 1 } \times X$est composee avec des facteurs directs de faisceaux´ de la forme

$$
\left(q _ {0} ^ {*} \sigma_ {0} \otimes q _ {1} ^ {*} \sigma_ {1} ^ {\prime}\right) \otimes \left(q _ {1} ^ {*} \sigma_ {1} \otimes q _ {2} ^ {*} \sigma_ {2} ^ {\prime}\right) \otimes \dots \otimes \left(q _ {k - 1} ^ {*} \sigma_ {k - 1} \otimes q _ {k} ^ {*} \sigma_ {k} ^ {\prime}\right)
$$

où$\sigma _ { 0 } , \sigma _ { 1 } ^ { \prime } , \sigma _ { 1 } , \sigma _ { 2 } ^ { \prime } , \ldots , \sigma _ { k - 1 } , \sigma _ { k } ^ { \prime }$sont des faisceaux -adiques sur X irreduc-´ tibles de rangs$\leq \operatorname* { m a x } \{ r _ { 1 } , \ldots , r _ { k } \} < r$. D’après la formule de Künneth, la cohomologie de$\mathcal { C }$au-dessus de$X \times X$est alors composee avec des facteurs´ directs de faisceaux de la forme

$$
q _ {0} ^ {*} \sigma_ {0} \otimes \chi \otimes q _ {k} ^ {*} \sigma_ {k} ^ {\prime}
$$

où$\sigma _ { 0 }$et$\sigma _ { k } ^ { \prime }$sont comme ci-dessus et les$\chi$sont des faisceaux -adiques irreductibles donc de rang 1 sur Spec´$\mathbb { F } _ { q }$. Elle est r-negligeable.´!"

Afin de traiter le cas où il y a un niveau$N \neq \emptyset$, on a besoin d’un lemme preparatoire.´

Pour tout entier$d _ { 0 } \geq 1$, on note$W _ { F _ { d _ { 0 } } ^ { 2 } } ^ { \eta } , W _ { F _ { d _ { 0 } } } ^ { \eta ^ { \prime } }$et$W _ { F _ { d _ { 0 } } } ^ { \eta ^ { \prime \prime } }$les sous-groupes de $W _ { F ^ { 2 } } ^ { \eta } , W _ { F } ^ { \eta ^ { \prime } }$et$W _ { F } ^ { \eta ^ { \prime \prime } }$images reciproques de´$d _ { 0 } \mathbb { Z }$dans Z. On a :

## Lemme VI.16. – Soit$d _ { 0 } \geq 1$un entier.

(i) Etant donnee´ σ une representation´ -adique irreductible de´$W _ { F _ { d _ { 0 } } } ^ { \eta ^ { \prime } }$ou $W _ { F _ { d _ { 0 } } } ^ { \eta ^ { \prime \prime } }$, toutes les representations irr ´ eductibles de´$W _ { F } ^ { \eta ^ { \prime } }$ou$W _ { F } ^ { \eta ^ { \prime \prime } }$qui la contiennent ont même dimension ; quand celle-ci est$< r ,$, on dit que$\sigma$ est r-negligeable.´

(ii) Soit σ une representation´ -adique irreductible de´$W _ { F _ { d _ { 0 } } ^ { 2 } } ^ { \eta } . \ S i ,$, parmi les representations irr´ eductibles de´$W _ { F ^ { 2 } } ^ { \eta }$qui la contiennent, l’une est r-negligeable, il en est de même des autres. On dit alors que´ σ est r-negligeable.´

C’est equivalent à demander qu’elle soitfacteur direct d’une rep´ resenta-´ tion de laforme$q ^ { \prime * } \sigma ^ { \prime } \otimes q ^ { \prime \prime * } \dot { \sigma } ^ { \prime \prime }$, avec$\sigma ^ { \prime } , \sigma ^ { \prime \prime }$deux representations irr´ e-´ ductibles r-negligeables de´$W _ { F _ { d _ { 0 } } } ^ { \eta ^ { \prime } } e t W _ { F _ { d _ { 0 } } } ^ { \eta ^ { \prime \prime } }$

Demonstration :´ Cela resulte de ce que le sous-groupe´$W _ { d _ { 0 } } = W _ { F _ { d _ { 0 } } } ^ { \eta ^ { \prime } } , W _ { F _ { d _ { 0 } } } ^ { \eta ^ { \prime \prime } }$ ou$W _ { F _ { d _ { 0 } } ^ { 2 } } ^ { \eta }$est distingue dans´$W = W _ { F } ^ { \eta ^ { \prime } } , W _ { F } ^ { \eta ^ { \prime \prime } }$ou$W _ { F ^ { 2 } } ^ { \eta }$et de ce que le quotient $W / W _ { d _ { 0 } } \overset { \sim } { = } \mathbb { Z } / d _ { 0 } \mathbb { Z }$est abelien. En effet, deux repr´ esentations irr´ eductibles de´ W qui contiennent une même representation irr´ eductible de´$W _ { d _ { 0 } }$ne peuvent alors differer que´$\mathrm { d } ^ { \prime }$une torsion par un caractère de$\mathbb { Z } / d _ { 0 } \mathbb { Z }$!"

Nous pouvons maintenant traiter :

Le cas où il y a un niveau N :

Pour$N = \operatorname { S p e c } { \mathcal { O } } _ { N } \hookrightarrow X$un niveau non vide, les assertions (i) et (ii) de la proposition VI.15 sont des cas particuliers du resultat g ´ en´ eral suivant :´

Proposition VI.17. – Soient p un polygone de troncature assez convexe en fonction de X et N et d$\in \mathbb { Z }$un degre.´

Soient C un champ algebrique repr´ esentable quasi-projectif sur´$\mathcal { C } ^ { r , N }$ et${ \mathfrak { X } } \quad { \xrightarrow { \quad p x \ } } \quad ( X - N ) \times ( X - N )$le champ serein compactifiable sur $( X - N ) \times ( X - N )$qui est defini comme produit fibr´ e dans le carr´ e´ cartesien :´

![](images/page_169_image_8.jpg)

Alors pour tout complexe de faisceaux -adiques constructibles$\mathcal { F }$sur C qui est supporte par le bord´ (l’image reciproque du bord´$\mathcal { C } ^ { r , N } - \mathcal { C } _ { \varnothing } ^ { r , N }$de $\mathcal { C } ^ { r , N } )$, les faisceaux -adiques lisses sur$( X - N ) \times ( X - N )$

$$
R ^ {i} (p _ {\mathfrak {X}})! \mathrm{Res} ^ {*} \mathcal {F}
$$

sont r-negligeables.´

Demonstration :´ Quitte à prolonger$\mathcal { F }$par 0, on peut supposer que$\mathcal { C }$est representable projectif sur´$\hat { \mathcal { C } } ^ { r , N }$et même que$\mathcal { C } = \bar { \mathcal { C } } ^ { r , N }$puisque les foncteurs cohomologiques d’images directes par les morphismes propres commutent aux changements de base.

On se place donc sur${ \mathfrak { X } } = { \overline { { \mathbf { C } \mathbf { h } { \mathfrak { t } } ^ { r , d , { \overline { { p } } } } { \leq } p } } } \times _ { X \times X } \left( X - N \right) \times \left( X - N \right) .$

Raisonnant par recurrence croissante sur la dimension du support, nous´ pouvons supposer le resultat d´ ejà connu pour les faisceaux´ -adiques sur $\bar { \mathsf { C } } ^ { r , N } - \mathsf { C } _ { \varnothing } ^ { r , \bar { N } }$dont le support est de codimension$\qquad > \ c$et nous devons le montrer pour les faisceaux -adiques constructibles$\mathcal { F }$sur$\mathcal { C } ^ { r , N } - \mathcal { C } _ { \varnothing } ^ { r , N }$dont le support est de codimension$\geq c$

D’après le lemme VI.16 et avec ses notations, il suffit de prouver que les$R ^ { i } ( \hat { p } _ { \mathfrak { X } } ) _ { ! } \mathrm { R e s } ^ { * } \mathcal { F }$sont r-negligeables comme repr´ esentations de´$W _ { F _ { d _ { 0 } } ^ { 2 } } ^ { \eta }$pour $d _ { 0 } \geq 1$un entier assez grand.

On peut se limiter au cas où$\mathcal { F }$est un faisceau lisse sur un sous-champ localement ferme´ C de codimension$c$de$\mathcal { C } ^ { r , N }$qui est contenu dans une strate$\mathcal { C } _ { \underline { { r } } } ^ { r , N }$associee à une partition non triviale´$\underline { { r } } = ( r = r _ { 1 } + \cdot \cdot \cdot + r _ { k } )$de l’entier$r _ { \cdot }$.

Comme on a vu au paragraphe 2b du chapitre III, la strate$\widetilde { \mathcal { C } } _ { \underline { { r } } } ^ { r , N }$qui contient$\mathcal { C } _ { \underline { { r } } } ^ { r , N }$comme ouvert est munie d’un morphisme

$$
\widetilde {\mathcal {C}} _ {\underline {{r}}} ^ {r, N} \longrightarrow \overline {{\mathcal {C}}} ^ {\underline {{r}}, N} = \overline {{\mathcal {C}}} _ {\emptyset} ^ {r _ {1}, N} \times_ {\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}} r _ {2} \overline {{\mathcal {C}}} _ {\emptyset} ^ {N} \times \dots \times_ {\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}} r _ {k} \overline {{\mathcal {C}}} _ {\emptyset} ^ {N}  .
$$

D’autre part,$\mathrm { C h t } _ { \underline { { r } } } ^ { r , d , \overline { { p } } \leq p }$est une gerbe dont le groupe de structure est plat, fini et radiciel au-dessus de

$$
\mathrm{Cht} ^ {r, d, \overline {{p}} \leq p} \subset \mathrm{Cht} ^ {r} = \mathrm{Cht} ^ {r _ {1}} \times_ {X} ^ {r _ {2}} \mathrm{Cht} \times \dots \times_ {X} ^ {r _ {k}} \mathrm{Cht}
$$

et on a un carre commutatif :´

$$
\begin{array}{c c c} \operatorname{Cht} _ {\underline {{r}}} ^ {r, d, \overline {{p}} \leq p} & \xrightarrow {(2)} & \widetilde {\mathcal {C}} _ {\underline {{r}}} ^ {r, N} \\ \Big \downarrow & & \Big \downarrow^ {(3)} \\ \operatorname{Cht} _ {\underline {{r}}. d, \overline {{p}} \leq p} & \xrightarrow {(1)} & \overline {{\mathcal {C}}} ^ {\underline {{r}}, N} \end{array}
$$

Dans ce carre, le morphisme (1) est lisse de dimension´$2 r - k + 1$(d’après le lemme II.1), (2) est lisse de dimension$2 r \left( \mathrm { c } \right)$est la proposition III.5) et les groupes d’automorphismes des points de$\widetilde { \mathcal { C } } _ { \underline { { r } } } ^ { r , N }$au-dessus de leurs images dans$\overline { { \mathcal { C } } } ^ { \underline { { r } } , N }$sont geom´ etriquement connexes de dimension´$k - 1 \colon$; il en resulte´ en particulier que tout point de$\overline { { \mathcal { C } } } ^ { \underline { { r } } , N }$n’a dans$\widetilde { \mathcal { C } } _ { \underline { { r } } } ^ { r , N }$(ou plutôt dans l’image ouverte de (2))$\mathrm { \ q u } ^ { \prime }$un nombre fini$\mathrm { d } ^ { \prime }$antec´ edents. Quitte à remplacer´ C par un ouvert dense, on peut supposer que la projection de$\mathcal { C }$sur son image par (3) est le compose d’un morphisme de gerbe dont le groupe de structure´ est plat à fibres geom´ etriquement connexes,´$\mathrm { d } ^ { \prime }$un morphisme fini, plat et radiciel et d’un morphisme fini etale. Puis, quitte à remplacer´$\mathcal { F }$par un faisceau lisse sur C dont il est facteur direct, on peut supposer aussi que$\mathcal { F }$ provient$\mathrm { d } ^ { \prime }$un faisceau lisse sur un sous-champ localement ferme de´$\bar { \mathsf { C } } ^ { { \underline { { r } } } , N }$

Souvenons-nous encore qu’on a deux morphismes radiciels surjectifs

$$
\begin{array}{c} \operatorname{Cht} ^ {r, d, \overline {{p}} \leq p} \longrightarrow \operatorname{Cht} ^ {r _ {1}, d _ {1}, \overline {{p}} \leq p _ {1}} \times_ {X} \operatorname{Cht} ^ {r _ {2}, d _ {2}, \overline {{p}} \leq p _ {2}} \times_ {X, \text {Frob}} \dots \times_ {X, \text {Frob}} \operatorname{Cht} ^ {r _ {k}, d _ {k}, \overline {{p}} \leq p _ {k}} \\ \overline {{\mathcal {C}}} ^ {\underline {{r}}, N} \longrightarrow \overline {{\mathcal {C}}} _ {\emptyset} ^ {r _ {1}, N} \times_ {\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}} \overline {{\mathcal {C}}} _ {\emptyset} ^ {r _ {2}, N} \times_ {\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}, \text {Frob}} \times \dots \times_ {\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}, \text {Frob}} \overline {{\mathcal {C}}} _ {\emptyset} ^ {r _ {k}, N} \end{array}
$$

au-dessus l’un de l’autre.

L’image de$\mathcal { C } _ { \underline { { r } } } ^ { r , N }$dans$\overline { { \mathcal { C } } } _ { \varnothing } ^ { r _ { 1 } , N }$[resp.$\overline { { \mathcal { C } } } _ { \varnothing } ^ { r _ { k } , N } ]$est constituee de “chtoucas´ sur$N ^ { \ast }$qui n’ont pas de pôle [resp. pas de zero]. A isomorphisme près il´$\boldsymbol { \mathrm { n ^ { \prime } y } }$ a qu’un nombre fini de tels chtoucas sur N et on peut supposer que les deux images du support C de$\mathcal { F }$dans$\overline { { \mathcal { C } } } _ { \varnothing } ^ { r _ { 1 } , N }$et$\overline { { \mathcal { C } } } _ { \varnothing } ^ { r _ { k } , N }$consistent en deux points localement fermes´$\widetilde { \mathcal { B } } _ { 1 }$et$\widetilde { \mathcal B } _ { k }$definis sur l’extension´$\mathbb { F } _ { q _ { 0 } }$de$\mathbb { F } _ { q }$de degre´$d _ { 0 }$.

En tant que champs,$\widetilde { \mathcal { B } } _ { 1 }$et B s’ecrivent comme les quotients de Spec´$\mathbb { F } _ { q _ { 0 } }$  par deux groupes d’automorphismes Aut$\widetilde { \mathcal { B } } _ { 1 }$et Aut$\widetilde { \mathcal B } _ { k }$; ceux-ci ont une partie “continue” (la composante de l’unite)´ (Aut$\widetilde { \mathcal { B } } _ { 1 } ) ^ { \mathrm { { c o n t } } }$ou$( \operatorname { A u t } \widetilde { \mathcal { B } } _ { k } )$cont qui est geom´ etriquement connexe et une partie “discrète”´ (Aut${ \mathcal { B } } _ { 1 } ) ^ { \mathrm { d i s c } } =$ Aut$\widetilde { \mathcal { B } } _ { 1 } \big / ( \mathrm { A u t } \widetilde { \mathcal { B } } _ { 1 } ) ^ { \mathrm { c o n t } }$ou$( \operatorname { A u t } \widetilde { \mathcal { B } } _ { k } ) ^ { \mathrm { d i s c } } \ = \ \mathrm { \normalfont ~ \hat { A } u t } \widetilde { \mathcal { B } } _ { k } / ( \operatorname { A u t } \widetilde { \mathcal { B } } _ { k } ) ^ { \mathrm { c o n t } }$qui est un   groupe fini. Les quotients de Spec$\mathbb { F } _ { q _ { 0 } }$par$( \operatorname { A u t } \widetilde { \mathcal { B } } _ { 1 } ) ^ { \mathrm { c o n t } }$et (Aut$\widetilde { \mathcal { B } _ { k } } ) ^ { \mathrm { c o n t } }$defi-´ nissent deux revêtements finis etales galoisiens´$\mathcal { \widetilde { B } } _ { 1 } ^ { \prime }$et$\mathcal { \widetilde { B } } _ { k } ^ { \prime }$de$\widetilde { \mathcal { B } } _ { 1 }$et$\widetilde { \mathcal B } _ { k }$; les    faisceaux -adiques y sont triviaux au sens qu’ils proviennent de Spec$\mathbb { F } _ { q _ { 0 } } .$

On note$\alpha : \mathcal { C } ^ { \prime } \to \mathcal { C }$le revêtement fini etale galoisien de´ C deduit de´ $\widetilde { \mathcal { B } } _ { 1 } ^ { \prime } \times \widetilde { \mathcal { B } } _ { k } ^ { \prime }  \widetilde { \mathcal { B } } _ { 1 } \times \widetilde { \mathcal { B } } _ { k }$par le changement de base$\mathcal { C }  \widetilde { \mathcal { B } } _ { 1 } \times \widetilde { \mathcal { B } } _ { k }$. Le faisceau $\mathcal { F }$  est un facteur direct du faisceau -adique lisse sur C

$$
\mathcal {F} ^ {\prime} = \alpha_ {*} \alpha^ {*} \mathcal {F}
$$

et il suffit de montrer que les$R ^ { \nu } ( p _ { \mathfrak { X } } ) _ { ! } \operatorname { R e s } ^ { * } \mathcal { F } ^ { \prime }$sont r-negligeables comme´ representations de´$W _ { F _ { d _ { 0 } } ^ { 2 } } ^ { \eta }$

L’interêt d’avoir remplac´ e´$\mathcal { F }$par${ \mathcal { F } } ^ { \prime }$est que$\mathcal { F } ^ { \prime } \mathrm { s } ^ { \prime }$’ecrit comme le produit´ tensoriel externe des trois faisceaux -adiques suivants :

• le faisceau$\mathcal { F } _ { 1 }$sur$\widetilde { \mathcal { B } } _ { 1 }$associe à la repr´ esentation r´ egulière du groupe fini´ $( \operatorname { A u t } \widetilde { \mathcal { B } } _ { 1 } ) ^ { \mathrm { d i s c } }$

• le faisceau$\mathcal { F } _ { k }$sur$\widetilde { \mathcal B } _ { k }$associe à la repr´ esentation r´ egulière du groupe fini´ $( \operatorname { A u t } \widetilde { \mathcal { B } } _ { k } ) ^ { \mathrm { d i s c } }$

• un faisceau -adique lisse$\mathcal { F } ^ { \prime \prime }$sur un certain sous-champ localement ferme de´

$$
\overline {{\mathcal {C}}} _ {\emptyset} ^ {r _ {2}, N} \times_ {\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}, \text { Frob }} \dots \times_ {\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}, \text { Frob }} \overline {{\mathcal {C}}} _ {\emptyset} ^ {r _ {k - 1}, N}.
$$

Ceci permet d’appliquer la formule de Künneth comme dans le cas sans niveau. On calcule la cohomologie au-dessus de$( X - N ) \times ( X - N )$en deux temps, en calculant d’abord la cohomologie au-dessus de$( X - N ) \times$ $X \times X \times ( X - N )$(où les deux facteurs X du milieu sont le premier et le dernier deg´ en´ erateurs situ´ es en rangs´$r _ { 1 }$et$r - r _ { k } )$et on se ramène à montrer :

• Si$\widetilde { \mathcal { B } } _ { 1 }$a un zero [resp. n’en a pas], les espaces de cohomologie´$H _ { c } ^ { \nu }$de

$$
\mathrm{Cht} ^ {r _ {1}, d _ {1}, \overline {{p}} \leq p _ {1}} \times_ {\overline {{\mathcal {C}}} _ {\emptyset} ^ {r _ {1}, N}} \widetilde {\mathcal {B}} _ {1} ^ {\prime}
$$

au-dessus du point gen´ erique de´ X [resp. de$X \times X ]$sont r-negligeables´ comme representations de ´$W _ { F _ { d _ { 0 } } } ^ { \eta ^ { \prime } }$[resp.$W _ { F _ { d _ { 0 } } ^ { 2 } } ^ { \eta } ]$

• Si$\widetilde { \mathcal B } _ { k }$a un pôle [resp. n’en a pas], les espaces de cohomologie$H _ { c } ^ { \nu }$de

$$
\mathrm{Cht} ^ {r _ {k}, d _ {k}, \overline {{p}} \leq p _ {k}} \times_ {\overline {{\mathcal {C}}} _ {\emptyset} ^ {r _ {1}, N}} \widetilde {\mathcal {B}} _ {k} ^ {\prime}
$$

au-dessus du point gen´ erique de´ X [resp. de$X \times X ]$sont r-negligeables´ comme representations de´$W _ { F _ { d _ { 0 } } } ^ { \eta ^ { \prime \prime } }$[resp.$W _ { F _ { d _ { 0 } } ^ { 2 } } ^ { \eta } ]$

Traitons par exemple le cas de$\widetilde { \mathcal { B } } _ { 1 }$, celui de$\widetilde { \mathcal B } _ { k }$etant semblable.´

Si$\widetilde { \mathcal { B } } _ { 1 }$n’a pas de zero, Aut´$\widetilde { \mathcal { B } } _ { 1 }$est discret,$\mathrm { C h t } ^ { r _ { 1 } , d _ { 1 } , \overline { { p } } \leq p _ { 1 } } \times _ { \overline { { \mathfrak { C } } } _ { \varnothing } ^ { r _ { 1 } , N } } \widetilde { \mathcal { B } } _ { 1 } ^ { \prime }$s’identifie $\mathsf { a } \mathrm { C h t } _ { N } ^ { r _ { 1 } , d _ { 1 } , \overline { { p } } \leq p _ { 1 } } \otimes _ { \mathbb { F } _ { q } } \mathbb { F } _ { q _ { 0 } }$et la conclusion resulte de la proposition VI.15(iii)´ supposee´$\mathrm { d e j a }$connue en rang$r _ { 1 } < r$

Si au contraire$\mathcal { \widetilde { B } } _ { 1 }$a un zero 0 (qui est un point de´ N defini sur´$\mathbb { F } _ { q _ { 0 } } )$, introduisons le produit fibre´

$$
\mathfrak {X} _ {1} ^ {d _ {1}} = \overline {{\operatorname{Cht} ^ {r _ {1} , d _ {1} , \overline {{p}} \leq p _ {1}}}} \times_ {X \times X} (X - N) \times 0.
$$

$\mathbf { C } '$est un champ serein et propre sur$X - N$et d’après la proposition III.5, le morphisme produit

$$
\left(p _ {\mathfrak {X} _ {1} ^ {d _ {1}}}, \operatorname{Res} _ {1}\right): \mathfrak {X} _ {1} ^ {d _ {1}} \longrightarrow (X - N) \times \left(\overline {{\mathcal {C}}} ^ {r _ {1}, N} \times_ {\mathbb {A} ^ {N} / \mathbb {G} _ {m} ^ {N}} 0\right)
$$

est lisse. D’après le theorème´$\phantom { - } \mathsf { A } . 9 ( \mathrm { i } )$, pour tout complexe de faisceaux$\ell -$ adiques$\mathcal { F } _ { 1 }$sur le champ$\overline { { \mathcal { C } } } ^ { r _ { 1 } , N } \times _ { \mathbb { A } ^ { N } / \mathbb { G } _ { m } ^ { N } } 0$, tous les faisceaux de cohomologie -adique$R ^ { \nu } ( p _ { \mathfrak { X } _ { 1 } ^ { d _ { 1 } } } )$Res<sup>∗</sup>$\mathcal { F } _ { 1 }$sont lisses sur$X - N$

Il suffit de montrer :

Lemme VI.18. – Pour tout rang$r _ { 1 } ~ < ~ r _ { \mathrm { { ; } } }$, tout polygone de troncature$p _ { 1 }$ (assez convexe en fonction de X et N), tout degre´$d _ { 1 }$et tout complexe de faisceaux -adiques$\mathcal { F } _ { 1 }$sur$\overline { { \mathcal { C } } } ^ { r _ { 1 } , N } \times _ { \mathrm { A } ^ { N } / \mathbb { G } _ { m } ^ { N } }$0, lesfaisceaux de cohomologie

$$
R ^ {\nu} (p _ {\mathfrak {X} _ {1} ^ {d _ {1}}})! \operatorname{Res} _ {1} ^ {*} \mathcal {F} _ {1}
$$

sont r-negligeables comme repr´ esentations de´$W _ { F _ { d _ { 0 } } } ^ { \eta ^ { \prime } }$

Demonstration´$\therefore \mathrm { O n }$raisonne par recurrence sur le rang´$r _ { 1 }$et sur la dimension du support de$\mathcal { F } _ { 1 }$. Supposons donc le resultat d´ ejà connu en les´ rangs$< ~ r _ { 1 }$et, en rang$r _ { 1 }$, pour les complexes$\mathcal { F } _ { 1 }$dont le support est de codimension$> c$

Il s’agit de prouver le lemme pour un faisceau -adique$\mathcal { F } _ { 1 }$lisse sur un sous-champ localement ferme´ C de codimension$c$de$\overline { { \mathcal { C } } } ^ { r _ { 1 } , N } \times _ { \mathbb { A } ^ { N } / { \mathbb G } _ { m } ^ { N } } 0$ On peut supposer que$\mathcal { C }$est contenu dans une seule strate associee à une´ partition$\underline { { r } } _ { 1 }$de l’entier$r _ { 1 }$.

Si$\underline { { r } } _ { 1 }$est non triviale, on raisonne comme nous avons fait pour nous ramener à l’enonc´ e du lemme VI.18 et on conclut d’après d’hypothèse de´ recurrence.´

Sinon, on peut supposer que$\mathcal { F } _ { 1 }$est supporte par un unique point lo-´ calement ferme´$\widetilde { \mathcal { B } } _ { 1 }$de$\overline { { \mathcal { C } } } _ { \varnothing } ^ { r _ { 1 } , N } \times _ { \mathbb { A } ^ { N } / \mathbb { G } _ { m } ^ { N } }$0 et même que${ \mathrm { c } } ^ { \prime }$est le faisceau - adique (pur de poids 0) associe à la repr´ esentation r´ egulière du groupe fini´ $( \mathrm { A u t } \widetilde { \mathcal { B } } _ { 1 } ) ^ { \mathrm { d i s c } } = \mathrm { \hat { A } u t } \widetilde { \mathcal { B } } _ { 1 } / ( \mathrm { A u t } \widetilde { \mathcal { B } } _ { 1 } ) ^ { \mathrm { c o n t } }$

  Le resultat´ etant d´ ejà connu quand la codimension du support est´$> c .$, il est equivalent de montrer que si´$\bar { \mathcal { F } } _ { 1 } ^ { \prime }$designe le faisceau pervers qui est le pro-´ longement intermediaire de´$\mathcal { F } _ { 1 }$sur l’adherence de´$\widetilde { \mathcal { B } } _ { 1 }$dans$\overline { { \mathcal { C } } } _ { \varnothing } ^ { r _ { 1 } , N } \times _ { \operatorname { \mathbb { A } } ^ { N } / \mathbb { G } _ { m } ^ { N } } 0$ les$R ^ { \nu } ( p _ { \mathfrak { X } _ { 1 } ^ { d _ { 1 } } } )$Res<sup>∗</sup>$\mathcal { F } _ { 1 } ^ { \prime }$sont r-negligeables. D’après le th´ eorème A.9(ii)´ ceux-ci sont purs de poids ν et il en est de même des faisceaux de cohomologie

$$
R ^ {\nu} (p _ {\mathfrak {X} _ {1}}) _ {!} \operatorname{Res} _ {1} ^ {*} \mathcal {F} _ {1} ^ {\prime} = \bigoplus_ {1 \leq d _ {1} \leq r _ {1} | \deg (a) |} R ^ {\nu} (p _ {\mathfrak {X} _ {1} ^ {d _ {1}}}) _ {!} \operatorname{Res} _ {1} ^ {*} \mathcal {F} _ {1} ^ {\prime}
$$

à coefficients dans$\mathcal { F } _ { 1 } ^ { \prime }$de$\mathfrak { X } _ { 1 } = \coprod _ { d _ { 1 } \in \mathbb { Z } } \mathfrak { X } _ { 1 } ^ { d _ { 1 } } / a ^ { \mathbb { Z } } \cong \coprod _ { 1 \leq d _ { 1 } \leq r _ { 1 } | \mathrm { d e g } ( a ) | } \mathfrak { X } _ { 1 } ^ { d _ { 1 } }$. Dans la somme alternee´

$$
H _ {c} ^ {*} \left(\mathfrak {X} _ {1}, \mathcal {F} _ {1} ^ {\prime}\right) = \sum_ {\nu} (- 1) ^ {\nu} \left[ R ^ {\nu} \left(p _ {\mathfrak {X} _ {1}}\right)! \operatorname{Res} _ {1} ^ {*} \mathcal {F} _ {1} ^ {\prime} \right] ^ {s s},
$$

il ne peut y avoir de simplification et il suffit de montrer que$H _ { c } ^ { * } ( \mathfrak { X } _ { 1 } , \mathcal { F } _ { 1 } ^ { \prime } )$ est r-negligeable en tant que repr´ esentation virtuelle de´$W _ { F _ { d _ { 0 } } } ^ { \eta ^ { \prime } }$

Toujours d’après l’hypothèse de recurrence,´${ \mathrm { c } } '$est equivalent à prouver´ que

$$
H _ {c} ^ {*} \left(\mathfrak {X} _ {1}, \mathcal {F} _ {1}\right) = \sum_ {\nu} (- 1) ^ {\nu} \left[ R ^ {\nu} \left(p _ {\mathfrak {X} _ {1}}\right)! \operatorname{Res} ^ {*} \mathcal {F} _ {1} \right] ^ {s s}
$$

est r-negligeable. Or, avec les notations qui suivent la propositi´ on II.4, la cohomologie sur X − N à coefficients dans$\mathcal { F } _ { 1 }$de$\mathfrak { X } _ { 1 }$s’identifie à la cohomologie sur$X - N$à coefficients dans$\mathbb { Q } _ { \ell }$de

$$
\operatorname{Cht} _ {N, \widetilde {\mathcal {B}} _ {1}} ^ {r _ {1}, \overline {{p}} \leq p _ {1}} / a ^ {\mathbb {Z}}.
$$

En effet, si$\mathcal { \widetilde { B } } _ { 1 } ^ { \prime }$est le revêtement fini etale galoisien de groupe´ (Aut$\widetilde { \mathcal { B } } _ { 1 } )$disc de$\widetilde { \mathcal { B } } _ { 1 }$que definit Spec´$\mathbb { F } _ { q _ { 0 } } / ( \mathrm { A u t } \ \widetilde { \mathcal { B } } _ { 1 } ) ^ { \mathrm { c o n t } }$, on a pour tout degre´$d _ { 1 }$

$$
\mathfrak {X} _ {1} ^ {d _ {1}} \times_ {\overline {{\mathcal {C}}} ^ {r _ {1}, N}} \widetilde {\mathcal {B}} _ {1} ^ {\prime} = \operatorname{Cht} _ {N, \widetilde {\mathcal {B}} _ {1}} ^ {r _ {1}, d _ {1}, \overline {{p}} \leq p _ {1}}.
$$

D’après la formule des traces de Grothendieck-Lefschetz et le theorème´ II.15, il existe des constantes$c _ { \iota } .$, des entiers$m _ { \iota } \ \geq \ 0$, des scalaires$\lambda _ { \iota }$et des representations automorphes cuspidales´$\pi ^ { \iota }$de rangs$r _ { \iota } \leq r _ { 1 } < r$non ramifiees sur´$X - N$telles qu’on ait la formule suivante :

Pour toute place$\infty \in | X - N |$(en dehors d’un nombre fini) et pour tout multiple assez grand$s = \deg ( \infty ) s ^ { \prime }$de deg(∞) et$d _ { 0 }$(choisi suffisamment

divisible),

$$
\begin{array}{c} \operatorname{Tr} \big (\operatorname{Frob} _ {\infty} ^ {- s ^ {\prime}}, H _ {c} ^ {*} \big (\operatorname{Cht} _ {N, \widetilde {\mathcal {B}} _ {1}} ^ {r _ {1}, \overline {{p}} \leq p _ {1}} / a ^ {\mathbb {Z}} \big) \big) \\ = \sum_ {\iota} c _ {\iota} s ^ {m _ {\iota}} \lambda_ {\iota} ^ {s} \big (z _ {1} \big (\pi_ {\infty} ^ {\iota} \big) ^ {- s ^ {\prime}} + \dots + z _ {\pi_ {\iota}} \big (\pi_ {\infty} ^ {\iota} \big) ^ {- s ^ {\prime}} \big). \end{array}
$$

Dans cette expression, les termes tels que$m _ { \iota } \ > \ 0$doivent se simplifier mutuellement et on peut supposer que tous les$m _ { \iota }$valent 0.

D’après l’hypothèse de recurrence, chaque repr´ esentation automorphe´ cuspidale$\pi ^ { \iota }$tordue par$\lambda ^ { \iota }$correspond au sens de Langlands à une representation´ -adique$\sigma _ { \iota }$de$W _ { F } ^ { \eta ^ { \prime } }$irreductible de rang´$r _ { \iota } \leq r _ { 1 } < r$. Les deux representations virtuelles de´$W _ { F } ^ { \eta ^ { \prime } }$

$$
H _ {c} ^ {*} \left(\operatorname{Cht} _ {N, \widetilde {\mathcal {B}} _ {1}} ^ {r _ {1}, \overline {{p}} \leq p _ {1}} / a ^ {\mathbb {Z}}\right) \quad \text { et } \quad \sum_ {\iota} c _ {\iota} \sigma_ {\iota}
$$

coïncident quand on les restreint au sous-groupe$W _ { F _ { d _ { 0 } } } ^ { \eta ^ { \prime } }$. Cela conclut le raisonnement.!"

Remarque : Pour demontrer que la cohomologie à supports compacts des´ strates de bord ouvertes ou fermees des´$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { ' } } / a ^ { \mathbb Z }$est r-negligeable, on´ peut proceder comme dans le cas sans niveau et se ramener à dire que,´ d’après la proposition VI.15(iii) dejà connue en rang´ r et la formule de Künneth, la cohomologie à supports compacts au-dessus de$( X - N ) \times$ (X − N) des

$$
\operatorname{Cht} _ {N} ^ {r _ {1}, d _ {1}, \overline {{p}} \leq p _ {1}} \times_ {X - N} \operatorname{Cht} _ {N} ^ {r _ {2}, d _ {2}, \overline {{p}} \leq p _ {2}} \times_ {X - N, \text { Frob }} \dots \times_ {X - N, \text { Frob }} \operatorname{Cht} _ {N} ^ {r _ {k}, d _ {k}, \overline {{p}} \leq p _ {k}}
$$

est r-negligeable.´

Cependant, on a aussi besoin d’arguments de purete et pour cela de´ verifier que la diff´ erence entre les´$H _ { c } ^ { \nu } ( { \mathbf { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$et les$I H _ { c } ^ { \nu } ( { \bf C h t } _ { N } ^ { r , \overline { { { p } } } \leq p } / a ^ { \mathbb { Z } } )$ est r-negligeable. C’est pourquoi la proposition VI.17 dans toute´ sa gen´ era-´ lite est n´ ecessaire à notre d´ emonstration de la correspondance de Langlands´ et il en est de même du contenu du chapitre II qui intervient dans la preuve de cette proposition via le lemme VI.18.

## d) Separation de la cohomologie essentielle´

On rappelle qu’on a fixe un entier´$r \geq 2$et un niveau$N = \operatorname { S p e c } { \mathcal { O } } _ { N } \hookrightarrow X$ et qu’on a note´

$$
\{\pi \} _ {N} ^ {r} = \left\{\pi \in \mathcal {A} ^ {r} (F) \mid \chi_ {\pi} (a) = 1 \wedge \pi \cdot \mathbb {1} _ {N} \neq 0 \right\}.
$$

Notre but est d’identifier la partie essentielle de$H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$. On commence par :

Lemme VI.19. – Pour tout polygone de troncature$p : [ 0 , r ] \to \mathbb { R } _ { + }$(assez convexe enfonction de X et N), il existe une combinaison lineaire formelle´ $H _ { N , \mathrm { e s s } } ^ { * }$à coefficients dans Q defaisceaux -adiques lisses irreductibles dans´ ${ \mathcal { G } } _ { \ell } ( ( X - N ) \times ( X - N ) )$eventuellement tordus par des caractères de´$\mathbb { Z } ,$ telle que :

## (i) La difference formelle´

$$
H _ {N, \text { ess }} ^ {*} - \frac {1}{r !} \sum_ {n = 1} ^ {r!} \left(\operatorname{Frob} _ {X} ^ {n} \times \operatorname{Id} _ {X}\right) ^ {*} H _ {c} ^ {*} \left(\operatorname{Cht} _ {N} ^ {r, \overline {{p}} \leq p} / a ^ {\mathbb {Z}}\right),
$$

vue comme representation virtuelle de´$W _ { F ^ { 2 } } ^ { \eta }$, est r-negligeable complète.´ (ii) Pour tout point ferme x de´$X \times X$au-dessus de deux points fermes´ distincts ∞,$0 \in | X - N | ,$, et notant Frob l’el´ ement de Frobenius en x´ dans$W ( ( X - N ) \times ( X - N ) , \eta )$, on apour tout multiple$s = \deg ( \infty ) s ^ { \prime } =$ deg(0)u	 de deg(x) = ppcm(deg(0), deg(∞))

$$
\begin{array}{c} \operatorname{Tr} _ {H _ {N, \text {ess}} ^ {*}} \big (\operatorname{Frob} _ {x} ^ {- s / \deg (x)} \big) = q ^ {(r - 1) s} \sum_ {\pi \in \{\pi \} _ {N} ^ {r}} \operatorname{Tr} _ {\pi} (\mathbb {1} _ {N}) \\ \big (z _ {1} (\pi_ {\infty}) ^ {- s ^ {\prime}} + \dots + z _ {r} (\pi_ {\infty}) ^ {- s ^ {\prime}} \big) \big (z _ {1} (\pi_ {0}) ^ {u ^ {\prime}} + \dots + z _ {r} (\pi_ {0}) ^ {u ^ {\prime}} \big). \end{array}
$$

Remarque : D’après la proposition VI.15(i) dejà d´ emontr´ ee en rang´ r, la difference´$H _ { c } ^ { * } ( \overline { { \mathrm { C h t } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } } } ) - H _ { c } ^ { * } ( \mathrm { C h t } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } ) \left( \mathrm { s i } N { = } \emptyset \right) , I H _ { c } ^ { * } ( \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$ $- \mathbf { \nabla } H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$(si$N \neq \emptyset )$ou eventuellement´$H _ { c } ^ { * } ( { \mathrm { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } ) \ -$ $H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$est r-negligeable.´

Dans l’enonc´ e du lemme, on peut donc remplacer dans (i) le terme´ $H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$par$H _ { c } ^ { * } ( \overline { { \mathbf { C h t } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } } ) \ ( \mathrm { s i } \ N = \emptyset ) , \ I H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$ou eventuellement´$H _ { c } ^ { * } ( \mathbf { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$

Demonstration :´ D’après la formule des points fixes de Grothendieck-Lefschetz pour les puissances de Frob et le theorème I.13 appliqu´ e à´$f = \mathbb { 1 } _ { N }$ et$t = 0$, on a pour tout point$x \mapsto ( \infty , 0 )$et tout multiple$s = \deg ( \infty ) s ^ { \prime } =$ $\mathrm { d e g } ( 0 ) u ^ { \prime }$comme dans l’enonc´ e´

$$
\begin{array}{c} \operatorname{Tr} _ {\frac {1}{r !} \sum_ {n = 1} ^ {r!} \left(\operatorname{Frob} _ {X} ^ {n} \times \operatorname{Id} _ {X}\right) ^ {*} H _ {c} ^ {*} \left(\operatorname{Cht} _ {N} ^ {r, \overline {{p}} \leq p / a ^ {\mathbb {Z}}}\right)} \left(\operatorname{Frob} _ {x} ^ {- s / \deg (x)}\right) \\ = q ^ {(r - 1) s} \sum_ {\pi \in \{\pi \} _ {N} ^ {r}} \operatorname{Tr} _ {\pi} (\mathbb {1} _ {N}) \big (z _ {1} (\pi_ {\infty}) ^ {- s ^ {\prime}} + \dots + z _ {r} (\pi_ {\infty}) ^ {- s ^ {\prime}} \big) \big (z _ {1} (\pi_ {0}) ^ {u ^ {\prime}} + \dots + z _ {r} (\pi_ {0}) ^ {u ^ {\prime}} \big) \\ + \sum_ {\iota} c _ {\iota} s ^ {m _ {\iota}} \lambda_ {\iota} ^ {s} \big (z _ {1} \big (\pi_ {\infty} ^ {\prime \iota} \big) ^ {- s ^ {\prime}} + \dots + z _ {r _ {\iota} ^ {\prime}} \big (\pi_ {\infty} ^ {\prime \iota} \big) ^ {- s ^ {\prime}} \big) \big (z _ {1} \big (\pi_ {0} ^ {\iota} \big) ^ {u ^ {\prime}} + \dots + z _ {r _ {\iota}} \big (\pi_ {0} ^ {\iota} \big) ^ {u ^ {\prime}} \big) \end{array}
$$

où les$c _ { \iota }$sont des constantes, les$m _ { \iota }$des entiers$\geq 0$, les$\lambda _ { \iota }$des scalaires non nuls et les$\pi ^ { \iota }$et$\pi ^ { \prime } { \boldsymbol { \imath } }$des representations automorphes cuspidales en rangs´$r _ { \iota }$ et$r _ { \mathrm { \Delta } _ { l } } ^ { \prime } < r$

Les termes indexes par les´ ι tels que$m _ { \iota } \ > \ 0$doivent se simplifier mutuellement et on peut supposer que tous les$m _ { \iota }$valent 0. De même, on peut supposer que tous les$c _ { \iota }$sont dans$\mathbb { Q }$

D’après l’hypothèse de recurrence, les´$\pi ^ { \prime } { \boldsymbol { \iota } }$et$\pi ^ { \iota }$correspondent au sens de Langlands à des faisceaux -adiques irreductibles de rangs´$r _ { \iota } ^ { \prime }$et$r _ { \iota }$dans ${ \mathcal { G } } _ { \ell } ( X - N )$et les termes

$$
\lambda_ {\iota} ^ {s} \left(z _ {1} \left(\pi_ {\infty} ^ {\prime \iota}\right) ^ {- s ^ {\prime}} + \dots + z _ {r _ {\iota} ^ {\prime}} \left(\pi_ {\infty} ^ {\prime \iota}\right) ^ {- s ^ {\prime}}\right) \left(z _ {1} \left(\pi_ {0} ^ {\iota}\right) ^ {u ^ {\prime}} + \dots + z _ {r _ {\iota}} \left(\pi_ {0} ^ {\iota}\right) ^ {u ^ {\prime}}\right)
$$

se recrivent sous la forme´

$$
\operatorname{Tr} _ {\sigma_ {l}} \left(\operatorname{Frob} _ {x} ^ {- s / \deg (x)}\right)
$$

où les$\sigma _ { \iota }$sont des faisceaux -adiques lisses dans${ \mathcal { G } } _ { \ell } ( ( X - N ) \times ( X - N ) )$ eventuellement tordus par des caractères de´ Z et qui sont r-negligeables´ complets.

Alors la difference formelle´

$$
H _ {N, \text { ess }} ^ {*} = \frac {1}{r !} \sum_ {n = 1} ^ {r!} \left(\operatorname{Frob} _ {X} ^ {n} \times \operatorname{Id} _ {X}\right) ^ {*} H _ {c} ^ {*} \left(\operatorname{Cht} _ {N} ^ {r, \overline {{p}} \leq p} / a ^ {\mathbb {Z}}\right) - \sum_ {\iota} c _ {\iota} \cdot \sigma_ {\iota}
$$

repond à la question pos´ ee.´

On remarque que d’après la partie (ii) du lemme,$H _ { N , \mathrm { e s s } } ^ { * }$ne depend pas´ du polygone de troncature p. Montrons que${ \mathrm { c } } ^ { \prime }$est la partie essentielle des faisceaux -adiques virtuels$\begin{array} { r } { \frac { 1 } { r ! } \sum _ { n = 1 } ^ { r ! } ( \mathrm { F r o b } _ { X } ^ { n } \times \mathrm { I d } _ { X } ) ^ { * } H _ { c } ^ { * } ( \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z } ) } \end{array}$

## Proposition VI.20. –

(i) Aucune des composantes irreductibles de´$H _ { N , \mathrm { e s s } } ^ { * }$n’est r-negligeable.´ Toutes apparaissent avec des multiplicites positives et sont des´ faisceaux -adiques lisses dans$\mathcal { G } _ { \ell } ( ( X - N ) \times ( X - N ) )$purs de poids $2 r - 2 .$

(ii) Pour p un polygone (assez convexe en fonction de X et N), les $H _ { c } ^ { \nu } ( { \mathrm { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } ) , \ \nu \not = 2 r - 2$, sont r-negligeables de même que la´ difference formelle´

$$
\frac {1}{r !} \sum_ {n = 1} ^ {r!} \left(\operatorname{Frob} _ {X} ^ {n} \times \operatorname{Id} _ {X}\right) ^ {*} H _ {c} ^ {2 r - 2} \left(\operatorname{Cht} _ {N} ^ {r, \overline {{p}} \leq p} / a ^ {\mathbb {Z}}\right) ^ {s s} - H _ {N, \text { ess }} ^ {*}.
$$

Remarque : D’après le lemme VI.19(ii), il est equivalent de dire que´$H _ { N } ^ { * }$ess est pur de poids$2 r - 2$ou que les representations´$\pi \in \{ \pi \} _ { N } ^ { r }$verifient la´ conjecture de Ramanujan-Petersson en toutes les places en dehors de N.

Demonstration de la proposition :´

(ii) Pour tout ν, notons$H ^ { \nu } = H _ { c } ^ { \nu } ( { \mathrm { C h t } } ^ { r , \overline { { { p } } } \leq p } / a ^ { \mathbb { Z } } ) ^ { s s }$si$N \mathop { = } \mathop { \emptyset }$et$H ^ { \nu } =$ $I H _ { c } ^ { \nu } ( { \mathrm { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb Z } ) ^ { s s }$(ou eventuellement´$H ^ { \nu } = H _ { c } ^ { \nu } ( \mathrm { C h t } _ { N } ^ { r , \overline { { { p } } } \leq p } / a ^ { \mathbb { Z } } ) ^ { s s } )$si $N \neq \emptyset .$

Dans tous les cas, les$H ^ { \nu }$sont purs de poids ν si bien qu’il ne peut y avoir de simplification dans la somme

$$
\sum_ {n = 1} ^ {r!} \sum_ {\nu = 0} ^ {2 (2 r - 2)} (- 1) ^ {\nu} \left(\operatorname{Frob} _ {X} ^ {n} \times \operatorname{Id} _ {X}\right) ^ {*} H ^ {\nu}.
$$

Donc (ii) est implique par (i), le lemme VI.19 et la proposition VI.15(i)´ dejà d ´ emontr ´ ee en rang ´ r.

(i) Notons$H = H _ { N , \mathrm { e s s } } ^ { * } ( r - 1 )$

On voit sur la formule du lemme VI.19(ii) que$H _ { N , \mathrm { e s s } } ^ { * }$ou H est invariante par l’action de$\mathrm { F r o b } _ { X } ^ { n } \times \mathrm { I d } _ { X }$. Il en est de même de sa partie r-negligeable´ qui donc est complète.

D’après l’hypothèse de recurrence, toutes les repr´ esentations´ -adiques r-negligeables et irr´ eductibles sont pures. Donc toutes les composantes de´ H sont pures d’un certain poids. Il resulte de la proposition B.2 de Jacquet et´ Shalika que l’ensemble des poids de H est contenu dans l’intervalle ]−2, 2[et d’autre part il est symetrique par rapport à 0.´

Considerons´$\sigma ^ { \prime } , \ : \bar { \sigma } ^ { \prime \prime }$deux faisceaux dans${ \mathcal { G } } _ { \ell } ( X - N )$irreductibles de´ rangs$r ^ { \prime } , r ^ { \prime \prime } < r$et purs de poids 0. D’après l’hypothèse de recurrence, il´ leur correspond au sens de Langlands deux representations automorphes´ cuspidales unitaires$\pi ^ { \prime } , \pi ^ { \prime \prime }$en rangs$\boldsymbol { r } ^ { \prime } , \boldsymbol { r } ^ { \prime \prime }$qui sont non ramifiees en dehors´ de N.

Le theorème B.10 entraîne que pour toute´$\pi \in \{ \pi \} _ { N } ^ { r }$les series d´ eriv´ ees´ logarithmiques des fonctions L

$$
\begin{array}{l}\frac{\mathrm{L}^{\prime}_{X - N}(\pi\times\check{\pi}^{\prime},Z)}{\mathrm{L}_{X - N}(\pi\times\check{\pi}^{\prime},Z)} = \sum_{\infty \in |X - N|}\deg (\infty)\sum_{k\geq 1}\big(z_{1}(\pi_{\infty})^{-k} + \dots +z_{r}(\pi_{\infty})^{-k}\big)\\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \left(z_{1}\big(\pi^{\prime}_{\infty}\big)^{k} + \dots +z_{r^{\prime}}\big(\pi^{\prime}_{\infty}\big)^{k}\right)Z^{k\deg (\infty) - 1}\\ = \sum_{s\geq 1}Z^{s - 1}\sum_{\substack{\infty \in |X - N|\\ \frac{s}{\deg(\infty)} = s^{\prime}\in \mathbb{N}}}\deg (\infty)\big(z_{1}\big(\pi_{\infty}\big)^{-s^{\prime}} + \dots +z_{r}\big(\pi_{\infty}\big)^{-s^{\prime}}\big)\\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \left(z_{1}\big(\pi^{\prime}_{\infty}\big)^{s^{\prime}} + \dots +z_{r}\big(\pi^{\prime}_{\infty}\big)^{s^{\prime}}\right) \end{array}
$$

et

$$
\begin{array}{l}\frac{\mathrm{L}^{\prime}_{X - N}(\check{\pi}\times\check{\pi}^{\prime \prime},Z)}{\mathrm{L}_{X - N}(\check{\pi}\times\check{\pi}^{\prime \prime},Z)} = \sum_{0\in |X - N|}\deg (0)\sum_{k\geq 1}\big(z_{1}(\pi_{0})^{k} + \dots +z_{r}(\pi_{0})^{k}\big)\\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \left(z_{1}\big(\pi_{0}^{\prime \prime}\big)^{k} + \dots +z_{r}\big(\pi_{0}^{\prime \prime}\big)^{k}\right)Z^{k\deg (0) - 1}\\ = \sum_{s\geq 1}Z^{s - 1}\sum_{\substack{0\in |X - N|\\ \frac{s}{\deg(0)} = u^{\prime}\in \mathbb{N}}}\deg (0)\big(z_{1}\big(\pi_{0}\big)^{u^{\prime}} + \dots +z_{r}\big(\pi_{0}\big)^{u^{\prime}}\big)\\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \left(z_{1}\big(\pi_{0}^{\prime \prime}\big)^{u^{\prime}} + \dots +z_{r^{\prime \prime}}\big(\pi_{0}^{\prime \prime}\big)^{u^{\prime}}\right) \end{array}
$$

sont absolument convergentes dans une zone$| Z | < q ^ { - 1 + \varepsilon }$(pour$\varepsilon > 0$un reel assez petit).´

Par consequent, la s´ erie “produit”´

$$
= \sum_{s\geq 1}Z^{s - 1}\sum_{\substack{\infty ,0\in |X - N|\\ \frac{s}{\deg(\infty)} = s^{\prime}\in \mathbb{N},\frac{s}{\deg(0)} = u^{\prime}\in \mathbb{N}}}\deg (\infty)\deg (0)\big(z_{1}(\pi_{\infty})^{-s^{\prime}} + \dots +z_{r}(\pi_{\infty})^{-s^{\prime}}\big)\\ \big(z_{1}(\pi_{0})^{u^{\prime}} + \dots +z_{r}(\pi_{0})^{u^{\prime}}\big)\big(z_{1}\big(\pi_{\infty}^{\prime}\big)^{s^{\prime}} + \dots +z_{r^{\prime}}\big(\pi_{\infty}^{\prime}\big)^{s^{\prime}}\big)\big(z_{1}\big(\pi_{0}^{\prime \prime}\big)^{u^{\prime}} + \dots +z_{r^{\prime \prime}}\big(\pi_{0}^{\prime \prime}\big)^{u^{\prime}}\big)
$$

est absolument convergente dans la zone$| Z | < q ^ { - 2 + 2 \varepsilon }$

D’autre part et bien que les composantes de H apparaissent a priori avec des coefficients dans$\mathbb { Q } .$, on peut definir la d´ eriv´ ee logarithmique´

$$
\frac {\mathrm{L} _ {(X - N) \times (X - N)} ^ {\prime} \big (H \otimes \big (q _ {\infty} ^ {*} \check {\sigma} ^ {\prime} \otimes q _ {0} ^ {*} \check {\sigma} ^ {\prime \prime} \big) , Z \big)}{\mathrm{L} _ {(X - N) \times (X - N)} \big (H \otimes \big (q _ {\infty} ^ {*} \check {\sigma} ^ {\prime} \otimes q _ {0} ^ {*} \check {\sigma} ^ {\prime \prime} \big) , Z \big)}
$$

comme serie formelle en´$Z .$Comme$\sigma ^ { \prime }$et$\sigma ^ { \prime \prime }$correspondent au sens de Langlands$\grave { \textrm { a } } \pi ^ { \prime }$et$\pi ^ { \prime \prime }$et d’après le lemme VI.19(ii), cette serie ne peut´ differer de la somme sur les´$\pi \in \{ \pi \} _ { N } ^ { r }$des series “produits” ci-dessus que´ par les termes indexes par les´ ∞,$0 \in \dot { | } X - N |$tels que$\infty = 0 . { \mathrm { S i } } \varepsilon > 0$a et´ e choisi assez petit pour que´$2 ( 1 - 2 \varepsilon )$majore tous les poids de H, cette difference est born´ ee à une constante multiplicative près par´

$$
\sum_{s\geq 1}|Z|^{s - 1}\sum_{\substack{\infty \in |X - N|\\ \deg (\infty)|s}}\deg (\infty)^{2}q^{(1 - 2\varepsilon)s}
$$

qui converge pour$| Z | < q ^ { - 2 + 2 \varepsilon }$

Recapitulant, on a prouv´ e que la s´ erie´

$$
\frac {\mathrm{L} _ {(X - N) \times (X - N)} ^ {\prime} \big (H \otimes \big (q _ {\infty} ^ {*} \check {\sigma} ^ {\prime} \otimes q _ {0} ^ {*} \check {\sigma} ^ {\prime \prime} \big) , Z \big)}{\mathrm{L} _ {(X - N) \times (X - N)} \big (H \otimes \big (q _ {\infty} ^ {*} \check {\sigma} ^ {\prime} \otimes q _ {0} ^ {*} \check {\sigma} ^ {\prime \prime} \big) , Z \big)}
$$

converge absolument pour$| Z | < q ^ { - 2 + 2 \varepsilon }$

Comme on a pu prendre$\sigma ^ { \prime }$et$\sigma ^ { \prime \prime }$arbitraires (et que H est invariante par$( \mathrm { F r o b } _ { X } \times \mathrm { I d } _ { X } ) ^ { * } )$, on conclut d’après le corollaire VI.3 que parmi les composantes de poids maximal (necessairement compris dans´ [0, 2[) de H, aucune n’est r-negligeable. Modulo la torsion par´$r - 1$, elles proviennent donc toutes des$( \mathrm { F r o b } _ { X } ^ { n } \times \mathrm { I d } _ { X } ) ^ { * } H ^ { 2 r - 1 }$ou des$( \mathrm { F r o b } _ { X } ^ { n } \times \mathrm { I d } _ { X } ) ^ { * } H ^ { 2 r - 2 }$; le premier cas est impossible car il ferait apparaître des coefficients −1. Donc le poids maximal de H est 0, par symetrie´ H est pur de poids 0, il n’a pas de composante r-negligeable et provient entièrement des´ (Frob$\mathbf \Delta _ { X } ^ { n } \times \mathbf { I d } _ { X } ) ^ { * } \mathbf { \tilde { \mathit { H } } } ^ { 2 r - 2 }$ ou, ce qui est equivalent, des´$( \mathrm { F r o b } _ { X } ^ { n } \times \mathrm { I d } _ { X } ) ^ { * } H ^ { 2 r - 2 } ( \mathrm { C h t } _ { N } ^ { r , \overline { { { p } } } \leq p } / a ^ { \mathbb Z } ) ^ { s s }$!"

## e) Effet r-negligeable des troncatures´

Si N est un niveau non vide, on a note´$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } }$l’ouvert lisse de$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p }$ defini en demandant que les d´ eg´ en´ erateurs´ evitent´ N. Si$N = \emptyset$, on notera simplement$\overline { { { \mathrm { C h t } _ { N } ^ { r , \overline { { { p } } } \leq p ^ { \prime } } } } } = \overline { { { \mathrm { C h t } ^ { r , \overline { { { p } } } \leq p } } } }$

D’après la proposition VI.20(ii) et la proposition VI.15(ii) dejà d´ emontr´ ee´ en rang r, nous savons qu’en tout degre´$\nu \neq 2 r - 2$, tous les$H _ { c } ^ { \nu } ( \overline { { \mathbf { C } \mathbf { h } \mathbf { t } _ { N } ^ { r , \overline { { p } } \leq p } } } / a ^ { \mathbb { Z } } )$ et$H _ { c } ^ { \nu } ( { \mathbf { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } } )$sont r-negligeables. En le degr´ e m´ ediant´$\nu = 2 r - 2$où se concentre la cohomologie essentielle, nous pouvons preciser :´

Corollaire VI.21. – (i) Pour tout polygone de troncature p (assez convexe enfonction de X et N), le noyau et le conoyau de l’homomorphisme

$$
H _ {c} ^ {2 r - 2} \left(\operatorname{Cht} _ {N} ^ {r, \overline {{p}} \leq p} / a ^ {\mathbb {Z}}\right)\rightarrow H _ {c} ^ {2 r - 2} \left(\overline {{\operatorname{Cht} _ {N} ^ {r , \overline {{p}} \leq p}}} / a ^ {\mathbb {Z}}\right)
$$

induits par l’immersion ouverte

$$
\mathrm{Cht} _ {N} ^ {r, \overline {{p}} \leq p} / a ^ {\mathbb {Z}} \hookrightarrow \overline {{\mathrm{Cht} _ {N} ^ {r , \overline {{p}} \leq p}}} ^ {\prime} / a ^ {\mathbb {Z}}
$$

sont r-negligeables.´

(ii) Pour tous polygones de troncature$p \leq q$(assez convexes en fonction de X et N), le noyau et le conoyau de l’homomorphisme

$$
H _ {c} ^ {2 r - 2} \left(\operatorname{Cht} _ {N} ^ {r, \overline {{p}} \leq p} / a ^ {\mathbb {Z}}\right)\rightarrow H _ {c} ^ {2 r - 2} \left(\operatorname{Cht} _ {N} ^ {r, \overline {{p}} \leq q} / a ^ {\mathbb {Z}}\right)
$$

induits par l’inclusion

$$
\mathrm{Cht} _ {N} ^ {r, \overline {{p}} \leq p} / a ^ {\mathbb {Z}} \hookrightarrow \mathrm{Cht} _ {N} ^ {r, \overline {{p}} \leq q} / a ^ {\mathbb {Z}}
$$

sont r-negligeables.´

Demonstration :´ (i) resulte de ce que ce noyau et ce conoyau se plongent´ dans la cohomologie du bord$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } } / a ^ { \mathbb { Z } } - \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$laquelle est rnegligeable.´

(ii) D’après le theorème V.14(i), la normalisation du graphe de l’in-´ clusion de$\mathrm { \bar { C h t } } _ { N } ^ { r , \overline { { p } } \leq p } / a ^ { \mathbb { Z } }$dans$\mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq q } / a ^ { \mathbb { Z } }$definit une correspondance de´ $\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq q ^ { \prime } } } } / a ^ { \mathbb { Z } }$dans$\overline { { \mathrm { C h t } _ { N } ^ { r , \overline { { p } } \leq p ^ { \prime } } } } / a ^ { \mathbb Z }$au-dessus de$( X - N ) \times ( X - N )$et donc un homomorphisme

$$
H _ {c} ^ {2 r - 2} \big (\overline {{\mathrm{Cht} _ {N} ^ {r , \overline {{p}} \leq q}}} ^ {\prime} / a ^ {\mathbb {Z}} \big) \to H _ {c} ^ {2 r - 2} \big (\overline {{\mathrm{Cht} _ {N} ^ {r , \overline {{p}} \leq p}}} ^ {\prime} / a ^ {\mathbb {Z}} \big)
$$

qui, d’après le lemme A.7, fait commuter le diagramme :

$$
\begin{array}{c c c} H _ {c} ^ {2 r - 2} \big (\mathrm{Cht} _ {N} ^ {r, \overline {{p}} \leq q} / a ^ {\mathbb {Z}} \big) & \longrightarrow & H _ {c} ^ {2 r - 2} \big (\overline {{\mathrm{Cht} _ {N} ^ {r , \overline {{p}} \leq q}}} ^ {\prime} / a ^ {\mathbb {Z}} \big) \\ \uparrow & & \downarrow \\ H _ {c} ^ {2 r - 2} \big (\mathrm{Cht} _ {N} ^ {r, \overline {{p}} \leq p} / a ^ {\mathbb {Z}} \big) & \longrightarrow & H _ {c} ^ {2 r - 2} \big (\overline {{\mathrm{Cht} _ {N} ^ {r , \overline {{p}} \leq p}}} ^ {\prime} / a ^ {\mathbb {Z}} \big) \end{array}
$$