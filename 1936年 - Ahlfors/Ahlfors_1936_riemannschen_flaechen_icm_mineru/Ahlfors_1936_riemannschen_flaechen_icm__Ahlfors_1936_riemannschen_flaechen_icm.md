# GEOMETRIE DER RIEMANNSCHEN FLÄCHEN

Von Lars V. Ahlfors, Helsingfors.

1. Riemanns einfache Idee, mehrfach bedeckte Gebiete der komplexen Ebene als Existenz- und Wertbereiche von Funktionen zu betrachten, gehört zu den genialsten Kunstgriffen der gesamten Mathematik. Mit einem kühnen Gedankenzug werden alle Schwierigkeiten bei der Theorie der mehrdeutigen und impliziten Funktionen eliminiert und eine ein-eindeutige Abbildung hergestellt. In Einfachheit ist Riemanns Methode dem Verfahren von Weierstrafs weit überlegen, aber leider hat Riemann die Schwierigkeiten bei der Präzisierung seines grundlegenden Begriffs des „mehrfach bedeckten Gebiets“ nicht recht eingeschätzt, und darin liegt wohl der Grund zu der vorherrschenden Stellung der Weierstrafs'schen Funktionentheorie bis zur allerneusten Zeit.

Versucht man den Riemannschen Gedanken axiomatisch zu begründen so bieten sich zwei Wege dar. Entweder läßt man sich von Riemanns späteren Ideen im Zusammenhang mit der metrischen Geometrie leiten, und gelangt dann zu dem von Weyl aufgestellten metrischen Begriff einer Riemannschen Fläche. Oder man kann aus dem Begriff des mehrfach bedeckten Gebiets die Überdeckung als das wesentliche Merkmal heraussondern, und wird dann zu dem rein topologischen Begriff einer Überlagerungsfläche geführt. Die zentralen Aufgaben der Funktionentheorie können letzten Endes auf das gegenseitige Verhältnis zwischen diesen beiden Begriffsbildungen zurückgeführt werden.

Die geometrische Funktionentheorie dient einerseits dazu, die Behandlung analytischer Aufgaben durch die Einführung eines geometrischen Elements anschaulicher und dadurch einfacher zu machen, andererseits kommt es auch vor, daß die selbständige Betrachtung der geometrischen Seite zu einer erweiterten Fragestellung führt, die dann eine einheitliche Behandlung der ganzen Theorie ermöglicht. Ich will in diesem Vortrag dieses Verhalten an dem Beispiel der Wertverteilungstheorie der analytischen Funktionen beleuchten. Die zentrale Aufgabe wurde hier erst rein analytisch formuliert und behandelt. Später wurden geometrische Begriffe und Methoden eingeführt, die eine wesentliche formale Vereinfachung gestatteten. Geht man jetzt noch weiter, indem man die ganze Aufgabe geometrisch formuliert, so kommt man zu einer Überdeckungstheorie, die, wie ich glaube, auch inhaltlich eine neue Klarheit und Vereinfachung gegenüber der analytischen Theorie bietet.

Dieser Standpunkt ist in vielen Arbeiten der letzten Jahre implizit vertreten, aber erst durch eine ausdrücklich geometrische Durcharbeitung der allmählich hervorgewachsenen Ideen kommt die Theorie zu ihrer vollen

Geltung. Ich hoffe mit der in diesem Vortrag gegebenen kurzen Zusammenfassung, in der manches leider noch unvollkommen ist, der kommenden Forschung zu dienen.

2. Wegen der nicht ganz einheitlichen Terminologie ist es wichtig mit den Definitionen der grundlegenden Begriffe anzufangen. Man versteht zunächst unter einer Fläche einen zusammenhängenden Hausdorff-Raum, dessen Umgebungen einem Kreisinneren homeomorph sind. Gewöhnlich wird außerdem verlangt, daß die Mannigfaltigkeit separabel sei, d. h. sie erfüllt eine Abzählbarkeitsbedingung die mit Triangulierbarkeit äquivalent ist. Eine Riemannsche Fläche (R. Fl.) im Sinne von Weyl entsteht, wenn außerdem Folgendes gilt:

1. Zu jeder Umgebung U gehört eine bestimmte umkehrbar eindeutige Abbildung w=TP auf den Kreis  $|w|=|u+iv|<1$ .

2. Wenn  $U_{1}U_{2}$  nicht leer ist, so definiert  $w_{2}=T_{2}T_{1}^{-1}w_{1}$  eine direkt konforme Abbildung.

Nach einer wichtigen Bemerkung von Radó folgt die Triangulierbarkeit aus diesen Bedingungen und braucht also nicht postuliert zu werden.

Die zu jeder Umgebung gehörige komplexe Variable w heifat Ortsuniformisierende oder besser lokaler Parameter. Die inneren Eigenschaften der R. Fl. müssen, im lokalen Parameter ausgedrückt, eine gegenüber konforme Abbildungen invariante Form haben. Man kann demnach eine auf der Fläche gegebene Funktion als analytisch oder harmonisch definieren, falls sie in bezug auf den lokalen Parameter analytisch bzw. harmonisch ist, denn diese Begriffe haben ja die verlangte Invarianzeigenschaft. Dasselbe gilt von der konformen Abbildung einer Fläche auf eine andere.

Es ist noch zu sagen, daß zwei R. Fl. als äquivalent angesehen werden müssen, sobald sie umkehrbar eindeutig und konform aufeinander bezogen werden können. Demnach gibt es nur zwei offene, einfach zusammenhängende R. Fl., der Einheitskreis und die Ebene. Dies hindert natürlich nicht daß man verschiedene Verwirklichungen derselben R. Fl. betrachten kann und muß. Eine der grundlegenden Aufgaben besteht gerade darin, die Identität von zwei explizit gegebenen R. Fl. festzustellen.

3. Wir gehen zum Begriff der Überlagerungsfläche (Ü. Fl.) über. Wir betrachten zwei topologisch gegebene Flächen $W$ und $W_{0}$ und eine Transformation $P_{0}=SP$, welche jedem Punkt von $W$ einen Spurpunkt $P_{0}$ auf $W_{0}$ zuordnet. Man sagt auch daß $P$ über den Punkt $P_{0}$ liegt. Damit eine Ü. Fl. definiert sei verlangen wir, daß $S$ eine sogenannte innere Transformation sei. Dieser Begriff wurde von Stoilow eingeführt und kann durch folgende Bedingungen charakterisiert werden:

1. S ist stetig.

2. Offene Mengen werden in offene Mengen übergeführt.

3. Die Punkte P mit  $SP=P_{0}$  liegen isoliert.

Die dritte Bedingung kann nach Stoilow durch eine bedeutend schwächere ersetzt werden.

Es läßt sich zeigen, daß die Abbildung S lokal umkehrbar eindeutig ist, mit der Ausnahme von gewissen isoliert gelegenen Verzweigungspunkten, wo die Abbildung den Charakter einer Potenz besitzt. Die rein topologische Behandlung und Klassifizierung von Ü. Fl. ist von größter Bedeutung für die Funktionentheorie.

Ist $W_0$ besonders eine R. Fl., so kann man die Winkelmessung von $W_0$ auf $W$ übertragen, und erhält dann eine neue R. Fl., die als Ü. Fl. einer Riemannschen Grundfläche gegeben ist. Wählt man für $W_0$ eine einfache, explizit gegebene R. Fl., z. B. die Ebene oder die Riemannsche Kugel, so gelangt man genau zu der von Riemann selbst betrachteten Situation. In unseren Anwendungen wird $W_0$ eine geschlossene R. Fl. sein.

4. In diesem Vortrag beschäftigen uns die als Ü. Fl. gegebenen R. Fl. Das Hauptproblem lautet: Welche Eigenschaften einer Ü. Fl. sind innere Eigenschaften der R. Fl., d. h. solche Eigenschaften, die jeder Darstellung einer gegebenen R. Fl. als Ü. Fl. von  $W_{0}$  zukommen. Oder anders ausgedrückt, wie erkennt man, daß zwei gegebene Ü. Fl. konform-äquivalent bzw. nicht konform-äquivalent sind. Hierin ist das spezielle Typenproblem enthalten: W sei eine offene, einfach zusammenhängende Ü. Fl. Es gilt zu entscheiden ob sie mit einem endlichen Kreis oder mit der ganzen Ebene äquivalent ist. Im ersten Falle spricht man vom hyperbolischen, im zweiten Falle vom parabolischen Typus. Alle wesentlichen Ergebnisse beziehen sich auf dieses spezielle Problem, das uns in der Folge ausschließlich beschäftigen soll.

Von welcher Art müssen nun die Eigenschaften sein, durch welche wir den Typus der R. Fl. charakterisieren wollen. Eine naturgemäße Forderung ist, daß sie möglichst explizit durch die Transformation SP ausgedrückt werden können. Hierin liegt eine besondere Schwierigkeit, weil das Darstellungsproblem für die Transformation S von einigen Sonderfällen abgesehen gar nicht angegriffen worden ist. Es wäre in der Tat ein Desideratum, daß man diese wichtige Frage ganz getrennt von dem Typenproblem behandeln würde. Bei diesem Mangel hilft man sich durch das folgende Verfahren aus: Die gegebene Fläche wird durch eine Folge von abgeschlossenen Teilgebieten ausgeschöpft, und für jedes Teilgebiet wird die Anzahl der über einem Spurpunkt gelegenen Punkte sowie die Anzahl der Verzweigungspunkte abgezählt. Aus dem asymptotischem Verhalten dieser Überdeckungszahlen versucht man dann den Typus zu ermitteln.

Dies ist offenbar ein ungenaues Verfahren von dem man nicht zu viel erwarten darf.

5. Ich will jetzt versuchen einen Einblick in die Methoden zu geben, die man für die Behandlung der eben genannten Aufgabe verwendet, selbstverständlich ohne auf Einzelkeiten einzugehen. $^{1}$

Auf einer R. Fl. kann man durch eine Differentialform  $ds=\lambda|dw|$  in mannigfacher Weise eine Riemannsche Metrik einführen. Die positive Funktion  $\lambda$  soll nicht als Punktfunktion erklärt sein, sondern in solcher Weise von dem lokalen Parameter abhängen, daß ds invariant wird. Die neue Metrik ist in anderen Worten dadurch bestimmt, daß sie mit der euklidischen Metrik der Parameterebene konform sein soll.

In der Riemannschen Metrik kann man nun zunächst Kurvenlängen und Flächeninhalte bestimmen. Wegen der additiven Charakter genügt es nämlich solche Kurven und Gebiete zu betrachten, die innerhalb einer Umgebung liegen, und für diese kann man Länge und Inhalt durch die invarianten Integrale

$$
\int d s = \int \lambda | d w | \text {   und   } \iint d \omega = \iint \lambda^ {2} d u d v
$$

definieren.

In der Differentialgeometrie werden auch andere invariante Bildungen betrachtet, die voraussichtlich für unsere Zwecke wichtig sein können. Es sind dies die curvatura integra $\iint K d\omega$ und das geodätische Krümmungsintegral $\int \frac{ds}{\varrho_g}$ längs einer Kurve. Zwischen diesen geometrischen Größen bestehen gewisse Beziehungen, aus denen die Ergebnisse der Überdeckungstheorie folgen werden.

I. Nach dem Fundamentalsatz der konformen Abbildung gibt es auf W eine harmonische Funktion  $G(w)$ , die bis auf einen negativen logarithmischen

Pol regulär ist und im hyperbolischen Falle gegen 0, im parabolischen Falle gegen ∞ strebt, wenn w eine eigentlich divergente (d. h. häufungspunktlose) Folge durchläuft. Die Gebiete $W(t)$, definiert durch $G(w) \leq t$, bestimmen eine Ausschöpfung von W, die wir eine Normalausschöpfung nennen wollen. Die Niveaukurven $G(w) = t$ werden mit $\Gamma(t)$ bezeichnet.

In einer beliebigen Metrik  $ds=\lambda|dw|$  sei  $L(t)=\int_{\Gamma(t)}ds$  und  $A(t)=\iint_{W(t)}d\omega$ . Man findet unmittelbar

$$
A ^ {\prime} (t) = \int_ {\Gamma (t)} \frac {d s}{\frac {\partial G}{\partial n}},
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Inzwischen erschien eine ausführliche Darstellung: Lars Ahlfors, Über die Anwendung differentialgeometrischer Methoden zur Untersuchung von Überlagerungsflächen, Acta Soc. Scient. Fenn., Nov. Ser. T. II, N: o 6.</span></small>

wobei die Normalableitung in Bezug auf die Riemannsche Metrik zu nehmen ist, und durch Anwendung der Schwarz'schen Ungleichung

$$
L (t) ^ {2} \leq A ^ {\prime} (t) \int_ {\Gamma (t)} \frac {\partial G}{\partial n} d s = 2 \pi A ^ {\prime} (t),
$$

woraus

$$
d t \leqslant \frac {d A (t)}{L (t) ^ {2}}.
$$

Man schließt hieraus z. B.: Im parabolischen Falle ist das Integral

$$
\int^ {\infty} \frac {d A (t)}{L (t) ^ {2}}
$$

in jeder Metrik divergent.

Ähnliches gilt für das geodätische Krümmungsintegral $H(t) = \int_{\Gamma(t)} \frac{ds}{\varrho_g}$.

Nach bekannten Formeln aus der Differentialgeometrie wird wegen  $\Delta G=0$

$$
H (t) = \int_ {\Gamma (t)} \frac {\partial}{\partial n} \log \frac {\lambda}{| \operatorname{grad} G |} d s,
$$

wo natürlich  $\frac{\partial}{\partial n}\cdot ds$  von der benutzten Metrik unabhängig ist. Integration und Anwendung der Green'schen Formel ergibt

$$
\begin{array}{l} \int_ {t _ {0}} ^ {t} H (t) d t = \iint_ {W (t) - W (t _ {0})} \frac {\partial}{\partial n} \log \frac {\lambda}{| \operatorname{grad} G |} d s d t = \iint \frac {\partial}{\partial n} \log \frac {\lambda}{| \operatorname{grad} G |} \frac {\partial G}{\partial n} d s d n \\ = D \left(\log \frac {\lambda}{| \operatorname{grad} G |}, G\right) = \Bigg | _ {t _ {0}} ^ {t} \int_ {\Gamma (t)} \log \frac {\lambda}{| \operatorname{grad} G |} \cdot \frac {\partial G}{\partial n} d s \end{array}
$$

und hieraus folgt, wenn man das geometrische Mittel durch das arithmetische ersetzt,

$$
\int_ {t _ {0}} ^ {t} H (t) d t \leqq 2 \pi \log L (t) + \text {Konst.}
$$

In Verbindung mit dem früheren Ergebnis wird für  $H(t)$  eine obere Schranke von der Gröfaenordnung log  $A(t)$  gewonnen. Die Ermittlung einer unteren Schranke ist eine Aufgabe, deren Lösung große Tragweite hätte.

II. Zweitens betrachten wir eine beliebige Ausschöpfung, die durch die Niveaukurven $\Phi(w)=\tau$ bestimmt wird, wobei $\Phi(w)$ nur gewissen allgemeinen Bedingungen unterworfen ist. Wir führen diesmal eine bestimmte zugehörige Metrik ein, in welcher diese Niveaukurven parallell sind. Man erzielt dies durch die Wahl $ds=|\text{grad}\Phi|\cdot|dw|$, eine Bildung, welche offenbar die nötige Invarianzeigenschaft besitzt.

Die oben betrachteten geometrischen Gröfaen stehen bei dieser Wahl in einem besonders einfachen Zusammenhang miteinander. Mit denselben Bezeichnungen wie oben (der neue Parameter soll Mißverständnisse verhindern) gilt nämlich

$$
A ^ {\prime} (\tau) = L (\tau), L ^ {\prime} (\tau) = H (\tau).
$$

Weiter läßt sich auch hier eine Beziehung zu der Funktion  $G(w)$  herleiten. Für genügend große  $\tau$  wird

$$
\int_ {\Gamma (\tau)} \frac {\partial G}{\partial n} d s = 2 \pi ,
$$

woraus

$$
4 \pi^ {2} \leq L (\tau) \int_ {\Gamma (\tau)} \left(\frac {\partial G}{\partial n}\right) ^ {2} d s
$$

und durch Integration

$$
4 \pi^ {2} \int_ {\tau_ {0}} ^ {\tau} \frac {d \tau}{L (\tau)} \leq \int_ {\tau_ {0}} ^ {\tau} \int_ {\tau_ {0}} ^ {\tau} \left(\frac {\partial G}{\partial n}\right) ^ {2} d s d t = \int_ {\tau_ {0}} ^ {\tau} \int_ {\tau_ {0}} ^ {\tau} | \operatorname{grad} G | ^ {2} d u d v.
$$

Ist die Fläche hyperbolisch, so wird das letzte Integral beschränkt, denn für das zwischen zwei Niveaulinien G=a und G=b gelegene Gebiet wird

$$
\iint \left| \operatorname{grad} G \right| ^ {2} d u d v = \Bigg | _ {a} ^ {b} \int G \frac {\partial G}{\partial n} d s = (b - a) 2 \pi .
$$

Wenn W hyperbolisch ist, so gilt für eine beliebige Ausschöpfung und die zugehörige Metrik, in welcher die Niveaukurven parallel sind,

$$
\int_ {0} ^ {\infty} \frac {d \tau}{L (\tau)} <   \infty .
$$

Die eben angeführten Resultate liefern an und für sich keinen Beitrag zur Lösung des Typenproblems, denn sie enthalten ja nur eine Beziehung zwischen dem Typus und den möglichen Metriken auf einer R. Fl. Ihre Bedeutung für die Untersuchung der Ü. Fl. besteht aber darin, daß es jetzt nur noch übrig bleibt eine Beziehung zwischen der Metrik und den Überdeckungseigenschaften aufzustellen, um dann durch Kombination Aussagen über das Typenproblem zu erhalten. Diese Spaltung der Aufgabe in einen metrisch-konformen und einen topologisch-metrischen Teil ist von größter Wichtigkeit.

6. Die topologisch-metrische Aufgabe kann mit Methoden angegriffen werden, die ich in einer neulich erschienen Arbeit auseinandergesetzt habe. $^{1}$  Wir schlagen hier einen anderen Weg ein, der die Zusammenhänge mit der Differentialgeometrie besser hervorhebt. Das Verfahren leidet zwar an dem Mangel, daß die Scheidung zwischen metrisch und konform nicht ganz restlos durchgeführt ist. Immerhin ist dies nicht wesentlich und könnte ohne größere Schwierigkeiten vermieden werden.

Wir besprechen zunächst die Fragen, die sich an den sog. ersten Hauptsatz von Nevanlinna schließen. Auf der Grundfläche $W_0$ sei $\mu(\Omega)$ eine vollständig additive Mengenfunktion von beschränkter Schwankung, die der normierenden Bedingung $\mu(W_0)=1$ genügt. Von der additiven Eigenschaft ausgehend kann man die Funktion auch für mehrfach bedeckte Gebiete $\overline{W}$ der Ü. Fl. erklären, indem man

$$
\mu (\bar {W}) = \int_ {W _ {0}} n (a) d \mu (a)
$$

setzt. Hier bezeichnet $n(a)$ die Anzahl der über $a$ gelegenen Punkte. Die Zahl $\mu(\overline{W})$ gibt ein Mafs für die Überdeckung durch das Gebiet $\overline{W}$ und heißt auch die mittlere Blätteranzahl von $\overline{W}$. Es entsteht die Frage: Inwiefern hängt die mittlere Blätteranzahl von der benutzten Mengenfunktion ab?

Um dies zu entscheiden betrachte man zwei verschiedene Belegungen  $\mu_{1}(\Omega)$  und  $\mu_{2}(\Omega)$  und bilde  $\mu_{0}=\mu_{1}-\mu_{2}$ . Für eine Belegung mit verschwindender Gesamtmaße kann man leicht ein Potential definieren. Auf  $W_{0}$  gibt es eine bis auf eine additive Konstante bestimmte harmonische Funktion  $\chi(w,a,b)$  die in a und b logarithmische Pole mit den Residuen 1 bzw. -1 besitzt. Man bilde

$$
p (w) = \int_ {W _ {0}} \chi (w, a, b) d \mu (a),
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$  Acta Mathematica, t. 65, 1935.</span></small>

wo b ein fester Punkt ist und die zu verschiedenen a gehörigen  $\chi(w, a, b)$  so normiert sind, daß ihr Unterschied im Punkte b verschwindet. Es ist leicht zu sehen, daß  $p(w)$  nur scheinbar von b abhängt.

Man bezeichne nun mit $S(t)$ die mittlere Blätteranzahl des Gebiets $W(t)$ einer normalen Ausschöpfung. In einer unmittelbar verständlichen Bezeichnung gilt dann

$$
\int_ {t _ {0}} ^ {t} \left(S _ {1} (t) - S _ {2} (t)\right) d t = \left| \int_ {t _ {0}} ^ {t} \int_ {\Gamma (t)} p (w) \frac {\partial G}{\partial n} d s. \right.\tag{1}
$$

Diese Gleichung stellt die allgemeinste Form des ersten Hauptsatzes dar. Die wichtigste Anwendung bezieht sich auf den Fall, wo die Belegung  $\mu_{0}$  ein bzw. nach oben, nach unten oder in beiden Richtungen beschränktes Potential besitzt. Man erhält jenachdem eine asymptotische Ungleichung oder Gleichung zwischen  $S_{1}(t)$  und  $S_{2}(t)$ .

Als Normalbelegung ist es zweckmäßig eine Belegung von stetiger Flächendichte zu wählen, und die zugehörige Größe $S(t)$ als eine Charakteristik der Ü. Fl. zu betrachten. Ist $\overline{S}(t)$ eine zweite, in derselben Weise bestimmte Größe, so gilt jedenfalls

$$
\int_ {t _ {0}} ^ {t} S (t) d t = \int_ {t _ {0}} ^ {t} \bar {S} (t) d t + O (1),
$$

und es kommt in den Anwendungen nicht darauf an, ob man  $S(t)$  oder  $\overline{S}(t)$  betrachtet.

7. Den zweiten Hauptsatz von Nevanlinna wollen wir in Zusammenhang mit einer klassischen Formel der Differentialgeometrie stellen, nämlich mit dem Satz von Gauss-Bonnet. Es besteht kein Zweifel, daß diese Zusammenstellung im besten Einklang mit der topologisch-metrischen Natur des zweiten Hauptsatzes steht.

Auf der Grundfläche führen wir zunächst eine überall reguläre Metrik  $ds = \lambda |dw|$  ein. Die Gauss-Bonnetsche Formel für ein Teilgebiet  $\bar{W}$  mit der Eulerschen Charakteristik E lautet dann

$$
- \frac {1}{2 \pi} \int_ {\bar {W}} \int K d \omega = E + \frac {1}{2 \pi} \int_ {\Gamma} \frac {d s}{\varrho_ {g}}.\tag{I}
$$

Besonders erhält man für die ganze Fläche  $W_{0}$

$$
- \frac {1}{2 \pi} \int_ {W _ {0}} \int K d \omega = E _ {0}.\tag{2}
$$

Die Formel (1) gilt nicht unverändert für ein Teilgebiet der Ü. Fl., denn die übertragene Metrik der Grundfläche wird in den Windungspunkten singular. Durch Zerlegung in schlichte Teilgebiete beweist man leicht die verallgemeinerte Formel

$$
- \frac {1}{2 \pi} \int_ {\bar {w}} \int K d \omega = E - n _ {1} + \frac {1}{2 \pi} \int_ {\Gamma} \frac {d s}{\varrho_ {g}},\tag{3}
$$

wo  $n_{1}$  die Anzahl der mit ihren Verzweigungsordnungen gezählten Windungspunkte von  $\bar{W}$  bezeichnet.

Wir fassen jetzt einen noch allgemeineren Fall ins Auge, indem wir erlauben, daß die benutzte Metrik der Grundfläche in endlich vielen Punkten $a_{1}, \cdots, a_{q}$ singular wird. Damit (3) noch gültig sei verlangen wir, daß die singulären Punkte durch geodätische Nullkreise ausgeschlossen werden können, d. h. durch kleine Kreise für welche das geodätische Krümmungsintegral an der Grenze verschwindet. Bei einem bestimmten asymptotischen Verhalten von $\lambda$ wird diese Bedingung erfüllt; es genügt in der Tat, daß $r\frac{\partial}{\partial r}\log \lambda \to 1$ wenn $r = |w - a_{v}| \to 0$.

Die Fläche $W_0$ wird nun in allen Punkten $a_r$ und die Fläche $\bar{W}$ in allen überliegenden Punkten punktiert. Offenbar wird der Zusammenhang von $W_0$ dadurch um $q$ und der Zusammenhang von $\bar{W}$ um $\sum_{1}^{q} \bar{n}(a_r)$ erhöht, wenn $\bar{n}(a)$ die einfach gezählte Anzahl der über $a$ gelegenen Punkte von $\bar{W}$ bezeichnet. Die Formeln (3) und (2) gehen dann in

$$
- \frac {1}{2 \pi} \int_ {\bar {W}} \int K d \omega = E + \sum_ {1} ^ {q} n (a _ {v}) - n _ {1} + \frac {1}{2 \pi} \int_ {\Gamma} \frac {d s}{\varrho_ {g}}\tag{4}
$$

und

(5)

über.

$$
- \frac {1}{2 \pi} \int_ {w _ {0}} \int K d \omega = q + E _ {0}
$$

Wir wenden (4) und (5) auf die Gebiete $W(t)$ einer normalen Ausschöpfung an und benutzen den ersten Hauptsatz. Mit unmittelbar verständlichen Bezeichnungen ergibt sich

$$
(q + E _ {0}) S (t) = \sum_ {1} ^ {q} n (a _ {\nu}, t) - n _ {1} (t) - 1 + H (t) + \beta (t),\tag{II}
$$

wo $\beta(t)$ vom Potential der durch $\iint K d\omega$ definierten Belegung abhängt. Indem man unter Befriedigung der obigen Bedingungen $\lambda$ passend wählt, so wird es möglich $H(t)$ und $\beta(t)$ mit Hilfe der früher dergestellten Methoden abzuschätzen, und man erhält in (II) die allgemeinste Form des zweiten Hauptsatzes.

Für die Kugel ist  $E_{0}=-2$  und man erhält den Satz von Nevanlinna mit seinen bekannten Folgerungen für die Wertverteilung bei meromorphen Funktionen. Der Torus hat die Charakteristik 0, und man findet daß alle Nevanlinnaschen Defekte und Verzweigungsindizes im parabolischen Falle verschwinden müssen. Endlich führt (II) im Falle  $E_{0}>0$  schon mit q=0 zu einem leicht erkennbaren Widerspruch, falls t gegen Unendlich wachsen kann. Es ist dies ein Ausdruck für den sog. zweiten Satz von Picard, der in unserer Formulierung besagt, daß jede Überlagerungsfläche einer geschlossenen Fläche vom Geschlecht größer als 0 hyperbolisch sein muß.

8. Die Zeit erlaubt nicht auf die in Nr. 5 unter II. eingeleiteten Betrachtungen näher einzugehen. Sie sollen prinzipiell zu hinreichenden Bedingungen für den parabolischen Fall führen. Eine allgemeine Theorie ist noch nicht entwickelt worden; es sei nur erwähnt dafs auch in diesem Zusammenhange die Gauss-Bonnetsche Formel von Bedeutung ist. Bemerkenswerte Ergebnisse, die immerhin nur in Einzelfällen anwendbar sind, hat besonders Kobayashi $^{1}$ erhalten.

$^{1}$  Sci. Rep. Tokyo Bunrika Daigaku, sect. A Nr. 39 (1935).