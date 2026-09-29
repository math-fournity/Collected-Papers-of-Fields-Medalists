# 100 Years of the (Critical) Ising Model on the Hypercubic Lattice

Hugo Duminil-Copin

Dedicated to the memory ofcolleagues andfriends Dmitry Iofe and Vladas Sidoravicius

## Abstract

We take the occasion of this article to review one hundred years of the physical and mathematical study of the Ising model. The model, introduced by Lenz in 1920, has been at the cornerstone of many major revolutions in statistical mechanics. We wish, through its history, to outline some of these amazing developments. We restrict our attention to the ferromagnetic nearest-neighbour model on the hypercubic lattice, and essentially focus on what happens at or near the so-called critical point.

Mathematics Subject Classification 2020 Primary 82B20; Secondary 60K35

Keywords Ising model, percolation theory, phase transition, statistical mechanics

## 1. Short motivation

How to provide an introduction to (part of) statistical physics aimed at a wide audience of mathematicians? The question is not easy, especially since the domain is positioned halfway between theoretical physics and mathematics, and that contrarily to (some) other fields of mathematics, it is hard to identify a theory that would embrace most of statistical physics. A partial answer may be to follow the standard approach of teaching by examples, and to pick what is maybe the most classical model of statistical physics, namely the Ising model. Through its history, one may trace many of the revolutions, both on the theoretical physics and mathematical sides, that statistical physics underwent in the last century.

We therefore chose to streamline this history, from the emergence of the model to explain experimental results, to its modern applications in mathematics, physics, and beyond. Obviously, the story will be tainted by the expertise of the author since thousands of papers have been published on the subject, which ranges over many subfields of mathematics and theoretical physics. A subjective selection of papers has therefore been made, and the attention has been restricted to the model on the hypercubic lattice, at equilibrium, (for most of the review) at criticality, and always with nearest neighbour ferromagnetic interactions (we are well aware that non-critical and dynamical aspects, as well as long-range, random, or antiferromagnetic interactions also are of prime importance).

We tried to respect the timing of the appearance of the diferent notions pertaining to the model, and avoided as much as possible some tempting anachronisms. As a result, certain readers may be surprised by some statements, knowing that simpler and more natural versions exist nowadays. Also, the large number of breakthroughs in the Ising model’s history – Peierls’ argument, Onsager’s solution on the square lattice and the exact integrability results that followed, Kadanof’s scaling and universality hypotheses, the Lee-Yang theorem, correlation inequalities, the Fortuin-Kasteleyn representation, reflection positivity, Aizenman’s treatment of the random current representation and use of diferential inequalities, conformal field theory, rigorous renormalisation group, Chelkak-Smirnov’s conformal invariance, 3D conformal bootstrap, to cite but a few – forced us to be very quick on some of these developments. References are added for the avid reader. We also refer to [20,86] for historical introductions, and [48] for a book on statistical physics including a study of the Ising model.

## 2. The first twenty years: a laborious start

## 2.1. Ising model’s prehistory

The story starts with the French physicist Pierre Curie [30], who noticed that magnets lose their magnetic attraction when they are heated above a certain critical temperature, now called the Curie temperature. While the Curie temperature varies from slightly over 100 degrees Celsius for certain alloys, to 769.85 degrees Celsius for magnets made of iron, the underlying phenomenon is always the same: at a certain temperature, a magnet ceases to be able to keep a spontaneous magnetisation and exhibits magnetisation only when an external field is applied to it. This phenomenon is called a phase transition between a paramagnetic phase above the Curie temperature, and a ferromagnetic phase below it.

Curie also identified a law, now called Curie’s law, relating the magnetic susceptibility of the system to the temperature and the external magnetic field applied to the magnet. He noticed the similarity between the ferromagnetic and paramagnetic phases of a magnet in terms of the temperature and the external magnetic field applied to it, and respectively the liquid and gas phases of a fluid in terms of the pressure and temperature. Pierre Weiss [101] tried to produce an eficient physical explanation of this phenomenon by introducing an assumption, referred to today as the mean-field approximation. This mean-field model, called the Curie-Weiss model, gave rise to an interesting yet not fully accurate description of the phase transition.

The German physicist Wilhelm Lenz got interested in Curie’s law. Lenz agreed with one of Weiss’ suggestions that magnets are made of elementary pieces that behave themselves as small magnets. Yet, he was at the same time in line with his contemporary physicists, thinking that one of Weiss’ assumption, namely that elementary magnets can rotate freely within a solid, was wrong. Taking this into account, he challenged the rotational freeness. Observing that a crystal selects certain directions corresponding to its symmetries, he made the assumption that elementary magnets also behave in this way. By analogy, he then suggested that a crystal-like mechanism for magnets should favour that neighbouring elementary magnets are aligned, therefore corresponding to either pointing in the same or opposite directions. At the end, the reasoning of Lenz led to the assumption that elementary magnets were taking only two possible directions that are opposite of each other. He formalized this reasoning in [80].

At this stage, Lenz did not propose an explicit form for the interaction between elementary magnets. Also, the paper approximately explained the typical behaviour of a paramagnet having respectively zero magnetisation when no magnetic field is applied, and a magnetisation when such a magnetic field is applied, but Lenz made no mention of what will later be referred to as the ferromagnetic behaviour.

Ernst Ising was a German physicist born in 1900, who was a PhD student of Lenz in Hamburg. He graduated in 1924 and published a paper [70] on Lenz’s model in 1925. So, what did Ising actually achieve in his famous paper from 1925?

First of all, he went one step further than Lenz by specifying the interaction between elementary magnets. He first made the assumption that interactions "decay rapidly with distance, so that we, in general, to a first approximation, only have to take the influence on neighbouring elements into account". He also assumed that "of all the possible positions that the neighbouring atoms can assume in relation to each other, the one that requires the minimum energy is when they are both acting in the same direction". These two assumptions led to the mathematical model that we will define formally in the next section. In order to treat this model, Ising made a further assumption: he assumed that the elementary magnets are positioned on a linear chain.

From all of this, Ising could deduce Curie’s law in the paramagnetic phase. While this was a source for optimism, the latter was severely challenged by the observation that the magnetisation was tending to 0 as the magnetic field vanishes, irrespective of the temperature. In other words, no explanation for ferromagnetism was in sight. Even worse, despite a few attempts at generalising the model (Ising considered non-nearest neighbour interactions, more possible directions for the elementary magnets, and a hybrid three dimensional model that would correspond to a limit in which only pairs of neighbouring elementary magnets in one direction truly interact), the ferromagnetism did not seem to be explainable. This led Ising to conjecture that the model was not a good explanation for ferromagnetism (even when considering higher dimensional base graph for the spins), a thought that he gathered in a letter to American historian Stephen Brush years later: "I discussed the result ofmy paper widely with Professor Lenz and with$D r$Wolfgang Pauli, who at that time was teaching in Hamburg. There was some disappointment that the linear model did not show the expected ferromagnetic properties."

After his PhD, Ising left academia to become a teacher in Germany before being forced to step down due to his Jewish origins. He fled Nazi Germany and emigrated to the United States, where he became a Professor in Physics at Bradley University. He never published after his first original paper, and only later became aware of how famous the model had grown into.

## 2.2. Formal definition

Let us turn to the formal definition ofthe model for our magnet. Consider a finite non-oriented subgraph$G = ( V , E )$of the hypercubic lattice$\mathbb { Z } ^ { d }$with vertex-set � corresponding to the position of its elementary magnet constituents, and edge-set � modeling the links between neighbouring ones. An edge$e \in E$is often written$e = \{ x , y \}$, where � and � are its endpoints. The elementary magnet at$x \in V$will be a quantity$\sigma _ { x } \in \{ - 1 , + 1 \}$, where −1 and +1 correspond to the two opposite directions that it may take. The value$\sigma _ { x }$is called the spin at �, and the collection$( \sigma _ { x } : x \in V ) \in \{ - 1 , 1 \} ^ { V }$of all spins at vertices in � is called the spin configuration, and should be understood as the state of our magnet.

The energy – or Hamiltonian – of a configuration$\sigma$on$G$is given by

$$
H _ {G, h} (\sigma) := - \sum_ {\{x, y \} \in E} \sigma_ {x} \sigma_ {y} - h \sum_ {x \in V} \sigma_ {x},\tag{2.1}
$$

where$h \in \mathbb { R }$is called the magneticfield. Sometimes, one may want to generalise the mode to accommodate non-nearest neighbour and non-ferromagnetic interactions by setting

$$
H _ {G, h, (J _ {x, y})} (\sigma) := - \sum_ {x, y \in V} J _ {x, y} \sigma_ {x} \sigma_ {y} - h \sum_ {x \in V} \sigma_ {x}\tag{2.2}
$$

where the$( J _ { x , y } : x , y \in V )$are called the coupling constants of the model. Except when otherwise stated, we focus here on the Hamiltonian$H _ { G , h }$corresponding to what is called the nearest neighbourferromagnetic (n.n.f.) Ising model on �.

Following Boltzmann, one considers the (grand) partition function of the Ising model on � at inverse-temperature$\beta$and magnetic field ℎ defined by

$$
Z (G, \beta , h) := \sum_ {\sigma \in \{- 1, 1 \} ^ {V}} \exp [ - \beta H _ {G, h} (\sigma) ].\tag{2.3}
$$

The quantity$\beta$is interpreted as the inverse of the temperature, as the latter corresponds to the thermal excitation of elementary magnets, for which it is natural to predict that the larger their excitation, the less relevant their interaction.

Physicists then consider the linear form defined for every function$X : \{ - 1 , 1 \} ^ { V } \to \mathbb { R }$ by the formula

$$
\langle X \rangle_ {G, \beta , h} := \frac {1}{Z (G , \beta , h)} \sum_ {\sigma \in \{- 1, 1 \} ^ {V}} X (\sigma) \exp [ - \beta H _ {G, \beta , h} (\sigma) ].\tag{2.4}
$$

At this stage, we do not consider$\langle \cdot \rangle _ { G , \beta , h }$itself, and instead focus on a thermodynamical quantity of the system called the free energy. Consider a box$\Lambda _ { n } : = [ - n , n ] ^ { d } \cap \mathbb { Z } ^ { d }$ and define thefree energy of the �-dimensional Ising model by the formula

$$
f (\beta , h) := - \frac {1}{\beta} \lim _ {n \rightarrow \infty} \frac {1}{| \Lambda_ {n} |} \ln Z (\Lambda_ {n}, \beta , h)\tag{2.5}
$$

(the existence of the limit is justified by a sub-additivity argument left to the reader).

Originally, Lenz and Ising were interested in a quantity

$$
m (\beta , h) := - \frac {\partial}{\partial h} f (\beta , h),\tag{2.6}
$$

which is interpreted as the magnetisation of the system in the presence of a magnetic field of strength ℎ. One may then define the spontaneous magnetisation, which corresponds to the remaining magnetisation when removing the magnet from the ambient magnetic field,

$$
m ^ {*} (\beta) := \lim _ {h \searrow 0} m (\beta , h)\tag{2.7}
$$

(to justify the limit, one may prove that �$( \beta , h )$decreases as ℎ decreases). The cases$m ^ { * } ( \beta ) =$ 0 and$m ^ { * } ( \beta ) > 0$are respectively called the paramagnetic and ferromagnetic cases as they correspond to the cases where the magnet respectively loses or keeps its magnetisation even without external magnetic field.

## 2.3. What does the Ising model truly model?

The Ising model did not develop quickly after its introduction. The original paper was cited very sporadically in the ten years that followed. In fact, Ising himself was aware of one citation to his paper only, and this lack of interest was one of the reasons that pushed him to abandon academia.

There are several explanations why the paper received little attention. The first one is that the negative result of the paper, stating that the model did not explain ferromagnetism, was a pretty disappointing one. The second is a timing problem. A few years after Ising’s paper, Heisenberg introduced another model of ferromagnetism [63] based on quantum mechanics, in which the “classical” spins of the Ising model are replaced by the quantum spins of electrons. In other words, Heisenberg’s model tries to explain ferromagnetism via the interaction of the spin angular momentum of the electrons in the atoms, while the Ising model was relying on their magnetic moments. In a certain sense, the Ising model was a semi-classical version of Heisenberg model, and as such was violating the latest developments of quantum mechanics. The discrepancy between the great predictive successes of the Heisenberg model, and the impossibility to reconcile the Ising model with the recent advancements in modern physics almost entirely disqualified the model as a good description of ferromagnetic materials.

At this point, one may wonder why this model, initially introduced in theoretical physics to explain ferromagnetism but seemingly failed to do so, did not simply fall into darkness after this rocky start. An element of answer can be found in the developments of other fields of physics, which we now review.

In 1919, the Russian-German chemical physicist Gustav Tamman presented an interesting experiment in which atoms in alloys of copper and gold tend to be surrounded by atoms of the other kind (to picture this, think of a chessboard colouring of the square lattice). In Tamman’s experiment, the thermal agitation has a direct impact on how much the atoms tend to be in the right places. In 1935, Bragg and Williams [19] explained this phenomenon by a statistical mechanics’s argument involving the energy cost of having an atom in the wrong place. Hans Bethe simplified the model by assuming that only nearest atoms interact.

In 1936, Ralph Fowler and his team in Cambridge introduced another theoretical model to understand the adsorption of metal vapour on a glass. Fowler more generally identified a class of experiments exhibiting similar behaviours, that he named cooperative phenomena.

The German theoretical physicists RudolfPeierls later noticed the similarity between Bethe’s approximation of the Bragg-Williams model, Fowler’s theory of adsorption, and the Ising model. While the original physical problems are diferent, the mathematical treatment is in fact similar. In retrospect, Peierls was perhaps the first person to identify that the Ising model could treat a number of diferent phenomena, even though the model was a coarse caricature for each one of the phenomena in question.

This observation was maybe what kept the Ising model alive for some years, but it is mathematics that truly changed the nature of the model and made it what it is today. We now turn to the first mathematical breakthrough in the model.

## 2.4. Peierls’ argument

While Peierls agreed with the majority ofthe physics community that the Ising model was not a good model for ferromagnetism, he certainly recognised that the model was ofmathematical interest. Furthermore, he totally disagreed with the naive generalisation, based on the few attempts of Ising, of the absence of a ferromagnetic phase to higher dimensional lattices. This led him to reconsider the problem of the Ising model in two and three dimensions. As a result, he produced what is probably one of the most important papers in the early Ising history [90], in which he developed a technique which is now widely known in statistical physics as Peierls’ argument.

Roughly speaking, the argument runs as follows. When considering a configuration $\sigma$of the Ising model on${ \mathbb { Z } } ^ { 2 }$, or a finite subgraph of it, one may associate a subset �(�) composed of the edges$\{ x , y \}$of the graph with$\sigma _ { x } \neq \sigma _ { y }$. In a planar context, one may draw these edges$e \in E ( \sigma )$by considering the dual edges$( e ^ { \ast } : e \in E ( \sigma ) )$on the dual graph1; see Figure 1. These dual edges and their endpoints form an even subgraph of the dual graph (call Even$( G ^ { * } )$the set of such even subgraphs) which can be interpreted as a collection of loops on the dual graph. The representation of configurations$\sigma$in terms of even subgraphs is called the low-temperature expansion. Using the mapping between$\sigma$and$E ( \sigma )$, one may rewrite the partition function as

$$
Z (G, \beta , 0) = \sum_ {\sigma \in \{- 1, 1 \} ^ {V}} e ^ {- \beta H _ {G, h} (\sigma)} = e ^ {\beta | E (G) |} \sum_ {F \in \operatorname{Even} (G ^ {*})} e ^ {- 2 \beta | F |}.\tag{2.8}
$$

This formula immediately highlights the fact tha$\boldsymbol { \cdot } \beta$large renders configurations$F \in \operatorname { E v e n } ( G ^ { * } )$ with large loops unlikely. Building on this observation, Peierls was able to obtain that $m ^ { * } ( \beta ) > 0$for large values of$\beta ,$, see Frame 1 for more details.

The idea to introduce a model of “domain walls” separating the diferent phases (here pure +1 and pure −1) from each other is not restricted to the Ising model: it has been very fruitful to prove the existence of phase transitions, and Peierls’ argument is now one of the most famous and robust arguments in statistical physics.

## Frame 1: a quick version of Peierls’ argument

We do not consider the magnetization$m ^ { * } ( \beta )$but rather the correlation $\langle \sigma _ { 0 } \sigma _ { \mathbf { g } } \rangle _ { \Lambda _ { n } ^ { + } , \beta , 0 }$, where${ \Lambda } _ { n } ^ { + }$is the graph$\Lambda _ { n }$plus a vertex$\mathbf { g } ,$sometimes referred to as Griffiths’ “ghost” vertex, connected to all the vertices on the boundary of$\Lambda _ { n }$; see Figure 1 on the left. The limit as � tends to infinity can be shown to be$m ^ { * } ( \beta )$, so it is suficient to prove that the quantity is bounded away from 0 uniformly in$n .$

If one denotes by$\mathbf { C } = \mathbf { C } ( \sigma )$the connected component of 0 in$\mathbb { R } ^ { 2 } \setminus \{ e ^ { * } : e \in$ $E ( \sigma ) \}$, one may decompose the magnetisation depending on the value of C to get

$$
\langle \sigma_ {0} \sigma_ {\mathbf {g}} \rangle_ {\Lambda_ {n} ^ {+}, \beta , 0} = 1 - 2 \sum_ {\mathbf {g} \notin C \in \mathrm{Even} ((\Lambda_ {n} ^ {+}) ^ {*})} \langle \mathbb {I} (\mathbf {C} = C) \rangle_ {\Lambda_ {n} ^ {+}, \beta , 0}.\tag{2.9}
$$

Now things become interesting. For every$C \ \not \ni \ \mathbf { g } ,$consider the configuration$\operatorname { F l i p } _ { C } ( \sigma )$ obtained from$\sigma$by flipping the values of the spins inside �. This efectively corresponds to removing the set$\partial _ { e } C$of edges in$E ( \sigma )$with exactly one endpoint in$C .$. Taking into account the cost of this operation leads to

$$
\langle \mathbb {I} (\mathbf {C} = C) \rangle_ {\Lambda_ {n} ^ {+}, \beta , 0} \leq e ^ {- 2 \beta | \partial_ {e} C |}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">�<sup>∗</sup> = (�<sup>∗</sup>, �<sup>∗</sup> )</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">� = (�, � )</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">�</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">{�, �}</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">t �<sup>∗</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sub>�</sub><sup>∗</sup></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">{�, �}</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1The dual graph of a planar graph is the planar graph with vertex-set given by the faces of (including the exterior one) and edge-se given by unordered pairs , where � and � are two faces that are bordered by the same edge When this edge is �, we denote the dual edge by �<sup>∗</sup>. The map is therefore aρ\*� ↦→ �<sup>∗</sup> bĳection between � and . On the square lattice, the dual graph is nothing but the trans late by of the square lattice itself.( <sup>1</sup><sub>2</sub> , <sup>1</sup><sub>2</sub> )</span></small>

for every � ∌ g. At this stage, the fact that$\partial _ { e } C$is a loop and that there are at most $( k + 1 ) 4 ^ { k }$possible loops of length � surrounding the origin gives

$$
\langle \sigma_ {0} \sigma_ {\mathbf {g}} \rangle_ {\Lambda_ {n} ^ {+}, \beta , 0} \geq 1 - 2 \sum_ {k \geq 1} k 4 ^ {k} e ^ {- 2 \beta k} > 1 - \frac {8 e ^ {- 2 \beta}}{(1 - 4 e ^ {- 2 \beta}) ^ {2}}.\tag{2.10}
$$

## 3. Onsager’s 1944 revolution and the integrability of the Ising mode

## 3.1. Kramers-Wannier treatment of the Ising model and duality

While Peierls’ result is certainly one of the first key rigorous steps in the understanding of the Ising model, the work [79] of Hans Kramers and Gregory Wannier in 1941 propelled the Ising model in another dimension in terms of mathematical interest. Indeed, the two physicists agreed that the Ising model was not necessarily an accurate description of ferromagnetism, but they were precursors in strongly believing that having mathematical models that can be rigorously analysed was of crucial interest for the understanding of physical phenomena, even if only approximate.

Kramers and Wannier’s goal was to understand what happens for the Ising model at arbitrary inverse-temperature. Peierls’ argument shows that the model behaves like a ferromagnet when$\beta$is large. A fairly simple argument, see Frame 4, shows that it behaves like a paramagnet when$\beta$is small. It is therefore tempting to think that there is an intermediate inverse-temperature, playing the theoretical role of the inverse of Curie’s temperature, that separates a paramagnetic phase from a ferromagnetic phase, i.e. a critical inversetemperature$\beta _ { c }$defined by the formula

$$
\beta_ {c} = \beta_ {c} (\mathbb {Z} ^ {d}) := \inf \{\beta : m ^ {*} (\beta) > 0 \}.\tag{3.1}
$$

Of course, the notion of critical inverse-temperature immediately leads to the following question: can one compute the value of the critical point$\beta _ { c } ?$

The work [79] represented an important historical step towards this computation. It involved a number of ideas that deeply influenced the way mathematicians and physicists approach the Ising model. The first key observation is that Kramers and Wannier did not work with the Ising model in the presence of a magnetic field (in other words, they set ℎ to be 0). Instead, they proposed to look at the specific heat defined by

$$
C (\beta) := - \beta^ {2} \frac {\partial^ {2}}{(\partial \beta) ^ {2}} (\beta f) (\beta , 0).\tag{3.2}
$$

Kramers and Wannier argued that the critical point of the model on${ \mathbb { Z } } ^ { 2 }$should correspond to a value of$\beta$at which$C ( \beta )$blows up. The next step is maybe the most interesting one. By assuming that there exists a unique point at which$C ( \beta )$blows up, they were able to predict the value of$\beta _ { c }$. The reason behind this prediction is the following duality relation for the free energy on${ \mathbb { Z } } ^ { 2 }$:

$$
\beta f (\beta , 0) = \beta^ {*} f (\beta^ {*}, 0) - 2 \beta + \ln 2 + 2 \ln \cosh (\beta^ {*}),\tag{3.3}
$$

![](images/page_8_image_0.jpg)

On the left. A picture of the low-temperature expansion on$\Lambda _ { 1 } ^ { + }$. The set$\Lambda _ { 1 } ^ { + }$is depicted in dashed gray, and$( \Lambda _ { 1 } ^ { + } ) ^ { * }$ in plain black. The edges in the dual configuration are depicted in bold. On the right. The se$\mathbb { S } ( 5 , 3 )$with the bottom and top sets depicted. In this case � and � are respectively constant equal to −1 and +1.

where$\beta$and$\beta ^ { * }$are related via the formula tanh$( \beta ^ { * } ) = e ^ { - 2 \beta }$. The uniqueness implies that $\beta _ { c }$must be the self-dual point satisfying$\beta ^ { * } = \beta , \mathrm { i . e . } \beta _ { c }$must be equal to${ \frac { 1 } { 2 } } \ln ( 1 + { \sqrt { 2 } } )$. Of course, this reasoning is not a formal proof as it is a priori non-obvious that the singular point is unique.

The proof of Kramers and Wannier of the duality relation is also of great interest. Originally, they used so-called transfer matrices to do it; see Frame 2 for details. While they did not invent those matrices (they already appeared in the work of Montroll [85]), they probably made the first important use of them. Today, the derivation of this relation is straightforward and does not rely on transfer matrices. It involves relating the partition functions$Z ( G , \beta , 0 )$and$Z ( G ^ { * } , \beta ^ { * } , 0 )$using, for the first one, the expression given by the low-temperature expansion (2.8), and for the second, an alternative representation called the high-temperature expansion, obtained by van der Waerden [100] and briefly described in Frame 4. When observing that the dual of a box in the square lattice is (except on the boundary) a box of the square lattice, one obtains the identity above by considering larger and larger boxes.

## Frame 2: transfer matrices of the Ising model

To lighten the presentation we restrict our attention to the case$h = 0$. Consider the slices$\mathbb { S } ( N , M ) : = ( \mathbb { Z } / N \mathbb { Z } ) ^ { d - 1 } \times \mathbb { I } 0 , M \mathbb { I }$with no edges between the vertices of the bottom$( \mathbb { Z } / N \mathbb { Z } ) ^ { d - 1 } \times \{ 0 \}$(we call$( \mathbb { Z } / N \mathbb { Z } ) ^ { d - 1 } \times \{ M \}$the top of the slice); see Figure 1 on the right. Let$\sigma _ { | \mathrm { b o t t o m } }$and$\sigma _ { | \mathrm { t o p } }$be the restrictions of$\sigma$to the top and bottom of $\mathbb { S } ( N , M )$, considered as two elements of$\{ - 1 , 1 \} ^ { ( \mathbb { Z } / N \mathbb { Z } ) ^ { d - 1 } }$. Introduce the quantit

$$
Z (N, M, \underline {{\tau}}, \overline {{\tau}}) := \sum_ {\sigma \in \{- 1, 1 \} ^ {\mathbb {S} (N, M)}} \exp [ - \beta H _ {\mathbb {S} (N, M), h} (\sigma) ] \mathbb {I} (\sigma_ {| \text { bottom }} = \underline {{\tau}}, \sigma_ {| \text { top }} = \overline {{\tau}}),\tag{3.4}
$$

where$\underline { { \tau } } , \overline { { \tau } } \in \{ - 1 , 1 \} ^ { ( \mathbb { Z } / N \mathbb { Z } ) ^ { d - 1 } }$, as well as the so-called transfer matrix

$$
V _ {N} (\underline {{\tau}}, \overline {{\tau}}) := Z (N, 1, \underline {{\tau}}, \overline {{\tau}}) = \exp \Big [ - \beta \bigg (\sum_ {x \in (\mathbb {Z} / N \mathbb {Z}) ^ {d - 1}} \underline {{\tau}} _ {x}   \overline {{\tau}} _ {x} + \sum_ {\{x, y \} \in E ((\mathbb {Z} / N \mathbb {Z}) ^ {d - 1})} \overline {{\tau}} _ {x}   \overline {{\tau}} _ {y} \bigg) \Big ].\tag{3.5}
$$

One immediately finds that$Z ( N , M , \underline { { \tau } } , \overline { { \tau } } ) = V _ { N } ^ { M } ( \underline { { \tau } } , \overline { { \tau } } )$. Other quantities of the model may be written in terms of transfer matrices: for instance the partition function of the model on the �-dimensional torus$( \mathbb { Z } / N \mathbb { Z } ) ^ { d }$becomes the trace of$V _ { N } ^ { N }$

One important aspect of those transfer matrices$V _ { N }$is that certain questions on the behaviour of the model are rephrased as spectral questions on the transfer matrix. For instance, by letting � and then � go to infinity, one observes that the asymptotic behaviour of the partition function on$( \mathbb { Z } / N \mathbb { Z } ) ^ { d - 1 } \times ( \mathbb { Z } / M \mathbb { Z } )$, and therefore the value of the free energy, are connected to the asymptotic behaviour of the leading eigenvalue of$V _ { N }$as � tends to infinity. This can very well be an intractable problem, but in some cases it is not.

## 3.2. Onsager’s result

Kramers and Wannier’s results unraveled the potential mathematical interest of the Ising model, but the real revolution came only a few years after with one of the most impressive achievements in mathematical physics. Lars Onsager, Nobel prize winner in 1968, was a Norwegian specialist in theoretical chemistry. He was particularly interested in mathematical problems and focused his attention on the Ising model for the formidable challenge that its exact solution represented more than for his physical relevance2.

To everyone’s surprise, Onsager announced at a conference ofthe New York Academy of Sciences in 1942 that he obtained the following exact expression for the free energy (at zero magnetic field) of the Ising model on the square lattice${ \mathbb { Z } } ^ { 2 }$:

$$
- \beta f (\beta , 0) = \ln 2 + \frac {1}{8 \pi^ {2}} \int_ {0} ^ {2 \pi} \int_ {0} ^ {2 \pi} \ln [ \cosh (2 \beta) ^ {2} - \sinh (2 \beta) (\cos \theta_ {1} + \cos \theta_ {2}) ] d \theta_ {1} d \theta_ {2}.\tag{3.6}
$$

This implies, in physics jargon, that the model is exactly solvable. This solvability is itself linked to a deep property of the model called integrability. Onsager’s underlying idea was that the transfer matrices of the 2D Ising model are a product of two matrices that generate (by taking successive brackets) a finite-dimensional Lie algebra. He used this observation to derive the asymptotic behaviour of the leading eigenvalue of these matrices in his famous 1944 paper [87]. In 1949, Bruria Kaufman [76] provided an alternative and simpler derivation.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2His opinion on this fact seemingly evolved: in his first 1944 paper [87] he presents it as a poor model of ferromagnetism, but a fairly good model for binary alloys, while in his paper with Kaufman in 1949 [76] he describes it as a model for ferromagnetism.</span></small>

A few years later, Onsager surprised the world of theoretical physicists again by claiming an exact expression for the spontaneous magnetisation on$\mathbb { Z } ^ { 2 }$: for$\beta \geq \beta _ { c }$,

$$
m ^ {*} (\beta) = (1 - \sinh (2 \beta) ^ {- 4}) ^ {1 / 8}.\tag{3.7}
$$

While the result was announced by Onsager first, it was a young physicist, that would later become one of the most influential theoretical physicists of the second half of the twentieth century, Chen-Ning Yang (from Yang-Baxter’s equation, Yang-Mills’s theory, Lee-Yang’s theory, etc.), who provided a mathematical proof [105] of this statement by achieving a mathematical tour de force involving Toeplitz determinants. The proof relies on a computation, again using transfer matrices but much more evolved than for the free energy, of the two-point function$\langle \sigma _ { ( 0 , 0 ) } \sigma _ { ( n , 0 ) } \rangle _ { ( \mathbb { Z } / N \mathbb { Z } ) ^ { 2 } , \beta , 0 } ,$, and the observation that

$$
m ^ {*} (\beta) ^ {2} = \lim _ {n \to \infty} \lim _ {N \to \infty} \left\langle \sigma_ {(0, 0)} \sigma_ {(n, 0)} \right\rangle_ {(\mathbb {Z} / N \mathbb {Z}) ^ {2}, \beta , 0}\tag{3.8}
$$

(at the time, such an identity was not obviously true, but nowadays this can be proved easily using for instance the FK percolation, see Section 7.2).

In the forties and fifties, these successes were considered by physicists as a mathematical curiosity rather than a truly crucial advance. Yet, they had a revolutionary impact on theoretical physics for multiple reasons: First, the level of sophistication of the mathematical tools used in the proofs is without any common measure with what was previously used in such kinds of problems, and these techniques created whole new types of mathematical physics. Second, the behaviour of the model did not correspond to previous mean-field approximations, thus invalidating rigorously the Curie-Weiss or Landau theories and open-ing a new era in statistical mechanics. Third, the results had many direct applications for the Ising model itself: for instance the specific heat$C ( \beta )$can easily be shown to blow up logarithmically as$\beta$approaches$\scriptstyle { \frac { 1 } { 2 } } \log ( 1 + { \sqrt { 2 } } )$, thus confirming rigorously that this value is the critical point of the system (the logarithmic blow up is one example of non mean-field behaviour).

Numerous alternatives have been proposed to the approach of Onsager-Kaufman-Yang, often referred to as the algebraic method. As a joke, Baxter and Enting named their 1978 paper [10], introducing a solution to the 2D Ising model involving the notion of startriangle transformation, the "399th solution of the Ising model". This count is, of course, overestimated, but one can list a large number of alternative strategies.

The first such strategy is called the combinatorial approach and is referring to an original argument of Kac and Ward [71] rewriting the partition function of the model in terms of the square root of the determinants of so-called Kac-Ward’s matrices using a combinatorial expansion ofthe partition function generalising the van der Waerden high-temperature expansion [100]. The advantage of such an approach is that it does not rely on transfer matrices, and therefore is applicable to every finite planar graph, even with arbitrary nearest-neighbour coupling constants. Unfortunately, the original argument was not entirely rigorous and one had to wait until 1999 [33] to finally obtain a mathematical derivation ofthis approach. Nowadays, the method is very well understood and especially useful in relation to discrete holomorphicity and higher genus graphs, see [29] and references therein for a more complete account.

The (nowadays) most classical method is probably the Pfafian method. It came as an attempt to go around the substantial dificulties to make the combinatorial approach rigorous. Due to Hurst and Green [66], Kasteleyn [75], and Fisher [46], the strategy consists in writing the Ising partition function on a finite planar graph � in terms of the dimer (a dimer configuration is a subset of edges which covers every vertex exactly once) partition function on a related graph �(�) (the precise definition of the graph depends on the implementation of the Pfafian method). It is then possible to relate the partition function to a skew-symmetric adjacency matrix and express the partition as a Pfafian, hence the name of the method. This strategy has been the basis of a number of more refined results about the model, in particular the computation of the spin-spin correlations of the model at and away from criticality. For the deepest and most impressive results, we recommend that the reader takes a look at the two books of McCoy-Wu [83] and Palmer [89].

Another approach of importance was proposed by Schultz-Mattis-Lieb in [95] to tackle the cases for which a transfer matrix can be used. In this paper, they connected the transfer matrix with the exponential of a quantum hamiltonian. This connection to 1D quantum spin chains has been very fruitful and understood in a number of alternative ways since then. As a byproduct, the authors were able to express the partition function as a Grassmann "Gaussian" integral. The advantage of this way of writing the partition function is that the Pfafians emerge naturally. This approach is at the basis of renormalisation schemes in two dimensions; see Section 8.3.

Yet another approach dealing with the context in which transfer matrices can be applied is worth mentioning, as it is by far the most generalisable to other models. It is based on the commutation of the transfer matrices attached to the model with diferent critical parameters. Pioneered by Rodney Baxter, this approach consists in using the so-called Yang-Baxter equation. The advantage is that the same strategy can be applied to a very large variety of integrable systems, such as the six-vertex model, to cite only one example. We refer to [9] and references therein for more details.

## 4. The fifties and sixties: the Ising model becomes a laboratory for understanding critical phenomena

The fifties and sixties were probably the decades during which the Ising model became an "unavoidable" model. The realisation that having a tractable model of statistical physics could be a useful explanatory but also predicting tool became more and more obvious. The Ising model, with Onsager’s solution, was a prime example of a model with such qualities.

The model therefore developed tremendously in the postwar era in theoretical physics as well as in a rapidly growing field called mathematical physics. The latter gathered more and more physicists that were interested in rigorous aspects of the objects they studied, and mathematicians willing to study problems that were naturally emerging from physical modelling. The Ising model ofered a wonderful playground for such scientists, and the number of papers mentioning the model started to be counted in the hundreds.

## 4.1. Progress in mathematical physics: from perturbative regions of the phase diagram to the vicinity of the critical point

During this period, the newly developing community of mathematical physicists recognised that the study of phase transitions, and in particular of the critical phase (when$\beta$ is equal to$\beta _ { c } )$, was a vast field of its own. While the previous developments mostly concerned values of$\beta$and ℎ that were far from the critical regime (Peierls’ argument [90] or Baker’s use of Padé approximant [8] for instance), the situation changed drastically around the fifties. The interest in the intermediate values o$\mu$became stronger and stronger. Onsager’s solution ofers a precise understanding of the critical behaviour of the 2D Ising model, yet it has clear downsides related to the relative fragility of the integrability of the system. As a consequence, mathematical physicists started using the Ising model not only as a solvable system, but more generally as a good mathematical model that one should not reduce to its integrability aspects. New rigorous techniques emerged during this period to try to understand the vicinity of the critical point for non-integrable cases, for instance in higher dimensions.

## 4.1.1. Correlation inequalities

It is natural to ask which monotonicity properties are satisfied by the system, in par ticular by the spin-spin correlations$\langle \sigma _ { A } \rangle _ { G , \beta , h }$where$\sigma _ { A } : = \Pi _ { x \in A } \sigma _ { x }$, when the parameter vary (for instance,$G , \beta$or ℎ).

To tackle such questions, mathematical physicists started proving what we now call correlation inequalities using combinatorial arguments. Among the first such examples are Grifiths’ inequalities [57]: for every$\beta , h \ge 0$and every �,$B \subset V$

$$
\langle \sigma_ {A} \rangle_ {G, \beta , h} \geq 0 \quad \text { and } \quad \langle \sigma_ {A} \sigma_ {B} \rangle_ {G, \beta , h} \geq \langle \sigma_ {A} \rangle_ {G, \beta , h} \langle \sigma_ {B} \rangle_ {G, \beta , h}.\tag{4.1}
$$

A byproduct of the second inequality when applied to$B = \{ x , y \}$and summed over all edges $\{ x , y \}$, is that correlations$\langle \sigma _ { A } \rangle _ { G , \beta , h }$are increasing in$\beta$(and also in$G$with a little bit of additional work). One may derive the same for the spontaneous magnetisation$m ^ { * } ( \beta )$, so that the definition of$\beta _ { c }$can now be rephrased as

$$
\beta_ {c} = \inf \{\beta \geq 0: m ^ {*} (\beta) > 0 \} = \sup \{\beta \geq 0: m ^ {*} (\beta) = 0 \}.\tag{4.2}
$$

This implies in particular that there is indeed a unique transition between paramagnetic and ferromagnetic phases.

Other interesting correlation inequalities were obtained in subsequent years. Let us contemplate a few examples (we do not write them in full generality, and we drop the subscript after ⟨·⟩):

$\mathrm { G H } \mathrm { S } ^ { \prime } \mathrm { s }$inequality [59]: for$h \geq 0$and$x \in G$

$$
\frac {\partial^ {2}}{(\partial h) ^ {2}} \langle \sigma_ {x} \rangle \leq 0.\tag{4.3}
$$

• Simon-Lieb’s inequality <sub>[82]</sub>: for$S \ni 0$and$x \notin S$, when$\langle \cdot \rangle _ { S }$refers to the model in �,

$$
\langle \sigma_ {0} \sigma_ {x} \rangle \leq \sum_ {y \in \partial S} \langle \sigma_ {0} \sigma_ {y} \rangle_ {S} \langle \sigma_ {y} \sigma_ {x} \rangle .\tag{4.4}
$$

• Messager-Miracle-Solé’s inequality <sub>[84]</sub>: for$x , y \in \mathbb { Z } _ { + } ^ { d }$(below ⟨·⟩ is defined on$\mathbb { Z } ^ { d } )$

$$
\langle \sigma_ {0} \sigma_ {x + y} \rangle \leq \langle \sigma_ {0} \sigma_ {x} \rangle .\tag{4.5}
$$

$\mathrm { F K G } ^ { \prime } \mathrm { s }$inequality [47]: for any increasing functions$f , g : \{ - 1 , 1 \} ^ { V } \to \mathbb { R }$

$$
\langle f g \rangle \geq \langle f \rangle \langle g \rangle .\tag{4.6}
$$

This far from exhaustive list, which we did not discuss in detail, is intended to show the variety of possible correlation inequalities. Clever use of these inequalities provided the embryo of what would be considered later as the theory of non-critical statistical physics systems at equilibrium, as the correlation inequalities and their consequences often generalise in the same (or slightly altered) form to a wider class of lattice spin models.

## 4.1.2. The Ising model with a magnetic field: the Lee-Yang theory

While studying the whole phase diagram is a Herculean task that was far beyond the techniques developed at the time, a beautiful development enabled mathematical physicists to understand the case$h \neq 0$

The twin papers [81], referred to as the Lee-Yang theory, relate the regularity properties of the free energy (and therefore the location of singular points corresponding to places where a phase transition occurs) to the locus of the complex zeroes of the partition function $Z ( G , \beta , h )$when seen as a function of$h \in \mathbb { C }$. Beyond the result itself, the philosophy consisting in studying the complex zeroes of the partition function had a resounding efect on the field of mathematical physics. This can be put in parallel with the analysis of zeroes of the Riemann zeta function: one learns something about prime numbers by studying the zeroes of a generating-type function associated with them.

The result of Lee and Yang is not restricted to the n.n.f. Ising model on$G \subset \mathbb { Z } ^ { d }$, but the latter gives an important application of it. In our context, let$Z ( G , \beta , \mathbf { h } ) \in \mathbb { C }$(for $\mathbf { h } = ( \mathbf { h } _ { x } : x \in V ) \in \mathbb { C } ^ { V } )$be the partition function defined as in (2.3) with the diference that the magnetic field is allowed to vary with the vertex, i.e. that the$\textstyle \sum _ { x \in V } h \sigma _ { x }$term of the Hamiltonian in (2.2) is replaced by$\textstyle \sum _ { x \in V } \mathbf { h } _ { x } \sigma _ { x }$. The result states that for this model, the zeroes of the function h$\mapsto Z ( G , \beta , \mathbf { h } )$are satisfying$\mathbf { R e } ( \mathbf { h } _ { x } ) = 0$for every$x \in V .$

As a consequence of this theorem, the free energy$f ( \beta , h )$(which we recall from (2.5) is expressed in terms of the limit of the logarithm of partition functions) is analytic as soon as$h \neq 0$. Other consequences follow, such as exponential decay of so-called truncated correlations of the system, as well as analyticity of the other thermodynamical quantities when the magnetic field is non-zero. Roughly put, the Lee-Yang theory enables to understand in full detail the part of the phase diagram corresponding to non-zero magnetic field

## 4.2. Revolutionary progress on the physics front

In parallel to these first successes in mathematical physics, revolutionary progress was made during this period on the physical understanding of phase transitions. Among other things, the scaling and universality hypotheses were formulated, and the pillars of the renormalisation group were cast, in both cases using the Ising model as an important source of inspiration.

## 4.2.1. Critical exponents and the success of scaling theory

A fundamental notion of physics is the assumption that thermodynamical quantities of physical systems near criticality tend to take simple forms when expressed in terms of the parameters of the system. A major advance was achieved in the sixties by American chemist Benjamin Widom who proposed in [102] that these quantities are powers in each parameter. For the Ising model, the parameters are$\beta$and ℎ, and this scaling hypothesis translates into the existence of so-called critical exponents. To give a few examples related to already defined quantities, one may for instance predict that

$$
m ^ {*} (\beta) = (\beta - \beta_ {c}) _ {+} ^ {\beta + o (1)} \qquad m (\beta_ {c}, h) = h ^ {1 / \delta + o (1)} \qquad \langle \sigma_ {0} \sigma_ {x} \rangle_ {\beta_ {c}, 0} = \frac {1}{| x | ^ {d - 2 + \delta}}\tag{4.7}
$$

(notice that$\beta$and$\beta$have nothing to do with each other), where$o ( 1 )$is a quantity tending to $_ 0$as$\beta$tends to$\beta _ { c }$, ℎ tends to 0, or |�| tends to infinity, respectively. In fact, a whole family of such exponents, denoted by$\alpha , \beta , \gamma , \delta , \eta , \nu$(for the most classical ones) can be defined for each model. Understanding the phase transition boils down to, among other things, deriving those exponents.

Dealing with such exponents, one may naturally wonder how many degrees of freedom truly exist in statistical physics models. For instance, could some of these critical exponents be connected via direct relations that would transcend the precise definition of each model? In the sixties, physicists such as Essam, Fisher, and Widom himself, to cite only those three (see [42, 45, 102] for some early works on the subject), started unraveling system atic connections between the exponents, thus hinting towards the fact that only two degrees of freedom exist and that exponents are related by so-called scaling relations

$$
\nu d = 2 - \alpha = 2 \beta + \gamma = \beta (\delta + 1) = \gamma \frac {\delta + 1}{\delta - 1} \quad 2 - \eta = \frac {\gamma}{\nu} = d \frac {\delta - 1}{\delta + 1}.\tag{4.8}
$$

The scaling relations apply in a context which is far more general than just the Ising model (see for instance [38] for a proof in the case of a large family of two-dimensional percolation models). In the course of discovering these diferent scaling relations, the Ising model in two and three dimensions played the important role of a sanity check. While other experimental systems were used as testing grounds, the Ising model was the only example of a theoretical system which did not exhibit mean-field behaviour (and therefore was not too “trivial”) and for which such exponents were available, either rigorously thanks to the exact solution in 2D, or approximately thanks to Baker’s use of Padé approximant [8] in 3D.

To conclude this section, let us mention an important quantity, called the correlation length$\xi ( \beta )$of the system, that plays an important role in the scaling hypothesis (it corresponds to the exponent �). We consider the case$\beta < \beta _ { c }$but a similar notion can be introduced for$\beta > \beta _ { c }$, with analogous interpretations.

When considering, say, spin-spin correlations at criticality, one expects an algebraic decay as mentioned in (4.7). Yet, when$\beta < \beta _ { c }$, the scaling hypothesis cannot hold uniformly in$| x |$and such a decay does not occur. In fact, it was found in many systems that spin-spin correlations decay exponentially fast (see Section 7.1 for more details) and the inverse-rate of decay is the correlation length$\xi ( \beta )$. This correlation length has an interesting interpretation: it is the smallest scale at which the system with$\beta < \beta _ { c }$is of-critical, meaning that when looking at a system with a size which is much smaller than$\xi ( \beta )$, the diference between the system and a critical system will be invisible to the physicist’s eye, while on the contrary when the size is much larger than$\xi ( \beta )$, the model looks similar to the case of$\beta \ll \beta _ { c }$. In other words, when approaching the critical point, a system becomes more and more “critical”. By how much this is true depends on the size of the system, and the correlation length separates between the sizes at which the system looks critical, and the sizes at which it looks clearly non critical.

## 4.2.2. Kadanof’s block-spin renormalisation and universality

While Widom’s scaling hypothesis provides compelling evidence that critical exponents exist, the underlying justification of the hypothesis itself remained slightly superficial until Russian physicist Leo Kadanof provided an illuminating argument for it. In his famous 1966 paper [72], Kadanof suggested that the block-spin renormalisation transformation – i.e. replacing a block of neighbouring sites by one site having a spin equal to the dominant spin in the block – corresponds to appropriately changing the scale and the parameter$\beta$and ℎ of the model. Assuming that iterating this procedure somehow converges suggests that the asymptotic properties of the system are described by a fixed point of a renormalisation map. As a result, one ends up with the scale invariance of the model. This argument, inspired by the study of the Ising model, turned out to be the basis of the monumental theory of the renormalisation group (RG) that was put in a general framework a few years later by Kenneth Wilson [104].

The block-spin argument of Kadanof achieved much more than a physical justification of the scaling hypothesis. Assuming uniqueness of the fixed point also implies that the renormalisation of Ising models defined on diferent �-dimensional lattices should converge to the same fixed point, and therefore share the same critical exponents. This was already partially realised in 2D by observing the Ising model on the square, hexagonal, and triangular lattices (they are all exactly solvable) as well as in 3D by approximations using series expansions [34], but the renormalisation argument suggests that the few examples of equalities between exponents are, in fact, the illustration of a much more general phenomenon.

What is now known as the universality hypothesis was explicitly formulated in parallel by Robert B. Grifiths and Kadanof in 1971 [58,73]. Roughly speaking, it states that the critical properties of a physical system only depend on

• the lattice dimension �;

• the symmetry of the space of possible spins (Z/2Z symmetry for Ising);

• the speed of decay of coupling constants (this is only relevant when the$J _ { x , y }$are allowed to decay polynomially with$\| x - y \|$, which is not the case in this text).

This realisation of universality is fundamental to the relevance of statistical physics as a whole. To borrow from Kadanof’s wording: “Why study a simplified model like the Ising model? The strategy ofstudyingphysical questions by using highly simplified models is made rewarding by a characteristic ofphysical systems called “universality”, in that many systems may show the very same qualitativefeatures, and sometimes even the same quantitative ones. To study a given qualitativefeature, it often pays to lookfor the simplest possible example.”

To summarise Section 4, by the end of the sixties it became clear to mathematical physicists and theoretical physicists that the Ising model was one of the most striking examples of a simple physical system which was rich enough to grasp a large variety of phenomena falling in the range of statistical physics. Results on the Ising model started to play a role similar to experimental results in the sense that they could corroborate$^ { \mathrm { o r , } }$on the contrary, invalidate the embryo of a theory. It is fair to say that the importance of the model was never argued upon later on and that it was finally recognised as one of the centerpieces of modern statistical physics.

## 5. The sixties and seventies: emergence of the probabilistic interpretation

Physicists and mathematical physicists think of the quantity$\langle \cdot \rangle _ { G , \beta , h }$as a form attributing to each function$X : \{ - 1 , 1 \} ^ { V } \to \mathbb { R }$(resp. C) a value in$\mathbb { R }$(resp. C). In the late sixties and seventies, the rise of probabilistic methods led to an alternative interpretation of the Ising model in which$\langle \cdot \rangle _ { G , \beta , h }$is now understood as (dual to) a probability measure$\mu _ { G , \beta , h }$. As a consequence of this reinterpretation, it becomes natural to ask what the properties of a randomly chosen spin configuration are, and what the possible measures on the infinite lattice that can be obtained as limits of measures in finite volume are.

## 5.1. The random geometry of the spin configuration

As mentioned above,$\langle \cdot \rangle _ { G , \beta , h }$is the linear form associated with the probability measure$\mu _ { G , \beta , h }$on$\{ - 1 , 1 \} ^ { V }$defined for every configuration$\sigma$by the formula

$$
\mu_ {G, \beta , h} [ \{\sigma \} ] := \frac {1}{Z (G , \beta , h)} \exp [ - \beta H _ {G, h} (\sigma) ].\tag{5.1}
$$

Then, quantities like$\langle \sigma _ { A } \rangle _ { G , \beta , h }$can be interpreted as the correlations between the random variables$\sigma _ { x }$with$x \in A$. Note that in this interpretation the partition function is a normalising factor making the measure at hand a probability measure.

Let us assume for a moment that$h = 0$and interpret the phase transition in terms of probability. The structure of the probability measure is such that configurations have greater probability if they have more pairs of neighbours with a similar spin. In this interpretation, the larger$\beta$is the more important it is that neighbours have the same spins. In particular, in the limit as$\beta$tends to infinity, one ends up with one of the two configurations where all spins are the same. It becomes then natural to expect that for$\beta$large, typical configurations have an excess of one spin compared to the other. On the other hand, when$\beta$is very small, how much the measure takes the agreements into account is fairly limited, and one may expect that spins behave roughly independently, at least at large distance of each other.

The interpretation in terms of random variables opens new uncharted territories: one can interpret probabilistically natural thermodynamical quantities such as magnetisation (which corresponds to the expectation ofthe spin at a vertex) or surface tension. It also opens a way to new problems, such as dynamics on the space ofspin configurations or large deviations (for instance for an Ising model at an inverse-temperature$\beta ,$, but with an excess of +1 spins in a region and of −1 spins in another); see Frame 3.

## Frame 3: sampling the Ising model – Glauber dynamics

The probabilistic interpretation naturally raises the question of sampling ran dom configurations according to$\mu _ { G , \beta , 0 }$(set$h = 0$for simplicity). A classical method consists in expressing the measure as the invariant measure of a Markovian dynamics $( \sigma ( t ) : t \geq 0 ) \in ( \{ - 1 , 1 \} ^ { V } ) ^ { \mathbb { R } _ { + } }$, called the Glauber dynamics and defined as follows: attach an exponential clock to each vertex of �. Each time a clock rings, say at time � at$x \in V$,

• If$\begin{array} { r } { \sigma _ { x } ( t ) \sum _ { y : \{ x , y \} \in E } \sigma _ { y } ( t ) < 0 , } \end{array}$, switch the value of the spin at �,

• Otherwise, switch the value of the spin at <sub>�</sub> with a probability equal to exp$\begin{array} { r } { [ - 2 \beta \sum _ { y : \{ x , y \} \in E } \sigma _ { y } ( t ) ] } \end{array}$, and do not switch otherwise.

Since$\mu _ { G , \beta , 0 }$is the only invariant measure for this dynamics, the limit as � tends to infinity, irrespectively of the initial value$\sigma ( 0 )$, is sampled according to$\mu _ { G , \beta , h } .$

This dynamics was named after the American physicist Roy J. Glauber. Alternative choices of dynamics are obtained by changing the jump probabilities. In Figure 2, three simulations of the Ising model are shown respectively below (on the left), at (in the middle) and above (on the right)$\beta _ { c }$

## 5.2. Boundary conditions and the Gibbs formalism

An important output ofthe probabilistic interpretation ofthe model is that it becomes natural to condition on spins in a subset of�. More precisely, let$W \subset V$and let � be the graph with vertex-set � and edge-set induced by the edges of the graph �. Let$\tau \in \{ - 1 , 1 \} ^ { V }$be a spin configuration on �. One may ask what is the law of the spins in � when conditioning $\sigma$outside � to be equal to �, i.e. what is$\mu _ { G , \beta , h } [ \cdot | \sigma _ { x } = \tau _ { x } , \forall x \notin W ] ?$

The answer to this question is best cast when introducing the notion of boundary conditions. For a subgraph � of$\mathbb { Z } ^ { d }$and a configuration$\tau \in \{ - 1 , 1 \} ^ { \mathbb { Z } ^ { d } }$, introduce the measur $\mu _ { G , \beta , h } ^ { \tau }$with � boundary conditions defined like$\mu _ { G , \beta , h }$except that$H _ { G , h }$is replaced by

$$
H _ {G, h} ^ {\tau} (\sigma) := H _ {G, h} (\sigma) - \sum_ {\{x, y \} \in E (\mathbb {Z} ^ {d}): x \in V, y \notin V} \sigma_ {x} \tau_ {y}.\tag{5.2}
$$

Note that the only values of � that matter are on the exterior boundary of �, i.e. on the vertices that are connected by an edge of$\mathbb { Z } ^ { d }$to a vertex in �.

With this definition, we obtain the following important property of the Ising model, called the spatial Markov property: for every finite subgraph � of$\mathbb { Z } ^ { d }$, every$W \subset V$, and every configuration$\tau \in \{ - 1 , 1 \} ^ { \mathbb { Z } ^ { d } }$, if � denotes the graph induced by the set �,

$$
\mu_ {G, \beta , h} [ \cdot | \sigma_ {x} = \tau_ {x}, \forall x \notin W ] = \mu_ {H, \beta , h} ^ {\tau} [ \cdot ].\tag{5.3}
$$

In words, when conditioning the Ising model on$G$to coincide with a given configuration outside �, one gets the measure in � with the corresponding boundary condition.

This property ofers a natural consistency relation between measures$\mu _ { G , \beta , h } ^ { \tau }$for varying � and �. As a byproduct, one is naturally led to postulate that any reasonable infinitevolume version of Ising measures should satisfy the same consistency relation. One therefore ends up with the following notion: a measure$\mu$on$( \{ - 1 , 1 \} ^ { \mathbb { Z } ^ { d } } , \mathfrak { F } _ { \mathbb { Z } ^ { d } } )$is called a Gibbs measure of the Ising model with parameters$\beta$and ℎ if it satisfies the Dobrushin-Lanford-Ruelle (DLR) property: for every finite$V \subset \mathbb { Z } ^ { d }$and$\tau \in \{ - 1 , 1 \} ^ { \mathbb { Z } ^ { d } }$

$$
\mu [ \cdot | \mathfrak {F} _ {\mathbb {Z} ^ {d} \backslash V} ] = \mu_ {G, \beta , h} ^ {\tau} [ \cdot ] \text {   on   } E _ {\tau} \mu \text {-almost   surely },\tag{5.4}
$$

where

•$G$is the graph induced by the vertex-set$V ;$

•$E _ { \tau }$is the event that$\sigma$and � agree on the exterior boundary of$G \mathrm { : }$;

${ \mathfrak { F } } _ { \mathbb { Z } ^ { d } \backslash V }$is the �-algebra generated by the random variables$( \sigma _ { x } : x \notin V )$

The notion of Gibbs measure is not restricted to the Ising model (see [52] for a book on the subject), but the classification of such Gibbs measures has been the object of intense study in the specific case of the Ising model, with a very successful outcome.

The first question that one may ask is the existence of Gibbs measures. At least three such measures can be defined in a fairly straightforward way. By taking limits as � tends to$\mathbb { Z } ^ { d }$of the measures$\mu _ { G , \beta , h } , \mu _ { G , \beta , h } ^ { + }$, and$\mu _ { G , \beta , h } ^ { - }$(where + and − refer, with a slight abuse of notation, to � equal to all +1 or all −1), one ends up with three (possibly equal) Gibbs measures$\mu _ { \beta , h } , \mu _ { \beta , h } ^ { + }$and$\mu _ { \beta , h } ^ { - }$. More generally, one may construct measures by taking all possible sub-sequential limits of measures of the form$\mu _ { G , \beta , h } ^ { \tau }$, where one may even consider � as a random variable.

In general, the set of possible Gibbs measures on$\mathbb { Z } ^ { d }$is a non-empty simplex whose extremal measures are called extremal states. One can therefore try to classify such extremal Gibbs measures.

Some cases are quite simple to treat: for$h \neq 0$or$h = 0$and$\beta < \beta _ { c }$the simplex is reduced to a singleton, i.e. there exists a unique Gibbs measure. When$h = 0$and$\beta =$ $\beta _ { c }$, it was recently proved that this is also the case [5]. On the contrary, when$h = 0$and $\beta > \beta _ { c }$, things are more interesting. It was realised very early on that there may be more extremal states than the two obvious$\mu _ { \beta , 0 } ^ { + }$and$\mu _ { \beta , 0 } ^ { - } ,$, but examples that were found did not exhibit translation invariance. The most important such specimen was provided by Russian mathematical physicist Roland Dobrushin [31], who explained that in three dimensions, the measure$\mu _ { \beta , 0 } ^ { \mathrm { d o b r } }$obtained by taking the limit of measures$\mu _ { [ - n , n ] ^ { 3 } , \beta , 0 } ^ { \tau } ,$, where � is all plus on the upper half-space, and all minus on the lower half-space, was not translation invariant in the vertical direction at high values of$\beta .$. The existence of these Dobrushin states is related to a very deep and still mysterious (at least on a mathematical level) phenomenon in 3D statistical physics often referred to as the roughening phase transition.

Leaving non-translation invariant measures aside, many eforts were made to prove that every translation invariant Gibbs state is a convex combination o$\dot { \mu } _ { \beta , 0 } ^ { + }$and$\mu _ { \beta , 0 } ^ { - }$. The first result in this direction proved a stronger statement that draws a direct link with the previous paragraph. In two dimensions, Aizenman [1] and Higuchi [64] proved in the eighties that every Gibbs state, not only translation invariant ones, is a mixture of$\mu _ { \beta , 0 } ^ { + }$and$\mu _ { \beta , 0 } ^ { - }$. In particular, $\begin{array} { r } { { \mu _ { \beta , 0 } } = \frac { 1 } { 2 } \mu _ { \beta , 0 } ^ { + } + \frac { 1 } { 2 } \mu _ { \beta , 0 } ^ { - } } \end{array}$. In higher dimensions, it took twenty more years to obtain the result for every translation invariant Gibbs measure. We refer to the historical proof of Bodineau [18] and to the recent generalisation of Raoufi [92].

![](images/page_19_image_0.jpg)

Figure 2

On the left. Simulations at three diferent temperatures$( \beta < \beta _ { c } , \beta = \beta _ { c }$, and$\beta > \beta _ { c } )$) of the Ising model with plus boundary conditions on the top and minus boundary conditions on the bottom. Pluses are in gray and minuse in black. Credit: S. Smirnov. On the right. An example of a bubble of minuses in an environment of pluses at $\beta > \beta _ { c }$. Credit: Y. Velenik.

## 5.3. Phase coexistence and Wulf shape

The classification of Gibbs states naturally raises the question of the coexistence of diferent so-called phases. When$h = 0$and$\beta > \beta _ { c } , \mu _ { \beta , 0 } ^ { + }$and$\mu _ { \beta , 0 } ^ { - }$are not equal: they correspond to two extremal states, sometimes referred to as the plus and minus phases. Now, what happens when one tries to “mix” the two states? For instance, how does it look if one asks that part of the space is in one state, and the other part is in the other one?

In 2D, an interface is created between the two phases (see Figure 2 for simulations at diferent temperatures). While it is not obvious to define such an object in general, let us consider the simple example of the Ising model on a finite box$[ - n , n ] ^ { 2 }$of the triangular lattice with plus spins on the part of the boundary above the �-axis, and minus spins on the rest of the boundary. In this case, one can draw a unique interface going from$( - n , 0 )$to (�, 0) winding between pluses and minuses. It was understood heuristically early on that above criticality this interface should have the same fluctuations as Brownian motions, but it took decades to turn this intuition into a rigorous proof, first in the large$\beta$regime and then in the whole$\beta > \beta _ { c }$regime; see [56] and references therein. The techniques involved also enabled mathematicians to understand precise asymptotics of spin-spin correlations in the non-critical regimes. The theory, known under the coined name of Ornstein-Zernike theory, is now an area of intense research and spans over a large variety of statistical physics models. We refer to [23] for details on the Ising case.

When conditioning on the neighbourhood of the origin to be in a plus phase inside a minus phase, one ends up with a “bubble” (see Figure 2 on the right) converging when taking larger and larger volume to the so-called Wulfshape. In 2D, this bubble was analysed in detail, see the book [32] and the article [67]. In 3D, the story is even more complex. The boundary between the plus and minus phases is a kind of two-dimensional surface. The study of this object is quite intricate, and the fluctuations of the surface are still widely open. We refer to [15,17,24] and references therein.

## 6. The seventies and eighties: the Ising model and field theory

## 6.1. Constructive quantum field theory

Quantum field theories with local interaction are central in most subfields of theoretical physics, from high energy to condensed matter physics. The mathematical challenge of the proper formulation of this concept led to the program of constructive quantum field theory (CQFT). A path towards that goal was charted through the proposal to define quantum fields satisfying Wightman axioms [103] using the Osterwalder-Schrader theorem [88], in which case the construction boils down to producing relevant random distributions defined over the corresponding Euclidean space that meet a number of conditions such as suitable analyticity, permutation symmetry, Euclidean covariance, and reflection-positivity.

Finding these Euclideanfields boils down to constructing probability averages over random distributions Φ(�) of the form

$$
\langle F (\Phi) \rangle \approx \frac {1}{\mathrm{norm}} \int F (\Phi) \exp [ - H (\Phi) ] \prod_ {x \in \mathbb {R} ^ {d}} d \Phi (x),\tag{6.1}
$$

where

• �(Φ) is a smeared average of the form$\begin{array} { r } { T _ { f } ( \Phi ) : = \int _ { \mathbb { R } ^ { d } } f ( x ) \Phi ( x ) } \end{array}$�� associated with continuous functions of compact support �.

• �(Φ) is a Hamiltonian$\begin{array} { r } { H ( \Phi ) : \approx ( \Phi , A \Phi ) + \int _ { \mathbb { R } ^ { d } } P ( \Phi ( x ) ) } \end{array}$�� with (Φ, �Φ) a posi tive definite and reflection-positive (see Section 6.2) quadratic form, and$P ( \Phi ( x ) )$ an even polynomial whose terms of order$\Phi ( x ) ^ { 2 k }$are interpreted heuristically as representing �-particle interactions.

By linearity, the expectation values of products of such variables can be rewritten as

$$
\left\langle \prod_ {j = 1} ^ {n} T _ {f _ {j}} (\Phi) \right\rangle := \int_ {(\mathbb {R} ^ {d}) ^ {n}} S _ {n} (x _ {1}, \dots , x _ {n}) \prod_ {j = 1} ^ {n} f (x _ {j}) d x _ {1} \dots d x _ {n},\tag{6.2}
$$

where the$S _ { n } ( x _ { 1 } , \ldots , x _ { n } )$are the Schwingerfunctions of the corresponding Euclidean field theory which can be interpreted heuristically as pointwise correlations$\langle \prod _ { j = 1 } ^ { n } \Phi ( x _ { j } ) \rangle$⟩. Interpreting (6.1) raises a number of problems of varying dificulty.

The simplest example of Euclidean fields are the reflection-positive (see Section 6.2 again) Gaussian fields, for which �(Φ) contains only quadratic terms. Gaussian fields are alternatively characterised by 2�-point Schwinger functions satisfying Wick’s law:

$$
S _ {2 n} (x _ {1}, \dots , x _ {2 n}) = \sum_ {\pi \text {   pairings }} \prod_ {j = 1} ^ {n} S _ {2} (x _ {\pi (2 j - 1)}, x _ {\pi (2 j)}).\tag{6.3}
$$

The field theoretical interpretation of (6.3) is the absence of interaction. Due to that and to their algebraically simple structure, such fields are referred to as trivial.

The next level of dificulty is to add the next lowest order even term, i.e.$\lambda \Phi ^ { 4 }$for $\lambda > 0$. Note that, if it exists at all, the corresponding field is a random distribution so making sense of this fourth power is not straightforward. The heuristic RG approach to the problem by Wilson [104] indicates that in low enough dimensions, the problem could be tackled through a renormalisation procedure. The CQFT program has successfully yielded non-trivial scalar field theories over$\mathbb { R } ^ { 2 }$[55] and$\mathbb { R } ^ { 3 }$[44,54], and is still a lively field of mathematical physics.

A natural example aimed at constructing a$\Phi _ { d } ^ { 4 }$functional integral is to regularise it with a pair of cutofs: at a short distance (ultraviolet) scale and a large distance (infrared) scale. A lattice version of that is the restriction of Φ(·) to the vertices of a finite graph$\Lambda _ { R } ^ { ( a ) } : =$ $( a \mathbb { Z } ) ^ { d } \cap [ - R , R ] ^ { d }$, where � and � play respectively the roles of the ultraviolet and infrared cutofs. For the corresponding finite collection ofvariables$( \phi _ { x } : x \in \Lambda _ { R } ^ { ( a ) } )$, the Hamiltonian is then interpreted in terms of a Riemann-sum style discrete analog of the integral expressions, leading to the following statistical-mechanics Gibbs equilibrium state average

$$
\langle F (\phi) \rangle = \frac {1}{\text { norm }} \int_ {\mathbb {R} ^ {\Lambda_ {R} ^ {(a)}}} F (\phi) \exp [ - H (\phi) ] \prod_ {x \in \Lambda_ {R} ^ {(a)}} d \rho (\phi_ {x}),\tag{6.4}
$$

with a Hamiltonian$H ( \phi )$and an a-priori measure$\rho$of the form

$$
H (\phi) = - \sum_ {\{x, y \} \subset E (\Lambda_ {R} ^ {(a)})} \phi_ {x} \phi_ {y}, \qquad d \rho (\phi_ {x}) = e ^ {- \lambda \phi_ {x} ^ {4} - b \phi_ {x} ^ {2}} d \phi_ {x},\tag{6.5}
$$

where$d \phi _ { x }$is the Lebesgue measure on R. This is called the$\phi ^ { 4 }$lattice model.

The cutofs are removed through the limit$R ~ { \nearrow }$∞ followed by$a \searrow 0$. Parameters may be added to adjust in the process the spin-spin correlations$\langle \phi _ { x _ { 1 } } \ldots \phi _ { x _ { n } } \rangle$in such a way that they stabilise to the Schwinger functions$S _ { n } ( x _ { 1 } , \ldots , x _ { n } )$in the continuum limit scale.

The Ising model can be thought of as a limiting case of a$\phi ^ { 4 }$lattice model as it is obtained by letting$\lambda = b / 2$tend to infinity (the limit of the measures$\rho$then forces the spins$\phi _ { x }$to take the values ±1). Actually, the discrete approximations of the$\phi ^ { 4 }$functional integral and the Gibbs states of an Ising model are always connected. This relation is based on a construction which was initiated by Grifiths to obtain the Lee-Yang theorem for the$\phi ^ { 4 }$ lattice models, and was advanced further by Grifiths and Simon [60]. A probability measure on$\rho ( d \phi )$on R is said to belong to the Grifiths-Simon class if the expectation values with respect to$\rho$can be represented as an Ising model on the complete graph with well-chosen coupling constants, or as a limit of such models (satisfying some mild tail conditions). The $\phi ^ { 4 }$lattice model belongs to the Grifiths-Simon class. For this reason, most techniques that are at our disposal for the Ising model apply to the Grifiths-Simon class. This makes the Ising model an object of major interest when working on CQFT. The developments of the model have therefore been deeply connected to CQFT in the eighties, and we now discuss some examples of such interactions.

## 6.2. Reflection positivity

The notion of reflection positivity was introduced in Quantum Field Theory in the work of Osterwalder-Schrader [88], and we refer to [16] for a review. While reflection positivity did not emerge initially as a property of the Ising model, the model remains one of the most natural instances of a reflection positive model, and some of the most striking applications of reflection positivity are indeed dealing with the Ising model.

Consider the Ising model on a �-dimensional torus$\mathbb { T } _ { L } : = ( \mathbb { Z } / L \mathbb { Z } ) ^ { d }$with � even and split equally the torus into two pieces$\mathbb { T } _ { L } ^ { + }$and$\mathbb { T } _ { L } ^ { - }$using hyperplanes (the two pieces are isomorphic to$[ 0 , L / 2 ] \times ( \mathbb { Z } / L \mathbb { Z } ) ^ { d - 1 } )$) and consider a reflection � with respect to one of these hyperplanes mapping$\mathbb { T } _ { L } ^ { + }$to$\mathbb { T } _ { L } ^ { - }$. We say that$\langle \cdot \rangle$is reflection positive if for al$f , g : \mathbb { T } _ { L } ^ { + } \to \mathbb { R }$

$$
\langle f \vartheta g \rangle = \langle g \vartheta f \rangle \quad \text { and } \quad \langle f \vartheta f \rangle \geq 0,\tag{6.6}
$$

or, in other words, that$f , g \mapsto \langle f \vartheta g \rangle$is a positive semi-definite symmetric bilinear form. The archetypical examples of reflection positive measures are the Ising n.n.f. measures$\langle \cdot \rangle _ { \mathbb { T } _ { L } , \beta , 0 } .$ but many other examples exist, including some Ising models with long-range interactions.

Reflection positivity has two important implications, namely gaussian domination leading to the infrared bound, and the chessboard estimate. By lack of space, and since most of the applications of reflection positivity to the specific example of the Ising model rely on the infrared bound, let us focus on it and gaussian domination.

Gaussian domination is a statement linking the partition function of the Ising model with magnetic field to the partition function of the model without it. Formally, it states that for every function h :$V  \mathbb { R } , Z _ { L } ( \mathbf { h } ) \leq Z _ { L } ( 0 )$, where

$$
Z _ {L} (\mathbf {h}) := \sum_ {\sigma \in \{- 1, 1 \} ^ {V}} \exp \left[ - \beta \sum_ {\{x, y \} \in E (\mathbb {T} _ {L})} \left(\sigma_ {x} - \sigma_ {y} + \mathbf {h} _ {x} - \mathbf {h} _ {y}\right) ^ {2} \right].\tag{6.7}
$$

Gaussian domination can be proved via reflection positivity through the two hyperplanes mentioned above to show that for each h, a symmetric version of h with respect to a hyperplane has a larger value of$Z _ { L } ( \cdot )$. Gaussian domination immediately implies a Fourier version of the infrared bound by using a second-order expansion of$Z _ { L } ( \mathbf { h } )$near 0: for �$> 2$and every $( a _ { x } ) \in \mathbb { C } ^ { \mathbb { T } _ { L } }$summing to zero,

$$
\sum_ {x, y \in \mathbb {T} _ {L}} a _ {x} \overline {{a}} _ {y} \langle \sigma_ {x} \sigma_ {y} \rangle_ {\mathbb {T} _ {L}, \beta , 0} \leq \frac {2}{\beta} \sum_ {x, y \in \mathbb {T} _ {L}} a _ {x} \overline {{a}} _ {y} G (x, y),\tag{6.8}
$$

where$G ( x , y )$is the Green function of the simple random walk on$\mathbb { Z } ^ { d }$

In the specific case of the Ising model, the Messager-Miracle-Solé inequality enables to turn this Fourier estimate into a pointwise estimate on the two-point function: there exist $C , C ^ { \prime } > 0$such that for every$\beta > 0$and every �,$y \in \mathbb { Z } ^ { d }$

$$
\langle \sigma_ {x} \sigma_ {y} \rangle_ {\beta , 0} - m ^ {*} (\beta) ^ {2} \leq \frac {C}{\beta} G (x, y) \leq \frac {C ^ {\prime}}{\| x - y \| _ {2} ^ {d - 2}}.\tag{6.9}
$$

This is particularly interesting when$\beta$approaches$\beta _ { c }$from below, as it implies that the spin spin correlations decay algebraically fast at$\beta _ { c }$, with an exponent at least$d - 2$

## 6.3. The random current revolution

The context of CQFT was also at the origin of one of the most important revolutions in our understanding of the Ising model that we will describe in Section 6.4. The technique, called the random current representation, was introduced by Grifiths and greatly developed by Aizenman. It became one of the most powerful and robust tools available to mathematicians to study the Ising model. We describe it now (see [35] for a review).

The whole story starts with the observation that the component$\mathrm { { s x p } } [ \beta \sigma _ { x } \sigma _ { y } ]$of the Hamiltonian term attached to each edge can be rewritten using Taylor’s expansion to get

$$
Z (G, \beta , 0) = \sum_ {\sigma \in \{- 1, 1 \} ^ {V}} \prod_ {\{x, y \} \in E} \sum_ {\mathbf {n} _ {\{x, y \}} = 0} ^ {\infty} \frac {(\beta \sigma_ {x} \sigma_ {y}) ^ {\mathbf {n} _ {\{x , y \}}}}{\mathbf {n} _ {\{x , y \}} !} = \sum_ {\mathbf {n} \in \mathbb {Z} _ {+} ^ {E}} w _ {\beta} (\mathbf {n}) \sum_ {\sigma \in \{- 1, 1 \} ^ {V}} \prod_ {x \in V} \sigma_ {x} ^ {\Delta_ {x} (\mathbf {n})},\tag{6.10}
$$

where

$$
w _ {\beta} (\mathbf {n}) := \prod_ {\{x, y \} \in E} \frac {\beta^ {\mathbf {n} _ {\{x , y \}}}}{\mathbf {n} _ {\{x , y \}} !} \quad \text { and } \quad \Delta_ {x} (\mathbf {n}) := \sum_ {y \in V: \{x, y \} \in E} \mathbf {n} _ {\{x, y \}}.\tag{6.11}
$$

Now, the involutions on spin configurations switching the spins at a vertex immediately imply that the sum on$\sigma$on the right-hand side is either equal to$2 ^ { | V | }$if$\Delta _ { x } ( \mathbf { n } )$is even for all$x \in V$ or 0 otherwise (this seems like a very elementary observation, but it bears at the heart of it the$+ / -$symmetry of the space of possible spins).

Call a function from$E$to$\mathbb { Z } _ { + }$a current. A source of the current will be a vertex � with$\Delta _ { x } ( \mathbf { n } )$odd. The set of sources will be denoted by$\partial \mathbf { n }$. The previous discussion and the notation lead to the identity

$$
Z (G, \beta , 0) = 2 ^ {| V |} \sum_ {\partial \mathbf {n} = \emptyset} w _ {\beta} (\mathbf {n}),\tag{6.12}
$$

where from now on we omit to specify that we consider currents when using the notation n.

A current n with$\partial \mathbf { n } = A$can be interpreted as the occupation time of a collection of paths pairing vertices of � and loops – or equivalently the number of times the collection of paths and loops goes through an edge. The decomposition into loops and paths is not unique, nonetheless it remains interesting to interpret currents in terms of them

Proceeding in a similar fashion with the numerator of the spin-spin correlations, we get that

$$
\langle \sigma_ {A} \rangle_ {G, \beta , 0} = \frac {\sum_ {\partial \mathbf {n} = A} w _ {\beta} (\mathbf {n})}{\sum_ {\partial \mathbf {n} = \emptyset} w _ {\beta} (\mathbf {n})}.\tag{6.13}
$$

In words, one may write spin-spin correlations in terms of weighted sums of currents with specific source constraints$\partial \mathbf { n } = A$and$\partial \mathbf { n } = \boldsymbol { \emptyset }$. Note that the source constraint is not the same for the numerator and denominator.

## Frame 4: the high-temperature expansion and$\beta _ { c } > 0$

The high-temperature expansion of the Ising model, due to van der Waerden [100], can be neatly defined here as the set of edges with an odd current (it can also be obtained by a direct expansion using that exp$[ \beta \sigma _ { x } \sigma _ { y } ] = \cosh ( \beta ) + \sinh ( \beta ) \sigma _ { x } \sigma _ { y } )$. One ends up with another expression of the partition function in terms of even subgraphs

$$
Z (G, \beta , 0) = \cosh (\beta) ^ {| E |} \sum_ {F \in \operatorname{Even} (G)} \tanh (\beta) ^ {| F |},\tag{6.14}
$$

which resembles the low-temperature expansion, except that it is on � instead of$G ^ { * }$and that it is valid for arbitrary graphs and not only planar ones. In particular, one may easily deduce the Kramers-Wannier duality between the low and high temperature expansions at temperatures$\beta$and$\beta ^ { * }$satisfying tanh$( \beta ) = e ^ { - 2 \beta ^ { * } }$in the case of the square lattice.

One application of currents (or alternatively high-temperature expansion) is obtained by considering a mapping from currents with${ \partial \bf n } = \{ x , y \}$to currents with $\partial \mathbf { n } = \boldsymbol { \emptyset }$setting the current on a path from � to � of odd current (such a path necessarily exists) to 0. This many-to-one mapping (one has to keep track of the path and the value of the current on it to reconstruct the preimage) increases drastically the weight of the current as soon as$\beta \ll 1$, which shows that the spin-spin correlations$\langle \sigma _ { x } \sigma _ { y } \rangle _ { G , \beta , 0 }$are decaying exponentially fast in this regime. This implies in particular that$\beta _ { c } > 0$

A key observation of Aizenman is that the so-called switching lemma, see Frame 5, pertaining to combinatorial properties of the random current model, could be used to reinterpret spin-spin correlations as well as many other properties in terms ofprobabilities involving multiple independent currents. This lemma completely changed the point of view on currents, as it transforms them from a combinatorial type object into a probabilistic one. In particular, intuitions coming from probabilistic models such as random walks and percolation was later used to prove new theorems on the Ising model; see Sections 6.4, 6.6, and 7.1.

## Frame 5: the switching lemma for random currents

Write$\mathbf { n } \in \mathcal { F } _ { A }$if there exists$\mathbf { k } \leq \mathbf { n }$with$\partial \mathbf { k } = A$. Note that if$A = \{ x , y \}$, this is equivalent to the existence of a path from � to � which is made of edges with a positive current. Recall that �Δ� denotes the symmetric diference of the sets � and �. With this notation, the switching lemma [59] states that for every$F : \mathbb { Z } _ { + } ^ { E } \to \mathbb { R }$and every two sets of vertices �$B \subset V$,

$$
\sum_{\substack{\partial \mathbf{n}_{1} = A\\ \partial \mathbf{n}_{2} = B}}w(\mathbf{n}_{1})w(\mathbf{n}_{2})F(\mathbf{n}_{1} + \mathbf{n}_{2}) = \sum_{\substack{\partial \mathbf{n}_{1} = A\Delta B\\ \partial \mathbf{n}_{2} = \emptyset}}w(\mathbf{n}_{1})w(\mathbf{n}_{2})F(\mathbf{n}_{1} + \mathbf{n}_{2})\mathbb{I}(\mathbf{n}_{1} + \mathbf{n}_{2}\in \mathcal{F}_{B}).\tag{6.15}
$$

The name of the lemma is fairly self-explanatory, as it consists, when considering sums of two currents, of a recipe to switch the sources from the second one to the first one. The proof is a very entertaining combinatorial problem that is left to the reader.

A direct application (to illustrate the strength of the lemma) is the case$A = B$ which gives immediately that

$$
\langle \sigma_ {A} \rangle_ {G, \beta , 0} ^ {2} = \mathbb {P} _ {G} ^ {\emptyset} \otimes \mathbb {P} _ {G} ^ {\emptyset} [ \mathbf {n} _ {1} + \mathbf {n} _ {2} \in \mathcal {F} _ {A} ],\tag{6.16}
$$

where$\mathbb { P } _ { G } ^ { B }$is the measure on currents n on � with$\partial \mathbf { n } = B$attributing to each such n a probability that is proportional to$w ( \mathbf { n } )$, and$\otimes$denotes the product for probability measures. In words, one may interpret the square ofspin-spin correlations$\langle \sigma _ { A } \rangle _ { G , \beta , 0 }$as the probability, for the sum of two independent random currents, of pairing the elements of � by paths of positive current. One may also try as an exercise to recover Grifiths inequalities from the switching lemma.

## 6.4. Triviality in dimension �$> 4$

In 1982, Michael Aizenman and Juerg Fröhlich [2,49] independently proved that the scaling limit of the Ising model is trivial in dimension five and more in the following sense. Consider discrete smeared averages defined by

$$
T _ {f, L} (\sigma) := \frac {1}{\sqrt {\Sigma_ {L}}} \sum_ {x \in \mathbb {Z} ^ {d}} f (x / L)   \sigma_ {x}  ,\tag{6.17}
$$

where � ranges over compactly supported continuous functions, and$\begin{array} { r } { \Sigma _ { L } : = \Big \langle \big ( \sum _ { x \in \Lambda _ { L } } \sigma _ { x } \big ) ^ { 2 } \Big \rangle } \end{array}$ denotes the variance of the sum of spins over the box of size �. The theorem states that when $d > 4$, these smeared averages$T _ { f , L } ( \sigma )$are approximately Gaussian of variance$\langle T _ { f , L } ( \sigma ) ^ { 2 } \rangle _ { \beta }$ in the sense that there exists an explicit constant$C _ { f } > 0$such that for every$\beta \leq \beta _ { c }$, every $L \le \xi ( \beta )$, and every$z > 0$

$$
\left| \left\langle \exp [ z T _ {f, L} (\sigma) - \frac {z ^ {2}}{2} \langle T _ {f, L} (\sigma) ^ {2} \rangle_ {\beta} ] \right\rangle_ {\beta} - 1 \right| \leq \frac {C _ {f} z ^ {4}}{L ^ {d - 4}}.\tag{6.18}
$$

In words, the previous statement claims that the characteristic function of$T _ { f , L } ( \sigma )$is close to the one of a Gaussian random variables.

As a direct consequence of this result, one obtains that any well-defined scaling limit of the Ising model, and in fact more generally of the$\phi ^ { 4 }$lattice model, is inevitably Gaussian. The result marked a brutal stop in the CQFT program outlined in Section 6.1 as the proofs suggested, while not proving, that the model should also be trivial in four dimensions.

As mentioned above, one of the most striking applications of the random current representation is related to CQFT. Indeed, Aizenman’s proof of this theorem relies on a beautiful parallel between random walks and the paths joining sources in currents. We do not resist discussing this link below. But before doing so, let us mention that the approach of Fröhlich in [49], based on the Brydges-Fröhlich-Spencer (BFS) walk representation of spinspin correlations [21], is deeply connected to the random current as well. The walks in the BFS representation play the roles of the paths between sources in the random current. The advantage of this alternative approach is that it works for more general models, at the cost of losing the switching lemma and its benefits.

Let us focus on the four-point function and define the corresponding Ursell function given, for$x _ { 1 } , \ldots , x _ { 4 } \in \mathbb { Z } ^ { d }$, by

$$
U _ {4} ^ {\beta} (x _ {1}, \ldots , x _ {4}) := \langle \sigma_ {x _ {1}} \dots \sigma_ {x _ {4}} \rangle_ {\beta} - \sum_ {\pi \text {pairing}} \prod_ {i = 1} ^ {2} \langle \sigma_ {x _ {\pi (2 i - 1)}} \sigma_ {x _ {\pi (2 i)}} \rangle_ {\beta}.\tag{6.19}
$$

A simple exercise involving the switching lemma shows that

$$
U _ {4} ^ {\beta} (x _ {1}, \ldots , x _ {4}) = - 2 \langle \sigma_ {x _ {1}} \sigma_ {x _ {2}} \rangle \langle \sigma_ {x _ {3}} \sigma_ {x _ {4}} \rangle \mathbb {P} ^ {\{x _ {1}, x _ {2} \}} \otimes \mathbb {P} ^ {\{x _ {3}, x _ {4} \}} [ x _ {1}, \ldots , x _ {4}
$$

$$
\left. \mathbf {n} _ {1} + \mathbf {n} _ {2} \right]\tag{6.20}
$$

where connected in$\mathbf { n } _ { 1 } + \mathbf { n } _ { 2 }$means being connected by a path of edges with$\mathbf { n } _ { 1 } + \mathbf { n } _ { 2 }$not equal to zero. If one remembers that one can think of a current with sources$x _ { 1 }$and$x _ { 2 }$as a path connecting the two vertices together with a collection of loops, one can reinterpret the right-hand side of the previous identity at the light of so-called random walks (a random walker traces his way through the vertices ofa graph by picking its next steps at random among neighbours of where it currently stands – this Markov process is one of the most fundamental objects of probability theory). It is a classical result that two random walks connecting two pairs of points that are at a mutual distance of order � intersect with a probability bounded away from 0 as � tends to infinity in dimensions$d < 4 .$, and tending to zero in dimension $d \ge 4$

At this stage, it is totally unclear why the paths linking the points$x _ { 1 }$and � in${ \bf n } _ { 1 }$, and $x _ { 3 }$and$x _ { 4 }$in${ \bf n } _ { 2 }$, would behave as random walks. It is also unclear what would be the impact of the additional loops. Still, it is tempting to think that if an analogy with random walks was valid, then it would single out dimensions$d \ge 4$as being dimensions for which$U _ { 4 } ^ { \beta }$becomes much smaller than products of two-point correlations or, in other words, for which Wick’s law would become asymptotically valid, thus hinting at triviality.

When the dimension is strictly larger than 4, the story for random walks becomes even simpler, as the expected number of intersections is also tending to zero with �. Using the infrared bound to estimate the spin-spin correlations of the Ising model, one may go around the dificulty of proving a random walk type behaviour for currents to show that the intersection probability is tending to 0.

Making the argument work for currents in dimension 4 is more subtle because, contrarily to larger dimensions, the expected number of intersections does not tend to 0 when � tends to infinity. Hence, in order to prove that the intersection probability goes to 0, one inevitably has to go deeper in the understanding of the analogy between currents and random walks.

## 6.5. Rigorous renormalisation group in 4D Ising

The triviality of the Ising model in dimension$d > 4$naturally raises the question of its triviality in dimension$d = 4$, which is not only the pertinent physical dimension for CQFT, but also for the so-called 4 − � expansions providing information on dimension 3. In the eighties, Wilson’s renormalisation group method was already in every physicists’ toolbox, yet the challenges to overcome to cast the general theory in a mathematical framework seemed out of reach. Interestingly, a very relevant case became an important exception.

Consider the lattice version of the$\phi ^ { 4 }$model discussed in Section 6.1. The case $b = \lambda = 0$corresponds to a Gaussian field known under the name of discrete Gaussian Free Field (GFF), which enjoys a number of striking features. One of them is that the model converges, when rescaling the lattice, to the continuum GFF. In a series of impressive papers [43, 51, 62], mathematical physicists proved in the eighties that, when starting from a weakly coupled$\phi ^ { 4 }$lattice model (meaning that � is small), one may apply a multi-scale analysis to prove convergence of the model to the continuum GFF.

Several methods were used at the time, but let us mention that the method of Gawedski and Kupiainen [51] can be thought of as a rigorous version of Kadanof block-spin renormalisation procedure. It consists of writing the model in terms of averages of spins over large blocks of size$L ^ { k }$, and to average them out scale by scale. At leading order, each step of the procedure boils down to modifying the parameters of the model. Of course, the reality is much more complicated than the first order analysis suggests, and the renormalisation scheme is quite complex.

An alternative to this block-spin renormalisation was later developed by Bauer schmidt, Brydges, and Slade [11] in order to obtain refined results, as well as to treat more general models. In these alternative approaches, the block-spin analysis is replaced by the following strategy: one thinks of quantities in the$\phi ^ { 4 }$lattice model as being expressed in terms of the discrete GFF itself. In order to control the asymptotic behaviour of such quantities, one decomposes the covariance of the discrete GFF into a sum of finite-range covariances that one integrates out one by one. At each step a change of the parameters of the system is required to keep things converging towards a limit. Doing so enables the authors to focus their attention on how the parameters evolve under this procedure. This evolution can be thought of as the renormalisation map in the renormalisation group.

The level of sophistication of these techniques is quite astonishing, and the precision of the results outstanding. As one may guess, this comes at a price. At the bottom of both strategies lies the fact that the original$\phi ^ { 4 }$lattice model is in the “vicinity of a model”, the Gaussian Free Field, that enjoys a number of nice properties. As a result, the technique is (as for today) perturbative in nature, which is somehow its main limitation. We will see another instance of such a renormalisation scheme, this time near another fixed point, when discussing the 2D Ising model.

## 6.6. Forty years later: the random current strikes back

While renormalisation techniques provided impressive rigorous results in dimension 4, they remained as we mentioned perturbative, meaning that they required that the lattice$\phi ^ { 4 }$ model one starts from has a small$\phi ^ { 4 }$term. Yet, if one would like to construct a non-trivial 4D quantum field theory, one would definitely try to start with a strongly coupled$\phi ^ { 4 }$lattice model (meaning with a$\phi ^ { 4 }$terms which is not a priori small), for instance working with the Ising model which in some sense can be thought of as the model with the strongest possible coupling, thus excluding existing renormalisation group techniques.

This asks for another approach, and this is probably why one had to wait for forty years to finally obtain a proof of the triviality of the 4D Ising and$\phi ^ { 4 }$lattice models, which states [4] that there exists$c > 0$such that for the n.n.f.$\phi ^ { 4 }$lattice model on${ \mathbb { Z } } ^ { 4 }$with parameters $b , \lambda .$, and a compactly supported continuous function$f ,$, there exists$C _ { f } > 0$such that for every$\beta \leq \beta _ { c } = \beta _ { c } ( b , \lambda )$, every$L \le \xi ( \beta )$, and every$z > 0$7

$$
\left| \left\langle \exp [ z T _ {f, L} (\varphi) - \frac {z ^ {2}}{2} \langle T _ {f, L} (\varphi) ^ {2} \rangle_ {\beta} ] \right\rangle_ {\beta} - 1 \right| \leq \frac {C _ {f} z ^ {4}}{(\log L) ^ {c}}.\tag{6.21}
$$

The strategy of the proof uses a more delicate probabilistic perspective on the random current than in [2], still keeping in mind the interpretation in terms of random walks of the paths joining the sources of the current. Indeed, it can be proved that two random walkers in four dimensions going from points to points that are all at a mutual distance of order � intersect with probability of order (log$L ) ^ { - c }$for some universal constant$c > 0$. The reason is that while the expected number of intersections is of order 1, the number of intersections, when such intersections exist, is with high probability quite large in � (and is growing with $L )$. The core of the paper is to apply a similar argument to the paths in the random current. Of course, challenges emerge when trying to handle the highly non-Markovian paths obtained by considering the paths joining the sources in currents. Nevertheless, guided by the random walk intuition, one can build a multi-scale analysis to prove that conditioned on intersecting, random currents intersect a large number of times, and ultimately deduce from this the triviality result.

## 7. The last fifty years: Ising model and percolation

Percolation theory gathers under its umbrella a variety of random graphs systems. A configuration on$G = ( V , E )$is an element$\omega = ( \omega _ { e } : e \in E ) \in \{ 0 , 1 \} ^ { E }$which is interpreted as a subgraph with vertex-set � and edge-set$\{ e \in E : \omega _ { e } = 1 \}$. Then, diferent percolation models can be defined by considering diferent measures on$\{ 0 , 1 \} ^ { E }$. Historically, the original model, called Bernoulli percolation, is defined in such a way that the$\omega _ { e }$are independent Bernoulli random variables. It was introduced to understand the behaviour ofliquid in a porous medium. Nevertheless, the theory of non-Bernoulli models has been found to be related to a variety of other models of statistical physics explaining various physical phenomena.

As often, the Ising model has played an essential role in the development of percolation theory, and conversely certain advances in percolation theory have been fundamental to our understanding of the Ising model. Sometimes, the link between the two models is simply an analogy between their behaviours, but sometimes the connection is much more direct. For instance, spin-spin correlations can be rewritten in terms of a percolation model, in which case we speak of the percolation model as being a graphical representation of the Ising model. We now propose to discuss some examples of these links between the Ising model and percolation.

## 7.1. Percolation interpretation of random currents

We have seen one example ofa graphical representation in Frame 5 where the squares of spin-spin correlations get rephrased as connectivity properties of the sum of two currents.

One may easily define a percolation model out of the pair of currents above by saying that for an edge$\{ x , y \} , \omega _ { \{ x , y \} } = 1 \mathrm { i f } ( \mathbf { n } _ { 1 } + \mathbf { n } _ { 2 } ) _ { \{ x , y \} } > 0$. Then, the square of the spin-spin correlations between two points becomes the probability, for this percolation model, that � and$y$are connected in$\omega .$

The best illustration of how intuition from percolation or the Ising model can drive developments on the other model is provided by an important result on the Ising model in the regime$\beta < \beta _ { c }$. This result from 1987, due to Aizenman, Barsky and Fernandez [3] (see [39] for an alternative argument), states that correlations of the n.n.f. Ising model decay exponentially fast as soon as$\beta < \beta _ { c }$in the sense that for each such$\beta ,$, there exists$\tau > 0$such that for every $x , y \in \mathbb { Z } ^ { d }$,

$$
\langle \sigma_ {x} \sigma_ {y} \rangle_ {\beta , 0} \leq \exp (- \tau \| x - y \|).\tag{7.1}
$$

We say that the phase transition is sharp: there is no intermediate phase$( \beta _ { \mathrm { { e x p } } } , \beta _ { c } )$in the Ising model in which spin-spin correlations would decay polynomially. Let us mention that a similar exponential decay was obtained recently for truncated correlations$\langle \sigma _ { x } \sigma _ { y } \rangle _ { \beta , 0 } -$ $m ^ { * } ( \beta ) ^ { 2 }$when$\beta > \beta _ { c }$, see [36].

This theorem is of fundamental importance for the following reason. Perturbative results, which are combinatorial in nature, are valid under the assumption that certain quantities decay exponentially fast, and in fact with a rate of decay which is suficiently large. While this hypothesis is important to apply the techniques, it happens to be of little relevance from a physical point of view. In fact, one expects that most of the phenomenology remains unchanged as long as spin-spin correlations decay exponentially fast. As a consequence, (7.1) can be thought of as a bottleneck in the understanding of the phase$\beta < \beta _ { c }$: as soon as it is obtained, a number of important results can be derived from it. As an example, the results on fluctuations of interfaces and Ornstein-Zernike estimates were proved to hold in the whole regime$\beta < \beta _ { c }$. The result also provides meaning to the correlation length$\xi ( \beta )$mentioned in Section 4.1, as it proves that it is finite as soon as$\beta < \beta _ { c }$

Let us now comment on the proof. The argument relies on a fruitful idea consisting in deriving diferential inequalities between thermodynamical quantities of the Ising model. The archetypical example of such diferential inequalities are given, for the problem at hand, by (recall that the magnetisation$m = m ( \beta , h )$is a function of$\beta$and ℎ)

$$
m \leq \tanh (\beta h) \frac {\partial}{\partial (\beta h)} m + m ^ {2} \left(\beta \frac {\partial}{\partial \beta} m + m\right) \quad \text { and } \quad m \frac {\partial}{\partial \beta} m \geq c.\tag{7.2}
$$

The interesting feature here is that similar diferential inequalities appear when studying Bernoulli percolation. In fact, a number of results were obtained in parallel during the eighties, where each result for Ising had its pendant for Bernoulli percolation, and vice versa. As an example, critical exponents for$d > 4$were obtained by Aizenman and Fernandez [7] using diferential inequalities that can be adapted to Bernoulli percolation. These techniques are useful to transform qualitative results (e.g. a quantity tends to 0) to quantitative ones (e.g. exponentially fast). We do not resist mentioning one of them: for$h = 0$and$\beta < \beta _ { c }$<sub>�</sub>,

$$
\left(1 - \frac {B}{\chi}\right) \frac {2 d \chi^ {2}}{1 + B} \leq \frac {\partial}{\partial \beta} \chi \leq 2 d \chi^ {2},\tag{7.3}
$$

where$\chi ( \beta ) : = \sum _ { x } \langle \sigma _ { 0 } \sigma _ { x } \rangle _ { \beta , 0 }$is the susceptibility, and$B ( \beta )$is the Bubble diagram and is given by

$$
B (\beta) := \sum_ {x \in \mathbb {Z} ^ {d}} \langle \sigma_ {0} \sigma_ {x} \rangle_ {\beta , 0} ^ {2}.\tag{7.4}
$$

Since the Infrared Bound implies that$B ( \beta )$remains bounded uniformly in$\beta < \beta _ { c }$as soon as$d > 4 , \chi ( \beta )$must blow up like$1 / | \beta - \beta _ { c } |$as$\beta$approaches$\beta _ { c }$from below.

Another striking instance of how fruitful the connection between percolation models and the Ising model was for the development of both models is the following continuity resul of the phase transition of the 3D Ising model, due to [5], stating that the n.n.f. Ising model satisfies$m ^ { * } ( \beta _ { c } ) = 0$for every$d \ge 3$

The argument relies on percolation methods applied to the double random current representation of an argument of Burton and Keane proving the uniqueness of the infinite connected component of percolation. The whole argument can be improved and extended to study all translation-invariant Gibbs measures, obtaining the classification result already mentioned in Section 5.2.

## 7.2. Fortuin-Kasteleyn percolation

Another (and in fact older) example of a graphical representation is provided by a special case of the Fortuin-Kasteleyn (FK) percolation. In this model, introduced in [47], the measure$\phi _ { G , p , q }$is given, for$G = ( V , E )$finite and$\omega \in \{ 0 , 1 \} ^ { E }$, by

$$
\phi_ {G, p, q} [ \{\omega \} ] := \frac {1}{Z (G , p , q)} p ^ {| \omega |} (1 - p) ^ {| E | - | \omega |} q ^ {k (\omega)},\tag{7.5}
$$

where$p \in [ 0 , 1 ]$and$q > 0$are the parameters of the model, called respectively the edgeweight and the cluster-weight,$\begin{array} { r } { | \omega | : = \sum _ { e \in E } \omega _ { e } } \end{array}$is interpreted as the number of edges in �, and$k ( \omega )$is the number of connected components of �.

When$q = 1$, one ends up with the classical Bernoulli percolation model in which the$\omega _ { e }$are independent. When$q \neq 1$, the state of edges is no longer independent and one ends up with a dependent percolation model whose study is central in modern probability theory. From now on, we focus on the case$q = 2$, which we call the FK Ising model. We confine our discussion to two features of this percolation model, namely its link to the Ising model, and the FKG inequality.

Let us start with the former, which provides a recipe to obtain the Ising model configuration out of FK Ising; see Figure 3. Consider a random variable$\omega \in \{ 0 , 1 \} ^ { E }$with the law of FK Ising with parameter$p \in [ 0 , 1 ]$and construct$\sigma \in \{ - 1 , 1 \} ^ { V }$by

• choosing for every connected component C of <sub>�</sub> a spin$\sigma _ { C }$uniformly between −1 and +1, and independently of the other connected components.

• defining$\sigma _ { x } = \sigma _ { C }$for every C and every$x \in C$

Then,$\sigma$has the law of the Ising model on � with parameter$\textstyle { \beta = { \frac { 1 } { 2 } } \log [ 1 / ( 1 - p ) ] }$and$h = 0$ This coupling, due to Fortuin and Kasteleyn and often referred to as the Edwards-Sokal coupling due to the paper [40], enables to express correlation functions of the Ising model in terms of FK Ising. For instance, by decomposing on the events that � is connected to � or not

![](images/page_31_image_0.jpg)

Figure 3

The Edwards-Sokal coupling, with on the left a picture of the FK Ising configuration (bold edges are those with $\omega _ { e } = 1 )$, in the middle, spins are attached to each cluster (one example in black and others in grey), and on th right, the spins without the FK Ising configuration.

in �, one easily gets that

$$
\langle \sigma_ {x} \sigma_ {y} \rangle_ {G, \beta , 0} = \phi_ {G, 1 - e ^ {- 2 \beta}, 2} [ x \text {   connected   to   } y \text {   in   } \omega ].\tag{7.6}
$$

Similarly,$\langle \sigma _ { A } \rangle _ { G , \beta , 0 } = \phi _ { G , 1 - e ^ { - 2 \beta } , 2 } [ \mathcal { F } _ { A } ]$, where$\mathcal { F } _ { A }$is the event that each connected component of � contains an even number (possibly equal to 0) of vertices in �. Another interesting feature of this coupling is that it is at the basis of so-called cluster algorithms due to Swendsen and Wang, who used it to speed up the Glauber dynamics and the simulation of the Ising model, in particular near the critical point. The interest of FK Ising and more generally FK percolation models with$q \geq 1$is that they enjoy some nice monotonicity properties (dependent percolation models satisfying these properties have been an object of intense study in the past ten years). Let us mention two such properties. The Fortuin-Kasteleyn-Ginibre (FKG) inequality states that for every increasing functions$f , g : \{ 0 , 1 \} ^ { E } \to \mathbb { R }$

$$
\phi_ {G, p, q} [ f g ] \geq \phi_ {G, p, q} [ f ] \phi_ {G, p, q} [ g ].\tag{7.7}
$$

This inequality is often used for indicator functions of increasing events (i.e. events for which the indicator function is an increasing function), in which case the inequality states that increasing events are positively correlated. Another manifestation of the monotonicity prop erties is the monotonicity in$p \mathrm { : }$for every increasing function$f : \{ 0 , 1 \} ^ { E } \to \mathbb { R }$and$p ^ { \prime } \geq p$,

$$
\phi_ {G, p ^ {\prime}, q} [ f ] \geq \phi_ {G, p, q} [ f ].\tag{7.8}
$$

These monotonicity properties are particularly useful. The second one applied to FK Ising and the indicator function of$\mathcal { F } _ { A }$implies that$\langle \sigma _ { A } \rangle _ { G , \beta , 0 }$is increasing in$\beta ,$, and the first one applied to indicator functions of$\mathcal { F } _ { A }$and$\mathcal { F } _ { B }$implies the second Grifiths inequality $\langle \sigma _ { A } \sigma _ { B } \rangle _ { G , \beta , 0 } \geq \langle \sigma _ { A } \rangle _ { G , \beta , 0 } \langle \sigma _ { B } \rangle _ { G , \beta , 0 } .$

## 7.3. The broader impact of the Ising model on dependent percolation models

In the first fifty years that followed its introduction, the theory of percolation was much more advanced for Bernoulli percolation than for other dependent percolation models.

The past ten years have seen tremendous progress in bridging the gap between our understanding of the Bernoulli case and the others. The interplay between dependent percolation models and the Ising model has been fundamental for these developments.

We already saw that the Ising model is related to FK Ising and a percolation model created out of random currents. It does not come as a surprise that one of the first dependent percolation models to see significant progress in its understanding was the FK Ising. Of course, the Edwards-Sokal coupling enables to transfer immediately certain known facts about the Ising model to its percolation representation (for instance, the critical point of the FK Ising on${ \mathbb { Z } } ^ { 2 }$is$1 - e ^ { - 2 \beta _ { c } } = \sqrt { 2 } / ( 1 + \sqrt { 2 } )$thanks to Onsager’s result). Also, the model enjoys some specific features that make its direct analysis simpler than for other dependent percolation models.

For all these reasons, the FK Ising became the entrance gate to a new realm of results on dependent percolation models. A perfect illustration of this is provided by the study of crossing probabilities for planar dependent percolation models. Let us provide slightly more detail.

One important feature of critical dependent percolation models in two dimensions is that they satisfy the box-crossing property (BCP), and its connected notion the Russo-Seymour-Welsh theory (RSW). More precisely, if for a rectangle �, the event Cross(�) corresponds to the existence of a path in � between the left and right sides of �, the properties (BCP) and (RSW) for a percolation model on${ \mathbb { Z } } ^ { 2 }$with measure$\mathbb { P }$are the following:

• (BCP) for all$\rho > 0$, there exists$c > 0$such that for every$n \geq 1$

$$
c \leq \mathbb {P} [ \operatorname{Cross} ([ 0, \rho n ] \times [ 0, n ]) | \omega_ {| [ - n, (\rho + 1) n ] \times [ - n, 2 n ] ^ {c}} ] \leq 1 - c \text {   almost   surely. }\tag{7.9}
$$

• (RSW) for all$\rho > 0$, there exists$C > 0$such that for every$n \geq 1$

$$
\mathbb {P} [ \mathrm{Cross} ([ 0, \rho n ] \times [ 0, n ]) ] \geq \mathbb {P} [ \mathrm{Cross} ([ 0, n ] \times [ 0, \rho n ]) ] ^ {C}.\tag{7.10}
$$

These two properties have been the driving force of the progress in our understanding of the 2D dependent percolation models. The FK-Ising model played an essential role in these developments, as it was the first dependent percolation model for which (BCP) could be proved [37]. This development triggered a whole new direction of research that led to substantial progress in our understanding of (BCP) and (RSW) for various percolation models.

## 8. Over the last ten years: conformal invariance of the Ising mode

## 8.1. What is conformal invariance?

As mentioned before, Kadanof used his block-spin renormalisation to predict that the large scale properties of the critical Ising model were invariant under scaling. The same argument also leads to postulate translation and rotation invariance. In 1970, Polyakov [91] suggested a much stronger invariance of the model. Since we saw that it is natural to associate a QFT with the large scale properties of the critical Ising model, and since this QFT is a local field, these properties should be invariant under any map which is locally a composition of translation, rotation and homothety. As a corollary one predicts full conformal invariance, i.e. invariance under all one-to-one holomorphic maps. This prediction was turned into a classification of possible conformal field theories (CFT) in 2D in seminal papers by Belavin, Polyakov and Zamolodchikov [12] that generated an explosion of activity, allowing non-rigorous explanations of many critical phenomena.

From a mathematical perspective, the notion of conformal invariance of a model is not straightforward to define. A number of interpretations of the limit of large scale properties – called the scaling limit – can be taken, and we mention a few now.

For clarity of the exposition, we focus on the critical Ising model on$\mathbb { Z } ^ { d }$and its rescaled versions$a \mathbb { Z } ^ { d }$for$a > 0$. We drop the subscript referring to$\beta$and ℎ as they are fixed to be equal to$\beta _ { c }$and 0 respectively. Consider a simply connected domain$\Omega \subset \mathbb { R } ^ { d }$

(Spins) The most natural approach is to consider the spin-spin correlations defined for every $a > 0$and$x _ { 1 } , \ldots , x _ { n } \in \Omega$by

$$
S _ {\Omega} ^ {(a)} (x _ {1}, \ldots , x _ {n}) := \langle \sigma_ {[ x _ {1} ] _ {a}} \ldots \sigma_ {[ x _ {n} ] _ {a}} \rangle_ {a \mathbb {Z} ^ {d} \cap \Omega},\tag{8.1}
$$

where$[ x ] _ { a }$is the vertex of$a \mathbb { Z } ^ { d } \cap \Omega$closest to �. These Schwinger functions already appeared as the key players in CQFT. One is then interested in the limit as � tends to 0 of these properly renormalised quantities. If the limit exists, we call it$S _ { \Omega } ( x _ { 1 } , \ldots , x _ { n } )$

(Energies) Another object of interest is the energy-energy correlations. For$a > 0$and $x _ { 1 } , \ldots , x _ { n } \in \Omega$, one considers at the quantities

$$
T _ {\Omega} ^ {(a)} (x _ {1}, \dots , x _ {n}) := \left\langle \varepsilon_ {(x _ {1}) _ {a}} \dots \varepsilon_ {(x _ {n}) _ {a}} \right\rangle_ {a \mathbb {Z} ^ {d} \cap \Omega},\tag{8.2}
$$

where$\varepsilon _ { \{ u , v \} } : = \sigma _ { u } \sigma _ { v } - \langle \sigma _ { u } \sigma _ { v } \rangle _ { a \mathbb { Z } ^ { d } }$and$( x ) _ { a }$is the edge closest to �. The quantity$\varepsilon _ { x }$is called the energy. One is again interested in the limit$T _ { \Omega } ( x _ { 1 } , \ldots . . , x _ { n } )$as � tends to 0 of these properly rescaled quantities.

(Geometry of interfaces) In two dimensions, another direction was proposed in the nineties. It consists in considering the low-temperature representation, i.e. the interfaces between plu and minus spins. In a domain$\Omega ,$it creates a family of non-intersecting loops together with arcs from boundary to boundary. Let${ \mathfrak { C } } _ { \Omega }$be the set of such collections of loops and arcs. The set${ \mathfrak { C } } _ { \Omega }$can be turned into a metric space by attaching a distance$d _ { \Omega }$which, heuristically, states that two configurations are close to each other when the large loops and arcs are close to each other. Let us call$C _ { \Omega } ^ { ( a ) }$the random variable obtained by considering the low-temperature expansion of a critical Ising model configuration in$a \mathbb { Z } ^ { d } \cap \Omega$. Here, we are interested in the limit of$C _ { \Omega } ^ { ( a ) }$as a random object.

Now, what do we mean by conformal invariance? Roughly speaking, we mean that certain quantities of the model are conformally covariant/invariant. With the definitions above, it would for instance mean that there exists a way of renormalising the$S _ { \Omega } ^ { ( a ) } ( x _ { 1 } , \ldots \ldots , x _ { n } )$ and$T _ { \Omega } ^ { ( a ) } ( x _ { 1 } , \dots , x _ { n } )$in such a way that they converge to quantities$S _ { \Omega } ( x _ { 1 } , \dots , x _ { n } )$and

$T _ { \Omega } ( x _ { 1 } , \dots , x _ { n } )$that satisfy that there exist$\Delta _ { \sigma } , \Delta _ { \varepsilon }$such that for every conformal (i.e. holomorphic and one-to-one) map$f : \Omega \to f ( \Omega )$, we have

$$
S _ {f (\Omega)} (f (x _ {1}), \ldots , f (x _ {n})) = | f ^ {\prime} (x _ {1}) | ^ {- \Delta_ {\sigma}} \dots | f ^ {\prime} (x _ {n}) | ^ {- \Delta_ {\sigma}} S _ {\Omega} (x _ {1}, \ldots , x _ {n}),\tag{8.3}
$$

$$
T _ {f (\Omega)} (f (x _ {1}), \ldots , f (x _ {n})) = | f ^ {\prime} (x _ {1}) | ^ {- \Delta_ {\varepsilon}} \dots | f ^ {\prime} (x _ {n}) | ^ {- \Delta_ {\varepsilon}} T _ {\Omega} (x _ {1}, \ldots , x _ {n}).\tag{8.4}
$$

For the geometry of interfaces, the situation is even simpler as one means that the family of loops and arcs${ C } _ { \Omega } ^ { ( a ) }$converges to a limit$C _ { \Omega }$as � tends to 0 and that this limit satisfies that $C _ { f ( \Omega ) }$and$f ( C _ { \Omega } )$have the same law for every conformal map$f : \Omega \to f ( \Omega )$).

## 8.2. Conformal invariance of the 2D Ising model

Around fifteen years ago, Smirnov [99] and Chelkak and Smirnov [28] obtained a major breakthrough towards proving conformal invariance of 2D Ising model. This fundamental proof, that we discuss below, opened the way to a very deep understanding of the scaling limit of the model.

A few years later, Chelkak-Izyurov-Hongler [27] proved conformal covariance of the spin-spin correlations (with$\Delta _ { \sigma } = 1 / 8 )$. It was later proved in [22] that the quantities $S _ { \Omega } ( x _ { 1 } , \ldots , x _ { n } )$are the Schwinger functions of a random distribution, that can be understood as the spin-field that physicists sometimes refer to. In the same spirit, conformal covariance of the energy-energy correlations was proved in [65] (with$\Delta _ { \varepsilon } = 1 )$). In this case, one may prove that the correlations are not the Schwinger functions of a random distribution. Turning to interfaces, the following result was the culmination of the theory: the arcs in$C _ { \Omega }$are given by the so-called free arc ensemble of parameter 3 and the loops by conformal loop ensembles of parameter 3 in the simply connected domains obtained as the complements of the arcs (see [13,14]). In particular, the scaling limit is conformally invariant. This body of work uses the ideas from [28, 99] together with the theory of the Schramm-Loewner evolution and its consequences.

As mentioned above, an important breakthrough came from the works [28,99] where conformal covariance of so-calledfermionic observables$f _ { \Omega } ^ { ( a ) }$is proved. Those observables are linear combinations of order-disorder operators (see Frame 6) considered by Kadanof and Ceva in [74], see also [26] for several connections to other classical objects.

## Frame 6: Fermionic observable

Consider a simply connected domain$\Omega \subset \mathbb { C }$and for$a > 0$, let � be the largest connected component of$a \mathbb { Z } ^ { 2 } \cap \Omega$. Consider � vertices$x _ { 1 } , \ldots , x _ { n }$of �, and � faces $f _ { 1 } , \ldots , f _ { n }$of � such that$f _ { i }$is bordered by$x _ { i }$for every$1 \leq i \leq n$. Choose � disjoint cuts $\ell _ { 1 } , \ldots , \ell _ { n }$, i.e. families of dual edges$( e _ { i } ^ { * } ( j ) )$forming self-avoiding paths in the dual from the unbounded face to the center of$f _ { i }$. Define the disorder operator$\mu _ { \ell }$for a cut ℓ as the observable that efectively switches the coupling constants of the edges$e _ { i } ( j )$ associated with the$e _ { i } ^ { * } ( j )$in the cut (it can be written as a product of terms of the form $\exp [ - 2 \beta \sigma _ { x } \sigma _ { y } ]$over edges appearing in the family of edges$\{ e _ { i } ( j ) : i , j \} )$). Then, the order-disorder correlations are given by the formula

$$
F _ {\Omega} ^ {(a)} (x _ {1}, f _ {1}, \ldots , x _ {n}, f _ {n}) := \langle \sigma_ {x _ {1}} \mu_ {\ell_ {1}} \ldots \sigma_ {x _ {n}} \mu_ {\ell_ {n}} \rangle_ {\Omega}.\tag{8.5}
$$

Let us mention that these quantities can be expressed in terms of correlations of Grassmann variables in the Schultz-Mattis-Lieb representation [95].

Smirnov introduced a fermionic observable$f _ { \Omega } ^ { ( a ) }$defined at centers of edges $\{ x , y \}$of � that can be written as a linear combination (with complex coeficients) of the$F _ { \Omega } ^ { ( a ) }$with$x _ { 1 }$equal to � or �, and$f _ { 1 }$to one of the two faces bordered by$\{ x , y \}$. The details of the definition are unimportant here and the take-home message is that Chelkak and Smirnov proved that the limit (as � tends to 0) of these fermionic observables is conformally covariant.

The conformal covariance of the fermionic observable should be understood as the first brick among the conformal covariance results of spin-spin, energy-energy correlations, and even of the conformal invariance of interfaces. Let us mention that these results require substantial additional ideas compared to [28,99]. In fact, conformal covariance/invariance of virtually all quantities one may be interested in the 2D Ising model can be recovered today.

The proof of the theorem relies on the observation that$f _ { \Omega } ^ { ( a ) }$is the solution of a discrete version of a Riemann-Hilbert boundary value problem. More precisely, the function can be proved, via combinatorial arguments involving the van der Waerden high-temperature expansion, to be preholomorphic (see Frame 7), and to satisfy certain boundary conditions. These special features are connected to the integrability of the model. From general principles on preholomorphic functions, the limit as � tends to 0 of these objects must be the holomorphic solution of a continuum Riemann-Hilbert boundary value problem, which can be computed and proved to be conformally covariant. Such reasoning has been used in several existing proofs of conformal invariance, for instance for dimers or Bernoulli site percolation on the triangular lattice. It has created an explosion of results in the field as many quantities can be proved to converge using a similar strategy.

## Frame 7: Preholomorphic observables

The notion of preholomorphic function on a planar graph � appeared implicitly in the work of Kirchhof on electrical networks [77]. It was explicitly linked to holomorphicity in the work of Isaacs [68, 69], in which the author proposed to discretise the Cauchy-Riemann equation to get to the definition (on the square lattice)

$$
F (N W) - F (S E) = i [ F (N E) - F (S W) ],\tag{8.6}
$$

where ��, ��, ��, and �� are the four corners found in counterclockwise order around each face, when starting from the top left vertex.

The properties of preholomorphic functions have been the object of a renewed interest with the emergence of the question of conformal invariance in connections to boundary value problems. Indeed, general theorems stating that preholomorphic functions satisfying certain boundary value conditions converge when taking finer and finer meshsize to holomorphic solutions of the continuum version of the boundary value problem took a central place in the theory.

In the case of the Ising model, the complexity of the boundary value problem (involving a condition on the argument of the fermionic observable) pushed Smirnov to introduce a stronger notion of preholomorphicity, called �-holomorphicity, which is also satisfied by fermionic observables. The advantage of this notion is that it enables one to define the imaginary part of the primitive of the square of the observable, which roughly speaking becomes the discrete solution of a Dirichlet boundary value problem, a much more tractable problem for which convergence (when � tends to 0) can be proved very elegantly.

## 8.3. Towards universality of the 2D Ising mode

As mentioned in Section 4.2.2, the large-scale properties of the critical Ising model should not depend on the precise properties of the underlying graph. With the tremendous successes that have been achieved over the years in the case of the Ising model on${ \mathbb { Z } } ^ { 2 }$and more generally on planar graphs, it is natural to test the validity of the universality hypothesis in this context. Several advances have been made in this direction in the last fifteen years.

The first impressive progress can be found in the work of Chelkak and Smirnov themselves [28]. They observed that the preholomorphicity argument leading to conformal invariance can be articulated naturally in the setting of so-called isoradial graphs. An isoradial graph is an embedding of a graph � in the plane such that every face of the graph is inscribed in a circle of radius 1. In this context, one may define special coupling constants $J _ { x , y }$depending on the graph in such a way that$\beta _ { c } = 1$and that the fermionic observable is naturally preholomorphic on this graph. Then, the strategy of Chelkak and Smirnov on the square lattice applies to isoradial graphs with the same conclusions. Note that this result can be understood as a universality result on the graph (isoradial graphs are a fairly large family of planar graphs, even though not fully general), but that the choice of$J _ { x , y }$is determined by the embedded graph itself. Moreover, a striking feature of this theorem is that no transitivity or quasi-transitivity is required for this to work.

In recent developments, Chelkak generalised the conformal invariance result to a wider class of Ising models, namely those defined on planar locally-finite doubly periodic weighted graphs$( G , J )$, i.e. weighted graphs which are invariant under the action of some lattice$\Lambda \approx \mathbb { Z } \oplus \mathbb { Z }$(in such case$G / \Lambda$is a finite graph embedded in the torus). For such models, Chelkak proved in [25] that there exists an embedding in the plane, called an �-embedding, with the property that the scaling limit of the critical model defined on this embedding is conformally invariant.

This result is a strong indication of universality for planar graphs. Now what happens beyond planar graphs? The universality conjecture asserts that the scaling limit depends on the large scale geometry of the graph (for instance a planar Euclidean geometry). In particular, one may consider the graph obtained with the vertex-set${ \mathbb { Z } } ^ { 2 }$and edge-set given by pairs ofvertices at a distance at most � ofeach other. This model, called thefinite-range model on${ \mathbb { Z } } ^ { 2 }$, should have a behaviour that is similar to the nearest-neighbour case as it is “almost planar”. The additional dificulty is that non-planarity immediately breaks the integrability of the system. The universality of such Ising models has been investigated in two diferent directions.

First, one may consider finite-range models that are perturbations of the nearestneighbour integrable case, meaning that non-nearest neighbour interactions are very weak, i.e. that$J _ { x , y }$is small when$1 < \| x - y \| _ { 2 } \leq R$. Using the Schultz-Mattis-Lieb Grassmann representation [95] of the nearest neighbour case, one may express the partition function and more generally the energy-energy and spin-spin correlations in terms of Grassmann variables, and therefore at the end in terms ofthe nearest-neighbour model. Using an elaborate multi-scale analysis and studying the renormalisation of parameters induced by this multi-scale analysis, Giuliani-Greenblatt-Mastropietro derived in [53] the large-scale behaviour of energy-energy correlations in the full plane. While the previously mentioned renormalisation schemes in dimension 4 were enabled by the fact that the model is a small perturbation of the discrete GFF (which is a gaussian process), the two-dimensional case relies on a similar connection, this time to the n.n.f. Ising model on${ \mathbb { Z } } ^ { 2 }$(which has a Grassmannian structure). As a consequence, the strategy sufers from the same limitations as the 4D case in the sense that it is restricted to small perturbations of the n.n.f. Ising model on${ \mathbb { Z } } ^ { 2 }$

A totally diferent approach explaining the emergence of planarity in finite range Ising models was proposed in [6] based on the random current representation. The underlying idea relies on the fact that thanks to the switching lemma, intersection properties of random currents with sources are related to the structure of �-point correlations in the model. Yet, the intersection properties of long paths on the graph induced by${ \mathbb { Z } } ^ { 2 }$and the edges between vertices at a distance � of each other resemble the ones that can be obtained for planar graphs. As an example of a possible application, one can obtain that spin-spin correlations on the boundary of a domain Ω have a Pfafian structure, a result which is specific to the universality class of the 2D Ising model. More precisely, for any collection of points$x _ { 1 } = ( k _ { 1 } , 0 ) , \ldots , x _ { 2 n } =$ $( k _ { 2 n } , 0 )$satisfying$k _ { 1 } < k _ { 2 } < \cdots < k _ { 2 n }$on the boundary of the upper half-plane H$: = \mathbb { Z } \times \mathbb { Z } _ { + }$

$$
\langle \sigma_ {x _ {1}} \dots \sigma_ {x _ {2 n}} \rangle_ {\mathbb {H}, \beta_ {c}} = \operatorname{Pfaff} _ {n} \left(\left[ \langle \sigma_ {x _ {i}} \sigma_ {x _ {j}} \rangle_ {\mathbb {H}, \beta_ {c}} \right] _ {1 \leq i <   j \leq 2 n}\right) [ 1 + o (1) ],\tag{8.7}
$$

where$o ( 1 )$is a function of the points$x _ { 1 } , \ldots , x _ { 2 n }$which tends to zero for configuration sequences with min$\{ | x _ { i } - x _ { j } | : 1 \le i < j \le 2 n \}$tending to infinity.

This is, to the author’s knowledge, the first property witnessing the 2D Ising universality class that can be obtained in a level of generality that is not restricted to planar graphs and their perturbations. Also, the proof relies on the key properties of the Ising model that one would like to use: the ± spin symmetry (entering the story through the use of the random current representation) and the large scale planarity of the underlying graph (which for finite range models on${ \mathbb { Z } } ^ { 2 }$is the reason behind the “almost” intersection properties of long paths). The trade-of is that full conformal invariance of this family of models is still out of reach.

## 8.4. Conformal bootstrap in 3D Ising model

At this point, we already mentioned that the 1D Ising model was trivially solved in the original paper of Ising [70], and that it took 20 more years to achieve a solution of the 2D Ising model [87]. We also saw that the model in dimensions 4 and higher is much simpler as its large-scale properties should be Gaussian. This singles out 3D as the remaining challenging dimension. To the best of our knowledge, it is not known whether the model is integrable or not. This is particularly problematic as the third dimension is probably the most relevant one physically (for instance the model should be in the universality class of liquid–vapour systems, and totally anisotropic magnets).

In recent years, a striking progress has been made on the physics side using the so-called conformal bootstrap. A conformal field theory (CFT) is characterised by the correlation functions ⟨−−⟩ of an infinite number of local operators${ \mathcal { A } } ( x )$, which in the case of Ising should be understood as the objects obtained by taking the limit of random variables defined in terms of spins next to a given position of space. For example, the scaling limit of spin and energy observables$\sigma _ { x }$and$\varepsilon _ { \{ x , y \} } = \sigma _ { x } \sigma _ { y } - \langle \sigma _ { x } \sigma _ { y } \rangle$give such local operators in the case of Ising, but one may think of more complicated ones, such as the scaling limit of (products of) the gradient$\sigma _ { x + y } - \sigma _ { x }$of the spins.

Conformal invariance already forces huge constraints on the correlations of operators in the theory. Oversimplifying slightly, for scalar local operators there must exist expo nents$\Delta \mathcal { A }$and coeficients$f _ { \mathcal { R B C } }$such that

$$
\langle \mathcal {A} (x) \mathcal {A} (y) \rangle = \frac {1}{\| x - y \| _ {2} ^ {\boldsymbol {\Delta} _ {\mathcal {A}}}},\tag{8.8}
$$

$$
\langle \mathcal {A} (x) \mathcal {B} (y) \mathcal {C} (z) \rangle = \frac {f _ {\mathcal {A B C}}}{\| x - y \| _ {2} ^ {\boldsymbol {\Delta} _ {\mathcal {A}} + \boldsymbol {\Delta} _ {\mathcal {B}} - \boldsymbol {\Delta} _ {C}} \| y - z \| _ {2} ^ {\boldsymbol {\Delta} _ {\mathcal {B}} + \boldsymbol {\Delta} _ {C} - \boldsymbol {\Delta} _ {\mathcal {A}}} \| z - x \| _ {2} ^ {\boldsymbol {\Delta} _ {C} + \boldsymbol {\Delta} _ {\mathcal {A}} - \boldsymbol {\Delta} _ {\mathcal {B}}}}\tag{8.9}
$$

(in (8.8), we adopted without loss ofgenerality the normalization of A that makes the constant in the numerator equal to 1). The exponents and coeficients depend a priori on the CFT, but a striking feature is that there exists a way, called the conformal block decomposition, to express multi-point correlations of local operators in terms of three-point functions by gluing points together using the so-called operator product expansion. This theoretically shows that all the information in a CFT can be encoded in terms of the$\Delta \mathcal { A }$and the$f _ { \mathcal { R B C } }$. Of course, determining these coeficients is very dificult.

While in 2D this was done in the eighties, the analogous question remains widely open in 3D. Nevertheless, one can proceed in a slightly diferent way by asking which choices of these quantities can lead to a consistent CFT. This approach, called the conformal bootstrap, was shown to be amazingly powerful in 3D. The underlying idea is that one is facing an infinite family of consistency relations coming from diferent ways of applying the conformal block decomposition (which is not unique). For instance, one may start with $\langle \mathcal { A } ( x _ { 1 } ) \mathcal { A } ( x _ { 2 } ) \mathcal { A } ( x _ { 3 } ) \mathcal { A } ( x _ { 4 } ) \rangle$and proceed by gluing first$x _ { 1 }$and$x _ { 2 }$or, on the contrary,$x _ { 3 }$and � . This leads to two decompositions of the same object as a linear combination (with positive coeficients in the Ising case) of known objects called the conformal blocks. Equalling these two decompositions, one ends up with constraints on the possible exponents.

There is a priori no reason to be able to determine the critical exponents as the unique values satisfying a (finite) number of constraints thus obtained. Indeed, the set of possible values may not shrink when considering more and more conditions, but it happens that in the case of the Ising model, the region of the plane for possible critical exponents$( \Delta _ { \sigma } , \Delta _ { \varepsilon } )$for the spin and energy local operators can be reduced drastically, to a point where estimates – namely$\left( \Delta _ { \sigma } , \Delta _ { \varepsilon } \right) = \left( 0 . 5 1 8 1 4 8 9 ( 1 0 ) , 1 . 4 1 2 6 2 5 ( 1 0 ) \right)$– using this bootstrap technique become way better than Monte-Carlo simulations. We refer to [41,78,93] for some of the original papers and [97] for a review ofthe most recent progress in this very exciting area ofmodern theoretical physics.

Let us conclude that even if one may use conformal bootstrap to exactly identify the critical exponents, this would leave the question of proving that the critical 3D Ising model indeed converges to a CFT widely open. In some sense, getting suficient information on the possible scaling limits and proving that these scaling limits indeed exist are two almost entirely disjoint questions even though, of course, one may hope that information on the former question would help answer the latter.

## 9. A tail to this story

The Ising model has always played the role of a locomotive in the developments of statistical physics. Its central place and incredible properties turn it into an amazing playground for both mathematicians and physicists. As a consequence, during most of its history novel techniques were developed to solve problems on it, which later led to whole independent fields of mathematical physics (integrable systems, graphical representations, rigorous renormalisation methods, etc).

Let us mention several long-standing problems remaining widely open for this model. At the top of the list, universality of the 2D behaviour (see Section 8.3), critical properties of the 3D model (see Section 8.4), and the roughening phase transition (see Section 5.3) are among the most important unsolved puzzles. Solving them will probably require the development of new techniques that will again, through cross-fertilisation, benefit the whole field of statistical mechanics.

## Acknowledgments

We thank all our coauthors for the wonderful years of joint research, both past and future. We also wish to thank D. Cimasoni, T. Gunaratnam, D. Krachun, I. Manolescu, R. Panis, V. Tassion, and Y. Velenik who, without knowing its ultimate aim, took the time to take a look at this review and to give the author feedback.

## Funding

This work has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreements No. 757296). The author acknowledges funding from the NCCR SwissMap, the Swiss FNS, and the Simons collaboration on localization of waves.

## References

[1]M. Aizenman. Translation invariance and instability of phase coexistence in the two dimensional Ising system. Commun. Math. Phys. 73 (1980), no. 1, 83–94.

[2]M. Aizenman. Geometric analysis of$\varphi ^ { 4 }$fields and Ising models. I, II, Commun. Math. Phys. 86 (1982), no. 1, 1–48.

[3]M. Aizenman, D.J. Barsky, and R. Fernández. The phase transition in a genera class of Ising-type models is sharp, J. Statist. Phys. 47 (1987), no. 3–4, 343–374.

[4]M. Aizenman and H. Duminil-Copin. Marginal triviality of the scaling limits of critical 4D Ising and$\phi _ { 4 } ^ { 4 }$models. Ann. Math. 194 (2021), no. 1, 163–235.

[5]M. Aizenman, H. Duminil-Copin, and V. Sidoravicius. Random Currents and Continuity of Ising Model’s Spontaneous Magnetization, Commun. Math. Phys 334 (2015), 719–742.

[6]M. Aizenman, H. Duminil-Copin, V. Tassion, and S. Warzel. Emergent planarity in two-dimensional Ising models with finite-range interactions. Invent. Math. 216 (2019), no. 3, 661–743.

[7]M. Aizenman and R. Fernández. On the critical behavior of the magnetization in high-dimensional Ising models, J. Statist. Phys. 44 (1986), no. 3–4, 393–454.

[8]J.R. Baker and A. George. Application of the Padé approximant method to the investigation of some magnetic properties of the Ising model. Phys. Rev. 124 (1961), no. 3, 768.

[9]R.J. Baxter. Exactly solved models in statistical mechanics. Academic Press Inc. London, 1989. Reprint of the 1982 original.

[10] R.J. Baxter and I.G. Enting. 399th solution of the Ising model. J. ofPhys. A: Math. and Gen. 11 (1978), no. 12, 2463.

[11] R. Bauerschmidt, D.C. Brydges, and G. Slade. Scaling limits and critical behaviour of the 4-dimensional �-component$| \phi ^ { 4 } |$spin model. J. Stat. Phys. 157 (2014), 692–742.

[12] A.A. Belavin, A.M. Polyakov, and A.B. Zamolodchikov. Infinite conformal symmetry in two-dimensional quantum field theory. Nuclear Physics B 241 (1984), no. 2, 333–380.

[13] S. Benoist, H. Duminil-Copin, and C. Hongler. Conformal invariance of crossing probabilities for the Ising model with free boundary conditions. Ann. de l’IHP 52 (2016), no. 4, 1784–1798.

[14] S. Benoist and C. Hongler. The scaling limit of critical Ising interfaces is CLE(3). Ann. Probab. 47 (2019), no. 4, 2049–2086.

[15] T. Bodineau, D. Iofe, and Y. Velenik. Rigorous probabilistic analysis of equilibrium crystal shapes. J. Math. Phys. 41 (2000), no. 3, 1033–1098.

[16] M. Biskup. Reflection positivity and phase transitions in lattice spin models. In Methods ofcontemporary mathematical statistical physics, volume 1970 of Lecture Notes in Math., pages 1–86. Springer, Berlin, 2009.

[17] T. Bodineau. The Wulf construction in three and more dimensions. Commun. Math. Phys. 207 (1999), no. 1, 197–229.

[18] T. Bodineau. Translation invariant Gibbs states for the Ising model. Prob. Th. Rel. Fields 135 (2006), no. 2, 153–168.

[19]W. Bragg and E. Williams. The efect of thermal agitation on atomic arrangemen in alloys. (–II) Proc. ofthe Royal Soc. ofLondon. 145 (1934), no. 855, 699–730 – 151 (1935), no. 874, 540–566.

[20] S.G. Brush. History of the Lenz-Ising model. Rev. Mod. Phys. 39 (1967), no. 4, 883.

[21] D. Brydges, J. Fröhlich, and T. Spencer. The random walk representation of classical spin systems and correlation inequalities. Commun. Math. Phys. 83 (1982), no. 1, 123–150.

[22] F. Camia, C. Garban, and C.M. Newman. Planar Ising magnetization field I. Uniqueness of the critical scaling limit. Ann. Probab. 43 (2015), no. 2, 528–571.

[23] M. Campanino, D. Iofe, and Y. Velenik. Ornstein-Zernike theory for finite range Ising models above � . Prob. Th. Rel. Fields 125 (2003), no. 3, 305–349.

[24] R. Cerf and A. Pisztora. On the Wulf crystal in the Ising model. Ann. Probab. 28 (2000), 947–1017.

[25] D. Chelkak. Ising model and s-embeddings of planar graphs. arXiv:2006.14559 (2020).

[26] D. Chelkak, D. Cimasoni, and A. Kassel. Revisiting the combinatorics of the 2D Ising model. Ann. IHP D 4 (2017), no. 3, 309–385.

[27] D. Chelkak, C. Hongler, and K. Izyurov. Conformal invariance of spin correla tions in the planar Ising model. Ann. ofMath. (2) 181 (2015), no. 3, 1087–1138.

[28] D. Chelkak, and S. Smirnov. Universality in the 2D Ising model and conforma invariance of fermionic observables. Invent. Math. 189 (2012), no. 3, 515–580.

[29] D. Cimasoni. The Critical Ising Model via Kac-Ward Matrices. Commun. Math. Phys. 316 (2012), 99–126.

[30] P. Curie. Propriétés magnétiques des corps à diverses températures. 4, Gauthier-Villars etfils.

[31] R.L. Dobrushin. Gibbs state describing coexistence of phases for a three-dimensional Ising model. Th. Probab. & Its Appl. 17 (1973), no. 4, 582–600.

[32] R.L. Dobrushin, R. Kotecký, and S. Shlosman. Wulfconstruction: a global shape from local interaction. Providence: American Math. Society. 104 (1992), x+204.

[33]N.P. Dolbilin, ,Y.M. Zinov’ev, A.S. Mishchenko, M.A. Shtan’ko, and M.I. Shtogrin. The two-dimensional Ising model and the Kac-Ward determinant. Izvestiya: Math 63 (1999), no. 4, 707.

[34] C. Domb and M.F. Sykes. On the susceptibility of a ferromagnetic above the Curie point. Proc. Royal Soc. London. Series A. Mathematical and Physical Sciences 240 (1957), no. 1221, 214–228.

[35]H. Duminil-Copin. Random currents expansion of the Ising model. arXiv:1607.06933 (2016).

[36] H. Duminil-Copin, S. Goswami, and A. Raoufi. Exponential decay of truncated correlations for the Ising model in any dimension for all but the critical tempera ture. Commun. Math. Phys. 374 (2020), no. 2, 891–921.

[37] H. Duminil-Copin, C. Hongler, and P. Nolin. Connection probabilities and RSW-type bounds for the two-dimensional FK Ising model. Comm. Pure Appl. Math. 64 (2011), no. 9, 1165–1198.

[38] H. Duminil-Copin and I. Manolescu. Planar random-cluster model: scaling relations. arXiv:2011.15090 (2020).

[39] H. Duminil-Copin and V. Tassion. A new proof of the sharpness of the phase transition for Bernoulli percolation and the Ising model. Commun. Math. Phys. 343 (2016), no. 2, 725–745.

[40] R.G. Edwards, and A.D. Sokal. Generalization of the Fortuin-Kasteleyn-Swendsen-Wang representation and monte carlo algorithm. Phys. Rev. D 38 (1988), no. 6, 2009.

[41]S. El-Showk, M.F. Paulos, D. Poland, V.S. Rychkov, D. Simmons-Dufin, and A. Vichi. Solving the 3D Ising model with the conformal bootstrap. Phys. Rev D 86 (2012), no. 2, 025022.

[42] J.W. Essam and M.E. Fisher. Padé approximant studies of the lattice gas and Ising ferromagnet below the critical point. J. Chem. Phys. 38 (1963), no. 4, 802–812.

[43] J. Feldman, J. Magnen, V. Rivasseau, and R. Sénéor. Construction and Bore Summability of Infrared$\Phi _ { 4 } ^ { 4 }$by a Phase Space Expansion. Commun. Math. Phys. 109 (1987), 437–480.

[44] J.S. Feldman and K. Osterwalder. The Wightman axioms and the mass gap for weakly coupled$\phi _ { 3 } ^ { 4 }$quantum field theories. Ann. Phys. 97 (1976), no. 1, 80–135.

[45]M.E. Fisher. Correlation functions and the critical region of simple fluids. J Math. Phys. 5 (1964), no. 7, 944–962.

[46]M.E. Fisher. On the dimer solution of planar Ising models. J. Math. Phys. 7 (1963) 1776.

[47] C.M. Fortuin and P.W. Kasteleyn. On the random-cluster model. I. Introduction and relation to other models. Physica 57 (1972), 536–564.

[48] S. Friedli and Y. Velenik. Statistical mechanics of lattice systems: a concrete mathematical introduction. Cambridge University Press (2017).

[49] J. Fröhlich. On the triviality of$\lambda \phi _ { d } ^ { 4 }$theories and the approach to the critical point in$d ( - ) > 4$dimensions. Nuclear Physics B 200 (1982), no. 2, 281–296.

[50] J. Fröhlich, B. Simon, and T. Spencer. Infrared bounds, phase transitions and continuous symmetry breaking. Commun. Math. Phys. 50 (1976), no. 1, 79–95.

[51] K. Gawedzki and A. Kupiainen. Massless Lattice$\Phi _ { 4 } ^ { 4 }$Theory: Rigorous Control o a Renormalizable Asymptotically Free Model, Commun. Math. Phys. 99 (1985), 197–252.

[52] H.O. Georgii. Gibbs measures and phase transitions, volume 9 of de Gruyter Studies in Mathematics. Walter de Gruyter and Co., Berlin, second edition, 2011.

[53] A. Giuliani, R.L. Greenblatt, and V. Mastropietro. The scaling limit of the energy correlations in non-integrable Ising models. J. Math. Phys. 53 (2012), no. 9, 095214.

[54] J. Glimm and A. Jafe. Positivity of the$\phi _ { 3 } ^ { 4 }$hamiltonian. Fortschritte der Physik. 21 (1973), no. 7, 327–376.

[55] J. Glimm and A. Jafe. Quantum physics: afunctional integral point ofview. Springer Science & Business Media (2012).

[56] L. Greenberg and D. Iofe. On an invariance principle for phase separation lines. Ann. l’IHP (B) Probab. Stat. 41 (2005), no. 5, 871–885.

[57] R.B. Grifiths. Correlation in Ising ferromagnets I, II. J. Math. Phys. 8 (1967), 478–489.

[58] R.B. Grifiths. Dependence of critical indices on a parameter. Phys. Rev. Letters 24 (1970), no. 26, 1479.

[59] R.B. Grifiths, C.A. Hurst, and S. Sherman. Concavity of magnetization of an Ising ferromagnet in a positive external field. J. Math. Phys. 11 (1970), 790–795.

[60] R.B. Grifiths and B. Simon, The$( \Phi _ { 2 } ) ^ { 4 }$Field Theory as a Classical Ising Model, Commun. Math. Phys. 33 (1973), 145–164.

[61] F. Guerra, L. Rosen and B. Simon, The$P ( \phi ) ^ { 2 }$Euclidean Quantum Field Theory as Classical Statistical Mechanics, Ann. ofMath. 101 (1975), 111–189.

[62] T. Hara and H. Tasaki. A Rigorous Control of Logarithmic Corrections in Four-Dimensional$( \phi _ { 4 } ) ^ { 4 }$Spin Systems. II. Critical Behaviour of Susceptibility and Correlation Length, J. Stat. Phys. 47 (1987), no. 1/2, 99–121.

[63] W. Heisenberg. Zur Theorie des Ferromagnetismus. Zeitsch.für Physik, 49 (1928), no. 9, 619–636.

[64] Y. Higuchi. On limiting Gibbs states of the two-dimensional Ising models. Publ. Res. Instit. Math. Sciences. 14 (1978), no. 1, 53–69.

[65] C. Hongler. Conformal invariance ofIsing model correlations. PhD thesis, université de Genève, 2010.

[66] C.A. Hurst and H.S. Green. New solution of the Ising problem for a rectangular lattice, J. Chem. Phys. 33 (1960) 1059.

[67] D. Iofe and R.H. Schonmann. Dobrushin-Kotecký-Shlosman theorem up to the critical temperature. Commun. Math. Phys. 199 (1998), no. 1, 117–167.

[68] R.P. Isaacs. A finite diference function theory. Univ. Nac. Tucumán. Revista A., 2 (1941), 177–201.

[69] R.P. Isaacs. Monodifric functions. Construction and applications of conformal maps. Proc. ofa symp. (1941), no. 18, 257–266.

[70] E. Ising. Beitrag zur Theorie des Ferromagnetismus. Zeitsch. Phys., 31 (1925), 253–258.

[71] M. Kac and J.C. Ward. A combinatorial solution of the two-dimensional Ising model, Phys. Rev. 88 (1952), 1332.

[72] L.P. Kadanof. Scaling laws for Ising models near � . Physics Physique Fizika 2 (1966), no. 6, 263.

[73]L.P. Kadanof. Critical behaviour. Universality and scaling. In Critical phenomena Ed. M.S. Green. Proceedings ofthe International School ‘Enrico Fermi’ 51. Italian Physical Society, 100–107. New York: Academic Press.

[74] L.P. Kadanof and H. Ceva. Determination of an operator algebra for the twodimensional Ising model. Phys. Rev. B 3 (1971), no. 11, 3918.

[75] P.W. Kasteleyn. The statistics of dimers on a lattice. Physica 27 (1961) 1209 – Dimer statistics and phase transitions. J. Math. Phys. 4 (1963) 287.

[76] B. Kaufman and L. Onsager. Crystal statistics. III. Short-range order in a binary Ising lattice. Phys. Rev. 76 (1949), no. 8, 1244.

[77]G. Kirchhof. Ueber die Auflösung der Gleichungen, auf welche man bei der Untersuchung der linearen Vertheilung galvanischer Ströme geflührt wird. Ann der Physik. 148 (1847), no. 12, 497–508.

[78] F. Kos, D. Poland, and D. Simmons-Dufin. Bootstrapping mixed correlators in the 3D Ising model. J. High Energy Phys. (2014), 1411, 109.

[79] H.A. Kramers and G.H. Wannier. Statistics of the two-dimensional ferromagnet. Part I. Phys. Rev. 60 (1941), no. 3, 252.

[80] W. Lenz. Beitrag zum Verständnis der magnetischen Eigenschaften in festen Körpern. Phys. Zeitschr. 21 (1920), 613–615.

[81] T.D. Lee and C.N. Yang. Statistical theory of equations of state and phase tran sitions. I. Theory of condensation. II. Lattice gas and Ising model. Phys. Rev. 8 (1952), no. 3, 404, 410.

[82] E.H. Lieb. A refinement of Simon’s correlation inequality. Commun. Math. Phys.. 77 (1980), no. 2, 127–135.

[83] B.M. McCoy and T.T. Wu. The two-dimensional Ising model. Harvard Univ. Press (2013).

[84] S. Miracle-Solé and A. Messager. Correlation functions and boundary conditions in the Ising ferromagnet. J. Stat. Phys. 17 (1977), no. 4, 245–262.

[85] E.W. Montroll. Statistical mechanics of nearest neighbour systems. J. ofChem Phys. 9 (1941), no. 9, 706–721.

[86]M. Niss. History of the Lenz-Ising model 1920–1950: from ferromagnetic to cooperative phenomena. 1950–1965: from irrelevance to relevance. 1965–1971: the role of a simple model in understanding critical phenomena. Archivefor history ofexact sciences. 59 (2005), no. 3, 267-318. 63 (2009), no. 3, 267-318 243-287. 65 (2011), no. 6, 625-658.

[87] L. Onsager. Crystal statistics. I. A two-dimensional model with an order-disorder transition. Phys. Rev.. 65 (1944), no. 3-4, 117.

[88] K. Osterwalder and R. Schrader. Axioms for Euclidean Green’s functions I. II. Comm. Math. Phys. 31 (1973) 83–112. Comm. Math. Phys. 42 (1975) 281–305.

[89] J. Palmer. Planar Ising Correlations. Springer Science & Business Media. 49 (2007).

[90] R. Peierls. On Ising’s model of ferromagnetism. Math. Proc. ofthe Cambridge Phil. Soc. 32 (1936), no. 3, 477–481.

[91] A.M. Polyakov. Conformal symmetry of critical fluctuations. JETP Lett. 12 (1970), 381–383.

[92] A. Raoufi. Translation-invariant Gibbs states of the Ising model: general setting. Ann. ofProbab. 48 (2020), no. 2, 760–777.

[93] R. Rattazzi, V.S. Rychkov, E. Tonni, and A. Vichi. Bounding scalar operator dimensions in 4D CFT. J. High Energy Phys. (2008) 0812, 031.

[94] S. El-Showk, M.F. Paulos, D. Poland, V.S. Rychkov, D. Simmons-Dufin, and A. Vichi. Solving the 3d Ising model with the conformal bootstrap. Phys. Rev. D, 86 (2012), no. 2.

[95]T.D. Schultz, D.C. Mattis, and E.H. Lieb. Two-dimensional Ising model as a sol uble problem of many fermions. Rev. Mod. Phys. 36 (1964), no. 3, 856.

[96] P.D. Seymour and D.J.A. Welsh. Percolation probabilities on the square lattice. Ann. Discrete Math. 3 (1978), 227–245.

[97] D. Simmons-Dufin. The conformal bootstrap. New Frontiers in Fields and Strings: TASI 2015 Proceedings ofthe 2015 Theoretical Advanced Study Institute in Elementary Particle Physics. (2017), 1–74.

[98] B. Simon and R.B. Grifiths. The �<sup>4</sup> field theory as a classical Ising model, Commun. Math. Phys. 33 (1973), no. 2, 145–164.

[99] S. Smirnov. Conformal invariance in random cluster models. I. Holomorphic fermions in the Ising model. Ann. ofMath. (2). 172 (2010), no. 2, 1435–1467.

[100] B.L. van der Waerden. Die lange Reichweite der regelmassigen Atomanordnung in Mischkristallen. Z. Physik 118 (1941), 473–488.

[101] P. Weiss. L’hypothèse du champ moléculaire et la propriété ferromagnétique. J. Phys. Theor. Appl. 6 (1907), no. 1, 661–690.

[102] B. Widom. Equation of state in the neighborhood of the critical point. J. Chem. Phys. 43 (1965), no. 11, 3898–3905.

[103] A.S. Wightman. Quantum Field Theory in Terms ofVacuum Expectation Values. Phys. Rev. 101 (1956), 860.

[104] K.G. Wilson. Renormalization Group and Critical Phenomena. I. Renormalization Group and the Kadanof Scaling Picture, Phys. Rev. B 4 (1971).

[105] C.N. Yang. The spontaneous magnetization of a two-dimensional Ising model. Phys. Rev. 85 (1952), no. 5, 808.

## Hugo Duminil-Copin

Unige, 7-9 rue du Conseil-Général, 1205 Genève, Switzerland, hugo.duminil@unige.ch, IHES, 35 route de Chartres, 91440 Bures-Sur-Yvette, France, duminil@ihes.fr.