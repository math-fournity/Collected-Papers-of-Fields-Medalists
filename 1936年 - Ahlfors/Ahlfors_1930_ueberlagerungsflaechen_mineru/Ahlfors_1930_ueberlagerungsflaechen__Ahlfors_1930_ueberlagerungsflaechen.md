# ZUR THEORIE DER ÜBERLAGERUNGSFLÄCHEN.

Von

LARS AHLFORS

in HELSINGFORS.

## Einleitung.

Die vorliegende Arbeit hat ihren Ursprung in einem Versuch die wichtigsten Ergebnisse der Theorie der meromorphen Funktionen auf geometrischem Wege zu gewinnen. Es ging in diesem Zusammenhang hervor, dass die Hauptsätze von R. NEVANLINNA, und damit auch fast alle klassischen Resultate, nur zu einem gewissen, leicht abgrenzbaren Teil vom analytischen Charakter der Abbildung abhängen, während die ganze Struktur dieser Sätze lediglich aus den metrischen und topologischen Eigenschaften der Riemannschen Fläche bestimmt wird, auf welche die komplexe Ebene abgebildet wird. Diese Fläche hat man sich dabei über die Riemannsche Kugel ausgebreitet zu denken, d. h. sie erscheint als Überlagerungsfläche einer geschlossenen Grundfläche.

In der Topologie werden meistens nur solche Überlagerungsflächen behandelt, welche in Bezug auf die Grundfläche relativ unberandet sind. Das hat seinen Grund darin, dass man nur für unberandete Überlagerungsflächen allgemeingültige, rein-topologische Beziehungen aufstellen kann. Wenn wir in dieser Arbeit eine Theorie entwickeln wollen, die auch für berandete Überlagerungsflächen gültig sein soll, so sind wir also gezwungen eine Metrik einzuführen. Es wird dann möglich topologisch-metrische Beziehungen aufzustellen, die als Verallgemeinerungen der bekannten topologischen Eigenschaften der unberandeten Überlagerungsflächen anzusehen sind.

In diesem Sinne wird diejenige Ungleichung, aus welcher bei konformer Abbildung der zweite Hauptsatz von NEVANLINNA hervorgeht, als Erweiterung

der bekannten HURWITZ-RIEMANNschen Relation erscheinen. Hierdurch erhält die zwischen dem zweiten Hauptsatz und der RIEMANNschen Relation bestehende Analogie ihre endgültige Erklärung.

## I. Endliche Überlagerungsflächen.

## § 1. Die Metrik der Grundfläche.

1. Die Definition einer Fläche wird beim Leser als bekannt vorausgesetzt, ebenso was unter der Umgebung eines Flächenpunktes zu verstehen ist. $^{1}$  Durch den Umgebungsbegriff sind auch die Definitionen einer einfachen Kurve, eines Gebiets, einer abgeschlossenen Punktmenge usw. gegeben. Die Definition der Fläche setzt die Möglichkeit einer Dreiecksteilung voraus. Wir betrachten zunächst nur solche Flächen, bei welchen die Anzahl der Dreiecke endlich ist. Eine derartige endliche Fläche heisst geschlossen, wenn sämtliche Dreieckskanten zu zwei verschiedenen Dreiecken gehören, sie ist berandet, wenn wenigstens eine Kante zu einem einzigen Dreieck gehört.

Die Fläche ist mit einer Metrik versehen, wenn jeder einfachen Kurve eine positive, endliche oder unendliche Länge zukommt, und wenn jedes Gebiet, das von einer einfachen Kurve mit endlicher Länge begrenzt wird, einen positiven, endlichen Flächeninhalt besitzt. Sowohl die Länge als der Flächeninhalt sollen additiv sein. Die untere Grenze der Längen aller Kurven, welche zwei gegebene Punkte verbinden, heisst der Abstand dieser Punkte. In jeder brauchbaren Metrik muss dieser Abstandsbegriff folgende Eigenschaften haben: 1° Der Abstand zwischen zwei verschiedenen Punkten ist immer positiv und endlich; 2° Zu jedem Punkte P und jeder positiven Zahl ε gehört eine Umgebung, deren Punkte einen Abstand kleiner als ε von P haben. Es folgt dann z. B., dass zwei abgeschlossene, fremde Punktmengen einen bestimmten, positiven kürzesten Abstand haben.

Wir betrachten zunächst eine geschlossene Fläche  $W_{0}$  und setzen voraus, dass ihre Metrik ausser den oben angegebenen allgemeinen Bedingungen noch einer besonderen Regularitätsbedingung genügt. Gemäss dieser Bedingung soll zu jedem Punkte P auf  $W_{0}$  eine Umgebung  $U_{P}$  gehören, innerhalb deren jede geschlossene Kurve von der Länge L ein Gebiet vom Inhalt I < kL begrenzt,

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">131-163</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Wir verweisen den Leser auf die Darstellung bei KERÉKJÁRTÓ: Vorl. über Topologie, S. 131—163.</span></small>

wobei k nur von der Umgebung abhängt. $^{1}$  Man erkennt leicht, dass diese Voraussetzung äusserst allgemein ist.

Es sei $\delta$ der kürzeste Abstand von $P$ zum Rande der Umgebung $U_P$, und $U_P'$ eine Umgebung, deren Punkte einen Abstand kleiner als $\frac{\partial}{2}$ von $P$ haben. Nach einem bekannten Satz kann man die ganze Fläche $W_0$ mit endlich vielen Umgebungen $U_P'$ überdecken. Wir setzen $d$ gleich der kleinsten der zugehörigen Zahlen $\frac{\partial}{2}$ und sehen sofort, dass jede Kurve, deren Länge kleiner als $d$ ist, ganz in einer der endlich vielen Umgebungen $U_P$ liegt, die den ausgewählten Umgebungen $U_P'$ entsprechen. Wenn noch die grösste der zu denselben Umgebungen $U_P$ gehörigen Konstanten wieder mit $k$ bezeichnet wird, so können wir also schliessen, dass jede geschlossene Kurve von der Länge $L < d$ ein Gebiet vom Inhalt $I < kL$ begrenzt.

2. Aus dem letzten Resultat leitet man sofort folgende Eigenschaft im Grossen ab:

Hilfssatz 1. — Die Fläche $W_0$ sei durch eine oder mehrere geschlossene Kurven von der Gesamtlänge $L$ in zwei Teile zerlegt, so dass jeder Teil aus endlich vielen Gebieten besteht. Wenn die Flächeninhalte dieser Teile mit $I'$ und $I''$ bezeichnet werden, so gilt

$$
\operatorname{Min} \left(I ^ {\prime}, I ^ {\prime \prime}\right) \leq k L,\tag{1}
$$

wo k nur von der Fläche  $W_{0}$  abhängt.

Zuerst wird angenommen, dass die Länge $L^{(v)}$ jeder einzelnen Kurve kleiner als $d$ ist. Jede Kurve begrenzt dann ein Gebiet vom Inhalt $I^{(v)} < kL^{(v)}$. Die Punkte der Fläche, welche in keinem dieser Gebiete liegen, gehören alle zu demselben der zwei Teile, in welche $W_0$ zerlegt wurde. Hieraus folgt, dass der andere Teil einen Inhalt kleiner oder gleich $\Sigma I^{(v)} < k\Sigma L^{(v)} = kL$ hat.

Wenn andererseits $L \geq d$, so ist der Satz trivial. Wählt man nämlich $k = I_0 / 2d$, wo $I_0$ den Inhalt der ganzen Fläche $W_0$ bezeichnet, so folgt (1) sofort aus $\text{Min}(I', I'') \leq I_0 / 2$.

3. Wir betrachten jetzt auf  $W_{0}$  eine geschlossene oder offene Kurve  $\gamma$ . In einer der Umgebungen  $U_{P}$  sei eine geschlossene Kurve von der Länge L

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$k^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Wir machen darauf aufmerksam, dass wir in der ganzen Arbeit mit k oder  $k'$  eine konstante Grösse bezeichnen, aber nicht notwendig immer dieselbe.</span></small>

gezogen. Wenn das von dieser Kurve eingeschlossene, in  $U_{P}$  gelegene Gebiet einen Bogen der Kurve  $\gamma$  enthält, so sei  $\lambda$  die Länge dieses Bogens. Wir nehmen an, dass die Kurve  $\gamma$  einer Regularitätsbedingung genügt, welche durch eine Ungleichung der Form  $\lambda < k'L$  ausgedrückt wird, wobei  $k'$  wieder nur von der Umgebung  $U_{P}$  abhängt.

Man kann hieraus einen zweiten Hilfssatz herleiten:

Hilfssatz 2. — Wenn die Fläche $W_0$ wieder in derselben Weise in zwei Teile zerlegt wird, und $\lambda', \lambda''$ die Längen der zu den beiden Teilen gehörigen Stücke der Kurve $\gamma$ bezeichnen, so gilt

$$
\operatorname{Min} \left(\lambda^ {\prime}, \lambda^ {\prime \prime}\right) \leq k ^ {\prime} L,
$$

wo $k^{\prime}$ nur von $W_0$ und $\gamma$ abhängt.

Der Beweis ist natürlich ganz analog zu dem vorigen.

4. Der Fall einer berandeten Fläche kann leicht auf den bereits erledigten Fall zurückgeführt werden. Man braucht nämlich nur zwei Exemplare der berandeten Fläche  $W_{0}$  zu nehmen und ihre Randkurven punktweise zu identifizieren, um eine geschlossene Fläche zu erhalten, deren Metrik durch die Metrik der ursprünglich vorgelegten Fläche gegeben ist. Es wird vorausgesetzt, dass die neue Fläche den nötigen Regularitätsbedingungen genügt.

Durch die Verdopplung werden alle Querschnitte von  $W_{0}$  geschlossen. Hieraus geht hervor, dass die beiden Hilfssätze ihre Gültigkeit behalten, wenn die Zerlegung mit Hilfe von geschlossenen Kurven und Querschnitten, also durch relativ zu  $W_{0}$  geschlossene Kurven geschieht.

Im zweiten Hilfssatz kann man besonders für  $\gamma$  die Randkurve C von  $W_{0}$  wählen, vorausgesetzt dass sie der Regularitätsbedingung genügt. Das hierdurch gewonnene Ergebnis möge noch besonders formuliert werden:

Wenn eine berandete Fläche  $W_{0}$  durch endlich viele Querschnitte von der Gesamtlänge L in zwei Teile zerlegt wird, so zerfällt der Rand in Teile, deren Längen  $\lambda'$  und  $\lambda''$  der Bedingung

genügen.

$$
\operatorname{Min} \left(\lambda^ {\prime}, \lambda^ {\prime \prime}\right) \leq k ^ {\prime} L
$$

## § 2. Metrische Eigenschaften der Überlagerungsfläche.

5. Eine endliche Fläche W ist über die Grundfläche  $W_{0}$  ausgebreitet oder bildet eine Überlagerungsfläche derselben, wenn es eine Dreiecksteilung der beiden Flächen gibt, die eine Zuordnung der folgenden Art gestattet:

Jedem Dreieck D von W ist ein bestimmtes Dreieck  $D_{0}$  von  $W_{0}$  als Spurdreieck zugeordnet. Zu zwei Dreiecken mit einer gemeinsamen Kante oder Ecke sollen zwei Spurdreiecke gehören, die ebenfalls eine Kante oder Ecke gemeinsam haben. Sind schliesslich  $D_{0}^{(1)}$  und  $D_{0}^{(2)}$  zwei benachbarte Dreiecke auf  $W_{0}$, und bezeichnet  $D^{(1)}$  ein beliebiges Dreieck auf W, dessen Spurdreieck  $D_{0}^{(1)}$  ist, so soll es höchstens ein Dreieck  $D^{(2)}$  mit dem Spurdreieck  $D_{0}^{(2)}$  geben, das mit  $D^{(1)}$  eine gemeinsame Kante hat.

Durch topologische Abbildung der Dreiecke D auf ihre Spurdreiecke wird jedem Punkt der Fläche W ein bestimmter Spurpunkt auf  $W_{0}$  zugeordnet. Die Abbildung kann so eingerichtet werden, dass die Eckpunkte und Kantenpunkte eines Dreiecks den Eckpunkten bzw. Kantenpunkten des Spurdreiecks entsprechen, wobei die gemeinsamen Randpunkte benachbarter Dreiecke gemeinsame Spurpunkte haben sollen. Wenn  $P_{0}$  der Spurpunkt von P ist, so sagen wir auch der Punkt P liege über  $P_{0}$ .

Der relative Rand von W in Bezug auf  $W_{0}$  besteht aus den Randpunkten von W, die über einem inneren Punkt der Grundfläche liegen. Ein relativer Rand entsteht nur dann, wenn es auf  $W_{0}$  ein Paar von benachbarten Dreiecken  $D_{0}^{(1)}$  und  $D_{0}^{(2)}$  gibt, sodass ein gewisses über  $D_{0}^{(1)}$  gelegenes Dreieck  $D^{(1)}$  mit keinem über  $D_{0}^{(2)}$  gelegenen Dreieck eine Kante gemeinsam hat. Eine Überlagerungsfläche ohne relativen Rand heisst relativ unberandet oder unbegrenzt.

Ein innerer Eckpunkt P auf W gehört zu einem Zyklus von Dreiecken D, deren Spurdreiecke  $D_{0}$  zyklisch um den Spurpunkt  $P_{0}$  angeordnet sind. Über jedem der Dreiecke  $D_{0}$  liegt dieselbe Anzahl h von Dreiecken D in jenem Zyklus. Ist h > 1, so heisst P ein Verzweigungspunkt der Fläche W; h heisst die Vielfachheit des Punktes P, h - 1 die Verzweigungsordnung.

Die Metrik der Grundfläche überträgt sich unmittelbar auf die Überlagerungsfläche. Um die Länge einer Kurve zu bestimmen, zerlegen wir sie in die Teile, die in den verschiedenen Dreiecken D liegen. Jedem Teil geben wir die Länge seiner Spurkurve und erhalten durch Addition die Länge der gegebenen Kurve. Ganz ähnlich wird der Inhalt eines beliebigen Gebiets bestimmt.

21-34686. Acta mathematica. 65. Imprimé le 8 février 1935.

6. Man erhält eine übersichtliche Darstellung der Überdeckungseigenschaften der Fläche W durch folgende Betrachtung. In der Folge  $W_{1}, W_{2}, \ldots, W_{n}, \ldots$  sei  $W_{n}$  die Menge derjenigen Punkte auf  $W_{0}$ , über welchen wenigstens n innere Punkte der Fläche W liegen, wobei die Verzweigungspunkte mit der entsprechenden Vielfachheit gezählt werden sollen. Die Menge  $W_{n}$  besteht aus endlich vielen Gebieten und wird als das n:te Blatt der Fläche W bezeichnet. Aus der Definition folgt, dass die Mengenfolge abnehmend ist, d. h. jede Menge  $W_{n}$  enthält alle folgenden. Der grösste Index n, für welchen  $W_{n}$  nicht leer ist, heisst die maximale Blätteranzahl der Überlagerungsfläche und soll mit N bezeichnet werden.

In Überdeckungshinsicht ist die Fläche W äquivalent mit der Blätterfolge  $W_{1}, W_{2}, \ldots, W_{N}$ . In der Tat, wenn ein Punkt  $P_{0}$  zu den genau  $n_{0}$  ersten Blättern  $W_{n}$  gehört, so wird er von genau  $n_{0}$  inneren Punkten der Fläche W überdeckt. Hieraus folgt auch, dass man den Inhalt I der ganzen Fläche W erhält, wenn man die Inhalte  $I_{n}$  der Blätter  $W_{n}$  addiert:

$$
I = I _ {1} + I _ {2} + \dots + I _ {N}.\tag{2}
$$

Der relative Rand von W entspricht in ähnlicher Weise den relativen Rändern der verschiedenen Blätter. Eine innere Dreieckskante auf  $W_{0}$ , welche selbst nicht zu  $W_{n}$  gehört, soll einfach zum relativen Rande von  $W_{n}$  gezählt werden, wenn sie Kante eines zu  $W_{n}$  gehörigen Dreiecks ist; sie wird doppelt gezählt, wenn sie die gemeinsame Kante von zwei solchen Dreiecken ist. Wenn mit dieser Festsetzung die Summe der Vielfachheiten einer Kante in Bezug auf alle Blätter gleich  $n_{0}$  ist, so liegen über dieser Kante genau  $n_{0}$  Kanten, die zum relativen Rande von W gehören. Wenn L und  $L_{n}$  die Längen der relativen Ränder von W und  $W_{n}$  bezeichnen, so gilt

$$
L = L _ {1} + L _ {2} + \dots + L _ {N},
$$

wobei die Länge einer doppelten Kante zweifach zu zählen ist.

7. Wenn der Inhalt I durch den Inhalt  $I_{0}$  der Grundfläche  $W_{0}$  dividiert wird, so erhält man eine Zahl S, die wir als die mittlere Blätteranzahl von W bezeichnen. Nach (2) gilt

$$
S = S _ {1} + S _ {2} + \dots + S _ {N},
$$

wo  $S_{n}$  die mittlere Blätteranzahl von  $W_{n}$  ist.

Betrachten wir ein Teilgebiet $\Delta$ von $W_{0}$, so können wir die mittlere Blätteranzahl über $\Delta$ durch die Zahl $S(\Delta)$ ausdrücken, die man erhält, wenn man den Inhalt sämtlicher über $\Delta$ gelegener Teile von $W$ durch den Inhalt $\delta$ des Gebiets $\Delta$ dividiert. Man hat in leicht verständlicher Bezeichnung

$$
S (\mathcal {A}) = S _ {1} (\mathcal {A}) + S _ {2} (\mathcal {A}) + \dots + S _ {N} (\mathcal {A})
$$

und folglich

$$
S - S (\mathcal {A}) = \sum_ {1} ^ {N} (S _ {n} - S _ {n} (\mathcal {A})).
$$

Hieraus ergibt sich durch eine leichte Überlegung eine Abschätzung der Differenz  $|S-S(\mathcal{A})|$ . Wenn man ausdrückt, dass der Inhalt des in  $\varDelta$  gelegenen Teils von  $W_{n}$  höchstens gleich dem ganzen Inhalt von  $W_{n}$  ist, so erhält man

$$
S _ {n} (\mathcal {A}) \leqslant \frac {I _ {0}}{\delta} S _ {n}.
$$

Ersetzt man  $W_{n}$  durch die Komplementärmenge  $W_{0}-W_{n}$ , so folgt in derselben Weise

$$
\mathrm{I} - S _ {n} (\mathcal {A}) \leq \frac {I _ {0}}{\delta} (\mathrm{I} - S _ {n}).
$$

Man hat nun einerseits

$$
\left| S _ {n} - S _ {n} (\mathcal {A}) \right| \leq \operatorname{Max} \left(S _ {n}, S _ {n} (\mathcal {A})\right) \leq \frac {I _ {0}}{\delta} S _ {n}
$$

und andererseits

$$
\left| S _ {n} - S _ {n} (\mathcal {A}) \right| = \left| (1 - S _ {n}) - (1 - S _ {n} (\mathcal {A})) \right| \leq \operatorname{Max} (1 - S _ {n}, 1 - S _ {n} (\mathcal {A})) \leq \frac {I _ {0}}{\delta} (1 - S _ {n}).
$$

Diese Ungleichungen kann man in die eine Ungleichung

$$
\left| S _ {n} - S _ {n} (\mathcal {A}) \right| \leq \frac {I _ {0}}{\delta} \operatorname{Min} \left(S _ {n}, \mathrm{I} - S _ {n}\right)
$$

zusammenfassen. Wenn jetzt die Metrik von  $W_{0}$  den früher aufgestellten Bedingungen genügt, so gilt der erste Hilfssatz, und wir finden

$$
\left| S _ {n} - - S _ {n} (\Delta) \right| \leq \frac {k}{\delta} L _ {n},
$$

woraus durch Addition

$$
\left| S - S (\mathcal {A}) \right| \leq \frac {k}{\delta} \sum_ {1} ^ {N} L _ {n} = \frac {k}{\delta} L.
$$

Hiermit ist der erste Teil des für die ganze Theorie grundlegenden Überdeckungssatzes bewiesen:

Überdeckungssatz 1. — Die mittlere Blätteranzahl über der ganzen Grundfläche $W_0$ unterscheidet sich von der mittleren Blätteranzahl über einem Teilgebiet $\Delta$ um eine Grösse, die durch die Länge $L$ des relativen Randes majoriert wird, d. h. es gilt eine Ungleichung der Form

$$
\left| S - S (\mathcal {A}) \right| \leq k L.\tag{I. I}
$$

Das Wesentliche in diesem Satze ist natürlich, dass die Abschätzung gleichmässig für alle Überlagerungsflächen gilt, indem die Konstante k nur von  $W_{0}$  und  $\Delta$  abhängt, dagegen weder von der Überlagerungsfläche W noch von der zu ihrer Definition verwendeten Dreiecksteilung. Ist L = 0 so wird  $S = S(\Delta)$  für jedes Gebiet  $\Delta$, d. h. die Blätteranzahl einer relativ unberandeten Überlagerungsfläche ist konstant.

8. Wir gehen dann zur Untersuchung der linearen Überdeckung über. Auf  $W_{0}$  betrachten wir eine Kurve  $\gamma$  von der Länge  $\lambda_{0}$ , welche der in 3. eingeführten Regularitätsbedingung genügt. Die mittlere Blätteranzahl über  $\gamma$  wird mit  $s(\gamma)$  bezeichnet, und ist gleich der durch  $\lambda_{0}$  dividierten Länge sämtlicher über  $\gamma$  gelegener Kurven auf W. Auch für  $s(\gamma)$  gilt die Zerlegung

$$
s (\gamma) = s _ {1} (\gamma) + s _ {2} (\gamma) + \dots + s _ {N} (\gamma).
$$

Wenn $\gamma'$ einen Teilbogen von $\gamma$ bezeichnet, so kann man ganz wie in der vorigen Nummer die Differenz $|s(\gamma)-s(\gamma')|$ abschätzen. Man erhält unter Anwendung des zweiten Hilfssatzes

$$
\left| s (\gamma) - s \left(\gamma^ {\prime}\right) \right| \leq \frac {k ^ {\prime}}{\lambda^ {\prime}} L,
$$

wo $\lambda'$ die Länge von $\gamma'$ bedeutet. Hieraus schliesst man, dass die Differenz zwischen den mittleren Blätteranzahlen über zwei verschiedenen Kurven durch $L$ majoriert wird, denn sie können als Teilbogen derselben Kurve aufgefasst werden.

Wir wollen noch zeigen, dass auch  $s(\gamma)$  und S sich nur um eine durch L majorierte Grösse unterscheiden. Wir wählen für  $\gamma$  eine Kurve, welche die Fläche  $W_{0}$  zerlegt. Es sei  $\Delta$  das kleinere der von  $\gamma$  begrenzten Teilgebiete.

Wenn man den ersten Hilfssatz auf den Durchschnitt von  $W_{n}$  und  $\Delta$  anwendet, so erhält man

$$
S _ {n} (\mathcal {A}) \leq \frac {k}{\delta} \left(\lambda_ {0} s _ {n} (\gamma) + L _ {n}\right).
$$

Ebenso gilt für den Durchschnitt von $W_{0}-W_{n}$ und $\Delta$

$$
\mathrm{I} - S _ {n} (\mathcal {A}) \leqslant \frac {k}{\delta} \left(\lambda_ {0} (\mathrm{I} - s _ {n} (\gamma)) + L _ {n}\right).
$$

Hieraus folgt, wenn man die aus dem ersten Hilfssatz folgende Ungleichung $\delta \leq k\lambda_{0}$ beachtet, einerseits

$$
\left| S _ {n} (\mathcal {A}) - s _ {n} (\gamma) \right| \leq \operatorname{Max} \left(S _ {n} (\mathcal {A}), s _ {n} (\gamma)\right) \leq \frac {k}{\delta} \left(\lambda_ {0} s _ {n} (\gamma) + L _ {n}\right)
$$

und andererseits

$$
\left| S _ {n} (\mathcal {A}) - s _ {n} (\gamma) \right| \leq \operatorname{Max} \left(\mathrm{i} - S _ {n} (\mathcal {A}), \mathrm{i} - s _ {n} (\gamma)\right) \leq \frac {k}{\delta} (\lambda_ {0} \left(\mathrm{i} - s _ {n} (\gamma)\right) + L _ {n}).
$$

Wenn jetzt noch der zweite Hilfssatz angewandt wird, so ergibt sich endlich

$$
\left| S _ {n} (\mathcal {A}) - s _ {n} (\gamma) \right| \leq \frac {k}{\delta} \left(\lambda_ {0} \operatorname{Min} (s _ {n} (\gamma), 1 - s _ {n} (\gamma)) + L _ {n}\right) \leq \frac {k}{\delta} \left(\lambda_ {0} k ^ {\prime} + 1\right) L _ {n} = \bar {k} L _ {n}.
$$

Durch Addition erhält man dann

und mit Hilfe von (I. 1)

$$
\begin{array}{l} \left| S (\mathcal {A}) - s (\gamma) \right| \leq \bar {k} L, \\ \left| S - s (\gamma) \right| \leq (k + \bar {k}) L. \end{array}
$$

Die neue Konstante können wir wieder mit k bezeichnen und finden so den zweiten Teil des Überdeckungssatzes:

Überdeckungssatz 2. — Der Unterschied zwischen den mittleren Blätteranzahlen über der ganzen Fläche $W_0$ und über einer Kurve γ genügt einer Ungleichung der Form

$$
\left| S - s (\gamma) \right| \leq k L.\tag{I. 2}
$$

Wenn  $W_{0}$  berandet ist, so kann man für  $\gamma$  besonders einen Teilbogen des Randes wählen. Diese Art der Anwendung wird im folgenden sehr wichtig.

## § 3. Die Charakteristik.

9. In diesem Abschnitt ist W eine beliebige endliche Fläche, auf der eine Dreiecksteilung gegeben ist. Die Ecken der Dreiecke sind entweder innere Ecken, d. h. innere Punkte der Fläche W, oder sie liegen auf dem Rand von W. Ebenso unterscheidet man zwischen inneren Kanten und zum Rande gehörigen Kanten. Wir wollen mit E die Anzahl der inneren Ecken, mit K die Anzahl der inneren Kanten und schliesslich mit P die Anzahl der Dreiecke (Polygone) auf der Fläche W bezeichnen. Aus diesen Anzahlen bildet man die Grösse

$$
\varrho = - E + K - P,
$$

die als Charakteristik der Fläche W in der vorgegebenen Dreiecksteilung bezeichnet wird.

Wenn wir eine Anzahl der inneren Kanten und Ecken unterdrücken, so erhalten wir eine polygonale Zerlegung, welche die gegebene Dreiecksteilung als Unterteilung besitzt. Die erhaltenen Teilgebiete bezeichnen wir mit $\Omega$, die aus den übriggebliebenen inneren Kanten gebildeten Kurven mit $\sigma$. Die Charakteristik eines Gebiets $\Omega$ in der gegebenen Dreiecksteilung sei $\varrho(\Omega)$. Wenn $\bar{E}$ und $\bar{K}$ die Anzahlen der übriggebliebenen Dreiecksteile sind, so wird offenbar

$$
\varrho = \sum \varrho (\Omega) - \bar {E} + \bar {K}.\tag{3}
$$

Wir wollen als bewiesen voraussetzen, dass die Charakteristik eines Dreiecks in jeder Unterteilung gleich -1 ist. Dann erkennt man leicht, dass die Charakteristik auch im allgemeinen Falle von der Dreiecksteilung unabhängig ist und folglich eine topologische Invariante darstellt. Es genügt nämlich zu zeigen, dass eine Teilung und ihre Unterteilung dieselbe Charakteristik ergeben, und dieses geht durch Anwendung der Formel (3) hervor. In der Tat, jedes $\varrho(\Omega)$ ist gleich -1, und wenn $\overline{E}, \overline{K}, \overline{P}$ die zur Oberteilung gehörigen Anzahlen sind, so erhält man für die Charakteristik der Unterteilung den Ausdruck $-\overline{E} + \overline{K} - \overline{P}$.

Die Bedeutung des Gliedes  $-\bar{E}+\bar{K}$  in der Gleichung (3) soll näher untersucht werden. Eine einfache geschlossene Kurve enthält ebensoviele Kanten wie Ecken und gibt also keinen Beitrag zum genannten Glied, während ein Querschnitt eine Kante mehr enthält und folglich den Beitrag 1 liefert. Wenn nun die Zerlegung der Fläche W in die Gebiete  $\Omega$  durch lauter punktfremde Rückkehrschnitte und Querschnitte erfolgt, so findet man also

$$
\varrho = \sum \varrho (\Omega) + n (\sigma),\tag{4}
$$

wo  $n(\sigma)$  die Anzahl der Querschnitte bezeichnet. Die Formel (4), die wir als die allgemeine Zerlegungsformel bezeichnen wollen, wird uns in den Anwendungen oft begegnen.

Wir verwenden sie zunächst um die Charakteristiken der verschiedenen topologischen Typen zu ermitteln. Eine schlichtartige Fläche mit q Konturen kann durch q - 1 Querschnitte in eine Fläche verwandelt werden, die topologisch äquivalent mit einem Dreieck ist; die Charakteristik wird folglich gleich q - 2. Eine orientierbare Fläche mit q Konturen und q' nicht zerlegenden Rückkehrschnitten wird durch diese Rückkehrschnitte in eine schlichtartige Fläche mit  $q + 2q'$  Konturen verwandelt. Sie erhält also die Charakteristik  $q + 2q' - 2$ . Auch die Charakteristik einer nicht orientierbaren Fläche liesse sich leicht berechnen, hat aber in dieser Arbeit keine Bedeutung.

Die geschlossene Fläche vom Geschlecht Null besitzt mit $\varrho = -2$ die kleinste Charakteristik. Für berandete Flächen ist die kleinste Charakteristik gleich $-1$; sie kommt allen einfach zusammenhängenden Flächen zu. Wenn man von dieser Bemerkung Gebrauch macht, so bekommt man aus (4) eine wichtige Ungleichung. Es wird nämlich, wenn $N(\Omega)$ die Anzahl der Gebiete $\Omega$ angibt,

$$
\varrho \geq n (\sigma) - N (\Omega),\tag{5}
$$

und das Gleichheitszeichen gilt nur, wenn sämtliche Teilgebiete einfach zusammenhängend sind. Etwas genauer gilt sogar

$$
\varrho \geq n (\sigma) - N _ {1} (\Omega),\tag{\( (5') \}
$$

wo  $N_{1}(\Omega)$  die Anzahl der einfach zusammenhängenden Gebiete  $\Omega$  ist.

10. Wenn W als Überlagerungsfläche von  $W_{0}$  gegeben ist, so besteht eine der Hauptaufgaben dieser Arbeit in der Aufstellung der Beziehungen zwischen den Charakteristiken von W und  $W_{0}$ . Als Vorbereitung wollen wir in dieser Nummer den Zusammenhang zwischen der Charakteristik von W und den topologischen Eigenschaften der zugehörigen Blätter  $W_{n}$  untersuchen.

Der Betrachtung wird diejenige Dreiecksteilung der Fläche $W_0$ zugrunde gelegt, mit deren Hilfe die Überlagerungsfläche definiert wird. Wenn $E_n$, $K_n$ und $P_n$ die zu $W_n$ gehörigen Anzahlen sind, so ist $\varrho_n = -E_n + K_n - P_n$ die Summe der Charakteristiken derjenigen Gebiete, aus denen $W_n$ besteht. Für die Teilung

der Fläche W gilt, wie man sofort bestätigt,  $P = \sum P_{n}$  und  $K = \sum K_{n}$ . Dagegen ist im allgemeinen  $E \leq \sum E_{n}$ , denn bei der Berechnung von E wird die Vielfachheit der Ecken nicht berücksichtigt. Die genaue Relation lautet  $E = \sum E_{n} - w$ , wo w die sog. Verzweigungszahl der Fläche W bezeichnet, d. h. die Summe der Ordnungen sämtlicher Verzweigungspunkte. Aus den gefundenen Gleichungen ergibt sich unmittelbar

$$
\varrho = \sum \varrho_ {n} + w.\tag{6}
$$

Die Charakteristik einer Überlagerungsfläche ist gleich der Summe der Charakteristiken der Gebiete, aus welchen die einzelnen Blätter bestehen, vermehrt um die Verzweigungszahl der Fläche.

Dieser Satz bildet eine direkte Verallgemeinerung der bekannten Hurwitzschen Relation für unberandete Überlagerungsflächen. Wenn W keinen relativen Rand besitzt, so sind alle  $\varrho_{n}$  gleich der Charakteristik  $\varrho_{0}$  der Grundfläche. Man erhält dann  $\varrho = N\varrho_{0} + w$ , wo N die Blätteranzahl bezeichnet. Diese Gleichung ist mit der Hurwitzschen Relation identisch.

## § 4. Der metrisch-topologische Hauptsatz.

11. Die im letzten Abschnitt gefundene Gleichung (6) bildet eine rein topologische Verallgemeinerung der Hurwitzschen Relation. Sie hat den wesentlichen Nachteil, dass man für ihre Verwertung die Grössen  $\varrho_{n}$  kennen muss, die in komplizierter Weise von den Überdeckungs- und Zusammenhangseigenschaften der Überlagerungsfläche abhängen.

Es liegt nahe nach einer metrisch-topologischen Verallgemeinerung der Hurwitzschen Relation zu suchen, welche die früher eingeführte mittlere Blätteranzahl benutzt. Eine solche Verallgemeinerung wird durch den folgenden Satz gegeben, dessen zentrale Stellung in unserer Theorie die Bezeichnung Hauptsatz rechtfertigt:

Metrisch-topologischer Hauptsatz. — Es sei  $W_{0}$  eine geschlossene oder berandete Grundfläche mit der Charakteristik  $\varrho_{0}$ , W eine Überlagerungsfläche derselben. Wenn  $\varrho$  die Charakteristik von W bedeutet, so sei  $\dot{\varrho}$  die grössere der Zahlen  $\varrho$  und o. Dann gilt die Ungleichung

$$
\stackrel {+} {\varrho} \geq \varrho_ {0} S - k L,\tag{II. 1}
$$

wo S die mittlere Blätteranzahl, L die Länge des relativen Randes bezeichnet.

Es soll zunächst kurz erklärt werden, wie man zu dieser Formulierung kommt. Aus der Hurwitzschen Relation $\varrho = N\varrho_{0} + w$ folgt die weniger genaue Ungleichung $\varrho \geq N\varrho_{0}$. Um diese Ungleichung auf den Fall einer berandeten Überlagerungsfläche zu verallgemeinern ersetzen wir $N$ durch die mittlere Blätterzahl $S$ und fügen rechts ein Restglied hinzu. Die Ungleichung (II. I) besagt im Falle $\varrho > 0$, dass für dieses Restglied eine ähnliche Abschätzung gilt wie in (I. I) und (I. 2). Wenn $\varrho = -1$ ist, so ist es klar dass man auf der linken Seite Null schreiben muss, denn $S$ und $L$ können beliebig klein sein.

Wir bemerken schliesslich, dass der Satz trivial ist für $\varrho_{0} \leq 0$. Wir brauchen also nur solche Grundflächen zu betrachten, deren Charakteristik $\varrho_{0}$ positiv ist.

12. Wir beginnen unseren Beweis mit dem Fall einer schlichtartigen Grundfläche. $W_0$ besitze $q > 2$ geschlossene Konturen, die sich eventuell auf Punkte reduzieren können; dann gilt $\varrho_0 = q - 2$. Durch $q$ punktfremde Querschnitte $\gamma_1, \ldots, \gamma_q$ mit endlicher Länge zerlegt man die Grundfläche in zwei einfach zusammenhängende Teile $\Delta'$ und $\Delta''$. Die Wahl dieser Querschnitte soll natürlich ein für alle Mal festgelegt werden, und darf nicht von der Überlagerungsfläche $W$ abhängen.

Die Überlagerungsfläche W ist definiert mit Hilfe einer gewissen Dreiecksteilung der Grundfläche. Wir nehmen an, dass es eine gewisse Unterteilung dieser Teilung gibt, in welcher die Querschnitte  $\gamma_{1}, \ldots, \gamma_{q}$  aus lauter Kanten bestehen. Ferner wird vorausgesetzt, dass W keine über diesen Querschnitten gelegenen Verzweigungspunkte besitzt. Diese Annahmen bedeuten keine Einschränkung, denn jede Fläche kann durch eine beliebig kleine Deformation, welche den Zusammenhang unverändert lässt und eine beliebig kleine Änderung von S und L verursacht, in eine Fläche verwandelt werden, die diesen Voraussetzungen genügt.

Die folgenden Betrachtungen beziehen sich auf die oben eingeführte Unterteilung und die ihr entsprechende Dreiecksteilung der Fläche W. Auf W ziehen wir sämtliche Kantenzüge, die über den Querschnitten γ liegen. Sie bilden ein System von punktfremden Querschnitten σ der Fläche W, welche diese Fläche in endlich viele Gebiete Ω zerlegen. Für diese Zerlegung gilt die im vorigen Abschnitt bewiesene topologische Ungleichung

$$
\varrho \geq n (\sigma) - N (\Omega).\tag{5}
$$

22-34686. Acta mathematica. 65. Imprimé le 8 février 1935.

Aus dieser Ungleichung soll die gewünschte Relation (II. 1) hergeleitet werden. Dazu wird zunächst eine Klasseneinteilung der Querschnitte σ und der Gebiete Ω eingeführt, welche den Weg zum Beweis bereitet.

13. Wir beginnen mit der Absonderung einer Folge von Gebietsklassen  $(\Omega_{1}), \ldots, (\Omega_{p})$  und entsprechenden Querschnittsklassen  $(\sigma_{1}), \ldots, (\sigma_{p})$ , die in folgender Weise definiert werden:

Zu der ersten Klasse  $(\Omega_{1})$  gehören sämtliche Gebiete  $\Omega$ , die von genau einem Querschnitt  $\sigma$  begrenzt werden. Diese Querschnitte bilden die erste Querschnittsklasse  $(\sigma_{1})$ . Zur Klasse  $(\Omega_{2})$  zählen wir diejenigen Gebiete  $\Omega$ , deren Rand einen einzigen, nicht zur Klasse  $(\sigma_{1})$  gehörigen Querschnitt umfasst, und zur Klasse  $(\sigma_{2})$  diese Querschnitte. Allgemein sei  $(\Omega_{n})$  die Klasse derjenigen Gebiete  $\Omega$ , die von genau einem neuen, d. h. zu keiner der Klassen  $(\sigma_{1}),\ldots,(\sigma_{n-1})$  gehörigen Querschnitt begrenzt werden, und  $(\sigma_{n})$  die Klasse dieser neuen Querschnitte. Das Verfahren wird so lange fortgesetzt, bis sämtliche Gebiete  $\Omega$  erschöpft sind, oder bis sämtliche übriggebliebene Gebiete entweder von gar keinem oder von wenigstens zwei neuen Querschnitten begrenzt werden.

Aus der Definition folgt, dass jedes Gebiet $\Omega_{n}$ von einem Querschnitt $\sigma_{n}$ begrenzt wird. Umgekehrt wollen wir zeigen, dass jeder Querschnitt $\sigma_{n}$ im allgemeinen nur ein einziges Gebiet $\Omega_{n}$ begrenzen kann. Wir beweisen zuerst folgende Eigenschaft: Jeder Querschnitt $\sigma_{n}$ zerlegt die Fläche $W$ in zwei Teile, und alle Querschnitte $\sigma$, die in demselben Teilgebiet liegen wie ein von $\sigma_{n}$ begrenztes $\Omega_{n}$, gehören zu den Klassen $(\sigma_{1}),\ldots, (\sigma_{n-1})$.

Für $n=1$ ist der Satz unmittelbar klar. Wir nehmen an dass er bewiesen ist für alle Indizes, die kleiner als das gegebene $n$ sind. Das Gebiet $\Omega_{n}$ wird ausser von $\sigma_{n}$ noch von gewissen Querschnitten niedrigerer Klasse begrenzt. Diese Querschnitte bestimmen nach der Induktionsvoraussetzung je ein Teilgebiet von $W$, das nur Querschnitte von noch niedrigerer Ordnung enthält. Die Menge aller Punkte, welche ohne Überschreitung von $\sigma_{n}$ mit dem Innern von $\Omega_{n}$ verbunden werden können, wird aus $\Omega_{n}$ und den genannten Teilgebieten gebildet. Hieraus folgt, dass sämtliche in dieser Menge enthaltene Querschnitte $\sigma$ zu den Klassen $(\sigma_{1}),\ldots,( \sigma_{n-1})$ gehören, und unser Satz ist bewiesen.

Wenn es vorkommt, dass ein Querschnitt $\sigma_{n}$ gleichzeitig zwei Gebiete $\Omega_{n}$ begrenzt, so folgt aus dem soeben bewiesenen sofort, dass alle anderen Querschnitte von niedrigerer Klasse sind. Dieser Fall kann also nur eintreten, wenn sämtliche Querschnitte $\sigma$ zu den abgesonderten Klassen gehören, und auch dann

nur für den einzigen Querschnitt der höchsten Klasse. Von diesem Ausnahmefall abgesehen entsprechen sich die abgesonderten Gebiete und Querschnitte umkehrbar eindeutig.

Die übriggebliebenen Gebiete Ω werden, wie schon bemerkt wurde, entweder nur von abgesonderten Querschnitten oder von wenigstens zwei nicht abgesonderten Querschnitten begrenzt. Wir behaupten, dass der erste Fall nur ausnahmsweise vorkommt. In der Tat, wenn ein Gebiet Ω von lauter abgesonderten Querschnitten begrenzt wird, so bestimmen diese Querschnitte Teilgebiete, in deren Inneren nur abgesonderte Querschnitte liegen, und zwar keine von der höchsten Klasse. Hieraus schliesst man, dass alle Querschnitte abgesondert sind, und dass es höchstens ein Gebiet Ω von der betrachteten Art geben kann. Die Charakter eines Ausnahmefalls ist damit nachgewiesen.

14. Wir wollen jetzt voraussetzen, dass nicht sämtliche Querschnitte σ abgesondert sind, und für diesen Fall die Klasseneinteilung weiterführen. Jedes Ω, das zu keiner der Klassen (Ωn) gehört, wird nach dem vorhergehenden von wenigstens zwei nicht abgesonderten Querschnitten begrenzt. Jenachdem die Anzahl dieser Querschnitte kleiner als q oder wenigstens gleich q ist, zählen wir Ω zur Klasse (Ω') oder (Ω\*).

Die entsprechenden Querschnitte werden am besten in drei Klassen eingeteilt: Die Querschnitte der Klasse (σ\*) begrenzen zwei Gebiete Ω\*, die der Klasse (σ') begrenzen ein Ω\* und ein Ω' und die der Klasse (σ'') begrenzen zwei Gebiete Ω'.

Damit ist die ganze Klasseneinteilung vollzogen. Zur besseren Orientierung geben wir noch eine Übersicht über die eingeführten Klassen und wiederholen die wichtigsten Beziehungen. Die Klassen sind

$$
\begin{array}{c c} (\Omega_ {1}) \dots (\Omega_ {p}) & (\Omega^ {\prime}) \\ (\sigma_ {1}) \dots (\sigma_ {p}) & (\overbrace {\sigma^ {\prime}} ^ {\prime}) (\sigma^ {\prime \prime}) \end{array}\tag{\((\Omega^{*})\}
$$

$(\sigma^{*})$

und es gilt:

$^{1}$  Die  $\Omega_{n}$  und  $\sigma_{n}$  entsprechen sich ein-eindeutig.

$2^{\circ}$  Jedes  $\Omega'$  wird von wenigstens zwei, aber höchstens q-1 Querschnitten  $\sigma'$  oder  $\sigma''$  begrenzt.

$3^{\circ}$ Jedes $\Omega^{*}$ wird von wenigstens $q$ Querschnitten $\sigma'$, $\sigma''$ oder $\sigma^{*}$ begrenzt.

Die obige Einteilung bezieht sich auf den Fall, dass nicht sämtliche  $\sigma$  durch die Klassen  $(\sigma_{n})$  erschöpft werden. Auch im entgegengesetzten Falle genügen

die durchgeführten Untersuchungen um die Struktur der Fläche festzustellen. Wir brauchen aber, aus einem Grunde, der sofort klar werden wird, auf diesen Fall nicht näher einzugehen.

14. Wir kehren zur Ungleichung (5) zurück und betrachten die auf der rechten Seite stehende Differenz $n(\sigma)-N(\Omega)$. Wenn wir voraussetzen, dass nicht alle Querschnitte abgesondert sind, so heben sich die Anzahlen der zu den Klassen $(\Omega_{n})$ und $(\sigma_{n})$ gehörigen Gebiete und Querschnitte auf und brauchen bei der Berechnung der Differenz nicht berücksichtigt zu werden. Durch eine den Klassen $(\Omega^{\prime})$ und $(\Omega^{*})$ entsprechende Aufspaltung erhalten wir, in unmittelbar verständlicher Bezeichnung,

$$
\varrho \geq \left[ n \left(\sigma^ {\prime \prime}\right) + \frac {1}{2} n \left(\sigma^ {\prime}\right) - N \left(\Omega^ {\prime}\right) \right] + \left[ n \left(\sigma^ {*}\right) + \frac {1}{2} n \left(\sigma^ {\prime}\right) - N \left(\Omega^ {*}\right) \right].\tag{7}
$$

Wenn man ausdrückt, dass alle Gebiete $\Omega'$ von wenigstens zwei Querschnitten $\sigma'$ oder $\sigma''$ begrenzt werden, so findet man die Ungleichung $n(\sigma') + 2n(\sigma'') \geqq 2N(\Omega')$, d. h. der erste Klammer in (7) ist sicher nicht negativ. In gleicher Weise folgt aus der Definition der Gebiete $\Omega^{*}$, dass $n(\sigma') + 2n(\sigma^{*}) \geqq qN(\Omega^{*})$. Diese Ungleichung können wir zur Elimination von $N(\Omega^{*})$ benutzen, und erhalten aus (7)

$$
\varrho \geq \frac {q - 2}{q} \left(n (\sigma^ {*}) + \frac {1}{2} n (\sigma^ {\prime})\right) \geq \frac {q - 2}{q} n (\sigma^ {*}).\tag{8}
$$

Es gilt jetzt die Anzahl $n(\sigma^{*})$ nach unten abzuschätzen. Jeder Querschnitt $\sigma$ liegt über einer der Kurven $\gamma_{\nu}$; $\lambda(\sigma)$ bezeichne die Länge des Querschnitts dividiert durch die Länge dieser Kurve. Ferner setzen wir $\lambda^{*}=\Sigma\lambda(\sigma^{*})$, $\lambda^{\prime}=\Sigma\lambda(\sigma^{\prime})$, $\lambda^{\prime\prime}=\Sigma\lambda(\sigma^{\prime\prime})$ und endlich $\lambda_{a}$ gleich der entsprechenden Summe erstreckt über alle Querschnitte der abgesonderten Klassen ($\sigma_{n}$). Es ist zunächst $n(\sigma^{*})\geq\lambda^{*}$, denn jedes $\lambda(\sigma)$ ist höchstens gleich 1. Weiter gilt definitionsgemäss $\sum_{1}^{q}s(\gamma_{\nu})=\lambda^{*}+\lambda^{\prime}+\lambda^{\prime\prime}+\lambda_{a}$. Nach dem Überdeckungssatz ist andererseits

$\sum_{1}^{q}s(\gamma_{v}) \geqq qS - kL$ und wir erhalten aus (8)

$$
\varrho \geq (q - 2) S - k L - (\lambda^ {\prime} + \lambda^ {\prime \prime} + \lambda_ {a}).
$$

Um den Beweis zu vollenden brauchen wir nur noch zu zeigen, dass $\lambda' + \lambda'' + \lambda_a$ kleiner ist als $L$ multipliziert mit einer von $W$ unabhängigen Kon-

stante. Dieses genügt auch in dem Falle, wo die Klassen  $(\sigma_{n})$  sämtliche Querschnitte umfassen. Man schliesst nämlich dann mit Hilfe des Überdeckungssatzes, dass S selbst kleiner als eine Konstante mal L wird, und die Ungleichung (II. I) ist erfüllt für einen gewissen Wert der Konstante k.

15. Die Zuendeführung des Beweises geschieht durch eine neue Anwendung des Überdeckungssatzes. Wir betrachten als Grundflächen die von den Kurven $\gamma_{\nu}$ begrenzten Teilgebiete $\Delta'$ und $\Delta''$, und bestimmen eine feste Zahl $k$ mit folgender Eigenschaft: Wenn $\Omega$ eine beliebige Überlagerungsfläche von $\Delta'$ oder $\Delta''$ ist und $s(\gamma_{\nu})$ ihre mittlere Blätteranzahl über $\gamma_{\nu}$, so soll für jedes Kurvenpaar $\gamma_{\mu}, \gamma_{\nu}$ die Ungleichung

$$
\left| s \left(\gamma_ {\mu}\right) - s \left(\gamma_ {\nu}\right) \right| \leq \frac {q - 2}{q - 1} k L (\Omega)
$$

erfüllt sein, wobei $L(\Omega)$ die Länge des relativen Randes von $\Omega$ in Bezug auf $\mathcal{A}'$ bzw. $\mathcal{A}''$ bezeichnet.

Für Ω wählen wir eines der Gebiete Ω$_{n}$. Der entsprechende Querschnitt σ$_{n}$ liege z. B. über γ$_{1}$. Dann gilt für ν = 2, ..., q

$$
\lambda (\sigma_ {n}) \leq s (\gamma_ {1}) \leq s (\gamma_ {\nu}) + \frac {q - 2}{q - 1} k L (\Omega_ {n}).
$$

Diese Ungleichungen rechnen wir zusammen und addieren noch beiderseits $\lambda(\sigma_{n})$. Es wird dann

$$
q \lambda (\sigma_ {n}) \leq \sum_ {\Omega_ {n}} \lambda (\sigma) + (q - 2) k L (\Omega_ {n}),
$$

wo die Summe über sämtliche $\Omega_{n}$ begrenzende Querschnitte erstreckt werden soll. Wir addieren noch einmal über sämtliche Gebiete der abgesonderten Klassen $(\Omega_{1}),\ldots,(\Omega_{p})$. Auf der linken Seite erhalten wir $q\lambda_{a}$, falls die abgesonderten Querschnitte und Gebiete sich ein-eindeutig entsprechen, oder ausnahmsweise eine grössere Summe, wenn ein $\sigma_{n}$ gleichzeitig zu zwei $\Omega_{n}$ gehört. Das rechtsstehende Hauptglied gibt bei der Addition eine Summe, die höchstens gleich $2\lambda_{a}$ ist, denn jeder Querschnitt begrenzt höchstens zwei Gebiete $\Omega$. Schliesslich wird die Summe der Restglieder kleiner oder gleich $(q-2)kL$. Wir finden also die Ungleichung

$$
q \lambda_ {a} \leq 2, \lambda_ {a} + (q - 2) k L,
$$

woraus sofort $\lambda_{a} \leq kL$ folgt.

Die Grössen $\lambda'$ und $\lambda''$ sind jetzt leicht abzuschätzen. Es gibt zu jedem $\Omega'$ eine Kurve $\gamma_{\mu}$, die von keinem zu $\Omega'$ gehörigen Querschnitt $\sigma'$ oder $\sigma''$ überdeckt wird. Für diesen Index $\mu$ gilt

$$
\sum_ {\Omega^ {\prime}} \lambda (\sigma^ {\prime}) + \sum_ {\Omega^ {\prime}} \lambda (\sigma^ {\prime \prime}) \leq \sum_ {v \neq \mu} s (\gamma_ {v}) \leq (q - 1) s (\gamma_ {\mu}) + (q - 2) k L (\Omega^ {\prime}). ^ {1}
$$

Wenn wir diese Ungleichungen addieren, so erhalten wir links die Summe $\lambda' + 2\lambda''$. Rechts hat man zu beachten, dass die $s(\gamma_{\mu})$ nur von den abgesonderten Querschnitten herrühren können, und dass jeder Querschnitt $\sigma_n$ höchstens ein $\Omega'$ begrenzt. Man findet dann

$$
\lambda^ {\prime} + 2 \lambda^ {\prime \prime} \leq (q - 1) \lambda_ {a} + (q - 2) k L \leq (2 q - 3) k L.
$$

Hiermit ist der Hauptsatz bewiesen für den Fall einer schlichtartigen Grundfläche.

16. Eine nicht schlichtartige Fläche $W_0$ kann durch ein System von Rückkehrschnitten $\bar{\gamma}$ in eine schlichtartige Fläche $\overline{W}_0$ mit derselben Charakteristik $\varrho_0$ verwandelt werden. Auf der Überlagerungsfläche $W$ ziehen wir sämtliche Kurven $\bar{\sigma}$, die über den Rückkehrschnitten gelegen sind. Diese sind teils Querschnitte, teils Rückkehrschnitte auf $W$, und zerlegen die Fläche $W$ in Teilflächen $\overline{W}$, die als Überlagerungsflächen von $\overline{W}_0$ aufgefasst werden können. Es gilt nach dem Zerlegungsgesetz (4)

$$
\varrho = \sum \varrho (\bar {W}) + n (\bar {\sigma}),\tag{9}
$$

wo $n(\bar{\sigma})$ die Anzahl der unter den Kurven $\bar{\sigma}$ vorkommenden Querschnitte bezeichnet. Wenn wir bemerken, dass jedes negative $\varrho(\overline{W})$ gleich $-1$ ist, so können wir (9) auch in der Form

$$
\varrho = \sum^ {+} \varrho (\bar {W}) - N _ {1} + n (\sigma)
$$

schreiben, wobei  $N_{1}$  die Zahl der einfach zusammenhängenden Teilflächen angibt.

Nach einem grundlegenden Satz der Topologie wird eine zasammenhängende Fläche durch einen Querschnitt in höchstens zwei Teile zerlegt, und beide Teile sind einfach zusammenhängend nur wenn dieses von der ursprünglichen Fläche gilt. Wendet man diesen Satz wiederholt an, so sieht man dass in jeder Zerlegung durch lauter Querschnitte die Anzahl der Teilgebiete höchstens um Eins grösser ist als die Anzahl der Querschnitte. Wenn die gegebene Fläche mehr-

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\Omega^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\sigma^{\prime}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Die linksstehenden Summen werden über sämtliche  $\Omega'$  begrenzende  $\sigma'$  bzw.  $\sigma''$  erstreckt.</span></small>

fach zusammenhängend ist, so ist ausserdem die Anzahl der einfach zusammenhängenden Teilgebiete höchstens gleich der Anzahl der Querschnitte. Dieses Resultat wenden wir auf die obige Zerlegung an. Wenn die Zerlegung nur durch Querschnitte erfolgen würde, so hätte man, vorausgesetzt dass $\varrho \geq 0$, $N_{1} \leq n(\overline{\sigma})$. Durch Hinzufügung der Rückkehrschnitte werden keine neuen einfach zusammenhängenden Gebiete erhalten, denn jedes Teilgebiet, das von einem Rückkerschnitt $\overline{\sigma}$ begrenzt wird, besitzt ausserdem wenigstens eine andere Kontur und ist folglich mehrfach zusammenhängend. Es gilt also tatsächlich $N_{1} \leq n(\overline{\sigma})$, wenn nur $\varrho \geq 0$ ist, und wir finden

$$
{ } ^ { + } \varrho \geq \sum { } ^ { + } \varrho ( \bar { W } ) .
$$

Wenn andererseits $\varrho = -1$, so haben wir $N_{1} \leq n(\overline{\sigma}) + 1$, und es folgt dass kein $\varrho^{+}(\overline{W})$ positiv ist. Wir schliessen hieraus, dass die Ungleichung

$$
\stackrel {+} {\varrho} \geq \sum \stackrel {+} {\varrho} (\overline {{W}})
$$

in jedem Falle erfüllt ist.

Die Grössen  $\varrho(\overline{W})$  werden jetzt mit Hilfe des schon bewiesenen Teils des Hauptsatzes nach unten abgeschätzt. Wir erhalten dann nichts anderes als die Ungleichung (II. 1), denn S ist die Summe der mittleren Blätteranzahlen der Teilflächen  $\overline{W}$ , und L ist bestimmt nicht grösser als die Summe der Längen ihrer relativen Ränder.

## § 5. Die Umkehrung.

17. Die Hurwitzsche Relation für eine unverzweigte und relativ unberandete Überlagerungsfläche lautet $\varrho = N\varrho_{0}$, oder wenn wir dieselbe Gleichung metrisch-topologisch schreiben, $\varrho = S\varrho_{0}$. Man stellt sich die Frage, welche Bedingungen eine unverzweigte Überlagerungsfläche $W$ erfüllen muss, damit die Ungleichung (II. 1) durch eine entsprechende Gleichung ersetzt werden könne. Es liegt uns nicht daran, die allgemeinsten derartigen Bedingungen aufzustellen, sondern wir wollen nur einen Fall behandeln, wo die betrachtete Ungleichung sich sofort umkehren lässt.

Die Fläche W sei in einer endlich vielblättrigen, unverzweigten und relativ unberandeten Überlagerungsfläche von  $W_{0}$  enthalten, die wir mit F bezeichnen wollen und deren Blätteranzahl gleich N sei. Das Komplement von

W in Bezug auf F zerfällt in Gebiete  $W'$ , und man erhält, wenn man die Charakteristik von F einmal nach der Hurwitzschen Relation, einmal nach dem Zerlegungsgesetz (4) berechnet,

$$
N \varrho_ {0} = \varrho + \sum \varrho (W ^ {\prime}) + n (\Gamma),
$$

wo  $n(\Gamma)$  die Anzahl der Querschnitte von F bezeichnet, die der relative Rand  $\Gamma$  von W enthält.

Setzen wir  $N_{1}$  gleich der Anzahl der einfach zusammenhängenden Gebiete  $W'$ , so wird

$$
N \varrho_ {0} = \varrho + \sum^ {+} \varrho (W ^ {\prime}) - N _ {1} + n (\Gamma).
$$

Auf die Gebiete $W'$ wenden wir die Ungleichung (II. 1) an, und bemerken dass die Summe ihrer mittleren Blätteranzahlen gleich $N - S$ ist. Wir erhalten also

oder

$$
N \varrho_ {0} \geq \varrho + (N - S) \varrho_ {0} - N _ {1} + n (\Gamma) - k L
$$

$$
\varrho \leq S \varrho_ {0} + N _ {1} - n (\Gamma) + k L.
$$

Wenn der ganze Rand $\Gamma$ aus lauter Querschnitten besteht, so zerfällt $F'$ in höchstens $n(\Gamma)+1$ Teilgebiete, wovon eines mit $W$ identisch ist. In diesem Falle ist also $N_{1}\leq n(\Gamma)$. Für jeden Rückkehrschnitt kann die Anzahl $N_{1}$ höchstens um eine Einheit zunehmen. Wenn die Anzahl der zu $\Gamma$ gehörigen geschlossenen Konturen mit $\alpha$ bezeichnet wird, so erhalten wir folglich $N_{1}\leq n(\Gamma)+\alpha$, woraus

$$
\varrho \leq S \varrho_ {0} + k L + \alpha .
$$

Diese Ungleichung stellen wir mit (II. 1) zusammen, und bemerken gleichzeitig dass $\varrho \geq \stackrel{+}{\varrho} - 1$. Wir erhalten dann folgende

Metrisch-topologische Doppelungleichung. — Es sei bekannt, dass die Fläche W als Teil einer über  $W_{0}$  ausgebreiteten, relativ zu  $W_{0}$  unberandeten und unverzweigten Überlagerungsfläche aufgefasst werden kann. Wenn der relative Rand von W höchstens a geschlossene Konturen umfasst, so gilt die Doppelungleichung

$$
S \varrho_ {0} - k L - \mathrm{i} \leq \varrho \leq S \varrho_ {0} + k L + \alpha .\tag{II. 2}
$$

Ist $\varrho_{0} \geq 0$, so gilt etwas einfacher

$$
S \varrho_ {0} - k L \leq^ {+} \varrho \leq S \varrho_ {0} + k L + \alpha ,\tag{II. \(z^{\prime}\)}
$$

denn die zweite Hälfte dieser Ungleichung ist trivial für  $\varrho = -1$ .

## II. Offene Überlagerungsflächen.

18. Eine endliche Überlagerungsfläche ist Teil einer anderen oder ist in ihr enthalten, wenn es eine topologische Abbildung der ersten auf einen Teil der zweiten gibt, bei welcher entsprechende Punkte denselben Spurpunkt haben. Eine abzählbare Folge von endlichen Überlagerungsflächen W definiert eine unendliche oder offene Überlagerungsfläche  $W^{*}$ , wenn jede Fläche Teil der folgenden ist. Zwei Folgen definieren dieselbe offene Überlagerungsfläche, wenn jede Fläche der einen Folge in allen bis auf endlich vielen Flächen der anderen Folge enthalten ist und umgekehrt.

Eine Folge von endlichen Flächen, welche die offene Fläche $W^{*}$ definiert, heisst auch eine Ausschöpfung der Fläche $W^{*}$. Eine offene Fläche zu untersuchen bedeutet nichts anderes als die Eigenschaften der ausschöpfenden Folgen zu betrachten. Wenn wir die vorhergehende Theorie auf die Flächen $W$ einer solchen Folge anwenden, so kommt etwas neues heraus, nur wenn wir das asymptotische Verhalten der Restglieder in (I) und (II) kennen. Diesem Umstande trägt die Einführung des folgenden Begriffs Rechnung: Eine Ausschöpfung der offenen Fläche $W^{*}$ durch eine Folge von endlichen Flächen $W$ heisst regulär, wenn das Verhältnis zwischen der Länge des relativen Randes und der mittleren Blätteranzahl gegen Null strebt, d. h. wenn $\lim \frac{L}{S} = 0$.

In den folgenden Untersuchungen spielt die Frage nach der Existenz einer regulären Ausschöpfung eine hervorragende Rolle.

19. Wenn $\Delta$ ein beliebiges Teilgebiet von $W_{0}$ ist, so gilt nach dem Überdeckungssatz

$$
\left| S - S (\Delta) \right| \leq k L,
$$

gleichmäßig für alle Flächen $W$ einer ausschöpfenden Folge. Wir wollen die Grösse $S(\Delta)$ etwas näher untersuchen. Der über $\Delta$ gelegene Teil einer Fläche $W$ zerfällt in zusammenhängende Flächenteile $\Omega$ von zwei verschiedenen Arten. Entweder ist ein Flächenstück $\Omega$ relativ unberandet in bezug auf $\Delta$; dann wird $\Omega$ eine »Insel» genannt. Oder $\Omega$ besitzt einen relativen Rand, der dann natürlich Teil des relativen Randes von $W$ ist; in diesem Falle heisst $\Omega$ eine »Zunge». Der von einer Insel herrührende Teil von $S(\Delta)$ ist ganzzahlig und gleich der Blätteranzahl der Insel. Wir nennen diese Zahl die Multiplizität der betref-23–34686. Acta mathematica. 65. Imprimé le 8 février 1935.

fenden Insel. Rechnet man die Multiplizitäten aller Inseln zusammen, so erhält man eine Zahl $n(\Delta)$ welche angibt, wie oft $\Delta$ sozusagen vollständig überdeckt wird.

Den von den Zungen herrührenden Teil von $S(\mathcal{A})$ bezeichnen wir mit $\mu(\mathcal{A})$. Den Überdeckungssatz können wir dann in der Form der

Gleichung (A)

$$
n (\Delta) + \mu (\Delta) = S + O (L)
$$

schreiben. Die Landausche Bezeichnungsweise gibt an, dass das letzte Glied dem absoluten Betrag nach kleiner ist als $L$ multipliziert mit einer Konstante. Diese Abschätzung wird besonders bedeutungsvoll, wenn wir die Gleichung (A) auf eine regulär ausschöpfende Folge anwenden. Für eine derartige Ausschöpfung folgt z. B.

$$
\overline {{\lim}} \frac {n (\Delta)}{S} \leq 1.
$$

Wenn man das Gebiet $\Delta$ durch ein Teilgebiet ersetzt, so wird $n(\Delta)$ unverändert oder grösser. Lässt man $\Delta$ sich auf einen Punkt $a$ zusammenziehen, so wird $n(\Delta)$ schliesslich gleich der Anzahl $n(a)$ der über $a$ gelegenen inneren Punkte von $W$, vorausgesetzt dass die Verzweigungspunkte bei der Berechnung dieser Anzahl mit ihren Multiplizitäten gezählt werden. Man muss aber beachten, dass die Gleichung (A) bei diesem Grenzübergang ihre Geltung verliert, denn die Konstante $k$ kann über alle Grenzen wachsen.

20. Wir wollen jetzt die bisherige Allgemeinheit verlassen, indem wir einen besonders wichtigen Spezialfall ins Auge fassen. Die Betrachtungen sind jedoch die ganze Zeit solcher Art, dass sie ohne Mühe auch in allgemeineren Fällen durchgeführt werden können.

Als Grundfläche $W_0$ wählen wir eine geschlossene Fläche vom Geschlecht Null; es ist keine Einschränkung, wenn wir für $W_0$ z. B. eine Kugel nehmen. Weiter setzen wir voraus, dass die über $W_0$ ausgebreitete offene Überlagerungsfläche $W^*$ einfach zusammenhängend ist, d. h. es soll eine Ausschöpfung durch lauter einfach zusammenhängende Flächen $W$ geben. Auf $W_0$ betrachten wir eine Anzahl von $q \geq 2$ ausserhalb einander liegenden, einfach zusammenhängenden Gebieten $\Delta_1, \ldots, \Delta_q$. Die folgenden Untersuchungen beziehen sich auf die Überdeckung dieser Gebiete.

Ausser der oben eingeführten, gewöhnlichen Multiplizität einer Insel, die einem Gebiet  $\Delta$  entspricht, wollen wir noch eine zweite Multiplizität definieren,

die wir als einfache Multiplizität der Insel bezeichnen. Diese einfache Multiplizität soll gleich der mit umgekehrtem Vorzeichen genommenen Charakteristik der betreffenden Insel sein. Also ist die einfache Multiplizität höchstens gleich 1, sie kann aber auch Null oder negativ sein. Sie ist 1 bei jeder einfach zusammenhängenden Insel, und diesen Fall können wir als den normalen betrachten, vorausgesetzt dass wir die einfachen Multiplizitäten nur für einfach zusammenhängende Gebiete Δ bilden.

Die Summe aller einfachen Multiplizitäten, die zu den über einem Gebiet $\Delta$ gelegenen Inseln gehören, bezeichnen wir mit $p(\Delta)$. Sie ist höchstens gleich der Anzahl der Inseln, und also sicher kleiner oder gleich $n(\Delta)$. Wir bilden die Grössen $p(\Delta_v)$ für eine Fläche $W$ der $W^*$ ausschöpfenden Folge und bezeichnen die Summe $\sum_{1}^{q} p(\Delta_v)$ kurz mit $p$. Eine obere Schranke für $p$ ist durch $qS + kL$ gegeben. Es handelt sich darum, auch eine untere Abschätzung für dieselbe Summe zu finden.

Wir betrachten sämtliche über den Gebieten $\Delta_{1},\ldots,\Delta_{q}$ gelegene Flächenstücke $\Omega$, bezeichnen die Inseln mit $\Omega_{i}$ und die Zungen mit $\Omega_{z}$. Aus $W$ entfernen wir zunächst alle $\Omega_{z}$; dadurch zerfällt $W$ in lauter einfach zusammenhängende Restgebiete $W'$. Aus den Gebieten $W'$ entfernen wir jetzt noch alle Inseln $\Omega_{i}$. Dann können die übriggebliebenen Gebiete $\overline{W}$ als Überlagerungsflächen des $q$-fach zusammenhängenden Komplementärgebiets $\overline{W}_{0}$ der Gebiete $\Delta_{v}$ aufgefasst werden. Die Gebiete $\overline{W}$ sind von zwei wesentlich verschiedenen Arten: die Gebiete der ersten Art sind relativ unberandet in bezug auf $\overline{W}_{0}$, während die Gebiete der zweiten Art einen relativen Rand besitzen.$^{1}$ Die Gebiete $\overline{W}$ sind sicher mehrfach zusammenhängend, denn sie besitzen nach der Hurwitzschen Relation eine Charakteristik, die wenigstens gleich einem Vielfachen von $q-2$ ist und folglich nicht negativ sein kann.

Die Zerlegung der Gebiete $W'$ in die Teile $\Omega_i$ und $\overline{W}$ erfolgt mit Hilfe von lauter Rückkehrschnitten. Es gilt folglich $\sum \varrho(\overline{W}) + \sum \varrho(\Omega_i) = \sum \varrho(W')$, woraus $p = -\sum \varrho(\Omega_i) = \sum \varrho(\overline{W}) + N(W')$, wenn $N(W')$ die Anzahl der Gebiete $W'$ bezeichnet. Setzen wir $N_1(\overline{W})$ gleich der Anzahl der einfach zusammenhängenden $\overline{W}$, so erhalten wir noch $p = \sum \varrho^+(\overline{W}) + N(W') - N_1(\overline{W})$. Nach dem was oben gezeigt wurde, sind die einfach zusammenhängenden $\overline{W}$ von der zweiten Art und offenbar mit einem $W'$ identisch. Hieraus folgt dass

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Die Gebiete der ersten Art könnten zweckmäßig als »Binnenseen« bezeichnet werden.</span></small>

$\beta = N(W') - N_{1}(W)$  die Anzahl derjenigen unter den Gebieten  $W'$  angibt, welche wenigstens eine Insel enthalten.

Wir wenden jetzt den metrisch-topologischen Hauptsatz auf sämtliche Flächen  $\overline{W}$  an. Ihre mittlere Blätteranzahlen ergeben zusammen den Wert  $S(\overline{W}_{0})$  und die relativen Ränder haben eine Gesamtlänge  $\leq L$ . Es folgt also

$$
p = \sum^ {+} \varrho (\bar {W}) + \beta \geq (q - 2) S (\bar {W} _ {0}) + \beta - k L.
$$

Durch Heranziehung des Überdeckungssatzes können wir noch  $S(\overline{W}_{0})$  durch S ersetzen und finden dann

$$
p - \beta \geq (q - 2) S - k L.\tag{10}
$$

Die nicht-negative Anzahl  $\beta$  wollen wir in diesem Zusammenhang einfach weglassen und erhalten so die wichtige

Ungleichung (B)

$$
p = \sum_ {1} ^ {q} p (\varDelta_ {v}) \geqq (q - 2) S - k L,
$$

gültig für  $q \geq 2$ .

Wenn $q = 2$ ist, so sieht man durch eine rein topologische Betrachtung ein, dass sogar $p \geq 0$ gilt. Die eigentliche Bedeutung unserer Ungleichung fängt also erst mit $q = 3$ an.

21. Wenn man auf alle Inseln, die einem einfach zusammenhängenden Gebiet  $\Delta$  entsprechen, die Hurwitzsche Relation anwendet, so ergibt sich

$$
p (\Delta) = n (\Delta) - w (\Delta),
$$

wo $w(\mathcal{A})$ die Summe der Verzweigungsordnungen der zu den Inseln gehörigen Verzweigungspunkte bedeutet. Die Ungleichung (B) erhält die Form

$$
\sum_ {1} ^ {q} n \left(\Delta_ {v}\right) - \sum_ {1} ^ {q} w \left(\Delta_ {v}\right) \geq (q - 2) S - k L
$$

oder

$$
\sum_ {1} ^ {q} (S - n (\mathcal {A} _ {v})) + \sum_ {1} ^ {q} w (\mathcal {A} _ {v}) \leq 2 S + k L.
$$

Durch Anwendung der Gleichung (A) ergibt sich noch die besonders einfache Form

$$
\sum_ {1} ^ {q} \mu (\Delta_ {\nu}) + \sum_ {1} ^ {q} w (\Delta_ {\nu}) \leq 2 S + k L.\tag{B'}
$$

Wenn es eine reguläre Ausschöpfung existiert, so liegt es nahe folgende Begriffe einzuführen: Unter dem Defekt $\delta(\Delta)$ und dem Verzweigungsindex $\varepsilon(\Delta)$ eines Gebiets $\Delta$ verstehen wir die kleinsten Zahlen, für welche eine reguläre Ausschöpfung existiert mit

$$
\lim \frac {\mu (\Delta)}{S} = \delta (\Delta)
$$

und

$$
\lim \frac {w (\Delta)}{S} = \varepsilon (\Delta).
$$

Nach dieser Definition liegt der Defekt zwischen o und i oder fällt mit einer dieser Grenzen zusammen, und der Verzweigungsindex ist jedenfalls grösser oder gleich Null. Aus (B') folgt die

Defektrelation. — Für eine beliebige Anzahl von ausserhalb einander gelegenen, einfach zusammenhängenden Gebieten  $\Delta$  gilt

$$
\sum \delta (\Delta) + \sum \varepsilon (\Delta) \leq 2,
$$

d. h. die Summe sämtlicher Defekte und Verzweigungsindizes ist höchstens gleich 2.

Wir erinnern daran, dass der ganze Defektbegriff und folglich auch die Gültigkeit der Defektrelation wesentlich auf der Annahme beruht, dass eine reguläre Ausschöpfung existiert.

Schliesslich wollen wir noch diejenige Ungleichung aufstellen, die aus (B) entsteht, wenn sämtliche Gebiete $\Delta_{v}$ sich auf Punkte reduzieren. Wir betrachten $q$ Punkte $a_{1},\ldots,a_{q}$ und wählen die Gebiete $\Delta_{v}$ so, dass sie je einen Punkt $a_{v}$ enthalten. Es sei $p(a_{v})$ die mit einfachen Multiplizitäten gezählte Anzahl der über $a_{v}$ gelegenen inneren Punkte von $W$. Dann ist offenbar $p(a_{v})\geqq p(\Delta_{v})$ und wir finden

$$
\sum_ {1} ^ {q} p (a _ {\nu}) \geqq (q - 2) S - k L.\tag{\((\mathbf{B}_1)\}
$$

22. Wir werden jetzt zeigen dass es möglich ist, aus der Ungleichung (B) eine notwendige Bedingung für die Existenz einer regulären Ausschöpfung abzulesen.

Wir betrachten die Gebiete $\Delta_{1},\ldots,\Delta_{q}$ und nehmen an, es gehöre zu jedem Gebiet $\Delta_{i}$ eine ganze positive Zahl $\mu_{i}$ mit folgender Eigenschaft: Für eine beliebige Fläche $W$ der ausschöpfenden Folge ist die gewöhnliche Multiplizität von jeder Insel, die über dem Gebiet $\Delta_{i}$ liegt, wenigstens $\mu_{i}$-mal so gross wie die einfache Multiplizität der Insel. Wenn die Insel mehrfach zusammenhängend ist, so ist die Bedingung immer erfüllt. Für eine einfach zusammenhängende Insel besagt sie, dass die Insel wenigstens $\mu_{i}$-blättrig sein soll.

Unter dieser Voraussetzung gilt für jedes Gebiet $\Delta_{i}$ die Ungleichung $S(\Delta_{i}) \geq n(\Delta_{i}) \geq \mu_{i} p(\Delta_{i})$, woraus folgt $p(\Delta_{i}) \leq \frac{1}{\mu_{i}} S + kL$. Wenn wir dieses in (B) einsetzen, so wird

$$
\left(q - 2 - \sum_ {1} ^ {q} \frac {\mathrm{I}}{\mu_ {i}}\right) S \leq k L
$$

mit einem neuen Wert von k. Wenn nun der linksstehende Koeffizient positiv ist, so können wir schliessen, dass bei jeder Ausschöpfung S kleiner als L multipliziert mit einer festen Konstante bleibt. Das heisst aber nichts anderes als dass es keine reguläre Ausschöpfung gibt.

Die Fläche $W^{*}$ sei so beschaffen, dass jede über dem Gebiet $\Delta_{i}$ gelegene, einfach zusammenhängende Insel wenigstens $\mu_{i}$-blättrig ist, wobei die Zahlen $\mu_{i}$ der Bedingung

$$
\sum_ {1} ^ {q} \left(\mathrm{I} - \frac {\mathrm{I}}{\mu_ {i}}\right) > 2\tag{II}
$$

genügen. Dann gibt es keine reguläre Ausschöpfung von $W^{*}$.

Es gibt fünf verschiedene Systeme von möglichst kleinen Zahlen $\mu_{i}$, die der Ungleichung (II) genügen. Sie sind folgende: $(2, 2, 2, 2, 2)$, $(2, 2, 2, 3)$, $(2, 3, 7)$, $(2, 4, 5)$ und $(3, 3, 4)$. In den drei letzten Fällen ist derjenige Sonderfall enthalten, wo es drei Gebiete $\Delta_{1}, \Delta_{2}, \Delta_{3}$ gibt, über denen gar keine Inseln liegen.

Der soeben bewiesene Satz bleibt wie die Ungleichung (B) gültig, wenn man die Gebiete  $\Delta_{i}$  durch Punkte  $a_{i}$  ersetzt. Wir formulieren nur das folgende, besonders anschauliche Resultat: Eine über die Kugel ausgebreitete, einfach zu-

sammenhängende Fläche, welche drei Punkte nicht überdeckt, gestattet keine reguläre Ausschöpfung.

In diesem Zusammenhang wollen wir noch ein ähnliches Resultat erwähnen, das unmittelbar aus der Ungleichung (II, I) folgt. Eine offene, einfach zusammenhängende Fläche $W^{*}$ sei über eine geschlossene Fläche vom Geschlecht grösser als Eins, d. h. mit positiver Charakteristik $\varrho_{0}$, ausgebreitet. Dann gilt für jede Fläche einer ausschöpfenden Folge $\varrho_{0}S \leq kL$, woraus man schliesst, dass keine reguläre Ausschöpfung existiert.

Eine einfach zusammenhängende Fläche, die über eine geschlossene Grundfläche vom Geschlecht grösser als Eins ausgebreitet ist, kann nicht regulär ausgeschöpft werden.

23. Wir betrachten jetzt eine besonders einfache Art von offenen Flächen $W^{*}$, die wir als unverzweigt und relativ unbegrenzt über $\overline{W}_{0}$ bezeichnen.$^{1}$ Dieselbe Eigenschaft wird ausgedrückt, wenn wir die Fläche $\overline{W}_{0}$ durch $q$ Querschnitte $\gamma$ in zwei einfach zusammenhängende Teilgebiete $\Delta'$ und $\Delta''$ zerlegen, und dann verlangen, dass $W^{*}$ aus lauter einblättrigen Inseln über $\Delta'$ und $\Delta''$ bestehen soll.

Um diese Bedingung klarzumachen, definieren wir einen Punkt auf $W^*$ als den Inbegriff aller Punkte der ausschöpfenden Flächen $W$, die sich bei der topologischen Abbildung einer Fläche auf ein Teilgebiet der Folgenden entsprechen. Alsdann wird gefordert, dass jeder Punkt, dessen Spur im Innern von $\overline{W}_0$ liegt, schliesslich — d. h. auf einer genügend umfassenden Fläche $W$ — zu einer Insel über $\Delta'$ oder $\Delta''$ gehört, eventuell als Randpunkt derselben, und dass diese Insel einblättrig ist.

Wenn diese Bedingung erfüllt ist, so können wir jedes über  $\overline{W}_{0}$  gelegene Teilgebiet  $\overline{W}$  von  $W^{*}$  in eine endliche, unverzweigte und relativ unberandete Überlagerungsfläche F von  $\overline{W}_{0}$  einschliessen. Eine solche Fläche F wird konstruiert, indem man zunächst so viele Inseln auf  $W^{*}$  auswählt, dass sie zusammen das Gebiet  $\overline{W}$  enthalten, und die aus ihnen gebildete Fläche durch symmetrische Wiederholung abschliesst. $^{2}$

Wir nehmen eine Fläche W der ausschöpfenden Folge und betrachten wie

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\overline{W}_{0}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{2}$  Um diesen bekannten Prozess genau zu erklären müsste man eigentlich den Begriff des topologischen Baums einführen. Wir verweisen den Leser auf die eingehende Behandlung dieser Frage in der neulich erschienenen Arbeit G. ELFVING: Über eine Klasse von Riemannschen Flächen und ihre Uniformisierung (Acta Soc. Scient. Fenn., Nov. Ser. A. t. II No. 3.).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$$\overline{W}_{0}$  ist das Komplementärgebiet der Gebiete  $\Delta\nu$ .</span></small>

in Nr. 20 ihre über $\overline{W}_{0}$ gelegenen Teile $\overline{W}$. Es gilt wie damals $p = \sum_{\varrho}^{+} (\overline{W}) + \beta$, und die $\varrho^{+}(\overline{W})$ können mit Hilfe von (II, $2'$) nach oben abgeschätzt werden. Unter den relativen Rändern der Flächen $\overline{W}$ kommt höchstens eine geschlossene Kontur vor (wegen des einfachen Zusammenhangs von $W$), und wir erhalten folglich

$$
p - \beta \leq (q - 2) S + k L + 1.
$$

Wird diese Ungleichung mit (10) verbunden, so folgt:

Wenn die einfach zusammenhängende, offene Fläche $W^{*}$ ausserhalb der Gebiete $\Delta_{1},\ldots,\Delta_{q}$ ($q\geq2$) unverzweigt und unbegrenzt ist, so gilt

$$
\left| p - \beta - (q - 2) S \right| \leq k L + \mathrm{I}.\tag{C}
$$

Wenn man den Beweis durchgeht, so sieht man dass der Satz seine Richtigkeit behält, wenn die Gebiete $\Delta_{v}$ sich auf Punkte $a_{v}$ reduzieren. In diesem Falle ist $\beta \leq 1$, und man findet:

Wenn sämtliche Verzweigungs- und Grenzpunkte über den endlich vielen Punkten  $a_{1}, \ldots, a_{q} (q \geq 2)$  liegen, so gilt die Beziehung

$$
\left| \sum_ {1} ^ {q} p (a _ {v}) - (q - 2) S \right| \leq k L + 2.\tag{C'}
$$

Ist $a$ ein von allen $a_{v}$ verschiedener Wert, so können wir $(\mathbf{C}^{\prime})$ auf die Werte $a_{1},\ldots ,a_{q}$ und $a$ anwenden. Es folgt

$$
\left| n (a) + \sum_ {1} ^ {q} p (a _ {v}) - (q - 1) S \right| \leq k L + 2,
$$

und wenn man diese Ungleichung mit (C') vergleicht

$$
\left| n (a) - S \right| \leq 2 k L + 4.
$$

Die Überdeckung der a-Stellen ist also möglichst regelmässig.

## III. Die Abbildung einer offenen Fläche.

24. Eine offene, einfach zusammenhänge Fläche  $W^{*}$  kann topologisch auf die komplexe z-Ebene abgebildet werden, wobei die ausschöpfenden Flächen W

in eine Folge von Gebieten G übergehen, welche schliesslich jeden endlichen Punkt der Ebene enthalten. Umgekehrt erhält man aus jeder Ausschöpfung der Ebene durch einfach zusammenhängende Gebiete G eine entsprechende Ausschöpfung der Fläche  $W^{*}$ .

Es gebe eine Abbildung, bei welcher die Metrik der Fläche  $W^{*}$  durch eine positiv definite Differentialform

$$
d s ^ {2} = E (z) d x ^ {2} + 2 F (z) d x d y + G (z) d y ^ {2} \quad (z = x + i y)
$$

bestimmt wird, d. h. die Länge einer Kurve und der Inhalt eines Gebiets auf $W^{*}$ sollen durch die Integrale $\int\sqrt{E dx^{2}+2 F dx dy+G dy^{2}}$ und $\iint\sqrt{EG-F^{2}} dx dy$, erstreckt über die Bildkurve bzw. das Bildgebiet in der $z$-Ebene, gegeben sein. Es wird vorausgesetzt, dass die Koeffizienten $E$, $F$ und $G$ gewissen Regularitätsbedingungen genügen; sie seien z. B. stückweise analytische Funktionen der Argumente $x$ und $y$.

Die Abbildung heisst quasikonform, wenn es eine Konstante K gibt, sodass die Ungleichung

$$
E + G \leq 2 K V E G - F ^ {2}\tag{12}
$$

in jedem Punkte z erfüllt ist. Es ist notwendigerweise  $K \geq 1$ , und K = 1 bedingt F = 0, E = G. Die Abbildung ist in diesem Falle konform.

Es sei  $W_{r}$  diejenige endliche Fläche, welche dem Kreis  $G_{r}$  ( $|z| \leq r$ ) entspricht,  $I(r)$  ihr Inhalt und  $L(r)$  die Länge ihrer Randkurve. Nach Voraussetzung ist

$$
L (r) = \int_ {| z | = r} V E d y ^ {2} + 2 F d x d y + G d y ^ {2}
$$

und

$$
I (r) = \iint_ {| z | \leq r} \sqrt {E G - F ^ {2}} d x d y.
$$

Aus der letzten Gleichung folgt durch Differentiation

$$
I ^ {\prime} (r) = \int_ {| z | = r} \sqrt {E G - F ^ {2}} | d z |.
$$

24-34686. Acta mathematica. 65. Imprimé le 8 février 1935.

Unter Anwendung der Schwarzschen Ungleichung erhält man die Abschätzung

$$
L (r) ^ {2} \leq 2 \pi r \int_ {| z | = r} \frac {E d x ^ {2} + 2 F d x d y + G d y ^ {2}}{d x ^ {2} + d y ^ {2}} | d z |.\tag{13}
$$

Durch eine wohlbekannte Rechnung kann man bestätigen, dass die Ungleichung

$$
\frac {E d x ^ {2} + 2 F d x d y + G d y ^ {2}}{d x ^ {2} + d y ^ {2}} \leqslant \frac {1}{2} \left(E + G + \sqrt {(E + G) ^ {2} - 4 (E G - F ^ {2})}\right)
$$

für jeden Wert des Verhältnisses $\frac{dy}{dx}$ erfüllt ist. Der rechtsstehende Ausdruck ist nach (12) höchstens gleich $(K + \sqrt{K^2 - 1})\sqrt{EG - F^2} < 2K\sqrt{EG - F^2}$. Diese Schranke in (13) eingesetzt gibt

$$
L (r) ^ {2} <   4 \pi K r I ^ {\prime} (r)
$$

oder, als Differentialungleichung geschrieben,

$$
\frac {d r}{r} <   4 \pi K \frac {d I (r)}{L (r) ^ {2}}.\tag{14}
$$

Diese Ungleichung $^{1}$ enthält eine möglichst scharfe Aussage über das gegenseitige Verhalten der Funktionen $I(r)$ und $L(r)$. Durch Integration können verschiedene Folgerungen gezogen werden.

$^{1}$  Die Integration zwischen den Grenzen  $r_{0}$  und r ergibt

$$
\log \frac {r}{r _ {0}} <   4 \pi K \int_ {r _ {0}} ^ {r} \frac {d I (r)}{L (r) ^ {2}}.
$$

Lässt man r gegen Unendlich wachsen, so schliesst man, dass das Integral

$$
\int^ {\infty} \frac {d I (r)}{L (r) ^ {2}}\tag{15}
$$

divergieren muss.

$2^{\circ}$ Es sei $\Phi(t)$ eine Funktion, für welche das Integral $\int_{0}^{\infty}\frac{dt}{\Phi(t)}$ konvergiert.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Im Falle einer konformen Abbildung erhält man die Ungleichung</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\frac{dr}{r} \leq 2\pi \frac{dI(r)}{L(r)^2},$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">dessen Beweis sich noch einfacher als der obige gestaltet.</span></small>

Die Ungleichung $L(r) \geq \sqrt{\Phi(I(r))}$ möge innerhalb einer gewissen Intervallfolge $\delta_r$ erfüllt sein. Durch Integration von (14) über diese Intervallfolge erhält man

$$
\int_ {\delta_ {r}} d \log r <   4 \pi K \int_ {\delta_ {r}} \frac {d I (r)}{\Phi (I (r))} <   4 \pi K \int^ {\infty} \frac {d t}{\Phi (t)} <   \infty ,
$$

d. h. es gilt $L(r) < \sqrt{\Phi(I(r))}$ ausser für die Werte einer Intervallfolge von endlicher logarithmischer Gesamtlänge. Am einfachsten wählt man $\Phi(t) = t^{1+2\varepsilon}$ und erhält $L(r) < I(r)^{\frac{1}{2} + \varepsilon}$ ausserhalb der Ausnahmeintervalle.

$3^{\circ}$ Die Differentialungleichung (14) gilt unverändert, wenn die Abbildung nicht auf die ganze Ebene sondern auf einen endlichen Kreis $|z| < R$ geschieht. Es gelte eine Ungleichung der Form $I(r) \leq kL(r)$ in einem Intervall $r_0 < r < R$. Man berechnet dann

$$
\log \frac {R}{r} <   4 \pi k ^ {2} K \int_ {r} ^ {R} \frac {d I (r)}{I (r) ^ {2}} \leqslant \frac {4 \pi k ^ {2} K}{I (r)}
$$

oder

$$
I (r) <   \frac {4 \pi k ^ {2} K}{\log \frac {R}{r}} <   \frac {4 \pi k ^ {2} K R}{R - r}.
$$

Man findet also die Abschätzung $I(r) = O\left(\frac{1}{R - r}\right)$.

25. Der Zusammenhang dieser Ergebnisse mit der Frage nach der regulären Ausschöpfbarkeit der Fläche  $W^{*}$  wird unmittelbar klar, wenn man bedenkt, dass die mittlere Blätteranzahl von  $W_{r}$  einfach durch Multiplikation des Inhalts  $I(r)$  mit einer Konstante erhalten wird. Dann folgt als einfaches Korollar zu dem soeben Bewiesenen der folgende

Abbildungssatz. — Wenn es eine konforme oder quasikonforme Abbildung der Fläche  $W^{*}$  auf die ganze Ebene gibt, dann gibt es auch eine reguläre Ausschöpfung von  $W^{*}$ .

Allgemeiner gibt es sogar eine Ausschöpfung, bei welcher $L < V\Phi(S)$ gilt, vorausgesetzt dass das Integral $\int_{0}^{\infty}\frac{dt}{\Phi(t)}$ konvergiert.

Die Existenz einer regulären Ausschöpfung ist dargelegt auch wenn man weiss, dass die Fläche $W^{*}$ auf einen endlichen Kreis $|z| < R$ konform oder quasikonform abgebildet werden kann, und dass dabei $\lim (R - r) I(r) = \infty$ gilt.

Mit Hilfe dieses Satzes können die Resultate des vorigen Abschnitts unmittelbar für die Abbildungstheorie verwertet werden.

Wir wollen noch einige Worte über den Zusammenhang der obigen Ergebnisse mit dem sog. Typenproblem hinzufügen. Man weiss, dass eine offene, einfach zusammenhängende Riemannsche Fläche $W^{*}$ konform entweder auf die ganze im Unendlichen punktierte Ebene oder auf einen endlichen Kreis abgebildet werden kann. Das Typenproblem besteht in der Aufstellung von Bedingungen für das Eintreten des einen oder des anderen Falles, wobei es zu bemerken ist, dass man bei der Formulierung dieser Bedingungen nur von den inneren Eigenschaften der Fläche $W^{*}$ Gebrauch machen darf, dagegen nicht von solchen Eigenschaften, die erst durch die Abbildung bestimmt sind.

Der Abbildungssatz zeigt, dass ein Zusammenhang zwischen dem Typenproblem und den isoperimetrischen Eigenschaften einer Riemannschen Fläche existiert. Wir verstehen allgemein unter einer isoperimetrischen Eigenschaft eine Ungleichung der Form  $L \geq P(I)$ , welche für jedes einfach zusammenhängende Teilgebiet der Fläche erfüllt ist, wenn L die Länge seines relativen Randes und I seinen Inhalt bezeichnen. Aus dem Abbildungssatz wird folgendes Kriterium erhalten:

Auf der Fläche $W^{*}$ gelte die isoperimetrische Ungleichung $L > P(I)$, wobei $P(I)$ eine Funktion sein soll, für welche das Integral $\int_{0}^{\infty} \frac{dt}{P(t)^2}$ konvergiert. Es ist dann unmöglich, die Fläche $W^{*}$ konform auf die ganze endliche Ebene abzubilden.

## IV. Anwendung auf die Theorie der meromorphen Funktionen.

26. In diesem Abschnitt werden wir alles zusammenstellen, was unsere Theorie für die meromorphen Funktionen liefert. Erst dadurch erhalten die vorigen Ergebnisse ihren richtigen Hintergrund, denn so wie die reine Topologie ursprünglich geschaffen wurde, um der Theorie der analytischen Funktionen zu dienen, so sind auch unsere metrisch-topologischen Betrachtungen aus dem Wunsche entstanden, die Wertverteilungstheorie auf neuer Grundlage aufzubauen.

Die Funktion $w = f(z)$ sei meromorph für $|z| < R$, wobei $R$ endlich oder unendlich sein kann. Durch Vermittlung von $f(z)$, verbunden mit einer stereographischen Projektion, wird der Kreis $|z| \leq r < R$ auf eine endliche Über-

lagerungsfläche $W_r$ der Riemannschen Kugel konform abgebildet.$^1$ Als Grundfläche $W_0$ betrachten wir also die Kugel vom Durchmesser 1, welche die $w$-Ebene im Ursprung berührt; die Metrik der Grundfläche ist die natürliche Metrik der Kugel. Lässt man $r$ eine gegen $R$ strebende Wertfolge durchlaufen, so definieren die Flächen $W_r$ eine offene Fläche $W$, die dem ganzen Kreis $|z| < R$ entspricht.

Die mittlere Blätteranzahl der Fläche  $W_{r}$  lässt sich unmittelbar berechnen. Man erhält für sie die explizite Darstellung

$$
S (r) = \frac {1}{\pi} \int_ {0} ^ {r} \int_ {0} ^ {2 \pi} \frac {\left| f ^ {\prime} (z) \right| ^ {2}}{\left(1 + \left| f (z) \right| ^ {2}\right) ^ {2}} r d r d \varphi ,
$$

und für die Länge der Randkurve entsprechend

$$
L (r) = \int_ {0} ^ {2 \pi} \frac {\left| f ^ {\prime} (z) \right|}{1 + \left| f (z) \right| ^ {2}} r d \varphi .
$$

Wählen wir jetzt auf der Riemannschen Kugel ein beliebiges Gebiet $\Delta$, so können wir die Gleichung (A) aufstellen und in der Form

$$
n (r, \Delta) + \mu (r, \Delta) = S (r) + O (L (r))\tag{a}
$$

schreiben, wo die Bezeichnung kaum eine Erklärung benötigt. Für das Restglied verfügt man über alle Abschätzungen, die in Nr. 24 erhalten wurden.

Ebenso erhalten wir für ein System von $q$ ausserhalb einander gelegenen, einfach zusammenhängenden Gebieten $\Delta_{1},\ldots,\Delta_{q}$ aus (B) die Ungleichung

$$
p (r) = \sum_ {1} ^ {q} p (r, \Delta_ {v}) \geqslant (q - 2) S (r) - k L (r),\tag{b}
$$

und aus  $(\mathrm{B}_{1})$  die entsprechende Ungleichung

$$
\sum_ {1} ^ {q} p (r, a _ {v}) \geq (q - 2) S (r) - k L (r).\tag{b1}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$W_{r}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$W_{r}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$|z| < r$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$|z| = r$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Um  $W_{r}$  als Überlagerungsfläche der Kugel zu erkennen, müssen wir eine Dreiecksteilung der beiden Flächen angeben, bei welcher jedem Dreieck auf  $W_{r}$  ein bestimmtes Spurdreieck entspricht. Wir ziehen auf der Kugel die Bildkurve des Kreises  $|z| = r$ . Diese Kurve zerlegt die Kugel in endlich viele Gebiete; wenn man diese Gebiete in Dreiecke teilt und dafür sorgt, dass die für  $|z| < r$  mehrfach angenommenen Werte unter den Eckpunkten vorkommen, so erhält man eine Dreiecksteilung der verlangten Art.</span></small>

Wir betrachten schliesslich den Fall, wo die Funktion $f(z)$ keinen ausserhalb der Gebiete $\Delta_{v}$ gelegenen Wert mehrfach annimmt und auch nicht als asymptotischen Wert besitzt. Dann sieht man leicht, dass die entsprechende Riemannsche Fläche $W^{*}$ unverzweigt und unbegrenzt über das Komplementargebiet der Gebiete $\Delta_{v}$ ist. Wir können also die Ungleichung (C) anwenden und erhalten

$$
p (r) - \beta (r) = (q - 2) S (r) + O (L (r) + 1).\tag{c}
$$

Wenn alle mehrfach angenommenen und asymptotischen Werte zu den endlich vielen Werten $a_{1},\ldots,a_{q}$ gehören, so gilt nach $(C^{\prime})$

$$
\sum_ {1} ^ {q} p (a _ {v}) = (q - 2) S (r) + O (L (r) + 1).\tag{c'}
$$

Diese Beziehung ist vollständig neu und zeigt das ausserordentlich reguläre Verhalten der Funktionen der betrachteten Funktionsklasse.

27. Aus der in Nr. 22 aufgestellten Bedingung für die Nicht-Existenz einer regulären Ausschöpfung folgt unmittelbar der sogenannte

Scheibensatz. $^{1}$  — Wenn alle über den Gebieten  $\Delta_{i}$  ( $i=1,\ldots,q$ ) gelegenen, einfach zusammenhängenden Inseln der Fläche  $W^{*}$  wenigstens  $\mu_{i}$ -blättrig sind, und wenn die Zahlen  $\mu_{i}$  der Bedingung

$$
\sum_ {1} ^ {q} \left(\mathrm{I} - \frac {\mathrm{I}}{\mu_ {i}}\right) > 2
$$

genügen, so ist notwendig $R < \infty$ und es gilt sogar $S(r) = O\left(\frac{1}{R - r}\right)$.

In diesem Resultat sind sämtliche bisher bekannten Sätze enthalten, die aus den inneren Eigenschaften einer Riemannschen Fläche auf die Unmöglichkeit einer konformen Abbildung auf die ganze Ebene zu schliessen gestatten.

Es lohnt sich einige Spezialfälle des Scheibensatzes besonders hervorzuheben. Der erste Fall ist eine direkte Verallgemeinerung des Picardschen Satzes, und wurde von uns früher mit Hilfe einer anderen Methode bewiesen $^{2}$ :

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Die Bezeichnung »Scheibensatz« verdanke ich Herrn E. ULLRICH.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{2}$  Sur les domaines dans lesquels une fonction méromorphe prend des valeurs appartenant à une région donnée, Acta Soc. Scient. Fenn., Nov. Ser. A, t. II, No. 2, Helsingfors (1933).</span></small>

Auf der Riemannschen Kugel seien drei ausserhalb einander gelegene, einfach zusammenhängende Gebiete gegeben. Wenn die Riemannsche Fläche $W^{*}$ zu einer in der ganzen Ebene meromorphen Funktion gehört, so enthält sie eine Insel, die über einem der drei Gebiete liegt.

Ein zweiter Fall, wo die Bedeutung des Scheibensatzes auch sehr anschaulich ist, ist der folgende:

Wenn fünf ausserhalb einander liegende, einfach zusammenhängende Gebiete gegeben sind, so enthält die zu einer in der ganzen Ebene meromorphen Funktion gehörige Riemannsche Fläche eine einblättrige Insel, die über einem dieser Gebiete liegt.

Ist die Funktion ganz, so gilt derselbe Satz schon für drei im Endlichen gelegene Gebiete. Hieraus folgt z. B. der VALIRONSche Satz, dass die über die Ebene ausgebreitete Fläche einer ganzen Funktion beliebig grosse schlichte Kreise enthält.

28. Verwandt mit dem Scheibensatz ist ein klassischer Satz, der auf PICARD zurückgeht. Es sei $\Phi(u,v)=\circ$ eine algebraische Gleichung und $W_{0}$ die über die $u$-Kugel ausgebreitete Riemannsche Fläche, auf welcher die Funktion $v=v(u)$ eindeutig wird. Wenn die Charakteristik der Fläche $W_{0}$ positiv ist, d. h. wenn das Geschlecht der Fläche grösser als Eins ist, so behaupten wir, dass zwei in der ganzen Ebene meromorphe Funktionen $f(z)$ und $g(z)$ die Relation $\Phi(f(z), g(z))=\circ$ nicht identisch befriedigen können.

Es sei $W^*$ die über die $u$-Kugel ausgebreitete offene Fläche, auf welche die $z$-Ebene durch Vermittlung der Funktion $u = f(z)$ abgebildet wird. Zu jedem Punkte $P$ auf der Fläche $W^*$ gehört ein bestimmter Bildpunkt $z$ in der $z$-Ebene. Wenn nun die Gleichung $\Phi(f(z), g(z)) = 0$ identisch erfüllt ist, so wird durch diesen Bildpunkt nicht nur ein Wertpaar $u = f(z), v = g(z)$ mit $\Phi(u, v) = 0$, sondern auch der zugehörige Zweig der algebraischen Funktion $v(u)$ eindeutig festgelegt. Der Punkt $P$ hat mit anderen Worten auf $W_0$ einen wohlbestimmten Spurpunkt $P_0$, der über demselben Punkt der $u$-Kugel liegt wie $P$. Ferner sieht man, dass der Punkt $P_0$ sich stetig mit $P$ ändert. Hieraus folgt, dass die Fläche $W^*$ als Überlagerungsfläche von $W_0$ betrachtet werden kann. Auch die Metriken der beiden Flächen entsprechen sich in der richtigen Weise, vorausgesetzt dass man beide mit Hilfe der Kugelmetrik definiert.

Wir sind hierdurch zu einem Widerspruch geführt, denn einerseits haben

wir bewiesen, dass eine einfach zusammenhängende Überlagerungsfläche einer geschlossenen Fläche vom Geschlecht grösser als Eins nicht regulär ausgeschöpft werden kann, und andererseits wissen wir, dass eine reguläre Ausschöpfung von $W^{*}$ existiert. Wir haben also gefunden:

Zwei in der ganzen Ebene meromorphe Funktionen können keine algebraische Gleichung vom Geschlecht grösser als Eins erfüllen. Dasselbe gilt von zwei in einem endlichen Kreis meromorphen Funktionen, wenn die eine Funktion der Bedingung  $\lim S(r)(R-r)=\infty$  genügt.

28. Es ist angebracht, dass wir zum Schluss einen Vergleich zwischen der hier entwickelten Theorie und der NEVANLINNASchen Wertverteilungstheorie anstellen.

Man betrachtet in dieser Theorie die logarithmisch integrierten Anzahlfunktionen

$$
N (r, a) = \int_ {0} ^ {r} n (r, a) \frac {d r}{r}, ^ {1}
$$

die Schmiegungsfunktionen

$$
m (r, a) = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} \log^ {+} \frac {1}{| f (z) - a |} d \varphi
$$

$$
(a \neq \infty)
$$

bzw.

$$
m (r, \infty) = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} \log^ {+} | f (z) | d \varphi ,
$$

und schliesslich die charakteristische Funktion

$$
T (r) = N (r, \infty) + m (r, \infty).
$$

Der erste Hauptsatz von NEVANLINNA wird aus der JENSENSchen Formel gewonnen und lautet

$$
N (r, a) + m (r, a) = T (r) + h (r, a),\tag{16}
$$

wo das Restglied  $h(r, a)$  der Bedingung

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$a = f(0)$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Für  $a = f(o)$  wird diese Definition in bekannter Weise abgeändert.</span></small>

Zur Theorie der Überlagerungsflächen.

$$
\left| h (r, a) \right| \leq \left| \log \left| f (0) - a \right| \right| + \log^ {+} a + \log 2
$$

genügt.

Wir betrachten in (16) $a$ als Veränderliche und integrieren über die ganze Riemannsche Kugel. Sowohl $m(r, a)$ als $h(r, a)$ ergeben bei der Integration beschränkte Restglieder. Bei der Integration von $N(r, a)$ kann man die Reihenfolge der Integrationen vertauschen, und kommt so zu der von SHIMIZU herrührenden Beziehung

$$
T (r) = \int_ {0} ^ {r} S (r) \frac {d r}{r} + O (\mathrm{I}),
$$

wo  $S(r)$  dieselbe Bedeutung wie vorhin hat.

Integriert man statt über die ganze Kugel nur über ein Teilgebiet $A$, so erhält man in ganz derselben Weise

$$
T (r) = \int_ {0} ^ {r} S (r, \Delta) \frac {d r}{r} + O (\mathrm{I}).
$$

Setzt man nun

$$
S (r) - S (r, \Delta) = x (r),
$$

so ergibt sich durch Vergleich.

$$
\int_ {0} ^ {r} \varkappa (r) \frac {d r}{r} = O (\mathrm{I}),
$$

während wir früher die Relation

$$
\left| x (r) \right| \leq k L (r)
$$

bewiesen haben. Diese beiden Resultate, das aus der NEVANLINNASchen Theorie gewonnene und das aus unseren Betrachtungen hervorgehende, komplettieren sich, indem das eine nicht aus dem anderen hergeleitet werden kann. Wenn man auf $L(r)$ die auf S. 187 gefundene Abschätzung anwendet, so folgt aus der letzten Ungleichung

$$
\left| \varkappa (r) \right| <   S (r) ^ {\frac {1}{2} + \varepsilon}
$$

ausserhalb der Ausnahmeintervalle, eine Abschätzung, die gleichfalls keine Folge des ersten Hauptsatzes ist.

25-34686. Acta mathematica. 65. Imprimé le 9 février 1935.

Ganz ähnlich steht es mit dem zweiten Hauptsatz von NEVANLINNA. Nach diesem Satze gilt die Ungleichung

$$
\sum_ {1} ^ {q} N (r, a _ {v}) - N _ {1} (r) \geq (q - 2) T (r) - O (\log r + \log T (r)),\tag{17}
$$

wo  $N_{1}(r)$  die aus den mehrfachen Stellen herrührende Anzahlfunktion bedeutet, ausser wenn r zu gewissen Ausnahmeintervallen gehört. Etwas ungenauer ist die Formulierung

$$
\sum_ {1} ^ {q} \overline {{{N}}} (r, a _ {v}) \geqslant (q - 2) T (r) - O (\log r + \log T (r)),\tag{17'}
$$

in welcher  $\overline{N}(r, a_{v})$  diejenige Anzahlfunktion bezeichnet, die man erhält, wenn man die  $a_{v}$ -Stellen mit einfacher Multiplizität zählt. Es gilt mit anderen Worten

$$
\overline {{{N}}} (r, a _ {v}) = \int_ {0} ^ {r} p (r, a) \frac {d r}{r},
$$

woraus folgt dass (17') nur eine integrierte Form von (b₁) (S. 189) darstellt.

Wenn wir

$$
\sum_ {1} ^ {q} p (r, a _ {v}) = (q - 2) S (r) - \lambda (r)
$$

schreiben, so gilt nach NEVANLINNA

$$
\int_ {0} ^ {r} \lambda (r) \frac {d r}{r} <   O (\log r + \log T (r)),
$$

und nach unserer Theorie

$$
\lambda (r) \leq k L (r) <   S (r) ^ {\frac {1}{2} + \varepsilon},
$$

alles mit gewissen Ausnahmeintervallen. Zufolge der Mittelbildung ist die NE-VANLINNASche Abschätzung schärfer, aber sie gibt andererseits keine Auskunft über das unintegrierte Restglied $\lambda(r)$.

Das Ergebnis unseres Vergleichs ist also, dass die hier entwickelte, auf geometrischer Grundlage fussende Theorie zwar nicht die originalen Formeln von NEVANLINNA liefert, aber anstelle dieselben in wichtiger Weise komplettiert.