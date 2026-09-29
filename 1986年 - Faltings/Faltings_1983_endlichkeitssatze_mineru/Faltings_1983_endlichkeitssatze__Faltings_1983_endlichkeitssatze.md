# Endlichkeitssätze für abelsche Varietäten über Zahlkörpern

G. Faltings

Fachbereich Mathematik, Bergische Universitäts-Gesamthochschule Wuppertal, Gaußstr. 20, D-5600 Wuppertal 1, Bundesrepublik Deutschland

## §1. Einleitung

Sei K eine endliche Erweiterung von Q, A eine über K definierte abelsche Varietät,  $\pi=\text{Gal}(\overline{K}/K)$  die absolute Galois-Gruppe von K, l eine Primzahl. Dann operiert  $\pi$  auf dem Tate-Modul

$$
T _ {l} (A) = \varprojlim A [ l ^ {n} ] (\overline {{K}}).
$$

Ziel der vorliegenden Arbeit ist der Beweis der folgenden Resultate:

a) Die Darstellung von $\pi$ auf $T_{l}(A)\otimes_{\mathbf{Z}_{l}}\mathbb{Q}_{l}$ ist halbeinfach.

b) Die Abbildung

$$
\operatorname{End} _ {K} (A) \otimes_ {\mathbf {Z}} \mathbb {Z} _ {l} \rightarrow \operatorname{End} _ {\pi} (T _ {l} (A))
$$

ist ein Isomorphismus.

c) Sei S eine endliche Menge von Stellen von K, d>0. Dann gibt es nur endlich viele Isomorphieklassen d-fach polarisierter abelscher Varietäten über K, welche gute Reduktion außerhalb S haben.

a) und b) sind bekannt unter dem Namen Tate-Vermutung, c) als Shafarevich-Vermutung. Weiter weiß man ([9]), daß aus c) die Mordell-Vermutung folgt. Die Tate-Vermutung ist von Tate selbst für abelsche Varietäten über endlichen Körpern gezeigt worden. Zarhin verallgemeinerte dies auf Funktionenkörper ([15, 16]) über solchen, und unser Beweis ist eine Übertragung seiner Methoden auf den Zahlkörper-Fall. Das zur Übersetzung notwendige Wörterbuch hat Arakelov geliefert ([2]), und seine Methoden sind vom Verfasser ausgebaut worden ([5]). Kurz gesagt handelt es sich darum, „alles“ mit hermiteschen Metriken zu versehen.

Der Beweis für c) erfolgt so, daß zunächst nur die Endlichkeit für Isogenie-Klassen gezeigt wird. Die grundlegende Idee dazu hat mir der Gutachter der „Inventiones“ anläßlich der Veröffentlichung meiner Arbeit [6] mitgeteilt, und ich mußte sie nur noch von der Hodge-Theorie in die étale Kohomologie über-

setzen. Ich möchte daher dem mir persönlich unbekannten Gutachter an dieser Stelle für seine Anregung herzlich danken.

Der Rest des Beweises von c) benutzt eine Variante der bei a) und b) verwendeten Methoden.

Die Arbeit beginnt zunächst mit einigen technischen Details über Höhen. Die Komplikationen ergeben sich daraus, daß meines Wissens noch kein guter Modulraum semiabelscher Varietäten über Z existiert. (Mit ähnlichen Problemen hat sich auch L. Moret-Bailly zu kämpfen, der die Verhältnisse über Funktionenkörpern untersucht ([7]).) Danach werden die sehr schönen Ergebnisse von Tate ([13]) über p-divisible Gruppen benutzt. Der Schluß ist dann wieder etwas technischer.

Ich habe viel über das Thema von L. Szpiro gelernt, dem ich an dieser Stelle für seine Einführung in diesen Problemkreis danke. P. Deligne hat mich auf eine Unstimmigkeit in der ursprünglichen Fassung der Arbeit aufmerksam gemacht.

## §2. Semiabelsche Varietäten

Definition. Sei S ein Schema (oder ein algebraic stack). Eine semiabelsche Varietät der relativen Dimension g über S ist eine glatte algebraische Gruppe  $p: G \to S$ , so daß die Fasern von p zusammenhängend von der Dimension g sind, und Erweiterungen einer abelschen Varietät durch einen Torus.

Beispiel. Sei $q\colon C\to S$ eine stabile Kurve vom Geschlecht $g$ ([4]). Dann ist

$$
J = \operatorname{Pic} ^ {\tau} (C / S) \rightarrow S
$$

eine semiabelsche Varietät der relativen Dimension g.

Wir benötigen das folgende

Lemma 1. Sei S normal, $U \subset S$ offen und dicht $p_{1}: A_{1} \to S$ und $p_{2}: A_{2} \to S$ zwei semiabelsche Varietäten, $\phi: A_{1}/U \to A_{2}/U$ ein über U definierter Homomorphismus algebraischer Gruppen. Dann läßt sich $\phi$ eindeutig auf ganz S fortsetzen.

Beweis. Dies ist wohlbekannt, falls S Spektrum eines kompletten diskreten Bewertungsringes ist. Im allgemeinen reduziert man sofort auf S noethersch und exzellent, und bezeichnet mit

$$
X \subseteq A _ {1} \times_ {s} A _ {2}
$$

den Abschluß des Graphen von $\phi$.

Nach Basiswechsel mit geeigneten Bewertungsringen sieht man, daß die Projektion  $pr_{1}: X \rightarrow A_{1}$  eigentlich ist, und daß ihre Fasern nur einen Punkt besitzen. Da  $A_{1}$  normal ist, muß  $pr_{1}$  ein Isomorphismus sein, und X der Graph der eindeutig bestimmten Fortsetzung von  $\phi$ . (Eindeutigkeit folgt zum Beispiel durch Betrachtung von Torsionspunkten, oder auf tausend andere Arten.)

Definition. Sei $p: A \to S$ eine semiabelsche Varietät der relativen Dimension $g$, $s: S \to A$ der Nullschnitt.

Setze:

$$
\omega_ {A / S} = s ^ {*} (\Omega_ {A / S} ^ {g}),
$$

$\omega_{A/S}$  ist ein Geradenbündel auf S.

Bemerkungen. a) Wenn $p$ eigentlich ist, so ist $\omega_{A/S} \cong p_*(\Omega_{A/S}^g)$.

b) $\omega_{A / S}$ kommutiert mit Basiswechsel.

c) Wenn $A = \operatorname{Pic}^{\tau}(C/S)$ mit einer stabilen Kurve $q: C \to S$, so ist $\omega_{A/S} \cong A^{g} q_{*}(\omega_{C/S})$, wobei $\omega_{C/S}$ den relativen dualisierenden Modul bezeichnet.

d) Wenn $S = \operatorname{Spec}(\mathbb{C})$ und $p$ eigentlich ist (d.h., $A / \mathbb{C}$ ist eine komplexe abelsche Varietät), so besitzt

$$
\omega_ {A / S} \cong \Gamma (A, \Omega_ {A / \mathbb {C}} ^ {g})
$$

ein kanonisches hermitesches Skalarprodukt:

Wenn  $\alpha$ ,  $\beta$  holomorphe Differentialformen auf A sind, so setze

$$
\langle \alpha , \beta \rangle = \left(\frac {i}{2}\right) ^ {g} \int_ {A} \alpha \wedge \bar {\beta}.
$$

Wir benötigen einige Tatsachen über die Modulräume stabiler Kurven und abelscher Varietäten. Dazu scheint die Sprache der „algebraic stacks“ am angemessensten zu sein. Falls dem Leser diese Notation zu abstrakt erscheint, so möge er die folgenden Überlegungen durchführen:

Es geht eigentlich um Endlichkeitsaussagen.

Wenn S einer der demnächst einzuführenden algebraic stacks ist, und S den zugehörigen groben Modulraum bezeichnet, so gibt es stets eine offene Überdeckung

$$
S = \bigcup_ {i = 1} ^ {r} U _ {i}
$$

und endlich surjektive Abbildungen $V_{i}\to U_{i}$, so daß über $V_{i}$ das „universelle Objekt zu $\mathfrak{S}^{\prime\prime}$ existiert. Man kann dann alle Rechnungen in den $V_{i}$ durchführen.

Nun zu den hier verwendeten algebraic stacks.

1. $\overline{\mathfrak{M}}_g$ klassifiziere die stabilen Kurven vom Geschlecht $g$ ([4]). $\overline{\mathfrak{M}}_g$ ist eigentlich über $\operatorname{Spec}(\mathbb{Z})$, und der zugehörige grobe Modulraum heiße $\overline{M}_g$.

2. $\mathfrak{A}_{g}$ klassifiziere die prinzipal-polarisierten abelschen Varietäten der relativen Dimension $g$, und $A_{g}$ sei der zugehörige Modulraum.

$\mathfrak{A}_{\mathrm{g}}$ ist nicht eigentlich über $\operatorname{Spec}(\mathbf{Z})$, aber die folgenden Tatsachen sind bekannt:

a) Wenn

$$
p \colon A \to \mathfrak {A} _ {g}
$$

die universelle abelsche Varietät über $\mathfrak{A}_{g}$ bezeichnet, so gibt es ein $r>0$, für welches $(\omega_{A/\mathfrak{A}_{g}})^{\otimes r}$ ein sehr amples Geradenbündel auf $A_{g}/\mathbb{Q}$ definiert ([3]). Sei $\bar{A}_{g}/\mathbb{Q}$ der Zariski-Abschluß von $A_{g}/\mathbb{Q}$ in dem zugehörigen projektiven Raum $\mathbb{IP}_{\mathbb{Q}}^{N}$, $\bar{A}_{g}/\mathbb{Z}$ der Zariski-Abschluß in $\mathbb{IP}_{\mathbb{Z}}^{N}$, und $\mathcal{M}$ das Geradenbündel $\mathcal{O}(1)$ auf $\bar{A}_{g}/\mathbb{Z}$. ($\mathcal{M}$ setzt auf $\bar{A}_{g}/\mathbb{Q} (\omega_{A/\mathfrak{A}_{g}})^{\otimes r}$ fort.)

b) Es gibt über $\mathbb{C}^{s}$ einen eigentlichen dominanten Morphismus

$$
\phi \colon \mathfrak {N} \to \bar {A} _ {g} / \mathbb {C},
$$

so daß über $\mathfrak{N}$ eine semiabelsche Varietät existiert, welche die universelle abelsche Varietät über $\mathfrak{A}_{g}$ fortsetzt (siehe [8], §9). Außerdem ist bekannt, daß $\omega^{\otimes r}$ dieser semiabelschen Varietät isomorph zu $\phi^{*}(\mathcal{M})$ ist. (Hierzu muß man direkt rechnen, siehe meine Ausführungen dazu in [6], §2.)

Lemma 2. Es gibt über $\operatorname{Spec}(\mathbb{Z})$ einen eigentlichen algebraic stack $3$, eine offene Teilmenge $\mathfrak{U}\subset\mathfrak{Z}$ und einen eigentlichen Morphismus $\psi\colon\mathfrak{U}\to\mathfrak{A}_{\mathrm{g}}$, welcher sich zu einem $\bar{\psi}\colon\mathfrak{Z}/\mathbb{Q}\to\bar{A}_{\mathrm{g}}/\mathbb{Q}$ fortsetzt, so daß über $3$ die folgenden Objekte existieren:

a) Eine stabile Kurve $q: C \to 3$.

b) Ein Untergeradenbündel (= lokal direkter Sumand) $\mathcal{L} \subseteq A^{g} q_{*}(\omega_{C/\mathbb{Z}})$.

c) Über $\mathfrak{U}$ ein Paar von Gruppenhomomorphismen

$$
\alpha \colon \operatorname{Pic} ^ {\tau} (C / 3) \rightarrow \psi^ {*} (A),
$$

$$
\beta \colon \psi^ {*} (A) \to \operatorname{Pic} ^ {\tau} (C / 3)
$$

mit

$$
\alpha \circ \beta = \text { Multiplikation   mit   einem } d \in \mathbb {N}, d \neq 0.
$$

(Dabei sei $A$ wieder die universelle abelsche Varietät über $\mathfrak{A}_{g}$.)

d) Auf $3 \otimes_{\mathbf{Z}} \mathbb{Q}$ existiert ein Isomorphismus $\mathcal{L}^{\otimes r} = \bar{\psi}^{*}(\mathcal{M})$, und $\mathcal{L}$ ist über $\mathfrak{U}/\mathbb{Q}$ das Bild von

$$
\alpha^ {*} \colon \psi^ {*} (\omega_ {A / \mathfrak {U} _ {g}}) \to \Lambda^ {g} q _ {*} (\omega_ {C / Z}).
$$

Der daraus resultierende Isomorphismus (über $\mathfrak{U}/\mathbb{Q}$)

$$
\psi^ {*} (\omega_ {A / \mathfrak {A} _ {g}}) ^ {\otimes r} \cong \psi^ {*} (\mathcal {M})
$$

ist $\psi^{*}$-Pullback des bei der Konstruktion von $\mathcal{M}$ angegebenen Isomorphismus über $A_{g}$.

Beweis. In dem generischen Punkte von $\mathfrak{A}_{g}$ ist die zugehörige abelsche Varietät Quotient einer Jacobischen. Die zugehörige Kurve entspricht einer rationalen Abbildung von $\mathfrak{A}_{g}$ in $\overline{\mathfrak{M}}_{\tilde{g}}$, für ein $\tilde{g}$.

Wenn man den Graphen dieser Abbildung betrachtet, so erhält man (mit Hilfe einiger trivialer Zusatzüberlegungen) einen ersten Kandidaten 3, so daß schon a) und (nach Lemma 1) c) erfüllt sind. $\mathcal{L}$ ist dann über $\mathfrak{U} \otimes_{\mathbb{Z}} \mathbb{Q}$ durch d) schon festgelegt, und liefert eine rationale Abbildung von $\mathfrak{U} \otimes_{\mathbb{Z}} \mathbb{Q}$ in ein geeignetes projektives Bündel über 3. Man ersetzt 3 durch die Normalisierung des Abschlusses des zugehörigen Graphen, und dann sind auch b) und der zweite Teil von d) erfüllt. Zum Rest von d) ist zu vermerken, daß man den gesuchten Isomorphismus schon über $\mathfrak{U} \otimes_{\mathbb{Z}} \mathbb{Q}$ konstruiert hat, und man muß nur noch die Fortsetzbarkeit auf $3 \otimes_{\mathbb{Z}} \mathbb{Q}$ zeigen. Dazu kann man den Grundkörper von $\mathbb{Q}$ auf $\mathbb{C}$ erweitern, und es reicht, die Fortsetzbarkeit für ein $\tilde{3}/\mathbb{C}$ zu zeigen, welches dominant und eigentlich über 3 liegt.

Mit Hilfe des weiter oben eingeführten $\phi\colon\mathfrak{N}\to\bar{A}_{g}/\mathbb{C}$ konstruiert man ein normales $\tilde{\mathfrak{Z}}$, so daß $\psi^{*}(A)$ sich auf $\tilde{\mathfrak{Z}}$ zu einer semiabelschen Varietät fortsetzt. Nach Lemma 1 kann man auch $\alpha$ und $\beta$ fortsetzen, und diese liefern den gewünschten Isomorphismus über $\tilde{\mathfrak{Z}}$.

Korollar. Es gibt eine natürliche Zahl e>0 mit der folgenden Eigenschaft:

Sei K ein Zahlkörper, R der Ring der ganzen Zahlen in K,

$$
p \colon A \to \operatorname{Spec} (R)
$$

eine semiabelsche Varietät, so daß die generische Faser A/K eigentlich über K ist, und eine prinzipale Polarisation bestitzt. Dem entspricht eine Abbildung  $\rho\colon\operatorname{Spec}(K)\to A_{g}/\mathbb{Q}$ , welche sich zu einem  $\rho\colon\operatorname{Spec}(R)\to\bar{A}_{g}/\mathbb{Z}$  fortsetzt.

Nach Konstruktion besteht ein Isomorphismus

$$
\rho^ {*} (\mathcal {M}) \otimes_ {R} K \cong (\omega_ {A / R}) ^ {\otimes r} \otimes_ {R} K.
$$

Unter Benutzung dieses Isomorphismus gilt:

$$
e \cdot \rho^ {*} (\mathcal {M}) \subseteq (\omega_ {A / R}) ^ {\otimes r} \subseteq e ^ {- 1} \cdot \rho^ {*} (\mathcal {M}) (\subseteq \rho^ {*} (\mathcal {M}) \otimes_ {R} K).
$$

Beweis. Wir dürfen annehmen, daß $\bar{\psi}\colon 3/\mathbb{Q}\to\bar{A}_{g}/\mathbb{Q}$ sich fortsetzt zu einem eigentlichen $\bar{\psi}\colon 3/\mathbb{Z}\to\bar{A}_{g}/\mathbb{Z}$. Dann gibt es eine endliche Körpererweiterung $K^{\prime}\supseteq K$ (mit ganzen Zahlen $R^{\prime}\subseteq K^{\prime}$), so daß sich $\rho$ liften läßt zu

$$
\tilde {\rho}: \operatorname{Spec} (R ^ {\prime}) \rightarrow 3.
$$

Da über $3 \otimes_{\mathbb{Z}} \mathbb{Q} \bar{\psi}^{*}(\mathcal{M})$ und $\mathcal{L}^{\otimes r}$ isomorph sind, gibt es ein $e_{1}>0$, so daß über 3

$$
e _ {1} \cdot \mathscr {L} ^ {\otimes r} \subseteq \bar {\psi} ^ {*} (\mathscr {M}) \subseteq e _ {1} ^ {- 1} \cdot \mathscr {L} ^ {\otimes r}.
$$

Es reicht, die Behauptung nach dem Basiswechsel zu  $R'$  zu zeigen, und wir müssen nur noch  $\omega_{A/R'}$  und  $\tilde{\rho}^{*}(\mathcal{L})$  vergleichen.

Durch Pullback erhält man eine stabile Kurve

$$
q \colon C \to \operatorname{Spec} (R ^ {\prime})
$$

und

$$
\alpha \colon \operatorname{Pic} ^ {\tau} (C / R ^ {\prime}) \rightarrow A / R ^ {\prime}, \quad \beta \colon A / R ^ {\prime} \rightarrow \operatorname{Pic} ^ {\tau} (C / R ^ {\prime})
$$

mit $\alpha\circ\beta=d\cdot\text{id}$ (Benutze Lemma 1 über $R'$), so daß $\tilde{\rho}^{*}(\mathscr{L})$ das Unterbündel von $A^{\mathrm{g}}q_{*}(\omega_{C/R'})$ ist, welches vom Bild von

$$
\alpha^ {*}: \omega_ {A / R ^ {\prime}} \rightarrow \Lambda^ {g} q _ {*} (\omega_ {C / R ^ {\prime}})
$$

erzeugt wird. Daraus folgt unmittelbar, daß $d^{g} \cdot \bar{\rho}^{*}(\mathcal{L}) \subseteq \omega_{A/R'} \subseteq \bar{\rho}^{*}(\mathcal{L})$, und wir sind fertig.

## § 3. Höhen

Sei $K$ wieder ein Zahlkörper, $R$ der Ring der ganzen Zahlen in $K$. Analog zu [5] definieren wir ein metrisiertes Geradenbündel auf $\operatorname{Spec}(R)$ als einen projektiven $R$-Modul $P$ vom Rang 1, zusammen mit Normen $\| \cdot \|_v$ auf $P \otimes_R K_v$ für alle unendlichen Stellen $v$ von $K$. Dabei bezeichnet $K_v$ die Komplettierung von $K$ in $v$, und wir definieren ein $\varepsilon_v = 1$ oder 2, je nachdem ob $K_v \cong \mathbb{R}$ oder $K_v \cong \mathbb{C}$.

Der Grad des metrisierten Geradenbündels wird definiert als („#“=Ordnung)

$$
\operatorname{Grad} (P, \| \cdot \|) = \log (\# (P / R \cdot p)) - \sum_ {v} \varepsilon_ {v} \cdot \log \| p \| _ {v}.
$$

Dabei ist p ein von Null verschiedenes Element von P, die Summe geht über alle unendlichen Stellen von K, und die rechte Seite ist selbstverständlich unabhängig von p.

Bemerkung. Der Begriff des metrischen Geradenbündels stammt von Arakelov ([2]). Der Grad von P hängt natürlich auch mit dem Volumen von P zusammen.

Uns interessieren besonders die metrisierten Geradenbündel  $\omega_{A/R}$ , wobei

$$
p \colon A \to \operatorname{Spec} (R)
$$

eine semiabelsche Varietät ist, mit eigentlicher generischer Faser A/K. Die Metriken an den unendlichen Stellen kommen vom schon erwähnten Skalarprodukt:

$$
\| \alpha \| _ {v} ^ {2} = \left(\frac {i}{2}\right) ^ {g} \cdot \int_ {A (\bar {K} _ {v})} \alpha \wedge \bar {\alpha}.
$$

Definition. Die modultheoretische Höhe  $h(A)$  ist

$$
h (A) = \frac {1}{[ K : \mathbb {Q} ]} \operatorname{Grad} (\omega_ {A / R}).
$$

Man sieht sofort, daß $h(A)$ invariant ist gegenüber Erweiterungen des Grundkörpers. Der Name „Höhe“ rechtfertigt sich wie folgt:

Im allgemeinen definiert man die Höhe eines Punktes  $x \in \mathbb{P}^{n}(K)$ , indem man x einen Morphismus  $\rho: \operatorname{Spec}(R) \to \mathbb{P}_{\mathbf{Z}}^{n}$  zuordnet, das Bündel  $\mathcal{O}(1)$  auf  $IP_{C}^{n}$  mit einer Metrik versieht, und dann als Höhe von x

$$
\frac {1}{[ K : \mathbb {Q} ]} \cdot \operatorname{Grad} (\rho^ {*} \mathcal {O} (1))
$$

definiert.

Bei Veränderung der hermiteschen Metrik ändert sich die Höhenfunktion nur um einen beschränkten Betrag, und es ist bekannt, daß für jedes c nur endlich viele K-rationale Punkte des  $IP^{n}$  Höhe  $\leq c$  haben. Entsprechende Überlegungen gelten für abgeschlossene Untervariatäten des  $IP^{n}$ . Angewandt auf unsere Situation bettet man wie bisher  $A_{g}$  mittels M in  $IP_{Z}^{n}$  ein. Außerdem hat man schon eine Metrik || || auf dem von M auf  $A_{g}(\mathbb{C})$  induzierten Bündel definiert. Wenn sich diese Metrik auf  $\bar{A}_{\mathrm{g}}(\mathbb{C})$  fortsetzen ließe, so könnte man sie zur Definition der Höhe verwenden, und aus dem Korollar zu Lemma 2 würde folgen, daß für eine semiabelsche Varietät A über R (wie oben), welche über K eine prinzipale Polarisation besitzt und damit ein  $x \in A_{\mathrm{g}}(K)$  definiert,  $h(x)$  und  $r \cdot h(A)$  sich nur um eine beschränkten Betrag unterscheiden.

Leider hat die Metrik $\| \|$ Singularitäten längs $\bar{A}_{g}(\mathbb{C}) - A_{g}(\mathbb{C})$, doch sind diese so mild, daß die fundamentale Endlichkeits-Eigenschaft der Höhe erhalten bleibt:

Definition. Sei $X/\mathbb{C}$ eine kompakte komplexe Varietät, $Y\subseteq X$ eine abgeschlossene Untervarietät, $\mathcal{M}$ eine Geradenbündel auf $X$, $\|\|$ eine hermitesche Metrik auf $\mathcal{M}|X-Y$. Die Metrik $\|\|$ hat logarithmische Singularitäten längs $Y$, wenn folgendes gilt: Es gibt eine eigentliche dominante Abbildung

$$
\phi \colon \tilde {X} \to X,
$$

so daß $\tilde{X}$ glatt und $\phi^{-1}(Y)$ ein Divisor mit normalen Überkreuzungen ist, und so daß für ein lokales Erzeugendes $h$ von $\phi^{*}(\mathcal{M})$ und eine lokale Gleichung $f$ von $\phi^{-1}(Y)$.

$$
\operatorname * {S u p} \left\{\| h \|, \| h \| ^ {- 1} \right\} \leq c _ {1} \cdot | (\log | f |) | ^ {c _ {2}}
$$

(mit Konstanten $c_{1}, c_{2} > 0$) gilt.

Beispiel.

$$
X = \bar {A} _ {g} (\mathbb {C}), \quad Y = \bar {A} _ {g} (\mathbb {C}) - A _ {g} (\mathbb {C}), \quad \mathcal {M} \text {   und   } \| \|
$$

wie bisher.

Dies wurde zwar schon in [6] gezeigt (Ende von §2), doch folgt hier auf Wunsch der Referenten eine kurze Beweisskizze:

Allgemeiner gilt für ein glattes X, einen Divisor Y von X mit normalen Überkreuzungen und eine semiabelsche Varietät

$$
p \colon A \to X,
$$

so daß über X-Y p eigentlich und A prinzipal polarisiert ist, daß die kanonische Metrik auf  $\omega_{A/X}$  logarithmische Singularitäten längs Y hat.

Dazu betrachtet man statt $\omega_{A/X} p_{*}(\Omega_{A/X}^{1})$ („logarithmische Singularitäten“ läßt sich auch für Vektorbündel definieren), und mit den Methoden des §2 reduziert man das Problem auf den Fall, daß $A$ Jacobische einer semi-stabilen Kurve $q\colon C\to X$ ist.

Wir behandeln kurz den Fall einer semi-stabilen Kurve über dem Einheitskreis ID. Der allgemeine Fall geht genauso. Wenn

$$
q \colon C \to \mathbb {D} = \{t | | t | <   1 \}
$$

eine semi-stabile Kurve ist, mit guter Reduktion außerhalb 0, so besitzt C eine Überdeckung

$$
C = \bigcup_ {i = 1} ^ {l} U _ {i},
$$

so daß entweder

a)  $U_{i}=\{(z,t)||z|<1, |t|<1\}$ ,  $q|U_{i}: U_{i}\rightarrow ID$  glatt, z liefert Koordinate auf allen Fasern

oder

$$
\text { b) } U _ {i} = \{(z _ {1}, z _ {2}, t) | | z _ {1} | <   \varepsilon , | z _ {2} | <   \varepsilon , z _ {1} z _ {2} = t ^ {m} \}, q (z _ {1}, z _ {2}, t) = t.
$$

Wenn $\alpha$ ein lokaler Schnitt von $q_{*}(\omega_{C/\mathbb{D}})$ ist, so ist $\alpha$ auf den $U_{i}$ von der Form

a) $\alpha = (\mathrm{holomorph})\cdot dz$ bzw.

$$
\alpha = (\text { holomorph }) \cdot \frac {d z _ {1}}{z _ {1}}.
$$

Eine explizite Rechnung ergibt, daß

$$
\frac {i}{2} \int_ {U _ {i} \cap q ^ {- 1} (t)} \alpha \wedge \overline {{\alpha}}
$$

für  $t \to 0$  entweder beschränkt bleibt, oder höchstens wie  $|\log |t||$  wächst. Außerdem sieht man sofort, daß

$$
\| \quad \| \geq (\text { pos.   Konst. }) \| \| _ {1},
$$

wobei  $\parallel\parallel_{1}$  eine auf ganz X erklärte hermitesche Metrik auf  $q_{*}(\omega_{C/X})$  bezeichnet.

Lemma 3. Sei $X \subseteq \mathbb{P}_{\mathbf{Z}}^{n}$ Zariski-abgeschlossen, $Y \subseteq X$ abgeschlossen, $\| \cdot \|$ eine hermitesche Metrik auf $\mathcal{O}(1)|(X(\mathbb{C}) - Y(\mathbb{C}))$, mit logarithmischen Singularitäten längs $Y$. Für einen Zahlkörper $K$ und $x \in X(K) - Y(K)$ definiert man wie bisher $h(x)$. Dann gibt es für jedes $c$ nur endlich viele $x \in X(K) - Y(K)$ mit $h(x) \leq c$.

Beweis. Sei $\| \cdot \| _1$ eine hermitesche Metrik für $\mathcal{O}(1)|X(\mathbb{C})$, $h_1$ die zugehörige Höhenfunktion, und man wähle ein $s > 0$ und

$$
f _ {1}, \dots , f _ {t} \in \Gamma (X / \mathbb {Z}, \mathcal {O} (s)),
$$

deren gemeinsame Nullstellenmenge genau Y ist. Dann definiert  $\parallel\parallel_{1}$  eine Metrik auf  $\mathcal{O}(s)$  (welche auch  $\parallel\parallel_{1}$  heiße), und aus den Voraussetzungen folgt sofort, daß Konstanten  $c_{1}, c_{2} > 0$  existieren

$$
\text { mit } \log \left| \frac {\| \quad \|}{\| \quad \| _ {1}} (z) \right| \leq c _ {1} + c _ {2} \cdot \inf \{\log (\| \log \| f _ {i} (z) \| _ {1} \|) \}
$$

für  $z \in X(\mathbb{C})$ .

Wenn $x \in X(K) - Y(K)$, entsprechend einem

$$
\rho \colon \operatorname{Spec} (R) \to X,
$$

so definieren die $f_{i}$ Schnitte $\rho^{*}(f_{i})$ von $\rho^{*}(\mathcal{O}(s))$, mit deren Hilfe man die Höhe $h_{1}(x)$ berechnen kann. Da $\|f_{i}(z)\|_{1}$ auf $X(\mathbb{C})$ nach oben beschränkt ist, erhält man sofort Konstanten $c_{3}, c_{4}>0$ mit

$$
| h (x) - h _ {1} (x) | \leq c _ {3} + c _ {4} \cdot \log (h _ {1} (x)).
$$

Daraus folgt unmittelbar die Behauptung.

Wir können nun die Früchte unserer Bemühungen ernten. Das folgende Resultat ist schon fast bewiesen:

Satz 1. Sei c gegeben. Dann gibt es nur endlich viele Isomorphieklassen von Paaren aus

i) einer semiabelschen Varietät der relativen Dimension g

$$
p \colon A \to \operatorname{Spec} (R)
$$

mit eigentlicher generischer Faser A/K

ii) einer prinzipalen Polarisation auf A/K, für welche

$$
h (A) \leq c
$$

gilt.

Beweis. Nach dem Korollar zu Lemma 2 ist die Differenz zwischen $h(x)$ und $r \cdot h(A)$ beschränkt ($x \in A_g(K)$ gehört zu $A$). Nach Lemma 3 liefern die $A$ mit $h(A) \leq c$ somit nur endlich viele verschiedene $x \in A_g(K)$. Wir müssen uns nun noch überlegen, daß nur endlich viele $K$-Isomorphieklassen dieselbe Klasse über dem algebraischen Abschluß $\overline{K}$ induzieren können. Wir fixieren also eine solche Klasse über $\overline{K}$, und betrachten die entsprechenden $A/K$. Es ist bekannt, daß alle diese an denselben Stellen von $K$ schlechte Reduktion haben. Aus dem Lemma 4 weiter unten folgt dann sofort die Existenz einer endlichen Erweiterung $K' \supseteq K$, welche für ein $n \geq 3$ die Koordinaten der $n$-Teilungspunkte aller $A/K$ enthält. Bekanntlich sind dann unsere $A$'s schon über $K'$ isomorph, und der Rest folgt aus allgemeinen Grundsätzen der Galois-Kohomologie.

Es bleibt nachzutragen das

Lemma 4. Sei K ein Zahlkörper, S eine endliche Menge von Stellen von K. Dann gibt es nur endlich viele Körpererweiterungen  $K^{\prime} \supseteq K$  von vorgegebener Ordnung, welche außerhalb von S unverzweigt sind.

Beweis. Bekannt (Hermite-Minkowski).

## § 4. Isogenien

Wir untersuchen das Verhalten von  $h(A)$  unter Isogenien. Wie immer ist K ein Zahlkörper,  $R \subset K$  der Ring der ganzen Zahlen.

Seien

$$
p _ {1} \colon A _ {1} \to \operatorname{Spec} (R)
$$

und

$$
p _ {2} \colon A _ {2} \to \operatorname{Spec} (R)
$$

semiabelsche Varietäten mit eigentlicher generischer Faser,

$$
s \colon \operatorname{Spec} (R) \to A _ {1}
$$

der Nullschnitt, und $\phi: A_{1} \to A_{2}$ eine Isogenie. (Nach Lemma 1 reicht es natürlich, wenn man $\phi$ über $K$ definiert.)

Wir setzen $G = \operatorname{Ker}(\phi) \subseteq A_1$. Da $\phi$ automatisch flach ist, ist $G$ ein quasiendliches flaches Gruppenschema über $\operatorname{Spec}(R)$.

$\phi$  induziert eine Injektion

$$
\phi^ {*}: \omega_ {A _ {2} / R} \rightarrow \omega_ {A _ {1} / R},
$$

und man sieht sofort, daß

$$
\# (\omega_ {A _ {1} / R} / \phi^ {*} (\omega_ {A _ {2} / R})) = \# s ^ {*} (\Omega_ {A _ {1} / A _ {2}} ^ {1}) = \# s ^ {*} (\Omega_ {G / R} ^ {1}).
$$

Da außerdem $\phi^{*}$ die Normen an den unendlichen Stellen um $(\mathrm{Grad}(\phi))^{1/2}$ verändert, folgt unmittelbar

Lemma 5.

$$
h (A _ {2}) = h (A _ {1}) + \frac {1}{2} \log (\operatorname{Grad} (\phi)) - \frac {1}{[ K : \mathbb {Q} ]} \cdot \log (\# s ^ {*} (\Omega_ {G / R} ^ {1})).
$$

Bemerkung. Wenn $G$ von einer Zahl $n\in\mathbb{N}$ annulliert wird, so annulliert $n$ auch $\Omega_{G/R}^{1}$. Daraus folgt, daß

$$
\exp (2 [ K: \mathbb {Q} ] \cdot (h (A _ {2}) - h (A _ {1})))
$$

eine rationale Zahl ist, in deren Zähler und Nenner nur Primteiler von Grad( $\phi$ ) auftauchen. Die Exponenten dieser Primteiler darin können durch ihre Exponenten in Grad( $\phi$ ) beschränkt werden.

Wir untersuchen nun das Verhalten der  $h(A_{n})$ , falls  $A_{n}=A/G_{n}$ , wobei die  $G_{n}$  die Stufen einer l-divisiblen Gruppe  $G\subseteq A[l^{\infty}]$  durchlaufen.

Satz 2. Sei p: $A \to \operatorname{Spec}(R)$ eine semiabelsche Varietät mit eigentlicher generischer Faser, $l$ eine Primzahl, und $G/K \subseteq A[l^{\infty}]/K$ eine $l$-divisible Untergruppe.

Weiter sei $G_{n}$ der Kern von $l^{n}$ auf $G$, und $A_{n}$ die semiabelsche Varietät $A_{n} = A / G_{n}$. Dann ist

$$
h (A _ {n}) = h (A).
$$

Beweis. Seien $v_{1},\ldots,v_{r}$ die über $l$ liegenden Stellen von $k$, $K_{i}=K_{v_{i}}$ die entsprechenden lokalen Körper, $R_{i}\subseteq K_{i}$ die Bewertungsringe, $m_{i}=[K_{i}:\mathbb{Q}_{l}]$, so daß

$$
m = [ K: \mathbb {Q} ] = \sum_ {i = 1} ^ {r} m _ {i}.
$$

Wir wählen ein festes $i$, und betrachten das formale Gruppenschema $\hat{A}$ über $Spf(R_{i})$, die Komplettierung von $A/R_{i}$ längs der Faser $A_{s}$ über dem abgeschlossenen Punkt $s$ von $\operatorname{Spec}(R_{i})$.

$A_{s}$ ist eine Erweiterung $0 \to T_{s} \to A_{s} \to B_{s} \to 0$ mit $T_{s}$ Torus, $B_{s}$ eine abelsche Varietät.

Nach allgemeinen Grundsätzen kann man  $T_{s}$  liften zu einem Torus T über  $\operatorname{Spec}(R_{i})$ , und  $\hat{T}$  ist abgeschlossenes formales Unterschema von  $\hat{A}$ . (Morphismen von  $T_{s}$  in glatte Gruppenschemata können geliftet werden.)

Sei

$$
\hat {H} _ {i} = \hat {A} [ l ^ {\infty} ]
$$

die assoziierte $l$-divisible Gruppe. $\hat{H}_{i}$ ist formale Komplettierung einer $l$-divisiblen Gruppe $H_{i}$ über $R_{i}$, und $H_{i}/K_{i}$ ist eine $l$-divisible Untergruppe von $A[l^{\infty}]/K_{i}$. Dasselbe gilt für $T[l^{\infty}]$, und zu diesen Untergruppen gehören $\mathbb{Z}_{l}$-Untergitter

$$
T _ {l} (T) \subseteq T _ {l} (H _ {i}) \subseteq T _ {l} (A).
$$

Lemma 6. Sei $D_i = \text{Gal}(\overline{K}_i / K_i)$ die absolute Galois-Gruppe von $K_i$, $I_i \subseteq D_i$ die Verzweigungsgruppe.

Dann operiert $I_{i}$ trivial auf $T_{l}(A)/T_{l}(H_{i})$, und die induzierte Operation von $D_{i}/I_{i} \cong \widehat{\mathbf{Z}}$ erfolgt über einen endlichen Quotienten von $\widehat{\mathbf{Z}}$.

Beweis. Sei

$$
\langle , \rangle : T _ {l} (A) x T _ {l} (A) \rightarrow \mathbb {Z} _ {l} (1) = T _ {l} (\mathbb {G} _ {m})
$$

die von einer Polarisation von $A/K$ induzierte symplektische Form. $\langle ,\rangle$ ist nicht ausgeartet, und bekanntlich (SGA VII, Exp. IX, §7) ist

$$
\langle T _ {l} (T), T _ {l} (H _ {i}) \rangle = 0.
$$

Aus Dimensionsgründen ist  $T_{l}(H_{i}) = T_{l}(T)^{\perp}$ , und wir erhalten eine Injektion

$$
T _ {l} (A) / T _ {l} \left(H _ {i}\right) \hookrightarrow \operatorname{Hom} _ {\mathbf {Z} _ {l}} \left(T _ {l} (T), \mathbb {Z} _ {l} (1)\right).
$$

Diese Injektion ist $D_{i}$-linear, und $D_{i}$ operiert in der verlangten Art und Weise auf $\mathrm{Hom}_{\mathbb{Z}_{l}}(T_{l}(T),\mathbb{Z}_{l}(1))$.

Nunmehr zurück zu unserem  $G/K \subseteq A[l^{\infty}]/K$ . Nach Basiserweiterung  $K \subseteq K_{i}$  können wir den Durchschnitt  $G_{i} = G \cap H_{i}$  bilden. Dies ist die maximale l-divisible Untergruppe von  $G_{i}/K_{i}$ , welche sich über  $R_{i}$  ausdehnen läßt, und es ist

$$
\# (s ^ {*} \Omega_ {A / A _ {n}} ^ {1} \otimes_ {R} R _ {i}) = \# s ^ {*} (\Omega_ {(G _ {i}) _ {n} / R _ {i}} ^ {1}).
$$

Nach [13], Proposition 2 kann man dies sofort ausrechnen: Sei $d_{i}$ die Dimension der maximalen formalen Untergruppe von $G_{i}$. Dann ist

$$
\# s ^ {*} (\Omega_ {(G _ {i}) _ {n} / R _ {i}} ^ {1}) = l ^ {n \cdot m _ {i} \cdot d _ {i}}.
$$

Wenn $C_i$ die Komplettierung des algebraischen Abschlusses von $K_i$ bezeichnet, so ist weiter bekannt ([13], Theorem 3, Corollary 2), daß

$$
T _ {l} (G _ {i}) \otimes_ {\mathbb {Z} _ {l}} C _ {i} \cong C _ {i} ^ {h _ {i} - d _ {i}} \oplus C _ {i} ^ {d _ {i}} (+ 1),
$$

$$
(h _ {i} = \text { Höhe } (G _ {i}),  ,, (+ 1) ^ {\prime \prime} = \text { Tate - Twist }) \text {   als   } D _ {i} \text {-Moduln. }
$$

Zusammen mit Lemma 6 ergibt sich daraus, daß $D_{i}$ auf

$$
\begin{array}{c} \Lambda^ {h} T _ {l} (G) \otimes_ {\mathbb {Z} _ {l}} C _ {i} \subseteq \Lambda^ {h} T _ {l} (A) \otimes_ {\mathbb {Z} _ {l}} C _ {i} \\ (h = \mathrm{Höhe} (G)) \end{array}
$$

wie auf

$$
C _ {i} (\chi_ {0} ^ {d _ {1}}) = C _ {i} (d _ {i})
$$

operiert ($\chi_0 =$ zyklotomischer Charakter).

Wir übertragen dies nun wieder auf den globalen Fall:

Es ist

$$
\# s ^ {*} (\Omega_ {A / A _ {n}} ^ {1}) = l ^ {n \sum_ {i = 1} ^ {r} m _ {i} d _ {i}}, \quad (l ^ {n} \cdot \Omega_ {A / A _ {n}} ^ {1} = 0)
$$

und

$$
h (A _ {n}) - h (A) = n \cdot \log (l) \cdot \left(\frac {h}{2} - \sum_ {i = 1} ^ {r} \frac {m _ {i}}{m} \cdot d _ {i}\right).
$$

Wir müssen also zeigen, daß $\sum_{i=1}^{r} m_i d_i = \frac{1}{2} m h$. Dazu betrachten wir die absolute Galois-Gruppe $\tilde{\pi} = \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$, und den $\tilde{\pi}$-Modul

$$
\tilde {V} = \operatorname{Ind} _ {\pi} ^ {\pi} (T _ {l} (A)) \quad (\pi = \operatorname{Gal} (\overline {{{K}}} / K)).
$$

Dieser enthält den Untermodul

$$
\tilde {W} = \operatorname{Ind} _ {\pi} ^ {\tilde {\pi}} (T _ {l} (G))
$$

vom Rang mh, und  $\tilde{\pi}$  operiert auf der Geraden

$$
L = \Lambda^ {m h} (\tilde {W}) \subseteq \Lambda^ {m h} (\tilde {V})
$$

via einen Charakter $\chi\colon\tilde{\pi}\to\mathbb{Z}_{l}^{*}$.

Aus der Klassenkörpertheorie folgt, daß $\chi$ von der Form $\chi=(l$-adische Potenz von $\chi_{0})\cdot(\text{Charakter endlicher Ordnung})$ ist.

Die darin auftretende l-adische Potenz von  $\chi_{0}$  bestimmt sich wie folgt: Sei C die Komplettierung des algebraischen Abschlusses von  $Q_{l}$ ,

$$
D \cong \operatorname{Gal} (\overline {{\mathbb {Q}}} _ {l} / \mathbb {Q} _ {l}) \subseteq \tilde {\pi}
$$

die Zerlegungs-Gruppe von l. Dann gilt als D-Modul

$$
L \otimes_ {\mathbf {Z} _ {i}} C \cong C \left(+ \sum_ {i = 1} ^ {r} m _ {i} d _ {i}\right)
$$

(dies folgt aus unseren vorherigen Berechnungen), und somit ist nach [13], Theorem 2

$$
\chi \cdot \chi_ {0} ^ {- \sum_ {i = 1} ^ {r} m _ {i} d _ {i}}
$$

ein Charakter endlicher Ordnung auf D und auch auf  $\tilde{\pi}$ . Schließlich folgt aus dem schon von Weil bewiesenen Teil der Weil-Vermutungen mit einigen lokalen Überlegungen, daß  $\chi(F_{p})$  (p=Primzahl,  $F_{p}=Frobenius$ ) für fast alle p eine algebraische Zahl ist, all deren Konjugierte Betrag  $p^{\frac{mh}{2}}$  haben. Da  $\chi_{0}(F_{p})=p$ , ist wie verlangt

$$
\sum_ {i = 1} ^ {r} m _ {i} d _ {i} = \frac {m h}{2}.
$$

## § 5. Endomorphismen

Sei K Zahlkörper, A/K eine abelsche Varietät der Dimension g, l eine Primzahl,  $T_{l}=T_{l}(A)$  der Tate-Modul, auf dem  $\pi=\operatorname{Gal}(\overline{K}/K)$  operiert.

Satz 3. Die Operation von $\pi$ auf $T_{l} \otimes_{\mathbf{Z}_{l}} \mathbb{Q}_{l}$ ist halbeinfach.

Satz 4. Die Abbildung

$$
\operatorname{End} _ {\mathbf {K}} (A) \otimes_ {\mathbf {Z}} \mathbb {Z} _ {l} \rightarrow \operatorname{End} _ {\pi} (T _ {l})
$$

ist ein Isomorphismus.

Beweis. Die beiden Sätze werden zusammen bewiesen. Es reicht bekanntlich, statt Satz4 die etwas schwächere Aussage zu beweisen, daß die Abbildung

$$
\operatorname{End} _ {K} (A) \otimes_ {\mathbf {Z}} \mathbb {Q} _ {l} \rightarrow \operatorname{End} _ {\pi} (T _ {l} \otimes_ {\mathbf {Z} _ {l}} \mathbb {Q} _ {l})
$$

bijektiv ist.

Man darf dann zum Beweis den Grundkörper erweitern, oder A durch eine isogene abelsche Varietät ersetzen. Wir können also annehmen, daß A/K prinzipal polarisiert ist, und daß A sich zu einer semiabelschen Varietät über Spec(R) fortsetzt. Dann besitz  $T_{l}$  eine nichtausgeartete schiefsymmetrische Bilinearform. Sei

$$
W \subseteq T _ {l} \otimes_ {\mathbf {Z} _ {l}} \mathbb {Q} _ {l}
$$

ein $\pi$-invarianter maximal isotroper Teilraum. Dem entspricht eine $l$-divisible Untergruppe $G \subseteq A[l^{\infty}]$, und die semiabelschen Varietäten $A_{n} = A / G_{n}$ tragen wieder prinzipale Polarisationen.

Nach Satz 2 ist $h(A_n) = h(A)$, und nach Satz 1 sind unendlich viele $A_n$'s isomorph.

Wie in [16] folgt daraus, daß $W$ Bild eines Idempotents aus $\operatorname{End}_{K}(A) \otimes_{\mathbb{Z}} \mathbb{Q}_{l}$ ist. Der Rest des Beweises geht genauso wie in [16], und sei daher nur skizziert:

Wähle $a, b, c, d \in \mathbb{Q}_l$ mit $a^2 + b^2 + c^2 + d^2 = -1$. Setze

$$
v = \left( \begin{array}{c c c c} a & - b & - c & - d \\ b & a & d & - c \\ c & - d & a & b \\ d & c & - b & a \end{array} \right)
$$

(entsprechend dem Quaternion $a + bi + cj + dk$), so daß $v \cdot {}^t v = -1$. Wenn $W$ ein beliebiger $\pi$-invarianter Teilraum von $T_l \otimes_{\mathbf{Z}_l} \mathbb{Q}_l$ ist, so wendet man obige Überlegungen an auf den maximal isotropen Teilraum

$$
W _ {1} = \{(x, v x) | x \in W ^ {4} \} \oplus \{(y, - v y) | y \in (W ^ {\perp}) ^ {4} \} \subseteq T _ {l} (A) ^ {8} \otimes_ {\mathbf {Z} _ {l}} \mathbf {Q} _ {l}.
$$

Korollar 1. Seien $A_{1}$ und $A_{2}$ abelsche Varietäten über $K$. Dann ist

$$
\operatorname{Hom} _ {K} (A _ {1}, A _ {2}) \otimes_ {\mathbb {Z}} \mathbb {Z} _ {l} \rightarrow \operatorname{Hom} _ {\pi} (T _ {l} (A _ {1}), T _ {l} (A _ {2}))
$$

ein Isomorphismus.

Beweis. Satz 4 für $A_{1} \times A_{2}$.

Die L-Reihe eines A's ist bekanntlich definiert als

$$
L (A, s) = \prod_ {v} \frac {1}{\det (1 - (N _ {v}) ^ {- s} \cdot F _ {v} | T _ {l} (A))} = \prod_ {v} L _ {v} (A, s),
$$

wobei das Produkt über fast alle Stellen von K zu erstrecken ist. Die lokalen L-Faktoren  $L_{v}(A,s)$  sind unabhängig von l.

Korollar 2. Seien $A_{1}, A_{2}$ wie im Korollar 1. Es sind äquivalent

i) $A_{1}$ und $A_{2}$ sind isogen.

ii) $T_{l}(A_{1})\otimes_{\mathbf{Z}}\mathbb{Q}_{l}\cong T_{l}(A_{2})\otimes_{\mathbf{Z}}\mathbb{Q}_{l}$ als $\pi$ -Modul.

iii) $L_{v}(s,A_{1}) = L_{v}(s,A_{2})$ für fast alle Stellen $v$ von $K$.

iv) $L_{v}(s,A_{1}) = L_{v}(s,A_{2})$ für alle $v$.

Beweis. Die Äquivalenz von i) und ii) folgt aus Satz 4, die von ii) und iii) aus Satz 3 (+Čebotarev), und aus ii) folgt iv) folgt iii) ist trivial.

Korollar 3. Sei A/K eine abelsche Varietät, d>0. Dann gibt es nur endlich viele Isomorphieklassen d-fach polarisierter abelscher Varietäten B/K, so daß für alle l  $T_{l}(A)\cong T_{l}(B)$ .

Beweis. Die Voraussetzung besagt, daß zu jedem l eine Isogenie vom Grad prim zu l zwischen A und B existiert. Wir dürfen weiter den Grundkörper K zum Beweis erweitern, und dann annehmen, daß A und alle B's sich zu semiabelschen Varietäten über Spec(R) fortsetzen, und daß es für alle B's eine Isogenie vom Grad  $\sqrt{d}$  mit einer prinzipal polarisierten abelschen Varietät gibt. Man kommt dann leicht auf folgende Voraussetzungen:

a) alle B's haben semistabile Reduktion,

b) alle B/K sind prinzipal polarisiert,

c) es gibt ein N, so daß für jede Primzahl l und alle B's Isogenien  $\phi: A \to B$  existieren, für die die größte l-Potenz in  $\text{Grad}(\varphi)$  N teilt.

Die Bemerkung nach Lemma 5 zeigt dann, daß $\exp(2[K:\mathbb{Q}](h(B)-h(A))$ eine rationale Zahl ist, deren Zähler und Nenner durch eine geeignete Potenz von $N$ abgeschätzt werden kann.

Also sind die  $h(B)$  beschränkt, und man kann Satz 1 anwenden.

## § 6. Endlichkeitssätze

Satz5. Sei S eine endliche Menge von Stellen von K. Dann gibt es nur endlich viele Isogenie-Klassen abelscher Varietäten vorgegebener Dimension über K, welche gute Reduktion außerhalb S haben.

Beweis. Sei A eine solche abelsche Varietät. Nach den Weil-Vermutungen gibt es für  $v \notin S$  nur endlich viele Möglichkeiten für den lokalen L-Faktor  $L_{v}(A, s)$ . Wir werden endlich viele Stellen  $v_{1}, \ldots, v_{r}$  konstruieren, so daß zwei A's schon isogen sind, wenn sie an diesen Stellen denselben lokalen L-Faktor haben. Dazu wähle man eine Primzahl l. Nach Lemma 4 existiert eine endliche Galois-Erweiterung  $K' \supseteq K$ , welche alle außerhalb l und S unverzweigten Körpererweiterungen von K vom Grad  $\leq l^{8g^{2}}$  umfaßt ( $g = \dim(A)$ ).

Sei $G=\mathrm{Gal}(K'/K)$; und man wähle $v_{1},\ldots,v_{r}$ so daß jede Konjugationsklasse in $G$ das Bild eines Frobenius $F_{v}$ für $v\in\{v_{1},\ldots,v_{r}\}$ enthält (Čebotarev). Dann erfüllen $v_{1},\ldots,v_{r}$ unsere Forderungen: Seien $A_{1},A_{2}$ zwei abelsche Varietäten über $K$, welche denselben lokalen $L$-Faktor an $v_{1},\ldots,v_{r}$ haben.

Sei

$$
M \subseteq \operatorname{End} _ {\mathbf {Z} _ {l}} (T _ {l} (A _ {1})) \times \operatorname{End} _ {\mathbf {Z} _ {l}} (T _ {l} (A _ {2}))
$$

die  $Z_{l}$ -Unteralgebra, die vom Bild von  $\pi$  erzeugt wird.

Dann ist $M$ freier $\mathbb{Z}_{l}$-Modul vom $\operatorname{Rang} \leq 8g^{2}$, und $M$ besitzt Darstellungen auf $T_{l}(A_{1})$ und $T_{l}(A_{2})$.

Wir müssen zeigen, daß für jedes  $m \in M$

$$
\operatorname{Spur} (m \mid T _ {l} (A _ {1})) = \operatorname{Spur} (m \mid T _ {l} (A _ {2})).
$$

Es reicht natürlich, dies für m aus einer  $Z_{l}$ -Modulbasis von M zu zeigen, und nach Voraussetzung gilt die Gleichheit schon, wenn m Bild eines Elements aus

der Konjugationsklasse von  $F_{v}$  ist, für  $v \in \{v_{1}, \ldots, v_{r}\}$ . Wir zeigen, daß diese Bilder M über  $Z_{l}$  erzeugen. Nach Nakayama reicht es, wenn sie M/lM erzeugen. Dies gilt aber aus folgendem Grund:

Wir haben eine Darstellung

$$
\rho \colon \pi \rightarrow (M / l M) ^ {*} = \text { Einheiten   von } M / l M,
$$

deren Bild M/lM erzeugt.

Da

$$
\# (M / l M) ^ {*} \leq l ^ {8 g ^ {2}},
$$

faktorisiert $\rho$ über $G$, und $\rho(\pi)$ ist die Vereinigung der Bilder der Konjugationsklassen der $F_{v}$, $v\in\{v_{1},\ldots,v_{r}\}$.

Satz 6 (Shafarevich-Vermutung). Sei S eine endliche Menge von Stellen von K, d>0. Dann gibt es nur endlich viele Isomorphie-Klassen d-fach polarisierter abelscher Varietäten über K von vorgegebener Dimension, welche außerhalb S gute Reduktion haben.

Beweis. Nach Satz 5 nehmen wir an, daß die betrachteten abelschen Varietäten B/K alle isogen zu einem festen A/K sind. Wie im Beweis des Korollar 3 zu Satz 4 dürfen wir weiter voraussetzen, daß sich alle B's zu semiabelschen Varietäten über Spec(R) fortsetzen, und daß d=1 ist. Wir wissen schon, daß

$$
\exp (2 [ K: \mathbb {Q} ] (h (B) - h (A)))
$$

eine rationale Zahl ist. Wir werden ein N konstruieren, so daß Zähler und Nenner dieser rationalen Zahl keine Primfaktoren l>N besitzen, und daß die auftretenden l-Potenzen für Primzahlen  $l \leq N$  beschränkt sind.

Das letztere ist ganz einfach:

Wenn für zwei abelsche Varietäten  $B_{1}/K$  und  $B_{2}/K$$T_{l}(B_{1})$  und  $T_{l}(B_{2})$  als  $\pi$ -Moduln isomorph sind, so existiert nach Satz4 eine Isogenie vom Grad prim zu l zwischen  $B_{1}$  und  $B_{2}$, und l tritt nicht in

$$
\exp (2 [ K: \mathbb {Q} ] (h (B _ {1}) - h (B _ {2})))
$$

auf.

Es reicht also, wenn es nur endlich viele Isomorphie-Klassen $\pi$-invarianter Gitter in $T_{l}(A)\otimes_{\mathbb{Z}_{l}}\mathbb{Q}_{l}$ gibt. Dazu sei $M_{l}$ die von $\pi$ erzeugte $\mathbb{Z}_{l}$-Unteralgebra von $\operatorname{End}_{\mathbb{Z}_{l}}(T_{l}(A))$. Es folgt dann alles aus der Tatsache, daß $M_{l}\otimes_{\mathbb{Z}_{l}}\mathbb{Q}_{l}$ halbeinfach ist (Satz 3).

Wir kommen nun zur Wahl von N. Dazu sei n das Produkt der Primzahlen l, für welche entweder die Erweiterung  $K \supseteq Q$  in l verzweigt, oder A nicht gute Reduktion an allen Stellen der Charakteristik l hat.

Wähle eine Primzahl p, welche n nicht teilt. Sei wieder

$$
\tilde {\pi} = \operatorname{Gal} (\overline {{{\mathbb {Q}}}} / \mathbb {Q}) \supseteq \pi = \operatorname{Gal} (\overline {{{K}}} / K),
$$

und, für $0 \leq h \leq 2gm$ ($g = \dim(A)$, $m = [K: \mathbb{Q}]$), sei

$$
P _ {h} (T) = \det \left[ T - F _ {p} | \Lambda^ {h} (\operatorname{Ind} _ {\tilde {\pi}} ^ {\pi} (T _ {l} (A))) \right].
$$

Dabei ist l eine zu pn prime Primzahl, und  $F_{p}$  bezeichnet den Frobenius an der Stelle p.

Die  $P_{h}(T)$  sind unabhängig von l, haben Koeffizienten in Z, und ihre Nullstellen haben absoluten Betrag  $p^{+\frac{h}{2}}$  (Weil-Vermutung oder besser -Satz).

Wir wählen nun  $N \geq 2$  so groß, daß keine Primzahl  $l > N$$P_{h}(\pm p^{j})$  teilt, falls

$$
\begin{array}{l} 0 \leq h \leq 2 g m \\ 0 \leq j \leq g m \\ j \neq \frac {1}{2} h. \end{array}
$$

Außerdem sei $N \geq np$.

Wir werden zeigen, daß für jede Isogenie

$$
\phi \colon B _ {1} \to B _ {2}
$$

von zu A isogenen abelschen Varietäten, deren Grad eine l-Potenz mit einer Primzahl l>N ist,  $h(B_{1})$  und  $h(B_{2})$  übereinstimmen. Dies geht ähnlich wie beim Beweis des Satzes 2: Wir dürfen annehmen, daß l den Kern G von  $\phi$  annuliert. Sei

$$
\begin{array}{l} V _ {l} = T _ {l} (B _ {1}) / l \cdot T _ {l} (B _ {1}) \cong B _ {1} [ l ] (\overline {{K}}), \\ \tilde {V} _ {l} = \mathrm{Ind} _ {\pi} ^ {\pi} (V), \\ W _ {l} = G (\overline {{K}}) \subseteq V _ {l} \\ \tilde {W} _ {l} = \mathrm{Ind} _ {\pi} ^ {\pi} (W _ {l}) \subseteq \tilde {V} _ {l}. \end{array}
$$

Wenn $\phi$ die Ordnung $l^h$ hat, so operiert $\tilde{\pi}$ auf

$$
L = \Lambda^ {m h} (\tilde {W} _ {l}) \subseteq \Lambda^ {m h} (\tilde {V} _ {l})
$$

via einen Charakter $\chi\colon\tilde{\pi}\to(\mathbb{Z}/l\mathbb{Z})^{*}$.

Wenn $\varepsilon\colon\tilde{\pi}\to\{\pm1\}$ den Charakter bezeichnet, mit dem $\tilde{\pi}$ auf $A^{m}\operatorname{Ind}_{\pi}^{\tilde{\pi}}(\mathbb{Z})$ operiert, so ist $\chi\cdot\varepsilon^{h}$ unverzweigt außerhalb $l$, denn die Trägheitsgruppen der Stellen $v$ von $K$, welche $l$ nicht teilen, operieren unipotent auf $V_{l}$ (semistabile Reduktion). Nach der Klassenkörpertheorie ist $\chi\cdot\varepsilon^{h}$ eine Potenz des zyklotomischen Charakters $\chi_{0}$. Diese Potenz läßt sich mit Hilfe von [10], Théorème 4.11 (statt der Tateschen Theorie [13]) wie folgt bestimmen:

Sei

$$
\begin{array}{l} l ^ {d} = \# s ^ {*} (\Omega_ {G / R} ^ {1}), \\ 0 \leq d \leq g m. \end{array}
$$

Dann ist (nach Raynaud) $\chi \cdot \varepsilon^{h} = \chi_{0}^{+d}$. Also ist

$$
\chi_ {0} ^ {d} (F _ {p}) = \pm p ^ {d}
$$

eine Nullstelle von $P_{mh}(T)$ modulo $l$, und nach Wahl von $N$ muß $d=\frac{hm}{2}$ gelten. Da wieder

$$
h (B _ {2}) - h (B _ {1}) = \log (l) \left(\frac {h}{2} - \frac {d}{m}\right),
$$

folgt unsere Behauptung, und es ergibt sich, daß die  $h(B)$ 's der betrachteten B's beschränkt sind. Damit folgt Satz6 aus Satz1.

Korollar 1. Es gibt nur endlich viele Isomorphie-Klassen glatter Kurven X/K vom Geschlecht g≥2, welche außerhalb S gute Reduktion haben.

Beweis. Torelli.

Satz 7 (Mordell-Vermutung). Sei X/K eine glatte Kurve vom Geschlecht  $g \geq 2$ . Dann ist  $X(K)$  endlich.

Beweis. Dies steht in [9]: Nach eventueller Erweiterung des Grundkörpers gibt es eine unverzweigte Überlagerung vom Grad m>2:

$$
\phi \colon X _ {1} \to X.
$$

Lemma 4 liefert einen endlichen Oberkörper $K_{1} \supseteq K$, so daß für jedes $x \in X(K)$$\phi^{-1}(x)$ aus $m$ verschiedenen $K_{1}$-rationalen Punkten besteht. Man wähle einen davon aus, etwa $y \in p^{-1}(x)$.

Sei  $D=\phi^{-1}(x)-\{y\}$ , und  $A/K_{1}$  die verallgemeinerte Jacobische zu dem Paar  $(X_{1},D)$ . Mit Hilfe von y konstruiert man eine Abbildung von  $X_{1}-D$  nach A.

Die Multiplikation mit 2 auf A induziert dann eine genaue über D verzweigte Überlagerung  $Y(x) \to X_{1}$ , wobei die Kurve  $Y(x)$  nur an solchen Stellen v von  $K_{1}$  schlechte Reduktion haben kann, für die eine der drei folgenden Bedingungen gilt:

a) v teilt 2.

b) $X_{1}$ hat schlechte Reduktion in $v$.

c) $\phi$ verzweigt in der Faser mod $v$.

Dies sind nur endlich viele Stellen, und es gibt somit nur endlich viele Möglichkeiten für  $Y(x)$ .

Dasselbe gilt für die Abbildung  $Y(x) \to X_{1} \to X$ , welche genau über x verzweigt. Es folgt die Behauptung.

Bemerkungen. 1. Man erhält auf diesem Wege auch einen Beweis des Siegelschen Satzes (über ganze Punkte), welcher ohne diophantische Approximation auskommt.

2. Mit Hilfe der Methode aus [16] kann man aus Satz 6 folgern, daß für fast alle Primzahlen $l$ die von $\pi$ erzeugte Unteralgebra $M_{l}$ von $\operatorname{End}_{\mathbb{Z}_{l}}(T_{l}(A))$ der volle Kommutator von $\operatorname{End}_{K}(A)\otimes_{\mathbb{Z}}\mathbb{Z}_{l}$ ist.

## Literatur

1. Arakelov, S.: Families of curves with fixed degeneracies. Math. USSR Izvestija 5, 1277-1302 (1971)

2. Arakelov, S.: An Intersection theory for divisors on an arithmetic surface. Math. USSR Izvestija 8, 1167-1180 (1974)

3. Baily, W.L., Borel, A.: Compactification of arithmetic quotients of bounded symmetric domains. Ann. of Math. 84, 442-528 (1966)

## Zusatz bei der Korrektur

Herr O. Gabber hat mir mitgeteilt, daß der Beweis von Satz 2 nicht ganz korrekt ist. Man erhält nur, daß die Folge $h(A_{n})$ stationär wird. Dies reicht für unsere Zwecke.