## Topology and K-Theory

Lectures by Daniel Quillen

# Lecture Notes in Mathematics

# History of Mathematics Subseries

Volume 2262

Series Editor

Patrick Popescu-Pampu, CNRS, UMR 8524 - Laboratoire Paul Painlevé, Université de Lille, Lille, France

More information about this subseries at http://www.springer.com/series/8909

Robert Penner

# Topology and K-Theory Lectures by Daniel Quillen

With Contribution by Mikhail Kapranov, Kavli Institute for the Physics and Mathematics of the Universe, Kashiwa, Chiba, Japan

Robert Penner

Institut des Hautes Études Scientifiques

Bures-sur-Yvette, France

ISSN 0075-8434

Lecture Notes in Mathematics

ISSN 1617-9692 (electronic)

ISSN 2193-1771

ISSN 2625-7157 (electronic)

History of Mathematics Subseries

ISBN 978-3-030-43995-8

ISBN 978-3-030-43996-5 (eBook)

https://doi.org/10.1007/978-3-030-43996-5

Mathematics Subject Classification (2010): 19-01, 55-01

© Springer Nature Switzerland AG 2020

This work is subject to copyright. All rights are reserved by the Publisher, whether the whole or part of the material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting, reproduction on microfilms or in any other physical way, and transmission or information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed.

The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use.

The publisher, the authors and the editors are safe to assume that the advice and information in this book are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or the editors give a warranty, expressed or implied, with respect to the material contained herein or for any errors or omissions that may have been made. The publisher remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

This Springer imprint is published by the registered company Springer Nature Switzerland AG The registered company address is: Gewerbestrasse 11, 6330 Cham, Switzerland

These are notes from a graduate student course on algebraic topology and K-theory given by Daniel Quillen at the Massachusetts Institute of Technology during 1979–1980. He had just received the Fields Medal for his work on these topics, among others. As a second-semester graduate student myself, it seemed an opportunity to see what all this meant, what a Fields medalist looked and sounded like, what was this exciting new mathematics. Among the gaggle of graduate students, there was also one senior faculty member in attendance, namely Giancarlo Rota.

Dan Quillen was funny and playful with a confident humility from the start. There were points during lectures where he might get stuck and just abandon a proof midstream with a casual never mind, and there was always much joking and laughter, enormous energy. A particularly funny moment about which I have periodically chuckled over the years occurred when he was asked some question or other, thought deeply a long moment and answered with a smile that from a sufficiently enlightened point of view it is obvious.

Giancarlo was also characteristically funny and playful. He early in the semester asked if we could share class notes, especially when he was absent. At that time in my studies, I was able to scrawl every word uttered in class, and given the attention from Giancarlo, I was driven to revise and legibly copy my notes like never before or since. Furiously taking notes in Sweden a few years later, Peter Jones pulled postdoc me aside and explained that gentlemen don't take notes, and I gave up the practice altogether then and there except for an occasional reference or formula.

Giancarlo and I would discuss the lectures which sometimes informed my revisions, and we quickly became friends despite our obviously different circumstances. This was only further cemented a bit less than a decade later when he was a regular Visiting Scholar at the University of Southern California, where I was an assistant professor. We used to joke that we had gone to graduate school together because of the course memorialized here. There were furthermore several occasions from days when I was apparently absent comprising Giancarlo's own notes.

The handwritten notes, mine, ours, and Giancarlo's, are actually in complete sentences with acceptable grammar, and they surfaced recently from a drawer when I moved from my home of thirty years. These are not meant to be polished lecture

notes, rather, I have tried to present things as did Quillen, reflected in the handwritten notes, resisting any temptation to change or add notation, details, or elaborations. Indeed, I have been faithful to Quillen's own exposition, even respecting the board-like presentation of formulae, diagrams, and proofs, omitting numbering theorems in favor of names and so on. This is meant to be Quillen on Quillen as it happened forty years ago, an informal text for a second-semester graduate student. The intellectual pace of the lectures, namely fast and lively, is Quillen himself, and part of the point here is to capture some of this intimacy. I remember especially the last lecture with its abrupt end, a kind of charmingly embarrassed sayonara, having shared so much of himself during the course.

Despite the avowed goal to present these lectures in their native form, a few insignificant and obvious errors have been corrected. Quillen's own writings are sheer perfection, and the same standard cannot be applied here in the informal context of lecture notes where much ground is covered quickly. The reader is warned, therefore, that there may be small inconsistencies remaining though I and we have done our best in this regard and hope that the overall flow and temperament of these notes might compensate whatever errors may remain.

To be sure, much has happened since then from this categorical perspective started by Grothendieck, and I am grateful to my friend Misha Kapranov for contributing an Afterword to this volume in order to make it more useful to current students and also for refining and correcting my own notes. It is likewise a pleasure to thank Cécile Gourgues for her superb transcription from the handwritten notes to beautiful LATEX and the Institut des Hautes Études Scientifiques for supporting this project. Thanks also to Geoff Taylor and Tony Philp for their hospitality in Fiji, where this manuscript was ultimately completed. Let me finally dedicate this little volume to the memories of my friend Gianco and my love Lexy.

Savusavu, Fiji
November 2018

Robert Penner

## Contents

1 Group Extensions and Cohomology 1  
2 Categories and Their Nerves 5  
3 Simplicial Objects 9  
4 Normalization and Conical Contractibility 15  
5 Effaceable $\delta$-Functors 21  
6 (Co)homology of Cyclic Groups 25  
7 An Application to the Schur-Zassenhaus Theorem 33  
8 The Yoneda Lemma 39  
9 Kan Formulae 45  
10 Abelian and Additive Categories 51  
11 Diagram Chasing in Abelian Categories 57  
12 Fibered and Cofibered Categories 61  
13 Examples of Fibered Categories 67  
14 Projective Resolutions 71  
15 Analogues of Homotopy Liftings 75  
16 The Mapping Cylinder and Mapping Cone 83  
17 Derived Categories 89  
18 The First Homotopy Property 95  
19 Group Completions and Grothendieck Groups 101  
20 Devissage and Resolution Theorems 105

21 Exact Sequences of Homotopy Classes ..... 109
22 Spectral Sequences ..... 113
23 Spectral Sequences Continued ..... 119
24 Hyper-Homology Spectral Sequences ..... 125
25 Generalized Kan Formulae ..... 131
26 The Hochschild–Serre Spectral Sequence ..... 137
27 Resolution for Exact Categories ..... 143
28 $K_0 A \cong K_0 A[T]$ ..... 149
29 Classifying Spaces ..... 155
30 Higher K-Groups ..... 159
31 The Category QM ..... 165
32 Homotopy Equivalence ..... 169
33 A Filtration of $Q(\mathcal{P}_A)$ ..... 175
34 Bi-simplicial Sets and Dold-Thom ..... 179
35 Homology of $Q(\mathcal{P}_A)$ and the Tits Complex ..... 185
36 Long Exact Sequences of K-Groups ..... 189
37 Localization ..... 195
38 The Plus Construction, $K_1$ and $K_2$ ..... 201
Afterword by Mikhail Karpranov ..... 207
References ..... 209
Index ..... 211

## Chapter 1 Group Extensions and Cohomology

Consider an extension E of the group G by the group N

$$
* \hookrightarrow N \xrightarrow {i} E \xrightarrow {p} G \longrightarrow *,
$$

so $i:N\hookrightarrow E$ is an injection, $p:E\twoheadrightarrow G$ a surjection and the kernel $\operatorname{Ker}p$ of $p$ equals the image $\operatorname{Im}i$ of $i$, i.e., a short exact sequence. The obvious notion of isomorphisms of extensions is given by a commutative diagram

$$
\begin{array}{c} * \longrightarrow N \longrightarrow E \longrightarrow G \longrightarrow * \\ \text { id } \Big \downarrow \equiv \quad \Big \downarrow \cong \quad \text { id } \Big \downarrow \equiv \\ * \longrightarrow N \longrightarrow E ^ {\prime} \longrightarrow G \longrightarrow * \end{array}
$$

and we let $\mathcal{E}(G, N)$ denote the collection of isomorphism classes.

If $u: G' \to G$ is a homomorphism, then there is a pull back

$$
u ^ {*}: \mathcal {E} (G, N) \to \mathcal {E} (G ^ {\prime}, N)
$$

defined by the diagram

![](images/page_9_image_9.jpg)

where  $E \times_{G} G' = \{(a, b) : a \in E, b \in G' \text{ and } pa = ub\}$  and  $\pi_{1}$  is induced by projection onto the first factor.

The pull back of an epimorphism is again an epimorphism, the pull back preserves fibers, i.e., cosets of N, and we can check directly that the induced map  $N \rightarrow N$  in the diagram is the identity map.

Given an extension  $* \longrightarrow N \stackrel{i}{\rightarrow} E \stackrel{p}{\rightarrow} G \longrightarrow *$  and given  $g \in G$ , choose some  $h \in E$  so that  $p(h) = g$ . Then h acts on E by conjugation and in particular on N since  $N \triangleleft E$ . Thus we have

![](images/page_10_image_2.jpg)

where Aut denotes the automorphism group, Inn $\triangleleft$ Aut the inner automorphism group, and the quotient Out = Aut/Inn is the outer automorphism group. In particular for N abelian, we have Aut N = Out N and get a homomorphism

$$
\begin{array}{l} G \longrightarrow \operatorname{Aut} N \\ g \longmapsto (n \mapsto i ^ {- 1} (h   i (n)   h ^ {- 1})) \end{array}
$$

where  $h \in E$  projects to  $g = p(h)$ .

Thus for $N$ abelian as we assume from now on, $N$ is a $G$-module and

$$
\mathcal {E} (G, N) = \coprod_ {G \xrightarrow {\theta} \operatorname{Aut} N} \mathcal {E} _ {\theta} (G, N),
$$

where  $\mathcal{E}_{\theta}(G,N)$  denotes the extensions compatible with the homomorphism  $\theta:G\to$  Aut N.  $\mathcal{E}_{\theta}(G,N)$  is covariant in the G-module N for G-equivariant maps in the sense that given two G-actions  $\theta$  on N and  $\theta'$  on  $N'$, a G-equivariant  $u:N\to N'$  induces  $\mathcal{E}_{\theta}(G,N)\to\mathcal{E}_{\theta'}(g,N')$, i.e.,

![](images/page_10_image_9.jpg)

where  $E' = N' \times^{N} E = N' \times E$  modulo the action of N, i.e.,  $(n'n, e) \sim (n', ne)$ . Carry on to define multiplication in  $E'$  by

$$
\left(c \ell (n _ {1} ^ {\prime}, e _ {1})\right) \cdot \left(c \ell (n _ {2} ^ {\prime}, e _ {2})\right) \stackrel {{d}} {{=}} \left(c \ell (n _ {1} ^ {\prime} \cdot p (e _ {1}) n _ {2} ^ {\prime}, e _ {1} e _ {2})\right),
$$

where  $c\ell$  means equivalence class, the motivation being

$$
n _ {1} ^ {\prime} e _ {1} n _ {2} ^ {\prime} e _ {2} = n _ {1} ^ {\prime} e _ {1} n _ {2} ^ {\prime} e _ {1} ^ {- 1} e _ {1} e _ {2},
$$

and we check that this is well-defined.

## Description by Means of Cocycles

Given the extension  $* \longrightarrow N \stackrel{i}{\longrightarrow} E \stackrel{p}{\longrightarrow} G \longrightarrow *,$  choose a section  $s : G \to E$  of p, that is, a map of sets so that  $ps = id_{G}$ . Then every element of E can be uniquely written as

$$
i (u) s (g), \quad \text { for } n \in N \text { and } g \in G.
$$

The multiplication is

$$
[ i (n _ {1}) s (g _ {1}) ] [ i (n _ {2}) s (g _ {2}) ] \stackrel {{d}} {{=}} i (n _ {1} + g _ {1} n _ {2}) s (g _ {1}) s (g _ {2}).
$$

The notation is that N is additive, E and G multiplicative, and we denote the action of g on N multiplicatively, so the product can be written

$$
\begin{array}{l} = i (n _ {1} + g _ {1} n _ {2}) i (f (g _ {1}, g _ {2})) s (g _ {1} g _ {2}) \\ = i (n _ {1} + g _ {1} n _ {2} + f (g _ {1}, g _ {2})) s (g _ {1} g _ {2}), \end{array}
$$

where  $f: G \times G \rightarrow N$  depending on the choice of s.

Conclusion the group operation on E is determined by f where

$$
s (g _ {1}) s (g _ {2}) = i (f (g _ {1}, g _ {2})) s (g _ {1} g _ {2}).
$$

Exercise 1.1 Associativity in $E$ implies

$(*_{1})$

$$
g _ {1} f (g _ {2}, g _ {3}) - f (g _ {1} g _ {2}, g _ {3}) + f (g _ {1}, g _ {2} g _ {3}) - f (g _ {1}, g _ {2}) = 0.
$$

Hint:  $(s(g_{1})s(g_{2}))s(g_{3})$  gives the second and fourth terms, and  $s(g_{1})(s(g_{2})s(g_{3}))$  gives the first and third.

Such an  $f: G \times G \rightarrow N$  is called a 2-cocycle of G with values in the G-module N.

Exercise 1.2 Suppose $\tilde{s}: G \to E$ is another section of $p$. Then we get $h: G \to N$ by $\tilde{s}(g) = i(h(g))s(g)$. Show

$(*_{2})$

$$
\tilde {f} \left(g _ {1}, g _ {2}\right) - f \left(g _ {1}, g _ {2}\right) = g _ {1} h \left(g _ {2}\right) - h \left(g _ {1} g _ {2}\right) + h \left(g _ {1}\right).
$$

Hint:  $\tilde{s}(g_{1})\tilde{s}(g_{2})=i h(g_{1})s(g_{2})i h(g_{2})s(g_{2}).$

The right-hand side of  $(*_{2})$  is called the 1-coboundary of h.

Conclusion Can attach to  $* \rightarrow N \rightarrow E \rightarrow G \rightarrow *,$  for N a G-module, a well-defined element of

$H^{2}(G,N)\stackrel {d}{=}$ (group of 2-cocycles with values in $N$ )/(group of 1-coboundaries).

An element of the denominator is a 2-cocycle of the form

$$
(g _ {1}, g _ {2}) \mapsto g _ {1} h (g _ {2}) - h (g _ {1} g _ {2}) + h (g _ {1}).
$$

Theorem In the above way, the isomorphism classes of extensions of $G$ by the $G$-module $N$ are in $1 - 1$ correspondence with elements of $H^2(G, N)$.

Proof A messy but routine exercise.

□

## General Formulae for the Cochain Complex of $G$ with Values in the $G$-Module $N$

Consider the cochain complex

$$
\dots \longrightarrow 0 \longrightarrow C ^ {0} (G, N) \stackrel {\delta} {\rightarrow} C ^ {1} (G, N) \stackrel {\delta} {\rightarrow} C ^ {2} (G, N) \stackrel {\delta} {\rightarrow} \dots ,
$$

with $C^q(G, N) = \text{Maps}(G^q, N)$, where $G^q$ is the q-fold Cartesian product and $\text{Maps}(X, Y)$ denotes all set maps from $X$ to $Y$ with $C^0(G, N) = N$, and for $f \in C^q$

$$
\begin{array}{l} (\delta f) (g _ {1}, \dots , g _ {q + 1}) \stackrel {{d}} {{=}} g _ {1} f (g _ {2}, \dots , g _ {q + 1}) - f (g _ {1} g _ {2}, g _ {3}, \dots , g _ {q + 1}) \\ \quad + f (g _ {1}, g _ {2} g _ {3}, g _ {4}, \dots , g _ {q + 1}) - \dots \pm f (g _ {1}, \dots , g _ {q}). \end{array}
$$

A routine but messy exercise which we shall explicate later shows that  $\delta^{2}=0$ , and we define

$$
H ^ {q} (G, N) = (\text { Kernel   of } \delta \text { on } C ^ {q}) / (\text { Image   of } C ^ {q - 1} \text { under } \delta).
$$

To compute $H^0$, if $n \in C^0(G, N) \equiv N$, then $(\delta^0 n)(g) = gn - n$, and so

$$
\begin{array}{r l} H ^ {0} (G, N) & = \{n: g n = n \text {   for   all   } g \in G \} \\ & = \text { subgroup   of   elements   of   } N \text {   fixed   by   } G \\ & = N ^ {G}. \end{array}
$$

And by the Theorem, $H^2(G, N)$ is the collection of isomorphism classes of extensions of $G$ by $N$.

# Chapter 2 Categories and Their Nerves

Let us next compute $H^{1}(G, N)$ for $N$ a $G$-module.

$h \in Z^{1}(G, N) = \text{cycles in } C^{1} = \operatorname{Ker}(\delta : C^{1} \to C^{2}) \text{ means}$

$$
h (g _ {1} g _ {2}) = g _ {1} h (g _ {2}) + h (g _ {1}),
$$

and h is called either a derivation or a crossed homomorphism in this case. They can be interpreted as follows:

Let $\theta$ be an automorphism of an extension $E$ of $G$ by $N$, so that

![](images/page_13_image_6.jpg)

Consider $E \to E$ where $e \mapsto \theta(e)e^{-1}$ so $p(\theta(e)e^{-1}) = 1$ while

$$
\begin{array}{r l} \theta (e \cdot i (n)) (e \cdot i (n)) ^ {- 1} & = \theta (e) \theta (i (n)) i (n) ^ {- 1} e ^ {- 1} \\ & = \theta (e) e ^ {- 1}. \end{array}
$$

So this map is constant on cosets of $N$, and there is some $h: G \to N$ so that

$$
\theta (e) e ^ {- 1} = i (h (p e)).
$$

We claim that this h is a derivation.

To see this, take  $g_{1}, g_{2} \in G$ , lift to  $e_{1}, e_{2} \in E$  and compare the two sides of

$$
\begin{array}{r l} \theta (e _ {1} e _ {2}) & = \theta (e _ {1}) \theta (e _ {2}) \\ & = i h (g _ {1}) e _ {1} i h (g _ {2}) e _ {2}. \end{array}
$$

The left-hand side is $i(h(g_1 g_2)) e_1 e_2$, while the right-hand side is

$$
i h (g _ {1}) i (g _ {1} h (g _ {2})) e _ {1} e _ {2} = i (h (g _ {1}) + g _ {1} h (g _ {2})) e _ {1} e _ {2}, \text {   as   desired.   }
$$

Conversely, defining $\theta(e) = i h(pe)e$ gives an automorphism.

Thus $Z^{1}(G, N) = \text{group of automorphisms of any extension of } G \text{ by } N$.

Exercise  $B^{1}(G, N) = \text{coboundaries in } C^{1} = \text{Im}\{\delta : C^{0} \to C^{1}\}$  is the subgroup consisting of all inner automorphisms by elements of N.

Note that for G acting trivially on N, we have  $\delta_{0} \equiv 0$ , and a derivation is just a homomorphism, so  $H^{0}(G, N) = N$ ,  $H^{1}(G, N) = \text{group homomorphisms from } G \text{ to } N \text{ and } H^{2}(G, N) = \text{isomorphism classes of central extensions of } G \text{ by the abelian group } N$ .

## Categories

A category C consists of a class Ob C of objects, and for X,  $Y \in Ob C$  we are given a set  $\operatorname{Hom}_{\mathcal{C}}(X, Y)$  of maps or morphisms, and for X,  $Y, Z \in Ob C$  a composition map

$$
\begin{array}{c} \operatorname{Hom} _ {\mathcal {C}} (X, Y) \times \operatorname{Hom} _ {\mathcal {C}} (Y, Z) \longrightarrow \operatorname{Hom} _ {\mathcal {C}} (X, Z) \\ f \times g \longmapsto g f \end{array}
$$

If $f \in Hom_{\mathcal{C}}(X, Y)$, then we sometimes write simply $f: X \to Y$ and may call $f$ an arrow in $\mathcal{C}$.

Axioms (1) associativity of composition,

(2) existence of identity maps,

(3) the sets $\operatorname{Hom}_{\mathcal{C}}(X, Y)$ are disjoint as $X, Y$ varies in $\operatorname{Ob} \mathcal{C}$.

A small category is a category C so that ObC is a set.

Example 2.1 Given a partially ordered set $(I, \leq)$, called a poset for short, we get a small category $\tilde{I}$ so that $\mathrm{Ob} \tilde{I} = I$ and

$$
\operatorname{Hom} _ {\bar {I}} (X, Y) = \left\{ \begin{array}{l l} \{(x, y) \} (\text { a   1   -   element   set }), & \text { if } x \leq y, \\ \varnothing , & \text { if } (x \leq y) \text { does   not   hold }. \end{array} \right.
$$

Example 2.2 For a monoid M, so the operation is associative and there are identity maps, we get a category  $\widetilde{M}$  with

$$
\mathrm{Ob} \widetilde {M} = \{* \}, \quad \mathrm{Hom} _ {\widetilde {M}} (*, *) = M,
$$

where composition is multiplication in M.

In a category C,  $f : X \rightarrow Y$  is an isomorphism if there is

$$
g: Y \rightarrow X \text {   so   that   } g f = \mathrm{id} _ {X} \text {   and   } f g = \mathrm{id} _ {Y}.
$$

A groupoid is a category in which every morphism is an isomorphism. Note that $\tilde{I}$ is groupoid if and only if all elements are incomparable. Also $m \in \widetilde{M}$ is an isomorphism if $m^{-1}$ exists, and $\widetilde{M}$ is a groupoid if and only if $M$ is a group.

Let $\mathcal{C}$ be a small category. Let $N_0(\mathcal{C})$ be the set of objects and

$$
N _ {1} (\mathcal {C}) = \bigcup_ {X, Y \in \mathrm{Ob} \mathcal {C}} \operatorname{Hom} _ {\mathcal {C}} (X, Y).
$$

We have maps

$$
N _ {1} (\mathcal {C}) \xrightarrow [ \text {   target   } ]{\text {   source   }} N _ {0} (\mathcal {C}).
$$

Let now

$N_{q}(\mathcal{C}) = \text{diagrams in } \mathcal{C} \text{ of composable arrows of length } q$

and call an element of $N_{q}$ (C) a q-simplex. We have maps

$$
N _ {q} (\mathcal {C}) \xrightarrow {d _ {j} , j = 0 , \dots , q} N _ {q - 1} (\mathcal {C})
$$

where

$$
\begin{array}{r l} d _ {j} \left(X _ {0} \leftarrow \dots \xleftarrow {f _ {j}} X _ {j} \xleftarrow {f _ {j + 1}} X _ {j + 1} \dots \leftarrow X _ {q}\right) \\ = \left(X _ {0} \leftarrow \dots \xleftarrow {f _ {j - 1}} X _ {j - 1} \xleftarrow {f _ {j} f _ {j + 1}} X _ {j + 1} \leftarrow \dots X _ {q}\right). \end{array}
$$

We also have maps

$$
N _ {q - 1} (\mathcal {C}) \xrightarrow {s _ {j} , j = 0 , \dots , q - 1} N _ {q} (\mathcal {C})
$$

where

$$
s _ {j} \left(X _ {0} \longleftarrow \dots \longleftarrow X _ {j} \dots \longleftarrow X _ {q - 1}\right) = \left(X _ {0} \longleftarrow \dots \longleftarrow X _ {j} \xleftarrow {\mathrm{id}} X _ {j} \longleftarrow \dots X _ {q}\right).
$$

This so-called simplicial set is the nerve of the category C.

A functor $F:\mathcal{C}_1\to \mathcal{C}_2$ induces a map

$$
N (\mathcal {C} _ {1}) \longrightarrow N (\mathcal {C} _ {2}).
$$

Consider the following posets.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$[q]^{\mathrm{op}} = \{0,1,\dots ,q\}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">C,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\overline{[q]^{op}}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$\widetilde{[q]^{op}}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$[q]^{\mathrm{op}}=\{0,1,\ldots,q\}$  with the wrong order. A functor  $[q]^{\mathrm{op}}\to C$  is the same thing as a q-simplex in C, where  $[q]^{\mathrm{op}}$  is the category of Example 1 derived from the poset  $[q]^{\mathrm{op}}$ .</span></small>

An order preserving map $[p]^{\mathrm{op}} \xrightarrow{\theta} [q]^{\mathrm{op}}$ will induce a map

$$
N _ {q} (\mathcal {C}) \xrightarrow {\theta^ {*}} N _ {p} (\mathcal {C}),
$$

and any $\theta^{*}$ has a canonical presentation

$$
s _ {i _ {1}} \dots s _ {i _ {p}} d _ {j _ {1}} \dots d _ {j _ {k}}
$$

where

$$
i _ {1} > \dots > i _ {p} \text {   and   } j _ {1} <   \dots <   j _ {k}
$$

using the commutation relations.

Let $\Delta$ be the small category with objects $\mathrm{Ob}\, \Delta = \{[p] | p \geq 0\}$, where $[p] = \{0, \ldots, p\}$ with the usual order and $\mathrm{Hom}\, \Delta$ the set of order-preserving maps.

If $\mathcal{C}$ is any category, then a simplicial object in $\mathcal{C}$ is a contravariant functor $X: \mathbb{A} \to \mathcal{C}$. In particular the nerve of a small category $\mathcal{C}$ is such, and the nerve itself is a functor on $\mathbb{A}$.

## Morphisms in $\triangle$

There is a nice system of generators as follows

$$
f a c e s \partial_ {i}: [ p - 1 ] \rightarrow [ p ],
$$

the unique order-preserving injective map with i omitted from the image,

degeneracies $\sigma_{j}$: $[p + 1] \to [p]$, the unique order-preserving surjective map identifying $j$ and $j + 1$.

Now, any injective map $\varepsilon : [p] \to [q]$ has a canonical factorization

$$
\varepsilon = \partial_ {i _ {r}} \dots \partial_ {i _ {1}},
$$

where  $i_{1} < \ldots < i_{r}$  are the elements omitted in the image of  $\varepsilon$ . Likewise any surjective map  $\eta : [p] \to [q]$  has a canonical factorization

$$
\eta = \sigma_ {j _ {1}} \dots \sigma_ {j _ {s}},
$$

where  $j_{1} < \ldots < j_{s}$  are the elements so that  $\eta(j) = \eta(j + 1)$ .

Thus any map $\theta$ in $\triangle$ factors as

$$
\theta = \partial_ {i _ {r}} \dots \partial_ {i _ {1}} \sigma_ {j _ {1}} \dots \sigma_ {j _ {s}}.
$$

Axioms for simplicial objects are (essentially) rules for composition:

$$
a \leq b \quad \text { implies } \quad \partial_ {a} \partial_ {b} = \partial_ {b + 1} \partial_ {a},
$$

$$
a \leq b \quad \text { implies } \quad \sigma_ {b}   \sigma_ {a} = \sigma_ {a}   \sigma_ {b + 1}  ,
$$

$$
\text {   for   all   } a, b, \quad \sigma_ {a}   \partial_ {b} = \left\{ \begin{array}{l l} \text {   id,   } & \text {   if   } a \in \{b, b - 1 \}, \\ \partial_ {b}   \sigma_ {a - 1}, & \text {   if   } a > b, \\ \partial_ {b - 1}   \sigma_ {a}, & \text {   if   } a <   b - 1. \end{array} \right.
$$

Proposition A simplicial object $X:\mathbb{A}\to\mathcal{C}$ in a category $\mathcal{C}$ is a collection

$$
X _ {p} \in \mathrm{Ob} \mathcal {C}, f o r p \geq 0,
$$

together with morphisms

$$
d _ {i}: X _ {p} \longrightarrow X _ {p - 1}, \text {   for   } i = 0, \dots , p,
$$

$$
s _ {i}: X _ {p} \longrightarrow X _ {p + 1}, \text {   for   } i = 0, \dots , p,
$$

so that

$$
\begin{array}{l l} a \leq b & \text { implies } \quad d _ {b}   d _ {a} = d _ {a}   d _ {b + 1}, \\ a \leq b & \text { implies } \quad s _ {a}   s _ {b} = s _ {b + 1}   s _ {a}, \\ & \text { for   all   } a, b, \quad d _ {b}   s _ {a} = \left\{ \begin{array}{l l} i d, & \text { for   } b \in \{a, a + 1 \}, \\ s _ {a - 1} d _ {b}, & \text { for   } a > b, \\ s _ {a}   d _ {b - 1}, & \text { for   } a <   b - 1. \end{array} \right. \end{array}
$$

Given a morphism $\theta : [p] \longrightarrow [q]$, there is an induced $\theta^{*}: X_{p} \longleftarrow X_{q}$, where $\theta^{*}$ is a composition.

$$
\theta^ {*} = \underbrace {s \dots s} _ {\text { indices   go   down }} \underbrace {d \dots d} _ {\text { indices   go   up }}.
$$

## Chains

Let C be a small category and let  $F : C \rightarrow Ab$  be a covariant functor to the category Ab of abelian groups. We shall presently define a simplicial abelian group. A motivating example is described by the diagram

$$
\dots \bigoplus_ {X _ {0} \leftarrow X _ {1} \leftarrow X _ {2}} F (X _ {2}) \Longrightarrow \bigoplus_ {X _ {0} \leftarrow X _ {1}} F (X _ {1}) \Longrightarrow \bigoplus_ {X _ {0}} F (X _ {0}).
$$

Precisely with $\bigsqcup = \oplus$ the direct sum, define

3 Simplicial Objects

$$
C_{p}(\mathcal{C},F)\stackrel {d}{=}\coprod_{\substack{X_{0}\leftarrow \ldots \leftarrow X_{p}\\ \in N_{p}(\mathcal{C})}}F(X_{p}).
$$

Given a monotone $\theta :[p]\to [q]$ , define

$$
\theta^ {*}: \mathcal {C} _ {q} (\mathcal {C}, F) \longrightarrow C _ {p} (\mathcal {C}, F)
$$

as follows. Suppose  $\alpha$  is in the summand belonging to

$$
X _ {0} \longleftarrow \dots \longleftarrow X _ {q}
$$

and let $X_{j}\xrightarrow{\mathrm{in}_{j}}\coprod_{j}[X_{j}$ be the canonical map. Then

$$
\alpha = \mathrm{in} _ {(X _ {0} \leftarrow \dots \leftarrow X _ {q})} \xi , \quad \text { for } \quad \xi \in F (X _ {q}),
$$

and we have

$$
\theta^ {*} (X _ {0} \longleftarrow \dots X _ {\theta (p)} \dots \longleftarrow X _ {q}) = X _ {\theta (0)} \longleftarrow \dots \longleftarrow X _ {\theta (p)}.
$$

Then there is a map $X_{q} \xrightarrow{u} X_{\theta(p)}$ as part of this simplex, and we define

$$
\theta^ {*} \operatorname{in} _ {(X _ {0} \leftarrow \dots \leftarrow X _ {q})} \alpha = \operatorname{in} _ {\theta^ {*} (X _ {0} \leftarrow \dots \leftarrow X _ {q})} F (u) (\alpha).
$$

Exercise If F as above is contravariant, then modify the construction to make sense of

$$
\dots \coprod_ {X _ {0} \leftarrow X _ {1} \leftarrow X _ {2}} F (X _ {0}) \stackrel {{\longrightarrow}} {{=}} \coprod_ {X _ {0} \leftarrow X _ {1}} F (X _ {0}) \stackrel {{\longrightarrow}} {{=}} \coprod_ {X _ {0}} F (X _ {0}).
$$

A co-simplicial object in $\mathcal{C}$ is a covariant functor $\Delta \to \mathcal{C}$.

Co-chains

Suppose $F:\mathcal{C}\to \mathrm{Ab}$ is covariant. Construct

$$
\prod_ {X _ {0}} F (X _ {0}) \stackrel {\partial_ {0}} {\Longrightarrow} \prod_ {X _ {0} \leftarrow X _ {1}} F (X _ {0}) \stackrel {\Longrightarrow} {\Longrightarrow} \prod_ {X _ {0} \leftarrow X _ {1} \leftarrow X _ {2}} F (X _ {0}) \dots
$$

as before, namely

$$
C ^ {p} (\mathcal {C}, F) = \prod_ {X _ {0} \leftarrow \dots \leftarrow X _ {p} \in N _ {p} \mathcal {C}} F (X _ {0}),
$$

and given $\theta : [p] \to [q]$, define $\theta_{*}: C^{p}(\mathcal{C}, F) \to \mathcal{C}^{q}(\mathcal{C}, F)$, for $\alpha \in \prod_{N_{p}\mathcal{C}} F(X_{0})$, as follows

$$
\operatorname{pr} _ {X _ {0} \leftarrow \dots \leftarrow X _ {q}} \theta_ {*} \alpha \longmapsto F (u) \operatorname{pr} _ {\theta^ {*} (X _ {0} \leftarrow \dots \leftarrow X _ {q})} \alpha ,
$$

where  $\Pr_{(X_{0}\leftarrow\cdots\leftarrow X_{q})}$  denotes the canonical map.

$$
(X _ {0} \leftarrow \dots \leftarrow X _ {q})
$$

Let now

$$
\alpha \in \prod_ {X _ {0} \leftarrow \dots \leftarrow X _ {p} \in N _ {p} \mathcal {C}} F (X _ {0}) \in C ^ {p} (\mathcal {C}, F)
$$

and write $\alpha(X_0 \leftarrow \cdots \leftarrow X_p)$ for $\mathrm{pr}_{X_0 \leftarrow \cdots \leftarrow X_p} \alpha$, so given $\partial_j : [p] \to [p + 1]$, we have

$$
(\partial_ {j} \alpha) (X _ {0} \longleftarrow \dots \longleftarrow X _ {p + 1}) = \left\{ \begin{array}{l l} \alpha   (X _ {0} \longleftarrow \dots \widehat {X} _ {j} \longleftarrow \dots \longleftarrow X _ {p + 1})  , & \text { for } j \neq 0, \\ F (u)   \alpha (X _ {1} \longleftarrow \dots \longleftarrow X _ {p + 1})  , & \text { for } j = 0. \end{array} \right.
$$

Suppose now given a simplicial abelian group

$$
\dots C ^ {3} \xrightarrow {\text {   }} C _ {2} \xrightarrow {\text {   }} C _ {1} \xrightarrow {\text {   }} C _ {0},
$$

and define

$$
d = \sum_ {j = 0} ^ {p - 1} (- 1) ^ {j} d _ {j}: C _ {p} \longrightarrow C _ {p - 1}.
$$

Claim $d^2 = 0$.

Proof For $j \geq i$, we have $d_j d_i = d_i d_{j+1}$, and

$$
\begin{aligned} d^{2} & = \sum_{j = 0}^{p - 1}(-1)^{j}d_{j}\sum_{k = 0}^{p}(-1)^{k}d_{k}\\ & = \sum_{\substack{0\leq j\leq p - 1\\ 0\leq k\leq p}}(-1)^{j + k}d_{j}d_{k}\\ & = \sum_{0\leq j <   k\leq p}(-1)^{j + k}d_{j}d_{k} + \underbrace{\sum_{0\leq k\leq j\leq p - 1}(-1)^{j + k}d_{j}d_{k}}_{= \sum_{\substack{0\leq a\leq p - 1\\ a <   b\leq p}}(-1)^{a + b - 1}d_{a}d_{b}}\\ & = 0. \end{aligned}
$$

The homology $H_{*}(C_{p}(C,F),d)$ of $\mathcal{C}$ with values in $F$ is thus defined, and the cohomology $H_{*}(C^{p}(\mathcal{C},F),\delta)$ of $\mathcal{C}$ with values in $F$ is now defined as above, where

## 3 Simplicial Objects

$$
\delta = \sum_ {i = 0} ^ {p + 1} (- 1) ^ {i} \partial_ {i}.
$$

For $\alpha \in \mathcal{C}^p (\mathcal{C},F)$, we have $\alpha (X_0\gets \dots \gets X_p)\in F(X_0)$ and

$$
\begin{array}{l} (\delta \alpha) \left(X _ {0} \xleftarrow [ u ]{\leftarrow} \dots X _ {j} \leftarrow \dots X _ {p + 1}\right) \\ = u _ {*} \alpha (X _ {1} \leftarrow \dots \leftarrow X _ {p + 1}) - \alpha (X _ {0} \leftarrow \widehat {X} _ {1} \leftarrow \dots \leftarrow X _ {p + 1}) \\ + \alpha (X _ {0} \leftarrow X _ {1} \leftarrow \widehat {X} _ {2} \leftarrow \dots \leftarrow X _ {p + 1}) - \dots . \end{array}
$$

Now, if $G$ is a group and $N$ a $G$-module, then interpret $N$ as a functor

$$
\begin{array}{l}\tilde {N}: \tilde {G} \longrightarrow \mathrm{Ab}\\* \underset {g} {\rightarrow} * \longmapsto N \underset {g} {\rightarrow} N,\end{array}
$$

so $C^p (\tilde{G},\tilde{N}) = \prod_{N_p(\tilde{G})}N$ , and an element of $N_{p}(G)$ is

$$
\begin{array}{c} * \xleftarrow {g _ {1}} * \xleftarrow {g _ {2}} \dots \xleftarrow {g _ {p}} *. \\ 0 \end{array}
$$

Therefore $C^p (\tilde{G},\tilde{N}) = \mathrm{Maps}(G^p ,N)$ , as before and

$$
\begin{array}{r l} (\delta \alpha) (g _ {1}, \dots , g _ {p}) & = g _ {1} \alpha (g _ {2}, \dots , g _ {p}) \\ & - \alpha (g _ {1} g _ {2}, g _ {3}, \dots , g _ {p}) \\ & + \dots \end{array}
$$

as before and hence  $H^{p}(\tilde{G},\tilde{N})=H^{p}(G,N)$ .

## Chapter 4 Normalization and Conical Contractibility

Let $I$ be a poset (short for partially ordered set) and take $\widetilde{I}$ as before. $N_{p}(\widetilde{I}) = \{\text{chains of sequences}\}$, i.e., $X_{0}, \ldots, X_{p} \in I$ with $X_{0} \geq \ldots \geq X_{p}$. When the weak equality is actually equality, then we have a degeneracy, and by collapsing we can get a non-degenerate simplex.

Exercise Suppose that $X = \{X_p\}$, a simplicial set. Show any simplex can be uniquely expressed as $x = \eta^* y$ where $\eta$ is a surjective monotone map $\eta : [p] \to [q]$ and $y$ is non-degenerate in the sense it is not in the image of any degeneracy.

Recall the definition of  $H_{*}(\widetilde{I}, F)$  for a functor  $F : \widetilde{I} \to Ab$ .

Take $F$ to be a constant functor $X \mapsto A$ and $f \mapsto \mathrm{id}_A$ for all morphisms $f$. Taking sums in $C_*(\widetilde{I}, F)$ only over non-degenerate simplexes of any poset gives rise to a simplicial complex in the sense of combinatorial topology.

Vertices are elements of I and non-degenerate simplexes are  $X_{0} > \ldots > X_{p}$ .

If $K$ is a simplicial complex, then let $I$ be the poset of simplexes in $K$. Then the simplicial complex associated to $I$ is the barycentric sub-division of $K$.

Note that the usual complex of chains on the simplicial complex belonging to $I$ is the non-degenerate part of $C_{*}(\widetilde{I}, A)$.

Reference Dold-Puppe, Ann. Inst. Fourier (1961).

Normalization Theorem Let $\{C_p\}$ be a simplicial abelian group. Then

$$
\begin{array}{l} C _ {p} = \sum_ {j = 0} ^ {p - 1} \operatorname{Im} \left\{s _ {j}: C _ {p - 1} \longrightarrow C _ {p} \right\} \\ \oplus \bigcap_ {j = 1} ^ {p} \operatorname{Ker} \left\{d _ {j}: C _ {p} \longrightarrow C _ {p - 1} \right\} \end{array}
$$

is a decomposition of the complex  $\cdots\rightarrow C_{p+1}\xrightarrow{d}C_{p}\xrightarrow{d}C_{p-1}\rightarrow\cdots$ . Moreover calling the first summand  $C_{p}^{deg}$ , the degenerate sub-complex,  $\{C_{p}^{deg}\}$  has trivial homology.

Consequence

$$
C _ {*} \longrightarrow C _ {*} / C _ {*} ^ {\mathrm{deg}}
$$

induces a homology isomorphism and in particular

![](images/page_23_image_3.jpg)

Conclusion For a constant functor $A$, $H_{*}(\widetilde{I}, A)$ is the same as the homology of the simplicial complex, and likewise for cohomology.

Example 4.1 [p] as a simplicial complex is $\Delta(p)$ so that

$$
H _ {*} ([ p ], A) = \left\{ \begin{array}{l l} A, * = 0, \\ 0, \text { else }. \end{array} \right.
$$

Example 4.2 The poset described by the Hasse diagram

![](images/page_23_image_8.jpg)

has the "same" simplicial complex so

$$
H _ {*} = \left\{ \begin{array}{l l} A, * = 0, 1, \\ 0, & \text { else }. \end{array} \right.
$$

Exercise Suppose $\{C_p\}$ is the simplicial abelian group

$$
\dots C _ {2} \xrightarrow {\quad} C _ {1} \xrightarrow {\quad} C _ {0}
$$

and suppose there is  $s_{-1}: C_{p} \rightarrow C_{p+1}$ , for all  $p \geq 0$ , so that the usual identities hold. Then

$$
H _ {*} C = 0 \text {   for   } * > 0.
$$

For example, given a simplicial abelian group

$$
A _ {3} \xrightarrow {\longrightarrow} A _ {2} \xrightarrow {\longrightarrow} A _ {1} \xrightarrow {\longrightarrow} A _ {0},
$$

define

$C_p = A_{p+1}$ with $d_j, s_j$ for $C$ given respectively by $d_{j+1}, s_{j+1}$ for $A$.

Then $\{C_p\}$ is a simplicial abelian group and $s_{-1}$ exists as in the exercise, so then $H_* C = 0$.

Why is $H_{1}C = 0$? Well, we have

$$
C _ {2} \xrightarrow {d} C _ {1} \xrightarrow {d} C _ {0}
$$

with

$$
d s _ {- 1} = \left(d _ {0} - d _ {1} + d _ {2}\right) s _ {- 1} = \mathrm{id} - s _ {- 1} d _ {0} + s _ {- 1} d _ {1},
$$

and

$$
s _ {- 1} d = s _ {- 1} (d _ {0} - d _ {1}) = s _ {- 1} d _ {0} - s _ {- 1} d _ {1},
$$

so that

$$
d s _ {- 1} + s _ {- 1} d = \text { id   which   implies } H _ {1} C = 0.
$$

Exercise Generalize this. In general, the extra degeneracy map gives a chain homotopy id  $\simeq 0$ , and C is said to be conically contractible.

Application Suppose that C is a small category and Y a fixed object of C. Take  $F(X) = \coprod_{X \leftarrow Y} A$  for A an object in Ab. Then  $C_{*}(C, F)$  is

$$
\coprod_ {X _ {0} \leftarrow X _ {1} \leftarrow X _ {2}} \coprod_ {X _ {2} \leftarrow Y} A \Longrightarrow \coprod_ {X _ {0} \leftarrow X _ {1}} \coprod_ {X _ {1} \leftarrow Y} A \Longrightarrow \coprod_ {X _ {0} \leftarrow Y} A = C _ {0} (\mathcal {C}, F),
$$

so we have

$$
\coprod_ {X _ {0} \leftarrow X _ {1} \leftarrow X _ {2} \leftarrow Y} A \Longrightarrow \coprod_ {X _ {0} \leftarrow X _ {1} \leftarrow Y} A \xrightarrow [ d _ {1} ]{d _ {0}} \coprod_ {X _ {0} \leftarrow Y} A.
$$

We get an extra degeneracy map, where we have  $s_{p+1}$  here, so acyclic as above since conically contractible.

Note that the direct sum of this construction over all Y gives the construction of the previous exercise. Also note  $C \xrightarrow{\quad} C'$  together with  $H_{*}C' = 0$  implies  $H_{*}C = 0$ .

Cohomology

Consider $C^{*}(\mathcal{C},F)$ with $F$ covariant

$$
\prod_ {X _ {0}} F (X _ {0}) \xrightarrow [ \partial_ {1} ]{\partial_ {0}} \prod_ {X _ {0} \leftarrow X _ {1}} F (X _ {0}) \xlongequal {\quad} \dots
$$

and take for fixed $Y$, $F(X) = \prod_{Y \leftarrow X} A$, the product over all arrows, i.e., over all morphisms. For this $F$, $C^*(\mathcal{C}, F)$ is

$$
\prod_ {Y \leftarrow X _ {0}} A \underset {\sigma_ {1}} {\overset {\sigma_ {0}} {\rightleftharpoons}} \prod_ {Y \leftarrow X _ {0} \leftarrow X _ {1}} A \underset {\longrightarrow} {\rightleftharpoons} \dots ,
$$

and we again have the extra degeneracy

$$
(\sigma_ {- 1} f) (Y \longleftarrow X _ {0} \longleftarrow \dots \longleftarrow X _ {p}) = f (Y \stackrel {\mathrm{id}} {\longleftarrow} Y \longleftarrow \dots \longleftarrow X _ {p}),
$$

so the complex is acyclic.

Thus we have constructed functors for $H_{*}$ and $H^{*}$ which kill homology in that

Theorem For all \* > 0, we have

$$
H _ {*} \left(\mathcal {C}, X \longmapsto \coprod_ {X \leftarrow Y} A\right) = 0,
$$

$$
H ^ {*} \left(\mathcal {C}, X \longmapsto \prod_ {Y \leftarrow X} A\right) = 0.
$$

Example 4.1 Let $\mathcal{C} = \widetilde{G}$ be the category associated to the group $G$. Consider

$$
X \longmapsto \prod_ {Y \leftarrow X} A
$$

i.e., the image is  $\prod_{g\in G}A$ , so this functor is the G-module Maps(G, A), where G acts on the right of G to give a left action on Maps(G, A).

Example 4.2

$$
X \longmapsto \coprod_ {X \leftarrow Y} A = \coprod_ {g} A = \mathbb {Z} [ G ] \otimes_ {\mathbb {Z}} A,
$$

where we multiply on the left in $\mathbb{Z}[G]$ for the module structure.

Corollary

$$
H ^ {*} (G, \operatorname{Maps} (G, A)) = 0 \quad \text { for   all } * > 0,
$$

$$
H _ {*} (G, \mathbb {Z} [ G ] \otimes_ {\mathbb {Z}} A) = 0 \quad \text { for   all } * > 0.
$$

Note that this corollary plus long exact sequences allow us to compute in practice.

Suppose $0 \to M' \to M \to M'' \to 0$ is an exact sequence of $G$-modules. Then we get an exact sequence of complexes of cochains on $G$

$$
0 \longrightarrow C ^ {*} (G, M ^ {\prime}) \longrightarrow C ^ {*} (G, M) \longrightarrow C ^ {*} (G, M ^ {\prime \prime}) \longrightarrow 0
$$

with values in these modules and hence get the usual long exact sequence in cohomology

$$
0 \longrightarrow H ^ {0} (G, M ^ {\prime}) \longrightarrow H ^ {0} (G, M) \longrightarrow H ^ {0} (G, M ^ {\prime \prime}) \stackrel {\delta} {\longrightarrow} H ^ {1} (G, M ^ {\prime}) \longrightarrow \dots
$$

which is natural

$$
\begin{array}{c} 0 \longrightarrow H ^ {0} M ^ {\prime} \longrightarrow H ^ {0} M \longrightarrow H ^ {0} M ^ {\prime \prime} \longrightarrow H ^ {1} M ^ {\prime} \longrightarrow \dots \\ \Bigg \downarrow \quad \Bigg \downarrow \quad \Bigg \downarrow \quad \Bigg \downarrow \\ 0 \longrightarrow H ^ {0} N ^ {\prime} \longrightarrow H ^ {0} N \longrightarrow H ^ {0} N ^ {\prime \prime} \longrightarrow H ^ {1} N ^ {\prime} \longrightarrow \dots \end{array}
$$

with respect to maps of exact sequences in the usual sense. Last time we saw that if  $A \in Ab$ , then the G-module  $\text{Maps}(G, A)$ , that is, set maps, with the action  $(gf)(x) = f(xg)$ , had the property that  $H^{*}(G, \text{Maps}(G, A)) = 0$ , for all  $* > 0$ .

A functor  $T : C \to Ab$  is effaceable if for any object X in C there exists an injection  $X \to Y$  in C so that  $T(Y) = 0$ . Say a cohomology theory itself is effaceable if it is so in positive dimensions.

Proposition $H^{*}(G,\cdot):\text{Mod}_{G}\to\text{Ab}$ is effaceable, for all $*>0$, where $\text{Mod}_{G}$ denotes the category of G-modules.

Proof Consider

$$
M \longrightarrow \operatorname{Maps} _ {\text { set }} (G, M)
$$

$$
m \longmapsto (x \longmapsto x m)
$$

and check this is a G-module map; it is clearly an embedding.

## Example of Free Groups

Let $G$ be the free group on $\{g_i : i \in I\}$. Then a $G$-module is the same thing as an abelian group $M$ with a family of automorphisms indexed by $I$. Recall that $H^0(G, M) = M^G$ and

$H^{2}(G, M) = \text{isomorphism classes of extension of } G \text{ by } M.$

Lift each $g_{i} \in G$ back to $\widetilde{g}_{i} \in E$. Since $G$ is free, we get a section $s$ to $p$

$$
* \longrightarrow M \longrightarrow E \xrightarrow [ s ]{p} G \longrightarrow *,
$$

and $s$ is a group homomorphism. This says the extension splits, and $E$ is the semi-direct product of $G$ acting on $M$.

Note that in general split extensions of G by M correspond to the zero element in  $H^{2}(G, M)$ . The reason is that  $s(g_{1})s(g_{2}) = i(f(g_{1}, g_{2}))s(g_{1}g_{2})$  where f is the two-cocycle belonging to the extension, and f = 0 since s is a group map.

Thus, $H^{2}(G,M) = 0$, for all $M$ if $G$ is free.

Claim $H^{*}(G, M) = 0$, for all $M$ and all $* \geq 2$ if $G$ is free.

Proof Given M, embed M in N where  $H^{*}(G, N) = 0$  for all  $* > 0$  giving

$$
0 \longrightarrow M \longrightarrow N \longrightarrow M _ {1} \longrightarrow 0.
$$

Take the long exact sequence. The proof follows from dimension shift and induction.

Recall that $H^{1}(G, M) = Z^{1}(G, M) / B^{1}(G, M)$ where

$$
\begin{array}{r l} Z ^ {1} (G, M) & = \operatorname{Der} (G, M) \\ & = \text { derivations } G \to M. \end{array}
$$

Claim Der $(G, M) = \text{Maps}(I, M)$.

Proof A derivation is determined by the  $Dg_{i}$ , and these can be assigned arbitrarily. To get  $D(g_{1}^{-1})$ , note that  $D(e)=0$  so  $0=Dg_{1}^{-1}+g_{1}^{-1}Dg_{1}$  so that  $Dg_{1}^{-1}=-g_{1}^{-1}D(g_{1})$ . ☐

The exact sequence for cohomology of free groups gives

$$
m \longmapsto (i \longmapsto g _ {i} m - m)   0 \longrightarrow H ^ {0} (G, M) \longrightarrow M \longrightarrow \underset {\text {Der} (G, M)} {\text {Maps}} (I, M) \longrightarrow H ^ {1} (G, M) \longrightarrow 0.
$$

For instance if $M = \mathbb{Z}$ with trivial $G$-action, then

$$
H ^ {0} (G, \mathbb {Z}) = \mathbb {Z} \text { and } H ^ {1} (G, \mathbb {Z}) \cong \mathbb {Z} ^ {n}
$$

where n is the number of generators of G.

This concludes our discussion for the example of free groups.

Definition A $\delta$-functor on the category of $G$-modules to abelian groups is a collection of so-called additive functors $T^{q}$, for $q \geq 0$, together with, for any sequence $0 \to M' \to M \to M'' \to 0$ of $G$-modules, an assignment of connecting homomorphisms $\delta: T^{q}M'' \to T^{q+1}M'$ so that

(i)  $T^{0}M^{\prime}\rightarrow T^{0}M\rightarrow T^{0}M^{\prime\prime}\stackrel{\delta}{\rightarrow}T^{1}(M^{\prime})\rightarrow\cdots$  is a complex,

(ii) naturality of connecting homomorphisms with respect to maps of exact sequences.

As an exercise, generalize this definition so that the domain of the functor is any abelian category.

In this definition, an additive functor means

$$
\begin{array}{c} \operatorname{Hom} _ {G - \mathrm{mod}} (M, N) \longrightarrow \operatorname{Hom} _ {\mathrm{Ab}} (T ^ {q} M, T ^ {q} N) \\ u \longmapsto T ^ {q} (u) \end{array}
$$

is a homomorphism of abelian groups.

Example 5.1 $N \longmapsto \operatorname{Hom}_{G - \operatorname{mod}}(M, N)$ is additive.

Example 5.2 $N \longmapsto N \otimes_{\mathbb{Z}[G]} M$ is additive.

Example 5.3 $N \longmapsto M \otimes_G N$ is not additive.

Theorem Suppose  $\{T^{q}\}$  and  $\{U^{q}\}$  are  $\delta$ -functors from G-modules to Ab. Assume  $T^{q}$  is effaceable for all q > 0 and  $\{T^{q}\}$  is exact, i.e., (i) in the definition above is in fact exact. Then any natural transformation  $\theta : T^{0} \to U^{0}$  extends uniquely to a natural transformation of  $\delta$ -functors.

We shall prove this theorem in the next Chapter.

Corollary Any two exact effaceable functors that are equal in dimension 0 agree everywhere.

Proof of Corollary Given $M$, find $0 \to M \to N \to M_1 \to 0$ so that $T^*N = 0$ for all $* > 0$. Then

$$
\begin{array}{c} T ^ {0} M \longrightarrow T ^ {0} N \longrightarrow T ^ {0} M ^ {\prime} \xrightarrow {\delta} T ^ {1} M \longrightarrow T ^ {1} / N = 0 \\ \Biggl \downarrow_ {\theta} \qquad \qquad \Biggl \downarrow_ {\theta} \qquad \qquad \Biggl \downarrow_ {\theta} \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text { exists   uniquely } \\ U ^ {0} M \longrightarrow U ^ {0} N \longrightarrow U ^ {0} M ^ {\prime} \xrightarrow {\delta} U ^ {1} M \longrightarrow U ^ {1} N \end{array}
$$

Now induct. It remains as an exercise to check functoriality and independence of choice of N. □

# Chapter 6 (Co)homology of Cyclic Groups

## Homology of Cyclic Groups

Suppose $G = \mathbb{Z} / n\mathbb{Z}$, so $\mathbb{Z}[G] = \mathbb{Z}[T] / (T^n - 1)$, $T$ some indeterminate. This holds since $\operatorname{Hom}_{\operatorname{ring}}(\mathbb{Z}[G], A) = \operatorname{Hom}_{\operatorname{groups}}(G, A^\bullet)$ where $A^\bullet =$ groups of units of $A$ and for $G = \mathbb{Z} / n\mathbb{Z}$

$$
\begin{array}{l} A ^ {\bullet} = \{a \in A: a ^ {n} = 1 \} \\ = \operatorname{Hom} _ {\text { rings }} (\mathbb {Z} [ T ] / (T ^ {n} - 1), A). \end{array}
$$

Now,  $T^{n}-1=(T-1)(T^{n-1}+\ldots+1)$ , so we get two exact sequences of groups and the following identifications:

$$
\begin{array}{c} (* _ {1}) \\ 0 \longrightarrow (T - 1) / (T ^ {n} - 1) \xrightarrow {\text { mult   by } T - 1} \mathbb {Z} [ T ] / (T ^ {n} - 1) \longrightarrow \mathbb {Z} [ T ] / (T - 1) \longrightarrow 0 \\ \Bigg | _ {\mathbb {Z} [ T ] / (T ^ {n - 1} + \dots + 1)} \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \end{array}
$$

where the isomorphism $\mathbb{Z}[T] / (T^{n - 1} + \ldots +1)\to (T - 1) / (T^n -1)$ is given by $1\mapsto T - 1$

$$
\begin{array}{c} 0 \longrightarrow (T ^ {n - 1} + \dots + 1) / (T ^ {n} - 1) \xrightarrow [ (T ^ {n - 1} + \dots + 1) ]{\text { mult   by }} \mathbb {Z} [ T ] / (T ^ {n} - 1) \longrightarrow \mathbb {Z} [ T ] / (T ^ {n - 1} + \dots + 1) \longrightarrow 0 \\ \Bigg | _ {\mathbb {Z} [ T ] / (T - 1)} \\ \Bigg | _ {\mathbb {Z}} \end{array} \tag {*2}
$$

where the isomorphism  $\mathbb{Z}[T]/(T-1)\to(T^{n-1}+\ldots+1)/(T^{n}-1)$  is given by  $1\mapsto(T^{n-1}+\ldots+1)$ . Note that both these sequences split over Z since the terms are free. Note also that  $(*_{2})$  is a “resolution” of the leftmost term in  $(*_{1})$ .
Define

$$
\begin{array}{r l} I (G) & = \mathbb {Z} [ T ] / (T ^ {n - 1} + \dots + 1) \\ & = \text { augmentation   ideal   for } G = \mathbb {Z} / n \mathbb {Z}, \end{array}
$$

$$
\begin{array}{r l} \mathbb {Z} (G) & = \mathbb {Z} [ T ] / (T ^ {n} - 1) \\ & = \mathbb {Z} [ G ] \text {   for   } G = \mathbb {Z} / n \mathbb {Z}, \text {   as   above. } \end{array}
$$

The sequences $(\ast_{1})$ and $(\ast_{2})$ become

$(**_{1})$

$$
0 \longrightarrow I (G) \longrightarrow \mathbb {Z} (G) \longrightarrow \mathbb {Z} \longrightarrow 0,\tag{\((**_{2})\}
$$

$$
0 \longrightarrow \mathbb {Z} \longrightarrow \mathbb {Z} (G) \longrightarrow I (G) \longrightarrow 0.
$$

Now suppose $M$ is a $G$-module, $G = \mathbb{Z}/n\mathbb{Z}$, and tensor $(**_{1})$ and $(**_{2})$ with $M$ to get two exact sequences of $G$-modules

$$
0 \longrightarrow I (G) \otimes_ {\mathbb {Z}} M \xrightarrow {(T - 1) \otimes m \mapsto 1 \otimes m} \mathbb {Z} [ G ] \otimes_ {\mathbb {Z}} M \xrightarrow {1 \otimes m \mapsto m} M \longrightarrow 0 \tag {†1}
$$

$(\dagger_{2})$

$$
0 \longrightarrow M \xrightarrow {m \mapsto \sum_ {i = 0} ^ {n - 1} T ^ {i} \otimes m} \mathbb {Z} [ G ] \otimes_ {\mathbb {Z}} M \xrightarrow {1 \otimes m \mapsto (T - 1) \otimes m} I (G) \otimes_ {\mathbb {Z}} M \longrightarrow 0
$$

where the $G$-action on $M$ is as usual and the $G$-module structure of $A \otimes_{\mathbb{Z}} B$ is $g(a \otimes b) = ga \otimes gb$; check these are $G$-module sequences.

Moreover, if $M$ is a $G$-module, then $\mathbb{Z}[G] \otimes_{\mathbb{Z}} M$ with action $x(g \otimes m) = xg \otimes m$ is isomorphic to $\mathbb{Z}[G] \otimes_{\mathbb{Z}} M$ with action $x(g \otimes m) = xg \otimes xm$, where $g \otimes m \mapsto g \otimes gm$ and $g \otimes g^{-1}m' \leftrightarrow g \otimes m'$. Recall we showed $H_*(G, \mathbb{Z}[G] \otimes_{\mathbb{Z}} A) = 0$, for all $*> 0$. We use this and long exact sequences to compute the homology of cyclic groups. Long exact sequences of $(\dagger_1)$ and $(\dagger_2)$ respectively give

$$
H _ {q} (G, \mathbb {Z} [ G ] \otimes M) \longrightarrow H _ {q} (G, M) \stackrel {\partial} {\longrightarrow} H _ {q - 1} (G, I [ G ] \otimes M) \longrightarrow H _ {q - 1} (G, \mathbb {Z} [ G ] \otimes M)
$$

so the first $\partial$ is an isomorphism for $q \geq 2$, and

$$
H _ {q} (G, \mathbb {Z} [ G ] \otimes M) \longrightarrow H _ {q} (G, I (G) \otimes M) \stackrel {\partial} {\longrightarrow} H _ {q - 1} (G, M) \longrightarrow H _ {q - 1} (G, \mathbb {Z} [ G ] \otimes M)
$$

so the second  $\partial$  is an isomorphism for  $q \geq 2$ .

We thus get canonical isomorphisms

$$
H _ {q} (G, M) \longrightarrow H _ {q - 2} (G, M), \quad \text { for   all } q > 2
$$

and we finally compute  $H_{q}(G, M)$ , for q = 0, 1, 2.

Exercise

$$
\boxed {H _ {0} (G, M) = \mathbb {Z} \bigotimes_ {\mathbb {Z} [ G ]} M = M / \{(g - 1) m \}}
$$

i.e., the largest quotient on which the group acts trivially. Indeed,

$$
\begin{array}{c} C _ {1} (G, M) \xrightarrow {} C _ {0} (G, M) \\ \coprod_ {\stackrel {*} {\leftarrow} ^ {g} \ast} M \xrightarrow {d _ {0}} M \end{array}
$$

and

$$
\begin{array}{l} d _ {0}: g \otimes m \longmapsto m, \\ d _ {1}: g \otimes m \longmapsto g m. \end{array}
$$

Thus,

$$
H _ {0} (G, \mathbb {Z} [ G ] \otimes M) = \mathbb {Z} \bigotimes_ {\mathbb {Z} [ G ]} (\mathbb {Z} [ G ] \otimes_ {\mathbb {Z}} M) = M.
$$

Now, we have

$$
\begin{array}{c} 0 \longrightarrow H _ {1} (G, I \otimes M) \xrightarrow {\partial} H _ {0} (G, M) \longrightarrow H _ {0} (G, \mathbb {Z} [ G ] \otimes M) \longrightarrow H _ {0} (G, I \otimes M) \longrightarrow 0 \\ \left| \begin{array}{l l l} & & \\ M / \{(g - 1) m \} & & \\ & & \\ M / (T - 1) M & \longrightarrow & M \\ \hline & & \text { mult   by } \sum_ {i = 0} ^ {n - 1} T ^ {i} \end{array} \right. \end{array}
$$

The map given by multiplication by  $\sum_{i=0}^{n-1}T^{i}$  is called the norm:  $M \rightarrow M$ .

Thus $H_0(G, I \otimes M) = M / \operatorname{Im}\{\text{norm}: M \to M\}$ and

$$
H _ {1} (G, I \otimes M) = \frac {\operatorname{Ker} \{\text { norm }: M \to M \}}{\operatorname{Im} \{(T - 1) : M \to M \}}.
$$

Since $H_{2}(G,M) = H_{1}(G,I\otimes M)$ , we get

$$
\boxed {H _ {2} (G, M) = \frac {\operatorname{Ker} \{\text { norm }: M \rightarrow M \}}{\operatorname{Im} \{(T - 1) : M \rightarrow M \}}}
$$

Exercise

$$
\boxed {H _ {1} (G, M) = \frac {\operatorname{Ker} \{(T - 1) : M \rightarrow M \}}{\operatorname{Im} \{\text { norm } : M \rightarrow M \}}}
$$

Cohomology of Cyclic Groups

Recall $H^{*}(G, \text{Maps } (G, A)) = 0$, for all $* > 0$, and for $G$ finite abelian

$$
\operatorname{Maps} (G, M) = \operatorname{Hom} _ {\mathbb {Z}} (\mathbb {Z} [ G ], M) = \operatorname{Hom} _ {\mathbb {Z}} (\mathbb {Z} [ G ], \mathbb {Z}) \otimes_ {\mathbb {Z}} M.
$$

Thus, from $(**_{1})$ and $(**_{2})$, which we recall are split, we get two exact sequences

$$
0 \longrightarrow \operatorname{Hom} _ {\mathbb {Z}} (\mathbb {Z}, M) \longrightarrow \operatorname{Hom} _ {\mathbb {Z}} (\mathbb {Z} [ G ], M) \longrightarrow \operatorname{Hom} _ {\mathbb {Z}} (I, M) \longrightarrow 0
$$

$$
0 \longrightarrow \operatorname{Hom} _ {\mathbb {Z}} (I, M) \longrightarrow \operatorname{Hom} _ {\mathbb {Z}} (\mathbb {Z} [ G ], M) \longrightarrow \operatorname{Hom} _ {\mathbb {Z}} (\mathbb {Z}, M) \longrightarrow 0
$$

and as above $\mathrm{Hom}_{\mathbb{Z}}(\mathbb{Z}[G], M)$ has trivial higher cohomology.

Exercise (if interested)

$$
H ^ {q} (G, M) \stackrel {\cong} {\longrightarrow} H ^ {q + 2} (G, M), \quad \text { for } q \geq 1,
$$

$$
H ^ {2} (G, M) = \frac {\operatorname{Ker} \{(T - 1) : M \rightarrow M \}}{\operatorname{Im} \{\text { norm } : M \rightarrow M \}},
$$

$$
H ^ {1} (G, M) = \frac {\operatorname{Ker} \{\text { norm } : M \to M \}}{\operatorname{Im} \{(T - 1) : M \to M \}},
$$

and we know $H^0 (G,M) = M^G$, as before, completing this discussion of cyclic groups.

Recall the

Theorem Suppose  $\{T^{q}, q \geq 0\}$  is an exact  $\delta$ -functor and  $T^{q}$  is effaceable for all q > 0 and  $\{U^{q}, q \geq 0\}$  is any  $\delta$ -functor. Then any natural transformation  $\theta^{0}: T^{0} \to U^{0}$  extends uniquely to a natural transformation of  $\delta$ -functors.

Proof It suffices to extend to q = 1 and check properties by induction.

1: Uniqueness: Suppose given M and find exact

$$
0 \longrightarrow M \longrightarrow M ^ {\prime} \longrightarrow M ^ {\prime \prime} \longrightarrow 0 \text {so that} T ^ {1} M ^ {\prime} = 0.
$$

Then we have

$$
\begin{array}{c} T ^ {0} M ^ {\prime} \longrightarrow T ^ {0} M ^ {\prime \prime} \xrightarrow {\delta} T ^ {1} M \longrightarrow T ^ {1} M ^ {\prime} = 0 \\ \Biggl \downarrow_ {\theta^ {0}} \qquad \qquad \qquad \Biggl \downarrow_ {\theta^ {0}} \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ U ^ {0} M ^ {\prime} \longrightarrow U ^ {0} M ^ {\prime \prime} \xrightarrow {\delta} U ^ {1} M \end{array}
$$

with the top row exact. A diagram chase gives uniqueness of $\theta^1$.

Defining $\theta^1$ as before in the obvious way, we must check:

Claim 6.2 Well-defined.

Claim 6.3 Natural transformation.

Claim 6.4 Compatible with $\delta$.

Check 6.2 We have the

Claim Given $M \hookrightarrow M'$ and $M \hookrightarrow M_1'$ with $T^1 M' = T^1 M_1' = 0$, then we can embed these maps in a diagram

![](images/page_35_image_15.jpg)

with  $T^{1}M_{2}^{\prime}=0$ .

Proof Take the push out, i.e., take $\widehat{M}_{2}^{\prime}=M^{\prime}\oplus M_{1}^{\prime}/(\operatorname{Im}M\oplus-\operatorname{Im}M)$ and embed it $\widehat{M}_{2}^{\prime}\hookrightarrow M_{2}^{\prime}$ by effaceability. $\square$

Thus to show $\theta^1: T^1M \to U^1M$ is the same for $M \hookrightarrow M'$ and $M \hookrightarrow M'_1$, we may assume

![](images/page_36_image_1.jpg)

commutes. Thus we have

![](images/page_36_image_3.jpg)

which gives the following cube of arrows

![](images/page_36_image_5.jpg)

and this all commutes by definition except perhaps the rightmost face, which thus also commutes, as desired.

Check 6.3 Suppose we have

![](images/page_36_image_8.jpg)

We get the same cube as above with identity maps replaced by  $u_{*}$  and all appearances of M in parentheses having subscript “1”.

Check 6.4 We must check that an exact

$$
0 \longrightarrow M \longrightarrow N \longrightarrow Q \longrightarrow 0
$$

gives a commutative

![](images/page_37_image_1.jpg)

To this end we resolve

![](images/page_37_image_3.jpg)

so that  $T^{1}M' = 0$ .

Exercise Finish the argument.

# Chapter 7 An Application to the Schur–Zassenhaus Theorem

We have the

Theorem Given $\{T^{q}\}$ an exact $\delta$-functor with $T^{q}$ effaceable, for $q > 0$, and $\{U^{q}\}$ any $\delta$-functor. Then any natural transformation $\theta^{0}: T^{0} \to U^{0}$ extends uniquely to a natural transformation of $\delta$-functors.

Example 7.1 Suppose $f: H \to G$ is a group homomorphism. Then any $G$-module $M$ is also an $H$-module, denoted $f^{*}M$. We define two $\delta$-functors

$$
T ^ {q} (M) = H ^ {q} (G, M)
$$

$U^{q}(M) = H^{q}(H,M)$ with $M$ regarded as $f^{*}M$.

from the category of $G$-modules to the category of abelian groups. Automatically a short exact sequence of $G$-modules is a short exact sequence of $H$-modules. Then

$H^{0}(G,M)\subset H^{0}(H,M)$ is a natural transformation of $\delta$-functors. By the theorem, there exists a unique morphism of $\delta$-functors

$$
\operatorname{Res} _ {f: H \to G}: H ^ {q} (G, M) \longrightarrow H ^ {q} (H, M)
$$

extending from G to H.

Formulae Given $K \xrightarrow{u} H \xrightarrow{f} G$, we have

$$
\operatorname{Res} _ {K \rightarrow M} \operatorname{Res} _ {H \rightarrow G} = \operatorname{Res} _ {K \rightarrow G}
$$

by the uniqueness assertion, since it is true in degree 0. We could define the restriction on the cochain level, and this must agree, again by uniqueness.

Example 7.2 Transfer Map Let H < G be a subgroup of finite index and let M be a G-module. We have the transfer

$$
H^{0}_{\substack{\parallel \\ M^{H}}} (H,M)\longrightarrow H^{0}_{\substack{\parallel \\ M^{G}}}(G,M)  ,
$$

defined as follows. If  $m \in M^{H}$  and  $g \in G$ , then gm depends only on the coset gH of g, where  $(gh)m = g(hm) = gm$ . Thus if  $g_{1}, \ldots, g_{n}$  are coset representatives, so  $G = \coprod_{i=1}^{n} g_{i} H$ , then the element

$$
\sum_ {i = 1} ^ {n} g _ {i} m
$$

is independent of the choice of coset representatives. Write it as $\sum_{gH\in G / H}(gH)m$. This element is invariant under all $g\in G$. In this way we get a homomorphism

$$
M ^ {H} \longrightarrow M ^ {G}
$$

called the transfer, denoted variously by

$$
\operatorname{Ver} _ {H \rightarrow G}, \operatorname{Ind} _ {H \rightarrow G}.
$$

Check the hypotheses of the theorem so as to extend to higher dimensions. Exactness is clear, and the only point that remains to be checked is that  $H^{q}(H,\cdot)$  from the category of G-modules is effaceable. As before, we have

$$
M \longrightarrow \operatorname{Maps} (G, M),
$$

and it is enough to show that for any abelian group A that as an H-module

$$
\begin{array}{l} \text { Maps } (G, A) = \prod_ {g H \in G / H} \text { Maps } (g H, A) \\ \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \text {   ||   } \\ \prod_ {g H \in G / H} \text { Maps } (H, A) \end{array}
$$

and Maps $(H, A)$ has trivial $H^{+}(H, \operatorname{Maps}(H, A))$, as proved at the end of Chapter 4. We thus obtain $\operatorname{Ver}_{H \to G}: H^{*}(H, M) \to H^{*}(G, M)$.

## Formulae

Exercise 7.1 Transitivity If $K < H < G$ with

$$
[ H: K ] <   \infty \quad [ H: G ] <   \infty ,
$$

then

$$
\operatorname{Ver} _ {H \hookrightarrow G} \operatorname{Ver} _ {K \hookrightarrow H} = \operatorname{Ver} _ {K \hookrightarrow G}.
$$

Exercise 7.2 If $H < G$ is finite index, then

$$
H ^ {*} (G, M) \xrightarrow {\operatorname{Res} _ {H \hookrightarrow G}} H ^ {*} (H, M) \xrightarrow {\operatorname{Ver} _ {H \hookrightarrow G}} H ^ {*} (G, M)
$$

is multiplication by  $[G:H]$ .

Exercise 7.3 Mackey Formula Suppose

$$
\begin{array}{c c c} g h g ^ {- 1} & \longmapsto & h \\ K \cap g H g ^ {- 1} & \longrightarrow & H \\ \cap & & \cap \text { finite   index } \\ K & \underset {\text { inclusion }} {\longrightarrow} & G \end{array}
$$

Then

$$
\operatorname{Res} _ {K \rightarrow G} \operatorname{Ver} _ {H \hookrightarrow G} = \sum_ {K g H \in K \backslash G / H} \operatorname{Ver} _ {K \cap g H g ^ {- 1} \rightarrow K} \operatorname{Res} \quad K \cap g H g ^ {- 1} \rightarrow H _ {x \mapsto g ^ {- 1} x g}.
$$

This is not fantastically useful.

Interesting special case:  $H = K \triangleleft G$  a normal subgroup of finite index, then

$$
\operatorname{Res} _ {H \hookrightarrow G} \operatorname{Ver} _ {H \hookrightarrow G} = \sum_ {g H \in G / H} \operatorname{Res} \quad \begin{array}{l} H \to H \\ h \mapsto g ^ {- 1} h g \end{array} .
$$

Proof of 2 Check in degree zero and use the Theorem:

$$
\begin{array}{c c c c c} M ^ {G} & \xrightarrow {\text { Res }} & M ^ {H} & \xrightarrow {\text { Ver }} & M ^ {G} \\ m & \longmapsto & m & \longmapsto & \sum_ {g H \in G / H} (g H)   m = [ G: H ]   m \quad \text { for }   m \in M ^ {G}. \end{array}
$$

Corollary of 2 Suppose that G is a finite group and M is a G-module so that multiplication by  $|G|$  is an isomorphism of M. Then  $H^{+}(G, M) = 0$ , where  $H^{+}$ means  $H^{*}$  for  $* > 0$ .

Proof Take $H = \{e\}$. Then we have the commutative

![](images/page_40_image_14.jpg)

Multiplication by $|G|$ is an isomorphism and $H^{*}(e, M) = 0$, for $q > 0$, as the trivial group $e$ is hilariously free.

Theorem (Schur–Zassenhaus) Any extension  $* \longrightarrow H \longrightarrow G \stackrel{p}{\longrightarrow} Q \longrightarrow *$  of finite groups, where  $|H|$  and  $|Q|$  are relatively prime, splits, i.e., there exists a homomorphism  $s : Q \to G$  so that ps = id.

In particular, if $H \triangleleft G$, for $G$ finite and $|H|$ relatively prime to $[G : H]$, then there exists a subgroup complementary to $H$.

Proof (in the spirit of finite group-theory) Let G be a minimal counter-example. Let P be a Sylow p-subgroup of G for a prime p dividing  $|H|$ . Then since  $|H|$  and  $|Q|$  are relatively prime, we must have  $P \subset H$ .

Claim  $N_{G}(P)$  maps onto Q, for, given  $q \in Q$ , lift it to g; compare  $gPg^{-1}$  and P, both Sylow p-subgroups of H, so they are conjugate in H and there exists  $h \in H$  with  $gPg^{-1} = hPh^{-1}$  which implies  $h^{-1}gP(h^{-1}g)^{-1} = P$ , so  $h^{-1}g \in N_{G}H$ , the normalizer of H in G, and  $h^{-1}g \stackrel{p}{\longmapsto} q$ . Thus we have

![](images/page_41_image_4.jpg)

where the kernel of the top map is  $N_{H}P$ .

By minimality, if  $N_{G}(P) < G$ , then  $N_{G}(P)$  would contain a subgroup mapping onto Q, a contradiction since the top sequence would then split, whence the bottom as well. We conclude that

$$
N _ {G} P = G.
$$

Transitivity argument Suppose we can find a subgroup K so that 1 < K < H with  $K \triangleleft G$ . Then

$$
* \longrightarrow H / K \longrightarrow G / K \longrightarrow Q \longrightarrow *.
$$

By minimality, this splits. Let $A \subset G / K$ map isomorphically onto $Q$. Then $A = B / K$ where $B \subsetneq G$ with $B \twoheadrightarrow Q$. It is therefore an extension of $Q$ by $H \cap B$, which is of order prime to $Q$. By minimality again, this extension

$$
* \longrightarrow B \cap H \longrightarrow B \longrightarrow Q \longrightarrow *
$$

splits, giving a section  $Q \rightarrow B$  and hence a section  $Q \rightarrow G$ , contradiction. Thus K as above does not exist.

We conclude that for a minimal counter-example G, H has no proper subgroups K which are normal in G. In particular, P, which is the unique Sylow p-subgroup of G since it is normal in G must be all of H, so P = H. Since P has no characteristic subgroups, i.e., invariant under all automorphisms of the group, it must be an elementary abelian p-group.

Now, use that  $H^{2}(Q, H)$  classifies the extensions for H abelian. H is a p-group and p is relatively prime to  $|Q|$ , so the Corollary of 2 above implies that  $H^{+}(Q, H) = 0$ . A minimal counter-example therefore cannot exist.

Let $\mathcal{C}$ be some category and fix some $X\in \mathrm{Ob}\mathcal{C}$. Define $\mathcal{C}^{\mathrm{op}} =$ opposed category, which has the same objects but with $\operatorname {Hom}_{\mathcal{C}^{\mathrm{op}}}(X,Y) = \operatorname {Hom}_{\mathcal{C}}(Y,X)$.

Define  $h_{X}:C^{op}\rightarrow$  Sets, i.e., just a contravariant functor  $C\rightarrow$  Sets, given by

$$
h _ {X}: Y \longmapsto \operatorname{Hom} _ {\mathcal {C}} (Y, X).
$$

Define

$$
\begin{array}{c} h ^ {X}: \mathcal {C} \longrightarrow \text { Sets } \\ Y \longmapsto \operatorname{Hom} _ {\mathcal {C}} (X, Y). \end{array}
$$

Yoneda Lemma If $F: \mathcal{C}^{\mathrm{op}} \to$ Sets is a functor, then the set $\operatorname{NatTrans}(h_X, F)$ of natural transformations from $h_X$ to $F$ is in one-to-one correspondence with $F(X)$ given by

$$
\begin{array}{c} {(\theta : h _ {X} \to F) \longmapsto \theta (X) (\mathrm{id} _ {X})} \\ {\theta \text { so   that } \theta (Y) (f) = F (f) \xi \longleftrightarrow \xi .} \end{array}
$$

In a diagram,

$$
\begin{array}{c} \operatorname{Hom} (Y, X) = h _ {X} (Y) \xrightarrow {\theta (Y)} F (Y) \\ \Bigg | _ {f _ {*}} ^ {\uparrow} \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \operatorname{Hom} (X, X) = h _ {X} (X) \xrightarrow {\theta (X)} F (X) \end{array}
$$

where

$$
\theta (Y) (f) = F (f) \theta (X) (\mathrm{id} _ {X}).
$$

Corollary NatTrans $(h_X, h_Y)$ is in one-to-one correspondence with $\operatorname{Hom}(X, Y)$. Modulo set-theory, we have a functor as follows

$$
\begin{array}{l} \mathcal {C} \longrightarrow \operatorname{Funct} (\mathcal {C} ^ {\mathrm{op}}, \text { Sets }) \\ X \longmapsto h _ {X}, \end{array}
$$

where Funct as a category has its morphisms given by natural transformations, and the corollary says

$$
\operatorname{Hom} _ {\text { Funct } (\mathcal {C} ^ {\mathrm{op}}, \text { Sets })} (h _ {X}, h _ {Y}) = \operatorname{Hom} _ {\mathcal {C}} (X, Y).
$$

Thus $X \mapsto h_X$ gives an embedding of $\mathcal{C}$ in $\text{Funct}(\mathcal{C}^{\text{op}}, \text{Sets})$.

Definition A functor $F: \mathcal{C}^{\mathrm{op}} \to \text{Sets is representable if it is isomorphic to a functor of the form } h_X$. According to Yoneda's Lemma, an isomorphism of $h_X \simeq F$ is given by some $\xi \in F(X)$. Thus $F$ is representable when there exist $X \in \operatorname{Ob} \mathcal{C}$ and $\xi \in F(X)$ so that for all $Y \in \operatorname{Ob} \mathcal{C}$,

$$
\begin{array}{c} \operatorname{Hom} _ {\mathcal {C}} (Y, X) \stackrel {{\simeq}} {{\longrightarrow}} F (Y) \\ f \longmapsto F (f) \xi . \end{array}
$$

This says  $(X, \xi)$  have the following universal property: for any  $Y \in ObC$  and  $\eta \in F(Y)$  there is a unique map  $f : Y \to X$  so that  $\eta$  is induced from  $\xi$ .

General exercise Re-write universal constructions in terms of representable functors.

Example 8.1 A final (or terminal) object of C, call it e, is an object so that for all  $Y \in C$  there exists a unique  $Y \to e$ , and e represents the functor  $Y \to *$ .

Example 8.2 The product $\Pi_I X_i \in \mathrm{Ob}\mathcal{C}$ of $X_i \in \mathrm{Ob}\mathcal{C}$, for $i \in I$, equipped with maps $\operatorname{pr}_i: \Pi_I X_i \to X_i, i \in I$, has the universal property that for all $Y$ and $f_i: Y \to X_i$, for all $i \in I$, there exists a unique map $Y \xrightarrow{f} \Pi X_i$ so that $\operatorname{pr}_i f = f_i$. The functor represented is $\prod_{i \in I} h_{X_i}$.

Example 8.3 Let $I$ be a small category and $i \mapsto X_{i}$ a functor from I to $\mathcal{C}$. Then $\lim_{\leftarrow} X_{i}$ denotes an object in $\mathcal{C}$ equipped with maps

$$
p _ {i}: \varprojlim X _ {i} \longrightarrow X _ {i}
$$

compatible with the morphisms in I in the sense that for all  $\alpha: i \rightarrow i'$  in I, the diagram

![](images/page_45_image_0.jpg)

commutes and enjoying the obvious universal property. The “new” terminology for this is simply  $\varprojlim = \lim$  and  $\varinjlim = colim$ . The functor being so represented assigns to Y all

$$
(f _ {i}) \in \prod_ {i \in \mathrm{Ob} I} \operatorname{Hom} (Y, X _ {i})
$$

so that for all $\alpha : i \mapsto i'$ we have $\alpha_{*} f_{i} = f_{i'}$. We can write this as

$$
\operatorname{Ker} \left\{\prod_ {i \in \mathrm{Ob} \mathcal {C}} \operatorname{Hom} (Y, X _ {i}) \Longrightarrow \prod_ {i ^ {\prime} \xleftarrow {\alpha} i} \operatorname{Hom} (Y, X _ {i ^ {\prime}}) \right\}
$$

$$
\begin{array}{l} f (i) \mapsto \left(\left(i ^ {\prime} \stackrel {\alpha} {\longleftarrow} i\right) \mapsto f _ {i ^ {\prime}}\right) \\ \mapsto \left(\left(i ^ {\prime} \stackrel {\alpha} {\longleftarrow} i\right) \mapsto \alpha_ {*} f _ {i}\right) \end{array}
$$

where Ker here denotes equalizer, i.e., elements having the same image under each map.

If this kernel is written  $\lim_{\leftarrow I}\operatorname{Hom}(Y,X_{i})$  then

$$
\operatorname{Hom} _ {\mathcal {C}} \left(Y, \varprojlim X _ {i}\right) = \varprojlim_ {I} \operatorname{Hom} _ {\mathcal {C}} (Y, X _ {i}).
$$

Note that if $F:\mathcal{C}\to \mathrm{Sets}$ , then

$$
\varprojlim_ {\mathcal {C}} F = \operatorname{Ker} \left\{\prod_ {X _ {0}} F (X _ {0}) \Longrightarrow \prod_ {X _ {0} \leftarrow X _ {1}} F (X _ {0}) \right\},
$$

and this coincides with $H^{0}(\mathcal{C}, F)$ for $F$ an abelian group functor, i.e., in general

$$
H ^ {0} (\mathcal {C}, F) = \varprojlim_ {\mathcal {C}} F.
$$

For example, a $G$-set is a functor

$$
\widetilde {G} \longrightarrow \text { Sets }
$$

$$
* \longmapsto S
$$

and then

$$
\varprojlim_ {\widetilde {G}} S = S ^ {G}.
$$

In general by Yondea, we have $\mathrm{Hom}_{\mathrm{Funct}(\mathcal{C},\mathrm{Sets})}(h^{X},F) = F(X)$ and get an embedding

$$
\begin{array}{c} \mathcal {C} ^ {\mathrm{op}} \longrightarrow \operatorname{Funct} (\mathcal {C}, \text { Sets }) \\ X \longmapsto h ^ {X}. \end{array}
$$

An initial object $\phi$ is so that $\operatorname{Hom}(\phi, Y) = *$ for all $Y$.

For instance:

(1) Direct sum $\bigsqcup_{I} X_{i}$: for all $i \in I$, we have $X_{i} \xrightarrow{in_{i}} \bigsqcup_{I} X_{i}$ with the appropriate universal property.

(2) Direct limit (or colimit):  $\lim_{I} X_{i}$  together with  $Y_{i} \xrightarrow{in_{i}} \lim_{I} X_{i}$  compatible with the arrows of I and the appropriate universal property.

(1) represents $\operatorname{Hom}\left(\bigsqcup_{I} X_i, Y\right) = \prod_{I} \operatorname{Hom}(X_i, Y)$, and

(2) represents $\mathrm{Hom}_{\mathcal{C}}\left(\varinjlim_{I}X_i,Y\right)=\varprojlim_{I}\mathrm{Hom}_{\mathcal{C}}(X_i,Y)$.

Example With  $C = \widetilde{G}$ , a functor  $S : \widetilde{G} \to$  Sets is the same as a G-set S, and a functor  $M : \widetilde{G} \to$  Ab is a G-module M, where

$$
\varprojlim_ {\widetilde {G}} S = S ^ {G} \text {   and   } \varprojlim_ {\widetilde {G}} M = M ^ {G}.
$$

But what about

$$
\varinjlim_ {\widetilde {G}} S = ? \text {   and   } \varinjlim_ {\widetilde {G}} M = ?
$$

Now,  $\varinjlim S$  is a set together with arrows  $S \rightarrow \varinjlim S$  compatible with the arrows in

$$
\tilde {G}
$$

![](images/page_46_image_16.jpg)

Thus $\lim_{\widetilde{G}} S$ is the set of orbits $G \setminus S$, and

$$
\begin{array}{r l} \varinjlim_ {\widetilde {G}} S & = M / \{g m - m: g \in G, m \in M \} \\ & = \text { largest   quotient   module   of } M \text { on   which } G \text { acts   trivially. } \end{array}
$$

Thus, we must specify the category in which we are computing  $\varinjlim$ , as they do not in general agree.

## Adjoint Functors

Suppose C and  $C'$  are categories. A pair of adjoint functors is  $C \xrightarrow{F} C'$  together with a natural bijection

$$
\operatorname{Hom} _ {\mathcal {C} ^ {\prime}} (F (X), Y) \stackrel {{\sim}} {{\longrightarrow}} \operatorname{Hom} _ {\mathcal {C}} (X, G (Y)).\tag{*}
$$

for each $X \in \operatorname{Ob} \mathcal{C}$, $Y \in \operatorname{Ob} \mathcal{C}'$. $F$ is the left adjoint and $G$ right adjoint of the pair. By Yoneda, (\*) is given either by natural transformations

$$
\alpha : F G \longrightarrow \mathrm{id} _ {\mathcal {C}}
$$

or

$$
\beta : \mathrm{id} _ {\mathcal {C}} \longrightarrow G F.
$$

Easy to check that

$$
F = F \mathrm{id} _ {\mathcal {C}} \xrightarrow {F \cdot \beta} F G F \xrightarrow {\alpha \cdot F} \mathrm{id} _ {\mathcal {C ^ {\prime}}} F = F
$$

and

$$
G = \mathrm{id} _ {\mathcal {C}} G \xrightarrow {\beta \cdot G} G F G \xrightarrow {G \cdot \alpha} G \mathrm{id} _ {\mathcal {C ^ {\prime}}} = G
$$

are both the identity. Thus we could alternatively define adjoint functors to be  $(F, G)$  together with  $\alpha$  and  $\beta$  so that these composites are the identity. To see this given  $\alpha, \beta$ , we have

$$
\operatorname{Hom} (F X, Y) \xrightarrow {G} \operatorname{Hom} (G F X, G Y) \xrightarrow {\beta^ {*}} \operatorname{Hom} (X, G Y) \xrightarrow {F} \operatorname{Hom} (F X, F G Y) \xrightarrow {\alpha^ {*}} \operatorname{Hom} (F X, Y)
$$

By Yoneda, take $Y = F(X)$. Then

$$
\mathrm{id} _ {X} \longmapsto \mathrm{id} _ {G F X} \quad \text { and } \quad \beta \longmapsto F \cdot \beta \longmapsto \alpha F \cdot \beta  ,
$$

and equivalence of the two definitions follows.

Kan Formulae for Computing Adjoint Functors

Let $\mathcal{C}$ and $\mathcal{C}'$ be small categories and $f:\mathcal{C}\to \mathcal{C}'$. Consider

$$
\text { Funct } (\mathcal {C}, \text { Sets }) \xleftarrow {f ^ {*}} \text { Funct } (\mathcal {C} ^ {\prime}, \text { Sets })
$$

i.e.,

$$
(f ^ {*} F) (X) = F (f (X)).
$$

This $f^{*}$ has two adjoints $f_{!}$ and $f_{*}$.

Theorem $f^{*}$ has a left adjoint $f_{!}$ (pronounced $f$ shriek) and right adjoint $f_{*}$.

We shall discuss this next time.

Suppose $\mathcal{C} \xrightarrow[F]{F} \mathcal{C}'$ is a pair of adjoint functors where we are given natural transformations

$$
\operatorname{Hom} _ {\mathcal {C} ^ {\prime}} (F X, Y) \simeq \operatorname{Hom} _ {\mathcal {C}} (X, G Y).
$$

Example 9.1

$$
(\text { Sets }) \xrightarrow [ G = \text { forgetful } ]{F = \text { free   group }} (\text { Groups })
$$

and

$$
\operatorname{Hom} _ {\text { groups }} (F S, G) = \operatorname{Hom} _ {\text { Sets }} (S, G _ {\text { forgotten }}).
$$

Example 9.2 Suppose $A \xrightarrow{u} B$ is a homomorphism of rings with unit, and $\operatorname{Mod}_A$ is the category of (left) $A$-modules. We have

$$
\operatorname{Mod} _ {A} \xleftarrow {u ^ {*}} \operatorname{Mod} _ {B}
$$

where  $u^{*}$  is restriction of scalars with respect to u, i.e.,  $M \mapsto M$  and we have  $am = u(a)m$ .

Then $u^{*}$ has a left adjoint given by base extension

$$
\operatorname{Mod} _ {A} \longrightarrow \operatorname{Mod} _ {B},
$$

i.e.,  $M \longmapsto B \otimes_{A} M$  B is a right A module via u, and

$$
\operatorname{Hom} _ {B} (B \otimes_ {A} M, N) = \operatorname{Hom} _ {A} (M, u ^ {*} N).
$$

And $u^{*}$ has also a right adjoint

$$
\begin{array}{r l}\operatorname{Mod} _ {A}&\longrightarrow \operatorname{Mod} _ {B}\\M&\longmapsto \operatorname{Hom} _ {A} (B, M) = \{f: B \rightarrow M \mid f (u (a) b) = u f (b) \text { and } f \text { is   additive } \}\end{array}
$$

where $\operatorname{Hom}_A(B, M)$ is a left $B$-module by

$$
b f (b _ {1}) = f (b _ {1} b), \text {   i.e.,   use   right   action   on   } B,
$$

and

$$
\operatorname{Hom} _ {B} (N, \operatorname{Hom} _ {A} (B, M)) = \operatorname{Hom} _ {A} (u ^ {*} N, M).
$$

Exercise Check this. The idea is that the left-hand side is  $\operatorname{Hom}_{A}(B \otimes_{B} N, M)$  and  $B \otimes_{B} N = N$ ; see Cartan and Eilenberg.

Summary of Example 9.5:

$$
M \longmapsto B \otimes_ {A} M
$$

$$
M \longmapsto \operatorname{Hom} _ {A} (B, M)
$$

with canonical maps; recall Yoneda's lemma that canonical maps are given by $FG \to$ id and $GF \leftarrow$ id

$$
\begin{array}{c c c} u ^ {*} (B \otimes_ {A} M) \longleftarrow M & B \otimes_ {A} u ^ {*} N \longrightarrow N \\ 1 \otimes m \quad \longleftarrow m & b \otimes n \quad \longmapsto n \end{array}
$$

and

$$
\begin{array}{c c c} \operatorname{Hom} _ {A} (B, u ^ {*} N) \longrightarrow & N & u ^ {*} \operatorname{Hom} _ {A} (B, N) \longleftarrow N \\ f & \longmapsto f (1) & (b \mapsto b n) \quad \longleftarrow n. \end{array}
$$

Example 9.3 Consider the category of topological spaces and continuous maps. Let $I$ be compact. Then

$$
\operatorname{Hom} (X \times I, Y) = \quad \operatorname{Hom} (X, Y ^ {I})
$$

with  $Y^{I}$  given the compact-open topology.

Changing gears now, consider the following situation: $\mathcal{C}$ and $\mathcal{C}'$ are small categories and $f:\mathcal{C}\to\mathcal{C}'$ a functor. Set $\widehat{C}=\text{Funct}(\mathcal{C},\text{Sets})$, so we have $\widehat{C}\xleftarrow{f^{*}}\widehat{\mathcal{C}'}$, $G\circ f\leftrightarrow G$.

Kan's Formula $^{1}$

$f^{*}$  has left adjoint  $f_{!}$  and right adjoint  $f_{*}$  given by

$$
(f _ {!} F) (Y) = \varinjlim_ {(X, u: f X \rightarrow Y)} F (X)
$$

$$
(f _ {*} F) (Y) \underset {(X, Y \rightarrow f X)} {\lim} F (X).
$$

For $Y \in \operatorname{Ob} \mathcal{C}'$, consider the category whose objects are pairs $(X, u)$, $X \in \operatorname{Ob} \mathcal{C}$ and $u: fX \to Y$ a morphism in $\mathcal{C}'$ and

$$
\operatorname{Hom} ((X, u), (X ^ {\prime}, u ^ {\prime})) = \left\{v: X \rightarrow X ^ {\prime} \mid \downarrow \mathrm{f(v)} \quad Y \text {commutes} \right\}
$$

Call this the left-fiber of $f: \mathcal{C} \to \mathcal{C}'$ over $Y$. As an exercise, we can check that this is a category.

Similarly, we have the right-fiber of $f: \mathcal{C} \to \mathcal{C}'$ over $Y$ consisting of all pairs $(X, u: Y \to fX)$, again a category.

Each of these is different from the fiber of $f: \mathcal{C} \to \mathcal{C}'$ over $Y$, which consists of all $X \in \operatorname{Ob} \mathcal{C}$ with $f(X) = Y$, and morphisms sit over the identity of $Y$. The fiber is denoted simply $f^{-1}Y$.

Note that $f^{-1}Y$ is a subcategory of both the left fiber and the right fiber.

Example 9.4 Suppose C and  $C'$  are discrete categories, i.e., objects are sets and all arrows are identity maps. Then  $f: C \to$  Sets is a family of sets  $F(X)$  indexed by  $X \in \operatorname{Ob} C$ . So we can think of F as just a set over  $\operatorname{Ob} C$ , i.e., F, so in this case  $\widehat{C}$  is

the category of sets over Ob C, and given

![](images/page_51_image_12.jpg)

we have $(f^{*}G)(X) = G(fX)$, so $f^{*}G$ is just the usual pull back of $G$ via $f$. Furthermore $f_{!}F = F$ is viewed as a set over $\operatorname{Ob}\mathcal{C}'$ via $f$ since $f_{!}(F)(Y) = \coprod_{X \in f^{-1}Y} F(X)$, and this is just Kan's formula

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$f_{1}$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{1}$ For  $f_{1}$  this formula also appears in SGA4 Éxp. 1 by Grothendieck and Verdier [6].</span></small>

$$
(f _ {!} F) (Y) = \varinjlim_ {(X, f X \rightarrow Y)} F (X) \text {   but   a   discrete   category   so   OK. }
$$

As to $f_{*}$ , we have

$$
\mathrm{Hom} _ {\widehat {\mathcal {C}}} (G, f _ {*} F) = \mathrm{Hom} _ {\widehat {\mathcal {C}}} (f ^ {*} G, F)
$$

but

$$
\operatorname{Hom} (G, f _ {*} F) = \left(f _ {*} F\right) (Y) \quad \text { with } f ^ {*} G = f ^ {- 1} Y \subset \mathrm{Ob} \mathcal {C}
$$

and

$$
\begin{array}{r l} \operatorname{Hom} _ {\text { sets   over   Ob } \mathcal {C}} (f ^ {*} G, F) & = \text { sections   of } F \text { over } f ^ {- 1} Y \\ & = \prod_ {X \in f ^ {- 1} Y} F (X). \end{array}
$$

In this case

$$
(f _ {!} F) (Y) = \coprod_ {X \in f ^ {- 1} Y} F (X),
$$

$$
(f _ {*} F) (Y) = \prod_ {X \in f ^ {- 1} Y} F (X).
$$

Example 9.5 Suppose $\mathcal{C} = \widetilde{G}$ and $\mathcal{C}' = \widetilde{G}'$ with $f: G \to G'$ a group homomorphism. Then $\widehat{\mathcal{C}}$ is the category of $G$-sets, $\widehat{\mathcal{C}'}$ the category of $G'$-sets, and

$$
\begin{array}{c} \xrightarrow {f _ {!}} \\ (G \text {-sets}) \xleftarrow {f ^ {*}} (G ^ {\prime} \text {-sets}) \\ \xrightarrow {f _ {*}} \end{array}
$$

where essentially $f^{*}S = S \circ f$ and $f^{*}S = S$ viewed as a $G$-set via $f$. Furthermore, we have

$$
f _ {!} S = G ^ {\prime} \times_ {G} S \stackrel {{d}} {{=}} (G \times S) / (g ^ {\prime}, g s) \sim (g ^ {\prime} f (g), s)
$$

and in fact

$$
\operatorname{Hom} _ {G ^ {\prime} - \text { set }} (G ^ {\prime} \times_ {G} S, T) = \operatorname{Hom} _ {G - \text { set }} (S, f ^ {*} T).
$$

We also have that

$$
f _ {*} S = \operatorname{Hom} _ {G - \text { set }} (G ^ {\prime}, S) = \{h: G ^ {\prime} \rightarrow S \mid h (f (g) g ^ {\prime}) = g h (g ^ {\prime}) \}
$$

is a $G'$-set with $G'$ acting by

$$
(g ^ {\prime} h) (g _ {1} ^ {\prime}) = h (g _ {1} ^ {\prime} g ^ {\prime}),
$$

in analogy with the case of rings.

The Kan formulae are

$$
(f _ {!} F) (Y) = \varinjlim_ {(X, f X \xrightarrow {u} Y)} F (X) = \operatorname{Coker} \left\{\coprod_ {Y \xleftarrow {u} f X _ {0}} F (X _ {0}) \Leftarrow \coprod_ {Y \xleftarrow {u} f X _ {0} \xleftarrow {f v} f X _ {1}} F (X _ {1}) \right\}
$$

where

$$
\operatorname{Coker} \left\{A \underset {d _ {1}} {\overset {d _ {0}} {\rightleftharpoons}} B \right\} = A / (d _ {0} b \sim d _ {1} b).
$$

For the case of groups

$$
\begin{array}{l} f _ {!} S \left(* ^ {\prime}\right) = \operatorname{Coker} \left\{\coprod_ {\substack {* ^ {\prime} \xleftarrow {u \in G ^ {\prime}} * ^ {\prime}}} S (*) \Leftarrow \coprod_ {\substack {* \xleftarrow {u ^ {\prime} \in G ^ {\prime}} * ^ {\prime} \xleftarrow {v \in G} *}} S (*) \right\} \\ = \operatorname{Coker} \left\{G ^ {\prime} \times S \Leftarrow G ^ {\prime} \times G \times S \right\} \\ (u f (v), s) \leftrightarrow (u, v, s) \\ (u, v s) \leftrightarrow \\ = G ^ {\prime} \times_ {G} S. \end{array}
$$

$$
\varprojlim_ {X, Y \xrightarrow {u} f X} = \operatorname{Hom} _ {G ^ {\prime}} (G, S).
$$

As an exercise, check Kan also for $f_{*}$, i.e., confirm that

## Chapter 10 Abelian and Additive Categories

## Abelian Categories

For example,  $\operatorname{Mod}_{A} = (\text{left}) A\text{-modules or functors Funct}(\mathcal{C}, \operatorname{Mod}_{A})$  with C a small category.

In $\operatorname{Mod}_A$, we have that $\operatorname{Hom}_A(M, N)$ is an abelian group in a natural way and have a notion of exact sequences. We have the same structures in functors $\operatorname{Funct}(\mathcal{C}, \operatorname{Mod}_A)$, namely

$$
\operatorname{Hom} _ {\text { Funct }} (F, G) = \operatorname{Ker} \left\{\prod_ {X \in \mathrm{Ob} \mathcal {C}} \operatorname{Hom} _ {A} (F (X), G (X)) \Rightarrow \prod_ {\substack {X - \frac {u}{n}, Y \\ \text {in} \mathcal {C}}} \operatorname{Hom} _ {A} (F (X), G (Y)) \right\},
$$

where the sum of $\theta : F \to G$ and $\eta : F \to G$ is $(\theta + \eta)(X) = \theta(X) + \eta(X)$. Moreover, a sequence of functors $F \to F' \to F''$ from $\mathcal{C}$ to $\operatorname{Mod}_A$ is exact when $F(X) \to F'(X) \to F''(X)$ is exact for all $X \in \operatorname{Ob} \mathcal{C}$.

Question Can we get at the abelian group structure on $\operatorname{Hom}_A(M, N)$ more intrinsically in terms of the category $\operatorname{Mod}_A$?

If $X$ is an object of $\mathcal{C}$, then a group (respectively ring, lattice, etc.) structure on $X$ is a group (etc.) structure on the functor $h_X = \operatorname{Hom}_{\mathcal{C}}(\cdot, X)$, i.e., for all $Y \in \operatorname{Ob}\mathcal{C}$ we specify a group (etc.) structure on $\operatorname{Hom}_{\mathcal{C}}(Y, X)$ so that for all $u: Y \to Y'$ in $\mathcal{C}$, we have a group (etc.) homomorphism $\operatorname{Hom}_{\mathcal{C}}(Y', X) \to \operatorname{Hom}_{\mathcal{C}}(Y, X)$. Put still differently, a group structure on $X$ is a lifting

![](images/page_54_image_8.jpg)

of  $h_{X}$  to a functor  $C^{op} \rightarrow$  Groups. Suppose now C has a terminal object e and that the products  $X \times X$  and  $X \times X \times X$  exist. Note that the group law gives  $h_{X} \times h_{X} \rightarrow h_{X}$ , i.e.,

![](images/page_55_image_0.jpg)

where the vertical map is given by  $f \mapsto (\mathrm{pr}_{1}f, \mathrm{pr}_{2}f)$ , and so by Yoneda's lemma, this natural transformation  $h_{X \times X} \to h_{X}$  is given by a morphism  $m : X \times X \to X$ .

The unit element gives a natural transformation $\operatorname{Hom}(Y, e) = \text{point} \to \operatorname{Hom}(Y, X)$, and by Yoneda's lemma, this comes from $e \xrightarrow{1} X$.

Finally and similarly, the group inverse is given by a map $X \xrightarrow{\mu} X$.

Then the group axioms correspond to the following diagrams commuting:

![](images/page_55_image_5.jpg)

$$
\left. \begin{array}{l l} X \xrightarrow {\text {(id,1)}} & X \times X \xrightarrow {m} X \\ a \mapsto & (a, 1) \mapsto a 1 \\ X \xrightarrow {\text {(1,id)}} & (X \times X) \xrightarrow {m} X \\ a \mapsto & (1, a) \mapsto 1 a \end{array} \right\}
$$

are $\mathrm{id}_X$, where $1:X\to X$ is short

![](images/page_55_image_8.jpg)

![](images/page_55_image_9.jpg)

In  $Mod_{A}$ , every object N is an abelian group object in a natural way because  $\operatorname{Hom}_{A}(\cdot, N)$  has a natural abelian group structure.

A cogroup structure on X in C is the same as a group structure on X in  $C^{op}$ , i.e., a group structure on  $\operatorname{Hom}(X,\cdot):\mathcal{C}\to\operatorname{Sets}$ . Such a structure is given by

$X \longrightarrow X \coprod X, \text{comultiplication},$

$X \longrightarrow \phi, \phi = \text{initial object},$

$X \longrightarrow X$, an inverse

satisfying the appropriate diagrams.

Thus, in  $Mod_{A}$ , every object is naturally a co-abelian group object since  $\operatorname{Hom}_{A}(M,\cdot)$  is naturally an abelian group.

Example Any free group is a co-group in the category of groups since

$$
\operatorname{Hom} _ {\text { Groups }} (F (S), G) = \prod_ {S} G,
$$

where $F(\bullet)$ denotes free group on $\bullet$.

Exercise Interpret the arrows above in this setting.

Theorem Suppose we have a monoid object X and a co-monoid object Y in a category C. Then the two possible monoid structures on  $\operatorname{Hom}_{\mathcal{C}}(Y, X)$  coincide and this unique operation is abelian.

Standard example C = category of spaces with basepoint and homotopy classes of basepoint-preserving maps. Take G to be an H-space (e.g.,  $G = \Omega X$ , the loop space) and Y to be  $S^{1}$ , which is a co-group because homotopy classes of maps  $[S^{1}, X] = \pi_{1} X$ . Then the theorem says the two operations on  $[S^{1}, G] = \pi_{1} G$  coincide and are abelian.

Proof of Theorem Denote

$$
\begin{array}{r l} Y & \xrightarrow {\gamma} Y \coprod Y, \text {   comultiplication } \\ Y & \xrightarrow {\varepsilon} \phi , \text {   co - unit } \\ \widetilde {\varepsilon}: Y & \xrightarrow {\varepsilon} \phi \xrightarrow {\text { unique }} Y \end{array}
$$

Thus we have

$$
Y \xrightarrow {\gamma} Y \bigsqcup Y \xrightarrow [ (\mathrm{id} , \widetilde {\varepsilon}) ]{(\widetilde {\varepsilon} , \mathrm{id})} X
$$

Apply the monoid-valued functor $\operatorname{Hom}(\cdot, X)$ to these arrows

$$
\begin{array}{c} \operatorname{Hom} (Y, X) \times \operatorname{Hom} (Y, X) \\ \uparrow \cong \\ \operatorname{Hom} (Y \bigsqcup Y, X) \end{array} \xrightarrow {\gamma^ {*}} \operatorname{Hom} (Y, X)
$$

We thus get a map  $M \times M \xrightarrow{\theta} M$ , where M is the monoid  $\operatorname{Hom}(Y, X)$  with operation coming from  $X \times X \to X$ .  $\theta$  is a monoid homomorphism so that  $\theta(m, 1) = m = \theta(1, m)$  since  $\varepsilon$  behaves as a co-unit for  $\gamma$ . Now,

$$
\theta (m _ {1}, m _ {2}) = \theta ((m _ {1}, 1) (1, m _ {2})) = \theta (m _ {1}, 1) \theta (1, m _ {2}) = m _ {1} m _ {2},
$$

so  $\theta$  has same effect as the product on M. Remains to check abelian. To see this, replace  $X \times X \xrightarrow{m} X$  by  $X \times X \xrightarrow{flip} X \times X \xrightarrow{m} X$ . ☐

In $\mathrm{Mod}_A$, we have $\phi = e$ since the 0 module is both initial and final. Also, the canonical map $M \coprod N \xrightarrow{\alpha} M \times N$ is an isomorphism, where $\alpha$ is given by

$$
\begin{array}{c} \operatorname{pr} _ {1} \alpha \operatorname{in} _ {1} = \operatorname{id} _ {M}, \operatorname{pr} _ {1} \alpha \operatorname{in} _ {2} = 0, \\ \operatorname{pr} _ {2} \alpha \operatorname{in} _ {1} = 0, \operatorname{pr} _ {2} \alpha \operatorname{in} _ {2} = \operatorname{id} _ {N}. \end{array}
$$

Moreover, the co-monoid (in fact, co-abelian group) structure on M is given by

$$
M \xrightarrow {\Delta} M \times M \xleftarrow [ \cong ]{\alpha} M \bigsqcup M,
$$

and the abelian group structure is given by

$$
M \times M \xrightarrow {\alpha^ {- 1}} M \coprod M \xrightarrow {\text { fold }} M.
$$

We are led to define an additive category as a category $\mathcal{A}$ so that

(1) A has an object 0 which is both initial and final,

(2) for any $M, N \in \operatorname{Ob} \mathcal{A}, M \coprod N$ and $M \times N$ exist,

(3) the canonical map $M \coprod N \xrightarrow{\alpha} M \times N$ is an isomorphism,

(4) $\operatorname{Hom}_{\mathcal{A}}(M, N)$ is an abelian group for all $M, N \in \operatorname{Ob} \mathcal{A}$, with $\operatorname{Hom}_{\mathcal{A}}(\cdot, \cdot)$ given the natural structure as below.

Notice that (2) and (3) imply that $\operatorname{Hom}_{\mathcal{A}}(M, N)$ is an abelian monoid with $f + g$ defined as

$$
M \xrightarrow {\Delta} M \times M \xrightarrow {\alpha^ {- 1}} M \coprod M \xrightarrow {(f , g)} N
$$

or equivalently as

$$
M \xrightarrow {(f , g)} N \times N \xrightarrow {(\text { fold }) \circ \alpha^ {- 1}} N.
$$

We denote it as $M \oplus N = M \coprod N \approx M \times N$.

For A an additive category and  $f: M \rightarrow N$  in A, we define a cokernel for f as a pair C, p, where  $p: N \rightarrow C$  in A so that for all objects X

$$
0 \longrightarrow \operatorname{Hom} (C, X) \xrightarrow {p ^ {*}} \operatorname{Hom} (N, X) \xrightarrow {f ^ {*}} \operatorname{Hom} (M, X)
$$

is exact, i.e., $u \circ f$ zero implies $u$ factors through $C$

![](images/page_58_image_0.jpg)

Dually, a kernel for  $f: M \rightarrow N$  is a map  $i: K \rightarrow M$  so that for all X

$$
0 \longrightarrow \operatorname{Hom} (X, K) \stackrel {i _ {*}} {\longrightarrow} \operatorname{Hom} (X, M) \stackrel {f _ {*}} {\longrightarrow} \operatorname{Hom} (X, N)
$$

is exact, i.e., $f \circ u$ zero implies $u$ factors through $K$

![](images/page_58_image_4.jpg)

Now given f, take the kernel and cokernel to get

![](images/page_58_image_6.jpg)

Ker p is called the image Im f and Cok i the coimage Coim f of f.

We define an abelian category as an additive category $\mathcal{A}$ so that

(5) for any map $f$, Ker $f$ and Cok $f$ exist,

(6) for any map $f$, the canonical map Coim $f \to \operatorname{Im} f$ is an isomorphism.

## Chapter 11 Diagram Chasing in Abelian Categories

Example (standard example of additive but non-abelian category) Let A be the category of topological abelian groups. Then  $\operatorname{Hom}_{\mathcal{A}}(A, B)$  is itself an abelian group. Checking Condition (5), suppose  $f : A \to B$ , then Ker f is the usual set-theoretic kernel with the topology induced by A. Cok f is the group  $B/f(A)$  with the quotient topology, so the topology is Hausdorff for  $f(A)$  closed. Condition (6) breaks down however: the map

$$
\mathbb {R} _ {\text { discrete }} \xrightarrow {\mathrm{id}} \mathbb {R} _ {\text { usual }}
$$

from $\mathbb{R}$ with the discrete topology to $\mathbb{R}$ with the usual topology has $\mathrm{Ker} = \mathrm{Cok} = 0$, while $\mathrm{Im} = \mathbb{R}_{\mathrm{usual}}$, $\mathrm{Coim} = \mathbb{R}_{\mathrm{discrete}}$, i.e., $\mathrm{Im} = f(A)$ has the subspace topology and $\mathrm{Coim}f = f(A) \cong A / \mathrm{Ker}f$ has the quotient top.

Example If C is a small category, then A = Funct (C, Ab) is an abelian category. We can think of functors as diagrams of abelian groups indexed by C.

Suppose $u: F \to G$ is a natural transformation, then $\operatorname{Ker} u$ is computed as

$$
(\operatorname{Ker} u) (X) = \operatorname{Ker} (u (X): F (X) \longrightarrow G (X)),
$$

and similarly,

$$
(\operatorname{Cok} u) (X) = \operatorname{Cok} \left(F (X) \xrightarrow {u (X)} G (X)\right).
$$

As for checking Condition (6), we have

$$
\begin{array}{c} \operatorname{Ker} u (X) \longrightarrow F (X) \xrightarrow {u (X)} G (X) \longrightarrow \operatorname{Cok} u (X). \\ \Biggl \downarrow \\ \operatorname{Coim} u (X) \longrightarrow \operatorname{Im} u (X) \end{array}
$$

Note that sheaves of abelian groups on topological spaces is also an abelian category, but this requires some work that we shall skip.

Let A be an abelian category. Then  $f: X \to Y$  is an epimorphism if  $\operatorname{Cok} f = 0$  (i.e., if for all T,  $\operatorname{Hom}(Y, T) \hookrightarrow \operatorname{Hom}(X, T)$ ), and is a monomorphism if  $\operatorname{Ker} f = 0$  (i.e., for all T,  $\operatorname{Hom}(T, X) \hookrightarrow \operatorname{Hom}(T, Y)$ ). The adjectival form of epimorphism is epic and of monomorphism is monic. If f is epic, then we write  $A \twoheadrightarrow B$ , and if f is monic, then we write  $A \hookrightarrow B$ .

If $f$ is epic, then we have

![](images/page_60_image_3.jpg)

so that  $Y = \operatorname{Cok}(\operatorname{Ker} f \longrightarrow X)$ .

This has the consequence that if we are given $X \xrightarrow{f} Y$, in order to construct $Y \to T$, it suffices to construct $X \to T$ that carries $\operatorname{Ker} f$ to zero. This is the basis of the

General Principle Any of the usual diagram-chasing arguments used for modules can be extended to an arbitrary abelian category.

Below we indicate a proof of the Serpent Lemma in an arbitrary abelian category to illustrate how this is done.

Proposition (i) The pull back of an epic $f: Y \to Z$ by any map $X \to Y$ is again epic, i.e.,

$$
\begin{array}{c} X \times_ {Z} Y \xrightarrow {g ^ {\prime}} Y \\ \Big | _ {f ^ {\prime}} \\ \Big | _ {X} \xrightarrow {g} Z \end{array} \quad f e p i c i m p l i e s f ^ {\prime} e p i c.
$$

(ii) Dually, the push out of a monic $f: A \to B$ by any map $A \to C$ is again monic, i.e.,

$$
\begin{array}{c c} A & \xrightarrow {g} C \\ f \Bigg | _ {\Downarrow} & \begin{array}{c} \mid \\ \mid_ {f ^ {\prime}} \\ \Downarrow \end{array} \\ B & \xrightarrow [ g ^ {\prime} ]{} B + _ {A} C \end{array} \quad f \text {   monic   implies   } f ^ {\prime} \text {   monic. }
$$

Proof C is abelian if and only if  $C^{op}$  is abelian, so we prove only (ii).

We define  $B +_{A} C = \operatorname{Cok}\left(A \xrightarrow{(f, -g)} B \oplus C\right)$ . Then by definition of Cok, we have an exact sequence

$$
\begin{array}{c} 0 \longrightarrow \operatorname{Hom} (B + _ {A} C, T) \longrightarrow \operatorname{Hom} (B \oplus C, T) \xrightarrow {(f , - g) ^ {*}} \operatorname{Hom} (A, T) \\ \Bigg | _ {\text { Hom } (B, T) \oplus \operatorname{Hom} (C, T)} \end{array}
$$

Thus, a map  $B +_{A} C \rightarrow T$  is the “same” as maps  $B \rightarrow T$  and  $C \rightarrow T$  which agree on A, and so  $B +_{A} C$  is the usual push out.

Suppose now that  $A \xrightarrow{g} C$  is monic. Then we claim  $A \xrightarrow{(f,-g)} B \oplus C$  is monic. Suppose we have  $T \xrightarrow{} A \longrightarrow B \oplus C \longrightarrow C$  so  $T \to C$  is the zero map

and  $A \rightarrow C$  is monic which implies that  $T \rightarrow A$  is zero, proving the claim.

We proved before that  $X \rightarrow Y$  epic implies  $Y = \operatorname{Cok} (\operatorname{Ker} f \rightarrow X)$ , and dually for  $A \rightarrow B \oplus C$  monic, we have  $A = \operatorname{Ker}\{B \oplus C \rightarrow B + _{A} C\}$ . We thus have the commutative diagram

![](images/page_61_image_7.jpg)

But $-g$ monic and $-g \circ h = 0$ implies $h = 0$, so $\operatorname{Ker} g' \to B$ is the zero map whence $\operatorname{Ker} g' = 0$, as desired.

To substantiate the general principle above, we indicate a proof of the serpent lemma in an abelian category A.

Serpent Lemma Given a commutative diagram

![](images/page_62_image_0.jpg)

Then there exists an exact sequence

$$
\operatorname{Ker} u ^ {\prime} \longrightarrow \operatorname{Ker} u \longrightarrow \operatorname{Ker} u ^ {\prime \prime} \stackrel {\delta} {\longrightarrow} \operatorname{Cok} u ^ {\prime} \longrightarrow \operatorname{Cok} u \longrightarrow \operatorname{Cok} u ^ {\prime \prime}.
$$

The interesting part of the proof is the construction of  $\delta$ , which we next discuss.

Take the pull back

![](images/page_62_image_5.jpg)

and by the usual diagram chase, we get a map

$$
A \times_ {A ^ {\prime \prime}} \operatorname{Ker} u ^ {\prime \prime} \xrightarrow {\partial} \operatorname{Cok} u ^ {\prime}.
$$

Now, $\operatorname{Ker} u'' = \operatorname{Coker} (\operatorname{Ker} \xi \to A \times_{A''} \operatorname{Ker} u'')$ so by the remark before the general principle above, to get $\delta : \operatorname{Ker} u'' \to \operatorname{Cok} u'$ it suffices to check that $\operatorname{Ker} \xi$ maps to zero under $\partial$. To see this, let $C = \operatorname{Ker} (A \to A'')$ and note that a diagram chase gives $A \times_{A''} \operatorname{Ker} u'' \to C$. Take the pull back

![](images/page_62_image_9.jpg)

Thus given  $x \in \operatorname{Ker} \xi$ , pull back to  $y \in A' \times_{c} \operatorname{Ker} \xi$ . Then  $u' \circ \alpha(y)$  is the coset of  $\partial(x)$ , i.e.,  $\partial(\operatorname{Ker} \xi) = 0$ , as desired.

Exercise Finish the proof of the serpent lemma.

Suppose that $f: \mathcal{C} \to \mathcal{C}'$ is a functor and $Y$ is an object in $\mathcal{C}'$. Then we have already discussed the following categories:

(1) the fiber $f^{-1}Y$ of $f$ over $Y$ is the subcategory of $\mathcal{C}$ where arrows lie over $\mathrm{id}_Y$;  
(2) the left fiber $f / Y$ over $Y$ whose objects are $(X, u)$, where $X \in \operatorname{Ob} \mathcal{C}$ and $u: f(X) \to Y$, and a map $(X, u) \to (X', u')$ is given by maps $X \xrightarrow{v} X'$ so that the diagram

![](images/page_63_image_2.jpg)

commutes;

(3) the right fiber  $Y \setminus f$  consists of  $(X, u : Y \to f(X))$ .

With $\widehat{C} = \operatorname{Funct}(\mathcal{C},\text{Sets})$, for $\mathcal{C}$ small, $f$ induces $f^{*}:\widehat{\mathcal{C}}^{\prime}\to \widehat{\mathcal{C}},G\mapsto G\circ f$.

Proposition We have adjoint functors

![](images/page_63_image_7.jpg)

that is,

(i)  $\operatorname{Hom}(f_{!}F,G)=\operatorname{Hom}(F,f^{*}G),$

(ii)  $\operatorname{Hom}(G, f_{*}F) = \operatorname{Hom}(f^{*}G, F),$

given by Kan's formulae

$$
f _ {!} (F) (Y) \underset {X, f X \rightarrow Y \in f / Y} {\lim} F (X),
$$

$$
f _ {*} (F) (Y) = \varprojlim_ {X, Y \rightarrow f X \in Y \setminus f} F (X).
$$

Proof (i) Start with  $\theta: F \rightarrow f^{*}G$ ,

$$
\theta = (\theta_ {X}: F (X) \rightarrow G (f X)).
$$

Let $\mathcal{M}(f) = \mathcal{C} \times_{\mathcal{C}'} \operatorname{Arr} \mathcal{C}'$, where $\operatorname{Arr} \mathcal{C}'$ are the arrows (that is, the morphisms) in $\mathcal{C}'$, denote the category whose objects are given by pairs $(X, u : fX \to Y)$ and whose maps $(X, u) \to (X', u')$ are a pair $X \xrightarrow{a} X'$ and $Y \xrightarrow{b} Y'$ so that

$$
\begin{array}{l} f (X) \xrightarrow {u} Y \\ \Biggl \downarrow_ {f (a)} \qquad \qquad \qquad \Biggl \downarrow_ {b} \\ f (X ^ {\prime}) \xrightarrow {u ^ {\prime}} Y ^ {\prime} \end{array} \quad \text { commutes. }
$$

Given $(X, u: f(X) \to Y)$ in $\mathcal{M}(f)$, we define

$$
\theta_ {(X, u)}: F (X) \xrightarrow {\theta_ {X}} G (f X) \xrightarrow {G (u)} G (Y).
$$

Thus $\theta = (\theta_X)$ gives a family of maps $F(X) \to G(Y)$, for each $(X, u)$, which are natural with respect to maps in $\mathcal{M}(f)$.

Now fix Y. Then the maps  $\theta_{(X,u)}$  induce a map

![](images/page_64_image_10.jpg)

i.e., induce a map $f_{!}F(Y) \to G(Y)$. We check easily that this gives a natural transformation $f_{!}F \to G$.

It is clear that the following gadgets are the same:

(1) a natural transformation $\theta : F \to f^{*}G$ over $\mathcal{C}$,

(2) a natural transformation $F(X) \to G(Y)$ over $\mathcal{M}(f)$,

(3) a natural transformation $f_{!}F(Y)\to G(Y)$ over $C'$.

Therefore,

$$
\operatorname{Hom} (F, f ^ {*} G) = \operatorname{Hom} (f _ {!} F, G).
$$

The proof of (ii) is exactly dual.

□

Fibered Category [due to Grothendieck]

Example Let $\mathcal{B}$ be the category of topological spaces. For each $X \in \mathrm{Ob} \mathcal{B}$, we let $\mathcal{E}_X$ be the category of spaces over $X$ i.e., pairs $E$, $p: E \to X$ in $\mathcal{B}$. This is denoted $\mathcal{B}/X$. Now, if $u: X \to X'$ is a map in $\mathcal{B}$, we have a pull back functor $u^*: \mathcal{E}_{X'} \to \mathcal{E}_X$

$$
\left( \begin{array}{c} E \\ \downarrow \\ X ^ {\prime} \end{array} \right) \longmapsto \left( \begin{array}{c c} X \times_ {X ^ {\prime}} E \\ \downarrow \\ X \end{array} \right).
$$

Given  $Z \stackrel{v}{\rightarrow} Y \stackrel{u}{\rightarrow} X$  in B, we have a canonical isomorphism

$$
Z \times_ {Y} (Y \times_ {X} E) \simeq Z \times_ {X} E
$$

given by  $c_{u,v}:v^{*}u^{*}\xrightarrow{\sim}(uv)^{*}$ .

We have the following (cocycle) condition

$$
\begin{array}{c} w ^ {*} v ^ {*} u ^ {*} \xrightarrow {w ^ {*} (c _ {u , v})} w ^ {*} (u v) ^ {*} \\ \Biggl \downarrow (c _ {v, w}) u ^ {*} \qquad \qquad \qquad \qquad \qquad \qquad \Biggl \downarrow c _ {u v, w} \\ (v w) ^ {*} u ^ {*} \xrightarrow {c _ {u , v w}} (u v w) ^ {*} \end{array}
$$

where the diagram commutes.

First definition of fibered category over a category $\mathcal{B}$: It is a pseudo-functor from $\mathcal{B}^{\mathrm{op}}$ to the category Cat of categories. Namely, a way of assigning a category $\mathcal{E}_X$ to each $X\in \mathrm{Ob}\mathcal{B}$, to each arrow $u:Y\to X$ a functors $u^{*}:\mathcal{E}_{X}\to \mathcal{E}_{Y}$ and to each pair $Z\xrightarrow{v}Y\xrightarrow{u}X$ in $\mathcal{B}$ an isomorphism of functors $c_{u,v}:v^{*}u^{*}\xrightarrow{\sim}(uv)^{*}$ so that the cocycle condition holds. Note that a functor from $\mathcal{B}$ to Cat is a pseudo-functor so that $c_{u,v}$ is the identity.

New definition of fibered category: Suppose we have a functor $p: \mathcal{E} \to \mathcal{B}$. If $X \in \operatorname{Ob} \mathcal{B}$, then let $\mathcal{E}_X$ denote the fiber $p^{-1}X$. Let $E' \xrightarrow{f} E$ be a morphism in $\mathcal{E}$ lying over $X' \xrightarrow{u} X$, i.e., $p(E') = X'$, $p(E) = X$ and $p(f) = u$. We say that $f$ is cartesian provided that for any $F \in \operatorname{Ob} \mathcal{E}_{X'}$, we have the isomorphism

$$
\begin{array}{c} \operatorname{Hom} _ {\mathcal {E} _ {X ^ {\prime}}} (F, E ^ {\prime}) \stackrel {{\sim}} {{\longrightarrow}} \{g \in \operatorname{Hom} _ {\mathcal {E}} (F, E): p (g) = u \} \\ \alpha \longmapsto f \alpha . \end{array}
$$

Given $p: \mathcal{E} \to \mathcal{B}$, we say $\mathcal{E}$ is a pre-fibered category over $\mathcal{B}$ if given any $u: X' \to X$ in $\mathcal{B}$ and object $E \in \mathcal{E}_X$, there exists a cartesian arrow $E' \to E$ lying

over u. A fibered category is a pre-fibered category in which the composition of two cartesian arrows is again cartesian.

Suppose $p: \mathcal{E} \to \mathcal{B}$ is pre-fibered. Then given any $u: X' \to X$, we get a functor $u^*: \mathcal{E}_X \to \mathcal{E}_{X'}$ by choosing for each $E \in \mathcal{E}_X$ a cartesian arrow $E' \to E$ over $u$ and setting $u^*E = E'$. Then

$$
\operatorname{Hom} _ {\mathcal {E} _ {X ^ {\prime}}} (f, u ^ {*} E) \simeq \{g: F \rightarrow E: p (g) = u \},
$$

$$
\operatorname{Hom} _ {\mathcal {E}} (F, E) _ {u} \stackrel {{d}} {{=}} \left\{g: F \rightarrow E: p (g) = u \right\},
$$

and then for all $F$ over $X'$,

$$
\operatorname{Hom} _ {\mathcal {E} _ {X ^ {\prime}}} (F, u ^ {*} E) \stackrel {{\sim}} {{\longrightarrow}} \operatorname{Hom} _ {\mathcal {E}} (F, E) _ {u}.
$$

Therefore  $u^{*}E$  is unique up to canonical isomorphism.

If  $X'' \stackrel{v}{\longrightarrow} X' \stackrel{u}{\longrightarrow} X$ , then there is a canonical arrow

$$
v ^ {*} u ^ {*} \longrightarrow (u v) ^ {*},
$$

and we can check it satisfies the co-cycle condition and is an isomorphism $\mathcal{E} \to \mathcal{B}$ in a fibered category. This indicates that the two definitions are the same.

Dual Notions $p: \mathcal{E} \to \mathcal{B}$ is pre-cofibered when for every $u: X \to Y$ in $\mathcal{B}$ we have a functor $u_{*}: \mathcal{E}_{X} \to \mathcal{E}_{Y}$ so that

$$
\operatorname{Hom} _ {\mathcal {E} _ {Y}} (u _ {*} E, F) \simeq \operatorname{Hom} _ {\mathcal {E}} (E, F) _ {u}.
$$

Cofibered means pre-cofibered and composition of co-cartesian is co-cartesian.

Now go back to $f: \mathcal{C} \to \mathcal{C}'$ with $Y$ and object in $\mathcal{C}'$ where

$$
f _ {!} (F) (Y) = \varinjlim_ {(X, u: f X \rightarrow Y) \in f \backslash Y} F (X).
$$

Claim 12.1 If $f$ is pre-cofibered, then

$$
f _ {!} (F) (Y) = \varinjlim_ {X \in f ^ {- 1} Y} F (X).
$$

Moreover,

$$
f _ {*} (F) (Y) = \underset {\left(X, Y \xrightarrow {u} f X\right) \in Y \setminus f} {\lim} F (X).
$$

Claim 12.2 If $f$ is pre-fibered, then

$$
f _ {*} (F) (Y) = \varprojlim_ {X \in f ^ {- 1} Y} F (X).
$$

Exercise Prove the two claims.

## Chapter 13 Examples of Fibered Categories

In a pre-cofibered category $\mathcal{C} \xrightarrow{f} \mathcal{C}$, we have maps

$$
\begin{array}{l} i: f ^ {- 1} Y \hookrightarrow f / Y \\ : E \longmapsto \binom {E} {f E \stackrel {\mathrm{id}} {=} Y} \end{array}
$$

and

$$
\begin{array}{r l} r & : f / Y \longrightarrow f ^ {- 1} Y \\ & : \binom {X} {f X \stackrel {u} {\to} Y} \longmapsto u _ {*} X, \end{array}
$$

and it is clear that  $ri = id_{f^{-1}Y}$ .

Claim That r is left adjoint to i.

Proof

$$
\begin{array}{l} \operatorname{Hom} _ {f / Y} \left(\binom {X} {f X \xrightarrow {u} Y}, \binom {E} {f E = Y}\right) \\ = \operatorname{Hom} _ {\mathcal {C}} (X, E) _ {u} \text { by   definition } \\ = \operatorname{Hom} _ {f ^ {- 1} Y} (u _ {*} X, E) \text { by   the   universal   property   of } u _ {*} X. \end{array}
$$

Exercise Check that $f$ is pre-cofibered if and only if $f^{-1}Y \hookrightarrow f/Y$ has a left adjoint for all $Y \in \mathcal{C}'$.

Claim

$$
\lim _ {\stackrel {\rightarrow} {(X, f X \stackrel {u} {\rightarrow} Y)}} F (X) = \lim _ {X \in f ^ {- 1} Y} F X.
$$

Proof Consider  $A \xrightarrow[i]{r} B$  with  $ri = id_{A}$  and r a left adjoint to i, so there is a natural transformation  $id_{B} \to ir$ , and suppose  $B \xrightarrow{F}$  Sets. We show

$$
\varinjlim_ {B \in \mathcal {B}} F (B) = \varinjlim_ {A \in \mathcal {A}} F (i A).
$$

We have a canonical map $\lim_{A\in\mathcal{A}}F(iA)\to\lim_{B\in\mathcal{B}}F(B)$, and using the universal property of $\lim_{\rightarrow}$, we have to show that

$$
\varprojlim_ {B \in \mathcal {B}} \operatorname{Hom} _ {\text { Sets }} (F (B), S) \xrightarrow {\sim} \varprojlim_ {A \in \mathcal {A}} \operatorname{Hom} _ {\text { Sets }} (F (i A), S).
$$

Then $G(B) = \operatorname{Hom}_{\text{Sets}}(F(B), S)$ is a contravariant functor, and we want to prove

$$
\varprojlim_ {B \in \mathcal {B}} G (B) \stackrel {{\sim}} {{\longrightarrow}} \varinjlim_ {A \in \mathcal {A}} G (i A).\tag{*}
$$

An element of the left-hand side is a family  $g_{B} \in G(B)$  compatible with the arrows in B. That the map in (\*) is an isomorphism follows from the picture

![](images/page_69_image_9.jpg)

□

Example 13.1 For $\mathcal{A} \stackrel{i}{\hookrightarrow} \mathcal{B}$, $i$ has a left adjoint if and only if $i(\text{point}) = e \in \mathcal{B}$ is a final object for $\mathcal{B}$. Then the claim says $\lim_{\substack{\text{point}\\ }} F(B) = F(e)$ for $F: \mathcal{B} \to \text{Sets}$.

Example 13.2 This is false for contravariant functors, e.g., take

![](images/page_70_image_1.jpg)

Then  $\lim_{\rightarrow} F = F(a) \coprod_{F(e)} F(b) \neq F(e)$ .

Example 13.3 A discrete category has all morphisms identity morphisms, so the arrows comprise a set. Suppose $\mathcal{E} \xrightarrow{p} \mathcal{B}$ is a fibered category so that the fibers are discrete for each $X$ in $\mathcal{B}$. We get, then, a contravariant functor $\mathcal{B}^{\mathrm{op}} \to \mathrm{Sets}$, $B \mapsto \mathrm{Ob} \mathcal{E}_X$, that is, a pseudo-functor is in fact a functor in a discrete category.

Conversely, given any functor $F: \mathcal{B}^{\mathrm{op}} \to \text{Sets}$, we can form the category $\mathcal{B}/F$ whose objects are $(X, \xi)$, $X \in \operatorname{Ob}(\mathcal{B})$, $\xi \in F(X)$, and

$$
\begin{array}{c} p: \mathcal {B} / F \longrightarrow \mathcal {B} \\ (X, \xi) \longmapsto X \end{array}
$$

is a fibered category with discrete fibers. The fiber over X is the set  $F(X)$  regarded as a discrete category.

Note that

$$
\operatorname{Hom} _ {\mathcal {B} / F} ((X, \xi), (Y, \eta)) = \{f: X \to Y: F (f) \eta = \xi \},
$$

and in B/F every arrow is cartesian.

Thus fibered categories over C with discrete fibers are the same as  $F : C^{op} \rightarrow Sets$ , and cofibered categories over C with discrete fibers are the same as  $F : C \rightarrow Sets$ .

Example 13.4 Suppose $U \xrightarrow{p} G$ is a group homomorphism and consider $p: \widetilde{U} \to \widetilde{G}$. If this is fibered, then $p$ must be epic, and every arrow is cartesian by unique cancellation. Thus $\widetilde{U} \to \widetilde{G}$ is a fibered category if and only if $U \to G$ is epic, and the fiber over the unique object of $\widetilde{G}$ is the category $\widetilde{K}$ where $K$ is $\operatorname{Ker}\{p: U \to G\}$.

In general, given a fibered category $p: \mathcal{E} \to \mathcal{B}$, we can define for each $u: X \to Y$ in $\mathcal{B}$ a functor $u^{*}: \mathcal{E}_{Y} \to \mathcal{E}_{X}$, unique up to canonical isomorphism.

In the case of  $\vec{U} \rightarrow \vec{G}$ , such a choice is the same as a set-theoretic section of U over G. Check that the canonical isomorphisms

$$
(u v) ^ {*} \stackrel {\sim} {\longleftarrow} v ^ {*} u ^ {*}
$$

are the same thing as the 2-cocycle describing $U$ as a group extension.

Example 13.5 Let $f: X \to Y$ be a simplicial map of simplicial complexes. Take $\mathcal{C}$ to be the simplexes in $X$ and $\mathcal{C}'$ to be the simplexes in $Y$ as posets and let $f: \mathcal{C} \to \mathcal{C}'$ be the induced map of posets.

If $\sigma$ is a simplex in $Y$, then what is $f / \sigma$? $f / \sigma$ is the poset of simplices in the subcomplex $f^{-1}\overline{\sigma}$. Is $f: \mathcal{C} \to \mathcal{C}'$ fibered? We have

$$
\begin{array}{c} u ^ {*} T \subset T \\ \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \sigma^ {\prime} \subset \sigma \\ u \end{array}
$$

So $u^{*}T$ is the face of $T$ whose vertices lie over vertices $\sigma'$. So yes it is fibered but not cofibered.

Furthermore,  $f^{-1}\sigma$  is the poset of all simplexes mapping onto  $\sigma$, and this is interesting because  $f^{-1}$  (open simplex  $\sigma$) is homeomorphic to  $f^{-1}(\xi) \times \sigma$, where  $\xi \in Int\sigma$. So  $f^{-1}\xi$  is not a simplicial complex, but it is a union of contractible pieces whose inclusion relations are described by the poset  $f^{-1}\sigma$.

Suppose $\mathcal{A} \xrightarrow{F} \mathcal{B}$ is a functor between abelian categories. $F$ is an additive functor if $\operatorname{Hom}_{\mathcal{A}}(A, A') \to \operatorname{Hom}_{\mathcal{B}}(FA, FA')$ is a homomorphism of abelian groups.

Example 14.1 $\mathcal{A} = \operatorname{Funct}(\mathcal{C},\mathrm{Ab}),\mathcal{B} = \mathrm{Ab}$, with $F = \varinjlim_{\mathcal{C}}$ that is,

$$
F (A) = \varinjlim_ {X \in \mathcal {C}} A (X).
$$

Example 14.2 $\mathcal{A} = G$-mod, $\mathcal{B} = \mathrm{Ab}$, and

$$
F (M) = \mathbb {Z} \otimes_ {\mathbb {Z} [ G ]} M,
$$

i.e., the largest quotient on which G acts trivially.

An object $P$ of an abelian category $\mathcal{A}$ is projective (respectively injective) if $\operatorname{Hom}_{\mathcal{A}}(P,\cdot):\mathcal{A}\to\operatorname{Ab}$ is exact (respectively $\operatorname{Hom}_{\mathcal{A}}(\cdot,P):\mathcal{A}^{\mathrm{op}}\to\operatorname{Ab}$ is exact).

In general, given  $0 \rightarrow A' \rightarrow A \rightarrow A'' \rightarrow 0$  exact in A, we know that for any  $P \in A$  we have

$$
0 \longrightarrow \operatorname{Hom} (P, A ^ {\prime}) \longrightarrow \operatorname{Hom} (P, A) \longrightarrow \operatorname{Hom} (P, A ^ {\prime \prime}) \text {   exact.   }
$$

So P is projective if and only if  $\operatorname{Hom}(P, \cdot)$  carries epic maps to epic maps.

Similarly, $P$ is injective if and only if $\operatorname{Hom}_{\mathcal{A}}(\cdot, P)$ carries monic maps to epic maps.

If $P$ is projective and we have an epic $A \to P$, then $\operatorname{Hom}(P, A) \twoheadrightarrow \operatorname{Hom}(P, P)$, so there exists $\alpha \mapsto \operatorname{id}_P$ so that $P$ is a direct summand of $A$ and conversely, and therefore $P$ is projective if and only if every $A \twoheadrightarrow P$ has a section.

Thus an R-module P is projective in the category of R-modules if and only if it is a direct summand in a free R-module.

Suppose $\mathcal{A}$ is an abelian category. A complex in $\mathcal{A}$ is a diagram

$$
\dots \stackrel {d} {\longrightarrow} A _ {n + 1} \stackrel {d} {\longrightarrow} A _ {n} \stackrel {d} {\longrightarrow} A _ {n - 1} \stackrel {d} {\longrightarrow} \dots ,\tag{*}
$$

for  $n \in Z$ , so that  $d^{2} = 0$ .

The complexes in A form a category in the obvious way called  $C(\mathcal{A})$ , and  $C(\mathcal{A})$  is an abelian category. A. is the notation for a complex,

$$
\operatorname{Ker} \{A. \longrightarrow B. \} _ {n} = \operatorname{Ker} \{A _ {n} \longrightarrow B _ {n} \}
$$

and so on.

Now (\*) can also be written

$$
\dots \xrightarrow {d} A ^ {n} \xrightarrow {d} A ^ {n + 1} \xrightarrow {d} \dots
$$

where $A^n = A_{-n}$, and we define

$$
\begin{array}{r l} C _ {\geq 0} (\mathcal {A}) & = \text { category   of   chain   complexes } \\ & = \{A. \text { so   that } A _ {n} = 0, n <   0 \}, \end{array}
$$

$$
C _ {\leq 0} (\mathcal {A}) = C ^ {\geq 0} (\mathcal {A}) = \text { category   of   co - chain   complexes },
$$

$$
C ^ {+} (\mathcal {A}) = \text { category   of   complexes   with } A ^ {n} = 0, n <   <   0,
$$

$$
C ^ {-} (\mathcal {A}) = \text { category   of   complexes   with } A ^ {n} = 0, n > > 0.
$$

Homology and cohomology are defined as usual.

Suppose we have $f, g: A. \to B$. Then a homotopy between $f$ and $g$ is

$$
h = \{h _ {n}: A _ {n} \rightarrow B _ {n + 1} \}
$$

so that

$$
f - g = d h + h d.
$$

Proposition Homotopic maps induce the same maps on homology.

The proof is standard and left as an exercise.

Homotopy is an equivalence relation on $\mathrm{Hom}_{\mathcal{C}(\mathcal{A})}(A., B.)$, so we can form the abelian group of homotopy classes $[A., B.]$.

Denote $K(\mathcal{A}) =$ category with the same objects as $C(\mathcal{A})$, but in which

$$
\operatorname{Hom} _ {K (\mathcal {A})} (A., B.) = [ A., B. ],
$$

and define  $K^{+}$ ,  $K^{-}$ as before. Note that the notion of isomorphism in  $K(\mathcal{A})$ , namely homotopy equivalence, is too strong.

A quasi-isomorphism of complexes, or sometimes simply quis for short, is a map $A. \to B$. in $C(\mathcal{A})$ which induces a homology isomorphism.

Example A homotopy equivalence $f: A \to B$ is a quis.

Given $M \in \text{ObA}$, a (left) resolution of $M$ is an exact sequence of the form

$$
\dots \longrightarrow A _ {1} \longrightarrow A _ {0} \longrightarrow M \longrightarrow 0.
$$

A projective resolution is a resolution so that each  $A_{i}$  is projective.

Key Proposition Any two projective resolutions of M are homotopy equivalent, and this assignment of projective resolution is functorial in M up to homotopy.

Again the proof is an exercise.

Think of M as being a complex concentrated in degree 0 and a resolution of M as being a chain complex A, equipped with a quasi-isomorphism

![](images/page_74_image_7.jpg)

Let $\mathcal{P}$ be the full subcategory of $\mathcal{A}$ consisting of projectives, where a subcategory $\mathcal{B}$ of $\mathcal{A}$ is full if for any two of its objects $A, B \in \mathcal{B}$, we have $\operatorname{Hom}_{\mathcal{B}}(A, B) = \operatorname{Hom}_{\mathcal{A}}(A, B)$. $\mathcal{P}$ is an additive category, so it makes sense to talk about $C_{+}(\mathcal{P})$, $K(\mathcal{P})$, etc.

Define  $K(\mathcal{P})$  to be the full subcategory of  $K(\mathcal{A})$  consisting of complexes made up of projectives. A (left) resolution of a complex M. is another complex A. together with a quis  $A. \rightarrow M.$ , and a projective resolution is a resolution  $A. \in C(\mathcal{P})$ .

Proposition Provided we stay in  $K_{+}(\mathcal{A})$ , i.e., bounded above, any two projective resolutions of M. are isomorphic in  $K_{+}(\mathcal{P})$ . Moreover, by choosing for each M a projective resolution  $P. \rightarrow M$ , we get a well-defined functor  $K_{+}(\mathcal{A}) \rightarrow K_{+}(\mathcal{P})$ , and this is adjoint to inclusion, where  $M. \mapsto P$ .

Proof (of the simplest case) Given

![](images/page_74_image_12.jpg)

where successive horizontal arrows compose to zero, the  $P_{i}$ 's are projective and the bottom sequence is exact, there exist  $u_{0}, u_{1}, u_{2}, \ldots$  making the diagram commute, and the map of complexes is unique up to homotopy.

A diagram chase gives $u: M. \to P$. as usual. Suppose we extend $u$ also to $u'$, and consider $u - u' = \widetilde{u}$. Then we have

$$
\begin{array}{c} P _ {2} \longrightarrow P _ {1} \longrightarrow P _ {0} \longrightarrow M \longrightarrow 0 \\ \Biggl \downarrow \tilde {u} _ {2} \qquad \Biggl \downarrow \tilde {u} _ {1} \nearrow h _ {0} \Biggl \downarrow \tilde {u} _ {0} \qquad \Biggl \downarrow 0 \\ A _ {2} \longrightarrow A _ {1} \longrightarrow A _ {0} \longrightarrow N \longrightarrow 0. \end{array}
$$

Now  $\widetilde{u}_{0}=dh_{0}$  and  $d(\widetilde{u}_{1}-h_{0}d)=0$ , so we find  $h_{1}$  with  $\widetilde{u}_{1}-h_{0}d=dh_{1}$ , and so on. This proves the simplest case.

Why are two projective resolutions $P \to M, Q \to M$ homotopy equivalent? Use the simplest case to get

![](images/page_75_image_3.jpg)

Then

![](images/page_75_image_5.jpg)

so $v.u. \simeq id_{M}$ and similarly for $u.v.$.

□

At this point, we have a functor well defined up to canonical isomorphism given by

$$
\begin{array}{l} \mathcal {A} \longrightarrow K _ {\geq 0} (\mathcal {P}) \\ M \longmapsto \text {   projective   resolution   of   } M. \end{array}
$$

Important We must assume that $\mathcal{A}$ has enough projectives, i.e., any $M \in \mathrm{Ob} \mathcal{A}$ is the quotient of some projective $P$. Then we construct projective resolutions

$$
\dots \longrightarrow P _ {1} \longrightarrow P _ {0} \longrightarrow M \longrightarrow 0.
$$

Example The category A of finite abelian p-groups does not have enough projectives (or injectives) since

$$
A = \mathbb {Z} / p ^ {r} \mathbb {Z} \times \dots \text {   for   } A \in \mathcal {A}
$$

is not projective. Note that  $Z/p^{r+1}Z \twoheadrightarrow Z/p^{r}Z$  is epic yet there is no section.

# Chapter 15 Analogues of Homotopy Liftings

Recall last time we constructed  $\cdots\rightarrow P_{1}\rightarrow P_{0}\rightarrow M\rightarrow0$ , which is the same as a quis

![](images/page_76_image_2.jpg)

Let

$\mathcal{A} =$ abelian category with enough projectives,

$\mathcal{P} =$ full subcategory of projectives.

Suppose given a complex $A. \in C_{+}\mathcal{A}$; we want to construct a complex and an epimorphism

$$
P _ {\cdot} \longrightarrow A _ {\cdot}
$$

which is a quasi-isomorphism with  $P. \in C_{+}(\mathcal{P})$ .

Without loss of generality, A. is so that  $A_{n}=0$  for all n<0. Choose  $P_{0}\twoheadrightarrow A_{0}$  and consider the diagram

![](images/page_77_image_0.jpg)

Apply the Serpent Lemma to the first two columns to get  $K_{1} \twoheadrightarrow K_{0}$ . So far, this gives

![](images/page_77_image_2.jpg)

Put

$$
\begin{array}{l}K _ {1 0} = \operatorname{Ker} \{K _ {1} \rightarrow K _ {0} \},\\P _ {1 0} = \operatorname{Ker} \{P _ {1} \rightarrow P _ {0} \},\\A _ {1 0} = \operatorname{Ker} \{A _ {1} \rightarrow A _ {0} \}.\end{array}
$$

The Serpent Lemma gives the commutative diagram

![](images/page_78_image_0.jpg)

with exact verticals. Apply the Serpent Lemma again to get  $K_{2} \twoheadrightarrow K_{10}$ .

Iterate to get a diagram with exact verticals

![](images/page_78_image_3.jpg)

so that $K$. has trivial homology, whence $H_{*}P. \simeq H_{*}A$, so $P. \to A$. is indeed a quis. Another construction: given $A. \in C_{+}(\mathcal{A})$, we can find a $P. \twoheadrightarrow A$. so that $P. \in C_{+}(\mathcal{P})$ and $P$. is acyclic

![](images/page_79_image_0.jpg)

Incidentally, any $P. \in C_{+}\mathcal{P}$ with $P$. acyclic looks this way. To see this, consider

$$
P _ {1} \xrightarrow {} P _ {0} \longrightarrow 0
$$

so $P_{1} \approx P_{10} \oplus P_{0}$ and so on.

The next step using either construction is to show that two projective resolutions of $A \in C_{+}(\mathcal{A})$ are homotopy equivalent and to prove functoriality in $\mathcal{A}$.

Recall,

Homotopy Extension (HE) Theorem: Suppose given CW complexes $A$ and $B$, maps

![](images/page_79_image_7.jpg)

and a homotopy $h: A \times I \to E$ so that $h_0 = f i$. Then there exists an extension $\widehat{h}: B \times I \to E$ so that $\widehat{h} = h$ on $A \times I$ and $\widehat{h}_0 = f$, i.e., a lift $--\to$ making the diagram commute

![](images/page_79_image_9.jpg)

or in other words

![](images/page_80_image_0.jpg)

evaluation at 0

Chain Homotopy (CH) Theorem: Suppose given a fiber space E with

![](images/page_80_image_3.jpg)

so that

![](images/page_80_image_5.jpg)

E are fibrations in the sense of Serre, and

![](images/page_80_image_7.jpg)

are inclusions of CW complexes.

Then each of the following is a homotopy equivalence

![](images/page_80_image_10.jpg)

Chain Homotopy Extension (CHE) Theorem: Given

$$
\begin{array}{c} A \longrightarrow E \\ C W \Biggl \downarrow i \quad \nearrow \quad \Biggl \downarrow \\ B \longrightarrow X \end{array} \text {   a   fibration   in   the   sense   of   Serre   }
$$

If either $i$ or $p$ is a homotopy equivalence, then a lift $\longrightarrow$ exists making the diagram commute.

By analogy, we have

Proposition Suppose given in $C_{+}(\mathcal{A})$ a diagram

$$
\begin{array}{c} A. \xrightarrow {f} E. \\ \Biggl \downarrow_ {i} \quad \Biggl \downarrow_ {p} \\ B. \xrightarrow {g} X. \end{array}
$$

with $p$ epic in each dimension, $i$ monic in each dimension, $B / A \in C_{+}(\mathcal{P})$ and either $i$ or $p$ a quis. Then there exists a lift $-\rightarrow$ making the diagram commute.

Proof Suppose first that $p$ is quis

![](images/page_81_image_5.jpg)

Let $SK_{n}(B, A)$ be the complex

$$
\dots \longrightarrow A _ {n + 1} \longrightarrow A _ {n} \longrightarrow B _ {n - 1} \longrightarrow B _ {n - 2} \longrightarrow \dots
$$

Then

$$
A. = S K _ {0} (B, A) \subset S K _ {1} (B, A) \subset \dots \subset S K _ {n} (B, A) \subset \dots \subset B.
$$

are all subcomplexes. Moreover

$$
S K _ {n + 1} (B, A) / S K _ {n} (B, A) = \left\{ \begin{array}{l l} P _ {n}, & \text { in   degree } n, \\ 0, & \text { else }. \end{array} \right.
$$

Thus we have

![](images/page_82_chart_1.jpg)

and have thus reduced the problem to the case where A. and B. differ in one degree by a projective object.

Denote $P[n] =$ complex with $P$ in dimension $n$, and zeroes elsewhere. Because $P$ is projective, $0 \longrightarrow A_n \longrightarrow B_n \xrightarrow{\angle} P_n \longrightarrow 0$ splits, and so

$$
B _ {.} = A _ {.} \oplus P [ n ]
$$

with  $d_{n}(a,p)=da+\theta p$  where  $\theta:P_{n}\to\operatorname{Ker}\{A_{n-1}\to A_{n-2}\}$ . Thus we have

![](images/page_82_image_6.jpg)

Problem: Define $h: P_n \to E_n$ so that

$p_n h = g_n$ on $P$ with

$$
d h = f _ {n - 1} d: A _ {n} \oplus P \rightarrow E _ {n - 1}
$$

![](images/page_83_image_3.jpg)

and h exists because (\*) is epic and P is projective.

Recall the lifting result from last time which we continue discussing: Given

$$
\begin{array}{l} A \xrightarrow {f} E \\ \Biggl \downarrow_ {i} \quad \text {   h   } \quad \Biggl \downarrow_ {p} \\ B \xrightarrow {g} X \end{array} \text {   in   } C _ {+} (\mathcal {A})
$$

with i monic, Coker  $i \in C_{+}(\mathcal{P})$ , p epic and either i or p a quis, then there exists a lifting h making diagram commute.

We did the case where p is a quis last time.

Now suppose $i$ is a quis. Then $\operatorname{Coker} i = (B / A) = P$, and the long exact sequence gives $H_{*}P_{*} = 0$. Since $P_{*} \in C_{+}(\mathcal{P})$, we showed $P_{*}$ is a direct sum of complexes of the form

$$
\dots 0 \longrightarrow 0 \longrightarrow P _ {\deg n} \stackrel {{\text {   }}} {{\longrightarrow}} P _ {\deg n - 1} \longrightarrow 0 \longrightarrow 0 \longrightarrow \dots .
$$

We have the commutative diagram

![](images/page_85_image_0.jpg)

Consider the following special case

![](images/page_85_image_2.jpg)

Then the dotted arrow exists because

$$
\operatorname{Hom} _ {C (\mathcal {A})} \left(\left\{0 \longrightarrow P _ {n} \stackrel {\mathrm{id}} {\longrightarrow} P _ {n - 1} \longrightarrow 0 \right\}, K.\right) = \operatorname{Hom} (P, K _ {n}),
$$

and we have

![](images/page_85_image_6.jpg)

since $P$ is projective. We denote $D_{n}(P) = \left\{0\longrightarrow P\stackrel {\mathrm{id}}{\longrightarrow}P\stackrel {n - 1}{\longrightarrow}0\right\} .$

Returning to the general case, we have

![](images/page_86_image_1.jpg)

where $Q_{n}\in \mathcal{P}$. By the special case, we can lift each $D_{n}(Q_{n})$ so that $*$ exists and so

$$
B \simeq A \oplus \bigoplus_ {n \geq 0} D _ {n} (Q _ {n}).
$$

Finally we have

![](images/page_86_image_5.jpg)

where we construct h by lifting each  $D_{n}(Q_{n})$  by the special case. □

Recall that in homotopy theory we have the mapping cylinder construction, namely, given  $A \xrightarrow{f} B$ , we construct

$$
M (f) = (A \times I) \bigcup_ {A \times 1} B
$$

and have then a factorization of $f$ as follows

$$
A \xrightarrow {i} M (f) \xrightarrow {p} B
$$

with i an embedding and p a homotopy equivalence.

The analogue for complexes: let $A. \in C(\mathcal{A})$, and define $A_{I}$ as follows

$$
(A _ {I}) _ {n} = A _ {n} \oplus A _ {n - 1} \oplus A _ {n}.
$$

Notice that if we were working with modules, then we would like to denote an element of  $(A_{I})_{n}$  by  $(0)\otimes a+(0,1)\otimes b+(1)\otimes c$ , for  $a,c\in A_{n}$  and  $b\in A_{n-1}$ , and then d is given by

$$
\begin{array}{r l} d ((0) \otimes a + (0, 1) \otimes b + (1) \otimes c) \\ & = (0) \otimes d a - (0) \otimes b + (1) \otimes b - (0, 1) \otimes d b + (1) \otimes d c. \end{array}
$$

Back to complexes, the differential  $d:(A_{I})_{n}\to(A_{I})_{n-1}$  is defined as follows

![](images/page_87_image_2.jpg)

i.e.,

$$
d (a, b, c) = (d a - b, - d b, b + d c).
$$

We check

$$
\begin{array}{r l} d ^ {2} (a, b, c) & = d (d a - b, - d b, b + d c) \\ & = (d (d a - b) - (- d b), - d (- d b), - d b + d (b + d c)) \\ & = 0 \end{array}
$$

Proposition To give a map of complexes  $A_{I} \rightarrow B$ . amounts to giving two maps f, g: A. → B. and a homotopy between them, i.e., giving h: f → g so that g - f = dh + hd.

Proof

$$
\begin{array}{c} A _ {n} \oplus A _ {n - 1} \oplus A _ {n} \longrightarrow B _ {n} \\ a \oplus b \oplus c \longmapsto f (a) + h (b) + g (c). \end{array}
$$

Check this is a chain map

$$
\begin{array}{c} (a, b, c) \longmapsto f (a) + h (b) + g (c) \\ \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad d f (a) + d h (b) + d g (c) \\ (d a - b, - d b, b + d c) \longmapsto f (d a - b) - h d b + g b + g d c \end{array}
$$

Now given $f:A.\to B$, a map in $\mathcal{C}(\mathcal{A})$, we define $M(f)$ by push out

![](images/page_88_image_0.jpg)

Therefore

$$
(M (f)) _ {n} = A _ {n} \oplus A _ {n - 1} \oplus B _ {n}
$$

and

$$
d (a, a ^ {\prime}, b) = \left(d a - a ^ {\prime}, - d a ^ {\prime}, f a ^ {\prime} + d b\right).
$$

We have a canonical factorization

$$
A. \xrightarrow {i} M (f) \xrightarrow {p} B.,
$$

that is,

$$
A _ {n} \longrightarrow A _ {n} \oplus A _ {n - 1} \oplus B _ {n} \longrightarrow B _ {n}
$$

given by $i: a \mapsto (a, 0, 0)$ and $p: (a, a', b) \mapsto f(a) + b$, where $i$ is monic, $p$ is epic and

Exercise $p: M(f) \to B$ is a homotopy equivalence.

We can also define  $A^{I}$  so that a map  $B. \rightarrow A^{I}$  is the same as a pair  $f, g: B. \rightarrow A$ . of maps and a homotopy  $h: f \rightarrow g$ . In fact,  $(A^{I})_{n} = A_{n} \times A_{n+1} \times A_{n}$ .

Exercise Find the differential.

Then we can factor $f:B\to A$. into $B\xrightarrow{i}B.\times_{A}A^{I}\xrightarrow{p}A$, where $i$ is monic, $p$ is epic and $i$ is homotopy equivalence.

The mapping cone of  $f: A \rightarrow B$  is given by the quotient

$$
C (f) = M (f) / \text { Image   of } A.
$$

Proposition Let $E.\to X$ be a quis in $C_{+}(\mathcal{A})$ and let $P.\in C_{+}(\mathcal{P})$. Then

$$
[ P., E. ] \stackrel {\sim} {\longrightarrow} [ P., X. ]
$$

is an isomorphism, where  $[\cdot,\cdot]$  denotes homotopy classes.

Proof We factor $E. \to X$. into $E. \xrightarrow{i} \widetilde{E}. \xrightarrow{p} X$, where $p$ is epic and $i$ is a homotopy equivalence as well as being monic. Since $E. \to X$. is a quis, it follows that $p$ is also a quis, and moreover,

$$
i _ {*}: [ P., E. ] \simeq [ P., \widetilde {E} ].
$$

so without loss of generality we assume $E \xrightarrow{p} X$. is an epic quis.

We must show $[P., E.] \to [P., X.]$ is epic, and to this end, given

![](images/page_89_image_2.jpg)

we use the lifting theorem.

To show it is monic, suppose $f, f': P. \to E$. and given a homotopy $h: pf' \to pf$ where $p: E. \to X$, we have the diagram

![](images/page_89_chart_5.jpg)

where  $(i_{0}, i_{1})$  is monic with cokernel in  $C_{+}(\mathcal{P})$ . Use the lifting theorem to conclude that f and  $f'$  are homotopic. □

Note that this Proposition gives uniqueness up to canonical homotopy equivalence of projective resolutions... more next time.

From last time, we saw

Proposition If $P. \in C_{+}(\mathcal{P})$ and $E. \to X$. is a quis in $C_{+}(\mathcal{A})$, then

$$
[ P., E. ] \stackrel {\cong} {\longrightarrow} [ P., X ]
$$

is a natural isomorphism.

Remark Check from the proof that this holds without assuming $E$, $X$, are in $C_{+}(\mathcal{A})$ but just in $C(\mathcal{A})$.

Now, recall that we have $K_{+}(\mathcal{P})$, which has the same objects as $C_{+}(\mathcal{P})$, but the morphisms are homotopy classes of maps of complexes. We have of course $K_{+}(\mathcal{P}) \stackrel{i}{\hookrightarrow} K_{+}(\mathcal{A})$ and claim that $i$ has a right adjoint functor $K_{+}(\mathcal{P}) \xleftarrow{r} K_{+}(\mathcal{A})$ defined by choosing for each $A. \in K_{+}(\mathcal{A})$ a quis $P. \to A.$ with $P. \in C_{+}(\mathcal{P})$ and setting $r(A.) = P..$

Claim that

$$
\begin{array}{c c c} \operatorname{Hom} _ {K _ {+} (\mathcal {P})} (r (Q.), r (A.)) & \cong & \operatorname{Hom} _ {K _ {+} (\mathcal {A})} (i Q., A.) \\ = \uparrow & & = \uparrow \\ [ Q., P. ] & \cong & [ Q., A. ] \end{array}
$$

via the proposition above.

These two functors of $A$ are isomorphic. Thus it follows that $r$ is, in fact, a functor. So we have

$$
K _ {+} (\mathcal {P}) \underset {r} {\overset {i} {\rightleftarrows}} K _ {+} (\mathcal {A}) \text {with} r i = \mathrm{id}.
$$

For any A., the canonical map  $ir(A.) \to A.$  is the quis  $P. \to A.$  which we have chosen.

Let $D_{+}(\mathcal{A})$ be the category with same objects as $C_{+}(\mathcal{A})$, but with morphisms

$$
\operatorname{Hom} _ {D _ {+} (\mathcal {A})} (A., B.) = [ r A., r B. ] \stackrel {{\sim}} {{\longrightarrow}} [ r A., B ].
$$

Then we notice

Proposition We have

$$
\begin{array}{l} K _ {+} (\mathcal {A}) \longrightarrow D _ {+} (\mathcal {A}) \\ [ A., B. ] \longmapsto [ r A., r B. ], \end{array}
$$

and this canonical functor is universal with respect to the property that it sends quasi-isomorphisms into isomorphisms

![](images/page_91_image_9.jpg)

Proof

![](images/page_91_image_11.jpg)

as F carries quasi-isomorphisms to isomorphisms and where the equivalence comes from the fact that the composition gives a clear equivalence of categories.

We want to show that given  $F: K_{+}(\mathcal{A}) \to \mathcal{C}$  inverting the quis, there is a unique way of defining

$$
\begin{array}{c} F _ {*}: \operatorname{Hom} _ {D _ {+} (\mathcal {A})} (A., B.) - - > \operatorname{Hom} (F (A.), F (B)) \\ \Bigg \| \quad \Bigg | \\ [ r A., r B. ] \xmapsto {F _ {*}} \operatorname{Hom} (F r A., F r B.) \end{array}
$$

for  $F(rA.) \stackrel{\sim}{\longrightarrow} F(A.)$  and  $F(rB.) \stackrel{\sim}{\longrightarrow} F(B.)$  since r is quis. Clearly, this will work.

$D_{+}(\mathcal{A})$ is called the derived category of complexes in A bounded below.

$D(\mathcal{A})$ is defined by an analogous universal property from $K(\mathcal{A})$. However, its existence is proved by a process of localization. The idea is to define a map $A. \rightarrow B$ in $D(\mathcal{A})$ to be represented by a diagram

![](images/page_92_image_3.jpg)

where $C$ is projective. Think of this as a fraction of $s$ and then proceed as in the construction of localization for a multiplicative system. Consider a projective resolution

![](images/page_92_image_5.jpg)

Let $F: \mathcal{A} \to \mathcal{B}$ be an additive functor between abelian categories. Then given $M$ in $\mathcal{A}$, assuming $\mathcal{A}$ has enough projectives, choose a projective resolution

$$
\dots \longrightarrow P _ {2} \longrightarrow P _ {1} \longrightarrow P _ {0} \longrightarrow M \longrightarrow 0 \longrightarrow \dots ,
$$

which is unique up to homotopy. Form

$$
F (P _ {.}): \dots \longrightarrow F (P _ {2}) \longrightarrow F (P _ {1}) \longrightarrow F (P _ {0}) \longrightarrow 0 \longrightarrow \dots
$$

and take the homology groups of this chain complex

$$
(L _ {q} F) (M) = H _ {q} (F (P)).
$$

Since P. is unique up to homotopy equivalence and F is additive, the homotopy type of  $F(P)$ , and hence its homology, depends only on M.

$L_{q}$  F is called the  $q^{th}$  left-derived functor of F.

Generalization $F$ induces

$$
\begin{array}{l} C (\mathcal {A}) \longrightarrow C (\mathcal {B}), \\ K (\mathcal {A}) \longrightarrow K (\mathcal {B}). \end{array}
$$

Namely, given $A. \in K_{+}(\mathcal{A})$, we have $rA. \in K_{+}(\mathcal{P})$, and we can define

$$
(\mathbb {L} F): K _ {+} \mathcal {A} \rightarrow D _ {+} \mathcal {B} \text { by } (\mathbb {L} F) (A.) = F (r A.).
$$

This $\mathbb{L}F$ has the property that it inverts quasi-isomorphisms. To see this, note that if

![](images/page_93_image_2.jpg)

then $rA_{\cdot}, rA_{\cdot}^{\prime}$ are homotopy equivalent complexes, so $\mathbb{L}F(A_{\cdot}) \to \mathbb{L}F(A_{\cdot}^{\prime})$ is a homotopy equivalence, hence an isomorphism in $D_{+}(\mathcal{B})$. Thus $\mathbb{L}F$ can be viewed as a functor $\mathbb{L}F: D_{+}(\mathcal{A}) \to D_{+}(\mathcal{B})$.

By definition, if $M \in \operatorname{Ob} \mathcal{A}$, then $\mathbb{L} F(M[0]) \in D_{+}(\mathcal{B})$ is an object which is well defined up to canonical isomorphism with

$$
H _ {q} (\mathbb {L} F (M [ 0 ])) = (L _ {q} F) (M).
$$

Properties of $\{L_q F\}$

1: Long exact sequence: Given  $0 \rightarrow M' \rightarrow M \rightarrow M'' \rightarrow 0$  exact in A, we get a long exact sequence of derived functors

$$
\longrightarrow (L _ {1} F) M ^ {\prime \prime} \longrightarrow (L _ {0} F) (M ^ {\prime}) \longrightarrow (L _ {0} F) (M) \longrightarrow (L _ {0} F) (M ^ {\prime \prime}) \longrightarrow 0.
$$

2:  $(L_{q} F)(P) = 0$  for q > 0 if P is projective.

3: There is a canonical map $F \to L$. $F$ which is an isomorphism if and only if $F$ is right exact, that is, $0 \to M' \to M \to M'' \to 0$ exact implies that $F(M') \to F(M) \to F(M'') \to 0$ is also exact.

Proof of 2 If P is projective, then a projective resolution is

$$
\longrightarrow 0 _ {2} \longrightarrow 0 _ {1} \longrightarrow P _ {0} \stackrel {\mathrm{id}} {\longrightarrow} P \longrightarrow 0
$$

SO

$$
(L _ {q} F) (P) = H _ {q} (F (P [ 0 ])) = \left\{ \begin{array}{c c} F (P) & q = 0, \\ 0 & q \neq 0. \end{array} \right.
$$

Note that Property 3 implies that Property 1 implies that  $L_{0} F$  is right exact, for if  $\cdots \rightarrow P_{1} \rightarrow P_{0} \rightarrow M \rightarrow 0$  is exact, then  $\cdots \rightarrow F(P_{1}) \rightarrow F(P_{0}) \rightarrow F(M) \rightarrow 0$  is not necessarily exact, but  $L_{0} F(M) = H_{0}(F(P)) \rightarrow F(M)$ .

Lemma The following are equivalent conditions on $F$

(a) $0 \to M' \to M \to M'' \to 0$ exact implies $F(M') \to F(M) \to F(M'') \to 0$ exact;

(b) $M^{\prime}\to M\to M^{\prime \prime}\to 0$ exact implies $F(M^{\prime})\rightarrow F(M)\rightarrow F(M^{\prime \prime})\rightarrow 0$ exact.

Proof (b) obviously implies (a). Conversely, given (a) and  $N' \stackrel{u}{\longrightarrow} N \to N'' \to 0$  exact, break it into

$$
0 \rightarrow \operatorname{Im} u \rightarrow N \rightarrow N ^ {\prime \prime} \rightarrow 0 \text {   exact,   }
$$

$$
\text { so } F (\operatorname{Im} u) \to F (N) \to F (N ^ {\prime \prime}) \to 0 \text { exact },
$$

and

$$
0 \rightarrow \operatorname{Ker} u \rightarrow N ^ {\prime} \rightarrow \operatorname{Im} u \rightarrow 0 \text {   exact },
$$

$$
\text { so } F (\operatorname{Ker} u) \to F (N ^ {\prime}) \to F (\operatorname{Im} u) \to 0 \text { exact },
$$

and putting them back together,  $F(N') \rightarrow F(N) \rightarrow F(N'') \rightarrow 0$  is also exact.

Given functors

$$
\mathcal {C} \xrightarrow [ g ]{f} \mathcal {C} ^ {\prime}
$$

between small categories and a suitable natural transformation  $h : f \rightarrow g$ , we want to show that f and g induce the same map on homology. This is the first homotopy property.

Suppose $F$ is a complex of functors $\mathcal{C} \to \mathrm{Ab}$. Then we have $H_{*}(\mathcal{C}, F)$, and for $f: \mathcal{C} \to \mathcal{C}'$ a functor, we have

$$
H _ {*} (\mathcal {C}, F) = H _ {*} (\mathcal {C} ^ {\prime}, \mathbb {L} f _ {!} (F)).
$$

Thus, if we give $\mathbb{L}f_{!}(F)\xrightarrow{\alpha}F^{\prime}$, we get an induced homomorphism

$$
H _ {*} (\mathcal {C}, F) \longrightarrow H _ {*} (\mathcal {C} ^ {\prime}, F ^ {\prime})
$$

associated to  $(f, \alpha)$ .

For simplicity we assume that $F$ and $F'$ are just functors (instead of complexes). Then $H_{0}(\mathbb{L}f_{!}(F)) = f_{!}(F)$, so $\alpha$ is the same as a map $f_{!}F \to F'$ which is in turn the same as $F \to f^{*}F'$. Thus, given $f: \mathcal{C} \to \mathcal{C}'$, $F, F'$ and $\alpha: F \to f^{*}F'$, we get an induced map on homology

$$
H _ {n} (\mathcal {C}, F) \longrightarrow H _ {n} (\mathcal {C} ^ {\prime}, F ^ {\prime}),
$$

and in particular, we always have

$$
H _ {n} (\mathcal {C}, f ^ {*} F ^ {\prime}) \longrightarrow H _ {n} (\mathcal {C} ^ {\prime}, F ^ {\prime})
$$

for any  $F' : C' \rightarrow Ab$ .

Claim The pair $f, g: \mathcal{C} \to \mathcal{C}'$ together with $h: f \to g$ is the same thing as a functor $\mathcal{C} \times I \xrightarrow{H} \mathcal{C}'$, where $I = \{0 < 1\}$ is regarded as a category, with $Hi_0 = f$, with $Hi_1 = g$ and with $\mathcal{C} \xrightarrow{i_0} \mathcal{C} \times I$ the obvious maps.

There are the three kinds of maps in $\mathcal{C} \times I$:

$$
(X, 0) \xrightarrow {(u , \mathrm{id})} (X ^ {\prime}, 0) \mid \xrightarrow {H} f (X) \xrightarrow {f (u)} f (X ^ {\prime}),\tag{i}
$$

![](images/page_96_image_4.jpg)

$$
(X, 1) \xrightarrow {(u , \mathrm{id})} (X ^ {\prime}, 1) \vdash^ {H} > f (X) \xrightarrow {f (u)} f (X ^ {\prime}),
$$

where the diamond in (ii) commutes. This justifies the claim.

Consider the projection $p = \mathcal{C} \times I \to \mathcal{C}$ onto the first factor and choose $F: \mathcal{C} \to \mathrm{Ab}$. We compute

$$
H _ {n} (\mathcal {C} \times I, p ^ {*} F) = H _ {n} (\mathcal {C}, \mathbb {L} p _ {!} (p ^ {*} F)).
$$

But $\mathbb{L} p_{!}(p^{*}F)$ has the homology groups $L_{n} p_{!}(p^{*}F)$ and $p$ is fibered and cofibered so

$$
\begin{array}{r l} L _ {n} p _ {!} (p ^ {*} F) (X) & = H _ {n} (p ^ {- 1} X, p ^ {*} F | _ {p ^ {- 1} (X)}) \\ & = H _ {n} (I, F (X) \text {   as   a   constant   functor }). \end{array}
$$

(\*) Now, $I$ has a final object $e$, so $\varinjlim_{I} F = F(e)$, whence this is an exact functor of $F$, and so $L_q \varinjlim_{I} (\cdot) = H_q(I, \cdot) = 0$, for all $q > 0$. It follows that

$$
L _ {n} p _ {!} (p ^ {*} F) (X) = \left\{ \begin{array}{c c} 0, & n \neq 0, \\ F (X), & n = 0, \end{array} \right.
$$

so $\mathbb{L}p_{!}(p^{*}F)$ is quis to $F$. Therefore $H_{n}(\mathcal{C}\times I,p^{*}F) = H_{n}(\mathcal{C},F)$.

Exercise 1 Compute $H_{n}(\mathcal{C} \times I, G)$ for any $G$ on $\mathcal{C} \times I$. One of the embeddings $i_{0}, i_{1}$ has $p$ as adjoint of the sort that (by last time) $\mathbb{L}p_{!}$ is $i_{j}^{*}$. Quillen is not sure that this will work.

Proposition (First Homotopy Property) Suppose given  $C \xrightarrow{f} C'$  with  $h : f \to g$  and  $F' : C' \to Ab$ , such that h induces an isomorphism  $f^{*}F' \to g^{*}F'$ . Recall

$$
(f ^ {*} F ^ {\prime}) (X) = F ^ {\prime} (f (X)) \xrightarrow {F ^ {\prime} (h _ {X})} F ^ {\prime} (g (X)) = (g ^ {*} F ^ {\prime}) (X),
$$

and we claim

![](images/page_97_image_6.jpg)

commutes, where  $f_{*}$  here means maps induced on homology, not the adjoint of  $f^{*}$  and likewise for  $g_{*}$ .

Example If  $F'$  is the constant functor with value  $A \in Ob Ab$ , then the proposition says that the following diagram commutes.

![](images/page_97_image_9.jpg)

Proof of Proposition We have

![](images/page_98_image_0.jpg)

and given $F'$, we know $F'(fX) \xrightarrow{\sim} F'(gX)$. But $H^{*}(F')$ is constant on the fibers of $p$, and so

$$
H ^ {*} (F ^ {\prime}) \cong p ^ {*} f ^ {*} (F ^ {\prime}) \stackrel {d} {=} p ^ {*} G.
$$

Thus we have the commutative diagram

![](images/page_98_image_4.jpg)

where  $i_{0*}$ ,  $i_{1*}$  and  $p_{*}$  are isomorphisms.

We noted in (\*) that if C has a final object, then  $\lim_{n\to\infty}\mathcal{C}$  is exact so  $H_{n}(\mathcal{C},F)=0$ , for all  $n\neq0$ . However, the conclusion is not true if  $\overrightarrow{C}$  has just an initial object.

Example

$$
a \xrightarrow {}\begin{array}{l}b\\\equiv c\end{array}\mathcal {C} \rightsquigarrow F (a) \xrightarrow {}\begin{array}{l}F (b)\\F (c)\end{array}
$$

and $H_{n}(\mathcal{C})$ fits into a Mayer-Vietoris type sequence

$$
0 \longrightarrow H _ {1} (\mathcal {C}, F) \longrightarrow F (a) \longrightarrow F (b) \oplus F (c) \longrightarrow H _ {0} (\mathcal {C}, F) \longrightarrow 0,
$$

with all  $H_{n}(\mathcal{C}, F) = 0$  for  $n \neq 0, 1$ .

This example was abandoned apologetically.

We know, for  $i_{b}$ : point  $\rightarrow C$  with image b, that

$$
\begin{array}{r l} H _ {n} (\mathcal {C}, i _ {b!} A) & = H _ {n} (\mathcal {C}, \mathbb {L} i _ {b!} (A)) \text { since } i _ {b!} \text { is   exact } \\ & = H _ {n} (\text { point }, A) \\ & = \left\{ \begin{array}{l l} A, n = 0, \\ 0, \text { else }. \end{array} \right. \end{array}
$$

Claim For a constant functor A and a category C with an initial object that

$$
H _ {n} (\mathcal {C}, A) = \left\{ \begin{array}{l l} A, & n = 0, \\ 0, & \text { else }, \end{array} \right.
$$

using the homotopy property, i.e., that if  $C \xrightarrow{f} C'$  and  $h : f \to g$ , then  $H_n(\mathcal{C}, A) \xrightarrow{f_*} H_n(\mathcal{C}', A)$  coincide.

Thus, if we have a pair of adjoint functors $\mathcal{C} \xrightarrow[f]{g} \mathcal{C}'$, then

$$
H _ {n} (\mathcal {C}, A) \xrightarrow [ g _ {*} ]{f _ {*}} H _ {n} (\mathcal {C} ^ {\prime}, A),
$$

and so $f_{*}$ and $g_{*}$ are inverses.

Proof point  $\xrightarrow{i_{X}}C$  has a right adjoint  $Y\mapsto*,$  and  $\operatorname{Hom}_{\mathcal{C}}(i_{X}*,Y)=\operatorname{Hom}_{\operatorname{point}}(*,*)$ , when X is initial in C. Thus  $H_{n}(\operatorname{point},A)=H_{n}(\mathcal{C},A)$  when C has an initial object. ☐

Claim We have  $H_{n}(\mathcal{C}, A) \cong H_{n}(\mathcal{C}^{\mathrm{op}}, A)$ .

Proof We form over  $C^{op} \times C$  the cofibered category E belonging to the functor  $(X, Y) \mapsto \operatorname{Hom}_{\mathcal{C}}(X, Y)$ . The objects of E are arrows  $X \xrightarrow{f} Y$ , and a morphism is a diagram

![](images/page_99_image_10.jpg)

We will show that the two obvious functors

![](images/page_99_image_12.jpg)

induce isomorphisms on homology.

To this end, the functor

$$
\begin{array}{c} p: \mathcal {E} \longrightarrow \mathcal {C} \\ : (X \stackrel {{f}} {{\longrightarrow}} Y) \longmapsto Y \end{array}
$$

is the composite of cofibered hence cofibered (exercise) with

$$
p ^ {- 1} Y = (\mathcal {C} / Y) ^ {\mathrm{op}}.
$$

But $\mathcal{C} / Y$ has a final object, which implies that $(\mathcal{C} / Y)^{\mathrm{op}}$ has an initial one.

Similarly,

$$
\begin{array}{c} p ^ {\prime}: \mathcal {E} \longrightarrow \mathcal {C} ^ {\prime} \\ : (X \stackrel {{f}} {{\longrightarrow}} Y) \longmapsto X \end{array}
$$

is cofibered with $(p')^{-1}(X) = X\backslash \mathcal{C}$, which also has an initial object. Now

$$
H _ {n} (\mathcal {E}, A) = H _ {n} (\mathcal {C}, \mathbb {L} p _ {!} (A))\tag{†}
$$

and $\mathbb{L} p_{!}(A)$ has homology groups given by

$$
\begin{array}{l l} L _ {q} p _ {!} (A) (Y) = H _ {q} \left(p ^ {- 1} Y, A\right) & \text { since } p \text { cofibered } \\ = \left\{ \begin{array}{l l} A, q = 0, \\ 0, \text { else }, \end{array} \right. & \text { since } p ^ {- 1} Y \text { has   an   initial   object }. \end{array}
$$

Therefore $\mathbb{L} p_{!}A = A$, so (†) follows, and similarly for $p'$.

## Chapter 19 Group Completions and Grothendieck Groups

We want to define the group completion of an abelian monoid S, (being a monoid means that S has a commutative and associative operation + and the unit 0 exists). More precisely:

Problem Construct an abelian group G and a monoid morphism  $S \stackrel{u}{\rightarrow} G$  which is universal. G is then called the group completion of S.

Solution Take $G = (S \times S) / \sim$ where $\sim$ is generated by $(s_1, s_2) \sim (s + s_1, s + s_2)$. Check this works and yields an abelian group with $-(s_1, s_2) = (s_2, s_1)$ and $u : s \mapsto (s, 0)$, so $(s_1, s_2) = u(s_1) - u(s_2)$. This is Grothendieck's construction.

Example $S = \mathbb{N}$

$$
\begin{array}{c} \mathbb {N} \times \mathbb {N} \longrightarrow \mathbb {Z} \\ (n _ {1}, n _ {2}) \longmapsto n _ {1} - n _ {2}. \end{array}
$$

We get $G = (\mathbb{N} \times \mathbb{N}) / \sim \to \mathbb{Z}$, and this map is clearly a bijection.

More generally, if S is a sub-monoid of an abelian group A so that  $A = S + (-S)$ , then  $A \approx$  group completion of S. Notice that we can do this for a category leading to a groupoid, but this loses most structure, e.g., higher homotopy.

If $X$ is a set on which $S$ acts, construct $S^{-1}X = (X \times S) / \sim$ where $\sim$ is generated by $(x, s) \sim (s' x, s' + s)$. $S^{-1}X$ is a set with $S$ action $s'(x, s) = (s' x, s)$, and each $s'$ acts invertibly on $S^{-1}X$. We also have a map $X \to S^{-1}X$ which is universal for maps from $X$ to $S$-sets on which $S$ acts invertibly.

Example Localization for S a multiplicative system in a commutative ring A and X an A-module.

Note that the group completion of S is  $S^{-1}$  S.

Exercise Calculate  $S^{-1}$  S where S = Z under multiplication.

Let $A$ be a ring and $\mathcal{P}_{A}$ the category of finitely generated projective $A$-modules $P$, so $\operatorname{Hom}(P, \cdot)$ is exact and in particular id: $P \to P$ comes from $P \to A^{n}$. Take $S$ to be the set of isomorphism classes of $\mathcal{P}_{A}$ and addition on $S$ induced by $(P, Q) \mapsto P \oplus Q$.

The Grothendieck group of  $P_{A}$  is the group completion of S, denoted  $K_{0}$  A.

Example 1 If $F$ is a field, then isomorphism classes of $\mathcal{P}_{F} \cong \mathbb{N}$ by dimension whence $K_{0} F = \mathbb{Z}$. More generally, if every $P \in \mathcal{P}_{A}$ is free, then $K_{0} A \cong \mathbb{Z}$. For instance

(1) local commutative rings by Nakayama,

(2) principal ideal domains,

(3) [1976] (Serre problem) $A = k[X_1, \ldots, X_n]$ for $k$ a principal ideal domain.

Example 2 Consider a Dedekind domain A, e.g., algebraic integers in an algebraic number field. Any finitely generated torsion free A-module is projective and is a direct sum  $P = A_{1} \oplus \ldots \oplus A_{n}$ , where the  $A_{i}$  are ideals. Actually  $P = A^{n-1} \oplus A$  where A is an ideal. In fact, the exterior algebra  $\Lambda^{n}P \cong \Lambda^{n-1}A^{n-1} \otimes \Lambda^{1}A \cong A$ , and the class of A is the ideal class group Pic A, an invariant of P. Moreover, it depends additively on the projective module. The isomorphism classes in Pic A are therefore  $S \subset N \times \operatorname{Pic} A$  in the obvious way and  $K_{0}A = Z \oplus \operatorname{Pic} A$ .

Example 3 [Serre]: Consider a compact Hausdorff space X and let A be the ring of continuous C-valued functions on X. Serre and Swan showed there is an equivalence between  $P_{A}$  and the category of complex vector bundles E over X as follows. If E is a vector bundle, let  $\Gamma(X, E)$  denote the continuous global sections of E.  $\Gamma(X, E)$  is a finitely generated projective A-module: Any E is a direct summand of a trivial vector bundle, and we get a surjection  $X \times C^{n} \to E$  which splits. Thus  $\Gamma(X, E)$  is a direct summand of  $\Gamma(X, X \times \mathbb{C}^{n}) = A^{n}$ . Conversely, given  $P \in P_{A}$ , express P as a summand of  $A^{n}$ . This gives an idempotent  $n \times n$  matrix M over A. Then M can be viewed as an endomorphism of  $X \times C^{n}$  which splits the bundle by idempotence. To see locally triviality, note that Im  $M = \text{Ker}\{1 - M\}$  again by idempotence.

Now, from algebraic topology for $X$ connected, we have isomorphism classes of $n$-dimensional vector bundles over $X$ corresponding to $[X, BU_n]$.

Instead of  $P_{A}$ , we can use any category C having a set of isomorphism classes together with a functor  $C \times C \stackrel{\perp}{\longrightarrow} C$ , where  $X \times Y \longmapsto X \perp Y$ , so that

$$
X \perp Y \simeq Y \perp X,
$$

$$
(X \perp Y) \perp Z \simeq X \perp (Y \perp Z),
$$

$$
\text { there   is } 0 \in \mathcal {C} \text { so   that } 0 \perp X \simeq X.
$$

Given all this, we can group complete the isomorphism classes in C to get a Grothendieck group  $K_{0}C$ .

Exercise For G a finite group, C the category of finite G-sets and  $X \perp Y$  the disjoint union of G-sets, describe  $K_{0}$ , called the Burnside ring of G.

Grothendieck's original: Let $\mathcal{M}$ be a full subcategory of an abelian category $\mathcal{A}$. Assume $0 \in \mathcal{M}$ and $\mathcal{M}$ is closed under extensions, i.e., if $0 \to M' \to A \to M \to 0$ is exact with $M$, $M' \in \mathcal{M}$, then $A \in \mathcal{M}$ as well.

The Grothendieck group $K_{0}\mathcal{M}$ is an abelian group together with a map

$$
M \longmapsto [ M ]
$$

from isomorphism classes of $\mathcal{M}$ to $K_0\mathcal{M}$ so that for any exact sequence $0\to M^{\prime}\to$$M\to M''\to 0$ , we have $[M] = [M'] + [M'']$ , and moreover, this map is universal.

Remark  $K_{0}(\mathcal{M},\oplus)\twoheadrightarrow K_{0}\mathcal{M}.$

$$
K_{0}(\mathcal{M},\oplus) = \bigoplus_{\substack{\text{primes $p$}\\ r\in \mathbb{Z}_{+}}}\mathbb{Z}  ,
$$

Example For M the category of finite abelian groups, we get

$$
K _ {0} (\mathcal {M}) = \bigoplus_ {\text { primes } p} \mathbb {Z}.
$$

# Chapter 20 Devissage and Resolution Theorems

Suppose that $\mathcal{M}$ is a full subcategory of an abelian category $\mathcal{A}$ where $\mathcal{M}$ is closed under finite direct sums, contains 0 and whose isomorphism classes form a set. Recall that $K_{0} \mathcal{M}$ is an abelian group together with a universal map

$$
\mathrm{Ob} \mathcal {M} \longrightarrow K _ {0} \mathcal {M}
$$

so that

$$
0 \longrightarrow M ^ {\prime} \longrightarrow M \longrightarrow M ^ {\prime \prime} \longrightarrow 0
$$

exact in M implies that  $[M]=[M']+[M'']$ .

Remark If  $M = P_{A}$ , then exact sequences split, so  $K_{0}(\mathcal{M}, \oplus) = K_{0}\mathcal{M}$ . In general,  $K_{0}\mathcal{M}$  is a quotient of  $K_{0}(\mathcal{M}, \oplus)$ .

Example Let $\mathcal{M}$ be the category of finite abelian $p$-groups. Recall that Krull-Schmidt says every $M \in \mathcal{M}$ is a direct sum of indecomposables in a unique way up to isomorphism. Thus isomorphism classes of $\mathcal{M}$ are given by the free abelian monoid generated by indecomposable isomorphism classes, i.e., $\mathbb{Z}/p^r$, $r = 1, \ldots$. Thus $K_0(\mathcal{M}, \oplus)$ is the free abelian group generated by

$$
\mathbb {Z} / p ^ {r} \mathbb {Z}, \quad r \geq 1.
$$

Whilst in general if we have a filtration

$$
0 = F _ {- 1} M \subset F _ {0} M \subset \dots \subset F _ {n} M = M
$$

of $M \in \mathcal{M}$ so that each $F_{p} M$ and $F_{p} M / F_{p-1} M \in \mathcal{M}$, then in $K_{0} \mathcal{M}$, we have

$$
(\dagger) M = \sum_ {p = 0} ^ {n} [ F _ {p} M / F _ {p - 1} M ].
$$

Thus in our example, every M has a filtration with quotients Z/pZ so  $K_{0}M = Z$ . Namely we have the map assigning the integral filtration length which is a homomorphism  $K_{0}M \to Z$  by universality.

More generally, suppose $\mathcal{M}$ is an abelian category where every object has the descending chain condition and the ascending chain condition on its sub-objects. Then Jordan–Hölder applies, so we can speak of the multiplicity $m_{\sigma}(M)$ of the simple object $\sigma$ in any composition series for $M$. We have $M \longmapsto \{m_{\sigma}(M)\}$ in the free monoid generated by simple objects and get a map $K_0 \mathcal{M} \stackrel{\approx}{\to} \bigoplus \mathbb{Z}$.

Devissage Theorem (Grothendieck) Let $\mathcal{A}$ be an abelian category and $\mathcal{A}' \subset \mathcal{A}$ full so that also $\mathcal{A}'$ is abelian. Assume every $A$ in $\mathcal{A}$ has a finite filtration

$$
0 = F _ {- 1} \subset \dots \subset F _ {n} = A
$$

so that $F_{p} / F_{p - 1}\in \mathcal{A}'$ . Then $K_0\mathcal{A}'\stackrel {\sim}{\longrightarrow}K_0\mathcal{A}$

Example 1 Take A to be finite abelian p-groups and  $A'$  to be finitely generated Z/p-modules.

Example 2 Suppose A is a noetherian ring,  $\mathcal{M} = \text{Modf}(A)$ , the finitely generated A-modules, and  $I \subset A$  is a nilpotent ideal. Take  $\mathcal{M}' = \text{Modf}(A/I)$  where

$$
0 = I ^ {n} M \subset \dots \subset I M \subset M.
$$

Thus  $K_{0}$  Mod  $f(A/I) = K_{0}$  Mod  $f(A)$ .

The proof of the Devissage Theorem is based on the Schreier refinement lemma.

Lemma (Schreier) Suppose M has two filtrations  $\cdots \subset F_{p} M \subset F_{p+1} M \subset \cdots$  and  $\cdots \subset F_{q}' M \subset F_{q+1}' M \subset \cdots$ , neither necessarily terminating. Then  $F'$  induces a filtration on  $gr^{F} M = \bigoplus F_{p} M / F_{p-1} M$  via  $F_{q}'(F_{p} M) = F_{q}' M \cap F_{p} M$ , i.e.,

$$
F _ {q} ^ {\prime} (F _ {p} M / F _ {p - 1} M) = \text { Image } \left\{F _ {q} ^ {\prime} \cap F _ {p} \longrightarrow F _ {p} / F _ {p - 1} \right\}.
$$

Similarly $F$ induces a filtration on $\mathrm{gr}^{F'}M = \oplus F_q' / F_{q - 1}'$. Then we have

$$
\operatorname{gr} ^ {F ^ {\prime}} \left(\operatorname{gr} ^ {F} (M)\right) = \operatorname{gr} ^ {F} \left(\operatorname{gr} ^ {F ^ {\prime}} (M)\right).
$$

Proof We have the formulae

$$
\begin{array}{c} F _ {q} ^ {\prime} (F _ {p} / F _ {p - 1}) = F _ {q} ^ {\prime} \cap F _ {p} + F _ {p - 1} / F _ {p - 1}, \\ \mathrm{gr} _ {q} ^ {F ^ {\prime}} (F _ {p} / F _ {p - 1}) = \frac {F _ {q} ^ {\prime} \cap F _ {p} + F _ {p - 1}}{F _ {q - 1} ^ {\prime} \cap F _ {p} + F _ {p - 1}} = \frac {F _ {q} ^ {\prime} \cap F _ {p}}{(F _ {q - 1} ^ {\prime} \cap F _ {p} + F _ {p - 1}) \cap (F _ {q} ^ {\prime} \cap F _ {p})} \end{array}
$$

but

$$
\left(\left(F _ {q - 1} ^ {\prime} \cap F _ {p}\right) + F _ {p - 1}\right) \cap \left(F _ {q} ^ {\prime} \cap F _ {p}\right) = F _ {q - 1} ^ {\prime} \cap F _ {p} + F _ {p - 1} \cap F _ {q} ^ {\prime}.
$$

□

Remark The refinement lemma fails for 3 filtrations since the modular law fails.

Proof of Devissage Given $M \in \mathcal{A}$, choose a filtration $F_{p} M$ exhausting $M$ with quotients $\mathrm{gr}_{p}^{F}(M) \in \mathcal{A}'$ and consider

$$
\sum_ {p} \left[ \mathrm{gr} _ {p} ^ {F} M \right] \in K _ {0} \mathcal {A} ^ {\prime}.
$$

Claim This does not depend on the choice of  $\{F_{p} M\}$ . This follows easily from the previous lemma and (†).

Thus we get a map $\gamma: \text{Ob } \mathcal{A} \to K_0 \mathcal{A}'$. Then $0 \to M' \to M \to M'' \to 0$ exact in $\mathcal{A}$ implies that $\gamma(M) = \gamma(M') + \gamma(M'')$. By universality, we get $\gamma: K_0 \mathcal{A} \to K_0 \mathcal{A}'$, which is inverse to the map induced by inclusion.

Example Take $\mathcal{A} = \operatorname{Modf}(\mathbb{Z})$, so $\mathcal{P}_{\mathbb{Z}}$ is the category of free finitely generated abelian groups, and we have $K_0\mathcal{P}_{\mathbb{Z}}) = \mathbb{Z}$. Now, any finitely generated abelian group has a resolution

$$
0 \longrightarrow \mathbb {Z} ^ {q} \longrightarrow \mathbb {Z} ^ {p} \longrightarrow M \longrightarrow 0
$$

SO

$$
\begin{array}{c} {[ M ] = [ \mathbb {Z} ^ {p} ] - [ \mathbb {Z} ^ {q} ]} \\ {= (p - q) [ \mathbb {Z} ],} \end{array}
$$

whence  $K_{0} \mathcal{P}_{\mathbb{Z}} \twoheadrightarrow K_{0}(\text{Mod } f(\mathbb{Z}))$  is in fact an isomorphism.

Resolution Theorem (Grothendieck) Suppose A is a noetherian ring so that every finitely generated A-module M has a finite resolution of projectives

$$
0 \longrightarrow P _ {n} \longrightarrow \dots \longrightarrow P _ {0} \longrightarrow M \longrightarrow 0\tag{*}
$$

A is said to be regular in this case.

Then

$$
K _ {0} (\mathcal {P} _ {A}) \stackrel {{\sim}} {{\longrightarrow}} K _ {0} \operatorname{Modf} (A).
$$

The idea is to define

$$
\begin{array}{c} K _ {0} \operatorname{Modf} (A) \longrightarrow K _ {0} \mathcal {P} _ {A} \\ [ M ] \longmapsto \sum_ {i = 0} ^ {n} (- 1) ^ {i} [ P _ {i} ]. \end{array}
$$

If this is well defined, then it is an inverse to $K_0 \mathcal{P}_A \to K_0 \operatorname{Modf}(A)$. To see this, decompose (\*) into

$$
0 \longrightarrow R _ {1} \longrightarrow P _ {0} \longrightarrow M \longrightarrow 0
$$

$$
0 \longrightarrow R _ {2} \longrightarrow P _ {1} \longrightarrow R _ {1} \longrightarrow 0
$$

$$
0 \longrightarrow 0 \longrightarrow P _ {n} \longrightarrow R _ {n} \longrightarrow 0.
$$

Thus in $K_{0}\operatorname{Modf}(A)$, we have

$$
[ M ] = \sum_ {i = 0} ^ {n} (- 1) ^ {i} [ P _ {i} ],
$$

and it remains as an exercise only to show it is well defined.

# Chapter 21 Exact Sequences of Homotopy Classes

Suppose that $F: \mathcal{A} \to \mathcal{B}$ is an additive functor between abelian categories and $\mathcal{A}$ has enough projectives. For $M$ in $\mathcal{A}$, choose a projective resolution, i.e., a quis $P. \to M[0]$. Then $F(P.) = \mathbb{L}F(M[0])$ is unique up to canonical isomorphism in $D_{+}(\mathcal{B})$, and we define

$$
\begin{array}{r l} L _ {i} F (M) & = H _ {i} \mathbb {L} F (M [ 0 ]) \\ & = H _ {i} F (P). \end{array}
$$

Claim Given $0 \to M' \to M \to M'' \to 0$ exact in $\mathcal{A}$, then we have a natural long exact sequence

(†)  $\cdots\longrightarrow L_{1}FM^{\prime}\longrightarrow L_{1}FM\longrightarrow L_{1}FM^{\prime\prime}\longrightarrow L_{0}FM^{\prime}\longrightarrow L_{0}FM\longrightarrow L_{0}FM^{\prime\prime}\longrightarrow0$ . We shall prove this more generally for M. in  $C_{+}(\mathcal{A})$  and  $P.\rightarrow M.$ , and then the sequence (†) continues on to the right:  $L_{0}FM^{\prime\prime}\rightarrow L_{-1}FM^{\prime}\rightarrow\cdots$ .

Proof Start with projective resolutions of $M'$ and $M$

$$
\begin{array}{c} P ^ {\prime} - \stackrel {{f}} {{-}} > P \\ \text {quis} \Biggl \downarrow p ^ {\prime} \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text {quis} \\ 0 \longrightarrow M ^ {\prime} \xrightarrow [ i ]{} M \longrightarrow M ^ {\prime \prime} \longrightarrow 0 \end{array}\tag{*}
$$

and note that the induced  $P' \rightarrow P$  comes from  $[P', P] \stackrel{\sim}{\longrightarrow} [P', M]$ .

Thus we get $f: P' \to P$ and a homotopy $h: ip' \to pf$, i.e., $dh + hd = pf - ip'$.

Note that given

(\*\*)

![](images/page_109_image_2.jpg)

with a homotopy $h$ from $f$ to $g$, we can form $A \xrightarrow{i_0} A \times I \cup_i B$ and get a map $M(i) \to X$, where $M(\bullet)$ is the mapping cylinder of $\bullet$. satisfying

![](images/page_109_image_4.jpg)

where the right-hand diagram and the bottom triangle of the left-hand diagram each commutes and the diagonal morphism of the left-hand diagram is a homotopy equivalence.

Recall we have $M(f: P' \to P) = P_I' \coprod_{P'} P$ as $M(f: P' \to P)_n = P_n' \oplus P_{n-1}' \oplus P_n$ with the appropriate differential.

Thus we can replace $P$ in $(*)$ by $M(f:P^{\prime}\to P)$ to get

![](images/page_109_image_8.jpg)

where we can check that with an appropriate choice of sign in  $\pm h$  that  $(ip', h, p)$  is a chain map.

We get

![](images/page_109_image_11.jpg)

where Cone(●) is the mapping cone of ● and the leftmost square commutes, proving the rightmost map to be a quis by a long exact and the 5-lemma.

It is also clear that Cone (f) is projective.

Now apply $F$ to get a sequence

$$
0 \longrightarrow F (P ^ {\prime}) \longrightarrow F M (f) \longrightarrow F \operatorname{Cone} (f) \longrightarrow 0,\tag{‡}
$$

which is exact because the sequence ( $^{**}$ ) splits since Cone  $(f) \in C_{+}(\mathcal{P})$ . In fact F Cone  $(f) = \text{Cone } Ff$  for F additive.

Now take the long exact homology sequence of (‡). Naturality follows easily.

Suppose given a module exact sequence and two projective resolutions, so we have

![](images/page_110_image_4.jpg)

This does not work for complexes because projective in each degree does not imply projective.

Exercise Describe projective objects in  $C_{+}(\mathcal{A})$ ; the answer is not all of  $C_{+}(\mathcal{P})$ .

Puppe Sequences Fix an additive category A and suppose we have a map  $f : A \to B$  of complexes. Then we get, for any complex N, a long exact sequence

$$
\begin{array}{r l} & \dots \longleftarrow [ S ^ {- 1} \text {Cone} f, N ] \longleftarrow [ A, N ] \longleftarrow [ B, N ] \longleftarrow [ \text {Cone} f, N ] \longleftarrow \\ & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \dots \\ & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \end{array}
$$

where $SA = \operatorname{Cone} A \to 0$ so $(SA)_n = A_{n-1}$ and $d: (SA)_n \to (SA)_{n-1}$ is given by $-d: A_{n-1} \to A_{n-2}$.

Lemma Suppose  $0 \rightarrow A' \rightarrow A \rightarrow A'' \rightarrow 0$  is an exact sequence of complexes which splits in each dimension. Then for any N, we have exact sequences

$$
[ A ^ {\prime}, N ] \longleftarrow [ A, N ] \longleftarrow [ A ^ {\prime \prime}, N ],
$$

$$
[ N, A ^ {\prime} ] \longrightarrow [ N, A ] \longrightarrow [ N, A ^ {\prime \prime} ].
$$

Proof We introduce the complex Hom. $(A, N)$ , where

$$
\operatorname{Hom} _ {p} (A, N) = \prod_ {n} \operatorname{Hom} (A _ {n}, N _ {n + p})
$$

with  $df = d \circ f - (-1)^{p} f \circ d$ .

Remark 0-cycles in Hom. $(A, N)$ are $f = (f : A_{n} \to N_{n})$ so that $d \circ f = f \circ d$, i.e., maps of complexes $A \to N$. A zero-boundary is a map $f = (f : A_{n} \to N_{n})$ of the form $f = d \circ h + h \circ d$ for some $h = (h : A_{n} \to N_{n+1})$ i.e., those maps homotopic to zero. Thus

$$
H _ {0} \operatorname{Hom}. (A, N) = [ A, N ].
$$

Now, if  $0 \rightarrow A' \rightarrow A \rightarrow A'' \rightarrow 0$  splits in each dimension, then

$$
0 \longrightarrow \operatorname{Hom}. (N, A ^ {\prime}) \longrightarrow \operatorname{Hom}. (N, A) \longrightarrow \operatorname{Hom}. (N, A ^ {\prime \prime}) \longrightarrow 0
$$

is exact as a product of exact sequences. Take the homology.

Remark For complexes of abelian groups for example, we have $K \otimes L$. with $d(x \otimes y) = dx \otimes y + (-1)^{|x|} x \otimes dy$. Then the differential in Hom. (A, N) is the one making the evaluation map

$$
\operatorname{Hom}. (A., N.) \otimes N. \longrightarrow N.
$$

a map of complexes.

Recall the

Lemma Suppose $0 \to A' \to A \to A'' \to 0$ is exact in $C(\mathcal{A})$ and splits in each dimension. Then

$$
[ A ^ {\prime}, X ] \longleftarrow [ A, X ] \longleftarrow [ A ^ {\prime \prime}, X ]
$$

is exact.

Recall also that given $A \xrightarrow{f} B$, we can construct $M(f) = A_I \coprod_A B$. Thus, we have the commutative diagram

![](images/page_112_image_5.jpg)

and set $C(f) = \operatorname{Cok} i_0$. The Lemma applies to

$$
0 \longrightarrow A \stackrel {i _ {0}} {\longrightarrow} M (f) \longrightarrow C (f) \longrightarrow 0
$$

because in dimension $n$ we have

$$
0 \longrightarrow A _ {n} \longrightarrow A _ {n} \oplus A _ {n - 1} \stackrel {\angle} {\oplus} B _ {n} \longrightarrow A _ {n - 1} \oplus B _ {n} \longrightarrow 0,
$$

and so we get an exact

![](images/page_113_image_0.jpg)

where  $j : B \hookrightarrow C(f)$ .

Now construct

$$
A \xrightarrow {f} B \xrightarrow {j} C (f) \xrightarrow {j ^ {\prime}} C (j) \longrightarrow C (j ^ {\prime}) \longrightarrow \dots
$$

and get exact sequences of homotopy classes

$$
[ A, X ] \longleftarrow [ B, X ] \longleftarrow [ C (f), X ] \longleftarrow [ C (j), X ] \longleftarrow [ C (j ^ {\prime}), X ].
$$

Note that in general $C(f) / B = S(A)$ and $C(j) / C(f) = S(B)$.

(†) Lemma: If $A \xrightarrow{f} B$ is injective and splits in each dimension, then the canonical map

$$
C (f) \longrightarrow B / A
$$

is a homotopy equivalence.

Thus $C(f)/B \xleftarrow{\text{homotopy}} C(j)$ and $C(j)/C(f) \xleftarrow{\text{homotopy}} C(j')$,

and so we get the exact sequence

$$
\dots \longleftarrow [ A, X ] \longleftarrow [ B, X ] \longleftarrow [ C (f), X ] \longleftarrow [ S A, X ] \longleftarrow [ S B, X ] \longleftarrow \dots
$$

Point of Lemma (†): We have

![](images/page_113_image_14.jpg)

The first lemma gives the following exact

$$
\begin{array}{c} \left[ A, X \right] \xleftarrow {} \left[ B, X \right] \xleftarrow {} \left[ B / A, X \right] \xleftarrow {} H _ {1} \operatorname{Hom}. (A, X) \xleftarrow {} \bullet \\ \Big \| \quad \Big \downarrow \\ \left[ A, X \right] \xleftarrow {} \left[ M (f), X \right] \xleftarrow {} \left[ C (f), X \right] \xleftarrow {} H _ {1} \operatorname{Hom}. (A, X) \xleftarrow {} H _ {1} \operatorname{Hom}. C (f) \end{array}
$$

so the 5-lemma implies $[B / A, X] \xrightarrow{\sim} [C(f), X]$ and by Yoneda $C(f) \to B / A$ is an isomorphism in $K\mathcal{A}$, as desired.

## Spectral Sequences

Situation: Suppose K is a complex provided with an increasing filtration by sub-complexes

$$
0 \subset \dots \subset F _ {p - 1} K \subset F _ {p} K \subset F _ {p + 1} K \subset \dots \subset K
$$

and suppose  $T_{*}=\{T_{n}\}$  is a “ $\partial$ -functor on complexes”, that is, it associates naturally to a short exact sequence of complexes  $0\to K'\to K\to K''\to0$  a long exact sequence

$$
\dots \longrightarrow T _ {n + 1} K ^ {\prime \prime} \stackrel {\partial} {\longrightarrow} T _ {n} K ^ {\prime} \longrightarrow T _ {n} K \longrightarrow T _ {n} K ^ {\prime \prime} \stackrel {\partial} {\longrightarrow} T _ {n - 1} K ^ {\prime} \longrightarrow \dots
$$

in an abelian category B.

Problem To relate  $T_{*}K$  with  $T_{*}gr_{*}K$  where

$$
\operatorname{gr} _ {p} K = F _ {p} K / F _ {p - 1} K.
$$

Useful diagram: Given

![](images/page_114_image_9.jpg)

where the top-left square commutes, then we have

$$
\begin{array}{l} \text {Cok} v / \text {Cok} u \\ \Bigg \backslash \\ \text {Cok} b / \text {Cok} a = D / (\text {Im} b \oplus \text {Im} v). \end{array}
$$

Proof Diagram chase.

Consider the induced filtration on $T_{*}(K)$ and let $F_{p}T_{*}K = \operatorname{Im}\{T_{*}F_{p}K\to T_{*}K\}$. Can we see $F_{p}TK / F_{p - 1}TK$ inside $TK_{p} / K_{p - 1}$? Use the exact sequence

$$
T _ {n + 1} (K / F _ {p} K) \xrightarrow {\partial} T _ {n} F _ {p} K \longrightarrow T _ {n} K \longrightarrow T _ {n} K / F _ {p} K
$$

to get

$$
\operatorname{Cok} \left\{T _ {n + 1} K / F _ {p} K \xrightarrow {\partial} T _ {n} F _ {p} K \right\} = F _ {p} T K.
$$

Then we find

![](images/page_115_image_3.jpg)

Thus by the useful diagram,  $F_{p} T_{n} K / F_{p-1} T_{n} K$  is isomorphic to a sub-quotient of  $T_{n} F_{p} K / F_{p-1} K$ .

Precisely, if we put

$$
F _ {p} T _ {n} K / F _ {p - 1} T _ {n} K \cong \frac {\operatorname{Im} \left\{T _ {n} F _ {p} K \rightarrow T _ {n} F _ {p} / F _ {p - 1} \right\}}{\operatorname{Im} \left\{T _ {n + 1} K / F _ {p} K \rightarrow T _ {n} F _ {p} / F _ {p - 1} \right\}},
$$

then we derive

Corollary If the filtration is finite and exhausts $K$ and if $T_{n}(F_{p} / F_{p - 1}) = 0$, then $T_{n}K = 0$.

Define $T_{n}F_{p}K / F_{q}K = T_{n}(p,q)$ and set

$$
\begin{array}{r l} Z _ {p, q} ^ {r} & = \operatorname{Im} \{T _ {p + q} (p, p - r) \longrightarrow T _ {p + q} (p, p - 1) \} \\ & = \operatorname{Im} \{T _ {p + q} F _ {p} / F _ {p - r} \longrightarrow T _ {p + q} F _ {p} / F _ {p - 1} \}. \end{array}
$$

Then we find

$$
\dots \subset Z _ {p q} ^ {3} \subset Z _ {p q} ^ {2} \subset Z _ {p q} ^ {1} = T _ {p + q} (p, p - 1),
$$

and if we interpret $F_{-\infty}K = 0$ then

$$
Z _ {p q} ^ {\infty} = \operatorname{Im} \left\{T _ {p + q} \left(F _ {p}\right) \longrightarrow T _ {p + q} F _ {p} / F _ {p - 1} \right\}.
$$

Putting

$$
B _ {p q} ^ {r} = \operatorname{Im} \left\{T _ {p + q + 1} (p + r - 1, p) \longrightarrow T _ {p + q} (p, p - 1) \right\},
$$

we have

$$
0 = B _ {p q} ^ {1} \subset B _ {p q} ^ {2} \subset B _ {p q} ^ {3} \subset \dots ,
$$

and if we interpret $F_{\infty}K = K$, then we have

$$
B _ {p q} ^ {\infty} = \operatorname{Im} \left\{T _ {p + q + 1} K / F _ {p} K \longrightarrow T _ {p + q} F _ {p} / F _ {p - 1} \right\}.
$$

Thus we have

$$
0 = B ^ {1} \subset B ^ {2} \subset \dots \subset B ^ {\infty} \subset Z ^ {\infty} \subset \dots \subset Z ^ {2} \subset Z ^ {1} = T _ {p + q} F _ {p} / F _ {p - 1}.
$$

Now exactness of

$$
T _ {n} (p - 1, p - r) \longrightarrow T _ {n} (p, p - r) \longrightarrow T _ {n} (p, p - 1)
$$

implies

$$
Z _ {p q} ^ {r} = \operatorname{Cok} \left\{T _ {p + q} (p - 1, p - r) \longrightarrow T _ {p + q} (p, p - r) \right\}
$$

and

$$
Z _ {p q} ^ {r + 1} = \operatorname{Cok} \left\{T _ {p + q} (p - 1, p - r - 1) \longrightarrow T _ {p + q} (p, p - r - 1) \right\}.
$$

Similarly

$$
T _ {n + 1} (p + r - 1, p - 1) \longrightarrow T _ {n + 1} (p + r - 1, p) \stackrel {\partial} {\longrightarrow} T _ {n} (p, p - 1)
$$

gives

$$
B _ {p q} ^ {r} = \operatorname{Cok} \left\{T _ {p + q + 1} (p + r - 1, p - 1) \longrightarrow T _ {p + q + 1} (p + r - 1, p) \right\}
$$

and

$$
B _ {p - r, q + r - 1} ^ {r} = \operatorname{Cok} \left\{T _ {p + q} (p - 1, p - r - 1) \longrightarrow T _ {p + q} (p - 1, p - r) \right\},
$$

and we find

$$
\begin{array}{c} T _ {p + q} (p - 1, p - r - 1) \longrightarrow T _ {p + q} (p, p - r - 1) \longrightarrow Z _ {p q} ^ {r + 1} \longrightarrow 0 \\ \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Bigg \downarrow \\ T _ {p + q} (p - 1, p - r) \longrightarrow T _ {p + q} (p, p - r) \longrightarrow Z _ {p q} ^ {r} \longrightarrow 0 \\ \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \Bigg \downarrow \\ B _ {p - r, q + r - 1} ^ {r} \qquad \qquad \qquad B _ {p - r, q + r - 1} ^ {r + 1} \\ \Bigg \downarrow \qquad \qquad \qquad \qquad \Bigg \downarrow \\ 0 \qquad \qquad 0 \end{array}
$$

If we set

$$
E _ {p q} ^ {r} = Z _ {p q} ^ {r} / B _ {p q} ^ {r}
$$

and define

$$
\begin{array}{c} d _ {r}: E _ {p q} ^ {r} \longrightarrow E _ {p - r, q + r - 1} ^ {r} \\ \Big \| \qquad \qquad \qquad \qquad \qquad \qquad \Big \| \\ Z _ {p q} ^ {r} / B _ {p q} ^ {r} \longrightarrow Z _ {p q} ^ {r} / Z _ {p q} ^ {r + 1} = B _ {p q} ^ {r + 1} / B _ {p q} ^ {r}, \end{array}
$$

then $d_r^2 = 0$ on $E_{**}^r$ and has homology $H(E_{**}^r,d_r) = E_{**}^{r + 1}$.

Recall that

$$
T _ {n} (p, p ^ {\prime}) = T _ {n} (F _ {p} K / F _ {p ^ {\prime}} K),
$$

$$
E _ {p, q} ^ {1} = T _ {p + q} (p, p - 1).
$$

We define

$$
0 = B _ {p q} ^ {1} \subset B _ {p q} ^ {2} \subset \ldots \subset B _ {p q} ^ {\infty} \subset Z _ {p q} ^ {\infty} \subset \ldots \subset Z _ {p q} ^ {2} \subset Z _ {p q} ^ {1} = E _ {p q} ^ {1},
$$

$$
\begin{array}{l} Z _ {p q} ^ {r} = \operatorname{Ker} \left\{T _ {p + q} (p, p - 1) \xrightarrow {\partial} T _ {p + q - 1} (p - 1, p - r) \right\} \\ = \operatorname{Im} \left\{T _ {p + q} (p, p - r) \longrightarrow T _ {p + q - 1} (p - 1, p - r) \right\} \\ = \operatorname{Cok} \left\{T _ {p + q} (p - 1, p - r) \longrightarrow T _ {p + q} (p, p - r) \right\}, \end{array}
$$

$$
Z _ {p q} ^ {r + 1} = \operatorname{Cok} \left\{T _ {p + q} (p - 1, p - r - 1) \longrightarrow T _ {p + q} (p, p - r - 1) \right\},
$$

$$
\begin{array}{r l} B _ {p q} ^ {r} & = \mathrm{Im} \left\{T _ {p + q + 1} (p + r - 1, p) \xrightarrow {\partial} T _ {p + q} (p, p - 1) \right\} \\ & = \mathrm{Cok} \left\{T _ {p + q + 1} (p + r - 1, p - 1) \longrightarrow T _ {p + q + 1} (p + r - 1, p) \right\}, \end{array}
$$

$$
B _ {p - r, q + r - 1} ^ {r} = \operatorname{Cok} \left\{T _ {p + q} (p - 1, p - r - 1) \longrightarrow T _ {p + q} (p - 1, p - r) \right\},
$$

$$
B _ {p - r, q + r - 1} ^ {r + 1} = \operatorname{Cok} \left\{T _ {p + q} (p, p - r - 1) \longrightarrow T _ {p + q} (p, p - r) \right\}.
$$

We thus have

$$
\begin{array}{c} T _ {p + q} (p - 1, p - r - 1) \longrightarrow T _ {p + q} (p, p - r - 1) \longrightarrow Z _ {p q} ^ {r + 1} \longrightarrow 0 \\ \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \cap \\ T _ {p + q} (p - 1, p - r) \longrightarrow T _ {p + q} (p, p - r) \longrightarrow Z _ {p q} ^ {r} \longrightarrow 0 \\ \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Bigg \downarrow \\ B _ {p - r, q + r - 1} ^ {r} \subset B _ {p - r, q + r - 1} ^ {r + 1} \\ \Bigg \downarrow \qquad \qquad \qquad \qquad \qquad \Bigg \downarrow \\ 0 \qquad \qquad 0 \end{array}
$$

Thus,

$$
\boxed {Z _ {p q} ^ {r} / Z _ {p q} ^ {r + 1} \approx B _ {p - r, q + r - 1} ^ {r + 1} / B _ {p - r, q + r - 1} ^ {r}}
$$

by the previous useful diagram and lemma from last time.

Put $E_{pq}^{r} = Z_{pq}^{r} / B_{pq}^{r}$ and consider

$$
E _ {p + r, q - r + 1} ^ {r} \xrightarrow {d _ {r}} E _ {p q} ^ {r} \xrightarrow {d _ {r}} E _ {p - r, q + r - 1} ^ {r}
$$

$$
\begin{array}{c c c} Z _ {p + r, q - r + 1} ^ {r} & Z _ {q} ^ {r} & Z _ {p - r, q + r - 1} ^ {r} \\ \cup & \cup & \cup \end{array}
$$

$$
\begin{array}{c c c} Z _ {p + r, q - r + 1} ^ {r + 1} & Z _ {p q} ^ {r + 1} & Z _ {p - r, q + r - 1} ^ {r + 1} \\ \cup & \cup & \cup \end{array}
$$

$$
\begin{array}{c c c} B _ {p + r, q - r + 1} ^ {r + 1} \cong & B _ {p q} ^ {r + 1} & \cong B _ {p - r, q + r - 1} ^ {r + 1} \\ \cup & \cup & \cup \end{array}
$$

$$
B _ {p + r, q - r + 1} ^ {r} \quad B _ {p q} ^ {r} \quad B _ {p - r, q + r - 1} ^ {r}
$$

where the boxed result above gives an isomorphism between the quotients of top two terms with the quotients of the adjacent bottom two terms.

Define $d_r: E_{p,q}^r \to E_{p-r,q+r-1}^r$ to be the composition

$$
E _ {p q} ^ {r} \longrightarrow Z _ {p q} ^ {r} / Z _ {p q} ^ {r + 1} \quad \cong B _ {p - r, q + r - 1} ^ {r + 1} / B _ {p - r, q + r - 1} ^ {r}
$$

$$
E _ {p - r, q + r - 1} ^ {r}
$$

Clear that $d_r^2 = 0$ and

$$
E _ {p q} ^ {r + 1} = \frac {\operatorname{Ker} \left\{d _ {r} : E _ {p q} ^ {r} \longrightarrow E _ {p - r , q + r - 1} ^ {r} \right\}}{\operatorname{Im} \left\{d _ {r} : E _ {p + r , q - r + 1} ^ {r} \longrightarrow E _ {p q} ^ {r} \right\}}.
$$

We get the spectral sequence

$$
E _ {* *} ^ {r} = \{E _ {p q} ^ {r} \}, \qquad r = 1, 2, \ldots ,
$$

and on each  $E^{r}$  there is  $d_{r}: E_{pq}^{r} \rightarrow E_{p-r,q+r-1}^{r}$  so that  $d_{r}^{2}=0$ , and  $E^{r+1}=H(E_{r}, d_{r})$ .

The beginning of the spectral sequence is

$$
\begin{array}{r} E _ {p q} ^ {1} = T _ {p + q} (p, p - 1) \\ = T _ {p + q} (F _ {p} K / F _ {p - 1} K) \end{array}
$$

and the end is

$$
E _ {p q} ^ {\infty} = \frac {\operatorname{Im} \left\{T _ {p + q} F _ {p} K \longrightarrow T _ {p + q} K \right\}}{\operatorname{Im} \left\{T _ {p + q} F _ {p - 1} K \longrightarrow T _ {p + q} K \right\}}.
$$

$T_{*}K$  is called the abutment.

Convergence Question: In what sense is $E^{\infty} = \lim E^{r}$?

$$
Z _ {p q} ^ {\infty} = \operatorname{Ker} \left\{T _ {p + q} (p, p - 1) \xrightarrow {\partial} T _ {p + q - 1} (F _ {p - 1} K) \right\},
$$

and

$$
B _ {p q} ^ {\infty} = \operatorname{Im} \left\{T _ {p + q + 1} (F _ {p} K) \longrightarrow T _ {p + q} (p, p - 1) \right\}.
$$

We say the spectral sequence converges strongly if for a given p and q we have

$$
Z _ {p q} ^ {\infty} = Z _ {p q} ^ {r} \quad \text { and } \quad B _ {p q} ^ {\infty} = Z _ {p q} ^ {r} \quad \text { for   } r \text {   large   enough }.
$$

Exercise Consider a $\partial$-functor $\{T_n\}$, where the $\partial$'s lower degree by 1, and a complex with a decreasing filtration $\ldots \supset F_q K \supset F_{q+1} K \supset \ldots$. Show then that we have a spectral sequence $E_{pq}^r$, for $r \geq 2$, starting with

$$
E _ {p q} ^ {2} = T _ {p + q} (F _ {q} K / F _ {q + 1} K)
$$

and with

![](images/page_121_image_3.jpg)

abutting to  $T_{*}K$ .

Reference: Cartan Seminars.

Examples 2 step filtration: $0 = F_{-1}K \subset F_0K \subset F_1K = K$ so

$$
\begin{array}{r l} E _ {p q} ^ {1} & = T _ {p + q} F _ {p} K / F _ {p - 1} K \\ & = 0 \quad \text { for } p \neq 0, 1. \end{array}
$$

with

(\*)

$$
\begin{array}{c} 0 \longrightarrow F _ {0} / F _ {- 1} \longrightarrow F _ {1} / F _ {- 1} \longrightarrow F _ {1} / F _ {0} \longrightarrow 0 \\ \Big \| \quad \Big \| \quad \Big \| \\ K ^ {\prime} \quad K \quad K ^ {\prime \prime} \end{array}
$$

and we suppose  $T_{n}=0$  for all n<0.

| $T_{3}K'$ |  |  |
| --- | --- | --- |
| $T_{2}K'$ | $T_{3}K''$ |  |
| $T_{1}K'$ | $T_{2}K''$ |  |
| $T_{0}K'$ | $T_{1}K''$ |  |
| $T_{-1}K'$ | $T_{0}K''$ |  |

$$
\begin{array}{c} d _ {1}: E _ {p q} ^ {1} \xrightarrow {} E _ {p - 1, q} ^ {1} \\ \Big \| \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Big \| \\ T _ {p + q} (F _ {p} / F _ {p - 1}) \xrightarrow {\partial} T _ {p + q - 1} (F _ {p - 1} / F _ {p - 2}), \end{array}
$$

and it can be shown that $d_{1} = 0$ for the long exact sequence.

Now $d_{2}$ lowers $p$ by 2 and hence is zero, whence $E_{pq}^{\infty}=E_{pq}^{2}$.

Thus $T_{n}K$ has a 2-step filtration

$$
\begin{array}{r l} E _ {0, n} ^ {\infty} & = \mathrm{Im} \{T _ {n} K ^ {\prime} \to T _ {n} K \} = E _ {0, n} ^ {2} \\ & = \mathrm{Cok} \{T _ {n + 1} (K ^ {\prime \prime}) \to T _ {n} K ^ {\prime} \} \\ E _ {1, n - 1} ^ {\infty} & = T _ {n} K / \mathrm{Im} \{T _ {n} K ^ {\prime} \to T _ {n} K \} \\ & = E _ {1, n - 1} ^ {2} \\ & = \mathrm{Ker} \{T _ {n} K ^ {\prime \prime} \to T _ {n - 1} K ^ {\prime} \}. \end{array}
$$

This gives the same information as the long exact sequence of (\*).

Another picture of the spectral sequence:

$$
\begin{array}{c} \xrightarrow {\partial} T _ {p + q} (p - 2) \xrightarrow {} T _ {p + q} (p - 2, p - 3) \xrightarrow {\partial} T _ {p + q - 1} (p - 3) \\ \Bigg \downarrow \\ T _ {p + q + 1} (p, p - 1) \xrightarrow {\partial} T _ {p + q} (p - 1) \xrightarrow {} T _ {p + q} (p - 1, p - 2) \xrightarrow {\partial} T _ {p + q - 1} (p - 2) \\ \Bigg \downarrow \\ T _ {p + q} (p) \xrightarrow {} T _ {p + q} (p, p - 1) \xrightarrow {\partial} T _ {p + q - 1} (p - 1) \xrightarrow {} T _ {p + q - 1} (p - 1, p - 2) \\ \text {TnF*K} \quad E ^ {1} \quad T _ {p + q - 1} (p) \quad E ^ {1} \end{array}
$$

A complex K has two canonical filtrations by dimension:

(1) the increasing one:  $\cdots \rightarrow K_{n+1} \rightarrow K_{n} \rightarrow \cdots$

$$
\begin{array}{c} (F _ {p} K) _ {n} = \left\{ \begin{array}{l l} 0, & n > p, \\ K _ {n}, & n \leq p, \end{array} \right. \\ F _ {p} K / F _ {p - 1} K = K _ {p} [ p ] \end{array}
$$

(2) the decreasing one (the Postnikov filtration):

$$
\begin{array}{l} \dots \longrightarrow K _ {n + 2} \longrightarrow K _ {n + 1} \longrightarrow Z _ {n} \longrightarrow 0 \longrightarrow 0 \longrightarrow \dots F _ {n} K \\ \quad \Big \| \quad \Big \| \\ \dots \longrightarrow K _ {n + 2} \longrightarrow K _ {n + 1} \longrightarrow K _ {n} \longrightarrow K _ {n - 1} \longrightarrow K _ {n - 2} \longrightarrow \dots K \end{array}
$$

with

$$
\begin{array}{r l} H _ {i} (F _ {n} K) & \stackrel {\approx} {\longrightarrow} H _ {i} K \quad \text { for } \quad i \geq n \\ & = 0 \quad \text { else } \end{array}
$$

and

$$
F _ {n} K / F _ {n + 1} K \text {   is   given   by   } 0 \longrightarrow K _ {n + 1} / Z _ {n + 1} \longrightarrow Z _ {n} \longrightarrow 0,
$$

so $F_{n}K / F_{n + 1}K$ is quis to $H_{n}(K)[n]$.

## Chapter 24 Hyper-Homology Spectral Sequences

General Remark 24.1 Let $A$ be a complex. Then we have the exact

![](images/page_124_image_2.jpg)

where  $M(A \rightarrow 0)$  is the mapping cylinder of  $A \rightarrow 0$  and so is homotopy equivalent to 0, and SA is the suspension. Thus if T is a  $\partial$ -functor on K A, then we have the exact

$$
\dots \longrightarrow T _ {n} A \longrightarrow T _ {n} M \longrightarrow T _ {n} S A \longrightarrow T _ {n - 1} A \longrightarrow T _ {n - 1} M \longrightarrow \dots
$$

so $T_{n}SA \approx T_{n - 1}A$ canonically.

General Remark 24.2 Suppose $T$ is so that $T_{n}A = 0$ for all $n < 0$. Then

$$
\begin{array}{c} T _ {n} A / F _ {p} A = T _ {n - (p + 1)} (S ^ {- p - 1} A / F _ {p} A) \\ = 0 \text {if} n - (p + 1) <   0. \end{array}
$$

Thus $T_{n}A / F_{p}A = 0$ if $n \leq p$, and we have the exact

$$
\dots \longrightarrow T _ {n + 1} A / F _ {p} A \longrightarrow T _ {n} F _ {p} A \longrightarrow T _ {n} A \longrightarrow T _ {n} A / F _ {p} A \longrightarrow \dots
$$

whence

$$
\operatorname{Im} \left\{T _ {n} F _ {p} A \longrightarrow T _ {n} A \right\} = T _ {n} A \text {   for   } p > n.
$$

If moreover $F_{< 0}A = A$, then

$$
T _ {n} A / F _ {<   0} A = 0 \text {   which   implies   that   } \operatorname{Im} \{T _ {n} A / F _ {<   0} A \longrightarrow T _ {n} A \} = 0.
$$

Thus the  $E_{pq}^{1}$  spectral sequence is first quadrant and converges.

General Remark 24.3 $L_{n}F(A) = H_{n}(F(P))$ is a $\partial$-functor as in Remark 2, where $P \xrightarrow{\text{quis}} A$ is a projective resolution, since if $A$ is a chain complex, $P$ can also be chosen as a chain complex.

Now, let $K$ be a complex

$$
\dots \longrightarrow K _ {n + 1} \longrightarrow K _ {n} \longrightarrow \dots \longrightarrow K _ {0} \longrightarrow 0
$$

and  $T_{n}$  a  $\partial$ -functor on K A so that  $T_{*}$  carries quasi-isomorphisms to isomorphisms. We have the two canonical filtrations of last time.

(I) Increasing:  $F_{n}K$  is  $0 \rightarrow \cdots \rightarrow 0 \rightarrow K_{n} \rightarrow K_{n-1} \rightarrow \cdots K_{0} \rightarrow 0$  and so  $F_{n}K/$

$F_{n - 1}K = K_n[n] = S^n K_n[0]$ .We get a spectral sequence with

$$
E _ {p q} ^ {1} = T _ {p + q} (K _ {p} [ p ]) = T _ {q} (K _ {p} [ 0 ]) \text {   abutting   to   gr   } T _ {*} K.
$$

(II) Decreasing (Postnikov):  $F_{n}K$  is

$$
\begin{array}{c} \operatorname{Ker} \left\{K _ {n} \xrightarrow {\partial} K _ {n - 1} \right\} \\ \Bigg \| \\ \dots \longrightarrow K _ {n + 2} \longrightarrow K _ {n + 1} \longrightarrow Z _ {n} \longrightarrow 0 \longrightarrow 0 \longrightarrow \dots \end{array}
$$

and so $F_{n}K / F_{n - 1}K$ is

![](images/page_125_image_13.jpg)

Thus $F_{n}K / F_{n + 1}$ is quis to $H_{n}K[n]$. We get a spectral sequence with

$$
E _ {p q} ^ {2} = T _ {p + q} (F _ {q} K / F _ {q + 1} K) = T _ {p} (H _ {q} K [ 0 ]) \text {   abutting   to   } \mathrm{gr} (T _ {*} K).
$$

The spectral sequences for  $T_{<0}=0$  of (I) and (II) satisfy Remark 2 hence converge. They are called the hyper-homology spectral sequences for  $T(K)$ .

Program To apply the above to the homology of a small category C, let  $\operatorname{Hom}(\mathcal{C}, \operatorname{Ab})$  be the category of all functors  $F : C \to Ab$ , itself an abelian category. For any  $Y \in Ob C$ , we have a functor

$$
\begin{array}{c} i _ {Y}: \text { point } \longrightarrow \mathcal {C} \\ : * \longmapsto Y \end{array}
$$

which gives rise to

$$
\mathrm{Ab} = \operatorname{Hom} (\text {point}, \mathrm{Ab}) \xrightarrow [ i _ {Y *} ]{i _ {Y !}} \operatorname{Hom} (\mathcal {C}, \mathrm{Ab}),
$$

and for $A\in \mathrm{ObAb}$ , we have

$$
(i _ {Y!} A) (X) = \varinjlim_ {(*, i _ {Y *} \rightarrow X)} A (*) = \bigoplus_ {Y \rightarrow X} A,
$$

$$
(i _ {Y *} (A)) (X) = \varprojlim_ {(*, i _ {Y} (*) \leftarrow X)} A (*) = \prod_ {X \rightarrow Y} A
$$

by the Kan formulae. Moreover, by the adjunction formulae

$$
\begin{array}{r l} \operatorname{Hom} _ {\operatorname{Hom} (\mathcal {C}, \mathrm{Ab})} (i _ {Y!} A, F) & = \operatorname{Hom} _ {\mathrm{Ab}} (A, i _ {Y} ^ {*} F) \\ & = \operatorname{Hom} _ {\mathrm{Ab}} (A, F (Y)) \end{array}\tag{†}
$$

$$
\begin{array}{r l} \operatorname{Hom} _ {\operatorname{Hom} (\mathcal {C}, \mathrm{Ab})} (F, i _ {Y *} A) & = \operatorname{Hom} _ {\mathrm{Ab}} (i _ {Y} ^ {*} F, A) \\ & = \operatorname{Hom} _ {\mathrm{Ab}} (F (Y), A). \end{array}
$$

Proposition $\operatorname{Hom}(\mathcal{C},\operatorname{Ab})$ has enough projectives.

Proof The functor $F \mapsto i_{Y}^{*}F = F(Y)$ is exact. Thus if $A$ is projective, then $F \mapsto \operatorname{Hom}(A, F(Y))$ is exact, so by $(\dagger)i_{Y!}A$ is projective. Dually if $A$ is injective, then $i_{Y*}A$ is as well. Thus, we have the

General Principle If $f:\mathcal{A}\to\mathcal{B}$ is an additive functor between abelian categories having an exact right adjoint $g$, then $f$ carries projectives into projectives.

Now, note that if we are given a surjection  $A \twoheadrightarrow F(Y)$ , then the induced map

$$
i _ {Y!} (A) \longrightarrow F
$$

is surjective when applied to Y since

![](images/page_127_image_1.jpg)

Thus for X = Y with  $u = id_{Y}$  we get surjectivity.

We conclude that if we choose for each $Y \in \operatorname{Ob}\mathcal{C}$ a projective $P_{Y} \twoheadrightarrow F(Y)$, which is possible since Ab has enough projectives, then we get a surjection

$$
\bigoplus_ {Y \in \mathrm{Ob}   \mathcal {C}} i _ {Y!} P _ {Y} \twoheadrightarrow F  ,
$$

as desired.

Now, $f:\mathcal{C}\to \mathcal{C}'$ induces

$$
f _ {!}: \operatorname{Hom} (\mathcal {C}, \mathrm{Ab}) \longrightarrow \operatorname{Hom} (\mathcal {C} ^ {\prime}, \mathrm{Ab}),
$$

which is a right exact functor since $\operatorname{Hom}(f_{!}F,G) = \operatorname{Hom}(F,f^{*}G)$ and because of the

Proposition The sequence $A' \to A \to A'' \to 0$ is exact if and only if for all $B$, $0 \to \operatorname{Hom}(A'', B) \to \operatorname{Hom}(A, B) \to \operatorname{Hom}(A', B)$ is, where $A, A', A''$ and $B$ are in some abelian category.

Proof Exercise.

Thus given $F' \to F \to F'' \to 0$ exact in $\operatorname{Hom}(\mathcal{C}, \operatorname{Ab})$, we get the exact

$$
\begin{array}{c} \operatorname{Hom} (F ^ {\prime}, f ^ {*} G) \longleftarrow \operatorname{Hom} (F, f ^ {*} G) \longleftarrow \operatorname{Hom} (F ^ {\prime \prime}, f ^ {*} G) \longleftarrow 0 \\ \Big \| \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \operatorname{Hom} (f _ {!} F ^ {\prime}, G) \longleftarrow \operatorname{Hom} (f _ {!} F, G) \longleftarrow \operatorname{Hom} (f _ {!} F ^ {\prime \prime}, G) \longleftarrow 0 \end{array}
$$

so that $f_{!}F^{\prime}\to f_{!}F\to f_{!}F^{\prime \prime}$ is exact.

In particular, if $f:\mathcal{C}\to$ point, then

$$
(f _ {!} F) (*) = \varinjlim_ {(X, f X \rightarrow *)} F (X) = \varinjlim_ {\mathcal {C}} A (X).
$$

Now given any complex $F$. bounded below, we choose a projective resolution $P \to F$. and define

$$
(L _ {q} f _ {!}) (F _ {.}) = H _ {q} \{f _ {!} P _ {.} \}
$$

where $f: \mathcal{C} \to \mathcal{C}'$, $P$. and $F$. in $C_{+}(\operatorname{Hom}(\mathcal{C}, \operatorname{Ab}))$, $f_{!}(P)$ in $C_{+}(\operatorname{Hom}(\mathcal{C}', \operatorname{Ab}))$ and $(L_{q} f_{!})(F)$ in $\operatorname{Hom}(\mathcal{C}', \operatorname{Ab})$ for each $q$. We regard $F$ in $\operatorname{Hom}(\mathcal{C}, \operatorname{Ab})$ as the complex $F[0]$, and we write

$$
(L _ {q} f _ {!}) (F) = (L _ {q} f _ {!}) (F [ 0 ]).
$$

Finally,  $T_{n} = L_{n} f_{!}$  is a  $\partial$ -functor which inverts quasi-isomorphisms, so we get the hyper-homology spectral sequences convergent by Remark 3 with

$$
E _ {p q} ^ {1} = (L _ {q} f _ {!}) (F _ {p}) \text {   converging   to   } \operatorname{gr} L _ {*} f _ {!} (F _ {.})
$$

and

$$
E _ {p q} ^ {2} = (L _ {p} f _ {!}) (H _ {q} (F.)) \text {   converging   to   } \mathrm{gr} L _ {*} f _ {!} (F.)  .
$$

Example (where these sequences collapse) Assume that $F_{q}$ is acyclic for $f_{!}$, i.e., $(L_{q}f_{!})(F_{p} = \left\{ \begin{array}{ll}0, & \text{for } q \neq 0, \\ f_{!}F_{q}, & \text{for } q = 0. \end{array} \right.$

We find

$$
\begin{array}{c} 0 \\ q \quad f _ {!} F _ {0} f _ {!} F _ {1} f _ {!} F _ {2} \dots \\ p \end{array}
$$

and check easily that

$$
\begin{array}{c} d ^ {1}: E _ {p q} ^ {1} \longrightarrow E _ {p - 1, q} ^ {1} \\ \Big \| \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \Big \| \\ T _ {q} F _ {p} \qquad \qquad \qquad \qquad T _ {q} F _ {p - 1} \end{array}
$$

is induced by  $F_{p} \xrightarrow{d} F_{p-1}$ .

Thus $d^1$ is the only non-zero differential, and

$$
\begin{array}{l} E _ {* 0} ^ {1} = f _ {!} F _ {*}, \\ E _ {* q} ^ {1} = 0 \quad \text { for } q \neq 0, \end{array}
$$

SO

$$
E _ {p q} ^ {2} = \left\{ \begin{array}{c c} 0, & \text { if } q \neq 0, \\ H _ {p} (f _ {!} F _ {.}), & \text { if } q = 0, \end{array} \right.
$$

and we conclude

$$
(L _ {p} f _ {!}) (F.) = H _ {p} (f _ {!} (F.))
$$

whenever all  $F_{n}$  are acyclic for  $f_{!}$ .

Suppose that $\mathcal{C} \xrightarrow{f} \mathcal{C}'$ is a functor between small categories. We have

![](images/page_130_image_1.jpg)

and by the Kan formula

$$
(f _ {!} F) (Y) = \varinjlim_ {(X, f X \to Y) \in f / Y} F (X).
$$

Moreover, the adjunction formula says that

$$
\operatorname{Hom} (f _ {!} F, G) = \operatorname{Hom} (F, f ^ {*} G),\tag{*}
$$

and we saw that F projective implies  $f_{1}$  F projective.

Let $\mathcal{A} = \operatorname{Funct}(\mathcal{C},\mathrm{Ab})$, $M_{\cdot}\in C_{+}(\mathcal{A})$, and $\mathbb{L}f_1(M.) = f_1(P.)$, where $P_{\cdot}\to M$ is a projective resolution, and then $(L_qf_1)(M.) = H_q(\mathbb{L}f_1(M.))$ is a $\partial$-functor carrying quasi-isomorphisms to isomorphisms. This last is true since if we have

$$
\begin{array}{c} P. \xrightarrow {\text {quis}} M. \\ P ^ {\prime}. \xrightarrow {\text {quis}} M ^ {\prime}. \end{array}
$$

then $P$. is a projective resolution of $M'$, and the map $P \to P'$ making the diagram commute is a homotopy equivalence.

Recall the two spectral sequences

$$
E _ {p q} ^ {1} = L _ {q} f _ {!} (M _ {p}) \text {   converging   to   } \mathrm{gr} \{L _ {*} f _ {!} (M.) \},
$$

$$
E _ {p q} ^ {2} = L _ {p} f _ {!} (H _ {q} (M.)) \text {   converging   to   } \mathrm{gr} \{L _ {*} f _ {!} (M.) \}.
$$

Note that if $F \in \mathcal{A}$, then

$$
\begin{array}{r l} L _ {q} f _ {!} (F) & = L _ {q} f _ {!} (F [ 0 ]) \\ & = \left\{ \begin{array}{l l} f _ {!} F, & \text { if } q = 0, \\ 0, & \text { if } q <   0. \end{array} \right. \end{array}
$$

This is true since we construct

$$
\dots \longrightarrow P _ {1} \longrightarrow P _ {0} \longrightarrow F \longrightarrow 0
$$

and

$$
\begin{array}{r l} L _ {q} f _ {!} (F) & = H _ {q} (\dots \longrightarrow f _ {!} P _ {1} \longrightarrow f _ {!} P _ {0} \longrightarrow 0 \longrightarrow \dots) \\ & = f _ {!} F \end{array}
$$

in degree zero since  $f_{1}$  is right exact by the adjunction formula (\*).

If all the  $M_{p}$  are acyclic for  $f_{!}$ , then the first spectral sequence collapses and gives

$$
E _ {p q} ^ {1} = \left\{ \begin{array}{c c} 0, & \text {if} q \neq 0, \\ f _ {!} M _ {p}, & \text {if} q = 0, \end{array} \right.
$$

and

$$
E _ {p q} ^ {\infty} = E _ {p q} ^ {2} = \left\{ \begin{array}{c c} 0, & \text { if } q \neq 0, \\ H _ {p} (f _ {!} M.), & \text { if } q = 0, \end{array} \right.
$$

so that  $H_{p}(f_{!}M)=L_{p}f_{!}(M)$ .

In other words, when all the $M_{p}$ are $f_{!}$-acyclic, we have that the projective resolution $P_{\cdot} \to M_{\cdot}$ induces a quis $f_{!} P_{\cdot} \to f_{!} M_{\cdot}$, and so in this case we find the quis $\mathbb{L} f_{!}(M_{\cdot}) \to f_{!}(M_{\cdot})$.

Consider now  $C \stackrel{f}{\rightarrow} C' \stackrel{g}{\rightarrow} C''$ . We claim that  $g_{!} f_{!} = (gf)_{!}$ . This follows since

$$
\begin{array}{r l} \operatorname{Hom} ((g f) _ {!} F, A) & = \operatorname{Hom} (F, (g f) ^ {*} A) \\ & = \operatorname{Hom} (F, f ^ {*} g ^ {*} A) \\ & = \operatorname{Hom} (g _ {!} f _ {!} F, A), \end{array}
$$

and so Yoneda implies that $(gf)_! (F) \cong g_! f_! (F)$.

Suppose we have $\mathcal{C} \xrightarrow{f} \mathcal{C}' \xrightarrow{g}$ point. Then

$$
g _ {!} G = \varinjlim_ {\mathcal {C} ^ {\prime}} G,
$$

$$
(g f)! F = \varinjlim_ {\mathcal {C}} F.
$$

In this case we write $H_q(\mathcal{C}, F)$ instead of $L_q(gf)_! (F)$ and $H_q(\mathcal{C}', G)$ instead of $L_q g_! (G)$.

Suppose $M. \in C_{+}(\text{Func}(\mathcal{C}, \text{Ab}))$ and choose $P. \xrightarrow{\text{quis}} M$. Then

$$
\begin{array}{r l} \mathbb {L} (g f) _ {!} (M.) & = (g f) _ {!} (P.) \\ & = g _ {!} f _ {!} (P). \end{array}
$$

Now, $f_{!}(P)$ is a complex of projectives, and projectives are acyclic for $f_{!}$. Thus

$$
\mathbb {L} g _ {!} (f _ {!} P.) \xrightarrow {\text {quis}} g _ {!} (f _ {!} P.).
$$

We conclude that

$$
\boxed {\mathbb {L} (g f) _ {!} (M.) \xleftarrow {\text {quis}} \mathbb {L} g _ {!} (\mathbb {L} f _ {!} (M.))}
$$

Taking homology, we get

$$
H _ {q} (\mathbb {L} (g f) _ {!} (M.)) = L _ {q} (g f) _ {!} (M.) = H _ {q} (\mathcal {C}, M.),
$$

so we find

$$
H _ {q} (\mathcal {C}, M.) = H _ {q} \left(\mathcal {C} ^ {\prime}, \mathbb {L} f _ {!} (M.)\right).
$$

Thus the spectral sequence resulting from the Postnikov filtration is

$$
E _ {p q} ^ {2} = H _ {p} \left(\mathcal {C} ^ {\prime}, L _ {q} f _ {!} (M.)\right) \text { converging   to } \operatorname{gr} \left\{H _ {*} \left(\mathcal {C} ^ {\prime}, \mathbb {L} f _ {!} (M.)\right) \right\},
$$

and we obtain the Leray spectral sequence in homology for $f:\mathcal{C}\to\mathcal{C}'$ with

$$
E _ {p q} ^ {2} = H _ {p} (\mathcal {C} ^ {\prime}, L _ {q} f _ {!} (M.)) \text {   converging   to   } \mathrm{gr} H _ {*} (\mathcal {C}, M.)
$$

(†) Problem Generalize the Kan formula to  $(L_{q} f_{!}(M.))(Y)=H_{q}(f/Y,i^{*}M.)$ , where  $\mathrm{Ob}(f/Y)=\{(X,fX\xrightarrow{u}Y)\}$  and  $i:f/Y\to C$  sends  $(X,u)$  to X.

Now,

$$
\begin{array}{r l} L _ {q} f _ {!} (M.) (Y) & = H _ {q} (f _ {!} P.) (Y) \\ & = H _ {q} ((f _ {!} P.) (Y)) \\ & = H _ {q} (\varinjlim_ {(X, u) \in f / Y} P. (X)) \\ & = H _ {q} (\varinjlim_ {f / Y} i ^ {*} P.)  . \end{array}
$$

Moreover,

$$
H _ {q} (f / Y, i ^ {*} M.) = H _ {q} (\varinjlim_ {f / Y} Q.),
$$

where Q is a projective resolution of  $i^{*}M$ . in  $C_{+}(\text{Func}(f/Y, \text{Ab}))$ , thus the problem ( $\dagger$ ) becomes:

Problem If  $P_{*} \rightarrow M_{*}$  is a projective resolution, then  $i^{*}P_{*} \rightarrow i^{*}M_{*}$  is a quis since  $i^{*}$  is an exact functor. Is  $i^{*}P_{*}$  a complex of projectives?

If so, then take $Q. = i^{*}P$. Note that it would be enough to know that each $i^{*}P_{q}$ is acyclic for $\varinjlim_{f/Y}$.

Claim That  $i^{*}$  carries projectives to projectives. This would follow if we could exhibit an exact right adjoint to  $i^{*}$  as before. We show that  $i_{*}$  is exact. Recall that

$$
\begin{array}{c} i: f / Y \longrightarrow \mathcal {C} \\ : (X, u) \longmapsto X. \end{array}
$$

Clearly then $f/Y$ is the fibered category with discrete fibers over $\mathcal{C}$ associated to the contravariant functor $X\to\mathrm{Hom}_{\mathcal{C}}(fX,Y)$. Recall that if $i$ is fibered, then

$$
\begin{array}{l} (i _ {*} F) (X) = \underset {(Z, X \xrightarrow {u} i Z) \in X \backslash i} {\lim} F (Z) \\ = \underset {Z \in i ^ {- 1} X} {\lim} F (Z) \\ = \prod_ {Z \in \mathrm{Ob} i ^ {- 1} (X)} F (Z) \text { since   the   fibers   are   discrete }, \end{array}
$$

which is clearly exact in F. This proves the claim and the

General Fact If $\widetilde{\mathcal{C}}\stackrel{i}{\to}\mathcal{C}$ is a fibered category with discrete fibers, then $i_{*}$ is exact and $i^{*}$ carries projectives to projectives.

We have in fact proved the

Generalized Kan Formula  $L_{q} f_{!}(M.)(Y) = H_{q}(f/Y, i^{*}M).$

Now recall that if $f$ is pre-cofibered, then the Kan formula simplifies to

$$
\begin{array}{r l} (f _ {!} F) (Y) & = \varinjlim_ {(X, f X \to Y)} F (X) \\ & = \varinjlim_ {X \in f ^ {- 1} Y} F (X). \end{array}
$$

Immediate Goal If $f$ is pre-cofibered, then

$$
\begin{array}{r l} L _ {q} f _ {!} (M.) (Y) & = H _ {q} (f / Y, i ^ {*} M.) \\ & = H _ {q} (f ^ {- 1} Y, M. \text { restricted   to } f ^ {- 1} (Y)) \\ & = H _ {q} (f ^ {- 1} Y, j ^ {*} (i ^ {*} M)). \end{array}
$$

Recall that we have

$$
u _ {*} X \longleftarrow (f ^ {X} X \stackrel {u} {\rightarrow} Y)
$$

$$
f ^ {- 1} Y \xrightarrow [ j ]{r} f / Y
$$

$$
u \longmapsto (u, f u \stackrel {\mathrm{id}} {=} Y).
$$

Thus when $f$ is pre-cofibered, the embedding $j: f^{-1}Y \to f / Y$ has left adjoint $r$.

For the immediate goal, it suffices to prove that

$$
H _ {q} (f / Y, G.) = H _ {q} (f ^ {- 1} Y, j ^ {*} G.).
$$

$$
\text { Suppose   that } j ^ {*} = r _ {!}
$$

Then

$$
\begin{array}{c} H _ {p} (f / Y, G.) = H _ {p} (f ^ {- 1} Y, \mathbb {L} r _ {!} G.) \\ (\text { since } r _ {!} = j ^ {*} \text { is   exact }) = H _ {p} (f ^ {- 1} Y, r _ {!} G.) \\ (\text { by   supposition }) = H _ {p} (f ^ {- 1} Y, j ^ {*} G.), \end{array}
$$

as desired.

Whether the boxed supposition is correct will be determined next time.

# Chapter 26 The Hochschild–Serre Spectral Sequence

Suppose we have adjoint functors  $C \xrightarrow{g} C'$ . Recall that

$$
h ^ {X}: T \mapsto \operatorname{Hom} _ {\mathcal {C}} (X, T)
$$

and consider the category $\widehat{\mathcal{C}} = \operatorname{Func}(\mathcal{C},\text{Sets})$.

Claim $g_{!}h^{X}=h^{g^{X}}$.

Proof

$$
\begin{array}{r l} \operatorname{Hom} _ {\hat {C}} (g _ {!} h ^ {X}, G) & = \operatorname{Hom} _ {\hat {C}} (h ^ {X}, g ^ {*} G) \\ (\text { by   Yoneda }) & = (g ^ {*} G) (X) \\ & = G (g X) \\ (\text { by   Yoneda }) & = \operatorname{Hom} _ {\hat {C}} (h ^ {g ^ {X}}, G) \end{array}
$$

and finally, by Yoneda again  $g_{!}h^{X}=h^{g^{X}}$

Now,

$$
\begin{array}{r l} (g _ {!} h ^ {X}) (Y) & = h ^ {g ^ {X}} (Y) = \operatorname{Hom} _ {\mathcal {C}} (g X, Y) \\ & = \operatorname{Hom} _ {\mathcal {C}} (X, f Y) \\ & = h ^ {X} (f Y) \\ & = (f ^ {*} h ^ {X}) (Y), \end{array}
$$

and therefore $g_{!}h^{X} = f^{*}h^{X}$, so $g_{!}$ and $f^{*}$ agree on functors of the form $h^{X}$.

Now, let $F \in \widehat{\mathcal{C}}$ be any functor. Then form the category

$$
\mathcal {C} _ {F} = \{(X, \xi): \xi \in F (X) \},
$$

i.e., $\mathcal{C}_F$ is the cofibered category with discrete fibers belonging to $F$. Then Yoneda says $\xi \in F(X) = \operatorname{Hom}(h^X, F)$, and we claim

$$
\varinjlim_ {(X, \xi) \in \mathcal {C} _ {F}} h ^ {X} \stackrel {{\sim}} {{\longrightarrow}} F.
$$

The proof of this is an exercise as follows. Evaluate on an object Y and identify, or use Yoneda and look at  $\operatorname{Hom}(F, G)$ .

Now,  $g_{!}$  preserves inductive limits because it has a right adjoint since

$$
\begin{array}{r l} \operatorname{Hom} (g _ {!} \varinjlim_ {i} F _ {i}, G) & = \operatorname{Hom} (\varinjlim_ {i} F _ {i}, g ^ {*} G) \\ & = \varprojlim \operatorname{Hom} (F _ {i}, g ^ {*} G) \\ & = \varprojlim \operatorname{Hom} (g _ {!} F _ {i}, G) \\ & = \operatorname{Hom} (\varinjlim g _ {!} F _ {i}, G), \end{array}
$$

and finally, by Yoneda, the claim follows.

By the same argument,  $f^{*}$  preserves inductive limits.

Putting all this together,

$$
g _ {!} (F) = f ^ {*} (F), \quad \text { for   all } F \in \widehat {\mathcal {C}}.
$$

Thus, given  $C \xrightarrow{g} C'$ , we have

$$
\widehat {\mathcal {C}} \xrightarrow [ g ^ {*} = f _ {*} ]{f _ {!}} \widehat {\mathcal {C} ^ {\prime}}.
$$

In this situation where  $g_{!} = f^{*}$ , then  $g_{!}$  on abelian group-valued functors is the same as  $g_{!}$  on set valued functors. If F is abelian group-valued, then we have

$$
+: F \times F \longrightarrow F
$$

and

$$
\begin{array}{l} g _ {!} (F \times F) \longrightarrow g _ {!} F \\ \Bigg | \text { and   this   map   is   an   isomorphism   when } \\ g _ {!} = f ^ {*} \text { since } f ^ {*} \text { preserves   products. } \\ g _ {!} F \times g _ {!} F \end{array}
$$

For derived functors, $\mathbb{L}g_{!}$ is quis to $g_{!}$ since on $\operatorname{Func}(\mathcal{C},\mathrm{Ab})$, $g_{!}$ is exact.

Suppose $\mathcal{C} \xrightarrow{f} \mathcal{C}'$ and $M. \in C_{+}(\text{Func}(\mathcal{C}, \text{Ab}))$. Last time we saw that

(\*)

$$
H _ {n} (\mathcal {C} ^ {\prime}, \mathbb {L} f _ {!} (M)) = H _ {n} (\mathcal {C}, M).
$$

Moreover, we can show that

$$
\mathbb {L} \underset {\overrightarrow {c ^ {\prime}}} {\lim} \circ \mathbb {L} f _ {!} (M.) = \mathbb {L} \underset {\overrightarrow {c}} {\lim} (M.).
$$

On the other hand,

$$
E _ {p q} ^ {2} = H _ {p} \left(\mathcal {C} ^ {\prime}, L _ {q} f _ {!} (M.)\right) \text { converges   to } \operatorname{gr} \left\{H _ {n} \left(\mathcal {C} ^ {\prime}, \mathbb {L} f _ {!} (M.)\right) \right\},
$$

and we proved the generalized Kan formula

$$
L _ {q} f _ {!} (M.) (Y) = H _ {q} (f / Y, i ^ {*} M.)
$$

where $i:f / Y\to \mathcal{C}$ is the natural map.

Now suppose $f$ is pre-cofibered. We have

$$
f ^ {- 1} (Y) \xrightarrow [ j ]{r} f / Y\tag{†}
$$

where $j$ is the embedding, $r(X, fX \xrightarrow{u} Y) = u^{*}X$ and $r$ is left adjoint to $j$ so that $r_{!} = j^{*}$ and $\mathbb{L} r_{!} = r_{!}$, thus resolving a question from last time.

Thus, by (\*) applied to (†), we get

$$
\begin{array}{r l} H _ {n} (f / Y, i ^ {*} M.) & = H _ {n} (f ^ {- 1} (Y), \mathbb {L} r _ {!} (i ^ {*} M.)) \\ & = H _ {n} (f ^ {- 1} (Y), j ^ {*} i ^ {*} M). \end{array}
$$

Notice that  $j^{*}i^{*}M$ . is just M. restricted to  $f^{-1}(Y)$ .

Conclusion When $f$ is pre-cofibered, we have

$$
L _ {q} f _ {!} (M.) (Y) = H _ {q} \left(f ^ {- 1} (Y), M. \text { restricted   to } f ^ {- 1} (Y)\right).
$$

Exercise

$$
\mathbb {L} f _ {!} (M.) (Y) = \mathbb {L} \varinjlim_ {f ^ {- 1} (Y)} (M. \text { restricted   to } f ^ {- 1} (Y)).
$$

Example Given a group extension

$$
* \longrightarrow N \longrightarrow G \longrightarrow Q \longrightarrow *,
$$

we have $\widetilde{G} \xrightarrow{f} \widetilde{Q}$, and $f$ is clearly cofibered and fibered with fiber $f^{-1}(*) = \widetilde{N}$, where $\widetilde{X}$ is the category associated to each $X = G$, $Q, N$. As usual, a $G$-module is a functor from $\widetilde{G}$ to Ab. We have

$$
\begin{array}{r l} H _ {*} (\widetilde {G}, M) & = \text { group   homology   of } G \text { with   values   in } M \\ & = H _ {*} (G, M), \end{array}
$$

and we get a spectral sequence

$$
E _ {p q} ^ {2} = H _ {p} (\widetilde {Q}, L _ {q} f _ {!} (M)) \text { converging   to } \operatorname{gr} H _ {n} (\widetilde {G}, M.) = \operatorname{gr} H _ {n} (G, M)
$$

and

$$
H _ {p} (\widetilde {Q}, L _ {q} f _ {!} (M)) = H _ {p} (Q, H _ {q} (N, M)).
$$

This is the Hochschild–Serre spectral sequence

$$
E _ {p q} ^ {2} = H _ {p} (Q, H _ {q} (N, M)) \text {   converging   to   } \operatorname{gr} H _ {n} (G, M)  .
$$

Example Take a map  $K \rightarrow L$  of simplicial complexes and consider the functor

$$
\operatorname{Simp} (K) \xrightarrow {f} \operatorname{Simp} (L),
$$

where we take geometric realization of the poset $\operatorname{Simp}(K)$ of simplices in $K$ under inclusion to get the barycentric subdivision, as before. Then

$$
H _ {*} (\operatorname{Simp} (K), A) = H _ {*} (K, A),
$$

where the left-hand side has an abelian group A regarded as a constant functor, and the right-hand side is the usual homology of the simplicial complex with coefficients in A. Associated to f is a spectral sequence

$$
E _ {p q} ^ {2} = H _ {p} (\operatorname{Simp} (L), L _ {q} f _ {!} (A \text {   on   } \operatorname{Simp} K))
$$

converging to $H_{n}(\text{Simp } K, A \text{ on Simp}(K))$. We showed before that $f$ is fibered, and the fiber is

$$
f ^ {- 1} (T) = \{\text { all   simplexes   mapping   onto } T \}.
$$

(Open) Problem Show that the simplicial complex belonging to  $f^{-1}(T)$  is a triangulation of the inverse image of any interior point of T.

If so, then we have the spectral sequence

$$
E _ {p q} ^ {2} = H _ {p} (\text { Simp   } L, T \mapsto H _ {q} (f ^ {- 1} (T), A)) \text {   converging   to   } H _ {p} (\text { Simp   } K, A)  .
$$

Here we use contravariant functors, whence we have

$$
\begin{array}{c} L _ {q} f _ {!} (F) (Y) = H _ {q} (Y \backslash f, F) \\ (\text { for   } f \text {   pre - fibered }) = H _ {q} (f ^ {- 1} (Y), F). \end{array}
$$

## Variants

(1) contravariant functors,

(2) cohomology: for $f: \mathcal{C} \to \mathcal{C}'$, we have $f_{*}: \operatorname{Func}(\mathcal{C}, \mathrm{Ab}) \to \operatorname{Func}(\mathcal{C}', \mathrm{Ab})$ which is left exact, i.e., $0 \to F' \to F \to F''$ exact implies $0 \to f_{*}F' \to f_{*}F \to f_{*}F''$ exact. Using injective resolutions, define

$$
\mathbb {R} f _ {*} (M.), \quad \text { for } M \in C ^ {*} (\operatorname{Func} (\mathcal {C}, \mathrm{Ab})).
$$

Exercise Figure out when it happens that

$$
\mathbb {R} f _ {*} (M.) (Y) = H ^ {q} (f ^ {- 1} (Y), M).
$$

## Chapter 27 Resolution for Exact Categories

Consider an additive full subcategory M of an additive category A with its induced notion of exact sequences  $0 \rightarrow M' \rightarrow M \rightarrow M'' \rightarrow 0$  inherited from A. Then M is an exact category provided it is closed under extensions in A, i.e., if  $M', M''$  are objects in M, then so too is M. We can cook up an axiomatic notion of such, but it is not worth it here. Note that the set of projective modules is an exact but not an abelian category.

Example (of properties of exact sequences)

![](images/page_140_image_3.jpg)

Then the vertical left-hand sequence is exact if the right-hand one is because $\mathcal{M}$ is closed under extensions $N\times_{M^{\prime \prime}}M\in \mathcal{M}$ and similarly for push-outs of the first term of the exact sequence.

Given an exact category M, a map  $M \rightarrow M'$  is an admissible monomorphism if it is part of an exact sequence  $0 \rightarrow M \rightarrow M' \rightarrow M'' \rightarrow 0$  in M, and similarly for an admissible epimorphism. An admissible filtration of M is a filtration

$$
0 = F _ {- 1} M \subset F _ {0} M \subset \dots \subset F _ {n} M = M
$$

so that each $F_{p-1}M \subset F_pM$ is an admissible monomorphism.

Note that composition of admissible monomorphisms is admissible since the cokernel of the composition is an extension of the respective cokernels.

Resolution Theorem Given an exact category $\mathcal{M}$ and a full subcategory $\mathcal{P}$ closed under extensions in $\mathcal{M}$. Assume that

(i) if $0 \to M' \to P \to P' \to 0$ is exact in $\mathcal{M}$ and $P, P' \in \mathcal{P}$ implies also that $M' \in \mathcal{P}$; note that the kernel of maps between projectives is itself projective.

(ii) for any $M \in \mathcal{M}$, there exists an admissible exact sequence

$$
0 \longrightarrow P _ {n} \longrightarrow \dots \longrightarrow P _ {1} \longrightarrow P _ {0} \longrightarrow M \longrightarrow 0\tag{*}
$$

so that $P_{i} \in \mathcal{P}$, where admissible here means that each associated short exact sequence is admissible.

Then $K_0\mathcal{P}\to K_0\mathcal{M}$ is an isomorphism.

Proof It remains (from last time) to show that given (\*), then

$$
\sum (- 1) ^ {i} [ P _ {i} ] \in K _ {0} \mathcal {P}
$$

is independent of the resolution.

Suppose we have resolutions

$$
0 \longrightarrow P _ {n} \longrightarrow \dots \longrightarrow P _ {0} \longrightarrow M \longrightarrow 0
$$

$$
0 \longrightarrow P _ {n} ^ {\prime} \longrightarrow \dots \longrightarrow P _ {0} ^ {\prime} \longrightarrow M \longrightarrow 0
$$

where without loss of generality we take them to have same length by adding zeros if necessary. Construct the fiber product

![](images/page_141_image_17.jpg)

and get another resolution of $M$, which may however not be in $\mathcal{P}$; if it were, then we would be done by considering the kernel of $P_{.} \times P_{.}' \to P$. and showing it is in $\mathcal{P}$ using (i) above.

More formally, we require the

Lemma Consider an exact sequence

$$
0 \longrightarrow K. \longrightarrow Q. \longrightarrow P. \longrightarrow 0,
$$

of finite complexes in $\mathcal{M}$, where $\mathcal{M}$ satisfies condition (i) above, so that each $Q_{i}$ and $P_{i}$ are in $\mathcal{P}$ and so that $K$. is acyclic. Then we have

$$
\sum (- 1) ^ {i} [ Q _ {i} ] = \sum (- 1) ^ {i} [ P _ {i} ] \in K _ {0} \mathcal {P}.
$$

Proof Condition (i) implies that each  $K_{i} \in P$  since  $0 \rightarrow K_{n} \rightarrow \cdots \rightarrow K_{0} \rightarrow 0$  is exact, and K. is admissible in P, so

$$
\sum (- 1) ^ {i} \left[ K _ {i} \right] = 0 = \sum (- 1) ^ {i} \left(\left[ Q _ {i} \right] - \left[ P _ {i} \right]\right).
$$

Now, define  $P_{n}$  to be the subcategory of M consisting of elements of M having a resolution (\*) of length at most n with each  $P_{i} \in P$ . We therefore have  $P = P_{0} \subset P_{1} \subset \cdots \subset \bigcup_{n} P_{n} = M$ .

We prove  $K_{0}P_{0}\stackrel{\sim}{\longrightarrow}K_{0}P_{1}$ , i.e., suppose  $M\in P_{1}$  and we have

![](images/page_142_image_10.jpg)

Thus $P_0 \times_M P_0'$ is an extension of $P_1$ by $P_0'$, and hence $P_0 \times_M P_0' \in \mathcal{P}$, as desired. Clearly

$$
\begin{array}{c} {[ P _ {0} ] - [ P _ {1} ] = [ P _ {0} ] - [ P _ {0} \times_ {M} P _ {0} ^ {\prime} ] + [ P _ {0} ^ {\prime} ]} \\ {= [ P _ {0} ^ {\prime} ] - [ P _ {1} ^ {\prime} ].} \end{array}
$$

To finish the argument, we must show that  $P_{n}$  is closed under extensions, that  $0 \rightarrow M' \rightarrow M \rightarrow M'' \rightarrow 0$  is exact in  $P_{n}$  and also that  $M''$ ,  $M \in P_{n-1}$  and  $M' \in P_{n}$  implies  $M' \in P_{n-1}$ . See Quillen's paper; these are straightforward but tedious.

This proves the theorem.

Here is the proof that  $P_{n}$  is closed under extensions for n = 2. Suppose we have the diagram

![](images/page_143_image_3.jpg)

where $K, P \in \mathcal{P}$ with $0 \to M' \to M \to M'' \to 0$ exact. It suffices to show that $R \in \mathcal{P}$, i.e.,

$$
0 \longrightarrow R \longrightarrow P \longrightarrow M ^ {\prime} \longrightarrow 0
$$

with $P \in \mathcal{P}$ and $M' \in \mathcal{P}_1$ implies that $R \in \mathcal{P}$. But we have

![](images/page_143_image_7.jpg)

so indeed  $R \in P$  as desired.

Corollary Let A be a regular noetherian ring, i.e., every finitely generated module has a finite resolution by finitely generated projective A-modules, e.g.,  $A = k[T_{1}, \ldots, T_{n}]$  by the Szyzygy Theorem.

Then recall that $K_0 A = K_0 \mathcal{P}_A$. By the Resolution Theorem, $K_0 \mathcal{P}_A \xrightarrow{\sim} K_0 \operatorname{Modf}(A)$. (This is also true for $A[T]$; the proof of Szyzygy Theorem says $A[T]$ is regular, Quillen thinks.)

Example If A is noetherian, then the collection of finitely generated A-modules is an abelian category. Let S be a multiplicative system in A and form  $S^{-1}A$ . We have

![](images/page_144_image_2.jpg)

A thick (or Serre) subcategory of an abelian category A is a full subcategory which is closed under sub-objects, quotient objects and extensions, for example,  $B \subset A$ .

Now, given a thick subcategory $\mathcal{B} \subset \mathcal{A}$, we call a map $f: M \to N$ in $\mathcal{A}$ an isomorphism mod $\mathcal{B}$ if $\operatorname{Ker} f$ and $\operatorname{Cok} f$ are in $\mathcal{B}$.

Define A/B to be the category with the same objects as A but in which the arrows are obtained from the arrows in A by formally adjoining inverses for all isomorphisms mod B.

In our particular case, any  $M \rightarrow N$  in A/B can be represented by a diagram

![](images/page_144_image_7.jpg)

where s is an isomorphism mod B and  $f: M' \rightarrow N$  is in A, so we have

![](images/page_144_image_9.jpg)

and  $fs^{-1} = f_{1}s_{1}^{-1}$  when there exists an  $M''$  dominating the both of them.

Composition is given by

![](images/page_145_image_1.jpg)

Fact $\mathcal{A} / \mathcal{B}$ is an abelian category. The functor $\mathcal{A} \to \mathcal{A} / \mathcal{B}$ is exact, and $\mathcal{B}$ is exactly the set of objects killed by this functor.

Suppose now $V$ is in $\operatorname{Modf}(S^{-1}A)$. Then $V = S^{-1}M$, where $M$ is in $\operatorname{Modf} A$, and consider

$$
\operatorname{Hom} _ {S ^ {- 1} A} (S ^ {- 1} M, S ^ {- 1} N).
$$

Then we have

![](images/page_145_image_6.jpg)

by "clearing denominators", whence

Modf  $S^{-1}A \equiv \text{Modf } A/(S - torsion finitely generated modules)$ .

Preview There is a basic exact sequence

$$
K _ {1} \mathcal {A} / \mathcal {B} \longrightarrow K _ {0} \mathcal {B} \longrightarrow K _ {0} \mathcal {A} \longrightarrow K _ {0} \mathcal {A} / \mathcal {B} \longrightarrow 0.
$$

Theorem If $A$ is a regular noetherian ring, then $K_{0}A \cong K_{0}A[T]$.

## Ingredients of Proof

1: Because A is regular noetherian, which implies that  $A[T]$  is regular noetherian as well, we have  $K_{0} \mathcal{P}_{A} = K_{0}(\text{Modf } A)$ , and moreover Modf A is an abelian category, and similarly for  $A[T]$ .

2: Localization Theorem: If B is a Serre subcategory of the abelian category A, then we have the exact sequence

$$
K _ {0} \mathcal {B} \longrightarrow K _ {0} \mathcal {A} \longrightarrow K _ {0} (\mathcal {A} / \mathcal {B}) \longrightarrow 0.
$$

Put  $B = A[T_{0}, T_{1}]$ , a ring graded by degree. Take A to be all finitely generated graded B-modules, e.g.,  $M = \bigoplus_{n \geq 0} M_{n}$ , so  $B = \bigoplus_{n \geq 0} B_{n}$  where  $B_{n} = AT_{0}^{n} + \cdots + AT_{1}^{n}$  and check this is an abelian category by classical results. Consider

$$
B \left[ T _ {0} ^ {- 1} \right] = A \left[ T _ {1} \right] \otimes_ {A} A \left[ T _ {0}, T _ {0} ^ {- 1} \right],
$$

where $A[T_0, T_0^{-1}]$ is the collection of Laurent polynomials. If $M = \bigoplus_{n \geq 0} M_n$, then $M[T_0^{-1}] = \widetilde{M} \otimes_A A[T_0, T_0^{-1}] = \bigoplus_{n \geq 0} \widetilde{M} T_0^n$, where $\widetilde{M}$ is the degree zero part of $M[T_0^{-1}]$, i.e., $\widetilde{M} = \varinjlim \{M_n \xrightarrow{\times T_0} M_{n+1}\}$.

3: Conclude that finitely generated Z-graded modules over  $B[T_{0}^{-1}]$  may be identified with finitely generated modules over A[T] where  $T = T_{1}/T_{0}$ .

We have $\mathcal{B} \subset \mathcal{A}$ with $\mathcal{B}$ the collection of finitely generated graded $B$-modules killed by some power of $T_0$, so

$$
\mathcal {B} \subset \mathcal {A} \longrightarrow \mathcal {A} / \mathcal {B}
$$

with $\mathcal{A}/\mathcal{B}$ the collection of finitely generated graded $B[T_0^{-1}]$-modules, i.e., Modf(A[T]), which has the same $K_0$ as $A[T]$ by the Resolution Theorem.

We consider the projective modules in A. A free graded B-module is a direct sum of various  $B(p)$ , where  $B(p)$  is just B with the grading shifted p steps, i.e.,  $B(p)_{n} = B_{n-p}$ .

Fact Any projective graded B-module P is of the form

$$
P = B \otimes_ {A} Q _ {0} \oplus B \otimes_ {A} Q _ {1} [ 1 ] \oplus \dots ,
$$

where $Q_0, Q_1, \ldots$ are projective $A$-modules and

$$
B \otimes_ {A} Q _ {1} [ 1 ] = B (1) \otimes_ {A} Q _ {1}.
$$

In general, define an increasing filtration  $F_{p}$  M given by the B-submodule generated by  $M_{0}, M_{1}, \ldots, M_{p}$ , so we have

$$
\begin{array}{c} B (p) \otimes (M _ {p} / B _ {1} M _ {p - 1} + \dots + B _ {p} M _ {0}) \\ \Bigg \downarrow \\ F _ {p} M / F _ {p - 1} M \end{array}
$$

These are clearly isomorphisms for free modules, which implies also isomorphisms for projectives since projective implies summand of free and the construction is functorial.

Thus

$$
K _ {0} \binom{\text { graded   finitely   generated }}{\text { projective   B   -modules}} = K _ {0} (\mathcal {P} _ {A}) [ \xi ]
$$

where

$$
\begin{array}{c} B (n) \otimes_ {A} Q \longleftrightarrow [ Q ] \xi^ {n} \\ [ P ] \longmapsto \sum [ Q _ {n} ] \xi^ {n} \end{array}
$$

with  $Q_{n} = (P/B^{+}P)_{n}$  and  $B^{+} = B_{1} + B_{2} + \cdots$  the augmentation ideal.

The Szyzygy Theorem implies that any  $M \in A$  has a finite resolution by graded finitely generated projective B-modules whence

$$
K _ {0} \mathcal {A} = K _ {0} (A) [ \xi ].
$$

The Devissage Theorem implies that  $K_{0}B = K_{0}\left(\begin{array}{c} finitely generated graded \\ modules over B/T_{0}B\end{array}\right)$ .

But $A[T_1] = B / T_0B$ , and by the argument above

$$
K _ {0} \mathcal {B} = K _ {0} (A) [ \xi ]
$$

$$
Q \otimes_ {A} B / T _ {0} B (n) \longleftrightarrow [ Q ] \xi^ {n}.
$$

We thus have

$$
\begin{array}{c c} B / T _ {0}   B (n) \otimes_ {A} Q \\ \Big \uparrow & \\ [ Q ] \xi^ {n} & \end{array} \qquad \begin{array}{c c} K _ {0}   \mathcal {B} & \longrightarrow K _ {0}   \mathcal {A} \\ \Big \| & \\ K _ {0} (A) [ \xi ] & K _ {0} (A) [ \xi ] \end{array}
$$

and also have a resolution of, for instance,  $B/T_{0}B \otimes Q$  given by

$$
0 \longrightarrow B (1) \otimes_ {A} Q \stackrel {T _ {0}} {\longrightarrow} B \otimes Q \longrightarrow B / T _ {0} B \otimes Q \longrightarrow 0,
$$

so in $K_0\mathcal{A}, B / T_0B(n)\otimes Q$ maps to

$$
[ Q ] \xi^ {n} - [ Q ] \xi^ {n + 1}.
$$

It follows that the map $K_0 \mathcal{B} \to K_0 \mathcal{A}$ is multiplication by $(1 - \xi)$, whose cokernel is $K_0 A$, as desired.

Note that map is

$$
B \rightsquigarrow B \oplus_ {A} Q \rightsquigarrow (B \otimes_ {A} Q) [ T _ {0} ^ {- 1} ] \rightsquigarrow B [ T _ {0} ^ {- 1} ] \otimes_ {A} Q
$$

and take the degree zero part.

[Paul Goerss points out that this map is actually induced by augmentation.]  $K_{0}$  is functorial with respect to exact functors.

Proof of 2 We have

$$
\mathcal {B} \subset \mathcal {A} \xrightarrow {\gamma} \mathcal {B} / \mathcal {A}
$$

and think of the examples S-torsion finitely generated A modules  $\subset$  finitely generated A modules  $\rightarrow$  finitely generated  $S^{-1}A$  modules.

Given any object $V$ of $\mathcal{A}/\mathcal{B}$, choose $M \in \mathcal{A}$ with $\gamma M \cong V$. The point is such an $M$ is unique up to isomorphism mod $B$, i.e.,

![](images/page_149_image_0.jpg)

where  $[M]-[M']=[Cok u]-[Ker u]$  in  $K_{0}A$ , so  $[M]\cong[M']=[M']$  in  $K_{0}A/K_{0}B$  because  $[Cok u]$  and  $[Ker u]$  lie in  $K_{0}B$  since  $B\subset A$  is Serre.

We therefore associate to $V$ an element of $K_{0}\mathcal{A}/K_{0}\mathcal{B}$. This is additive for exact sequences hence is a homomorphism

$$
K _ {0} \mathcal {A} / K _ {0} \mathcal {B} \xrightarrow {\text {   }} K _ {0} (\mathcal {A} / \mathcal {B}).
$$

Easy to check these are inverses.

Another Example Take $G$ to be a finite group and $\mathbb{Q}_{p}$ to be the $p$-adic rationals and $\mathbb{Z}_{p}$ the $p$-adic integers. Let $R(G, \mathbb{Q}_{p})$, $R(G, \mathbb{Z}/p\mathbb{Z})$ and $R(G, \mathbb{Z}_{p})$ be the respective Grothendieck groups of representations of $G$ over $\mathbb{Q}_{p}$, $\mathbb{Z}/p\mathbb{Z}$ and $\mathbb{Z}_{p}$.

We have

{finitely generated torsion $\mathbb{Z}_p[G]$ - modules} $\longleftrightarrow$ Modf $(\mathbb{Z}_p[G]) \twoheadrightarrow$ Modf $(\mathbb{Q}_p[G])$

and get

$$
\begin{array}{c} K _ {0} (\text {torsion}) \longrightarrow K _ {0} (\text {Modf} \mathbb {Z} _ {p} [ G ]) \longrightarrow R (G, \mathbb {Q} _ {p}) \longrightarrow 0 \\ \left\| \text {by Devissage} \right. \qquad \qquad \qquad \left\| \text {by Resolution theorem} \right. \\ R (G, \mathbb {Z} / p \mathbb {Z}) \qquad \qquad R (G, \mathbb {Z} _ {p}) \end{array}
$$

i.e., we have

$$
\begin{array}{c} R (G, \mathbb {Z} / p   \mathbb {Z}) \xrightarrow {\alpha} R (G, \mathbb {Z} _ {p}) \longrightarrow R (G, \mathbb {Q} _ {p}) \longrightarrow 0 \\ \rho \Biggl | _ { \begin{array}{c} M \\ \downarrow \\ M / P M \end{array} } \text { exact   functor   for } M \text { free   over } \mathbb {Z} _ {p} \\ R (G, \mathbb {Z} / p   \mathbb {Z}) \end{array}
$$

where  $\alpha$  takes a representation W over Z/pZ and sends [W] to  $[P_{0}]-[P_{1}]$ , where

$$
0 \longrightarrow P _ {1} \longrightarrow P _ {0} \longrightarrow W \longrightarrow 0
$$

is an exact sequence of $G$-modules and $P_0$ and $P_1$ are free over $\mathbb{Z}_p$. Thus

$$
\rho \alpha [ \omega ] = [ P _ {0} / p P _ {0} ] - [ P _ {1} / p P _ {1} ].
$$

But we have

$$
\begin{array}{c} \operatorname{Tor} _ {1} ^ {\mathbb {Z} _ {p}} (\mathbb {Z} / p \mathbb {Z}, W) \longrightarrow P _ {1} / p P _ {1} \longrightarrow P _ {0} / p \mathbb {Z} \longrightarrow W \longrightarrow 0 \\ \Bigg | \\ W \end{array}
$$

Thus

$$
\rho \alpha [ W ] = [ W ] - [ W ] = 0,
$$

and we therefore get an induced map $R(G, \mathbb{Q}_p) \to R(G, \mathbb{Z}/p\mathbb{Z})$ called the specialization mod $p$. There is also a lifting map $R(G, \mathbb{Z}/p\mathbb{Z}) \to R(G, \mathbb{Q}_p)$ which is its inverse. See Serre's book.

## Geometric Realization of a Simplicial Space

Recall that  $\Delta$  is the category of posets  $[p] = \{0, \cdots, p\}$  in the usual order and maps of posets. We have the functor

$\triangle \longrightarrow$ Top = the category of topological spaces and continuous maps

$[p] \longmapsto \Delta_{p} = \text{simplex with vertices } \{0, \cdots, p\}.$

A (semi-)simplical space (s.s.) $X$ is a functor

$$
\mathbb {A} ^ {\mathrm{op}} \longrightarrow \text { Top }
$$

$$
[ p ] \longmapsto X _ {p}.
$$

The geometric realization $|X|$ of $X$ is defined as a coequalizer

$$
\coprod_ {[ p ] \rightarrow [ q ]} X _ {q} \times \Delta_ {p} \Rightarrow \coprod_ {[ p ]} X _ {p} \times \Delta_ {p} \rightarrow | X |.
$$

Note that $\mathrm{Hom}_{\mathrm{Top}}(|X|, Y) = \mathrm{Hom}_{\mathrm{s.s.}}(X, [p] \mapsto Y^{\Delta_p})$.

## Classifying Space of a Topological Category $\mathcal{C}$

We have the diagram

$$
\dots \operatorname{Ar} \mathcal {C} _ {\text {Ob} \mathcal {C}} \times \operatorname{Ar} \mathcal {C} \Longrightarrow \operatorname{Ar} \mathcal {C} \Longrightarrow \operatorname{Ob} \mathcal {C}.
$$

In general in a category T where we have fibered products, we have also the notion of a category object C. It is ObC and ArC plus maps

![](images/page_152_image_1.jpg)

and

![](images/page_152_image_3.jpg)

so that for any $Y \in \mathcal{T}$, $\operatorname{Hom}_{\mathcal{T}}(Y, \cdot)$ carries this data into a category.

A topological category is a category object C in Top. That is, the set of objects  $\mathrm{Ob}(\mathcal{C})$  and the set of morphisms  $\mathrm{Ar}(\mathcal{C})$  are made into topological spaces so that usual maps such as the composition  $Ar \times_{Ob} Ar \rightarrow Ar$ , are continuous.

The nerve of a topological category C is the simplicial space

$$
\dots \mathrm{Ar} \underset {\mathrm{Ob}} {\times} \mathrm{Ar} \underset {\mathrm{Ob}} {\times} \mathrm{Ar} \underset {\mathrm{Ob}} {\longrightarrow} \mathrm{Ar} \underset {\mathrm{Ob}} {\times} \mathrm{Ar} \underset {\mathrm{Ob}} {\longrightarrow} \mathrm{Ar} \mathcal {C} \longrightarrow \mathrm{Ob} \mathcal {C},
$$

and the classifying space is the geometric realization |nerve of C| of the nerve.

Example Take G a topological group. The nerve is

$$
\dots G \times G \times G \xrightarrow {\pi_ {2}} G \times G \xrightarrow {\cdot} G \xrightarrow {\pi_ {1}} *
$$

$G\times G\times G\xrightarrow{\text{pr}_{12}}G\times G\xrightarrow{\text{pr}_1}G \equiv \text{nerve of cofibered category defined by Hom(*,·)}$$G\times G\xrightarrow{\text{pr}_{12}}G\xrightarrow{\text{pr}_1}G*$

Taking $PG = |\text{top line}|$, $BG = |\text{bottom line}|$, then

$$
\begin{array}{c} P G \\ \Bigg \downarrow \\ B G \end{array}
$$

is a principal fiber bundle over BG with structure group G. Moreover, it is universal in the sense that  $[X, BG]$  is the collection of isomorphism classes of principal G-bundles over X for X paracompact.

Example Take a poset I. Then we can see that BI is a simplicial complex whose simplexes are chains in I.

Fun Example Fix a vector space  $V = C^{n}$  over C and consider the poset of proper subspaces of V. This is topological poset so a topological category. Consider a self-adjoint operator A on V with  $0 \leq A \leq I$ . Then it has eigenspaces, so if the eigenvalues are  $0 \leq \lambda_{1} < \cdots < \lambda_{p} \leq I$ , then we get a flag  $0 \subset V_{1} \subset V_{2} \subset \cdots \subset V_{p} \subset V$ . We get an identification of this classifying space with a certain family of self-adjoint operators. Exercise to fix this: try all rays of A's with tr A = 0. If this works, then  $BC = S^{\frac{n(n+1)}{2}-2}$ , a sphere.

Suppose C is a discrete category. What are  $\pi_{0} BC, \pi_{1}(BC, *)$ ,  $H_{*}(BC, \mathbb{Z})$ ? It is clear that  $\pi_{0} BC$  is the set of components of C. Also, for  $X \in Ob C$ , what is  $\pi_{1}(BC, X)$ ? The fundamental groupoid of BC is equivalent to the groupoid obtained from C by inverting the arrows of C as for covering spaces. In effect given a covering space E of BC, we get a functor from C to Sets by

$$
\begin{array}{l} X \longmapsto \text { fiber   of } E \text { over } X \\ f \longmapsto \text { deck   transformation }. \end{array}
$$

This carries maps to isomorphisms.

Conversely, given $F: \mathcal{C} \to$ Sets so that $F(f)$ is an isomorphism for all $f$, we get a covering space by taking $\mathcal{C}_F$ to be the cofibered category over $\mathcal{C}$ defined by the functor $F$, so $\mathrm{Ob}\,\mathcal{C}_F = \{(X, \xi): \xi \in F(X)\}$, and finally forming $B\,\mathcal{C}_F$.

We saw that  $\pi_{0} BC$  is the set of components of C in the usual sense. If we think of objects X of C as being points in BC, then we can speak of  $\pi_{1}(BC, X)$ . Now the fundamental groupoid of BC is simply the groupoid obtained from C by inverting all the arrows. For given a covering space E of BC, we get a functor  $C \rightarrow$  Sets

$$
\begin{array}{l} X \longmapsto \text { fiber   of } C \text { over } X \\ \Biggl \downarrow_ {f} \qquad \qquad \qquad \qquad \Biggl \downarrow \cong \text { lifting   of   path   association   to } f \\ Y \longmapsto \text { fiber   of } C \text { over } Y \end{array}
$$

which inverts morphisms. Conversely, given  $F : C \to$  Sets so that  $F(f)$  is an isomorphism for all f, we get a covering space by taking  $C_{F}$  to be the cofibered category over C defined by F and forming  $E = B C_{F}$ . So  $\pi_{1}(B C, X)$  is just the group of “loops” based at X in the groupoid obtained from C by inverting arrows.

Fun Example of Chapter 29 Fixed Consider the topological poset of all subspaces of a finite-dimensional vector space V. The nerve is

$$
\dots \Longrightarrow \coprod_ {p \leq q} \operatorname{Flag} _ {p, q} (V) \Longrightarrow \coprod_ {p = 0} ^ {n} \operatorname{Flag} _ {p} (V).
$$

Then the realization of this s.s. is the space of self-adjoint operators A on V so that  $0 \leq A \leq I$ . Call this space Y. To each subspace W we associate the projection operator  $p_{W}$ , and to an inclusion  $W' \subset W$  we associate the “1-simplex”

$$
t _ {0} p _ {W ^ {\prime}} + t _ {1} p _ {W}
$$

for $t_0 + t_1 = 1, 0 \leq t_0, t_1 \leq 1$. Similarly for higher dimensions, so that a point in the realization of the form

$$
(t _ {0}, t _ {1}, \dots , t _ {p}) \times (W _ {0} <   W _ {1} <   \dots <   W _ {p})
$$

for  $(t_{0},\cdots,t_{p})\in\operatorname{Int}\Delta_{p}$ , and  $W_{0}<W_{1}<\cdots<W_{p}$  a flag of length p, is mapped to the self-adjoint operator

$$
\sum_ {j = 0} ^ {p} t _ {j} p _ {W _ {j}}.
$$

Check that this works.

Now for a small category C, we have seen that  $B C = |nerve of C|$  has fundamental groupoid equivalent to the groupoid obtained by inverting the arrows of C.

Example If C is a poset, then BC is the simplicial complex of chains in C. Since BC is a CW-complex, the homology of BC with coefficients in a local coefficient system L can be computed cellularly

$$
C_{q}(B  \mathcal{C},L) = \bigoplus_{\substack{X_{0}\longleftarrow \dots \longleftarrow X_{q}\\ \text{none the identity map}}}L(X_{q})  .
$$

On the other hand, we have $H_{q}(\mathcal{C}, L)$, where $L$ is viewed as a covariant functor $\mathcal{C} \to \mathrm{Ab}$. This homology is computed via the simplicial abelian group $C(\mathcal{C}, L)$

$$
\dots \underset {\rightarrow} {\longrightarrow} \bigoplus_ {X _ {2} \rightarrow X _ {1} \rightarrow X _ {0}} L (X _ {2}) \underset {\rightarrow} {\longrightarrow} \bigoplus_ {X _ {1} \rightarrow X _ {0}} L (X _ {1}) \underset {\rightarrow} {\longrightarrow} \bigoplus_ {X _ {0}} L (X _ {0})
$$

which is the same as $C(B\mathcal{C},L)$ except for degeneracies. Thus, the Normalization Theorem says

$$
\begin{array}{r l} H _ {*} (C _ {+} (\mathcal {C}, L)) & = H _ {*} (C _ {*} (\mathcal {C}, L) / \text { degeneracies }) \\ & \cong H _ {*} (C _ {*} (B \mathcal {C}, L)), \end{array}
$$

so we have an isomorphism

$$
H _ {*} (B \mathcal {C}, L) \cong H _ {*} (\mathcal {C}, L)
$$

between "geometric" and "derived-functor" homologies.

Now we recall the Whitehead theorem. If  $f : X \to Y$  is a map of CW complexes, then f is a homotopy equivalence if and only if f induces isomorphisms

$$
\pi_ {0} (X) \stackrel {\sim} {\longrightarrow} \pi_ {0} (Y),
$$

$$
\pi_ {1} (X, x) \stackrel {{\sim}} {{\longrightarrow}} \pi_ {1} (Y, f (x)), \text {   for   all   } x \in X,
$$

$H_{q}(X, f^{-1}(L)) \stackrel{\sim}{\longrightarrow} H_{q}(Y, L)$ , for all q and all local coefficient systems L on Y. Therefore, a functor  $f : C \to C'$  induces a homotopy equivalence  $B C \to B C'$  when f induces an isomorphism on associated groupoids and homology with coefficients in any morphism-inverting Ab-valued functor.

Fun Example of Chapter 29 Again Let $\mathcal{C}$ be the poset of subspaces of $V$. Consider

$$
\left| \begin{array}{l} \text { s.s.   of } U \subset W _ {0} <   W _ {1} <   \dots <   W _ {r} \subset V \\ \text { so   that   either } W _ {0} > 0 \text { or } W _ {1} <   V \end{array} \right| \subset B \mathcal {C}
$$

The space on the left can be written

$$
B (\text { all   subspaces } W > U) \bigcup_ {B (\text { proper   subspaces })} B (\text { all   subspaces } W <   V).
$$

Now

$$
Y = \left\{\text { self - adjoint } A \mid 0 \leq A \leq I \right\}
$$

is homeomorphic to $D^{n(n + 1) / 2}$, so $\partial Y\cong S^{n(n + 1) / 2 - 1}$. If we set

$$
Z = B (\text { proper   subspaces })
$$

then

$$
\left| \begin{array}{c} 0 \subset W _ {0} <   \dots <   W _ {p} \subset V \text {so} \\ \text {that} W _ {0} > 0 \text {or} W _ {p} <   V \end{array} \right| = \partial Y = C Z \bigcup_ {Z} C Z,
$$

so

$$
S Z = \partial Y \cong S ^ {n (n + 1) / 2 - 1},
$$

and with more work we can show $Z \cong S^{n(n+1)/2-2}$.

## Definition of Higher $K$-groups

Let $\mathcal{M}$ be an exact category. Define $Q\mathcal{M}$ to be the category with the same objects as $\mathcal{M}$, but in which an arrow $M' \to M$ is an isomorphism of $M'$ with an admissible subquotient of $M$, where an admissible subquotient of $M$ is something of the form $M_1 / M_2$, where $0 \subset M_2 \subset M_1 \subset M$ is an admissible filtration of $M$. So a map from $M'$ to $M$ in $Q\mathcal{M}$ is an isomorphism

$$
M ^ {\prime} \stackrel {{\sim}} {{\longrightarrow}} M _ {1} / M _ {2}.
$$

Composition is clear.

The higher $K$-groups of an exact category $\mathcal{M}$ are defined by

$$
K _ {i} \mathcal {M} = \pi_ {i + i} (B Q \mathcal {M}, 0).
$$

For this definition to be reasonable, it should correspond with the Grothendieck definition for $i = 0$. First we show $\pi_1(BQ\mathcal{M})$ is abelian. Direct sum gives a functor

$$
Q \mathcal {M} \times Q \mathcal {M} \longrightarrow Q \mathcal {M},
$$

so we get a map

$$
\begin{array}{c} B (Q \mathcal {M} \times Q \mathcal {M}) \longrightarrow B Q \mathcal {M} \\ \Bigg | _ {B Q \mathcal {M} \times B Q \mathcal {M}} \end{array}
$$

providing an operation on $BQM$. It follows that $BQM$ is an $H$-space, and this implies that $\pi_1(BQM)$ is abelian.

Picture: In QM, we have maps

$$
0 \xrightarrow [ 0 \text {   sub - object } ]{0 \text {   quotient   object }} M
$$

For any object $M$, this gives a loop in $BQM$ associated to $M$. For an exact sequence

$$
0 \longrightarrow M ^ {\prime} \longrightarrow M \longrightarrow M ^ {\prime \prime} \longrightarrow 0
$$

in $\mathcal{M}$ we have arrows

$$
0 \xrightarrow { \begin{array}{c} 0 = M ^ {\prime} / M \\ 0 = M ^ {\prime} / M ^ {\prime} \\ 0 = 0 / 0 \end{array} } M
$$

in QM. Then we get a homotopy of the loop associated to  $M'$  with one of those associated to M via

![](images/page_157_image_12.jpg)

But we also have

![](images/page_158_image_0.jpg)

Hence the loop $0 \xrightarrow[0/0]{M/M} M$ is the loop of $M'$ followed by that of $M''$.

Suppose that $\mathcal{M}$ is an exact category and let $Q\mathcal{M}$ be the category with the same objects but in which a morphism $M' \to M$ is an isomorphism of $M'$ with an admissible subquotient of $M$, i.e., $0 \subset M_0 \subset M_1 \subset M$ with all quotients in $\mathcal{M}$ and $M_1 / M_0$ is a sub-quotient.

An admissible monomorphism $i:M^{\prime}\hookrightarrow M$ is an injection so that $M/M^{\prime}\in\mathcal{M}$. Such determines a map in $\mathcal{Q}\mathcal{M}$ to be denoted

$$
i _ {!}: M ^ {\prime} - - - \rightarrow M.
$$

Likewise, an admissible epimorphism $j:M\to M''$ in $\mathcal{M}$ determines a map

$$
j ^ {!}: M ^ {\prime \prime} - - - \rightarrow M
$$

in QM.

Suppose given an arbitrary map $N - \infty \to M$ in $\mathcal{QM}$ determined by $\theta : N \stackrel{\sim}{\longrightarrow} M_1 / M_0$, where $0 \subset M_0 \subset M_1 \subset M$ is an admissible filtration. We get a diagram

$$
\begin{array}{c} M _ {1} \xrightarrow {i ^ {\prime}} M \\ \text {"} \theta^ {- 1}" \Biggl \downarrow_ {j ^ {\prime}} \\ N \xrightarrow {i} M / M _ {0} \\ \text {"} \theta^ {\prime \prime} \end{array}
$$

in $\mathcal{M}$. The original $N - - - \rightarrow M$ in $Q\mathcal{M}$ is either of

$$
\begin{array}{l} M _ {1} - \frac {(i ^ {\prime}) !}{-} > M \\ \text {   A   } \quad \text {   A   } \\ | (j ^ {\prime}) ^ {!} | j ^ {!} \\ | \quad | \\ N - \frac {}{i !} > M / M _ {0} \end{array}
$$

Proposition A functor  $Q M \xrightarrow{F} C$  is the “same thing” as giving for each object  $M \in M$  an object  $F(M)$  in C, for each admissible monomorphism  $i : N \hookrightarrow M$  a map  $i_{*} : F(N) \to F(M)$  and for each admissible epimorphism  $j : M \to M''$  a map  $j^{*} : F(M'') \to F(M)$  so that

$I: (\mathrm{id}_M)_* = \mathrm{id}_{F(M)}$ and $(i_1 i_2)_* = i_{1*} i_{2*}$,

2: $(\mathrm{id}_M)^* = \mathrm{id}_{F(M)}$ and $(j_1 j_2)^* = j_2^* j_1^*$,

3: for any cartesian square

![](images/page_160_image_5.jpg)

of admissible monomorphisms and epimorphisms, we have

$$
i _ {*} j ^ {*} = (j ^ {\prime}) ^ {*} i _ {*} ^ {\prime}.
$$

Proof Exercise ... except for the following remark. We can think of a map $M - - - \rightarrow N$ in $\mathcal{QM}$ as being an isomorphism class of diagrams

$$
\begin{array}{c} N _ {1} \xrightarrow {} N \\ \Big \downarrow \\ M \end{array}
$$

and composition of such given by

![](images/page_160_image_11.jpg)

Theorem $\pi_1(BQ\mathcal{M},0)\cong K_0\mathcal{M}$

Proof The idea is to look at morphism-inverting functors F from QM to Sets, which are essentially the same as covering spaces of BQM and to show that  $K_{0}M$  acts naturally on  $F(0)$ , and that in this way the category of such F becomes equivalent to  $(K_{0}\mathcal{M})$ -sets. To each M we have  $i_{M}:0\hookrightarrow M$  and

$$
(i _ {M}) _ {!}: 0 - - - - \rightarrow M \text { in } Q \mathcal {M}
$$

and

$$
(i _ {M}) _ {*} = F (i _ {M!}): F (0) \stackrel {\sim} {\longrightarrow} F (M).
$$

Replace $F$ by a map so that these are the identity; this is like choosing a maximal tree. Thus we have

$$
F _ {(i _ {1})} = \mathrm{id} _ {F (0)}, \quad \text { for   all } \quad i: M \hookrightarrow N
$$

and

![](images/page_161_image_7.jpg)

Apply $F$ to see that $F(j^{!})$ depends only on $\operatorname{Ker} j$. To each $N$, let $P_{N}: N \twoheadrightarrow 0$. Then to each $N$ we get an isomorphism $F(P_{N}^{!}): F(0) \to F(0)$, and we have thus shown that

$$
F (j ^ {!}) = F \left(P _ {\text {Ker} j} ^ {!}\right),
$$

and in fact

$$
F \left( \begin{array}{c} M \\ N \end{array} \right) = F (P _ {\text {Ker} j} ^ {!})
$$

Given $0 \to N' \to N \to N'' \to 0$ we have

![](images/page_161_image_13.jpg)

SO

$$
F (P _ {N} ^ {!}) = F (P _ {N ^ {\prime}} ^ {!}) \circ F (P _ {N ^ {\prime \prime}} ^ {!}).
$$

So to each N in M we have associated an automorphism  $F(P_{N}^{!})$  of  $F(0)$ .

But $K_{0}\mathcal{M}$ is the not necessarily abelian group generated by $[N]$ for $N\in\mathrm{Ob}\mathcal{M}$ with the relations $[N]=[N^{\prime}][N^{\prime\prime}]$ for each exact $0\to N^{\prime}\to N\to N^{\prime\prime}\to 0$.

Note however that

$$
[ N ^ {\prime} ] [ N ^ {\prime \prime} ] = [ N ^ {\prime} \oplus N ^ {\prime \prime} ] = [ N ^ {\prime \prime} \oplus N ^ {\prime} ] = [ N ^ {\prime \prime} ] [ N ^ {\prime} ],
$$

so we get by universal nonsense a map

$$
\begin{array}{c} K _ {0} \mathcal {M} \longrightarrow \operatorname{Aut} (F (0)) \\ [ N ] \longmapsto F (P _ {N} ^ {!}). \end{array}
$$

Thus $F(0)$ is a $(K_0\mathcal{M})$-set.

Conversely, given a $(K_0\mathcal{M})$ -set $S$ , define

$$
F _ {S}: Q \mathcal {M} \longrightarrow \text { Sets }
$$

by $F_S(M) = S$ and $F_S(i_!) = \mathrm{id}_S$ with $F_S(j^! )$ given by multiplication by $[\operatorname{Ker} j] \in K_0 \mathcal{M}$.

A functor $F: \mathcal{C} \to \mathcal{C}'$ is a homotopy equivalence if the induced map

$$
B \mathcal {C} \longrightarrow B \mathcal {C} ^ {\prime}
$$

is a homotopy equivalence. Call C contractible if  $BC \cong *, i.e., if BC$  is homotopy equivalent to a point.

(Nice) Theorem $B(\mathcal{C} \times \mathcal{C}') \to BC \times BC'$ is a homeomorphism for $\times$ on the right the CW-product of CW complexes and $\times$ on the left the category product.

Proof Follows from Milnor's theorem that  $|X \times Y| = |X| \times |Y|$  for X, Y simplicial sets. □

Take in particular  $C'$  to be the poset  $\{0 < 1\}$  so that  $BC' = [0, 1]$ . Therefore

$$
B (\mathcal {C} \times \{0 <   1 \}) \cong B \mathcal {C} \times [ 0, 1 ].
$$

A functor $F: \mathcal{C} \times \{0 < 1\} \to \mathcal{C}'$ is the same as a pair of functors $f_0, f_1: \mathcal{C} \to \mathcal{C}'$ and a natural transformation $F$ from $f_0$ to $f_1$. Thus

$$
B \mathcal {C} \times [ 0, 1 ] \cong B (\mathcal {C} \times \{0, 1 \}) \xrightarrow {B (F)} B \mathcal {C} ^ {\prime}
$$

is a homotopy between $B(f_{0})$ and $B(f_{1})$. Therefore two functors $f, g: \mathcal{C} \to \mathcal{C}'$ which can be connected by a finite sequence (zigzag) of natural transformations

$$
f = f _ {0} \longrightarrow f _ {1} \longleftarrow f _ {2} \longrightarrow \dots \longleftarrow f _ {n} = g
$$

induce homotopic maps  $Bf \simeq Bg : BC \to BC'$ .

Example 32.1 If $f: \mathcal{C} \to \mathcal{C}'$ has an adjoint $g: \mathcal{C}' \to \mathcal{C}$, then we have adjunction maps

$$
g f \longleftarrow \mathrm{id} \quad f g \longrightarrow \mathrm{id}
$$

so $f$ and $g$ are homotopy equivalences.

Example 32.2 A category with final or initial object is automatically contractible. In particular, this holds for any abelian category.

Example 32.3 If a category C has an object  $x_{0}$ , then we have the constant functor  $x_{0}:C\to C$  sending every object to  $x_{0}$  and every morphism to the identity of  $x_{0}$ . Suppose, in addition, that we have a functor  $F:C\to C$  and natural transformations

$$
\underline {{{x _ {0}}}} \longleftarrow F \longrightarrow \operatorname{Id} _ {\mathcal {C}}.
$$

Then $\mathcal{C}$ is contractible.

A useful condition for a functor to be a homotopy equivalence is

Theorem A $f: \mathcal{C} \to \mathcal{C}'$ is a homotopy equivalence when $f/Y$ is contractible for all $Y \in \mathrm{Ob}\mathcal{C}'$ or when $Y/f$ is contractible for all $Y \in \mathrm{Ob}\mathcal{C}'$.

Proof From last term, either condition is sufficient to prove homology equivalence, and the isomorphism of  $\pi_{1}$  is easy when  $\pi_{1}$  is viewed categorically. The result then follows from Whitehead's Theorem. ☐

Recall that f/Y has objects  $(X, u)$

$$
u: f X \longrightarrow Y.
$$

Devissage Theorem Suppose that A is an abelian category and B is a full sub-category closed under sub-objects, quotient objects and products. (Think of A = Modf (A), B = Modf (A/I).) Assume every  $M \in Ob A$  has a finite filtration whose quotients are in B (e.g.,  $I^{n} = 0$ ). Then the inclusion

$$
Q B \subset Q A
$$

is a homotopy equivalence, so B and A have the same K-groups.

Proof Let $f:QB\hookrightarrow QA$. Let $M\in\mathrm{Ob}\,QA=\mathrm{Ob}\,A$. What is $f/M$? It consists of $(N,u)$, $N\in\mathrm{Ob}\,B$ and $u:N---\to M$ in $QA$. Easy to see $f/M$ is equivalent to the poset $J_{M}$ of all layers $(M_{0},M_{1})$ in $M$, i.e., $M_{0}\subset M_{1}\subset M$ so that $M_{1}/M_{0}\subset\mathrm{Ob}\,B$, and where the ordering in $J_{M}$ is

$$
(M _ {0} \subset M _ {1}) \leq (M _ {0} ^ {\prime} \subset M _ {1} ^ {\prime})
$$

if and only if

$$
M _ {0} ^ {\prime} \subseteq M _ {0} \subseteq M _ {1} \subseteq M _ {1} ^ {\prime}.
$$

We know there exists

$$
0 \subset F _ {1} \subset \dots \subset F _ {p} = M
$$

so that $F_{p} / F_{p - 1}\in \mathrm{Ob}\mathcal{B}$ .We shall show that each inclusion in

$$
J _ {0} \subset J _ {F _ {1}} \subset J _ {F _ {2}} \subset \dots \subset J _ {F _ {p}} = J _ {M}
$$

is a homotopy equivalence, and it is enough to show that

$J_{M'} \subset J_M$ is a homotopy equivalence when $M'/M \in \mathrm{Ob}\mathcal{B}$.

Now,

$$
J _ {M} \ni (M _ {0}, M _ {1}) \leq (M ^ {\prime} \cap M _ {0}, M _ {1}) \geq (M ^ {\prime} \cap M _ {0}, M ^ {\prime} \cap M _ {1}) \in J _ {M ^ {\prime}}\tag{*}
$$

and $(M' \cap M_0, M_1)$ is in $J_M$ since $M_1 / (M' \cap M_0) \subset (M / M') \times (M_1 / M_0)$ with both $M / M'$ and $M_1 / M_0$ in $\mathcal{B}$.

Thus we have

$$
\begin{array}{c} i: J _ {M ^ {\prime}} \longrightarrow J _ {M}, \text { inclusion }, \\ r: (M _ {0}, M _ {1}) \longmapsto (M ^ {\prime} \cap M _ {0}, M ^ {\prime} \cap M _ {1}) \end{array}
$$

and ri = id while (\*) gives id ≈ ir.

Now use Theorem A.

□

(Special case of) Resolution Theorem Suppose $\mathcal{M}$ is an exact category and $\mathcal{P}$ is a full subcategory closed under extensions in $\mathcal{M}$. Assume

(i) for  $0 \rightarrow M' \rightarrow P \rightarrow M \rightarrow 0$  exact in M;  $P \in P$  implies  $M' \in P$ ,

(ii) given $M \in \mathcal{M}$, there is an exact sequence

$$
0 \longrightarrow P _ {1} \longrightarrow P _ {0} \longrightarrow M \longrightarrow 0 \text { with } P _ {0}, P _ {1} \in \mathcal {P}.
$$

Then $QP \hookrightarrow Q\mathcal{M}$ is a homotopy equivalence.

Proof Factor into

$$
Q \mathcal {P} \xrightarrow {g} \mathcal {C} \xrightarrow {f} Q \mathcal {M}
$$

where C is the full subcategory of QM whose objects are the P in P. Note that in C a morphism  $P' \longrightarrow P$  is given by an isomorphism  $P' \simeq M_{1}/M_{0}$  where  $0 \subset M_{0} \subset M_{1} \subset P$  is admissible in M.

We consider $g / P$ for $P \in \mathcal{P}$. $g / P$ is equivalent to the poset of $\mathcal{M}$-admissible layers $(M_0, M_1)$ in $P$ with $M_1 / M_0 \in \mathcal{P}$, where we have

$$
(M _ {0} ^ {\prime}, M _ {1} ^ {\prime}) \leq (M _ {0}, M _ {1})
$$

if and only if  $M_{0} \subseteq M_{0}^{\prime} \subseteq M_{1}^{\prime} \subseteq M_{1}$  and all quotients of this are in P.

This poset is contractible since

$$
(M _ {0}, M _ {1}) \leq (0, M _ {1}) \geq (0, 0),
$$

for which we need property (i). Thus by Theorem A, $g$ is a homotopy equivalence.

We consider $M/f$ for $M \in \mathcal{M}$. An object of this category is a $P$ in $\mathcal{C}$ and a map $M \xrightarrow{u} P$ in $Q\mathcal{M}$.

First step: Introduce the full subcategory $\mathcal{F}$ of all $(P, u)$ where $u$ comes from an epimorphism. Show

![](images/page_166_image_8.jpg)

is adjoint to inclusion of $\mathcal{F} \subset M \setminus f$.

Second step:  $F^{op}$  consists of all  $\downarrow$ , for  $P \in P$ , and morphisms are M

![](images/page_166_image_11.jpg)

This category has a “conical contraction” as in Example 32.3, namely fix

![](images/page_167_image_0.jpg)

Thus $M \backslash f \cong *,$ so by Theorem A, $f$ is a homotopy equivalence, as desired.

Let $A$ be a Dedekind domain and $F$ its field of fractions. Consider $Q(\mathcal{P}_A)$. There is a natural filtration

$$
\begin{array}{l} F _ {n} Q (\mathcal {P} _ {A}) = \text { full   subcategory   consisting   of   those } P \in Q (\mathcal {P} _ {A}) \\ \text { of   rank   at   most } n. \end{array}
$$

Since we work over a Dedekind domain, two $P$, $Q \in \mathcal{P}_A$ are isomorphic when they have the same rank $r$, and in this case

$$
\Lambda^ {r} P \cong \Lambda^ {r} Q \in \operatorname{Pic} A.
$$

Thus,

$$
\{0 \} = F _ {0} Q (\mathcal {P} _ {A}) \subset F _ {1} Q (\mathcal {P} _ {A}) \subset \dots ,
$$

and  $F_{n} Q(\mathcal{P}_{A})$  is obtained from  $F_{n-1} Q(\mathcal{P}_{A})$  by adding one new isomorphism class for each element of  $\operatorname{Pic}(A)$ .

Let us “compute”  $H_{*}(F_{n} Q(\mathcal{P}_{A}), F_{n-1} Q(\mathcal{P}_{A}))$ .

To this end, fix  $P \in P_{A}$  and consider  $F_{n-1} Q(\mathcal{P}_{A})/P$ . This is equivalent to the poset of admissible layers  $(P_{0}, P_{1})$  in P where rank  $(P_{1}/P_{0}) < n$  with the ordering  $(P_{0}^{\prime}, P_{1}^{\prime}) \leq (P_{0}, P_{1})$  if  $P_{0} \subseteq P_{0}^{\prime} \subseteq P_{1}^{\prime} \subseteq P_{1}$ .

First observation: Admissible sub-objects  $P' \subset P$  are in one-to-one correspondence with subspaces  $V'$  of  $V = F \otimes_{A} P$  via

$$
F \otimes_ {A} P ^ {\prime} = V ^ {\prime} \quad \text { where } \quad P ^ {\prime} = V ^ {\prime} \cap P \subset V.
$$

Let $V$ be a vector space over $F$ and let $Y(V)$ be the poset of layers $(V_{0}, V_{1})$ in $V$ such that $V_{0} \neq 0$ or $V_{1} \neq V$.

Thus  $Y(V) = Y^{+} \cup Y^{-}$  where  $Y^{+}$  are the layers so that  $V_{1} < V$  and  $Y^{-}$  are the layers so that  $V_{0} > 0$ .

Remark If I is a poset and J is the poset of layers in I, then I and J are homotopy equivalent.

More generally if C is a small category, we can form a category A whose objects are arrows in C and in which a morphism  $(X' \stackrel{u'}{\longrightarrow} Y') \longrightarrow (X \stackrel{u}{\longrightarrow} Y)$  is a diagram

![](images/page_169_image_3.jpg)

A is the cofibered category over  $C^{op} \times C$  belonging to the functor

$$
X, Y \longmapsto \operatorname{Hom} _ {\mathcal {C}} (X, Y),
$$

and the functor $\mathcal{A} \xrightarrow{p} \mathcal{C}$ given by $(X \xrightarrow{u} Y) \longmapsto Y$ is cofibered with fiber over $Y$ equal to $(\mathcal{C}/Y)^{\mathrm{op}}$, which is contractible since it has an initial object.

Similarly  $A \xrightarrow{q} C^{op}$  is cofibered with contractible fiber over Y = X/C.

It follows that $p$ and $q$ are homotopy equivalences by Theorem A plus the fact that for a cofibered functor $f: \mathcal{C} \to \mathcal{C}'$ the left fiber $\mathcal{C}/Y$ is homotopy equivalent to the fiber $f^{-1}(Y)$, that is, we have

$$
f ^ {- 1} Y \subset \mathcal {C} / Y,
$$

$u_{*}X\longleftarrow \binom{X}{fX\xrightarrow{u}Y}$ adjoint to inclusion.

In fact $BA$ is a kind of subdivision of $BC$ where $X \to Y$ subdivides to

and

![](images/page_169_image_13.jpg)

It follows that  $Y^{+}$ is homotopy equivalent to the poset of all subspaces contained in but not equal to V, whence  $Y^{+} \cong *$ . Similarly  $Y^{-} \cong *$ , and  $Y^{+} \cap Y^{-}$ is homotopy equivalent to the poset of all proper subspaces of V. Thus

$$
\begin{array}{r l} Y (V) & = \sum (Y ^ {+} \cap Y ^ {-}) \\ & = F _ {n - 1} Q (\mathcal {P} _ {A}) / P, \end{array}
$$

where $\sum$ denotes the suspension.

Example The Tits building  $T(V)$  is the simplicial complex associated to the poset of proper subspaces of V. If G = Aut V, then the parabolic subgroups of G which are distinct from G are in one-to-one correspondence with the flags in V. We have the

Theorem (Tits) $T(V)$ is homotopy equivalent to a bouquet of $(n - 2)$ spheres, where $n$ is the dimension of $V$.

Example For n = 2,  $T(V)$  is the zero-dimensional complex with vertices given by lines in V, and for n = 3,  $T(V)$  is a connected graph.

The Steinberg module is $\widetilde{H}_{n-2}(T(V),\mathbb{Z})$.

Theorem A $f: \mathcal{C} \to \mathcal{C}'$ is a homotopy equivalence if $Y \setminus f \cong *$ for all $Y$, where $Y \setminus f = \left\{\binom{X}{Y \xrightarrow{u} fX}\right\}$ is the cofibered category corresponding to the map $X \mapsto \operatorname{Hom}_{\mathcal{C}'}(Y, fX)$.

Let $S(f)$ be the cofibered category over $\mathcal{C} \times (\mathcal{C}')^{\mathrm{op}}$ associated to $(X, Y) \mapsto \operatorname{Hom}_{\mathcal{C}'}(Y, fX)$, so $S(f)$ has objects $\{(X, Y, u : Y \to fX)\}$ and morphisms given by diagrams

$$
\begin{array}{c} Y \xrightarrow {u} f X \\ \bigwedge \\ \big | \\ \big | \\ Y ^ {\prime} \xrightarrow {u ^ {\prime}} f X ^ {\prime} \end{array}
$$

Let $T(f)$ be a bi-simplicial set, that is,

$$
[ p ], [ q ] \longmapsto \text { sets   of   pairs }
$$

$$
\left(Y _ {p} \longrightarrow Y _ {p - 1} \longrightarrow \dots \longrightarrow Y _ {0} \longrightarrow f X _ {0}, X _ {0} \longrightarrow \dots \longrightarrow X _ {q}\right)
$$

of diagrams, the first in  $C'$  and the second in C, and call this  $T(f)_{p,q}$ , i.e.,

$$
\begin{array}{r l}T (f) _ {p, q}&= \coprod_ {X _ {0} \rightarrow \dots \rightarrow X _ {q} \in N (\mathcal {C})} N _ {p} (\mathcal {C} ^ {\prime} / f X _ {0})\\&= \coprod_ {Y _ {p} \rightarrow \dots \rightarrow Y _ {0} \in N (\mathcal {C} ^ {\prime})} N _ {q} (Y _ {0} \backslash f).\end{array}
$$

Proposition Given a bi-simplicial set $p, q \mapsto T_{p,q}$, we have homeomorphisms

$$
\left| [ p ] \longmapsto \left| [ q ] \longmapsto T _ {p q} \right| \right|
$$

$$
\left| [ p ] \longmapsto T _ {p p} \right|
$$

$$
\left| [ q ] \longmapsto \left| [ p ] \longmapsto T _ {p q} \right| \right|
$$

Example  $T_{pq} = X_{p} \times Y_{q}$  for X and Y simplicial sets, whence

$$
\left| [ q ] \longmapsto X _ {p} \times Y _ {q} \right| = X _ {p} \times | Y |
$$

SO

$$
\left| [ p ] \longmapsto \left| [ q ] \longmapsto X _ {p} \times Y _ {q} \right| \right| = | X | \times | Y |.
$$

Milnor's Theorem says $|X \times Y| = |X| \times |Y|$, where $X \times Y : [p] \longmapsto X_p \times Y_p$. Thus the Proposition works here.

Proof of Proposition First, by general nonsense, we only have to exhibit these homeomorphisms for the following generators on the category of bi-simplicial sets

$$
h _ {([ m ], [ n ])}: [ p ], [ q ] \longmapsto \operatorname{Hom} _ {\mathbb {A}} ([ p ], [ m ]) \times \operatorname{Hom} _ {\mathbb {A}} ([ q ], [ n ])
$$

since for any $F:\mathcal{C}\to$ Sets, we have

$$
\varinjlim_ {(X, \xi) \in \mathcal {C} _ {F}} h _ {X} = F.
$$

Second, $|[p] \mapsto \operatorname{Hom}_{\mathbb{A}}([p], [m])|$ is the $m$-simplex $\mathbb{A}_m$, and the combinatorial part is that

$$
\mathbb {A} _ {m} \times \mathbb {A} _ {n} = | [ p ] \mapsto \operatorname{Hom} _ {\mathbb {A}} ([ p ], [ m ]) \times \operatorname{Hom} _ {\mathbb {A}} ([ p ], [ n ]) |,
$$

proving the second assertion and hence the proposition.

□

Claim  $T(f)_{pp} = N_{p}(S(f))$ .

The proposition thus gives homeomorphisms

$$
\left| p \longmapsto | q \longmapsto T _ {p q} | \right| \approx \left| p \longmapsto \coprod_ {Y _ {p} \rightarrow Y _ {0}} B (Y _ {0} / f) \right|,
$$

$$
\left| q \longmapsto | p \longmapsto T _ {p q} | \right| \approx \left| q \longmapsto \coprod_ {X _ {0} \rightarrow \dots X _ {q}} B (\mathcal {C} ^ {\prime} / f X _ {0}) \right|.
$$

By the hypothesis of Theorem A

$$
B (\mathcal {C} ^ {\prime} / f X _ {0}) \cong * \text { and } B (Y _ {0} / f) \cong *.
$$

We still need the

Lemma If $X \mapsto B_X$ is a functor from $\mathcal{C}$ to topological spaces so that $B_X \cong *$, for all $X$ in $\mathcal{C}$, then

$$
\left| [ p ] \longmapsto \coprod_ {X _ {0} \rightarrow \dots \rightarrow X _ {p}} B _ {X _ {0}} \right| \cong \left| [ p ] \longmapsto \coprod_ {Y _ {0} \rightarrow \dots \rightarrow X _ {p}} \text { point } \right| = B C.
$$

To see this, consider  $\left|[p]\mapsto\coprod_{X_{0}\to\cdots\to X_{p}}B_{X_{0}}\right|$  and conclude that

$$
\left| [ p ] \longrightarrow \coprod_ {Y _ {p} \rightarrow \dots Y _ {0}} B (Y _ {0} / f) \right| \stackrel {\simeq} {\longrightarrow} B \mathcal {C} ^ {\prime},
$$

$$
\left| [ q ] \longrightarrow \coprod_ {X _ {0} \rightarrow \dots \rightarrow X _ {q}} B (\mathcal {C} ^ {\prime} / f X _ {0}) \right| \stackrel {\simeq} {\longrightarrow} B \mathcal {C}.
$$

Thus we find

$$
\begin{array}{c} B (S (f)) \xrightarrow {\simeq} B C ^ {\prime} \\ \Biggl \downarrow \simeq \\ B C \end{array}
$$

and compare this with the same thing for $\mathrm{id}_{\mathcal{C}'} : \mathcal{C}' \to \mathcal{C}'$:

$$
\begin{array}{c} \mathcal {C} ^ {\prime} \xleftarrow {} S (f) \xrightarrow {} \mathcal {C} \\ \Big \| \quad \Big | _ {\downarrow} \quad \Big | _ {\downarrow} \\ \mathcal {C} ^ {\prime} \xleftarrow {} S (\mathrm{id} _ {\mathcal {C}} ^ {\prime}) \xrightarrow {} \mathcal {C} ^ {\prime} \end{array}
$$

where the right-hand square of the diagram commutes. The argument above is natural in $f$ thus proving Theorem A.

Recall that if $E \xrightarrow{f} B$ is a map of spaces and $b \in B$, then the homotopy fiber of $f$ over $b$ is

$$
\begin{array}{r l} E (f; b) & = E \times_ {B} B ^ {I} \times_ {B} \{b \} \\ & = \{(e, \lambda): \lambda \text { is   a   path   from } f (e) \text { to } b \}. \end{array}
$$

This is the actual fiber over b of the Serre construction

![](images/page_174_image_2.jpg)

We get of course $e \in f^{-1}(b)$ and the homotopy exact sequence

$$
\dots \longrightarrow \pi_ {n + 1} \longrightarrow \pi_ {n} (E (f; b), \widetilde {e}) \longrightarrow \pi_ {n} (E, e) \longrightarrow \pi_ {n} (B, b) \longrightarrow \pi_ {n - 1} \longrightarrow \dots .
$$

Note that

$$
f ^ {- 1} b \subset E (f, b)
$$

via

$$
\widetilde {e} = (e, \text { constant   path })
$$

We call $f$ a quasi-fibration (in the sense of Dold-Thom) when the inclusion $f^{-1}b \subset E(f, b)$ is a weak homotopy equivalence for all $b \in B$.

Dold-Thom Example Let A be a “nice” subspace of a “nice” space X, where A is connected and has a base point, and let  $SP(X) = \cup_{n} X^{n} / \Sigma^{n}$  be the infinite symmetric product. We have also  $SP(X/A)$ , and the map

$$
S P (X) \longrightarrow S P (X / A)
$$

is a quasi-fibration (this is a theorem), where the fiber over the base point is  $SP(A)$ . We conclude that there is an exact sequence

$$
\dots \longrightarrow \pi_ {n} S P A \longrightarrow \pi_ {n} S P X \longrightarrow \pi_ {n} S P X / A \longrightarrow \dots
$$

We also have the

Theorem  $\pi_{n} SPX = \widetilde{H}_{n}(X, \mathbb{Z})$ .

A good paradigm for a quasi-fibration which is not a fibration is given by the natural mapping from the mapping cylinder of  $X \xrightarrow{f} Y$  to the unit interval, which is not a

fibration unless f is the identity map but is a quasi-fibration provided f is a homotopy equivalence.

Theorem B Suppose $f: \mathcal{C} \to \mathcal{C}'$ is so that for all $Y' \xrightarrow{u} Y$ in $\mathcal{C}'$, the functor $u^*: Y \setminus f \longrightarrow Y' \setminus f$ is a homotopy equivalence. Then $B(Y \setminus f)$ is homotopy equivalent to the homotopy fiber of $Bf$ over $Y$.

Proof We have

$$
\begin{array}{c}\left| [ p ] \longmapsto \coprod_ {Y _ {p} \rightarrow \dots \rightarrow Y _ {0}} B (Y _ {0} \backslash f) \right|\\\Bigg \downarrow\\\left| [ p ] \longmapsto \coprod_ {Y _ {p} \rightarrow \dots \rightarrow Y _ {0}} \text {point} \right|\end{array}
$$

This is a quasi-fibration from Dold-Thom theory because all specialization maps are homotopy equivalences by assumption.

As in Theorem A, we have

$$
\left| [ p ] \longrightarrow \coprod_ {Y _ {P} \rightarrow \dots \rightarrow Y _ {0}} B (Y _ {0} \backslash f) \right| = | [ q ] \longmapsto B (\mathcal {C} ^ {\prime} / X _ {0}) | \simeq B \mathcal {C}
$$

and

$$
\left| [ p ] \longmapsto \coprod_ {Y _ {p} \rightarrow \dots \rightarrow Y _ {0}} \text { point } \right| \simeq B C ^ {\prime}. \quad \square
$$

# Chapter 35 Homology of $Q(\mathcal{P}_A)$ and the Tits Complex

We begin with the

Example Take

$$
S P X \xrightarrow {f} S P X / A
$$

and let  $[y_{1},\cdots,y_{n}]\in SP(X/A)$ , where without loss of generality  $y_{i}\in X\backslash A$ . Then  $f^{-1}[y_{1},\cdots,y_{n}]$  is the union of  $[y_{1},\cdots,y_{n}]$  and any set in  $SP(A)$ . Specialization maps are multiplication by elements of  $SP(A)$ .  $SP(A)$  is a connected monoid, so these are homotopy equivalences.

Let $A$ be a Dedekind domain and $F$ its field of fractions. We defined $F_{n}Q(\mathcal{P}_{A})$ to be the full subcategory comprised of those $P$ with rank at most $n$. Then

$$
0 = F _ {0} \subset F _ {1} \subset \dots \subset \bigcup_ {n} F _ {n} = Q (\mathcal {P} _ {A}).
$$

Problem Compare the homology of  $F_{n}$  and  $F_{n-1}$ . To simplify what follows, assume  $\operatorname{Pic}(A)=0$ , so the only projective module P of rank n is  $A^{n}$  and

$$
\operatorname{Hom} _ {Q (\mathcal {P} _ {A})} (P, P) = \operatorname{Aut} (P) = \mathrm{GL} _ {n} (A).
$$

If we regard Aut $A^n$ as a category, then we have inclusions

$$
F _ {n - 1} \xrightarrow {i} F _ {n} <   \underset {j} {\longrightarrow} \text {Aut} A ^ {n}
$$

of categories. Recall from last term that for a functor $f: \mathcal{C} \to \mathcal{C}'$ and a functor $F: \mathcal{C} \to \mathrm{Ab}$, we have

$$
f _ {!} (F) (Y) = \underset {(X, f X \rightarrow Y)} {\operatorname{colim}} F (X).
$$

More generally, if $F_{\cdot}$ is a complex in $\operatorname{Funct}(\mathcal{C},\mathrm{Ab})$, then we have a complex $\mathbb{L}f_{1}(F_{\cdot})$ in $\operatorname{Funct}(\mathcal{C}',\mathrm{Ab})$ unique up to quasi-isomorphism. There is an isomorphism

$$
H _ {p} \left(\mathcal {C} ^ {\prime}, \mathbb {L} f _ {!} (F.)\right) \cong H _ {p} (\mathcal {C}, F.),
$$

and there is a spectral sequence with

$$
E _ {p q} ^ {2} = H _ {p} (\mathcal {C} ^ {\prime}, L _ {q} f _ {!} (F.)) \text {   converging   to   } H _ {n} (\mathcal {C} ^ {\prime}, \mathbb {L} f _ {!} (F.))
$$

with

$$
L _ {q} f _ {!} (P) (Y) = H _ {q} (f / Y, F \text {   pulled   back   to   } f / Y).
$$

Setting $\Gamma = \mathrm{GL}_n A$, if we put $f = j: \widetilde{\Gamma} \hookrightarrow F_n$, then

$j/p = \begin{cases} \varnothing, & \text{if } P \in F_{n-1}, \\ \text{the category whose objects are elements of } \operatorname{Hom}(A^n, P) \text{ and whose maps are given by composition with elements of } \Gamma, & \text{if rank } P = n. \end{cases}$

So if $M$ is any $\Gamma$-module, then

$$
L _ {q} j _ {!} (M) (P) = \left\{ \begin{array}{l l} 0, & \text { if } P \in F _ {n - 1}, \\ 0, & \text { if } P \cong A ^ {n} \text { and } q > 0, \\ M, & \text { if } P \cong A ^ {n} \text { and } q = 0, \end{array} \right.
$$

SO

$$
H _ {*} (F _ {n}, j _ {!} (M)) = H _ {*} (\Gamma , M).
$$

Note that  $j_{1}(M)$  is a typical functor on  $F_{n}$  with support  $\{A^{n}\}$ .

Now we consider $i:F_{n-1}\to F_n$. Then for $P\in F_{n-1}, i/p$ is a category with final object, hence $H_q(i/p,F)=0$, for $q>0$, and any $F:i/p\to\mathrm{Ab.}i/A^n$ is equivalent to the poset of proper layers in $F^n$, which in turn is equivalent to the suspension of $T(F^n)$, namely the poset of proper subspaces of $F^n$. Thus

$$
\begin{array}{r l} \widetilde {H} _ {k} (i / A ^ {n}, \mathbb {Z}) & = \widetilde {H} _ {k - 1} (T (F ^ {n}), \mathbb {Z}) \\ & = \left\{ \begin{array}{l l} 0, & k - 1 \neq n - 2, \\ I (F ^ {n}), & k - 1 = n - 2, \end{array} \right. \end{array}
$$

where $I(F^{n})$ is the Steinberg module of $F^{n}$. Now we have

$$
H _ {*} (F _ {n - 1}, \mathbb {Z}) = H _ {*} (F _ {n}, \mathbb {L} i _ {!} (\mathbb {Z})),
$$

$$
L _ {q} i _ {!} (\mathbb {Z}) (p) = \left\{ \begin{array}{l l} 0, q \neq 0, p \in F _ {n - 1}, \\ Z, q = 0, p \in F _ {n - 1}, \end{array} \right.
$$

and

$$
L _ {q}   i _ {!} (\mathbb {Z}) (A ^ {n}) = H _ {q} (i / A ^ {n}, \mathbb {Z}) = \left\{ \begin{array}{c c} 0, & q \neq 0, n - 1, \\ \mathbb {Z}, & q = 0, \\ I (F ^ {n}), & q = n - 1, \end{array} \right.
$$

provided $n \neq 1$. A formula valid even for $n = 1$ is an exact sequence

$$
0 \longleftarrow \mathbb {Z} \longleftarrow \mathbb {L} i _ {!} (\mathbb {Z}) \longleftarrow j _ {!} I (F ^ {n}) [ n - 1 ] \longleftarrow 0,
$$

and from this we get exact homology sequences

$$
\begin{array}{r l} & \dots \longleftarrow H _ {q} (F _ {n}, \mathbb {Z}) \longleftarrow H _ {q} (F _ {n}, \mathbb {L} i _ {!} (\mathbb {Z})) \longleftarrow H _ {q} (F _ {n}, j _ {!} I (F ^ {n}) [ n - 1 ]) \longleftarrow \dots \\ & \quad \Big \| \quad \Big \| \quad \Big \| \\ & \dots \longleftarrow H _ {q} (F _ {n}, \mathbb {Z}) \longleftarrow H _ {q} (F _ {n - 1}, \mathbb {Z}) \longleftarrow H _ {q - n + 1} (\mathrm{GL} _ {n} (A), I (F ^ {n})) \longleftarrow \dots \end{array}
$$

## The Tits complex

For a vector space $V$, $|T(V)|$ is the simplicial complex associated to the poset $T(V)$ of proper subspaces of $V$. Choose a line $L$ in $V$ and consider the map $W \mapsto W + L$. If this were a well-defined map $T(V) \to T(V)$, then $T(V)$ would be conically contractible since we would have

$$
W \leq W + L \geq L.
$$

But the map fails to be well-defined on

$$
\mathcal {H} _ {L} = \{\text { hyperplanes   } H \text {   with   } H + L = V \},
$$

and the above argument shows that the poset  $T(V) - \mathcal{H}_{L}$  is contractible.

Now for a vertex v in a simplicial complex K, we define

Link v = the subcomplex of simplices  $\tau$  with  $v \notin \tau$  such that  $v \cup \tau \in K$ ,

Star v = the subcomplex of simplices  $\sigma$  such that  $v \in \sigma$ ,

$\overline{\text{Star } v} = \text{ the subcomplex of simplices } \sigma \text{ with } v \cup \tau \in K,$

so we have

$\overline{\operatorname{Star} v} = \operatorname{Star} v \cup \operatorname{Link} v$.

Then for any v, we have

$$
K = (K - \text { Star } v) \bigcup_ {\text { Link } v} \overline {{\text { Star } v}},
$$

SO

$$
| T (v) | = \bigcup_ {H \in \mathcal {H} _ {L}} | T (v) - \mathcal {H} _ {L} | \cup \bigcup_ {\text { Link } H} \text { cone   on   Link } (H)
$$

since no two H in  $H_{L}$  form a simplex. Then since  $|T(v)-\mathcal{H}_{L}|\cong*$ , we find

$$
| T (v) | \simeq \bigcup_ {H \in \mathcal {H} _ {L}} S \operatorname{Link} (H).
$$

But Link $(H) = |T(H)|$, so by induction $|T(v)|$ is a bouquet of spheres, and

$$
\# \text { spheres   in } | T (P ^ {n}) | = (\# H \text { in } \mathcal {H} _ {L}) \cdot (\# \text { spheres   in } | T (P ^ {n - 1}) |).
$$

Moreover, for $F$ a finite field of characteristic $q$, we have $\# H$ in $\mathcal{H}_L = q^n$.

It follows from this argument that once a flag  $0 < F_{1} < F_{2} < \cdots < F_{n-1} < V$  is chosen, then  $I(V)$  has a basis indexed in a natural way by flags

$$
V > H _ {1} > H _ {2} > \dots > H _ {n - 1} > 0
$$

with $H_{i} \oplus F_{i} = V$ for each $i$. As a module over the unipotent radical of the Borel subgroup $B^{n}$ of $\operatorname{Aut}(V) = \operatorname{GL}_{n}(F)$ fixing $\{F_{i}\}$, $I(V)$ is free, i.e.,

$$
I (V) \simeq \mathbb {Z} [ B ^ {n} ].
$$

For $F = \mathbb{F}_{q}, B^{n}$ is a Sylow $p$-subgroup and $I(V)$ is projective over Sylow subgroups. It follows that $I(K)_{p}$ is projective over $\mathbb{Z}_{p}[\mathrm{GL}_{n}(F)]$.