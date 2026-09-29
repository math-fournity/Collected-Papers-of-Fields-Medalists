# A theory of regularity structures

M. Hairer

Received: 1 October 2013 / Accepted: 21 January 2014 / Published online: 14 March 2014 © Springer-Verlag Berlin Heidelberg 2014

Abstract We introduce a new notion of “regularity structure” that provides an algebraic framework allowing to describe functions and/or distributions via a kind of “jet” or local Taylor expansion around each point. The main novel idea is to replace the classical polynomial model which is suitable for describing smooth functions by arbitrary models that are purpose-built for the problem at hand. In particular, this allows to describe the local behaviour not only of functions but also of large classes of distributions. We then build a calculus allowing to perform the various operations (multiplication, composition with smooth functions, integration against singular kernels) necessary to formulate fixed point equations for a very large class of semilinear PDEs driven by some very singular (typically random) input. This allows, for the first time, to give a mathematically rigorous meaning to many interesting stochastic PDEs arising in physics. The theory comes with convergence results that allow to interpret the solutions obtained in this way as limits of classical solutions to regularised problems, possibly modified by the addition of diverging counterterms. These counterterms arise naturally through the action of a “renormalisation group” which is defined canonically in terms of the regularity structure associated to the given class of PDEs. Our theory also allows to easily recover many existing results on singular stochastic PDEs (KPZ equation, stochastic quantisation equations, Burgers-type equations) and to understand them as particular instances of a unified framework. One surprising insight is that in all of these instances local solutions are actually “smooth” in the sense that they can be approximated locally to arbitrarily high degree as linear combinations of a fixed family of random functions/distributions that play the role of “polynomials” in the theory. As an example of a novel application, we solve the long-standing problem of building a natural Markov process that is symmetric with respect to the (finite volume) measure describing the$\Phi _ { 3 } ^ { 4 }$Euclidean quantum field theory. It is natural to conjecture that the Markov process built in this way describes the Glauber dynamic of 3-dimensional ferromagnets near their critical temperature.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sub>M. Hairer (</sub>B<sub>)</sub></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Mathematics Department, University of Warwick, Coventry CV4 7AL, U.K e-mail: M.Hairer@Warwick.ac.uk</span></small>

## Mathematics Subject Classification (2000) 60H15 81S20 82C28

## Contents

1 Introduction 271  
1.1 Some examples of interesting stochastic PDEs 274  
1.2 On regularity structures 277  
1.3 Main results: abstract theory 278  
1.4 On renormalisation procedures 281  
1.5 Main results: applications 284  
1.5.1 Generalisation of the parabolic Anderson model 284  
1.5.2 The dynamical $\Phi_3^4$ model 285  
1.5.3 General methodology 286  
1.6 Alternative theories 287  
1.6.1 Bony's paraproduct 287  
1.6.2 Colombeau's generalised functions 289  
1.6.3 White noise analysis 290  
1.6.4 Rough paths 290  
1.7 Notations 291  
2 Abstract regularity structures 291  
2.1 Basic properties of regularity structures 294  
2.2 The polynomial regularity structure 295  
2.3 Models for regularity structures 299  
2.4 Automorphisms of regularity structures 304  
3 Modelled distributions 305  
3.1 Elements of wavelet analysis 310  
3.2 A convergence criterion in $\mathcal{C}_5^\alpha$ 313  
3.3 The reconstruction theorem for distributions 318  
3.4 The reconstruction theorem for functions 324  
3.5 Consequences of the reconstruction theorem 325  
3.6 Symmetries 328  
4 Multiplication 331  
4.1 Classical multiplication 338  
4.2 Composition with smooth functions 340  
4.3 Relation to Hopf algebras 343  
4.4 Rough paths 346  
5 Integration against singular kernels 350  
5.1 Proof of the extension theorem 359  
5.2 Multi-level Schauder estimate 369  
5.3 The symmetric case 376

5.4 Differentiation . 377   
6 Singular modelled distributions . 379   
6.1 Reconstruction theorem . 384   
6.2 Multiplication . 387   
6.3 Composition with smooth functions . 390   
6.4 Differentiation . 393   
6.5 Integration against singular kernels . 394   
7 Solutions to semilinear (S)PDEs . 398   
7.1 Short-time behaviour of convolution kernels . 399   
7.2 The effect of the initial condition . 404   
7.3 A general fixed point map . 408   
8 Regularity structures for semilinear (S)PDEs . 415   
8.1 General algebraic structure . 418   
8.2 Realisations of the general algebraic structure . 433   
8.3 Renormalisation group associated to the general algebraic structure . 437   
9 Two concrete renormalisation procedures . 446   
9.1 Renormalisation group for (PAMg) . 447   
9.2 Renormalisation group for the dynamical $\Phi_3^4$ model . 448   
9.3 Renormalised equations for (PAMg) . 450   
9.4 Solution theory for the dynamical $\Phi_3^4$ model . 455   
10 Homogeneous Gaussian models . 463   
10.1 Wiener chaos decomposition . 463   
10.2 Gaussian models for regularity structures . 466   
10.3 Functions with prescribed singularities . 471   
10.4 Wick renormalisation and the continuous parabolic Anderson model . 479   
10.5 The dynamical $\Phi_3^4$ model . 487   
Acknowledgments . 496   
Appendix A: A generalised Taylor formula . 496   
Appendix B: Symbolic index . 498   
References . 500

## 1 Introduction

The purpose of this article is to develop a general theory allowing to formulate, solve and analyse solutions to semilinear stochastic partial differential equations of the type

$$
\mathcal {L} u = F (u, \xi),\tag{1.1}
$$

where$\mathcal { L }$is a (typically parabolic but possibly elliptic) differential operator, ξ is a (typically very irregular) random input, and$F$is some nonlinearity. The nonlinearity$F$does not necessarily need to be local, and it is also allowed to depend on some partial derivatives of u, as long as these are of strictly lower order than${ \mathcal { L } } .$One example of random input that is of particular interest in many situations arising from the large-scale behaviour of some physical microscopic model is that of white noise (either space-time or just in space), but let us stress immediately that Gaussianity is not essential to the theory, although it simplifies certain arguments. Furthermore, we will assume that$F$ depends on$\xi$in an affine way, although this could in principle be relaxed to some polynomial dependencies.

Our main assumption will be that the equation described by (1.1) is locally subcritical (see Assumption 8.3 below). Roughly speaking, this means that if one rescales (1.1) in a way that keeps both$\mathcal { L } u$and$\xi$invariant then, at small scales, all nonlinear terms formally disappear. A “naïve” approach to such a problem is to consider a sequence of regularised problems given by

$$
\mathcal {L} u _ {\varepsilon} = F (u _ {\varepsilon}, \xi_ {\varepsilon}),\tag{1.2}
$$

where$\xi _ { \varepsilon }$is some smoothened version of$\xi$(obtained for example by convolution with a smooth mollifier), and to show that$u _ { \varepsilon }$converges to some limit u which is independent of the choice of mollifier.

This approach does in general fail, even under the assumption of local subcriticality. Indeed, consider the KPZ equation on the line [76], which is the stochastic PDE formally given by

$$
\partial_ {t} h = \partial_ {x} ^ {2} h + (\partial_ {x} h) ^ {2} + \xi ,\tag{1.3}
$$

where$\xi$denotes space-time white noise. This is indeed of the form (1.1) with$\mathcal { L } = \partial _ { t } - \partial _ { x } ^ { 2 }$and$F ( h , \xi ) = ( \partial _ { x } h ) ^ { 2 } + \xi$and it is precisely this kind of problem that we have in mind. Furthermore, if we zoom into the small scales by writing$\tilde { h } ( x , t ) = \delta ^ { - 1 / 2 } h ( \delta x , \delta ^ { 2 } t )$and$\tilde { \xi } ( x , t ) = \delta ^ { 3 / 2 } \xi ( \delta x , \delta ^ { 2 } t )$for some small parameter δ, then we have that on the one hand$\tilde { \xi }$equals$\xi$in distribution, and on the other hand$\tilde { h }$solves

$$
\partial_ {t} \tilde {h} = \partial_ {x} ^ {2} \tilde {h} + \delta^ {1 / 2} (\partial_ {x} \tilde {h}) ^ {2} + \tilde {\xi}.
$$

As$\delta  0$(which corresponds to probing solutions at very small scales), we see that, at least at a formal level, the nonlinearity vanishes and we simply recover the stochastic heat equation. This shows that the KPZ equation is indeed locally subcritical in dimension 1. On the other hand, if we simply replace$\xi$by$\xi _ { \varepsilon }$in (1.3) and try to take the limit$\varepsilon  0$, solutions diverge due to the ill-posedness of the term$( \partial _ { x } h ) ^ { 2 }$

However, in this case, it is possible to devise a suitable renormalisation procedure [8,59], which essentially amounts to subtracting a very large constant to the right hand side of a regularised version of (1.3). This then ensures that the corresponding sequence of solutions converges to a finite limit. The pur pose of this article is to build a general framework that goes far beyond the example of the KPZ equation and allows to provide a robust notion of solution to a very large class of locally subcritical stochastic PDEs that are classically ill-posed.

Remark 1.1 In the language of quantum field theory (QFT), equations that are subcritical in the way just described give rise to “superrenormalisable” theories. One major difference between the results presented in this article and most of the literature on quantum field theory is that the approach explored here is truly non-perturbative and therefore allows one to deal also with some non-polynomial equations like (PAMg) or (KPZ) below. We furthermore consider parabolic problems, where we need to deal with the problem of initial conditions and local (rather than global) solutions. Nevertheless, the mathematical analysis of QFT was one of the main inspirations in the development of the techniques and notations presented in Sects. 8 and 10.

Conceptually, the approach developed in this article for formulating and solving problems of the type (1.1) consists of three steps.

1. In an algebraic step, one first builds a “regularity structure”, which is sufficiently rich to be able to describe the fixed point problem associated to (1.1). Essentially, a regularity structure is a vector space that allows to describe the coefficients in a kind of “Taylor expansion” of the solution around any point in space-time. The twist is that the “model” for the Taylor expansion does not only consist of polynomials, but can in general contain other functions and / or distributions built from multilinear expressions involving ξ.

2. In an analytical step, one solves the fixed point problem formulated in the algebraic step. This allows to build an “abstract” solution map to (1.1). In a way, this is a closure procedure: the abstract solution map essentially describes all “reasonable” limits that can be obtained when solving (1.1) for sequences of regular driving noises that converge to something very rough.

3. In a final probabilistic step, one builds a “model” corresponding to the Gaussian process ξ we are really interested in. In this step, one typically has to choose a renormalisation procedure allowing to make sense offinitely many products of distributions that have no classical meaning. Although there is some freedom involved, there usually is a canonical model, which is “almost unique” in the sense that it is naturally parametrized by elements in some finite-dimensional Lie group, which has an interpretation as a “renormalisation group” for (1.1).

We will see that there is a very general theory that allows to build a “black box”, which performs the first two steps for a very large class of stochastic PDEs. For the last step, we do not have a completely general theory at the moment, but we have a general methodology, as well as a general toolbox, which seem to be very useful in practice.

## 1.1 Some examples of interesting stochastic PDEs

Some examples of physically relevant equations that in principle fall into the category of problems amenable to analysis via the techniques developed in this article include:

The stochastic quantisation of$\Phi ^ { 4 }$quantum field theory in dimension 3. This formally corresponds to the equation

$$
\partial_ {t} \Phi = \Delta \Phi - \Phi^ {3} + \xi ,\tag{\((\Phi^{4})\}
$$

where$\xi$denotes space-time white noise and the spatial variable takes values in the 3-dimensional torus, see [89]. Formally, the invariant measure of$( \Phi ^ { 4 } )$ (or rather a suitably renormalised version of it) is the measure on Schwartz distributions associated to Bosonic Euclidean quantum field theory in 3 space-time dimensions. The construction of this measure was one of the major achievements ofthe programme ofconstructive quantum field theory, see the articles [37,39,40,47,49], as well as the monograph [48] and the references therein.

In two spatial dimensions, this problem was previously treated in [5,34]. It has also been argued more recently in [4] that even though it is formally symmetric, the 3-dimensional version of this model is not amenable to analysis via Dirichlet forms. In dimension 4, the model$( \Phi ^ { 4 } )$becomes critical and one does not expect to be able to give it any non-trivial (i.e. non-Gaussian in this case) meaning as a random field for$d \ge 4 .$, see for example [3,41,75].

Another reason why$( \Phi ^ { 4 } )$is a very interesting equation to consider is that it is related to the behaviour of the 3D Ising model under Glauber dynamic near its critical temperature. For example, it was shown in [16] that the onedimensional version of this equation describes the Glauber dynamic of an Ising chain with a Kac-type interaction at criticality. In [50], it is argued that the same should hold true in higher dimensions and an argument is given that relates the renormalisation procedure required to make sense of $( \Phi ^ { 4 } )$to the precise choice of length scale as a function of the distance from criticality.

The continuous parabolic Anderson model

$$
\partial_ {t} u = \Delta u + \xi u,\tag{PAM}
$$

where$\xi$denotes spatial white noise that is constant in time. For smooth noise, this problem has been treated extensively in [24]. While the problem with$\xi$given by spatial white noise is well-posed in dimension 1 (and a good approximation theory exists, see [73]), it becomes ill-posed already in dimension 2. One does however expect this problem to be renormalisable with the help of the techniques presented here in spatial dimensions 2 and 3. Again, dimension 4 is critical and one does not expect any continuous version of the model for$d \geq 4$

KPZ-type equations of the form

$$
\partial_ {t} h = \partial_ {x} ^ {2} h + g _ {1} (h) (\partial_ {x} h) ^ {2} + g _ {2} (h) \partial_ {x} h + g _ {3} (h) + g _ {4} (h) \xi ,\tag{KPZ}
$$

where$\xi$denotes space-time white noise and the$g _ { i }$are smooth functions. While the classical KPZ equation can be made sense of via the Cole–Hopf transform [8,25,64], this trick fails in the more general situation given above or in the case of a system of coupled KPZ equations, which arises naturally in the study of chains of nonlinearly interacting oscillators [10]. A more robust concept ofsolution for the KPZ equation where$g _ { 4 } = g _ { 1 } = 1$ and$g _ { 2 } = g _ { 3 } = 0$, as well as for a number of other equations belonging to the class (KPZ) was given recently in the series of articles [57–59,72], using ideas from the theory of rough paths that eventually lead to the development of the theory presented here. The more general class of equations (KPZ) is of particular interest since it is formally invariant under changes of coordinates and would therefore be a good candidate for describing a natural “free evolution” for loops on a manifold, which generalises the stochastic heat equation. See [42] for a previous attempt in this direction and [9] for some closely related work.

The Navier–Stokes equations with very singular forcing

$$
\partial_ {t} v = \Delta v - P (v \cdot \nabla) v + \xi ,\tag{SNS}
$$

where P is Leray’s projection onto the space of divergence-free vector fields. If we take$\xi$to have the regularity of space-time white noise, (SNS) is already classically ill-posed in dimension 2, although one can circumvent this problem, see [1,2,33]. However, it turns out that the actual critical dimension is 4 again, so that we can hope to make sense of (SNS) in a suitably renormalised sense in dimension 3 and construct local solutions there.

One common feature of all of these problems is that they involve products between terms that are too irregular for such a product to make sense as a continuous bilinear form defined on some suitable function space. Indeed, denoting by$\mathcal { C ^ { \alpha } }$for$\alpha < 0$the Besov space$B _ { \infty , \infty } ^ { \alpha }$, it is well-known that, for non-integer values of α and$\beta _ { \cdot }$, the map$( u , v ) \mapsto u v$is well defined from $\mathcal { C } ^ { \alpha } \times \mathcal { C } ^ { \beta }$into some space of Schwartz distributions if and only if$\alpha + \beta > 0$ (see for example [6]), which is quite easily seen to be violated in all of these examples.

In the case of second-order parabolic equations, it is straightforward to verify (see also Sect. 6 below) that, for fixed time, the solutions to the linear equation

$$
\partial_ {t} X = \Delta X + \xi ,
$$

belong to$\mathcal { C ^ { \alpha } }$for$\begin{array} { r } { \alpha < 1 - \frac { d } { 2 } } \end{array}$when$\xi$is space-time white noise and$\begin{array} { r } { \alpha < 2 - \frac { d } { 2 } } \end{array}$ when$\xi$is purely spatial white noise. As a consequence, one expects - to take values in$\mathcal { C } ^ { \alpha }$with$\alpha < - 1 / 2$, so that$\Phi ^ { 3 }$is ill-defined. In the case of (PAM), one expects u to take values in$\mathcal { C } ^ { \alpha }$with$\alpha < 2 - d / 2$, so that the product$u \xi$is well-posed only for$d < 2$. As in the case of$( \Phi ^ { 4 } )$, dimension 2 is “borderline” with the appearance of logarithmic divergencies, while dimension 3 sees the appearance of algebraic divergencies and logarithmic subdivergencies. Note also that, since$\xi$is white noise in space, there is no theory of stochastic integration available to make sense of the product$u \xi$, unlike in the case when $\xi$is space-time white noise. (See however [46] for a very recent article solving this particular problem in dimension 2.) Finally, one expects the function h in (KPZ) to take values in$\mathcal { C } ^ { \alpha }$for$\begin{array} { r } { \alpha < \frac { 1 } { 2 } } \end{array}$, so that all the terms appearing in (KPZ) are ill-posed, except for the term involving$g _ { 3 }$

Historically, such situations have been dealt with by replacing the products in question by their Wick ordering with respect to the Gaussian structure given by the solution to the linear problem$\mathcal { L } u = \xi$, see for example [5,33–35,74] and references therein. In many of the problems mentioned above, such a technique is bound to fail due to the presence of additional subdivergencies. Furthermore, we would like to be able to consider terms like$g _ { 1 } ( h ) ( \partial _ { x } h ) ^ { 2 }$in (KPZ) where$g _ { 1 }$is an arbitrary smooth function, so that it is not clear at all what a Wick ordering would mean. Over the past few years, it has transpired that the theory of controlled rough paths [54,55,82] could be used in certain situations to provide a meaning to the ill-posed nonlinearities arising in a class of Burgers-type equations [57,63,70,72], as well as in the KPZ equation [59]. That theory however is intrinsically a one-dimensional theory, which is why it has so far only been successfully applied to stochastic evolution equations with one spatial dimension.

In general, the theory of rough paths and its variants do however allow to deal with processes taking values in an infinite-dimensional space. It has therefore been applied successfully to stochastic PDEs driven by signals that are very rough in time (i.e. rougher than white noise), but at the expense of requiring additional spatial regularity [19,53,96].

One very recent attempt to use related ideas in higher dimensions was made in [46] by using a novel theory of “controlled distributions”. With the help of this theory, which relies heavily on the use of Bony’s paraproduct, the authors can treat for example (PAM) (as well as some nonlinear variant thereof)

in dimension$d \ : = \ : 2$. The present article can be viewed as a far-reaching generalisation of related ideas, in a way which will become clearer in Sect. 2 below.

## 1.2 On regularity structures

The main idea developed in the present work is that of describing the “regularity” of a function or distribution in a way that is adapted to the problem at hand. Traditionally, the regularity of a function is measured by its proximity to polynomials. Indeed, we say that a function u$\mathbf R ^ { d } \to \mathbf R$is of class$\mathcal { C ^ { \alpha } }$with $\alpha > 0 \mathrm { i f } .$, for every point$x \in \mathbf { R } ^ { d }$, it is possible to find a polynomial$P _ { x }$such that

$$
| f (y) - P _ {x} (y) | \lesssim | x - y | ^ {\alpha}.
$$

What is so special about polynomials? For one, they have very nice algebraic properties: products of polynomials are again polynomials, and so are their translates and derivatives. Furthermore, a monomial is a homogeneous function: it behaves at the origin in a self-similar way under rescalings. The latter property however does rely on the choice of a base point: the polynomial $y \mapsto ( y - x ) ^ { k }$is homogeneous of degree k when viewed around x, but it is made up from a sum of monomials with different homogeneities when viewed around the origin.

In all of the examples considered in the previous subsection, solutions are expected to be extremely irregular (at least in the classical sense!), so that polynomials alone are a very poor model for trying to describe them. However, because of local subcriticality, one expects the solutions to look at smallest scales like solutions to the corresponding linear problems, so we are in situations where it might be possible to make a good “guess” for a much more adequate model allowing to describe the small-scale structure of solutions.

Remark 1.2 In the particular case of functions of one variable, this point of view has been advocated by Gubinelli in [54,55] (and to some extent by Davie in [31]) as a way of interpreting Lyons’s theory of rough paths. (See also [45,78,79] for some recent monographs surveying that theory.) That theory does however rely very strongly on the notion of “increments” which is very one-dimensional in nature and forces one to work with functions, rather than general distributions. In a more subtle way, it also relies on the fact that onedimensional integration can be viewed as convolution with the Heaviside function, which is locally constant away from 0, another typically one-dimensional feature.

This line of reasoning is the motivation behind the introduction of the main novel abstract structure proposed in this work, which is that of a “regularity structure”. The precise definition will be given in Definition 2.1 below, but the basic idea is to fix a finite family of functions (or distributions!) that will play the role of polynomials. Typically, this family contains all polynomials, but it may contain more than that. A simple way of formalising this is that one fixes some abstract vector space T where each basis vector represents one of these distributions. A “Taylor expansion” (or “jet”) is then described by an element$a \in T$which, via some “model” -$T  S ^ { \prime } ( \mathbf { R } ^ { d } )$, one can interpret as determining some distribution$\pmb { \Pi } a \in \mathcal { S } ^ { \prime } ( \mathbf { R } ^ { d } )$. In the case of polynomials, $T$would be the space of abstract polynomials in d commuting indeterminates and - would be the map that realises such an abstract polynomial as an actual function on$\mathbf { R } ^ { d }$

As in the case of polynomials, different distributions have different homogeneities (but these can now be arbitrary real numbers!), so we have a splitting of$T$into “homogeneous subspaces”$T _ { \alpha }$. Again, as in the case of polynomials, the homogeneity of an element$a$describes the behaviour of$\Pi a$around some base point, say the origin 0. Since we want to be able to place this base point at an arbitrary location we also postulate that one has a family of invertible linear maps$F _ { x } \colon T \to T$such that if$a \ \in \ T _ { \alpha }$, then$\Pi F _ { x } a$exhibits behaviour “of order$\alpha ^ { \prime \prime }$(this will be made precise below in the case of distribution) near the point x. In this sense, the map$\Pi _ { x } = \Pi \circ F _ { x }$plays the role of the “polynomials based at$x '$, while the map$\Gamma _ { x y } = F _ { x } ^ { - 1 } \circ F _ { y }$plays the role of a “translation operator” that allows to rewrite a “jet based at$y '$into a “jet based at$x '$

We will endow the space of all models (-, F) as above with a topology that enforces the correct behaviour of$\Pi _ { x }$near each point x, and furthermore enforces some natural notion of regularity of the map$x \mapsto F _ { x }$. The important remark is that although this turns the space of models into a complete metric space, it does not turn it into a linear (Banach) space! It is the intrinsic nonlinearity of this space which allows to encode the subtle cancellations that one needs to be able to keep track of in order to treat the examples mentioned in Sect. 1.1. Note that the algebraic structure arising in the theory of rough paths (truncated tensor algebra, together with its group-like elements) can be viewed as one particular example of an abstract regularity structure. The space of rough paths with prescribed Hölder regularity is then precisely the corresponding space of models. See Sect. 4.4 for a more detailed description of this correspondence.

## 1.3 Main results: abstract theory

Let us now expose some of the main abstract results obtained in this article. Unfortunately, since the precise set-up requires a number of rather lengthy definitions, we cannot give precise statements here. However, we would like to provide the reader with a flavour of the theory and refer to the main text for more details.

One of the main novel definitions consists in spaces$\mathcal { D } ^ { \gamma }$and$\mathcal { D } _ { \alpha } ^ { \gamma }$(see Definition 3.1 and Remark 3.5 below) which are the equivalent in our framework to the usual spaces$\mathcal { C } ^ { \gamma }$. They are given in terms of a “local Taylor expansion of order$\gamma ^ { \ast }$at every point, together with suitable regularity assumption. Here, the index$\gamma$measures the order of the expansion, while the index α (if present) denotes the lowest homogeneity of the different terms appearing in the expansion. In the case of regular Taylor expansions, the term with the lowest homogeneity is always the constant term, so one has$\alpha = 0$. However, since we allow elements of negative homogeneity, one can have$\alpha \leq 0$in general. Unlike the case of regular Taylor expansions where the first term always consists of the value of the function itself, we are here in a situation where, due to the fact that our “model” might contain elements that are distributions, it is not clear at all whether these “jets” can actually be patched together to represent an actual distribution. The reconstruction theorem, Theorem 3.10 below, states that this is always the case as soon as$\gamma > 0$. Loosely speaking, it states the following, where we again write$\mathcal { C ^ { \alpha } }$for the Besov space$B _ { \infty , \infty } ^ { \alpha }$ (Note that with this notation$\mathcal { C } ^ { 0 }$really denotes the space$L ^ { \infty } , { \mathcal { C } } ^ { 1 }$the space of Lipschitz continuous functions, etc. This is consistent with the usual notation for non-integer values of α.)

Theorem 1.3 (Reconstruction) For every$\gamma > 0$and$\alpha \leq 0 ,$, there exists a unique continuous linear map R$\mathcal { D } _ { \alpha } ^ { \gamma }  \mathcal { C } ^ { \alpha } ( \mathbf { R } ^ { d } )$with the property that, in a neighbourhood ofsize ε around any$\boldsymbol { x } \in \mathbf { R } ^ { d } , \mathcal { R } f$is approximated by$\Pi _ { x } f ( x )$ the jet described by$f ( x )$, up to an error oforder$\varepsilon ^ { \gamma }$

The reconstruction theorem shows that elements$f \in { \mathcal { D } } ^ { \gamma }$uniquely describe distributions that are modelled locally on the distributions described by $\Pi _ { x } f ( x )$. We therefore call such an element$f$a “modelled distribution”. At this stage, the theory is purely descriptive: given a model of a regularity structure, it allows to describe a large class of functions and / or distributions that “locally look like” linear combinations of the elements in the model. We now argue that it is possible to construct a whole calculus that makes the theory operational, and in particular sufficiently rich to allow to formulate and solve large classes of semilinear PDEs.

One of the most important and non-trivial operations required for this is multiplication. Indeed, one of the much lamented drawbacks of the classical theory ofSchwartz distributions is that there is no canonical way ofmultiplying them [92]. As a matter of fact, it is in general not even possible to multiply a distribution with a continuous function, unless the said function has sufficient regularity.

The way we use here to circumvent this problem is to postulate the values of the products between elements of our model. If the regularity structure is sufficiently large to also contain all of these products (or at least sufficiently many of them in a sense to be made precise), then one can simply perform a pointwise multiplication of the jets of two modelled distributions at each point. Our main result in this respect is that, under some very natural structural assumptions, such a product is again a modelled distribution. The following is a loose statement of this result, the precise formulation of which is given in Theorem 4.7 below.

Theorem 1.4 (Multiplication) Let be a suitable product on T and let$f _ { 1 } \in$ $\mathcal { D } _ { \alpha _ { 1 } } ^ { \gamma _ { 1 } }$and$f _ { 2 } \in \mathcal { D } _ { \alpha _ { 2 } } ^ { \gamma _ { 2 } }$with$\gamma _ { i } > 0 .$. Set$\alpha = \alpha _ { 1 } + \alpha _ { 2 }$and$\gamma = ( \gamma _ { 1 } + \alpha _ { 2 } ) \wedge ( \gamma _ { 2 } + \alpha _ { 1 } )$ Then, the pointwise product$f _ { 1 } \star f _ { 2 }$belongs to$\mathcal { D } _ { \alpha } ^ { \gamma }$

In the case of$f \in \mathcal { D } _ { 0 } ^ { \gamma }$, all terms in the local expansion have positive homogeneity, so that$\mathcal { R } f$is actually a function. It is then of course possible to compose this function with any smooth function$g .$The non-trivial fact is that the new function obtained in this way does also have a local “Taylor expansion” around every point which is typically of the same order as for the original function$f$. The reason why this statement is not trivial is that the function$\mathcal { R } f$does in general not possess much “classical” regularity, so that$\mathcal { R } f$typically does not belong to$\mathcal { C } ^ { \gamma }$. Our precise result is the content of Theorem 4.16 below, which can be stated loosely as follows.

Theorem 1.5 (Smooth functions) Let g$\mathbf R  \mathbf R$be a smooth function and consider a regularity structure endowed with a product satisfying suitable compatibility assumptions. Then, for$\gamma > 0$, one can build a map$\mathcal { G } \colon \mathcal { D } _ { 0 } ^ { \gamma }$ $\mathcal { D } _ { 0 } ^ { \gamma }$such that the identity$( \mathcal { R } \mathcal { G } ( f ) ) ( x ) = g ( ( \mathcal { R } f ) ( x ) )$) holdsfor every$\boldsymbol { x } \in \mathbf { R } ^ { d }$

The final ingredient that is required in any general solution theory for semi-linear PDEs consists in some regularity improvement arising from the linear part of the equation. One of the most powerful class of such statements is given by the Schauder estimates. In the case of convolution with the Green’s function$G$of the Laplacian, the Schauder estimates state that if$f \in { \mathcal { C } } ^ { \alpha }$, then $G * f \in \mathcal { C } ^ { \alpha + 2 }$, unless$\alpha + 2 \in \mathbf { N }$. (In which case some additional logarithms appear in the modulus of continuity of$G * f . )$One of the main reasons why the theory developed in this article is useful is that such an estimate still holds when$f \in \mathcal { D } ^ { \alpha }$. This is highly non-trivial since it involves “guessing” an expansion for the local behaviour of$G * \mathcal { R } f$up to sufficiently high order. Somewhat surprisingly, it turns out that even though the convolution with$G$is not a local operator at all, its action on the local expansion of a function is local, except for those coefficients that correspond to the usual polynomials.

One way of stating our result is the following, which will be reformulated more precisely in Theorem 5.12 below.

Theorem 1.6 (Multi-level Schauder estimate) Let$K \colon \mathbf { R } ^ { d } \setminus \{ 0 \}$R be a smooth kernel with a singularity oforder$\beta - d$at the originfor some$\beta > 0$ Then, under certain natural assumptions on the regularity structure and the model realising it, and provided that$\boldsymbol { \gamma } + \boldsymbol { \beta } \not \in { \bf N } ,$, one can constructfor$\gamma > 0$ a linear operator$K _ { \gamma } \colon { \mathcal { D } } _ { \alpha } ^ { \gamma } \to { \mathcal { D } } _ { ( \alpha + \beta ) \wedge 0 } ^ { \gamma + \beta }$such that the identity

$$
\mathcal {R K} _ {\gamma} f = K * \mathcal {R} f,
$$

holds for every$f \in { \mathcal { D } } _ { \alpha } ^ { \gamma }$. Here, denotes the usual convolution between two functions / distributions.

We call this a “multi-level” Schauder estimate because it is a statement not just about f itself but about every “layer” appearing in its local expansion.

Remark 1.7 The precise formulation of the multi-level Schauder estimate allows to specify a non-uniform scaling of$\mathbf { R } ^ { d }$. This is very useful for example when considering the heat kernel which scales differently in space and in time. In this case, Theorem 1.6 still holds, but all regularity statements have to be interpreted in a suitable sense. See Sects. 2.3 and 5 below for more details.

At this stage, we appear to possibly rely very strongly on the various still unspecified structural assumptions that are required of the regularity structure and of the model realising it. The reason why, at least to some extent, this can be “brushed under the rug” without misleading the reader is the following result, which is a synthesis of Proposition 4.11 and Theorem 5.14 below.

Theorem 1.8 (Extension theorem) It is always possible to extend a given regularity structure in such a way that the assumptions implicit in the statements ofTheorems 1.4–1.6 do hold.

Loosely speaking, the idea is then to start with the “canonical” regularity structure corresponding to classical Taylor expansions and to enlarge it by successively applying the extension theorem, until it is large enough to allow a closed formulation of the problem one wishes to study as a fixed point map.

## 1.4 On renormalisation procedures

The main problem with the strategy outlined above is that while the extension of an abstract regularity structure given by Theorem 1.8 is actually very explicit and rather canonical, the corresponding extension of the model ( , F) is unique (and continuous) only in the case of the multi-level Schauder theorem and the composition by smooth functions, but not in the case of multiplication when some of the homogeneities are strictly negative. This is a reflection of the fact that multiplication between distributions and functions that are too rough simply cannot be defined in any canonical way [92]. Different non-canonical choices of product then yield truly different solutions, so one might think that the theory is useless at selecting one “natural” solution process.

If the driving noise$\xi$in any of the equations from Sect. 1.1 is replaced by a smooth approximation$\xi ^ { ( \varepsilon ) }$, then the associated model for the corresponding regularity structure also consists of smooth functions. In this case, there is of course no problem in multiplying these functions, and one obtains a canonical sequence of models$( \hat { \Pi } ^ { ( \varepsilon ) } , \bar { F } ^ { ( \varepsilon ) } )$) realising our regularity structure. (See Sect. 8.2 for details of this construction.) At fixed$\varepsilon ,$, our theory then simply yields some very local description of the corresponding classical solutions. In some special cases, the sequence$( \Pi ^ { ( \varepsilon ) } , F ^ { ( \varepsilon ) } )$) converges to a limit that is independent of the regularisation procedure for a relatively large class of such regularisations. In particular, due to the symmetry of finite-dimensional control systems under time reversal, this is often the case in the classical theory of rough paths, see [28,44,82].

One important feature of the regularity structures arising naturally in the context of solving semilinear PDEs is that they come with a natural finitedimensional group R of transformations that act on the space of models. In some examples (we will treat the case of$( \Phi ^ { 4 } )$with$d \ : = \ : 3$in Sect. 10.5 and a generalisation of (PAM) with$d = 2$in Sect. 10.4), one can explicitly exhibit a subgroup$\Re _ { 0 }$of R and a sequence of elements$M _ { \varepsilon } \in \Re _ { 0 }$such that the “renormalised” sequence$M _ { \varepsilon } ( \Pi ^ { ( \varepsilon ) } , F ^ { ( \varepsilon ) } )$) converges to a finite limiting model$( { \hat { \Pi } } , { \hat { F } } )$. In such a case, the set of possible limits is parametrised by elements of$\Re _ { 0 }$, which in our setting is always just a finite-dimensional nilpotent Lie group. In the two cases mentioned above, one can furthermore reinterpret solutions corresponding to the “renormalised” model$M _ { \varepsilon } ( \Pi ^ { ( \varepsilon ) } , F ^ { ( \varepsilon ) } )$as solutions corresponding to the “bare” mode$( \Pi ^ { ( \varepsilon ) } , F ^ { ( \varepsilon ) } )$, but for a modified equation.

In this sense, R (or a subgroup thereof) has an interpretation as a renormalisation group acting on some space of formal equations, which is a very common viewpoint in the physics literature. (See for example [32] for a short introduction.) This thus allows to usually reinterpret the objects constructed by our theory as limits of solutions to equations that are modified by the addition of finitely many diverging counterterms. In the case of (PAM) with$d = 2$, the corresponding renormalisation procedure is essentially a type of Wick ordering and therefore yields the appearance of counterterms that are very similar in nature to those arising in the Itô–Stratonovich conversion formula for regular SDEs. (But with the crucial difference that they diverge logarithmically instead of being constant!) In the case of$( \Phi ^ { 4 } )$with$d = 3$, the situation is much more delicate because of the appearance of a logarithmic subdivergence “below” the leading order divergence that cannot be dealt with by a Wick-type renormalisation. For the invariant (Gibbs) measure corresponding to$( \Phi ^ { 4 } )$, this fact is well-known and had previously been observed in the context of constructive Euclidean QFT in [39,40,49].

Remark 1.9 Symmetries typically play an important role in the analysis of the renormalisation group R. Indeed, if the equation under consideration exhibits some symmetry, at least at a formal level, then it is natural to approximate it by regularised versions with the same symmetry. This then often places some natural restrictions on$\Re _ { 0 } \subset \Re$, ensuring that the renormalised version of the equation is still symmetric. For example, in the case of the KPZ equation, it was already remarked in [59] that regularisation via a non-symmetric mollifier can cause the appearance in the limiting solution of an additional transport term, thus breaking the invariance under left/right reflection. In Sect. 1.5.1 below, we will consider a class of equations which, via the chain rule, is formally invariant under composition by diffeomorphisms. This “symmetry” again imposes a restriction on$\Re _ { 0 }$ensuring that the renormalised equations again satisfy the chain rule.

Remark 1.10 If an equation needs to be renormalised in order to have a finite limit, it typically yields a whole family of limits parametrised by R (or rather $\Re _ { 0 }$in the presence of symmetries). Indeed, if$\bar { M _ { \varepsilon } } ( \Pi ^ { ( \varepsilon ) } , F ^ { ( \varepsilon ) } )$converges to a finite limit and M is any fixed element of$\Re _ { 0 }$, then$M M _ { \varepsilon } ( \Pi ^ { ( \varepsilon ) } , F ^ { ( \varepsilon ) } )$) obviously also converges to a finite limit. At first sight, this might look like a serious shortcoming of the theory: our equations still aren’t well-posed after all! It turns out that this state of affairs is actually very natural. Even the very wellunderstood situation of one-dimensional SDEs of the type

$$
d x = f (x) d t + \sigma (x) d W (t),\tag{1.4}
$$

exhibits this phenomena: solutions are different whether we interpret the stochastic integral as an Itô integral, a Stratonovich integral, etc. In this particular case, one would have$\Re \approx \mathbf { R }$endowed with addition as its group structure and the action of R onto the space of equations is given by$M _ { c } ( f , \sigma ) =$ $( f , \sigma + c \sigma \sigma ^ { \prime } )$, where$M _ { c } \in \Re$is the group element corresponding to the real constant c. Switching between the Itô and Stratonovich formulations is indeed a transformation of this type with$c \in \{ \pm \frac { 1 } { 2 } \}$

If the equation is driven by more than one Brownian motion, our renormalisation group increases in size: one now has a choice of stochastic integral for each of the integrals appearing in the equation. On symmetry grounds however, we would of course work with the subgroup$\Re _ { 0 } \subset \Re$which corresponds to the same choice for each. If we additionally exploit the fact that the class of equations (1.4) is formally invariant under the action of the group of diffeomorphisms of R (via the chain rule), then we could reduce$\Re _ { 0 }$further by postulating that the renormalised solutions should also transform under the classical chain rule. This would then reduce$\Re _ { 0 }$to the trivial group, thus leading to a “canonical” choice (the Stratonovich integral). In this particular case, we could of course also have imposed instead that the integral W dW has -no component in the 0th Wiener chaos, thus leading to Wick renormalisation with the Itô integral as a second “canonical” choice.

## 1.5 Main results: applications

We now show what kind of convergence results can be obtained by concretely applying the theory developed in this article to two examples of stochastic PDEs that cannot be interpreted by any classical means. The precise type of convergence will be detailed in the main body of the article, but it is essentially a convergence in probability on spaces of continuous trajectories with values in$\mathcal { C ^ { \alpha } }$for a suitable (possibly negative) value of α. A slight technical difficulty arises due to the fact that the limit processes do not necessarily have global solutions, but could exhibit blow-ups in finite time. In such a case, we know that the blow-up time is almost surely strictly positive and we have convergence “up to the blow-up time”.

## 1.5.1 Generalisation ofthe parabolic Anderson model

First, we consider the following generalisation of (PAM):

$$
\partial_ {t} u = \Delta u + f _ {i j} (u) \partial_ {i} u \partial_ {j} u + g (u) \xi , \quad u (0) = u _ {0},\tag{PAMg}
$$

where$f$and$g$are smooth function and summation of the indices i and$j$is implicit. Here,$\xi$denotes spatial white noise. This notation is of course only formal since neither the product$g ( u ) \xi$, nor the product$\partial _ { i } u \partial _ { j } u$make any sense classically. Here, we view u as a function of time$t \geq 0$and of$x \in \mathbf { T } ^ { 2 }$, the two-dimensional torus.

It is then natural to replace$\xi$by a smooth approximation$\xi _ { \varepsilon }$which is given by the convolution of$\xi$with a rescaled mollifier$\varrho$. Denote by$u _ { \varepsilon }$the solution to the equation

$$
\partial_ {t} u _ {\varepsilon} = \Delta u _ {\varepsilon} + f _ {i j} (u _ {\varepsilon}) \left(\partial_ {i} u _ {\varepsilon} \partial_ {j} u _ {\varepsilon} - \delta_ {i j} C _ {\varepsilon} g ^ {2} (u _ {\varepsilon})\right) + g (u _ {\varepsilon}) \left(\xi_ {\varepsilon} - 2 C _ {\varepsilon} g ^ {\prime} (u _ {\varepsilon})\right),\tag{1.5}
$$

again with initial condition$u _ { 0 }$. Then, we have the following result:

Theorem 1.11 Let$\alpha \in ( \frac { 1 } { 2 } , 1 )$. There exists a choice ofconstants$C _ { \varepsilon }$such that, for every initial condition$u _ { 0 } \in \mathcal { C } ^ { \alpha } ( \mathbf { T } ^ { 2 } )$, the sequence of solutions$u _ { \varepsilon }$to (1.5) converges to a limit u. Furthermore, there is an explicit constant$K _ { \varrho }$depending on  such that ifone sets$\begin{array} { r } { C _ { \varepsilon } = - \frac { 1 } { \pi } \log \varepsilon + K _ { \varrho . } } \end{array}$, then the limit obtained in this way is independent ofthe choice ofmollifier .

Proof This is a combination of Corollary 9.3 (well-posedness of the abstract formulation of the equation), Theorem 10.19 (convergence of the renormalised models to a limiting model) and Proposition 9.4 (identification of the renormalised solutions with (1.5)). The explicit value of the constant$C _ { \varepsilon }$is given in (10.32).□

Remark 1.12 In the case$f = 0$, this result has recently been obtained by different (though related in spirit) techniques in [46].

Remark 1.13 Since solutions might blow up in finite time, the notion of convergence considered here is to fix some large cut-off$L > 0$and terminal time T and to stop the solutions$u _ { \varepsilon }$as soon as$\| u _ { \varepsilon } ( t ) \| _ { \alpha } \geq L$, and similarly for the limiting process u. The convergence is then convergence in probability in $\mathcal { C } _ { \mathfrak { s } } ^ { \alpha } ( [ 0 , T ] \times \mathbf { T } ^ { 2 } )$for the stopped process. Here elements in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$are α-Hölder continuous in space and${ \frac { \alpha } { 2 } } { \mathrm { - H } } { \ddot { \mathrm { o l d e r } } }$continuous in time, see Definition 2.14 below.

Remark 1.14 It is lengthy but straightforward to verify that the additional diverging terms in the renormalised equation (1.5) are precisely such that if $\psi : \textbf { R }  \textbf { R }$is a smooth diffeomorphism, then$v _ { \varepsilon } \stackrel { \mathrm { d e f } } { = } \psi ( u _ { \varepsilon } )$solves again an equation of the type (1.5). Furthermore, this equation is precisely the renormalised version of the equation that one obtains by just formally applying the chain rule to (PAMg)! This gives a rigorous justification of the chain rule for $\mathbf { ( P A M g ) }$. In the case (KPZ), one expects a similar phenomenon, which would then allow to interpret the Cole–Hopf transform rigorously as a particular case of a general change of variables formula.

## 1.5.2 The dynamical$\Phi _ { 3 } ^ { 4 }$model

A similar convergence result can be obtained for$( \Phi ^ { 4 } )$. This time, the renormalised equation takes the form

$$
\partial_ {t} u _ {\varepsilon} = \Delta u _ {\varepsilon} + C _ {\varepsilon} u _ {\varepsilon} - u _ {\varepsilon} ^ {3} + \xi_ {\varepsilon},\tag{1.6}
$$

where$u _ { \varepsilon }$is a function of time$t \geq 0$and space$\boldsymbol { x } \in \mathbf { T } ^ { 3 }$, the three-dimensional torus. It turns out that the simplest class of approximating noise is to consider a space-time mollifier$\varrho ( { x } , t )$and to set$\xi _ { \varepsilon } \stackrel { \mathrm { d e f } } { = } \xi * \varrho _ { \varepsilon }$, where$\varrho _ { \varepsilon }$is the rescaled mollifier given by$\varrho _ { \varepsilon } ( x , t ) = \varepsilon ^ { - 5 } \varrho ( x / \varepsilon , t / \varepsilon ^ { 2 } )$

With this notation, we then have the following convergence result, which is the content of Sect. 10.5 below.

Theorem 1.15 Let$\alpha \in ( - \frac { 2 } { 3 } , - \frac { 1 } { 2 } )$. There exists a choice ofconstants$C _ { \varepsilon }$such that, for every initial condition u$\in \mathcal { C } ^ { \alpha } ( \mathbf { T } ^ { 3 } )$, the sequence of solutions$u _ { \varepsilon }$ converges to a limit u. Furthermore,$i f C _ { \varepsilon }$are chosen suitably, then this limit is again independent ofthe choice ofmollifier$\varphi .$

Proof This time, the statement is a consequence of Proposition 9.8 (wellposedness of the abstract formulation), Theorem 10.22 (convergence of the renormalised models) and Proposition 9.10 (identification of renormalised solutions with (1.6)).□

Remark 1.16 It turns out that the limiting solution u is almost surely a continuous function in time with values in$\mathcal { C } ^ { \bar { \alpha } } ( \mathbf { T } ^ { 3 } )$. The notion of convergence is then as in Remark 1.13. Here, we wrote again$\mathcal { C ^ { \alpha } }$as a shorthand for the Besov space$B _ { \infty , \infty } ^ { \alpha }$

Remark 1.17 As already noted in [39] (but for a slightly different regularisation procedure, which is more natural for the static version of the model considered there), the correct choice of constants$C _ { \varepsilon }$is of the form

$$
C _ {\varepsilon} = \frac {C _ {1}}{\varepsilon} + C _ {2} \log \varepsilon + C _ {3},
$$

where$C _ { 1 }$and$C _ { 3 }$depend on the choice of$\varrho$in a way that is explicitly computable, and the constant$C _ { 2 }$is independent of the choice of$\varrho$. It is the presence of this additional logarithmic divergence that makes the analysis of$( \Phi ^ { 4 } )$highly non-trivial. In particular, it was recently remarked in [4] that this seems to rule out the use of Dirichlet form techniques for interpreting$( \Phi ^ { 4 } )$

Remark 1.18 Again, we do not claim that the solutions constructed here are global. Indeed, the convergence holds in the space${ \mathcal { C } } ( [ 0 , T ] , { \mathcal { C } } ^ { \alpha } )$, but only up to some possibly finite explosion time. It is very likely that one can show that the solutions are global for almost every choice of initial condition, where “almost every” refers to the measure built in [39]. This is because that measure is expected to be invariant for the limiting process constructed in Theorem 1.15.

## 1.5.3 General methodology

Our methodology for proving the kind ofconvergence results mentioned above is the following. First, given a locally subcritical SPDE of the type (1.2), we build a regularity structure$\mathcal { T } _ { F }$which takes into account the structure of the nonlinearity$F$(as well as the regularity index of the driving noise and the local scaling properties of the linear operator$\mathcal { L } )$, together with a class$\mathcal { M } _ { F }$of “admissible models” on$\mathcal { T } _ { F }$which are defined using the abstract properties of$\mathcal { T } _ { F }$and the Green’s function of${ \mathcal { L } } .$. The general construction of such a structure is performed in Sect. 8. We then also build a natural “lift map” $Z \colon { \mathcal { C } } ( \mathbf { R } ^ { d } ) \to { \mathcal { M } } _ { F }$(see Sect. 8.2), where d is the dimension of the underlying space-time, as well as an abstract solution map$S \colon { \mathcal { C } } ^ { \alpha } \times { \mathcal { M } } _ { F } \to { \mathcal { D } } ^ { \gamma }$, with the property that$\mathcal { R } S ( u _ { 0 } , Z ( \xi _ { \varepsilon } ) )$yields the classical (local) solution to (1.2) with initial condition$u _ { 0 }$and noise$\xi _ { \varepsilon }$. Here,$\mathcal { R }$is the “reconstruction operator” already mentioned earlier. A general result showing that$s$can be built for “most” subcritical semilinear evolution problems is provided in Sect. 7. This relies fundamentally on the multi-level Schauder estimate of Sect. 5, as well as the results of Sect. 6 dealing with singular modelled distributions, which is required in order to deal with the behaviour near time 0.

The main feature of this construction is that both the abstract solution map $s$and the reconstruction operator$\mathcal { R }$are continuous. In most cases of interest they are even locally Lipschitz continuous in a suitable sense. Note that we made a rather serious abuse of notation here, since the very definition of the space$\mathcal { D } ^ { \gamma }$does actually depend on the particular model$Z ( \xi _ { \varepsilon } ) !$This will not bother us unduly since one could very easily remedy this by having the target space be$\begin{array} { r } { ^ { \ast } \mathcal { M } _ { F } \ltimes D ^ { \gamma \ast } } \end{array}$, with the understanding that each “fiber”$\mathcal { D } ^ { \gamma }$is modelled on the corresponding model in$\mathcal { M } _ { F }$. The map$s$would then simply act as the identity on$\mathcal { M } _ { F }$

Finally, we show that it is possible to find a sequence of elements$M _ { \varepsilon } \in \Re$ such that the sequence of renormalised models$M _ { \varepsilon } Z ( \xi _ { \varepsilon } )$converge to some limiting model$\hat { Z }$and we identify$\mathcal { R } S ( u _ { 0 } , M _ { \varepsilon } Z ( \xi _ { \varepsilon } ) )$) with the classical solution to a modified equation. The proofofthis fact is the only part ofthe whole theory which is not “automated”, but has to be performed by hand for each class of problems. However, if two problems give rise to the same structure$\mathcal { M } _ { F }$and are based on the same linear operator${ \mathcal { L } } .$, then they can be treated with the same procedure, since it is only the details of the solution map$\boldsymbol { \mathcal { S } }$that change from one problem to the other. We treat two classes of problems in detail in Sects. 9 and 10. Section 10 also contains a quite general toolbox that is very useful for treating the renormalisation of many equations with Gaussian driving noise.

## 1.6 Alternative theories

Before we proceed to the meat of this article, let us give a quick review of some of the main existing theories allowing to make sense of products of distributions. For each of these theories, we will highlight the differences with the theory of regularity structures.

## 1.6.1 Bony’s paraproduct

Denoting by$\Delta _ { j } f$the jth Paley–Littlewood block of a distribution$f$, one can define the bilinear operators

$$
\begin{array}{c} \pi_ {<  } (f, g) = \sum_ {i <   j - 1} \Delta_ {i} f \Delta_ {j} g, \quad \pi_ {>} (f, g) = \pi_ {<  } (g, f), \\ \pi_ {o} (f, g) = \sum_ {| i - j | \leq 1} \Delta_ {i} f \Delta_ {j} g, \end{array}
$$

so that, at least formally, one has$f g = \pi _ { < } ( f , g ) + \pi _ { > } ( f , g ) + \pi _ { o } ( f , g )$. (See [14] for the original article and some applications to the analysis of solutions to fully nonlinear PDEs, as well as the monograph and review article [6,13]. The notation of this section is borrowed from the recent work [46].) It turns out that$\pi _ { < }$and$\pi _ { > }$make sense for any two distributions$f$and g. Furthermore, if $f \in { \mathcal { C } } ^ { \alpha }$and$g \in \mathcal { C } ^ { \beta }$with$\alpha + \beta > 0$, then

$$
\pi_ {<  } (f, g) \in \mathcal {C} ^ {\beta}, \qquad \pi_ {>} (f, g) \in \mathcal {C} ^ {\alpha}, \qquad \pi_ {o} (f, g) \in \mathcal {C} ^ {\alpha + \beta},\tag{1.7}
$$

so that one has a gain of regularity there, but one does again encounter a “barrier” at$\alpha + \beta = 0$

The idea exploited in [46] is to consider a “model distribution” η and to consider “controlled distributions” of the type

$$
f = \pi_ {<  } (f ^ {\eta}, \eta) + f ^ {\sharp},
$$

where both$f ^ { \eta }$and$f ^ { \sharp }$are more regular than η. The construction is such that, at small scales, irregularities of$f$“look like” irregularities of η. The hope is then that if f is controlled by η, g is controlled by$\zeta .$, and one knows of a renormalisation procedure allowing to make sense of the product$\eta \zeta$(by using tools from stochastic analysis for example), then one can also give a consistent meaning to the product$f g$. This is the philosophy that was implemented in [46, Theorems 9 and 31].

This approach is very close to the one taken in the present work, and indeed it is possible to recover the results of [46] in the context of regularity structures, modulo slight modifications in the precise rigorous formulation of the convergence results. There are also some formal similarities: compare for example (1.7) with the bounds on each of the three terms appearing in (4.4). The main philosophical difference is that the approach presented here is very local in nature, as opposed to the more global approach used in Bony’s paraproduct. It is also more general, allowing for an arbitrary number of controls which do themselves have small-scale structures that are linked to each other. As a consequence, the current work also puts a strong emphasis on the highly non-trivial algebraic structures underlying our construction. In particular, we allow for rather sophisticated renormalisation procedures going beyond the usual Wick ordering, which is something that is required in several of the examples presented above.

## 1.6.2 Colombeau’s generalisedfunctions

In the early eighties, Colombeau introduced an algebra$\mathcal { G } ( \mathbf { R } ^ { d } )$of generalised functions on$\mathbf { R } ^ { d }$(or an open subset thereof) with the property that$S ^ { \prime } ( \mathbf { R } ^ { d } ) \subset$ $\mathcal { G } ( \mathbf { R } ^ { d } )$where$S ^ { \prime }$denotes the usual Schwartz distributions [26,27]. Without entering into too much detail,$\mathcal { G } ( \mathbf { R } ^ { d } )$is essentially defined as the set of smooth functions from$S ( \mathbf { R } ^ { d } )$, the set of Schwartz test functions, into R, quotiented by a certain natural equivalence relation.

Some (but not all) generalised functions have an “associated distribution”. In other words, the theory comes with a kind of “projection operator” $P \colon \mathcal { G } ( \mathbf { R } ^ { d } )  \mathcal { S } ^ { \prime } ( \mathbf { R } ^ { d } )$which is a left inverse for the injection ι$S ^ { \prime } ( \mathbf { R } ^ { d } ) \hookrightarrow$ $\mathcal { G } ( \mathbf { R } ^ { d } )$. However, it is important to note that the domain of definition of P is not all of$\mathcal { G } ( \mathbf { R } ^ { d } )$. Furthermore, the product in$\mathcal { G } ( \mathbf { R } ^ { d } )$behaves as one would expect on the images of objects that one would classically know how to multi-ply. For example, if$f$and$g$are continuous functions, then$P ( ( \iota f ) ( \iota g ) ) = f g$ The same holds true if$f$is a smooth function and$g$is a distribution.

There are some similarities between the theory of regularity structures and that of Colombeau generalised functions. For example, just like elements in $\mathcal { G } .$, elements in the spaces$\mathcal { D } ^ { \alpha }$(see Definition 3.1 below) contain more information than what is strictly required in order to reconstruct the correspond ing distribution. The theory of regularity structures involves a reconstruction operator$\mathcal { R } _ { { } }$, which plays a very similar role to the operator P from the theory of Colombeau’s generalised functions by allowing to discard that additional information. Also, both theories allow to provide a rigorous mathematical interpretation of some of the calculations performed in the context of quantum field theory.

One major difference between the two theories is that the theory ofregularity structures has more flexibility built in. Indeed, it allows some freedom in the definition of the product between elements of the “model” used for performing the local Taylor expansions. This allows to account for the fact that taking limits along different smooth approximations might in general yield different answers. (A classical example is the fact that sin$( x / \varepsilon ) \to 0$in any reasonable topology where it does converge, while$\sin ^ { 2 } ( x / \varepsilon ) \to 1 / 2$. More sophisticated effects of this kind can easily be encoded in a regularity structure, but are invisible to the theory of Colombeau’s generalised functions.) This could be viewed as a disadvantage of the theory of regularity structures: it requires substantially more effort on the part of the “user” in order to specify the theory completely in a given example. Also, there isn’tjust “one” regularity structure: the precise algebraic structure that is suitable for analysing a given problem does depend a lot on the problem in question. However, we will see in Sect. 8 that there is a general procedure allowing to build a large class of regularity structures arising in the analysis of semilinear SPDEs in a unified way.

## 1.6.3 White noise analysis

One theory that in principle allows to give some meaning to$( \Phi ^ { 4 } )$, (PAM), and (SNS) (but to the best of the author’s knowledge not to (PAMg) or (KPZ) with non-constant coefficients) is the theory of “white noise analysis” (WNA), exposed for example in [66] (see also [60,67] for some of the earlier works). For example, the case of the stochastic Navier–Stokes equations has been considered in [85], while the case of a stochastic version of the nonlinear heat equation was considered in [7]. Unfortunately, WNA has a number of severe drawbacks that are not shared by the theory of regularity structures:

Solutions in the WNA sense typically do not consist of random variables but of “Hida distributions”. As a consequence, only some suitable moments are obtained by this theory, but no actual probability distributions and / or random variables.

Solutions in the WNA sense are typically not obtained as limits of classical solutions to some regularised version of the problem. As a consequence, their physical interpretation is unclear. As a matter of fact, it was shown in [20] that the WNA solution to the KPZ equation exhibits a physically incorrect large-time behaviour, while the Cole–Hopf solution (which can also be obtained via a suitable regularity structure, see [59]) is the physically relevant solution [8].

There are exceptions to these two rules (usually when the only ill-posed product is of the form F(u) ξ with ξ some white noise, and the problem is parabolic), and in such cases the solutions obtained by the theory of regularity structures typically “contain” the solutions obtained by WNA. On the other hand, white noise analysis (or, in general, the Wiener chaos decomposition of random variables) is a very useful tool when building explicit models associated to a Gaussian noise. This will be exploited in Sect. 10 below.

## 1.6.4 Rough paths

The theory of rough paths was originally developed in [82] in order to interpret solutions to controlled differential equations of the type

$$
d Y (t) = F (Y) d X (t),
$$

where$X \colon \mathbf { R } ^ { + }  \mathbf { R } ^ { m }$is an irregular function and$F \colon \mathbf { R } ^ { d }  \mathbf { R } ^ { d m }$is a sufficiently regular collection of vector fields on$\mathbf { R } ^ { d }$. This can be viewed as an instance of the general problem (1.1) if we set${ \mathcal { L } } = \partial _ { t }$and$\begin{array} { r } { \xi = \frac { d X } { d t } } \end{array}$, which is now a rather irregular distribution. It turns out that, in the case ofHölder-regular rough paths, the theory of rough paths can be recast into our framework. It can then be interpreted as one particular class of regularity structures (one for each pair$( \alpha , m )$, where$m$is the dimension of the rough path and$\alpha$its index of Hölder regularity), with the corresponding space of rough paths being identified with the associated space of models. Indeed, the theory of rough paths, and particularly the theory of controlled rough paths as developed in [54,55], was one major source of inspiration of the present work. See Sect. 4.4 below for more details on the link between the two theories.

## 1.7 Notations

Given a distribution$\xi$and a test function$\varphi _ { \cdot }$, we will use indiscriminately the notations$\langle \xi , \varphi \rangle$and$\xi ( \varphi )$for the evaluation of$\xi$against$\varphi$. We will also sometimes use the abuse of notation$\textstyle \int \varphi ( x ) \xi ( x )$dx or$\textstyle \int \varphi ( x ) \xi ( d x )$

\- -Throughout this article, we will always work with multiindices on$\mathbf { R } ^ { d }$. A multiindex k is given by a vector$( k _ { 1 } , \ldots , k _ { d } )$with each$k _ { i } ~ \geq ~ 0$a positive integer. For$x \in \mathbf { R } ^ { d }$, we then write$x ^ { k }$as a shorthand for$x _ { 1 } ^ { k _ { 1 } } \cdot \cdot \cdot x _ { d } ^ { \bar { k } _ { d } }$. The same notation will still be used when$X ~ \in ~ T ^ { d }$for some algebra$T$. For a sufficiently regular function$g \colon  { \mathbf { R } } ^ { d } \to  { \mathbf { R } }$, we write$D ^ { k } g ( x )$) as a shorthand for $\partial _ { x _ { 1 } } ^ { k _ { 1 } } \ldots \partial _ { x _ { d } g ( x ) } ^ { k _ { d } }$. We also write k as a shorthand for$k _ { 1 } ! \cdots k _ { d } !$

Finally, we will write$a \wedge b$for the minimum of a and b and$a \lor b$for the maximum.

## 2 Abstract regularity structures

We start by introducing the abstract notion of a “regularity structure”, which was already mentioned in a loose way in the introduction, and which permeates the entirety of this work.

Definition 2.1 A regularity structure$\mathcal { T } = ( A , T , G )$) consists of the follow ing elements:

An index set$A \subset \mathbf { R }$such that$0 \in A$, A is bounded from below, and A is locally finite.

A model space T, which is a graded vector space$T = \oplus _ { \alpha \in A } T _ { \alpha }$, with each $T _ { \alpha }$a Banach space. Furthermore,$T _ { 0 } \approx \mathbf { R }$and its unit vector is denoted by 1.

A structure group G of linear operators acting on$T$such that, for every $\Gamma \in G$, every$\alpha \in A$, and every$a \in T _ { \alpha }$, one has

$$
\Gamma a - a \in \bigoplus_ {\beta <   \alpha} T _ {\beta}.\tag{2.1}
$$

Furthermore,$\Gamma { \bf 1 } = { \bf 1 }$for every$\Gamma \in G$

Remark 2.2 It will sometimes be an advantage to consider$G$as an abstract group, together with a representation$\Gamma$of$G$on$T$. This point of view will be very natural in the construction of Sect. 7 below. We will then sometimes use the notation$g \in G$for the abstract group element, and$\Gamma _ { g }$for the corresponding linear operator. For the moment however, we identify elements of$G$directly with linear operators on$T$in order to reduce the notational overhead.

Remark 2.3 Recall that the elements of$T = \oplus _ { \alpha \in A } T _ { \alpha }$are finite series of the type$\begin{array} { r } { a = \sum _ { \alpha \in A } a _ { \alpha } } \end{array}$with$a _ { \alpha } \in T _ { \alpha }$. All the operations that we will construct in the sequel will then make sense component by component.

Remark 2.4 A good analogy to have in mind is the space of all polynomials, which will be explored in detail in Sect. 2.2 below. In line with this analogy, we say that$T _ { \alpha }$consists of elements that are homogeneous of order$\alpha .$. In the particular case of polynomials in commuting indeterminates our theory boils down to the very familiar theory of Taylor expansions on$\mathbf { R } ^ { d }$, so that the reader might find it helpful to read the present section and Sect. 2.2 in parallel to help build an intuition. The reader familiar with the theory of rough paths [82] will also find it helpful to simultaneously read Sect. 4.4 which shows how the theory of rough paths (as well as the theory of “branched rough paths” [55]) fits within our framework.

The idea behind this definition is that$T$is a space whose elements describe the “jet” or “local expansion” of a function (or distribution!)$f$at any given point. One should then think of$T _ { \alpha }$as encoding the information required to describe$f$locally “at order$\alpha ^ { \prime \prime }$in the sense that, at scale$\varepsilon _ { i }$, elements of$T _ { \alpha }$ describe fluctuations of size$\varepsilon ^ { \alpha }$. This interpretation will be made much clearer below, but at an intuitive level it already shows that a regularity structure with $A \subset \mathbf { R } _ { + }$will describe functions, while a regularity structure with${ \cal A } \not \subset { \bf R } _ { + }$ will also be able to describe distributions.

The role of the structure group$G$will be to translate coefficients from a local expansion around a given point into coefficients for an expansion around a different point. Keeping in line with the analogy of Taylor expansions, the coefficients of a Taylor polynomial are just given by the partial derivatives of the underlying function$\varphi$at some point$x$. However, in order to compare the Taylor polynomial at$x$with the Taylor polynomial at$y _ { : }$, it is not such a good idea to compare the coefficients themselves. Instead, it is much more natural to first translate the first polynomial by the quantity$y - x$. In the case of polynomials on$\mathbf { R } ^ { d }$, the structure group$G$will therefore simply be given by$\mathbf { \bar { R } } ^ { d }$with addition as its group property, but we will see that non-abelian structure groups arise naturally in more general situations. (For example, the structure group is non-Abelian in the theory of rough paths.)

Before we proceed to a study of some basic properties of regularity structures, let us introduce a few notations. For an element$a \in T$, we write${ \mathcal { Q } } _ { \alpha } a$ for the component of a in$T _ { \alpha }$and$\| a \| _ { \alpha } = \| \mathcal { Q } _ { \alpha } a \|$for its norm. We also use the shorthand notations

$$
T _ {\alpha} ^ {+} = \bigoplus_ {\gamma \geq \alpha} T _ {\gamma}, \quad T _ {\alpha} ^ {-} = \bigoplus_ {\gamma <   \alpha} T _ {\gamma},\tag{2.2}
$$

with the conventions that$T _ { \alpha } ^ { + } = \{ 0 \}$ifα > max A and$T _ { \alpha } ^ { - } = \{ 0 \}$if α min A. We furthermore denote by$L _ { 0 } ^ { - } ( T )$) the space of all operators L on T such that $L a \in T _ { \alpha } ^ { - }$for$a \in T _ { \alpha }$and by$L ^ { - }$the set of operators L such that$L - 1 \in L _ { 0 } ^ { - }$ so that$G \subset L ^ { - }$

The condition that$\Gamma a - a \in T _ { \alpha } ^ { - }$for$a \in T _ { \alpha }$, together with the fact that the index set A is bounded from below, implies that, for every$\alpha \in A$there exists$n > 0$such that$( \Gamma - 1 ) ^ { n } T _ { \alpha } = 0$for every$\Gamma \in G$. In other words, G is necessarily nilpotent. In particular, one can define a function log$G  L _ { 0 } ^ { - }$ by

$$
\log \Gamma = \sum_ {k = 1} ^ {n} \frac {(- 1) ^ {k + 1}}{k} (\Gamma - 1) ^ {k}.\tag{2.3}
$$

Conversely, one can define an exponential map exp$L _ { 0 } ^ { - }  L ^ { - }$by its Taylor series, and one has the rather unsurprising identity$\Gamma = \exp ( \log \Gamma )$. As usual in the theory of Lie groups, we write${ \mathfrak { g } } = \log G$as a shorthand.

A useful definition will be the following:

Definition 2.5 Given a regularity structure as above and some$\alpha \leq 0$, a sector V of regularity α is a graded subspace$V = \oplus _ { \beta \in A } V _ { \beta }$with$V _ { \beta } \subset T _ { \beta }$having the following properties.

One has$V _ { \beta } = \{ 0 \}$for every$\beta < \alpha$

The space V is invariant under G, i.e.$\Gamma V \subset V$for every$\Gamma \in G$

For every$\beta \in A$, there exists a complement$\bar { V } _ { \beta } \subset T _ { \beta }$such that$T _ { \beta }$is given by the direct sum$T _ { \beta } = V _ { \beta } \oplus \bar { V } _ { \beta }$

A sector of regularity 0 is also calledfunction-like for reasons that will become clear in Sect. 3.4.

Remark 2.6 The regularity of a sector will always be less or equal to zero. In the case of the regularity structure generated by polynomials for example, any non-trivial sector has regularity 0 since it always has to contain the element 1. See Corollary 3.16 below for a justification of this terminology.

Remark 2.7 Given a sector V, we can define$A _ { V } \subset A$as the set of indices α such that$V _ { \alpha } \ \ne \ \{ 0 \}$. If$\alpha ~ > ~ 0$, our definitions then ensure that$\mathcal { T } _ { V } =$ $( V , A _ { V } , G )$is again a regularity structure with$\mathcal { T } _ { V } \subset \mathcal { T }$. (See below for the meaning of such an inclusion.) It is then natural to talk about a subsector $W \subset V$if W is a sector for$\mathcal { T } _ { V }$

Remark 2.8 Two natural non-empty sectors are given by$T _ { 0 } = \mathrm { s p a n } \{ { \bf 1 } \}$and by $T _ { \alpha }$with$\alpha = \operatorname* { m i n } A$. In both cases,$G$automatically acts on them in a trivial way. Furthermore, as an immediate consequence of the definitions, given a sector V of regularity$\alpha$and a real number$\gamma > \alpha$, the space$V \cap T _ { \gamma } ^ { - }$is again a sector of regularity$\alpha .$.

In the case ofpolynomials on$\mathbf { R } ^ { d }$, typical examples ofsectors would be given by the set of polynomials depending only on some subset of the variables or by the set of polynomials of some fixed degree.

## 2.1 Basic properties of regularity structures

The smallest possible regularity structure is given by$\mathcal { T } _ { 0 } = ( \{ 0 \} , { \bf R } , \{ 1 \} )$, where 1 is the trivial group consisting only of the identity operator, and with ${ \bf 1 } = { \bf 1 }$. This “trivial” regularity structure is the smallest possible structure that accommodates the local information required to describe an arbitrary continuous function, i.e. simply the value of the function at each point.

The set of all regularity structures comes with a natural partial order. Given two regularity structures$\mathcal { T } = ( A , T , G )$and$\bar { \mathcal { T } } = ( \bar { A } , \bar { T } , \bar { G } )$we say that$\mathcal { T }$ contains$\bar { \mathcal T }$and write$\bar { \mathcal { T } } \subset \mathcal { T }$if the following holds.

One has${ \bar { A } } \subset A$

There is an injection$\iota \colon \bar { T } \  \ T$such that, for every$\alpha \in { \bar { A } }$, one has $\iota ( \bar { T } _ { \alpha } ) \subset T _ { \alpha }$

The space$\iota ( \hat { T } )$is invariant under G and the map$j \colon G \to L ( { \bar { T } } , { \bar { T } } )$defined by the identity$j \Gamma = \iota ^ { - 1 } \Gamma \iota$is a surjective group homomorphism from$G$ to$\bar { G }$.

With this definition, one has$\mathcal { T } _ { 0 } \subset \mathcal { T }$for every regularity structure$\mathcal { T }$, with $\iota 1 = 1$and$j$given by the trivial homomorphism.

One can also define the product$\mathcal { \hat { T } } = \mathcal { T } \otimes \mathcal { \bar { T } }$of two regularity structures $\mathcal { T } = ( A , T , G )$and$\bar { \mathcal { T } } = ( \bar { A } , \bar { T } , \bar { G } )$by$\hat { \mathcal { T } } = ( \hat { A } , \hat { T } , \hat { G } )$with

$\hat { A } = A + \bar { A }$

$\hat { T } = \oplus _ { ( \alpha , \beta ) } T _ { \alpha } \otimes \bar { T } _ { \beta }$and$\begin{array} { r } { \hat { T } _ { \gamma } = \bigoplus _ { \alpha + \beta = \gamma } T _ { \alpha } \otimes \bar { T } _ { \beta } } \end{array}$, where both sums run <sub>over pairs</sub>$( \alpha , \beta ) \in A \times { \bar { A } }$

$\hat { G } = G \otimes \bar { G }$

Setting$\hat { \mathbf { 1 } } = \mathbf { 1 } \otimes \bar { \mathbf { 1 } }$(where 1 and$\bar { \bf 1 }$are the unit elements of$\mathcal { T }$and$\bar { \mathcal T }$respectively), it is easy to verify that this definition satisfies all the required axioms for a regularity structure. If the individual components of$T$and$/$or$\bar { T }$are infinite-dimensional, this construction does of course rely on choices of tensor products for$T _ { \alpha } \otimes { \bar { T } } _ { \beta }$

Remark 2.9 One has both$\mathcal { T } \subset \mathcal { T } \otimes \bar { \mathcal { T } }$and$\bar { \mathcal { T } } \subset \mathcal { T } \otimes \bar { \mathcal { T } }$with obvious inclusion maps. Furthermore, one has$\mathcal { T } \otimes \mathcal { T } _ { 0 } \approx \mathcal { T }$for the trivial regularity structure$\mathcal { T } _ { 0 }$

## 2.2 The polynomial regularity structure

One very important example to keep in mind for the abstract theory of regu larity structures presented in the main part of this article is that generated by polynomials in d commuting variables. In this case, we simply recover the usual theory of Taylor expansions / regular functions in$\mathbf { R } ^ { d }$. However, it is still of interest since it helps building our intuition and provides a nicely unified way of treating regular functions with different scalings.

In this case, the model space T consists of all abstract polynomials in d indeterminates. More precisely, we have d “dummy variables”$\{ X _ { i } \} _ { i = 1 } ^ { d }$and T consists of polynomials in X. Given a multiindex$k = ( k _ { 1 } , \ldots , k _ { d } )$=<sub>, we will</sub> use throughout this article the shorthand notation

$$
X ^ {k} \stackrel {\mathrm{def}} {=} X _ {1} ^ {k _ {1}} \dots X _ {d} ^ {k _ {d}}.
$$

Finally, we denote by$\mathbf { 1 } = X ^ { 0 }$the “empty” monomial.

In general, we will be interested in situations where different variables come with different degrees of homogeneity. A good example to keep in mind is that of parabolic equations, where the linear operator is given by$\partial _ { t } - \Delta$, with the Laplacian acting on the spatial coordinates. By homogeneity, it is then natural to make powers of t “count double”. In order to implement this classical idea, we assume from now on that we fix a scaling$\mathfrak { s } \in \mathbf { N } ^ { d }$of$\mathbf { R } ^ { d }$, which is simply a vector of strictly positive relatively prime integers. The Euclidean scaling is simply given by${ \mathfrak { s } } _ { c } = ( 1 , \ldots , 1 )$).

Given such a scaling, we define the “scaled degree” of a multiindex k by

$$
| k | _ {\mathfrak {s}} = \sum_ {i = 1} ^ {d} \mathfrak {s} _ {i} k _ {i}.\tag{2.4}
$$

With this notation we define, for every$n \in \mathbf { N }$, the subspace$T _ { n } \subset T$by

$$
T _ {n} = \operatorname{span} \{X ^ {k}: | k | _ {\mathfrak {s}} = n \}.
$$

For a monomial P of the type$P ( X ) = X ^ { k }$, we then refer to$| k | _ { \mathfrak { s } }$as the scaled degree of P. Setting$A = \mathbf { N }$, we have thus constructed the first two components of a regularity structure.

Our structure comes with a natural model, which is given by the concrete realisation of an abstract polynomial as a function on$\mathbf { R } ^ { d }$. More precisely, for every$x \in \mathbf { R } ^ { d }$, we have a natural linear map$T \to { \mathcal { C } } ^ { \infty } ( \mathbf { R } ^ { d } )$given by

$$
\left(\Pi_ {x} X ^ {k}\right) (y) = (y - x) ^ {k}.\tag{2.5}
$$

In other words, given any “abstract polynomial” P(X),$\Pi _ { x }$realises it as a concrete polynomial on$\mathbf { R } ^ { d }$based at the point x.

This suggests that there is a natural action of$\mathbf { R } ^ { d }$on T which simply shifts the base point x. This is precisely the action that is described by the group G which is the last ingredient missing to obtain a regularity structure. As an abstract group,$G$will simply be a copy of$\mathbf { R } ^ { d }$endowed with addition as its group operation. For any$h \in \mathbf { R } ^ { d } \approx G$, the action of$\Gamma _ { h }$on an abstract polynomial is then given by

$$
(\Gamma_ {h} P) (X) = P (X + h).
$$

It is obvious from our notation that one has the identities

$$
\Gamma_ {h} \circ \Gamma_ {\bar {h}} = \Gamma_ {h + \bar {h}}, \quad \Pi_ {x + h} \Gamma_ {h} = \Pi_ {x},
$$

which will play a fundamental role in the sequel.

The triple (N, T, G) constructed in this way thus defines a regularity structure, which we call$\mathcal { T } _ { d , \mathfrak { s } }$. (It depends on the scaling s only in the way that T is split into subspaces, so s does not explicitly appear in the definition of$\mathcal { T } _ { d , \mathfrak { s } \cdot } )$

In this construction, the space$T$comes with more structure than just that of a regularity structure. Indeed, it comes with a natural multiplication given by

$$
(P \star Q) (X) = P (X) Q (X).
$$

It is then straightforward to verify that this representation satisfies the properties that

For$P \in T _ { m }$and$Q \in T _ { n }$, one has$P \star Q \in T _ { m + n }$

The element 1 is neutral for .

For every$h \in \mathbf { R } ^ { d }$and$P , Q \in T$, one has$\Gamma _ { h } ( P \star Q ) = \Gamma _ { h } P \star \Gamma _ { h } Q .$

Furthermore, there exists a natural element$\langle \mathbf { 1 } , \cdot \rangle$in the dual of T which consists of formally evaluating the corresponding polynomial at the origin. More precisely, one sets$\left. \mathbf { 1 } , X ^ { k } \right. = \delta _ { k , 0 }$

As a space of polynomials, T arises naturally as the space in which the Taylor expansion of a function$\varphi \colon { \bf R } ^ { d }  { \bf R }$takes values. Given a smooth function$\varphi \colon \mathbf { R } ^ { d }  \mathbf { R }$and an integer$\ell \geq 0$, we can$\mathbf { \bar { \Psi } } ] \mathbf { \dot { i } } \mathbf { f t } ^ { \mathbf { \lessgtr } } \varphi$in a natural way to

T by computing its Taylor expansion of order less than  at each point. More precisely, we set

$$
(\mathcal {T} _ {\ell} \varphi) (x) = \sum_ {| k | _ {\mathfrak {s}} <   \ell} \frac {X ^ {k}}{k !} D ^ {k} \varphi (x),\tag{2.6}
$$

where, for a given multiindex$k = ( k _ { 1 } , \ldots , k _ { d } ) , D ^ { k } \varphi$stands as usual for the partial derivative$\partial _ { 1 } ^ { k _ { 1 } } \cdot \cdot \cdot \partial _ { d } ^ { k _ { d } } \varphi ( x )$. It then follows immediately from the general Leibniz rule that for$\mathcal { C } ^ { \ell }$functions,$\mathcal { T } _ { \ell }$is “almost” an algebra morphism, in the sense that in addition to being linear, one has

$$
\mathcal {T} _ {\ell} (\varphi \cdot \psi) (x) = \mathcal {T} _ {\ell} \varphi (x) \star \mathcal {T} _ {\ell} \psi (x) + R (x),\tag{2.7}
$$

where the remainder$R ( x )$is a sum of homogeneous terms of scaled degree greater or equal to .

We conclude this subsection by defining the classes$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$of functions that are $\mathcal { C } ^ { \alpha }$with respect to a given scaling s. Recall that, for$\alpha \in ( 0 , 1 ]$, the class$\mathcal { C } ^ { \alpha }$ of “usual” α-Hölder continuous functions is given by those functions$f$such that$| f ( x ) - f ( y ) | \lesssim | x - y | ^ { \alpha }$, uniformly over x and y in any compact set. For any$\alpha > 1$, we can then define$\mathcal { C ^ { \alpha } }$recursively as consisting of functions that are continuously differentiable and such that each directional derivative belongs to$\mathcal { C } ^ { \alpha - 1 }$

Remark 2.10$\bigtriangleup$In order to keep our notations consistent, we have slightly strayed from the usual conventions by declaring a function to be of class${ \mathcal C } ^ { 1 }$ even if it is only Lipschitz continuous. A similar abuse of notation will be repeated for all positive integers, and this will be the case throughout this article.

Remark 2.11 We could have defined the spaces$\mathcal { C } ^ { \alpha }$for$\alpha \in [ 0 , 1 )$(note the missing point 1!) similarly as above, but replacing the bound on$f ( x ) - f ( y )$ by

$$
\lim _ {| h | \to 0} | f (x + h) - f (x) | / | h | ^ {\alpha} = 0,\tag{2.8}
$$

imposing uniformity of the convergence for x in any compact set. If we extended this definition to$\alpha \geq 1$recursively as above, this would coincide with the usual spaces$\mathcal { C } ^ { k }$for integer$k$, but the resulting spaces would be slightly smaller than the Hölder spaces for non-integer values. (In fact, they would then coincide with the closure of smooth functions under the α-Hölder norm.) Since the bound (2.8) includes a supremum and a limit rather than just a supremum, we prefer to stick with the definition given above.

Keeping this characterisation in mind, one nice feature of the regularity structure just described is that it provides a very natural “direct” characterisation of$\mathcal { C } ^ { \alpha }$for any$\alpha > 0$without having to resort to an inductive construction. Indeed, in the case of the classical Euclidean scaling${ \mathfrak { s } } = ( 1 , \dotsc , 1 )$, we have the following result, where for$a \in T$, we denote by$\| a \| _ { m }$the norm of the component of a in$T _ { m }$

Lemma 2.12 Afunction$\varphi \colon \mathbf { R } ^ { d }  \mathbf { R }$is of class$\mathcal { C ^ { \alpha } }$with$\alpha > 0$ifand only if there exists afunction$\hat { \varphi } : \mathbf { R } ^ { d } \to T _ { \alpha } ^ { - }$such that$\langle \mathbf { 1 } , \hat { \varphi } ( x ) \rangle = \varphi ( x )$and such that

$$
\| \hat {\varphi} (x + h) - \Gamma_ {h} \hat {\varphi} (x) \| _ {m} \lesssim | h | ^ {\alpha - m},\tag{2.9}
$$

uniformly over m$< \alpha , | h | \leq 1$and x in any compact set.

Proof For$\alpha \in ( 0 , 1 ] , ( 2 . 9 )$is just a rewriting of the definition of$\mathcal { C ^ { \alpha } }$. For the general case, denote by$\mathcal { D } ^ { \alpha }$the space of T-valued functions such that (2.9) holds. Denote furthermore by$\mathcal { D } _ { i } \colon T  T$the linear map defined by $\mathcal { D } _ { i } { X } _ { j } = \delta _ { i j } \mathbf { 1 }$and extended to higher powers of X by the Leibniz rule. For $\hat { \varphi } \in \mathcal { D } ^ { \alpha }$with$\alpha > 1$, we then have that:

The bound (2.9) for$m = 0$implies that$\varphi = \langle \mathbf { 1 } , \hat { \varphi } \langle$is differentiable at x with ith directional derivative given by$\partial _ { i } \varphi ( x ) = \langle \mathbf { 1 } , \mathcal { D } _ { i } \hat { \varphi } ( x ) \langle .$

The case$m = 1$implies that the derivative$\partial _ { i } \varphi$is itself continuous.

Since the operators$\mathcal { D } _ { i }$commute with$\Gamma _ { h }$for every h, one has$\mathcal { D } _ { i } \varphi \in \mathcal { D } ^ { \alpha - 1 }$ for every$i \in \{ 1 , \ldots , d \}$

The claim then follows at once from the fact that this is precisely the recursive characterisation of the spaces$\mathcal { C ^ { \alpha } }$□

This now provides a very natural generalisation ofHölder spaces ofarbitrary order to non-Euclidean scalings. Indeed, to a scaling s of$\mathbf { R } ^ { d }$, we can naturally associate the metric$d _ { \mathfrak { s } }$on$\mathbf { R } ^ { d }$given by

$$
d _ {\mathfrak {s}} (x, y) \stackrel {{\mathrm{def}}} {{=}} \sum_ {i = 1} ^ {d} | x _ {i} - y _ {i} | ^ {1 / \mathfrak {s} _ {i}}.\tag{2.10}
$$

We will also use in the sequel the notation$| \mathfrak { s } | = \mathfrak { s } _ { 1 } + \cdot \cdot \cdot + \mathfrak { s } _ { d }$, which plays the role of a dimension. Indeed, with respect to the metric$d _ { \mathfrak { s } }$, the unit ball in$\mathbf { R } ^ { d }$is easily seen to have Hausdorffdimension$| \mathfrak { s } |$rather than d. Even though the right hand side of (2.10) does not define a norm (it is not 1-homogeneous, at least not in the usual sense), we will usually use the notation$d _ { \mathfrak { s } } ( x , y ) = \| x - y \| _ { \mathfrak { s } }$

Remark 2.13 It may occasionally be more convenient to use a metric with the same scaling properties as$d _ { \mathfrak { s } }$which is smooth away from the origin. In this case, one can for example take$p = 2 \operatorname { l c m } ( \mathfrak { s } _ { 1 } , \dots , \mathfrak { s } _ { d } )$and set

$$
\tilde {d} _ {\mathfrak {s}} (x, y) \stackrel {{\text { def }}} {{=}} \left(\sum_ {i = 1} ^ {d} | x _ {i} - y _ {i} | ^ {p / \mathfrak {s} _ {i}}\right) ^ {1 / p}.
$$

It is easy to see that$\tilde { d } _ { \mathfrak { s } }$and$d _ { \mathfrak { s } }$are equivalent in the sense that they are bounded by fixed multiples of each other. In the Euclidean setting,$d _ { \mathfrak { s } }$would be the$\ell ^ { 1 }$ distance, while$\tilde { d } _ { \mathfrak { s } }$would be the$\ell ^ { 2 }$distance.

With this notation at hand, and in view of Lemma 2.12, the following definition is very natural:

Definition 2.14 Given a scaling s on$\mathbf { R } ^ { d }$and$\alpha > 0$, we say that a function $\varphi \colon { \bf R } ^ { d } \  \ { \bf R }$is of class$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$if there exists a function$\hat { \varphi } : \bar { \mathbf { R } } ^ { d } \to T _ { \alpha } ^ { - }$with $\langle \mathbf { 1 } , \hat { \varphi } ( x ) \rangle = \varphi ( x )$for every x and such that, for every compact set$\mathcal { \hat { R } } \subset \mathbb { R } ^ { d }$ one has

$$
\| \hat {\varphi} (x + h) - \Gamma_ {h} \hat {\varphi} (x) \| _ {m} \lesssim \| h \| _ {\mathfrak {s}} ^ {\alpha - m},\tag{2.11}
$$

uniformly over$m < \alpha , \| h \| _ { \mathfrak { s } } \le 1$and$x \in { \mathfrak { K } }$

Remark 2.15 One can verify that the map$x \mapsto \| x \| _ { \mathfrak { s } } ^ { \alpha }$is in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$for$\alpha \in ( 0 , 1 ]$ Another well-known example [56,98] is that the solutions to the additive stochastic heat equation on the real line belong to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha } ( \mathbf { R } ^ { 2 } )$for every$\alpha \ < \ \frac { 1 } { 2 }$, provided that the scaling s is the parabolic scaling${ \mathfrak { s } } = ( 2 , 1 )$). (Here, the first component is the time direction.)

Remark 2.16 The choice of$\hat { \varphi }$in Definition 2.14 is essentially unique in the sense that any two choices$\hat { \varphi } _ { 1 }$and$\hat { \varphi } _ { 2 }$satisfy$\mathcal { Q } _ { \ell } \hat { \varphi } _ { 1 } ( x ) = \mathcal { Q } _ { \ell } \hat { \varphi } _ { 2 } ( x )$for every x and every$\ell < \alpha$. (Recall that$\mathcal { Q } _ { \ell }$is the projection onto$T _ { \ell } . )$This is because, similarly to the proof of Lemma 2.12, one can show that the components in$T _ { \ell }$ have to coincide with the corresponding directional derivatives of$\varphi$at x, and that, if (2.11) is satisfied locally uniformly in x, these directional derivatives exist and are continuous.

## 2.3 Models for regularity structures

In this section, we introduce the key notion of a “model” for a regularity structure, which was already alluded to several times in the introduction. Essentially, a model associates to each “abstract” element in T a “concrete” function or distribution on$\mathbf { R } ^ { d }$. In the above example, such a model was given by an interplay of the maps$\Pi _ { x }$that would associate to$a \in T$a polynomial on$\bar { \mathbf { R } } ^ { d }$centred around$x ,$, and the maps$\Gamma _ { h }$that allow to translate the polynomial in question to any other point in$\mathbf { R } ^ { d }$.

This is the structure that we are now going to generalise and this is where our theory departs significantly from the theory of jets, as our model will typically contain elements that are extremely irregular. If we take again the case of the polynomial regularity structures as our guiding principle, we note that the index$\alpha \in A$describes the speed at which functions of the form$\Pi _ { x } a$ with$a \in T _ { \alpha }$vanish near x. The action of  is then necessary in order to ensure that this behaviour is the same at every point. In general, elements in the image of$\Pi _ { x }$are distributions and not functions and the index$\alpha$can be negative, so how do we describe the behaviour near a point?

One natural answer to this question is to test the distribution in question against approximations to a delta function and to quantify this behaviour. Given a scaling s, we thus define scaling maps

$$
\mathcal {S} _ {\mathfrak {s}} ^ {\delta} \colon \mathbf {R} ^ {d} \to \mathbf {R} ^ {d}, \quad \mathcal {S} _ {\mathfrak {s}} ^ {\delta} (x _ {1}, \ldots , x _ {d}) = (\delta^ {- \mathfrak {s} _ {1}} x _ {1}, \ldots , \delta^ {- \mathfrak {s} _ {d}} x _ {d}).\tag{2.12}
$$

These scaling maps yield in a natural way a family of isometries on$L ^ { 1 } ( \mathbf R ^ { d } )$ by

$$
\left(\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \varphi\right) (y) \stackrel {{\text { def }}} {{=}} \delta^ {- | \mathfrak {s} |} \varphi \left(\mathcal {S} _ {\mathfrak {s}} ^ {\delta} (y - x)\right).\tag{2.13}
$$

They are also the natural scalings under which$\| \cdot \| _ { \mathfrak { s } }$behaves like a norm in the sense that$\lVert S _ { \mathfrak { s } } ^ { \delta } x \rVert _ { \mathfrak { s } } = \delta ^ { - 1 } \rVert x \rVert _ { \mathfrak { s } }$. Note now that if$P$is a monomial of scaled degree$\ell \geq 0$over$\mathbf { R } ^ { d }$(where the scaled degree simply means that the monomial$x _ { i }$has degree$s _ { i }$rather than 1) and$\varphi \colon { \bf R } ^ { d }  { \bf R }$is a compactly supported function, then we have the identity

$$
\begin{array}{c} \int P (y - x) \left(\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \varphi\right) (y) d y = \int P (\delta^ {\mathfrak {s} _ {1}} z _ {1}, \ldots , \delta^ {\mathfrak {s} _ {d}} z _ {d}) \varphi (z) d z \\ = \delta^ {\ell} \int P (z) \varphi (z) d z. \end{array}\tag{2.14}
$$

Following the philosophy of taking the case of polynomials/Taylor expansions as our source of inspiration, this simple calculation motivates the following definition.

Definition 2.17 A model for a given regularity structure$\mathcal { T } = ( A , T , G )$on $\mathbf { R } ^ { d }$with scaling s consists of the following elements:

A map$\mathbf { R } ^ { d } \times \mathbf { R } ^ { d }  G$such that$\Gamma _ { x x } = 1$, the identity operator, and such that$\Gamma _ { x y } \Gamma _ { y z } = \Gamma _ { x z }$for every$x , y , z$in$\mathbf { R } ^ { d }$

A collection of continuous linear maps$\Pi _ { x } \colon T \to S ^ { \prime } ( \mathbf { R } ^ { d } )$such that$\Pi _ { y } =$ $\Pi _ { x } \circ \Gamma _ { x y }$for every x,$\boldsymbol { y } \in \mathbf { R } ^ { d }$

Furthermore, for every$\gamma > 0$and every compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$, there exists a constant$C _ { \gamma , \mathfrak { K } }$such that the bounds

$$
\left| \left(\Pi_ {x} a\right) \left(\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \varphi\right) \right| \leq C _ {\gamma , \mathfrak {K}} \| a \| \delta^ {\ell}, \quad \| \Gamma_ {x y} a \| _ {m} \leq C _ {\gamma , \mathfrak {K}} \| a \| \| x - y \| _ {\mathfrak {s}} ^ {\ell - m},\tag{2.15}
$$

hold uniformly over all$x , y \in { \mathcal { R } }$, all$\delta \in ( 0 , 1 ]$, all smooth test functions $\varphi \colon B _ { \mathfrak { s } } ( 0 , 1 ) \to \mathbf { R }$with$\| \varphi \| _ { \mathcal { C } ^ { r } } \leq 1$, all$\ell \in A$with$\ell < \gamma$, all$m < \ell .$, and all $a \in T _ { \ell }$. Here, r is the smallest integer such that$\ell > - r$for every$\ell \in A$. (Note that$\| \Gamma _ { x y } a \| _ { m } = \| \Gamma _ { x y } a - a \| _ { m }$since$a \in T _ { \ell }$and$m < \ell . )$

Remark 2.18 We will also sometimes call the pair$( \Pi , \Gamma )$a model for the regularity structure$\mathcal { T }$

The following figure illustrates a typical example of model for a simple regularity structure where$A = \{ 0 , { \frac { 1 } { 2 } } , { \dot { 1 } } , { \frac { 3 } { 2 } } \}$and each$T _ { \alpha }$is one-dimensional:

| α = 0 |  |
| --- | --- |
| / |  |
| / |  |

![](images/page_32_image_6.jpg)

![](images/page_32_image_7.jpg)

![](images/page_32_image_8.jpg)

Write$\tau _ { \alpha }$for the unit vector in$T _ { \alpha }$. Given a${ \frac { 1 } { 2 } } { \mathrm { - H } } { \ddot { \mathrm { o l d e r } } }$continuous function $f \colon \mathbf { R }  \mathbf { R } \quad$, the above picture has

$$
\left(\Pi_ {x} \tau_ {\frac {1}{2}}\right) (y) = f (y) - f (x), \quad \left(\Pi_ {x} \tau_ {\frac {3}{2}}\right) (y) = \int_ {x} ^ {y} (f (z) - f (x)) d z,
$$

while$\Pi _ { x } \tau _ { 0 }$and$\Pi _ { x } \tau _ { 1 }$are given by the canonical one-dimensional model of polynomials.

A typical action of$\Gamma _ { x y }$is illustrated below:

![](images/page_32_image_13.jpg)

Here, the left figure shows$\Pi _ { x } \tau _ { \frac { 3 } { 7 } }$, while the right figure shows$\Pi _ { y } \tau _ { \frac { 3 } { 7 } } =$ $\Pi _ { x } \Gamma _ { x y } \tau _ { \frac { 3 } { 7 } }$. In this particular example, this is obtained from$\Pi _ { x } \tau _ { \frac { 3 } { 7 } }$by adding a suitable affine function, i.e. a linear combination of$\Pi _ { x } \tau _ { 0 }$and$\bar { \Pi } _ { x } \tau _ { 1 }$

Remark 2.19 Given a sector$V \subset T$, it will on occasion be natural to consider models for$\mathcal { T } _ { V }$rather than all of$\mathcal { T }$. In such a situation, we will say that ( , ) is a model for$\mathcal { T }$on$V .$, or just a model for$V$

Remark 2.20 Given a map$( x , y ) \mapsto \Gamma _ { x y }$as above, the set of maps$x \mapsto \Pi _ { x }$ as above is actually a linear space. We can endow it with the natural system of seminorms$\Vert \Pi \Vert _ { \gamma ; \mathcal { R } }$given by the smallest constant$C _ { \gamma , \mathfrak { K } }$such that the first bound in (2.15) holds. Similarly, we denote by$\| \Gamma \| _ { \gamma ; \mathbb { A } }$the smallest constant $C _ { \gamma , \mathfrak { K } }$such that the second bound in (2.15) holds. Occasionally, it will be useful to have a notation for the combined bound, and we will then write

$$
\| Z \| _ {\gamma ; \mathfrak {K}} = \| \Pi \| _ {\gamma ; \mathfrak {K}} + \| \Gamma \| _ {\gamma ; \mathfrak {K}},\tag{2.16}
$$

where we set$Z = ( \Pi , \Gamma )$

Remark 2.21 The first bound in (2.15) could alternatively have been formulated as$| ( \Pi _ { x } a ) ( \varphi ) | \leq C \Vert a \Vert \delta ^ { \ell }$for all smooth test functions$\varphi$with support in a ball of radius δ around x (in the$d _ { \mathfrak { s } ^ { - } } \mathrm { d i s t a n c e } )$, which are bounded by $\delta ^ { - | \mathfrak { s } | }$and such that their derivatives satisfy$\begin{array} { r } { \operatorname* { s u p } _ { x } | D ^ { \ell } \varphi ( x ) | \le \delta ^ { - | \mathfrak { s } | - | \ell | _ { \mathfrak { s } } } } \end{array}$for all multiindices$\ell$of (usual) size less or equal to$r _ { \cdot }$.

One important notion is that of an extension of a model ( , ):

Definition 2.22 Let$\mathcal { T } \subset \hat { \mathcal { T } }$be two regularity structures and let$( \Pi , \Gamma )$be a model for$\mathcal { T }$. A model$( \hat { \Pi } , \hat { \Gamma } )$is said to extend ( , ) for$\hat { \mathcal T }$if one has

$$
\iota \Gamma_ {x y} a = \hat {\Gamma} _ {x y} \iota a, \quad \Pi_ {x} a = \hat {\Pi} _ {x} \iota a,
$$

for every$a \in T$and every$x , y$in$\mathbf { R } ^ { d }$. Here, ι is as in Sect. 2.1.

We henceforth denote by$\mathcal { M } _ { \mathcal { T } }$the set of all models of$\mathcal { T }$, which is a slight abuse of notation since one should also fix the dimension d and the scaling s, but these are usually very clear from the context. This space is endowed with a natural system of pseudo-metrics by setting, for any two models$Z = ( \Pi , \Gamma )$ and$\bar { z } = ( \bar { \Pi } , \bar { \Gamma } )$

$$
\| Z; \bar {z} \| _ {\gamma ; \mathfrak {K}} \stackrel {\mathrm{def}} {=} \| \Pi - \bar {\Pi} \| _ {\gamma ; \mathfrak {K}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma ; \mathfrak {K}}.\tag{2.17}
$$

While$\| \cdot ; \cdot \| _ { \gamma ; \mathscr { R } }$defined in this way looks very much like a seminorm, the space $\mathcal { M } _ { \mathcal { T } }$is not a linear space due to the two nonlinear constraints

$$
\Gamma_ {x y} \Gamma_ {y z} = \Gamma_ {x z}, \quad \text { and } \quad \Pi_ {y} = \Pi_ {x} \circ \Gamma_ {x y},\tag{2.18}
$$

and due to the fact that G is not necessarily a linear set of operators. While$\mathcal { M } _ { \mathcal { T } }$ is not linear, it is however an algebraic variety in some infinite-dimensional Banach space.

Remark 2.23 In most cases considered below, our regularity structure contains $\mathcal { T } _ { d , \mathfrak { s } }$for some dimension d and scaling s. In such a case, we denote by$\bar { T } \subset T$ the image of the model space of$\mathcal { T }$in T under the inclusion map and we only consider models ( , ) that extend (in the sense of Definition 2.22) the polynomial model on$\bar { T }$. It is straightforward to verify that the polynomial model does indeed verify the bounds and algebraic relations of Definition 2.17, provided that we make the identification$\Gamma _ { x y } \sim \Gamma _ { h }$with$h = x - y$

Remark 2.24 If, for every$a \in T _ { \ell } , \Pi _ { x } a$happens to be a function such that $| \Pi _ { x } a ( y ) | \leq C \| x - y \| _ { \mathfrak { s } } ^ { \ell }$for y close to x, then the first bound in (2.15) holds for$\ell \geq 0$. Informally, it thus states that$\Pi _ { x } a$behaves “as$\mathrm { i f } ^ { \dag }$it were -Hölder continuous at x. The formulation given here has the very significant advantage that it also makes sense for negative values of .

Remark 2.25 Given a linear map$\bar { \Pi } \colon T  S ^ { \prime } ( D )$), and a function$F \colon D \to G$ we can always set

$$
\Gamma_ {x y} = F (x) \cdot F (y) ^ {- 1}, \quad \Pi_ {x} = \bar {\Pi} \circ F (x) ^ {- 1}.\tag{2.19}
$$

Conversely, given a model ( , ) as above and a reference point o, we could set

$$
F (x) = \Gamma_ {x o}, \qquad \bar {\Pi} = \Pi_ {o},\tag{2.20}
$$

and  and could then be recovered from F and by (2.19). The reason why we choose to keep our seemingly redundant formulation is that the definition (2.17) and the bounds (2.15) are more natural in this formulation. We will see in Sect. 8.2 below that in all the cases mentioned in the introduction, there are natural maps and F such that ( , ) are given by (2.19). These are however not of the form (2.20) for any reference point.

Remark 2.26 It follows from the definition (2.3) that the second bound in (2.15) is equivalent to the bound

$$
\| \log \Gamma_ {x y} a \| _ {m} \lesssim \| a \| \| x - y \| _ {\mathfrak {s}} ^ {\ell - m},\tag{2.21}
$$

for all$a \in T _ { \ell }$. Similarly, one can consider instead of (2.17) the equivalent distance obtained by replacing$\Gamma _ { x y }$by log$\Gamma _ { x y }$and similarly for$\bar { \Gamma } _ { x y }$

Remark 2.27 The reason for separating the notion of a regularity structure from the notion of a model is that, in the type of applications that we have in mind, the regularity structure will be fixed once and for all. The model however will typically be random and there will be a different model for the regularity structure for every realisation of the driving noise.

## 2.4 Automorphisms of regularity structures

There is a natural notion of “automorphism” of a given regularity structure.

For this, we first define the set$L _ { 0 } ^ { + }$of linear maps$L \colon T \to T$such that, for every$\alpha \in A$there exists$\gamma \in A$such that$L a \in \oplus _ { \alpha < \beta \leq \gamma } T _ { \beta }$for every$a \in T _ { \alpha }$ We furthermore denote by$L _ { 1 } ^ { + }$<sub>the set of all linear operators</sub>$Q$of the form

$$
Q a - a = L a, \quad L \in L _ {0} ^ {+}.
$$

Finally, we denote by$L ^ { 0 }$the set of invertible “block-diagonal” operators D such that$D T _ { \alpha } \subset T _ { \alpha }$for every$\alpha \in A$

With these notations at hand, denote by$L ^ { + }$the set of all operators of the form

$$
M = D \circ Q, \quad D \in L ^ {0}, \quad Q \in L _ {1} ^ {+}.
$$

This factorisation is unique since it suffices to define$\begin{array} { r } { D = \sum _ { \alpha \in A } \mathcal { Q } _ { \alpha } M \mathcal { Q } _ { \alpha } } \end{array}$and to set$Q = D ^ { - 1 } M$, which yields an element of$L _ { 1 } ^ { + }$. Note also that conjugation by block-diagonal operators preserves$L _ { 1 } ^ { + }$. Furthermore, elements in$L _ { 1 } ^ { + }$can be inverted by using the identity

$$
(1 - L) ^ {- 1} = 1 + \sum_ {n \geq 1} L ^ {n},\tag{2.22}
$$

although this might map some elements of$T _ { \alpha }$into an infinite series. With all of these notations at hand, we then give the following definition:

Definition 2.28 Given a regularity structure$\mathcal { T } = ( A , T , G )$, its group of automorphisms Aut$\mathcal { T }$is given by

$$
\operatorname{Aut} \mathcal {T} = \{M \in L ^ {+}: M ^ {- 1} \Gamma M \in G \forall \Gamma \in G \}.
$$

Remark 2.29 This is really an abuse of terminology since it might happen that Aut$\mathcal { T }$contains some elements in whose inverse maps finite series into infinite series and therefore does not belong to$L ^ { + }$. In most cases of interest however, the index set A is finite, in which case Aut$\mathcal { T }$is always an actual group.

The reason why Aut$\mathcal { T }$is important is that its elements induce an action on the models for$\mathcal { T }$by

$$
R _ {M} \colon (\Pi , \Gamma) \mapsto (\bar {\Pi}, \bar {\Gamma}), \quad \bar {\Pi} _ {x} = \Pi_ {x} M, \quad \bar {\Gamma} _ {x y} = M ^ {- 1} \Gamma_ {x y} M.
$$

One then has:

Proposition 2.30 For every$M \in \operatorname { A u t } \mathcal { T } , R _ { M }$is a continuous mapfrom$\mathcal { M } _ { \mathcal { T } }$ into itself.

Proof It is clear that the algebraic identities (2.18) are satisfied, so we only need to check that the analytical bounds of Definition 2.17 hold for$( \bar { \Pi } , \bar { \Gamma } )$

For , this is straightforward since, for$a \in T _ { \alpha }$and any$M \in L ^ { + }$, one has

$$
\begin{array}{l} \bar {\Pi} _ {x} a (\psi_ {x} ^ {\lambda}) = \Pi_ {x} M a (\psi_ {x} ^ {\lambda}) = \sum_ {\beta \in A \cap [ \alpha , \gamma ]} \Pi_ {x} \mathcal {Q} _ {\beta} M a (\psi_ {x} ^ {\lambda}) \\ \qquad \leq C \| a \| _ {\alpha} \sum_ {\beta \in A \cap [ \alpha , \gamma ]} \lambda^ {\beta} \leq \tilde {C} \lambda^ {\alpha} \| a \| _ {\alpha}, \end{array}
$$

where, for a given test function ψ we use the shorthand$\psi _ { x } ^ { \lambda } = S _ { \mathfrak { s } , x } ^ { \lambda } \psi$and where$\tilde { C }$is a finite constant depending only on the norms of the components of M and on the value$\gamma$appearing in the definition of$L ^ { + }$

For , we similarly write, for$a \in T _ { \alpha }$and$\beta < \alpha$

$$
\begin{array}{l} \| (\bar {\Gamma} _ {x y} - 1) a \| _ {\beta} = \| M ^ {- 1} (\Gamma_ {x y} - 1) M a \| _ {\beta} \leq C \sum_ {\zeta \leq \beta} \| (\Gamma_ {x y} - 1) M a \| _ {\zeta} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}
$$

Since one has on the one hand$\zeta \leq \beta$and on the other hand$\xi \ge \alpha$, all terms appearing in this sum involve a power of$\| x - y \| _ { \mathfrak { s } }$that is at least equal to $\alpha - \beta$. Furthermore, the sum is finite by the definition of$L ^ { + }$, so that the claim follows at once.□

## 3 Modelled distributions

Given a regularity structure$\mathcal { T }$, as well as a model ( , ), we are now in a position to describe a class of distributions that locally “look like” the distributions in the model. Inspired by Definition 2.14, we define the space$\mathcal { D } ^ { \gamma }$(which depends in general not only on the regularity structure, but also on the model) in the following way.

Definition 3.1 Fix a regularity structure$\mathcal { T }$and a model ( , ). Then, for any$\gamma \in \mathbf { R }$, the space$\mathcal { D } ^ { \gamma }$consists of all$T _ { \gamma } ^ { - }$-valued functions f such that, for

every compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$, one has

$$
\| f\|_{\gamma ;\mathfrak{K}} = \sup_{x\in \mathfrak{K}}\sup_{\beta <  \gamma}\| f(x)\|_{\beta} + \sup_{\substack{(x,y)\in \mathfrak{K}\\ \| x - y\|_{\mathfrak{s}}\leq 1}}\sup_{\beta <  \gamma}\frac{\|f(x) - \Gamma_{xy}f(y)\|_{\beta}}{\|x - y\|_{\mathfrak{s}}^{\gamma - \beta}} <  \infty .\tag{3.1}
$$

Here, the supremum runs only over elements$\beta \ \in \ A$. We call elements of $\mathcal { D } ^ { \gamma }$modelled distributions for reasons that will become clear in Theorem 3.10 below.

Remark 3.2 One could alternatively think of$\mathcal { D } ^ { \gamma }$as consisting of equivalence classes of functions where$f \sim g \mathrm { i f } \ Q _ { \alpha } f ( x ) = \mathcal { Q } _ { \alpha } g ( x )$for every$x \in \mathbf { R } ^ { d }$ and every$\alpha \ : < \gamma$. However, any such equivalence class has one natural distinguished representative, which is the function$f$such that$\mathcal { Q } _ { \alpha } f ( x ) = 0$for every$\alpha \geq \gamma$, and this is the representative used in (3.1). (In general, the norm $\Vert \cdot \Vert _ { \gamma ; \mathscr { R } }$would depend on the choice of representative because$\Gamma _ { x y } \tau$can have components in$T _ { \gamma } ^ { - }$even if$\tau$itself doesn’t.) In the sequel, if we state that $f \in { \mathcal { D } } ^ { \gamma }$for some$f$which does not necessarily take values in$T _ { \gamma } ^ { - }$, it is this representative that we are talking about. This also allows to identify$\mathcal { D } ^ { \bar { \gamma } }$as a subspace of$\mathcal { D } ^ { \gamma }$for any$\bar { \Gamma } > \bar { \gamma }$. (Verifying that this is indeed the case is a useful exercise!)

Remark 3.3 The choice of notation$\mathcal { D } ^ { \gamma }$is intentionally close to the notation$\mathcal { C } ^ { \gamma }$ for the space of$\gamma { \mathrm { - H } } { \mathrm { i } } \mathrm { d } \mathrm { e r }$continuous functions since, in the case of the “canon ical” regularity structures built from polynomials, the two spaces essentially agree, as we saw in Sect. 2.2.

Remark 3.4 The spaces$\mathcal { D } ^ { \gamma }$, as well as the norms$\| \cdot \| _ { \gamma ; \mathbb { A } }$do depend on the choice of , but not on the choice of . However, Definition 2.17 strongly interweaves  and , so that a given choice of typically restricts the choice of very severely. As we will see in Proposition 3.31 below, there are actually situations in which the choice of  completely determines . In order to compare elements of spaces$\mathcal { D } ^ { \gamma }$corresponding to different choices of , say $f \in { \mathcal { D } } ^ { \gamma } ( \Gamma )$and$\bar { f } \in \bar { \mathcal { D } } ^ { \gamma } ( \bar { \Gamma } )$, it will be convenient to introduce the norm

$$
\| f - \bar {f} \| _ {\gamma ; \mathfrak {K}} = \sup _ {x \in \mathfrak {K}} \sup _ {\beta <   \gamma} \| f (x) - \bar {f} (x) \| _ {\beta},
$$

which is independent of the choice of . Measuring the distance between elements of$\mathcal { D } ^ { \gamma }$in the norm$\| \cdot \| _ { \gamma ; \mathbb { A } }$will be sufficient to obtain some convergence properties, as long as this is supplemented by uniform bounds in$\| \cdot \| _ { \gamma ; \mathbb { A } }$

Remark 3.5 It will often be advantageous to consider elements of$\mathcal { D } ^ { \gamma }$that only take values in a given sector V of T. In this case, we use the notation ${ \mathcal { D } } ^ { \gamma } ( V )$instead. In cases where V is of regularity$\alpha$for some$\alpha \geq$min A, we will also occasionally use instead the notation$\mathcal { D } _ { \alpha } ^ { \dot { \gamma } }$to emphasise this additional regularity. Occasionally, we will also write$\mathcal { D } ^ { \gamma } ( \Gamma )$or$\mathcal { D } ^ { \gamma } ( \Gamma ; V )$to emphasise the dependence of these spaces on the particular choice of .

Remark 3.6 A more efficient way of comparing elements$f \in { \mathcal { D } } ^ { \gamma } ( \Gamma )$and $\bar { f } \in \mathcal { D } ^ { \gamma } ( \bar { \Gamma } )$for two different models ( , ) and$( \bar { \Pi } , \bar { \Gamma } )$is to introduce the quantity

$$
\begin{array}{l}\| f;\bar{f}\|_{\gamma ;\mathfrak{K}} = \| f - \bar{f}\|_{\gamma ;\mathfrak{K}}\\ \qquad +\sup_{\substack{(x,y)\in \mathfrak{K}\\ \| x - y\|_{\mathfrak{s}}\leq 1}}\sup_{\beta <  \gamma}\frac{\|f(x) - \bar{f} (x) - \Gamma_{xy}f(y) + \bar{\Gamma}_{xy}\bar{f} (y)\|_{\beta}}{\|x - y\|_{\mathfrak{s}}^{\gamma - \beta}}. \end{array}
$$

Note that this quantity is not a function of$f - { \bar { f } }$, which is the reason for the slightly unusual notation$\| f ; { \bar { f } } \| _ { \gamma ; \mathscr { R } }$

It turns out that the spaces$\mathcal { D } ^ { \gamma }$encode a very useful notion of regularity. The idea is that functions$f \in { \mathcal { D } } ^ { \gamma }$should be interpreted as “jets” of distributions that locally, around any given point$\boldsymbol { x } \in \mathbf { R } ^ { d }$, “look like” the model distribution $\Pi _ { x } f ( x ) \in S ^ { \prime }$. The results of this section justify this point of view by showing that it is indeed possible to “reconstruct” all elements of$\mathcal { D } ^ { \gamma }$as distributions in$\mathbf { R } ^ { d }$. Furthermore, the corresponding reconstruction map R is continuous as a function of both the element in$f \in { \mathcal { D } } ^ { \gamma }$and the model ( , ) realising the regularity structure under consideration.

To this end, we further extend the definition of the Hölder spaces$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$to include exponents$\alpha < 0$, consisting of distributions that are suitable for our purpose. Informally speaking, elements of$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$have scaling properties akin to $\| x - y \| _ { \mathfrak { s } } ^ { \alpha }$when tested against a test function localised around some$\boldsymbol { x } \in \mathbf { R } ^ { d }$ In the following definition, we write$\mathcal { C } _ { 0 } ^ { r }$for the space of compactly supported $\mathcal { C } ^ { r }$functions. For further properties of the spaces$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$, see Sect. 3.2 below. We set:

Definition 3.7 Let$\alpha < 0$and let$r = - \lfloor \alpha \rfloor$. We say that$\xi \in { \cal S } ^ { \prime }$belongs to $\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$if it belongs to the dual of$\mathcal { C } _ { 0 } ^ { r }$and, for every compact set${ \mathfrak { K } } .$, there exists a constant C such that the bound

$$
\left\langle \xi , \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle \leq C \delta^ {\alpha},
$$

holds for all$\eta \in \mathcal { C } ^ { r }$with$\| \boldsymbol { \eta } \| _ { \mathcal { C } ^ { r } } \leq 1$and suppη$\textsf { C } B _ { 5 } ( 0 , 1 )$, all$\delta \leq 1$, and all $x \in \mathbb { A }$. Here,$B _ { \mathfrak { s } } ( 0 , 1 )$denotes the ball of radius 1 in the distance$d _ { \mathfrak { s } }$, centred at the origin.

From now on, we will denote by$B _ { \mathfrak { s } , 0 } ^ { r }$the set of all test functions$\eta$as in Definition 3.7. For$\xi \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$and$\mathscr { k }$a compact set, we will henceforth denote by $\| \xi \| _ { \alpha ; \mathcal { R } }$the seminorm given by

$$
\| \xi \| _ {\alpha ; \mathfrak {K}} \stackrel {{\text { def }}} {{=}} \sup _ {x \in \mathfrak {K}} \sup _ {\eta \in \mathcal {B} _ {\mathfrak {s}, 0} ^ {r}} \sup _ {\delta \leq 1} \delta^ {- \alpha} | \langle \xi , \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle |.\tag{3.2}
$$

We also write$\| \cdot \| _ { \alpha }$for the same expression with$\mathcal { R } = \mathbf { R } ^ { d }$

Remark 3.8 The space$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$is essentially the Besov space$B _ { \infty , \infty } ^ { \alpha }$(see e.g. [83]), with the slight difference that our definition is local rather than global and, more importantly, that it allows for non-Euclidean scalings.

Remark 3.9 The seminorm (3.2) depends of course not only on α, but also on the choice of scaling s. This scaling will however always be clear from the context, so we do not emphasise this in the notation.

The following “reconstruction theorem” is one of the main workhorses of this theory.

Theorem 3.10 (Reconstruction theorem) Let$\mathcal { T } = ( A , T , G )$be a regularity structure, let ( , ) be a model for$\mathcal { T }$on$\mathbf { R } ^ { d }$with scaling s, let$\alpha = \operatorname* { m i n } A _ { \mathrm { { } } }$ and let$r > | \alpha |$

Then,for every$\gamma \in \mathbf { R }$, there exists a continuous linear map$\mathcal { R } \colon \mathcal { D } ^ { \gamma }  \mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$ with the property that,for every compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$

$$
\left| (\mathcal {R} f - \Pi_ {x} f (x)) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta) \right| \lesssim \delta^ {\gamma} \| \Pi \| _ {\gamma ; \bar {\mathfrak {K}}} \| f \| _ {\gamma ; \bar {\mathfrak {K}}},\tag{3.3}
$$

uniformly over all testfunctions$\eta \in B _ { \mathfrak { s } , 0 } ^ { r } ,$, all$\delta \in ( 0 , 1 ]$, all$f \in { \mathcal { D } } ^ { \gamma }$, and all $x \in { \mathcal { R } } . f \gamma > 0 .$, then the bound (3.3) defines Rf uniquely. Here, we denoted by K¯ the 1-fattening ofK, and the proportionality constant depends only on$\gamma$ and the structure of$\mathcal { T }$

Furthermore,$i f ( { \bar { \Pi } } , { \bar { \Gamma } } )$is a second modelfor$\mathcal { T }$with associated reconstruction operator$\bar { \mathcal { R } } ,$, then one has the bound

$$
\begin{array}{l} \left| \left(\mathcal {R} f - \bar {\mathcal {R}} \bar {f} - \Pi_ {x} f (x) + \bar {\Pi} _ {x} \bar {f} (x)\right) \left(\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta\right) \right| \lesssim \delta^ {\gamma} \left(\| \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}} \| f; \bar {f} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}} \| f \| _ {\gamma ; \bar {\mathfrak {K}}}\right), \end{array} \tag {3.}\tag{3.4}
$$

uniformly over x and η as above. Finally, for$0 < \kappa < \gamma / ( \gamma - \alpha )$and for every$C > 0$, one has the bound

$$
\begin{array}{r l} & {\big | \big (\mathcal {R} f - \bar {\mathcal {R}} \bar {f} - \Pi_ {x} f (x) + \bar {\Pi} _ {x} \bar {f} (x) \big) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta) \big |} \\ & {\quad \lesssim \delta^ {\bar {\Gamma}} \left(\| f - \bar {f} \| _ {\gamma ; \bar {\mathfrak {K}}} ^ {\kappa} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}} ^ {\kappa} + \| \Gamma - \bar {\Gamma} \| _ {\gamma ; \bar {\mathfrak {K}}} ^ {\kappa}\right),} \end{array}\tag{3.5}
$$

where we set$\bar { \Gamma } = \gamma - \kappa ( \gamma - \alpha )$, and where we assume that$f \| _ { \gamma ; \bar { \mathcal { R } } } , \| \Pi \| _  \gamma ;$K and$\| \Gamma \| _ { \gamma ; \bar { \mathcal { R } } }$are bounded by$C ,$, and similarlyfor${ \bar { f } } ,$, and$\bar { \Gamma }$.

Remark 3.11 At first sight, it might seem surprising that$\Gamma$does not appear in the bound (3.3). It does however appear in a hidden way through the definition of the spaces$\mathcal { D } ^ { \gamma }$and thus of the norm$\| f \| _ { \gamma ; { \bar { \mathcal { R } } } } .$. Furthermore, (3.3) is quite reasonable since, for$\Gamma$fixed, the map$\mathcal { R }$is actually bilinear in$f$and . However, the mere existence of$\mathcal { R }$depends crucially on the nonlinear structure encoded in Definition 2.17, and the spaces$\mathcal { D } ^ { \gamma }$do depend on the choice of$\Gamma$. Occasionally, when the particular model ( , ) plays a role, we will denote R by$\mathcal { R } _ { \Gamma }$in order to emphasise its dependence on$\Gamma$

Remark 3.12 Setting$\tilde { f } ( y ) = f ( y ) - \Gamma _ { y x } f ( x )$, we note that one has

$$
\mathcal {R} f - \Pi_ {x} f (x) = \mathcal {R} \tilde {f} - \Pi_ {x} \tilde {f} (x) = \mathcal {R} \tilde {f}.
$$

As a consequence, the bound (3.3) actually depends only on the second term in the right hand side of (3.1).

Remark 3.13 In the particular case when$( \bar { \Pi } , \bar { \Gamma } ) = ( \Pi , \Gamma )$, the bound (3.4) is a trivial consequence of (3.3) and the bilinearity of R in$f$and . As it stands however, this bound needs to be stated and proved separately. The bound (3.5) can be interpreted as an interpolation theorem between (3.3) and (3.4).

Proof (uniqueness only) The uniqueness of the map$\mathcal { R }$in the case$\gamma > 0$is quite easy to prove. Take$f \in { \mathcal { D } } ^ { \gamma }$as in the statement and assume that the two distributions$\xi _ { 1 }$and$\xi _ { 2 }$are candidates for$\mathcal { R } f$that both satisfy the bound (3.3). Our aim is to show that one then necessarily has$\xi _ { 1 } = \xi _ { 2 }$. Take any smooth compactly supported test function$\psi : \mathbf { R } ^ { d }  \mathbf { R }$, and choose an even smooth function$\eta \colon B _ { 1 } \to \mathbf { R } _ { + }$with$\textstyle \int \eta ( x ) d x = 1$. Define

$$
\psi_ {\delta} (y) = \left\langle \mathcal {S} _ {\mathfrak {s}, y} ^ {\delta} \eta , \psi \right\rangle = \int \psi (x) \left(\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta\right) (y) d x,
$$

so that, for any distribution$\xi$, one has the identity

$$
\xi (\psi_ {\delta}) = \int \psi (x) \left\langle \xi , \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle d x.\tag{3.6}
$$

Choosing$\xi = \xi _ { 2 } - \xi _ { 1 }$, it then follows from (3.3) that

$$
| \xi (\psi_ {\delta}) | \lesssim \delta^ {\gamma} \int_ {D} \psi (x) \bar {\varrho} (x) d x,
$$

which converges to 0 as$\delta  0$. On the other hand, one has$\psi _ { \delta }  \psi$in the${ \mathcal { C } } ^ { \infty }$ topology, so that$\xi ( \psi _ { \delta } )  \xi ( \psi )$. This shows that$\xi ( \psi ) = 0$for every smooth compactly supported test function$\psi$, so that$\xi = 0$

The existence of a map$\mathcal { R }$with the required properties is much more difficult to establish, and this is the content of the remainder of this section.□

Remark 3.14 We call the map$\mathcal { R }$the “reconstruction map” as it allows to reconstruct a distribution in terms of its local description via a model and regularity structure.

Remark 3.15 One very important special case is when the model ( , ) happens to be such that there exists$\alpha > 0$such that$\Pi _ { x } a \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha } ( \mathbf { R } ^ { d } )$for every $a \in T$, even though the homogeneity of$a$might be negative. In this case, for $f \in \mathcal { D } ^ { \gamma }$with$\gamma > 0 , \mathcal { R } f$is a continuous function and one has the identity $( \mathcal { R } f ) ( x ) = ( \Pi _ { x } f ( x ) ) ( x )$. Indeed, setting$\tilde { \mathcal { R } } f ( x ) = ( \Pi _ { x } f ( x ) ) ( x )$, one has

$$
\begin{array}{c} \left| \tilde {\mathcal {R}} f (y) - \tilde {\mathcal {R}} f (x) \right| \leq | (\Pi_ {x} f (x)) (x) - (\Pi_ {x} f (x)) (y) | \\ + \left| \Pi_ {y} \left(\Gamma_ {y x} f (x) - f (y)\right) (y) \right|. \end{array}
$$

By assumption, the first term is bounded by$C \| x - y \| _ { \mathfrak { s } } ^ { \alpha }$for some constant$C$ The second term on the other hand is bounded by$C \| x - y \| _ { \mathfrak { s } } ^ { \gamma }$by the definition of$\mathcal { D } ^ { \gamma }$, combined with the fact that our assumption on the model implies that $( \Pi _ { x } a ) ( x ) = 0$whenever a is homogeneous of positive degree.□

A straightforward corollary of this result is given by the following statement, which is the a posteriori justification for the terminology “regularity” in Definition 2.5:

Corollary 3.16 In the context of the statement of Theorem 3.10, if f takes values in a sector V ofregularity$\beta \in [ \alpha , 0 )$, then one has$\mathcal { R } f \in \mathcal { C } _ { \mathfrak { s } } ^ { \beta }$and,for every compact set$\mathscr { k }$and$\gamma > 0$, there exists a constant C such that

$$
\| \mathcal {R} f \| _ {\beta ; \mathfrak {K}} \leq C \| \Pi \| _ {\gamma ; \bar {\mathfrak {K}}} \| f \| _ {\gamma ; \bar {\mathfrak {K}}}.
$$

Proof Immediate from (3.3), Remark 2.20, and the definition of$\| \cdot \| _ { \beta ; \mathscr { R } }$□

Before we proceed to the remainder of the proof of Theorem 3.10, we introduce some of the basic notions of wavelet analysis required for its proof. For a more detailed introduction to the subject, see for example [30,83].

## 3.1 Elements of wavelet analysis

Recall that a multiresolution analysis of R is based on a real-valued “scaling function”$\varphi \in L ^ { 2 } ( \mathbf { R } )$with the following two properties:

1. One has$\begin{array} { r } { \int \varphi ( x ) \varphi ( x + k ) d x = \delta _ { k , 0 } } \end{array}$for every$k \in \mathbf { Z }$

-2. There exist “structure constants” a such that

$$
\varphi (x) = \sum_ {k \in \mathbf {Z}} a _ {k} \varphi (2 x - k).\tag{3.7}
$$

One classical example of such a function$\varphi$is given by the indicator function $\varphi ( x ) = \mathbf { 1 } _ { [ 0 , 1 ) } ( x )$, but this has the substantial drawback that it is not even continuous. A celebrated result by Daubechies (see the original article [29] or for example the monograph [30]) ensures the existence of functions$\varphi$as above that are compactly supported but still regular:

Theorem 3.17 (Daubechies) For every$r > 0$there exists a compactly supported function$\varphi$with the two properties above and such that$\varphi \in \mathcal { C } ^ { r } ( \mathbf { R } )$

From now on, we will always assume that the scaling function$\varphi$is compactly supported. Denote now$\Lambda _ { n } = \{ 2 ^ { - n } k : k \in { \bf Z } \}$and, for${ n \in \mathbf { Z } }$and$x \in \Lambda _ { n }$, set

$$
\varphi_ {x} ^ {n} (y) = 2 ^ {n / 2} \varphi \left(2 ^ {n} (y - x)\right).\tag{3.8}
$$

One furthermore denotes by$V _ { n } \subset L ^ { 2 } ( \mathbf { R } )$the subspace generated by$\{ \varphi _ { x } ^ { n } : x \in$ $\textstyle \Lambda _ { n } \}$. Property 2 above then ensures that these spaces satisfy the inclusion$V _ { n } \subset$ $V _ { n + 1 }$for every$n .$. Furthermore, it turns out that there is a simple description of the orthogonal complement$V _ { n } ^ { \perp }$of$V _ { n }$in$V _ { n + 1 }$. It turns out that it is possible to find finitely many coefficients$b _ { k }$such that, setting

$$
\psi (x) = \sum_ {k \in \mathbf {Z}} b _ {k} \varphi (2 x - k),\tag{3.9}
$$

and defining$\psi _ { x } ^ { n }$similarly to (3.8), the space$V _ { n } ^ { \perp }$is given by the linear span of$\{ \psi _ { x } ^ { n } ~ : ~ x ~ \in ~ \Lambda _ { n } \}$, see for example [88, Chap. 6.4.5]. (One has actually $b _ { k } = ( - 1 ) ^ { k } a _ { 1 - k }$but this isn’t important for us.) The following result is taken from [83]:

Theorem 3.18 One has$\langle \psi _ { x } ^ { n } , \psi _ { v } ^ { m } \rangle = \delta _ { n , m } \delta _ { x , y }$for every$n , m \in \mathbf { Z }$and every $x \in \Lambda _ { n } , y \in \Lambda _ { m }$. Furthermore,$\langle \varphi _ { x } ^ { n } , \psi _ { v } ^ { m } \rangle = 0$for every$m \geq n$and every $x \in \Lambda _ { n } , y \in \Lambda _ { m }$. Finally,for every$n \in \dot { \mathbf { Z } } ,$, the set

$$
\{\varphi_ {x} ^ {n}: x \in \Lambda_ {n} \} \cup \{\psi_ {x} ^ {m}: m \geq n, x \in \Lambda_ {m} \},
$$

forms an orthonormal basis of$L ^ { 2 } ( \mathbf { R } )$

Intuitively, one should think ofthe$\varphi _ { x } ^ { n }$as providing a description ofa function at scales down to$2 ^ { - n }$and the$\psi _ { x } ^ { m }$as “filling in the details” at even smaller scales. In particular, for every function$f \in \bar { L } ^ { 2 }$, one has

$$
\lim _ {n \to \infty} \mathcal {P} _ {n} f {\stackrel {\mathrm{def}} {=}} \lim _ {n \to \infty} \sum_ {x \in \Lambda_ {n}} \left\langle f, \varphi_ {x} ^ {n} \right\rangle \varphi_ {x} ^ {n} = f,\tag{3.10}
$$

and this relation actually holds for much larger classes of$f$, including sufficiently regular tempered distributions [83].

One very useful properties of wavelets, which can be found for example in [83, Chap. 3.2], is that the functions$\psi _ { x } ^ { m }$automatically have vanishing moments:

Lemma 3.19 Let ϕ be a compactly supported scalingfunction as above which is C<sup>r</sup> for$r \geq 0$and let ψ be defined by (3.9). Then,$\textstyle \int _ { \mathbf { R } } \psi ( x ) x ^ { m } d x = 0$for every integer m$\leq r .$□

For our purpose, we need to extend this construction to$\mathbf { R } ^ { d }$. Classically, such an extension can be performed by simply taking products of the$\varphi _ { x } ^ { n }$for each coordinate. In our case however, we want to take into account the fact that we consider non-trivial scalings. For any given scaling s of$\mathbf { R } ^ { d }$and any ${ n \in \mathbf { Z } }$, we thus define

$$
\Lambda_ {n} ^ {\mathfrak {s}} = \left\{\sum_ {j = 1} ^ {d} 2 ^ {- n \mathfrak {s} _ {j}} k _ {j} e _ {j}: k _ {j} \in \mathbf {Z} \right\} \subset \mathbf {R} ^ {d},
$$

where we denote by$e _ { j }$the jth element of the canonical basis of$\mathbf { R } ^ { d }$. For every $x \in \Lambda _ { n } ^ { \mathfrak { s } }$, we then set

$$
\varphi_ {x} ^ {n, \mathfrak {s}} (y) \stackrel {{\text { def }}} {{=}} \prod_ {j = 1} ^ {d} \varphi_ {x _ {j}} ^ {n \mathfrak {s} _ {j}} (y _ {j}).\tag{3.11}
$$

Since we assume that$\varphi$is compactly supported, it follows from (3.7) that there exists a finite collection of vectors$\kappa \subset \Lambda _ { 1 } ^ { \mathfrak { s } }$and structure constants $\{ a _ { k } : k \in \mathcal { K } \}$such that the identity

$$
\varphi_ {x} ^ {0, \mathfrak {s}} (y) = \sum_ {k \in \mathcal {K}} a _ {k} \varphi_ {x + k} ^ {1, \mathfrak {s}} (y),\tag{3.12}
$$

holds. In order to simplify notations, we will henceforth use the notation

$$
2 ^ {- n \mathfrak {s}} k = \left(2 ^ {- n \mathfrak {s} _ {1}} k _ {1}, \dots , 2 ^ {- n \mathfrak {s} _ {d}} k _ {d}\right),
$$

so that the scaling properties of the$\varphi _ { x } ^ { n , \mathfrak { s } }$combined with (3.12) imply that

$$
\varphi_ {x} ^ {n, \mathfrak {s}} (y) = \sum_ {k \in \mathcal {K}} a _ {k} \varphi_ {x + 2 ^ {- n \mathfrak {s}} k} ^ {n + 1, \mathfrak {s}} (y).\tag{3.13}
$$

Similarly, there exists a finite collection  of orthonormal compactly supported functions such that, if we define$V _ { n }$similarly as before,$V _ { n } ^ { \perp }$is given by

$$
V _ {n} ^ {\perp} = \operatorname{span} \{\psi_ {x} ^ {n, \mathfrak {s}}: \psi \in \Psi x \in \Lambda_ {n} ^ {\mathfrak {s}} \}.
$$

In this expression, given a function$\psi \in \Psi$, we have set$\psi _ { x } ^ { n , 5 } = 2 ^ { - n | \mathfrak { s } | / 2 } S _ { \mathfrak { s } , x } ^ { 2 ^ { - n } } \psi$ where the scaling map was defined in (2.13). (The additional factor makes sure that the scaling leaves the$L ^ { 2 }$norm invariant instead of the$L ^ { 1 }$norm, which is more convenient in this context.) Furthermore, this collection forms an orthonormal basis of$V _ { n } ^ { \perp }$. Actually, the set  is given by all functions obtained by products of the form$\Pi _ { i = 1 } ^ { d } \psi _ { \pm } ( x _ { i } )$, where$\psi _ { - } = \psi$and$\psi _ { + } = \varphi$ and where at least one factor consists of an instance of$\psi$

## 3.2 A convergence criterion in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$

The spaces$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$with$\alpha < 0$given in Definition 3.7 enjoy a number ofremarkable properties that will be very useful in the sequel. In particular, it turns out that distributions in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$can be completely characterised by the magnitude of the coefficients in their wavelet expansion. This is true independently of the particular choice of the scaling function$\varphi _ { \cdot }$, provided that it has sufficient regularity.

In this sense, the interplay between the wavelet expansion and the spaces $\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$is very similar to the classical interplay between Fourier expansion and fractional Sobolev spaces. The feature of wavelet expansions that makes it much more suitable for our purpose is that its basis functions are compactly supported with supports that are more and more localised for larger values of n. The announced characterisation is given by the following.

Proposition 3.20 Let$\alpha < 0$and$\xi \in \mathcal { S } ^ { \prime } ( \mathbf { R } ^ { d } )$. Consider a wavelet analysis as above with a compactly supported scalingfunction$\varphi \in \mathcal { C } ^ { r }$for some$r > | \alpha |$ Then$\xi \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$ifand only$i f \xi$belongs to the dual of$\mathcal { C } _ { 0 } ^ { r }$and,for every compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$, the bounds

$$
\left| \left\langle \xi , \psi_ {x} ^ {n, \mathfrak {s}} \right\rangle \right| \lesssim 2 ^ {- \frac {n | \mathfrak {s} |}{2} - n \alpha}, \quad \left| \left\langle \xi , \varphi_ {y} ^ {0} \right\rangle \right| \lesssim 1,\tag{3.14}
$$

hold uniformly over$n \geq 0$, every$\psi ~ \in ~ \Psi$, every$x \ \in \ \Lambda _ { n } ^ { \mathfrak { s } } \ \cap \ \mathfrak { K } .$, and every $y \in \Lambda _ { 0 } ^ { \mathfrak { s } } \cap \mathfrak { K } .$

The proof of Proposition 3.20 relies on classical arguments very similar to those found for example in the monograph [83]. Since the spaces with inhomogeneous scaling do not seem to be standard in the literature and since we consider localised versions of the spaces, we prefer to provide a proof. Before we proceed, we state the following elementary fact:

Lemma 3.21 Let$a \in \mathbf { R }$and let$b _ { - } , b _ { + } \in \mathbf { R }$. Then, the bound

$$
\sum_ {n = 0} ^ {n _ {0}} 2 ^ {a n} 2 ^ {- b _ {-} (n _ {0} - n)} + \sum_ {n = n _ {0}} ^ {\infty} 2 ^ {a n} 2 ^ {- b _ {+} (n - n _ {0})} \lesssim 2 ^ {a n _ {0}},
$$

holds provided that$b _ { + } > a$and$b _ { - } > - a$

ProofofProposition 3.20 It is clear that the condition (3.14) is necessary, since it boils down to taking$\eta \in \Psi$and$\delta = 2 ^ { - n }$in Definition 3.7. In order to show that it is also sufficient, we take an arbitrary test function$\eta \in \mathcal { C } ^ { r }$with support in$B _ { 1 }$and we rewrite$\langle \xi , { \mathcal { S } } _ { \mathfrak { s } , x } ^ { \delta } \eta \rangle$as

$$
\left\langle \xi , \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle = \sum_ {n \geq 0} \sum_ {y \in \Lambda_ {n} ^ {\mathfrak {s}}} \left\langle \xi , \psi_ {y} ^ {n, \mathfrak {s}} \right\rangle \left\langle \psi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle + \sum_ {y \in \Lambda_ {0} ^ {\mathfrak {s}}} \left\langle \xi , \varphi_ {y} ^ {0, \mathfrak {s}} \right\rangle \left\langle \varphi_ {y} ^ {0, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle .\tag{3.15}
$$

Let furthermore$n _ { 0 }$be the smallest integer such that$2 ^ { - n _ { 0 } } \leq \delta$. For the situations where the supports of$\psi _ { y } ^ { n , 5 }$and$\mathcal { S } _ { \mathfrak { s } , x } ^ { \delta } \eta$overlap, we then have the following bounds.

First, we note that if$( x , y )$contributes to (3.15), then$\| x - y \| _ { \mathfrak { s } } \leq C$for some fixed constant C. As a consequence of this, it follows that one has the bound

$$
\left| \left\langle \xi , \psi_ {y} ^ {n, \mathfrak {s}} \right\rangle \right| \lesssim 2 ^ {- \frac {n | \mathfrak {s} |}{2} - n \alpha},\tag{3.16}
$$

uniformly over all pairs$( x , y )$yielding a non-vanishing contribution to (3.15).

For$n \geq n _ { 0 }$, and$\| x - y \| _ { \mathfrak { s } } \leq C \delta$, we furthermore have the bound

$$
\left| \left\langle \psi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle \right| \lesssim 2 ^ {- (n - n _ {0}) \left(r + \frac {| \mathfrak {s} |}{2}\right)} 2 ^ {\frac {n _ {0} | \mathfrak {s} |}{2}},\tag{3.17}
$$

so that

$$
\sum_ {y \in \Lambda_ {n} ^ {\mathfrak {s}}} \left| \left\langle \psi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle \right| \lesssim 2 ^ {- (n - n _ {0}) \left(r - \frac {| \mathfrak {s} |}{2}\right)} 2 ^ {\frac {n _ {0} | \mathfrak {s} |}{2}}.
$$

Here and below, the proportionality constants are uniform over all$\eta$with $\| \boldsymbol { \eta } \| _ { \mathcal { C } ^ { r } } \leq 1$with suppη$\subset B _ { 1 }$. On the other hand, for$n \leq n _ { 0 }$, and$\| x - y \| _ { 5 } \leq$ $C 2 ^ { - n _ { 0 } }$, we have the bound

$$
\left| \left\langle \psi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle \right| \lesssim 2 ^ {n \frac {| \mathfrak {s} |}{2}},\tag{3.18}
$$

so that, since only finitely many terms contribute to the sum,

$$
\sum_ {y \in \Lambda_ {n} ^ {\mathfrak {s}}} \left| \left\langle \psi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle \right| \lesssim 2 ^ {n \frac {| \mathfrak {s} |}{2}}.
$$

Since, by the assumptions on r and$\alpha ,$, one has indeed$\begin{array} { r } { r + \frac { | \mathfrak { s } | } { 2 } > \alpha + \frac { | \mathfrak { s } | } { 2 } } \end{array}$and $\begin{array} { r } { { \frac { | { \mathfrak { s } } | } { 2 } } > { \frac { | { \mathfrak { s } } | } { 2 } } - \alpha } \end{array}$, we can apply Lemma 3.21 to conclude that the first sum in (3.15) is indeed bounded by a multiple of$\delta ^ { \alpha }$, which is precisely the required bound. The second term on the other hand satisfies a bound similar to (3.18) with$n = 0$, so that the claim follows.□

Remark 3.22 For$\alpha \geq 0 .$, it is not so straightforward to characterise the Hölder regularity of a function by the magnitude of its wavelet coefficients due to special behaviour at integer values, but for non-integer values the characterisation given above still holds, see [83].

Another nice property of the spaces$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$is that, using Proposition 3.20, one can give a very useful and sharp condition for a sequence of elements in$V _ { n }$ to converge to an element in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$. Once again, we fix a multiresolution analysis of sufficiently high regularity (i.e.$r > \left| \alpha \right| )$and the spaces$V _ { n }$are given in terms of that particular analysis. For this characterisation, we use the fact that a sequence$\{ f _ { n } \} _ { n \ge 0 }$with$f _ { n } \in V _ { n }$for every n can always be written as

$$
f _ {n} = \sum_ {x \in \Lambda_ {n} ^ {\mathfrak {s}}} A _ {x} ^ {n} \varphi_ {x} ^ {n, \mathfrak {s}}, \qquad A _ {x} ^ {n} = \left\langle \varphi_ {x} ^ {n, \mathfrak {s}}, f _ {n} \right\rangle .\tag{3.19}
$$

Given a sequence of coefficients$A _ { x } ^ { n } .$, we then define$\delta A _ { x } ^ { n }$by

$$
\delta A _ {x} ^ {n} = A _ {x} ^ {n} - \sum_ {k \in \mathcal {K}} a _ {k} A _ {x + 2 ^ {- n \mathfrak {s}} k} ^ {n + 1},
$$

where the set$\kappa$and the structure constants$a _ { k }$are as in (3.12). We then have the following result, which can be seen as a generalisation of the “sewing lemma” (see [54, Prop. 1] or [38, Lem. 2.1]), which can itself be viewed as a generalisation of Young’s original theory of integration [100]. In order to make the link to these theories, consider the case where$\mathbf { R } ^ { d }$is replaced by an interval and take for$\varphi$the Haar wavelets.

Theorem 3.23 Let s be a scaling of$\mathbf { R } ^ { d }$, let$\alpha < 0 < \gamma$, and fix a wavelet basis with regularity$r > | \alpha |$. For every$n \geq 0 _ { \mathrm { { i } } }$, let$x \mapsto A _ { x } ^ { n }$be a function on $\mathbf { R } ^ { d }$satisfying the bounds

$$
\left| A _ {x} ^ {n} \right| \leq \| A \| 2 ^ {- \frac {n \mathfrak {s}}{2} - \alpha n}, \quad \left| \delta A _ {x} ^ {n} \right| \lesssim \| A \| 2 ^ {- \frac {n \mathfrak {s}}{2} - \gamma n},\tag{3.20}
$$

for some constant$\| A \|$, uniformly over$n \geq 0$and$\boldsymbol { x } \in \mathbf { R } ^ { d }$

Then, the sequence$\{ f _ { n } \} _ { n \ge 0 }$given by$\begin{array} { r } { f _ { n } = \sum _ { x \in \Lambda _ { n } ^ { \varsigma } } A _ { x } ^ { n } \varphi _ { x } ^ { n , \mathfrak { s } } } \end{array}$converges in$\mathcal { C } _ { \mathfrak { s } } ^ { \bar { \alpha } }$ for every$\bar { \alpha } < \alpha$and its limit f belongs to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$. Furthermore, the bounds

$$
\| f - f _ {n} \| _ {\bar {\alpha}} \lesssim \| A \| 2 ^ {- (\alpha - \bar {\alpha}) n}, \quad \| \mathcal {P} _ {n} f - f _ {n} \| _ {\alpha} \lesssim \| A \| 2 ^ {- \gamma n},\tag{3.21}
$$

hold for$\bar { \alpha } \in ( \alpha - \gamma , \alpha )$, where$\mathcal { P } _ { n }$is as in (3.10).

Proof By linearity, it is sufficient to restrict ourselves to the case$\| A \| = 1$ $\mathtt { B y }$construction, we have$f _ { n + 1 } - f _ { n } \in V _ { n + 1 }$, so that we can decompose this difference as

$$
f _ {n + 1} - f _ {n} = g _ {n} + \delta f _ {n},\tag{3.22}
$$

where$\delta f _ { n } \in V _ { n } ^ { \bot }$and$g _ { n } \in V _ { n }$. By Proposition 3.20, we note that there exists a constant C such that, for every$n \geq 0$and$m \geq n$, and for every$\beta < 0$, one has

$$
\left\| \sum_ {k = n} ^ {m} \delta f _ {k} \right\| _ {\beta} \leq C \sup _ {k \in \{n, \dots , m \}} \| \delta f _ {k} \| _ {\beta},
$$

so that a sufficient condition for the sequence$\textstyle \{ \sum _ { k = 0 } ^ { n } \delta f _ { k } \} _ { n \geq 0 }$to have the required properties is given by

$$
\lim _ {n \to \infty} \| \delta f _ {n} \| _ {\bar {\alpha}} = 0, \quad \sup _ {n} \| \delta f _ {n} \| _ {\alpha} <   \infty .\tag{3.23}
$$

Regarding the bounds on$\delta f _ { n }$, we have

$$
\left\langle \delta f _ {n}, \psi_ {x} ^ {n, \mathfrak {s}} \right\rangle = \left\langle f _ {n + 1} - f _ {n}, \psi_ {x} ^ {n, \mathfrak {s}} \right\rangle = \sum_ {\| x - y \| _ {\mathfrak {s}} \leq K 2 ^ {- n | \mathfrak {s} |}} a _ {x y} A _ {y} ^ {n + 1},
$$

where the$a _ { x y } = \langle \varphi _ { y } ^ { n + 1 , \mathfrak { s } } , \psi _ { x } ^ { n , \mathfrak { s } } \rangle$are a finite number ofuniformly bounded coefficients and$K > 0$is some fixed constant. It then follows from the assumption on the coefficients$A _ { y } ^ { n }$that

$$
\left| \left\langle \delta f _ {n}, \psi_ {x} ^ {n, \mathfrak {s}} \right\rangle \right| \lesssim 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \alpha n}.
$$

Combining this with the characterisation of$\mathcal { C } _ { \mathfrak { s } } ^ { \bar { \alpha } }$given in Proposition 3.20, we conclude that

$$
\| \delta f _ {n} \| _ {\bar {\alpha}} \lesssim 2 ^ {- (\alpha - \bar {\alpha}) n}, \quad \| \delta f _ {n} \| _ {\alpha} \lesssim 1,\tag{3.24}
$$

so that the condition (3.23) is indeed satisfied.

It remains to show that the sequence of partial sums of the$g _ { k }$from (3.22) also satisfies the requested properties. Using again the characterisation given by Proposition 3.20, we see that

$$
\left\| \sum_ {k = n} ^ {m} g _ {k} \right\| _ {\alpha} \lesssim \sup _ {N \geq 0} \sum_ {k = n} ^ {m} \| \mathcal {Q} _ {N} g _ {k} \| _ {\alpha}.\tag{3.25}
$$

From the definition of$g _ { n }$, we furthermore have the identity

$$
\begin{array}{l} \left\langle g _ {n}, \varphi_ {x} ^ {n, \mathfrak {s}} \right\rangle = \left\langle f _ {n + 1} - f _ {n}, \varphi_ {x} ^ {n, \mathfrak {s}} \right\rangle = \left(\sum_ {k \in \mathcal {K}} a _ {k} \left\langle f _ {n + 1}, \varphi_ {x + 2 ^ {- n \mathfrak {s}} k} ^ {n + 1, \mathfrak {s}} \right\rangle\right) - \left\langle f _ {n}, \varphi_ {x} ^ {n, \mathfrak {s}} \right\rangle \\ = - \delta A _ {x} ^ {n}, \end{array} \tag {3.2}\tag{3.26}
$$

so that one can decompose$g _ { n }$as

$$
g _ {n} = - \sum_ {x \in \Lambda_ {n} ^ {\mathfrak {s}}} \delta A _ {x} ^ {n} \varphi_ {x} ^ {n, \mathfrak {s}}.\tag{3.27}
$$

It follows in a straightforward way from the definitions that, for$m \leq n$, there exists a constant C such that we have the bound

$$
\left| \left\langle \psi_ {y} ^ {m, \mathfrak {s}}, \varphi_ {x} ^ {n, \mathfrak {s}} \right\rangle \right| \leq C 2 ^ {(m - n) \frac {| \mathfrak {s} |}{2}} \mathbf {1} _ {\| x - y \| _ {\mathfrak {s}} \leq C 2 ^ {- m}}.\tag{3.28}
$$

Since on the other hand, one has

$$
\left| \left\{x \in \Lambda_ {n} ^ {\mathfrak {s}}: \| x - y \| _ {\mathfrak {s}} \leq C 2 ^ {- m} \right\} \right| \lesssim 2 ^ {(n - m) | \mathfrak {s} |},
$$

we obtain from this and (3.27) the bound

$$
\begin{array}{c} \left| \left\langle \psi_ {y} ^ {m, \mathfrak {s}}, g _ {n} \right\rangle \right| \lesssim 2 ^ {(n - m) \frac {| \mathfrak {s} |}{2}} \sup \left\{| \delta A _ {x} ^ {n} |: \| x - y \| _ {\mathfrak {s}} \leq C 2 ^ {- m} \right\} \\ \lesssim 2 ^ {- m \frac {| \mathfrak {s} |}{2} - \gamma n}, \end{array}\tag{3.29}
$$

where we used again the fact that$\lVert x - y \rVert _ { \mathfrak { s } } \lesssim d _ { \mathfrak { s } } ( y , \partial D )$by the definition of the functions$\psi _ { y } ^ { m , \mathfrak { s } }$. Combining this with the characterisation of$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$given in

Proposition 3.20, we conclude that

$$
\| \mathcal {Q} _ {m} g _ {n} \| _ {\alpha} \lesssim 2 ^ {\alpha m - \gamma n} \mathbf {1} _ {m \leq n},
$$

so that

$$
\sum_ {k = n} ^ {m} \| \mathcal {Q} _ {N} g _ {k} \| _ {\alpha} \lesssim \sum_ {k = n \vee N} ^ {m} 2 ^ {\alpha N - \gamma k} \lesssim 2 ^ {\alpha N - \gamma (N \vee n)}.
$$

This expression is maximised at$N = 0$, so that the bound$\parallel \sum _ { k = n } ^ { m }$g<sub>k α</sub>$\lesssim$ $2 ^ { - \gamma n }$follows from (3.25). Combining this with (3.24), we thus obtain (3.21), as stated.□

A simple but important corollary of the proof is given by

Corollary 3.24 In the situation ofTheorem 3.23, let$\mathcal { R } \subset \mathbf { R } ^ { d }$be a compact set and let$\bar { \mathcal { R } }$be its 1-fattening. Then, provided that (3.20) holds uniformly over $\textstyle { \bar { \mathcal { R } } } ,$the bound (3.21) still holds with$\| \cdot \| _ { \alpha }$replaced by$\| \cdot \| _ { \alpha ; \mathscr { R } } .$

Proof Follow step by step the argument given above noting that, since all the arguments in the proof of Proposition 3.20 are local, one can bound the norm $\| \cdot \| _ { \alpha ; \mathscr { R } }$by the smallest constant such that the bounds (3.14) hold uniformly over x,$y \in \bar { \mathcal { R } }$□

## 3.3 The reconstruction theorem for distributions

One very important special case of Theorem 3.23 is given by the situation where there exists a family$x \ \mapsto \ \zeta _ { x } \ \in \ { \mathcal { S } } ^ { \prime } ( \mathbf { R } ^ { d } )$of distributions such that the sequence$f _ { n }$is given by (3.19) with$A _ { x } ^ { n } = \left. \varphi _ { x } ^ { n , \mathfrak { s } } , \zeta x \right.$. Once this is established, the reconstruction theorem will be straightforward. In the situation just described, we have the following result which, as we will see shortly, can really be interpreted as a generalisation of the reconstruction theorem.

Proposition 3.25 In the above situation, assume that the family$\zeta _ { x }$is such that,for some constants$K _ { 1 }$and$K _ { 2 }$and exponents α$< 0 < \gamma$, the bounds

$$
\left| \left\langle \varphi_ {x} ^ {n, \mathfrak {s}}, \zeta_ {x} - \zeta_ {y} \right\rangle \right| \leq K _ {1} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \alpha} 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \alpha n}, \quad \left| \left\langle \varphi_ {x} ^ {n, \mathfrak {s}}, \zeta_ {x} \right\rangle \right| \leq K _ {2} 2 ^ {- \alpha n - \frac {n | \mathfrak {s} |}{2}},\tag{3.30}
$$

hold uniformly over all x, y such that$2 ^ { - n } \leq \| x - y \| _ { 5 } \leq 1$. Here, as before, $\varphi$is the scaling function for a wavelet basis of regularity$r > | \alpha |$. Then, the assumptions ofTheorem 3.23 are satisfied. Furthermore, the limit distribution $f \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$satisfies the bound

$$
| (f - \zeta_ {x}) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta) | \lesssim K _ {1} \delta^ {\gamma},\tag{3.31}
$$

uniformly over$\eta \in \mathcal { B } _ { \mathfrak { s } , 0 } ^ { r }$. Here, the proportionality constant only depends on the choice ofwavelet basis, but not on$K _ { 2 }$

Proof We are in the situation of Theorem 3.23 with$A _ { x } ^ { n } = \zeta _ { x } ( \varphi _ { x } ^ { n , \mathfrak { s } } )$, so that one has the identity

$$
\delta A _ {x} ^ {n} = \sum_ {k \in \mathcal {K}} a _ {k} \langle \zeta_ {x} - \zeta_ {y}, \varphi_ {y} ^ {(n + 1), \mathfrak {s}} \rangle ,\tag{3.32}
$$

where we used the shortcut$y = x + 2 ^ { - n \mathfrak { s } } k$in the right hand side. It then follows immediately from (3.30) that the assumptions of Theorem 3.23 are indeed satisfied, so that the sequence$f _ { n }$converges to some limit$f .$. It remains to show that the local behaviour of$f$around every point x is given by (3.31).

For this, we write

$$
f - \zeta_ {x} = \left(f _ {n _ {0}} - \mathcal {P} _ {n _ {0}} \zeta_ {x}\right) + \sum_ {n \geq n _ {0}} (f _ {n + 1} - f _ {n} - (\mathcal {P} _ {n + 1} - \mathcal {P} _ {n}) \zeta_ {x})\tag{3.33}
$$

for some$n _ { 0 } > 0$. We choose$n _ { 0 }$to be the smallest integer such that$2 ^ { - n _ { 0 } } \leq \delta$ Note that, as in (3.17), one has for$n \geq n _ { 0 }$the bounds

$$
\begin{array}{l} \left| \left\langle \psi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle \right| \lesssim 2 ^ {\frac {n _ {0} | \mathfrak {s} |}{2}} 2 ^ {- (n - n _ {0}) \left(r + \frac {| \mathfrak {s} |}{2}\right)}, \\ \left| \left\langle \varphi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle \right| \lesssim 2 ^ {\frac {n _ {0} | \mathfrak {s} |}{2}} 2 ^ {- (n - n _ {0}) \frac {| \mathfrak {s} |}{2}}. \end{array}\tag{3.34}
$$

Since, by construction, the first term in (3.33) belongs to$V _ { n _ { 0 } }$, we can rewrite it as

$$
\left(f _ {n _ {0}} - \mathcal {P} _ {n _ {0}} \zeta_ {x}\right) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta) = \sum_ {y \in \Lambda_ {n _ {0}} ^ {\mathfrak {s}}} \left(\zeta_ {y} - \zeta_ {x}\right) (\varphi_ {y} ^ {n _ {0}, \mathfrak {s}}) \left\langle \varphi_ {y} ^ {n _ {0}, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle .
$$

Since terms appearing in the above sum with$\| x - y \| _ { \mathfrak { s } } \ge \delta$are identically 0, we can use the bound

$$
\left| \left(\zeta_ {y} - \zeta_ {x}\right) \left(\varphi_ {y} ^ {n _ {0}, \mathfrak {s}}\right) \right| \lesssim K _ {1} 2 ^ {- \gamma n _ {0} - \frac {n _ {0} | \mathfrak {s} |}{2}}.
$$

Combining this with (3.34) and the fact that there are only finitely many non-vanishing terms in the sum, we obtain the bound

$$
\left| \left(f _ {n _ {0}} - \mathcal {P} _ {n _ {0}} \zeta_ {x}\right) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta) \right| \lesssim K _ {1} 2 ^ {- n _ {0} \gamma} \approx K _ {1} \delta^ {\gamma},\tag{3.35}
$$

which is of the required order.

Regarding the second term in (3.33), we decompose$f _ { n + 1 } - f _ { n }$as in the proof of Theorem 3.23 as$f _ { n + 1 } - f _ { n } = g _ { n } + \delta f _ { n }$with$g _ { n } \in V _ { n }$and$\delta f _ { n } \in V _ { n } ^ { \bot }$ As a consequence of (3.26) and of the bounds (3.30) and (3.34), we have the bound

$$
\begin{array}{l} \left| \left\langle g _ {n}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle \right| \leq \sum_ {y \in \Lambda_ {n} ^ {\mathfrak {s}}} \left| \left\langle g _ {n}, \varphi_ {y} ^ {n, \mathfrak {s}} \right\rangle \right| \left| \left\langle \varphi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle \right| \\ \leq \sum_ {y \in \Lambda_ {n} ^ {\mathfrak {s}}} \left| \delta A _ {y} ^ {n} \right| \left| \left\langle \varphi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle \right| \lesssim K _ {1} 2 ^ {- (n - n _ {0}) (| \mathfrak {s} | + \alpha) - \gamma n}, \end{array}
$$

where we made use of (3.32) for the last bound. Summing this bound over all$n \geq n _ { 0 }$, we obtain again a bound of order$K _ { 1 } \delta ^ { \gamma }$, as required. It remains to obtain a similar bound for the quantity

$$
\sum_ {n \geq n _ {0}} (\delta f _ {n} - (\mathcal {P} _ {n + 1} - \mathcal {P} _ {n}) \zeta_ {x}) \left(\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta\right).
$$

Note that$\delta f _ { n }$is nothing but the projection of$f _ { n + 1 }$onto the space$V _ { n } ^ { \perp }$. Similarly, $( \mathcal P _ { n + 1 } - \mathcal P _ { n } ) \zeta _ { x }$is the projection of$\zeta _ { x }$onto that same space. As a consequence, we have the identity

$$
\begin{array}{l} (\delta f _ {n} - (\mathcal {P} _ {n + 1} - \mathcal {P} _ {n}) \zeta_ {x}) \left(\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta\right) \\ = \sum_ {z \in \Lambda_ {\mathfrak {s}} ^ {n + 1}} \sum_ {y \in \Lambda_ {\mathfrak {s}} ^ {n}} \sum_ {\psi \in \Psi} \big \langle \zeta_ {z} - \zeta_ {x}, \varphi_ {z} ^ {n + 1, \mathfrak {s}} \big \rangle \Big \langle \varphi_ {z} ^ {n + 1, \mathfrak {s}}, \psi_ {y} ^ {n, \mathfrak {s}} \Big \rangle \big \langle \psi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \big \rangle . \end{array}
$$

Note that this triple sum only contains of the order of$2 ^ { ( n - n _ { 0 } ) | \mathfrak { s } | }$terms since, for any given value of y, the sum over z only has a fixed finite number of non-vanishing terms. At this stage, we make use of the first bound in (3.34), together with the assumption (3.30) and the fact that$2 ^ { - n _ { 0 } } \lesssim \| x - z \| _ { \mathfrak { s } } \lesssim \delta$for every term in this sum. This yields for this expression a bound of the order

$$
K _ {1} 2 ^ {(n - n _ {0}) | \mathfrak {s} |} \delta^ {\gamma - \alpha} 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \alpha n} 2 ^ {\frac {n _ {0} | \mathfrak {s} |}{2}} 2 ^ {- (n - n _ {0}) (r + | \mathfrak {s} | / 2)} = K _ {1} \delta^ {\gamma - \alpha} 2 ^ {- r (n - n _ {0}) - \alpha n}.
$$

Since, by assumption, r is sufficiently large so that$r > | \alpha |$, this expression converges to 0 as$n  \infty$. Summing over$n \geq n _ { 0 }$and combining all of the above bounds, the claim follows at once.□

Remark 3.26 As before, the construction is completely local. As a consequence, the required bounds hold over a compact${ \mathfrak { R } } ,$provided that the assumptions hold over its 1-fattening$\bar { \mathbf { \mathcal { R } } }$

We now finally have all the elements in place to give the proof of Theorem 3.10.

ProofofTheorem 3.10 We first consider the case$\gamma > 0$, where the operator $\mathcal { R }$is unique. In order to construct$\mathcal { R }$, we will proceed by successive approximations, using a multiresolution analysis. Again, we fix a wavelet basis as above associated with a compactly supported scaling function$\varphi$. We choose$\varphi$ to be$\mathcal { C } ^ { r }$for$r > |$min$A |$. (Which in particular also implies that the elements $\psi \in \Psi$annihilate polynomials of degree$r . )$

Since, for any given$n > 0$, the functions$\varphi _ { x } ^ { n , \mathfrak { s } }$are orthonormal and since, as$n  \infty$, they get closer and closer to forming a basis of very sharply localised functions of$L ^ { 2 }$, it appears natural to define a sequence of operators $\mathcal { R } _ { n } \colon \mathcal { D } ^ { \gamma }  \mathcal { C } ^ { r }$by

$$
\mathcal {R} _ {n} f = \sum_ {x \in \Lambda_ {n} ^ {\mathfrak {s}}} (\Pi_ {x} f (x)) (\varphi_ {x} ^ {n, \mathfrak {s}}) \varphi_ {x} ^ {n, \mathfrak {s}},
$$

and to define$\mathcal { R }$as the limit of$\textstyle { \mathcal { R } } _ { n }$as$n  \infty$, if such a limit exists.

We are thus precisely in the situation ofProposition 3.25 with$\zeta _ { x } = \Pi _ { x } f ( x )$ Since we are interested in a local statement, we only need to construct the distribution$\mathcal { R } f$acting on test functions supported on a fixed compact domain ${ \mathcal { \kappa } } .$As a consequence, since all of our constructions involve some fixed wavelet basis, it suffices to obtain bounds on the wavelet coefficients$\psi _ { x } ^ { n }$with x such that$\psi _ { x } ^ { n }$is supported in${ \bar { \mathbf { x } } } ,$, the 1-fattening of$\scriptstyle { \mathcal { R } }$

It follows from the definitions of$\mathcal { D } ^ { \gamma }$and the space of models$\mathcal { M } _ { \mathcal { T } }$that, for such values of x, one has

$$
| \left\langle \Pi_ {x} f (x), \varphi_ {x} ^ {n, \mathfrak {s}} \right\rangle | \lesssim \| f \| _ {\gamma ; \bar {\mathfrak {K}}} \| \Pi \| _ {\gamma ; \bar {\mathfrak {K}}} 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \alpha n},
$$

where, as before,$\alpha = \operatorname* { m i n } A$is the smallest homogeneity arising in the description of the regularity structure$\mathcal { T }$. Similarly, we have

$$
\begin{array}{c} \left| \left\langle \Pi_ {x} f (x) - \Pi_ {y} f (y), \varphi_ {x} ^ {n, \mathfrak {s}} \right\rangle \right| = \left| \left\langle \Pi_ {x} \left(f (x) - \Gamma_ {x y} f (y)\right), \varphi_ {x} ^ {n, \mathfrak {s}} \right\rangle \right| \\ \lesssim \sum_ {\ell <   \gamma} \| f \| _ {\gamma ; \bar {\mathfrak {K}}} \| \Pi \| _ {\gamma ; \bar {\mathfrak {K}}} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \ell n}, \end{array}\tag{3.36}
$$

where the sum runs over elements in A. Since, in the assumption of Proposition 3.25, we only consider points$( x , y )$such that$\| x - y \| _ { \mathfrak { s } } \gtrsim 2 ^ { - n }$, the bound (3.30) follows.

As a consequence, we can apply Theorem 3.23 to construct a limiting distribution$\begin{array} { r } { \mathscr { R } f = \operatorname* { l i m } _ { n  \infty } \mathscr { R } _ { n } f } \end{array}$, where convergence takes place in$\mathcal { C } _ { \mathfrak { s } } ^ { \bar { \alpha } }$for every $\bar { \alpha } < \alpha$. Furthermore, the limit does itself belong to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$. The bound (3.3) follows immediately from Proposition 3.25.

In order to obtain the bound (3.4), we use again Proposition 3.25, but this time with$\zeta _ { x } = \Pi _ { x } f ( x ) - { \bar { \Pi } } _ { x } { \bar { f } } ( x )$. We then have the identity

$$
\begin{array}{c} \zeta_ {x} - \zeta_ {y} = \Pi_ {x} \left(f (x) - \Gamma_ {x y} f (y) - \bar {f} (x) + \bar {\Gamma} _ {x y} \bar {f} (y)\right) \\ + (\Pi_ {x} - \bar {\Pi} _ {x}) \left(\bar {f} (x) - \bar {\Gamma} _ {x y} \bar {f} (y)\right). \end{array}
$$

Similarly to above, it then follows from the definition of$\| f ; { \bar { f } } \| _ { \gamma ; \mathscr { R } }$that

$$
\begin{array}{c} \left| \left\langle \zeta_ {x} - \zeta_ {y}, \varphi_ {x} ^ {n, \mathfrak {s}} \right\rangle \right| \lesssim \left(\| \Pi \| _ {\gamma ; \mathfrak {K}} \| f; \bar {f} \| _ {\gamma ; \mathfrak {K}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \mathfrak {K}} \| \bar {f} \| _ {\gamma ; \mathfrak {K}}\right) \\ \times \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \alpha} 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \alpha n}, \end{array}
$$

from which the requested bound follows at once.

The bound (3.5) is obtained again from Proposition 3.25 with$\zeta _ { x } =$ $\Pi _ { x } f ( x ) - { \bar { \Pi } } _ { x } { \bar { f } } ( x )$. This time however, we aim to obtain bounds on this quantity by only making use of bounds on$\| f - \bar { f } \| _ { \gamma ; \mathcal { R } }$rather than$f ; { \bar { f } } \| _ { \gamma ; \mathscr { R } } .$ Note first that, as a consequence of (3.36), we have the bound

$$
\left| \left\langle \zeta_ {x} - \zeta_ {y}, \varphi_ {x} ^ {n, \mathfrak {s}} \right\rangle \right| \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \alpha} 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \alpha n}.\tag{3.37}
$$

On the other hand, we can rewrite$\zeta _ { x } - \zeta _ { y }$as

$$
\begin{array}{c} \zeta_ {x} - \zeta_ {y} = \Pi_ {x} \left(f (x) - \bar {f} (x)\right) + (\bar {\Pi} _ {x} - \Pi_ {x}) \left(\bar {\Gamma} _ {x y} \bar {f} (y) - \bar {f} (x)\right) \\ - \Pi_ {x} \Gamma_ {x y} \left(f (y) - \bar {f} (y)\right) + \Pi_ {x} \left(\bar {\Gamma} _ {x y} - \Gamma_ {x y}\right) \bar {f} (x). \end{array}
$$

It follows at once that one has the bound

$$
\left| \left\langle \zeta_ {x} - \zeta_ {y}, \varphi_ {x} ^ {n, \mathfrak {s}} \right\rangle \right| \lesssim \left(\| f - \bar {f} \| _ {\gamma ; \mathfrak {K}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \mathfrak {K}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma ; \mathfrak {K}}\right) 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \alpha n}.
$$

Combining this with (3.37) and making use of the bound a$\wedge b \leq a ^ { \kappa } b ^ { 1 - \kappa }$ which is valid for any two positive numbers a and b, we have

$$
\begin{array}{r l} & {\left| \left\langle \zeta_ {x} - \zeta_ {y}, \varphi_ {x} ^ {n, \mathfrak {s}} \right\rangle \right| \lesssim \big (\| f - \bar {f} \| _ {\gamma ; \mathfrak {K}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \mathfrak {K}}} \\ & {\qquad + \| \Gamma - \bar {\Gamma} \| _ {\gamma ; \mathfrak {K}} \big) ^ {\kappa} \| x - y \| _ {\mathfrak {s}} ^ {\bar {\Gamma} - \alpha} 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \alpha n},} \end{array}
$$

from which the claimed bound follows.

We now prove the claim for$\gamma \le 0$. It is clear that in this case$\mathcal { R }$cannot be unique since, if$\mathcal { R } f$satisfies (3.3) and$\xi \in \mathcal { C } _ { \mathfrak { s } } ^ { \gamma }$, then$\mathcal { R } f + \xi$does again satisfy (3.3). Still, the existence of Rf is not completely trivial in general since $\Pi _ { x } f ( x )$itself only belongs to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$and one can have$\alpha < \gamma \leq 0$in general. It turns out that one very simple choice for$\mathcal { R } f$is given by

$$
\mathcal {R} f = \sum_ {n \geq 0} \sum_ {x \in \Lambda_ {\mathfrak {s}} ^ {n}} \sum_ {\psi \in \Psi} \left\langle \Pi_ {x} f (x), \psi_ {x} ^ {n, \mathfrak {s}} \right\rangle \psi_ {x} ^ {n, \mathfrak {s}} + \sum_ {x \in \Lambda_ {\mathfrak {s}} ^ {0}} \left\langle \Pi_ {x} f (x), \varphi_ {x} ^ {0, \mathfrak {s}} \right\rangle \varphi_ {x} ^ {0, \mathfrak {s}}.\tag{3.38}
$$

This is obviously not canonical: different choices for our multiresolution analysis yield different definitions for$\mathcal { R }$. However, it has the advantage ofnot relying at all on the axiom of choice, which was used in [81] to prove a similar result in the one-dimensional case. Furthermore, it has the additional property that if f is “constant” in the sense that$f ( x ) = \Gamma _ { x y } f ( y )$for any two points x and y, then one has the identity

$$
\mathcal {R} f = \Pi_ {x} f (x),\tag{3.39}
$$

where the right hand side is independent of x by assumption. (This wouldn’t be the case if the second term in (3.38) were absent.) Actually, our construction is related in spirit to the one given in [97], but it has the advantage of being very straightforward to analyse.

For$\mathcal { R } f$as in (3.38), it remains to show that (3.3) holds. Note first that the second part of (3.38) defines a smooth function, so that we can discard it. To bound the remainder, let$\eta$be a suitable test function and note that one has the bounds

$$
\left| \left\langle \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta , \psi_ {y} ^ {n, \mathfrak {s}} \right\rangle \right| \lesssim \left\{ \begin{array}{l l} 2 ^ {- n \frac {| \mathfrak {s} |}{2} - r n} \delta^ {- | \mathfrak {s} | - r} & \text { if } 2 ^ {- n} \leq \delta , \\ 2 ^ {n \frac {| \mathfrak {s} |}{2}} & \text { otherwise }. \end{array} \right.
$$

Furthermore, one has of course$\langle S _ { \mathfrak { s } , x } ^ { \delta } \eta , \psi _ { y } ^ { n , \mathfrak { s } } \rangle = 0$unless$\| x - y \| _ { \mathfrak { s } } \lesssim \delta + 2 ^ { - n }$ It also follows immediately from the definition (3.38) that one has the bound

$$
\begin{array}{l} \Big | (\mathcal {R} f - \Pi_ {x} f (x))   (\psi_ {y} ^ {n, \mathfrak {s}}) \Big | = \Big | \big (\Pi_ {y} f (y) - \Pi_ {x} f (x) \big)   (\psi_ {y} ^ {n, \mathfrak {s}}) \Big | \\ = \Big | \Pi_ {y} \left(f (y) - \Gamma_ {y x} f (x)\right) (\psi_ {y} ^ {n, \mathfrak {s}}) \Big | \\ \lesssim \sum_ {\beta <   \gamma} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \beta} 2 ^ {- n \frac {| \mathfrak {s} |}{2} - \beta n}, \end{array}
$$

where the proportionality constant is as in (3.3). These bounds are now inserted into the identity

$$
\begin{array}{r l} & {(\mathcal {R} f - \Pi_ {x} f (x)) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta) = \sum_ {n > 0} \sum_ {y \in \Lambda_ {\mathfrak {s}} ^ {n}} \sum_ {\psi \in \Psi} (\mathcal {R} f - \Pi_ {x} f (x)) (\psi_ {y} ^ {n, \mathfrak {s}})} \\ & {\qquad \times \left\langle \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta , \psi_ {y} ^ {n, \mathfrak {s}} \right\rangle .} \end{array}
$$

For the terms with$2 ^ { - n } \leq \delta$, we thus obtain a contribution of the order

$$
\delta^ {| \mathfrak {s} |} \sum_ {2 ^ {- n} \leq \delta} 2 ^ {n | \mathfrak {s} |} \sum_ {\beta <   \gamma} \delta^ {\gamma - \beta} 2 ^ {- n \frac {| \mathfrak {s} |}{2} - \beta n} 2 ^ {- n \frac {| \mathfrak {s} |}{2} - r n} \delta^ {- | \mathfrak {s} | - r} \lesssim \delta^ {\gamma}.
$$

Here, the bound follows from the fact that we have chosen r such that$r > | \gamma |$ and the factor$\delta ^ { \vert \mathfrak { s } \vert } 2 ^ { n \vert \mathfrak { s } \vert }$counts the number of non-zero terms appearing in the sum over y. For the terms with$2 ^ { - n } > \delta$, we similarly obtain a contribution of

$$
\sum_ {2 ^ {- n} > \delta} \sum_ {\beta <   \gamma} \delta^ {\gamma - \beta} 2 ^ {- n \frac {| \mathfrak {s} |}{2} - \beta n} 2 ^ {n \frac {| \mathfrak {s} |}{2}} \lesssim \delta^ {\gamma},
$$

where we used the fact that$\beta < \gamma \leq 0$. The claim then follows at once.

Remark 3.27 Recall that in Proposition 3.25, the bound on$f - \zeta _ { x }$depends on $K _ { 1 }$but not on$K _ { 2 }$. This shows that in the reconstruction theorem, the bound on ${ \mathcal R f } { - } \Pi _ { x } f ( x )$only depends on the second part ofthe definition of$f \| _ { \gamma ; \mathbb { A } }$. This remark will be important when dealing with singular modelled distributions in Sect. 6 below.

## 3.4 The reconstruction theorem for functions

A very important special case is given by the situation in which$\mathcal { T }$contains a copy of the canonical regularity structure$\mathcal { T } _ { d , \mathfrak { s } }$(write$\bar { T } \subset T$for the model space associated to the abstract polynomials) as in Remark 2.23, and where the model ( , ) we consider yields the canonical polynomial model when restricted to$\bar { T }$. We consider the particular case of the reconstruction theorem applied to elements$f \in { \mathcal { D } } ^ { \gamma } ( V )$, where V is a sector of regularity 0, but such that

$$
V \subset \bar {T} + T _ {\alpha} ^ {+},\tag{3.40}
$$

for some$\alpha \in ( 0 , \gamma )$. Loosely speaking, this states that the elements of the model used to describe$\mathcal { R } f$consist only of polynomials and of functions that are Hölder regular of order α or more.

This is made more precise by the following result:

Proposition 3.28 Let$f \in { \mathcal { D } } ^ { \gamma } ( V )$, where V is a sector as in (3.40). Then,$\mathcal { R } f$ coincides with thefunction given by

$$
\mathcal {R} f (x) = \langle \mathbf {1}, f (x) \rangle ,\tag{3.41}
$$

and one has$\mathcal { R } f \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$

Proof The fact that the function$x \mapsto \langle \mathbf { 1 } , f ( x ) \rangle$belongs to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$is an immediate consequence of the definitions and the fact that the projection of$f$onto$\bar { T }$ belongs to$\mathcal { D } ^ { \alpha }$. It follows immediately that one has

$$
\int_ {\mathbf {R} ^ {d}} (\mathcal {R} f (x) - \langle \mathbf {1}, f (x) \rangle)   \psi_ {y} ^ {\lambda} (x)   d x \lesssim \lambda^ {\alpha},
$$

from which, by the uniqueness of the reconstruction operator, we deduce that one does indeed have the identity (3.41).□

Another useful fact is the following result showing that once we know that $f \in \mathcal { D } ^ { \gamma }$for some$\gamma > 0$, the components of f in$\hat { T } _ { k }$for$0 < k < \gamma$are uniquely determined by the knowledge of the remaining components. More precisely, we have

Proposition 3.29 If$f , g \in \mathcal { D } ^ { \gamma }$with$\gamma ~ > ~ 0$are such that$f ( x ) - g ( x ) \in$ $\oplus _ { 0 < k < \gamma } \bar { T } _ { k }$, then$f = g$

Proof Setting$\begin{array} { r } { h \ = \ f - \ g } \end{array}$, one has$\mathcal { R } h \ = \ 0$from the uniqueness of the reconstruction operator. The fact that this implies that$h = 0$was already shown in Remark 2.16.□

Remark 3.30 In full generality, it is not true that h is completely determined by the knowledge of$\mathcal { R } h$. Actually, whether such a determinacy holds or not depends on the intricate details of the particular model ( , ) that is being considered. However, for models that are built in a “natural” way from a sufficiently non-degenerate Gaussian process, it does tend to be the case that Rh fully determines h. See [68] for more details in the particular case of rough paths.

## 3.5 Consequences of the reconstruction theorem

To conclude this section, we provide a few very useful consequences of the reconstruction theorem which shed some light on the interplay between and . First, we show that for$\alpha > 0$, the action of$\Pi _ { x }$on$T _ { \alpha }$is completely determined by$\Gamma$. In a way, one can interpret this result as a generalisation of [82, Theorem 2.2.1].

Proposition 3.31 Let$\mathcal { T }$be a regularity structure, let$\alpha > 0$, and let ( , ) be a model for$\mathcal { T }$over$\mathbf { R } ^ { d }$with scaling s. Then, the action of on$T _ { \alpha }$is completely determined by the action of on$T _ { \alpha } ^ { - }$and the action of  on$T _ { \alpha }$. Furthermore, one has the bound

$$
\sup_{x\in \mathfrak{K}}\sup_{\delta <  1}\sup_{\varphi \in \mathcal{B}_{\mathfrak{s},0}^{r}}\sup_{\substack{a\in T_{\alpha}\\ \| a\| \leq 1}}\delta^{-\alpha}|(\Pi_{x}a)(\mathcal{S}_{\mathfrak{s},x}^{\delta}\varphi)|\leq \| \Pi \|_{\alpha ;\bar{\mathfrak{K}}}\| \Gamma \|_{\alpha ;\bar{\mathfrak{K}}},\tag{3.42}
$$

where$\bar { \mathbf { x } }$denotes the 1-fattening of$\mathscr { k }$as before and$r > | \operatorname* { m i n } A | . I f ( { \bar { \Pi } } , { \bar { \Gamma } } )$ is a second model for the same regularity structure, one furthermore has the bound

$$
\begin{array}{l} \sup _ {x \in \mathfrak {K} \delta ; \varphi ; a} \sup \delta^ {- \alpha} | (\Pi_ {x} a - \bar {\Pi} _ {x} a) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \varphi) | \leq \| \Pi - \bar {\Pi} \| _ {\alpha ; \bar {\mathfrak {K}}} \left(\| \Gamma \| _ {\alpha ; \bar {\mathfrak {K}}} + \| \Gamma \| _ {\alpha ; \bar {\mathfrak {K}}}\right) \\ + \| \Gamma - \bar {\Gamma} \| _ {\alpha ; \bar {\mathfrak {K}}} \left(\| \Pi \| _ {\alpha ; \bar {\mathfrak {K}}} + \| \bar {\Pi} \| _ {\alpha ; \bar {\mathfrak {K}}}\right), \end{array} \tag {3.43}
$$

where the supremum runs over the same set as in (3.42).

Proof For any$a \in T _ { \alpha }$and$x \in \mathbf { R } ^ { d }$, we define a function$f _ { a , x } \colon \mathbf { R } ^ { d } \to T _ { \alpha } ^ { - }$by

$$
f _ {a, x} (y) = \Gamma_ {y x} a - a.\tag{3.44}
$$

It follows immediately from the definitions that$f _ { a , x } \in \mathcal { D } ^ { \alpha }$and that, uniformly over all$a$with$\| a \| ~ \leq ~ 1$, its norm over any domain K is bounded by the corresponding norm of . Indeed, we have the identity

$$
\begin{array}{c} \Gamma_ {y z} f _ {a, x} (z) - f _ {a, x} (y) = \left(\Gamma_ {y x} a - \Gamma_ {y z} a\right) - \left(\Gamma_ {y x} a - a\right) \\ = a - \Gamma_ {y z} a, \end{array}
$$

so that the required bound follows from Definition 2.17.

We claim that one then has$\Pi _ { x } a \ : = \ : { \mathcal R } f _ { a , x }$, which depends only on the action of on$T _ { \alpha } ^ { - }$. This follows from the fact that, for every$\boldsymbol { y } \in \mathbf { R } ^ { d }$, one has $\Pi _ { x } a = \Pi _ { y } \Gamma _ { y x } a$, so that

$$
\begin{array}{l} \left(\Pi_ {x} a - \Pi_ {y} f _ {a, x} (y)\right) (\mathcal {S} _ {\mathfrak {s}, y} ^ {\lambda} \eta) = \left(\Pi_ {y} a\right) (\mathcal {S} _ {\mathfrak {s}, y} ^ {\lambda} \eta) \lesssim \lambda^ {\alpha} \| \Pi \| _ {\alpha ; \bar {\mathfrak {K}}} \| f _ {a, x} \| _ {\alpha ; \bar {\mathfrak {K}}} \\ \leq \lambda^ {\alpha} \| \Pi \| _ {\alpha ; \bar {\mathfrak {K}}} \| \Gamma \| _ {\alpha ; \bar {\mathfrak {K}}}, \end{array} \tag {3.4}\tag{3.45}
$$

for all suitable test functions η. The claim now follows from the uniqueness part of the reconstruction theorem. Furthermore, the bound (3.42) is a consequence of (3.45) with$y = x$, noting that$f _ { a , x } ( x ) = 0$

It remains to obtain the bound (3.43). For this, we consider two models as in the statement, and we set$\bar { f } _ { a , x } ( y ) = \bar { \Gamma } _ { y x } a - a$, We then apply the generalised version of the reconstruction theorem, Proposition 3.25, noting that we are exactly in the situation that it covers, with$\zeta _ { y } = \Pi _ { y } f _ { a , x } ( y ) - \bar { \Pi } _ { y } \bar { f } _ { a , x } ( y )$. We then have the identity

$$
\begin{array}{r l} & {\zeta_ {y} - \zeta_ {z} = \left(\Pi_ {y} (\Gamma_ {y x} - I) - \bar {\Pi} _ {y} (\bar {\Gamma} _ {y x} - I)\right) a - \left(\Pi_ {z} (\Gamma_ {z x} - I) - \bar {\Pi} _ {z} (\bar {\Gamma} _ {z x} - I)\right) a} \\ & {\qquad = \Pi_ {y} (\Gamma_ {y z} - I) a - \bar {\Pi} _ {y} (\bar {\Gamma} _ {y z} - I) a} \\ & {\qquad = (\Pi_ {y} - \bar {\Pi} _ {y}) (\Gamma_ {y z} - I) a + \bar {\Pi} _ {y} (\Gamma_ {y z} - \bar {\Gamma} _ {y z}) a.} \end{array}
$$

It follows that one has the bound

$$
\begin{array}{c} 2 ^ {\frac {n | \mathfrak {s} |}{2}} \left\langle \zeta_ {y} - \zeta_ {z}, \varphi_ {y} ^ {n, \mathfrak {s}} \right\rangle \leq \| \Pi - \bar {\Pi} \| _ {\alpha ; \bar {\mathfrak {K}}} \| \Gamma \| _ {\alpha ; \bar {\mathfrak {K}}} \sum_ {\beta <   \alpha} \| y - z \| _ {\mathfrak {s}} ^ {\alpha - \beta} 2 ^ {- \beta n} \\ + \| \Gamma - \bar {\Gamma} \| _ {\alpha ; \bar {\mathfrak {K}}} \| \bar {\Pi} \| _ {\alpha ; \bar {\mathfrak {K}}} \sum_ {\beta <   \alpha} \| y - z \| _ {\mathfrak {s}} ^ {\alpha - \beta} 2 ^ {- \beta n}, \end{array}
$$

where, in both instances, the sum runs over elements in A. Since we only need to consider pairs$( y , z )$such that$\| y - z \| _ { \mathfrak { s } } \geq 2 ^ { - n }$, this does imply the bound (3.30) with the desired constants, so that the claim follows from Proposition 3.25.□

Another consequence of the reconstruction theorem is that, in order to characterise a model ( , ) on some sector$V \subset T$, it suffices to know the action of$\Gamma _ { x y }$on$V .$, as well as the values of$( \Pi _ { x } a ) ( \varphi _ { x } ^ { n , 5 } )$for$a \in V , x \in \Lambda _ { \mathfrak { s } } ^ { n }$and$\varphi$ the scaling function of some fixed sufficiently regular multiresolution analysis as in Sect. 3.1. More precisely, we have:

Proposition 3.32 A model ( , ) for a given regularity structure is completely determined by the knowledge of$( \Pi _ { x } a ) ( \varphi _ { x } ^ { n , 5 } )$for$x \in \Lambda _ { \mathfrak { s } } ^ { n }$and$n \geq 0$ as well as$\Gamma _ { x y } a f o r x , y \in \mathbf { R } ^ { d }$

Furthermore, for every compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$and every sector V, one has the bound

$$
\| \Pi \| _ {V; \mathfrak {K}} \lesssim \left(1 + \| \Gamma \| _ {V; \mathfrak {K}}\right) \sup _ {\alpha \in A _ {V}} \sup _ {a \in V _ {\alpha}} \sup _ {n \geq 0} \sup _ {x \in \Lambda_ {\mathfrak {s}} ^ {n} (\bar {\mathfrak {K}})} 2 ^ {\alpha n + \frac {n | \mathfrak {s} |}{2}} \frac {\left| (\Pi_ {x} a) (\varphi_ {x} ^ {n , \mathfrak {s}}) \right|}{\| a \|}.\tag{3.46}
$$

Here, we denote by$\| \Pi \| _ { V ; \mathcal { R } }$the norm given as in Definition 2.17, but where we restrict ourselves to vectors$a \in V$. Finally,for any two models ( , ) and

( ,¯ )¯ , one has

$$
\begin{array}{l} \| \Pi - \bar {\Pi} \| _ {V; \mathfrak {K}} \lesssim \big (1 + \| \Gamma \| _ {V; \mathfrak {K}} \big) \\ \qquad \times \sup _ {\alpha \in A _ {V}} \sup _ {a \in V _ {\alpha}} \sup _ {n \geq 0} \sup _ {x \in \Lambda_ {\mathfrak {s}} ^ {n} (\bar {\mathfrak {K}})} 2 ^ {\alpha n + \frac {n | \mathfrak {s} |}{2}} \frac {\big | \big (\Pi_ {x} a - \bar {\Pi} _ {x} a \big) (\varphi_ {x} ^ {n , \mathfrak {s}}) \big |}{\| a \|}. \end{array}
$$

Proof Given$a \ \in \ V _ { \alpha }$and$x \in \mathbf { R } ^ { d }$, we define similarly to above a function $f _ { x } ^ { a } \colon { \mathbf { R } } ^ { d } \to V$by$f _ { x } ^ { a } ( y ) = \Gamma _ { y x } a$. (This time α can be arbitrary though.) One then has$\Pi _ { y } f _ { x } ^ { a } ( y ) = \Pi _ { y } \Gamma _ { y x } a = \Pi _ { x } a$, so that${ \mathcal R f } _ { x } ^ { a } = \Pi _ { x } a$. On the other hand, the proof of the reconstruction theorem only makes use of the values $( \Pi _ { x } a ) ( \varphi _ { x } ^ { n , 5 } )$and the function$( x , y ) \mapsto \Gamma _ { x y }$, so that the claim follows.

The bound (3.46), as well as the corresponding bound on$\Pi - \bar { \Pi }$are an immediate consequence of Theorem 3.23, noting again that the coefficients $A _ { x } ^ { n }$only involve evaluations of$( \Pi _ { x } a ) ( \varphi _ { x } ^ { n , 5 } )$and the map$\Gamma _ { x y }$□

Although this result was very straightforward to prove, it is very important when constructing random models for a regularity structure. Indeed, provided that one has suitable moment estimates, it is in many cases possible to show that the right hand side of (3.46) is bounded almost surely. One can then make use of this knowledge to define the distribution$\Pi _ { x } a$by$\mathcal { R } f _ { x } ^ { a }$via the reconstruction theorem. This is completely analogous to Kolmogorov’s continuity criterion where the knowledge of a random function on a dense countable subset of$\mathbf { R } ^ { d }$ is sufficient to define a random variable on the space of continuous functions on$\mathbf { R } ^ { d }$as a consequence of suitable moment bounds. Actually, the standard proof of Kolmogorov’s continuity criterion is very similar in spirit to the proof given here, since it also relies on the hierarchical approximation of points in $\mathbf { R } ^ { d }$by points with dyadic coordinates, see for example [91].

## 3.6 Symmetries

It will often be useful to consider modelled distributions that, although they are defined on all of$\mathbf { R } ^ { d }$, are known to obey certain symmetries. Although the extension of the framework to such a situation is completely straightforward, we perform it here mostly in order to introduce the relevant notation which will be used later.

Consider some discrete symmetry group$\mathcal { S }$which acts on$\mathbf { R } ^ { d }$via isometries $T _ { g }$. In other words, for every$g \in \mathcal { S } , T _ { g }$is an isometry of$\mathbf { R } ^ { d }$and$T _ { g \bar { G } } = T _ { g } \circ T _ { \bar { G } }$ Given a regularity structure$\mathcal { T }$, we call a map$M \colon \mathcal { S }  L ^ { 0 }$(where$L ^ { 0 }$is as in Sect. 2.4) an action of$\mathcal { S }$on$\mathcal { T }$if$M _ { g } \in$Aut$\mathcal { T }$for every$g \in \mathcal { S }$and furthermore one has the identity$M _ { g \bar { G } } = M _ { \bar { G } } \circ M _ { g }$for any two elements $g , { \bar { G } } \in { \mathcal { S } }$. Note that$\mathcal { S }$also acts naturally on any space of functions on$\mathbf { R } ^ { d }$

via the identity

$$
\left(T _ {g} ^ {\star} \psi\right) (x) = \psi (T _ {g} ^ {- 1} x).
$$

With these notations, the following definition is natural:

Definition 3.33 Let$\mathcal { S }$be a group of symmetries of$\mathbf { R } ^ { d }$acting on some regularity structure$\mathcal { T }$. A model ( , ) for$\mathcal { T }$is said to be adapted to the action of$\mathcal { S }$if the following two properties hold:

For every test function$\psi : \mathbf { R } ^ { d }  \mathbf { R }$, every$x \in \mathbf { R } ^ { d }$, every$a \in T$, and every$g \in \mathcal { S }$, one has the identity$( \Pi _ { T _ { g } x } a ) ( T _ { g } ^ { \star } \psi ) = ( \Pi _ { x } M _ { g } a ) ( \psi )$

For every$x , y \in \mathbf { R } ^ { d }$and every$g \in \mathcal { S }$, one has the identity$M _ { g } \Gamma _ { T _ { g } x T _ { g } y } =$ $\Gamma _ { x y } M _ { g }$

A modelled distribution$f \colon \mathbf { R } ^ { d }  T$is said to be symmetric if$M _ { g } f ( T _ { g } x ) =$ $f ( x )$for every$\boldsymbol { x } \in \mathbf { R } ^ { d }$and every$g \in \mathcal { S }$

Remark 3.34 One could additionally impose that the norms on the spaces$T _ { \alpha }$ are chosen in such a way that the operators$M _ { g }$all have norm 1. This is not essential but makes some expressions nicer.

Remark 3.35 In the particular case where$\mathcal { T }$contains the polynomial regularity structure${ \mathcal { T } } _ { d , \mathfrak { s } }$and ( , ) extends its canonical model, the action$M _ { g }$of $\mathcal { S }$on the abstract element X is necessarily given by$M _ { g } X = A _ { g } X$, where$A _ { g }$ is the$d \times d$matrix such that$T _ { g }$acts on elements of$\mathbf { R } ^ { d }$by$T _ { g } x = A _ { g } x + b _ { g }$ for some vector$b _ { g }$. This can be checked by making use of the first identity in Definition 3.33.

The action on elements of the form$X ^ { k }$for an arbitrary multiindex k is then naturally given by$\begin{array} { r } { M _ { g } ( X ^ { k } ) = ( A _ { g } X ) ^ { k } = \prod _ { i } ( \sum _ { j } A _ { g } ^ { i j } X _ { j } ) ^ { k _ { i } } } \end{array}$

Remark 3.36 One could have relaxed the first property to the identity $( \Pi _ { T _ { g } x } a ) ( T _ { g } ^ { \star } \psi ) = ( - 1 ) ^ { \varepsilon ( g ) } ( \Pi _ { x } M _ { g } a ) ( \psi )$, where$\varepsilon \colon \mathcal { S }  \{ \pm 1 \}$is any group morphism. This would then also allow to treat Dirichlet boundary conditions in domains generated by reflections. We will not consider this for the sake of conciseness.

Remark 3.37 While Definition 3.33 ensures that the model ( , ) behaves “nicely” under the action of$\mathcal { S }$, this does not mean that the distributions$\Pi _ { x }$ themselves are symmetric in the sense that$\Pi _ { x } ( \psi ) = \Pi _ { x } ( T _ { g } ^ { \star } \psi )$. The simplest possible example on which this is already visible is the case where$\mathcal { S }$consists of a subgroup of the translations. If we take$\mathcal { T }$to be the canonical polynomial structure and M to be the trivial action, then it is straightforward to verify that the canonical model ( , ) is indeed adapted to the action of$\mathcal { S }$. Furthermore, $f$being “symmetric” in this case simply means that$f$has a suitable periodicity. However, polynomials themselves of course aren’t periodic.

Our definitions were chosen in such a way that one has the following result.

Proposition 3.38 Let$\mathcal { S }$be as above, acting on$\mathcal { T }$, let$( \Pi , \Gamma )$be adapted to the action$o f { \mathcal { S } } ,$, and let$f \in \mathcal { D } ^ { \gamma }$(for some$\gamma > 0 )$be symmetric. Then, Rf satisfies$( \mathcal { R } f ) ( T _ { g } ^ { \star } \psi ) = ( \mathcal { R } f ) ( \psi )$for every testfunction ψ and every$g \in { \mathcal { S } } .$

Proof Take a smooth compactly supported test function$\varphi$that integrates to 1 and fix an element$g \in \mathcal { S }$. Since$T _ { g }$is an isometry of$\mathbf { R } ^ { d }$, its action is given by$T _ { g } ( x ) = A _ { g } x + b _ { g }$for some orthogonal matrix$A _ { g }$and a vector$b _ { g } \in \mathbf { R } ^ { d }$ We then define$\varphi ^ { g } ( x ) = \varphi ( A _ { g } ^ { - 1 } x )$, which is a test function having the same properties as$\varphi$itself.

One then has the identity

$$
\psi (x) = \lim _ {\lambda \rightarrow 0} \int_ {\mathbf {R} ^ {d}} \left(\mathcal {S} _ {\mathfrak {s}, y} ^ {\lambda} \varphi\right) (x) \psi (y) d y.
$$

Furthermore, this convergence holds not only pointwise, but in every space $\mathcal { C } ^ { k }$. As a consequence of this, combined with the reconstruction theorem, we have

$$
\begin{array}{l} (\mathcal {R} f) (\psi) = \lim _ {\lambda \to 0} \int_ {\mathbf {R} ^ {d}} (\mathcal {R} f) \left(\mathcal {S} _ {\mathfrak {s}, y} ^ {\lambda} \varphi\right) \psi (y) d y = \lim _ {\lambda \to 0} \int_ {\mathbf {R} ^ {d}} \left(\Pi_ {y} f (y)\right) \left(\mathcal {S} _ {\mathfrak {s}, y} ^ {\lambda} \varphi\right) \psi (y) d y \\ = \lim _ {\lambda \to 0} \int_ {\mathbf {R} ^ {d}} \left(\Pi_ {T _ {g} y} M _ {g} ^ {- 1} M _ {g} f (T _ {g} y)\right) \left(T _ {g} ^ {\star} \mathcal {S} _ {\mathfrak {s}, y} ^ {\lambda} \varphi\right) \psi (y) d y \\ = \lim _ {\lambda \to 0} \int_ {\mathbf {R} ^ {d}} \left(\Pi_ {y} f (y)\right) \left(T _ {g} ^ {\star} \mathcal {S} _ {\mathfrak {s}, T _ {g} ^ {- 1} y} ^ {\lambda} \varphi\right) \left(T _ {g} ^ {\star} \psi\right) (y) d y \\ = \lim _ {\lambda \to 0} \int_ {\mathbf {R} ^ {d}} \left(\Pi_ {y} f (y)\right) \left(\mathcal {S} _ {\mathfrak {s}, y} ^ {\lambda} \varphi^ {g}\right) \left(T _ {g} ^ {\star} \psi\right) (y) d y = (\mathcal {R} f) (T _ {g} ^ {\star} \psi), \end{array}
$$

as claimed. Here, we used the symmetry of$f$and the adaptedness of$( \Pi , \Gamma )$ to obtain the second line, while we performed a simple change of variables to obtain the third line.□

One particularly nice situation is that when the fundamental domain$\mathscr { k }$of $\mathcal { S }$is compact in$\mathbf { \dot { R } } ^ { d }$. In this case, provided of course that ( , ) is adapted to the action of$\mathcal { S }$, the analytical bounds (2.15) automatically hold over all of$\mathbf { R } ^ { d }$. The same is true for the bounds (3.1) if$f$is a symmetric modelled distribution.

## 4 Multiplication

So far, our theory was purely descriptive: we have shown that T-valued maps with a suitable regularity property can be used to provide a precise local description of a class of distributions that locally look like a given family of “model distributions”. We now proceed to show that one can perform a number of operations on these modelled distributions, while still retaining their description as elements in some$\mathcal { D } ^ { \gamma }$

The most conceptually non-trivial of such operations is of course the multi-plication of distributions, which we address in this section. Surprisingly, even though elements in$\mathcal { D } ^ { \gamma }$describe distributions that can potentially be extremely irregular, it is possible to work with them largely as if they consisted of continuous functions. In particular, if we are given a product on$T$(see below for precise assumptions on ), then we can multiply modelled distributions by forming the pointwise product

$$
\big (f \star g \big) (x) = f (x) \star g (x),\tag{4.1}
$$

and then projecting the result back to$T _ { \gamma } ^ { - }$for a suitable$\gamma$.

Definition 4.1 A continuous bilinear map$( a , b ) \mapsto a \star b$is a product on T if

For every$a \in T _ { \alpha }$and$b \in T _ { \beta }$, one has$a \star b \in T _ { \alpha + \beta }$

One has 1${ \star a } = a { \star \mathbf { 1 } } = a$for every$a \in T$

Remark 4.2 In all of the situations considered later on, the product will furthermore be associative and commutative. However, these properties do not seem to be essential as far as the abstract theory is concerned.

Remark 4.3 What we mean by “continuous” here is that for any two indices $\alpha , \beta \in A$, the bilinear map$T _ { \alpha } \times T _ { \beta } \to T _ { \alpha + \beta }$is continuous.

Remark 4.4 If$V _ { 1 }$and$V _ { 2 }$are two sectors of$\mathcal { T }$and is defined as a bilinear map on$V _ { 1 } \times V _ { 2 }$, we can always extend it to T by setting$a \star b = 0$if either a belongs to the complement of$V _ { 1 }$or b belongs to the complement of$V _ { 2 }$

Remark 4.5 We could have slightly relaxed the first assumption by allowing $a \star b \in T _ { \alpha + \beta } ^ { + }$. However, the current formulation appears more natural in the +<sub>context of interpreting elements of the spaces</sub>$T _ { \alpha }$as “homogeneous elements”.

Ideally, one would also like to impose the additional property that$\Gamma ( a { \star } b ) =$ $( \Gamma a ) \star ( \Gamma b )$for every$\Gamma \in G$and every a,$b \in T$. Indeed, assume for a moment that$\Pi _ { x }$takes values in some function space and that the operation represents the actual pointwise product between two functions, namely

$$
\Pi_ {x} (a \star b) (y) = (\Pi_ {x} a) (y) (\Pi_ {x} b) (y).\tag{4.2}
$$

In this case, one has the identity

$$
\begin{array}{c} \Pi_ {x} \Gamma_ {x y} (a \star b) = \Pi_ {y} (a \star b) = (\Pi_ {y} a) (\Pi_ {y} b) = (\Pi_ {x} \Gamma_ {x y} a) (\Pi_ {x} \Gamma_ {x y} b) \\ = \Pi_ {x} \bigl (\Gamma_ {x y} a \star \Gamma_ {x y} b \bigr). \end{array}
$$

In many cases considered in this article however, the model space T is either finite-dimensional or, even though it is infinite-dimensional, some truncation still takes place and one cannot expect (4.2) to hold exactly. Instead, the following definition ensures that it holds up to an error which is “of order$\gamma ^ { \ast }$

Definition 4.6 Let$\mathcal { T }$be a regularity structure, let V and W be two sectors of $\mathcal { T }$, and let be a product on$\mathcal { T }$. The pair$( V , W )$is said to be γ -regular if $\Gamma ( a \star b ) = ( \Gamma a ) \star ( \Gamma b )$for every$\Gamma \in G$and for every$a \in V _ { \alpha }$and$b \in W _ { \beta }$ such that$\alpha + \beta < \gamma$and every$\Gamma \in G$

We say that (V, W) is regular if it is γ-regular for every γ. In the case $V = W$, we say that V is (γ -)regular if this is true for the pair$( V , V )$

The aim of this section is to demonstrate that, provided that a pair of sectors is γ -regular for some$\gamma > 0$, the pointwise product between modelled distributions in these sectors yields again a modelled distribution. Throughout this section, we assume that V and W are two sectors of regularities$\alpha _ { 1 }$and $\alpha _ { 2 }$respectively. We then have the following:

Theorem 4.7 Let (V, W) be a pair of sectors with regularities$\alpha _ { 1 }$and$\alpha _ { 2 }$ respectively, let$f _ { 1 } \in { \mathcal { D } } ^ { \gamma _ { 1 } } ( V )$and$f _ { 2 } \in { \mathcal { D } } ^ { \gamma _ { 2 } } ( W )$, and let$\gamma = ( \gamma _ { 1 } + \alpha _ { 2 } ) \wedge$ $( \gamma _ { 2 } + \alpha _ { 1 } )$. Then, provided that (V, W) is γ-regular, one has$f _ { 1 } \star f _ { 2 } \in { \cal D } ^ { \gamma } ( T )$ and,for every compact set${ \mathfrak { R } } ,$the bound

$$
\| f _ {1} \star f _ {2} \| _ {\gamma ; \mathfrak {K}} \lesssim \| f _ {1} \| _ {\gamma_ {1}; \mathfrak {K}} \| f _ {2} \| _ {\gamma_ {2}; \mathfrak {K}} (1 + \| \Gamma \| _ {\gamma_ {1} + \gamma_ {2}; \mathfrak {K}}) ^ {2},
$$

holds for some proportionality constant only depending on the underlying structure$\mathcal { T }$

Remark 4.8 If we denote as before by$\mathcal { D } _ { \alpha } ^ { \gamma }$an element of${ \mathcal { D } } ^ { \gamma } ( V )$for some sector V of regularity α, then Theorem 4.7 can loosely be stated as

$$
f _ {1} \in \mathcal {D} _ {\alpha_ {1}} ^ {\gamma_ {1}} \& f _ {2} \in \mathcal {D} _ {\alpha_ {2}} ^ {\gamma_ {2}} \Rightarrow f _ {1} \star f _ {2} \in \mathcal {D} _ {\alpha} ^ {\gamma},
$$

where$\alpha = \alpha _ { 1 } + \alpha _ { 2 }$and$\gamma = ( \gamma _ { 1 } + \alpha _ { 2 } ) \wedge ( \gamma _ { 2 } + \alpha _ { 1 } )$. This statement appears to be slightly misleading since it completely glosses over the assumption that the pair (V, W) be γ-regular. However, at the expense of possibly extending the regularity structure$\mathcal { T }$and the model ( , ), we will see in Proposition 4.11 below that it is always possible to ensure that this assumption holds, albeit possibly in a non-canonical way.

Remark 4.9 The proof of this result is a rather straightforward consequence of our definitions, combined with standard algebraic manipulations. It has non-trivial consequences mostly when combined with the reconstruction theorem, Theorem 3.10.

ProofofTheorem 4.7 Note first that since we are only interested in showing that$f _ { 1 } \star f _ { 2 } \in \mathcal { D } ^ { \gamma }$, we discard all of the components in$T _ { \gamma } ^ { + }$. (See also Remark 3.2.) As a consequence, we actually consider the function given by

$$
f (x) \stackrel {{\mathrm{def}}} {{=}} \bigl (f _ {1} \star_ {\gamma} f _ {2} \bigr) (x) \stackrel {{\mathrm{def}}} {{=}} \sum_ {m + n <   \gamma} \mathcal {Q} _ {m} f _ {1} (x) \star \mathcal {Q} _ {n} f _ {2} (x).\tag{4.3}
$$

It then follows immediately from the properties of the product that

$$
\| f _ {1} \star_ {\gamma} f _ {2} \| _ {\gamma ; \mathfrak {K}} \lesssim \| f _ {1} \| _ {V; \mathfrak {K}} \| f _ {2} \| _ {W; \mathfrak {K}},
$$

where the proportionality constant depends only on$\gamma$and$\mathcal { T }$, but not on${ \mathcal { \kappa } } .$

From now on we will assume that$f _ { 1 } \| _ { V ; \mathscr { R } } \le 1$and$\| f _ { 2 } \| _ { W ; \mathscr { R } } \leq 1$, which is not a restriction by bilinearity. It remains to obtain a bound on

$$
\Gamma_ {x y} \big (f _ {1} \star_ {\gamma} f _ {2} \big) (y) - \big (f _ {1} \star_ {\gamma} f _ {2} \big) (x).
$$

Using the triangle inequality and recalling that$\mathcal { Q } _ { \ell } ( f _ { 1 } \star _ { \gamma } f _ { 2 } ) = \mathcal { Q } _ { \ell } ( f _ { 1 } \star f _ { 2 } )$ for$\gamma < \ell$, we can write

$$
\begin{array}{l} \| \Gamma_ {x y} f (y) - f (x) \| _ {\ell} \leq \| \Gamma_ {x y} \left(f _ {1} \star_ {\gamma} f _ {2}\right) (y) - \left(\Gamma_ {x y} f _ {1} (y)\right) \star \left(\Gamma_ {x y} f _ {2} (y)\right) \| _ {\ell} \\ + \| \left(\Gamma_ {x y} f _ {1} (y) - f _ {1} (x)\right) \star \left(\Gamma_ {x y} f _ {2} (y) - f _ {2} (x)\right) \| _ {\ell} \\ + \| \left(\Gamma_ {x y} f _ {1} (y) - f _ {1} (x)\right) \star f _ {2} (x) \| _ {\ell} \\ + \| f _ {1} (x) \star \left(\Gamma_ {x y} f _ {2} (y) - f _ {2} (x)\right) \| _ {\ell}. \end{array} \tag {4.4}\tag{4.4}
$$

It follows from (4.3) and the definition of$( V , W )$being γ-regular that for the first term, one has the identity

$$
\begin{array}{l} \Gamma_ {x y} f (y) - \left(\Gamma_ {x y} f _ {1} (y)\right) \star \left(\Gamma_ {x y} f _ {2} (y)\right) \\ = - \sum_ {m + n \geq \gamma} \left(\Gamma_ {x y} \mathcal {Q} _ {m} f _ {1} (y)\right) \star \left(\Gamma_ {x y} \mathcal {Q} _ {n} f _ {2} (y)\right). \end{array}\tag{4.5}
$$

Furthermore, one has

$$
\begin{array}{l} \| \left(\Gamma_ {x y} \mathcal {Q} _ {m} f _ {1} (y)\right) \star \left(\Gamma_ {x y} \mathcal {Q} _ {n} f _ {2} (y)\right) \| _ {\ell} \\ \lesssim \sum_ {\beta_ {1} + \beta_ {2} = \ell} \| \Gamma_ {x y} \mathcal {Q} _ {m} f _ {1} (y) \| _ {\beta_ {1}} \| \Gamma_ {x y} \mathcal {Q} _ {n} f _ {2} (y) \| _ {\beta_ {2}} \\ \lesssim \sum_ {\beta_ {1} + \beta_ {2} = \ell} \| \Gamma \| _ {\gamma_ {1} + \gamma_ {2}; \mathfrak {K}} ^ {2} \| x - y \| _ {\mathfrak {s}} ^ {m + n - \beta_ {1} - \beta_ {2}} \\ \lesssim \| \Gamma \| _ {\gamma_ {1} + \gamma_ {2}; \mathfrak {K}} ^ {2} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \end{array}\tag{4.6}
$$

where we have made use of the facts that$m + n \ge \gamma$and that$\| x - y \| _ { \mathfrak { s } } \leq 1$

It follows from the properties of the product that the second term in (4.4) is bounded by a constant times

$$
\begin{array}{l} \sum_ {\beta_ {1} + \beta_ {2} = \ell} \| \Gamma_ {x y} f _ {1} (y) - f _ {1} (x) \| _ {\beta_ {1}} \| \Gamma_ {x y} f _ {2} (y) - f _ {2} (x) \| _ {\beta_ {2}} \\ \lesssim \sum_ {\beta_ {1} + \beta_ {2} = \ell} \| x - y \| _ {\mathfrak {s}} ^ {\gamma_ {1} - \beta_ {1}} \| x - y \| _ {\mathfrak {s}} ^ {\gamma_ {2} - \beta_ {2}} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma_ {1} + \gamma_ {2} - \ell}. \end{array}
$$

The third term is bounded by a constant times

$$
\begin{array}{c} \sum_ {\beta_ {1} + \beta_ {2} = \ell} \| \Gamma_ {x y} f _ {1} (y) - f _ {1} (x) \| _ {\beta_ {1}} \| f _ {2} (x) \| _ {\beta_ {2}} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma_ {1} - \beta_ {1}} \mathbf {1} _ {\beta_ {2} \geq \alpha_ {2}} \\ \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma_ {1} + \alpha_ {2} - \ell}, \end{array}
$$

where the second inequality uses the identity$\beta _ { 1 } + \beta _ { 2 } = \ell$. The last term is bounded similarly by reversing the roles played by$f _ { 1 }$and$f _ { 2 }$□

In applications, one would also like to have suitable continuity properties of the product as a function of its factors. By bilinearity, it is of course straightforward to obtain bounds of the type

$$
\begin{array}{l} \| f _ {1} \star f _ {2} - g _ {1} \star g _ {2} \| _ {\gamma ; \mathfrak {K}} \lesssim \| f _ {1} - g _ {1} \| _ {\gamma_ {1}; \mathfrak {K}} \| f _ {2} \| _ {\gamma_ {2}; \mathfrak {K}} + \| f _ {2} - g _ {2} \| _ {\gamma_ {2}; \mathfrak {K}} \| g _ {1} \| _ {\gamma_ {1}; \mathfrak {K}}, \\ \| f _ {1} \star f _ {2} - g _ {1} \star g _ {2} \| _ {\gamma ; \mathfrak {K}} \lesssim \| f _ {1} - g _ {1} \| _ {\gamma_ {2}; \mathfrak {K}} \| f _ {2} \| _ {\gamma_ {2}; \mathfrak {K}} + \| f _ {2} - g _ {2} \| _ {\gamma_ {2}; \mathfrak {K}} \| g _ {1} \| _ {\gamma_ {1}; \mathfrak {K}}, \end{array}
$$

provided that both$f _ { i }$and$g _ { i }$belong to$\mathcal { D } ^ { \gamma _ { i } }$with respect to the same model. Note also that as before the proportionality constants implicit in these bounds depend on the size of  in the domain${ \mathcal { \kappa } } .$. However, one has also the following improved bound:

Proposition 4.10 Let (V, W) be as above, let ( , ) and$( \bar { \Pi } , \bar { \Gamma } )$be two models for$\mathcal { T }$, and let$f _ { 1 } \in \mathcal { D } ^ { \gamma _ { 1 } } ( V ; \Gamma ) , f _ { 2 } \in \mathcal { D } ^ { \gamma _ { 2 } } ( W ; \Gamma ) , g _ { 1 } \in \mathcal { D } ^ { \gamma _ { 1 } } ( V ; \bar { \Gamma } )$, and $g _ { 2 } \in \mathcal { D } ^ { \gamma _ { 2 } } ( W ; \bar { \Gamma } )$

Then,for every$C > 0$, one has the bound

$$
\| f _ {1} \star f _ {2}; g _ {1} \star g _ {2} \| _ {\gamma ; \mathfrak {K}} \lesssim \| f _ {1}; g _ {1} \| _ {\gamma_ {1}; \mathfrak {K}} + \| f _ {2}; g _ {2} \| _ {\gamma_ {2}; \mathfrak {K}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma_ {1} + \gamma_ {2}; \mathfrak {K}},
$$

uniformly over all$f _ { i }$and$g _ { i }$with$\begin{array} { r } { \lvert f _ { i } \rvert \lVert _ { \gamma _ { i } ; \mathbb { A } } + \lVert g _ { i } \rVert _ { \gamma _ { i } ; \mathbb { A } } \le C , } \end{array}$, as well as models satisfying$\| \Gamma \| _ { \gamma _ { 1 } + \gamma _ { 2 } ; \mathfrak { R } } + \| \bar { \Gamma } \| _ { \gamma _ { 1 } + \gamma _ { 2 } ; \mathfrak { R } } \leq C$. Here, the proportionality constant depends only on$C$

Proof As before, our aim is to bound the components in$T _ { \ell }$for$\ell < \gamma$of the quantity

$$
f _ {1} (x) \star f _ {2} (x) - g _ {1} (x) \star g _ {2} (x) - \Gamma_ {x y} \bigl (f _ {1} \star_ {\gamma} f _ {2} \bigr) (y) + \bar {\Gamma} _ {x y} \bigl (g _ {1} \star_ {\gamma} g _ {2} \bigr) (y).
$$

First, as in the proof of Theorem 4.7, we would like to replace$\Gamma _ { x y } ( f _ { 1 } \star _ { \gamma } f _ { 2 } ) ( y )$ by$\Gamma _ { x y } f _ { 1 } ( y ) \star \Gamma _ { x y } f _ { 2 } ( y )$and similarly for the corresponding term involving the$g _ { i }$. This can be done just as in (4.6), which yields a bound of the order

$$
\left(\| \Gamma - \bar {\Gamma} \| _ {\gamma_ {1} + \gamma_ {2}; \mathfrak {K}} + \| f _ {1} - g _ {1} \| _ {\gamma_ {1}; \mathfrak {K}} + \| f _ {2} - g _ {2} \| _ {\gamma_ {2}; \mathfrak {K}}\right) \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell},
$$

as required. We rewrite the remainder as

$$
\begin{array}{l} f _ {1} (x) \star f _ {2} (x) - g _ {1} (x) \star g _ {2} (x) - \Gamma_ {x y} f _ {1} (y) \star \Gamma_ {x y} f _ {2} (y) + \bar {\Gamma} _ {x y} g _ {1} (y) \star \bar {\Gamma} _ {x y} g _ {2} (y) \\ = \left(f _ {1} (x) - g _ {1} (x) - \Gamma_ {x y} f _ {1} (y) + \bar {\Gamma} _ {x y} g _ {1} (y)\right) \star f _ {2} (x) \\ \quad + \Gamma_ {x y} f _ {1} (y) \star \left(f _ {2} (x) - g _ {2} (x) - \Gamma_ {x y} f _ {2} (y) + \bar {\Gamma} _ {x y} g _ {2} (y)\right) \\ \quad + \bar {\Gamma} _ {x y} \left(g _ {1} (y) - f _ {1} (y)\right) \star \left(\bar {\Gamma} _ {x y} g _ {2} (y) - g _ {2} (x)\right) \\ \quad + \left(\bar {\Gamma} _ {x y} f _ {1} (y) - \Gamma_ {x y} f _ {1} (y)\right) \star \left(\bar {\Gamma} _ {x y} g _ {2} (y) - g _ {2} (x)\right) \\ \quad + \left(g _ {1} (y) - \bar {\Gamma} _ {x y} g _ {1} (y)\right) \star \left(f _ {2} (x) - g _ {2} (x)\right) \\ \stackrel {{\text { def }}} {{=}} T _ {1} + T _ {2} + T _ {3} + T _ {4} + T _ {5}. \end{array} \tag {4.7}
$$

It follows from the definition of$\| \cdot ; \cdot \| _ { \gamma _ { 1 } ; \mathbb { A } }$that we have the bound

$$
\| T_{1}\|_{\ell}\lesssim \| f_{1};  g_{1}\|_{\gamma_{1};\mathfrak{K}}\sum_{\substack{m + n = \ell \\ m\geq \alpha_{1};n\geq \alpha_{2}}}\| x - y\|_{\mathfrak{s}}^{\gamma_{1} - m}.
$$

(As usual, sums are performed over exponents in A.) Since the largest possible value for m is equal to$\ell - \alpha _ { 2 }$, this is the required bound. A similar bound on $T _ { 2 }$follows in virtually the same way. The term$T _ { 3 }$is bounded by

$$
\| T_{3}\|_{\ell}\lesssim \| f_{1} - g_{1}\|_{\gamma_{1};\mathfrak{K}}\sum_{\substack{m + n = \ell \\ m\geq \alpha_{1};n\geq \alpha_{2}}}\| x - y\|_{\mathfrak{s}}^{\gamma_{2} - n}.
$$

Again, the largest possible value for n is given by$\ell - \alpha _ { 1 }$, so the required bound follows. The bound on$T _ { 4 }$is obtained in a similar way, replacing$\| f _ { 1 } - g _ { 1 } \| _ { \gamma _ { 1 } ; \mathbb { A } }$ by$\| \Gamma - \bar { \Gamma } \| _ { \gamma _ { 1 } ; \mathcal { R } }$. The last term$T _ { 5 }$is very similar to$T _ { 3 }$and can be bounded in the same fashion, thus concluding the proof.□

As already announced earlier, the regularity condition on (V, W) can always be satisfied by possibly extending our regularity structure. However, at this level of generality, the way of extending$\mathcal { T }$and ( , ) can of course not be expected to be canonical! In practice, one would have to identify a “natural” extension, which can potentially require a great deal of effort. Our abstract result however is:

Proposition 4.11 Let$\mathcal { T }$be a regularity structure such that each of the$T _ { \alpha }$is finite-dimensional, let (V, W) be two sectors of$\mathcal { T }$, let ( , ) be a modelfor $\mathcal { T }$, and let$\gamma \in \mathbf { R }$. Then, it is always possible tofind a regularity structure$\bar { \mathcal T }$ containing$\mathcal { T }$and a model$( \bar { \Pi } , \bar { \Gamma } ) \dot { f } o \dot { r } \bar { \mathcal { T } }$extending ( , ), such that the pair $( \iota V , \iota W )$is γ -regular in$\bar { \mathcal T }$

Proof It suffices to consider the situation where there exist α and$\beta$in A such that (V, W) is$( \alpha + \beta )$-regular but isn’t yet defined on$V _ { \alpha }$and$W _ { \beta }$. In such a situation, we build the required extension as follows. First, extend the action of$G$to$T \oplus ( V _ { \alpha } \otimes W _ { \beta } )$by setting

$$
\Gamma (a \otimes b) \stackrel {\mathrm{def}} {=} \Gamma a \bar {\star} \Gamma b, \quad a \in V _ {\alpha}, \quad b \in W _ {\beta}, \quad \Gamma \in G,\tag{4.8}
$$

where$\bar { \star }$is defined on$V _ { \alpha } \times W _ { \beta }$by$a \bar { \star } b = a \otimes b$. (Outside of$V _ { \alpha } \times W _ { \beta }$ we simply set$\bar { \star } = \star . )$Then, consider some linear equivalence relation on $T _ { \alpha + \beta } \oplus ( V _ { \alpha } \otimes W _ { \beta } )$such that

$$
a \sim b \Rightarrow \Gamma a - a = \Gamma b - b \forall \Gamma \in G,\tag{4.9}
$$

and such that no two elements in$T _ { \alpha + \beta }$are equivalent. (Note that the implication only goes from left to right. In particular, it is always possible to take for the trivial relation under which no two distinct elements are equivalent. However, allowing for non-trivial equivalence relations allows to impose additional algebraic properties, like the commutativity of$\bar { \star }$or Leibniz’s rule.) Given such an equivalence relation, we now define$\check { \bar { \mathcal { T } } } = ( \bar { A } , \bar { T } , \bar { G } )$by setting

$$
\bar {A} = A \cup \{\alpha + \beta \}, \quad \bar {T} _ {\alpha + \beta} = \big (T _ {\alpha + \beta} \oplus (V _ {\alpha} \otimes W _ {\beta}) \big) / \sim .
$$

For$\gamma \neq \alpha + \beta$, we simply set$\bar { T } _ { \gamma } = T _ { \gamma }$. Furthermore, we use$\bar { \star }$as the product in$\bar { T }$which, by construction, coincides with , except on$T _ { \alpha } \otimes T _ { \beta }$. Finally, the group$\bar { G }$is identical to$G$as an abstract group, but each element of G is extended to$\bar { T } _ { \alpha + \beta }$in the way described above. Property (4.9) ensures that this is well-defined in the sense that the action of G on different elements of an equivalence class of is compatible.

It remains to extend ( , ) to a model$( \bar { \Pi } , \bar { \Gamma } )$for$\bar { \mathcal T }$as an abstract group element, with its action on$\bar { T }$given by (4.8). For$\bar { \Gamma }$, we simply set$\bar { \Gamma } _ { x y } = \Gamma _ { x y }$ The definition (4.9) then ensures that the bound (2.15) for  also holds for elements in$\bar { T } _ { \alpha + \beta }$. Regarding$\bar { \Pi }$, since$\bar { T } _ { \alpha + \beta }$still contains$T _ { \alpha + \beta }$as a subspace, it remains to define it on some basis of the complement of$T _ { \alpha + \beta }$in$\bar { T } _ { \alpha + \beta }$ For each such basis vector$^ { a , }$, we can then proceed as in Proposition 3.31 to construct$\Pi _ { x } a$for some (and therefore all)$\bar { \boldsymbol { x } } \in  { \mathbf { R } } ^ { d }$. More precisely, we define $\Pi _ { x } a$by$\Pi _ { x } a = \mathcal { R } f _ { a , x }$with$f _ { a , x }$as in (3.44), where R is the reconstruction operator given in the proof of Theorem 3.10. In case$\alpha + \beta \leq 0$, the choice of$\mathcal { R }$is not unique and we explicitly make the choice given in (3.38) for a suitable wavelet basis. This definition then implies for any two points x and$z$ the identity

$$
\begin{array}{r l} & {\Pi_ {z} \Gamma_ {z x} a - \Pi_ {x} a = \Pi_ {z} a - \Pi_ {x} a + \Pi_ {z} (\Gamma_ {z x} a - a)} \\ & {\qquad = \mathcal {R} (f _ {a, z} - f _ {a, x}) + \Pi_ {z} (\Gamma_ {z x} a - a),} \end{array}
$$

where we used the linearity of$\mathcal { R }$. Note now that$\bigl ( f _ { a , z } - f _ { a , x } \bigr ) ( y ) = \Gamma _ { y z } \bigl ( a -$ $\Gamma _ { z x } a )$  , so that we are precisely in the situation of (3.39). This shows that our construction guarantees that$\mathcal { R } \big ( f _ { a , z } - f _ { a , x } \big ) = - \Pi _ { z } \big ( \Gamma _ { z x } a - a \big )$, so that the algebraic identity$\Pi _ { z } \Gamma _ { z x } a = \Pi _ { x } a$  holds for any two points, as required. The required analytical bounds on$\Pi _ { x } a$on the other hand are an immediate consequence of Theorem 3.10.

As a byproduct of our construction and of Proposition 3.31, we see that the extension is essentially unique if$\alpha + \beta > 0$, but that there is considerable freedom whenever$\alpha + \beta \leq 0$□

Remark 4.12 At this stage one might wonder what the meaning of$\mathcal { R } ( f _ { 1 } \star f _ { 2 } )$ is in situations where the distributions$\mathcal { R } f _ { 1 }$and$\mathcal { R } f _ { 2 }$cannot be multiplied in any “classical” sense. In general, this strongly depends on the choice of model and of regularity structure. However, we will see below that in cases where the model was built using a natural renormalisation procedure and the$f _ { i }$are obtained as solutions to some fixed point problem, it is usually possible to interpret$\mathcal { R } ( f _ { 1 } \star f _ { 2 } )$as the weak limit of some (possibly quite non-trivial) expression involving the$f _ { i } ^ { \mathrm { ~ \tiny ~ s ~ } }$

Remark 4.13 In situations where a model happens to consist of continuous functions such that one has indeed$\Pi _ { x } ( a \star b ) ( y ) = { \bigl ( } \Pi _ { x } a { \bigr ) } ( y ) { \bigl ( } \Pi _ { x } b { \bigr ) } ( y )$, it follows from Remark 3.15 that one has the identity$\mathcal { R } ( f _ { 1 } \star f _ { 2 } ) = \mathcal { R } f _ { 1 } \mathcal { R } f _ { 2 }$ In some situations, it may thus happen that there are natural approximating models and approximating functions such that$\begin{array} { r } { \mathcal { R } f _ { 1 } = \operatorname* { l i m } _ { \varepsilon \to 0 } \mathcal { R } _ { \varepsilon } f _ { 1 ; \varepsilon } } \end{array}$(and similarly for$f _ { 2 } )$and$\begin{array} { r } { \mathcal { R } ( f _ { 1 } \star f _ { 2 } ) = \operatorname* { l i m } _ { \varepsilon \to 0 } ( \mathcal { R } _ { \varepsilon } f _ { 1 ; \varepsilon } ) ( \mathcal { R } _ { \varepsilon } f _ { 2 ; \varepsilon } ) } \end{array}$. See for example Sect. 4.4, as well as [28,44].

However, this need not always be the case. As we have already seen in Sect. 2.4, the formalism is sufficiently flexible to allow for products that encode some renormalisation procedure, which is actually the main purpose of this theory.

## 4.1 Classical multiplication

We are now able to give a rather straightforward application of this theory, which can be seen as a multidimensional analogue of Young integration. In the case of the Euclidean scaling, this result is of course well-known, see for example [6].

Proposition 4.14 For α,$\beta \in \mathbf { R }$, the map$( f , g ) \mapsto f \cdot g$extends to a continuous bilinear map from$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha } ( \mathbf { R } ^ { d } ) \times \mathcal { C } _ { \mathfrak { s } } ^ { \beta } ( \mathbf { R } ^ { d } )$to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha \wedge \beta } ( \mathbf { R } ^ { d } )$if$\alpha + \beta > 0 .$ Furthermore, ifα$\notin \mathbf { N } ,$, then this condition is also necessary.

Remark 4.15 More precisely, if$\mathscr { k }$is a compact subset of$\mathbf { R } ^ { d }$and$\bar { \mathbf { x } }$its 1- fattening, then there exists a constant$C$such that

$$
\| f \cdot g \| _ {(\alpha \wedge \beta); \mathfrak {K}} \leq C \| f \| _ {\alpha ; \bar {\mathfrak {K}}} \| g \| _ {\beta ; \bar {\mathfrak {K}}},\tag{4.10}
$$

for any two smooth functions$f$and$g$.

Proof The necessity of the condition$\alpha + \beta > 0$is straightforward. Fixing a compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$and assuming that$\alpha + \beta \le 0$(or the corresponding strict inequality for integer values), it suffices to exhibit a sequence of$\mathcal { C } ^ { r }$ functions$f _ { n } , g _ { n } \in \mathcal { C } ( \mathcal { R } )$(with$r > \operatorname* { m a x } \{ | \alpha | , | \beta | \} )$such that$\{ f _ { n } \}$is bounded in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha } ( \mathfrak { s } ) , g _ { n }$is bounded in$\mathcal { C } _ { \mathfrak { s } } ^ { \beta } ( \mathfrak { s } )$, and$\langle f _ { n } , g _ { n } \rangle \to \infty$, where$\langle \cdot , \cdot \rangle$denotes the usual$L ^ { 2 }$-scalar product. This is because, since$f _ { n }$and$g _ { n }$are supported in ${ \mathcal { \ R } } .$, one can easily find a smooth compactly supported test function$\varphi$such that $\langle f _ { n } , g _ { n } \rangle = \langle \varphi , f _ { n } g _ { n } \rangle$

A straightforward modification of [83, Thm 6.5] shows that the characterisation of Proposition 3.20 for$f \in \mathcal { C } ( \mathcal { \mathbb { R } } )$to belong to$\mathcal { C } _ { s } ^ { \alpha }$is also valid for $\alpha \in \mathbf { R } _ { + } \setminus \mathbf { N }$(since$f$is compactly supported, there are no boundary effects). The required counterexample can then easily be constructed by setting for example

$$
f _ {n} = \sum_ {k = 0} ^ {n} \frac {1}{\sqrt {k}} \sum_ {x \in \Lambda_ {k} ^ {\mathfrak {s}} \cap \bar {\mathfrak {K}}} 2 ^ {- k \frac {| \mathfrak {s} |}{2} - \alpha k} \psi_ {x} ^ {k, \mathfrak {s}},
$$

and similarly for$g _ { n }$with α replaced by$\beta .$. Here,${ \bar { \mathcal { R } } } \subset { \mathcal { R } }$is such that the support of each of the$\psi _ { x } ^ { k , \mathfrak { s } }$is indeed in${ \mathcal { \kappa } } .$. (One may have to start the sum from some $k _ { 0 } > 0 . )$Noting that$\begin{array} { r } { \operatorname* { l i m } _ { n  \infty }  f _ { n } , g _ { n }  = \infty } \end{array}$as soon as$\alpha + \beta \leq 0$, this is the required counterexample.

Combining Theorem 4.7 and the reconstruction theorem, Theorem 3.10, we can give a short and elegant proof of the sufficiency of$\alpha + \beta > 0$that no longer makes any reference to wavelet analysis. Assume from now on that $\xi \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$for some$\alpha < 0$and that$f \in \mathcal { C } _ { 5 } ^ { \beta }$for some$\beta > | \alpha |$. By bilinearity, we can also assume without loss of generality that the norms appearing in the right hand side of (4.10) are bounded by 1. We then build a regularity structure$\mathcal { T }$in the following way. For the set A, we take$A = \mathbf { N } \cup ( \mathbf { N } + \alpha )$ For T, we set$T = V \oplus W$, where each of the sectors V and W is a copy of $\mathcal { T } _ { d , \mathfrak { s } }$, the canonical model. We also choose$\Gamma$as in the canonical model, acting simultaneously on each of the two instances.

As before, we denote by$X ^ { k }$the canonical basis vectors in V. We also use the suggestive notation${ } ^ { \mathfrak { s e } } \Xi X ^ { k ^ { , , } }$for the corresponding basis vector in$W$, but we postulate that$\Xi X ^ { k } \in T _ { \alpha + | k | _ { \mathfrak { s } } }$rather than$\Xi X ^ { k } \in T _ { | k | _ { \mathfrak { s } } }$. With this notation at hand, we also define the product between V and W by the natural identity

$$
\left(\Xi X ^ {k}\right) \star \left(X ^ {\ell}\right) = \Xi X ^ {k + \ell}.
$$

It is straightforward to verify that, with this product, the pair$( V , W )$is regular.

Finally, we define a map$J \colon { \mathcal { C } } _ { 5 } ^ { \alpha } \to { \mathcal { M } } _ { \mathcal { T } }$given by$J : \xi \mapsto ( \Pi ^ { \xi } , \Gamma )$, where is as in the canonical model, while$\Pi ^ { \xi }$acts as

$$
\big (\Pi_ {x} ^ {\xi} X ^ {k} \big) (y) = (y - x) ^ {k}, \qquad \big (\Pi_ {x} ^ {\xi} \Xi X ^ {k} \big) (y) = (y - x) ^ {k} \xi (y),
$$

with the obvious abuse of notation in the second expression. It is then straightforward to verify that$\Pi _ { y } = \Pi _ { x } \circ \Gamma _ { x y }$and that the map J is Lipschitz continuous.

Denote now by$\mathcal { R } ^ { \xi }$the reconstruction map associated to the model$J ( \xi )$ and, for$u \in \mathcal { C } _ { \mathfrak { s } } ^ { \beta }$, denote by$\mathcal { T } _ { \beta } u$as in (2.6) the unique element in${ \mathcal { D } } ^ { \beta } ( V )$such that$\langle \mathbf { 1 } , ( T _ { \beta } u ) ( x ) \rangle = u ( x )$. Note that even though the space${ \mathcal { D } } ^ { \beta } ( V )$does in principle depend on the choice of model, in our situation it is independent of $\xi$for every model$J ( \xi )$. Since, when viewed as a W-valued function, one has $\Xi \in { \mathcal { D } } ^ { \infty } ( W )$, one has${ \mathcal { T } } _ { \beta } u \star \Xi \in { \mathcal { D } } ^ { \alpha + \beta }$by Theorem 4.7. We now consider the map

$$
B (u, \xi) = \mathcal {R} ^ {\xi} \big (\mathcal {T} _ {\beta} u \star \Xi \big).
$$

By Theorem 3.10, combined with the continuity of J, this is a jointly continuous map from$\mathcal { C } _ { \mathfrak { s } } ^ { \beta } \times \mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$into$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$, provided that$\alpha + \beta > 0$. If$\xi$happens to be a smooth function, then it follows immediately from Remark 3.15 that $B ( u , \xi ) = u ( x ) \xi ( x )$, so that B is indeed the requested continuous extension of the product.□

## 4.2 Composition with smooth functions

In general, it makes no sense to compose elements$f \in \mathcal { D } ^ { \gamma }$with arbitrary smooth functions. In the particular case when$f \in { \mathcal { D } } ^ { \gamma } ( V )$for a function-like sector V however, this is possible. Throughout this subsection, we decompose elements$a \in V$as$a = { \bar { A } } \mathbf { 1 } + { \tilde { a } }$, with$\tilde { a } \in \Gamma _ { 0 } ^ { + }$and$\bar { A } = \langle \mathbf { 1 } , a \rangle$. (This notation is suggestive of the fact that a encodes the small-scale fluctuations of$\Pi _ { x } a$near x.) We denote by$\zeta > 0$the smallest non-zero value such that$V _ { \zeta } \neq 0$, so that one actually has$\tilde { a } \in T _ { \zeta } ^ { + }$

Given a function-like sector V and a smooth function$F \colon \mathbf { R } ^ { n }  \mathbf { R }$, we lift $F$to a function${ \hat { F } } \colon V ^ { n } \to V$by setting

$$
\hat {F} (a) = \sum_ {k} \frac {D ^ {k} F (\bar {A})}{k !} \tilde {a} ^ {\star k},\tag{4.11}
$$

where the sum runs over all possible multiindices. Here,$a = ( a _ { 1 } , \ldots , a _ { n } )$ with$a _ { i } ~ \in ~ V$and, for an arbitrary multiindex$k = ( k _ { 1 } , \ldots , k _ { n } )$, we used the shorthand notation

$$
\tilde {a} ^ {\star k} = \tilde {a} _ {1} ^ {\star k _ {1}} \star \dots \star \tilde {a} _ {d} ^ {\star k _ {n}},
$$

with the convention that$\tilde { a } ^ { \star 0 } = 1$

In order for this definition to make any sense, the sector V needs of course to be endowed with a product which also leaves V invariant. In principle, the sum in (4.11) looks infinite, but by the properties of the product , we have$\tilde { a } ^ { \star k } \in T _ { | k | \zeta } ^ { + }$. Since$\zeta$is strictly positive, only finitely many terms in (4.11) contribute at each order of homogeneity, so that${ \hat { F } } ( a )$is well-defined as soon as$F \in { \mathcal { C } } ^ { \infty }$. The main result in this subsection is given by:

Theorem 4.16 Let V be afunction-like sector ofsome regularity structure$\mathcal { T } _ { i }$ let$\zeta > 0$be as above, let$\gamma > 0$, and let$F \in \mathcal { C } ^ { \kappa } ( \mathbf { R } ^ { k } , \mathbf { R } )$for some$\kappa \geq \gamma / \zeta \vee 1$ Assume furthermore that V is γ-regular. Then, for any$f \in { \mathcal { D } } ^ { \gamma } ( V )$, the map $\hat { F } _ { \gamma } ( f )$defined by

$$
\hat {F} _ {\gamma} (f) (x) = \mathcal {Q} _ {\gamma} ^ {-} \hat {F} (f (x)),
$$

again belongs to${ \mathcal { D } } ^ { \gamma } ( V )$. If one furthermore has$F \in \mathcal { C } ^ { \kappa } ( \mathbf { R } ^ { k } , \mathbf { R } )$for$\kappa \geq$ $( \gamma / \zeta \vee 1 ) + 1$, then the map$f \mapsto { \hat { F } } ( f )$is locally Lipschitz continuous in the

sense that one has the bounds

$$
\begin{array}{l} \| \hat {F} _ {\gamma} (f) - \hat {F} _ {\gamma} (g) \| _ {\gamma ; \mathfrak {K}} \lesssim \| f - g \| _ {\gamma ; \mathfrak {K}}, \\ \| \hat {F} _ {\gamma} (f) - \hat {F} _ {\gamma} (g) \| _ {\gamma ; \mathfrak {K}} \lesssim \| f - g \| _ {\gamma ; \mathfrak {K}}, \end{array}\tag{4.12}
$$

for any compact set$\mathcal { R } \subset \mathbb { R } ^ { d } .$, where the proportionality constant in the first bound is uniform over all f, g with$\| f \| _ { \gamma ; \mathscr { R } } + \| g \| _ { \gamma ; \mathscr { R } } \leq C$, while in the second bound it is uniform over all f, g with$f \| _ { \gamma ; \mathbb { A } } + \| g \| _ { \gamma ; \mathbb { A } } \leq C$, for any fixed constant C. We furthermore performed a slight abuse of notation by writing again$\| f \| _ { \gamma ; \mathbb { A } }$(for example) instead of$\begin{array} { r } { \sum _ { i \leq n } \| f _ { i } \| _ { \gamma ; \mathscr { R } } . } \end{array}$

Proof From now on we redefine$\zeta$so that$\zeta = \gamma$in the case when A contains no index between 0 and$\gamma$. In this case, our original condition$\kappa \geq \gamma / \zeta \vee 1$ reads simply as$\kappa \geq \gamma / \zeta$

Let$L = \lfloor \gamma / \zeta \rfloor$, which is the length of the largest multiindex appearing in (4.11) which still yields a contribution to$T _ { \gamma } ^ { - }$. Writing$b ( x ) = \bar { \mathcal { Q } } _ { \gamma } ^ { - } \hat { F } \big ( f ( x ) \big )$ we aim to find a bound on$\Gamma _ { y x } b ( x ) - b ( y )$ . It follows from a straightforward generalisation of the computation from Theorem 4.7 that

$$
\begin{array}{l} \Gamma_ {y x} b (x) = \sum_ {| k | \leq L} \frac {D ^ {k} F (\bar {f} (x))}{k !} \Gamma_ {y x} \big (\mathcal {Q} _ {\gamma} ^ {-} \tilde {f} (x) ^ {\star k} \big) \\ = \sum_ {| k | \leq L} \frac {D ^ {k} F (\bar {f} (x))}{k !} \big (\Gamma_ {y x} \tilde {f} (x) \big) ^ {\star k} + R _ {1} (x, y), \end{array}
$$

with a remainder term$R _ { 1 }$such that$\| R _ { 1 } ( x , y ) \| _ { \beta } \lesssim \| x - y \| _ { \mathfrak { s } } ^ { \gamma - \beta }$, for all$\beta < \gamma$ Since$\Gamma _ { y x } \mathbf { 1 } = \mathbf { 1 }$, we can furthermore write

$$
\Gamma_ {y x} \tilde {f} (x) = \Gamma_ {y x} f (x) - \bar {f} (x) \mathbf {1} = \tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) \mathbf {1} + R _ {f} (x, y),
$$

where, by the assumption on$f ,$, the remainder term$R _ { f }$again satisfies the bound$\| R _ { f } ( x , y ) \| _ { \beta } \lesssim \| x - y \| _ { \mathfrak { s } } ^ { \gamma - \beta }$for all$\beta < \gamma$. Combining this with the bound we already obtained, we get

$$
\begin{array}{l} \Gamma_ {y x} b (x) = \sum_ {| k | \leq L} \frac {D ^ {k} F (\bar {f} (x))}{k !} \big (\tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) {\bf 1} \big) ^ {\star k} \\ + R _ {2} (x, y), \end{array}\tag{4.13}
$$

with

$$
\| R _ {2} (x, y) \| _ {\beta} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \beta},
$$

for all$\beta < \gamma$as above. We now expand$D ^ { k } F$around$\bar { f } ( y )$, yielding

$$
\begin{array}{l} D ^ {k} F (\bar {f} (x)) = \sum_ {| k + \ell | \leq L} \frac {D ^ {k + \ell} F (\bar {f} (y))}{\ell !} \big (\bar {f} (x) - \bar {f} (y) \big) ^ {\ell} \\ \qquad + \mathcal {O} \big (\| x - y \| _ {\mathfrak {s}} ^ {\gamma - | k | \zeta} \big), \end{array}\tag{4.14}
$$

where we made use of the fact that$| { \bar { f } } ( x ) - { \bar { f } } ( y ) | \lesssim \| x - y \| _ { \mathfrak { s } } ^ { \zeta }$by the definition of$\mathcal { D } ^ { \gamma }$, and the fact that F is$\mathcal { C } ^ { \gamma / \zeta }$by assumption. Similarly, we have the bound

$$
\left\| \left(\tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) \mathbf {1}\right) ^ {\star k} \right\| _ {\beta} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\zeta | k | - \beta},\tag{4.15}
$$

so that, combining this with (4.13) and (4.14), we obtain the identity

$$
\begin{array}{l} \Gamma_ {y x} b (x) = \sum_ {| k + \ell | \leq L} \frac {D ^ {k + \ell} F (\bar {f} (y))}{k ! \ell !} \big (\tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) {\bf 1} \big) ^ {\star k} \\ \times (\bar {f} (x) - \bar {f} (y)) ^ {\ell} + R _ {3} (x, y), \end{array}\tag{4.16}
$$

where$R _ { 3 }$is again a remainder term satisfying the bound

$$
\| R _ {3} (x, y) \| _ {\beta} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \beta}.\tag{4.17}
$$

Using the generalised binomial identity, we have

$$
\sum_ {k + \ell = m} \frac {1}{k ! \ell !} \big (\tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) \mathbf {1} \big) ^ {\star k} (\bar {f} (x) - \bar {f} (y)) ^ {\ell} = \frac {\tilde {f} (y) ^ {\star m}}{m !},
$$

so that the component in$T _ { \gamma } ^ { - }$of the first term in the right hand side of (4.16) is precisely equal to the component in$T _ { \gamma } ^ { - }$of$b ( y )$. Since the remainder satisfies (4.17), this shows that one does indeed have$b \in { \mathcal { D } } ^ { \gamma } ( V )$

The first bound in (4.12) is immediate from the definition (4.11), as well as the fact that the assumption implies the local Lipschitz continuity of$D ^ { k } F$for every$| k | \leq L$

The second bound is a little more involved. One way of obtaining it is to first define$h = f - g$and to note that one then has the identity

$$
\begin{array}{l} \hat {F} (f (x)) - \hat {F} (g (x)) \\ = \sum_ {k, i} \int_ {0} ^ {1} \frac {D ^ {k + e _ {i}} F (\bar {G} (x) + t \bar {h} (x))}{k !} \big (\tilde {g} (x) + t \tilde {h} (x) \big) ^ {\star k} \bar {h} _ {i} (x) d t \\ + \sum_ {k, i} \int_ {0} ^ {1} \frac {D ^ {k} F (\bar {G} (x) + t \bar {h} (x))}{k !} k _ {i} \big (\tilde {g} (x) + t \tilde {h} (x) \big) ^ {\star (k - e _ {i})} \tilde {h} _ {i} (x) d t \\ = \sum_ {k, i} \int_ {0} ^ {1} \frac {D ^ {k + e _ {i}} F (\bar {G} (x) + t \bar {h} (x))}{k !} \big (\tilde {g} (x) + t \tilde {h} (x) \big) ^ {\star k} h _ {i} (x) d t. \end{array}
$$

Here, k runs over all possible multiindices and i takes the values$1 , \ldots , n$. We used the notation$e _ { i }$for the ith canonical multiindex. Note also that our way of writing the second term makes sense since, whenever$k _ { i } = 0$so that$k - e _ { i }$ isn’t a multiindex anymore, it vanishes thanks to the prefactor$k _ { i }$

From this point on, the calculation is virtually identical to the calculation already performed previously. The main differences are that F appears with one more derivative and that every term always appears with a prefactor h, which is responsible for the bound proportional to$\| h \| _ { \gamma ; \mathscr { R } } .$□

## 4.3 Relation to Hopf algebras

Structures like the one of Definition 4.6 must seem somewhat familiar to the reader used to the formalism of Hopf algebras [95]. Indeed, there are several natural instances of regularity structures that are obtained from a Hopf algebra (see for example Sect. 4.4 below). This will also be useful in the context of the kind of structures arising when solving semilinear PDEs, so let us quickly outline this construction.

Let H be a connected, graded, commutative Hopf algebra with product and a compatible coproduct  so that$\Delta ( f \star g ) = \Delta f \star \Delta g$. We assume that the grading is indexed by$\mathbf { Z } _ { + } ^ { d }$for some$d \geq 1$, so that$\mathcal { H } = \oplus _ { k \in \mathbf { Z } _ { + } ^ { d } } \mathcal { H } _ { k }$, and that each of the$\mathcal { H } _ { k }$is finite-dimensional. The grading is assumed to be compatible with the product structures, meaning that

$$
\star \colon \mathcal {H} _ {k} \otimes \mathcal {H} _ {\ell} \to \mathcal {H} _ {k + \ell}, \quad \Delta \colon \mathcal {H} _ {k} \to \bigoplus_ {\ell + m = k} \mathcal {H} _ {\ell} \otimes \mathcal {H} _ {m}.\tag{4.18}
$$

Furthermore,$\mathcal { H } _ { 0 }$is spanned by the unit 1 (this is the definition of connectedness), the antipode$\mathcal { A }$maps$\mathcal { H } _ { k }$to itself for every$k .$, and the counit$^ { 1 ^ { * } }$is normalised so that$\langle \mathbf { 1 } ^ { * } , \mathbf { 1 } \rangle = 1$

The dual$\mathcal { H } ^ { \star } = \oplus _ { k \in \mathbf { Z } _ { + } ^ { d } } \mathcal { H } _ { k } ^ { * }$is then again a graded Hopf algebra with a product given by the adjoint of$\Delta$and a coproduct$\Delta ^ { \star }$given by the adjoint of . (Note that while is assumed to be commutative, is definitely not in general!) By (4.18), both and$\Delta ^ { \star }$respect the grading of$\mathcal { H } ^ { \star }$. There is a natural action  of$\mathcal { H } ^ { \star }$onto H given by the identity

$$
\left\langle \ell , \Gamma_ {g} f \right\rangle = \left\langle \ell \circ g, f \right\rangle ,\tag{4.19}
$$

valid for all ,$g \in { \mathcal { H } } ^ { \star }$and all$f \in { \mathcal { H } }$. An alternative way of writing this is

$$
\Gamma_ {g} f = (1 \otimes g) \Delta f,\tag{4.20}
$$

where we view$g$as a linear operator from H to R. It follows easily from (4.18) that, if$g$and$f$are homogeneous of degrees$d _ { g }$and$d _ { f }$respectively, then$\Gamma _ { g } f$ is homogeneous of degree$d _ { f } - d _ { g }$, provided that$d _ { f } - d _ { g } \in \mathbf { Z } _ { + } ^ { d }$. If not, then one necessarily has$\Gamma _ { g } f = 0$

Remark 4.17 Another natural action of$\mathcal { H } ^ { \star }$onto$\mathcal { H }$would be given by

$$
\left\langle \ell , \bar {\Gamma} _ {g} f \right\rangle = \left\langle (\mathcal {A} ^ {\star} g) \circ \ell , f \right\rangle ,
$$

where,$\mathcal { A } ^ { \star }$, the adjoint of${ \mathcal { A } } .$is the antipode for$\mathcal { H } ^ { \star }$. Since it is an antihomomorphism, one has indeed the required identity$\bar { \Gamma } _ { g _ { 1 } } \bar { \Gamma } _ { g _ { 2 } } = \bar { \Gamma } _ { g _ { 1 } \circ g _ { 2 } }$

Since we assumed that is commutative, it follows from the Milnor-Moore theorem [84] that$\mathcal { H } ^ { \star }$is the universal enveloping algebra of$P ( \mathcal { H } ^ { \star } )$, the set of primitive elements of$\mathcal { H } ^ { \star }$given by

$$
P (\mathcal {H} ^ {\star}) = \{g \in \mathcal {H} ^ {\star}: \Delta^ {\star} g = \mathbf {1} ^ {\star} \otimes g + g \otimes \mathbf {1} ^ {\star} \}.
$$

Using the fact that the coproduct$\Delta ^ { \star }$is an algebra morphism, it is easy to check that$P ( \mathcal { H } ^ { \star } )$is indeed a Lie algebra with bracket given by$[ g _ { 1 } , g _ { 2 } ] =$ $g _ { 1 } \circ g _ { 2 } - g _ { 2 } \circ g _ { 1 }$. This yields in a natural way a Lie group$G \subset { \mathcal { H } } ^ { \star }$given by $G = \exp ( P ( \mathcal { H } ^ { \star } ) )$. It turns out (see [94]) that this Lie group has the very useful property that

$$
\Delta^ {\star} (g) = g \otimes g, \quad \forall g \in G.
$$

As a consequence, it is straightforward to verify that one has the remarkable identity

$$
\Gamma_ {g} (f _ {1} \star f _ {2}) = (\Gamma_ {g} f _ {1}) \star (\Gamma_ {g} f _ {2}),\tag{4.21}
$$

valid for every$g \in G$. This is nothing but an exact version of the regularity requirement of Definition 4.6! Note also that (4.21) is definitely not true for arbitrary elements$g \in { \mathcal { H } } ^ { \star }$

All this suggests that a very natural way ofconstructing a regularity structure is from a graded commutative Hopf algebra. The typical set-up will then be to fix scaling exponents$\{ \alpha _ { i } \} _ { i = 1 } ^ { d }$and to write$\begin{array} { r } { \langle \alpha , k \rangle = \sum _ { i = 1 } ^ { d } \alpha _ { i } k _ { 1 } } \end{array}$for any index $k \in \mathbf { Z } _ { + } ^ { d }$. We then set

$$
A = \{\langle \alpha , k \rangle : k \in \mathbf {Z} _ {+} ^ {d} \}, T _ {\gamma} = \bigoplus_ {\langle \alpha , k \rangle = \gamma} \mathcal {H} _ {k}.
$$

With this notation at hand, we have:

Lemma 4.18 In the setting ofthis subsection,$( A , T , G )$is a regularity structure, with G acting on T via . Furthermore, T equipped with the product is regular.

Proof In view of (4.21), the only property that remains to be shown is that $\Gamma _ { g } a - a \in T _ { \gamma } ^ { - }$for$a \in T _ { \gamma }$

It is easy to show that$P ( \mathcal { H } ^ { \star } )$has a basis consisting of homogeneous elements and that these belong to$\mathcal { H } _ { k } ^ { \star }$for some$k \neq 0 .$. (Since$\Delta ^ { \star } \mathbf { 1 ^ { \star } } = \mathbf { 1 ^ { \star } } \otimes \mathbf { 1 ^ { \star } } . )$ As a consequence, for$a \in T _ { \gamma } , g ^ {  } \in P ( \mathcal { H } ^ { \star } )$, and$n > 0$, we have$\Gamma _ { g ^ { n } } a \in T _ { \beta }$ for some$\beta < \gamma$. Since every element of G is of the form exp(g) for some $g \in P ( \mathcal { H } ^ { \star } )$and since$g \mapsto \Gamma _ { g }$is linear, one has indeed$\Gamma _ { g } a - a \in T _ { \gamma } ^ { - }$□

Remark 4.19 The canonical regularity structure is an example of a regularity structure that can be obtained via this construction. Indeed, a natural dual to the space$\mathcal { H }$of polynomials in d indeterminates is given by the space$\mathcal { H } ^ { \star }$of differential operators over$\mathbf { R } ^ { d }$with constant coefficients, which does itself come with a natural commutative product given by the composition of operators. (Here, the word “differential operator” should be taken in a somewhat loose sense since it consists in general of an infinite power series.) Given such a differential operator$\mathcal { L }$and an (abstract) polynomial$P _ { \mathrm { : } }$, a natural duality pairing $\langle \mathcal { L } , P \rangle$is given by applying$\mathcal { L }$to$P$and evaluating the resulting polynomial at the origin. Somewhat informally, one sets

$$
\langle \mathcal {L}, P \rangle = (\mathcal {L} P) (0).
$$

The action  described in (4.19) is then given by simply applying$\mathcal { L }$to$P$:

$$
\Gamma_ {\mathcal {L}} P = \mathcal {L} P.
$$

It is indeed obvious that (4.19) holds in this case. The space of primitives of${ \mathcal { H } } ^ { \star }$then consists of those differential operators that satisfy Leibniz’s rule, which are of course precisely the first-order differential operators. The grouplike elements consist of their exponentials, which act on polynomials indeed precisely as the group of translations on$\mathbf { R } ^ { d }$

## 4.4 Rough paths

A prime example of a regularity structure on R that is quite different from the canonical structure of polynomials is the structure associated to E-valued geometric rough paths of class$\mathcal { C } ^ { \gamma }$for some$\gamma \in \mathsf { \Gamma } ( 0 , 1 ]$, and some Banach space E. For an introduction to the theory of rough paths, see for example the monographs [45,78,79] or the original article [82]. We will see in this section that, given a Banach space$E .$, we can associate to it in a natural way a regularity structure$\Re _ { E } ^ { \gamma }$which describes the space of E-valued rough paths. The regularity index$\gamma$will only appear in the definition of the index set$A$ Given such a structure, the space of rough paths with regularity$\gamma$turns out to be nothing but the space of models for$\Re _ { E } ^ { \gamma }$

Setting$A \ = \ \gamma \mathbf { N } ,$, we take for$T$the tensor algebra built upon$E ^ { * }$, the topological dual of$E$:

$$
T = \bigoplus_ {k = 0} ^ {\infty} T _ {k \gamma}, \qquad T _ {k \gamma} = \left(E ^ {*}\right) ^ {\otimes k},\tag{4.22}
$$

where$( E ^ { * } ) ^ { \otimes 0 } = \mathbf { R }$. The choice of tensor product on$E$and$E ^ { * }$does not matter in principle, as long as we are consistent in the sense that$\left( E ^ { \otimes k } \right) ^ { * } = ( E ^ { * } ) ^ { \otimes k }$ for every k. We also introduce the space$T _ { \star }$ (which is the predual of T) as the tensor algebra built from$E$, namely$T _ { \star } = T ( ( E ) )$.

Remark 4.20 One would like to write again$T _ { \star } = \bigoplus _ { k = 0 } ^ { \infty } E ^ { \otimes k }$. However, while we consider for T finite linear combinations of elements in the spaces$T _ { k \gamma }$, for $T _ { \star }$, it will be useful to allow for infinite linear combinations.

Both$T$and$T _ { \star }$come equipped with a natural product. On$T _ { \star }$, it will be natural to consider the tensor product$\otimes$, which will be used to define$G$and its action on$T$. The space$T$also comes equipped with a natural product, the shuffle product, which plays in this context the role that polynomial multiplication played for the canonical regularity structures. Recall that, for any alphabet$\mathcal { W }$ the shuffle product is defined on the free algebra over$\mathcal { W }$by considering all possible ways of interleaving two words in ways that preserve the original order of the letters. In our context, if a, b and$c$are elements of$E ^ { * }$, we set for example

$$
\begin{array}{c} (a \otimes b) \sqcup (a \otimes c) = a \otimes b \otimes a \otimes c + 2 a \otimes a \otimes b \otimes c + 2 a \otimes a \otimes c \otimes b \\ + a \otimes c \otimes a \otimes b. \end{array}
$$

Regarding the group G, we then perform the following construction. For any two elements$a , b \in T _ { \star }$, we define their “Lie bracket” by

$$
[ a, b ] = a \otimes b - b \otimes a.
$$

We then define$\mathcal { L } \subset T _ { \star }$as the (possibly infinite) linear combinations of all such brackets, and we set$G = \exp ( \mathfrak { L } ) \subset T _ { \star }$, with the group operation given by the tensor product$\otimes$. Here, for any element$a \in T _ { \star }$, we write

$$
\exp (a) = \sum_ {k = 0} ^ {\infty} \frac {a ^ {\otimes k}}{k !},
$$

with the convention that$a ^ { \otimes 0 } = \mathbf { 1 } \in T _ { 0 }$. Note that this sum makes sense for every element in$T _ { \star }$, and that$\exp ( - a ) = \left( \exp ( a ) \right) ^ { - 1 }$. For every$a \in G$, the corresponding linear map$\Gamma _ { a }$ acting on T is then obtained by duality, via the identity

$$
\langle c, \Gamma_ {a} b \rangle = \left\langle a ^ {- 1} \otimes c, b \right\rangle ,\tag{4.23}
$$

where$\langle \cdot , \cdot \rangle$denotes the pairing between T and$T _ { \star }$. Let us denote by$\Re _ { E } ^ { \gamma }$the regularity structure$( A , T , G )$constructed in this way.

Remark 4.21 The regularity structure$\Re _ { E } ^ { \gamma }$is yet another example ofa regularity structure that can be obtained via the general construction of Sect. 4.3. In this case, our Hopf algebra is given by$T .$, equipped with the commutative product and the non-commutative coproduct obtained from$\otimes$by duality. The required morphism property then just reflects the fact that the shuffle product is indeed a morphism for the deconcatenation coproduct. The choice of action is then the one given by Remark 4.17.

What are the models ( , ) for the regularity structure$\Re _ { E } ^ { \gamma } ?$It turns out that the elements$\Gamma _ { s t }$(which we identify with an element$X _ { s t }$in$T _ { \star }$acting via (4.23)) are nothing but what is generally referred to as geometric rough paths. Indeed, the identity$\Gamma _ { s t } \circ \Gamma _ { t u } = \Gamma _ { s u }$, translates into the identity

$$
\boldsymbol {X} _ {s u} = \boldsymbol {X} _ {s t} \otimes \boldsymbol {X} _ {t u},\tag{4.24}
$$

which is nothing but Chen’s relations [21]. The bound (2.21) on the other hand precisely states that the rough path X is γ-Hölder continuous in the sense of [45] for example. Finally, it is well-known (see (4.21) or [90]) that, for$a \in T _ { k \gamma }$ and$b \in T _ { \ell \gamma }$with$k + \ell \leq p$, and any$\Gamma \in G$, one has the shuffle identity,

$$
\Gamma (a \sqcup b) = (\Gamma a) \sqcup (\Gamma b),
$$

which can be interpreted as a way of encoding the chain rule. This should again be compared to Definition 4.6, which shows that the shuffle product is indeed the natural product for$T$in this context and that T is regular for .

By Proposition 3.31, since our regularity structure only contains elements of positive homogeneity, the model is uniquely determined by$\Gamma$. It is straightforward to check that if we set

$$
\left(\Pi_ {s} a\right) (t) = \langle X _ {s t}, a \rangle ,
$$

then the relations and bounds of Definition 2.17 are indeed satisfied, so that this is the unique model compatible with a given choice of  (or equivalently X).

The interpretation of such a rough path is as follows. Denote by$X _ { t }$the projection of$X _ { 0 t }$onto E, the predual of$T _ { \gamma }$. Then, for every$a \in T _ { k \gamma }$with $k \in \mathbf { N }$, we interpret$\langle X _ { s t } , a \rangle$as providing a value for the corresponding k-fold iterated integral, i.e.,

$$
\left\langle \boldsymbol {X} _ {s t}, a \right\rangle “ = ” \int_ {s} ^ {t} \int_ {s} ^ {t _ {k}} \dots \int_ {s} ^ {t _ {2}} \left\langle d X _ {t _ {1}} \otimes \dots \otimes d X _ {t _ {k - 1}} \otimes d X _ {t _ {k}}, a \right\rangle .\tag{4.25}
$$

A celebrated result by Chen [21] then shows that indeed, if$t \mapsto X _ { t } \in E$is a continuous function of bounded variation, and if X is defined by the right hand side of (4.25), then it is the case that$X _ { s t } \in G$for every s, t and (4.24) holds.

Now that we have identified geometric rough paths with the space of models realising$\Re _ { E } ^ { \gamma }$, it is natural to ask what is the interpretation of the spaces $\mathcal { D } ^ { \beta }$introduced in Sect. 3. An element$f$of$\mathcal { D } ^ { \beta }$should then be thought of as describing a function whose increments can locally (at scale$\varepsilon )$be approximated by linear combinations of components of$X$, up to errors of order$\varepsilon ^ { \beta }$ Setting$p = \lfloor 1 / \gamma \rfloor$, it can be checked that elements of$\mathcal { D } ^ { \beta }$with$\beta = p \gamma$are nothing but the controlled rough paths in the sense of [54].

Writing$f _ { 0 } ( t )$for the component of$f ( t )$in$T _ { 0 } = \mathbf { R }$, it does indeed follow from the definition of$\mathcal { D } ^ { \beta }$that

$$
| f _ {0} (t) - \langle X _ {s t}, f (s) \rangle | \lesssim | t - s | ^ {\beta}.
$$

Since, on the other hand,$\langle X _ { s t } , \mathbf { 1 } \rangle = 1$, we see that one has indeed

$$
f _ {0} (t) - f _ {0} (s) = \left\langle X _ {s t}, \mathcal {Q} _ {0} ^ {\perp} f (s) \right\rangle + \mathcal {O} (| t - s | ^ {\beta}),
$$

where$\mathcal { Q } _ { 0 } ^ { \perp }$is the projection onto the orthogonal complement to 1.

The power of the theory is then that, even though$f _ { 0 }$itself is typically only γ-Hölder continuous, it does in many respects behave “as$\mathrm { i f } ^ { \dag }$it was actually β-Hölder continuous, and one can have$\beta > \gamma$. In particular, it is now quite straightforward to define “integration maps”${ \mathcal { T } } _ { a }$for$a \in E ^ { * }$such that$F = \mathcal { T } _ { a } f$ should be thought of as describing the integral$\begin{array} { r } { F _ { 0 } ( t ) = \int _ { 0 } ^ { t } f _ { 0 } ( s ) d \left. X _ { s } , a \right. } \end{array}$ provided that$\beta + \gamma > 1$

It follows from the interpretation (4.25) that if$f _ { 0 } ( t ) = \langle X _ { t } , b \rangle$for some element$b \in T$, then it is natural to have$F _ { 0 } ( t ) = \left. X _ { t } , b \otimes a \right.$. At first sight, this suggests that one should simply set$F ( t ) = \bigl (  { \mathbb { Z } } _ { a } f \bigr ) ( t ) = f ( t ) \otimes a$. However, since$\langle \mathbf { 1 } , f ( t ) \otimes a \rangle \ = \ 0$, this would not define an element of$\mathcal { D } _ { \gamma } ^ { \beta }$for any $\beta > \gamma$so one still needs to find the correct value for$\langle \mathbf { 1 } , F ( t ) \rangle$. The following result, which is essentially a reformulation of [55, Thm 8.5] in the geometric context, states that there is a unique natural way of constructing this missing component.

Theorem 4.22 For every$\beta > 1 - \gamma$and every$a \in E ^ { * }$there exists a unique linear map$I _ { a } \colon \mathcal { D } ^ { \beta } \to \mathcal { C } ^ { \gamma }$such that$( I _ { a } f ) ( 0 ) = 0$and such that the map${ \mathcal { T } } _ { a }$ defined by

$$
\left(\mathcal {I} _ {a} f\right) (t) = f (t) \otimes a + \left(I _ {a} f\right) (t) \mathbf {1},
$$

maps$\mathcal { D } ^ { \beta }$into$\mathcal { D } ^ { \bar { \beta } }$with$\bar { \beta } = ( \beta \wedge \gamma p ) + \gamma$

Remark 4.23 Even in the context of the classical theory of rough paths, one advantage of the framework presented here is that it is straightforward to accommodate the case of driving processes with different orders of regularity for different components.

Remark 4.24 Using Theorem 4.22, it is straightforward to combine it with Theorem 4.16 in order to solve “rough differential equations” ofthe form$d Y =$ $F ( Y ) d X$. It does indeed suffice to formulate them as fixed point problems

$$
Y = y _ {0} + \mathcal {I} (\hat {F} (Y)).
$$

As a map from$\mathcal { D } ^ { \beta } ( [ 0 , T ] )$into itself, I then has norm$\mathcal { O } ( T ^ { \bar { \beta } - \beta } )$, which tends to 0 as$T  0$and the composition with F is (locally) Lipschitz continuous for sufficiently regular$F _ { \ast }$, so that this map is indeed a contraction for small enough$T$.

Remark 4.25 In general, one can imagine theories of integration in which the chain rule fails, which is very natural in the context of numerical approximations. In this case, it makes sense to replace the tensor algebra by the Connes– Kreimer Hopf algebra of rooted trees [17], which plays in this context the role ofthe “free” algebra generated by the multiplication and integration maps. This is precisely what was done in [55], and one can verify that the construction given there is again equivalent to the construction of Sect. 4.3. See also [18,71] for more details on the role of the Connes–Kreimer algebra (whose group-like elements are also called the “Butcher group” in the numerical analysis literature) in the context of the numerical approximation of solutions to ODEs with smooth coefficients. See also [61] for an analysis of this type of structure from a different angle more closely related to the present work.

## 5 Integration against singular kernels

In this section, we show how to integrate a modelled distribution against a kernel (think of the Green’s function for the linear part of the stochastic PDE under consideration) with a well-behaved singularity on the diagonal in order to obtain another modelled distribution. In other words, given a modelled distribution$f .$, we would like to build another modelled distribution$\kappa f$with the property that

$$
\bigl (\mathcal {R K} f \bigr) (x) = \bigl (K * \mathcal {R} f \bigr) (x) \stackrel {\mathrm{def}} {=} \int_ {\mathbf {R} ^ {d}} K (x, y) \mathcal {R} f (y) d y,\tag{5.1}
$$

for a given kernel$K \colon \mathbf { R } ^ { d } \times \mathbf { R } ^ { d }  \mathbf { R }$, which is singular on the diagonal. Here, $\mathcal { R }$denotes the reconstruction operator as before. Of course, this way of writing is rather formal since neither$\mathcal { R } f$nor$\mathcal { R } \mathcal { K } f$need to be functions, but it is more suggestive than the actual property we are interested in, namely

$$
\begin{array}{r l} \big (\mathcal {R K} f \big) (\psi) & = \big (K * \mathcal {R} f \big) (\psi) \stackrel {{\text { def }}} {{=}} \big (\mathcal {R} f \big) (K ^ {\star} \psi), \\ K ^ {\star} \psi (y) & \stackrel {{\text { def }}} {{=}} \int_ {\mathbf {R} ^ {d}} K (x, y) \psi (x)   d x, \end{array}\tag{5.2}
$$

for all sufficiently smooth test functions$\psi$. In the remainder of this section, we will always use a notation of the type (5.1) instead of (5.2) in order to state our assumptions and results. It is always straightforward to translate it into an expression that makes sense rigorously, but this would clutter the exposition of the results, so we only use the more cumbersome notation in the proofs. Furthermore, we would like to encode the fact that the kernel$K$“improves regularity by$\beta ^ { \ast }$in the sense that, in the notation of Remark 4.8, K is bounded from$\mathcal { D } _ { \alpha } ^ { \gamma }$into$\mathcal { D } _ { ( \alpha + \beta ) \wedge 0 } ^ { \gamma + \beta }$for some$\beta > 0$. For example, in the case of the convolution with the heat kernel, one would like to obtain such a bound with $\beta = 2$, which would be a form of Schauder estimate in our context.

In the case when the right hand side of (5.1) actually defines a function (which is the case for many examples of interest), it may appear that it is straightforward to define$\kappa \colon$simply encode it into the canonical part of the regularity structure by (5.1) and possibly some of its derivatives. The problem with this is that since, for$f ~ \in ~ { \mathcal { D } } _ { \alpha } ^ { \gamma }$, one has$\mathcal { R } f \in \mathcal { C } ^ { \alpha }$, the best one can expect is to have$\mathcal { R } \mathcal { K } f \in \mathcal { C } ^ { \alpha + \beta }$. Encoding this into the canonical regularity structure would then yield an element of$\bar { \mathcal { D } } _ { 0 } ^ { \alpha + \beta }$, provided that one even has $\alpha + \beta > 0$. In cases where$\gamma > \alpha$, which is the generic situation considered in this article, this can be substantially short of the result announced above. As a consequence,$\kappa f$should in general also have non-zero components in parts of T that do not encode the canonical regularity structure, which is why the construction of$\kappa$is highly non-trivial.

Let us first state exactly what we mean by the fact that the kernel$K \colon  { \mathbf { R } } ^ { d } \times$ $\mathbf R ^ { d } \to \mathbf R$“improves regularity by order$\beta ^ { \dag }$:

## Assumption 5.1 Thefunction K can be decomposed as

$$
K (x, y) = \sum_ {n \geq 0} K _ {n} (x, y),\tag{5.3}
$$

where thefunctions$K _ { n }$have thefollowing properties:

For all$n \geq 0$, the map$K _ { n }$is supported in the set$\{ ( x , y ) : \| x - y \| _ { 5 } \leq 2 ^ { - n } \}$

For any two multiindices k and , there exists a constant C such that the bound

$$
\left| D _ {1} ^ {k} D _ {2} ^ {\ell} K _ {n} (x, y) \right| \leq C 2 ^ {(| \mathfrak {s} | - \beta + | \ell | _ {\mathfrak {s}} + | k | _ {\mathfrak {s}}) n},\tag{5.4}
$$

holds uniformly over all$n \geq 0$and all$x , y \in \mathbf { R } ^ { d }$

For any two multiindices k and , there exists a constant C such that the bounds

$$
\left| \int_ {\mathbf {R} ^ {d}} (x - y) ^ {\ell} D _ {2} ^ {k} K _ {n} (x, y)   d x \right| \leq C 2 ^ {- \beta n},
$$

$$
\left| \int_ {\mathbf {R} ^ {d}} (y - x) ^ {\ell} D _ {1} ^ {k} K _ {n} (x, y)   d y \right| \leq C 2 ^ {- \beta n},\tag{5.5}
$$

hold uniformly over all$n \geq 0$and all x,$\boldsymbol { y } \in \mathbf { R } ^ { d }$

In these expressions, we write$D _ { 1 }$for the derivative with respect to the first argument and$D _ { 2 } f o r$the derivative with respect to the second argument.

Remark 5.2 In principle, we typically only need (5.4) and (5.5) to hold for multiindices k and  that are smaller than some fixed number, which depends on the particular “Schauder estimate” we wish to obtain. In practice however these bounds tend to hold for all multiindices, so we assume this in order to simplify notations.

A very important insight is that polynomials are going to play a distinguished role in this section. As a consequence, we work with a fixed regularity structure $\mathcal { T } = ( A , T , G )$and we assume that one has$\mathcal { T } _ { d , \mathfrak { s } } \subset \mathcal { T }$for the same scaling s and dimension d as appearing in Definition 5.1. As already mentioned in Remark 2.23, we will use the notation$\bar { T } \subset T$for the subspace spanned by the “abstract polynomials”. Furthermore, as in Sect. 2.2, we will denote by$X ^ { \check { k } }$the canonical basis vectors of$\bar { T }$, where k is a multiindex in$\mathbf { N } ^ { d }$. We furthermore assume that, except for polynomials, integer homogeneities are avoided:

Assumption 5.3 For every integer value$n ~ \ge ~ 0 , ~ T _ { n } ~ = ~ \bar { T } _ { n }$consists of the linear span of elements of the form$X ^ { k }$with$| k | _ { 5 } = n .$. Furthermore, one considers models that are compatible with this structure in the sense that $\left( \Pi _ { x } X ^ { k } \right) ( y ) = ( y - x ) ^ { k }$

In order to interplay nicely with our structure, we will make the following additional assumption on the decomposition of the kernel K:

Assumption 5.4 There exists$r > 0$such that

$$
\int_ {\mathbf {R} ^ {d}} K _ {n} (x, y)   P (y)   d y = 0,\tag{5.6}
$$

for every$n \geq 0 _ { i }$, every$\boldsymbol { x } \in \mathbf { R } ^ { d }$, and every polynomial P ofscaled degree less than or equal to r.

All of these three assumptions will be standing throughout this whole section. We will therefore not restate this explicitly, except in the statements of the main theorems. Even though Assumption 5.4 seems quite restrictive, it turns out not to matter at all. Indeed, a kernel K that is regularity improving in the sense of Definition 5.1 can typically be rewritten as$K = K _ { 0 } + K _ { 1 }$ such that$K _ { 0 }$is smooth and$K _ { 1 }$additionally satisfies both Assumptions 5.1 and 5.4. Essentially, it suffices to “excise the singularity” with the help of a compactly supported smooth cut-off function and to then add and subtract some smooth function supported away from the origin which ensures that the required number of moments vanish.

In many cases of interest, one can take K to depend only on the difference between its two arguments. In this case, one has the following result, which shows that our assumptions typically do cover the Green’s functions of differential operators with constant coefficients.

Lemma 5.5$L e t \bar { K } \colon { \bf R } ^ { d } \backslash \{ 0 \}$R be a smoothfunction which is homogeneous under the scaling s in the sense that there exists a$\beta > 0$such that the identity

$$
\bar {K} (\mathcal {S} _ {\mathfrak {s}} ^ {\delta} x) = \delta^ {| \mathfrak {s} | - \beta} \bar {K} (x),\tag{5.7}
$$

holdsfor all$x \neq 0$and all$\delta \in ( 0 , 1 ]$. Then, it is possible to decompose$\bar { K }$as $\bar { K } ( x ) = K ( x ) + R ( x )$in such a way that the “remainder” R is${ \mathcal { C } } ^ { \infty }$on all of $\mathbf { R } ^ { d }$and such that the map$( x , y ) \mapsto K ( x - y )$satisfies Assumptions 5.1 and 5.4.

Proof Note first that if each of the$K _ { n }$is a function of$x - y$, then the bounds (5.5) follow from (5.4) by integration by parts. We therefore only need to exhibit a decomposition$K _ { n }$such that (5.4) is satisfied and such that (5.6) holds for every polynomial P of some fixed but arbitrary degree.

Let$N \colon { \mathbf { R } } ^ { d } \setminus \{ 0 \} \to { \mathbf { R } } _ { + }$be a smooth “norm” for the scaling s in the sense that N is smooth, convex, strictly positive, and${ \cal N } ( S _ { \mathfrak { s } } ^ { \delta } x ) = \delta { \cal N } ( x )$. (See for example Remark 2.13.) Then, we can introduce “spherical coordinates$\ " ( r , \theta )$ with$r \in \mathbf { R } _ { + }$and$\theta \in S { \stackrel { \mathrm { d e f } } { = } } N ^ { - 1 } ( 1 )$) by$r ( x ) = N ( x )$, and$\boldsymbol { \theta } ( \boldsymbol { x } ) = \boldsymbol { S _ { 5 } ^ { r ( x ) } } \boldsymbol { x }$. With these notations, (5.7) is another way of stating that$\bar { K }$can be factored as

$$
\bar {K} (x) = r ^ {\beta - | \mathfrak {s} |} \Theta (\theta),
$$

(5.8)

for some smooth function on S. Here and below, we suppress the implicit dependency of r and θ on x.

Our main ingredient is then the existence of a smooth “cutoff function” $\varphi : \mathbf { R } _ { + } \to [ 0 , 1 ]$such that$\varphi ( r ) = 0$for$r \not \in [ 1 / 2 , 2 ]$, and such that

$$
\sum_ {n \in \mathbf {Z}} \varphi (2 ^ {n} r) = 1,\tag{5.9}
$$

for all$r > 0$(see for example the construction of Paley–Littlewood blocks in [6]). We also set$\begin{array} { r } { \varphi _ { R } ( r ) = \sum _ { n < 0 } \varphi ( 2 ^ { n } r ) } \end{array}$and, for$n \geq 0 , \varphi _ { n } ( r ) = \varphi ( 2 ^ { n } r )$. With these functions at hand, we define

$$
\bar {K} _ {n} (x) = \varphi_ {n} (r) \bar {K} (x), \quad \bar {R} (x) = \varphi_ {R} (r) \bar {K} (x).
$$

Since$\varphi _ { R }$is supported away from the origin, the function$\bar { R }$is globally smooth. Furthermore, each of the$\bar { K } _ { n }$is supported in the ball of radius$2 ^ { - n }$, provided that the “norm” N was chosen such that$N ( x ) \geq 2 \| x \| _ { \mathfrak { s } }$

It is straightforward to verify that (5.4) also holds. Indeed, by the exact scaling property (5.7) of$\bar { K }$, one has the identity

$$
\bar {K} _ {n} (x) = 2 ^ {- (\beta - | \mathfrak {s} |) n} \bar {K} _ {0} (\mathcal {S} _ {\mathfrak {s}} ^ {2 ^ {- n}} x),
$$

and (5.4) then follows immediately form the fact that$K _ { 0 }$is a compactly supported smooth function.

It remains to modify this construction in such a way that (5.6) holds as well. For this, choose any function$\psi$which is smooth, supported in the unit ball around the origin, and such that, for every multiindex$k$with$| k | _ { \mathfrak { s } } \leq r$, one has the identity

$$
\left(1 - 2 ^ {- \beta - | k | _ {\mathfrak {s}}}\right) \int x ^ {k} \psi (x) d x = \int x ^ {k} \bar {K} _ {0} (x) d x.
$$

It is of course straightforward to find such a function. We then set

$$
K _ {0} (x) = \bar {K} _ {0} (x) - \psi (x) + 2 ^ {| \mathfrak {s} | - \beta} \psi (\mathcal {S} _ {\mathfrak {s}} ^ {2} x),
$$

as well as

$$
K _ {n} (x) = 2 ^ {- (\beta - | \mathfrak {s} |) n} K _ {0} (\mathcal {S} _ {\mathfrak {s}} ^ {2 ^ {n}} x), \qquad R (x) = \bar {R} (x) + \psi (x).
$$

Since$\psi$is smooth and$K _ { n }$has the same scaling properties as before, it is clear that the required bounds are still satisfied. Furthermore, our construction is such that one has the identity

$$
\sum_ {n = 0} ^ {N - 1} K _ {n} (x) = \sum_ {n = 0} ^ {N - 1} \bar {K} _ {n} (x) - \psi (x) + 2 ^ {- (\beta - | \mathfrak {s} |) N} \psi (\mathcal {S} _ {\mathfrak {s}} ^ {2 ^ {N}} x),
$$

so that it is still the case that$\begin{array} { r } { \bar { K } ( x ) = R ( x ) + \sum _ { n > 0 } K _ { n } ( x ) } \end{array}$. Finally, the exact scaling properties of these expressions imply that

$$
\begin{array}{r l} & {\int x ^ {k} K _ {n} (x) d x = 2 ^ {- (\beta + | k | _ {\mathfrak {s}}) n} \int x ^ {k} K _ {0} (x) d x} \\ & {\qquad = 2 ^ {- (\beta + | k | _ {\mathfrak {s}}) n} \int x ^ {k} \big (\bar {K} _ {0} (x) - \psi (x) + 2 ^ {| \mathfrak {s} | - \beta} \psi (\mathcal {S} _ {\mathfrak {s}} ^ {2} x) \big) d x} \\ & {\qquad = 2 ^ {- (\beta + | k | _ {\mathfrak {s}}) n} \int x ^ {k} \big (\bar {K} _ {0} (x) - (1 - 2 ^ {- \beta - | k | _ {\mathfrak {s}}}) \psi (x) \big) d x = 0,} \end{array}
$$

as required.

Remark 5.6 A slight modification of the argument given above also allows to cover the situation where (5.8) is replaced by$\bar { K } ( x ) = \Theta ( \theta )$log r. One can then set

$$
\bar {K} _ {n} (x) = - \Theta (\theta) \int_ {r} ^ {\infty} \frac {\varphi_ {n} (r)}{r} d r,
$$

and the rest of the argument is virtually identical to the one just given. In such a situation, one then has$\beta = | \mathfrak { s } |$, thus covering for example the case of the Green’s function of the Laplacian in dimension 2.

Of course, in order to have any chance at all to obtain a Schauder-type bound as above, our model needs to be sufficiently “rich” to be able to describe$\kappa f$ with sufficient amount of detail. For this, we need two ingredients. First, we need the existence of a map$\mathcal { T } \colon T  T$that provides an “abstract” representation of K operating at the level of the regularity structure, and second we need that the model is adapted to this representation in a suitable manner.

In our definition, we denote again by$\bar { T }$the sector spanned by abstract monomials of the type$X ^ { k }$for some multiindex$k$

Definition 5.7 Given a sector V, a linear map${ \mathcal { T } } \colon V \ \to \ T$is an abstract integration map of order$\beta > 0$if it satisfies the following properties:

One has I$V _ { \alpha } \to T _ { \alpha + \beta }$for every$\alpha \in A$

One has$\mathcal { T } a = 0$for every$a \in V \cap { \bar { T } }$

One has$\mathcal { T } \Gamma a - \Gamma \mathcal { T } a \in \bar { T }$for every$a \in V$and every$\Gamma \in G$

(The first property should be interpreted as${ \mathcal { T } } a = 0 { \mathrm { i f } } a \in V _ { \alpha }$and$\alpha + \beta \not \in A . )$

Remark 5.8 At first sight, the second and third conditions might seem strange. It would have been aesthetically more pleasing to impose that I commutes with G, i.e. that$\mathcal { T } \Gamma = \Gamma \mathcal { T }$. This would indeed be very natural if I was a “direct” abstraction of our integration map in the sense that

$$
\Pi_ {x} \mathcal {I} a = \int_ {\mathbf {R} ^ {d}} K (\cdot , z) \bigl (\Pi_ {x} a \bigr) (d z).\tag{5.10}
$$

The problem with such a definition is that if$a \in T _ { \alpha }$with$\alpha > - \beta$, so that $\mathcal { T } a \in T _ { \bar { \alpha } }$for some$\bar { \alpha } > 0$, then (2.15) requires us to define$\Pi _ { x } \mathcal { I } a$in such a way that it vanishes to some positive order for localised test functions. This is simply not true in general, so that (5.10) is not the right requirement. Instead, we will see below that one should modify (5.10) in a way to subtract a suitable polynomial that forces the$\Pi _ { x } \mathcal { I } a$to vanish at the correct order. It is this fact that leads to consider structures with$\mathcal { T } \Gamma a - \Gamma \mathcal { T } a \in \bar { T }$rather than$\mathscr { T } \Gamma a - \Gamma \mathscr { T } a = 0$

Our second and main ingredient is that the model should be “compatible” with the fact that$\mathcal { T }$encodes the integral kernel K. For this, given an integral kernel K as above, an important role will be played by the function$\mathcal { I } \colon  { \mathbf { R } ^ { d } } \to$ $L _ { T } ^ { \beta }$which, for every$a \in T _ { \alpha }$and every$\alpha \in A$, is given by

$$
\mathcal {J} (x) a = \sum_ {| k | _ {\mathfrak {s}} <   \alpha + \beta} \frac {X ^ {k}}{k !} \int_ {\mathbf {R} ^ {d}} D _ {1} ^ {k} K (x, z) (\Pi_ {x} a) (d z),\tag{5.11}
$$

where we denote by$D _ { 1 }$the differentiation operator with respect to the first variable. It is straightforward to verify that, writing$K = \sum K _ { n }$as before and swapping the sum over n with the integration, this expression does indeed make sense.

Definition 5.9 Given a sector V and an abstract integration operator I on$V$ we say that a model realises K for I if, for every$\alpha \in A$, every$a \in V _ { \alpha }$and every$\boldsymbol { \mathbf { \bar { \mathbf { x } } } } \in \mathbf { \mathbf { R } } ^ { d }$, one has the identity

$$
\Pi_ {x} \mathcal {I} a = \int_ {\mathbf {R} ^ {d}} K (\cdot , z) \bigl (\Pi_ {x} a \bigr) (d z) - \Pi_ {x} \mathcal {J} (x) a,\tag{5.12}
$$

Remark 5.10 The rigorous way of stating this definition is that, for all smooth and compactly supported test functions$\psi$and for all$a \in T _ { \alpha }$, one has

$$
\bigl (\Pi_ {x} \mathcal {I} a \bigr) (\psi) = \sum_ {n \geq 0} \int_ {\mathbf {R} ^ {d}} \psi (y) \bigl (\Pi_ {x} a \bigr) (K _ {n; x y} ^ {\alpha}) d y,\tag{5.13}
$$

where the function$K _ { n ; x y } ^ { \alpha }$is given by

$$
K _ {n; x y} ^ {\alpha} (z) = K _ {n} (y, z) - \sum_ {| k | _ {\mathfrak {s}} <   \alpha + \beta} \frac {(y - x) ^ {k}}{k !} D _ {1} ^ {k} K _ {n} (x, z).\tag{5.14}
$$

The purpose of subtracting the term involving the truncated Taylor expansion of K is to ensure that$\Pi _ { x } \mathcal { Z } a$vanishes at x at sufficiently high order. We will see below that in our context, it is always guaranteed that the sum over n appearing in (5.13) converges absolutely, see Lemma 5.19 below.

Remark 5.11 The case of simple integration in one dimension is very special in this respect. Indeed, the role of the “Green’s function” K is then played by the Heaviside function. This has the particular property of being constant away from the origin, so that all of its derivatives vanish. In particular, the quantity$\mathcal { I } ( x ) a$then always takes values in$T _ { 0 }$. This is why it is possible to consider expansions of arbitrary order in the theory of rough paths without ever having to incorporate the space of polynomials into the corresponding regularity structure.

Note however that the “rough integral” is not an immediate corollary of Theorem 5.12 below, due in particular to the fact that Assumption 5.4 does not hold for the Heaviside function. It is however straightforward to build the rough integral of any controlled path against the underlying rough path using the formalism developed here. In order not to stray too far from our main line of investigation we refrain from giving this construction.

With all ofthese definitions at hand, we are now in the position to provide the definition of the map$\kappa$on modelled distributions announced at the beginning of this section. Actually, it turns out that for different values of$\gamma$one should use slightly different definitions. Given$f \in { \mathcal { D } } ^ { \gamma }$, we set

$$
\big (\mathcal {K} _ {\gamma} f \big) (x) = \mathcal {I} f (x) + \mathcal {J} (x) f (x) + \big (\mathcal {N} _ {\gamma} f \big) (x),\tag{5.15}
$$

where$\mathcal { T }$is as above, acting pointwise,$\mathcal { I }$is given in (5.11), and the operator $\mathcal { N } _ { \gamma }$maps$f$into a$\bar { T }$-valued function by setting

$$
\left(\mathcal {N} _ {\gamma} f\right) (x) = \sum_ {| k | _ {\mathfrak {s}} <   \gamma + \beta} \frac {X ^ {k}}{k !} \int_ {\mathbf {R} ^ {d}} D _ {1} ^ {k} K (x, y) \left(\mathcal {R} f - \Pi_ {x} f (x)\right) (d y).\tag{5.16}
$$

(We will show later that this expression is indeed well-defined for all$f \in { \mathcal { D } } ^ { \gamma } . )$

With all of these definitions at hand, we can state the following two results, which are the linchpin around which the whole theory developed in this work revolves. First, we have the announced Schauder-type estimate:

Theorem 5.12 Let$\mathcal { T } = ( A , T , G )$be a regularity structure and$( \Pi , \Gamma )$be a modelfor$\mathcal { T }$satisfying Assumption 5.3. Let K be a β-regularising kernelfor some$\beta > 0$, let I be an abstract integration map of order$\beta$acting on some sector V, and let be a model realising K for I. Let furthermore$\gamma > 0$ assume that K satisfies Assumption 5.4for$r = \gamma + \beta$, and define the operator $\kappa _ { \gamma }$by (5.15).

Then,provided that$\gamma + \beta \notin \mathbf { N } , \mathcal { K } _ { \gamma }$maps${ \mathcal { D } } ^ { \gamma } ( V )$into$\mathcal { D } ^ { \gamma + \beta }$, and the identity

$$
\mathcal {R K} _ {\gamma} f = K * \mathcal {R} f,\tag{5.17}
$$

holdsfor every$f \in { \mathcal { D } } ^ { \gamma } ( V )$. Furthermore,$i f ( { \bar { \Pi } } , { \bar { \Gamma } } )$) is a second model realising K and one has$\bar { f } \in \mathcal { D } ^ { \gamma } ( V ; \bar { \Gamma } )$, then the bound

$$
\| \mathcal {K} _ {\gamma} f; \bar {\mathcal {K}} _ {\gamma} \bar {f} \| _ {\gamma + \beta ; \mathfrak {K}} \lesssim \| f; \bar {f} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma + \beta ; \bar {\mathfrak {K}}},
$$

holds. Here,$\mathscr { k }$is a compact and$\bar { \mathbf { \mathcal { R } } }$is its 1-fattening. The proportionality constant implicit in the bound depends only on the norms$\| f \| _ { \gamma ; \bar { \mathscr { R } } } , \| \bar { f } \| _ { \gamma ; \bar { \mathscr { R } } } ,$as well as similar bounds on the two models.

Remark 5.13 One surprising feature of Theorem 5.12 is that the only non-local term in$\kappa _ { \gamma }$is the operator$\mathcal { N } _ { \gamma }$which is a kind of“remainder term”. In particular, the “rough” parts of$\kappa _ { \gamma } f , \mathrm { i . e }$. the fluctuations that cannot be described by the canonical model consisting of polynomials, are always obtained as the image of the “rough” parts of$f$under a simple local linear map. We will see in Sect. 8 below that, as a consequence of this fact, if$f \in \mathcal { D } ^ { \gamma }$is the solution to a stochastic PDE built from a local fixed point argument using this theory, then the “rough” part in the description of$f$is always given by explicit local functions of the “smooth part”, which can be interpreted as some kind of renormalised Taylor series.

The assumptions on the model and on the regularity structure$\mathcal { T } =$ $( A , T , G )$(in particular the existence of a map$\mathcal { T }$with the right properties) may look quite stringent at first sight. However, it turns out that it is always possible to embed any regularity structure$\mathcal { T }$into a larger regularity structure in such a way that these assumptions are satisfied. This is our second main result, which can be stated in the following way.

Theorem 5.14 (Extension theorem) Let$\mathcal { T } = ( A , T , G )$be a regularity structure containing the canonical regularity structure$\mathcal { T } _ { d , \mathfrak { s } }$as stated in Assumption 5.3, let$\beta > 0 ,$, and let$V \subset T$be a sector oforder  with the property that for every α$\notin \mathbf { N }$with$V _ { \alpha } \neq 0$, one has$\alpha + \beta \not \in \mathbf { N } .$. Letfurthermore$W \subset V$be a subsector of V and let K be a kernel on$\mathbf { R } ^ { d }$satisfying Assumptions 5.1 and 5.4 for every$r \leq \bar { \Gamma }$. Let ( , ) be a model for$\mathcal { T }$, and let I$W  T$be an abstract integration map oforder$\beta$such that realises K for$\mathcal { T } .$

Then, there exists a regularity structure$\hat { \mathcal T }$containing$\mathcal { T } _ { ; }$, a model$( \hat { \Pi } , \hat { \Gamma } )$ for$\hat { \mathcal T }$extending ( , ), and an abstract integration map$\hat { \mathcal { I } }$oforder β acting on$\hat { V } = \iota V$such that:

The model$\hat { \Pi }$realises K for$\hat { \mathcal { T } } .$

The map$\hat { \mathcal { I } }$extends I in the sense that$\hat { \mathcal { T } } \iota a = \iota \mathcal { T } a$for every$a \in W$

Furthermore, the map$( \Pi , \Gamma ) \mapsto ( \hat { \Pi } , \hat { \Gamma } )$is locally bounded and Lipschitz continuous in the sense that if ( , ) and$( \bar { \Pi } , \bar { \Gamma } )$are two modelsfor$\mathcal { T }$and ( , ) and$( \hat { \bar { \Pi } } , \hat { \bar { \Gamma } } )$are their respective extensions, then one has the bounds

$$
\| \hat {\Pi} \| _ {\hat {V}; \mathfrak {K}} + \| \hat {\Gamma} \| _ {\hat {V}; \mathfrak {K}} \lesssim \| \Pi \| _ {V; \bar {\mathfrak {K}}} (1 + \| \Gamma \| _ {V; \bar {\mathfrak {K}}}),
$$

$$
\begin{array}{r} \| \hat {\Pi} - \hat {\bar {\Pi}} \| _ {\hat {V}; \mathfrak {K}} + \| \hat {\Gamma} - \hat {\bar {\Gamma}} \| _ {\hat {V}; \mathfrak {K}} \lesssim \| \Pi - \bar {\Pi} \| _ {V; \bar {\mathfrak {K}}} (1 + \| \Gamma \| _ {V; \bar {\mathfrak {K}}}) \\ + \| \bar {\Pi} \| _ {V; \bar {\mathfrak {K}}} \| \Gamma - \bar {\Gamma} \| _ {V; \bar {\mathfrak {K}}}, \end{array}\tag{5.18}
$$

for any compact$\mathcal { R } \subset \mathbf { R } ^ { d }$and its 2-fattening$\bar { \mathcal { R } } .$

Remark 5.15 In this statement, the sector W is also allowed to be empty. See also Sect. 8.2 below for a general construction showing how one can build a regularity structure from an abstract integration map.

The remainder of this section is devoted to the proof of these two results. We start with the proof of the extension theorem, which allows us to introduce all the objects that are then needed in the proof of the multi-level Schauder estimate, Theorem 5.12.

## 5.1 Proof of the extension theorem

Before we turn to the proof, we prove the following lemma which will turn out to be very useful:

Lemma 5.16 Let$\mathcal { I } \colon \mathbf { R } ^ { d } \to \bar { T }$be as above, let$V \subset T$be a sector, and let $\mathcal { T } \colon V  T$be adapted to the kernel K. Then one has the identity

$$
\Gamma_ {x y} \big (\mathcal {I} + \mathcal {J} (y) \big) = \big (\mathcal {I} + \mathcal {J} (x) \big) \Gamma_ {x y},\tag{5.19}
$$

for every$x , y \in \mathbf { R } ^ { d }$

Proof Note first that$\mathcal { I }$is well-defined in the sense that the following expression converges:

$$
\bigl (\mathcal{J}(x)a\bigr)_{k} = \frac{1}{k!}\sum_{\substack{\gamma \in A\\ |k|_{\mathfrak{s}} <   \gamma +\beta}}\sum_{n\geq 0}\bigl (\Pi_{x}\mathcal{Q}_{\gamma}a\bigr)\bigl (D_{1}^{k}K_{n}(x,\cdot)\bigr).\tag{5.20}
$$

Indeed, applying the bound (5.29) which will be obtained in the proof of Lemma 5.19 below, we see that the sum in (5.20) is uniformly convergent for every$\gamma \in A$

In order to show (5.19) we use the fact that, by the definition of an abstract integration map, we have$\Gamma _ { x y } \mathcal { T } a - \mathcal { T } \Gamma _ { x y } a \in \bar { T }$for every$a \in T$and every pair $x , y \in \mathbf { R } ^ { d }$. Since$\Pi _ { x }$is injective on$\bar { T }$(it maps an abstract polynomial into its concrete realisation based at x), it therefore suffices to show that one has the identity

$$
\Pi_ {y} \big (\mathcal {I} + \mathcal {J} (y) \big) = \Pi_ {x} \big (\mathcal {I} + \mathcal {J} (x) \big) \Gamma_ {x y}.
$$

This however follows immediately from (5.12).

ProofofTheorem 5.14 We first argue that we can assume without loss of gen erality that we are in a situation where the sector V is given by a finite sum

$$
V = V _ {\alpha_ {1}} \oplus V _ {\alpha_ {2}} \oplus \ldots \oplus V _ {\alpha_ {n}},\tag{5.21}
$$

where the$\alpha _ { i }$are an increasing sequence of elements in$A$, and where furthermore$W _ { \alpha _ { k } } = V _ { \alpha _ { k } }$for all$k < n$. Indeed, we can first consider the case$V = V _ { \alpha _ { 1 } }$ and$W = W _ { \alpha _ { 1 } }$and apply our result to build an extension to all of$V _ { \alpha _ { 1 } }$. We then consider the case$V = V _ { \alpha _ { 1 } } \oplus V _ { \alpha _ { 2 } }$and$W = V _ { \alpha _ { 1 } } \oplus W _ { \alpha _ { 2 } }$, etc. We then denote by$\bar { W }$the complement of$W _ { \alpha _ { n } }$in$V _ { \alpha _ { n } }$so that$V _ { \alpha _ { n } } = W _ { \alpha _ { n } } \oplus \bar { W } _ { \alpha _ { n } }$

The proof then consists of two steps. First, we build the regularity structure $\hat { \mathcal { T } } = \hat { ( A , T , G ) }$and the map$\hat { \boldsymbol { \mathcal { I } } } .$, and we show that they have the required properties. In a second step, we will then build the required extension$( \hat { \Pi } , \hat { \Gamma } )$ and we will show that it satisfies the identity given by Definition 5.9, as well as the bounds of Definition 2.17 required to make it a bona fide model for$\hat { \mathcal T }$

The only reason why$\mathcal { T }$needs to be extended is that we have no way a priori to define$\hat { \mathcal { I } }$to$\bar { W }$, so we simply add a copy of it to$T$and we postulate this copy to be image of$\bar { W }$under the extension$\hat { \mathcal { I } }$of$\mathcal { T } .$. We then extend G in a way which is consistent with Definition 5.7. More precisely, our construction goes as follows. We first define

$$
\hat {A} = A \cup \{\alpha_ {n} + \beta \},
$$

where$\alpha _ { n }$is as in (5.21), and we define$\hat { T }$to be the space given by

$$
\hat {T} = T \oplus \bar {W}.
$$

We henceforth denote elements in${ \hat { T } } \ b y \ ( a , b )$with$a \in T$and$b \in \bar { W }$, and the injection map$\iota \colon T  { \hat { T } }$is simply given by$\iota a = ( a , 0 )$. Furthermore, we set

$$
\hat {T} _ {\alpha} = \left\{ \begin{array}{l l} T _ {\alpha} \oplus \bar {W} \text {   if   } \alpha = \alpha_ {n} + \beta , \\ T _ {\alpha} \oplus 0 \text {   otherwise. } \end{array} \right.
$$

With these notations, one then indeed has the identity$\hat { T } = \oplus _ { \alpha \in \hat { A } } \hat { T } _ { \alpha }$as required.

In order to complete the construction of$\hat { \mathcal { T } }$, it remains to extend$G$. As a set, we simply set$\hat { \hat { G } } = G \times M _ { \bar { W } } ^ { \alpha _ { n } + \beta }$, where$M _ { \bar { W } } ^ { \alpha }$denotes the set of linear maps from$\bar { W }$into$\bar { T } _ { \alpha } ^ { - } ~ \mathrm { ( i . e }$. the polynomials of scaled degree strictly less than α). The composition rule on$\hat { G }$is then given by the following skew-product:

$$
\left(\Gamma_ {1}, M _ {1}\right) \circ \left(\Gamma_ {2}, M _ {2}\right) = \left(\Gamma_ {1} \Gamma_ {2}, \Gamma_ {1} M _ {2} + M _ {1} + \left(\Gamma_ {1} \mathcal {I} - \mathcal {I} \Gamma_ {1}\right) (\Gamma_ {2} - 1)\right).\tag{5.22}
$$

One can check that this composition rule yields an element of$\hat { G }$. Indeed, by assumption,$G$leaves$\bar { T }$invariant, so that$\Gamma _ { 1 } M _ { 2 }$is indeed again an ele ment of$\hat { M } _ { \bar { W } } ^ { \alpha _ { n } + \beta }$. Furthermore,$\Gamma _ { 1 } \mathcal { T } - \mathcal { I } \Gamma _ { 1 }$is an element of$L _ { V } ^ { \beta } \subset M _ { V } ^ { \alpha _ { n } + \beta }$by assumption, so that the last term also maps$\bar { W }$into$\bar { T } _ { \alpha _ { n } + \beta } ^ { - }$as required. For any $( \Gamma , M ) \in { \hat { G } }$, we then give its action on$\hat { T }$by setting

$$
(\Gamma , M) (a, b) = \left(\Gamma a + \mathcal {I} (\Gamma b - b) + M b, b\right).
$$

Observe that

$$
(\Gamma , M) (a, b) - (a, b) = \big ((\Gamma a - a) + \mathcal {I} (\Gamma b - b) + M b, 0 \big),
$$

so that this definition does satisfy the condition (2.1).

Straightforward verification shows that one has indeed

$$
\bigl ((\Gamma_ {1}, M _ {1}) \circ (\Gamma_ {2}, M _ {2}) \bigr) (a, b) = (\Gamma_ {1}, M _ {1}) \bigl ((\Gamma_ {2}, M _ {2}) (a, b) \bigr).
$$

Since it is immediate that this action is also faithful, this does imply that the operation$^ { \circ }$defined in (5.22) is associative as required. Furthermore, one can verify that (1, 0) is neutral for the operation$^ { \circ }$and that$( \Gamma , M )$has an inverse given by

$$
(\Gamma , M) ^ {- 1} = \left(\Gamma^ {- 1}, - \Gamma^ {- 1} \big (M + (\Gamma \mathcal {I} - \mathcal {I} \Gamma) (\Gamma - 1) \big)\right),
$$

so that$( { \hat { G } } , \circ )$is indeed a group. This shows that$\hat { \mathcal { T } } = ( \hat { A } , \hat { T } , \hat { G } )$is indeed again a regularity structure. Furthermore, the map$j \colon { \hat { G } } \to G$given by$j ( \Gamma , M ) = \Gamma$ is a group homomorphism which verifies that, for every$a \in T$and$\Gamma \in G$ one has the identity

$$
\big (j (\Gamma , M) \big) a = \Gamma a = \iota^ {- 1} (\Gamma a, 0) = \iota^ {- 1} (\Gamma , M) \iota a.
$$

This shows that ι and$j$do indeed define a canonical inclusion$\mathcal { T } \subset \hat { \mathcal { T } }$, see Sect. 2.1.

It is now very easy to extend I to the image of all of V in$\hat { T }$. Indeed, for any$a \in V$, we have a unique decomposition$a = a _ { 0 } + a _ { 1 }$with$a _ { 0 } \in \ W$and $a _ { 1 } \in \bar { W }$. We then set

$$
\hat {\mathcal {I}} (a, 0) = (\mathcal {I} a _ {0}, a _ {1}).
$$

Since$a _ { 1 } = 0$for$a \in W$, one has indeed$\hat { \mathcal { T } } \iota a = \hat { \mathcal { I } } ( a , 0 ) = ( \mathcal { T } a , 0 ) = \iota \mathcal { T } a$in this case, as claimed in the statement of the theorem. As far as the abstract part of our construction is concerned, it therefore remains to verify that$\hat { \mathcal { I } }$defined in this way does verify our definition of an abstract integration map. The fact that$\hat { \mathcal { T } } \colon \hat { V } _ { \alpha } \to \hat { T } _ { \alpha + \beta }$is a direct consequence of the fact that we have simply postulated that 0$\hat W \subset \hat { T } _ { \alpha _ { n } + \beta }$. Since the action of$\mathcal { T }$on$\bar { T }$did not change in our construction, one still has$\hat { \mathcal { T } } \bar { T } = 0$. Regarding the third property, for any $( \Gamma , M ) \in { \hat { G } }$and every$a = a _ { 1 } + a _ { 2 } \in V$as above, we have

$$
\hat {\mathcal {I}} (\Gamma , M) (a, 0) = \hat {\mathcal {I}} (\Gamma a, 0) = \left(\mathcal {I} \Gamma a _ {1} + \mathcal {I} (\Gamma a _ {2} - a _ {2}), a _ {2}\right),
$$

where we use the fact that$\Gamma a _ { 2 } - a _ { 2 } \in V$by the structural assumption (5.21) we made at the beginning of this proof. On the other hand, we have

$$
(\Gamma , M) \hat {\mathcal {I}} (a, 0) = (\Gamma , M) (\mathcal {I} a _ {1}, a _ {2}) = \left(\Gamma \mathcal {I} a _ {1} + \mathcal {I} (\Gamma a _ {2} - a _ {2}) + M a _ {2}, a _ {2}\right),
$$

so that the last property of an abstract integration map is also satisfied. It remains to provide an explicit formula for the extended model$( \hat { \Pi } , \hat { \Gamma } )$ Regarding$\hat { \Pi }$, for$b \in \bar { W }$and$\boldsymbol { x } \in \mathbf { R } ^ { d }$, we simply define it to be given by

$$
\hat {\Pi} _ {x} (a, b) = \Pi_ {x} a + \int_ {\mathbf {R} ^ {d}} K (\cdot , z) \bigl (\Pi_ {x} b \bigr) (d z) - \Pi_ {x} \mathcal {J} (x) b,\tag{5.23}
$$

where$\mathcal { I }$is given by (5.11), which guarantees that the model$\hat { \Pi }$realises K for $\hat { \mathcal { I } }$on V. Again, this expression is only formal and should really be interpreted as in (5.13). It follows from Lemma 5.19 below that the sum in (5.13) converges and that it furthermore satisfies the required bounds when tested against smooth test functions that are localised near x. Note that the map$\Pi _ { x } \mapsto \hat { \Pi } _ { x }$is linear and does not depend at all on the realisation of . As a consequence, the bound on the difference between the extensions of different regularity structures follows at once. It remains to define$\hat { \Gamma } _ { x y } \in \hat { G }$and to show that it satisfies both the algebraic and the analytical conditions given by Definition 2.17.

We set

$$
\hat {\Gamma} _ {x y} = (\Gamma_ {x y}, M _ {x y}), \qquad M _ {x y} b = \mathcal {J} (x) \Gamma_ {x y} b - \Gamma_ {x y} \mathcal {J} (y) b.\tag{5.24}
$$

By the definition of$\mathcal { I }$, the linear map$M _ { x y }$defined in this way does indeed belong to$M _ { \bar { W } } ^ { \alpha _ { n } + \beta }$. Making use of Lemma 5.16, we then have the identity

$$
\begin{array}{r l} & {\hat {\Gamma} _ {x y} \circ \hat {\Gamma} _ {y z} = \big (\Gamma_ {x y} \Gamma_ {y z}, \Gamma_ {x y} (\mathcal {J} (y) \Gamma_ {y z} - \Gamma_ {y z} \mathcal {J} (z)) + \mathcal {J} (x) \Gamma_ {x y} - \Gamma_ {x y} \mathcal {J} (y)} \\ & {\qquad + (\Gamma_ {x y} \mathcal {I} - \mathcal {I} \Gamma_ {x y}) (\Gamma_ {y z} - 1) \big)} \\ & {\qquad = \big (\Gamma_ {x z}, - \Gamma_ {x z} \mathcal {J} (z) + \Gamma_ {x y} \mathcal {J} (y) \Gamma_ {y z} + \mathcal {J} (x) \Gamma_ {x y} - \Gamma_ {x y} \mathcal {J} (y)} \\ & {\qquad + (\mathcal {J} (x) \Gamma_ {x y} - \Gamma_ {x y} \mathcal {J} (y)) (\Gamma_ {y z} - 1) \big)} \\ & {\qquad = \big (\Gamma_ {x z}, \mathcal {J} (x) \Gamma_ {x z} - \Gamma_ {x z} \mathcal {J} (z) \big),} \end{array}
$$

which is the first required algebraic identity. Regarding the second identity, we have

$$
\begin{array}{l} \hat {\Pi} _ {x} \hat {\Gamma} _ {x y} (a, b) = \hat {\Pi} _ {x} \big (\Gamma_ {x y} a + \mathcal {I} (\Gamma_ {x y} b - b) + \mathcal {J} (x) \Gamma_ {x y} b - \Gamma_ {x y} \mathcal {J} (y) b, b \big) \\ \qquad = \Pi_ {x} a + \int_ {\mathbf {R} ^ {d}} K (\cdot , z) \Pi_ {x} (\Gamma_ {x y} b - b) (d z) - \Pi_ {x} \mathcal {J} (x) (\Gamma_ {x y} b - b) \\ \qquad + \Pi_ {x} \mathcal {J} (x) \Gamma_ {x y} b - \Pi_ {y} \mathcal {J} (y) b + \int_ {\mathbf {R} ^ {d}} K (\cdot , z) \Pi_ {x} b (d z) - \Pi_ {x} \mathcal {J} (x) b \end{array}
$$

$$
\begin{array}{l} = \Pi_ {x} a + \int_ {\mathbf {R} ^ {d}} K (\cdot , z) \Pi_ {y} b (d z) - \Pi_ {y} \mathcal {J} (y) b \\ = \hat {\Pi} _ {y} (a, b). \end{array}\tag{5.25}
$$

Here, in order to go from the first to the second line, we used the fact that I realises K for$\mathcal { T }$on W by assumption.

It then only remains to check the bound on$\hat { \Gamma } _ { x y }$stated in (2.15). Since $\hat { \Gamma } _ { x y } ( a , 0 ) = ( \Gamma _ { x y } a , 0 )$, we only need to check that the required bound holds for elements of the form$( 0 , b )$. Note here that$( 0 , b ) \in \hat { T } _ { \alpha _ { n } + \beta }$, but that$( b , 0 ) \in$ $\hat { T } _ { \alpha _ { n } }$. As a consequence,

$$
\| \mathcal {I} (\Gamma_ {x y} b - b) \| _ {\gamma} = \| \Gamma_ {x y} b - b \| _ {\gamma - \beta} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\alpha_ {n} - (\gamma - \beta)} = \| x - y \| _ {\mathfrak {s}} ^ {(\alpha_ {n} + \beta) - \gamma},
$$

as required. It therefore remains to obtain a similar bound on the term$\| M _ { x y } b \| _ { \gamma }$ In view of (5.24), this on the other hand is precisely the content of Lemma 5.21 below, which concludes the proof.□

Remark 5.17 It is clear from the construction that$\hat { \mathcal T }$is the “smallest possible” extension of$\mathcal { T }$which is guaranteed to have all the required properties. In some particular cases it might however happen that there exists an even smaller extension, due to the fact that the matrices$M _ { x y }$appearing in (5.24) may have additional structure.

The remainder of this subsection is devoted to the proof of the quantitative estimates given in Lemmas 5.19 and 5.21. We will assume without further restating it that some regularity structure$\mathcal { T } = ( A , T , G )$is given and that K is a kernel satisfying Assumptions 5.1 and 5.4 for some$\beta > 0$. The test functions $K _ { n ; x y } ^ { \alpha }$introduced in (5.14) will play an important role in these bounds. Actually, we will encounter the following variant: for any multiindex k and for$\alpha \in \mathbf { R }$ set

$$
K _ {n, x y} ^ {k, \alpha} (z) = D _ {1} ^ {k} K _ {n} (y, z) - \sum_ {| k + \ell | _ {\mathfrak {s}} <   \alpha + \beta} \frac {(y - x) ^ {\ell}}{\ell !} D _ {1} ^ {k + \ell} K _ {n} (x, z),
$$

so that$K _ { n , x y } ^ { \alpha } = K _ { n , x y } ^ { 0 , \alpha }$. We then have the following bound:

Lemma 5.18 Let$K _ { n , x y } ^ { k , \alpha }$be as above,$a \in T _ { \alpha }$for some α$\in { \cal A }$, and assume that $\alpha + \beta \not \in \mathbf { N }$. Then, one has the bound

$$
\left| \left(\Pi_ {y} a\right) \left(K _ {n, x y} ^ {k, \alpha}\right) \right| \lesssim \| \Pi \| _ {\alpha ; \mathfrak {K} _ {x}} \left(1 + \| \Gamma \| _ {\alpha ; \mathfrak {K} _ {x}}\right) \sum_ {\delta > 0} 2 ^ {\delta n} \| x - y \| _ {\mathfrak {s}} ^ {\delta + \alpha + \beta - | k | _ {\mathfrak {s}}},\tag{5.26}
$$

and similarlyfor$\left| \left( \Pi _ { x } a \right) \left( K _ { n , x y } ^ { k , \alpha } \right) \right|$. Here, the sum runs overfinitely many strictly   positive values and we used the shorthand${ \mathcal { R } } _ { x }$for the ball ofradius$^ 2$centred around x. Furthermore, one has the bound

$$
\begin{array}{c} \big | \big (\Pi_ {y} - \bar {\Pi} _ {y} a \big) \big (K _ {n, x y} ^ {k, \alpha} \big) \big | \lesssim \big (\| \Pi - \bar {\Pi} \| _ {\alpha ; \mathfrak {K} _ {x}} \big (1 + \| \Gamma \| _ {\alpha ; \mathfrak {K} _ {x}} \big) \\ + \| \bar {\Pi} \| _ {\alpha ; \mathfrak {K} _ {x}} \| \Gamma - \bar {\Gamma} \| _ {\alpha ; \mathfrak {K} _ {x}} \big) \\ \times \sum_ {\delta > 0} 2 ^ {\delta n} \| x - y \| _ {\mathfrak {s}} ^ {\delta + \alpha + \beta - | k | _ {\mathfrak {s}}}, \end{array}\tag{5.27}
$$

(and similarlyfor$\Pi _ { x } - \bar { \Pi } _ { x } )$for any two models ( , ) and$( \bar { \Pi } , \bar { \Gamma } )$

Proof It turns out that the cases$\alpha + \beta > | k | _ { \mathfrak { s } }$and$\alpha + \beta \ : < \ : | k | _ { s }$are treated slightly differently. (The case$\alpha + \beta = | k | _ { \mathfrak { s } }$is ruled out by assumption.) In the case$\alpha + \beta > | k | _ { \mathfrak { s } }$, it follows from Proposition 11.1 that we can express$K _ { n ; x y } ^ { k , \alpha }$ as

$$
K _ {n; x y} ^ {k, \alpha} (z) = \sum_ {\ell \in \partial A _ {\alpha}} \int_ {\mathbf {R} ^ {d}} D _ {1} ^ {k + \ell} K _ {n} (y + h, z) \mathcal {Q} ^ {\ell} (x - y, d h),\tag{5.28}
$$

where$A _ { \alpha }$is the set of multiindices given by$A _ { \alpha } = \{ \ell : | k + \ell | _ { \mathfrak { s } } < \alpha + \beta \}$ and the objects$\partial A _ { \alpha }$and$\mathcal { Q } ^ { \ell }$are as in Proposition 11.1. In particular, note that $| \ell | _ { \mathfrak { s } } \geq \alpha + \beta - | k | _ { \mathfrak { s } }$for every term appearing in the above sum.

At this point, we note that, thanks to the first two properties in Definition 5.1, we have the bound

$$
\left| \left(\Pi_ {y} a\right) \left(D _ {1} ^ {k + \ell} K _ {n} (y, \cdot)\right) \right| \lesssim 2 ^ {| k + \ell | _ {\mathfrak {s}} n - \alpha n - \beta n} \| \Pi \| _ {\alpha ; \mathfrak {K} _ {x}},\tag{5.29}
$$

uniformly over all y with$\| y - x \| _ { \mathfrak { s } } \leq 1$and for all$a \in T _ { \alpha }$. Unfortunately, the function$\phantom { } ^ { \phantom { } } D ^ { k + \ell } K _ { n }$is evaluated at$( y + h , z )$in our case, but this can easily be remedied by shifting the model:

$$
\begin{array}{l} \left(\Pi_ {y} a\right) \left(D _ {1} ^ {k + \ell} K _ {n} (y + h, \cdot)\right) = \left(\Pi_ {y + h} \Gamma_ {y + h, x} a\right) \left(D _ {1} ^ {k + \ell} K _ {n} (y + h, \cdot)\right) \\ \lesssim \sum_ {\zeta \leq \alpha} \| h \| _ {\mathfrak {s}} ^ {\alpha - \zeta} 2 ^ {| k + \ell | _ {\mathfrak {s}} n - \zeta n - \beta n}, \end{array}\tag{5.30}
$$

where the sum runs over elements in A (in particular, it is a finite sum). In order to obtain the bound on the second line, we made use of the properties (2.15) of the model. We now use the fact that$\mathcal { Q } ^ { \ell } ( y - x , \cdot )$is supported on values h such that$\| h \| _ { \mathfrak { s } } \le \| x - y \| _ { \mathfrak { s } }$and that

$$
\mathcal {Q} ^ {\ell} (y - x, \mathbf {R} ^ {d}) \lesssim \prod_ {i = 1} ^ {d} | y _ {i} - x _ {i} | ^ {\ell_ {i}} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {| \ell | _ {\mathfrak {s}}}.\tag{5.31}
$$

Combining these bounds, it follows that one has indeed

$$
\big | \big (\Pi_ {y} a \big) \big (K _ {n; x y} ^ {k, \alpha} \big) \big | \lesssim \sum_ {\zeta ; \ell} \| x - y \| _ {\mathfrak {s}} ^ {\alpha - \zeta + | \ell | _ {\mathfrak {s}}} 2 ^ {| k + \ell | _ {\mathfrak {s}} n - \zeta n - \beta n},
$$

where the sum runs over finitely many values of$\zeta$and  with$\zeta \ \leq \ \alpha$and $| \ell | _ { \mathfrak { s } } \geq \alpha + \beta - | k | _ { \mathfrak { s } }$. Since, by assumption, one has$\alpha + \beta \not \in \mathbf { N }$, it follows that one actually has$| \ell | _ { \mathfrak { s } } > \alpha + \beta - | k | _ { \mathfrak { s } }$for each of these terms, so that the required bound follows at once. The bound with$\Pi _ { y }$replaced by$\Pi _ { x }$follows in exactly the same way as above.

In the case$\alpha + \beta < | k | _ { \mathfrak { s } }$, we have$K _ { n ; y x } ^ { k , \alpha } ( z ) = D _ { 1 } ^ { k } K _ { n } ( x , z )$and, proceeding almost exactly as above, one obtains

$$
\begin{array}{l} \big | \big (\Pi_ {x} a \big) (D _ {1} ^ {k} K _ {n} (x, \cdot)) \big | \lesssim 2 ^ {| k | _ {\mathfrak {s}} n - \alpha n - \beta n}, \\ \big | \big (\Pi_ {y} a \big) (D _ {1} ^ {k} K _ {n} (x, \cdot)) \big | \lesssim \sum_ {\zeta \leq \alpha} \| x - y \| _ {\mathfrak {s}} ^ {\alpha - \zeta} 2 ^ {| k | _ {\mathfrak {s}} n - \zeta n - \beta n}. \end{array}
$$

with proportionality constants of the required order.

Regarding the bound on the differences between two models, the proof is again virtually identical, so we do not repeat it.□

Definition 5.9 makes sense thanks to the following lemma:

Lemma 5.19 In the same setting as above, for any$\alpha \in A$with$\alpha + \beta \notin \mathbf { N } ,$ the right hand side in (5.13) with$a \in T _ { \alpha }$converges absolutely. Furthermore, one has the bound

$$
\sum_ {n \geq 0} \int_ {\mathbf {R} ^ {d}} (\Pi_ {x} a) (K _ {n; y x} ^ {\alpha})   \psi_ {x} ^ {\lambda} (y)   d y \lesssim \lambda^ {\alpha + \beta} \| \Pi \| _ {\alpha ; \mathfrak {K} _ {x}} \big (1 + \| \Gamma \| _ {\alpha ; \mathfrak {K} _ {x}} \big),\tag{5.32}
$$

uniformly over all$x \in \mathbf { R } ^ { d }$, all$\lambda \in ( 0 , 1 ]$, and all smoothfunctions supported in$B _ { \mathfrak { s } } ( 1 )$with$\| \psi \| _ { \mathcal { C } ^ { r } } \leq 1$. Here, we used the shorthand notation$\psi _ { x } ^ { \lambda } = S _ { \mathfrak { s } , x } ^ { \lambda } \psi$ and${ \mathcal { R } } _ { x }$is as above. As in Lemma 5.18, a similar bound holdsfor$\Pi _ { x } - { \bar { \Pi } } _ { x }$, but with the expressionfrom the right hand side ofthefirst line of (5.18) replaced by the expression appearing on the second line.

Remark 5.20 The condition that$\alpha + \beta \not \in \mathbf { N }$is actually known to be necessary in general. Indeed, it is possible to construct examples of functions$f \in \mathcal { C } ( \mathbf { R } ^ { 2 } )$ such that$K * f \notin \mathcal { C } ^ { \hat { 2 } } ( \mathbf { R } ^ { 2 } )$, where K denotes the Green’s function of the Laplacian [83].

Proof We treat various regimes separately. For this, we obtain separately the bounds

$$
\begin{array}{c} \big (\Pi_ {x} a \big) (K _ {n; y x} ^ {\alpha}) \lesssim \| \Pi \| _ {\alpha ; \mathfrak {K} _ {x}} \big (1 + \| \Gamma \| _ {\alpha ; \mathfrak {K} _ {x}} \big) \sum_ {\delta > 0} \| x - y \| _ {\mathfrak {s}} ^ {\alpha + \beta + \delta} 2 ^ {\delta n}, \\ \int_ {\mathbf {R} ^ {d}} \big (\Pi_ {x} a \big) (K _ {n; y x} ^ {\alpha}) \quad \psi_ {x} ^ {\lambda} (y)   d y \lesssim \| \Pi \| _ {\alpha ; \mathfrak {K} _ {x}} \sum_ {\delta > 0} \lambda^ {\alpha + \beta - \delta} 2 ^ {- \delta n}, \end{array}\tag{5.33a}
$$

(5.33b)

for$\| x - y \| _ { \mathfrak { s } } \le 1$. Both sums run over some finite set of strictly positive indices δ. Furthermore, (5.33a) holds whenever$\| x - y \| _ { 5 } \leq 2 ^ { - n }$, while (5.33b) holds whenever$2 ^ { - n } \leq \lambda$. Using the expression (5.13), it is then straightforward to show that (5.33) implies (5.32) by using the bound

$$
\int_ {\mathbf {R} ^ {d}} \| x - y \| _ {\mathfrak {s}} ^ {\gamma} \psi_ {x} ^ {\lambda} (y) d y \lesssim \lambda^ {\gamma},
$$

and summing the resulting expressions over n.

The bound (5.33a) (as well as the corresponding version for the difference between two different models for our regularity structure) is a particular case of Lemma 5.18, so we only need to consider the second bound. This bound is only useful in the regime$2 ^ { - n } \leq \lambda$, so that we assume this from now on. It turns out that in this case, the bound (5.33b) does not require the use of the identity $\Pi _ { z } = \Pi _ { x } \Gamma _ { x z }$, so that the corresponding bound on the difference between two models follows by linearity. For fixed n, it follows from the linearity of$\Pi _ { x } a$ that

$$
\int_ {\mathbf {R} ^ {d}} \bigl (\Pi_ {x} a \bigr) (K _ {n; y x} ^ {\alpha}) \psi_ {x} ^ {\lambda} (y)   d y = \bigl (\Pi_ {x} a \bigr) \biggl (\int_ {\mathbf {R} ^ {d}} K _ {n; y x} ^ {\alpha} (\cdot)   \psi_ {x} ^ {\lambda} (y)   d y \biggr).
$$

We decompose$K _ { n ; y x } ^ { \alpha }$according to (5.14) and consider the first term. It follows;<sub>from the first property in Definition 5.1 that the function</sub>

$$
Y _ {n} ^ {\lambda} (z) = \int_ {\mathbf {R} ^ {d}} K _ {n} (y, z) \psi_ {x} ^ {\lambda} (y) d y\tag{5.34}
$$

is supported in a ball of radius 2λ around x, and bounded by$C 2 ^ { - \beta n } \lambda ^ { - | \mathfrak { s } | }$for some constant C. In order to bound its derivatives, we use the fact that

$$
\begin{array}{l} D ^ {\ell} Y _ {n} ^ {\lambda} (z) = \sum_ {k <   \ell} \frac {(D ^ {k} \psi_ {x} ^ {\lambda}) (x)}{k !} \int_ {\mathbf {R} ^ {d}} D _ {2} ^ {\ell} K _ {n} (y, z)   (y - x) ^ {k}   d y \\ \qquad + \int_ {\mathbf {R} ^ {d}} D _ {2} ^ {\ell} K _ {n} (y, z)   R _ {x} (y)   d y, \end{array}
$$

where the remainder$R _ { x } ( y )$satisfies the bound$\begin{array} { r } { | R _ { x } ( y ) | \lesssim \lambda ^ { - | \mathfrak { s } | - | \ell | _ { \mathfrak { s } } } \| x - y \| _ { \mathfrak { s } } ^ { | \ell | _ { \mathfrak { s } } } } \end{array}$ Making use of (5.4) and (5.5), we thus obtain the bound

$$
\begin{array}{c} \sup _ {z \in \mathbf {R} ^ {d}} \big | D ^ {\ell} Y _ {n} ^ {\lambda} (z) \big | \lesssim \sum_ {k <   \ell} 2 ^ {- \beta n} \lambda^ {- | \mathfrak {s} | - | k | _ {\mathfrak {s}}} + 2 ^ {- \beta n} \lambda^ {- | \mathfrak {s} | - | \ell | _ {\mathfrak {s}}} \\ \lesssim 2 ^ {- \beta n} \lambda^ {- | \mathfrak {s} | - | \ell | _ {\mathfrak {s}}}. \end{array}\tag{5.35}
$$

Combining these bounds with Remark 2.21, we obtain the estimate

$$
\left| \left(\Pi_ {x} a\right) (Y _ {n} ^ {\lambda}) \right| \lesssim \lambda^ {\alpha} 2 ^ {- \beta n}.
$$

It remains to obtain a similar bound on the remaining terms in the decomposition of$K _ { n ; y x } ^ { \alpha }$. This follows if we obtain a bound analogous to (5.35), but for;<sub>the test functions</sub>

$$
Z _ {n, \ell} ^ {\lambda} (z) = D _ {1} ^ {\ell} K _ {n} (x, z) \int_ {\mathbf {R} ^ {d}} (y - x) ^ {\ell} \psi_ {x} ^ {\lambda} (y) d y.
$$

These are supported in a ball of radius$2 ^ { - n }$around x and bounded by a constant multiple of$2 ^ { ( | \ell | \varsigma + | \varsigma | - \beta ) n } \lambda ^ { | \ell | _ { \mathfrak { s } } }$. Regarding their derivatives, the bound (5.4) immediately yields

$$
\sup _ {z \in \mathbf {R} ^ {d}} \left| D ^ {k} Z _ {n, \ell} ^ {\lambda} (z) \right| \lesssim 2 ^ {(| \ell | _ {\mathfrak {s}} + | k | _ {\mathfrak {s}} + | \mathfrak {s} | - \beta) n} \lambda^ {| \ell | _ {\mathfrak {s}}}.
$$

Combining these bounds again with Remark 2.21 yields the estimate

$$
\left| \left(\Pi_ {x} a\right) (Z _ {n, \ell} ^ {\lambda}) \right| \lesssim 2 ^ {(| \ell | _ {\mathfrak {s}} - \alpha - \beta) n} \lambda^ {| \ell | _ {\mathfrak {s}}}.
$$

Since the indices  appearing in (5.14) all satisfy$| \ell | _ { \mathfrak { s } } < \alpha + \beta$, the bound (5.33b) does indeed hold for some finite collection of strictly positive indices δ.□

The following lemma is the last ingredient required for the proof of the extension theorem. In order to state it, we make use of the shorthand notation

$$
\mathcal {J} _ {x y} \stackrel {{\text { def }}} {{=}} \mathcal {J} (x) \Gamma_ {x y} - \Gamma_ {x y} \mathcal {J} (y),\tag{5.36}
$$

where, given a regularity structure$\mathcal { T }$and a model ( , ), the map$\mathcal { I }$was defined in (5.11).

Lemma 5.21 Let$V ~ \subset ~ T$be a sector satisfying the same assumptions as in Theorem 5.14. Then, for every$\alpha \in A , a \in V _ { \alpha }$, every multiindex k with $| k | _ { \mathfrak { s } } < \alpha + \beta$, and every pair$( x , y )$with$\| x - y \| _ { \mathfrak { s } } \leq 1$, one has the bound

$$
\big | \big (\mathcal {J} _ {x y} a \big) _ {k} \big | \lesssim \| \Pi \| _ {\alpha ; \mathfrak {K} _ {x}} \big (1 + \| \Gamma \| _ {\alpha ; \mathfrak {K} _ {x}} \big) \| x - y \| _ {\mathfrak {s}} ^ {\alpha + \beta - | k | _ {\mathfrak {s}}},\tag{5.37}
$$

where${ \mathcal { R } } _ { x }$is as before. Furthermore, if we denote by${ \bar { \mathcal { I } } } _ { x y }$thefunction defined like (5.36), but with respect to a second model$( \bar { \Pi } , \bar { \Gamma } )$, then we obtain a bound similar to (5.37) on the difference$\mathcal { T } _ { x y } a - \bar { \mathcal { T } } _ { x y } a$, again with the expression from the right hand side of the first line of (5.18) replaced by the expression appearing on the second line.

Proof For any multiindex k with$| k | _ { \mathfrak { s } } < \alpha + \beta$, we can rewrite the kth component of$\mathcal { I } _ { x y } a$as

$$
\begin{array}{l} \big (\mathcal {J} _ {x y} a \big) _ {k} = \frac {1}{k !} \sum_ {n \geq 0} \left(\sum_ {| k | _ {\mathfrak {s}} - \beta <   \gamma \leq \alpha} \big (\Pi_ {x} \mathcal {Q} _ {\gamma} \Gamma_ {x y} a \big) \big (D _ {1} ^ {k} K _ {n} (x, \cdot) \big) \right. \\ \left. - \sum_ {| \ell | _ {\mathfrak {s}} <   \alpha + \beta - | k | _ {\mathfrak {s}}} \frac {(x - y) ^ {\ell}}{\ell !} \big (\Pi_ {y} a \big) \big (D _ {1} ^ {k + \ell} K _ {n} (y, \cdot) \big)\right) \\ \stackrel {{\mathrm{def}}} {{=}} \frac {1}{k !} \sum_ {n \geq 0} \mathcal {J} _ {x y} ^ {n, k} a. \end{array}\tag{5.38}
$$

As usual, we treat separately the cases$\| x - y \| _ { \mathfrak { s } } \leq 2 ^ { - n }$and$\| x - y \| _ { 5 } \geq 2 ^ { - n }$ In the case$\| x - y \| _ { \mathfrak { s } } \leq 2 ^ { - n }$, we rewrite$\mathcal { T } _ { x y } ^ { n , k } a$as

$$
\mathcal {J} _ {x y} ^ {n, k} a = \left(\Pi_ {y} a\right) \left(K _ {n; x y} ^ {k, \alpha}\right) - \sum_ {\gamma \leq | k | _ {5} - \beta} \left(\Pi_ {x} \mathcal {Q} _ {\gamma} \Gamma_ {x y} a\right) \left(D _ {1} ^ {k} K _ {n} (x, \cdot)\right).\tag{5.39}
$$

The first term has already been bounded in Lemma 5.18, yielding a bound of the type (5.37) when summing over the relevant values of n. Regarding the second term, we make use of the fact that, for$\gamma < \alpha$(which is satisfied since $| k | _ { \mathfrak { s } } < \alpha + \beta )$, one has the bound$\| \Gamma _ { x y } a \| _ { \gamma } \lesssim \| x - y \| _ { \mathfrak { s } } ^ { \alpha - \gamma }$. Furthermore, for any$b \in T _ { \gamma }$, one has

$$
\left(\Pi_ {x} b\right) \left(D _ {x} ^ {k} K _ {n} (x, \cdot)\right) \lesssim \| b \| 2 ^ {\left(| k | _ {\mathfrak {s}} - \beta - \gamma\right) n}.\tag{5.40}
$$

In principle, the exponent appearing in this term might vanish. As a consequence of our assumptions, this however cannot happen. Indeed, if$\gamma$is such that$\gamma + \beta = | k | _ { \mathfrak { s } }$, then we necessarily have that$\gamma$itself is an integer. By Assumptions 5.3 and 5.4 however, we have the identity

$$
\left(\Pi_ {x} b\right) \left(D _ {x} ^ {k} K _ {n} (x, \cdot)\right) = 0,
$$

for every b with integer homogeneity.

Combining all these bounds, we thus obtain similarly to before the bound

$$
\left| \mathcal {J} _ {x y} ^ {n, k} a \right| \lesssim \| \Pi \| _ {\alpha ; \mathfrak {K} _ {x}} \big (1 + \| \Gamma \| _ {\alpha ; \mathfrak {K} _ {x}} \big) \sum_ {\delta > 0} \| x - y \| _ {\mathfrak {s}} ^ {\alpha + \beta - | k | _ {\mathfrak {s}} + \delta} 2 ^ {\delta n},\tag{5.41}
$$

where the sum runs over a finite number of exponents. This expression is valid for all$n \geq 0$with$\| x - y \| _ { 5 } \leq 2 ^ { - n }$. Furthermore, if we consider two different models ( , ) and ( , ) , we obtain a similar bound on the difference$\mathcal { T } _ { x y } ^ { n , k } a -$ ${ \bar { \mathcal { I } } } _ { x y } ^ { n , k } a$

In the case$\| x - y \| _ { \mathfrak { s } } \geq 2 ^ { - n }$, we treat the two terms in (5.38) separately and, for both cases, we make use of the bound (5.40). As a consequence, we obtain

$$
\begin{array}{l} \left| \mathcal {J} _ {x y} ^ {n, k} a \right| \lesssim \sum_ {| k | _ {\mathfrak {s}} - \beta <   \gamma \leq \alpha} \| x - y \| _ {\mathfrak {s}} ^ {\alpha - \gamma} 2 ^ {(| k | _ {\mathfrak {s}} - \beta - \gamma) n} \\ \qquad + \sum_ {| \ell | _ {\mathfrak {s}} <   \alpha + \beta - | k | _ {\mathfrak {s}}} \| x - y \| _ {\mathfrak {s}} ^ {| \ell | _ {\mathfrak {s}}} 2 ^ {(| k | _ {\mathfrak {s}} + | \ell | _ {\mathfrak {s}} - \beta - \alpha) n}, \end{array}
$$

with a proportionality constant as before. Thanks to our assumptions, the exponent of$2 ^ { n }$appearing in each of these terms is always strictly negative. We thus obtain a bound like (5.41), but where the sum now runs over a finite number of exponents δ with$\delta < 0$. Summing both bounds over n, we see that (5.37) does indeed hold for$\mathcal { I } _ { x y }$. In this case, the bound on the difference again simply holds by linearity.□

## 5.2 Multi-level Schauder estimate

We now have all the ingredients in place to prove the “multi-level Schauder estimate” announced at the beginning of this section. Our proof has a similar flavour to proofs of the classical (elliptic or parabolic) Schauder estimates using scale-invariance, like for example [93].

ProofofTheorem 5.12 We first note that (5.16) is well-defined for every k with$| k | _ { \mathfrak { s } } < \gamma + \beta$. Indeed, it follows from the reconstruction theorem and the assumptions on K that

$$
\big (\mathcal {R} f - \Pi_ {x} f (x) \big) \big (D _ {1} ^ {k} K _ {n} (x, \cdot) \big) \lesssim 2 ^ {(| k | _ {\mathfrak {s}} - \beta - \gamma) n},\tag{5.42}
$$

which is summable since the exponent appearing in this expression is strictly negative. Regarding$\kappa _ { \gamma } f - \bar { \kappa } _ { \gamma } \bar { f }$, we use (3.4), which yields

$$
\begin{array}{l} \big | \big (\mathcal {R} f - \bar {\mathcal {R}} \bar {f} - \Pi_ {x} f (x) + \bar {\Pi} _ {x} \bar {f} (x) \big) \big (D _ {1} ^ {k} K _ {n} (x, \cdot) \big) \big | \\ \lesssim 2 ^ {(| k | _ {\mathfrak {s}} - \beta - \gamma) n} \big (\| f; \bar {f} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}} \big), \end{array}\tag{5.43}
$$

where the proportionality constants depend on the bounds on$f , { \bar { f } } .$, and the two models. In particular, this already shows that one has the bounds

$$
\begin{array}{r l} & {\| \mathcal {K} _ {\gamma} f \| _ {\gamma + \beta ; \mathfrak {K}} \lesssim \| f \| _ {\gamma ; \bar {\mathfrak {K}}},} \\ & {\| \mathcal {K} _ {\gamma} f - \bar {\mathcal {K}} _ {\gamma} \bar {f} \| _ {\gamma + \beta ; \mathfrak {K}} \lesssim \| f; \bar {f} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}},} \end{array}
$$

so that it remains to obtain suitable bounds on differences between two points.

We also note that by the definition of$\kappa _ { \gamma }$and the properties of$\mathcal { T } _ { : }$, one has for$\ell \not \in \mathbf { N }$the bound

$$
\begin{array}{c} \| \mathcal {K} _ {\gamma} f (x) - \Gamma_ {x y} \mathcal {K} _ {\gamma} f (y) \| _ {\ell} = \| \mathcal {I} \big (f (x) - \Gamma_ {x y} f (y) \big) \| _ {\ell} \lesssim \| f (x) - \Gamma_ {x y} f (y) \| _ {\ell - \beta} \\ \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma + \beta - \ell}, \end{array}
$$

which is precisely the required bound. A similar calculation allows to bound the terms involved in the definition of$\| \mathcal { K } _ { \gamma } f ; \bar { \mathcal { K } } _ { \gamma } \bar { f } \| _ { \gamma + \beta ; \mathcal { R } } .$, so that it remains to show a similar bound for$\boldsymbol { \ell } \in \mathbf { N }$

It follows from (5.19), combined with the fact that$\mathcal { T }$does not produce any component in$\bar { T }$by assumption, that one has the identity

$$
\begin{array}{r} \big (\Gamma_ {x y} \mathcal {K} _ {\gamma} f (y) \big) _ {k} - \big (\mathcal {K} _ {\gamma} f (x) \big) _ {k} = \big (\Gamma_ {x y} \mathcal {N} _ {\gamma} f (y) \big) _ {k} - \big (\mathcal {N} _ {\gamma} f (x) \big) _ {k} \\ + \big (\mathcal {J} (x) \big (\Gamma_ {x y} f (y) - f (x) \big) \big) _ {k}, \end{array}
$$

so our aim is to bound this expression. We decompose$\mathcal { I }$as$\begin{array} { r } { \mathcal { I } = \sum _ { n > 0 } \mathcal { I } ^ { ( n ) } } \end{array}$ and$\begin{array} { r } { \mathcal { N } _ { \gamma } = \sum _ { n > 0 } \mathcal { N } _ { \gamma } ^ { ( n ) } } \end{array}$, where the nth term in each sum is obtained by replacing K by$K _ { n }$in the expressions for$\mathcal { I }$and$\mathcal { N } _ { \gamma }$respectively. It follows from the definition of$\mathcal { N } _ { \gamma }$, as well as the action of$\Gamma$on the space of elementary polynomials that one has the identities

$$
\begin{array}{l} \left(\Gamma_ {x y} \mathcal {N} _ {\gamma} ^ {(n)} f (y)\right) _ {k} = \frac {1}{k !} \sum_ {| k + \ell | _ {\mathfrak {s}} <   \gamma + \beta} \frac {(x - y) ^ {\ell}}{\ell !} \left(\mathcal {R} f - \Pi_ {y} f (y)\right) \left(D _ {1} ^ {k + \ell} K _ {n} (y, \cdot)\right), \\ \left(\mathcal {J} ^ {(n)} (x) \Gamma_ {x y} f (y)\right) _ {k} = \frac {1}{k !} \sum_ {\delta \in B _ {k}} \left(\Pi_ {x} \mathcal {Q} _ {\delta} \Gamma_ {x y} f (y)\right) \left(D _ {1} ^ {k} K _ {n} (x, \cdot)\right), \\ \left(\mathcal {J} ^ {(n)} (x) f (x)\right) _ {k} = \frac {1}{k !} \sum_ {\delta \in B _ {k}} \left(\Pi_ {x} \mathcal {Q} _ {\delta} f (x)\right) \left(D _ {1} ^ {k} K _ {n} (x, \cdot)\right), \end{array} \tag {5}\tag{5.44}
$$

where the set$B _ { k }$is given by

$$
B _ {k} = \{\delta \in A: | k | _ {\mathfrak {s}} - \beta <   \delta <   \gamma \}.
$$

(The upper bound$\gamma$appearing in$B _ { k }$actually has no effect since, by assumption,$f$has no component in$T _ { \delta }$for$\delta \geq \gamma . )$As previously, we use different strategies for small scales and for large scales.

We first bound the terms at small scales, i.e. when$2 ^ { - n } \leq \| x -$ $y \Vdash$. In this case, we bound separately the terms$\mathcal { N } _ { \gamma } ^ { ( n ) } f , \ \Gamma _ { x y } \mathcal { N } _ { \gamma } ^ { ( n ) } f$, and $\mathcal { T } ^ { ( n ) } ( x ) ( \Gamma _ { x y } f ( y ) - f ( x ) )$. In order to bound the distance between$\kappa _ { \gamma } f$and $\bar { \kappa } _ { \gamma } \bar { f }$, we also need to obtain similar bounds on$\mathcal { N } _ { \gamma } ^ { ( n ) } f - \bar { \mathcal { N } } _ { \gamma } ^ { ( n ) } \bar { f } , \Gamma _ { x y } \mathcal { N } _ { \gamma } ^ { ( n ) } f -$ $\bar { \Gamma } _ { x y } \bar { \mathcal { N } } _ { \gamma } ^ { ( n ) } \bar { f } .$, as well as$\mathcal { T } ^ { ( n ) } ( x ) ( \Gamma _ { x y } f ( y ) - f ( x ) ) - \bar { \mathcal { T } } ^ { ( n ) } ( x ) ( \bar { \Gamma } _ { x y } \bar { f } ( y ) - \bar { f } ( x ) )$ Here, we denote by$\bar { \mathcal { I } }$the same function as$\mathcal { I }$, but defined from the model ( , ) . The same holds for$\bar { \mathcal { N } } _ { \gamma }$

Recall from (5.42) that we have for$\mathcal { N } _ { \gamma } ^ { ( n ) } f$the bound

$$
\big | \big (\mathcal {N} _ {\gamma} ^ {(n)} f (x) \big) _ {k} \big | \lesssim 2 ^ {(| k | _ {\mathfrak {s}} - \beta - \gamma) n},\tag{5.45}
$$

so that, since we only consider indices k such that$| k | _ { \mathfrak { s } } - \beta - \gamma < 0$, one obtains

$$
\sum_ {n: 2 ^ {- n} \leq \| x - y \| _ {\mathfrak {s}}} \big | \big (\mathcal {N} _ {\gamma} ^ {(n)} f (x) \big) _ {k} \big | \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\beta + \gamma - | k | _ {\mathfrak {s}}},
$$

as required. In the same way, we obtain the bound

$$
\begin{array}{l} \sum_ {n: 2 ^ {- n} \leq \| x - y \| _ {\mathfrak {s}}} \big | \big (\mathcal {N} _ {\gamma} ^ {(n)} f (x) - \bar {\mathcal {N}} _ {\gamma} ^ {(n)} \bar {f} (x) \big) _ {k} \big | \\ \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\beta + \gamma - | k | _ {\mathfrak {s}}} \big (\| f;   \bar {f} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}} \big), \end{array}
$$

where we made use of (5.43) instead of (5.42).

Similarly, we obtain for$( \Gamma _ { x y } \mathcal { N } _ { \gamma } ^ { ( n ) } f ( y ) ) _ { k }$the bound

$$
\big | \big (\Gamma_ {x y} \mathcal {N} _ {\gamma} ^ {(n)} f (y) \big) _ {k} \big | \lesssim \sum_ {| k + \ell | _ {\mathfrak {s}} <   \gamma + \beta} \| x - y \| _ {\mathfrak {s}} ^ {| \ell | _ {\mathfrak {s}}} 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - \gamma) n}.
$$

Summing over values of n with$2 ^ { - n } \leq \| x - y \| _ { \mathfrak { s } } ,$we can bound this term again by a multiple of$\| x - y \| _ { \mathfrak { s } } ^ { \beta + \gamma - | k | _ { \mathfrak { s } } }$. In virtually the same way, we obtain the bound

$$
\begin{array}{r l} & {\big | \big (\Gamma_ {x y} \mathcal {N} _ {\gamma} ^ {(n)} f - \bar {\Gamma} _ {x y} \bar {\mathcal {N}} _ {\gamma} ^ {(n)} \bar {f} \big) _ {k} \big |} \\ & {\lesssim \| x - y \| _ {\mathfrak {s}} ^ {\beta + \gamma - | k | _ {\mathfrak {s}}} \big (\| f; \bar {f} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma + \beta ; \bar {\mathfrak {K}}} \big),} \end{array}
$$

where rewrote the left hand side as$( \Gamma _ { x y } - \bar { \Gamma } _ { x y } ) \mathcal { N } _ { \gamma } ^ { ( n ) } f + \bar { \Gamma } _ { x y } \big ( \bar { \mathcal { N } } _ { \gamma } ^ { ( n ) } \bar { f } - \mathcal { N } _ { \gamma } ^ { ( n ) } f \big )$ and then proceeded to bound both terms as above.

We now turn to the term involving${ \mathcal { I } } ^ { ( n ) }$. From the definition of${ \mathcal { I } } ^ { ( n ) }$, we then obtain the bound

$$
\begin{array}{l} \left| \left(\mathcal {J} ^ {(n)} (x) (\Gamma_ {x y} f (y) - f (x))\right) _ {k} \right| = \sum_ {\delta \in B _ {k}} \left(\Pi_ {x} \mathcal {Q} _ {\delta} \left(\Gamma_ {x y} f (y) - f (x)\right)\right) \left(D _ {1} ^ {k} K _ {n} (x, \cdot)\right) \\ \lesssim \sum_ {\delta \in B _ {k}} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \delta} 2 ^ {(| k | _ {\mathfrak {s}} - \beta - \delta) n}. \end{array} \tag {5.46}
$$

It follows from the definition of$B _ { k }$that$| k | _ { \mathfrak { s } } - \beta - \delta < 0$for every term appearing in this sum. As a consequence, summing over all n such that$2 ^ { - n } \leq$ $\| x - y \| _ { \mathfrak { s } }$, we obtain a bound ofthe order$\| x - y \| _ { \mathfrak { s } } ^ { \gamma + \widetilde { \beta - } | k | _ { \mathfrak { s } } }$as required. Regarding the corresponding term arising in$\kappa _ { \gamma } f - \bar { \kappa } _ { \gamma } \bar { f }$, we use the identity

$$
\begin{array}{l} \Pi_ {x} \mathcal {Q} _ {\delta} \big (\Gamma_ {x y} f (y) - f (x) \big) - \bar {\Pi} _ {x} \mathcal {Q} _ {\delta} \big (\bar {\Gamma} _ {x y} \bar {f} (y) - \bar {f} (x) \big) \\ = \big (\Pi_ {x} - \bar {\Pi} _ {x} \big) \mathcal {Q} _ {\delta} \big (\Gamma_ {x y} f (y) - f (x) \big) \\ + \bar {\Pi} _ {x} \mathcal {Q} _ {\delta} \big (\bar {f} (x) - f (x) - \bar {\Gamma} _ {x y} \bar {f} (y) + \Gamma_ {x y} f (y) \big), \end{array}\tag{5.47}
$$

and we bound both terms separately in the same way as above, making use of the definition of$\| f ; { \bar { f } } \| _ { \gamma ; { \bar { \mathcal { R } } } }$in order to control the second term.

It remains to obtain similar bounds on large scales, i.e. in the regime$2 ^ { - n } \geq$ $\| x - y \| _ { \mathfrak { s } }$. We define

$$
\begin{array}{l} \mathcal {T} _ {1} ^ {k} \stackrel {{\text { def }}} {{=}} - k! \big (\big (\mathcal {N} _ {\gamma} ^ {(n)} f \big) (x) + \mathcal {J} ^ {(n)} (x) f (x) \big) _ {k}, \\ \mathcal {T} _ {2} ^ {k} \stackrel {{\text { def }}} {{=}} k! \big (\big (\Gamma_ {x y} \mathcal {N} _ {\gamma} ^ {(n)} f \big) (y) + \mathcal {J} ^ {(n)} (x) \Gamma_ {x y} f (y) \big) _ {k}. \end{array}
$$

Inspecting the definitions of these terms, we then obtain the identities

$$
\begin{array}{l} \mathcal {T} _ {1} ^ {k} = \Big (\sum_ {\zeta \leq | k | _ {\mathfrak {s}} - \beta} \Pi_ {x} \mathcal {Q} _ {\zeta} f (x) - \mathcal {R} f \Big) \big (D _ {1} ^ {k} K _ {n} (x, \cdot) \big), \\ \mathcal {T} _ {2} ^ {k} = \sum_ {\zeta > | k | _ {\mathfrak {s}} - \beta} \big (\Pi_ {x} \mathcal {Q} _ {\zeta} \Gamma_ {x y} f (y) \big) \big (D _ {1} ^ {k} K _ {n} (x, \cdot) \big) \\ - \sum_ {| k + \ell | _ {\mathfrak {s}} <   \gamma + \beta} \frac {(x - y) ^ {\ell}}{\ell !} \big (\Pi_ {y} f (y) - \mathcal {R} f \big) \big (D _ {1} ^ {k + \ell} K _ {n} (y, \cdot) \big). \end{array}
$$

Adding these two terms, we have

$$
\begin{array}{l} \mathcal {T} _ {2} ^ {k} + \mathcal {T} _ {1} ^ {k} = \big (\Pi_ {y} f (y) - \mathcal {R} f \big) \big (K _ {n; x y} ^ {k, \gamma} \big) \\ \qquad - \sum_ {\zeta \leq | k | _ {\mathfrak {s}} - \beta} \big (\Pi_ {x} \mathcal {Q} _ {\zeta} \big (\Gamma_ {x y} f (y) - f (x) \big) \big) \big (D _ {1} ^ {k} K _ {n} (x, \cdot) \big). \end{array}\tag{5.48}
$$

In order to bound the first term, we proceed similarly to the proof of the second part of Lemma 5.18. The only difference is that the analogue to the left hand side of (5.30) is now given by

$$
\begin{array}{l} \big (\Pi_ {y} f (y) - \mathcal {R} f \big) \left(D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot)\right) = \big (\Pi_ {\bar {y}} f (\bar {y}) - \mathcal {R} f \big) \big (D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot) \big) \\ \qquad + \big (\Pi_ {\bar {y}} \big (\Gamma_ {\bar {y} y} f (y) - f (\bar {y}) \big) \big) \big (D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot) \big), \end{array}\tag{5.49}
$$

where we set${ \bar { y } } = y + h$. Regarding the first term in this expression, recall from (5.42) that

$$
\left| \left(\Pi_ {\bar {y}} f (\bar {y}) - \mathcal {R} f\right) \left(D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot)\right) \right| \lesssim 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - \gamma) n}.
$$

Since$\beta + \gamma \notin \mathbf { N }$by assumption, the exponent appearing in this expression is always strictly positive, thus yielding the required bound. The corresponding bound on$\kappa _ { \gamma } f - \bar { \kappa } _ { \gamma } \bar { f }$is obtained in the same way, but making use of (5.43) instead of (5.42).

To bound the second term in (5.49), we use the fact that$f \in \mathcal { D } ^ { \gamma }$which yields

$$
\left| \left(\Pi_ {\bar {y}} \left(\Gamma_ {\bar {y} y} f (y) - f (\bar {y})\right)\right) \left(D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot)\right) \right| \lesssim \sum_ {\zeta \leq \gamma} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \zeta} 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \zeta - \beta) n}.
$$

We thus obtain a bound analogous to (5.30), with α replaced by$\gamma .$. Proceeding analogously to (5.47), we obtain a similar bound (but with a prefactor $\| \Gamma - \bar { \Gamma } \| _ { \gamma + \beta ; \bar { \mathcal { R } } } + \| f ; \bar { f } \| _ { \gamma ; \bar { \mathcal { R } } } )$for the corresponding term appearing in the difference between$\kappa _ { \gamma } f$and$\bar { \kappa } _ { \gamma } \bar { f }$. Proceeding as in the remainder of the proof of Lemma 5.18, we then obtain the bound

$$
\big | \big (\Pi_ {y} f (y) - \mathcal {R} f \big) \big (K _ {n; x y} ^ {k, \gamma} \big) \big | \lesssim \sum_ {\delta > 0} 2 ^ {\delta n} \| x - y \| _ {\mathfrak {s}} ^ {\delta + \gamma + \beta - | k | _ {\mathfrak {s}}},\tag{5.50}
$$

where the sum runs only over finitely many values of$\delta$. The corresponding bound for the difference is obtained in the same way.

Regarding the second term in (5.48), we obtain the bound

$$
\left| \left(\Pi_ {x} \mathcal {Q} _ {\zeta} \left(\Gamma_ {x y} f (y) - f (x)\right)\right) \left(D _ {1} ^ {k} K _ {n} (x, \cdot)\right) \right| \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \zeta} 2 ^ {(| k | _ {\mathfrak {s}} - \beta - \zeta) n}.
$$

At this stage, one might again have summability problems if$\zeta = | k | _ { \mathfrak { s } } - \beta$ However, just as in the proof of Lemma 5.21, our assumptions guarantee that such terms do not contribute. Summing both of these bounds over the relevant values of n, the requested bound follows at once. Again, the corresponding term involved in the difference can be bounded in the same way, by making use of the decomposition (5.47).

It remains to show that the identity (5.17) holds. Actually, by the uniqueness part of the reconstruction theorem, it suffices to show that, for any suitable test function$\psi$and any$x \in D$, one has

$$
\bigl (\Pi_ {x} \mathcal {K} f (x) - K * \mathcal {R} f \bigr) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\lambda} \psi) \lesssim \lambda^ {\delta},
$$

for some strictly positive exponent δ. Writing$\psi _ { x } ^ { \lambda } = S _ { \mathfrak { s } , x } ^ { \lambda } \psi$as a shorthand, we obtain the identity

$$
\begin{array}{l} \big (\Pi_ {x} \mathcal {K} f (x) - K * \mathcal {R} f \big) (\psi_ {x} ^ {\lambda}) \\ = \sum_ {n \geq 0} \int \left(\sum_ {\zeta \in A} \big (\Pi_ {x} \mathcal {Q} _ {\zeta} f (x) \big) \Big (K _ {n} (y, \cdot) - \sum_ {| \ell | _ {\mathfrak {s}} <   \zeta + \beta} \frac {(y - x) ^ {\ell}}{\ell !} D _ {1} ^ {\ell} K _ {n} (x, \cdot)\right) \\ + \sum_ {\zeta \in A} \sum_ {| \ell | _ {\mathfrak {s}} <   \zeta + \beta} \frac {(y - x) ^ {\ell}}{\ell !} \big (\Pi_ {x} \mathcal {Q} _ {\zeta} f (x) \big) \big (D _ {1} ^ {\ell} K _ {n} (x, \cdot) \big) \\ + \sum_ {| k | _ {\mathfrak {s}} <   \gamma + \beta} \frac {(y - x) ^ {k}}{k !} \big (\mathcal {R} f - \Pi_ {x} f (x) \big) \big (D _ {1} ^ {k} K _ {n} (x, \cdot) \big) \\ - \big (\mathcal {R} f \big) \big (K _ {n} (y, \cdot) \big) \Big) \psi_ {x} ^ {\lambda} (y) d y \\ = \sum_ {n \geq 0} \int \big (\Pi_ {x} f (x) - \mathcal {R} f \big) (K _ {n; y x} ^ {\gamma}) \psi_ {x} ^ {\lambda} (y) d y. \end{array}
$$

It thus remains to obtain a suitable bound on$\bigl ( \Pi _ { x } f ( x ) - \mathscr { R } f \bigr ) ( K _ { n ; y x } ^ { \gamma } )$. As is by now usual, we treat separately the cases$2 ^ { - n } \lessgtr \lambda$

In the case$2 ^ { - n } \geq \lambda$, we already obtained the bound (5.50) (with$k = 0 )$ which yields a bound of the order of$\lambda ^ { \gamma + \beta }$when summed over n and integrated against$\psi _ { x } ^ { \lambda }$. In the case$2 ^ { - n } \leq \lambda$, we rewrite$K _ { n ; y x } ^ { \gamma }$as

$$
K _ {n; y x} ^ {\gamma} = K _ {n} (y, \cdot) - \sum_ {| \ell | _ {\mathfrak {s}} <   \gamma + \beta} \frac {(y - x) ^ {\ell}}{\ell !} D _ {x} ^ {\ell} K _ {n} (x, \cdot),\tag{5.51}
$$

and we bound the resulting terms separately. To bound the terms involving derivatives of$K _ { n }$, we note that, as a consequence ofthe reconstruction theorem, we have the bound

$$
\big | \big (\Pi_ {y} f (y) - \mathcal {R} f \big) \big (D _ {x} ^ {\ell} K _ {n} (x, \cdot) \big) \big | \lesssim 2 ^ {(| \ell | _ {\mathfrak {s}} - \beta - \gamma) n}.
$$

Since this exponent is always strictly negative (because$\gamma + \beta \not \in \mathbf { N }$by assumption), this term is summable for large n. After summation and integration against$\psi _ { x } ^ { \lambda }$, we indeed obtain a bound of the order of$\lambda ^ { \gamma + \beta }$as required.

To bound the expression arising from the first term in (5.51), we rewrite it as

$$
\int \bigl (\Pi_ {x} f (x) - \mathcal {R} f \bigr) \bigl (K _ {n} (y, \cdot) \bigr) \psi_ {x} ^ {\lambda} (y) d y = \bigl (\Pi_ {x} f (x) - \mathcal {R} f \bigr) \bigl (Y _ {n} ^ {\lambda} \bigr),
$$

where$Y _ { n } ^ { \lambda }$is as in (5.34). It then follows from (5.35), combined with the reconstruction theorem, that

$$
\left| \left(\Pi_ {x} f (x) - \mathcal {R} f\right) \left(Y _ {n} ^ {\lambda}\right) \right| \lesssim 2 ^ {- \beta n} \lambda^ {\gamma}.
$$

Summing over all n with$2 ^ { - n } \leq \lambda$, we obtain again a bound of the order$\lambda ^ { \gamma + \beta }$, which concludes the proof.□

Remark 5.22 Alternatively, it is also possible to prove the multi-level Schauder estimate as a consequence of the extension and the reconstruction theorems. The argument goes as follows: first, we add to T one additional “abstract” element b which we decree to be of homogeneity$\gamma$. We then extend the representation ( , ) to b by setting

$$
\Pi_ {x} b \stackrel {{\text { def }}} {{=}} \mathcal {R} f - \Pi_ {x} f (x), \quad \Gamma_ {x y} b - b \stackrel {{\text { def }}} {{=}} f (x) - \Gamma_ {x y} f (y).
$$

(Of course the group G has to be suitable extended to ensure the second identity.) It is an easy exercise to verify that this satisfies the required algebraic identities. Furthermore, the required analytical bounds on are satisfied as a consequence of the reconstruction theorem, while the bounds on  are satisfied by the definition of$\mathcal { D } ^ { \gamma }$

Setting${ \hat { F } } ( x ) = f ( x ) + b$, it then follows immediately from the definitions that$\Pi _ { x } { \hat { F } } ( x ) = { \mathcal { R } } f$for every x. One can then apply the extension theorem to construct an element$\mathcal { T } b$such that (5.12) holds. In particular, this shows that the function$\hat { F }$given by

$$
\hat {F} (x) = \mathcal {I} \hat {F} (x) + \mathcal {J} (x) \hat {F} (x),
$$

satisfies$\Pi _ { x } \hat { F } ( x ) = K * \mathcal { R } f$for every x. Noting that$\Gamma _ { x y } \hat { F } ( x ) = \hat { F } ( y )$, it is then possible to show that on the one hand the map$x \mapsto { \hat { F } } ( x ) - { \mathcal { T } } b$belongs to$\mathcal { D } ^ { \bar { \gamma } + \beta }$, and that on the other hand one has$\bar { F } ( x ) ^ { \top } - \mathcal { T } b = \bigl ( \mathcal { K } _ { \gamma } f \bigr ) ( x )$, so the claim follows.

The reason for providing the longer proof is twofold. First, it is more direct and therefore gives a “reality check” of the rather abstract construction performed in the extension theorem. Second, the direct proof extends to the case of singular modelled distributions considered in Sect. 6 below, while the short argument given above does not.

## 5.3 The symmetric case

If we are in the situation of some symmetry group$\mathcal { S }$acting on$\mathcal { T }$as in Sect. 3.6, then it is natural to impose that K is also symmetric in the sense that $K ( T _ { g } x , T _ { g } y ) = K ( x , y )$, and that the abstract integration map$\mathcal { T }$commutes with the action of$\mathcal { S }$in the sense that$M _ { g } \mathcal { I } = \mathcal { I } M _ { g }$for every$g \in \mathcal { S }$

One then has the following result:

Proposition 5.23 In the setting of Theorem 5.12, assume furthermore that a discrete symmetry group$\mathcal { S }$acts on$\mathbf { R } ^ { d }$and on$\mathcal { T }$, that K is symmetric under this action, that ( , ) is adapted to it, and that I commutes with it. Then,$i f$ $f \in { \mathcal { D } } ^ { \gamma }$is symmetric, so is$\kappa _ { \gamma } f$

Proof For$g \in \mathcal { S }$, we write again its action on$\mathbf { R } ^ { d }$as$T _ { g } x = A _ { g } x + b _ { g }$. We want to verify that$M _ { g } ( { K _ { \gamma } f } ) ( T _ { g } x ) = ( K _ { \gamma } f ) ( x )$. Actually, this identity holds true separately for the three terms that make up$\kappa _ { \gamma } f$in (5.15).

For the first term, this holds by our assumption on$\mathcal { T }$. To treat the second term, recall Remark 3.37. With the notation used there, we have the identity

$$
M _ {g} \mathcal {J} (T _ {g} x) a = \sum_ {| k | _ {\mathfrak {s}} \leq \alpha} \frac {(A _ {g} X) ^ {k}}{k !} \int D _ {1} ^ {k} K (T _ {g} x, z) (\Pi_ {T _ {g} x} a) (d z)
$$

$$
\begin{array}{l} = \sum_ {| k | _ {\mathfrak {s}} \leq \alpha} \frac {(A _ {g} X) ^ {k}}{k !} \int D _ {1} ^ {k} K (T _ {g} x, T _ {g} z) (\Pi_ {x} M _ {g} a) (d z) \\ = \sum_ {| k | _ {\mathfrak {s}} \leq \alpha} \frac {X ^ {k}}{k !} \int D _ {1} ^ {k} K (x, z) (\Pi_ {x} M _ {g} a) (d z) = \mathcal {J} (x) M _ {g} a, \end{array}
$$

as required. Here, we made use of the symmetry of$K$, combined with the fact that$A _ { g }$is an orthogonal matrix, to go from the second line to the third. The last term is treated similarly by exploiting the symmetry of$\mathcal { R } f$given by Proposition 3.38.□

Finally, one has

Lemma 5.24 In the setting ofLemma 5.5,$i f { \bar { K } }$is symmetric, then it is possible to choose the decomposition${ \bar { K } } = K + R$in such a way that both K and R are symmetric.

Proof Denote by$\mathcal { G }$the crystallographic point group associated to$\mathcal { S }$. Then, given any decomposition$\bar { K } = K _ { 0 } + R _ { 0 }$given by Lemma 5.5, it suffices to set

$$
K (x) = \frac {1}{| \mathcal {G} |} \sum_ {A \in \mathcal {G}} K (A x), \qquad R (x) = \frac {1}{| \mathcal {G} |} \sum_ {A \in \mathcal {G}} R (A x).
$$

The required properties then follow at once.

## 5.4 Differentiation

Being a local operation, differentiating a modelled distribution is straightforward, provided again that the model one works with is sufficiently rich. Denote by$D _ { i }$the (usual) derivative of a distribution on$\mathbf { R } ^ { d }$with respect to the ith coordinate. We then have the following natural definition:

Definition 5.25 Given a sector V of a regularity structure$\mathcal { T }$, a family of operators$\mathcal { D } _ { i } \colon V \to T$is an abstract gradient for$\dot { \mathbf { R } } ^ { d }$with scaling s if

one has$\mathcal { D } _ { i } a \in T _ { \alpha - \mathfrak { s } _ { i } }$for every$a \in V _ { \alpha }$

one has$\Gamma \mathcal { D } _ { i } a = \mathcal { D } _ { i } \Gamma a$for every$a \in V$and every$i$.

Regarding the realisation of the actual derivations$D _ { i }$, we use the following definition:

Definition 5.26 Given an abstract gradient$\mathcal { D }$as above, a model$( \Pi , \Gamma )$on $\mathbf { R } ^ { d }$with scaling s is compatible with$\mathcal { D }$if the identity

$$
D _ {i} \Pi_ {x} a = \Pi_ {x} \mathcal {D} _ {i} a,
$$

holds for every$a \in V$and every$\boldsymbol { x } \in \mathbf { R } ^ { d }$

Remark 5.27 Note that we do not make any assumption on the interplay between the abstract gradient$\mathcal { D }$and the product . In particular, unless one happens to have the identity$\mathcal { D } _ { i } ( a \star b ) = a \star \mathcal { D } _ { i } b + \mathcal { D } _ { i } a \star b$, there is absolutely no a priori reason forcing the Leibniz rule to hold. This is not surprising since our framework can accommodate Itô integration, where the chain rule (and thus the Leibniz rule) fails. See [61] for a more thorough investigation of this fact.

Proposition 5.28 Let$\mathcal { D }$be an abstract gradient as above and let$f \in \mathcal { D } _ { \alpha } ^ { \beta } ( V )$ for some$\beta > \mathfrak { s } _ { i }$and some model ( , ) compatible with${ \mathcal { D } } .$. Then,$\mathcal { D } _ { i } f \in$ $\mathcal { D } _ { \alpha - \mathfrak { s } _ { i } } ^ { \beta - \mathfrak { s } _ { i } }$and the identity$\mathcal { R D } _ { i } f = D _ { i } \mathcal { R } f$holds.

Proof The fact that$\mathcal { D } _ { i } f \in \mathcal { D } _ { \alpha - 5 i } ^ { \beta - 5 i }$is an immediate consequence of the definitions, so we only need to show that$\mathcal { R D } _ { i } f = D _ { i } \mathcal { R } f$

By the “uniqueness” part of the reconstruction theorem, this on the other hand follows immediately if we can show that, for every fixed test function$\psi$ and every$x \in D$, one has

$$
\left(\Pi_ {x} \mathscr {D} _ {i} f (x) - D _ {i} \mathscr {R} f\right) \left(\psi_ {x} ^ {\lambda}\right) \lesssim \lambda^ {\delta},
$$

for some$\delta > 0$. Here, we defined$\psi _ { x } ^ { \lambda } = \mathcal { S } _ { \mathfrak { s } , x } ^ { \lambda } \psi$as before. By the assumption on the model , we have the identity

$$
\begin{array}{r} \big (\Pi_ {x} \mathcal {D} _ {i} f (x) - D _ {i} \mathcal {R} f \big) (\psi_ {x} ^ {\lambda}) = \big (D _ {i} \Pi_ {x} f (x) - D _ {i} \mathcal {R} f \big) (\psi_ {x} ^ {\lambda}) \\ = - \big (\Pi_ {x} f (x) - \mathcal {R} f \big) (D _ {i} \psi_ {x} ^ {\lambda}). \end{array}
$$

Since$D _ { i } \psi _ { x } ^ { \lambda } = \lambda ^ { - \mathfrak { s } _ { i } } { \mathcal { D } } _ { \mathfrak { s } , x } ^ { \lambda } D _ { i } \psi$, it then follows immediately from the reconstruction theorem that the right hand side of this expression is of order$\lambda ^ { \beta - s _ { i } }$, as required.□

Remark 5.29 The polynomial regularity structures$\mathcal { T } _ { d , \mathfrak { s } }$do of course come equipped with a natural gradient operator, obtained by setting$\mathcal { D } _ { i } X _ { j } = \delta _ { i j } \mathbf { 1 }$ and extending this to all of$T$by imposing the Leibniz rule.

Remark 5.30 In cases where a symmetry$\mathcal { S }$acts on$\mathcal { T }$, it is natural to impose that the abstract gradient is covariant in the sense that if$g \in \mathcal { S }$acts on$\mathbf { R } ^ { d }$ as$T _ { g } x = A _ { g } x + b _ { g }$and$M _ { g }$denotes the corresponding action on$T$, then one imposes that

$$
M _ {g} \mathcal {D} _ {i} \tau = \sum_ {j = 1} ^ {d} A _ {g} ^ {i j} \mathcal {D} _ {j} \tau ,
$$

for every$\tau$in the domain of$\mathcal { D }$. This is consistent with the fact that

$$
\begin{array}{r l} & {\left(\Pi_ {x} M _ {g} \mathcal {D} _ {i} \tau\right) (\psi) = \left(\Pi_ {T _ {g} x} \mathcal {D} _ {i} \tau\right) (T _ {g} ^ {\sharp} \psi) = \left(D _ {i} \Pi_ {T _ {g} x} \tau\right) (T _ {g} ^ {\sharp} \psi)} \\ & {\qquad = - \left(\Pi_ {T _ {g} x} \tau\right) (D _ {i} T _ {g} ^ {\sharp} \psi) = - A _ {g} ^ {i j} \left(\Pi_ {T _ {g} x} \tau\right) (T _ {g} ^ {\sharp} D _ {j} \psi)} \\ & {\qquad = - A _ {g} ^ {i j} \left(\Pi_ {x} M _ {g} \tau\right) (D _ {j} \psi) = A _ {g} ^ {i j} \left(\Pi_ {x} \mathcal {D} _ {j} M _ {g} \tau\right) (\psi),} \end{array}
$$

where summation over$j$is implicit. It is also consistent with Remark 3.35.

## 6 Singular modelled distributions

In all ofthe previous section, we have considered situations where our modelled distributions belong to some space$\mathcal { D } ^ { \gamma }$, which ensures that the bounds (3.1) hold locally uniformly in$\mathbf { R } ^ { d }$. One very important situation for the treatment of initial conditions and / or boundary values is that of functions$f \colon \mathbf { R } ^ { d }  T$ which are of the class$\mathcal { D } ^ { \gamma }$away from some fixed sufficiently regular submanifold$P$(think of the hyperplane formed by “time$0 ^ { \circ }$, which will be our main example), but may exhibit a singularity on$P$

In order to streamline the exposition, we only consider the case where$P$is given by a hyperplane that is furthermore parallel to some ofthe canonical basis elements of$\mathbf { R } ^ { d }$. The extension to general submanifolds is almost immediate. Throughout this section, we fix again the ambient space$\mathbf { R } ^ { d }$and its scaling s, and we fix a hyperplane$P$which we assume for simplicity to be given by

$$
P = \{x \in \mathbf {R} ^ {d}: x _ {i} = 0, i = 1, \ldots , \bar {d} \}.
$$

An important role will be played by the “effective codimension” of$P ,$, which we denote by

$$
\mathfrak {m} = \mathfrak {s} _ {1} + \dots + \mathfrak {s} _ {\bar {d}}.\tag{6.1}
$$

Remark 6.1 In the case where P is a smooth submanifold, it is important for our analysis that it has a product structure with each factor belonging to a subspace with all components having the same scaling. More precisely, we consider a partition$\mathcal { P }$of the set$\{ 1 , \ldots , d \}$into J disjoint non-empty subsets with cardinalities$\{ d _ { j } \} _ { j = 1 } ^ { J }$such that${ \mathfrak { s } } _ { i } = { \mathfrak { s } } _ { j }$if and only if i and$j$belong to the same element of$\mathcal { P }$. This yields a decomposition

$$
\mathbf {R} ^ {d} \sim \mathbf {R} ^ {d _ {1}} \times \dots \times \mathbf {R} ^ {d _ {J}}.
$$

With this notation, we impose that P is of the form$\mathcal { M } _ { 1 } \times . . . \times \mathcal { M } _ { J }$, with each of the$\mathcal { M } _ { j }$being a smooth (or at least Lipschitz) submanifold of$\mathbf { R } ^ { d _ { j } }$

The effective codimension m is then given by$\begin{array} { r } { \mathfrak { m } = \sum _ { j = 1 } ^ { J } \mathfrak { m } _ { j } } \end{array}$, where${ \mathfrak { m } } _ { j }$is the codimension of$\mathcal { M } _ { j }$in$\mathbf { R } ^ { d _ { j } }$<sub>, multiplied by the corresponding scaling factor.</sub>

We also introduce the notations

$$
\| x \| _ {P} = 1 \wedge d _ {\mathfrak {s}} (x, P), \quad \| x, y \| _ {P} = \| x \| _ {P} \wedge \| y \| _ {P}.
$$

Given a subset$\mathcal { R } \subset \mathbf { R } ^ { d }$, we also denote by${ \mathcal { R } } _ { P }$the set

$$
\mathfrak {K} _ {P} = \{(x, y) \in (\mathfrak {K} \setminus P) ^ {2}: x \neq y \text { and } \| x - y \| _ {\mathfrak {s}} \leq \| x, y \| _ {P} \}.
$$

With these notations at hand, we define the spaces$\mathcal { D } _ { P } ^ { \gamma , \eta }$similarly to$\mathcal { D } ^ { \gamma }$, but we introduce an additional exponent η controlling the behaviour of the coefficients near P. Our precise definition goes as follows:

Definition 6.2 Fix a regularity structure$\mathcal { T }$and a model$( \Pi , \Gamma )$, as well as a hyperplane$P$as above. Then, for any$\gamma > 0$and$\eta \in \mathbf { R }$, we set

$$
\| f \| _ {\gamma , \eta ; \mathfrak {K}} \stackrel {{\text { def }}} {{=}} \sup _ {x \in \mathfrak {K} \setminus P} \sup _ {\ell <   \gamma} \frac {\| f (x) \| _ {\ell}}{\| x \| _ {P} ^ {(\eta - \ell) \wedge 0}}, \qquad \llbracket f \rrbracket_ {\gamma , \eta ; \mathfrak {K}} \stackrel {{\text { def }}} {{=}} \sup _ {x \in \mathfrak {K} \setminus P} \sup _ {\ell <   \gamma} \frac {\| f (x) \| _ {\ell}}{\| x \| _ {P} ^ {\eta - \ell}}.
$$

The space$\mathcal { D } _ { P } ^ { \gamma , \eta } ( V )$then consists of all functions$f \colon { \mathbf { R } } ^ { d } \setminus P  T _ { \gamma } ^ { - }$such that, for every compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$, one has

$$
\| f \| _ {\gamma , \eta ; \mathfrak {K}} \stackrel {{\text { def }}} {{=}} \| f \| _ {\gamma , \eta ; \mathfrak {K}} + \sup _ {(x, y) \in \mathfrak {K} _ {P}} \sup _ {\ell <   \gamma} \frac {\| f (x) - \Gamma_ {x y} f (y) \| _ {\ell}}{\| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \| x , y \| _ {P} ^ {\eta - \gamma}} <   \infty .\tag{6.2}
$$

Similarly to before, we also set

$$
\begin{array}{l} \| f; \bar {f} \| _ {\gamma , \eta ; \mathfrak {K}} \stackrel {{\text { def }}} {{=}} \| f - \bar {f} \| _ {\gamma , \eta ; \mathfrak {K}} \\ + \sup _ {(x, y) \in \mathfrak {K} _ {P}} \sup _ {\ell <   \gamma} \frac {\| f (x) - \bar {f} (x) - \Gamma_ {x y} f (y) + \bar {\Gamma} _ {x y} \bar {f} (y) \| _ {\ell}}{\| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \| x , y \| _ {P} ^ {\eta - \gamma}}. \end{array}
$$

Remark 6.3 In the particular case of$\mathcal { T } = \mathcal { T } _ { d , \mathfrak { s } }$and ( , ) being the canonical model consisting of polynomials, we use the notation$\mathcal { C } _ { P } ^ { \gamma , \eta } ( \bar { V } )$instead of $\mathcal { D } _ { P } ^ { \gamma , \eta } ( V )$

At distances of order 1 from P, we see that the spaces$\mathcal { D } _ { P } ^ { \gamma , \eta }$and$\mathcal { D } ^ { \gamma }$coincide. However, if$\mathscr { k }$is such that$d _ { \mathfrak { s } } ( x , P ) \sim \lambda$, for all$x \in { \mathcal { R } }$, then one has, roughly speaking,

$$
\| f \| _ {\gamma , \eta ; \mathfrak {K}} \sim \lambda^ {\gamma - \eta} \| f \| _ {\gamma ; \mathfrak {K}}.\tag{6.3}
$$

In fact, this is not quite true: the components appearing in the first term in (6.2) scale slightly differently. However, it turns out that the first bound actually follows from the second, provided that one has an order one bound on f somewhere at order one distance from P, so that (6.3) does convey the right intuition in most situations.

The spaces$\mathcal { D } _ { P } ^ { \gamma , \eta }$will be particularly useful when setting up fixed point arguments to solve semilinear parabolic problems, where the solution exhibits a singularity (or at least some form of discontinuity) at$t = 0$. In particular, in all of the concrete examples treated in this article, we will have$P = \{ ( t , x )$ $t = 0 \}$

Remark 6.4 The space$\mathcal { D } _ { P } ^ { \gamma , 0 }$does not coincide with$\mathcal { D } ^ { \gamma }$. This is due to the fact that our definition still allows for some discontinuity at P. However,$\mathcal { D } _ { P } ^ { \gamma , \gamma }$ essentially coincides with$\mathcal { D } ^ { \gamma }$, the difference being that the supremum in (6.2) only runs over elements in${ \mathcal { R } } _ { P }$. If P is a hyperplane of codimension 1, then $f ( x )$can have different limits whether x approaches P from one side or the other.

Definition 6.2 is tailored in such a way that if K is of bounded diameter and we know that

$$
\sup _ {\ell <   \gamma} \| f (x) \| _ {\ell} <   \infty
$$

for some$x \in { \mathcal { R } } \setminus P$, then the bound on the first term in (6.2) follows from the bound on the second term. The following statement is a slightly different version of this fact which will be particularly useful when setting up local fixed point arguments, since it yields good control on$f ( x )$for x near P.

For$x \in \mathbf { R } ^ { d }$and$\delta > 0$, we write$S _ { P } ^ { \delta } x$for the value

$$
\mathcal {S} _ {P} ^ {\delta} x = (\delta x _ {1}, \ldots , \delta x _ {\bar {d}}, x _ {\bar {d} + 1}, \ldots , x _ {d}).
$$

With this notation at hand, we then have:

Lemma 6.5 Let K be a domain such thatfor every$x = ( x _ { 1 } , \ldots , x _ { d } ) \in \mathcal { R } ,$, one has$S _ { P } ^ { \delta } x \in \mathcal { R }$for every$\delta \in [ 0 , 1 ]$. Let$f \in \mathcal { D } _ { P } ^ { \gamma , \eta }$for some$\gamma > 0$and assume that, for every$\ell < \eta$, the map$x \mapsto \mathcal Q _ { \ell } f ( x )$extends continuously to all of K in such a way that$\mathcal { Q } _ { \ell } f ( x ) = 0 f o r x \in P$. Then, one has the bound

$$
\llbracket f \rrbracket_ {\gamma , \eta ; \mathfrak {K}} \lesssim \| | f \| | _ {\gamma , \eta ; \mathfrak {K}},
$$

with a proportionality constant depending affinely on$\| \Gamma \| _ { \gamma ; \mathscr { R } } .$. Similarly, let $\bar { f } \in \mathcal { D } _ { P } ^ { \gamma , \eta }$with respect to a second model ( ,¯ )¯ and assume this time that $\begin{array} { r } { \operatorname* { l i m } _ { x  P } \mathcal { Q } _ { \ell } ( f ( x ) - \bar { f } ( x ) ) = 0 } \end{array}$for every$\ell < \eta$. Then, one has the bound

$$
\llbracket f - \bar {f} \rrbracket_ {\gamma , \eta ; \mathfrak {K}} \lesssim \| f; \bar {f} \| _ {\gamma , \eta ; \mathfrak {K}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma ; \mathfrak {K}} \big (\| f \| _ {\gamma , \eta ; \mathfrak {K}} + \| \bar {f} \| _ {\gamma , \eta ; \mathfrak {K}} \big),
$$

with a proportionality constant depending again affinely on$\| \Gamma \| _ { \gamma ; \mathbb { A } }$and $\| \bar { \Gamma } \| _ { \gamma ; \mathscr { R } } .$

Proof For$d _ { \mathfrak { s } } ( x , P ) \geq 1$or$\ell \geq \eta$, the bounds follow trivially from the definitions, so we only need to consider the case$d _ { \mathfrak { s } } ( x , P ) < 1$and$\ell < \eta$. We then set$x _ { n } = S _ { P } ^ { 2 ^ { - n } }$x and$x _ { \infty } = { \mathcal { S } } _ { P } ^ { 0 } x$. We also use the shorthand$\Gamma _ { n } = \Gamma _ { x _ { n + 1 } x _ { n } }$, and we assume without loss of generality that$\| f \| _ { \gamma , \eta ; \mathscr { R } } \le 1$. Note that the sequence$x _ { n }$converges to$x _ { \infty }$and that

$$
\| x _ {n + 1} - x _ {n} \| _ {\mathfrak {s}} = \| x _ {n + 1} - x _ {\infty} \| _ {\mathfrak {s}} = \| x _ {n + 1} \| _ {P} = 2 ^ {- (n + 1)} \| x \| _ {P}.\tag{6.4}
$$

The argument now goes by “reverse induction” on . Assume that the bound $\| f ( x ) \| _ { m } \lesssim \| x \| _ { P } ^ { \eta - m }$holds for all$m > \ell$, which we certainly know to be the case when  is the largest element in A smaller than η since then this bound is already controlled by$f \| _ { \gamma , \eta ; \mathbb { R } }$. One then has

$$
\begin{array}{l} \| f (x _ {n + 1}) - f (x _ {n}) \| _ {\ell} \leq \| f (x _ {n + 1}) - \Gamma_ {n} f (x _ {n}) \| _ {\ell} + \| (1 - \Gamma_ {n}) f (x _ {n}) \| _ {\ell} \\ \lesssim 2 ^ {- n (\eta - \ell)} \| x \| _ {P} ^ {\eta - \ell} + \sum_ {m > \ell} 2 ^ {- n (m - \ell)} \| x \| _ {P} ^ {m - \ell} 2 ^ {- n (\eta - m)} \| x \| _ {P} ^ {\eta - m} \\ \lesssim 2 ^ {- n (\eta - \ell)} \| x \| _ {P} ^ {\eta - \ell}, \end{array} \tag {6}\tag{6.5}
$$

where we made use of the definition of$f \| _ { \gamma , \eta ; \mathbb { R } }$and (6.4) to bound the first term and of the inductive hypothesis, combined with (6.4) and the bounds on for the second term. It immediately follows that

$$
\begin{array}{c} \| f (x) \| _ {\ell} = \| f (x) - f (x _ {\infty}) \| _ {\ell} \leq \sum_ {n \geq 0} \| f (x _ {n + 1}) - f (x _ {n}) \| _ {\ell} \\ \lesssim \sum_ {n \geq 0} 2 ^ {- n (\eta - \ell)} \| x \| _ {P} ^ {\eta - \ell}, \end{array}
$$

which is precisely what is required for the first bound to hold. Here, the induction argument on  works because A is locally finite by assumption.

The second bound follows in a very similar way. Setting$\delta f = f - \bar { f }$, we write

$$
\begin{array}{r l} & {\| \delta f (x _ {n + 1}) - \delta f (x _ {n}) \| _ {\ell} \leq \| f (x _ {n + 1}) - \bar {f} (x _ {n + 1}) - \Gamma_ {n} f (x _ {n}) + \bar {\Gamma} _ {n} \bar {f} (x _ {n}) \| _ {\ell}} \\ & {\qquad + \| (1 - \Gamma_ {n}) f (x _ {n}) - (1 - \bar {\Gamma} _ {n}) \bar {f} (x _ {n}) \| _ {\ell}.} \end{array}
$$

The first term in this expression is bounded in the same way as above. The second term is bounded by

$$
\begin{array}{r l} & {\| (1 - \Gamma_ {n}) f (x _ {n}) - (1 - \bar {\Gamma} _ {n}) \bar {f} (x _ {n}) \| _ {\ell}} \\ & {\qquad \lesssim 2 ^ {- n (\eta - \ell)} \| x \| _ {P} ^ {\eta - \ell} \big (\| | f, \bar {f} \| _ {\gamma , \eta ; \mathfrak {K}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma ; \mathfrak {K}} \big),} \end{array}
$$

from which the stated bound then also follows in the same way as above.

The following kind of interpolation inequality will also be useful:

Lemma 6.6 Let$\gamma > 0$and$\kappa \in ( 0 , 1 )$and let f and$\bar { f }$satisfy the assumptions ofLemma 6.5. Then,for every compact set${ \mathfrak { R } } ,$one has the bound

$$
\| f; \bar {f} \| _ {(1 - \kappa) \gamma , \eta ; \mathfrak {K}} \lesssim \mathbb {I} f - \bar {f} \mathbb {I} _ {\gamma , \eta ; \mathfrak {K}} ^ {\kappa} \big (\| f \| _ {\gamma , \eta ; \mathfrak {K}} + \| \bar {f} \| _ {\gamma , \eta ; \mathfrak {K}} \big) ^ {1 - \kappa},
$$

where the proportionality constant depends on$\| \Gamma \| _ { \gamma ; \mathscr { R } } + \| \bar { \Gamma } \| _ { \gamma ; \mathscr { R } } .$

Proof All the operations are local, so we can just as well take$\mathcal { R } = \mathbf { R } ^ { d }$. First, one then has the obvious bound

$$
\begin{array}{l} \| f (x) - \Gamma_ {x y} f (y) - \bar {f} (x) + \bar {\Gamma} _ {x y} \bar {f} (y) \| _ {\ell} \\ \qquad \leq \big (\| | f \| | _ {\gamma , \eta} + \| | \bar {f} \| | _ {\gamma , \eta} \big) \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \| x, y \| _ {P} ^ {\eta - \gamma}. \end{array}
$$

On the other hand, one also has the bound

$$
\| f (x) - \Gamma_ {x y} f (y) - \bar {f} (x) + \bar {\Gamma} _ {x y} \bar {f} (y) \| _ {\ell} \lesssim [   [ f - \bar {f} ]   ] _ {\gamma , \eta} \| x, y \| _ {P} ^ {\eta - \ell},
$$

where the proportionality depends on the sizes of  and$\bar { \Gamma }$. As a consequence of these two bounds, we obtain

$$
\begin{array}{l} \| f (x) - \Gamma_ {x y} f (y) - \bar {f} (x) + \bar {\Gamma} _ {x y} \bar {f} (y) \| _ {\ell} \lesssim \mathbb {I} f - \bar {f} \mathbb {I} _ {\gamma , \eta} ^ {\kappa} \big (\| f \| _ {\gamma , \eta} + \| \bar {f} \| _ {\gamma , \eta} \big) ^ {1 - \kappa} \\ \qquad \times \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell - \kappa (\gamma - \ell)} \| x, y \| _ {P} ^ {\eta - \kappa \ell - (1 - \kappa) \gamma} \\ \qquad \lesssim \mathbb {I} f - \bar {f} \mathbb {I} _ {\gamma , \eta} ^ {\kappa} \big (\| f \| _ {\gamma , \eta} + \| \bar {f} \| _ {\gamma , \eta} \big) ^ {1 - \kappa} \| x - y \| _ {\mathfrak {s}} ^ {(1 - \kappa) \gamma - \ell} \| x, y \| _ {P} ^ {\eta - (1 - \kappa) \gamma}, \end{array}
$$

which is precisely the required bound. Here, we made use of the fact that we only consider points with$\| x - y \| _ { \mathfrak { s } } \lesssim \| x , y \| _ { P }$to obtain the last inequality.

Regarding the bound on$\| f ( x ) - { \bar { f } } ( x ) \| _ { \ell }$, one immediately obtains the required bound

$$
\| f (x) - \bar {f} (x) \| _ {\ell} \lesssim \mathbb {I} f - \bar {f} \mathbb {I} _ {\gamma , \eta} ^ {\kappa} \big (\| f \| _ {\gamma , \eta} + \| \bar {f} \| _ {\gamma , \eta} \big) ^ {1 - \kappa} \| x \| _ {P} ^ {(\eta - \ell) \wedge 1},
$$

simply because both$\mathbb { I } \cdot \mathbb { I } _ { \gamma , \eta }$and$\Vert \cdot \Vert _ { \gamma , \eta }$dominate that term.

In this section, we show that all of the calculus developed in the previous sections still carries over to these weighted spaces, provided that the exponents η are chosen in a suitable way. The proofs are mostly based on relatively straightforward but tedious modifications of the existing proofs in the uniform case, so we will try to focus mainly on those aspects that do actually differ.

## 6.1 Reconstruction theorem

We first obtain a modified version of the reconstruction theorem for elements $f \in \mathcal { D } _ { P } ^ { \gamma , \eta }$. Since the reconstruction operator$\mathcal { R }$is local and since f belongs to$\mathcal { D } ^ { \gamma }$away from$P _ { \mathrm { : } }$, there exists a unique element$\tilde { \mathcal { R } } f$in the dual of smooth functions that are compactly supported away from P which is such that

$$
\big (\tilde {\mathcal {R}} f - \Pi_ {x} f (x) \big) (\psi_ {x} ^ {\lambda}) \lesssim \lambda^ {\gamma},
$$

for all$x \notin P$and$\lambda \ll d ( x , P )$. The aim ofthis subsection is to show that, under suitable assumptions,$\tilde { \mathcal { R } } f$extends in a natural way to an actual distribution $\mathcal { R } f$on$\mathbf { R } ^ { d }$

In order to prepare for this result, the following result will be useful.

Lemma 6.7 Let$\mathcal { T } = ( A , T , G )$be a regularity structure and let$( \Pi , \Gamma )$be a model for$\mathcal { T }$over$\mathbf { R } ^ { d }$with scaling s. Let$\psi \in B _ { \mathfrak { s } , 0 } ^ { r }$with$r > |$min$A |$and $\lambda > 0$. Then,for$f \in { \mathcal { D } } ^ { \gamma }$, one has the bound

$$
\big | \big (\mathcal {R} f - \Pi_ {x} f (x) \big) (\psi_ {x} ^ {\lambda}) \big | \lesssim \lambda^ {\gamma} \sup _ {y, z \in B _ {2 \lambda} (x)} \sup _ {\ell <   \gamma} \frac {\| f (z) - \Gamma_ {z y} f (y) \| _ {\ell}}{\| z - y \| _ {\mathfrak {s}} ^ {\gamma - \ell}},
$$

where the proportionality constant is oforder$1 + \| \Gamma \| _ { \gamma ; B _ { 2 \lambda } ( x ) } \| \prod \gamma ; B _ { 2 \lambda } ( x )$

Remark 6.8 This is essentially a refinement of the reconstruction theorem. The difference is that the bound only uses information about$f$in a small area around the support of$\varphi _ { x } ^ { \lambda }$

Proof Inspecting the proof of Proposition 3.25, we note that one really only uses the bounds (3.30) only for pairs x and y with$\| x - y \| _ { \mathfrak { s } } \leq C \lambda$for some fixed$C > 0$. By choosing$n _ { 0 }$sufficiently large, one can furthermore easily ensure that$C \le 2$□

Proposition 6.9 Let$f \in \mathcal { D } _ { P } ^ { \gamma , \eta } ( V )$for some sector V of regularity$\alpha \leq 0 ,$ some$\gamma > 0$, and some$\eta ~ \leq ~ \gamma$. Then, provided that α$\wedge \eta > - \mathfrak { m }$where m is as in (6.1), there exists a unique distribution${ \mathcal R } f \in { \mathcal C } _ { \mathfrak s } ^ { \alpha \wedge \eta }$such that $\bigl ( \mathcal { R } f \bigr ) ( \varphi ) = \bigl ( \tilde { \mathcal { R } } f \bigr ) ( \varphi )$for smooth testfunctions that are compactly supported awayfrom P. If f and$\bar { f }$are modelled after two models Z and$\bar { z } ,$then one has the bound

$$
\| \mathcal {R} f - \bar {\mathcal {R}} \bar {f} \| _ {\alpha \wedge \eta ; \mathfrak {K}} \lesssim \| | f; \bar {f} \| | _ {\gamma , \eta ; \bar {\mathfrak {K}}} + \| | Z; \bar {z} \| | _ {\gamma ; \bar {\mathfrak {K}}},
$$

where the proportionality constant depends on the norms of$f , \bar { f } , Z$and${ \bar { z } } .$ Here, K is any compact set and$\bar { \mathbf { x } }$is its 1-fattening.

Remark$6 . I0$The condition α$\wedge \eta > - \mathfrak { m }$rules out the possibility of creating a non-integrable singularity on P, which would prevent$\tilde { \mathcal { R } } f$from defining a distribution on all of$\mathbf { R } ^ { \dot { d } }$. (Unless one “cancels out” the singularity by a diverging term located on$P$, but this would then lead to$\mathcal { R } f$being well-posed only up to some finite distribution localised on$P . )$

Remark$6 . I I$If$\alpha = 0$and$\eta \geq 0$, then due to our definition of$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$, Proposition$6 . 9$only implies that$\mathcal { R } f$is a bounded function, not that it is actually continuous.

Proof Since the reconstruction operator is linear and local, it suffices to consider the case where$\| f \| _ { \gamma , \eta ; \mathscr { R } } \leq 1$, which we will assume from now on.

Our main tool in the proof of this result is a suitable partition of the identity in the complement of$P$. Let$\varphi \colon \mathbf { R } _ { + }  [ 0 , 1 ]$be as in Lemma 5.5 and let $\tilde { \varphi } : \mathbf { R }  [ 0 , 1 ]$be a smooth function such that$\mathsf { s u p p } \tilde { \varphi } \subset [ - 1 , 1 ]$and

$$
\sum_ {k \in \mathbf {Z}} \tilde {\varphi} (x + k) = 1.
$$

For${ \boldsymbol { n } } \in \mathbf { Z }$, we then define the countable sets$\Xi _ { P } ^ { n }$by

$$
\Xi_ {P} ^ {n} = \{x \in \mathbf {R} ^ {d}: x _ {i} = 0 \text {   for   } i \leq \bar {d} \text {   and   } x _ {i} \in 2 ^ {- n \mathfrak {s} _ {i}} \mathbf {Z} \text {   for   } i > \bar {d} \}.
$$

This is very similar to the definition of the sets$\Lambda _ { n } ^ { \mathfrak { s } }$in Sect. 3.1, except that the points in$\Xi _ { P } ^ { n }$are all located in a small “boundary layer” around P. For${ \boldsymbol { n } } \in \mathbf { Z }$ and$x \in \Xi _ { P } ^ { n }$, we define the cutoff function$\varphi _ { x , n }$by

$$
\varphi_ {x, n} (y) = \varphi (2 ^ {n} N _ {P} (y)) \tilde {\varphi} \big (2 ^ {n \mathfrak {s} _ {\bar {d} + 1}} (y _ {\bar {d} + 1} - x _ {\bar {d} + 1}) \big) \dots \tilde {\varphi} \big (2 ^ {n \mathfrak {s} _ {d}} (y _ {d} - x _ {d}) \big),
$$

where$N _ { P }$is a smooth function on$\mathbf R ^ { d } \backslash P$which depends only on$( y _ { 1 } , \ldots , y _ { \bar { d } } )$ and which is “1-homogeneous” in the sense that$N _ { P } ( D _ { \mathfrak { s } } ^ { \delta } y ) = \delta N _ { P } ( y )$

One can verify that this construction yields a partition of the unity in the sense that

$$
\sum_ {n \in \mathbf {Z}} \sum_ {x \in \Xi_ {P} ^ {n}} \varphi_ {x, n} (y) = 1,
$$

for every$\boldsymbol { y } \in \mathbf { R } ^ { d } \setminus P$

Let furthermore$\hat { \varphi } _ { N }$be given by$\begin{array} { r } { \hat { \varphi } _ { N } = \sum _ { n \leq N } \sum _ { x \in \Xi _ { P } ^ { n } } \varphi _ { x , n } } \end{array}$. One can then show that, for every distribution$\xi \in \mathcal { C } _ { \mathfrak { s } } ^ { \bar { \alpha } }$<sub>with</sub>$\bar { \alpha } > - \mathfrak { m }$and every smooth test function$\psi$, one has

$$
\lim _ {N \to \infty} \xi (\psi (1 - \hat {\varphi} _ {N})) = 0.
$$

As a consequence, it suffices to show that, for every smooth compactly supported test function$\psi$, the sequence$( \tilde { \mathcal { R } } f ) ( \psi \hat { \varphi } _ { N } )$is Cauchy and that its limit, which we denote by$( { \mathcal { R } } f ) ( \psi )$, satisfies the bound of Definition 3.7.

Take now a smooth test function ψ supported in$B ( 0 , 1 )$and define the translated and rescaled versions$\psi _ { x } ^ { \lambda }$as before with$\lambda \in ( 0 , 1 ] . \operatorname { I f } d _ { \mathfrak { s } } ( x , P ) \geq 2 \lambda$ then it follows from Lemma 6.7 that

$$
\bigl (\tilde {\mathcal {R}} f - \Pi_ {x} f (x) \bigr) (\psi_ {x} ^ {\lambda}) \lesssim d _ {\mathfrak {s}} (x, P) ^ {\eta - \gamma} \lambda^ {\gamma} \lesssim \lambda^ {\eta},\tag{6.6}
$$

where the last bound follows from the fact that$\gamma \geq \eta$by assumption. Since furthermore

$$
\bigl (\Pi_ {x} f (x) \bigr) (\psi_ {x} ^ {\lambda}) \lesssim \sum_ {\alpha \leq \ell <   \gamma} \| x \| _ {P} ^ {(\eta - \ell) \wedge 0} \lambda^ {\ell} \lesssim \lambda^ {\alpha \wedge \eta},\tag{6.7}
$$

we do have the required bound in this case.

In the case$d _ { \mathfrak { s } } ( x , P ) \leq 2 \lambda$, we rewrite$\psi _ { x } ^ { \lambda }$as

$$
\psi_ {x} ^ {\lambda} = \sum_ {n \geq n _ {0}} \sum_ {y \in \Xi_ {P} ^ {n}} \psi_ {x} ^ {\lambda} \varphi_ {y, n},
$$

where$n _ { 0 }$is the greatest integer such that$2 ^ { - n _ { 0 } } \geq 3 \lambda$. Setting

$$
\chi_ {n, x y} = \lambda^ {| \mathfrak {s} |} 2 ^ {n | \mathfrak {s} |} \psi_ {x} ^ {\lambda} \varphi_ {y, n},
$$

it is straightforward to verify that$\chi _ { n , x y }$satisfies the bounds

$$
\sup _ {z \in \mathbf {R} ^ {d}} | D ^ {k} \chi_ {n, x y} (z) | \lesssim 2 ^ {- (| \mathfrak {s} | + | k | _ {\mathfrak {s}}) n},
$$

for any multiindex k. Furthermore, just as in the case of the bound (6.6), every point in the support of$\chi _ { n , x y }$is located at a distance of P that is of the same order. Using a suitable partition of unity, one can therefore rewrite it as

$$
\chi_ {n, x y} = \sum_ {j = 1} ^ {M} \chi_ {n, x y} ^ {(j)},
$$

where M is a fixed constant and where each of the$\chi _ { n , x y } ^ { ( j ) }$has its support centred in a ball of radius$\frac { 1 } { 2 } d _ { 5 } ( z _ { j } , P )$around some point$z _ { j }$. As a consequence, by the same argument as before, we obtain the bound

$$
\bigl (\tilde {\mathcal {R}} f - \Pi_ {z _ {j}} f (z _ {j}) \bigr) (\chi_ {n, x y}) \lesssim \sum_ {j = 1} ^ {M} d _ {\mathfrak {s}} (z _ {j}, P) ^ {\eta - \gamma} 2 ^ {- \gamma n} \lesssim 2 ^ {- \eta n}.\tag{6.8}
$$

Using the same argument as in (6.7), it then follows at once that

$$
\left| \left(\tilde {\mathcal {R}} f\right) \left(\chi_ {n, x y}\right) \right| \lesssim 2 ^ {- (\alpha \wedge \eta) n}.\tag{6.9}
$$

Note now that we have the identity

$$
\bigl (\tilde {\mathcal {R}} f \bigr) \bigl (\psi_ {x} ^ {\lambda} \hat {\varphi} _ {N} \bigr) = \sum_ {n = n _ {0}} ^ {N} \lambda^ {- | \mathfrak {s} |} 2 ^ {- n | \mathfrak {s} |} \sum_ {y \in \Xi_ {P} ^ {n}} \bigl (\tilde {\mathcal {R}} f \bigr) \bigl (\chi_ {n, x y} \bigr).
$$

At this stage, we make use of the fact that$\chi _ { n , x y } = 0$, unless$\| x - y \| _ { \mathfrak { s } } \lesssim \lambda$. As a consequence, for$n \geq n _ { 0 }$, the number of terms contributing in the above sum is bounded by$( 2 ^ { n } \lambda ) ^ { | \mathfrak { s } | - \mathfrak { m } }$. Combining this remark with (6.9) yields the bound

$$
\left| \lambda^ {- | \mathfrak {s} |} 2 ^ {- n | \mathfrak {s} |} \sum_ {y \in \Xi_ {P} ^ {n}} \bigl (\tilde {\mathcal {R}} f \bigr) \bigl (\chi_ {n, x y} \bigr) \right| \lesssim \lambda^ {- \mathfrak {m}} 2 ^ {- ((\alpha \wedge \eta) + \mathfrak {m}) n},
$$

from which the claim follows at once, provided that α$\wedge \eta > - \mathfrak { m }$, which is true by assumption. The bound on$\mathcal { R } f - \bar { \mathcal { R } } f$then follows in exactly the same way.□

In the remainder of this section, we extend the calculus developed in the previous sections to the case of singular modelled distributions.

## 6.2 Multiplication

We now show that the product of two singular modelled distributions yields again a singular modelled distribution under suitable assumptions. The precise workings of the exponents is as follows:

Proposition 6.12 Let P be as above and let$f _ { 1 } ~ \in \mathcal { D } _ { P } ^ { \gamma _ { 1 } , \eta _ { 1 } } ( V ^ { ( 1 ) } )$and$f _ { 2 } \in$ $\mathcal { D } _ { P } ^ { \gamma _ { 2 } , \eta _ { 2 } } ( V ^ { ( 2 ) } )$for two sectors$V ^ { ( 1 ) }$and$V ^ { ( 2 ) }$with respective regularities$\alpha _ { 1 }$and $\alpha _ { 2 }$. Let furthermore be a product on T such that$( V ^ { ( 1 ) } , V ^ { ( 2 ) } )$is γ -regular with$\gamma = ( \gamma _ { 1 } + \alpha _ { 2 } ) \wedge ( \gamma _ { 2 } + \alpha _ { 1 } )$. Then, thefunction$f = f _ { 1 } \star _ { \gamma } f _ { 2 }$belongs to $\mathcal { D } _ { P } ^ { \gamma , \eta }$with$\eta = ( \eta _ { 1 } + \alpha _ { 2 } ) \wedge ( \eta _ { 2 } + \alpha _ { 1 } ) \wedge ( \eta _ { 1 } + \eta _ { 2 } ) . ( H e r e , \star _ { \gamma }$is the projection ofthe product onto$T _ { \gamma } ^ { - }$as before.)

Furthermore, in the situation analogous to Proposition 4.10, writing$f =$ $f _ { 1 } \star f _ { 2 }$and$g = g _ { 1 } \star g _ { 2 }$, one has the bound

$$
\| f; g \| _ {\gamma , \eta ; \mathfrak {K}} \lesssim \| f _ {1}; g _ {1} \| _ {\gamma_ {1}, \eta_ {1}; \mathfrak {K}} + \| f _ {2}; g _ {2} \| _ {\gamma_ {2}, \eta_ {2}; \mathfrak {K}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma_ {1} + \gamma_ {2}; \mathfrak {K}},
$$

uniformly over any bounded set.

Proof We first show that$f = f _ { 1 } \star _ { \gamma } f _ { 2 }$does indeed satisfy the claimed bounds. By Theorem 4.7, we only need to consider points x, y which are both at distance less than 1 from P. Also, by bilinearity and locality, it suffices to consider the case when both$f _ { 1 }$and$f _ { 2 }$are of norm 1 on the fixed compact${ \mathcal { \kappa } } .$. Regarding the supremum bound on$f$, we have

$$
\begin{array}{l} \| f (x) \| _ {\ell} \leq \sum_ {\ell_ {1} + \ell_ {2} = k} \| f _ {1} (x) \| _ {\ell_ {1}} \| f _ {2} (x) \| _ {\ell_ {2}} \leq \sum_ {\ell_ {1} + \ell_ {2} = \ell} \| x \| _ {P} ^ {(\eta_ {1} - \ell_ {1}) \wedge 0} \| x \| _ {P} ^ {(\eta_ {2} - \ell_ {2}) \wedge 0} \\ \lesssim \| x \| _ {P} ^ {(\eta - \ell) \wedge 0}, \end{array}
$$

which is precisely as required.

It remains to obtain a suitable bound on$f ( x ) - \Gamma _ { x y } f ( y )$. For this, it follows from Definition 6.2 that it suffices to consider pairs$( x , y )$such that$2 \| x - y \| _ { \mathfrak { s } } \le$ $d _ { \mathfrak { s } } ( x , P ) \wedge d _ { \mathfrak { s } } ( y , P ) \leq 1$. For such pairs$( x , y )$, it follows immediately from the triangle inequality that

$$
d _ {\mathfrak {s}} (x, P) = \| x \| _ {P} \sim \| y \| _ {P} \sim \| x, y \| _ {P},\tag{6.10}
$$

in the sense that any of these quantities is bounded by a multiple of any other quantity, with some universal proportionality constants. For$\ell < \gamma _ { i }$, one then has the bounds

$$
\begin{array}{c} \| f _ {i} (x) - \Gamma_ {x y} f _ {i} (y) \| _ {\ell} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma_ {i} - \ell_ {i}} \| x, y \| _ {P} ^ {\eta_ {i} - \gamma_ {i}}, \\ \| f _ {i} (x) \| _ {\ell} \lesssim \| x, y \| _ {P} ^ {(\eta_ {i} - \ell_ {i}) \wedge 0}, \end{array}\tag{6.11}
$$

for$i \in \{ 1 , 2 \}$

As in (4.6), one then has

$$
\begin{array}{l} \| \Gamma_ {x y} f (y) - (\Gamma_ {x y} f _ {1} (y)) \star (\Gamma_ {x y} f _ {2} (y)) \| _ {\ell} \\ \lesssim \sum_ {m + n \geq \gamma} \| x - y \| _ {\mathfrak {s}} ^ {m + n - \ell} \| f _ {1} (y) \| _ {m} \| f _ {2} (y) \| _ {n} \\ \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \sum_ {m + n \geq \gamma} \| x, y \| _ {P} ^ {m + n - \gamma} \| x, y \| _ {P} ^ {(\eta_ {1} - m) \wedge 0} \| x, y \| _ {P} ^ {(\eta_ {2} - n) \wedge 0} \\ = \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \sum_ {m + n \geq \gamma} \| x, y \| _ {P} ^ {- \gamma} \| x, y \| _ {P} ^ {\eta_ {1} \wedge m} \| x, y \| _ {P} ^ {\eta_ {2} \wedge n} \\ \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \| x, y \| _ {P} ^ {- \gamma} \| x, y \| _ {P} ^ {\eta_ {1} \wedge \alpha_ {2}} \| x, y \| _ {P} ^ {\eta_ {2} \wedge \alpha_ {1}} \\ = \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \| x, y \| _ {P} ^ {\eta - \gamma}. \end{array} \tag {6}\tag{6.12}
$$

Here, in order to obtain the second line, we made use of (6.10), as well as the fact that we are only considering points$( x , y )$such that$\| x - y \| _ { \mathfrak { s } } \leq \| x , y \| _ { P }$ Combining this with the bound (4.4) from the proof of Theorem 4.7 and using again the bounds (6.11), the requested bound then follows at once.

It remains to obtain a bound on$\| f ; g \| _ { \gamma , \eta ; \mathcal { R } } .$. For this, we proceed almost exactly as in Proposition 4.10. First note that, proceeding as above, one obtains the estimate

$$
\begin{array}{l} \| \Gamma_ {x y} f (y) - \bar {\Gamma} _ {x y} g (y) - \Gamma_ {x y} f _ {1} (y) \star \Gamma_ {x y} f _ {2} (y) + \bar {\Gamma} _ {x y} g _ {1} (y) \star \bar {\Gamma} _ {x y} g _ {2} (y) \| _ {\ell} \\ \leq \| \Gamma - \bar {\Gamma} \| _ {\gamma_ {1} + \gamma_ {2}; \mathfrak {K}} \sum_ {m + n \geq \gamma} \| x - y \| _ {\mathfrak {s}} ^ {m + n - \ell} \| f _ {1} (y) \| _ {m} \| f _ {2} (y) \| _ {n} \\ + \sum_ {m + n \geq \gamma} \| x - y \| _ {\mathfrak {s}} ^ {m + n - \ell} \| f _ {1} (y) - g _ {1} (y) \| _ {m} \| f _ {2} (y) \| _ {n} \\ + \sum_ {m + n \geq \gamma} \| x - y \| _ {\mathfrak {s}} ^ {m + n - \ell} \| g _ {1} (y) \| _ {m} \| f _ {2} (y) - g _ {2} (y) \| _ {n}, \end{array}
$$

which then yields a bound of the desired type by proceeding as in (6.12). The remainder is then decomposed exactly as in (4.7). Denoting by$T _ { 1 } , \ldots , T _ { 5 }$the terms appearing there, we proceed to bound them again separately.

For the term$T _ { 1 }$, we obtain this time the bound

$$
\| T_{1}\|_{\ell}\lesssim \| f_{1};  g_{1}\|_{\gamma_{1},\eta_{1};\mathfrak{K}}\sum_{\substack{m + n = \ell \\ n\geq \alpha_{2};m\geq \alpha_{1}}}\| x - y\|_{\mathfrak{s}}^{\gamma_{1} - m}\| x\|_{P}^{(\eta_{2} - n)\wedge 0}\| x,y\|_{P}^{\eta_{1} - \gamma_{1}}.
$$

Since, as in the proof of Proposition 4.10, all the terms in this sum satisfy $\gamma _ { 1 } - m > \gamma - \ell$, we can bound$\| x - y \| _ { 5 } ^ { \gamma _ { 1 } - m }$by$\| x - y \| _ { \mathfrak { s } } ^ { \gamma - \ell } \| x , y \| _ { P } ^ { n + \gamma _ { 1 } - \gamma }$

We thus obtain the bound

$$
\| T _ {1} \| _ {\ell} \lesssim \| f _ {1}; g _ {1} \| _ {\gamma_ {1}, \eta_ {1}; \mathfrak {K}} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \| x, y \| _ {P} ^ {(\eta_ {2} \wedge \alpha_ {2}) + \eta_ {1} - \gamma}.
$$

Since$\eta \leq ( \eta _ { 2 } \land \alpha _ { 2 } ) + \eta _ { 1 }$, this bound is precisely as required.

The bound on$T _ { 2 }$follows in a similar way, once we note that for the pairs $( x , y )$under consideration one has

$$
\begin{array}{l} \| \Gamma_ {x y} f _ {1} (y) \| _ {\ell} \lesssim \sum_ {m \geq \ell} \| x - y \| _ {\mathfrak {s}} ^ {m - \ell} \| f _ {1} (y) \| _ {m} \lesssim \sum_ {m \geq \ell} \varrho_ {\mathfrak {s}} ^ {m - \ell} (x, y) \| f _ {1} (y) \| _ {m} \\ \lesssim \sum_ {m \geq \ell} \varrho_ {\mathfrak {s}} ^ {m - \ell} (x, y) \varrho_ {\mathfrak {s}} ^ {(\eta_ {1} - m) \wedge 0} (x, y) \lesssim \varrho_ {\mathfrak {s}} ^ {(\eta_ {1} - \ell) \wedge 0} (x, y), \end{array} \tag {6}\tag{6.13}
$$

where we used (6.10) to obtain the penultimate bound, so that$\Gamma _ { x y } f _ { 1 } ( y )$satisfies essentially the same bounds as$f _ { 1 } ( x )$

Regarding the term$T _ { 5 }$, we obtain

$$
\| T_{5}\|_{\ell}\lesssim \| f_{2} - g_{2}\|_{\gamma_{2},\eta_{2};\mathfrak{K}}\sum_{\substack{m + n = \ell \\ m\geq \alpha_{1};n\geq \alpha_{2}}}\| x - y\|_{\mathfrak{s}}^{\gamma_{1} - m}\| x,y\|_{P}^{\eta_{1} - \gamma_{1}}\| y\|_{P}^{(\eta_{2} - n)\wedge 0},
$$

from which the required bound follows in the same way as for$T _ { 1 }$. The term $T _ { 3 }$is treated in the same way by making again use of the remark (6.13), this time with$g _ { 1 } ( y ) - f _ { 1 } ( y )$playing the role of$f _ { 1 } ( y )$

The remaining term$T _ { 4 }$can be bounded in virtually the same way as$T _ { 5 }$, the main difference being that the bounds on$( \bar { \Gamma } _ { x y } - \Gamma _ { x y } ) f _ { 1 } ( y )$are proportional to$\| \Gamma - \bar { \Gamma } \| _ { \gamma _ { 1 } ; \mathscr { R } } .$, so that one has

$$
\| T _ {4} \| _ {\ell} \lesssim \| \Gamma - \bar {\Gamma} \| _ {\gamma_ {1}; \mathfrak {K}} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \| x, y \| _ {P} ^ {(\eta_ {1} \wedge \alpha_ {1}) + \eta_ {2} - \gamma}.
$$

Combining all of these bounds completes the proof.

## 6.3 Composition with smooth functions

Similarly to the case of multiplication of two modelled distributions, we can compose them with smooth functions as in Sect. 4.2, provided that they belong to$\mathcal { D } _ { P } ^ { \hat { \gamma } , \eta } ( V )$for some function-like sector V stable under the product , and for some$\eta \geq 0$

Proposition 6.13 Let P be as above, let$\gamma > 0$, and let$f _ { i } \in { \mathcal { D } } _ { P } ^ { \gamma , \eta } ( V )$be a collection of n modelled distributions for some function-like sector V which is stable under the product . Assume furthermore that V is γ-regular in the sense ofDefinition 4.6.

Letfurthermore$F \colon \mathbf { R } ^ { n }  \mathbf { R }$be a smoothfunction. Then,provided that$\eta \in$ $[ 0 , \gamma ]$, the modelled distribution$\hat { F } _ { \gamma } ( f )$defined as in Sect. 4.2 also belongs to $\mathcal { D } _ { P } ^ { \gamma , \eta } ( V )$. Furthermore, the map$\hat { F } _ { \gamma } \colon { \mathcal { D } } _ { P } ^ { \gamma , \eta } ( V ) \to { \mathcal { D } } _ { P } ^ { \gamma , \eta } ( V )$is locally Lipschitz continuous in any ofthe seminorms$\| \cdot \| _ { \gamma , \eta ; \mathscr { R } }$and$\Vert \cdot \Vert _ { \gamma , \eta ; \mathscr { R } } .$

Remark 6.14 In fact, we do not need F to be${ \mathcal { C } } ^ { \infty }$, but the same regularity requirements as in Sect. 4.2 suffice. Also, it is likely that one could obtain continuity in the strong sense, but in the interest of brevity, we refrain from doing so.

Proof Write$b ( x ) = \hat { F } _ { \gamma } ( f ( x ) )$as before. We also set$\zeta ~ \in ~ [ 0 , \gamma ]$as in the proof of Theorem 4.16. Regarding the bound on$\| b \| _ { \gamma , \eta ; \mathbb { A } } .$, we note first that since we assumed that$\eta \ge 0 , ( 6 . 2 )$implies that the quantities$D ^ { k } F ( { \bar { f } } ( x ) )$) are locally uniformly bounded. It follows that one has the bound

$$
\| b (x) \| _ {\ell} \lesssim \sum_ {\ell_ {1} + \dots + \ell_ {n} = \ell} \| f (x) \| _ {\ell_ {1}} \dots \| f (x) \| _ {\ell_ {n}},
$$

where the sum runs over all possible ways of decomposing  into finitely many strictly positive elements$\ell _ { i } \in A$. Note now that one necessarily has the bound

$$
\left((\eta - \ell_ {1}) \wedge 0\right) + \dots + \left((\eta - \ell_ {n}) \wedge 0\right) \geq (\eta - \ell) \wedge 0.\tag{6.14}
$$

Indeed, if all of the terms on the left vanish, then the bound holds trivially. Otherwise, at least one term is given by$\eta - \ell _ { i }$and, for all the other terms, we use the fact that$( \eta - \ell _ { j } ) \wedge 0 \geq - \ell _ { j }$. Since$\| x \| _ { P } \leq 1$, it follows at once that

$$
\| b (x) \| _ {\ell} \lesssim \| x \| _ {P} ^ {(\eta - \ell) \wedge 0},
$$

as required.

In order to bound$\Gamma _ { x y } b ( y ) - b ( x )$, we proceed exactly as in the proof of Theorem 4.16. All we need to show is that the various remainder terms appearing in that proof satisfy bounds of the type

$$
\| R _ {i} (x, y) \| _ {\ell} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \| x, y \| _ {P} ^ {\eta - \gamma}.\tag{6.15}
$$

Regarding the term$R _ { 1 } ( x , y )$, it follows from a calculation similar to (4.5) that it consists of terms proportional to

$$
\Gamma_ {x y} \mathcal {Q} _ {\ell_ {1}} \tilde {f} (y) \star \dots \star \Gamma_ {x y} \mathcal {Q} _ {\ell_ {n}} \tilde {f} (y),
$$

where$\sum \ell _ { i } \geq \gamma$. Combining the bounds on  with the definition of the space $\mathcal { D } _ { P } ^ { \gamma , \eta }$, we know furthermore that each of these factors satisfies a bound of the

type

$$
\| \Gamma_ {x y} \mathcal {Q} _ {\ell_ {i}} \tilde {f} (y) \| _ {m} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\ell_ {i} - m} \| x \| _ {P} ^ {(\eta - \ell_ {i}) \wedge 0}.\tag{6.16}
$$

Combining this with the fact that$\sum \ell _ { i } \geq \gamma$, that$\| x - y \| _ { 5 } \lesssim \| x \| _ { P }$, and the bound (6.14), the bound (6.15) follows for$R _ { 1 }$

Regarding$R _ { f }$, it follows from the definitions that

$$
\| R _ {f} (x, y) \| _ {m} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma - m} \| x, y \| _ {P} ^ {\eta - \gamma}.\tag{6.17}
$$

Furthermore, as a consequence of the fact that$\eta \geq 0$and$\| x - y \| _ { 5 } \lesssim \| x \| _ { P }$ it follows from (6.16) and (6.17) that

$$
\| \Gamma_ {x y} \tilde {f} (y) \| _ {m} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {- m}, \quad \| \tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) \mathbf {1} \| _ {m} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {- m}.
$$

Combining this with (6.17) and the expression for$R _ { 2 }$, we immediately conclude that$R _ { 2 }$also satisfies (6.15).

Note now that one has the bound

$$
\begin{array}{l} | \bar {f} (x) - \bar {f} (y) | \lesssim \| \Gamma_ {x y} \tilde {f} (y) \| _ {0} + \| x - y \| _ {\mathfrak {s}} ^ {\gamma}   \| x, y \| _ {P} ^ {\eta - \gamma} \\ \qquad \lesssim \sum_ {\zeta \leq \ell <   \gamma} \| x - y \| _ {\mathfrak {s}} ^ {\ell}   \| x, y \| _ {P} ^ {(\eta - \ell) \wedge 0} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\zeta}   \| x, y \| _ {P} ^ {(\eta - \zeta) \wedge 0}, \end{array}\tag{6.18}
$$

where we used the fact that$\zeta \ \leq \gamma$. Since we furthermore know that${ \bar { f } } ( x )$is uniformly bounded in$\mathscr { k }$as a consequence of the fact that$\eta \geq 0$, it follows that the bound equivalent to (4.14) in this context is given by

$$
\begin{array}{l} D ^ {k} F (\bar {f} (x)) = \sum_ {| k + \ell | \leq L} \frac {D ^ {k + \ell} F (\bar {f} (y))}{\ell !} \big (\bar {f} (x) - \bar {f} (y) \big) ^ {\ell} \\ \quad + \mathcal {O} \big (\| x - y \| _ {\mathfrak {s}} ^ {\gamma - | k | \zeta} \| x, y \| _ {P} ^ {\mu_ {k}} \big), \end{array}\tag{6.19}
$$

where$L = \lfloor \gamma / \zeta \rfloor$and the exponent$\mu _ { k }$is given by$\mu _ { k } = \big ( | k | \zeta - \gamma - | k | \eta +$ $( \gamma \eta / \zeta ) ) \land 0$. We can furthermore assume without loss of generality that$\zeta \leq 1$ Furthermore, making use of (6.18), it follows as in (4.15) that

$$
\begin{array}{l} \left\| \left(\tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) \mathbf {1}\right) ^ {\star k} \right\| _ {\beta} \\ \lesssim \sum_ {m \geq 0} \sum_ {\ell} \| x - y \| _ {\mathfrak {s}} ^ {\zeta (| k | - m)} \| x, y \| _ {P} ^ {(| k | - m) ((\eta - \zeta) \wedge 0)} \\ \times \| x, y \| _ {P} ^ {(\eta - \ell_ {1}) \wedge 0} \dots \| x, y \| _ {P} ^ {(\eta - \ell_ {m}) \wedge 0}, \end{array}
$$

where the second sum runs over all indices$\ell _ { 1 } , \ldots , \ell _ { m }$with$\textstyle \sum \ell _ { i } = \beta$and $\ell _ { i } \geq \zeta$for every i. In particular, one has the bound

$$
\begin{array}{l} \left\| \big (\tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) \mathbf {1} \big) ^ {\star k} \right\| _ {\beta} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\zeta | k | - \beta} \| x, y \| _ {P} ^ {\beta - \zeta m} \\ \times \sum_ {m \geq 0} \sum_ {\ell} \| x, y \| _ {P} ^ {(| k | - m) ((\eta - \zeta) \wedge 0)} \| x, y \| _ {P} ^ {(\eta - \ell_ {1}) \wedge 0} \dots \| x, y \| _ {P} ^ {(\eta - \ell_ {m}) \wedge 0}. \end{array}
$$

Let us have a closer look at the exponents of$\| x , y \| _ { P }$appearing in this expression:

$$
\mu_ {m, \ell} \stackrel {\text { def }} {=} \beta - \zeta m + (| k | - m) ((\eta - \zeta) \wedge 0) + \sum_ {i = 1} ^ {m} (\eta - \ell_ {i}) \wedge 0.
$$

Note that, thanks to the distributivity of the infimum with respect to addition and to the facts that$\textstyle \sum \ell _ { i } = \beta$and$\ell _ { i } \geq \zeta$, one has the bound

$$
\sum_ {i = 1} ^ {m} (\eta - \ell_ {i}) \wedge 0 \geq \inf _ {n \leq m} (n \eta - \beta + (m - n) \zeta) = m \zeta - \beta + \inf _ {n \leq m} n (\eta - \zeta).
$$

As a consequence, we have$\mu _ { m , \ell } \geq 0 \mathrm { i f } \eta \geq \zeta$and$\mu _ { m , \ell } \geq | k | ( \eta - \zeta )$otherwise, so that

$$
\left\| \left(\tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) \mathbf {1}\right) ^ {\star k} \right\| _ {\beta} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\zeta | k | - \beta} \| x, y \| _ {P} ^ {| k | (\eta - \zeta) \wedge 0}.
$$

Note furthermore that, by an argument similar to above, one has the bound

$$
\mu_ {k} + | k | (\eta - \zeta) \wedge 0 \geq (\eta - \zeta) \frac {\gamma}{\zeta} \wedge 0 \geq (\eta - \gamma) \wedge 0 = \eta - \gamma ,
$$

where we used the fact that$\zeta ~ \leq ~ \gamma$and the last identity follows from the assumption that$\eta \leq \gamma$. Combining this with (6.19) and the definition of$R _ { 3 }$ from (4.16), we obtain the bound (6.15) for$R _ { 3 }$, which implies that${ \hat { F } } ( f ) \in$ $\mathcal { D } _ { P } ^ { \gamma , \eta }$as required.

The proof of the local Lipschitz continuity then follows in exactly the same way as in the proof of Theorem 4.16.□

## 6.4 Differentiation

In the same context as Sect. 5.4, one has the following result:

Proposition 6.15 Let$\mathcal { D }$be an abstract gradient as in Sect. 5.4 and let$f \in$ $\mathcal { D } _ { P } ^ { \gamma , \hat { \eta } } ( V )$for some$\gamma > \mathfrak { s } _ { i }$and$\eta \in \mathbf { R }$. Then,$\mathcal { D } _ { i } f \in \mathcal { D } _ { P } ^ { \gamma - \mathfrak { s } _ { i } , \eta - \mathfrak { s } _ { i } }$

Proof This is an immediate consequence of the definition (6.2) and the properties of abstract gradients.□

## 6.5 Integration against singular kernels

In this section, we extend the results from Sect. 5 to spaces ofsingular modelled distributions. Our main result can be stated as follows.

Proposition 6.16 Let$\mathcal { T }$, V, K and β be as in Theorem 5.12 and let$f \in$ $\mathcal { D } _ { P } ^ { \gamma , \bar { \eta } } ( V )$with$\eta < \gamma$. Denote furthermore by α the regularity of the sector V and assume that$\eta \wedge \alpha > - \mathfrak { m }$. Then, provided that$\gamma + \beta \not \in \mathbf { N }$and$\eta + \beta \not \in \mathbf { N } ,$ one has$\kappa _ { \gamma } f \in \mathcal { D } _ { P } ^ { \bar { \Gamma } , \bar { \eta } }$with$\bar { \Gamma } = \gamma + \beta$and$\bar { \eta } = ( \eta \wedge \alpha ) + \beta .$

Furthermore, in the situation analogous to that of the last part of Theorem 5.12, one has the bound

$$
\| \mathcal {K} _ {\gamma} f; \bar {\mathcal {K}} _ {\gamma} \bar {f} \| _ {\bar {\Gamma}, \bar {\eta}; \bar {\mathfrak {K}}} \lesssim \| f; \bar {f} \| _ {\gamma , \eta ; \bar {\mathfrak {K}}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Gamma - \bar {\Gamma} \| _ {\bar {\Gamma}; \bar {\mathfrak {K}}},\tag{6.20}
$$

for all$f \in { \mathcal { D } } _ { P } ^ { \gamma , \eta } ( V ; \Gamma )$and$\bar { f } \in \mathcal { D } _ { P } ^ { \gamma , \eta } ( V ; \bar { \Gamma } )$

Proof We first observe that$\mathcal { N } _ { \gamma } f$is well-defined for a singular modelled distribution as in the statement. Indeed, for every x$\notin P$, it suffices to decompose K as$K = K ^ { ( 1 ) } + K ^ { ( 2 ) }$, where$K ^ { ( 1 ) }$is given by$\begin{array} { r } { K ^ { ( 1 ) } = \sum _ { n \geq n _ { 0 } } K _ { n } } \end{array}$, and$n _ { 0 }$ is sufficiently large so that$2 ^ { - n _ { 0 } } \leq d _ { \mathfrak { s } } ( x , P ) / 2$, say. Then, the fact that (5.16) is well-posed with K replaced by$K ^ { ( 1 ) }$follows from Theorem 5.12. The fact that it is well-posed with K replaced by$K ^ { ( 2 ) }$follows from the fact that$K ^ { ( 2 ) }$ is globally smooth and compactly supported, combined with Proposition 6.9.

To prove that$\kappa _ { \gamma } f$belongs to$\bar { \mathcal { D } } _ { P } ^ { \bar { \gamma } + \beta , ( \eta \wedge \alpha ) + \beta } ( V )$, we proceed as in the proof of Theorem 5.12. We first consider values of  with$\ell \not \in \mathbf { N }$. For such values, one has as before$\mathcal { Q } _ { \ell } \big ( \mathcal { K } _ { \gamma } f \big ) ( x ) = \mathcal { Q } _ { \ell } \mathcal { T } f ( x )$and$\mathcal { Q } _ { \ell } \Gamma _ { x y } \big ( \mathcal { K } _ { \gamma } f \big ) ( y ) =$ $\mathcal { Q } _ { \ell } \mathcal { I } \Gamma _ { x y } f ( y )$ , so that the required bounds on$\| \mathcal { K } _ { \gamma } f ( x ) \| _ { \ell } , ~ \| \dot { \mathcal { K } } _ { \gamma } \dot { f } ( x ) ~ -$ $\Gamma _ { x y } K _ { \gamma } f ( x ) \| _ { \ell } , \| K _ { \gamma } f ( x ) - \bar { K } _ { \gamma } \bar { f } ( x ) \| _ { \ell }$, as well as$\| \mathcal { K } _ { \gamma } f ( x ) - \Gamma _ { x y } \mathcal { K } _ { \gamma } f ( x ) -$ $\bar { \mathcal { K } } _ { \gamma } \bar { f } ( x ) + \bar { \Gamma } _ { x y } \bar { \mathcal { K } } _ { \gamma } \bar { f } ( x ) \| _ { \ell }$follow at once. (Here and below we use the fact that $\left\| x , y \right\| _ { P } ^ { \eta - \gamma } \leq \left\| x , y \right\| _ { P } ^ { ( \eta \wedge \alpha ) - \gamma }$since one only considers pairs$( x , y )$such that $\varrho _ { \mathfrak { s } } \leq 1 . )$

It remains to treat the integer values of . First, we want to show that one has the bound

$$
\| \mathcal {K} _ {\gamma} f (x) \| _ {\ell} \lesssim \| x \| _ {P} ^ {(\bar {\eta} - \ell) \wedge 0},
$$

and similarly for$\| \mathcal { K } _ { \gamma } f - \bar { \mathcal { K } } _ { \gamma } \bar { f } \| _ { \ell }$. For this, we proceed similarly to Theorem 5.12, noting that if$2 ^ { - ( n + 1 ) } \leq \| x \| _ { P }$then, by Remark 3.27, one has the

bound

$$
\left| \left(\mathcal {R} f - \Pi_ {x} f (x)\right) \left(D _ {1} ^ {\ell} K _ {n} (x, \cdot)\right) \right| \lesssim 2 ^ {(| \ell | _ {\mathfrak {s}} - \beta - \gamma) n} \| x \| _ {P} ^ {\eta - \gamma}.
$$

(In this expression,  is a multiindex.) Furthermore, regarding$\mathcal { T } ^ { ( n ) } ( x ) f ( x )$, one has

$$
\| \mathcal {J} ^ {(n)} (x) f (x) \| _ {\ell} \lesssim \sum_ {\zeta > \ell - \beta} \| x \| _ {P} ^ {(\eta - \zeta) \wedge 0} 2 ^ {(\ell - \beta - \zeta) n}.
$$

Combining these two bounds and summing over the relevant values of n yields

$$
\sum_ {2 ^ {- (n + 1)} \leq \| x \| _ {P}} \| \mathcal {K} _ {\gamma} ^ {(n)} f \| _ {\ell} \lesssim \sum_ {\zeta > \ell - \beta} \| x \| _ {P} ^ {\zeta + \beta - \ell + ((\eta - \zeta) \wedge 0)},
$$

which is indeed bounded by$\| x \| _ { P } ^ { ( \bar { \eta } - \ell ) \wedge 0 }$as required since one always has$\zeta \geq$ α. For$\| x \| _ { P } < 2 ^ { - ( n + 1 ) }$on the other hand, we make use of the reconstruction theorem for modelled distributions which yields

$$
\begin{array}{l} \big | \big (\mathcal {R} f - \Pi_ {x} f (x) \big) \big (D _ {1} ^ {\ell} K _ {n} (x, \cdot) \big) + \mathcal {Q} _ {| \ell | _ {\mathfrak {s}}} \mathcal {J} ^ {(n)} (x) f (x) \big | \\ \lesssim \big | \big (\mathcal {R} f \big) \big (D _ {1} ^ {\ell} K _ {n} (x, \cdot) \big) \big | + \sum_ {\zeta \leq | \ell | _ {\mathfrak {s}} - \beta} \big | \big (\Pi_ {x} f (x) \big) \big (D _ {1} ^ {\ell} K _ {n} (x, \cdot) \big) \big | \\ \lesssim 2 ^ {(| \ell | _ {\mathfrak {s}} - \beta - (\eta \wedge \alpha)) n} + \sum_ {\zeta \leq | \ell | _ {\mathfrak {s}} - \beta} 2 ^ {(| \ell | _ {\mathfrak {s}} - \beta - \zeta) n} \| x \| _ {P} ^ {(\eta - \zeta) \wedge 0}. \end{array}
$$

Summing again over the relevant values of n yields again

$$
\sum_ {2 ^ {- (n + 1)} > \| x \| _ {P}} \| \mathcal {K} _ {\gamma} ^ {(n)} f \| _ {\ell} \lesssim \sum_ {\zeta \leq \ell - \beta} \| x \| _ {P} ^ {\zeta + \beta - \ell + ((\eta - \zeta) \wedge 0)},
$$

which is bounded by$\| x \| _ { P } ^ { ( { \bar { \eta } } - { \ell } ) \wedge 0 }$for the same reason as before. The corresponding bounds on$\| \mathcal { K } _ { \gamma } f - \bar { \mathcal { K } } _ { \gamma } \bar { f } \| _ { \ell }$are obtained in virtually the same way.

It therefore remains to obtain the bounds on$\| \mathcal { K } _ { \gamma } f ( x ) - \bar { \mathcal { K } } _ { \gamma } \bar { f } ( x ) \| _ { \ell }$and $\| \mathcal { K } _ { \gamma } f ( x ) - \Gamma _ { x y } \mathcal { K } _ { \gamma } f ( x ) - \bar { \mathcal { K } } _ { \gamma } \bar { f } ( x ) + \bar { \Gamma } _ { x y } \bar { \mathcal { K } } _ { \gamma } \bar { f } ( x ) \| _ { \ell } .$. For this, we proceed exactly as in the proof of Theorem 5.12, but we keep track of the dependency on x and y, rather thanjust the difference. Recall also that we only ever consider the case where$( x , y ) \in \mathcal { R } _ { P }$, so that$\| x , y \| _ { P } > \| x { - } y \| _ { \mathfrak { s } }$. This time, we consider separately the three cases$\begin{array} { r } { 2 ^ { - n } \leq \| x - y \| _ { \mathfrak { s } } , 2 ^ { - n } \in [ \| x - y \| _ { \mathfrak { s } } , \frac { 1 } { 2 } \| x , y \| _ { P } ] } \end{array}$and $2 ^ { - n } \geq { \frac { 1 } { \gamma } } \| x , y \| _ { P }$

When$2 ^ { - n } \leq \| x - y \| _ { \mathfrak { s } }$, we use Remark 3.27 which shows that, when following the exact same considerations as in Theorem 5.12, we always obtain the same bounds, but multiplied by a factor$\| x , y \| _ { P } ^ { \eta - \gamma }$. The case$2 ^ { - n } \leq \| x -$ $y \parallel _ { \mathfrak { s } }$therefore follows at once.

We now turn to the case$2 ^ { - n } \in [ \| x - y \| _ { \mathfrak { s } } , { \frac { 1 } { 2 } } \| x , y \| _ { P } ]$. As in the proof of Theorem 5.12 (see (5.48) in particular), we can again reduce this case to obtaining the bounds

$$
\begin{array}{l} \big | \big (\Pi_ {x} \mathcal {Q} _ {\zeta} \big (\Gamma_ {x y} f (y) - f (x) \big) \big) \big (D _ {1} ^ {k} K _ {n} (x, \cdot) \big) \big | \\ \qquad \lesssim \| x, y \| _ {P} ^ {\eta - \gamma} \sum_ {\delta > 0} \| x - y \| _ {\mathfrak {s}} ^ {\delta + \gamma + \beta - | k | _ {\mathfrak {s}}} 2 ^ {\delta n} \\ \big | \big (\Pi_ {y} f (y) - \mathcal {R} f \big) \big (K _ {n; x y} ^ {k, \gamma} \big) \big |   \lesssim \| x, y \| _ {P} ^ {\eta - \gamma} \sum_ {\delta > 0} \| x - y \| _ {\mathfrak {s}} ^ {\delta + \gamma + \beta - | k | _ {\mathfrak {s}}} 2 ^ {\delta n}, \end{array}
$$

for every$\zeta \leq | k | _ { \mathfrak { s } } - \beta$and where the sums over$\delta$contain only finitely many terms. The first line is obtained exactly as in the proof of Theorem 5.12, so we focus on the second line. Following the same strategy as in the proof of Theorem 5.12, we similarly reduce it to obtaining bounds of the form

$$
\left| \left(\Pi_ {y} f (y) - \mathcal {R} f\right) \left(D _ {1} ^ {\ell} K _ {n} (\bar {y}, \cdot)\right) \right| \lesssim \| x, y \| _ {P} ^ {\eta - \gamma} \sum_ {\delta > 0} \| x - y \| _ {\mathfrak {s}} ^ {\delta + \gamma + \beta - | \ell | _ {\mathfrak {s}}} 2 ^ {\delta n},
$$

where$\bar { y }$is such that$\| x - { \bar { y } } \| _ { 5 } \leq \| x - y \| _ { 5 }$and$\ell$is a multiindex with$| \ell | _ { \mathfrak { s } } \geq$ $| k | _ { \mathfrak { s } } + \bigl ( 0 \vee \left( \gamma + \beta \right) \bigr )$. Since we only consider pairs$( x , y )$such that$\| x - y \| _ { \mathfrak { s } } \leq$ ${ \frac { 1 } { 2 } } \left\| x , y \right\| _ { P }$, one has$\| y , { \bar { y } } \| _ { P } \sim \| x , y \| _ { P }$. As a consequence, we obtain as in the proof of Theorem 5.12

$$
\begin{array}{l} \big | \big (\Pi_ {\bar {y}} \big (\Gamma_ {\bar {y} y} f (y) - f (\bar {y}) \big) \big) \big (D _ {1} ^ {\ell} K _ {n} (\bar {y}, \cdot) \big) \big | \\ \lesssim \| x, y \| _ {P} ^ {\eta - \gamma} \sum_ {\zeta \leq \gamma} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \zeta} 2 ^ {(| \ell | _ {\mathfrak {s}} - \zeta - \beta) n}. \end{array}
$$

Furthermore, since$2 ^ { - n } \leq \| x , y \| _ { P }$, we obtain as in (6.6) the bound

$$
\left| \left(\Pi_ {\bar {y}} f (\bar {y}) - \mathcal {R} f\right) \left(D _ {1} ^ {\ell} K _ {n} (\bar {y}, \cdot)\right) \right| \lesssim 2 ^ {(| \ell | _ {\mathfrak {s}} - \beta - \gamma) n} \| x, y \| _ {P} ^ {\eta - \gamma}.
$$

The rest of the argument is then again exactly the same as for Theorem 5.12. The corresponding bounds on the distance between$\kappa _ { \gamma } f$$\bar { \kappa } _ { \gamma } \bar { f }$follows analogously.

It remains to consider the case$\textstyle 2 ^ { - n } \geq { \frac { 1 } { 2 } } \| x , y \| _ { P }$. In this case, we proceed as before but, in order to bound the term involving$\Pi _ { y } f ( y ) - { \mathcal { R } } f$, we simply use the triangle inequality to rewrite it as

$$
\big | \big (\Pi_ {y} f (y) - \mathcal {R} f \big) \big (K _ {n; x y} ^ {k, \gamma} \big) \big | \leq \big | \big (\Pi_ {y} f (y) \big) \big (K _ {n; x y} ^ {k, \gamma} \big) \big | + \big | \big (\mathcal {R} f \big) \big (K _ {n; x y} ^ {k, \gamma} \big) \big |.
$$

We then use again the representation (5.28) for$K _ { n ; x y } ^ { k , \gamma }$, together with the bounds

$$
\begin{array}{c} \big | \big (\mathcal {R} f \big) \big (D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot) \big) \big | \lesssim 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - (\alpha \wedge \eta)) n}, \\ \big | \big (\Pi_ {y} f (y) \big) \big (D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot) \big) \big | \lesssim \sum_ {\alpha \leq \zeta <   \gamma} \| y \| _ {P} ^ {(\eta - \zeta) \wedge 0} 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - \zeta) n}. \end{array}
$$

Here, the first bound is a consequence of the reconstruction theorem for singular modelled distributions, while the second bound follows from Definition 6.2. Since

$$
2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - (\alpha \wedge \eta)) n} \leq 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - \alpha) n} + 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - \eta) n},
$$

and since$\eta \in [ \alpha , \gamma )$by assumption, we see that the first bound is actually of the same form as the second, so that

$$
\big | \big (\Pi_ {y} f (y) - \mathcal {R} f \big) \big (D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot) \big) \big | \lesssim \sum_ {\alpha \leq \zeta <   \gamma} \| y \| _ {P} ^ {(\eta - \zeta) \wedge 0} 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - \zeta) n},
$$

where the sum runs over finitely many terms. Performing the integration in (5.28) and using the bound (5.31), we conclude that

$$
\big | \big (\Pi_ {y} f (y) - \mathcal {R} f \big) \big (K _ {n; x y} ^ {k, \gamma} \big) \big | \lesssim \sum_ {\zeta ; \ell} \| x - y \| _ {\mathfrak {s}} ^ {| \ell | _ {\mathfrak {s}}} \| x, y \| _ {P} ^ {(\eta - \zeta) \wedge 0} 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - \zeta) n},
$$

where we used the fact that$\| y \| _ { P } \sim \| x , y \| _ { P }$. Here, the sum runs over exponents$\zeta$as before and multiindices  such that$| k + \ell | _ { \mathfrak { s } } > \beta + \gamma$. Summing this expression over the relevant range of values for n, we have

$$
\begin{array}{c} \sum_ {2 ^ {- n} \geq \| x, y \| _ {P}} \big | \big (\Pi_ {y} f (y) - \mathcal {R} f \big) \big (K _ {n; x y} ^ {k, \gamma} \big) \big | \lesssim \sum_ {\zeta ; \ell} \| x - y \| _ {\mathfrak {s}} ^ {| \ell | _ {\mathfrak {s}}} \| x, y \| _ {P} ^ {(\eta \wedge \zeta) + \beta - | k + \ell | _ {\mathfrak {s}}} \\ \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma + \beta - | k | _ {\mathfrak {s}}} \| x, y \| _ {P} ^ {(\eta \wedge \alpha) - \gamma}, \end{array}
$$

where we used the fact that$\begin{array} { r } { \| x - y \| _ { \mathfrak { s } } \leq \frac { 1 } { 2 } \| x , y \| _ { P } } \end{array}$to obtain the second bound. Again, the corresponding bounds on the distance between$\kappa _ { \gamma } f$and$\bar { \kappa } _ { \gamma } \bar { f }$ follow analogously, thus concluding the proof.□

Remark$6 . I 7$The condition$\alpha \wedge \eta > - \mathfrak { m }$is only required in order to be able to apply Proposition 6.9. There are some situations in which, even though $\alpha \wedge \eta < - \mathfrak { m }$, there exists a canonical element$\mathcal { R } f \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha \wedge \eta }$extending$\tilde { \mathcal { R } } f$. In such a case, Proposition 6.16 still holds and the bound (6.20) holds provided that the corresponding bound holds for$\mathcal { R } f - \bar { \mathcal { R } } \bar { f }$

## 7 Solutions to semilinear (S)PDEs

In order to solve a typical semilinear PDE of the type

$$
\partial_ {t} u = A u + F (u), \quad u (0) = u _ {0},
$$

a standard methodology is to rewrite it in its mild form as

$$
u (t) = S (t) u _ {0} + \int_ {0} ^ {t} S (t - s) F (u (s)) d s,
$$

where$S ( t ) = e ^ { A t }$is the semigroup generated by A. One then looks for some family of spaces$\mathcal { X } _ { T }$of space-time functions (with$\mathcal { X } _ { T }$containing functions up to time$T )$such that the map given by

$$
\big (\mathcal {M} u \big) (t) = S (t) u _ {0} + \int_ {0} ^ {t} S (t - s) F (u (s)) d s,
$$

is a contraction in$\mathcal { X } _ { T }$, provided that the terminal time$T$is sufficiently small. (As soon as$F$is nonlinear, the notion of “sufficiently small” typically depends on the choice of$u _ { 0 }$, thus leading to a local solution theory.) The main step of such an argument is to show that the linear map S given by

$$
\big (S v \big) (t) = \int_ {0} ^ {t} S (t - s)   v (s)   d s,
$$

can be made to have arbitrarily small norm as$T  0$as a map from some suitable space$\mathcal { V } _ { T }$into$\mathcal { X } _ { T }$, where$\mathcal { V } _ { T }$is chosen such that$F$is then locally Lipschitz continuous as a map from$\mathcal { X } _ { T }$to$\mathcal { V } _ { T }$, with some uniformity in$T \in$ (0, 1 , say.

The aim of this section is to show that, in many cases, this methodology can still be applied when looking for solutions in$\dot { \mathcal { D } } _ { P } ^ { \gamma , \eta }$for suitable exponents $\gamma$and$\eta .$, and for suitable regularity structures allowing to formulate a fixed point map of the type of$\mathcal { M } _ { F }$. At this stage, all of our arguments are purely deterministic. However, they rely on a choice of model for the given regularity structure one works with, which in many interesting cases can be built using probabilistic techniques.

## 7.1 Short-time behaviour of convolution kernels

From now on, we assume that we work with$d - 1$spatial coordinates, so that the solution u we are looking for is a function on$\mathbf { R } ^ { d }$. (Or rather a subset of it.) In order to be able to reuse the results of Sect. 5, we also assume that$S ( t )$ is given by an integral operator with kernel$G ( t , \cdot )$. For simplicity, assume that the scaling s and exponent$\beta$are such that, as a space-time function,$G$ furthermore satisfies the assumptions of Sect. 5. (Typically, one would actually write$G = K + R$, where R is smooth and a K satisfies the assumptions of Sect. 5. We will go into more details in Sect. 8 below.) In this section, time plays a distinguished role. We will therefore denote points in$\mathbf { R } ^ { d }$either by $( t , x )$with$t \in \mathbf { R }$and$x \in \mathbf { R } ^ { d - 1 }$or by$z \in \mathbf { R } ^ { d }$, depending on the context.

In our setting, we have so far been working solely with modelled distributions defined on all of$\mathbf { R } ^ { d }$, so it not clear a priori how a map like S should be defined when acting on (possibly singular) modelled distributions. One natural way of reformulating it is by writing

$$
S v = G * (R ^ {+} v),\tag{7.1}
$$

where$\pmb { R } ^ { + } : \mathbf { R } \times \mathbf { R } ^ { d - 1 }  \mathbf { R }$is given by$R ^ { + } ( t , x ) = 1 \mathrm { f o r } t > 0$and$R ^ { + } ( t , x ) =$ 0 otherwise.

From now on, we always take$P \subset \mathbf { R } ^ { d }$to be the hyperplane defined by “time $0 ^ { \circ }$, namely$P = \{ ( t , x ) : t = 0 \}$, which has effective codimension m$\mathbf { \xi } = \mathfrak { s } _ { 1 }$ We then note that the obvious interpretation of$\pmb { R } ^ { + }$as a modelled distribution yields an element of$\mathcal { D } _ { P } ^ { \infty , \infty }$, whatever the details of the underlying regularity structure. Indeed, the second term in (6.2) always vanishes identically, while the first term is non-zero only for$\ell = 0$, in which case it is bounded for every choice of η. It then follows immediately from Proposition 6.12 that the map $v \mapsto R ^ { + } v$is always bounded as a map from$\mathcal { D } _ { P } ^ { \gamma , \eta }$into$\mathcal { D } _ { P } ^ { \gamma , \eta }$. Furthermore, this map does not even rely on a choice of product, since$\pmb { R } ^ { + }$is proportional to 1, which is always neutral for any product.

In order to avoid the problem of having to control the behaviour of functions at infinity, we will from now on assume that we have a symmetry group$\mathcal { S }$ acting on$\mathbf { R } ^ { d }$in such a way that

The time variable is left unchanged in the sense that there is an action$\tilde { T }$of $\mathcal { S }$on$\mathbf { R } ^ { d - 1 }$such that$T _ { g } ( t , x ) = ( t , \tilde { T } _ { g } x )$

The fundamental domain K of the action$\tilde { T }$is compact in$\mathbf { R } ^ { d - 1 }$

We furthermore assume that$\mathcal { S }$acts on our regularity structure$\mathcal { T }$and that the model ( , ) for$\mathcal { T }$is adapted to its action. All the modelled distributions considered in the remainder of this section will always be assumed to be symmetric, and when we write$\mathcal { D } ^ { \gamma } , \mathcal { D } _ { P } ^ { \gamma , \eta }$, etc, we always refer to the closed subspaces consisting of symmetric functions.

One final ingredient used in this section will be that the kernels arising in the context of semilinear PDEs are non-anticipative in the sense that

$$
t <   s \Rightarrow K ((t, x), (s, y)) = 0.
$$

We furthermore use the notations$O = [ - 1 , 2 ] \times \mathbf { R } ^ { d - 1 }$and$O _ { T } = ( - \infty , T ] \times$ $\mathbf { R } ^ { d - 1 }$. Finally, we will use the shorthands$\Vert \cdot \Vert _ { \gamma , \eta ; T }$as a shorthand for$\| \cdot \| _ { \gamma , \eta ; O _ { T } }$ and similarly for$\| \cdot \| _ { \gamma ; T }$. The backbone of our argument is then provided by Proposition 3.31 which guarantees that one can give bounds on$\kappa _ { \gamma } f$on$O _ { T }$ solely in terms of the behaviour of$f$on$O _ { T }$

With all of these preliminaries in place, the main result of this subsection is the following.

Theorem 7.1 Let$\gamma > 0$and let K be a non-anticipative kernel satisfying Assumptions 5.1 and 5.4for some$\beta > 0$and$r > \gamma + \beta$. Assumefurthermore that the regularity structure$\mathcal { T }$comes with an integration map$\mathcal { T }$of order$\beta$ acting on some sector$V$of regularity$\alpha > - \mathfrak { s } _ { 1 }$and assume that the models $Z = ( \Pi , \Gamma )$and$\bar { z } = ( \bar { \Pi } , \bar { \Gamma } )$both realise K for I on$V .$. Then, there exists a constant C such that,for every$T \in ( 0 , 1 ]$, the bounds

$$
\begin{array}{c} \| \mathcal {K} _ {\gamma} \boldsymbol {R} ^ {+} f \| _ {\gamma + \beta , \bar {\eta}; T} \leq C T ^ {\kappa / \mathfrak {s} _ {1}} \| f \| _ {\gamma , \eta ; T}, \\ \| \mathcal {K} _ {\gamma} \boldsymbol {R} ^ {+} f; \bar {\mathcal {K}} _ {\gamma} \boldsymbol {R} ^ {+} \bar {f} \| _ {\gamma + \beta , \bar {\eta}; T} \leq C T ^ {\kappa / \mathfrak {s} _ {1}} \big (\| f; \bar {f} \| _ {\gamma , \eta ; T} + \| Z, \bar {z} \| _ {\gamma ; O} \big), \end{array}
$$

hold, provided that$f \in { \mathcal { D } } _ { P } ^ { \gamma , \eta } ( V ; \Gamma )$and$\bar { f } \in \mathcal { D } _ { P } ^ { \gamma , \eta } ( V ; \bar { \Gamma } )$for some$\eta > - \mathfrak { s } _ { 1 }$ Here, η and κ are such that$\bar { \eta } = ( \eta \wedge \alpha ) + \beta - \kappa$and$\kappa > 0 .$

In the first bound, the proportionality constant depends only on$\Vert Z \Vert _ { \gamma ; O }$ while in the second bound it is also allowed to depend on$\| f \| _ { \gamma , \eta ; T } + \| \bar { f } \| _ { \gamma , \eta ; T }$

One of main ingredients of the proof is the fact that$( \mathcal { K } _ { \gamma } R _ { + } f ) ( t , x )$is welldefined using only the knowledge of$f$up to time t. This is a consequence of the following result, which is an improved version of Lemma 6.7.

Proposition 7.2 In the setting of Lemma 6.7, and assuming that$\varphi ( 0 ) \neq 0 ,$ one has the improved bound

$$
\big | \big (\mathcal {R} f - \Pi_ {x} f (x) \big) (\psi_ {x} ^ {\lambda}) \big | \lesssim \lambda^ {\gamma} \sup _ {y, z \in \operatorname{supp}} \sup _ {\psi_ {x} ^ {\lambda} \ell <   \gamma} \frac {\| f (x) - \Gamma_ {x y} f (y) \| _ {\ell}}{\| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell}},\tag{7.2}
$$

where the proportionality constant is as in Lemma 6.7.

Proof Since the statement is linear in$f _ { \cdot }$, we can assume without loss of generality that the right hand side of (7.2) is equal to 1. Let$\varphi$be the scaling function of a wavelet basis of$\mathbf { R } ^ { d }$and let$\varphi _ { y } ^ { n }$be defined by

$$
\varphi_ {y} ^ {n} (z) = \varphi \big (\mathcal {S} _ {\mathfrak {s}} ^ {2 ^ {- n}} (z - x) \big).
$$

Note that this is slightly different from the definition of the$\varphi _ { y } ^ { n , { \mathfrak { s } } }$in Sect. 3.1! The reason for this particular scaling is that it ensures that$\begin{array} { r } { \sum _ { y \in \Lambda _ { n } ^ { \mathfrak { s } } } \varphi _ { y } ^ { n } ( z ) = 1 } \end{array}$ Again, we have coefficients$a _ { k }$such that, similarly to (3.13),

$$
\varphi_ {y} ^ {n - 1} (z) = \sum_ {k \in \mathcal {K}} a _ {k} \varphi_ {y + 2 ^ {- n} k} ^ {n} (z),
$$

for some finite set${ \mathcal { K } } \subset { \mathbf { Z } } ^ { d }$, and this time our normalisation ensures that $\begin{array} { r } { \sum _ { k \in \mathcal { K } } a _ { k } = 1 } \end{array}$

For every$n \geq 0$, define

$$
\Lambda_ {n} ^ {\psi} = \{y \in \Lambda_ {n} ^ {\mathfrak {s}}: \operatorname{supp} \varphi_ {y} ^ {n} \cap \operatorname{supp} \psi_ {x} ^ {\lambda} \neq \emptyset \},
$$

and, for any$y \in \Lambda _ { n } ^ { \psi }$, we denote by$y | _ { n }$some point in the intersection of these two supports. There then exists some constant C depending only on our choice of scaling function such that$\| y - y | _ { n } \| _ { \mathfrak { s } } \leq C 2 ^ { - n }$. Let now$R _ { n }$be defined by

$$
R _ {n} \stackrel {{\text { def }}} {{=}} \sum_ {y \in \Lambda_ {n} ^ {\psi}} \big (\mathcal {R} f - \Pi_ {y | _ {n}} f (y | _ {n}) \big) (\psi_ {x} ^ {\lambda} \varphi_ {y} ^ {n}),
$$

and let$n _ { 0 }$be the smallest value such that$2 ^ { - n _ { 0 } } \leq \lambda$. It is then straightforward to see that one has

$$
\begin{array}{l} \big | \big (\mathcal {R} f - \Pi_ {x} f (x) \big) (\psi_ {x} ^ {\lambda}) - R _ {n _ {0}} \big | \\ = \Big | \sum_ {y \in \Lambda_ {n _ {0}} ^ {\psi}} \big (\Pi_ {x} f (x) - \Pi_ {y | _ {n}} f (y | _ {n}) \big) (\psi_ {x} ^ {\lambda} \varphi_ {y} ^ {n}) \Big | \lesssim \lambda^ {\gamma}. \end{array}\tag{7.3}
$$

Furthermore, using as in Sect. 3.1 the shortcut$z = y + 2 ^ { - n \mathfrak { s } } k$, one then has for every$n \geq 1$the identity

$$
\begin{array}{c} R _ {n - 1} = \sum_ {y \in \Lambda_ {n - 1} ^ {\psi}} \sum_ {k \in \mathcal {K}} a _ {k} \big (\mathcal {R} f - \Pi_ {y | _ {n - 1}} f (y | _ {n - 1}) \big) (\psi_ {x} ^ {\lambda} \varphi_ {z} ^ {n}) \\ = \sum_ {y \in \Lambda_ {n - 1} ^ {\psi}} \sum_ {k \in \mathcal {K}} a _ {k} \big (\mathcal {R} f - \Pi_ {z | _ {n}} f (z | _ {n}) \big) (\psi_ {x} ^ {\lambda} \varphi_ {z} ^ {n}) \end{array}
$$

$$
\begin{array}{l} + \sum_ {y \in \Lambda_ {n - 1} ^ {\psi}} \sum_ {k \in \mathcal {K}} a _ {k} \big (\Pi_ {z | _ {n}} f (z | _ {n}) - \Pi_ {y | _ {n - 1}} f (y | _ {n - 1}) \big) (\psi_ {x} ^ {\lambda} \varphi_ {z} ^ {n}) \\ = R _ {n} + \sum_ {y \in \Lambda_ {n - 1} ^ {\psi}} \sum_ {k \in \mathcal {K}} a _ {k} \big (\Pi_ {z | _ {n}} f (z | _ {n}) - \Pi_ {y | _ {n - 1}} f (y | _ {n - 1}) \big) (\psi_ {x} ^ {\lambda} \phi_ {z} ^ {n}). \end{array}\tag{7.4}
$$

Note now that, in (7.4), one has$\| z | _ { n } - y | _ { n - 1 } \| _ { \mathfrak { s } } \leq \tilde { C } 2 ^ { - n }$for some constant $\tilde { C }$. It furthermore follows from the scaling properties of our functions that if $n \geq n _ { 0 }$and$\tau \in T _ { \ell }$with$\| \tau \| = 1$, one has

$$
\left| \left(\Pi_ {y} \tau\right) (\psi_ {x} ^ {\lambda} \varphi_ {z} ^ {n}) \right| \lesssim \lambda^ {- | \mathfrak {s} |} 2 ^ {- \ell n - | \mathfrak {s} | n},
$$

with a proportionality constant that is uniform over all y and z such that $\| y - z \| _ { \mathfrak { s } } \le \tilde { C } 2 ^ { - n }$. As a consequence, each summand in the last term of (7.4) is bounded by some fixed multiple of$\lambda ^ { - | \mathfrak { s } | } 2 ^ { - \gamma n - | \mathfrak { s } | n }$. Since furthermore the number of terms in this sum is bounded by a fixed multiple of$( 2 ^ { n } \lambda ) ^ { | \mathfrak { s } | }$, this yields the bound

$$
\left| R _ {n - 1} - R _ {n} \right| \lesssim 2 ^ {- \gamma n}.\tag{7.5}
$$

Finally, writing$S _ { n } ( \psi )$for the$2 ^ { - n }$-fattening of the support of$\psi _ { x } ^ { \lambda }$, we see that, as a consequence of Lemma 6.7 and using a similar argument to what we have just used to bound$R _ { n - 1 } - R _ { n }$, one has

$$
| R _ {n} | \lesssim 2 ^ {- \gamma n} \| f \| _ {\gamma ; S _ {n} (\psi)}.
$$

This is the only time that we use information on f (slightly) away from the support of$\psi _ { x } ^ { \lambda }$. This however is only used to conclude that l$\begin{array} { r } { \operatorname* { m } _ { n \to \infty } | R _ { n } | = 0 } \end{array}$ and no explicit bound on this rate of convergence is required. Combining this with (7.5) and (7.3), the stated bound follows.□

ProofofTheorem 7.1 First of all, we see that, as a consequence of Proposition 7.2, we can exploit the fact that K is non-anticipative to strengthen (6.20) to

$$
\| \mathcal {K} _ {\gamma} f; \bar {\mathcal {K}} _ {\gamma} \bar {f} \| _ {\bar {\Gamma}, \bar {\eta}; T} \lesssim \| f; \bar {f} \| _ {\gamma , \eta ; T} + \| \Pi - \bar {\Pi} \| _ {\gamma ; O} + \| \Gamma - \bar {\Gamma} \| _ {\bar {\Gamma}; O},\tag{7.6}
$$

in the particular case where furthermore$f ( t , x ) = 0$for$t < 0$and similarly for${ \bar { f } } .$. Of course, a similar bound also holds for$\| \mathcal { K } _ { \gamma } f \| _ { \bar { \Gamma } , \bar { \eta } ; T }$

The main ingredient of the proof is the following remark. Since, provided that$\eta > - \mathfrak { s } _ { 1 }$, we know that$\mathcal { R } \dot { R } ^ { + } f \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha \wedge \eta }$by Proposition 6.9, it follows that

the quantity

$$
z \mapsto \int_ {\mathbf {R} ^ {d}} D _ {1} ^ {k} K (z, \bar {z}) \big (\mathcal {R} \boldsymbol {R} ^ {+} f \big) (\bar {z}) d \bar {z},
$$

is continuous as soon as$| k | _ { \mathfrak { s } } < ( \alpha \wedge \eta ) + \beta$. Furthermore, since K is non anticipative and$\mathscr { R } R ^ { + } f \equiv 0$for negative times, this quantity vanishes there.

As a consequence, we can apply Lemma 6.5 which shows that the bound (7.6) can in this case be strengthened to the additional bounds

$$
\begin{array}{c} \sup _ {z \in O _ {T}} \sup _ {\ell <   \gamma + \beta} \frac {\| \mathcal {K} _ {\gamma} \boldsymbol {R} ^ {+} f (z) \| _ {\ell}}{\| z \| _ {P} ^ {(\eta \wedge \alpha) + \beta - \ell}} \lesssim \| f \| _ {\gamma , \eta ; T}, \\ \sup _ {z \in O _ {T}} \sup _ {\ell <   \gamma + \beta} \frac {\| \mathcal {K} _ {\gamma} \boldsymbol {R} ^ {+} f (z) - \bar {\mathcal {K}} _ {\gamma} \boldsymbol {R} ^ {+} \bar {f} (z) \| _ {\ell}}{\| z \| _ {P} ^ {(\eta \wedge \alpha) + \beta - \ell}} \lesssim \| f;   \bar {f} \| _ {\gamma , \eta ; T} + \| Z, \bar {z} \| _ {\gamma ; O}. \end{array}
$$

Since, for every$z , { \bar { z } } \in O _ { T }$, one has$\| z \| _ { P } \leq T ^ { 1 / \mathfrak { s } _ { 1 } }$as well as$\| z , \bar { z } \| _ { P } \leq T ^ { 1 / { \mathfrak { s } } _ { 1 } }$ we can combine these bounds with the definition of the norm$\| \cdot \| _ { \gamma + \beta , \bar { \eta } ; T }$to show that one has

$$
\| \mathcal {K} _ {\gamma} \boldsymbol {R} ^ {+} f \| _ {\gamma + \beta , \bar {\eta}; T} \lesssim T ^ {\kappa / \mathfrak {s} _ {1}} \| f \| _ {\gamma , \eta ; T},
$$

and similarly for$\| \mathcal { K } _ { \gamma } R ^ { + } f ; \bar { \mathcal { K } } _ { \gamma } R ^ { + } \bar { f } \| _ { \gamma + \beta , \bar { \eta } ; T }$, thus concluding the proof.

In all the problems we consider in this article, the Green’s function of the linear part of the equation, i.e. the kernel of$\displaystyle { \mathcal { L } } ^ { - 1 }$where$\mathcal { L }$is as in (1.2), can be split into a sum of two terms, one of which satisfies the assumptions of Sect. 5 and the other one of which is smooth (see Lemma 5.5). Given a smooth kernel $R \colon \mathbf { R } ^ { d } \times \mathbf { R } ^ { d }  \mathbf { R }$that is supported in$\{ ( z , \bar { z } ) ~ : ~ \| z - \bar { z } \| _ { \mathfrak { s } } \le L \}$for some $L > 0$, and a regularity structure$\mathcal { T }$containing$\mathcal { T } _ { \mathfrak { s } , d }$as usual, we can define an operator$R _ { \gamma } \colon { \mathcal { C } } _ { \mathfrak { s } } ^ { \alpha }  { \mathcal { D } } ^ { \gamma }$by

$$
\left(R _ {\gamma} \xi\right) (z) = \sum_ {| k | _ {\mathfrak {s}} <   \gamma} \frac {X ^ {k}}{k !} \int_ {\mathbf {R} ^ {d}} D _ {1} ^ {k} R (z, \bar {z}) \xi (\bar {z}) d \bar {z}.\tag{7.7}
$$

(As usual, this integral should really be interpreted as$\xi ( D _ { 1 } ^ { k } R ( z , \cdot ) )$, but the above notation is much more suggestive.) The fact that this is indeed an element of$\mathcal { D } ^ { \gamma }$is a consequence of the fact that R is smooth in both variables, so that it follows from Lemma 2.12. The following result is now straightforward:

Lemma 7.3 Let R be a smooth kernel and consider a symmetric situation as above. Iffurthermore R is non-anticipative, then the bounds

$$
\begin{array}{c} \| R _ {\gamma} \mathcal {R} \boldsymbol {R} ^ {+} f \| _ {\gamma + \beta , \bar {\eta}; T} \leq C T \| f \| _ {\gamma , \eta ; T}, \\ \| R _ {\gamma} \mathcal {R} \boldsymbol {R} ^ {+} f; R _ {\gamma} \bar {\mathcal {R}} \boldsymbol {R} ^ {+} \bar {f} \| _ {\gamma + \beta , \bar {\eta}; T} \leq C T \big (\| f; \bar {f} \| _ {\gamma , \eta ; T} + \| Z; \bar {z} \| _ {\gamma , O} \big), \end{array}
$$

holds uniformly over all$T \leq 1$

Proof Since R is assumed to be non-anticipative, one has$\begin{array} { r } { \big ( R _ { \gamma } \mathcal { R } R ^ { + } f \big ) ( t , x ) = } \end{array}$ 0 for every$t \leq 0$. Furthermore, the map$( t , x ) \mapsto \bigl ( R _ { \gamma } \mathscr { R } R ^ { + } f \bigr ) ( t , x )$is smooth  (in the classical sense of a map taking values in a finite-dimensional vector space!), so that the claim follows at once. Actually, it would even be true with $T$replaced by an arbitrarily large power of$T$in the bound on the right hand side.□

## 7.2 The effect of the initial condition

One of the obvious features of PDEs is that they usually have some boundary data. In this article, we restrict ourselves to spatially periodic situations, but even such equations have some boundary data in the form of their initial condition. When they are considered in their mild formulation, the initial condition enters the solution to a semilinear PDE through a term of the form$S ( t ) u _ { 0 }$for some function (or distribution)$u _ { 0 }$on$\mathbf { R } ^ { d - 1 }$and S the semigroup generated by the linear evolution.

All of the equations mentioned in the introduction are nonlinear perturbations of the heat equation. More generally, their linear part is of the form

$$
\mathcal {L} = \partial_ {t} - Q (\nabla_ {x}),
$$

where$Q$is a polynomial of even degree which is homogeneous of degree$2 q$ for some scaling$\bar { \mathfrak { s } }$on$\mathbf { R } ^ { d - 1 }$and some integer$q > 0$. (In our case, this would always be the Euclidean scaling and one has$q = 1 . )$In this case, the operator $\mathcal { L }$itself has the property that

$$
\mathcal {L} \mathcal {S} _ {\mathfrak {s}} ^ {\delta} \varphi = \delta^ {2 q} \mathcal {S} _ {\mathfrak {s}} ^ {\delta} \mathcal {L} \varphi .\tag{7.8}
$$

where s is the scaling on$\mathbf { R } ^ { d } = \mathbf { R } \times \mathbf { R } ^ { d - 1 }$given by${ \mathfrak { s } } = ( 2 q , { \bar { \mathfrak { s } } } )$). Denote by$G$ the Green’s function$G$of$\mathcal { L }$which is a distribution satisfying$\mathcal { L } G = \delta _ { 0 }$in the distributional sense and$G ( x , t ) = 0$for$t \leq 0$. Assuming that$\mathcal { L }$is such that these properties define$G$uniquely (which is the case if$\mathcal { L }$is hypoelliptic), it follows from (7.8) and the scaling properties of the Dirac distribution that$G$

has exact scaling property

$$
G (\mathcal {S} _ {\mathfrak {s}} ^ {\delta} z) = \delta^ {| \bar {\mathfrak {s}} |} G (z),\tag{7.9}
$$

which is precisely of the form (5.7) with$\beta = 2 q$. Under well-understood assumptions on$Q , { \mathcal { L } }$is known to be hypoelliptic [65], so that its Green’s function$G$is smooth. In this case, the following lemma applies.

Lemma 7.4 If G satisfies (7.9), is non-anticipative, and is smooth then there exists a smoothfunction$\hat { G } \colon  { \mathbf { R } } ^ { d } \to  { \mathbf { R } }$such that one has the identity

$$
G (x, t) = t ^ {- \frac {| \bar {\mathfrak {s}} |}{2 q}} \hat {G} (\mathcal {S} _ {\bar {\mathfrak {s}}} ^ {t ^ {1 / 2 q}} x),\tag{7.10}
$$

and such that, for every$( d - 1 )$-dimensional multiindex k and every$n > 0$ there exists a constant C such that the bound

$$
| D ^ {k} \hat {G} (y) | \leq C (1 + | y | ^ {2}) ^ {- n},\tag{7.11}
$$

holds uniformly over$y \in \mathbf { R } ^ { d - 1 }$

Proof The existence of$\hat { G }$such that (7.10) holds follows immediately from the scaling property (7.9). The bound (7.11) can be obtained by noting that, since G is smooth off the origin and satisfies$G ( x , t ) = 0$for$t \leq 0$, one has, for every$n > 0$, a bound of the type

$$
| D _ {x} ^ {k} G (x, t) | \lesssim t ^ {n},\tag{7.12}
$$

uniformly over all$x \in \mathbf { R } ^ { d - 1 }$with$\| \boldsymbol { x } \| _ { \bar { \mathfrak { s } } } = 1$. It follows from (7.10) that

$$
D ^ {k} G (x, t) = t ^ {- \frac {| \bar {\mathfrak {s}} | + | k | _ {\bar {\mathfrak {s}}}}{2 q}} \big (D ^ {k} \hat {G} \big) \big (\mathcal {S} _ {\bar {\mathfrak {s}}} ^ {t ^ {1 / 2 q}} x \big).
$$

Setting$y = S _ { s } ^ { t ^ { 1 / 2 q } } x$and noting that$\| y \| _ { \bar { \mathfrak { s } } } = 1 / t ^ { 1 / 2 q } \ \mathrm { i f } \ \| x \| _ { \bar { \mathfrak { s } } } = 1$, it remains to combine this with (7.12) to obtain the required bound.□

Given a function (or distribution)$u _ { 0 }$on$\mathbf { R } ^ { d - 1 }$with sufficiently nice behaviour at infinity, we now denote by$G u _ { 0 }$its “harmonic extension”, given by

$$
\bigl (G u _ {0} \bigr) (x, t) = \int_ {\mathbf {R} ^ {d - 1}} G (x - y, t)   u _ {0} (y)   d y.\tag{7.13}
$$

(Of course this is to be suitably interpreted when$u _ { 0 }$is a distribution.) This expression does define a function of$( t , x )$which, thanks to Lemma 7.4, is smooth everywhere except at$t = 0$. As in Sect. 2.2, we can lift$G u _ { 0 }$at every point to an element of the model space T (provided of course that$\mathcal { T } _ { d , \mathfrak { s } } \subset \mathcal { T }$ which we always assume to be the case) by considering its truncated Taylor expansion. We will from now on use this point of view without introducing a new notation.

We can say much more about the function$G u _ { 0 }$, namely we can find out precisely to which spaces$\mathcal { D } _ { P } ^ { \gamma , \eta }$it belongs. This is the content of the following Lemma, variants of which are commonplace in the PDE literature. However, since our spaces are not completely standard and since it is very easy to prove, we give a sketch of the proof here.

Lemma 7.5 Let$u _ { 0 } \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha } ( \mathbf { R } ^ { d - 1 } )$be periodic. Then, for every α$\notin \mathbf { N } ,$, the function$\boldsymbol { v } = G \boldsymbol { u } _ { 0 }$defined in (7.13) belongs to$\mathcal { D } _ { P } ^ { \gamma , \alpha }$for every$\gamma > ( \alpha \lor 0 )$

Proof We first aim to bound the various directional derivatives of v. In the case$\alpha < 0$, it follows immediately from the scaling and decay properties of $G$, combined with the definition of$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$that, for any fixed$( t , x )$, one has the bound

$$
\left| \left(G u _ {0}\right) (x, t) \right| \lesssim t ^ {\frac {\alpha}{2}},
$$

valid uniformly over x (by the periodicity of$u _ { 0 } )$and over$t \in ( 0 , 1 ]$. As a consequence (exploiting the fact that, as an operator,$G$commutes with all spatial derivatives and that one has the identity$\partial _ { t } G u _ { 0 } = Q ( \nabla _ { x } ) G u _ { 0 } )$, one also obtains the bound

$$
\left| \left(D ^ {k} G u _ {0}\right) (x, t) \right| \lesssim t ^ {\frac {\alpha - | k | _ {\mathfrak {S}}}{2}},\tag{7.14}
$$

where k is any d-dimensional multiindex (i.e. we also admit time derivatives).

For$\alpha > 0$, we use the fact that elements in$\mathcal { C } _ { \bar { \mathfrak { s } } } ^ { \alpha }$can be characterised recursively as those functions whose kth distributional derivatives belong to${ \mathcal { C } } _ { \bar { \mathfrak { s } } } ^ { \alpha - | k | _ { \bar { \mathfrak { s } } } }$ It follows that the bound (7.14) then still holds for$| k | _ { \mathfrak { s } } > \alpha$, while one has $| ( D ^ { k } G u _ { 0 } ) ( x , t ) | \lesssim 1$for$| k | _ { 5 } < \alpha$. This shows that the first bound in (6.2) does indeed hold for every integer value  as required.

In this particular case, the second bound in (6.2) is then an immediate consequence of the first by making use of the generalised Taylor expansion from Proposition 11.1. Since the argument is very similar to the one already used for example in the proof of Lemma 5.18, we omit it here.□

Starting from a Green’s function G as above, we would like to apply the theory developed in Sect. 5. From now on, we will assume that we are in the situation where we have a symmetry given by a discrete subgroup$\mathcal { S }$of the group of isometries of$\mathbf { R } ^ { d - 1 }$with compact fundamental domain${ \mathcal { \kappa } } .$. This covers the case of periodic boundary conditions, when$\mathcal { S }$is a subgroup of the group of translations, but it also covers Neumann boundary conditions in the case where$\mathcal { S }$is a reflection group.

Remark 7.6 One could even cover Dirichlet boundary conditions by reflection, but this would require a slight modification of Definition 3.33. In order to simplify the exposition, we refrain from doing so.

To conclude this subsection, we show how, in the presence of a symmetry with compact fundamental domain, a Green’s function$G$as above can be decomposed in a way similar to Lemma 5.5, but such that R is also compactly supported. We assume therefore that we are given a symmetry$\mathcal { S }$acting on$\mathbf { R } ^ { d - 1 }$with compact fundamental domain and that$G$respects this symmetry in the sense that, for every$g \in \mathcal { S }$acting on$\mathbf { R } ^ { d - 1 }$via an isometry $T _ { g } \colon x \mapsto A _ { g } x + b _ { g }$, one has the identity$G ( t , x ) = G ( t , A _ { g } x )$. We then have the following result:

Lemma 7.7 Let G and$\mathcal { S }$be as above. Then, there existfunctions K and R such that the identity

$$
(G * u) (z) = (K * u) (z) + (R * u) (z),\tag{7.15}
$$

holds for every symmetric function u supported in$\mathbf { R } _ { + } \times \mathbf { R } ^ { d - 1 }$and every $z \in ( - \infty , 1 ] \times \mathbf { R } ^ { d - 1 }$

Furthermore, K is non-anticipative and symmetric, and satisfies Assumption 5.1 with$\beta = 2 q$, as well as Assumption 5.4for some arbitrary (butfixed) value r. Thefunction R is smooth, symmetric, non-anticipative, and compactly supported.

Proof It follows immediately from Lemmas 5.5 and 5.24 that one can write

$$
G = K + \bar {R},
$$

where K has all the required properties, and$\bar { R }$is smooth, non-anticipative, and symmetric. Since$u$is supported on positive times and we only consider (7.15) for times$t \leq 1$, we can replace$\bar { R }$by any function$\tilde { R }$which is supported in$\{ ( t , x ) : t \leq 2 \}$say, and such that$\tilde { R } ( t , x ) = \bar { R } ( t , x )$for$t \leq 1$

It remains to replace$\tilde { R }$by a kernel R which is compactly supported. It is well-known [11,12] that any crystallographic group$\mathcal { S }$can be written as the skew-product of a (finite) crystallographic point group$\mathcal { G }$with a lattice$\Gamma$of translations. We then fix a function$\varphi \colon \mathbf { R } ^ { \bar { d - 1 } }  [ 0 , \bar { 1 } ]$which is compactly supported in a ball of radius$C _ { \varphi }$around the origin and such that$\textstyle \sum _ { k \in { \Lambda } } \varphi ( x +$ $k ) = 1$for every x. Since elements in$\mathcal { G }$leave the lattice  invariant, the same property holds true for the maps$x \mapsto \varphi ( A x )$for every$A \in { \mathcal { G } }$

It then suffices to set

$$
R (t, x) = \frac {1}{| \mathcal {G} |} \sum_ {A \in \mathcal {G}} \sum_ {k \in \Lambda} \tilde {R} (t, x + k) \varphi (A x).
$$

The fact that R is compactly supported follows from the same property for$\varphi$. Furthermore, the above sum converges to a smooth function by Lemma 7.4. Also, using the fact that u is invariant under translations by elements in  by assumption, it is straightforward to verify that${ \tilde { R } } * u = { \overline { { R } } } * u$as required. Finally, for any$A _ { 0 } \in \mathcal { G }$, one has

$$
\begin{array}{l} R (t, A _ {0} x) = \frac {1}{| \mathcal {G} |} \sum_ {A \in \mathcal {G}} \sum_ {k \in \Lambda} \tilde {R} (t, A _ {0} x + k) \varphi (A A _ {0} x) \\ \qquad = \frac {1}{| \mathcal {G} |} \sum_ {A \in \mathcal {G}} \sum_ {k \in \Lambda} \tilde {R} (t, A _ {0} (x + k)) \varphi (A x) \\ \qquad = \frac {1}{| \mathcal {G} |} \sum_ {A \in \mathcal {G}} \sum_ {k \in \Lambda} \tilde {R} (t, x + k) \varphi (A x) = R (t, x), \end{array}
$$

so that R is indeed symmetric for$\mathcal { S }$. Here, we first exploited the fact that elements of$\mathcal { G }$leave the lattice  invariant, and then used the symmetry of$\tilde { R }$. □

## 7.3 A general fixed point map

We have now collected all the ingredients necessary for the proof of the following result, which can be viewed as one of the main abstract theorems of this article. The setting for our result is the following. As before, we assume that we have a crystallographic group$\mathcal { S }$acting on$\mathbf { R } ^ { d - 1 }$. We also write $\mathbf { R } ^ { d } = \mathbf { R } \times \mathbf { R } ^ { d - 1 }$, endow$\bar { \mathbf { R } ^ { d } }$with a scaling s, and extend the action of$\mathcal { S }$ to$\mathbf { R } ^ { d }$in the obvious way. Together with this data, we assume that we are given a non-anticipative kernel$G \colon { \mathbf { R } } ^ { d } \backslash 0  { \mathbf { R } }$that is smooth away from the origin, preserves the symmetry$\mathcal { S }$, and is scale-invariant with exponent$\beta - | \mathfrak { s } |$for some fixed$\beta > 0$

Using Lemma 7.7, we then construct a singular kernel K and a smooth compactly supported function R on$\mathbf { R } ^ { d }$such that (7.15) holds for symmetric functions u that are supported on positive times. Here, the kernel K is assumed to be again non-anticipative and symmetric, and it is chosen in such a way that it annihilates all polynomials of some arbitrary (but fixed) degree$r > 0$. We then assume that we are given a regularity structure$\mathcal { T }$containing$\mathcal { T } _ { \mathfrak { s } , d }$such that$\mathcal { S }$acts on it, and which is endowed with an abstract integration map I of order$2 q \in \mathbf { N }$. (The domain of I will be specified later.) We also assume that we have abstract differentiation maps$\mathcal { D } _ { i }$which are covariant with respect to the symmetry$\mathcal { S }$as in Remark 5.30. We also denote by$\mathcal { M } _ { \mathcal { T } } ^ { r }$the set of all models for$\mathcal { T }$which realise K on$T _ { r } ^ { - }$. As before, we denote by$\kappa _ { \gamma }$the concrete integration map against K acting on$\mathcal { D } ^ { \gamma }$and constructed in Sect. 5, and by$R _ { \gamma }$the integration map against R constructed in (7.7).

Finally, we denote by$P = \{ ( t , x ) \in \mathbf { R } \times \mathbf { R } ^ { d - 1 } : t = 0 \}$the “time$0 ^ { \circ }$ hyperplane and we consider the spaces$\mathcal { D } _ { P } ^ { \gamma , \eta }$as in Sect. 6. Given$\gamma \geq \bar { \Gamma } > 0$ a map$F \colon \mathbf { R } ^ { d } \times T _ { \gamma }  T _ { \bar { \Gamma } }$, and a map$f \colon \mathbf { R } ^ { d }  T _ { \gamma }$, we denote by$F ( f )$the map given by

$$
\big (F (f) \big) (z) \stackrel {\text { def }} {=} F (z, f (z)).\tag{7.16}
$$

If it so happens that, via (7.16), F maps$\mathcal { D } _ { P } ^ { \gamma , \eta }$into$\mathcal { D } _ { P } ^ { \bar { \Gamma } , \bar { \eta } }$for some$\eta , { \bar { \eta } } \in \mathbf { R }$ we say that F is locally Lipschitz if, for every compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$and every $R > 0$, there exists a constant$C > 0$such that the bound

$$
\| F (f) - F (g) \| _ {\bar {\Gamma}, \bar {\eta}; \mathfrak {K}} \leq C \| f - g \| _ {\gamma , \eta ; \mathfrak {K}},
$$

holds for every$f , g \in \mathcal { D } _ { P } ^ { \gamma , \eta }$with$f \| _ { \gamma , \eta ; \mathbb { R } } + \| g \| _ { \gamma , \eta ; \mathbb { R } } \leq R$, as well as for all models Z with$\| Z \| _ { \gamma ; \mathscr { R } } \leq R$. We also impose that the similar bound

$$
\llbracket F (f) - F (g) \rrbracket_ {\bar {\Gamma}, \bar {\eta}; \mathfrak {K}} \leq C \llbracket f - g \rrbracket_ {\gamma , \eta ; \mathfrak {K}},\tag{7.17}
$$

holds.

We say that it is strongly locally Lipschitz if furthermore

$$
\| F (f); F (g) \| _ {\bar {\Gamma}, \bar {\eta}; \mathfrak {K}} \leq C \big (\| f; g \| _ {\gamma , \eta ; \mathfrak {K}} + \| Z - \bar {z} \| _ {\gamma ; \bar {\mathfrak {K}}} \big),
$$

for any two models$Z , { \bar { z } }$with$\| Z \| _ { \gamma ; \bar { \mathfrak { x } } } + \| \bar { z } \| _ { \gamma ; \bar { \mathfrak { x } } } \le R$, where this time$f \in$ $\mathcal { D } _ { P } ^ { \gamma , \eta } ( Z ) , g \in \mathcal { D } _ { P } ^ { \gamma , \eta } ( \bar { z } )$, and$\bar { \mathbf { x } }$denotes the 1-fattening of${ \mathcal { \kappa } } .$. Finally, given an open interval$I \subset \mathbf { R }$, we use the terminology

$$
\text {``u = \mathcal {K} _{\gamma} v\quad on\quad I''}
$$

to mean that the identity$u ( t , x ) = \bigl ( \mathcal { K } _ { \gamma } v \bigr ) ( t , x )$holds for every$t \in I$and $x \in \mathbf { R } ^ { d - 1 }$, and that for those values of$( t , x )$the quantity$\left( \mathcal { K } _ { \gamma } v \right) ( t , x )$only depends on the values$v ( s , y )$for$s \in I$and$y \in \mathbf { R } ^ { d - 1 }$

With all of this terminology in place, we then have the following general result.

Theorem 7.8 Let V and$\bar { V }$be two sectors of a regularity structure$\mathcal { T }$with respective regularities$\boldsymbol { \zeta } , \bar { \boldsymbol { \zeta } } \in \mathbf { R }$with$\zeta \leq \bar { \zeta } + 2 q$. In the situation described above, for some$\gamma \geq \bar { \Gamma } > 0$and some$\eta \in \mathbf { R }$, let$F \colon \mathbf { R } ^ { d } \times V _ { \gamma }  \bar { V } _ { \bar { \Gamma } }$be a smooth function such that,$i f f \in \mathcal { D } _ { P } ^ { \gamma , \eta }$is symmetric with respect to$\mathcal { S }$, then $F ( f )$, defined by (7.16), belongs to$\mathcal { D } _ { P } ^ { \bar { \Gamma } , \bar { \eta } }$and is also symmetric with respect $t o \mathcal { S } .$. Assumefurthermore that we are given an abstract integration map$\mathcal { T }$as above such that$\mathcal { Q } _ { \gamma } ^ { - } \mathcal { T } \bar { V } _ { \bar { \Gamma } } \subset V _ { \gamma }$

$J f \eta < ( \bar { \eta } \wedge \bar { \zeta } ) + 2 q , \gamma < \bar { \Gamma } + 2 q , ( \bar { \eta } \wedge \bar { \zeta } ) > - 2 q$, and$F$is locally Lipschitz then,for every$v \in \bar { \mathcal { D } } _ { P } ^ { \gamma , \eta }$which is symmetric with respect to$\mathcal { S } _ { : }$, andfor every symmetric model$Z \doteq ( \Pi , \Gamma )$for the regularity structure$\mathcal { T }$such that$\mathcal { T }$is adapted to the kernel K, there exists a time$T > 0$such that the equation

$$
u = (\mathcal {K} _ {\bar {\Gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} ^ {+} F (u) + v,\tag{7.18}
$$

admits a unique solution$u \in \mathcal { D } _ { P } ^ { \gamma , \eta } o n \left( 0 , T \right)$. The solution map$S _ { T } \colon ( v , Z ) \mapsto$ u isjointly continuous in a neighbourhood around$( v , Z )$in the sense that,for every fixed v and$Z$as above, as well as any$\varepsilon > 0 _ { ; }$, there exists$\delta > 0$such that, denoting by u the solution to thefixed point map with data$\bar { V }$and$\bar { z } ,$, one has the bound

$$
\| u; \bar {u} \| _ {\gamma , \eta ; T} \leq \varepsilon ,
$$

provided that$\| Z ; \bar { z } \| _ { \gamma ; O } + \| v ; \bar { V } \| _ { \gamma , \eta ; T } \leq \delta$

Iffurthermore F is strongly locally Lipschitz then the map$( v , Z ) \mapsto u$is jointly Lipschitz continuous in a neighbourhood around$( v , Z )$in the sense that$\delta$can locally be chosen proportionally to ε in the bound above.

Proof We first consider the case of a fixed model$Z = ( \Pi , \Gamma )$, so that the space $\mathcal { D } _ { P } ^ { \gamma , \dot { \eta } }$(defined with respect to the given multiplicative map ) is a Banach space. In this case, denote by$\mathcal { M } _ { F } ^ { Z } ( u )$the right hand side of (7.18). Note that, even though$\mathcal { M } _ { F } ^ { Z }$appears not to depend on$Z$at first sight, it does so through the definition of$\kappa _ { \bar { \Gamma } }$

It follows from Theorem 7.1 and Lemma 7.3, as well as our assumptions on the exponents$\gamma , \bar { \Gamma } , \eta$and$\bar { \eta }$that there exists$\kappa > 0$such that one has the bound

$$
\| \mathcal {M} _ {F} ^ {Z} (u) - \mathcal {M} _ {F} ^ {Z} (\bar {u}) \| _ {\gamma , \eta ; T} \lesssim T ^ {\kappa} \| F (u) - F (\bar {u}) \| _ {\bar {\Gamma}, \bar {\eta}; T}.
$$

It follows from the local Lipschitz continuity of$F$that, for every$R > 0$, there exists a constant$C > 0$such that

$$
\| \mathcal {M} _ {F} ^ {Z} (u) - \mathcal {M} _ {F} ^ {Z} (\bar {u}) \| _ {\gamma , \eta ; T} \leq C T ^ {\kappa} \| u - \bar {u} \| _ {\gamma , \eta ; T},
$$

uniformly over T (0, 1 and over all u and$\bar { u }$such that$\begin{array} { r } { \| u \| _ { \gamma , \eta ; T } + \| \bar { u } \| _ { \gamma , \eta ; T } \leq } \end{array}$ R. Similarly, for every$R > 0$, there exists a constant$C > 0$such that one has

the bound

$$
\| \mathcal {M} _ {F} ^ {Z} (u) \| _ {\gamma , \eta ; T} \leq C T ^ {\kappa} + \| v \| _ {\gamma , \eta ; T}.
$$

As a consequence, as soon as$\| v \| _ { \gamma , \eta ; T }$is finite and provided that$T$is small enough$\mathcal { M } _ { F } ^ { Z }$maps the ball of radius$\lvert \boldsymbol { v } \rvert \rvert _ { \gamma , \eta ; T } + 1$in$\mathcal { D } _ { P } ^ { \gamma , \eta }$into itself and is a contraction there, so that it admits a unique fixed point. The fact that this is also the unique global fixed point for$\mathcal { M } _ { F } ^ { \mathrm { ~ Z ~ } }$follows from a simple continuity argument similar to the one given in the proof of Theorem 4.8 in [59].

For a fixed model$Z ,$, the local Lipschitz continuity of the map$v \mapsto u$for sufficiently small$T$is immediate. Regarding the dependency on the model$Z$, we first consider the simpler case where$F$is assumed to be strongly Lipschitz continuous. In this case, the same argument as above yields the bound

$$
\| \mathcal {M} _ {F} ^ {Z} (u); \mathcal {M} _ {F} ^ {\bar {z}} (\bar {u}) \| _ {\gamma , \eta ; T} \leq C T ^ {\kappa} \big (\| u; \bar {u} \| _ {\gamma , \eta ; T} + \| Z; \bar {z} \| _ {\gamma ; O} \big),
$$

so that the claim follows at once.

It remains to show that the solution is also locally uniformly continuous as a function of the model$Z$in situations where$F$is locally Lipschitz continuous, but not in the strong sense. Given a second model$\bar { z } = ( \bar { \Pi } , \bar { \Gamma } )$, we denote by$\bar { u }$ the corresponding solution to (7.18). We assume that$\bar { z }$is sufficiently close to Z so that both$\mathcal { M } _ { F } ^ { Z }$and$\mathcal { M } _ { F } ^ { \bar { z } }$are strict contractions on the same ball. We also use the shorthand notations$u ^ { ( n ) } = ( \mathcal { M } _ { F } ^ { Z } ) ^ { n } ( 0 )$and$\bar { u } ^ { ( n ) } = ( \mathcal { M } _ { F } ^ { \bar { z } } ) ^ { n } ( 0 )$. Using the strict contraction property of the two fixed point maps, we have the bound

$$
\begin{array}{c} \| u - \bar {u} \| _ {\gamma , \eta ; T} \lesssim \| u - u ^ {(n)} \| _ {\gamma , \eta ; T} + \| u ^ {(n)} - \bar {u} ^ {(n)} \| _ {\gamma , \eta ; T} + \| \bar {u} ^ {(n)} - \bar {u} \| _ {\gamma , \eta ; T} \\ \lesssim \varrho^ {n} + [   ] u ^ {(n)} - \bar {u} ^ {(n)}   ] _ {\gamma , \eta ; T}, \end{array}
$$

for some constant$\varrho ~ < ~ 1 . ~ \mathrm { A s }$a consequence of Lemmas 6.5, 6.6, (7.17), Proposition 6.16, and using the fact that there is a little bit of “wiggle room” between$\gamma$and$\bar { \Gamma } + 2 q$, we obtain the existence of a constant$\kappa > 0$such that one has the bound

$$
\begin{array}{r l} \llbracket u ^ {(n)} - \bar {u} ^ {(n)} \rrbracket_ {\gamma , \eta ; T} & \lesssim \| \mathcal {M} _ {F} ^ {Z} (u ^ {(n - 1)}); \mathcal {M} _ {F} ^ {\bar {z}} (\bar {u} ^ {(n - 1)}) \| _ {\gamma , \eta ; T} \\ & \lesssim \| F (u ^ {(n - 1)}); F (\bar {u} ^ {(n - 1)}) \| _ {\bar {\Gamma} - \kappa , \bar {\eta}; T} + \| Z; \bar {z} \| _ {\gamma ; O} \\ & \lesssim \llbracket F (u ^ {(n - 1)}) - F (\bar {u} ^ {(n - 1)}) \rrbracket_ {\bar {\Gamma}, \bar {\eta}; T} ^ {\kappa} + \| Z; \bar {z} \| _ {\gamma ; O} \\ & \lesssim \llbracket u ^ {(n - 1)} - \bar {u} ^ {(n - 1)} \rrbracket_ {\gamma , \eta ; T} ^ {\kappa} + \| Z; \bar {z} \| _ {\gamma ; O}, \end{array}
$$

uniformly in n. By making$T$sufficiently small, one can furthermore ensure that the proportionality constant that in principle appears in this bound is bounded by 1. Since$u ^ { 0 } = \bar { u } ^ { 0 }$, we can iterate this bound n times to obtain

$$
\| u ^ {(n)} - \bar {u} ^ {(n)} \| _ {\gamma , \eta ; T} \lesssim \| Z; \bar {z} \| _ {\gamma ; O} ^ {\kappa^ {n}},
$$

with a proportionality constant that is bounded uniformly in n. Setting$\varepsilon =$ $\| Z ; \bar { z } \| _ { \gamma ; O }$, a simple calculation shows that the term$\varrho ^ { n }$and the term$\mathcal { E } ^ { \bar { \kappa } ^ { n } }$are of (roughly) the same order when$n \sim \log \log \varepsilon ^ { - 1 }$, which eventually yields a bound of the type

$$
\| u; \bar {u} \| _ {\gamma , \eta ; T} \lesssim \left| \log \| Z; \bar {z} \| _ {\gamma ; O} \right| ^ {- \nu},
$$

for some exponent$\nu > 0$, uniformly in a small neighbourhood of any initial condition and any model Z. While this bound is of course suboptimal in many situations, it is sufficient to yield the joint continuity of the solution map for a very large class of nonlinearities.□

Remark 7.9 The condition$( \bar { \eta } \wedge \bar { \zeta } ) > - 2 q$is required in order to be able to apply Proposition 6.16. Recall however that the assumptions of that theorem can on occasion be slightly relaxed, see Remark 6.17. The relevant situation in our context is when$F$can be rewritten as$F ( z , u ) = F _ { 0 } ( z , u ) + F _ { 1 } ( z )$, where $F _ { 0 }$satisfies the assumption of our theorem, but$F _ { 1 }$does not. If we then make sense of$( \mathcal { K } _ { \bar { \Gamma } } + R _ { \gamma } \mathcal { R } ) R ^ { + } F _ { 1 }$“by hand” as an element of$\mathcal { D } _ { P } ^ { \gamma , \eta }$and impose sufficient restrictions on our model$Z$such that this element is continuous as a function of$Z$, then we can absorb it into v so that all of our conclusions still hold.

Remark 7.10 In many situations, the map F has the property that

$$
\mathcal {Q} _ {\zeta + 2 q} ^ {-} \tau = \mathcal {Q} _ {\zeta + 2 q} ^ {-} \bar {\tau} \Rightarrow \mathcal {Q} _ {\zeta + 2 q} ^ {-} F (z, \tau) = \mathcal {Q} _ {\zeta + 2 q} ^ {-} F (z, \bar {\tau}).\tag{7.19}
$$

Denote as before by$\bar { T } \subset T$the sector spanned by abstract polynomials. Then, provided that (7.19) holds, for every$z \in \mathbf { R } ^ { d }$and every$v \in \bar { T }$, the equation

$$
\tau = \mathcal {Q} _ {\gamma} ^ {-} \big (\mathcal {I} F (z, \tau) + v \big),
$$

admits a unique solution$\mathfrak { F } ( z , v )$in V. Indeed, it follows from the properties of the abstract integration map$\mathcal { T }$, combined with (7.19), that there exists$n >$ 0 such that the map$F _ { z , v } : \tau \mapsto \mathcal { Q } _ { \gamma } ^ { - } ( \mathcal { T } F ( z , \tau ) + v )$has the property that $F _ { z , v } ^ { n + 1 } ( \tau ) = F _ { z , v } ^ { n } ( \tau )$

It then follows from the definitions of the operations appearing in (7.21) that, if we denote by$\bar { \mathcal Q } u$the component of u in$\bar { T }$, one has the identity

$$
u (t, x) = \mathfrak {F} \big ((t, x), \bar {\mathcal {Q}} u (t, x) \big), \qquad t \in (0, T ],\tag{7.20}
$$

for the solution to our fixed point equation (7.21). In other words, ifwe interpret the$\bar { \mathcal Q } u ( t , x )$as a “renormalised Taylor expansion” for the solution u, then any of the components$\mathcal { Q } _ { \zeta } u ( t , x )$is given by some explicit nonlinear function of the renormalised Taylor expansion up to some order depending on$\zeta$. This fact will be used to great effect in Sect. 9.3 below.

Before we proceed, we show that, in the situations of interest for us, the local solution maps built in Theorem 7.8 are consistent. In other words, we would like to be able to construct a “maximal solution” by piecing together local solutions. In the context considered here, it is a priori not obvious that this is possible. In order to even formulate what we mean by such a statement, we introduce the set$P _ { t } = \{ ( s , y ) ~ : ~ s = t \}$and write$R _ { t } ^ { + }$for the indicator function of the set$\{ ( s , y ) : s > t \}$, which we interpret as before as a bounded operator from$\mathcal { D } _ { P _ { t } } ^ { \gamma , \eta }$into itself for any$\gamma > 0$and$\eta \in \mathbf { R }$

From now on, we assume that$G$is the parabolic Green’s function of a constant coefficient parabolic differential operator$\mathcal { L }$on$\mathbf { R } ^ { d - 1 }$. In this way, for any distribution$u _ { 0 }$on$\mathbf { R } ^ { d - 1 }$, the function$v = G u _ { 0 }$defined as in Lemma 7.5 is a classical solution to the equation$\partial _ { t } \boldsymbol { v } = \mathcal { L } \boldsymbol { v }$for$t > 0$. We then consider the class of equations of the type (7.18) with$\boldsymbol { v } = G \boldsymbol { u } _ { 0 }$, for some function (or possibly distribution)$u _ { 0 }$on$\mathbf { R } ^ { d - 1 }$. We furthermore assume that the sector V is function-like. Recall Proposition 3.28, which implies that any modelled distribution u with values in V is such that$\mathcal { R } u$is a continuous function belonging to$\mathcal { C } _ { \mathfrak { s } } ^ { \beta }$for some$\beta > 0$. In particular,$( { \mathcal { R } } u ) ( t , \cdot )$is then perfectly well-defined as a function on$\mathbf { R } ^ { d - 1 }$belonging to$\mathcal { C } _ { \bar { s } } ^ { \beta }$. We then have the following result:

Proposition 7.11 In the setting ofTheorem 7.8, assume that$\zeta = 0$and$- \mathfrak { s } _ { 1 } <$ $\eta < \beta$with η N and β as above. Let$u _ { 0 } \in \mathcal { C } _ { \bar { s } } ^ { \eta } ( \mathbf { R } ^ { d - 1 } )$be symmetric and let $T > 0$be sufficiently small so that the equation

$$
u = (\mathcal {K} _ {\bar {\Gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} ^ {+} F (u) + G u _ {0},\tag{7.21}
$$

admits a unique solution$u \in \mathcal { D } _ { P } ^ { \gamma , \eta }$on$( 0 , T )$. Letfurthermore$s \in ( 0 , T )$and $\bar { T } > T$be such that

$$
\bar {u} = (\mathcal {K} _ {\bar {\Gamma}} + R _ {\gamma} \mathcal {R}) \pmb {R} _ {s} ^ {+} F (\bar {u}) + G u _ {s},
$$

where$u _ { s } \overset { \mathrm { d e f } } { = } ( \mathcal { R } u ) ( s , \cdot )$, admits a unique solution$\bar { u } \in \mathcal { D } _ { P _ { s } } ^ { \gamma , \eta }$on$( s , { \bar { T } } )$

Then, one necessarily has$\bar { u } ( t , x ) = u ( t , x )$for every$x \in \mathbf { R } ^ { d - 1 }$and every $t \in ( s , T )$. Furthermore, the element$\hat { u } \in \mathcal { D } _ { P } ^ { \gamma , \ d }$defined by$\hat { u } ( t , x ) = u ( t , x )$ $f o r t \le s$and$\hat { u } ( t , x ) = \bar { u } ( t , x )$for$t > s$satisfies (7.21) on$( 0 , \bar { T } )$

Proof Setting$v = R _ { s } ^ { + } u \in \mathcal { D } _ { P _ { s } } ^ { \gamma , \eta }$, it follows from the definitions of$\kappa _ { \bar { \Gamma } }$and$R _ { \gamma }$ that one has for$t \in ( s , T ]$the identity

$$
\begin{array}{l} \langle \mathbf {1}, v (t, x) \rangle = \int_ {0} ^ {t} \int_ {\mathbf {R} ^ {d - 1}} G (t - r, x - y) \big (\mathcal {R} F (u) \big) (r, y) d y d r \\ \qquad + \int_ {\mathbf {R} ^ {d - 1}} G (t, x - y) u _ {0} (y) d y \\ \qquad = \int_ {s} ^ {t} \int_ {\mathbf {R} ^ {d - 1}} G (t - r, x - y) \big (\mathcal {R} F (v) \big) (r, y) d y d r \\ \qquad + \int_ {\mathbf {R} ^ {d - 1}} G (t - s, x - y) u _ {s} (y) d y. \end{array}
$$

Here, the fact that there appears no additional term is due to the fact that $\bar { \zeta } > - 2 q$, so that the term$\langle \mathbf { 1 } , { \mathcal { T } } ( t , x ) ( F ( u ) ( t , x ) ) \langle$cancels exactly with the corresponding term appearing in the definition of$\mathcal { N } _ { \bar { \Gamma } }$. This quantity on the other hand is precisely equal to

$$
\left\langle \mathbf {1}, \left((\mathcal {K} _ {\bar {\Gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} _ {s} ^ {+} F (v) + G u _ {s}\right) (t, x) \right\rangle .
$$

Setting

$$
w = (\mathcal {K} _ {\bar {\Gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} _ {s} ^ {+} F (v) + G u _ {s},
$$

we deduce from the definitions of the various operators appearing above that, for$\boldsymbol { \ell } \not \in \mathbf { N }$, one has$\mathcal { Q } _ { \ell } w ( z ) = \mathcal { Q } _ { \ell } \mathcal { T } F ( z , v ( z ) )$). However, we also know that v satisfies$\mathcal { Q } _ { \ell } \boldsymbol { v } ( z ) = \mathcal { Q } _ { \ell } \mathcal { T } F ( z , \boldsymbol { v } ( z ) )$. We can therefore apply Proposition 3.29, which yields the identity$w = v$, from which it immediately follows that$v = { \bar { u } }$ on$( 0 , T )$

The argument regarding$\hat { u }$is virtually identical, so we do not reproduce it here.□

This shows that we can patch together local solutions in exactly the same way as for “classical” solutions to nonlinear evolution equations. Furthermore, it shows that the only way in which local solutions can fail to be global is by an explosion of the$\dot { \mathcal { C } } _ { \bar { \mathfrak { s } } } ^ { \eta } \mathrm { - n o r m }$of the quantity$\bigl ( \mathcal { R } u \bigr ) ( t , \cdot )$. Furthermore, since the reconstruction operator$\mathcal { R }$is continuous into$\mathcal { C } _ { \bar { \mathfrak { s } } } ^ { \eta }$, this norm is continuous as a function of time, so that for any cut-off value$L > 0$, there exists a (possibly infinite) first time t at which$\| u ( t , \cdot ) \| _ { \eta } = L$

Given a symmetric model$Z = ( \Pi , \Gamma )$for$\mathcal { T }$, a symmetric initial condition $u _ { 0 } \in \mathcal { C } _ { \bar { \mathfrak { s } } } ^ { \eta }$, and some (typically large) cut-off value$L \ > \ 0$, we denote by $u = \mathcal { S } ^ { \bar { L } } ( u _ { 0 } , Z ) \in \mathcal { D } _ { P } ^ { \gamma , \eta }$and$T = T ^ { L } ( u _ { 0 } , Z ) \in \mathbb { R } _ { + } \cup \{ + \infty \}$the (unique) modelled distribution and time such that

$$
u = (\mathcal {K} _ {\bar {\Gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} ^ {+} F (u) + G u _ {0},
$$

on$[ 0 , T ]$, such that$\| ( \mathcal { R } u ) ( t , \cdot ) \| _ { \eta } \ < \ \ L$for$\smash { t } \quad < \quad T$, and such that $\| ( { \mathcal { R } } u ) ( t , \cdot ) \| _ { \eta } \geq L$for$t \geq T$. The following corollary is now straightforward:

Corollary 7.12 Let$L > 0$be fixed. In the setting of Proposition 7.11, let$S ^ { L }$ and$T ^ { L }$be defined as above and set$O = [ - 1 , 2 ] \times \mathbf { R } ^ { d - 1 }$. Then,for every$\varepsilon > 0$ and$C > 0$there exists$\delta > 0$such that, setting$T = 1 \land T ^ { L } ( u _ { 0 } , Z ) \land T ^ { L } ( \bar { u } _ { 0 } , \bar { z } )$ one has the bound

$$
\| \mathcal {S} ^ {L} (u _ {0}, Z) - \mathcal {S} ^ {L} (\bar {u} _ {0}, \bar {z}) \| _ {\gamma , \eta ; T} \leq \varepsilon ,
$$

for all$u _ { 0 } , \ \bar { u } _ { 0 } , \ Z , \ \bar { z }$such that$\| Z \| _ { \gamma ; O } \ \leq \ C , \ \| \bar { z } \| _ { \gamma ; O } \ \leq \ C , \ \| u _ { 0 } \| _ { \eta } \ \leq \ L / 2 ,$ $\lVert \bar { u } _ { 0 } \rVert _ { \eta } \leq L / 2 , \lVert u _ { 0 } - \bar { u } _ { 0 } \rVert _ { \eta } \leq \delta _ { \mathrm { { \iota } } }$, and$\| Z ; { \bar { z } } \| _ { \gamma ; O } \leq \delta .$

Proof The argument is straightforward and works in exactly the same way as analogous statements in the classical theory of semilinear PDEs. The main ingredient is the fact that for every$t > 0$, one can obtain an a priori bound on the number of iterations required to reach the time$t \wedge T ^ { L } ( u _ { 0 } , Z )$□

## 8 Regularity structures for semilinear (S)PDEs

In this section, we show how to apply the theory developed in this article to construct an abstract solution map to a very large class of semilinear PDEs driven by rough input data. Given Theorem 7.8, the only task that remains is to build a sufficiently large regularity structure allowing to formulate the equation.

First, we give a relatively simple heuristic that allows one to very quickly decide whether a given problem is at all amenable to the analysis presented in this article. For the sake of conciseness, we will assume that the problem of interest can be rewritten as a fixed point problem of the type

$$
u = K * F (u, \nabla u, \xi) + \tilde {u} _ {0},\tag{8.1}
$$

where K is a singular integral operator that is β-regularising on$\mathbf { R } ^ { d }$with respect to some fixed scaling s,$F$is a smooth function,$\xi$denotes the rough input data, and$\tilde { u } _ { 0 }$describes some initial condition (or possibly boundary data). In general, one might imagine that$F$also depends on derivatives of higher order (provided that$\beta$is sufficiently large) and / or that$F$itself involves some singular integral operators. We furthermore assume that F is affine in$\xi$. (Accommodating the general case where$F$is polynomial in$\xi$would also be possible with minor modifications, but we stick to the affine case for ease of presentation.)

It is also straightforward to deal with the situation when$F$is non-homogeneous in the sense that it depends on the (space-time) location explicitly, as long as any such dependence is sufficiently smooth. For the sake of readability, we will refrain from presenting such extensions and we will focus on a situation which is just general enough to be able to describe all of the examples given in the introduction.

Remark 8.1 In all the examples we are considering, K is the Green’s function of some differential operator${ \mathcal { L } } .$. In order to obtain optimal results, it is usually advisable to fix the scaling s in such a way that all the dominant terms in$\mathcal { L }$ have the same homogeneity, when counting powers with the weights given by s.

Remark 8.2 We have seen in Sect. 7.1 that in general, one would really want to consider instead of (8.1) fixed point problems of the type

$$
u = \left((K + R) * \left(\boldsymbol {R} ^ {+} F (u, \nabla u, \xi)\right)\right) + \tilde {u} _ {0},\tag{8.2}
$$

where$\pmb { R } ^ { + }$denotes again the characteristic function of the set of positive times and R is a smooth non-anticipative kernel. However, if we are able to formulate (8.1), then it is always straightforward to also formulate (8.2) in our framework, so we concentrate on (8.1) for the moment in order not to clutter the presentation.

Denoting by$\alpha \ < \ 0$the regularity of$\xi$and considering our multi-level Schauder estimate, Theorem 5.12, we then expect the regularity of the solution $u$to be of order at most$\beta { + } \alpha$, the regularity of$\nabla \boldsymbol { u }$to of order at most$\beta + \alpha - 1$ etc. We then make the following assumption:

Assumption 8.3 (local subcriticality) In the formal expression of F, replace $\xi$by a dummy variable . For any$i \in \{ 1 , \ldots , d \}$, if$\beta + \alpha \ \leq \ { \mathfrak { s } } _ { i }$, then replacefurthermore any occurrence of∂ u by the dummy variable$P _ { i }$. Finally, $i f \beta + \alpha \leq 0$, replace any occurrence ofu by the dummy variable U.

We then make the following two assumptions. First, we assume that the resulting expression is polynomial in the dummy variables. Second, we associate to each such monomial a homogeneity by postulating that$\Xi$has homogeneity α, U has homogeneity$\beta + \alpha$, and$P _ { i }$has homogeneity$\beta + \alpha - \mathfrak { s } _ { i }$ (The homogeneity of a monomial then being the sum of the homogeneities of eachfactor.) With these notations, the assumption oflocal subcriticality is that terms containing  do not contain the dummy variables and that the remaining monomials each have homogeneity strictly greater than α.

Whenever a problem of the type (8.1) satisfies Assumption 8.3, we say that it is locally subcritical. The role of this assumption is to ensure that, using Theorems 4.7, 4.16, and 5.12, one can reformulate (8.1) as a fixed point map in$\mathcal { D } ^ { \gamma }$ for sufficiently high$\gamma$(actually any$\gamma > | \alpha |$would do) by replacing the convolution K with$\kappa _ { \gamma }$as in Theorem 5.12, replacing all products by the abstract product , and interpreting compositions with smooth functions as in Sect. 4.2.

For such a formulation to make sense, we need of course to build a sufficiently rich regularity structure. This could in principle be done by repeatedly applying Proposition 4.11 and Theorem 5.14, but we will actually make use of a more explicit construction given in this section, which will also have the advantage of coming automatically with a “renormalisation group” that allows to understand the kind of convergence results mentioned in Theorems 1.11 and 1.15. Our construction suggests the following “metatheorem”, which is essentially a combination of Theorems 7.8, 4.7, 4.16, and 8.24 below.

Metatheorem 8.4 Whenever (8.1) is locally subcritical, it is possible to build a regularity structure allowing to reformulate it as afixedpointproblem in$\mathcal { D } ^ { \gamma }$ for γ large enough. Furthermore, if the problem is parabolic on a bounded domain (say the torus), then the fixed point problem admits a unique local solution.

Before we proceed to building the family of regularity structures allowing to formulate these SPDEs, let us check that Assumption 8.3 is indeed verified for our examples$( \Phi ^ { 4 } )$, (PAM), and (KPZ). Note first that it is immediate from Proposition 3.20 and the equivalence of moments for Gaussian random variables that white noise on$\mathbf { R } ^ { d }$with scaling s almost surely belongs to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$for every$\alpha < - { \frac { | { \mathfrak { s } } | } { 2 } }$. (See also Lemma 10.2 below.) Furthermore, the heat kernel is 2-regularising, so that$\beta = 2$in all of the problems considered here.

In the case of$( \Phi ^ { 4 } )$in dimension$d ,$space-time is given by$\mathbf { R } ^ { d + 1 }$with scaling ${ \mathfrak { s } } = ( 2 , 1 , \dots , 1 )$, so that$| \mathfrak { s } | = d + 2$. This implies that$\xi$belongs to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$for every$\begin{array} { r } { \alpha < - \frac { d + 2 } { 2 } = - 1 - \frac { d } { 2 } } \end{array}$. In this case$\begin{array} { r } { \beta + \alpha \approx 1 - \frac { d } { 2 } } \end{array}$so that, following the procedure of Assumption 8.3, the monomials appearing are$U ^ { 3 }$and$\Xi$. The homogeneity of$U ^ { 3 }$is$\begin{array} { r } { 3 ( \beta + \alpha ) \approx 3 - \frac { 3 d } { 2 } } \end{array}$, which is greater than$- 1 - \frac { d } { 2 }$if and only if$d < 4$. This is consistent with the fact that 4 is the critical dimension for Euclidean$\Phi ^ { 4 }$quantum field theory [3]. Classical fixed point arguments using purely deterministic techniques on the other hand already fail for dimension 2, where the homogeneity of u becomes negative, which is a well-known fact [52]. In the particular case of$d = 2$however, provided that one defines the powers$( K * \xi ) ^ { k }$“by hand”, one can write$u = K * \xi + v$, and the equation for v is amenable to classical analysis, a fact that was exploited for example in [34,69]. In dimension 3, this breaks down, but our arguments show that one still expects to be able to reformulate$( \Phi ^ { 4 } )$as a fixed point problem in$\mathcal { D } ^ { \gamma }$ provided that$\gamma > \frac { 3 } { 2 }$. This will be done in Sect. 7.3 below.

For (PAM) in dimension d (and therefore space-time$\mathbf { R } ^ { d + 1 }$with the same scaling as above), spatial white noise belongs to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$for$\alpha < - \frac { d } { 2 }$. As a consequence, Assumption 8.3 does in this case boil down to the condition$2 + \alpha > 0$ which is again the case ifand only if$d < 4$. This is again not surprising. Indeed, dimension 4 is precisely such that, if one considers the classical parabolic Anderson model on the lattice${ \mathbf Z } ^ { 4 }$and simply rescales the solutions without changing the parameters of the model, one formally converges to solutions to the continuous model (PAM). On the other hand, as a consequence of Anderson localisation, one would expect that the rescaled solution converges to an object that is “trivial” in the sense that it could only be described either by the 0 distribution or by a Dirac distribution concentrated in a random location, which is something that falls outside of the scope of the theory presented in this article. In dimensions 2 and 3 however, one expects to be able to formulate and solve a fixed point problem in$\mathcal { D } ^ { \gamma }$for$\gamma > \frac { 3 } { 2 }$. This time, one also expects solutions to be global, since the equation is linear.

In the case of (KPZ), one can verify in a similar way that Assumption 8.3 holds. As before, if we consider an equation of this type in dimension$d ,$, we have$| \mathfrak { s } | = d + 2$, so that one expects the solution u to be of regularity just below$1 - { \frac { d } { 2 } }$. In this case, dimension 2 is already critical for three unrelated reasons. First, this is the dimension where u ceases to be function-valued, so that compositions with smooth functions ceases to make sense. Second, even if the functions$g _ { i }$were to be replaced by polynomials,$g _ { 4 }$would have to be constant in order to satisfy Assumption 8.3. Finally, the homogeneity of the term$| \nabla h | ^ { 2 } \mathrm { i } \mathrm { s } - d$. In dimension 2, this precisely matches the regularity$- 1 - \frac { d } { 2 }$ of the noise term.

We finally turn to the Navier–Stokes equations (SNS), which we can write in the form (8.1) with K given by the heat kernel, composed with Leray’s projection onto the space of divergence-free vector fields. The situation is slightly more subtle here, as the kernel is now matrix-valued, so that we really have$\bar { d ^ { 2 } }$(or rather$d ( d + 1 ) / 2$because of the symmetry) different convolution operators. Nevertheless, the situation is similar to before and each component of K is regularity improving with$\beta = 2$. The condition for local subcriticality given by Assumption 8.3 then states that one should have$( 1 - \textstyle { \frac { d } { 2 } } ) + ( - \textstyle { \frac { d } { 2 } } ) { \dot { > } }$ $- 1 - \frac { d } { 2 }$, which is satisfied if and only if$d < 4$

## 8.1 General algebraic structure

The general structure arising in the abstract solution theory for semilinear SPDEs of the form$( \Phi ^ { 4 } )$, (PAM), etc is very close to the structure already mentioned in Sect. 4.3. The difference however is that$T$only “almost” forms a Hopf algebra, as we will see presently.

In general, we want to build a regularity structure that is sufficiently rich to allow to formulate a fixed point map for solving our SPDEs. Such a regularity structure will depend on the dimension$d$of the underlying space(-time), the scaling s of the linear operator, the degree$\beta$of the linear operator (which is equal to the regularising index of the corresponding Green’s function), and the regularity$\alpha$of the driving noise$\xi$. It will also depend on finer details of the equation, such as whether the nonlinearity contains derivatives of$u ,$, arbitrary functions of$u .$, etc.

At the minimum, our regularity structure should contain polynomials, and it should come with an abstract integration map$\mathcal { T }$that represents integration against the Green’s function$K$of the linear operator${ \mathcal { L } } .$. (Or rather integration against a suitable cut-off version.) Furthermore, since we might want to represent derivatives of$u ,$, we can introduce the integration map$\mathcal { T } _ { k }$for a multiindex$k _ { : }$, which one should think as representing integration against$D ^ { k } K$ The “naïve” way of building$T$would be then to consider all possible formal expressions$\mathcal { F }$that can be obtained from the abstract symbols$\Xi$and$\{ X _ { i } \} _ { i = 1 } ^ { d }$ as well as the abstract integration maps$\mathcal { T } _ { k }$. More formally, we can define a set$\mathcal { F }$by postulating that$\{ 1 , \Xi , X _ { i } \} \subset \mathcal { F }$and, whenever$\tau , \bar { \tau } \in \mathcal { F }$, we have $\tau \bar { \tau } \in \mathcal { F }$and$\mathcal { T } _ { k } ( \tau ) \in \mathcal { F }$. (However, we do not include any expression containing a factor of$\mathcal { T } _ { k } ( X ^ { \ell } )$, thus reflecting Assumption 5.4 at the algebraic level.) Furthermore, we postulate that the product is commutative and associative by identifying the corresponding formal expressions (i.e.$X { \mathcal { T } } ( \Xi ) = { \mathcal { T } } ( \Xi ) X , { \mathrm { e t c } } )$, and that 1 is neutral for the product.

One can then associate to each$\tau \in \mathcal { F }$a weight$| \tau | _ { s }$which is obtained by setting$| \mathbf { 1 } | _ { \mathfrak { s } } = 0$,

$$
| \tau \bar {\tau} | _ {\mathfrak {s}} = | \tau | _ {\mathfrak {s}} + | \tau | _ {\mathfrak {s}},
$$

for any two formal expressions$\tau$and$\bar { \tau }$in$\mathcal { F }$, and such that

$$
| \Xi | _ {\mathfrak {s}} = \alpha , | X _ {i} | _ {\mathfrak {s}} = \mathfrak {s} _ {i}, | \mathcal {I} _ {k} (\tau) | _ {\mathfrak {s}} = | \tau | _ {\mathfrak {s}} + \beta - | k | _ {\mathfrak {s}}.
$$

Since these operations are sufficient to generate all of$\mathcal { F }$, this does indeed define$| \cdot | _ { s } .$

Example 8.5 These rules yield the weights

$$
| \Xi \mathcal {I} _ {\ell} (\Xi^ {2} X ^ {k}) | _ {\mathfrak {s}} = 3 \alpha + | k | _ {\mathfrak {s}} + \beta - | \ell | _ {\mathfrak {s}}, \quad | X ^ {k} \mathcal {I} (\Xi) ^ {2} | _ {\mathfrak {s}} = | k | _ {\mathfrak {s}} + 2 (\alpha + \beta),
$$

for any two multiindices$k$and$\ell .$

We could then define$T _ { \gamma }$simply as the set of all formal linear combinations of elements$\tau \in \mathcal { F }$with$| \tau | _ { \mathfrak { s } } = \gamma$. The problem with this procedure is that since$\alpha < 0$, we can build in this way expressions that have arbitrarily negative weight, so that the set of homogeneities$A \subset \mathbf { R }$would not be bounded from below anymore. (And it would possibly not even be locally finite.)

The ingredient that allows to circumvent this problem is the assumption of local subcriticality loosely formulated in Assumption 8.3. To make this more formal, assuming again for simplicity that the right hand side$F$of our problem (8.1) depends only on ξ, u, and some partial derivatives$\partial _ { i } u$, we can associate to F a (possibly infinite) collection${ \mathfrak { M } } _ { F }$of monomials in , U, and$P _ { i }$in the following way.

Definition 8.6 For any two integers m and n, and multiindex$k ,$, we have $\Xi ^ { m } U ^ { n } P ^ { k } \in \mathfrak { M } _ { F }$if$F$contains a term of the type$\xi ^ { \bar { m } } u ^ { \bar { n } } ( D u ) ^ { \bar { K } }$for${ \bar { m } } \geq m$ ${ \bar { n } } \geq n$, and$\bar { K } \ge k$. Here, we consider arbitrary smooth functions as polynomials of “infinite order”, i.e. we formally substitute$g ( u )$by$u ^ { \infty }$and similarly for functions involving derivatives of u. Note also that k and$\bar { K }$are multiindices since, in general,$P$is a d-dimensional vector.

Remark$8 . 7$Of course, M is not really well-defined. For example, in the case of$( \Phi ^ { 4 } )$, we have$F ( u , \xi ) = \xi - u ^ { 3 }$, so that

$$
\mathfrak {M} _ {F} = \{\Xi , U ^ {m}: m \leq 3 \}.
$$

However, we could of course have rewritten this as$F ( u , \xi ) = \xi + g ( u )$, hiding the fact that$g$actually happens to be a polynomial itself, and this would lead to adding all higher powers$\{ U ^ { n } \} _ { n > 3 }$to${ \mathfrak { M } } _ { F }$. In practice, it is usually obvious what the minimal choice of${ \mathfrak { M } } _ { F }$is.

Furthermore, especially in situations where the solution u is actually vectorvalued, it might be useful to encode into our regularity structure additional structural properties of the equation, like whether a given function can be written as a gradient. (See the series of works [62,63,72] for situations where this would be of importance.)

Remark 8.8 In the case of (PAM), we have

$$
\mathfrak {M} _ {F} = \{1, U, U \Xi , \Xi \},
$$

while in the more general case of (PAMg), we have

$$
\mathfrak {M} _ {F} = \left\{U ^ {n}, U ^ {n} \Xi , U ^ {n} P _ {i}, U ^ {n} P _ {i} P _ {j}: n \geq 0, i, j \in \{1, 2 \} \right\}.
$$

This and$( \Phi ^ { 4 } )$are the only examples that will be treated in full detail, but it is straightforward to see what${ \mathfrak { M } } _ { F }$would be for the remaining examples.

Remark 8.9 Throughout this whole section, we consider the case where the noise$\xi$driving our equation is real-valued and there is only one integral kernel required to describe the fixed point map. In general, one might also want to consider a finite family$\{ \Xi ^ { ( i ) } \}$of formal symbols describing the driving noises and a family$\{ \mathcal { T } ^ { ( i ) } \}$of symbols describing integration against various integral kernels. For example, in the case of (SNS), the integral kernel also involves the Leray projection and is therefore matrix-valued, while the driving noise is vector-valued. This is an immediate generalisation that merely requires some additional indices decorating the objects  and$\mathcal { T }$and all the results obtained in the present section trivially extend to this case. One could even accommodate the situation where different components of the noise have different degrees of regularity, but it would then become awkward to state an analogue to Assumption 8.3, although it is certainly possible. Since notations are already quite heavy in the current state of things, we refrain from increasing our level of generality.

Given a set of monomials${ \mathfrak { M } } _ { F }$as in Definition 8.6, we then build subsets $\{ \mathcal { U } _ { n } \} _ { n \ge 0 } , \{ \mathcal { P } _ { n } ^ { i } \} _ { n \ge 0 }$and$\{ \mathcal { W } _ { n } \} _ { n \ge 0 }$of$\mathcal { F }$by the following algorithm. We set$\mathcal { W } _ { 0 } =$ $\mathcal { U } _ { 0 } = \mathcal { P } _ { 0 } ^ { i } = \mathcal { V }$and, given subsets A,$B \subset { \mathcal { F } }$, we also write AB for the set of all products$\tau { \bar { \tau } }$with$\tau \in A$and$\bar { \tau } \in B$, and similarly for higher order monomials. (Note that this yields the convention$A ^ { 2 } = \{ \tau \bar { \tau } : \tau , \bar { \tau } \in A \} \neq \{ \tau ^ { 2 } : \tau \in A \} . )$

Then, we define the sets$\ w _ { \boldsymbol { w } _ { n } } , \boldsymbol { u } _ { n }$and$\mathcal { P } _ { n } ^ { i }$for$n > 0$recursively by

$$
\begin{array}{l} \mathcal {W} _ {n} = \mathcal {W} _ {n - 1} \cup \bigcup_ {\mathcal {Q} \in \mathfrak {M} _ {F}} \mathcal {Q} (\mathcal {U} _ {n - 1}, \mathcal {P} _ {n - 1}, \Xi), \\ \mathcal {U} _ {n} = \{X ^ {k} \} \cup \left\{\mathcal {I} (\tau): \tau \in \mathcal {W} _ {n} \right\}, \\ \mathcal {P} _ {n} ^ {i} = \{X ^ {k} \} \cup \left\{\mathcal {I} _ {i} (\tau): \tau \in \mathcal {W} _ {n} \right\}, \end{array}\tag{8.3}
$$

where in the set$\{ X ^ { k } \}$, k runs over all possible multiindices. In plain words, we take any of the monomials in${ \mathfrak { M } } _ { F }$and build$\mathcal { W } _ { n }$by formally substituting each occurrence of U by one of the expressions already obtained in$\mathcal { U } _ { n - 1 }$and each occurrence of$P _ { i }$by one of the expressions from$\mathcal { P } _ { n - 1 } ^ { i }$. We then apply the maps$\mathcal { T }$and$\mathcal { T } _ { i }$respectively to build$\mathcal { U } _ { n }$and$\mathcal { P } _ { n } ^ { i } .$, ensuring further that they include all monomials involving only the symbols$X _ { i }$. With these definitions at hand, we then set

$$
\mathcal {F} _ {F} \stackrel {{\text { def }}} {{=}} \bigcup_ {n \geq 0} \left(\mathcal {W} _ {n} \cup \mathcal {U} _ {n}\right).\tag{8.4}
$$

In situations where$F$depends on$u$(and not only on$D u$and$\xi$like in the case of the KPZ equation for example), we furthermore set

$$
\mathcal {U} _ {F} \stackrel {{\text { def }}} {{=}} \bigcup_ {n \geq 0} \mathcal {U} _ {n}.\tag{8.5}
$$

We similarly define$\begin{array} { r } { \mathcal P _ { F } ^ { i } = \bigcup _ { n > 0 } \mathcal P _ { n } ^ { i } } \end{array}$in the case when$F$depends on$\partial _ { i } u$ ' ≥The idea of this construction is that$\boldsymbol { \mathcal { U } } _ { F }$contains those elements of$\mathcal { F }$that are required to describe the solution u to the problem at hand,$\mathcal { P } _ { F } ^ { i }$contains the elements appearing in the description of$\partial _ { i } u$, and$\mathcal { F } _ { F }$contains the elements required to describe both the solution and the right hand side of (8.1), so that $\mathcal { F } _ { F }$is rich enough to set up the whole fixed point map.

The following result then shows that our assumption of local subcriticality, Assumption 8.3, is really the correct assumption for the theory developed in this article to apply:

Lemma 8.10 Let$\alpha < 0 .$. Then, the set$\{ \tau \in \mathcal { F } _ { F } : | \tau | _ { \mathfrak { s } } \le \gamma \}$isfinitefor every $\gamma \in \mathbf { R }$ifand only ifAssumption 8.3 holds.

Proof We only show that Assumption 8.3 is sufficient. Its necessity can be shown by similar arguments and is left to the reader. Set$\alpha ^ { ( n ) } = \mathrm { i n f } \{ | \tau | _ { 5 } \ :$ $\tau \in \mathcal { U } _ { n } \setminus \mathcal { U } _ { n - 1 } \big \}$and$\overline { { \alpha } } _ { i } ^ { ( n ) } = \operatorname* { i n f } \{ | \tau | _ { \mathfrak { s } } : \tau \in \mathcal { P } _ { n } ^ { ( i ) } \setminus \mathcal { P } _ { n - 1 } ^ { ( i ) } \}$. We claim that under Assumption 8.3 there exists$\zeta > 0$such that$\alpha ^ { ( n ) } > \alpha ^ { ( n - 1 ) } + \zeta$and similarly for$\alpha _ { i } ^ { ( n ) }$, which then proves the claim.

Note now that${ \mathcal { W } } _ { 1 } = \{ \Xi \}$, so that one has

$$
\alpha^ {(1)} = (\alpha + \beta) \wedge 0, \quad \alpha_ {i} ^ {(1)} = (\alpha + \beta - \mathfrak {s} _ {i}) \wedge 0.
$$

Furthermore, Assumption 8.3 implies that if$\Xi ^ { p } U ^ { q } P ^ { k } \in \mathfrak { M } _ { F } \setminus \{ \Xi \}$, then

$$
p \alpha + q (\alpha + \beta) + \sum_ {i} k _ {i} (\alpha + \beta - \mathfrak {s} _ {i}) > \alpha ,\tag{8.6}
$$

and$k _ { i }$is allowed to be non-zero only if$\beta > { \mathfrak { s } } _ { i }$. This immediately implies that one has$| \tau | _ { \mathfrak { s } } \geq \alpha$for every$\tau \in \mathcal { F } _ { F } , | \tau | _ { \mathfrak { s } } \geq ( \alpha + \beta ) \wedge 0$for every$\tau \in \mathcal { U } _ { F }$, and $| \tau | _ { \mathfrak { s } } \geq ( \alpha + \beta - \mathfrak { s } _ { i } ) \wedge 0$for every$\tau \in \mathcal P _ { F } ^ { i }$. (If this were to fail, then there would be a smallest index n at which it fails. But then, since it still holds at$n - 1$ condition (8.6) ensures that it also holds at n, thus creating a contradiction.)

Let now$\zeta > 0$be defined as

$$
\zeta = \inf _ {\Xi^ {p} U ^ {q} P ^ {k} \in \mathfrak {M} _ {F} \backslash \{\Xi \}} \left\{(p - 1) \alpha + q (\alpha + \beta) + \sum_ {i} k _ {i} (\alpha + \beta - \mathfrak {s} _ {i}) \right\}.
$$

Then we see that$\alpha ^ { ( 2 ) } \geq \alpha ^ { ( 1 ) } + \zeta$and similarly for$\alpha _ { i } ^ { ( 2 ) }$. Assume now by contradiction that there is a smallest value n such that either$\alpha ^ { ( n ) } < \alpha ^ { ( n - 1 ) } + \zeta$ or$\alpha _ { i } ^ { ( n ) } < \alpha _ { i } ^ { ( n - 1 ) } + \zeta$for some index i. Note first that one necessarily has $n \geq 3$and that, for any such n, one necessarily has$\alpha _ { i } ^ { ( n ) } = \alpha ^ { ( n ) } - \mathfrak { s } _ { i }$by (8.3) so that we can assume that one has$\alpha ^ { ( n ) } < \alpha ^ { ( n - 1 ) } + \dot { \zeta }$

Note now that there exists some element$\tau \in \mathcal { U } _ { n }$with$| \tau | _ { \mathfrak { s } } = \alpha ^ { ( n ) }$and that τ is necessarily of the form$\tau = \mathcal { T } ( \bar { \tau } )$) with$\bar { \tau } \in \mathcal { W } _ { n } \setminus \mathcal { W } _ { n - 1 }$. In other words, $\bar { \tau }$is a product of elements in$\mathcal { U } _ { n - 1 }$and$\mathcal { P } _ { n - 1 } ^ { i }$(and possibly a factor$\Xi )$with at least one factor belonging to either$\mathcal { U } _ { n - 1 } \setminus \mathcal { U } _ { n - 2 } \operatorname { o r } \mathcal { P } _ { n - 1 } ^ { i } \setminus \mathcal { P } _ { n - 2 } ^ { i }$. Denote that factor by σ, so that$\bar { \tau } = \sigma u$for some$u \in \mathcal W _ { n }$

Assume that$\sigma \in \mathcal { U } _ { n - 1 } \setminus \mathcal { U } _ { n - 2 }$, the argument being analogous if it belongs to one of the$\mathcal P _ { n - 1 } ^ { i } \setminus \mathcal P _ { n - 2 } ^ { i }$. Then, by definition, one has$| \sigma | _ { \mathfrak { s } } \geq \alpha ^ { ( n - 1 ) }$. Furthermore, one has$\alpha ^ { ( n - 1 ) } \geq \alpha ^ { ( n - 2 ) } + \zeta$, so that there exists some element $\hat { \sigma } \in \mathcal { U } _ { n - 2 } \setminus \mathcal { U } _ { n - 3 }$with$| \hat { \sigma } | _ { \mathfrak { s } } \leq | \sigma | _ { \mathfrak { s } } - \zeta$. By the same argument, one can find $\hat { u } \in \mathcal { W } _ { n - 1 }$with$| \hat { u } | _ { 5 } \le | u | _ { 5 }$. Consider now the element$\hat { \tau } = \mathcal { T } ( \hat { \sigma } \hat { u } )$. By the definitions, one has$\hat { \tau } \in \mathcal { U } _ { n - 1 }$and, since$\hat { \sigma } \notin \mathcal { U } _ { n - 3 }$, one has$\hat { \tau } \notin \mathcal { U } _ { n - 2 }$. Therefore, we conclude from this that

$$
\alpha^ {(n - 1)} \leq | \hat {\tau} | _ {\mathfrak {s}} \leq | \tau | _ {\mathfrak {s}} - \zeta = \alpha^ {(n)} - \zeta ,
$$

thus yielding the contradiction required to prove our claim.

Remark 8.11 If F depends explicitly on u, then one has$U \in \mathfrak { M } _ { F }$, so that one automatically has$\mathcal { U } _ { F } ~ \subset ~ \mathcal { F } _ { F }$. Similarly, if$F$depends on$\partial _ { i } u$, one has $\mathcal P _ { F } ^ { i } \subset \mathcal F _ { F }$

Remark 8.12 If$\tau \in \mathcal { F } _ { F }$is such that there exists$\tau _ { 1 }$and$\tau _ { 2 }$in$\mathcal { F }$with$\tau = \tau _ { 1 } \tau _ { 2 }$ then one also has$\tau _ { 1 } , \tau _ { 2 } \ \in \ \mathcal { F } _ { F }$. This is a consequence of the fact that, by Definition 8.6, whenever a monomial in${ \mathfrak { M } } _ { F }$can be written as a product of two monomials, each of these also belongs to${ \mathfrak { M } } _ { F }$

Similarly, if$\ b { \mathcal { T } } ( \tau ) \in \ b { \mathcal { F } } _ { F }$or$\mathcal { T } _ { i } ( \tau ) \in \mathcal { F } _ { F }$for some$\tau \in \mathcal { F }$, then one actually has$\tau \in \mathcal { F } _ { F }$

Given any problem of the type (1.1), and under Assumption 8.3, this procedure thus allows us to build a candidate T for the model space of a regularity structure, by taking for$T _ { \gamma }$the formal linear combinations of elements in$\mathcal { F } _ { F }$ with$| \tau | _ { \mathfrak { s } } = \gamma$. The spaces$T _ { \gamma }$are all finite-dimensional by Lemma 8.10, so the choice of norm on$T _ { \gamma }$is irrelevant. For example, we could simply decree that the elements of$\mathcal { F } _ { F }$form an orthonormal basis. Furthermore, the natural product in$\mathcal { F }$extends to a product on T by linearity, and by setting$\tau \star \bar { \tau } = 0$ whenever$\tau , \bar { \tau } \in \mathcal { F } _ { F }$are such that$\tau \bar { \tau } \notin \mathcal { F } _ { F }$

While we now have a candidate for a model space$T$, as well as an index set A (take$A = \{ | \tau | _ { \mathfrak { s } } : \tau \in \mathcal { F } _ { F } \} )$, we have not yet constructed the structure group$G$that allows to “translate” our model from one point to another. The remainder of this subsection is devoted to this construction. In principle, G is completely determined by the action of the group of translations on the$X ^ { k }$ the assumption that$\Gamma \Xi = \Xi$, the requirements

$$
\Gamma (\tau \bar {\tau}) = (\Gamma \tau) \star (\Gamma \bar {\tau}),
$$

for any τ,$\bar { \tau } \in \mathcal { F } _ { F }$such that$\tau { \bar { \tau } } \in \mathcal { F } _ { F }$, as well as the construction of Sect. 5.1. However, since it has a relatively explicit construction similar to the one of Sect. 4.3, we give it for the sake of completeness. This also gives us a much better handle on elements of$G _ { \cdot }$, which will be very useful in the next section. Finally, the construction of$G$given here exploits the natural relations between the integration maps$\mathcal { T } _ { k }$for different values of$k$(which are needed when considering equations involving derivatives of the solution in the right hand side), which is something that the general construction of Sect. 5.1 does not do.

In order to describe the structure group$G _ { \cdot }$, we introduce three different vector spaces. First, we denote by$\mathcal { H } _ { F }$the set of finite linear combinations of elements in$\mathcal { F } _ { F }$and by$\mathcal { H }$the set of finite linear combinations of all elements in$\mathcal { F }$. We furthermore define a set$\mathcal { F } _ { + }$consisting of all formal expressions of the type

$$
X ^ {k} \prod_ {j} \mathcal {J} _ {k _ {j}} \tau_ {j},\tag{8.7}
$$

where the product runs over finitely many terms, the$\tau _ { j }$are elements of${ \mathcal F } .$ and the$k _ { j }$are multiindices with the property that$| \tau _ { j } | _ { \mathfrak { s } } + \beta - | k _ { j } | _ { \mathfrak { s } } > 0$ for every factor appearing in this product. We should really think of$\mathcal { T } _ { k }$as being essentially the same as$\mathcal { T } _ { k }$, so that one can alternatively think of$\mathcal { F } _ { + }$ as being the set of all elements$\tau \in \mathcal { F }$such that either$\tau = 1 \mathrm { o r } | \tau | _ { \mathfrak { s } } > 0$ and such that, whenever τ can be written as$\tau = \tau _ { 1 } \tau _ { 2 }$, one also has either $\tau _ { i } = 1 \mathrm { o r } | \tau _ { i } | _ { \mathfrak { s } } > 0$. The notation$\mathcal { T } _ { k }$instead of$\mathcal { T } _ { k }$will however serve to reduce confusion in the sequel, since elements of$\mathcal { F } _ { + }$play a role that is distinct from the corresponding elements in$\mathcal { F }$. It is no coincidence that the symbol $\mathcal { I }$is the same as in Sect. 5 since elements of the type$\mathcal { T } _ { k } \tau$are precisely placeholders for the coefficients$\mathcal { T } ( x ) \tau$defined in (5.11). Similarly, we define $\hat { \mathcal { F } } _ { F } ^ { + }$as the set of symbols as in (8.7), but with the$\tau _ { j }$assumed to belong to $\mathcal { F } _ { F }$. Expressions of the type (8.7) come with a natural notion of homogeneity, given by$\begin{array} { r } { | k | _ { \mathfrak { s } } + \sum _ { i } ( | \tau _ { j } | _ { \mathfrak { s } } + \beta - | k _ { j } | _ { \mathfrak { s } } ) } \end{array}$, which is always positive by definition.

We then denote by$\mathcal { H } _ { + }$the set of all finite linear combinations of all elements in$\mathcal { F } _ { + }$, and similarly for$\mathcal { H } _ { F } ^ { + }$. Note that both$\mathcal { H }$and$\mathcal { H } _ { + }$are algebras, by simply extending the product$( \tau , \bar { \tau } ) \mapsto \tau \bar { \tau }$in a distributive way. While$\mathcal { H } _ { F }$is a linear subspace of$\mathcal { H } .$it is not in general a subalgebra of$\mathcal { H } .$, but this will not concern us very much since it is mostly the structure of the larger space$\mathcal { H }$that matters. The space$\mathcal { H } _ { F } ^ { + }$on the other hand is an algebra. (Actually the free algebra over the symbols$\{ X _ { j } , \mathcal { T } _ { k } \tau \}$, where$j \in \{ 1 , \ldots , d \} , \tau \in \mathcal { F } _ { F }$, and$k$is an arbitrary d-dimensional multiindex with$| k | _ { \mathfrak { s } } < | \tau | _ { \mathfrak { s } } + \beta . )$

We now describe a structure on the spaces H and$\mathcal { H } _ { + }$that endows$\mathcal { H } _ { + }$(resp. $\mathcal { H } _ { F } ^ { + } )$with a Hopf algebra structure and$\mathcal { H } \left( \mathrm { r e s p . ~ } \mathcal { H } _ { F } \right)$with the structure of a comodule over$\mathcal { H } _ { + } ~ ( \mathrm { r e s p . } ~ \mathcal { H } _ { F } ^ { + } )$. The purpose of these structures is to yield an explicit construction of a regularity structure that is sufficiently rich to allow to formulate fixed point maps for large classes of semilinear (stochastic) PDEs. This construction will in particular allow us to describe the structure group G in a way that is similar to the construction in Sect. 4.3, but with a slight twist since$T = \mathcal { H } _ { F }$itself is different from both the Hopf algebra$\mathcal { H } _ { + }$and the comodule H.

We first note that for every multiindex k, we have a natural linear map $\hat { \mathcal { T } } _ { k } \colon \mathcal { H } \to \mathcal { H } _ { + }$by setting

$$
\hat {\mathcal {J}} _ {k} (\tau) = \mathcal {J} _ {k} \tau , | k | _ {\mathfrak {s}} <   | \tau | _ {\mathfrak {s}} + \beta , \quad \hat {\mathcal {J}} _ {k} (\tau) = 0, \text { otherwise. }
$$

Since there can be no scope for confusion, we will make a slight abuse of notation and simply write again$\mathcal { T } _ { k }$instead of$\hat { \mathcal { I } } _ { k }$. We then define two linear maps$\Delta \colon { \mathcal { H } } \to { \mathcal { H } } \otimes { \mathcal { H } } _ { + }$and$\Delta ^ { + } \colon \mathcal { H } _ { + } \to \mathcal { H } _ { + } \otimes \mathcal { H } _ { + }$by

$$
\begin{array}{l l} \Delta \mathbf {1} = \mathbf {1} \otimes \mathbf {1}, & \Delta^ {+} \mathbf {1} = \mathbf {1} \otimes \mathbf {1}, \\ \Delta X _ {i} = X _ {i} \otimes \mathbf {1} + \mathbf {1} \otimes X _ {i}, & \Delta^ {+} X _ {i} = X _ {i} \otimes \mathbf {1} + \mathbf {1} \otimes X _ {i} \\ \Delta \Xi = \Xi \otimes \mathbf {1}, \end{array}
$$

and then, recursively, by

$$
\Delta (\tau \bar {\tau}) = (\Delta \tau) (\Delta \bar {\tau})\tag{8.8a}
$$

$$
\Delta (\mathcal {I} _ {k} \tau) = \left(\mathcal {I} _ {k} \otimes I\right) \Delta \tau + \sum_ {\ell , m} \frac {X ^ {\ell}}{\ell !} \otimes \frac {X ^ {m}}{m !} \mathcal {J} _ {k + \ell + m} \tau ,\tag{8.8b}
$$

as well as

$$
\Delta^ {+} (\tau \bar {\tau}) = (\Delta^ {+} \tau) (\Delta^ {+} \bar {\tau})\tag{8.9a}
$$

$$
\Delta^ {+} (\mathcal {J} _ {k} \tau) = \sum_ {\ell} \left(\mathcal {J} _ {k + \ell} \otimes \frac {(- X) ^ {\ell}}{\ell !}\right) \Delta \tau + \mathbf {1} \otimes \mathcal {J} _ {k} \tau .\tag{8.9b}
$$

In both cases, these sums run in principle over all possible multiindices  and m. Note however that these sums are actually finite since, by definition, for $| \ell | _ { \mathfrak { s } }$large enough it is always the case that$\mathcal { T } _ { k + \ell } \tau = 0$

Remark 8.13 By construction, for every$\tau \in \mathcal { F }$, one has the identity$\Delta \tau =$ $\begin{array} { r } { \tau \otimes \mathbf { 1 } + \sum _ { i } c _ { i } \dot { \tau } _ { i } ^ { ( 1 ) } \otimes \tau _ { i } ^ { ( 2 ) } } \end{array}$, for some constants$c _ { i }$and some elements with ${ | \tau _ { i } ^ { ( 1 ) } | _ { \mathfrak { s } } } < | \tau | _ { \mathfrak { s } }$and$| \tau _ { i } ^ { ( 1 ) } | _ { \mathfrak { s } } + | \tau _ { i } ^ { ( 2 ) } | _ { \mathfrak { s } } = | \tau | _ { \mathfrak { s } }$. This is a reflection in this context of the condition (2.1).

Similarly, for every$\sigma \in \mathcal { F } _ { + }$, one has the identity

$$
\Delta^ {+} \sigma = \sigma \otimes {\bf 1} + {\bf 1} \otimes \sigma + \sum_ {i} c _ {i} \sigma_ {i} ^ {(1)} \otimes \sigma_ {i} ^ {(2)},
$$

for some constants$c _ { i }$and some elements with$| \sigma _ { i } ^ { ( 1 ) } | _ { \mathfrak { s } } + | \sigma _ { i } ^ { ( 2 ) } | _ { \mathfrak { s } } = | \sigma | _ { \mathfrak { s } }$. Note also that (8.9) is coherent with our abuse of notation for$\hat { \mathcal { I } } _ { k }$in the sense that if τ and k are such that$\hat { \mathcal { T } } _ { k } \tau = 0$, then the right hand side automatically vanishes.

Remark 8.14 The fact that it is$\Delta$(rather than$\Delta ^ { + } )$that appears in the right hand side of (8.9b) is not a typo: there is not much choice since$\tau \in \mathcal { F }$and not in$\mathcal { F } _ { + }$. The motivation for the definitions of$\Delta$and$\Delta ^ { + }$will be given in Sect. 8.2 below where we show how it allows to canonically lift a continuous realisation$\xi$of the “noise” to a model for the regularity structure built from these algebraic objects.

Remark 8.15 In the sequel, we will use Sweedler’s notation for coproducts. Whenever we write$\begin{array} { r } { \dot { \Delta \tau } = \sum \tau ^ { ( 1 ) } \otimes \tau ^ { ( 2 ) } } \end{array}$, this should be read as a shorthand for: “There exists a finite index set I, non-zero constants$\{ c _ { i } \} _ { i \in I }$, and basis elements$\{ \tau _ { i } ^ { ( 1 ) } \} _ { i \in I } , \{ \tau _ { i } ^ { ( 2 ) } \} _ { i \in I }$such that the identity$\begin{array} { r } { \Delta \tau = \sum _ { i \in I } c _ { i } \tau _ { i } ^ { ( 1 ) } \otimes \tau _ { i } ^ { ( 2 ) } } \end{array}$ holds.” If we then later refer to a joint property of$\tau ^ { ( 1 ) }$and$\tau ^ { ( 2 ) }$, this means that the property in question holds for every pair$( \tau _ { i } ^ { ( 1 ) } , \tau _ { i } ^ { ( 2 ) } )$appearing in the above sum.

The structure just introduced has the following nice algebraic properties.

Theorem 8.16 The space$\mathcal { H } _ { + }$is a Hopf algebra and H is a comodule over $\mathcal { H } _ { + }$. In particular, one has the identities

$$
(I \otimes \Delta^ {+}) \Delta \tau = (\Delta \otimes I) \Delta \tau ,\tag{8.10a}
$$

$$
(I \otimes \Delta^ {+}) \Delta^ {+} \tau = (\Delta^ {+} \otimes I) \Delta^ {+} \tau ,\tag{8.10b}
$$

for every$\tau \in { \mathcal { H } } .$. Furthermore, there exists an idempotent antipode$\mathcal { A } \colon \mathcal { H } _ { + } \to$ $\mathcal { H } _ { + }$, satisfying the identity

$$
\mathcal {M} (I \otimes \mathcal {A}) \Delta^ {+} \tau = \left\langle \mathbf {1} ^ {*}, \tau \right\rangle \mathbf {1} = \mathcal {M} (\mathcal {A} \otimes I) \Delta^ {+} \tau ,\tag{8.11}
$$

where we denotedby$\mathcal { M } \colon \mathcal { H } _ { + } \otimes \mathcal { H } _ { + }  \mathcal { H } _ { + }$the multiplication operator defined by$\mathcal { M } ( \tau \otimes \bar { \tau } ) = \tau \bar { \tau }$, and by$1 ^ { * }$the element of$\mathcal { H } _ { + } ^ { \ast }$such that$\langle \mathbf { 1 } ^ { * } , \mathbf { 1 } \rangle = 1$and $\langle \mathbf { 1 } ^ { * } , \tau \rangle = 0$for all$\tau \in \mathcal { F } _ { + } \setminus \{ 1 \}$

Proof We first prove (8.10a). Both operators map 1 onto$\mathbf { 1 } \otimes \mathbf { 1 } \otimes \mathbf { 1 } , \Xi$onto $\Xi \otimes { \bf 1 } \otimes { \bf 1 }$, and$X _ { i }$onto$X _ { i } \otimes \mathbf { 1 } \otimes \mathbf { 1 } + \mathbf { 1 } \otimes X _ { i } \otimes \mathbf { 1 } + \mathbf { 1 } \otimes \mathbf { 1 } \otimes X _ { i }$. Since$\mathcal { F }$ is then generated by multiplication and action with$\mathcal { T } _ { k }$, we can verify (8.10a) recursively by showing that it is stable under products and applications of the integration maps.

Assume first that, for some τ and$\bar { \tau }$in${ \mathcal { F } } _ { : }$, the identity (8.10a) holds when applied to both τ and τ. By (8.8a), (8.9a), and the induction hypothesis, one then has the identity

$$
\begin{array}{r l} & {(I \otimes \Delta^ {+}) \Delta (\tau \bar {\tau}) = (I \otimes \Delta^ {+}) (\Delta \tau \Delta \bar {\tau}) = \big ((I \otimes \Delta^ {+}) \Delta \tau \big) \big ((I \otimes \Delta^ {+}) \Delta \bar {\tau} \big)} \\ & {\qquad = \big ((\Delta \otimes I) \Delta \tau \big) \big ((\Delta \otimes I) \Delta \bar {\tau} \big) = (\Delta \otimes I) (\Delta \tau \Delta \bar {\tau})} \\ & {\qquad = (\Delta \otimes I) \Delta (\tau \bar {\tau}),} \end{array}
$$

as required.

It remains to show that if (8.10a) holds for some$\tau \in \mathcal { F }$, then it also holds for$\mathcal { T } _ { k } \tau$for every multiindex k. First, by (8.8b) and (8.9b), one has the identity

$$
\begin{array}{l} (I \otimes \Delta^ {+}) \Delta \mathcal {I} _ {k} \tau = (I \otimes \Delta^ {+}) (\mathcal {I} _ {k} \otimes I) \Delta \tau + \sum_ {\ell , m} \frac {X ^ {\ell}}{\ell !} \otimes \Delta^ {+} \left(\frac {X ^ {m}}{m !} \mathcal {J} _ {k + \ell + m} \tau\right) \\ = (\mathcal {I} _ {k} \otimes I \otimes I) (I \otimes \Delta^ {+}) \Delta \tau \\ + \sum_ {\ell , m, n} \frac {X ^ {\ell}}{\ell !} \otimes \left(\frac {X ^ {m}}{m !} \otimes \frac {X ^ {n}}{n !}\right) \Delta^ {+} \mathcal {J} _ {k + \ell + m + n} \tau , \end{array} \tag {8.12}
$$

where we used the multiplicative property of$\Delta ^ { + }$and the fact that

$$
\Delta^ {+} \frac {X ^ {k}}{k !} = \sum_ {m \leq k} \frac {X ^ {m}}{m !} \otimes \frac {X ^ {k - m}}{(k - m) !}.
$$

(Note again that the seemingly infinite sums appearing in (8.12) are actually all finite since$\mathcal { T } _ { k } \tau = 0$for k large enough. This will be the case for every expression of this type appearing below.) At this stage, we use the recursion relation (8.9b) which yields

$$
\begin{array}{l} \sum_ {m, n} \Big (\frac {X ^ {m}}{m !} \otimes \frac {X ^ {n}}{n !} \Big) \Delta^ {+} \mathcal {J} _ {k + m + n} \tau = \sum_ {m, n} \Big (\frac {X ^ {m}}{m !} \otimes \frac {X ^ {n}}{n !} \mathcal {J} _ {k + m + n} \tau \Big) \\ \qquad + \sum_ {\ell , m, n} \Big (\frac {X ^ {m}}{m !} \mathcal {J} _ {k + \ell + m + n} \otimes \frac {X ^ {n}}{n !} \frac {(- X) ^ {\ell}}{\ell !} \Big) \Delta \tau \\ \qquad = \sum_ {m, n} \Big (\frac {X ^ {m}}{m !} \otimes \frac {X ^ {n}}{n !} \mathcal {J} _ {k + m + n} \tau \Big) + \sum_ {m} \Big (\frac {X ^ {m}}{m !} \mathcal {J} _ {k + m} \otimes I \Big) \Delta \tau . \end{array}
$$

Here we made use of the fact that$\scriptstyle \sum _ { \ell + n = k } { \frac { X ^ { n } } { n ! } } { \frac { ( - X ) ^ { \ell } } { \ell ! } }$always vanishes, except when$k = 0$ + = ! !in which case itjust yields 1. Inserting this in the above expression, we finally obtain the identity

$$
\begin{array}{l} (I \otimes \Delta^ {+}) \Delta \mathcal {I} _ {k} \tau = (\mathcal {I} _ {k} \otimes I \otimes I) (I \otimes \Delta^ {+}) \Delta \tau \\ \qquad + \sum_ {\ell , m, n} \frac {X ^ {\ell}}{\ell !} \otimes \frac {X ^ {m}}{m !} \otimes \frac {X ^ {n}}{n !} \mathcal {J} _ {k + \ell + m + n} \tau \\ \qquad + \sum_ {\ell , m} \frac {X ^ {\ell}}{\ell !} \otimes \Big (\frac {X ^ {m}}{m !} \mathcal {J} _ {k + \ell + m} \otimes I \Big) \Delta \tau . \end{array}\tag{8.13}
$$

On the other hand, using again (8.8b), (8.9b), and the binomial identity, we obtain

$$
\begin{array}{l} (\Delta \otimes I) \Delta \mathcal {I} _ {k} \tau = (\Delta \mathcal {I} _ {k} \otimes I) \Delta \tau + \sum_ {\ell , m} (\Delta \otimes I) \left(\frac {X ^ {\ell}}{\ell !} \otimes \frac {X ^ {m}}{m !} \mathcal {J} _ {k + \ell + m} \tau\right) \\ = (\mathcal {I} _ {k} \otimes I \otimes I) (\Delta \otimes I) \Delta \tau + \sum_ {\ell , m} \frac {X ^ {\ell}}{\ell !} \otimes \Bigl (\frac {X ^ {m}}{m !} \mathcal {J} _ {k + \ell + m} \otimes I \Bigr) \Delta \tau \\ + \sum_ {\ell , m, n} \frac {X ^ {\ell}}{\ell !} \otimes \frac {X ^ {m}}{m !} \otimes \frac {X ^ {n}}{n !} \mathcal {J} _ {k + \ell + m + n} \tau . \end{array}
$$

Comparing this expression with (8.13) and using the induction hypothesis, the claim follows at once.

We now turn to the proof of (8.10b). Proceeding in a similar way as before, we verify that the claim holds for$\tau = 1 , \tau = X _ { i }$, and$\tau = \Xi$. Using the fact that$\Delta ^ { + }$is a multiplicative morphism, it follows as before that if (8.10b) holds for τ and$\bar { \tau }$, then it also holds for$\tau { \bar { \tau } }$. It remains to show that it holds for$\mathcal { T } _ { k } \tau$ One verifies, similarly to before, that one has the identity

$$
\begin{array}{l} (\Delta^ {+} \otimes I) \Delta^ {+} \mathcal {J} _ {k} \tau = \mathbf {1} \otimes \mathbf {1} \otimes \mathcal {J} _ {k} \tau + \mathbf {1} \otimes \sum_ {\ell} \Bigl (\mathcal {J} _ {k + \ell} \otimes \frac {(- X) ^ {\ell}}{\ell !} \Bigr) \Delta \tau \\ \qquad + \sum_ {\ell , m} \Bigl (\mathcal {J} _ {k + \ell + m} \otimes \frac {(- X) ^ {\ell}}{\ell !} \otimes \frac {(- X) ^ {m}}{m !} \Bigr) (\Delta \otimes I) \Delta \tau , \end{array}
$$

while one also has

$$
(I \otimes \Delta^ {+}) \Delta^ {+} \mathcal {J} _ {k} \tau = \mathbf {1} \otimes \sum_ {\ell} \Bigl (\mathcal {J} _ {k + \ell} \otimes \frac {(- X) ^ {\ell}}{\ell !} \Bigr) \Delta \tau + \mathbf {1} \otimes \mathbf {1} \otimes \mathcal {J} _ {k} \tau
$$

$$
+ \sum_ {\ell , m} \left(\mathcal {J} _ {k + \ell + m} \otimes \frac {(- X) ^ {\ell}}{\ell !} \otimes \frac {(- X) ^ {m}}{m !}\right) (I \otimes \Delta^ {+}) \Delta \tau .
$$

The claim now follows from (8.10a).

It remains to show that$\mathcal { H } _ { + }$admits an antipode$\mathcal { A } \colon \mathcal { H } _ { + } \to \mathcal { H } _ { + }$. This is automatic for connected graded bialgebras but it turns out that in our case, although it admits a natural integer grading,$\mathcal { H } _ { + }$is not connected for it (i.e. there is more than one basis element with vanishing degree). It is ofcourse connected for the grading$| \cdot | _ { \mathfrak { s } } ,$, but this is not integer-valued. The general construction of $\mathcal { A }$however still works in essentially the same way. The natural integer grading $| \cdot |$on$\mathcal { F } _ { + }$for this purpose is defined recursively by$| X _ { i } | = | \Xi | = | \mathbf { 1 } | = 0$ and then$| \tau \bar { \tau } | = | \tau | + | \bar { \tau } |$and$| \mathcal { T } _ { k } \tau | = | \tau | + 1$. In plain terms, it counts the number of times that an integration operator arises in the formal expression$\tau$

Recall that A should be a linear map satisfying (8.11), and we furthermore want$\mathcal { A }$to be a multiplicative morphism namely, for$\tau = \tau _ { 1 } \tau _ { 2 }$, we impose that $\mathcal { A } \tau = ( \mathcal { A } \tau _ { 1 } ) ( \mathcal { A } \tau _ { 2 } )$. To construct${ \mathcal { A } } .$, we start by setting

$$
\mathcal {A} X _ {i} = - X _ {i}, \quad \mathcal {A} \mathbf {1} = \mathbf {1}.\tag{8.14}
$$

Given the construction of$\mathcal { H } _ { + }$, it then remains to define$\mathcal { A }$on elements of the type$\mathcal { T } _ { k } \tau$with$\tau \in \mathcal { H }$and$| \mathcal { T } _ { k } \tau | _ { \mathfrak { s } } > 0$. This should be done in such a way that one has

$$
\mathcal {M} (I \otimes \mathcal {A}) \Delta^ {+} \mathcal {J} _ {k} \tau = 0,\tag{8.15}
$$

which then guarantees that the first equality in (8.11) holds for all$\tau \in \mathcal { H } _ { + }$. This is because$\mathcal { M } ( I \otimes \mathcal { A } ) \Delta ^ { + }$is then a multiplicative morphism which vanishes on $X _ { i }$and every element of the form$\mathcal { T } _ { k } \tau$, and, except for$\tau = 1$, every element of$\mathcal { F } _ { + }$has at least one such factor.

To show that it is possible to enforce (8.15) in a coherent way, we proceed by induction. Indeed, by the definition of$\Delta ^ { + }$and the definition of$\mathcal { M }$, one has the identity

$$
\mathcal {M} (I \otimes \mathcal {A}) \Delta^ {+} \mathcal {J} _ {k} \tau = \sum_ {\ell} \mathcal {M} \Big (\mathcal {J} _ {k + \ell} \otimes \frac {X ^ {\ell}}{\ell !} \mathcal {A} \Big) \Delta \tau + \mathcal {A} \mathcal {J} _ {k} \tau .
$$

Therefore,$\mathcal { A T } _ { k } \tau$is determined by (8.15) as soon as we know$( I \otimes \mathcal { A } ) \Delta \tau$ This can be guaranteed by iterating over$\mathcal { F }$in an order of increasing degree. (In the sense of the number of times that the integration operator appears in a formal expression, as defined above.)

We can then show recursively that the antipode also satisfies$\mathcal { M } ( A \otimes$ $I ) \Delta ^ { + } \tau = 1 ^ { * } ( \tau ) 1$. Again, we only need to verify it inductively on elements of

the form$\mathcal { T } _ { k } \tau$. One then has

$$
\begin{array}{l} \mathcal {M} (\mathcal {A} \otimes I) \Delta^ {+} \mathcal {J} _ {k} \tau = \mathcal {J} _ {k} \tau + \sum_ {\ell} \frac {(- X) ^ {\ell}}{\ell !} \mathcal {M} \big (\mathcal {A} \mathcal {J} _ {k + \ell} \otimes I \big) \Delta \tau \\ \qquad = \mathcal {J} _ {k} \tau - \sum_ {\ell , m} \frac {(- X) ^ {\ell} X ^ {m}}{\ell ! m !} \mathcal {M} \big (\mathcal {J} _ {k + \ell + m} \otimes \mathcal {A} \otimes I \big) \big (\Delta \otimes I \big) \Delta \tau \\ \qquad = \mathcal {J} _ {k} \tau - \mathcal {M} \big (\mathcal {J} _ {k} \otimes \mathcal {A} \otimes I \big) \big (I \otimes \Delta^ {+} \big) \Delta \tau , \end{array}
$$

where we used the fact that$\begin{array} { r } { \sum _ { \ell + m = n } { \frac { ( - X ) ^ { \ell } X ^ { m } } { \ell ! m ! } } = 0 } \end{array}$unless$n = 0$in which  + = ! !case it is 1. At this stage, we use the fact that it is straightforward to verify inductively that

$$
(I \otimes \mathbf {1} ^ {*}) \Delta \tau = \tau ,\tag{8.16}
$$

for every$\tau \ \in \ { \mathcal { H } } .$, so that an application of our inductive hypothesis yields $\mathcal { M } ( \mathcal { A } \otimes I ) \Delta ^ { + } \mathcal { T } _ { k } \tau = \mathcal { T } _ { k } \tau - \mathcal { T } _ { k } \tau = 0$as required. The fact that$A ^ { 2 } \tau = \tau$can be verified in a similar way. It is also a consequence of the fact that the Hopf algebra$\mathcal { H } _ { + }$is commutative [95].□

Remark$8 . I 7$Note that H is not a Hopf module over$\mathcal { H } _ { + }$since the identity $\Delta ( \tau \bar { \tau } ) = \Delta \tau \Delta ^ { + } \bar { \tau }$does in general not hold for any$\tau \in \mathcal { H }$and$\bar { \tau } \in \mathcal { H } _ { + }$ However,$\hat { \mathcal { H } } = \mathcal { H } \otimes \mathcal { H } _ { + }$can be turned in a very natural way into a Hopf module over$\mathcal { H } _ { + }$. The module structure is given by$( \tau \otimes { \bar { \tau } } _ { 1 } ) { \bar { \tau } } _ { 2 } = \tau \otimes ( { \bar { \tau } } _ { 1 } { \bar { \tau } } _ { 2 } )$ for$\tau \in \mathcal { H }$and$\bar { \tau } _ { 1 } , \bar { \tau } _ { 2 } \in \mathcal { H } _ { + }$, while the comodule structure$\hat { \Delta } \colon \hat { \mathcal { H } }  \hat { \mathcal { H } } \otimes \mathcal { H } _ { + }$ is given by

$$
\hat {\Delta} (\tau \otimes \bar {\tau}) = \Delta \tau \cdot \Delta^ {+} \bar {\tau},
$$

where$( \tau _ { 1 } \otimes \tau _ { 2 } ) \cdot ( \bar { \tau } _ { 1 } \otimes \bar { \tau } _ { 2 } ) = ( \tau _ { 1 } \otimes \bar { \tau } _ { 1 } ) \otimes ( \tau _ { 2 } \bar { \tau } _ { 2 } )$for$\tau _ { 1 } \in \mathcal { H }$and$\tau _ { 2 } , \bar { \tau } _ { 1 } , \bar { \tau } _ { 2 } \in \mathcal { H } _ { + }$ These structures are then compatible in the sense that$( \hat { \Delta } \otimes I ) \hat { \Delta } = ( I \otimes \Delta ^ { + } ) \hat { \Delta }$ and$\hat { \Delta } ( \tau \bar { \tau } ) = \hat { \Delta } \tau \cdot \Delta ^ { + } \bar { \tau }$. It is not clear at this stage whether known general results on these structures (like the fact that Hopf modules are always free) can be of use for the type of analysis performed in this article.

We are now almost ready to construct the structure group$G$in our context. First, we define a product on$\mathcal { H } _ { + } ^ { \ast }$, the dual of$\mathcal { H } _ { + }$, by

Definition 8.18 Given two elements g,$\bar { G } \in \mathcal { H } _ { + } ^ { * }$, their product$g \circ { \bar { G } }$is given by the dual of$\Delta ^ { + } , \mathrm { i . e . }$, it is the element satisfying

$$
\left\langle g \circ \bar {G}, \tau \right\rangle = \left\langle g \otimes \bar {G}, \Delta^ {+} \tau \right\rangle ,
$$

for all$\tau \in \mathcal { H } _ { + }$

From now on, we will use the notations$\langle g , \tau \rangle , g ( \tau )$, or even$g \tau$interchangeably for the duality pairing. We also identify$X \otimes \mathbf { R }$with X in the usual way $( x \otimes c \sim c x )$for any space X. Furthermore, to any$g \in \mathcal { H } _ { + } ^ { * }$, we associate a linear map$\Gamma _ { g } \colon \mathcal { H } \to \mathcal { H }$in essentially the same way as in (4.19), by setting

$$
\Gamma_ {g} \tau = (I \otimes g) \Delta \tau .\tag{8.17}
$$

Note that, by (8.16), one has$\Gamma _ { 1 ^ { * } } \tau = \tau$. One can also verify inductively that the co-unit$^ { 1 ^ { * } }$is indeed the neutral element for$^ { \circ . }$. With these definitions at hand, we have

Proposition 8.19 For any$g , { \bar { G } } \in { \mathcal { H } } _ { + } ^ { * }$, one has$\Gamma _ { g } \Gamma _ { \bar { G } } = \Gamma _ { g \circ \bar { G } }$. Furthermore, the product is associative.

Proof One has the identity

$$
\begin{array}{r} \Gamma_ {g} \Gamma_ {\bar {G}} \tau = \Gamma_ {g} (I \otimes \bar {G}) \Delta \tau = (I \otimes g \otimes \bar {G}) (\Delta \otimes I) \Delta \tau \\ = (I \otimes g \otimes \bar {G}) (I \otimes \Delta^ {+}) \Delta \tau = (I \otimes (g \circ \bar {G})) \Delta \tau , \end{array}
$$

where we first used Theorem 8.16 and then the definition of the product . The associativity of is equivalent to the coassociativity (8.10b) of$\Delta ^ { + }$, which we already proved in Theorem 8.16.□

We now have all the ingredients in place to define the structure group$G \mathrm { : }$:

Definition 8.20 The group G is given by the group-like elements$g \in \mathcal { H } _ { + } ^ { * }$ i.e. the elements such that$g ( \tau _ { 1 } \tau _ { 2 } ) = g ( \tau _ { 1 } ) g ( \tau _ { 2 } )$for any$\tau _ { i } \in \mathcal { H } _ { + }$. Its action on H is given by$g \mapsto \Gamma _ { g }$

This definition is indeed meaningful thanks to the following standard result:

Proposition 8.21 Given$g , { \bar { G } } \in G$, one has$g \circ { \bar { G } } \in G$. Furthermore, each element$g \in G$has a unique inverse$g ^ { - 1 }$

Proof This is standard, see [95]. The explicit expression for the inverse is simply$g ^ { - 1 } ( \tau ) = g ( \mathcal { A } \tau )$□

Finally, we note that our operations behave well when restricting ourselves to the spaces$\mathcal { H } _ { F }$and$\mathcal { H } _ { F } ^ { + }$constructed as explained previously by only considering those formal expressions that are “useful” for the description ofthe nonlinearity $F \colon$

Lemma 8.22 One has$\Delta \colon { \mathcal { H } } _ { F } \to { \mathcal { H } } _ { F } \otimes { \mathcal { H } } _ { F } ^ { + } a n d \Delta ^ { + } \colon { \mathcal { H } } _ { F } ^ { + } \to { \mathcal { H } } _ { F } ^ { + } \otimes { \mathcal { H } } _ { F } ^ { + } .$

Proof We claim that actually, even more is true. Recall the definitions of the sets$\mathcal { W } _ { n } , \mathcal { U } _ { n }$and$\mathcal { P } _ { n } ^ { i }$from (8.3) and denote by$\langle \mathcal { W } _ { n } \rangle$the linear span of$\mathcal { W } _ { n }$ in$\mathcal { H } _ { F }$, and similarly for$\left. l _ { n } \right.$and$\langle \mathcal { P } _ { n } ^ { i } \rangle$. Then, denoting by$\mathcal { X }$any of these vector spaces, we claim that$\Delta$has the property that$\Delta \bar { \mathcal { X } } \subset \mathcal { X } \otimes \bar { \mathcal { H } } _ { F } ^ { + }$, which in particular then also implies that the action of$G$leaves each of the spaces$\mathcal { X }$ invariant. This can easily be seen by induction over n. The claim is clearly true for$n = 0$by definition. Assuming now that it holds for$\langle \mathcal { U } _ { n - 1 } \rangle$and$\langle \mathcal { P } _ { n - 1 } ^ { i } \rangle$ it follows from the definition of$\mathcal { W } _ { n }$and the morphism property of$\Delta$that the claim also holds for$\mathcal { W } _ { n }$. The identity (8.8b) then also implies that the claim is true for$\left. l _ { n } \right.$and$\langle \mathcal { P } _ { n } ^ { i } \rangle$, as required.

Regarding the property$\Delta ^ { + } \colon \mathcal { H } _ { F } ^ { + } \to \mathcal { H } _ { F } ^ { + } \otimes \mathcal { H } _ { F } ^ { + }$, it follows from the morphism property of$\Delta ^ { + }$(and the fact that$\mathcal { H } _ { F } ^ { + }$itselfis closed under multiplication) that we only need to check it on elements τ of the form$\tau = \mathcal { T } _ { k } \bar { \tau }$with$\bar { \tau } \in \mathcal { F } _ { F }$ Using (8.9b), the claim then immediately follows from the first claim.□

Remark 8.23 This shows that the action of$G$onto$\mathcal { H } _ { F }$is equivalent to the action of the quotient group$G _ { F }$obtained by identifying elements that act in the same way onto$\mathcal { H } _ { F } ^ { + }$

This concludes our construction of the regularity structure associated to a general subcritical semilinear (S)PDE, which we summarise as a theorem:

Theorem 8.24 Let F be a locally subcritical nonlinearity, let$T = \mathcal { H } _ { F }$with $T _ { \gamma } = \langle \{ \tau \in \mathcal { F } _ { F } : | \tau | _ { \mathfrak { s } } = \gamma \} \rangle , A = \{ | \tau | _ { \mathfrak { s } } : \tau \in \mathcal { F } _ { F } \}$, and$G _ { F }$be defined as above. Then,$\mathcal { T } _ { F } = ( A , \mathcal { H } _ { F } , G _ { F } )$, defines a regularity structure$\mathcal { T }$. Furthermore, I is an abstract integration map oforder$\beta$for$\mathcal { T }$

Proof To check that$\mathcal { T } _ { F }$is a regularity structure, the only property that remains to be shown is (2.1). This however follows immediately from the fact that if one writes$\begin{array} { r } { \Delta \tau = \sum \tau ^ { ( 1 ) } \otimes \tau ^ { ( 2 ) } } \end{array}$, then each of these terms satisfies$| \tau ^ { ( 1 ) } | _ { \mathfrak { s } } + | \tau ^ { ( 2 ) } | _ { \mathfrak { s } } =$ $| \tau | _ { s }$and$| \tau ^ { ( 2 ) } | _ { \mathfrak { s } } \geq 0$. Furthermore, one verifies by induction that the term $\tau \otimes 1$appears exactly once in this sum, so that for all other terms,$\tau ^ { ( 1 ) }$is of homogeneity strictly smaller than that of$\tau$.

The map$\mathcal { T }$obviously satisfies the first two requirements of an abstract integration map by our definitions. The last property follows from the fact that

$$
\Gamma_ {g} \mathcal {I} _ {k} \tau = (I \otimes g) \Delta \mathcal {I} _ {k} \tau = (I \otimes g) (\mathcal {I} _ {k} \otimes I) \Delta \tau + \sum_ {\ell} \frac {(X - x _ {g}) ^ {\ell}}{\ell !} g \big (\mathcal {J} _ {k + \ell} \tau \big),
$$

where we defined$x _ { g } \in \mathbf { R } ^ { d }$as the element with coordinates$- g ( X _ { i } )$. Noting that$( I \otimes g ) ( \mathcal { T } _ { k } \otimes I ) \Delta \tau = \mathcal { T } _ { k } \Gamma _ { g } \tau$, the claim follows.□

Remark 8.25 If some element of${ \mathfrak { M } } _ { F }$also contains a factor$\mathcal { P } _ { i }$, then one can check in the same way as above that$\mathscr { T } _ { i }$is an abstract integration map of order $\beta - { \mathfrak { s } } _ { i }$for$\mathcal { T }$

Remark 8.26 Given$F$as above and$r > 0$, we will sometimes write$\mathcal { T } _ { F } ^ { ( r ) }$ (or simply$\mathcal { T } ^ { ( r ) }$when F is clear from the context) for the regularity structure obtained as above, but with$T _ { \gamma } = 0$for$\gamma > r$

## 8.2 Realisations of the general algebraic structure

While the results of the previous subsection provide a systematic way of constructing a regularity structure$\mathcal { T }$that is sufficiently rich to allow to reformulate (8.1) as a fixed point problem which has some local solution$U \in \mathcal { D } _ { P } ^ { \gamma , \eta }$for suitable indices$\gamma$and$\eta$, it does not at all address the problem of constructing a model (or family of models) ( , ) such that$\mathcal { R } U$can be interpreted as a limit of classical solutions to some regularised version of (8.1).

It is in the construction of the model ( , ) that one has to take advantage of additional knowledge about$\xi$(for example that it is Gaussian), which then allows to use probabilistic tools, combined with ideas from renormalisation theory, to build a “canonical model” (or in many cases actually a canonical finite-dimensional family of models) associated to it. We will see in Sect. 10 below how to do this in the particular cases of (PAMg) and$( \Phi ^ { 4 } )$. For any continuous realisation of the driving noise however, it is straightforward to “lift” it to the regularity structure that we just built, as we will see presently.

Given any continuous approximation$\xi _ { \varepsilon }$to the driving noise$\xi$, we now show how one can build a canonical model$( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$) for the regularity structure $\mathcal { T }$built in the previous subsection. First, we set

$$
\bigl (\Pi_ {x} ^ {(\varepsilon)} \Xi \bigr) (y) = \xi_ {\varepsilon} (y), \quad \bigl (\Pi_ {x} ^ {\varepsilon} X ^ {k} \bigr) (y) = (y - x) ^ {k}.
$$

Then, we recursively define$\Pi _ { x } ^ { ( \varepsilon ) } \tau$by

$$
\left(\Pi_ {x} ^ {(\varepsilon)} \tau \bar {\tau}\right) (y) = \left(\Pi_ {x} ^ {(\varepsilon)} \tau\right) (y) \left(\Pi_ {x} ^ {(\varepsilon)} \bar {\tau}\right) (y),\tag{8.18}
$$

as well as

$$
\bigl (\Pi_ {x} ^ {(\varepsilon)} \mathcal {I} _ {k} \tau \bigr) (y) = \int D _ {1} ^ {k} K (y, z) \left(\Pi_ {x} ^ {(\varepsilon)} \tau\right) (z) d z + \sum_ {\ell} \frac {(y - x) ^ {\ell}}{\ell !} f _ {x} ^ {(\varepsilon)} \bigl (\mathcal {J} _ {k + \ell} \tau \bigr).\tag{8.19}
$$

In this expression, the quantities$f _ { x } ^ { ( \varepsilon ) } ( \mathcal { T } _ { \ell } \tau )$are defined by

$$
f _ {x} ^ {(\varepsilon)} \big (\mathcal {J} _ {\ell} \tau \big) = - \int D _ {1} ^ {\ell} K (x, z) \left(\Pi_ {x} ^ {(\varepsilon)} \tau\right) (z) d z.\tag{8.20}
$$

If we furthermore impose that

$$
f _ {x} ^ {(\varepsilon)} (X _ {i}) = - x _ {i}, \qquad f _ {x} ^ {(\varepsilon)} (\tau \bar {\tau}) = \big (f _ {x} ^ {(\varepsilon)} \tau \big) \big (f _ {x} ^ {(\varepsilon)} \bar {\tau} \big),\tag{8.21}
$$

and extend this to all of$\mathcal { H } _ { F } ^ { + }$by linearity, then$f _ { x } ^ { ( \varepsilon ) }$defines an element of the group$G _ { F }$given in Definition 8.20 and Remark 8.23.

Denote by$F _ { x } ^ { ( \varepsilon ) }$the corresponding linear operator on$\mathcal { H } _ { F }$, i.e.$F _ { x } ^ { \left( \varepsilon \right) } = \Gamma _ { f _ { x } ^ { \left( \varepsilon \right) } }$ where the map$g \mapsto \Gamma _ { g }$is given by (8.17). With these definitions at hand, we then define$\Gamma _ { x y } ^ { ( \varepsilon ) }$by

$$
\Gamma_ {x y} ^ {(\varepsilon)} = \left(F _ {x} ^ {(\varepsilon)}\right) ^ {- 1} \circ F _ {y} ^ {(\varepsilon)}.\tag{8.22}
$$

Furthermore, for any$\tau \in \mathcal { F }$, we denote by$V _ { \tau }$the sector given by the linear span of$\{ \Gamma \tau : \Gamma \in G \}$. This is also given by the projection of$\Delta \tau$onto its first factor. We then have:

Proposition 8.27 Let K be as in Lemma 5.5 and satisfying Assumption 5.4for some$r > 0 .$. Let furthermore$\mathcal { T } _ { F } ^ { ( r ) }$be the regularity structure obtained from any semilinear locally subcritical problem as in Sect. 8.1 and Remark 8.26. Letfinally$\xi _ { \varepsilon } \colon \mathbf { R } ^ { d } \to \mathbf { R }$be a smooth function and let$( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$be defined as above. Then,$( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$is a modelfor$\mathcal { T } _ { F } ^ { ( r ) }$

Furthermore, for any$\tau \in \mathcal { F } _ { F }$such that$\mathcal { T } _ { k } \tau \in \mathcal { F } _ { F }$, the model$( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$) realises the abstract integration operator$\mathcal { T } _ { k }$on the sector$V _ { \tau }$

Proof We need to verify both the algebraic relations and the analytical bounds of Definition 2.17. The fact that$\Gamma _ { x y } ^ { ( \varepsilon ) } \Gamma _ { y z } ^ { ( \varepsilon ) } = \Gamma _ { x z } ^ { ( \varepsilon ) }$is immediate from the definition (8.22). In view of (8.22), the identity$\Pi _ { x } ^ { ( \varepsilon ) } \Gamma _ { x y } ^ { ( \varepsilon ) } = \Pi _ { y } ^ { ( \varepsilon ) }$follows if we can show that

$$
\Pi_ {x} ^ {(\varepsilon)} \big (F _ {x} ^ {(\varepsilon)} \big) ^ {- 1} \tau = \Pi_ {y} ^ {(\varepsilon)} \big (F _ {y} ^ {(\varepsilon)} \big) ^ {- 1} \tau ,\tag{8.23}
$$

for every$\tau \in \mathcal { F } _ { F }$and any two points x and y. In order to show that this is the case, it turns out that it is easiest to simply “guess” an expression for $\Pi _ { x } ^ { ( \varepsilon ) } ( F _ { x } ^ { ( \varepsilon ) } ) ^ { - 1 } \tau$that is independent of x and to then verify recursively that our guess was correct. For this, we define a linear map$\pmb { \Pi } ^ { ( \varepsilon ) } \colon \mathcal { H } _ { F }  \mathcal { C } ( \mathbf { R } ^ { d } )$by

$$
\big (\boldsymbol {\Pi} ^ {(\varepsilon)} \mathbf {1} \big) (y) = 1, \quad \big (\boldsymbol {\Pi} ^ {(\varepsilon)} X _ {i} \big) (y) = y _ {i}, \quad \big (\boldsymbol {\Pi} ^ {(\varepsilon)} \Xi \big) (y) = \xi_ {\varepsilon} (y),
$$

and then recursively by

$$
\left(\boldsymbol {\Pi} ^ {(\varepsilon)} \tau \bar {\tau}\right) (y) = \left(\boldsymbol {\Pi} ^ {(\varepsilon)} \tau\right) (y) \left(\boldsymbol {\Pi} ^ {(\varepsilon)} \bar {\tau}\right) (y),\tag{8.24}
$$

as well as

$$
\left(\boldsymbol {\Pi} ^ {(\varepsilon)} \mathcal {I} _ {k} \tau\right) (y) = \int D _ {1} ^ {k} K (y, z) \left(\boldsymbol {\Pi} ^ {(\varepsilon)} \tau\right) (z) d z.\tag{8.25}
$$

We claim that one has$\Pi _ { x } ^ { ( \varepsilon ) } ( F _ { x } ^ { ( \varepsilon ) } ) ^ { - 1 } \tau = \Pi ^ { ( \varepsilon ) } \tau$for every$\tau \in \mathcal { F } _ { F }$and every $x \in \mathbf { R } ^ { d }$. Actually, it is easier to verify the equivalent identity

$$
\Pi_ {x} ^ {(\varepsilon)} \tau = \Pi^ {(\varepsilon)} F _ {x} ^ {(\varepsilon)} \tau .\tag{8.26}
$$

To show this, we proceed by induction. The identity obviously holds for $\tau = \Xi$and$\tau = 1$. For$\tau = X _ { i }$, we have by (8.21)

$$
\begin{array}{c} \big (\boldsymbol {\Pi} ^ {(\varepsilon)} F _ {x} ^ {(\varepsilon)} X _ {i} \big) (y) = \big ((\boldsymbol {\Pi} ^ {(\varepsilon)} \otimes f _ {x} ^ {(\varepsilon)}) (X _ {i} \otimes \mathbf {1} + \mathbf {1} \otimes X _ {i}) \big) (y) \\ = y _ {i} - x _ {i} = \big (\Pi_ {x} ^ {(\varepsilon)} X _ {i} \big) (y). \end{array}
$$

Furthermore, in view of (8.24), (8.18), and the fact that$F _ { x } ^ { ( \varepsilon ) }$acts as a multi plicative morphism, it holds for$\tau { \bar { \tau } }$if it holds for both$\tau$and$\bar { \tau }$.

To complete the proof of (8.23), it remains to show that (8.26) holds for elements of the form$\mathcal { T } _ { k } \tau$if it holds for τ. It follows from the definitions that

$$
\begin{array}{r l} & F _ {x} ^ {(\varepsilon)} \mathcal {I} _ {k} \tau = \mathcal {I} _ {k} F _ {x} ^ {(\varepsilon)} \tau + \sum_ {\ell , m} \frac {X ^ {\ell}}{\ell !} f _ {x} ^ {(\varepsilon)} \Big (\frac {X ^ {m}}{m !} \mathcal {J} _ {k + \ell + m} \tau \Big) \\ & \qquad = \mathcal {I} _ {k} F _ {x} ^ {(\varepsilon)} \tau + \sum_ {\ell , m} \frac {X ^ {\ell}}{\ell !} \frac {(- x) ^ {m}}{m !} f _ {x} ^ {(\varepsilon)} \Big (P \mathcal {J} _ {k + \ell + m} \tau \Big) \\ & \qquad = \mathcal {I} _ {k} F _ {x} ^ {(\varepsilon)} \tau + \sum_ {\ell} \frac {(X - x) ^ {\ell}}{\ell !} f _ {x} ^ {(\varepsilon)} \big (\mathcal {J} _ {k + \ell} \tau \big), \end{array}\tag{8.27}
$$

where we used (8.21), the morphism property of$f _ { x } ^ { ( \varepsilon ) }$, and the binomial identity. The above identity is precisely the abstract analogue in this context of the identity postulated in Definition 5.9.

Inserting this into (8.25), we obtain the identity

$$
\begin{array}{r l} & {\big (\boldsymbol {\Pi} ^ {(\varepsilon)} F _ {x} ^ {(\varepsilon)} \mathcal {I} _ {k} \tau \big) (y) = \int D _ {1} ^ {k} K (y, z) \big (\boldsymbol {\Pi} ^ {(\varepsilon)} F _ {x} ^ {(\varepsilon)} \tau \big) (z) d z} \\ & {\qquad + \sum_ {\ell} \frac {(y - x) ^ {\ell}}{\ell !} f _ {x} ^ {(\varepsilon)} \big (\mathcal {J} _ {k + \ell} \tau \big).} \end{array}\tag{8.28}
$$

Since$\Pi ^ { ( \varepsilon ) } F _ { x } ^ { ( \varepsilon ) } \tau = \Pi _ { x } ^ { ( \varepsilon ) } \tau$by our induction hypothesis, this is precisely equal to the right hand side of (8.19), as required.

It remains to show that the required analytical bounds also hold. Regarding $\Pi _ { x } ^ { ( \varepsilon ) }$, we actually show the slightly stronger fact that$( \Pi _ { x } ^ { ( \varepsilon ) } \tau ) ( y ) \lesssim \| x - y \| _ { \mathfrak { s } } ^ { | \tau | _ { \mathfrak { s } } }$ This is obvious for$\tau \ : = \ : X _ { i }$as well as for$\tau = \Xi$since$| \Xi | _ { \mathfrak { s } } < 0$and we assumed that$\xi _ { \varepsilon }$is continuous. (Of course, such a bound would typically not hold uniformly in ε!) Since$| \tau \bar { \tau } | _ { \mathfrak { s } } = | \tau | _ { \mathfrak { s } } + | \bar { \tau } | _ { \mathfrak { s } } .$, it is also obvious that such a bound holds for$\tau \bar { \tau }$if it holds for both τ and τ. Regarding elements of the form $\mathcal { T } _ { k } \tau$, we note that the second term in (8.19) is precisely the truncated Taylor series of the first term, so that the required bound holds by Proposition 11.1 or, more generally, by Theorem 5.14. To conclude the proof that$( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$ is a model for our regularity structure, it remains to obtain a bound of the type (2.15) for$\Gamma _ { x y } ^ { \left( \varepsilon \right) }$. In principle, this also follows from Theorem 5.14, but we can also verify it more explicitly in this case.

Note that the required bound follows if we can show that

$$
| \gamma_ {x y} ^ {(\varepsilon)} (\tau) | \stackrel {{\mathrm{def}}} {{=}} \bigl | \bigl (f _ {x} \mathcal {A} \otimes f _ {y} \bigr) \Delta^ {+} \tau \bigr | \lesssim \| x - y \| _ {\mathfrak {s}} ^ {| \tau | _ {\mathfrak {s}}},
$$

for all$\tau \in \mathcal { F } _ { F } ^ { + }$with$| \tau | _ { \mathfrak { s } } \leq r$. Again, this can easily be checked for$\tau = X ^ { k }$ For$\tau = \mathcal { T } _ { k } \bar { \tau }$, note that one has the identity

$$
\begin{array}{l} \big (\mathcal {A} \otimes I \big) \Delta^ {+} \mathcal {J} _ {k} \bar {\tau} = \mathbf {1} \otimes \mathcal {J} _ {k} \bar {\tau} \\ - \sum_ {\ell , m} \big (\mathcal {M} \otimes I \big) \Big (\mathcal {J} _ {k + \ell + m} \otimes \frac {X ^ {\ell}}{\ell !} \mathcal {A} \otimes \frac {(- X) ^ {m}}{m !} \Big) \big (I \otimes \Delta^ {+} \big) \Delta \bar {\tau}. \end{array}
$$

As a consequence, we have the identity

$$
\gamma_ {x y} ^ {(\varepsilon)} (\mathcal {J} _ {k} \bar {\tau}) = f _ {y} ^ {(\varepsilon)} (\mathcal {J} _ {k} \bar {\tau}) - \sum_ {\ell} \frac {(y - x) ^ {\ell}}{\ell !} f _ {x} ^ {(\varepsilon)} (\mathcal {J} _ {k + \ell} \Gamma_ {x y} ^ {(\varepsilon)} \bar {\tau}).
$$

It now suffices to realise that this is equal to the quantity$\left( \Gamma _ { y x } ^ { \left( \varepsilon \right) } \mathcal { T } _ { x y } \bar { \tau } \right) _ { k }$ where$\mathcal { I } _ { x y }$ was introduced in (5.36), so that the required bound follows from Lemma 5.21. There is an unfortunate notational clash between$\mathcal { I } _ { x y }$and$\mathcal { T } _ { k }$ appearing here, but since this is the only time in the article that both objects appear simultaneously, we leave it at that.

The fact that the model built in this way realises K for the abstract integration operator I (and indeed for any of the$\textstyle { \mathcal { T } } _ { k } )$follows at once from the definition (8.19).□

Remark 8.28 In general, one does not even need$\xi _ { \varepsilon }$to be continuous. One just needs it to be in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$for sufficiently large (but possibly negative) α such that all the products appearing in the above construction satisfy the conditions of Proposition 4.14.

This construction motivates the following definition, where we assume that the kernel K annihilates monomials up to order r and that we are given a regularity structure$\mathcal { T } _ { F }$built from a locally subcritical nonlinearity$F$as above.

Definition 8.29 A model ( , ) for$\mathcal { T } _ { F } ^ { ( r ) }$is admissible if it satisfies $( \Pi _ { x } X ^ { k } ) ( y ) \ : = \ : ( y - x ) ^ { k }$, as well as (8.19), (8.21), (8.22), and (8.20). We denote by$\mathcal { M } _ { F }$the set of admissible models.

Note that the set of admissible models is a closed subset of the set of all models and that the models built from canonical lifts of smooth functions $\xi ^ { ( \varepsilon ) }$are admissible by definition. Admissible models are also adapted to the integration map K (and suitable derivatives thereof) for the integration map$\mathcal { T }$ (and the maps$\mathcal { T } _ { k }$if applicable). Actually, the converse is also true provided that we define f by (8.20). This can be shown by a suitable recursion procedure, but since we will never actually use this fact we do not provide a full proof.

Remark 8.30 It is not clear in general whether canonical lifts of smooth functions are dense in$\mathcal { M } _ { F }$. As the definitions stand, this will actually never be the case since smooth functions are not even dense in$\mathcal { C } ^ { \alpha } !$This is however an artificial problem that can easily be resolved in a manner similar to what we did in the proof of the reconstruction theorem, Theorem 3.10. (See also the note [43].) However, even when allowing for some weaker notion of density, it will in general not be the case that lifts of smooth functions are dense. This is because the regularity structure$\mathcal { T } _ { F } ^ { ( r ) }$built in this section does not encode the Leibniz rule, so that it can accommodate the type of effects described in [55,61,62] (or even just$\mathrm { I t } \hat { \mathrm { o } } ^ { \prime } \mathrm { s }$formula in one dimension) which cannot arise when only considering lifts of smooth functions.

## 8.3 Renormalisation group associated to the general algebraic structure

There are many situations where, if we take for$\xi _ { \varepsilon }$a smooth approximation to $\xi$such that$\xi _ { \varepsilon } \to \xi$in a suitable sense, the sequence$( \Pi ^ { ( \varepsilon ) } , \bar { \Gamma ^ { ( \varepsilon ) } } )$of models built from$\xi _ { \varepsilon }$as in the previous section fails to converge. This is somewhat different from the situation encountered in the context of the theory of rough paths where natural smooth approximations to the driving noise very often do yield finite limits without the need for renormalisation [28,44]. (The reason why this is so stems from the fact that if a process X is symmetric under time-reversal, then the expression$X _ { i } \partial _ { t } X _ { j }$is antisymmetric, thus introducing additional cancellations. Recall the discussion on the role of symmetries in Remark 1.9.)

In general, in order to actually build a model associated to the driving noise $\xi$, we will need to be able to encode some kind of renormalisation procedure. In the context of the regularity structures built in this section, it turns out that they come equipped with a natural group of continuous transformations on their space of admissible models. At the abstract level, this group of transformations (which we call R) will be nothing but a finite-dimensional nilpotent Lie group – in many instances just a copy of$\mathbf { R } ^ { n }$for some$n > 0$. As already mentioned in the introduction, a renormalisation procedure then consists in finding a sequence$M _ { \varepsilon }$of elements in R such that$\bar { M } _ { \varepsilon } ( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$converges to a finite limit ( , ), where$( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$is the bare model built in Sect. 8.2. As previously, different renormalisation procedures yield limits that differ only by an element in R.

Remark 8.31 The construction outlined in this section, and indeed the whole methodology presented here, has a flavour that is strongly reminiscent of the theory given in [22,23]. The scope however is different: the construction pre-sented here applies to subcritical situations in which one obtains superrenormalisable theories, so that the group R is always finite-dimensional. The construction of [22,23] on the other hand applies to critical situations and yields an infinite-dimensional renormalisation group.

Assume that we are given some model ( , ) for our regularity structure $\mathcal { T }$. As before, we assume that$\Gamma _ { x y }$is provided to us in the form

$$
\Gamma_ {x y} = F _ {x} ^ {- 1} \circ F _ {y},\tag{8.29}
$$

and we denote by$f _ { x }$the group-like element in the dual of$\mathcal { H } _ { F } ^ { + }$corresponding to$F _ { x }$. As a consequence, the operator$\Pi _ { x } F _ { x } ^ { - 1 }$is independent of x and, as in Sect. 8.2, we will henceforth denote it simply by

$$
\Pi \stackrel {\mathrm{def}} {=} \Pi_ {x} F _ {x} ^ {- 1}.\tag{8.30}
$$

Throughout this whole section, we will thus represent a model by the pair (-, f) where - is one single linear map -$T  S ^ { \prime } ( \mathbf { R } ^ { d } )$and f is a map on $\mathbf { R } ^ { d }$with values in the morphisms of$\mathcal { H } _ { F } ^ { + }$

We furthermore make the additional assumption that our model is admissible, so that one has the identities

$$
\boldsymbol {\Pi} \mathcal {I} _ {k} \tau = \int_ {\mathbf {R} ^ {d}} D ^ {k} K (\cdot , y) (\boldsymbol {\Pi} \tau) (d y),\tag{8.31}
$$

$$
f _ {x} \mathcal {J} _ {k} \tau = - \int_ {\mathbf {R} ^ {d}} D ^ {k} K (x, y) (\Pi_ {x} \tau) (d y),\tag{8.32}
$$

where, in view of (8.30), - and$\Pi _ { x }$are related by

$$
\boldsymbol {\Pi} \tau = (\Pi_ {x} \otimes f _ {x} \mathcal {A}) \Delta \tau , \quad \Pi_ {x} \tau = (\boldsymbol {\Pi} \otimes f _ {x}) \Delta \tau .
$$

Note that by definition, (8.32) only ever applies to elements with$| \mathcal { T } _ { k } \tau | _ { \mathfrak { s } } > 0$ which implies that the corresponding integral actually makes sense. In view of (8.8b) and (5.12), this ensures that our model does realise K for the abstract integration operator$\mathcal { T }$(and, if needed, the relevant derivatives of K for the $\textstyle { \mathcal { T } } _ { k } )$. It is crucial that any transformation that we would like to apply to our model preserves this property, since otherwise the operators$\kappa _ { \gamma }$cannot be constructed anymore for the new model.

Remark 8.32 While it is clear that$( \Pi , f )$is sufficient to determine the corresponding model by (8.29) and (8.30), the converse is not true in general if one only imposes (8.29). However, if we also impose (8.32), together with the canonical choice$f _ { x } ( X ) = - x$, then$f$is uniquely determined by the model in its usual representation ( , ). This shows that although the transformations constructed in this section will be given in terms of$f ,$, they do actually define maps defined on the set$\mathcal { M } _ { F }$of all admissible models.

The important feature ofR is its action on elements τ ofnegative homogeneity. It turns out that, in order to describe it, it is convenient to work on a slightly larger set$\mathcal { F } _ { 0 } \subset \mathcal { F } _ { F }$with some additional properties. Given any set$\mathcal { C } \subset \mathcal { F } _ { F }$ we will henceforth denote by$\mathrm { A l g } ( { \mathcal { C } } ) \subset { \mathcal { F } } _ { F } ^ { + }$the set of all elements in$\mathcal { F } _ { F } ^ { + }$of the form$X ^ { k } \prod _ { i } \mathcal { T } _ { \ell _ { i } } \tau _ { i }$, for some multiindices$k$and$\ell _ { i }$such that$| \mathcal { T } _ { \ell _ { i } } \tau _ { i } | _ { \mathfrak { s } } > 0$ and where the elements$\tau _ { i }$all belong to$\mathcal { C } .$. (The empty product also counts, so that one always has$X ^ { k } \in \operatorname { A l g } ( { \mathcal { C } } )$and in particular$\mathbf { 1 } \in \mathrm { A l g } ( \mathcal { C } ) . )$We will also use the notation C for the linear span of a set$\mathcal { C } .$. We now fix a subset $\mathcal { F } _ { 0 } \subset \mathcal { F } _ { F }$as follows.

Assumption 8.33 The set$\mathcal { F } _ { 0 } \subset \mathcal { F } _ { F }$has thefollowing properties:

The set$\mathcal { F } _ { 0 }$contains every$\tau \in \mathcal { F } _ { F }$with$| \tau | _ { \mathfrak { s } } \le 0 .$

There exists$\mathcal { F } _ { \star } \subset \mathcal { F } _ { 0 }$such that, for every$\tau \in \mathcal { F } _ { 0 }$, one has$\Delta \tau \in \langle \mathcal { F } _ { 0 } \rangle$ $\langle \mathrm { A l g } ( \mathcal { F } _ { \star } ) \rangle$

Remark 8.34 Similarly to before, we write$\mathcal { H } _ { 0 } = \langle \mathcal { F } _ { 0 } \rangle , \mathcal { F } _ { 0 } ^ { + } = \mathrm { A l g } ( \mathcal { F } _ { \star } )$, and $\mathcal { H } _ { 0 } ^ { + } = \langle \mathcal { F } _ { 0 } ^ { + } \rangle$. Proceeding as in the proofs of Lemmas 8.38 and 8.39 below, one can verify that the second condition automatically implies that the operators $\Delta ^ { + }$and A both leave$\mathcal { H } _ { 0 } ^ { + }$invariant.

Let now$M \colon \mathcal { H } _ { 0 }  \mathcal { H } _ { 0 }$be a linear map such that$M \mathcal { T } _ { k } \tau = \mathcal { T } _ { k } M \tau$for every $\tau \in \mathcal { F } _ { 0 }$such that$\mathcal { T } _ { k } \tau \in \mathcal { F } _ { 0 }$. Then, we would like to use the map M to build a new model$( \mathbf { I I } ^ { M } , f ^ { M } )$with the property that

$$
\boldsymbol {\Pi} ^ {M} \boldsymbol {\tau} = \boldsymbol {\Pi} M \boldsymbol {\tau}.\tag{8.33}
$$

(The condition$M \mathcal { T } _ { k } \tau = \mathcal { T } _ { k } M \tau$is required to guarantee that (8.31) still holds for$\boldsymbol { \Pi } ^ { M } . )$This is not always possible, but the aim of this section is to provide conditions under which it is. In order to realise the above identity, we would like to build linear maps$\Delta ^ { M } \colon \mathcal { H } _ { 0 } \to \mathcal { H } _ { 0 } \times \mathcal { H } _ { 0 } ^ { + }$and$\hat { M } : \mathcal { H } _ { 0 } ^ { + } \to \dot { \mathcal { H } } _ { 0 } ^ { + }$such that one has

$$
\Pi_ {x} ^ {M} \tau = (\Pi_ {x} \otimes f _ {x}) \Delta^ {M} \tau , \quad f _ {x} ^ {M} \tau = f _ {x} \hat {M} \tau .\tag{8.34}
$$

Remark 8.35 One might wonder why we choose to make the ansatz (8.34). The first identity really just states that$\Pi _ { x } ^ { M } \tau$is given by a bilinear expression of the type

$$
\Pi_ {x} ^ {M} \tau = \sum_ {\tau_ {1}, \tau_ {2}} C _ {\tau} ^ {\tau_ {1}, \tau_ {2}} f _ {x} (\tau_ {1}) \Pi_ {x} \tau_ {2},
$$

which is not unreasonable since the objects appearing on the right hand side are the only objects available as “building blocks” for our construction. One might argue that the coefficients could be given by some polynomial expression in the$f _ { x } ( \tau _ { 1 } )$, but thanks to the fact that$f _ { x }$is group-like, this can always be reformulated as a linear expression. Similarly, the second expression simply states that$f _ { x } ^ { M }$is given by some arbitrary linear (or polynomial by the same argument as before) expression in the$f _ { x }$

Furthermore, we would like to ensure that if the pair$( \Pi , f )$satisfies the identities (8.31) and (8.32), then the pair$( \boldsymbol { \Pi } ^ { M } , f ^ { M } )$also satisfies them. Inserting (8.34) into (8.32), we see that this is guaranteed if we impose that

$$
\hat {M} \mathcal {J} _ {k} = \mathcal {M} (\mathcal {J} _ {k} \otimes I) \Delta^ {M},\tag{8.35a}
$$

where, as before, M$\mathcal { H } _ { 0 } ^ { + } \times \mathcal { H } _ { 0 } ^ { + } \to \mathcal { H } _ { 0 } ^ { + }$denotes the multiplication map. We also note that if we want to ensure that (8.33) holds, then we should require that, for every$x \in \mathbf { R } ^ { d }$, one has the identity$\Pi M = \Pi _ { x } ^ { M } \big ( F _ { x } ^ { M } \big ) ^ { - 1 }$, which we rewrite as$\Pi _ { x } ^ { M } = \pmb { \Pi } M F _ { x } ^ { M }$ . Making use of the first identity of (8.34) and of the fact that$\Pi _ { x } = \Pi F _ { x }$, the left hand side of this identity can be expressed as

$$
\Pi_ {x} ^ {M} \tau = \big (\Pi \otimes f _ {x} \otimes f _ {x}) (\Delta \otimes I) \Delta^ {M} \tau = \big (\Pi \otimes f _ {x}) (I \otimes \mathcal {M}) (\Delta \otimes I) \Delta^ {M} \tau .
$$

Using the second identity of (8.34), the right hand side on the other hand can be rewritten as

$$
\boldsymbol {\Pi} M F _ {x} ^ {M} \boldsymbol {\tau} = (\boldsymbol {\Pi} \otimes f _ {x} ^ {M}) (M \otimes I) \Delta \boldsymbol {\tau} = (\boldsymbol {\Pi} \otimes f _ {x}) (M \otimes \hat {M}) \Delta \boldsymbol {\tau}.
$$

We see that these two expressions are guaranteed to be equal for any choice of - and$f _ { x }$if we impose the consistency condition

$$
(I \otimes \mathcal {M}) (\Delta \otimes I) \Delta^ {M} = (M \otimes \hat {M}) \Delta .\tag{8.35b}
$$

Finally, we impose that$\hat { M }$is a multiplicative morphism and that it leaves$X ^ { k }$ invariant, namely that

$$
\hat {M} (\tau_ {1} \tau_ {2}) = (\hat {M} \tau_ {1}) (\hat {M} \tau_ {2}), \quad \hat {M} X ^ {k} = X ^ {k},\tag{8.35c}
$$

which is a natural condition given its interpretation. In view of (8.34), this is required to ensure that$f _ { x } ^ { M }$is again a group-like element with$f _ { x } ^ { M } ( X _ { i } ) = - x _ { i }$ which is crucial for our purpose. It then turns out that equations (8.35a)–(8.35c) are sufficient to uniquely characterise$\Delta ^ { M }$and$\hat { M }$and that it is always possible to find two operators satisfying these constraints:

Proposition 8.36 Given a linear map M as above, there exists a unique choice of M andˆ$\Delta ^ { M }$satisfying (8.35a)–(8.35c).

In order to prove this result, it turns out to be convenient to consider the following recursive construction of elements in$\mathcal { H } _ { F }$. We define$\mathcal { F } ^ { ( 0 ) } = \varnothing$and then, recursively,

$$
\mathcal {F} ^ {(n + 1)} = \left\{\tau \in \mathcal {F} _ {F}: \Delta \tau \in \mathcal {H} _ {F} \otimes \left\langle \operatorname{Alg} (\mathcal {F} ^ {(n)}) \right\rangle \right\}.\tag{8.36}
$$

Remark 8.37 In practice, a typical choice for the set$\mathcal { F } _ { 0 }$of Assumption 8.33 is to take$\mathcal { F } _ { 0 } = \mathcal { F } ^ { ( n ) }$and$\mathscr { F } _ { \star } = \bar { \mathscr { F } } ^ { ( n - 1 ) }$for some sufficiently large n, which then automatically has the required properties by Lemma 8.38 below. In particular, this also shows that such sets do exist.

For example,$\mathcal { F } ^ { ( 1 ) }$contains all elements of the form$\Xi ^ { n } X ^ { k }$that belong to $\mathcal { F } _ { F }$, but it might contain more than that depending on the values of$\alpha$and$\beta$. The following properties of these sets are elementary:

One has$\mathcal { F } ^ { ( n - 1 ) } \subset \mathcal { F } ^ { ( n ) }$. This is shown by induction. For$n \ = \ 1$, the statement is trivially true. If it holds for some n then one has$\mathrm { A l g } ( \mathcal { F } ^ { ( n - 1 ) } ) \subset$ $\mathrm { A l g } ( \mathcal { F } ^ { ( n ) } )$) and so, by (8.36), one also has${ \mathcal { F } } ^ { ( n ) } \subset { \mathcal { F } } ^ { ( n + 1 ) }$, as required.

If$\tau , \bar { \tau } \in \mathcal { F } ^ { ( n ) }$are such that$\tau { \bar { \tau } } ~ \in ~ \mathcal { F } _ { F }$, then$\tau \bar { \tau } \in \mathcal { F } ^ { ( n ) }$as an immediate consequence of the morphism property of$\Delta$, combined with the definition of$\mathrm { A l g }$

If$\tau ~ \in ~ \mathcal { F } ^ { ( n ) }$and k is such that$\mathcal { T } _ { k } \tau ~ \in ~ \mathcal { F } _ { F }$, then$\mathcal { T } _ { k } \tau ~ \in ~ \mathcal { F } ^ { ( n + 1 ) }$. As a consequence of this fact, and since all elements in$\mathcal { F } _ { F }$can be generated by multiplication and integration from$\Xi$and the$X _ { i }$, one has$\begin{array} { r } { \dot { \bigcup } _ { n \geq 0 } \mathcal { F } ^ { ( n ) } = } \end{array}$ $\mathcal { F } _ { F }$

The following consequence is slightly less obvious:

Lemma 8.38 For every$n ~ \geq ~ 0$and$\tau ~ \in ~ \mathcal { F } ^ { ( n ) }$, one has$\Delta \tau ~ \in ~ \langle \mathcal { F } ^ { ( n ) } \rangle$⊗ $\langle \mathbf { A l g } ( \mathcal { F } ^ { ( n - 1 ) } ) \rangle$. For every$n ~ \geq ~ 0$and$\tau ~ \in ~ \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } )$), one has$\Delta ^ { + } \tau \in$ $\langle \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } ) \rangle \otimes \rangle \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } ) \rangle$.

Proof We proceed by induction. For$n \ = \ 0$, both statements are trivially true, so we assume that they hold for all$n \leq k$. Take then$\tau \in \mathcal { F } ^ { ( k + 1 ) }$and assume by contradiction that$\Delta \tau \not \in \langle \mathcal { F } ^ { ( k + 1 ) } \rangle \otimes \langle \mathrm { A l g } ( \mathcal { F } ^ { ( k ) } ) \rangle$. This then implies that$( \Delta \otimes I ) \Delta \tau \ \not \in \ { \mathcal { H } } _ { F } \otimes \langle { \mathrm { A l g } } ( { \mathcal { F } } ^ { ( k ) } ) \rangle \otimes \langle { \mathrm { A l g } } ( { \mathcal { F } } ^ { ( k ) } ) \rangle$. However, we have $( \Delta \otimes I ) \Delta \tau \ : = \ : ( I \otimes \Delta ^ { + } ) \Delta \tau$by Theorem 8.16 and$\Delta ^ { + }$maps$\langle \mathrm { A l g } ( \mathcal { F } ^ { ( k ) } ) \rangle$ to$\langle \operatorname { A l g } ( { \mathcal { F } } ^ { ( k ) } ) \rangle \otimes \langle \operatorname { A l g } ( { \mathcal { F } } ^ { ( k ) } ) \rangle$by our induction hypothesis, thus yielding the required contradiction.

It remains to show that$\Delta ^ { + }$has the desired property for$n = k + 1$. Since $\Delta ^ { + }$is a multiplicative morphism, we can assume that τ is of the form$\tau = \mathcal { T } _ { \ell } \bar { \tau }$ with$\bar { \tau } \in \mathcal { F } ^ { ( k + 1 ) }$. One then has by definition

$$
\Delta^ {+} \tau = \sum_ {m} \Bigl (\mathcal {J} _ {\ell + m} \otimes \frac {(- X) ^ {m}}{m !} \Bigr) \Delta \bar {\tau} + \mathbf {1} \otimes \tau .
$$

By the first part of the proof, we already know that$\Delta \bar { \tau } \ \in \ \left. \mathcal { F } ^ { ( k + 1 ) } \right.$⊗ $\left. \mathrm { A l g } ( \mathcal { F } ^ { ( k ) } ) \right.$, so that the first term belongs to$\langle \mathrm { A l g } ( \mathcal { F } ^ { ( k + 1 ) } ) \rangle \otimes \langle \mathrm { A l g } ( \mathcal { F } ^ { ( k ) } ) \rangle$ The second term on the other hand belongs to$\langle \mathrm { A l g } ( \mathcal { F } ^ { ( 0 ) } ) \rangle \otimes \langle \mathrm { A l g } ( \mathcal { F } ^ { ( k + 1 ) } ) \rangle$ by definition, so that the claim follows.□

A useful consequence of Lemma 8.38 is the following.

Lemma 8.39$I f \tau \in \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } )$for some$n \geq 0 _ { : }$, then$\mathcal { A } \tau \ \in \ \langle \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } ) \rangle$ where A is the antipode in$\mathcal { H } _ { + }$defined in the previous subsection.

Proof The proof goes by induction, using the relations$\mathcal { A } ( \tau \bar { \tau } ) = \mathcal { A } ( \tau ) \mathcal { A } ( \bar { \tau } )$ as well as the identity

$$
\mathcal {A J} _ {k} \bar {\tau} = - \sum_ {\ell} \mathcal {M} \Big (\mathcal {J} _ {k + \ell} \otimes \frac {X ^ {\ell}}{\ell !} \mathcal {A} \Big) \Delta \bar {\tau},\tag{8.37}
$$

which is valid as soon as$| \mathcal { T } _ { k } \bar { \tau } | _ { 5 } > 0$. For$n = 0$, the claim is trivially true. For arbitrary$n > 0$, by the multiplicative property of${ \mathcal { A } } ,$, it suffices to consider the case$\tau = \mathcal { T } _ { k } \bar { \tau }$with$\bar { \tau } \in \mathcal { F } ^ { ( n ) }$. Since$\Delta \bar { \tau } \in \langle \mathcal { F } ^ { ( n ) } \rangle \otimes \langle \mathrm { A l g } ( \mathcal { F } ^ { ( n - 1 ) } ) \rangle$by Lemma 8.38, it follows from our definitions and the inductive assumption that the right hand side of (8.37) does indeed belong to$\langle \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } ) \rangle \otimes \langle \mathrm { A \bar { l g } } ( \mathcal { F } ^ { ( n ) } ) \rangle$ as required.□

We now have all the ingredients in place for the

ProofofProposition 8.36 We first introduce the map$D \colon { \mathcal { H } } _ { 0 } \otimes { \mathcal { H } } _ { 0 } ^ { + } \to { \mathcal { H } } _ { 0 } \otimes$ $\mathcal { H } _ { 0 } ^ { + }$given by$D = ( I \otimes \mathcal { M } ) ( \Delta \otimes I )$. It follows immediately from the definition of$\Delta$and the fact that, by Lemma 8.10, homogeneities of elements in$\mathcal { F } _ { F }$(and a fortiori of elements in$\mathcal { F } _ { 0 } )$are bounded from below, that D can be written as

$$
D (\tau \otimes \bar {\tau}) = \tau \otimes \bar {\tau} - \bar {D} (\tau \otimes \bar {\tau}),
$$

for some nilpotent map$\bar { D }$. As a consequence, D is invertible with inverse given by the Neumann series$\begin{array} { r } { D ^ { - 1 } = \sum _ { k \geq 0 } \bar { D } ^ { k } } \end{array}$, which is always finite.

The proof of the statement then goes by induction over${ \mathcal { F } } ^ { ( n ) } \cap { \mathcal { F } } _ { 0 }$. Assume that$\hat { M }$and$\Delta ^ { M }$are uniquely defined on$\mathrm { A l g } ( \mathcal { F } ^ { ( n ) } \cap \mathcal { F } _ { \star } )$and on${ \mathcal { F } } ^ { ( n ) } \cap { \mathcal { F } } _ { 0 }$ respectively which, by (8.35c), is trivially true for$n = 0$. (For$\Delta ^ { M }$this is also trivial since$\mathcal { F } ^ { ( 0 ) }$is empty.) Take then$\tau \in \mathcal { F } ^ { ( n + 1 ) } \cap \mathcal { F } _ { 0 }$. By (8.35b), one has

$$
\Delta^ {M} \tau = D ^ {- 1} (M \otimes \hat {M}) \Delta \tau .
$$

By Lemma 8.38 and Remark 8.34, the second factor of$\Delta \tau$belongs to $\left. \dot { \mathrm { A l g } } ( \mathcal { F } ^ { ( n ) } \cap \mathcal { F } _ { \star } ) \right.$on which$\hat { M }$is already known by assumption, so that this uniquely determines$\Delta ^ { M } \tau$

On the other hand, in order to determine$\hat { M }$on elements of$\mathrm { A l g } ( \mathcal { F } ^ { ( n + 1 ) } \cap \mathcal { F } _ { \star } )$ it suffices by (8.35c) and Remark 8.34 to determine it on elements of the form$\tau = \mathcal { T } _ { k } \bar { \tau }$with$\bar { \tau } \in \mathcal { F } ^ { ( n + 1 ) } \cap \mathcal { F } _ { \star }$. The action of$\hat { M }$on such elements is determined by (8.35a) so that, since we already know by the first part of the proof that$\Delta ^ { \bar { M } } \bar { \tau }$is uniquely determined, the proof is complete.□

Before we proceed, we introduce a final object whose utility will be clear later on. Similarly do the definition of$\Delta ^ { M }$, we define$\hat { \Delta } ^ { M } : \mathcal { H } _ { 0 } ^ { + } \mathbf { \bar { \Delta } } \to \mathcal { H } _ { 0 } ^ { + } \otimes \mathcal { H } _ { 0 } ^ { + }$ by the identity

$$
(\mathcal {A} \hat {M} \mathcal {A} \otimes \hat {M}) \Delta^ {+} = (I \otimes \mathcal {M}) (\Delta^ {+} \otimes I) \hat {\Delta} ^ {M}.\tag{8.38}
$$

Note that, similarly to before, one can verify that the map$D ^ { + } = ( I \otimes \mathcal M ) ( \Delta ^ { + } \otimes$ $I )$is invertible on$\mathcal { H } _ { 0 } ^ { + } \otimes \mathcal { H } _ { 0 } ^ { + }$, so that this expression does indeed define$\hat { \Delta } ^ { M }$ uniquely.

Remark 8.40 Note also that in the particular case when$M = I$, the identity, one has$\Delta ^ { M } \tau = \tau \otimes { \mathbf { 1 } } , \hat { \Delta } ^ { M } \tau = \tau \otimes { \mathbf { 1 } }$, as well as$\hat { M } = I$

With these notations at hand, we then give the following description of the “renormalisation group” R:

Definition 8.41 Let$\mathcal { F } _ { F }$and$\mathcal { F } _ { 0 }$be as above. Then the corresponding renormalisation group R consists of all linear maps$M \colon \mathcal { H } _ { 0 }  \mathcal { H } _ { 0 }$such that M commutes with the$\mathcal { T } _ { k }$, such that$M X ^ { k } = X ^ { k }$, and such that, for every$\tau \in \mathcal { F } _ { 0 }$ and every$\hat { \tau } \in \mathcal { F } _ { 0 } ^ { + }$, one can write

$$
\Delta^ {M} \tau = \tau \otimes {\bf 1} + \sum \tau^ {(1)} \otimes \tau^ {(2)}, \quad \hat {\Delta} ^ {M} \bar {\tau} = \bar {\tau} \otimes {\bf 1} + \sum \bar {\tau} ^ {(1)} \otimes \bar {\tau} ^ {(2)},\tag{8.39}
$$

where each of the$\tau ^ { ( 1 ) } \in \mathcal { F } _ { 0 }$and$\bar { \tau } ^ { ( 1 ) } \in \mathcal { F } _ { 0 } ^ { + }$is such that$\vert \tau ^ { ( 1 ) } \vert _ { \mathfrak { s } } > \vert \tau \vert _ { \mathfrak { s } }$and $| \bar { \tau } ^ { ( 1 ) } | _ { \mathfrak { s } } > | \bar { \tau } | _ { \mathfrak { s } }$

Remark 8.42 Note that$\hat { \Delta } ^ { M }$is automatically a multiplicative morphism. Since one has furthermore$\hat { \Delta } ^ { M } X ^ { k } = X ^ { k } \otimes$1 for every$M$, the second condition in (8.39) really needs to be verified only for elements of the form$\mathcal { T } _ { k } ( \tau )$with $\tau \in \mathcal { F } _ { \star }$. The reason for introducing the quantity$\hat { \Delta } ^ { M }$and defining R in this way is that these conditions appear naturally in Theorem 8.44 below where we check that the renormalised model defined by (8.34) does again satisfy the analytical bounds of Definition 2.17.

We first verify that our terminology is not misleading, namely that R really is a group:

Lemma 8.43 If$M _ { 1 } , M _ { 2 } \in \Re$, then$M _ { 1 } M _ { 2 } \in \Re$. Furthermore, if$M \in \Re$, then $M ^ { - 1 } \in \Re$

Proof Note first that if$M = M _ { 1 } M _ { 2 }$then, due to the identity$\Pi ^ { M } = \Pi M _ { 1 } M _ { 2 }$ one obtains the model$( \boldsymbol { \Pi } ^ { M } , \boldsymbol { F } ^ { M } )$by applying the group element corresponding to$M _ { 2 }$to$( \boldsymbol { \Pi } ^ { M _ { 1 } } , \boldsymbol { F } ^ { M _ { 1 } } )$. As a consequence, one can “guess” the identities

$$
\Delta^ {M} = (I \otimes \mathcal {M}) \big (\Delta^ {M _ {1}} \otimes \hat {M} _ {1} \big) \Delta^ {M _ {2}},\tag{8.40a}
$$

$$
\hat {\Delta} ^ {M} = (I \otimes \mathcal {M}) \big (\hat {\Delta} ^ {M _ {1}} \otimes \hat {M} _ {1} \big) \hat {\Delta} ^ {M _ {2}},\tag{8.40b}
$$

$$
\hat {M} = \hat {M} _ {1} \hat {M} _ {2}.\tag{8.40c}
$$

Since we know that (8.35) characterises$\Delta ^ { M }$and$\hat { M }$, (8.40) can be verified by checking that$\Delta ^ { M }$and$\hat { M }$defined in this way do indeed satisfy (8.35). The identity (8.35c) is immediate, so we concentrate on the two other ones.

For (8.35a), we have

$$
\begin{array}{r l} & {\mathcal {M} (\mathcal {J} _ {k} \otimes I) \Delta^ {M} = \mathcal {M} \big ((\mathcal {J} _ {k} \otimes I) \Delta^ {M _ {1}} \otimes \hat {M} _ {1} \big) \Delta^ {M _ {2}}} \\ & {\qquad = \mathcal {M} \big (\hat {M} _ {1} \mathcal {J} _ {k} \otimes \hat {M} _ {1} \big) \Delta^ {M _ {2}}} \\ & {\qquad = \hat {M} _ {1} \mathcal {M} \big (\mathcal {J} _ {k} \otimes I \big) \Delta^ {M _ {2}} = \hat {M} _ {1} \hat {M} _ {2} \mathcal {J} _ {k},} \end{array}
$$

which is indeed the required property. Here, we made use of the morphism property of$\hat { M } _ { 1 }$to go from the second to the third line.

For (8.35b), we use (8.40a) to obtain

$$
\begin{array}{r l} & {(I \otimes \mathcal {M}) (\Delta \otimes I) \Delta^ {M} = (I \otimes \mathcal {M}) (\Delta \otimes I) (I \otimes \mathcal {M}) \big (\Delta^ {M _ {1}} \otimes \hat {M} _ {1} \big) \Delta^ {M _ {2}}} \\ & {\qquad = (I \otimes \mathcal {M}) \big ((M _ {1} \otimes \hat {M} _ {1}) \Delta \otimes \hat {M} _ {1} \big) \Delta^ {M _ {2}}} \\ & {\qquad = (M _ {1} \otimes \hat {M} _ {1}) (I \otimes \mathcal {M}) \big (\Delta \otimes I \big) \Delta^ {M _ {2}}} \\ & {\qquad = (M _ {1} \otimes \hat {M} _ {1}) (M _ {2} \otimes \hat {M} _ {2}) \Delta = (M \otimes \hat {M}) \Delta ,} \end{array}
$$

as required. Here, we used again the morphism property of$\hat { M } _ { 1 }$to go from the second to the third line. We also used the fact that, by assumption, (8.35b) holds for both$M _ { 1 }$and$M _ { 2 }$. Finally, we want to verify that the expression (8.40b) for $\hat { \Delta } ^ { M }$is the correct one. For this, it suffices to proceed in virtually the same way as for$\Delta ^ { M }$, replacing$\Delta$by$\hat { \Delta }$when needed.

To show that R is a group and not just a semigroup, we first define, for any $\boldsymbol { \kappa } \in \textbf { R }$, the projection$\mathcal { P } _ { \kappa } \colon \mathcal { H } _ { 0 } \to \mathcal { H } _ { 0 }$given by$\mathcal { P } _ { \kappa } \tau = 0 \ \mathrm { i f } \ | \tau | _ { \mathfrak { s } } > \kappa$and ${ \mathcal { P } } _ { \kappa } \tau = \tau \ \mathrm { i f } \ | \tau | _ { \mathfrak { s } } \leq \kappa$. We also write$\hat { \mathcal { P } } _ { \kappa } = \mathcal { P } _ { \kappa } \otimes I$as a shorthand. We then argue by contradiction as follows. Assuming that$M ^ { - 1 } \not \in \Re$, one of the two conditions in (8.39) must be violated. Assume first that it is the first one, then there exists$\mathrm { ~ a ~ } \tau \in \mathcal { F } _ { 0 }$and a homogeneity$\kappa \leq | \boldsymbol { \tau } | _ { \mathfrak { s } }$, such that$\Delta ^ { M ^ { - 1 } } \tau$can be rewritten as

$$
\Delta^ {M ^ {- 1}} \tau = R _ {-} ^ {M} \tau + R _ {+} ^ {M} \tau ,
$$

with$\hat { \mathcal { P } } _ { \kappa } R _ { - } ^ { M } \tau = R _ { - } ^ { M } \tau \neq 0 , \hat { \mathcal { P } } _ { \kappa } R _ { + } ^ { M } \tau = 0$, and$R _ { - } ^ { M } \tau \neq \tau \otimes { \bf 1 }$. We furthermore choose for κ the smallest possible value such that such a decomposition exists, i.e. we assume that$\hat { \mathcal { P } } _ { \bar { \kappa } } R _ { - } ^ { M } \tau = 0$for every$\bar { \kappa } < \kappa$

It follows from (8.40a) that one has

$$
\hat {\mathcal {P}} _ {\kappa} (\tau \otimes \mathbf {1}) = \hat {\mathcal {P}} _ {\kappa} \Delta^ {I} \tau = (I \otimes \mathcal {M}) \bigl (\hat {\mathcal {P}} _ {\kappa} \Delta^ {M} \otimes \mathcal {M} \hat {\Delta} ^ {M} \bigr) \Delta^ {M ^ {- 1}} \tau .
$$

Since, by Definition 8.41, the identity$\hat { \mathcal { P } } _ { \kappa } \Delta ^ { M } \bar { \tau } = \hat { \mathcal { P } } _ { \kappa } ( \bar { \tau } \otimes \mathbf { 1 } )$holds as soon as $| \bar { \tau } | _ { \mathfrak { s } } \geq \kappa$, one eventually obtains

$$
\hat {\mathcal {P}} _ {\kappa} (\tau \otimes \mathbf {1}) = R _ {-} ^ {M} \tau ,
$$

which is a contradiction. Therefore, the only way in which one could have $M ^ { - 1 } \notin$R is by violating the second condition in (8.39). This however can also be ruled out in almost exactly the same way, by making use of (8.40b) instead of (8.40a) and exploiting the fact that one also has$\hat { \Delta } ^ { \bar { I } } \tau = \tau \otimes { \bf 1 }$□

The main result in this section states that any transformation$M \in \Re$extends canonically to a transformation on the set of admissible models for$\mathcal { T } _ { F } ^ { ( r ) }$for arbitrary$r > 0$

Theorem 8.44 Let$M \in \Re$, where R is as in Definition 8.41, let$r > 0$be such that the kernel K annihilatespolynomials ofdegree r, and let$( \Pi , f ) \sim ( \Pi , \Gamma )$ be an admissible modelfor$\mathcal { T } _ { F } ^ { ( r ) }$with f and  related as in (8.29)

Define$\Pi _ { x } ^ { M }$and$f ^ { M }$on H and$\mathcal { H } _ { 0 } ^ { + }$as in (8.34) and define$\Gamma ^ { M }$via (8.29). Then,$( \Pi ^ { M } , \Gamma ^ { M } )$is an admissible modelfor$\mathcal { T } _ { F }$on$\mathcal { H } _ { 0 }$. Furthermore, it extends uniquely to an admissible modelfor all of$\mathcal { T } _ { F } ^ { ( r ) }$

Proof We first verify that the renormalised model does indeed yield a model for $\mathcal { T } _ { F }$on$\mathcal { H } _ { 0 }$. For this, it suffices to show that the bounds (2.15) hold. Regarding the bound on$\Pi _ { x } ^ { M }$, recall the first identity of (8.34). As a consequence of Definition 8.41, this implies that$( \Pi _ { x } ^ { M } \tau ) ( \dot { \varphi } _ { x } ^ { \lambda } )$can be written as a finite linear combination of terms of the type$( \Pi _ { x } \hat { \tau } ) ( \varphi _ { x } ^ { \lambda } )$with$| \bar { \tau } | _ { \mathfrak { s } } \geq | \tau | _ { \mathfrak { s } }$. The required scaling as a function of λ then follows at once.

Regarding the bounds on$\Gamma _ { x y }$, recall that$\Gamma _ { x y } \tau = ( I \otimes \gamma _ { x y } ) \Delta \tau$with

$$
\gamma_ {x y} = (f _ {x} \mathcal {A} \otimes f _ {y}) \Delta^ {+},\tag{8.41}
$$

and similarly for$\gamma _ { x y } ^ { M }$. Since we know that ( , ) is a model for$\mathcal { T } _ { F } ^ { ( r ) }$, this implies that one has the bound

$$
| \gamma_ {x y} \tau | \lesssim \| x - y \| _ {\mathfrak {s}} ^ {| \tau | _ {\mathfrak {s}}},\tag{8.42}
$$

and we aim to obtain a similar bound for$\gamma _ { x y } ^ { M }$. Recalling the definitions (8.41) as well as (8.34), we obtain for$\gamma _ { x y } ^ { M }$the identity

$$
\begin{array}{l} \gamma_ {x y} ^ {M} = (f _ {x} \mathcal {A} \otimes f _ {y}) (\mathcal {A} \hat {M} \mathcal {A} \otimes \hat {M}) \Delta^ {+} = (f _ {x} \mathcal {A} \otimes f _ {y}) (I \otimes \mathcal {M}) (\Delta^ {+} \otimes I) \hat {\Delta} ^ {M} \\ = (f _ {x} \mathcal {A} \otimes f _ {y} \otimes f _ {y}) (\Delta^ {+} \otimes I) \hat {\Delta} ^ {M} = \big (\gamma_ {x y} \otimes f _ {y} \big) \hat {\Delta} ^ {M}, \end{array}
$$

where the second equality is the definition of$\hat { \Delta } ^ { M }$, while the last equality uses the definition of$\gamma _ { x y }$, combined with the morphism property of$f _ { y }$. It then follows immediately from Definition 8.41 and (8.42) that the bound (8.42) also holds for$\gamma _ { x y } ^ { M }$

Finally, we have already seen that if ( , ) is admissible, then$\Pi _ { x } ^ { M }$and$f _ { x } ^ { M }$ satisfy the identities (8.31) and (8.32) as a consequence of (8.35a), so that they also form an admissible model. The fact that the model$( \Pi ^ { M } , \Gamma ^ { M } )$extends uniquely (and continuously) to all of$\mathcal { T } _ { F } ^ { ( r ) }$follows from a repeated application of Theorem 5.14 and Proposition 3.31.□

Remark 8.45 In principle, the construction of R given in this section depends on the choice of a suitable set$\mathcal { F } _ { 0 }$. It is natural to conjecture that R does not actually depend on this choice (at least if$\mathcal { F } _ { 0 }$is sufficiently large), but it is not clear at this stage whether there is a simple algebraic proof of this fact.

## 9 Two concrete renormalisation procedures

In this section, we show how the regularity structure and renormalisation group built in the previous section can be used concretely to renormalise (PAMg) and$( \Phi ^ { 4 } )$

## 9.1 Renormalisation group for (PAMg)

Consider the regularity structure generated by (PAMg) with${ \mathfrak { M } } _ { F }$as in Remark$8 . 8 , \beta = 2$, and$\alpha \in ( - \frac { 4 } { 3 } , - 1 )$. In this case, we can choose

$$
\mathcal {F} _ {0} = \{\mathbf {1}, \Xi , X _ {i} \Xi , \mathcal {I} (\Xi) \Xi , \mathcal {I} _ {i} (\Xi), \mathcal {I} _ {i} (\Xi) \mathcal {I} _ {j} (\Xi) \}, \qquad \mathcal {F} _ {\star} = \{\Xi \},
$$

where i and j denote one of the two spatial coordinates. It is straightforward to check that this set satisfies Assumption 8.33. Indeed, provided that $\alpha \in ( - \frac { 4 } { 3 } , - 1 )$, it does contain all the elements of negative homogeneity. Furthermore, all of the elements$\tau \in \mathcal { F } _ { 0 }$satisfy$\Delta \tau = \tau \otimes { \bf 1 }$, except for$\Xi \mathcal { T } ( \Xi )$ and$X _ { i } \Xi$which satisfy

$$
\Delta \big (\Xi \mathcal {I} (\Xi) \big) = \Xi \mathcal {I} (\Xi) \otimes \mathbf {1} + \Xi \otimes \mathcal {J} (\Xi), \quad \Delta X _ {i} \Xi = X _ {i} \Xi \otimes \mathbf {1} + \Xi \otimes X _ {i}.
$$

It follows that these elements indeed satisfy$\Delta \tau \in \mathcal { H } _ { 0 } \otimes \mathcal { H } _ { 0 } ^ { + }$, as required by our assumption.

Then, for any constant$C \in \mathbf { R }$and$2 \times 2$matrix$\bar { C } .$, one can define a linear map$M$on the span of$\mathcal { F } _ { 0 }$by

$$
\begin{array}{r} M \big (\mathcal {I} (\Xi) \Xi \big) = \mathcal {I} (\Xi) \Xi - C {\bf 1}, \\ M \big (\mathcal {I} _ {i} (\Xi) \mathcal {I} _ {j} (\Xi) \big) = \mathcal {I} _ {i} (\Xi) \mathcal {I} _ {j} (\Xi) - \bar {C} _ {i j} {\bf 1}, \end{array}
$$

as well as$M ( \tau ) = \tau$for the remaining basis vectors in$\mathcal { F } _ { 0 }$. Denote by$\Re _ { 0 }$the set of all linear maps M of this type.

In order to verify that$\Re _ { 0 } \subset \Re$as our notation implies, we need to verify that$\Delta ^ { M }$and$\hat { \Delta } ^ { M }$satisfy the property required by Definition 8.41. Note first that

$$
\hat {M} \mathcal {I} (\Xi) = \mathcal {I} (\Xi),
$$

as a consequence of (8.35a). Since one furthermore has$\hat { M } X _ { i } = X _ { i }$, this shows that one has

$$
(M \otimes \hat {M}) \Delta \tau = (M \otimes I) \Delta \tau ,
$$

for every$\tau \in \mathcal { F } _ { 0 }$. Furthermore, it is straightforward to verify that$( M \otimes I ) \Delta \tau =$ $\Delta M \tau$for every$\tau \in \mathcal { F } _ { 0 }$. Comparing this to (8.35b), we conclude that in the special case considered here we actually have the identity

$$
\Delta^ {M} \tau = (M \tau) \otimes \mathbf {1},\tag{9.1}
$$

for every$\tau \in \mathcal { F } _ { 0 }$. Indeed, when plugging$( 9 . 1 )$into the left hand side of (8.35b), we do recover the right hand side, which shows the desired claim since we already know that (8.35b) is sufficient to characterise$\Delta ^ { M }$. Furthermore, it is straightforward to verify that$\hat { \Delta } ^ { M } \mathcal { T } ( \Xi ) = \mathcal { T } ( \Xi ) \otimes \mathbf { 1 }$so that, by Remark 8.42, this shows that$M \in \Re$for every choice of the matrix$C _ { i j }$and the constant$\bar { C }$

Furthermore, this 5-parameter subgroup of R is canonically isomorphic to $\mathbf { R } ^ { 5 }$endowed with addition as its group structure. This is the subgroup$\Re _ { 0 }$that will be used to renormalise (PAMg) in Sect. 9.3.

## 9.2 Renormalisation group for the dynamical$\Phi _ { 3 } ^ { 4 }$model

We now consider the regularity structure generated by$( \Phi ^ { 4 } )$, which is our second main example. Recall from Remark 8.7 that this corresponds to the case where

$$
\mathfrak {M} _ {F} = \{\Xi , U ^ {n}: n \leq 3 \},
$$

$\beta = 2$and α$< - { \frac { 5 } { 2 } }$. In order for the relevant terms ofnegative homogeneity not to depend on α, we will choose$\alpha \in ( - \frac { 1 8 } { 7 } , - \frac { 5 } { 2 } )$. The reason for this strangelooking value$- { \frac { 1 8 } { 7 } }$is that this is precisely the value of$\alpha$at which, setting $\Psi \ = \ \mathcal { T } ( \Xi )$as a shorthand, the homogeneity of the term$\Psi ^ { 2 } \mathcal { T } ( \Psi ^ { 2 } \mathcal { T } ( \Psi ^ { 3 } ) )$ vanishes, so that one would have to modify our choice of$\mathcal { F } _ { 0 }$

In this particular case, it turns out that we can choose for$\mathcal { F } _ { 0 }$and$\mathcal { F } _ { \star }$the sets

$$
\begin{array}{c} \mathcal {F} _ {0} = \{\mathbf {1},   \Xi ,   \Psi ,   \Psi^ {2},   \Psi^ {3},   \Psi^ {2} X _ {i}, \mathcal {I} (\Psi^ {3}) \Psi , \mathcal {I} (\Psi^ {3}) \Psi^ {2}, \\ \mathcal {I} (\Psi^ {2}) \Psi^ {2}, \mathcal {I} (\Psi^ {2}), \mathcal {I} (\Psi) \Psi , \mathcal {I} (\Psi) \Psi^ {2}, X _ {i} \}, \quad \mathcal {F} _ {\star} = \{\Psi ,   \Psi^ {2},   \Psi^ {3} \} \end{array}\tag{9.2}
$$

where the index i corresponds again to any of the three spatial directions.

Then, for any two constants$C _ { 1 }$and$C _ { 2 }$, we define a linear map M on$\mathcal { H } _ { 0 }$by

$$
\begin{array}{c} {M \Psi^ {2} = \Psi^ {2} - C _ {1} {\bf 1},} \\ {M \big (\Psi^ {2} X _ {i} \big) = \Psi^ {2} X _ {i} - C _ {1} X _ {i},} \\ {M \Psi^ {3} = \Psi^ {3} - 3 C _ {1} \Psi ,} \\ {M \big (\mathcal {I} (\Psi^ {2}) \Psi^ {2} \big) = \mathcal {I} (\Psi^ {2}) \big (\Psi^ {2} - C _ {1} {\bf 1} \big) - C _ {2} {\bf 1},} \\ {M \big (\mathcal {I} (\Psi^ {3}) \Psi \big) = \big (\mathcal {I} (\Psi^ {3}) - 3 C _ {1} \mathcal {I} (\Psi) \big) \Psi ,} \\ {M \big (\mathcal {I} (\Psi^ {3}) \Psi^ {2} \big) = \big (\mathcal {I} (\Psi^ {3}) - 3 C _ {1} \mathcal {I} (\Psi) \big) \big (\Psi^ {2} - C _ {1} {\bf 1}) - 3 C _ {2} \Psi ,} \\ {M \big (\mathcal {I} (\Psi) \Psi^ {2} \big) = \mathcal {I} (\Psi) \big (\Psi^ {2} - C _ {1} {\bf 1} \big),} \end{array}\tag{9.3}
$$